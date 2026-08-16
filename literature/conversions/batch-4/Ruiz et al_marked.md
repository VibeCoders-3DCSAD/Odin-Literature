---
conversion_metadata:
  converted_at: "2026-07-21T08:23:30Z"
  converter_tool: "markitdown"
  converter_version: "0.1.6"
  source_pdf: "Ruiz et al.pdf"
  source_pdf_sha256: "2f7ca7250ed3c652ecd965718691d7d75b0da247509b74a9922d078f185e6170"
  page_count: 40
  markdown_char_count: 228752
---

<!-- PAGE-AWARE EXTRACTION (via pdfminer.six) -->

<!-- PAGE 1 -->

Ruiz, Mark Gerald C.; Miral, Ramona Maria L.; Rivera, John Paolo R.

Working Paper
Election-year stimuli and economic performance: Evidence
from a macroeconometric model of the Philippines

PIDS Discussion Paper Series, No. 2025-60

Provided in Cooperation with:
Philippine Institute for Development Studies (PIDS), Philippines

Suggested Citation: Ruiz, Mark Gerald C.; Miral, Ramona Maria L.; Rivera, John Paolo R. (2025) :
Election-year stimuli and economic performance: Evidence from a macroeconometric model of the
Philippines, PIDS Discussion Paper Series, No. 2025-60, Philippine Institute for Development Studies
(PIDS), Quezon City,
https://doi.org/10.62986/dp2025.60

This Version is available at:
https://hdl.handle.net/10419/339140

Standard-Nutzungsbedingungen:

Terms of use:

Die Dokumente auf EconStor dürfen zu eigenen wissenschaftlichen
Zwecken und zum Privatgebrauch gespeichert und kopiert werden.

Documents in EconStor may be saved and copied for your personal
and scholarly purposes.

Sie dürfen die Dokumente nicht für öffentliche oder kommerzielle
Zwecke vervielfältigen, öffentlich ausstellen, öffentlich zugänglich
machen, vertreiben oder anderweitig nutzen.

You are not to copy documents for public or commercial purposes, to
exhibit the documents publicly, to make them publicly available on the
internet, or to distribute or otherwise use the documents in public.

Sofern die Verfasser die Dokumente unter Open-Content-Lizenzen
(insbesondere CC-Lizenzen) zur Verfügung gestellt haben sollten,
gelten abweichend von diesen Nutzungsbedingungen die in der dort
genannten Lizenz gewährten Nutzungsrechte.

If the documents have been made available under an Open Content
Licence (especially Creative Commons Licences), you may exercise
further usage rights as specified in the indicated licence.

---

<!-- PAGE 2 -->

5
2
0
2
r
e
b
m
e
c
e
D

,

0
6
-
5
2
0
2

.

o
N

S
E
I
R
E
S
R
E
P
A
P
N
O
S
S
U
C
S
D

I

I

Election-Year Stimuli and Economic 
Performance: Evidence from a 
Macroeconometric Model of 
the Philippines

Mark Gerald C. Ruiz, Ramona Maria L. Miral, and
John Paolo R. Rivera

The PIDS Discussion Paper Series constitutes studies that are preliminary and subject to further 
revisions. They are posted on the PIDS website for purposes of soliciting comments and 
suggestions for further refinements. The studies under the Series are unedited and unreviewed. 
The views and opinions expressed are those of the author(s) and do not necessarily reflect 
those of the Institute. The Institute allows citation and quotation of the paper as long as proper 
attribution is made.

CONTACT US:
RESEARCH INFORMATION DEPARTMENT
Philippine Institute for Development Studies

18th Floor, Three Cyberpod Centris - North Tower
EDSA corner Quezon Avenue, Quezon City, Philippines

https://www.pids.gov.ph

publications@pids.gov.ph

(+632) 8877-4000

---

<!-- PAGE 3 -->

Election-Year Stimuli and Economic Performance:  
Evidence from a Macroeconometric Model of the Philippines

Mark Gerald C. Ruiz 
Ramona Maria L. Miral 
John Paolo R. Rivera

PHILIPPINE INSTITUTE FOR DEVELOPMENT STUDIES

08 November 2025

---

<!-- PAGE 4 -->

Abstract

We  evaluated  the  transmission  of  election  shocks  in  the  Philippine  economy  using  an 
augmented macroeconometric model that integrates political business cycle (PBC) dynamics 
into  the  country’s  macroeconomic  framework.  Building  upon  the  model  developed  by 
Debuque-Gonzales and Corpus (2023, 2024), quarterly data from 2002 to 2023 were utilized 
to  simulate  the  effects  of  election-induced  fiscal  and  private  sector  behavior  on  key 
macroeconomic  variables,  namely  private  consumption,  employment,  investment,  and 
government  consumption.  Results  reveal  that  election  years  generate  short-term,  demand-
driven  expansions,  fueled  by  heightened  government  spending,  campaign  activities,  and 
temporary job creation. However, these effects are transitory, with economic activity reverting 
near  baseline  levels  post-election  as  fiscal  impulses  fade.  Findings  align  with  established 
literature on political budget cycles, confirming that election-driven growth is cyclical rather 
than structural, and may induce inefficiencies in expenditure allocation and fiscal discipline. 
The study highlights the need for institutional reforms, fiscal transparency, and counter-cyclical 
policies to mitigate  volatility  and  promote long-term  stability. Finally, limitations related to 
model stability, pandemic disruptions, and evolving post-COVID economic structures suggest 
avenues for recalibrating and rewriting the macroeconometric model for future applications.

Keywords: election shocks; macroeconometric modeling, political business cycles

JEL Classification: C51, E62

i

---

<!-- PAGE 5 -->

Table of Contents

1. Introduction .................................................................................................................... 1 
2. Literature review ............................................................................................................ 2 
2.1. Historical evolution of macroeconometric models ....................................................... 2 
2.2. Existing macroeconometric models in the Philippines ................................................. 3 
2.3. Economic impacts of from election activities ............................................................... 4 
2.4. Political business cycles ............................................................................................. 4 
2.5. Model enhancements ................................................................................................. 5 
2.6. Research gap ............................................................................................................. 5 
3. Methodology ................................................................................................................... 6 
3.1. Conceptual framework ................................................................................................ 6 
3.2. Operational framework ............................................................................................... 6 
3.3. Estimation ................................................................................................................... 8 
4. Results and discussion ................................................................................................. 9 
4.1. Model evaluation ........................................................................................................ 9 
4.2. Impact analysis of election-related spending shock .................................................. 13 
5. Ways forward ............................................................................................................... 19 
5.1. Conclusions .............................................................................................................. 19 
5.2. Policy recommendations ........................................................................................... 20 
5.3. Limitations and areas for future studies .................................................................... 21 
6. References.................................................................................................................... 22 
7. Appendix ...................................................................................................................... 28

List of Figures 
Figure 1. Model structure ...................................................................................................... 6 
Figure 2. In-sample simulations .......................................................................................... 10 
Figure 3. Election spending shock scenario ........................................................................ 17

List of Tables 
Table 1. Model equations and variables ................................................................................ 7 
Table 2. Evaluation of in-sample forecast accuracy, 2021Q1-2023Q4 ................................ 12 
Table 3. Validation of empirical results ................................................................................ 19 
Table 4. Policy recommendations ....................................................................................... 20

ii

---

<!-- PAGE 6 -->

Asian Development Bank 
Augmented Dickey–Fuller 
Akaike Information Criterion 
Autoregressive Distributed Lag 
Bureau of Internal Revenue 
Bureau of Customs 
Bangko Sentral ng Pilipinas  
Commission on Audit

List of Abbreviations 
ADB 
ADF 
AIC 
ARDL 
BIR 
BOC 
BSP 
COA 
COMELEC  Commission on Elections 
COVID-19  Coronavirus Disease 2019 
CPI 
CPBRD 
CUSUM 
DBM 
DEPDev 
DLSU 
DOH 
DSGE 
ECM 
FDI 
FRB 
GDP 
GE 
GFC 
GMM 
HANK 
IMF 
IS-LM 
MAE 
MAPE 
MEM 
NBER 
NEDA 
NG 
OECD 
OLG 
PBC 
PIDS 
PPP 
PSA 
RBA 
SVAR 
VAR 
ADB

Consumer Price Index 
Congressional Policy and Budget Research Department 
Cumulative Sum 
Department of Budget and Management 
Department of Economy, Planning, and Development  
De La Salle University 
Department of Health 
Dynamic Stochastic General Equilibrium 
Error Correction Model 
Foreign Direct Investment 
Federal Reserve Bank 
Gross Domestic Product 
General Equilibrium 
Global Financial Crisis 
Generalized Method of Moments 
Heterogeneous Agent New Keynesian 
International Monetary Fund 
Investment-Saving and Liquidity Preference-Money Supply 
Mean Absolute Error 
Mean Absolute Percentage Error 
Macroeconometric Model 
National Bureau of Economic Research 
National Economic and Development Authority 
National Government 
Organisation for Economic Co-operation and Development 
Overlapping Generations 
Political Business Cycle(s) 
Philippine Institute for Development Studies 
Public-Private Partnership 
Philippine Statistics Authority 
Reserve Bank of Australia 
Structural Vector Autoregression 
Vector Autoregression 
Asian Development Bank

iii

---

<!-- PAGE 7 -->

Election-Year Stimuli and Economic Performance: Evidence from a 
Macroeconometric Model of the Philippines

Mark Gerald C. Ruiz1, Ramona Maria L. Miral2, and John Paolo R. Rivera3

1. Introduction

The Philippine economy has historically shown fluctuations during election years, distinct from 
non-election periods, driven by increased government expenditures, heightened consumer and 
business  activity,  and  shifts  in  investor  confidence  (Ochave  2025;  Habito  2013;  Landingin 
2010).  Elections,  being  periodic  events  when  political  and  economic  forces  interact,  impact 
macroeconomic performance through economic shocks that are transmitted to changes in fiscal 
policy, public infrastructure spending, capital flows, and overall market sentiment (de Haan et 
al. 2023). However, this growth can be unsustainable if it is not driven by structural economic 
improvements  (Curtis  2023).  Thus,  such  periods  also  introduce  uncertainty,  affecting 
inflationary trends, foreign direct investment (FDI) inflows, and long-term fiscal sustainability 
(Azzimonti 2024; Goodell et al. 2020; Gupta et al 2015).

The year 2025, being an election year in the Philippines (i.e., midterm elections4), differs from 
non-election years. On one hand, election years often see an uptick in gross domestic product 
(GDP) growth due to increased fiscal expenditures, particularly on infrastructure projects (i.e., 
to  demonstrate  accomplishments  and  gain  voter  support,  governments  often  accelerate 
infrastructure programs in the months leading  up  to  an  election), social assistance programs 
(i.e., increased funding for social programs, subsidies, and cash transfers is common to bolster 
political  goodwill),  and  election-related  administrative  spending  (i.e.,  budget  for  electoral 
processes,  including  voter  registration,  election  security,  and  logistics,  contributes  to 
government spending growth) (Das et al. 2025; Olano 2019). Also, the government tends to 
frontload disbursements in the run-up to elections, driving short-term demand in the economy 
(Frieden  2020).  Succeeding,  post-election  years  often  see  fiscal  tightening  as  governments 
attempt  to  curb  deficits  and  adhere  to  fiscal  discipline,  leading  to  a  slowdown  in  public 
investment (Tannous 2024).

Consequently,  the  increased  liquidity  in  the  economy  during  election  years,  stemming  from 
government  expenditures  and  campaign-related  spending,  can  contribute  to  higher  inflation 
(Kladakis and Skouralis 2024). The surge in money supply, combined with increased consumer 
demand, can lead to price increases, particularly in food, services, and transportation. Moreover, 
if  the  government  resorts  to  deficit  spending  to  finance  election-related  expenditures, 
inflationary  pressures  may  persist  beyond  the  election  period.  While  GDP  growth  may 
temporarily  rise,  election-related  uncertainty  often  dampens  investor  confidence  (Azzimonti 
2024; Goodell et al. 2020; Gupta et al 2015). FDI inflows tend to slow during election years as 
businesses  and  investors  adopt  a  wait-and-see  approach,  assessing  potential  shifts  in  policy, 
regulatory frameworks, and political stability (Jahn and Stricker 2022). Political transitions can 
lead  to  concerns  over  changes  in  business  conditions,  tax  regimes,  and  contract  security, 
prompting  investors  to  delay  commitments  or  divert  capital  to  more  stable  environments

1 Research Specialist, Philippine Institute for Development Studies. Email: mruiz@pids.gov.ph   
2 Research Specialist, Philippine Institute for Development Studies. Email: rmiral@pids.gov.ph  
3 Senior Research Fellow, Philippine Institute for Development Studies. Email: jrivera@pids.gov.ph   
4 In the Philippine context, a midterm election refers to a national and local election held halfway through the six-year term of the 
incumbent  president. It  takes  place  three  years  after  a  presidential election  and  serves  as  a  political barometer  of the sitting 
administration’s performance and public approval.

1

---

<!-- PAGE 8 -->

(Boyles 2022). The impact on FDI flows depends on the perceived credibility of institutions 
and the policy stance of incoming leadership (Kapas 2020).

On the other hand, election years also see significant uptick in private sector and household 
expenditures (Olano 2019). Political campaigns inject significant liquidity into the  economy 
through salaries, advertising expenditures, and logistics, leading to higher consumer spending, 
particularly  in  services,  retail,  and  transport.  Likewise,  some  businesses  increase  spending 
during  election  years,  particularly  those  linked  to  election-related  industries  such  as  media, 
advertising, and printing (Le et al. 2024). However, firms with long-term investment plans may 
delay  major  capital  expenditures  due  to  policy  uncertainty  and  a  wait-and-see  behavior 
(Azzimonti 2024; Goodell et al. 2020; Gupta et al 2015).

Given the May 2025 Philippine midterm elections, our study is relevant in providing empirical 
insights  on  the  extent  of  election-driven  economic  stimulation.  While  election-related 
government  expenditures  may  create  short-term  growth,  concerns  remain  about  inflationary 
pressures,  fiscal  sustainability,  and  economic  volatility  post-election.  Moreover,  investor 
sentiment (both domestic and foreign) can be swayed by electoral uncertainty, impacting capital 
inflows and business decisions.

Given the abovementioned backdrop and the cyclical nature of these economic dynamics, we 
inquire  on  how  election-related  shocks  are 
the  Philippine 
macroeconomy?  In  addressing  this  research  question,  we  are  guided  by  an  overarching 
objective to integrate election variables into a macroeconometric model for the Philippines. 
Supporting this are the following specific objectives:  
1.  To estimate the magnitude of election-year stimulus on GDP growth and whether it leads

transmitted

through

to sustained economic benefits or short-term artificial growth;

2.  To estimate the extent to which inflation is influenced by election-related liquidity surges,

private sector expenditures, and government spending patterns;

3.  To evaluate how election-induced uncertainty affects FDI inflows and business confidence;

and

4.  To  generate  policy  recommendations  on  how  the  government  can  balance  economic

stimulus with long-term stability.

By  evaluating  the  transmission  of  election  shocks  through  a  macroeconometric  framework 
developed  by  Debuque-Gonzales  and  Corpus  (2023),  we  contribute  to  evidence-based 
policymaking,  helping  stakeholders  better  understand  the  economic  implications  of  election 
cycles.  Also,  by  offering  a  structured  analysis  of  these  effects,  we  contribute  to  informed 
decision-making  for  policymakers,  economists,  and  business 
the 
complexities  of  election-year  economic  shifts  and  in  anticipating  both  short-term  economic 
boosts  and  potential  long-term  distortions.  Findings  can  serve  as  a  basis  for  formulating 
strategies to mitigate economic risks while leveraging potential benefits during election periods.

leaders  navigating

2. Literature review

2.1. Historical evolution of macroeconometric models

The  origins  of  macroeconometric  modeling  trace  back  to  early  macroeconomic  thought  on 
general equilibrium (GE) theory, which introduced aggregate demand as an analytical variable 
distinct from aggregate supply. Keynes (1936) challenged the classical notion of self-correcting 
markets  by  arguing  that  economies  could  settle  into  equilibrium  with  involuntary

2

---

<!-- PAGE 9 -->

unemployment,  requiring  government  intervention  to  stimulate  demand.  Hicks  (1937) 
formalized this interaction in the IS-LM (investment-saving and liquidity preference-money 
supply) framework, later integrated into the “neoclassical synthesis” that combined long-run 
neoclassical principles with short-run Keynesian dynamics (Samuelson 1948).

The post-war period saw the rise of large-scale econometric models, spurred by the Cowles 
Commission’s5 pioneering work in statistical estimation and model testing. A major turning 
point came with the Lucas Critique6 (Lucas 1976). This critique spurred the development of 
micro-founded models grounded in rational expectations, including the policy-ineffectiveness 
proposition of Sargent and Wallace (1975).

In subsequent decades, macroeconomic modeling evolved toward Dynamic Stochastic General 
Equilibrium  (DSGE)  frameworks  that  explicitly  incorporate  intertemporal  optimization  and 
stochastic shocks (Kydland and Prescott 1982; Smets and Wouters 2007). Later refinements 
introduced New Keynesian DSGE models that allow for nominal rigidities (Calvo 1983) and 
Heterogeneous Agent New Keynesian (HANK) models that account for distributional effects 
(Kaplan et al. 2018). Despite their sophistication, DSGE models faced criticism for failing to 
anticipate  the  2008  Global  Financial  Crisis  (Hendry  and  Muellbauer  2018;  Stiglitz  2018). 
Contemporary  work  thus  emphasizes  more  flexible  and  data-driven  macroeconometric 
approaches  integrating  behavioral  expectations,  non-linearities,  and  institutional  factors 
(Blanchard 2016; Guerrieri and Iacoviello 2017; Albuquerque et al. 2025).

2.2. Existing macroeconometric models in the Philippines

The  Philippines’  experience  with  macroeconometric  modeling  has  evolved  alongside  global 
developments.  Early  models  were  developed  by  academic  institutions7,  multilateral 
organizations8,  and  government  agencies  such  as  the  Philippine  Institute  for  Development 
Studies (PIDS), the Department of Economy, Planning and Development (DEPDev9), and the 
Bangko Sentral ng Pilipinas (BSP10). These models, often medium-scale and demand-driven, 
were  designed  to  inform  fiscal  and  monetary  policy  by  simulating  relationships  among 
aggregate  output,  consumption,  investment,  and  inflation  (Debuque-Gonzales  and  Corpus 
2023,  2024).  For  a  historical  background  of  earlier  macroeconometric  models  in  the 
Philippines, Debuque-Gonzales and Corpus (2023, 2024) provided a detailed discussion from 
the annual macroeconometric model (MEM) by Constantino and Yap (1988), Constantino et

5  Focuses  on  linking  economic  theory  to  mathematics  and  statistics;  its  advances  in  economics  involved  the  creation  and 
integration of GE theory and econometrics. 
6 A theory in macroeconomics that criticizes the use of past data to predict how new economic policies will affect the economy. It 
argued that people's expectations and behavior change in response to new economic policies. Therefore, using historical data to 
predict the effects of new policies is not reliable. Moreover, it is a fundamental criticism of empirical economics, which questions 
its ability to model, test, or predict the economy (Stanley 2000).  
7 For instance, De La Salle University (DLSU) has developed multiple macroeconometric models of the Philippine economy(i.e., 
ANIMO model, Quarterly model, Simultaneous equation system, OLG model). These models are used to forecast the economy 
and help inform policy decisions. For more information, see https://www.dlsu-aki.com/research-programs-and-projects.html. Also, 
Rodriguez and Briones (2002) built the quarterly Ateneo Macroeconomic and Forecasting Model (AMFM) based on the short-run 
version of the Murphy model of Australia.   
8 The Asian Development Bank (ADB) developed macroeconometric models of select ADB member economies for forecasting 
and policy simulation. The model designed for the Philippines (Cagas et al. 2006; Ducanes et al. 2005) paid special attention to 
the 
See 
https://www.adb.org/sites/default/files/publication/28191/wp062.pdf.   
9 Formerly known as the National Economic and Development Authority (NEDA); the Philippine government agency responsible 
for  national  economic  planning,  policy  coordination,  and  monitoring  to  ensure  sustainable  development;  also  oversees  the 
approval of large projects, trade policies, and the efficient use of land and natural resources, working to link development planning 
with the national budget. Website: https://depdev.gov.ph/.    
10 The Policy Analysis Model for the Philippines (PAMPh) is a model used by the BSP to analyze the economy and guide monetary 
policy.  It  is  used  as  the  main  model  for  medium-term  forecasting  and  policy  analysis  (Alarcon  et  al.  2020).  See 
https://www.bsp.gov.ph/Sites/researchsite/Publications/BSP-Working-PaperSeries/WPS202012.pdf.

government

simulations.

enable

model

block

fiscal

the

to

of

3

---

<!-- PAGE 10 -->

al. (1980), Reyes and Yap (1993), Yap (2000) to more recent macroeconometric and forecasting 
model by Rodrigues and Briones (2002), structural MEM by Ducanes et al. (2005) and Cagas 
et  al.  (2006),  quarterly  macroeconometric  model  of  Bautista  et  al.  (2009),  annual  MEM  by 
Reyes et al. (2020),

Debuque-Gonzales and Corpus (2023, 2024) made a significant step toward systematizing this 
framework  using  robust  econometric  specifications.  These  models  align  with  international 
standards  by  employing  simultaneous  equations,  error-correction  mechanisms,  and 
cointegration analysis to  capture both short- and  long-run  dynamics. However, political  and 
institutional  shocks,  particularly  election-induced  fluctuations,  remain  underexplored  within 
these models. We build on this gap by integrating election shocks as exogenous or structural 
disturbances that influence fiscal behavior, investor confidence, and macroeconomic outcomes.

2.3. Economic impacts of from election activities

Substantial scholarly literature has explored the two-way relationship between elections and the 
economy. On one hand, macroeconomic conditions affect voting behavior, known as economic 
voting, where voters reward or punish incumbents based on perceived economic performance 
(Bello 2021; Guntermann et al. 2021; Leigh 2004; Alvarez et al. 1999; Fiorina 1978).

Conversely, elections influence the economy through various channels. The political business 
cycle  literature  suggests  that  incumbents  manipulate  fiscal  or  monetary  tools  to  enhance 
reelection  prospects  (Schultz  1995;  Rogoff  and  Sibert  1988).  Empirical  studies  show  that 
election years often coincide with surges in public expenditures, shifts in credit conditions, or 
changes in money  supply  (Kolios, 2019; Peters,  2010).  Recent  cross-country  evidence from 
Nguyen and Tran (2023) confirmed that incumbents in 91 emerging and developing economies 
expanded government spending before and during elections, then contracted it afterward.

Sector-specific analyses corroborate these macro-level findings. Broni et al. (2019) observed 
higher bank returns during Ghanaian election years as citizens increased deposits amid political 
uncertainty, while Tabash et al. (2024) found that the 2018 Pakistan general election positively 
affected  stock  market  performance.  Despite  this  broad  literature,  there  remains  limited 
empirical  research  assessing  the  multi-sectoral  macroeconomic  impact  of  elections  in  the 
Philippine context, creating space for our contribution.

2.4. Political business cycles

The  concept  of  political  business  cycles  (PBCs)  provides  the  theoretical  foundation  for 
analyzing  election  shocks.  PBC  models  posit  that  elected  officials,  seeking  reelection, 
manipulate  fiscal  and  monetary  levers  to  generate  temporary  economic  upswings  before 
elections (Schultz 1995; Rogoff and Sibert 1988; Nordhaus 1975). Subsequent empirical work 
quantified  these  effects  such  as  that  of  Coulombe  (2021)  who  identified  ideological  and 
electoral drivers of fiscal expansions in OECD countries, as well as Cipullo and Reslow (2022) 
who documented politically motivated GDP forecast optimism in advanced economies.

These findings suggest that election shocks transmit through multiple macroeconomic channels 
(i.e.,  government  spending,  inflation  expectations,  investor  sentiment),  all  of  which  can  be 
modeled within a macroeconometric framework to understand cyclical fluctuations in output 
and employment.

4

---

<!-- PAGE 11 -->

2.4. Econometric approaches to modeling election shocks

Modeling  election  shocks  requires  distinguishing  between  anticipated  and  unanticipated 
components (Adams and Barrett 2023; Mertens and Ravn 2012). Anticipated shocks are often 
captured  using  dummy  variables  representing  election  periods  to  model  systematic  policy 
changes,  particularly  fiscal  expansions  (Ivanovic  et  al.  2023;  Van  Dalen  and  Swank  1996). 
Meanwhile, unanticipated shocks, such as surprise election outcomes or abrupt policy shifts, 
are  typically  modeled  using  Structural  Vector  Autoregression  (SVAR)  frameworks,  which 
isolate the dynamic responses of  key variables to  unexpected  shocks (Gambetti 2021; Hoke 
2019). These econometric techniques are  essential in quantifying how  election cycles affect 
aggregate demand, investment, and inflation through different transmission mechanisms.

2.5. Model enhancements

Integrating political and institutional variables into macroeconometric models enhances both 
model calibration and policy design. From a modeling perspective, the inclusion of political 
variables  allows  for  more  precise  calibration,  improving  the  reliability  of  simulations  and 
forecasts (Martinoli et al. 2022). From a policy standpoint, understanding election-driven cycles 
supports the formulation of counter-cyclical fiscal policies to offset inflationary pressures or 
post-election  slowdowns  (Jalles  et  al.  2023;  IMF  2023).  This  integrated  approach  bridges 
empirical  modeling  with  practical  fiscal  governance,  making  macroeconometric  tools  more 
responsive to real-world political dynamics.

2.6. Research gap

Despite an extensive body of scholarship on PBCs and macroeconomic modeling, there remains 
a  dearth  of  studies  that  systematically  examines  how  election  shocks  transmit  through  the 
Philippine  economy  within  an  econometric  framework.  Existing  studies,  both  local  and 
international,  tend  to  focus  on  short-term  fiscal  dynamics,  such  as  pre-election  increases  in 
government  disbursements  or  post-election  fiscal  adjustments,  or  on  sector-specific  impacts 
like financial markets, inflation, or employment. These fragmented analyses, while valuable, 
fall  short  of  capturing  the  economy-wide  propagation  mechanisms  through  which  election-
related disturbances affect aggregate output, consumption, investment, and external accounts.

In the Philippines, most empirical work has emphasized descriptive or correlational approaches 
rather  than  model-based  simulations  that  integrate  behavioral  and  structural  relationships 
among macroeconomic variables. It lacks a comprehensive, empirically estimated framework 
that can quantify how political cycles, through fiscal impulses, policy uncertainty, or investor 
sentiment, interact with the broader macroeconomic system. This limits policymakers’ ability 
to distinguish between temporary election-induced booms and sustainable growth drivers.

Our  study  addresses  this  analytical  and  methodological  gap  by  developing  an  augmented 
macroeconometric model for the Philippines, building from the work of Debuque-Gonzales and 
Corpus (2023, 2024), that explicitly incorporates election shocks. This enhancement allows for 
a  more  rigorous  understanding  of  the  timing,  magnitude,  and  persistence  of  election-related 
effects  on  macroeconomic  variables.  By  embedding  electoral  cycles  as  exogenous  shocks 
within  the  structural  equations  of  the  model,  we  can  simulate  how  fiscal  behavior,  private 
investment,  and  external  balances  respond  under  different  election  scenarios.  Hence,  we 
contribute  not  only  to  the  empirical  literature  on  political  business  cycles  but  also  to 
macroeconomic  policy  design,  providing  evidence-based  insights  into  how  political  events

5

---

<!-- PAGE 12 -->

shape  cyclical  fluctuations,  fiscal  sustainability,  and  long-term  growth  trajectories.  It  also 
extends  the  capability  of  existing  Philippine  macroeconometric  frameworks  from  merely 
describing  economic  trends  to  explaining  and  forecasting  politically  driven  economic 
dynamics. This is a critical advancement for planning and fiscal management in the country.

3. Methodology

3.1. Conceptual framework

traditional  macroeconometric  models

We build on the framework and model developed by Debuque-Gonzales and Corpus (2023, 
2024)  anchored  on 
instead  of  micro-founded 
macroeconomic models in response to the Lucas Crique. We continue to align with an empirical 
approach to analyzing the transmission mechanism of election shocks to  the macroeconomy 
following Hendry (2020) citing the continued use of econometric approach to macroeconomic 
analysis like the Federal Reserve Bank (FRB), the Norges Bank, the Reserve Bank of Australia 
(RBA), the Bank of Canada, and the European Central Bank employing non-DSGE models. 
Debuque-Gonzales and Corpus (2023, 2024) comprehensively reviewed the justifications for 
the  continued  preference  for  empirical  approaches.  By  integrating  election  shocks  into  the 
macroeconometric  model,  we  quantify  how  election  cycles  influence  key  macroeconomic 
indicators as seen in Figure 1.

Figure 1. Model structure

Note:  Orange  boxes  denote  the  exogenous  variables  in  the  model.  Solid  blue  lines  represent  behavioral 
relationships, while broken lines represent identities.   
Source: Debuque-Gonzales and Corpus (2023, p. 21); Debuque-Gonzales and Corpus (2024, p. 6).

3.2. Operational framework

Following Debuque-Gonzales and Corpus (2023, 2024), we also adapted a pragmatic approach, 
where the objective was to build a policy model guided by economic theory but can fit data

6

---

<!-- PAGE 13 -->

reasonably well. We emphasized on usability, tractability, and ease of maintenance, apart from 
model  validity  and  robustness.  Table  1  shows  the  behavioral  equations  representing  the 
macroeconomic variables in Figure 1.

Table 1. Model equations and variables

bl

oil

US

rice

t10y

t91d

= US Consumer Price Index

= World price of oil 
  = Retail price of rice

= Real 10-year Treasury rate 
 = Real 91-day Treasury rate 
 = 10-year Treasury rate

Variables 
C = Household consumption 
CPI = Consumer Price Index 
CPI
D = National Government (NG) debt (nominal) 
D
D
 = Domestic NG debt (nominal) 
F 
D
= Foreign NG debt (nominal) 
emp = Employment rate 
G = Government consumption  
I = Investment 
M = Imports 
NX = Net exports 
p
p
PB = Primary balance  
Y
P
 = GDP de�lator 
bl
r
 = Bank lending rate 
cb
r
 = BSP policy rate 
dd
r
 = Effective interest rate on domestic debt 
df
r
 = Effective interest rate on foreign debt 
RES = Debt residual (nominal) 
rr
 = Real bank lending rate 
rr
rr
t10y
r
t10yUS
r
t91d
r
 = 91-day Treasury rate 
RV = Total revenues (nominal) 
RV
RV
RV
RV
X = exports 
XP = Total expenditure (nominal) 
XP
 = Domestic interest payments (nominal) 
XP
 = Foreign interest payments (nominal) 
XP
 = Interest payments (nominal) 
XP
 = Primary expenditure (nominal) 
xr = nominal peso-dollar exchange rate 
xrr = real peso-dollar exchange rate 
Y = GDP 
YD = disposable income 
N
Y
 = nominal GDP 
WORLD
Y
𝛼𝛼= Share of domestic debt in total 
𝜋𝜋 = in�lation rate 
𝜋𝜋
𝑒𝑒
𝜋𝜋𝑡𝑡

= Internal tax revenues (nominal) 
 = Customs revenues (nominal)

= Non-tax revenues (nominal) 
 = Tax revenues (nominal)

= in�lation target (midpoint) 
 = expected in�lation rate

= US 10-year Treasury rate

= World GDP

TXBOC

TXBIR

NTX

IND

INT

INF

PR

TX

𝑇𝑇

)

𝑒𝑒
𝑒𝑒
− 𝜋𝜋𝑡𝑡
, 𝜋𝜋𝑡𝑡
𝑒𝑒
𝑒𝑒
), 𝜋𝜋𝑡𝑡
− 𝜋𝜋𝑡𝑡
)

Equations 
Domestic demand 
𝑏𝑏𝑏𝑏
log 𝐶𝐶𝑡𝑡 = 𝑓𝑓(log(𝑌𝑌𝐷𝐷𝑡𝑡), 𝑒𝑒𝑒𝑒𝑝𝑝𝑡𝑡, 𝑟𝑟𝑡𝑡
𝑏𝑏𝑏𝑏
log (𝐼𝐼𝑡𝑡) = 𝑓𝑓(log(𝑌𝑌𝑡𝑡) , Δ(𝑟𝑟𝑡𝑡
𝑃𝑃𝑃𝑃
log 𝐺𝐺𝑡𝑡 = 𝑓𝑓(𝑋𝑋𝑃𝑃𝑡𝑡
) 
log 𝑀𝑀𝑡𝑡 = 𝑓𝑓(𝐼𝐼𝑡𝑡, 𝑋𝑋𝑡𝑡) 
𝑌𝑌𝑡𝑡 ≡ 𝐶𝐶𝑡𝑡 + 𝐼𝐼𝑡𝑡 + 𝐺𝐺𝑡𝑡 + 𝑋𝑋𝑡𝑡 − 𝑀𝑀𝑡𝑡 
𝑌𝑌𝐷𝐷𝑡𝑡 ≡ 𝑌𝑌𝑡𝑡 − 𝑅𝑅𝑉𝑉𝑡𝑡
𝑌𝑌
) = 𝑓𝑓(log(𝐶𝐶𝑃𝑃𝐼𝐼𝑡𝑡))  
log(𝑃𝑃𝑡𝑡
𝑌𝑌
𝑁𝑁
≡ 𝑃𝑃𝑡𝑡
𝑌𝑌𝑡𝑡

𝑌𝑌𝑡𝑡

𝑇𝑇𝑇𝑇𝑇𝑇𝑇𝑇𝑃𝑃

𝑊𝑊𝑊𝑊𝑃𝑃𝑊𝑊𝑊𝑊

Trade block 
log(𝑋𝑋𝑡𝑡) = 𝑓𝑓(log (𝑌𝑌𝑡𝑡
log (𝑀𝑀𝑡𝑡) = 𝑓𝑓(log(𝐼𝐼𝑡𝑡), log(𝑋𝑋𝑡𝑡))   
𝑁𝑁𝑋𝑋𝑡𝑡 ≡ 𝑋𝑋𝑡𝑡 − 𝑀𝑀𝑡𝑡

) , log(𝑥𝑥𝑟𝑟𝑟𝑟𝑡𝑡))

Employment block 
𝑒𝑒𝑒𝑒𝑝𝑝𝑡𝑡 = 𝑓𝑓(𝑌𝑌𝑡𝑡)

Price block 
Δ log(𝐶𝐶𝑃𝑃𝐼𝐼𝑡𝑡) =
𝑓𝑓�Δlog�𝑝𝑝𝑡𝑡
𝜋𝜋𝑡𝑡 ≡ 100 �

𝑜𝑜𝑜𝑜𝑏𝑏

𝑟𝑟𝑜𝑜𝑟𝑟𝑒𝑒

� , Δ log�𝑝𝑝𝑡𝑡
𝐶𝐶𝑃𝑃𝑇𝑇𝑡𝑡
𝐶𝐶𝑃𝑃𝑇𝑇𝑡𝑡−4 − 1�

� , Δ log(𝐷𝐷𝐷𝐷𝑡𝑡) , Δ log(𝑥𝑥𝑟𝑟𝑡𝑡)�

)

)

𝑡𝑡91𝑑𝑑

Monetary block 
𝑇𝑇
𝑒𝑒
𝑟𝑟𝑏𝑏
= 𝑓𝑓(𝜋𝜋𝑡𝑡
𝑟𝑟𝑡𝑡
− 𝜋𝜋𝑡𝑡
𝑟𝑟𝑏𝑏
𝑡𝑡91𝑑𝑑
= 𝑓𝑓(𝑟𝑟𝑡𝑡
𝑟𝑟𝑡𝑡
𝑡𝑡10𝑦𝑦
= 𝑓𝑓(𝑟𝑟𝑡𝑡
𝑟𝑟𝑡𝑡
𝑡𝑡10𝑦𝑦
𝑏𝑏𝑏𝑏
𝑟𝑟𝑡𝑡
𝑟𝑟𝑟𝑟𝑡𝑡
𝑟𝑟𝑟𝑟𝑡𝑡
𝑏𝑏𝑏𝑏
𝑟𝑟𝑟𝑟𝑡𝑡

= 𝑓𝑓(𝑟𝑟𝑡𝑡
𝑡𝑡91𝑑𝑑
≡ 𝑟𝑟𝑡𝑡
≡ 𝑟𝑟𝑡𝑡
𝑏𝑏𝑏𝑏
≡ 𝑟𝑟𝑡𝑡

𝑡𝑡10𝑦𝑦

𝑡𝑡10𝑦𝑦

𝑡𝑡91𝑑𝑑

𝑒𝑒
, 𝑃𝑃𝐵𝐵𝑡𝑡/𝑌𝑌𝑡𝑡, 𝜋𝜋𝑡𝑡
𝑒𝑒
, 𝜋𝜋𝑡𝑡
) 
𝑒𝑒
, 𝜋𝜋𝑡𝑡
) 
− 𝜋𝜋𝑡𝑡 
− 𝜋𝜋𝑡𝑡

𝑈𝑈𝑈𝑈

− 𝜋𝜋𝑡𝑡 
𝐶𝐶𝑃𝑃𝐼𝐼𝑡𝑡
𝐶𝐶𝑃𝑃𝐼𝐼𝑡𝑡 � 
�   
𝑡𝑡10𝑦𝑦𝑈𝑈𝑈𝑈

𝑡𝑡10𝑦𝑦

𝑥𝑥𝑟𝑟𝑟𝑟𝑡𝑡 = 𝑥𝑥𝑟𝑟𝑡𝑡 �
𝑑𝑑𝑑𝑑
𝑟𝑟𝑡𝑡
𝑑𝑑𝑑𝑑
𝑟𝑟𝑡𝑡

= 𝑓𝑓�𝑟𝑟𝑡𝑡
= 𝑓𝑓�𝑟𝑟𝑡𝑡

, 𝐷𝐷𝑌𝑌𝑡𝑡�

𝑜𝑜𝑜𝑜𝑏𝑏

𝑇𝑇𝑁𝑁𝐼𝐼

𝑁𝑁𝑇𝑇𝑇𝑇

𝑇𝑇𝑇𝑇𝑇𝑇𝑊𝑊𝐶𝐶

), log(𝑥𝑥𝑟𝑟𝑡𝑡))

+ 𝑅𝑅𝑉𝑉𝑡𝑡
) = 𝑓𝑓(𝐷𝐷𝑌𝑌𝑡𝑡)   
𝑇𝑇𝑁𝑁𝑊𝑊
+ 𝑋𝑋𝑃𝑃𝑡𝑡
≡ 𝑋𝑋𝑃𝑃𝑡𝑡
𝑇𝑇𝑁𝑁𝑇𝑇
𝑃𝑃𝑃𝑃
+ 𝑋𝑋𝑃𝑃𝑡𝑡
𝑊𝑊
𝑑𝑑𝑑𝑑
× 𝐷𝐷𝑡𝑡−1
𝑑𝑑𝑑𝑑

Fiscal block 
𝑇𝑇𝑇𝑇𝑇𝑇𝑇𝑇𝑃𝑃
𝑁𝑁
log(𝑅𝑅𝑉𝑉𝑡𝑡
) = 𝑓𝑓(log(𝑌𝑌𝑡𝑡
))  
𝑌𝑌
𝑀𝑀𝑡𝑡), log(𝑝𝑝𝑡𝑡
log(𝑅𝑅𝑉𝑉𝑡𝑡
) = 𝑓𝑓 (log(𝑃𝑃𝑡𝑡
𝑁𝑁
log(𝑅𝑅𝑉𝑉𝑡𝑡
) = 𝑓𝑓(log(𝑌𝑌𝑡𝑡
))  
𝑇𝑇𝑇𝑇𝑇𝑇𝑊𝑊𝐶𝐶
𝑇𝑇𝑇𝑇
𝑇𝑇𝑇𝑇𝑇𝑇𝑇𝑇𝑃𝑃
𝑅𝑅𝑉𝑉𝑡𝑡
+ 𝑅𝑅𝑉𝑉𝑡𝑡
≡ 𝑅𝑅𝑉𝑉𝑡𝑡
𝑁𝑁𝑇𝑇𝑇𝑇
𝑇𝑇𝑇𝑇
𝑅𝑅𝑉𝑉𝑡𝑡 ≡ 𝑅𝑅𝑉𝑉𝑡𝑡
𝑃𝑃𝑃𝑃
log(𝑋𝑋𝑃𝑃𝑡𝑡
𝑇𝑇𝑁𝑁𝑇𝑇
𝑋𝑋𝑃𝑃𝑡𝑡
𝑋𝑋𝑃𝑃𝑡𝑡 ≡ 𝑋𝑋𝑃𝑃𝑡𝑡
𝑇𝑇𝑁𝑁𝑊𝑊
≡ 𝑟𝑟𝑡𝑡
𝑋𝑋𝑃𝑃𝑡𝑡
𝑥𝑥𝑟𝑟𝑡𝑡
𝑋𝑋𝑃𝑃𝑡𝑡
𝑥𝑥𝑟𝑟𝑡𝑡−1� 𝑟𝑟𝑡𝑡
≡ �
𝑃𝑃𝑃𝑃
𝑃𝑃𝐵𝐵𝑡𝑡 ≡ 𝑅𝑅𝑉𝑉𝑡𝑡 − 𝑋𝑋𝑃𝑃𝑡𝑡
𝑊𝑊
𝐷𝐷𝑡𝑡 ≡ 𝑋𝑋𝑃𝑃𝑡𝑡
+ 𝐷𝐷𝑡𝑡−1
𝑊𝑊
𝐷𝐷𝑡𝑡
Source: Corpus and Debuque-Gonzales (2023, p. 3).    
𝐼𝐼
𝐷𝐷𝑡𝑡

≡ 𝛼𝛼𝑡𝑡𝐷𝐷𝑡𝑡  
≡ (1 − 𝛼𝛼𝑡𝑡)𝐷𝐷𝑡𝑡

𝑥𝑥𝑟𝑟𝑡𝑡
𝑥𝑥𝑟𝑟𝑡𝑡−1� 𝐷𝐷𝑡𝑡−1

− 𝑃𝑃𝐵𝐵𝑡𝑡 + 𝑅𝑅𝑅𝑅𝑆𝑆𝑡𝑡

𝐼𝐼
𝐷𝐷𝑡𝑡−1

+ �

𝑇𝑇𝑁𝑁𝐼𝐼

𝑇𝑇𝑁𝑁𝑇𝑇

𝐼𝐼

Similar  to  Debuque-Gonzales  and  Corpus  (2023,  2024),  we  continue  to  adopt  a  stylized 
framework  where  output  is  determined  from  the  demand  side,  as  in  earlier  Keynes-based

7

---

<!-- PAGE 14 -->

models  and  some  other  small  macroeconometric  models  (Hammersland  and  Træe  2014; 
Kasimati and Dawson 2009).

Debuque-Gonzales and Corpus (2023) introduced the following shocks: “a positive shock to 
government consumption; a positive shock to world oil prices; and a recession in the country’s 
major  export  partners”  (p.  32).  Meanwhile,  Debuque-Gonzales  and  Corpus  (2024)  made  an 
extension by also considering the following shocks: “a world oil price shock, an exchange rate 
shock,  and  a  primary  spending  shock”  (p.  19).  We  build  on  Debuque-Gonzales  and  Corpus 
(2023,  2024)  by  introducing  impulse  (temporary)  shocks  to  the  exogenous  variables  and 
examine  the  reaction  of  the  endogenous  variables  relative  to  their  baseline  paths  from  the 
deterministic dynamic simulation. Thus, we introduce election spending shock in the domestic 
demand  block  by  simultaneously  altering  the  private  consumption  and  government 
consumption  equations  (e.g.,  introduce  shocks  through  the  structural  equations  in  Figure  2, 
and/or inflate the variables by x percent, where x can be 0.10, 0.15, and 0.20). With this, we 
assess the ability of the model, simulated as a complete system, to generate forecasts that are 
close to the actual data. Both in-sample and out-of-sample model evaluations were conducted.

3.3. Estimation

Behavioral  equations  were  estimated11  using  the  Autoregressive  Distributed  Lag  (ARDL) 
method in Error Correction Model (ECM) form. Lag lengths were optimally selected using the 
Akaike Information Criterion (AIC) restricted to a maximum of 2 lags. Cointegration between 
level variables was tested using the bounds test approach developed by Pesaran et al. (2001). 
We chose  specifications  such that estimated coefficients of variables that enter  the long-run 
equation display signs consistent with theory; variables with parameters that failed to conform 
with expectations based on either theory or intuition were relegated to the short-run equation or 
omitted  altogether.  In  cases  where  the  bounds  test  indicated  the  absence  of  cointegration, 
behavioral  relationships  were  modeled  as  a  short-run  equation  in  first  differences.  Residual 
diagnostic  checks  testing  for  homoskedasticity,  serial  correlation,  and  normality  were 
performed to ensure model adequacy. Appendix 1 shows the results of the stability tests.

Quarterly data spanning from the first quarter of 2002 to the fourth quarter of 2023 (2022Q1 to 
2023Q4)  were  used  in  the  model,  covering  a  more  extended  period  than  that  employed  by 
Debuque-Gonzales and Corpus (2023, 2024) by an additional four years. Data were sourced 
from the CEIC Economic Database12 and all series were seasonally adjusted using the X-13 
routine  prior  to  estimation  to  ensure  comparability  and  remove  regular  seasonal  effects. 
Appendix  2  shows  the  descriptive  statistics.  Results  from  Augmented  Dickey–Fuller  (ADF) 
tests indicated that most series were either integrated of order I(1) or stationary at level I(0), 
confirming  their  suitability  for  econometric  modeling.  Appendix  3  shows  the  results  of 
stationarity tests.

The inclusion of the coronavirus (COVID-19) pandemic years (2020 to 2023) is justified on 
both  methodological  and  economic  grounds.  While  we  recognize  that  these  years  represent 
atypical macroeconomic conditions, we retained them in the sample to ensure a comprehensive 
representation of the Philippine economy’s evolution over time. See the succeeding section for 
a  detailed  discussion  on  how  the  model  empirically  accounts  for  pandemic-specific  shocks.

11 EViews was used to solve the model, combining estimated behavioral equations and identities to obtain the dynamic numerical 
solution for simulation. The model was solved using the Broyden solution algorithm. For a description, see IHS Markit (2020, 
pp.1044 and 1324). 
12 Offers a global database with macroeconomic data from official sources, international institutions, and alternative data to help 
economists and investors track and analyze global trends. Website: https://www.ceicdata.com/en.

8

---

<!-- PAGE 15 -->

From  an  econometric  standpoint,  excluding  these  years  would  truncate  the  dataset  and  risk 
introducing bias into the long-run estimates by omitting a structural shock of unprecedented 
magnitude that influenced virtually all macroeconomic aggregates. Including this period allows 
the  model  to  capture  and  differentiate  extraordinary,  non-cyclical  disturbances  from  regular 
election-related  fluctuations,  thereby  enhancing  the  robustness  of  parameter  estimates  and 
improving the model’s out-of-sample forecasting accuracy.

Second, from an economic standpoint, the pandemic period provides valuable insights into how 
policy responses and economic behavior adjust under extreme shocks, including fiscal stimulus, 
mobility restrictions, and shifts in consumption and investment patterns. These dynamics mirror 
the shock-transmission mechanisms, both demand- and policy-driven, that are central to this 
study’s examination of election-induced disturbances. Including pandemic data thus broadens 
the  model’s  empirical  base,  enabling  it  to  account  for  both  exogenous  global  crises  and 
domestic  political  cycles,  and  to  test  whether  election  shocks  produce  comparable 
macroeconomic effects or interact with crisis-related volatility.

Hence,  the  2002  to  2023  data  points  provide  a  comprehensive  temporal  coverage  that 
encapsulates multiple electoral cycles, episodes of macroeconomic expansion and contraction, 
and the unprecedented COVID-19 disruption, offering a richer foundation for evaluating the 
transmission of election shocks within the Philippine macroeconomy.

4. Results and discussion

4.1. Model evaluation

Following the earlier iterations by Debuque-Gonzales and Corpus (2023, 2024), we also focus 
on the model’s dynamic forecasting performance. As indicated earlier, our sample period was 
extended  to  cover  data  from  2002Q1  to  2023Q4,  thereby  incorporating  recent  economic 
developments and policy episodes. This inclusion necessitated accounting for the COVID-19 
pandemic period, an unprecedented disruption to the Philippine economy.

To control for pandemic effects, a dummy variable, equal to one from 2020Q2 to 2021Q2, was 
introduced in the behavioral equations. This period represents the span of maximum economic 
disruption and intensive policy response. The starting point coincides with the country’s entry 
into a technical recession (Congressional Policy and Budget Research Department [CPBRD] 
2020), while the endpoint reflects the onset of sequential economic recovery and the rollout of 
mass  vaccination  campaigns  (Department  of  Health  [DOH]  2021;  Philippine  Statistics 
Authority  [PSA]  2021; World  Bank  [WB]  2021).  While  the  use  of  a  single  binary  variable 
simplifies a complex and evolving crisis, it provides a tractable way to capture the pandemic’s 
immediate  structural  shock  and 
the  government’s  corresponding  emergency  policy 
interventions  within  the  model’s  framework.  Future  refinements  may  consider  alternative 
specifications, such as structural-break tests, regime-switching parameters, or distributed-lag 
formulations to better encapsulate pandemic-related uncertainties.

Model evaluation, as seen in Figure 2 and Table 2, focused on assessing predictive capability 
using  standard  forecast  accuracy  metrics,  specifically,  the  mean  absolute  percentage  error 
(MAPE) and mean absolute error (MAE). The MAPE was applied to level variables, while the 
MAE was used for percentage and rate variables, as seen in Table 2. Overall, forecasts for GDP 
and GDP growth demonstrated reasonable predictive accuracy, with estimated paths closely 
tracking  the  actual  de-seasonalized  series.  Among  GDP  components,  private  consumption,

9

---

<!-- PAGE 16 -->

government consumption, and exports registered MAPEs of approximately 2%, 4%, and 5%, 
respectively.  Slightly  higher  errors  were  observed  for  investment  and  imports,  reflecting 
modest divergence between actual and predicted values during 2017 to 2022. This affected net 
exports toward the end of the sample.

For tax revenues, including internal and customs revenues, the MAPE remained below 10%, 
only marginally higher than in earlier model versions. Non-tax revenues, however, recorded a 
higher MAPE of around 15%, due mainly to transient spikes during specific quarters, as seen 
in Figure 2. Interest payments followed the general trend of the actual data, though the forecast 
error  was  elevated  in  the  first  two  years  and  again  toward  the  latter  part  of  the  sample, 
particularly when disaggregated into domestic and foreign components. Dynamic forecasts for 
national government debt aligned closely with observed data, though a widening gap was noted 
near the end of the series. However, the MAPE was nearly identical from the previous iteration.

For  percentage  and  rate  variables,  the  model  also  displayed  satisfactory  predictive 
performance. Employment rate had an MAE of about 0.7, maintaining close alignment with 
observed  trends.  Inflation  forecasts  showed  minor  deviations,  especially  during  2020, 
consistent with pandemic-induced price volatility. Similarly, forecasts for bank lending and for 
91-day  and  10-year  treasury  bill  rates  exhibited  modest  divergences  yet  remained  within 
acceptable margins, with MAEs of roughly 1.2, 2.3, and 2.0, respectively. When adjusted for 
real terms, these financial variables displayed forecast paths consistent with observed data.

The  remaining  forecast  deviations,  particularly  during  and  immediately  after  the  pandemic 
period, likely reflect the heightened uncertainty and nonlinear adjustments that are inherently 
challenging  to  capture  within  a  small-scale  macroeconometric  model.  Nonetheless,  the 
extended model maintains a commendable level of accuracy, demonstrating its robustness in 
tracking  both  normal  cyclical  fluctuations  and  exceptional  economic  shocks  such  as  the 
COVID-19 crisis.

Figure 2. In-sample simulations

10

---

<!-- PAGE 17 -->

11

---

<!-- PAGE 18 -->

Note: Blue lines are the actual data, while the broken red lines are the dynamic forecasts. 
Source: Authors’ calculations.

Table 2. Evaluation of in-sample forecast accuracy, 2021Q1-2023Q4

Mean absolute percentage error (MAPE) of level variables, in percent

GDP 
Household consumption 
Investment 
Government consumption 
Exports 
Imports 
Net exports 
Nominal revenues 
Nominal tax revenues 
Nominal internal tax revenues 
Nominal customs revenues 
Nominal non-tax revenues 
Nominal NG expenditure 
Nominal interest payments 
Nominal domestic interest payments

2.617 
2.280 
9.694 
4.186 
5.223 
7.923 
22.634 
6.236 
5.997 
6.687 
8.682 
15.820 
5.728 
19.242 
20.704

12

---

<!-- PAGE 19 -->

Nominal foreign interest payments 
Nominal primary expenditure 
NG debt 
Domestic NG debt 
Foreign NG debt 
GDP deflator

17.509 
6.533 
7.737 
7.737 
7.734 
4.386

Mean absolute error (MAE) of rate and percentage variables, in percentage points

GDP growth 
Employment rate 
CPI inflation 
BSP policy rate 
91-day Treasury rate 
10-year Treasury rate 
Bank lending rate 
Real 91-day Treasury rate 
Real 10-year Treasury rate 
Real bank lending rate 
Effective domestic interest rate 
Effective foreign interest rate 
Revenue/GDP 
Tax revenue/GDP 
Internal tax revenue/GDP 
Customs revenue/GDP 
Non-tax revenue/GDP 
Expenditure/GDP 
Primary spending/GDP 
Interest payments/GDP 
Foreign interest payments/GDP 
Domestic interest payments/GDP 
Primary balance/GDP 
Fiscal balance/GDP 
Debt/GDP 
Domestic debt/GDP 
Foreign debt/GDP

2.448 
0.691 
2.293 
1.315 
2.287 
1.961 
1.212 
1.780 
1.749 
1.987 
0.197 
0.117 
0.677 
3.011 
0.328 
0.266 
0.267 
1.240 
1.428 
0.379 
0.106 
0.292 
1.418 
1.286 
3.805 
2.520 
1.287

Source: Authors’ calculations.

4.2. Impact analysis of election-related spending shock

Defining election spending shock. We define an election spending shock as the four quarters 
preceding a Philippine national election, consistent with the empirical timing of political budget 
cycles observed across both developed and emerging economies (Brender and Drazen 2005; 
Shi  and  Svensson  2006;  Drazen  and  Eslava  2010).  In  our  study,  shocks  are  introduced  in 
2015Q3 to 2016Q2 and 2018Q3 to 2019Q2, corresponding to the lead-up periods of the 2016 
and 2019 elections.

Scope  of  macroeconomic  variable  selection.  While  Table  1  lists  various  macroeconomic 
variables used in the model, we only focus on private consumption, employment, investment, 
and government consumption because these variables represent the core transmission channels 
of election-related shocks identified in theory and empirical literature. That is, election cycles 
primarily  operate  through  fiscal  expansions  and  liquidity  injections,  influencing  aggregate 
demand  rather  than  supply-side  fundamentals  (Rogoff  and  Sibert  1988;  Drazen  and  Eslava

13

---

<!-- PAGE 20 -->

2010). These four variables capture the direct behavioral responses of households, firms, and 
the public sector to election-driven spending.

Our  selected  macroeconomic  variables  also  exhibit  clear  and  measurable  variations  during 
election  years  in  Philippine  national  accounts.  In  contrast,  other  macroeconomic  indicators 
such as inflation, external balance, or interest rates tend to be indirectly affected, with weaker 
or lagged responses that are harder to isolate from concurrent global or  policy shocks (e.g., 
commodity price movements, monetary tightening). Equally important, given the small-scale 
structure  of  the  macroeconometric  model,  including  additional  variables  risks  introducing 
multicollinearity and parameter instability. Restricting interpretation to the principal demand-
side  variables  ensures  a  more  robust  and  interpretable  simulation  of  election-shock 
transmission.  Ultimately,  our  selected  macroeconomic  variables  also  provide  the  most 
actionable  insights  for  fiscal  and  development  planning.  Understanding  the  dynamics  of 
consumption, 
informs 
countercyclical policy design and resource allocation in election years.

investment,  employment,  and  public  expenditure  directly

Hence, by concentrating on these core aggregates, we capture the most salient and empirically 
verifiable pathways through which election shocks influence the Philippine economy, while 
maintaining methodological rigor and analytical focus.

Shock  assumptions.  To  simulate  these  shocks,  private  domestic  demand,  comprising 
household consumption and private investment, is assumed to increase by 7%, 8%, 14%, and 
9% in each of the four pre-election quarters, while government consumption rises by 8%, 9%, 
15%, and 10%, respectively. These magnitudes are grounded in both domestic and international 
empirical evidence showing that election years are typically associated with elevated economic 
activity,  primarily  driven  by  heightened  public  expenditure  and  election-induced  private 
spending.  That  is,  the  percentages  introduced  were  based  on  the  historical  change  in 
consumption and government spending for that particular quarter in the Philippines. Studies 
such as Rogoff and Sibert (1988) and Schultz (1995) established that incumbents often engage 
in expansionary fiscal policies prior to elections, while Akhmedov and Zhuravskaya (2004) 
and Drazen and Eslava (2010) confirmed that such spending creates short-lived surges in output 
and consumption. Philippine evidence also supports this pattern. Evangelista and Libre (2008) 
and Habito (2013) noted that national income growth typically accelerates in election years due 
to  campaign-related  activities,  expanded  government  outlays,  and  higher  liquidity  in 
circulation.

Thus,  our  shock  assumptions  reflect  the  observed  behavioral  and  fiscal  regularities  of  the 
Philippine  political  cycle  namely,  frontloaded  government  spending,  elevated  household 
consumption,  and  temporary  investment  expansion  driven  by  improved  liquidity  and 
sentiment. Consistent with the approach adopted in political business cycle literature, the model 
is solved under both baseline and shock scenarios for the sample period 2012Q1 to 2023Q4, 
generating dynamic forecasts for endogenous variables. These simulations, as seen in Figure 
3, provide a quantitative basis to evaluate how pre-election demand impulses transmit through 
the  Philippine  macroeconomy  and  how  quickly  such  effects  dissipate  once  election-related 
activities subside.

Response  of  private  consumption.  Solving  the  model  under  the  generated  shock  scenario 
produced a notable increase in private consumption relative to the baseline. During the 2016 
election cycle, consumption rose by approximately 8.3%, 9.5%, 15.7%, and 10.7% in 2015Q3 
to 2016Q2, while in the 2019 cycle it increased by 10.7%, 10.8%, 18.2%, and 14.4% in 2018Q3

14

---

<!-- PAGE 21 -->

to 2019Q2. These results confirm that election periods are associated with discernible surges 
in  private  domestic  demand,  consistent  with  the  empirical  evidence  of  pre-election  fiscal 
expansions observed in both developing and emerging economies (Brender and Drazen 2005; 
Shi and Svensson 2006; Drazen and Eslava, 2010).

From Figure 3, the model also captures the transitory nature of this consumption boost. In the 
quarters immediately following an election, household consumption reverts toward its baseline 
trajectory,  reflecting  the  dissipation  of  election-related  spending  once  campaign  activities 
conclude.  The  temporary  spike  in  consumption  highlights  the  unsustainable  and  short-lived 
nature of  election-induced  demand surges,  a  feature well-documented in studies of  political 
budget cycles (Rogoff and Sibert 1988; Schultz 1995).

This  short-term  uplift  is  partly  driven  by  policies  and  fiscal  measures  implemented  or 
accelerated ahead of elections to increase disposable income, such as cash transfers, subsidies, 
or targeted social aid programs (Labonne 2016; Lokshin et al. 2022). These measures often 
expand  liquidity  among  select  demographic  segments,  temporarily  boosting  household 
consumption without creating lasting welfare gains. Additionally, political campaign spending, 
through  wages,  logistics,  and  advertising,  injects  short-term  liquidity  into  the  economy, 
stimulating short-lived consumer spending (Olano 2019).

Beyond these direct income effects, consumer sentiment also appears to play a role. As Cipullo 
and Reslow (2022) observed, governments tend to release optimistic growth forecasts before 
elections, potentially shaping public expectations and encouraging households to spend more 
in  anticipation  of  continued  economic  expansion.  However,  such  optimism  often  proves 
temporary, leading to a normalization of consumption behavior once post-election realities and 
fiscal adjustments set in.

Response  of  employment.  Furthermore,  the  injection  of  liquidity  into  households  during 
election periods can be partly attributed to campaign mobilization and the creation of temporary 
“election jobs.” As seen in Figure 3, employment rises in tandem with heightened economic 
activity,  particularly  in  the  first  quarters  of  election  years  (2016Q1  and  2019Q1),  when  the 
model estimates an average employment increase of about 2.7 percent relative to the baseline. 
This result aligns with evidence from political business cycle studies showing that pre-election 
spending spurs temporary employment in construction, logistics, and service sectors associated 
with campaign and government activities (Akhmedov and Zhuravskaya 2004; Labonne 2016).

However,  the  model also  reflects  the ephemeral  nature of such gains. Once election-related 
activities subside, the employment variable converges toward its baseline level, signifying the 
disappearance  of  short-term  and  informal  election-linked  jobs.  This  cyclical  pattern  mirrors 
findings  in  emerging  economies,  where  politically  induced  labor  demand  expands  briefly 
before  elections  and  subsequently  contracts  when  fiscal  and  campaign  spending  normalizes 
(Shi and Svensson 2006; Drazen and Eslava 2010).

Response of investment. For investment, the simulation indicates deviations of approximately 
4.5%,  5.4%,  10.8%,  and  9.1%  from  the  baseline  during  2015Q3  to  2016Q2,  reflecting  a 
discernible rise in capital formation during the pre-election period. From Figure 3, investment 
activity  continues  to  strengthen  modestly  in  the  post-election  quarters,  suggesting  an 
improvement in investor sentiment once political uncertainty subsides. The results imply that 
while  pre-election  fiscal  expansion  temporarily  boosts  demand-driven  investment,  the

15

---

<!-- PAGE 22 -->

subsequent resolution of electoral uncertainty can foster a mild but sustained rebound in private 
capital spending.

Empirical  evidence  supports  this  dual  mechanism.  Although  findings  on  election-related 
investment behavior are mixed, there is broad consensus that election periods stimulate private 
domestic  demand,  creating  short-term  conditions  favorable  to  investment  (Le  et  al.  2024; 
Azzimonti 2024; Inosante 2025). Heightened consumption and government expenditure may 
prompt firms to expand production capacity or upgrade operations to meet increased demand. 
Moreover, sector-specific effects emerge as industries directly linked to electoral activity, such 
as media, advertising, logistics, and printing, register temporary surges in output, leading to 
targeted capital injections in these areas (Drazen and Eslava 2010).

At the same time, election cycles may influence investment indirectly through infrastructure 
continuity. The sustained implementation of Public-Private Partnership (PPP) projects, many 
of  which  are  exempted  from  the  election  spending  ban,  provides  a  stabilizing  channel  for 
private  investment  even  amid  political  transitions  (Commission  on  Elections  [COMELEC] 
2018;  Aning,  2024).  This  finding  aligns  with  cross-country  studies  highlighting  that  policy 
credibility  and  ongoing  public  investment  programs  can  partially  offset  uncertainty  effects 
during election periods (Julio and Yook 2012; Shi and Svensson, 2006). Overall, the simulated 
outcomes suggest that while election shocks generate short-term investment accelerations, the 
extent  to  which  these  persist  depends  on  the  post-election  policy  environment  and  the 
continuity of major infrastructure initiatives.

Response  of  government  consumption.  The  shock  analysis  reveals  that  government 
consumption  increased  by  approximately  7%  to  14%  in  the  quarters  preceding  the  2016 
election and by 9.5% to 12.6% ahead of the 2019 election. This pattern affirms that Philippine 
election  years  typically  witness  an  acceleration  of  public  expenditure  in  anticipation  of  the 
statutory  election  spending  ban,  encompassing  infrastructure  outlays,  social  assistance 
programs, and the administrative costs of election operations (Das et al. 2025; Cigaral 2025). 
Similar  to  household  consumption,  government  spending  displays  a  cyclical  moderation  in 
non-election years, returning to near-baseline levels once electoral activities conclude.

These findings align with the broader PBC literature, which demonstrates that incumbents often 
employ expansionary fiscal policies before elections to influence voter perceptions, followed 
by  contractionary  adjustments  post-election  (Rogoff  and  Sibert  1988;  Schultz  1995;  Peters 
2010;  Labonne  2016).  The  model  likewise  shows  spending  slowdowns  before  and  after 
elections, with government consumption trending close to or even slightly below the baseline 
between 2015Q3 and 2016Q2, mirroring the empirical results of Evangelista and Libre (2008) 
for the Philippines. This suggests a pattern of fiscal frontloading, an intentional acceleration of 
expenditures before the COMELEC spending ban, particularly for infrastructure projects and 
social welfare programs, which are often justified as development priorities but may also serve 
political signaling purposes.

However, such behavior carries macroeconomic and developmental trade-offs. While election-
driven  fiscal  expansions  provide  a  temporary  stimulus,  they  can  also  distort  expenditure 
composition, diverting resources toward short-term, highly visible projects at the expense of 
long-term  investments  (Labonne  2016;  De  Haan  et  al.  2023;  Punongbayan  2025).  This 
reallocation  may  reduce  fiscal  efficiency,  undermining  the  sustainability  of  growth  once 
political incentives dissipate. Thus, results echo the consensus in empirical research. Although

16

---

<!-- PAGE 23 -->

election-induced spending cycles can generate brief economic gains, their cumulative effect 
may weaken fiscal discipline and development outcomes in the long run.

Figure 3. Election spending shock scenario

17

---

<!-- PAGE 24 -->

Note: Green lines are the baseline, while the broken red lines are the shock scenario. 
Source: Authors’ calculation.

Key findings. From Figure 3, we can construe that election years in the Philippines generate 
short-term, demand-driven expansions in key macroeconomic aggregates, consistent with PBC 
theory. We highlight that private consumption surged significantly by 8% to 16% during 2016 
and 11% to 18% during 2019 election quarters. This is reflective of higher disposable income, 
intensified  campaign  activity,  and  optimistic  expectations.  This  confirms  the  temporary 
consumption  boost  identified  by  Rogoff  and  Sibert  (1988),  Shi  and  Svensson  (2006),  and 
Evangelista and Libre (2008). For employment, we have seen it rise by roughly 2.7% in early 
election  quarters,  capturing  the  creation  of  short-term  “election  jobs.”  However,  this  effect 
quickly  dissipated  post-election,  consistent  with  Akhmedov  and  Zhuravskaya  (2004)  and 
Labonne (2016).

18

---

<!-- PAGE 25 -->

Meanwhile, private investment exhibited moderate pre-election growth of 4% to 11% driven 
by increased demand and the continuation of PPP projects, though partly offset by election-
related uncertainty (Julio and Yook  2012;  Drazen  and Eslava 2010).  Similarly, government 
consumption expanded by 7% to 14% before elections and normalized afterward, mirroring 
evidence of fiscal frontloading and subsequent retrenchment typical of political budget cycles 
(Brender and Drazen 2005; De Haan et al. 2023).

Together, these patterns illustrate that election shocks transmit primarily through the demand 
side  of  the  economy,  via  household  spending,  employment,  investment,  and  government 
outlays, producing short-term macroeconomic acceleration that is not sustained once electoral 
incentives subside.

Validation  with  scholarly  literature.  To  assess  the  model’s  consistency  with  empirical 
findings, we benchmarked our simulation results against established scholarly literature across 
four  analytical  dimensions:  (1)  magnitude  and  timing;  (2)  transmission  channels;  (3) 
persistence;  and  (4)  investment  ambiguity.  Table  3  summarizes  the  validation  of  these 
dimensions against key studies.

Table 3. Validation of empirical results

Dimensions

Magnitude and 
timing

Transmission 
channels

Persistence

Investment 
ambiguity

Results 
The four-quarter, front-loaded shock matches 
canonical PBC timing with visible fiscal expansions in 
the year before elections. 
Results underscore demand-side transmission from 
consumption to output, employment, and 
composition effects in public outlays. 
Rapid post-election mean reversion in consumption 
and employment is consistent with PBC models 
where the incentive is temporary and with evidence 
that expansions do not durably raise trend growth. 
The model’s short-run investment bump coexists 
with scholarly literature’s uncertainty-induced 
deferral at the microeconomic level suggesting that 
macroeconomic demand can partially offset firm-
level caution in election-exposed industries.

Reference 
Shi and Svensson 
(2006); Brender and 
Drazen (2005)

Drazen and Eslava 
(2010)

Brender and Drazen 
(2005); Rogoff and 
Sibert (1988)

Julio and Yook 
(2012).

Source: Authors’ tabulation.

5. Ways forward

5.1. Conclusions

We have examined the transmission of election shocks in the Philippine economy through an 
augmented  macroeconometric  model  developed  by  Debuque-Gonzales  and  Corpus  (2023, 
2024). Using quarterly data from 2002 to 2023, the model simulated the effects of pre-election 
demand  surges  on  key  macroeconomic  aggregates  namely  private  consumption,  investment, 
employment, and government consumption. Our results confirmed that election periods in the 
Philippines  are  associated  with  short-term,  demand-driven  expansions  consistent  with  the 
predictions of PBC theory. Private consumption, government spending, and employment all 
rise significantly in the quarters preceding elections, reflecting heightened fiscal disbursements,

19

---

<!-- PAGE 26 -->

campaign-related expenditures, and temporary labor creation. Investment also shows moderate 
gains, supported by buoyant demand and infrastructure continuity, though partially tempered 
by election-related uncertainty.

However,  these  effects  are  transitory.  Post-election  normalization  occurs  rapidly  as  fiscal 
activities contract and private confidence adjusts, highlighting the cyclical and unsustainable 
nature of election-induced growth. The model’s findings align with scholarly literature (Rogoff 
and Sibert 1988; Brender and Drazen 2005; Drazen and Eslava 2010), which similarly identifies 
temporary expansions followed by corrective adjustments in fiscal behavior.

Overall, we have underscored that while election shocks provide short-term stimulus, they also 
reveal  structural  vulnerabilities  in  fiscal  discipline,  expenditure  allocation,  and  policy 
continuity.  Election-related  economic  activity  boosts  aggregate  demand  but  may  distort 
development priorities, exacerbate clientelism, and undermine long-term fiscal sustainability.

5.2. Policy recommendations

Building  on  our  findings,  we  outline  policy  measures  to  manage  the  short-term  economic 
fluctuations arising from election-related activities. While we have seen that election periods 
provide a temporary boost to consumption, investment, and employment, these gains are largely 
transitory and fiscally driven. To ensure that such cycles do not compromise fiscal sustainability 
or long-term development priorities, the following recommendations, seen in Table 4, focus on 
strengthening institutional discipline, improving expenditure quality, enhancing transparency, 
and fostering macroeconomic stability during and beyond election years.

Table 4. Policy recommendations

Policy recommendation

Institutionalize fiscal 
rules and pre-election 
spending discipline

Prioritize capital-forming 
and inclusive 
expenditures

Enhance transparency in 
budget execution and 
electoral financing

Strengthen automatic 
stabilizers and counter-
cyclical policy tools

Implementation scheme 
To mitigate the volatility associated with election cycles, government 
agencies should strengthen adherence to fiscal rules that limit 
discretionary spending before elections. Establishing medium-term 
expenditure frameworks and transparent reporting of pre-election 
disbursements can reduce the scope for politically motivated fiscal 
expansion. 
Rather than short-lived consumption-driven outlays, fiscal efforts 
during election years should prioritize capital-forming investments 
(i.e., infrastructure, human capital, and climate resilience) that yield 
longer-term productivity gains. Such reorientation minimizes waste 
and ensures that electoral cycles do not compromise developmental 
integrity. 
Commission on Audit (COA), COMELEC, and Department of Budget and 
Management (DBM) should collaborate on real-time monitoring of 
government spending patterns during election periods. Public 
disclosure of infrastructure disbursements, subsidy releases, and 
transfers would improve accountability and help deter opportunistic 
fiscal manipulation. 
To cushion the economy from post-election slowdowns, the 
government should enhance automatic stabilizers (e.g., 
unemployment insurance, targeted social protection, progressive 
taxation). This would help sustain aggregate demand and maintain 
stability without resorting to politically driven fiscal impulses.

20

---

<!-- PAGE 27 -->

Maintain continuity of 
infrastructure and PPP 
programs

Improve data collection 
and political economy 
analysis

Source: Authors’ tabulation.

Continuity of PPP and flagship infrastructure projects should be 
insulated from political transitions to maintain investor confidence. 
Expanding the exemption of ongoing PPP projects from the election 
spending ban ensures policy predictability, supporting private 
investment even during periods of political uncertainty. 
We highlight the need for higher-frequency and disaggregated data on 
government spending and campaign-related activity to deepen 
analysis of political business cycles. Integrating political economy 
variables into national forecasting frameworks (e.g., DEPDev, DBM, 
BSP) would allow for more realistic macroeconomic projections during 
election years.

5.3. Limitations and areas for future studies

While we have offered  valuable insights into the  transmission  of  election  shocks  within  the 
Philippine  economy,  several  limitations  emerged  in  the  course  of  model  development  and 
simulation that future research may address.

First is on model stability and specification issues. As with any small-scale macroeconometric 
model,  maintaining  parameter  stability  across  extended  periods  remains  a  challenge.  The 
inclusion of multiple structural breaks, such as  the  2008 Global  Financial Crisis (GFC), the 
COVID-19 pandemic, and changes in fiscal regimes, may have introduced instability in long-
run relationships among variables. Future studies should explore model re-specification or re-
estimation  using  time-varying  parameters,  structural  break  tests,  or  Bayesian  updating 
techniques to improve robustness over changing macroeconomic environments.

Second is on  the impact of atypical years  and structural shocks. Our  analysis covered years 
characterized by atypical and extraordinary economic conditions, particularly the COVID-19 
pandemic (i.e., 2020 to 2022). While we have employed dummy variables to account for these 
shocks,  such  a  simplified  treatment  may  not  fully  capture  the  depth  and  persistence  of 
pandemic-induced  disruptions,  including  behavioral  shifts  in  consumption,  investment,  and 
labor market dynamics. Future studies could adopt nonlinear or regime-switching models to 
distinguish between ordinary cyclical shocks and extraordinary global crises.

Third is on post-COVID-19 structural changes. We recognize that the post-pandemic period 
introduced  significant  structural  changes  (e.g.,  digital  transformation,  altered  household 
spending patterns, supply chain reconfigurations) that the current model, calibrated on pre-2020 
relationships,  may  only  partially  reflect.  Thus,  a  full  rewriting  or  recalibration  of  the 
macroeconometric model  may be warranted to capture these evolving  structural  parameters, 
particularly in labor productivity, consumption behavior, and fiscal multipliers.

Fourth, future research could extend the analysis by estimating election-shock impacts at the 
sectoral level, specifically across agriculture, industry, and services. Such disaggregation would 
provide  deeper  insight  into  how  political  cycles  affect  sector-specific  dynamics,  such  as 
employment  and  output  composition.  However,  this  approach  would  require  consistent  and 
high-frequency  sectoral  time  series  data,  and  may  necessitate  the  development  of  separate 
sectoral macroeconometric models rather than an aggregate one, given differences in structural 
behavior and data availability.

21

---

<!-- PAGE 28 -->

Fifth,  future  research  may  also  extend  the  analysis  to  examine  the  qualitative  influence  of 
election  outcomes,  particularly  the  characteristics  of  winning  candidates  or  administrations. 
Beyond fiscal behavior and macroeconomic trends, future models could incorporate leadership 
attributes  (e.g.,  integrity,  credibility,  professional  background,  policy  platforms,  and 
governance orientation) as variables that may shape post-election economic performance. This 
approach  would  allow for  an assessment  of  how  political leadership  quality affects investor 
confidence, fiscal prudence, and macroeconomic stability. However, such an extension would 
require developing quantifiable proxies for leadership traits and compiling corresponding post-
election  economic  indicators,  posing  both  methodological  and  data  challenges  that  warrant 
dedicated empirical exploration.

Sixth,  is  on  the  practical  versus  theoretical  application.  While  we  aligned  with  econometric 
rigor, the model’s usability for real-time decision-making remains limited relative to the needs 
of the private sector. Business and investment analysts often prioritize practical forecasting and 
scenario tools over structural rigor. Future extensions may consider developing simplified or 
hybrid  models  such  as  integrating  macroeconometric  foundations  with  business-cycle 
indicators to enhance practical relevance for private-sector users while maintaining analytical 
credibility.

Thus, these limitations point to promising directions for future studies. Refining the model’s 
structure, enhancing its adaptability to non-traditional shocks, and bridging the gap between 
academic modeling and policy or market applications can help build a more resilient, context-
sensitive  macroeconometric  framework  for  the  Philippines  that  is  capable  of  capturing  both 
cyclical and structural dynamics in a rapidly evolving economic landscape.

6. References

Adams, J. J., & Barrett, P. (2023, September 29). Identifying news shocks from forecasts

(Working Paper No. 2023/208). International Monetary Fund. 
https://www.imf.org/en/Publications/WP/Issues/2023/09/29/Identifying-News-Shocks-
from-Forecasts-539674 (accessed March 5, 2025).

Akhmedov, A., & Zhuravskaya, E. (2004). Opportunistic political cycles: test in a young

democracy setting. Journal of Public Economics, 88(9–10), 2079–2105. 
Alarcon, S. J., Alhambra, P. R., Amodia, R., & Bautista, D. (2020, December). Policy

analysis model for the Philippines (BSP Working Paper Series No. 2020-12). Bangko 
Sentral ng Pilipinas. https://www.bsp.gov.ph/Sites/researchsite/Publications/BSP-
Working-PaperSeries/WPS202012.pdf (accessed March 5, 2025).

Albuquerque, D., J. Chan, D. Kanngiesser, D. Latto, S. Lloyd, S. Singh, and J. Žáček. 2025.

Decompositions, forecasts and scenarios from an estimated DSGE model for the UK 
economy. Macro Technical Paper No. 1. Bank of England. 
https://www.bankofengland.co.uk/macro-technical-paper/2025/decompositions-
forecasts-and-scenarios-from-an-estimated-dsge-model-for-the-uk-economy (accessed 
July 17 2025)

Alvarez, R. M, J. Nagler, and J. R. Willette. 1999. Measuring the relative impact of issues and 
the  economy  in  democratic  elections.  Social  Science  Working  Paper  1052.  Pasadena, 
California: California Institute of Technology.

Aning,  J.  2024.  Comelec  exempts  48  projects

from  election  ban.

Inquirer.net.

https://www.inquirer.net/423236/comelec-exempts-48-projects-from-election-ban/

Azzimonti, M. (2024, June). Economic policy uncertainty in election years (Economic Brief

No. 24-20). Federal Reserve Bank of Richmond.

22

---

<!-- PAGE 29 -->

https://www.richmondfed.org/publications/research/economic_brief/2024/eb_24-20 
(accessed March 5, 2025).

Bello, A. L. 2021. Economic voting in the Philippines. HOLISTICA – Journal of Business and

Public Administration 12(3): 1-12.

Blanchard, O. 2016. Do DSGE Models Have a Future? PIIE Policy Brief 16-11. Peterson 
Institute for International Economics. https://www.piie.com/publications/policy-
briefs/do-dsge-models-have-future (accessed July 17 2025)

Boyles,  M.  (2022,  July  19).  Understanding  how  politics  can  affect  your  business.  Harvard 
Business School Online. https://online.hbs.edu/blog/post/politics-and-business (accessed 
March 5, 2025).

Brender, A., & Drazen, A. (2005). Political budget cycles in new versus established

democracies. Journal of Monetary Economics, 52(7): 1271–1295.

Broni, M. Y., M. Hosen, H. N. Mohammed, and G. Tiamiyu. 2018. Should banks be averse to 
elections? A GMM analysis of recent elections in Ghana. Journal of Economics, Finance 
and Administrative Science 24(47): 47-65.

Calvo, G. A. 1983. Staggered prices in a utility-maximizing framework. Journal of Monetary

Economics 12 (3): 383-398.

Cigaral, I. N. P. 2024. Gov’t infrastructure spending surged ahead of election ban, says DBM.

Inquirer.net. https://business.inquirer.net/530194/govt-infrastructure-spending-surged-
ahead-of-election-ban

Cipullo,  D.  and  A.  Reslow.  2022.  Electoral  cycles  in  macroeconomic  forecasts.  Journal  of

Economic Behavior & Organization 202: 307-340.

Commission on Elections (COMELEC). 2018. In the matter of the request for confirmation of 
the Commission that the procurement of PPP projects are not covered by section 261(v) 
and (w) of the Omnibus Election Code; and study of the Law Department thereon. Minute 
Resolution  No.  18-1127-3.  https://ppp.gov.ph/wp-content/uploads/2018/12/Comelec-
Resolution-18-1127-3.pdf (accessed March 5, 2025).

Coulombe,  R.  G.  2021.  The  electoral  origin  of  government  spending  shocks.  Journal  of

Economic Dynamics and Control 129(104167).

Congressional Policy and Budget Research Department (CPBRD). 2020. Second Quarter

2020 Philippine Economic Performance. FF2020-32. House of Representatives of the 
Philippines. https://cpbrd.congress.gov.ph/ff2020-32-second-quarter-2020-philippine-
economic-performance/ (accessed October 4 2025).

Curtis, A. (2023, December 7). Do elections really matter for the economy? Capital

Economics. https://www.capitaleconomics.com/publications/global-economics-
focus/do-elections-really-matter-economy (accessed March 5, 2025).

Das, A., Rajan, B. R., Santosh Bandi, S. S., & Udandarao, V. (2025, February 28). From

polls to policies: The economic impact of elections (MPRA Paper No. 123801). Munich 
Personal RePEc Archive. https://mpra.ub.uni-muenchen.de/123801/ (accessed March 5, 
2025).

Debuque-Gonzales, M. & Corpus, J. P. P. (2023). Quantifying the Short-Run Macroeconomic 
Impacts of the COVID-19 Pandemic: A Macroeconometric Approach (Discussion Paper 
Series No. 2023-42). Philippine Institute for Development Studies. 
https://doi.org/10.62986/dp2023.42

Debuque-Gonzales,  M.  &  Corpus,  J.  P.  P.  (2024).  Let’s  Get  Fiscal:  Extending  the  Small 
Macroeconometric Model of the Philippine Economy (Research Paper Series No. 2024-
05). Philippine Institute for Development Studies.

De Haan, J., Ohnsorge, F., & Yu, S. (2023, December 20). Election-induced fiscal policy 
cycles in emerging market and developing economies (MPRA Paper No. 119551).

23

---

<!-- PAGE 30 -->

Munich Personal RePEc Archive. https://mpra.ub.uni-muenchen.de/119551/ (accessed 
March 5, 2025).

Department of Health (DOH). 2021. Vaccines Administered in the Philippines as of June 21,

2021. https://caro.doh.gov.ph/vaccines-administered-in-the-philippines-as-of-june-21-
2021/ (accessed October 4 2025).

Drazen, A., & Eslava, M. (2010). Electoral manipulation via voter-friendly spending: Theory

and evidence. Journal of Development Economics, 92(1): 39–52.

Ducanes, G., Cagas, M. A., Qin, D., Quising, P., and Magtibay-Ramos, N. 2005. A small

macroeconometric model of the Philippine economy (ERD Working Paper Series No. 
62). Asian Development Bank. 
https://www.adb.org/sites/default/files/publication/28191/wp062.pdf (accessed March 
5, 2025).

Evangelista, D. P., and P. A. Libre. 2008. Electoral cycles in Philippine fiscal and monetary 
119-159.

policy. 
https://pre.econ.upd.edu.ph/index.php/pre/article/view/180/644

Philippine  Review

Economics

The

(2):

45

of

Fiorina, M. P. 1978. Economic retrospective voting in American national elections: A micro-

analysis. American Journal of Political Science 22(2): 426-443.

Frieden, J. (2020, June). The political economy of economic policy. Finance & Development

Magazine. International Monetary Fund. 
https://www.imf.org/en/Publications/fandd/issues/2020/06/political-economy-of-
economic-policy-jeff-frieden (accessed March 5, 2025).

Gambetti, L. (2021, April 26). Shocks, information, and structural VARs. Oxford Research

Encyclopedia of Economics and Finance. 
https://doi.org/10.1093/acrefore/9780190625979.013.621

Goodell, J. W., McGee, R. J., & McGroarty, F. (2020). Election uncertainty, economic policy

uncertainty and financial market uncertainty: A prediction market analysis. Journal of 
Banking & Finance 110, 105684. https://doi.org/10.1016/j.jbankfin.2019.105684

Guerrieri, L. and M. Iacoviello. 2017. Collateral constraints and macroeconomic

asymmetries. Journal of Monetary Economics 90: 28-49. 
https://www.matteoiacoviello.com/research_files/ASYMMETRIES_PAPER.pdf  
(accessed July 17 2025)

Guntermann, E., G. S. Lenz, and J. R. Myers. 2021. The impact of the economy on presidential

elections throughout US history. Political Behavior 43: 837-857.

Gupta, S., Liu, E., & Mulas-Granados, C. (2015). Now or later? The political economy of 
public investment in democracies (IMF Working Paper 175). International Monetary 
Fund. https://www.imf.org/external/pubs/ft/wp/2015/wp15175.pdf (accessed March 5, 
2025).

Habito, C. F. (2013). Elections and the economy. The Philippine Daily Inquirer.

https://opinion.inquirer.net/52565/elections-and-the-economy (accessed March 5, 
2025).

Hendry, D. F. and J. N. J. Muellbauer. 2018. The future of macroeconomics: macro theory

and models at the Bank of England. Oxford Review of Economic Policy 34 (1-2): 287-
328. https://www.jstor.org/stable/48539417 (accessed July 17 2025)

Hendry, D. F. (2020). A short history of macro-econometric modelling. University of Oxford. 
https://www.nuffield.ox.ac.uk/economics/Papers/2020/2020W01_MacroHist18.pdf 
(accessed March 5, 2025).

Hicks, J. R. 1937. Mr. Keynes and the "Classics"; A Suggested Interpretation. Econometrica

5 (2): 147-159. https://www.jstor.org/stable/1907242 (accessed July 17 2025) 
Hoke, S. H. (2019, December). Macroeconomic effects of political risk shocks (Staff 
Working Paper No. 841). Bank of England. https://www.bankofengland.co.uk/-

24

---

<!-- PAGE 31 -->

/media/boe/files/working-paper/2019/macroeconomic-effects-of-political-risk-
shocks.pdf

Inosante, A. R. A. 2025. Election-tied spending may shield growth from tariffs. Business 
World. https://www.bworldonline.com/top-stories/2025/05/19/673200/election-tied-
spending-may-shield-growth-from-tariffs/

Ivanovic, V., Lami, E., & Imami, D. (2023). Political budget cycles in early versus regular

elections: The case of Serbia. Comparative Economic Studies, 65: 551-581. 
https://doi.org/10.1057/s41294-023-00210-0

Jahn, M., & Stricker, P. (2022). FDI, liquidity, and political uncertainty: A global analysis.

International Economics and Economic Policy, 19, 783-823. 
https://doi.org/10.1007/s10368-022-00543-8

Jalles, J. T., Kiendrebeogo, Y., Lam, W. R., Piazza R. (2023). Revisiting the

countercyclicality of fiscal policy (IMF Working Paper Series 2023/089). International 
Monetary Fund. https://doi.org/10.5089/9798400240683.001

Julio, B., & Yook, Y. (2012). Political uncertainty and corporate investment cycles. Journal of

Finance, 67(1): 45–83.

Kapas, J. (2020). Formal and informal institutions, and FDI flows: A review of the empirical 
literature and propositions for further research. Economic and Business Review, 22(2): 
161-189. https://doi.org/10.15458/ebr100.

Kaplan, G., B. Moll, and G. Violante. 2018. Monetary Policy According to HANK. American

Economic Review 18 (3): 697–743. https://benjaminmoll.com/wp-
content/uploads/2019/07/HANK.pdf (accessed July 17 2025)

Keynes, J. M. 1936. The General Theory of Employment, Interest and Money. Macmillan. 
Kladakis, G., & Skouralis, A. (2024, October). Election cycles and systemic risk (Center for

Banking Research Working Paper Series 02/24). Bayes Business School. 
https://www.bayes.citystgeorges.ac.uk/__data/assets/pdf_file/0011/835184/2024-
Kladakis-Skouralis-CBR-WP-0224.pdf (accessed March 5, 2025).

Kolios, B. 2019. Political business cycles in Australia elections and party ideology. Journal of

Time Series Econometrics 2019(20170012).

Kydland, F. E., and E. C. Prescott. 1982. Time to Build and Aggregate Fluctuations.

Econometrica, 50(6): 1345-1370. https://www.jstor.org/stable/1913386 (accessed July 
17 2025)

Labonne,  J.  2016.  Local  political  business  cycles:  Evidence  from  Philippine  municipalities. 
56-62.

Journal 
121: 
https://www.sciencedirect.com/science/article/pii/S0304387816300153

Development

Economics,

of

Landingin, R. (2010, August 26). Philippine growth spurt: it’s election spending, stupid.

Financial Times. https://www.ft.com/content/cc3b8b4a-1e8e-358c-a703-898fa874bf80 
(accessed March 5, 2025).

Leigh, A. 2004. Does the world economy swing national elections? Centre for Economic Policy

Research Discussion Paper No. 485. The Australian National University. 
Le, T., Onur, I., Sarwar, R., & Yalcin, E. (2024). Money in politics: How does It affect

election outcomes? Sage Open, 14(4). https://doi.org/10.1177/21582440241279659  
Lokshin, M. M., A. Rodriguez-Ferrari, I. Torre. 2022. Electoral Cycles and Public Spending 
during the Pandemic. Policy Research Working  Paper Series No. 10214. Washington, 
D.C.: 
Group. 
http://documents.worldbank.org/curated/en/099536210202216248

World

Bank

Lucas, R. E. 1976. Econometric policy evaluation: A critique. Carnegie-Rochester

Conference Series on Public Policy: 19-46. (accessed July 17 2025) 
Martinoli, M., Moneta, A., & Pallante, G. (2022). Calibration and validation of

macroeconomic simulation models: A general protocol by causal search (LEM

25

---

<!-- PAGE 32 -->

Working Paper Series No. 2022/33). 
https://www.econstor.eu/bitstream/10419/273635/1/1822613671.pdf (accessed March 
5, 2025).

Mertens, K., & Ravn, M. (2010). Empirical evidence on the aggregate effects of anticipated 
and unanticipated U.S. tax policy shocks (NBER Working Paper 16289). National 
Bureau of Economic Research. 
https://www.nber.org/system/files/working_papers/w16289/w16289.pdf (accessed 
March 5, 2025).

Nguyen, T. C. and T. L. Tran. 2023. The political budget cycles in emerging and developing

countries. Journal of Economics and Development 25(3): 205-225.

Ochave, R. M. D. (2015, January 21). Elections may help boost consumer goods firms’

bottom line. BusinessWorld. https://www.bworldonline.com/top-
stories/2025/01/21/647847/elections-may-help-boost-consumer-goods-firms-bottom-
line/ (accessed March 5, 2025).

Olano, C. A. V. (2019, May 14). How much economic boost does election spending deliver? 
BusinessWorld. https://www.bworldonline.com/editors-picks/2019/05/14/230732/how-
much-economic-boost-does-election-spending-deliver/ (accessed March 5, 2025).  
Pesaran, M. H., Shin, Y., & Smith, R. J. (2001). Bounds Testing Approaches to the Analysis 
of  Level  Relationships.  Journal  of  Applied  Econometrics,  16(3):  289–326. 
http://www.jstor.org/stable/2678547

Peters, A. C. 2010. Election induced fiscal and monetary cycles: Evidence from the Caribbean.

The Journal of Developing Areas 44(1): 287-302.

Philippine Statistics Authority (PSA). 2021. GDP posted a growth of 7.1 percent in the third 
quarter of 2021. https://psa.gov.ph/statistics/national-accounts/node/165276 (accessed 
October 4 2025).

Punongbayan,  J.  C.  2025.  Politics  in  the  Purse:  Political  Budget  Cycles  as  Constraints  to 
Philippine Development. ISEAS Perspective 2025 No. 17. ISEAS-Yusof Ishak Institute. 
https://www.iseas.edu.sg/articles-commentaries/iseas-perspective/2025-17-politics-in-
the-purse-political-budget-cycles-as-constraints-to-philippine-development-by-jc-
punongbayan/

Reyes, C., Bayudan-Dacuycuy, C., Abrigo, R., Quimba, F., Borromeo, N., Bautista, D., 
Ocampo, J., Baje, L., Calizo, S., Tam, Z., Hernandez, G. 2020. PIDS-BSP annual 
macroeconometric model for the Philippines: preliminary estimates and ways forward. 
PIDS Discussion Paper Series No. 2020-16. Quezon City: Philippine Institute for 
Development Studies.

Reyes, C. and Yap, J. 1993. Re-estimation of the PIDS-NEDA annual macroeconometric

model. Unpublished manuscript.

Rodriguez, U. E., & Briones, R. M. (2002). The Ateneo macroeconomic and forecasting

model. The Philippine Review of Economics, 39(1), 142-178. 
https://pre.econ.upd.edu.ph/index.php/pre/article/view/59 (accessed March 5, 2025).

Rogoff, K. and A. Sibert. 1988. Elections and macroeconomic policy cycles. Review of

Economic Studies 55(1):1-16.

Samuelson, P. A. 1948. Economics: An Introductory Analysis. McGraw-Hill. 
Sargent, T. J., and N. Wallace. 1975. Rational" Expectations, the Optimal Monetary

Instrument, and the Optimal Money Supply Rule. Journal of Political Economy 83 (2): 
241-254. https://www.jstor.org/stable/1830921 (accessed July 17 2025).

Schultz, K. A. (1995). The politics of the political business cycle. British Journal of Political

Science, 25(1), 79-99. https://www.jstor.org/stable/194177 (accessed March 5, 2025).

Shi, M., & Svensson, J. (2006). Political budget cycles: Do they differ across countries and

why? Journal of Public Economics, 90(8–9): 1367–1389.

26

---

<!-- PAGE 33 -->

Sibert,  A.  (1988).  Elections  and  macroeconomic  policy  cycles.  The  Review  of  Economic 
Studies, 55(1), 1-16. http://www.jstor.org/stable/2297526?origin=JSTOR-pdf (accessed 
March 5, 2025).

Smets, F., and R. Wouters. 2007. Shocks and Frictions in US Business Cycles: A Bayesian

DSGE Approach. American Economic Review, 97(3): 586-606. (accessed July 17 
2025)

Stanley, T. D. (2000). An empirical critique of the Lucas critique. The Journal of Socio-
Economics, 29(1), 91-107. https://doi.org/10.1016/S1053-5357(00)00055-X   
Stiglitz, J. E. 2018. Where modern macroeconomics went wrong. Oxford Review of

Economic Policy 34 (1–2): 70–106 https://academic.oup.com/oxrep/article/34/1-
2/70/4781816 (accessed July 17 2025)

Tabash, M., M. Valappil, U. Iqbal, U. Farooq, and K. Y. Woo. 2024. Stock market reaction to 
general  election  in  Pakistan:  An  event  study  methodology.  Advances  in  Decision 
Sciences 27(4).

Tannous, K. (2024, November 12). Post-election jitters: Fiscal policy, GDP growth, and 
rising yields. LinkedIn. https://www.linkedin.com/pulse/post-election-jitters-fiscal-
policy-gdp-growth-rising-tannous-qkpfc/ (accessed March 5, 2025).

Van Dalen, H. P., & Swank, O. H. (1996). Government Spending Cycles: Ideological or

Opportunistic? Public Choice, 89(1/2), 183-200. https://www.jstor.org/stable/30024155 
(accessed March 5, 2025).

World Bank (WB) 2021. Philippines Economic  Update  December  2021  Edition:  Regaining 
Workforce.

Lost 
https://thedocs.worldbank.org/en/doc/bca0601a640711811e2dea678fa08c32-
0070062021/original/World-Bank (accessed October 4 2025).

Revitalizing

Ground,

Filipino

the

Yap, J. T. 2000. PIDS annual macroeconometric model 2000. PIDS Discussion Paper Series

No. 2000-13. Makati City: Philippine Institute for Development Studies.

27

---

<!-- PAGE 34 -->

30

20

10

0

-10

-20

-30

30

20

10

0

-10

-20

7. Appendix

Appendix 1. Cumulative sum (CUSUM) and CUSUM of squares test on equations

1.  Consumption

CUSUM

CUSUM of squared

1.2

1.0

0.8

0.6

0.4

0.2

0.0

-0.2

2008

2010

2012

2014

2016

2018

2020

2022

2008

2010

2012

2014

2016

2018

2020

2022

CUSUM

5% Significance

CUSUM of Square s

5% Significance

2.  Investment

CUSUM

CUSUM of squared

1.2

1.0

0.8

0.6

0.4

0.2

0.0

-0.2

04

06

08

10

12

14

16

18

20

22

-30

04

06

08

10

12

14

16

18

20

22

CUSUM

5% Significance

CUSUM of Squares

5% Significance

3.  Government consumption

CUSUM

CUSUM of squared

30

20

10

0

-10

-20

-30

04

06

08

10

12

14

16

18

20

22

1.2

1.0

0.8

0.6

0.4

0.2

0.0

-0.2

04

06

08

10

12

14

16

18

20

22

CUSUM

5% Significance

CUSUM of Squares

5% Significance

28

---

<!-- PAGE 35 -->

4.  Imports

CUSUM

CUSUM of squared

30

20

10

0

-10

-20

-30

30

20

10

0

-10

-20

-30

30

20

10

0

-10

-20

-30

30

20

10

0

-10

-20

-30

2006

2008

2010

2012

2014

2016

2018

2020

2022

CUSUM

5% Significance

5.  Exports

CUSUM

2006

2008

2010

2012

2014

2016

2018

2020

2022

CUSUM

5% Significance

6.  Employment rate 
CUSUM

2008

2010

2012

2014

2016

2018

2020

2022

CUSUM

5% Significance

7.  Internal tax revenues

CUSUM

04

06

08

10

12

14

16

18

20

22

1.2

1.0

0.8

0.6

0.4

0.2

0.0

-0.2

1.2

1.0

0.8

0.6

0.4

0.2

0.0

-0.2

1.2

1.0

0.8

0.6

0.4

0.2

0.0

-0.2

1.2

1.0

0.8

0.6

0.4

0.2

0.0

-0.2

2006

2008

2010

2012

2014

2016

2018

2020

2022

CUSUM of Square s

5% Significance

CUSUM of squared

2006

2008

2010

2012

2014

2016

2018

2020

2022

CUSUM of Square s

5% Significance

CUSUM of squared

2008

2010

2012

2014

2016

2018

2020

2022

CUSUM of Square s

5% Significance

CUSUM of squared

04

06

08

10

12

14

16

18

20

22

CUSUM

5% Significance

CUSUM of Squares

5% Significance

29

---

<!-- PAGE 36 -->

8.  Customs revenues 
CUSUM

CUSUM of squared

1.6

1.2

0.8

0.4

0.0

-0.4

III

IV

I

II

III

IV

I

II

III

IV

I

II

III

IV

III

IV

I

II

III

IV

I

II

III

IV

I

II

III

IV

2020

2021

2022

2023

2020

2021

2022

2023

CUSUM

5% Significance

CUSUM of Square s

5% Significance

9.  Non-tax revenues 
CUSUM

CUSUM of squared

30

20

10

0

-10

-20

-30

04

06

08

10

12

14

16

18

20

22

04

06

08

10

12

14

16

18

20

22

CUSUM

5% Significance

CUSUM

5% Significance

10. Primary expenditure

CUSUM

CUSUM of squared

1.2

1.0

0.8

0.6

0.4

0.2

0.0

-0.2

04

06

08

10

12

14

16

18

20

22

04

06

08

10

12

14

16

18

20

22

CUSUM

5% Significance

CUSUM of Squares

5% Significance

11. Effective interest rate on domestic debt

CUSUM

CUSUM of squared

1.2

1.0

0.8

0.6

0.4

0.2

0.0

-0.2

04

06

08

10

12

14

16

18

20

22

04

06

08

10

12

14

16

18

20

22

CUSUM

5% Significance

CUSUM of Squares

5% Significance

12

8

4

0

-4

-8

-12

30

20

10

0

-10

-20

-30

30

20

10

0

-10

-20

-30

30

20

10

0

-10

-20

-30

30

---

<!-- PAGE 37 -->

12. Effective interest rate on foreign debt

CUSUM

CUSUM of squared

30

20

10

0

-10

-20

-30

-40

04

06

08

10

12

14

16

18

20

22

1.2

1.0

0.8

0.6

0.4

0.2

0.0

-0.2

04

06

08

10

12

14

16

18

20

22

CUSUM

5% Significance

CUSUM of Squares

5% Significance

13. Central bank policy rate

CUSUM

CUSUM of squared

30

20

10

0

-10

-20

1.4

1.2

1.0

0.8

0.6

0.4

0.2

0.0

-30

08 09 10 11 12 13 14 15 16 17 18 19 20 21 22 23

-0.2

08 09 10 11 12 13 14 15 16 17 18 19 20 21 22 23

CUSUM

5% Significance

CUSUM of Squares

5% Significance

14. 91-day Treasury bill rate

CUSUM

CUSUM of squared

30

20

10

0

-10

-20

-30

-40

30

20

10

0

-10

-20

-30

04

06

08

10

12

14

16

18

20

22

CUSUM

5% Significance

15. 10-year Treasury bond rate

CUSUM

04

06

08

10

12

14

16

18

20

22

1.2

1.0

0.8

0.6

0.4

0.2

0.0

-0.2

1.2

1.0

0.8

0.6

0.4

0.2

0.0

-0.2

04

06

08

10

12

14

16

18

20

22

CUSUM of Squares

5% Significance

CUSUM of squared

04

06

08

10

12

14

16

18

20

22

CUSUM

5% Significance

CUSUM of Squares

5% Significance

31

---

<!-- PAGE 38 -->

16. Bank lending rate 
CUSUM

CUSUM of squared

1.2

1.0

0.8

0.6

0.4

0.2

0.0

-0.2

04

06

08

10

12

14

16

18

20

22

04

06

08

10

12

14

16

18

20

22

CUSUM

5% Significance

CUSUM of Squares

5% Significance

17. Consumer price index

CUSUM

CUSUM of squared

1.2

1.0

0.8

0.6

0.4

0.2

0.0

30

20

10

0

-10

-20

-30

-40

30

20

10

0

-10

-20

-30

2006

2008

2010

2012

2014

2016

2018

2020

2022

-0.2

2006

2008

2010

2012

2014

2016

2018

2020

2022

CUSUM

5% Significance

CUSUM of Square s

5% Significance

18. GDP deflator

CUSUM

CUSUM of squared

30

20

10

0

-10

-20

-30

30

20

10

0

-10

-20

-30

04

06

08

10

12

14

16

18

20

22

CUSUM

5% Significance

19. Inflation expectations

CUSUM

04

06

08

10

12

14

16

18

20

22

1.2

1.0

0.8

0.6

0.4

0.2

0.0

-0.2

1.2

1.0

0.8

0.6

0.4

0.2

0.0

-0.2

04

06

08

10

12

14

16

18

20

22

CUSUM of Squares

5% Significance

CUSUM of squared

04

06

08

10

12

14

16

18

20

22

CUSUM

5% Significance

CUSUM of Squares

5% Significance

32

---

<!-- PAGE 39 -->

Appendix 2. Summary statistics 
Variable 
GDP 
GDP growth 
Household consumption 
Investment 
Government consumption 
Imports 
Exports 
Disposable income 
Domestic demand 
Employment rate 
Consumer price index 
GDP deflator 
US consumer price index 
CPI inflation 
Deviation from inflation target 
Expected inflation 
Deviation from inflation target 
World oil price (USD per barrel) 
Retail price of ordinary rice (USD/ton) 
PHP/USD exchange rate 
Real PHP/USD exchange rate 
BSP policy rate 
91-day Treasury rate 
10-year Treasury rate 
Bank lending rate 
Real 91-day Treasury rate 
Real 10-year Treasury rate 
Real bank lending rate 
10-year Treasury rate US 
Nominal revenues 
Nominal tax revenues 
Nominal internal tax revenues 
Nominal customs revenues 
Nominal non-tax revenues 
Nominal NG expenditure 
Nominal primary expenditure 
Nominal interest payments 
Nominal domestic interest payments 
Nominal foreign interest payments 
Effective domestic interest rate 
Effective foreign interest rate 
Primary balance/GDP 
NG debt 
Domestic NG debt 
Foreign NG debt 
Debt/GDP 
Domestic debt/GDP 
Foreign debt/GDP 
Source: Authors’ calculation

Obs 
 92.00000 
 92.00000 
 92.00000 
 92.00000 
 92.00000 
 92.00000 
 92.00000 
 92.00000 
 92.00000 
 79.00000 
 92.00000 
 92.00000 
 92.00000 
 92.00000 
 92.00000 
 90.00000 
 90.00000 
 92.00000 
 81.00000 
 92.00000 
 92.00000 
 92.00000 
 92.00000 
 92.00000 
 91.00000 
 92.00000 
 92.00000 
 91.00000 
 92.00000 
 92.00000 
 92.00000 
 92.00000 
 92.00000 
 92.00000 
 92.00000 
 92.00000 
 92.00000 
 92.00000 
 92.00000 
 92.00000 
 92.00000 
 92.00000 
 92.00000 
 92.00000 
 92.00000 
 92.00000 
 92.00000 
 92.00000

Mean 
 15.00616 
 5.100274 
 14.71327 
 13.40527 
 12.85640 
 13.90079 
 13.67446 
 14.90120 
 15.07274 
 93.32286 
 4.434372 
 4.462031 
 4.584116 
 3.863665 
 0.081057 
 3.880644 
 0.102866 
 4.130562 
 6.528090 
 3.896962 
 4.046706 
 4.785326 
 3.834284 
 7.014418 
 7.413242 
-0.029381 
 3.150752 
 3.535160 
 3.079301 
 12.94328 
 12.81778 
 12.55341 
 11.31126 
 10.76776 
 13.13778 
 12.94093 
 11.31601 
 10.90898 
 10.19951 
 1.635488 
 1.267831 
-0.282698 
 15.57367 
 15.08119 
 14.60770 
 53.31662 
 32.47692 
 20.83998

Std. dev. 
 0.337554 
 3.919953 
 0.312916 
 0.493765 
 0.458427 
 0.442758 
 0.377367 
 0.330769 
 0.360153 
 1.762076 
 0.244569 
 0.201113 
 0.150793 
 1.978919 
 1.987872 
 1.826359 
 1.858691 
 0.440772 
 0.233192 
 0.097006 
 0.146097 
 1.691357 
 2.138260 
 2.983422 
 1.642790 
 2.237194 
 2.947634 
 2.032507 
 1.144704 
 0.593574 
 0.605913 
 0.597581 
 0.647554 
 0.548466 
 0.637177 
 0.717014 
 0.313734 
 0.362481 
 0.266079 
 0.445163 
 0.268807 
 2.962809 
 0.481192 
 0.575729 
 0.339936 
 9.753641 
 5.482577 
 6.393255

Min 
 14.41938 
-15.73532 
 14.16219 
 12.60449 
 12.17256 
 13.28778 
 12.99249 
 14.31227 
 14.50052 
 82.68118 
 3.988600 
 4.048779 
 4.320689 
-0.039411 
-3.039411 
 0.176666 
-2.823334 
 3.024053 
 5.879447 
 3.706344 
 3.830282 
 2.000000 
 0.399254 
 2.933949 
 5.404006 
-4.365562 
-1.868480 
-1.492220 
 0.662028 
 11.81075 
 11.68525 
 11.42865 
 10.00319 
 9.662538 
 12.16042 
 11.84193 
 10.58728 
 10.21010 
 9.429575 
 0.931173 
 0.636514 
-10.71427 
 14.71613 
 14.06369 
 13.97840 
 39.46933 
 25.62184 
 13.38040

Max 
 15.54991 
 12.28460 
 15.22696 
 14.12053 
 13.62048 
 14.56990 
 14.22927 
 15.43205 
 15.64909 
 96.13102 
 4.844825 
 4.782431 
 4.895367 
 10.31928 
 6.319283 
 10.17660 
 6.176596 
 4.767946 
 6.814592 
 4.064011 
 4.358443 
 7.500000 
 8.133365 
 14.30097 
 10.85725 
 5.032397 
 11.17548 
 7.816798 
 5.069424 
 13.95539 
 13.80315 
 13.53053 
 12.37857 
 12.10431 
 14.23665 
 14.08569 
 12.27139 
 11.83774 
 11.26906 
 2.667550 
 1.768446 
 4.635260 
 16.59206 
 16.20897 
 15.45108 
 71.06895 
 43.41447 
 34.67981

33

---

<!-- PAGE 40 -->

Appendix 3. Results of the ADF test

Variables 
GDP 
GDP growth 
Household consumption 
Investment 
Government consumption 
Imports 
Exports 
Disposable income 
Domestic demand 
Employment rate 
Consumer price index 
GDP deflator 
US consumer price index 
CPI inflation 
Deviation from inflation target 
Expected inflation 
Deviation from inflation target 
World oil price (USD per barrel) 
Retail price of ordinary rice (USD/ton) 
PHP/USD exchange rate 
Real PHP/USD exchange rate 
BSP policy rate 
91-day Treasury rate 
10-year Treasury rate 
Bank lending rate 
Real 91-day Treasury rate 
Real 10-year Treasury rate 
Real bank lending rate 
10-year Treasury rate US 
Nominal revenues 
Nominal tax revenues 
Nominal internal tax revenues 
Nominal customs revenues 
Nominal non-tax revenues 
Nominal NG expenditure 
Nominal primary expenditure 
Nominal interest payments 
Nominal domestic interest payments 
Nominal foreign interest payments 
Effective domestic interest rate 
Effective foreign interest rate 
Primary balance/GDP 
NG debt 
Domestic NG debt 
Foreign NG debt 
Debt/GDP 
Domestic debt/GDP 
Foreign debt/GDP

Source: Authors’ calculation

diff=0 
 0.848505 
 0.018645 
 0.850132 
 0.787998 
 0.973755 
 0.868088 
 0.719263 
 0.812715 
 0.917530 
 0.000100 
 0.733661 
 0.364247 
 0.991907 
 0.007652 
 0.004059 
 0.184991 
 0.004307 
 0.071016 
 0.059567 
 0.668310 
 0.510377 
 0.163745 
 0.031014 
 0.017979 
 0.014352 
 0.015754 
 0.008301 
 0.001256 
 0.278236 
 0.827929 
 0.839660 
 0.748273 
 0.683355 
 0.880388 
 0.984335 
 0.968874 
 0.988705 
 0.969265 
 0.873016 
 0.470250 
 0.401333 
 0.358776 
 0.996948 
 0.989639 
 0.998088 
 0.481812 
 0.548330 
 0.601342

diff=1 
 1.80E-08 
 2.22E-08 
 6.62E-08 
 0.000100 
 0.000100 
 0.000100 
 0.000100 
 8.59E-08 
 4.13E-08 
 0.000100 
 5.62E-05 
 3.00E-07 
 1.13E-06 
 2.35E-05 
 0.001588 
 3.38E-05 
 1.07E-06 
 2.01E-08 
 1.43E-07 
 4.04E-07 
 2.95E-07 
 2.44E-05 
 2.12E-06 
 1.10E-08 
 5.99E-08 
 0.001393 
 4.83E-08 
 0.000383 
 2.41E-08 
 2.09E-07 
 0.000100 
 0.000100 
 0.000100 
 0.000100 
 0.000100 
 0.000100 
 0.000100 
 0.000100 
 0.000100 
 0.000100 
 2.35E-08 
 1.08E-05 
 6.83E-05 
 8.17E-06 
 1.00E-06 
 0.002019 
 0.000683 
 0.047112

diff=2 
 2.79E-08 
 3.72E-08 
 0.000100 
 1.23E-07 
 0.000100 
 3.14E-08 
 0.000100 
 2.92E-08 
 0.000100 
 0.000100 
 2.38E-08 
 3.50E-08 
 2.53E-08 
 2.13E-05 
 7.13E-08 
 1.19E-07 
 1.40E-07 
 2.35E-08 
 0.000100 
 0.000100 
 5.39E-06 
 2.37E-08 
 0.000100 
 1.42E-05 
 1.22E-06 
 3.10E-08 
 5.39E-08 
 6.18E-07 
 1.56E-08 
 0.000100 
 3.34E-06 
 5.02E-08 
 0.000100 
 3.07E-08 
 4.79E-07 
 1.52E-06 
 4.16E-08 
 4.36E-08 
 3.33E-05 
 3.45E-06 
 0.000100 
 1.52E-06 
 8.54E-07 
 0.000100 
 7.32E-05 
 0.000100 
 0.000100 
 0.000100

34

<!-- MARKITDOWN CONVERSION -->

<!-- Full MarkItDown conversion for formatting fidelity. -->

Ruiz, Mark Gerald C.; Miral, Ramona Maria L.; Rivera, John Paolo R.
Working Paper
Election-year stimuli and economic performance: Evidence
from a macroeconometric model of the Philippines
PIDS Discussion Paper Series, No. 2025-60
Provided in Cooperation with:
Philippine Institute for Development Studies (PIDS), Philippines
Suggested Citation: Ruiz, Mark Gerald C.; Miral, Ramona Maria L.; Rivera, John Paolo R. (2025) :
Election-year stimuli and economic performance: Evidence from a macroeconometric model of the
Philippines, PIDS Discussion Paper Series, No. 2025-60, Philippine Institute for Development Studies
(PIDS), Quezon City,
https://doi.org/10.62986/dp2025.60
This Version is available at:
https://hdl.handle.net/10419/339140
Standard-Nutzungsbedingungen: Terms of use:
Die Dokumente auf EconStor dürfen zu eigenen wissenschaftlichen Documents in EconStor may be saved and copied for your personal
Zwecken und zum Privatgebrauch gespeichert und kopiert werden. and scholarly purposes.
Sie dürfen die Dokumente nicht für öffentliche oder kommerzielle You are not to copy documents for public or commercial purposes, to
Zwecke vervielfältigen, öffentlich ausstellen, öffentlich zugänglich exhibit the documents publicly, to make them publicly available on the
machen, vertreiben oder anderweitig nutzen. internet, or to distribute or otherwise use the documents in public.
Sofern die Verfasser die Dokumente unter Open-Content-Lizenzen If the documents have been made available under an Open Content
(insbesondere CC-Lizenzen) zur Verfügung gestellt haben sollten, Licence (especially Creative Commons Licences), you may exercise
gelten abweichend von diesen Nutzungsbedingungen die in der dort further usage rights as specified in the indicated licence.
genannten Lizenz gewährten Nutzungsrechte.

CONTACT US:
https://www.pids.gov.ph
RESEARCH INFORMATION DEPARTMENT
Philippine Institute for Development Studies
publications@pids.gov.ph
18th Floor, Three Cyberpod Centris - North Tower
EDSA corner Quezon Avenue, Quezon City, Philippines
(+632) 8877-4000
SEIRES
REPAP
NOISSUCSID
5202
rebmeceD
,06-5202
.oN
Photo from the Philippine Information Agency (https://pia.gov.ph/news/luzon/calabarzon/paghahanda-para-sa-2025-elections-inilatag-ng-comelec-quezon)
Election-Year Stimuli and Economic
Performance: Evidence from a
Macroeconometric Model of
the Philippines
Mark Gerald C. Ruiz, Ramona Maria L. Miral, and
John Paolo R. Rivera
The PIDS Discussion Paper Series constitutes studies that are preliminary and subject to further
revisions. They are posted on the PIDS website for purposes of soliciting comments and
suggestions for further refinements. The studies under the Series are unedited and unreviewed.
The views and opinions expressed are those of the author(s) and do not necessarily reflect
those of the Institute. The Institute allows citation and quotation of the paper as long as proper
attribution is made.

Election-Year Stimuli and Economic Performance:
Evidence from a Macroeconometric Model of the Philippines
Mark Gerald C. Ruiz
Ramona Maria L. Miral
John Paolo R. Rivera
PHILIPPINE INSTITUTE FOR DEVELOPMENT STUDIES
08 November 2025

Abstract
We evaluated the transmission of election shocks in the Philippine economy using an
augmented macroeconometric model that integrates political business cycle (PBC) dynamics
into the country’s macroeconomic framework. Building upon the model developed by
Debuque-Gonzales and Corpus (2023, 2024), quarterly data from 2002 to 2023 were utilized
to simulate the effects of election-induced fiscal and private sector behavior on key
macroeconomic variables, namely private consumption, employment, investment, and
government consumption. Results reveal that election years generate short-term, demand-
driven expansions, fueled by heightened government spending, campaign activities, and
temporary job creation. However, these effects are transitory, with economic activity reverting
near baseline levels post-election as fiscal impulses fade. Findings align with established
literature on political budget cycles, confirming that election-driven growth is cyclical rather
than structural, and may induce inefficiencies in expenditure allocation and fiscal discipline.
The study highlights the need for institutional reforms, fiscal transparency, and counter-cyclical
policies to mitigate volatility and promote long-term stability. Finally, limitations related to
model stability, pandemic disruptions, and evolving post-COVID economic structures suggest
avenues for recalibrating and rewriting the macroeconometric model for future applications.
Keywords: election shocks; macroeconometric modeling, political business cycles
JEL Classification: C51, E62
i

Table of Contents
1. Introduction .................................................................................................................... 1
2. Literature review ............................................................................................................ 2
2.1. Historical evolution of macroeconometric models ....................................................... 2
2.2. Existing macroeconometric models in the Philippines ................................................. 3
2.3. Economic impacts of from election activities ............................................................... 4
2.4. Political business cycles ............................................................................................. 4
2.5. Model enhancements ................................................................................................. 5
2.6. Research gap ............................................................................................................. 5
3. Methodology ................................................................................................................... 6
3.1. Conceptual framework ................................................................................................ 6
3.2. Operational framework ............................................................................................... 6
3.3. Estimation ................................................................................................................... 8
4. Results and discussion ................................................................................................. 9
4.1. Model evaluation ........................................................................................................ 9
4.2. Impact analysis of election-related spending shock .................................................. 13
5. Ways forward ............................................................................................................... 19
5.1. Conclusions .............................................................................................................. 19
5.2. Policy recommendations ........................................................................................... 20
5.3. Limitations and areas for future studies .................................................................... 21
6. References.................................................................................................................... 22
7. Appendix ...................................................................................................................... 28
List of Figures
Figure 1. Model structure ...................................................................................................... 6
Figure 2. In-sample simulations .......................................................................................... 10
Figure 3. Election spending shock scenario ........................................................................ 17
List of Tables
Table 1. Model equations and variables ................................................................................ 7
Table 2. Evaluation of in-sample forecast accuracy, 2021Q1-2023Q4 ................................ 12
Table 3. Validation of empirical results ................................................................................ 19
Table 4. Policy recommendations ....................................................................................... 20
ii

List of Abbreviations
ADB Asian Development Bank
ADF Augmented Dickey–Fuller
AIC Akaike Information Criterion
ARDL Autoregressive Distributed Lag
BIR Bureau of Internal Revenue
BOC Bureau of Customs
BSP Bangko Sentral ng Pilipinas
COA Commission on Audit
COMELEC Commission on Elections
COVID-19 Coronavirus Disease 2019
CPI Consumer Price Index
CPBRD Congressional Policy and Budget Research Department
CUSUM Cumulative Sum
DBM Department of Budget and Management
DEPDev Department of Economy, Planning, and Development
DLSU De La Salle University
DOH Department of Health
DSGE Dynamic Stochastic General Equilibrium
ECM Error Correction Model
FDI Foreign Direct Investment
FRB Federal Reserve Bank
GDP Gross Domestic Product
GE General Equilibrium
GFC Global Financial Crisis
GMM Generalized Method of Moments
HANK Heterogeneous Agent New Keynesian
IMF International Monetary Fund
IS-LM Investment-Saving and Liquidity Preference-Money Supply
MAE Mean Absolute Error
MAPE Mean Absolute Percentage Error
MEM Macroeconometric Model
NBER National Bureau of Economic Research
NEDA National Economic and Development Authority
NG National Government
OECD Organisation for Economic Co-operation and Development
OLG Overlapping Generations
PBC Political Business Cycle(s)
PIDS Philippine Institute for Development Studies
PPP Public-Private Partnership
PSA Philippine Statistics Authority
RBA Reserve Bank of Australia
SVAR Structural Vector Autoregression
VAR Vector Autoregression
ADB Asian Development Bank
iii

Election-Year Stimuli and Economic Performance: Evidence from a
Macroeconometric Model of the Philippines
Mark Gerald C. Ruiz1, Ramona Maria L. Miral2, and John Paolo R. Rivera3
1. Introduction
The Philippine economy has historically shown fluctuations during election years, distinct from
non-election periods, driven by increased government expenditures, heightened consumer and
business activity, and shifts in investor confidence (Ochave 2025; Habito 2013; Landingin
2010). Elections, being periodic events when political and economic forces interact, impact
macroeconomic performance through economic shocks that are transmitted to changes in fiscal
policy, public infrastructure spending, capital flows, and overall market sentiment (de Haan et
al. 2023). However, this growth can be unsustainable if it is not driven by structural economic
improvements (Curtis 2023). Thus, such periods also introduce uncertainty, affecting
inflationary trends, foreign direct investment (FDI) inflows, and long-term fiscal sustainability
(Azzimonti 2024; Goodell et al. 2020; Gupta et al 2015).
The year 2025, being an election year in the Philippines (i.e., midterm elections4), differs from
non-election years. On one hand, election years often see an uptick in gross domestic product
(GDP) growth due to increased fiscal expenditures, particularly on infrastructure projects (i.e.,
to demonstrate accomplishments and gain voter support, governments often accelerate
infrastructure programs in the months leading up to an election), social assistance programs
(i.e., increased funding for social programs, subsidies, and cash transfers is common to bolster
political goodwill), and election-related administrative spending (i.e., budget for electoral
processes, including voter registration, election security, and logistics, contributes to
government spending growth) (Das et al. 2025; Olano 2019). Also, the government tends to
frontload disbursements in the run-up to elections, driving short-term demand in the economy
(Frieden 2020). Succeeding, post-election years often see fiscal tightening as governments
attempt to curb deficits and adhere to fiscal discipline, leading to a slowdown in public
investment (Tannous 2024).
Consequently, the increased liquidity in the economy during election years, stemming from
government expenditures and campaign-related spending, can contribute to higher inflation
(Kladakis and Skouralis 2024). The surge in money supply, combined with increased consumer
demand, can lead to price increases, particularly in food, services, and transportation. Moreover,
if the government resorts to deficit spending to finance election-related expenditures,
inflationary pressures may persist beyond the election period. While GDP growth may
temporarily rise, election-related uncertainty often dampens investor confidence (Azzimonti
2024; Goodell et al. 2020; Gupta et al 2015). FDI inflows tend to slow during election years as
businesses and investors adopt a wait-and-see approach, assessing potential shifts in policy,
regulatory frameworks, and political stability (Jahn and Stricker 2022). Political transitions can
lead to concerns over changes in business conditions, tax regimes, and contract security,
prompting investors to delay commitments or divert capital to more stable environments
1 Research Specialist, Philippine Institute for Development Studies. Email: mruiz@pids.gov.ph
2 Research Specialist, Philippine Institute for Development Studies. Email: rmiral@pids.gov.ph
3 Senior Research Fellow, Philippine Institute for Development Studies. Email: jrivera@pids.gov.ph
4 In the Philippine context, a midterm election refers to a national and local election held halfway through the six-year term of the
incumbent president. It takes place three years after a presidential election and serves as a political barometer of the sitting
administration’s performance and public approval.
1

(Boyles 2022). The impact on FDI flows depends on the perceived credibility of institutions
and the policy stance of incoming leadership (Kapas 2020).
On the other hand, election years also see significant uptick in private sector and household
expenditures (Olano 2019). Political campaigns inject significant liquidity into the economy
through salaries, advertising expenditures, and logistics, leading to higher consumer spending,
particularly in services, retail, and transport. Likewise, some businesses increase spending
during election years, particularly those linked to election-related industries such as media,
advertising, and printing (Le et al. 2024). However, firms with long-term investment plans may
delay major capital expenditures due to policy uncertainty and a wait-and-see behavior
(Azzimonti 2024; Goodell et al. 2020; Gupta et al 2015).
Given the May 2025 Philippine midterm elections, our study is relevant in providing empirical
insights on the extent of election-driven economic stimulation. While election-related
government expenditures may create short-term growth, concerns remain about inflationary
pressures, fiscal sustainability, and economic volatility post-election. Moreover, investor
sentiment (both domestic and foreign) can be swayed by electoral uncertainty, impacting capital
inflows and business decisions.
Given the abovementioned backdrop and the cyclical nature of these economic dynamics, we
inquire on how election-related shocks are transmitted through the Philippine
macroeconomy? In addressing this research question, we are guided by an overarching
objective to integrate election variables into a macroeconometric model for the Philippines.
Supporting this are the following specific objectives:
1. To estimate the magnitude of election-year stimulus on GDP growth and whether it leads
to sustained economic benefits or short-term artificial growth;
2. To estimate the extent to which inflation is influenced by election-related liquidity surges,
private sector expenditures, and government spending patterns;
3. To evaluate how election-induced uncertainty affects FDI inflows and business confidence;
and
4. To generate policy recommendations on how the government can balance economic
stimulus with long-term stability.
By evaluating the transmission of election shocks through a macroeconometric framework
developed by Debuque-Gonzales and Corpus (2023), we contribute to evidence-based
policymaking, helping stakeholders better understand the economic implications of election
cycles. Also, by offering a structured analysis of these effects, we contribute to informed
decision-making for policymakers, economists, and business leaders navigating the
complexities of election-year economic shifts and in anticipating both short-term economic
boosts and potential long-term distortions. Findings can serve as a basis for formulating
strategies to mitigate economic risks while leveraging potential benefits during election periods.
2. Literature review
2.1. Historical evolution of macroeconometric models
The origins of macroeconometric modeling trace back to early macroeconomic thought on
general equilibrium (GE) theory, which introduced aggregate demand as an analytical variable
distinct from aggregate supply. Keynes (1936) challenged the classical notion of self-correcting
markets by arguing that economies could settle into equilibrium with involuntary
2

unemployment, requiring government intervention to stimulate demand. Hicks (1937)
formalized this interaction in the IS-LM (investment-saving and liquidity preference-money
supply) framework, later integrated into the “neoclassical synthesis” that combined long-run
neoclassical principles with short-run Keynesian dynamics (Samuelson 1948).
The post-war period saw the rise of large-scale econometric models, spurred by the Cowles
Commission’s5 pioneering work in statistical estimation and model testing. A major turning
point came with the Lucas Critique6 (Lucas 1976). This critique spurred the development of
micro-founded models grounded in rational expectations, including the policy-ineffectiveness
proposition of Sargent and Wallace (1975).
In subsequent decades, macroeconomic modeling evolved toward Dynamic Stochastic General
Equilibrium (DSGE) frameworks that explicitly incorporate intertemporal optimization and
stochastic shocks (Kydland and Prescott 1982; Smets and Wouters 2007). Later refinements
introduced New Keynesian DSGE models that allow for nominal rigidities (Calvo 1983) and
Heterogeneous Agent New Keynesian (HANK) models that account for distributional effects
(Kaplan et al. 2018). Despite their sophistication, DSGE models faced criticism for failing to
anticipate the 2008 Global Financial Crisis (Hendry and Muellbauer 2018; Stiglitz 2018).
Contemporary work thus emphasizes more flexible and data-driven macroeconometric
approaches integrating behavioral expectations, non-linearities, and institutional factors
(Blanchard 2016; Guerrieri and Iacoviello 2017; Albuquerque et al. 2025).
2.2. Existing macroeconometric models in the Philippines
The Philippines’ experience with macroeconometric modeling has evolved alongside global
developments. Early models were developed by academic institutions7, multilateral
organizations8, and government agencies such as the Philippine Institute for Development
Studies (PIDS), the Department of Economy, Planning and Development (DEPDev9), and the
Bangko Sentral ng Pilipinas (BSP10). These models, often medium-scale and demand-driven,
were designed to inform fiscal and monetary policy by simulating relationships among
aggregate output, consumption, investment, and inflation (Debuque-Gonzales and Corpus
2023, 2024). For a historical background of earlier macroeconometric models in the
Philippines, Debuque-Gonzales and Corpus (2023, 2024) provided a detailed discussion from
the annual macroeconometric model (MEM) by Constantino and Yap (1988), Constantino et
5 Focuses on linking economic theory to mathematics and statistics; its advances in economics involved the creation and
integration of GE theory and econometrics.
6 A theory in macroeconomics that criticizes the use of past data to predict how new economic policies will affect the economy. It
argued that people's expectations and behavior change in response to new economic policies. Therefore, using historical data to
predict the effects of new policies is not reliable. Moreover, it is a fundamental criticism of empirical economics, which questions
its ability to model, test, or predict the economy (Stanley 2000).
7 For instance, De La Salle University (DLSU) has developed multiple macroeconometric models of the Philippine economy(i.e.,
ANIMO model, Quarterly model, Simultaneous equation system, OLG model). These models are used to forecast the economy
and help inform policy decisions. For more information, see https://www.dlsu-aki.com/research-programs-and-projects.html. Also,
Rodriguez and Briones (2002) built the quarterly Ateneo Macroeconomic and Forecasting Model (AMFM) based on the short-run
version of the Murphy model of Australia.
8 The Asian Development Bank (ADB) developed macroeconometric models of select ADB member economies for forecasting
and policy simulation. The model designed for the Philippines (Cagas et al. 2006; Ducanes et al. 2005) paid special attention to
the government block of the model to enable fiscal simulations. See
https://www.adb.org/sites/default/files/publication/28191/wp062.pdf.
9 Formerly known as the National Economic and Development Authority (NEDA); the Philippine government agency responsible
for national economic planning, policy coordination, and monitoring to ensure sustainable development; also oversees the
approval of large projects, trade policies, and the efficient use of land and natural resources, working to link development planning
with the national budget. Website: https://depdev.gov.ph/.
10 The Policy Analysis Model for the Philippines (PAMPh) is a model used by the BSP to analyze the economy and guide monetary
policy. It is used as the main model for medium-term forecasting and policy analysis (Alarcon et al. 2020). See
https://www.bsp.gov.ph/Sites/researchsite/Publications/BSP-Working-PaperSeries/WPS202012.pdf.
3

al. (1980), Reyes and Yap (1993), Yap (2000) to more recent macroeconometric and forecasting
model by Rodrigues and Briones (2002), structural MEM by Ducanes et al. (2005) and Cagas
et al. (2006), quarterly macroeconometric model of Bautista et al. (2009), annual MEM by
Reyes et al. (2020),
Debuque-Gonzales and Corpus (2023, 2024) made a significant step toward systematizing this
framework using robust econometric specifications. These models align with international
standards by employing simultaneous equations, error-correction mechanisms, and
cointegration analysis to capture both short- and long-run dynamics. However, political and
institutional shocks, particularly election-induced fluctuations, remain underexplored within
these models. We build on this gap by integrating election shocks as exogenous or structural
disturbances that influence fiscal behavior, investor confidence, and macroeconomic outcomes.
2.3. Economic impacts of from election activities
Substantial scholarly literature has explored the two-way relationship between elections and the
economy. On one hand, macroeconomic conditions affect voting behavior, known as economic
voting, where voters reward or punish incumbents based on perceived economic performance
(Bello 2021; Guntermann et al. 2021; Leigh 2004; Alvarez et al. 1999; Fiorina 1978).
Conversely, elections influence the economy through various channels. The political business
cycle literature suggests that incumbents manipulate fiscal or monetary tools to enhance
reelection prospects (Schultz 1995; Rogoff and Sibert 1988). Empirical studies show that
election years often coincide with surges in public expenditures, shifts in credit conditions, or
changes in money supply (Kolios, 2019; Peters, 2010). Recent cross-country evidence from
Nguyen and Tran (2023) confirmed that incumbents in 91 emerging and developing economies
expanded government spending before and during elections, then contracted it afterward.
Sector-specific analyses corroborate these macro-level findings. Broni et al. (2019) observed
higher bank returns during Ghanaian election years as citizens increased deposits amid political
uncertainty, while Tabash et al. (2024) found that the 2018 Pakistan general election positively
affected stock market performance. Despite this broad literature, there remains limited
empirical research assessing the multi-sectoral macroeconomic impact of elections in the
Philippine context, creating space for our contribution.
2.4. Political business cycles
The concept of political business cycles (PBCs) provides the theoretical foundation for
analyzing election shocks. PBC models posit that elected officials, seeking reelection,
manipulate fiscal and monetary levers to generate temporary economic upswings before
elections (Schultz 1995; Rogoff and Sibert 1988; Nordhaus 1975). Subsequent empirical work
quantified these effects such as that of Coulombe (2021) who identified ideological and
electoral drivers of fiscal expansions in OECD countries, as well as Cipullo and Reslow (2022)
who documented politically motivated GDP forecast optimism in advanced economies.
These findings suggest that election shocks transmit through multiple macroeconomic channels
(i.e., government spending, inflation expectations, investor sentiment), all of which can be
modeled within a macroeconometric framework to understand cyclical fluctuations in output
and employment.
4

2.4. Econometric approaches to modeling election shocks
Modeling election shocks requires distinguishing between anticipated and unanticipated
components (Adams and Barrett 2023; Mertens and Ravn 2012). Anticipated shocks are often
captured using dummy variables representing election periods to model systematic policy
changes, particularly fiscal expansions (Ivanovic et al. 2023; Van Dalen and Swank 1996).
Meanwhile, unanticipated shocks, such as surprise election outcomes or abrupt policy shifts,
are typically modeled using Structural Vector Autoregression (SVAR) frameworks, which
isolate the dynamic responses of key variables to unexpected shocks (Gambetti 2021; Hoke
2019). These econometric techniques are essential in quantifying how election cycles affect
aggregate demand, investment, and inflation through different transmission mechanisms.
2.5. Model enhancements
Integrating political and institutional variables into macroeconometric models enhances both
model calibration and policy design. From a modeling perspective, the inclusion of political
variables allows for more precise calibration, improving the reliability of simulations and
forecasts (Martinoli et al. 2022). From a policy standpoint, understanding election-driven cycles
supports the formulation of counter-cyclical fiscal policies to offset inflationary pressures or
post-election slowdowns (Jalles et al. 2023; IMF 2023). This integrated approach bridges
empirical modeling with practical fiscal governance, making macroeconometric tools more
responsive to real-world political dynamics.
2.6. Research gap
Despite an extensive body of scholarship on PBCs and macroeconomic modeling, there remains
a dearth of studies that systematically examines how election shocks transmit through the
Philippine economy within an econometric framework. Existing studies, both local and
international, tend to focus on short-term fiscal dynamics, such as pre-election increases in
government disbursements or post-election fiscal adjustments, or on sector-specific impacts
like financial markets, inflation, or employment. These fragmented analyses, while valuable,
fall short of capturing the economy-wide propagation mechanisms through which election-
related disturbances affect aggregate output, consumption, investment, and external accounts.
In the Philippines, most empirical work has emphasized descriptive or correlational approaches
rather than model-based simulations that integrate behavioral and structural relationships
among macroeconomic variables. It lacks a comprehensive, empirically estimated framework
that can quantify how political cycles, through fiscal impulses, policy uncertainty, or investor
sentiment, interact with the broader macroeconomic system. This limits policymakers’ ability
to distinguish between temporary election-induced booms and sustainable growth drivers.
Our study addresses this analytical and methodological gap by developing an augmented
macroeconometric model for the Philippines, building from the work of Debuque-Gonzales and
Corpus (2023, 2024), that explicitly incorporates election shocks. This enhancement allows for
a more rigorous understanding of the timing, magnitude, and persistence of election-related
effects on macroeconomic variables. By embedding electoral cycles as exogenous shocks
within the structural equations of the model, we can simulate how fiscal behavior, private
investment, and external balances respond under different election scenarios. Hence, we
contribute not only to the empirical literature on political business cycles but also to
macroeconomic policy design, providing evidence-based insights into how political events
5

shape cyclical fluctuations, fiscal sustainability, and long-term growth trajectories. It also
extends the capability of existing Philippine macroeconometric frameworks from merely
describing economic trends to explaining and forecasting politically driven economic
dynamics. This is a critical advancement for planning and fiscal management in the country.
3. Methodology
3.1. Conceptual framework
We build on the framework and model developed by Debuque-Gonzales and Corpus (2023,
2024) anchored on traditional macroeconometric models instead of micro-founded
macroeconomic models in response to the Lucas Crique. We continue to align with an empirical
approach to analyzing the transmission mechanism of election shocks to the macroeconomy
following Hendry (2020) citing the continued use of econometric approach to macroeconomic
analysis like the Federal Reserve Bank (FRB), the Norges Bank, the Reserve Bank of Australia
(RBA), the Bank of Canada, and the European Central Bank employing non-DSGE models.
Debuque-Gonzales and Corpus (2023, 2024) comprehensively reviewed the justifications for
the continued preference for empirical approaches. By integrating election shocks into the
macroeconometric model, we quantify how election cycles influence key macroeconomic
indicators as seen in Figure 1.
Figure 1. Model structure
Note: Orange boxes denote the exogenous variables in the model. Solid blue lines represent behavioral
relationships, while broken lines represent identities.
Source: Debuque-Gonzales and Corpus (2023, p. 21); Debuque-Gonzales and Corpus (2024, p. 6).
3.2. Operational framework
Following Debuque-Gonzales and Corpus (2023, 2024), we also adapted a pragmatic approach,
where the objective was to build a policy model guided by economic theory but can fit data
6

reasonably well. We emphasized on usability, tractability, and ease of maintenance, apart from
model  validity  and  robustness.  Table  1  shows  the  behavioral  equations  representing  the
macroeconomic variables in Figure 1.

Table 1. Model equations and variables
| Equations        |     |     |     | Variables                  |
| ---------------- | --- | --- | --- | -------------------------- |
| Domestic demand  |     |     |     | C = Household consumption  |
𝑏𝑏𝑏𝑏 𝑒𝑒 𝑒𝑒
log𝐶𝐶𝑡𝑡=𝑓𝑓(log(𝑌𝑌𝐷𝐷𝑡𝑡),𝑒𝑒𝑒𝑒𝑝𝑝𝑡𝑡,𝑟𝑟𝑡𝑡 −𝜋𝜋𝑡𝑡,𝜋𝜋𝑡𝑡)  CPI = Consumer Price Index
|     |     |     | 𝑏𝑏𝑏𝑏 𝑒𝑒 𝑒𝑒 | US  |
| --- | --- | --- | ---------- | --- |
log (𝐼𝐼𝑡𝑡)=𝑓𝑓(log(𝑌𝑌𝑡𝑡),Δ(𝑟𝑟𝑡𝑡 −𝜋𝜋𝑡𝑡),𝜋𝜋𝑡𝑡)  CPI  = US Consumer Price Index
𝑃𝑃𝑃𝑃
log𝐺𝐺𝑡𝑡=𝑓𝑓(𝑋𝑋𝑃𝑃𝑡𝑡 )  D  = National Government (NG) debt (nominal)
D
| log𝑀𝑀𝑡𝑡=𝑓𝑓(𝐼𝐼𝑡𝑡,𝑋𝑋𝑡𝑡)  |     |     |     | D  = Domestic NG debt (nominal)  |
| ---------------------- | --- | --- | --- | -------------------------------- |
F
𝑌𝑌𝑡𝑡≡𝐶𝐶𝑡𝑡+𝐼𝐼𝑡𝑡+𝐺𝐺𝑡𝑡+𝑋𝑋𝑡𝑡−𝑀𝑀𝑡𝑡  D = Foreign NG debt (nominal)
𝑇𝑇𝑇𝑇𝑇𝑇𝑇𝑇𝑃𝑃
| 𝑌𝑌𝐷𝐷𝑡𝑡≡𝑌𝑌𝑡𝑡−𝑅𝑅𝑉𝑉𝑡𝑡 |     |     |     | emp = Employment rate  |
| ------------------ | --- | --- | --- | ---------------------- |
𝑌𝑌
| log(𝑃𝑃𝑡𝑡)=𝑓𝑓(log(𝐶𝐶𝑃𝑃𝐼𝐼𝑡𝑡))   |     |     |     | G = Government consumption   |
| ----------------------------- | --- | --- | --- | ---------------------------- |
𝑁𝑁 𝑌𝑌
| 𝑌𝑌𝑡𝑡                   | ≡𝑃𝑃𝑡𝑡𝑌𝑌𝑡𝑡   |     |                    | I = Investment            |
| ---------------------- | ----------- | --- | ------------------ | ------------------------- |
|                        |             |     |                    | M = Imports               |
| Trade block            |             |     |                    | N X  = Net exports        |
|                        |             |     | 𝑊𝑊𝑊𝑊𝑃𝑃𝑊𝑊𝑊𝑊         | o il                      |
| log(𝑋𝑋𝑡𝑡)=𝑓𝑓(log (𝑌𝑌𝑡𝑡 |             |     | ),log(𝑥𝑥𝑟𝑟𝑟𝑟𝑡𝑡))   | p   = World price of oil  |
ric e
| log (𝑀𝑀𝑡𝑡)=𝑓𝑓(log(𝐼𝐼𝑡𝑡),log(𝑋𝑋𝑡𝑡))    |     |     |     | p   = Retail price of rice  |
| ------------------------------------- | --- | --- | --- | --------------------------- |
| 𝑁𝑁𝑋𝑋𝑡𝑡≡𝑋𝑋𝑡𝑡−𝑀𝑀𝑡𝑡                      |     |     |     | P B = Primary balance       |
Y
|     |     |     |     | P  = GDP de�lator  |
| --- | --- | --- | --- | ------------------ |
bl
| Employment block  |     |     |     | r  = Bank lending rate  |
| ----------------- | --- | --- | --- | ----------------------- |
cb
| 𝑒𝑒𝑒𝑒𝑝𝑝𝑡𝑡=𝑓𝑓(𝑌𝑌𝑡𝑡)   |     |     |     | r  = BSP policy rate  |
| ------------------- | --- | --- | --- | --------------------- |
dd
|     |     |     |     | r  = Effective interest rate on domestic debt  |
| --- | --- | --- | --- | ---------------------------------------------- |
df
| Price block  |     |          |          | r  = Effective interest rate on foreign debt  |
| ------------ | --- | -------- | -------- | --------------------------------------------- |
| Δlog(𝐶𝐶𝑃𝑃𝐼𝐼  |     | 𝑡𝑡 ) =   |          | RE S = Debt residual (nominal)                |
|              |     | 𝑜𝑜 𝑜𝑜 𝑏𝑏 | 𝑟𝑟𝑜𝑜𝑟𝑟𝑒𝑒 | bl                                            |
𝑓𝑓�Δlog�𝑝𝑝𝑡𝑡 �,Δlog�𝑝𝑝𝑡𝑡 �,Δlog(𝐷𝐷𝐷𝐷𝑡𝑡),Δlog(𝑥𝑥𝑟𝑟𝑡𝑡)�    rr   =  Real bank lending rate
|     |     | 𝐶𝐶𝑃𝑃𝑇𝑇𝑡𝑡 |     | t1 0 y |
| --- | --- | -------- | --- | ------ |
rr  = Real 10-year Treasury rate
| 𝜋𝜋𝑡𝑡≡100�𝐶𝐶𝑃𝑃𝑇𝑇𝑡𝑡−4−1�    |     |     |     | t91d |
| ------------------------- | --- | --- | --- | ---- |
rr  = Real 91-day Treasury rate
t10y
|     |     |     |     | r  = 10-year Treasury rate  |
| --- | --- | --- | --- | --------------------------- |
t10yUS
| M      | o netary  | block   |     | r  = US 10-year Treasury rate  |
| ------ | --------- | ------- | --- | ------------------------------ |
| 𝑟𝑟     | 𝑏𝑏        | 𝑒𝑒 𝑇𝑇   |     | t91d                           |
| 𝑟𝑟𝑡𝑡   | =𝑓𝑓(𝜋𝜋𝑡𝑡  | −𝜋𝜋𝑡𝑡)  |     | r  = 91-day Treasury rate      |
| 𝑡𝑡91𝑑𝑑 |           | 𝑟𝑟𝑏𝑏    | 𝑒𝑒  |                                |
𝑟𝑟𝑡𝑡 =𝑓𝑓(𝑟𝑟𝑡𝑡 ,𝑃𝑃𝐵𝐵𝑡𝑡/𝑌𝑌𝑡𝑡,𝜋𝜋𝑡𝑡)  RV = Total revenues (nominal)
| 𝑡𝑡10𝑦𝑦 |          | 𝑡𝑡91𝑑𝑑         | 𝑒𝑒  | NTX                                    |
| ------ | -------- | -------------- | --- | -------------------------------------- |
| 𝑟𝑟𝑡𝑡   | =𝑓𝑓(     | 𝑟𝑟 𝑡𝑡 , 𝜋𝜋𝑡𝑡)  |     | RV  = Non-tax revenues (nominal)       |
| 𝑏𝑏𝑏𝑏   |          | 𝑡𝑡1 0 𝑦𝑦 𝑒𝑒    |     | TX                                     |
| 𝑟𝑟𝑡𝑡   | =𝑓𝑓(𝑟𝑟𝑡𝑡 | ,𝜋𝜋𝑡𝑡)         |     | RV  =  Tax revenues (nominal)          |
|        | 𝑡𝑡91𝑑𝑑   | 𝑡𝑡91𝑑𝑑         |     | TXB IR                                 |
| 𝑟𝑟𝑟𝑟𝑡𝑡 | ≡𝑟𝑟𝑡𝑡    | −𝜋𝜋𝑡𝑡          |     | RV  = Internal tax revenues (nominal)  |
|        | 𝑡𝑡10𝑦𝑦   | 𝑡𝑡10𝑦𝑦         |     | TXBOC                                  |
RV  = Customs revenues (nominal)
| 𝑟𝑟𝑟𝑟𝑡𝑡 | ≡𝑟𝑟𝑡𝑡     | −𝜋𝜋𝑡𝑡  |     |              |
| ------ | --------- | ------ | --- | ------------ |
|        | 𝑏𝑏𝑏𝑏 𝑏𝑏𝑏𝑏 |        |     | X = exports  |
𝑟𝑟𝑟𝑟𝑡𝑡 ≡𝑟𝑟𝑡𝑡 −𝜋𝜋𝑡𝑡
|                  |          | 𝑈𝑈𝑈𝑈        |     | XP = Total expenditure (nominal)            |
| ---------------- | -------- | ----------- | --- | ------------------------------------------- |
|                  |          | 𝐶𝐶𝑃𝑃𝐼𝐼𝑡𝑡    |     | IND                                         |
| 𝑥𝑥𝑟𝑟𝑟𝑟𝑡𝑡=𝑥𝑥𝑟𝑟𝑡𝑡� |          |             |     | XP  = Domestic interest payments (nominal)  |
|                  |          | 𝑃𝑃𝐼𝐼𝑡𝑡      | �   | INF                                         |
|                  |          | 𝐶𝐶          |     | XP  = Foreign interest payments (nominal)   |
| 𝑑𝑑𝑑𝑑             |          | 𝑡𝑡10 𝑦𝑦     |     | INT                                         |
| 𝑟𝑟𝑡𝑡             | =𝑓𝑓�𝑟𝑟𝑡𝑡 | �           |     | XP  = Interest payments (nominal)           |
| 𝑑𝑑𝑑𝑑             |          | 𝑡𝑡10𝑦𝑦𝑈𝑈 𝑈𝑈 |     | PR                                          |
𝑟𝑟𝑡𝑡 =𝑓𝑓�𝑟𝑟𝑡𝑡 ,𝐷𝐷𝑌𝑌𝑡𝑡�    XP  = Primary expenditure (nominal)
xr = nominal peso-dollar exchange rate

xrr = real peso-dollar exchange rate
| Fiscal block  | 𝑇𝑇𝑇𝑇𝑇𝑇𝑇𝑇𝑃𝑃      |                 | 𝑁𝑁                                        |                                       |
| ------------- | --------------- | --------------- | ----------------------------------------- | ------------------------------------- |
| log(𝑅𝑅𝑉𝑉𝑡𝑡    |                 | )=𝑓𝑓(log(𝑌𝑌𝑡𝑡   |                                           | Y = GDP                               |
|               | 𝑇𝑇𝑇𝑇𝑇𝑇𝑊𝑊𝐶𝐶      |                 | ))                                        |                                       |
|               |                 |                 | 𝑌𝑌 𝑀𝑀𝑡𝑡),log(𝑝𝑝𝑡𝑡 𝑜𝑜𝑜𝑜𝑏𝑏 ),log(𝑥𝑥𝑟𝑟𝑡𝑡))   | Y D = disposable income               |
| log(𝑅𝑅𝑉𝑉𝑡𝑡    |                 | )=𝑓𝑓 (log(𝑃𝑃𝑡𝑡  |                                           | N                                     |
|               | 𝑁𝑁𝑇𝑇𝑇𝑇          |                 | 𝑁𝑁                                        | Y  = nominal GDP                      |
| log(𝑅𝑅𝑉𝑉𝑡𝑡    |                 | )=𝑓𝑓(log(𝑌𝑌𝑡𝑡   | ))                                        | WORLD                                 |
|               | 𝑇𝑇𝑇𝑇            | 𝑇𝑇𝑇𝑇𝑇𝑇𝑇𝑇𝑃𝑃      | 𝑇𝑇𝑇𝑇𝑇𝑇𝑊𝑊𝐶𝐶                                | Y  = World GDP                        |
| 𝑅𝑅𝑉𝑉𝑡𝑡        | ≡𝑅𝑅𝑉𝑉𝑡𝑡         |                 | +𝑅𝑅𝑉𝑉𝑡𝑡                                   |                                       |
|               |                 | 𝑇𝑇𝑇𝑇            | 𝑁𝑁𝑇𝑇𝑇𝑇                                    | 𝛼𝛼= Share of domestic debt in total   |
| 𝑅𝑅𝑉𝑉𝑡𝑡≡𝑅𝑅𝑉𝑉𝑡𝑡 |                 | +𝑅𝑅𝑉𝑉𝑡𝑡         |                                           |                                       |
|               | 𝑃𝑃𝑃𝑃            |                 |                                           | 𝜋𝜋 = in�lation rate                   |
| log(𝑋𝑋𝑃𝑃𝑡𝑡    |                 | )=𝑓𝑓(𝐷𝐷𝑌𝑌𝑡𝑡)    |                                           | 𝑇𝑇                                    |
|               | 𝑇𝑇𝑁𝑁𝑇𝑇          | 𝑇𝑇𝑁𝑁𝑊𝑊          | 𝑇𝑇𝑁𝑁𝐼𝐼                                    | 𝜋𝜋 𝑒𝑒  = in�lation target (midpoint)  |
| 𝑋𝑋𝑃𝑃𝑡𝑡        | ≡𝑋𝑋             | 𝑃𝑃 𝑡𝑡 +         | 𝑋𝑋 𝑃𝑃 𝑡𝑡                                  |                                       |
|               |                 | 𝑃𝑃 𝑃𝑃           | 𝑇𝑇 𝑁𝑁 𝑇𝑇                                  | 𝜋𝜋𝑡𝑡  = expected in�lation rate       |
| 𝑋𝑋𝑃𝑃𝑡𝑡≡𝑋𝑋𝑃𝑃𝑡𝑡 |                 | +𝑋𝑋𝑃𝑃𝑡𝑡         |                                           |                                       |
|               | 𝑇𝑇𝑁𝑁𝑊𝑊          | 𝑑𝑑𝑑𝑑            | 𝑊𝑊                                        |                                       |
| 𝑋𝑋𝑃𝑃𝑡𝑡        | ≡𝑟𝑟𝑡𝑡           | ×𝐷𝐷𝑡𝑡−1         |                                           |                                       |
|               | 𝑇𝑇𝑁𝑁𝐼𝐼          | 𝑥𝑥𝑟𝑟𝑡𝑡          | 𝑑𝑑𝑑𝑑 𝐼𝐼                                   |                                       |
| 𝑋𝑋𝑃𝑃𝑡𝑡        | ≡�𝑥𝑥𝑟𝑟𝑡𝑡−1�𝑟𝑟𝑡𝑡 |                 | 𝐷𝐷𝑡𝑡−1                                    |                                       |
𝑃𝑃𝑃𝑃
| 𝑃𝑃𝐵𝐵𝑡𝑡≡𝑅𝑅𝑉𝑉𝑡𝑡−𝑋𝑋𝑃𝑃𝑡𝑡 |     |     |     |     |
| -------------------- | --- | --- | --- | --- |
𝑥𝑥𝑟𝑟𝑡𝑡
|             | 𝑇𝑇𝑁𝑁𝑇𝑇 | 𝑊𝑊                                         | 𝐼𝐼  |     |
| ----------- | ------ | ------------------------------------------ | --- | --- |
| 𝐷𝐷𝑡𝑡≡𝑋𝑋𝑃𝑃𝑡𝑡 |        | +𝐷𝐷𝑡𝑡−1+�𝑥𝑥𝑟𝑟𝑡𝑡−1�𝐷𝐷𝑡𝑡−1−𝑃𝑃𝐵𝐵𝑡𝑡+𝑅𝑅𝑅𝑅𝑆𝑆𝑡𝑡   |     |     |
𝑊𝑊
So𝐷𝐷𝑡𝑡 𝑡𝑡 𝑡𝑡
u𝐼𝐼r≡ce𝛼𝛼:  𝐷𝐷C o  rpus and Debuque-Gonzales (2023, p. 3).
𝐷𝐷𝑡𝑡 ≡(1−𝛼𝛼𝑡𝑡)𝐷𝐷𝑡𝑡

Similar to Debuque-Gonzales and Corpus (2023, 2024), we continue to adopt a stylized
framework where output is determined from the demand side, as in earlier Keynes-based

7

models and some other small macroeconometric models (Hammersland and Træe 2014;
Kasimati and Dawson 2009).
Debuque-Gonzales and Corpus (2023) introduced the following shocks: “a positive shock to
government consumption; a positive shock to world oil prices; and a recession in the country’s
major export partners” (p. 32). Meanwhile, Debuque-Gonzales and Corpus (2024) made an
extension by also considering the following shocks: “a world oil price shock, an exchange rate
shock, and a primary spending shock” (p. 19). We build on Debuque-Gonzales and Corpus
(2023, 2024) by introducing impulse (temporary) shocks to the exogenous variables and
examine the reaction of the endogenous variables relative to their baseline paths from the
deterministic dynamic simulation. Thus, we introduce election spending shock in the domestic
demand block by simultaneously altering the private consumption and government
consumption equations (e.g., introduce shocks through the structural equations in Figure 2,
and/or inflate the variables by x percent, where x can be 0.10, 0.15, and 0.20). With this, we
assess the ability of the model, simulated as a complete system, to generate forecasts that are
close to the actual data. Both in-sample and out-of-sample model evaluations were conducted.
3.3. Estimation
Behavioral equations were estimated11 using the Autoregressive Distributed Lag (ARDL)
method in Error Correction Model (ECM) form. Lag lengths were optimally selected using the
Akaike Information Criterion (AIC) restricted to a maximum of 2 lags. Cointegration between
level variables was tested using the bounds test approach developed by Pesaran et al. (2001).
We chose specifications such that estimated coefficients of variables that enter the long-run
equation display signs consistent with theory; variables with parameters that failed to conform
with expectations based on either theory or intuition were relegated to the short-run equation or
omitted altogether. In cases where the bounds test indicated the absence of cointegration,
behavioral relationships were modeled as a short-run equation in first differences. Residual
diagnostic checks testing for homoskedasticity, serial correlation, and normality were
performed to ensure model adequacy. Appendix 1 shows the results of the stability tests.
Quarterly data spanning from the first quarter of 2002 to the fourth quarter of 2023 (2022Q1 to
2023Q4) were used in the model, covering a more extended period than that employed by
Debuque-Gonzales and Corpus (2023, 2024) by an additional four years. Data were sourced
from the CEIC Economic Database12 and all series were seasonally adjusted using the X-13
routine prior to estimation to ensure comparability and remove regular seasonal effects.
Appendix 2 shows the descriptive statistics. Results from Augmented Dickey–Fuller (ADF)
tests indicated that most series were either integrated of order I(1) or stationary at level I(0),
confirming their suitability for econometric modeling. Appendix 3 shows the results of
stationarity tests.
The inclusion of the coronavirus (COVID-19) pandemic years (2020 to 2023) is justified on
both methodological and economic grounds. While we recognize that these years represent
atypical macroeconomic conditions, we retained them in the sample to ensure a comprehensive
representation of the Philippine economy’s evolution over time. See the succeeding section for
a detailed discussion on how the model empirically accounts for pandemic-specific shocks.
11 EViews was used to solve the model, combining estimated behavioral equations and identities to obtain the dynamic numerical
solution for simulation. The model was solved using the Broyden solution algorithm. For a description, see IHS Markit (2020,
pp.1044 and 1324).
12 Offers a global database with macroeconomic data from official sources, international institutions, and alternative data to help
economists and investors track and analyze global trends. Website: https://www.ceicdata.com/en.
8

From an econometric standpoint, excluding these years would truncate the dataset and risk
introducing bias into the long-run estimates by omitting a structural shock of unprecedented
magnitude that influenced virtually all macroeconomic aggregates. Including this period allows
the model to capture and differentiate extraordinary, non-cyclical disturbances from regular
election-related fluctuations, thereby enhancing the robustness of parameter estimates and
improving the model’s out-of-sample forecasting accuracy.
Second, from an economic standpoint, the pandemic period provides valuable insights into how
policy responses and economic behavior adjust under extreme shocks, including fiscal stimulus,
mobility restrictions, and shifts in consumption and investment patterns. These dynamics mirror
the shock-transmission mechanisms, both demand- and policy-driven, that are central to this
study’s examination of election-induced disturbances. Including pandemic data thus broadens
the model’s empirical base, enabling it to account for both exogenous global crises and
domestic political cycles, and to test whether election shocks produce comparable
macroeconomic effects or interact with crisis-related volatility.
Hence, the 2002 to 2023 data points provide a comprehensive temporal coverage that
encapsulates multiple electoral cycles, episodes of macroeconomic expansion and contraction,
and the unprecedented COVID-19 disruption, offering a richer foundation for evaluating the
transmission of election shocks within the Philippine macroeconomy.
4. Results and discussion
4.1. Model evaluation
Following the earlier iterations by Debuque-Gonzales and Corpus (2023, 2024), we also focus
on the model’s dynamic forecasting performance. As indicated earlier, our sample period was
extended to cover data from 2002Q1 to 2023Q4, thereby incorporating recent economic
developments and policy episodes. This inclusion necessitated accounting for the COVID-19
pandemic period, an unprecedented disruption to the Philippine economy.
To control for pandemic effects, a dummy variable, equal to one from 2020Q2 to 2021Q2, was
introduced in the behavioral equations. This period represents the span of maximum economic
disruption and intensive policy response. The starting point coincides with the country’s entry
into a technical recession (Congressional Policy and Budget Research Department [CPBRD]
2020), while the endpoint reflects the onset of sequential economic recovery and the rollout of
mass vaccination campaigns (Department of Health [DOH] 2021; Philippine Statistics
Authority [PSA] 2021; World Bank [WB] 2021). While the use of a single binary variable
simplifies a complex and evolving crisis, it provides a tractable way to capture the pandemic’s
immediate structural shock and the government’s corresponding emergency policy
interventions within the model’s framework. Future refinements may consider alternative
specifications, such as structural-break tests, regime-switching parameters, or distributed-lag
formulations to better encapsulate pandemic-related uncertainties.
Model evaluation, as seen in Figure 2 and Table 2, focused on assessing predictive capability
using standard forecast accuracy metrics, specifically, the mean absolute percentage error
(MAPE) and mean absolute error (MAE). The MAPE was applied to level variables, while the
MAE was used for percentage and rate variables, as seen in Table 2. Overall, forecasts for GDP
and GDP growth demonstrated reasonable predictive accuracy, with estimated paths closely
tracking the actual de-seasonalized series. Among GDP components, private consumption,
9

government consumption, and exports registered MAPEs of approximately 2%, 4%, and 5%,
respectively. Slightly higher errors were observed for investment and imports, reflecting
modest divergence between actual and predicted values during 2017 to 2022. This affected net
exports toward the end of the sample.
For tax revenues, including internal and customs revenues, the MAPE remained below 10%,
only marginally higher than in earlier model versions. Non-tax revenues, however, recorded a
higher MAPE of around 15%, due mainly to transient spikes during specific quarters, as seen
in Figure 2. Interest payments followed the general trend of the actual data, though the forecast
error was elevated in the first two years and again toward the latter part of the sample,
particularly when disaggregated into domestic and foreign components. Dynamic forecasts for
national government debt aligned closely with observed data, though a widening gap was noted
near the end of the series. However, the MAPE was nearly identical from the previous iteration.
For percentage and rate variables, the model also displayed satisfactory predictive
performance. Employment rate had an MAE of about 0.7, maintaining close alignment with
observed trends. Inflation forecasts showed minor deviations, especially during 2020,
consistent with pandemic-induced price volatility. Similarly, forecasts for bank lending and for
91-day and 10-year treasury bill rates exhibited modest divergences yet remained within
acceptable margins, with MAEs of roughly 1.2, 2.3, and 2.0, respectively. When adjusted for
real terms, these financial variables displayed forecast paths consistent with observed data.
The remaining forecast deviations, particularly during and immediately after the pandemic
period, likely reflect the heightened uncertainty and nonlinear adjustments that are inherently
challenging to capture within a small-scale macroeconometric model. Nonetheless, the
extended model maintains a commendable level of accuracy, demonstrating its robustness in
tracking both normal cyclical fluctuations and exceptional economic shocks such as the
COVID-19 crisis.
Figure 2. In-sample simulations
10

|     |     |     |     |
| --- | --- | --- | --- |
|     |     |     |     |
|     |     |     |     |
|     |     |     |     |
|     |     |     |     |
|     |     |     |     |
|     |     |     |     |

11

|     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- |
|     |     |     |     |     |     |
|     |     |     |     |     |     |
|     |     |     |     |     |     |
|     |     |     |     |     |     |
Note: Blue lines are the actual data, while the broken red lines are the dynamic forecasts.
Source: Authors’ calculations.

Table 2. Evaluation of in-sample forecast accuracy, 2021Q1-2023Q4
Mean absolute percentage error (MAPE) of level variables, in percent
|     |                                     | GDP               |     | 2.617   |     |
| --- | ----------------------------------- | ----------------- | --- | ------- | --- |
|     | Household consumption               |                   |     | 2.280   |     |
|     |                                     | Investment        |     | 9.694   |     |
|     | Government consumption              |                   |     | 4.186   |     |
|     |                                     | Exports           |     | 5.223   |     |
|     |                                     | Imports           |     | 7.923   |     |
|     |                                     | Net exports       |     | 22.634  |     |
|     |                                     | Nominal revenues  |     | 6.236   |     |
|     | Nominal tax revenues                |                   |     | 5.997   |     |
|     | Nominal internal tax revenues       |                   |     | 6.687   |     |
|     | Nominal customs revenues            |                   |     | 8.682   |     |
|     | Nominal non-tax revenues            |                   |     | 15.820  |     |
|     | Nominal NG expenditure              |                   |     | 5.728   |     |
|     | Nominal interest payments           |                   |     | 19.242  |     |
|     | Nominal domestic interest payments  |                   |     | 20.704  |     |

12

| Nominal foreign interest payments  | 17.509  |     |
| ---------------------------------- | ------- | --- |
| Nominal primary expenditure        | 6.533   |     |
| NG debt                            | 7.737   |     |
| Domestic NG debt                   | 7.737   |     |
| Foreign NG debt                    | 7.734   |     |
| GDP deflator                       | 4.386   |     |
Mean absolute error (MAE) of rate and percentage variables, in percentage points
| GDP growth                        | 2.448  |     |
| --------------------------------- | ------ | --- |
| Employment rate                   | 0.691  |     |
| CPI inflation                     | 2.293  |     |
| BSP policy rate                   | 1.315  |     |
| 91-day Treasury rate              | 2.287  |     |
| 10-year Treasury rate             | 1.961  |     |
| Bank lending rate                 | 1.212  |     |
| Real 91-day Treasury rate         | 1.780  |     |
| Real 10-year Treasury rate        | 1.749  |     |
| Real bank lending rate            | 1.987  |     |
| Effective domestic interest rate  | 0.197  |     |
| Effective foreign interest rate   | 0.117  |     |
| Revenue/GDP                       | 0.677  |     |
| Tax revenue/GDP                   | 3.011  |     |
| Internal tax revenue/GDP          | 0.328  |     |
| Customs revenue/GDP               | 0.266  |     |
| Non-tax revenue/GDP               | 0.267  |     |
| Expenditure/GDP                   | 1.240  |     |
| Primary spending/GDP              | 1.428  |     |
| Interest payments/GDP             | 0.379  |     |
| Foreign interest payments/GDP     | 0.106  |     |
| Domestic interest payments/GDP    | 0.292  |     |
| Primary balance/GDP               | 1.418  |     |
| Fiscal balance/GDP                | 1.286  |     |
| Debt/GDP                          | 3.805  |     |
| Domestic debt/GDP                 | 2.520  |     |
| Foreign debt/GDP                  | 1.287  |     |
Source: Authors’ calculations.

4.2. Impact analysis of election-related spending shock

Defining election spending shock. We define an election spending shock as the four quarters
preceding a Philippine national election, consistent with the empirical timing of political budget
cycles observed across both developed and emerging economies (Brender and Drazen 2005;
Shi and Svensson 2006; Drazen and Eslava 2010). In our study, shocks are introduced in
2015Q3 to 2016Q2 and 2018Q3 to 2019Q2, corresponding to the lead-up periods of the 2016
and 2019 elections.

Scope of macroeconomic variable selection. While Table 1 lists various macroeconomic
variables used in the model, we only focus on private consumption, employment, investment,
and government consumption because these variables represent the core transmission channels
of election-related shocks identified in theory and empirical literature. That is, election cycles
primarily operate through fiscal expansions and liquidity injections, influencing aggregate
demand rather than supply-side fundamentals (Rogoff and Sibert 1988; Drazen and Eslava

13

2010). These four variables capture the direct behavioral responses of households, firms, and
the public sector to election-driven spending.
Our selected macroeconomic variables also exhibit clear and measurable variations during
election years in Philippine national accounts. In contrast, other macroeconomic indicators
such as inflation, external balance, or interest rates tend to be indirectly affected, with weaker
or lagged responses that are harder to isolate from concurrent global or policy shocks (e.g.,
commodity price movements, monetary tightening). Equally important, given the small-scale
structure of the macroeconometric model, including additional variables risks introducing
multicollinearity and parameter instability. Restricting interpretation to the principal demand-
side variables ensures a more robust and interpretable simulation of election-shock
transmission. Ultimately, our selected macroeconomic variables also provide the most
actionable insights for fiscal and development planning. Understanding the dynamics of
consumption, investment, employment, and public expenditure directly informs
countercyclical policy design and resource allocation in election years.
Hence, by concentrating on these core aggregates, we capture the most salient and empirically
verifiable pathways through which election shocks influence the Philippine economy, while
maintaining methodological rigor and analytical focus.
Shock assumptions. To simulate these shocks, private domestic demand, comprising
household consumption and private investment, is assumed to increase by 7%, 8%, 14%, and
9% in each of the four pre-election quarters, while government consumption rises by 8%, 9%,
15%, and 10%, respectively. These magnitudes are grounded in both domestic and international
empirical evidence showing that election years are typically associated with elevated economic
activity, primarily driven by heightened public expenditure and election-induced private
spending. That is, the percentages introduced were based on the historical change in
consumption and government spending for that particular quarter in the Philippines. Studies
such as Rogoff and Sibert (1988) and Schultz (1995) established that incumbents often engage
in expansionary fiscal policies prior to elections, while Akhmedov and Zhuravskaya (2004)
and Drazen and Eslava (2010) confirmed that such spending creates short-lived surges in output
and consumption. Philippine evidence also supports this pattern. Evangelista and Libre (2008)
and Habito (2013) noted that national income growth typically accelerates in election years due
to campaign-related activities, expanded government outlays, and higher liquidity in
circulation.
Thus, our shock assumptions reflect the observed behavioral and fiscal regularities of the
Philippine political cycle namely, frontloaded government spending, elevated household
consumption, and temporary investment expansion driven by improved liquidity and
sentiment. Consistent with the approach adopted in political business cycle literature, the model
is solved under both baseline and shock scenarios for the sample period 2012Q1 to 2023Q4,
generating dynamic forecasts for endogenous variables. These simulations, as seen in Figure
3, provide a quantitative basis to evaluate how pre-election demand impulses transmit through
the Philippine macroeconomy and how quickly such effects dissipate once election-related
activities subside.
Response of private consumption. Solving the model under the generated shock scenario
produced a notable increase in private consumption relative to the baseline. During the 2016
election cycle, consumption rose by approximately 8.3%, 9.5%, 15.7%, and 10.7% in 2015Q3
to 2016Q2, while in the 2019 cycle it increased by 10.7%, 10.8%, 18.2%, and 14.4% in 2018Q3
14

to 2019Q2. These results confirm that election periods are associated with discernible surges
in private domestic demand, consistent with the empirical evidence of pre-election fiscal
expansions observed in both developing and emerging economies (Brender and Drazen 2005;
Shi and Svensson 2006; Drazen and Eslava, 2010).
From Figure 3, the model also captures the transitory nature of this consumption boost. In the
quarters immediately following an election, household consumption reverts toward its baseline
trajectory, reflecting the dissipation of election-related spending once campaign activities
conclude. The temporary spike in consumption highlights the unsustainable and short-lived
nature of election-induced demand surges, a feature well-documented in studies of political
budget cycles (Rogoff and Sibert 1988; Schultz 1995).
This short-term uplift is partly driven by policies and fiscal measures implemented or
accelerated ahead of elections to increase disposable income, such as cash transfers, subsidies,
or targeted social aid programs (Labonne 2016; Lokshin et al. 2022). These measures often
expand liquidity among select demographic segments, temporarily boosting household
consumption without creating lasting welfare gains. Additionally, political campaign spending,
through wages, logistics, and advertising, injects short-term liquidity into the economy,
stimulating short-lived consumer spending (Olano 2019).
Beyond these direct income effects, consumer sentiment also appears to play a role. As Cipullo
and Reslow (2022) observed, governments tend to release optimistic growth forecasts before
elections, potentially shaping public expectations and encouraging households to spend more
in anticipation of continued economic expansion. However, such optimism often proves
temporary, leading to a normalization of consumption behavior once post-election realities and
fiscal adjustments set in.
Response of employment. Furthermore, the injection of liquidity into households during
election periods can be partly attributed to campaign mobilization and the creation of temporary
“election jobs.” As seen in Figure 3, employment rises in tandem with heightened economic
activity, particularly in the first quarters of election years (2016Q1 and 2019Q1), when the
model estimates an average employment increase of about 2.7 percent relative to the baseline.
This result aligns with evidence from political business cycle studies showing that pre-election
spending spurs temporary employment in construction, logistics, and service sectors associated
with campaign and government activities (Akhmedov and Zhuravskaya 2004; Labonne 2016).
However, the model also reflects the ephemeral nature of such gains. Once election-related
activities subside, the employment variable converges toward its baseline level, signifying the
disappearance of short-term and informal election-linked jobs. This cyclical pattern mirrors
findings in emerging economies, where politically induced labor demand expands briefly
before elections and subsequently contracts when fiscal and campaign spending normalizes
(Shi and Svensson 2006; Drazen and Eslava 2010).
Response of investment. For investment, the simulation indicates deviations of approximately
4.5%, 5.4%, 10.8%, and 9.1% from the baseline during 2015Q3 to 2016Q2, reflecting a
discernible rise in capital formation during the pre-election period. From Figure 3, investment
activity continues to strengthen modestly in the post-election quarters, suggesting an
improvement in investor sentiment once political uncertainty subsides. The results imply that
while pre-election fiscal expansion temporarily boosts demand-driven investment, the
15

subsequent resolution of electoral uncertainty can foster a mild but sustained rebound in private
capital spending.
Empirical evidence supports this dual mechanism. Although findings on election-related
investment behavior are mixed, there is broad consensus that election periods stimulate private
domestic demand, creating short-term conditions favorable to investment (Le et al. 2024;
Azzimonti 2024; Inosante 2025). Heightened consumption and government expenditure may
prompt firms to expand production capacity or upgrade operations to meet increased demand.
Moreover, sector-specific effects emerge as industries directly linked to electoral activity, such
as media, advertising, logistics, and printing, register temporary surges in output, leading to
targeted capital injections in these areas (Drazen and Eslava 2010).
At the same time, election cycles may influence investment indirectly through infrastructure
continuity. The sustained implementation of Public-Private Partnership (PPP) projects, many
of which are exempted from the election spending ban, provides a stabilizing channel for
private investment even amid political transitions (Commission on Elections [COMELEC]
2018; Aning, 2024). This finding aligns with cross-country studies highlighting that policy
credibility and ongoing public investment programs can partially offset uncertainty effects
during election periods (Julio and Yook 2012; Shi and Svensson, 2006). Overall, the simulated
outcomes suggest that while election shocks generate short-term investment accelerations, the
extent to which these persist depends on the post-election policy environment and the
continuity of major infrastructure initiatives.
Response of government consumption. The shock analysis reveals that government
consumption increased by approximately 7% to 14% in the quarters preceding the 2016
election and by 9.5% to 12.6% ahead of the 2019 election. This pattern affirms that Philippine
election years typically witness an acceleration of public expenditure in anticipation of the
statutory election spending ban, encompassing infrastructure outlays, social assistance
programs, and the administrative costs of election operations (Das et al. 2025; Cigaral 2025).
Similar to household consumption, government spending displays a cyclical moderation in
non-election years, returning to near-baseline levels once electoral activities conclude.
These findings align with the broader PBC literature, which demonstrates that incumbents often
employ expansionary fiscal policies before elections to influence voter perceptions, followed
by contractionary adjustments post-election (Rogoff and Sibert 1988; Schultz 1995; Peters
2010; Labonne 2016). The model likewise shows spending slowdowns before and after
elections, with government consumption trending close to or even slightly below the baseline
between 2015Q3 and 2016Q2, mirroring the empirical results of Evangelista and Libre (2008)
for the Philippines. This suggests a pattern of fiscal frontloading, an intentional acceleration of
expenditures before the COMELEC spending ban, particularly for infrastructure projects and
social welfare programs, which are often justified as development priorities but may also serve
political signaling purposes.
However, such behavior carries macroeconomic and developmental trade-offs. While election-
driven fiscal expansions provide a temporary stimulus, they can also distort expenditure
composition, diverting resources toward short-term, highly visible projects at the expense of
long-term investments (Labonne 2016; De Haan et al. 2023; Punongbayan 2025). This
reallocation may reduce fiscal efficiency, undermining the sustainability of growth once
political incentives dissipate. Thus, results echo the consensus in empirical research. Although
16

election-induced spending cycles can generate brief economic gains, their cumulative effect
may weaken fiscal discipline and development outcomes in the long run.

Figure 3. Election spending shock scenario
|     |     |     |
| --- | --- | --- |
|     |     |     |
|     |     |     |

|     |     |     |
| --- | --- | --- |
|     |     |     |

|     |     |     |
| --- | --- | --- |

17

|     |     |     |
| --- | --- | --- |
|     |     |     |
|     |     |     |

|     |     |     |
| --- | --- | --- |
|     |     |     |

|     |     |     |
| --- | --- | --- |

Note: Green lines are the baseline, while the broken red lines are the shock scenario.
Source: Authors’ calculation.

Key findings. From Figure 3, we can construe that election years in the Philippines generate
short-term, demand-driven expansions in key macroeconomic aggregates, consistent with PBC
theory. We highlight that private consumption surged significantly by 8% to 16% during 2016
and 11% to 18% during 2019 election quarters. This is reflective of higher disposable income,
intensified  campaign  activity,  and  optimistic  expectations.  This  confirms  the  temporary
consumption boost identified by Rogoff and Sibert (1988), Shi and Svensson (2006), and
Evangelista and Libre (2008). For employment, we have seen it rise by roughly 2.7% in early
election quarters, capturing the creation of short-term “election jobs.” However, this effect
quickly dissipated post-election, consistent with Akhmedov and Zhuravskaya (2004) and
Labonne (2016).

18

Meanwhile, private investment exhibited moderate pre-election growth of 4% to 11% driven
by increased demand and the continuation of PPP projects, though partly offset by election-
related uncertainty (Julio and Yook 2012; Drazen and Eslava 2010). Similarly, government
consumption expanded by 7% to 14% before elections and normalized afterward, mirroring
evidence of fiscal frontloading and subsequent retrenchment typical of political budget cycles
(Brender and Drazen 2005; De Haan et al. 2023).
Together, these patterns illustrate that election shocks transmit primarily through the demand
side of the economy, via household spending, employment, investment, and government
outlays, producing short-term macroeconomic acceleration that is not sustained once electoral
incentives subside.
Validation with scholarly literature. To assess the model’s consistency with empirical
findings, we benchmarked our simulation results against established scholarly literature across
four analytical dimensions: (1) magnitude and timing; (2) transmission channels; (3)
persistence; and (4) investment ambiguity. Table 3 summarizes the validation of these
dimensions against key studies.
Table 3. Validation of empirical results
Dimensions Results Reference
The four-quarter, front-loaded shock matches Shi and Svensson
Magnitude and
canonical PBC timing with visible fiscal expansions in (2006); Brender and
timing
the year before elections. Drazen (2005)
Results underscore demand-side transmission from
Transmission Drazen and Eslava
consumption to output, employment, and
channels (2010)
composition effects in public outlays.
Rapid post-election mean reversion in consumption
Brender and Drazen
and employment is consistent with PBC models
Persistence (2005); Rogoff and
where the incentive is temporary and with evidence
Sibert (1988)
that expansions do not durably raise trend growth.
The model’s short-run investment bump coexists
with scholarly literature’s uncertainty-induced
Investment Julio and Yook
deferral at the microeconomic level suggesting that
ambiguity (2012).
macroeconomic demand can partially offset firm-
level caution in election-exposed industries.
Source: Authors’ tabulation.
5. Ways forward
5.1. Conclusions
We have examined the transmission of election shocks in the Philippine economy through an
augmented macroeconometric model developed by Debuque-Gonzales and Corpus (2023,
2024). Using quarterly data from 2002 to 2023, the model simulated the effects of pre-election
demand surges on key macroeconomic aggregates namely private consumption, investment,
employment, and government consumption. Our results confirmed that election periods in the
Philippines are associated with short-term, demand-driven expansions consistent with the
predictions of PBC theory. Private consumption, government spending, and employment all
rise significantly in the quarters preceding elections, reflecting heightened fiscal disbursements,
19

campaign-related expenditures, and temporary labor creation. Investment also shows moderate
gains, supported by buoyant demand and infrastructure continuity, though partially tempered
by election-related uncertainty.
However, these effects are transitory. Post-election normalization occurs rapidly as fiscal
activities contract and private confidence adjusts, highlighting the cyclical and unsustainable
nature of election-induced growth. The model’s findings align with scholarly literature (Rogoff
and Sibert 1988; Brender and Drazen 2005; Drazen and Eslava 2010), which similarly identifies
temporary expansions followed by corrective adjustments in fiscal behavior.
Overall, we have underscored that while election shocks provide short-term stimulus, they also
reveal structural vulnerabilities in fiscal discipline, expenditure allocation, and policy
continuity. Election-related economic activity boosts aggregate demand but may distort
development priorities, exacerbate clientelism, and undermine long-term fiscal sustainability.
5.2. Policy recommendations
Building on our findings, we outline policy measures to manage the short-term economic
fluctuations arising from election-related activities. While we have seen that election periods
provide a temporary boost to consumption, investment, and employment, these gains are largely
transitory and fiscally driven. To ensure that such cycles do not compromise fiscal sustainability
or long-term development priorities, the following recommendations, seen in Table 4, focus on
strengthening institutional discipline, improving expenditure quality, enhancing transparency,
and fostering macroeconomic stability during and beyond election years.
Table 4. Policy recommendations
Policy recommendation Implementation scheme
To mitigate the volatility associated with election cycles, government
agencies should strengthen adherence to fiscal rules that limit
Institutionalize fiscal
discretionary spending before elections. Establishing medium-term
rules and pre-election
expenditure frameworks and transparent reporting of pre-election
spending discipline
disbursements can reduce the scope for politically motivated fiscal
expansion.
Rather than short-lived consumption-driven outlays, fiscal efforts
during election years should prioritize capital-forming investments
Prioritize capital-forming
(i.e., infrastructure, human capital, and climate resilience) that yield
and inclusive
longer-term productivity gains. Such reorientation minimizes waste
expenditures
and ensures that electoral cycles do not compromise developmental
integrity.
Commission on Audit (COA), COMELEC, and Department of Budget and
Management (DBM) should collaborate on real-time monitoring of
Enhance transparency in
government spending patterns during election periods. Public
budget execution and
disclosure of infrastructure disbursements, subsidy releases, and
electoral financing
transfers would improve accountability and help deter opportunistic
fiscal manipulation.
To cushion the economy from post-election slowdowns, the
Strengthen automatic government should enhance automatic stabilizers (e.g.,
stabilizers and counter- unemployment insurance, targeted social protection, progressive
cyclical policy tools taxation). This would help sustain aggregate demand and maintain
stability without resorting to politically driven fiscal impulses.
20

Continuity of PPP and flagship infrastructure projects should be
Maintain continuity of insulated from political transitions to maintain investor confidence.
infrastructure and PPP Expanding the exemption of ongoing PPP projects from the election
programs spending ban ensures policy predictability, supporting private
investment even during periods of political uncertainty.
We highlight the need for higher-frequency and disaggregated data on
government spending and campaign-related activity to deepen
Improve data collection
analysis of political business cycles. Integrating political economy
and political economy
variables into national forecasting frameworks (e.g., DEPDev, DBM,
analysis
BSP) would allow for more realistic macroeconomic projections during
election years.
Source: Authors’ tabulation.
5.3. Limitations and areas for future studies
While we have offered valuable insights into the transmission of election shocks within the
Philippine economy, several limitations emerged in the course of model development and
simulation that future research may address.
First is on model stability and specification issues. As with any small-scale macroeconometric
model, maintaining parameter stability across extended periods remains a challenge. The
inclusion of multiple structural breaks, such as the 2008 Global Financial Crisis (GFC), the
COVID-19 pandemic, and changes in fiscal regimes, may have introduced instability in long-
run relationships among variables. Future studies should explore model re-specification or re-
estimation using time-varying parameters, structural break tests, or Bayesian updating
techniques to improve robustness over changing macroeconomic environments.
Second is on the impact of atypical years and structural shocks. Our analysis covered years
characterized by atypical and extraordinary economic conditions, particularly the COVID-19
pandemic (i.e., 2020 to 2022). While we have employed dummy variables to account for these
shocks, such a simplified treatment may not fully capture the depth and persistence of
pandemic-induced disruptions, including behavioral shifts in consumption, investment, and
labor market dynamics. Future studies could adopt nonlinear or regime-switching models to
distinguish between ordinary cyclical shocks and extraordinary global crises.
Third is on post-COVID-19 structural changes. We recognize that the post-pandemic period
introduced significant structural changes (e.g., digital transformation, altered household
spending patterns, supply chain reconfigurations) that the current model, calibrated on pre-2020
relationships, may only partially reflect. Thus, a full rewriting or recalibration of the
macroeconometric model may be warranted to capture these evolving structural parameters,
particularly in labor productivity, consumption behavior, and fiscal multipliers.
Fourth, future research could extend the analysis by estimating election-shock impacts at the
sectoral level, specifically across agriculture, industry, and services. Such disaggregation would
provide deeper insight into how political cycles affect sector-specific dynamics, such as
employment and output composition. However, this approach would require consistent and
high-frequency sectoral time series data, and may necessitate the development of separate
sectoral macroeconometric models rather than an aggregate one, given differences in structural
behavior and data availability.
21

Fifth, future research may also extend the analysis to examine the qualitative influence of
election outcomes, particularly the characteristics of winning candidates or administrations.
Beyond fiscal behavior and macroeconomic trends, future models could incorporate leadership
attributes (e.g., integrity, credibility, professional background, policy platforms, and
governance orientation) as variables that may shape post-election economic performance. This
approach would allow for an assessment of how political leadership quality affects investor
confidence, fiscal prudence, and macroeconomic stability. However, such an extension would
require developing quantifiable proxies for leadership traits and compiling corresponding post-
election economic indicators, posing both methodological and data challenges that warrant
dedicated empirical exploration.
Sixth, is on the practical versus theoretical application. While we aligned with econometric
rigor, the model’s usability for real-time decision-making remains limited relative to the needs
of the private sector. Business and investment analysts often prioritize practical forecasting and
scenario tools over structural rigor. Future extensions may consider developing simplified or
hybrid models such as integrating macroeconometric foundations with business-cycle
indicators to enhance practical relevance for private-sector users while maintaining analytical
credibility.
Thus, these limitations point to promising directions for future studies. Refining the model’s
structure, enhancing its adaptability to non-traditional shocks, and bridging the gap between
academic modeling and policy or market applications can help build a more resilient, context-
sensitive macroeconometric framework for the Philippines that is capable of capturing both
cyclical and structural dynamics in a rapidly evolving economic landscape.
6. References
Adams, J. J., & Barrett, P. (2023, September 29). Identifying news shocks from forecasts
(Working Paper No. 2023/208). International Monetary Fund.
https://www.imf.org/en/Publications/WP/Issues/2023/09/29/Identifying-News-Shocks-
from-Forecasts-539674 (accessed March 5, 2025).
Akhmedov, A., & Zhuravskaya, E. (2004). Opportunistic political cycles: test in a young
democracy setting. Journal of Public Economics, 88(9–10), 2079–2105.
Alarcon, S. J., Alhambra, P. R., Amodia, R., & Bautista, D. (2020, December). Policy
analysis model for the Philippines (BSP Working Paper Series No. 2020-12). Bangko
Sentral ng Pilipinas. https://www.bsp.gov.ph/Sites/researchsite/Publications/BSP-
Working-PaperSeries/WPS202012.pdf (accessed March 5, 2025).
Albuquerque, D., J. Chan, D. Kanngiesser, D. Latto, S. Lloyd, S. Singh, and J. Žáček. 2025.
Decompositions, forecasts and scenarios from an estimated DSGE model for the UK
economy. Macro Technical Paper No. 1. Bank of England.
https://www.bankofengland.co.uk/macro-technical-paper/2025/decompositions-
forecasts-and-scenarios-from-an-estimated-dsge-model-for-the-uk-economy (accessed
July 17 2025)
Alvarez, R. M, J. Nagler, and J. R. Willette. 1999. Measuring the relative impact of issues and
the economy in democratic elections. Social Science Working Paper 1052. Pasadena,
California: California Institute of Technology.
Aning, J. 2024. Comelec exempts 48 projects from election ban. Inquirer.net.
https://www.inquirer.net/423236/comelec-exempts-48-projects-from-election-ban/
Azzimonti, M. (2024, June). Economic policy uncertainty in election years (Economic Brief
No. 24-20). Federal Reserve Bank of Richmond.
22

https://www.richmondfed.org/publications/research/economic_brief/2024/eb_24-20
(accessed March 5, 2025).
Bello, A. L. 2021. Economic voting in the Philippines. HOLISTICA – Journal of Business and
Public Administration 12(3): 1-12.
Blanchard, O. 2016. Do DSGE Models Have a Future? PIIE Policy Brief 16-11. Peterson
Institute for International Economics. https://www.piie.com/publications/policy-
briefs/do-dsge-models-have-future (accessed July 17 2025)
Boyles, M. (2022, July 19). Understanding how politics can affect your business. Harvard
Business School Online. https://online.hbs.edu/blog/post/politics-and-business (accessed
March 5, 2025).
Brender, A., & Drazen, A. (2005). Political budget cycles in new versus established
democracies. Journal of Monetary Economics, 52(7): 1271–1295.
Broni, M. Y., M. Hosen, H. N. Mohammed, and G. Tiamiyu. 2018. Should banks be averse to
elections? A GMM analysis of recent elections in Ghana. Journal of Economics, Finance
and Administrative Science 24(47): 47-65.
Calvo, G. A. 1983. Staggered prices in a utility-maximizing framework. Journal of Monetary
Economics 12 (3): 383-398.
Cigaral, I. N. P. 2024. Gov’t infrastructure spending surged ahead of election ban, says DBM.
Inquirer.net. https://business.inquirer.net/530194/govt-infrastructure-spending-surged-
ahead-of-election-ban
Cipullo, D. and A. Reslow. 2022. Electoral cycles in macroeconomic forecasts. Journal of
Economic Behavior & Organization 202: 307-340.
Commission on Elections (COMELEC). 2018. In the matter of the request for confirmation of
the Commission that the procurement of PPP projects are not covered by section 261(v)
and (w) of the Omnibus Election Code; and study of the Law Department thereon. Minute
Resolution No. 18-1127-3. https://ppp.gov.ph/wp-content/uploads/2018/12/Comelec-
Resolution-18-1127-3.pdf (accessed March 5, 2025).
Coulombe, R. G. 2021. The electoral origin of government spending shocks. Journal of
Economic Dynamics and Control 129(104167).
Congressional Policy and Budget Research Department (CPBRD). 2020. Second Quarter
2020 Philippine Economic Performance. FF2020-32. House of Representatives of the
Philippines. https://cpbrd.congress.gov.ph/ff2020-32-second-quarter-2020-philippine-
economic-performance/ (accessed October 4 2025).
Curtis, A. (2023, December 7). Do elections really matter for the economy? Capital
Economics. https://www.capitaleconomics.com/publications/global-economics-
focus/do-elections-really-matter-economy (accessed March 5, 2025).
Das, A., Rajan, B. R., Santosh Bandi, S. S., & Udandarao, V. (2025, February 28). From
polls to policies: The economic impact of elections (MPRA Paper No. 123801). Munich
Personal RePEc Archive. https://mpra.ub.uni-muenchen.de/123801/ (accessed March 5,
2025).
Debuque-Gonzales, M. & Corpus, J. P. P. (2023). Quantifying the Short-Run Macroeconomic
Impacts of the COVID-19 Pandemic: A Macroeconometric Approach (Discussion Paper
Series No. 2023-42). Philippine Institute for Development Studies.
https://doi.org/10.62986/dp2023.42
Debuque-Gonzales, M. & Corpus, J. P. P. (2024). Let’s Get Fiscal: Extending the Small
Macroeconometric Model of the Philippine Economy (Research Paper Series No. 2024-
05). Philippine Institute for Development Studies.
De Haan, J., Ohnsorge, F., & Yu, S. (2023, December 20). Election-induced fiscal policy
cycles in emerging market and developing economies (MPRA Paper No. 119551).
23

Munich Personal RePEc Archive. https://mpra.ub.uni-muenchen.de/119551/ (accessed
March 5, 2025).
Department of Health (DOH). 2021. Vaccines Administered in the Philippines as of June 21,
2021. https://caro.doh.gov.ph/vaccines-administered-in-the-philippines-as-of-june-21-
2021/ (accessed October 4 2025).
Drazen, A., & Eslava, M. (2010). Electoral manipulation via voter-friendly spending: Theory
and evidence. Journal of Development Economics, 92(1): 39–52.
Ducanes, G., Cagas, M. A., Qin, D., Quising, P., and Magtibay-Ramos, N. 2005. A small
macroeconometric model of the Philippine economy (ERD Working Paper Series No.
62). Asian Development Bank.
https://www.adb.org/sites/default/files/publication/28191/wp062.pdf (accessed March
5, 2025).
Evangelista, D. P., and P. A. Libre. 2008. Electoral cycles in Philippine fiscal and monetary
policy. The Philippine Review of Economics 45 (2): 119-159.
https://pre.econ.upd.edu.ph/index.php/pre/article/view/180/644
Fiorina, M. P. 1978. Economic retrospective voting in American national elections: A micro-
analysis. American Journal of Political Science 22(2): 426-443.
Frieden, J. (2020, June). The political economy of economic policy. Finance & Development
Magazine. International Monetary Fund.
https://www.imf.org/en/Publications/fandd/issues/2020/06/political-economy-of-
economic-policy-jeff-frieden (accessed March 5, 2025).
Gambetti, L. (2021, April 26). Shocks, information, and structural VARs. Oxford Research
Encyclopedia of Economics and Finance.
https://doi.org/10.1093/acrefore/9780190625979.013.621
Goodell, J. W., McGee, R. J., & McGroarty, F. (2020). Election uncertainty, economic policy
uncertainty and financial market uncertainty: A prediction market analysis. Journal of
Banking & Finance 110, 105684. https://doi.org/10.1016/j.jbankfin.2019.105684
Guerrieri, L. and M. Iacoviello. 2017. Collateral constraints and macroeconomic
asymmetries. Journal of Monetary Economics 90: 28-49.
https://www.matteoiacoviello.com/research_files/ASYMMETRIES_PAPER.pdf
(accessed July 17 2025)
Guntermann, E., G. S. Lenz, and J. R. Myers. 2021. The impact of the economy on presidential
elections throughout US history. Political Behavior 43: 837-857.
Gupta, S., Liu, E., & Mulas-Granados, C. (2015). Now or later? The political economy of
public investment in democracies (IMF Working Paper 175). International Monetary
Fund. https://www.imf.org/external/pubs/ft/wp/2015/wp15175.pdf (accessed March 5,
2025).
Habito, C. F. (2013). Elections and the economy. The Philippine Daily Inquirer.
https://opinion.inquirer.net/52565/elections-and-the-economy (accessed March 5,
2025).
Hendry, D. F. and J. N. J. Muellbauer. 2018. The future of macroeconomics: macro theory
and models at the Bank of England. Oxford Review of Economic Policy 34 (1-2): 287-
328. https://www.jstor.org/stable/48539417 (accessed July 17 2025)
Hendry, D. F. (2020). A short history of macro-econometric modelling. University of Oxford.
https://www.nuffield.ox.ac.uk/economics/Papers/2020/2020W01_MacroHist18.pdf
(accessed March 5, 2025).
Hicks, J. R. 1937. Mr. Keynes and the "Classics"; A Suggested Interpretation. Econometrica
5 (2): 147-159. https://www.jstor.org/stable/1907242 (accessed July 17 2025)
Hoke, S. H. (2019, December). Macroeconomic effects of political risk shocks (Staff
Working Paper No. 841). Bank of England. https://www.bankofengland.co.uk/-
24

/media/boe/files/working-paper/2019/macroeconomic-effects-of-political-risk-
shocks.pdf
Inosante, A. R. A. 2025. Election-tied spending may shield growth from tariffs. Business
World. https://www.bworldonline.com/top-stories/2025/05/19/673200/election-tied-
spending-may-shield-growth-from-tariffs/
Ivanovic, V., Lami, E., & Imami, D. (2023). Political budget cycles in early versus regular
elections: The case of Serbia. Comparative Economic Studies, 65: 551-581.
https://doi.org/10.1057/s41294-023-00210-0
Jahn, M., & Stricker, P. (2022). FDI, liquidity, and political uncertainty: A global analysis.
International Economics and Economic Policy, 19, 783-823.
https://doi.org/10.1007/s10368-022-00543-8
Jalles, J. T., Kiendrebeogo, Y., Lam, W. R., Piazza R. (2023). Revisiting the
countercyclicality of fiscal policy (IMF Working Paper Series 2023/089). International
Monetary Fund. https://doi.org/10.5089/9798400240683.001
Julio, B., & Yook, Y. (2012). Political uncertainty and corporate investment cycles. Journal of
Finance, 67(1): 45–83.
Kapas, J. (2020). Formal and informal institutions, and FDI flows: A review of the empirical
literature and propositions for further research. Economic and Business Review, 22(2):
161-189. https://doi.org/10.15458/ebr100.
Kaplan, G., B. Moll, and G. Violante. 2018. Monetary Policy According to HANK. American
Economic Review 18 (3): 697–743. https://benjaminmoll.com/wp-
content/uploads/2019/07/HANK.pdf (accessed July 17 2025)
Keynes, J. M. 1936. The General Theory of Employment, Interest and Money. Macmillan.
Kladakis, G., & Skouralis, A. (2024, October). Election cycles and systemic risk (Center for
Banking Research Working Paper Series 02/24). Bayes Business School.
https://www.bayes.citystgeorges.ac.uk/__data/assets/pdf_file/0011/835184/2024-
Kladakis-Skouralis-CBR-WP-0224.pdf (accessed March 5, 2025).
Kolios, B. 2019. Political business cycles in Australia elections and party ideology. Journal of
Time Series Econometrics 2019(20170012).
Kydland, F. E., and E. C. Prescott. 1982. Time to Build and Aggregate Fluctuations.
Econometrica, 50(6): 1345-1370. https://www.jstor.org/stable/1913386 (accessed July
17 2025)
Labonne, J. 2016. Local political business cycles: Evidence from Philippine municipalities.
Journal of Development Economics, 121: 56-62.
https://www.sciencedirect.com/science/article/pii/S0304387816300153
Landingin, R. (2010, August 26). Philippine growth spurt: it’s election spending, stupid.
Financial Times. https://www.ft.com/content/cc3b8b4a-1e8e-358c-a703-898fa874bf80
(accessed March 5, 2025).
Leigh, A. 2004. Does the world economy swing national elections? Centre for Economic Policy
Research Discussion Paper No. 485. The Australian National University.
Le, T., Onur, I., Sarwar, R., & Yalcin, E. (2024). Money in politics: How does It affect
election outcomes? Sage Open, 14(4). https://doi.org/10.1177/21582440241279659
Lokshin, M. M., A. Rodriguez-Ferrari, I. Torre. 2022. Electoral Cycles and Public Spending
during the Pandemic. Policy Research Working Paper Series No. 10214. Washington,
D.C.: World Bank Group.
http://documents.worldbank.org/curated/en/099536210202216248
Lucas, R. E. 1976. Econometric policy evaluation: A critique. Carnegie-Rochester
Conference Series on Public Policy: 19-46. (accessed July 17 2025)
Martinoli, M., Moneta, A., & Pallante, G. (2022). Calibration and validation of
macroeconomic simulation models: A general protocol by causal search (LEM
25

Working Paper Series No. 2022/33).
https://www.econstor.eu/bitstream/10419/273635/1/1822613671.pdf (accessed March
5, 2025).
Mertens, K., & Ravn, M. (2010). Empirical evidence on the aggregate effects of anticipated
and unanticipated U.S. tax policy shocks (NBER Working Paper 16289). National
Bureau of Economic Research.
https://www.nber.org/system/files/working_papers/w16289/w16289.pdf (accessed
March 5, 2025).
Nguyen, T. C. and T. L. Tran. 2023. The political budget cycles in emerging and developing
countries. Journal of Economics and Development 25(3): 205-225.
Ochave, R. M. D. (2015, January 21). Elections may help boost consumer goods firms’
bottom line. BusinessWorld. https://www.bworldonline.com/top-
stories/2025/01/21/647847/elections-may-help-boost-consumer-goods-firms-bottom-
line/ (accessed March 5, 2025).
Olano, C. A. V. (2019, May 14). How much economic boost does election spending deliver?
BusinessWorld. https://www.bworldonline.com/editors-picks/2019/05/14/230732/how-
much-economic-boost-does-election-spending-deliver/ (accessed March 5, 2025).
Pesaran, M. H., Shin, Y., & Smith, R. J. (2001). Bounds Testing Approaches to the Analysis
of Level Relationships. Journal of Applied Econometrics, 16(3): 289–326.
http://www.jstor.org/stable/2678547
Peters, A. C. 2010. Election induced fiscal and monetary cycles: Evidence from the Caribbean.
The Journal of Developing Areas 44(1): 287-302.
Philippine Statistics Authority (PSA). 2021. GDP posted a growth of 7.1 percent in the third
quarter of 2021. https://psa.gov.ph/statistics/national-accounts/node/165276 (accessed
October 4 2025).
Punongbayan, J. C. 2025. Politics in the Purse: Political Budget Cycles as Constraints to
Philippine Development. ISEAS Perspective 2025 No. 17. ISEAS-Yusof Ishak Institute.
https://www.iseas.edu.sg/articles-commentaries/iseas-perspective/2025-17-politics-in-
the-purse-political-budget-cycles-as-constraints-to-philippine-development-by-jc-
punongbayan/
Reyes, C., Bayudan-Dacuycuy, C., Abrigo, R., Quimba, F., Borromeo, N., Bautista, D.,
Ocampo, J., Baje, L., Calizo, S., Tam, Z., Hernandez, G. 2020. PIDS-BSP annual
macroeconometric model for the Philippines: preliminary estimates and ways forward.
PIDS Discussion Paper Series No. 2020-16. Quezon City: Philippine Institute for
Development Studies.
Reyes, C. and Yap, J. 1993. Re-estimation of the PIDS-NEDA annual macroeconometric
model. Unpublished manuscript.
Rodriguez, U. E., & Briones, R. M. (2002). The Ateneo macroeconomic and forecasting
model. The Philippine Review of Economics, 39(1), 142-178.
https://pre.econ.upd.edu.ph/index.php/pre/article/view/59 (accessed March 5, 2025).
Rogoff, K. and A. Sibert. 1988. Elections and macroeconomic policy cycles. Review of
Economic Studies 55(1):1-16.
Samuelson, P. A. 1948. Economics: An Introductory Analysis. McGraw-Hill.
Sargent, T. J., and N. Wallace. 1975. Rational" Expectations, the Optimal Monetary
Instrument, and the Optimal Money Supply Rule. Journal of Political Economy 83 (2):
241-254. https://www.jstor.org/stable/1830921 (accessed July 17 2025).
Schultz, K. A. (1995). The politics of the political business cycle. British Journal of Political
Science, 25(1), 79-99. https://www.jstor.org/stable/194177 (accessed March 5, 2025).
Shi, M., & Svensson, J. (2006). Political budget cycles: Do they differ across countries and
why? Journal of Public Economics, 90(8–9): 1367–1389.
26

Sibert, A. (1988). Elections and macroeconomic policy cycles. The Review of Economic
Studies, 55(1), 1-16. http://www.jstor.org/stable/2297526?origin=JSTOR-pdf (accessed
March 5, 2025).
Smets, F., and R. Wouters. 2007. Shocks and Frictions in US Business Cycles: A Bayesian
DSGE Approach. American Economic Review, 97(3): 586-606. (accessed July 17
2025)
Stanley, T. D. (2000). An empirical critique of the Lucas critique. The Journal of Socio-
Economics, 29(1), 91-107. https://doi.org/10.1016/S1053-5357(00)00055-X
Stiglitz, J. E. 2018. Where modern macroeconomics went wrong. Oxford Review of
Economic Policy 34 (1–2): 70–106 https://academic.oup.com/oxrep/article/34/1-
2/70/4781816 (accessed July 17 2025)
Tabash, M., M. Valappil, U. Iqbal, U. Farooq, and K. Y. Woo. 2024. Stock market reaction to
general election in Pakistan: An event study methodology. Advances in Decision
Sciences 27(4).
Tannous, K. (2024, November 12). Post-election jitters: Fiscal policy, GDP growth, and
rising yields. LinkedIn. https://www.linkedin.com/pulse/post-election-jitters-fiscal-
policy-gdp-growth-rising-tannous-qkpfc/ (accessed March 5, 2025).
Van Dalen, H. P., & Swank, O. H. (1996). Government Spending Cycles: Ideological or
Opportunistic? Public Choice, 89(1/2), 183-200. https://www.jstor.org/stable/30024155
(accessed March 5, 2025).
World Bank (WB) 2021. Philippines Economic Update December 2021 Edition: Regaining
Lost Ground, Revitalizing the Filipino Workforce.
https://thedocs.worldbank.org/en/doc/bca0601a640711811e2dea678fa08c32-
0070062021/original/World-Bank (accessed October 4 2025).
Yap, J. T. 2000. PIDS annual macroeconometric model 2000. PIDS Discussion Paper Series
No. 2000-13. Makati City: Philippine Institute for Development Studies.
27

7. Appendix

Appendix 1. Cumulative sum (CUSUM) and CUSUM of squares test on equations

1.  Consumption
|     | CUSUM  |     |     |     | CUSUM of squared  |     |     |
| --- | ------ | --- | --- | --- | ----------------- | --- | --- |
| 30  |        |     | 1.2 |     |                   |     |     |
| 20  |        |     | 1.0 |     |                   |     |     |
0.8
10
0.6
0
0.4
-10
0.2
| -20 |     |     | 0.0  |     |     |     |     |
| --- | --- | --- | ---- | --- | --- | --- | --- |
| -30 |     |     | -0.2 |     |     |     |     |
2008 2010 2012 2014 2016 2018 2020 2022 2008 2010 2012 2014 2016 2018 2020 2022
|     | CUSUM | 5% Significance |     |     | CUSUM of Squares | 5% Significance |     |
| --- | ----- | --------------- | --- | --- | ---------------- | --------------- | --- |
|     |       |                 |     |     |                  |                 |     |

2.  Investment
|     | CUSUM  |     |     |     | CUSUM of squared  |     |     |
| --- | ------ | --- | --- | --- | ----------------- | --- | --- |
| 30  |        |     | 1.2 |     |                   |     |     |
| 20  |        |     | 1.0 |     |                   |     |     |
0.8
10
0.6
0
0.4
-10
0.2
| -20   |          |                 | 0.0   |          |                                  |          |     |
| ----- | -------- | --------------- | ----- | -------- | -------------------------------- | -------- | --- |
| -30   |          |                 | -0.2  |          |                                  |          |     |
| 04 06 | 08 10 12 | 14 16 18        | 20 22 | 04 06 08 | 10 12 14                         | 16 18 20 | 22  |
|       | CUSUM    | 5% Significance |       |          | CUSUM of Squares 5% Significance |          |     |
|       |          |                 |       |          |                                  |          |     |

3.  Government consumption
|     | CUSUM  |     |     |     | CUSUM of squared  |     |     |
| --- | ------ | --- | --- | --- | ----------------- | --- | --- |
| 30  |        |     | 1.2 |     |                   |     |     |
1.0
20
0.8
10
0.6
0
0.4
-10
0.2
-20
0.0
-0.2
-30
| 04 06 | 08 10 12 | 14 16 18        | 20 22 | 04 06 08 | 10 12 14                         | 16 18 20 | 22  |
| ----- | -------- | --------------- | ----- | -------- | -------------------------------- | -------- | --- |
|       | CUSUM    | 5% Significance |       |          | CUSUM of Squares 5% Significance |          |     |
|       |          |                 |       |          |                                  |          |     |

28

4.  Imports
|     | CUSUM  |     |     | CUSUM of squared  |     |     |     |
| --- | ------ | --- | --- | ----------------- | --- | --- | --- |
| 30  |        |     | 1.2 |                   |     |     |     |
1.0
20
0.8
10
0.6
0
0.4
-10
0.2
-20
0.0
| -30 |     |     | -0.2 |     |     |     |     |
| --- | --- | --- | ---- | --- | --- | --- | --- |
2006 2008 2010 2012 2014 2016 2018 2020 2022 2006 2008 2010 2012 2014 2016 2018 2020 2022
|     | CUSUM | 5% Significance |     | CUSUM of Squares | 5% Significance |     |     |
| --- | ----- | --------------- | --- | ---------------- | --------------- | --- | --- |
|     |       |                 |     |                  |                 |     |     |

5.  Exports
|     | CUSUM  |     |     | CUSUM of squared  |     |     |     |
| --- | ------ | --- | --- | ----------------- | --- | --- | --- |
| 30  |        |     | 1.2 |                   |     |     |     |
1.0
20
0.8
10
0.6
0
0.4
-10
0.2
-20
0.0
| -30 |     |     | -0.2 |     |     |     |     |
| --- | --- | --- | ---- | --- | --- | --- | --- |
2006 2008 2010 2012 2014 2016 2018 2020 2022 2006 2008 2010 2012 2014 2016 2018 2020 2022
|     | CUSUM | 5% Significance |     | CUSUM of Squares | 5% Significance |     |     |
| --- | ----- | --------------- | --- | ---------------- | --------------- | --- | --- |
|     |       |                 |     |                  |                 |     |     |

6.  Employment rate
|     | CUSUM  |     |     | CUSUM of squared  |     |     |     |
| --- | ------ | --- | --- | ----------------- | --- | --- | --- |
| 30  |        |     | 1.2 |                   |     |     |     |
1.0
20
0.8
10
0.6
0
0.4
-10
0.2
| -20 |     |     | 0.0  |     |     |     |     |
| --- | --- | --- | ---- | --- | --- | --- | --- |
| -30 |     |     | -0.2 |     |     |     |     |
2008 2010 2012 2014 2016 2018 2020 2022 2008 2010 2012 2014 2016 2018 2020 2022
|     | CUSUM | 5% Significance |     | CUSUM of Squares | 5% Significance |     |     |
| --- | ----- | --------------- | --- | ---------------- | --------------- | --- | --- |
|     |       |                 |     |                  |                 |     |     |
7.  Internal tax revenues
|     | CUSUM  |     |     | CUSUM of squared  |     |     |     |
| --- | ------ | --- | --- | ----------------- | --- | --- | --- |
| 30  |        |     | 1.2 |                   |     |     |     |
| 20  |        |     | 1.0 |                   |     |     |     |
| 10  |        |     | 0.8 |                   |     |     |     |
0.6
0
0.4
-10
0.2
| -20   |          |                 | 0.0   |                  |                 |          |     |
| ----- | -------- | --------------- | ----- | ---------------- | --------------- | -------- | --- |
| -30   |          |                 | -0.2  |                  |                 |          |     |
| 04 06 | 08 10 12 | 14 16 18        | 20 22 | 04 06 08         | 10 12 14        | 16 18 20 | 22  |
|       |          |                 |       | CUSUM of Squares | 5% Significance |          |     |
|       | CUSUM    | 5% Significance |       |                  |                 |          |     |
|       |          |                 |       |                  |                 |          |     |

29

8.  Customs revenues
|     | CUSUM  |     |     |     |     | CUSUM of squared  |     |     |     |
| --- | ------ | --- | --- | --- | --- | ----------------- | --- | --- | --- |
| 12  |        |     |     | 1.6 |     |                   |     |     |     |
| 8   |        |     |     | 1.2 |     |                   |     |     |     |
4
0.8
0
0.4
-4
| -8  |     |     |     | 0.0  |     |     |     |     |     |
| --- | --- | --- | --- | ---- | --- | --- | --- | --- | --- |
| -12 |     |     |     | -0.4 |     |     |     |     |     |
III IV I II III IV I II III IV I II III IV III IV I II III IV I II III IV I II III IV
| 2020 | 2021  | 2022            | 2023 |     | 2020 | 2021             | 2022            | 2023 |     |
| ---- | ----- | --------------- | ---- | --- | ---- | ---------------- | --------------- | ---- | --- |
|      | CUSUM | 5% Significance |      |     |      | CUSUM of Squares | 5% Significance |      |     |
|      |       |                 |      |     |      |                  |                 |      |     |
9.  Non-tax revenues
|       | CUSUM    |                 |       |     |       | CUSUM of squared  |                 |          |     |
| ----- | -------- | --------------- | ----- | --- | ----- | ----------------- | --------------- | -------- | --- |
| 30    |          |                 |       | 30  |       |                   |                 |          |     |
| 20    |          |                 |       | 20  |       |                   |                 |          |     |
| 10    |          |                 |       | 10  |       |                   |                 |          |     |
| 0     |          |                 |       | 0   |       |                   |                 |          |     |
| -10   |          |                 |       | -10 |       |                   |                 |          |     |
| -20   |          |                 |       | -20 |       |                   |                 |          |     |
| -30   |          |                 |       | -30 |       |                   |                 |          |     |
| 04 06 | 08 10 12 | 14 16           | 18 20 | 22  | 04 06 | 08 10 12          | 14              | 16 18 20 | 22  |
|       | CUSUM    | 5% Significance |       |     |       | CUSUM             | 5% Significance |          |     |
|       |          |                 |       |     |       |                   |                 |          |     |
|       |          |                 |       |     |       |                   |                 |          |     |
10. Primary expenditure
|     | CUSUM  |     |     |     |     | CUSUM of squared  |     |     |     |
| --- | ------ | --- | --- | --- | --- | ----------------- | --- | --- | --- |
| 30  |        |     |     | 1.2 |     |                   |     |     |     |
1.0
20
0.8
10
0.6
0
0.4
-10
0.2
| -20   |          |                 |     | 0.0  |       |                  |                 |          |     |
| ----- | -------- | --------------- | --- | ---- | ----- | ---------------- | --------------- | -------- | --- |
| -30   |          |                 |     | -0.2 |       |                  |                 |          |     |
| 04 06 | 08 10 12 | 14 16 18        | 20  | 22   | 04 06 | 08 10 12         | 14              | 16 18 20 | 22  |
|       | CUSUM    | 5% Significance |     |      |       | CUSUM of Squares | 5% Significance |          |     |
|       |          |                 |     |      |       |                  |                 |          |     |
11. Effective interest rate on domestic debt
|     | CUSUM  |     |     |     |     | CUSUM of squared  |     |     |     |
| --- | ------ | --- | --- | --- | --- | ----------------- | --- | --- | --- |
| 30  |        |     |     | 1.2 |     |                   |     |     |     |
1.0
20
0.8
10
0.6
0
0.4
-10
0.2
-20
0.0
-0.2
-30
| 04 06 | 08 10 12 | 14 16 18        | 20  | 22  | 04 06 | 08 10 12         | 14              | 16 18 20 | 22  |
| ----- | -------- | --------------- | --- | --- | ----- | ---------------- | --------------- | -------- | --- |
|       | CUSUM    | 5% Significance |     |     |       | CUSUM of Squares | 5% Significance |          |     |
|       |          |                 |     |     |       |                  |                 |          |     |

30

12. Effective interest rate on foreign debt
|       | CUSUM    |                 |       | CUSUM of squared  |                                  |          |     |
| ----- | -------- | --------------- | ----- | ----------------- | -------------------------------- | -------- | --- |
| 30    |          |                 | 1.2   |                   |                                  |          |     |
| 20    |          |                 | 1.0   |                   |                                  |          |     |
| 10    |          |                 | 0.8   |                   |                                  |          |     |
| 0     |          |                 | 0.6   |                   |                                  |          |     |
| -10   |          |                 | 0.4   |                   |                                  |          |     |
| -20   |          |                 | 0.2   |                   |                                  |          |     |
| -30   |          |                 | 0.0   |                   |                                  |          |     |
| -40   |          |                 | -0.2  |                   |                                  |          |     |
| 04 06 | 08 10 12 | 14 16 18        | 20 22 | 04 06 08          | 10 12 14                         | 16 18 20 | 22  |
|       | CUSUM    | 5% Significance |       |                   | CUSUM of Squares 5% Significance |          |     |
|       |          |                 |       |                   |                                  |          |     |

13. Central bank policy rate
|     | CUSUM  |     |     |     | CUSUM of squared  |     |     |
| --- | ------ | --- | --- | --- | ----------------- | --- | --- |
| 30  |        |     | 1.4 |     |                   |     |     |
1.2
20
1.0
10
0.8
| 0   |     |     | 0.6 |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- |
0.4
-10
0.2
-20
0.0
| -30 |     |     | -0.2 |     |     |     |     |
| --- | --- | --- | ---- | --- | --- | --- | --- |
08 09 10 11 12 13 14 15 16 17 18 19 20 21 22 23 08 09 10 11 12 13 14 15 16 17 18 19 20 21 22 23
|     |       |                 |     |     | CUSUM of Squares 5% Significance |     |     |
| --- | ----- | --------------- | --- | --- | -------------------------------- | --- | --- |
|     | CUSUM | 5% Significance |     |     |                                  |     |     |

14. 91-day Treasury bill rate
|       | CUSUM    |                 |       |          | CUSUM of squared                 |          |     |
| ----- | -------- | --------------- | ----- | -------- | -------------------------------- | -------- | --- |
| 30    |          |                 | 1.2   |          |                                  |          |     |
| 20    |          |                 | 1.0   |          |                                  |          |     |
| 10    |          |                 | 0.8   |          |                                  |          |     |
| 0     |          |                 | 0.6   |          |                                  |          |     |
| -10   |          |                 | 0.4   |          |                                  |          |     |
| -20   |          |                 | 0.2   |          |                                  |          |     |
| -30   |          |                 | 0.0   |          |                                  |          |     |
| -40   |          |                 | -0.2  |          |                                  |          |     |
| 04 06 | 08 10 12 | 14 16 18        | 20 22 | 04 06 08 | 10 12 14                         | 16 18 20 | 22  |
|       | CUSUM    | 5% Significance |       |          | CUSUM of Squares 5% Significance |          |     |
|       |          |                 |       |          |                                  |          |     |

15. 10-year Treasury bond rate
|     | CUSUM  |     |     |     | CUSUM of squared  |     |     |
| --- | ------ | --- | --- | --- | ----------------- | --- | --- |
| 30  |        |     | 1.2 |     |                   |     |     |
| 20  |        |     | 1.0 |     |                   |     |     |
0.8
10
0.6
0
0.4
-10
0.2
| -20   |          |                 | 0.0   |          |                                  |          |     |
| ----- | -------- | --------------- | ----- | -------- | -------------------------------- | -------- | --- |
| -30   |          |                 | -0.2  |          |                                  |          |     |
| 04 06 | 08 10 12 | 14 16 18        | 20 22 | 04 06 08 | 10 12 14                         | 16 18 20 | 22  |
|       | CUSUM    | 5% Significance |       |          | CUSUM of Squares 5% Significance |          |     |
|       |          |                 |       |          |                                  |          |     |

31

16. Bank lending rate
|       | CUSUM    |                 |       |       | CUSUM of squared  |                 |       |
| ----- | -------- | --------------- | ----- | ----- | ----------------- | --------------- | ----- |
| 30    |          |                 | 1.2   |       |                   |                 |       |
| 20    |          |                 | 1.0   |       |                   |                 |       |
| 10    |          |                 | 0.8   |       |                   |                 |       |
| 0     |          |                 | 0.6   |       |                   |                 |       |
| -10   |          |                 | 0.4   |       |                   |                 |       |
| -20   |          |                 | 0.2   |       |                   |                 |       |
| -30   |          |                 | 0.0   |       |                   |                 |       |
| -40   |          |                 | -0.2  |       |                   |                 |       |
| 04 06 | 08 10 12 | 14 16 18        | 20 22 | 04 06 | 08 10 12          | 14 16 18        | 20 22 |
|       | CUSUM    | 5% Significance |       |       | CUSUM of Squares  | 5% Significance |       |
|       |          |                 |       |       |                   |                 |       |

17. Consumer price index
|     | CUSUM  |     |     |     | CUSUM of squared  |     |     |
| --- | ------ | --- | --- | --- | ----------------- | --- | --- |
| 30  |        |     | 1.2 |     |                   |     |     |
1.0
20
0.8
10
0.6
0
0.4
-10
0.2
| -20 |     |     | 0.0  |     |     |     |     |
| --- | --- | --- | ---- | --- | --- | --- | --- |
| -30 |     |     | -0.2 |     |     |     |     |
2006 2008 2010 2012 2014 2016 2018 2020 2022 2006 2008 2010 2012 2014 2016 2018 2020 2022
|     | CUSUM | 5% Significance |     |     | CUSUM of Squares | 5% Significance |     |
| --- | ----- | --------------- | --- | --- | ---------------- | --------------- | --- |
|     |       |                 |     |     |                  |                 |     |

18. GDP deflator
|     | CUSUM  |     |     |     | CUSUM of squared  |     |     |
| --- | ------ | --- | --- | --- | ----------------- | --- | --- |
| 30  |        |     | 1.2 |     |                   |     |     |
| 20  |        |     | 1.0 |     |                   |     |     |
0.8
10
0.6
0
0.4
-10
0.2
| -20   |          |                 | 0.0   |       |                  |                 |       |
| ----- | -------- | --------------- | ----- | ----- | ---------------- | --------------- | ----- |
| -30   |          |                 | -0.2  |       |                  |                 |       |
| 04 06 | 08 10 12 | 14 16 18        | 20 22 | 04 06 | 08 10 12         | 14 16 18        | 20 22 |
|       | CUSUM    | 5% Significance |       |       | CUSUM of Squares | 5% Significance |       |
|       |          |                 |       |       |                  |                 |       |

19. Inflation expectations
|     | CUSUM  |     |     |     | CUSUM of squared  |     |     |
| --- | ------ | --- | --- | --- | ----------------- | --- | --- |
| 30  |        |     | 1.2 |     |                   |     |     |
1.0
20
0.8
10
0.6
0
0.4
-10
0.2
-20
0.0
-0.2
| -30   |          |                 |       | 04 06 | 08 10 12         | 14 16 18        | 20 22 |
| ----- | -------- | --------------- | ----- | ----- | ---------------- | --------------- | ----- |
| 04 06 | 08 10 12 | 14 16 18        | 20 22 |       |                  |                 |       |
|       | CUSUM    | 5% Significance |       |       | CUSUM of Squares | 5% Significance |       |

32

Appendix 2. Summary statistics
Variable Obs Mean Std. dev. Min Max
GDP 92.00000 15.00616 0.337554 14.41938 15.54991
GDP growth 92.00000 5.100274 3.919953 -15.73532 12.28460
Household consumption 92.00000 14.71327 0.312916 14.16219 15.22696
Investment 92.00000 13.40527 0.493765 12.60449 14.12053
Government consumption 92.00000 12.85640 0.458427 12.17256 13.62048
Imports 92.00000 13.90079 0.442758 13.28778 14.56990
Exports 92.00000 13.67446 0.377367 12.99249 14.22927
Disposable income 92.00000 14.90120 0.330769 14.31227 15.43205
Domestic demand 92.00000 15.07274 0.360153 14.50052 15.64909
Employment rate 79.00000 93.32286 1.762076 82.68118 96.13102
Consumer price index 92.00000 4.434372 0.244569 3.988600 4.844825
GDP deflator 92.00000 4.462031 0.201113 4.048779 4.782431
US consumer price index 92.00000 4.584116 0.150793 4.320689 4.895367
CPI inflation 92.00000 3.863665 1.978919 -0.039411 10.31928
Deviation from inflation target 92.00000 0.081057 1.987872 -3.039411 6.319283
Expected inflation 90.00000 3.880644 1.826359 0.176666 10.17660
Deviation from inflation target 90.00000 0.102866 1.858691 -2.823334 6.176596
World oil price (USD per barrel) 92.00000 4.130562 0.440772 3.024053 4.767946
Retail price of ordinary rice (USD/ton) 81.00000 6.528090 0.233192 5.879447 6.814592
PHP/USD exchange rate 92.00000 3.896962 0.097006 3.706344 4.064011
Real PHP/USD exchange rate 92.00000 4.046706 0.146097 3.830282 4.358443
BSP policy rate 92.00000 4.785326 1.691357 2.000000 7.500000
91-day Treasury rate 92.00000 3.834284 2.138260 0.399254 8.133365
10-year Treasury rate 92.00000 7.014418 2.983422 2.933949 14.30097
Bank lending rate 91.00000 7.413242 1.642790 5.404006 10.85725
Real 91-day Treasury rate 92.00000 -0.029381 2.237194 -4.365562 5.032397
Real 10-year Treasury rate 92.00000 3.150752 2.947634 -1.868480 11.17548
Real bank lending rate 91.00000 3.535160 2.032507 -1.492220 7.816798
10-year Treasury rate US 92.00000 3.079301 1.144704 0.662028 5.069424
Nominal revenues 92.00000 12.94328 0.593574 11.81075 13.95539
Nominal tax revenues 92.00000 12.81778 0.605913 11.68525 13.80315
Nominal internal tax revenues 92.00000 12.55341 0.597581 11.42865 13.53053
Nominal customs revenues 92.00000 11.31126 0.647554 10.00319 12.37857
Nominal non-tax revenues 92.00000 10.76776 0.548466 9.662538 12.10431
Nominal NG expenditure 92.00000 13.13778 0.637177 12.16042 14.23665
Nominal primary expenditure 92.00000 12.94093 0.717014 11.84193 14.08569
Nominal interest payments 92.00000 11.31601 0.313734 10.58728 12.27139
Nominal domestic interest payments 92.00000 10.90898 0.362481 10.21010 11.83774
Nominal foreign interest payments 92.00000 10.19951 0.266079 9.429575 11.26906
Effective domestic interest rate 92.00000 1.635488 0.445163 0.931173 2.667550
Effective foreign interest rate 92.00000 1.267831 0.268807 0.636514 1.768446
Primary balance/GDP 92.00000 -0.282698 2.962809 -10.71427 4.635260
NG debt 92.00000 15.57367 0.481192 14.71613 16.59206
Domestic NG debt 92.00000 15.08119 0.575729 14.06369 16.20897
Foreign NG debt 92.00000 14.60770 0.339936 13.97840 15.45108
Debt/GDP 92.00000 53.31662 9.753641 39.46933 71.06895
Domestic debt/GDP 92.00000 32.47692 5.482577 25.62184 43.41447
Foreign debt/GDP 92.00000 20.83998 6.393255 13.38040 34.67981
Source: Authors’ calculation
33

Appendix 3. Results of the ADF test
| Variables  | diff=0  | diff=1  | diff=2  |
| ---------- | ------- | ------- | ------- |
GDP
|                         |  0.848505  |  1.80E-08  |  2.79E-08  |
| ----------------------- | ---------- | ---------- | ---------- |
| GDP growth              |  0.018645  |  2.22E-08  |  3.72E-08  |
| Household consumption   |  0.850132  |  6.62E-08  |  0.000100  |
| Investment              |  0.787998  |  0.000100  |  1.23E-07  |
| Government consumption  |  0.973755  |  0.000100  |  0.000100  |
| Imports                 |  0.868088  |  0.000100  |  3.14E-08  |
| Exports                 |  0.719263  |  0.000100  |  0.000100  |
Disposable income
|                  |  0.812715  |  8.59E-08  |  2.92E-08  |
| ---------------- | ---------- | ---------- | ---------- |
| Domestic demand  |  0.917530  |  4.13E-08  |  0.000100  |
Employment rate
|                          |  0.000100  |  0.000100  |  0.000100  |
| ------------------------ | ---------- | ---------- | ---------- |
| Consumer price index     |  0.733661  |  5.62E-05  |  2.38E-08  |
| GDP deflator             |  0.364247  |  3.00E-07  |  3.50E-08  |
| US consumer price index  |  0.991907  |  1.13E-06  |  2.53E-08  |
| CPI inflation            |  0.007652  |  2.35E-05  |  2.13E-05  |
Deviation from inflation target   0.004059   0.001588   7.13E-08
| Expected inflation  |  0.184991  |  3.38E-05  |  1.19E-07  |
| ------------------- | ---------- | ---------- | ---------- |
Deviation from inflation target
|     |  0.004307  |  1.07E-06  |  1.40E-07  |
| --- | ---------- | ---------- | ---------- |
World oil price (USD per barrel)   0.071016   2.01E-08   2.35E-08
Retail price of ordinary rice (USD/ton)
|                             |  0.059567  |  1.43E-07  |  0.000100  |
| --------------------------- | ---------- | ---------- | ---------- |
| PHP/USD exchange rate       |  0.668310  |  4.04E-07  |  0.000100  |
| Real PHP/USD exchange rate  |  0.510377  |  2.95E-07  |  5.39E-06  |
| BSP policy rate             |  0.163745  |  2.44E-05  |  2.37E-08  |
| 91-day Treasury rate        |  0.031014  |  2.12E-06  |  0.000100  |
10-year Treasury rate
|                    |  0.017979  |  1.10E-08  |  1.42E-05  |
| ------------------ | ---------- | ---------- | ---------- |
| Bank lending rate  |  0.014352  |  5.99E-08  |  1.22E-06  |
Real 91-day Treasury rate
|                             |  0.015754  |  0.001393  |  3.10E-08  |
| --------------------------- | ---------- | ---------- | ---------- |
| Real 10-year Treasury rate  |  0.008301  |  4.83E-08  |  5.39E-08  |
Real bank lending rate
|                           |  0.001256  |  0.000383  |  6.18E-07  |
| ------------------------- | ---------- | ---------- | ---------- |
| 10-year Treasury rate US  |  0.278236  |  2.41E-08  |  1.56E-08  |
| Nominal revenues          |  0.827929  |  2.09E-07  |  0.000100  |
| Nominal tax revenues      |  0.839660  |  0.000100  |  3.34E-06  |
Nominal internal tax revenues   0.748273   0.000100   5.02E-08
Nominal customs revenues
|                           |  0.683355  |  0.000100  |  0.000100  |
| ------------------------- | ---------- | ---------- | ---------- |
| Nominal non-tax revenues  |  0.880388  |  0.000100  |  3.07E-08  |
Nominal NG expenditure
|     |  0.984335  |  0.000100  |  4.79E-07  |
| --- | ---------- | ---------- | ---------- |
Nominal primary expenditure   0.968874   0.000100   1.52E-06
Nominal interest payments
|     |  0.988705  |  0.000100  |  4.16E-08  |
| --- | ---------- | ---------- | ---------- |
Nominal domestic interest payments   0.969265   0.000100   4.36E-08
Nominal foreign interest payments   0.873016   0.000100   3.33E-05
Effective domestic interest rate   0.470250   0.000100   3.45E-06
Effective foreign interest rate   0.401333   2.35E-08   0.000100
Primary balance/GDP
|          |  0.358776  |  1.08E-05  |  1.52E-06  |
| -------- | ---------- | ---------- | ---------- |
| NG debt  |  0.996948  |  6.83E-05  |  8.54E-07  |
Domestic NG debt
|                    |  0.989639  |  8.17E-06  |  0.000100  |
| ------------------ | ---------- | ---------- | ---------- |
| Foreign NG debt    |  0.998088  |  1.00E-06  |  7.32E-05  |
| Debt/GDP           |  0.481812  |  0.002019  |  0.000100  |
| Domestic debt/GDP  |  0.548330  |  0.000683  |  0.000100  |
| Foreign debt/GDP   |  0.601342  |  0.047112  |  0.000100  |
Source: Authors’ calculation

34