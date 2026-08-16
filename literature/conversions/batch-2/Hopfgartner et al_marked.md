---
conversion_metadata:
  converted_at: "2026-07-22T13:35:00Z"
  converter_tool: "markitdown"
  converter_version: "0.1.6"
  source_pdf: "Hopfgartner et al.pdf"
  source_pdf_sha256: "24f3b48a4719d16cd87e6b3c591e7472783debd736901e40858d71bca0e78372"
  page_count: 23
  markdown_char_count: 162939
---

<!-- PAGE-AWARE EXTRACTION (via pdfminer.six) -->

<!-- PAGE 1 -->

International Journal of Mental Health and Addiction (2026) 24:981–1003
https://doi.org/10.1007/s11469-024-01312-1

ORIGINAL ARTICLE

Using Artificial Intelligence Algorithms to Predict 
Self‑Reported Problem Gambling Among Online Casino 
Gamblers from Different Countries Using Account‑Based 
Player Data

Niklas Hopfgartner1 · Michael Auer1 · Denis Helic2 · Mark D. Griffiths3

Accepted: 22 April 2024 / Published online: 7 May 2024 
© The Author(s) 2024

Abstract
The prevalence of online gambling and the potential for related harm necessitate predic-
tive models for early detection of problem gambling. The present study expands upon prior 
research by incorporating a cross-country approach to predict self-reported problem gam-
bling  using  player-tracking  data  in  an  online  casino  setting.  Utilizing  a  secondary  data-
set comprising 1743 British, Canadian, and Spanish online casino gamblers (39% female; 
mean  age = 42.4  years;  27.4%  scoring  8 + on  the  Problem  Gambling  Severity  Index),  the 
present  study  examined  the  association  between  demographic,  behavioral,  and  monetary 
intensity  variables  with  self-reported  problem  gambling,  employing  a  hierarchical  logis-
tic regression model. The study also tested the efficacy of five different machine learning 
models to predict self-reported problem gambling among online casino gamblers from dif-
ferent countries. The findings indicated that behavioral variables, such as taking self-exclu-
sions, frequent in-session monetary depositing, and account depletion, were paramount in 
predicting  self-reported  problem  gambling  over  monetary  intensity  variables.  The  study 
also  demonstrated  that  while  machine  learning  models  can  effectively  predict  problem 
gambling  across  different  countries  without  country-specific  training  data,  incorporating 
such data improved the overall model performance. This suggests that specific behavioral 
patterns are universal, yet nuanced differences across countries exist that can improve pre-
diction models.

Keywords  Responsible gambling · Responsible gambling tools · Problem gambling · 
Problem Gambling Severity Index · PGSI · Machine learning · Artificial intelligence

Introduction

Online  gambling  involves  an  activity  where  money  is  wagered  on  the  internet  and  can 
involve  a  wide  variety  of  games  (e.g.,  sports  betting,  poker,  slots,  and  lotto).  Such  gam-
bling  can  take  place  on  personal  computers,  smartphones,  or  any  other  device  which  is 
connected to the internet. Over the past decade, online gambling has become more popular 
and widespread, leading to diverse regulatory landscapes across different countries (Selin,

Extended author information available on the last page of the article

---

<!-- PAGE 2 -->

982

International Journal of Mental Health and Addiction (2026) 24:981–1003

2019). For example, in the United States, the regulatory framework differentiates between 
online sports betting and online casino gambling, commonly known as iGaming (Holden & 
Edelman, 2020). These frameworks are crucial not only for regulating the industry, but also 
for monitoring how the increasing accessibility of online gambling affects the prevalence 
of problem gambling.

Prevalence of Problem Gambling Among Online Gamblers

As  the  present  study  investigated  self-reported  problem  gambling  of  online  gamblers 
across different countries, this section highlights recent research regarding the prevalence 
of problem gambling among these populations. Several studies have reported a higher risk 
prevalence  of  problem  gambling  among  online  gamblers  (e.g.,  Chóliz,  2016;  Elton-Mar-
shall et al., 2016; Hing et al., 2017). Hing et al. (2022) compared land-based-only gamblers 
(LBOGs), online-only gamblers (OOGs), and mixed-mode gamblers (MMGs), using data 
from  a  2019  Australian  national  telephone  survey  (N = 15,000).  MMGs  had  the  highest 
gambling  involvement,  gambling  problems,  and  gambling-related  harm.  Relative  risk  of 
gambling problems for MMGs exceeded that of both LBOGs and OOGs. The study found 
that  engaging  in  more  gambling  forms,  being  male,  being  single,  being  less  educated, 
being  indigenous,  and  speaking  a  non-English  language  increased  the  risk  of  problem 
gambling. Gambling on the internet (OOGs and MMGs combined) was associated with a 
higher problem gambling severity than land-based-only gambling.

Mora-Salgueiro  et  al.  (2021)  conducted  a  meta-study  of  prevalence,  comorbidities, 
and/or  demographics  of  online  disordered  gambling  using  studies  in  the  Medline  data-
base. There was a large variation in the prevalence of problem gambling (2.7% to 20.3%) 
reported by the selected studies. Prevalence rates of at-risk and disordered gambling among 
adolescents ranged from 5.7% to 57.52%. Being male and single were the most common 
risk factors among online gamblers with disordered gambling.

Tomei et al. (2022) collected survey responses from 1869 young males in Switzerland 
about offline and online gambling behaviors, as well as the severity of problem gambling. 
Compared to a previous study (Tomei et al., 2015), which reported that 16% of the partici-
pants gambled online during the past 12 months, Tomei et al. (2022) reported that 24% of 
participants gambled online. Moreover, 70% of online gamblers reported using the smart-
phone to access internet gambling sites. The study also found that compared to those with-
out gambling problems, those at-risk and those with gambling problems had higher preva-
lence rates of online gambling. The proportion of those at-risk or with gambling problems 
was approximately twice of those without problems among online-only gamblers.

The Use of Account‑Based Data in Problem Gambling Research

Online  gambling  operators  record  every  bet,  win,  deposit,  and  withdrawal,  and  therefore 
have objective data concerning each player’s money and time expenditure, as well as data 
on  every  game  played.  For  two  decades,  researchers  have  emphasized  the  potential  of 
player tracking as a method of detecting problematic gambling in online gambling settings 
(Catania  &  Griffiths,  2021;  Finkenwirth  et  al.,  2021;  Griffiths  &  Parke,  2002;  Haeusler, 
2016; Hancock et al., 2008). One way of assessing problem gambling among online gam-
blers is for operators to collect responses to a problem gambling screen from a sample of 
their gamblers. However, this involves substantial effort. Therefore, researchers frequently

---

<!-- PAGE 3 -->

International Journal of Mental Health and Addiction (2026) 24:981–1003

983

use  voluntary  self-exclusion  as  a  proxy  measure  for  problem  gambling  as  it  is  always 
recorded and readily available for analysis.

A number of studies have used voluntary self-exclusion as a proxy measure for problem 
gambling  (Hopfgartner  et  al.,  2023;  Nower  &  Blaszczynski,  2006a;  Percy  et  al.,  2016). 
The underlying assumption is that gamblers who voluntarily self-exclude are problem gam-
blers. An algorithm that detects gambling patterns which precede voluntary self-exclusion 
could then be used to identify problem gamblers. This would then allow gambling opera-
tors  to  interact  with  these  players.  Self-exclusion  is  a  very  common  responsible  gaming 
tool, and most regulated markets require licensed online gambling operators to offer vol-
untary self-exclusion (Catania & Griffiths, 2023). This might also be a reason for the rela-
tively large number of studies which have used voluntary self-exclusion as a proxy measure 
for problem gambling. Moreover, a few studies have used machine learning algorithms to 
analyze  correlations  between  voluntary  self-exclusion  and  preceding  gambling  behavior 
using player-tracking data (e.g., Finkenwirth et al., 2021; Hopfgartner et al., 2023).

Finkenwirth  et  al.  (2021)  used  20  variables,  including  gambling  frequency,  intensity, 
and variability to predict self-exclusion using player-tracking data. The study found that the 
variability in the amount of money wagered per session was the most important predictor 
of  self-exclusion.  This  variable  captured  betting  patterns  with  significant  fluctuations  in 
bet amounts, indicative of problematic gambling behaviors (e.g., loss chasing). The second 
most important predictor was the number of bets per day. The performance of the machine 
learning models varied between 65% and 76%, demonstrating the efficacy of player-track-
ing data in identifying individuals who might experience problem gambling.

Hopfgartner et al. (2023) applied hierarchal regressions using behavioral and monetary 
metrics.  In  the  first  step,  behavioral  variables,  such  as  the  type  of  payment  method,  fre-
quency of deposits, session length, and number of game types, were used. In the second step, 
monetary metrics, such as the amount of money lost, deposited, or withdrawn, were added. 
Interestingly,  very  few  of  the  monetary  metrics  significantly  improved  the  model  quality. 
The same study also reported that the number of voluntary limit changes, previous volun-
tary self-exclusions, number of deposits per session, number of different payment methods, 
and playing multiple types of games were predictive of future voluntary self-exclusion. The 
fact that the monetary variables were less important could reflect differences in the financial 
backgrounds of individual gamblers. For some gamblers, spending $1000 a month might be 
easily affordable whereas for others, spending just $100 per month might not be affordable.

Griffiths  and  Auer  (2016)  have  argued  that  there  can  be  some  issues  when  voluntary 
self-exclusion is used as a proxy measure for problem gambling in player tracking studies. 
This is because not all gamblers who self-exclude are problem gamblers and not all prob-
lem  gamblers  self-exclude.  After  analyzing  a  sample  of  7732  gamblers  who  voluntarily 
self-excluded  in  a  90-day  period,  Catania  and  Griffiths  (2021)  concluded  that  this  group 
was heterogeneous and therefore not a reliable proxy measure for problem gambling. More 
specifically, 19% of the gamblers played for less than 24 h before self-excluding and 50% 
of the gamblers played for less than a week before self-excluding. These findings suggested 
that gamblers were self-excluding for reasons other than problem gambling.

Combining Self‑Reported Problem Gambling and Player‑Tracking Data

Given that voluntary self-exclusion among online gamblers is a sub-optimal proxy meas-
ure of problem gambling, responses to standardized questionnaires on problem gambling 
have to be collected. The correlation between actual player-tracking data and self-reported

---

<!-- PAGE 4 -->

984

International Journal of Mental Health and Addiction (2026) 24:981–1003

gambling behavior can provide insight into the behavioral predictors of self-reported prob-
lem  gambling.  Five  player  tacking  studies  have  used  self-reported  problem  gambling  to 
predict problem gambling using player-tracking data (Auer & Griffiths, 2023a; Louderback 
et al., 2021; Luquiens et al., 2016; Murch et al., 2023; Perrot et al., 2022). All five stud-
ies collected self-reported problem gambling data using a problem gambling screen (e.g., 
PGSI, Ferris & Wynne, 2001) and correlated the self-report results with objective player 
tracking data. The resulting statistical models predicted the likelihood of a player being a 
self-reported problem gambler.

Murch  et  al.  (2023)  had  access  to  the  responses  of  the  PGSI  from  9145  adults  (aged 
18 + years)  who  played  on  lotoquebec.com.  The  website  offers  lottery,  casino,  and  sports-
betting products. The player-tracking data included time and money expenditure as well as 
responsible gambling (RG) tool use for the 12 months preceding the completion of the PGSI 
(using a 5 + score to indicate at-risk gambling and 8 + to indicate problem gambling). The 
final model retained 10 explanatory variables, including younger age and repeated deposit-
ing over a weekly period following a bet. The other significant variables were based on the 
amount of money bet and amount withdrawn. However, they did not examine any session 
explanatory variables which were based on gambling sessions. Their overall model had an 
area under the curve (AUC) of 84%. Although this was an impressive finding, it could also 
have been the result of a large number of inactive players in the final sample. More specifi-
cally, gamblers only needed to have at least one bet in the 12 months preceding the comple-
tion of the PGSI. Players with high PGSI scores most likely gambled shortly before answer-
ing questions on the PGSI, and players with low PGSI scores most likely gambled very little 
or not at all in the weeks before completing the PGSI. This means that any activity before 
completing the PGSI most likely contributed largely to the high model accuracy.

Perrot  et  al.  (2022)  collected  PGSI  responses  from  8172  French  online  sports  bettors 
and  poker  players,  as  well  as  5404  online  scratch-card  and  lottery  players.  Like  Murch 
et  al.  (2023),  they  used  the  same  PGSI  scoring.  The  AUC  values  which  reflect  model 
quality were 83% and 74% for the two samples. Player-tracking features (e.g., amount of 
money  lost,  deposited,  wagered,  gambling  days,  and  number  of  bets)  were  computed  for 
the 4 months preceding the PGSI completion, and only participants who showed any gam-
bling activity in the 30 days before were included. Chasing losses was operationalized as 
“making three deposits in less than 12 h” or “making a deposit less than 1 h after placing a 
bet” (Perrot et al., 2022, p. 3). Perrot et al. argued that a repeated sequence of deposits or a 
deposit that quickly followed a bet may reflect cases where gamblers lose all the remaining 
money on their account, and then try to recover the losses by depositing money. However, 
Perrot et al.’s study did not include online casino gamblers because it was limited to sports 
bettors, poker players, and lottery players. Casino games typically possess a much higher 
event frequency, which influences amount of money wagered, amount of money won, as 
well as the amount of time spent gambling (Auer & Griffiths, 2023d). Therefore, the results 
cannot be generalized to online casino gamblers.

Luquiens et al. (2016) developed predictive machine learning models based on PGSI 
responses from 14,261 online poker players. Explanatory variables were computed for 
the 30 days preceding the completion of the PGSI (using a PGSI score of 5 + for prob-
lem gambling). The risk factors of problem gambling reported by the predictive model 
were being male, being “compulsive” (i.e., defined by having at least three deposits in 
a 12-h period), being younger than 28 years, making a monetary deposit in the 30 days 
before completing the PGSI, having a mean loss per gambling session > €1.7, losing a 
total of > €45 in the last 30 days, having a total stake > €298 in the 30 days before com-
pleting the PGSI, having > 60 gambling sessions in the past 30 days, and multi-tabling.

---

<!-- PAGE 5 -->

International Journal of Mental Health and Addiction (2026) 24:981–1003

985

The model quality using the AUC was 72%. However, Luquiens et al.’s study was based 
on data from online poker players. Given that poker possesses different structural char-
acteristics to other forms of gambling, the findings might not be valid for online casino 
gamblers (Auer & Griffiths, 2023d).

Louderback et al. (2021) identified low-risk gambling thresholds based on a sample 
of  1772  online  casino  gamblers  who  completed  the  Brief  Biosocial  Gambling  Screen 
(BBGS; Gebauer et al., 2010). The BBGS comprises three items which can be answered 
“yes”  or  “no.”  Answering  any  item  ’yes’  was  considered  as  an  indication  for  problem 
gambling.  They  concluded  that  a  high  likelihood  of  self-reported  problem  gambling 
was  indicated  by  wagering  €167.97  or  more  each  month,  spending  more  than  6.71% 
of  annual  income  on  online  gambling  wagers,  losing  €26.11  or  more  per  month,  and 
demonstrating variability (i.e., standard deviation) in daily amount wagered of €35.14 or 
more over a 1-month period. In contrast to Murch et al. (2023), Perrot et al. (2022), and 
Luquiens  et  al.  (2016),  Louderback  et  al.  used  the  BBGS  to  assess  problem  gambling 
among a sample of online gamblers. Dowling et al. (2018) reported that the BBGS ade-
quately detects both problem and moderate-risk, but not low-risk, gambling. Moreover, 
Auer and Griffiths (2023e) did not find significant correlations between responses to the 
BBGS and player-tracking data in a sample of 1000 online slot gamblers.

Auer  and  Griffiths  (2023a)  were  given  access  to  the  raw  data  of  1287  players  from  a 
European  online  gambling  casino  who  answered  questions  on  the  PGSI.  They  used  the 
player tracking data 30  days before  completion  of  the PGSI  (using 8 + for problem gam-
bling) to train machine learning models. They found that self-reported problem gamblers 
lost  less  money,  deposited  less  money,  and  bet  on  fewer  days  compared  to  non-problem 
gamblers in the 30 days before answering the PGSI. However, self-reported problem gam-
blers  self-excluded  more  often  than  non-problem  gamblers  during  the  30  days  before, 
which might explain the lower overall activity. Self-reported problem gamblers lost more 
money  per  gambling  day,  lost  more  money  per  gambling  session,  and  deposited  money 
more frequently per gambling session. Problem gamblers also tended to deplete their gam-
bling  accounts  more  frequently  compared  to  non-problem  gamblers.  Auer  and  Griffiths 
(2023a) also recommended that online gambling operators should make depositing more 
than  once  per  day  more  difficult  to  prevent  players  from  chasing  their  losses.  However, 
Auer  and  Griffiths  did  not  analyze  country-specific  differences  regarding  the  association 
between self-reported problem gambling and player-tracking data.

The Present Study

Several  European  countries  (e.g.,  UK,  Germany,  Spain,  Sweden,  Denmark)  as  well  as 
the province of Ontario in Canada require online gambling operators to assess the risk of 
problem gambling among their players. However, as aforementioned, the body of research 
which  has  correlated  self-reported  problem  gambling  with  objective  gambling  behavior 
is  limited  (i.e.,  Auer  &  Griffiths,  2023a;  Louderback  et  al.,  2021;  Luquiens  et  al.,  2016; 
Murch et al., 2023; Perrot et al., 2022). Therefore, the present study attempted to increase 
the knowledge concerning the association between gambling behavior at an online casino 
and self-reported problem gambling. To do so, the study utilized a secondary dataset with 
gamblers from three different countries (i.e., Canada, Great Britain, and Spain). The pre-
sent study investigated the following three research questions (RQs):

---

<!-- PAGE 6 -->

986

International Journal of Mental Health and Addiction (2026) 24:981–1003

1.  What type of account-based tracking behavior correlates with self-reported problem

gambling? (RQ1)

2.  Can self-reported problem gambling be explained by behavioral variables independent

of the actual amount of money spent? (RQ2)

3.  Can machine learning models predict self-reported problem gambling across gamblers

from three countries? (RQ3)

These  research  questions  aimed  to  evaluate  whether  behavioral  variables  such  as 
the  number  of  deposits  per  session,  the  number  of  payment  accounts,  or  the  number 
of  failed  deposits  were  sufficient  to  predict  self-reported  problem  gambling  across 
online  casino  gamblers  from  different  countries.  This  reasoning  is  because  Auer  and 
Griffiths  (2023b)  predicted  high-risk  gambling  based  on  the  first  7  days  of  behavior 
after registration, and found that behavioral variables were responsible for a larger part 
of  model  accuracy  compared  to  monetary  intensity  variables.  Therefore,  the  present 
study extended previous lines of research by comparing player-tracking data with self-
reported problem gambling among players from three different countries to assess the 
importance  of  monetary  features  in  identifying  self-reported  problem  gambling.  The 
advantage  of  using  behavioral  variables  to  predict  problem  gambling  is  their  greater 
generalizability. Income levels vary across countries, which lead to deviations in mon-
etary measures such as amount of money bet, won, deposited, and withdrawn, impair-
ing the accuracy of prediction models. On the other hand, metrics such as the number 
of deposits, the number of gambling days, and gambling during the night are independ-
ent of income levels, leading to more robust and generalizable statistical models.

Additionally, the present study tested the generalizability of machine learning mod-
els to predict self-reported problem gambling among players from different countries. 
It is important to understand whether such models developed in specific countries can 
be effectively applied to players from other countries. Such data would likely provide 
valuable insights into the development of universally applicable responsible gambling 
tools and policies.

Method

The  authors  were  given  access  to  a  secondary  dataset  comprising  British,  Canadian, 
and Spanish online casino gamblers playing a variety of casino games (e.g., slots, rou-
lette,  and  blackjack)  who  completed  the  nine  PGSI  questions  between  January  2022 
and November 2023. If the PGSI was competed more than once, only the most recent 
answers were used. The nine PGSI questions are listed in Appendix 1. For each gam-
bler, the raw data 30 days before completing the PGSI were available. Every bet, win, 
deposit,  withdrawal,  the  type  of  game  played,  depositing  method,  and  withdrawal 
method were included in the data. Additionally, the monetary balance before and after 
each bet, win, deposit, and withdrawal was recorded. Session length was computed in 
line  with  previous  research  (e.g.,  Auer  &  Griffiths,  2023a,  2023b;  Hopfgartner  et  al., 
2023).  More  specifically,  if  two  bets  were  placed  within  a  15-min  period,  the  time 
between was counted as within session. If more than 15 min elapsed between two bets, 
they were counted as belonging to separate sessions.

---

<!-- PAGE 7 -->

International Journal of Mental Health and Addiction (2026) 24:981–1003

987

Study Design

Each of the nine PGSI items could be answered with “never” (0), “sometimes” (1), “most 
of the time” (2), and “almost always” (3). Therefore, the maximum score was 27, and the 
minimum  score  was  0.  Player-tracking  features  were  computed  for  the  30  days  prior  to 
completing  the  PGSI  (mirroring  the  studies  by  Auer  and  Griffiths  [2023a]  and  Luquiens 
et  al.  [2016]).  The  player-tracking  features  examined  are  listed  in  Appendix  2  and  are 
largely in line with those of Auer and Griffiths (2023a). Apart from the demographics (i.e., 
country, gender, and age in years), the player-tracking features included the total amount 
of money bet, lost, withdrawn, and deposited 30 days prior to PGSI completion. Monetary 
aspects can be a crucial aspect in the development of problem gambling (Tabri et al., 2022; 
Blaszczynski  and  Nower,  2010).  Previous  studies  have  also  emphasized  the  importance 
of  time  spent  gambling  in  the  development  of  problem  gambling  (Lin  et  al.,  2010;  Wil-
liams  et  al.,  2006).  The  player-tracking  features  also  included  behavioral  aspects  such  as 
the number of monetary deposits per session and the number of failed deposits (e.g., due to 
insufficient funds). The number of voluntary limit changes, as well as the number of volun-
tary temporary self-exclusions, was also included in the data collected. Two metrics (i.e., 
regular  account  depletion  and  frequent  depositing)  were  specifically  designed  to  assess 
impulsivity as it is a crucial aspect of problem gambling (Nower & Blaszczynski, 2006b).

1.  Regular account depletion: This was assessed using the percentage of sessions end-
ing with low account balance for each gambler. The authors had access to the account 
balance before and after each monetary bet, win, deposit, and withdrawal. The authors 
assumed that individuals with disordered gambling only stop gambling when their online 
gambling account is depleted. This metric indicates if less than €5 was left in the online 
gambling account at the end of a session. Furthermore, regular account depletion was 
identified by Auer and Griffiths (2023c) as a significant indicator of chasing losses.
2.  Frequent deposits: This was assessed using the average number of monetary deposits 
per session for each gambler. This metric was also highlighted as a significant indicator 
of chasing losses by Auer and Griffiths (2023c).

Statistical Analysis

A  hierarchical  logistic  regression  was  conducted  to  test  the  importance  of  three  catego-
ries  of  independent  variables,  as  proposed  by  Hopfgartner  et  al.  (2023).  These  were  age 
and gender (i.e., control variables), behavioral variables, and monetary intensity variables. 
These are listed in Appendix 2. First, three control models were fitted, one for each coun-
try, utilizing the control variables and a subsequent stepwise backward elimination process. 
Given  the  limited  number  of  groups  (i.e.,  three  countries),  individual  regression  models 
for each country (i.e., no pooling approach) were opted for as opposed to a mixed effects 
or a multilevel model (i.e., partial pooling approach) as recommended by Gelman and Hill 
(2006).  During  the  backward  elimination,  variables  with  the  highest  collective  p-value 
(Zaykin,  2011)  were  sequentially  excluded  until  only  variables  significant  in  at  least  one 
country remained.

To address RQ1, the authors employed the same methodology, conducting three regres-
sions  that  included  both  control  and  behavioral  variables.  These  models  (model  RQ1) 
were then evaluated against the initial control models. To address RQ2, monetary intensity

---

<!-- PAGE 8 -->

988

International Journal of Mental Health and Addiction (2026) 24:981–1003

variables were also added to the models (model RQ2), and comparisons were made with 
the previous models (model RQ1). A likelihood ratio chi-squared test was used to validate 
the significance of each feature category and with Akaike’s information criteria (AIC) pro-
viding additional information concerning potential improvements of the models.

To  mitigate  potential  multicollinearity  within  the  variables,  a  threshold  was  set  to 
include only those variables with a variance inflation factor (VIF) below 10 (James et al., 
2013). Standardization of all independent variables was performed to facilitate the compar-
ison between models. Coefficients are reported for each model, where negative coefficients 
indicate a decrease (and positive coefficients an increase) in the probability of self-reported 
problem  gambling.  To  assess  the  fit  of  all  models,  Nagelkerke’s  (1991)  R2  is  reported, 
quantifying the explained variance within the models.

To address RQ3, five different machine learning models were trained: AdaBoost, deci-
sion trees, extra-trees (extremely randomized trees), gradient boosting, and random forests. 
To test whether machine learning models generalized to other countries in predicting self-
reported problem gambling, each model was trained using data from two countries while 
reserving the third country for testing. This process allowed every country to function as a 
test set once to assess how well the models could be applied across countries.

For comparability, the authors also included a baseline model, which used the gamblers’ 
total amount of money deposited within the past 30 days as a direct score for self-reported 
problem  gambling.  The  rationale  for  this  baseline  was  to  evaluate  how  such  a  simple 
model, which only relied on the total monetary deposits, would compare to a model includ-
ing more complex behavioral variables. Therefore, the baseline model established a direct 
correlation,  where  higher  deposits  indicated  a  stronger  tendency  towards  problem  gam-
bling. To further evaluate whether incorporating country-specific data during model train-
ing  improved  the  overall  performance  of  the  prediction,  an  additional  model  was  trained 
which included the data of all three countries and performed a 70/30 train-test split on it.

The optimization of hyperparameters for each tree-based model was conducted through 
a  randomized  cross-validation  search,  using  a  unified  parameter  space.  For  parameters 
such  as  maximum  tree  depth  and  the  minimum  percentage  of  samples  per  leaf,  a  range 
was pre-defined, specifically from 2 to 10 for tree depth, and 0% to 10% samples per leaf. 
The  learning  rates  for  gradient  boosting  and  AdaBoost  were  set  within  a  0  to  0.5  range. 
Default parameters from the scikit-learn library (Pedregosa et al., 2011) were applied for 
any remaining parameters. The performance of all models was reported using the receiver 
operating characteristic area under the curve (ROC-AUC) values, which indicate the extent 
to  which  the  models  can  distinguish  between  individuals  with  and  without  self-reported 
problem gambling.

Participants

A total of 6352 players completed the nine PGSI questions between January 2022 and Novem-
ber 2023. Figure 1 displays the PGSI score distribution before and after data cleaning. The 
PGSI score and the respective frequency were negatively correlated (i.e., most gamblers had 
low PGSI scores). However, before data cleaning, there was strong increase in scoring 27 (the 
maximum score) on the PGSI. In line with Auer and Griffiths (2023a), it was assumed that this 
spike was caused by gamblers who did not take enough time and simply rushed through the 
scale items. Therefore, participants who completed the PGSI in less than 1 min were excluded 
from the analysis to ensure the reliability of the data, leaving 1743 participants.

---

<!-- PAGE 9 -->

International Journal of Mental Health and Addiction (2026) 24:981–1003

989

Fig. 1   Distribution of PGSI responses before and after removing participants who completed the PGSI in 
under a minute. The percentages above the orange bars indicate the percentage of participants which were 
retained after removing short response times

Less  strict  variations  to  this  exclusion  criterion  (e.g.,  only  excluding  participants  who 
completed the PGSI in less than 40 s or 50 s) yielded significant, but not practically rele-
vant differences. The 1-min threshold was also empirically supported by the observed data 
pattern for participants who scored 27 out of 27 on the PGSI. A visible natural gap in com-
pletion times around the 1-min mark, as shown in Fig. 2, indicated a difference between 
participants who engaged thoughtfully with the PGSI survey questions and those who did 
not.  This  pattern  confirmed  the  use  of  this  threshold  and  suggested  that  responses  com-
pleted  in  less  than  1  min  were  unlikely  to  reflect  genuine  self-assessment  and  therefore

Fig. 2   Distribution of PGSI completion times for gamblers who scored 27 out of 27. A natural gap in com-
pletion  times  around  the  1-min  mark  indicates  a  separation  between  gamblers  who  thoughtfully  engaged 
with the PGSI items and those who likely rushed their responses

---

<!-- PAGE 10 -->

990

International Journal of Mental Health and Addiction (2026) 24:981–1003

indicated a lack of engagement with the PGSI survey questions. Notably, the distribution 
of scores after this cleaning process shows a stronger reduction in the proportion of partici-
pants with extreme scores of 0 and 27, supporting the hypothesis that these responses were 
likely hasty and uniformly answered with the same response, indicating a potential bias in 
the validity of their data.

Table  1  presents  a  comparative  overview  of  gambling  statistics  by  the  participants 
across  the  three  countries  (Canada,  Spain,  GB)  in  the  dataset.  Canadian  gamblers  com-
prised  6.0%  of  the  sample,  with  a  mean  PGSI  score  of  7.11,  and  35.2%  having  a  PGSI 
score equal or above 8 (indicating problem gambling). The mean age of Canadian gamblers 
was 45.9 years, and the proportion of female gamblers was 40.0%. British gamblers com-
prised 73.7% of the sample, with a mean PGSI score of 5.47, and 26.4% having a PGSI 
score of equal or above 8. The mean age of British gamblers was 43.5 years, and the pro-
portion of female gamblers was 41.8%. Spanish gamblers comprised 20.3% of the sample, 
with an average PGSI score of 5.67, and 28.9% having a PGSI score of equal or above 8. 
The mean age of Spanish gamblers was 37.3 years, and the proportion of female gamblers 
was 28.3%. Overall, the mean PGSI score across the total sample of gamblers was 5.61, 
and 27.4% having a PGSI score of equal or above 8. The mean age of the total sample was 
42.4 years, and the proportion of female gamblers was 39.0%. These results highlight the 
cross-national variations in the demographic and risk profile of the gamblers from the three 
different countries.

The  cross-national  variations  in  gambling  behaviors,  as  indicated  by  the  PGSI  scores 
among participants from Canada, GB, and Spain, were further evident in the post hoc anal-
ysis  shown  in  Table  2.  This  analysis  showed  statistically  significant  differences  in  PGSI 
scores  between  the  gamblers  from  the  three  countries  (Kruskal–Wallis  test:  H = 18.3, 
p < 0.001).  Notably,  the  difference  between  Canadian  and  British  gamblers,  as  well  as 
between  Canadian  and  Spanish  gamblers,  was  significant  (U = 51,348,  p < 0.001  and 
U = 14,996, p = 0.0014, respectively), indicating that Canadian gamblers had a significantly 
higher  PGSI  score  compared  to  their  British  and  Spanish  counterparts.  The  difference 
between the PGSI scores from Spanish and British gamblers (U = 213,829, p = 0.0486) was

Table 1   Descriptive statistics of the dataset per country

Country

Number of players Mean PGSI

Canada

Great Britain
Spain

105 (6.0%)

1285 (73.7%)
353 (20.3%)
1743 (100%)

score

7.11

5.47
5.67
5.61

Players with 
PGSI 8 +

Mean
age

Female gamblers

37 (35.2%)

339 (26.4%)
102 (28.9%)
478 (27.4%)

45.9 years

43.5 years
37.3 years
42.4 years

40%

41.8%
28.3%
39.0%

not  significant  after  Bonferroni  correction  for  multiple  testing  (i.e.,  corrected  alpha  level

Table 2   Post hoc tests for differences in the countries’ PGSI scores. Significant p-values highlighted in bold 
according to the Bonferroni corrected alpha level of 0.05/3 = 0.016

Great Britain

Spain

Canada

< 0.001

0.0014

Great Britain

-

0.0486

---

<!-- PAGE 11 -->

International Journal of Mental Health and Addiction (2026) 24:981–1003

991

of 0.016). These findings align with the initial observations from Table 1, which suggested 
notable variations in the gambling risk profiles across these nations.

Ethics

The study adhered to the guidelines set forth in the Declaration of Helsinki and received 
approval from the research team’s university ethics committees.

Results

Table 3 highlights descriptive statistics distinguishing problem gamblers (PGs, PGSI score 
8 +) from non-problem gamblers (NPGs, PGSI score < 8). PGs had a lower mean amount 
of money deposited in the 30 days before completing the PGSI (€524), as compared to the 
average of €708 deposited by NPGs. However, a Mann–Whitney U test showed no signifi-
cant difference between PGs and NPGs in the amount of money deposited (U = 290,854.5, 
p = 0.2207).  A  significant  difference  in  age  was  observed  between  PGs  and  NPGs.  As  a 
Shapiro–Wilk test reported that the age was not normally distributed (S = 0.98, p < 0.001), 
a  Mann–Whitney  U  test  indicated  that  PGs  were  significantly  younger  than  NPGs 
(U = 235,128,  p < 0.001).  The  proportion  of  female  gamblers  did  not  significantly  differ 
between PGs (36.2%) and NPGs (40.0%; Z = 1.45, p = 0.146).

Associating Player‑Tracking Data with Self‑Reported Problem Gambling (RQ1 
and RQ2)

Figure 3 shows the findings from hierarchical regression analyses focusing on the predic-
tors of self-reported problem gambling. The control models (Fig. 3a) explored the impact 
of  demographics  after  backward  elimination,  showing  that  in  Great  Britain  and  Spain, 
younger  gamblers  were  more  likely  to  be  self-reported  problem  gamblers,  with  a  visible 
but  non-significant  trend  in  Canada  suggesting  the  same  direction.  A  solid  dot  indicates 
statistical  significance  and  a  cross  that  the  variable  is  not  statistically  significant  in  that 
country.

The models addressing RQ1 in Fig. 3b incorporated behavioral variables to assess their 
influence on self-reported problem gambling. The results suggested that specific behaviors, 
such as taking self-exclusions, gambling for a shorter average session length, frequent in-
session  depositing,  and  frequent  depletion  of  the  gambling  balance,  were  indicators  of  a 
higher likelihood towards self-reported problem gambling. Frequent in-session depositing

Table 3   Descriptive statistics for problem gamblers (PG, i.e., PGSI score 8 +) and non-problem gamblers 
(NPG; PGSI score < 8)

Self-reported 
problem gambler

Number of 
players

Mean amount of 
money deposited 
(€)

Mean number of 
active gambling 
days

Mean
age

Female gamblers

No

Yes

1265 (72.6%)

478 (27.4%)
1743 (100.0%)

708

524
657

8

7
8

43.7 years

40.0%

39.2 years
42.4 years

36.2%
39.0%

---

<!-- PAGE 12 -->

992

International Journal of Mental Health and Addiction (2026) 24:981–1003

Fig. 3   Coefficients including 95% confidence intervals for the hierarchical regression analyses. Each model 
consisted  of  three  separate  regressions  (i.e.,  one  for  each  country)  and  included  only  those  variables  that 
were significant in at least one country. Solid dots indicate statistical significance

was  significantly  associated  with  self-reported  problem  gambling  in  two  countries  (i.e., 
Canada and Spain). The other behavioral variables were only significantly associated with 
self-reported problem gambling in one of the three countries. Overall, adding behavioral 
features to the models significantly increased the Nagelkerke R2 (see likelihood ratio chi-
square tests in Table 4 for RQ1) and reduced the AIC compared to the model which only 
contained the control variables. Only in Canada did the inclusion of behavioral variables 
not significantly improve the model performance (χ2 = 6.2, df = 4, p = 0.184).

RQ2, illustrated in Fig. 3c, adds monetary gambling intensity variables to the aforemen-
tioned  demographics  and  behavioral  features.  The  results  suggested  that  monetary  vari-
ables did not significantly improve the models’ performance, given the inclusion of demo-
graphics and behavioral features. Therefore, the backward elimination resulted in the same 
models as for RQ1, suggesting that beyond behavioral patterns, the intensity of monetary

Table 4   Likelihood ratio chi-squared test (LRT), Nagelkerke-R2 (NK-R2), and AIC values for the hierarchi-
cal regression analyses. Significant p-values highlighted in bold according to the Bonferroni corrected alpha 
level of 0.05/3 = 0.016. Note that the values of the Nagelkerke-R2 and the AIC are the same for RQ2, as the 
final models were the same. Therefore, also no LRT for RQ2 was calculated

Canada (CA)

Great Britain (GB)

Spain (ES)

LRT (RQ1)

LRT (RQ2)

NK-R2

AIC

χ2(df)
p-value
χ2(df)
p-value
Model control
Model RQ1
Model RQ2
Model control
Model RQ1
Model RQ2

6.2 (4)

145.5 (4)

0.184
-
-
0.013
0.091
0.091
139.3
141.0
141.0

< 0.001
-
-
0.044
0.196
0.196
1447.5
1310.0
1310.0

19.1 (4)

< 0.001
-
-
0.045
0.118
0.118
417.2
406.0
406.0

---

<!-- PAGE 13 -->

International Journal of Mental Health and Addiction (2026) 24:981–1003

993

gambling  does  not  significantly  contribute  to  the  likelihood  of  self-reported  problem 
gambling.

Overall, the regression analyses emphasized the significance of behavioral factors over 
monetary ones when associating player-tracking data with self-reported problem gambling. 
The models showed that age and specific gambling behaviors, like self-exclusions, in-ses-
sion depositing, and account depletion were more important predictors than the amount of 
money gambled.

Predicting Self‑Reported Problem Gambling (RQ3)

Table  5  shows  the  performance  (ROC-AUC  values)  of  various  machine  learning  models 
in  predicting  self-reported  problem  gambling.  In  the  first  approach,  data  from  one  coun-
try was reserved for testing, and the other two countries provided the training data. This 
approach enabled the testing of whether the models generalized across countries in predict-
ing self-reported problem gambling. For the second approach, a standard 70/30 train-test 
split on the entire data was utilized, and the performance was reported by country. With 
this  approach,  each  country’s  data  were  included  in  the  training  dataset,  which  provided 
country-specific patterns to the models.

The results from Table 5 indicated the machine learning models, which are trained on 
data from all three countries, outperformed those that were trained on two countries only. 
For Canada, the random forest model, which was trained including Canadian players, had 
a ROC-AUC score of 0.717, while the extra-trees model which was only trained on data 
from  GB  and  Spain  had  a  score  of  0.662.  In  Great  Britain,  the  extra-trees  model  with 
which was trained including British players had a ROC-AUC of 0.699, compared to 0.644 
(random forest) which was only trained on Canadian and Spanish players. In Spain, the 
highest score for the model, which was trained including Spanish players, was 0.654 (gra-
dient boosting), while the decision tree, which was only trained on British and Canadian 
players, had a ROC-AUC of 0.609.

The  baseline  model’s  performance,  utilizing  the  total  amount  of  money  deposited 
as  a  stand-alone  predictor,  had  an  ROC-AUC  value  of  approximately  0.5.  Therefore,

Table 5   ROC-AUC values of the five machine learning models for each country. In the first approach, one 
country was left out during training and was used as test set. In the second approach, a global model trained 
on all data was used and a 70/30 split into training and test data was applied

Canada

Canada 
data left 
out

0.518

0.575
0.592

0.662
0.588

Baseline

AdaBoost
Decision tree
Extra-trees
Gradient 
boosting

Random forest 0.600

Great Britain

Spain

Entire dataset GB data left

Entire dataset Spain data left

Entire dataset

out

0.476

0.597
0.585
0.617
0.577

0.644

out

0.548

0.572

0.609
0.541
0.585

0.597

0.476

0.606
0.598
0.699

0.653

0.653

0.518

0.515
0.475
0.613
0.570

0.717

0.548

0.631
0.519
0.598
0.654

0.647

---

<!-- PAGE 14 -->

994

International Journal of Mental Health and Addiction (2026) 24:981–1003

its performance was similar to a random guess, emphasizing the limitations of relying 
solely on a monetary metric. This result again highlighted the importance of behavio-
ral  variables  in  the  detection  of  self-reported  problem  gambling.  Overall,  the  results 
indicated  that  including  country-specific  patterns  generally  enhanced  the  models’ 
predictive  power.  However,  the  variance  in  ROC-AUC  scores  across  different  models 
and  countries  also  emphasized  the  importance  of  model  selection  based  on  the  data 
characteristics.

Discussion

The  present  study  analyzed  the  correlation  between  self-reported  PGSI  responses  and 
actual gambling behavior in a secondary dataset of 6352 Spanish, British, and Canadian 
(from  the  Canadian  province  Ontario  only)  online  casino  gamblers.  Out  of  the  6352 
gamblers, 1743 spent at least 1 min responding to the nine items. These were retained 
for  further  analysis.  In  line  with  Auer  and  Griffiths  (2023a),  the  minimum  answering 
time  was  seen  as  an  indication  responding  to  the  items  seriously.  Taking  a  very  short 
amount of time to respond to all the items assumes that the gamblers did not properly 
read the questions, and therefore, the responses would not accurately reflect their prob-
lem gambling status. The data cleaning process removed the majority of the gamblers 
reaching  the  highest  score  (27/27)  as  they  chose  the  highest  answer  category  for  each 
of  the  nine  items.  The  same  effect  was  observed  on  the  lowest  end  of  the  score  range 
(0/27) as these gamblers always chose the lowest answer category for the nine items.

Out  of  the  1743  gamblers,  478  had  a  PGSI  score  of  8  or  more  out  of  27  (27.4%). 
A score of 8 + is considered as indicating problem gambling (Holtgraves, 2008). Sev-
eral other studies have collected PGSI responses from online gambling cohorts. Auer 
and Griffiths (2023a) reported that among a sample of European online casino players, 
26%  reported  a  PGSI  score  of  8  or  more.  Murch  et  al.  (2023)  reported  12%  problem 
gambling  among  a  sample  of  Canadian  online  casino  gamblers.  However,  the  Cana-
dian  online  gambling  site  also  offered  lottery  games,  which  are  less  likely  to  cause 
gambling problems which may have explained the lower prevalence of problem gam-
bling.  Among  a  sample  of  French  online  gamblers  (engaging  in  horse  betting,  sports 
betting, poker), 26% of gamblers reported problem gambling based on a PGSI score of 
8 + (Perrot et al., 2022). Therefore, the present study’s prevalence of problem gambling 
is in line with previous research using similar methodologies.

In the present study, the largest prevalence of problem gambling was observed among 
Canadian  gamblers  (35.2%).  Online  gambling  in  the  Canadian  province  of  Ontario  was 
introduced in 2022, whereas Spain legalized the online gambling market in 2011. To the 
best of the authors’ knowledge, legal online gambling has been available in Great Britain 
for over 20 years. The long availability of legal online gambling is also related to a longer 
history of regulation, which could have resulted in safer gambling practices and therefore 
lower  problem  gambling  rates.  Additionally,  the  UK  Gambling  Commission  frequently 
fines operators for player safety violations (e.g., Andrade et al., 2023; Gambling Commis-
sion, 2022a, 2022b), which could also have led to improved player protection.

---

<!-- PAGE 15 -->

International Journal of Mental Health and Addiction (2026) 24:981–1003

995

Demographics and Behaviors Associated with Self‑Reported Problem Gambling

Age was negatively associated with self-reported problem gambling, and the effect was 
significant  among  online  casino  gamblers  in  Great  Britain  and  Spain.  Although  there 
was a visible effect in Canada, it was not statistically significant. Many prevalence stud-
ies  have  reported  a  higher  prevalence  of  problem  gambling  among  younger  individu-
als (e.g., Abbott et al., 2014; Ekholm et al., 2014; 2015; Kun et al., 2012). Impulsivity 
(i.e., acting without thinking and the inability to delay gratification and sensation seek-
ing) and depression have been reported as key risk factors for problem gambling among 
adolescents  (e.g.,  Gupta  et  al.,  2013;  Secades-Villa  et  al.,  2016;  Turner  et  al.,  2008). 
Although online gambling is only legal from the age of 18 years in most countries, the 
adolescent brain does not fully mature until around the mid-20s (Andrews et al., 2021; 
Icenogle et al., 2019).

After  adding  behavioral  metrics  to  the  regression  model,  only  taking  self-exclu-
sions,  gambling  for  shorter  session  lengths,  frequent  monetary  depositing  per  session, 
and  regular  account  depletion  significantly  contributed  to  self-reported  problem  gam-
bling.  These  independent  variables  were  significant  in  at  least  one  of  the  three  coun-
tries.  Frequent  monetary  depositing  within  sessions  has  previously  been  reported  as  a 
behavior that is indicative of chasing losses (Auer & Griffiths, 2023c). Chasing losses 
is  a  crucial  aspect  of  impulsivity,  and  online  gambling  among  vulnerable  individuals 
can  have  negative  impacts  on  self-control  (Siemens  and  Kopp,  2011).  Depositing  fre-
quently  within  sessions  and  regular  account  depletion  also  significantly  contributed  to 
the prediction of self-reported problem gambling in a previous study (Auer & Griffiths, 
2023b). Moreover, Perrot et al. (2022) and Murch et al. (2023) also identified frequent 
depositing  (although  not  within  sessions)  to  be  significant  predictors  of  self-reported 
problem gambling.

Several  previous  studies  predicting  self-reported  problem  gambling  have  reported 
a  significant  association  with  self-exclusion.  Perrot  et  al.  (2022)  reported  that  31%  of 
those with problem gambling had taken at least one temporary self-exclusion since they 
started  gambling  online.  In  contrast,  only  4%  of  non-problem  gamblers  had  done  so. 
The respective percentages reported by Auer and Griffiths (2023a) in their study were 
46% among those with problem gambling and 12% among those with no problems.

Among  the  behavioral  variables,  the  average  time  spent  gambling  per  session  over 
the  past  30  days  was  also  significant.  However,  the  association  between  self-reported 
problem gambling and average time spent gambling was negative. This means that self-
reported problem gamblers average session length was lower compared to non-problem 
gamblers.  Time  devoted  to  gambling  has  been  reported  as  a  predictive  factor  of  online 
gambling  (Barrault  &  Varescon,  2013;  Hopley  &  Nicki,  2010).  Luquiens  et  al.  (2016) 
reported  a  significantly  longer  gambling  time  for  problematic  online  poker  playing 
compared  to  non-problematic  online  poker  playing.  Considering  previous  research,  the 
negative  association  in  the  present  study  between  average  gambling  duration  and  self-
reported  problem  gambling  appears  contradictory.  However,  one  explanation  could  be 
that  those  with  self-reported  problem  gambling  might  already  have  attempted  to  con-
trol their gambling, and therefore had shorter average gambling sessions in the 30 days 
prior to completing the PGSI. This hypothesis is also supported by the higher percentage 
of self-exclusions among those self-reporting problem gambling, which is indicative of 
attempts to control or stop gambling.

---

<!-- PAGE 16 -->

996

International Journal of Mental Health and Addiction (2026) 24:981–1003

None  of  the  monetary  intensity  variables  contributed  significantly  to  the  model, 
which included demographic and behavioral metrics. This means that the total amount 
of  money  bet,  lost,  withdrawn,  and  deposited  did  not  improve  the  prediction  of  self-
reported problem gambling. To the best of the authors knowledge, the present study is 
the  first  that  has  predicted  self-reported  problem  gambling  using  a  hierarchical  mod-
eling  approach.  Only  one  previous  study  (Hopfgartner  et  al.,  2023)  applied  hierarchi-
cal logistic regressions to investigate behavioral patterns associated with voluntary self-
exclusions.  In  their  study,  the  authors  also  reported  that  monetary  intensity  variables 
did not significantly contribute to the model’s performance in most countries. The fact 
that the amount of money gambled did not significantly contribute to the prediction of 
self-reported  problem  gambling  in  the  present  study  also  supports  the  generalizability 
of  the  statistical  model  across  jurisdictions.  Income  levels  (and  therefore  expenditure) 
vary across countries, but a purely behavioral model is not affected by these variations.

Applying Machine Learning Models to Predict Self‑Reported Problem Gambling

Despite the improved performance of the models, which were trained on all three countries’s 
data, the models trained without one country’s data still showed a good performance indicating 
a weak generalization across countries. The slightly lower AUC values can be partly attributed 
to the nature of the target variable, which is self-reported and was determined using a threshold 
(i.e., considering a score of 8 or more as problem gambling), leading to skewness in the data. 
This aspect, coupled with the smaller number of Canadian participants in the dataset and its 
distinct characteristics compared to the other two countries (i.e., higher PGSI scores in Can-
ada), emphasizes the challenges in achieving higher ROC AUC values in such varied settings. 
Despite these constraints, the ability of these  models  to (weakly) generalize across countries 
and identify patterns of self-reported problem gambling is promising. This means that models 
which were not trained with data from a specific country still identified some of the patterns of 
self-reported problem gambling in the player-tracking data of that country. This robustness sug-
gests that while country-specific patterns enhance model performance, the underlying behav-
ioral  patterns  captured  by  the  machine  learning  models  were  sufficient  to  weakly  generalize 
across  countries  to  predict  self-reported  problem  gambling.  This  is,  for  example,  important 
regarding newly regulated jurisdictions, which might introduce legalized online gambling in the 
future. The general predictors of self-reported problem gambling, which were identified in the 
present study, appeared to be valid in all three jurisdictions. Nevertheless, future research can 
explore these possibilities on larger datasets and information from additional countries to isolate 
the common as well as diverging behavioral patterns across those countries.

Applications and Implications

The present study is important because it is one of the very few studies to integrate sub-
jective self-report data with objective account-based tracking data. Such a methodological 
approach  will  help  move  the  gambling  study  field  given  the  robustness  of  the  combined 
datasets. Such an approach can be used by both researchers and practitioners in the field, 
as well as by the gambling industry who often do their own internal approach. Importantly, 
the present study also (i) highlighted the benefits of using artificial intelligence in the study 
of  both  gambling  and  problem  gambling,  (ii)  identified  behavioral  markers  of  gambling 
harm (e.g., frequent monetary depositing within session, regular account depletion) which 
can be utilized by gambling operators (and enforced by regulators) to help them identify

---

<!-- PAGE 17 -->

International Journal of Mental Health and Addiction (2026) 24:981–1003

997

risky gambling and potential problem gamblers, and (iii) provided important implications 
for the development of responsible gambling tools and interventions. By highlighting the 
significance  of  behavioral  patterns,  such  as  frequent  in-session  monetary  depositing  and 
account depletion, the study contributes to the body of knowledge required for designing 
tailored responsible gambling strategies that can be adapted to diverse regulatory contexts. 
The  comprehensive  approach  used  in  the  present  study  could  serve  as  a  foundation  for 
future research in newly regulated or evolving online gambling markets.

Limitations and Future Research

While contributing valuable insights into the predictors of self-reported problem gambling, the 
present study is subject to specific limitations that must be acknowledged. One specific limita-
tion arises from the self-selection bias inherent in the dataset (Tripepi et al., 2010) because it 
only included data from gamblers who had voluntarily completed the PGSI. This self-selection 
bias is also visible in the disproportionately high rate of problem gamblers within the present 
sample compared to the rates reported in prevalence studies. More specifically, the present study 
identified self-reported problem gambling rates of 35.2% in Canada, 26.4% in Great Britain, 
and 28.9% in Spain, using the PGSI with a threshold of 8 or more for problem gambling. These 
rates were significantly higher than those reported in the respective national prevalence studies: 
0.6% in Canada (Williams et al., 2021), between 2.5% and 2.8% in Great Britain (Gambling 
Commission, 2023; Gunstone et al., 2022), and 0.72% in Spain (Chóliz et al., 2021). Individuals 
who choose to assess their gambling behaviors through the PGSI may already have concerns 
about their gambling habits, thereby skewing the sample towards higher rates of problem gam-
bling compared to a randomized or representative sample of the general gambling population. 
This bias must be considered when interpreting the results because it may influence the predic-
tive accuracy of the machine learning models used. Future studies would benefit from analyzing 
a more representative sample to provide a more comprehensive picture.

Secondly,  the  reliance  on  self-reported  data  in  determining  problem  gambling  sever-
ity presents another limitation, given the potential discrepancies between self-perceptions 
and actual gambling behaviors. The accuracy of self-reported data can be compromised by 
a  variety  of  factors,  including  memory  recall,  social  desirability  bias,  and  the  subjective 
nature of self-assessment tools (Auer et al., 2023; Schell et al., 2021). While the present 
study provides insights to the predictive factors of self-reported problem gambling, these 
limitations must be considered.

Third, another limitation to consider is the relatively small sample size of this study in 
comparison to other player-tracking studies. The reduction in sample size, primarily due to 
the data cleaning process where participants completing the PGSI in less than 1 min were 
excluded, can limit the statistical power of the study. This, in turn, can potentially affect the 
robustness and reliability of the findings (Button et al., 2013). However, it is equally impor-
tant to emphasize that the integrity and reliability of the data are of paramount importance. 
Including data from gamblers who were unlikely to have engaged seriously with the PGSI 
survey questions could have led to confounding and potentially misleading results, which 
could  affect  the  validity  of  the  study’s  findings.  The  significant  reduction  in  sample  size 
is therefore considered a limitation, but this decision was made to ensure the quality and 
reliability of the data. Furthermore, the imbalance between the proportions of gamblers in 
each country presents another limitation. Gambling behaviors can vary significantly across 
different regions and cultures, influenced by various factors such as legal regulations, soci-
etal  norms,  and  economic  conditions  (Raylu  &  Oei,  2004;  Selin,  2019).  Therefore,  the

---

<!-- PAGE 18 -->

998

International Journal of Mental Health and Addiction (2026) 24:981–1003

overrepresentation or underrepresentation of gamblers from specific countries can impact 
the study’s ability to generalize its findings.

Next, the use of a 30-day period for calculating gambling behavior prior to completing the 
PGSI represented a methodological decision that may have affected the results of the study. 
One  advantage  of  this  time  frame  is  that  it  captured  the  current  gambling  behavior  that  is 
likely to most influence participants’ responses to the PGSI, which is intended as an instru-
ment  to  reflect  gambling  behavior  over  the  past  year.  On  the  other  hand,  a  shorter  period 
does  not  account  for  long-term  behavioral  trends  and  fluctuations  in  gambling  that  can  be 
captured by a 12-month period, such as episodic gambling. However, a 12-month observation 
period can also lead to biases. For example, it is possible that players who scored high on the 
PGSI may have participated in gambling shortly before completing the PGSI, while players 
with lower scores may not have gambled recently. This temporal proximity could lead to an 
overestimation  of  problem  gambling  behavior  among  active  gamblers  and  an  underestima-
tion among less active gamblers, which in turn affects the accuracy of the model. The present 
study’s choice to rely on a 30-day observation period is therefore a compromise between the 
temporal relevance of the behavioral data and the risk of biasing the model by including less 
recent gambling activity. This trade-off should be considered in future research to match the 
observation period to the temporal scope of the PGSI.

Finally, several behavioral variables in the present study were not significantly associated with 
self-reported problem gambling. This highlights the multifaceted nature of gambling disorder, 
which encompasses not only behavioral aspects, but also psychological aspects. The PGSI incor-
porates indicators such as experiencing health problems and feelings of guilt, which are reflective 
of the psychological state of individuals with gambling disorders. These characteristics relate to 
cognitive aspects and the consequences of gambling, factors that are cannot be captured in player 
tracking data. Given this difference in the items of the PGSI between measurable behaviors and 
less measurable psychological criteria, this may be one explanation why only specific behaviors 
were significantly associated with self-reported problem gambling in the present study.

Future  research  should  aim  to  mitigate  these  limitations  and  explore  the  utility  of  the 
findings across a wider and more balanced array of gambling platforms and jurisdictions to 
improve the development of effective responsible gambling tools and interventions. Moreo-
ver, the machine learning models’ performance in predicting self-reported problem gam-
bling  across  countries  highlighted  the  potential  for  future  research  to  refine  and  enhance 
these predictive capabilities. Finally, replication studies with various operators and across 
different countries are needed. Such studies would provide greater insight into the gener-
alizability of the present findings and could potentially identify unique behavioral patterns 
that are specific to specific regions or gambling platforms.

Conclusions

The  present  study  provided  a  nuanced  understanding  of  the  predictors  of  self-reported 
problem  gambling,  emphasizing  the  importance  of  behavioral  variables  over  monetary 
variables. The findings support the hypothesis that self-reported problem gambling can be 
predicted  using  player-tracking  data,  independent  of  monetary  expenditure,  across  differ-
ent  countries.  Applying  machine  learning  models  to  predict  self-reported  problem  dem-
onstrated that the inclusion of country-specific data enhanced the predictive performance. 
Nevertheless, the robustness of the models without country-specific training data suggested 
the existence of universal behavioral patterns that cross cultural and regulatory boundaries.

---

<!-- PAGE 19 -->

International Journal of Mental Health and Addiction (2026) 24:981–1003

999

Appendices

Appendix 1    Problem  Gambling  Severity  Index  items.  Individuals  can  answer:  never  (0),  sometimes  (1), 
most of the time (2), and almost always (3). A score of 8 + indicates problem gambling

Item number and question

(1) Have you bet more than you could really afford to lose?

(2) Have you needed to gamble with larger amounts of money to get the same excitement?
(3) Have you gone back to try to win to back the money you’d lost?
(4) Have you borrowed money or sold anything to get money to gamble?
(5) Have you felt that you might have a problem with gambling?
(6) Have you felt that gambling has caused you any health problems, including stress or anxiety
(7) Have people criticized your betting, or told you that you have a gambling problem, whether or not you

thought it is true?

(8) Have you felt your gambling has caused financial problems for you or your household?
(9) Have you felt guilty about the way you gamble or what happens when you gamble?

Appendix 2    Player tracking features based on the thirty days before answering the PGSI

Demographics

Behavioral features

Monetary features

Amount of money bet

Amount of money deposited
Amount of money lost
Amount of money withdrawn

Country

Age (in years)
Gender

Number of self-exclusions

Number of voluntary limit changes
Number of withdrawals
Standard deviation of withdrawals
Number of failed deposits
Standard deviation of bets
Number of different game types played
Number of different payment methods
Average session length (in minutes)
Average number of deposits per session
Percent of bet at night
Percent of sessions at night
Percent of sessions on weekends
Percent of bet on weekends
Percent of sessions ending with low account bal-

ance (Account depletion)

Percent of loss at night

---

<!-- PAGE 20 -->

1000

International Journal of Mental Health and Addiction (2026) 24:981–1003

Authors’ Contribution  All authors contributed to the preparation of this manuscript.

Funding  Not applicable.

Data Availability  The data for this study are not available due to commercial sensitivity.

Declarations

Ethics  This study was performed in line with the principles of the Declaration of Helsinki and was approved 
by the research team’s university ethic committees.

Conflict of Interest  The last author has received research funding from Norsk Tipping (the gambling operator 
owned by the Norwegian government). The last author has also received funding for a number of research 
projects in the area of gambling education for young people, social responsibility in gambling and gambling 
treatment  from  Gamble  Aware  (formerly  the  Responsibility  in  Gambling  Trust),  a  charitable  body  which 
funds its research program based on donations from the gambling industry. The first, second and last authors 
undertake consultancy for various gaming companies in the area of social responsibility in gambling.

Open  Access  This  article  is  licensed  under  a  Creative  Commons  Attribution  4.0  International  License, 
which  permits  use,  sharing,  adaptation,  distribution  and  reproduction  in  any  medium  or  format,  as  long 
as you give appropriate credit to the original author(s) and the source, provide a link to the Creative Com-
mons licence, and indicate if changes were made. The images or other  third party material in this article 
are  included  in  the  article’s  Creative  Commons  licence,  unless  indicated  otherwise  in  a  credit  line  to  the 
material. If material is not included in the article’s Creative Commons licence and your intended use is not 
permitted by statutory regulation or exceeds the permitted use, you will need to obtain permission directly 
from the copyright holder. To view a copy of this licence, visit http://creativecommons.org/licenses/by/4.0/.

References

Abbott, M. W., Romild, U., & Volberg, R. A. (2014). Gambling and problem gambling in Sweden: Changes

between 1998 and 2009. Journal of Gambling Studies, 30(4), 985–999.

Andrade, M., Sharman, S., Xiao, L. Y., & Newall, P. W. (2023). Safer gambling and consumer protection 
failings among 40 frequently visited cryptocurrency-based online gambling operators. Psychology of 
Addictive Behaviors, 37(3), 545–557.

Andrews, J. L., Ahmed, S. P., & Blakemore, S. J. (2021). Navigating the social environment in adolescence:

The role of social brain development. Biological Psychiatry, 89(2), 109–118.

Auer, M., Griffiths, M.D. (2023b). Predicting high-risk gambling based on the first seven days of gambling 
activity  after  registration  using  account-based  tracking  data.  International  Journal  of  Mental  Health 
and Addiction. Advance online publication. https:// doi. org/ 10. 1007/ s11469- 023- 01056-4

Auer, M., Hopfgartner, N., Helic, D., & Griffiths, M. D. (2023). Self-reported deposits versus actual depos-
its in online gambling: An empirical study. Journal of Gambling Studies. Advance online publication. 
https:// doi. org/ 10. 1007/ s10899- 023- 10230-1

Auer, M., & Griffiths, M. D. (2023a). Using artificial intelligence algorithms to predict self-reported prob-
lem gambling with account-based player data in an online casino setting. Journal of Gambling Studies, 
39(3), 1273–1294.

Auer,  M.,  &  Griffiths,  M.  D.  (2023c).  An  empirical  attempt  to  operationalize  chasing  losses  in  gambling

utilizing account-based player tracking data. Journal of Gambling Studies, 39(4), 1547–1561.

Auer,  M.,  &  Griffiths,  M.  D.  (2023d).  The  relationship  between  structural  characteristics  and  gambling 
behaviour: An online gambling player tracking study. Journal of Gambling Studies, 39(1), 265–279.
Auer, M., & Griffiths, M. D. (2023e). Attitude towards deposit limits and relationship with their account-based 
data among a sample of German online slots players. Journal of Gambling Studies, 39(3), 1319–1336.
Barrault, S., & Varescon, I. (2013). Cognitive distortions, anxiety, and depression among regular and pathologi-
cal gambling online poker players. Cyberpsychology, Behavior and Social Networking, 16(3), 183–188.
Blaszczynski, A., & Nower, L. (2010). Instrumental tool or drug: Relationship between attitudes to money

and problem gambling. Addiction Research & Theory, 18(6), 681–691.

---

<!-- PAGE 21 -->

International Journal of Mental Health and Addiction (2026) 24:981–1003

1001

Button, K. S., Ioannidis, J. P. A., Mokrysz, C., Nosek, B. A., Flint, J., Robinson, E. S. J., & Munafò, M. 
R.  (2013).  Power  failure:  Why  small  sample  size  undermines  the  reliability  of  neuroscience.  Nature 
Reviews Neuroscience, 14(5), 365–376. https:// doi. org/ 10. 1038/ nrn34 75

Catania,  M.,  &  Griffiths,  M.  D.  (2021).  Understanding  online  voluntary  self-exclusion  in  gambling:  An 
empirical study using account-based behavioral tracking data. International Journal of Environmental 
Research and Public Health, 18(4), 2000.

Catania, M., & Griffiths, M. D. (2023). Analyzing consumer protection for gamblers across different online 
gambling operators: A replication study. International Journal of Mental Health and Addiction, 21(3), 
1882–1897.

Chóliz, M. (2016). The challenge of online gambling: The effect of legalization on the increase in online

gambling addiction. Journal of Gambling Studies, 32(2), 749–756.

Chóliz, M., Marcos, M., & Lázaro-Mateo, J. (2021). The risk of online gambling: A study of gambling disor-
der prevalence rates in Spain. International Journal of Mental Health and Addiction, 19, 404–417.
Dowling, N. A., Merkouris, S. S., Manning, V., Volberg, R., Lee, S. J., Rodda, S. N., & Lubman, D. I. 
(2018). Screening for problem gambling within mental health services: A comparison of the clas-
sification accuracy of brief instruments. Addiction, 113(6), 1088–1104.

Ekholm,  O.,  Eiberg,  S.,  Davidsen,  M.,  Holst,  M.,  Larsen,  C.  V.,  &  Juel,  K.  (2014).  The  prevalence  of 
problem gambling in Denmark in 2005 and 2010: A sociodemographic and socioeconomic charac-
terization. Journal of Gambling Studies, 30, 1–10.

Elton-Marshall,  T.,  Leatherdale,  S.  T.,  &  Turner,  N.  E.  (2016).  An  examination  of  internet  and  land-
based gambling among adolescents in three Canadian provinces: Results from the youth gambling 
survey (YGS). BMC Public Health, 16(1), 277.

Ferris, J., & Wynne, H. J. (2001). The Canadian Problem Gambling Index: Final report. Canadian Cen-

tre on Substance Abuse.

Finkenwirth,  S.,  MacDonald,  K.,  Deng,  X.,  Lesch,  T.,  &  Clark,  L.  (2021).  Using  machine  learning  to 
predict self-exclusion status in online gamblers on the PlayNow.com platform in British Columbia. 
International Gambling Studies, 21(2), 220–237.

Gambling  Commission  (2023).  Statistics  on  participation  and  problem  gambling.  https:// www. gambl 
ingco mmiss ion. gov. uk/ stati stics- and- resea rch/ publi cation/ gambl ing- parti cipat ion- and- the- preva 
lence- of- probl em- gambl ing- survey- final

Gambling Commission (2022a). £1.17m fine for marketing to vulnerable consumers. https:// www. gambl

ingco mmiss ion. gov. uk/ news/ artic le/ gbp1- 17m- fine- for- marke ting- to- vulne rable- consu mers

Gambling Commission (2022b). £9.4m fine for online operator 888. https:// www. gambl ingco mmiss ion.

gov. uk/ news/ artic le/ gbp9- 4m- fine- for- online- opera tor- 888

Gebauer,  L.,  LaBrie,  R.,  &  Shaffer,  H.  J.  (2010).  Optimizing  DSM-IV-TR  classification  accuracy:  A 
brief  biosocial  screen  for  detecting  current  gambling  disorders  among  gamblers  in  the  general 
household population. Canadian Journal of Psychiatry, 55(2), 82–90.

Gelman, A., & Hill, J. (2006). Data analysis using regression and multilevel/hierarchical models. Cam-

bridge University Press.

Griffiths, M. D., & Auer, M. (2016). Should voluntary “self-exclusion” by gamblers be used as a proxy

measure for problem gambling? Addiction Medicine & Therapy, 2(2), 31–33.

Griffiths, M. D., & Parke, J. (2002). The social impact of internet gambling. Social Science Computer

Review, 20(3), 312–320.

Gunstone, B., Gosschalk, K., Zabicka, E., & Sullivan-Drage, C. (2022). Annual GB Treatment and Sup-
port  Survey  2021.  https:// www. begam bleaw are. org/ sites/ defau lt/ files/ 2022- 03/ Annual% 20GB% 
20Tre atment% 20and% 20Sup port% 20Sur vey% 20Rep ort% 202021% 20% 28FIN AL% 29. pdf

Gupta, R., Nower, L., Derevensky, J. L., Blaszczynski, A., Faregh, N., & Temcheff, C. (2013). Problem 
gambling  in  adolescents:  An  examination  of  the  pathways  model.  Journal  of  Gambling  Studies, 
29(3), 575–588.

Haeusler, J. (2016). Follow the money: Using payment behaviour as predictor for future self-exclusion.

International Gambling Studies, 16(2), 246–262.

Hancock, L., Schellinck, T., & Schrans, T. (2008). Gambling and corporate social responsibility (CSR): 
Re-defining industry and state roles on duty of care, host responsibility and risk management. Pol-
icy and Society, 27(1), 55–68.

Hing, N., Russell, A. M., & Browne, M. (2017). Risk factors for gambling problems on online electronic

gaming machines, race betting and sports betting. Frontiers in Psychology, 8, 779.

Hing, N., Russell, A. M., Black, A., Rockloff, M., Browne, M., Rawat, V., & Woo, L. (2022). Gambling 
prevalence  and  gambling  problems  amongst  land-based-only,  online-only  and  mixed-mode  gam-
blers in Australia: A national study. Computers in Human Behavior, 132, 107269.

---

<!-- PAGE 22 -->

1002

International Journal of Mental Health and Addiction (2026) 24:981–1003

Holden,  J.  T.,  &  Edelman,  M.  (2020).  A  short  treatise  on  sports  gambling  and  the  law:  How  America

regulates its most lucrative vice. Wisconsin Law Review, 907, 907–974.

Holtgraves, T. (2008). Evaluating the Problem Gambling Severity Index. Journal of Gambling Studies,

25(1), 105–120.

Hopfgartner, N., Auer, M., Griffiths, M. D., & Helic, D. (2023). Predicting self-exclusion among online

gamblers: An empirical real-world study. Journal of Gambling Studies, 39(1), 447–465.

Hopley, A. A., & Nicki, R. M. (2010). Predictive factors of excessive online poker playing. Cyberpsy-

chology, Behavior and Social Networking, 13(4), 379–385.

Icenogle, G., Steinberg, L., Duell, N., Chein, J., Chang, L., Chaudhary, N., & Bacchini, D. (2019). Ado-
lescents’ cognitive capacity reaches adult levels prior to their psychosocial maturity: Evidence for a 
“maturity gap” in a multinational, cross-sectional sample. Law and Human Behavior, 43(1), 69–85.
James,  G.,  Witten,  D.,  Hastie,  T.,  &  Tibshirani,  R.  (2013).  An  introduction  to  statistical  learning.

Springer.

Kun, B., Balázs, H., Arnold, P., Paksi, B., & Demetrovics, Z. (2012). Gambling in western and eastern

Europe: The example of Hungary. Journal of Gambling Studies, 28, 27–46.

Lin, E. Y. J., Casswell, S., Easton, B., Huckle, T., Asiasiga, L., & You, R. Q. (2010). Time and money 
spent  gambling  and  the  relationship  with  quality-of-life  measures:  A  national  study  of  New  Zea-
landers. Journal of Gambling Issues, 24, 33–53.

Louderback,  E.  R.,  LaPlante,  D.  A.,  Currie,  S.  R.,  &  Nelson,  S.  E.  (2021).  Developing  and  validating 
lower risk online gambling thresholds with actual bettor data from a major internet gambling opera-
tor. Psychology of Addictive Behaviors, 35(8), 921–938.

Luquiens, A., Tanguy, M. L., Benyamina, A., Lagadec, M., Aubin, H. J., & Reynaud, M. (2016). Track-
ing  online  poker  problem  gamblers  with  player  account-based  gambling  data  only.  International 
Journal of Methods in Psychiatric Research, 25(4), 333–342.

Mora-Salgueiro, J., García-Estela, A., Hogg, B., Angarita-Osorio, N., Amann, B. L., Carlbring, P., Jiménez-
Murcia,  S.,  Pérez-Sola,  V.,  &  Colom,  F.  (2021).  The  prevalence  and  clinical  and  sociodemographic 
factors of problem online gambling: A systematic review. Journal of Gambling Studies, 37, 899–926.

Murch,  W.  S.,  Kairouz,  S.,  Dauphinais,  S.,  Picard,  E.,  Costes,  J.  M.,  &  French,  M.  (2023).  Using 
machine learning to retrospectively predict self-reported gambling problems in Quebec. Addiction, 
118(8), 1569–1578.

Nagelkerke, N. J. (1991). A note on a general definition of the coefficient of determination. Biometrika,

78(3), 691–692.

Nower,  L.,  &  Blaszczynski,  A.  (2006a).  Characteristics  and  gender  differences  among  self-excluded

casino problem gamblers: Missouri data. Journal of Gambling Studies, 22, 81–99.

Nower,  L.,  &  Blaszczynski,  A.  (2006b).  Impulsivity  and  pathological  gambling:  A  descriptive  model.

International Gambling Studies, 6(1), 61–75.

Pedregosa, F., Varoquaux, G., Gramfort, A., Michel, V., Thirion, B., Grisel, O., & Duchesnay, E. (2011).

Scikit-learn: Machine learning in Python. Journal of Machine Learning Research, 12, 2825–2830.
Percy,  C.,  França,  M.,  Dragičević,  S.,  &  d’Avila  Garcez,  A.  (2016).  Predicting  online  gambling  self-
exclusion:  An  analysis  of  the  performance  of  supervised  machine  learning  models.  International 
Gambling Studies, 16(2), 193–210.

Perrot, B., Hardouin, J. B., Thiabaud, E., Saillard, A., Grall-Bronnec, M., & Challet-Bouju, G. (2022). 
Development and validation of a prediction model for online gambling problems based on players’ 
account data. Journal of Behavioral Addictions, 11(3), 874–889.

Raylu, N., & Oei, T. P. (2004). Role of culture in gambling and problem gambling. Clinical Psychology

Review, 23(8), 1087–1114.

Schell,  C.,  Godinho,  A.,  &  Cunningham,  J.  A.  (2021).  Examining  change  in  self-reported  gambling 
measures over time as related to socially desirable responding bias. Journal of Gambling Studies, 
37(3), 1043–1054.

Secades-Villa,  R.,  Martínez-Loredo,  V.,  Grande-Gosende,  A.,  &  Fernández-Hermida,  J.  (2016).  The  rela-
tionship between impulsivity and problem gambling in adolescence. Frontiers in Psychology, 7, 1931.
Selin,  J.  (2019).  National  gambling  policies  and  the  containment  of  the  EU’s  politico-legal  influence.

Nordic Studies on Alcohol and Drugs, 36(2), 77–90.

Siemens, J. C., & Kopp, S. W. (2011). The influence of online gambling environments on self-control.

Journal of Public Policy & Marketing, 30(2), 279–293.

Tabri, N., Xuereb, S., Cringle, N., & Clark, L. (2022). Associations between financial gambling motives, 
gambling  frequency  and  level  of  problem  gambling:  A  meta-analytic  review.  Addiction,  117(3), 
559–569.

---

<!-- PAGE 23 -->

International Journal of Mental Health and Addiction (2026) 24:981–1003

1003

Tomei, A., Tichelli, E., Ewering, N., Nunweiler-Hardegger, S., & Simon, O. (2015). A descriptive study 
of  gambling  among  emerging  adult  males  in  French-speaking  Switzerland.  Journal  of  Gambling 
Studies, 31(3), 607–620.

Tomei,  A.,  Petrovic,  G.,  &  Simon,  O.  (2022).  Offline  and  online  gambling  in  a  Swiss  emerging-adult

male population. Journal of Gambling Studies, 38(4), 1215–1228.

Tripepi,  G.,  Jager,  K.  J.,  Dekker,  F.  W.,  &  Zoccali,  C.  (2010).  Selection  bias  and  information  bias  in

clinical research. Nephron Clinical Practice, 115(2), c94–c99.

Turner, N. E., Jain, U., Spence, W., & Zangeneh, M. (2008). Pathways to pathological gambling: Com-
ponent  analysis  of  variables  related  to  pathological  gambling.  International  Gambling  Studies, 
8(3), 281–298.

Williams, R. J., Connolly, D., Wood, R. T., & Nowatzki, N. R. (2006). Gambling and problem gambling in a

sample of university students. Journal of Gambling Issues, 16, 1–14.

Williams, R. J., Leonard, C. A., Belanger, Y. D., Christensen, D. R., El-Guebaly, N., Hodgins, D. C., & Ste-
vens, R. M. (2021). Gambling and problem gambling in Canada in 2018: Prevalence and changes since 
2002. Canadian Journal of Psychiatry, 66(5), 485–494.

Zaykin, D. V. (2011). Optimally weighted Z-test is a powerful method for combining probabilities in meta-

analysis. Journal of Evolutionary Biology, 24(8), 1836–1841.

Publisher’s Note  Springer Nature remains neutral with regard to jurisdictional claims in published maps and 
institutional affiliations.

Authors and Affiliations

Niklas Hopfgartner1 · Michael Auer1 · Denis Helic2 · Mark D. Griffiths3

*  Mark D. Griffiths 
  mark.griffiths@ntu.ac.uk

Niklas Hopfgartner 
n.hopfgartner@neccton.com

Michael Auer 
  m.auer@neccton.com

Denis Helic 
dhelic@tugraz.at

1  Neccton GmbH, Davidgasse 5, 7052 Müllendorf, Austria
2

Institute of Interactive Systems and Data Science, Graz University of Technology, Sandgasse 
36/III, 8010 Graz, Austria

3

International Gaming Research Unit, Psychology Department, Nottingham Trent University, 50 
Shakespeare Street, Nottingham NG1 4FQ, UK

<!-- MARKITDOWN CONVERSION -->

<!-- Full MarkItDown conversion for formatting fidelity. -->

International Journal of Mental Health and Addiction (2026) 24:981–1003
https://doi.org/10.1007/s11469-024-01312-1
ORIGINAL ARTICLE
Using Artificial Intelligence Algorithms to Predict
Self‑Reported Problem Gambling Among Online Casino
Gamblers from Different Countries Using Account‑Based
Player Data
Niklas Hopfgartner1 · Michael Auer1 · Denis Helic2 · Mark D. Griffiths3
Accepted: 22 April 2024 / Published online: 7 May 2024
© The Author(s) 2024
Abstract
The prevalence of online gambling and the potential for related harm necessitate predic-
tive models for early detection of problem gambling. The present study expands upon prior
research by incorporating a cross-country approach to predict self-reported problem gam-
bling using player-tracking data in an online casino setting. Utilizing a secondary data-
set comprising 1743 British, Canadian, and Spanish online casino gamblers (39% female;
mean age = 42.4 years; 27.4% scoring 8 + on the Problem Gambling Severity Index), the
present study examined the association between demographic, behavioral, and monetary
intensity variables with self-reported problem gambling, employing a hierarchical logis-
tic regression model. The study also tested the efficacy of five different machine learning
models to predict self-reported problem gambling among online casino gamblers from dif-
ferent countries. The findings indicated that behavioral variables, such as taking self-exclu-
sions, frequent in-session monetary depositing, and account depletion, were paramount in
predicting self-reported problem gambling over monetary intensity variables. The study
also demonstrated that while machine learning models can effectively predict problem
gambling across different countries without country-specific training data, incorporating
such data improved the overall model performance. This suggests that specific behavioral
patterns are universal, yet nuanced differences across countries exist that can improve pre-
diction models.
Keywords Responsible gambling · Responsible gambling tools · Problem gambling ·
Problem Gambling Severity Index · PGSI · Machine learning · Artificial intelligence
Introduction
Online gambling involves an activity where money is wagered on the internet and can
involve a wide variety of games (e.g., sports betting, poker, slots, and lotto). Such gam-
bling can take place on personal computers, smartphones, or any other device which is
connected to the internet. Over the past decade, online gambling has become more popular
and widespread, leading to diverse regulatory landscapes across different countries (Selin,
Extended author information available on the last page of the article
1 3
Vol.:(0123456789)

982 International Journal of Mental Health and Addiction (2026) 24:981–1003
2019). For example, in the United States, the regulatory framework differentiates between
online sports betting and online casino gambling, commonly known as iGaming (Holden &
Edelman, 2020). These frameworks are crucial not only for regulating the industry, but also
for monitoring how the increasing accessibility of online gambling affects the prevalence
of problem gambling.
Prevalence of Problem Gambling Among Online Gamblers
As the present study investigated self-reported problem gambling of online gamblers
across different countries, this section highlights recent research regarding the prevalence
of problem gambling among these populations. Several studies have reported a higher risk
prevalence of problem gambling among online gamblers (e.g., Chóliz, 2016; Elton-Mar-
shall et al., 2016; Hing et al., 2017). Hing et al. (2022) compared land-based-only gamblers
(LBOGs), online-only gamblers (OOGs), and mixed-mode gamblers (MMGs), using data
from a 2019 Australian national telephone survey (N = 15,000). MMGs had the highest
gambling involvement, gambling problems, and gambling-related harm. Relative risk of
gambling problems for MMGs exceeded that of both LBOGs and OOGs. The study found
that engaging in more gambling forms, being male, being single, being less educated,
being indigenous, and speaking a non-English language increased the risk of problem
gambling. Gambling on the internet (OOGs and MMGs combined) was associated with a
higher problem gambling severity than land-based-only gambling.
Mora-Salgueiro et al. (2021) conducted a meta-study of prevalence, comorbidities,
and/or demographics of online disordered gambling using studies in the Medline data-
base. There was a large variation in the prevalence of problem gambling (2.7% to 20.3%)
reported by the selected studies. Prevalence rates of at-risk and disordered gambling among
adolescents ranged from 5.7% to 57.52%. Being male and single were the most common
risk factors among online gamblers with disordered gambling.
Tomei et al. (2022) collected survey responses from 1869 young males in Switzerland
about offline and online gambling behaviors, as well as the severity of problem gambling.
Compared to a previous study (Tomei et al., 2015), which reported that 16% of the partici-
pants gambled online during the past 12 months, Tomei et al. (2022) reported that 24% of
participants gambled online. Moreover, 70% of online gamblers reported using the smart-
phone to access internet gambling sites. The study also found that compared to those with-
out gambling problems, those at-risk and those with gambling problems had higher preva-
lence rates of online gambling. The proportion of those at-risk or with gambling problems
was approximately twice of those without problems among online-only gamblers.
The Use of Account‑Based Data in Problem Gambling Research
Online gambling operators record every bet, win, deposit, and withdrawal, and therefore
have objective data concerning each player’s money and time expenditure, as well as data
on every game played. For two decades, researchers have emphasized the potential of
player tracking as a method of detecting problematic gambling in online gambling settings
(Catania & Griffiths, 2021; Finkenwirth et al., 2021; Griffiths & Parke, 2002; Haeusler,
2016; Hancock et al., 2008). One way of assessing problem gambling among online gam-
blers is for operators to collect responses to a problem gambling screen from a sample of
their gamblers. However, this involves substantial effort. Therefore, researchers frequently
1 3

International Journal of Mental Health and Addiction (2026) 24:981–1003 983
use voluntary self-exclusion as a proxy measure for problem gambling as it is always
recorded and readily available for analysis.
A number of studies have used voluntary self-exclusion as a proxy measure for problem
gambling (Hopfgartner et al., 2023; Nower & Blaszczynski, 2006a; Percy et al., 2016).
The underlying assumption is that gamblers who voluntarily self-exclude are problem gam-
blers. An algorithm that detects gambling patterns which precede voluntary self-exclusion
could then be used to identify problem gamblers. This would then allow gambling opera-
tors to interact with these players. Self-exclusion is a very common responsible gaming
tool, and most regulated markets require licensed online gambling operators to offer vol-
untary self-exclusion (Catania & Griffiths, 2023). This might also be a reason for the rela-
tively large number of studies which have used voluntary self-exclusion as a proxy measure
for problem gambling. Moreover, a few studies have used machine learning algorithms to
analyze correlations between voluntary self-exclusion and preceding gambling behavior
using player-tracking data (e.g., Finkenwirth et al., 2021; Hopfgartner et al., 2023).
Finkenwirth et al. (2021) used 20 variables, including gambling frequency, intensity,
and variability to predict self-exclusion using player-tracking data. The study found that the
variability in the amount of money wagered per session was the most important predictor
of self-exclusion. This variable captured betting patterns with significant fluctuations in
bet amounts, indicative of problematic gambling behaviors (e.g., loss chasing). The second
most important predictor was the number of bets per day. The performance of the machine
learning models varied between 65% and 76%, demonstrating the efficacy of player-track-
ing data in identifying individuals who might experience problem gambling.
Hopfgartner et al. (2023) applied hierarchal regressions using behavioral and monetary
metrics. In the first step, behavioral variables, such as the type of payment method, fre-
quency of deposits, session length, and number of game types, were used. In the second step,
monetary metrics, such as the amount of money lost, deposited, or withdrawn, were added.
Interestingly, very few of the monetary metrics significantly improved the model quality.
The same study also reported that the number of voluntary limit changes, previous volun-
tary self-exclusions, number of deposits per session, number of different payment methods,
and playing multiple types of games were predictive of future voluntary self-exclusion. The
fact that the monetary variables were less important could reflect differences in the financial
backgrounds of individual gamblers. For some gamblers, spending $1000 a month might be
easily affordable whereas for others, spending just $100 per month might not be affordable.
Griffiths and Auer (2016) have argued that there can be some issues when voluntary
self-exclusion is used as a proxy measure for problem gambling in player tracking studies.
This is because not all gamblers who self-exclude are problem gamblers and not all prob-
lem gamblers self-exclude. After analyzing a sample of 7732 gamblers who voluntarily
self-excluded in a 90-day period, Catania and Griffiths (2021) concluded that this group
was heterogeneous and therefore not a reliable proxy measure for problem gambling. More
specifically, 19% of the gamblers played for less than 24 h before self-excluding and 50%
of the gamblers played for less than a week before self-excluding. These findings suggested
that gamblers were self-excluding for reasons other than problem gambling.
Combining Self‑Reported Problem Gambling and Player‑Tracking Data
Given that voluntary self-exclusion among online gamblers is a sub-optimal proxy meas-
ure of problem gambling, responses to standardized questionnaires on problem gambling
have to be collected. The correlation between actual player-tracking data and self-reported
1 3

984 International Journal of Mental Health and Addiction (2026) 24:981–1003
gambling behavior can provide insight into the behavioral predictors of self-reported prob-
lem gambling. Five player tacking studies have used self-reported problem gambling to
predict problem gambling using player-tracking data (Auer & Griffiths, 2023a; Louderback
et al., 2021; Luquiens et al., 2016; Murch et al., 2023; Perrot et al., 2022). All five stud-
ies collected self-reported problem gambling data using a problem gambling screen (e.g.,
PGSI, Ferris & Wynne, 2001) and correlated the self-report results with objective player
tracking data. The resulting statistical models predicted the likelihood of a player being a
self-reported problem gambler.
Murch et al. (2023) had access to the responses of the PGSI from 9145 adults (aged
18 + years) who played on lotoquebec.com. The website offers lottery, casino, and sports-
betting products. The player-tracking data included time and money expenditure as well as
responsible gambling (RG) tool use for the 12 months preceding the completion of the PGSI
(using a 5 + score to indicate at-risk gambling and 8 + to indicate problem gambling). The
final model retained 10 explanatory variables, including younger age and repeated deposit-
ing over a weekly period following a bet. The other significant variables were based on the
amount of money bet and amount withdrawn. However, they did not examine any session
explanatory variables which were based on gambling sessions. Their overall model had an
area under the curve (AUC) of 84%. Although this was an impressive finding, it could also
have been the result of a large number of inactive players in the final sample. More specifi-
cally, gamblers only needed to have at least one bet in the 12 months preceding the comple-
tion of the PGSI. Players with high PGSI scores most likely gambled shortly before answer-
ing questions on the PGSI, and players with low PGSI scores most likely gambled very little
or not at all in the weeks before completing the PGSI. This means that any activity before
completing the PGSI most likely contributed largely to the high model accuracy.
Perrot et al. (2022) collected PGSI responses from 8172 French online sports bettors
and poker players, as well as 5404 online scratch-card and lottery players. Like Murch
et al. (2023), they used the same PGSI scoring. The AUC values which reflect model
quality were 83% and 74% for the two samples. Player-tracking features (e.g., amount of
money lost, deposited, wagered, gambling days, and number of bets) were computed for
the 4 months preceding the PGSI completion, and only participants who showed any gam-
bling activity in the 30 days before were included. Chasing losses was operationalized as
“making three deposits in less than 12 h” or “making a deposit less than 1 h after placing a
bet” (Perrot et al., 2022, p. 3). Perrot et al. argued that a repeated sequence of deposits or a
deposit that quickly followed a bet may reflect cases where gamblers lose all the remaining
money on their account, and then try to recover the losses by depositing money. However,
Perrot et al.’s study did not include online casino gamblers because it was limited to sports
bettors, poker players, and lottery players. Casino games typically possess a much higher
event frequency, which influences amount of money wagered, amount of money won, as
well as the amount of time spent gambling (Auer & Griffiths, 2023d). Therefore, the results
cannot be generalized to online casino gamblers.
Luquiens et al. (2016) developed predictive machine learning models based on PGSI
responses from 14,261 online poker players. Explanatory variables were computed for
the 30 days preceding the completion of the PGSI (using a PGSI score of 5 + for prob-
lem gambling). The risk factors of problem gambling reported by the predictive model
were being male, being “compulsive” (i.e., defined by having at least three deposits in
a 12-h period), being younger than 28 years, making a monetary deposit in the 30 days
before completing the PGSI, having a mean loss per gambling session > €1.7, losing a
total of > €45 in the last 30 days, having a total stake > €298 in the 30 days before com-
pleting the PGSI, having > 60 gambling sessions in the past 30 days, and multi-tabling.
1 3

International Journal of Mental Health and Addiction (2026) 24:981–1003 985
The model quality using the AUC was 72%. However, Luquiens et al.’s study was based
on data from online poker players. Given that poker possesses different structural char-
acteristics to other forms of gambling, the findings might not be valid for online casino
gamblers (Auer & Griffiths, 2023d).
Louderback et al. (2021) identified low-risk gambling thresholds based on a sample
of 1772 online casino gamblers who completed the Brief Biosocial Gambling Screen
(BBGS; Gebauer et al., 2010). The BBGS comprises three items which can be answered
“yes” or “no.” Answering any item ’yes’ was considered as an indication for problem
gambling. They concluded that a high likelihood of self-reported problem gambling
was indicated by wagering €167.97 or more each month, spending more than 6.71%
of annual income on online gambling wagers, losing €26.11 or more per month, and
demonstrating variability (i.e., standard deviation) in daily amount wagered of €35.14 or
more over a 1-month period. In contrast to Murch et al. (2023), Perrot et al. (2022), and
Luquiens et al. (2016), Louderback et al. used the BBGS to assess problem gambling
among a sample of online gamblers. Dowling et al. (2018) reported that the BBGS ade-
quately detects both problem and moderate-risk, but not low-risk, gambling. Moreover,
Auer and Griffiths (2023e) did not find significant correlations between responses to the
BBGS and player-tracking data in a sample of 1000 online slot gamblers.
Auer and Griffiths (2023a) were given access to the raw data of 1287 players from a
European online gambling casino who answered questions on the PGSI. They used the
player tracking data 30 days before completion of the PGSI (using 8 + for problem gam-
bling) to train machine learning models. They found that self-reported problem gamblers
lost less money, deposited less money, and bet on fewer days compared to non-problem
gamblers in the 30 days before answering the PGSI. However, self-reported problem gam-
blers self-excluded more often than non-problem gamblers during the 30 days before,
which might explain the lower overall activity. Self-reported problem gamblers lost more
money per gambling day, lost more money per gambling session, and deposited money
more frequently per gambling session. Problem gamblers also tended to deplete their gam-
bling accounts more frequently compared to non-problem gamblers. Auer and Griffiths
(2023a) also recommended that online gambling operators should make depositing more
than once per day more difficult to prevent players from chasing their losses. However,
Auer and Griffiths did not analyze country-specific differences regarding the association
between self-reported problem gambling and player-tracking data.
The Present Study
Several European countries (e.g., UK, Germany, Spain, Sweden, Denmark) as well as
the province of Ontario in Canada require online gambling operators to assess the risk of
problem gambling among their players. However, as aforementioned, the body of research
which has correlated self-reported problem gambling with objective gambling behavior
is limited (i.e., Auer & Griffiths, 2023a; Louderback et al., 2021; Luquiens et al., 2016;
Murch et al., 2023; Perrot et al., 2022). Therefore, the present study attempted to increase
the knowledge concerning the association between gambling behavior at an online casino
and self-reported problem gambling. To do so, the study utilized a secondary dataset with
gamblers from three different countries (i.e., Canada, Great Britain, and Spain). The pre-
sent study investigated the following three research questions (RQs):
1 3

986 International Journal of Mental Health and Addiction (2026) 24:981–1003
1. What type of account-based tracking behavior correlates with self-reported problem
gambling? (RQ1)
2. Can self-reported problem gambling be explained by behavioral variables independent
of the actual amount of money spent? (RQ2)
3. Can machine learning models predict self-reported problem gambling across gamblers
from three countries? (RQ3)
These research questions aimed to evaluate whether behavioral variables such as
the number of deposits per session, the number of payment accounts, or the number
of failed deposits were sufficient to predict self-reported problem gambling across
online casino gamblers from different countries. This reasoning is because Auer and
Griffiths (2023b) predicted high-risk gambling based on the first 7 days of behavior
after registration, and found that behavioral variables were responsible for a larger part
of model accuracy compared to monetary intensity variables. Therefore, the present
study extended previous lines of research by comparing player-tracking data with self-
reported problem gambling among players from three different countries to assess the
importance of monetary features in identifying self-reported problem gambling. The
advantage of using behavioral variables to predict problem gambling is their greater
generalizability. Income levels vary across countries, which lead to deviations in mon-
etary measures such as amount of money bet, won, deposited, and withdrawn, impair-
ing the accuracy of prediction models. On the other hand, metrics such as the number
of deposits, the number of gambling days, and gambling during the night are independ-
ent of income levels, leading to more robust and generalizable statistical models.
Additionally, the present study tested the generalizability of machine learning mod-
els to predict self-reported problem gambling among players from different countries.
It is important to understand whether such models developed in specific countries can
be effectively applied to players from other countries. Such data would likely provide
valuable insights into the development of universally applicable responsible gambling
tools and policies.
Method
The authors were given access to a secondary dataset comprising British, Canadian,
and Spanish online casino gamblers playing a variety of casino games (e.g., slots, rou-
lette, and blackjack) who completed the nine PGSI questions between January 2022
and November 2023. If the PGSI was competed more than once, only the most recent
answers were used. The nine PGSI questions are listed in Appendix 1. For each gam-
bler, the raw data 30 days before completing the PGSI were available. Every bet, win,
deposit, withdrawal, the type of game played, depositing method, and withdrawal
method were included in the data. Additionally, the monetary balance before and after
each bet, win, deposit, and withdrawal was recorded. Session length was computed in
line with previous research (e.g., Auer & Griffiths, 2023a, 2023b; Hopfgartner et al.,
2023). More specifically, if two bets were placed within a 15-min period, the time
between was counted as within session. If more than 15 min elapsed between two bets,
they were counted as belonging to separate sessions.
1 3

International Journal of Mental Health and Addiction (2026) 24:981–1003 987
Study Design
Each of the nine PGSI items could be answered with “never” (0), “sometimes” (1), “most
of the time” (2), and “almost always” (3). Therefore, the maximum score was 27, and the
minimum score was 0. Player-tracking features were computed for the 30 days prior to
completing the PGSI (mirroring the studies by Auer and Griffiths [2023a] and Luquiens
et al. [2016]). The player-tracking features examined are listed in Appendix 2 and are
largely in line with those of Auer and Griffiths (2023a). Apart from the demographics (i.e.,
country, gender, and age in years), the player-tracking features included the total amount
of money bet, lost, withdrawn, and deposited 30 days prior to PGSI completion. Monetary
aspects can be a crucial aspect in the development of problem gambling (Tabri et al., 2022;
Blaszczynski and Nower, 2010). Previous studies have also emphasized the importance
of time spent gambling in the development of problem gambling (Lin et al., 2010; Wil-
liams et al., 2006). The player-tracking features also included behavioral aspects such as
the number of monetary deposits per session and the number of failed deposits (e.g., due to
insufficient funds). The number of voluntary limit changes, as well as the number of volun-
tary temporary self-exclusions, was also included in the data collected. Two metrics (i.e.,
regular account depletion and frequent depositing) were specifically designed to assess
impulsivity as it is a crucial aspect of problem gambling (Nower & Blaszczynski, 2006b).
1. Regular account depletion: This was assessed using the percentage of sessions end-
ing with low account balance for each gambler. The authors had access to the account
balance before and after each monetary bet, win, deposit, and withdrawal. The authors
assumed that individuals with disordered gambling only stop gambling when their online
gambling account is depleted. This metric indicates if less than €5 was left in the online
gambling account at the end of a session. Furthermore, regular account depletion was
identified by Auer and Griffiths (2023c) as a significant indicator of chasing losses.
2. Frequent deposits: This was assessed using the average number of monetary deposits
per session for each gambler. This metric was also highlighted as a significant indicator
of chasing losses by Auer and Griffiths (2023c).
Statistical Analysis
A hierarchical logistic regression was conducted to test the importance of three catego-
ries of independent variables, as proposed by Hopfgartner et al. (2023). These were age
and gender (i.e., control variables), behavioral variables, and monetary intensity variables.
These are listed in Appendix 2. First, three control models were fitted, one for each coun-
try, utilizing the control variables and a subsequent stepwise backward elimination process.
Given the limited number of groups (i.e., three countries), individual regression models
for each country (i.e., no pooling approach) were opted for as opposed to a mixed effects
or a multilevel model (i.e., partial pooling approach) as recommended by Gelman and Hill
(2006). During the backward elimination, variables with the highest collective p-value
(Zaykin, 2011) were sequentially excluded until only variables significant in at least one
country remained.
To address RQ1, the authors employed the same methodology, conducting three regres-
sions that included both control and behavioral variables. These models (model RQ1)
were then evaluated against the initial control models. To address RQ2, monetary intensity
1 3

988 International Journal of Mental Health and Addiction (2026) 24:981–1003
variables were also added to the models (model RQ2), and comparisons were made with
the previous models (model RQ1). A likelihood ratio chi-squared test was used to validate
the significance of each feature category and with Akaike’s information criteria (AIC) pro-
viding additional information concerning potential improvements of the models.
To mitigate potential multicollinearity within the variables, a threshold was set to
include only those variables with a variance inflation factor (VIF) below 10 (James et al.,
2013). Standardization of all independent variables was performed to facilitate the compar-
ison between models. Coefficients are reported for each model, where negative coefficients
indicate a decrease (and positive coefficients an increase) in the probability of self-reported
problem gambling. To assess the fit of all models, Nagelkerke’s (1991) R2 is reported,
quantifying the explained variance within the models.
To address RQ3, five different machine learning models were trained: AdaBoost, deci-
sion trees, extra-trees (extremely randomized trees), gradient boosting, and random forests.
To test whether machine learning models generalized to other countries in predicting self-
reported problem gambling, each model was trained using data from two countries while
reserving the third country for testing. This process allowed every country to function as a
test set once to assess how well the models could be applied across countries.
For comparability, the authors also included a baseline model, which used the gamblers’
total amount of money deposited within the past 30 days as a direct score for self-reported
problem gambling. The rationale for this baseline was to evaluate how such a simple
model, which only relied on the total monetary deposits, would compare to a model includ-
ing more complex behavioral variables. Therefore, the baseline model established a direct
correlation, where higher deposits indicated a stronger tendency towards problem gam-
bling. To further evaluate whether incorporating country-specific data during model train-
ing improved the overall performance of the prediction, an additional model was trained
which included the data of all three countries and performed a 70/30 train-test split on it.
The optimization of hyperparameters for each tree-based model was conducted through
a randomized cross-validation search, using a unified parameter space. For parameters
such as maximum tree depth and the minimum percentage of samples per leaf, a range
was pre-defined, specifically from 2 to 10 for tree depth, and 0% to 10% samples per leaf.
The learning rates for gradient boosting and AdaBoost were set within a 0 to 0.5 range.
Default parameters from the scikit-learn library (Pedregosa et al., 2011) were applied for
any remaining parameters. The performance of all models was reported using the receiver
operating characteristic area under the curve (ROC-AUC) values, which indicate the extent
to which the models can distinguish between individuals with and without self-reported
problem gambling.
Participants
A total of 6352 players completed the nine PGSI questions between January 2022 and Novem-
ber 2023. Figure 1 displays the PGSI score distribution before and after data cleaning. The
PGSI score and the respective frequency were negatively correlated (i.e., most gamblers had
low PGSI scores). However, before data cleaning, there was strong increase in scoring 27 (the
maximum score) on the PGSI. In line with Auer and Griffiths (2023a), it was assumed that this
spike was caused by gamblers who did not take enough time and simply rushed through the
scale items. Therefore, participants who completed the PGSI in less than 1 min were excluded
from the analysis to ensure the reliability of the data, leaving 1743 participants.
1 3

International Journal of Mental Health and Addiction (2026) 24:981–1003 989
Fig. 1 Distribution of PGSI responses before and after removing participants who completed the PGSI in
under a minute. The percentages above the orange bars indicate the percentage of participants which were
retained after removing short response times
Less strict variations to this exclusion criterion (e.g., only excluding participants who
completed the PGSI in less than 40 s or 50 s) yielded significant, but not practically rele-
vant differences. The 1-min threshold was also empirically supported by the observed data
pattern for participants who scored 27 out of 27 on the PGSI. A visible natural gap in com-
pletion times around the 1-min mark, as shown in Fig. 2, indicated a difference between
participants who engaged thoughtfully with the PGSI survey questions and those who did
not. This pattern confirmed the use of this threshold and suggested that responses com-
pleted in less than 1 min were unlikely to reflect genuine self-assessment and therefore
Fig. 2 Distribution of PGSI completion times for gamblers who scored 27 out of 27. A natural gap in com-
pletion times around the 1-min mark indicates a separation between gamblers who thoughtfully engaged
with the PGSI items and those who likely rushed their responses
1 3

990 International Journal of Mental Health and Addiction (2026) 24:981–1003
indicated a lack of engagement with the PGSI survey questions. Notably, the distribution
of scores after this cleaning process shows a stronger reduction in the proportion of partici-
pants with extreme scores of 0 and 27, supporting the hypothesis that these responses were
likely hasty and uniformly answered with the same response, indicating a potential bias in
the validity of their data.
Table 1 presents a comparative overview of gambling statistics by the participants
across the three countries (Canada, Spain, GB) in the dataset. Canadian gamblers com-
prised 6.0% of the sample, with a mean PGSI score of 7.11, and 35.2% having a PGSI
score equal or above 8 (indicating problem gambling). The mean age of Canadian gamblers
was 45.9 years, and the proportion of female gamblers was 40.0%. British gamblers com-
prised 73.7% of the sample, with a mean PGSI score of 5.47, and 26.4% having a PGSI
score of equal or above 8. The mean age of British gamblers was 43.5 years, and the pro-
portion of female gamblers was 41.8%. Spanish gamblers comprised 20.3% of the sample,
with an average PGSI score of 5.67, and 28.9% having a PGSI score of equal or above 8.
The mean age of Spanish gamblers was 37.3 years, and the proportion of female gamblers
was 28.3%. Overall, the mean PGSI score across the total sample of gamblers was 5.61,
and 27.4% having a PGSI score of equal or above 8. The mean age of the total sample was
42.4 years, and the proportion of female gamblers was 39.0%. These results highlight the
cross-national variations in the demographic and risk profile of the gamblers from the three
different countries.
The cross-national variations in gambling behaviors, as indicated by the PGSI scores
among participants from Canada, GB, and Spain, were further evident in the post hoc anal-
ysis shown in Table 2. This analysis showed statistically significant differences in PGSI
scores between the gamblers from the three countries (Kruskal–Wallis test: H = 18.3,
p < 0.001). Notably, the difference between Canadian and British gamblers, as well as
between Canadian and Spanish gamblers, was significant (U = 51,348, p < 0.001 and
U = 14,996, p = 0.0014, respectively), indicating that Canadian gamblers had a significantly
higher PGSI score compared to their British and Spanish counterparts. The difference
between the PGSI scores from Spanish and British gamblers (U = 213,829, p = 0.0486) was
Table 1 Descriptive statistics of the dataset per country
Country Number of players Mean PGSI Players with Mean Female gamblers
score PGSI 8 + age
Canada 105 (6.0%) 7.11 37 (35.2%) 45.9 years 40%
Great Britain 1285 (73.7%) 5.47 339 (26.4%) 43.5 years 41.8%
Spain 353 (20.3%) 5.67 102 (28.9%) 37.3 years 28.3%
1743 (100%) 5.61 478 (27.4%) 42.4 years 39.0%
not significant after Bonferroni correction for multiple testing (i.e., corrected alpha level
Table 2 Post hoc tests for differences in the countries’ PGSI scores. Significant p-values highlighted in bold
according to the Bonferroni corrected alpha level of 0.05/3 = 0.016
Canada Great Britain
Great Britain < 0.001 -
Spain 0.0014 0.0486
1 3

International Journal of Mental Health and Addiction (2026) 24:981–1003 991
of 0.016). These findings align with the initial observations from Table 1, which suggested
notable variations in the gambling risk profiles across these nations.
Ethics
The study adhered to the guidelines set forth in the Declaration of Helsinki and received
approval from the research team’s university ethics committees.
Results
Table 3 highlights descriptive statistics distinguishing problem gamblers (PGs, PGSI score
8 +) from non-problem gamblers (NPGs, PGSI score < 8). PGs had a lower mean amount
of money deposited in the 30 days before completing the PGSI (€524), as compared to the
average of €708 deposited by NPGs. However, a Mann–Whitney U test showed no signifi-
cant difference between PGs and NPGs in the amount of money deposited (U = 290,854.5,
p = 0.2207). A significant difference in age was observed between PGs and NPGs. As a
Shapiro–Wilk test reported that the age was not normally distributed (S = 0.98, p < 0.001),
a Mann–Whitney U test indicated that PGs were significantly younger than NPGs
(U = 235,128, p < 0.001). The proportion of female gamblers did not significantly differ
between PGs (36.2%) and NPGs (40.0%; Z = 1.45, p = 0.146).
Associating Player‑Tracking Data with Self‑Reported Problem Gambling (RQ1
and RQ2)
Figure 3 shows the findings from hierarchical regression analyses focusing on the predic-
tors of self-reported problem gambling. The control models (Fig. 3a) explored the impact
of demographics after backward elimination, showing that in Great Britain and Spain,
younger gamblers were more likely to be self-reported problem gamblers, with a visible
but non-significant trend in Canada suggesting the same direction. A solid dot indicates
statistical significance and a cross that the variable is not statistically significant in that
country.
The models addressing RQ1 in Fig. 3b incorporated behavioral variables to assess their
influence on self-reported problem gambling. The results suggested that specific behaviors,
such as taking self-exclusions, gambling for a shorter average session length, frequent in-
session depositing, and frequent depletion of the gambling balance, were indicators of a
higher likelihood towards self-reported problem gambling. Frequent in-session depositing
Table 3 Descriptive statistics for problem gamblers (PG, i.e., PGSI score 8 +) and non-problem gamblers
(NPG; PGSI score < 8)
Self-reported Number of Mean amount of Mean number of Mean Female gamblers
problem gambler players money deposited active gambling age
(€) days
No 1265 (72.6%) 708 8 43.7 years 40.0%
Yes 478 (27.4%) 524 7 39.2 years 36.2%
1743 (100.0%) 657 8 42.4 years 39.0%
1 3

992 International Journal of Mental Health and Addiction (2026) 24:981–1003
Fig. 3  Coefficients including 95% confidence intervals for the hierarchical regression analyses. Each model
consisted of three separate regressions (i.e., one for each country) and included only those variables that
were significant in at least one country. Solid dots indicate statistical significance
was significantly associated with self-reported problem gambling in two countries (i.e.,
Canada and Spain). The other behavioral variables were only significantly associated with
self-reported problem gambling in one of the three countries. Overall, adding behavioral
features to the models significantly increased the Nagelkerke R2 (see likelihood ratio chi-
square tests in Table 4 for RQ1) and reduced the AIC compared to the model which only
contained the control variables. Only in Canada did the inclusion of behavioral variables
not significantly improve the model performance (χ2 = 6.2, df = 4, p = 0.184).
RQ2, illustrated in Fig. 3c, adds monetary gambling intensity variables to the aforemen-
tioned demographics and behavioral features. The results suggested that monetary vari-
ables did not significantly improve the models’ performance, given the inclusion of demo-
graphics and behavioral features. Therefore, the backward elimination resulted in the same
models as for RQ1, suggesting that beyond behavioral patterns, the intensity of monetary
Table 4  Likelihood ratio chi-squared test (LRT), Nagelkerke-R2 (NK-R2), and AIC values for the hierarchi-
cal regression analyses. Significant p-values highlighted in bold according to the Bonferroni corrected alpha
level of 0.05/3 = 0.016. Note that the values of the Nagelkerke-R2 and the AIC are the same for RQ2, as the
final models were the same. Therefore, also no LRT for RQ2 was calculated
|           |         | Canada (CA) | Great Britain (GB) | Spain (ES) |
| --------- | ------- | ----------- | ------------------ | ---------- |
| LRT (RQ1) | χ2(df)  | 6.2 (4)     | 145.5 (4)          | 19.1 (4)   |
|           | p-value | 0.184       |                    |            |
|           |         |             |  < 0.001           |  < 0.001   |
χ2(df)
| LRT (RQ2) |         | -   | -   | -   |
| --------- | ------- | --- | --- | --- |
|           | p-value | -   | -   | -   |
NK-R2
|     | Model control | 0.013 | 0.044  | 0.045 |
| --- | ------------- | ----- | ------ | ----- |
|     | Model RQ1     | 0.091 | 0.196  | 0.118 |
|     | Model RQ2     | 0.091 | 0.196  | 0.118 |
| AIC | Model control | 139.3 | 1447.5 | 417.2 |
|     | Model RQ1     | 141.0 | 1310.0 | 406.0 |
|     | Model RQ2     | 141.0 | 1310.0 | 406.0 |
1 3

International Journal of Mental Health and Addiction (2026) 24:981–1003 993
gambling does not significantly contribute to the likelihood of self-reported problem
gambling.
Overall, the regression analyses emphasized the significance of behavioral factors over
monetary ones when associating player-tracking data with self-reported problem gambling.
The models showed that age and specific gambling behaviors, like self-exclusions, in-ses-
sion depositing, and account depletion were more important predictors than the amount of
money gambled.
Predicting Self‑Reported Problem Gambling (RQ3)
Table 5 shows the performance (ROC-AUC values) of various machine learning models
in predicting self-reported problem gambling. In the first approach, data from one coun-
try was reserved for testing, and the other two countries provided the training data. This
approach enabled the testing of whether the models generalized across countries in predict-
ing self-reported problem gambling. For the second approach, a standard 70/30 train-test
split on the entire data was utilized, and the performance was reported by country. With
this approach, each country’s data were included in the training dataset, which provided
country-specific patterns to the models.
The results from Table 5 indicated the machine learning models, which are trained on
data from all three countries, outperformed those that were trained on two countries only.
For Canada, the random forest model, which was trained including Canadian players, had
a ROC-AUC score of 0.717, while the extra-trees model which was only trained on data
from GB and Spain had a score of 0.662. In Great Britain, the extra-trees model with
which was trained including British players had a ROC-AUC of 0.699, compared to 0.644
(random forest) which was only trained on Canadian and Spanish players. In Spain, the
highest score for the model, which was trained including Spanish players, was 0.654 (gra-
dient boosting), while the decision tree, which was only trained on British and Canadian
players, had a ROC-AUC of 0.609.
The baseline model’s performance, utilizing the total amount of money deposited
as a stand-alone predictor, had an ROC-AUC value of approximately 0.5. Therefore,
Table 5 ROC-AUC values of the five machine learning models for each country. In the first approach, one
country was left out during training and was used as test set. In the second approach, a global model trained
on all data was used and a 70/30 split into training and test data was applied
Canada Great Britain Spain
Canada Entire dataset GB data left Entire dataset Spain data left Entire dataset
data left out out
out
Baseline 0.518 0.518 0.476 0.476 0.548 0.548
AdaBoost 0.575 0.515 0.597 0.606 0.572 0.631
Decision tree 0.592 0.475 0.585 0.598 0.609 0.519
Extra-trees 0.662 0.613 0.617 0.699 0.541 0.598
Gradient 0.588 0.570 0.577 0.653 0.585 0.654
boosting
Random forest 0.600 0.717 0.644 0.653 0.597 0.647
1 3

994 International Journal of Mental Health and Addiction (2026) 24:981–1003
its performance was similar to a random guess, emphasizing the limitations of relying
solely on a monetary metric. This result again highlighted the importance of behavio-
ral variables in the detection of self-reported problem gambling. Overall, the results
indicated that including country-specific patterns generally enhanced the models’
predictive power. However, the variance in ROC-AUC scores across different models
and countries also emphasized the importance of model selection based on the data
characteristics.
Discussion
The present study analyzed the correlation between self-reported PGSI responses and
actual gambling behavior in a secondary dataset of 6352 Spanish, British, and Canadian
(from the Canadian province Ontario only) online casino gamblers. Out of the 6352
gamblers, 1743 spent at least 1 min responding to the nine items. These were retained
for further analysis. In line with Auer and Griffiths (2023a), the minimum answering
time was seen as an indication responding to the items seriously. Taking a very short
amount of time to respond to all the items assumes that the gamblers did not properly
read the questions, and therefore, the responses would not accurately reflect their prob-
lem gambling status. The data cleaning process removed the majority of the gamblers
reaching the highest score (27/27) as they chose the highest answer category for each
of the nine items. The same effect was observed on the lowest end of the score range
(0/27) as these gamblers always chose the lowest answer category for the nine items.
Out of the 1743 gamblers, 478 had a PGSI score of 8 or more out of 27 (27.4%).
A score of 8 + is considered as indicating problem gambling (Holtgraves, 2008). Sev-
eral other studies have collected PGSI responses from online gambling cohorts. Auer
and Griffiths (2023a) reported that among a sample of European online casino players,
26% reported a PGSI score of 8 or more. Murch et al. (2023) reported 12% problem
gambling among a sample of Canadian online casino gamblers. However, the Cana-
dian online gambling site also offered lottery games, which are less likely to cause
gambling problems which may have explained the lower prevalence of problem gam-
bling. Among a sample of French online gamblers (engaging in horse betting, sports
betting, poker), 26% of gamblers reported problem gambling based on a PGSI score of
8 + (Perrot et al., 2022). Therefore, the present study’s prevalence of problem gambling
is in line with previous research using similar methodologies.
In the present study, the largest prevalence of problem gambling was observed among
Canadian gamblers (35.2%). Online gambling in the Canadian province of Ontario was
introduced in 2022, whereas Spain legalized the online gambling market in 2011. To the
best of the authors’ knowledge, legal online gambling has been available in Great Britain
for over 20 years. The long availability of legal online gambling is also related to a longer
history of regulation, which could have resulted in safer gambling practices and therefore
lower problem gambling rates. Additionally, the UK Gambling Commission frequently
fines operators for player safety violations (e.g., Andrade et al., 2023; Gambling Commis-
sion, 2022a, 2022b), which could also have led to improved player protection.
1 3

International Journal of Mental Health and Addiction (2026) 24:981–1003 995
Demographics and Behaviors Associated with Self‑Reported Problem Gambling
Age was negatively associated with self-reported problem gambling, and the effect was
significant among online casino gamblers in Great Britain and Spain. Although there
was a visible effect in Canada, it was not statistically significant. Many prevalence stud-
ies have reported a higher prevalence of problem gambling among younger individu-
als (e.g., Abbott et al., 2014; Ekholm et al., 2014; 2015; Kun et al., 2012). Impulsivity
(i.e., acting without thinking and the inability to delay gratification and sensation seek-
ing) and depression have been reported as key risk factors for problem gambling among
adolescents (e.g., Gupta et al., 2013; Secades-Villa et al., 2016; Turner et al., 2008).
Although online gambling is only legal from the age of 18 years in most countries, the
adolescent brain does not fully mature until around the mid-20s (Andrews et al., 2021;
Icenogle et al., 2019).
After adding behavioral metrics to the regression model, only taking self-exclu-
sions, gambling for shorter session lengths, frequent monetary depositing per session,
and regular account depletion significantly contributed to self-reported problem gam-
bling. These independent variables were significant in at least one of the three coun-
tries. Frequent monetary depositing within sessions has previously been reported as a
behavior that is indicative of chasing losses (Auer & Griffiths, 2023c). Chasing losses
is a crucial aspect of impulsivity, and online gambling among vulnerable individuals
can have negative impacts on self-control (Siemens and Kopp, 2011). Depositing fre-
quently within sessions and regular account depletion also significantly contributed to
the prediction of self-reported problem gambling in a previous study (Auer & Griffiths,
2023b). Moreover, Perrot et al. (2022) and Murch et al. (2023) also identified frequent
depositing (although not within sessions) to be significant predictors of self-reported
problem gambling.
Several previous studies predicting self-reported problem gambling have reported
a significant association with self-exclusion. Perrot et al. (2022) reported that 31% of
those with problem gambling had taken at least one temporary self-exclusion since they
started gambling online. In contrast, only 4% of non-problem gamblers had done so.
The respective percentages reported by Auer and Griffiths (2023a) in their study were
46% among those with problem gambling and 12% among those with no problems.
Among the behavioral variables, the average time spent gambling per session over
the past 30 days was also significant. However, the association between self-reported
problem gambling and average time spent gambling was negative. This means that self-
reported problem gamblers average session length was lower compared to non-problem
gamblers. Time devoted to gambling has been reported as a predictive factor of online
gambling (Barrault & Varescon, 2013; Hopley & Nicki, 2010). Luquiens et al. (2016)
reported a significantly longer gambling time for problematic online poker playing
compared to non-problematic online poker playing. Considering previous research, the
negative association in the present study between average gambling duration and self-
reported problem gambling appears contradictory. However, one explanation could be
that those with self-reported problem gambling might already have attempted to con-
trol their gambling, and therefore had shorter average gambling sessions in the 30 days
prior to completing the PGSI. This hypothesis is also supported by the higher percentage
of self-exclusions among those self-reporting problem gambling, which is indicative of
attempts to control or stop gambling.
1 3

996 International Journal of Mental Health and Addiction (2026) 24:981–1003
None of the monetary intensity variables contributed significantly to the model,
which included demographic and behavioral metrics. This means that the total amount
of money bet, lost, withdrawn, and deposited did not improve the prediction of self-
reported problem gambling. To the best of the authors knowledge, the present study is
the first that has predicted self-reported problem gambling using a hierarchical mod-
eling approach. Only one previous study (Hopfgartner et al., 2023) applied hierarchi-
cal logistic regressions to investigate behavioral patterns associated with voluntary self-
exclusions. In their study, the authors also reported that monetary intensity variables
did not significantly contribute to the model’s performance in most countries. The fact
that the amount of money gambled did not significantly contribute to the prediction of
self-reported problem gambling in the present study also supports the generalizability
of the statistical model across jurisdictions. Income levels (and therefore expenditure)
vary across countries, but a purely behavioral model is not affected by these variations.
Applying Machine Learning Models to Predict Self‑Reported Problem Gambling
Despite the improved performance of the models, which were trained on all three countries’s
data, the models trained without one country’s data still showed a good performance indicating
a weak generalization across countries. The slightly lower AUC values can be partly attributed
to the nature of the target variable, which is self-reported and was determined using a threshold
(i.e., considering a score of 8 or more as problem gambling), leading to skewness in the data.
This aspect, coupled with the smaller number of Canadian participants in the dataset and its
distinct characteristics compared to the other two countries (i.e., higher PGSI scores in Can-
ada), emphasizes the challenges in achieving higher ROC AUC values in such varied settings.
Despite these constraints, the ability of these models to (weakly) generalize across countries
and identify patterns of self-reported problem gambling is promising. This means that models
which were not trained with data from a specific country still identified some of the patterns of
self-reported problem gambling in the player-tracking data of that country. This robustness sug-
gests that while country-specific patterns enhance model performance, the underlying behav-
ioral patterns captured by the machine learning models were sufficient to weakly generalize
across countries to predict self-reported problem gambling. This is, for example, important
regarding newly regulated jurisdictions, which might introduce legalized online gambling in the
future. The general predictors of self-reported problem gambling, which were identified in the
present study, appeared to be valid in all three jurisdictions. Nevertheless, future research can
explore these possibilities on larger datasets and information from additional countries to isolate
the common as well as diverging behavioral patterns across those countries.
Applications and Implications
The present study is important because it is one of the very few studies to integrate sub-
jective self-report data with objective account-based tracking data. Such a methodological
approach will help move the gambling study field given the robustness of the combined
datasets. Such an approach can be used by both researchers and practitioners in the field,
as well as by the gambling industry who often do their own internal approach. Importantly,
the present study also (i) highlighted the benefits of using artificial intelligence in the study
of both gambling and problem gambling, (ii) identified behavioral markers of gambling
harm (e.g., frequent monetary depositing within session, regular account depletion) which
can be utilized by gambling operators (and enforced by regulators) to help them identify
1 3

International Journal of Mental Health and Addiction (2026) 24:981–1003 997
risky gambling and potential problem gamblers, and (iii) provided important implications
for the development of responsible gambling tools and interventions. By highlighting the
significance of behavioral patterns, such as frequent in-session monetary depositing and
account depletion, the study contributes to the body of knowledge required for designing
tailored responsible gambling strategies that can be adapted to diverse regulatory contexts.
The comprehensive approach used in the present study could serve as a foundation for
future research in newly regulated or evolving online gambling markets.
Limitations and Future Research
While contributing valuable insights into the predictors of self-reported problem gambling, the
present study is subject to specific limitations that must be acknowledged. One specific limita-
tion arises from the self-selection bias inherent in the dataset (Tripepi et al., 2010) because it
only included data from gamblers who had voluntarily completed the PGSI. This self-selection
bias is also visible in the disproportionately high rate of problem gamblers within the present
sample compared to the rates reported in prevalence studies. More specifically, the present study
identified self-reported problem gambling rates of 35.2% in Canada, 26.4% in Great Britain,
and 28.9% in Spain, using the PGSI with a threshold of 8 or more for problem gambling. These
rates were significantly higher than those reported in the respective national prevalence studies:
0.6% in Canada (Williams et al., 2021), between 2.5% and 2.8% in Great Britain (Gambling
Commission, 2023; Gunstone et al., 2022), and 0.72% in Spain (Chóliz et al., 2021). Individuals
who choose to assess their gambling behaviors through the PGSI may already have concerns
about their gambling habits, thereby skewing the sample towards higher rates of problem gam-
bling compared to a randomized or representative sample of the general gambling population.
This bias must be considered when interpreting the results because it may influence the predic-
tive accuracy of the machine learning models used. Future studies would benefit from analyzing
a more representative sample to provide a more comprehensive picture.
Secondly, the reliance on self-reported data in determining problem gambling sever-
ity presents another limitation, given the potential discrepancies between self-perceptions
and actual gambling behaviors. The accuracy of self-reported data can be compromised by
a variety of factors, including memory recall, social desirability bias, and the subjective
nature of self-assessment tools (Auer et al., 2023; Schell et al., 2021). While the present
study provides insights to the predictive factors of self-reported problem gambling, these
limitations must be considered.
Third, another limitation to consider is the relatively small sample size of this study in
comparison to other player-tracking studies. The reduction in sample size, primarily due to
the data cleaning process where participants completing the PGSI in less than 1 min were
excluded, can limit the statistical power of the study. This, in turn, can potentially affect the
robustness and reliability of the findings (Button et al., 2013). However, it is equally impor-
tant to emphasize that the integrity and reliability of the data are of paramount importance.
Including data from gamblers who were unlikely to have engaged seriously with the PGSI
survey questions could have led to confounding and potentially misleading results, which
could affect the validity of the study’s findings. The significant reduction in sample size
is therefore considered a limitation, but this decision was made to ensure the quality and
reliability of the data. Furthermore, the imbalance between the proportions of gamblers in
each country presents another limitation. Gambling behaviors can vary significantly across
different regions and cultures, influenced by various factors such as legal regulations, soci-
etal norms, and economic conditions (Raylu & Oei, 2004; Selin, 2019). Therefore, the
1 3

998 International Journal of Mental Health and Addiction (2026) 24:981–1003
overrepresentation or underrepresentation of gamblers from specific countries can impact
the study’s ability to generalize its findings.
Next, the use of a 30-day period for calculating gambling behavior prior to completing the
PGSI represented a methodological decision that may have affected the results of the study.
One advantage of this time frame is that it captured the current gambling behavior that is
likely to most influence participants’ responses to the PGSI, which is intended as an instru-
ment to reflect gambling behavior over the past year. On the other hand, a shorter period
does not account for long-term behavioral trends and fluctuations in gambling that can be
captured by a 12-month period, such as episodic gambling. However, a 12-month observation
period can also lead to biases. For example, it is possible that players who scored high on the
PGSI may have participated in gambling shortly before completing the PGSI, while players
with lower scores may not have gambled recently. This temporal proximity could lead to an
overestimation of problem gambling behavior among active gamblers and an underestima-
tion among less active gamblers, which in turn affects the accuracy of the model. The present
study’s choice to rely on a 30-day observation period is therefore a compromise between the
temporal relevance of the behavioral data and the risk of biasing the model by including less
recent gambling activity. This trade-off should be considered in future research to match the
observation period to the temporal scope of the PGSI.
Finally, several behavioral variables in the present study were not significantly associated with
self-reported problem gambling. This highlights the multifaceted nature of gambling disorder,
which encompasses not only behavioral aspects, but also psychological aspects. The PGSI incor-
porates indicators such as experiencing health problems and feelings of guilt, which are reflective
of the psychological state of individuals with gambling disorders. These characteristics relate to
cognitive aspects and the consequences of gambling, factors that are cannot be captured in player
tracking data. Given this difference in the items of the PGSI between measurable behaviors and
less measurable psychological criteria, this may be one explanation why only specific behaviors
were significantly associated with self-reported problem gambling in the present study.
Future research should aim to mitigate these limitations and explore the utility of the
findings across a wider and more balanced array of gambling platforms and jurisdictions to
improve the development of effective responsible gambling tools and interventions. Moreo-
ver, the machine learning models’ performance in predicting self-reported problem gam-
bling across countries highlighted the potential for future research to refine and enhance
these predictive capabilities. Finally, replication studies with various operators and across
different countries are needed. Such studies would provide greater insight into the gener-
alizability of the present findings and could potentially identify unique behavioral patterns
that are specific to specific regions or gambling platforms.
Conclusions
The present study provided a nuanced understanding of the predictors of self-reported
problem gambling, emphasizing the importance of behavioral variables over monetary
variables. The findings support the hypothesis that self-reported problem gambling can be
predicted using player-tracking data, independent of monetary expenditure, across differ-
ent countries. Applying machine learning models to predict self-reported problem dem-
onstrated that the inclusion of country-specific data enhanced the predictive performance.
Nevertheless, the robustness of the models without country-specific training data suggested
the existence of universal behavioral patterns that cross cultural and regulatory boundaries.
1 3

International Journal of Mental Health and Addiction (2026) 24:981–1003 999
Appendices
Appendix 1 Problem Gambling Severity Index items. Individuals can answer: never (0), sometimes (1),
most of the time (2), and almost always (3). A score of 8 + indicates problem gambling
Item number and question
(1) Have you bet more than you could really afford to lose?
(2) Have you needed to gamble with larger amounts of money to get the same excitement?
(3) Have you gone back to try to win to back the money you’d lost?
(4) Have you borrowed money or sold anything to get money to gamble?
(5) Have you felt that you might have a problem with gambling?
(6) Have you felt that gambling has caused you any health problems, including stress or anxiety
(7) Have people criticized your betting, or told you that you have a gambling problem, whether or not you
thought it is true?
(8) Have you felt your gambling has caused financial problems for you or your household?
(9) Have you felt guilty about the way you gamble or what happens when you gamble?
Appendix 2 Player tracking features based on the thirty days before answering the PGSI
Demographics Behavioral features Monetary features
Country Number of self-exclusions Amount of money bet
Age (in years) Number of voluntary limit changes Amount of money deposited
Gender Number of withdrawals Amount of money lost
Standard deviation of withdrawals Amount of money withdrawn
Number of failed deposits
Standard deviation of bets
Number of different game types played
Number of different payment methods
Average session length (in minutes)
Average number of deposits per session
Percent of bet at night
Percent of sessions at night
Percent of sessions on weekends
Percent of bet on weekends
Percent of sessions ending with low account bal-
ance (Account depletion)
Percent of loss at night
1 3

1000 International Journal of Mental Health and Addiction (2026) 24:981–1003
Authors’ Contribution All authors contributed to the preparation of this manuscript.
Funding Not applicable.
Data Availability The data for this study are not available due to commercial sensitivity.
Declarations
Ethics This study was performed in line with the principles of the Declaration of Helsinki and was approved
by the research team’s university ethic committees.
Conflict of Interest The last author has received research funding from Norsk Tipping (the gambling operator
owned by the Norwegian government). The last author has also received funding for a number of research
projects in the area of gambling education for young people, social responsibility in gambling and gambling
treatment from Gamble Aware (formerly the Responsibility in Gambling Trust), a charitable body which
funds its research program based on donations from the gambling industry. The first, second and last authors
undertake consultancy for various gaming companies in the area of social responsibility in gambling.
Open Access This article is licensed under a Creative Commons Attribution 4.0 International License,
which permits use, sharing, adaptation, distribution and reproduction in any medium or format, as long
as you give appropriate credit to the original author(s) and the source, provide a link to the Creative Com-
mons licence, and indicate if changes were made. The images or other third party material in this article
are included in the article’s Creative Commons licence, unless indicated otherwise in a credit line to the
material. If material is not included in the article’s Creative Commons licence and your intended use is not
permitted by statutory regulation or exceeds the permitted use, you will need to obtain permission directly
from the copyright holder. To view a copy of this licence, visit http://creativecommons.org/licenses/by/4.0/.
References
Abbott, M. W., Romild, U., & Volberg, R. A. (2014). Gambling and problem gambling in Sweden: Changes
between 1998 and 2009. Journal of Gambling Studies, 30(4), 985–999.
Andrade, M., Sharman, S., Xiao, L. Y., & Newall, P. W. (2023). Safer gambling and consumer protection
failings among 40 frequently visited cryptocurrency-based online gambling operators. Psychology of
Addictive Behaviors, 37(3), 545–557.
Andrews, J. L., Ahmed, S. P., & Blakemore, S. J. (2021). Navigating the social environment in adolescence:
The role of social brain development. Biological Psychiatry, 89(2), 109–118.
Auer, M., Griffiths, M.D. (2023b). Predicting high-risk gambling based on the first seven days of gambling
activity after registration using account-based tracking data. International Journal of Mental Health
and Addiction. Advance online publication. https:// doi. org/ 10. 1007/ s11469- 023- 01056-4
Auer, M., Hopfgartner, N., Helic, D., & Griffiths, M. D. (2023). Self-reported deposits versus actual depos-
its in online gambling: An empirical study. Journal of Gambling Studies. Advance online publication.
https:// doi. org/ 10. 1007/ s10899- 023- 10230-1
Auer, M., & Griffiths, M. D. (2023a). Using artificial intelligence algorithms to predict self-reported prob-
lem gambling with account-based player data in an online casino setting. Journal of Gambling Studies,
39(3), 1273–1294.
Auer, M., & Griffiths, M. D. (2023c). An empirical attempt to operationalize chasing losses in gambling
utilizing account-based player tracking data. Journal of Gambling Studies, 39(4), 1547–1561.
Auer, M., & Griffiths, M. D. (2023d). The relationship between structural characteristics and gambling
behaviour: An online gambling player tracking study. Journal of Gambling Studies, 39(1), 265–279.
Auer, M., & Griffiths, M. D. (2023e). Attitude towards deposit limits and relationship with their account-based
data among a sample of German online slots players. Journal of Gambling Studies, 39(3), 1319–1336.
Barrault, S., & Varescon, I. (2013). Cognitive distortions, anxiety, and depression among regular and pathologi-
cal gambling online poker players. Cyberpsychology, Behavior and Social Networking, 16(3), 183–188.
Blaszczynski, A., & Nower, L. (2010). Instrumental tool or drug: Relationship between attitudes to money
and problem gambling. Addiction Research & Theory, 18(6), 681–691.
1 3

International Journal of Mental Health and Addiction (2026) 24:981–1003 1001
Button, K. S., Ioannidis, J. P. A., Mokrysz, C., Nosek, B. A., Flint, J., Robinson, E. S. J., & Munafò, M.
R. (2013). Power failure: Why small sample size undermines the reliability of neuroscience. Nature
Reviews Neuroscience, 14(5), 365–376. https:// doi. org/ 10. 1038/ nrn34 75
Catania, M., & Griffiths, M. D. (2021). Understanding online voluntary self-exclusion in gambling: An
empirical study using account-based behavioral tracking data. International Journal of Environmental
Research and Public Health, 18(4), 2000.
Catania, M., & Griffiths, M. D. (2023). Analyzing consumer protection for gamblers across different online
gambling operators: A replication study. International Journal of Mental Health and Addiction, 21(3),
1882–1897.
Chóliz, M. (2016). The challenge of online gambling: The effect of legalization on the increase in online
gambling addiction. Journal of Gambling Studies, 32(2), 749–756.
Chóliz, M., Marcos, M., & Lázaro-Mateo, J. (2021). The risk of online gambling: A study of gambling disor-
der prevalence rates in Spain. International Journal of Mental Health and Addiction, 19, 404–417.
Dowling, N. A., Merkouris, S. S., Manning, V., Volberg, R., Lee, S. J., Rodda, S. N., & Lubman, D. I.
(2018). Screening for problem gambling within mental health services: A comparison of the clas-
sification accuracy of brief instruments. Addiction, 113(6), 1088–1104.
Ekholm, O., Eiberg, S., Davidsen, M., Holst, M., Larsen, C. V., & Juel, K. (2014). The prevalence of
problem gambling in Denmark in 2005 and 2010: A sociodemographic and socioeconomic charac-
terization. Journal of Gambling Studies, 30, 1–10.
Elton-Marshall, T., Leatherdale, S. T., & Turner, N. E. (2016). An examination of internet and land-
based gambling among adolescents in three Canadian provinces: Results from the youth gambling
survey (YGS). BMC Public Health, 16(1), 277.
Ferris, J., & Wynne, H. J. (2001). The Canadian Problem Gambling Index: Final report. Canadian Cen-
tre on Substance Abuse.
Finkenwirth, S., MacDonald, K., Deng, X., Lesch, T., & Clark, L. (2021). Using machine learning to
predict self-exclusion status in online gamblers on the PlayNow.com platform in British Columbia.
International Gambling Studies, 21(2), 220–237.
Gambling Commission (2023). Statistics on participation and problem gambling. https:// www. gambl
ingco mmiss ion. gov. uk/ stati stics- and- resea rch/ publi cation/ gambl ing- parti cipat ion- and- the- preva
lence- of- probl em- gambl ing- survey- final
Gambling Commission (2022a). £1.17m fine for marketing to vulnerable consumers. https:// www. gambl
ingco mmiss ion. gov. uk/ news/ artic le/ gbp1- 17m- fine- for- marke ting- to- vulne rable- consu mers
Gambling Commission (2022b). £9.4m fine for online operator 888. https:// www. gambl ingco mmiss ion.
gov. uk/ news/ artic le/ gbp9- 4m- fine- for- online- opera tor- 888
Gebauer, L., LaBrie, R., & Shaffer, H. J. (2010). Optimizing DSM-IV-TR classification accuracy: A
brief biosocial screen for detecting current gambling disorders among gamblers in the general
household population. Canadian Journal of Psychiatry, 55(2), 82–90.
Gelman, A., & Hill, J. (2006). Data analysis using regression and multilevel/hierarchical models. Cam-
bridge University Press.
Griffiths, M. D., & Auer, M. (2016). Should voluntary “self-exclusion” by gamblers be used as a proxy
measure for problem gambling? Addiction Medicine & Therapy, 2(2), 31–33.
Griffiths, M. D., & Parke, J. (2002). The social impact of internet gambling. Social Science Computer
Review, 20(3), 312–320.
Gunstone, B., Gosschalk, K., Zabicka, E., & Sullivan-Drage, C. (2022). Annual GB Treatment and Sup-
port Survey 2021. https:// www. begam bleaw are. org/ sites/ defau lt/ files/ 2022- 03/ Annual% 20GB%
20Tre atment% 20and% 20Sup port% 20Sur vey% 20Rep ort% 202021% 20% 28FIN AL% 29. pdf
Gupta, R., Nower, L., Derevensky, J. L., Blaszczynski, A., Faregh, N., & Temcheff, C. (2013). Problem
gambling in adolescents: An examination of the pathways model. Journal of Gambling Studies,
29(3), 575–588.
Haeusler, J. (2016). Follow the money: Using payment behaviour as predictor for future self-exclusion.
International Gambling Studies, 16(2), 246–262.
Hancock, L., Schellinck, T., & Schrans, T. (2008). Gambling and corporate social responsibility (CSR):
Re-defining industry and state roles on duty of care, host responsibility and risk management. Pol-
icy and Society, 27(1), 55–68.
Hing, N., Russell, A. M., & Browne, M. (2017). Risk factors for gambling problems on online electronic
gaming machines, race betting and sports betting. Frontiers in Psychology, 8, 779.
Hing, N., Russell, A. M., Black, A., Rockloff, M., Browne, M., Rawat, V., & Woo, L. (2022). Gambling
prevalence and gambling problems amongst land-based-only, online-only and mixed-mode gam-
blers in Australia: A national study. Computers in Human Behavior, 132, 107269.
1 3

1002 International Journal of Mental Health and Addiction (2026) 24:981–1003
Holden, J. T., & Edelman, M. (2020). A short treatise on sports gambling and the law: How America
regulates its most lucrative vice. Wisconsin Law Review, 907, 907–974.
Holtgraves, T. (2008). Evaluating the Problem Gambling Severity Index. Journal of Gambling Studies,
25(1), 105–120.
Hopfgartner, N., Auer, M., Griffiths, M. D., & Helic, D. (2023). Predicting self-exclusion among online
gamblers: An empirical real-world study. Journal of Gambling Studies, 39(1), 447–465.
Hopley, A. A., & Nicki, R. M. (2010). Predictive factors of excessive online poker playing. Cyberpsy-
chology, Behavior and Social Networking, 13(4), 379–385.
Icenogle, G., Steinberg, L., Duell, N., Chein, J., Chang, L., Chaudhary, N., & Bacchini, D. (2019). Ado-
lescents’ cognitive capacity reaches adult levels prior to their psychosocial maturity: Evidence for a
“maturity gap” in a multinational, cross-sectional sample. Law and Human Behavior, 43(1), 69–85.
James, G., Witten, D., Hastie, T., & Tibshirani, R. (2013). An introduction to statistical learning.
Springer.
Kun, B., Balázs, H., Arnold, P., Paksi, B., & Demetrovics, Z. (2012). Gambling in western and eastern
Europe: The example of Hungary. Journal of Gambling Studies, 28, 27–46.
Lin, E. Y. J., Casswell, S., Easton, B., Huckle, T., Asiasiga, L., & You, R. Q. (2010). Time and money
spent gambling and the relationship with quality-of-life measures: A national study of New Zea-
landers. Journal of Gambling Issues, 24, 33–53.
Louderback, E. R., LaPlante, D. A., Currie, S. R., & Nelson, S. E. (2021). Developing and validating
lower risk online gambling thresholds with actual bettor data from a major internet gambling opera-
tor. Psychology of Addictive Behaviors, 35(8), 921–938.
Luquiens, A., Tanguy, M. L., Benyamina, A., Lagadec, M., Aubin, H. J., & Reynaud, M. (2016). Track-
ing online poker problem gamblers with player account-based gambling data only. International
Journal of Methods in Psychiatric Research, 25(4), 333–342.
Mora-Salgueiro, J., García-Estela, A., Hogg, B., Angarita-Osorio, N., Amann, B. L., Carlbring, P., Jiménez-
Murcia, S., Pérez-Sola, V., & Colom, F. (2021). The prevalence and clinical and sociodemographic
factors of problem online gambling: A systematic review. Journal of Gambling Studies, 37, 899–926.
Murch, W. S., Kairouz, S., Dauphinais, S., Picard, E., Costes, J. M., & French, M. (2023). Using
machine learning to retrospectively predict self-reported gambling problems in Quebec. Addiction,
118(8), 1569–1578.
Nagelkerke, N. J. (1991). A note on a general definition of the coefficient of determination. Biometrika,
78(3), 691–692.
Nower, L., & Blaszczynski, A. (2006a). Characteristics and gender differences among self-excluded
casino problem gamblers: Missouri data. Journal of Gambling Studies, 22, 81–99.
Nower, L., & Blaszczynski, A. (2006b). Impulsivity and pathological gambling: A descriptive model.
International Gambling Studies, 6(1), 61–75.
Pedregosa, F., Varoquaux, G., Gramfort, A., Michel, V., Thirion, B., Grisel, O., & Duchesnay, E. (2011).
Scikit-learn: Machine learning in Python. Journal of Machine Learning Research, 12, 2825–2830.
Percy, C., França, M., Dragičević, S., & d’Avila Garcez, A. (2016). Predicting online gambling self-
exclusion: An analysis of the performance of supervised machine learning models. International
Gambling Studies, 16(2), 193–210.
Perrot, B., Hardouin, J. B., Thiabaud, E., Saillard, A., Grall-Bronnec, M., & Challet-Bouju, G. (2022).
Development and validation of a prediction model for online gambling problems based on players’
account data. Journal of Behavioral Addictions, 11(3), 874–889.
Raylu, N., & Oei, T. P. (2004). Role of culture in gambling and problem gambling. Clinical Psychology
Review, 23(8), 1087–1114.
Schell, C., Godinho, A., & Cunningham, J. A. (2021). Examining change in self-reported gambling
measures over time as related to socially desirable responding bias. Journal of Gambling Studies,
37(3), 1043–1054.
Secades-Villa, R., Martínez-Loredo, V., Grande-Gosende, A., & Fernández-Hermida, J. (2016). The rela-
tionship between impulsivity and problem gambling in adolescence. Frontiers in Psychology, 7, 1931.
Selin, J. (2019). National gambling policies and the containment of the EU’s politico-legal influence.
Nordic Studies on Alcohol and Drugs, 36(2), 77–90.
Siemens, J. C., & Kopp, S. W. (2011). The influence of online gambling environments on self-control.
Journal of Public Policy & Marketing, 30(2), 279–293.
Tabri, N., Xuereb, S., Cringle, N., & Clark, L. (2022). Associations between financial gambling motives,
gambling frequency and level of problem gambling: A meta-analytic review. Addiction, 117(3),
559–569.
1 3

International Journal of Mental Health and Addiction (2026) 24:981–1003 1003
Tomei, A., Tichelli, E., Ewering, N., Nunweiler-Hardegger, S., & Simon, O. (2015). A descriptive study
of gambling among emerging adult males in French-speaking Switzerland. Journal of Gambling
Studies, 31(3), 607–620.
Tomei, A., Petrovic, G., & Simon, O. (2022). Offline and online gambling in a Swiss emerging-adult
male population. Journal of Gambling Studies, 38(4), 1215–1228.
Tripepi, G., Jager, K. J., Dekker, F. W., & Zoccali, C. (2010). Selection bias and information bias in
clinical research. Nephron Clinical Practice, 115(2), c94–c99.
Turner, N. E., Jain, U., Spence, W., & Zangeneh, M. (2008). Pathways to pathological gambling: Com-
ponent analysis of variables related to pathological gambling. International Gambling Studies,
8(3), 281–298.
Williams, R. J., Connolly, D., Wood, R. T., & Nowatzki, N. R. (2006). Gambling and problem gambling in a
sample of university students. Journal of Gambling Issues, 16, 1–14.
Williams, R. J., Leonard, C. A., Belanger, Y. D., Christensen, D. R., El-Guebaly, N., Hodgins, D. C., & Ste-
vens, R. M. (2021). Gambling and problem gambling in Canada in 2018: Prevalence and changes since
2002. Canadian Journal of Psychiatry, 66(5), 485–494.
Zaykin, D. V. (2011). Optimally weighted Z-test is a powerful method for combining probabilities in meta-
analysis. Journal of Evolutionary Biology, 24(8), 1836–1841.
Publisher’s Note Springer Nature remains neutral with regard to jurisdictional claims in published maps and
institutional affiliations.
Authors and Affiliations
Niklas Hopfgartner1 · Michael Auer1 · Denis Helic2 · Mark D. Griffiths3
*
Mark D. Griffiths
mark.griffiths@ntu.ac.uk
Niklas Hopfgartner
n.hopfgartner@neccton.com
Michael Auer
m.auer@neccton.com
Denis Helic
dhelic@tugraz.at
1 Neccton GmbH, Davidgasse 5, 7052 Müllendorf, Austria
2 Institute of Interactive Systems and Data Science, Graz University of Technology, Sandgasse
36/III, 8010 Graz, Austria
3 International Gaming Research Unit, Psychology Department, Nottingham Trent University, 50
Shakespeare Street, Nottingham NG1 4FQ, UK
1 3