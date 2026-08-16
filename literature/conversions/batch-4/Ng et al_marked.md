---
conversion_metadata:
  converted_at: "2026-07-21T07:47:04Z"
  converter_tool: "markitdown"
  converter_version: "0.1.6"
  source_pdf: "Ng et al.pdf"
  source_pdf_sha256: "f3c30041b5ba142e60ca5eecd75eeae402b34b6ca02db538cdcd0424b2fb5b6d"
  page_count: 32
  markdown_char_count: 235082
---

<!-- PAGE-AWARE EXTRACTION (via pdfminer.six) -->

<!-- PAGE 1 -->

6
2
0
2

r
p
A
6

]
T
S
.
n
i
f
-
q
[

4
v
6
6
0
6
1
.
0
1
5
2
:
v
i
X
r
a

Published as a conference paper at ICLR 2026

AI-BAAM: AI-DRIVEN BANK STATEMENT ANALYT-
ICS AS ALTERNATIVE DATA FOR MALAYSIAN MSME
CREDIT SCORING

Chun Chet Ng∗∗, Zhen Hao Chu∗, Jia Yu Lim,
Yin Yin Boon, Wei Zeng Low & Jin Khye Tan
AI Lens, Kuala Lumpur, Malaysia
chunchet.ng@ailensgroup.com

ABSTRACT

Despite accounting for 96.1% of all businesses in Malaysia (Department of Statis-
tics Malaysia, 2025), access to financing remains one of the most persistent chal-
lenges faced by Micro, Small, and Medium Enterprises (MSMEs). Newly es-
tablished businesses are often excluded from formal credit markets as traditional
underwriting approaches rely heavily on credit bureau data. This study investi-
gates the potential of bank statement data as an alternative data source for credit
assessment to promote financial inclusion in emerging markets. First, we propose
a cash flow-based underwriting pipeline where we utilize bank statement data for
end-to-end data extraction and machine learning credit scoring. Second, we in-
troduce a novel dataset of 611 loan applicants from a Malaysian consulting firm.
Third, we develop and evaluate credit scoring models based on application infor-
mation and bank transaction-derived features. Empirical results demonstrate that
incorporating bank statement features yields substantial improvements, with our
best model achieving an AUROC of 0.806 on validation set, representing a 24.6%
improvement over models using application information only. Finally, we will
release the anonymized bank transaction dataset to facilitate further research on
MSME financial inclusion within Malaysia’s emerging economy.

1

INTRODUCTION

Financial inclusion remains a pressing challenge in emerging markets, where a significant portion
of the population lacks sufficient credit history to access formal lending. According to the Secu-
rities Commission Malaysia (Malaysia, 2025), MSMEs are estimated to contribute around 60% of
Malaysia’s gross domestic product. Despite their significant contributions, MSMEs remain under-
served by financial institutions in terms of access to financing, giving rise to an estimated MYR 90
billion funding gap (Corporation, 2017). One fundamental issue is that many MSMEs do not have
lending history. Traditional credit assessment relies heavily on credit bureau data such as repayment
history, outstanding obligations, and past delinquencies. While traditional credit models work well
for established businesses, they have shortcomings for MSMEs with thin credit files. First, they are
inherently backward-looking and focus on past repayment behavior rather than current or forward-
looking capacity to repay. Second, they overlook real-time financial signals or operational dynamics
that could more accurately reflect a firm’s present financial health. Third, they omit alternative indi-
cators of creditworthiness, such as cash flow consistency, receivables and payables patterns, digital
transactions, and behavioral metrics from daily financial activity.

On the other hand, bank statements represent an up-to-date and verifiable source of financial be-
havior that also captures income regularity, spending patterns, and cash flow stability. This study
explores the use of Malaysian bank statement transactions as alternative data for credit scoring model
development and evaluates their predictive value for MSMEs. The objectives are as follows:

• To propose a cash flow-based underwriting workflow capable of ingesting and analyzing

bank transaction data for credit decisioning to narrow the MSME financing gap.

∗These authors contributed equally.

1

---

<!-- PAGE 2 -->

Published as a conference paper at ICLR 2026

Figure 1: Proposed end-to-end workflow using bank statement transaction data for credit scoring.

• To introduce the first-ever Malaysian bank statement dataset based on MSME loans.

• To evaluate the performance of machine learning–based credit scoring models trained on
the proposed bank statement transaction dataset, and to examine the feasibility and predic-
tive power of transaction-derived features in assessing MSME creditworthiness.

2 RELATED WORK

With the recent technological advancements in machine learning algorithms, the research commu-
nity has recognized the limitations of existing traditional credit scoring methods (Gote & Mendhe,
2024). Such studies are crucial for enhancing financial inclusion of MSMEs in emerging markets,
where MSMEs are often the backbone of economic growth despite having limited access to financ-
ing (Elebe & Imediegwu, 2021). As such, alternative data from non-traditional sources that are not
included in standard credit bureau files are being used for credit scoring (Group, 2024).

Limitations of Traditional Credit Scoring. Traditional credit scoring models used by financial
institutions primarily rely on credit bureau data such as payment history, amount of debt, and other
indicators (Shivhare, 2024). Unfortunately, reliance on such data creates a high entry barrier for
MSMEs in emerging economies where they usually lack audited financial statements or loan ser-
vicing history required by financial institutions (Courchane & Baines, 2020; Elebe & Imediegwu,
2021). This leads MSMEs to be perceived as high-risk applicants and results in a perpetual cycle of
financial exclusion that severely limits their growth potential (Courchane & Baines, 2020). Besides,
traditional methods fail to capture recent cash flow status of MSMEs, which can be an accurate rep-
resentation of financial health (Elebe & Imediegwu, 2021). A recent survey indicates that 58% of
financial institutions feel less confident to make decisions based on traditional credit data only (Wat-
terson, 2024). The increasing dissatisfaction motivates the urgent need to use alternative data for a
more adaptive and inclusive credit assessment (Gote & Mendhe, 2024).

Credit Scoring with Alternative Data. In order to overcome the limitations of traditional methods,
credit underwriting using alternative data has emerged as a new approach (Gote & Mendhe, 2024;
Watterson, 2024; Ngwenya, 2024). For instance, mobile network data are used for credit scoring in
Africa (Ngwenya, 2024; Gathu, 2020) and bank account transactions are used for cash flow under-
writing in consumer lending (Watterson, 2024). Recent studies suggest that incorporating transac-
tional data can improve predictive accuracy and expand credit to underserved populations (Djeundje
et al., 2021). For instance, research has shown that retail transaction data can help construct alterna-
tive credit scores (Lee et al., 0). A study examining two Indian financial technology (FinTech) firms
found that transactional data from platform activity worked as well as credit bureau data in predict-
ing creditworthiness and improved the predictive accuracy when combined with bureau data (Caire
& Vidal, 2024). However, the adoption of alternative data in MSME lending in Malaysia remains at
an early stage, with limited research focus from the industry.

Machine Learning Models in Credit Scoring. Machine learning (ML) models have proven to
be highly effective in processing financial data to produce accurate credit scores (B¨ucker et al.,
2022; Gunnarsson et al., 2021; Trivedi, 2020). These include statistical models like Logistic Re-
gression (LR), Naive Bayes (NB), and ensemble methods like Random Forest, AdaBoost, and Gra-

2

---

<!-- PAGE 3 -->

Published as a conference paper at ICLR 2026

dient Boosting (B¨ucker et al., 2022; Trivedi, 2020). For example, a Random Forest model achieved
the best performance on Taiwanese credit card data (Abbas & Hussein, 2024). A NB classifier
performed well on a highly imbalanced dataset from a New Zealand lender, especially when un-
declared features derived from bank statements were incorporated to supplement application form
data (Bunker et al., 2016). Given the positive impact of ML models in credit scoring, we aim to im-
prove financial inclusion of Malaysian MSMEs through proposed cash flow underwriting workflow.

Agentic Workflow in Credit Scoring. The deployment of Large Language Model (LLM)-powered
agentic systems marks a major advancement in automated credit scoring, loan approval, and cus-
tomer risk profiling within financial services (Okpala et al., 2025; Ali, 2025; Paleti, 2024). Recent
agentic frameworks have demonstrated strong performance in complex model risk management
tasks, including credit card approval and portfolio risk modeling (Okpala et al., 2025). Beyond
these use cases, agentic workflows are transforming banking by enabling adaptive credit profiling
and predictive loan approvals, thereby improving risk assessment accuracy through bias detection
and intelligent decision automation (Paleti, 2024). Similar approaches have been explored in mort-
gage lending, where machine learning-driven agents streamline underwriting and accelerate credit
evaluation (Chitturi, 2025). However, existing methods remain limited in production deployment
and lack a fully grounded, end-to-end workflow for MSME credit scoring.

3 BANK STATEMENT CASH FLOW UNDERWRITING

The proposed cash flow underwriting workflow enhances traditional credit underwriting by inte-
grating bank statement-derived features into the credit decision-making process. As illustrated in
Figure 1, the workflow consists of six main modules, each serving a distinct purpose. By automat-
ing manual extraction and analysis tasks, it shortens turnaround time and improves operational effi-
ciency while expanding credit access for thin-file MSMEs who lack sufficient credit bureau history.

Key Information Extraction Module. The key information extraction module employs Optical
Character Recognition (OCR) to extract essential fields from bank statements, including the bank
name, account number, account holder name, address, and statement date. These attributes are cross-
validated across statements to ensure accurate document ownership verification. These fields enable
the engine to link multiple accounts belonging to the same business entity, providing a holistic view
of its financial activity and cash flow across multiple bank accounts.

Transaction Table Extraction Module. The transaction table extraction module localizes and dig-
itizes tabular transaction data using OCR and layout analysis. It identifies table headers, then maps
rows and columns to extract transaction date, description, debit, credit, and balance amounts. Ad-
ditional pre-processing handles merged cells, page breaks, and format inconsistencies to preserve
data fidelity. The resulting structured transaction records serve as critical inputs for downstream
analytical modules that evaluate transaction patterns and account-level cash flow dynamics.

Fraud Analysis Module. The fraud analysis module leverages Computer Vision and rule-based
techniques to detect tampered or falsified bank statements. For each document, it examines both
visual and metadata cues such as inconsistent font styles or sizes, altered layouts, metadata mis-
matches, and abnormal pixel-level patterns that may indicate digital editing. Once potential tamper-
ing is identified, the affected statements are automatically flagged and returned to bank officers for
manual verification. This module provides an additional layer of security and assurance within the
underwriting workflow, ensuring that only authentic bank statements are analyzed for credit scoring.

Network Analysis Module. The network analysis module constructs transaction networks from the
extracted transaction data to uncover relationships among senders and beneficiaries across multiple
bank accounts. Using graph-based algorithms, it maps transaction linkages to detect circular fund
flows, kiting activities, and transfers to blacklisted or interrelated entities. This module also quanti-
fies network connectivity and transaction density to reveal abnormal money movement patterns that
may indicate fraudulent activity or financial distress, thereby enhancing overall risk assessment.

Cash Flow Analysis Module. The cash flow analysis module evaluates cash flow status based on
the inflows and outflows extracted from transaction records. It then applies Natural Language Pro-
cessing to infer transaction intent and classify entries into meaningful categories based on their de-
scriptions. Using these classifications, this module groups related transactions to identify spending
and receipt patterns, enabling the detection of outliers that deviate from typical cash flow behavior.

3

---

<!-- PAGE 4 -->

Published as a conference paper at ICLR 2026

It also computes key metrics such as average, highest, and lowest balances, quantifying cash flow
health and providing predictive features for credit scoring.

Data & Scoring Layer (Cash Flow Underwriting). This layer stores the analyzed data and engi-
neered features in a secure database to ensure traceability, regulatory compliance, and auditability.
The stored data are then preprocessed, and feature selection methods are applied to retain the most
informative variables. Using the selected features, a predictive model is trained to estimate the
probability of default and classify credit risk.

4 BANK STATEMENT TRANSACTION DATASET

Table 1: Statistics of MSME loan application datasets.

Split

Non-Default Default

Total

Train (60%)
Validation (40%)

Overall

310
208

518

56
37

93

366
245

611

Transaction data derived from bank statements represents a valuable alternative resource for cash
flow underwriting. To the best of our knowledge, no published studies have examined the use of
bank statement data for credit assessment of MSMEs in Malaysia. In collaboration with a consulting
firm, we constructed the first Malaysian bank statements dataset to address this gap.

This study adopts the Cross-Industry Standard Process for Data Mining (CRISP-DM) frame-
work (Chapman et al., 2000) as the methodological basis. CRISP-DM is a widely recognized pro-
cess model for systematic FinTech studies (Cheng, 2023; Rawat, 2023; da Rocha & de Sousa Junior,
2010) and comprises six main phases, i.e., business understanding, data understanding, data prepa-
ration, modeling, evaluation, and deployment. The first phase involves evaluating bank statement
transaction data as an alternative source for MSME credit risk assessment in Malaysia. The sec-
ond phase focuses on constructing the proposed dataset of 611 MSME loan applicants. Summary
statistics of the dataset are presented in Table 1.

Dataset Distribution and Preparation. The dataset is split into training (60%) and validation
(40%) sets using stratified random sampling to preserve class distribution. Among all applicants, 518
have a good credit record, while 93 have a history of default. Each applicant’s record contains two
main components: application form information submitted during the loan application process (e.g.,
demographic and business characteristics) and bank statement transaction data capturing detailed
inflows and outflows over a six-month period. The third phase involves data preparation and includes
several key tasks: (1) cleaning and de-duplicating data to ensure consistency, (2) fixing missing
values, standardizing transaction categories, and validating data integrity across all records, and (3)
deriving features and variables from transaction data, such as determining cash flow stability, deposit
regularity, and balance volatility.

Dataset Masking. All personally identifiable information was anonymized prior to analysis. To
preserve confidentiality, the features are grouped into application information (7 features) and bank
statement features (10 features). The specific feature calculations cannot be disclosed due to a non-
disclosure agreement and all bank statement features are derived solely from bank statement data.
Further details on ethical use of data are provided in Section 8.

5 TRANSACTION DATA-BASED CREDIT SCORING

The fourth phase of CRISP-DM in this study employs Logistic Regression on application form
and bank transaction data derived from our dataset as the baseline credit scoring model. LR is
widely adopted in credit risk modeling due to its interpretability, statistical robustness, and capacity
to estimate the probability of default (B¨ucker et al., 2022; Trivedi, 2020; Abbas & Hussein, 2024;
Bunker et al., 2016). To ensure that only informative predictors are retained, feature selection and
transformation are guided by the Weight of Evidence (WOE) and Information Value (IV) framework,
which are widely used in credit risk modeling for quantifying the predictive power of individual

4

---

<!-- PAGE 5 -->

Published as a conference paper at ICLR 2026

variables (Ngwenya, 2024).
In practice, each feature is divided into discrete intervals based on
suitable thresholds determined from the data. These bins allow the calculation of WOE and IV at
the group level, which makes them easier to interpret within a LR model. The following notation is
used to quantify the distribution of defaults and non-defaults across feature bins:

Let yi ∈ {0, 1} indicate default (yi = 1) or non-default (yi = 0) for applicant i. The total number
of default and non-default applicants is defined as:

Nb =

n
(cid:88)

i=1

I(yi = 1),

Ng =

n
(cid:88)

i=1

I(yi = 0),

(1)

Furthermore, let xij denote the value of feature j for applicant i. For a given feature j, suppose it is
divided into Kj disjoint bins {Bj1, . . . , BjKj }; then the corresponding counts within each bin are
defined as:

nbjk =

ngjk =

n
(cid:88)

i=1
n
(cid:88)

i=1

I(xij ∈ Bjk) I(yi = 1),

I(xij ∈ Bjk) I(yi = 0).

The distribution of defaults and non-defaults in each bin is:

Dist(b)

jk =

nbjk
Nb

,

Dist(g)

jk =

ngjk
Ng

.

Weight of Evidence (WOE). Firstly, we calculate the WOE for bin k of feature j using:
(cid:32) Dist(g)
jk
Dist(b)
jk

(cid:18) ngjk/Ng
nbjk/Nb

WOEjk = log

= log

(cid:33)

(cid:19)

.

(2)

(3)

(4)

A positive WOEjk indicates that bin Bjk is more common among non-default cases, suggesting
lower risk, whereas a negative value indicates a higher likelihood of default. Once WOE is computed
for each bin, the overall predictive strength of feature j can then be summarized by its IV.

Information Value (IV). Secondly, we measure the IV of feature j by aggregating the WOE across
all respective bins:

IVj =

Kj
(cid:88)

(cid:16)

k=1

Dist(g)

jk − Dist(b)

jk

(cid:17)

WOEjk.

(5)

A larger IVj indicates stronger discriminatory power of feature j between default and non-default
classes. In this study, IV serves as both a feature-ranking criterion and an interpretability measure,
helping to identify the most influential transaction-level indicators for creditworthiness. Following
industry practice (Siddiqi, 2017), we adopt the commonly used interpretive thresholds: IV < 0.02
(not predictive), 0.02 ≤ IV < 0.1 (weak), 0.1 ≤ IV < 0.3 (medium), 0.3 ≤ IV < 0.5 (strong), and
IV ≥ 0.5 (suspiciously high, suggesting potential data leakage).

Binning of Bank Statement Features. Specifically, we used supervised monotonic binning to ob-
tain {Bjk}Kj
k=1 for continuous transaction-derived variables (e.g., cash flow stability, balance volatil-
ity) and sparse categorical variables (e.g., State/Location). Then, rare categories are grouped to
ensure that each bin contains sufficient observations of both default and non-default classes while
preserving monotonicity. Computations of WOE and IV are performed on training folds only to
avoid data leakage.

6 EXPERIMENTS

Following the fifth phase of CRISP-DM, we conduct a series of experiments to evaluate the effec-
tiveness of the proposed cash flow underwriting workflow and the role of bank statement data in
enhancing MSME credit scoring performance. The experiments include comparative analyses with
established machine learning methods and detailed ablation studies on transaction-derived features.

5

---

<!-- PAGE 6 -->

Published as a conference paper at ICLR 2026

6.1

IMPLEMENTATION DETAILS

We benchmark the baseline Logistic Regression model against several widely used machine learn-
ing methods, including Random Forest (RF) (Breiman, 2001), Gradient Boosting (GB) (Friedman,
2001), and AdaBoost (AB) (Schapire, 2013). All models are implemented in scikit-learn (scikit
learn, 2025c;a;b;d). For the results in Section 6.2, models were trained with default hyperparame-
ters. In Section 6.3, hyperparameters were tuned using a randomized grid search with 50 trials to
ensure robustness. We evaluate model performance using the Area Under the Receiver Operating
Characteristic Curve (AUROC) (Bradley, 1997), which measures the ability to discriminate between
default and non-default cases across varying thresholds. An AUROC of 0.5 indicates no discrimina-
tive power (equivalent to random guessing), whereas a value of 1.0 indicates perfect discrimination.
To ensure interpretability and systematic analysis, both application information and bank statement
features are grouped into two categories:

i Account Behavior: logarithmic growth rate of average balance, six-month average account bal-
ance, change in 3-month minimum balance (recent), percent change in minimum balance vs
prior period, recent 3-month maximum average balance, and debt repayment capacity.

ii Business Demographics: business operational duration, geographic region, industry classifica-

tion (MSIC), total board directors, and minimum director age.

This structured feature grouping facilitates clearer attribution of model performance to different
behavioral and demographic dimensions of MSME credit profiles. It also supports experimental
reproducibility, while respecting confidentiality constraints around proprietary feature derivations.
Further details on deployment and operational considerations are provided in Appendix B.

6.2 QUANTITATIVE RESULTS

Validation Performance. Quantitative results on the validation split are presented in Figure 2.
Logistic Regression with blended features achieves the highest validation AUROC of 0.806, outper-
forming all ensemble methods across every feature set (GB: 0.664, RF: 0.678, AB: 0.680). This
consistent advantage is attributable to the small, class-imbalanced training set (310 non-default vs.
56 default cases), where LR’s well-calibrated probabilities and lower variance outweigh the flexi-
bility of tree-based ensembles (Brown & Mues, 2012; Lessmann et al., 2015). The value of bank
statement data is evident across all algorithms. For LR, moving from application-only to bank
statement-only features yields a gain of 0.116 AUROC (0.647 → 0.763), and blending both feature
sets achieves a further improvement to 0.806, a 24.6% relative gain over application-only. This pat-
tern holds for ensemble methods as well, confirming that cash flow behaviour captures default risk
dimensions that static application attributes alone cannot.

Extraction Module Performance. Beyond credit scoring, we evaluate the upstream AI modules
responsible for bank statement data extraction, as their accuracy directly affects downstream fea-
ture quality. For key information extraction, we benchmark 15 OCR-GPT pipeline configurations
against our template matching approach across six Malaysian banks (Table 3 in Appendix). Our
method achieves perfect 100% exact match accuracy and Normalized Edit Distance (NED) score
across all five extraction fields (bank name, account holder, account number, address, and statement
date), whereas the best-performing baseline (Azure AI 4.0 + GPT-4.1) reaches 100% on four fields
but drops to 94.82% on address extraction. For transaction table extraction, we evaluate 16 configu-
rations including recent vision-language models (Tables 8 and 9). Our template matching approach
achieves the highest average matching NED of 98.08% and exact NED of 97.80% across all col-
umn types. The closest competitor, Surya Paruchuri & Team (2025) + docTR Mindee (2021) with
GPT-5-mini, attains 96.94% and 94.23% respectively. Notably, end-to-end vision models such as
olmOCR (Poznanski et al., 2025) and paddleOCR-VL (Cui et al., 2025a) show substantially lower
performance on structured table extraction, underscoring the advantage of specialized pipeline de-
signs for financial documents. These general-purpose models struggle with the highly structured yet
bank-specific formatting of Malaysian bank statements, particularly multi-line transaction descrip-
tions, inconsistent date formats, and merged table cells that vary across institutions. Our template
matching method succeeds because it exploits the deterministic and standardized layouts within each
bank’s PDF format, bypassing the need for LLM entirely and thus eliminating both error propaga-
tion and API dependency. Table 2 summarizes the performance of selected configurations across

6

---

<!-- PAGE 7 -->

Published as a conference paper at ICLR 2026

Figure 2: Evaluation results of all models across different feature combinations and data splits.

Table 2: Summary of extraction performance, latency, and cost for methods evaluated on key in-
formation and transaction table extraction tasks. Accuracy scores are averaged over five fields (key
info) and five column types (table); F1 is averaged over six banks. Latency is the average total time
per document (seconds). The proposed template matching method was measured on a MacBook Air
2025 with M4 chip and 24GB unified memory. Cost is the total API token cost per document. Best
results are in bold; second-best are underlined. Full breakdowns in Appendix Tables 3–14.

Key Information

Table Extraction

Latency (s)

Cost (USD)

Method

docTR + GPT-4o-mini
docTR + GPT-4.1

PyMuPDF + GPT-4o-mini
PyMuPDF + GPT-4.1

Pdfium + GPT-4o-mini
Pdfium + GPT-4.1

Exact
Match

91.87
94.79

89.32
93.23

87.65
93.57

NED Match. Exact
Score

NED NED Score

F1

Key
Info Extraction Extraction

Table

Table

99.20
99.32

92.22
93.86

92.01
94.20

88.41
94.90

90.34
94.76

89.33
93.82

78.52
94.45

74.78
93.49

78.20
89.63

92.16
97.51

90.91
97.64

89.63
95.66

2.38
6.13

1.86
0.81

1.86
0.86

7.59
11.92

4.98
10.72

6.21
11.19

0.11

N/A
0.53

0.04
N/A

N/A
N/A

$0

Ours (template matching) 100.00

100.00

98.08

97.80 100.00 0.01

both extraction tasks. Full per-bank breakdowns, F1 scores, and detailed analysis along with a com-
prehensive latency and cost analysis across all configurations are provided in Appendix A.5.

Cost and Latency Analysis. Operational efficiency is a key consideration for AI-BAAM. We report
latency and cost measurements across all configurations in Appendix Tables 12, 13, and 14. For key
information extraction, our template matching method averages 0.01s per document with perfect
accuracy, orders of magnitude faster than the fastest LLM-based baseline (PyMuPDF (pymupdf,
2025) + GPT-4.1 at 0.81s). For table extraction, our method averages 0.11s compared to 4.98s for
PyMuPDF + GPT-4o-mini. For transaction table extraction, text-based pipelines such as PyMuPDF
+ GPT-4o-mini average under 5s, whereas end-to-end vision-language models require 104–150s.
Among LLM-based methods, Surya + docTR with GPT-5-mini ($0.02) and docTR with GPT-4.1-
nano ($0.03) are the most cost-effective, while docTR + GPT-4.1 incurs $0.53 for the dataset. Our
template matching approach eliminates API costs entirely while maintaining sub-second processing
latency, achieving the best accuracy–efficiency trade-off for production deployment.

7

---

<!-- PAGE 8 -->

Published as a conference paper at ICLR 2026

6.3 ABLATION STUDIES

Results in Figure 3 presents the information value of individual features, ranked by discriminatory
power. Bank statement features dominate the top positions with logarithmic growth rate of average
balance having the highest score of 0.484. In contrast, the strongest application information fea-
ture is business operational duration with an IV of 0.213, ranking far below the transaction-based
features. These findings reinforce the superior discriminatory strength of bank statement features in
distinguishing default from non-default outcomes.

Furthermore, we conducted ablation experiments by progressively removing feature groups to study
their relative importance in MSMEs credit scoring. We applied 5-fold cross-validation on the train-
ing split (366 samples) to reduce the risk that results are due to random chance and to increase
confidence in model stability. From results illustrated in Figure 2, we observe that Logistic Regres-
sion with blended features achieves the strongest cross-validation AUROC of 0.850, outperforming
Gradient Boosting (0.720) and Random Forest (0.730). When considering bank statement features
alone, LR achieves a validation AUROC of 0.821, compared to 0.672 for account information alone,
demonstrating a substantial uplift of 0.149 points. These results confirm that transactional data
provides significant incremental predictive value. Across all feature configurations and data splits,
LR consistently outperforms tree-based ensembles. Moreover, models incorporating bank transac-
tion data consistently outperform those relying on application information alone. Further studies of
the credit score distribution for each feature group as well as the analysis on rejected cases can be
found in Appendix A.6.1-A.6.2. In general, these findings strongly support the hypothesis that bank
statement transaction data offers significant predictive power in credit risk assessment for MSMEs
in Malaysia. While application form information provides some discriminatory power, the inclu-
sion of bank transaction-based features substantially enhances model performance, reinforcing the
effectiveness of AI-BAAM. Limitations and future work are discussed in Appendix C.

Figure 3: IV of features derived from application information and bank statement data.

7 CONCLUSION

This study introduces bank statement transactions as alternative data for MSME credit scoring in
Malaysia and presents AI-BAAM, an end-to-end cash flow underwriting workflow spanning doc-
ument extraction, feature engineering, and predictive modeling. Empirical results confirm that
transaction-derived features capture dynamic financial behavior overlooked by traditional credit
models: models trained on bank transaction data alone substantially outperform those using only
application information, and combining both feature sets yields the highest predictive power. Be-
yond credit scoring, we benchmark over 30 OCR and LLM configurations for key information and
transaction table extraction across six Malaysian banks. Our template matching approach achieves
perfect accuracy on key information fields and the highest NED and F1 scores on table extraction,
while processing documents in under 0.12 seconds with zero API cost. In contrast, the best LLM-
based pipelines require 0.81-11.92 seconds per document and incur a total of $0.53, and end-to-end

8

---

<!-- PAGE 9 -->

Published as a conference paper at ICLR 2026

vision-language models exhibit 104-150 seconds latency with substantially lower extraction quality.
These findings demonstrate that our template matching method offers a superior accuracy-efficiency
trade-off over general-purpose LLM pipelines for Malaysian bank statements.

8 ETHICAL USE OF DATA AND INFORMED CONSENT

All data used in this study were obtained through a formal data-sharing agreement with the partner-
ing Malaysian consulting firm. The dataset contains loan application records and bank statements
from MSME applicants who consented to the use of their financial data for credit assessment pur-
poses as part of the loan application process. All personally identifiable information, including ap-
plicant names, national identification numbers, bank account numbers, and physical addresses, was
masked or removed prior to analysis, as described in Section 4. Feature names were anonymized
and grouped into application information and bank statement features to prevent re-identification.
The specific feature derivation logic is protected under a non-disclosure agreement with the lending
institution. No individual-level predictions or risk scores are disclosed in this paper, and all reported
results are presented in aggregate form. The anonymized dataset intended for public release will
undergo additional de-identification review to ensure compliance with Malaysia’s Personal Data
Protection Act 2010 (PDPA) and applicable institutional data governance policies.

9 REPRODUCIBILITY

The complete modeling pipeline, feature engineering methodology, and evaluation protocol are doc-
umented in Sections 4–6.2. All machine learning models are implemented using scikit-learn (scikit
learn, 2025c;d;a;b), with hyperparameter configurations detailed in Section 6.2 and ablation set-
tings in Section 6.3. The WOE/IV-based feature transformation and supervised monotonic binning
procedures are described formally in Section 4, and the feature groupings used in all experiments
are enumerated in Section 6.2. For the OCR and LLM benchmarks, the evaluated configurations
and system setups are reported in Appendix A.3 and Appendix A.4. The dataset used in this study
consists of real bank statements and loan records collected under a data-sharing agreement with a
Malaysian consulting firm. As the data contains sensitive financial information, we are unable to re-
lease the raw records due to contractual obligations and Malaysia’s PDPA. We are working towards
releasing an anonymized version pending a de-identification review, as described in Section 8. In
the meantime, researchers can replicate our workflow on their own bank statement data using the
step-by-step methodology detailed throughout the paper and appendix.

10 ACKNOWLEDGEMENT

We thank the Cradle Fund and the Microsoft for Startups program for their funding support, which
made this research possible. We also thank the DocLab, DocSuite, and MLSuite teams at AI Lens for
their contributions across document processing, system development, and machine learning, which
collectively shaped the AI-BAAM pipeline presented in this work.

9

---

<!-- PAGE 10 -->

Published as a conference paper at ICLR 2026

REFERENCES

Elaf Adel Abbas and Nisreen Abbas Hussein. Algorithm comparison for data mining classification:
Assessing bank customer credit scoring default risk. Jurnal Kejuruteraan, 36(5):1935–1944,
2024.

Mohammad Asif Ali. Efficient underwriting using agentic ai. Available at SSRN 5169848, 2025.

Andrew P Bradley. The use of the area under the roc curve in the evaluation of machine learning

algorithms. Pattern recognition, 30(7):1145–1159, 1997.

Leo Breiman. Random forests. Machine learning, 45(1):5–32, 2001.

Iain Brown and Christophe Mues. An experimental comparison of classification algorithms for
imbalanced credit scoring data sets. Expert systems with applications, 39(3):3446–3453, 2012.

Michael B¨ucker, Gero Szepannek, Alicja Gosiewska, and Przemyslaw Biecek. Transparency, au-
ditability, and explainability of machine learning models in credit scoring. Journal of the Opera-
tional Research Society, 73(1):70–90, 2022.

Rory P Bunker, Wenjun Zhang, and M Asif Naeem. Improving a credit scoring model by incorpo-

rating bank statement derived features. arXiv preprint arXiv:1611.00252, 2016.

Dean Caire and Maria Fernandez Vidal. Leveraging transactional data for micro and small enterprise
(mse) lending, March 2024. URL https://www.cgap.org/sites/default/files/
publications/Leveraging%20Transactional%20Data.pdf.

Pete Chapman,

Julian Clinton, Randy Kerber, Colin Shearer Thomas Khabaza ands
Crisp-dm 1.0 step-by-step data mining guide,
URL https://www.kde.cs.uni-kassel.de/wp-content/uploads/

Thomas Reinartz, and R¨udiger Wirth.
2000.
lehre/ws2012-13/kdd/files/CRISPWP-0800.pdf.

Aijun Cheng. Evaluating fintech industry’s risks: A preliminary analysis based on crisp-dm frame-

work. Finance Research Letters, 55:103966, 2023.

Naganarendar Chitturi. Agentic artificial intelligence: Architectural paradigms and transformative
impact of autonomous financial assistants across the mortgage lending lifecycle. Journal of Com-
puter Science and Technology Studies, 7(8):1155–1165, 2025.

International Finance Corporation. MSME Finance Gap: Assessment of the Shortfalls and Oppor-
tunities in Financing Micro, Small, and Medium Enterprises in Emerging Markets. World Bank,
Washington, D.C., United States, 2017.

MJ Courchane

and AP Baines.
2020.

The

use

underwriting
https://finreglab.org/wp-content/

cash-flow data

of

in

October

credit,
URL
uploads/2023/12/FinRegLab_2020-03-03_Research-Report_
The-Use-of-Cash-Flow-Data-in-Underwriting-Credit_
Market-Context-and-Policy-Analysis.pdf.

Cheng Cui, Ting Sun, Suyin Liang, Tingquan Gao, Zelun Zhang, Jiaxuan Liu, Xueqing Wang,
Changda Zhou, Hongen Liu, Manhui Lin, et al. Paddleocr-vl: Boosting multilingual docu-
ment parsing via a 0.9 b ultra-compact vision-language model. arXiv preprint arXiv:2510.14528,
2025a.

Cheng Cui, Ting Sun, Manhui Lin, Tingquan Gao, Yubo Zhang, Jiaxuan Liu, Xueqing Wang, Zelun
Zhang, Changda Zhou, Hongen Liu, Yue Zhang, Wenyu Lv, Kui Huang, Yichao Zhang, Jing
Zhang, Jun Zhang, Yi Liu, Dianhai Yu, and Yanjun Ma. Paddleocr 3.0 technical report, 2025b.
URL https://arxiv.org/abs/2507.05595.

B Carneiro da Rocha and R Timoteo de Sousa Junior. Identifying bank frauds using crisp-dm and
International Journal of Computer Science and Information Technology, 2(5):

decision trees.
162–169, 2010.

10

---

<!-- PAGE 11 -->

Published as a conference paper at ICLR 2026

DOSM Department of Statistics Malaysia.

gust
2020-02-11-08-01-24/profile-and-importance-to-the-economy.

in 2015-2024, Au-
URL https://smecorp.gov.my/index.php/en/policies/

Profile of msmes

2025.

Viani B Djeundje, Jonathan Crook, Raffaella Calabrese, and Mona Hamid. Enhancing credit scoring

with alternative data. Expert Systems with Applications, 163:113766, 2021.

Adrien Ehrhardt, Christophe Biernacki, Vincent Vandewalle, Philippe Heinrich, and S´ebastien
Beben. Reject inference methods in credit scoring. Journal of Applied Statistics, 48(13-15):
2734–2754, 2021. doi: 10.1080/02664763.2021.1929090.

Okeoghene Elebe and Chikaome Chimara Imediegwu. A credit scoring system using transaction-
level behavioral data for msmes. Journal of Frontiers in Multidisciplinary Research, 2(1):312–
322, 2021.

Jerome H Friedman. Greedy function approximation: a gradient boosting machine. Annals of

statistics, pp. 1189–1232, 2001.

Anthony Gathu. The Role of alternative data in accurately determining credit score for mobile

lending on digital wallets in Kenya. PhD thesis, Strathmore University, 2020.

Amol Gote and Vikas Mendhe. Building a cash flow underwriting system: Insights from implemen-

tation. International Journal of Computer Trends and Technology, 72(2):70–74, 2024.

World Bank Group.

use

of

alternative

in

credit

Opportunities,

ment:
documents1.worldbank.org/curated/en/099031325132018527/pdf/
P179614-3e01b947-cbae-41e4-85dd-2905b6187932.pdf.

challenges,

URL

and

data
2024.

The
risks,

risk

assess-
https://

Bj¨orn Rafn Gunnarsson, Seppe Vanden Broucke, Bart Baesens, Mar´ıa ´Oskarsd´ottir, and Wilfried
Lemahieu. Deep learning for credit scoring: Do or don’t? European Journal of Operational
Research, 295(1):292–305, 2021.

Experian Insights. Reject inference and underwriting: A deep dive, 2024. URL https://www.

experian.com/blogs/insights/reject-inference/.

Eunji Kim, Jehyuk Lee, Hunsik Shin, Hoseong Yang, Sungzoon Cho, Seung-kwan Nam, Youngmi
Song, Jeong-a Yoon, and Jong-il Kim. Champion-challenger analysis for credit card fraud de-
tection: Hybrid ensemble and deep learning. Expert Systems with Applications, 128:214–224,
2019.

Jung Youn Lee, Joonhyuk Yang, and Eric T. Anderson. Express: Who benefits from alter-
Journal of Marketing Research, 0(ja):
native data for credit scoring? evidence from peru.
00222437251360996, 0. doi: 10.1177/00222437251360996. URL https://doi.org/10.
1177/00222437251360996.

Stefan Lessmann, Bart Baesens, Hsin-Vonn Seow, and Lyn C Thomas. Benchmarking state-of-
the-art classification algorithms for credit scoring: An update of research. European journal of
operational research, 247(1):124–136, 2015.

Zhang Li, Yuliang Liu, Qiang Liu, Zhiyin Ma, Ziyang Zhang, Shuo Zhang, Zidun Guo, Jiarui Zhang,
Xinyu Wang, and Xiang Bai. Monkeyocr: Document parsing with a structure-recognition-relation
triplet paradigm. arXiv preprint arXiv:2506.05218, 2025.

Minghui Liao, Zhaoyi Wan, Cong Yao, Kai Chen, and Xiang Bai. Real-time scene text detection
with differentiable binarization. In Proceedings of the AAAI conference on artificial intelligence,
volume 34, pp. 11474–11481, 2020.

Security Commissions Malaysia.

Enabling a more relevant, efficient and diversified mar-
ket, 2025. URL https://www.sc.com.my/api/documentms/download.ashx?id=
61f72817-e06d-4e54-b25c-8be8abddcd28.

Mindee. doctr: Document text recognition. https://github.com/mindee/doctr, 2021.

11

---

<!-- PAGE 12 -->

Published as a conference paper at ICLR 2026

Andrew Y Ng. Feature selection, l 1 vs. l 2 regularization, and rotational invariance. In Proceedings

of the twenty-first international conference on Machine learning, pp. 78, 2004.

Mfanasibili Ngwenya. Credit scoring in africa: Employing logistic regression on alternative data. In
2024 4th International Conference on Electrical, Computer, Communications and Mechatronics
Engineering (ICECCME), pp. 1–6, Maldives, 2024. IEEE. doi: 10.1109/ICECCME62383.2024.
10796011.

Izunna Okpala, Ashkan Golgoon, and Arjun Ravi Kannan. Agentic ai systems applied to tasks in fi-
nancial services: modeling and model risk management crews. arXiv preprint arXiv:2502.05439,
2025.

Srinivasarao Paleti. Agentic ai in financial decision-making: Enhancing customer risk profiling,
predictive loan approvals, and automated treasury management in modern banking. Multidisci-
plinary, Scientific Work and Management Journal, 2024.

Vikas Paruchuri and Datalab Team. Surya: A lightweight document ocr and analysis toolkit.

https://github.com/VikParuchuri/surya, 2025. GitHub repository.

Jake Poznanski, Jon Borchardt, Jason Dunkelberger, Regan Huff, Daniel Lin, Aman Rangapur,
Christopher Wilhelm, Kyle Lo, and Luca Soldaini. olmOCR: Unlocking Trillions of Tokens
in PDFs with Vision Language Models, 2025. URL https://arxiv.org/abs/2502.
18443.

pymupdf. Pymupdf. https://github.com/pymupdf/PyMuPDF, 2025. GitHub repository.

Kuldeep Rawat. Applying crisp-dm methodology in developing machine learning model for credit

risk prediction. In Science and Information Conference, pp. 522–538. Springer, 2023.

Robert E Schapire. Explaining adaboost. In Empirical inference: festschrift in honor of vladimir N.

Vapnik, pp. 37–52. Springer, 2013.

scikit learn. Adaboostclassifier, 2025a. URL https://scikit-learn.org/stable/

modules/generated/sklearn.ensemble.AdaBoostClassifier.html.

scikit

learn.

Gradientboostingclassifier,

2025b.

URL

https://

scikit-learn.org/stable/modules/generated/sklearn.ensemble.
GradientBoostingClassifier.html.

scikit learn. Logisticregression, 2025c. URL https://scikit-learn.org/stable/
modules/generated/sklearn.linear_model.LogisticRegression.html.

scikit learn. Randomforestclassifier, 2025d. URL https://scikit-learn.org/stable/
modules/generated/sklearn.ensemble.RandomForestClassifier.html.

Baoguang Shi, Xiang Bai, and Cong Yao. An end-to-end trainable neural network for image-based
sequence recognition and its application to scene text recognition. IEEE transactions on pattern
analysis and machine intelligence, 39(11):2298–2304, 2016.

Tanmay Shivhare. How to Utilize Bank Statements as a New Credit Scoring Method. PhD thesis,

Dublin, National College of Ireland, 2024.

Naeem Siddiqi. Intelligent credit scoring: Building and implementing better credit risk scorecards.

John Wiley & Sons, North Carolina, USA, 2017. ISBN 9781119282396.

Shrawan Kumar Trivedi. A study on credit scoring modeling with different feature selection and

machine learning approaches. Technology in Society, 63:101413, 2020.

Bin Wang, Chao Xu, Xiaomeng Zhao, Linke Ouyang, Fan Wu, Zhiyuan Zhao, Rui Xu, Kaiwen Liu,
Yuan Qu, Fukai Shang, et al. Mineru: An open-source solution for precise document content
extraction, 2024a. arXiv preprint arXiv:2409.18839.

12

---

<!-- PAGE 13 -->

Published as a conference paper at ICLR 2026

Stewart Watterson.
2024.

Cash flow underwriting:
landscape,
URL https://assets.ctfassets.net/ss5kfr270og3/

November
2LceEfOxttxwSpVtkiAPUw/dd87916c5d598b4fa8950d12f896ab1d/
20241203_Cash_Flow_Underwriting_Reshaping_the_Lending_Landscape_
White_Paper_Plaid.pdf.

Reshaping

lending

the

Haoran Wei, Yaofeng Sun, and Yukun Li. Deepseek-ocr 2: Visual causal flow. arXiv preprint

arXiv:2601.20552, 2026.

13

---

<!-- PAGE 14 -->

Published as a conference paper at ICLR 2026

A APPENDIX

A.1 LOGISTIC REGRESSION MODEL

Given that WOE provides a log-odds transformation of each feature, this aligns naturally with the
LR model. The WOE transformed feature value can be represented as WOEj(xij) and the LR
model can be expressed in a simplified form as:

log

P (yi = 1 | xi)
P (yi = 0 | xi)

= β0 +

d
(cid:88)

j=1

βj WOEj(xij).

(6)

where β0 is the intercept and βj represents the coefficient for feature j. This allows direct inter-
pretation of coefficients in terms of the credit risk associated with each feature. Positive βj values
indicate that higher WOE corresponds to lower default risk, and vice versa. Hence, WOE encoding
stabilizes estimation and supports consistent, monotonic relationships between predictors and credit
outcomes.
Formally, let xi ∈ Rd denote the feature vector for applicant i, where d is the number of features
engineered from both application form data and bank statement transactions, and let yi ∈ {0, 1} be
the binary output indicating default (yi = 1) or non-default (yi = 0). The LR model specifies the
conditional probability of default as

P (yi = 1 | xi; β) = σ(β0 + x⊤

i β),

(7)

1+e−z is the sigmoid function, β0 ∈ R is the intercept term, and β ∈ Rd is the
where σ(z) = 1
coefficient vector associated with the predictors. The parameters are estimated by maximizing the
penalized log-likelihood function:

L(β) =

n
(cid:88)

i=1

[yi log pi + (1 − yi) log(1 − pi)] − λ ∥β∥2
2,

(8)

where pi = P (yi = 1 | xi; β) and λ ≥ 0 controls the strength of the ℓ2 regularization (Ng, 2004).
This mitigates overfitting by shrinking coefficient magnitudes, which is particularly important when
modeling high-dimensional, transaction-derived features.

A.2 USE OF LARGE LANGUAGE MODELS

A.2.1 DATASET

We gathered bank statements of various consulting firms in Malaysia. The dataset consists of ap-
proximately 110 unique bank statement PDFs from the top 6 banks in Malaysia: Maybank, Public
Bank, CIMB Bank, RHB Bank, Hong Leong Bank, and AmBank. Each bank statement contains key
information fields such as bank name, account holder name, account number, address, and statement
date, as well as transaction tables listing individual transactions with details such as date, description,
debit amount, credit amount, and balance.

A.2.2 MODEL CHOICES

Precise text bounding box coordinates for OCR results are required because bank officers must cross-
check extraction results before they can be used for subsequent processing; this ensures transparency,
traceability, and auditability of our AI results, and explains our design choice of using OCR and
LLMs for financial information extraction. The OCR models used are mainly from Azure with
different variations: prebuilt-bankStatement.us is an Azure Document Intelligence prebuilt OCR
model specifically designed for bank statements in the US, while pretrained-read is a more general
OCR model that can be fine-tuned for various document types. The Azure Vision 4.0 model refers
to the Azure generic OCR model. The GPT models used are GPT-4o-mini and GPT-4.1, which are
different versions of OpenAI’s GPT-4 architecture with varying capabilities and performance levels.

14

---

<!-- PAGE 15 -->

Published as a conference paper at ICLR 2026

Certain specialized OCR models such as MinerU (Wang et al.), PyMuPDF (pymupdf, 2025) and
PPStructureV3 (Cui et al., 2025b) are included for comparison since they are widely adopted in the
industry for document processing tasks. PyMuPDF-Formatted refers to formatting the output from
document parser to imitate actual document layout before passing them into LLM. LLM-based
OCR models such as olmOCR (Poznanski et al., 2025), paddleOCR-VL (Cui et al., 2025a), and
Surya (Paruchuri & Team, 2025) are also included for table extraction comparisons. Our template
matching method is built based on the layout of the bank statements in our dataset, where we manu-
ally define the regions of interest for key information fields and transaction tables. For our method,
we use DB with ResNet50 backbone (Liao et al., 2020) for text detection and CRNN with VGG16
backbone (Shi et al., 2016) for text recognition. Then we build our own template matching algorithm
in Python logic. Do note that we are the only method that is not using any LLMs for information
extraction.

As shown in Tables 3, 4, 8, and 9, our template matching method achieves the best performance when
the bank statement formats are consistent, which is the case in Malaysia. In real-world scenarios
where bank statement formats can vary significantly, template matching methods may not be as
effective as more flexible OCR models. In future work, we plan to explore more advanced techniques
such as OCR+LLM-based layout analysis and document understanding models (Deepseek-OCR
2 (Wei et al., 2026), MonkeyOCR (Li et al., 2025)) to improve the robustness of key information
and table extraction across diverse bank statement formats.

A.2.3 EVALUATION METRIC

Key information results are evaluated based on exact match accuracy between the extracted text
and the ground truth for each field. An exact match is counted when the extracted text matches the
ground truth character by character, including spaces and punctuation. The accuracy is then calcu-
lated as the percentage of exact matches over the total number of key information fields evaluated.

Table extraction results are evaluated based on the normalized edit distance (NED) between the
extracted text and the ground truth for each transaction row. The NED for a single row entry is
calculated as follows:

NED = 1 −

Edit Distance
max(Length of Extracted Text, Length of Ground Truth Text)

(9)

where Edit Distance is the minimum number of operations (insertions, deletions, substitutions) re-
quired to transform the extracted text into the ground truth text. A higher NED value indicates better
accuracy, with a maximum of 1.0 representing a perfect match. The score is then scaled to the range
of 0 to 100 for easier interpretation.

We report two variants of the per-column similarity score to capture different aspects of extraction
quality:

Matching NED Score (%). For each column (date, description, debit, credit, balance), we compute
the NED for every matched row. Only rows with NED > 70% are retained, and the per-column
score is the average NED across these filtered rows for a given bank. This metric measures how ac-
curately the system extracts content for rows that it has reasonably identified, by excluding severely
misaligned or garbled entries that fall below the 70% threshold. It thus reflects extraction quality
conditioned on successful row matching.

Exact NED Score (%). For each column, we compute the NED for every row without any filtering
threshold. All rows are included regardless of their NED value, and the per-column score is the
average NED across all rows for a given bank. This metric provides a stricter evaluation that penal-
izes both character-level extraction errors and row-level alignment failures (e.g., missed rows, extra
rows, or misaligned entries), as these contribute low NED values that reduce the overall average.

The key difference between the two metrics lies in their treatment of poorly matched rows. Match-
ing NED isolates extraction accuracy by filtering out rows with NED ≤ 70%, while exact NED
captures the full picture including row detection failures. A large gap between matching and exact
NED scores for a given configuration indicates that the system produces accurate extractions when
it correctly identifies rows, but frequently fails at row-level alignment or misses rows entirely. Con-
versely, similar matching and exact NED scores suggest consistent row detection with few alignment
failures.

15

---

<!-- PAGE 16 -->

Published as a conference paper at ICLR 2026

A.3 QUANTITATIVE RESULTS FOR KEY INFORMATION EXTRACTION

We evaluate key information extraction across the top six largest Malaysian banks: Maybank
(MBBE), Public Bank (PBBE), CIMB Bank (CIBB), RHB Bank (RHBB), Hong Leong Bank
(HLBB), and AmBank (ARBK). The evaluation covers five structured fields: bank name, account
holder, account number, address, and statement date. We report both exact match accuracy with
strict character-level equality and Normalized Edit Distance (NED) similarity with a tolerance for
minor character-level discrepancies. Tables 3 and 4 summarize the average exact match accuracy
and NED score performance across all banks respectively, while Tables 5 and 6 provide per-bank
breakdowns.

Overall Performance. Our template matching approach achieves a perfect 100% on both exact
match accuracy and NED score across all five fields and all six banks, demonstrating robust and
consistent extraction without reliance on external OCR or LLM APIs. Among the baselines, config-
urations pairing high-quality OCR engines (Pretrained-Read, Azure AI 4.0) with GPT-4.1 achieve
near-perfect results, with Azure AI 4.0 + GPT-4.1 reaching 100% exact match accuracy on four
fields (bank name, account holder, account number, and statement date) and 94.82% on address.
The address field proves most challenging across all configurations due to multi-line formatting and
bank-specific layout variations.

OCR Engine Impact. The choice of OCR engine substantially influences downstream extraction
quality. Cloud-based OCR solutions (Pretrained-Read, Azure AI 4.0) consistently outperform open-
source alternatives. MinerU exhibits the weakest bank name extraction (28.33%–41.30% exact
match accuracy) due to its inability to parse graphical logos and stylized text commonly found in
Malaysian bank statement headers. Text-based extractors (PyMuPDF, Pdfium) show variable bank
name accuracy (58.76%–74.87%), as they rely on the PDF text layer, which may not encode bank
names embedded in header images.
In contrast, docTR achieves 100% bank name accuracy by
leveraging deep learning-based text detection on rendered page images.

GPT Model Impact. Across all OCR engines, upgrading from GPT-4o-mini to GPT-4.1 consis-
tently improves extraction accuracy, particularly for address and statement date fields. For example,
with docTR, the address exact match accuracy improves from 73.97% to 80.82% when switching
to GPT-4.1. This improvement stems from GPT-4.1’s enhanced ability to parse multi-line address
formats and normalize date representations across different bank templates.

Per-Bank Variation. AmBank and Hong Leong Bank statements are generally easier to process due
to their standardized digital-native PDF formats, achieving near-perfect scores across most configu-
rations. RHB Bank and CIMB Bank present greater challenges: RHB Bank’s multi-column layouts
reduce MinerU’s performance to 40–70% across most fields, while CIMB Bank’s header formatting
leads to lower bank name recognition for text-based extractors. These per-bank variations under-
score the importance of bank-specific evaluation when deploying extraction systems in multi-bank
production environments.

Table 3: Average exact match accuracy scores across all top six largest banks.

OCR

Prebuilt-
BankStatement
Pretrained-Read
Pretrained-Read
Azure AI 4.0
Azure AI 4.0
docTR
docTR
MinerU
MinerU
PyMuPDF
PyMuPDF

GPT

N/A

gpt-4o-mini
gpt-4.1
gpt-4o-mini
gpt-4.1
gpt-4o-mini
gpt-4.1
gpt-4o-mini
gpt-4.1
gpt-4o-mini
gpt-4.1

Key Information Extraction - Exact Match Accuracy

Bank Name Acc Holder Acc Number Address Statement Date

93.39

80.82

92.86

100.00
100.00
100.00
100.00
100.00
100.00
28.33
41.30
62.09
71.16

96.48
100.00
98.15
100.00
87.78
93.15
86.48
86.67
96.30
98.33

100.00
100.00
100.00
100.00
100.00
100.00
90.95
93.33
100.00
100.00

92.77

89.10
92.43
88.20
94.82
73.97
80.82
61.43
72.14
90.58
96.67

Continued on next page

77.51

97.62
100.00
97.62
100.00
97.62
100.00
95.00
95.00
97.62
100.00

16

---

<!-- PAGE 17 -->

Published as a conference paper at ICLR 2026

OCR

GPT

PyMuPDF-
Formatted
PyMuPDF-
Formatted
Pdfium
Pdfium

gpt-4o-mini

gpt-4.1

gpt-4o-mini
gpt-4.1

Ours (template matching)

Table 3 – Continued from previous page

Key Information Extraction - Exact Match Accuracy

Bank Name Acc Holder Acc Number Address Statement Date

61.92

74.87

58.76
71.16
100.00

98.15

98.15

96.30
100.00
100.00

100.00

100.00

100.00
100.00
100.00

92.25

96.48

83.17
96.67
100.00

100.00

100.00

100.00
100.00
100.00

Table 4: Average NED scores across all top six largest banks.

Key Information Extraction - NED Score

Bank Name Acc Holder Acc Number Address Statement Date

93.39

82.75

95.11

GPT

N/A

gpt-4o-mini
gpt-4.1
gpt-4o-mini
gpt-4.1
gpt-4o-mini
gpt-4.1
gpt-4o-mini
gpt-4.1
gpt-4o-mini
gpt-4.1
gpt-4o-mini

OCR

Prebuilt-
BankStatement
Pretrained-Read
Pretrained-Read
Azure AI 4.0
Azure AI 4.0
docTR
docTR
MinerU
MinerU
PyMuPDF
PyMuPDF
PyMuPDF-
Formatted
PyMuPDF-
Formatted
Pdfium
Pdfium

100.00
100.00
100.00
100.00
100.00
100.00
37.00
43.79
64.99
71.17
69.36

97.36
100.00
98.59
100.00
98.44
98.02
88.29
86.67
97.28
98.33
98.15

98.40

96.30
99.34
96.90
99.59
97.84
98.60
77.46
84.20
99.11
99.82
99.17

99.50

98.97
99.82
100.00

79.13

99.70
100.00
99.70
100.00
99.70
100.00
97.50
96.25
99.70
100.00
100.00

100.00

100.00
100.00
100.00

100.00
100.00
100.00
100.00
100.00
100.00
92.74
93.33
100.00
100.00
100.00

100.00

100.00
100.00
100.00

gpt-4.1

75.77

99.32

gpt-4o-mini
gpt-4.1

Ours (template matching)

63.96
71.17
100.00

97.13
100.00
100.00

Table 5: Key information extraction exact match accuracy score grouped by bank across OCR and
GPT configurations.

OCR

GPT

Key Information Extraction - Exact Match Accuracy

Bank Name Acc Holder Acc Number Address Statement Date

Prebuilt-
BankStatement
Pretrained-Read
Pretrained-Read
Azure AI 4.0
Azure AI 4.0
docTR
docTR
MinerU
MinerU
PyMuPDF
PyMuPDF
PyMuPDF-
Formatted

CIMB Bank (7 Unique PDFs)

N/A

71.43

71.43

57.14

85.71

42.86

gpt-4o-mini
gpt-4.1
gpt-4o-mini
gpt-4.1
gpt-4o-mini
gpt-4.1
gpt-4o-mini
gpt-4.1
gpt-4o-mini
gpt-4.1
gpt-4o-mini

100.00
100.00
100.00
100.00
100.00
100.00
0.00
0.00
71.43
71.43
71.43

100.00
100.00
100.00
100.00
100.00
100.00
85.71
100.00
100.00
100.00
100.00

85.71
85.71
71.43
100.00
57.14
57.14
85.71
100.00
85.71
100.00
85.71

Continued on next page

85.71
100.00
85.71
100.00
85.71
100.00
100.00
100.00
85.71
100.00
100.00

100.00
100.00
100.00
100.00
100.00
100.00
100.00
100.00
100.00
100.00
100.00

17

---

<!-- PAGE 18 -->

Prebuilt-
BankStatement
Pretrained-Read
Pretrained-Read
Azure AI 4.0
Azure AI 4.0
docTR
docTR
MinerU
MinerU
PyMuPDF
PyMuPDF
PyMuPDF-
Formatted
PyMuPDF-
Formatted
Pdfium
Pdfium

Prebuilt-
BankStatement
Pretrained-Read
Pretrained-Read
Azure AI 4.0
Azure AI 4.0
docTR
docTR
MinerU
MinerU
PyMuPDF
PyMuPDF
PyMuPDF-
Formatted
PyMuPDF-
Formatted
Pdfium
Pdfium

Published as a conference paper at ICLR 2026

Table 5 – Continued from previous page

OCR

GPT

Key Information Extraction - Exact Match Accuracy

Bank Name Acc Holder Acc Number Address Statement Date

gpt-4.1

71.43

100.00

100.00

100.00

100.00

PyMuPDF-
Formatted
Pdfium
Pdfium

gpt-4o-mini
gpt-4.1

Ours (template matching)

71.43
71.43
100.00

100.00
100.00
100.00

100.00
100.00
100.00

85.71
100.00
100.00

RHB Bank (10 Unique PDFs)

N/A

100.00

90.00

100.00

70.00

gpt-4o-mini
gpt-4.1
gpt-4o-mini
gpt-4.1
gpt-4o-mini
gpt-4.1
gpt-4o-mini
gpt-4.1
gpt-4o-mini
gpt-4.1
gpt-4o-mini

100.00
100.00
100.00
100.00
100.00
100.00
70.00
70.00
90.00
100.00
100.00

100.00
100.00
100.00
100.00
70.00
70.00
50.00
50.00
100.00
100.00
100.00

100.00
100.00
100.00
100.00
100.00
100.00
70.00
70.00
100.00
100.00
100.00

90.00
80.00
100.00
80.00
80.00
70.00
40.00
40.00
80.00
80.00
100.00

100.00
100.00
100.00

100.00

100.00
100.00
100.00
100.00
100.00
100.00
70.00
70.00
100.00
100.00
100.00

gpt-4.1

100.00

100.00

100.00

100.00

100.00

gpt-4o-mini
gpt-4.1

Ours (template matching)

70.00
100.00
100.00

100.00
100.00
100.00

100.00
100.00
100.00

80.00
80.00
100.00

100.00
100.00
100.00

Hong Leong Bank (9 Unique PDFs)

N/A

100.00

88.89

100.00

100.00

100.00

gpt-4o-mini
gpt-4.1
gpt-4o-mini
gpt-4.1
gpt-4o-mini
gpt-4.1
gpt-4o-mini
gpt-4.1
gpt-4o-mini
gpt-4.1
gpt-4o-mini

100.00
100.00
100.00
100.00
100.00
100.00
0.00
44.44
100.00
100.00
100.00

88.89
100.00
88.89
100.00
66.67
88.89
88.89
100.00
88.89
100.00
88.89

100.00
100.00
100.00
100.00
100.00
100.00
100.00
100.00
100.00
100.00
100.00

100.00
100.00
88.89
100.00
88.89
100.00
100.00
100.00
88.89
100.00
88.89

100.00
100.00
100.00
100.00
100.00
100.00
100.00
100.00
100.00
100.00
100.00

gpt-4.1

100.00

100.00

100.00

100.00

100.00

gpt-4o-mini
gpt-4.1

Ours (template matching)

100.00
100.00
100.00

88.89
100.00
100.00

100.00
100.00
100.00

44.44
100.00
100.00

100.00
100.00
100.00

AmBank (7 Unique PDFs)

Prebuilt-
BankStatement
Pretrained-Read
Pretrained-Read
Azure AI 4.0
Azure AI 4.0
docTR
docTR
MinerU
MinerU

N/A

100.00

85.71

100.00

100.00

100.00

gpt-4o-mini
gpt-4.1
gpt-4o-mini
gpt-4.1
gpt-4o-mini
gpt-4.1
gpt-4o-mini
gpt-4.1

100.00
100.00
100.00
100.00
100.00
100.00
0.00
0.00

100.00
100.00
100.00
100.00
100.00
100.00
100.00
100.00

100.00
100.00
100.00
100.00
100.00
100.00
42.86
42.86

Continued on next page

100.00
100.00
100.00
100.00
100.00
100.00
100.00
100.00

100.00
100.00
100.00
100.00
100.00
100.00
100.00
100.00

18

---

<!-- PAGE 19 -->

Published as a conference paper at ICLR 2026

OCR

GPT

PyMuPDF
PyMuPDF
PyMuPDF-
Formatted
PyMuPDF-
Formatted
Pdfium
Pdfium

gpt-4o-mini
gpt-4.1
gpt-4o-mini

gpt-4.1

gpt-4o-mini
gpt-4.1

Ours (template matching)

Table 5 – Continued from previous page

Key Information Extraction - Exact Match Accuracy

Bank Name Acc Holder Acc Number Address Statement Date

0.00
0.00
0.00

0.00

0.00
0.00
100.00

100.00
100.00
100.00

100.00
100.00
100.00

100.00
100.00
100.00

100.00
100.00
100.00

100.00

100.00

100.00

100.00

100.00
100.00
100.00

100.00
100.00
100.00

100.00
100.00
100.00

100.00
100.00
100.00

Table 6: Key information extraction similarity score grouped by bank across OCR and GPT config-
urations.

OCR

GPT

Key Information Extraction - NED Score

Bank Name Acc Holder Acc Number Address Statement Date

Maybank (10 Unique PDFs)

prebuilt-
bankStatement.us
pretrained-read
pretrained-read
Azure AI 4.0
Azure AI 4.0
MinerU
MinerU
PyMuPDF
PyMuPDF
pdfium
pdfium

N/A

GPT-4o-mini
GPT-4.1
GPT-4o-mini
GPT-4.1
GPT-4o-mini
GPT-4.1
GPT-4o-mini
GPT-4.1
GPT-4o-mini
GPT-4.1

Ours (template matching)

prebuilt-
bankStatement.us
pretrained-read
pretrained-read
Azure AI 4.0
Azure AI 4.0
MinerU
MinerU
PyMuPDF
PyMuPDF
pdfium
pdfium

N/A

GPT-4o-mini
GPT-4.1
GPT-4o-mini
GPT-4.1
GPT-4o-mini
GPT-4.1
GPT-4o-mini
GPT-4.1
GPT-4o-mini
GPT-4.1

Ours (template matching)

prebuilt-
bankStatement.us
pretrained-read
pretrained-read
Azure AI 4.0
Azure AI 4.0
MinerU
MinerU
PyMuPDF
PyMuPDF

N/A

GPT-4o-mini
GPT-4.1
GPT-4o-mini
GPT-4.1
GPT-4o-mini
GPT-4.1
GPT-4o-mini
GPT-4.1

100

100
100
100
100
100
100
100
100
100
100
100

69.09

92.63
100
100
100
85.14
70
100
90
100
100
100

Public Bank (9 Unique PDFs)

88.89

100
100
100
100
20.16
41.83
16.88
55.56
20.85
55.56
100

88.89

100
100
100
100
100
100
92.16
100
91.27
100
100

CIMB Bank (7 Unique PDFs)

71.43

100
100
100
100
5.04
0
71.43
71.43

73.91

100
100
100
100
100
100
100
100

19

100

100
100
100
100
90
90
100
100
100
100
100

100

100
100
100
100
100
100
100
100
100
100
100

70.68

100
100
100
100
96.43
100
100
100

100

82.01
100
87.24
100
27.41
66.36
100
100
100
100
100

98.60

99.74
98.60
98.60
98.60
100
100
98.60
100
98.60
100
100

99.77

98.51
98.51
97.59
100
98.51
100
98.51
100

100

100
100
100
100
100
100
100
100
10
10
100

31.94

100
100
100
100
100
100
100
100
100
100
100

42.86

98.21
100
98.21
100
100
100
98.21
100

Continued on next page

---

<!-- PAGE 20 -->

Published as a conference paper at ICLR 2026

OCR

pdfium
pdfium

GPT

GPT-4o-mini
GPT-4.1

Ours (template matching)

prebuilt-
bankStatement.us
pretrained-read
pretrained-read
Azure AI 4.0
Azure AI 4.0
MinerU
MinerU
PyMuPDF
PyMuPDF
pdfium
pdfium

N/A

GPT-4o-mini
GPT-4.1
GPT-4o-mini
GPT-4.1
GPT-4o-mini
GPT-4.1
GPT-4o-mini
GPT-4.1
GPT-4o-mini
GPT-4.1

Ours (template matching)

prebuilt-
bankStatement.us
pretrained-read
pretrained-read
Azure AI 4.0
Azure AI 4.0
MinerU
MinerU
PyMuPDF
PyMuPDF
pdfium
pdfium

N/A

GPT-4o-mini
GPT-4.1
GPT-4o-mini
GPT-4.1
GPT-4o-mini
GPT-4.1
GPT-4o-mini
GPT-4.1
GPT-4o-mini
GPT-4.1

Ours (template matching)

prebuilt-
bankStatement.us
pretrained-read
pretrained-read
Azure AI 4.0
Azure AI 4.0
MinerU
MinerU
PyMuPDF
PyMuPDF
pdfium
pdfium

N/A

GPT-4o-mini
GPT-4.1
GPT-4o-mini
GPT-4.1
GPT-4o-mini
GPT-4.1
GPT-4o-mini
GPT-4.1
GPT-4o-mini
GPT-4.1

Ours (template matching)

Table 6 – Continued from previous page

Key Information Extraction - NED Score

Bank Name Acc Holder Acc Number Address Statement Date

71.43
71.43
100

100
100
100

RHB Bank (10 Unique PDFs)

100

100
100
100
100
70
70
93.03
100
79.09
100
100

90

100
100
100
100
55.69
50
100
100
100
100
100

100
100
100

100

100
100
100
100
70
70
100
100
100
100
100

Hong Leong Bank (9 Unique PDFs)

100

100
100
100
100
11.85
50.88
100
100
100
100
100

88.89

91.53
100
91.53
100
88.89
100
91.50
100
91.50
100
100

AmBank (7 Unique PDFs)

100

100
100
100
100
14.97
0
8.57
0
12.38
0
100

85.71

100
100
100
100
100
100
100
100
100
100
100

100

100
100
100
100
100
100
100
100
100
100
100

100

100
100
100
100
100
100
100
100
100
100
100

98.51
100
100

92.01

99.35
98.92
100
98.92
40
40
98.92
98.92
98.92
98.92
100

100

100
100
97.99
100
100
100
98.64
100
97.80
100
100

100

100
100
100
100
98.82
98.82
100
100
100
100
100

100
100
100

100

100
100
100
100
85
77.50
100
100
100
100
100

100

100
100
100
100
100
100
100
100
100
100
100

100

100
100
100
100
100
100
100
100
100
100
100

A.4 QUANTITATIVE RESULTS FOR TRANSACTION TABLE EXTRACTION

We evaluate transaction table extraction across the same six Malaysian banks. This task is substantially more
challenging than key information extraction, as it requires localizing table boundaries, parsing multi-page tables
with varying row counts, and correctly aligning five column types: date, description, debit, credit, and balance.
We report matching NED (tolerance for row-level alignment differences) in Table 8 and exact NED (strict
row-level matching) in Table 9, F1 scores for row detection in Table 7, and per-bank breakdowns in Tables 10
and 11.

Overall Performance. Our template matching approach achieves the highest or near-highest performance
across all metrics. On matching NED, it attains 100% on date and description columns, 91.12% on debit, 100%

20

---

<!-- PAGE 21 -->

Published as a conference paper at ICLR 2026

on credit, and 99.28% on balance, with an average of 98.08%. For exact NED, it achieves 98.08% (date),
98.35% (description), 99.87% (debit), 92.68% (credit), and 100% (balance). The F1 score is a perfect 100%
across all six banks, indicating that our method correctly identifies all transaction rows without false positives
or missed entries. The Surya + docTR pipeline with GPT-5-mini is the closest competitor, achieving 98.95%
matching NED on date and 96.94% average, with strong F1 scores (98.28–100%) across banks.

LLM-Based vs. End-to-End Approaches. Configurations using GPT-4.1 as the structuring model consis-
tently outperform those using GPT-4o-mini or smaller models. For instance, docTR + GPT-4.1 achieves 95.28%
matching NED on description, compared to 92.82% with GPT-4o-mini. The gap widens for numerical fields:
debit matching NED increases from 80.00% (GPT-4o-mini) to 98.78% (GPT-4.1) with docTR. This indicates
that larger language models are better at parsing ambiguous numerical formats (e.g., Malaysian Ringgit for-
matting with commas and periods) and handling multi-line transaction descriptions. Conversely, end-to-end
vision models show mixed results. While olmOCR achieves reasonable matching NED (77–91% per column),
its exact NED drops substantially (71–84%), indicating frequent minor character-level errors in numerical
fields. PPStructureV3 and PaddleOCR-VL (0.9B) demonstrate the weakest overall performance, particularly
on balance columns (43.79% and 53.44% matching NED respectively), likely due to their limited training on
Southeast Asian financial document formats.

Per-Bank Analysis. Performance varies across banks due to differences in statement formatting. Public Bank
statements, with their clean tabular layouts, achieve near-perfect extraction across most configurations (100%
matching NED for our method). In contrast, RHB Bank’s multi-column balance presentation and CIMB Bank’s
merged description cells present greater challenges, reducing baseline performance by 5–15% on average.
Hong Leong Bank statements with wrapped transaction descriptions cause the largest performance drops for
text-based extractors (PyMuPDF + GPT-4o-mini drops to 70.91% date matching NED). These bank-specific
challenges validate the need for robust extraction pipelines that can generalize across diverse formats.

F1 Score Analysis. Row-level detection accuracy, measured by F1 score (Table 7), reveals that our template
matching method and GPT-4.1-based configurations achieve near-perfect row detection (98–100% F1 across
banks). PaddleOCR-based methods show the most inconsistency, with F1 scores dropping to 10.26% on CIMB
Bank and 14.29% on Maybank for PPStructureV3, indicating catastrophic table detection failures on certain
bank formats. This highlights the unreliability of general-purpose table detection models for production de-
ployment on Malaysian bank statements without format-specific adaptation.

Table 7: F1 scores across all banks for transaction table extraction.

OCR

GPT

MBBE PBBE CIBB RHBB HLBB ARBK

N/A
prebuilt-layout
N/A
PPStructureV3
gpt-4o-mini
docTR
gpt-4.1
docTR
gpt-4.1-mini
docTR
gpt-4.1-nano
docTR
gpt-5-mini
docTR
gpt-5-mini (low)
docTR
gpt-5-nano
docTR
gpt-4o-mini
PyMuPDF
gpt-4.1
PyMuPDF
gpt-4o-mini
pdfium
gpt-4.1
pdfium
olmOCR-2-7B-1025
N/A
paddleOCR-VL (0.9B) N/A
Surya + docTR

100.00
99.58
81.60
97.41
89.47
92.12
10.26
80.89
23.19
70.97
87.37 100.00 85.34
98.81
88.70
98.95 100.00 100.00 100.00
90.09
91.38
88.24
96.93
81.14
97.30
83.19
93.26
73.87
96.49
71.79
91.21
100.00
96.43 100.00 94.74
96.34
90.35
85.96
100.00 95.70
97.01
98.95
91.89
68.38
66.67
98.20
87.18 100.00 76.19
89.26
100.00
98.95 100.00 99.58
92.59
96.43
80.77
88.52
79.65
98.25
98.81
99.47 100.00 98.31
83.64
98.20
83.84
63.04 100.00 73.68
95.65
64.16
22.22
17.89
61.18
100.00
99.15
98.28
gpt-5-mini (header) 100.00 100.00 98.96
100.00 100.00 100.00 100.00 100.00 100.00

93.67
14.29
92.73
96.04
91.74
36.11
98.71
94.64
94.64
94.64
94.69
94.17
93.75
87.93
61.31

Ours (template matching)

Table 8: Average per-column matching NED scores across all banks for transaction table extraction.

OCR

prebuilt-layout
PPStructureV3

GPT

N/A
N/A

Transaction Table Extraction - Matching NED Score

Date Desc Debit Credit

Balance

89.59 95.54 95.88 98.31
63.29 66.43 74.30 82.56

Continued on next page

94.15
43.79

21

---

<!-- PAGE 22 -->

Published as a conference paper at ICLR 2026

Table 8 – Continued from previous page

OCR

GPT

Transaction Table Extraction - Matching NED Score

Date Desc Debit Credit

Balance

gpt-4o-mini
gpt-4.1
gpt-4.1-mini
gpt-4.1-nano
gpt-5-mini
gpt-5-mini (low)
gpt-5-nano
gpt-4o-mini
gpt-4.1
gpt-4o-mini
gpt-4.1

docTR
docTR
docTR
docTR
docTR
docTR
docTR
PyMuPDF
PyMuPDF
pdfium
pdfium
olmOCR-2-7B-1025 N/A
N/A
paddleOCR-VL
(0.9B)
Surya + docTR

gpt-5-mini
(header)

86.41 92.82 80.00 86.07
88.05 95.28 98.78 96.65
88.48 94.60 86.79 91.85
84.87 78.88 80.02 78.64
86.64 97.73 93.74 94.78
80.44 95.81 87.10 90.94
82.65 90.68 79.31 80.05
88.45 93.29 86.07 88.72
87.13 95.79 97.80 97.08
88.48 91.66 85.32 87.95
88.08 92.85 99.69 95.03
82.94 90.53 82.58 79.08
79.18 58.94 69.44 80.67

98.95 98.59 90.79 97.97

Ours (template matching)

100

100

91.12

100

96.76
95.72
94.66
73.55
96.00
88.77
92.55
95.17
96.02
93.26
93.46
77.87
53.44

98.39

99.28

Table 9: Average per-column exact NED scores across all banks for transaction table extraction.

OCR

GPT

Transaction Table Extraction - Exact NED Score

Date Desc Debit Credit

Balance

N/A
N/A
gpt-4o-mini
gpt-4.1
gpt-4.1-mini
gpt-4.1-nano
gpt-5-mini
gpt-5-mini (low)
gpt-5-nano
gpt-4o-mini
gpt-4.1
gpt-4o-mini
gpt-4.1

prebuilt-layout
PPStructureV3
docTR
docTR
docTR
docTR
docTR
docTR
docTR
PyMuPDF
PyMuPDF
pdfium
pdfium
olmOCR-2-7B-1025 N/A
N/A
paddleOCR-VL
(0.9B)
Surya + docTR

gpt-5-mini
(header)

83.52 75.34 89.29 94.29
55.79 42.70 58.65 72.54
83.83 79.91 68.45 82.04
85.42 92.80 98.95 98.35
79.12 70.17 60.73 72.03
75.73 54.52 63.43 70.45
83.08 91.30 92.14 95.15
74.88 71.20 65.70 72.59
79.01 80.45 77.38 76.08
81.36 70.96 71.08 78.31
85.15 93.19 96.32 98.48
83.03 75.67 74.08 81.01
84.96 86.32 95.32 93.41
84.18 76.51 71.42 77.04
65.86 41.18 55.70 62.36

89.76 94.80 95.01 96.91

Ours (template matching)

98.08 98.35 99.87 92.68

78.31
47.19
78.35
96.72
57.50
56.24
94.97
59.10
84.06
72.17
94.33
77.19
88.13
71.11
40.58

94.65

100

Table 10: Transaction table extraction matching NED grouped by bank across OCR and GPT con-
figurations.

OCR

GPT

Transaction Table Extraction - Matching NED Score

Date Description Debit Credit Balance Average

Maybank (10 Unique PDFs)

prebuilt-layout
PPStructureV3
PyMuPDF
PyMuPDF

N/A
N/A
gpt-4o-mini
gpt-4.1

98.61
59.92
85.59
100.00

95.77
54.19
91.16
95.64

99.21
94.44
89.47
70.45
88.98
97.46
100.00 100.00

91.27
7.69
89.83
92.37

95.86
56.34
90.60
97.60

Continued on next page

22

---

<!-- PAGE 23 -->

Published as a conference paper at ICLR 2026

Table 10 – Continued from previous page

OCR

GPT

Transaction Table Extraction - Matching NED Score

Date Description Debit Credit Balance Average

gpt-4o-mini
pdfium
gpt-4.1
pdfium
olmOCR-2-7B-1025
N/A
paddleOCR-VL (0.9B) N/A
gpt-5-mini
Surya + docTR
gpt-4o-mini
docTR
gpt-4.1
docTR
gpt-4o-mini
docTR
gpt-4.1
docTR
olmOCR-2-7B-1025
N/A
paddleOCR-VL (0.9B) N/A
Surya + docTR

83.90
81.92
100.00
83.90
97.46
85.59
94.12
85.59
95.60
73.37
90.63
gpt-5-mini (header) 100.00
100.00

Ours (template matching)

90.02
57.24
98.39
93.39
93.96
93.39
93.28
92.80
92.16
85.79
60.63
100.00
100.00

Public Bank (10 Unique PDFs)

N/A
prebuilt-layout
N/A
PPStructureV3
gpt-4o-mini
PyMuPDF
gpt-4.1
PyMuPDF
gpt-4o-mini
pdfium
gpt-4.1
pdfium
olmOCR-2-7B-1025
N/A
paddleOCR-VL (0.9B) N/A
gpt-5-mini
Surya + docTR
gpt-4o-mini
docTR
gpt-4.1
docTR
gpt-4o-mini
docTR
gpt-4.1
docTR
olmOCR-2-7B-1025
N/A
paddleOCR-VL (0.9B) N/A
Surya + docTR

100.00
98.40
89.06
70.49
92.98
88.57
62.41
44.64
46.67
98.51
70.69
98.53
78.12
67.62
89.49
gpt-5-mini (header) 100.00
100.00

Ours (template matching)

100.00
73.61
91.60
81.92
97.75
70.10
95.35
99.20
93.36
91.00
86.21
90.00
71.88
71.74
64.53
100.00
100.00

CIMB Bank (10 Unique PDFs)

N/A
prebuilt-layout
N/A
PPStructureV3
gpt-4o-mini
PyMuPDF
gpt-4.1
PyMuPDF
gpt-4o-mini
pdfium
gpt-4.1
pdfium
N/A
olmOCR-2-7B-1025
paddleOCR-VL (0.9B) N/A
gpt-5-mini
Surya + docTR
gpt-4o-mini
docTR
gpt-4.1
docTR
gpt-4o-mini
docTR
gpt-4.1
docTR
olmOCR-2-7B-1025
N/A
paddleOCR-VL (0.9B) N/A
Surya + docTR

gpt-5-mini (header)

Ours (template matching)

96.94
45.25
90.57
97.92
96.74
95.60
100.00
93.81
100.00
92.55
97.92
93.39
98.95
94.74
54.91
97.94
100.00

98.50
59.69
85.03
97.91
92.53
70.81
99.86
94.98
98.85
85.97
97.92
80.17
99.29
100.00
58.73
100.00
100.00

prebuilt-layout
PPStructureV3
PyMuPDF
PyMuPDF
pdfium
pdfium

RHB Bank (10 Unique PDFs)

N/A
N/A
gpt-4o-mini
gpt-4.1
gpt-4o-mini
gpt-4.1

71.36
16.10
89.39
89.39
86.57
89.41

80.45
45.22
94.97
98.87
98.57
89.03

88.14
61.02
99.15
91.53
98.31
92.37
95.80
92.37
99.16
92.31
55.79
90.66
90.66

96.61
37.85
99.15
98.31
99.15
97.46
98.32
96.61
98.32
88.46
70.53
100.00
100.00

90.62
90.62
96.00
96.00
85.94
82.81
81.97
100.00
87.72
87.72
78.57
81.43
94.83
100.00
98.21
98.21
86.67
88.33
89.55
89.55
86.21
93.10
89.71
88.24
71.88
100.00
63.49
87.30
94.07
97.46
100.00 100.00
100.00 100.00

95.92
66.49
71.03
97.92
75.00
87.33
93.68
79.38
70.83
79.09
97.92
79.03
98.95
85.26
77.46
97.94
96.21

94.29
48.36
66.67
94.74
88.89
88.14

100.00
48.65
71.03
97.92
78.26
86.67
93.68
83.51
69.79
78.18
97.92
79.03
100.00
85.26
77.46
97.94
100.00

100.00
71.31
87.72
100.00
100.00
94.92

88.14
22.03
95.76
93.22
89.83
93.22
91.60
92.37
89.92
78.46
50.53
99.83
99.25

100.00
66.00
93.75
81.97
98.25
81.43
93.10
100.00
95.00
92.54
86.21
89.71
71.88
47.62
55.93
100.00
100.00

95.92
8.11
100.00
100.00
96.74
61.33
100.00
93.81
100.00
92.73
100.00
84.68
98.95
94.74
9.83
98.96
97.18

78.57
17.21
100.00
100.00
95.56
100.00

89.36
52.01
98.49
92.07
95.74
92.41
94.62
91.95
95.03
83.68
65.62
98.10
97.98

96.25
86.00
88.63
83.27
92.88
80.02
89.14
88.05
82.01
92.23
84.48
91.24
78.75
67.55
80.30
100.00
100.00

97.45
45.64
83.53
98.33
87.85
80.35
97.45
89.10
87.90
85.70
98.33
83.26
99.23
92.00
55.68
98.56
98.68

84.93
39.64
87.75
96.60
93.92
92.30

Continued on next page

23

---

<!-- PAGE 24 -->

Published as a conference paper at ICLR 2026

Table 10 – Continued from previous page

OCR

GPT

Transaction Table Extraction - Matching NED Score

Date Description Debit Credit Balance Average

N/A
olmOCR-2-7B-1025
paddleOCR-VL (0.9B) N/A
gpt-5-mini
Surya + docTR
gpt-4o-mini
docTR
gpt-4.1
docTR
gpt-4o-mini
docTR
gpt-4.1
docTR
olmOCR-2-7B-1025
N/A
paddleOCR-VL (0.9B) N/A
Surya + docTR

gpt-5-mini (header)

Ours (template matching)

89.42
89.54
91.05
89.39
89.39
89.58
89.39
91.46
70.39
96.61
100.00

98.28
97.91
72.65
98.44
98.87
97.09
98.99
93.84
14.09
93.22
100.00

93.33
85.00
81.54
75.38
56.58
59.21
100.00 100.00
100.00 100.00
91.38
91.38
100.00 100.00
62.50
59.72
60.16
35.16
86.36
91.53
100.00
89.39

Hong Leong Bank (10 Unique PDFs)

N/A
prebuilt-layout
N/A
PPStructureV3
gpt-4o-mini
PyMuPDF
gpt-4.1
PyMuPDF
gpt-4o-mini
pdfium
gpt-4.1
pdfium
olmOCR-2-7B-1025
N/A
paddleOCR-VL (0.9B) N/A
gpt-5-mini
Surya + docTR
gpt-4o-mini
docTR
gpt-4.1
docTR
gpt-4o-mini
docTR
gpt-4.1
docTR
olmOCR-2-7B-1025
N/A
paddleOCR-VL (0.9B) N/A
Surya + docTR

gpt-5-mini (header)

Ours (template matching)

78.98
70.12
70.91
78.80
73.09
71.58
76.31
70.74
70.02
71.70
78.98
71.85
75.82
70.42
69.65
99.16
100.00

98.54
71.14
94.57
97.32
92.71
90.91
94.52
92.94
87.27
92.91
98.46
92.67
95.99
92.57
59.63
98.32
100.00

AmBank (10 Unique PDFs)

N/A
prebuilt-layout
N/A
PPStructureV3
gpt-4o-mini
PyMuPDF
gpt-4.1
PyMuPDF
gpt-4o-mini
pdfium
gpt-4.1
pdfium
olmOCR-2-7B-1025
N/A
paddleOCR-VL (0.9B) N/A
gpt-5-mini
Surya + docTR
gpt-4o-mini
docTR
gpt-4.1
docTR
gpt-4o-mini
docTR
gpt-4.1
docTR
N/A
olmOCR-2-7B-1025
paddleOCR-VL (0.9B) N/A
Surya + docTR

91.67
89.92
92.94
91.67
97.62
82.11
91.67
100.00
90.70
92.94
91.67
91.95
90.59
100.00
100.00
gpt-5-mini (header) 100.00
100.00

Ours (template matching)

100.00
94.73
99.58
100.00
96.02
95.17
100.00
96.42
97.98
98.04
100.00
97.25
98.80
99.24
96.00
100.00
100.00

100.00 100.00
95.52
76.87
78.95
75.19
100.00 100.00
92.06
88.10
78.03
72.73
87.69
84.62
88.80
84.00
70.13
62.99
60.14
70.63
100.00 100.00
65.47
75.54
100.00 100.00
75.94
74.44
79.57
61.28
78.08
98.32
100.00
78.80

100.00 100.00
94.38
87.64
95.29
95.29
100.00 100.00
96.43
92.86
89.47
95.79
100.00 100.00
95.29
94.12
95.35
98.84
95.29
96.47
100.00 100.00
95.40
95.40
100.00 100.00
98.82
96.47
92.86
98.81
100.00
91.67
100.00
91.67

88.33
73.85
93.42
100.00
100.00
100.00
100.00
56.94
14.06
95.58
99.74

99.16
80.60
96.99
100.00
95.24
76.52
100.00
77.60
80.52
93.71
98.32
92.81
100.00
89.47
97.45
96.36
99.48

100.00
83.15
100.00
100.00
94.05
100.00
98.81
94.12
96.51
98.82
100.00
100.00
100.00
100.00
92.86
99.58
100.00

90.87
83.64
74.58
97.57
97.65
93.88
97.68
72.89
38.77
92.66
97.83

95.34
78.85
83.32
95.22
88.24
77.95
88.63
82.82
74.19
77.82
95.15
79.67
94.36
80.57
73.51
94.05
95.65

98.33
89.96
96.62
98.33
95.39
92.51
98.10
95.99
95.88
96.31
98.33
96.00
97.88
98.91
96.11
98.25
98.33

24

---

<!-- PAGE 25 -->

Published as a conference paper at ICLR 2026

Table 11: Transaction table extraction exact NED grouped by bank across OCR and GPT configu-
rations.

OCR

GPT

Transaction Table Extraction - Exact NED Score

Date Description Debit Credit Balance Average

Maybank (10 Unique PDFs)

N/A
prebuilt-layout
N/A
PPStructureV3
gpt-4o-mini
PyMuPDF
gpt-4.1
PyMuPDF
gpt-4o-mini
pdfium
gpt-4.1
pdfium
olmOCR-2-7B-1025
N/A
paddleOCR-VL (0.9B) N/A
Surya + docTR

75.71
24.25
74.34
87.49
75.77
84.64
70.45
57.59
gpt-5-mini (header) 90.07
90.07

Ours (template matching)

78.84
57.78
66.66
87.89
71.55
77.7
73.71
41.18
99.16
99.24

Public Bank (10 Unique PDFs)

N/A
prebuilt-layout
N/A
PPStructureV3
gpt-4o-mini
PyMuPDF
gpt-4.1
PyMuPDF
gpt-4o-mini
pdfium
gpt-4.1
pdfium
olmOCR-2-7B-1025
N/A
paddleOCR-VL (0.9B) N/A
Surya + docTR

gpt-5-mini (header)

Ours (template matching)

94.39
91.39
89.17
72.14
94.44
75.14
93.52
82.15
100
100

25.27
15.05
67.78
89.91
64.97
79.91
48.11
21.84
99.46
100

CIMB Bank (10 Unique PDFs)

N/A
prebuilt-layout
N/A
PPStructureV3
gpt-4o-mini
PyMuPDF
gpt-4.1
PyMuPDF
gpt-4o-mini
pdfium
gpt-4.1
pdfium
olmOCR-2-7B-1025
N/A
paddleOCR-VL (0.9B) N/A
Surya + docTR

88.69
32.12
90.77
98.81
84.63
97.62
95.56
33.01
gpt-5-mini (header) 91.09
91.43

Ours (template matching)

85.53
38.08
75.35
97.27
65.63
90.02
98.32
78.28
83.2
95.22

RHB Bank (10 Unique PDFs)

prebuilt-layout
N/A
PPStructureV3
N/A
PyMuPDF
gpt-4o-mini
PyMuPDF
gpt-4.1
pdfium
gpt-4o-mini
pdfium
gpt-4.1
N/A
olmOCR-2-7B-1025
paddleOCR-VL (0.9B) N/A
Surya + docTR

73.66
49.35
84.02
84.02
84.02
84.02
84.02
87.3
gpt-5-mini (header) 88.19
84.02

Ours (template matching)

66.77
21.28
79.69
88.69
87.71
73.51
90.75
12.56
97.42
99.53

81.19
39.86
60.56
90.91
70.56
78.6
62.73
61.99
100
100

85.36
82.74
68.39
93.33
67.97
100
85.71
79.17
100
100

87.94
50.24
76.47
98.41
71.48
93.33
85.95
66.51
77.55
100

86.36
63.21
97.22
100
91.94
100
78.05
31.12
92.5
100

Hong Leong Bank (10 Unique PDFs)

prebuilt-layout
PPStructureV3
PyMuPDF
PyMuPDF
pdfium
pdfium
olmOCR-2-7B-1025

N/A
N/A
gpt-4o-mini
gpt-4.1
gpt-4o-mini
gpt-4.1
N/A

77.05
51.35
63.65
76.82
65.3
76.71
63.84

95.7
48.21
56.72
95.36
66.6
97.58
57.34

94.87
33.54
41.78
95.24
46.33
100
31.29

93.02
84.39
73.39
97.41
76.25
86.95
78.11
71.1
100
100

89.82
90.28
85.42
96.67
85.56
84
65.81
81.74
100
100

90.48
41.41
82.75
98.41
73.49
89.52
85.95
66.5
89.8
100

92.42
81.24
97.22
100
91.94
100
76.67
34.84
91.67
100

100
59.51
43.37
98.41
62.65
100
61.15

71.99
13.33
40
82.31
50
63.08
53.68
49.21
100
100

41.94
30.28
70.47
90
70.2
80
48.26
51.48
100
100

83.18
23.41
90.86
100
78.42
85.71
93.62
28.57
70.68
100

72.73
49.23
100
100
100
100
76.67
26.13
98.61
100

100
67.87
55.28
93.65
64.54
100
64.43

80.15
43.92
62.99
89.20
68.83
78.19
67.74
56.21
97.85
97.86

67.36
61.95
76.25
88.41
76.63
83.81
68.28
63.28
99.89
100

87.16
37.05
83.24
98.58
74.73
91.24
91.88
54.58
82.47
97.33

78.39
52.86
91.63
94.54
91.12
91.5
81.23
38.39
93.68
96.71

93.53
52.09
52.16
91.9
61.08
94.86
55.61

Continued on next page

25

---

<!-- PAGE 26 -->

Published as a conference paper at ICLR 2026

Table 11 – Continued from previous page

OCR

GPT

Transaction Table Extraction - Exact NED Score

Date Description Debit Credit Balance Average

paddleOCR-VL (0.9B) N/A
Surya + docTR

gpt-5-mini (header)

Ours (template matching)

46.95
77.6
78.33

47.44
95.51
99.47

76.48
100
100

83.72
100
100

AmBank (10 Unique PDFs)

N/A
prebuilt-layout
N/A
PPStructureV3
gpt-4o-mini
PyMuPDF
gpt-4.1
PyMuPDF
gpt-4o-mini
pdfium
gpt-4.1
pdfium
olmOCR-2-7B-1025
N/A
paddleOCR-VL (0.9B) N/A
Surya + docTR

91.61
86.27
86.18
91.61
93.99
91.61
97.71
88.17
gpt-5-mini (header) 91.61
91.61

Ours (template matching)

99.91
75.79
79.54
100
97.58
99.18
90.81
45.76
94.03
100

100
82.53
82.04
100
96.19
100
84.76
18.92
100
100

100
83.96
87.69
100
96.19
100
94.52
36.28
100
100

86.88
98.61
100

100
75.27
76.4
100
100
100
90
1.19
100
100

68.3
94.34
95.56

98.3
80.77
82.37
98.32
96.79
98.16
91.56
38.07
97.13
98.32

A.5 LATENCY AND COST ANALYSIS

Practical deployment of bank statement extraction systems requires careful consideration of processing latency
and operational cost. We provide latency measurements for both key information extraction (Table 12) and
transaction table extraction (Table 13), along with cost analysis for table extraction (Table 14). All latency
measurements are reported in seconds per document, decomposed into OCR processing time and GPT inference
time where applicable.

Table 12: Latency analysis for key information extraction (seconds).

OCR

GPT

OCR

GPT

Total

Min. Avg. Max. Min. Avg. Max. Min. Avg. Max.

3.26
2.87
1.71
1.42
0.63
5.20

6.07
5.15
3.41
2.35
1.31
7.59

Prebuilt-BankStatement.us N/A
Pretrained-Read
Pretrained-Read
Azure AI 4.0
Azure AI 4.0
docTR
docTR
MinerU
MinerU
PyMuPDF
PyMuPDF
PyMuPDF-Formatted
PyMuPDF-Formatted
Pdfium
Pdfium

0.88 1.70 3.64
0.59 0.96 4.16
1.12 1.71 3.41
0.63 1.09 3.65
1.00 1.75 5.49
0.54 0.94 2.93

N/A N/A N/A N/A N/A N/A 5.26
2.52
2.34
2.37
1.86
1.34
3.58

9.28 17.27
7.90
4.96
gpt-4o-mini 1.64
7.07
3.83
gpt-4.1
1.61
5.01
3.34
gpt-4o-mini 1.03
5.50
2.72
gpt-4.1
1.01
6.51
2.38
gpt-4o-mini 0.32
gpt-4.1
8.56
6.13
2.96
gpt-4o-mini 28.69 32.18 38.72 1.27 2.05 3.62 30.10 34.24 41.88
33.51 44.32 55.03 0.83 1.18 8.40 34.38 45.50 60.62
gpt-4.1
0.97
3.92
0.95 1.85 3.89
gpt-4o-mini 0.00
0.04
0.57
1.47
0.56 0.80 1.46
0.00
gpt-4.1
0.04
0.87
6.10
0.85 1.50 6.08
gpt-4o-mini 0.01
0.05
0.55
1.39
0.53 0.72 1.36
gpt-4.1
0.00
0.06
4.92
0.97
0.95 1.84 4.91
gpt-4o-mini 0.00
0.09
1.67
0.03
0.00
0.55
0.54 0.85 1.66
gpt-4.1
0.01
0.01 N/A N/A N/A 0.01
0.01

1.86
0.81
1.53
0.74
1.86
0.86
0.01

0.02
0.01
0.02
0.02
0.02
0.01
0.01

Ours (template matching)

Key Information Extraction Latency. The latency profiles for key information extraction (Table 12) re-
veal substantial variation across pipeline configurations. Text-based extractors (PyMuPDF, Pdfium) achieve
near-instantaneous OCR processing (0.01–0.02s average), with total latency dominated by the GPT inference
component. PyMuPDF + GPT-4.1 achieves the lowest average total latency at 0.81 seconds, followed by
PyMuPDF-Formatted + GPT-4.1 at 0.74 seconds. Our template matching method averages 0.01 seconds per
document, making it the fastest configuration overall while eliminating dependency on external APIs. Cloud-
based OCR solutions introduce higher latency: Pretrained-Read averages 2.87–3.26 seconds for OCR alone,
while MinerU exhibits the highest latency at 34–45 seconds average due to its computationally intensive doc-
ument understanding pipeline. The Prebuilt-BankStatement endpoint (Azure’s turnkey solution) averages 9.28
seconds total but does not expose separate OCR/GPT components. DocTR presents an interesting trade-off:
its OCR component is fast (0.63s average with GPT-4o-mini) but increases substantially with GPT-4.1 (5.20s),
suggesting that the rendering and image preparation step scales with downstream model expectations.

26

---

<!-- PAGE 27 -->

Published as a conference paper at ICLR 2026

Table 13: Latency analysis for transaction table extraction (seconds).

OCR

GPT

OCR

GPT

Total

Min. Avg. Max. Min. Avg. Max. Min. Avg. Max.

N/A
N/A
gpt-4o-mini
gpt-4.1
gpt-4.1-mini
gpt-4.1-nano
gpt-5-mini
gpt-5-mini (low)
gpt-5-nano
gpt-4o-mini
gpt-4.1
gpt-4o-mini
gpt-4.1

prebuilt-layout
PPStructureV3
docTR
docTR
docTR
docTR
docTR
docTR
docTR
PyMuPDF
PyMuPDF
pdfium
pdfium
olmOCR-2-7B-1025 N/A
paddleOCR-VL (0.9B) N/A
Surya + docTR

7.59

4.58

6.33
3.80

N/A N/A N/A N/A 2.56
7.46
N/A N/A
N/A N/A N/A N/A 15.26 40.95 98.17
N/A N/A
1.32 6.41 14.83 2.30
1.59
15.93
1.18
0.78
0.89 11.03 153.16 2.07 11.92 153.50
1.56
0.89
0.34
13.51
1.12 5.38 12.47 2.08
1.60
0.96
0.57
1.02
7.31
1.76
6.59
1.14 3.13
0.67
0.28
1.19 11.15 24.54 54.64 11.70 25.27 55.20
0.74
0.30
1.48 5.77 11.64 2.74
1.54
12.93
1.07
0.66
7.47 31.51 60.65 8.07 32.38 61.23
1.76
0.87
0.36
12.13
1.08 4.97 12.12 1.09
0.04
0.01
0.00
0.84 10.72 157.78 0.85 10.72 157.79
0.05
0.01
0.00
1.36 6.19 16.90 1.39
0.04
16.92
0.02
0.00
0.04
0.77 11.17 155.22 0.79 11.19 155.23
0.00
0.02
N/A N/A
N/A N/A N/A N/A 42.58 104.45 175.93
23.20 150.10 341.10 N/A N/A N/A 23.20 150.10 341.10
9.19
0.13

7.34
1.67
0.13 N/A N/A N/A 0.10

0.75 1.19

4.28
0.11

2.51
0.11

1.85

6.84

6.21

4.98

Ours (template matching)

gpt-5-mini (header) 2.26
0.10

Transaction Table Extraction Latency. Table extraction latency (Table 13) is generally higher than key infor-
mation extraction due to the increased complexity of parsing multi-page tabular data. Our template matching
method achieves the fastest average total latency at 0.11 seconds, followed by the Surya + docTR pipeline at
2.51 seconds and the prebuilt-layout API at 4.58 seconds. GPT-4.1-based configurations exhibit high latency
variance with maximum processing times reaching 153–158 seconds for certain documents, likely caused by
complex multi-page statements that require extensive reasoning. In contrast, GPT-4o-mini configurations main-
tain more consistent latency (4.97–7.59s average), suggesting that smaller models, while less accurate, provide
more predictable processing times suitable for latency-sensitive production environments. End-to-end vision
models exhibit the highest latencies: PaddleOCR-VL averages 150.10 seconds and olmOCR averages 104.45
seconds, making them impractical for real-time processing of bank statements. GPT-5-mini and GPT-5-nano,
despite being more recent models, show elevated latency (25.27s and 32.38s respectively) due to their reasoning
token overhead.

Cost Analysis. The cost analysis for table extraction (Table 14) reveals that per-document processing costs
vary from effectively zero (template matching, open-source models) to $0.01 per PDF (GPT-4.1, GPT-5-mini).
GPT-4.1-nano offers the lowest API cost at $0.03 total, while GPT-4.1 incurs the highest at $0.53 due to
its larger prompt and completion token consumption. Reasoning-capable models (GPT-5-mini, GPT-5-nano)
allocate a significant proportion of their completion cost to reasoning tokens ($0.35 out of $0.43 for GPT-5-
mini), which explains both their improved accuracy and higher cost. The Surya + docTR with GPT-5-mini
(header) configuration achieves the best cost-accuracy balance among API-dependent solutions at only $0.02
total cost while achieving 96.94% average matching NED. Our template matching approach and open-source
models (olmOCR, PaddleOCR-VL) incur no API cost, though they require local compute resources. For a
production deployment processing hundreds of bank statements daily, the cumulative cost difference between
configurations becomes significant, making the template matching approach advantageous for high-throughput
scenarios.

Table 14: Cost analysis for transaction table extraction (USD). Total cost represents aggregate API
expenses across all documents in the evaluation dataset where Per PDF shows the average cost per
individual document.

OCR

GPT

Token Cost

Cost Breakdown

Prompt Completion Total Reasoning Comp - Reason Per PDF

prebuilt-layout
PPStructureV3
docTR
docTR
docTR
docTR

N/A
N/A
gpt-4o-mini
gpt-4.1
gpt-4.1-mini
gpt-4.1-nano

N/A
N/A
N/A
0.19
0.04
0.01

N/A
N/A
N/A
0.34
0.07
0.02

N/A
N/A
N/A
0.53
0.11
0.03

N/A
N/A
N/A
N/A
N/A
N/A

N/A
N/A
N/A
N/A
N/A
N/A

N/A
N/A
N/A
0.01
0.00
0.00

Continued on next page

27

---

<!-- PAGE 28 -->

Published as a conference paper at ICLR 2026

OCR

GPT

Token Cost

Cost Breakdown

Prompt Completion Total Reasoning Comp - Reason Per PDF

Table 14 – Continued from previous page

gpt-5-mini
gpt-5-mini (low)
gpt-5-nano
gpt-4o-mini
gpt-4.1
gpt-4o-mini
gpt-4.1

docTR
docTR
docTR
PyMuPDF
PyMuPDF
pdfium
pdfium
olmOCR-2-7B-1025 N/A
paddleOCR-VL (0.9B) N/A
Surya + docTR

gpt-5-mini (header)

Ours (template matching)

0.02
0.02
0.00
0.01
N/A
N/A
N/A
N/A
N/A
0.01
N/A

0.43
0.08
0.24
0.03
N/A
N/A
N/A
N/A
N/A
0.01
N/A

0.45
0.10
0.25
0.04
N/A
N/A
N/A
N/A
N/A
0.02
N/A

0.35
0.00
0.23
N/A
N/A
N/A
N/A
N/A
N/A
0.00
N/A

0.08
0.08
0.02
N/A
N/A
N/A
N/A
N/A
N/A
0.01
N/A

0.01
0.00
0.00
0.00
N/A
N/A
N/A
N/A
N/A
0.00
N/A

Note:
1. N/A indicate data not available or not applicable.
2. Prompt = Prompt token cost.
3. Completion = Completion token cost.
4. Reasoning = Reasoning token cost.
5. Comp - Reason = Completion cost minus reasoning cost.
6. Per PDF = Average cost per PDF document.
7. OCR = OCR processing time in seconds.
8. GPT = GPT inference time in seconds.
9. Total = Total processing time in seconds.

A.6 ABLATION STUDIES FOR CREDIT SCORING

A.6.1 CREDIT SCORE DISTRIBUTION

We evaluate the score distribution of our Logistic Regression baseline across three feature set configurations:
application information only, bank statement only, and blended. Figure 4–6 present score distributions for
good accounts (green) and bad accounts (red), with Earth Mover’s Distance (EMD) quantifying distributional
divergence as a measure of discriminatory power.

Application Information: Figure 4 shows limited separation between good and bad accounts when using
application features alone. The histogram and kernel density estimation (KDE) curves reveal good accounts
clustering at higher scores (mean of 665.7) and bad accounts at lower scores (mean of 641.5), yielding an EMD
of 24.11. This modest divergence indicates reasonable but constrained discriminatory power from traditional
application data.

Bank Statement: Figure 5 demonstrates markedly improved separation when using bank statement features.
Good accounts exhibit a mean score of 699.2 while bad accounts concentrate near 625.7. The EMD increases
to 74.48, a 3.1× improvement over application information alone, reflecting the stronger signal provided by
transactional cash flow indicators. This result suggests bank statement-derived features create more distinct
risk profiles.

Blended: Figure 6 displays the combined model using both application and bank statement features. This
blended approach achieves the strongest distribution separation, with good accounts centered near 708.4 and
bad accounts near 612.6. The EMD reaches 96.84, a 4.0× improvement over application information and
1.3× over bank statement alone, demonstrating that combining feature sources enhances discriminatory power
beyond either individual approach. The progressive EMD improvement from 24.11 (application only) to 74.48
(bank statement) to 96.84 (blended) also shows that transaction-derived features are the primary driver of score
separation between good and bad accounts.

A.6.2 REJECTED CASES ANALYSIS

Problem Statement. Credit scoring models trained exclusively on approved applicants suffer from selection
bias, as they capture only the subset of the applicant population deemed acceptable by historical underwriting
decisions (Ehrhardt et al., 2021). This creates a two-fold problem: (1) the model lacks evidence about how
rejected applicants would have performed if approved, leading to potential underestimation of actual portfolio
risk, and (2) the model’s decision boundary is calibrated to a biased distribution rather than the true applicant

28

---

<!-- PAGE 29 -->

Published as a conference paper at ICLR 2026

Figure 4: Score distribution for the application information model. Good accounts (green) cluster
at higher scores (mean 665.7) while bad accounts (red) concentrate lower (mean 641.5). EMD of
24.11 indicates moderate discriminatory power.

population (Insights, 2024). To address this limitation, we conducted rejected cases analysis on 264 rejected
loan applicants.

Methodology. This analysis applies the scorecard model developed on approved applicants to the rejected
population, generating predicted risk scores without retraining. This non-augmentation approach allows us
to assess model consistency and identify systematic characteristics that distinguish rejected from approved
applicants. By scoring rejected applicants with the existing model, we can observe whether rejection decisions
align with predicted risk profiles and understand the key financial behaviors driving rejection decisions.

Applying our Logistic Regression scorecard to these rejected applicants reveals that 96.97% (256 of 264) are
classified as high risk, 3.03% (8 of 264) as medium risk, and 0% as low risk (Table 15). This distribution
demonstrates strong alignment between the consulting firm’s rejection decisions and our model’s risk assess-
ment, validating that the scorecard accurately captures the underlying risk factors that motivated original re-
jection decisions. Critically, no rejected applicant scored in the low-risk category, indicating that rejection
decisions were not arbitrary but rather grounded in genuine credit risk indicators observable in transaction data.

Table 15: Risk Distribution of Rejected Loan Applicants via Scorecard Model Prediction

Risk Level High Risk Medium Risk Low Risk
0 (0.00%)
Count

256 (96.97%)

8 (3.03%)

Implications. This analysis serves two critical purposes. First, it validates that our scorecard model generalizes
consistently to the rejected population, with rejection decisions strongly aligned to predicted risk. Second, it
provides evidence that bank statements contain sufficient cash flow signal to identify high-risk applicants,
and that rejection decisions were data-driven rather than arbitrary. The finding that all rejected applicants are
either high or medium risk, with a concentration in high risk, suggesting that the consulting firm’s historical
underwriting was appropriately conservative and that our model captures the legitimate risk factors underlying
those decisions. These results strengthen confidence that the scorecard can be reliably extended to new applicant
populations with limited credit history.

29

---

<!-- PAGE 30 -->

Published as a conference paper at ICLR 2026

Figure 5: Score distribution for the bank statement model. Bank statement-derived cash flow indi-
cators produce stronger separation with good accounts (mean 699.2) and bad accounts (mean 625.7)
showing clearer divergence. EMD of 74.48 (3.1× higher than application information) reflects the
discriminatory advantage of transactional data.

Figure 6: Score distribution for the blended model. Combining application and bank statement
features achieves the strongest separation with good accounts (mean 708.4) and bad accounts (mean
612.6) showing maximal divergence. EMD of 96.84 (4.0× higher than application information
alone) demonstrates complementary value of both feature sources.

30

---

<!-- PAGE 31 -->

Published as a conference paper at ICLR 2026

B DEPLOYMENT AND OPERATIONAL FRAMEWORK

The sixth phase of CRISP-DM focuses on the deployment of the proposed cash flow underwriting workflow
in a production environment. This workflow is designed to leverage verifiable transaction data to enable trans-
parent and evidence-based credit decisions while establishing a continuous feedback cycle for data collection,
model retraining, and performance monitoring within existing core banking systems. To support this, a robust
machine learning operations framework is implemented to structure the end-to-end pipeline into five key stages.
Lastly, an integrated credit scoring framework is introduced to provide comprehensive risk evaluation for both
established and new-to-credit MSMEs.

B.1 DATA INGESTION

The pipeline begins when bank statements are received. Extraction modules parse and structure the raw trans-
action data using OCR and layout analysis techniques. This process transforms unstructured documents into
a standardized tabular format suitable for downstream processing. The ingestion stage also performs integrity
verification and data validation checks to ensure document authenticity.

B.2 FEATURE ENGINEERING AND FEATURE STORE

Following ingestion, structured data are fed into the feature engineering module, which computes transaction-
derived and behavioral features. These features are time-stamped, versioned, and stored in a centralized reposi-
tory. The feature store provides a single source of truth for both training and inference, ensuring the same logic
used to generate historical features is consistently applied to new applicants in real time. This design guarantees
reproducibility, prevents feature skew, and supports traceability across model iterations.

B.3 CONTINUOUS INTEGRATION (CI)

The CI pipeline automates model retraining and validation prior to integration into the production registry. It
is triggered by two primary events: (1) a predefined schedule (e.g., annually) when new labeled data become
available from the core banking system, and (2) alerts from the monitoring system indicating potential model
or data drift. Upon activation, the pipeline retrieves the latest versioned feature set and ground truth labels,
retrains the model, and evaluates its performance against the current production model using predefined and
consistent evaluation metrics.

B.4 MODEL REGISTRY AND CONTINUOUS DEPLOYMENT (CD)

If the retrained model demonstrates superior performance, it is automatically versioned and stored in the model
registry. The CD process then packages the validated model into a containerized microservice and deploys it as
a secure REST API endpoint. To ensure reliability and minimize production risk, a canary deployment strategy
is applied, initially routing a small fraction of live traffic to the new model for performance validation before
full-scale rollout.

B.5 CONTINUOUS MONITORING AND FEEDBACK LOOP

Once the bank statement-based credit scoring model is deployed, it operates within a Champion-Challenger
framework (Kim et al., 2019) to enable continuous performance optimization. The Champion model serves as
the current production baseline, while one or more Challenger models are periodically retrained on the latest
data and evaluated in parallel. Model performance is continuously monitored and compared across predefined
metrics. When a Challenger consistently outperforms the Champion, the system automatically notifies des-
ignated bank officers to review the results and promote the new model to production. This approach ensures
sustained model improvement, robustness, and operational stability.

B.6

INTEGRATED CREDIT SCORING FRAMEWORK

In production, the cash flow underwriting system functions as an integrated decision engine embedded within
the lending process. Upon submission of bank statements, AI modules automatically extract and structure
the raw data using OCR and natural language processing models. The processed data then undergoes fraud
detection, cash flow analysis, and network analytics to generate transaction-derived features and credit scores
for MSME applicants. The existing bureau-based scorecard, designed for borrowers with established credit
histories, operates in parallel with the newly developed cash flow-based model. Each model independently
produces a risk rating, and a risk override mechanism ensures conservative decisioning; if either model indicates
higher risk, the final classification adopts that rating. This framework provides a transparent, evidence-based,

31

---

<!-- PAGE 32 -->

Published as a conference paper at ICLR 2026

and data-driven approach to MSME credit assessment using adaptive, explainable AI scoring. It also extends
financial access to new-to-credit businesses through verifiable transaction data.

C LIMITATIONS AND FUTURE WORK

This work has several limitations that should be addressed in future research. First, the dataset comprises 611
loan applications from a single Malaysian consulting firm. While the dataset represents real-world production
data collected over a two-year period, the sample size is constrained by the practical realities of MSME lend-
ing in emerging markets, where data availability remains limited due to stringent data privacy and regulatory
requirements. Future work should validate these findings across multiple institutions and larger datasets as
additional MSME lending data become available.

Second, the class imbalance in our dataset (518 non-default vs. 93 default cases) reflects the natural distribution
observed in real-world lending portfolios, where the majority of borrowers successfully repay their loans. While
this imbalance poses modeling challenges, it accurately reflects real-world credit risk settings. In this work,
we addressed this limitation through appropriate model selection, WOE-based feature engineering, and careful
evaluation using AUROC, which is robust to class imbalance. It is important to note that class imbalance is not
a limitation that can be fully eliminated, but rather an inherent characteristic of credit scoring datasets. As credit
assessment models improve and lending decisions become more accurate, successful repayment rates increase,
thereby maintaining or even intensifying this natural imbalance. Nevertheless, future studies could explore
advanced resampling techniques or cost-sensitive learning methods to further enhance model performance on
minority class prediction.

Third, while we describe multiple AI modules for document processing, fraud detection, and transaction anal-
ysis within the proposed end-to-end cash flow underwriting workflow, the evaluation focuses on overall credit
scoring performance rather than the effectiveness of individual modules. However, detailed module-level as-
sessment is constrained by the use of proprietary methods and sensitive operational data that cannot be pub-
licly disclosed. Future work utilizing synthetic or anonymized data could enable more granular module-level
analysis and benchmarking. Additionally, future research could explore formalizing these modules as fully au-
tonomous agents, enabling the development of a multi-agent credit scoring architecture with clearer inter-agent
responsibilities and interactions.

Fourth, the proposed workflow has been deployed in a production environment with one Malaysian consulting
firm. While this demonstrates real-world applicability, broader validation across different lending institutions,
regulatory environments, and MSME segments would strengthen the generalizability of our findings. Further
research is needed to systematically integrate the proposed cash flow underwriting workflow with existing
credit assessment systems that rely on behavioral and credit bureau data, ensuring coherent and robust risk
evaluation. Additionally, longitudinal studies examining model performance stability across economic cycles
would provide valuable insights into the temporal robustness and adaptability of bank statement-based features
under varying macroeconomic conditions.

32

<!-- MARKITDOWN CONVERSION -->

<!-- Full MarkItDown conversion for formatting fidelity. -->

PublishedasaconferencepaperatICLR2026
| AI-BAAM: |             | AI-DRIVEN |     |      | BANK | STATEMENT |     |     | ANALYT- |
| -------- | ----------- | --------- | --- | ---- | ---- | --------- | --- | --- | ------- |
|          | ALTERNATIVE |           |     | DATA |      | MALAYSIAN |     |     | MSME    |
| ICS      | AS          |           |     |      |      | FOR       |     |     |         |
| CREDIT   | SCORING     |           |     |      |      |           |     |     |         |
ChunChetNg∗∗,ZhenHaoChu∗,JiaYuLim,
YinYinBoon,WeiZengLow&JinKhyeTan
AILens,KualaLumpur,Malaysia
chunchet.ng@ailensgroup.com
6202 rpA 6  ]TS.nif-q[  4v66061.0152:viXra
ABSTRACT
Despiteaccountingfor96.1%ofallbusinessesinMalaysia(DepartmentofStatis-
ticsMalaysia,2025),accesstofinancingremainsoneofthemostpersistentchal-
|     | lenges faced | by Micro, | Small, | and Medium |     | Enterprises | (MSMEs). |     | Newly es- |
| --- | ------------ | --------- | ------ | ---------- | --- | ----------- | -------- | --- | --------- |
tablishedbusinessesareoftenexcludedfromformalcreditmarketsastraditional
|     | underwriting | approaches | rely | heavily | on credit | bureau | data. | This study | investi- |
| --- | ------------ | ---------- | ---- | ------- | --------- | ------ | ----- | ---------- | -------- |
gatesthepotentialofbankstatementdataasanalternativedatasourceforcredit
|     | assessmenttopromotefinancialinclusioninemergingmarkets. |     |     |     |     |     |     | First,wepropose |     |
| --- | ------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --------------- | --- |
acashflow-basedunderwritingpipelinewhereweutilizebankstatementdatafor
|     | end-to-end | data extraction |     | and machine | learning | credit | scoring. | Second, | we in- |
| --- | ---------- | --------------- | --- | ----------- | -------- | ------ | -------- | ------- | ------ |
troduceanoveldatasetof611loanapplicantsfromaMalaysianconsultingfirm.
Third,wedevelopandevaluatecreditscoringmodelsbasedonapplicationinfor-
|     | mationandbanktransaction-derivedfeatures. |      |           |          |        | Empiricalresultsdemonstratethat |               |     |          |
| --- | ----------------------------------------- | ---- | --------- | -------- | ------ | ------------------------------- | ------------- | --- | -------- |
|     | incorporating                             | bank | statement | features | yields | substantial                     | improvements, |     | with our |
bestmodelachievinganAUROCof0.806onvalidationset,representinga24.6%
|     | improvement | over models |      | using application |         | information   | only. | Finally, | we will     |
| --- | ----------- | ----------- | ---- | ----------------- | ------- | ------------- | ----- | -------- | ----------- |
|     | release the | anonymized  | bank | transaction       | dataset | to facilitate |       | further  | research on |
MSMEfinancialinclusionwithinMalaysia’semergingeconomy.
1 INTRODUCTION
Financial inclusion remains a pressing challenge in emerging markets, where a significant portion
of the population lacks sufficient credit history to access formal lending. According to the Secu-
ritiesCommissionMalaysia(Malaysia,2025), MSMEsareestimatedtocontributearound60%of
Malaysia’sgrossdomesticproduct. Despitetheirsignificantcontributions, MSMEsremainunder-
servedbyfinancialinstitutionsintermsofaccesstofinancing,givingrisetoanestimatedMYR90
billionfundinggap(Corporation,2017). OnefundamentalissueisthatmanyMSMEsdonothave
lendinghistory. Traditionalcreditassessmentreliesheavilyoncreditbureaudatasuchasrepayment
history,outstandingobligations,andpastdelinquencies. Whiletraditionalcreditmodelsworkwell
forestablishedbusinesses,theyhaveshortcomingsforMSMEswiththincreditfiles. First,theyare
inherentlybackward-lookingandfocusonpastrepaymentbehaviorratherthancurrentorforward-
lookingcapacitytorepay.Second,theyoverlookreal-timefinancialsignalsoroperationaldynamics
thatcouldmoreaccuratelyreflectafirm’spresentfinancialhealth. Third,theyomitalternativeindi-
catorsofcreditworthiness,suchascashflowconsistency,receivablesandpayablespatterns,digital
transactions,andbehavioralmetricsfromdailyfinancialactivity.
On the other hand, bank statements represent an up-to-date and verifiable source of financial be-
havior that also captures income regularity, spending patterns, and cash flow stability. This study
explorestheuseofMalaysianbankstatementtransactionsasalternativedataforcreditscoringmodel
developmentandevaluatestheirpredictivevalueforMSMEs. Theobjectivesareasfollows:
• To propose a cash flow-based underwriting workflow capable of ingesting and analyzing
banktransactiondataforcreditdecisioningtonarrowtheMSMEfinancinggap.
∗Theseauthorscontributedequally.
1

PublishedasaconferencepaperatICLR2026
Figure1: Proposedend-to-endworkflowusingbankstatementtransactiondataforcreditscoring.
• Tointroducethefirst-everMalaysianbankstatementdatasetbasedonMSMEloans.
• To evaluate the performance of machine learning–based credit scoring models trained on
theproposedbankstatementtransactiondataset,andtoexaminethefeasibilityandpredic-
tivepoweroftransaction-derivedfeaturesinassessingMSMEcreditworthiness.
2 RELATED WORK
Withtherecenttechnologicaladvancementsinmachinelearningalgorithms, theresearchcommu-
nityhasrecognizedthelimitationsofexistingtraditionalcreditscoringmethods(Gote&Mendhe,
2024). SuchstudiesarecrucialforenhancingfinancialinclusionofMSMEsinemergingmarkets,
whereMSMEsareoftenthebackboneofeconomicgrowthdespitehavinglimitedaccesstofinanc-
ing(Elebe&Imediegwu,2021). Assuch,alternativedatafromnon-traditionalsourcesthatarenot
includedinstandardcreditbureaufilesarebeingusedforcreditscoring(Group,2024).
Limitations of Traditional Credit Scoring. Traditional credit scoring models used by financial
institutionsprimarilyrelyoncreditbureaudatasuchaspaymenthistory,amountofdebt,andother
indicators (Shivhare, 2024). Unfortunately, reliance on such data creates a high entry barrier for
MSMEs in emerging economies where they usually lack audited financial statements or loan ser-
vicing history required by financial institutions (Courchane & Baines, 2020; Elebe & Imediegwu,
2021). ThisleadsMSMEstobeperceivedashigh-riskapplicantsandresultsinaperpetualcycleof
financialexclusionthatseverelylimitstheirgrowthpotential(Courchane&Baines,2020). Besides,
traditionalmethodsfailtocapturerecentcashflowstatusofMSMEs,whichcanbeanaccuraterep-
resentation of financial health (Elebe & Imediegwu, 2021). A recent survey indicates that 58% of
financialinstitutionsfeellessconfidenttomakedecisionsbasedontraditionalcreditdataonly(Wat-
terson,2024). Theincreasingdissatisfactionmotivatestheurgentneedtousealternativedatafora
moreadaptiveandinclusivecreditassessment(Gote&Mendhe,2024).
CreditScoringwithAlternativeData. Inordertoovercomethelimitationsoftraditionalmethods,
creditunderwritingusingalternativedatahasemergedasanewapproach(Gote&Mendhe,2024;
Watterson,2024;Ngwenya,2024). Forinstance,mobilenetworkdataareusedforcreditscoringin
Africa(Ngwenya,2024;Gathu,2020)andbankaccounttransactionsareusedforcashflowunder-
writinginconsumerlending(Watterson,2024). Recentstudiessuggestthatincorporatingtransac-
tionaldatacanimprovepredictiveaccuracyandexpandcredittounderservedpopulations(Djeundje
etal.,2021). Forinstance,researchhasshownthatretailtransactiondatacanhelpconstructalterna-
tivecreditscores(Leeetal.,0). AstudyexaminingtwoIndianfinancialtechnology(FinTech)firms
foundthattransactionaldatafromplatformactivityworkedaswellascreditbureaudatainpredict-
ingcreditworthinessandimprovedthepredictiveaccuracywhencombinedwithbureaudata(Caire
&Vidal,2024). However,theadoptionofalternativedatainMSMElendinginMalaysiaremainsat
anearlystage,withlimitedresearchfocusfromtheindustry.
Machine Learning Models in Credit Scoring. Machine learning (ML) models have proven to
be highly effective in processing financial data to produce accurate credit scores (Bu¨cker et al.,
2022; Gunnarsson et al., 2021; Trivedi, 2020). These include statistical models like Logistic Re-
gression(LR),NaiveBayes(NB),andensemblemethodslikeRandomForest,AdaBoost,andGra-
2

PublishedasaconferencepaperatICLR2026
dientBoosting(Bu¨ckeretal.,2022;Trivedi,2020). Forexample,aRandomForestmodelachieved
the best performance on Taiwanese credit card data (Abbas & Hussein, 2024). A NB classifier
performed well on a highly imbalanced dataset from a New Zealand lender, especially when un-
declared features derived from bank statements were incorporated to supplement application form
data(Bunkeretal.,2016). GiventhepositiveimpactofMLmodelsincreditscoring,weaimtoim-
provefinancialinclusionofMalaysianMSMEsthroughproposedcashflowunderwritingworkflow.
AgenticWorkflowinCreditScoring. ThedeploymentofLargeLanguageModel(LLM)-powered
agentic systems marks a major advancement in automated credit scoring, loan approval, and cus-
tomerriskprofilingwithinfinancialservices(Okpalaetal.,2025;Ali,2025;Paleti,2024). Recent
agentic frameworks have demonstrated strong performance in complex model risk management
tasks, including credit card approval and portfolio risk modeling (Okpala et al., 2025). Beyond
these use cases, agentic workflows are transforming banking by enabling adaptive credit profiling
and predictive loan approvals, thereby improving risk assessment accuracy through bias detection
andintelligentdecisionautomation(Paleti,2024). Similarapproacheshavebeenexploredinmort-
gage lending, where machine learning-driven agents streamline underwriting and accelerate credit
evaluation (Chitturi, 2025). However, existing methods remain limited in production deployment
andlackafullygrounded,end-to-endworkflowforMSMEcreditscoring.
3 BANK STATEMENT CASH FLOW UNDERWRITING
The proposed cash flow underwriting workflow enhances traditional credit underwriting by inte-
grating bank statement-derived features into the credit decision-making process. As illustrated in
Figure1,theworkflowconsistsofsixmainmodules,eachservingadistinctpurpose. Byautomat-
ingmanualextractionandanalysistasks,itshortensturnaroundtimeandimprovesoperationaleffi-
ciencywhileexpandingcreditaccessforthin-fileMSMEswholacksufficientcreditbureauhistory.
Key Information Extraction Module. The key information extraction module employs Optical
Character Recognition (OCR) to extract essential fields from bank statements, including the bank
name,accountnumber,accountholdername,address,andstatementdate.Theseattributesarecross-
validatedacrossstatementstoensureaccuratedocumentownershipverification. Thesefieldsenable
theenginetolinkmultipleaccountsbelongingtothesamebusinessentity,providingaholisticview
ofitsfinancialactivityandcashflowacrossmultiplebankaccounts.
TransactionTableExtractionModule. Thetransactiontableextractionmodulelocalizesanddig-
itizestabulartransactiondatausingOCRandlayoutanalysis. Itidentifiestableheaders,thenmaps
rowsandcolumnstoextracttransactiondate, description, debit, credit, andbalanceamounts. Ad-
ditional pre-processing handles merged cells, page breaks, and format inconsistencies to preserve
data fidelity. The resulting structured transaction records serve as critical inputs for downstream
analyticalmodulesthatevaluatetransactionpatternsandaccount-levelcashflowdynamics.
Fraud Analysis Module. The fraud analysis module leverages Computer Vision and rule-based
techniques to detect tampered or falsified bank statements. For each document, it examines both
visual and metadata cues such as inconsistent font styles or sizes, altered layouts, metadata mis-
matches,andabnormalpixel-levelpatternsthatmayindicatedigitalediting. Oncepotentialtamper-
ingisidentified,theaffectedstatementsareautomaticallyflaggedandreturnedtobankofficersfor
manualverification. Thismoduleprovidesanadditionallayerofsecurityandassurancewithinthe
underwritingworkflow,ensuringthatonlyauthenticbankstatementsareanalyzedforcreditscoring.
NetworkAnalysisModule. Thenetworkanalysismoduleconstructstransactionnetworksfromthe
extractedtransactiondatatouncoverrelationshipsamongsendersandbeneficiariesacrossmultiple
bank accounts. Using graph-based algorithms, it maps transaction linkages to detect circular fund
flows,kitingactivities,andtransferstoblacklistedorinterrelatedentities. Thismodulealsoquanti-
fiesnetworkconnectivityandtransactiondensitytorevealabnormalmoneymovementpatternsthat
mayindicatefraudulentactivityorfinancialdistress,therebyenhancingoverallriskassessment.
CashFlowAnalysisModule. Thecashflowanalysismoduleevaluatescashflowstatusbasedon
theinflowsandoutflowsextractedfromtransactionrecords. ItthenappliesNaturalLanguagePro-
cessingtoinfertransactionintentandclassifyentriesintomeaningfulcategoriesbasedontheirde-
scriptions. Usingtheseclassifications,thismodulegroupsrelatedtransactionstoidentifyspending
andreceiptpatterns,enablingthedetectionofoutliersthatdeviatefromtypicalcashflowbehavior.
3

PublishedasaconferencepaperatICLR2026
It also computes key metrics such as average, highest, and lowest balances, quantifying cash flow
healthandprovidingpredictivefeaturesforcreditscoring.
Data&ScoringLayer(CashFlowUnderwriting). Thislayerstorestheanalyzeddataandengi-
neeredfeaturesinasecuredatabasetoensuretraceability,regulatorycompliance,andauditability.
Thestoreddataarethenpreprocessed,andfeatureselectionmethodsareappliedtoretainthemost
informative variables. Using the selected features, a predictive model is trained to estimate the
probabilityofdefaultandclassifycreditrisk.
4 BANK STATEMENT TRANSACTION DATASET
Table1: StatisticsofMSMEloanapplicationdatasets.
Split Non-Default Default Total
Train(60%) 310 56 366
Validation(40%) 208 37 245
Overall 518 93 611
Transaction data derived from bank statements represents a valuable alternative resource for cash
flow underwriting. To the best of our knowledge, no published studies have examined the use of
bankstatementdataforcreditassessmentofMSMEsinMalaysia.Incollaborationwithaconsulting
firm,weconstructedthefirstMalaysianbankstatementsdatasettoaddressthisgap.
This study adopts the Cross-Industry Standard Process for Data Mining (CRISP-DM) frame-
work(Chapmanetal.,2000)asthemethodologicalbasis. CRISP-DMisawidelyrecognizedpro-
cessmodelforsystematicFinTechstudies(Cheng,2023;Rawat,2023;daRocha&deSousaJunior,
2010)andcomprisessixmainphases,i.e.,businessunderstanding,dataunderstanding,dataprepa-
ration, modeling, evaluation, and deployment. The first phase involves evaluating bank statement
transaction data as an alternative source for MSME credit risk assessment in Malaysia. The sec-
ond phase focuses on constructing the proposed dataset of 611 MSME loan applicants. Summary
statisticsofthedatasetarepresentedinTable1.
Dataset Distribution and Preparation. The dataset is split into training (60%) and validation
(40%)setsusingstratifiedrandomsamplingtopreserveclassdistribution.Amongallapplicants,518
haveagoodcreditrecord,while93haveahistoryofdefault. Eachapplicant’srecordcontainstwo
maincomponents:applicationforminformationsubmittedduringtheloanapplicationprocess(e.g.,
demographic and business characteristics) and bank statement transaction data capturing detailed
inflowsandoutflowsoverasix-monthperiod.Thethirdphaseinvolvesdatapreparationandincludes
several key tasks: (1) cleaning and de-duplicating data to ensure consistency, (2) fixing missing
values,standardizingtransactioncategories,andvalidatingdataintegrityacrossallrecords,and(3)
derivingfeaturesandvariablesfromtransactiondata,suchasdeterminingcashflowstability,deposit
regularity,andbalancevolatility.
Dataset Masking. All personally identifiable information was anonymized prior to analysis. To
preserveconfidentiality,thefeaturesaregroupedintoapplicationinformation(7features)andbank
statementfeatures(10features). Thespecificfeaturecalculationscannotbedisclosedduetoanon-
disclosure agreement and all bank statement features are derived solely from bank statement data.
FurtherdetailsonethicaluseofdataareprovidedinSection8.
5 TRANSACTION DATA-BASED CREDIT SCORING
The fourth phase of CRISP-DM in this study employs Logistic Regression on application form
and bank transaction data derived from our dataset as the baseline credit scoring model. LR is
widelyadoptedincreditriskmodelingduetoitsinterpretability,statisticalrobustness,andcapacity
toestimatetheprobabilityofdefault(Bu¨ckeretal.,2022;Trivedi,2020;Abbas&Hussein,2024;
Bunkeretal.,2016). Toensurethatonlyinformativepredictorsareretained, featureselectionand
transformationareguidedbytheWeightofEvidence(WOE)andInformationValue(IV)framework,
which are widely used in credit risk modeling for quantifying the predictive power of individual
4

PublishedasaconferencepaperatICLR2026
variables (Ngwenya, 2024). In practice, each feature is divided into discrete intervals based on
suitable thresholds determined from the data. These bins allow the calculation of WOE and IV at
thegrouplevel,whichmakesthemeasiertointerpretwithinaLRmodel. Thefollowingnotationis
usedtoquantifythedistributionofdefaultsandnon-defaultsacrossfeaturebins:
Lety ∈ {0,1}indicatedefault(y = 1)ornon-default(y = 0)forapplicanti. Thetotalnumber
| i   |     | i   |     | i   |     |     |
| --- | --- | --- | --- | --- | --- | --- |
ofdefaultandnon-defaultapplicantsisdefinedas:
|     |     | n        |     |     | n        |     |
| --- | --- | -------- | --- | --- | -------- | --- |
|     |     | (cid:88) |     |     | (cid:88) |     |
|     | N = | I(y =1), |     | N = | I(y =0), | (1) |
|     | b   | i        |     | g   | i        |     |
|     |     | i=1      |     |     | i=1      |     |
Furthermore,letx ij denotethevalueoffeaturej forapplicanti. Foragivenfeaturej,supposeitis
dividedintoK disjointbins{B ,...,B }; thenthecorrespondingcountswithineachbinare
|     | j   | j1  | jKj |     |     |     |
| --- | --- | --- | --- | --- | --- | --- |
definedas:
n
(cid:88) I(x )I(y
|     |     | n = | ∈B  | =1), |     |     |
| --- | --- | --- | --- | ---- | --- | --- |
|     |     | bjk | ij  | jk i |     |     |
i=1
(cid:88) n
I(x )I(y
|     |     | n gjk = | ij ∈B | jk i =0). |     | (2) |
| --- | --- | ------- | ----- | --------- | --- | --- |
i=1
Thedistributionofdefaultsandnon-defaultsineachbinis:
|     |         | n    |     |         | n    |     |
| --- | ------- | ---- | --- | ------- | ---- | --- |
|     | Dist(b) | bjk, |     | Dist(g) | gjk. |     |
|     |         | =    |     |         | =    | (3) |
|     |         | jk N |     |         | jk N |     |
|     |         | b    |     |         | g    |     |
WeightofEvidence(WOE).Firstly,wecalculatetheWOEforbinkoffeaturej using:
(cid:32) Dist(g)(cid:33)
|     |     |             |         | (cid:18) n | /N (cid:19) |     |
| --- | --- | ----------- | ------- | ---------- | ----------- | --- |
|     |     |             | jk      | gjk        | g           |     |
|     |     | WOE jk =log | =log    |            | .           | (4) |
|     |     |             | Dist(b) | n          | /N          |     |
|     |     |             | jk      | bjk        | b           |     |
A positive WOE indicates that bin B is more common among non-default cases, suggesting
|     | jk  | jk  |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- |
lowerrisk,whereasanegativevalueindicatesahigherlikelihoodofdefault.OnceWOEiscomputed
foreachbin,theoverallpredictivestrengthoffeaturej canthenbesummarizedbyitsIV.
InformationValue(IV).Secondly,wemeasuretheIVoffeaturej byaggregatingtheWOEacross
allrespectivebins:
Kj
|     |     | (cid:16) |                 | (cid:17) |      |     |
| --- | --- | -------- | --------------- | -------- | ---- | --- |
|     |     | (cid:88) | Dist(g)−Dist(b) |          |      |     |
|     |     | IV j =   |                 | WOE      | jk . | (5) |
jk jk
k=1
AlargerIV j indicatesstrongerdiscriminatorypoweroffeaturej betweendefaultandnon-default
classes. Inthisstudy,IVservesasbothafeature-rankingcriterionandaninterpretabilitymeasure,
helpingtoidentifythemostinfluentialtransaction-levelindicatorsforcreditworthiness. Following
industrypractice(Siddiqi,2017),weadoptthecommonlyusedinterpretivethresholds: IV < 0.02
(notpredictive),0.02≤IV<0.1(weak),0.1≤IV<0.3(medium),0.3≤IV<0.5(strong),and
IV≥0.5(suspiciouslyhigh,suggestingpotentialdataleakage).
BinningofBankStatementFeatures. Specifically,weusedsupervisedmonotonicbinningtoob-
}Kj
tain{B jk forcontinuoustransaction-derivedvariables(e.g.,cashflowstability,balancevolatil-
k=1
ity) and sparse categorical variables (e.g., State/Location). Then, rare categories are grouped to
ensure that each bin contains sufficient observations of both default and non-default classes while
preserving monotonicity. Computations of WOE and IV are performed on training folds only to
avoiddataleakage.
6 EXPERIMENTS
FollowingthefifthphaseofCRISP-DM,weconductaseriesofexperimentstoevaluatetheeffec-
tiveness of the proposed cash flow underwriting workflow and the role of bank statement data in
enhancingMSMEcreditscoringperformance. Theexperimentsincludecomparativeanalyseswith
establishedmachinelearningmethodsanddetailedablationstudiesontransaction-derivedfeatures.
5

PublishedasaconferencepaperatICLR2026
6.1 IMPLEMENTATIONDETAILS
WebenchmarkthebaselineLogisticRegressionmodelagainstseveralwidelyusedmachinelearn-
ingmethods,includingRandomForest(RF)(Breiman,2001),GradientBoosting(GB)(Friedman,
2001), and AdaBoost (AB) (Schapire, 2013). All models are implemented in scikit-learn (scikit
learn,2025c;a;b;d). FortheresultsinSection6.2, modelsweretrainedwithdefaulthyperparame-
ters. In Section 6.3, hyperparameters were tuned using a randomized grid search with 50 trials to
ensure robustness. We evaluate model performance using the Area Under the Receiver Operating
CharacteristicCurve(AUROC)(Bradley,1997),whichmeasurestheabilitytodiscriminatebetween
defaultandnon-defaultcasesacrossvaryingthresholds. AnAUROCof0.5indicatesnodiscrimina-
tivepower(equivalenttorandomguessing),whereasavalueof1.0indicatesperfectdiscrimination.
Toensureinterpretabilityandsystematicanalysis,bothapplicationinformationandbankstatement
featuresaregroupedintotwocategories:
i AccountBehavior: logarithmicgrowthrateofaveragebalance,six-monthaverageaccountbal-
ance, change in 3-month minimum balance (recent), percent change in minimum balance vs
priorperiod,recent3-monthmaximumaveragebalance,anddebtrepaymentcapacity.
ii Business Demographics: business operational duration, geographic region, industry classifica-
tion(MSIC),totalboarddirectors,andminimumdirectorage.
This structured feature grouping facilitates clearer attribution of model performance to different
behavioral and demographic dimensions of MSME credit profiles. It also supports experimental
reproducibility, while respecting confidentiality constraints around proprietary feature derivations.
FurtherdetailsondeploymentandoperationalconsiderationsareprovidedinAppendixB.
6.2 QUANTITATIVERESULTS
Validation Performance. Quantitative results on the validation split are presented in Figure 2.
LogisticRegressionwithblendedfeaturesachievesthehighestvalidationAUROCof0.806,outper-
forming all ensemble methods across every feature set (GB: 0.664, RF: 0.678, AB: 0.680). This
consistentadvantageisattributabletothesmall,class-imbalancedtrainingset(310non-defaultvs.
56 default cases), where LR’s well-calibrated probabilities and lower variance outweigh the flexi-
bility of tree-based ensembles (Brown & Mues, 2012; Lessmann et al., 2015). The value of bank
statement data is evident across all algorithms. For LR, moving from application-only to bank
statement-onlyfeaturesyieldsagainof0.116AUROC(0.647→0.763),andblendingbothfeature
setsachievesafurtherimprovementto0.806,a24.6%relativegainoverapplication-only. Thispat-
ternholdsforensemblemethodsaswell,confirmingthatcashflowbehaviourcapturesdefaultrisk
dimensionsthatstaticapplicationattributesalonecannot.
Extraction Module Performance. Beyond credit scoring, we evaluate the upstream AI modules
responsible for bank statement data extraction, as their accuracy directly affects downstream fea-
ture quality. For key information extraction, we benchmark 15 OCR-GPT pipeline configurations
against our template matching approach across six Malaysian banks (Table 3 in Appendix). Our
method achieves perfect 100% exact match accuracy and Normalized Edit Distance (NED) score
acrossallfiveextractionfields(bankname,accountholder,accountnumber,address,andstatement
date),whereasthebest-performingbaseline(AzureAI4.0+GPT-4.1)reaches100%onfourfields
butdropsto94.82%onaddressextraction. Fortransactiontableextraction,weevaluate16configu-
rationsincludingrecentvision-languagemodels(Tables8and9). Ourtemplatematchingapproach
achieves the highest average matching NED of 98.08% and exact NED of 97.80% across all col-
umntypes. Theclosestcompetitor,SuryaParuchuri&Team(2025)+docTRMindee(2021)with
GPT-5-mini, attains 96.94% and 94.23% respectively. Notably, end-to-end vision models such as
olmOCR(Poznanskietal.,2025)andpaddleOCR-VL(Cuietal.,2025a)showsubstantiallylower
performanceonstructuredtableextraction, underscoringtheadvantageofspecializedpipelinede-
signsforfinancialdocuments. Thesegeneral-purposemodelsstrugglewiththehighlystructuredyet
bank-specificformattingofMalaysianbankstatements,particularlymulti-linetransactiondescrip-
tions, inconsistent date formats, and merged table cells that vary across institutions. Our template
matchingmethodsucceedsbecauseitexploitsthedeterministicandstandardizedlayoutswithineach
bank’sPDFformat,bypassingtheneedforLLMentirelyandthuseliminatingbotherrorpropaga-
tion and API dependency. Table 2 summarizes the performance of selected configurations across
6

PublishedasaconferencepaperatICLR2026
AUROC Across Algorithms, Feature Sets, and Data Splits
|     |     | Logistic Regression |     |     |     |     | Gradient Boosting |     |     |
| --- | --- | ------------------- | --- | --- | --- | --- | ----------------- | --- | --- |
1.0
|     |             | 0.821 | 0.850 | 0.806 |       |       |       |       |       |
| --- | ----------- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- |
| 0.8 |             | 0.763 |       |       |       |       |       |       |       |
|     |             |       |       |       |       |       | 0.705 |       | 0.720 |
|     | 0.672 0.647 |       |       |       |       |       |       |       | 0.664 |
|     |             |       |       |       | 0.578 |       |       | 0.599 |       |
| 0.6 |             |       |       |       |       | 0.519 |       |       |       |
0.4
0.2
0.0
CORUA Application Info Bank Statement Blended Application Info Bank Statement Blended
|     |     |               | Data Split: |     | Train | Validation |     |          |     |
| --- | --- | ------------- | ----------- | --- | ----- | ---------- | --- | -------- | --- |
|     |     | Random Forest |             |     |       |            |     | AdaBoost |     |
1.0
| 0.8 |             | 0.717 | 0.730 |       |       |     |       |       |             |
| --- | ----------- | ----- | ----- | ----- | ----- | --- | ----- | ----- | ----------- |
|     |             |       |       | 0.678 |       |     |       |       | 0.675 0.680 |
|     |             | 0.651 |       |       |       |     | 0.617 | 0.645 |             |
| 0.6 | 0.571 0.551 |       |       |       | 0.585 |     |       |       |             |
0.499
0.4
0.2
0.0
|     | Application Info | Bank Statement | Blended |     | Application Info |     | Bank Statement |     | Blended |
| --- | ---------------- | -------------- | ------- | --- | ---------------- | --- | -------------- | --- | ------- |
Feature Sets
Figure2: Evaluationresultsofallmodelsacrossdifferentfeaturecombinationsanddatasplits.
Table 2: Summary of extraction performance, latency, and cost for methods evaluated on key in-
formationandtransactiontableextractiontasks. Accuracyscoresareaveragedoverfivefields(key
info)andfivecolumntypes(table);F1isaveragedoversixbanks. Latencyistheaveragetotaltime
perdocument(seconds).TheproposedtemplatematchingmethodwasmeasuredonaMacBookAir
2025withM4chipand24GBunifiedmemory. CostisthetotalAPItokencostperdocument. Best
resultsareinbold;second-bestareunderlined. FullbreakdownsinAppendixTables3–14.
|        |     | KeyInformation |       | TableExtraction |       |       | Latency(s) |            | Cost(USD)  |
| ------ | --- | -------------- | ----- | --------------- | ----- | ----- | ---------- | ---------- | ---------- |
| Method |     | Exact          | NED   | Match.          | Exact | F1    | Key        | Table      | Table      |
|        |     | Match          | Score | NED             | NED   | Score | Info       | Extraction | Extraction |
docTR+GPT-4o-mini 91.87 99.20 88.41 78.52 92.16 2.38 7.59 N/A
| docTR+GPT-4.1 |     | 94.79 | 99.32 | 94.90 | 94.45 | 97.51 | 6.13 | 11.92 | 0.53 |
| ------------- | --- | ----- | ----- | ----- | ----- | ----- | ---- | ----- | ---- |
PyMuPDF+GPT-4o-mini 89.32 92.22 90.34 74.78 90.91 1.86 4.98 0.04
| PyMuPDF+GPT-4.1 |     | 93.23 | 93.86 | 94.76 | 93.49 | 97.64 | 0.81 | 10.72 | N/A |
| --------------- | --- | ----- | ----- | ----- | ----- | ----- | ---- | ----- | --- |
Pdfium+GPT-4o-mini 87.65 92.01 89.33 78.20 89.63 1.86 6.21 N/A
| Pdfium+GPT-4.1 |     | 93.57 | 94.20 | 93.82 | 89.63 | 95.66 | 0.86 | 11.19 | N/A |
| -------------- | --- | ----- | ----- | ----- | ----- | ----- | ---- | ----- | --- |
Ours(templatematching) 100.00 100.00 98.08 97.80 100.00 0.01 0.11 $0
bothextractiontasks. Fullper-bankbreakdowns,F1scores,anddetailedanalysisalongwithacom-
prehensivelatencyandcostanalysisacrossallconfigurationsareprovidedinAppendixA.5.
CostandLatencyAnalysis.OperationalefficiencyisakeyconsiderationforAI-BAAM.Wereport
latencyandcostmeasurementsacrossallconfigurationsinAppendixTables12,13,and14. Forkey
information extraction, our template matching method averages 0.01s per document with perfect
accuracy, orders of magnitude faster than the fastest LLM-based baseline (PyMuPDF (pymupdf,
2025)+GPT-4.1at0.81s). Fortableextraction,ourmethodaverages0.11scomparedto4.98sfor
PyMuPDF+GPT-4o-mini. Fortransactiontableextraction,text-basedpipelinessuchasPyMuPDF
+ GPT-4o-mini average under 5s, whereas end-to-end vision-language models require 104–150s.
AmongLLM-basedmethods, Surya+docTRwithGPT-5-mini($0.02)anddocTRwithGPT-4.1-
nano($0.03)arethemostcost-effective,whiledocTR+GPT-4.1incurs$0.53forthedataset. Our
templatematchingapproacheliminatesAPIcostsentirelywhilemaintainingsub-secondprocessing
latency,achievingthebestaccuracy–efficiencytrade-offforproductiondeployment.
7

PublishedasaconferencepaperatICLR2026
6.3 ABLATIONSTUDIES
ResultsinFigure3presentstheinformationvalueofindividualfeatures,rankedbydiscriminatory
power. Bankstatementfeaturesdominatethetoppositionswithlogarithmicgrowthrateofaverage
balance having the highest score of 0.484. In contrast, the strongest application information fea-
tureisbusinessoperationaldurationwithanIVof0.213, rankingfarbelowthetransaction-based
features. Thesefindingsreinforcethesuperiordiscriminatorystrengthofbankstatementfeaturesin
distinguishingdefaultfromnon-defaultoutcomes.
Furthermore,weconductedablationexperimentsbyprogressivelyremovingfeaturegroupstostudy
theirrelativeimportanceinMSMEscreditscoring. Weapplied5-foldcross-validationonthetrain-
ing split (366 samples) to reduce the risk that results are due to random chance and to increase
confidenceinmodelstability. FromresultsillustratedinFigure2,weobservethatLogisticRegres-
sionwithblendedfeaturesachievesthestrongestcross-validationAUROCof0.850,outperforming
GradientBoosting(0.720)andRandomForest(0.730). Whenconsideringbankstatementfeatures
alone,LRachievesavalidationAUROCof0.821,comparedto0.672foraccountinformationalone,
demonstrating a substantial uplift of 0.149 points. These results confirm that transactional data
providessignificantincrementalpredictivevalue. Acrossallfeatureconfigurationsanddatasplits,
LRconsistentlyoutperformstree-basedensembles. Moreover,modelsincorporatingbanktransac-
tiondataconsistentlyoutperformthoserelyingonapplicationinformationalone. Furtherstudiesof
thecreditscoredistributionforeachfeaturegroupaswellastheanalysisonrejectedcasescanbe
foundinAppendixA.6.1-A.6.2. Ingeneral,thesefindingsstronglysupportthehypothesisthatbank
statementtransactiondataofferssignificantpredictivepowerincreditriskassessmentforMSMEs
in Malaysia. While application form information provides some discriminatory power, the inclu-
sionofbanktransaction-basedfeaturessubstantiallyenhancesmodelperformance, reinforcingthe
effectivenessofAI-BAAM.LimitationsandfutureworkarediscussedinAppendixC.
Figure3: IVoffeaturesderivedfromapplicationinformationandbankstatementdata.
7 CONCLUSION
This study introduces bank statement transactions as alternative data for MSME credit scoring in
Malaysia and presents AI-BAAM, an end-to-end cash flow underwriting workflow spanning doc-
ument extraction, feature engineering, and predictive modeling. Empirical results confirm that
transaction-derived features capture dynamic financial behavior overlooked by traditional credit
models: models trained on bank transaction data alone substantially outperform those using only
application information, and combining both feature sets yields the highest predictive power. Be-
yondcreditscoring,webenchmarkover30OCRandLLMconfigurationsforkeyinformationand
transactiontableextractionacrosssixMalaysianbanks. Ourtemplatematchingapproachachieves
perfectaccuracyonkeyinformationfieldsandthehighestNEDandF1scoresontableextraction,
whileprocessingdocumentsinunder0.12secondswithzeroAPIcost. Incontrast,thebestLLM-
basedpipelinesrequire0.81-11.92secondsperdocumentandincuratotalof$0.53,andend-to-end
8

PublishedasaconferencepaperatICLR2026
vision-languagemodelsexhibit104-150secondslatencywithsubstantiallylowerextractionquality.
Thesefindingsdemonstratethatourtemplatematchingmethodoffersasuperioraccuracy-efficiency
trade-offovergeneral-purposeLLMpipelinesforMalaysianbankstatements.
8 ETHICAL USE OF DATA AND INFORMED CONSENT
Alldatausedinthisstudywereobtainedthroughaformaldata-sharingagreementwiththepartner-
ing Malaysian consulting firm. The dataset contains loan application records and bank statements
fromMSMEapplicantswhoconsentedtotheuseoftheirfinancialdataforcreditassessmentpur-
posesaspartoftheloanapplicationprocess. Allpersonallyidentifiableinformation,includingap-
plicantnames,nationalidentificationnumbers,bankaccountnumbers,andphysicaladdresses,was
masked or removed prior to analysis, as described in Section 4. Feature names were anonymized
and grouped into application information and bank statement features to prevent re-identification.
Thespecificfeaturederivationlogicisprotectedunderanon-disclosureagreementwiththelending
institution. Noindividual-levelpredictionsorriskscoresaredisclosedinthispaper,andallreported
results are presented in aggregate form. The anonymized dataset intended for public release will
undergo additional de-identification review to ensure compliance with Malaysia’s Personal Data
ProtectionAct2010(PDPA)andapplicableinstitutionaldatagovernancepolicies.
9 REPRODUCIBILITY
Thecompletemodelingpipeline,featureengineeringmethodology,andevaluationprotocolaredoc-
umentedinSections4–6.2. Allmachinelearningmodelsareimplementedusingscikit-learn(scikit
learn, 2025c;d;a;b), with hyperparameter configurations detailed in Section 6.2 and ablation set-
tingsinSection6.3. TheWOE/IV-basedfeaturetransformationandsupervisedmonotonicbinning
procedures are described formally in Section 4, and the feature groupings used in all experiments
are enumerated in Section 6.2. For the OCR and LLM benchmarks, the evaluated configurations
andsystemsetupsarereportedinAppendixA.3andAppendixA.4. Thedatasetusedinthisstudy
consists of real bank statements and loan records collected under a data-sharing agreement with a
Malaysianconsultingfirm. Asthedatacontainssensitivefinancialinformation,weareunabletore-
leasetherawrecordsduetocontractualobligationsandMalaysia’sPDPA.Weareworkingtowards
releasing an anonymized version pending a de-identification review, as described in Section 8. In
the meantime, researchers can replicate our workflow on their own bank statement data using the
step-by-stepmethodologydetailedthroughoutthepaperandappendix.
10 ACKNOWLEDGEMENT
WethanktheCradleFundandtheMicrosoftforStartupsprogramfortheirfundingsupport,which
madethisresearchpossible.WealsothanktheDocLab,DocSuite,andMLSuiteteamsatAILensfor
theircontributionsacrossdocumentprocessing,systemdevelopment,andmachinelearning,which
collectivelyshapedtheAI-BAAMpipelinepresentedinthiswork.
9

PublishedasaconferencepaperatICLR2026
REFERENCES
ElafAdelAbbasandNisreenAbbasHussein. Algorithmcomparisonfordataminingclassification:
Assessing bank customer credit scoring default risk. Jurnal Kejuruteraan, 36(5):1935–1944,
2024.
MohammadAsifAli. Efficientunderwritingusingagenticai. AvailableatSSRN5169848,2025.
Andrew P Bradley. The use of the area under the roc curve in the evaluation of machine learning
algorithms. Patternrecognition,30(7):1145–1159,1997.
LeoBreiman. Randomforests. Machinelearning,45(1):5–32,2001.
Iain Brown and Christophe Mues. An experimental comparison of classification algorithms for
imbalancedcreditscoringdatasets. Expertsystemswithapplications,39(3):3446–3453,2012.
Michael Bu¨cker, Gero Szepannek, Alicja Gosiewska, and Przemyslaw Biecek. Transparency, au-
ditability,andexplainabilityofmachinelearningmodelsincreditscoring. JournaloftheOpera-
tionalResearchSociety,73(1):70–90,2022.
RoryPBunker,WenjunZhang,andMAsifNaeem. Improvingacreditscoringmodelbyincorpo-
ratingbankstatementderivedfeatures. arXivpreprintarXiv:1611.00252,2016.
DeanCaireandMariaFernandezVidal.Leveragingtransactionaldataformicroandsmallenterprise
(mse) lending, March 2024. URL https://www.cgap.org/sites/default/files/
publications/Leveraging%20Transactional%20Data.pdf.
Pete Chapman, Julian Clinton, Randy Kerber, Colin Shearer Thomas Khabaza ands
Thomas Reinartz, and Ru¨diger Wirth. Crisp-dm 1.0 step-by-step data mining guide,
2000. URL https://www.kde.cs.uni-kassel.de/wp-content/uploads/
lehre/ws2012-13/kdd/files/CRISPWP-0800.pdf.
AijunCheng. Evaluatingfintechindustry’srisks: Apreliminaryanalysisbasedoncrisp-dmframe-
work. FinanceResearchLetters,55:103966,2023.
NaganarendarChitturi. Agenticartificialintelligence: Architecturalparadigmsandtransformative
impactofautonomousfinancialassistantsacrossthemortgagelendinglifecycle. JournalofCom-
puterScienceandTechnologyStudies,7(8):1155–1165,2025.
InternationalFinanceCorporation. MSMEFinanceGap: AssessmentoftheShortfallsandOppor-
tunitiesinFinancingMicro,Small,andMediumEnterprisesinEmergingMarkets. WorldBank,
Washington,D.C.,UnitedStates,2017.
MJ Courchane and AP Baines. The use of cash-flow data in underwriting
credit, October 2020. URL https://finreglab.org/wp-content/
uploads/2023/12/FinRegLab_2020-03-03_Research-Report_
The-Use-of-Cash-Flow-Data-in-Underwriting-Credit_
Market-Context-and-Policy-Analysis.pdf.
Cheng Cui, Ting Sun, Suyin Liang, Tingquan Gao, Zelun Zhang, Jiaxuan Liu, Xueqing Wang,
Changda Zhou, Hongen Liu, Manhui Lin, et al. Paddleocr-vl: Boosting multilingual docu-
mentparsingviaa0.9bultra-compactvision-languagemodel. arXivpreprintarXiv:2510.14528,
2025a.
ChengCui,TingSun,ManhuiLin,TingquanGao,YuboZhang,JiaxuanLiu,XueqingWang,Zelun
Zhang, Changda Zhou, Hongen Liu, Yue Zhang, Wenyu Lv, Kui Huang, Yichao Zhang, Jing
Zhang, Jun Zhang, Yi Liu, Dianhai Yu, and Yanjun Ma. Paddleocr 3.0 technical report, 2025b.
URLhttps://arxiv.org/abs/2507.05595.
BCarneirodaRochaandRTimoteodeSousaJunior. Identifyingbankfraudsusingcrisp-dmand
decision trees. International Journal of Computer Science and Information Technology, 2(5):
162–169,2010.
10

PublishedasaconferencepaperatICLR2026
DOSM Department of Statistics Malaysia. Profile of msmes in 2015-2024, Au-
gust 2025. URL https://smecorp.gov.my/index.php/en/policies/
2020-02-11-08-01-24/profile-and-importance-to-the-economy.
VianiBDjeundje,JonathanCrook,RaffaellaCalabrese,andMonaHamid.Enhancingcreditscoring
withalternativedata. ExpertSystemswithApplications,163:113766,2021.
Adrien Ehrhardt, Christophe Biernacki, Vincent Vandewalle, Philippe Heinrich, and Se´bastien
Beben. Reject inference methods in credit scoring. Journal of Applied Statistics, 48(13-15):
2734–2754,2021. doi: 10.1080/02664763.2021.1929090.
Okeoghene Elebe and Chikaome Chimara Imediegwu. A credit scoring system using transaction-
level behavioral data for msmes. Journal of Frontiers in Multidisciplinary Research, 2(1):312–
322,2021.
Jerome H Friedman. Greedy function approximation: a gradient boosting machine. Annals of
statistics,pp.1189–1232,2001.
Anthony Gathu. The Role of alternative data in accurately determining credit score for mobile
lendingondigitalwalletsinKenya. PhDthesis,StrathmoreUniversity,2020.
AmolGoteandVikasMendhe. Buildingacashflowunderwritingsystem:Insightsfromimplemen-
tation. InternationalJournalofComputerTrendsandTechnology,72(2):70–74,2024.
World Bank Group. The use of alternative data in credit risk assess-
ment: Opportunities, risks, and challenges, 2024. URL https://
documents1.worldbank.org/curated/en/099031325132018527/pdf/
P179614-3e01b947-cbae-41e4-85dd-2905b6187932.pdf.
Bjo¨rn Rafn Gunnarsson, Seppe Vanden Broucke, Bart Baesens, Mar´ıa O´skarsdo´ttir, and Wilfried
Lemahieu. Deep learning for credit scoring: Do or don’t? European Journal of Operational
Research,295(1):292–305,2021.
ExperianInsights. Rejectinferenceandunderwriting: Adeepdive,2024. URLhttps://www.
experian.com/blogs/insights/reject-inference/.
EunjiKim,JehyukLee,HunsikShin,HoseongYang,SungzoonCho,Seung-kwanNam,Youngmi
Song, Jeong-a Yoon, and Jong-il Kim. Champion-challenger analysis for credit card fraud de-
tection: Hybrid ensemble and deep learning. Expert Systems with Applications, 128:214–224,
2019.
Jung Youn Lee, Joonhyuk Yang, and Eric T. Anderson. Express: Who benefits from alter-
native data for credit scoring? evidence from peru. Journal of Marketing Research, 0(ja):
00222437251360996, 0. doi: 10.1177/00222437251360996. URLhttps://doi.org/10.
1177/00222437251360996.
Stefan Lessmann, Bart Baesens, Hsin-Vonn Seow, and Lyn C Thomas. Benchmarking state-of-
the-art classification algorithms for credit scoring: An update of research. European journal of
operationalresearch,247(1):124–136,2015.
ZhangLi,YuliangLiu,QiangLiu,ZhiyinMa,ZiyangZhang,ShuoZhang,ZidunGuo,JiaruiZhang,
XinyuWang,andXiangBai.Monkeyocr:Documentparsingwithastructure-recognition-relation
tripletparadigm. arXivpreprintarXiv:2506.05218,2025.
Minghui Liao, Zhaoyi Wan, Cong Yao, Kai Chen, and Xiang Bai. Real-time scene text detection
withdifferentiablebinarization. InProceedingsoftheAAAIconferenceonartificialintelligence,
volume34,pp.11474–11481,2020.
Security Commissions Malaysia. Enabling a more relevant, efficient and diversified mar-
ket,2025.URLhttps://www.sc.com.my/api/documentms/download.ashx?id=
61f72817-e06d-4e54-b25c-8be8abddcd28.
Mindee. doctr: Documenttextrecognition. https://github.com/mindee/doctr,2021.
11

PublishedasaconferencepaperatICLR2026
AndrewYNg. Featureselection,l1vs.l2regularization,androtationalinvariance. InProceedings
ofthetwenty-firstinternationalconferenceonMachinelearning,pp. 78,2004.
MfanasibiliNgwenya.Creditscoringinafrica:Employinglogisticregressiononalternativedata.In
20244thInternationalConferenceonElectrical,Computer,CommunicationsandMechatronics
Engineering(ICECCME),pp.1–6,Maldives,2024.IEEE. doi: 10.1109/ICECCME62383.2024.
10796011.
IzunnaOkpala,AshkanGolgoon,andArjunRaviKannan. Agenticaisystemsappliedtotasksinfi-
nancialservices:modelingandmodelriskmanagementcrews. arXivpreprintarXiv:2502.05439,
2025.
Srinivasarao Paleti. Agentic ai in financial decision-making: Enhancing customer risk profiling,
predictive loan approvals, and automated treasury management in modern banking. Multidisci-
plinary,ScientificWorkandManagementJournal,2024.
Vikas Paruchuri and Datalab Team. Surya: A lightweight document ocr and analysis toolkit.
https://github.com/VikParuchuri/surya,2025. GitHubrepository.
Jake Poznanski, Jon Borchardt, Jason Dunkelberger, Regan Huff, Daniel Lin, Aman Rangapur,
Christopher Wilhelm, Kyle Lo, and Luca Soldaini. olmOCR: Unlocking Trillions of Tokens
in PDFs with Vision Language Models, 2025. URL https://arxiv.org/abs/2502.
18443.
pymupdf. Pymupdf. https://github.com/pymupdf/PyMuPDF,2025. GitHubrepository.
KuldeepRawat. Applyingcrisp-dmmethodologyindevelopingmachinelearningmodelforcredit
riskprediction. InScienceandInformationConference,pp.522–538.Springer,2023.
RobertESchapire. Explainingadaboost. InEmpiricalinference: festschriftinhonorofvladimirN.
Vapnik,pp.37–52.Springer,2013.
scikit learn. Adaboostclassifier, 2025a. URL https://scikit-learn.org/stable/
modules/generated/sklearn.ensemble.AdaBoostClassifier.html.
scikit learn. Gradientboostingclassifier, 2025b. URL https://
scikit-learn.org/stable/modules/generated/sklearn.ensemble.
GradientBoostingClassifier.html.
scikit learn. Logisticregression, 2025c. URL https://scikit-learn.org/stable/
modules/generated/sklearn.linear_model.LogisticRegression.html.
scikitlearn. Randomforestclassifier, 2025d. URLhttps://scikit-learn.org/stable/
modules/generated/sklearn.ensemble.RandomForestClassifier.html.
BaoguangShi,XiangBai,andCongYao. Anend-to-endtrainableneuralnetworkforimage-based
sequencerecognitionanditsapplicationtoscenetextrecognition. IEEEtransactionsonpattern
analysisandmachineintelligence,39(11):2298–2304,2016.
TanmayShivhare. HowtoUtilizeBankStatementsasaNewCreditScoringMethod. PhDthesis,
Dublin,NationalCollegeofIreland,2024.
NaeemSiddiqi. Intelligentcreditscoring: Buildingandimplementingbettercreditriskscorecards.
JohnWiley&Sons,NorthCarolina,USA,2017. ISBN9781119282396.
Shrawan Kumar Trivedi. A study on credit scoring modeling with different feature selection and
machinelearningapproaches. TechnologyinSociety,63:101413,2020.
BinWang,ChaoXu,XiaomengZhao,LinkeOuyang,FanWu,ZhiyuanZhao,RuiXu,KaiwenLiu,
Yuan Qu, Fukai Shang, et al. Mineru: An open-source solution for precise document content
extraction,2024a. arXivpreprintarXiv:2409.18839.
12

PublishedasaconferencepaperatICLR2026
Stewart Watterson. Cash flow underwriting: Reshaping the lending landscape,
November 2024. URL https://assets.ctfassets.net/ss5kfr270og3/
2LceEfOxttxwSpVtkiAPUw/dd87916c5d598b4fa8950d12f896ab1d/
20241203_Cash_Flow_Underwriting_Reshaping_the_Lending_Landscape_
White_Paper_Plaid.pdf.
Haoran Wei, Yaofeng Sun, and Yukun Li. Deepseek-ocr 2: Visual causal flow. arXiv preprint
arXiv:2601.20552,2026.
13

PublishedasaconferencepaperatICLR2026
A APPENDIX
A.1 LOGISTICREGRESSIONMODEL
Given thatWOE provides alog-odds transformation of eachfeature, this alignsnaturally with the
LR model. The WOE transformed feature value can be represented as WOE (x ) and the LR
j ij
modelcanbeexpressedinasimplifiedformas:
d
log P(y i =1|x i ) =β + (cid:88) β WOE (x ). (6)
P(y =0|x ) 0 j j ij
i i
j=1
where β is the intercept and β represents the coefficient for feature j. This allows direct inter-
0 j
pretationofcoefficientsintermsofthecreditriskassociatedwitheachfeature. Positiveβ values
j
indicatethathigherWOEcorrespondstolowerdefaultrisk,andviceversa. Hence,WOEencoding
stabilizesestimationandsupportsconsistent,monotonicrelationshipsbetweenpredictorsandcredit
outcomes.
Formally, let x ∈ Rd denote the feature vector for applicant i, where d is the number of features
i
engineeredfrombothapplicationformdataandbankstatementtransactions,andlety ∈{0,1}be
i
thebinaryoutputindicatingdefault(y = 1)ornon-default(y = 0). TheLRmodelspecifiesthe
i i
conditionalprobabilityofdefaultas
P(y =1|x ;β)=σ(β +x⊤β), (7)
i i 0 i
where σ(z) = 1 is the sigmoid function, β ∈ R is the intercept term, and β ∈ Rd is the
1+e−z 0
coefficientvectorassociatedwiththepredictors. Theparametersareestimatedbymaximizingthe
penalizedlog-likelihoodfunction:
n
(cid:88)
L(β)= [y logp +(1−y )log(1−p )]−λ∥β∥2, (8)
i i i i 2
i=1
wherep = P(y = 1 | x ;β)andλ ≥ 0controlsthestrengthoftheℓ regularization(Ng,2004).
i i i 2
Thismitigatesoverfittingbyshrinkingcoefficientmagnitudes,whichisparticularlyimportantwhen
modelinghigh-dimensional,transaction-derivedfeatures.
A.2 USEOFLARGELANGUAGEMODELS
A.2.1 DATASET
We gathered bank statements of various consulting firms in Malaysia. The dataset consists of ap-
proximately110uniquebankstatementPDFsfromthetop6banksinMalaysia: Maybank,Public
Bank,CIMBBank,RHBBank,HongLeongBank,andAmBank.Eachbankstatementcontainskey
informationfieldssuchasbankname,accountholdername,accountnumber,address,andstatement
date,aswellastransactiontableslistingindividualtransactionswithdetailssuchasdate,description,
debitamount,creditamount,andbalance.
A.2.2 MODELCHOICES
PrecisetextboundingboxcoordinatesforOCRresultsarerequiredbecausebankofficersmustcross-
checkextractionresultsbeforetheycanbeusedforsubsequentprocessing;thisensurestransparency,
traceability, and auditability of our AI results, and explains our design choice of using OCR and
LLMs for financial information extraction. The OCR models used are mainly from Azure with
different variations: prebuilt-bankStatement.us is an Azure Document Intelligence prebuilt OCR
modelspecificallydesignedforbankstatementsintheUS,whilepretrained-readisamoregeneral
OCRmodelthatcanbefine-tunedforvariousdocumenttypes. TheAzureVision4.0modelrefers
totheAzuregenericOCRmodel. TheGPTmodelsusedareGPT-4o-miniandGPT-4.1,whichare
differentversionsofOpenAI’sGPT-4architecturewithvaryingcapabilitiesandperformancelevels.
14

PublishedasaconferencepaperatICLR2026
Certain specialized OCR models such as MinerU (Wang et al.), PyMuPDF (pymupdf, 2025) and
PPStructureV3(Cuietal.,2025b)areincludedforcomparisonsincetheyarewidelyadoptedinthe
industryfordocumentprocessingtasks. PyMuPDF-Formattedreferstoformattingtheoutputfrom
document parser to imitate actual document layout before passing them into LLM. LLM-based
OCR models such as olmOCR (Poznanski et al., 2025), paddleOCR-VL (Cui et al., 2025a), and
Surya(Paruchuri&Team,2025)arealsoincludedfortableextractioncomparisons. Ourtemplate
matchingmethodisbuiltbasedonthelayoutofthebankstatementsinourdataset,wherewemanu-
allydefinetheregionsofinterestforkeyinformationfieldsandtransactiontables. Forourmethod,
weuseDBwithResNet50backbone(Liaoetal.,2020)fortextdetectionandCRNNwithVGG16
backbone(Shietal.,2016)fortextrecognition.Thenwebuildourowntemplatematchingalgorithm
in Python logic. Do note that we are the only method that is not using any LLMs for information
extraction.
AsshowninTables3,4,8,and9,ourtemplatematchingmethodachievesthebestperformancewhen
the bank statement formats are consistent, which is the case in Malaysia. In real-world scenarios
where bank statement formats can vary significantly, template matching methods may not be as
effectiveasmoreflexibleOCRmodels.Infuturework,weplantoexploremoreadvancedtechniques
such as OCR+LLM-based layout analysis and document understanding models (Deepseek-OCR
2 (Wei et al., 2026), MonkeyOCR (Li et al., 2025)) to improve the robustness of key information
andtableextractionacrossdiversebankstatementformats.
A.2.3 EVALUATIONMETRIC
Key information results are evaluated based on exact match accuracy between the extracted text
andthegroundtruthforeachfield. Anexactmatchiscountedwhentheextractedtextmatchesthe
groundtruthcharacterbycharacter,includingspacesandpunctuation. Theaccuracyisthencalcu-
latedasthepercentageofexactmatchesoverthetotalnumberofkeyinformationfieldsevaluated.
Table extraction results are evaluated based on the normalized edit distance (NED) between the
extracted text and the ground truth for each transaction row. The NED for a single row entry is
calculatedasfollows:
EditDistance
NED=1− (9)
max(LengthofExtractedText,LengthofGroundTruthText)
whereEditDistanceistheminimumnumberofoperations(insertions,deletions,substitutions)re-
quiredtotransformtheextractedtextintothegroundtruthtext.AhigherNEDvalueindicatesbetter
accuracy,withamaximumof1.0representingaperfectmatch. Thescoreisthenscaledtotherange
of0to100foreasierinterpretation.
Wereporttwovariantsoftheper-columnsimilarityscoretocapturedifferentaspectsofextraction
quality:
MatchingNEDScore(%). Foreachcolumn(date,description,debit,credit,balance),wecompute
the NED for every matched row. Only rows with NED > 70% are retained, and the per-column
scoreistheaverageNEDacrossthesefilteredrowsforagivenbank. Thismetricmeasureshowac-
curatelythesystemextractscontentforrowsthatithasreasonablyidentified,byexcludingseverely
misaligned or garbled entries that fall below the 70% threshold. It thus reflects extraction quality
conditionedonsuccessfulrowmatching.
ExactNEDScore(%). Foreachcolumn,wecomputetheNEDforeveryrowwithoutanyfiltering
threshold. All rows are included regardless of their NED value, and the per-column score is the
averageNEDacrossallrowsforagivenbank. Thismetricprovidesastricterevaluationthatpenal-
izesbothcharacter-levelextractionerrorsandrow-levelalignmentfailures(e.g.,missedrows,extra
rows,ormisalignedentries),asthesecontributelowNEDvaluesthatreducetheoverallaverage.
Thekeydifferencebetweenthetwometricsliesintheirtreatmentofpoorlymatchedrows. Match-
ing NED isolates extraction accuracy by filtering out rows with NED ≤ 70%, while exact NED
capturesthefullpictureincludingrowdetectionfailures. Alargegapbetweenmatchingandexact
NEDscoresforagivenconfigurationindicatesthatthesystemproducesaccurateextractionswhen
itcorrectlyidentifiesrows,butfrequentlyfailsatrow-levelalignmentormissesrowsentirely. Con-
versely,similarmatchingandexactNEDscoressuggestconsistentrowdetectionwithfewalignment
failures.
15

PublishedasaconferencepaperatICLR2026
A.3 QUANTITATIVERESULTSFORKEYINFORMATIONEXTRACTION
We evaluate key information extraction across the top six largest Malaysian banks: Maybank
(MBBE), Public Bank (PBBE), CIMB Bank (CIBB), RHB Bank (RHBB), Hong Leong Bank
(HLBB), and AmBank (ARBK). The evaluation covers five structured fields: bank name, account
holder, account number, address, and statement date. We report both exact match accuracy with
strict character-level equality and Normalized Edit Distance (NED) similarity with a tolerance for
minor character-level discrepancies. Tables 3 and 4 summarize the average exact match accuracy
and NED score performance across all banks respectively, while Tables 5 and 6 provide per-bank
breakdowns.
Overall Performance. Our template matching approach achieves a perfect 100% on both exact
match accuracy and NED score across all five fields and all six banks, demonstrating robust and
consistentextractionwithoutrelianceonexternalOCRorLLMAPIs. Amongthebaselines,config-
urations pairing high-quality OCR engines (Pretrained-Read, Azure AI 4.0) with GPT-4.1 achieve
near-perfect results, with Azure AI 4.0 + GPT-4.1 reaching 100% exact match accuracy on four
fields (bank name, account holder, account number, and statement date) and 94.82% on address.
Theaddressfieldprovesmostchallengingacrossallconfigurationsduetomulti-lineformattingand
bank-specificlayoutvariations.
OCR Engine Impact. The choice of OCR engine substantially influences downstream extraction
quality. Cloud-basedOCRsolutions(Pretrained-Read,AzureAI4.0)consistentlyoutperformopen-
source alternatives. MinerU exhibits the weakest bank name extraction (28.33%–41.30% exact
match accuracy) due to its inability to parse graphical logos and stylized text commonly found in
Malaysianbankstatementheaders. Text-basedextractors(PyMuPDF,Pdfium)showvariablebank
nameaccuracy(58.76%–74.87%), astheyrelyonthePDFtextlayer, whichmaynotencodebank
names embedded in header images. In contrast, docTR achieves 100% bank name accuracy by
leveragingdeeplearning-basedtextdetectiononrenderedpageimages.
GPT Model Impact. Across all OCR engines, upgrading from GPT-4o-mini to GPT-4.1 consis-
tentlyimprovesextractionaccuracy,particularlyforaddressandstatementdatefields. Forexample,
with docTR, the address exact match accuracy improves from 73.97% to 80.82% when switching
to GPT-4.1. This improvement stems from GPT-4.1’s enhanced ability to parse multi-line address
formatsandnormalizedaterepresentationsacrossdifferentbanktemplates.
Per-BankVariation.AmBankandHongLeongBankstatementsaregenerallyeasiertoprocessdue
totheirstandardizeddigital-nativePDFformats,achievingnear-perfectscoresacrossmostconfigu-
rations. RHBBankandCIMBBankpresentgreaterchallenges: RHBBank’smulti-columnlayouts
reduceMinerU’sperformanceto40–70%acrossmostfields,whileCIMBBank’sheaderformatting
leads to lower bank name recognition for text-based extractors. These per-bank variations under-
scoretheimportanceofbank-specificevaluationwhendeployingextractionsystemsinmulti-bank
productionenvironments.
Table3: Averageexactmatchaccuracyscoresacrossalltopsixlargestbanks.
KeyInformationExtraction-ExactMatchAccuracy
| OCR       | GPT |          |           |           |         |               |
| --------- | --- | -------- | --------- | --------- | ------- | ------------- |
|           |     | BankName | AccHolder | AccNumber | Address | StatementDate |
| Prebuilt- | N/A | 93.39    | 80.82     | 92.86     | 92.77   | 77.51         |
BankStatement
| Pretrained-Read | gpt-4o-mini | 100.00 | 96.48  | 100.00 | 89.10 | 97.62  |
| --------------- | ----------- | ------ | ------ | ------ | ----- | ------ |
| Pretrained-Read | gpt-4.1     | 100.00 | 100.00 | 100.00 | 92.43 | 100.00 |
| AzureAI4.0      | gpt-4o-mini | 100.00 | 98.15  | 100.00 | 88.20 | 97.62  |
| AzureAI4.0      | gpt-4.1     | 100.00 | 100.00 | 100.00 | 94.82 | 100.00 |
| docTR           | gpt-4o-mini | 100.00 | 87.78  | 100.00 | 73.97 | 97.62  |
| docTR           | gpt-4.1     | 100.00 | 93.15  | 100.00 | 80.82 | 100.00 |
| MinerU          | gpt-4o-mini | 28.33  | 86.48  | 90.95  | 61.43 | 95.00  |
| MinerU          | gpt-4.1     | 41.30  | 86.67  | 93.33  | 72.14 | 95.00  |
| PyMuPDF         | gpt-4o-mini | 62.09  | 96.30  | 100.00 | 90.58 | 97.62  |
| PyMuPDF         | gpt-4.1     | 71.16  | 98.33  | 100.00 | 96.67 | 100.00 |
Continuedonnextpage
16

PublishedasaconferencepaperatICLR2026
Table3–Continuedfrompreviouspage
KeyInformationExtraction-ExactMatchAccuracy
| OCR      | GPT         |          |           |           |         |               |
| -------- | ----------- | -------- | --------- | --------- | ------- | ------------- |
|          |             | BankName | AccHolder | AccNumber | Address | StatementDate |
| PyMuPDF- | gpt-4o-mini | 61.92    | 98.15     | 100.00    | 92.25   | 100.00        |
Formatted
| PyMuPDF- | gpt-4.1 | 74.87 | 98.15 | 100.00 | 96.48 | 100.00 |
| -------- | ------- | ----- | ----- | ------ | ----- | ------ |
Formatted
| Pdfium                 | gpt-4o-mini                                          | 58.76  | 96.30  | 100.00 | 83.17  | 100.00 |
| ---------------------- | ---------------------------------------------------- | ------ | ------ | ------ | ------ | ------ |
| Pdfium                 | gpt-4.1                                              | 71.16  | 100.00 | 100.00 | 96.67  | 100.00 |
| Ours(templatematching) |                                                      | 100.00 | 100.00 | 100.00 | 100.00 | 100.00 |
|                        | Table4: AverageNEDscoresacrossalltopsixlargestbanks. |        |        |        |        |        |
KeyInformationExtraction-NEDScore
| OCR       | GPT |          |           |           |         |               |
| --------- | --- | -------- | --------- | --------- | ------- | ------------- |
|           |     | BankName | AccHolder | AccNumber | Address | StatementDate |
| Prebuilt- | N/A | 93.39    | 82.75     | 95.11     | 98.40   | 79.13         |
BankStatement
| Pretrained-Read | gpt-4o-mini | 100.00 | 97.36  | 100.00 | 96.30 | 99.70  |
| --------------- | ----------- | ------ | ------ | ------ | ----- | ------ |
| Pretrained-Read | gpt-4.1     | 100.00 | 100.00 | 100.00 | 99.34 | 100.00 |
| AzureAI4.0      | gpt-4o-mini | 100.00 | 98.59  | 100.00 | 96.90 | 99.70  |
| AzureAI4.0      | gpt-4.1     | 100.00 | 100.00 | 100.00 | 99.59 | 100.00 |
| docTR           | gpt-4o-mini | 100.00 | 98.44  | 100.00 | 97.84 | 99.70  |
| docTR           | gpt-4.1     | 100.00 | 98.02  | 100.00 | 98.60 | 100.00 |
| MinerU          | gpt-4o-mini | 37.00  | 88.29  | 92.74  | 77.46 | 97.50  |
| MinerU          | gpt-4.1     | 43.79  | 86.67  | 93.33  | 84.20 | 96.25  |
| PyMuPDF         | gpt-4o-mini | 64.99  | 97.28  | 100.00 | 99.11 | 99.70  |
| PyMuPDF         | gpt-4.1     | 71.17  | 98.33  | 100.00 | 99.82 | 100.00 |
| PyMuPDF-        | gpt-4o-mini | 69.36  | 98.15  | 100.00 | 99.17 | 100.00 |
Formatted
| PyMuPDF- | gpt-4.1 | 75.77 | 99.32 | 100.00 | 99.50 | 100.00 |
| -------- | ------- | ----- | ----- | ------ | ----- | ------ |
Formatted
| Pdfium                 | gpt-4o-mini | 63.96  | 97.13  | 100.00 | 98.97  | 100.00 |
| ---------------------- | ----------- | ------ | ------ | ------ | ------ | ------ |
| Pdfium                 | gpt-4.1     | 71.17  | 100.00 | 100.00 | 99.82  | 100.00 |
| Ours(templatematching) |             | 100.00 | 100.00 | 100.00 | 100.00 | 100.00 |
Table5: KeyinformationextractionexactmatchaccuracyscoregroupedbybankacrossOCRand
GPTconfigurations.
KeyInformationExtraction-ExactMatchAccuracy
| OCR | GPT |          |           |           |         |               |
| --- | --- | -------- | --------- | --------- | ------- | ------------- |
|     |     | BankName | AccHolder | AccNumber | Address | StatementDate |
CIMBBank(7UniquePDFs)
| Prebuilt- | N/A | 71.43 | 71.43 | 57.14 | 85.71 | 42.86 |
| --------- | --- | ----- | ----- | ----- | ----- | ----- |
BankStatement
| Pretrained-Read | gpt-4o-mini | 100.00 | 100.00 | 100.00 | 85.71  | 85.71  |
| --------------- | ----------- | ------ | ------ | ------ | ------ | ------ |
| Pretrained-Read | gpt-4.1     | 100.00 | 100.00 | 100.00 | 85.71  | 100.00 |
| AzureAI4.0      | gpt-4o-mini | 100.00 | 100.00 | 100.00 | 71.43  | 85.71  |
| AzureAI4.0      | gpt-4.1     | 100.00 | 100.00 | 100.00 | 100.00 | 100.00 |
| docTR           | gpt-4o-mini | 100.00 | 100.00 | 100.00 | 57.14  | 85.71  |
| docTR           | gpt-4.1     | 100.00 | 100.00 | 100.00 | 57.14  | 100.00 |
| MinerU          | gpt-4o-mini | 0.00   | 100.00 | 85.71  | 85.71  | 100.00 |
| MinerU          | gpt-4.1     | 0.00   | 100.00 | 100.00 | 100.00 | 100.00 |
| PyMuPDF         | gpt-4o-mini | 71.43  | 100.00 | 100.00 | 85.71  | 85.71  |
| PyMuPDF         | gpt-4.1     | 71.43  | 100.00 | 100.00 | 100.00 | 100.00 |
| PyMuPDF-        | gpt-4o-mini | 71.43  | 100.00 | 100.00 | 85.71  | 100.00 |
Formatted
Continuedonnextpage
17

PublishedasaconferencepaperatICLR2026
Table5–Continuedfrompreviouspage
KeyInformationExtraction-ExactMatchAccuracy
| OCR      | GPT     |          |           |           |         |               |
| -------- | ------- | -------- | --------- | --------- | ------- | ------------- |
|          |         | BankName | AccHolder | AccNumber | Address | StatementDate |
| PyMuPDF- | gpt-4.1 | 71.43    | 100.00    | 100.00    | 100.00  | 100.00        |
Formatted
| Pdfium                 | gpt-4o-mini | 71.43  | 100.00 | 100.00 | 85.71  | 100.00 |
| ---------------------- | ----------- | ------ | ------ | ------ | ------ | ------ |
| Pdfium                 | gpt-4.1     | 71.43  | 100.00 | 100.00 | 100.00 | 100.00 |
| Ours(templatematching) |             | 100.00 | 100.00 | 100.00 | 100.00 | 100.00 |
RHBBank(10UniquePDFs)
| Prebuilt- | N/A | 100.00 | 90.00 | 100.00 | 70.00 | 100.00 |
| --------- | --- | ------ | ----- | ------ | ----- | ------ |
BankStatement
Pretrained-Read gpt-4o-mini 100.00 100.00 100.00 90.00 100.00
| Pretrained-Read | gpt-4.1     | 100.00 | 100.00 | 100.00 | 80.00  | 100.00 |
| --------------- | ----------- | ------ | ------ | ------ | ------ | ------ |
| AzureAI4.0      | gpt-4o-mini | 100.00 | 100.00 | 100.00 | 100.00 | 100.00 |
| AzureAI4.0      | gpt-4.1     | 100.00 | 100.00 | 100.00 | 80.00  | 100.00 |
| docTR           | gpt-4o-mini | 100.00 | 70.00  | 100.00 | 80.00  | 100.00 |
| docTR           | gpt-4.1     | 100.00 | 70.00  | 100.00 | 70.00  | 100.00 |
| MinerU          | gpt-4o-mini | 70.00  | 50.00  | 70.00  | 40.00  | 70.00  |
| MinerU          | gpt-4.1     | 70.00  | 50.00  | 70.00  | 40.00  | 70.00  |
| PyMuPDF         | gpt-4o-mini | 90.00  | 100.00 | 100.00 | 80.00  | 100.00 |
| PyMuPDF         | gpt-4.1     | 100.00 | 100.00 | 100.00 | 80.00  | 100.00 |
| PyMuPDF-        | gpt-4o-mini | 100.00 | 100.00 | 100.00 | 100.00 | 100.00 |
Formatted
| PyMuPDF- | gpt-4.1 | 100.00 | 100.00 | 100.00 | 100.00 | 100.00 |
| -------- | ------- | ------ | ------ | ------ | ------ | ------ |
Formatted
| Pdfium                 | gpt-4o-mini | 70.00  | 100.00 | 100.00 | 80.00  | 100.00 |
| ---------------------- | ----------- | ------ | ------ | ------ | ------ | ------ |
| Pdfium                 | gpt-4.1     | 100.00 | 100.00 | 100.00 | 80.00  | 100.00 |
| Ours(templatematching) |             | 100.00 | 100.00 | 100.00 | 100.00 | 100.00 |
HongLeongBank(9UniquePDFs)
| Prebuilt- | N/A | 100.00 | 88.89 | 100.00 | 100.00 | 100.00 |
| --------- | --- | ------ | ----- | ------ | ------ | ------ |
BankStatement
Pretrained-Read gpt-4o-mini 100.00 88.89 100.00 100.00 100.00
| Pretrained-Read | gpt-4.1     | 100.00 | 100.00 | 100.00 | 100.00 | 100.00 |
| --------------- | ----------- | ------ | ------ | ------ | ------ | ------ |
| AzureAI4.0      | gpt-4o-mini | 100.00 | 88.89  | 100.00 | 88.89  | 100.00 |
| AzureAI4.0      | gpt-4.1     | 100.00 | 100.00 | 100.00 | 100.00 | 100.00 |
| docTR           | gpt-4o-mini | 100.00 | 66.67  | 100.00 | 88.89  | 100.00 |
| docTR           | gpt-4.1     | 100.00 | 88.89  | 100.00 | 100.00 | 100.00 |
| MinerU          | gpt-4o-mini | 0.00   | 88.89  | 100.00 | 100.00 | 100.00 |
| MinerU          | gpt-4.1     | 44.44  | 100.00 | 100.00 | 100.00 | 100.00 |
| PyMuPDF         | gpt-4o-mini | 100.00 | 88.89  | 100.00 | 88.89  | 100.00 |
| PyMuPDF         | gpt-4.1     | 100.00 | 100.00 | 100.00 | 100.00 | 100.00 |
| PyMuPDF-        | gpt-4o-mini | 100.00 | 88.89  | 100.00 | 88.89  | 100.00 |
Formatted
| PyMuPDF- | gpt-4.1 | 100.00 | 100.00 | 100.00 | 100.00 | 100.00 |
| -------- | ------- | ------ | ------ | ------ | ------ | ------ |
Formatted
| Pdfium                 | gpt-4o-mini | 100.00 | 88.89  | 100.00 | 44.44  | 100.00 |
| ---------------------- | ----------- | ------ | ------ | ------ | ------ | ------ |
| Pdfium                 | gpt-4.1     | 100.00 | 100.00 | 100.00 | 100.00 | 100.00 |
| Ours(templatematching) |             | 100.00 | 100.00 | 100.00 | 100.00 | 100.00 |
AmBank(7UniquePDFs)
| Prebuilt- | N/A | 100.00 | 85.71 | 100.00 | 100.00 | 100.00 |
| --------- | --- | ------ | ----- | ------ | ------ | ------ |
BankStatement
Pretrained-Read gpt-4o-mini 100.00 100.00 100.00 100.00 100.00
| Pretrained-Read | gpt-4.1     | 100.00 | 100.00 | 100.00 | 100.00 | 100.00 |
| --------------- | ----------- | ------ | ------ | ------ | ------ | ------ |
| AzureAI4.0      | gpt-4o-mini | 100.00 | 100.00 | 100.00 | 100.00 | 100.00 |
| AzureAI4.0      | gpt-4.1     | 100.00 | 100.00 | 100.00 | 100.00 | 100.00 |
| docTR           | gpt-4o-mini | 100.00 | 100.00 | 100.00 | 100.00 | 100.00 |
| docTR           | gpt-4.1     | 100.00 | 100.00 | 100.00 | 100.00 | 100.00 |
| MinerU          | gpt-4o-mini | 0.00   | 100.00 | 100.00 | 42.86  | 100.00 |
| MinerU          | gpt-4.1     | 0.00   | 100.00 | 100.00 | 42.86  | 100.00 |
Continuedonnextpage
18

PublishedasaconferencepaperatICLR2026
Table5–Continuedfrompreviouspage
KeyInformationExtraction-ExactMatchAccuracy
| OCR      | GPT         |          |      |           |           |        |         |               |
| -------- | ----------- | -------- | ---- | --------- | --------- | ------ | ------- | ------------- |
|          |             | BankName |      | AccHolder | AccNumber |        | Address | StatementDate |
| PyMuPDF  | gpt-4o-mini |          | 0.00 | 100.00    |           | 100.00 | 100.00  | 100.00        |
| PyMuPDF  | gpt-4.1     |          | 0.00 | 100.00    |           | 100.00 | 100.00  | 100.00        |
| PyMuPDF- | gpt-4o-mini |          | 0.00 | 100.00    |           | 100.00 | 100.00  | 100.00        |
Formatted
| PyMuPDF- | gpt-4.1 |     | 0.00 | 100.00 |     | 100.00 | 100.00 | 100.00 |
| -------- | ------- | --- | ---- | ------ | --- | ------ | ------ | ------ |
Formatted
| Pdfium                 | gpt-4o-mini |     | 0.00   | 100.00 |     | 100.00 | 100.00 | 100.00 |
| ---------------------- | ----------- | --- | ------ | ------ | --- | ------ | ------ | ------ |
| Pdfium                 | gpt-4.1     |     | 0.00   | 100.00 |     | 100.00 | 100.00 | 100.00 |
| Ours(templatematching) |             |     | 100.00 | 100.00 |     | 100.00 | 100.00 | 100.00 |
Table6: KeyinformationextractionsimilarityscoregroupedbybankacrossOCRandGPTconfig-
urations.
KeyInformationExtraction-NEDScore
| OCR | GPT |          |     |           |     |           |         |               |
| --- | --- | -------- | --- | --------- | --- | --------- | ------- | ------------- |
|     |     | BankName |     | AccHolder |     | AccNumber | Address | StatementDate |
Maybank(10UniquePDFs)
| prebuilt- | N/A |     | 100 | 69.09 |     | 100 | 100 | 100 |
| --------- | --- | --- | --- | ----- | --- | --- | --- | --- |
bankStatement.us
| pretrained-read        | GPT-4o-mini |     | 100 | 92.63 |     | 100 | 82.01 | 100 |
| ---------------------- | ----------- | --- | --- | ----- | --- | --- | ----- | --- |
| pretrained-read        | GPT-4.1     |     | 100 | 100   |     | 100 | 100   | 100 |
| AzureAI4.0             | GPT-4o-mini |     | 100 | 100   |     | 100 | 87.24 | 100 |
| AzureAI4.0             | GPT-4.1     |     | 100 | 100   |     | 100 | 100   | 100 |
| MinerU                 | GPT-4o-mini |     | 100 | 85.14 |     | 90  | 27.41 | 100 |
| MinerU                 | GPT-4.1     |     | 100 | 70    |     | 90  | 66.36 | 100 |
| PyMuPDF                | GPT-4o-mini |     | 100 | 100   |     | 100 | 100   | 100 |
| PyMuPDF                | GPT-4.1     |     | 100 | 90    |     | 100 | 100   | 100 |
| pdfium                 | GPT-4o-mini |     | 100 | 100   |     | 100 | 100   | 10  |
| pdfium                 | GPT-4.1     |     | 100 | 100   |     | 100 | 100   | 10  |
| Ours(templatematching) |             |     | 100 | 100   |     | 100 | 100   | 100 |
PublicBank(9UniquePDFs)
| prebuilt- | N/A |     | 88.89 | 88.89 |     | 100 | 98.60 | 31.94 |
| --------- | --- | --- | ----- | ----- | --- | --- | ----- | ----- |
bankStatement.us
| pretrained-read        | GPT-4o-mini |     | 100   | 100   |     | 100 | 99.74 | 100 |
| ---------------------- | ----------- | --- | ----- | ----- | --- | --- | ----- | --- |
| pretrained-read        | GPT-4.1     |     | 100   | 100   |     | 100 | 98.60 | 100 |
| AzureAI4.0             | GPT-4o-mini |     | 100   | 100   |     | 100 | 98.60 | 100 |
| AzureAI4.0             | GPT-4.1     |     | 100   | 100   |     | 100 | 98.60 | 100 |
| MinerU                 | GPT-4o-mini |     | 20.16 | 100   |     | 100 | 100   | 100 |
| MinerU                 | GPT-4.1     |     | 41.83 | 100   |     | 100 | 100   | 100 |
| PyMuPDF                | GPT-4o-mini |     | 16.88 | 92.16 |     | 100 | 98.60 | 100 |
| PyMuPDF                | GPT-4.1     |     | 55.56 | 100   |     | 100 | 100   | 100 |
| pdfium                 | GPT-4o-mini |     | 20.85 | 91.27 |     | 100 | 98.60 | 100 |
| pdfium                 | GPT-4.1     |     | 55.56 | 100   |     | 100 | 100   | 100 |
| Ours(templatematching) |             |     | 100   | 100   |     | 100 | 100   | 100 |
CIMBBank(7UniquePDFs)
| prebuilt- | N/A |     | 71.43 | 73.91 |     | 70.68 | 99.77 | 42.86 |
| --------- | --- | --- | ----- | ----- | --- | ----- | ----- | ----- |
bankStatement.us
| pretrained-read | GPT-4o-mini |     | 100   | 100 |     | 100   | 98.51 | 98.21 |
| --------------- | ----------- | --- | ----- | --- | --- | ----- | ----- | ----- |
| pretrained-read | GPT-4.1     |     | 100   | 100 |     | 100   | 98.51 | 100   |
| AzureAI4.0      | GPT-4o-mini |     | 100   | 100 |     | 100   | 97.59 | 98.21 |
| AzureAI4.0      | GPT-4.1     |     | 100   | 100 |     | 100   | 100   | 100   |
| MinerU          | GPT-4o-mini |     | 5.04  | 100 |     | 96.43 | 98.51 | 100   |
| MinerU          | GPT-4.1     |     | 0     | 100 |     | 100   | 100   | 100   |
| PyMuPDF         | GPT-4o-mini |     | 71.43 | 100 |     | 100   | 98.51 | 98.21 |
| PyMuPDF         | GPT-4.1     |     | 71.43 | 100 |     | 100   | 100   | 100   |
Continuedonnextpage
19

PublishedasaconferencepaperatICLR2026
Table6–Continuedfrompreviouspage
KeyInformationExtraction-NEDScore
| OCR                    | GPT         |          |           |           |         |               |
| ---------------------- | ----------- | -------- | --------- | --------- | ------- | ------------- |
|                        |             | BankName | AccHolder | AccNumber | Address | StatementDate |
| pdfium                 | GPT-4o-mini | 71.43    | 100       | 100       | 98.51   | 100           |
| pdfium                 | GPT-4.1     | 71.43    | 100       | 100       | 100     | 100           |
| Ours(templatematching) |             | 100      | 100       | 100       | 100     | 100           |
RHBBank(10UniquePDFs)
| prebuilt- | N/A | 100 | 90  | 100 | 92.01 | 100 |
| --------- | --- | --- | --- | --- | ----- | --- |
bankStatement.us
| pretrained-read        | GPT-4o-mini | 100   | 100   | 100 | 99.35 | 100   |
| ---------------------- | ----------- | ----- | ----- | --- | ----- | ----- |
| pretrained-read        | GPT-4.1     | 100   | 100   | 100 | 98.92 | 100   |
| AzureAI4.0             | GPT-4o-mini | 100   | 100   | 100 | 100   | 100   |
| AzureAI4.0             | GPT-4.1     | 100   | 100   | 100 | 98.92 | 100   |
| MinerU                 | GPT-4o-mini | 70    | 55.69 | 70  | 40    | 85    |
| MinerU                 | GPT-4.1     | 70    | 50    | 70  | 40    | 77.50 |
| PyMuPDF                | GPT-4o-mini | 93.03 | 100   | 100 | 98.92 | 100   |
| PyMuPDF                | GPT-4.1     | 100   | 100   | 100 | 98.92 | 100   |
| pdfium                 | GPT-4o-mini | 79.09 | 100   | 100 | 98.92 | 100   |
| pdfium                 | GPT-4.1     | 100   | 100   | 100 | 98.92 | 100   |
| Ours(templatematching) |             | 100   | 100   | 100 | 100   | 100   |
HongLeongBank(9UniquePDFs)
| prebuilt- | N/A | 100 | 88.89 | 100 | 100 | 100 |
| --------- | --- | --- | ----- | --- | --- | --- |
bankStatement.us
| pretrained-read        | GPT-4o-mini | 100   | 91.53 | 100 | 100   | 100 |
| ---------------------- | ----------- | ----- | ----- | --- | ----- | --- |
| pretrained-read        | GPT-4.1     | 100   | 100   | 100 | 100   | 100 |
| AzureAI4.0             | GPT-4o-mini | 100   | 91.53 | 100 | 97.99 | 100 |
| AzureAI4.0             | GPT-4.1     | 100   | 100   | 100 | 100   | 100 |
| MinerU                 | GPT-4o-mini | 11.85 | 88.89 | 100 | 100   | 100 |
| MinerU                 | GPT-4.1     | 50.88 | 100   | 100 | 100   | 100 |
| PyMuPDF                | GPT-4o-mini | 100   | 91.50 | 100 | 98.64 | 100 |
| PyMuPDF                | GPT-4.1     | 100   | 100   | 100 | 100   | 100 |
| pdfium                 | GPT-4o-mini | 100   | 91.50 | 100 | 97.80 | 100 |
| pdfium                 | GPT-4.1     | 100   | 100   | 100 | 100   | 100 |
| Ours(templatematching) |             | 100   | 100   | 100 | 100   | 100 |
AmBank(7UniquePDFs)
| prebuilt- | N/A | 100 | 85.71 | 100 | 100 | 100 |
| --------- | --- | --- | ----- | --- | --- | --- |
bankStatement.us
| pretrained-read        | GPT-4o-mini | 100   | 100 | 100 | 100   | 100 |
| ---------------------- | ----------- | ----- | --- | --- | ----- | --- |
| pretrained-read        | GPT-4.1     | 100   | 100 | 100 | 100   | 100 |
| AzureAI4.0             | GPT-4o-mini | 100   | 100 | 100 | 100   | 100 |
| AzureAI4.0             | GPT-4.1     | 100   | 100 | 100 | 100   | 100 |
| MinerU                 | GPT-4o-mini | 14.97 | 100 | 100 | 98.82 | 100 |
| MinerU                 | GPT-4.1     | 0     | 100 | 100 | 98.82 | 100 |
| PyMuPDF                | GPT-4o-mini | 8.57  | 100 | 100 | 100   | 100 |
| PyMuPDF                | GPT-4.1     | 0     | 100 | 100 | 100   | 100 |
| pdfium                 | GPT-4o-mini | 12.38 | 100 | 100 | 100   | 100 |
| pdfium                 | GPT-4.1     | 0     | 100 | 100 | 100   | 100 |
| Ours(templatematching) |             | 100   | 100 | 100 | 100   | 100 |
A.4 QUANTITATIVERESULTSFORTRANSACTIONTABLEEXTRACTION
WeevaluatetransactiontableextractionacrossthesamesixMalaysianbanks. Thistaskissubstantiallymore
challengingthankeyinformationextraction,asitrequireslocalizingtableboundaries,parsingmulti-pagetables
withvaryingrowcounts,andcorrectlyaligningfivecolumntypes:date,description,debit,credit,andbalance.
We report matching NED (tolerance for row-level alignment differences) in Table 8 and exact NED (strict
row-levelmatching)inTable9,F1scoresforrowdetectioninTable7,andper-bankbreakdownsinTables10
and11.
Overall Performance. Our template matching approach achieves the highest or near-highest performance
acrossallmetrics.OnmatchingNED,itattains100%ondateanddescriptioncolumns,91.12%ondebit,100%
20

PublishedasaconferencepaperatICLR2026
on credit, and 99.28% on balance, with an average of 98.08%. For exact NED, it achieves 98.08% (date),
98.35%(description),99.87%(debit),92.68%(credit),and100%(balance). TheF1scoreisaperfect100%
acrossallsixbanks,indicatingthatourmethodcorrectlyidentifiesalltransactionrowswithoutfalsepositives
ormissedentries. TheSurya+docTRpipelinewithGPT-5-miniistheclosestcompetitor,achieving98.95%
matchingNEDondateand96.94%average,withstrongF1scores(98.28–100%)acrossbanks.
LLM-Based vs. End-to-End Approaches. Configurations using GPT-4.1 as the structuring model consis-
tentlyoutperformthoseusingGPT-4o-miniorsmallermodels.Forinstance,docTR+GPT-4.1achieves95.28%
matchingNEDondescription,comparedto92.82%withGPT-4o-mini. Thegapwidensfornumericalfields:
debitmatchingNEDincreasesfrom80.00%(GPT-4o-mini)to98.78%(GPT-4.1)withdocTR.Thisindicates
thatlargerlanguagemodelsarebetteratparsingambiguousnumericalformats(e.g., MalaysianRinggitfor-
mattingwithcommasandperiods)andhandlingmulti-linetransactiondescriptions. Conversely, end-to-end
visionmodelsshowmixedresults.WhileolmOCRachievesreasonablematchingNED(77–91%percolumn),
its exact NED drops substantially (71–84%), indicating frequent minor character-level errors in numerical
fields. PPStructureV3andPaddleOCR-VL(0.9B)demonstratetheweakestoverallperformance,particularly
onbalancecolumns(43.79%and53.44%matchingNEDrespectively),likelyduetotheirlimitedtrainingon
SoutheastAsianfinancialdocumentformats.
Per-BankAnalysis. Performancevariesacrossbanksduetodifferencesinstatementformatting. PublicBank
statements,withtheircleantabularlayouts,achievenear-perfectextractionacrossmostconfigurations(100%
matchingNEDforourmethod).Incontrast,RHBBank’smulti-columnbalancepresentationandCIMBBank’s
merged description cells present greater challenges, reducing baseline performance by 5–15% on average.
HongLeongBankstatementswithwrappedtransactiondescriptionscausethelargestperformancedropsfor
text-basedextractors(PyMuPDF+GPT-4o-minidropsto70.91%datematchingNED).Thesebank-specific
challengesvalidatetheneedforrobustextractionpipelinesthatcangeneralizeacrossdiverseformats.
F1ScoreAnalysis. Row-leveldetectionaccuracy,measuredbyF1score(Table7),revealsthatourtemplate
matchingmethodandGPT-4.1-basedconfigurationsachievenear-perfectrowdetection(98–100%F1across
banks).PaddleOCR-basedmethodsshowthemostinconsistency,withF1scoresdroppingto10.26%onCIMB
Bankand14.29%onMaybankforPPStructureV3, indicatingcatastrophictabledetectionfailuresoncertain
bankformats. Thishighlightstheunreliabilityofgeneral-purposetabledetectionmodelsforproductionde-
ploymentonMalaysianbankstatementswithoutformat-specificadaptation.
Table7: F1scoresacrossallbanksfortransactiontableextraction.
| OCR                | GPT             | MBBE  | PBBE CIBB RHBB     | HLBB ARBK     |
| ------------------ | --------------- | ----- | ------------------ | ------------- |
| prebuilt-layout    | N/A             | 93.67 | 89.47 97.41 81.60  | 99.58 100.00  |
| PPStructureV3      | N/A             | 14.29 | 70.97 10.26 23.19  | 80.89 92.12   |
| docTR              | gpt-4o-mini     | 92.73 | 88.70 87.37 100.00 | 85.34 98.81   |
| docTR              | gpt-4.1         | 96.04 | 90.09 98.95 100.00 | 100.00 100.00 |
| docTR              | gpt-4.1-mini    | 91.74 | 97.30 81.14 88.24  | 91.38 96.93   |
| docTR              | gpt-4.1-nano    | 36.11 | 73.87 71.79 96.49  | 83.19 93.26   |
| docTR              | gpt-5-mini      | 98.71 | 96.43 100.00 94.74 | 91.21 100.00  |
| docTR              | gpt-5-mini(low) | 94.64 | 100.00 95.70 85.96 | 90.35 96.34   |
| docTR              | gpt-5-nano      | 94.64 | 91.89 98.95 66.67  | 68.38 97.01   |
| PyMuPDF            | gpt-4o-mini     | 94.64 | 89.26 87.18 100.00 | 76.19 98.20   |
| PyMuPDF            | gpt-4.1         | 94.69 | 92.59 98.95 100.00 | 99.58 100.00  |
| pdfium             | gpt-4o-mini     | 94.17 | 88.52 80.77 98.25  | 79.65 96.43   |
| pdfium             | gpt-4.1         | 93.75 | 83.64 99.47 100.00 | 98.31 98.81   |
| olmOCR-2-7B-1025   | N/A             | 87.93 | 63.04 100.00 73.68 | 83.84 98.20   |
| paddleOCR-VL(0.9B) | N/A             | 61.31 | 61.18 17.89 22.22  | 64.16 95.65   |
Surya+docTR gpt-5-mini(header) 100.00 100.00 98.96 98.28 99.15 100.00
| Ours(templatematching) |     | 100.00 | 100.00 100.00 100.00 | 100.00 100.00 |
| ---------------------- | --- | ------ | -------------------- | ------------- |
Table8:Averageper-columnmatchingNEDscoresacrossallbanksfortransactiontableextraction.
TransactionTableExtraction-MatchingNEDScore
| OCR             | GPT |             |              |         |
| --------------- | --- | ----------- | ------------ | ------- |
|                 |     | Date Desc   | Debit Credit | Balance |
| prebuilt-layout | N/A | 89.59 95.54 | 95.88 98.31  | 94.15   |
| PPStructureV3   | N/A | 63.29 66.43 | 74.30 82.56  | 43.79   |
Continuedonnextpage
21

PublishedasaconferencepaperatICLR2026
Table8–Continuedfrompreviouspage
TransactionTableExtraction-MatchingNEDScore
| OCR              |     | GPT             |             |              |         |
| ---------------- | --- | --------------- | ----------- | ------------ | ------- |
|                  |     |                 | Date Desc   | Debit Credit | Balance |
| docTR            |     | gpt-4o-mini     | 86.41 92.82 | 80.00 86.07  | 96.76   |
| docTR            |     | gpt-4.1         | 88.05 95.28 | 98.78 96.65  | 95.72   |
| docTR            |     | gpt-4.1-mini    | 88.48 94.60 | 86.79 91.85  | 94.66   |
| docTR            |     | gpt-4.1-nano    | 84.87 78.88 | 80.02 78.64  | 73.55   |
| docTR            |     | gpt-5-mini      | 86.64 97.73 | 93.74 94.78  | 96.00   |
| docTR            |     | gpt-5-mini(low) | 80.44 95.81 | 87.10 90.94  | 88.77   |
| docTR            |     | gpt-5-nano      | 82.65 90.68 | 79.31 80.05  | 92.55   |
| PyMuPDF          |     | gpt-4o-mini     | 88.45 93.29 | 86.07 88.72  | 95.17   |
| PyMuPDF          |     | gpt-4.1         | 87.13 95.79 | 97.80 97.08  | 96.02   |
| pdfium           |     | gpt-4o-mini     | 88.48 91.66 | 85.32 87.95  | 93.26   |
| pdfium           |     | gpt-4.1         | 88.08 92.85 | 99.69 95.03  | 93.46   |
| olmOCR-2-7B-1025 |     | N/A             | 82.94 90.53 | 82.58 79.08  | 77.87   |
| paddleOCR-VL     |     | N/A             | 79.18 58.94 | 69.44 80.67  | 53.44   |
(0.9B)
| Surya+docTR |     | gpt-5-mini | 98.95 98.59 | 90.79 97.97 | 98.39 |
| ----------- | --- | ---------- | ----------- | ----------- | ----- |
(header)
|     | Ours(templatematching) |     | 100 100 | 91.12 100 | 99.28 |
| --- | ---------------------- | --- | ------- | --------- | ----- |
Table9: Averageper-columnexactNEDscoresacrossallbanksfortransactiontableextraction.
TransactionTableExtraction-ExactNEDScore
| OCR              |     | GPT             |       |                   |         |
| ---------------- | --- | --------------- | ----- | ----------------- | ------- |
|                  |     |                 | Date  | Desc Debit Credit | Balance |
| prebuilt-layout  |     | N/A             | 83.52 | 75.34 89.29 94.29 | 78.31   |
| PPStructureV3    |     | N/A             | 55.79 | 42.70 58.65 72.54 | 47.19   |
| docTR            |     | gpt-4o-mini     | 83.83 | 79.91 68.45 82.04 | 78.35   |
| docTR            |     | gpt-4.1         | 85.42 | 92.80 98.95 98.35 | 96.72   |
| docTR            |     | gpt-4.1-mini    | 79.12 | 70.17 60.73 72.03 | 57.50   |
| docTR            |     | gpt-4.1-nano    | 75.73 | 54.52 63.43 70.45 | 56.24   |
| docTR            |     | gpt-5-mini      | 83.08 | 91.30 92.14 95.15 | 94.97   |
| docTR            |     | gpt-5-mini(low) | 74.88 | 71.20 65.70 72.59 | 59.10   |
| docTR            |     | gpt-5-nano      | 79.01 | 80.45 77.38 76.08 | 84.06   |
| PyMuPDF          |     | gpt-4o-mini     | 81.36 | 70.96 71.08 78.31 | 72.17   |
| PyMuPDF          |     | gpt-4.1         | 85.15 | 93.19 96.32 98.48 | 94.33   |
| pdfium           |     | gpt-4o-mini     | 83.03 | 75.67 74.08 81.01 | 77.19   |
| pdfium           |     | gpt-4.1         | 84.96 | 86.32 95.32 93.41 | 88.13   |
| olmOCR-2-7B-1025 |     | N/A             | 84.18 | 76.51 71.42 77.04 | 71.11   |
| paddleOCR-VL     |     | N/A             | 65.86 | 41.18 55.70 62.36 | 40.58   |
(0.9B)
| Surya+docTR |     | gpt-5-mini | 89.76 | 94.80 95.01 96.91 | 94.65 |
| ----------- | --- | ---------- | ----- | ----------------- | ----- |
(header)
|     | Ours(templatematching) |     | 98.08 | 98.35 99.87 92.68 | 100 |
| --- | ---------------------- | --- | ----- | ----------------- | --- |
Table10: TransactiontableextractionmatchingNEDgroupedbybankacrossOCRandGPTcon-
figurations.
TransactionTableExtraction-MatchingNEDScore
| OCR |     | GPT |                  |              |                 |
| --- | --- | --- | ---------------- | ------------ | --------------- |
|     |     |     | Date Description | Debit Credit | Balance Average |
Maybank(10UniquePDFs)
| prebuilt-layout |     | N/A         | 98.61  | 95.77 94.44 99.21   | 91.27 95.86 |
| --------------- | --- | ----------- | ------ | ------------------- | ----------- |
| PPStructureV3   |     | N/A         | 59.92  | 54.19 70.45 89.47   | 7.69 56.34  |
| PyMuPDF         |     | gpt-4o-mini | 85.59  | 91.16 88.98 97.46   | 89.83 90.60 |
| PyMuPDF         |     | gpt-4.1     | 100.00 | 95.64 100.00 100.00 | 92.37 97.60 |
Continuedonnextpage
22

PublishedasaconferencepaperatICLR2026
Table10–Continuedfrompreviouspage
TransactionTableExtraction-MatchingNEDScore
| OCR                | GPT         |                  |              |                 |
| ------------------ | ----------- | ---------------- | ------------ | --------------- |
|                    |             | Date Description | Debit Credit | Balance Average |
| pdfium             | gpt-4o-mini | 83.90 90.02      | 88.14 96.61  | 88.14 89.36     |
| pdfium             | gpt-4.1     | 81.92 57.24      | 61.02 37.85  | 22.03 52.01     |
| olmOCR-2-7B-1025   | N/A         | 100.00 98.39     | 99.15 99.15  | 95.76 98.49     |
| paddleOCR-VL(0.9B) | N/A         | 83.90 93.39      | 91.53 98.31  | 93.22 92.07     |
| Surya+docTR        | gpt-5-mini  | 97.46 93.96      | 98.31 99.15  | 89.83 95.74     |
| docTR              | gpt-4o-mini | 85.59 93.39      | 92.37 97.46  | 93.22 92.41     |
| docTR              | gpt-4.1     | 94.12 93.28      | 95.80 98.32  | 91.60 94.62     |
| docTR              | gpt-4o-mini | 85.59 92.80      | 92.37 96.61  | 92.37 91.95     |
| docTR              | gpt-4.1     | 95.60 92.16      | 99.16 98.32  | 89.92 95.03     |
| olmOCR-2-7B-1025   | N/A         | 73.37 85.79      | 92.31 88.46  | 78.46 83.68     |
| paddleOCR-VL(0.9B) | N/A         | 90.63 60.63      | 55.79 70.53  | 50.53 65.62     |
Surya+docTR gpt-5-mini(header) 100.00 100.00 90.66 100.00 99.83 98.10
Ours(templatematching) 100.00 100.00 90.66 100.00 99.25 97.98
PublicBank(10UniquePDFs)
| prebuilt-layout    | N/A         | 100.00 100.00 | 90.62 90.62  | 100.00 96.25 |
| ------------------ | ----------- | ------------- | ------------ | ------------ |
| PPStructureV3      | N/A         | 98.40 73.61   | 96.00 96.00  | 66.00 86.00  |
| PyMuPDF            | gpt-4o-mini | 89.06 91.60   | 82.81 85.94  | 93.75 88.63  |
| PyMuPDF            | gpt-4.1     | 70.49 81.92   | 100.00 81.97 | 81.97 83.27  |
| pdfium             | gpt-4o-mini | 92.98 97.75   | 87.72 87.72  | 98.25 92.88  |
| pdfium             | gpt-4.1     | 88.57 70.10   | 81.43 78.57  | 81.43 80.02  |
| olmOCR-2-7B-1025   | N/A         | 62.41 95.35   | 100.00 94.83 | 93.10 89.14  |
| paddleOCR-VL(0.9B) | N/A         | 44.64 99.20   | 98.21 98.21  | 100.00 88.05 |
| Surya+docTR        | gpt-5-mini  | 46.67 93.36   | 88.33 86.67  | 95.00 82.01  |
| docTR              | gpt-4o-mini | 98.51 91.00   | 89.55 89.55  | 92.54 92.23  |
| docTR              | gpt-4.1     | 70.69 86.21   | 93.10 86.21  | 86.21 84.48  |
| docTR              | gpt-4o-mini | 98.53 90.00   | 88.24 89.71  | 89.71 91.24  |
| docTR              | gpt-4.1     | 78.12 71.88   | 100.00 71.88 | 71.88 78.75  |
| olmOCR-2-7B-1025   | N/A         | 67.62 71.74   | 87.30 63.49  | 47.62 67.55  |
| paddleOCR-VL(0.9B) | N/A         | 89.49 64.53   | 94.07 97.46  | 55.93 80.30  |
Surya+docTR gpt-5-mini(header) 100.00 100.00 100.00 100.00 100.00 100.00
Ours(templatematching) 100.00 100.00 100.00 100.00 100.00 100.00
CIMBBank(10UniquePDFs)
| prebuilt-layout    | N/A         | 96.94 98.50  | 95.92 100.00 | 95.92 97.45  |
| ------------------ | ----------- | ------------ | ------------ | ------------ |
| PPStructureV3      | N/A         | 45.25 59.69  | 66.49 48.65  | 8.11 45.64   |
| PyMuPDF            | gpt-4o-mini | 90.57 85.03  | 71.03 71.03  | 100.00 83.53 |
| PyMuPDF            | gpt-4.1     | 97.92 97.91  | 97.92 97.92  | 100.00 98.33 |
| pdfium             | gpt-4o-mini | 96.74 92.53  | 75.00 78.26  | 96.74 87.85  |
| pdfium             | gpt-4.1     | 95.60 70.81  | 87.33 86.67  | 61.33 80.35  |
| olmOCR-2-7B-1025   | N/A         | 100.00 99.86 | 93.68 93.68  | 100.00 97.45 |
| paddleOCR-VL(0.9B) | N/A         | 93.81 94.98  | 79.38 83.51  | 93.81 89.10  |
| Surya+docTR        | gpt-5-mini  | 100.00 98.85 | 70.83 69.79  | 100.00 87.90 |
| docTR              | gpt-4o-mini | 92.55 85.97  | 79.09 78.18  | 92.73 85.70  |
| docTR              | gpt-4.1     | 97.92 97.92  | 97.92 97.92  | 100.00 98.33 |
| docTR              | gpt-4o-mini | 93.39 80.17  | 79.03 79.03  | 84.68 83.26  |
| docTR              | gpt-4.1     | 98.95 99.29  | 98.95 100.00 | 98.95 99.23  |
| olmOCR-2-7B-1025   | N/A         | 94.74 100.00 | 85.26 85.26  | 94.74 92.00  |
| paddleOCR-VL(0.9B) | N/A         | 54.91 58.73  | 77.46 77.46  | 9.83 55.68   |
Surya+docTR gpt-5-mini(header) 97.94 100.00 97.94 97.94 98.96 98.56
Ours(templatematching) 100.00 100.00 96.21 100.00 97.18 98.68
RHBBank(10UniquePDFs)
| prebuilt-layout | N/A         | 71.36 80.45 | 94.29 100.00 | 78.57 84.93  |
| --------------- | ----------- | ----------- | ------------ | ------------ |
| PPStructureV3   | N/A         | 16.10 45.22 | 48.36 71.31  | 17.21 39.64  |
| PyMuPDF         | gpt-4o-mini | 89.39 94.97 | 66.67 87.72  | 100.00 87.75 |
| PyMuPDF         | gpt-4.1     | 89.39 98.87 | 94.74 100.00 | 100.00 96.60 |
| pdfium          | gpt-4o-mini | 86.57 98.57 | 88.89 100.00 | 95.56 93.92  |
| pdfium          | gpt-4.1     | 89.41 89.03 | 88.14 94.92  | 100.00 92.30 |
Continuedonnextpage
23

PublishedasaconferencepaperatICLR2026
Table10–Continuedfrompreviouspage
TransactionTableExtraction-MatchingNEDScore
| OCR                | GPT         |                  |               |                 |
| ------------------ | ----------- | ---------------- | ------------- | --------------- |
|                    |             | Date Description | Debit Credit  | Balance Average |
| olmOCR-2-7B-1025   | N/A         | 89.42 98.28      | 85.00 93.33   | 88.33 90.87     |
| paddleOCR-VL(0.9B) | N/A         | 89.54 97.91      | 75.38 81.54   | 73.85 83.64     |
| Surya+docTR        | gpt-5-mini  | 91.05 72.65      | 56.58 59.21   | 93.42 74.58     |
| docTR              | gpt-4o-mini | 89.39 98.44      | 100.00 100.00 | 100.00 97.57    |
| docTR              | gpt-4.1     | 89.39 98.87      | 100.00 100.00 | 100.00 97.65    |
| docTR              | gpt-4o-mini | 89.58 97.09      | 91.38 91.38   | 100.00 93.88    |
| docTR              | gpt-4.1     | 89.39 98.99      | 100.00 100.00 | 100.00 97.68    |
| olmOCR-2-7B-1025   | N/A         | 91.46 93.84      | 59.72 62.50   | 56.94 72.89     |
| paddleOCR-VL(0.9B) | N/A         | 70.39 14.09      | 35.16 60.16   | 14.06 38.77     |
Surya+docTR gpt-5-mini(header) 96.61 93.22 86.36 91.53 95.58 92.66
Ours(templatematching) 100.00 100.00 89.39 100.00 99.74 97.83
HongLeongBank(10UniquePDFs)
| prebuilt-layout    | N/A         | 78.98 98.54 | 100.00 100.00 | 99.16 95.34  |
| ------------------ | ----------- | ----------- | ------------- | ------------ |
| PPStructureV3      | N/A         | 70.12 71.14 | 76.87 95.52   | 80.60 78.85  |
| PyMuPDF            | gpt-4o-mini | 70.91 94.57 | 75.19 78.95   | 96.99 83.32  |
| PyMuPDF            | gpt-4.1     | 78.80 97.32 | 100.00 100.00 | 100.00 95.22 |
| pdfium             | gpt-4o-mini | 73.09 92.71 | 88.10 92.06   | 95.24 88.24  |
| pdfium             | gpt-4.1     | 71.58 90.91 | 72.73 78.03   | 76.52 77.95  |
| olmOCR-2-7B-1025   | N/A         | 76.31 94.52 | 84.62 87.69   | 100.00 88.63 |
| paddleOCR-VL(0.9B) | N/A         | 70.74 92.94 | 84.00 88.80   | 77.60 82.82  |
| Surya+docTR        | gpt-5-mini  | 70.02 87.27 | 62.99 70.13   | 80.52 74.19  |
| docTR              | gpt-4o-mini | 71.70 92.91 | 60.14 70.63   | 93.71 77.82  |
| docTR              | gpt-4.1     | 78.98 98.46 | 100.00 100.00 | 98.32 95.15  |
| docTR              | gpt-4o-mini | 71.85 92.67 | 65.47 75.54   | 92.81 79.67  |
| docTR              | gpt-4.1     | 75.82 95.99 | 100.00 100.00 | 100.00 94.36 |
| olmOCR-2-7B-1025   | N/A         | 70.42 92.57 | 74.44 75.94   | 89.47 80.57  |
| paddleOCR-VL(0.9B) | N/A         | 69.65 59.63 | 61.28 79.57   | 97.45 73.51  |
Surya+docTR gpt-5-mini(header) 99.16 98.32 78.08 98.32 96.36 94.05
Ours(templatematching) 100.00 100.00 78.80 100.00 99.48 95.65
AmBank(10UniquePDFs)
| prebuilt-layout    | N/A         | 91.67 100.00 | 100.00 100.00 | 100.00 98.33 |
| ------------------ | ----------- | ------------ | ------------- | ------------ |
| PPStructureV3      | N/A         | 89.92 94.73  | 87.64 94.38   | 83.15 89.96  |
| PyMuPDF            | gpt-4o-mini | 92.94 99.58  | 95.29 95.29   | 100.00 96.62 |
| PyMuPDF            | gpt-4.1     | 91.67 100.00 | 100.00 100.00 | 100.00 98.33 |
| pdfium             | gpt-4o-mini | 97.62 96.02  | 92.86 96.43   | 94.05 95.39  |
| pdfium             | gpt-4.1     | 82.11 95.17  | 89.47 95.79   | 100.00 92.51 |
| olmOCR-2-7B-1025   | N/A         | 91.67 100.00 | 100.00 100.00 | 98.81 98.10  |
| paddleOCR-VL(0.9B) | N/A         | 100.00 96.42 | 94.12 95.29   | 94.12 95.99  |
| Surya+docTR        | gpt-5-mini  | 90.70 97.98  | 98.84 95.35   | 96.51 95.88  |
| docTR              | gpt-4o-mini | 92.94 98.04  | 95.29 96.47   | 98.82 96.31  |
| docTR              | gpt-4.1     | 91.67 100.00 | 100.00 100.00 | 100.00 98.33 |
| docTR              | gpt-4o-mini | 91.95 97.25  | 95.40 95.40   | 100.00 96.00 |
| docTR              | gpt-4.1     | 90.59 98.80  | 100.00 100.00 | 100.00 97.88 |
| olmOCR-2-7B-1025   | N/A         | 100.00 99.24 | 96.47 98.82   | 100.00 98.91 |
| paddleOCR-VL(0.9B) | N/A         | 100.00 96.00 | 92.86 98.81   | 92.86 96.11  |
Surya+docTR gpt-5-mini(header) 100.00 100.00 91.67 100.00 99.58 98.25
Ours(templatematching) 100.00 100.00 91.67 100.00 100.00 98.33
24

PublishedasaconferencepaperatICLR2026
Table11: TransactiontableextractionexactNEDgroupedbybankacrossOCRandGPTconfigu-
rations.
TransactionTableExtraction-ExactNEDScore
| OCR | GPT |                  |              |                 |
| --- | --- | ---------------- | ------------ | --------------- |
|     |     | Date Description | Debit Credit | Balance Average |
Maybank(10UniquePDFs)
| prebuilt-layout        | N/A                | 75.71 78.84 | 81.19 93.02 | 71.99 80.15 |
| ---------------------- | ------------------ | ----------- | ----------- | ----------- |
| PPStructureV3          | N/A                | 24.25 57.78 | 39.86 84.39 | 13.33 43.92 |
| PyMuPDF                | gpt-4o-mini        | 74.34 66.66 | 60.56 73.39 | 40 62.99    |
| PyMuPDF                | gpt-4.1            | 87.49 87.89 | 90.91 97.41 | 82.31 89.20 |
| pdfium                 | gpt-4o-mini        | 75.77 71.55 | 70.56 76.25 | 50 68.83    |
| pdfium                 | gpt-4.1            | 84.64 77.7  | 78.6 86.95  | 63.08 78.19 |
| olmOCR-2-7B-1025       | N/A                | 70.45 73.71 | 62.73 78.11 | 53.68 67.74 |
| paddleOCR-VL(0.9B)     | N/A                | 57.59 41.18 | 61.99 71.1  | 49.21 56.21 |
| Surya+docTR            | gpt-5-mini(header) | 90.07 99.16 | 100 100     | 100 97.85   |
| Ours(templatematching) |                    | 90.07 99.24 | 100 100     | 100 97.86   |
PublicBank(10UniquePDFs)
| prebuilt-layout        | N/A                | 94.39 25.27 | 85.36 89.82 | 41.94 67.36 |
| ---------------------- | ------------------ | ----------- | ----------- | ----------- |
| PPStructureV3          | N/A                | 91.39 15.05 | 82.74 90.28 | 30.28 61.95 |
| PyMuPDF                | gpt-4o-mini        | 89.17 67.78 | 68.39 85.42 | 70.47 76.25 |
| PyMuPDF                | gpt-4.1            | 72.14 89.91 | 93.33 96.67 | 90 88.41    |
| pdfium                 | gpt-4o-mini        | 94.44 64.97 | 67.97 85.56 | 70.2 76.63  |
| pdfium                 | gpt-4.1            | 75.14 79.91 | 100 84      | 80 83.81    |
| olmOCR-2-7B-1025       | N/A                | 93.52 48.11 | 85.71 65.81 | 48.26 68.28 |
| paddleOCR-VL(0.9B)     | N/A                | 82.15 21.84 | 79.17 81.74 | 51.48 63.28 |
| Surya+docTR            | gpt-5-mini(header) | 100 99.46   | 100 100     | 100 99.89   |
| Ours(templatematching) |                    | 100 100     | 100 100     | 100 100     |
CIMBBank(10UniquePDFs)
| prebuilt-layout    | N/A         | 88.69 85.53 | 87.94 90.48 | 83.18 87.16 |
| ------------------ | ----------- | ----------- | ----------- | ----------- |
| PPStructureV3      | N/A         | 32.12 38.08 | 50.24 41.41 | 23.41 37.05 |
| PyMuPDF            | gpt-4o-mini | 90.77 75.35 | 76.47 82.75 | 90.86 83.24 |
| PyMuPDF            | gpt-4.1     | 98.81 97.27 | 98.41 98.41 | 100 98.58   |
| pdfium             | gpt-4o-mini | 84.63 65.63 | 71.48 73.49 | 78.42 74.73 |
| pdfium             | gpt-4.1     | 97.62 90.02 | 93.33 89.52 | 85.71 91.24 |
| olmOCR-2-7B-1025   | N/A         | 95.56 98.32 | 85.95 85.95 | 93.62 91.88 |
| paddleOCR-VL(0.9B) | N/A         | 33.01 78.28 | 66.51 66.5  | 28.57 54.58 |
Surya+docTR gpt-5-mini(header) 91.09 83.2 77.55 89.8 70.68 82.47
| Ours(templatematching) |     | 91.43 95.22 | 100 100 | 100 97.33 |
| ---------------------- | --- | ----------- | ------- | --------- |
RHBBank(10UniquePDFs)
| prebuilt-layout    | N/A         | 73.66 66.77 | 86.36 92.42 | 72.73 78.39 |
| ------------------ | ----------- | ----------- | ----------- | ----------- |
| PPStructureV3      | N/A         | 49.35 21.28 | 63.21 81.24 | 49.23 52.86 |
| PyMuPDF            | gpt-4o-mini | 84.02 79.69 | 97.22 97.22 | 100 91.63   |
| PyMuPDF            | gpt-4.1     | 84.02 88.69 | 100 100     | 100 94.54   |
| pdfium             | gpt-4o-mini | 84.02 87.71 | 91.94 91.94 | 100 91.12   |
| pdfium             | gpt-4.1     | 84.02 73.51 | 100 100     | 100 91.5    |
| olmOCR-2-7B-1025   | N/A         | 84.02 90.75 | 78.05 76.67 | 76.67 81.23 |
| paddleOCR-VL(0.9B) | N/A         | 87.3 12.56  | 31.12 34.84 | 26.13 38.39 |
Surya+docTR gpt-5-mini(header) 88.19 97.42 92.5 91.67 98.61 93.68
| Ours(templatematching) |     | 84.02 99.53 | 100 100 | 100 96.71 |
| ---------------------- | --- | ----------- | ------- | --------- |
HongLeongBank(10UniquePDFs)
| prebuilt-layout  | N/A         | 77.05 95.7  | 94.87 100   | 100 93.53   |
| ---------------- | ----------- | ----------- | ----------- | ----------- |
| PPStructureV3    | N/A         | 51.35 48.21 | 33.54 59.51 | 67.87 52.09 |
| PyMuPDF          | gpt-4o-mini | 63.65 56.72 | 41.78 43.37 | 55.28 52.16 |
| PyMuPDF          | gpt-4.1     | 76.82 95.36 | 95.24 98.41 | 93.65 91.9  |
| pdfium           | gpt-4o-mini | 65.3 66.6   | 46.33 62.65 | 64.54 61.08 |
| pdfium           | gpt-4.1     | 76.71 97.58 | 100 100     | 100 94.86   |
| olmOCR-2-7B-1025 | N/A         | 63.84 57.34 | 31.29 61.15 | 64.43 55.61 |
Continuedonnextpage
25

PublishedasaconferencepaperatICLR2026
Table11–Continuedfrompreviouspage
TransactionTableExtraction-ExactNEDScore
| OCR                |     | GPT |       |             |              |                 |
| ------------------ | --- | --- | ----- | ----------- | ------------ | --------------- |
|                    |     |     | Date  | Description | Debit Credit | Balance Average |
| paddleOCR-VL(0.9B) |     | N/A | 46.95 | 47.44       | 76.48 83.72  | 86.88 68.3      |
Surya+docTR gpt-5-mini(header) 77.6 95.51 100 100 98.61 94.34
|     | Ours(templatematching) |     | 78.33 | 99.47 | 100 100 | 100 95.56 |
| --- | ---------------------- | --- | ----- | ----- | ------- | --------- |
AmBank(10UniquePDFs)
| prebuilt-layout    |                        | N/A                | 91.61 | 99.91 | 100 100     | 100 98.3    |
| ------------------ | ---------------------- | ------------------ | ----- | ----- | ----------- | ----------- |
| PPStructureV3      |                        | N/A                | 86.27 | 75.79 | 82.53 83.96 | 75.27 80.77 |
| PyMuPDF            |                        | gpt-4o-mini        | 86.18 | 79.54 | 82.04 87.69 | 76.4 82.37  |
| PyMuPDF            |                        | gpt-4.1            | 91.61 | 100   | 100 100     | 100 98.32   |
| pdfium             |                        | gpt-4o-mini        | 93.99 | 97.58 | 96.19 96.19 | 100 96.79   |
| pdfium             |                        | gpt-4.1            | 91.61 | 99.18 | 100 100     | 100 98.16   |
| olmOCR-2-7B-1025   |                        | N/A                | 97.71 | 90.81 | 84.76 94.52 | 90 91.56    |
| paddleOCR-VL(0.9B) |                        | N/A                | 88.17 | 45.76 | 18.92 36.28 | 1.19 38.07  |
| Surya+docTR        |                        | gpt-5-mini(header) | 91.61 | 94.03 | 100 100     | 100 97.13   |
|                    | Ours(templatematching) |                    | 91.61 | 100   | 100 100     | 100 98.32   |
A.5 LATENCYANDCOSTANALYSIS
Practicaldeploymentofbankstatementextractionsystemsrequirescarefulconsiderationofprocessinglatency
and operational cost. We provide latency measurements for both key information extraction (Table 12) and
transaction table extraction (Table 13), along with cost analysis for table extraction (Table 14). All latency
measurementsarereportedinsecondsperdocument,decomposedintoOCRprocessingtimeandGPTinference
timewhereapplicable.
|     | Table12: | Latencyanalysisforkeyinformationextraction(seconds). |           |      |                |                |
| --- | -------- | ---------------------------------------------------- | --------- | ---- | -------------- | -------------- |
|     |          |                                                      | OCR       |      | GPT            | Total          |
| OCR |          | GPT                                                  |           |      |                |                |
|     |          |                                                      | Min. Avg. | Max. | Min. Avg. Max. | Min. Avg. Max. |
Prebuilt-BankStatement.us N/A N/A N/A N/A N/A N/A N/A 5.26 9.28 17.27
Pretrained-Read gpt-4o-mini 1.64 3.26 6.07 0.88 1.70 3.64 2.52 4.96 7.90
Pretrained-Read gpt-4.1 1.61 2.87 5.15 0.59 0.96 4.16 2.34 3.83 7.07
AzureAI4.0 gpt-4o-mini 1.03 1.71 3.41 1.12 1.71 3.41 2.37 3.34 5.01
AzureAI4.0 gpt-4.1 1.01 1.42 2.35 0.63 1.09 3.65 1.86 2.72 5.50
docTR gpt-4o-mini 0.32 0.63 1.31 1.00 1.75 5.49 1.34 2.38 6.51
| docTR |     | gpt-4.1 | 2.96 5.20 | 7.59 | 0.54 0.94 2.93 | 3.58 6.13 8.56 |
| ----- | --- | ------- | --------- | ---- | -------------- | -------------- |
MinerU gpt-4o-mini 28.69 32.18 38.72 1.27 2.05 3.62 30.10 34.24 41.88
MinerU gpt-4.1 33.51 44.32 55.03 0.83 1.18 8.40 34.38 45.50 60.62
PyMuPDF gpt-4o-mini 0.00 0.02 0.04 0.95 1.85 3.89 0.97 1.86 3.92
| PyMuPDF |     | gpt-4.1 | 0.00 0.01 | 0.04 | 0.56 0.80 1.46 | 0.57 0.81 1.47 |
| ------- | --- | ------- | --------- | ---- | -------------- | -------------- |
PyMuPDF-Formatted gpt-4o-mini 0.01 0.02 0.05 0.85 1.50 6.08 0.87 1.53 6.10
PyMuPDF-Formatted gpt-4.1 0.00 0.02 0.06 0.53 0.72 1.36 0.55 0.74 1.39
Pdfium gpt-4o-mini 0.00 0.02 0.09 0.95 1.84 4.91 0.97 1.86 4.92
| Pdfium |     | gpt-4.1 | 0.00 0.01 | 0.03 | 0.54 0.85 1.66 | 0.55 0.86 1.67 |
| ------ | --- | ------- | --------- | ---- | -------------- | -------------- |
Ours(templatematching) 0.01 0.01 0.01 N/A N/A N/A 0.01 0.01 0.01
Key Information Extraction Latency. The latency profiles for key information extraction (Table 12) re-
veal substantial variation across pipeline configurations. Text-based extractors (PyMuPDF, Pdfium) achieve
near-instantaneousOCRprocessing(0.01–0.02saverage),withtotallatencydominatedbytheGPTinference
component. PyMuPDF + GPT-4.1 achieves the lowest average total latency at 0.81 seconds, followed by
PyMuPDF-Formatted+GPT-4.1at0.74seconds. Ourtemplatematchingmethodaverages0.01secondsper
document,makingitthefastestconfigurationoverallwhileeliminatingdependencyonexternalAPIs. Cloud-
basedOCRsolutionsintroducehigherlatency: Pretrained-Readaverages2.87–3.26secondsforOCRalone,
whileMinerUexhibitsthehighestlatencyat34–45secondsaverageduetoitscomputationallyintensivedoc-
umentunderstandingpipeline.ThePrebuilt-BankStatementendpoint(Azure’sturnkeysolution)averages9.28
secondstotalbutdoesnotexposeseparateOCR/GPTcomponents. DocTRpresentsaninterestingtrade-off:
itsOCRcomponentisfast(0.63saveragewithGPT-4o-mini)butincreasessubstantiallywithGPT-4.1(5.20s),
suggestingthattherenderingandimagepreparationstepscaleswithdownstreammodelexpectations.
26

PublishedasaconferencepaperatICLR2026
Table13: Latencyanalysisfortransactiontableextraction(seconds).
|                 |     |      | OCR  |      | GPT       |           | Total |       |
| --------------- | --- | ---- | ---- | ---- | --------- | --------- | ----- | ----- |
| OCR             | GPT |      |      |      |           |           |       |       |
|                 |     | Min. | Avg. | Max. | Min. Avg. | Max. Min. | Avg.  | Max.  |
| prebuilt-layout | N/A | N/A  | N/A  | N/A  | N/A N/A   | N/A 2.56  | 4.58  | 7.46  |
| PPStructureV3   | N/A | N/A  | N/A  | N/A  | N/A N/A   | N/A 15.26 | 40.95 | 98.17 |
docTR gpt-4o-mini 0.78 1.18 1.59 1.32 6.41 14.83 2.30 7.59 15.93
docTR gpt-4.1 0.34 0.89 1.56 0.89 11.03 153.16 2.07 11.92 153.50
docTR gpt-4.1-mini 0.57 0.96 1.60 1.12 5.38 12.47 2.08 6.33 13.51
docTR gpt-4.1-nano 0.28 0.67 1.02 1.14 3.13 6.59 1.76 3.80 7.31
docTR gpt-5-mini 0.30 0.74 1.19 11.15 24.54 54.64 11.70 25.27 55.20
docTR gpt-5-mini(low) 0.66 1.07 1.54 1.48 5.77 11.64 2.74 6.84 12.93
docTR gpt-5-nano 0.36 0.87 1.76 7.47 31.51 60.65 8.07 32.38 61.23
PyMuPDF gpt-4o-mini 0.00 0.01 0.04 1.08 4.97 12.12 1.09 4.98 12.13
PyMuPDF gpt-4.1 0.00 0.01 0.05 0.84 10.72 157.78 0.85 10.72 157.79
pdfium gpt-4o-mini 0.00 0.02 0.04 1.36 6.19 16.90 1.39 6.21 16.92
pdfium gpt-4.1 0.00 0.02 0.04 0.77 11.17 155.22 0.79 11.19 155.23
olmOCR-2-7B-1025 N/A N/A N/A N/A N/A N/A N/A 42.58 104.45 175.93
paddleOCR-VL(0.9B) N/A 23.20 150.10 341.10 N/A N/A N/A 23.20 150.10 341.10
Surya+docTR gpt-5-mini(header) 2.26 4.28 7.34 0.75 1.19 1.85 1.67 2.51 9.19
Ours(templatematching) 0.10 0.11 0.13 N/A N/A N/A 0.10 0.11 0.13
TransactionTableExtractionLatency.Tableextractionlatency(Table13)isgenerallyhigherthankeyinfor-
mationextractionduetotheincreasedcomplexityofparsingmulti-pagetabulardata. Ourtemplatematching
methodachievesthefastestaveragetotallatencyat0.11seconds,followedbytheSurya+docTRpipelineat
2.51secondsandtheprebuilt-layoutAPIat4.58seconds. GPT-4.1-basedconfigurationsexhibithighlatency
variancewithmaximumprocessingtimesreaching153–158secondsforcertaindocuments,likelycausedby
complexmulti-pagestatementsthatrequireextensivereasoning.Incontrast,GPT-4o-miniconfigurationsmain-
tainmoreconsistentlatency(4.97–7.59saverage),suggestingthatsmallermodels,whilelessaccurate,provide
morepredictableprocessingtimessuitableforlatency-sensitiveproductionenvironments. End-to-endvision
modelsexhibitthehighestlatencies: PaddleOCR-VLaverages150.10secondsandolmOCRaverages104.45
seconds,makingthemimpracticalforreal-timeprocessingofbankstatements. GPT-5-miniandGPT-5-nano,
despitebeingmorerecentmodels,showelevatedlatency(25.27sand32.38srespectively)duetotheirreasoning
tokenoverhead.
CostAnalysis. Thecost analysisfor tableextraction(Table 14)reveals thatper-document processingcosts
varyfromeffectivelyzero(templatematching,open-sourcemodels)to$0.01perPDF(GPT-4.1,GPT-5-mini).
GPT-4.1-nano offers the lowest API cost at $0.03 total, while GPT-4.1 incurs the highest at $0.53 due to
itslargerpromptandcompletiontokenconsumption. Reasoning-capablemodels(GPT-5-mini,GPT-5-nano)
allocateasignificantproportionoftheircompletioncosttoreasoningtokens($0.35outof$0.43forGPT-5-
mini), which explains both their improved accuracy and higher cost. The Surya + docTR with GPT-5-mini
(header)configurationachievesthebestcost-accuracybalanceamongAPI-dependentsolutionsatonly$0.02
totalcostwhileachieving96.94%averagematchingNED.Ourtemplatematchingapproachandopen-source
models (olmOCR, PaddleOCR-VL) incur no API cost, though they require local compute resources. For a
productiondeploymentprocessinghundredsofbankstatementsdaily,thecumulativecostdifferencebetween
configurationsbecomessignificant,makingthetemplatematchingapproachadvantageousforhigh-throughput
scenarios.
Table14: Costanalysisfortransactiontableextraction(USD).TotalcostrepresentsaggregateAPI
expensesacrossalldocumentsintheevaluationdatasetwherePerPDFshowstheaveragecostper
individualdocument.
|                 |              |        | TokenCost  |      |                 | CostBreakdown |     |        |
| --------------- | ------------ | ------ | ---------- | ---- | --------------- | ------------- | --- | ------ |
| OCR             | GPT          |        |            |      |                 |               |     |        |
|                 |              | Prompt | Completion |      | Total Reasoning | Comp-Reason   |     | PerPDF |
| prebuilt-layout | N/A          | N/A    |            | N/A  | N/A N/A         |               | N/A | N/A    |
| PPStructureV3   | N/A          | N/A    |            | N/A  | N/A N/A         |               | N/A | N/A    |
| docTR           | gpt-4o-mini  | N/A    |            | N/A  | N/A N/A         |               | N/A | N/A    |
| docTR           | gpt-4.1      | 0.19   |            | 0.34 | 0.53 N/A        |               | N/A | 0.01   |
| docTR           | gpt-4.1-mini | 0.04   |            | 0.07 | 0.11 N/A        |               | N/A | 0.00   |
| docTR           | gpt-4.1-nano | 0.01   |            | 0.02 | 0.03 N/A        |               | N/A | 0.00   |
Continuedonnextpage
27

PublishedasaconferencepaperatICLR2026
Table14–Continuedfrompreviouspage
|                        |                    | TokenCost         |                 | CostBreakdown |        |
| ---------------------- | ------------------ | ----------------- | --------------- | ------------- | ------ |
| OCR                    | GPT                |                   |                 |               |        |
|                        |                    | Prompt Completion | Total Reasoning | Comp-Reason   | PerPDF |
| docTR                  | gpt-5-mini         | 0.02 0.43         | 0.45 0.35       | 0.08          | 0.01   |
| docTR                  | gpt-5-mini(low)    | 0.02 0.08         | 0.10 0.00       | 0.08          | 0.00   |
| docTR                  | gpt-5-nano         | 0.00 0.24         | 0.25 0.23       | 0.02          | 0.00   |
| PyMuPDF                | gpt-4o-mini        | 0.01 0.03         | 0.04 N/A        | N/A           | 0.00   |
| PyMuPDF                | gpt-4.1            | N/A N/A           | N/A N/A         | N/A           | N/A    |
| pdfium                 | gpt-4o-mini        | N/A N/A           | N/A N/A         | N/A           | N/A    |
| pdfium                 | gpt-4.1            | N/A N/A           | N/A N/A         | N/A           | N/A    |
| olmOCR-2-7B-1025       | N/A                | N/A N/A           | N/A N/A         | N/A           | N/A    |
| paddleOCR-VL(0.9B)     | N/A                | N/A N/A           | N/A N/A         | N/A           | N/A    |
| Surya+docTR            | gpt-5-mini(header) | 0.01 0.01         | 0.02 0.00       | 0.01          | 0.00   |
| Ours(templatematching) |                    | N/A N/A           | N/A N/A         | N/A           | N/A    |
Note:
1.N/Aindicatedatanotavailableornotapplicable.
2.Prompt=Prompttokencost.
3.Completion=Completiontokencost.
4.Reasoning=Reasoningtokencost.
5.Comp-Reason=Completioncostminusreasoningcost.
6.PerPDF=AveragecostperPDFdocument.
7.OCR=OCRprocessingtimeinseconds.
8.GPT=GPTinferencetimeinseconds.
9.Total=Totalprocessingtimeinseconds.
A.6 ABLATIONSTUDIESFORCREDITSCORING
A.6.1 CREDITSCOREDISTRIBUTION
WeevaluatethescoredistributionofourLogisticRegressionbaselineacrossthreefeaturesetconfigurations:
application information only, bank statement only, and blended. Figure 4–6 present score distributions for
goodaccounts(green)andbadaccounts(red),withEarthMover’sDistance(EMD)quantifyingdistributional
divergenceasameasureofdiscriminatorypower.
Application Information: Figure 4 shows limited separation between good and bad accounts when using
applicationfeaturesalone. Thehistogramandkerneldensityestimation(KDE)curvesrevealgoodaccounts
clusteringathigherscores(meanof665.7)andbadaccountsatlowerscores(meanof641.5),yieldinganEMD
of24.11. Thismodestdivergenceindicatesreasonablebutconstraineddiscriminatorypowerfromtraditional
applicationdata.
BankStatement: Figure5demonstratesmarkedlyimprovedseparationwhenusingbankstatementfeatures.
Goodaccountsexhibitameanscoreof699.2whilebadaccountsconcentratenear625.7. TheEMDincreases
to74.48, a3.1×improvementoverapplicationinformationalone, reflectingthestrongersignalprovidedby
transactional cash flow indicators. This result suggests bank statement-derived features create more distinct
riskprofiles.
Blended: Figure 6 displays the combined model using both application and bank statement features. This
blendedapproachachievesthestrongestdistributionseparation,withgoodaccountscenterednear708.4and
bad accounts near 612.6. The EMD reaches 96.84, a 4.0× improvement over application information and
1.3×overbankstatementalone,demonstratingthatcombiningfeaturesourcesenhancesdiscriminatorypower
beyondeitherindividualapproach.TheprogressiveEMDimprovementfrom24.11(applicationonly)to74.48
(bankstatement)to96.84(blended)alsoshowsthattransaction-derivedfeaturesaretheprimarydriverofscore
separationbetweengoodandbadaccounts.
A.6.2 REJECTEDCASESANALYSIS
ProblemStatement. Creditscoringmodelstrainedexclusivelyonapprovedapplicantssufferfromselection
bias,astheycaptureonlythesubsetoftheapplicantpopulationdeemedacceptablebyhistoricalunderwriting
decisions(Ehrhardtetal.,2021). Thiscreatesatwo-foldproblem: (1)themodellacksevidenceabouthow
rejectedapplicantswouldhaveperformedifapproved,leadingtopotentialunderestimationofactualportfolio
risk,and(2)themodel’sdecisionboundaryiscalibratedtoabiaseddistributionratherthanthetrueapplicant
28

PublishedasaconferencepaperatICLR2026
16
14
12
10
8
6
4
2
0
567 587 607 627 647 667 687 707 727 747 767 787
Score Points
ytisneD
/
ycneuqerF
Score Distribution Chart:
Logistic Regression - Application Info Features
Earth Mover's Distance: 24.11 Good Accounts (Histogram)
Bad Accounts (Histogram)
Good Accounts (Smoothed)
Bad Accounts (Smoothed)
Good Mean: 665.7
Bad Mean: 641.5
Figure 4: Score distribution for the application information model. Good accounts (green) cluster
at higher scores (mean 665.7) while bad accounts (red) concentrate lower (mean 641.5). EMD of
24.11indicatesmoderatediscriminatorypower.
population(Insights,2024). Toaddressthislimitation,weconductedrejectedcasesanalysison264rejected
loanapplicants.
Methodology. This analysis applies the scorecard model developed on approved applicants to the rejected
population, generating predicted risk scores without retraining. This non-augmentation approach allows us
to assess model consistency and identify systematic characteristics that distinguish rejected from approved
applicants.Byscoringrejectedapplicantswiththeexistingmodel,wecanobservewhetherrejectiondecisions
alignwithpredictedriskprofilesandunderstandthekeyfinancialbehaviorsdrivingrejectiondecisions.
ApplyingourLogisticRegressionscorecardtotheserejectedapplicantsrevealsthat96.97%(256of264)are
classified as high risk, 3.03% (8 of 264) as medium risk, and 0% as low risk (Table 15). This distribution
demonstratesstrongalignmentbetweentheconsultingfirm’srejectiondecisionsandourmodel’sriskassess-
ment, validatingthatthescorecardaccuratelycapturestheunderlyingriskfactorsthatmotivatedoriginalre-
jection decisions. Critically, no rejected applicant scored in the low-risk category, indicating that rejection
decisionswerenotarbitrarybutrathergroundedingenuinecreditriskindicatorsobservableintransactiondata.
Table15: RiskDistributionofRejectedLoanApplicantsviaScorecardModelPrediction
RiskLevel HighRisk MediumRisk LowRisk
Count 256(96.97%) 8(3.03%) 0(0.00%)
Implications.Thisanalysisservestwocriticalpurposes.First,itvalidatesthatourscorecardmodelgeneralizes
consistentlytotherejectedpopulation,withrejectiondecisionsstronglyalignedtopredictedrisk. Second,it
provides evidence that bank statements contain sufficient cash flow signal to identify high-risk applicants,
andthatrejectiondecisionsweredata-drivenratherthanarbitrary. Thefindingthatallrejectedapplicantsare
eitherhighormediumrisk,withaconcentrationinhighrisk,suggestingthattheconsultingfirm’shistorical
underwritingwasappropriatelyconservativeandthatourmodelcapturesthelegitimateriskfactorsunderlying
thosedecisions.Theseresultsstrengthenconfidencethatthescorecardcanbereliablyextendedtonewapplicant
populationswithlimitedcredithistory.
29

PublishedasaconferencepaperatICLR2026
8
6
4
2
0
416 436 456 476 496 516 536 556 576 596 616 636 656 676 696 716 736 756 776 796 816 836 856 876 896 916 936 956 976 996 1016 1036
Score Points
ytisneD
/
ycneuqerF
Score Distribution Chart:
Logistic Regression - Bank Statement Features
Earth Mover's Distance: 74.48 Good Accounts (Histogram)
Bad Accounts (Histogram)
Good Accounts (Smoothed)
Bad Accounts (Smoothed)
Good Mean: 699.2
Bad Mean: 625.7
Figure5: Scoredistributionforthebankstatementmodel. Bankstatement-derivedcashflowindi-
catorsproducestrongerseparationwithgoodaccounts(mean699.2)andbadaccounts(mean625.7)
showingclearerdivergence. EMDof74.48(3.1×higherthanapplicationinformation)reflectsthe
discriminatoryadvantageoftransactionaldata.
8
7
6
5
4
3
2
1
0
374 394 414 434 454 474 494 514 534 554 574 594 614 634 654 674 694 714 734 754 774 794 814 834 854 874 894 914 934 954 974 994 1014
Score Points
ytisneD
/
ycneuqerF
Score Distribution Chart:
Logistic Regression - Blended Features
Earth Mover's Distance: 96.84 Good Accounts (Histogram)
Bad Accounts (Histogram)
Good Accounts (Smoothed)
Bad Accounts (Smoothed)
Good Mean: 708.4
Bad Mean: 612.6
Figure 6: Score distribution for the blended model. Combining application and bank statement
featuresachievesthestrongestseparationwithgoodaccounts(mean708.4)andbadaccounts(mean
612.6) showing maximal divergence. EMD of 96.84 (4.0× higher than application information
alone)demonstratescomplementaryvalueofbothfeaturesources.
30

PublishedasaconferencepaperatICLR2026
B DEPLOYMENT AND OPERATIONAL FRAMEWORK
ThesixthphaseofCRISP-DMfocusesonthedeploymentoftheproposedcashflowunderwritingworkflow
inaproductionenvironment.Thisworkflowisdesignedtoleverageverifiabletransactiondatatoenabletrans-
parentandevidence-basedcreditdecisionswhileestablishingacontinuousfeedbackcyclefordatacollection,
modelretraining,andperformancemonitoringwithinexistingcorebankingsystems. Tosupportthis,arobust
machinelearningoperationsframeworkisimplementedtostructuretheend-to-endpipelineintofivekeystages.
Lastly,anintegratedcreditscoringframeworkisintroducedtoprovidecomprehensiveriskevaluationforboth
establishedandnew-to-creditMSMEs.
B.1 DATAINGESTION
Thepipelinebeginswhenbankstatementsarereceived. Extractionmodulesparseandstructuretherawtrans-
actiondatausingOCRandlayoutanalysistechniques. Thisprocesstransformsunstructureddocumentsinto
astandardizedtabularformatsuitablefordownstreamprocessing. Theingestionstagealsoperformsintegrity
verificationanddatavalidationcheckstoensuredocumentauthenticity.
B.2 FEATUREENGINEERINGANDFEATURESTORE
Followingingestion,structureddataarefedintothefeatureengineeringmodule,whichcomputestransaction-
derivedandbehavioralfeatures.Thesefeaturesaretime-stamped,versioned,andstoredinacentralizedreposi-
tory.Thefeaturestoreprovidesasinglesourceoftruthforbothtrainingandinference,ensuringthesamelogic
usedtogeneratehistoricalfeaturesisconsistentlyappliedtonewapplicantsinrealtime.Thisdesignguarantees
reproducibility,preventsfeatureskew,andsupportstraceabilityacrossmodeliterations.
B.3 CONTINUOUSINTEGRATION(CI)
TheCIpipelineautomatesmodelretrainingandvalidationpriortointegrationintotheproductionregistry. It
istriggeredbytwoprimaryevents: (1)apredefinedschedule(e.g.,annually)whennewlabeleddatabecome
availablefromthecorebankingsystem,and(2)alertsfromthemonitoringsystemindicatingpotentialmodel
or data drift. Upon activation, the pipeline retrieves the latest versioned feature set and ground truth labels,
retrainsthemodel, andevaluatesitsperformanceagainstthecurrentproductionmodelusingpredefinedand
consistentevaluationmetrics.
B.4 MODELREGISTRYANDCONTINUOUSDEPLOYMENT(CD)
Iftheretrainedmodeldemonstratessuperiorperformance,itisautomaticallyversionedandstoredinthemodel
registry.TheCDprocessthenpackagesthevalidatedmodelintoacontainerizedmicroserviceanddeploysitas
asecureRESTAPIendpoint.Toensurereliabilityandminimizeproductionrisk,acanarydeploymentstrategy
isapplied,initiallyroutingasmallfractionoflivetraffictothenewmodelforperformancevalidationbefore
full-scalerollout.
B.5 CONTINUOUSMONITORINGANDFEEDBACKLOOP
Once the bank statement-based credit scoring model is deployed, it operates within a Champion-Challenger
framework(Kimetal.,2019)toenablecontinuousperformanceoptimization. TheChampionmodelservesas
thecurrentproductionbaseline,whileoneormoreChallengermodelsareperiodicallyretrainedonthelatest
dataandevaluatedinparallel. Modelperformanceiscontinuouslymonitoredandcomparedacrosspredefined
metrics. When a Challenger consistently outperforms the Champion, the system automatically notifies des-
ignatedbankofficerstoreviewtheresultsandpromotethenewmodeltoproduction. Thisapproachensures
sustainedmodelimprovement,robustness,andoperationalstability.
B.6 INTEGRATEDCREDITSCORINGFRAMEWORK
Inproduction,thecashflowunderwritingsystemfunctionsasanintegrateddecisionengineembeddedwithin
the lending process. Upon submission of bank statements, AI modules automatically extract and structure
therawdatausingOCRandnaturallanguageprocessingmodels. Theprocesseddatathenundergoesfraud
detection,cashflowanalysis,andnetworkanalyticstogeneratetransaction-derivedfeaturesandcreditscores
for MSME applicants. The existing bureau-based scorecard, designed for borrowers with established credit
histories, operates in parallel with the newly developed cash flow-based model. Each model independently
producesariskrating,andariskoverridemechanismensuresconservativedecisioning;ifeithermodelindicates
higherrisk,thefinalclassificationadoptsthatrating. Thisframeworkprovidesatransparent,evidence-based,
31

PublishedasaconferencepaperatICLR2026
anddata-drivenapproachtoMSMEcreditassessmentusingadaptive,explainableAIscoring. Italsoextends
financialaccesstonew-to-creditbusinessesthroughverifiabletransactiondata.
C LIMITATIONS AND FUTURE WORK
Thisworkhasseverallimitationsthatshouldbeaddressedinfutureresearch. First,thedatasetcomprises611
loanapplicationsfromasingleMalaysianconsultingfirm. Whilethedatasetrepresentsreal-worldproduction
datacollectedoveratwo-yearperiod,thesamplesizeisconstrainedbythepracticalrealitiesofMSMElend-
inginemergingmarkets,wheredataavailabilityremainslimitedduetostringentdataprivacyandregulatory
requirements. Future work should validate these findings across multiple institutions and larger datasets as
additionalMSMElendingdatabecomeavailable.
Second,theclassimbalanceinourdataset(518non-defaultvs.93defaultcases)reflectsthenaturaldistribution
observedinreal-worldlendingportfolios,wherethemajorityofborrowerssuccessfullyrepaytheirloans.While
thisimbalanceposesmodelingchallenges, itaccuratelyreflectsreal-worldcreditrisksettings. Inthiswork,
weaddressedthislimitationthroughappropriatemodelselection,WOE-basedfeatureengineering,andcareful
evaluationusingAUROC,whichisrobusttoclassimbalance.Itisimportanttonotethatclassimbalanceisnot
alimitationthatcanbefullyeliminated,butratheraninherentcharacteristicofcreditscoringdatasets.Ascredit
assessmentmodelsimproveandlendingdecisionsbecomemoreaccurate,successfulrepaymentratesincrease,
thereby maintaining or even intensifying this natural imbalance. Nevertheless, future studies could explore
advancedresamplingtechniquesorcost-sensitivelearningmethodstofurtherenhancemodelperformanceon
minorityclassprediction.
Third,whilewedescribemultipleAImodulesfordocumentprocessing,frauddetection,andtransactionanal-
ysiswithintheproposedend-to-endcashflowunderwritingworkflow,theevaluationfocusesonoverallcredit
scoringperformanceratherthantheeffectivenessofindividualmodules. However,detailedmodule-levelas-
sessmentisconstrainedbytheuseofproprietarymethodsandsensitiveoperationaldatathatcannotbepub-
liclydisclosed. Futureworkutilizingsyntheticoranonymizeddatacouldenablemoregranularmodule-level
analysisandbenchmarking.Additionally,futureresearchcouldexploreformalizingthesemodulesasfullyau-
tonomousagents,enablingthedevelopmentofamulti-agentcreditscoringarchitecturewithclearerinter-agent
responsibilitiesandinteractions.
Fourth,theproposedworkflowhasbeendeployedinaproductionenvironmentwithoneMalaysianconsulting
firm. Whilethisdemonstratesreal-worldapplicability,broadervalidationacrossdifferentlendinginstitutions,
regulatoryenvironments,andMSMEsegmentswouldstrengthenthegeneralizabilityofourfindings. Further
research is needed to systematically integrate the proposed cash flow underwriting workflow with existing
credit assessment systems that rely on behavioral and credit bureau data, ensuring coherent and robust risk
evaluation. Additionally,longitudinalstudiesexaminingmodelperformancestabilityacrosseconomiccycles
wouldprovidevaluableinsightsintothetemporalrobustnessandadaptabilityofbankstatement-basedfeatures
undervaryingmacroeconomicconditions.
32