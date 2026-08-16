---
conversion_metadata:
  converted_at: "2026-07-21T08:07:17Z"
  converter_tool: "markitdown"
  converter_version: "0.1.6"
  source_pdf: "Percca.pdf"
  source_pdf_sha256: "f7b8905c29d201201c7669c2874b4248b80ef312bdb6428a56f2b2f7069824fd"
  page_count: 27
  markdown_char_count: 138887
---

<!-- PAGE-AWARE EXTRACTION (via pdfminer.six) -->

<!-- PAGE 1 -->

Unveiling the Financial Wellbeing Ecosystem: A Data-Driven Framework of Six Behavioral 
Profiles*

Preprint not peer reviewed

* Data Availability: The data used in this study are drawn from the 2021 National Financial Capability Study 
(NFCS),  sponsored  by  the  FINRA  Investor  Education  Foundation.  The  dataset  is  publicly  available  at 
[https://finrafoundation.org/nfcs-data-and-downloads]

This preprint research paper has not been peer reviewed. Electronic copy available at: https://ssrn.com/abstract=6826893

---

<!-- PAGE 2 -->

Abstract

Daniel Fernando Masias Percca, Universidad ESAN, Lima, Peru
Jr. Alonso de Molina 1652, Lima, Peru
dmasias@esan.edu.pe

Traditional  evaluations  of  financial  wellbeing  rely  on  unidimensional,  linear  indices  that 
overlook  the  complex  interaction  between  short-term  preparedness  and  long-term  security. 
This study proposes a novel intertemporal framework to capture the inherent heterogeneity of 
financial profiles through the integration of economic theory with machine learning techniques. 
Using data from the 2021 National Financial Capability Study (NFCS), a multi-stage pipeline 
is  implemented,  including  theory-driven  feature  engineering,  clustering  and  Random  Forest 
classification to identify and validate six distinct segments, ranging from "The Established" to 
"The  Distressed."  Our  findings  reveal  a  consistent  "Subjective  Dominance"  effect,  where 
individual  self-perception  significantly  outweighs  objective  metrics  and  cognitive  factors  in 
predicting wellbeing profiles. Furthermore, the analysis uncovers critical structural distinctions 
between vulnerable segments: while "The Short-Sighted" are primarily constrained by human 
capital deficits, "The Illiquid Planners" are destabilized by exogenous income shocks despite 
their  planning  capabilities.  These  results  challenge  the  efficacy  of  generalized  policy 
interventions and highlight the necessity of data-driven, psychologically informed strategies 
that account for the nuances of intertemporal trade-offs in personal finances.

Preprint not peer reviewed

Keywords – Financial wellbeing, financial literacy, financial fragility, financial stress

This preprint research paper has not been peer reviewed. Electronic copy available at: https://ssrn.com/abstract=6826893

---

<!-- PAGE 3 -->

Unveiling the financial wellbeing ecosystem: A data-driven framework of six behavioural 
profiles*

Preprint not peer reviewed

*  Data  availability:  The  data  used  in  this  study  are  drawn  from  the  2021  National  Financial  Capability  Study 
(NFCS),  sponsored  by  the  FINRA  Investor  Education  Foundation.  The  dataset  is  publicly  available  at: 
https://finrafoundation.org/nfcs-data-and-downloads.

This preprint research paper has not been peer reviewed. Electronic copy available at: https://ssrn.com/abstract=6826893

---

<!-- PAGE 4 -->

ABSTRACT

Keywords: Financial wellbeing, Financial literacy, Financial fragility, Financial stress

Traditional  evaluations  of  financial  wellbeing  rely  on  unidimensional,  linear  indices  that 
overlook  the  complex  interaction  between  short-term  preparedness  and  long-term  security. 
This study proposes a novel, intertemporal framework to capture the inherent heterogeneity of 
financial profiles through the integration of economic theory and machine learning techniques. 
Using data from the 2021 National Financial Capability Study (NFCS), a multi-stage pipeline 
is implemented, including theory-driven feature engineering, clustering, and Random Forest 
classification to identify and validate six distinct segments, ranging from “The Established” to 
“The  Distressed”.  The  findings  reveal  a  consistent  “subjective  dominance”  effect,  where 
individual  self-perception  significantly  outweighs  objective  metrics  and  cognitive  factors  in 
predicting wellbeing profiles. Furthermore, the analysis uncovers critical structural distinctions 
between vulnerable segments: while “The Short-Sighted” are primarily constrained by human 
capital deficits, “The Illiquid Planners” are destabilised by exogenous income shocks despite 
their  planning  capabilities.  These  results  challenge  the  efficacy  of  generalised  policy 
interventions and highlight the need for data-driven, psychologically informed strategies that 
account for the nuances of intertemporal trade-offs in personal finances.

Preprint not peer reviewed

Financial wellbeing can be defined as being and feeling in control of personal expenses, 
and demonstrating short-term preparedness and long-term security. According to Sticha et al. 
(2023), it refers to managing money to meet daily demands, but also considering a retirement

1. Introduction

This preprint research paper has not been peer reviewed. Electronic copy available at: https://ssrn.com/abstract=6826893

---

<!-- PAGE 5 -->

2

plan. This concept becomes noteworthy when both historical and recent events claim a strong 
relationship between socioeconomic status and ill-health, and even mortality. Evidence shows 
that general distress and mental illness are strongly driven by financial issues (Greene & Patil, 
2023).  Without  proper  management,  these  pathologies  impact  individuals’  quality  of  life, 
leading to a cycle of negative impacts on household welfare (Jiménez-Solomon et al., 2024).

The  research  landscape  acknowledges  a  clear  problem:  financial  wellbeing  lacks  an 
integral evaluation system, where its periodic nature and fundamental determinants are jointly 
recognised.  Previous  work  aimed  to  develop  compound  scales  with  a  multidimensional 
approach (Sticha et al., 2023). However, its subjective methodology complicates transparent 
interpretation. Authors such as Wagner and Walstad (2019) and Netemeyer et al. (2018) have 
formulated mathematical models to evaluate the effect of certain regressors on target variables. 
Nevertheless, not all critical determinants are considered, likely distorting the actual effect of 
the covariates.

Financial  wellbeing  has  heterogeneous  perspectives  towards  its  measurement  and 
evaluation.  A  common  definition  is  based  on  numerical  scores.  Although  granular,  these 
metrics  represent  an  over-simplification  of  an  individual's  wellbeing,  which  indeed  has 
multiple dimensions (Salignac et al., 2020). Furthermore, several efforts have also been made 
to evaluate its determinants. Objective metrics of financial profiles (e.g., income) were the first 
variables modelled, followed by the incorporation of subjective approximations (e.g., feelings 
towards  such  income).  More  recently,  financial  literacy  has  been  included  given  its  strong 
correlation  with  the  previous  two  concepts,  all  of  them  modelled  along  with  demographic 
features to control for contextual scenarios (Lusardi & Streeter, 2023).

Preprint not peer reviewed

Recognising  the  integral  nature  of  personal  finances  is  essential  for  maintaining 
economic balance and mitigating risks of neglecting critical areas such as health and education. 
In  addition,  understanding  the  underlying  drivers  behind  individuals'  financial  situations  is 
paramount  to  forecasting  effective  decisions  and  policies.  These  findings  hold  universal 
relevance for a broad spectrum of stakeholders: from ordinary citizens striving for financial 
autonomy,  to  policymakers  aiming  to  enhance  public  health,  and  non-governmental 
organisations  (NGOs)  dedicated  to  assisting  underrepresented  populations.  Ultimately,  this 
framework  serves  all  stakeholders  committed  to  strengthening  the  financial  wellbeing  of 
populations across decades and even generations.

This  study  aims  to  address  the  issue  by  designing  and  testing  a  holistic  financial 
wellbeing  framework.  The  proposed  framework  fulfils  both  theoretical  and  practical 
fragmentation in concept measurement and determinant evaluation. Accordingly, the focus is 
on establishing accurate profiles and analysing the reasons behind such differentiation. For this 
purpose,  the  study  follows  a  non-experimental,  quantitative  methodology,  supported  by 
descriptive  and  predictive  analyses.  The  central  evaluation  is  conducted  through  machine 
learning techniques due to their strong capacity to model complex variable interactions within 
an interrelated system.

Human health comprises a broad concept where mental and physical welfare are the 
central objective (World Health Organization, 2021). In this sense, financial wellbeing has been

2. Literature review

This preprint research paper has not been peer reviewed. Electronic copy available at: https://ssrn.com/abstract=6826893

---

<!-- PAGE 6 -->

3

Based on the above, financial wellbeing has emerged as an essential indicator of social 
stability  and  progress  (Brüggen  et  al.,  2017).  While  its  preservation  is  a  central  objective 
globally,  heterogeneous  conceptualisations  and  fragmented  operationalisations  continue  to 
obscure  a  transparent  understanding  (Mahendru  et  al.,  2022).  In  this  sense,  a  robust 
measurement and analysis of financial wellbeing is critical to mitigate systemic public health 
risks and foster long-term resilience (Salignac et al., 2020).

Regarding conceptualisation, the literature presents a range of perspectives drawing on 
economic foundations, technical definitions, and heuristic analogies, as discussed by Brüggen 
et al. (2017), Sorgente, Totenhagen, and Lanz (2022), and Sajid et al. (2024). These multiple 
approaches overcomplicate a general understanding. To overcome this issue, Sticha, Lusardi, 
and Sconti (2023) proposed a comprehensive definition, stating that “financial wellbeing is not 
only  about  long-term  financial  security  (retirement  planning)  but  also  about  short-term 
financial preparedness”. This contribution reinforces a previous approximation of Salignac et 
al. (2020), who concluded that a person is financially healthy when “they are in control of their 
finances and feel financially secure, now and in the future”.

extensively researched due to its impact on both health domains. Mental illness, chronic stress, 
and medical avoidance are some of the consequences of poor financial management (Spivak et 
al., 2019). For instance, in the United States, the effects of the COVID-19 pandemic revealed 
a surge in psychological pathologies among individuals experiencing income instability or job 
loss. Ringlein et al. (2024) found that, between 6 and 10 months following the onset March in 
2020, the psychological distress levels of those affected by income shocks were 9% higher than 
their stable-income counterparts. This disparity increased to 11% between months 25 to 29, 
suggesting a chronic mental health deterioration in the long-term. This divergence implies that 
the psychological burden of financial stress outlasted government interventions, highlighting a 
latent public health crisis.

Preprint not peer reviewed

The previous methodological heterogeneity is not limited to its measurement; it also 
extends  to  the  analysis  of  the  drivers  behind  financial  wellbeing  outcomes.  Research  on 
household financial wellbeing has normally been conducted considering income-based drivers, 
plus  demographic  controls  (Cardona-Montoya  et  al.,  2022).  For  instance,  studies  such  as 
Theodossiou  (1998)  were  focused  primarily  on  the  impact  of  low  wages  on  mental  health. 
Twenty years later, Dolan, Peasgood, and White (2008) presented an interesting contribution 
stating that happiness was more strongly influenced by relative income comparisons than by 
the actual income received by individuals. In other words, self-assessments towards one's own 
situation represent an indispensable factor on personal welfare. This finding explains the origin 
of the subjective-objective dichotomy and adds a second driver of financial wellbeing.

The previous foundation is critical for providing a complete measurement. Thus, the 
intertemporal  duality  of  financial  wellbeing  is  employed  in  this  study,  defining  it  as  the 
effective management of day-to-day expenses and proper budget planning for the future. As 
noted above, current measurements are solely based on one-dimensional scores or subjective 
compound metrics. Crucially, the majority of existing indices do not assess the intertemporal 
integrability  of  financial  wellbeing.  These  limitations  increase  the  risk  of  misguided 
conclusions  and  ineffective  interventions.  Given  the  above,  the  first  research  question  is 
formulated as follows:

Notably, a common feature among existing works is the acknowledgement of structural 
differences  reflected  in  demographic  variables.  In  this  sense,  Wagner  and  Walstad  (2019)

RQ1: How can financial wellbeing be measured within an intertemporal framework?

This preprint research paper has not been peer reviewed. Electronic copy available at: https://ssrn.com/abstract=6826893

---

<!-- PAGE 7 -->

4

3. Method

RQ2: What is the role of the entire set of financial wellbeing determinants?

suggest that both momentary and long-lasting circumstances must be considered, underscoring 
the significance of age, gender, income range, and marital status, among other variables.

More  recently,  Lusardi  and  Streeter  (2023)  concluded  that  financial  literacy  plays  a 
fundamental  role  in  shaping  money-management  practices  (subjective  perceptions)  and 
financial  decision-making  (objective  behaviour),  finding  a  strong  impact  on  financial 
wellbeing. This third variable complemented the set of determinants.

To address these research questions, this study adopts a robust quantitative approach. 
Specifically,  to  answer  RQ1,  an  index  construction  is  constructed  for  each  intertemporal 
dimension, followed by its consolidation into a comprehensive framework that presents a novel 
taxonomy  of  financial  wellbeing  profiles.  Subsequently,  to  address  RQ2  and  explore  the 
interplay  between  determinants,  a  machine  learning  algorithm  is  trained,  and  a  granular 
analysis is conducted on the role of each determinant.

Although several studies have tested the effects of these three determinants, they were 
mostly analysed in isolation. In this sense, financial wellbeing research still lacks an integral 
modelling where all the aforementioned drivers are jointly evaluated (subjective perceptions 
along with objective behaviours and financial literacy). By providing a robust model, a better 
understanding of financial wellbeing outputs, their causes and consequences is achieved. This 
contributes to conscious decisions and tailored actions. Given the above, the second research 
question is formulated as follows:

Preprint not peer reviewed

The methodology comprises a quantitative and non-experimental analyses, with a strong focus 
on  variable  interactions  within  the  created  framework.  This  research  is  based  on  the  2021 
National  Financial  Capability  Study  (NFCS),  a  strategic  dataset  to  analyse  the  COVID-19 
pandemic effects on population financial wellbeing (FINRA Investor Education Foundation, 
2021).  It  comprises  information  of  27,118  adults  from  the  United  States,  representing  a 
population of over 250 million. Of those, all observations which belong to retired individuals 
or lacking responses to key questions to estimate the model variables were excluded. In this 
sense, the final sample involves 11,857 observations. The strength of this dataset relies on its 
vast  amount  of  information  for  a  complete  analysis.  Financial  behaviours,  perceptions,  and 
education are covered, along with sociodemographic and contextual features.

The strategy employed to address the research questions follows a sequential, multi-
stage architecture. This is structured into three phases to ensure robustness and reproducibility. 
First, the research design and data sourcing are established to guarantee sample accuracy and 
representativeness  (Section  3.1).  Then,  a  rigorous  feature  engineering  is  conducted  to 
operationalise  the  intertemporal  measurements  and  determinants  of  financial  wellbeing 
(Section 3.2). Finally, the implementation and testing of the framework are detailed, describing 
the machine learning technique used to uncover the novel taxonomy (Section 3.3).

Based on the literature review, the dependent variable was built within an intertemporal 
framework. Following the method adapted from Wagner and Walstad (2019), eight items from 
the NFCS were selected to construct this measure. Specifically, four items are designated to

3.2. Variable construction and feature engineering

3.1. Research design, sample and data

This preprint research paper has not been peer reviewed. Electronic copy available at: https://ssrn.com/abstract=6826893

---

<!-- PAGE 8 -->

5

assess  short-term  (ST)  financial  control,  while  the  remaining  four  evaluate  long-term  (LT) 
financial security.

The short-term index is constructed using four questions shown in Table 1. These items 
are designed to capture the immediate cash-flow management and daily financial behaviours 
that define an individual’s financial stability. Following the framework proposed by Wagner 
and  Walstad  (2019),  four  key  dimensions  were  identified:  expense  management,  banking 
behaviour, credit discipline, and debt perception. Each item was binarised (1 = favourable, 0 = 
unfavourable)  using  a  “top-box”  criterion  to  isolate  optimal  financial  behaviours  (such  as 
paying credit cards in full or having no difficulty covering bills) from any degree of financial 
distress. This operationalisation allows the index to reflect clear distinctions between financial 
stability and vulnerability in the short-term.

To construct these two indices, a feature engineering process is employed, involving 
the binarisation and additive aggregation of the selected items. While dimensionality reduction 
techniques,  such  as  Principal  Component  Analysis  (PCA)  or  Multiple  Correspondence 
Analysis (MCA), are common in large datasets, feature engineering was preferred to preserve 
the theoretical interpretability and semantic integrity of the financial constructs. Unlike PCA, 
which  generates  latent  components  that  maximise  statistical  variance  but  often  lack  direct 
interpretation (Zytek et al., 2022; Karaahmetoğlu et al., 2025), this approach ensures that the 
resulting indices directly reflect the intertemporal duality of financial wellbeing, as defined in 
the literature. The detailed interpretation of the drivers, which purely statistical components 
might obscure, is key for actionable insights (Huston, 2010). In this sense, binarisation and 
aggregation enable the synthesis of variables from raw data while maintaining consistency with 
the objectives and preserving the dependencies within the model (Kuhn & Johnson, 2013).

Preprint not peer reviewed

The long-term index is measured by four questions shown in Table 2. These items focus on 
asset accumulation and future resilience, adapting the methodology of Wagner and Walstad

G23: How strongly do you agree or disagree 
with the following statement? - I have too much 
debt right now.

F2_1: In the past 12 months, which of the 
following describes your experience with credit 
cards? - I always paid my credit cards in full.

J4: In a typical month, how difficult is it for you 
to cover your expenses and pay all your bills?

B4: Do you [or your spouse/partner] overdraw 
your checking account occasionally?

Operationalisation and binary encoding of short-term financial wellbeing components

Note: Data from the 2021 National Financial Capability Study (NFCS).

No (Never occasionally 
overdraws)

Yes  (Always  paid  in 
full)

Strongly 
disagree/Disagree

Binarisation logic
(1 = favourable)

Expense 
management

Debt 
perception

Banking 
behaviour

Credit 
discipline

Not at all difficult

NFCS item

Construct

Table 1

This preprint research paper has not been peer reviewed. Electronic copy available at: https://ssrn.com/abstract=6826893

---

<!-- PAGE 9 -->

6

Table 2

Construct

NFCS item

(Maintains

Emergency 
resilience

Asset 
accumulation

Yes 
formal savings)

Liquidity/basic 
saving

Binarisation logic 
(1 = favourable)

Yes  (Has  3-month 
buffer)

Operationalisation and binary encoding of long-term financial wellbeing components

J5: Have you set aside emergency or rainy-day 
funds that would cover expenses for 3 months?

B14: Not including retirement, do you have any 
investments in stocks, bonds, or mutual funds?

B2:  Do  you  have  a  savings  account,  money 
market account, or CDs?

(2019) as well. They cover emergency resilience and formal liquidity, essential metrics to avoid 
financial  stress  during  economic  downturns  (Haveman  &  Wolff,  2005).  Furthermore, 
investment activities and retirement planning items are considered, which are critical for life-
cycle financial wellbeing (Lusardi et al., 2017). Consistent with the short-term index, all items 
are  binarised  using  a  threshold  of  proactive  financial  security.  Favourable  outcomes  reflect 
anticipatory  financial  actions  rather  than  mere  asset  ownership.  For  example,  retirement 
planning is defined by the active calculation of future needs rather than merely the existence 
of a retirement account.

Preprint not peer reviewed

The objective behaviour index is measured by the questions shown in Table 3. These 
items serve as a proxy for personal pillars for financial stability and security. The inclusion of 
the  income  threshold  at  the  $75,000  mark  aligns  with  established  literature  suggesting  that 
emotional stability tends to plateau beyond this income level (Kahneman & Deaton, 2010). 
Budgetary discipline is incorporated as a measure of active saving behaviour, reflecting the 
individual’s capacity for capital retention regardless of total earnings. Liquidity shock capacity 
represents the NFCS standard for assessing financial fragility. By isolating only those who are 
“totally  confident,”  this  index  applies  a  stringent  filter  for  immediate  financial  resilience 
(Lusardi  et  al.,  2011).  Finally,  the  index  accounts  for  institutional  coverage  and  credit  risk 
avoidance,  capturing  the  external  support  systems  and  the  avoidance  of  high-cost, 
unsustainable debt.

Subsequently,  the  independent  variables  are  defined,  representing  the  entire  set  of 
critical  determinants  of  financial  wellbeing.  This  approach  comprises  objective  behaviours, 
subjective perceptions, financial literacy, and demographic characteristics. Twenty-six items 
were  selected  from  the  NFCS  to  construct  these  measures.  Specifically,  five  items  were 
designed to assess the objective behaviour, five to evaluate the subjective perceptions, seven 
to  measure  financial  literacy,  and  nine  to  reference  the  individuals’  demographic 
characteristics.

J8: Have you ever tried to figure out how much 
you need to save for retirement?

Note. Data from the 2021 National Financial Capability Study (NFCS).

Yes  (Has  calculated 
retirement needs)

Retirement 
planning

Yes 
investor)

Table 3

(Active

This preprint research paper has not been peer reviewed. Electronic copy available at: https://ssrn.com/abstract=6826893

---

<!-- PAGE 10 -->

7

=

is

(>

(has

high

your

budget

surplus

income

covered

Construct

NFCS item

household's

liquidity 
(totally

Income 
threshold

Budgetary 
discipline

Institutional 
coverage

1  =  high 
$75,000)

Credit  risk 
avoidance

Liquidity 
shock 
capacity

= 
1 
confidence 
confident)

Binarisation logic 
(1 = favourable)

1  = 
(spending < income)

1 
employer-sponsored plan)

1  =  safe  credit  behaviour 
(never)

A8_2021:  What 
approximate annual income?

Note: Data from the 2021 National Financial Capability Study (NFCS).

Operationalisation and binary encoding of objective behaviour components

G25_1:  In  the  past  5  years,  how  many  times 
have you taken out an auto title loan?

J20:  How  confident  are  you  that  you  could 
come up with $2,000 for an unexpected need?

J3: Was your household's spending less than, 
more than, or equal to your income?

C1_2012:  Do  you  have  any  retirement  plans 
through an employer (e.g., pension)?

Preprint not peer reviewed

The subjective perception index is measured by the questions shown in Table 4. The 
abbreviated version of the Consumer Financial Protection Bureau (CFPB) scale was employed 
for  this  purpose.  This  validated  index  captures  the  psychological  dimension  of  financial 
wellbeing, moving beyond mere solvency to measure individuals’ internal sense of security 
and freedom. Unlike the previous indices, these items were not binarised; instead, a two-step 
transformation process was applied. First, raw responses were coded on a 0–4 scale depending 
on  their  wellbeing  phrasing.  Second,  the  cumulative  scores  were  mapped  onto  the  official 
CFPB Conversion Table to produce a final standardised score ranging from 0 to 100. Following 
the CFPB technical protocol, negatively phrased items were reverse-coded to ensure that higher 
values consistently reflect greater levels of perceived wellbeing.

How well do these statements describe you? Because 
of my money situation, I feel like I will never have 
the things I want in life.

How well do these statements describe you?
I am just getting by financially.

Operationalisation and binary encoding of subjective perception components

Negatively phrased
0 = completely
4 = not at all

Negatively phrased
0 = completely
4 = not at all

Financial 
sufficiency 
perceptions

Long-term 
goal 
attainment

Scoring 
methodology

NFCS item

Construct

Table 4

This preprint research paper has not been peer reviewed. Electronic copy available at: https://ssrn.com/abstract=6826893

---

<!-- PAGE 11 -->

8

Table 5

Future 
security 
anxiety

Perceived 
financial 
agency

Monthly 
budgetary 
margin

Positively phrased
4 = always
0 = never

Negatively phrased
0 = always
4 = never

Negatively phrased
0 = completely
4 = not at all

Note: Data from the 2021 National Financial Capability Study (NFCS).

How often do these statements apply to you?
My finances control my life.

How often do these statements apply to you?
I have money left over at the end of the month.

How well do these statements describe you?
I  am  concerned  that  the  money  I  have  or  will  save 
won't last.

The financial literacy index is measured by the questions shown in Table 5. This index 
measures the cognitive foundation of financial decision-making. Following the work of Lusardi 
and Mitchell (2011), the index incorporates the “Big Three” concepts (interest rates, inflation, 
and  risk  diversification),  alongside  more  advanced  topics  such  as  bond  pricing,  mortgage 
structures, compound interest, and probabilistic reasoning. These items serve to differentiate 
between  basic  numeracy  and  functional  financial  knowledge.  Each  item  was  binarised  (1  = 
correct, 0 = incorrect/do not know), creating a cumulative scale that ranges from 0 to 7.

Preprint not peer reviewed

A 15-year mortgage typically requires higher monthly 
payments  than  a  30-year  mortgage,  but  the  total 
interest paid over the life of the loan will be less.

Suppose you had $100 in an account with an interest 
rate of 2% per year. How much would you have after 
five years if you left the money to grow?

Imagine that the interest rate on your account was 1% 
per year and inflation was 2% per year. After 1 year, 
how much would you be able to buy with the money?

Suppose you owe $1,000 on a loan and the interest rate 
is  20%  per  year  compounded  annually.  If  you  didn't

If interest rates rise, what will typically happen to bond 
prices?

Buying  a  single  company's  stock  usually  provides  a 
safer return than a stock mutual fund.

Operationalisation and binary encoding of financial literacy components

Binarisation logic 
(1 = correct answer)

Numeracy/inte
rest

Risk 
diversification

Compound 
interest

Mortgage 
literacy

Inflation 
awareness

Bond 
valuation

1 = more than $102

1 = less than today

1 = they will fall

1 = 2 to 5 years

NFCS item

Construct

1= false

1= true

This preprint research paper has not been peer reviewed. Electronic copy available at: https://ssrn.com/abstract=6826893

---

<!-- PAGE 12 -->

9

indicates

the  highest

1 = one-in-twenty

Probabilistic 
reasoning

3.3. Implementation of the financial wellbeing framework

Note: Data from the 2021 National Financial Capability Study (NFCS).

the  following 
Which  of 
probability of getting a particular disease?

pay anything off, at this interest rate, how many years 
would it take for the amount you owe to double?

Lastly,  nine  demographic  and  socioeconomic  variables  are  integrated  as  control 
features  to  account  for  individual  heterogeneity  in  financial  outcomes.  These  include  age 
group,  gender,  educational  attainment,  household  income,  number  of  dependent  children, 
income  shocks,  secondary  employment,  labour  status,  and  marital  status.  All  of  them  were 
extensively  employed  in  previous  work,  such  as  the  studies  of  Lusardi  and  Streeter  (2023), 
Sticha, Lusardi, and Sconti (2023), and Wagner and Walstad (2019). The ordinal structure of 
age,  education,  income,  and  number  of  dependants  was  preserved  to  capture  the  inherent 
gradients in these dimensions. Conversely, the nominal variables were all transformed using 
one-hot  encoding.  This  process  generates  distinct  binary  indicators  for  each  category, 
preventing the model from assuming a non-existent hierarchy among nominal labels. A detailed 
description of each indicator and its corresponding measurement scale is provided in the Online 
Appendix (Fig. B.1).

Preprint not peer reviewed

Based on the previously constructed indices, the dependent variable was derived from 
a cross-tabulation of the short-term (ST) and long-term (LT) scales. As illustrated in Fig. 1, 
this bivariate approach maps the intertemporal framework of financial wellbeing, resulting in 
a 5x5 matrix with twenty-five distinct cells. This spatial representation allows for a granular 
identification of financial profiles. The bottom-left quadrant identifies individuals experiencing 
concurrent fragility in both ST and LT dimensions, whereas the top-right quadrant characterises 
those  exhibiting  strong  intertemporal  security.  Consequently,  this  matrix  serves  as  the 
structural  basis  for  operationalising  the  financial  wellbeing  profiles,  thereby  defining  the 
model's dependent variable.

With  both  the  dependent  and  independent  variables  constructed,  a  supervised 
classification model was implemented to simultaneously validate the proposed framework and 
analyse  the  financial  wellbeing  of  U.S.  adults.  Two  models  are  estimated  for  this  purpose. 
Equation  (1)  represents  the  model  without  control  variables,  and  Equation  (2)  adds  the 
demographic controls. Both models are presented below:

𝑌𝑖 is the dependent label value for individual “i”
X1,i is the independent index value of subjective perception for individual “i”
X2,i is the independent index value of objective behaviour for individual “i”

𝑌𝑖 = 𝑓( X1,i + X2,i + X3,i +  𝒁𝒊)  + ϵi

𝑌𝑖 = 𝑓( X1,i + X2,i + X3,i)  + ϵi

where:

(2)

(1)

This preprint research paper has not been peer reviewed. Electronic copy available at: https://ssrn.com/abstract=6826893

---

<!-- PAGE 13 -->

10

X3,i is the independent index value of financial literacy for individual “i”
Zi is the set of demographic controls for individual “i”
𝜖i is the random error term for individual “i”

The  Random  Forest  implementation  in  this  study  follows  a  principled  approach  for 
hyperparameter tuning (Breiman, 2001; James et al., 2023). The number of trees is set to 100, 
sufficient for the out-of-bag error to converge. The number of features at each node split is set 
to  the  square  root  of  the  number  of  predictors,  a  common  heuristic  to  reduce  correlation 
between  trees.  These  choices  target  the  main  sources  of  ensemble  variance  and  bias.  The 
remaining hyperparameters were kept at their default values to avoid overfitting and ensure a 
reproducible baseline framework.

The algorithm selected is Random Forest (RF) due to its superior capacity to handle 
heterogeneous  data  types  and  capture  the  nonlinear  relationships  inherent  in  socioeconomic 
data (Wright & König, 2019). As an ensemble method that aggregates multiple decision trees, 
RF is robust against outliers and multicollinearity (Kuhn & Johnson, 2013), making it suitable 
for the complex behavioural interactions within financial datasets. By adopting this approach, 
the study provides an empirical validation of the bi-dimensional framework presented in Fig. 1. 
The dataset is then partitioned into training (80%) and testing (20%) subsets to ensure out-of-
sample  evaluation.  To  address  class  imbalance,  the  Synthetic  Minority  Over-Sampling 
Technique (SMOTE) is applied exclusively to the training sample.

Preprint not peer reviewed

Model  performance  was  evaluated  using  a  robust  set  of  out-of-bag  measure  error 
estimates.  While  global  accuracy  and  the  confusion  matrix  provided  a  baseline  for  overall 
model  validity,  the  analysis  prioritised  precision  and  recall  (sensitivity)  to  ensure  a  proper 
assessment of the classifier's performance across heterogeneous segments. Given the inherent 
class imbalance within the financial wellbeing clusters, these last two metrics were prioritised 
for minority classes. This multi-metric approach ensures that the framework’s predictive power 
is  consistently  validated,  even  for  underrepresented  populations  within  the  NFCS  dataset. 
Furthermore, the inclusion of feature importance metrics enables an analysis of the primary 
drivers  of  financial  wellbeing,  ensuring  that  the  model  fulfils  both  the  classificatory  and 
diagnostic objectives of this research.

The  development  of  the  intertemporal  framework  reveals  a  complex  landscape  of 
financial wellbeing that linear models often obscure. This section presents the findings in three 
stages.  First,  a  novel,  six-clusters  taxonomy  is  established  to  measure  the  U.S.  population 
across  the  short-term  and  long-term  spectrum.  Second,  the  most  important  determinants  in 
shaping  financial  wellbeing  are  identified  through  the  Global  Random  Forest  classification. 
Finally, an original examination of “boundary dynamics” is presented, identifying the specific 
drivers that differentiate adjacent clusters, thus offering granular insights into the mechanisms 
of financial mobility.

Fig. 1 shows that the intertemporal framework is not distributed uniformly. While a 
significant density of observations (n) clusters in the high-performance quadrant (indicating 
intertemporal synergy), distinct pockets of vulnerability emerge in the lower bounds and off-
diagonal axes. Following the segmentation logic applied by Azevedo et al. (2024) in social 
science research, this study prioritises a clear distinctiveness over equally sized groupings. The 
objective  is  not  to  create  statistical  quartiles,  but  to  isolate  relevant  profiles  that  exhibit

4.1. New taxonomy of financial wellbeing

4. Results

This preprint research paper has not been peer reviewed. Electronic copy available at: https://ssrn.com/abstract=6826893

---

<!-- PAGE 14 -->

11

contrasting financial realities. Consequently, the 25-cell matrix was synthesised into six distinct 
clusters, forming a new taxonomy of financial wellbeing.

Preprint not peer reviewed

Fig. 1. The intertemporal financial wellbeing framework: identification of six distinct profiles. 
Note: The framework illustrates the six distinct profiles identified through the intersection of 
the short-term and long-term indices.

Cluster 1: The Established (C1). This group reaches the highest level of financial health. It 
is characterised by strong liquidity management in the present and robust capital planning for 
the future.

Drawing  on  the  spatial  configuration  presented  above,  the  proposed  framework 
delineates  distinct  profiles  with  unique  intertemporal  combinations,  ranging  from  robust 
stability to systemic vulnerability. The specific cluster characteristics are detailed below.

Cluster  2:  The  Resilient  (C2).  This  segment  demonstrates  moderate  control  over  current 
finances and adequate future security, but it has sub-optimal financial habits.

Cluster 3: The Short-Sighted (C3). This 
consumption satisfaction but shows deficient long-term preparedness.

cluster  maintains

adequate

liquidity

and

This preprint research paper has not been peer reviewed. Electronic copy available at: https://ssrn.com/abstract=6826893

---

<!-- PAGE 15 -->

12

Cluster  6:  The  Distressed  (C6).  This  segment  occupies  the  lower  tier  of  financial  health, 
revealing immediate liquidity crises and minimal safety for the future.

Cluster 4: The Illiquid Planners (C4). In contrast to C3, this group has managed to construct 
a substantial future budget, but struggles to fund its day-to-day demands.

Cluster 5: The Precarious (C5). This segment presents a latent risk, marked by instability and 
lack of control of their finances. They are theoretically solvent, but vulnerable in practice to 
any kind of income shock.

The descriptive analysis of the three core determinants across the six identified clusters 
is presented in Fig. 2. A progressive gradient is evident. Cluster 1 (C1) exhibits the highest 
mean scores across all dimensions, justifying its label as The Established, while the indicators 
steadily  decrease  until  reaching  the  lowest  scores  within  The  Distressed  (C6).  Intermediate 
clusters reveal distinct differences in determinants, yet substantial heterogeneity in outcomes. 
A more granular analysis of this critical differentiation is presented in Section 4.3.

Preprint not peer reviewed

Beyond  the  heterogeneity  evidenced  in  Fig.  1,  clear  socioeconomic  and  structural 
differences  emerge  among  the  six  clusters,  and  their  acknowledgement  supports  a  granular 
understanding of such profiles. Detailed distributions of these demographic characteristics are 
presented in Online Appendix B. Education and income among The Established (C1) play a 
fundamental role within this segment. A significant portion of individuals with postgraduate 
degrees (47.1%) and individuals with annual earnings above $300,000 (72.5%) are located in 
C1. In contrast, within The Distressed (C6), 79.7% have not attained an undergraduate degree 
and  66.1%  earn  less  than  $50,000  annually  (Figs.  B.2-B.3).  A  gender  gap  is  also  evident.

Fig. 2. Multidimensional profiling of financial wellbeing clusters: a comparative analysis of 
key  determinants.  Note:  The  chart  displays  the  normalised  average  scores  for  each  cluster, 
rescaled to 0-100% relative to the theoretical range of each index. Values closer to the periphery 
indicate a higher prevalence of the attribute.

This preprint research paper has not been peer reviewed. Electronic copy available at: https://ssrn.com/abstract=6826893

---

<!-- PAGE 16 -->

13

4.2. Global determinants of financial wellbeing

Females are disproportionately represented in the less healthy segment, comprising 69.4% of 
The  Distressed,  whereas  males  dominate  the  most-healthy  cluster  reaching  57.8%  of  The 
Established (Fig. B.4).

Regarding the lifecycle hypothesis of Wagner and Walstad (2018), financial wellbeing 
generally  improves  with  age,  suggesting  that  financial  maturity  and  prudence  develop  over 
time (Fig. B.5). An exogenous incident, based on the COVID-19 pandemic effects, was critical 
for group demarcation. Only 12% of The Established reported an income disruption, compared 
with an average of 48.6% among the vulnerable clusters (The Illiquid Planners, The Precarious, 
and The Distressed) (Fig. B.6).

Finally,  family  composition  and  marital  status  indicate  no  global  patterns;  however, 
they are relevant for clusters with intertemporal biases, such as The Short-Sighted (C3) and 
The Illiquid Planners (C4). There is a significantly higher proportion of dependent children 
within  C4,  compared  with  C3,  reaching  a  difference  of  31.6%.  This  suggests  that  family 
demands  constrain  liquidity  for  daily  expenses.  Moreover,  The  Short-Sighted,  largely 
composed  by  non-partnered  individuals  (59.7%  belong  to  single,  separated,  divorced,  or 
widowed  statuses),  may  direct  income  flows  toward  required  immediate  consumption, 
preventing long-term savings (Figs. B.7-B.8).

Preprint not peer reviewed

After the initial diagnostic analysis, the stepwise Random Forest application provides 
both confirmatory and novel findings. Two models are estimated: Model 1 is the baseline, with 
only the three core determinants (objective, subjective, and literacy scales), while Model 2 adds 
the sociodemographic controls. The results, summarised in Table 6, show an expected insight: 
the  inclusion  of  contextual  and  personal  characteristics  is  critical  to  capture  the  variance  in 
financial  wellbeing  outcomes.  Model  2  improves  the  accuracy  from  0.37  to  0.46,  with 
consistent gains in precision and recall metrics. This enhanced performance validates previous 
studies, such as Wagner and Walstad (2019), Lusardi and Streeter (2023), and Sticha, Lusardi, 
and  Sconti  (2023),  which  established  that  an  individual's  contextual  environment  deeply 
influences their financial wellbeing.

Comparative  performance  of  Random  Forest  models:  baseline  determinants  vs.  full 
demographic model

Precision
C1
C2
C3
C4
C5
C6

0.66
0.38
0.14
0.27
0.40
0.31

0.70
0.38
0.08
0.15
0.33
0.28

Accuracy

Table 6

Model 1

Model 2

0.3689

0.4557

Metric

This preprint research paper has not been peer reviewed. Electronic copy available at: https://ssrn.com/abstract=6826893

---

<!-- PAGE 17 -->

14

Metric

Model 1

Model 2

0.64
0.18
0.23
0.32
0.20
0.46

0.70
0.31
0.12
0.33
0.44
0.34

Recall
C1
C2
C3
C4
C5
C6

Note: Accuracy indicates overall model performance, whereas precision and recall provide a 
granular assessment of each cluster, controlling for class-size disparities.

Beyond the classification metrics, the feature importance analysis provides surprising 
findings into the determinants structure. Table 7 presents a ranking analysis for both models. 
Even though there is a slight variation in variable significance between the two models, the 
Subjective  Index  emerges  as  the  paramount  classifier,  exhibiting  superior  predictive 
importance  compared  with  the  Objective  Index  and  the  Financial  Literacy  Index.  This 
hierarchy evidences that individuals’ internal sense of preparedness and security (their mindset) 
is more important than their actual financial behaviours and habits (their actions). Regarding 
the demographic features, results for age and education level confirm the previous descriptive 
analyses, indicating that financial health involves life-cycle dynamism, with education acting 
as a strong differentiator.

Preprint not peer reviewed

The inclusion of sociodemographic controls allows the model to classify with higher 
accuracy.  Nevertheless,  the  confusion  matrix  shown  in  Table  8  reveals  persistent 
misclassification between adjacent clusters. Particularly, individuals among the intermediate 
clusters,  The  Short-Sighted  (C3),  The  Illiquid  Planners  (C4),  and  The  Precarious  (C5),  are 
likely to overlap because of their similar characteristics. Likewise, The Established (C1) are

Note:  Higher  ranking  indicates  a  greater  predictive  contribution  of  the  variable  in 
distinguishing financial wellbeing profiles.

Random Forest feature importance (FI): hierarchy of financial wellbeing determinants

Subjective Index

Subjective Index

Education Level

Objective Index

Objective Index

Literacy Index

Literacy Index

FI Ranking

Age Group

Model 1

Model 2

Table 7

4

2

3

5

1

This preprint research paper has not been peer reviewed. Electronic copy available at: https://ssrn.com/abstract=6826893

---

<!-- PAGE 18 -->

15

6

8

3

2

6

8

7

18

85

32

30

25

79

56

22

69

29

89

80

33

15

15

46

66

48

26

27

46

64

27

25

14

10

37

14

26

28

12

14

35

28

14

18

24

71

44

44

55

33

29

13

31

55

87

C6

C5

C4

C3

C2

C6

C5

C4

C3

C2

C1

C6

C5

C4

C3

C2

C1

C1

C6

C5

C4

C3

C2

C1

199

127

110

105

194

193

128

125

111

168

151

546

102

498

Model 2

Model 1

Table 8

Confusion matrix: analysis of inter-cluster misclassification patterns

Note:  Rows  represent  the  actual  (true)  cluster  membership,  while  columns  represent  the 
predicted classification by both models.

frequently misclassified as The Resilient (C2), and vice versa. This phenomenon was expected, 
as previous work suggests that financial wellbeing modelling is indeed complex, where similar 
determinants may result in different outcomes (Dolan et al., 2008; Lusardi & Streeter, 2023). 
Ultimately, the heterogeneity among individual profiles within each cluster underscores that 
there is not a unique or infallible determinant, neither at the personal nor at the contextual level.

Preprint not peer reviewed

Previous analyses suggest that global determinants delineate the broad framework for 
financial wellbeing. However,  they  obscure the specific  drivers that prevent  social  mobility 
across  adjacent  clusters.  To  identify  these  “levers  of  change”,  a  new  strategy  is  adopted  by 
isolating the decision boundaries between key segments. This is implemented through three 
binary  Random  Forest  classifications,  the  results  of  which  are  presented  in  Table  9.  The 
granular analysis reveals that financial wellbeing determinants shift according to the location 
of the individual within the intertemporal framework.

Subjective Index
Income Shock
Literacy Index
Education Level
Dependent Children

Subjective Index
Literacy Index
Education Level
Objective Index
Age Group

Subjective Index
Literacy Index
Objective Index
Age Group
Education Level

Pairwise discriminant analysis: evaluation metrics across adjacent clusters

4.3. The dynamics of mobility: boundary analysis

Feature importance

Pair C5 - C6

Pair C1 - C2

Pair C3 - C4

Accuracy

Table 9

1
2
3
4
5

0.6426

0.7030

0.7932

Metric

18

74

62

5

This preprint research paper has not been peer reviewed. Electronic copy available at: https://ssrn.com/abstract=6826893

---

<!-- PAGE 19 -->

16

The “survival gradient analysis” behind The Precarious (C5) and The Distressed (C6)

The “mismatch analysis” behind The Short-Sighted (C3) and The Illiquid Planners (C4)

Note: Results are derived from distinct Random Forest applications on each specified pair of 
clusters. Higher ranking of feature importance indicates a greater predictive contribution of the 
variable in distinguishing financial wellbeing profiles.

The intertemporal imbalance of these clusters indicates a critical policy insight. Both 
segments  present  bias,  however,  the  discrimination  is  not  entirely  behavioural,  but  event-
driven.  The  binary  classification  (accuracy:  0.79)  reveals  that  they  represent  structurally 
different populations influenced by opposing forces.

The  Random  Forest  identifies  Subjective  Index  and  Income  Shock  as  the  top-tier 
differentiators, as shown in the first column of Table 9. Notably, 58% of The Illiquid Planners 
experienced  a  recent  income  disruption,  compared  with  16.6%  of  The  Short-Sighted.  This 
suggests that C4 weakness does not lie in poor financial habits, but rather in liquidity hardship 
due to exogenous events, including job loss and business failure. This erosion of C4 short-term 
stability, despite their long-term assets, is also impacting on their self-assessment, leading to 
an  unusual  decline  in  its  Subjective  Index.  Conversely,  the  friction  in  The  Short-Sighted  is 
structural  and,  mainly,  educational.  Only  28.9%  of  C3  hold  a  bachelor’s  degree  or  higher, 
leading  to  a  human  capital  gap  compared  with  their  same-age  peers.  Their  lack  of  future 
preparedness is also exacerbated by their low Financial Literacy Index, meaning a significant 
systematic  risk.  This  distinction  implies  that  C4  requires  safety  nets  such  as  insurance, 
emergency  liquidity,  or  temporary  government  funding,  while  C3  requires  structural 
interventions in financial literacy and general education.

Preprint not peer reviewed

At the top of the framework, composed of C2 and C1, the driver of differentiation shifts 
from “survival” to “optimisation”. The boundary between The Established and The Resilient 
is not driven by shocks or income alone, but by marginal gains resulting from cognitive and 
maturity alignment, as shown in Fig. 2 and the third column of Table 9. C1 individuals exhibit 
a  "synergistic  advantage"  with  higher  literacy  (+2.03  points),  markedly  better  subjective 
perception  (+8.88  points),  and  older  age  (maturity  effect).  Specific  details  regarding  this 
differentiation are presented in the Online Appendix (Fig. B.9). This suggests that transitioning 
from  “middle  class”  to  “wealthy  established”  is  an  evolutionary  process  driven  by  the 
accumulation of assets and confidence over the lifecycle, with financial education playing a 
significant mediating role.

Analysing  the  vertical  transitions  at  the  framework  extremes  reveals  a  different 
dynamic. At the bottom of the framework, comprising C5 and C6, the distinction is driven by 
a “poverty trap” mechanism. Fig. 2 and the second column of Table 9 show that The Distressed 
are  separated  from  The  Precarious  by  a  set  of  aggravated  negative  indicators.  They  exhibit 
consistently lower financial literacy, lower general education, more negative perceptions, and, 
crucially,  greater  exposure  to  income  shocks  (49.2%  vs.  38.7%).  In  this  low-level  zone, 
mobility  is  largely  shaped  by  an  accumulation  of  disadvantages,  likely  exacerbated  by  the 
consequences of COVID-19.

The empirical identification of six distinct profiles challenges the traditional view of 
financial  wellbeing  as  a  linear  and  unidimensional  construct.  By  revealing  the  structural

The “optimisation gradient analysis” behind The Resilient (C2) and The Established (C1)

5. Discussion

This preprint research paper has not been peer reviewed. Electronic copy available at: https://ssrn.com/abstract=6826893

---

<!-- PAGE 20 -->

17

5.1. Theoretical implications: beyond the linear paradigm

heterogeneity  among  U.S.  households,  this  study  demonstrates  that  financial  wellbeing  is 
driven by the dynamic interplay between present stability and future security. The following 
sections  discuss  the  implications  of  these  findings:  first,  the  theoretical  necessity  of 
transcending  to  robust,  comprehensive  frameworks  (Section  5.1);  and  second,  the  practical 
shift from generic interventions to tailored and data-driven policies (Section 5.2).

This study expands the literature on financial wellbeing by shifting the analytical scope 
from  linear  and  independent  models  to  a  multidimensional  and  intertemporal  framework. 
Previous research has largely employed continuous gradients (Lusardi & Streeter, 2023; Sticha 
et al., 2023); however, this study confirms that financial wellbeing is better understood as a 
heterogeneous system of behavioural-structural clusters.

Specifically, this analysis provides strong support for Netemeyer et al. (2018) regarding 
the importance of subjective perceptions. A critical insight from this study is the “subjective 
dominance  effect”,  whereby  an  individual’s  self-assessment  plays  a  pivotal  role  in  their 
position within the framework, even more than their objective behaviours or literacy levels. 
This suggests that psychological strain is not merely an outcome of financial wellbeing, but a 
structural driver that can shift individuals into lower wellbeing clusters or propel them upward. 
This creates a feedback loop in which negative perceptions, aggravated by income shocks, can 
paralyse decision-making, even among literate individuals, as observed in The Illiquid Planners 
(C4).  The  previous  insight  complements  and  expands  the  cyclical  phenomenon  of  financial 
wellbeing and mental health acknowledged by Jiménez-Salomon et al. (2024).

Preprint not peer reviewed

Furthermore,  this  research  enriches  the  foundational  work  of  Lusardi  and  Streeter 
(2023) and Wagner and Walstad (2019). Although the well-known “Big Three” questions used 
to  measure  financial  literacy  constitute  a  validated  metric,  this  study  demonstrates  that 
expanding  the  scale  to  capture  more  complex  concepts  is  critical.  A  novel  finding  of  this 
research is that, while basic literacy is necessary for shifts between intermediate clusters (e.g., 
from C5 to C4), mastery of advanced financial knowledge acts as the gatekeeper to the highest 
wellbeing tiers (C1 shows a significant, unusual leap in its Literacy Index compared with C2 
and  the  other  clusters).  Similarly,  the  present-future  dichotomy  in  financial  wellbeing 
measurement cannot be analysed in isolation as it obscures the intertemporal foundation for 
individuals  profiling.  This  research  highlights  that  a  multidimensional  analysis  provides 
valuable insights for uncovering latent risks and optimisation opportunities, which are key to 
effective policy design.

The Distressed (C6) and The Precarious (C5) require an income stabilisation mechanism and 
social  protection  strategies,  rather  than  purely  literacy  programmes,  which  are  likely  to  be 
insufficient and misdirected. Data indicate that their financial fragility is driven by a systematic 
lack of resources, rather than an absence of a money-management guide. For individuals in this 
segment,  food  security  and  humanitarian  transfers  are  essential  to  prevent  a  compounding

The heterogeneity revealed by the six-cluster framework classification argues against a 
unique,  conventional  policy  intervention.  Effective  decisions  require  a  data-driven  triage 
tailored to the specific needs of each group. Based on the insights of this study, a three-tiered 
policy intervention is proposed.

5.2. Policy and managerial implications: from generic to precise decision-making

Tier 1: The structural-based intervention for the vulnerable segments: C5 and C6

This preprint research paper has not been peer reviewed. Electronic copy available at: https://ssrn.com/abstract=6826893

---

<!-- PAGE 21 -->

18

-

-

that this research offers to policymakers for effective intervention.

Tier 2: The equilibrium-based intervention for the middle segments: C3 and C4

Tier 3: The preservation-based intervention for the secure segments: C1 and C2

Distinguishing The Short-Sighted from The Illiquid Planners is a significant contribution

effect of multidimensional deprivation (Lee, 2023). With the aim of avoiding a positional drop 
from  C6  to  C5,  educational  interventions  are  also  needed,  focusing  on  survival  financial 
management, where fraud prevention and excessive debt avoidance should be prioritised given 
their vulnerable social situation.

For  The  Short-Sighted  (C3),  their  deficit  in  both  general  and  financial  education 
demands  priority  literacy  interventions  through  mandatory  curricular  modifications 
with a strong focus on long-term financial awareness. Conversely, the adults who are 
no longer part of the traditional education system, a commitment contract strategy is an 
effective tool to “force” individuals to enrol in saving plans and counteract their present 
bias (Halpern et al., 2012).
For The Illiquid Planners (C4), their deficit in contingency planning requires deliberate 
preparation  through  appropriate  financial  instruments.  Better  financial  education 
translates into greater knowledge for this cluster. A policy should focus on resilience 
instruments,  such  as  unemployment  insurance  or  highly  liquid  savings,  reducing  the 
investment on illiquid assets (e.g., real estate or long-term bonds). This strategy allows 
an immediate availability of resources when exogenous shocks occur.

Preprint not peer reviewed

Beyond the theoretical novelty of the framework, the primary practical contribution is 
the identification of the “subjective dominance effect”, “imbalance drivers”, and the “advanced 
literacy threshold”. These results challenge traditional beliefs by demonstrating that subjective 
perceptions of personal finances are the core driver behind wellbeing segmentation, rather than 
material possessions or financial education. This finding suggests that psychological factors 
act as structural determinants that can either amplify or limit material and cognitive benefits. 
Furthermore,  while  general  education  strengthens  long-term  security,  advanced  financial 
proficiency (mastery of complex instruments) is a prerequisite for accessing top-tier financial 
profiles, acting as a barrier to entry for the middle class.

For the high-performing segments, specifically The Resilient (C2) and The Established 
(C1), the strategy should focus on wealth preservation and financial literacy upgrades. Since 
C1  exhibits  privileged  knowledge  of  complex  and  advanced  financial  concepts,  including 
probabilistic and compound interest calculations, the intervention should focus on leveraging 
C2  financial  abilities  to  promote  an  upgrade  in  their  financial  profile.  Otherwise,  given  a 
demographic  profile  skewed  toward  older  and  wealthier  individuals,  another  policy  should 
focus on pension maintenance by facilitating low-fee, fiduciary financial advice to avoid capital 
erosion, which is fundamental for a healthy retirement period.

This research advances the measurement of financial wellbeing by moving from linear, 
single-score indices to a comprehensive and replicable framework. Through the application of 
a  Random  Forest  algorithm  to  a  nationally  representative  sample,  financial  wellbeing 
measurement  is  validated  as  a  complex  ecosystem  consisting  of  six  distinct  profiles,  where 
intertemporal  connections  between  short-term  preparedness  and  long-term  security  provide 
significant insights.

6. Conclusion

This preprint research paper has not been peer reviewed. Electronic copy available at: https://ssrn.com/abstract=6826893

---

<!-- PAGE 22 -->

19

Crucially,  the  distinction  between  The  Short-Sighted  (C3)  and  The  Illiquid  Planners 
(C4)  resolves  a  critical  ambiguity  in  the  current  literature.  While  both  clusters  exhibit 
vulnerability, the underlying drivers are fundamentally different. C3 is constrained by human 
capital deficits and behavioural myopia, while C4 is destabilised by exogenous shocks. This 
differentiation  provides  a  data-driven  insight  for  accurate  policymaking,  shifting  from 
traditional literacy programmes to tailored interventions on structural deficiencies.

Future  research  should  focus  on  longitudinal  panel  data  to  map  the  dynamics  of 
individuals shifting between clusters over the lifecycle. Additionally, while this study captures 
the unusual effects of COVID-19 economic disruptions, further research is needed to analyse 
how these clusters react to other large-scale macro-stressors, such as political or environmental 
crises. Finally, given the primary significance of subjective perceptions demonstrated in this 
research, future qualitative analysis could provide deeper insight into the mindset gap between 
The  Established  (C1)  and  The  Distressed  (C6),  promoting  educational  and  psychological 
mechanisms that may help achieve financial freedom among populations.

The  interpretation  of  these  findings  requires  the  acknowledgement  of  specific 
methodological  constraints.  First,  the  rigorous  data  pre-processing  involves  a  cleaning 
procedure  that  drops  incomplete  survey  responses.  While  necessary  to  ensure  index 
consistency, this may introduce survivorship bias, potentially underrepresenting the individuals 
with fragmented records, who are often the most vulnerable. Second, the cross-sectional nature 
of  the  data  limits  temporal  analysis,  which  would  enrich  the  understanding  of  movement 
dynamics  within  the  framework  across  different  stages  of  individuals’  lives.  Finally,  as  the 
study is based on the U.S. financial infrastructure, generalisations to emerging economies with 
different social systems should be approached with caution.

Preprint not peer reviewed

This research received no specific grant from any funding agency in the public, commercial, 
or not-for-profit sectors.

Breiman, L. (2001). Random Forests. Machine Learning, 45(1), 5–32.

https://doi.org/10.1023/A:1010933404324

References

Funding

This preprint research paper has not been peer reviewed. Electronic copy available at: https://ssrn.com/abstract=6826893

---

<!-- PAGE 23 -->

20

https://doi.org/10.1016/j.joep.2007.09.001

https://doi.org/10.1108/JEFAS-01-2022-0005

Journal of Economic Psychology, 29(1), 94–122.

79, 228–237. https://doi.org/10.1016/j.jbusres.2017.03.013

Economics, Finance and Administrative Science, 27(54), 376–393.

well-being: A conceptualization and research agenda. Journal of Business Research,

stress during the COVID-19 crisis: Evidence from Colombian households. Journal of

review of the economic literature on the factors associated with subjective well-being.

FINRA Investor Education Foundation. (2021). 2021 National Financial Capability Study

Dolan, P., Peasgood, T., & White, M. (2008). Do we really know what makes us happy? A

Brüggen, E. C., Hogreve, J., Holmlund, M., Kabadayi, S., & Löfgren, M. (2017). Financial

Cardona-Montoya, R. A., Cruz, V., & Mongrut, S. A. (2022). Financial fragility and financial

Preprint not peer reviewed

Haveman, R., & Wolff, E. N. (2005). The concept and measurement of asset poverty: Levels,

Huston, S. J. (2010). Measuring Financial Literacy. Journal of Consumer Affairs, 44(2), 296–

Greene, M., & Patil, R. (2023). Understanding the Mental-Financial Health Connection.

Halpern, S. D., Asch, D. A., & Volpp, K. G. (2012). Commitment contracts as a way to

trends and composition for the U.S., 1983?2001. The Journal of Economic Inequality,

https://www.finrafoundation.org/knowledge-we-help-create/national-financial-

health. BMJ, 344(jan30 1), e522–e522. https://doi.org/10.1136/bmj.e522

(NFCS) [Dataset]. FINRA Investor Education Foundation.

2(2), 145–169. https://doi.org/10.1007/s10888-005-4387-y

316. https://doi.org/10.1111/j.1745-6606.2010.01170.x

Financial Health Network.

capability-study

This preprint research paper has not been peer reviewed. Electronic copy available at: https://ssrn.com/abstract=6826893

---

<!-- PAGE 24 -->

21

031-38747-0_1

https://doi.org/10.1016/j.ssmph.2024.101624

16489–16493. https://doi.org/10.1073/pnas.1011492107

psychological distress. SSM - Population Health, 25, 101624.

health problems pile up: The reciprocal relationship between income and

emotional well-being. Proceedings of the National Academy of Sciences, 107(38),

Karaahmetoğlu, A., Yıldız, M., Ünal, E., Aydın, U., Koraş, M., & Akgün, B. (2025).

James, D. Witten, T. Hastie, R. Tibshirani, & J. Taylor, An Introduction to Statistical

Learning (pp. 1–13). Springer International Publishing. https://doi.org/10.1007/978-3-

Kahneman, D., & Deaton, A. (2010). High income improves evaluation of life but not

James, G., Witten, D., Hastie, T., Tibshirani, R., & Taylor, J. (2023). Introduction. In G.

Jiménez-Solomon, O., Garfinkel, I., Wall, M., & Wimer, C. (2024). When money and mental

Preprint not peer reviewed

Lusardi, A., Michaud, P.-C., & Mitchell, O. S. (2017). Optimal Financial Knowledge and

Lee, J.-Y. (2023). Economic Inequality, Social Determinants of Health, and the Right to

Lusardi, A., & Mitchell, O. S. (2011). Financial Literacy and Planning: Implications for

Kuhn, M., & Johnson, K. (2013). Applied Predictive Modeling. Springer New York.

Retirement Well-being. In O. S. Mitchell & A. Lusardi (Eds.), Financial Literacy:

Efficient, interpretable and automated feature engineering for bank data. Big Data

Implications for Retirement Security and the Financial Marketplace (pp. 16–39).

Wealth Inequality. Journal of Political Economy, 125(2), 431–477.

Research, 40, 100524. https://doi.org/10.1016/j.bdr.2025.100524

Social Security. Health and Human Rights, 25(2), 155–169.

https://doi.org/10.1007/978-1-4614-6849-3

https://doi.org/10.1086/690950

This preprint research paper has not been peer reviewed. Electronic copy available at: https://ssrn.com/abstract=6826893

---

<!-- PAGE 25 -->

22

Oxford University Press.

https://doi.org/10.1017/flw.2023.13

https://doi.org/10.1016/j.jbusres.2022.06.034

https://doi.org/10.1093/acprof:oso/9780199696819.003.0002

future research agenda. Journal of Business Research, 150, 417–436.

from the US. Journal of Financial Literacy and Wellbeing, 1(2), 169–198.

and Implications. SSRN Electronic Journal. https://doi.org/10.2139/ssrn.1809708

money honey? Analyzing and mapping financial well-being research and identifying

Lusardi, A., & Streeter, J. L. (2023). Financial literacy and financial well-being: Evidence

Lusardi, A., Schneider, D., & Tufano, P. (2011). Financially Fragile Households: Evidence

Material and social deprivation index 2021: User manual. (2024). Institut national de santé

Mahendru, M., Sharma, G. D., Pereira, V., Gupta, M., & Mundi, H. S. (2022). Is it all about

Preprint not peer reviewed

Ringlein, G. V., Ettman, C. K., & Stuart, E. A. (2024). Income or Job Loss and Psychological

Sajid, M., Mushtaq, R., Murtaza, G., Yahiaoui, D., & Pereira, V. (2024). Financial literacy,

Netemeyer, R. G., Warmath, D., Fernandes, D., & Lynch, J. G. (2018). How Am I Doing?

Perceived Financial Well-Being, Its Potential Antecedents, and Its Relation to Overall

Distress During the COVID-19 Pandemic. JAMA Network Open, 7(7), e2424601.

confidence and well-being: The mediating role of financial behavior. Journal of

Business Research, 182, 114791. https://doi.org/10.1016/j.jbusres.2024.114791

Well-Being. Journal of Consumer Research, 45(1), 68–89.

https://doi.org/10.1001/jamanetworkopen.2024.24601

https://doi.org/10.1093/jcr/ucx109

publique du Québec.

This preprint research paper has not been peer reviewed. Electronic copy available at: https://ssrn.com/abstract=6826893

---

<!-- PAGE 26 -->

23

financial well-being measure. (201).

https://doi.org/10.1007/s10902-021-00381-6

112632. https://doi.org/10.1016/j.psychres.2019.112632

Agenda. Journal of Happiness Studies, 23(1), 333–358.

Studies, 21(5), 1581–1602. https://doi.org/10.1007/s10902-019-00145-3

Methods to Study Financial Well-Being: A Scoping Review and Future Research

Financial Wellbeing: An Ecological Life-Course Approach. Journal of Happiness

hardship among individuals with serious mental illness. Psychiatry Research, 282,

Spivak, S., Cullen, B., Eaton, W. W., Rodriguez, K., & Mojtabai, R. (2019). Financial

Salignac, F., Hamilton, M., Noone, J., Marjolin, A., & Muir, K. (2020). Conceptualizing

Sticha, A., Lusardi, A., & Sconti, A. (2023). Development and testing of a comprehensive

Sorgente, A., Totenhagen, C. J., & Lanz, M. (2022). The Use of the Intensive Longitudinal

Preprint not peer reviewed

Wagner, J., & Walstad, W. B. (2019). The Effects of Financial Education on Short‐Term and

Wright, M. N., & König, I. R. (2019). Splitting on categorical predictors in random forests.

Theodossiou, I. (1998). The effects of low-pay and unemployment on psychological well-

World Health Organization. (2021). Health Promotion Glossary of Terms 2021 (1st ed).

https://www.tiaa.org/public/institute/publication/2023/development-and-testing-of-a-

being: A logistic regression approach. Journal of Health Economics, 17(1), 85–104.

Long‐Term Financial Behaviors. Journal of Consumer Affairs, 53(1), 234–259.

PeerJ, 7, e6339. https://doi.org/10.7717/peerj.6339

https://doi.org/10.1016/S0167-6296(97)00018-0

comprehensive-financial-well-being

https://doi.org/10.1111/joca.12210

World Health Organization.

This preprint research paper has not been peer reviewed. Electronic copy available at: https://ssrn.com/abstract=6826893

---

<!-- PAGE 27 -->

24

Newsletter, 24(1), 1–13. https://doi.org/10.1145/3544903.3544905

Interpretable Features: Motivation and Taxonomy. ACM SIGKDD Explorations

Zytek, A., Arnaldo, I., Liu, D., Berti-Equille, L., & Veeramachaneni, K. (2022). The Need for

Preprint not peer reviewed

This preprint research paper has not been peer reviewed. Electronic copy available at: https://ssrn.com/abstract=6826893

<!-- MARKITDOWN CONVERSION -->

<!-- Full MarkItDown conversion for formatting fidelity. -->

d
Unveiling the Financial Wellbeing Ecosystem: A Data-Driven Framework of Six Behavioral
Profiles*
e
w
e
i
v
e
r
r
e
e
p
t
o
n
t
n
i
r
p
e
r
P
* Data Availability: The data used in this study are drawn from the 2021 National Financial Capability Study
(NFCS), sponsored by the FINRA Investor Education Foundation. The dataset is publicly available at
[https://finrafoundation.org/nfcs-data-and-downloads]
This preprint research paper has not been peer reviewed. Electronic copy available at: https://ssrn.com/abstract=6826893

d
e
Daniel Fernando Masias Percca, Universidad ESAN, Lima, Peru
Jr. Alonso de Molina 1652, Lima, Peru w
dmasias@esan.edu.pe
Abstract e
Traditional evaluations of financial wellbeing rely on unidimensiional, linear indices that
overlook the complex interaction between short-term preparedvness and long-term security.
This study proposes a novel intertemporal framework to capture the inherent heterogeneity of
financial profiles through the integration of economic theorye with machine learning techniques.
Using data from the 2021 National Financial Capability Study (NFCS), a multi-stage pipeline
is implemented, including theory-driven feature engineering, clustering and Random Forest
r
classification to identify and validate six distinct segments, ranging from "The Established" to
"The Distressed." Our findings reveal a consistent "Subjective Dominance" effect, where
individual self-perception significantly outweighs robjective metrics and cognitive factors in
predicting wellbeing profiles. Furthermore, the analysis uncovers critical structural distinctions
e
between vulnerable segments: while "The Short-Sighted" are primarily constrained by human
capital deficits, "The Illiquid Planners" are destabilized by exogenous income shocks despite
e
their planning capabilities. These results challenge the efficacy of generalized policy
interventions and highlight the necessity of data-driven, psychologically informed strategies
that account for the nuances of intertepmporal trade-offs in personal finances.
Keywords – Financial wellbeing, financial literacy, financial fragility, financial stress
t
o
n
t
n
i
r
p
e
r
P
This preprint research paper has not been peer reviewed. Electronic copy available at: https://ssrn.com/abstract=6826893

d
Unveiling the financial wellbeing ecosystem: A data-driven framework of six behavioural
profiles*
e
w
e
i
v
e
r
r
e
e
p
t
o
n
t
n
i
r
p
e
r
P
* Data availability: The data used in this study are drawn from the 2021 National Financial Capability Study
(NFCS), sponsored by the FINRA Investor Education Foundation. The dataset is publicly available at:
https://finrafoundation.org/nfcs-data-and-downloads.
This preprint research paper has not been peer reviewed. Electronic copy available at: https://ssrn.com/abstract=6826893

d
e
ABSTRACT w
Traditional evaluations of financial wellbeing rely on unidimensional, linear indices that
overlook the complex interaction between short-term preparedness eand long-term security.
This study proposes a novel, intertemporal framework to capture the inherent heterogeneity of
financial profiles through the integration of economic theory and maichine learning techniques.
Using data from the 2021 National Financial Capability Study (vNFCS), a multi-stage pipeline
is implemented, including theory-driven feature engineering, clustering, and Random Forest
classification to identify and validate six distinct segments, eranging from “The Established” to
“The Distressed”. The findings reveal a consistent “subjective dominance” effect, where
individual self-perception significantly outweighs objective metrics and cognitive factors in
r
predicting wellbeing profiles. Furthermore, the analysis uncovers critical structural distinctions
between vulnerable segments: while “The Short-Sight ed” are primarily constrained by human
capital deficits, “The Illiquid Planners” are destabirlised by exogenous income shocks despite
their planning capabilities. These results challenge the efficacy of generalised policy
e
interventions and highlight the need for data-driven, psychologically informed strategies that
account for the nuances of intertemporal trade-offs in personal finances.
e
Keywords: Financial wellbeing, Finanpcial literacy, Financial fragility, Financial stress
t
o
n
t
n
i
r
p
e
r
P1. Introduction
Financial wellbeing can be defined as being and feeling in control of personal expenses,
and demonstrating short-term preparedness and long-term security. According to Sticha et al.
(2023), it refers to managing money to meet daily demands, but also considering a retirement
This preprint research paper has not been peer reviewed. Electronic copy available at: https://ssrn.com/abstract=6826893

2
d
plan. This concept becomes noteworthy when both historical and recent events claim a strong
relationship between socioeconomic status and ill-health, and even mortality. Evidence shows
e
that general distress and mental illness are strongly driven by financial issues (Greene & Patil,
2023). Without proper management, these pathologies impact individuals’ quality of life,
leading to a cycle of negative impacts on household welfare (Jiménez-Solowmon et al., 2024).
Financial wellbeing has heterogeneous perspectives towards its measurement and
evaluation. A common definition is based on numerical scores. Aelthough granular, these
metrics represent an over-simplification of an individual's wellbeing, which indeed has
multiple dimensions (Salignac et al., 2020). Furthermore, several efforts have also been made
i
to evaluate its determinants. Objective metrics of financial profiles (e.g., income) were the first
v
variables modelled, followed by the incorporation of subjective approximations (e.g., feelings
towards such income). More recently, financial literacy has been included given its strong
e
correlation with the previous two concepts, all of them modelled along with demographic
features to control for contextual scenarios (Lusardi & Streeter, 2023).
r
The research landscape acknowledges a clear problem: financial wellbeing lacks an
integral evaluation system, where its periodic nature and fundamental determinants are jointly
r
recognised. Previous work aimed to develop compound scales with a multidimensional
approach (Sticha et al., 2023). However, its suebjective methodology complicates transparent
interpretation. Authors such as Wagner and Walstad (2019) and Netemeyer et al. (2018) have
formulated mathematical models to evaluate the effect of certain regressors on target variables.
e
Nevertheless, not all critical determinants are considered, likely distorting the actual effect of
the covariates.
p
This study aims to address the issue by designing and testing a holistic financial
wellbeing framework. The prop osed framework fulfils both theoretical and practical
fragmentation in concept measurement and determinant evaluation. Accordingly, the focus is
t
on establishing accurate profiles and analysing the reasons behind such differentiation. For this
o
purpose, the study follows a non-experimental, quantitative methodology, supported by
descriptive and predictive analyses. The central evaluation is conducted through machine
n
learning techniques due to their strong capacity to model complex variable interactions within
an interrelated system.
Recognising the integral nature of personal finances is essential for maintaining
t
economic balance and mitigating risks of neglecting critical areas such as health and education.
n
In addition, understanding the underlying drivers behind individuals' financial situations is
paramount to forecasting effective decisions and policies. These findings hold universal
relevance foir a broad spectrum of stakeholders: from ordinary citizens striving for financial
autonomyr, to policymakers aiming to enhance public health, and non-governmental
orgapnisations (NGOs) dedicated to assisting underrepresented populations. Ultimately, this
framework serves all stakeholders committed to strengthening the financial wellbeing of
populations across decades and even generations.
e
r
P
2. Literature review
Human health comprises a broad concept where mental and physical welfare are the
central objective (World Health Organization, 2021). In this sense, financial wellbeing has been
This preprint research paper has not been peer reviewed. Electronic copy available at: https://ssrn.com/abstract=6826893

3
d
extensively researched due to its impact on both health domains. Mental illness, chronic stress,
and medical avoidance are some of the consequences of poor financial management (Spivak et
e
al., 2019). For instance, in the United States, the effects of the COVID-19 pandemic revealed
a surge in psychological pathologies among individuals experiencing income instability or job
loss. Ringlein et al. (2024) found that, between 6 and 10 months followingw the onset March in
2020, the psychological distress levels of those affected by income shocks were 9% higher than
their stable-income counterparts. This disparity increased to 11% between months 25 to 29,
suggesting a chronic mental health deterioration in the long-term. Thise divergence implies that
the psychological burden of financial stress outlasted government interventions, highlighting a
latent public health crisis. i
v
Based on the above, financial wellbeing has emerged as an essential indicator of social
stability and progress (Brüggen et al., 2017). While its preservation is a central objective
e
globally, heterogeneous conceptualisations and fragmented operationalisations continue to
obscure a transparent understanding (Mahendru et al., 2022). In this sense, a robust
r
measurement and analysis of financial wellbeing is critical to mitigate systemic public health
risks and foster long-term resilience (Salignac et al., 2 020).
r
Regarding conceptualisation, the literature presents a range of perspectives drawing on
economic foundations, technical definitions, aned heuristic analogies, as discussed by Brüggen
et al. (2017), Sorgente, Totenhagen, and Lanz (2022), and Sajid et al. (2024). These multiple
approaches overcomplicate a general understanding. To overcome this issue, Sticha, Lusardi,
e
and Sconti (2023) proposed a comprehensive definition, stating that “financial wellbeing is not
only about long-term financial security (retirement planning) but also about short-term
p
financial preparedness”. This contribution reinforces a previous approximation of Salignac et
al. (2020), who concluded that a person is financially healthy when “they are in control of their
finances and feel financially secure , now and in the future”.
t
The previous foundation is critical for providing a complete measurement. Thus, the
o
intertemporal duality of financial wellbeing is employed in this study, defining it as the
effective management of day-to-day expenses and proper budget planning for the future. As
n
noted above, current measurements are solely based on one-dimensional scores or subjective
compound metrics. Crucially, the majority of existing indices do not assess the intertemporal
integrability of fina ncial wellbeing. These limitations increase the risk of misguided
conclusions and itneffective interventions. Given the above, the first research question is
formulated as follows:
n
RQ1: How can financial wellbeing be measured within an intertemporal framework?
i
Trhe previous methodological heterogeneity is not limited to its measurement; it also
extends to the analysis of the drivers behind financial wellbeing outcomes. Research on
p
household financial wellbeing has normally been conducted considering income-based drivers,
plus demographic controls (Cardona-Montoya et al., 2022). For instance, studies such as
e
Theodossiou (1998) were focused primarily on the impact of low wages on mental health.
Twenty years later, Dolan, Peasgood, and White (2008) presented an interesting contribution
rstating that happiness was more strongly influenced by relative income comparisons than by
the actual income received by individuals. In other words, self-assessments towards one's own
P
situation represent an indispensable factor on personal welfare. This finding explains the origin
of the subjective-objective dichotomy and adds a second driver of financial wellbeing.
Notably, a common feature among existing works is the acknowledgement of structural
differences reflected in demographic variables. In this sense, Wagner and Walstad (2019)
This preprint research paper has not been peer reviewed. Electronic copy available at: https://ssrn.com/abstract=6826893

4
d
suggest that both momentary and long-lasting circumstances must be considered, underscoring
the significance of age, gender, income range, and marital status, among other variables.
e
More recently, Lusardi and Streeter (2023) concluded that financial literacy plays a
fundamental role in shaping money-management practices (subjectivew perceptions) and
financial decision-making (objective behaviour), finding a strong impact on financial
wellbeing. This third variable complemented the set of determinants.
e
Although several studies have tested the effects of these three determinants, they were
mostly analysed in isolation. In this sense, financial wellbeing research still lacks an integral
i
modelling where all the aforementioned drivers are jointly evaluated (subjective perceptions
v
along with objective behaviours and financial literacy). By providing a robust model, a better
understanding of financial wellbeing outputs, their causes and consequences is achieved. This
e
contributes to conscious decisions and tailored actions. Given the above, the second research
question is formulated as follows:
r
RQ2: What is the role of the entire set of financial wellbeing determinants?
To address these research questions, this sturdy adopts a robust quantitative approach.
Specifically, to answer RQ1, an index construction is constructed for each intertemporal
e
dimension, followed by its consolidation into a comprehensive framework that presents a novel
taxonomy of financial wellbeing profiles. Subsequently, to address RQ2 and explore the
e
interplay between determinants, a machine learning algorithm is trained, and a granular
analysis is conducted on the role of each determinant.
p
3. Method
The strategy employed to a ddress the research questions follows a sequential, multi-
stage architecture. This is structutred into three phases to ensure robustness and reproducibility.
First, the research design and data sourcing are established to guarantee sample accuracy and
o
representativeness (Section 3.1). Then, a rigorous feature engineering is conducted to
operationalise the intertemporal measurements and determinants of financial wellbeing
n
(Section 3.2). Finally, the implementation and testing of the framework are detailed, describing
the machine learning technique used to uncover the novel taxonomy (Section 3.3).
3.1. Research design, sample and data
t
n
The methodology comprises a quantitative and non-experimental analyses, with a strong focus
on variable interactions within the created framework. This research is based on the 2021
National Finiancial Capability Study (NFCS), a strategic dataset to analyse the COVID-19
pandemicr effects on population financial wellbeing (FINRA Investor Education Foundation,
2021). It comprises information of 27,118 adults from the United States, representing a
p
population of over 250 million. Of those, all observations which belong to retired individuals
or lacking responses to key questions to estimate the model variables were excluded. In this
e
sense, the final sample involves 11,857 observations. The strength of this dataset relies on its
vast amount of information for a complete analysis. Financial behaviours, perceptions, and
reducation are covered, along with sociodemographic and contextual features.
P
3.2. Variable construction and feature engineering
Based on the literature review, the dependent variable was built within an intertemporal
framework. Following the method adapted from Wagner and Walstad (2019), eight items from
the NFCS were selected to construct this measure. Specifically, four items are designated to
This preprint research paper has not been peer reviewed. Electronic copy available at: https://ssrn.com/abstract=6826893

5
d
assess short-term (ST) financial control, while the remaining four evaluate long-term (LT)
financial security.
e
To construct these two indices, a feature engineering process is employed, involving
the binarisation and additive aggregation of the selected items. While dimenwsionality reduction
techniques, such as Principal Component Analysis (PCA) or Multiple Correspondence
Analysis (MCA), are common in large datasets, feature engineering was preferred to preserve
the theoretical interpretability and semantic integrity of the financial ceonstructs. Unlike PCA,
which generates latent components that maximise statistical variance but often lack direct
interpretation (Zytek et al., 2022; Karaahmetoğlu et al., 2025), this approach ensures that the
i
resulting indices directly reflect the intertemporal duality of financial wellbeing, as defined in
v
the literature. The detailed interpretation of the drivers, which purely statistical components
might obscure, is key for actionable insights (Huston, 2010). In this sense, binarisation and
e
aggregation enable the synthesis of variables from raw data while maintaining consistency with
the objectives and preserving the dependencies within the model (Kuhn & Johnson, 2013).
r
The short-term index is constructed using four questions shown in Table 1. These items
are designed to capture the immediate cash-flow management and daily financial behaviours
r
that define an individual’s financial stability. Following the framework proposed by Wagner
and Walstad (2019), four key dimensions weere identified: expense management, banking
behaviour, credit discipline, and debt perception. Each item was binarised (1 = favourable, 0 =
unfavourable) using a “top-box” criterion to isolate optimal financial behaviours (such as
e
paying credit cards in full or having no difficulty covering bills) from any degree of financial
distress. This operationalisation allows the index to reflect clear distinctions between financial
p
stability and vulnerability in the short-term.
Table 1
t
Operationalisation and binary encoding of short-term financial wellbeing components
o
Construct NFCS item Binarisation logic
n
(1 = favourable)
Expense J4 : In a typical month, how difficult is it for you Not at all difficult
management to cover your expenses and pay all your bills?
t
n
Banking B4: Do you [or your spouse/partner] overdraw No (Never occasionally
behaviour your checking account occasionally? overdraws)
i
Credit rF2_1: In the past 12 months, which of the Yes (Always paid in
discipline following describes your experience with credit full)
p
cards? - I always paid my credit cards in full.
e
Debt G23: How strongly do you agree or disagree Strongly
perception with the following statement? - I have too much disagree/Disagree
r debt right now.
P
Note: Data from the 2021 National Financial Capability Study (NFCS).
The long-term index is measured by four questions shown in Table 2. These items focus on
asset accumulation and future resilience, adapting the methodology of Wagner and Walstad
This preprint research paper has not been peer reviewed. Electronic copy available at: https://ssrn.com/abstract=6826893

6
d
(2019) as well. They cover emergency resilience and formal liquidity, essential metrics to avoid
financial stress during economic downturns (Haveman & Wolff, 2005). Furthermore,
e
investment activities and retirement planning items are considered, which are critical for life-
cycle financial wellbeing (Lusardi et al., 2017). Consistent with the short-term index, all items
are binarised using a threshold of proactive financial security. Favourablwe outcomes reflect
anticipatory financial actions rather than mere asset ownership. For example, retirement
planning is defined by the active calculation of future needs rather than merely the existence
of a retirement account. e
Table 2
i
v
Operationalisation and binary encoding of long-term financial wellbeing components
e
Construct NFCS item Binarisation logic
(1 = favourable)
r
Emergency J5: Have you set aside emergency or rainy-day Yes (Has 3-month
resilience funds that would cover expenses for 3 months? buffer)
r
Liquidity/basic B2: Do you have a saevings account, money Yes (Maintains
saving market account, or CDs? formal savings)
e
Asset B14: Not including retirement, do you have any Yes (Active
accumulation investments in stocks, bonds, or mutual funds? investor)
p
Retirement J8: Have you ever tried to figure out how much Yes (Has calculated
planning you need to sa ve for retirement? retirement needs)
t
Note. Data from the 2021 Noational Financial Capability Study (NFCS).
Subsequently, the independent variables are defined, representing the entire set of
n
critical determinants of financial wellbeing. This approach comprises objective behaviours,
subjective perceptions, financial literacy, and demographic characteristics. Twenty-six items
were selected from the NFCS to construct these measures. Specifically, five items were
designed to assesst the objective behaviour, five to evaluate the subjective perceptions, seven
to measure nfinancial literacy, and nine to reference the individuals’ demographic
characteristics.
i
The objective behaviour index is measured by the questions shown in Table 3. These
r
items serve as a proxy for personal pillars for financial stability and security. The inclusion of
the ipncome threshold at the $75,000 mark aligns with established literature suggesting that
emotional stability tends to plateau beyond this income level (Kahneman & Deaton, 2010).
Budgetary discipline is incorporated as a measure of active saving behaviour, reflecting the
e
individual’s capacity for capital retention regardless of total earnings. Liquidity shock capacity
represents the NFCS standard for assessing financial fragility. By isolating only those who are
r
“totally confident,” this index applies a stringent filter for immediate financial resilience
P(Lusardi et al., 2011). Finally, the index accounts for institutional coverage and credit risk
avoidance, capturing the external support systems and the avoidance of high-cost,
unsustainable debt.
Table 3
This preprint research paper has not been peer reviewed. Electronic copy available at: https://ssrn.com/abstract=6826893

7
d
Operationalisation and binary encoding of objective behaviour components
e
Construct NFCS item Binarisation logic
(1 = favourable)
w
Income A8_2021: What is your household's 1 = high income (>
threshold approximate annual income? $75,000)
e
Budgetary J3: Was your household's spending less than, 1 = budget surplus
discipline more than, or equal to your income? (ispending < income)
v
Liquidity J20: How confident are you that you could 1 = high liquidity
shock come up with $2,000 for an unexpected neeed? confidence (totally
capacity confident)
r
Institutional C1_2012: Do you have any retirement plans 1 = covered (has
coverage through an employer (e.g., pension)? employer-sponsored plan)
r
Credit risk G25_1: In the past 5 years, how many times 1 = safe credit behaviour
e
avoidance have you taken out an auto title loan? (never)
e
Note: Data from the 2021 National Financial Capability Study (NFCS).
The subjective perception indpex is measured by the questions shown in Table 4. The
abbreviated version of the Consumer Financial Protection Bureau (CFPB) scale was employed
for this purpose. This validated index captures the psychological dimension of financial
wellbeing, moving beyond mere solvency to measure individuals’ internal sense of security
t
and freedom. Unlike the previous indices, these items were not binarised; instead, a two-step
transformation process was oapplied. First, raw responses were coded on a 0–4 scale depending
on their wellbeing phrasing. Second, the cumulative scores were mapped onto the official
CFPB Conversion Tablne to produce a final standardised score ranging from 0 to 100. Following
the CFPB technical protocol, negatively phrased items were reverse-coded to ensure that higher
values consistently reflect greater levels of perceived wellbeing.
Table 4 t
n
Operationalisation and binary encoding of subjective perception components
i
Construct NFCS item Scoring
r
methodology
p
Long-term How well do these statements describe you? Because Negatively phrased
egoal of my money situation, I feel like I will never have 0 = completely
attainment the things I want in life. 4 = not at all
r
Financial How well do these statements describe you? Negatively phrased
Psufficiency I am just getting by financially. 0 = completely
perceptions 4 = not at all
This preprint research paper has not been peer reviewed. Electronic copy available at: https://ssrn.com/abstract=6826893

8
d
Future How well do these statements describe you? Negatively phrased
security I am concerned that the money I have or will save 0 = comepletely
anxiety won't last. 4 = not at all
w
Monthly How often do these statements apply to you? Positively phrased
budgetary I have money left over at the end of the month. 4 = always
margin 0 = never
e
Perceived How often do these statements apply to you? Negatively phrased
financial My finances control my life. i0 = always
v
agency 4 = never
e
Note: Data from the 2021 National Financial Capability Study (NFCS).
The financial literacy index is measured by the qurestions shown in Table 5. This index
measures the cognitive foundation of financial decision-making. Following the work of Lusardi
and Mitchell (2011), the index incorporates the “Big Three” concepts (interest rates, inflation,
r
and risk diversification), alongside more advanced topics such as bond pricing, mortgage
structures, compound interest, and probabilistiec reasoning. These items serve to differentiate
between basic numeracy and functional financial knowledge. Each item was binarised (1 =
correct, 0 = incorrect/do not know), creating a cumulative scale that ranges from 0 to 7.
e
p
Table 5
Operationalisation and binary enco ding of financial literacy components
t
Construct oNFCS item Binarisation logic
(1 = correct answer)
n
Suppose you had $100 in an account with an interest
Numeracy/inte
rate of 2% per year. How much would you have after 1 = more than $102
rest
five years if you left the money to grow?
t
nImagine that the interest rate on your account was 1%
Inflation
per year and inflation was 2% per year. After 1 year, 1 = less than today
awareness
how much would you be able to buy with the money?
i
r
Risk Buying a single company's stock usually provides a
1= false
diveprsification safer return than a stock mutual fund.
eBond If interest rates rise, what will typically happen to bond
1 = they will fall
valuation prices?
r
A 15-year mortgage typically requires higher monthly
Mortgage
P payments than a 30-year mortgage, but the total 1= true
literacy
interest paid over the life of the loan will be less.
Compound Suppose you owe $1,000 on a loan and the interest rate
1 = 2 to 5 years
interest is 20% per year compounded annually. If you didn't
This preprint research paper has not been peer reviewed. Electronic copy available at: https://ssrn.com/abstract=6826893

9
d
pay anything off, at this interest rate, how many years
would it take for the amount you owe to double? e
Probabilistic Which of the following indicates the highest
1 w= one-in-twenty
reasoning probability of getting a particular disease?
Note: Data from the 2021 National Financial Capability Study (NFCS).
e
Lastly, nine demographic and socioeconomic variables are integrated as control
features to account for individual heterogeneity in financial outciomes. These include age
group, gender, educational attainment, household income, nuvmber of dependent children,
income shocks, secondary employment, labour status, and marital status. All of them were
extensively employed in previous work, such as the studiees of Lusardi and Streeter (2023),
Sticha, Lusardi, and Sconti (2023), and Wagner and Walstad (2019). The ordinal structure of
age, education, income, and number of dependants wras preserved to capture the inherent
gradients in these dimensions. Conversely, the nominal variables were all transformed using
one-hot encoding. This process generates distinct binary indicators for each category,
r
preventing the model from assuming a non-existent hierarchy among nominal labels. A detailed
description of each indicator and its correspondeing measurement scale is provided in the Online
Appendix (Fig. B.1).
e
3.3. Implementation of the financial wellbeing framework
Based on the previously constructed indices, the dependent variable was derived from
p
a cross-tabulation of the short-term (ST) and long-term (LT) scales. As illustrated in Fig. 1,
this bivariate approach maps the intertemporal framework of financial wellbeing, resulting in
a 5x5 matrix with twenty-five distinct cells. This spatial representation allows for a granular
t
identification of financial profiles. The bottom-left quadrant identifies individuals experiencing
concurrent fragility in both SoT and LT dimensions, whereas the top-right quadrant characterises
those exhibiting strong intertemporal security. Consequently, this matrix serves as the
structural basis for opnerationalising the financial wellbeing profiles, thereby defining the
model's dependent variable.
With both the dependent and independent variables constructed, a supervised
classification modetl was implemented to simultaneously validate the proposed framework and
analyse the finnancial wellbeing of U.S. adults. Two models are estimated for this purpose.
Equation (1) represents the model without control variables, and Equation (2) adds the
demographic controls. Both models are presented below:
i
r
𝑌 =𝑓( X +X +X ) +ϵ (1)
𝑖 1,i 2,i 3,i i
p
e
𝑌 𝑖 =𝑓( X 1,i +X 2,i +X 3,i + 𝒁 𝒊 ) + ϵ i (2)
r
P
where:
𝑌 is the dependent label value for individual “i”
𝑖
X is the independent index value of subjective perception for individual “i”
1,i
X is the independent index value of objective behaviour for individual “i”
2,i
This preprint research paper has not been peer reviewed. Electronic copy available at: https://ssrn.com/abstract=6826893

10
d
X is the independent index value of financial literacy for individual “i”
3,i
Z is the set of demographic controls for individual “i”
i e
𝜖 is the random error term for individual “i”
i
w
The algorithm selected is Random Forest (RF) due to its superior capacity to handle
heterogeneous data types and capture the nonlinear relationships inherent in socioeconomic
data (Wright & König, 2019). As an ensemble method that aggregates multiple decision trees,
e
RF is robust against outliers and multicollinearity (Kuhn & Johnson, 2013), making it suitable
for the complex behavioural interactions within financial datasets. By adopting this approach,
the study provides an empirical validation of the bi-dimensional framiework presented in Fig. 1.
The dataset is then partitioned into training (80%) and testing (2v0%) subsets to ensure out-of-
sample evaluation. To address class imbalance, the Synthetic Minority Over-Sampling
Technique (SMOTE) is applied exclusively to the training seample.
The Random Forest implementation in this study follows a principled approach for
r
hyperparameter tuning (Breiman, 2001; James et al., 2023). The number of trees is set to 100,
sufficient for the out-of-bag error to converge. The nu mber of features at each node split is set
to the square root of the number of predictors, ar common heuristic to reduce correlation
between trees. These choices target the main sources of ensemble variance and bias. The
e
remaining hyperparameters were kept at their default values to avoid overfitting and ensure a
reproducible baseline framework.
e
Model performance was evaluated using a robust set of out-of-bag measure error
estimates. While global accuracy and the confusion matrix provided a baseline for overall
p
model validity, the analysis prioritised precision and recall (sensitivity) to ensure a proper
assessment of the classifier's performance across heterogeneous segments. Given the inherent
class imbalance within the financial wellbeing clusters, these last two metrics were prioritised
for minority classes. This multi-mtetric approach ensures that the framework’s predictive power
is consistently validated, eoven for underrepresented populations within the NFCS dataset.
Furthermore, the inclusion of feature importance metrics enables an analysis of the primary
drivers of financial wellbeing, ensuring that the model fulfils both the classificatory and
n
diagnostic objectives of this research.
4. Results
t
The development of the intertemporal framework reveals a complex landscape of
n
financial wellbeing that linear models often obscure. This section presents the findings in three
stages. First, a novel, six-clusters taxonomy is established to measure the U.S. population
i
across the short-term and long-term spectrum. Second, the most important determinants in
r
shaping financial wellbeing are identified through the Global Random Forest classification.
Finaplly, an original examination of “boundary dynamics” is presented, identifying the specific
drivers that differentiate adjacent clusters, thus offering granular insights into the mechanisms
of financial mobility.
e
4.1. New taxonomy of financial wellbeing
r
Fig. 1 shows that the intertemporal framework is not distributed uniformly. While a
P
significant density of observations (n) clusters in the high-performance quadrant (indicating
intertemporal synergy), distinct pockets of vulnerability emerge in the lower bounds and off-
diagonal axes. Following the segmentation logic applied by Azevedo et al. (2024) in social
science research, this study prioritises a clear distinctiveness over equally sized groupings. The
objective is not to create statistical quartiles, but to isolate relevant profiles that exhibit
This preprint research paper has not been peer reviewed. Electronic copy available at: https://ssrn.com/abstract=6826893

11
d
contrasting financial realities. Consequently, the 25-cell matrix was synthesised into six distinct
clusters, forming a new taxonomy of financial wellbeing.
e
w
e
i
v
e
r
r
e
e
p
t
o
n
Fig. 1. The intertemtporal financial wellbeing framework: identification of six distinct profiles.
Note: The framework illustrates the six distinct profiles identified through the intersection of
n
the short-term and long-term indices.
Drawiing on the spatial configuration presented above, the proposed framework
delineaters distinct profiles with unique intertemporal combinations, ranging from robust
stabiplity to systemic vulnerability. The specific cluster characteristics are detailed below.
Cluster 1: The Established (C1). This group reaches the highest level of financial health. It
eis characterised by strong liquidity management in the present and robust capital planning for
the future.
r
Cluster 2: The Resilient (C2). This segment demonstrates moderate control over current
P
finances and adequate future security, but it has sub-optimal financial habits.
Cluster 3: The Short-Sighted (C3). This cluster maintains adequate liquidity and
consumption satisfaction but shows deficient long-term preparedness.
This preprint research paper has not been peer reviewed. Electronic copy available at: https://ssrn.com/abstract=6826893

12
d
Cluster 4: The Illiquid Planners (C4). In contrast to C3, this group has managed to construct
a substantial future budget, but struggles to fund its day-to-day demands.
e
Cluster 5: The Precarious (C5). This segment presents a latent risk, marked by instability and
lack of control of their finances. They are theoretically solvent, but vulnewrable in practice to
any kind of income shock.
Cluster 6: The Distressed (C6). This segment occupies the lower tier of financial health,
e
revealing immediate liquidity crises and minimal safety for the future.
The descriptive analysis of the three core determinants acrossi the six identified clusters
is presented in Fig. 2. A progressive gradient is evident. Clustver 1 (C1) exhibits the highest
mean scores across all dimensions, justifying its label as The Established, while the indicators
steadily decrease until reaching the lowest scores within eThe Distressed (C6). Intermediate
clusters reveal distinct differences in determinants, yet substantial heterogeneity in outcomes.
A more granular analysis of this critical differentiation is presented in Section 4.3.
r
r
e
e
p
t
o
n
t
n
i
Fig. 2. Multidimensional profiling of financial wellbeing clusters: a comparative analysis of
r
key determinants. Note: The chart displays the normalised average scores for each cluster,
rescapled to 0-100% relative to the theoretical range of each index. Values closer to the periphery
indicate a higher prevalence of the attribute.
e
Beyond the heterogeneity evidenced in Fig. 1, clear socioeconomic and structural
differences emerge among the six clusters, and their acknowledgement supports a granular
r
understanding of such profiles. Detailed distributions of these demographic characteristics are
Ppresented in Online Appendix B. Education and income among The Established (C1) play a
fundamental role within this segment. A significant portion of individuals with postgraduate
degrees (47.1%) and individuals with annual earnings above $300,000 (72.5%) are located in
C1. In contrast, within The Distressed (C6), 79.7% have not attained an undergraduate degree
and 66.1% earn less than $50,000 annually (Figs. B.2-B.3). A gender gap is also evident.
This preprint research paper has not been peer reviewed. Electronic copy available at: https://ssrn.com/abstract=6826893

13
d
Females are disproportionately represented in the less healthy segment, comprising 69.4% of
The Distressed, whereas males dominate the most-healthy cluster reaching 57.8% of The
e
Established (Fig. B.4).
Regarding the lifecycle hypothesis of Wagner and Walstad (2018), wfinancial wellbeing
generally improves with age, suggesting that financial maturity and prudence develop over
time (Fig. B.5). An exogenous incident, based on the COVID-19 pandemic effects, was critical
for group demarcation. Only 12% of The Established reported an incomee disruption, compared
with an average of 48.6% among the vulnerable clusters (The Illiquid Planners, The Precarious,
and The Distressed) (Fig. B.6).
i
v
Finally, family composition and marital status indicate no global patterns; however,
they are relevant for clusters with intertemporal biases, such as The Short-Sighted (C3) and
e
The Illiquid Planners (C4). There is a significantly higher proportion of dependent children
within C4, compared with C3, reaching a difference of 31.6%. This suggests that family
demands constrain liquidity for daily expenses. Morreover, The Short-Sighted, largely
composed by non-partnered individuals (59.7% belong to single, separated, divorced, or
widowed statuses), may direct income flows toward required immediate consumption,
r
preventing long-term savings (Figs. B.7-B.8).
e
4.2. Global determinants of financial wellbeing
e
After the initial diagnostic analysis, the stepwise Random Forest application provides
both confirmatory and novel findings. Two models are estimated: Model 1 is the baseline, with
only the three core determinants (objepctive, subjective, and literacy scales), while Model 2 adds
the sociodemographic controls. The results, summarised in Table 6, show an expected insight:
the inclusion of contextual and personal characteristics is critical to capture the variance in
financial wellbeing outcomes. Model 2 improves the accuracy from 0.37 to 0.46, with
t
consistent gains in precision and recall metrics. This enhanced performance validates previous
o
studies, such as Wagner and Walstad (2019), Lusardi and Streeter (2023), and Sticha, Lusardi,
and Sconti (2023), which established that an individual's contextual environment deeply
influences their financinal wellbeing.
Table 6
Comparative perftormance of Random Forest models: baseline determinants vs. full
demographic nmodel
i
r
Metric Model 1 Model 2
p
Accuracy 0.3689 0.4557
e
Precision
C1 0.70 0.66
r C2 0.38 0.38
C3 0.08 0.14
P
C4 0.15 0.27
C5 0.33 0.40
C6 0.28 0.31
This preprint research paper has not been peer reviewed. Electronic copy available at: https://ssrn.com/abstract=6826893

14
d
|     | Metric |     | Model 1 | Model 2 |
| --- | ------ | --- | ------- | ------- |
e
Recall
|     | C1  |     | 0.64 | 0.70 |
| --- | --- | --- | ---- | ---- |
w
|     | C2  |     | 0.18 | 0.31 |
| --- | --- | --- | ---- | ---- |
|     | C3  |     | 0.23 | 0.12 |
|     | C4  |     | 0.32 | 0.33 |
e
|     | C5  |     | 0.20 | 0.44 |
| --- | --- | --- | ---- | ---- |
|     | C6  |     | 0.46 | 0.34 |
i
Note: Accuracy indicates overall model performance, whereas precision and recall provide a  v
granular assessment of each cluster, controlling for class-size disparities.
e
Beyond the classification metrics, the feature importance analysis provides surprising
findings into the determinants structure. Table 7 presents a ranking analysis for both models.
r
Even though there is a slight variation in variable significance between the two models, the

Subjective  Index  emerges  as  the  paramount  classifier,  exhibiting  superior  predictive
importance  compared  with  the  Objective  Index rand  the  Financial  Literacy  Index.  This
hierarchy evidences that individuals’ internal sense of preparedness and security (their mindset)  e
is more important than their actual financial behaviours and habits (their actions). Regarding
the demographic features, results for age and education level confirm the previous descriptive
e
analyses, indicating that financial health involves life-cycle dynamism, with education acting
as a strong differentiator.
p
Table 7
t
Random Forest feature importance (FI): hierarchy of financial wellbeing determinants
o
n
|     | FI Ranking |     | Model 1 | Model 2 |
| --- | ---------- | --- | ------- | ------- |

|     | 1   | Subjective Index |     | Subjective Index |
| --- | --- | ---------------- | --- | ---------------- |
t
n
|     | 2   | Objective Index |     | Literacy Index  |
| --- | --- | --------------- | --- | --------------- |
| i   | 3   | Literacy Index  |     | Objective Index |
r
|     | 4   |     |     | Education Level |
| --- | --- | --- | --- | --------------- |
p
|     | 5   |     |     | Age Group |
| --- | --- | --- | --- | --------- |
e
Note:  Higher  ranking  indicates  a  greater  predictive  contribution  of  the  variable  in
distinguishing financial wellbeing profiles.
r
PThe inclusion of sociodemographic controls allows the model to classify with higher
accuracy.  Nevertheless,  the  confusion  matrix  shown  in  Table  8  reveals  persistent
misclassification between adjacent clusters. Particularly, individuals among the intermediate
clusters, The Short-Sighted (C3), The Illiquid Planners (C4), and The Precarious (C5), are
likely to overlap because of their similar characteristics. Likewise, The Established (C1) are
This preprint research paper has not been peer reviewed. Electronic copy available at: https://ssrn.com/abstract=6826893

15
d
frequently misclassified as The Resilient (C2), and vice versa. This phenomenon was expected,
as previous work suggests that financial wellbeing modelling is indeed complex, where similar
e
determinants may result in different outcomes (Dolan et al., 2008; Lusardi & Streeter, 2023).
Ultimately, the heterogeneity among individual profiles within each cluster underscores that
there is not a unique or infallible determinant, neither at the personal nor at twhe contextual level.
Table 8
e
Confusion matrix: analysis of inter-cluster misclassification patterns
i
|     |     |     |     | Model 1 |     |     |     |     | Model 2 |     |
| --- | --- | --- | --- | ------- | --- | --- | --- | --- | ------- | --- |
v
|     |     | C1  | C2  | C3  | C4  | C5  | C6  | C1 C2 | C3  | C4 C5 C6 |
| --- | --- | --- | --- | --- | --- | --- | --- | ----- | --- | -------- |
e
|     | C1  | 498 | 102 | 87  | 55  | 31  | 7   | C1 546 151 | 13  | 29 33 8   |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------- | --- | --------- |
|     | C2  | 168 | 111 | 125 | 128 | 55  | 44  | C2 193r194 | 44  | 71 105 24 |
|     | C3  | 18  | 14  | 28  | 35  | 14  | 12  | C3 2 8 26  | 14  | 6 37 10   |
r
|     | C4  | 14  | 25  | 27  | 64  | 46  | 27  | C4 26 48 | 2   | 66 46 15 |
| --- | --- | --- | --- | --- | --- | --- | --- | -------- | --- | -------- |
e
|     | C5  | 15  | 33  | 80  | 110 | 89  | 127   | C5 29 69 | 22  | 56 199 79 |
| --- | --- | --- | --- | --- | --- | --- | ----- | -------- | --- | --------- |
|     | C6  | 3   | 8   | 25  | 30  | 32  | 85eC6 | 6 18     | 5   | 18 74 62  |
Note: Rows represent the actual (true) cluster membership, while columns represent the
p
predicted classification by both models.
4.3. The dynamics of mobility: bou ndary analysis
t
Previous analyses suggest that global determinants delineate the broad framework for
o
financial wellbeing. However, they obscure the specific drivers that prevent social mobility
across adjacent clusters. To identify these “levers of change”, a new strategy is adopted by
isolating the decision bnoundaries between key segments. This is implemented through three
binary Random Forest classifications, the results of which are presented in Table 9. The
granular analysis rev eals that financial wellbeing determinants shift according to the location
of the individual within the intertemporal framework.
t
n
Table 9
Pairwise discriminant analysis: evaluation metrics across adjacent clusters
i
r
p
|     |     | Metric |     |     | Pair C3 - C4 |     |     | Pair C5 - C6 |     | Pair C1 - C2 |
| --- | --- | ------ | --- | --- | ------------ | --- | --- | ------------ | --- | ------------ |
e
|     | Accuracy |     |     |     |     | 0.7932 |     | 0.6426 |     | 0.7030 |
| --- | -------- | --- | --- | --- | --- | ------ | --- | ------ | --- | ------ |
r
Feature importance
| P1  |     |     |     |     | Subjective Index   |     |     | Subjective Index |     | Subjective Index |
| --- | --- | --- | --- | --- | ------------------ | --- | --- | ---------------- | --- | ---------------- |
|     |     | 2   |     |     | Income Shock       |     |     | Literacy Index   |     | Literacy Index   |
|     |     | 3   |     |     | Literacy Index     |     |     | Education Level  |     | Objective Index  |
|     |     | 4   |     |     | Education Level    |     |     | Objective Index  |     | Age Group        |
|     |     | 5   |     |     | Dependent Children |     |     | Age Group        |     | Education Level  |
This preprint research paper has not been peer reviewed. Electronic copy available at: https://ssrn.com/abstract=6826893

16
d
Note: Results are derived from distinct Random Forest applications on each specified pair of
clusters. Higher ranking of feature importance indicates a greater predictive contribution of the
e
variable in distinguishing financial wellbeing profiles.
The “mismatch analysis” behind The Short-Sighted (C3) and The Illiquid Pwlanners (C4)
The intertemporal imbalance of these clusters indicates a critical policy insight. Both
segments present bias, however, the discrimination is not entirely behavioural, but event-
e
driven. The binary classification (accuracy: 0.79) reveals that they represent structurally
different populations influenced by opposing forces.
i
The Random Forest identifies Subjective Index and Incovme Shock as the top-tier
differentiators, as shown in the first column of Table 9. Notably, 58% of The Illiquid Planners
experienced a recent income disruption, compared with 1e6.6% of The Short-Sighted. This
suggests that C4 weakness does not lie in poor financial habits, but rather in liquidity hardship
due to exogenous events, including job loss and business failure. This erosion of C4 short-term
r
stability, despite their long-term assets, is also impacting on their self-assessment, leading to
an unusual decline in its Subjective Index. Conversely, the friction in The Short-Sighted is
structural and, mainly, educational. Only 28.9% orf C3 hold a bachelor’s degree or higher,
leading to a human capital gap compared weith their same-age peers. Their lack of future
preparedness is also exacerbated by their low Financial Literacy Index, meaning a significant
systematic risk. This distinction implies that C4 requires safety nets such as insurance,
e
emergency liquidity, or temporary government funding, while C3 requires structural
interventions in financial literacy and general education.
p
The “survival gradient analysis” behind The Precarious (C5) and The Distressed (C6)
Analysing the vertical transitions at the framework extremes reveals a different
dynamic. At the bottom of the frtamework, comprising C5 and C6, the distinction is driven by
a “poverty trap” mechanismo. Fig. 2 and the second column of Table 9 show that The Distressed
are separated from The Precarious by a set of aggravated negative indicators. They exhibit
consistently lower financial literacy, lower general education, more negative perceptions, and,
n
crucially, greater exposure to income shocks (49.2% vs. 38.7%). In this low-level zone,
mobility is largely shaped by an accumulation of disadvantages, likely exacerbated by the
consequences of COVID-19.
t
The “optimisantion gradient analysis” behind The Resilient (C2) and The Established (C1)
At the top of the framework, composed of C2 and C1, the driver of differentiation shifts
i
from “survival” to “optimisation”. The boundary between The Established and The Resilient
r
is not driven by shocks or income alone, but by marginal gains resulting from cognitive and
matuprity alignment, as shown in Fig. 2 and the third column of Table 9. C1 individuals exhibit
a "synergistic advantage" with higher literacy (+2.03 points), markedly better subjective
perception (+8.88 points), and older age (maturity effect). Specific details regarding this
e
differentiation are presented in the Online Appendix (Fig. B.9). This suggests that transitioning
from “middle class” to “wealthy established” is an evolutionary process driven by the
r
accumulation of assets and confidence over the lifecycle, with financial education playing a
Psignificant mediating role.
5. Discussion
The empirical identification of six distinct profiles challenges the traditional view of
financial wellbeing as a linear and unidimensional construct. By revealing the structural
This preprint research paper has not been peer reviewed. Electronic copy available at: https://ssrn.com/abstract=6826893

17
d
heterogeneity among U.S. households, this study demonstrates that financial wellbeing is
driven by the dynamic interplay between present stability and future security. The following
e
sections discuss the implications of these findings: first, the theoretical necessity of
transcending to robust, comprehensive frameworks (Section 5.1); and second, the practical
shift from generic interventions to tailored and data-driven policies (Sectiown 5.2).
5.1. Theoretical implications: beyond the linear paradigm
e
This study expands the literature on financial wellbeing by shifting the analytical scope
from linear and independent models to a multidimensional and intertemporal framework.
i
Previous research has largely employed continuous gradients (Lusardi & Streeter, 2023; Sticha
v
et al., 2023); however, this study confirms that financial wellbeing is better understood as a
heterogeneous system of behavioural-structural clusters.
e
Specifically, this analysis provides strong support for Netemeyer et al. (2018) regarding
the importance of subjective perceptions. A critical insight from this study is the “subjective
r
dominance effect”, whereby an individual’s self-assessment plays a pivotal role in their
position within the framework, even more than their objective behaviours or literacy levels.
This suggests that psychological strain is not merelry an outcome of financial wellbeing, but a
structural driver that can shift individuals into leower wellbeing clusters or propel them upward.
This creates a feedback loop in which negative perceptions, aggravated by income shocks, can
paralyse decision-making, even among literate individuals, as observed in The Illiquid Planners
e
(C4). The previous insight complements and expands the cyclical phenomenon of financial
wellbeing and mental health acknowledged by Jiménez-Salomon et al. (2024).
p
Furthermore, this research enriches the foundational work of Lusardi and Streeter
(2023) and Wagner and Walstad (2019). Although the well-known “Big Three” questions used
to measure financial literacy constitute a validated metric, this study demonstrates that
t
expanding the scale to capture more complex concepts is critical. A novel finding of this
o
research is that, while basic literacy is necessary for shifts between intermediate clusters (e.g.,
from C5 to C4), mastery of advanced financial knowledge acts as the gatekeeper to the highest
wellbeing tiers (C1 shonws a significant, unusual leap in its Literacy Index compared with C2
and the other clusters). Similarly, the present-future dichotomy in financial wellbeing
measurement cannot be analysed in isolation as it obscures the intertemporal foundation for
individuals profiling. This research highlights that a multidimensional analysis provides
t
valuable insights for uncovering latent risks and optimisation opportunities, which are key to
n
effective policy design.
5.2. Policy aind managerial implications: from generic to precise decision-making
r
The heterogeneity revealed by the six-cluster framework classification argues against a
p
unique, conventional policy intervention. Effective decisions require a data-driven triage
tailored to the specific needs of each group. Based on the insights of this study, a three-tiered
epolicy intervention is proposed.
Tier 1: The structural-based intervention for the vulnerable segments: C5 and C6
r
The Distressed (C6) and The Precarious (C5) require an income stabilisation mechanism and
P
social protection strategies, rather than purely literacy programmes, which are likely to be
insufficient and misdirected. Data indicate that their financial fragility is driven by a systematic
lack of resources, rather than an absence of a money-management guide. For individuals in this
segment, food security and humanitarian transfers are essential to prevent a compounding
This preprint research paper has not been peer reviewed. Electronic copy available at: https://ssrn.com/abstract=6826893

18
d
effect of multidimensional deprivation (Lee, 2023). With the aim of avoiding a positional drop
from C6 to C5, educational interventions are also needed, focusing on survival financial
e
management, where fraud prevention and excessive debt avoidance should be prioritised given
their vulnerable social situation.
w
Tier 2: The equilibrium-based intervention for the middle segments: C3 and C4
Distinguishing The Short-Sighted from The Illiquid Planners is a significant contribution
e
that this research offers to policymakers for effective intervention.
- For The Short-Sighted (C3), their deficit in both generali and financial education
demands priority literacy interventions through mandavtory curricular modifications
with a strong focus on long-term financial awareness. Conversely, the adults who are
no longer part of the traditional education system, a ecommitment contract strategy is an
effective tool to “force” individuals to enrol in saving plans and counteract their present
bias (Halpern et al., 2012).
r
- For The Illiquid Planners (C4), their deficit in contingency planning requires deliberate
preparation through appropriate financial instruments. Better financial education
translates into greater knowledge for this clruster. A policy should focus on resilience
instruments, such as unemployment inesurance or highly liquid savings, reducing the
investment on illiquid assets (e.g., real estate or long-term bonds). This strategy allows
an immediate availability of resources when exogenous shocks occur.
e
Tier 3: The preservation-based intervention for the secure segments: C1 and C2
p
For the high-performing segments, specifically The Resilient (C2) and The Established
(C1), the strategy should focus on wealth preservation and financial literacy upgrades. Since
C1 exhibits privileged knowledge of complex and advanced financial concepts, including
probabilistic and compound intetrest calculations, the intervention should focus on leveraging
C2 financial abilities to proomote an upgrade in their financial profile. Otherwise, given a
demographic profile skewed toward older and wealthier individuals, another policy should
focus on pension maintenance by facilitating low-fee, fiduciary financial advice to avoid capital
n
erosion, which is fundamental for a healthy retirement period.
6. Conclusion
t
This research advances the measurement of financial wellbeing by moving from linear,
n
single-score indices to a comprehensive and replicable framework. Through the application of
a Random Forest algorithm to a nationally representative sample, financial wellbeing
i
measurement is validated as a complex ecosystem consisting of six distinct profiles, where
r
intertemporal connections between short-term preparedness and long-term security provide
signipficant insights.
Beyond the theoretical novelty of the framework, the primary practical contribution is
e
the identification of the “subjective dominance effect”, “imbalance drivers”, and the “advanced
literacy threshold”. These results challenge traditional beliefs by demonstrating that subjective
rperceptions of personal finances are the core driver behind wellbeing segmentation, rather than
material possessions or financial education. This finding suggests that psychological factors
P
act as structural determinants that can either amplify or limit material and cognitive benefits.
Furthermore, while general education strengthens long-term security, advanced financial
proficiency (mastery of complex instruments) is a prerequisite for accessing top-tier financial
profiles, acting as a barrier to entry for the middle class.
This preprint research paper has not been peer reviewed. Electronic copy available at: https://ssrn.com/abstract=6826893

19
d
Crucially, the distinction between The Short-Sighted (C3) and The Illiquid Planners
(C4) resolves a critical ambiguity in the current literature. While both clusters exhibit
e
vulnerability, the underlying drivers are fundamentally different. C3 is constrained by human
capital deficits and behavioural myopia, while C4 is destabilised by exogenous shocks. This
differentiation provides a data-driven insight for accurate policymakwing, shifting from
traditional literacy programmes to tailored interventions on structural deficiencies.
The interpretation of these findings requires the acknoweledgement of specific
methodological constraints. First, the rigorous data pre-processing involves a cleaning
procedure that drops incomplete survey responses. While necessary to ensure index
i
consistency, this may introduce survivorship bias, potentially underrepresenting the individuals
v
with fragmented records, who are often the most vulnerable. Second, the cross-sectional nature
of the data limits temporal analysis, which would enrich the understanding of movement
e
dynamics within the framework across different stages of individuals’ lives. Finally, as the
study is based on the U.S. financial infrastructure, generalisations to emerging economies with
r
different social systems should be approached with caution.
Future research should focus on longitudinal panel data to map the dynamics of
r
individuals shifting between clusters over the lifecycle. Additionally, while this study captures
the unusual effects of COVID-19 economic diesruptions, further research is needed to analyse
how these clusters react to other large-scale macro-stressors, such as political or environmental
crises. Finally, given the primary significance of subjective perceptions demonstrated in this
e
research, future qualitative analysis could provide deeper insight into the mindset gap between
The Established (C1) and The Distressed (C6), promoting educational and psychological
p
mechanisms that may help achieve financial freedom among populations.
Funding
t
This research received no specific grant from any funding agency in the public, commercial,
o
or not-for-profit sectors.
n
t
n
i
r
p
e
References
r
PBreiman, L. (2001). Random Forests. Machine Learning, 45(1), 5–32.
https://doi.org/10.1023/A:1010933404324
This preprint research paper has not been peer reviewed. Electronic copy available at: https://ssrn.com/abstract=6826893

20
d
Brüggen, E. C., Hogreve, J., Holmlund, M., Kabadayi, S., & Löfgren, M. (2017). Financial
e
well-being: A conceptualization and research agenda. Journal of Business Research,
79, 228–237. https://doi.org/10.1016/j.jbusres.2017.03.013 w
Cardona-Montoya, R. A., Cruz, V., & Mongrut, S. A. (2022). Financial fragility and financial
e
stress during the COVID-19 crisis: Evidence from Colombian households. Journal of
i
Economics, Finance and Administrative Science, 27(54)v, 376–393.
https://doi.org/10.1108/JEFAS-01-2022-0005 e
Dolan, P., Peasgood, T., & White, M. (2008). Do we really know what makes us happy? A
r
review of the economic literature on the factor s associated with subjective well-being.
r
Journal of Economic Psychology, 29(1), 94–122.
e
https://doi.org/10.1016/j.joep.2007.09.001
e
FINRA Investor Education Foundation. (2021). 2021 National Financial Capability Study
p
(NFCS) [Dataset]. FINRA Investor Education Foundation.
https://www.finrafoundation.org/knowledge-we-help-create/national-financial-
t
o
capability-study
Greene, M., & Patil, R.n (2023). Understanding the Mental-Financial Health Connection.
Financial Hea lth Network.
t
Halpern, S. D., Asch, D. A., & Volpp, K. G. (2012). Commitment contracts as a way to
n
health. BMJ, 344(jan30 1), e522–e522. https://doi.org/10.1136/bmj.e522
i
r
Haveman, R., & Wolff, E. N. (2005). The concept and measurement of asset poverty: Levels,
p
trends and composition for the U.S., 1983?2001. The Journal of Economic Inequality,
e
2(2), 145–169. https://doi.org/10.1007/s10888-005-4387-y
r
Huston, S. J. (2010). Measuring Financial Literacy. Journal of Consumer Affairs, 44(2), 296–
P
316. https://doi.org/10.1111/j.1745-6606.2010.01170.x
This preprint research paper has not been peer reviewed. Electronic copy available at: https://ssrn.com/abstract=6826893

21
d
James, G., Witten, D., Hastie, T., Tibshirani, R., & Taylor, J. (2023). Introduction. In G.
e
James, D. Witten, T. Hastie, R. Tibshirani, & J. Taylor, An Introduction to Statistical
Learning (pp. 1–13). Springer International Publishing. https://doi.owrg/10.1007/978-3-
031-38747-0_1
e
Jiménez-Solomon, O., Garfinkel, I., Wall, M., & Wimer, C. (2024). When money and mental
i
health problems pile up: The reciprocal relationship betwveen income and
psychological distress. SSM - Population Health, 25e, 101624.
https://doi.org/10.1016/j.ssmph.2024.101624
r
Kahneman, D., & Deaton, A. (2010). High income im proves evaluation of life but not
r
emotional well-being. Proceedings of the National Academy of Sciences, 107(38),
e
16489–16493. https://doi.org/10.1073/pnas.1011492107
e
Karaahmetoğlu, A., Yıldız, M., Ünal, E., Aydın, U., Koraş, M., & Akgün, B. (2025).
p
Efficient, interpretable and automated feature engineering for bank data. Big Data
Research, 40, 100524. https://doi.org/10.1016/j.bdr.2025.100524
t
o
Kuhn, M., & Johnson, K. (2013). Applied Predictive Modeling. Springer New York.
https://doi.org/1n0.1007/978-1-4614-6849-3
Lee, J.-Y. (2023). Ec onomic Inequality, Social Determinants of Health, and the Right to
t
Social Security. Health and Human Rights, 25(2), 155–169.
n
Lusardi, A., Michaud, P.-C., & Mitchell, O. S. (2017). Optimal Financial Knowledge and
i
r
Wealth Inequality. Journal of Political Economy, 125(2), 431–477.
p
https://doi.org/10.1086/690950
e
Lusardi, A., & Mitchell, O. S. (2011). Financial Literacy and Planning: Implications for
r
Retirement Well-being. In O. S. Mitchell & A. Lusardi (Eds.), Financial Literacy:
P
Implications for Retirement Security and the Financial Marketplace (pp. 16–39).
This preprint research paper has not been peer reviewed. Electronic copy available at: https://ssrn.com/abstract=6826893

22
d
Oxford University Press.
e
https://doi.org/10.1093/acprof:oso/9780199696819.003.0002
Lusardi, A., Schneider, D., & Tufano, P. (2011). Financially Fragile Housewholds: Evidence
and Implications. SSRN Electronic Journal. https://doi.org/10.2139/ssrn.1809708
e
Lusardi, A., & Streeter, J. L. (2023). Financial literacy and financial well-being: Evidence
i
from the US. Journal of Financial Literacy and Wellbeinvg, 1(2), 169–198.
https://doi.org/10.1017/flw.2023.13 e
Mahendru, M., Sharma, G. D., Pereira, V., Gupta, M., & Mundi, H. S. (2022). Is it all about
r
money honey? Analyzing and mapping financi al well-being research and identifying
r
future research agenda. Journal of Business Research, 150, 417–436.
e
https://doi.org/10.1016/j.jbusres.2022.06.034
e
Material and social deprivation index 2021: User manual. (2024). Institut national de santé
p
publique du Québec.
Netemeyer, R. G., Warmath, D., Fernandes, D., & Lynch, J. G. (2018). How Am I Doing?
t
o
Perceived Financial Well-Being, Its Potential Antecedents, and Its Relation to Overall
Well-Being. Jounrnal of Consumer Research, 45(1), 68–89.
https://doi.org /10.1093/jcr/ucx109
t
Ringlein, G. V., Ettman, C. K., & Stuart, E. A. (2024). Income or Job Loss and Psychological
n
Distress During the COVID-19 Pandemic. JAMA Network Open, 7(7), e2424601.
i
r
https://doi.org/10.1001/jamanetworkopen.2024.24601
p
Sajid, M., Mushtaq, R., Murtaza, G., Yahiaoui, D., & Pereira, V. (2024). Financial literacy,
e
confidence and well-being: The mediating role of financial behavior. Journal of
r
Business Research, 182, 114791. https://doi.org/10.1016/j.jbusres.2024.114791
P
This preprint research paper has not been peer reviewed. Electronic copy available at: https://ssrn.com/abstract=6826893

23
d
Salignac, F., Hamilton, M., Noone, J., Marjolin, A., & Muir, K. (2020). Conceptualizing
e
Financial Wellbeing: An Ecological Life-Course Approach. Journal of Happiness
Studies, 21(5), 1581–1602. https://doi.org/10.1007/s10902-019-001w45-3
Sorgente, A., Totenhagen, C. J., & Lanz, M. (2022). The Use of the Intensive Longitudinal
e
Methods to Study Financial Well-Being: A Scoping Review and Future Research
i
Agenda. Journal of Happiness Studies, 23(1), 333–358. v
https://doi.org/10.1007/s10902-021-00381-6 e
Spivak, S., Cullen, B., Eaton, W. W., Rodriguez, K., & Mojtabai, R. (2019). Financial
r
hardship among individuals with serious menta l illness. Psychiatry Research, 282,
r
112632. https://doi.org/10.1016/j.psychres.2019.112632
e
Sticha, A., Lusardi, A., & Sconti, A. (2023). Development and testing of a comprehensive
e
financial well-being measure. (201).
p
https://www.tiaa.org/public/institute/publication/2023/development-and-testing-of-a-
comprehensive-financial-well-being
t
o
Theodossiou, I. (1998). The effects of low-pay and unemployment on psychological well-
being: A logistinc regression approach. Journal of Health Economics, 17(1), 85–104.
https://doi.org /10.1016/S0167-6296(97)00018-0
t
Wagner, J., & Walstad, W. B. (2019). The Effects of Financial Education on Short‐Term and
n
Long‐Term Financial Behaviors. Journal of Consumer Affairs, 53(1), 234–259.
i
r
https://doi.org/10.1111/joca.12210
p
World Health Organization. (2021). Health Promotion Glossary of Terms 2021 (1st ed).
e
World Health Organization.
r
Wright, M. N., & König, I. R. (2019). Splitting on categorical predictors in random forests.
P
PeerJ, 7, e6339. https://doi.org/10.7717/peerj.6339
This preprint research paper has not been peer reviewed. Electronic copy available at: https://ssrn.com/abstract=6826893

24
d
Zytek, A., Arnaldo, I., Liu, D., Berti-Equille, L., & Veeramachaneni, K. (2022). The Need for
e
Interpretable Features: Motivation and Taxonomy. ACM SIGKDD Explorations
Newsletter, 24(1), 1–13. https://doi.org/10.1145/3544903.3544905w
e
i
v
e
r
r
e
e
p
t
o
n
t
n
i
r
p
e
r
P
This preprint research paper has not been peer reviewed. Electronic copy available at: https://ssrn.com/abstract=6826893