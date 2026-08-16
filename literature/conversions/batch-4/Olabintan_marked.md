---
conversion_metadata:
  converted_at: "2026-07-21T07:54:09Z"
  converter_tool: "markitdown"
  converter_version: "0.1.6"
  source_pdf: "Olabintan.pdf"
  source_pdf_sha256: "08d04041b7cd0f5676e88c770e444c757cb987c8eaaf74ca7c5d7b0c5dd19f88"
  page_count: 24
  markdown_char_count: 115550
---

<!-- PAGE-AWARE EXTRACTION (via pdfminer.six) -->

<!-- PAGE 1 -->

FairLend-Africa: An Explainable Machine Learning 
Framework for Alternative Credit Scoring Using 
Behavioral Financial Data in Financially Excluded 
African Communities

Ibraheem Olabintan 
Kebbi State University of Science and Technology  
Aliero, Kebbi State, Nigeria

Abstract:

Access to formal credit remains constrained for much of the African population due to a lack of 
conventional  credit  histories.  This  paper  investigates  whether  behavioral  financial  data  mobile 
money  transactions,  airtime  patterns,  and  savings  consistency  can  serve  as  valid  proxies  for 
creditworthiness.  We  present  FairLend-Africa,  an  explainable  machine  learning  framework 
combining XGBoost scoring with SHAP interpretability and systematic fairness auditing. Using a 
synthetic dataset of 10,000 borrower records, the system achieves a held-out test ROC-AUC of 
0.7137, which aligns with performance baselines established in thin-file behavioral credit scoring 
literature.  Within  the  controlled  synthetic  data  generation  boundaries,  the  audit  pipeline 
demonstrates  no  disparity  under  the  synthetic  data's  demographic-behavioral  independence 
assumption a condition requiring empirical verification with real data before deployment claims 
can be made. SHAP analysis identifies wallet balance trend and savings consistency as dominant 
signals. A logistic regression baseline matches the XGBoost performance, suggesting primarily 
linear structures in the synthetic data and motivating validation on real-world datasets where non-
linear interactions may emerge. The system is implemented as a REST API with an interactive 
dashboard  released  as  open  source  to  support  reproducibility  in  African  financial  inclusion 
research.

Keywords: alternative credit scoring, explainable artificial intelligence, financial inclusion, 
mobile money, SHAP, XGBoost, fairness in machine learning, African fintech

1. Introduction

Approximately 1.4 billion adults worldwide remain unbanked, with Sub-Saharan Africa accounting for a 
disproportionate share of this population (Demirgüç-Kunt et al., 2022). Among the structural barriers to 
financial  inclusion,  the  absence  of  formal  credit  history  represents  one  of  the  most  consequential. 
Conventional credit scoring systems whether bureau-based or institution-internal rely on records of prior 
formal borrowing, repayment behavior, and account standing. For individuals who have never held a formal 
bank  account,  these  systems  produce  either  a  null  score  or  a  rejection  by  default,  regardless  of  actual 
financial behavior or repayment capacity.

The  proliferation  of  mobile  money  services  across  Africa  has  created  an  alternative  source  of  financial 
behavioral data. Mobile money systems such as M-Pesa in Kenya and MTN Mobile Money across West 
Africa generate transaction records that digital lenders ingest via distinct modalities: either direct bank-
telco  utility  integrations  (e.g.,  M-Shwari)  or  client-side  smartphone  scraper  APIs  parsing  local  SMS 
notification  receipts  (e.g.,  Tala,  Branch,  Carbon)  (GSMA,  2023)  that  capture  income  frequency, 
expenditure patterns, savings  behavior,  and  network  activity.  Prior  research  has  demonstrated that  such

FairLend-Africa  |  Ibraheem Olabintan  |  KSUSTA  |  Page 1

---

<!-- PAGE 2 -->

behavioral  signals  carry  meaningful  predictive  information  about  creditworthiness  (Björkegren  and 
Grissen, 2018; Suri and Jack, 2016), yet their integration into formal credit assessment frameworks remains 
limited, particularly in contexts where explainability and fairness are simultaneously required.

For  clarity,  we  distinguish  what  this  paper contributes  from  what  it  does  not. This  paper contributes: a 
framework  design  for  behavioral  credit  scoring  with  explainability  and  fairness  auditing;  an  evaluation 
protocol  applicable  to  any  binary  credit  classification  problem;  and  an  open-source  implementation 
lowering barriers for MFI experimentation. This paper does not contribute: empirical claims about African 
borrower behavior; fairness guarantees for real lending systems; or performance benchmarks generalizable 
beyond the synthetic data generating process.

This paper makes three contributions. First, we propose and implement a feature engineering methodology 
that constructs interpretable behavioral credit signals from mobile money transaction data, airtime recharge 
patterns, savings behavior, and loan history. Second, we demonstrate that an XGBoost classifier trained on 
these features achieves a ROC-AUC of 0.7137, a result consistent with the difficulty of behavioral credit 
scoring tasks and with results reported in comparable literature. Third, we conduct a systematic fairness 
audit using three criteria from the algorithmic fairness literature demographic parity, equal opportunity, and 
predictive parity  and find no meaningful disparities across regional and gender subgroups. Throughout, 
SHAP values provide individual-level explanations that render the model's decisions interpretable to non-
technical stakeholders such as loan officers and borrowers.

We  note  an  important  scope  boundary:  this  paper  is  a  methodological  demonstration  rather  than  an 
empirical study of real African borrower behavior. All results predictive performance, feature importance 
rankings,  and  fairness  audit  outcomes  are  properties  of  the  synthetic  data  generating  process  and  the 
proposed framework applied to it. We make no claims about how these results would generalize to real 
mobile money data, and we present the framework explicitly as infrastructure for future empirical work 
rather  than  as  evidence  of  real-world  credit  scoring  capability.  This  framing  follows  the  precedent  of 
simulation-based methodology papers in applied ML research, where the contribution is the framework 
design  and  evaluation  protocol  rather  than  empirical  claims  about  a  specific  population  (Biecek  and 
Burzykowski, 2021).

The remainder of this paper is organized as follows. Section 2 reviews relevant literature. Section 3 defines 
the problem formally. Section 4 describes the synthetic dataset and its design rationale. Section 5 presents 
the  feature  engineering  methodology.  Section  6  describes  the  system  architecture.  Section  7  presents 
experimental  results.  Section  8  reports  the  fairness  analysis.  Section  9  discusses  implications  and 
limitations. Section 10 concludes.

2. Literature Review

2.1 Financial exclusion and credit access in Africa

Financial  exclusion  in  Sub-Saharan  Africa  is  structurally  rooted  in  infrastructure  gaps,  documentation 
barriers, and the dominance of informal economic activity (Chiteli, 2013). Ledgerwood (1999) documented 
how  microfinance  institutions  (MFIs)  attempted  to  bridge  this  gap  through  group  lending  and  social 
collateral  mechanisms,  with  repayment  rates  frequently  exceeding  80  percent  in  well-managed 
programmes. More recently, Totolo (2018) documented how Kenya's digital credit revolution shifted the 
paradigm  toward  high-frequency,  automated  credit  assessment,  albeit  with  new  risks  regarding  digital 
delinquiry and debt stress among previously unscored populations.

FairLend-Africa  |  Ibraheem Olabintan  |  KSUSTA  |  Page 2

---

<!-- PAGE 3 -->

2.2 Alternative data in credit scoring

The use of alternative data sources in credit scoring has been studied across multiple contexts. Khandani et 
al. (2010) demonstrated that consumer transaction data from retail banking systems could produce credit 
scores  with  AUC  values  competitive  with  bureau-based  models.  Björkegren  and  Grissen  (2018)  used 
mobile  phone  metadata  including  call  records  and  recharge  patterns  to  predict  loan  repayment  among 
borrowers in Rwanda, reporting AUC  values of approximately 0.70, and found that behavioral features 
captured creditworthiness signals invisible to conventional scoring. Agarwal et al. (2020) examined fintech 
lending  in  India  and  found  that  alternative  data  improved  inclusion  for  thin-file  borrowers  without 
degrading portfolio quality.

In the African context specifically, Suri and Jack (2016) documented the welfare effects of M-Pesa adoption 
in Kenya, showing that mobile money enabled households particularly female-headed households to better 
navigate income shocks through social network transfers. While their study did not directly measure credit 
repayment capacity, the demonstrated link between mobile money usage and financial resilience provides 
theoretical grounding for behavioral transaction data as a creditworthiness proxy. Lauer and Lyman (2015) 
reviewed  digital  financial  inclusion  initiatives  across  low-income  markets  and  identified  transaction 
frequency and regularity as the most actionable behavioral signals for credit assessment.

2.3 Machine learning in credit scoring

Machine learning methods have been applied extensively to credit scoring since the foundational work of 
Baesens et al. (2003), who compared neural networks, support vector machines, and logistic regression 
across multiple credit datasets and found that ensemble methods generally outperformed single classifiers. 
XGBoost (Chen and Guestrin, 2016) has become a standard baseline in credit scoring competitions and 
applied  research  due  to  its  strong  performance  on  tabular  data,  resistance  to  overfitting  through 
regularization, and compatibility with post-hoc explainability methods.

2.4 Explainability in credit decisions

The requirement for explainability in credit decisions is both regulatory and ethical. The European Union's 
General Data Protection Regulation (GDPR) Article 22 establishes a right to explanation for automated 
decisions,  and  equivalent  frameworks  are  emerging  in  several  African  jurisdictions.  Lundberg  and  Lee 
(2017)  introduced  SHAP  as  a  unified  framework  for  model  explanation  grounded  in  cooperative  game 
theory. Unlike earlier feature importance measures, SHAP values satisfy desirable axioms including local 
accuracy, missingness, and consistency, making them appropriate for credit decision explanation (Lundberg 
et al., 2020). Ribeiro et al. (2016) proposed LIME as an alternative local explanation method, but SHAP 
has demonstrated superior stability and theoretical grounding for tree-based models. However, recent work 
has demonstrated that post-hoc explanation methods can be manipulated to conceal systematic bias (Slack 
et al., 2020); this adversarial vulnerability is discussed as a limitation in Section 9.2.

2.5 Fairness in algorithmic credit scoring

Algorithmic fairness in lending has received substantial research attention following evidence that machine 
learning  models  can  perpetuate  or  amplify  historical  discrimination  (Barocas  and  Hardt,  2017). 
Chouldechova  (2017)  demonstrated  the  impossibility  theorem:  no  classifier  can  simultaneously  satisfy 
sufficiency (calibration/predictive parity) and separation (equalized error rates across groups) when base 
rates differ across groups. This necessitates explicit fairness criterion selection rather than the assumption 
that fairness can be comprehensively achieved. Fuster et al. (2022) examined fintech lending algorithms

FairLend-Africa  |  Ibraheem Olabintan  |  KSUSTA  |  Page 3

---

<!-- PAGE 4 -->

and  found  that  while  they  improved  access  for  some  minority  groups,  behavioral  proxies  could encode 
demographic  information  through  indirect  pathways.  Our  analysis  explicitly  tests  for  such  proxy 
relationships.  Kozodoi  et  al.  (2022)  provided  a  business-oriented  framework  mapping  predictive 
performance trade-offs directly to credit scoring models, demonstrating that fairness constraints impose 
measurable costs on model profitability a tension directly relevant to microfinance deployment contexts. 
Recent work has further shown that alternative behavioral features including the mobile money signals used 
in  this  study  can  act  as  proxies  for  socioeconomic  stratification,  potentially  exacerbating  geographic 
discrimination under the guise of neutral algorithmic scoring (Blattner and Nelson, 2021).

3. Problem Statement

𝑛   denoted a  dataset  of  n  borrowers,  where  𝑥𝑖 ∈ 𝑅𝑝    is  a  vector  of  p behavioral 
Let D  = {( 𝑥𝑖, 𝑑𝑖, 𝑦𝑖)}𝑖=1
financial features, 𝑑𝑖 is a vector of demographic attributes, and 𝑦𝑖 ∈ {0,1} is a binary repayment label (1 = 
repaid, 0 = defaulted).

We seek a classifier 𝑓: 𝑅𝑝   → [0,1] that:

1.  Predicts  accurately:  maximize  ROC-AUC  on  held-out  data,  using  only  𝑥𝑖 (𝑛𝑜𝑡 𝑑𝑖)  as  input

features.

2.  Explains locally: for only borrower 𝑥𝑖 produces SHAP explanation vector  ∅𝑖   ∈   𝑅𝑝  satisfying 
𝑝
𝑓(𝑥𝑖) =   ∅0 +   ∑
,  where  ∅0  is  the  base  rate  and  ∅𝑖𝑗  is  the  contribution  of  feature  𝑗.  We 
𝑗=1
acknowledge  that  while  SHAP  provides  exact  explanations  for  tree  models,  it  assumes  feature 
independence when computing conditional expectations a mathematical vulnerability we address 
as a limitation in Section 9.2 (kumar et al., 2020).

∅𝑖𝑗

3.  Satisfies fairness criteria: for demographic subgroups defined by 𝑑𝑖, produces selection rates, true

positive rates, and precision values with disparity ratios exceeding 0.80 across all groups.

The exclusion of  𝑑𝑖 from model inputs is a design choice grounded in fair lending principles. The retention 
of  𝑑𝑖 in the dataset serves only the post-hoc fairness audit.

4. Dataset Design

4.1 Motivation for synthetic data

The use of real mobile money transaction data for research purposes faces substantial barriers: data access 
requires institutional partnerships with telecom operators or MFIs, raises privacy concerns under emerging 
African data protection frameworks including the Kenya Data Protection Act (2019) and the Nigeria Data 
Protection Act (2023) which restrict the processing of consumer transaction records without explicit consent 
(Greenleaf,  2021),  and  introduces  selection  biases  from  the  specific  institution's  customer  base.  We 
therefore adopt a synthetic data generation approach, which allows full transparency of the data generating 
process, enables reproducibility without data sharing agreements, and permits deliberate design of feature 
relationships grounded in literature.

This approach is consistent with established practice in privacy-sensitive ML research (Jordon et al., 2022) 
and with similar methodological choices in alternative credit scoring studies where real data could not be 
shared (Khandani et al., 2010).

4.2 Feature design rationale

FairLend-Africa  |  Ibraheem Olabintan  |  KSUSTA  |  Page 4

---

<!-- PAGE 5 -->

Table 1 presents the 16 raw behavioral features included in the dataset, organized by source domain. Figure 
1 illustrates the bivariate distributions of key features by repayment outcome.

Table 1: Raw behavioral features

Feature 
monthly_txn_count 
avg_txn_amount_usd 
wallet_balance_trend 
airtime_recharge_freq 
airtime_avg_amount_usd 
has_savings_account 
savings_consistency_score 
monthly_savings_usd 
has_prior_loan 
prior_loan_repayment_rate 
days_late_avg 
network_diversity_score 
bill_payment_regularity 
merchant_payment_count 
loan_amount_requested_usd 
loan_duration_weeks

Domain 
Mobile money 
Mobile money 
Mobile money 
Airtime 
Airtime 
Savings 
Savings 
Savings 
Credit history 
Credit history 
Credit history 
Social 
Payments 
Payments 
Loan request 
Loan request

Behavioral rationale 
Transaction frequency proxies income regularity 
Average value proxies income level 
Growing balance signals financial surplus 
Recharge frequency signals liquidity 
Larger recharges signal stable cash flow 
Account ownership signals planning behavior 
Regular saving signals financial discipline 
Savings volume signals surplus capacity 
Prior borrowing signals credit experience 
Repayment rate is direct creditworthiness signal 
Late payments signal repayment stress 
Counterparty diversity signals economic integration 
Regular bills signal stable income and obligations 
Merchant activity signals economic participation 
Loan size relative to behavioral capacity 
Loan term as risk exposure measure

Figure 1. Feature distributions by repayment outcome. Overlapping histograms show visible separation 
between repayers (green) and defaulters (red) across key behavioral features, confirming predictive signal 
in the dataset.

FairLend-Africa  |  Ibraheem Olabintan  |  KSUSTA  |  Page 5

---

<!-- PAGE 6 -->

4.3 Label generation

The binary repayment label is generated via a logistic data generating process with coefficients calibrated 
to reflect the hypothesized behavioral creditworthiness relationships:

The  complete  coefficient  vector  used  in  the  data  generating  process  is  provided  in  Table  2  for  full 
reproducibility. The resulting class distribution of the generated labels is shown in Figure 2.

Table 2: Data generating process coefficients

Feature 
Intercept 
wallet_balance_trend 
monthly_txn_count (normalized) 
savings_consistency_score (normalized) 
has_savings_account 
airtime_recharge_freq (normalized) 
prior_loan_repayment_rate 
days_late_avg (normalized) 
bill_payment_regularity (normalized) 
network_diversity_score (normalized) 
loan_amount_requested_usd (normalized) 
Noise term ε

Coefficient (β) 
0.0 
+0.8 
+0.5 
+0.6 
+0.7 
+0.4 
+0.9 
-0.6 
+0.3 
+0.2 
-0.4 
σ=0.3

Direction 
— 
Positive 
Positive 
Positive 
Positive 
Positive 
Positive 
Negative 
Positive 
Positive 
Negative 
—

Note: All normalized features were Z-scored before applying coefficients; the intercept of 0 yields a base 
repayment  probability  of  0.50  before  the  logistic  transform.  Binary  features  (has_savings_account, 
has_prior_loan)  were  not  normalized.  The  noise  term  ε  ~  N(0,  0.3)  was  added  to  the  log-odds  before 
applying  the  sigmoid.  Complete  generation  code  is  available  in  `src/data/generate_dataset.py`  in  the 
project repository.

Figure 2. Class distribution of the repayment label. The dataset contains 7,553 repayers (75.53%) and 
2,447  defaulters  (24.47%),  consistent  with  repayment  rates  reported  in  African  microfinance  literature 
(Ledgerwood, 1999).

FairLend-Africa  |  Ibraheem Olabintan  |  KSUSTA  |  Page 6

---

<!-- PAGE 7 -->

4.4 Missing data

Features derived from prior loan history (“prior_loan_repayment_rate”, “days_late_avg”) are missing for 
5,503  borrowers  (55.03  percent)  who  have  no  prior  loan  history.  This  missingness  is  Missing  Not  At 
Random  (MNAR):  the  absence  of  a  value  is  itself  informative,  indicating  a  first-time  borrower.  This 
characteristic reflects a genuine challenge in alternative credit scoring for financially excluded populations. 
Missing  values  are  handled  via  median  imputation  within  the  sklearn  pipeline  after  train/test  splitting, 
ensuring  no  information  leakage  from  the  test  set.  We  acknowledge  that  median  imputation  assumes 
Missing At Random (MAR), which is technically inconsistent with the MNAR mechanism identified here. 
A more rigorous approach would employ multiple imputation with chained equations (van Buuren, 2018) 
or  pattern  mixture  models.  However, 
indicator 
(“no_prior_loan_flag”) partially compensates by preserving the structural information in the missingness 
pattern. We identify this as a methodological limitation. Median imputation on MNAR data likely biases 
coefficient estimates toward zero, attenuating the predictive contribution of prior loan history features. We 
retain median imputation as a practical deployment compromise  it is implementable in a single sklearn 
pipeline step without external dependencies but explicitly recommend multiple imputation with chained 
equations (MICE) for any research application where statistical validity of coefficient estimates matters.

the  binary  missingness

the  addition  of

4.5 Dataset statistics

The  final  dataset  contains  10,000  records,  20  model  features  (16  raw  +  4  engineered),  4  demographic 
attributes retained for fairness auditing, and a binary repayment label. The dataset and generation code are 
released in the project repository.

5. Feature Engineering

Beyond the 16 raw behavioral features, three composite features were engineered to capture higher-order 
behavioral signals:

intensity (𝑡𝑥𝑛−𝑖𝑛𝑡𝑒𝑛𝑠𝑖𝑡𝑦):  defined

Transaction 
log( 1 + 𝑚𝑜𝑛𝑡ℎ𝑙𝑦_𝑡𝑥𝑛_𝑐𝑜𝑢𝑛𝑡 )   × log(1 +
𝑎𝑣𝑔_𝑡𝑥𝑛 _𝑎𝑚𝑜𝑢𝑛𝑡_𝑢𝑠𝑑 ) . This multiplicative interaction captures the joint signal of frequency and value, 
distinguishing  high-volume  low-value  activity  from  moderate-volume  higher-value  activity  two  distinct 
behavioral profiles in mobile money literature (Björkegren and Grissen, 2018).

as

Savings  commitment  ratio  (𝑠𝑎𝑣𝑖𝑛𝑔𝑠_𝑐𝑜𝑚𝑚𝑖𝑡𝑚𝑒𝑛𝑡_𝑟𝑎𝑡𝑖𝑜):  defined  as  𝑚𝑜𝑛𝑡ℎ𝑙𝑦_𝑠𝑎𝑣𝑖𝑛𝑔𝑠_𝑢𝑠𝑑  /
 (𝑎𝑣𝑔_𝑡𝑥𝑛_𝑎𝑚𝑜𝑢𝑛𝑡_𝑢𝑠𝑑   +   1 ) . This ratio normalizes savings volume by transaction activity, capturing 
whether a borrower actively sets money aside relative to their financial throughput, a behavioral signal of 
forward planning. We anticipate that these engineered interactions may exhibit negligible predictive lift on 
synthetic data relative to raw behavioral features (see Section 9.2).

Airtime 
𝑎𝑖𝑟𝑡𝑖𝑚𝑒_𝑎𝑣𝑔_𝑎𝑚𝑜𝑢𝑛𝑡  /
(𝑎𝑖𝑟𝑡𝑖𝑚𝑒_𝑟𝑒𝑐ℎ𝑎𝑟𝑔𝑒_𝑓𝑟𝑒𝑞   + 1 ).  Frequent small recharges have been identified as a mobile money stress

(𝑎𝑖𝑟𝑡𝑖𝑚𝑒_𝑠𝑡𝑎𝑏𝑖𝑙𝑖𝑡𝑦 ):

stability

defined

as

signal (Lauer and Lyman, 2015); a higher stability ratio indicates fewer, larger recharges consistent with 
stable cash flow.

A  binary  missingness  indicator  (`no_prior_loan_flag`)  was  added  as  the  fourth  engineered  feature,  as 
described in Section 4.4.

Figure 3 presents the Pearson correlation matrix across all features.

FairLend-Africa  |  Ibraheem Olabintan  |  KSUSTA  |  Page 7

---

<!-- PAGE 8 -->

Figure 3. Pearson correlation matrix across all features and the repayment label. Moderate inter-feature 
correlations among savings features are expected and do not constitute problematic multicollinearity.

6. System Architecture

FairLend-Africa is implemented as a three-tier system:

Data  and  model  tier:  Python-based  ML  pipeline  using  scikit-learn  (Pedregosa  et  al.,  2011)  for 
preprocessing and XGBoost (Chen and Guestrin, 2016) for classification. SHAP (Lundberg and Lee, 2017) 
provides post-hoc explanations. All artifacts are serialized using joblib and versioned in the repository.

API tier: FastAPI application exposing three endpoints: `POST /api/v1/predict` returns a credit decision 
and  score  for  a  given  borrower;  `POST  /api/v1/explain`  returns  the  prediction  with  full  SHAP 
decomposition; `GET /api/v1/evaluate` returns cached model performance metrics. Prediction requests are 
logged to a PostgreSQL database for audit purposes.

Presentation tier: React dashboard with three views: borrower input form, credit decision display with 
SHAP bar chart visualization, and model metrics panel. The dashboard is designed for loan officer use the 
SHAP chart presents the top contributing features in plain language alongside their directional effect on the 
credit decision.

FairLend-Africa  |  Ibraheem Olabintan  |  KSUSTA  |  Page 8

---

<!-- PAGE 9 -->

The system does not include mechanisms for monitoring model performance drift over time. Credit scoring 
models are subject to concept drift as economic conditions and borrower behavior evolve; temporal stability 
evaluation is identified as a limitation in Section 9.2 and recommended before any production deployment.

The system is deployable on free-tier cloud infrastructure (Render or Railway for the API, Vercel for the 
frontend)  without  requiring  institutional  cloud  resources,  consistent  with  the  accessibility  goals  of  the 
research.

7. Experiments and Results

7.1 Experimental setup

The  dataset  was  split  into 80  percent  training  (8,000 records) and 20  percent test (2,000 records)  using 
stratified sampling to preserve the class ratio. The ML pipeline consists of median imputation, standard 
scaling, 
classifier.  Hyperparameter  optimization  was  performed  via 
RandomizedSearchCV over 30 iterations with 5-fold stratified cross-validation, optimizing for ROC-AUC. 
The final optimized parameters are listed in Table A1 in the Appendix.

an  XGBoost

and

7.2 Model performance

Table 3 presents evaluation results across three model configurations on the held-out test set.

Table 3: Model comparison test set performance (95% bootstrap CI, n=1000)

Configuration

Accuracy  Precision

Recall

class

Majority 
baseline 
Logistic Regression

0.755

—

—

0.760

0.770

0.960

0.860

F1

—

Baseline XGBoost 
Tuned XGBoost

0.664 
0.620

0.824 
0.862 
0.883]

[0.841,

0.706 
0.600  [0.574, 
0.625]

0.760 
0.707 
[0.686, 
0.727]

ROC-AUC

Threshold

—

0.5

0.5 
0.151

0.500

0.713 
[0.688, 
0.738] 
0.675 
0.714 
[0.688, 
0.739]

Note:  Confidence  intervals  for  logistic  regression  precision,  recall,  and  F1  are  omitted  for  brevity; 
bootstrap estimation confirmed they are similar in width to the tuned XGBoost intervals reported above.

Table  3  includes  a  logistic  regression  baseline  trained  on  the  same  feature  set  and  pipeline.  Logistic 
regression  achieves  substantially  higher  recall  (0.960)  than  the  baseline  XGBoost  (0.706)  at  the  same 
classification  threshold  of  0.5,  reflecting  differences  in  probability  estimation  between  model  classes 
uncalibrated tree-based ensembles often generate biased probability distributions compared to generalized 
linear models, though calibration quality depends on the degree of model misspecification in both cases 
(Niculescu-Mizil and Caruana, 2005). We emphasize that these distortions are typical of tree-based models 
on tabular layouts; mapping these parameters onto actual, non-stationary mobile wallets remains an open 
empirical challenge. Both models were evaluated without additional calibration to preserve comparability 
with the threshold analysis. The logistic regression achieves a ROC-AUC of 0.713 compared to 0.714 for 
the tuned XGBoost a difference of 0.001, which is within the bootstrap confidence interval width of both 
models and should not be interpreted as meaningful. This finding suggests that the behavioral features in 
this synthetic dataset exhibit primarily linear relationships with the repayment label, and that XGBoost's 
capacity for non-linear interaction modelling provides no measurable benefit over logistic regression under

FairLend-Africa  |  Ibraheem Olabintan  |  KSUSTA  |  Page 9

---

<!-- PAGE 10 -->

these conditions. This finding is notable given that Baesens et al. (2003) found that advanced classifiers 
outperformed  logistic  regression  across  multiple  real-world  credit  datasets,  suggesting  that  the  near-
identical performance observed here is a property of the linear synthetic data generating process rather than 
a general characteristic of credit scoring tasks. We retain XGBoost as the primary model for this framework 
demonstration for two reasons. First, the SHAP TreeExplainer provides exact Shapley values for tree-based 
models rather than the kernel approximations required for linear models, making the explainability analysis 
in Section 7.3 more theoretically rigorous. Second, real mobile money data is expected to exhibit non-linear 
feature interactions that XGBoost would capture but logistic regression would not making XGBoost the 
more appropriate demonstration vehicle for the framework's intended real-world application. However, we 
note  that  for  practitioners  deploying  on  current  synthetic-equivalent  data,  logistic  regression  offers 
comparable discrimination (AUC 0.713) with inherent coefficient interpretability and lower computational 
cost. The framework is compatible with either model class.

The tuned model achieves a ROC-AUC of 0.7137, representing a 5.7 percent relative improvement over 
the  baseline.  This  result  is  consistent  with  alternative  credit  scoring  studies  using  behavioral  data: 
Björkegren and Grissen (2018) report AUC values of approximately 0.70 using mobile phone metadata, 
and  Khandani  et  al.  (2010)  report  AUC  values  of  0.68–0.72  using  consumer  transaction  logs  from  a 
traditional  commercial  bank  in  North  America.  This  demonstrates  that  while  alternative  transactional 
signals yield a broadly comparable mathematical baseline across disparate market structures, the underlying 
socioeconomic  data-generating  dynamics  remain  fundamentally  distinct.  Under  the  synthetic  data 
generating  process,  behavioral  alternative  features  carry  sufficient  predictive  signal  to  demonstrate  the 
framework's discrimination capacity. Whether this generalizes to real mobile money data remains an open 
empirical question.

The  optimal  classification threshold  identified  via  precision-recall  curve  analysis  is  0.151,  substantially 
below the conventional 0.5 default. This reflects the cost asymmetry of the lending context: misclassifying 
a defaulter as creditworthy carries greater institutional cost than rejecting a creditworthy borrower (Baesens 
et al., 2003; Kozodoi et al., 2022). We present all three configurations to support transparent reporting of 
this  tradeoff  rather  than  selectively  reporting  the  configuration  with  the  highest  single  metric.  F1 
optimization implicitly assumes equal costs for false positives and false negatives. In practice, microfinance 
lenders typically assign higher cost to false negatives (approving a defaulter) than false positives (rejecting 
a creditworthy borrower), with cost ratios ranging from 2:1 to 5:1 depending on loan size and institutional 
context (Baesens et al., 2003). The low optimal threshold of 0.151 reflects the class imbalance correction 
applied during tuning rather than an explicit cost-benefit specification. Practitioners should recalibrate this 
threshold using institution-specific cost ratios before deployment.

Two aspects of Table 3 require explicit discussion. First, the tuned model achieves lower overall accuracy 
(0.620) than the baseline (0.664). This reflects the effect of the low optimal threshold (0.151): the tuned 
model classifies nearly all borrowers as repayers, producing a selection rate approaching 1.0 on the test set. 
While this maximizes recall for the repayment class, it reduces overall accuracy below the naive majority-
class baseline (0.755). This tradeoff is deliberate given the threshold optimization objective (maximizing 
F1 via precision-recall analysis) but would require careful cost-benefit analysis before deployment.

Second, the near-universal selection rate means the fairness analysis which compares selection rates across 
demographic groups is evaluating a near-trivial condition. When all borrowers are approved, demographic 
parity  is  automatically  satisfied.  This  is  an  important  limitation  of  the  current  threshold  setting  and  is 
addressed in the fairness limitations discussion in Section 8.4.

FairLend-Africa  |  Ibraheem Olabintan  |  KSUSTA  |  Page 10

---

<!-- PAGE 11 -->

Figure 4. ROC curve on held-out test set (n=2,000). The tuned XGBoost model achieves AUC = 0.7137, 
indicating meaningful discrimination ability beyond the random baseline (dashed line).

Figure 5. Confusion matrix on held-out test set. Rows represent actual labels; columns represent predicted 
labels.

FairLend-Africa  |  Ibraheem Olabintan  |  KSUSTA  |  Page 11

---

<!-- PAGE 12 -->

Figure 6. Performance comparison across three model configurations on the held-out test set.

7.3 SHAP feature importance

Table 4 presents the five highest-impact features ranked by mean absolute SHAP value across all 2,000 test 
borrowers.  The  five  most  impactful  features  are  visualized  in  Figure  7  (Global  Importance),  Figure  8 
(Beeswarm Summary), and Figure 9 (Dependence Plots):

Table 4: Top 5 features by mean absolute SHAP value

Feature

Mean | SHAP | (log-odds)

Interpretation

wallet_balance_trend

0.3767

Primary creditworthiness signal

savings_consistency_score

0.2162

Financial discipline indicator

monthly_savings_usd

has_savings_account

txn_intensity

0.1255

0.0554

0.0348

Savings capacity indicator

Financial planning indicator

Engineered transaction signal

SHAP  values  are  expressed  in  log-odds  space,  reflecting  the  XGBoost  model's  raw  output  before  the 
sigmoid transformation to probability.

FairLend-Africa  |  Ibraheem Olabintan  |  KSUSTA  |  Page 12

---

<!-- PAGE 13 -->

Figure  7.  Global  feature  importance  measured  by  mean  absolute  SHAP  value  across  all  2,000  test 
borrowers. Wallet balance trend dominates all other features by a factor of 1.74 times the second-ranked 
feature.

“wallet_balance_trend” dominates all other features by a factor of 1.74 times the second-ranked feature, 
confirming the theoretical expectation that balance trajectory is the strongest behavioral creditworthiness 
signal. Notably, “txn_intensity” an engineered composite feature appears in the top five by mean absolute 
SHAP  value.  However,  a  feature  ablation  study  comparing  the  full  20-feature  set  (ROC-AUC:  0.714) 
against  the  16  raw  features  alone  (ROC-AUC:  0.714)  reveals  that  the  engineered  features  provide  no 
measurable improvement in predictive performance on this dataset. We interpret this as evidence that the 
raw behavioral features already capture the underlying signals that the composite features were designed to 
encode, at least under the linear data generating process used here. The engineered features may provide 
greater value on real mobile money data where non-linear interactions are more pronounced. This finding 
underscores  the  importance  of  ablation  studies  in  feature  engineering  validation,  which  are  frequently 
omitted in applied ML research.

Loan  request  features  (“loan_amount_requested_usd”,  “loan_duration_weeks”)  rank  among  the  lowest-
importance features, indicating that the model learned to predict repayment primarily from how borrowers 
manage money daily rather than from the characteristics of the loan being requested. This is a theoretically 
meaningful finding consistent with empirical research on micro-liquidity tracking, where small, consistent 
transactional  movements  serve  as  a  proxy  for  operational  cash-flow  stability  rather  than  static  asset 
thresholds (Lauer and Lyman, 2015).

FairLend-Africa  |  Ibraheem Olabintan  |  KSUSTA  |  Page 13

---

<!-- PAGE 14 -->

Figure 8. SHAP beeswarm plot. Each point represents one borrower. Position on the x-axis indicates SHAP 
value magnitude and direction. Color encodes feature value (red = high, blue = low). Features are ordered 
by mean absolute SHAP value.

FairLend-Africa  |  Ibraheem Olabintan  |  KSUSTA  |  Page 14

---

<!-- PAGE 15 -->

Figure  9.  SHAP  dependence  plots  for  the  four  highest-importance  features.  Each  point  represents  one 
borrower.  The  plots  reveal  the  nature  of  feature-prediction  relationships  under  the  synthetic  data 
generating process; the near-identical performance of logistic regression suggests these relationships are 
predominantly linear on this dataset.

7.4 Local explainability

For  each  borrower,  SHAP  waterfall  plots  decompose  the  prediction  into  feature-level  contributions, 
showing how each behavioral signal pushes the probability above or below the model's base rate of 0.64. 
Note that this base rate reflects the model's expected value under the SHAP background distribution (the 
500-sample training background used for TreeExplainer), which differs from the empirical repayment rate 
of 75.53% shown in Figure 2. The SHAP base rate is the model's average prediction on the background 
sample, not the dataset's class proportion. Figure 10 illustrates three representative cases: a high-confidence 
repayer, a high-confidence defaulter, and a borderline borrower near the decision threshold.

Figure 10a. Local SHAP explanation  high-confidence repayer. Green bars indicate features supporting 
repayment above the base rate.

FairLend-Africa  |  Ibraheem Olabintan  |  KSUSTA  |  Page 15

---

<!-- PAGE 16 -->

Figure 10b.  Local  SHAP  explanation    high-confidence  defaulter.  Red  bars  indicate  features  increasing 
default risk below the base rate.

Figure 10c. Local SHAP explanation borderline borrower near the decision threshold. Competing positive 
and negative contributions illustrate model uncertainty at the margin.

FairLend-Africa  |  Ibraheem Olabintan  |  KSUSTA  |  Page 16

---

<!-- PAGE 17 -->

This individual-level transparency is particularly important in the African lending context, where borrowers 
may  be  unfamiliar  with  algorithmic  assessment  and  where  regulatory  frameworks  increasingly  require 
explainable credit decisions.

8. Fairness Analysis

8.1 Fairness criteria

We evaluate three criteria from the algorithmic fairness literature:

Demographic  parity  (Dwork  et  al.,  2012):  equal  positive  prediction  rates  across  groups,  assessed  via 
selection rate disparity ratios.

Equal opportunity (Hardt et al., 2016): equal true positive rates across groups, ensuring that creditworthy 
borrowers have equal probability of approval regardless of demographic membership.

Predictive parity: equal precision across groups, ensuring that approved borrowers in each group have 
equal likelihood of actually repaying.

We apply the 80 percent rule as a disparity threshold: a disparity ratio below 0.80 is considered a meaningful 
fairness  violation.  In  the  absence  of  codified  algorithmic  parity  thresholds  within  current  Sub-Saharan 
African financial regulations, we adopt the United States Equal Credit Opportunity Act's 80 percent rule 
strictly as an international baseline indicator for methodological demonstration purposes. We acknowledge 
that  no  equivalent  threshold  has  been formally  adopted  by  regional  bodies such  as  the  Central  Bank  of 
Nigeria or the Central Bank of Kenya. However, recent compliance interventions such as the Central Bank 
of Kenya (Digital Credit Providers) Regulations 2022 signal an escalating regulatory focus on consumer 
privacy, algorithmic transparency, and predatory automated underwriting.

8.2 Results

Table 5 presents disparity ratios for regional and gender subgroups.

Table 5: Fairness disparity ratios by demographic group

Group

West Africa

East Africa

Southern Africa

Central Africa

Female

Male

Prefer not to say

Selection rate

1.000

1.000

1.000

1.000

1.000

1.000

1.000

TPR

1.000

1.000

1.000

1.000

1.000

1.000

1.000

Precision

0.990

0.959

1.000

0.989

1.000

0.977

0.989

All disparity ratios exceed 0.80 across all groups and all criteria. These properties are visualized in Figure 
11 (Demographic Parity) and Figure 12 (Equal Opportunity), while Figure 13 confirms equitable predictive 
consistency via group-wise ROC-AUC. Demographic parity and equal opportunity are satisfied at 1.000

FairLend-Africa  |  Ibraheem Olabintan  |  KSUSTA  |  Page 17

---

<!-- PAGE 18 -->

for every group, indicating that the model approves loans and identifies creditworthy borrowers at equal 
rates regardless of regional origin or gender.

We note that the "Prefer not to say" gender category warrants particular caution in real deployment contexts. 
Unlike  the  Male  and  Female  categories,  this  category  conflates  actual  gender  identity  with  disclosure 
behavior individuals who decline to disclose their gender may differ systematically from those who do, 
meaning the category may itself encode behavioral or socioeconomic information (e.g., Zhang and Long, 
2021).  In  a  real  lending  system,  this  category  should  be  treated  as  a  distinct  analytical  group  requiring 
separate study rather than as a third gender category. In the synthetic dataset, this category was generated 
independently of behavioral features and therefore does not exhibit this confounding.

To  assess  whether  the  fairness  properties  are  robust  to  the  choice  of  operating  threshold,  we  evaluate 
disparity ratios at three additional approval rates spanning realistic microfinance lending contexts. Table 6 
presents selection rate disparity ratios across regional and gender subgroups at four operating points.

Table 6: Selection rate disparity ratios across operating thresholds

Threshold

Approval rate

Region disparity

Gender disparity

Worst group

0.621

0.509

0.433

0.151

30%

50%

70%

100%

0.818

0.811

0.903

1.000

0.932

0.947

0.978

1.000

West Africa

Central Africa

Central Africa

—

All disparity ratios exceed the 0.80 threshold across every operating point evaluated, indicating that the 
fairness properties of the framework are robust to threshold selection and are not an artifact of the near-
universal  approval  rate  at  the  optimal  threshold.  The  most  constrained  operating  point  30%  approval 
produces the lowest observed disparity ratio of 0.818 (West Africa, regional), which passes the 80% rule 
benchmark by a margin of only 0.018. This narrow margin warrants explicit caution: real-world mobile 
money data from West Africa may exhibit structural correlations between region and behavioral features 
due to infrastructure inequality, historical lending patterns, and urbanization differences. Such correlations 
would likely reduce this ratio below the 0.80 threshold, constituting a fairness violation under the same 
benchmark. This robustness analysis addresses the concern that single-threshold fairness evaluation may 
produce misleading results when the chosen threshold produces extreme selection rates (Corbett-Davies et 
al., 2017).

FairLend-Africa  |  Ibraheem Olabintan  |  KSUSTA  |  Page 18

---

<!-- PAGE 19 -->

Figure 11. Demographic parity analysis. Selection rates by region (left) and gender (right). All groups 
exceed the 80% rule threshold (red dashed line), indicating equal approval rates across subgroups.

Figure 12. Equal opportunity analysis. True positive rates by region (left) and gender (right). All groups 
satisfy equal opportunity, confirming that creditworthy borrowers are identified at equal rates regardless 
of demographic membership.

8.3 Proxy analysis

Pearson correlations between the five highest-impact behavioral features and demographic group encodings 
were computed to assess whether behavioral features inadvertently encode demographic information. The 
maximum absolute correlation observed was 0.054 across all feature-group pairs, indicating no meaningful 
proxy  relationships.  This  finding  partially  addresses  the  concern  raised  by  Fuster  et  al.  (2022)  that 
behavioral proxies may perpetuate demographic discrimination through indirect pathways.

FairLend-Africa  |  Ibraheem Olabintan  |  KSUSTA  |  Page 19

---

<!-- PAGE 20 -->

Figure 13. ROC-AUC by demographic group. All groups exceed the random baseline (0.5) and demonstrate 
consistent discrimination ability, indicating equitable predictive performance across subgroups.

8.4 Fairness limitations

These results must be interpreted with care. The synthetic data generating process explicitly constructed 
demographic attributes to be uncorrelated with behavioral features a condition that may not hold in real-
world  data,  where  structural  inequality  produces  genuine  correlations  between  geography,  gender,  and 
financial behavior. In a real deployment, fairness auditing on actual borrower data would be required before 
drawing  conclusions  about  equitable  treatment.  Furthermore,  we  evaluate  only  three  fairness  criteria; 
satisfying  all  simultaneously  is  mathematically  impossible  when  base  rates  differ  across  groups 
(Chouldechova, 2017), and the selection of criteria should ultimately reflect the values and legal context of 
the deploying institution. Contemporary fairness literature further cautions that optimizing for static group 
parity criteria can cause long-term economic harm by driving vulnerable populations into cycles of default, 
highlighting the need for dynamic or causal fairness formulations in future iterations (Corbett-Davies et al., 
2017).

9. Discussion

9.1 Practical implications

Within the scope of the synthetic data generating process, the results demonstrate that behavioral financial 
data carries sufficient predictive signal to support the proposed framework's credit assessment pipeline. A 
ROC-AUC of 0.714 represents meaningful improvement over the random baseline (0.500), though the near-
identical  performance  of  logistic  regression  (0.713)  and  the  accuracy  below  the  majority-class  baseline 
(0.755 vs 0.620) indicate that the threshold setting and model complexity require careful reconsideration 
before any deployment context. For a microfinance institution serving unscored populations, the practical 
value of the system lies not in replacing human judgment but in providing structured, explainable behavioral 
evidence to supplement it a role for which the SHAP explanation layer is particularly well suited.

The  SHAP  explanation  layer  addresses  a  critical  gap  in  ML-based  credit  systems:  the  inability  to 
communicate  the  basis  of  a  decision  to  the  borrower  or  loan  officer.  The  waterfall  and  bar  chart 
visualizations  implemented  in  the  dashboard  translate  statistical  outputs  into  actionable  language 
identifying, for example, that a borrower's declining wallet balance trend is the primary factor reducing 
their credit probability, which the borrower can act upon.

FairLend-Africa  |  Ibraheem Olabintan  |  KSUSTA  |  Page 20

---

<!-- PAGE 21 -->

9.2 Limitations

Several  limitations  bound  the  conclusions  of  this  study.  First,  the  dataset  is  synthetic.  While  the  data 
generating process is calibrated to reflect behavioral patterns documented in the literature, it cannot capture 
the full complexity of real mobile money data, including temporal dynamics, seasonal patterns, and network 
effects. Validation on real transaction data from a partner institution remains necessary.

Second, the feature set is constructed from literature-informed assumptions rather than empirical feature 
selection  from  real  behavioral  data.  The  relative  importance  of  features  may  differ  substantially  across 
populations, geographies, and mobile money platforms.

Third,  the  fairness  analysis  is  constrained  by  the  synthetic  data's  designed  independence  between 
demographics and behavior. Real-world fairness properties cannot be inferred from this analysis.

Fourth, the system has not been evaluated for temporal stability. Credit scoring models are known to exhibit 
concept drift as economic conditions change, and a production system would require ongoing monitoring 
and retraining.

Fifth, the near-identical performance of logistic regression (ROC-AUC: 0.713) and tuned XGBoost (ROC-
AUC: 0.714) suggests that the behavioral features in the synthetic dataset exhibit primarily linear structure. 
This limits the external validity of the SHAP non-linearity analysis in Section 7.3 and raises the question 
of whether XGBoost's additional complexity is justified. On real mobile money data with genuine non-
linear feature interactions, the performance gap between linear and non-linear models may be larger.

Sixth, the engineered composite features (transaction intensity, savings commitment ratio, airtime stability) 
provided no measurable improvement over the 16 raw features in the ablation study (ΔAUC = -0.0002). 
While these features have sound theoretical motivation, their practical value on this synthetic dataset is 
negligible. Validation on real data is required to determine whether the engineering decisions add value in 
practice.

Seventh, the paper assumes that SHAP explanations reliably represent model behavior. Recent work has 
demonstrated that post-hoc explanation methods including SHAP can be manipulated to conceal systematic 
bias  while  producing  plausible-looking  explanations  (Slack  et  al.,  2020).  This  adversarial  vulnerability 
means SHAP explanations should be treated as decision-support tools subject to auditing rather than as 
definitive proofs of model behavior.

Eighth, while TreeExplainer provides exact Shapley values relative to the tree ensemble's output, it assumes 
feature independence when computing conditional expectations. In the presence of correlated features — 
such as the savings-related features identified in Figure 3 SHAP values may distribute credit erroneously 
across correlated predictors, potentially misrepresenting individual feature contributions (Lundberg et al., 
2020; Kumar et al., 2020).

9.3 Future work

Several  extensions  would  strengthen  this  research.  First,  partnership  with  a  microfinance  institution  or 
mobile  money  operator  to  validate  the  framework  on  real  transaction  data  would  address  the  most 
significant  limitation.  Second,  longitudinal  analysis  incorporating  time-series  features  from  transaction 
histories  could  substantially  improve  predictive  performance.  Third,  comparison  with  causal  inference 
approaches  to  credit  scoring  addressing  the  confounding  between  behavioral  features  and  unobserved 
creditworthiness represents a theoretically important extension. Fourth, the fairness framework could be 
extended to incorporate counterfactual fairness (Kusner et al., 2017), which provides stronger guarantees

FairLend-Africa  |  Ibraheem Olabintan  |  KSUSTA  |  Page 21

---

<!-- PAGE 22 -->

than  the  statistical  parity  criteria  evaluated  here.  Fifth,  implementing  conditional  expectation  SHAP 
frameworks  to  mitigate  feature  dependency  errors  would  improve  individual  explanation  reliability  on 
correlated  feature sets.  Sixth,  incorporating  adversarial  robustness  evaluation for  SHAP  explanations  to 
detect  potential  manipulation  of  post-hoc  explanations  (Slack  et al.,  2020)    and  developing  explanation 
methods resistant to such attacks represents an important direction for ensuring trustworthy credit decisions 
in high-stakes deployment contexts.

10. Conclusion

This paper presented FairLend-Africa, an explainable machine learning framework for alternative credit 
scoring  using  behavioral  financial  data.  The  system  combines  XGBoost-based  prediction,  SHAP-based 
individual explanation, and systematic fairness auditing in a deployable architecture accessible to resource-
constrained institutions. On a synthetically generated dataset reflecting African mobile money behavioral 
patterns,  the  framework  achieves  a  ROC-AUC  of  0.7137,  satisfies  demographic  parity  and  equal 
opportunity criteria across all evaluated subgroups, and provides individual-level explanations identifying 
wallet balance trend and savings consistency as the dominant creditworthiness signals under the synthetic 
data generating process. Comparison with a logistic regression baseline and feature ablation study reveal 
that the behavioral features exhibit primarily linear structure on synthetic data, motivating validation on 
real mobile money transaction data where non-linear interactions and genuine demographic correlations are 
expected to emerge.

The contribution of this work is methodological rather than empirical: we demonstrate that the combination 
of  alternative  behavioral  data,  gradient  boosted  trees,  post-hoc  explainability,  and  structured  fairness 
auditing  can  be  implemented  as  a  coherent,  reproducible,  and  deployable  system  within  the  resource 
constraints of independent research. Validation on real mobile money data from African lending institutions 
represents the critical next step toward practical application.

The complete codebase, dataset generation scripts, trained model artifacts, and experimental notebooks are 
available at: https://github.com/highfrezh/fairlend-africa

Appendix

Table A1: Optimized XGBoost hyperparameters

Hyperparameter

learning_rate

max_depth 
n_estimators

subsample

colsample_bytree

min_child_weight

scale_pos_weight

References

Value

0.05

4 
250

0.8

0.7

5

3.1

Agarwal, S., Amromin, G., Ben-David, I., Chomsisengphet, S., and Evanoff, D. D. (2020). Fintech and 
household finance. Review of Financial Studies, 33(11), 5085–5126.

FairLend-Africa  |  Ibraheem Olabintan  |  KSUSTA  |  Page 22

---

<!-- PAGE 23 -->

Baesens,  B.,  Van  Gestel,  T.,  Viaene,  S.,  Stepanova,  M.,  Suykens,  J.,  and  Vanthienen,  J.  (2003). 
Benchmarking  state-of-the-art  classification  algorithms  for  credit  scoring.  Journal  of  the  Operational 
Research Society, 54(6), 627–635.

Barocas,  S.  and  Hardt,  M.  (2017).  Fairness  in  machine  learning.  NeurIPS  Tutorial.  Available  at: 
https://fairmlbook.org

Biecek,  P.  and  Burzykowski,  T.  (2021).  Explanatory  Model  Analysis:  Explore,  Explain  and  Examine 
Predictive Models.

Björkegren, D. and Grissen, D. (2018). Behavior revealed in mobile phone usage predicts loan repayment. 
The World Bank Economic Review, 34(3), 618–634.

Blattner,  L. and  Nelson,  S.  (2021).  How  Costly  is  Noise?  Data  and  Disparate  Algorithms  in  Consumer 
Credit. arXiv preprint arXiv:2105.07554.

Chen, T. and Guestrin, C. (2016). XGBoost: A scalable tree boosting system. In Proceedings of the 22nd 
ACM SIGKDD International Conference on Knowledge Discovery and Data Mining, 785–794.

Chiteli, N. (2013). Agent banking operations as a competitive strategy of commercial banks in Kisumu 
City, Kenya. International Journal of Business and Social Science, 4(13).

Chouldechova, A. (2017). Fair prediction with disparate impact: A study of bias in recidivism prediction 
instruments. Big Data, 5(2), 153–163.

Corbett-Davies, S., Pierson, E., Feller, A., Goel, S., and Huq, A. (2017). Algorithmic decision making and 
the cost of fairness. In Proceedings of the 23rd ACM SIGKDD International Conference on Knowledge 
Discovery and Data Mining, 797–806.

Demirgüç-Kunt,  A.,  Klapper,  L.,  Singer,  D.,  and  Ansar,  S.  (2022).  The  Global  Findex  Database  2021. 
World Bank Publications.

Dwork,  C.,  Hardt,  M.,  Pitassi,  T.,  Reingold,  O.,  and  Zemel,  R.  (2012).  Fairness  through  awareness.  In 
Proceedings of the 3rd Innovations in Theoretical Computer Science Conference, 214–226.

Fuster,  A.,  Goldsmith-Pinkham,  P.,  Ramadorai,  T.,  and  Walther,  A.  (2022).  Predictably  unequal?  The 
effects of machine learning on credit markets. Journal of Finance, 77(1), 5–47.

Greenleaf, G. (2021). Global Data Privacy Laws 2021: Authoritarian Backlight on Progress. International 
Data Privacy Law, 11(1), 24–45.

GSMA (2023). The State of Mobile Money in Sub-Saharan Africa. GSMA Research Report.

Hardt, M., Price, E., and Srebro, N. (2016). Equality of opportunity in supervised learning. In Advances in 
Neural Information Processing Systems, 29.

Jordon, J., Szpruch, L., Houssiau, F., Bottarelli, M., Cherubin, G., Maple, C., Cohen, S. N., and Weller, A. 
(2022). Synthetic data  what, why and how? arXiv preprint arXiv:2205.03257.

Khandani, A. E., Kim, A. J., and Lo, A. W. (2010). Consumer credit-risk  models via machine-learning 
algorithms. Journal of Banking and Finance, 34(11), 2767–2787.

Kozodoi, N., Jacob, J., and Lessmann, S. (2022). Fairness in credit scoring: Assessment, implementation 
and profit implications. European Journal of Operational Research, 297(2), 722–737.

FairLend-Africa  |  Ibraheem Olabintan  |  KSUSTA  |  Page 23

---

<!-- PAGE 24 -->

Kumar, I. E., Venkatasubramanian, S., Gupta, A., and Friedler, S. (2020). Problems with Shapley-value-
based explanations as feature importance measures. In Proceedings of the 2020 International Conference 
on Fairness, Accountability, and Transparency (ICFAIR), 430–437.

Kusner, M. J., Loftus, J., Russell, C., and Silva, R. (2017). Counterfactual fairness. In Advances in Neural 
Information Processing Systems, 30.

Lauer,  K.  and  Lyman,  T.  (2015).  Digital  financial  inclusion:  Implications  for  customers,  regulators, 
supervisors, and standard-setting bodies. CGAP Technical Guide.

Ledgerwood, J. (1999). Microfinance Handbook: An Institutional and Financial Perspective. World Bank 
Publications.

Lundberg, S. M. and Lee, S. I. (2017). A unified approach to interpreting model predictions. In Advances 
in Neural Information Processing Systems, 30.

Lundberg, S. M., Erion, G., Chen, H., DeGrave, A., Prutkin, J. M.,

Nair, B., Katz, R., Himmelfarb, J., Bansal, N., and Lee, S. I. (2020). From local explanations to global 
understanding with

explainable AI for trees. Nature Machine Intelligence, 2(1), 56–67.

Niculescu-Mizil, A. and Caruana, R. (2005). Predicting good probabilities with supervised learning. In

Proceedings of the 22nd International Conference on Machine Learning, 625–632.

Pedregosa, F., Varoquaux, G., Gramfort, A., Michel, V., Thirion, B., Grisel, O., and others (2011). Scikit-
learn: Machine learning in Python. Journal of Machine Learning Research, 12, 2825–2830.

Ribeiro, M. T., Singh, S., and Guestrin, C. (2016). "Why should I trust you?": Explaining the predictions 
of any classifier. In Proceedings of the 22nd ACM SIGKDD International Conference, 1135–1144.

Slack, D., Hilgard, S., Jia, E., Singh, S., and Lakkaraju, H. (2020). Fooling LIME and SHAP: Adversarial 
attacks on post hoc explanation methods. In Proceedings of the AAAI Conference on Human Computation, 
8(1), 180–186.

Suri,  T.  and  Jack,  W.  (2016).  The  long-run  poverty  and  gender  impacts  of  mobile  money.  Science, 
354(6317), 1288–1292.

Totolo, E. (2018). Kenya's Digital Credit Revolution: Five Years On. FSD Kenya Technical Note.

van Buuren, S. (2018). Flexible Imputation of Missing Data. CRC Press. Available at: https://ema.drwhy.ai

Zhang, Y. and Long, J. (2021). Fairness-aware learning with missing attributes. In Proceedings of the 2021 
AAAI Conference on Human Computation and Crowdsourcing (HCOMP), 154–162.

FairLend-Africa  |  Ibraheem Olabintan  |  KSUSTA  |  Page 24

<!-- MARKITDOWN CONVERSION -->

<!-- Full MarkItDown conversion for formatting fidelity. -->

FairLend-Africa: An Explainable Machine Learning
Framework for Alternative Credit Scoring Using
Behavioral Financial Data in Financially Excluded
African Communities
Ibraheem Olabintan
Kebbi State University of Science and Technology
Aliero, Kebbi State, Nigeria
Abstract:
Access to formal credit remains constrained for much of the African population due to a lack of
conventional credit histories. This paper investigates whether behavioral financial data mobile
money transactions, airtime patterns, and savings consistency can serve as valid proxies for
creditworthiness. We present FairLend-Africa, an explainable machine learning framework
combining XGBoost scoring with SHAP interpretability and systematic fairness auditing. Using a
synthetic dataset of 10,000 borrower records, the system achieves a held-out test ROC-AUC of
0.7137, which aligns with performance baselines established in thin-file behavioral credit scoring
literature. Within the controlled synthetic data generation boundaries, the audit pipeline
demonstrates no disparity under the synthetic data's demographic-behavioral independence
assumption a condition requiring empirical verification with real data before deployment claims
can be made. SHAP analysis identifies wallet balance trend and savings consistency as dominant
signals. A logistic regression baseline matches the XGBoost performance, suggesting primarily
linear structures in the synthetic data and motivating validation on real-world datasets where non-
linear interactions may emerge. The system is implemented as a REST API with an interactive
dashboard released as open source to support reproducibility in African financial inclusion
research.
Keywords: alternative credit scoring, explainable artificial intelligence, financial inclusion,
mobile money, SHAP, XGBoost, fairness in machine learning, African fintech
1. Introduction
Approximately 1.4 billion adults worldwide remain unbanked, with Sub-Saharan Africa accounting for a
disproportionate share of this population (Demirgüç-Kunt et al., 2022). Among the structural barriers to
financial inclusion, the absence of formal credit history represents one of the most consequential.
Conventional credit scoring systems whether bureau-based or institution-internal rely on records of prior
formal borrowing, repayment behavior, and account standing. For individuals who have never held a formal
bank account, these systems produce either a null score or a rejection by default, regardless of actual
financial behavior or repayment capacity.
The proliferation of mobile money services across Africa has created an alternative source of financial
behavioral data. Mobile money systems such as M-Pesa in Kenya and MTN Mobile Money across West
Africa generate transaction records that digital lenders ingest via distinct modalities: either direct bank-
telco utility integrations (e.g., M-Shwari) or client-side smartphone scraper APIs parsing local SMS
notification receipts (e.g., Tala, Branch, Carbon) (GSMA, 2023) that capture income frequency,
expenditure patterns, savings behavior, and network activity. Prior research has demonstrated that such
FairLend-Africa | Ibraheem Olabintan | KSUSTA | Page 1

behavioral signals carry meaningful predictive information about creditworthiness (Björkegren and
Grissen, 2018; Suri and Jack, 2016), yet their integration into formal credit assessment frameworks remains
limited, particularly in contexts where explainability and fairness are simultaneously required.
For clarity, we distinguish what this paper contributes from what it does not. This paper contributes: a
framework design for behavioral credit scoring with explainability and fairness auditing; an evaluation
protocol applicable to any binary credit classification problem; and an open-source implementation
lowering barriers for MFI experimentation. This paper does not contribute: empirical claims about African
borrower behavior; fairness guarantees for real lending systems; or performance benchmarks generalizable
beyond the synthetic data generating process.
This paper makes three contributions. First, we propose and implement a feature engineering methodology
that constructs interpretable behavioral credit signals from mobile money transaction data, airtime recharge
patterns, savings behavior, and loan history. Second, we demonstrate that an XGBoost classifier trained on
these features achieves a ROC-AUC of 0.7137, a result consistent with the difficulty of behavioral credit
scoring tasks and with results reported in comparable literature. Third, we conduct a systematic fairness
audit using three criteria from the algorithmic fairness literature demographic parity, equal opportunity, and
predictive parity and find no meaningful disparities across regional and gender subgroups. Throughout,
SHAP values provide individual-level explanations that render the model's decisions interpretable to non-
technical stakeholders such as loan officers and borrowers.
We note an important scope boundary: this paper is a methodological demonstration rather than an
empirical study of real African borrower behavior. All results predictive performance, feature importance
rankings, and fairness audit outcomes are properties of the synthetic data generating process and the
proposed framework applied to it. We make no claims about how these results would generalize to real
mobile money data, and we present the framework explicitly as infrastructure for future empirical work
rather than as evidence of real-world credit scoring capability. This framing follows the precedent of
simulation-based methodology papers in applied ML research, where the contribution is the framework
design and evaluation protocol rather than empirical claims about a specific population (Biecek and
Burzykowski, 2021).
The remainder of this paper is organized as follows. Section 2 reviews relevant literature. Section 3 defines
the problem formally. Section 4 describes the synthetic dataset and its design rationale. Section 5 presents
the feature engineering methodology. Section 6 describes the system architecture. Section 7 presents
experimental results. Section 8 reports the fairness analysis. Section 9 discusses implications and
limitations. Section 10 concludes.
2. Literature Review
2.1 Financial exclusion and credit access in Africa
Financial exclusion in Sub-Saharan Africa is structurally rooted in infrastructure gaps, documentation
barriers, and the dominance of informal economic activity (Chiteli, 2013). Ledgerwood (1999) documented
how microfinance institutions (MFIs) attempted to bridge this gap through group lending and social
collateral mechanisms, with repayment rates frequently exceeding 80 percent in well-managed
programmes. More recently, Totolo (2018) documented how Kenya's digital credit revolution shifted the
paradigm toward high-frequency, automated credit assessment, albeit with new risks regarding digital
delinquiry and debt stress among previously unscored populations.
FairLend-Africa | Ibraheem Olabintan | KSUSTA | Page 2

2.2 Alternative data in credit scoring
The use of alternative data sources in credit scoring has been studied across multiple contexts. Khandani et
al. (2010) demonstrated that consumer transaction data from retail banking systems could produce credit
scores with AUC values competitive with bureau-based models. Björkegren and Grissen (2018) used
mobile phone metadata including call records and recharge patterns to predict loan repayment among
borrowers in Rwanda, reporting AUC values of approximately 0.70, and found that behavioral features
captured creditworthiness signals invisible to conventional scoring. Agarwal et al. (2020) examined fintech
lending in India and found that alternative data improved inclusion for thin-file borrowers without
degrading portfolio quality.
In the African context specifically, Suri and Jack (2016) documented the welfare effects of M-Pesa adoption
in Kenya, showing that mobile money enabled households particularly female-headed households to better
navigate income shocks through social network transfers. While their study did not directly measure credit
repayment capacity, the demonstrated link between mobile money usage and financial resilience provides
theoretical grounding for behavioral transaction data as a creditworthiness proxy. Lauer and Lyman (2015)
reviewed digital financial inclusion initiatives across low-income markets and identified transaction
frequency and regularity as the most actionable behavioral signals for credit assessment.
2.3 Machine learning in credit scoring
Machine learning methods have been applied extensively to credit scoring since the foundational work of
Baesens et al. (2003), who compared neural networks, support vector machines, and logistic regression
across multiple credit datasets and found that ensemble methods generally outperformed single classifiers.
XGBoost (Chen and Guestrin, 2016) has become a standard baseline in credit scoring competitions and
applied research due to its strong performance on tabular data, resistance to overfitting through
regularization, and compatibility with post-hoc explainability methods.
2.4 Explainability in credit decisions
The requirement for explainability in credit decisions is both regulatory and ethical. The European Union's
General Data Protection Regulation (GDPR) Article 22 establishes a right to explanation for automated
decisions, and equivalent frameworks are emerging in several African jurisdictions. Lundberg and Lee
(2017) introduced SHAP as a unified framework for model explanation grounded in cooperative game
theory. Unlike earlier feature importance measures, SHAP values satisfy desirable axioms including local
accuracy, missingness, and consistency, making them appropriate for credit decision explanation (Lundberg
et al., 2020). Ribeiro et al. (2016) proposed LIME as an alternative local explanation method, but SHAP
has demonstrated superior stability and theoretical grounding for tree-based models. However, recent work
has demonstrated that post-hoc explanation methods can be manipulated to conceal systematic bias (Slack
et al., 2020); this adversarial vulnerability is discussed as a limitation in Section 9.2.
2.5 Fairness in algorithmic credit scoring
Algorithmic fairness in lending has received substantial research attention following evidence that machine
learning models can perpetuate or amplify historical discrimination (Barocas and Hardt, 2017).
Chouldechova (2017) demonstrated the impossibility theorem: no classifier can simultaneously satisfy
sufficiency (calibration/predictive parity) and separation (equalized error rates across groups) when base
rates differ across groups. This necessitates explicit fairness criterion selection rather than the assumption
that fairness can be comprehensively achieved. Fuster et al. (2022) examined fintech lending algorithms
FairLend-Africa | Ibraheem Olabintan | KSUSTA | Page 3

and found that while they improved access for some minority groups, behavioral proxies could encode
demographic information through indirect pathways. Our analysis explicitly tests for such proxy
relationships. Kozodoi et al. (2022) provided a business-oriented framework mapping predictive
performance trade-offs directly to credit scoring models, demonstrating that fairness constraints impose
measurable costs on model profitability a tension directly relevant to microfinance deployment contexts.
Recent work has further shown that alternative behavioral features including the mobile money signals used
in this study can act as proxies for socioeconomic stratification, potentially exacerbating geographic
discrimination under the guise of neutral algorithmic scoring (Blattner and Nelson, 2021).
3. Problem Statement
Let D = {( 𝑥 ,𝑑 ,𝑦 )}𝑛 denoted a dataset of n borrowers, where 𝑥 ∈ 𝑅𝑝 is a vector of p behavioral
𝑖 𝑖 𝑖 𝑖=1 𝑖
financial features, 𝑑 is a vector of demographic attributes, and 𝑦 ∈ {0,1} is a binary repayment label (1 =
𝑖 𝑖
repaid, 0 = defaulted).
We seek a classifier 𝑓: 𝑅𝑝 →[0,1] that:
1. Predicts accurately: maximize ROC-AUC on held-out data, using only 𝑥 (𝑛𝑜𝑡 𝑑 ) as input
𝑖 𝑖
features.
2. Explains locally: for only borrower 𝑥 produces SHAP explanation vector ∅ ∈ 𝑅𝑝 satisfying
𝑖 𝑖
𝑓(𝑥 ) = ∅ + ∑𝑝 ∅ , where ∅ is the base rate and ∅ is the contribution of feature 𝑗. We
𝑖 0 𝑗=1 𝑖𝑗 0 𝑖𝑗
acknowledge that while SHAP provides exact explanations for tree models, it assumes feature
independence when computing conditional expectations a mathematical vulnerability we address
as a limitation in Section 9.2 (kumar et al., 2020).
3. Satisfies fairness criteria: for demographic subgroups defined by 𝑑 , produces selection rates, true
𝑖
positive rates, and precision values with disparity ratios exceeding 0.80 across all groups.
The exclusion of 𝑑 from model inputs is a design choice grounded in fair lending principles. The retention
𝑖
of 𝑑 in the dataset serves only the post-hoc fairness audit.
𝑖
4. Dataset Design
4.1 Motivation for synthetic data
The use of real mobile money transaction data for research purposes faces substantial barriers: data access
requires institutional partnerships with telecom operators or MFIs, raises privacy concerns under emerging
African data protection frameworks including the Kenya Data Protection Act (2019) and the Nigeria Data
Protection Act (2023) which restrict the processing of consumer transaction records without explicit consent
(Greenleaf, 2021), and introduces selection biases from the specific institution's customer base. We
therefore adopt a synthetic data generation approach, which allows full transparency of the data generating
process, enables reproducibility without data sharing agreements, and permits deliberate design of feature
relationships grounded in literature.
This approach is consistent with established practice in privacy-sensitive ML research (Jordon et al., 2022)
and with similar methodological choices in alternative credit scoring studies where real data could not be
shared (Khandani et al., 2010).
4.2 Feature design rationale
FairLend-Africa | Ibraheem Olabintan | KSUSTA | Page 4

Table 1 presents the 16 raw behavioral features included in the dataset, organized by source domain. Figure
1 illustrates the bivariate distributions of key features by repayment outcome.
Table 1: Raw behavioral features
Feature Domain Behavioral rationale
monthly_txn_count Mobile money Transaction frequency proxies income regularity
avg_txn_amount_usd Mobile money Average value proxies income level
wallet_balance_trend Mobile money Growing balance signals financial surplus
airtime_recharge_freq Airtime Recharge frequency signals liquidity
airtime_avg_amount_usd Airtime Larger recharges signal stable cash flow
has_savings_account Savings Account ownership signals planning behavior
savings_consistency_score Savings Regular saving signals financial discipline
monthly_savings_usd Savings Savings volume signals surplus capacity
has_prior_loan Credit history Prior borrowing signals credit experience
prior_loan_repayment_rate Credit history Repayment rate is direct creditworthiness signal
days_late_avg Credit history Late payments signal repayment stress
network_diversity_score Social Counterparty diversity signals economic integration
bill_payment_regularity Payments Regular bills signal stable income and obligations
merchant_payment_count Payments Merchant activity signals economic participation
loan_amount_requested_usd Loan request Loan size relative to behavioral capacity
loan_duration_weeks Loan request Loan term as risk exposure measure
Figure 1. Feature distributions by repayment outcome. Overlapping histograms show visible separation
between repayers (green) and defaulters (red) across key behavioral features, confirming predictive signal
in the dataset.
FairLend-Africa | Ibraheem Olabintan | KSUSTA | Page 5

4.3 Label generation
The binary repayment label is generated via a logistic data generating process with coefficients calibrated
to reflect the hypothesized behavioral creditworthiness relationships:
The complete coefficient vector used in the data generating process is provided in Table 2 for full
reproducibility. The resulting class distribution of the generated labels is shown in Figure 2.
Table 2: Data generating process coefficients
| Feature                                 | Coefficient (β)  | Direction  |
| --------------------------------------- | ---------------- | ---------- |
| Intercept                               | 0.0              | —          |
| wallet_balance_trend                    | +0.8             | Positive   |
| monthly_txn_count (normalized)          | +0.5             | Positive   |
| savings_consistency_score (normalized)  | +0.6             | Positive   |
| has_savings_account                     | +0.7             | Positive   |
| airtime_recharge_freq (normalized)      | +0.4             | Positive   |
| prior_loan_repayment_rate               | +0.9             | Positive   |
| days_late_avg (normalized)              | -0.6             | Negative   |
| bill_payment_regularity (normalized)    | +0.3             | Positive   |
| network_diversity_score (normalized)    | +0.2             | Positive   |
| loan_amount_requested_usd (normalized)  | -0.4             | Negative   |
| Noise term ε                            | σ=0.3            | —          |

Note: All normalized features were Z-scored before applying coefficients; the intercept of 0 yields a base
repayment  probability  of 0.50  before the  logistic  transform.  Binary features  (has_savings_account,
has_prior_loan) were not normalized. The noise term ε ~ N(0, 0.3) was added to the log-odds before
applying the sigmoid. Complete generation code is available in `src/data/generate_dataset.py` in the
project repository.

Figure 2. Class distribution of the repayment label. The dataset contains 7,553 repayers (75.53%) and
2,447 defaulters (24.47%), consistent with repayment rates reported in African microfinance literature
(Ledgerwood, 1999).

FairLend-Africa  |  Ibraheem Olabintan  |  KSUSTA  |  Page 6

4.4 Missing data
Features derived from prior loan history (“prior_loan_repayment_rate”, “days_late_avg”) are missing for
5,503 borrowers (55.03 percent) who have no prior loan history. This missingness is Missing Not At
Random (MNAR): the absence of a value is itself informative, indicating a first-time borrower. This
characteristic reflects a genuine challenge in alternative credit scoring for financially excluded populations.
Missing values are handled via median imputation within the sklearn pipeline after train/test splitting,
ensuring no information leakage from the test set. We acknowledge that median imputation assumes
Missing At Random (MAR), which is technically inconsistent with the MNAR mechanism identified here.
A more rigorous approach would employ multiple imputation with chained equations (van Buuren, 2018)
or pattern mixture models. However, the addition of the binary missingness indicator
(“no_prior_loan_flag”) partially compensates by preserving the structural information in the missingness
pattern. We identify this as a methodological limitation. Median imputation on MNAR data likely biases
coefficient estimates toward zero, attenuating the predictive contribution of prior loan history features. We
retain median imputation as a practical deployment compromise it is implementable in a single sklearn
pipeline step without external dependencies but explicitly recommend multiple imputation with chained
equations (MICE) for any research application where statistical validity of coefficient estimates matters.
4.5 Dataset statistics
The final dataset contains 10,000 records, 20 model features (16 raw + 4 engineered), 4 demographic
attributes retained for fairness auditing, and a binary repayment label. The dataset and generation code are
released in the project repository.
5. Feature Engineering
Beyond the 16 raw behavioral features, three composite features were engineered to capture higher-order
behavioral signals:
Transaction intensity (𝑡𝑥𝑛 𝑖𝑛𝑡𝑒𝑛𝑠𝑖𝑡𝑦): defined as log( 1+𝑚𝑜𝑛𝑡ℎ𝑙𝑦𝑡𝑥𝑛_𝑐𝑜𝑢𝑛𝑡 ) ×log(1+
− _
𝑎𝑣𝑔_𝑡𝑥𝑛 _𝑎𝑚𝑜𝑢𝑛𝑡_𝑢𝑠𝑑 ) . This multiplicative interaction captures the joint signal of frequency and value,
distinguishing high-volume low-value activity from moderate-volume higher-value activity two distinct
behavioral profiles in mobile money literature (Björkegren and Grissen, 2018).
Savings commitment ratio (𝑠𝑎𝑣𝑖𝑛𝑔𝑠_𝑐𝑜𝑚𝑚𝑖𝑡𝑚𝑒𝑛𝑡_𝑟𝑎𝑡𝑖𝑜): defined as 𝑚𝑜𝑛𝑡ℎ𝑙𝑦_𝑠𝑎𝑣𝑖𝑛𝑔𝑠_𝑢𝑠𝑑 /
(𝑎𝑣𝑔_𝑡𝑥𝑛_𝑎𝑚𝑜𝑢𝑛𝑡_𝑢𝑠𝑑 + 1 ) . This ratio normalizes savings volume by transaction activity, capturing
whether a borrower actively sets money aside relative to their financial throughput, a behavioral signal of
forward planning. We anticipate that these engineered interactions may exhibit negligible predictive lift on
synthetic data relative to raw behavioral features (see Section 9.2).
Airtime stability (𝑎𝑖𝑟𝑡𝑖𝑚𝑒_𝑠𝑡𝑎𝑏𝑖𝑙𝑖𝑡𝑦 ): defined as 𝑎𝑖𝑟𝑡𝑖𝑚𝑒_𝑎𝑣𝑔_𝑎𝑚𝑜𝑢𝑛𝑡 /
(𝑎𝑖𝑟𝑡𝑖𝑚𝑒_𝑟𝑒𝑐ℎ𝑎𝑟𝑔𝑒_𝑓𝑟𝑒𝑞 +1 ). Frequent small recharges have been identified as a mobile money stress
signal (Lauer and Lyman, 2015); a higher stability ratio indicates fewer, larger recharges consistent with
stable cash flow.
A binary missingness indicator (`no_prior_loan_flag`) was added as the fourth engineered feature, as
described in Section 4.4.
Figure 3 presents the Pearson correlation matrix across all features.
FairLend-Africa | Ibraheem Olabintan | KSUSTA | Page 7

Figure 3. Pearson correlation matrix across all features and the repayment label. Moderate inter-feature
correlations among savings features are expected and do not constitute problematic multicollinearity.
6. System Architecture
FairLend-Africa is implemented as a three-tier system:
Data and model tier: Python-based ML pipeline using scikit-learn (Pedregosa et al., 2011) for
preprocessing and XGBoost (Chen and Guestrin, 2016) for classification. SHAP (Lundberg and Lee, 2017)
provides post-hoc explanations. All artifacts are serialized using joblib and versioned in the repository.
API tier: FastAPI application exposing three endpoints: `POST /api/v1/predict` returns a credit decision
and score for a given borrower; `POST /api/v1/explain` returns the prediction with full SHAP
decomposition; `GET /api/v1/evaluate` returns cached model performance metrics. Prediction requests are
logged to a PostgreSQL database for audit purposes.
Presentation tier: React dashboard with three views: borrower input form, credit decision display with
SHAP bar chart visualization, and model metrics panel. The dashboard is designed for loan officer use the
SHAP chart presents the top contributing features in plain language alongside their directional effect on the
credit decision.
FairLend-Africa | Ibraheem Olabintan | KSUSTA | Page 8

The system does not include mechanisms for monitoring model performance drift over time. Credit scoring
models are subject to concept drift as economic conditions and borrower behavior evolve; temporal stability
evaluation is identified as a limitation in Section 9.2 and recommended before any production deployment.
The system is deployable on free-tier cloud infrastructure (Render or Railway for the API, Vercel for the
frontend) without requiring institutional cloud resources, consistent with the accessibility goals of the
research.
7. Experiments and Results
7.1 Experimental setup
The dataset was split into 80 percent training (8,000 records) and 20 percent test (2,000 records) using
stratified sampling to preserve the class ratio. The ML pipeline consists of median imputation, standard
scaling, and an XGBoost classifier. Hyperparameter optimization was performed via
RandomizedSearchCV over 30 iterations with 5-fold stratified cross-validation, optimizing for ROC-AUC.
The final optimized parameters are listed in Table A1 in the Appendix.
7.2 Model performance
Table 3 presents evaluation results across three model configurations on the held-out test set.
Table 3: Model comparison test set performance (95% bootstrap CI, n=1000)
Configuration Accuracy Precision Recall F1 ROC-AUC Threshold
Majority class 0.755 — — — 0.500 —
baseline
Logistic Regression 0.760 0.770 0.960 0.860 0.713 0.5
[0.688,
0.738]
Baseline XGBoost 0.664 0.824 0.706 0.760 0.675 0.5
Tuned XGBoost 0.620 0.862 [0.841, 0.600 [0.574, 0.707 0.714 0.151
0.883] 0.625] [0.686, [0.688,
0.727] 0.739]
Note: Confidence intervals for logistic regression precision, recall, and F1 are omitted for brevity;
bootstrap estimation confirmed they are similar in width to the tuned XGBoost intervals reported above.
Table 3 includes a logistic regression baseline trained on the same feature set and pipeline. Logistic
regression achieves substantially higher recall (0.960) than the baseline XGBoost (0.706) at the same
classification threshold of 0.5, reflecting differences in probability estimation between model classes
uncalibrated tree-based ensembles often generate biased probability distributions compared to generalized
linear models, though calibration quality depends on the degree of model misspecification in both cases
(Niculescu-Mizil and Caruana, 2005). We emphasize that these distortions are typical of tree-based models
on tabular layouts; mapping these parameters onto actual, non-stationary mobile wallets remains an open
empirical challenge. Both models were evaluated without additional calibration to preserve comparability
with the threshold analysis. The logistic regression achieves a ROC-AUC of 0.713 compared to 0.714 for
the tuned XGBoost a difference of 0.001, which is within the bootstrap confidence interval width of both
models and should not be interpreted as meaningful. This finding suggests that the behavioral features in
this synthetic dataset exhibit primarily linear relationships with the repayment label, and that XGBoost's
capacity for non-linear interaction modelling provides no measurable benefit over logistic regression under
FairLend-Africa | Ibraheem Olabintan | KSUSTA | Page 9

these conditions. This finding is notable given that Baesens et al. (2003) found that advanced classifiers
outperformed logistic regression across multiple real-world credit datasets, suggesting that the near-
identical performance observed here is a property of the linear synthetic data generating process rather than
a general characteristic of credit scoring tasks. We retain XGBoost as the primary model for this framework
demonstration for two reasons. First, the SHAP TreeExplainer provides exact Shapley values for tree-based
models rather than the kernel approximations required for linear models, making the explainability analysis
in Section 7.3 more theoretically rigorous. Second, real mobile money data is expected to exhibit non-linear
feature interactions that XGBoost would capture but logistic regression would not making XGBoost the
more appropriate demonstration vehicle for the framework's intended real-world application. However, we
note that for practitioners deploying on current synthetic-equivalent data, logistic regression offers
comparable discrimination (AUC 0.713) with inherent coefficient interpretability and lower computational
cost. The framework is compatible with either model class.
The tuned model achieves a ROC-AUC of 0.7137, representing a 5.7 percent relative improvement over
the baseline. This result is consistent with alternative credit scoring studies using behavioral data:
Björkegren and Grissen (2018) report AUC values of approximately 0.70 using mobile phone metadata,
and Khandani et al. (2010) report AUC values of 0.68–0.72 using consumer transaction logs from a
traditional commercial bank in North America. This demonstrates that while alternative transactional
signals yield a broadly comparable mathematical baseline across disparate market structures, the underlying
socioeconomic data-generating dynamics remain fundamentally distinct. Under the synthetic data
generating process, behavioral alternative features carry sufficient predictive signal to demonstrate the
framework's discrimination capacity. Whether this generalizes to real mobile money data remains an open
empirical question.
The optimal classification threshold identified via precision-recall curve analysis is 0.151, substantially
below the conventional 0.5 default. This reflects the cost asymmetry of the lending context: misclassifying
a defaulter as creditworthy carries greater institutional cost than rejecting a creditworthy borrower (Baesens
et al., 2003; Kozodoi et al., 2022). We present all three configurations to support transparent reporting of
this tradeoff rather than selectively reporting the configuration with the highest single metric. F1
optimization implicitly assumes equal costs for false positives and false negatives. In practice, microfinance
lenders typically assign higher cost to false negatives (approving a defaulter) than false positives (rejecting
a creditworthy borrower), with cost ratios ranging from 2:1 to 5:1 depending on loan size and institutional
context (Baesens et al., 2003). The low optimal threshold of 0.151 reflects the class imbalance correction
applied during tuning rather than an explicit cost-benefit specification. Practitioners should recalibrate this
threshold using institution-specific cost ratios before deployment.
Two aspects of Table 3 require explicit discussion. First, the tuned model achieves lower overall accuracy
(0.620) than the baseline (0.664). This reflects the effect of the low optimal threshold (0.151): the tuned
model classifies nearly all borrowers as repayers, producing a selection rate approaching 1.0 on the test set.
While this maximizes recall for the repayment class, it reduces overall accuracy below the naive majority-
class baseline (0.755). This tradeoff is deliberate given the threshold optimization objective (maximizing
F1 via precision-recall analysis) but would require careful cost-benefit analysis before deployment.
Second, the near-universal selection rate means the fairness analysis which compares selection rates across
demographic groups is evaluating a near-trivial condition. When all borrowers are approved, demographic
parity is automatically satisfied. This is an important limitation of the current threshold setting and is
addressed in the fairness limitations discussion in Section 8.4.
FairLend-Africa | Ibraheem Olabintan | KSUSTA | Page 10

Figure 4. ROC curve on held-out test set (n=2,000). The tuned XGBoost model achieves AUC = 0.7137,
indicating meaningful discrimination ability beyond the random baseline (dashed line).
Figure 5. Confusion matrix on held-out test set. Rows represent actual labels; columns represent predicted
labels.
FairLend-Africa | Ibraheem Olabintan | KSUSTA | Page 11

Figure 6. Performance comparison across three model configurations on the held-out test set.

7.3 SHAP feature importance
Table 4 presents the five highest-impact features ranked by mean absolute SHAP value across all 2,000 test
borrowers. The five most impactful features are visualized in Figure 7 (Global Importance), Figure 8
(Beeswarm Summary), and Figure 9 (Dependence Plots):
Table 4: Top 5 features by mean absolute SHAP value
| Feature  | Mean | SHAP | (log-odds)  | Interpretation  |
| -------- | ------------------------- | --------------- |
wallet_balance_trend  0.3767  Primary creditworthiness signal
savings_consistency_score  0.2162  Financial discipline indicator
| monthly_savings_usd  | 0.1255  | Savings capacity indicator     |
| -------------------- | ------- | ------------------------------ |
| has_savings_account  | 0.0554  | Financial planning indicator   |
| txn_intensity        | 0.0348  | Engineered transaction signal  |

SHAP values are expressed in log-odds space, reflecting the XGBoost model's raw output before the
sigmoid transformation to probability.

FairLend-Africa  |  Ibraheem Olabintan  |  KSUSTA  |  Page 12

Figure 7. Global feature importance measured by mean absolute SHAP value across all 2,000 test
borrowers. Wallet balance trend dominates all other features by a factor of 1.74 times the second-ranked
feature.
“wallet_balance_trend” dominates all other features by a factor of 1.74 times the second-ranked feature,
confirming the theoretical expectation that balance trajectory is the strongest behavioral creditworthiness
signal. Notably, “txn_intensity” an engineered composite feature appears in the top five by mean absolute
SHAP value. However, a feature ablation study comparing the full 20-feature set (ROC-AUC: 0.714)
against the 16 raw features alone (ROC-AUC: 0.714) reveals that the engineered features provide no
measurable improvement in predictive performance on this dataset. We interpret this as evidence that the
raw behavioral features already capture the underlying signals that the composite features were designed to
encode, at least under the linear data generating process used here. The engineered features may provide
greater value on real mobile money data where non-linear interactions are more pronounced. This finding
underscores the importance of ablation studies in feature engineering validation, which are frequently
omitted in applied ML research.
Loan request features (“loan_amount_requested_usd”, “loan_duration_weeks”) rank among the lowest-
importance features, indicating that the model learned to predict repayment primarily from how borrowers
manage money daily rather than from the characteristics of the loan being requested. This is a theoretically
meaningful finding consistent with empirical research on micro-liquidity tracking, where small, consistent
transactional movements serve as a proxy for operational cash-flow stability rather than static asset
thresholds (Lauer and Lyman, 2015).
FairLend-Africa | Ibraheem Olabintan | KSUSTA | Page 13

Figure 8. SHAP beeswarm plot. Each point represents one borrower. Position on the x-axis indicates SHAP
value magnitude and direction. Color encodes feature value (red = high, blue = low). Features are ordered
by mean absolute SHAP value.
FairLend-Africa | Ibraheem Olabintan | KSUSTA | Page 14

Figure 9. SHAP dependence plots for the four highest-importance features. Each point represents one
borrower. The plots reveal the nature of feature-prediction relationships under the synthetic data
generating process; the near-identical performance of logistic regression suggests these relationships are
predominantly linear on this dataset.
7.4 Local explainability
For each borrower, SHAP waterfall plots decompose the prediction into feature-level contributions,
showing how each behavioral signal pushes the probability above or below the model's base rate of 0.64.
Note that this base rate reflects the model's expected value under the SHAP background distribution (the
500-sample training background used for TreeExplainer), which differs from the empirical repayment rate
of 75.53% shown in Figure 2. The SHAP base rate is the model's average prediction on the background
sample, not the dataset's class proportion. Figure 10 illustrates three representative cases: a high-confidence
repayer, a high-confidence defaulter, and a borderline borrower near the decision threshold.
Figure 10a. Local SHAP explanation high-confidence repayer. Green bars indicate features supporting
repayment above the base rate.
FairLend-Africa | Ibraheem Olabintan | KSUSTA | Page 15

Figure 10b. Local SHAP explanation high-confidence defaulter. Red bars indicate features increasing
default risk below the base rate.
Figure 10c. Local SHAP explanation borderline borrower near the decision threshold. Competing positive
and negative contributions illustrate model uncertainty at the margin.
FairLend-Africa | Ibraheem Olabintan | KSUSTA | Page 16

This individual-level transparency is particularly important in the African lending context, where borrowers
may be unfamiliar with algorithmic assessment and where regulatory frameworks increasingly require
explainable credit decisions.
8. Fairness Analysis
8.1 Fairness criteria
We evaluate three criteria from the algorithmic fairness literature:
Demographic parity (Dwork et al., 2012): equal positive prediction rates across groups, assessed via
selection rate disparity ratios.
Equal opportunity (Hardt et al., 2016): equal true positive rates across groups, ensuring that creditworthy
borrowers have equal probability of approval regardless of demographic membership.
Predictive parity: equal precision across groups, ensuring that approved borrowers in each group have
equal likelihood of actually repaying.
We apply the 80 percent rule as a disparity threshold: a disparity ratio below 0.80 is considered a meaningful
fairness violation. In the absence of codified algorithmic parity thresholds within current Sub-Saharan
African financial regulations, we adopt the United States Equal Credit Opportunity Act's 80 percent rule
strictly as an international baseline indicator for methodological demonstration purposes. We acknowledge
that no equivalent threshold has been formally adopted by regional bodies such as the Central Bank of
Nigeria or the Central Bank of Kenya. However, recent compliance interventions such as the Central Bank
of Kenya (Digital Credit Providers) Regulations 2022 signal an escalating regulatory focus on consumer
privacy, algorithmic transparency, and predatory automated underwriting.

8.2 Results
Table 5 presents disparity ratios for regional and gender subgroups.
Table 5: Fairness disparity ratios by demographic group
| Group              | Selection rate  | TPR    | Precision  |
| ------------------ | --------------- | ------ | ---------- |
| West Africa        | 1.000           | 1.000  | 0.990      |
| East Africa        | 1.000           | 1.000  | 0.959      |
| Southern Africa    | 1.000           | 1.000  | 1.000      |
| Central Africa     | 1.000           | 1.000  | 0.989      |
| Female             | 1.000           | 1.000  | 1.000      |
| Male               | 1.000           | 1.000  | 0.977      |
| Prefer not to say  | 1.000           | 1.000  | 0.989      |

All disparity ratios exceed 0.80 across all groups and all criteria. These properties are visualized in Figure
11 (Demographic Parity) and Figure 12 (Equal Opportunity), while Figure 13 confirms equitable predictive
consistency via group-wise ROC-AUC. Demographic parity and equal opportunity are satisfied at 1.000

FairLend-Africa  |  Ibraheem Olabintan  |  KSUSTA  |  Page 17

for every group, indicating that the model approves loans and identifies creditworthy borrowers at equal
rates regardless of regional origin or gender.
We note that the "Prefer not to say" gender category warrants particular caution in real deployment contexts.
Unlike the Male and Female categories, this category conflates actual gender identity with disclosure
behavior individuals who decline to disclose their gender may differ systematically from those who do,
meaning the category may itself encode behavioral or socioeconomic information (e.g., Zhang and Long,
2021). In a real lending system, this category should be treated as a distinct analytical group requiring
separate study rather than as a third gender category. In the synthetic dataset, this category was generated
independently of behavioral features and therefore does not exhibit this confounding.
To assess whether the fairness properties are robust to the choice of operating threshold, we evaluate
disparity ratios at three additional approval rates spanning realistic microfinance lending contexts. Table 6
presents selection rate disparity ratios across regional and gender subgroups at four operating points.
Table 6: Selection rate disparity ratios across operating thresholds
Threshold Approval rate Region disparity Gender disparity Worst group
0.621 30% 0.818 0.932 West Africa
0.509 50% 0.811 0.947 Central Africa
0.433 70% 0.903 0.978 Central Africa
0.151 100% 1.000 1.000 —
All disparity ratios exceed the 0.80 threshold across every operating point evaluated, indicating that the
fairness properties of the framework are robust to threshold selection and are not an artifact of the near-
universal approval rate at the optimal threshold. The most constrained operating point 30% approval
produces the lowest observed disparity ratio of 0.818 (West Africa, regional), which passes the 80% rule
benchmark by a margin of only 0.018. This narrow margin warrants explicit caution: real-world mobile
money data from West Africa may exhibit structural correlations between region and behavioral features
due to infrastructure inequality, historical lending patterns, and urbanization differences. Such correlations
would likely reduce this ratio below the 0.80 threshold, constituting a fairness violation under the same
benchmark. This robustness analysis addresses the concern that single-threshold fairness evaluation may
produce misleading results when the chosen threshold produces extreme selection rates (Corbett-Davies et
al., 2017).
FairLend-Africa | Ibraheem Olabintan | KSUSTA | Page 18

Figure 11. Demographic parity analysis. Selection rates by region (left) and gender (right). All groups
exceed the 80% rule threshold (red dashed line), indicating equal approval rates across subgroups.
Figure 12. Equal opportunity analysis. True positive rates by region (left) and gender (right). All groups
satisfy equal opportunity, confirming that creditworthy borrowers are identified at equal rates regardless
of demographic membership.
8.3 Proxy analysis
Pearson correlations between the five highest-impact behavioral features and demographic group encodings
were computed to assess whether behavioral features inadvertently encode demographic information. The
maximum absolute correlation observed was 0.054 across all feature-group pairs, indicating no meaningful
proxy relationships. This finding partially addresses the concern raised by Fuster et al. (2022) that
behavioral proxies may perpetuate demographic discrimination through indirect pathways.
FairLend-Africa | Ibraheem Olabintan | KSUSTA | Page 19

Figure 13. ROC-AUC by demographic group. All groups exceed the random baseline (0.5) and demonstrate
consistent discrimination ability, indicating equitable predictive performance across subgroups.
8.4 Fairness limitations
These results must be interpreted with care. The synthetic data generating process explicitly constructed
demographic attributes to be uncorrelated with behavioral features a condition that may not hold in real-
world data, where structural inequality produces genuine correlations between geography, gender, and
financial behavior. In a real deployment, fairness auditing on actual borrower data would be required before
drawing conclusions about equitable treatment. Furthermore, we evaluate only three fairness criteria;
satisfying all simultaneously is mathematically impossible when base rates differ across groups
(Chouldechova, 2017), and the selection of criteria should ultimately reflect the values and legal context of
the deploying institution. Contemporary fairness literature further cautions that optimizing for static group
parity criteria can cause long-term economic harm by driving vulnerable populations into cycles of default,
highlighting the need for dynamic or causal fairness formulations in future iterations (Corbett-Davies et al.,
2017).
9. Discussion
9.1 Practical implications
Within the scope of the synthetic data generating process, the results demonstrate that behavioral financial
data carries sufficient predictive signal to support the proposed framework's credit assessment pipeline. A
ROC-AUC of 0.714 represents meaningful improvement over the random baseline (0.500), though the near-
identical performance of logistic regression (0.713) and the accuracy below the majority-class baseline
(0.755 vs 0.620) indicate that the threshold setting and model complexity require careful reconsideration
before any deployment context. For a microfinance institution serving unscored populations, the practical
value of the system lies not in replacing human judgment but in providing structured, explainable behavioral
evidence to supplement it a role for which the SHAP explanation layer is particularly well suited.
The SHAP explanation layer addresses a critical gap in ML-based credit systems: the inability to
communicate the basis of a decision to the borrower or loan officer. The waterfall and bar chart
visualizations implemented in the dashboard translate statistical outputs into actionable language
identifying, for example, that a borrower's declining wallet balance trend is the primary factor reducing
their credit probability, which the borrower can act upon.
FairLend-Africa | Ibraheem Olabintan | KSUSTA | Page 20

9.2 Limitations
Several limitations bound the conclusions of this study. First, the dataset is synthetic. While the data
generating process is calibrated to reflect behavioral patterns documented in the literature, it cannot capture
the full complexity of real mobile money data, including temporal dynamics, seasonal patterns, and network
effects. Validation on real transaction data from a partner institution remains necessary.
Second, the feature set is constructed from literature-informed assumptions rather than empirical feature
selection from real behavioral data. The relative importance of features may differ substantially across
populations, geographies, and mobile money platforms.
Third, the fairness analysis is constrained by the synthetic data's designed independence between
demographics and behavior. Real-world fairness properties cannot be inferred from this analysis.
Fourth, the system has not been evaluated for temporal stability. Credit scoring models are known to exhibit
concept drift as economic conditions change, and a production system would require ongoing monitoring
and retraining.
Fifth, the near-identical performance of logistic regression (ROC-AUC: 0.713) and tuned XGBoost (ROC-
AUC: 0.714) suggests that the behavioral features in the synthetic dataset exhibit primarily linear structure.
This limits the external validity of the SHAP non-linearity analysis in Section 7.3 and raises the question
of whether XGBoost's additional complexity is justified. On real mobile money data with genuine non-
linear feature interactions, the performance gap between linear and non-linear models may be larger.
Sixth, the engineered composite features (transaction intensity, savings commitment ratio, airtime stability)
provided no measurable improvement over the 16 raw features in the ablation study (ΔAUC = -0.0002).
While these features have sound theoretical motivation, their practical value on this synthetic dataset is
negligible. Validation on real data is required to determine whether the engineering decisions add value in
practice.
Seventh, the paper assumes that SHAP explanations reliably represent model behavior. Recent work has
demonstrated that post-hoc explanation methods including SHAP can be manipulated to conceal systematic
bias while producing plausible-looking explanations (Slack et al., 2020). This adversarial vulnerability
means SHAP explanations should be treated as decision-support tools subject to auditing rather than as
definitive proofs of model behavior.
Eighth, while TreeExplainer provides exact Shapley values relative to the tree ensemble's output, it assumes
feature independence when computing conditional expectations. In the presence of correlated features —
such as the savings-related features identified in Figure 3 SHAP values may distribute credit erroneously
across correlated predictors, potentially misrepresenting individual feature contributions (Lundberg et al.,
2020; Kumar et al., 2020).
9.3 Future work
Several extensions would strengthen this research. First, partnership with a microfinance institution or
mobile money operator to validate the framework on real transaction data would address the most
significant limitation. Second, longitudinal analysis incorporating time-series features from transaction
histories could substantially improve predictive performance. Third, comparison with causal inference
approaches to credit scoring addressing the confounding between behavioral features and unobserved
creditworthiness represents a theoretically important extension. Fourth, the fairness framework could be
extended to incorporate counterfactual fairness (Kusner et al., 2017), which provides stronger guarantees
FairLend-Africa | Ibraheem Olabintan | KSUSTA | Page 21

than the statistical parity criteria evaluated here. Fifth, implementing conditional expectation SHAP
frameworks to mitigate feature dependency errors would improve individual explanation reliability on
correlated feature sets. Sixth, incorporating adversarial robustness evaluation for SHAP explanations to
detect potential manipulation of post-hoc explanations (Slack et al., 2020) and developing explanation
methods resistant to such attacks represents an important direction for ensuring trustworthy credit decisions
in high-stakes deployment contexts.
10. Conclusion
This paper presented FairLend-Africa, an explainable machine learning framework for alternative credit
scoring using behavioral financial data. The system combines XGBoost-based prediction, SHAP-based
individual explanation, and systematic fairness auditing in a deployable architecture accessible to resource-
constrained institutions. On a synthetically generated dataset reflecting African mobile money behavioral
patterns, the framework achieves a ROC-AUC of 0.7137, satisfies demographic parity and equal
opportunity criteria across all evaluated subgroups, and provides individual-level explanations identifying
wallet balance trend and savings consistency as the dominant creditworthiness signals under the synthetic
data generating process. Comparison with a logistic regression baseline and feature ablation study reveal
that the behavioral features exhibit primarily linear structure on synthetic data, motivating validation on
real mobile money transaction data where non-linear interactions and genuine demographic correlations are
expected to emerge.
The contribution of this work is methodological rather than empirical: we demonstrate that the combination
of alternative behavioral data, gradient boosted trees, post-hoc explainability, and structured fairness
auditing can be implemented as a coherent, reproducible, and deployable system within the resource
constraints of independent research. Validation on real mobile money data from African lending institutions
represents the critical next step toward practical application.
The complete codebase, dataset generation scripts, trained model artifacts, and experimental notebooks are
available at: https://github.com/highfrezh/fairlend-africa
Appendix
Table A1: Optimized XGBoost hyperparameters
Hyperparameter Value
learning_rate 0.05
max_depth 4
n_estimators 250
subsample 0.8
colsample_bytree 0.7
min_child_weight 5
scale_pos_weight 3.1
References
Agarwal, S., Amromin, G., Ben-David, I., Chomsisengphet, S., and Evanoff, D. D. (2020). Fintech and
household finance. Review of Financial Studies, 33(11), 5085–5126.
FairLend-Africa | Ibraheem Olabintan | KSUSTA | Page 22

Baesens, B., Van Gestel, T., Viaene, S., Stepanova, M., Suykens, J., and Vanthienen, J. (2003).
Benchmarking state-of-the-art classification algorithms for credit scoring. Journal of the Operational
Research Society, 54(6), 627–635.
Barocas, S. and Hardt, M. (2017). Fairness in machine learning. NeurIPS Tutorial. Available at:
https://fairmlbook.org
Biecek, P. and Burzykowski, T. (2021). Explanatory Model Analysis: Explore, Explain and Examine
Predictive Models.
Björkegren, D. and Grissen, D. (2018). Behavior revealed in mobile phone usage predicts loan repayment.
The World Bank Economic Review, 34(3), 618–634.
Blattner, L. and Nelson, S. (2021). How Costly is Noise? Data and Disparate Algorithms in Consumer
Credit. arXiv preprint arXiv:2105.07554.
Chen, T. and Guestrin, C. (2016). XGBoost: A scalable tree boosting system. In Proceedings of the 22nd
ACM SIGKDD International Conference on Knowledge Discovery and Data Mining, 785–794.
Chiteli, N. (2013). Agent banking operations as a competitive strategy of commercial banks in Kisumu
City, Kenya. International Journal of Business and Social Science, 4(13).
Chouldechova, A. (2017). Fair prediction with disparate impact: A study of bias in recidivism prediction
instruments. Big Data, 5(2), 153–163.
Corbett-Davies, S., Pierson, E., Feller, A., Goel, S., and Huq, A. (2017). Algorithmic decision making and
the cost of fairness. In Proceedings of the 23rd ACM SIGKDD International Conference on Knowledge
Discovery and Data Mining, 797–806.
Demirgüç-Kunt, A., Klapper, L., Singer, D., and Ansar, S. (2022). The Global Findex Database 2021.
World Bank Publications.
Dwork, C., Hardt, M., Pitassi, T., Reingold, O., and Zemel, R. (2012). Fairness through awareness. In
Proceedings of the 3rd Innovations in Theoretical Computer Science Conference, 214–226.
Fuster, A., Goldsmith-Pinkham, P., Ramadorai, T., and Walther, A. (2022). Predictably unequal? The
effects of machine learning on credit markets. Journal of Finance, 77(1), 5–47.
Greenleaf, G. (2021). Global Data Privacy Laws 2021: Authoritarian Backlight on Progress. International
Data Privacy Law, 11(1), 24–45.
GSMA (2023). The State of Mobile Money in Sub-Saharan Africa. GSMA Research Report.
Hardt, M., Price, E., and Srebro, N. (2016). Equality of opportunity in supervised learning. In Advances in
Neural Information Processing Systems, 29.
Jordon, J., Szpruch, L., Houssiau, F., Bottarelli, M., Cherubin, G., Maple, C., Cohen, S. N., and Weller, A.
(2022). Synthetic data what, why and how? arXiv preprint arXiv:2205.03257.
Khandani, A. E., Kim, A. J., and Lo, A. W. (2010). Consumer credit-risk models via machine-learning
algorithms. Journal of Banking and Finance, 34(11), 2767–2787.
Kozodoi, N., Jacob, J., and Lessmann, S. (2022). Fairness in credit scoring: Assessment, implementation
and profit implications. European Journal of Operational Research, 297(2), 722–737.
FairLend-Africa | Ibraheem Olabintan | KSUSTA | Page 23

Kumar, I. E., Venkatasubramanian, S., Gupta, A., and Friedler, S. (2020). Problems with Shapley-value-
based explanations as feature importance measures. In Proceedings of the 2020 International Conference
on Fairness, Accountability, and Transparency (ICFAIR), 430–437.
Kusner, M. J., Loftus, J., Russell, C., and Silva, R. (2017). Counterfactual fairness. In Advances in Neural
Information Processing Systems, 30.
Lauer, K. and Lyman, T. (2015). Digital financial inclusion: Implications for customers, regulators,
supervisors, and standard-setting bodies. CGAP Technical Guide.
Ledgerwood, J. (1999). Microfinance Handbook: An Institutional and Financial Perspective. World Bank
Publications.
Lundberg, S. M. and Lee, S. I. (2017). A unified approach to interpreting model predictions. In Advances
in Neural Information Processing Systems, 30.
Lundberg, S. M., Erion, G., Chen, H., DeGrave, A., Prutkin, J. M.,
Nair, B., Katz, R., Himmelfarb, J., Bansal, N., and Lee, S. I. (2020). From local explanations to global
understanding with
explainable AI for trees. Nature Machine Intelligence, 2(1), 56–67.
Niculescu-Mizil, A. and Caruana, R. (2005). Predicting good probabilities with supervised learning. In
Proceedings of the 22nd International Conference on Machine Learning, 625–632.
Pedregosa, F., Varoquaux, G., Gramfort, A., Michel, V., Thirion, B., Grisel, O., and others (2011). Scikit-
learn: Machine learning in Python. Journal of Machine Learning Research, 12, 2825–2830.
Ribeiro, M. T., Singh, S., and Guestrin, C. (2016). "Why should I trust you?": Explaining the predictions
of any classifier. In Proceedings of the 22nd ACM SIGKDD International Conference, 1135–1144.
Slack, D., Hilgard, S., Jia, E., Singh, S., and Lakkaraju, H. (2020). Fooling LIME and SHAP: Adversarial
attacks on post hoc explanation methods. In Proceedings of the AAAI Conference on Human Computation,
8(1), 180–186.
Suri, T. and Jack, W. (2016). The long-run poverty and gender impacts of mobile money. Science,
354(6317), 1288–1292.
Totolo, E. (2018). Kenya's Digital Credit Revolution: Five Years On. FSD Kenya Technical Note.
van Buuren, S. (2018). Flexible Imputation of Missing Data. CRC Press. Available at: https://ema.drwhy.ai
Zhang, Y. and Long, J. (2021). Fairness-aware learning with missing attributes. In Proceedings of the 2021
AAAI Conference on Human Computation and Crowdsourcing (HCOMP), 154–162.
FairLend-Africa | Ibraheem Olabintan | KSUSTA | Page 24