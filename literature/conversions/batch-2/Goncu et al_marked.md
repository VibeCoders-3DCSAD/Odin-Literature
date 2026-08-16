---
conversion_metadata:
  converted_at: "2026-07-22T13:26:30Z"
  converter_tool: "markitdown"
  converter_version: "0.1.6"
  source_pdf: "Goncu et al.pdf"
  source_pdf_sha256: "3707d039e2fecafed02bed9f3779773c9b0c2cbd8e8834d8fe99f4dde8870b99"
  page_count: 8
  markdown_char_count: 107826
---

<!-- PAGE-AWARE EXTRACTION (via pdfminer.six) -->

<!-- PAGE 1 -->

Borsa Istanbul Review 26 (2026) 100800

Contents lists available at ScienceDirect

Borsa Istanbul Review

journal homepage: www.elsevier.com/journals/borsa-istanbul-review

Machine learning for risk profiling: An analysis of pension fund participants
,∗, Burak Saltoğlu b

Ahmet Göncü a, Tolga U. Kuzubaş b
a Istanbul Technical University, Department of Engineering Management, Türkiye
b Department of Economics, Boğaziçi University, Türkiye

A R T I C L E   I N F O

A B S T R A C T

JEL classification:
G11
G40

Keywords:
Feature selection
Machine learning
Pension fund
Risk profiling

1. Introduction

This study examines the use of machine learning (ML) techniques for profiling the risk of pension fund 
participants. We analyze a dataset of 81,563 individual investors in a major Turkish pension fund company 
(2018–2022), comparing various ML models to the regulatory benchmark. Using recursive feature elimination, 
we identify self-reported risk attitudes and age – with a nonlinear relationship – as the most important 
predictors of actual portfolio risk. Our cross-validation results indicate that boosting methods yield modest 
improvements in predictive accuracy relative to the regulatory risk score. Notably, the performance from using 
just four variables is comparable to that from using the full questionnaire. Although the overall explanatory 
power remains modest across all models (𝑅2 of 0.13–0.17), the findings suggest that ML can enhance risk 
profiling by identifying informative variables and capturing nonlinear relationships. These results have practical 
implications for designing more efficient risk assessment tools in pension fund settings, potentially simplifying 
questionnaires without sacrificing predictive accuracy.

The alignment between investors’ risk preferences and their port-
folio choices represents a fundamental challenge in financial markets. 
Mismatches between stated preferences and actual investment behav-
ior can lead to suboptimal outcomes, including premature liquidation 
during market downturns, inadequate retirement savings, and reduced 
long-term  wealth  accumulation  (Brayman  et  al.,  2015).  This  chal-
lenge has become increasingly critical as pension systems worldwide 
shift toward defined contribution plans, placing greater responsibility 
on individual participants to make appropriate investment decisions. 
In Türkiye, over 9 million participants managed approximately USD 
55–60 billion in pension assets as of 2024, making accurate risk as-
sessment  essential  for  both  individual  welfare  and  financial  system 
stability (Pension Monitoring Center of Türkiye (EGM), 2025).

This regulatory requirement, however, is coupled with a signifi-
cant operational challenge. Pension funds and financial institutions, 
often  interacting  with  clients  via  high-friction  channels  like  phone 
or digital apps, face major hurdles with long, complex surveys. This 
‘‘participant friction’’ can lead to low completion rates and incomplete 
data (Brayman et al., 2015), creating a critical tension between reg-
ulatory  compliance  and  operational  efficiency.  Furthermore,  studies 
examining global risk assessment practices have identified important 
limitations in many existing questionnaires. Roszkowski and Grable

∗ Corresponding author.

E-mail address:  umut.kuzubas@bogazici.edu.tr (T.U. Kuzubaş).
Peer review under responsibility of Borsa İstanbul Anonim Şirketi.

(2005) and Bouchey (2004) note that many questionnaires fail to meet 
established psychometric standards and often show limited ability to 
predict actual investment behavior.

Risk preferences are commonly assessed through either incentivized 
experimental  methods  that  reveal  preferences  through  observable
choices, or self-report measures that elicit stated preferences directly. 
The literature presents an ongoing debate regarding which approach 
better captures true risk preferences (Friedman et al., 2014; Beshears 
et al., 2008; Pedroni et al., 2017; Mata et al., 2018). Some studies 
suggest that revealed and stated preferences show limited consistency 
across methods (Pedroni et al., 2017). However, Mata et al. (2018) 
note that revealed preference measures do not necessarily demonstrate 
superior predictive validity compared to stated preference measures. 
Nevertheless, both types of risk assessment approaches typically exhibit 
modest  predictive  power  for  actual  financial  risk-taking  behavior, 
with  generally  low  𝑅2  values  (Barsky  et  al.,  1997;  Dohmen  et  al., 
2011; Beauchamp et al., 2017; Gürdal et al., 2017; Kapteyn & Teppa, 
2011).

Despite growing recognition of these limitations, three critical re-
search gaps remain. First, while studies have documented the mod-
est predictive power of risk questionnaires (Beauchamp et al., 2017; 
Dohmen et al., 2011), limited research has systematically compared 
machine learning (ML) approaches against regulatory benchmarks us-
ing  actual  portfolio  data  in  emerging  market  contexts.  Second,  the

https://doi.org/10.1016/j.bir.2026.100800
Received 23 July 2025; Received in revised form 19 January 2026; Accepted 19 January 2026
Available online 27 January 2026 
2214-8450/Copyright © 2026 Borsa İstanbul Anonim Şirketi. Published by Elsevier B.V. This is an open access article under the CC BY-NC-ND license ( http://creativecommons.org/licenses/by-nc-nd/4.0/ ).

---

<!-- PAGE 2 -->

A. Göncü et al.

relative importance of different questionnaire items for predictive ac-
curacy remains unclear, with no consensus on whether comprehensive 
assessments are necessary or if simplified tools could achieve com-
parable results—a question with significant practical implications for 
the  industry’s  participant  friction  problem.  Third,  the  potential  for 
non-linear relationships between demographic factors and risk-taking 
behavior has received insufficient attention, particularly in emerging 
markets where lifecycle patterns may differ.

This study contributes to this line of research by addressing these 
three gaps directly. First, we systematically compare a suite of ML mod-
els against the regulatory benchmark, using a large, real-world dataset 
of 81,563 investors’ actual portfolio risk from an emerging market. 
Second, we apply feature selection methods to identify a concise, 4-
variable set of predictors, directly addressing the trade-off between 
accuracy and the industry’s need to reduce operational friction. This 
shorter set of inputs offers a practical advantage for large-scale im-
plementation, especially in phone-based or digital enrollment channels 
where lengthy questionnaires create participation barriers. Third, we 
explicitly model and confirm a non-linear relationship between age and 
risk-taking. Our work moves beyond the Adekunle et al. (2023) study 
(which predicts survey-based risk) and the Kuzubaş and Saltoğlu (2024) 
factor analysis by providing a practical, data-driven path toward a more 
efficient and operationally viable assessment tool.

Our work is situated within a rapidly evolving literature on ML in 
finance. While foundational work focused on credit risk, bankruptcy 
prediction, and fraud detection (e.g., Khandani et al., 2010; Barboza 
et al., 2017; Shi et al., 2022), recent research has expanded into three 
distinct areas highly relevant to our study.

The first area is the application of ML to personalization in wealth 
management, particularly in the high-growth field of robo-advising. 
This  research  directly  intersects  with  behavioral  finance,  as  studies 
now evaluate how these technologies address (or fail to address) in-
vestor rationality, risk tolerance, and expectations (Eichler & Schwab, 
2024). Concurrently, researchers are developing complex deep learning 
frameworks  for  risk-aligned  portfolio  optimization  (Nguyen,  2025). 
This trend is particularly relevant for our work, as industry analysis 
now highlights the central role of AI in transforming pension systems 
and governance (Hayman & Genevieve, 2024), though significant con-
cerns remain about model-fit and the risks of using historical data for 
long-term predictions (Benefits Canada, 2025).

The second stream of research is exploring alternative data, with 
a  strong  focus  on  using  Natural  Language  Processing  (NLP)  to  ex-
tract investor sentiment from unstructured text. This field has matured 
rapidly, with recent systematic reviews mapping its evolution (Huynh 
et al., 2025). Current applications range from general sentiment anal-
ysis  (Hansen  &  Borch,  2022)  to  specific  tasks  like  real-time,  high-
frequency stock return prediction (Cai et al., 2024) and even using 
the text from lottery-choice scenarios to risk-profile investors (Thomas 
et al., 2023). This research path, focused on mining new data sources, 
contrasts with our study’s focus on making existing, mandatory survey 
data smarter and more efficient.

Finally,  the  adoption  of  these  increasingly  complex  models  has 
created a significant regulatory and practical challenge: the black box’’ 
problem.  This  is  no  longer  a  niche  concern;  a  wave  of  recent  sys-
tematic reviews has highlighted the black box’’ as a central academic 
and industry-wide challenge (e.g., Khan et al., 2025; Černevičieṅ e 
& Kabašinskas, 2024). This concern is mirrored by stakeholders and 
regulators, with major bodies like the CFA Institute (Wilson, 2025) and 
the Bank of England Gharbawi et al. (2024) now issuing guidance on AI 
transparency. This has spurred a critical field of Explainable AI (XAI) 
focused on building transparent models for parallel applications. This 
includes developing interpretable models for systemic risk (Tang et al., 
2024),  creating  frameworks  to  balance  the  accuracy-interpretability 
trade-off  (Hamerle  et  al.,  2024;  Mena  et  al.,  2024),  and  applying 
XAI techniques to fraud detection (Yaseen & Al-Amarneh, 2025) and 
credit  risk  (Nallakaruppan  et  al.,  2024).  Recent  systematic  reviews

Borsa Istanbul Review 26 (2026) 100800

on  default  prediction  further  confirm  the  move  toward  hybrid  and 
explainable models for regulatory acceptance (Reisen et al., 2024). Our 
study contributes directly to this XAI conversation. By demonstrating 
that an inherently interpretable, 4-variable model can achieve robust 
performance, we provide a practical solution that balances predictive 
power with the critical, and often overlooked, needs for operational 
efficiency and regulatory transparency.

The  remainder  of  the  paper  is  organized  as  follows:  Section  2 
provides a summary of the risk profiling in the private pension system 
in Türkiye. Section 3 presents the data set and empirical analysis of 
the questionnaire. Finally, Section 4 concludes with a summary and 
discussion of the results. The questions in the risk questionnaire and 
the details on the machine learning models used in the analysis are 
provided in the Appendix.

2. Research context and data

2.1. Türkiye’s private pension system and risk profiling requirements

Türkiye’s  private  pension  system  serves  as  a  supplement  to  the 
state-funded  social  security  retirement  system.  Established  through 
legislation in 2001 and fully operational by 2003 with six pension 
companies, the system saw a total asset investment of approximately 
20 billion USD in 2022, representing around 3% of the nation’s GDP. 
This system operates on a defined contribution basis with voluntary 
participation, allowing individuals to invest in mutual funds managed 
by asset management firms. Unlike the US pension system, partici-
pants cannot invest directly in individual stocks but can choose from 
mutual funds that invest in equities, bonds, or commodities. In 2017, 
the Capital Markets Board of Türkiye (CMB) mandated that financial 
institutions  evaluate  the  risk  tolerance  of  their  clients  and  provide 
financial advice that aligns with clients’ risk preferences. This mandate, 
known  as  suitability,  requires  financial  advisors  to  collect  relevant 
information about clients’ investment goals and risk attitudes before 
making portfolio recommendations, aligning with the EU’s Markets in 
Financial  Instruments  Directive  (MiFID).  This  regulatory  framework 
provides a systematic setting for examining risk profiling approaches, 
as all pension companies are required to use standardized assessment 
tools while participants’ actual portfolio choices may serve as a measure 
of risk-taking behavior.

2.2. The CMB risk assessment framework

To facilitate compliance with the suitability requirement, the CMB 
developed a standardized risk questionnaire designed to classify clients 
according to their risk attitudes. The questionnaire consists of eight 
questions1; the first seven assess risk-taking behavior across different 
dimensions, while the eighth concerns sensitivity to interest-bearing 
assets and is excluded from the total risk score.; the first seven assess 
risk-taking behavior across different dimensions, while the eighth con-
cerns sensitivity to interest-bearing assets and is excluded from the total 
risk score. Each participant’s risk profile is determined by weighted 
scores from the seven relevant questions, which categorize them into 
one of four risk groups: low (0–15 points), medium (16–23 points), high 
(24–32 points), and very high risk (33–47 points).

While this standardized approach ensures consistency across institu-
tions, studies examining global risk assessment practices have identified 
potential limitations in existing questionnaires. Brayman et al. (2015) 
report that only a small percentage of risk assessments may adequately 
fulfill their intended purpose, with issues including suboptimal question 
design  and  simplistic  scoring  approaches.  Several  researchers  have

1 The  complete  questionnaire  with  all  questions,  response  options,  and

scoring weights is provided in Appendix A1.

2

---

<!-- PAGE 3 -->

A. Göncü et al.

noted that many questionnaires used in practice may not meet estab-
lished psychometric standards and often show limited ability to predict 
actual  investment  behavior  (Bouchey,  2004;  Roszkowski  &  Grable, 
2005).

These  observations  regarding  current  risk  assessment  practices, 
combined with developments in machine learning techniques, suggest 
potential  opportunities  to  examine  risk  profiling  effectiveness.  Ma-
chine learning approaches may offer the ability to identify informative 
questions, account for non-linear relationships between variables, and 
potentially provide improved predictions of risk-taking behavior. This 
raises  the  question  of  whether  machine  learning  techniques  might 
enhance the current regulatory approach to risk profiling in Türkiye’s 
pension system.

2.3. Research setting and data overview

This study examines these questions using data from a major pen-
sion fund company in Türkiye, covering the years 2018 to 2022 and 
comprising information on 81,563 participants. The scale of this dataset 
may be suitable for machine learning applications, while the regulatory 
requirement for standardized questionnaires provides consistency in 
risk assessment across participants.

Our analysis is cross-sectional; we observe each participant’s risk 
questionnaire responses at a single point in time, along with their de-
mographic characteristics and average portfolio risk over the 2018–2022 
period.  This  allows  us  to  examine  the  relationship  between  stated 
preferences (questionnaire responses) and revealed preferences (actual 
portfolio choices), which represents an important consideration in risk 
profiling research.

Several aspects of Türkiye’s pension system may provide advantages 
for this research. First, the mandatory use of the CMB questionnaire 
ensures standardized risk assessment across participants. Second, the 
mutual fund structure of investments provides a measurable indicator 
of portfolio risk based on fund volatility ratings. Third, the regulatory 
environment creates incentives for accurate risk assessment, which may 
make our findings relevant to policy and practice.

This research setting allows us to examine three questions that may 
have implications for risk profiling in pension systems: (1) Whether 
machine learning models can improve predictive accuracy compared 
to the current regulatory approach; (2) Which variables appear most 
informative for predicting actual risk-taking behavior; and (3) Whether 
risk assessment questionnaires might be simplified without substan-
tially reducing predictive accuracy. The empirical analysis that follows 
attempts to provide evidence on these questions, which may inform 
regulatory policy and industry practice.

3. Data and empirical analysis

This section details our empirical methodology, structured to pro-
ceed from data exploration to model evaluation. We begin by defining 
our dependent variable, portfolio risk. We then introduce our predictor 
variables and analyze descriptive patterns, highlighting relationships 
that  inform  our  modeling  strategy.  Following  this,  we  outline  our 
modeling approach and employ recursive feature elimination (RFE) to 
identify the most salient predictors. Finally, we present a comparison 
of machine learning models using cross-validation and conclude with 
an interpretation of the results’ practical significance.

The data, covering 81,563 participants from 2018–2022, include 
responses to the CMB risk assessment questionnaire, demographic in-
formation, and portfolio risk measures derived from actual investment 
allocations. Table  1 shows the sample distribution, indicating that most 
participants are male, married, college graduates, with an average age 
of 39.48 years.

Borsa Istanbul Review 26 (2026) 100800

3.1. Portfolio risk: The dependent variable

In the Turkish pension fund system, participants choose from mu-
tual funds that invest across asset classes. The risk level of each fund is 
classified on a scale from 1 (lowest risk) to 7 (highest risk), determined 
by its annualized weekly return volatility over the past five years. The 
regulator provides the standardized formula for this calculation:

√
√
√
√ 𝑚

𝑇 − 1

𝜎𝑓 =

𝑇
∑

(𝑟𝑓 ,𝑡 − ̄𝑟)2

𝑡=1

where  𝑚 = 52,  𝑇 = 260,  𝑟𝑓 ,𝑡  is  the  weekly  return  of  the  fund, 
and  ̄𝑟  is  its  average  weekly  return  over  the  five-year  period.  This 
standardized volatility measure allows us to construct a continuous 
portfolio risk variable that serves as our dependent variable across all 
model specifications (detailed in Appendix A2).

For each individual, we calculate their overall portfolio risk as the 
weighted average of the risk scores of their chosen funds. Our analysis 
uses the average portfolio risk for each participant over the 2018–2022 
period. This continuous measure of revealed risk preference is similar 
to metrics used in prior literature, such as Beauchamp et al. (2017) 
and Cesarini et al. (2010), and offers greater granularity than binary 
indicators like stock ownership.

3.2. Predictor variables and descriptive patterns

Our predictor variables include participant responses to the seven 
core  questions  of  the  CMB  risk  survey  alongside  demographic  and 
economic information. Here, we examine the relationships between 
these variables and portfolio risk to identify patterns that can inform 
our modeling strategy.

Table  2 presents the survey responses and portfolio risk by educa-
tion, marital status, and gender. The investment horizon question (Q1) 
reveals that participants with higher education levels report shorter in-
vestment horizons, while married and male participants indicate longer 
horizons. Self-assessed financial literacy (Q2) demonstrates a negative 
association with education level but is positively associated with being 
male and married. Self-reported risk attitudes (Q3) and preferences 
in investment scenarios (Q4) both exhibit positive associations with 
education level. Similarly, married and male participants demonstrate 
higher risk tolerance in their responses. Responses to the loss reaction 
question (Q5) follow comparable patterns. Questions examining finan-
cial situations (Q6 and Q7) suggest that financial stability increases 
with education level and is generally higher among married and male 
participants. The observed portfolio risk measurements follow patterns 
similar to the questionnaire responses, increasing with education level 
and showing modest elevation for married and male participants.

Table  3 shows questionnaire responses and portfolio risk across age 
categories. An important finding is the non-linear relationship between 
age and risk attitudes, with risk-taking behavior increasing until middle 
age (35–44 category) before declining in older age groups. This pattern 
is particularly evident in portfolio risk measures, which reach 5.02 in 
the 35–44 age group before decreasing to 4.63 for participants aged 
55 and older. This observed pattern is consistent with life-cycle in-
vestment theories. This observed non-linear relationship has important 
implications for our modeling approach. Linear models require explicit 
specification of polynomial terms to capture such patterns, while tree-
based methods can identify these relationships through their recursive 
partitioning process.

Table  4 extends the analysis to income and employment sector. The 
data suggest that risk tolerance generally increases with income levels, 
and that public sector employees exhibit somewhat different response 
patterns compared to those in the private sector.

These  descriptive  findings  provide  motivation  for  our  empirical 
approach. The non-linear age effect suggests that models capable of 
capturing such relationships – either through explicit feature engineer-
ing (e.g., adding an age-squared term) or inherently (e.g., tree-based

3

---

<!-- PAGE 4 -->

A. Göncü et al.

Borsa Istanbul Review 26 (2026) 100800

Fig. 1. Relationship between age and average portfolio risk.

Table 1
Demographic characteristics.
College

Post-College

Age
39.48  
  Mean
9.49  
  S.D.
  Min
18
78.5  
  Max
  N.of Obs.
81 563 
Notes: Demographic characteristics of the pension participants. There are four education categories: primary school, high school, college, and post-college. ‘‘Married’’ is a dummy 
variable equal to 1 if the participant is married, and ‘‘Male’’ is a dummy variable equal to 1 if the participant is male.

High School
0.31
0.46
0
1
24 954

0.57
0.50
0
1
46 231

0.32
0.47
0
1
26 315

0.73
0.45
0
1
59 870

0.68
0.47
0
1
55 248

0.07
0.25
0
1
5712

0.06
0.23
0
1
4666

Primary

Married

Female

Male

Table 2
Responses to the risk questionnaire and portfolio risk: Demographic character-
istics.

Post-Col. College High school Primary Married Single Male Female 
  Q1
3.11
  Q2
2.74
  Q3
3.37
  Q4
2.76
  Q5
2.89
  Q6
2.82
  Q7
3.67
  Portfolio risk 5.01
Notes: Descriptive statistics for risk survey questions, demographic characteristics, and 
the portfolio risk measure.

3.01 2.89
2.40 2.18
3.18 2.91
2.67 2.38
2.87 2.65
2.62 2.52
3.37 3.15
4.98 4.88

3.04
2.44
3.20
2.64
2.83
2.59
3.41
4.99

2.86
2.11
2.91
2.45
2.74
2.41
3.08
4.88

2.85
2.24
2.99
2.48
2.75
2.48
3.17
4.89

2.68
1.96
2.77
2.35
2.67
2.39
2.93
4.77

3.02
2.37
3.14
2.61
2.82
2.57
3.35
4.96

35–44

25–34

18–24

45–54

Table 3
Responses to the questionnaire and portfolio risk: Age groups.
  Age group
55+ 
  Q1
2.35 
  Q2
2.45 
  Q3
3.07 
  Q4
2.6  
  Q5
2.79 
  Q6
2.83 
  Q7
3.57 
4.63 
  Portfolio Risk
Notes: Average responses for risk survey questions and portfolio risk for different age 
categories.

2.54
2.08
2.68
2.29
2.67
2.28
2.78
4.79

2.85
2.44
3.18
2.66
2.84
2.69
3.47
4.88

3.17
2.36
3.17
2.62
2.83
2.55
3.33
5.02

2.99
2.24
3.01
2.49
2.75
2.39
3.16
4.98

ensembles) – may offer better performance. The patterns associated 
with  self-reported  risk  attitudes  (Q3)  and  lottery  choices  (Q4)  also 
suggest these items may be informative predictors.

3.3. Modeling approach and feature selection

To  identify  the  most  predictive  variables,  we  apply  the  RFE  al-
gorithm. This method iteratively ranks and prunes features based on 
their contribution to model performance across our models: ordinary 
least  squares  (OLS),  ridge,  Lasso,  CART,  random  forest,  and  three 
boosting algorithms (GBoost, XGBoost, and LightGBM). The equations 
and algorithmic details for each model are in Appendix A2. Categor-
ical predictor variables – including education, marital status, gender,

Table 4
Responses to the questionnaire and portfolio risk: Income and sector.

Income Q1 Income Q2 Income Q3 Income Q4 Public Private 
  Q1
2.92
  Q2
2.31
  Q3
2.99
  Q4
2.47
  Q5
2.74
  Q6
2.49
  Q7
3.03
  Portfolio Risk 4.93
Notes:  Average  responses  for  risk  survey  questions  and  portfolio  risk  for  income 
quantiles (Q1=lowest, Q4=highest) and sectors of employment.

2.98
2.33
3.08
2.54
2.79
2.49
3.25
4.94

3.08
2.29
3.14
2.64
2.80
2.53
3.41
5.06

2.95
2.18
2.99
2.47
2.73
2.43
3.15
4.91

3.00
2.33
3.13
2.60
2.81
2.55
3.36
4.95

3.02
2.52
3.29
2.78
2.92
2.72
3.67
5.02

income quartiles, and employment sector – are transformed into bi-
nary  variables  using  one-hot  encoding  to  ensure  consistent  feature

4

---

<!-- PAGE 5 -->

A. Göncü et al.

Table 5
Recursive feature selection.

2
4
1
1
5
12
11
3
1

OLSRandom treeRandom forestGBoostXGBoostLGBoostRidgeLassoSelection 
  Q1
2
4
  Q2
3
3
  Q3
1
1
  Q4
1
2
  Q5
5
5
  Q6
7
7
  Q7
8
8
  Age
1
1
  Age-Squared1
14
  Male
11
10 10
  Married
9
14
9
  High-School 14 7
13
  College
10
13 9
  Post-College 12 8
12
  Income
6
11 6
  Public
4
6
Notes: This table lists the feature rankings from the RFE process. A lower rank indicates 
greater importance. The Selection column shows the number of models in which a 
feature ranks first.

15
14
1
1
12
11
10
8
7
9
1
4
6
5
13
2

2
4
1
1
5
9
7
1
3
10
11
13
12
14
6
8

3
4
1
2
5
7
9
1
1
10
8
13
14
12
11
6

4
3
1
2
5
7
8
1
1
10
9
14
13
12
11
6

3
2
4
6
8
7
5
1
14
10
11
13
12
15
1
9

0
0
7
4
0
0
0
6
4
0
1
0
0
0
1
0

13

representation across all models. To accommodate the nonlinear age 
effect identified in our descriptive analysis, we include age-squared 
as  a  predictor  in  all  linear  models  (OLS,  ridge,  Lasso,  elastic  net). 
Tree-based  models  (CART,  random  forest,  and  boosting  algorithms) 
inherently capture these nonlinearities without requiring polynomial 
feature engineering.

All models are tuned using grid search with fivefold cross-validation 
on the training set (80% of data), with mean squared error (MSE) as 
the selection criterion. For example, random forest hyperparameters 
include the number of trees (𝑛_𝑒𝑠𝑡𝑖𝑚𝑎𝑡𝑜𝑟𝑠 ∈ {100, 200}) and maximum 
tree  depth  (𝑚𝑎𝑥_𝑑𝑒𝑝𝑡ℎ ∈ {5, 10}),  with  optimal  values  of  200  and 
10, respectively. Complete details on the search spaces and optimal 
parameters for all models are in Appendix A3.

Table   5  lists  the  feature  rankings  from  each  model.  The  results 
are consistent with the patterns observed in our descriptive analysis. 
Self-reported risk attitude (Question 3) ranks as the most important 
predictor  by  seven  of  the  eight  models,  aligning  with  prior  work 
by Gürdal et al. (2017). Consistent with the life-cycle pattern shown 
in Table  3, age and age-squared are also highly important variables. 
The hypothetical lottery trade-off (Question 4) emerges as another key 
predictor. However, several other demographic and financial condition 
variables are less influential. These findings suggest that a small set, 
consisting of four variables – Questions 3 and 4, age, and age-squared 
– can capture a large proportion of the explanatory power.

To ensure the robustness of our feature selection findings, we con-
duct a comprehensive stability analysis across all 20 cross-validation 
folds  (detailed  in  Appendix  A4).  For  each  fold,  we  apply  the  RFE 
algorithm to the training data, generating 160 total feature rankings 
(20 folds × 8 models) for each variable. Our stability analysis confirms 
that the four core features – Question 3 (self-reported risk attitude), 
Question 4 (lottery choice), age, and age-squared – consistently rank 
among the top predictors across all models and folds, with standard 
deviations  below  5.0,  which  indicates  that  the  selection  is  robust. 
Question 3, in particular, demonstrates exceptional stability (mean rank 
= 2.09, SD = 0.90), whereas all the other features have mean ranks 
of more than 5.0, with no first-place rankings. This cross-validation 
stability suggests that the concise feature set that we identify reflects 
consistent patterns in the data, rather than being highly sensitive to 
particular sampling variations.

3.4. Model performance and comparison

We assess model performance using 20-fold cross-validation, com-
paring  models  trained  on  both  the  full  feature  set  and  the  smaller 
subset of four key features identified by RFE. We report the mean and

Borsa Istanbul Review 26 (2026) 100800

Table 6
Model comparison with cross-validation: All features.
  Model
𝑅2-Mean 𝑅2-Std MSE-Mean MSE-Std MAE-Mean MAE-Std 
  Regulator
0.0086  
0.1314
  OLS
0.0089  
0.1546
  KNN
0.0084  
0.1349
  CART
0.0081  
0.1385
  ANN
0.0086  
0.1510
  Random Forest
0.0083  
0.1522
  GBoost
0.0084  
0.1659
  XGBoost
0.0080  
0.1608
  LGBoost
0.0083  
0.1672
  Ridge
0.0089  
0.1546
  Lasso
0.0089  
0.1538
0.0089  
  Elastic Net
0.1546
Notes: This table compares the mean and standard deviation of 𝑅2, MSE, and MAE 
values across different models using 20-fold cross-validation.

0.01684
0.0175
0.0161
0.0157
0.0158
0.0157
0.0162
0.0151
0.0162
0.0175
0.0173
0.0175

0.6402
0.6300
0.6388
0.6388
0.6305
0.6324
0.6252
0.6273
0.6247
0.6300
0.6306
0.6300

0.0098
0.0094
0.0100
0.0093
0.0109
0.0093
0.0092
0.0091
0.0089
0.0094
0.0090
0.0094

0.6851
0.6668
0.6824
0.6795
0.6693
0.6690
0.6579
0.6619
0.6569
0.6668
0.6675
0.6668

Table 7
Model comparison with cross-validation: Selected features.
𝑅2-Mean 𝑅2-Std MSE-Mean MSE-Std MAE-Mean MAE-Std 
  Model
0.0086  
  Regulator
0.1314
0.6851
0.0092  
  OLS
0.1343
0.6829
0.0091  
  KNN
0.1159
0.6974
0.0086  
  CART
0.1319
0.6847
0.0094  
  ANN
0.1354
0.6813
0.0086  
  Random Forest
0.1384
0.6796
0.0089  
  GBoost
0.1433
0.6758
0.0087  
  XGBoost
0.1387
0.6794
0.0088  
  LGBoost
0.1442
0.6750
0.0092  
  Ridge
0.1343
0.6829
0.0092  
  Lasso
0.1326
0.6842
  Elastic Net
0.0092  
0.1343
0.6829
Notes: This table compares model performance using the selected features (Question 3, 
Question 4, age, and age-squared).

0.01684
0.0179
0.0180
0.0162
0.0169
0.0167
0.0166
0.0163
0.0165
0.0179
0.0178
0.0179

0.0098
0.0087
0.0100
0.0077
0.0086
0.0076
0.0079
0.0070
0.0077
0.0087
0.0083
0.0086

0.6402
0.6409
0.6484
0.6417
0.6406
0.6390
0.6376
0.6395
0.6371
0.6409
0.6416
0.6409

standard deviation of multiple performance metrics: R2, mean squared 
error (MSE), mean absolute error (MAE), and mean absolute percentage 
error (MAPE). Complete cross-validation results for all metrics are in 
Tables A4–A19 (Appendix A5).

As shown in Table  6, when all features are used, boosting methods 
(LightGBM, GBoost, XGBoost) outperform the regulatory benchmark 
and traditional linear models. LightGBM achieves an average 𝑅2 of 
0.1672, whereas the benchmark is 0.1314. The superior performance of 
these models may be due in part to their ability to capture the nonlinear 
age-related patterns observed in Fig.  1. Fig.  2 illustrates these results, 
showing that the ML models, in particular the boosting methods, have 
less performance variability across validation folds than the regulatory 
benchmark.

Next, we evaluate the models using only the four features selected. 
The results, summarized in Table  7, show that several models – includ-
ing GBoost and LightGBM – still outperform the regulator’s score. As 
Fig.  3 illustrates, the performance of models using the smaller feature 
set is comparable to that of models using the full set. This finding 
suggests diminishing returns from including additional questionnaire 
items beyond the most informative ones and indicates that a more 
concise risk assessment may be feasible without a substantial loss of 
predictive power.

3.5. Interpretation of model performance and practical significance

The 𝑅2s for all models (0.13–0.17) should be interpreted carefully. 
Although  these  values  might  appear  low,  they  are  consistent  with 
those  in  the  broader  literature  on  predicting  risk  preferences.  For 
example, Dohmen et al. (2011) and Beauchamp et al. (2017) find com-
parably modest explanatory power in their analyses of risk preference 
elicitation methods.

These  consistent  findings  suggest  that  predicting  financial  risk-
taking is an inherently challenging task. However, the improvement

5

---

<!-- PAGE 6 -->

A. Göncü et al.

Borsa Istanbul Review 26 (2026) 100800

Fig. 2. Model comparison with cross-validation: All features.
Notes: This figure compares the distribution of 𝑅2 across 20 cross-validation folds for every model using the full feature set.

Fig. 3. Model comparison: Selected features.
Notes: This figure compares the distribution of 𝑅2 across 20 cross-validation folds for each model using only the four features selected.

from 0.131 (regulatory benchmark) to 0.167 (LightGBM) represents a 
27 percent relative increase in explained variance. In practical terms, 
this enhancement could translate into more accurate risk categorization 
for thousands of pension participants, potentially reducing mismatches 
between recommended and appropriate investment strategies. To con-
textualize this: correct reclassification by an enhanced model of just 
5 percent of participants into more appropriate risk categories could 
prevent significant portfolio misallocation for approximately 4000 in-
dividuals in our sample alone. Extrapolated to Türkiye’s entire private 
pension system, such improvements could benefit a large number of 
participants.

4. Discussion and conclusion

This study evaluates the effectiveness of machine-learning methods 
in assessing the risk preferences of 81,563 participants in a pension 
fund from a major Turkish company (2018–2022). Our analysis con-
tributes to the literature on risk profiling by comparing the predictive

performance of various ML models against the regulatory benchmark 
currently used in the pension industry.

4.1. Discussion of findings

The modest 𝑅2s across all models (0.13–0.17) warrant careful in-
terpretation. Although these values might initially appear low, they 
are consistent with those in the broader literature on predicting risk 
preferences.  Dohmen  et  al.  (2011)  report  similar  𝑅2s  of  0.10–0.15 
in  predicting  actual  investment  behavior  based  on  risk  preference 
measures, whereas Beauchamp et al. (2017) find comparably modest 
explanatory power in their comprehensive analysis of risk preference 
elicitation methods. These consistent findings across studies suggest 
that  predicting  financial  risk-taking  behavior  is  an  inherently  chal-
lenging task, influenced by numerous factors beyond those captured 
in standard questionnaires. Nonetheless, the improvement from 0.131 
(regulatory benchmark) to 0.167 (LightGBM) represents a 27 percent 
relative  increase  in  explanatory  power.  In  practical  terms,  this  en-
hancement  could  translate  to  more  accurate  risk  categorization  for

6

---

<!-- PAGE 7 -->

A. Göncü et al.

thousands of pension participants. Even modest improvements in risk 
profiling accuracy can have great cumulative effects if the enhanced 
model correctly reclassifies just 5 percent of participants into more 
appropriate  risk  categories.  This  could  prevent  significant  portfolio 
misallocation for approximately 4000 individuals in our sample alone.
Our  findings  both  complement  and  extend  recent  work  in  this 
stream  of  literature.  The  analysis  by  Adekunle  et  al.  (2023)  simi-
larly  identifies  demographic  variables,  in  particular,  age,  as  crucial 
predictors.  However,  although  their  analysis  focuses  on  predicting 
survey-based risk measures, our approach directly predicts actual port-
folio risk, providing a more direct validation of the questionnaire’s 
practical utility. A key factor in this improved performance appears to 
be the ML models’ ability to capture the nonlinear age relationship that 
we identify (Fig.  1), which adds nuance to their findings and suggests 
that simple linear models might overlook important life-cycle patterns 
in risk-taking behavior. Our feature importance results also provide 
empirical support for the factor structure identified by Kuzubaş and 
Saltoğlu (2024). Their factor analysis revealed two latent dimensions – 
risk attitude and financial condition/literacy – and the risk attitude has 
greater predictive power. Our ML analysis independently confirms this 
hierarchy, in which Question 3 (self-reported risk attitude) consistently 
emerges as the most important single predictor. Whereas Kuzubaş and 
Saltoğlu (2024) report that their two-factor model explains approxi-
mately 14 percent of portfolio risk variance, our ML models achieve 
slightly higher explanatory power (as much as 16.7%), which suggests 
that the nonlinear relationships and interactions captured by boosting 
methods offer meaningful, albeit modest, enhancements over linear 
factor models.

Although boosting methods have the highest predictive accuracy, 
their relative opacity can be problematic with regard to regulatory 
acceptance and advisor-client communication, a concern highlighted 
in the explainable AI (XAI) literature. Our feature selection analysis 
(Table  5) offers a potential path forward by identifying a stable and 
interpretable core of four variables that drive most of the predictive 
power:  Question  3  (self-reported  risk),  Question  4  (lottery  choice), 
age, and age-squared. This finding is particularly relevant, given the 
operational challenges that pension funds face with lengthy surveys, 
especially in high-friction channels such as enrollment by phone. A 
more concise, four-item model, though representing a modest trade-off 
in predictive power (a 14% reduction over that of the full LightGBM 
model),  is  considerably  easier  to  implement  at  scale.  Notably,  this 
simpler model still outperforms the original full regulatory benchmark 
(Tables  6 and 7), which suggests use of a practical balance among 
accuracy, transparency, and operational feasibility.

Borsa Istanbul Review 26 (2026) 100800

against the potential benefits, including better risk categorization and 
enhanced participant experience through streamlined assessments. Our 
results show that gradient boosting methods, in particular, LightGBM, 
offer the most promising performance improvement. However, these 
gains are modest, and institutions should have realistic expectations 
about the extent to which ML can improve on current practices. Reg-
ular  model  retraining  and  validation  are  essential  for  maintaining 
accuracy as market conditions and participant demographics evolve. 
Furthermore, ethical considerations about the use of demographic vari-
ables, especially age, require careful attention to ensure that predictive 
models inform, rather than determine, investment recommendations.

Several  limitations  of  this  study  should  be  acknowledged.  First, 
although our data sample is large and representative of the Turkish 
pension market, the findings might not be fully generalizable to other 
regulatory  environments  or  cultural  contexts.  Second,  our  analysis 
focuses  on  predicting  observed  portfolio  risk,  which  itself  may  be 
influenced by factors other than individual preferences, such as advisor 
recommendations and default investment options. Third, the overall 
explanatory power of all the models tested is modest, which suggests 
that significant determinants of portfolio risk are not captured by stan-
dard questionnaires or demographics. The cross-sectional nature of our 
analysis is another limitation; incorporating a time-series dimension 
might help identify additional determinants of risk-taking behavior and 
enable an examination of evolution in risk preferences in response to 
market conditions.

In conclusion, this study provides empirical evidence on the appli-
cation of ML techniques to risk profiling in the pension fund industry. 
Although the modest improvements in predictive accuracy reflect the 
inherent difficulty of predicting risk-taking behavior, they represent 
meaningful progress in a critical financial domain that affects millions 
of people saving for retirement. Our findings suggest that ML meth-
ods can enhance risk assessment through better feature selection and 
nonlinear modeling, but they are not a panacea for addressing the 
fundamental challenges of preference elicitation. The identification of a 
small set of highly predictive, interpretable variables offers a potential 
path toward more efficient risk assessment, balancing the competing 
demands  of  accuracy,  user  experience,  and  regulatory  compliance. 
Future developments in risk profiling might benefit from hybrid ap-
proaches that combine the strengths of traditional questionnaires with 
ML insights, maintaining transparency while capturing the benefits of 
advanced analytics. These approaches merit further investigation across 
diverse cultural and regulatory environments to better understand their 
potential and limitations.

4.2. Implications, limitations, and concluding remarks

CRediT authorship contribution statement

Our findings lead to several realistic policy and implementation 
pathways. For instance, a two-level assessment framework could be 
considered. In such a system, all participants could complete the four-
item Core Risk Module (Q3, Q4, age, age-squared) for a rapid and 
robust initial classification, whereas those who have borderline scores 
or are close to retirement could be routed to the full assessment or 
a human advisor. This approach could efficiently allocate resources 
while addressing implementation challenges. Furthermore, our analysis 
suggests  a  re-evaluation  of  the  questionnaire’s  function.  Items  with 
weak predictive power for portfolio risk, such as those related to the 
investment horizon (Q1) or financial literacy (Q2), could be repur-
posed as part of a separate advisory and educational module, rather 
than for risk classification. Finally, our results strongly indicate that 
any approved risk-profiling model should account for the nonlinear, 
inverted-U-shaped relationship between age and risk-taking, as simple 
linear glide paths appear suboptimal.

From an implementation perspective, pension fund companies con-
sidering ML approaches should weigh several factors. The initial in-
vestment in technical infrastructure and staff training must be balanced

Ahmet  Göncü:  Conceptualization,  Data  curation,  Formal  analy-
sis,  Investigation,  Methodology,  Software,  Validation,  Visualization, 
Writing – original draft, and Writing – review & editing. Tolga U. 
Kuzubaş:  Conceptualization,  Data  curation,  Formal  analysis,  Inves-
tigation, Methodology, Software, Validation, Visualization, Writing – 
original draft, and Writing – review & editing. Burak Saltoğlu: Con-
ceptualization, Data curation, Formal analysis, Investigation, Method-
ology, Software, Validation, Visualization, Writing – original draft, and 
Writing – review & editing.

Funding

No external funding was received for this research.

Declaration of competing interest

The  authors  declare  that  they  have  no  known  competing  finan-
cial interests or personal relationships that could have appeared to 
influence the work reported in this paper.

7

---

<!-- PAGE 8 -->

A. Göncü et al.

Appendix A. Supplementary data

Supplementary material related to this article can be found online

at https://doi.org/10.1016/j.bir.2026.100800.

Data availability

The dataset analyzed in this study is not publicly available due to

confidentiality restrictions and proprietary information.

References

Adekunle,  O.,  Riedl,  A.,  &  Dumontier,  M.  (2023).  Models  towards  risk  behavior 
prediction and analysis: A netherlands case study. arXiv preprint arXiv:2311.04164.
Barboza, F., Kimura, H., & Altman, E. (2017). Machine learning models and bankruptcy

prediction. Expert Systems with Applications, 83, 405–417.

Barsky, R. B., Juster, F. T., Kimball, M. S., & Shapiro, M. D. (1997). Preference 
parameters and behavioral heterogeneity: An experimental approach in the health 
and retirement study. The Quarterly Journal of Economics, 112(2), 537–579.

Beauchamp, J. P., Cesarini, D., & Johannesson, M. (2017). The psychometric and 
empirical properties of measures of risk preferences. Journal of Risk and Uncertainty, 
54, 203–237.

Benefits Canada (2025). Head to head: Are there underlying risks in using AI and 
machine learning in pension administration and governance? benefitscanada.com. 
(Accessed 10 November 2025).

Beshears, J., Choi, J. J., Laibson, D., & Madrian, B. C. (2008). How are preferences

revealed? Journal of Public Economics, 92(8–9), 1787–1794.

Bouchey, P. (2004). Questionnaire quest: New research shows that standard ques-
tionnaires designed to reveal investors’ risk tolerance levels are often flawed or 
misleading. Financial Planning, 1.

Brayman, S., Finke, M., Bessner, E., Grable, J. E., Griffin, P., & Clement, R. (2015). 
Current practices for risk profiling in canada and review of global best practices. 
In Study prepared for the investor advisory panel of the ontario securities commission.
Cai, Y., Tang, Z., & Chen, Y. (2024). Can real-time investor sentiment help predict the 
high-frequency stock returns? Evidence from a mixed-frequency-rolling decomposi-
tion forecasting method. The North American Journal of Economics and Finance, 72, 
Article 102147.

Černevičieṅ e, J., & Kabašinskas, A. (2024). Explainable artificial intelligence (xai) in 
finance: A systematic literature review. Artificial Intelligence Review, 57(8), 216.
Cesarini, D., Johannesson, M., Lichtenstein, P., Sandewall, Ö., & Wallace, B. (2010). 
Genetic  variation  in  financial  decision-making.  The  Journal  of  Finance,  65(5), 
1725–1754.

Dohmen, T., Falk, A., Huffman, D., Sunde, U., Schupp, J., & Wagner, G. G. (2011). 
Individual risk attitudes: Measurement, determinants, and behavioral consequences. 
Journal of the European Economic Association, 9(3), 522–550.

Eichler,  K.  S.,  &  Schwab,  E.  (2024).  Evaluating  robo-advisors  through  behavioral 
finance:  A  critical  review  of  technology  potential,  rationality,  and  investor 
expectations. Frontiers in Behavioral Economics, 3, Article 1489159.

Friedman, D., Isaac, R. M., James, D., & Sunder, S. (2014). Risky curves: On the empirical

failure of expected utility. Routledge.

Gharbawi, M., Ward, E., Bratt, E., Diver, L., Mueller, H., Quartu, R., & Robinson, H.

(2024). Artificial intelligence in uk financial services.

Gürdal, M. Y., Kuzubaş, T. U., & Saltoğlu, B. (2017). Measures of individual risk 
attitudes  and  portfolio  choice:  Evidence  from  pension  participants.  Journal  of 
Economic Psychology, 62, 186–203.

Borsa Istanbul Review 26 (2026) 100800

Hamerle,  A.,  Hane,  C.,  &  Packham,  N.  (2024).  Explainable  machine  learning  for 
financial risk management: Two practical use cases. Statistics, 58(5), 753–772.
Hansen, K. B., & Borch, C. (2022). Alternative data and sentiment analysis: Prospecting 
non-standard data in machine learning-driven finance. Big Data & Society, 9(1), 
Article 20539517211070701.

Hayman, & Genevieve, P. (2024). Pensions in the age of artificial intelligence: Research

report, CFA Institute Research and Policy Center.

Huynh, N., De Mello, L., & Li, K. (2025). Evolution of investor sentiment: A systematic 
literature review and bibliometric analysis. International Review of Economics & 
Finance, 104115.

Kapteyn, A., & Teppa, F. (2011). Subjective measures of risk aversion, fixed costs, and

portfolio choice. Journal of Economic Psychology, 32(4), 564–580.

Khan,  F.  S.,  Mazhar,  S.  S.,  Mazhar,  K.,  A.  AlSaleh,  D.,  &  Mazhar,  A.  (2025). 
Model-agnostic explainable artificial intelligence methods in finance: A systematic 
review, recent developments, limitations, challenges and future directions. Artificial 
Intelligence Review, 58(8), 232.

Khandani, A. E., Kim, A. J., & Lo, A. W. (2010). Consumer credit-risk models via 
machine-learning algorithms. Journal of Banking and Finance, 34(11), 2767–2787.
Kuzubaş, T. U., & Saltoğlu, B. (2024). Survey-based measures of risk attitudes and 
portfolio  risk:  Evidence  from  pension  participants.  Journal  of  Behavioral  and 
Experimental Finance, 43, Article 100973.

Mata, R., Frey, R., Richter, D., Schupp, J., & Hertwig, R. (2018). Risk preference: A

view from psychology. Journal of Economic Perspectives, 32(2), 155–172.

Mena,  J.,  Vaca,  P.,  Martinez,  F.,  &  T-Ap,  J.  (2024).  Enhancing  financial  risk 
prediction with symbolic classifiers: Addressing class imbalance and the accuracy–
interpretability  trade–off.  Humanities  and  Social  Sciences  Communications,  11(1), 
1–16.

Nallakaruppan, M., Chaturvedi, H., Grover, V., Balusamy, B., Jaraut, P., Bahadur, J., 
Meena, V., & Hameed, I. A. (2024). Credit risk assessment and financial decision 
support using explainable artificial intelligence. Risks, 12(10), 164.

Nguyen, M. D. (2025). Advanced investing with deep learning for risk-aligned portfolio

optimization. PLoS One, 20(8), e0330547.

Pedroni, A., Frey, R., Bruhin, A., Dutilh, G., Hertwig, R., & Rieskamp, J. (2017). The

risk elicitation puzzle. Nature Human Behaviour, 1(11), 803–809.

Pension Monitoring Center of Türkiye (EGM) (2025). Private pension system (bes) data 
and statistics. https://www.egm.org.tr/veri-ve-istatistikler/. (Accessed 10 November 
2025).

Reisen,  F.,  de  Almeida,  F.,  &  Gold,  A.  (2024).  Advancing  financial  resilience:  A 
systematic review of default prediction models and future directions in credit risk 
management. PLoS One, 19(5), e0303129.

Roszkowski, M. J., & Grable, J. E. (2005). Estimating risk tolerance: The degree of 
accuracy and the paramorphic representations of the estimate. Journal of Financial 
Counseling and Planning, 16(2).

Shi, S., Tse, R., Luo, W., D’Addona, S., & Pau, G. (2022). Machine learning-driven credit 
risk: A systemic review. Neural Computing and Applications, 34(17), 14327–14339.
Tang,  K.,  Liu,  Z.,  Wu,  D.,  &  Xiong,  Y.  (2024).  Predicting  systemic  financial  risk 
with  interpretable  machine  learning.  International  Journal  of  Forecasting,  40(3), 
1011–1032.

Thomas, S., Goel, M., Verma, P., & Chhablani, G. (2023). Use of machine learning 
and financial risk profiling for sentiment analysis. In Recent advances in material, 
manufacturing, and machine learning (pp. 574–582). CRC Press.

Wilson, C.-A. (2025). Explainable ai in finance: Addressing the needs of diverse stakeholders:

Technical report, CFA Institute Research & Policy Center.

Yaseen, H., & Al-Amarneh, A. (2025). Adoption of artificial intelligence-driven fraud 
detection in banking: the role of trust, transparency, and fairness perception in 
financial institutions in the United Arab Emirates and Qatar. Journal of Risk and 
Financial Management, 18(4), 217.

8

<!-- MARKITDOWN CONVERSION -->

<!-- Full MarkItDown conversion for formatting fidelity. -->

Borsa Istanbul Review 26 (2026) 100800
Contents lists available at ScienceDirect
BorsaIstanbulReview
journal homepage: www.elsevier.com/journals/borsa-istanbul-review
Machinelearningforriskprofiling:Ananalysisofpensionfundparticipants
Ahmet Göncüa, Tolga U. Kuzubaşb ,∗, Burak Saltoğlub
aIstanbul Technical University, Department of Engineering Management,Türkiye
bDepartment of Economics, Boğaziçi University,Türkiye
A R T I C L E I N F O A B S T R A C T
JEL classification: This study examines the use of machine learning (ML) techniques for profiling the risk of pension fund
G11 participants. We analyze a dataset of 81,563 individual investors in a major Turkish pension fund company
G40 (2018–2022), comparing various ML models to the regulatory benchmark. Using recursive feature elimination,
Keywords: we identify self-reported risk attitudes and age – with a nonlinear relationship – as the most important
Feature selection predictors of actual portfolio risk. Our cross-validation results indicate that boosting methods yield modest
Machine learning improvements in predictive accuracy relative to the regulatory risk score. Notably, the performance from using
Pension fund just four variables is comparable to that from using the full questionnaire. Although the overall explanatory
Risk profiling
power remains modest across all models (𝑅2 of 0.13–0.17), the findings suggest that ML can enhance risk
profiling by identifying informative variables and capturing nonlinear relationships. These results have practical
implications for designing more efficient risk assessment tools in pension fund settings, potentially simplifying
questionnaires without sacrificing predictive accuracy.
1. Introduction (2005) and Bouchey (2004) note that many questionnaires fail to meet
established psychometric standards and often show limited ability to
The alignment between investors’ risk preferences and their port- predict actual investment behavior.
folio choices represents a fundamental challenge in financial markets. Risk preferences are commonly assessed through either incentivized
Mismatches between stated preferences and actual investment behav- experimental methods that reveal preferences through observable
ior can lead to suboptimal outcomes, including premature liquidation choices, or self-report measures that elicit stated preferences directly.
during market downturns, inadequate retirement savings, and reduced The literature presents an ongoing debate regarding which approach
long-term wealth accumulation (Brayman et al., 2015). This chal- better captures true risk preferences (Friedman et al., 2014; Beshears
lenge has become increasingly critical as pension systems worldwide et al., 2008; Pedroni et al., 2017; Mata et al., 2018). Some studies
shift toward defined contribution plans, placing greater responsibility suggest that revealed and stated preferences show limited consistency
on individual participants to make appropriate investment decisions. across methods (Pedroni et al., 2017). However, Mata et al. (2018)
In Türkiye, over 9 million participants managed approximately USD note that revealed preference measures do not necessarily demonstrate
55–60 billion in pension assets as of 2024, making accurate risk as- superior predictive validity compared to stated preference measures.
sessment essential for both individual welfare and financial system Nevertheless, both types of risk assessment approaches typically exhibit
stability (Pension Monitoring Center of Türkiye (EGM), 2025). modest predictive power for actual financial risk-taking behavior,
This regulatory requirement, however, is coupled with a signifi- with generally low 𝑅2 values (Barsky et al., 1997; Dohmen et al.,
cant operational challenge. Pension funds and financial institutions, 2011; Beauchamp et al., 2017; Gürdal et al., 2017; Kapteyn & Teppa,
often interacting with clients via high-friction channels like phone 2011).
or digital apps, face major hurdles with long, complex surveys. This Despite growing recognition of these limitations, three critical re-
‘‘participant friction’’ can lead to low completion rates and incomplete search gaps remain. First, while studies have documented the mod-
data (Brayman et al., 2015), creating a critical tension between reg- est predictive power of risk questionnaires (Beauchamp et al., 2017;
ulatory compliance and operational efficiency. Furthermore, studies Dohmen et al., 2011), limited research has systematically compared
examining global risk assessment practices have identified important machine learning (ML) approaches against regulatory benchmarks us-
limitations in many existing questionnaires. Roszkowski and Grable ing actual portfolio data in emerging market contexts. Second, the
∗ Corresponding author.
E-mail address: umut.kuzubas@bogazici.edu.tr (T.U. Kuzubaş).
Peer review under responsibility of Borsa İstanbul Anonim Şirketi.
https://doi.org/10.1016/j.bir.2026.100800
Received 23 July 2025; Received in revised form 19 January 2026; Accepted 19 January 2026
Available online 27 January 2026
2214-8450/Copyright © 2026 Borsa İstanbul Anonim Şirketi. Published by Elsevier B.V. This is an open access article under the CC BY-NC-ND license ( http://creativecommons.org/licenses/by-nc-nd/4.0/ ).

A. Göncü et al. Borsa Istanbul Review 26 (2026) 100800
relative importance of different questionnaire items for predictive ac- on default prediction further confirm the move toward hybrid and
curacy remains unclear, with no consensus on whether comprehensive explainable models for regulatory acceptance (Reisen et al., 2024). Our
assessments are necessary or if simplified tools could achieve com- study contributes directly to this XAI conversation. By demonstrating
parable results—a question with significant practical implications for that an inherently interpretable, 4-variable model can achieve robust
the industry’s participant friction problem. Third, the potential for performance, we provide a practical solution that balances predictive
non-linear relationships between demographic factors and risk-taking power with the critical, and often overlooked, needs for operational
behavior has received insufficient attention, particularly in emerging efficiency and regulatory transparency.
markets where lifecycle patterns may differ. The remainder of the paper is organized as follows: Section 2
This study contributes to this line of research by addressing these provides a summary of the risk profiling in the private pension system
three gaps directly. First, we systematically compare a suite of ML mod- in Türkiye. Section 3 presents the data set and empirical analysis of
els against the regulatory benchmark, using a large, real-world dataset the questionnaire. Finally, Section 4 concludes with a summary and
of 81,563 investors’ actual portfolio risk from an emerging market. discussion of the results. The questions in the risk questionnaire and
Second, we apply feature selection methods to identify a concise, 4- the details on the machine learning models used in the analysis are
variable set of predictors, directly addressing the trade-off between provided in the Appendix.
accuracy and the industry’s need to reduce operational friction. This
shorter set of inputs offers a practical advantage for large-scale im-
2. Research context and data
plementation, especially in phone-based or digital enrollment channels
where lengthy questionnaires create participation barriers. Third, we
2.1. Türkiye’s private pension system and risk profiling requirements
explicitly model and confirm a non-linear relationship between age and
risk-taking. Our work moves beyond the Adekunle et al. (2023) study
Türkiye’s private pension system serves as a supplement to the
(which predicts survey-based risk) and the Kuzubaş and Saltoğlu (2024)
state-funded social security retirement system. Established through
factor analysis by providing a practical, data-driven path toward a more
legislation in 2001 and fully operational by 2003 with six pension
efficient and operationally viable assessment tool.
companies, the system saw a total asset investment of approximately
Our work is situated within a rapidly evolving literature on ML in
20 billion USD in 2022, representing around 3% of the nation’s GDP.
finance. While foundational work focused on credit risk, bankruptcy
This system operates on a defined contribution basis with voluntary
prediction, and fraud detection (e.g., Khandani et al., 2010; Barboza
participation, allowing individuals to invest in mutual funds managed
et al., 2017; Shi et al., 2022), recent research has expanded into three
by asset management firms. Unlike the US pension system, partici-
distinct areas highly relevant to our study.
pants cannot invest directly in individual stocks but can choose from
The first area is the application of ML to personalization in wealth
mutual funds that invest in equities, bonds, or commodities. In 2017,
management, particularly in the high-growth field of robo-advising.
the Capital Markets Board of Türkiye (CMB) mandated that financial
This research directly intersects with behavioral finance, as studies
institutions evaluate the risk tolerance of their clients and provide
now evaluate how these technologies address (or fail to address) in-
financial advice that aligns with clients’ risk preferences. This mandate,
vestor rationality, risk tolerance, and expectations (Eichler & Schwab,
known as suitability, requires financial advisors to collect relevant
2024). Concurrently, researchers are developing complex deep learning
information about clients’ investment goals and risk attitudes before
frameworks for risk-aligned portfolio optimization (Nguyen, 2025).
making portfolio recommendations, aligning with the EU’s Markets in
This trend is particularly relevant for our work, as industry analysis
now highlights the central role of AI in transforming pension systems
Financial Instruments Directive (MiFID). This regulatory framework
and governance (Hayman & Genevieve, 2024), though significant con-
provides a systematic setting for examining risk profiling approaches,
cerns remain about model-fit and the risks of using historical data for
as all pension companies are required to use standardized assessment
long-term predictions (Benefits Canada, 2025).
tools while participants’ actual portfolio choices may serve as a measure
The second stream of research is exploring alternative data, with
of risk-taking behavior.
a strong focus on using Natural Language Processing (NLP) to ex-
tract investor sentiment from unstructured text. This field has matured 2.2. The CMB risk assessment framework
rapidly, with recent systematic reviews mapping its evolution (Huynh
et al., 2025). Current applications range from general sentiment anal- To facilitate compliance with the suitability requirement, the CMB
ysis (Hansen & Borch, 2022) to specific tasks like real-time, high- developed a standardized risk questionnaire designed to classify clients
frequency stock return prediction (Cai et al., 2024) and even using according to their risk attitudes. The questionnaire consists of eight
the text from lottery-choice scenarios to risk-profile investors (Thomas questions1; the first seven assess risk-taking behavior across different
et al., 2023). This research path, focused on mining new data sources, dimensions, while the eighth concerns sensitivity to interest-bearing
contrasts with our study’s focus on making existing, mandatory survey assets and is excluded from the total risk score.; the first seven assess
data smarter and more efficient. risk-taking behavior across different dimensions, while the eighth con-
Finally, the adoption of these increasingly complex models has cerns sensitivity to interest-bearing assets and is excluded from the total
created a significant regulatory and practical challenge: the black box’’ risk score. Each participant’s risk profile is determined by weighted
problem. This is no longer a niche concern; a wave of recent sys- scores from the seven relevant questions, which categorize them into
tematic reviews has highlighted the black box’’ as a central academic one of four risk groups: low (0–15 points), medium (16–23 points), high
and industry-wide challenge (e.g., Khan et al., 2025; Černevičieṅ e (24–32 points), and very high risk (33–47 points).
& Kabašinskas, 2024). This concern is mirrored by stakeholders and While this standardized approach ensures consistency across institu-
regulators, with major bodies like the CFA Institute (Wilson, 2025) and tions, studies examining global risk assessment practices have identified
the Bank of England Gharbawi et al. (2024) now issuing guidance on AI potential limitations in existing questionnaires. Brayman et al. (2015)
transparency. This has spurred a critical field of Explainable AI (XAI) report that only a small percentage of risk assessments may adequately
focused on building transparent models for parallel applications. This fulfill their intended purpose, with issues including suboptimal question
includes developing interpretable models for systemic risk (Tang et al., design and simplistic scoring approaches. Several researchers have
2024), creating frameworks to balance the accuracy-interpretability
trade-off (Hamerle et al., 2024; Mena et al., 2024), and applying
XAI techniques to fraud detection (Yaseen & Al-Amarneh, 2025) and 1 The complete questionnaire with all questions, response options, and
credit risk (Nallakaruppan et al., 2024). Recent systematic reviews scoring weights is provided in Appendix A1.
2

A. Göncü et al. Borsa Istanbul Review 26 (2026) 100800
noted that many questionnaires used in practice may not meet estab- 3.1. Portfolio risk: The dependent variable
lished psychometric standards and often show limited ability to predict
actual investment behavior (Bouchey, 2004; Roszkowski & Grable, In the Turkish pension fund system, participants choose from mu-
2005). tual funds that invest across asset classes. The risk level of each fund is
These observations regarding current risk assessment practices, classified on a scale from 1 (lowest risk) to 7 (highest risk), determined
combined with developments in machine learning techniques, suggest by its annualized weekly return volatility over the past five years. The
potential opportunities to examine risk profiling effectiveness. Ma- regulator provides the standardized formula for this calculation:
c
q
h
u
i
e
n
s
e
ti o
le
n
a
s
r
,
n
a
in
cc
g
o
a
u
p
n
p
t
r
f
o
o
a
r
c h
n
e
o
s
n -
m
li
a
n
y
e a
o
r
f f
r
e
e
r
l a
t
t
h
io
e
n
a
s
b
h
i
i
l
p
it
s
y
b
t
e
o
t w
id
e
e
e
n
n
ti f
v
y
a r
in
ia
f
b
o
l
r
e
m
s,
a t
a
i
n
v
d
e
𝜎 =
√ √ √
√
𝑚 ∑ 𝑇
(𝑟 −𝑟̄)2
𝑓 𝑇 −1 𝑓,𝑡
potentially provide improved predictions of risk-taking behavior. This 𝑡=1
raises the question of whether machine learning techniques might where 𝑚 = 52, 𝑇 = 260, 𝑟 is the weekly return of the fund,
𝑓,𝑡
enhance the current regulatory approach to risk profiling in Türkiye’s and 𝑟̄ is its average weekly return over the five-year period. This
pension system. standardized volatility measure allows us to construct a continuous
portfolio risk variable that serves as our dependent variable across all
2.3. Research setting and data overview
model specifications (detailed in Appendix A2).
For each individual, we calculate their overall portfolio risk as the
weighted average of the risk scores of their chosen funds. Our analysis
This study examines these questions using data from a major pen-
uses the average portfolio risk for each participant over the 2018–2022
sion fund company in Türkiye, covering the years 2018 to 2022 and
period. This continuous measure of revealed risk preference is similar
comprising information on 81,563 participants. The scale of this dataset
to metrics used in prior literature, such as Beauchamp et al. (2017)
may be suitable for machine learning applications, while the regulatory
and Cesarini et al. (2010), and offers greater granularity than binary
requirement for standardized questionnaires provides consistency in indicators like stock ownership.
risk assessment across participants.
Our analysis is cross-sectional; we observe each participant’s risk 3.2. Predictor variables and descriptive patterns
questionnaire responses at a single point in time, along with their de-
mographic characteristics and average portfolio risk over the 2018–2022 Our predictor variables include participant responses to the seven
period. This allows us to examine the relationship between stated core questions of the CMB risk survey alongside demographic and
preferences (questionnaire responses) and revealed preferences (actual economic information. Here, we examine the relationships between
portfolio choices), which represents an important consideration in risk these variables and portfolio risk to identify patterns that can inform
profiling research. our modeling strategy.
Several aspects of Türkiye’s pension system may provide advantages Table 2 presents the survey responses and portfolio risk by educa-
for this research. First, the mandatory use of the CMB questionnaire tion, marital status, and gender. The investment horizon question (Q1)
ensures standardized risk assessment across participants. Second, the reveals that participants with higher education levels report shorter in-
mutual fund structure of investments provides a measurable indicator
vestment horizons, while married and male participants indicate longer
of portfolio risk based on fund volatility ratings. Third, the regulatory
horizons. Self-assessed financial literacy (Q2) demonstrates a negative
environment creates incentives for accurate risk assessment, which may
association with education level but is positively associated with being
male and married. Self-reported risk attitudes (Q3) and preferences
make our findings relevant to policy and practice.
in investment scenarios (Q4) both exhibit positive associations with
This research setting allows us to examine three questions that may
education level. Similarly, married and male participants demonstrate
have implications for risk profiling in pension systems: (1) Whether
higher risk tolerance in their responses. Responses to the loss reaction
machine learning models can improve predictive accuracy compared
question (Q5) follow comparable patterns. Questions examining finan-
to the current regulatory approach; (2) Which variables appear most
cial situations (Q6 and Q7) suggest that financial stability increases
informative for predicting actual risk-taking behavior; and (3) Whether
with education level and is generally higher among married and male
risk assessment questionnaires might be simplified without substan-
participants. The observed portfolio risk measurements follow patterns
tially reducing predictive accuracy. The empirical analysis that follows similar to the questionnaire responses, increasing with education level
attempts to provide evidence on these questions, which may inform and showing modest elevation for married and male participants.
regulatory policy and industry practice. Table 3 shows questionnaire responses and portfolio risk across age
categories. An important finding is the non-linear relationship between
3. Data and empirical analysis age and risk attitudes, with risk-taking behavior increasing until middle
age (35–44 category) before declining in older age groups. This pattern
is particularly evident in portfolio risk measures, which reach 5.02 in
This section details our empirical methodology, structured to pro-
the 35–44 age group before decreasing to 4.63 for participants aged
ceed from data exploration to model evaluation. We begin by defining
55 and older. This observed pattern is consistent with life-cycle in-
our dependent variable, portfolio risk. We then introduce our predictor
vestment theories. This observed non-linear relationship has important
variables and analyze descriptive patterns, highlighting relationships
implications for our modeling approach. Linear models require explicit
that inform our modeling strategy. Following this, we outline our
specification of polynomial terms to capture such patterns, while tree-
modeling approach and employ recursive feature elimination (RFE) to
based methods can identify these relationships through their recursive
identify the most salient predictors. Finally, we present a comparison
partitioning process.
of machine learning models using cross-validation and conclude with
Table 4 extends the analysis to income and employment sector. The
an interpretation of the results’ practical significance. data suggest that risk tolerance generally increases with income levels,
The data, covering 81,563 participants from 2018–2022, include and that public sector employees exhibit somewhat different response
responses to the CMB risk assessment questionnaire, demographic in- patterns compared to those in the private sector.
formation, and portfolio risk measures derived from actual investment These descriptive findings provide motivation for our empirical
allocations. Table 1 shows the sample distribution, indicating that most approach. The non-linear age effect suggests that models capable of
participants are male, married, college graduates, with an average age capturing such relationships – either through explicit feature engineer-
of 39.48 years. ing (e.g., adding an age-squared term) or inherently (e.g., tree-based
3

A. Göncü et al.
Borsa Istanbul Review 26 (2026) 100800
Fig. 1. Relationship between age and average portfolio risk.
Table 1
Demographic characteristics.
  College Post-College High School Primary Married Male Female Age
|  Mean      |       |      |     |       |      |       |       |       |     | 39.48  |
| ---------- | ----- | ---- | --- | ----- | ---- | ----- | ----- | ----- | --- | ------ |
|            | 0.57  | 0.07 |     | 0.31  | 0.06 | 0.73  | 0.68  | 0.32  |     |        |
|  S.D.      |       |      |     |       |      |       |       |       |     |        |
|            | 0.50  | 0.25 |     | 0.46  | 0.23 | 0.45  | 0.47  | 0.47  |     | 9.49   |
|  Min       | 0     | 0    |     | 0     | 0    | 0     | 0     | 0     |     | 18     |
|  Max       | 1     | 1    |     | 1     | 1    | 1     | 1     | 1     |     | 78.5   |
|  N.of Obs. |       |      |     |       |      |       |       |       |     | 81563  |
|            | 46231 | 5712 |     | 24954 | 4666 | 59870 | 55248 | 26315 |     |        |
Notes: Demographic characteristics of the pension participants. There are four education categories: primary school, high school, college, and post-college. ‘‘Married’’ is a dummy
variable equal to 1 if the participant is married, and ‘‘Male’’ is a dummy variable equal to 1 if the participant is male.
| Table 2 |     |     |     |     | Table 3 |     |     |     |     |     |
| ------- | --- | --- | --- | --- | ------- | --- | --- | --- | --- | --- |
Responses to the risk questionnaire and portfolio risk: Demographic character- Responses to the questionnaire and portfolio risk: Age groups.
| istics. |     |     |     |     |  Age group | 18–24 | 25–34 | 35–44 | 45–54 | 55+  |
| ------- | --- | --- | --- | --- | ---------- | ----- | ----- | ----- | ----- | ---- |
  Post-Col. College High school Primary Married Single Male Female   Q1 2.35
|     |           |           |      |                |       | 2.54 | 2.99 | 3.17 | 2.85 |       |
| --- | --------- | --------- | ---- | -------------- | ----- | ---- | ---- | ---- | ---- | ----- |
|  Q1 |           |           |      |                |    Q2 |      |      |      |      | 2.45  |
|     | 3.11 3.04 | 2.86 2.68 | 3.02 | 2.85 3.01 2.89 |       | 2.08 | 2.24 | 2.36 | 2.44 |       |
 Q2 2.74 2.44 2.11 1.96 2.37 2.24 2.40 2.18    Q3 2.68 3.01 3.17 3.18 3.07
 Q3 3.37 3.20 2.91 2.77 3.14 2.99 3.18 2.91    Q4 2.29 2.49 2.62 2.66 2.6
|  Q4 |           |           |      |                |    Q5 |      |      |      |      | 2.79  |
| --- | --------- | --------- | ---- | -------------- | ----- | ---- | ---- | ---- | ---- | ----- |
|     | 2.76 2.64 | 2.45 2.35 | 2.61 | 2.48 2.67 2.38 |       | 2.67 | 2.75 | 2.83 | 2.84 |       |
|  Q5 |           |           |      |                |    Q6 | 2.28 | 2.39 | 2.55 | 2.69 | 2.83  |
|     | 2.89 2.83 | 2.74 2.67 | 2.82 | 2.75 2.87 2.65 |       |      |      |      |      |       |
 Q6 2.82 2.59 2.41 2.39 2.57 2.48 2.62 2.52    Q7 2.78 3.16 3.33 3.47 3.57
|     |     |     |     |     |  Portfolio Risk |     |     |     |     | 4.63  |
| --- | --- | --- | --- | --- | --------------- | --- | --- | --- | --- | ----- |
 Q7 3.67 3.41 3.08 2.93 3.35 3.17 3.37 3.15   4.79 4.98 5.02 4.88
|  Portfolio risk |     |     |     |     |     |     |     |     |     |     |
| --------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
5.01 4.99 4.88 4.77 4.96 4.89 4.98 4.88 Notes: Average responses for risk survey questions and portfolio risk for different age
| Notes: Descriptive statistics for risk survey questions, demographic characteristics, and  |     |     |     |     | categories. |     |     |     |     |     |
| ------------------------------------------------------------------------------------------ | --- | --- | --- | --- | ----------- | --- | --- | --- | --- | --- |
the portfolio risk measure.
Table 4
Responses to the questionnaire and portfolio risk: Income and sector.
ensembles) – may offer better performance. The patterns associated    Income Q1 Income Q2 Income Q3 Income Q4 Private
Public
with self-reported risk attitudes (Q3) and lottery choices (Q4) also
|     |     |     |     |     |  Q1 | 2.92 2.95 | 3.00 | 3.02 | 3.08 | 2.98   |
| --- | --- | --- | --- | --- | --- | --------- | ---- | ---- | ---- | ------ |
|     |     |     |     |     |  Q2 |           |      |      |      |        |
suggest these items may be informative predictors. 2.31 2.18 2.33 2.52 2.29 2.33
|     |     |     |     |     |  Q3 | 2.99 2.99 | 3.13 | 3.29 | 3.14 | 3.08   |
| --- | --- | --- | --- | --- | --- | --------- | ---- | ---- | ---- | ------ |
|     |     |     |     |     |  Q4 | 2.47 2.47 | 2.60 | 2.78 | 2.64 | 2.54   |
|     |     |     |     |     |  Q5 |           |      |      |      |        |
3.3. Modeling approach and feature selection 2.74 2.73 2.81 2.92 2.80 2.79
|     |     |     |     |     |  Q6 |           |      |      |      |        |
| --- | --- | --- | --- | --- | --- | --------- | ---- | ---- | ---- | ------ |
|     |     |     |     |     |     | 2.49 2.43 | 2.55 | 2.72 | 2.53 | 2.49   |
|     |     |     |     |     |  Q7 | 3.03 3.15 | 3.36 | 3.67 | 3.41 | 3.25   |
To identify the most predictive variables, we apply the RFE al-  Portfolio Risk 4.93 4.91 4.95 5.02 5.06 4.94
gorithm. This method iteratively ranks and prunes features based on  Notes: Average responses for risk survey questions and portfolio risk for income
their contribution to model performance across our models: ordinary  quantiles (Q1=lowest, Q4=highest) and sectors of employment.
least squares (OLS), ridge, Lasso, CART, random forest, and three
boosting algorithms (GBoost, XGBoost, and LightGBM). The equations
and algorithmic details for each model are in Appendix A2. Categor-
income quartiles, and employment sector – are transformed into bi-
ical predictor variables – including education, marital status, gender,  nary variables using one-hot encoding to ensure consistent feature
4

A. Göncü et al.
Borsa Istanbul Review 26 (2026) 100800
| Table 5 |     |     |     | Table 6 |     |     |     |     |
| ------- | --- | --- | --- | ------- | --- | --- | --- | --- |
Recursive feature selection. Model comparison with cross-validation: All features.
  OLSRandom treeRandom forestGBoostXGBoostLGBoostRidgeLassoSelection   Model 𝑅2-Mean 𝑅2-Std MSE-Mean MSE-Std MAE-Mean MAE-Std
|  Q1 |     |     |     |    Regulator |     |     |     |     |
| --- | --- | --- | --- | ------------ | --- | --- | --- | --- |
4 2 15 2 2 3 4 3 0 0.1314 0.0098 0.6851 0.01684 0.6402 0.0086
 Q2 3 4 14 4 3 2 3 4 0    OLS 0.1546 0.0094 0.6668 0.0175 0.6300 0.0089
 Q3 1 1 1 1 1 4 1 1 7    KNN 0.1349 0.0100 0.6824 0.0161 0.6388 0.0084
|  Q4 |       |       |       |    CART |               |               |               |     |
| --- | ----- | ----- | ----- | ------- | ------------- | ------------- | ------------- | --- |
|     | 2 1 1 | 1 1 6 | 2 2 4 |         | 0.1385 0.0093 | 0.6795 0.0157 | 0.6388 0.0081 |     |
 Q5 5 5 12 5 5 8 5 5 0    ANN 0.1510 0.0109 0.6693 0.0158 0.6305 0.0086
 Q6 7 12 11 9 7 7 7 7 0    Random Forest 0.1522 0.0093 0.6690 0.0157 0.6324 0.0083
|  Q7 |     |     |     |    GBoost |     |     |     |     |
| --- | --- | --- | --- | --------- | --- | --- | --- | --- |
8 11 10 7 8 5 8 9 0 0.1659 0.0092 0.6579 0.0162 0.6252 0.0084
|  Age |       |       |       |    XGBoost |               |               |               |     |
| ---- | ----- | ----- | ----- | ---------- | ------------- | ------------- | ------------- | --- |
|      | 1 3 8 | 1 1 1 | 1 1 6 |            | 0.1608 0.0091 | 0.6619 0.0151 | 0.6273 0.0080 |     |
 Age-Squared1 1 7 3 14 14 1 1 4    LGBoost 0.1672 0.0089 0.6569 0.0162 0.6247 0.0083
 Male 10 10 9 10 11 10 10 10 0    Ridge 0.1546 0.0094 0.6668 0.0175 0.6300 0.0089
|  Married |     |     |     |    Lasso |     |     |     |     |
| -------- | --- | --- | --- | -------- | --- | --- | --- | --- |
9 14 1 11 9 11 9 8 1 0.1538 0.0090 0.6675 0.0173 0.6306 0.0089
 High-School14 7 4 13 13 13 14 13 0    Elastic Net 0.1546 0.0094 0.6668 0.0175 0.6300 0.0089
|   C o l l e g e | 1 3 9 6 | 1 2 1 0 1 | 2 1 3 1 4 0 |     |     |     |     |     |
| --------------- | ------- | --------- | ----------- | --- | --- | --- | --- | --- |
    N o t e s:   T h i s  t a b l e   c o m p ar e s  t h e   m e a n   a n d   s t a n d a r d   d e v i a t io n of 𝑅2, MSE, and MAE
P o s t - C ollege 1 2 8 5 1 4 1 2 1 5 1 2 1 2 0    d  m s
    va l u e s a cr o s s i f f e r en t o d e l u s in g 2 0 - fo l d c r o ss - v a l id a t i o n .
| In c o m e                                                                                 | 1 1 6 13 | 6 6 1 | 1 1 1 1 1 |         |     |     |     |     |
| ------------------------------------------------------------------------------------------ | -------- | ----- | --------- | ------- | --- | --- | --- | --- |
|  Public                                                                                    | 6 13 2   | 8 4 9 | 6 6 0     |         |     |     |     |     |
| Notes: This table lists the feature rankings from the RFE process. A lower rank indicates  |          |       |           | Table 7 |     |     |     |     |
greater importance. The Selection column shows the number of models in which a  Model comparison with cross-validation: Selected features.
feature ranks first.  Model 𝑅2-Mean 𝑅2-Std MSE-Mean MSE-Std MAE-Mean MAE-Std
|     |     |     |     |  Regulator |               |                |               |     |
| --- | --- | --- | --- | ---------- | ------------- | -------------- | ------------- | --- |
|     |     |     |     |            | 0.1314 0.0098 | 0.6851 0.01684 | 0.6402 0.0086 |     |
|     |     |     |     |  OLS       |               |                |               |     |
|     |     |     |     |            | 0.1343 0.0087 | 0.6829 0.0179  | 0.6409 0.0092 |     |
representation across all models. To accommodate the nonlinear age   KNN 0.1159 0.0100 0.6974 0.0180 0.6484 0.0091
effect identified in our descriptive analysis, we include age-squared   CART 0.1319 0.0077 0.6847 0.0162 0.6417 0.0086
|     |     |     |     |  ANN |     |     |     |     |
| --- | --- | --- | --- | ---- | --- | --- | --- | --- |
as a predictor in all linear models (OLS, ridge, Lasso, elastic net).  0.1354 0.0086 0.6813 0.0169 0.6406 0.0094
|     |     |     |     |  Random Forest | 0.1384 0.0076 | 0.6796 0.0167 | 0.6390 0.0086 |     |
| --- | --- | --- | --- | -------------- | ------------- | ------------- | ------------- | --- |
Tree-based models (CART, random forest, and boosting algorithms)   GBoost 0.1433 0.0079 0.6758 0.0166 0.6376 0.0089
|     |     |     |     |  XGBoost |     |     |     |     |
| --- | --- | --- | --- | -------- | --- | --- | --- | --- |
inherently capture these nonlinearities without requiring polynomial  0.1387 0.0070 0.6794 0.0163 0.6395 0.0087
|     |     |     |     |  LGBoost |     |     |     |     |
| --- | --- | --- | --- | -------- | --- | --- | --- | --- |
feature engineering. 0.1442 0.0077 0.6750 0.0165 0.6371 0.0088
|     |     |     |     |  Ridge | 0.1343 0.0087 | 0.6829 0.0179 | 0.6409 0.0092 |     |
| --- | --- | --- | --- | ------ | ------------- | ------------- | ------------- | --- |
All models are tuned using grid search with fivefold cross-validation
|     |     |     |     |  Lasso | 0.1326 0.0083 | 0.6842 0.0178 | 0.6416 0.0092 |     |
| --- | --- | --- | --- | ------ | ------------- | ------------- | ------------- | --- |
on the training set (80% of data), with mean squared error (MSE) as   Elastic Net
|     |     |     |     |     | 0.1343 0.0086 | 0.6829 0.0179 | 0.6409 0.0092 |     |
| --- | --- | --- | --- | --- | ------------- | ------------- | ------------- | --- |
the selection criterion. For example, random forest hyperparameters
Notes: This table compares model performance using the selected features (Question 3,
include the number of trees (𝑛_𝑒𝑠𝑡𝑖𝑚𝑎𝑡𝑜𝑟𝑠∈{100,200}) and maximum
Question 4, age, and age-squared).
| tree depth (𝑚𝑎𝑥_𝑑𝑒𝑝𝑡ℎ | ∈ {5,10}), with optimal values of 200 and  |     |     |     |     |     |     |     |
| --------------------- | ------------------------------------------ | --- | --- | --- | --- | --- | --- | --- |
10, respectively. Complete details on the search spaces and optimal
parameters for all models are in Appendix A3.
standard deviation of multiple performance metrics: R2, mean squared
Table  5 lists the feature rankings from each model. The results
error (MSE), mean absolute error (MAE), and mean absolute percentage
are consistent with the patterns observed in our descriptive analysis.
error (MAPE). Complete cross-validation results for all metrics are in
Self-reported risk attitude (Question 3) ranks as the most important
Tables A4–A19 (Appendix A5).
predictor by seven of the eight models, aligning with prior work  As shown in Table  6, when all features are used, boosting methods
by Gürdal et al. (2017). Consistent with the life-cycle pattern shown
(LightGBM, GBoost, XGBoost) outperform the regulatory benchmark
in Table  3, age and age-squared are also highly important variables.  and traditional linear models. LightGBM achieves an average 𝑅2 of
The hypothetical lottery trade-off (Question 4) emerges as another key
0.1672, whereas the benchmark is 0.1314. The superior performance of
predictor. However, several other demographic and financial condition
these models may be due in part to their ability to capture the nonlinear
variables are less influential. These findings suggest that a small set,
age-related patterns observed in Fig.  1. Fig.  2 illustrates these results,
consisting of four variables – Questions 3 and 4, age, and age-squared
showing that the ML models, in particular the boosting methods, have
– can capture a large proportion of the explanatory power.
less performance variability across validation folds than the regulatory
To ensure the robustness of our feature selection findings, we con-
benchmark.
duct a comprehensive stability analysis across all 20 cross-validation
Next, we evaluate the models using only the four features selected.
folds (detailed in Appendix A4). For each fold, we apply the RFE
The results, summarized in Table  7, show that several models – includ-
algorithm to the training data, generating 160 total feature rankings
ing GBoost and LightGBM – still outperform the regulator’s score. As
(20 folds × 8 models) for each variable. Our stability analysis confirms
Fig.  3 illustrates, the performance of models using the smaller feature
that the four core features – Question 3 (self-reported risk attitude),
set is comparable to that of models using the full set. This finding
Question 4 (lottery choice), age, and age-squared – consistently rank  suggests diminishing returns from including additional questionnaire
among the top predictors across all models and folds, with standard  items beyond the most informative ones and indicates that a more
deviations below 5.0, which indicates that the selection is robust.  concise risk assessment may be feasible without a substantial loss of
Question 3, in particular, demonstrates exceptional stability (mean rank  predictive power.
= 2.09, SD = 0.90), whereas all the other features have mean ranks
of more than 5.0, with no first-place rankings. This cross-validation  3.5. Interpretation of model performance and practical significance
stability suggests that the concise feature set that we identify reflects
consistent patterns in the data, rather than being highly sensitive to  The 𝑅2s for all models (0.13–0.17) should be interpreted carefully.
particular sampling variations. Although these values might appear low, they are consistent with
those in the broader literature on predicting risk preferences. For
3.4. Model performance and comparison example, Dohmen et al. (2011) and Beauchamp et al. (2017) find com-
parably modest explanatory power in their analyses of risk preference
We assess model performance using 20-fold cross-validation, com- elicitation methods.
paring models trained on both the full feature set and the smaller
These consistent findings suggest that predicting financial risk-
subset of four key features identified by RFE. We report the mean and  taking is an inherently challenging task. However, the improvement
5

A. Göncü et al. Borsa Istanbul Review 26 (2026) 100800
Fig. 2. Model comparison with cross-validation: All features.
Notes: This figure compares the distribution of 𝑅2 across 20 cross-validation folds for every model using the full feature set.
Fig. 3. Model comparison: Selected features.
Notes: This figure compares the distribution of 𝑅2 across 20 cross-validation folds for each model using only the four features selected.
from 0.131 (regulatory benchmark) to 0.167 (LightGBM) represents a performance of various ML models against the regulatory benchmark
27 percent relative increase in explained variance. In practical terms, currently used in the pension industry.
this enhancement could translate into more accurate risk categorization
for thousands of pension participants, potentially reducing mismatches 4.1. Discussion of findings
between recommended and appropriate investment strategies. To con-
textualize this: correct reclassification by an enhanced model of just The modest 𝑅2s across all models (0.13–0.17) warrant careful in-
5 percent of participants into more appropriate risk categories could terpretation. Although these values might initially appear low, they
prevent significant portfolio misallocation for approximately 4000 in-
are consistent with those in the broader literature on predicting risk
dividuals in our sample alone. Extrapolated to Türkiye’s entire private
preferences. Dohmen et al. (2011) report similar 𝑅2s of 0.10–0.15
pension system, such improvements could benefit a large number of
in predicting actual investment behavior based on risk preference
measures, whereas Beauchamp et al. (2017) find comparably modest
participants.
explanatory power in their comprehensive analysis of risk preference
elicitation methods. These consistent findings across studies suggest
4. Discussion and conclusion
that predicting financial risk-taking behavior is an inherently chal-
lenging task, influenced by numerous factors beyond those captured
This study evaluates the effectiveness of machine-learning methods in standard questionnaires. Nonetheless, the improvement from 0.131
in assessing the risk preferences of 81,563 participants in a pension (regulatory benchmark) to 0.167 (LightGBM) represents a 27 percent
fund from a major Turkish company (2018–2022). Our analysis con- relative increase in explanatory power. In practical terms, this en-
tributes to the literature on risk profiling by comparing the predictive hancement could translate to more accurate risk categorization for
6

A. Göncü et al. Borsa Istanbul Review 26 (2026) 100800
thousands of pension participants. Even modest improvements in risk against the potential benefits, including better risk categorization and
profiling accuracy can have great cumulative effects if the enhanced enhanced participant experience through streamlined assessments. Our
model correctly reclassifies just 5 percent of participants into more results show that gradient boosting methods, in particular, LightGBM,
appropriate risk categories. This could prevent significant portfolio offer the most promising performance improvement. However, these
misallocation for approximately 4000 individuals in our sample alone. gains are modest, and institutions should have realistic expectations
Our findings both complement and extend recent work in this about the extent to which ML can improve on current practices. Reg-
stream of literature. The analysis by Adekunle et al. (2023) simi- ular model retraining and validation are essential for maintaining
larly identifies demographic variables, in particular, age, as crucial accuracy as market conditions and participant demographics evolve.
predictors. However, although their analysis focuses on predicting Furthermore, ethical considerations about the use of demographic vari-
survey-based risk measures, our approach directly predicts actual port- ables, especially age, require careful attention to ensure that predictive
folio risk, providing a more direct validation of the questionnaire’s models inform, rather than determine, investment recommendations.
practical utility. A key factor in this improved performance appears to Several limitations of this study should be acknowledged. First,
be the ML models’ ability to capture the nonlinear age relationship that although our data sample is large and representative of the Turkish
we identify (Fig. 1), which adds nuance to their findings and suggests pension market, the findings might not be fully generalizable to other
that simple linear models might overlook important life-cycle patterns regulatory environments or cultural contexts. Second, our analysis
in risk-taking behavior. Our feature importance results also provide focuses on predicting observed portfolio risk, which itself may be
empirical support for the factor structure identified by Kuzubaş and influenced by factors other than individual preferences, such as advisor
Saltoğlu (2024). Their factor analysis revealed two latent dimensions – recommendations and default investment options. Third, the overall
risk attitude and financial condition/literacy – and the risk attitude has explanatory power of all the models tested is modest, which suggests
greater predictive power. Our ML analysis independently confirms this that significant determinants of portfolio risk are not captured by stan-
hierarchy, in which Question 3 (self-reported risk attitude) consistently dard questionnaires or demographics. The cross-sectional nature of our
emerges as the most important single predictor. Whereas Kuzubaş and analysis is another limitation; incorporating a time-series dimension
Saltoğlu (2024) report that their two-factor model explains approxi- might help identify additional determinants of risk-taking behavior and
mately 14 percent of portfolio risk variance, our ML models achieve enable an examination of evolution in risk preferences in response to
slightly higher explanatory power (as much as 16.7%), which suggests market conditions.
that the nonlinear relationships and interactions captured by boosting In conclusion, this study provides empirical evidence on the appli-
methods offer meaningful, albeit modest, enhancements over linear cation of ML techniques to risk profiling in the pension fund industry.
factor models. Although the modest improvements in predictive accuracy reflect the
Although boosting methods have the highest predictive accuracy, inherent difficulty of predicting risk-taking behavior, they represent
their relative opacity can be problematic with regard to regulatory meaningful progress in a critical financial domain that affects millions
acceptance and advisor-client communication, a concern highlighted
of people saving for retirement. Our findings suggest that ML meth-
in the explainable AI (XAI) literature. Our feature selection analysis
ods can enhance risk assessment through better feature selection and
(Table 5) offers a potential path forward by identifying a stable and
nonlinear modeling, but they are not a panacea for addressing the
interpretable core of four variables that drive most of the predictive
fundamental challenges of preference elicitation. The identification of a
power: Question 3 (self-reported risk), Question 4 (lottery choice),
small set of highly predictive, interpretable variables offers a potential
age, and age-squared. This finding is particularly relevant, given the
path toward more efficient risk assessment, balancing the competing
operational challenges that pension funds face with lengthy surveys,
demands of accuracy, user experience, and regulatory compliance.
especially in high-friction channels such as enrollment by phone. A
Future developments in risk profiling might benefit from hybrid ap-
more concise, four-item model, though representing a modest trade-off
proaches that combine the strengths of traditional questionnaires with
in predictive power (a 14% reduction over that of the full LightGBM
ML insights, maintaining transparency while capturing the benefits of
model), is considerably easier to implement at scale. Notably, this
advanced analytics. These approaches merit further investigation across
simpler model still outperforms the original full regulatory benchmark
diverse cultural and regulatory environments to better understand their
(Tables 6 and 7), which suggests use of a practical balance among
potential and limitations.
accuracy, transparency, and operational feasibility.
CRediT authorship contribution statement
4.2. Implications, limitations, and concluding remarks
Ahmet Göncü: Conceptualization, Data curation, Formal analy-
Our findings lead to several realistic policy and implementation
sis, Investigation, Methodology, Software, Validation, Visualization,
pathways. For instance, a two-level assessment framework could be
Writing – original draft, and Writing – review & editing. Tolga U.
considered. In such a system, all participants could complete the four-
Kuzubaş: Conceptualization, Data curation, Formal analysis, Inves-
item Core Risk Module (Q3, Q4, age, age-squared) for a rapid and
tigation, Methodology, Software, Validation, Visualization, Writing –
robust initial classification, whereas those who have borderline scores
original draft, and Writing – review & editing. Burak Saltoğlu: Con-
or are close to retirement could be routed to the full assessment or
a human advisor. This approach could efficiently allocate resources
ceptualization, Data curation, Formal analysis, Investigation, Method-
while addressing implementation challenges. Furthermore, our analysis
ology, Software, Validation, Visualization, Writing – original draft, and
suggests a re-evaluation of the questionnaire’s function. Items with
Writing – review & editing.
weak predictive power for portfolio risk, such as those related to the
investment horizon (Q1) or financial literacy (Q2), could be repur- Funding
posed as part of a separate advisory and educational module, rather
than for risk classification. Finally, our results strongly indicate that No external funding was received for this research.
any approved risk-profiling model should account for the nonlinear,
inverted-U-shaped relationship between age and risk-taking, as simple Declaration of competing interest
linear glide paths appear suboptimal.
From an implementation perspective, pension fund companies con- The authors declare that they have no known competing finan-
sidering ML approaches should weigh several factors. The initial in- cial interests or personal relationships that could have appeared to
vestment in technical infrastructure and staff training must be balanced influence the work reported in this paper.
7

A. Göncü et al. Borsa Istanbul Review 26 (2026) 100800
Appendix A. Supplementary data Hamerle, A., Hane, C., & Packham, N. (2024). Explainable machine learning for
financial risk management: Two practical use cases. Statistics, 58(5), 753–772.
Supplementary material related to this article can be found online Hansen, K. B., & Borch, C. (2022). Alternative data and sentiment analysis: Prospecting
non-standard data in machine learning-driven finance. Big Data & Society, 9(1),
at https://doi.org/10.1016/j.bir.2026.100800.
Article 20539517211070701.
Hayman, & Genevieve, P. (2024). Pensions in the age of artificial intelligence: Research
Data availability report, CFA Institute Research and Policy Center.
Huynh, N., De Mello, L., & Li, K. (2025). Evolution of investor sentiment: A systematic
The dataset analyzed in this study is not publicly available due to
l
F
i
i
t
n
e
a
ra
n
t
c
u
e,
r e
1 0
r
4
ev
1
i
1
e
5
w
.
and bibliometric analysis. International Review of Economics &
confidentiality restrictions and proprietary information.
Kapteyn, A., & Teppa, F. (2011). Subjective measures of risk aversion, fixed costs, and
portfolio choice. Journal of Economic Psychology, 32(4), 564–580.
Khan, F. S., Mazhar, S. S., Mazhar, K., A. AlSaleh, D., & Mazhar, A. (2025).
References Model-agnostic explainable artificial intelligence methods in finance: A systematic
review, recent developments, limitations, challenges and future directions. Artificial
Adekunle, O., Riedl, A., & Dumontier, M. (2023). Models towards risk behavior Intelligence Review, 58(8), 232.
prediction and analysis: A netherlands case study. arXiv preprint arXiv:2311.04164. Khandani, A. E., Kim, A. J., & Lo, A. W. (2010). Consumer credit-risk models via
Barboza, F., Kimura, H., & Altman, E. (2017). Machine learning models and bankruptcy machine-learning algorithms. Journal of Banking and Finance, 34(11), 2767–2787.
prediction. Expert Systems with Applications, 83, 405–417. Kuzubaş, T. U., & Saltoğlu, B. (2024). Survey-based measures of risk attitudes and
Barsky, R. B., Juster, F. T., Kimball, M. S., & Shapiro, M. D. (1997). Preference portfolio risk: Evidence from pension participants. Journal of Behavioral and
parameters and behavioral heterogeneity: An experimental approach in the health Experimental Finance, 43, Article 100973.
and retirement study. The Quarterly Journal of Economics, 112(2), 537–579. Mata, R., Frey, R., Richter, D., Schupp, J., & Hertwig, R. (2018). Risk preference: A
Beauchamp, J. P., Cesarini, D., & Johannesson, M. (2017). The psychometric and view from psychology. Journal of Economic Perspectives, 32(2), 155–172.
empirical properties of measures of risk preferences. Journal of Risk and Uncertainty, Mena, J., Vaca, P., Martinez, F., & T-Ap, J. (2024). Enhancing financial risk
54, 203–237. prediction with symbolic classifiers: Addressing class imbalance and the accuracy–
Benefits Canada (2025). Head to head: Are there underlying risks in using AI and interpretability trade–off. Humanities and Social Sciences Communications, 11(1),
machine learning in pension administration and governance? benefitscanada.com. 1–16.
(Accessed 10 November 2025). Nallakaruppan, M., Chaturvedi, H., Grover, V., Balusamy, B., Jaraut, P., Bahadur, J.,
Beshears, J., Choi, J. J., Laibson, D., & Madrian, B. C. (2008). How are preferences Meena, V., & Hameed, I. A. (2024). Credit risk assessment and financial decision
revealed? Journal of Public Economics, 92(8–9), 1787–1794. support using explainable artificial intelligence. Risks, 12(10), 164.
Bouchey, P. (2004). Questionnaire quest: New research shows that standard ques- Nguyen, M. D. (2025). Advanced investing with deep learning for risk-aligned portfolio
tionnaires designed to reveal investors’ risk tolerance levels are often flawed or optimization. PLoS One, 20(8), e0330547.
misleading. Financial Planning, 1. Pedroni, A., Frey, R., Bruhin, A., Dutilh, G., Hertwig, R., & Rieskamp, J. (2017). The
Brayman, S., Finke, M., Bessner, E., Grable, J. E., Griffin, P., & Clement, R. (2015). risk elicitation puzzle. Nature Human Behaviour, 1(11), 803–809.
Current practices for risk profiling in canada and review of global best practices. Pension Monitoring Center of Türkiye (EGM) (2025). Private pension system (bes) data
In Study prepared for the investor advisory panel of the ontario securities commission. and statistics. https://www.egm.org.tr/veri-ve-istatistikler/. (Accessed 10 November
Cai, Y., Tang, Z., & Chen, Y. (2024). Can real-time investor sentiment help predict the 2025).
high-frequency stock returns? Evidence from a mixed-frequency-rolling decomposi- Reisen, F., de Almeida, F., & Gold, A. (2024). Advancing financial resilience: A
tion forecasting method. The North American Journal of Economics and Finance, 72, systematic review of default prediction models and future directions in credit risk
Article 102147. management. PLoS One, 19(5), e0303129.
Černevičieṅ e, J., & Kabašinskas, A. (2024). Explainable artificial intelligence (xai) in Roszkowski, M. J., & Grable, J. E. (2005). Estimating risk tolerance: The degree of
finance: A systematic literature review. Artificial Intelligence Review, 57(8), 216. accuracy and the paramorphic representations of the estimate. Journal of Financial
Cesarini, D., Johannesson, M., Lichtenstein, P., Sandewall, Ö., & Wallace, B. (2010). Counseling and Planning, 16(2).
Genetic variation in financial decision-making. The Journal of Finance, 65(5), Shi, S., Tse, R., Luo, W., D’Addona, S., & Pau, G. (2022). Machine learning-driven credit
1725–1754. risk: A systemic review. Neural Computing and Applications, 34(17), 14327–14339.
Dohmen, T., Falk, A., Huffman, D., Sunde, U., Schupp, J., & Wagner, G. G. (2011). Tang, K., Liu, Z., Wu, D., & Xiong, Y. (2024). Predicting systemic financial risk
Individual risk attitudes: Measurement, determinants, and behavioral consequences. with interpretable machine learning. International Journal of Forecasting, 40(3),
Journal of the European Economic Association, 9(3), 522–550. 1011–1032.
Eichler, K. S., & Schwab, E. (2024). Evaluating robo-advisors through behavioral Thomas, S., Goel, M., Verma, P., & Chhablani, G. (2023). Use of machine learning
finance: A critical review of technology potential, rationality, and investor and financial risk profiling for sentiment analysis. In Recent advances in material,
expectations. Frontiers in Behavioral Economics, 3, Article 1489159. manufacturing, and machine learning (pp. 574–582). CRC Press.
Friedman, D., Isaac, R. M., James, D., & Sunder, S. (2014). Risky curves: On the empirical Wilson, C.-A. (2025). Explainable ai in finance: Addressing the needs of diverse stakeholders:
failure of expected utility. Routledge. Technical report, CFA Institute Research & Policy Center.
Gharbawi, M., Ward, E., Bratt, E., Diver, L., Mueller, H., Quartu, R., & Robinson, H. Yaseen, H., & Al-Amarneh, A. (2025). Adoption of artificial intelligence-driven fraud
(2024). Artificial intelligence in uk financial services. detection in banking: the role of trust, transparency, and fairness perception in
Gürdal, M. Y., Kuzubaş, T. U., & Saltoğlu, B. (2017). Measures of individual risk financial institutions in the United Arab Emirates and Qatar. Journal of Risk and
attitudes and portfolio choice: Evidence from pension participants. Journal of Financial Management, 18(4), 217.
Economic Psychology, 62, 186–203.
8