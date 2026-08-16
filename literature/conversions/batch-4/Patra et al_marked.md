---
conversion_metadata:
  converted_at: "2026-07-21T08:06:01Z"
  converter_tool: "markitdown"
  converter_version: "0.1.6"
  source_pdf: "Patra et al.pdf"
  source_pdf_sha256: "889f4a1c27e19baea24a5e4aa59d88e4a308947d80a572241da3005ba6f3be32"
  page_count: 16
  markdown_char_count: 185689
---

<!-- PAGE-AWARE EXTRACTION (via pdfminer.six) -->

<!-- PAGE 1 -->

Engineering Research 
3048-880X 
Rademics Research Institute

https://doi.org/10.71443/er.ar16

AI-Driven Goal Based Financial Planning System: A Framework for Contextual 
Feasibility Validation

Bidisha Patra 1, Samadrita Sarkar 2, Sneha Pal 3, Sreejani Ghosh 4, Prof. Sujoy Datta 5

12345School of Computer Engineering, KIIT Deemed to be University, Bhubaneshwar, Odisha, India.

Article history 
Accepted: 18 December 
2025 
Keywords: 
Artificial Intelligence, 
Goal-Based Financial 
Planning, 
Feasibility Validation, 
Reinforcement Learning, 
Financial Forecasting, 
Context-Aware Systems.

Abstract 
In  the  wake  of  growing  complexity  in  financial  decision-making  and  the  ever-
changing economic environment, conventional financial planning strategies have 
proven  inadequate.  This  paper  presents  an  artificial  intelligence  (AI)  powered 
goal-based  financial  planning  system  with  contextual  feasibility  analysis  to 
improve  the  precision  and  responsiveness  of  financial  planning.  The  system 
combines  several  elements,  such  as  personal  financial  data  analysis,  machine 
learning for financial predictions, reinforcement learning for financial strategies, 
and  probabilistic  modeling  for  feasibility  validation.  A  holistic  framework  was 
proposed to model financial factors, including income, expenditure, savings, risk, 
and  market  dynamics,  into  a  single  framework  to  reflect  both  human  and 
environmental  factors.  Time-series  forecasting  models  are  used  for  financial 
predictions,  and  reinforcement  learning  for  investment  strategy  optimization. 
Monte Carlo simulation was used to assess various financial scenarios and assess 
the  feasibility  of  achieving  specific  financial  objectives.  The  tool  offers  tailored 
financial  plans,  feasibility  measures,  and  recommendations  to  help  make  more 
realistic and informed decisions. Empirical  experiments  show that the proposed 
system increases the accuracy of forecasts, adaptability, and more accurate goal 
feasibility evaluations than traditional rule-based approaches. The results indicate 
that  embedding  contextual  awareness  and  adaptive  learning  capabilities  in 
financial planning systems greatly enhances their performance. The study presents 
a scalable and smart approach that integrates predictive analytics with goal-based 
financial  planning,  which  can  be  applied  in  fintech  applications  and  personal 
financial advisors.

1. Introduction

Goal-based  financial  planning  represents  a  major  shift 
from  more  traditional  wealth  maximization  models  by 
focusing  on  tailoring  investment  strategies  to  achieve  life 
goals such as retirement, education, and asset acquisition [1]. 
Drawing on the insights of behavioral finance, this paradigm 
acknowledges  that  investment  decisions  are  not  purely 
rational  but  are  heavily  influenced  by  biases,  emotions,  and 
risk attitudes [2]. Pioneering theories of behavioral economics 
(Kahneman and Tversky) illustrate the impact of biases (such 
as loss aversion, anchoring, and overconfidence) on financial 
decision-making [3]. The literature also suggests that people

life-cycle

tend to compartmentalize financial goals and place different 
weights  of  importance  and  risk  appetite  on  each  goal,  thus 
undermining  the  homogeneity  assumptions  in  conventional 
investment 
[5].  The 
portfolio  optimization 
approaches indicate that investment goals and risk tolerance 
change  over 
tailored 
approaches  to  financial  planning  [4].  The  many  traditional 
systems  do  not  consider  dynamic  behavioral  factors  in 
addition  to  financial  data  streams,  leading  to  static,  often 
unrealistic  forecasts.  This  gap  suggests  a  need  for  smart 
systems capable of dynamically responding to both behavioral 
and financial factors to improve the realism and relevance of

time,  necessitating  flexible  and

Contact – ghoshsreejani@gmail.com

1

---

<!-- PAGE 2 -->

Bidisha Patra 1et al

2025, Vol 02. Issue 02

rebalancing  based  on  user-specified

goal-based financial planning within financial ecosystems [5]. 
Building  on  the  principles  of  goal-based  financial 
planning and behavioral finance, robo-advisory and FinTech 
platforms  are  a  technological  advancement  that  puts  these 
concepts  into  practice  through  automated,  data-driven,  and 
scalable  platforms  [6].  Services 
like  Betterment  and 
Wealthfront  are  examples  of  the  application  of  algorithmic 
portfolio  management,  passive  investment  approaches,  and 
automatic 
risk 
preferences  [7].  Prior  studies  show  that  these  systems 
primarily use Modern Portfolio Theory and exchange-traded 
fund  (ETF)  diversification  to  implement  efficient  asset 
allocation.  Though  robo-advisors  provide  benefits  such  as 
convenience, 
and  user-friendliness, 
frequently  rely  on  generic  risk  assessment  questionnaires, 
which fail to account for the nuanced preferences of users and 
changes in financial circumstances [8]. The tend to prioritize 
portfolio  optimization  over  assessing  the  achievability  of 
financial  goals.  This  results  in  a  gap  between  investment 
returns  and  achieving  financial  goals  [9].  While  recent 
developments in FinTech leverage machine learning and big 
data  to  improve  personalization,  there  are  still  many 
challenges to solving issues related to situational awareness, 
behavioral adaptability, and responsiveness. This suggests the 
need for more advanced systems that go beyond automation 
to provide integrated, goal-based financial planning [10].

cost-effectiveness,

Building on the advancements in robo-advisory, machine 
learning has emerged as a key element in financial forecasting, 
allowing the identification of patterns in high-dimensional and 
complex  financial  data  [11].  Historically,  statistical  models 
like  ARIMA  have  been  popular,  but  their  inability  to  cope 
with non-linear and non-stationary data has led to the adoption 
of  more  sophisticated  approaches  like  deep  learning.  For 
example,  Long  Short-Term  Memory  (LSTM)  networks, 
proposed by Sepp Hochreiter and Jürgen Schmidhuber, show 
effective  modeling  of  temporal  relationships  and  enhanced 
forecasting  performance  [12].  Ensemble  techniques  like 
random  forests  and  gradient  boosting  improve  the  model's 
stability  and  accuracy.  While  machine  learning  offers 
predictive  insights,  reinforcement  learning  builds  on  this 
approach  by  allowing  for  adaptive  decision-making  through 
interaction  with  the  dynamic  financial  environment  [13]. 
Building  on  basic  principles  outlined  in  reinforcement 
learning:  An  introduction:  Reinforcement  learning  models 
have  been 
into  portfolio  management, 
algorithmic  trading,  and  dynamic  allocation  [14].  These 
models  learn  and  adapt  strategies  over  time,  making  them 
well-adapted  to  dynamic  financial  environments.  But  issues 
related to reward function design, convergence, and volatility 
create difficulties in applying these models in practice [15].

incorporated

Expanding  on  the  adaptive  decision-making  abilities, 
models  for  feasibility  analysis  and  financial  goal  validation 
are essential to determining if the optimized strategies attain 
financial  goals  [16].  Existing  approaches  typically  involve 
deterministic assumptions about income growth, inflation, and 
investment  returns,  which  do  not  account  for  uncertainties. 
Modern methods increasingly use probabilistic methods, like 
Monte Carlo simulations, to quantify the chances of achieving 
financial  goals,  given  different  market  scenarios  [17].  The

models grounded in theories such as the Capital Asset Pricing 
Model (CAPM) use risk-adjusted expected returns for a better 
assessment.  But  the  success  of  these  models  of  validation 
largely relies on the quality of personal financial data analytics 
[18]. Insight into income, expenditure, savings, and debt was 
crucial  to  assessing  financial  status  and  potential.  The 
application of more sophisticated analytical methods such as 
clustering and predictive modeling also improves forecasting 
capabilities [19]. The issues such as data variability, privacy, 
and lack of behavioral considerations remain. As such, there 
was  a  need  for  more  integrated  approaches  that  integrate 
feasibility 
data-driven 
personalization [20].

validation  with

real-time

Combining  personal  financial  analytics  with  context-
aware artificial intelligence systems also adds flexibility and 
accuracy to personal financial plans. Unlike conventional AI 
systems that use static inputs, context-aware systems consider 
dynamic  multidimensional  factors  like  economic  changes, 
time,  user  activities,  and  events  to  offer  more  relevant  and 
specific recommendations [21]. The pioneering work of Mark 
Weiser  has  spawned  context-aware  computing,  which  has 
been applied to finance. The allow for real-time adaptations to 
market conditions and personal situations for more effective 
decision-making  [22].  This  ability  can  also  be  enhanced for 
risk measurement and portfolio management systems, which 
are based on classical financial theories such as the Modern 
Portfolio Theory (MPT) by Harry Markowitz and the Capital 
Asset  Pricing  Model  (CAPM)  by  William  F.  Sharpe.  These 
traditional  models  offer  a  robust  theoretical  framework,  but 
their  assumptions  restrict  them  in  a  dynamic  and  turbulent 
environment  [23].  Recent  research  using  machine  learning 
and  stochastic  modeling  tries  to  address  these  issues;  the 
incorporation  of  contextual  awareness  and  goal-based, 
personalized insights was still lacking [24]. This calls for the 
development of sophisticated and context-sensitive financial 
systems  that  link  risk  management  to  dynamic  goal-based 
financial planning [25].

2. Research gap

The literature has made substantial advancements in goal-
based  financial  planning,  robo-advisory  systems,  and  AI-
based  financial  predictions,  but  there  are  key  gaps  in  their 
integration  and  use.  Current  solutions  focus  primarily  on 
portfolio  management  and  forecasting  but  lack  dynamic 
financial  goal  feasibility  analysis.  The  tend  to  underuse 
behavioral  factors  and  real-time  contextual  information, 
leading to a lack of personalization and flexibility. Further, it 
was  not  common  to  see  the  integration  of  machine  learning 
learning  models  with  feasibility 
and/or  reinforcement 
analysis.  An 
that 
harmonizes  behavioral  factors,  real-time  financial  data 
analytics,  and  adaptive  decision-making  was  needed  to 
enhance the feasibility of achieving goals.

intelligent,  context-sensitive  system

3. Research methodology

Engineering Research

2

---

<!-- PAGE 3 -->

AI-Driven Goal Based Financial Planning System: A Framework for Contextual            2025, Vol 02. Issue 02

limitations of static models of financial planning by offering 
individuals' 
to 
dynamic,  goal-based  models  responsive 
financial situations and macroeconomic factors.

To  provide  a  robust  foundation  for  analysis,  relevant 
factors  in  financial  planning  were  identified  and  organized. 
Central financial variables such as income and expenses were 
complemented  with  other  variables  such  as  savings  and 
liabilities, behavioral and environmental factors such as risk 
aversion,  consumption  patterns,  and  external  economic 
parameters  [27].  These  factors  were  viewed  as  interrelated 
decision-making 
a  multi-dimensional 
elements 
environment,  allowing  a  more  comprehensive  portrayal  of 
personal financial attributes. Previous research has dealt with 
these  factors  individually;  the  present  formulation  stressed 
their interrelationship to improve the realism of the financial 
planning process.

in

In addition, the nature of financial decision-making in an 
uncertain environment calls for the problem to be formulated 
as  an  optimization  problem.  The  feasibility  of  financial 
objectives was formulated based on the time horizon, initial 
resources,  financial  markets,  and  personal  constraints.  The 
impact of uncertainty (e.g., in income and market prices) was 
also modeled. This problem formulation has allowed the use 
of  computational  methods  to  explore  different  financial 
scenarios  and  find  the  best  strategies  in  line  with  the  set 
objectives.

Lastly, the formulated problem enabled the creation of an 
AI-powered  system  with  the  potential  for  ongoing  learning 
and  evaluation.  Formulation  of  financial  planning  as  an 
optimization  problem  allowed  the  integration  of  predictive 
and  reinforcement  learning  approaches  with  probabilistic 
evaluations. This guaranteed that investment strategies were 
not only tailored to the optimum returns but also evaluated for 
their  suitability 
to  achieve  specific  objectives.  The 
formulation  of  the  financial  planning  problem  therefore 
provided  a  solid  theoretical  and  computational  basis  for  a 
context- and goal-driven financial planning system. 
Framework Design

FIGURE 1. Research methodology Flowchart

Problem Formulation

The  problem  statement  of  the  proposed  research  was 
based  on  the  need  to  create  an  intelligent  system  that  can 
harmonize  financial  plans  with  personal  life  goals.  Goal-
centered  financial  planning  was  defined  as  a  dynamic 
framework  where  financial  planning  was  based  on  the 
attainment  of  financial  goals  such  as  retirement  income, 
education funding, and wealth building [26]. Current methods 
were  seen  to  focus  on  maximizing  wealth  rather  than 
achieving goals, thus restricting their application. To counter 
this,  the  research  question  was  formulated  to  overcome  the

The system design was conceived to enable an intelligent 
and  scalable  system  to  tackle  complex  financial  planning 
problems in a layered approach. A hybrid AI architecture was 
envisaged, which involved three main layers: the data layer, 
the  AI  (artificial  intelligence)  layer,  and  the  decision  layer 
[28]. The data layer collected and organized various financial 
data, such as user financial data and macroeconomic data. The 
AI  layer  was  the  processing  layer,  where  adaptive  models 
were applied. The decision layer served as the output layer, 
providing an interface for creating actionable insights, making 
sure  that  the  system  process  its  analyses  and  translate  them 
into financial advice in line with users' objectives. 
  Within 
incorporated 
the  system,  we  strategically 
computational  methods  to  improve  its  analytical  prowess. 
Machine learning techniques were used to detect patterns in 
financial  behavior,  categorize  risk  tolerance,  and  predict 
critical 
income  and  spending. 
like 
Reinforcement  learning  techniques  were  used  to  facilitate 
dynamic  decision-making,  enabling  the  system  to  learn  and 
adjust  financial  strategies  in  response  to  feedback  and

financial

factors

Engineering Research

3

---

<!-- PAGE 4 -->

Bidisha Patra 1et al

2025, Vol 02. Issue 02

evolving circumstances. The data analytics components were 
employed  to  analyze  large  amounts  of  structured  and 
unstructured  financial  data  to  ensure  timely  insights  were 
extracted.  This  approach  enabled  a  holistic  analytical 
framework  to  support  predictive  and  prescriptive  financial 
planning.

A  key  feature  of  the  system  was  to  establish  a  data 
pipeline  between  the  various  components  of  the  system  to 
facilitate  communication  between 
inputs,  models,  and 
outputs.  Input  financial  data  was  collected,  processed,  and 
converted into structured data formats [29]. This transformed 
data  was  then  transferred  to  the  AI  layer  for  the  various  AI 
models to simultaneously produce predictions, classifications, 
and  optimizations.  The  outputs  of  these  models  were  then 
passed  to  the  decision  layer,  where  were  integrated  into 
meaningful  recommendations,  feasibility  assessments,  and 
insights.  This  structured  data  flow  provided  consistency, 
efficiency, and timeliness to the system.

The framework was designed to be modular, scalable, and 
flexible  to  support  changes  in  financial  use  cases  and  user 
needs. The  layers were designed to be  independent but also 
highly interconnected, enabling the seamless addition of new 
models  or  data  sources  without  impacting  the  system’s 
performance. This architecture enabled ongoing learning and 
evolution of the system to support changes in financial trends, 
market dynamics, and user behavior. This approach thus laid 
a  solid  groundwork  for  4uildingg  an  AI-enabled,  context-
aware financial service system that offered personalized and 
goal-based solutions. 
Data Collection & Preprocessing

such  as

information

The  data-gathering  phase  aimed  to  provide  a  solid 
foundation  for  the  development  of  the  AI-based  financial 
planning  system.  Data  was  collected  from  various  sources, 
including  user-specific 
income, 
expenditures, savings, investments, and debt data. Alongside 
personal  data,  macroeconomic  data,  including  inflation, 
interest rates, and market indices, were also gathered to reflect 
external  financial  factors  impacting  financial  planning  [30]. 
This mix of microeconomic and macroeconomic data allowed 
the system to capture both individual financial activities and 
macroeconomic  factors,  which  added  to  the  contextual 
understanding of the financial decision-making process.

After  collecting  the  data,  a  preprocessing  process  was 
implemented  to  enhance  data  quality.  Financial  data  can  be 
prone to missing entries, inconsistencies, and outliers, which 
affect  the  effectiveness  of  the  models.  To  resolve  these 
problems,  suitable  methods  were  employed  to  deal  with 
missing  values,  eliminate  outliers,  and  standardize  formats. 
Normalization techniques were applied to rescale variables to 
a  similar  range,  avoiding  undue  influence  of  any  specific 
variable on the models. The data transformation methods were 
applied  to  convert  non-numerical  and  temporal  data  into 
structured  data  formats  that  be  used  for  training  machine 
learning models.

The data preprocessing phase also included restructuring 
data  to  meet  the  needs  of  predictive  and  analytical  models. 
Time-based income and expense data were structured as time 
series to enable predictions. Data aggregation methods were 
transactional  data,  and 
used

to  create  summaries  of

segmentation  algorithms  were  used  to  segment  financial 
activities. This organization allowed for efficient training of 
models and enabled the system to better understand financial 
behaviors.

Next,  feature  extraction  was  applied  to  derive  relevant 
features that reflected critical aspects of financial  status and 
behavior  [31].  These  new  features  encompassed  cash  flow 
patterns,  savings  ratios,  spending  habits,  and  inferred  risk 
measures based on past financial transactions. These features 
provided  additional  information  about  a  person’s  financial 
stability and capacity, enabling better predictions and advice. 
Extraction  was  a  process  that  helped  convert  uninformative 
data  into  useful  features  that  improved  the  effectiveness  of 
machine 
learning  models, 
facilitating successful feasibility testing and decision-making 
in the proposed framework. 
AI Model Development

learning  and  reinforcement

learning

The  design  of  the  AI  models  phase  was  focused  on 
facilitating  prediction,  understanding,  and 
the 
behavior of the financial planning framework. Both predictive 
and intelligent models were developed to tackle the challenges 
of financial data and future uncertainties [32]. A primary focus 
was on the use of a combination of techniques to capture short 
and longer-term financial trends. This was the computational 
heart of the system in which insights were developed based on 
financial data to support goal-oriented financial planning and 
projections.

Time-series  models  were  created  to  predict  future 
financial  indicators  like  income,  expenses,  and  savings. 
Temporal models, such as Long Short-Term Memory (LSTM) 
networks,  were  employed  because  can  capture  the  temporal 
dependencies  and  handle  time-series  financial  data.  The 
regression  models  were  applied  to  model  relationships 
between financial variables and make continuous predictions. 
These  prediction  techniques  allowed  the  system  to  predict 
financial trends under different scenarios, thereby offering a 
predictive lens critical to assessing the feasibility of goals.

In  addition  to  forecasting,  machine  learning  techniques 
were applied for risk assessment and profiling. Classification 
techniques  were  used  to  classify  users  according  to  their 
financial  profiles,  spending  habits,  and  estimated  risk 
attitudes. Clustering algorithms also helped in the discovery 
of  user  clusters  with  similar  financial  profiles  [33].  This 
analytical  component  provided  insights  into 
individual 
financial  behavior  and  preferences,  enabling  the  system  to 
the 
recommendations  and  strategies  based  on 
make 
individual's risk tolerance and other characteristics. 
  We developed a reinforcement learning agent to support 
dynamic financial decision-making. The agent engaged with 
financial simulations and learned from rewards and penalties 
to  refine  its  strategies.  This  enabled  the  system  to  learn  the 
best actions to take under different circumstances, taking into 
account  both  user-specific  constraints  and 
investment 
conditions.  The  use  of  reinforcement  learning  improved  the 
system’s  adaptability  in  investment  strategy  to  ensure 
financial plans adapted to changing goals and circumstances. 
Feasibility Validation Framework

The  feasibility  validation  framework  was  designed  to 
validate  the  feasibility  of  achieving  set  financial  goals  in

Engineering Research

4

---

<!-- PAGE 5 -->

AI-Driven Goal Based Financial Planning System: A Framework for Contextual            2025, Vol 02. Issue 02

uncertain and dynamic settings. Financial goals were defined 
in  terms  of  short-,  medium-,  and  long-term,  with  each  time 
frame  having  its  own  set  of  priorities,  time  constraints,  and 
budgetary needs. Short-term goals were related to immediate 
needs such as cash reserves or minor expenses, while medium-
term  goals  were  associated  with  goals  such  as  education  or 
real  estate.  Long-term  goals  were  framed  as  retirement  and 
investment goals [34]. This categorization allowed the system 
to link financial planning strategies with time-bound goals and 
risk factors and have the goals assessed in the correct context. 
In order to test the influence of uncertainty on financial 
performance,  the  model  was  tested  using  Monte  Carlo 
simulations.  Various  simulations  were  created  by  adjusting 
parameters 
income  growth,  spending  variability, 
inflation,  and  returns.  This  resulted  in  a  distribution  of 
possible 
realistic 
uncertainty  in  economic  and  personal  factors.  Through 
iterative simulations, the system reflected the randomness of 
financial  markets  and  allowed  a  holistic  view  of  potential 
future conditions, rather than deterministic approaches.

financial  outcomes,  accounting

like

for

The  outcome  of  the  simulation  was  used  to  assess  the 
likelihood  of  achieving  financial  goals.  The  results  of  the 
simulations  were  statistically  analyzed 
the 
probability of achieving their target values within a given time 
period  [35].  Probability  distributions  were  developed  to 
capture the distribution and likelihood of outcomes, enabling 
a  quantitative  evaluation  of  financial  goals'  feasibility.  This 
approach allowed for the identification of risky goals and gave 
an  indication  of  the  extent  of  risk  involved  in  achieving 
financial goals.

to  assess

In  addition,  the  feasibility  validation  process  facilitated 
dynamic  assessment  and  adaptation  of  financial  plans.  The 
simulation step was periodically updated based on the latest 
data  or  financial  circumstances.  This  enabled  the  feasibility 
analysis to be up-to-date and for the system to suggest changes 
in savings, investment, or time frame for achieving the goals. 
The  combination  of  probabilistic  validation  and  dynamic 
updates  improved  the  realism  and  accuracy  of  financial 
planning,  enabling  the  framework  to  be  applied  to  context-
specific and personalized financial planning. 
Evaluation & Validation

The  evaluation  and  validation  phase  was  undertaken  to 
evaluate the accuracy, robustness, and effectiveness of the AI-
based  financial  planning  system.  We  took  a  structured 
approach  to  assess  the  performance  of  the  models  in 
forecasting  financial  variables  and  aiding  decisions.  The 
evaluation was done at both the model and system levels [36]. 
Performance  measures  such  as  accuracy,  error,  and 
computational  time  were  used  to  assess  the  accuracy  of 
prediction models and classification algorithms. This stage of 
the evaluation ensured the system satisfied the quality criteria 
for financial systems.

For  a  valid  comparison,  our  system  was  benchmarked 
against conventional financial planning approaches, which are 
based  on  static  forecasts  and  rule-based  decision-making 
heuristics. Traditional methods often relied on static growth 
assumptions  and  deterministic  calculations  and 
lacked 
personalized  recommendations,  leading  to  less  flexible

financial  plans.  The  AI-based  approach  involved  dynamic 
variables,  predictive  algorithms,  and  learning  mechanisms. 
Analysis  compared  the  flexibility,  adaptability,  and  tailored 
recommendations of the two approaches. This resulted in the 
benefits  of 
the  new  approach  being  highlighted  for 
overcoming issues with the old models.

The  system's  feasibility  results  were  validated  to  assess 
the  system's  prediction  of  goal  attainment.  The  system 
provided  information  on  the  probability  of  results  obtained 
from  simulations,  which  were  tested  to  establish  if  were 
consistent with actual financial scenarios. Sensitivity testing 
was  conducted  to  assess  the  impact  of  changes  to  input 
variables  on  feasibility  outcomes  and  ensure  accuracy  and 
consistency  [37].  This  analysis  verified  that  the  system 
accurately  predict  the  probability  of  meeting  financial 
objectives  in  various  scenarios,  thus  enhancing  trust  in  the 
system's analysis capabilities.

Further,  the  validity  of  the  recommendations  was 
assessed  to  validate  their  usefulness  and  applicability.  The 
capability of the system to provide suitable financial advice, 
such as modifying savings rates, investment portfolios, or time 
frames  of  the  goals,  was  assessed  based  on  improved 
outcomes  and  user  preferences.  This  ensured  that  the 
recommendations  were  effective  both  theoretically  and 
practically. In this phase, the validity of the proposed approach 
was confirmed as it was able to provide accurate predictions, 
feasible  feasibility  evaluations,  and  valuable  financial 
recommendations. 
Result Analysis & Output

The result analysis and output process aimed to transform 
computational results into financial recommendations in line 
with  users'  goals.  Using  the  system's  predictions,  behavior 
assessments, and feasibility predictions, financial plans were 
developed [38]. These plans took into account personal factors 
such as income, spending habits, risk profile, and time frame. 
This combination allowed the financial plans to be based on 
realistic scenarios and personal preferences. The results were 
presented  in  a  format  that  offered  recommendations  on 
savings and investment options and prioritization of financial 
goals, thus improving the usefulness of the plans.

The system not only produced the financial plans, but it 
also provided feasibility scores that indicated the probability 
of success for each financial goal. These were  based on the 
results  from  the  probabilistic  simulations  and  predictive 
modeling, providing a quantitative measure of success under 
different scenarios [39]. Besides feasibility scores, the system 
also  provided  recommendations  to  enhance  the  chance  of 
achieving goals. These suggestions involved changing savings 
levels, changing investment strategies, and changing the time 
frame  to  achieve  the  goal.  The  combination  of  scores  and 
recommendations  facilitated  an  informed  decision-making 
process.

Data  interpretation  was  done  to  make  the  output  of  the 
analysis easy to understand and meaningful. As such, financial 
results  were  examined  in  terms  of  assumptions  used,  model 
forecasts,  and  other  factors  affecting  performance  (such  as 
market  forces  and  human  behavior).  This  analysis  layer 
allowed  us  to  understand  what  factors  contributed  to  the

Engineering Research

5

---

<!-- PAGE 6 -->

Bidisha Patra 1et al

2025, Vol 02. Issue 02

success or failure of financial objectives and to gain insights 
into  financial  performance.  The  system 
the 
transparency  of  outcomes  through  the  connection  to  factors 
and informed financial decision-making.

improved

iterative

In  addition,  the  analysis  phase  helped  to  identify 
opportunities for improvement in the financial strategies and 
in  feasibility  scores  and  other 
system.  Discrepancies 
indicators were analyzed for inefficiencies or risks. In light of 
this, 
improvements  were  proposed,  such  as 
adjustments to the strategy and model. The iterative process 
ensured  that  the  system  was  dynamic  and  able  to  adapt  to 
prevailing financial conditions—thereby enhancing its ability 
to  provide  accurate  and  targeted  financial  planning  systems 
[40].

4. Result and discussion

FIGURE 2. Monthly Income–Expense

Dynamics and Financial Behavior Analysis

financial  practices  and  cash

The  graph  shown  was  a  comparative  view  of  monthly 
income  and  expenses  over  a  year,  offering  essential 
information  about 
flow 
management. The income graph shows significant variations, 
with  peaks  around  the  third  and  seventh  months  suggesting 
increased income during these periods. The expenditure curve 
was  relatively  diverse,  with  some  months  showing  higher 
expenses. The disparity between income and expenses reflects 
the dynamic nature of financial circumstances and the need for 
ongoing monitoring in smart financial planning systems.

Upon closer inspection, it appears that in some months, 
expenses are close to or at times even exceed income, as in the 
second and third months. These trends suggest potential cash 
flow challenges or less savings potential in these months. On 
the other hand, months with a larger disparity between income 
and  expenses  (seventh  and  eighth  months)  indicate  greater 
savings  capacity  and  enhanced  financial  well-being.  Such 
variability was vital in examining dynamic financial patterns 
and plays a key role in determining surplus and deficit periods 
in a planning model.

From a modeling point of view, these income and expense

fluctuations  highlight  the  need  to  include  time  series 
forecasting  models  and  learning  systems.  Assumptions  of 
income constancy or constant percentages of income spent on 
various  expenses  not  account  for  these  variations.  The 
forecasting techniques like LSTM can learn these dynamics, 
while  reinforcement  learning  processes  can  adapt  financial 
strategies to these changes. This keeps financial advice up-to-
date with the client's financial circumstances.

The  graph  was  a  starting  point  for  the  feasibility 
assessment  and  decision-making  process.  The 
income-
expense gaps observed in the graph affect savings, which play 
a  crucial  role  in goal  attainment.  Reduced  savings  lead  to a 
decreased likelihood of reaching financial goals, while excess 
savings can be used to optimize investments. By considering 
these  behavioral  insights  in  the  system  analysis,  the  system 
can  provide  more  realistic  feasibility  scores  and  tailored 
suggestions,  which  can  improve  the  financial  planning 
process.

Table 1. Monthly Income and Expense Data

Month

1 
2 
3 
4 
5 
6 
7 
8 
9 
10 
11 
12

Income 
56000 
41000 
78000 
51000 
46000 
57000 
77000 
62000 
56000 
42000 
41000 
43000

Expenses 
25000 
58000 
59000 
37000 
40000 
49000 
26000 
47000 
46000 
39000 
38000 
23000

Savings 
31000 
-17000 
19000 
14000 
6000 
8000 
51000 
15000 
10000 
3000 
3000 
20000

Table  1  shows  the  monthly  distribution  of  income, 
expenses, and savings, offering an overview of the cash flow 
in  the  period  considered.  This  table  shows  that  there  was 
considerable  variation  in  income  and  expenses,  suggesting 
that the financial circumstances were not constant throughout 
the  months.  Income  varied  from  as  low  as  approximately 
41,000  to  as  high  as  78,000,  and  expenses  also  exhibited 
variations.  This  highlights  that  cash  flows  were  subject  to 
varying  factors  and  must  be considered  together rather  than 
individually. The calculated savings column, representing the 
balance between income and expenses, was a crucial measure 
of financial well-being and surplus.

From  the  table,  we  can  see  instances  of  surplus  and 
deficit.  For  instance,  the  second  month  shows  a  deficit  in 
savings (negative value), implying either financial distress or 
the need to draw on additional resources. On the other hand, 
the seventh and first months displayed high positive savings, 
indicating financial fortitude in those months. This variation 
underscores the variability of financial resiliency and the need 
to focus on potential risk periods where financial interventions 
are needed.

Engineering Research

6

---

<!-- PAGE 7 -->

AI-Driven Goal Based Financial Planning System: A Framework for Contextual            2025, Vol 02. Issue 02

The  monthly  differences  in  savings  also  highlight  the 
effects of income minus expense on financial stability. Periods 
of  higher  income  and  lower  expenses  lead  to  substantial 
surplus savings, while moderate income levels lead to lower 
savings  when  expenses  are  high.  This  reflects  that  while 
income  was  important  for  financial  stability,  it  was  also 
important  to  keep  expenses  low.  The  interaction  of  these 
factors  offers  insights  into  the  decision-making  process, 
spending behavior, and savings discipline.

In terms of analysis, the figures in the  table represent a 
key  part  of  the  data  set  used  for  prediction  modeling  and 
feasibility studies. The variability in the data suggests the use 
of time-series analysis and dynamic financial planning, as the 
latter not account for such variations. The savings figures, in 
particular,  are  a  critical  input  to  assess  the  feasibility  of 
financial  objectives.  Leveraging  these  insights  in  analytical 
models will yield better forecasts and feasible financial plans, 
leading to better decision-making and financial security.

analysis, the savings' variability also stresses the importance 
of  adaptable  and  predictive  models.  Conventional  financial 
strategies, which rely on steady savings rates, not account for 
this variability. Time series forecasting techniques can detect 
these  trends,  while  adaptive  learning  techniques  can  make 
dynamic 
investment 
strategies.

recommendations

for  savings  or

This  allows  the  system  to  adapt  to  financial  turbulence 
and  stay  on  track  towards  financial  goals.  In  addition,  the 
savings trend was an essential element of the decision-making 
process  and  feasibility  analysis.  Negative  and  low  savings 
periods  affect  the  feasibility  of  financial  plans  and  goals, 
whereas  high  savings  increase  their  chance  of  success.  By 
considering  these  trends  in  probabilistic  modeling,  more 
accurate  feasibility  index  scores  can  be  obtained.  The 
information  gleaned  from  this  graph  can  be  used  to  inform 
individual financial plans, making sure recommendations are 
in  line  with  the  financial  realities  of  consumers'  changing 
circumstances.

FIGURE 3. Monthly Savings Variability and

Financial Stability Assessment

The variation in savings was depicted in the graph, which 
measures  the  difference  between  income  and  expenses  for 
each month over a year. There was considerable variation in 
savings,  including  a  negative  value  in  the  second  month, 
which suggests a deficit in which expenditure was greater than 
income.  The  fluctuation  underscores  the  volatile  nature  of 
individual  financial  circumstances  and  the  need  for  regular 
monitoring of savings patterns.

The  switching  signs  for  savings  reflect  the  balance 
between income and spending and are an essential measure to 
assess financial performance. Upon closer inspection, we see 
that savings have reached a peak around the seventh month, 
which  indicate  a  month  where  one  experienced  a  financial 
surplus.  This  was  a  time  when  investment  opportunities  be 
seized and/or financial goals be achieved more rapidly. On the 
other hand, negative savings earlier in the year and/or reduced 
savings later in the year imply periods of financial deficit or 
diminishing opportunities for wealth building.

Such  variability  was  crucial  for  analyzing  the  temporal 
allocation  of  financial  resources  and  for  pinpointing  times 
when  corrective  financial  measures  be  needed.  In  terms  of

FIGURE 4. Monthly Income Distribution and

Cash Flow Variability Analysis

The bar chart shows the monthly income distribution in a 
year, with variations in income. The insights provided by this 
data  indicate  that  the  income  was  not  stable,  with  higher 
values in the third and seventh months and lower values in the 
second,  tenth,  and  eleventh  months.  This  suggests  non-
stability, rather than stability, of income streams, which was 
an  important  consideration  in  financial  decision-making. 
These  variations  be  due  to  factors  like  incentive-based 
income,  seasonality,  or  economic  factors,  which  must  be 
considered in smart financial systems.

An in-depth analysis of the graph reveals that peak values 
generate  surplus  while  dips  in  income  limit  cash  flow.  For 
example, the higher values in mid-year suggest an increase in 
cash  flow  and  thus  surplus,  while  the  depressions  in  later 
months  suggest  a  decrease  in  cash  flow,  limiting  financial 
flexibility. For example, the peaks seen in mid-year highlight 
the  potential  for  higher  savings  and  investments,  while  the

Engineering Research

7

---

<!-- PAGE 8 -->

Bidisha Patra 1et al

2025, Vol 02. Issue 02

troughs in the subsequent months reflect lower cash inflows, 
which impact cash flow. This pattern of income suggests the 
need  for  financial  planning  that  was  able  to  adjust  to 
variability in cash inflows, as opposed to assuming a constant 
level of income.

In terms of modeling, the observed income  fluctuations 
highlight the need to use time series forecasting models in the 
analysis. Time-series models like LSTM are able to learn and 
predict  future  income  trends  from  past  data.  Such  forecasts 
allow  for  forward-looking  planning,  taking  into  account 
strategies  accordingly.  The 
variations  and  adapting 
incorporation of such information with other factors, such as 
behavioral and contextual information, improves the ability to 
provide relevant, realistic financial advice.

The understanding how income distributions impact the 
ability to achieve financial goals was crucial. Fluctuations in 
income  affect  savings  and  investment  capacities,  both  of 
which  are  crucial  in  achieving  financial  goals.  These 
variations  can  be  factored  into  models  for  validating 
feasibility to provide more reliable estimates of the likelihood 
of success. This graph provides insights that can be  used to 
develop flexible financial planning strategies that are in line 
with real-time income variability to enhance decision-making 
and financial stability.

FIGURE 5. Savings–Investment Allocation

Patterns and Financial Decision Dynamics

The  graph  illustrates  a  comparison  of  monthly  savings 
and 
the  distribution  of  financial 
investment,  showing 
resources.  There  was  a  clear  variability  in  both  parameters, 
where savings are highly variable, including a negative saving 
in one month, and investments are quite stable but variable. 
This  difference  suggests  that  investment  was  not  always 
directly related to savings and that other factors (such as short-
term planning or psychological factors) come into play. The 
disparity  between  savings  and  investment  highlights  the 
dynamics of financial behavior, in which individuals can still 
invest low or negative savings.

A  deeper  look  into  the  data  shows  some  months  where 
increased savings were associated with increased investment,

such as in the sixth and seventh months. These were months 
of  positive  financial  circumstances  with  excess  funds 
available for investment purposes. In contrast, in months with 
lower  (or  negative)  savings,  investment  did  not  decrease 
accordingly,  suggesting  the  use  of  previous  savings,  other 
sources  of  funds,  or  planned  investment  amounts.  This 
represents  a  risk  factor,  as  ongoing  investment  during  low 
savings months can impact cash flow and liquidity.

From  a  modeling  perspective,  the  savings-investment 
variability highlights the need for incorporating adaptive and 
intelligent decision-making. Conventional financial strategies 
that rely on fixed savings-investment relationships not capture 
the  variability.  Savings  and  investment  relationships  can  be 
learned  in  adaptive  models,  such  as  reinforcement  learning, 
which  adapt  to  financial  circumstances  and  long-term 
financial  goals.  This  allows  more  realistic  and  contextual 
financial  advice  and  better  matching  of  financial  advice  to 
current financial resources and long-term objectives. 
  What's  more,  the  interdependence  between  savings  and 
investment was important to achieve long-term financial goals 
and  determine  the  possibility  of  achieving  financial  goals. 
Optimal  investing  during  high-savings  periods  can  enhance 
the  chances  of  attaining  financial  goals,  whereas  poor 
investment  during  low-savings  periods  can  lead  to  financial 
risk.  This  can  be  used  to  inform  feasibility  models  to  make 
more  accurate  predictions  and  recommendations.  The  graph 
analysis  supports  the  creation  of  well-rounded  and  flexible 
financial strategies, which consider the financial capacity and 
dynamic changes in the financial market.

Table 2. Savings and Investment Allocation

Month 
1 
2 
3 
4 
5 
6 
7 
8 
9 
10 
11 
12

Savings 
31000 
-17000 
19000 
14000 
6000 
8000 
51000 
15000 
10000 
3000 
3000 
20000

Investment 
18000 
21000 
34000 
13000 
33000 
27000 
25000 
46000 
36000 
12000 
14000 
34000

The  monthly  allocation  of  savings  and  investment  was 
shown in Table 2, providing a glimpse of how surplus funds 
were  used  over  the  year.  The  table  reveals  that  savings 
fluctuated considerably, with a negative value  in the second 
month,  whereas  investment  fluctuated  less  but  at  a  higher 
level. This discrepancy indicates that investment activity was 
not  exclusively  driven  by  available  savings  but  can  also  be 
explained by other factors such as previous savings, ongoing 
investments,  or  financial  planning  strategies.  The  table 
illustrates  the  intricacies  of  financial  decision-making,  in 
which  investment  trends  do  not  necessarily  correspond  to

Engineering Research

8

---

<!-- PAGE 9 -->

AI-Driven Goal Based Financial Planning System: A Framework for Contextual            2025, Vol 02. Issue 02

savings.

An examination of individual months shows that in some 
months,  investment  was  positively  associated  with  savings 
(third, seventh, and twelfth months). These months represent 
times when positive financial situations allowed for increased 
funds  to  be  allocated  to  investment.  But  in  months  where 
savings  were  lower  or  negative  (e.g.,  the  second  month), 
investment  was  still  high.  This  suggests  the  possibility  of 
using accumulated savings or adhering to pre-set investment 
plans,  allowing  investment  activity  to  continue  short-term 
cash  flow  issues.  This  practice  pose  liquidity  risks  over  the 
long term if not supported by sufficient savings.

The  savings-investment  nexus  highlights  the  need  for 
financial development and security. While investment during 
long-term  savings, 
high-savings  periods  contributes 
investing during low-savings periods result in financial stress. 
This  disalignment  suggests  the  need  for  dynamic  financial 
strategies that respond to the current financial situation. These 
numbers  show  the  need  for  allocation  to  be  monitored  in 
relation to both balance and goals to maintain sustainability.

to

In terms of modeling and analysis, the insights shown in 
the  table  highlight  the  need  for  smart  investment  strategies. 
Static  models  assuming  a  constant  ratio  of  savings  to 
investment not be able to account for such patterns. Rather, 
dynamic  models  such  as  reinforcement  learning  can  be 
applied  to  learn  allocation  policies  in  response  to  financial 
situations  and  long-term  objectives.  By  considering  these 
patterns  in  the  feasibility  study,  we  can  better  estimate 
financial results while ensuring that the investment strategies 
are consistent with risk preferences and financial constraints.

range  implies  that  most  months  involved  mid-level  income, 
with  a  lower  frequency  of  very  high  values  suggesting 
occasional  high  income.  This  pattern  reflects  the  variable 
nature of income generation and the need to consider income 
patterns instead of just the average income.

Upon  inspection,  the distribution  of  income  values  was 
not even, with clusters of values around particular ranges. The 
clusters  show  that  there  were  periods  of  relative  stability  in 
income,  while  the  outliers  in  the  higher  ranges  reflect 
occasional  increases.  This  due  to  bonuses,  incentives,  or 
market conditions. The variability in this distribution implies 
that income was not a stable quantity, and financial planning 
algorithms need to take into account the regularity of moderate 
income together with the possibility of high-income events. 
that  probability-based 
suggests 
approaches ought to be used in financial analysis. Rather than 
assuming income was a constant or certain value, by modeling 
income as a distribution, we can better predict future income 
and  generate  scenarios.  These  distributions  can  be  used  to 
enhance  predictions  in  machine  learning  models  and  to 
incorporate  uncertainty  in  simulation-based  analysis.  This 
helps  to  incorporate  uncertainty  and  inform  better  decision-
making.

The  distribution

The  income  distribution  plays  a  significant  role  in 
financial outcomes such as savings and wealth accumulation. 
Over-represented  mid-income  levels  restrict  the  potential  to 
consistently generate surpluses, while periods of high incomes 
investment 
enhance 
can  dramatically 
opportunities.  Understanding 
and 
incorporating them into validation of financial feasibility can 
lead  to  better  projections  of  financial  feasibility.  This 
histogram provides information for building flexible strategies 
to adapt financial planning to likely sources of earnings and 
risk.

and 
savings 
these  distributions

𝑆𝑡 = 𝐼𝑡 − 𝐸𝑡 − 𝐶𝑡                              [1]

where  C_t  =  contextual  adjustments  (inflation  impact,

unexpected events)

Savings  at  the  time  were  modeled  not  only  as  the 
difference between income and expenses but also adjusted for 
contextual factors such as inflation, emergencies, or economic 
shocks.  This  formulation  improved  realism  by  capturing 
external influences that directly affect disposable income. It 
ensured  that  savings  estimation  reflected  actual  financial 
conditions rather than idealized assumptions.

FIGURE 6. Income Distribution and

𝑋𝑡 = [𝐼𝑡, 𝐸𝑡, 𝑆𝑡, 𝑅𝑡, 𝐵𝑡, 𝑀𝑡]                       [2]

Frequency-Based Financial Stability Analysis

the

The  histogram  below  shows  the  frequency  of  income 
time  period  and  provides  a  visual 
values  over 
representation  of  how  many  values  fall  into  each  income 
range.  The  frequency  values  indicate  that  income  spans  a 
range of values, specifically mid-to-high income levels. The 
relatively  higher  concentration  of  values  in  the  lower  mid-

where 
R_t = risk profile, 
B_t = behavioral factors, 
M_t = market conditions

The  financial  state  at  the  time  was  represented  as  a 
multidimensional vector combining financial, behavioral, and 
contextual variables. This formulation enabled the system to 
process  heterogeneous  inputs  simultaneously,  forming  the 
foundation  for  machine  learning  and  reinforcement  learning

Engineering Research

9

---

<!-- PAGE 10 -->

Bidisha Patra 1et al

2025, Vol 02. Issue 02

models.  It  ensured  that  decision-making  incorporated  a 
holistic view of the user’s financial environment.

𝑊𝑡+1 = 𝑊𝑡 + 𝑆𝑡 + 𝐴𝑡 ⋅ 𝑟𝑡                  [3]

where 
A_t = investment allocation, 
r_t = return rate 
  Wealth evolution was modeled as a function of savings 
and 
investment  returns.  This  equation  captured  how 
accumulated savings and investment decisions contributed to 
future  wealth.  The  inclusion  of  returns  introduced  growth 
dynamics, enabling the system to simulate long-term financial 
trajectories required for goal achievement.

𝑌̂𝑡+1 = 𝑓𝜃(𝑋𝑡)                                [4]

where f_θ represents a trained ML model (e.g., LSTM)

Future  financial variables such as income  and expenses 
were  predicted  using  a  parameterized  function  learned  from 
historical data. This formulation generalized forecasting using 
machine  learning  models.  It  allowed  the  system  to  adapt  to 
non-linear  patterns  and  temporal  dependencies,  improving 
traditional  statistical 
prediction  accuracy  compared 
approaches.

to

max
𝜋

𝑇
 𝔼 [∑ 𝛾𝑡
𝑡=0

(𝑟𝑒𝑤𝑎𝑟𝑑)]               [5]

𝑅𝑡

where 
π = policy, 
γ = discount factor

The  decision-making  process  was

framed  as  a 
reinforcement  learning  problem,  where  the  objective  was  to 
maximize  cumulative  rewards  over  time.  Rewards  were 
defined  based  on  goal  progress,  risk  control,  and  financial 
stability.  This 
formulation  enabled  adaptive  strategy 
optimization through continuous learning and feedback.

𝐹𝑡 = 𝜎 (𝛼

𝑊𝑡
𝐺

+ 𝛽𝑆𝑡 + 𝛾𝑅𝑡 + 𝛿𝑀𝑡)        [6]

where 
G = goal target, 
σ = sigmoid function

The feasibility of achieving a financial goal was modeled 
as  a  normalized  score  between  0  and  1.  The  equation 
combined  wealth  progress,  savings  capacity,  risk  level,  and 
market 
ensured 
interpretability  by  converting  outputs  into  probability-like 
values. This formulation directly supported decision-making 
and user feedback.

conditions.  The

function

sigmoid

𝑊𝑡+1

(𝑖) = 𝑊𝑡 + 𝑆𝑡 + 𝐴𝑡 ⋅ 𝑟𝑡

(𝑖)         [7]

Multiple scenarios were generated by varying return rates

based on stochastic distributions. This enabled simulation of 
diverse  financial  futures  under  uncertainty.  The  approach 
provided a robust mechanism to evaluate possible outcomes 
rather than relying on single deterministic projections.

𝑃(𝐺) =

1
𝑁

𝑁

∑ 𝕀

𝑖=1

(𝑖) ≥ 𝐺)                [8]

(𝑊𝑇

where I was an indicator function

The  probability  of  achieving  a  financial  goal  was 
computed as the proportion of simulated scenarios where final 
wealth  exceeded  the  target.  This  probabilistic  formulation 
provided a realistic measure of success likelihood, supporting 
informed financial decisions.

𝐴𝑡 = 𝜋(𝑋𝑡) = 𝜆1𝑆𝑡 + 𝜆2𝑅𝑡 + 𝜆3𝑀𝑡         [9]

Investment  allocation  was  determined  using  a  policy 
function  dependent  on  savings,  risk  tolerance,  and  market 
conditions.  The  weights  controlled  the  influence  of  each 
factor.  This  formulation  enabled  dynamic  and  personalized 
allocation strategies aligned with both financial capacity and 
external conditions.

𝐿(𝜃) =

1
𝑛

𝑛
2
∑(𝑌𝑖 − 𝑌̂𝑖)
𝑖=1

+ ‖𝜆‖‖𝜃‖2                            [10]

A regularized loss function was used to train predictive 
models,  balancing  accuracy  and  model  complexity.  The 
additional regularization term prevented overfitting, ensuring 
that the model generalized well to unseen financial data. This 
improved reliability in forecasting and decision-making.

FIGURE 7. Risk Score Distribution and

Investor Behavior Profiling

The  histogram  shows  the  effect  of  variability  in  risk 
tolerance  levels  by  depicting  the  distribution  of  risk  scores 
over time. The distribution of values along the scale suggests 
risk  attitudes  were  not  narrowly  focused  but  included  low,

Engineering Research

10

---

<!-- PAGE 11 -->

AI-Driven Goal Based Financial Planning System: A Framework for Contextual            2025, Vol 02. Issue 02

moderate, and high levels. The concentration of values in the 
lower  and  middle  ranges  indicates  that  more  individuals 
tended to exhibit low- to moderate-risk preferences rather than 
higher-risk scores. This reflects the range of financial attitudes 
and suggests the need to account for different risk preferences 
in financial analyses.

Further  analysis  of  the  distribution  shows  that  attitudes 
towards risk varied over time. The lower scores correspond to 
periods of caution, perhaps reflecting a response to uncertain 
financial conditions or less stable earnings. On the other hand, 
the  higher  scores  indicate  periods  of  heightened  financial 
decision-making  confidence,  which  attributed 
to  more 
positive circumstances such as greater income or the ability to 
save.  This  finding  highlights  the  dynamic  nature  of  risk 
tolerance,  which  can  shift  based  on  both  financial  and 
economic circumstances.

For

the  modeling  part,

this  variability  suggests 
incorporating  adaptive  risk  classification  methods.  While 
traditional  methods  of  risk  classification  not  capture  these 
variations,  machine  learning  can  classify  and  update  risk 
status  based  on  financial  variables.  This  dynamic  approach 
improves financial advice accuracy by tailoring it to observed 
behaviors. The risk variability in models enhances decision-
making outcomes by considering uncertainty in risk behavior. 
The distribution of risk scores was essential in financial 
strategizing  and  achieving  goal  feasibility.  Conservative 
strategies  can  be  executed  with  lower  risk  preferences, 
potentially stunting growth in the long term, whereas higher 
risk  preferences  can  be  reflective  of  more  aggressive 
investment strategies, which have greater potential returns but 
with higher risks. Incorporating these trends into the analytical 
and validation framework can ensure that financial strategies 
are  tailored  to  individual  preferences  and  abilities.  The 
information  obtained  from  this  graph  helps  to  inform  more 
individualized,  contextualized,  and  realistic  financial  advice 
and promote adaptability.

Table 3. Risk Score Distribution

Month 
1 
2 
3 
4 
5 
6 
7 
8 
9 
10 
11 
12

Risk Score 
2.1 
1.5 
3.8 
4.5 
5.2 
6.0 
7.5 
8.2 
9.0 
2.8 
3.5 
4.2

conservative  financial  strategy,  and  the  progressive  increase 
in the latter months suggests a shift towards a more risk-prone 
strategy. This shows that financial  decisions are affected by 
dynamic  factors,  rather  than  being  constant,  and  so  it's 
important to consider changing risk preferences in models.

A detailed analysis of the graph shows a gradual rise in 
the risk scores from the third month to the ninth month, where 
the scores peak. This increase indicates greater confidence in 
financial choices, which due to a positive change in financial 
status (increased earnings and/or savings). On the other hand, 
the  downward  trend  in  the  last  few  months  suggests  a  shift 
back  towards  more  conservative  attitudes.  These  changes 
show the dynamic aspect of risk tolerance, which can change 
at  different  points  in  time  due  to  both  personal  financial 
situations and economic conditions.

The  risk  score  fluctuations  also  suggest  the  human 
behavior  involved  in  financial  planning.  Increased  financial 
capacity  (such  as  surplus  cash)  or  financial  pressures  can 
affect an individual's risk tolerance. Generally, a higher risk 
score  reflects  a  willingness  to  invest  in  assets  that  provide 
greater returns but come with greater risks. This relationship 
highlights the  importance of considering behavioral insights 
in  financial  decision-making  models.  This  connection 
highlights the need to integrate behavioral finance in financial 
models.

The table's data suggests that from an analytical point of 
view,  dynamic  risk  profiling  ought  to  be  used.  A  fixed  risk 
profile  not  account  for  these  variations  and  result  in 
suboptimal  suggestions.  Adaptive  risk  profiling  through 
machine learning can monitor and adapt to changing financial 
trends,  allowing  strategies  to  be  in  line  with  preferences. 
Incorporating these risk scores into the decision-making and 
feasibility  assessment  processes  increases  the  effectiveness 
and personalization of financial planning, resulting in a more 
effective system.

FIGURE 8. Expense Distribution and Budget

Allocation Analysis

Table  3  shows  the  monthly  variation  of  risk  scores, 
indicating  the  level  of  risk  tolerance.  The  scores  are  low  to 
high, suggesting that there were changes in preferences over 
time.  The  risk  scores  in  the  first  few  months  indicate  a

The pie chart below illustrates the relative proportions of 
expenditure  across  key  expenditure  categories,  thereby 
providing  insights  into  this  household's  resource  allocation.

Engineering Research

11

---

<!-- PAGE 12 -->

Bidisha Patra 1et al

2025, Vol 02. Issue 02

The highest proportion of expenditure (40%) was allocated to 
rent,  which  means  that  housing  was  the  biggest  expense. 
Housing  was  followed  by  food  (25%),  miscellaneous 
expenses  (20%),  and  transportation  (15%).  The  allocation 
reflects the prominence of basic living expenses in the overall 
expenditure, which was common in financial allocation, with 
fixed  and  necessary  expenses  taking  up  a  significant 
proportion of income.

This distribution can be further analyzed in terms of the 
relatively large share of rent, which reduce the flexibility to 
adjust  spending  on  other  items.  Being  a  fixed  and  rigid 
expenditure,  housing  costs  limit  the  flexibility  in  budget 
adjustment under financial pressures. Likewise, food costs, as 
a necessity, also have a fixed proportion. On the other hand, 
expenses  like  transport  and  miscellaneous  expenses  are 
adjustable.  Knowing  the  flexible  items  was  essential  for 
enhancing  financial  efficiency  and  allowing  for  resource 
allocation.

For analytics, the breakdown of expenses offers insights 
for  financial  analysis  and  planning.  The  high  fixed  expense 
ratio indicates a tight financial structure, with limited income 
to allocate for savings and investments. This finding justifies 
the  role  of  smart  systems  in  uncovering  potential  expense 
reductions and suggesting spending optimization. Models can 
provide  specific  recommendations  for  improved  balance 
while meeting basic needs by examining spending categories. 
Also,  the  spending  pattern  of  the  household  was 
important  for  saving  and  future  financial  well-being.  An 
income  spent  on  non-flexible 
increased  share  of 
expenditures  decreases  the  generation  of  surplus,  which 
further impacts the capacity to reach targets. The inclusion of 
such distribution of expenses into the analysis and validation 
process  leads  to  an  improved  feasibility  assessment.  The 
graph  provides  insights  for  creating  individualized  financial 
plans that balance needs with savings and investment goals, 
leading  to  better  financial  security  and  achievement  of 
financial goals.

the

Table 4. Expense Distribution

Category 
Rent 
Food 
Transport 
Others

Percentage (%) 
40 
25 
15 
20

Table  4  shows  the  shares  of  expenses  in  different 
categories,  which  provides  an  overview  of  financial 
allocation. It shows that the highest proportion was spent on 
rent (40%), followed by food (25%), other expenses (20%), 
and transportation (15%). This allocation was consistent with 
the  typical  financial  allocation  pattern,  with  fixed  and  non-
discretionary  expenses  playing  a  prominent  role.  The 
allocation to housing expenses was relatively large, implying 
that  a  large  part  of  the  total  income  was  spent  on  fixed 
expenses  that  left  less  room  for  financial  flexibility  in

allocating funds to other needs.

The breakdown shows the difference between fixed and 
variable costs in the distribution. Rent was a fixed expense that 
was  relatively  stable,  creating  challenges  in  adjusting 
consumption  patterns  to  financial  challenges.  While  food 
costs  are  a  necessity,  present  few  opportunities  for  cost 
savings,  whereas  transportation  and  other  miscellaneous 
expenses  are  areas  where  savings  can  be  made.  This 
distinction  was  crucial  in  determining  which  costs  can  be 
optimized through cost control measures to enhance financial 
efficiency.

The  distribution  was  also  indicative  of  its  effect  on 
savings and security. An increase in the proportion of income 
allocated to fixed expenses result in a decrease in the surplus 
available for savings and investment.  This limitation impact 
the accomplishment of financial goals, particularly in times of 
reduced  earnings.  On  the  other  hand,  controlling  variable 
expenses  and  related  areas  can  facilitate  surplus  creation, 
which can in turn improve financial stability and the ability to 
achieve financial goals.

The expense distribution was an essential component in 
financial analysis and decision-making. It offers insights into 
resource  allocation,  allowing  for  more  precise  and  tailored 
financial planning. By taking into account these distribution 
patterns in forecasting and feasibility studies, it was possible 
to  provide  customized  advice  for  improved  consumer 
expenditure.  This  aids  in  more  holistic  financial  planning, 
prioritizing  essential  expenses  and  optimizing  savings  and 
investment opportunities.

FIGURE 9. Correlation Matrix of Financial

Variables and Interdependency Analysis

in

the

financial

The  heatmap  displays  the  correlation  between  various 
financial  variables,  providing  an  overall  picture  of 
interdependencies 
system.  Positive 
correlations  are  shown  in  warmer  colors  and  negative 
correlations  in  cooler  colors.  For  instance,  a  high  positive 
correlation was observed between income and savings, which 
implies  that  a  higher  income  leads  to  greater  savings.  This 
finding supports the basic financial fact that income was one 
of the key factors driving excess or surplus, which was crucial

Engineering Research

12

---

<!-- PAGE 13 -->

AI-Driven Goal Based Financial Planning System: A Framework for Contextual            2025, Vol 02. Issue 02

in the attainment of financial goals.

Conversely,  there  was  a  highly  negative  correlation 
between  expenses  and  savings,  suggesting  that  increased 
spending  trends  reduce  savings.  This  negative  correlation 
underscores the importance of managing expenses to achieve 
financial  stability.  There  are  moderate  positive  correlations 
between  income  and  investment,  indicating  that  higher 
incomes  allow  for  more  investment.  These  correlations 
underline  the  interconnected  nature  of  financial  parameters 
and how a change in one variable can affect multiple financial 
factors.

The  correlation  with  risk  score  shows  moderate 
relationships with investment and income, suggesting that risk 
levels are driven by income and potentially impact investment 
strategies. Weaker associations with savings indicate that the 
risk score does not directly influence savings patterns but was 
more  important  in  influencing  how  savings  are  used  for 
investment purposes. This finding suggests the importance of 
considering  behavioral  factors  in  analytical  models,  as  risk 
behavior can influence financial decisions.

In terms of model building, the correlation matrix offers 
insights for feature selection. Strongly correlated variables can 
be  used  to  enhance  predictive  accuracy,  and  negatively 
correlated  variables  indicate aspects  to  be  fine-tuned.  These 
relationships  help  to  develop  better  financial  models.  Using 
these relationships to inform the modeling of future financial 
outcomes,  decision-making,  and  the  assessment  of  financial 
feasibility, we can enhance the generation of financial advice 
and so improve financial planning systems.

Table 5. Correlation Between Financial 
Variables

Variabl
es

Inco
me

Expens
es

Savin
gs

Income

1.00

0.25

0.70

0.25

1.00

-0.60

0.70

-0.60

1.00

-0.20

0.15

-0.25

Risk 
Scor
e 
-
0.20 
0.15

-
0.25 
1.00

Investme
nt

0.45

0.30

0.20

0.35

0.45

0.30

0.20

0.35

1.00

Expense
s 
Savings

Risk 
Score 
Investm
ent

Table  5  shows  the  correlation  matrix  between  key 
financial factors, providing a numerical representation of their 
relationships. The numbers vary from -1 to 1, representing the 
intensity  of  the  relationships  between  income,  expenses, 
investment.  A  high  positive 
savings,  risk  score,  and 
income  and  savings, 
correlation  was  noticed  between 
implying that increased income was correlated with increased 
surplus.  This  correlation  supports  the  vital  importance  of 
income in building financial resilience and achieving financial 
goals.

A  strong  negative  correlation  was  found  between 
expenses  and  savings,  implying  that  higher  expenses  were 
associated  with  less  surplus  generated.  This  correlation 
underscores the importance of managing expenses to ensure 
financial  stability.  Further,  there  was  a  weak  positive 
correlation 
investment, 
implying that increased earnings led to increased investment. 
These  correlations  reveal  the  interdependence  between  the 
various financial variables and how a change in one variable 
affects the others.

identified  between

income  and

The correlation between risk score and other variables has 
lower correlations with savings and income, but a moderate 
positive  correlation  with  investment.  This  suggests  that  risk 
score  was  more  relevant  to  the  investment  decisions  rather 
than savings. Participants with higher risk scores were more 
likely  to  invest  (perhaps  in  an  attempt  to  achieve  greater 
returns the heightened risk). This trend highlights the role of 
behavioral finance in shaping investment strategies and how 
psychology plays a role in how people invest their money.

From a modeling standpoint, the correlation matrix offers 
insights for model building and feature engineering. Positive 
correlations can be used to improve the accuracy of models, 
whereas  negative  correlations  indicate  where  improvements 
are  needed.  These  relationships  allow  their  development  of 
richer,  more  contextual  financial  models.  The  inclusion  of 
these  relationships  in  forecasting,  decision-making,  and 
feasibility checks in the system allows for more precise and 
relevant recommendations, enhancing financial planning.

Conclusion

•  A  successful  AI-based  approach  to  goal-oriented 
implemented,  using

financial  planning  was 
predictive, behavioral, and contextual information.

•  The  research  showed  that  current  financial  planning 
methods  were  not  flexible  and  didn't  consider  the 
dynamic reality. 
learning

techniques  efficiently  captured 
financial trends and enhanced forecasts for income, 
expenses, and savings.

•  Machine

•  Reinforcement  learning  allowed  dynamic  decision-
investment

making  by 
strategies to financial and market environments. 
•  The use of Monte Carlo simulation allowed us to model 
the probability of achieving financial objectives.

continually

adapting

•  Situational

awareness

improved  personalization 
through  the  consideration  of  human  factors,  risk 
preferences, and macroeconomic conditions.

•  The  system  provided  feasibility  scores  and  specific 
recommendations  for  decision  support,  enhancing 
financial planning and decision-making.

•  Benchmarking  suggested  better  performance  in  terms 
of  accuracy,  flexibility,  and  realism  than  existing 
rule-based financial systems.

•  The  use  of  various  AI  techniques  in  an  integrated 
system  filled  the  gap  in  financial  planning  and 
feasibility assessment.

Engineering Research

13

---

<!-- PAGE 14 -->

Bidisha Patra 1et al

2025, Vol 02. Issue 02

•  The  proposed  system  provided  an  intelligent  and 
scalable solution that be applied to various real-world 
scenarios 
in  fintech  systems  and  personalized 
financial advice services.

Data Availability Statement

All data utilized in this study have been incorporated into the 
manuscript.

Authors’ Note

The  authors  declare  that  there  is  no  conflict  of  interest 
regarding  the  publication  of  this  article.  Authors  confirmed 
that the paper was free of plagiarism.

References

[1]  Addy, W. A., Ajayi-Nifise, A. O., Bello, B. G., Tula, 
S.  T.,  Odeyemi,  O.,  &  Falaiye,  T.  (2024). 
Transforming  financial  planning  with  AI-driven 
analysis:  A  review  and  application  insights.  World 
Journal  of  Advanced  Engineering  Technology  and 
Sciences, 11(1), 240-257.

[2]  Abdellatef, A. (2025). How AI was  Redefining the 
Future  of  Financial  Planning  and  Analysis: 
Transforming  financial  planning  and  analysis  with 
AI-driven insights. Strategic Finance.

[3]  Gadam,  H.,  &  Upadhyay,  A.  (2023).  AI-Driven 
Financial  Planning:  A  Study  on  Predictive 
Modelling.

[4]  Omoruyi,  N.  (2025).  Advanced  Computational 
Methods  for  Financial  Planning  and  Analysis  Risk 
Assessment  using  Data  Science-Driven  Model 
Validation  Techniques.  International  Journal  of 
doi: 
Research 
https://www. 
semanticscholar. 
org/paper/4d27d96c40e20c0bd7df2d9220bd4b355a
381c82.

and  Reviews.

Publication

[5]  Mlybari, E. A., & Elgohary, H. A. (2025). AI-driven 
value  management  in  construction:  a  theoretically-
grounded  framework  with  empirical  validation. 
Journal of Umm Al-Qura University for Engineering 
and Architecture, 16(4), 1686-1705.

[6]  OJO,  O.,  Akinadewo,  I.  S.,  Duduyegbe,  S.  S., 
Akinola, J. F., & Omolade, O. T. (2025). AI-driven 
decision-making 
financial  management. 
International  journal  of  economics  and  business 
management, 1, 644.

in

[7]  Cortez,  A.  M.  (2025).  Integrating  AI-Driven 
Predictive  Analytics,  Uncertainty  Quantification, 
and  Robust  Model  Validation 
for  Financial 
Forecasting  and  Autonomous  Decision  Systems. 
International Journal of Modern Medicine, 4(09), 13-
19.

[8]  Hesami,  S.  (2025).  Navigating

the  AI-driven 
transformation  of  personal  finance:  opportunities, 
challenges,  and  ethical  imperatives.  Strategy  &

Leadership.

budgeting

[9]  Talasila,  S.  D.  (2024).  AI-driven  personal  finance 
and 
management:  Revolutionizing 
financial planning. International Research Journal of 
Engineering and Technology, 11(7), 397-407. 
[10] Sholapurapu,  P.  K.  (2024).  AI-based  financial  risk 
assessment tools in project planning and execution. 
Project  Planning  and  Execution  (March  01,  2024). 
European Economic Letters, 14(1).

sustainability‐oriented

[11] Duong,  C.  D.  (2025).  How  AI‐enabled  drivers 
entrepreneurial 
inspire 
intentions:  Unraveling  the  (in)  congruent  effects  of 
perceived  desirability  and  feasibility  from 
the 
entrepreneurial event model perspective. Sustainable 
Development, 33(4), 6228-6246.

[12] Bessa,  G.,  &  Barbosa,  B.  (2025).  Integrating 
Artificial  Intelligence  into  scenario  analysis:  A 
validated  framework  for  strategic  planning  under 
economic uncertainty. Global Economics Research, 
100007.

[13] Sharma,  A.,  Kabade,  S.,  Chaudhari,  B.  B.,  & 
Kagalkar, A. (2025, August). Optimizing Retirement 
Income  Adequacy  with  AI-Based  Personalized 
In  2025  Global 
Financial  Planning  Systems. 
Conference  on 
Information  Technology  and 
Communication  Networks  (GITCON)  (pp.  1-10). 
IEEE.

[14] Thiyagarajan,  V.  (2024).  Expectation:  AI-driven 
forecasting  and  scenario  planning  in  planning  and 
budgeting  cloud  service  (PBCS).  International 
Journal  on  Recent  and  Innovation  Trends 
in 
Computing and Communication, 9(12), 75-85. 
[15] Rainy,  T.  A.,  Goswami,  D.,  Rabbi,  M.  S.,  &  Al 
Maruf,  A.  (2023).  A  Systematic  Review  of  AI-
Enhanced  Decision  Support  Tools  in  Information 
Systems: Strategic Applications In Service-Oriented 
Enterprises  And  Enterprise  Planning.  Review  of 
Applied Science and Technology, 2(01), 26-52. 
[16] Celestin, M., Vasuki, M., Kumar, A. D., & Asamoah, 
P.  J.  (2025).  AI-Driven  Risk  Forecasting  Theory. 
International  American  Council  for  Research  & 
Development.

[17] Bukovski,  K.,  Jain,  K.,  Cummins,  M.,  Bowden,  J., 
Tetteh,  G.  K.,  &  Khang,  Z.  (2025).  From  crisis  to 
prosperity: AI and open finance for holistic financial 
health and smart future planning.

[18] Sepanosian,  T.,  Milosevic,  Z.,  &  Blair,  A.  (2024, 
September).  Scaling  AI  adoption 
finance: 
modelling framework and implementation study. In 
International  Conference  on  Enterprise  Design, 
Operations,  and  Computing  (pp.  221-236).  Cham: 
Springer Nature Switzerland.

in

[19] Saleela, D., Oyegoke, A., Dauda, J. A., & Ajayi, S. 
(2025).  Feasibility  study  for  AI-Driven  Decision 
for  Personalised  Housing 
Support  System 
Adaptations and Assistive Technology.

[20] Ashiedu,  B.  I.,  Ogbuefi,  E.,  Nwabekee,  U.  S., 
Ogeawuchi,  J.  C.,  &  Abayomi,  A.  A.  (2023). 
Designing  Financial  Intelligence  Systems  for  Real-

Engineering Research

14

---

<!-- PAGE 15 -->

AI-Driven Goal Based Financial Planning System: A Framework for Contextual            2025, Vol 02. Issue 02

Time  Decision-Making 
in  African  Corporates. 
Journal  of  Frontiers  in  Multidisciplinary  Research, 
4(2), 68-81.

[21] Ahirrao, Y. S., Ansari, I., Azim, K. S., Bhujel, K., & 
Panchal,  S.  S.  (2025).  AI-Powered  Financial 
Strategy:  Transforming  Business  Decision-Making 
Through  Predictive  Analytics.  Emerging  Frontiers 
Library  for  The  American  Journal  of  Engineering 
and Technology, 7(09), 126-151.

[22] Tanim,  S.  H.,  &  Ahmad,  M.  S.  (2025).  AI  driven 
strategic decision-making in IT project management: 
Enhancing  risk  assessment,  cost  control,  and 
efficiency. Available at SSRN.

[23] Rong, C. (2024). An AI-driven decision framework 
in 
for  promoting  sustainable  entrepreneurship 
vocational colleges. Decision Making: Applications 
in Management and Engineering, 7(2), 748-769. 
[24] Ayankoya, M. B., Omotoso, S. S., & Ogunlana, A. 
A.  (2025).  Data  Driven  Financial  Optimization  for 
(SMEs):  A 
Small  and  Medium  Enterprises 
Framework to Improve Efficiency and Resilience in 
US  Local  Economies.  International  Journal  of 
Management and Organizational Research, 4(4), 90-
97.

[25] Talib,  A.  M.,  Al-Hgaish,  A.  M.,  Atan,  R.  B., 
Alshammari,  A., Alomary, F. O., Yaakob, R., ... & 
Osman,  M.  H.  (2025).  Evaluating  critical  success 
factors  in  AI-driven  drug  discovery  using  AHP:  a 
strategic framework for optimization. IEEE Access, 
13, 42045-42063.

[26] Sadri,  H.  (2025).  AI-driven  integration  of  digital 
twins and blockchain for smart building management 
systems:  A  multi-stage  empirical  study.  Journal  of 
Building Engineering, 105, 112439.

[27] Ahmed, A., Shah, A., Ahmed, T., Yasin, S., Longa, 
F.  E.  A.,  Hussaini,  W.,  &  Zubair,  M.  (2025).  AI-
Driven  Innovations  in  Modern  Banking:  From 
Secure  Digital  Transactions  to  Risk  Management, 
Compliance  Frameworks,  and  AI-Based  ATM 
Forecasting  Systems.  Journal  of  Management 
Science Research Review, 4(3), 1145-1183.

[28] Mahamad,  S.,  Chin,  Y.  H.,  Zulmuksah,  N.  I.  N., 
Haque,  M.  M.,  Shaheen,  M.,  &  Nisar,  K.  (2025). 
Technical 
review:  Architecting  an  AI-driven 
decision support system for enhanced online learning 
and assessment. Future Internet, 17(9), 383.

[29] Ayodeji,  D.  C.,  Oladimeji,  O.,  Ajayi,  J.  O., 
Akindemowo, A. O., Eboseremen, B. O., Obuse, E., 
... & Erigha, E. D. (2022). Operationalizing analytics 
strategic  planning:  A  business 
to 
intelligence case study in digital finance. Journal of 
Frontiers  in  Multidisciplinary  Research,  3(1),  567-
578.

improve

[30] Faqihi,  A.,  &  Miah,  S.  J.  (2023).  Artificial 
system: 
intelligence-driven 
Exploring  the  risks  and  options  for  constructing  a 
theoretical foundation. Journal of Risk and Financial 
Management, 16(1), 31.

talent  management

[31] Arun, M., Barik, D., Chandran, S. S., Praveenkumar, 
S., & Tudu, K. (2025). Economic, policy, social, and 
regulatory  aspects  of  AI-driven  smart  buildings. 
Journal of building engineering, 99, 111666.

[32] Hossain,  M.  S.,  Sikdar,  M.  S.  H.,  Chowdhury,  A., 
Bhuiyan, S. M. Y., & Mobin, S. M. (2025). AI-driven 
aggregate planning for sustainable supply chains: A 
systematic literature review of models, applications, 
and industry impacts. American Journal of Advanced 
Technology and Engineering Solutions, 1(01), 382-
437.

[33] Artene,  A.  E.,  Domil,  A.  E.,  &  Ivascu,  L.  (2024). 
Unlocking  business  value:  Integrating  AI-driven 
decision-making  in  financial  reporting  systems. 
Electronics, 13(15), 3069.

[34] Arshad,  N.,  Butt,  T.  A.,  &  Iqbal,  M.  (2025).  A 
comprehensive  framework for  Intelligent,  Scalable, 
and  Performance-Optimized  software  development. 
IEEE Access, 13, 74062-74077.

[35] J.  Nair,  A.,  Manohar,  S.,  &  Mittal,  A.  (2025).  AI-
enabled  FinTech  for 
innovative  sustainability: 
promoting  organizational  sustainability  practices  in 
digital accounting and finance. International Journal 
of  Accounting  &  Information  Management,  33(2), 
287-312.

[36] Chukwuma-Eke, E. C., Ogunsola, O. Y., & Isibor, N. 
J.  (2022).  A  conceptual  framework  for  financial 
optimization and budget management in large-scale 
energy 
of 
Multidisciplinary Research and Growth Evaluation, 
2(1), 823-834.

International

projects.

Journal

[37] Grabocka,  E.,  &  Ndoka,  E.  (2025).  AI-driven 
innovation  within  the  ICT  sector.  Smart  Cities  and 
Regional Development (SCRD) Journal, 9(1), 77-97. 
[38] Yang, H., Lin, L., She, Y., Liao, X., Wang, J., Zhang, 
R., ... & Wang, C. D. (2025). FinRobot: Generative 
Business Process AI Agents for Enterprise Resource 
Planning 
preprint 
arXiv:2506.01423.

Finance.

arXiv

in

[39] Jahid, M. S. R. (2025). AI-driven optimization and 
zone 
risk  modeling 
development  for  mid-sized  economies:  A  review 
approach. 
Journal  of  Scientific 
Interdisciplinary Research, 6(1), 185-218.

International

economic

strategic

in

[40] De Zarzà, I., De Curtò, J., Roig, G., & Calafate, C. T. 
(2023).  Optimized  financial  planning:  integrating 
individual  and  cooperative  budgeting  models  with 
LLM recommendations. AI, 5(1), 91-114.

Engineering Research

15

---

<!-- PAGE 16 -->

Bidisha Patra 1et al

2025, Vol 02. Issue 02

© Bidisha Patra, Samadrita Sarkar, Sneha Pal, Sreejani Ghosh, and Prof. Sujoy Datta. 2024 
Open  Access.  This  article  is  distributed  under  the  terms  of  the  Creative  Commons  Attribution  4.0 
International  License  (http://creativecommons.org/licenses/by/4.0/),  which  permits  unrestricted  use, 
distribution, and reproduction in any medium, provided you give appropriate credit to the original author(s) 
and the source, provide a link to the Creative Commons license, and indicate if changes were made.

Embargo period: The article has no embargo period.

To cite this Article: To cite this Article: Bidisha Patra, Samadrita Sarkar, Sneha Pal, Sreejani Ghosh, and 
Prof.  Sujoy  Datta,  AI-Driven  Goal  Based  Financial  Planning  System:  A  Framework  for  Contextual 
Feasibility Validation, Engineering Research 1.1(2025):1-2. https://doi.org/10.71443/er.ar16

Engineering Research

16

<!-- MARKITDOWN CONVERSION -->

<!-- Full MarkItDown conversion for formatting fidelity. -->

Engineering Research
3048-880X
Rademics Research Institute
https://doi.org/10.71443/er.ar16
AI-Driven Goal Based Financial Planning System: A Framework for Contextual
Feasibility Validation
Bidisha Patra 1, Samadrita Sarkar 2, Sneha Pal 3, Sreejani Ghosh 4, Prof. Sujoy Datta 5
12345School of Computer Engineering, KIIT Deemed to be University, Bhubaneshwar, Odisha, India.
Article history Abstract
Accepted: 18 December In the wake of growing complexity in financial decision-making and the ever-
2025 changing economic environment, conventional financial planning strategies have
Keywords:
proven inadequate. This paper presents an artificial intelligence (AI) powered
Artificial Intelligence,
goal-based financial planning system with contextual feasibility analysis to
Goal-Based Financial
Planning, improve the precision and responsiveness of financial planning. The system
Feasibility Validation, combines several elements, such as personal financial data analysis, machine
Reinforcement Learning, learning for financial predictions, reinforcement learning for financial strategies,
Financial Forecasting,
and probabilistic modeling for feasibility validation. A holistic framework was
Context-Aware Systems.
proposed to model financial factors, including income, expenditure, savings, risk,
and market dynamics, into a single framework to reflect both human and
environmental factors. Time-series forecasting models are used for financial
predictions, and reinforcement learning for investment strategy optimization.
Monte Carlo simulation was used to assess various financial scenarios and assess
the feasibility of achieving specific financial objectives. The tool offers tailored
financial plans, feasibility measures, and recommendations to help make more
realistic and informed decisions. Empirical experiments show that the proposed
system increases the accuracy of forecasts, adaptability, and more accurate goal
feasibility evaluations than traditional rule-based approaches. The results indicate
that embedding contextual awareness and adaptive learning capabilities in
financial planning systems greatly enhances their performance. The study presents
a scalable and smart approach that integrates predictive analytics with goal-based
financial planning, which can be applied in fintech applications and personal
financial advisors.
1. Introduction tend to compartmentalize financial goals and place different
weights of importance and risk appetite on each goal, thus
Goal-based financial planning represents a major shift
undermining the homogeneity assumptions in conventional
from more traditional wealth maximization models by
portfolio optimization [5]. The life-cycle investment
focusing on tailoring investment strategies to achieve life
approaches indicate that investment goals and risk tolerance
goals such as retirement, education, and asset acquisition [1].
change over time, necessitating flexible and tailored
Drawing on the insights of behavioral finance, this paradigm
approaches to financial planning [4]. The many traditional
acknowledges that investment decisions are not purely
systems do not consider dynamic behavioral factors in
rational but are heavily influenced by biases, emotions, and
addition to financial data streams, leading to static, often
risk attitudes [2]. Pioneering theories of behavioral economics
unrealistic forecasts. This gap suggests a need for smart
(Kahneman and Tversky) illustrate the impact of biases (such
systems capable of dynamically responding to both behavioral
as loss aversion, anchoring, and overconfidence) on financial
and financial factors to improve the realism and relevance of
decision-making [3]. The literature also suggests that people
Contact – ghoshsreejani@gmail.com 1

Bidisha Patra 1et al 2025, Vol 02. Issue 02
goal-based financial planning within financial ecosystems [5]. models grounded in theories such as the Capital Asset Pricing
Building on the principles of goal-based financial Model (CAPM) use risk-adjusted expected returns for a better
planning and behavioral finance, robo-advisory and FinTech assessment. But the success of these models of validation
platforms are a technological advancement that puts these largely relies on the quality of personal financial data analytics
concepts into practice through automated, data-driven, and [18]. Insight into income, expenditure, savings, and debt was
scalable platforms [6]. Services like Betterment and crucial to assessing financial status and potential. The
Wealthfront are examples of the application of algorithmic application of more sophisticated analytical methods such as
portfolio management, passive investment approaches, and clustering and predictive modeling also improves forecasting
automatic rebalancing based on user-specified risk capabilities [19]. The issues such as data variability, privacy,
preferences [7]. Prior studies show that these systems and lack of behavioral considerations remain. As such, there
primarily use Modern Portfolio Theory and exchange-traded was a need for more integrated approaches that integrate
fund (ETF) diversification to implement efficient asset feasibility validation with real-time data-driven
allocation. Though robo-advisors provide benefits such as personalization [20].
convenience, cost-effectiveness, and user-friendliness, Combining personal financial analytics with context-
frequently rely on generic risk assessment questionnaires, aware artificial intelligence systems also adds flexibility and
which fail to account for the nuanced preferences of users and accuracy to personal financial plans. Unlike conventional AI
changes in financial circumstances [8]. The tend to prioritize systems that use static inputs, context-aware systems consider
portfolio optimization over assessing the achievability of dynamic multidimensional factors like economic changes,
financial goals. This results in a gap between investment time, user activities, and events to offer more relevant and
returns and achieving financial goals [9]. While recent specific recommendations [21]. The pioneering work of Mark
developments in FinTech leverage machine learning and big Weiser has spawned context-aware computing, which has
data to improve personalization, there are still many been applied to finance. The allow for real-time adaptations to
challenges to solving issues related to situational awareness, market conditions and personal situations for more effective
behavioral adaptability, and responsiveness. This suggests the decision-making [22]. This ability can also be enhanced for
need for more advanced systems that go beyond automation risk measurement and portfolio management systems, which
to provide integrated, goal-based financial planning [10]. are based on classical financial theories such as the Modern
Building on the advancements in robo-advisory, machine Portfolio Theory (MPT) by Harry Markowitz and the Capital
learning has emerged as a key element in financial forecasting, Asset Pricing Model (CAPM) by William F. Sharpe. These
allowing the identification of patterns in high-dimensional and traditional models offer a robust theoretical framework, but
complex financial data [11]. Historically, statistical models their assumptions restrict them in a dynamic and turbulent
like ARIMA have been popular, but their inability to cope environment [23]. Recent research using machine learning
with non-linear and non-stationary data has led to the adoption and stochastic modeling tries to address these issues; the
of more sophisticated approaches like deep learning. For incorporation of contextual awareness and goal-based,
example, Long Short-Term Memory (LSTM) networks, personalized insights was still lacking [24]. This calls for the
proposed by Sepp Hochreiter and Jürgen Schmidhuber, show development of sophisticated and context-sensitive financial
effective modeling of temporal relationships and enhanced systems that link risk management to dynamic goal-based
forecasting performance [12]. Ensemble techniques like financial planning [25].
random forests and gradient boosting improve the model's
stability and accuracy. While machine learning offers
2. Research gap
predictive insights, reinforcement learning builds on this
approach by allowing for adaptive decision-making through
interaction with the dynamic financial environment [13]. The literature has made substantial advancements in goal-
Building on basic principles outlined in reinforcement based financial planning, robo-advisory systems, and AI-
learning: An introduction: Reinforcement learning models based financial predictions, but there are key gaps in their
have been incorporated into portfolio management, integration and use. Current solutions focus primarily on
algorithmic trading, and dynamic allocation [14]. These portfolio management and forecasting but lack dynamic
models learn and adapt strategies over time, making them financial goal feasibility analysis. The tend to underuse
well-adapted to dynamic financial environments. But issues behavioral factors and real-time contextual information,
related to reward function design, convergence, and volatility leading to a lack of personalization and flexibility. Further, it
create difficulties in applying these models in practice [15]. was not common to see the integration of machine learning
Expanding on the adaptive decision-making abilities, and/or reinforcement learning models with feasibility
models for feasibility analysis and financial goal validation analysis. An intelligent, context-sensitive system that
are essential to determining if the optimized strategies attain harmonizes behavioral factors, real-time financial data
financial goals [16]. Existing approaches typically involve analytics, and adaptive decision-making was needed to
deterministic assumptions about income growth, inflation, and enhance the feasibility of achieving goals.
investment returns, which do not account for uncertainties.
Modern methods increasingly use probabilistic methods, like 3. Research methodology
Monte Carlo simulations, to quantify the chances of achieving
financial goals, given different market scenarios [17]. The
Engineering Research 2

AI-Driven Goal Based Financial Planning System: A Framework for Contextual            2025, Vol 02. Issue 02
limitations of static models of financial planning by offering
|     |     |     |     |     |     |     | dynamic,  | goal-based  |     | models  | responsive  | to  | individuals'  |     |
| --- | --- | --- | --- | --- | --- | --- | --------- | ----------- | --- | ------- | ----------- | --- | ------------- | --- |
financial situations and macroeconomic factors.
  To provide a robust foundation for analysis, relevant
factors in financial planning were identified and organized.
Central financial variables such as income and expenses were
|     |     |     |     |     |     |     | complemented  |     | with  | other  | variables  | such  as  | savings  | and  |
| --- | --- | --- | --- | --- | --- | --- | ------------- | --- | ----- | ------ | ---------- | --------- | -------- | ---- |
liabilities, behavioral and environmental factors such as risk
|     |     |     |     |     |     |     | aversion,  | consumption  |     | patterns,  | and  | external  | economic  |     |
| --- | --- | --- | --- | --- | --- | --- | ---------- | ------------ | --- | ---------- | ---- | --------- | --------- | --- |
parameters [27]. These factors were viewed as interrelated
|     |     |     |     |     |     |     | elements  | in  | a   | multi-dimensional  |     | decision-making  |     |     |
| --- | --- | --- | --- | --- | --- | --- | --------- | --- | --- | ------------------ | --- | ---------------- | --- | --- |
environment, allowing a more comprehensive portrayal of
personal financial attributes. Previous research has dealt with
these factors individually; the present formulation stressed
their interrelationship to improve the realism of the financial
planning process.
  In addition, the nature of financial decision-making in an
uncertain environment calls for the problem to be formulated
|     |     |     |     |     |     |     | as  an  | optimization  |     | problem.  | The  | feasibility  | of  financial  |     |
| --- | --- | --- | --- | --- | --- | --- | ------- | ------------- | --- | --------- | ---- | ------------ | -------------- | --- |
objectives was formulated based on the time horizon, initial
resources, financial markets, and personal constraints. The
impact of uncertainty (e.g., in income and market prices) was
also modeled. This problem formulation has allowed the use
|     |     |     |     |     |     |     | of  computational  |     | methods  |     | to  explore  | different  | financial  |     |
| --- | --- | --- | --- | --- | --- | --- | ------------------ | --- | -------- | --- | ------------ | ---------- | ---------- | --- |
scenarios and find the best strategies in line with the set
objectives.
  Lastly, the formulated problem enabled the creation of an
AI-powered system with the potential for ongoing learning
|     |     |     |     |     |     |     | and  evaluation.  |     | Formulation  |     | of  financial  | planning  |     | as  an  |
| --- | --- | --- | --- | --- | --- | --- | ----------------- | --- | ------------ | --- | -------------- | --------- | --- | ------- |
optimization problem allowed the integration of predictive
|     |     |     |     |     |     |     | and  reinforcement  |     | learning  |     | approaches  | with  | probabilistic  |     |
| --- | --- | --- | --- | --- | --- | --- | ------------------- | --- | --------- | --- | ----------- | ----- | -------------- | --- |
evaluations. This guaranteed that investment strategies were
not only tailored to the optimum returns but also evaluated for
|     |     |     |     |     |     |     | their  suitability  |     | to   | achieve    | specific  | objectives.  |            | The  |
| --- | --- | --- | --- | --- | --- | --- | ------------------- | --- | ---- | ---------- | --------- | ------------ | ---------- | ---- |
|     |     |     |     |     |     |     | formulation         | of  | the  | financial  | planning  | problem      | therefore  |      |
provided a solid theoretical and computational basis for a
context- and goal-driven financial planning system.
Framework Design
  The system design was conceived to enable an intelligent
and scalable system to tackle complex financial planning
problems in a layered approach. A hybrid AI architecture was
envisaged, which involved three main layers: the data layer,
the AI (artificial intelligence) layer, and the decision layer

[28]. The data layer collected and organized various financial
data, such as user financial data and macroeconomic data. The
FIGURE 1. Research methodology Flowchart
AI layer was the processing layer, where adaptive models
were applied. The decision layer served as the output layer,
providing an interface for creating actionable insights, making
Problem Formulation
sure that the system process its analyses and translate them
  The problem statement of the proposed research was
into financial advice in line with users' objectives.
based on the need to create an intelligent system that can    Within  the  system,  we  strategically  incorporated
harmonize financial plans with personal life goals. Goal-
computational methods to improve its analytical prowess.
| centered  | financial  | planning  | was  | defined  | as  | a  dynamic  |     |     |     |     |     |     |     |     |
| --------- | ---------- | --------- | ---- | -------- | --- | ----------- | --- | --- | --- | --- | --- | --- | --- | --- |
Machine learning techniques were used to detect patterns in
| framework   | where          | financial  | planning  | was                   | based  | on  the  |            |            |          |             |               |             |            |          |
| ----------- | -------------- | ---------- | --------- | --------------------- | ------ | -------- | ---------- | ---------- | -------- | ----------- | ------------- | ----------- | ---------- | -------- |
|             |                |            |           |                       |        |          | financial  | behavior,  |          | categorize  | risk          | tolerance,  | and        | predict  |
| attainment  | of  financial  |            | goals     | such  as  retirement  |        | income,  |            |            |          |             |               |             |            |          |
|             |                |            |           |                       |        |          | critical   | financial  | factors  |             | like  income  | and         | spending.  |          |
education funding, and wealth building [26]. Current methods
Reinforcement learning techniques were used to facilitate
| were  seen  | to  | focus  | on  maximizing  | wealth  |     | rather  than  |     |     |     |     |     |     |     |     |
| ----------- | --- | ------ | --------------- | ------- | --- | ------------- | --- | --- | --- | --- | --- | --- | --- | --- |
dynamic decision-making, enabling the system to learn and
achieving goals, thus restricting their application. To counter
|     |     |     |     |     |     |     | adjust  | financial  | strategies  |     | in  response  | to  | feedback  | and  |
| --- | --- | --- | --- | --- | --- | --- | ------- | ---------- | ----------- | --- | ------------- | --- | --------- | ---- |
this, the research question was formulated to overcome the

|                       |     |     |     |     |     |     |     |     |     |     |     |     |     |     |
| --------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Engineering Research  |     |     |     |     |     |     |     |     |     |     |     |     |     | 3   |

Bidisha Patra 1et al 2025, Vol 02. Issue 02
evolving circumstances. The data analytics components were segmentation algorithms were used to segment financial
employed to analyze large amounts of structured and activities. This organization allowed for efficient training of
unstructured financial data to ensure timely insights were models and enabled the system to better understand financial
extracted. This approach enabled a holistic analytical behaviors.
framework to support predictive and prescriptive financial Next, feature extraction was applied to derive relevant
planning. features that reflected critical aspects of financial status and
A key feature of the system was to establish a data behavior [31]. These new features encompassed cash flow
pipeline between the various components of the system to patterns, savings ratios, spending habits, and inferred risk
facilitate communication between inputs, models, and measures based on past financial transactions. These features
outputs. Input financial data was collected, processed, and provided additional information about a person’s financial
converted into structured data formats [29]. This transformed stability and capacity, enabling better predictions and advice.
data was then transferred to the AI layer for the various AI Extraction was a process that helped convert uninformative
models to simultaneously produce predictions, classifications, data into useful features that improved the effectiveness of
and optimizations. The outputs of these models were then machine learning and reinforcement learning models,
passed to the decision layer, where were integrated into facilitating successful feasibility testing and decision-making
meaningful recommendations, feasibility assessments, and in the proposed framework.
insights. This structured data flow provided consistency, AI Model Development
efficiency, and timeliness to the system. The design of the AI models phase was focused on
The framework was designed to be modular, scalable, and facilitating prediction, understanding, and learning the
flexible to support changes in financial use cases and user behavior of the financial planning framework. Both predictive
needs. The layers were designed to be independent but also and intelligent models were developed to tackle the challenges
highly interconnected, enabling the seamless addition of new of financial data and future uncertainties [32]. A primary focus
models or data sources without impacting the system’s was on the use of a combination of techniques to capture short
performance. This architecture enabled ongoing learning and and longer-term financial trends. This was the computational
evolution of the system to support changes in financial trends, heart of the system in which insights were developed based on
market dynamics, and user behavior. This approach thus laid financial data to support goal-oriented financial planning and
a solid groundwork for 4uildingg an AI-enabled, context- projections.
aware financial service system that offered personalized and Time-series models were created to predict future
goal-based solutions. financial indicators like income, expenses, and savings.
Data Collection & Preprocessing Temporal models, such as Long Short-Term Memory (LSTM)
The data-gathering phase aimed to provide a solid networks, were employed because can capture the temporal
foundation for the development of the AI-based financial dependencies and handle time-series financial data. The
planning system. Data was collected from various sources, regression models were applied to model relationships
including user-specific information such as income, between financial variables and make continuous predictions.
expenditures, savings, investments, and debt data. Alongside These prediction techniques allowed the system to predict
personal data, macroeconomic data, including inflation, financial trends under different scenarios, thereby offering a
interest rates, and market indices, were also gathered to reflect predictive lens critical to assessing the feasibility of goals.
external financial factors impacting financial planning [30]. In addition to forecasting, machine learning techniques
This mix of microeconomic and macroeconomic data allowed were applied for risk assessment and profiling. Classification
the system to capture both individual financial activities and techniques were used to classify users according to their
macroeconomic factors, which added to the contextual financial profiles, spending habits, and estimated risk
understanding of the financial decision-making process. attitudes. Clustering algorithms also helped in the discovery
After collecting the data, a preprocessing process was of user clusters with similar financial profiles [33]. This
implemented to enhance data quality. Financial data can be analytical component provided insights into individual
prone to missing entries, inconsistencies, and outliers, which financial behavior and preferences, enabling the system to
affect the effectiveness of the models. To resolve these make recommendations and strategies based on the
problems, suitable methods were employed to deal with individual's risk tolerance and other characteristics.
missing values, eliminate outliers, and standardize formats. We developed a reinforcement learning agent to support
Normalization techniques were applied to rescale variables to dynamic financial decision-making. The agent engaged with
a similar range, avoiding undue influence of any specific financial simulations and learned from rewards and penalties
variable on the models. The data transformation methods were to refine its strategies. This enabled the system to learn the
applied to convert non-numerical and temporal data into best actions to take under different circumstances, taking into
structured data formats that be used for training machine account both user-specific constraints and investment
learning models. conditions. The use of reinforcement learning improved the
The data preprocessing phase also included restructuring system’s adaptability in investment strategy to ensure
data to meet the needs of predictive and analytical models. financial plans adapted to changing goals and circumstances.
Time-based income and expense data were structured as time Feasibility Validation Framework
series to enable predictions. Data aggregation methods were The feasibility validation framework was designed to
used to create summaries of transactional data, and validate the feasibility of achieving set financial goals in
Engineering Research 4

AI-Driven Goal Based Financial Planning System: A Framework for Contextual 2025, Vol 02. Issue 02
uncertain and dynamic settings. Financial goals were defined financial plans. The AI-based approach involved dynamic
in terms of short-, medium-, and long-term, with each time variables, predictive algorithms, and learning mechanisms.
frame having its own set of priorities, time constraints, and Analysis compared the flexibility, adaptability, and tailored
budgetary needs. Short-term goals were related to immediate recommendations of the two approaches. This resulted in the
needs such as cash reserves or minor expenses, while medium- benefits of the new approach being highlighted for
term goals were associated with goals such as education or overcoming issues with the old models.
real estate. Long-term goals were framed as retirement and The system's feasibility results were validated to assess
investment goals [34]. This categorization allowed the system the system's prediction of goal attainment. The system
to link financial planning strategies with time-bound goals and provided information on the probability of results obtained
risk factors and have the goals assessed in the correct context. from simulations, which were tested to establish if were
In order to test the influence of uncertainty on financial consistent with actual financial scenarios. Sensitivity testing
performance, the model was tested using Monte Carlo was conducted to assess the impact of changes to input
simulations. Various simulations were created by adjusting variables on feasibility outcomes and ensure accuracy and
parameters like income growth, spending variability, consistency [37]. This analysis verified that the system
inflation, and returns. This resulted in a distribution of accurately predict the probability of meeting financial
possible financial outcomes, accounting for realistic objectives in various scenarios, thus enhancing trust in the
uncertainty in economic and personal factors. Through system's analysis capabilities.
iterative simulations, the system reflected the randomness of Further, the validity of the recommendations was
financial markets and allowed a holistic view of potential assessed to validate their usefulness and applicability. The
future conditions, rather than deterministic approaches. capability of the system to provide suitable financial advice,
The outcome of the simulation was used to assess the such as modifying savings rates, investment portfolios, or time
likelihood of achieving financial goals. The results of the frames of the goals, was assessed based on improved
simulations were statistically analyzed to assess the outcomes and user preferences. This ensured that the
probability of achieving their target values within a given time recommendations were effective both theoretically and
period [35]. Probability distributions were developed to practically. In this phase, the validity of the proposed approach
capture the distribution and likelihood of outcomes, enabling was confirmed as it was able to provide accurate predictions,
a quantitative evaluation of financial goals' feasibility. This feasible feasibility evaluations, and valuable financial
approach allowed for the identification of risky goals and gave recommendations.
an indication of the extent of risk involved in achieving Result Analysis & Output
financial goals. The result analysis and output process aimed to transform
In addition, the feasibility validation process facilitated computational results into financial recommendations in line
dynamic assessment and adaptation of financial plans. The with users' goals. Using the system's predictions, behavior
simulation step was periodically updated based on the latest assessments, and feasibility predictions, financial plans were
data or financial circumstances. This enabled the feasibility developed [38]. These plans took into account personal factors
analysis to be up-to-date and for the system to suggest changes such as income, spending habits, risk profile, and time frame.
in savings, investment, or time frame for achieving the goals. This combination allowed the financial plans to be based on
The combination of probabilistic validation and dynamic realistic scenarios and personal preferences. The results were
updates improved the realism and accuracy of financial presented in a format that offered recommendations on
planning, enabling the framework to be applied to context- savings and investment options and prioritization of financial
specific and personalized financial planning. goals, thus improving the usefulness of the plans.
Evaluation & Validation The system not only produced the financial plans, but it
The evaluation and validation phase was undertaken to also provided feasibility scores that indicated the probability
evaluate the accuracy, robustness, and effectiveness of the AI- of success for each financial goal. These were based on the
based financial planning system. We took a structured results from the probabilistic simulations and predictive
approach to assess the performance of the models in modeling, providing a quantitative measure of success under
forecasting financial variables and aiding decisions. The different scenarios [39]. Besides feasibility scores, the system
evaluation was done at both the model and system levels [36]. also provided recommendations to enhance the chance of
Performance measures such as accuracy, error, and achieving goals. These suggestions involved changing savings
computational time were used to assess the accuracy of levels, changing investment strategies, and changing the time
prediction models and classification algorithms. This stage of frame to achieve the goal. The combination of scores and
the evaluation ensured the system satisfied the quality criteria recommendations facilitated an informed decision-making
for financial systems. process.
For a valid comparison, our system was benchmarked Data interpretation was done to make the output of the
against conventional financial planning approaches, which are analysis easy to understand and meaningful. As such, financial
based on static forecasts and rule-based decision-making results were examined in terms of assumptions used, model
heuristics. Traditional methods often relied on static growth forecasts, and other factors affecting performance (such as
assumptions and deterministic calculations and lacked market forces and human behavior). This analysis layer
personalized recommendations, leading to less flexible allowed us to understand what factors contributed to the
Engineering Research 5

|  Bidisha Patra 1et al  |     |     |     |     |     |     | 2025, Vol 02. Issue 02  |     |     |     |
| ---------------------- | --- | --- | --- | --- | --- | --- | ----------------------- | --- | --- | --- |
success or failure of financial objectives and to gain insights  fluctuations  highlight  the  need  to  include  time  series
into  financial  performance.  The  system  improved  the  forecasting models and learning systems. Assumptions of
transparency of outcomes through the connection to factors  income constancy or constant percentages of income spent on
and informed financial decision-making.  various  expenses  not  account  for  these  variations.  The
  In  addition,  the  analysis  phase  helped  to  identify  forecasting techniques like LSTM can learn these dynamics,
opportunities for improvement in the financial strategies and  while reinforcement learning processes can adapt financial
system.  Discrepancies  in  feasibility  scores  and  other  strategies to these changes. This keeps financial advice up-to-
indicators were analyzed for inefficiencies or risks. In light of  date with the client's financial circumstances.
this,  iterative  improvements  were  proposed,  such  as    The  graph  was  a  starting  point  for  the  feasibility
adjustments to the strategy and model. The iterative process  assessment  and  decision-making  process.  The  income-
ensured that the system was dynamic and able to adapt to  expense gaps observed in the graph affect savings, which play
prevailing financial conditions—thereby enhancing its ability  a crucial role in goal attainment. Reduced savings lead to a
to provide accurate and targeted financial planning systems  decreased likelihood of reaching financial goals, while excess
[40].  savings can be used to optimize investments. By considering
  these behavioral insights in the system analysis, the system
|     |     |     |     |     | can  provide  | more  realistic  | feasibility  | scores  | and  tailored  |     |
| --- | --- | --- | --- | --- | ------------- | ---------------- | ------------ | ------- | -------------- | --- |
4. Result and discussion
   suggestions,  which  can  improve  the  financial  planning
process.
Table 1. Monthly Income and Expense Data

|                                   |     |     |     |     | Month  | Income  | Expenses  |     | Savings  |     |
| --------------------------------- | --- | --- | --- | --- | ------ | ------- | --------- | --- | -------- | --- |
|                                   |     |     |     |     | 1      | 56000   | 25000     |     | 31000    |     |
|                                   |     |     |     |     | 2      | 41000   | 58000     |     | -17000   |     |
|                                   |     |     |     |     | 3      | 78000   | 59000     |     | 19000    |     |
|                                   |     |     |     |     | 4      | 51000   | 37000     |     | 14000    |     |
|                                   |     |     |     |     | 5      | 46000   | 40000     |     | 6000     |     |
|                                   |     |     |     |     | 6      | 57000   | 49000     |     | 8000     |     |
|                                   |     |     |     |     | 7      | 77000   | 26000     |     | 51000    |     |
|                                   |     |     |     |     | 8      | 62000   | 47000     |     | 15000    |     |
|                                   |     |     |     |     | 9      | 56000   | 46000     |     | 10000    |     |
| FIGURE 2. Monthly Income–Expense  |     |     |     |     | 10     | 42000   | 39000     |     | 3000     |     |
|                                   |     |     |     |     | 11     | 41000   | 38000     |     | 3000     |     |
Dynamics and Financial Behavior Analysis
|     |     |     |     |     | 12  | 43000  | 23000  |     | 20000  |     |
| --- | --- | --- | --- | --- | --- | ------ | ------ | --- | ------ | --- |

|     |     |     |     |     |   Table  | 1  shows  | the  monthly  | distribution  | of  income,  |     |
| --- | --- | --- | --- | --- | -------- | --------- | ------------- | ------------- | ------------ | --- |
  The graph shown was a comparative view of monthly
expenses, and savings, offering an overview of the cash flow
| income  | and  expenses  over  | a  year,  offering  | essential  |     |     |     |     |     |     |     |
| ------- | -------------------- | ------------------- | ---------- | --- | --- | --- | --- | --- | --- | --- |
in the period considered. This table shows that there was
| information  | about  financial  | practices  and  | cash  | flow  |     |     |     |     |     |     |
| ------------ | ----------------- | --------------- | ----- | ----- | --- | --- | --- | --- | --- | --- |
considerable variation in income and expenses, suggesting
management. The income graph shows significant variations,
that the financial circumstances were not constant throughout
with peaks around the third and seventh months suggesting
the months. Income varied from as low as approximately
increased income during these periods. The expenditure curve
41,000 to as high as 78,000, and expenses also exhibited
was relatively diverse, with some months showing higher
variations. This highlights that cash flows were subject to
expenses. The disparity between income and expenses reflects
varying factors and must be considered together rather than
the dynamic nature of financial circumstances and the need for
individually. The calculated savings column, representing the
ongoing monitoring in smart financial planning systems.
balance between income and expenses, was a crucial measure
  Upon closer inspection, it appears that in some months,
of financial well-being and surplus.
expenses are close to or at times even exceed income, as in the
|     |     |     |     |     |   From the table, we can see instances of surplus and  |     |     |     |     |     |
| --- | --- | --- | --- | --- | ------------------------------------------------------ | --- | --- | --- | --- | --- |
second and third months. These trends suggest potential cash
deficit. For instance, the second month shows a deficit in
flow challenges or less savings potential in these months. On
savings (negative value), implying either financial distress or
the other hand, months with a larger disparity between income
the need to draw on additional resources. On the other hand,
and expenses (seventh and eighth months) indicate greater
the seventh and first months displayed high positive savings,
savings capacity and enhanced financial well-being. Such
indicating financial fortitude in those months. This variation
variability was vital in examining dynamic financial patterns
underscores the variability of financial resiliency and the need
and plays a key role in determining surplus and deficit periods
to focus on potential risk periods where financial interventions
in a planning model.
are needed.
  From a modeling point of view, these income and expense

|                       |     |     |     |     |     |     |     |     |     |     |
| --------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Engineering Research  |     |     |     |     |     |     |     |     |     | 6   |

AI-Driven Goal Based Financial Planning System: A Framework for Contextual 2025, Vol 02. Issue 02
The monthly differences in savings also highlight the analysis, the savings' variability also stresses the importance
effects of income minus expense on financial stability. Periods of adaptable and predictive models. Conventional financial
of higher income and lower expenses lead to substantial strategies, which rely on steady savings rates, not account for
surplus savings, while moderate income levels lead to lower this variability. Time series forecasting techniques can detect
savings when expenses are high. This reflects that while these trends, while adaptive learning techniques can make
income was important for financial stability, it was also dynamic recommendations for savings or investment
important to keep expenses low. The interaction of these strategies.
factors offers insights into the decision-making process, This allows the system to adapt to financial turbulence
spending behavior, and savings discipline. and stay on track towards financial goals. In addition, the
In terms of analysis, the figures in the table represent a savings trend was an essential element of the decision-making
key part of the data set used for prediction modeling and process and feasibility analysis. Negative and low savings
feasibility studies. The variability in the data suggests the use periods affect the feasibility of financial plans and goals,
of time-series analysis and dynamic financial planning, as the whereas high savings increase their chance of success. By
latter not account for such variations. The savings figures, in considering these trends in probabilistic modeling, more
particular, are a critical input to assess the feasibility of accurate feasibility index scores can be obtained. The
financial objectives. Leveraging these insights in analytical information gleaned from this graph can be used to inform
models will yield better forecasts and feasible financial plans, individual financial plans, making sure recommendations are
leading to better decision-making and financial security. in line with the financial realities of consumers' changing
circumstances.
FIGURE 3. Monthly Savings Variability and
Financial Stability Assessment
FIGURE 4. Monthly Income Distribution and
The variation in savings was depicted in the graph, which
Cash Flow Variability Analysis
measures the difference between income and expenses for
each month over a year. There was considerable variation in
savings, including a negative value in the second month,
The bar chart shows the monthly income distribution in a
which suggests a deficit in which expenditure was greater than
year, with variations in income. The insights provided by this
income. The fluctuation underscores the volatile nature of
data indicate that the income was not stable, with higher
individual financial circumstances and the need for regular
values in the third and seventh months and lower values in the
monitoring of savings patterns.
second, tenth, and eleventh months. This suggests non-
The switching signs for savings reflect the balance
stability, rather than stability, of income streams, which was
between income and spending and are an essential measure to
an important consideration in financial decision-making.
assess financial performance. Upon closer inspection, we see
These variations be due to factors like incentive-based
that savings have reached a peak around the seventh month,
income, seasonality, or economic factors, which must be
which indicate a month where one experienced a financial
considered in smart financial systems.
surplus. This was a time when investment opportunities be
An in-depth analysis of the graph reveals that peak values
seized and/or financial goals be achieved more rapidly. On the
generate surplus while dips in income limit cash flow. For
other hand, negative savings earlier in the year and/or reduced
example, the higher values in mid-year suggest an increase in
savings later in the year imply periods of financial deficit or
cash flow and thus surplus, while the depressions in later
diminishing opportunities for wealth building.
months suggest a decrease in cash flow, limiting financial
Such variability was crucial for analyzing the temporal
flexibility. For example, the peaks seen in mid-year highlight
allocation of financial resources and for pinpointing times
the potential for higher savings and investments, while the
when corrective financial measures be needed. In terms of
Engineering Research 7

|  Bidisha Patra 1et al  |     |     |     |     |     |     |     | 2025, Vol 02. Issue 02  |     |     |     |     |
| ---------------------- | --- | --- | --- | --- | --- | --- | --- | ----------------------- | --- | --- | --- | --- |
troughs in the subsequent months reflect lower cash inflows,  such as in the sixth and seventh months. These were months
which impact cash flow. This pattern of income suggests the  of  positive  financial  circumstances  with  excess  funds
need  for  financial  planning  that  was  able  to  adjust  to  available for investment purposes. In contrast, in months with
variability in cash inflows, as opposed to assuming a constant  lower  (or  negative)  savings,  investment  did  not  decrease
level of income.  accordingly, suggesting the use of previous savings, other
  In terms of modeling, the observed income fluctuations  sources  of  funds,  or  planned  investment  amounts.  This
highlight the need to use time series forecasting models in the  represents a risk factor, as ongoing investment during low
analysis. Time-series models like LSTM are able to learn and  savings months can impact cash flow and liquidity.
predict future income trends from past data. Such forecasts    From a modeling perspective, the savings-investment
allow  for  forward-looking  planning,  taking  into  account  variability highlights the need for incorporating adaptive and
variations  and  adapting  strategies  accordingly.  The  intelligent decision-making. Conventional financial strategies
incorporation of such information with other factors, such as  that rely on fixed savings-investment relationships not capture
behavioral and contextual information, improves the ability to  the variability. Savings and investment relationships can be
provide relevant, realistic financial advice.  learned in adaptive models, such as reinforcement learning,
  The understanding how income distributions impact the  which  adapt  to  financial  circumstances  and  long-term
ability to achieve financial goals was crucial. Fluctuations in  financial goals. This allows more realistic and contextual
income affect savings and investment capacities, both of  financial advice and better matching of financial advice to
which  are  crucial  in  achieving  financial  goals.  These  current financial resources and long-term objectives.
variations  can  be  factored  into  models  for  validating    What's more, the interdependence between savings and
feasibility to provide more reliable estimates of the likelihood  investment was important to achieve long-term financial goals
of success. This graph provides insights that can be used to  and determine the possibility of achieving financial goals.
develop flexible financial planning strategies that are in line  Optimal investing during high-savings periods can enhance
with real-time income variability to enhance decision-making  the  chances  of  attaining  financial  goals,  whereas  poor
and financial stability.  investment during low-savings periods can lead to financial
  risk. This can be used to inform feasibility models to make
more accurate predictions and recommendations. The graph
analysis supports the creation of well-rounded and flexible
financial strategies, which consider the financial capacity and
dynamic changes in the financial market.
Table 2. Savings and Investment Allocation
|     |     |     |     |     |     | Month  |     | Savings  |     | Investment  |        |     |
| --- | --- | --- | --- | --- | --- | ------ | --- | -------- | --- | ----------- | ------ | --- |
|     |     |     |     |     |     | 1      |     | 31000    |     |             | 18000  |     |
|     |     |     |     |     |     | 2      |     | -17000   |     |             | 21000  |     |
|     |     |     |     |     |     | 3      |     | 19000    |     |             | 34000  |     |
|     |     |     |     |     |     | 4      |     | 14000    |     |             | 13000  |     |
|     |     |     |     |     |     | 5      |     | 6000     |     |             | 33000  |     |

|     |     |     |     |     |     | 6   |     | 8000   |     |     | 27000  |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------ | --- | --- | ------ | --- |
|     |     |     |     |     |     | 7   |     | 51000  |     |     | 25000  |     |
FIGURE 5. Savings–Investment Allocation
|                                           |     |     |     |     |     | 8   |     | 15000  |     |     | 46000  |     |
| ----------------------------------------- | --- | --- | --- | --- | --- | --- | --- | ------ | --- | --- | ------ | --- |
| Patterns and Financial Decision Dynamics  |     |     |     |     |     | 9   |     | 10000  |     |     | 36000  |     |
|                                           |     |     |     |     |     | 10  |     | 3000   |     |     | 12000  |     |
|                                           |     |     |     |     |     | 11  |     | 3000   |     |     | 14000  |     |
The graph illustrates a comparison of monthly savings
|                   |          |                    |                |     |     | 12  |     | 20000  |     |     | 34000  |     |
| ----------------- | -------- | ------------------ | -------------- | --- | --- | --- | --- | ------ | --- | --- | ------ | --- |
| and  investment,  | showing  | the  distribution  | of  financial  |     |     |     |     |        |     |     |        |     |

resources. There was a clear variability in both parameters,
|     |     |     |     |     |     | The monthly allocation of savings and investment was  |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | ----------------------------------------------------- | --- | --- | --- | --- | --- | --- |
where savings are highly variable, including a negative saving
shown in Table 2, providing a glimpse of how surplus funds
in one month, and investments are quite stable but variable.
|                   |                 |             |           |         | were  | used  over  | the  | year.  The  | table  | reveals  | that  savings  |     |
| ----------------- | --------------- | ----------- | --------- | ------- | ----- | ----------- | ---- | ----------- | ------ | -------- | -------------- | --- |
| This  difference  | suggests  that  | investment  | was  not  | always  |       |             |      |             |        |          |                |     |
fluctuated considerably, with a negative value in the second
directly related to savings and that other factors (such as short-
month, whereas investment fluctuated less but at a higher
term planning or psychological factors) come into play. The
level. This discrepancy indicates that investment activity was
| disparity  between  | savings  | and  investment  | highlights  | the  |     |     |     |     |     |     |     |     |
| ------------------- | -------- | ---------------- | ----------- | ---- | --- | --- | --- | --- | --- | --- | --- | --- |
not exclusively driven by available savings but can also be
dynamics of financial behavior, in which individuals can still
explained by other factors such as previous savings, ongoing
invest low or negative savings.
|     |     |     |     |     | investments,  |     | or  financial  | planning  |     | strategies.  | The  | table  |
| --- | --- | --- | --- | --- | ------------- | --- | -------------- | --------- | --- | ------------ | ---- | ------ |
  A deeper look into the data shows some months where
|     |     |     |     |     | illustrates  | the  | intricacies  | of  | financial  | decision-making,  |     | in  |
| --- | --- | --- | --- | --- | ------------ | ---- | ------------ | --- | ---------- | ----------------- | --- | --- |
increased savings were associated with increased investment,
which investment trends do not necessarily correspond to

|                       |     |     |     |     |     |     |     |     |     |     |     |     |
| --------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Engineering Research  |     |     |     |     |     |     |     |     |     |     |     | 8   |

AI-Driven Goal Based Financial Planning System: A Framework for Contextual 2025, Vol 02. Issue 02
savings. range implies that most months involved mid-level income,
An examination of individual months shows that in some with a lower frequency of very high values suggesting
months, investment was positively associated with savings occasional high income. This pattern reflects the variable
(third, seventh, and twelfth months). These months represent nature of income generation and the need to consider income
times when positive financial situations allowed for increased patterns instead of just the average income.
funds to be allocated to investment. But in months where Upon inspection, the distribution of income values was
savings were lower or negative (e.g., the second month), not even, with clusters of values around particular ranges. The
investment was still high. This suggests the possibility of clusters show that there were periods of relative stability in
using accumulated savings or adhering to pre-set investment income, while the outliers in the higher ranges reflect
plans, allowing investment activity to continue short-term occasional increases. This due to bonuses, incentives, or
cash flow issues. This practice pose liquidity risks over the market conditions. The variability in this distribution implies
long term if not supported by sufficient savings. that income was not a stable quantity, and financial planning
The savings-investment nexus highlights the need for algorithms need to take into account the regularity of moderate
financial development and security. While investment during income together with the possibility of high-income events.
high-savings periods contributes to long-term savings, The distribution suggests that probability-based
investing during low-savings periods result in financial stress. approaches ought to be used in financial analysis. Rather than
This disalignment suggests the need for dynamic financial assuming income was a constant or certain value, by modeling
strategies that respond to the current financial situation. These income as a distribution, we can better predict future income
numbers show the need for allocation to be monitored in and generate scenarios. These distributions can be used to
relation to both balance and goals to maintain sustainability. enhance predictions in machine learning models and to
In terms of modeling and analysis, the insights shown in incorporate uncertainty in simulation-based analysis. This
the table highlight the need for smart investment strategies. helps to incorporate uncertainty and inform better decision-
Static models assuming a constant ratio of savings to making.
investment not be able to account for such patterns. Rather, The income distribution plays a significant role in
dynamic models such as reinforcement learning can be financial outcomes such as savings and wealth accumulation.
applied to learn allocation policies in response to financial Over-represented mid-income levels restrict the potential to
situations and long-term objectives. By considering these consistently generate surpluses, while periods of high incomes
patterns in the feasibility study, we can better estimate can dramatically enhance savings and investment
financial results while ensuring that the investment strategies opportunities. Understanding these distributions and
are consistent with risk preferences and financial constraints. incorporating them into validation of financial feasibility can
lead to better projections of financial feasibility. This
histogram provides information for building flexible strategies
to adapt financial planning to likely sources of earnings and
risk.
𝑆 = 𝐼 −𝐸 −𝐶 [1]
𝑡 𝑡 𝑡 𝑡
where C_t = contextual adjustments (inflation impact,
unexpected events)
Savings at the time were modeled not only as the
difference between income and expenses but also adjusted for
contextual factors such as inflation, emergencies, or economic
shocks. This formulation improved realism by capturing
external influences that directly affect disposable income. It
ensured that savings estimation reflected actual financial
conditions rather than idealized assumptions.
FIGURE 6. Income Distribution and 𝑋 = [𝐼 ,𝐸 ,𝑆 ,𝑅 ,𝐵 ,𝑀 ] [2]
𝑡 𝑡 𝑡 𝑡 𝑡 𝑡 𝑡
Frequency-Based Financial Stability Analysis
where
R_t = risk profile,
B_t = behavioral factors,
The histogram below shows the frequency of income
M_t = market conditions
values over the time period and provides a visual
The financial state at the time was represented as a
representation of how many values fall into each income
multidimensional vector combining financial, behavioral, and
range. The frequency values indicate that income spans a
contextual variables. This formulation enabled the system to
range of values, specifically mid-to-high income levels. The
process heterogeneous inputs simultaneously, forming the
relatively higher concentration of values in the lower mid-
foundation for machine learning and reinforcement learning
Engineering Research 9

|  Bidisha Patra 1et al  |     |     |     |     |     |     |     |     |     |     |     | 2025, Vol 02. Issue 02  |     |     |     |     |
| ---------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----------------------- | --- | --- | --- | --- |
models.  It  ensured  that  decision-making  incorporated  a  based on stochastic distributions. This enabled simulation of
holistic view of the user’s financial environment.  diverse financial futures under uncertainty. The approach
|     |     |     |     |     |     |     |     |     | provided a robust mechanism to evaluate possible outcomes  |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ---------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
𝑊 = 𝑊 +𝑆 +𝐴 ⋅𝑟                   [3]  rather than relying on single deterministic projections.
|     | 𝑡+1 | 𝑡   | 𝑡   | 𝑡   | 𝑡   |     |     |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |
𝑁
| where  |     |     |     |     |     |     |     |     |     |     | 1   |     |     |     |     |     |
| ------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
(𝑖)
A_t = investment allocation,  𝑃(𝐺) = ∑𝕀(𝑊 ≥ 𝐺)                [8]
𝑇
| r_t = return rate  |     |     |     |     |     |     |     |     |     |     | 𝑁   |     |     |     |     |     |
| ------------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
𝑖=1
|      | Wealth evolution was modeled as a function of savings  |           |     |       |           |           |     |      |     |     |     |     |     |     |     |     |
| ---- | ------------------------------------------------------ | --------- | --- | ----- | --------- | --------- | --- | ---- | --- | --- | --- | --- | --- | --- | --- | --- |
| and  | investment                                             | returns.  |     | This  | equation  | captured  |     | how  |     |     |     |     |     |     |     |     |
where I was an indicator function
accumulated savings and investment decisions contributed to
|     |     |     |     |     |     |     |     |     |     | The  | probability  | of  achieving  |     | a  financial  | goal  | was  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---- | ------------ | -------------- | --- | ------------- | ----- | ---- |
future wealth. The inclusion of returns introduced growth  computed as the proportion of simulated scenarios where final
dynamics, enabling the system to simulate long-term financial
wealth exceeded the target. This probabilistic formulation
trajectories required for goal achievement.
provided a realistic measure of success likelihood, supporting

informed financial decisions.
|     | 𝑌̂  | = 𝑓 | (𝑋 )                                [4]  |     |     |     |     |     |     |     |       |       |      |      |               |     |
| --- | --- | --- | ---------------------------------------- | --- | --- | --- | --- | --- | --- | --- | ----- | ----- | ---- | ---- | ------------- | --- |
|     | 𝑡+1 | 𝜃   | 𝑡                                        |     |     |     |     |     |     |     |       |       |      |      |               |     |
|     |     |     |                                          |     |     |     |     |     |     | 𝐴 = | 𝜋(𝑋 ) | = 𝜆 𝑆 | +𝜆 𝑅 | +𝜆 𝑀 |          [9]  |     |
|     |     |     |                                          |     |     |     |     |     |     | 𝑡   | 𝑡     | 1 𝑡   | 2 𝑡  | 3 𝑡  |               |     |
where f_θ represents a trained ML model (e.g., LSTM)

  Future financial variables such as income and expenses
|     |     |     |     |     |     |     |     |     |     | Investment  | allocation  | was  | determined using  |     | a  policy  |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----------- | ----------- | ---- | ----------------- | --- | ---------- | --- |
were predicted using a parameterized function learned from  function dependent on savings, risk tolerance, and market
historical data. This formulation generalized forecasting using  conditions.  The  weights  controlled  the  influence  of  each
machine learning models. It allowed the system to adapt to
factor. This formulation enabled dynamic and personalized
non-linear patterns and temporal dependencies, improving  allocation strategies aligned with both financial capacity and
prediction  accuracy  compared  to  traditional  statistical  external conditions.
approaches.

|     |     |     |     |     |     |     |     |     |     |     | 1 𝑛           |                                             |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------- | ------------------------------------------- | --- | --- | --- | --- |
|     |     |     |     |     |     |     |     |     |     |     | 𝐿(𝜃)= ∑(𝑌−𝑌̂) | 2 +‖𝜆‖‖𝜃‖2                            [10]  |     |     |     |     |
|     |     | 𝑇   |     |     |     |     |     |     |     |     |               | 𝑖 𝑖                                         |     |     |     |     |
𝑛
|     | max 𝔼[∑𝛾𝑡𝑅 |     |     | (𝑟𝑒𝑤𝑎𝑟𝑑) |                      |     |     |     |     |     | 𝑖=1 |     |     |     |     |     |
| --- | ---------- | --- | --- | -------- | -------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|     |            |     |     |          | ]               [5]  |     |     |     |     |     |     |     |     |     |     |     |
𝑡
𝜋   A regularized loss function was used to train predictive
𝑡=0
  models,  balancing  accuracy  and  model  complexity.  The
where  additional regularization term prevented overfitting, ensuring
π = policy,  that the model generalized well to unseen financial data. This
γ = discount factor  improved reliability in forecasting and decision-making.

|     | The  decision-making  |     |     | process  | was  | framed  |     | as  a  |     |     |     |     |     |     |     |     |
| --- | --------------------- | --- | --- | -------- | ---- | ------- | --- | ------ | --- | --- | --- | --- | --- | --- | --- | --- |
reinforcement learning problem, where the objective was to
| maximize  | cumulative  |     | rewards  | over  | time.  | Rewards  |     | were  |     |     |     |     |     |     |     |     |
| --------- | ----------- | --- | -------- | ----- | ------ | -------- | --- | ----- | --- | --- | --- | --- | --- | --- | --- | --- |
defined based on goal progress, risk control, and financial
| stability.  | This  | formulation  |     | enabled  |     | adaptive  | strategy  |     |     |     |     |     |     |     |     |     |
| ----------- | ----- | ------------ | --- | -------- | --- | --------- | --------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
optimization through continuous learning and feedback.

𝑊
𝑡
|     | 𝐹 = 𝜎(𝛼 |     | +𝛽𝑆 | +𝛾𝑅 | +𝛿𝑀 | )        [6]  |     |     |     |     |     |     |     |     |     |     |
| --- | ------- | --- | --- | --- | --- | ------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|     | 𝑡       |     |     | 𝑡   | 𝑡   | 𝑡             |     |     |     |     |     |     |     |     |     |     |
𝐺

where
G = goal target,
σ = sigmoid function

  The feasibility of achieving a financial goal was modeled
| as  | a  normalized  | score  | between  |     | 0  and  | 1.  The  | equation  |     |     |     |     |     |     |     |     |     |
| --- | -------------- | ------ | -------- | --- | ------- | -------- | --------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
FIGURE 7. Risk Score Distribution and
combined wealth progress, savings capacity, risk level, and
market  conditions.  The  sigmoid  function  ensured  Investor Behavior Profiling
interpretability by converting outputs into probability-like
values. This formulation directly supported decision-making
and user feedback.
|     |     |     |     |     |     |     |     |     |     | The histogram shows the effect of variability in risk  |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------------------------------------------------ | --- | --- | --- | --- | --- | --- |
𝑊 (𝑖) = 𝑊 +𝑆 +𝐴 ⋅𝑟 (𝑖)          [7]  tolerance levels by depicting the distribution of risk scores
|     |     |     | 𝑡   | 𝑡   | 𝑡   |     |     |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|     | 𝑡+1 |     |     |     | 𝑡   |     |     |     |     |     |     |     |     |     |     |     |
  over time. The distribution of values along the scale suggests
risk attitudes were not narrowly focused but included low,
  Multiple scenarios were generated by varying return rates

|                       |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |
| --------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Engineering Research  |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     | 10  |

AI-Driven Goal Based Financial Planning System: A Framework for Contextual            2025, Vol 02. Issue 02
moderate, and high levels. The concentration of values in the  conservative financial strategy, and the progressive increase
lower  and  middle  ranges  indicates  that  more  individuals  in the latter months suggests a shift towards a more risk-prone
tended to exhibit low- to moderate-risk preferences rather than  strategy. This shows that financial decisions are affected by
higher-risk scores. This reflects the range of financial attitudes  dynamic  factors,  rather  than  being  constant,  and  so  it's
and suggests the need to account for different risk preferences  important to consider changing risk preferences in models.
in financial analyses.    A detailed analysis of the graph shows a gradual rise in
  Further analysis of the distribution shows that attitudes  the risk scores from the third month to the ninth month, where
towards risk varied over time. The lower scores correspond to  the scores peak. This increase indicates greater confidence in
periods of caution, perhaps reflecting a response to uncertain  financial choices, which due to a positive change in financial
financial conditions or less stable earnings. On the other hand,  status (increased earnings and/or savings). On the other hand,
the higher scores indicate periods of heightened financial  the downward trend in the last few months suggests a shift
decision-making  confidence,  which  attributed  to  more  back towards more conservative attitudes. These changes
positive circumstances such as greater income or the ability to  show the dynamic aspect of risk tolerance, which can change
save.  This  finding  highlights  the  dynamic  nature  of  risk  at different points in time due to both personal financial
tolerance,  which  can  shift  based  on  both  financial  and  situations and economic conditions.
economic circumstances.    The  risk  score  fluctuations  also  suggest  the  human
  For  the  modeling  part,  this  variability  suggests  behavior involved in financial planning. Increased financial
incorporating  adaptive  risk  classification  methods.  While  capacity (such as surplus cash) or financial pressures can
traditional methods of risk classification not capture these  affect an individual's risk tolerance. Generally, a higher risk
variations, machine learning can classify and update risk  score reflects a willingness to invest in assets that provide
status based on financial variables. This dynamic approach  greater returns but come with greater risks. This relationship
improves financial advice accuracy by tailoring it to observed  highlights the importance of considering behavioral insights
behaviors. The risk variability in models enhances decision- in  financial  decision-making  models.  This  connection
making outcomes by considering uncertainty in risk behavior.  highlights the need to integrate behavioral finance in financial
|   The distribution of risk scores was essential in financial  |     |     |     | models.  |     |     |
| ------------------------------------------------------------- | --- | --- | --- | -------- | --- | --- |
strategizing  and  achieving  goal  feasibility.  Conservative    The table's data suggests that from an analytical point of
strategies  can  be  executed  with  lower  risk  preferences,  view, dynamic risk profiling ought to be used. A fixed risk
potentially stunting growth in the long term, whereas higher  profile  not  account  for  these  variations  and  result  in
risk  preferences  can  be  reflective  of  more  aggressive  suboptimal  suggestions.  Adaptive  risk  profiling  through
investment strategies, which have greater potential returns but  machine learning can monitor and adapt to changing financial
with higher risks. Incorporating these trends into the analytical  trends, allowing strategies to be in line with preferences.
and validation framework can ensure that financial strategies  Incorporating these risk scores into the decision-making and
are  tailored  to  individual  preferences  and  abilities.  The  feasibility assessment processes increases the effectiveness
information obtained from this graph helps to inform more  and personalization of financial planning, resulting in a more
individualized, contextualized, and realistic financial advice  effective system.
| and promote adaptability.  |     |     |     |     |     |     |
| -------------------------- | --- | --- | --- | --- | --- | --- |
Table 3. Risk Score Distribution

|     | Month  | Risk Score  |     |     |     |     |
| --- | ------ | ----------- | --- | --- | --- | --- |
|     | 1      | 2.1         |     |     |     |     |
|     | 2      | 1.5         |     |     |     |     |
|     | 3      | 3.8         |     |     |     |     |
|     | 4      | 4.5         |     |     |     |     |
|     | 5      | 5.2         |     |     |     |     |
|     | 6      | 6.0         |     |     |     |     |
|     | 7      | 7.5         |     |     |     |     |

|          | 8                      | 8.2        |                    |                                            |                      |     |
| -------- | ---------------------- | ---------- | ------------------ | ------------------------------------------ | -------------------- | --- |
|          | 9                      | 9.0        |                    | FIGURE 8. Expense Distribution and Budget  |                      |     |
|          | 10                     | 2.8        |                    |                                            |                      |     |
|          | 11                     | 3.5        |                    |                                            | Allocation Analysis  |     |
|          | 12                     | 4.2        |                    |                                            |                      |     |
|   Table  | 3  shows the  monthly  | variation  | of  risk  scores,  |                                            |                      |     |
  The pie chart below illustrates the relative proportions of
indicating the level of risk tolerance. The scores are low to
high, suggesting that there were changes in preferences over  expenditure  across  key  expenditure  categories,  thereby
time. The risk scores in the first few months indicate a  providing insights into this household's resource allocation.

|                       |     |     |     |     |     |      |
| --------------------- | --- | --- | --- | --- | --- | ---- |
| Engineering Research  |     |     |     |     |     | 11   |

Bidisha Patra 1et al 2025, Vol 02. Issue 02
The highest proportion of expenditure (40%) was allocated to allocating funds to other needs.
rent, which means that housing was the biggest expense. The breakdown shows the difference between fixed and
Housing was followed by food (25%), miscellaneous variable costs in the distribution. Rent was a fixed expense that
expenses (20%), and transportation (15%). The allocation was relatively stable, creating challenges in adjusting
reflects the prominence of basic living expenses in the overall consumption patterns to financial challenges. While food
expenditure, which was common in financial allocation, with costs are a necessity, present few opportunities for cost
fixed and necessary expenses taking up a significant savings, whereas transportation and other miscellaneous
proportion of income. expenses are areas where savings can be made. This
This distribution can be further analyzed in terms of the distinction was crucial in determining which costs can be
relatively large share of rent, which reduce the flexibility to optimized through cost control measures to enhance financial
adjust spending on other items. Being a fixed and rigid efficiency.
expenditure, housing costs limit the flexibility in budget The distribution was also indicative of its effect on
adjustment under financial pressures. Likewise, food costs, as savings and security. An increase in the proportion of income
a necessity, also have a fixed proportion. On the other hand, allocated to fixed expenses result in a decrease in the surplus
expenses like transport and miscellaneous expenses are available for savings and investment. This limitation impact
adjustable. Knowing the flexible items was essential for the accomplishment of financial goals, particularly in times of
enhancing financial efficiency and allowing for resource reduced earnings. On the other hand, controlling variable
allocation. expenses and related areas can facilitate surplus creation,
For analytics, the breakdown of expenses offers insights which can in turn improve financial stability and the ability to
for financial analysis and planning. The high fixed expense achieve financial goals.
ratio indicates a tight financial structure, with limited income The expense distribution was an essential component in
to allocate for savings and investments. This finding justifies financial analysis and decision-making. It offers insights into
the role of smart systems in uncovering potential expense resource allocation, allowing for more precise and tailored
reductions and suggesting spending optimization. Models can financial planning. By taking into account these distribution
provide specific recommendations for improved balance patterns in forecasting and feasibility studies, it was possible
while meeting basic needs by examining spending categories. to provide customized advice for improved consumer
Also, the spending pattern of the household was expenditure. This aids in more holistic financial planning,
important for saving and future financial well-being. An prioritizing essential expenses and optimizing savings and
increased share of the income spent on non-flexible investment opportunities.
expenditures decreases the generation of surplus, which
further impacts the capacity to reach targets. The inclusion of
such distribution of expenses into the analysis and validation
process leads to an improved feasibility assessment. The
graph provides insights for creating individualized financial
plans that balance needs with savings and investment goals,
leading to better financial security and achievement of
financial goals.
Table 4. Expense Distribution
Category Percentage (%)
Rent 40
Food 25
FIGURE 9. Correlation Matrix of Financial
Transport 15
Others 20 Variables and Interdependency Analysis
Table 4 shows the shares of expenses in different
categories, which provides an overview of financial The heatmap displays the correlation between various
allocation. It shows that the highest proportion was spent on financial variables, providing an overall picture of
rent (40%), followed by food (25%), other expenses (20%), interdependencies in the financial system. Positive
and transportation (15%). This allocation was consistent with correlations are shown in warmer colors and negative
the typical financial allocation pattern, with fixed and non- correlations in cooler colors. For instance, a high positive
discretionary expenses playing a prominent role. The correlation was observed between income and savings, which
allocation to housing expenses was relatively large, implying implies that a higher income leads to greater savings. This
that a large part of the total income was spent on fixed finding supports the basic financial fact that income was one
expenses that left less room for financial flexibility in of the key factors driving excess or surplus, which was crucial
Engineering Research 12

AI-Driven Goal Based Financial Planning System: A Framework for Contextual            2025, Vol 02. Issue 02
in the attainment of financial goals.    A  strong  negative  correlation  was  found  between
  Conversely,  there  was  a  highly  negative  correlation  expenses and savings, implying that higher expenses were
between  expenses  and  savings,  suggesting  that  increased  associated  with  less  surplus  generated.  This  correlation
spending trends reduce savings. This negative correlation  underscores the importance of managing expenses to ensure
underscores the importance of managing expenses to achieve  financial  stability.  Further,  there  was  a  weak  positive
financial stability. There are moderate positive correlations  correlation  identified  between  income  and  investment,
between  income  and  investment,  indicating  that  higher  implying that increased earnings led to increased investment.
incomes  allow  for  more  investment.  These  correlations  These correlations reveal the interdependence between the
underline the interconnected nature of financial parameters  various financial variables and how a change in one variable
and how a change in one variable can affect multiple financial  affects the others.
factors.    The correlation between risk score and other variables has
  The  correlation  with  risk  score  shows  moderate  lower correlations with savings and income, but a moderate
relationships with investment and income, suggesting that risk  positive correlation with investment. This suggests that risk
levels are driven by income and potentially impact investment  score was more relevant to the investment decisions rather
strategies. Weaker associations with savings indicate that the  than savings. Participants with higher risk scores were more
risk score does not directly influence savings patterns but was  likely to invest (perhaps in an attempt to achieve greater
more  important  in  influencing  how  savings  are  used  for  returns the heightened risk). This trend highlights the role of
investment purposes. This finding suggests the importance of  behavioral finance in shaping investment strategies and how
considering behavioral factors in analytical models, as risk  psychology plays a role in how people invest their money.
behavior can influence financial decisions.    From a modeling standpoint, the correlation matrix offers
  In terms of model building, the correlation matrix offers  insights for model building and feature engineering. Positive
insights for feature selection. Strongly correlated variables can  correlations can be used to improve the accuracy of models,
be  used  to  enhance  predictive  accuracy,  and  negatively  whereas negative correlations indicate where improvements
correlated variables indicate aspects to be fine-tuned. These  are needed. These relationships allow their development of
relationships help to develop better financial models. Using  richer, more contextual financial models. The inclusion of
these relationships to inform the modeling of future financial  these  relationships  in  forecasting,  decision-making,  and
outcomes, decision-making, and the assessment of financial  feasibility checks in the system allows for more precise and
feasibility, we can enhance the generation of financial advice  relevant recommendations, enhancing financial planning.
| and so improve financial planning systems.  |     |     |     |     |     |     |     |     |     |
| ------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Conclusion
| Table 5. Correlation Between Financial  |     |     |     |     |     |     |     |     |     |
| --------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Variables  • A  successful  AI-based  approach  to  goal-oriented
|     |     |     |     | financial  | planning  | was  | implemented,  |     | using  |
| --- | --- | --- | --- | ---------- | --------- | ---- | ------------- | --- | ------ |
Variabl Inco Expens Savin Risk  Investme predictive, behavioral, and contextual information.
• The research showed that current financial planning
| es  me        | es  gs      | Scor nt  |            |                                                    |           |             |              |     |           |
| ------------- | ----------- | -------- | ---------- | -------------------------------------------------- | --------- | ----------- | ------------ | --- | --------- |
|               |             | e        |            | methods were not flexible and didn't consider the  |           |             |              |     |           |
| Income  1.00  | 0.25  0.70  | - 0.45   |            | dynamic reality.                                   |           |             |              |     |           |
|               |             |          | • Machine  |                                                    | learning  | techniques  | efficiently  |     | captured  |
0.20
Expense 0.25  1.00  -0.60  0.15  0.30  financial trends and enhanced forecasts for income,
| s              |              |         |                  | expenses, and savings.  |                  |          |           |             |           |
| -------------- | ------------ | ------- | ---------------- | ----------------------- | ---------------- | -------- | --------- | ----------- | --------- |
|                |              |         | • Reinforcement  |                         | learning         | allowed  |           | dynamic     | decision- |
| Savings  0.70  | -0.60  1.00  | - 0.20  |                  |                         |                  |          |           |             |           |
|                |              | 0.25    |                  | making                  | by  continually  |          | adapting  | investment  |           |
Risk  -0.20  0.15  -0.25  1.00  0.35  strategies to financial and market environments.
• The use of Monte Carlo simulation allowed us to model
Score
Investm 0.45  0.30  0.20  0.35  1.00  the probability of achieving financial objectives.
| ent  |     |     | • Situational  |          | awareness           | improved  |            | personalization  |       |
| ---- | --- | --- | -------------- | -------- | ------------------- | --------- | ---------- | ---------------- | ----- |
|      |     |     |                | through  | the  consideration  |           | of  human  | factors,         | risk  |

  Table  5  shows  the  correlation  matrix  between  key  preferences, and macroeconomic conditions.
financial factors, providing a numerical representation of their  • The system provided feasibility scores and specific
relationships. The numbers vary from -1 to 1, representing the  recommendations for decision support, enhancing
intensity  of  the  relationships  between  income,  expenses,  financial planning and decision-making.
savings,  risk  score,  and  investment.  A  high  positive  • Benchmarking suggested better performance in terms
correlation  was  noticed  between  income  and  savings,  of accuracy, flexibility, and realism than existing
implying that increased income was correlated with increased  rule-based financial systems.
surplus. This correlation supports the vital importance of  • The use of various AI techniques in an integrated
income in building financial resilience and achieving financial  system  filled  the  gap  in  financial  planning  and
| goals.  |     |     |     | feasibility assessment.  |     |     |     |     |     |
| ------- | --- | --- | --- | ------------------------ | --- | --- | --- | --- | --- |

|                       |     |     |     |     |     |     |     |     |      |
| --------------------- | --- | --- | --- | --- | --- | --- | --- | --- | ---- |
| Engineering Research  |     |     |     |     |     |     |     |     | 13   |

|  Bidisha Patra 1et al  |     |     |     |     |     |     |     |     |     | 2025, Vol 02. Issue 02  |     |     |     |     |
| ---------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----------------------- | --- | --- | --- | --- |
• The  proposed  system  provided  an  intelligent  and  Leadership.
scalable solution that be applied to various real-world  [9]  Talasila, S. D. (2024). AI-driven personal finance
|     |            |     |          |          |                    |     |     | management:  |     | Revolutionizing  |     | budgeting  |     | and  |
| --- | ---------- | --- | -------- | -------- | ------------------ | --- | --- | ------------ | --- | ---------------- | --- | ---------- | --- | ---- |
|     | scenarios  | in  | fintech  | systems  | and  personalized  |     |     |              |     |                  |     |            |     |      |
financial advice services.  financial planning. International Research Journal of
Engineering and Technology, 11(7), 397-407.
Data Availability Statement  [10] Sholapurapu, P. K. (2024). AI-based financial risk
assessment tools in project planning and execution.
All data utilized in this study have been incorporated into the  Project Planning and Execution (March 01, 2024).
| manuscript.  |     |     |     |     |     |     |              | European Economic Letters, 14(1).  |         |          |      |             |     |          |
| ------------ | --- | --- | --- | --- | --- | --- | ------------ | ---------------------------------- | ------- | -------- | ---- | ----------- | --- | -------- |
|              |     |     |     |     |     |     | [11] Duong,  |                                    | C.  D.  | (2025).  | How  | AI‐enabled  |     | drivers  |
Authors’ Note   inspire  sustainability‐oriented  entrepreneurial
intentions: Unraveling the (in) congruent effects of
|      |          |                |        |         |           |               |     | perceived  | desirability  |     | and  | feasibility  | from  | the  |
| ---- | -------- | -------------- | ------ | ------- | --------- | ------------- | --- | ---------- | ------------- | --- | ---- | ------------ | ----- | ---- |
| The  | authors  | declare  that  | there  | is  no  | conflict  | of  interest  |     |            |               |     |      |              |       |      |
regarding the publication of this article. Authors confirmed  entrepreneurial event model perspective. Sustainable
that the paper was free of plagiarism.  Development, 33(4), 6228-6246.
|     |     |     |     |     |     |     | [12] Bessa,  |     | G.,  &  | Barbosa,  | B.  | (2025).  | Integrating  |     |
| --- | --- | --- | --- | --- | --- | --- | ------------ | --- | ------- | --------- | --- | -------- | ------------ | --- |

|     |     |     |     |     |     |     |     | Artificial  | Intelligence  |     | into  scenario  |     | analysis:  | A   |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------- | ------------- | --- | --------------- | --- | ---------- | --- |
References
validated framework for strategic planning under

economic uncertainty. Global Economics Research,
|     | [1]  Addy, W. A., Ajayi-Nifise, A. O., Bello, B. G., Tula,  |           |      |              |     |              |               | 100007.  |               |     |                  |     |     |         |
| --- | ----------------------------------------------------------- | --------- | ---- | ------------ | --- | ------------ | ------------- | -------- | ------------- | --- | ---------------- | --- | --- | ------- |
|     | S.  T.,                                                     | Odeyemi,  | O.,  | &  Falaiye,  |     | T.  (2024).  |               |          |               |     |                  |     |     |         |
|     |                                                             |           |      |              |     |              | [13] Sharma,  |          | A.,  Kabade,  |     | S.,  Chaudhari,  |     | B.  | B.,  &  |
Transforming  financial  planning  with  AI-driven  Kagalkar, A. (2025, August). Optimizing Retirement
analysis: A review and application insights. World  Income  Adequacy  with  AI-Based  Personalized
Journal of Advanced Engineering Technology and
|     |     |     |     |     |     |     |     | Financial  | Planning  | Systems.  |     | In  | 2025  | Global  |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------- | --------- | --------- | --- | --- | ----- | ------- |
Sciences, 11(1), 240-257.  Conference  on  Information  Technology  and
[2]  Abdellatef, A. (2025). How AI was Redefining the  Communication  Networks  (GITCON)  (pp.  1-10).
|     | Future  | of  Financial  |     | Planning  | and  | Analysis:  |     |     |     |     |     |     |     |     |
| --- | ------- | -------------- | --- | --------- | ---- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- |
IEEE.
Transforming financial planning and analysis with
|     |     |     |     |     |     |     | [14] Thiyagarajan,  |     | V.  | (2024).  | Expectation:  |     | AI-driven  |     |
| --- | --- | --- | --- | --- | --- | --- | ------------------- | --- | --- | -------- | ------------- | --- | ---------- | --- |
AI-driven insights. Strategic Finance.  forecasting and scenario planning in planning and
[3]  Gadam,  H.,  &  Upadhyay,  A.  (2023).  AI-Driven  budgeting  cloud  service  (PBCS).  International
|     | Financial   | Planning:  |     | A  Study  | on  | Predictive  |     |                                             |             |      |             |     |         |     |
| --- | ----------- | ---------- | --- | --------- | --- | ----------- | --- | ------------------------------------------- | ----------- | ---- | ----------- | --- | ------- | --- |
|     |             |            |     |           |     |             |     | Journal                                     | on  Recent  | and  | Innovation  |     | Trends  | in  |
|     | Modelling.  |            |     |           |     |             |     | Computing and Communication, 9(12), 75-85.  |             |      |             |     |         |     |
[4]  Omoruyi,  N.  (2025).  Advanced  Computational  [15] Rainy, T. A., Goswami, D., Rabbi, M. S., & Al
Methods for Financial Planning and Analysis Risk
|     |     |     |     |     |     |     |     | Maruf,  | A.  (2023).  | A   | Systematic  | Review  |     | of  AI- |
| --- | --- | --- | --- | --- | --- | --- | --- | ------- | ------------ | --- | ----------- | ------- | --- | ------- |
Assessment  using  Data  Science-Driven  Model  Enhanced Decision Support Tools in Information
Validation  Techniques.  International  Journal  of  Systems: Strategic Applications In Service-Oriented
|     | Research      | Publication  |     | and  | Reviews.          | doi:  |     |              |      |             |            |     |         |     |
| --- | ------------- | ------------ | --- | ---- | ----------------- | ----- | --- | ------------ | ---- | ----------- | ---------- | --- | ------- | --- |
|     |               |              |     |      |                   |       |     | Enterprises  | And  | Enterprise  | Planning.  |     | Review  | of  |
|     | https://www.  |              |     |      | semanticscholar.  |       |     |              |      |             |            |     |         |     |
Applied Science and Technology, 2(01), 26-52.
org/paper/4d27d96c40e20c0bd7df2d9220bd4b355a [16] Celestin, M., Vasuki, M., Kumar, A. D., & Asamoah,
|     | 381c82.  |     |     |     |     |     |     | P. J. (2025). AI-Driven Risk Forecasting Theory.  |     |     |     |     |     |     |
| --- | -------- | --- | --- | --- | --- | --- | --- | ------------------------------------------------- | --- | --- | --- | --- | --- | --- |
[5]  Mlybari, E. A., & Elgohary, H. A. (2025). AI-driven
|     |     |     |     |     |     |     |     | International  | American  |     | Council  | for  | Research  | &   |
| --- | --- | --- | --- | --- | --- | --- | --- | -------------- | --------- | --- | -------- | ---- | --------- | --- |
value management in construction: a theoretically- Development.
grounded  framework  with  empirical  validation.  [17] Bukovski, K., Jain, K., Cummins, M., Bowden, J.,
Journal of Umm Al-Qura University for Engineering
Tetteh, G. K., & Khang, Z. (2025). From crisis to
and Architecture, 16(4), 1686-1705.  prosperity: AI and open finance for holistic financial
[6]  OJO,  O.,  Akinadewo,  I.  S.,  Duduyegbe,  S.  S.,  health and smart future planning.
Akinola, J. F., & Omolade, O. T. (2025). AI-driven
[18] Sepanosian, T., Milosevic, Z., & Blair, A. (2024,
|     | decision-making  |     | in  | financial  | management.  |     |     |              |          |     |               |     |     |           |
| --- | ---------------- | --- | --- | ---------- | ------------ | --- | --- | ------------ | -------- | --- | ------------- | --- | --- | --------- |
|     |                  |     |     |            |              |     |     | September).  | Scaling  |     | AI  adoption  |     | in  | finance:  |
International  journal  of  economics  and  business  modelling framework and implementation study. In
management, 1, 644.  International  Conference  on  Enterprise  Design,
|     | [7]  Cortez,  | A.  | M.  (2025).  | Integrating  |     | AI-Driven  |     |     |     |     |     |     |     |     |
| --- | ------------- | --- | ------------ | ------------ | --- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- |
Operations, and Computing (pp. 221-236). Cham:
Predictive  Analytics,  Uncertainty  Quantification,  Springer Nature Switzerland.
and  Robust  Model  Validation  for  Financial  [19] Saleela, D., Oyegoke, A., Dauda, J. A., & Ajayi, S.
|     | Forecasting  | and  | Autonomous  |     | Decision  | Systems.  |     |          |              |        |      |            |           |     |
| --- | ------------ | ---- | ----------- | --- | --------- | --------- | --- | -------- | ------------ | ------ | ---- | ---------- | --------- | --- |
|     |              |      |             |     |           |           |     | (2025).  | Feasibility  | study  | for  | AI-Driven  | Decision  |     |
International Journal of Modern Medicine, 4(09), 13- Support  System  for  Personalised  Housing
|     | 19.           |     |          |             |      |            |                | Adaptations and Assistive Technology.  |          |           |      |            |     |          |
| --- | ------------- | --- | -------- | ----------- | ---- | ---------- | -------------- | -------------------------------------- | -------- | --------- | ---- | ---------- | --- | -------- |
|     | [8]  Hesami,  | S.  | (2025).  | Navigating  | the  | AI-driven  |                |                                        |          |           |      |            |     |          |
|     |               |     |          |             |      |            | [20] Ashiedu,  |                                        | B.  I.,  | Ogbuefi,  | E.,  | Nwabekee,  |     | U.  S.,  |
transformation of personal finance: opportunities,
|     |     |     |     |     |     |     |     | Ogeawuchi,  | J.  | C.,  &  | Abayomi,  |     | A.  A.  | (2023).  |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------- | --- | ------- | --------- | --- | ------- | -------- |
challenges,  and  ethical  imperatives.  Strategy  &  Designing Financial Intelligence Systems for Real-

|                       |     |     |     |     |     |     |     |     |     |     |     |     |     |     |
| --------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Engineering Research  |     |     |     |     |     |     |     |     |     |     |     |     |     | 14  |

AI-Driven Goal Based Financial Planning System: A Framework for Contextual 2025, Vol 02. Issue 02
Time Decision-Making in African Corporates. [30] Faqihi, A., & Miah, S. J. (2023). Artificial
Journal of Frontiers in Multidisciplinary Research, intelligence-driven talent management system:
4(2), 68-81. Exploring the risks and options for constructing a
[21] Ahirrao, Y. S., Ansari, I., Azim, K. S., Bhujel, K., & theoretical foundation. Journal of Risk and Financial
Panchal, S. S. (2025). AI-Powered Financial Management, 16(1), 31.
Strategy: Transforming Business Decision-Making [31] Arun, M., Barik, D., Chandran, S. S., Praveenkumar,
Through Predictive Analytics. Emerging Frontiers S., & Tudu, K. (2025). Economic, policy, social, and
Library for The American Journal of Engineering regulatory aspects of AI-driven smart buildings.
and Technology, 7(09), 126-151. Journal of building engineering, 99, 111666.
[22] Tanim, S. H., & Ahmad, M. S. (2025). AI driven [32] Hossain, M. S., Sikdar, M. S. H., Chowdhury, A.,
strategic decision-making in IT project management: Bhuiyan, S. M. Y., & Mobin, S. M. (2025). AI-driven
Enhancing risk assessment, cost control, and aggregate planning for sustainable supply chains: A
efficiency. Available at SSRN. systematic literature review of models, applications,
[23] Rong, C. (2024). An AI-driven decision framework and industry impacts. American Journal of Advanced
for promoting sustainable entrepreneurship in Technology and Engineering Solutions, 1(01), 382-
vocational colleges. Decision Making: Applications 437.
in Management and Engineering, 7(2), 748-769. [33] Artene, A. E., Domil, A. E., & Ivascu, L. (2024).
[24] Ayankoya, M. B., Omotoso, S. S., & Ogunlana, A. Unlocking business value: Integrating AI-driven
A. (2025). Data Driven Financial Optimization for decision-making in financial reporting systems.
Small and Medium Enterprises (SMEs): A Electronics, 13(15), 3069.
Framework to Improve Efficiency and Resilience in [34] Arshad, N., Butt, T. A., & Iqbal, M. (2025). A
US Local Economies. International Journal of comprehensive framework for Intelligent, Scalable,
Management and Organizational Research, 4(4), 90- and Performance-Optimized software development.
97. IEEE Access, 13, 74062-74077.
[25] Talib, A. M., Al-Hgaish, A. M., Atan, R. B., [35] J. Nair, A., Manohar, S., & Mittal, A. (2025). AI-
Alshammari, A., Alomary, F. O., Yaakob, R., ... & enabled FinTech for innovative sustainability:
Osman, M. H. (2025). Evaluating critical success promoting organizational sustainability practices in
factors in AI-driven drug discovery using AHP: a digital accounting and finance. International Journal
strategic framework for optimization. IEEE Access, of Accounting & Information Management, 33(2),
13, 42045-42063. 287-312.
[26] Sadri, H. (2025). AI-driven integration of digital [36] Chukwuma-Eke, E. C., Ogunsola, O. Y., & Isibor, N.
twins and blockchain for smart building management J. (2022). A conceptual framework for financial
systems: A multi-stage empirical study. Journal of optimization and budget management in large-scale
Building Engineering, 105, 112439. energy projects. International Journal of
[27] Ahmed, A., Shah, A., Ahmed, T., Yasin, S., Longa, Multidisciplinary Research and Growth Evaluation,
F. E. A., Hussaini, W., & Zubair, M. (2025). AI- 2(1), 823-834.
Driven Innovations in Modern Banking: From [37] Grabocka, E., & Ndoka, E. (2025). AI-driven
Secure Digital Transactions to Risk Management, innovation within the ICT sector. Smart Cities and
Compliance Frameworks, and AI-Based ATM Regional Development (SCRD) Journal, 9(1), 77-97.
Forecasting Systems. Journal of Management [38] Yang, H., Lin, L., She, Y., Liao, X., Wang, J., Zhang,
Science Research Review, 4(3), 1145-1183. R., ... & Wang, C. D. (2025). FinRobot: Generative
[28] Mahamad, S., Chin, Y. H., Zulmuksah, N. I. N., Business Process AI Agents for Enterprise Resource
Haque, M. M., Shaheen, M., & Nisar, K. (2025). Planning in Finance. arXiv preprint
Technical review: Architecting an AI-driven arXiv:2506.01423.
decision support system for enhanced online learning [39] Jahid, M. S. R. (2025). AI-driven optimization and
and assessment. Future Internet, 17(9), 383. risk modeling in strategic economic zone
[29] Ayodeji, D. C., Oladimeji, O., Ajayi, J. O., development for mid-sized economies: A review
Akindemowo, A. O., Eboseremen, B. O., Obuse, E., approach. International Journal of Scientific
... & Erigha, E. D. (2022). Operationalizing analytics Interdisciplinary Research, 6(1), 185-218.
to improve strategic planning: A business [40] De Zarzà, I., De Curtò, J., Roig, G., & Calafate, C. T.
intelligence case study in digital finance. Journal of (2023). Optimized financial planning: integrating
Frontiers in Multidisciplinary Research, 3(1), 567- individual and cooperative budgeting models with
578. LLM recommendations. AI, 5(1), 91-114.
Engineering Research 15

Bidisha Patra 1et al 2025, Vol 02. Issue 02
© Bidisha Patra, Samadrita Sarkar, Sneha Pal, Sreejani Ghosh, and Prof. Sujoy Datta. 2024
Open Access. This article is distributed under the terms of the Creative Commons Attribution 4.0
International License (http://creativecommons.org/licenses/by/4.0/), which permits unrestricted use,
distribution, and reproduction in any medium, provided you give appropriate credit to the original author(s)
and the source, provide a link to the Creative Commons license, and indicate if changes were made.
Embargo period: The article has no embargo period.
To cite this Article: To cite this Article: Bidisha Patra, Samadrita Sarkar, Sneha Pal, Sreejani Ghosh, and
Prof. Sujoy Datta, AI-Driven Goal Based Financial Planning System: A Framework for Contextual
Feasibility Validation,Engineering Research 1.1(2025):1-2. https://doi.org/10.71443/er.ar16
Engineering Research 16