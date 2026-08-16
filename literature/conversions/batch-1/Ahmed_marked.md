---
conversion_metadata:
  converted_at: "2026-07-22T11:49:26Z"
  converter_tool: "markitdown"
  converter_version: "0.1.6"
  source_pdf: "Ahmed.pdf"
  source_pdf_sha256: "3c7ce77d30ce7183000a2af702333b53ccbf17f3b88f965a93080e20d20ea96d"
  page_count: 10
  markdown_char_count: 96510
---

<!-- PAGE-AWARE EXTRACTION (via pdfminer.six) -->

<!-- PAGE 1 -->

American International Journal of Business Management (AIJBM) 
ISSN- 2379-106X, www.aijbm.com Volume 9, Issue 06 (June - 2026), PP 44-53

AI-Driven Credit Risk Assessment in Fintech Lending: 
Implications for Financial Inclusion, Systemic Risk, and 
Regulatory Governance

SYED IJAZ AHMED 
Department Of Entrepreneur & Leadership, University Of Derby, United Kingdom 
Corresponding Author: Syed Ijaz Ahmed

ABSTRACT: Artificial intelligence (AI) and machine learning (ML) in fintech lending have revolutionized credit 
risk assessment,  enhanced financial  inclusion, but raised challenges to governance, such as algorithmic fairness, 
systemic  stability,  and  regulatory  sufficiency.  The  given  paper  provides  a  systematic  literature  review  and 
analytical  synthesis  of  AI-based  credit  risk  assessment  in  the  context  of  fintech  lending,  relying  on  30  peer-
reviewed articles that were published in 2012 and 2025. The paper compares the  performance of ML models to 
traditional  scoring  principles,  examines  the  dynamic  of  financial  inclusion  and  digital  exclusion,  and  suggests  a 
five-stage governance framework called the Integrated AI Credit Risk Framework (IACRF), which is an original 
operationalization of the SAFE AI principles of statistical  accuracy, algorithmic  fairness, financial  stability, and 
ethical  governance.  Results  show  that  ensemble  and  hybrid  explainable  AI  models  have  better  classification 
compared to those without governance, and their use without good governance increases inequality, systemic risk, 
and  exceeds  regulatory  capacity.  The  paper  ends  by  giving  specific  policy  suggestions  to  regulators,  fintech 
companies,  and  multilateral  development  agencies  to  find  a  balance  between  credit  innovation  and  financial 
stability as well as borrower equity.

KEYWORDS - Artificial Intelligence in Finance; Credit Risk Assessment; Fintech Lending; Machine Learning 
Credit Scoring; Financial Inclusion; Algorithmic Bias; Systemic Risk; Explainable AI (XAI)

I.   INTRODUCTION

In  its  contemporary  history,  the  financial  services  sector  is  witnessing  one  of  the  most  significant 
transformations  due  to  the  interplay  of  big  data  analytics,  artificial  intelligence  (AI),  and  the  digital  platform 
economics.  In  this  transformation,  credit  risk  assessment  has  become  not  just  the  main  place  of  AI 
implementation and where the technology has most of its most promising and dangerous implications are felt, 
but  also  the  location  where  the  technology  has  had  the  biggest  impacts.  Over  the  decades,  the  credit  risk 
assessment  market  has  been  dominated  by  more  classical  statistical  models  -  mainly  logistic  regression  and 
FICO scoring system, basing their analysis on structured credit bureau information, including payment history, 
credit  usage,  and  debt-to-income  ratios.  Although  these  instruments  could  offer  practical  estimates  of  default 
probability, they have avoided much of the population with no record of formal credit using bureau coverage at 
a  rate  that  can  be  below  20  percent  of  the  adult  population,  which  is  especially  true  in  emerging  economies 
where bureau coverage rates can drop to below 20 percent of the adult population [1].

It is against this backdrop that fintech lenders have used AI and ML architectures to process alternative 
data sources both in scale and speed more than ever before. Mobile phone usage and utility payment history, e-
commerce  history,  and  behavioral  indicators  are  some  of  the  proxies  of  creditworthiness  that  have  been 
pioneered by platforms like  Lending Club,  Ant Financial, and PayPal credit and deliver  quantifiable  financial 
inclusion benefits [2, 3]. Simultaneously, as opaque, data-dense AI models start proliferating, they have brought 
about governance issues, which industry standards and regulatory frameworks have not so far addressed.

There are three key tensions of the modern problem of AI-based credit risk assessment. The former is 
the accuracy explainability trade-off: the new generation of ensemble and deep learning models is more accurate 
than the traditional scorecards, but are black-box models that are difficult to interpret because of the demands of 
regulators  and  borrowers  [4,  5].  The  second  one  is  the  inclusion-bias  paradox:  alternative  data  pipelines  that 
credit  populations  that  it  previously  did  not  credit  are  also  at  risk  of  incurring  structural  discrimination  and 
amplifying the effect on the classes being protected, which can lead to disparate effects [6]. The third one is the 
stability-innovation dilemma: the systemic risk vectors (model herding, procyclicality, and platform contagion) 
of  the  interconnectedness  of  fintech  lending  platforms  cannot  be  identified  or  addressed  by  conventional 
prudential frameworks [7, 8].

The  paper  has  managed  to  focus  on  these  tensions  based  on  a  systematic  review  and  analysis  of  the 
empirical  and  theoretical  literature  on  AI-based  fintech  credit  risk.  It  suggests  an  innovative  five-step 
governance  framework,  the  Integrated  AI  Credit  Risk  Framework  (IACRF),  operationalizing  the  SAFE  AI

*Corresponding Author: SYED IJAZ AHMED1                  www.aijbm.com                            44 | Page

---

<!-- PAGE 2 -->

AI-Driven Credit Risk Assessment in Fintech Lending: Implications for Financial Inclusion…

principles  throughout  the  entire  operational  lifecycle  of  a  fintech  credit  system,  and  coming  up  with  policy 
proposals  to  regulators,  practitioners,  and  development  finance  institutions.  The  paper  has  the  following 
structure: in Section II, the literature review will be done on eight thematic domains; Section III will construct 
the theoretical framework and IACRF; Section IV will outline the methodology; Section V will summarize the 
results and discussion, and finally, Section VI will be a conclusion.

II.   LITERATURE REVIEW

2.1 Evolution of Credit Risk Assessment: From Traditional Models to AI

Formal  credit  risk  assessment  dates  back  to  the  logistic  regression-based  scorecards  created  in  the 
1950s  and  1960s,  with  Altman's  (1968)  Z-score  for  corporate  bankruptcy  prediction,  and  extends  through  the 
institutionalization of the FICO score in consumer lending in 1989. The traditional methods presuppose linear 
relationships  between  predictors,  are  vulnerable  to  multicollinearity,  and  rely  on  pre-determined  choice  of 
variables  -  features  that  are  not  well  aligned  to  the  high-dimensional  and  nonlinear  data  conditions  of  the 
contemporary digital lending [4, 9]. The shortcomings of bureau-based scoring opened the door to ML methods 
that can handle complex feature interactions, adapt to new data patterns, and handle unstructured inputs. Since 
the mid-2010s, decision trees, random forests, gradient boosting machines, especially XGBoost and LightGBM, 
and neural network architectures have started to enter fintech lending businesses, with improvements of 5 to 15 
percentage  points over logistic regression  models in  terms  of  AUC-ROC [10, 4]. The latest  frontier is adding 
explainability  mechanisms,  such  as  SHAP  values,  LIME,  and  integrated  gradients,  to  high-performing  ML 
architectures,  which  partially  closes  the  divide  between  the  performance  of  a  model  and  regulatory 
interpretability [5, 11]. 
2.2 Fintech Lending: Market Structure, Growth Dynamics, and Bank Interactions

The world fintech lending sector has evolved to become a multi-trillion-dollar business, including peer-
to-peer (P2P) lending, marketplace lending, balance sheet schemes, embedded finance, and buy-now-pay-later 
(BNPL).  [2]  chronicle  the  way  varying  fintech  business  models  take  advantage  of  AI  to  lower  underwriting 
expenses,  speed  up  the  process  of  credit  decisioning  (from  days  to  seconds),  and  serve  underserved  borrower 
groups not served by existing banks. [12] discovers that fintech lending does not replace access to bank credit in 
U.S. consumer  markets,  whereas [13] reveal that  the banking  market concentration determines the chances of 
fintech entering the market. According to [1], financial inclusion and development are some of the determinants 
of  fintech  and  BigTech  lending  volumes  that  are  recorded.  Notably,  [14]  discovered  that  the  fintech  credit-
exposed firms show higher bankruptcy rates in troughs, which casts doubt on the idea that AI-enhanced credit 
expansion can lead to a faster misallocation of risk in some segments of the credit portfolio and highlights the 
necessity to incorporate the through-the-cycle performance of credit models, as opposed to in-sample accuracy. 
2.3 Machine Learning Models for Credit Risk: Comparative Performance

This  systematic  review  by  [4]  confirms  that  the  ensemble  techniques  have  always  achieved  higher 
performance than the logistic regression benchmarks on all the datasets, evaluation  metrics, and  markets. The 
use  of  gradient  boosting  algorithms,  especially  XGBoost  and  LightGBM,  has  become  the  tool  of  choice  in 
fintech  credit  scoring,  providing  better  missing  data  behavior,  resistance  to  overfitting,  and  good  tabular  data 
behavior.  [10]  illustrate  that  a  hybrid  XAI  model  that  takes  the  form  of  gradient  boosting  with  SHAP-based 
explainability can attain an AUC-ROC of 0.89 as compared to a logistic regression baseline of 0.76, and meets 
the adverse action notice criteria. Similar conclusions are made by [11]  with regard to trade credit risk, and [9] 
demonstrate  that LSTM networks give an AUC-ROC over 0.90 with enterprise credit data used, but at a high 
interpretability cost. The results show that there is a performance hierarchy: deep learning models have marginal 
benefits in data-rich settings, and ensemble approaches are the most risk-adjusted option in real-world fintech 
applications. Table 1 summarises comparative performance evidence in the literature reviewed. 
Table 1: Comparative performance of ai/ml models in credit risk assessment

Model Type

AUC-ROC 
Range

Gini Coeff.

Interpretability  Fairness

Logistic Regression

0.68 – 0.77

0.36 – 0.54

High

Decision Tree

0.70 – 0.78

0.40 – 0.56

High

Random Forest

0.79 – 0.86

0.58 – 0.72

Low-Medium

Partial

XGBoost / LightGBM

0.83 – 0.91

0.66 – 0.82

Low

Partial

Compliance

Partial

Partial

Regulatory 
Suitability

High

High

Medium

Medium

LSTM / Deep Learning

0.85 – 0.93

0.70 – 0.86

Very Low

Unclear

Low

*Corresponding Author: SYED IJAZ AHMED1                  www.aijbm.com                            45 | Page

---

<!-- PAGE 3 -->

AI-Driven Credit Risk Assessment in Fintech Lending: Implications for Financial Inclusion…

Hybrid 
(SHAP/LIME)

XAI

0.84 – 0.92

0.68 – 0.84  Medium-High

Yes 
(Conditional)

Medium-
High

2.4 Financial Inclusion and AI-Driven Credit Expansion

[3]  shows  that  when  used  on  alternative  data  (mobile  usage,  records  of  digital  payments,  behavioral 
indicators),  ML  models  produce  creditworthiness  estimates  of  thin-file  borrowers  just  as  accurate  as  the 
traditional scoring on bureau-rich groups, and it is especially interesting in Sub-Saharan Africa, South Asia, and 
Southeast  Asia.  [14]  list  digital  financial  literacy  and  perceived  regulatory  support  as  the  most  important 
mediating variables, and it is important to highlight that the groups facing the highest likelihood of benefiting 
due to AI-driven credit expansion are the same most vulnerable to using AI-based credit products. In a study by 
[16],  the  benefits  of  fintech  inclusion  are  being  recorded  to  be  among  digitally  connected  groups,  posing  a 
second-order challenge of exclusion. [17] also adds that the pace of digital credit and its magnitude pose the risk 
of  overleverage  in  newly  added  borrowers  within  a  short  time.  The  composite  financial  inclusion  index  of 
developing  economies  presented  in  the  study  by  [18]  shows  that  access  indicators  tend  to  conceal  quality 
differences. Nominally included populations can have AI-generated credit products that have prohibitive interest 
rates and punitive default fees that harm and do not improve financial well-being. 
2.5 Algorithmic Bias, Fairness, and Ethical Dimensions

Algorithms'  bias  in  credit  scoring.  The  systematic  bias  of  AI  models  to  hurt  the  interests  of  the 
protected  groups  is  known  as  algorithmic  bias:  racial  minorities,  women,  and  older  adults.  [6]  show  that 
behavioral  biases  are  coded  in  an  ordered  manner  in  AI  systems  that  are  trained  on  biased  data  in  the  past. 
IJCATR  (2025)  analysis  reveals  that  the  discriminatory  patterns  are  seen  with  the  use  of  XAI  techniques, 
whereas visibility is not necessarily followed by remediation. The sources of bias can be categorized into three 
pipeline  stages:  pre-processing  (historical  training  data  based  on  past  discrimination),  in-processing  (model 
architecture decisions implicitly related to the protected attributes), and post-processing (use on populations that 
are  not  in  the  same  distribution  as  the  training).  [5]  posit  that  technical  debiasing,  such  as  re-sampling, 
adversarial  debiasing,  and  fairness  constraints,  cannot  be  effectively  used  without  institutional  accountability 
mechanisms, such as having  mandatory audits on algorithms, publishing fairness  measurements, and allowing 
recourse rights. The lack of these in the majority of the regulatory frameworks is the key gap in governance in 
the area of algorithmic fairness. 
2.6 Systemic Risk, Financial Stability, and Fintech Interconnectedness

[7]  prove  the  existence  of  tail-risk  spillovers  between  financial  institutions,  and  that  correlated  asset 
exposures  increase  the  tail-risk  spillovers  between  financial  institutions,  a  phenomenon  that  AI  lending 
promotes in the lending system via model convergence. In their record, [8] report a high level of systemic risk, 
which is due to the high growth rate of credit, the low capital adequacy, and reliance on wholesale funds. [19] 
lists  three  channels  of  systemic  risk:  the  concentration  of  powerful  platforms,  interconnectedness  via  API 
integrations with banking counterparties, and the lack of accessibility to the algorithms behind credit decisions 
made  by  algorithms  by  supervisors.  [20]  determine  that  systemic  risk  propagation  in  bank-firm  networks  is 
greatly moderated by the regulatory policy environment, whereas [21]  build on this to compound systemic risk 
due  to  the  interdependence  of  finance,  technology,  energy,  and  geopolitical  systems  -  environments  that  AI 
credit systems can enhance procyclical allocation. 
2.7 Regulatory Frameworks and AI Governance in Lending

[22] presents the initial examination of the problem of AI governance in financial services, which he 
describes as regulatory arbitrage, systemic openness, and discriminatory results as the three main risks that the 
government needs to approach in its strategy. [23] defines credit scoring AI as a high-risk category, which must 
have conformity tests, documentation of training data, human supervision, and explainability compliance. The 
Basel Committee has provided guidance on model risk management that requires validation of AI credit models, 
monitoring, and documentation of AI credit models. The U.S. CFPB has applied the requirements of the Equal 
Credit  Opportunity  Act  to  AI-generated  decisions  relating  to  adverse  actions,  but  has  not  applied  the 
requirements  to  non-bank  fintech  platforms  whose  enforcement  ability  is  limited.  A  structural  issue  that  is 
identified in the bibliometric analysis of [24] is regulatory arbitrage, i.e., the migration of model deployment to a 
jurisdiction with lighter regulation for fintech firms that needs to be coordinated internationally by the Financial 
Stability Board and Basel Committee. 
2.8 Identified Gaps in the Existing Literature

The  contributions to this paper are  inspired by four gaps. First, the streams of research  on the  model 
performance,  inclusion,  bias,  and  systemic  risk  are  relatively  isolated,  and  there  are  very  few  studies  that 
combine model-level analysis and macro-prudential assessment. Second, the literature on AI credit dynamics is 
strongly  biased  towards  North  American  and  European  situations,  and  little  is  known  about  the  AI  credit 
dynamics  in  Sub-Saharan  African  and  Southeast  Asian  fintech  markets.  Third,  there  is  no  currently  existing 
*Corresponding Author: SYED IJAZ AHMED1                  www.aijbm.com                            46 | Page

---

<!-- PAGE 4 -->

AI-Driven Credit Risk Assessment in Fintech Lending: Implications for Financial Inclusion…

system of governance that considers model-level explainability, fairness of borrowers, and systemic stability of 
the market at the same time in a single architecture that is tuned to fintech. Fourth, full-cycle empirical studies 
of the performance of AI credit models do not exist to allow sufficient evaluation of the procyclicality risks.

III.   THEORETICAL FRAMEWORK

3.1 Theoretical Anchors

The article is based on three theoretical traditions that are complementary. The information asymmetry 
theory  [25,  26]  provides  that  credit  market  inefficiencies  are  a  result  of  the  inability  of  lenders  to  completely 
monitor the type of borrower. Thought to be advanced information processors, AI credit systems are theorized 
to decrease the lender-side asymmetries with increased and more diverse datasets. But they also introduce new 
borrower-side  asymmetries,  hidden  algorithmic  judgments,  which  could  not  be  comprehended,  challenged,  or 
acted  upon  by  those  impacted,  creating  a  lack  of  fairness  and  accountability,  which  the  SAFE  AI  literature 
recognizes [5]. The literature on financial innovation [27] sees AI-driven fintech as an institutional change that 
can  be  caused  by  the  interplay  of  the  availability  of  data,  the  power  of  computers,  and  the  opportunity  of 
regulation  all  of  which  are  essentially  institutional,  but  not  technical,  in  nature.  The  macro-prudential  theory 
behind the development of the correlated AI credit models is known as systemic risk theory [7], which is based 
on the tail-risk spillover effects of generating systemic vulnerability due to the existence of monoculture risks 
that are not diversifiable. 
3.2 The SAFE AI Framework

The IACRF normative architecture is based on the normative architecture of [5] SAFE AI framework. 
The four SAFE pillars, Statistical accuracy, Algorithmic fairness, Financial stability and Ethical governance are 
operationalized  in  the  context  of  fintech  lending  as:  (a)  minimum,  validated  out-of-sample  performance 
thresholds;  (b)  published  parity  conditions  across  the  three  or  more  protected  groups  with  audited  disparate 
impact; (c) stress-tested resistance to procyclical behavior, model herding and systemic The SAFE framework is 
claimed to be more suitable in the high-stakes credit situations than single-objective accuracy optimization since 
it is a framework that takes into account all the aspects of the governance risk simultaneously. 
3.3 The Integrated AI Credit Risk Framework (IACRF)

The main theoretical contribution of the paper is the IACRF: a multi-level governance framework that 
is  a  map  of  four  pillars  of  the  SAFE  AI  onto  the  operational  lifecycle  of  a  fintech  credit  system  in  five 
consecutive,  iterative  steps.  The  framework  is  developed  in  a  way  that  it  is  applicable  to  both  mature  and 
emerging  markets,  where  the  regulation  is  at  either  the  firm  or  regulatory  interface  level.  The  IACRF 
architecture is shown in Fig.1

Stage 1 
Data goverance 
Accuracy pillar

Stage 5 
Impact evaluation 
All four pillars

Stage 2 
Model design 
Accuracy + fairness

Stage 4 
Regulatory interface 
Ethics + stability

Stage 3 
Deployment arch 
Stability + fairness

Figure 1: The integrated ai credit risk framework (iacrf) — conceptual architecture

Stage  1:  Data  Governance:  The  area  deals  with  the  data  sourcing,  quality  management,  consent 
architecture, training data bias audit, and representativeness standards, and operationalizes the SAFE accuracy 
pillar.  Stage  2:  Model  Design  regulates  the  choice  of  architecture,  integration  of  fairness  constraints,  the

*Corresponding Author: SYED IJAZ AHMED1                  www.aijbm.com                            47 | Page

---

<!-- PAGE 5 -->

AI-Driven Credit Risk Assessment in Fintech Lending: Implications for Financial Inclusion…

specification of explainability mechanisms, a documentation of proxy variables, as well as pre-deployment bias 
audits, operationalising SAFE accuracy and fairness. Stage 3: Deployment Architecture takes care of real-time 
scoring  infrastructure,  performance  degradation  checks,  distributional  shift  checks,  human  override  checks, 
regulatory  audit  trail  maintenance,  and  operationalizes  SAFE  stability  and  fairness.  Stage  4:    Regulatory 
Interface regulates model validation documentation, adverse action notice procedures, supervisory coordination, 
and  periodic  model  risk  assessment,  operationalises  SAFE  ethics  and  stability.  Stage  5:  Impact  Evaluation 
includes financial inclusion impact analysis by demographic groups, systemic risk monitoring, the presence of 
market-level  credit  correlation  and  concentration,  and  public  impact  reporting,  and  puts  all  four  SAFE  pillars 
into action at once. 
3.4 Theoretical Propositions

The  IACRF  and  literature  synthesis  give  rise  to  four  propositions:  (P1)  AI  credit  models  are  more 
predictive  than  traditional  methods  but  have  interpretability  limitations  leading  to  a  conflict  of  regulation  in 
adverse-action jurisdictions. (P2) Fintech lending based on AI financial inclusion benefits in data-rich settings, 
but does not reach the digitally low populations, enabling a second-order dynamic of AI-based exclusion. (P3) 
The  systemic  risk  is  exacerbated  by  market-wide  adoption  of  correlated  AI  credit  models  that  create  tail-risk 
spillovers,  and  the  model  herding  and  coordinated  credit  tightening  of  models,  which  have  larger  tail-risk 
spillovers  than  traditional  credit  monocultures.  (P4)  Adoption  of  IACRF-specified  governance  mechanisms, 
such as explainability integration, bias auditing, and systemic risk monitoring, is positively linked to regulatory 
compliance and financial stability in AI-driven lending.

4.1 Research Design and Protocol

IV.   METHODOLOGY

The present paper has a position of interpretivist-constructivist in a qualitative research design, which 
is  theory-building  in  nature.  It  combines  both  published  empirical  and  theoretical  studies  to  formulate  the 
IACRF and come up with policy implications, as is customary in high-impact journals in finance to contribute to 
a theoretical framework [2, 24]. The review of the literature is based on a PRISMA-inspired guideline. Searches 
were  done  and  regulatory  repositories  of  the  European  Banking  Authority,  the  U.S  CFPB,  and  the  Financial 
Stability Board. Keywords  were: 'AI credit risk,'  machine  learning  fintech lending, algorithmic credit scoring, 
and  fintech  systemic  risk.  Secondary  terms  were:  explainable  AI  finance,  algorithmic  bias  credit,  financial 
inclusion fintech, and credit model governance. This was during the period 2012-2025, but with a focus on 2021 
and  beyond.  Preliminary  search  results  of  about  280  documents  were  narrowed  down  by  filters  such  as 
duplicates,  title and abstract filtering, and quality  filtering that filtered out non-peer-reviewed sources to get a 
final corpus of 30 peer-reviewed articles and regulatory reports. Fig. 2 shows  how the screening is done. The 
analysis and framework development of comparative models will be conducted at this phase.

Figure 2: Prisma informed literature search and screening flowchart

4.2 Comparative Model Analysis and Framework Development

To analyze the performance of the comparative model in Section V, performance information reported 
in  studies  reviewed  is  gathered  and  tabulated  into  a  comparative  table.  Measurements  AUC-ROC,  Gini

*Corresponding Author: SYED IJAZ AHMED1                  www.aijbm.com                            48 | Page

---

<!-- PAGE 6 -->

AI-Driven Credit Risk Assessment in Fintech Lending: Implications for Financial Inclusion…

coefficient,  and  KS  statistic  are  tabulated  by  model  type  with  performance  ranges  instead  of  point  estimates 
being  used  to  address  heterogeneity  in  cross-study  characteristics  of  the  datasets  and  their  methodology.  The 
IACRF is formulated using the iterative framework construction approach of [28]. Theory and evidence are used 
to construct the theory using theory as the building blocks, and then iterate the relationship among the building 
blocks  to  develop  sufficient  specifications  in  the  framework  to  create  testable  propositions.  The  framework 
constructs are checked against published frameworks of fintech governance by a consistency check to make sure 
the structures are complete.

V.   RESULTS AND DISCUSSION

5.1 AI Model Performance: Comparative Analysis

The  evidence  of  the  comparison  proves  Proposition  1.  Gradient  boosting  models  are  able  to  attain 
values of 0.83-0.91 in AUC-ROC, which are 7-19 percentage points higher than the logistic regression baselines 
[4, 10]. Such returns have an economic impact: a 5-percentage-point improvement in the AUC-ROC is directly 
translated  into  lower  levels  of  false  positives  (creditworthy  borrowers  denied  credit)  and  false  negatives 
(defaulters granted credit) rates,  which improve  the quality of the portfolio and access to credit by borrowers. 
The best balance between performance and explainability is the hybrid XAI model [10]: SHAP attribution in a 
gradient  boosting  framework  can  be  applied  to  achieve  almost  the  same  accuracy  of  the  ensemble  as  well  as 
meet the adverse action criteria. Nonetheless, SHAP explanations are local models, which might not capture the 
behavior of global models, and their implementation is too complex to be adopted by smaller fintech operators. 
The  highest  reported  performance  (AUC-ROC  >  0.90)  comes  with  LSTM  architecture,  which  is  virtually 
incompatible  with  EU  AI  Act  high-risk  classification  requirements  on  its  black-box  nature  and  therefore,  is 
prone  to  be  adopted  by  the  less-regulated  market-driven  force  of  emerging  markets,  a  regulatory  arbitrage 
dynamic that needs supervisor consideration [9]. 
5.2 Financial Inclusion: Opportunities and Structural Contradictions

Evidence  reveals  that  there  is  qualitative  support  for  Proposition  2.  In  new  market  environments,  AI 
credit models on alternative data increase the rate of approval of thin-file and unbanked borrowers by 20 to 40 
percentage  points [3],  which  is an appreciable gain in terms of access to credit  to small business owners, gig 
economy workers, and rural households, who relied on informal credit before. There are limits to inclusionary 
potential, however, due to structural contradictions. The invisibility of some groups of people that do not have 
access to smartphones, connectivity, or a history of digital transactions leads to a coverage gap that AI models 
fail to predict unless non-digital sources of data are included [16]. Although allowing the approval of excluded 
borrowers  potentially  places  them  in  high-risk  pricing  tiers  that  would  earn  high  interest  rates,  potentially  far 
exceeding market rates, AI risk stratification granularity can also be dynamic in that nominal inclusion comes at 
a cost that can lead to financial ill health [17, 15]. Table 2 provides an overview of financial inclusion indicators 
in an AI-driven lending setting, by region. 
Table 2: Financial inclusion metrics across ai-driven lending contexts by region

Region

Platform Type

Key 
Data

Alternative

Approval 
Rate Uplift

Interest  Rate 
Premium

Digital 
Exclusion 
Risk

Sub-Saharan 
Africa

Mobile  Money  / 
P2P

Mobile  usage,  M-
PESA, airtime

30–45%

8–18%  above 
base

Very 
High

Southeast Asia  Digital  Bank

/

BNPL

E-commerce, 
share, social

ride-

20–35%

5–14%  above 
base

High

Latin America  Marketplace

Lending

Bill  payment,  utility, 
telco

15–28%

4–12%  above 
base

Medium-
High

European 
Union

Embedded 
Finance / BNPL

Open  banking,  PSD2 
data

8–15%

North America  Fintech

Marketplace

Rent, 
income

utility,

gig

10–20%

1–5% 
base

2–8% 
base

above

Low-
Medium

above

Low

*Corresponding Author: SYED IJAZ AHMED1                  www.aijbm.com                            49 | Page

---

<!-- PAGE 7 -->

AI-Driven Credit Risk Assessment in Fintech Lending: Implications for Financial Inclusion…

5.3 Algorithmic Bias: Technical Evidence and Institutional Imperatives

The  argument  that  institutional  accountability  structures,  in  conjunction  with  technical  debiasing,  are 
necessary  is  strongly  supported  by  the  evidence  [5].  [6]  show  that  AI  systems  can  produce  behavioral  biases 
methodically encoded within their designs based on the biases in the historical data used to train them - a credit 
model that learns the discriminatory approval and default patterns of decades learns to recapitulate those biases 
as  predictions,  despite  not  being  trained  to  do  so  on  purpose.  The  XAI  analysis  of  the  IJCATR  (2025) 
establishes  that  SHAP  and  LIME  are  more  effective  than  naive  debiasing  in  identifying  the  existence  of 
discriminatory patterns. Still,  it is  not able to remediate  them, and that performance-fairness trade-offs render 
naive debiasing commercially unfeasible among thin-margin fintech operators. The key institutional loophole is 
that in most major regulatory frameworks, such as the [23], mandatory independent bias auditing, disclosure of 
public fairness metrics, and enforceability of a right to recourse by borrowers are not mandatory, including the 
[23], which provides conformity assessment documentation, but does not mandate periodic third-party audits or 
disclosure of fairness metrics to the public. The priority regulatory reform to bridge this gap would be to set up 
mandatory bias auditing requirements and to enforce this requirement by the supervisory authority. 
5.4 Systemic Risk Propagation Pathways

Systemic vulnerability is enhanced by three different propagation pathways, which amplify the effects 
of AI-based fintech lending and support Proposition 3. Model herding is caused by converging industry-wide to 
similar gradient boosting architectures, and overlapping alternative data pipelines: a macroeconomic shock that 
causes the predictive value of behavioral data to fall at once causes credit assessments of all institutions using 
that  information  to  become  coordinated  in  tightening  their  credit  policies,  a  phenomenon  that  is  directly 
analogous to the correlated asset exposure problem reported by [7]. The AI models trained on expansionary data 
can  be  procyclical  because  they  can  implicitly  link  good  times  with  creditworthiness  and  can  produce 
permissive calibrations when there is a boom and sudden contractions when there is a downturn, and amplify the 
business  cycle  via  the  credit  channel  [21].  Contagion  between  platforms  occurs  as  a  result  of  institutional 
interconnectedness, which comes in the form of API integrations, similar banking infrastructure, and secondary 
market  securitization:  a  model  failure  in  governance  or  a  cyberattack  on  a  large  platform  at  machine  speed 
spreads to investors, counterparty banks, and  secondary  market participants even before  the conventional risk 
systems can react [8].

Figure 3: Systemic risk propagation pathways in ai-driven fintech lending

5.5 Regulatory Governance: Comparative Jurisdictional Analysis

The comparative study proves the existence of a disjointed and jurisdiction-based unequal governance 
environment.  Table 3 looks at the  AI credit governance frameworks in  five regulatory jurisdictions in aspects 
that are directly pertinent to the SAFE AI pillars.

*Corresponding Author: SYED IJAZ AHMED1                  www.aijbm.com                            50 | Page

---

<!-- PAGE 8 -->

AI-Driven Credit Risk Assessment in Fintech Lending: Implications for Financial Inclusion…

Table 3: Comparative ai credit governance frameworks by jurisdiction

Jurisdiction  Primary

Instrument

Explainability 
Req.

Bias  Audit 
Mandate

Model 
Validation 
Std.

Enforcement  Gov. 
Gap 
Score

United 
States

ECOA  /  CFPB 
Guidance

Partial 
(Adverse 
Action)

No 
(Voluntary)

SR 
11-7 
(Banks only)

CFPB  Civil 
Action

3 / 5

European 
Union

EU  AI  Act 
(2024)

(High-

Yes 
Risk Class)

United 
Kingdom

FCA  Consumer 
Duty

China

PBOC 
Algorithm Reg.

Yes 
(Outcome-
Based) 
Partial 
(Disclosure)

Yes 
(Conformity 
Assess.) 
Yes 
Treatment)

(Fair

Partial

CE  Marking 
+ EBA

/  Nat.

EBA 
Supervisors

2 / 5

FCA  Model 
Risk 
Guidance 
PBOC  Tech. 
Standards

FCA 
Supervisory

2 / 5

PBOC 
Administrative

3 / 5

Emerging 
Markets

Varies 
Minimal

/

Rarely 
Required

Rarely 
Required

Absent 
Informal

or

Limited 
Capacity

5 / 5

There  are  two  overall  findings.  To  start  with,  the  [23]  is  the  most  up-to-date  best-practice  model 
(closest to Stage 4 (Regulatory Interface) of the IACRF), but it is still not sufficient in the systemic risk aspect 
(there is no systemic risk tool in the EU to monitor AI-based credit concentration or procyclicality at the market 
level on the  same level as macroprudential banking supervisor instruments). Second, there is a higher level of 
governance gaps in the emerging markets since regulatory capacity in the emerging markets is the least, and the 
populations that are the most vulnerable to the inclusion-bias paradox are concentrated in the emerging markets. 
This  imbalance  requires  global  coordination  with  the  FSB  and  Basel  Committee  to  avoid  a  global  AI  credit 
governance system that will be based on two levels, where the most vulnerable groups will be least safeguarded.

6.1 Summary of Findings

VI.   CONCLUSION

The  paper  summarizes  30  peer-reviewed  articles  on  the  topic  of  AI-based  credit  risk  assessment  in 
fintech  lending  that  came  up  with  findings  in  four  dimensions.  Ensemble  and  hybrid  XAI  models  offer 
economic  material  benefits  to  traditional  scorecards  on  model  performance,  yet  the  performance  hierarchy  is 
coupled  with  interpretability  shortcomings  that  pose  real  regulatory  problems  that  arise  in  adverse-action 
jurisdictions. On financial inclusion, AI credit systems expand access rates to thin-file and unbanked borrowers 
by  significant  percentages  in  new  markets,  but  inherent  contradictions  of  digital  inclusion,  AI-driven  pricing 
bias,  and  excessive  leverage  constrain  and  even  hinder  the  potential  of  inclusion.  Three  new  propagation 
pathways  at  the  intersection  of  credit  and  financial  market  interconnections  driven  by  AI:  model  herding, 
procyclicality,  and  platform  contagion,  give  rise  to  systemic  vulnerability  and  are  left  unaddressed  by  current 
prudential frameworks in detecting and mitigating them. Regarding regulatory governance, the world market is 
divided  and  unbalanced,  with  jurisdictional  and  the  [23]  skewing  to  best  practice  without  addressing  the 
systemic risk aspect, and new markets experiencing the greatest governance gap. 
6.2 Theoretical Contributions

Three main contributions are promoted. To start with, the IACRF offers a novel multi-level governance 
architecture  to  combine  the  SAFE  AI  imperatives  and  the  fintech  credit  lifecycle  in  five  stages  of  operation, 
filling the uncharted gap in frameworks that jointly focus on model-level performance and fairness, firm-level 
compliance,  and  market-level  systemic  risk.  Second,  a  theoretically-based  taxonomy  of  systemic  risk 
propagation  pathways  that  are  particular  to  AI-powered  fintech  lending  is  introduced  that  builds  on  the 
connectedness  framework  by  [7]  in  the  algorithmic  credit  environment.  Third,  the  theory  of  information 
asymmetry,  the  theory  of  financial  innovation,  and  the  SAFE  AI  framework  are  brought  into  a  consistent 
analytical  framework  that  proves  these  traditions  to  be  mutually  reinforcing  and  how  integrating  them  brings 
insights into governance that none can bring forth alone. 
6.3 Policy Recommendations

There are four sets of recommendations that are promoted. To regulators and central banks: AI credit 
models  with  more  than  a  specified  level  of  deployment  should  be  required  to  have  explainability  and  an 
independent bias audit, coordinated by the Basel Committee and FSB, to avoid regulatory arbitrage; systemic

*Corresponding Author: SYED IJAZ AHMED1                  www.aijbm.com                            51 | Page

---

<!-- PAGE 9 -->

AI-Driven Credit Risk Assessment in Fintech Lending: Implications for Financial Inclusion…

risk observation of AI-driven credit concentration and model herding should be included in the macroprudential 
surveillance  frameworks.  In  the  case  of  fintech  companies,  embracing  the  IACRF  or  a  similar  governance 
framework  must  be  considered  a  prerequisite  to  a  regulatory  license  in  highly-regulated  AI  jurisdictions,  and 
there  should  be  a  model  risk  officer  and  fairness  engineering  position  on  credit  risk  teams.  In  the  case  of 
multilateral development institutions, to avoid increasing digital divides and the emergence of unregulated  AI 
credit  markets  where  governments  lack  the  capacity  to  regulate,  specific  funding  in  the  digital  infrastructure, 
financial  literacy,  and  capacity  building  in  emerging  markets  is  important.  In  the  case  of  the  academic 
community, longitudinal empirical research and tracking of the accuracy and bias of AI credit models across the 
full economic cycles, and quantitative models of the systemic risk propagation in AI-mediated lending networks 
are the most urgent research priorities. 
6.4 Limitations and Future Research

There  are three limitations in the paper. The  use of published literature restricts causal inference and 
evaluation of unpublished industry practices; the literature that is reviewed is likely to suffer from publication 
bias that would bias towards positive results of model performance. IACRF is theoretically based, but it is yet to 
be  supported  by  empirical  research  (field)  and  case  studies  of  practitioners.  The  fast-changing  regulatory 
environment will imply that particular references might have to be updated when the implementation of the AI 
Act  in  the  EU  and  the  FSB  AI  guidance  is  complete.  The  IACRF  should  be  empirically  tested  in  different 
fintech settings in future research, and longitudinal studies of AI credit models' performance in economic cycles 
and network-based empirical models of the propagation of systemic risk in AI-mediated lending markets should 
be developed. 
6.5 Concluding Remarks

FinTech  lending  credit  risk  assessment  based  on  AI  is  a  revolution  that  can  be  governable,  but  its 
effects on society depend on the governance models that govern its implementation. The IACRF, which will be 
suggested in this paper, is a step towards establishing such frameworks - a collaborative project that requires the 
participation  of  computer  scientists,  economists, 
lawyers,  regulators,  development  practitioners,  and 
communities  impacted.  The  AI  governance  in  credit  markets  is  not  an  issue  of  a  technical  nature  and  has  a 
technical solution; it is an institutional issue that requires institutional innovation in the interface of technology, 
finance, and democratic accountability.

REFERENCES

[1]

[2]

[3]

[4]

[5]

[6]

[7]

[8]

[9]

[10]

of

2(3),

Article

Journal

Analysis,

Economic

development.

in  Financial

Journal  of  Risk  Management

Ozili, P. K. (2023). Determinants of FinTech and BigTech lending: The role of financial inclusion and 
financial 
4. 
https://doi.org/10.58567/jea02030004 
Berg, T., Fuster, A., & Puri, M. (2022). FinTech lending. Annual Review of Financial Economics, 14, 
187–207. https://doi.org/10.1146/annurev-financial-101521-112042 
Mhlanga, D. (2021). Financial inclusion in emerging economies: The application of machine learning 
and  artificial  intelligence  in  credit  risk  assessment.  International  Journal  of  Financial  Studies,  9(3), 
Article 39. https://doi.org/10.3390/ijfs9030039 
Fan,  L.  (2025).  Review  of  theoretical  advancements  in  AI/ML  classification  models  for  credit  risk 
assessment. 
Institutions,  18(2),  171–184. 
https://doi.org/10.69554/NKJL6812 
Giudici, P., & Raffinetti, E. (2023). SAFE artificial intelligence in finance.  Finance Research Letters, 
56, Article 104088. https://doi.org/10.1016/j.frl.2023.104088 
Das,  T.,  Jeelani,  S.,  Das,  S.,  Giri,  P.,  &  Chatterjee,  A.  (2024).  Human  bias  in  algorithmic  trading: 
Evaluating  behavioral  finance  impacts  on  automated  systems.  In  Proceedings  of  the  2024  2nd 
International  Conference  on  Computational  and  Characterization  Techniques  in  Engineering  and 
Sciences (IC3TES 2024). IEEE. https://doi.org/10.1109/IC3TES62412.2024.10877548 
Billio, M., Getmansky, M., Lo, A. W., & Pelizzon, L. (2012). Econometric measures of connectedness 
and systemic risk in the finance and insurance sectors.  Journal of Financial Economics, 104(3), 535–
559. https://doi.org/10.2139/ssrn.1963216 
Chaudhry, S. M., Ahmed, R., Huynh, T. L. D., & Benjasak, C. (2022). Tail risk and systemic risk of 
finance  and  technology  (FinTech)  firms.  Technological  Forecasting  and  Social  Change,  174,  Article 
121191. https://doi.org/10.1016/j.techfore.2021.121191 
Liu,  R.,  Yang,  X.,  Dong,  X.,  &  Sun,  B.  (2021).  Credit  risk  assessment  of  banks'  loan  enterprise 
customer 
145–168. 
https://doi.org/10.31577/cai_2021_1_145 
Bulut, C., & Arslan, E. (2025). A hybrid approach to credit risk assessment using bill payment habits 
data 
intelligence.  Applied  Sciences,  15(10),  Article  5723. 
artificial 
explainable 
https://doi.org/10.3390/app15105723

state-constraint.  Computing

Informatics,

40(1),

based

and

and

on

*Corresponding Author: SYED IJAZ AHMED1                  www.aijbm.com                            52 | Page

---

<!-- PAGE 10 -->

AI-Driven Credit Risk Assessment in Fintech Lending: Implications for Financial Inclusion…

[11]

[12]

[13]

[14]

[15]

[16]

[17]

[18]

learning.

Liao,  M.,  Jiao,  W.,  &  Zhang,  J.  (2025).  Research  on  trade  credit  risk  assessment  for  foreign  trade 
enterprises  based  on  explainable  machine 
Information,  16(10),  Article  831. 
https://doi.org/10.3390/info16100831 
Balyuk, T. (2023). FinTech lending and bank credit access for consumers. Management Science, 69(1), 
555–575. https://doi.org/10.1287/mnsc.2022.4319 
Balyuk, T., Berger, A. N., & Hackney, J. (2025). What is fueling FinTech lending? The role of banking 
market structure. The Review of Corporate Finance Studies. https://doi.org/10.1093/rcfs/cfae028 
Nguyen, L.,  & Qiu, B. (2025).  Fintech lending and firm bankruptcies.  Journal of Credit Risk, 21(1), 
33–51. https://doi.org/10.21314/JCR.2024.009 
Amnas,  M.  B.,  Selvam,  M.,  &  Parayitam,  S.  (2024).  FinTech  and  financial  inclusion:  Exploring  the 
mediating  role  of  digital  financial  literacy  and  the  moderating  influence  of  perceived  regulatory 
support. 
108. 
https://doi.org/10.3390/jrfm17030108 
Tay,  L.  Y.,  Tai,  H.  T.,  &  Tan,  G.  S.  (2022).  Digital  financial  inclusion:  A  gateway  to  sustainable 
development. Heliyon, 8(6), Article e09766. https://doi.org/10.1016/j.heliyon.2022.e09766 
Ozili,  P.  K.  (2018).  Impact  of  digital  finance  on  financial  inclusion  and  stability.  Borsa  Istanbul 
Review, 18(4), 329–340. https://doi.org/10.1016/j.bir.2017.12.003 
Tram, T. X. H., Lai, T. D., & Nguyen, T. T. H. (2023). Constructing a composite financial inclusion 
index  for  developing  economies.  Quarterly  Review  of  Economics  and  Finance,  87,  257–265. 
https://doi.org/10.1016/j.qref.2021.01.003

Financial  Management,

17(3),  Article

Journal

Risk

and

of

[19]  Wu,  X.  (2023).  The  rise  of  digital  finance  and  systemic  risk:  Implications,  challenges,  and  coping 
in  Economics,  Management  and  Political  Sciences,  45(1),  327–333.

[20]

[21]

[22]

[23]

[24]

[25]

[26]

56(38),

Applied

Economics,

strategies.  Advances 
https://doi.org/10.54254/2754-1169/45/20230306 
Gao, Q., Wu, H., & Yang, C. (2024). The impact of technology finance policies on the systemic risk of 
bank-firm 
4611–4631. 
networks. 
https://doi.org/10.1080/00036846.2023.2212971 
Hoffart, F. M., D'Orazio, P., Holz, F., & Kemfert, C. (2024). Exploring the interdependence of climate, 
finance,  energy,  and  geopolitics:  A  conceptual  framework  for  systemic  risks  amidst  multiple  crises. 
Applied Energy, 361, Article 122885. https://doi.org/10.1016/j.apenergy.2024.122885 
Bredt,  S.  (2019).  Artificial  intelligence  (AI)  in  the  financial  sector:  Potential  and  public  strategies. 
Frontiers in Artificial Intelligence, 2, Article 16. https://doi.org/10.3389/frai.2019.00016 
Explainable AI in algorithmic trading: Mitigating bias and improving regulatory compliance in finance. 
(2025).  International  Journal  of  Computer  Applications  Technology  and  Research,  14(4). 
https://doi.org/10.7753/ijcatr1404.1006 
Najib, N. W. M., Basarud-din, S. K., Ghazali, S. F., Abu Kasim, N., Abdullah, N. K., & Wan Mustafa, 
W.  A.  (2025).  A  bibliometric  analysis  of  research  trends  in  artificial  intelligence  (AI)  and  finance 
(2015–2025).  Journal  of  Information  System  and  Technology  Management,  10(40),  88–103. 
https://doi.org/10.35631/jistm.1040007 
Akerlof, G. A. (1970). The market for "lemons": Quality uncertainty and the market mechanism.  The 
Quarterly Journal of Economics, 84(3), 488–500. https://doi.org/10.2307/1879431 
Stiglitz,  J.  E.,  &  Weiss,  A.  (1981).  Credit  rationing  in  markets  with  imperfect  information.  The 
American Economic Review, 71(3), 393–410. https://www.jstor.org/stable/1802787

[27]  Merton,  R.  C.  (1995).  A  functional  perspective  of  financial  intermediation.  Financial  Management,

[28]

[29]

[30]

24(2), 23–41. https://www.jstor.org/stable/3665532 
Eisenhardt,  K. M. (1989). Building theories from case  study research. The Academy of Management 
Review, 14(4), 532–550. https://doi.org/10.5465/amr.1989.4308385 
Akinnagbe, O. B., Akintayo,  T. A., &  Adanna,  A. B. (2025). The impact of artificial intelligence on 
risk management in banking and finance. Mikailalsys Journal of Advanced Engineering International, 
2(2), 118–128. https://doi.org/10.58578/mjaei.v2i2.5195 
Du, G., & Elston, F. (2022). Financial risk assessment to improve the accuracy of financial prediction 
in the  internet  financial industry  using data  analytics  models.  Operations  Management Research, 16, 
967–979. https://doi.org/10.1007/s12063-022-00293-5

*Corresponding Author: SYED IJAZ AHMED1                  www.aijbm.com                            53 | Page

<!-- MARKITDOWN CONVERSION -->

<!-- Full MarkItDown conversion for formatting fidelity. -->

American International Journal of Business Management (AIJBM)
ISSN- 2379-106X, www.aijbm.com Volume 9, Issue 06 (June - 2026), PP 44-53

AI-Driven Credit Risk Assessment in Fintech Lending:
Implications for Financial Inclusion, Systemic Risk, and
Regulatory Governance

SYED IJAZ AHMED
Department Of Entrepreneur & Leadership, University Of Derby, United Kingdom
Corresponding Author: Syed Ijaz Ahmed

ABSTRACT: Artificial intelligence (AI) and machine learning (ML) in fintech lending have revolutionized credit
risk assessment,  enhanced financial  inclusion, but raised challenges to governance, such as algorithmic fairness,
systemic  stability,  and  regulatory  sufficiency.  The  given  paper  provides  a  systematic  literature  review  and
analytical  synthesis  of  AI-based  credit  risk  assessment  in  the  context  of  fintech  lending,  relying  on  30  peer-
reviewed articles that were published in 2012 and 2025. The paper compares the  performance of ML models to
traditional  scoring  principles,  examines  the  dynamic  of  financial  inclusion  and  digital  exclusion,  and  suggests  a
five-stage governance framework called the Integrated AI Credit Risk Framework (IACRF), which is an original
operationalization of the SAFE AI principles of statistical  accuracy, algorithmic  fairness, financial  stability, and
ethical  governance.  Results  show  that  ensemble  and  hybrid  explainable  AI  models  have  better  classification
compared to those without governance, and their use without good governance increases inequality, systemic risk,
and  exceeds  regulatory  capacity.  The  paper  ends  by  giving  specific  policy  suggestions  to  regulators,  fintech
companies,  and  multilateral  development  agencies  to  find  a  balance  between  credit  innovation  and  financial
stability as well as borrower equity.

KEYWORDS - Artificial Intelligence in Finance; Credit Risk Assessment; Fintech Lending; Machine Learning
Credit Scoring; Financial Inclusion; Algorithmic Bias; Systemic Risk; Explainable AI (XAI)

I.   INTRODUCTION

In  its  contemporary  history,  the  financial  services  sector  is  witnessing  one  of  the  most  significant
transformations  due  to  the  interplay  of  big  data  analytics,  artificial  intelligence  (AI),  and  the  digital  platform
economics.  In  this  transformation,  credit  risk  assessment  has  become  not  just  the  main  place  of  AI
implementation and where the technology has most of its most promising and dangerous implications are felt,
but  also  the  location  where  the  technology  has  had  the  biggest  impacts.  Over  the  decades,  the  credit  risk
assessment  market  has  been  dominated  by  more  classical  statistical  models  -  mainly  logistic  regression  and
FICO scoring system, basing their analysis on structured credit bureau information, including payment history,
credit  usage,  and  debt-to-income  ratios.  Although  these  instruments  could  offer  practical  estimates  of  default
probability, they have avoided much of the population with no record of formal credit using bureau coverage at
a  rate  that  can  be  below  20  percent  of  the  adult  population,  which  is  especially  true  in  emerging  economies
where bureau coverage rates can drop to below 20 percent of the adult population [1].

It is against this backdrop that fintech lenders have used AI and ML architectures to process alternative
data sources both in scale and speed more than ever before. Mobile phone usage and utility payment history, e-
commerce  history,  and  behavioral  indicators  are  some  of  the  proxies  of  creditworthiness  that  have  been
pioneered by platforms like  Lending Club,  Ant Financial, and PayPal credit and deliver  quantifiable  financial
inclusion benefits [2, 3]. Simultaneously, as opaque, data-dense AI models start proliferating, they have brought
about governance issues, which industry standards and regulatory frameworks have not so far addressed.

There are three key tensions of the modern problem of AI-based credit risk assessment. The former is
the accuracy explainability trade-off: the new generation of ensemble and deep learning models is more accurate
than the traditional scorecards, but are black-box models that are difficult to interpret because of the demands of
regulators  and  borrowers  [4,  5].  The  second  one  is  the  inclusion-bias  paradox:  alternative  data  pipelines  that
credit  populations  that  it  previously  did  not  credit  are  also  at  risk  of  incurring  structural  discrimination  and
amplifying the effect on the classes being protected, which can lead to disparate effects [6]. The third one is the
stability-innovation dilemma: the systemic risk vectors (model herding, procyclicality, and platform contagion)
of  the  interconnectedness  of  fintech  lending  platforms  cannot  be  identified  or  addressed  by  conventional
prudential frameworks [7, 8].

The  paper  has  managed  to  focus  on  these  tensions  based  on  a  systematic  review  and  analysis  of  the
empirical  and  theoretical  literature  on  AI-based  fintech  credit  risk.  It  suggests  an  innovative  five-step
governance  framework,  the  Integrated  AI  Credit  Risk  Framework  (IACRF),  operationalizing  the  SAFE  AI

*Corresponding Author: SYED IJAZ AHMED1                  www.aijbm.com                            44 | Page

AI-Driven Credit Risk Assessment in Fintech Lending: Implications for Financial Inclusion…

principles  throughout  the  entire  operational  lifecycle  of  a  fintech  credit  system,  and  coming  up  with  policy
proposals  to  regulators,  practitioners,  and  development  finance  institutions.  The  paper  has  the  following
structure: in Section II, the literature review will be done on eight thematic domains; Section III will construct
the theoretical framework and IACRF; Section IV will outline the methodology; Section V will summarize the
results and discussion, and finally, Section VI will be a conclusion.

II.   LITERATURE REVIEW

2.1 Evolution of Credit Risk Assessment: From Traditional Models to AI

Formal  credit  risk  assessment  dates  back  to  the  logistic  regression-based  scorecards  created  in  the
1950s  and  1960s,  with  Altman's  (1968)  Z-score  for  corporate  bankruptcy  prediction,  and  extends  through  the
institutionalization of the FICO score in consumer lending in 1989. The traditional methods presuppose linear
relationships  between  predictors,  are  vulnerable  to  multicollinearity,  and  rely  on  pre-determined  choice  of
variables  -  features  that  are  not  well  aligned  to  the  high-dimensional  and  nonlinear  data  conditions  of  the
contemporary digital lending [4, 9]. The shortcomings of bureau-based scoring opened the door to ML methods
that can handle complex feature interactions, adapt to new data patterns, and handle unstructured inputs. Since
the mid-2010s, decision trees, random forests, gradient boosting machines, especially XGBoost and LightGBM,
and neural network architectures have started to enter fintech lending businesses, with improvements of 5 to 15
percentage  points over logistic regression  models in  terms  of  AUC-ROC [10, 4]. The latest  frontier is adding
explainability  mechanisms,  such  as  SHAP  values,  LIME,  and  integrated  gradients,  to  high-performing  ML
architectures,  which  partially  closes  the  divide  between  the  performance  of  a  model  and  regulatory
interpretability [5, 11].
2.2 Fintech Lending: Market Structure, Growth Dynamics, and Bank Interactions

The world fintech lending sector has evolved to become a multi-trillion-dollar business, including peer-
to-peer (P2P) lending, marketplace lending, balance sheet schemes, embedded finance, and buy-now-pay-later
(BNPL).  [2]  chronicle  the  way  varying  fintech  business  models  take  advantage  of  AI  to  lower  underwriting
expenses,  speed  up  the  process  of  credit  decisioning  (from  days  to  seconds),  and  serve  underserved  borrower
groups not served by existing banks. [12] discovers that fintech lending does not replace access to bank credit in
U.S. consumer  markets,  whereas [13] reveal that  the banking  market concentration determines the chances of
fintech entering the market. According to [1], financial inclusion and development are some of the determinants
of  fintech  and  BigTech  lending  volumes  that  are  recorded.  Notably,  [14]  discovered  that  the  fintech  credit-
exposed firms show higher bankruptcy rates in troughs, which casts doubt on the idea that AI-enhanced credit
expansion can lead to a faster misallocation of risk in some segments of the credit portfolio and highlights the
necessity to incorporate the through-the-cycle performance of credit models, as opposed to in-sample accuracy.
2.3 Machine Learning Models for Credit Risk: Comparative Performance

This  systematic  review  by  [4]  confirms  that  the  ensemble  techniques  have  always  achieved  higher
performance than the logistic regression benchmarks on all the datasets, evaluation  metrics, and  markets. The
use  of  gradient  boosting  algorithms,  especially  XGBoost  and  LightGBM,  has  become  the  tool  of  choice  in
fintech  credit  scoring,  providing  better  missing  data  behavior,  resistance  to  overfitting,  and  good  tabular  data
behavior.  [10]  illustrate  that  a  hybrid  XAI  model  that  takes  the  form  of  gradient  boosting  with  SHAP-based
explainability can attain an AUC-ROC of 0.89 as compared to a logistic regression baseline of 0.76, and meets
the adverse action notice criteria. Similar conclusions are made by [11]  with regard to trade credit risk, and [9]
demonstrate  that LSTM networks give an AUC-ROC over 0.90 with enterprise credit data used, but at a high
interpretability cost. The results show that there is a performance hierarchy: deep learning models have marginal
benefits in data-rich settings, and ensemble approaches are the most risk-adjusted option in real-world fintech
applications. Table 1 summarises comparative performance evidence in the literature reviewed.
Table 1: Comparative performance of ai/ml models in credit risk assessment

Model Type

AUC-ROC
Range

Gini Coeff.

Interpretability  Fairness

Logistic Regression

0.68 – 0.77

0.36 – 0.54

High

Decision Tree

0.70 – 0.78

0.40 – 0.56

High

Random Forest

0.79 – 0.86

0.58 – 0.72

Low-Medium

Partial

XGBoost / LightGBM

0.83 – 0.91

0.66 – 0.82

Low

Partial

Compliance

Partial

Partial

Regulatory
Suitability

High

High

Medium

Medium

LSTM / Deep Learning

0.85 – 0.93

0.70 – 0.86

Very Low

Unclear

Low

*Corresponding Author: SYED IJAZ AHMED1                  www.aijbm.com                            45 | Page

AI-Driven Credit Risk Assessment in Fintech Lending: Implications for Financial Inclusion…

Hybrid
(SHAP/LIME)

XAI

0.84 – 0.92

0.68 – 0.84  Medium-High

Yes
(Conditional)

Medium-
High

2.4 Financial Inclusion and AI-Driven Credit Expansion

[3]  shows  that  when  used  on  alternative  data  (mobile  usage,  records  of  digital  payments,  behavioral
indicators),  ML  models  produce  creditworthiness  estimates  of  thin-file  borrowers  just  as  accurate  as  the
traditional scoring on bureau-rich groups, and it is especially interesting in Sub-Saharan Africa, South Asia, and
Southeast  Asia.  [14]  list  digital  financial  literacy  and  perceived  regulatory  support  as  the  most  important
mediating variables, and it is important to highlight that the groups facing the highest likelihood of benefiting
due to AI-driven credit expansion are the same most vulnerable to using AI-based credit products. In a study by
[16],  the  benefits  of  fintech  inclusion  are  being  recorded  to  be  among  digitally  connected  groups,  posing  a
second-order challenge of exclusion. [17] also adds that the pace of digital credit and its magnitude pose the risk
of  overleverage  in  newly  added  borrowers  within  a  short  time.  The  composite  financial  inclusion  index  of
developing  economies  presented  in  the  study  by  [18]  shows  that  access  indicators  tend  to  conceal  quality
differences. Nominally included populations can have AI-generated credit products that have prohibitive interest
rates and punitive default fees that harm and do not improve financial well-being.
2.5 Algorithmic Bias, Fairness, and Ethical Dimensions

Algorithms'  bias  in  credit  scoring.  The  systematic  bias  of  AI  models  to  hurt  the  interests  of  the
protected  groups  is  known  as  algorithmic  bias:  racial  minorities,  women,  and  older  adults.  [6]  show  that
behavioral  biases  are  coded  in  an  ordered  manner  in  AI  systems  that  are  trained  on  biased  data  in  the  past.
IJCATR  (2025)  analysis  reveals  that  the  discriminatory  patterns  are  seen  with  the  use  of  XAI  techniques,
whereas visibility is not necessarily followed by remediation. The sources of bias can be categorized into three
pipeline  stages:  pre-processing  (historical  training  data  based  on  past  discrimination),  in-processing  (model
architecture decisions implicitly related to the protected attributes), and post-processing (use on populations that
are  not  in  the  same  distribution  as  the  training).  [5]  posit  that  technical  debiasing,  such  as  re-sampling,
adversarial  debiasing,  and  fairness  constraints,  cannot  be  effectively  used  without  institutional  accountability
mechanisms, such as having  mandatory audits on algorithms, publishing fairness  measurements, and allowing
recourse rights. The lack of these in the majority of the regulatory frameworks is the key gap in governance in
the area of algorithmic fairness.
2.6 Systemic Risk, Financial Stability, and Fintech Interconnectedness

[7]  prove  the  existence  of  tail-risk  spillovers  between  financial  institutions,  and  that  correlated  asset
exposures  increase  the  tail-risk  spillovers  between  financial  institutions,  a  phenomenon  that  AI  lending
promotes in the lending system via model convergence. In their record, [8] report a high level of systemic risk,
which is due to the high growth rate of credit, the low capital adequacy, and reliance on wholesale funds. [19]
lists  three  channels  of  systemic  risk:  the  concentration  of  powerful  platforms,  interconnectedness  via  API
integrations with banking counterparties, and the lack of accessibility to the algorithms behind credit decisions
made  by  algorithms  by  supervisors.  [20]  determine  that  systemic  risk  propagation  in  bank-firm  networks  is
greatly moderated by the regulatory policy environment, whereas [21]  build on this to compound systemic risk
due  to  the  interdependence  of  finance,  technology,  energy,  and  geopolitical  systems  -  environments  that  AI
credit systems can enhance procyclical allocation.
2.7 Regulatory Frameworks and AI Governance in Lending

[22] presents the initial examination of the problem of AI governance in financial services, which he
describes as regulatory arbitrage, systemic openness, and discriminatory results as the three main risks that the
government needs to approach in its strategy. [23] defines credit scoring AI as a high-risk category, which must
have conformity tests, documentation of training data, human supervision, and explainability compliance. The
Basel Committee has provided guidance on model risk management that requires validation of AI credit models,
monitoring, and documentation of AI credit models. The U.S. CFPB has applied the requirements of the Equal
Credit  Opportunity  Act  to  AI-generated  decisions  relating  to  adverse  actions,  but  has  not  applied  the
requirements  to  non-bank  fintech  platforms  whose  enforcement  ability  is  limited.  A  structural  issue  that  is
identified in the bibliometric analysis of [24] is regulatory arbitrage, i.e., the migration of model deployment to a
jurisdiction with lighter regulation for fintech firms that needs to be coordinated internationally by the Financial
Stability Board and Basel Committee.
2.8 Identified Gaps in the Existing Literature

The  contributions to this paper are  inspired by four gaps. First, the streams of research  on the  model
performance,  inclusion,  bias,  and  systemic  risk  are  relatively  isolated,  and  there  are  very  few  studies  that
combine model-level analysis and macro-prudential assessment. Second, the literature on AI credit dynamics is
strongly  biased  towards  North  American  and  European  situations,  and  little  is  known  about  the  AI  credit
dynamics  in  Sub-Saharan  African  and  Southeast  Asian  fintech  markets.  Third,  there  is  no  currently  existing
*Corresponding Author: SYED IJAZ AHMED1                  www.aijbm.com                            46 | Page

AI-Driven Credit Risk Assessment in Fintech Lending: Implications for Financial Inclusion…

system of governance that considers model-level explainability, fairness of borrowers, and systemic stability of
the market at the same time in a single architecture that is tuned to fintech. Fourth, full-cycle empirical studies
of the performance of AI credit models do not exist to allow sufficient evaluation of the procyclicality risks.

III.   THEORETICAL FRAMEWORK

3.1 Theoretical Anchors

The article is based on three theoretical traditions that are complementary. The information asymmetry
theory  [25,  26]  provides  that  credit  market  inefficiencies  are  a  result  of  the  inability  of  lenders  to  completely
monitor the type of borrower. Thought to be advanced information processors, AI credit systems are theorized
to decrease the lender-side asymmetries with increased and more diverse datasets. But they also introduce new
borrower-side  asymmetries,  hidden  algorithmic  judgments,  which  could  not  be  comprehended,  challenged,  or
acted  upon  by  those  impacted,  creating  a  lack  of  fairness  and  accountability,  which  the  SAFE  AI  literature
recognizes [5]. The literature on financial innovation [27] sees AI-driven fintech as an institutional change that
can  be  caused  by  the  interplay  of  the  availability  of  data,  the  power  of  computers,  and  the  opportunity  of
regulation  all  of  which  are  essentially  institutional,  but  not  technical,  in  nature.  The  macro-prudential  theory
behind the development of the correlated AI credit models is known as systemic risk theory [7], which is based
on the tail-risk spillover effects of generating systemic vulnerability due to the existence of monoculture risks
that are not diversifiable.
3.2 The SAFE AI Framework

The IACRF normative architecture is based on the normative architecture of [5] SAFE AI framework.
The four SAFE pillars, Statistical accuracy, Algorithmic fairness, Financial stability and Ethical governance are
operationalized  in  the  context  of  fintech  lending  as:  (a)  minimum,  validated  out-of-sample  performance
thresholds;  (b)  published  parity  conditions  across  the  three  or  more  protected  groups  with  audited  disparate
impact; (c) stress-tested resistance to procyclical behavior, model herding and systemic The SAFE framework is
claimed to be more suitable in the high-stakes credit situations than single-objective accuracy optimization since
it is a framework that takes into account all the aspects of the governance risk simultaneously.
3.3 The Integrated AI Credit Risk Framework (IACRF)

The main theoretical contribution of the paper is the IACRF: a multi-level governance framework that
is  a  map  of  four  pillars  of  the  SAFE  AI  onto  the  operational  lifecycle  of  a  fintech  credit  system  in  five
consecutive,  iterative  steps.  The  framework  is  developed  in  a  way  that  it  is  applicable  to  both  mature  and
emerging  markets,  where  the  regulation  is  at  either  the  firm  or  regulatory  interface  level.  The  IACRF
architecture is shown in Fig.1

Stage 1
Data goverance
Accuracy pillar

Stage 5
Impact evaluation
All four pillars

Stage 2
Model design
Accuracy + fairness

Stage 4
Regulatory interface
Ethics + stability

Stage 3
Deployment arch
Stability + fairness

Figure 1: The integrated ai credit risk framework (iacrf) — conceptual architecture

Stage  1:  Data  Governance:  The  area  deals  with  the  data  sourcing,  quality  management,  consent
architecture, training data bias audit, and representativeness standards, and operationalizes the SAFE accuracy
pillar.  Stage  2:  Model  Design  regulates  the  choice  of  architecture,  integration  of  fairness  constraints,  the

*Corresponding Author: SYED IJAZ AHMED1                  www.aijbm.com                            47 | Page

AI-Driven Credit Risk Assessment in Fintech Lending: Implications for Financial Inclusion…

specification of explainability mechanisms, a documentation of proxy variables, as well as pre-deployment bias
audits, operationalising SAFE accuracy and fairness. Stage 3: Deployment Architecture takes care of real-time
scoring  infrastructure,  performance  degradation  checks,  distributional  shift  checks,  human  override  checks,
regulatory  audit  trail  maintenance,  and  operationalizes  SAFE  stability  and  fairness.  Stage  4:    Regulatory
Interface regulates model validation documentation, adverse action notice procedures, supervisory coordination,
and  periodic  model  risk  assessment,  operationalises  SAFE  ethics  and  stability.  Stage  5:  Impact  Evaluation
includes financial inclusion impact analysis by demographic groups, systemic risk monitoring, the presence of
market-level  credit  correlation  and  concentration,  and  public  impact  reporting,  and  puts  all  four  SAFE  pillars
into action at once.
3.4 Theoretical Propositions

The  IACRF  and  literature  synthesis  give  rise  to  four  propositions:  (P1)  AI  credit  models  are  more
predictive  than  traditional  methods  but  have  interpretability  limitations  leading  to  a  conflict  of  regulation  in
adverse-action jurisdictions. (P2) Fintech lending based on AI financial inclusion benefits in data-rich settings,
but does not reach the digitally low populations, enabling a second-order dynamic of AI-based exclusion. (P3)
The  systemic  risk  is  exacerbated  by  market-wide  adoption  of  correlated  AI  credit  models  that  create  tail-risk
spillovers,  and  the  model  herding  and  coordinated  credit  tightening  of  models,  which  have  larger  tail-risk
spillovers  than  traditional  credit  monocultures.  (P4)  Adoption  of  IACRF-specified  governance  mechanisms,
such as explainability integration, bias auditing, and systemic risk monitoring, is positively linked to regulatory
compliance and financial stability in AI-driven lending.

4.1 Research Design and Protocol

IV.   METHODOLOGY

The present paper has a position of interpretivist-constructivist in a qualitative research design, which
is  theory-building  in  nature.  It  combines  both  published  empirical  and  theoretical  studies  to  formulate  the
IACRF and come up with policy implications, as is customary in high-impact journals in finance to contribute to
a theoretical framework [2, 24]. The review of the literature is based on a PRISMA-inspired guideline. Searches
were  done  and  regulatory  repositories  of  the  European  Banking  Authority,  the  U.S  CFPB,  and  the  Financial
Stability Board. Keywords  were: 'AI credit risk,'  machine  learning  fintech lending, algorithmic credit scoring,
and  fintech  systemic  risk.  Secondary  terms  were:  explainable  AI  finance,  algorithmic  bias  credit,  financial
inclusion fintech, and credit model governance. This was during the period 2012-2025, but with a focus on 2021
and  beyond.  Preliminary  search  results  of  about  280  documents  were  narrowed  down  by  filters  such  as
duplicates,  title and abstract filtering, and quality  filtering that filtered out non-peer-reviewed sources to get a
final corpus of 30 peer-reviewed articles and regulatory reports. Fig. 2 shows  how the screening is done. The
analysis and framework development of comparative models will be conducted at this phase.

Figure 2: Prisma informed literature search and screening flowchart

4.2 Comparative Model Analysis and Framework Development

To analyze the performance of the comparative model in Section V, performance information reported
in  studies  reviewed  is  gathered  and  tabulated  into  a  comparative  table.  Measurements  AUC-ROC,  Gini

*Corresponding Author: SYED IJAZ AHMED1                  www.aijbm.com                            48 | Page

AI-Driven Credit Risk Assessment in Fintech Lending: Implications for Financial Inclusion…

coefficient,  and  KS  statistic  are  tabulated  by  model  type  with  performance  ranges  instead  of  point  estimates
being  used  to  address  heterogeneity  in  cross-study  characteristics  of  the  datasets  and  their  methodology.  The
IACRF is formulated using the iterative framework construction approach of [28]. Theory and evidence are used
to construct the theory using theory as the building blocks, and then iterate the relationship among the building
blocks  to  develop  sufficient  specifications  in  the  framework  to  create  testable  propositions.  The  framework
constructs are checked against published frameworks of fintech governance by a consistency check to make sure
the structures are complete.

V.   RESULTS AND DISCUSSION

5.1 AI Model Performance: Comparative Analysis

The  evidence  of  the  comparison  proves  Proposition  1.  Gradient  boosting  models  are  able  to  attain
values of 0.83-0.91 in AUC-ROC, which are 7-19 percentage points higher than the logistic regression baselines
[4, 10]. Such returns have an economic impact: a 5-percentage-point improvement in the AUC-ROC is directly
translated  into  lower  levels  of  false  positives  (creditworthy  borrowers  denied  credit)  and  false  negatives
(defaulters granted credit) rates,  which improve  the quality of the portfolio and access to credit by borrowers.
The best balance between performance and explainability is the hybrid XAI model [10]: SHAP attribution in a
gradient  boosting  framework  can  be  applied  to  achieve  almost  the  same  accuracy  of  the  ensemble  as  well  as
meet the adverse action criteria. Nonetheless, SHAP explanations are local models, which might not capture the
behavior of global models, and their implementation is too complex to be adopted by smaller fintech operators.
The  highest  reported  performance  (AUC-ROC  >  0.90)  comes  with  LSTM  architecture,  which  is  virtually
incompatible  with  EU  AI  Act  high-risk  classification  requirements  on  its  black-box  nature  and  therefore,  is
prone  to  be  adopted  by  the  less-regulated  market-driven  force  of  emerging  markets,  a  regulatory  arbitrage
dynamic that needs supervisor consideration [9].
5.2 Financial Inclusion: Opportunities and Structural Contradictions

Evidence  reveals  that  there  is  qualitative  support  for  Proposition  2.  In  new  market  environments,  AI
credit models on alternative data increase the rate of approval of thin-file and unbanked borrowers by 20 to 40
percentage  points [3],  which  is an appreciable gain in terms of access to credit  to small business owners, gig
economy workers, and rural households, who relied on informal credit before. There are limits to inclusionary
potential, however, due to structural contradictions. The invisibility of some groups of people that do not have
access to smartphones, connectivity, or a history of digital transactions leads to a coverage gap that AI models
fail to predict unless non-digital sources of data are included [16]. Although allowing the approval of excluded
borrowers  potentially  places  them  in  high-risk  pricing  tiers  that  would  earn  high  interest  rates,  potentially  far
exceeding market rates, AI risk stratification granularity can also be dynamic in that nominal inclusion comes at
a cost that can lead to financial ill health [17, 15]. Table 2 provides an overview of financial inclusion indicators
in an AI-driven lending setting, by region.
Table 2: Financial inclusion metrics across ai-driven lending contexts by region

Region

Platform Type

Key
Data

Alternative

Approval
Rate Uplift

Interest  Rate
Premium

Digital
Exclusion
Risk

Sub-Saharan
Africa

Mobile  Money  /
P2P

Mobile  usage,  M-
PESA, airtime

30–45%

8–18%  above
base

Very
High

Southeast Asia  Digital  Bank

/

BNPL

E-commerce,
share, social

ride-

20–35%

5–14%  above
base

High

Latin America  Marketplace

Lending

Bill  payment,  utility,
telco

15–28%

4–12%  above
base

Medium-
High

European
Union

Embedded
Finance / BNPL

Open  banking,  PSD2
data

8–15%

North America  Fintech

Marketplace

Rent,
income

utility,

gig

10–20%

1–5%
base

2–8%
base

above

Low-
Medium

above

Low

*Corresponding Author: SYED IJAZ AHMED1                  www.aijbm.com                            49 | Page

AI-Driven Credit Risk Assessment in Fintech Lending: Implications for Financial Inclusion…

5.3 Algorithmic Bias: Technical Evidence and Institutional Imperatives

The  argument  that  institutional  accountability  structures,  in  conjunction  with  technical  debiasing,  are
necessary  is  strongly  supported  by  the  evidence  [5].  [6]  show  that  AI  systems  can  produce  behavioral  biases
methodically encoded within their designs based on the biases in the historical data used to train them - a credit
model that learns the discriminatory approval and default patterns of decades learns to recapitulate those biases
as  predictions,  despite  not  being  trained  to  do  so  on  purpose.  The  XAI  analysis  of  the  IJCATR  (2025)
establishes  that  SHAP  and  LIME  are  more  effective  than  naive  debiasing  in  identifying  the  existence  of
discriminatory patterns. Still,  it is  not able to remediate  them, and that performance-fairness trade-offs render
naive debiasing commercially unfeasible among thin-margin fintech operators. The key institutional loophole is
that in most major regulatory frameworks, such as the [23], mandatory independent bias auditing, disclosure of
public fairness metrics, and enforceability of a right to recourse by borrowers are not mandatory, including the
[23], which provides conformity assessment documentation, but does not mandate periodic third-party audits or
disclosure of fairness metrics to the public. The priority regulatory reform to bridge this gap would be to set up
mandatory bias auditing requirements and to enforce this requirement by the supervisory authority.
5.4 Systemic Risk Propagation Pathways

Systemic vulnerability is enhanced by three different propagation pathways, which amplify the effects
of AI-based fintech lending and support Proposition 3. Model herding is caused by converging industry-wide to
similar gradient boosting architectures, and overlapping alternative data pipelines: a macroeconomic shock that
causes the predictive value of behavioral data to fall at once causes credit assessments of all institutions using
that  information  to  become  coordinated  in  tightening  their  credit  policies,  a  phenomenon  that  is  directly
analogous to the correlated asset exposure problem reported by [7]. The AI models trained on expansionary data
can  be  procyclical  because  they  can  implicitly  link  good  times  with  creditworthiness  and  can  produce
permissive calibrations when there is a boom and sudden contractions when there is a downturn, and amplify the
business  cycle  via  the  credit  channel  [21].  Contagion  between  platforms  occurs  as  a  result  of  institutional
interconnectedness, which comes in the form of API integrations, similar banking infrastructure, and secondary
market  securitization:  a  model  failure  in  governance  or  a  cyberattack  on  a  large  platform  at  machine  speed
spreads to investors, counterparty banks, and  secondary  market participants even before  the conventional risk
systems can react [8].

Figure 3: Systemic risk propagation pathways in ai-driven fintech lending

5.5 Regulatory Governance: Comparative Jurisdictional Analysis

The comparative study proves the existence of a disjointed and jurisdiction-based unequal governance
environment.  Table 3 looks at the  AI credit governance frameworks in  five regulatory jurisdictions in aspects
that are directly pertinent to the SAFE AI pillars.

*Corresponding Author: SYED IJAZ AHMED1                  www.aijbm.com                            50 | Page

AI-Driven Credit Risk Assessment in Fintech Lending: Implications for Financial Inclusion…

Table 3: Comparative ai credit governance frameworks by jurisdiction

Jurisdiction  Primary

Instrument

Explainability
Req.

Bias  Audit
Mandate

Model
Validation
Std.

Enforcement  Gov.
Gap
Score

United
States

ECOA  /  CFPB
Guidance

Partial
(Adverse
Action)

No
(Voluntary)

SR
11-7
(Banks only)

CFPB  Civil
Action

3 / 5

European
Union

EU  AI  Act
(2024)

(High-

Yes
Risk Class)

United
Kingdom

FCA  Consumer
Duty

China

PBOC
Algorithm Reg.

Yes
(Outcome-
Based)
Partial
(Disclosure)

Yes
(Conformity
Assess.)
Yes
Treatment)

(Fair

Partial

CE  Marking
+ EBA

/  Nat.

EBA
Supervisors

2 / 5

FCA  Model
Risk
Guidance
PBOC  Tech.
Standards

FCA
Supervisory

2 / 5

PBOC
Administrative

3 / 5

Emerging
Markets

Varies
Minimal

/

Rarely
Required

Rarely
Required

Absent
Informal

or

Limited
Capacity

5 / 5

There  are  two  overall  findings.  To  start  with,  the  [23]  is  the  most  up-to-date  best-practice  model
(closest to Stage 4 (Regulatory Interface) of the IACRF), but it is still not sufficient in the systemic risk aspect
(there is no systemic risk tool in the EU to monitor AI-based credit concentration or procyclicality at the market
level on the  same level as macroprudential banking supervisor instruments). Second, there is a higher level of
governance gaps in the emerging markets since regulatory capacity in the emerging markets is the least, and the
populations that are the most vulnerable to the inclusion-bias paradox are concentrated in the emerging markets.
This  imbalance  requires  global  coordination  with  the  FSB  and  Basel  Committee  to  avoid  a  global  AI  credit
governance system that will be based on two levels, where the most vulnerable groups will be least safeguarded.

6.1 Summary of Findings

VI.   CONCLUSION

The  paper  summarizes  30  peer-reviewed  articles  on  the  topic  of  AI-based  credit  risk  assessment  in
fintech  lending  that  came  up  with  findings  in  four  dimensions.  Ensemble  and  hybrid  XAI  models  offer
economic  material  benefits  to  traditional  scorecards  on  model  performance,  yet  the  performance  hierarchy  is
coupled  with  interpretability  shortcomings  that  pose  real  regulatory  problems  that  arise  in  adverse-action
jurisdictions. On financial inclusion, AI credit systems expand access rates to thin-file and unbanked borrowers
by  significant  percentages  in  new  markets,  but  inherent  contradictions  of  digital  inclusion,  AI-driven  pricing
bias,  and  excessive  leverage  constrain  and  even  hinder  the  potential  of  inclusion.  Three  new  propagation
pathways  at  the  intersection  of  credit  and  financial  market  interconnections  driven  by  AI:  model  herding,
procyclicality,  and  platform  contagion,  give  rise  to  systemic  vulnerability  and  are  left  unaddressed  by  current
prudential frameworks in detecting and mitigating them. Regarding regulatory governance, the world market is
divided  and  unbalanced,  with  jurisdictional  and  the  [23]  skewing  to  best  practice  without  addressing  the
systemic risk aspect, and new markets experiencing the greatest governance gap.
6.2 Theoretical Contributions

Three main contributions are promoted. To start with, the IACRF offers a novel multi-level governance
architecture  to  combine  the  SAFE  AI  imperatives  and  the  fintech  credit  lifecycle  in  five  stages  of  operation,
filling the uncharted gap in frameworks that jointly focus on model-level performance and fairness, firm-level
compliance,  and  market-level  systemic  risk.  Second,  a  theoretically-based  taxonomy  of  systemic  risk
propagation  pathways  that  are  particular  to  AI-powered  fintech  lending  is  introduced  that  builds  on  the
connectedness  framework  by  [7]  in  the  algorithmic  credit  environment.  Third,  the  theory  of  information
asymmetry,  the  theory  of  financial  innovation,  and  the  SAFE  AI  framework  are  brought  into  a  consistent
analytical  framework  that  proves  these  traditions  to  be  mutually  reinforcing  and  how  integrating  them  brings
insights into governance that none can bring forth alone.
6.3 Policy Recommendations

There are four sets of recommendations that are promoted. To regulators and central banks: AI credit
models  with  more  than  a  specified  level  of  deployment  should  be  required  to  have  explainability  and  an
independent bias audit, coordinated by the Basel Committee and FSB, to avoid regulatory arbitrage; systemic

*Corresponding Author: SYED IJAZ AHMED1                  www.aijbm.com                            51 | Page

AI-Driven Credit Risk Assessment in Fintech Lending: Implications for Financial Inclusion…

risk observation of AI-driven credit concentration and model herding should be included in the macroprudential
surveillance  frameworks.  In  the  case  of  fintech  companies,  embracing  the  IACRF  or  a  similar  governance
framework  must  be  considered  a  prerequisite  to  a  regulatory  license  in  highly-regulated  AI  jurisdictions,  and
there  should  be  a  model  risk  officer  and  fairness  engineering  position  on  credit  risk  teams.  In  the  case  of
multilateral development institutions, to avoid increasing digital divides and the emergence of unregulated  AI
credit  markets  where  governments  lack  the  capacity  to  regulate,  specific  funding  in  the  digital  infrastructure,
financial  literacy,  and  capacity  building  in  emerging  markets  is  important.  In  the  case  of  the  academic
community, longitudinal empirical research and tracking of the accuracy and bias of AI credit models across the
full economic cycles, and quantitative models of the systemic risk propagation in AI-mediated lending networks
are the most urgent research priorities.
6.4 Limitations and Future Research

There  are three limitations in the paper. The  use of published literature restricts causal inference and
evaluation of unpublished industry practices; the literature that is reviewed is likely to suffer from publication
bias that would bias towards positive results of model performance. IACRF is theoretically based, but it is yet to
be  supported  by  empirical  research  (field)  and  case  studies  of  practitioners.  The  fast-changing  regulatory
environment will imply that particular references might have to be updated when the implementation of the AI
Act  in  the  EU  and  the  FSB  AI  guidance  is  complete.  The  IACRF  should  be  empirically  tested  in  different
fintech settings in future research, and longitudinal studies of AI credit models' performance in economic cycles
and network-based empirical models of the propagation of systemic risk in AI-mediated lending markets should
be developed.
6.5 Concluding Remarks

FinTech  lending  credit  risk  assessment  based  on  AI  is  a  revolution  that  can  be  governable,  but  its
effects on society depend on the governance models that govern its implementation. The IACRF, which will be
suggested in this paper, is a step towards establishing such frameworks - a collaborative project that requires the
participation  of  computer  scientists,  economists,
lawyers,  regulators,  development  practitioners,  and
communities  impacted.  The  AI  governance  in  credit  markets  is  not  an  issue  of  a  technical  nature  and  has  a
technical solution; it is an institutional issue that requires institutional innovation in the interface of technology,
finance, and democratic accountability.

REFERENCES

[1]

[2]

[3]

[4]

[5]

[6]

[7]

[8]

[9]

[10]

of

2(3),

Article

Journal

Analysis,

Economic

development.

in  Financial

Journal  of  Risk  Management

Ozili, P. K. (2023). Determinants of FinTech and BigTech lending: The role of financial inclusion and
financial
4.
https://doi.org/10.58567/jea02030004
Berg, T., Fuster, A., & Puri, M. (2022). FinTech lending. Annual Review of Financial Economics, 14,
187–207. https://doi.org/10.1146/annurev-financial-101521-112042
Mhlanga, D. (2021). Financial inclusion in emerging economies: The application of machine learning
and  artificial  intelligence  in  credit  risk  assessment.  International  Journal  of  Financial  Studies,  9(3),
Article 39. https://doi.org/10.3390/ijfs9030039
Fan,  L.  (2025).  Review  of  theoretical  advancements  in  AI/ML  classification  models  for  credit  risk
assessment.
Institutions,  18(2),  171–184.
https://doi.org/10.69554/NKJL6812
Giudici, P., & Raffinetti, E. (2023). SAFE artificial intelligence in finance.  Finance Research Letters,
56, Article 104088. https://doi.org/10.1016/j.frl.2023.104088
Das,  T.,  Jeelani,  S.,  Das,  S.,  Giri,  P.,  &  Chatterjee,  A.  (2024).  Human  bias  in  algorithmic  trading:
Evaluating  behavioral  finance  impacts  on  automated  systems.  In  Proceedings  of  the  2024  2nd
International  Conference  on  Computational  and  Characterization  Techniques  in  Engineering  and
Sciences (IC3TES 2024). IEEE. https://doi.org/10.1109/IC3TES62412.2024.10877548
Billio, M., Getmansky, M., Lo, A. W., & Pelizzon, L. (2012). Econometric measures of connectedness
and systemic risk in the finance and insurance sectors.  Journal of Financial Economics, 104(3), 535–
559. https://doi.org/10.2139/ssrn.1963216
Chaudhry, S. M., Ahmed, R., Huynh, T. L. D., & Benjasak, C. (2022). Tail risk and systemic risk of
finance  and  technology  (FinTech)  firms.  Technological  Forecasting  and  Social  Change,  174,  Article
121191. https://doi.org/10.1016/j.techfore.2021.121191
Liu,  R.,  Yang,  X.,  Dong,  X.,  &  Sun,  B.  (2021).  Credit  risk  assessment  of  banks'  loan  enterprise
customer
145–168.
https://doi.org/10.31577/cai_2021_1_145
Bulut, C., & Arslan, E. (2025). A hybrid approach to credit risk assessment using bill payment habits
data
intelligence.  Applied  Sciences,  15(10),  Article  5723.
artificial
explainable
https://doi.org/10.3390/app15105723

state-constraint.  Computing

Informatics,

40(1),

based

and

and

on

*Corresponding Author: SYED IJAZ AHMED1                  www.aijbm.com                            52 | Page

AI-Driven Credit Risk Assessment in Fintech Lending: Implications for Financial Inclusion…

[11]

[12]

[13]

[14]

[15]

[16]

[17]

[18]

learning.

Liao,  M.,  Jiao,  W.,  &  Zhang,  J.  (2025).  Research  on  trade  credit  risk  assessment  for  foreign  trade
enterprises  based  on  explainable  machine
Information,  16(10),  Article  831.
https://doi.org/10.3390/info16100831
Balyuk, T. (2023). FinTech lending and bank credit access for consumers. Management Science, 69(1),
555–575. https://doi.org/10.1287/mnsc.2022.4319
Balyuk, T., Berger, A. N., & Hackney, J. (2025). What is fueling FinTech lending? The role of banking
market structure. The Review of Corporate Finance Studies. https://doi.org/10.1093/rcfs/cfae028
Nguyen, L.,  & Qiu, B. (2025).  Fintech lending and firm bankruptcies.  Journal of Credit Risk, 21(1),
33–51. https://doi.org/10.21314/JCR.2024.009
Amnas,  M.  B.,  Selvam,  M.,  &  Parayitam,  S.  (2024).  FinTech  and  financial  inclusion:  Exploring  the
mediating  role  of  digital  financial  literacy  and  the  moderating  influence  of  perceived  regulatory
support.
108.
https://doi.org/10.3390/jrfm17030108
Tay,  L.  Y.,  Tai,  H.  T.,  &  Tan,  G.  S.  (2022).  Digital  financial  inclusion:  A  gateway  to  sustainable
development. Heliyon, 8(6), Article e09766. https://doi.org/10.1016/j.heliyon.2022.e09766
Ozili,  P.  K.  (2018).  Impact  of  digital  finance  on  financial  inclusion  and  stability.  Borsa  Istanbul
Review, 18(4), 329–340. https://doi.org/10.1016/j.bir.2017.12.003
Tram, T. X. H., Lai, T. D., & Nguyen, T. T. H. (2023). Constructing a composite financial inclusion
index  for  developing  economies.  Quarterly  Review  of  Economics  and  Finance,  87,  257–265.
https://doi.org/10.1016/j.qref.2021.01.003

Financial  Management,

17(3),  Article

Journal

Risk

and

of

[19]  Wu,  X.  (2023).  The  rise  of  digital  finance  and  systemic  risk:  Implications,  challenges,  and  coping
in  Economics,  Management  and  Political  Sciences,  45(1),  327–333.

[20]

[21]

[22]

[23]

[24]

[25]

[26]

56(38),

Applied

Economics,

strategies.  Advances
https://doi.org/10.54254/2754-1169/45/20230306
Gao, Q., Wu, H., & Yang, C. (2024). The impact of technology finance policies on the systemic risk of
bank-firm
4611–4631.
networks.
https://doi.org/10.1080/00036846.2023.2212971
Hoffart, F. M., D'Orazio, P., Holz, F., & Kemfert, C. (2024). Exploring the interdependence of climate,
finance,  energy,  and  geopolitics:  A  conceptual  framework  for  systemic  risks  amidst  multiple  crises.
Applied Energy, 361, Article 122885. https://doi.org/10.1016/j.apenergy.2024.122885
Bredt,  S.  (2019).  Artificial  intelligence  (AI)  in  the  financial  sector:  Potential  and  public  strategies.
Frontiers in Artificial Intelligence, 2, Article 16. https://doi.org/10.3389/frai.2019.00016
Explainable AI in algorithmic trading: Mitigating bias and improving regulatory compliance in finance.
(2025).  International  Journal  of  Computer  Applications  Technology  and  Research,  14(4).
https://doi.org/10.7753/ijcatr1404.1006
Najib, N. W. M., Basarud-din, S. K., Ghazali, S. F., Abu Kasim, N., Abdullah, N. K., & Wan Mustafa,
W.  A.  (2025).  A  bibliometric  analysis  of  research  trends  in  artificial  intelligence  (AI)  and  finance
(2015–2025).  Journal  of  Information  System  and  Technology  Management,  10(40),  88–103.
https://doi.org/10.35631/jistm.1040007
Akerlof, G. A. (1970). The market for "lemons": Quality uncertainty and the market mechanism.  The
Quarterly Journal of Economics, 84(3), 488–500. https://doi.org/10.2307/1879431
Stiglitz,  J.  E.,  &  Weiss,  A.  (1981).  Credit  rationing  in  markets  with  imperfect  information.  The
American Economic Review, 71(3), 393–410. https://www.jstor.org/stable/1802787

[27]  Merton,  R.  C.  (1995).  A  functional  perspective  of  financial  intermediation.  Financial  Management,

[28]

[29]

[30]

24(2), 23–41. https://www.jstor.org/stable/3665532
Eisenhardt,  K. M. (1989). Building theories from case  study research. The Academy of Management
Review, 14(4), 532–550. https://doi.org/10.5465/amr.1989.4308385
Akinnagbe, O. B., Akintayo,  T. A., &  Adanna,  A. B. (2025). The impact of artificial intelligence on
risk management in banking and finance. Mikailalsys Journal of Advanced Engineering International,
2(2), 118–128. https://doi.org/10.58578/mjaei.v2i2.5195
Du, G., & Elston, F. (2022). Financial risk assessment to improve the accuracy of financial prediction
in the  internet  financial industry  using data  analytics  models.  Operations  Management Research, 16,
967–979. https://doi.org/10.1007/s12063-022-00293-5

*Corresponding Author: SYED IJAZ AHMED1                  www.aijbm.com                            53 | Page

