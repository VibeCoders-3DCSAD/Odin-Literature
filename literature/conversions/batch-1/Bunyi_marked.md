---
conversion_metadata:
  converted_at: "2026-07-22T12:28:31Z"
  converter_tool: "markitdown"
  converter_version: "0.1.6"
  source_pdf: "Bunyi.pdf"
  source_pdf_sha256: "08f4c4a2f6884076c90cf0981f47df0bca6f6727b831354f7dd2ac8a4bc01896"
  page_count: 28
  markdown_char_count: 142501
---

<!-- PAGE-AWARE EXTRACTION (via pdfminer.six) -->

<!-- PAGE 1 -->

2024

R
E
P
A
P

N
O
I
S
S
U
C
S
I
D

P
S
B

Unpacking the Determinants of 
Financial Resilience in the Philippines

Mary Kryslette C. Bunyi

Series 
No.03 
Classification: GENERAL

BANGKO SENTRAL NG PILIPINAS

---

<!-- PAGE 2 -->

Unpacking the Determinants of Financial Resilience in the Philippines

March 2024

Unpacking the Determinants of Financial Resilience in the Philippines

Mary Kryslette C. Bunyi1

This version: February 2024

ABSTRACT

The  COVID-19  pandemic  exposed  financial  vulnerabilities  as  it  subjected 
households to health shocks and income losses. With inequalities likely to deepen, 
policymakers  may  benefit  from  asking:  What would make Filipinos financially 
in  the  Philippines  by 
resilient?  This  paper  examines  financial  resilience 
demographic  profile  and  employs  Logistic  LASSO  Regression,  Decision  Tree,  and 
other  machine  learning  models  to  create  predictive  models  and  generate 
inferences on determinants of financial resilience using data from the World Bank 
Global Financial Inclusion (Findex) surveys for 2017 and 2021. Variables were chosen 
based  on  the  components  of  Salignac  et  al.  (2019)’s  Multidimensional  Financial 
Resilience  Framework.  Empirical  findings  were  consistent  across  models  and 
suggest  that  demographics  may  provide  higher  predictive  value  for  financial 
resilience  than  financial  access.  Income  quintile,  saving  behavior,  and  gender 
emerged as the top predictors in both the 2017 and 2021 survey rounds. Age, saving 
for retirement, and online payments were also identified as important features for 
2017,  and  tertiary  education  and  medical  borrowing  for  2021.  Insights  from  this 
study could provide policymakers with baseline information on financial resilience 
in the Philippines and support interventions to identify and empower the financially 
vulnerable towards financial security.

JEL classification

:  D12, D14, G51, I30

Key words

:

financial resilience, financial vulnerability, 
financial inclusion, machine learning

Corresponding author

:  BunyiMC@bsp.gov.ph

Disclaimer: The views expressed in this discussion paper are solely the author’s and do not 
represent the official position of the Bangko Sentral ng Pilipinas.

1 Mary Kryslette C. Bunyi is Bank Economist IV at the Department of Economic Research.

Department of Economic Research   |   Discussion Paper Series No. xx

Page 2 of 28

---

<!-- PAGE 3 -->

Unpacking the Determinants of Financial Resilience in the Philippines

March 2024

I.

Introduction

Posting an average economic growth of 6.4 percent (at constant 2018 prices) 
from 2010 to 2019, the Philippines has benefited from one of the fastest economic 
growth  rates  in  the  world.  However,  deeply  entrenched  inequality2  persists  as  a 
conundrum  to  policymakers  who  seek  to  make  growth  more  inclusive  for  all 
Filipinos (Oxford Business Group, 2020).

A World Bank (2020) survey on the impact of COVID-19 found that income 
losses affected  40 percent  of households, especially  non-farm entrepreneurs. The 
study  further  notes  that  “the  poor  and  vulnerable,  many  of  whom  work  in  the 
informal sector, are especially likely to experience significant welfare losses, given 
their  limited  capacity  to  manage  risks”  (World  Bank, 2020,  p. 44).  Inequalities  are 
also  likely  to  deepen  in  the  aftermath  of  the  COVID-19  pandemic,  as  pandemics 
have historically done (Jurzyk et al., 2020).

To  increase  financial  safety  nets  for  the  vulnerable  sector,  the  Philippine 
government  has  implemented  various  interventions  even  before  the  pandemic 
such as agricultural insurance subsidies (World Bank, 2020); Credit Surety Fund for 
micro,  small,  and  medium  enterprises  (Bangko  Sentral  ng  Pilipinas,  2018);  and 
Emergency  Cash  Transfer  (ECT)  for  targeted  financial  assistance  to  the  poorest 
households (World Bank, 2020). Nonetheless, there have been recommendations to 
“assess  [the]  targeting  of  social  protection  programs”  (Economic  Policy  Research 
Institute,  2020,  p.  24)  given  the  disparities  observed  between  the  recipients  of 
financial assistance from different government units.

Financial inclusion, while an important contributor to financial resilience, is 
not sufficient to guarantee the latter. Financial inclusion refers to the accessibility, 
usage, and quality of financial products and services (Bangko Sentral ng Pilipinas, 
2022). On the other hand, financial resilience is concerned with the ability to deal 
with  financial  shocks  (Demirgüç-Kunt  et  al.,  2022).  The  link  between  financial 
inclusion and financial resilience is highlighted in the Philippines’ National Strategy 
for  Financial  Inclusion  2022-2028,  whose  overarching  vision  is  to  steer  “financial 
inclusion  toward  inclusive  growth  and  financial  resilience”  (Financial  Inclusion 
Steering Committee, 2023).

Country-level  data  from  the  2017  World  Bank  Global  Financial  Inclusion 
(Global  Findex)  Survey3  showed  that  while  individuals  in  countries  with  high 
financial  access  do  tend  to  report  high  financial  resilience,  it  is  also  possible  to 
exhibit high access but remain low in resilience. For instance, South Africa reported 
69.2 percent financial account ownership but only 28.7 percent financial resilience. 
The  converse  also  holds  –  Vietnam  was  found  to  be  low  in  financial  access  (30.8 
percent account ownership) but high in financial resilience (70.0 percent).

Similarly,  while  the  Global  Findex  2021  survey  finds  71  percent  financial 
account  ownership  in  developing  economies,  financial  resilience  in  these  areas 
stand  at  55 percent  (Klapper  &  Tayag,  2022).  Half  of  respondents  in  developing

2 The country’s income Gini ratio was measured at 0.45 in 1985, peaked at 0.49 in 1997, and has since gradually 
declined to 0.41 in 2021 (based on Philippine Statistics Authority (PSA) estimates as extracted from CEIC). The 
World Bank notes that the Philippines has one of the highest rates of income inequality in East Asia, second only 
to Thailand for countries with available data as of 2018 (World Bank, 2022b). 
3 Readers may refer to Section 3 (Data) for a broad description of the World Bank Global Findex Survey.

Department of Economic Research   |   Discussion Paper Series No. xx

Page 3 of 28

---

<!-- PAGE 4 -->

Unpacking the Determinants of Financial Resilience in the Philippines

March 2024

economies  were  “very  worried”  about  expenses  that  could  arise  from  medical-
related shocks such as illnesses and accidents (Demirgüç-Kunt et al., 2022).

As  an  emerging  economy,  the  Philippine  government  must  contend  with 
limited capacity and resources. Policies should be crafted to provide the greatest 
assistance  to  those  in  greatest  need.  Empowering  the  vulnerable  to  achieve 
financial resilience is key to lifting them out of poverty and helping them stay out 
of  it.  Determining  the  most  important  environmental  factors  that  build  financial 
resilience  and  establishing  the  characteristics  of  the  financially  vulnerable  would 
aid in designing better targeted interventions to curb their financial insecurity and 
help them achieve upward economic mobility.

This  paper  contributes  to  the  literature  by  investigating  the  research 
question: What makes Filipinos financially resilient? Using 2017 and 2021 survey data 
from  the  World  Bank  Global  Financial  Inclusion  (Findex)  Database,  this  paper 
employed Logistic LASSO Regression, Decision Tree, and machine learning models 
to generate predictions and produce inferences on the most important predictors 
of  financial  resilience.  This  paper  also  contextualizes  empirical  results  against 
existing financial inclusion literature, which could offer policymakers insights into 
the dynamics between demographics, financial inclusion, and financial  resilience 
in the Philippines.

The rest of this paper is organized as follows. Section 2 briefly surveys related 
literature on financial resilience. Section 3 presents an overview of the dataset and 
the selection of variables used for the analysis. Section 4 characterizes the data and 
analyzes  financial  resilience  by  demographic  profile.  Section  5  explains  model 
choice based on the data characterization in the prior section. Section 6 discusses 
the results of the prediction exercise and generates inferences on key explanatory 
variables based on the modeling results. Finally, Section 7 concludes the paper and 
offers potential policy implications.

II.  Related Literature

Financial  resilience  is  a  multifaceted  concept  that  has  typically  been 
characterized  as  the  ability  to  withstand  unexpected  income  loss  or  financial 
shocks (e.g., Klapper & Morduch, 2023 and Clark & Mitchell, 2022). It has also been 
viewed from a resource-centric perspective, focusing on individuals’ access to and 
usage of internal capabilities as well as external support during financial hardships 
(Salignac  et  al.,  2019).  Similarly,  financial  vulnerability  has  been  defined  as 
over-indebtedness,  falling  behind  on  utility  payments,  payments,  insufficient 
discretionary income, and susceptibility to financial shocks (Fernandez-Lopez et al., 
2023), among others.

Research on financial resilience has investigated its nexus with factors such 
as  financial  literacy,  financial  inclusion,  financial  behavior,  education,  income, 
gender, and age.

Klapper  and  Lusardi  (2019)  argued  that  financial  literacy  can  strengthen 
financial  resilience  as  it  prevents  over-indebtedness  and  encourages  savings 
diversification. They found substantial gaps in financial literacy rates across income 
levels (i.e., between the richest 60 percent and the poorest 40 percent households) 
and  educational  attainment  (i.e.,  between  recipients  of  primary,  secondary,  and 
tertiary education).

Department of Economic Research   |   Discussion Paper Series No. xx

Page 4 of 28

---

<!-- PAGE 5 -->

Unpacking the Determinants of Financial Resilience in the Philippines

March 2024

Clark  and  Mitchell  (2022)  designed  a  financial  resilience  index  based  on 
questions  regarding  a  household’s  ability  to  handle  unexpected  income  loss, 
financial planning behavior, perception of debt, and overall financial concern. They 
found  that  Americans  who  reported  higher  levels  of  resilience  at  the  start  of  the 
pandemic experienced lower levels of financial fragility a year after. They also found 
that  financial  fragility  was  lower  for  higher-income,  higher-educated,  and  more 
financially literate households. Financial fragility is a self-reported measure of the 
respondents’ level of confidence in their ability to gather USD2,000 in emergency 
funds within the next month.

Salignac  et  al.  (2019)  proposed  a  multidimensional  financial  resilience 
framework  in  their  analysis  of  financial  vulnerability  in  Australia.  The  authors 
developed a survey to gauge access to, or demonstration of, the framework’s four 
components  –  economic  resources,  financial  resources,  financial  knowledge  and 
behavior,  and  social  capital.  The  survey  also  accounted  for  the  respondents’ 
demographic characteristics, including educational attainment, home ownership, 
employment status, income level, gender, and age.

The study employed a linear regression model to predict composite financial 
resilience scores. Researchers marked responses to survey questions from 1 (severely 
financially  vulnerable)  to  4 (financially  resilient),  took  the  average  score  of  the 
relevant responses for each component, and then calculated the component mean 
to arrive at the composite financial resilience score.

The  authors  found  positive  associations  between  financial  resilience  and 
both income level and education. They also found that unsatisfactory employment 
situations  (i.e.,  being  underemployed,  unemployed,  and  working  solely  odd  jobs) 
were  linked  with  financial  vulnerability.  In  addition,  adults  aged  18-24  obtained 
significantly higher resilience scores than those aged 35–49. Finally, they found no 
significant evidence of a gender gap.

Hussain et al. (2019) analyzed the impact of financial inclusion on financial 
resilience using 2014 Global Findex data for Bangladesh. The authors ran chi-square 
tests  and  logistic  regression  models,  accounting  for  variables  such  as  financial 
account ownership, gender, education level, income quintile, and saving behavior. 
They  found  that  financial  resilience  rises  with  account  ownership,  education, 
income level, and saving behavior. They also noted a significant gender divide.

Similarly,  Fernandez-Lopez  et  al.  (2023)’s  survey  of  financial  vulnerability 
studies  showed  widespread  use  of  (ordered)  logit,  (ordered)  probit,  and  ordinary 
least squares regression in estimating different measures of financial vulnerability. 
The use of logit models was likewise noted in studies with definitions of financial 
vulnerability comparable to the Global Findex. Examples are Lee et al. (2019), which 
defined financial vulnerability as the “lack of emergency savings or rainy-day funds 
for three months”, and Philippas & Avdoulas (2020), whose dependent variable was 
the self-reported  inability  “to  raise €300  to tackle a  rush next month”  (as cited in 
Fernandez-Lopez et al., 2023).

In  the  Philippines,  financial  resilience  has  been  identified  as  one  of  the 
central goals of the Philippines’ National Strategy for Financial Inclusion 2022-2028 
(Financial Inclusion Steering Committee, 2023). The Financial Inclusion Survey (FIS) 
conducted by the Bangko Sentral ng Pilipinas (BSP) has also begun capturing the 
concept  of  financial  resilience  in  its  2021  survey  round.  While  the  topic  was  not 
covered  in  the  nationwide  quantitative  survey,  it  was  a  central  issue  in  the 
accompanying focus group discussions (FGDs) conducted in Mindanao in May 2022.

Department of Economic Research   |   Discussion Paper Series No. xx

Page 5 of 28

---

<!-- PAGE 6 -->

Unpacking the Determinants of Financial Resilience in the Philippines

March 2024

Apart  from  such  efforts  to  understand  and  integrate  financial  resilience  in 
policymaking, to the author’s knowledge, research focusing on the topic has yet to 
be conducted in the Philippine context.

III. Data

Dataset Overview

Financial  resilience  data  at  the  individual  level  remains  limited  in  the 
Philippines.  Nonetheless,  the  publicly  available  Global  Findex  Database  could 
surface information that may be useful in assessing the determinants of financial 
resilience  (Demirgüç-Kunt  et  al.,  2018).  The  Global  Findex  Survey  collects 
information  on  individuals’  access,  use,  and  perception  of  financial  services  and 
technologies. The survey also gathers data on financial resilience, which is framed 
as the ability of the respondent to gather emergency funds within the next month 
amounting to 5 percent of the country’s Gross National Income (GNI) per capita. This 
is  equivalent  to  around  1  month’s  salary  for  an  average  worker  in  the  Philippines 
(Kempis & Morduch, 2020).

The Global Findex Surveys are taken from nationally representative samples 
of adults aged 15 and above from more than 140 economies (Demirgüç-Kunt et al., 
2018).  Gallup,  Inc.  conducts  the  surveys  alongside  the  annual  Gallup  World  Poll. 
Since  the  Findex’s  launch  in  2011,  the  surveys  have  been  completed  in  3-year 
intervals,  with  the  latest  round  delayed  to  2021-2022  due  to  the  COVID-19 
pandemic4.

Since 2011, the global surveys have taken place through a mix of phone-based 
and  face-to-face  interviews,  depending  on  telephone  coverage  and  the  country’s 
conventional  survey  methodology.  Prior  to  the  pandemic,  most  developing 
economies were surveyed face-to-face. Several, including the Philippines, shifted to 
phone-based surveys in 2021 due to COVID-19 restrictions.

Data  collection  for  the  2017  Global  Findex  Survey  in  the  Philippines  took 
place  through  computer-assisted  face-to-face  interviews  of  1,000  respondents 
conducted  from  July  to  August  2017  (Demirgüç-Kunt  et  al.,  2018).  The  surveys 
employed a stratified sampling approach based on population size, geography, or 
both.  Households  were  chosen  through  random  route  procedures.  For  each 
household, individual respondents were randomly selected from eligible household 
members.  The  survey  was  carried  out  in  seven  languages,  namely:  Filipino,  Iluko, 
Hiligaynon, Cebuano, Masbatenyo, Waray, and Tausug.

On the other hand, the country’s 2021 survey round was conducted through 
phone-based  interviews  of  1,000  respondents  in  September  to  November  2021 
(Demirgüç-Kunt  et  al.,  2022).  Sampling  was  done  through  either  mobile  phone 
random  digit  dialing  or  extraction  of  a  nationally  representative  list  of  phone 
numbers. The survey was carried out in four languages, namely: Filipino, Cebuano, 
Bicol, and Waray.

Using  the  Global  Findex  dataset  to  examine  the  determinants  of  financial 
resilience has immediately perceptible limitations in terms of the timeliness of data 
collection and the narrow proxy measure for financial resilience. Moreover, model

4 As of writing, the World Bank has conducted Global Findex Surveys in 2011, 2014, 2017, and 2021-2022.

Department of Economic Research   |   Discussion Paper Series No. xx

Page 6 of 28

---

<!-- PAGE 7 -->

Unpacking the Determinants of Financial Resilience in the Philippines

March 2024

accuracy may be hampered by the lack of relevant demographic variables such as 
geographic location and occupation and predominantly binary variables.

Measurement  errors  may  likewise  arise  due  to  self-reporting.  Respondents 
may  incorrectly  recall  or  withhold  information  that  they  deem  shameful  (for 
instance, their ability to satisfy the condition for financial resilience). Nonetheless, 
the conduct of the interviews in the respondents’ native languages attempts to curb 
misunderstanding and response bias.

Data Preprocessing

In  selecting  predictive  attributes  for  the  model,  the  primary  consideration 
was to capture characteristics that may conceivably possess links to an individual’s 
financial  resilience.  Table  1  shows  the  list  of  variables  chosen  for  this  purpose, 
patterned  after  Salignac  et  al.  (2019)’s  Multidimensional  Financial  Resilience 
Framework. These attributes are present in both the 2017 and 2021 survey datasets. 
Most  are  binary  variables,  except  for  age, which  is  numeric/ratio;  education  level, 
which is ordinal; and income quintile, which is ordinal.

Financial 
Resources 
(4)

Table 1: Predictive Attributes Selected for the Model 
Financial 
Knowledge 
and Behavior  
(8) 
• Saved* 
• Saved for

Social Capital 
(1)

• Borrowed

from Family/ 
Friends*

Demographic 
Variables  
(4)

•  Age 
•  Sex 
•  Education

Level3 
•  Part of

Workforce

Economic 
Resources  
(6)

•  Income 
Quintile1 
•  Received 
Wages* 
•  Received

Agricultural 
Payments*

•  Received

Government 
Transfers* 
•  Received 
Pension*

•  Mobile Phone

Owner

• Financial 
Account 
Owner

• Debit

Cardholder

• Credit

Cardholder

• Mobile 
Money 
Account 
Owner

Retirement*

• Borrowed*  
• Borrowed for

Medical 
Purposes*

• Sent

Domestic 
Remittance*

• Received 
Domestic 
Remittance* 
• Paid Utilities* 
• Online

Transaction*2

Source: Author’s analysis 
* denotes behavior in the past 12 months. 
1  Income Quintile classifies  respondents  into  the  poorest  up  to  the  richest  20  percent  of 
households. 
2 Online Transaction  is  a  feature  generated  by  merging  responses  to  the  use  of  the  internet  in

making bill payments and online purchases.

3 Education level classifies respondents into “Primary or lower”, “Secondary”, and “Tertiary or more”. 
However,  it  is  uncertain  whether  academic  completion  is  required  to  be  considered  under 
“Secondary” or “Tertiary or more”.

To  eliminate  missing  data,  observations  were  dropped  where  respondents 
refused to answer or did not know the answer to any of the selected attributes. This 
trimmed the 2017 dataset from 1,000 to 980 data points and the 2021 dataset from 
1,000 to 992 data points. While both used the same 23 predictors, the target variable

Department of Economic Research   |   Discussion Paper Series No. xx

Page 7 of 28

---

<!-- PAGE 8 -->

Unpacking the Determinants of Financial Resilience in the Philippines

March 2024

of financial resilience changed as more specific responses were introduced in the 
2021 survey round5.

In  2017,  respondents  assessed  their  ability  to  gather  emergency  funds  as 
“possible”  or  “not  possible”.  In  2021,  the  evaluation  shifted  to  difficulty,  as 
respondents  chose  between  “not  difficult  at  all”,  “somewhat  difficult”,  and  “very 
difficult”. For comparability across survey rounds, respondents who answered that 
they  would  encounter  little  to  no  difficulty  in  raising  the  subject  funds  were 
considered financially resilient.

IV. Descriptive Results

Financial resilience is relatively balanced in both the 2017 and 2021 surveys 
(Figure 1). The high frequency of both outcomes would suggest that the model may 
be able to learn substantially about each class to make an adequate prediction.

Figure 1: Financial Resilience Self-Ratings

2017

2021

Source: Author’s estimates based on Global Findex data

For the 2017 survey round, financial resilience is roughly equally distributed 
across age groups, except for respondents aged 20 to 40, who displayed a higher 
level of resilience (Figure 2). On the other hand, 2021 survey respondents were more 
financially resilient overall, except for those younger than 25 years old. Investigating 
the interaction between workforce participation and age in determining resilience 
(Figure 3), a considerably higher percentage of 2017 survey respondents who were 
not  in  the  workforce reported  less  resilience,  except for  those  in their  late  20s  to 
early  30s,  who  were  markedly  more  financially  resilient  than  their  counterparts  – 
possibly because their exclusion from the labor force is by choice6. The same general 
pattern holds for 2021 survey respondents.

Figure 2: Financial Resilience by Age

2017

2021

5 A slight modification in phrasing was also implemented in the 2021 survey round. While the 2017 survey asked 
about the availability of emergency funds "within the next month", in 2021 the reference period changed to 
"within the next 30 days". 
6 The labor force comprises both the employed and the unemployed job-seekers. It excludes unpaid workers, 
family workers, and students. (Source: World Bank via https://data.worldbank.org/indicator/SL.TLF.TOTL.IN)

Department of Economic Research   |   Discussion Paper Series No. xx

Page 8 of 28

---

<!-- PAGE 9 -->

Unpacking the Determinants of Financial Resilience in the Philippines

March 2024

Source: Author’s estimates based on Global Findex data

Figure 3: Financial Resilience by Age and Workforce Participation

2017

2021

Source: Global Findex, Author’s estimates

A  breakdown  by  income  quintile  shows  a  balanced  dataset  for  the  2017 
survey and a higher percentage of adults from the richest 20 percent for the 2021 
survey  (Figure  4).  As  expected,  richer  households  reported  higher  financial 
resilience, although the proportion of non-financially resilient among  the highest 
socioeconomic  class  in  the  2017  survey  is  surprisingly  elevated  at  30  percent. 
Financial resilience also appears to have declined from 2017 to 2021 for the poorest 
40 percent, and the opposite for the richest 60 percent. Examining the interaction 
between  education and  income  level, the 2017 and 2021 surveys both reveal that

Department of Economic Research   |   Discussion Paper Series No. xx

Page 9 of 28

---

<!-- PAGE 10 -->

Unpacking the Determinants of Financial Resilience in the Philippines

March 2024

the  educated  tend  to  be  more  financially  resilient  and  also  belong  to  higher 
socioeconomic  classes  (Figure 5).  These  results  align  with  Debuque-Gonzales  and 
Corpus (2021)’s findings that lesser educated and lower-income individuals are less 
likely to be financially included.

Figure 4: Financial Resilience by Income

2017

2021

Source: Author’s estimates based on Global Findex data

Figure 5: Financial Resilience by Income Quintile and Education 
2017

2021

Source: Author’s estimates based on Global Findex data

Gender gaps have been widely noted in much of financial inclusion literature 
(e.g.,  Sahay  &  Cihak,  2018).  Results  for  the  2017  and  2021  Global  Findex  Database 
show  a  similar  gap  in  terms  of  financial  resilience  (Tables  2a  and  2b).  While  the 
difference is less pronounced  in the 2017 survey  compared  to other country-level 
studies that have used the Global Findex (e.g., Hussain et al., 2019), the gender gap 
in  financial  resilience  noticeably  widened  in  2021.  These  results  contrast  against 
findings  from  the  2017  Global  Findex  data  that  females  in  the  country  are  more

Department of Economic Research   |   Discussion Paper Series No. xx

Page 10 of 28

---

<!-- PAGE 11 -->

Unpacking the Determinants of Financial Resilience in the Philippines

March 2024

likely  to  own  a  bank  account  than  males,  with  the  gap  estimated  at  around  10 
percentage points (Debuque-Gonzales and Corpus, 2021).

Table 2a: Financial Resilience by Sex - 2017

Sex

Female 
Male

Not Financially 
Resilient

Financially 
Resilient

297 
199

254 
230

Total

551 
429

Table 2b: Financial Resilience by Sex – 2021

Sex

Not Financially 
Resilient

Financially 
Resilient

Female 
Male 
Source: Author’s estimates based on Global Findex data

296 
289

275 
132

Total

571 
421

Financial 
Resilience 
(in percent) 
46.1 
53.6

Financial 
Resilience 
(in percent) 
51.8 
68.6

Respondents in the 2021 Global Findex survey are substantially younger than 
those interviewed for the 2017 survey (Tables 3a and 3b). The standard deviation of 
17.5 years in the 2017 survey suggests that the data is reasonably spread out and that 
the  majority  of  respondents  are of  working  age  (i.e.,  aged  23  to 58).  On  the other 
hand,  for  the  2021  survey,  the  majority  of  respondents  are  aged  20  to  46.  The 
younger demographic could, in part, stem from the change in interview mode due 
to  the  COVID-19  pandemic,  as  researchers  shifted  from  face-to-face  interviews  in 
2017  to  phone  surveys  in  2021.  This  is  consistent  with  reports  of  the  Philippines 
having one of the highest generational divides globally both in terms of internet use 
and smartphone ownership.7

Table 3a: Descriptive Statistics for Numeric Variables - 2017

Variable 
Age (in years) 
Income Quintile

Minimum 
15 
1

Mean 
40.5 
3.1

SD 
17.5 
1.4

Median 
37 
3

Maximum 
95 
5

Table 3b: Descriptive Statistics for Numeric Variables – 2021

Variable 
Age (in years) 
Income Quintile 
Source: Author’s estimates based on Global Findex data

Minimum 
15 
1

Mean 
32.9 
3.4

SD 
12.6 
1.4

Median 
31 
4

Maximum 
87 
5

The  comparably lower median  relative to mean age for both the 2017 and 
2021 surveys (median of 37 and mean of 40.5 for the 2017 survey and median of 31 
and mean of 32.9 for the 2021 survey) suggests that older respondents are possible 
outliers who are pulling the mean upwards. Indeed, both z-score and interquartile 
range (IQR) methods identified one respondent aged 95 as an  outlier in the 2017 
survey  and  four  respondents  aged  71  and  above  as  outliers  in  the  2021  survey. 
However, these observations will be kept as they may provide useful information on 
one’s financial resilience as one ages.

The income quintile shows a roughly uniform distribution in the 2017 survey, 
while  the  2021  survey  appears  to  skew  towards higher  income  quintiles  given  its

7 A 2019 Pew Research survey found that 36 percent of Filipinos aged 50 and above used the internet or owned a 
smart phone, in contrast to 74 percent of 30- to 49-year-olds and 94 percent of adults aged 18 to 29 (Schumacher 
& Kent, 2020).

Department of Economic Research   |   Discussion Paper Series No. xx

Page 11 of 28

---

<!-- PAGE 12 -->

Unpacking the Determinants of Financial Resilience in the Philippines

March 2024

median  of  4  (Tables  3a  and  3b).  This  may  likewise  relate  to  the  shift  in  interview 
mode from 2017 to 2021.8

Roughly  60  percent  of  respondents  in  both  2017  and  2021  surveys  were 
classified  as  recipients  of  secondary  education  (Tables  4a  and  4b).  2021  survey 
respondents tended to be more educated than their 2017 counterparts. While 29.1 
percent of adults in the 2017 survey were primary-educated and 11.4 percent were 
tertiary-educated, the composition reversed in the 2021 survey, where 14.5 percent 
of respondents received only primary education or less and 27.6 percent reached 
tertiary  education.  This  is  in  line  with  earlier  observations  of  the  2021  survey 
demographic tending towards the technologically inclined (i.e., younger, working, 
and higher-income).

Table 4a: Frequency Tabulation for Education Level - 2017

Education Level

Frequency

Relative 
Frequency1 
(in percent)

Cumulative 
Frequency

Primary or less 
Secondary 
Tertiary or more

285 
583 
112

29.1 
59.5 
11.4

285 
868 
980

Cumulative 
Relative 
Frequency2 
(in percent) 
29.1 
88.6 
100.0

Table 4b: Frequency Tabulation for Education Level - 2021

Education Level

Frequency

Relative 
Frequency1 
(in percent)

Cumulative 
Frequency

144 
Primary or less 
574 
Secondary 
274 
Tertiary or more 
Source: Author’s estimates based on Global Findex data 
1 Relative Frequency is the proportion of  occurrence of  a subject category within the dataset. It is 
computed by dividing the frequency of the category by the number of observations in the dataset. 
2 Cumulative Relative Frequency is the proportion of occurrence of all categories lower than or equal 
to the subject category. It is computed by summing the relative frequencies of the said categories.

14.5 
57.9 
27.6

144 
718 
992

Cumulative 
Relative 
Frequency2 
(in percent) 
14.5 
72.4 
100.0

Figure 6 shows a graphical summary of the frequency tabulations generated 
by  the  binary  variables  selected  for  the  model.  More  than  half  of  indicators  fall 
below  50  percent  (marked  by  the  blue  dashed  line),  which  highlights  the  long 
journey  that  remains  towards  financial  development.  This  also  indicates  other 
possible  rare  cases  that  may  crop  up,  as  less  than  10  percent  of  respondents 
responded positively to the bottom 4 indicators in the 2017 survey, i.e.: credit card 
ownership, mobile money account ownership, conduct of online transactions, and 
receipt of pension.

Figure 6: Profile and Financial Behavior 
2017

8 The 2019 Pew Research survey found a differential of 19 percentage points between higher and lower-income 
use of internet or smartphone ownership (Schumacher & Kent, 2020).

Department of Economic Research   |   Discussion Paper Series No. xx

Page 12 of 28

---

<!-- PAGE 13 -->

Unpacking the Determinants of Financial Resilience in the Philippines

March 2024

2021

Source: Author’s estimates based on Global Findex data

Nonetheless, several indicators registered gains from 2017 to 2021 amid the 
COVID-19  pandemic.  Mobile  phone  ownership  rose  from  75.8  percent  to 
96.3 percent.  Financial  account  ownership 
improved  from  34.3  percent  to 
56.8 percent. Mobile money account owners leapt from 4.4 percent to 30.2 percent. 
Respondents that have engaged in online purchases likewise leapt from 8.8 percent 
to  51.1  percent.  Proactive  financial  behavior  developed  as  well,  with  savers 
increasing from 59.6 percent to 64.8 percent of respondents. Saving for retirement 
also jumped from 29.0 percent to 41.7 percent despite the younger demographic 
for the 2021 survey.

These developments could, in part, be an unintended consequence of the 
pandemic. Social distancing protocols may have enticed people to shift to online

Department of Economic Research   |   Discussion Paper Series No. xx

Page 13 of 28

---

<!-- PAGE 14 -->

Unpacking the Determinants of Financial Resilience in the Philippines

March 2024

transactions, while health and income shocks may have highlighted the need for 
proactive saving behavior. However, the change in survey enumeration from 
face-to-face in 2017 to phone-based in 2021 might also have contributed to the 
changes. The data characterization exercise thus far consistently suggests higher 
technological inclination for 2021 survey respondents.

The shift to phone-based surveys may have implications on generalizability, 
as  the  2021  respondents  needed  to  have  phone  access  (though  not  necessarily 
ownership)  for  them  to  be  interviewed.  Those  without  phones,  likely  from  lower 
incomes or less educated backgrounds, would be excluded. Nonetheless, we could 
hypothesize  that  the  income  and  education  gaps  noted  in  the  2021  data  would 
widen further if those without access to mobile phones were also included in the 
sample.

Trends found in the Global Findex are generally consistent with the results of 
the  BSP  Financial  Inclusion  Survey  (FIS),  which  found  that  account  penetration 
increased from 23 percent in 2017 to 56 percent in 2021. E-money accounts likewise 
jumped from 8 percent in 2019 to 36 percent in 2021. However, adults with savings 
declined from 48 percent in 2017 to 37 percent in 2021, contrasting against the rise 
in saving behavior found in the Global Findex. Results of the latter suggested that 
savers  slightly  increased,  from  59.6  percent  in  2017  to  64.8  percent  in  2021.  The 
divergence may be due to differences in questioning, where the Findex probes into 
any  instance  of  saving  behavior  within  the  past  year  while  the  FIS  asks  about 
outstanding savings at the time of the survey.

The  predominantly  binary  nature  of  the  Global  Findex  variables  renders 
correlation (and the related Variance Inflation Factor) inappropriate in checking for 
multicollinearity. The Simple Matching Coefficient (SMC) would be a more suitable 
measure for binary attributes, as SMC calculates similarity as the proportion of exact 
matches between two variables (i.e., respondents whose attributes are both positive 
(1-1)  or  both  null  (0-0)  for  the  variables  under  comparison).  Based  on  the  SMC, 
financial  resilience  does  not  appear  to  be  strongly  connected  to  any  specific 
attribute  (Figure  7).  However,  large  SMCs  (of  at  least  0.8)  were  found  for 
combinations  of  least  frequently  occurring  characteristics  identified  in  Figure  6, 
which could be due to the high number of null (0-0) matches.

Figure 7: Similarity between Binary Variables (Using Simple Matching Coefficient)

2017

2021

Source: Author’s estimates 
V.  Empirical Methodology

Department of Economic Research   |   Discussion Paper Series No. xx

Page 14 of 28

---

<!-- PAGE 15 -->

Unpacking the Determinants of Financial Resilience in the Philippines

March 2024

Model Selection

Based  on  this  study’s  objective  of  deriving  insights  on  the  most  important 
predictors of financial resilience in Filipinos, models selected for the purpose should 
be equipped to handle classification problems and provide meaningful inferences 
on the predictive power of the attributes. On the other hand, data characterization 
in the previous section indicates that (1) overfitting should be sufficiently addressed 
given  the  presence  of  23  predictors  chosen  based  on  domain  knowledge;  (2)  the 
model  would  ideally  be  robust  to  outliers,  considering  rare  binary  cases  and  a 
relatively small percentage of  older respondents; (3) the model should be able to 
handle redundant/irrelevant variables, given the various related financial indicators 
selected  as  attributes;  and  (4)  the  model  should  be  capable  of  dealing  with 
interacting  variables,  whose  presence  is  evident  from  the  data  characterization. 
Thus, the Logistic/Logistic LASSO Regression and the Decision Tree models appear 
well-suited for this study.

Logistic and Logistic LASSO Regression

Logistic regression belongs to a set of parametric techniques widely used as 
a foundation for statistical analysis due to their interpretability and portability from 
theoretical to empirical analysis.

Logistic regression predicts the probability that a particular entity belongs to 
a specific class. It does so by generating maximum likelihood estimates based on 
the combination of characteristics that led to previous occurrences of the outcome. 
In other words, it determines likely predictors of known outcomes and assesses new 
data against this model to predict which outcome is most likely given a specific set 
of values for the predictors.

Logistic regression has also been used in similar studies analyzing financial 
inclusion. One such study uses Findex Data collected from selected Southeast Asian 
countries in 2014 to study the determinants of financial inclusion, defined as access 
to  a  financial  account  (Tjahjadi  &  Ajani,  2018).  The  research  used  individual 
characteristics  and  factors  related  to  borrowing  to  predict  the  level  of  inclusion 
across different income levels and countries.

In  this  study,  logistic  regression  was  chosen  because  it  deals  well  with 
irrelevant, redundant, and interacting variables. However, the technique tends to be 
sensitive  to outliers.  Hence,  issues may  arise  around  the  robustness  of  the  results 
amidst  the  presence  of  rare  cases  in  the  age  variable  as  well  as  some  financial 
indicators.

Since it seeks the combination of predictors that will best fit existing  data, 
logistic  regression  models  tend  to  overfit  as  the  parameters  increase.  To  aid  in 
model generation, LASSO can be used as a shrinkage method to zero out irrelevant 
coefficient estimates. LASSO can filter factors of financial resilience that provide the 
highest  predictive  value.  Performing  LASSO  requires  standardized  features  to 
eliminate issues with scaling that may cause larger-ranged variables such as age to 
dominate the regression model.

Decision Tree

Department of Economic Research   |   Discussion Paper Series No. xx

Page 15 of 28

---

<!-- PAGE 16 -->

Unpacking the Determinants of Financial Resilience in the Philippines

March 2024

Decision  tree  is  a  non-parametric  technique  that  splits  known  cases  into 
groupings  that  would  maximize  homogeneity.  New  data  will  then  be  classified 
based  on  rules  generated  from  the  splits.  Decision  tree  is  widely  used  for  its 
straightforward interpretability and accessibility to the non-technical audience. The 
method is likewise robust to irrelevant variables and outliers, which is important in 
this study given the relatively large number of parameters and the rare cases noted 
during data characterization.

Decision  tree  has  likewise  been  used  to  determine  key  factors  in  financial 
inclusion.  Aiming  to  segment  Indian  survey  respondents  into  the  financially 
excluded and included, Tiwari et al. (2019) generated classes based on a composite 
measure  of  financial  inclusion  (composed  of  bank  account  ownership,  access  to 
loan requirements, insurance coverage, and access to digital banking). The authors 
generated a decision tree that classified individuals as included or excluded based 
on demographic, social, and economic variables.

Like  logistic  regression,  decision  tree  may  be  prone  to  overfitting  as  the 
number of parameters increases. Too many variables may cause the decision tree 
to  accidentally  overstate  the  importance  of  irrelevant  variables.  Nonetheless,  this 
should not preclude the use of the algorithm. Various methods can address model 
overfitting, such as limiting tree size or pruning to penalize larger trees.

VI. Results and Discussion

Predictive Models of Financial Resilience

Model performance is evaluated against the baseline financial resilience rate 
(49.4 percent  in  the 2017  survey  and  59.0  percent  in  the  2021 survey).  This  means 
that if a model were to tag all respondents as financially resilient, it will obtain an 
accuracy of 49.4 percent on 2017 data and 59.0 percent on 2021 data. Similarly, if all 
respondents  are  labeled  as  financially  vulnerable,  the  accuracy  will  stand  at  50.6 
percent on 2017 data and 41.0 percent on 2021 data.

For model building, this study runs different logistic regression and decision 
tree  models  based  on  selected  hyper-parameters.  Hyper-parameter  values 
maximizing  test  set  accuracy  were  chosen.  The  chosen  models  were  then  run 
against  the  same  set  of  training  and  test  data,  split  at  25 percent  to  allow  the 
models  to  train  on  a  substantial  training  set  (more  than  700 observations)  while 
keeping a sizeable test set (almost 250 observations).

Tables 5a and 5b compare the accuracy scores of the different models on the 
test data. The accuracy scores hovered in the 59-65 percent range for 2017 data and 
62-68  percent  for  2021  data.  To  the  author’s  knowledge,  the  closest  study  on 
financial  resilience  that  similarly  gauges  model  accuracy  is  that  of  Hussain  et  al. 
(2019),  which  estimates  that  its  logistic model  can  correctly  identify  the  financial 
resilience  of  76  percent  of  individuals,  based  on  2014  Global  Findex  data  in 
Bangladesh.

Table 5a: Accuracy Scores across Different Models – 2017

Classifier

Hyper-parameter1

Accuracy Score 
(in percent)

Department of Economic Research   |   Discussion Paper Series No. xx

Page 16 of 28

---

<!-- PAGE 17 -->

Unpacking the Determinants of Financial Resilience in the Philippines

March 2024

Logistic Regression

Decision Tree

Random Forest2

none 
LASSO (L1 penalty) with C = 0.21 
Maximum Tree Depth = 2 
Minimum Samples per Leaf = 39 
Cost Complexity Pruning Alpha = 0.015 
Minimum Samples per Split = 151 
Grid-Search Optimized Parameters 
Maximum Tree Depth = 3; Estimators = 1,500

60.0 
61.2 
61.2 
63.7 
61.2 
64.1 
59.2 
65.3

Table 5b: Accuracy Scores across Different Models – 2021

Classifier

Logistic Regression

Decision Tree

Hyper-parameter1

Accuracy Score 
(in percent) 
66.5 
none 
66.5 
LASSO (L1 penalty) with C = 0.1 
65.3 
Maximum Tree Depth = 4 
66.9 
Minimum Samples per Leaf = 52 
65.3 
Cost Complexity Pruning Alpha = 0.015 
68.1 
Minimum Samples per Split = 99 
Alpha = 0.001; Minimum Samples per Leaf = 60  66.9 
none

Linear Discriminant 
Analysis3 
Source: Author’s estimates 
Table 5 Notes: 
1  Except  for  Logistic  Regression,  models  were  iterated  across  a  range  of  hyper-parameter  values.  Final  hyper-

66.9

parameter values were those that yielded the best mean test set accuracy scores.

2 Random Forest generates predictions based on an ensemble of Decision Trees trained on different subsets of the

data and variables.

3 Linear Discriminant Analysis classifies data based on linear combinations of variables that minimize within-group

separation and maximize between-group separation.

Since  both  decision  tree  and  logistic  regression  models  may  sacrifice 
accuracy  for  interpretability,  a  benchmark  model  was  introduced  to  determine 
whether  higher  predictive  accuracy  could  be  achieved.  Random  Forest  (with  a 
maximum tree depth of 3 and 1,500 estimators) emerged with the best predictive 
score on 2017 data and Linear Discriminant Analysis on 2021 data. Nonetheless, both 
models  still  resulted  in  test  accuracy  scores  below  70  percent  (Table  5).  Other 
models  considered  include  Naïve  Bayes,  Linear  Discriminant  Analysis,  K-Nearest 
Neighbors, Neural Networks, Random Forest, and Support Vector Machines9.

The  Receiver  Operating  Characteristic  (ROC)  curve  in  Figure  8  provides  a 
graphical  comparison  of  the  models’  predictive  performances.  All  models  follow 
roughly the same path – all better than 50 percent chance but far from the ideal 
where the curve hugs the top left corner of the axis (signifying the ability to achieve 
high true positive rates while keeping false positive rates low). The Random Forest 
tends to produce better results for 2017 data while Linear Discriminant Analysis and 
Logistic (LASSO) Regression tend to perform better for 2021 data.

Figure 8: Receiver Operating Characteristic (ROC) Curve

2017

2021

9 Accuracy scores for the other models are as follows:

•

•

For 2017 survey data, Linear Discriminant Analysis: 60.0 percent, K Nearest Neighbors: 62.9 percent, 
Support Vector Machine: 60.0 percent, Naïve Bayes: 62.0 percent, Neural Network: 63.7 percent 
For 2021 survey data, K Nearest Neighbors: 65.7 percent, Random Forest: 64.1 percent, Support Vector 
Machine: 65.7 percent, Naïve Bayes: 65.3 percent, Neural Network: 64.9 percent

Department of Economic Research   |   Discussion Paper Series No. xx

Page 17 of 28

---

<!-- PAGE 18 -->

Unpacking the Determinants of Financial Resilience in the Philippines

March 2024

Source: Global Findex, Author’s estimates

While  accuracy  is  important  in  distinguishing  the  financially  resilient  from 
the  financially  vulnerable  (which  would  thereby  facilitate  the  proper  targeting  of 
interventions),  it  is  more  important  to  dissect  the  components  of  these  accuracy 
measures  and  assess  the  nature  of  the  models’  misclassifications.  The  models’ 
confusion  matrices  highlight  the  trade-off  between  sensitivity  (ability  to  identify 
true positives) and specificity (ability to identify true negatives) (Figure 9). For 2017 
data, the Decision Tree model with at least 151 samples per split yielded the highest 
number  of  true  negatives  and  fewest  false  positives  (where  “positive”  means 
financially  resilient  and  “negative”  means  otherwise).  For  2021  data,  the  same  is 
exhibited by the Decision Tree model with cost complexity alpha of 0.015.

Figure 9: Confusion Matrix Values across Models 
2017

2021

Department of Economic Research   |   Discussion Paper Series No. xx

Page 18 of 28

---

<!-- PAGE 19 -->

Unpacking the Determinants of Financial Resilience in the Philippines

March 2024

Source: Author’s estimates

Taken together, the model performance metrics considered thus far indicate 
that the best overall model for the 2017 data would be the Decision Tree model with 
at  least  151  samples  per  split  as  it  achieved  the  highest  accuracy  score  while 
maximizing true negatives and minimizing false positives. The ROC curve likewise 
showed  that,  except  at  very  low  positive  rates,  the  same  Decision  Tree  model 
generally  performed  at  par  with  the  Random  Forest,  which  registered  the  best 
performance in this measure. On the other hand, for 2021 data, considered model 
metrics suggest that the best overall model would be the Decision Tree model with 
at least 99 samples per split. It topped accuracy at 68.1 percent and performed well 
at higher positive rates in the ROC curve. It also identified the highest number of 
true positives out of the models tested, but fewer true negatives than the Decision 
Tree model with cost complexity alpha of 0.015.

Nonetheless,  with  the  intention  is  to  cover  as  many  of  the  financially 
vulnerable as possible, the models chosen to generate inferences in the next section 
were those that identified the highest number of true negatives and lowest false 
positives, i.e.: for 2017, the Decision Tree with at  least 151 samples per split (which 
incidentally is also the best overall model) and for 2021, the Decision Tree with cost 
complexity alpha of 0.015. It may be worth noting that the tradeoff for choosing a 
model with a higher number of false negatives would be that interventions would 
also  reach  a  considerable  number  of  individuals  who  may  already  be  financially 
resilient.

Inferences on the Determinants of Financial Resilience

Logistic  LASSO  regressions  for  both  the  2017  and  2021  survey  rounds 
consistently  suggest  that  financial  resilience  possesses  a  strong,  positive 
relationship with income quintile; a moderate, positive relationship with saving for 
retirement;  and  a  moderate,  negative  relationship  with  being  female  (Figure  10). 
The  magnitude  of  the  regression  coefficient  for  income  quintile  noticeably  rose 
from 2017 to 2021. Conversely, the magnitude for saving for retirement decreased

Department of Economic Research   |   Discussion Paper Series No. xx

Page 19 of 28

---

<!-- PAGE 20 -->

Unpacking the Determinants of Financial Resilience in the Philippines

March 2024

and  for  gender  (female),  increased  slightly.  Moreover,  tertiary  education  jumped 
from  assuming  a  minimal  regression  coefficient  in  2017  to  being  second  only  to 
income  quintile  in  2021.  The  widening  financial  resilience  gap  between  income 
classes,  genders,  and  educational  attainment,  coupled  with  the  weakened  link 
between  financial  resilience  and  saving  behavior,  supports  concerns  that  the 
COVID-19 pandemic would likely deepen inequalities (Jurzyk et al., 2020).

Figure 10: Logistic Regression and Logistic LASSO Regression Coefficients 
2017

2021

Source: Author’s estimates

The LASSO regression found that age was strongly negatively associated with 
financial resilience in 2017 but turned uninformative in 2021. In contrast, the model 
found borrowing for medical purposes uninformative in 2017 but noted a stronger 
negative  association  with  financial  resilience  in  2021,  second  only  to  gender  (i.e.,

Department of Economic Research   |   Discussion Paper Series No. xx

Page 20 of 28

---

<!-- PAGE 21 -->

Unpacking the Determinants of Financial Resilience in the Philippines

March 2024

being  female).  The  change  in  predictive  value  for  age  might  be  linked  with  the 
earlier  result  where  respondents  in  the  2017  survey  aged  below  40  tended  to  be 
more financially resilient than older age groups, especially those in retirement age 
(70 and above). On the other hand, there were no discernible differences between 
age groups in the 2021 survey. The negative association found for medical-related 
borrowing  in  the  2021  survey  could  be  linked  with  findings  of  the  COVID-19 
Household  Survey  that  the  World  Bank  conducted  in  December 2020,  where  62 
percent  of  households  cited  lack  of  money  as  a  reason  for  inability  to  access 
treatment (Piza et al., 2021).

While online payments was one of the top predictors in the 2017 survey, its 
association  with  financial  resilience  decreased  in  2021.  This  may  be  due  to  the 
adjustments brought about by physical lockdowns during the COVID-19 pandemic, 
as  transacting  online  became  widespread.  The  Global  Findex  survey  found  that 
Filipinos who conducted online payments sharply increased from 9 percent in 2017 
to  51  percent  in  2021.  That  the  pandemic  transformed  online  transactions  into  a 
norm rather than an exception may have led to the financial indicator’s weakened 
ability to distinguish between the resilient and vulnerable (perhaps as a proxy for 
financial literacy).

The positive association between financial resilience and sending domestic 
remittances also noticeably decreased from 2017 to 2021. Like online payments, the 
Global  Findex  found  that  more  Filipinos  sent  domestic  remittances  during  the 
pandemic, from 25 percent in 2017 to 39 percent in 2021. While the reason for the 
remittances is unknown, its positive link with financial resilience may be traced to 
social  capital,  one  of the  components  of  Salignac  et  al.  (2019)’s Multidimensional 
Financial  Resilience  Framework.  As  financial  hardships  mounted  during  the 
pandemic, it would be reasonable to hypothesize that families and friends would 
provide financial support to loved ones in need, at the expense of their own financial 
security.  Notably,  the  association  between  financial  resilience  and  receiving 
domestic remittances remained minimal and positive from 2017 to 2021.

Figure  11  displays  the  decision  trees  with  the  highest  true  negative  rates. 
Consistent  with  the  results  of  the  logistic  LASSO  regression,  income  quintile 
remained  the  most  important  predictor.  For  the  2017  survey  round,  this  was 
followed  by  savings  –  whether  for  retirement  (for  respondents  belonging  to  the 
richest 40 percent in terms of household income quintile) or regardless of purpose 
(for  the  poorest  60 percent).  On  the  other  hand,  saving  behavior  did  not  figure 
prominently in the 2021 survey round. Instead, the results suggest three groups of 
respondents exhibiting varying levels of financial resilience: first (and most likely to 
be resilient) are the more affluent (i.e., among the richest 40 percent) who were also 
tertiary-educated;  second  are  the  rest  of  the  more  affluent  who  did  not  receive 
tertiary  education;  and  third  (and  least  likely  to  be  resilient)  are  respondents 
belonging  to  the  poorest  60  percent  of  the  population.  Nonetheless,  it  must  be 
noted  that  Gini  scores  remain  high  across  most  nodes,  with  a  notable  exception 
being tertiary-educated, higher-income respondents for the 2021 survey (who were 
mostly financially resilient). Respondents must be segregated further, and a larger 
sample  might  be  needed  to  identify  more  accurately  who  are  the  financially 
resilient vis-à-vis those who are not.

Figure 11: Decision Trees with Highest True Negative Rates 
2017 (Minimum Samples per Split = 151)

Department of Economic Research   |   Discussion Paper Series No. xx

Page 21 of 28

---

<!-- PAGE 22 -->

Unpacking the Determinants of Financial Resilience in the Philippines

March 2024

2021 (Cost-Complexity Pruning Alpha = 0.015)

Source: Author’s estimates

In  terms  of  feature  importance  for  the  decision  tree  and  random  forest 
models (Figure 12), the results are similar to the Decision Trees chosen in Figure 11. 
Income quintile was the top predictor in both the 2017 and 2021 surveys. In 2017, 
both forms of saving behavior (i.e., saving for any purpose and saving for retirement) 
also  ranked  high  in  feature  importance.  Other  noteworthy  factors  that  figured 
prominently in 2017 are online purchases, debit card ownership, and age. In 2021, 
the  most  predictive  factors  were  tertiary  education,  saving  per  se,  borrowing  for 
medical reasons, and gender.

Department of Economic Research   |   Discussion Paper Series No. xx

Page 22 of 28

---

<!-- PAGE 23 -->

Unpacking the Determinants of Financial Resilience in the Philippines

March 2024

Figure 12: Feature Importance across Decision Tree and Random Forest Models 
2017

2021

Source: Author’s estimates

Department of Economic Research   |   Discussion Paper Series No. xx

Page 23 of 28

---

<!-- PAGE 24 -->

Unpacking the Determinants of Financial Resilience in the Philippines

March 2024

VII. Conclusions and Policy Implications

This paper explores the determinants of Filipinos’ financial resilience through 
the construction of predictive models and from there, the generation of inferences 
on the most important predictors of financial resilience. Using World Bank Global 
Findex  data  for  the  Philippines  in  2017  and  2021,  empirical  results  consistently 
identify  income  quintile,  saving  behavior,  and  gender  as  the  top  predictors  for 
financial  resilience  for  both  years.  Additionally,  age,  saving  for  retirement,  and 
online  payments  were  important  features  for  2017,  while  tertiary  education  and 
medical  borrowing  were  important  for  2021.  These  findings  indicate  that 
demographics remains the largest determinant for financial resilience. The results 
also seem to suggest that financial inclusion, i.e., access to and usage of financial 
products, does not necessarily translate to resilience.

Income  level  and  gender  consistently  emerged  as  the  most  important 
variables  in  the  models.  Results  of  the  2021  survey  round  likewise  showed  that 
tertiary  education  is  second  only  to  income  quintile  in  predicting  financial 
resilience. The significance of income, gender, and education to financial resilience 
is  consistent  with  literature.  Debuque-Gonzales  and  Corpus  (2021)  point  out  that 
lower-income and less-educated Filipinos may experience “involuntarily exclusion” 
from the formal financial system. In this regard, policymakers may consider crafting 
programs targeted towards improving employment and educational opportunities 
for  those  in  the  lower  socioeconomic  classes.  Additional  safety  nets  may  also  be 
considered  for  females,  who,  despite  their  higher  participation  in  the  formal 
financial  system,  still  lag  behind  males  in  terms  of  financial  resilience,  with  the 
divide even widening from 2017 to 2021.10 A similar gender gap is apparent in the 
labor market, where female labor force participation remains one of the lowest in 
the  region  (Buchhave  &  Belghith,  2022).  Initiatives  empowering  women  to  gain 
access to higher quality jobs and encouraging entry into the workforce could thus 
help close the financial resilience gap.

The  Philippine  government  has  implemented  a  conditional  cash  transfer 
(CCT)  program  which benefits around  20 percent of the population (World Bank, 
2017).  The  decision  tree  model’s  choice  to  split  after  the  3rd  income  quintile  may 
indicate  that  it  is  not  just  the  poorest  of  the  poor  who  face  increased  financial 
vulnerability.  This  result  warrants  a  reassessment  of  social  safety  nets  that  have 
traditionally  focused  on  the  poorest  20  percent.  Broadening  social  protection 
measures  provided  to  the  poorest  60  percent  may  not  necessarily  involve 
expanding CCT coverage or providing direct transfers but may come in other forms 
of  assistance  such  as  insurance  mechanisms  and  micro-credit  opportunities  that 
may  help  the  entrepreneurial  poor  to  tap  into  additional  funding  sources  that 
would  allow  them  to  earn  income  and  become  self-sufficient.  As  the  2018 
Consumer Finance Survey (CFS) finds, only a small segment of Filipino households 
(5.1 percent) are engaged in entrepreneurial activities.

Saving behavior was likewise a key predictor in most of the models. Notably, 
the decision tree identified different forms of savings as important for the different 
socioeconomic  classes.  For  those  with  lower  income  levels,  the  act  of  saving,  in 
whatever form or for whatever purpose, mattered the most. However, for those with 
higher income levels, saving for one’s retirement mattered the most.

10 Females are more likely and may even be more determined to become financially included (Debuque-Gonzales 
and Corpus, 2021).

Department of Economic Research   |   Discussion Paper Series No. xx

Page 24 of 28

---

<!-- PAGE 25 -->

Unpacking the Determinants of Financial Resilience in the Philippines

March 2024

The importance for poorer households of having the ability to save, coupled 
with the emergence of  a sizeable association between financial vulnerability and 
borrowing  for  medical  purposes,  highlight  the  need  for  enhanced  insurance 
mechanisms against economic shocks such as disasters and medical emergencies. 
For  instance,  for  lower-income  farmers  whose  earnings  may  be  sensitive  to 
weather-related disruptions, the government may consider setting up agricultural 
insurance programs. Healthcare coverage may also be reassessed to determine the 
extent  of  out-of-pocket  payments  required  from  poorer  beneficiaries.  Improved 
public  health  services  would  likewise  improve  the  quality  of  life  of  poor  families, 
protecting 
losses  and  health 
expenditures. Further, the government should enhance pandemic preparedness, as 
poor  epidemiological  response  undermines  not  only  public  health  but  also  the 
financial resilience of the lower income population.

them  against  morbidity-induced

income

For higher-income individuals, saving for the future may matter more than 
saving for other purposes (e.g., for business or for a major purchase). Since even the 
more  affluent  can  experience  financial  vulnerability,  expanding  financial  literacy 
programs can be beneficial in instilling the value of financial discipline and saving 
into the broader populace. Both the CFS report and Debuque-Gonzales and Corpus 
(2021)  study  similarly  advocate  for  financial  education.  The  2018  CFS  also  raised 
concerns  that  Filipino  households  appeared  to  prioritize  consumption  and 
purchase  of  non-financial  assets  over  savings  and  investment.  More  than  half  of 
Filipino  households  were  found  to  be over-indebted  and  experienced  challenges 
meeting monthly obligations.

Modest model accuracy coupled with other limitations of the dataset, such 
as the narrow proxy measure for financial resilience used in the Findex survey, may 
weigh on the validity of the findings. The consistent below-70 percent accuracy of 
the  various  models  highlights  the  need  for  more  granular  survey  data,  as  several 
factors remain unmeasured by the current dataset. A more adequate assessment of 
financial resilience may emanate from the introduction of additional demographic 
variables  relating  to  home  ownership,  employment  status,  industry,  as  well  as 
information  across  other  dimensions  of  financial  resilience  (such  as  savings  level, 
debt  management  ability,  access  to  credit,  access  to  insurance,  credit  demand, 
insurance  demand,  financial  knowledge,  financial  behavior,  and  access  to  social 
support).

Findings  from  this  study  may  allow  policymakers  to  assess  priority  areas 
requiring  intervention.  However,  a  definitive  understanding  of  the  financially 
vulnerable and  the appropriate interventions would require the conduct of more 
focused  studies.  As  such,  future  research  may  consider  investigating  causal  links 
between financial resilience and the variables with high predictive value that were 
identified in this study.

Department of Economic Research   |   Discussion Paper Series No. xx

Page 25 of 28

---

<!-- PAGE 26 -->

Unpacking the Determinants of Financial Resilience in the Philippines

March 2024

References

Bangko Sentral ng Pilipinas. (2018, February). The Credit Surety Fund: Concept and

Creation. Retrieved March 10, 2021, from 
https://www.bsp.gov.ph/Media_and_Research/Primers Faqs/CSF.pdf

Bangko Sentral ng Pilipinas. (2021, October). 2018 Consumer Finance Survey [PDF file].

Retrieved October 6, 2023, from 
https://www.bsp.gov.ph/Media_And_Research/Consumer%20Finance%20Survey/C
FS_2018.pdf

Bangko Sentral ng Pilipinas. (2018, July). 2017 Financial Inclusion Survey [PDF file].

Retrieved October 6, 2023, from 
https://www.bsp.gov.ph/Inclusive%20Finance/Financial%20Inclusion%20Reports%
20and%20Publications/2017/2017FISToplineReport.pdf

Bangko Sentral ng Pilipinas. (2022, August). 2021 Financial Inclusion Survey [PDF file].

Retrieved October 6, 2023, from 
https://www.bsp.gov.ph/Inclusive%20Finance/Financial%20Inclusion%20Reports%
20and%20Publications/2021/2021FISToplineReport.pdf

Buchhave, H. & Belghith, N.B.H. (2022, April 11). Overcoming barriers to women’s work in

the Philippines. Retrieved November 7, 2023, from 
https://blogs.worldbank.org/eastasiapacific/overcoming-barriers-womens-work-
philippines

Clark, R. L. & Mitchell, O. S. (2022). Americans’ financial resilience during the pandemic.

Financial Planning Review, 5(2–3). doi:10.1002/cfp2.1140

Debuque-Gonzales, M. & Corpus, J.P. (2021). Understanding and measuring financial

inclusion in the Philippines. Philippine Institute for Development Studies (PIDS) 
Discussion Paper Series, No. 2021-37. Retrieved June 20, 2023 from 
http://hdl.handle.net/10419/256872

Demirgüç-Kunt, A., Klapper, L., Singer, D., Ansar, S., & Hess, J. (2018). The Global Findex

Database 2017: Measuring Financial Inclusion and the Fintech Revolution. 
Washington, DC: World Bank. Ref: PHL_2017_FINDEX_v02_M. Accessed at 
https://microdata.worldbank.org/index.php/catalog/3311 on 11 July 2023.

Demirgüç-Kunt, A., Klapper, L., Singer, D., & Ansar, S. (2022). The Global Findex Database

2021: Financial inclusion, Digital Payments, and Resilience in the Age of COVID-19. 
Washington, DC: World Bank. doi:10.1596/978-1-4648-1897-4

Economic Policy Research Institute. (2020, December 10). The Impact of the COVID-19

Crisis on Households in the National Capital Region of the Philippines (Rep.). 
Retrieved March 10, 2021, from UNDP and UNICEF Philippines website: 
https://www.unicef.org/philippines/media/2061/file/Final report: The Impact of the 
COVID-19 Crisis on Households in the National Capital Region of the Philippines.pdf

Fernandez-Lopez, S., Alvarez-Espiño, M., Castro-Gonzalez, S., & Rey-Ares, L. (2023). Financial 
capability and households’ financial vulnerability: evidence for the Spanish 
case. Managerial Finance, 49(4), 679-702. doi:10.1108/MF-02-2022-0086

Financial Inclusion Steering Committee. (2023). 2022 Annual Report of the National

Strategy for Financial Inclusion 2022-2028. Retrieved September 29, 2023, from BSP 
website: 
https://www.bsp.gov.ph/Pages/InclusiveFinance/2022NSFIAnnualReport.pdf

Hussain, A. B., Endut, N., Das, S., Chowdhury, M. T., Haque, N., Sultana, S., & Ahmed, K. J.

(2019). Does financial inclusion increase financial resilience? Evidence from

Department of Economic Research   |   Discussion Paper Series No. xx

Page 26 of 28

---

<!-- PAGE 27 -->

Unpacking the Determinants of Financial Resilience in the Philippines

March 2024

Bangladesh. Development in Practice, 29(6), 798-807. 
doi:10.1080/09614524.2019.1607256

Jurzyk, E., Nair, M. M., Pouokam, N., Sedik, T. S., Tan, A., & Yakadina, I. (2020). COVID-19 and

Inequality in Asia. IMF Working Papers, 20(217). doi:10.5089/9781513559179.001

Kempis, M. & Morduch, J. (2020, May 21). How resilient are we? A dive into the global data 
on how people deal with unexpected shocks. Retrieved July 7, 2023, from 
https://www.financialaccess.org/blog/2020/5/21/how-resilient-are-we-a-dive-into-
the-global-data-on-how-people-deal-with-unexpected-shocks

Klapper, L. & Lusardi, A. (2019). Financial literacy and financial resilience: Evidence from

around the world. Financial Management, 49(3), 589–614. doi:10.1111/fima.12283

Klapper, L. & Morduch, J. (2023, January 18). For a strong economic recovery, invest in

financial resilience. Retrieved June 29, 2023, from 
https://www.weforum.org/agenda/2023/01/economic-recovery-financial-resilience-
world-bank-wef23/

Klapper, L. & Tayag, P. R. (2022, November 02). Responsible finance and its role in

improving financial resilience and well-being. Retrieved July 27, 2023, from 
https://blogs.worldbank.org/developmenttalk/responsible-finance-and-its-role-
improving-financial-resilience-and-well-being

O'Neill, A. (2021, April 01). Philippines: Average age of the population from 1950 to 2020. 
Retrieved April 19, 2021, from https://www.statista.com/statistics/578796/average-
age-of-the-population-in-philippines/

Oxford Business Group. (2020, December 16). The Report: Philippines 2021. Retrieved 
September 28, 2023, from https://oxfordbusinessgroup.com/philippines-
2021/economy

Piza, S. F. A., Cho, Y., & Zapanta, A. M. F. S. (2021). Philippines COVID-19 High Frequency 
Household Survey Round 2 (December 2020) Summary of Findings. Retrieved 
August 11, 2023, from 
https://thedocs.worldbank.org/en/doc/ab24c2a718fb53a344c5942d236b2fe6-
0070062021/philippines-covid-19-high-frequency-household-survey-round-2-
december-2020-summary-of-findings

Sahay, R., & Cihak, M. (2018). Women in Finance: A Case for Closing Gaps. Staff Discussion

Notes, 18(05), 1. doi:10.5089/9781484375907.006

Salignac, F., Marjolin, A., Reeve, R., & Muir, K. (2019). Conceptualizing and Measuring

Financial Resilience: A Multidimensional Framework. Social Indicators 
Research, 145(1), 17-38. doi:10.1007/s11205-019-02100-4

Schumacher, S. & Kent, N. (2020). 8 charts on internet use around the world as countries

grapple with COVID-19. Retrieved August 7, 2023, from 
https://www.pewresearch.org/short-reads/2020/04/02/8-charts-on-internet-use-
around-the-world-as-countries-grapple-with-covid-19/

Tiwari, T., Srivastava, A., & Kumar, S. (2019). Decision Tree: Categorizing Financial

Inclusion. International Journal of Recent Technology and Engineering Regular 
Issue, 8(4), 10431-10435. doi:10.35940/ijrte.d8979.118419

Tjahjadi, A. M., & Ajani, J. (2018). Assessing Financial Inclusion in ASEAN Countries: Are We

Done Yet? [Paper presentation].  ASEAN Youth Conference, Malaysia. 
https://www.researchgate.net/publication/331728531_Assessing_Financial_Inclusion
_in_ASEAN_Countries_Are_We_Done_Yet

Department of Economic Research   |   Discussion Paper Series No. xx

Page 27 of 28

---

<!-- PAGE 28 -->

Unpacking the Determinants of Financial Resilience in the Philippines

March 2024

World Bank. (2017, July 10). FAQs about the Pantawid Pamilyang Pilipino Program (4Ps).

Retrieved May 14, 2021, from 
https://www.worldbank.org/en/country/philippines/brief/faqs-about-the-pantawid-
pamilyang-pilipino-program

World Bank. (2018, October 23). Global Financial Inclusion (Global Findex) Database 2017.

Retrieved July 11, 2023, from 
https://microdata.worldbank.org/index.php/catalog/3311

World Bank. (2020). Philippines Economic Update December 2020 Edition (Publication).

Retrieved March 10, 2021, from World Bank website: 
https://openknowledge.worldbank.org/bitstream/handle/10986/34899/Philippines-
Economic-Update-Building-a-Resilient-Recovery.pdf

World Bank. (2022, October 13). Global Financial Inclusion (Global Findex) Database 20121.

Retrieved July 11, 2023, from 
https://microdata.worldbank.org/index.php/catalog/4607

World Bank. (2022). Overcoming poverty and inequality in the Philippines: Past, present,

and prospects for the future (Publication). Retrieved September 28, 2023, from 
World Bank website: 
https://openknowledge.worldbank.org/bitstream/handle/10986/38346/P17486101e2
9310810abaf0e8e336aed85a.pdf

Department of Economic Research   |   Discussion Paper Series No. xx

Page 28 of 28

<!-- MARKITDOWN CONVERSION -->

<!-- Full MarkItDown conversion for formatting fidelity. -->

2024
R
E
P
Unpacking the Determinants of
A
Financial Resilience in the Philippines
P
Mary Kryslette C. Bunyi
N
O
I
S
S
U
C
S
I
D
P
S
B
Series
BANGKO SENTRAL NG PILIPINAS
No.03
Classification: GENERAL

Unpacking the Determinants of Financial Resilience in the Philippines March 2024
Unpacking the Determinants of Financial Resilience in the Philippines
Mary Kryslette C. Bunyi1
This version: February 2024
ABSTRACT
The COVID-19 pandemic exposed financial vulnerabilities as it subjected
households to health shocks and income losses. With inequalities likely to deepen,
policymakers may benefit from asking: What would make Filipinos financially
resilient? This paper examines financial resilience in the Philippines by
demographic profile and employs Logistic LASSO Regression, Decision Tree, and
other machine learning models to create predictive models and generate
inferences on determinants of financial resilience using data from the World Bank
Global Financial Inclusion (Findex) surveys for 2017 and 2021. Variables were chosen
based on the components of Salignac et al. (2019)’s Multidimensional Financial
Resilience Framework. Empirical findings were consistent across models and
suggest that demographics may provide higher predictive value for financial
resilience than financial access. Income quintile, saving behavior, and gender
emerged as the top predictors in both the 2017 and 2021 survey rounds. Age, saving
for retirement, and online payments were also identified as important features for
2017, and tertiary education and medical borrowing for 2021. Insights from this
study could provide policymakers with baseline information on financial resilience
in the Philippines and support interventions to identify and empower the financially
vulnerable towards financial security.
JEL classification : D12, D14, G51, I30
Key words : financial resilience, financial vulnerability,
financial inclusion, machine learning
Corresponding author : BunyiMC@bsp.gov.ph
Disclaimer: The views expressed in this discussion paper are solely the author’s and do not
represent the official position of the Bangko Sentral ng Pilipinas.
1 Mary Kryslette C. Bunyi is Bank Economist IV at the Department of Economic Research.
Department of Economic Research | Discussion Paper Series No. xx Page 2 of 28

Unpacking the Determinants of Financial Resilience in the Philippines March 2024
I. Introduction
Posting an average economic growth of 6.4 percent (at constant 2018 prices)
from 2010 to 2019, the Philippines has benefited from one of the fastest economic
growth rates in the world. However, deeply entrenched inequality2 persists as a
conundrum to policymakers who seek to make growth more inclusive for all
Filipinos (Oxford Business Group, 2020).
A World Bank (2020) survey on the impact of COVID-19 found that income
losses affected 40 percent of households, especially non-farm entrepreneurs. The
study further notes that “the poor and vulnerable, many of whom work in the
informal sector, are especially likely to experience significant welfare losses, given
their limited capacity to manage risks” (World Bank, 2020, p. 44). Inequalities are
also likely to deepen in the aftermath of the COVID-19 pandemic, as pandemics
have historically done (Jurzyk et al., 2020).
To increase financial safety nets for the vulnerable sector, the Philippine
government has implemented various interventions even before the pandemic
such as agricultural insurance subsidies (World Bank, 2020); Credit Surety Fund for
micro, small, and medium enterprises (Bangko Sentral ng Pilipinas, 2018); and
Emergency Cash Transfer (ECT) for targeted financial assistance to the poorest
households (World Bank, 2020). Nonetheless, there have been recommendations to
“assess [the] targeting of social protection programs” (Economic Policy Research
Institute, 2020, p. 24) given the disparities observed between the recipients of
financial assistance from different government units.
Financial inclusion, while an important contributor to financial resilience, is
not sufficient to guarantee the latter. Financial inclusion refers to the accessibility,
usage, and quality of financial products and services (Bangko Sentral ng Pilipinas,
2022). On the other hand, financial resilience is concerned with the ability to deal
with financial shocks (Demirgüç-Kunt et al., 2022). The link between financial
inclusion and financial resilience is highlighted in the Philippines’ National Strategy
for Financial Inclusion 2022-2028, whose overarching vision is to steer “financial
inclusion toward inclusive growth and financial resilience” (Financial Inclusion
Steering Committee, 2023).
Country-level data from the 2017 World Bank Global Financial Inclusion
(Global Findex) Survey3 showed that while individuals in countries with high
financial access do tend to report high financial resilience, it is also possible to
exhibit high access but remain low in resilience. For instance, South Africa reported
69.2 percent financial account ownership but only 28.7 percent financial resilience.
The converse also holds – Vietnam was found to be low in financial access (30.8
percent account ownership) but high in financial resilience (70.0 percent).
Similarly, while the Global Findex 2021 survey finds 71 percent financial
account ownership in developing economies, financial resilience in these areas
stand at 55 percent (Klapper & Tayag, 2022). Half of respondents in developing
2 The country’s income Gini ratio was measured at 0.45 in 1985, peaked at 0.49 in 1997, and has since gradually
declined to 0.41 in 2021 (based on Philippine Statistics Authority (PSA) estimates as extracted from CEIC). The
World Bank notes that the Philippines has one of the highest rates of income inequality in East Asia, second only
to Thailand for countries with available data as of 2018 (World Bank, 2022b).
3 Readers may refer to Section 3 (Data) for a broad description of the World Bank Global Findex Survey.
Department of Economic Research | Discussion Paper Series No. xx Page 3 of 28

Unpacking the Determinants of Financial Resilience in the Philippines March 2024
economies were “very worried” about expenses that could arise from medical-
related shocks such as illnesses and accidents (Demirgüç-Kunt et al., 2022).
As an emerging economy, the Philippine government must contend with
limited capacity and resources. Policies should be crafted to provide the greatest
assistance to those in greatest need. Empowering the vulnerable to achieve
financial resilience is key to lifting them out of poverty and helping them stay out
of it. Determining the most important environmental factors that build financial
resilience and establishing the characteristics of the financially vulnerable would
aid in designing better targeted interventions to curb their financial insecurity and
help them achieve upward economic mobility.
This paper contributes to the literature by investigating the research
question: What makes Filipinos financially resilient? Using 2017 and 2021 survey data
from the World Bank Global Financial Inclusion (Findex) Database, this paper
employed Logistic LASSO Regression, Decision Tree, and machine learning models
to generate predictions and produce inferences on the most important predictors
of financial resilience. This paper also contextualizes empirical results against
existing financial inclusion literature, which could offer policymakers insights into
the dynamics between demographics, financial inclusion, and financial resilience
in the Philippines.
The rest of this paper is organized as follows. Section 2 briefly surveys related
literature on financial resilience. Section 3 presents an overview of the dataset and
the selection of variables used for the analysis. Section 4 characterizes the data and
analyzes financial resilience by demographic profile. Section 5 explains model
choice based on the data characterization in the prior section. Section 6 discusses
the results of the prediction exercise and generates inferences on key explanatory
variables based on the modeling results. Finally, Section 7 concludes the paper and
offers potential policy implications.
II. Related Literature
Financial resilience is a multifaceted concept that has typically been
characterized as the ability to withstand unexpected income loss or financial
shocks (e.g., Klapper & Morduch, 2023 and Clark & Mitchell, 2022). It has also been
viewed from a resource-centric perspective, focusing on individuals’ access to and
usage of internal capabilities as well as external support during financial hardships
(Salignac et al., 2019). Similarly, financial vulnerability has been defined as
over-indebtedness, falling behind on utility payments, payments, insufficient
discretionary income, and susceptibility to financial shocks (Fernandez-Lopez et al.,
2023), among others.
Research on financial resilience has investigated its nexus with factors such
as financial literacy, financial inclusion, financial behavior, education, income,
gender, and age.
Klapper and Lusardi (2019) argued that financial literacy can strengthen
financial resilience as it prevents over-indebtedness and encourages savings
diversification. They found substantial gaps in financial literacy rates across income
levels (i.e., between the richest 60 percent and the poorest 40 percent households)
and educational attainment (i.e., between recipients of primary, secondary, and
tertiary education).
Department of Economic Research | Discussion Paper Series No. xx Page 4 of 28

Unpacking the Determinants of Financial Resilience in the Philippines March 2024
Clark and Mitchell (2022) designed a financial resilience index based on
questions regarding a household’s ability to handle unexpected income loss,
financial planning behavior, perception of debt, and overall financial concern. They
found that Americans who reported higher levels of resilience at the start of the
pandemic experienced lower levels of financial fragility a year after. They also found
that financial fragility was lower for higher-income, higher-educated, and more
financially literate households. Financial fragility is a self-reported measure of the
respondents’ level of confidence in their ability to gather USD2,000 in emergency
funds within the next month.
Salignac et al. (2019) proposed a multidimensional financial resilience
framework in their analysis of financial vulnerability in Australia. The authors
developed a survey to gauge access to, or demonstration of, the framework’s four
components – economic resources, financial resources, financial knowledge and
behavior, and social capital. The survey also accounted for the respondents’
demographic characteristics, including educational attainment, home ownership,
employment status, income level, gender, and age.
The study employed a linear regression model to predict composite financial
resilience scores. Researchers marked responses to survey questions from 1 (severely
financially vulnerable) to 4 (financially resilient), took the average score of the
relevant responses for each component, and then calculated the component mean
to arrive at the composite financial resilience score.
The authors found positive associations between financial resilience and
both income level and education. They also found that unsatisfactory employment
situations (i.e., being underemployed, unemployed, and working solely odd jobs)
were linked with financial vulnerability. In addition, adults aged 18-24 obtained
significantly higher resilience scores than those aged 35–49. Finally, they found no
significant evidence of a gender gap.
Hussain et al. (2019) analyzed the impact of financial inclusion on financial
resilience using 2014 Global Findex data for Bangladesh. The authors ran chi-square
tests and logistic regression models, accounting for variables such as financial
account ownership, gender, education level, income quintile, and saving behavior.
They found that financial resilience rises with account ownership, education,
income level, and saving behavior. They also noted a significant gender divide.
Similarly, Fernandez-Lopez et al. (2023)’s survey of financial vulnerability
studies showed widespread use of (ordered) logit, (ordered) probit, and ordinary
least squares regression in estimating different measures of financial vulnerability.
The use of logit models was likewise noted in studies with definitions of financial
vulnerability comparable to the Global Findex. Examples are Lee et al. (2019), which
defined financial vulnerability as the “lack of emergency savings or rainy-day funds
for three months”, and Philippas & Avdoulas (2020), whose dependent variable was
the self-reported inability “to raise €300 to tackle a rush next month” (as cited in
Fernandez-Lopez et al., 2023).
In the Philippines, financial resilience has been identified as one of the
central goals of the Philippines’ National Strategy for Financial Inclusion 2022-2028
(Financial Inclusion Steering Committee, 2023). The Financial Inclusion Survey (FIS)
conducted by the Bangko Sentral ng Pilipinas (BSP) has also begun capturing the
concept of financial resilience in its 2021 survey round. While the topic was not
covered in the nationwide quantitative survey, it was a central issue in the
accompanying focus group discussions (FGDs) conducted in Mindanao in May 2022.
Department of Economic Research | Discussion Paper Series No. xx Page 5 of 28

Unpacking the Determinants of Financial Resilience in the Philippines March 2024
Apart from such efforts to understand and integrate financial resilience in
policymaking, to the author’s knowledge, research focusing on the topic has yet to
be conducted in the Philippine context.
III. Data
Dataset Overview
Financial resilience data at the individual level remains limited in the
Philippines. Nonetheless, the publicly available Global Findex Database could
surface information that may be useful in assessing the determinants of financial
resilience (Demirgüç-Kunt et al., 2018). The Global Findex Survey collects
information on individuals’ access, use, and perception of financial services and
technologies. The survey also gathers data on financial resilience, which is framed
as the ability of the respondent to gather emergency funds within the next month
amounting to 5 percent of the country’s Gross National Income (GNI) per capita. This
is equivalent to around 1 month’s salary for an average worker in the Philippines
(Kempis & Morduch, 2020).
The Global Findex Surveys are taken from nationally representative samples
of adults aged 15 and above from more than 140 economies (Demirgüç-Kunt et al.,
2018). Gallup, Inc. conducts the surveys alongside the annual Gallup World Poll.
Since the Findex’s launch in 2011, the surveys have been completed in 3-year
intervals, with the latest round delayed to 2021-2022 due to the COVID-19
pandemic4.
Since 2011, the global surveys have taken place through a mix of phone-based
and face-to-face interviews, depending on telephone coverage and the country’s
conventional survey methodology. Prior to the pandemic, most developing
economies were surveyed face-to-face. Several, including the Philippines, shifted to
phone-based surveys in 2021 due to COVID-19 restrictions.
Data collection for the 2017 Global Findex Survey in the Philippines took
place through computer-assisted face-to-face interviews of 1,000 respondents
conducted from July to August 2017 (Demirgüç-Kunt et al., 2018). The surveys
employed a stratified sampling approach based on population size, geography, or
both. Households were chosen through random route procedures. For each
household, individual respondents were randomly selected from eligible household
members. The survey was carried out in seven languages, namely: Filipino, Iluko,
Hiligaynon, Cebuano, Masbatenyo, Waray, and Tausug.
On the other hand, the country’s 2021 survey round was conducted through
phone-based interviews of 1,000 respondents in September to November 2021
(Demirgüç-Kunt et al., 2022). Sampling was done through either mobile phone
random digit dialing or extraction of a nationally representative list of phone
numbers. The survey was carried out in four languages, namely: Filipino, Cebuano,
Bicol, and Waray.
Using the Global Findex dataset to examine the determinants of financial
resilience has immediately perceptible limitations in terms of the timeliness of data
collection and the narrow proxy measure for financial resilience. Moreover, model
4 As of writing, the World Bank has conducted Global Findex Surveys in 2011, 2014, 2017, and 2021-2022.
Department of Economic Research | Discussion Paper Series No. xx Page 6 of 28

Unpacking the Determinants of Financial Resilience in the Philippines  March 2024

accuracy may be hampered by the lack of relevant demographic variables such as
geographic location and occupation and predominantly binary variables.
Measurement errors may likewise arise due to self-reporting. Respondents
may  incorrectly  recall  or  withhold  information  that  they  deem  shameful  (for
instance, their ability to satisfy the condition for financial resilience). Nonetheless,
the conduct of the interviews in the respondents’ native languages attempts to curb
misunderstanding and response bias.

Data Preprocessing

In selecting predictive attributes for the model, the primary consideration
was to capture characteristics that may conceivably possess links to an individual’s
financial resilience. Table 1 shows the list of variables chosen for this purpose,
patterned  after  Salignac  et  al.  (2019)’s  Multidimensional  Financial  Resilience
Framework. These attributes are present in both the 2017 and 2021 survey datasets.
Most are binary variables, except for age, which is numeric/ratio; education level,
which is ordinal; and income quintile, which is ordinal.

Table 1: Predictive Attributes Selected for the Model
| Economic    | Financial  | Financial      | Social Capital  | Demographic  |
| ----------- | ---------- | -------------- | --------------- | ------------ |
| Resources   | Resources  | Knowledge      | (1)             | Variables    |
| (6)         | (4)        | and Behavior   |                 | (4)          |
(8)
| • Income      | • Financial  | • Saved*        | • Borrowed    | • Age        |
| ------------- | ------------ | --------------- | ------------- | ------------ |
| Quintile1     | Account      | • Saved for     | from Family/  | • Sex        |
| • Received    |              |                 |               | • Education  |
|               | Owner        | Retirement*     | Friends*      |              |
| Wages*        | • Debit      | • Borrowed*     |               | Level3       |
| • Received    | Cardholder   | • Borrowed for  |               | • Part of    |
| Agricultural  | • Credit     | Medical         |               | Workforce    |
| Payments*     | Cardholder   | Purposes*       |               |              |
| • Received    | • Mobile     | • Sent          |               |              |
| Government    | Money        | Domestic        |               |              |
| Transfers*    | Account      | Remittance*     |               |              |
| • Received    | Owner        | • Received      |               |              |
| Pension*      |              | Domestic        |               |              |
• Mobile Phone
Remittance*
| Owner  |     | • Paid Utilities*  |     |     |
| ------ | --- | ------------------ | --- | --- |
• Online
Transaction*2
Source: Author’s analysis
* denotes behavior in the past 12 months.
1 Income Quintile classifies respondents into the poorest up to the richest 20 percent of
households.
2 Online Transaction is a feature generated by merging responses to the use of the internet in
making bill payments and online purchases.
3 Education level classifies respondents into “Primary or lower”, “Secondary”, and “Tertiary or more”.
However, it is uncertain whether academic completion is required to be considered under
“Secondary” or “Tertiary or more”.
To eliminate missing data, observations were dropped where respondents
refused to answer or did not know the answer to any of the selected attributes. This
trimmed the 2017 dataset from 1,000 to 980 data points and the 2021 dataset from
1,000 to 992 data points. While both used the same 23 predictors, the target variable
Department of Economic Research   |   Discussion Paper Series No. xx
Page 7 of 28

Unpacking the Determinants of Financial Resilience in the Philippines March 2024
of financial resilience changed as more specific responses were introduced in the
2021 survey round5.
In 2017, respondents assessed their ability to gather emergency funds as
“possible” or “not possible”. In 2021, the evaluation shifted to difficulty, as
respondents chose between “not difficult at all”, “somewhat difficult”, and “very
difficult”. For comparability across survey rounds, respondents who answered that
they would encounter little to no difficulty in raising the subject funds were
considered financially resilient.
IV. Descriptive Results
Financial resilience is relatively balanced in both the 2017 and 2021 surveys
(Figure 1). The high frequency of both outcomes would suggest that the model may
be able to learn substantially about each class to make an adequate prediction.
Figure 1: Financial Resilience Self-Ratings
2017 2021
Source: Author’s estimates based on Global Findex data
For the 2017 survey round, financial resilience is roughly equally distributed
across age groups, except for respondents aged 20 to 40, who displayed a higher
level of resilience (Figure 2). On the other hand, 2021 survey respondents were more
financially resilient overall, except for those younger than 25 years old. Investigating
the interaction between workforce participation and age in determining resilience
(Figure 3), a considerably higher percentage of 2017 survey respondents who were
not in the workforce reported less resilience, except for those in their late 20s to
early 30s, who were markedly more financially resilient than their counterparts –
possibly because their exclusion from the labor force is by choice6. The same general
pattern holds for 2021 survey respondents.
Figure 2: Financial Resilience by Age
2017 2021
5 A slight modification in phrasing was also implemented in the 2021 survey round. While the 2017 survey asked
about the availability of emergency funds "within the next month", in 2021 the reference period changed to
"within the next 30 days".
6 The labor force comprises both the employed and the unemployed job-seekers. It excludes unpaid workers,
family workers, and students. (Source: World Bank via https://data.worldbank.org/indicator/SL.TLF.TOTL.IN)
Department of Economic Research | Discussion Paper Series No. xx Page 8 of 28

Unpacking the Determinants of Financial Resilience in the Philippines March 2024
Source: Author’s estimates based on Global Findex data
Figure 3: Financial Resilience by Age and Workforce Participation
2017
2021
Source: Global Findex, Author’s estimates
A breakdown by income quintile shows a balanced dataset for the 2017
survey and a higher percentage of adults from the richest 20 percent for the 2021
survey (Figure 4). As expected, richer households reported higher financial
resilience, although the proportion of non-financially resilient among the highest
socioeconomic class in the 2017 survey is surprisingly elevated at 30 percent.
Financial resilience also appears to have declined from 2017 to 2021 for the poorest
40 percent, and the opposite for the richest 60 percent. Examining the interaction
between education and income level, the 2017 and 2021 surveys both reveal that
Department of Economic Research | Discussion Paper Series No. xx Page 9 of 28

Unpacking the Determinants of Financial Resilience in the Philippines March 2024
the educated tend to be more financially resilient and also belong to higher
socioeconomic classes (Figure 5). These results align with Debuque-Gonzales and
Corpus (2021)’s findings that lesser educated and lower-income individuals are less
likely to be financially included.
Figure 4: Financial Resilience by Income
2017 2021
Source: Author’s estimates based on Global Findex data
Figure 5: Financial Resilience by Income Quintile and Education
2017
2021
Source: Author’s estimates based on Global Findex data
Gender gaps have been widely noted in much of financial inclusion literature
(e.g., Sahay & Cihak, 2018). Results for the 2017 and 2021 Global Findex Database
show a similar gap in terms of financial resilience (Tables 2a and 2b). While the
difference is less pronounced in the 2017 survey compared to other country-level
studies that have used the Global Findex (e.g., Hussain et al., 2019), the gender gap
in financial resilience noticeably widened in 2021. These results contrast against
findings from the 2017 Global Findex data that females in the country are more
Department of Economic Research | Discussion Paper Series No. xx Page 10 of 28

Unpacking the Determinants of Financial Resilience in the Philippines  March 2024

likely to own a bank account than males, with the gap estimated at around 10
percentage points (Debuque-Gonzales and Corpus, 2021).

Table 2a: Financial Resilience by Sex - 2017
Financial
|      | Not Financially  | Financially  |        |             |     |
| ---- | ---------------- | ------------ | ------ | ----------- | --- |
| Sex  |                  |              | Total  | Resilience  |     |
|      | Resilient        | Resilient    |        |             |     |
(in percent)
| Female  | 297  | 254  | 551  | 46.1  |     |
| ------- | ---- | ---- | ---- | ----- | --- |
| Male    | 199  | 230  | 429  | 53.6  |     |

Table 2b: Financial Resilience by Sex – 2021
Financial
|      | Not Financially  | Financially  |        |             |     |
| ---- | ---------------- | ------------ | ------ | ----------- | --- |
| Sex  |                  |              | Total  | Resilience  |     |
|      | Resilient        | Resilient    |        |             |     |
(in percent)
| Female  | 275  | 296  | 571  | 51.8  |     |
| ------- | ---- | ---- | ---- | ----- | --- |
| Male    | 132  | 289  | 421  | 68.6  |     |
Source: Author’s estimates based on Global Findex data

Respondents in the 2021 Global Findex survey are substantially younger than
those interviewed for the 2017 survey (Tables 3a and 3b). The standard deviation of
17.5 years in the 2017 survey suggests that the data is reasonably spread out and that
the majority of respondents are of working age (i.e., aged 23 to 58). On the other
hand, for the 2021 survey, the majority of respondents are aged 20 to 46. The
younger demographic could, in part, stem from the change in interview mode due
to the COVID-19 pandemic, as researchers shifted from face-to-face interviews in
2017 to phone surveys in 2021. This is consistent with reports of the Philippines
having one of the highest generational divides globally both in terms of internet use
and smartphone ownership.7

Table 3a: Descriptive Statistics for Numeric Variables - 2017
| Variable         | Minimum  | Mean  | SD    | Median  | Maximum  |
| ---------------- | -------- | ----- | ----- | ------- | -------- |
| Age (in years)   | 15       | 40.5  | 17.5  | 37      | 95       |
| Income Quintile  | 1        | 3.1   | 1.4   | 3       | 5        |

Table 3b: Descriptive Statistics for Numeric Variables – 2021
| Variable         | Minimum  | Mean  | SD    | Median  | Maximum  |
| ---------------- | -------- | ----- | ----- | ------- | -------- |
| Age (in years)   | 15       | 32.9  | 12.6  | 31      | 87       |
| Income Quintile  | 1        | 3.4   | 1.4   | 4       | 5        |
Source: Author’s estimates based on Global Findex data

The comparably lower median relative to mean age for both the 2017 and
2021 surveys (median of 37 and mean of 40.5 for the 2017 survey and median of 31
and mean of 32.9 for the 2021 survey) suggests that older respondents are possible
outliers who are pulling the mean upwards. Indeed, both z-score and interquartile
range (IQR) methods identified one respondent aged 95 as an outlier in the 2017
survey and four respondents aged 71 and above as outliers in the 2021 survey.
However, these observations will be kept as they may provide useful information on
one’s financial resilience as one ages.
The income quintile shows a roughly uniform distribution in the 2017 survey,
while the 2021 survey appears to skew towards higher income quintiles given its

7 A 2019 Pew Research survey found that 36 percent of Filipinos aged 50 and above used the internet or owned a
smart phone, in contrast to 74 percent of 30- to 49-year-olds and 94 percent of adults aged 18 to 29 (Schumacher
& Kent, 2020).
Department of Economic Research   |   Discussion Paper Series No. xx
Page 11 of 28

Unpacking the Determinants of Financial Resilience in the Philippines  March 2024

median of 4 (Tables 3a and 3b). This may likewise relate to the shift in interview
mode from 2017 to 2021.8
Roughly 60 percent of respondents in both 2017 and 2021 surveys were
classified as recipients of secondary education (Tables 4a and 4b). 2021 survey
respondents tended to be more educated than their 2017 counterparts. While 29.1
percent of adults in the 2017 survey were primary-educated and 11.4 percent were
tertiary-educated, the composition reversed in the 2021 survey, where 14.5 percent
of respondents received only primary education or less and 27.6 percent reached
tertiary  education.  This  is  in  line  with  earlier  observations  of  the  2021  survey
demographic tending towards the technologically inclined (i.e., younger, working,
and higher-income).

Table 4a: Frequency Tabulation for Education Level - 2017
Cumulative
Relative
|                  |            |             | Cumulative  | Relative    |
| ---------------- | ---------- | ----------- | ----------- | ----------- |
| Education Level  | Frequency  | Frequency1  |             |             |
|                  |            |             | Frequency   | Frequency2  |
(in percent)
(in percent)
| Primary or less   | 285  | 29.1  | 285  | 29.1   |
| ----------------- | ---- | ----- | ---- | ------ |
| Secondary         | 583  | 59.5  | 868  | 88.6   |
| Tertiary or more  | 112  | 11.4  | 980  | 100.0  |

Table 4b: Frequency Tabulation for Education Level - 2021
Cumulative
Relative
|                  |            |             | Cumulative  | Relative    |
| ---------------- | ---------- | ----------- | ----------- | ----------- |
| Education Level  | Frequency  | Frequency1  |             |             |
|                  |            |             | Frequency   | Frequency2  |
(in percent)
(in percent)
| Primary or less   | 144  | 14.5  | 144  | 14.5   |
| ----------------- | ---- | ----- | ---- | ------ |
| Secondary         | 574  | 57.9  | 718  | 72.4   |
| Tertiary or more  | 274  | 27.6  | 992  | 100.0  |
Source: Author’s estimates based on Global Findex data
1 Relative Frequency is the proportion of occurrence of a subject category within the dataset. It is
computed by dividing the frequency of the category by the number of observations in the dataset.
2 Cumulative Relative Frequency is the proportion of occurrence of all categories lower than or equal
to the subject category. It is computed by summing the relative frequencies of the said categories.

Figure 6 shows a graphical summary of the frequency tabulations generated
by the binary variables selected for the model. More than half of indicators fall
below 50 percent (marked by the blue dashed line), which highlights the long
journey  that  remains  towards  financial  development.  This  also  indicates other
possible rare cases  that  may crop  up,  as  less than  10 percent  of  respondents
responded positively to the bottom 4 indicators in the 2017 survey, i.e.: credit card
ownership, mobile money account ownership, conduct of online transactions, and
receipt of pension.
Figure 6: Profile and Financial Behavior
2017

8 The 2019 Pew Research survey found a differential of 19 percentage points between higher and lower-income
use of internet or smartphone ownership (Schumacher & Kent, 2020).
Department of Economic Research   |   Discussion Paper Series No. xx
Page 12 of 28

Unpacking the Determinants of Financial Resilience in the Philippines March 2024
2021
Source: Author’s estimates based on Global Findex data
Nonetheless, several indicators registered gains from 2017 to 2021 amid the
COVID-19 pandemic. Mobile phone ownership rose from 75.8 percent to
96.3 percent. Financial account ownership improved from 34.3 percent to
56.8 percent. Mobile money account owners leapt from 4.4 percent to 30.2 percent.
Respondents that have engaged in online purchases likewise leapt from 8.8 percent
to 51.1 percent. Proactive financial behavior developed as well, with savers
increasing from 59.6 percent to 64.8 percent of respondents. Saving for retirement
also jumped from 29.0 percent to 41.7 percent despite the younger demographic
for the 2021 survey.
These developments could, in part, be an unintended consequence of the
pandemic. Social distancing protocols may have enticed people to shift to online
Department of Economic Research | Discussion Paper Series No. xx Page 13 of 28

Unpacking the Determinants of Financial Resilience in the Philippines March 2024
transactions, while health and income shocks may have highlighted the need for
proactive saving behavior. However, the change in survey enumeration from
face-to-face in 2017 to phone-based in 2021 might also have contributed to the
changes. The data characterization exercise thus far consistently suggests higher
technological inclination for 2021 survey respondents.
The shift to phone-based surveys may have implications on generalizability,
as the 2021 respondents needed to have phone access (though not necessarily
ownership) for them to be interviewed. Those without phones, likely from lower
incomes or less educated backgrounds, would be excluded. Nonetheless, we could
hypothesize that the income and education gaps noted in the 2021 data would
widen further if those without access to mobile phones were also included in the
sample.
Trends found in the Global Findex are generally consistent with the results of
the BSP Financial Inclusion Survey (FIS), which found that account penetration
increased from 23 percent in 2017 to 56 percent in 2021. E-money accounts likewise
jumped from 8 percent in 2019 to 36 percent in 2021. However, adults with savings
declined from 48 percent in 2017 to 37 percent in 2021, contrasting against the rise
in saving behavior found in the Global Findex. Results of the latter suggested that
savers slightly increased, from 59.6 percent in 2017 to 64.8 percent in 2021. The
divergence may be due to differences in questioning, where the Findex probes into
any instance of saving behavior within the past year while the FIS asks about
outstanding savings at the time of the survey.
The predominantly binary nature of the Global Findex variables renders
correlation (and the related Variance Inflation Factor) inappropriate in checking for
multicollinearity. The Simple Matching Coefficient (SMC) would be a more suitable
measure for binary attributes, as SMC calculates similarity as the proportion of exact
matches between two variables (i.e., respondents whose attributes are both positive
(1-1) or both null (0-0) for the variables under comparison). Based on the SMC,
financial resilience does not appear to be strongly connected to any specific
attribute (Figure 7). However, large SMCs (of at least 0.8) were found for
combinations of least frequently occurring characteristics identified in Figure 6,
which could be due to the high number of null (0-0) matches.
Figure 7: Similarity between Binary Variables (Using Simple Matching Coefficient)
2017 2021
Source: Author’s estimates
V. Empirical Methodology
Department of Economic Research | Discussion Paper Series No. xx Page 14 of 28

Unpacking the Determinants of Financial Resilience in the Philippines March 2024
Model Selection
Based on this study’s objective of deriving insights on the most important
predictors of financial resilience in Filipinos, models selected for the purpose should
be equipped to handle classification problems and provide meaningful inferences
on the predictive power of the attributes. On the other hand, data characterization
in the previous section indicates that (1) overfitting should be sufficiently addressed
given the presence of 23 predictors chosen based on domain knowledge; (2) the
model would ideally be robust to outliers, considering rare binary cases and a
relatively small percentage of older respondents; (3) the model should be able to
handle redundant/irrelevant variables, given the various related financial indicators
selected as attributes; and (4) the model should be capable of dealing with
interacting variables, whose presence is evident from the data characterization.
Thus, the Logistic/Logistic LASSO Regression and the Decision Tree models appear
well-suited for this study.
Logistic and Logistic LASSO Regression
Logistic regression belongs to a set of parametric techniques widely used as
a foundation for statistical analysis due to their interpretability and portability from
theoretical to empirical analysis.
Logistic regression predicts the probability that a particular entity belongs to
a specific class. It does so by generating maximum likelihood estimates based on
the combination of characteristics that led to previous occurrences of the outcome.
In other words, it determines likely predictors of known outcomes and assesses new
data against this model to predict which outcome is most likely given a specific set
of values for the predictors.
Logistic regression has also been used in similar studies analyzing financial
inclusion. One such study uses Findex Data collected from selected Southeast Asian
countries in 2014 to study the determinants of financial inclusion, defined as access
to a financial account (Tjahjadi & Ajani, 2018). The research used individual
characteristics and factors related to borrowing to predict the level of inclusion
across different income levels and countries.
In this study, logistic regression was chosen because it deals well with
irrelevant, redundant, and interacting variables. However, the technique tends to be
sensitive to outliers. Hence, issues may arise around the robustness of the results
amidst the presence of rare cases in the age variable as well as some financial
indicators.
Since it seeks the combination of predictors that will best fit existing data,
logistic regression models tend to overfit as the parameters increase. To aid in
model generation, LASSO can be used as a shrinkage method to zero out irrelevant
coefficient estimates. LASSO can filter factors of financial resilience that provide the
highest predictive value. Performing LASSO requires standardized features to
eliminate issues with scaling that may cause larger-ranged variables such as age to
dominate the regression model.
Decision Tree
Department of Economic Research | Discussion Paper Series No. xx Page 15 of 28

Unpacking the Determinants of Financial Resilience in the Philippines March 2024
Decision tree is a non-parametric technique that splits known cases into
groupings that would maximize homogeneity. New data will then be classified
based on rules generated from the splits. Decision tree is widely used for its
straightforward interpretability and accessibility to the non-technical audience. The
method is likewise robust to irrelevant variables and outliers, which is important in
this study given the relatively large number of parameters and the rare cases noted
during data characterization.
Decision tree has likewise been used to determine key factors in financial
inclusion. Aiming to segment Indian survey respondents into the financially
excluded and included, Tiwari et al. (2019) generated classes based on a composite
measure of financial inclusion (composed of bank account ownership, access to
loan requirements, insurance coverage, and access to digital banking). The authors
generated a decision tree that classified individuals as included or excluded based
on demographic, social, and economic variables.
Like logistic regression, decision tree may be prone to overfitting as the
number of parameters increases. Too many variables may cause the decision tree
to accidentally overstate the importance of irrelevant variables. Nonetheless, this
should not preclude the use of the algorithm. Various methods can address model
overfitting, such as limiting tree size or pruning to penalize larger trees.
VI. Results and Discussion
Predictive Models of Financial Resilience
Model performance is evaluated against the baseline financial resilience rate
(49.4 percent in the 2017 survey and 59.0 percent in the 2021 survey). This means
that if a model were to tag all respondents as financially resilient, it will obtain an
accuracy of 49.4 percent on 2017 data and 59.0 percent on 2021 data. Similarly, if all
respondents are labeled as financially vulnerable, the accuracy will stand at 50.6
percent on 2017 data and 41.0 percent on 2021 data.
For model building, this study runs different logistic regression and decision
tree models based on selected hyper-parameters. Hyper-parameter values
maximizing test set accuracy were chosen. The chosen models were then run
against the same set of training and test data, split at 25 percent to allow the
models to train on a substantial training set (more than 700 observations) while
keeping a sizeable test set (almost 250 observations).
Tables 5a and 5b compare the accuracy scores of the different models on the
test data. The accuracy scores hovered in the 59-65 percent range for 2017 data and
62-68 percent for 2021 data. To the author’s knowledge, the closest study on
financial resilience that similarly gauges model accuracy is that of Hussain et al.
(2019), which estimates that its logistic model can correctly identify the financial
resilience of 76 percent of individuals, based on 2014 Global Findex data in
Bangladesh.
Table 5a: Accuracy Scores across Different Models – 2017
Accuracy Score
Classifier Hyper-parameter1
(in percent)
Department of Economic Research | Discussion Paper Series No. xx Page 16 of 28

Unpacking the Determinants of Financial Resilience in the Philippines  March 2024

|     | none  | 60.0  |
| --- | ----- | ----- |
Logistic Regression
|                | LASSO (L1 penalty) with C = 0.21       | 61.2  |
| -------------- | -------------------------------------- | ----- |
|                | Maximum Tree Depth = 2                 | 61.2  |
|                | Minimum Samples per Leaf = 39          | 63.7  |
| Decision Tree  | Cost Complexity Pruning Alpha = 0.015  | 61.2  |
|                | Minimum Samples per Split = 151        | 64.1  |
|                | Grid-Search Optimized Parameters       | 59.2  |
Random Forest2  Maximum Tree Depth = 3; Estimators = 1,500  65.3

Table 5b: Accuracy Scores across Different Models – 2021
Accuracy Score
| Classifier  | Hyper-parameter1  |     |
| ----------- | ----------------- | --- |
(in percent)
|     | none  | 66.5  |
| --- | ----- | ----- |
Logistic Regression
|                      | LASSO (L1 penalty) with C = 0.1               | 66.5  |
| -------------------- | --------------------------------------------- | ----- |
|                      | Maximum Tree Depth = 4                        | 65.3  |
|                      | Minimum Samples per Leaf = 52                 | 66.9  |
| Decision Tree        | Cost Complexity Pruning Alpha = 0.015         | 65.3  |
|                      | Minimum Samples per Split = 99                | 68.1  |
|                      | Alpha = 0.001; Minimum Samples per Leaf = 60  | 66.9  |
| Linear Discriminant  | none                                          |       |
66.9
Analysis3
Source: Author’s estimates
Table 5 Notes:
1 Except for Logistic Regression, models were iterated across a range of hyper-parameter values. Final hyper-
parameter values were those that yielded the best mean test set accuracy scores.
2 Random Forest generates predictions based on an ensemble of Decision Trees trained on different subsets of the
data and variables.
3 Linear Discriminant Analysis classifies data based on linear combinations of variables that minimize within-group
separation and maximize between-group separation.

Since  both  decision  tree  and  logistic  regression  models  may  sacrifice
accuracy for interpretability, a benchmark model was introduced to determine
whether higher predictive accuracy could be achieved. Random Forest (with a
maximum tree depth of 3 and 1,500 estimators) emerged with the best predictive
score on 2017 data and Linear Discriminant Analysis on 2021 data. Nonetheless, both
models still resulted in test accuracy scores below 70 percent (Table 5). Other
models considered include Naïve Bayes, Linear Discriminant Analysis, K-Nearest
Neighbors, Neural Networks, Random Forest, and Support Vector Machines9.
The Receiver Operating Characteristic (ROC) curve in Figure 8 provides a
graphical comparison of the models’ predictive performances. All models follow
roughly the same path – all better than 50 percent chance but far from the ideal
where the curve hugs the top left corner of the axis (signifying the ability to achieve
high true positive rates while keeping false positive rates low). The Random Forest
tends to produce better results for 2017 data while Linear Discriminant Analysis and
Logistic (LASSO) Regression tend to perform better for 2021 data.

Figure 8: Receiver Operating Characteristic (ROC) Curve
| 2017  | 2021  |     |
| ----- | ----- | --- |

9 Accuracy scores for the other models are as follows:
•  For 2017 survey data, Linear Discriminant Analysis: 60.0 percent, K Nearest Neighbors: 62.9 percent,
Support Vector Machine: 60.0 percent, Naïve Bayes: 62.0 percent, Neural Network: 63.7 percent
•  For 2021 survey data, K Nearest Neighbors: 65.7 percent, Random Forest: 64.1 percent, Support Vector
Machine: 65.7 percent, Naïve Bayes: 65.3 percent, Neural Network: 64.9 percent
Department of Economic Research   |   Discussion Paper Series No. xx
Page 17 of 28

Unpacking the Determinants of Financial Resilience in the Philippines March 2024
Source: Global Findex, Author’s estimates
While accuracy is important in distinguishing the financially resilient from
the financially vulnerable (which would thereby facilitate the proper targeting of
interventions), it is more important to dissect the components of these accuracy
measures and assess the nature of the models’ misclassifications. The models’
confusion matrices highlight the trade-off between sensitivity (ability to identify
true positives) and specificity (ability to identify true negatives) (Figure 9). For 2017
data, the Decision Tree model with at least 151 samples per split yielded the highest
number of true negatives and fewest false positives (where “positive” means
financially resilient and “negative” means otherwise). For 2021 data, the same is
exhibited by the Decision Tree model with cost complexity alpha of 0.015.
Figure 9: Confusion Matrix Values across Models
2017
2021
Department of Economic Research | Discussion Paper Series No. xx Page 18 of 28

Unpacking the Determinants of Financial Resilience in the Philippines March 2024
Source: Author’s estimates
Taken together, the model performance metrics considered thus far indicate
that the best overall model for the 2017 data would be the Decision Tree model with
at least 151 samples per split as it achieved the highest accuracy score while
maximizing true negatives and minimizing false positives. The ROC curve likewise
showed that, except at very low positive rates, the same Decision Tree model
generally performed at par with the Random Forest, which registered the best
performance in this measure. On the other hand, for 2021 data, considered model
metrics suggest that the best overall model would be the Decision Tree model with
at least 99 samples per split. It topped accuracy at 68.1 percent and performed well
at higher positive rates in the ROC curve. It also identified the highest number of
true positives out of the models tested, but fewer true negatives than the Decision
Tree model with cost complexity alpha of 0.015.
Nonetheless, with the intention is to cover as many of the financially
vulnerable as possible, the models chosen to generate inferences in the next section
were those that identified the highest number of true negatives and lowest false
positives, i.e.: for 2017, the Decision Tree with at least 151 samples per split (which
incidentally is also the best overall model) and for 2021, the Decision Tree with cost
complexity alpha of 0.015. It may be worth noting that the tradeoff for choosing a
model with a higher number of false negatives would be that interventions would
also reach a considerable number of individuals who may already be financially
resilient.
Inferences on the Determinants of Financial Resilience
Logistic LASSO regressions for both the 2017 and 2021 survey rounds
consistently suggest that financial resilience possesses a strong, positive
relationship with income quintile; a moderate, positive relationship with saving for
retirement; and a moderate, negative relationship with being female (Figure 10).
The magnitude of the regression coefficient for income quintile noticeably rose
from 2017 to 2021. Conversely, the magnitude for saving for retirement decreased
Department of Economic Research | Discussion Paper Series No. xx Page 19 of 28

Unpacking the Determinants of Financial Resilience in the Philippines March 2024
and for gender (female), increased slightly. Moreover, tertiary education jumped
from assuming a minimal regression coefficient in 2017 to being second only to
income quintile in 2021. The widening financial resilience gap between income
classes, genders, and educational attainment, coupled with the weakened link
between financial resilience and saving behavior, supports concerns that the
COVID-19 pandemic would likely deepen inequalities (Jurzyk et al., 2020).
Figure 10: Logistic Regression and Logistic LASSO Regression Coefficients
2017
2021
Source: Author’s estimates
The LASSO regression found that age was strongly negatively associated with
financial resilience in 2017 but turned uninformative in 2021. In contrast, the model
found borrowing for medical purposes uninformative in 2017 but noted a stronger
negative association with financial resilience in 2021, second only to gender (i.e.,
Department of Economic Research | Discussion Paper Series No. xx Page 20 of 28

Unpacking the Determinants of Financial Resilience in the Philippines March 2024
being female). The change in predictive value for age might be linked with the
earlier result where respondents in the 2017 survey aged below 40 tended to be
more financially resilient than older age groups, especially those in retirement age
(70 and above). On the other hand, there were no discernible differences between
age groups in the 2021 survey. The negative association found for medical-related
borrowing in the 2021 survey could be linked with findings of the COVID-19
Household Survey that the World Bank conducted in December 2020, where 62
percent of households cited lack of money as a reason for inability to access
treatment (Piza et al., 2021).
While online payments was one of the top predictors in the 2017 survey, its
association with financial resilience decreased in 2021. This may be due to the
adjustments brought about by physical lockdowns during the COVID-19 pandemic,
as transacting online became widespread. The Global Findex survey found that
Filipinos who conducted online payments sharply increased from 9 percent in 2017
to 51 percent in 2021. That the pandemic transformed online transactions into a
norm rather than an exception may have led to the financial indicator’s weakened
ability to distinguish between the resilient and vulnerable (perhaps as a proxy for
financial literacy).
The positive association between financial resilience and sending domestic
remittances also noticeably decreased from 2017 to 2021. Like online payments, the
Global Findex found that more Filipinos sent domestic remittances during the
pandemic, from 25 percent in 2017 to 39 percent in 2021. While the reason for the
remittances is unknown, its positive link with financial resilience may be traced to
social capital, one of the components of Salignac et al. (2019)’s Multidimensional
Financial Resilience Framework. As financial hardships mounted during the
pandemic, it would be reasonable to hypothesize that families and friends would
provide financial support to loved ones in need, at the expense of their own financial
security. Notably, the association between financial resilience and receiving
domestic remittances remained minimal and positive from 2017 to 2021.
Figure 11 displays the decision trees with the highest true negative rates.
Consistent with the results of the logistic LASSO regression, income quintile
remained the most important predictor. For the 2017 survey round, this was
followed by savings – whether for retirement (for respondents belonging to the
richest 40 percent in terms of household income quintile) or regardless of purpose
(for the poorest 60 percent). On the other hand, saving behavior did not figure
prominently in the 2021 survey round. Instead, the results suggest three groups of
respondents exhibiting varying levels of financial resilience: first (and most likely to
be resilient) are the more affluent (i.e., among the richest 40 percent) who were also
tertiary-educated; second are the rest of the more affluent who did not receive
tertiary education; and third (and least likely to be resilient) are respondents
belonging to the poorest 60 percent of the population. Nonetheless, it must be
noted that Gini scores remain high across most nodes, with a notable exception
being tertiary-educated, higher-income respondents for the 2021 survey (who were
mostly financially resilient). Respondents must be segregated further, and a larger
sample might be needed to identify more accurately who are the financially
resilient vis-à-vis those who are not.
Figure 11: Decision Trees with Highest True Negative Rates
2017 (Minimum Samples per Split = 151)
Department of Economic Research | Discussion Paper Series No. xx Page 21 of 28

Unpacking the Determinants of Financial Resilience in the Philippines March 2024
2021 (Cost-Complexity Pruning Alpha = 0.015)
Source: Author’s estimates
In terms of feature importance for the decision tree and random forest
models (Figure 12), the results are similar to the Decision Trees chosen in Figure 11.
Income quintile was the top predictor in both the 2017 and 2021 surveys. In 2017,
both forms of saving behavior (i.e., saving for any purpose and saving for retirement)
also ranked high in feature importance. Other noteworthy factors that figured
prominently in 2017 are online purchases, debit card ownership, and age. In 2021,
the most predictive factors were tertiary education, saving per se, borrowing for
medical reasons, and gender.
Department of Economic Research | Discussion Paper Series No. xx Page 22 of 28

Unpacking the Determinants of Financial Resilience in the Philippines March 2024
Figure 12: Feature Importance across Decision Tree and Random Forest Models
2017
2021
Source: Author’s estimates
Department of Economic Research | Discussion Paper Series No. xx Page 23 of 28

Unpacking the Determinants of Financial Resilience in the Philippines March 2024
VII. Conclusions and Policy Implications
This paper explores the determinants of Filipinos’ financial resilience through
the construction of predictive models and from there, the generation of inferences
on the most important predictors of financial resilience. Using World Bank Global
Findex data for the Philippines in 2017 and 2021, empirical results consistently
identify income quintile, saving behavior, and gender as the top predictors for
financial resilience for both years. Additionally, age, saving for retirement, and
online payments were important features for 2017, while tertiary education and
medical borrowing were important for 2021. These findings indicate that
demographics remains the largest determinant for financial resilience. The results
also seem to suggest that financial inclusion, i.e., access to and usage of financial
products, does not necessarily translate to resilience.
Income level and gender consistently emerged as the most important
variables in the models. Results of the 2021 survey round likewise showed that
tertiary education is second only to income quintile in predicting financial
resilience. The significance of income, gender, and education to financial resilience
is consistent with literature. Debuque-Gonzales and Corpus (2021) point out that
lower-income and less-educated Filipinos may experience “involuntarily exclusion”
from the formal financial system. In this regard, policymakers may consider crafting
programs targeted towards improving employment and educational opportunities
for those in the lower socioeconomic classes. Additional safety nets may also be
considered for females, who, despite their higher participation in the formal
financial system, still lag behind males in terms of financial resilience, with the
divide even widening from 2017 to 2021.10 A similar gender gap is apparent in the
labor market, where female labor force participation remains one of the lowest in
the region (Buchhave & Belghith, 2022). Initiatives empowering women to gain
access to higher quality jobs and encouraging entry into the workforce could thus
help close the financial resilience gap.
The Philippine government has implemented a conditional cash transfer
(CCT) program which benefits around 20 percent of the population (World Bank,
2017). The decision tree model’s choice to split after the 3rd income quintile may
indicate that it is not just the poorest of the poor who face increased financial
vulnerability. This result warrants a reassessment of social safety nets that have
traditionally focused on the poorest 20 percent. Broadening social protection
measures provided to the poorest 60 percent may not necessarily involve
expanding CCT coverage or providing direct transfers but may come in other forms
of assistance such as insurance mechanisms and micro-credit opportunities that
may help the entrepreneurial poor to tap into additional funding sources that
would allow them to earn income and become self-sufficient. As the 2018
Consumer Finance Survey (CFS) finds, only a small segment of Filipino households
(5.1 percent) are engaged in entrepreneurial activities.
Saving behavior was likewise a key predictor in most of the models. Notably,
the decision tree identified different forms of savings as important for the different
socioeconomic classes. For those with lower income levels, the act of saving, in
whatever form or for whatever purpose, mattered the most. However, for those with
higher income levels, saving for one’s retirement mattered the most.
10 Females are more likely and may even be more determined to become financially included (Debuque-Gonzales
and Corpus, 2021).
Department of Economic Research | Discussion Paper Series No. xx Page 24 of 28

Unpacking the Determinants of Financial Resilience in the Philippines March 2024
The importance for poorer households of having the ability to save, coupled
with the emergence of a sizeable association between financial vulnerability and
borrowing for medical purposes, highlight the need for enhanced insurance
mechanisms against economic shocks such as disasters and medical emergencies.
For instance, for lower-income farmers whose earnings may be sensitive to
weather-related disruptions, the government may consider setting up agricultural
insurance programs. Healthcare coverage may also be reassessed to determine the
extent of out-of-pocket payments required from poorer beneficiaries. Improved
public health services would likewise improve the quality of life of poor families,
protecting them against morbidity-induced income losses and health
expenditures. Further, the government should enhance pandemic preparedness, as
poor epidemiological response undermines not only public health but also the
financial resilience of the lower income population.
For higher-income individuals, saving for the future may matter more than
saving for other purposes (e.g., for business or for a major purchase). Since even the
more affluent can experience financial vulnerability, expanding financial literacy
programs can be beneficial in instilling the value of financial discipline and saving
into the broader populace. Both the CFS report and Debuque-Gonzales and Corpus
(2021) study similarly advocate for financial education. The 2018 CFS also raised
concerns that Filipino households appeared to prioritize consumption and
purchase of non-financial assets over savings and investment. More than half of
Filipino households were found to be over-indebted and experienced challenges
meeting monthly obligations.
Modest model accuracy coupled with other limitations of the dataset, such
as the narrow proxy measure for financial resilience used in the Findex survey, may
weigh on the validity of the findings. The consistent below-70 percent accuracy of
the various models highlights the need for more granular survey data, as several
factors remain unmeasured by the current dataset. A more adequate assessment of
financial resilience may emanate from the introduction of additional demographic
variables relating to home ownership, employment status, industry, as well as
information across other dimensions of financial resilience (such as savings level,
debt management ability, access to credit, access to insurance, credit demand,
insurance demand, financial knowledge, financial behavior, and access to social
support).
Findings from this study may allow policymakers to assess priority areas
requiring intervention. However, a definitive understanding of the financially
vulnerable and the appropriate interventions would require the conduct of more
focused studies. As such, future research may consider investigating causal links
between financial resilience and the variables with high predictive value that were
identified in this study.
Department of Economic Research | Discussion Paper Series No. xx Page 25 of 28

Unpacking the Determinants of Financial Resilience in the Philippines March 2024
References
Bangko Sentral ng Pilipinas. (2018, February). The Credit Surety Fund: Concept and
Creation. Retrieved March 10, 2021, from
https://www.bsp.gov.ph/Media_and_Research/Primers Faqs/CSF.pdf
Bangko Sentral ng Pilipinas. (2021, October). 2018 Consumer Finance Survey [PDF file].
Retrieved October 6, 2023, from
https://www.bsp.gov.ph/Media_And_Research/Consumer%20Finance%20Survey/C
FS_2018.pdf
Bangko Sentral ng Pilipinas. (2018, July). 2017 Financial Inclusion Survey [PDF file].
Retrieved October 6, 2023, from
https://www.bsp.gov.ph/Inclusive%20Finance/Financial%20Inclusion%20Reports%
20and%20Publications/2017/2017FISToplineReport.pdf
Bangko Sentral ng Pilipinas. (2022, August). 2021 Financial Inclusion Survey [PDF file].
Retrieved October 6, 2023, from
https://www.bsp.gov.ph/Inclusive%20Finance/Financial%20Inclusion%20Reports%
20and%20Publications/2021/2021FISToplineReport.pdf
Buchhave, H. & Belghith, N.B.H. (2022, April 11). Overcoming barriers to women’s work in
the Philippines. Retrieved November 7, 2023, from
https://blogs.worldbank.org/eastasiapacific/overcoming-barriers-womens-work-
philippines
Clark, R. L. & Mitchell, O. S. (2022). Americans’ financial resilience during the pandemic.
Financial Planning Review, 5(2–3). doi:10.1002/cfp2.1140
Debuque-Gonzales, M. & Corpus, J.P. (2021). Understanding and measuring financial
inclusion in the Philippines. Philippine Institute for Development Studies (PIDS)
Discussion Paper Series, No. 2021-37. Retrieved June 20, 2023 from
http://hdl.handle.net/10419/256872
Demirgüç-Kunt, A., Klapper, L., Singer, D., Ansar, S., & Hess, J. (2018). The Global Findex
Database 2017: Measuring Financial Inclusion and the Fintech Revolution.
Washington, DC: World Bank. Ref: PHL_2017_FINDEX_v02_M. Accessed at
https://microdata.worldbank.org/index.php/catalog/3311 on 11 July 2023.
Demirgüç-Kunt, A., Klapper, L., Singer, D., & Ansar, S. (2022). The Global Findex Database
2021: Financial inclusion, Digital Payments, and Resilience in the Age of COVID-19.
Washington, DC: World Bank. doi:10.1596/978-1-4648-1897-4
Economic Policy Research Institute. (2020, December 10). The Impact of the COVID-19
Crisis on Households in the National Capital Region of the Philippines (Rep.).
Retrieved March 10, 2021, from UNDP and UNICEF Philippines website:
https://www.unicef.org/philippines/media/2061/file/Final report: The Impact of the
COVID-19 Crisis on Households in the National Capital Region of the Philippines.pdf
Fernandez-Lopez, S., Alvarez-Espiño, M., Castro-Gonzalez, S., & Rey-Ares, L. (2023). Financial
capability and households’ financial vulnerability: evidence for the Spanish
case. Managerial Finance, 49(4), 679-702. doi:10.1108/MF-02-2022-0086
Financial Inclusion Steering Committee. (2023). 2022 Annual Report of the National
Strategy for Financial Inclusion 2022-2028. Retrieved September 29, 2023, from BSP
website:
https://www.bsp.gov.ph/Pages/InclusiveFinance/2022NSFIAnnualReport.pdf
Hussain, A. B., Endut, N., Das, S., Chowdhury, M. T., Haque, N., Sultana, S., & Ahmed, K. J.
(2019). Does financial inclusion increase financial resilience? Evidence from
Department of Economic Research | Discussion Paper Series No. xx Page 26 of 28

Unpacking the Determinants of Financial Resilience in the Philippines March 2024
Bangladesh. Development in Practice, 29(6), 798-807.
doi:10.1080/09614524.2019.1607256
Jurzyk, E., Nair, M. M., Pouokam, N., Sedik, T. S., Tan, A., & Yakadina, I. (2020). COVID-19 and
Inequality in Asia. IMF Working Papers, 20(217). doi:10.5089/9781513559179.001
Kempis, M. & Morduch, J. (2020, May 21). How resilient are we? A dive into the global data
on how people deal with unexpected shocks. Retrieved July 7, 2023, from
https://www.financialaccess.org/blog/2020/5/21/how-resilient-are-we-a-dive-into-
the-global-data-on-how-people-deal-with-unexpected-shocks
Klapper, L. & Lusardi, A. (2019). Financial literacy and financial resilience: Evidence from
around the world. Financial Management, 49(3), 589–614. doi:10.1111/fima.12283
Klapper, L. & Morduch, J. (2023, January 18). For a strong economic recovery, invest in
financial resilience. Retrieved June 29, 2023, from
https://www.weforum.org/agenda/2023/01/economic-recovery-financial-resilience-
world-bank-wef23/
Klapper, L. & Tayag, P. R. (2022, November 02). Responsible finance and its role in
improving financial resilience and well-being. Retrieved July 27, 2023, from
https://blogs.worldbank.org/developmenttalk/responsible-finance-and-its-role-
improving-financial-resilience-and-well-being
O'Neill, A. (2021, April 01). Philippines: Average age of the population from 1950 to 2020.
Retrieved April 19, 2021, from https://www.statista.com/statistics/578796/average-
age-of-the-population-in-philippines/
Oxford Business Group. (2020, December 16). The Report: Philippines 2021. Retrieved
September 28, 2023, from https://oxfordbusinessgroup.com/philippines-
2021/economy
Piza, S. F. A., Cho, Y., & Zapanta, A. M. F. S. (2021). Philippines COVID-19 High Frequency
Household Survey Round 2 (December 2020) Summary of Findings. Retrieved
August 11, 2023, from
https://thedocs.worldbank.org/en/doc/ab24c2a718fb53a344c5942d236b2fe6-
0070062021/philippines-covid-19-high-frequency-household-survey-round-2-
december-2020-summary-of-findings
Sahay, R., & Cihak, M. (2018). Women in Finance: A Case for Closing Gaps. Staff Discussion
Notes, 18(05), 1. doi:10.5089/9781484375907.006
Salignac, F., Marjolin, A., Reeve, R., & Muir, K. (2019). Conceptualizing and Measuring
Financial Resilience: A Multidimensional Framework. Social Indicators
Research, 145(1), 17-38. doi:10.1007/s11205-019-02100-4
Schumacher, S. & Kent, N. (2020). 8 charts on internet use around the world as countries
grapple with COVID-19. Retrieved August 7, 2023, from
https://www.pewresearch.org/short-reads/2020/04/02/8-charts-on-internet-use-
around-the-world-as-countries-grapple-with-covid-19/
Tiwari, T., Srivastava, A., & Kumar, S. (2019). Decision Tree: Categorizing Financial
Inclusion. International Journal of Recent Technology and Engineering Regular
Issue, 8(4), 10431-10435. doi:10.35940/ijrte.d8979.118419
Tjahjadi, A. M., & Ajani, J. (2018). Assessing Financial Inclusion in ASEAN Countries: Are We
Done Yet? [Paper presentation]. ASEAN Youth Conference, Malaysia.
https://www.researchgate.net/publication/331728531_Assessing_Financial_Inclusion
_in_ASEAN_Countries_Are_We_Done_Yet
Department of Economic Research | Discussion Paper Series No. xx Page 27 of 28

Unpacking the Determinants of Financial Resilience in the Philippines March 2024
World Bank. (2017, July 10). FAQs about the Pantawid Pamilyang Pilipino Program (4Ps).
Retrieved May 14, 2021, from
https://www.worldbank.org/en/country/philippines/brief/faqs-about-the-pantawid-
pamilyang-pilipino-program
World Bank. (2018, October 23). Global Financial Inclusion (Global Findex) Database 2017.
Retrieved July 11, 2023, from
https://microdata.worldbank.org/index.php/catalog/3311
World Bank. (2020). Philippines Economic Update December 2020 Edition (Publication).
Retrieved March 10, 2021, from World Bank website:
https://openknowledge.worldbank.org/bitstream/handle/10986/34899/Philippines-
Economic-Update-Building-a-Resilient-Recovery.pdf
World Bank. (2022, October 13). Global Financial Inclusion (Global Findex) Database 20121.
Retrieved July 11, 2023, from
https://microdata.worldbank.org/index.php/catalog/4607
World Bank. (2022). Overcoming poverty and inequality in the Philippines: Past, present,
and prospects for the future (Publication). Retrieved September 28, 2023, from
World Bank website:
https://openknowledge.worldbank.org/bitstream/handle/10986/38346/P17486101e2
9310810abaf0e8e336aed85a.pdf
Department of Economic Research | Discussion Paper Series No. xx Page 28 of 28