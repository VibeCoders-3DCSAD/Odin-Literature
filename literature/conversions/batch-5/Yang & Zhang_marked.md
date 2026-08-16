---
conversion_metadata:
  converted_at: "2026-07-21T09:28:20Z"
  converter_tool: "markitdown"
  converter_version: "0.1.6"
  source_pdf: "Yang & Zhang.pdf"
  source_pdf_sha256: "6107819d962a8b613393fa067df069c4cb685b23f4ee1a1e249f854c4dcae2d1"
  page_count: 9
  markdown_char_count: 107126
---

<!-- PAGE-AWARE EXTRACTION (via pdfminer.six) -->

<!-- PAGE 1 -->

Journal  of Economic  Theory and Business  Management 
Journal  Home: https://www.suaspress.org/ojs/index.php/JETBM  | CODEN: JETBAU 
Vol. 3, No. 1, 2026 | ISSN 3006-4953 (Print) | ISSN 3006-4961 (Online)

Offline Conservative RL for Transaction Authorization: 
Smartly Balancing Fraud Risk and Customer Friction

XIMENG, Yang 1*  YIMING, Zhang 2

1 Board of Directors, Excellent  Era Lending Service Corp., Makati, Philippines, PH 
2 Department  of Financial Technology,  Peking University, Peking, China, CN

* XIMENG, Yang is the corresponding author, E-mail: Cocoliu898@gmail.com

Abstract:  This study instantiates credit strategy optimization at the transaction authorization layer, with actions approve, 
review,  and decline. Within an Offline Conservative RL (CQL) framework, we co -optimize fraud loss, operational burden 
from manual reviews, and customer friction from false positives and delays via a unified multi-objective cost function. Using a 
public credit-card transaction dataset with severe class imbalance, the learned policy improves total cost relative to cost -
sensitive supervised baselines, while  offering favorable trade-offs along a Pareto frontier between risk, operations, and 
friction. We detail the MDP design (state featurization, action space, and cost weights) and show that CQL mitigates out -of-
distribution overestimation in offline settings. The results indicate that conservative RL is a practical path for transaction -level 
credit decision-making that balances fraud risk with operational efficiency and user impact.

Keywords:   Offline Reinforcement Learning, Cost-Sensitive Credit Risk Optimization, User-Centric  Financial Decision 
Systems, Conservative Q-Learning CQL.

Disciplines: Business Analytics.

Subjects:  Econometric Modeling.

DOI:  https://doi.org/10.70393/6a6574626d.333932

ARK:  https://n2t.net/ark:/40704/JETBM.v3n1a01

1 INTRODUCTION

In  recent  years,

the  global  economy  has  been 
undergoing  profound  structural  changes,  with  intensified 
trade  frictions  and  heightened  geopolitical  uncertainty 
disrupting traditional patterns of growth and consumption. At 
the  same  time,  the  rapid  expansion of  digital  finance has 
made transaction-level credit card authorization a first line of 
defense for  consumer credit.  The  practical challenge  is  no 
longer  macro  demand  stimulation  per  se,  but rather 
controlling  fraud losses  without creating excessive customer 
friction (unnecessary declines or review  delays) in real  time. 
This 
trade-off—rather  than  aggregate 
consumption  effects—motivates  our  study  and  frames 
authorization  as  an  operations-  and  policy-optimization 
problem [1-3].

risk–experience

We

therefore

analyze transaction-level  decision 
policies  using  a  public,  severely  imbalanced  credit-card 
dataset with PCA-transformed  features  (V1–V28), Time (in 
seconds  since  the  first  transaction), and Amount (a  heavy-
tailed  distribution).  The  dataset is  used strictly  for  offline 
policy  learning  and  evaluation.  To  emulate  sequential 
deployment,  we 
through 
chronological  splits  and adopt conservative offline RL (e.g., 
CQL)  to learn policies  from logged  data , without requirin g 
online  experimentation,  thereby  aligning  with  operational

temporal  order

preserve

safety and governance expectations.

experimentation[5].  By

Taken  together,  these  developments  underscore  the 
need for innovative methodologies that balance risk control 
and  consumer  welfare  [4].  Reinforcement  learning  (RL), 
particularly in  its  offline and conservative variants, offers a 
promising approach for data-driven policy optimization from 
historical  logs,  thereby eliminating  the need for costly  real-
leveraging  user-centric 
time 
behavioral  data and  incorporating  multi-objective  reward 
functions,  such  methods  can  co-optimize  credit  risk  and 
incentive strategies, ensuring  that consumer lending not only 
boosts demand but also  safeguards financial  stability.  This 
study contributes  to  this  emerging  literature  by  empirically 
analyzing the co-optimization of credit risk management and 
incentive design  through offline conservative reinforcement 
learning,  situating  consumer  credit  as  both  a  driver  of 
domestic demand and a financial asset class with distinct risk 
properties.

2 RELATED WORK

2.1 CREDIT PRICING AND AUTHORIZATION

STRATEGIES

Traditional  studies  in  consumer credit  have primarily 
focused on risk-based and profit-based pricing, where lenders

Published By SOU THERN UNITED ACADEMY OF SCIENCES LIMITED  
Copyright ©  2026 The author retains copyright  and grants the journal the right of first publication.  
This work is licensed under a Creative Commons Attribution 4.0 International License.

1

---

<!-- PAGE 2 -->

Journal  of Economic  Theory and Business  Management 
Journal  Home: https://www.suaspress.org/ojs/index.php/JETBM  | CODEN: JETBAU 
Vol. 3, No. 1, 2026 | ISSN 3006-4953 (Print) | ISSN 3006-4961 (Online)

adjust  interest  rates  or  credit  limits  to  balance  expected 
default losses  and profitability (Phillips  et al.,  2015; Ban & 
Keskin, 2021). These approaches provide a useful foundation 
but differ fundamentally from transaction-level authorization, 
which  opera tes at millisecond  latency and emphasizes real-
time fraud control rather than long-term pricing  optimization 
[6].

Recent  work  has  extended  these  pricing  models  to 
sequential frameworks, such as Markov Decision  Processes 
(MDPs)  (So  &  Thomas,  2011)  and  offline  reinforcement 
learning (RL) (Khraishi & Okhrati, 2022), demonstrating that 
data -driven policies  can outperform static rules  in  dynamic 
environments. Building  on these insights,  the present study 
focuses  on  offline  conservative  RL 
transaction 
authorization, where the objective is to minimize total cost by 
balancing  fraud  losses,  manual-review  operations,  and 
customer friction [7].

for

Despite their  widespread adoption, both risk-based and 
profit-based approaches  exhibit  key  limitations.  First,  they 
are typically myopic: risk-based pricing ensures that coverage 
of expected losses  is  ensured.  Still,  it  overlooks  long-term  
effects,  such  as  adverse  selection,  whereas  profit-based 
pricing  prioritizes  short-term  profit  without  considering 
borrower  retention  or  lifetime  value  [8-9].  Second,  these 
methods assume that pricing decisions are independent across 
applicants,  neglecting  portfolio-level  risk  interactions  and 
competitive dynamics. Finally, their reliance on pre-specified  
functional forms for default risk and demand responses limits 
to  non-stationary  environments.  These 
adaptability 
challenges underscore the need for more flexible, data -driven 
approaches—such  as  reinforcement  learning—that  can 
capture  sequential  decision-making,  learn  from  historical 
data without  restrictive  assumptions, and  optimize  policies 
under uncertainty.

2.2 MARKOV DECISION PROCESS MODELS IN

CREDIT RISK MANAGEMENT

One  significant  stream  of  research  has  modeled 
consumer credit  management problems as Markov decision 
processes  (MDPs).  Early  work  by  Bierman  and  Hausman 
(1970)  and  Frydman  et  al.  (1985)  explored  repayment 
dynamics using  Markov chains,  while  more  recent  studies 
have extended  these  ideas  to  credit  card  profitability  and 
dynamic  limit  assignment.  For  example,  So  and  Thomas 
(2011)  proposed  an  MDP  framework  in  which  states  are 
defined by borrowers’ behavioral score bands, and actions are 
the  credit  limits  assigned  each  period.  By  leveraging 
historical  scoring  data routinely collected  by lenders  under 
Basel  II/III regulations,  they  demonstrated that MDPs  can 
produce optimal dynamic credit limit  policies  that maximize 
expected profitability [10-13]. This  approach highlights how 
credit card operations—traditionally managed through static 
sequential 
risk-return  matrices—can 
optimization  methods  that  explicitly  account  for  state 
transitions in borrower behavior.

benefit

from

Compared  with  earlier  static  models,  MDP-based 
approaches emphasize the evolution of borrower  states over 
time,  including  changes  in  delinquency  risk,  spending 
behavior,  and  profitability.  Trench  et  al.  (2003)  already 
demonstrated that  interest  rate  and  credit  limit  decisions 
could be embedded in an MDP  to capture consumer lifetime 
value, though  their  model  required  coarse discretization  of 
state variables  to  remain  tractable. Later,  So  and Thomas 
(2011)  refined this  idea by  focusing  directly  on  behavioral 
scores,  which  serve  as  sufficient  statistics  for  default risk, 
thereby  reducing  the  dimensionality  of  the  problem  [14]. 
These studies  collectively  show that dynamic programming 
frameworks can more accurately capture sequential trade-offs 
in  credit  policy  decisions  than  one-shot  regression-based  
profit  models,  while  also  reflecting  long-term  portfolio 
profitability rather than short-term outcomes [15-16].

and

learning

function

reinforcement

to  adopt  offline

Despite  these  advantages,  MDP-based  models  face 
significant  challenges,  such  as  the curse  of  dimensionality 
and difficulties  in  estimating  transition  probabilities  when 
defaults are rare.  To  address such  issues,  researchers  have 
(RL) 
begun 
techniques  that extend  MDP  formulations  by  using  data-
driven 
conservative 
approximation 
regularization  to mitigate distributional  shifts.  For  instance, 
Khraishi  and  Okhrati  (2022)  employed  conservative  Q-
learning  (CQL)  to optimize consumer credit pricing  policies 
using  static  datasets  of  loan  applications  [17,18].  Their 
approach demonstrated that offline RL could learn effective 
personalized strategies without live  experimentation, thereby 
avoiding  reputational and financial  risks  for  lenders.  This 
shift  from classical  MDPs  to  offline RL  reflects  a broader 
methodological  evolution:  from  rule-based  and  tabular 
models  toward  flexible,  data -driven  algorithms  that  can 
leverage  large-scale  consumer  data,  incorporate  multiple 
objectives, and adapt to non-stationary environments.

2.3 MARKOV DECISION PROCESS (MDP)

as

a  5-tuple ⟨S,  A,

A  Markov Decision  Process  (MDP)  provides a formal 
mathematical framework for  modeling  sequential  decision -
making problems  under uncertainty, in  which  outcomes are 
partly  random and  partly  under  the  control  of  a  decision 
maker (agent)  [19].  In reinforcement  learning,  an  MDP  is 
typically  defined 
P,  R,γ⟩, 
where S represents  the  set  of  possible  states, A the  set  of 
available  actions, P(s′∣s,  a) the  transition  probability  from 
state ss to s′s′ after  taking  action aa, R(s,  a) the  expected 
immediate 
factor 
and γ∈[0,1) 
determining  the  relative  importance of future rewards.  The 
defining  feature of an MDP  is  the Markov property,  which 
assumes that the future state depends only on the current state 
and action, not on the full history of previous states. Formally, 
this property can be expressed as:

the  discount

reward,

P(st+1∣st, at,st−1,at−1,…,s0,a0) =P(st+1∣st, at).

This assumption enables compact modeling of complex 
recursive

dynamic  systems  and  allows

for  efficient

Published By SOU THERN UNITED ACADEMY OF SCIENCES LIMITED  
Copyright ©  2026 The author retains copyright  and grants the journal the right of first publication.  
This work is licensed under a Creative Commons Attribution 4.0 International License.

2

---

<!-- PAGE 3 -->

Journal  of Economic  Theory and Business  Management 
Journal  Home: https://www.suaspress.org/ojs/index.php/JETBM  | CODEN: JETBAU 
Vol. 3, No. 1, 2026 | ISSN 3006-4953 (Print) | ISSN 3006-4961 (Online)

computation of optimal decisions.

indicators.  The actions correspond

In  the  context  of  credit  risk  management, the  MDP 
framework provides a natural way to represent the dynamics 
of  borrower  behavior  over  time.  Each state may  encode 
features  such  as  the  borrower’s  current  credit  score, 
outstanding  balance,  repayment  history,  and  external 
macroeconomic 
to 
lending decisions—such as whether to approve a loan, adjust 
a  credit  limit,  or  modify  interest  rates[20].  The reward 
function quantifies the  short-term  profit  or  loss  associated 
with  a decision,  for instance, positive  interest revenue from 
timely 
to  defaults. 
The discount factor γ reflects the time value of money and the 
uncertainty  of  future  cash  flows,  aligning 
the  MDP 
formulation with financial valuation principles.

repayments  versus  penalties  due

The  long-term  objective  of  the  agent  is

to  find 
a policy π(a∣s)—a  mapping  from  states  to  actions—that 
maximizes the expected cumulative discounted return:

Gt=E[k=0∑∞γkRt+k+1].

Solving  these equations yields the policy that optimally 
balances immediate  and  future  returns.  However,  in  real-
world  credit  scenarios,  transition  probabilities  and reward 
functions are rarely known in closed form. This motivates the 
use  of reinforcement 
learning  algorithms—such  as  Q-
learning, SARSA,  or value iteration—to directly approximate 
optimal  value  functions  from  historical  data. These  data-
driven  methods enable adaptive, sequential optimization of 
credit  decisions without requiring  explicit  knowledge of the 
underlying transition dynamics.

3 METHODOLOGY

3.1 PROBLEM FORMULATION

incorporated as  exogenous  variables  influencing  transition 
probabilities P  (s′∣s,  a,  ξt),  where ξt  denotes  the  economic 
environment at  time t.  This  coupling  enables the  model  to 
capture  cyclical  variations  in  credit  behavior  driven  by 
external conditions.

Beyond single-account MDPs,  coupled Markov chains 
(Wozabal &  Hochreiter, 2009) model correlated credit-state 
migrations  across  obligors  by  coupling  individual  Markov 
processes  through  shared  latent  factors,  thereby  capturing 
systemic  risk  and  contagion  at  the  portfolio  level.  This 
perspective  can  complement  account-level 
transaction 
authorization  by  incorporating 
latent  factors  such  as 
exogenous state variables or constraints, while  an offline RL 
agent (e.g.,  CQL)  learns cost-sensitive  policies  directly from 
logged  authorization data, eliminating  the  need  for  online 
experimentation. The resulting  formulation preserves micro -
level  behavioral signals  while  accounting for cross-sectional 
dependencies,  enabling  policies  that balance fraud  losses, 
review  costs, and customer friction under dynamic economic 
conditions.

3.2 COST-SENSITIVE REWARD DESIGN

In

learning

traditional

supervised

a  borrower  who

and  many 
reinforcement  learning  frameworks,  all  misclassification 
errors  are treated as equally costly.  However,  in  credit  risk  
management,  this  assumption  does  not  hold.  A  false 
negative—approving 
subsequently 
defaults—can lead  to  substantial  financial  losses,  while  a 
false  positive—rejecting  a  creditworthy  borrower—mainly 
affects  customer  experience  and  potential  revenue.  This 
asymmetry  in  error  costs  motivates  incorporating  cost-
sensitive 
the 
reinforcement  learning  reward  function.  Instead of merely 
maximizing accuracy or expected reward, the agent explicitly 
learns to minimize total expected cost, defined as

learning  principles

the  design  of

into

We cast transaction authorization as a Markov Decision 
Process with action set A = {Approve, Review, Reject}. The 
environment state s concatenates (i) customer and transaction 
features, (ii)  macro factors ξt, and (iii)  cohort features from 
optional clusterings.  A supervised score  model (LR/LGBM) 
produces a probability of fraud PD(s),  which becomes part of 
the state but does not define the policy by itself. The policy is 
learned offline via a conservative algorithm (e.g., CQL) using 
logged  data. Reward  and  constraints. We  optimize  a  cost-
sensitive objective:

r(s,a,y) =−(cfp 1[a=Approve∧y=Fraud] 
+cfn 1[a∈{Reject, Review}  ∧
y=Legit]+crev 1[a=Review])

∁= 𝒄𝒇𝒑 × 𝑭𝑷 × 𝒄𝒇𝒏 × 𝑭𝑵

where 𝒄𝒇𝒑 and 𝒄𝒇𝒏 denote the monetary or utility cost of 
false positive  and false  negative  decisions,  respectively.  In 
practice,  these  parameters can be  calibrated from portfolio 
loss  statistics,  default  recovery  rates,  or  business  impact 
analysis.  Consequently,  the  learning  objective  shifts  from 
maximizing accuracy to minimizing cost, enabling the model 
to  prioritize  high-risk  scenarios  with  greater  economic 
consequences.

Building  on this framework, the reward function in the 
proposed reinforcement learning environment is redefined as 
the negative of the total cost, i.e.,

𝑹𝒕 = −(𝒄𝒇𝒑 × 𝑭𝑷𝒕 × 𝒄𝒇𝒏 × 𝑭𝑷𝒕)

subject to business  rules  and capital limits.  Here, CFP 
penalizes approving a fraudulent transaction (chargeback, ops 
legitimate 
cost), CFPN penalizes  declining/reviewing 
transaction  (customer  friction),  and Crev captures  manual 
queue and latency costs. Moreover,  macroeconomic factors 
such as GDP  growth,  unemployment, and interest rates were

a

which  aligns  the  agent’s  optimization  behavior  with  
business  objectives.  This  design  effectively  integrates  the 
principles  of cost-sensitive learning into sequential decision-
making: each policy update reflects the trade-off between risk 
control and customer friction. Such a formulation also allows 
multi-objective  extensions,  for  instance  by  incorporating

Published By SOU THERN UNITED ACADEMY OF SCIENCES LIMITED  
Copyright ©  2026 The author retains copyright  and grants the journal the right of first publication.  
This work is licensed under a Creative Commons Attribution 4.0 International License.

3

---

<!-- PAGE 4 -->

Journal  of Economic  Theory and Business  Management 
Journal  Home: https://www.suaspress.org/ojs/index.php/JETBM  | CODEN: JETBAU 
Vol. 3, No. 1, 2026 | ISSN 3006-4953 (Print) | ISSN 3006-4961 (Online)

customer friction  or  portfolio  utilization  efficiency into  the 
reward structure.

FIGURE 1. CLOSED-LOOP OFFLINE RL FOR TRANSACTION 
AUTHORIZATION.

Historical

batches t1…tnt1…tn are  processed

to 
construct state features and labels  (default vs.  non-default). 
Optional customer clustering stabilizes policy generalization. 
A  cost  matrix  encodes  asymmetric  penalties  𝒄𝒇𝒑 and 
operational  constraints.  An  offline  RL  agent  (e.g.,  CQL) 
learns a policy π(a∣s) to minimize  expected total cost while 
preserving  customer friction  (authorization rate/utilization). 
Ultimately,  the  policy  outputs actions —approve or  reject. 
Outcomes  are  logged  to  compute  economic  rewards  and 
periodically retrain the policy, forming a closed-loop system. 
The resulting RL agent can thus learn policies that adaptively 
balance  profitability  and  prudence  under  varying  market 
conditions,  outperforming  traditional  fixed-threshold  or 
accuracy-driven  models.  As  shown  in  Figure  1,  for  the 
monthly/rolling  refresh,  state construction, cost matrix, and 
the offline-to-online loop.

CQL  penalizes  overestimation  of  unseen  actions  by 
adding a regularization term that explicitly  lowers  Q-values 
for actions not well  supported by the data. This ensures that 
the  learned policy  remains within  the  support of historical 
behavior while  remaining  optimal in  well-sampled  regions. 
BCQ,  by  contrast,  constrains  policy  learning  through  a 
generative  behavior  model  that  samples  candidate actions 
from the empirical  data distribution. It then evaluates them 
via a Q-network to select those expected to yield  the highest  
reward,  effectively  balancing  exploitation  of  known  good 
actions with  conservatism toward  novel  or  uncertain ones. 
Both  methods  enable  stable  policy  improvement  from 
active 
data  without 
historical 
experimentation.

requiring

credit

The  process  begins  with  preprocessed  customer–
transaction  data  and  risk  labels  derived  from  historical 
repayments. These  inputs  are  used  to  construct  an  offline 
environment E (S,  A, R) and a cost-sensitive reward function 
defined as R−(cfp⋅FP+cfn⋅FN).  A  deep  Q-network  (DQN)-
based or actor–critic architecture is trained to approximate the 
state–action value  function Q  (s,  a).  The  resulting  policy 
outputs adaptive thresholds  or  action probabilities  for  loan 
authorization, adjustment,  or  rejection.  After  training,  the 
model  undergoes  offline  evaluation using  metrics  such  as 
expected cost reduction, precision–recall trade-offs, and risk-
adjusted return. The learned policy  is  then validated against 
baseline  supervised  classifiers  (e.g.,  LightGBM  or  Logistic 
Regression)  to  demonstrate  its  advantage  in  optimizing 
business-aligned objectives beyond accuracy.

3.3 OFFLINE REINFORCEMENT LEARNING

4 EXPERIMENTS AND RESULTS

FRAMEWORK

In  real-world  credit  risk  management, direct  online 
exploration—such as approving high-risk borrowers to gather 
additional feedback—is impractical and ethically constrained. 
To  address  this,  the  proposed  framework adopts an  offline 
reinforcement  learning (offline  RL)  paradigm,  enabling 
learning  of  an  optimal  policy  from  logged  historical  data 
without  interacting  with  the  live  environment.  Offline  RL 
extends the standard Markov Decision  Process  formulation 
introduced in Section 3.1, using fixed transition tuples (s, a,r, 
s′)  drawn  from  historical  loan  data.  The  agent  aims  to 
optimize  a  policy π(a∣s) that  minimizes  the  total  expected 
cost E[C] under the empirical distribution of past interactions, 
while  ensuring  robustness to unseen state–action pairs. This 
enables the model to extract optimal decision strategies from 
static datasets, making  it  well  suited  to regulated  financial 
environments where exploration is infeasible.

A  key  challenge  in  offline  RL  lies  in distributional 
shift—the mismatch between the state–action pairs present in 
the dataset and those that the learned policy may generate. To 
mitigate  this,  conservative algorithms  such as Conservative 
Q-Learning 
(CQL)  and Batch-Constrained  Q-Learning 
(BCQ)  are employed.

4.1 DATASET DESCRIPTION

We  use  the publicly  available anonymized credit card 
transaction dataset (often  referred  to  as  the  ULB/Kaggle 
dataset),  which  contains  284,807  records  from  European 
cardholders  as  of  September  2013.  The  target  Variable  is 
binary (1 = fraud, 0 = legitimate),  with 492 frauds (0.172%), 
resulting  in  an  extreme  imbalance  that  motivates  cost-
sensitive evaluation.

Each transaction has 30 numeric features. V1–V28 are 
PCA-transformed  components  of  anonymized  variables. 
Time denotes seconds since the first transaction in the dataset, 
and  Amount  is  the  transaction  value.  Following  standard 
practice, we  apply log  (1 +  Am ount) and standardize Time 
and Amount using statistics fitted only to the training split  to 
avoid leakage.

We  split  the data chronologically  into 70%/15%/15% 
for  training/validation/testing  (no  shuffling),  preserving 
temporal order to emulate sequential deployment. The dataset 
does  not contain action labels  (e.g.,  “review”);  actions are 
policy decisions modeled in our cost function and used during 
offline policy evaluation. Figure 2 shows the class imbalance, 
Figures  3–5  depict  temporal  patterns,  and  Figures  6–7 
summarize the distribution of Amount.

Published By SOU THERN UNITED ACADEMY OF SCIENCES LIMITED  
Copyright ©  2026 The author retains copyright  and grants the journal the right of first publication.  
This work is licensed under a Creative Commons Attribution 4.0 International License.

4

---

<!-- PAGE 5 -->

Journal  of Economic  Theory and Business  Management 
Journal  Home: https://www.suaspress.org/ojs/index.php/JETBM  | CODEN: JETBAU 
Vol. 3, No. 1, 2026 | ISSN 3006-4953 (Print) | ISSN 3006-4961 (Online)

TABLE 1. DATASET OVERVIEW AND CLASS IMBALANCE 
(KAGGLE CREDIT CARD FRAUD, SEPTEMBER 2013).

4.2 EXPLORATORY DATA ANALYSIS

Attribute  Description

Records  Total  number 
of transactions

Range 
Type 
284,807

Features  V1–V28

Continuous

/

Notes

492 are fraud 
(0.172%) 
Scaled 
and 
anonymized

Time

(PCA-
transformed) 
Seconds 
elapsed  since 
first 
transaction 
Amount  Transaction

amount

Class

Target label

Continuous

Temporal 
ordering

Continuous  Highly 
skewed 
distribution 
Strong 
imbalance

Binary 
Legitimate, 
1: Fraud)

(0:

to

due

its realistic

The dataset is widely used in financial machine learning 
benchmarks 
transaction 
behavior and severe  class  imbalance,  making  it  an  ideal 
testing  ground 
reinforcement 
for cost-sensitive  offline 
this  study,  the  dataset  is  split  
learning  models.  In 
chronologically 
(15%), 
(70%), validation 
and testing  (15%) sets  to  simulate  a  temporal  deployment 
scenario where new transactions arrive sequentially.

into training

To  better understand the statistical  characteristics and 
behavioral  differences  between  legitimate  and  fraudulent 
transactions,  an  exploratory  data  analysis  (EDA)  was 
conducted prior  to model training.  This  analysis focuses on 
class  imbalance,  temporal  patterns,  transaction  amount 
distributions,  and  inter-feature  relationships,  which  jointly 
inform the construction of the state space and cost-sensitive 
reward  functions in  the reinforcement learning  framework. 
As  shown  in  Figure  2,  the  dataset exhibits  a  severe  class 
imbalance,  with  fraudulent  transactions representing  only 
0.17% of all cases.

FIGURE 3. DENSITY OF TRANSACTIONS OVER TIME (S) BY 
CLASS

Such  an  imbalance  can  lead  to  biased  decision 
boundaries  if  standard  classifiers  are  used  without  cost 
adjustment  or 
subsequent 
experiments  employ  cost-sensitive  weighting  and  offline 
reinforcement learning to mitigate this bias.

resampling.

Therefore,

FIGURE 2. CLASS DISTRIBUTION (EXTREME IMBALANCE).

As  summarized  in  Table  1, the  dataset  contains 
284,807 transactions with 492 frauds (0.172%),  confirming 
an  extreme  class  imbalance.  Features  V1–V28  are  PCA 
first 
seconds 
components; Time is 
transaction; Amount is  highly 
and  modeled 
with log⁡(1+Amount)  log(1+Amount).

since 
skewed

the

Figure 2 illustrates the  imbalance visually: the fraud 
bar  is  nearly  invisible  at  the  original  scale. This  skew 
motivates 
and  off-policy 
evaluation,  rather  than  accuracy  alone;  throughout,  we 
therefore report cost metrics under (cfp, cfn, crev) and avoid 
random shuffling by using chronological splits.

cost-sensitive  objectives

FIGURE 4. TOTAL AMOUNT AGGREGATED BY HOUR.

As  shown  in  Figure  3  (all  transactions) and Figure  4 
(fraud-only), hourly aggregates display clear diurnal cycles, 
while  fraud  exhibits  narrower  and  more  irregular  peaks, 
consistent  with  time-based  behavioral  clustering.  These 
temporal dynamics justify including time-of-day (and related 
calendar features) in the RL state, allowing the policy to adapt 
decisions based on transaction timing.

Published By SOU THERN UNITED ACADEMY OF SCIENCES LIMITED  
Copyright ©  2026 The author retains copyright  and grants the journal the right of first publication.  
This work is licensed under a Creative Commons Attribution 4.0 International License.

5

---

<!-- PAGE 6 -->

Journal  of Economic  Theory and Business  Management 
Journal  Home: https://www.suaspress.org/ojs/index.php/JETBM  | CODEN: JETBAU 
Vol. 3, No. 1, 2026 | ISSN 3006-4953 (Print) | ISSN 3006-4961 (Online)

FIGURE 6. AMOUNT BY CLASS: RAW VS. LOG-SCALED 
BOXPLOTS

The  left  plot  displays  the  complete  amount  range, 
including  extreme outliers,  while  the right  plot zooms in  on 
the  0–250  range  to  highlight  median  differences  and 
variability.

FIGURE 5. TOTAL AMOUNT OF FRAUD TRANSACTIONS BY 
HOUR

4.4 FEATURE CORRELATION AND PCA

BEHAVIOR

Further  analysis of the transaction amount reveals that 
fraudulent transactions tend to  occur  at both very  low  and 
very high  transaction values, as illustrated  in  Figure  5. The 
bimodal  nature of  fraud amount  distributions  suggests  the 
coexistence  of  two  behavioral  archetypes:  “ micro-fraud,” 
aimed  at  evading  detection  thresholds,  and  “ high-stakes 
fraud,” targeting large-value transactions. This heterogeneity 
motivates the use of adaptive reward scaling in the design of 
RL.

4.3 TRANSACTION AMOUNT DISTRIBUTION

The transaction amount is one of the most informative 
variables in  credit  card fraud detection. To understand how 
transaction value relates to fraudulent behavior, we examined 
the statistical distribution  of the Amount feature across the 
two  classes.  As  shown  in  Figure  6,  legitimate  transactions 
(Class  =  0)  exhibit a highly  skewed distribution,  with  most 
fraudulent 
values  concentrated  below  $100,  while 
transactions (Class = 1) display a wider variance and a greater 
number of extreme values.

This  discrepancy suggests  that fraudulent activities are 
often  associated with  atypical purchase  patterns  —  either 
small  micro-transactions  designed 
to  evade  detection 
thresholds  or  sporadic  high-value  purchases  aimed  at 
maximizing  illicit  gains.  The  right-hand  panel of  Figure  6 
presents  a  zoomed-in  view,  confirming  that  the  median 
transaction amount for  fraud cases  is  higher  and  exhibits 
greater dispersion.

Such  heterogeneity  in  transaction magnitude  implies 
that static threshold-based systems may perform poorly,  as 
they  fail  to  adapt to  dynamic  risk  levels.  Therefore,  the 
reinforcement learning framework later introduced in Section 
5 leverages transaction amount as a continuous state variable, 
enabling  dynamic  adjustment of  authorization  thresholds 
based on contextual risk signals.

To better understand the structural relationships among 
the  features,  a  correlation  analysis  was  conducted  on  all 
numerical variables in the dataset. Since the features V1–V28 
were obtained through Principal Component Analysis (PCA), 
they are expected to be approximately orthogonal. However, 
several  components exhibit moderate correlations  with  key 
behavioral indicators such as Amount, Time,  and the target 
variable Class.

components

Most  PCA-derived

remain  weakly 
correlated (|r|  <  0.3),  indicating  limited  redundancy among 
latent dimensions. Notably, V14, V17, and V21 show slightly  
higher  negative correlations with  the fraud label (Class =  1), 
consistent  with  prior  studies  suggesting  these  components 
encode  transaction  irregularities  and  spending  pattern 
anomalies. Meanwhile,  the  Amount feature demonstrates a 
mild  positive  correlation  with  Class, 
its 
importance in fraud detection models.

reaffirming

PCA

(V1–V28)

components

exhibit  weak 
intercorrelations, while  the amount and selected components, 
such  as V14 and V17,  Display  moderate relationships  with  
the  fraud label.  To  further analyze temporal dependencies, 
Figure  7 plots transaction amounts against time. The results 
reveal sporadic high-value spikes  distributed throughout the 
observation period, many of which correspond to fraudulent 
transactions.  This  pattern  supports  the  hypothesis  that 
fraudulent behavior does not follow regular time cycles  but 
rather opportunistic bursts—an important consideration when 
defining temporal states for the reinforcement learning agent.

By  combining  insights  from both  the  correlation  and 
temporal amount analyses, this study identifies a compact yet 
expressive feature subset for model input, comprising:

𝑺 = [𝑽𝟏𝟒 , 𝑽𝟏𝟕 , 𝑽𝟐𝟏 , 𝐀𝐦𝐨𝐮𝐧𝐭,𝐓𝐢𝐦𝐞,𝐇𝐨𝐮𝒓]

This  representation balances dimensionality  reduction 
from PCA with interpretability for downstream cost-sensitive 
reinforcement learning.

Published By SOU THERN UNITED ACADEMY OF SCIENCES LIMITED  
Copyright ©  2026 The author retains copyright  and grants the journal the right of first publication.  
This work is licensed under a Creative Commons Attribution 4.0 International License.

6

---

<!-- PAGE 7 -->

Journal  of Economic  Theory and Business  Management 
Journal  Home: https://www.suaspress.org/ojs/index.php/JETBM  | CODEN: JETBAU 
Vol. 3, No. 1, 2026 | ISSN 3006-4953 (Print) | ISSN 3006-4961 (Online)

interpretability  of the offline RL  state representation, where 
V14–V21,  Amount,  and  Time  variables  encapsulate both 
behavioral  and  financial  risk  signals.  The  reinforcement 
learning  model leverages  these embeddings  to dynamically 
improving 
adjust  the  authorization  threshold, 
sensitivity to rare but high-cost events.

thereby

5.2 COST-SENSITIVE REINFORCEMENT

LEARNING EVALUATION

To  evaluate the effectiveness of the  proposed Offline 
Conservative Reinforcement Learning (CQL) framework, we 
benchmarked  its  performance  against  baseline  classifiers 
under  asymmetric  cost  conditions.  As  shown  in  Figure  9, 
feature  importance  analysis  confirms  that  several  latent 
components (V17, V14, V4) and the transaction Amount play 
a decisive role  in identifying risky  behaviors. The confusion 
matrix shows  a significant  improvement in  recall  for  fraud 
detection,  while  maintaining  a  controlled  false-positive 
rate—a critical trade-off for user-centric financial systems.

FIGURE 9. MODEL INTERPRETABILITY AND EVALUATION.

(Top)  Feature  importance  ranking  highlighting  key 
behavioral  and  financial  components;(Bottom)  Confusion 
matrix showing improved fraud recall and balanced accuracy 
achieved  by  the  cost-sensitive  RL  policy.  Compared  to 
traditional 
profit-maximization 
approaches, the CQL framework achieves co-optimization of 
credit  risk  and customer friction  by directly  minimizing  the 
expected misclassification cost:

threshold-based

or

FIGURE 7. SCATTER PLOT OF TRANSACTION AMOUNT 
VERSUS TIME.

Fraudulent transactions tend to appear as isolated spikes, 
indicating non-stationary and opportunistic behavior patterns.

5 CONCLUSION AND DISCUSSION

5.1 MODEL PERFORMANCE AND FEATURE

INTERPRETABILITY

The  proposed  framework

integrates  conventional 
supervised  models  (e.g.,  LightGBM,  Logistic  Regression ) 
with  an offline  reinforcement learning  (RL)  component to 
jointly  optimize  credit  risk  control  and  customer  friction. 
Figure  8  illustrates  the  regression  relationships  between 
transaction amount and key PCA-derived  components (V2, 
V5,  V7,  V20),  revealing  distinct  behavioral signatures  for 
fraudulent and legitimate users. Legitimate transactions form 
dense low-variance clusters, while  fraudulent cases appear as 
sparse,  high-deviation  outliers  along  specific  principal 
components.

FIGURE 8. RELATIONSHIP BETWEEN TRANSACTION 
AMOUNT AND KEY PCA FEATURES (V2, V5, V7, V20) 
ACROSS FRAUD AND NON-FRAUD CLASSES.

Fraudulent transactions appear as sparse, high-deviation 
points,  reflecting  nonlinear  behavioral separability  that the 
RL  agent  can  exploit.  This  differentiation  supports  the

Published By SOU THERN UNITED ACADEMY OF SCIENCES LIMITED  
Copyright ©  2026 The author retains copyright  and grants the journal the right of first publication.  
This work is licensed under a Creative Commons Attribution 4.0 International License.

7

---

<!-- PAGE 8 -->

Journal  of Economic  Theory and Business  Management 
Journal  Home: https://www.suaspress.org/ojs/index.php/JETBM  | CODEN: JETBAU 
Vol. 3, No. 1, 2026 | ISSN 3006-4953 (Print) | ISSN 3006-4961 (Online)

𝑳 = 𝒄𝒇𝒑 × 𝑭𝑷 × 𝒄𝒇𝒏 × 𝑭𝑵

Not Applicable.

Through  cost-aware  policy

the  model 
effectively  captures  contextual  patterns 
in  historical 
transaction  logs,  thereby  eliminating  the  need  for  online 
exploration 
both operational 
safety and regulatory compliance.

learning,

ensuring

and

5.3 CONCLUSION

thresholds

This  research provides empirical  evidence that offline 
conservative reinforcement learning  can serve as a practical 
and  ethically  sound  framework  for  optimizing  credit 
decision-making  under  asymmetric  risk  conditions.  By 
combining cost-sensitive  reward  modeling with  deep policy 
approximation,  the  model  successfully 
learns  adaptive 
lending 
that  minimize  financial  loss  while 
reducing  customer friction.  The  interpretability  analysis  of 
PCA  components and feature-importance rankings confirms 
that latent behavioral  signals—particularly  V14,  V17,  and 
transaction Amount—exhibit  significant  predictive  power, 
enabling  the  RL  agent  to  detect  high-risk  patterns  that 
conventional classifiers overlook. Compared with supervised 
baselines, 
the  CQL-based  model  consistently  achieves 
superior  recall  and cost efficiency,  validating  its  suitability 
for  deployment in  real-world  financial systems  constrained 
by regulatory and operational limits.

guided

Beyond its technical contributions, this  study advances 
the  conceptual  understanding  of  user-centric  credit 
management by framing risk control and incentive design as 
a joint optimization problem  rather than a binary trade-off. 
The findings underscore that personalized credit strategies—
when 
policies—can 
simultaneously  promote  consumer  welfare,  institutional 
stability, and macroeconomic growth. Future extensions may 
explore multi-objective reinforcement learning  architectures 
that explicitly incorporate fairness, interpretability, and long-
term  user  engagement  metrics,  further  strengthening  the 
alignment  between  financial  innovation  and  sustainable 
economic development.

conservative  RL

by

ACKNOWLEDGMENTS

Not Applicable.

FUNDING

Not Applicable.

INSTITUTIONAL REVIEW BOARD 
STATEMENT

Not Applicable.

INFORMED CONSENT STATEMENT

DATA AVAILABILITY STATEMENT

Not Applicable.

CONFLICT OF INTEREST

Not Applicable.

PUBLISHER'S NOTE

All   claims  expressed  in  this  article  are  solely  those  
of the  authors  and  do  not  necessarily  represent  those  of  
their  affiliated organizations, or  those of the  publisher,  the 
editors and the reviewers.  Any product that may be evaluated 
in this article, or claim that may be made by its manufacturer, 
is not guaranteed or endorsed by the publisher.

AUTHOR CONTRIBUTIONS

Not application.

ABOUT THE AUTHORS

XIMENG,  Yang

Board of Directors, Excellent Era Lending Service

Corp., Makati, Philippines , PH, Cocoliu898@gmail.com.

YIMING,  Zhang

Department of Financial Technology, Peking

University,  Peking,  China , CN, 
zhang1ming137@outlook.com.

REFERENCES

[1]  Khraishi,  R.,  &  Okhrati,  R.  (2022, November).  Offline 
deep  reinforcement  learning  for  dynamic  pricing  of 
consumer  credit.  In  Proceedings  of  the  Third  ACM  
International Conference on AI in Finance (pp. 325–333).

[2]  So,  M.  M.,  &  Thomas,  L.  C.  (2011).  Modelling  the 
profitability of credit cards by Markov decision processes. 
European Journal of Operational Research, 212(1), 123 –
130.

[3] Sewak, M. (2019). Temporal difference learning, SARSA, 
and  Q-learning:  Some  popular  value  approximation-
based  reinforcement  learning  approaches.  In  Deep 
reinforcement learning: Frontiers  of artificial intelligence 
(pp. 51–63). Springer.

[4] Sha, F., Ding,  C., Zheng, X., et al. (2025). Weathering the 
policy storm: How trade uncertainty shapes firm financial 
performance 
innovation  and  operations. 
International Review of Economics & Finance, 104274.

through

Published By SOU THERN UNITED ACADEMY OF SCIENCES LIMITED  
Copyright ©  2026 The author retains copyright  and grants the journal the right of first publication.  
This work is licensed under a Creative Commons Attribution 4.0 International License.

8

---

<!-- PAGE 9 -->

Journal  of Economic  Theory and Business  Management 
Journal  Home: https://www.suaspress.org/ojs/index.php/JETBM  | CODEN: JETBAU 
Vol. 3, No. 1, 2026 | ISSN 3006-4953 (Print) | ISSN 3006-4961 (Online)

parallelism  optimization  methods  in  large 
model-based 
systems. 
recommendation 
https://arxiv.org/abs/2506.17551

language 
arXiv.

[17] Gonzalez, J., Tran, V., Meredith, J., Xu, I., Penchala, R., 
Vilar-Ribó,  L.,  et  al.  (2025).  How  it  begins:  Initial 
response to opioids strongly predicts self-reported opioid 
use disorder. medRxiv.

[18]  Wozabal,  D.,  &  Hochreiter,  R.  (2012).  A  coupled 
Markov chain approach to credit risk modeling.  Journal 
of Economic Dynamics and Control, 36(3), 403–415.

[19] Kumar, A.,  Zhou, A.,  Tucker, G.,  &  Levine, S.  (2020). 
reinforcement 
Conservative  Q-learning 
learning.  Advances  in  Neural  Information  Processin g 
Systems, 33, 1179–1191.

for  offline

[20] Mendonca, R., Geng,  X.,  Finn, C., & Levine, S. (2020). 
to 
learning 
identification  and 
arXiv.

Meta -reinforcement 
distributional  shifts  via  model 
experience 
relabeling. 
https://arxiv.org/abs/2006.07178

robust

that

is

[5] Deng,  X.  (2025). Cooperative optimization strategies for 
data  collection  and  machine  learning  in  large-scale 
distributed systems. In 2025 4th International Symposium 
on Computer Applications  and Information Technology 
(ISCAIT) (pp. 2151–2154). IEEE.

[6] Trench, M. S., Pederson, S. P.,  Lau, E. T., Ma, L., Wang, 
H., & Nair, S. K. (2003). Managing credit lines and prices 
for Bank One credit cards. Interfaces, 33(5), 4–21.

[7] Wiesemann, W.,  Kuhn, D.,  & Rustem, B. (2013). Robust 
Markov decision  processes.  Mathematics of Operations 
Research, 38(1), 153–183.

[8]  Tan, C.,  Gao,  F.,  Song,  C.,  Xu,  M.,  Li,  Y.,  &  Ma, H. 
(2024). Highly  reliable  CI-JSO  based densely connected 
convolutional networks  using  transfer learning  for fault 
diagnosis.  Journal  of  Information Systems  Engineerin g 
Management. 
and 
https://doi.org/10.52783/jisem.v10i4.12207

[9]  Tan, C.,  Gao,  F.,  Song,  C.,  Xu,  M.,  Li,  Y.,  &  Ma, H. 
(2024).  Proposed  damage detection  and isolation  from 
limited  experimental  data  based  on  a  deep  transfer 
learning  and an ensemble  learning  classifier.  Journal of 
Information  Systems  Engineering  and  Ma nagement. 
https://doi.org/10.52783/jisem.v10i4.12206

[10]  Han,  X.,  &  Dou,  X.  (2025).  User  recommendation 
method integrating  hierarchical graph  attention network 
with  multimodal  knowledge  graph.  Frontiers 
in  
Neurorobotics, 19, 1587973.

[11]  Zhuang,  R.  (2025).  Evolutionary logic  and theoretical 
construction  of  real  estate  marketing  strategies  under 
digital 
transformation.  Economics  and  Management 
Innovation, 2(2), 117–124.

[12] Yang,  Z.,  et al. (2025). RLHF fine-tuning  of LLMs for 
alignment with  implicit  user  feedback in conversational 
recommenders. arXiv. https://arxiv.org/abs/2508.05289

[13]  Deng,  X.,  &  Yang,  J.  (2025).  Multi-layer  defense 
strategies  and  privacy-preserving  enhancements  for 
membership  reasoning  attacks  in  a  federated learning 
framework.  In  2025  5th  International  Conference  on 
Computer Science and Blockchain (CCSB) (pp. 278–282). 
IEEE.

[14] Tan, C. (2024). The application and development trends 
in  automotive 
of  artificial 
production. Artificial  Intelligence  Technology Research, 
2(5).

intelligence

technology

[15] Zhang, L., & Meng, Q. (2025, September). User portrait-
driven  smart home device  deployment optimization and 
spatial  interaction  design.  In  2025  5th  International 
Conference  on  Artificial  Intelligence,  Automation  and 
High Performance Computing (AIAHPC)  (pp. 724–728). 
IEEE.

[16] Yang, H., Tian, Y.,  Yang, Z.,  Wang, Z., Zhou, C., & Li, 
D.  (2025).  Research  on  model  parallelism  and  data

Published By SOU THERN UNITED ACADEMY OF SCIENCES LIMITED  
Copyright ©  2026 The author retains copyright  and grants the journal the right of first publication.  
This work is licensed under a Creative Commons Attribution 4.0 International License.

9

<!-- MARKITDOWN CONVERSION -->

<!-- Full MarkItDown conversion for formatting fidelity. -->

Journal of Economic Theory and Business Management
Journal Home: https://www.suaspress.org/ojs/index.php/JETBM | CODEN: JETBAU
V ol. 3, No. 1, 2026 | ISSN 3006-4953 (Print) | ISSN 3006-4961 (Online)
Offline Conservative RL for Transaction Authorization:
Smartly Balancing Fraud Risk and Customer Friction
XIMENG, Yang 1* YIMING, Zhang 2
1 Board of Directors, Excellent Era Lending Service Corp., Makati, Philippines, PH
2 Department of Financial Technology, Peking University, Peking, China, CN
* XIMENG, Yang is the corresponding author, E-mail: Cocoliu898@gmail.com
Abstract: This study instantiates credit strategy optimization at the transaction authorization layer, with actions approve,
review, and decline. Within an Offline Conservative RL (CQL) framework, we co-optimize fraud loss, operational burden
from manual reviews, and customer friction from false positives and delays via a unified multi-objective cost function. Using a
public credit-card transaction dataset with severe class imbalance, the learned policy improves total cost relative to cost-
sensitive supervised baselines, while offering favorable trade-offs along a Pareto frontier between risk, operations, and
friction. We detail the MDP design (state featurization, action space, and cost weights) and show that CQL mitigates out-of-
distribution overestimation in offline settings. The results indicate that conservative RL is a practical path for transaction-level
credit decision-making that balances fraud risk with operational efficiency and user impact.
Keywords: Offline Reinforcement Learning, Cost-Sensitive Credit Risk Optimization, User-Centric Financial Decision
Systems, Conservative Q-Learning CQL.
Disciplines: Business Analytics. Subjects: Econometric Modeling.
DOI: https://doi.org/10.70393/6a6574626d.333932 ARK: https://n2t.net/ark:/40704/JETBM.v3n1a01
safety and governance expectations.
1 INTRODUCTION
Taken together, these developments underscore the
In recent years, the global economy has been need for innovative methodologies that balance risk control
undergoing profound structural changes, with intensified and consumer welfare [4]. Reinforcement learning (RL),
trade frictions and heightened geopolitical uncertainty particularly in its offline and conservative variants, offers a
disrupting traditional patterns of growth and consumption. At promising approach for data-driven policy optimization from
the same time, the rapid expansion of digital finance has historical logs, thereby eliminating the need for costly real-
made transaction-level credit card authorization a first line of time experimentation[5]. By leveraging user-centric
defense for consumer credit. The practical challenge is no behavioral data and incorporating multi-objective reward
longer macro demand stimulation per se, but rather functions, such methods can co-optimize credit risk and
controlling fraud losses without creating excessive customer incentive strategies, ensuring that consumer lending not only
friction (unnecessary declines or review delays) in real time. boosts demand but also safeguards financial stability. This
This risk–experience trade-off—rather than aggregate study contributes to this emerging literature by empirically
consumption effects—motivates our study and frames analyzing the co-optimization of credit risk management and
authorization as an operations- and policy-optimization incentive design through offline conservative reinforcement
problem [1-3]. learning, situating consumer credit as both a driver of
domestic demand and a financial asset class with distinct risk
We therefore analyze transaction-level decision
properties.
policies using a public, severely imbalanced credit-card
dataset with PCA-transformed features (V1–V28), Time (in
2 RELATED WORK
seconds since the first transaction), and Amount (a heavy-
tailed distribution). The dataset is used strictly for offline
policy learning and evaluation. To emulate sequential 2.1 CREDIT PRICING AND AUTHORIZATION
deployment, we preserve temporal order through STRATEGIES
chronological splits and adopt conservative offline RL (e.g.,
CQL) to learn policies from logged data, without requiring Traditional studies in consumer credit have primarily
online experimentation, thereby aligning with operational focused on risk-based and profit-based pricing, where lenders
Published By SOUTHERN UNITED ACADEMY OF SCIENCES LIMITED 1
Copyright © 2026 The author retains copyright and grants the journal the right of first publication.
This work is licensed under a Creative Commons Attribution 4.0 International License.

Journal of Economic Theory and Business Management
Journal Home: https://www.suaspress.org/ojs/index.php/JETBM | CODEN: JETBAU
V ol. 3, No. 1, 2026 | ISSN 3006-4953 (Print) | ISSN 3006-4961 (Online)
adjust interest  rates or  credit limits  to balance expected  Compared with  earlier  static  models,  MDP-based
default losses and profitability (Phillips et al., 2015; Ban &  approaches emphasize the evolution of borrower states over
Keskin, 2021). These approaches provide a useful foundation  time,  including  changes  in  delinquency  risk,  spending
but differ fundamentally from transaction-level authorization,  behavior, and profitability. Trench  et al.  (2003) already
which operates at millisecond latency and emphasizes real- demonstrated that interest rate and credit limit decisions
time fraud control rather than long-term pricing optimization  could be embedded in an MDP to capture consumer lifetime
[6].  value, though their model required coarse discretization of
state variables to remain tractable. Later, So and Thomas
| Recent work  |     | has extended these pricing  |     |     |     | models  | to  |     |     |     |     |     |     |     |
| ------------ | --- | --------------------------- | --- | --- | --- | ------- | --- | --- | --- | --- | --- | --- | --- | --- |
(2011) refined this idea by focusing directly on behavioral
sequential frameworks, such as Markov Decision Processes
scores, which serve as sufficient statistics for default risk,
(MDPs)  (So & Thomas, 2011) and offline reinforcement
|     |     |     |     |     |     |     |     | thereby reducing  |     | the dimensionality of the problem [14].  |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------------- | --- | ---------------------------------------- | --- | --- | --- | --- |
learning (RL) (Khraishi & Okhrati, 2022), demonstrating that
These studies collectively show that dynamic programming
data-driven policies can outperform static rules in dynamic
frameworks can more accurately capture sequential trade-offs
environments. Building on these insights, the present study
|          |              |               |     |     |      |              |     | in  credit policy decisions  |     |              | than one-shot regression-based  |            |     |            |
| -------- | ------------ | ------------- | --- | --- | ---- | ------------ | --- | ---------------------------- | --- | ------------ | ------------------------------- | ---------- | --- | ---------- |
| focuses  | on  offline  | conservative  |     | RL  | for  | transaction  |     |                              |     |              |                                 |            |     |            |
|          |              |               |     |     |      |              |     | profit  models,              |     | while  also  | reflecting                      | long-term  |     | portfolio  |
authorization, where the objective is to minimize total cost by
profitability rather than short-term outcomes [15-16].
| balancing  | fraud  | losses,  | manual-review  |     | operations,  |     | and  |     |     |     |     |     |     |     |
| ---------- | ------ | -------- | -------------- | --- | ------------ | --- | ---- | --- | --- | --- | --- | --- | --- | --- |
customer friction [7].  Despite  these  advantages, MDP-based  models  face
significant challenges, such as the curse of dimensionality
Despite their widespread adoption, both risk-based and
and difficulties in estimating transition probabilities when
profit-based approaches exhibit key limitations. First, they
defaults are rare. To address such issues, researchers have
are typically myopic: risk-based pricing ensures that coverage
|                                        |     |     |     |                         |     |     |     | begun  | to  adopt  | offline  | reinforcement  |     | learning  | (RL)  |
| -------------------------------------- | --- | --- | --- | ----------------------- | --- | --- | --- | ------ | ---------- | -------- | -------------- | --- | --------- | ----- |
| of expected losses is ensured. Still,  |     |     |     | it overlooks long-term  |     |     |     |        |            |          |                |     |           |       |
techniques that extend MDP formulations by using data-
| effects, such         | as  | adverse selection,  |         | whereas  |          | profit-based  |     |         |           |                |     |      |               |     |
| --------------------- | --- | ------------------- | ------- | -------- | -------- | ------------- | --- | ------- | --------- | -------------- | --- | ---- | ------------- | --- |
|                       |     |                     |         |          |          |               |     | driven  | function  | approximation  |     | and  | conservative  |     |
| pricing  prioritizes  |     | short-term          | profit  |          | without  | considering   |     |         |           |                |     |      |               |     |
regularization to mitigate distributional shifts. For instance,
| borrower  | retention or lifetime value [8-9]. Second, these  |     |     |     |     |     |     |           |              |     |                               |     |     |     |
| --------- | ------------------------------------------------- | --- | --- | --- | --- | --- | --- | --------- | ------------ | --- | ----------------------------- | --- | --- | --- |
|           |                                                   |     |     |     |     |     |     | Khraishi  | and Okhrati  |     | (2022) employed conservative  |     |     | Q-  |
methods assume that pricing decisions are independent across
learning (CQL) to optimize consumer credit pricing policies
| applicants, neglecting  |     | portfolio-level  |     | risk  | interactions and  |     |     |                                              |     |     |     |     |           |        |
| ----------------------- | --- | ---------------- | --- | ----- | ----------------- | --- | --- | -------------------------------------------- | --- | --- | --- | --- | --------- | ------ |
|                         |     |                  |     |       |                   |     |     | using  static datasets of loan applications  |     |     |     |     | [17,18].  | Their  |
competitive dynamics. Finally, their reliance on pre-specified
approach demonstrated that offline RL could learn effective
functional forms for default risk and demand responses limits
personalized strategies without live experimentation, thereby
| adaptability  | to  | non-stationary  |     | environments.  |     |     | These  |     |     |     |     |     |     |     |
| ------------- | --- | --------------- | --- | -------------- | --- | --- | ------ | --- | --- | --- | --- | --- | --- | --- |
avoiding reputational and financial risks for lenders. This
challenges underscore the need for more flexible, data-driven
shift from classical MDPs to offline RL reflects a broader
| approaches—such  |     | as  reinforcement  |     |     | learning—that  |     | can  |                 |     |             |       |             |      |          |
| ---------------- | --- | ------------------ | --- | --- | -------------- | --- | ---- | --------------- | --- | ----------- | ----- | ----------- | ---- | -------- |
|                  |     |                    |     |     |                |     |      | methodological  |     | evolution:  | from  | rule-based  | and  | tabular  |
capture sequential decision-making, learn from historical
|     |     |     |     |     |     |     |     | models  | toward flexible,  |     | data-driven algorithms  |     |     | that can  |
| --- | --- | --- | --- | --- | --- | --- | --- | ------- | ----------------- | --- | ----------------------- | --- | --- | --------- |
data without restrictive assumptions, and optimize policies
|     |     |     |     |     |     |     |     | leverage  | large-scale  | consumer data, incorporate multiple  |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --------- | ------------ | ------------------------------------ | --- | --- | --- | --- |
under uncertainty.
objectives, and adapt to non-stationary environments.
2.2 MARKOV DECISION PROCESS MODELS IN
2.3 MARKOV DECISION PROCESS (MDP)
CREDIT RISK MANAGEMENT
A Markov Decision Process (MDP) provides a formal
One  significant  stream  of  research  has  modeled  mathematical framework for modeling sequential decision-
consumer credit management problems as Markov decision  making problems under uncertainty, in which outcomes are
processes (MDPs).  Early work by Bierman and Hausman  partly random and partly under the control of a decision
(1970)  and Frydman et  al.  (1985)  explored  repayment  maker (agent) [19]. In reinforcement learning, an MDP is
dynamics using Markov chains, while more recent studies  typically  defined  as  a  5-tuple ⟨S,  A,  P,  R,γ⟩,
have extended these ideas to credit card profitability and  where S represents the set of possible states, A the set of
dynamic limit  assignment. For example, So and Thomas  available actions, P(s′∣s,  a) the transition probability from
(2011) proposed an MDP framework in which states are  state ss to s′s′ after  taking  action aa, R(s,  a) the  expected
defined by borrowers’ behavioral score bands, and actions are  immediate  reward,  and γ∈[0,1)  the  discount  factor
the  credit  limits  assigned  each  period.  By  leveraging  determining the relative importance of future rewards. The
historical scoring data routinely collected by lenders under  defining feature of an MDP is the Markov property, which
Basel II/III regulations, they demonstrated that MDPs can  assumes that the future state depends only on the current state
produce optimal dynamic credit limit policies that maximize  and action, not on the full history of previous states. Formally,
expected profitability [10-13]. This approach highlights how  this property can be expressed as:
credit card operations—traditionally managed through static
P(st+1∣st, at,st−1,at−1,…,s0,a0) =P(st+1∣st, at).
| risk-return   | matrices—can  |       | benefit     |     | from     | sequential  |        |     |     |     |     |     |     |     |
| ------------- | ------------- | ----- | ----------- | --- | -------- | ----------- | ------ | --- | --- | --- | --- | --- | --- | --- |
| optimization  | methods       | that  | explicitly  |     | account  | for         | state  |     |     |     |     |     |     |     |
This assumption enables compact modeling of complex
transitions in borrower behavior.
|     |     |     |     |     |     |     |     | dynamic  | systems  | and  | allows  | for  | efficient  | recursive  |
| --- | --- | --- | --- | --- | --- | --- | --- | -------- | -------- | ---- | ------- | ---- | ---------- | ---------- |
Published By SOUTHERN UNITED ACADEMY OF SCIENCES LIMITED    2
Copyright ©  2026 The author retains copyright and grants the journal the right of first publication.
This work is licensed under a Creative Commons Attribution 4.0 International License.

Journal of Economic Theory and Business Management
Journal Home: https://www.suaspress.org/ojs/index.php/JETBM | CODEN: JETBAU
V ol. 3, No. 1, 2026 | ISSN 3006-4953 (Print) | ISSN 3006-4961 (Online)
computation of optimal decisions.  incorporated as exogenous variables influencing transition
probabilities P (s′∣s, a, ξt), where ξt denotes the economic
| In the context of credit risk  |     |     |     | management, the MDP  |     |     |     |     |     |     |     |     |     |
| ------------------------------ | --- | --- | --- | -------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
environment at time t. This coupling enables the model to
framework provides a natural way to represent the dynamics
|              |                |     |        |                        |     |     | capture cyclical  |     | variations in  |     | credit  behavior driven  |     | by  |
| ------------ | -------------- | --- | ------ | ---------------------- | --- | --- | ----------------- | --- | -------------- | --- | ------------------------ | --- | --- |
| of borrower  | behavior over  |     | time.  | Each state may encode  |     |     |                   |     |                |     |                          |     |     |
external conditions.
| features  | such  as  | the  borrower’s  |     | current  | credit  | score,  |     |     |     |     |     |     |     |
| --------- | --------- | ---------------- | --- | -------- | ------- | ------- | --- | --- | --- | --- | --- | --- | --- |
outstanding  balance,  repayment  history,  and  external  Beyond single-account MDPs, coupled Markov chains
macroeconomic  indicators.  The actions correspond  to  (Wozabal & Hochreiter, 2009) model correlated credit-state
lending decisions—such as whether to approve a loan, adjust  migrations across obligors by coupling individual Markov
a credit  limit,  or  modify interest  rates[20].  The reward  processes through shared latent factors, thereby capturing
function quantifies the short-term profit or loss associated  systemic risk  and contagion at the portfolio level.  This
with a decision, for instance, positive interest revenue from  perspective  can  complement  account-level  transaction
timely  repayments  versus  penalties  due  to  defaults.  authorization  by  incorporating  latent  factors  such  as
The discount factor γ reflects the time value of money and the  exogenous state variables or constraints, while an offline RL
uncertainty  of  future  cash  flows,  aligning  the  MDP  agent (e.g., CQL) learns cost-sensitive policies directly from
formulation with financial valuation principles.  logged authorization data, eliminating the need for online
experimentation. The resulting formulation preserves micro-
| The  | long-term  | objective  |     | of  the  | agent  | is  to  find  |     |     |     |     |     |     |     |
| ---- | ---------- | ---------- | --- | -------- | ------ | ------------- | --- | --- | --- | --- | --- | --- | --- |
level behavioral signals while accounting for cross-sectional
| a policy π(a∣s)—a  |     | mapping  | from  | states to  | actions—that  |     |                                  |     |     |     |                             |     |     |
| ------------------ | --- | -------- | ----- | ---------- | ------------- | --- | -------------------------------- | --- | --- | --- | --------------------------- | --- | --- |
|                    |     |          |       |            |               |     | dependencies, enabling policies  |     |     |     | that balance fraud losses,  |     |     |
maximizes the expected cumulative discounted return:
review costs, and customer friction under dynamic economic
|     | Gt=E[k=0∑∞γkRt+k+1].  |     |     |     |     |     | conditions.  |     |     |     |     |     |     |
| --- | --------------------- | --- | --- | --- | --- | --- | ------------ | --- | --- | --- | --- | --- | --- |
3.2 COST-SENSITIVE REWARD DESIGN
Solving these equations yields the policy that optimally
balances immediate and future returns. However, in real-
|     |     |     |     |     |     |     | In  | traditional  | supervised  |     | learning  |     | and  many  |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------ | ----------- | --- | --------- | --- | ---------- |
world credit scenarios, transition probabilities and reward
|     |     |     |     |     |     |     | reinforcement  | learning  |     | frameworks,  | all  | misclassification  |     |
| --- | --- | --- | --- | --- | --- | --- | -------------- | --------- | --- | ------------ | ---- | ------------------ | --- |
functions are rarely known in closed form. This motivates the
errors are treated as equally costly. However, in credit risk
| use  of reinforcement  |     | learning algorithms—such  |     |     |     | as  Q- |              |       |             |     |       |             |           |
| ---------------------- | --- | ------------------------- | --- | --- | --- | ------ | ------------ | ----- | ----------- | --- | ----- | ----------- | --------- |
|                        |     |                           |     |     |     |        | management,  | this  | assumption  |     | does  | not  hold.  | A  false  |
learning, SARSA, or value iteration—to directly approximate
|     |     |     |     |     |     |     | negative—approving  |     | a   | borrower  |     | who  | subsequently  |
| --- | --- | --- | --- | --- | --- | --- | ------------------- | --- | --- | --------- | --- | ---- | ------------- |
optimal value functions from historical data. These data-
defaults—can lead to substantial financial losses, while a
driven methods enable adaptive, sequential optimization of
|     |     |     |     |     |     |     | false positive—rejecting  |     |     | a creditworthy borrower—mainly  |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ------------------------- | --- | --- | ------------------------------- | --- | --- | --- |
credit decisions without requiring explicit knowledge of the
|     |     |     |     |     |     |     | affects customer experience  |     |     | and potential revenue.  |     |     | This  |
| --- | --- | --- | --- | --- | --- | --- | ---------------------------- | --- | --- | ----------------------- | --- | --- | ----- |
underlying transition dynamics.
|     |     |     |     |     |     |     | asymmetry in  | error     | costs       | motivates incorporating  |            |         | cost-    |
| --- | --- | --- | --- | --- | --- | --- | ------------- | --------- | ----------- | ------------------------ | ---------- | ------- | -------- |
|     |     |     |     |     |     |     | sensitive     | learning  | principles  |                          | into  the  | design  | of  the  |
3 METHODOLOGY
reinforcement learning reward function. Instead of merely
maximizing accuracy or expected reward, the agent explicitly
3.1 PROBLEM FORMULATION  learns to minimize total expected cost, defined as
We cast transaction authorization as a Markov Decision  ∁= 𝒄 ×𝑭𝑷×𝒄 ×𝑭𝑵
|     |     |     |     |     |     |     |     |     | 𝒇𝒑  |     | 𝒇𝒏  |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Process with action set A = {Approve, Review, Reject}. The
|     |     |     |     |     |     |     | where 𝒄 |  and 𝒄 |  denote the monetary or utility cost of  |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ------- | ------ | ---------------------------------------- | --- | --- | --- | --- |
environment state s concatenates (i) customer and transaction  𝒇𝒑 𝒇𝒏
false positive and false negative decisions, respectively. In
features, (ii) macro factors ξt, and (iii) cohort features from
practice, these parameters can be calibrated from portfolio
optional clusterings. A supervised score model (LR/LGBM)
|     |     |     |     |     |     |     | loss  statistics, default recovery rates, or business  |     |     |     |     |     | impact  |
| --- | --- | --- | --- | --- | --- | --- | ------------------------------------------------------ | --- | --- | --- | --- | --- | ------- |
produces a probability of fraud PD(s), which becomes part of
|     |     |     |     |     |     |     | analysis. Consequently, the learning  |     |     |     | objective shifts from  |     |     |
| --- | --- | --- | --- | --- | --- | --- | ------------------------------------- | --- | --- | --- | ---------------------- | --- | --- |
the state but does not define the policy by itself. The policy is
maximizing accuracy to minimizing cost, enabling the model
learned offline via a conservative algorithm (e.g., CQL) using
|     |     |     |     |     |     |     | to  prioritize  | high-risk  |     | scenarios  | with  | greater  | economic  |
| --- | --- | --- | --- | --- | --- | --- | --------------- | ---------- | --- | ---------- | ----- | -------- | --------- |
logged  data. Reward and constraints. We optimize a cost-
consequences.
sensitive objective:
Building on this framework, the reward function in the
r(s,a,y) =−(cfp 1[a=Approve∧y=Fraud]
proposed reinforcement learning environment is redefined as
+cfn 1[a∈{Reject, Review} ∧
the negative of the total cost, i.e.,
y=Legit]+crev 1[a=Review])
|     |     |     |     |     |     |     |     | 𝑹   | = −(𝒄 | ×𝑭𝑷 | ×𝒄 ×𝑭𝑷 | )   |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ----- | --- | ------ | --- | --- |
|     |     |     |     |     |     |     |     | 𝒕   | 𝒇𝒑    |     | 𝒕 𝒇𝒏   | 𝒕   |     |
subject to business rules and capital limits. Here, CFP
|     |     |     |     |     |     |     | which aligns  |     | the agent’s optimization behavior with  |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ------------- | --- | --------------------------------------- | --- | --- | --- | --- |
penalizes approving a fraudulent transaction (chargeback, ops  business objectives. This design effectively integrates the
| cost), CFPN penalizes  |     | declining/reviewing  |     |     | a   | legitimate  |     |     |     |     |     |     |     |
| ---------------------- | --- | -------------------- | --- | --- | --- | ----------- | --- | --- | --- | --- | --- | --- | --- |
principles of cost-sensitive learning into sequential decision-
transaction (customer friction),  and Crev captures manual  making: each policy update reflects the trade-off between risk
queue and latency costs. Moreover, macroeconomic factors
control and customer friction. Such a formulation also allows
such as GDP growth, unemployment, and interest rates were
|     |     |     |     |     |     |     | multi-objective extensions,  |     |     | for instance by incorporating  |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ---------------------------- | --- | --- | ------------------------------ | --- | --- | --- |
Published By SOUTHERN UNITED ACADEMY OF SCIENCES LIMITED    3
Copyright ©  2026 The author retains copyright and grants the journal the right of first publication.
This work is licensed under a Creative Commons Attribution 4.0 International License.

Journal of Economic Theory and Business Management
Journal Home: https://www.suaspress.org/ojs/index.php/JETBM | CODEN: JETBAU
V ol. 3, No. 1, 2026 | ISSN 3006-4953 (Print) | ISSN 3006-4961 (Online)
customer friction or portfolio utilization efficiency into the CQL penalizes overestimation of unseen actions by
reward structure. adding a regularization term that explicitly lowers Q-values
for actions not well supported by the data. This ensures that
the learned policy remains within the support of historical
behavior while remaining optimal in well-sampled regions.
BCQ, by contrast, constrains policy learning through a
generative behavior model that samples candidate actions
from the empirical data distribution. It then evaluates them
via a Q-network to select those expected to yield the highest
reward, effectively balancing exploitation of known good
actions with conservatism toward novel or uncertain ones.
FIGURE 1. CLOSED-LOOP OFFLINE RL FOR TRANSACTION Both methods enable stable policy improvement from
AUTHORIZATION.
historical credit data without requiring active
experimentation.
Historical batches t1…tnt1…tn are processed to
construct state features and labels (default vs. non-default). The process begins with preprocessed customer–
Optional customer clustering stabilizes policy generalization. transaction data and risk labels derived from historical
A cost matrix encodes asymmetric penalties 𝒄 and repayments. These inputs are used to construct an offline
𝒇𝒑
operational constraints. An offline RL agent (e.g., CQL) environment E (S, A, R) and a cost-sensitive reward function
learns a policy π(a∣s) to minimize expected total cost while defined as R−(cfp⋅FP+cfn⋅FN). A deep Q-network (DQN)-
preserving customer friction (authorization rate/utilization). based or actor–critic architecture is trained to approximate the
Ultimately, the policy outputs actions—approve or reject. state–action value function Q (s, a). The resulting policy
Outcomes are logged to compute economic rewards and outputs adaptive thresholds or action probabilities for loan
periodically retrain the policy, forming a closed-loop system. authorization, adjustment, or rejection. After training, the
The resulting RL agent can thus learn policies that adaptively model undergoes offline evaluation using metrics such as
balance profitability and prudence under varying market expected cost reduction, precision–recall trade-offs, and risk-
conditions, outperforming traditional fixed-threshold or adjusted return. The learned policy is then validated against
accuracy-driven models. As shown in Figure 1, for the baseline supervised classifiers (e.g., LightGBM or Logistic
monthly/rolling refresh, state construction, cost matrix, and Regression) to demonstrate its advantage in optimizing
the offline-to-online loop. business-aligned objectives beyond accuracy.
3.3 OFFLINE REINFORCEMENT LEARNING 4 EXPERIMENTS AND RESULTS
FRAMEWORK
4.1 DATASET DESCRIPTION
In real-world credit risk management, direct online
exploration—such as approving high-risk borrowers to gather We use the publicly available anonymized credit card
additional feedback—is impractical and ethically constrained. transaction dataset (often referred to as the ULB/Kaggle
To address this, the proposed framework adopts an offline dataset), which contains 284,807 records from European
reinforcement learning (offline RL) paradigm, enabling cardholders as of September 2013. The target Variable is
learning of an optimal policy from logged historical data binary (1 = fraud, 0 = legitimate), with 492 frauds (0.172%),
without interacting with the live environment. Offline RL resulting in an extreme imbalance that motivates cost-
extends the standard Markov Decision Process formulation sensitive evaluation.
introduced in Section 3.1, using fixed transition tuples (s, a,r,
Each transaction has 30 numeric features. V1–V28 are
s′) drawn from historical loan data. The agent aims to
PCA-transformed components of anonymized variables.
optimize a policy π(a∣s) that minimizes the total expected
Time denotes seconds since the first transaction in the dataset,
cost E[C] under the empirical distribution of past interactions,
and Amount is the transaction value. Following standard
while ensuring robustness to unseen state–action pairs. This
practice, we apply log (1 + Amount) and standardize Time
enables the model to extract optimal decision strategies from
and Amount using statistics fitted only to the training split to
static datasets, making it well suited to regulated financial
avoid leakage.
environments where exploration is infeasible.
We split the data chronologically into 70%/15%/15%
A key challenge in offline RL lies in distributional
for training/validation/testing (no shuffling), preserving
shift—the mismatch between the state–action pairs present in
temporal order to emulate sequential deployment. The dataset
the dataset and those that the learned policy may generate. To
does not contain action labels (e.g., “review”); actions are
mitigate this, conservative algorithms such as Conservative
policy decisions modeled in our cost function and used during
Q-Learning (CQL) and Batch-Constrained Q-Learning
offline policy evaluation. Figure 2 shows the class imbalance,
(BCQ) are employed.
Figures 3–5 depict temporal patterns, and Figures 6–7
summarize the distribution of Amount.
Published By SOUTHERN UNITED ACADEMY OF SCIENCES LIMITED 4
Copyright © 2026 The author retains copyright and grants the journal the right of first publication.
This work is licensed under a Creative Commons Attribution 4.0 International License.

Journal of Economic Theory and Business Management
Journal Home: https://www.suaspress.org/ojs/index.php/JETBM | CODEN: JETBAU
V ol. 3, No. 1, 2026 | ISSN 3006-4953 (Print) | ISSN 3006-4961 (Online)
TABLE 1. DATASET OVERVIEW AND CLASS IMBALANCE
4.2 EXPLORATORY DATA ANALYSIS
(KAGGLE CREDIT CARD FRAUD, SEPTEMBER 2013).
To better understand the statistical characteristics and
| Attribute  | Description  |     | Range  |     | /  Notes  |     |     |     |     |     |     |     |
| ---------- | ------------ | --- | ------ | --- | --------- | --- | --- | --- | --- | --- | --- | --- |
Type  behavioral differences between legitimate and fraudulent
Records  Total  number  284,807  492 are fraud  transactions,  an  exploratory  data analysis  (EDA)  was
conducted prior to model training. This analysis focuses on
|     | of transactions  |     |     |     | (0.172%)  |     |     |     |     |     |     |     |
| --- | ---------------- | --- | --- | --- | --------- | --- | --- | --- | --- | --- | --- | --- |
Features  V1–V28  Continuous  Scaled  and  class  imbalance,  temporal  patterns,  transaction amount
(PCA- anonymized  distributions, and inter-feature relationships, which jointly
transformed)  inform the construction of the state space and cost-sensitive
Time  Seconds  Continuous  Temporal  reward functions in the reinforcement learning framework.
elapsed  since  ordering  As shown in Figure  2, the dataset exhibits a severe class
first  imbalance, with  fraudulent transactions representing  only
|         | transaction  |     |             |     |         |     | 0.17% of all cases.   |     |     |     |     |     |
| ------- | ------------ | --- | ----------- | --- | ------- | --- | --------------------- | --- | --- | --- | --- | --- |
| Amount  | Transaction  |     | Continuous  |     | Highly  |     |                       |     |     |     |     |     |
|         | amount       |     |             |     | skewed  |     |                       |     |     |     |     |     |
distribution
| Class  | Target label  |     | Binary       | (0:  | Strong     |     |     |     |     |     |     |     |
| ------ | ------------- | --- | ------------ | ---- | ---------- | --- | --- | --- | --- | --- | --- | --- |
|        |               |     | Legitimate,  |      | imbalance  |     |     |     |     |     |     |     |
1: Fraud)
The dataset is widely used in financial machine learning
| benchmarks           |          | due                 | to                    | its realistic      |                | transaction  |     |     |     |     |     |     |
| -------------------- | -------- | ------------------- | --------------------- | ------------------ | -------------- | ------------ | --- | --- | --- | --- | --- | --- |
| behavior and severe  |          | class               | imbalance, making it  |                    |                | an ideal     |     |     |     |     |     |     |
| testing              | ground   | for cost-sensitive  |                       | offline            | reinforcement  |              |     |     |     |     |     |     |
| learning             | models.  | In  this            | study,                | the                | dataset        | is  split    |     |     |     |     |     |     |
| chronologically      |          | into training       |                       | (70%), validation  |                | (15%),       |     |     |     |     |     |     |
and testing (15%) sets to simulate a temporal deployment  FIGURE 3. DENSITY OF TRANSACTIONS OVER TIME (S) BY
| scenario where new transactions arrive sequentially.  |     |     |     |     |     |     |                                    |                       | CLASS  |             |              |           |
| ----------------------------------------------------- | --- | --- | --- | --- | --- | --- | ---------------------------------- | --------------------- | ------ | ----------- | ------------ | --------- |
|                                                       |     |     |     |     |     |     | Such                               | an  imbalance         | can    | lead        | to  biased   | decision  |
|                                                       |     |     |     |     |     |     | boundaries if                      | standard classifiers  |        | are used    | without      | cost      |
|                                                       |     |     |     |     |     |     | adjustment                         | or  resampling.       |        | Therefore,  | subsequent   |           |
|                                                       |     |     |     |     |     |     | experiments employ cost-sensitive  |                       |        | weighting   | and offline  |           |
reinforcement learning to mitigate this bias.

FIGURE 2. CLASS DISTRIBUTION (EXTREME IMBALANCE).
FIGURE 4. TOTAL AMOUNT AGGREGATED BY HOUR.
| As  | summarized  | in  | Table  | 1, the  | dataset contains  |     |     |     |     |     |     |     |
| --- | ----------- | --- | ------ | ------- | ----------------- | --- | --- | --- | --- | --- | --- | --- |
284,807 transactions with 492 frauds (0.172%), confirming  As shown in Figure 3 (all transactions) and Figure  4
(fraud-only), hourly aggregates display clear diurnal cycles,
| an extreme class  |     | imbalance. Features V1–V28 are PCA  |     |     |     |     |     |     |     |     |     |     |
| ----------------- | --- | ----------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
components; Time is  seconds  since  the  first  while  fraud exhibits  narrower and more irregular  peaks,
transaction; Amount is  highly  skewed  and  modeled  consistent  with  time-based  behavioral  clustering.  These
temporal dynamics justify including time-of-day (and related
with log⁡(1+Amount) log(1+Amount).
calendar features) in the RL state, allowing the policy to adapt
Figure 2 illustrates the imbalance visually: the fraud
decisions based on transaction timing.
| bar is  nearly  |                 | invisible                         | at the original  |     | scale. This  | skew        |     |     |     |     |     |     |
| --------------- | --------------- | --------------------------------- | ---------------- | --- | ------------ | ----------- | --- | --- | --- | --- | --- | --- |
| motivates       | cost-sensitive  |                                   | objectives       |     | and          | off-policy  |     |     |     |     |     |     |
| evaluation,     | rather          | than accuracy alone; throughout,  |                  |     |              | we          |     |     |     |     |     |     |
therefore report cost metrics under (cfp, cfn, crev) and avoid
random shuffling by using chronological splits.

Published By SOUTHERN UNITED ACADEMY OF SCIENCES LIMITED    5
Copyright ©  2026 The author retains copyright and grants the journal the right of first publication.
This work is licensed under a Creative Commons Attribution 4.0 International License.

Journal of Economic Theory and Business Management
Journal Home: https://www.suaspress.org/ojs/index.php/JETBM | CODEN: JETBAU
V ol. 3, No. 1, 2026 | ISSN 3006-4953 (Print) | ISSN 3006-4961 (Online)
FIGURE 6. AMOUNT BY CLASS: RAW VS. LOG-SCALED
BOXPLOTS
The left plot displays the complete amount range,
including extreme outliers, while the right plot zooms in on
the 0–250 range to highlight median differences and
variability.
FIGURE 5. TOTAL AMOUNT OF FRAUD TRANSACTIONS BY 4.4 FEATURE CORRELATION AND PCA
HOUR BEHAVIOR
Further analysis of the transaction amount reveals that To better understand the structural relationships among
fraudulent transactions tend to occur at both very low and the features, a correlation analysis was conducted on all
very high transaction values, as illustrated in Figure 5. The numerical variables in the dataset. Since the features V1–V28
bimodal nature of fraud amount distributions suggests the were obtained through Principal Component Analysis (PCA),
coexistence of two behavioral archetypes: “micro-fraud,” they are expected to be approximately orthogonal. However,
aimed at evading detection thresholds, and “high-stakes several components exhibit moderate correlations with key
fraud,” targeting large-value transactions. This heterogeneity behavioral indicators such as Amount, Time, and the target
motivates the use of adaptive reward scaling in the design of variable Class.
RL.
Most PCA-derived components remain weakly
correlated (|r| < 0.3), indicating limited redundancy among
4.3 TRANSACTION AMOUNT DISTRIBUTION
latent dimensions. Notably, V14, V17, and V21 show slightly
The transaction amount is one of the most informative higher negative correlations with the fraud label (Class = 1),
variables in credit card fraud detection. To understand how consistent with prior studies suggesting these components
transaction value relates to fraudulent behavior, we examined encode transaction irregularities and spending pattern
the statistical distribution of the Amount feature across the anomalies. Meanwhile, the Amount feature demonstrates a
two classes. As shown in Figure 6, legitimate transactions mild positive correlation with Class, reaffirming its
(Class = 0) exhibit a highly skewed distribution, with most importance in fraud detection models.
values concentrated below $100, while fraudulent
PCA components (V1–V28) exhibit weak
transactions (Class = 1) display a wider variance and a greater
intercorrelations, while the amount and selected components,
number of extreme values.
such as V14 and V17, Display moderate relationships with
This discrepancy suggests that fraudulent activities are the fraud label. To further analyze temporal dependencies,
often associated with atypical purchase patterns — either Figure 7 plots transaction amounts against time. The results
small micro-transactions designed to evade detection reveal sporadic high-value spikes distributed throughout the
thresholds or sporadic high-value purchases aimed at observation period, many of which correspond to fraudulent
maximizing illicit gains. The right-hand panel of Figure 6 transactions. This pattern supports the hypothesis that
presents a zoomed-in view, confirming that the median fraudulent behavior does not follow regular time cycles but
transaction amount for fraud cases is higher and exhibits rather opportunistic bursts—an important consideration when
greater dispersion. defining temporal states for the reinforcement learning agent.
Such heterogeneity in transaction magnitude implies By combining insights from both the correlation and
that static threshold-based systems may perform poorly, as temporal amount analyses, this study identifies a compact yet
they fail to adapt to dynamic risk levels. Therefore, the expressive feature subset for model input, comprising:
reinforcement learning framework later introduced in Section
𝑺= [𝑽 ,𝑽 ,𝑽 ,𝐀𝐦𝐨𝐮𝐧𝐭,𝐓𝐢𝐦𝐞,𝐇𝐨𝐮𝒓]
5 leverages transaction amount as a continuous state variable, 𝟏𝟒 𝟏𝟕 𝟐𝟏
enabling dynamic adjustment of authorization thresholds This representation balances dimensionality reduction
based on contextual risk signals. from PCA with interpretability for downstream cost-sensitive
reinforcement learning.
Published By SOUTHERN UNITED ACADEMY OF SCIENCES LIMITED 6
Copyright © 2026 The author retains copyright and grants the journal the right of first publication.
This work is licensed under a Creative Commons Attribution 4.0 International License.

Journal of Economic Theory and Business Management
Journal Home: https://www.suaspress.org/ojs/index.php/JETBM | CODEN: JETBAU
V ol. 3, No. 1, 2026 | ISSN 3006-4953 (Print) | ISSN 3006-4961 (Online)
interpretability of the offline RL state representation, where
V14–V21, Amount, and Time variables encapsulate both
|     |     |     |     | behavioral and financial risk  |     |     | signals.  | The reinforcement  |     |
| --- | --- | --- | --- | ------------------------------ | --- | --- | --------- | ------------------ | --- |
learning model leverages these embeddings to dynamically
|     |     |     |     | adjust  the  | authorization  |     | threshold,  | thereby  | improving  |
| --- | --- | --- | --- | ------------ | -------------- | --- | ----------- | -------- | ---------- |
sensitivity to rare but high-cost events.
5.2 COST-SENSITIVE REINFORCEMENT
LEARNING EVALUATION
To evaluate the effectiveness of the proposed Offline
Conservative Reinforcement Learning (CQL) framework, we
|     |     |     |     | benchmarked its  |     | performance against baseline classifiers  |     |     |     |
| --- | --- | --- | --- | ---------------- | --- | ----------------------------------------- | --- | --- | --- |

FIGURE 7. SCATTER PLOT OF TRANSACTION AMOUNT  under asymmetric cost conditions. As shown in Figure 9,
VERSUS TIME.  feature importance analysis confirms  that several  latent
components (V17, V14, V4) and the transaction Amount play
Fraudulent transactions tend to appear as isolated spikes,  a decisive role in identifying risky behaviors. The confusion
indicating non-stationary and opportunistic behavior patterns.  matrix shows a significant improvement in recall for fraud
|     |     |     |     | detection,  | while  | maintaining  | a  controlled  |     | false-positive  |
| --- | --- | --- | --- | ----------- | ------ | ------------ | -------------- | --- | --------------- |
5 CONCLUSION AND DISCUSSION  rate—a critical trade-off for user-centric financial systems.
5.1 MODEL PERFORMANCE AND FEATURE
INTERPRETABILITY
| The  proposed             | framework  | integrates  | conventional  |     |     |     |     |     |     |
| ------------------------- | ---------- | ----------- | ------------- | --- | --- | --- | --- | --- | --- |
| supervised models (e.g.,  | LightGBM,  | Logistic    | Regression)   |     |     |     |     |     |     |
with an offline reinforcement learning (RL) component to
jointly optimize credit risk control and customer friction.
| Figure  8 illustrates  | the  regression  | relationships  | between  |     |     |     |     |     |     |
| ---------------------- | ---------------- | -------------- | -------- | --- | --- | --- | --- | --- | --- |
transaction amount and key PCA-derived components (V2,
V5, V7, V20), revealing distinct behavioral signatures for
fraudulent and legitimate users. Legitimate transactions form
dense low-variance clusters, while fraudulent cases appear as
| sparse,  high-deviation  | outliers  | along  specific  | principal  |     |     |     |     |     |     |
| ------------------------ | --------- | ---------------- | ---------- | --- | --- | --- | --- | --- | --- |
components.

FIGURE 9. MODEL INTERPRETABILITY AND EVALUATION.
|     |     |     |     | (Top)  | Feature  | importance ranking  |     | highlighting  | key  |
| --- | --- | --- | --- | ------ | -------- | ------------------- | --- | ------------- | ---- |

behavioral and financial components;(Bottom) Confusion
FIGURE 8. RELATIONSHIP BETWEEN TRANSACTION
matrix showing improved fraud recall and balanced accuracy
AMOUNT AND KEY PCA FEATURES (V2, V5, V7, V20)
|     |     |     |     | achieved by  | the cost-sensitive  |     | RL  | policy.  | Compared to  |
| --- | --- | --- | --- | ------------ | ------------------- | --- | --- | -------- | ------------ |
ACROSS FRAUD AND NON-FRAUD CLASSES.
|     |     |     |     | traditional  | threshold-based  |     | or  | profit-maximization  |     |
| --- | --- | --- | --- | ------------ | ---------------- | --- | --- | -------------------- | --- |
approaches, the CQL framework achieves co-optimization of
Fraudulent transactions appear as sparse, high-deviation
credit risk and customer friction by directly minimizing the
points, reflecting nonlinear behavioral separability that the
expected misclassification cost:
| RL  agent  can exploit.  | This  | differentiation supports  | the  |     |     |     |     |     |     |
| ------------------------ | ----- | ------------------------- | ---- | --- | --- | --- | --- | --- | --- |
Published By SOUTHERN UNITED ACADEMY OF SCIENCES LIMITED    7
Copyright ©  2026 The author retains copyright and grants the journal the right of first publication.
This work is licensed under a Creative Commons Attribution 4.0 International License.

Journal of Economic Theory and Business Management
Journal Home: https://www.suaspress.org/ojs/index.php/JETBM | CODEN: JETBAU
V ol. 3, No. 1, 2026 | ISSN 3006-4953 (Print) | ISSN 3006-4961 (Online)
|          |             | 𝑳= 𝒄 | ×𝑭𝑷     | ×𝒄 ×𝑭𝑵     |     |             | Not Applicable.  |     |     |     |     |     |
| -------- | ----------- | ---- | ------- | ---------- | --- | ----------- | ---------------- | --- | --- | --- | --- | --- |
|          |             | 𝒇𝒑   |         | 𝒇𝒏         |     |             |                  |     |     |     |     |     |
| Through  | cost-aware  |      | policy  | learning,  |     | the  model  |                  |     |     |     |     |     |
DATA AVAILABILITY STATEMENT
| effectively        | captures  | contextual           |     | patterns  |                      | in  historical  |     |     |     |     |     |     |
| ------------------ | --------- | -------------------- | --- | --------- | -------------------- | --------------- | --- | --- | --- | --- | --- | --- |
| transaction logs,  |           | thereby eliminating  |     |           | the need for online  |                 |     |     |     |     |     |     |
Not Applicable.
| exploration  |     | and  | ensuring  |     | both operational  |     |     |     |     |     |     |     |
| ------------ | --- | ---- | --------- | --- | ----------------- | --- | --- | --- | --- | --- | --- | --- |
safety and regulatory compliance.
CONFLICT OF INTEREST
5.3 CONCLUSION
Not Applicable.
This research provides empirical evidence that offline
conservative reinforcement learning can serve as a practical
PUBLISHER'S NOTE
| and  ethically  | sound  | framework  |     | for  | optimizing  | credit  |     |     |     |     |     |     |
| --------------- | ------ | ---------- | --- | ---- | ----------- | ------- | --- | --- | --- | --- | --- | --- |
decision-making  under  asymmetric  risk  conditions.  By  All  claims  expressed  in  this  article  are  solely  those
combining cost-sensitive reward modeling with deep policy  of the  authors  and  do  not  necessarily  represent  those  of
approximation,  the  model  successfully  learns  adaptive  their affiliated organizations, or those of the publisher, the
lending  thresholds  that  minimize  financial  loss  while  editors and the reviewers. Any product that may be evaluated
reducing customer friction. The interpretability analysis of  in this article, or claim that may be made by its manufacturer,
PCA components and feature-importance rankings confirms  is not guaranteed or endorsed by the publisher.
that latent behavioral signals—particularly V14, V17, and
transaction Amount—exhibit significant predictive power,  AUTHOR CONTRIBUTIONS
| enabling  | the RL  | agent to  | detect high-risk  |     |     | patterns that  |     |     |     |     |     |     |
| --------- | ------- | --------- | ----------------- | --- | --- | -------------- | --- | --- | --- | --- | --- | --- |
conventional classifiers overlook. Compared with supervised  Not application.
| baselines,  | the  CQL-based  |     | model  | consistently  |     | achieves  |     |     |     |     |     |     |
| ----------- | --------------- | --- | ------ | ------------- | --- | --------- | --- | --- | --- | --- | --- | --- |
superior recall and cost efficiency, validating its suitability  ABOUT THE AUTHORS
for deployment in real-world financial systems constrained
| by regulatory and operational limits.  |     |     |     |     |     |     | XIMENG, Yang  |     |     |     |     |     |
| -------------------------------------- | --- | --- | --- | --- | --- | --- | ------------- | --- | --- | --- | --- | --- |
Beyond its technical contributions, this study advances  Board of Directors, Excellent Era Lending Service
the  conceptual  understanding  of  user-centric  credit  Corp., Makati, Philippines , PH, Cocoliu898@gmail.com.
management by framing risk control and incentive design as
YIMING, Zhang
a joint optimization problem rather than a binary trade-off.
The findings underscore that personalized credit strategies— Department of Financial Technology, Peking
when  guided  by  conservative  RL  policies—can  University, Peking, China , CN,
simultaneously  promote  consumer  welfare,  institutional  zhang1ming137@outlook.com.

stability, and macroeconomic growth. Future extensions may
explore multi-objective reinforcement learning architectures
that explicitly incorporate fairness, interpretability, and long- REFERENCES
| term user  | engagement metrics,  |                           |     | further strengthening  |     | the          |     |     |     |     |     |     |
| ---------- | -------------------- | ------------------------- | --- | ---------------------- | --- | ------------ | --- | --- | --- | --- | --- | --- |
| alignment  | between              | financial innovation and  |     |                        |     | sustainable  |     |     |     |     |     |     |
[1] Khraishi, R., & Okhrati, R. (2022, November). Offline
economic development.  deep  reinforcement learning  for  dynamic pricing  of

|     |     |     |     |     |     |     | consumer credit.  |     | In Proceedings  | of the  | Third  | ACM  |
| --- | --- | --- | --- | --- | --- | --- | ----------------- | --- | --------------- | ------- | ------ | ---- |
International Conference on AI in Finance (pp. 325–333).
ACKNOWLEDGMENTS
|     |     |     |     |     |     |     | [2] So, M. M.,  | & Thomas, L. C. (2011). Modelling  |     |     |     | the  |
| --- | --- | --- | --- | --- | --- | --- | --------------- | ---------------------------------- | --- | --- | --- | ---- |
profitability of credit cards by Markov decision processes.
Not Applicable.
European Journal of Operational Research, 212(1), 123–
130.
FUNDING
[3] Sewak, M. (2019). Temporal difference learning, SARSA,
Not Applicable.  and Q-learning:  Some  popular value  approximation-
|     |     |     |     |     |     |     | based  reinforcement  |     | learning  | approaches.  | In  | Deep  |
| --- | --- | --- | --- | --- | --- | --- | --------------------- | --- | --------- | ------------ | --- | ----- |
INSTITUTIONAL REVIEW BOARD  reinforcement learning: Frontiers of artificial intelligence
(pp. 51–63). Springer.
STATEMENT
[4] Sha, F., Ding, C., Zheng, X., et al. (2025). Weathering the
Not Applicable.  policy storm: How trade uncertainty shapes firm financial
|     |     |     |     |     |     |     | performance  | through  | innovation  | and  | operations.  |     |
| --- | --- | --- | --- | --- | --- | --- | ------------ | -------- | ----------- | ---- | ------------ | --- |
INFORMED CONSENT STATEMENT  International Review of Economics & Finance, 104274.
Published By SOUTHERN UNITED ACADEMY OF SCIENCES LIMITED    8
Copyright ©  2026 The author retains copyright and grants the journal the right of first publication.
This work is licensed under a Creative Commons Attribution 4.0 International License.

Journal of Economic Theory and Business Management
Journal Home: https://www.suaspress.org/ojs/index.php/JETBM | CODEN: JETBAU
V ol. 3, No. 1, 2026 | ISSN 3006-4953 (Print) | ISSN 3006-4961 (Online)
[5] Deng, X. (2025). Cooperative optimization strategies for  parallelism  optimization  methods  in  large  language
data collection  and machine  learning  in  large-scale  model-based  recommendation  systems.  arXiv.
distributed systems. In 2025 4th International Symposium  https://arxiv.org/abs/2506.17551
on Computer Applications and Information Technology
[17] Gonzalez, J., Tran, V., Meredith, J., Xu, I., Penchala, R.,
(ISCAIT) (pp. 2151–2154). IEEE.
|     |     |     |     |     |     |     | Vilar-Ribó,  | L.,  et  | al.  (2025).  | How  | it  begins:  | Initial  |
| --- | --- | --- | --- | --- | --- | --- | ------------ | -------- | ------------- | ---- | ------------ | -------- |
[6] Trench, M. S., Pederson, S. P., Lau, E. T., Ma, L., Wang,  response to opioids strongly predicts self-reported opioid
H., & Nair, S. K. (2003). Managing credit lines and prices  use disorder. medRxiv.
for Bank One credit cards. Interfaces, 33(5), 4–21.
|     |     |     |     |     |     |     | [18]  Wozabal, D.,  | &   | Hochreiter,  | R.  | (2012). A  | coupled  |
| --- | --- | --- | --- | --- | --- | --- | ------------------- | --- | ------------ | --- | ---------- | -------- |
[7] Wiesemann, W., Kuhn, D., & Rustem, B. (2013). Robust  Markov chain approach to credit risk modeling. Journal
Markov decision processes. Mathematics of Operations  of Economic Dynamics and Control, 36(3), 403–415.
Research, 38(1), 153–183.
[19] Kumar, A., Zhou, A., Tucker, G., & Levine, S. (2020).
[8] Tan, C., Gao, F., Song, C., Xu, M., Li, Y., & Ma, H.  Conservative  Q-learning  for  offline  reinforcement
(2024). Highly reliable CI-JSO based densely connected  learning.  Advances in  Neural  Information Processing
convolutional networks using transfer learning for fault  Systems, 33, 1179–1191.
diagnosis. Journal of Information Systems Engineering
[20] Mendonca, R., Geng, X., Finn, C., & Levine, S. (2020).
| and  |     |     |     |     | Management.  |     |                     |     |           |       |     |             |
| ---- | --- | --- | --- | --- | ------------ | --- | ------------------- | --- | --------- | ----- | --- | ----------- |
|      |     |     |     |     |              |     | Meta-reinforcement  |     | learning  | that  | is  | robust  to  |
https://doi.org/10.52783/jisem.v10i4.12207
|     |     |     |     |     |     |     | distributional  | shifts  | via  | model  | identification  | and  |
| --- | --- | --- | --- | --- | --- | --- | --------------- | ------- | ---- | ------ | --------------- | ---- |
[9] Tan, C., Gao, F., Song, C., Xu, M., Li, Y., & Ma, H.  experience  relabeling.  arXiv.
(2024). Proposed damage detection and isolation from  https://arxiv.org/abs/2006.07178
| limited  | experimental  |     | data based on  |     | a deep  | transfer  |     |     |     |     |     |     |
| -------- | ------------- | --- | -------------- | --- | ------- | --------- | --- | --- | --- | --- | --- | --- |

learning and an ensemble learning classifier. Journal of
| Information Systems  |     |     | Engineering  |     | and  Management.  |     |     |     |     |     |     |     |
| -------------------- | --- | --- | ------------ | --- | ----------------- | --- | --- | --- | --- | --- | --- | --- |
https://doi.org/10.52783/jisem.v10i4.12206
| [10] Han, X.,  |     | & Dou,  | X.  (2025). User  |     | recommendation  |     |     |     |     |     |     |     |
| -------------- | --- | ------- | ----------------- | --- | --------------- | --- | --- | --- | --- | --- | --- | --- |
method integrating hierarchical graph attention network
| with  | multimodal  |     | knowledge  | graph.  | Frontiers  | in  |     |     |     |     |     |     |
| ----- | ----------- | --- | ---------- | ------- | ---------- | --- | --- | --- | --- | --- | --- | --- |
Neurorobotics, 19, 1587973.
[11] Zhuang, R. (2025). Evolutionary logic and theoretical
construction of real estate marketing strategies under
| digital  | transformation.  |     | Economics  |     | and  Management  |     |     |     |     |     |     |     |
| -------- | ---------------- | --- | ---------- | --- | ---------------- | --- | --- | --- | --- | --- | --- | --- |
Innovation, 2(2), 117–124.
[12] Yang, Z., et al. (2025). RLHF fine-tuning of LLMs for
alignment with implicit user feedback in conversational
recommenders. arXiv. https://arxiv.org/abs/2508.05289
| [13]  Deng,  | X.,  | &  Yang,            | J.  (2025).  | Multi-layer  |               | defense  |     |     |     |     |     |     |
| ------------ | ---- | ------------------- | ------------ | ------------ | ------------- | -------- | --- | --- | --- | --- | --- | --- |
| strategies   | and  | privacy-preserving  |              |              | enhancements  | for      |     |     |     |     |     |     |
membership reasoning attacks in a federated learning
framework. In 2025 5th International Conference on
Computer Science and Blockchain (CCSB) (pp. 278–282).
IEEE.
[14] Tan, C. (2024). The application and development trends
| of  artificial  |     | intelligence  | technology  |     | in  | automotive  |     |     |     |     |     |     |
| --------------- | --- | ------------- | ----------- | --- | --- | ----------- | --- | --- | --- | --- | --- | --- |
production. Artificial Intelligence Technology Research,
2(5).
[15] Zhang, L., & Meng, Q. (2025, September). User portrait-
driven smart home device deployment optimization and
| spatial                   | interaction design.  |     | In             | 2025  | 5th  International  |     |     |     |     |     |     |     |
| ------------------------- | -------------------- | --- | -------------- | ----- | ------------------- | --- | --- | --- | --- | --- | --- | --- |
| Conference on Artificial  |                      |     | Intelligence,  |       | Automation and      |     |     |     |     |     |     |     |
High Performance Computing (AIAHPC) (pp. 724–728).
IEEE.
[16] Yang, H., Tian, Y., Yang, Z., Wang, Z., Zhou, C., & Li,
| D.  (2025).  |     | Research on  | model  | parallelism  |     | and data  |     |     |     |     |     |     |
| ------------ | --- | ------------ | ------ | ------------ | --- | --------- | --- | --- | --- | --- | --- | --- |
Published By SOUTHERN UNITED ACADEMY OF SCIENCES LIMITED    9
Copyright ©  2026 The author retains copyright and grants the journal the right of first publication.
This work is licensed under a Creative Commons Attribution 4.0 International License.