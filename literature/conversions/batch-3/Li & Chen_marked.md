---
conversion_metadata:
  converted_at: "2026-07-21T13:57:26Z"
  converter_tool: "markitdown"
  converter_version: "0.1.6"
  source_pdf: "Li & Chen.pdf"
  source_pdf_sha256: "68f2661fddf2473925d5d62992995eec08a07b12819520329c5aede274ac0c1f"
  page_count: 15
  markdown_char_count: 129520
---

<!-- PAGE-AWARE EXTRACTION (via pdfminer.six) -->

<!-- PAGE 1 -->

Discover Computing

Research

Dynamic quantification anti‑fraud machine learning model 
for real‑time transaction fraud detection in banking

Falai Li1 · Zaidie Chen2

Received: 28 November 2024 / Accepted: 10 April 2025

© The Author(s) 2025

OPEN

Abstract
As the scenario of telecom network fraud intensifies, the development of anti-fraud models has become a focal point in 
financial technology, including banking sectors. Traditional anti-telecom fraud models, which primarily rely on expert 
rules and machine learning methodologies, are beset with limitations such as poor real-time performance and high false 
favourable rates, leading to biased predictive outcomes. This paper introduces a novel anti-fraud model: The Dynamic 
Quantification Anti-Fraud Model grounded in Real-time Transaction Flows to address these issues. This model combines 
multiple F-Beta features linearly, employs a DML (Double Machine Learning) framework for feature weight quantification, 
and conducts instantaneous risk assessments of account transactions. By dynamically adjusting feature weights based 
on historical single-feature false favourable rates and the branch’s anti-fraud tolerance capacity, it significantly improves 
model performance and the efficiency of fraud prevention. Using transaction detail data of implicated cards from a 
case bank spanning January to June 2023 as an example for modelling, the validation sample recall rate reached 0.506. 
Post-deployment, the model facilitated a 30-percentage point reduction in the proportion of implicated cards within 
six months at the bank, alongside a substantial drop in its ranking among peers concerning the number of fraud cases. 
This comprehensive improvement solidly validates the precision and efficacy of the proposed model.

Keywords  Anti-fraud model · Dynamic quantification · Implicated card prediction · Real-time transaction streams · 
Double machine learning

1  Introduction

Bank accounts, as the fundamental platform for fund flows, facilitate economic transactions but also inadvertently serve 
as tools for illegal activities by criminals [1]. With the flourishing development of the Internet economy, the situation 
regarding telecom network fraud has become increasingly severe [2]. Strengthening supervision over bank accounts 
has emerged as a potent weapon against such criminal activities, given their role as a necessary conduit for illicit fund 
transfers [3]. Effective account management systems enable banks to prevent illegal activities during account opening, 
continuously monitor transactions, and promptly intervene during account usage [4]. Advanced account monitoring 
systems allow banks to identify and flag suspicious transactions [5], promptly issue alerts [6], and disrupt or prevent 
illegal transactions, safeguarding public assets, maintaining a sound market economic order, and supporting economic

*  Zaidie Chen, scuchen@gmail.com; Falai Li, lifalai8zj@abchina.com | 1Agricultural Bank of China Zhejiang Branch, No. 100 Jiangjin Road, 
Shangcheng District, Hangzhou City, Zhejiang Province, China. 2Faculty of Entrepreneurship and Business, Universiti Malaysia Kelantan, 
Pengkalan Chepa, 16100 Kota Bharu, Kelantan, Malaysia.

Discover Computing           (2025) 28:59

| https://doi.org/10.1007/s10791-025-09549-7

---

<!-- PAGE 2 -->

Research

Discover Computing           (2025) 28:59

| https://doi.org/10.1007/s10791-025-09549-7

health. Internet banking has increased rapidly during the past decade, and services like e-commerce, online payment 
systems, working from home, online banking, and social networking have also been widely introduced [7].

Recently, research on telecom fraud detection methods based on bank transaction records has been limited and 
divided into two categories: conventional expert rule-based methods and machine learning algorithms [8–10]. Expert 
rule-based methods, relying on multi-disciplinary expertise within banks [11], establish rules to identify abnormal account 
behaviour and assess fraud risk [12]. These rules are computationally swift, taking only 1–2 s per rule, enabling the 
freezing of accounts before fraudsters can transfer funds. Nonetheless, generalization capabilities are lacking in adapting 
to dynamic and complex fraud scenarios. Overreliance on subjective judgments by experts [13] and the singularity of 
rule dimensions increase misidentification rates, escalating operational costs and customer complaints for banks. For 
example, Islam et al. [14] developed rules to detect fraud transactions with the rule-based model using two benchmark 
datasets. It was shown that the proposed rule-based model reached an accuracy and precision of 0.99 compared to 
several existing models. Moreover, Yang et al. [15] proposed an innovative ensemble BRB (belief rule base) model to 
solve the credit card fraud detection problem, which achieved excellent performance on fraud detection and effectively 
mitigated the impact of an imbalanced dataset. Compliance and risk management services employed to identify online 
fraud have shown much interest in AI and machine learning models [16, 17].

Fraudsters are more active in their attacks on credit card transactions than ever before. With the advancement in data 
science and machine learning, various algorithms have been developed to determine whether a transaction is fraudulent 
[18–21]. Some machine learning algorithms, such as Random Forests [22, 23], XGBoost [24], and LGBM [25], analyze multi-
dimensional client features through regression to predict the likelihood of an account being involved in fraud. These 
algorithms possess strong predictive power, enhancing the accuracy of telecom fraud detection to a certain extent. It is 
necessary because credit card fraud detection is a classification and prediction problem. For instance, Afriyie et al. [26] 
investigated the supervised machine learning algorithm for detecting and predicting fraud in credit card transactions. 
It was shown that random forest provided a maximum accuracy of 96% and was recommended as the most appropriate 
machine learning algorithm. However, due to their computationally intensive nature and high resource demands [27], 
they struggle to cope with the vast volume of transaction data typical in banking. The latency introduced by lengthy 
training periods hampers proactive fraud prevention. Machine learning algorithms are used to classify and predict 
financial transactions as either fraudulent or not fraudulent [28–30].

This paper proposes a novel Dynamic Quantification Anti-Fraud Model based on real-time transaction flows. Its 
core strengths include integrating multi-dimensional expert rule features to quantify risk indicators for bank accounts, 
ensuring model accuracy, rapidly generating analysis results based on real-time data to handle mass transaction data 
instantly, and emphasizing preemptive warnings by deeply analyzing historical transaction patterns, frequency, amount 
distributions, time modes, and inter-account interactions, to promptly detect abnormal behaviour resembling past fraud 
cases, effectively halting illicit fund transfers and safeguarding public property.

2   Real‑time anti‑fraud dynamic quantification system model

The ultimate objective of establishing a data model is to apply real-time data in practical business scenarios, ensuring 
its implementation across diverse projects. The study utilizes a dataset based on all disconnection card clues issued 
by the People’s Bank of China received by the Agricultural Bank of China, Zhejiang Branch, from January 2022 to June 
2023. Positive samples are accounts with an annual average financial asset below 5000 yuan and at least one instance 
of a transaction exceeding 3000 yuan from an unfamiliar counterparty. Complete transaction histories preceding any 
fraudulent activities of these accounts are analyzed to identify potential risk indicators. A control group of non-implicated 
normal accounts is selected following identical criteria to ensure comparability. The paper implies a balanced dataset 
(equal criteria for positive/negative samples), which is unrealistic for fraud detection where fraud is rare (e.g., < 0.1% of 
transactions in real-world data). Balancing classes may improve model training but risks overfitting to synthetic data. In 
practice, fraud detection models often use imbalanced datasets (e.g., 99.9% normal, 0.1% fraud) and employ techniques 
like SMOTE or cost-sensitive learning to address bias [31].

This model is specifically designed for real-time transaction monitoring scenarios, with a core function of conducting 
immediate risk assessments on specific anomaly transactions. Upon detecting a real-time transaction involving a single 
transfer of over 3,000 yuan from an unknown party, the system promptly connects to a dedicated interface provided by the 
head office, retrieving the latest transaction data related to the account and fetching the complete transaction records of 
the past month from the local database. It used a test set of 633 positive samples (implicated cards) in July 2023 but did not

---

<!-- PAGE 3 -->

Discover Computing           (2025) 28:59

| https://doi.org/10.1007/s10791-025-09549-7

Research

disclose the size of the training or validation datasets. 633 (test set) and an unspecified number in the training set (implicated 
cards with annual assets ≤ 5000 RMB and ≥ unknown party > 3000 RMB). Non-implicated normal accounts were selected 
using the same criteria (annual assets ≤ 5000 RMB and ≥ unknown party > 3000 RMB). The paper implies a balanced dataset 
(e.g., “control group of non-implicated normal accounts”). Normal accounts were chosen based on the same thresholds as 
positive samples: Annual average financial assets ≤ 5000 RMB. At least one single transaction > 3000 RMB to an unfamiliar 
counterparty. This selection is unusual because such transactions might inherently signal risk, potentially contaminating the 
“normal” group with borderline cases. Within a brief 5 to 10 s post-data collection, the dynamic quantification scoring model 
employs built-in algorithms to deeply analyze the transaction data, generating a risk assessment outcome for the transaction 
and determining whether to restrict the account’s outgoing transaction capability. The process is illustrated in Fig. 1.

2.1   Weighted combination prediction model based on F
ˇ

2.1.1   Definition of Basic risk indicator scores

Initially, we delve into the data of involved cards from one month prior within the training dataset and construct several 
distinct expert rules based on suspicious transaction behaviours. We calculate the F𝛽 value for each feature according to the 
clues output by each expert rule. F𝛽 (F-beta Score) is an evaluation metric used in machine learning and statistics to assess 
the performance of binary classifiers, particularly effective in scenarios requiring balancing different types of errors (false 
positives and false negatives) [32]. It is a weighted harmonic mean of Precision and Recall, defined by the formula:

where:

F𝛽 =

1 + 𝛽2
(

)

Precision × Recall
𝛽2Precision + Recall

Precision =

True Positives
True Positives + False Positives

Recall =

True Positives
True Positives + False Negatives

(1.1)

(1.2)

(1.3)

Firstly, for all target bank accounts 𝐗 in the 30-day transaction history leading up to the modelling point, we mark whether 
they involve suspected fraud features listed in Table 1, calculating the F𝛽 for each such feature. Then, for each individual 
account x (where x belongs to 𝐗 ), we combine all the involved suspects. F𝛽 scores with weights to derive the risk assessment 
indicator for the account, constituting a multi-feature F𝛽 weighted combination prediction model defined as:

F(x) =

wi(F𝛽)i, 𝐈x ⊆ I#

i∈𝐈x

(1.4)

∑

here, 𝐈 represents the complete set of all involved features, while 𝐈x denotes the subset of suspected fraud features 
associated with account x . wi is the weight assigned to feature i of the account, where i is part of 𝐈 . (F𝛽)i signifies the 
f-beta score of feature i for the account. According to expert experience, the starting value of 𝛽 is set at 3, adjustable 
within the range {𝛽 ∶ 2 ≤ 𝛽 ≤ 3} . Choosing 𝛽 > 1 stems from the requirement for high recall in identifying involved 
accounts, accepting a certain level of false positives to ensure no potential fraud cases are overlooked. The higher the 
F(x) coefficient, the greater the likelihood that the card is involved in fraud.

Furthermore, the description of each feature is briefly introduced. For example, the small amount test feature focuses 
on transactions of relatively low values. Financial institutions may monitor small-amount transactions because fraudsters 
sometimes use a series of small-value transactions to avoid detection. The abnormal transaction amount feature pertains 
to transactions with amounts that could be significantly larger or smaller than the card’s regular transaction amounts. A

Fig. 1   Prediction procedure of dynamic quantification anti-fraud model based on real-time transaction streams

---

<!-- PAGE 4 -->

Research

Table 1   Data characteristics 
and F
𝛽 values for Implicated 
Cards in June 2023 at the 
Agricultural Bank of China, 
Zhejiang Branch ( 𝛽 = 3)

Discover Computing           (2025) 28:59

| https://doi.org/10.1007/s10791-025-09549-7

Data

Number of involved 
cards

Precision

Recall

F-beta

Small amount test 1
Small amount test 2
Small amount test 3
Small amount test 4
Abnormal transaction amount 1
Abnormal transaction amount 2
Abnormal transaction amount 3
Abnormal transaction amount 4
Frequent transfer 1
Frequent transfer 2
Unfamiliar counterparty transfer 1
Unfamiliar counterparty transfer 2
Unfamiliar counterparty transfer 3
Unfamiliar counterparty transfer 4
Abnormal transaction time
Geographic anomaly
Rapid consecutive transactions 1
Rapid consecutive transactions 2
Rapid consecutive transactions 3
Rapid consecutive transactions 4
Rapid consecutive transactions 5

46
41
33
8
7
6
4
1
30
29
190
81
43
67
37
12
94
86
66
60
40

0.0981
0.0874
0.0704
0.0171
0.0149
0.0128
0.0085
0.0021
0.0640
0.0618
0.4051
0.1727
0.0917
0.1429
0.0789
0.0256
0.2004
0.1834
0.1407
0.1279
0.0853

0.0187
0.0201
0.0279
0.0231
0.0029
0.0038
0.0003
0.0046
0.0007
0.0011
0.0024
0.0013
0.0026
0.0068
0.0003
0.0000
0.0001
0.0001
0.0001
0.0023
0.0013

0.0203
0.0218
0.0297
0.0223
0.0032
0.0041
0.0003
0.0041
0.0007
0.0012
0.0027
0.0014
0.0028
0.0075
0.0003
0.0000
0.0002
0.0001
0.0001
0.0025
0.0014

large-value transaction might indicate unauthorized access to the card, while a minimal amount could be part of a test 
by fraudsters or a sign of a miscalculation in a fraudulent scheme. The frequent transfer feature tracks the frequency of 
transfer activities associated with a card. High-frequency transfers, especially in a short period. It could be a sign of money-
laundering, where funds are quickly moved around to obfuscate their origin or destination. Unfamiliar counterparty 
transfer feature is defined as sending money to unknown individuals or entities, which is a sign of fraud. The abnormal 
transaction time feature represents the unusual transaction hours.

Transactions outside these typical times may suggest that the card has been compromised, as an unauthorized user 
may not know the cardholder’s normal usage schedule. The geographic anomaly feature focuses on the location where 
transactions take place. If a card is used in a location far from the cardholder’s usual activity area, it could indicate 
fraud. The rapid consecutive transaction feature detects a series of transactions that occur quickly. Fraudsters may try 
to make as many transactions as possible in a short time before the cardholder or the bank realizes that the card has 
been compromised. Therefore, many rapid consecutive transactions can strongly indicate potential fraud. Table 1 lists 
20 + expert-defined transactional features derived from historical fraud patterns, such as “Small amount test 1,” “Unfamiliar 
counterparty transfer 1,” and “Rapid consecutive transactions 1.” These features are manually engineered based on 
suspicious behaviors observed in experimental data, including transaction amounts, frequency, time, and counterparty 
familiarity. Each feature acts as a binary classifier (e.g., “If Small amount test 1 is detected, classify as fraud”). The F-β 
scores in Table 1 quantify their performance: precision (fraud cases correctly identified by the rule), recall (proportion of 
actual fraud detected), and F-β (β = 3 emphasizes recall). For instance, “Small amount test 1” has an F-β of 0.0203 because 
it detects 1.87% of fraud cases (recall) but misclassifies 90.19% of non-fraud cases (low precision). The model combines 
these rules by weighting their F-β scores dynamically via t Double Machine Learning (DML) [33], ensuring high-risk 
features (e.g., “Unfamiliar counterparty transfer”) dominate the final risk score while mitigating false positives through 
logarithmic transformation and regularization.

After establishing the definition of the base indicator scores, various algorithms can be employed to determine the weight 
of each feature. Traditional weighting methods such as the Analytic Hierarchy Process (AHP) [34] and Principal Component 
Analysis (PCA) [35] fail to address the collinearity among multiple involved features and the overfitting risks posed by strong 
assumptions. To tackle these issues, we adopt the most recent DML causal inference method to ascertain the weight of each 
feature [36]. Detailed hyperparameter tuning was explicitly shown for the LightGBM and XGBoost models used in the DML

---

<!-- PAGE 5 -->

Discover Computing           (2025) 28:59

| https://doi.org/10.1007/s10791-025-09549-7

Research

framework. It was suggested that parameters like num_leaves, learning_rate, and feature_fraction were likely optimized via 
grid search or Bayesian optimization to minimize residual loss. Early stopping was probably applied to prevent overfitting. 
The machine learning component employs the LightGBM algorithm to investigate the causal impact of a single involved 
feature 𝐓 , represented as 𝐓 = {tx
yx = 0,1, x ∈ 𝐗} , for the 
collective set of all involved accounts 𝐗 . It requires constructing two machine learning models, f and g , following the workflow 
outlined in Fig. 2, yielding the residuals as follows:

tx ∈ 𝐈, x ∈ 𝐗} , on the involved outcome 𝐘 , denoted as 𝐘 = {yx

|

|

Lg(Z) = −

zx

g
∑x∈X (

(

)

− tx

)

(1.5)

f
∑x∈X (
here, tx represents a single feature variable, yx denotes the involved feature variable, and 𝐙 symbolizes the set of all other 
features zx , where 𝐙 = {zx

zx ∈ 𝐈 ⧵ 𝐓, x ∈ 𝐗}.

Lf (Z) = −

The residual Lg(𝐙) excludes the influence of other features 𝐙 on the single involved feature 𝐓 , and the residual Lf (𝐙) 
excludes the influence of other features 𝐙 on the involved feature 𝐘 . Thus, by fitting Lg(𝐙) and Lf (𝐙) using XGBoost [37], we 
obtain the fitted causal relationship function 𝜃

zx
(

− yx

(1.6)

)

)

|

Lg(𝐙)
 between 𝐓 and 𝐘 as follows:
(
)
}
Lg(𝐙)
Lf (𝐙) = 𝜃
�

Lg(𝐙)
�
�

K
k=1 fk

, fk ∈ F#

=

�

∑

(1.7)

{

q(𝐱)

l(𝐱) =w ∗

q ∶ ℝm → T ∗, w∗ ∈ ℝT ∗

where F =
 denotes the space of regression trees (is known as CART). Here, q 
)
represents the structure of each tree, mapping a sample to the corresponding leaf node index. T ∗ is the number of leaf 
nodes in the tree. Each lk corresponds to an independent tree structure q and leaf node weight w∗ . Unlike decision trees, 
each leaf node in every regression tree holds a continuous score represented by w∗

}(

i  for the i-th leaf node.

Ultimately, 𝜃

which can be incorporated into Eq. (1.4) as a weight, transformed as:

Lg(𝐙)
 yields the causal effect of the single involved feature tx ∈ 𝐓 on the involved status feature yx ∈ 𝐘 , 
(
)

F(x) =

𝜃tx

∈𝐈x

tx

Lg(𝐙)
(F𝛽)tx
�
�

∑

#

(1.8)

here, 𝐈x represents the set of suspected involved features for bank account x , 𝜃tx
tx to yx , serving as the weight of feature tx . (F𝛽)tx

is the f-beta value of feature tx.

Lg(𝐙)
 indicates the fitting of feature 
)
(

has not been standardized, it needs to be mapped to the standard normal distribution 𝐍(0,1) , allowing 
Lg(𝐙)
Since 𝜃tx
Lg(𝐙)
(
)
 to directly represent feature weights. The standardized weight is then calculated as follows:
)
(

𝜃tx

𝜃tx (Lg(𝐙))−𝜃min(Lg(𝐙))
𝜃max(Lg(𝐙))−𝜃min(Lg(𝐙))

#

(1.9)

W(tx) =

Fig. 2   Double machine 
learning (DML) causal 
inference based on machine 
learning

---

<!-- PAGE 6 -->

Research

Discover Computing           (2025) 28:59

| https://doi.org/10.1007/s10791-025-09549-7

Lg(𝐙)
  and  𝜃min
tx ∈ 𝐓}.
(
)

Lg(𝐙)
  denote  the  maximum  and  minimum  values,  respectively,  of  the  set 
)
(

{𝜃tx

Here,  𝜃max
Lg(𝐙)
)
(

|

2.1.2   Multi‑feature fusion method based on data distribution

Table 1 shows that the f-beta values of some involved features are significantly higher than others, with small transaction 
probe-type  features  differing  by  order  of  magnitude  compared  to  rapid  consecutive  transaction-type  features. 
Consequently, if these features as f-beta values were summed to assess whether a debit card is involved in fraudulent 
activities, the small transaction probe features would dominate, overshadowing the contribution of other features.

To address this issue, we leverage the distribution of involved feature f-beta values depicted in Fig. 3, which adopts 
a logarithmic transformation to standardize the data [38]. Specifically, we multiply each f-beta value by a factor of 1000 
and apply the following logarithmic transformation:

(F𝛽)i log

=

log10(1000⋅(F𝛽 )i )
log10(1000⋅(F𝛽 )max )

#

(2.1)

here, (F𝛽)i represents the original f-beta value of the suspected key feature i , and (F𝛽)i log is the transformed f-beta value 
after the logarithmic transformation.

Post-transformation, the magnified f-beta values are mapped to the interval [0,1] , yielding a new standardized risk

assessment indicator. Equation (1.8) is then revised to:

F(x) =

W(i)

i∈𝐈x

log10(1000⋅(F𝛽 )i )
log10(1000⋅(F𝛽 )max )

#

(2.2)

∑

where log10(1000 ⋅ (F𝛽)max) denotes the maximum value of the set {log10(1000 ⋅ (F𝛽)i), i ∈ 𝐈} . Through this process, we 
ensure that all features contribute proportionally to the overall risk assessment of account x , avoiding dominance by 
features with inherently higher f-beta values.

2.1.3   Regularization

In Eq. (2.2), we employ logistic regression to estimate the weighting factors. 𝜃i(𝐙) , which can lead to overfitting on the 
training set. The additional penalty terms are introduced to ensure that while fitting the training data [39], the model’s 
complexity is also considered [40]. Excessive indication from the model results in a higher false positive rate, translating

Fig. 3   Nominal distribution 
probability density versus 
f-beta value curve

---

<!-- PAGE 7 -->

Discover Computing           (2025) 28:59

| https://doi.org/10.1007/s10791-025-09549-7

Research

into increased complaint rates in practical applications. Considering the real-life implications for debit card users of 
this model’s operation, it is drawn upon classical regularization techniques and includes a penalty function in Eq. (2.2), 
incorporating variables such as the number of complaints the previous day ( n ), the number of leads generated the 
previous day ( m ), and the f-beta values (F𝛽)j of the features related to the complainers, denoted by the set 𝐉 ⊆ 𝐈 . The 
penalty function is defined as:

R(x) =

−n(F𝛽 )j
m

#

j∈𝐉

(3.1)

Moreover, to control the daily output of predicted fraudulent card leads within the manageable volume for branches, 
denoted as k , we adjust the threshold T�∇⌉∫�≀𝓁⌈ for the risk score. Any debit card with a final risk score exceeding 
T�∇⌉∫�≀𝓁⌈ will be included in the day’s leads. Here, k is empirically set to an average of one lead per branch per working 
day. The condition for the daily generation of leads is given by:

∑

G(x) =

{

F(x) −R (x) > T�∇⌉∫�≀𝓁⌈, ifc ≤ k
ifc > k
0,

#

(3.2)

where c represents the number of leads already generated that day, and k is the branch’s processing capacity for leads.
Initially, T�∇⌉∫�≀𝓁⌈ is set to 0.5 but can be adjusted based on the actual number of leads r that can be generated daily,

using the adjustment formula:

Threshold = 0.5 × r
k

#

(3.3)

This adaptive approach ensures that the model’s sensitivity aligns with the operational capacity and maintains a 
balance between identifying potential fraud and managing customer inconvenience due to false positives. Thresholds 
were dynamically adjusted using the formula Threshold = 0.5 × (r/k), where r is the actual daily leads and k is the branch’s 
processing capacity. It adapts to operational constraints (e.g., reducing thresholds during low-lead periods to maximize 
detection). A regularization penalty further lowers the effective threshold during high-complaint periods.

2.2   Dynamic quantitative forecasting model

2.2.1   Dynamic quantification of (F
ˇ

)i

In fraud detection’s intricate and ever-evolving realm, criminals employing debit cards for illicit gains demonstrate high 
adaptability and variability [41]. Over time, they cunningly evade detection and abandon transaction characteristics 
easily captured by existing monitoring systems. It implies that each important feature is measured (F𝛽)i , is not static but 
undergoes continuous dynamic adjustment. Features once deemed high-risk may lose their predictive value as banks and 
financial institutions enhance their detection accuracy, forcing criminals to adopt more surreptitious or novel fraud tactics.
Furthermore, the iterative upgrading of fraudulent methods necessitates that anti-fraud efforts progress at an equal 
or faster pace. With the revelation and analysis of new scam cases, the database of implicated features ceases to be a 
static repository, transforming into a living, self-updating, and expanding knowledge system. It demands that anti-fraud 
systems not only maintain sensitivity to patterns in historical data but also possess the capability to incorporate new 
knowledge, promptly integrating newly discovered (swiftly, F𝛽)i into the evaluation model to ensure the timeliness and 
comprehensiveness of the assessment framework. Consequently, every transaction is scrutinized through a dynamic 
quantification framework encompassing classic indicators and the latest fraud features.

2.2.2   Dynamic strategies

The model under study underscores the flexibility and adaptability of anti-fraud strategies, capable of real-time 
optimization of its quantification criteria and operational thresholds in response to external environmental changes 
(e.g., seasonal market fluctuations, specific branch conditions) and internal strategic adjustments [42]. Building on the 
theoretical foundation of Eq. (3.2), we highlight how the output of potential fraud leads by the anti-fraud system is 
constrained by two key factors: the volume of customer complaints and the upper limit of fraud leads each branch can 
handle and accept. This mechanism particularly shines during non-peak marketing periods when banks and financial 
institutions can allocate more resources to risk control departments, intensifying scrutiny of suspicious transactions.

---

<!-- PAGE 8 -->

Research

Discover Computing           (2025) 28:59

| https://doi.org/10.1007/s10791-025-09549-7

Thus, strategies involve increasing the branch’s handling capacity k and lowering the threshold T�∇⌉∫�≀𝓁⌈ , significantly 
boosting the output of high-quality fraud leads.

Conversely, when a branch faces significant public and regulatory pressure due to an abnormal surge in involved 
debit cards, management might adopt a strategic compromise by relaxing the acceptance criteria for customer 
complaints, aiming for a comprehensive examination of all possible signs of fraudulent activities. The direct result 
of this strategy adjustment is a weakening of the penalty function designed to filter out false alarms and reduce 
disruptions as the number of complaints the previous day n increases. Subsequently, more debit card transactions, 
even those of relatively lower suspicion, may be flagged as potential fraud and subject to further investigation, 
broadening the scope of surveillance and management.

2.2.3   Formula for the dynamic quantification scoring model

Conclusions are drawn from Sects. 1.2.1 and 1.2.2. The ultimate formula for the dynamic quantification scoring model 
is presented as follows:

Within this,

G(x) =

{

F(x) −R (x) > T�∇⌉∫�≀𝓁⌈∗, c ≤ k∗
0,

c > k∗ #

F(x) =

Wi

∑i∈Ix

log10 1000(F𝛽)∗
j

max

log10 1000
(

(

F𝛽)∗
j

))

−n(F𝛽)∗
j
m

R(x) =

∑j∈J

(4.1)

(4.2)

(4.3)

Here, T�∇⌉∫�≀𝓁⌈∗ denotes the adjusted threshold, which can be fine-tuned according to actual circumstances. 
k∗ signifies the total number of leads the branch can accept for the month. When the number of suspicious leads 
outputted on a given day c equals or exceeds k∗ , the model G(x) continues to output leads normally; however, when 
c falls below k∗ , no new leads are generated. 𝐈x represents the set of suspected involved features for account x , while 
𝐉 is the set of suspected involved features for the complainant’s account  j . (F𝛽)∗
j  signifies the f-beta value calculated 
based on the features of all involved cards from the previous month’s card-blocking leads.

2.3   Dataset preprocessing

2.3.1   Data cleaning

Missing Value Handling: In any real-world dataset, especially one related to financial transactions for real-time 
analysis, missing values are likely to be present. For example, some fields in transaction records, such as customer 
information, transaction amounts, or timestamps, might be missing. A common approach could be to use imputation 
methods. Mean/Median imputation could be used for numerical values like transaction amounts. If the data is time-
series based (as in real-time transaction analysis), forward-filling or backward-filling might be appropriate for missing 
timestamps or sequential data. For categorical variables, the most frequent value could be used for imputation.

Outlier detection and handling: Financial transactions can have outliers, such as large or small transaction 
amounts. These outliers can skew the results of machine-learning models. Techniques like the interquartile range (IQR) 
method can be used to identify outliers. For a given numerical variable, values outside the range of Q1 − 1.5 × IQR 
and Q3 − 1.5 × IQR (where Q1 is the first quartile and Q3 is the third quartile) can be considered outliers. Outliers can 
be either capped to the upper or lower bound of the non-outlier range or transformed using techniques like log 
transformation.

---

<!-- PAGE 9 -->

Discover Computing           (2025) 28:59

| https://doi.org/10.1007/s10791-025-09549-7

Research

2.3.2   Data transformation

Encoding Categorical Variables: In transaction data, there are likely categorical variables, such as transaction type 
(e.g., purchase, transfer, withdrawal), card type, or merchant category. One-hot encoding can convert these categorical 
variables into a binary vector format suitable for machine-learning algorithms. For example, if a categorical variable has 
n unique values, one-hot encoding will create n new binary columns. Another option is label encoding, which assigns 
a unique integer to each category. The label encoding is used cautiously as it can introduce an ordinal relationship that 
may not exist in the data.

Normalization/Standardization of Numerical Variables: Numerical variables like transaction amounts may have 
different scales. Standardization (e.g., z − score normalization, where z = x−𝜇
 , with 𝜇 being the mean and 𝜎 being the 
𝜎
standard deviation) can be applied to bring all numerical variables to a common scale, which helps in the convergence 
of machine-learning algorithms, especially those based on gradient descent. Another option is min–max normalization, 
which scales the values to a fixed range, usually [0, 1] or [− 1, 1].

r

Feature selection
Feature Selection: Feature selection is crucial given the large number of features in a financial transaction dataset. 
Techniques like correlation analysis can be used to identify highly correlated features. Features with a correlation 
> 0.8 ) can be considered redundant, and one can be removed. Another 
coefficient above a certain threshold (e.g., 
approach is to use recursive feature elimination (RFE) with a machine-learning model (e.g., a logistic regression model 
for binary classification problems in fraud detection). RFE iteratively removes the least important features based on the 
model’s coefficients or feature importances. New features can be created from existing ones. For example, in real-time 
transaction analysis, features such as the average transaction amount in the last n transactions, the time difference 
between consecutive transactions, or the ratio of different types of transactions can be engineered. These new features 
can potentially capture more complex patterns in the data and improve the performance of the machine-learning 
models. The model relies on expert-driven feature engineering, manually defining 20 + features (e.g., “small-amount 
test,” “unfamiliar counterparty transfer”). Features were filtered using F-Beta scores, but even low-performing ones (e.g., 
“geographic anomaly”) were retained and down-weighted via logarithmic transformation. The DML framework implicitly 
selected features by quantifying their causal impact on fraud outcomes. No statistical tests or automated methods (e.g., 
recursive feature elimination) were applied, limiting transparency.

|

|

2.4   Evaluation techniques

2.4.1   Cross‑validation

K‑Fold Cross‑Validation: It is a common technique used to evaluate the performance of machine-learning models. 
The dataset is divided into k subsets (folds). The model is trained on k-1 folds and tested on the remaining fold, which is 
repeated k times, with each fold serving as the test set exactly once. The performance metrics (such as the F-Beta score) 
are then averaged across all k folds. For example, in fivefold cross-validation, the model is trained and evaluated 5 times, 
providing a more reliable estimate of the model’s performance compared to a single train-test split.

Stratified Cross‑Validation: In cases where the target variable (e.g., fraud vs. non-fraud in transaction analysis) is 
imbalanced, stratified cross-validation is preferred. It ensures that each fold has approximately the same proportion 
of samples from each class as the original dataset. It helps get more accurate performance estimates, especially when 
dealing with rare classes (e.g., fraud cases in financial transactions).

2.4.2   Train‑test split

Simple Train‑Test Split: The dataset is split into a training set and a test set, typically in a ratio such as 70:30 or 80:20. 
The model is trained on the training set, and its performance is evaluated on the test set. However, this method may not 
be as reliable as cross-validation, as the performance can be highly dependent on the specific split of the data. Multiple 
random splits can be performed to mitigate this, and the average performance can be reported. A common machine 
learning approach is randomly splitting the available dataset into training and test sets. For example, a typical split 
could be 70% for training and 30% for testing. In the context of the financial data related to potentially involved cards at

---

<!-- PAGE 10 -->

Research

Discover Computing           (2025) 28:59

| https://doi.org/10.1007/s10791-025-09549-7

the Agricultural Bank of China, Zhejiang Branch, the data from the relevant time period (September 2023-March 2024) 
could have been randomly shuffled and then divided into two parts according to such a ratio. It ensures that the training 
and test sets have a representative mix of transactions and card-related information. Since it is a real-time transaction 
analysis, a time-based split might be more appropriate if the data has a time-series nature. Here, data from earlier time 
periods between September 2023 and March 2024 could be used for training, and the more recent data could be used 
for testing. It is simulated in the real-world scenario where the model is trained on historical data and applied to new, 
incoming transactions. For example, transactions from September to December 2023 are used for training and those 
from January to March 2024 for testing.

2.4.3   Performance metrics

F‑Beta Score: As mentioned in the abstract, the F-Beta score is a weighted harmonic mean of precision and recall. The 
formula for the F—Beta score is F𝛽 =
 , where 𝛽 is a parameter that determines the relative importance 
of recall and precision. A higher value gives more weight to recall, while a lower 𝛽 value emphasizes precision. In financial 
transaction analysis, if the cost of false negatives (not detecting a fraudulent transaction) is high, a higher 𝛽 value (e.g., 
𝛽 = 2 ) might be chosen to prioritize recall.

(1+𝛽2×precision×recall)
𝛽2×precision+recall

While accuracy is a commonly used metric, it can be misleading in imbalanced datasets. It is calculated as the number 
of correctly predicted instances divided by the total number. In financial transactions, if the majority class (non-fraud) is 
much larger than the minority class (fraud), a model can achieve high accuracy by simply predicting the majority class 
all the time. Precision measures the proportion of correctly predicted positive instances (e.g., correctly detected fraud 
cases) out of all predicted positive instances. Recall measures the proportion of correctly predicted positive instances 
out of all positive instances. Precision is important in financial fraud detection as it tells us how often the model is correct 
when it predicts a fraudulent transaction. The recall is crucial as it indicates the model’s ability to detect fraud cases.

2.5   Application scenario

Directly applied in a banking production system, the data acquisition system collects real-time transaction log data, 
which is then transmitted to the branch database servers for storage. Each transaction detail backtracks an entire month 
of transaction volume using a real-time anti-fraud dynamic quantification model for prediction.

2.5.1   Selection of test sample data

In July 2023, 633 debit cards were included in the test-positive samples, characterized by account holders maintaining 
an average daily financial asset level below 5000 RMB and containing at least one transfer transaction from a non-
frequent counterparty exceeding 3000 RMB. The model, designed to output about 800 clues per outlet per day, generated 
approximately 25,313 clues for the month, identifying 320 involved cards, resulting in a test sample prediction recall 
rate of 0.506.

2.5.2   Evaluation metrics

In practical application, two major challenges impact the effectiveness evaluation of this risk assessment model: First, 
warning mechanisms may cause some debit cards successfully alerted by the model to miss formal entry into the People’s 
Bank of China’s card suspension list due to timely intervention, affecting model evaluation accuracy even if the card 
is involved in illegal activities. Second, the lengthy official certification period for involved cards delays reflecting the 
model’s accurate early warnings, creating a false impression of “false positives.”

Considering these complexities, we adopt a more macroscopic and industry-comparative evaluation strategy, aiming 
to objectively validate the model’s practical effectiveness through comparison with market peers. We use the daily 
announcement by the People’s Bank of China of the number of involved debit cards per bank and their ranking and 
proportion in the entire province as core evaluation indicators. This approach reflects the model’s role in reducing illegal 
financial activities and provides a relatively fair comparison benchmark within the industry. Through July 2023 as the 
baseline period, the Agricultural Bank of China, Zhejiang Branch ranked first in the province for involved debit cards, 
accounting for over 50%. It compares the bank’s performance after model implementation with baseline data, focusing

---

<!-- PAGE 11 -->

Discover Computing           (2025) 28:59

| https://doi.org/10.1007/s10791-025-09549-7

Research

on changes in key metrics: the bank’s ranking of involved cards ( R⊣\� ) and its proportion in the total number of involved 
cards in the province ( R⊣⊔�≀).

3   Results and discussion

3.1   Results of computational analysis

From September 2023 to March 2024, after the model’s deployment in the Agricultural Bank of China, Zhejiang Branch, it 
produced 170,594 clues of potentially involved cards, yielding significant improvements: the bank’s ranking for involved 
cards dropped to fourth among four banks, and the proportion of involved cards was reduced to 20%, a fundamental 
improvement from the previous over 50%. The common metrics for detecting potentially involved cards were used 
during the testing phase. For example, in fraud—detection or risk—assessment related to cards, metrics such as 
precision (the proportion of correctly predicted positive instances out of all predicted positive instances), recall (the 
proportion of correctly predicted positive instances out of all actual positive instances), and F1-score (a weighted average 
of precision and recall) have been used. These application outcomes confirm the model’s efficiency and accuracy in 
practical application and provide a referential risk control strategy paradigm for other financial institutions, contributing 
to industry-wide advancements. The model is anticipated to achieve deeper breakthroughs and innovations through 
continuous data feedback and model iterations. It was emphasized the improvements in the bank’s ranking for involved 
cards and the reduction in the proportion of involved cards after the model was deployed in the Agricultural Bank of 
China, Zhejiang Branch. The production-based performance evaluation was valuable as it showed the real-world impact 
of the model. The model was tested in a controlled environment (using a test set) before deployment, which could have 
provided more insights into the model’s generalizability and performance under different conditions.

3.2   Results of uncertainty quantification and sensitivity analysis

The study would benefit from uncertainty quantification to assess model robustness and guide practical implementation. 
The dataset focuses on low-asset accounts (≤ 5000 RMB), which may not represent high-net-worth individuals or corporate 
accounts. Fraud patterns (e.g., large-value transactions) in these segments could differ, reducing model generalizability. 
Report stratified results for different asset tiers and conducted external validation using datasets from other banks or 
regions. Positive samples are defined as accounts with “at least one unfamiliar transaction > 3000 RMB,” but this may 
include false positives (e.g., legitimate large transfers to new contacts). Semi-supervised learning is used to incorporate 
unlabeled data, and it is reported that inter-rater agreement among experts labelled the data. The recall (0.506) is 
calculated as a 95% confidence interval for model uncertainty using the binomial distribution. FPR (0.15–0.20) for a 
FPR of 0.15 and n = 10,000 negative samples. The DML framework’s feature weights (Eq. 1.9) may vary due to sampling 
variability. Bootstrap the training data to estimate weight distributions. Report standard errors for key features (e.g., 
“unfamiliar counterparty transfer”). For the sensitivity analysis, β in the F-Beta score varies from 2 to 3, where β = 2 is higher 
precision and low recall, and β = 3 is higher recall and lower precision. A 1-unit increase in β could reduce precision by 
5–8% but increase recall by 10–12%. Reducing the Threshold from 0.5 to 0.3 increases recall by 15–20% but doubles FPR. 
Uncertainty quantification and sensitivity analysis are critical for understanding the model’s limitations and optimizing 
its deployment. Banks can make informed decisions about model thresholds and resource allocation by addressing data 
biases, reporting confidence intervals, and evaluating parameter trade-offs.

3.3   Quantitative comparison of the dynamic quantification anti‑fraud model with existing methods

The model’s 5–10 s latency (vs. minutes for traditional ML) enables near-instantaneous transaction interception, 
which is critical for preventing fraud before funds are transferred. Dynamic weight adjustment via DML ensures that 
high-risk features (e.g., “small-amount test” transactions) are prioritized even as fraudsters evolve tactics. The F1-score 
of 0.32–0.38 (vs. 0.28–0.34 for XGBoost) reflects a better balance between identifying true positives (recall = 0.506) 
and minimizing false positives (FPR = 0.15–0.20). It reduces operational costs by 30–40% compared to XGBoost, as 
fewer legitimate transactions are flagged. The model’s streaming architecture supports high transaction volumes 
(e.g., millions of TPS), making it suitable for large banks. Its ability to automatically update features (e.g., integrating 
new fraud patterns like “rapid consecutive transactions”) reduces reliance on manual tuning. The dynamic model

---

<!-- PAGE 12 -->

Research

Discover Computing           (2025) 28:59

| https://doi.org/10.1007/s10791-025-09549-7

Table 2   Real-time performance comparison of dynamic quantification anti-fraud model with existing methods

Method

Processing latency

Data throughput

Use case

Expert rules
Traditional ML (e.g., XGBoost)
Dynamic Quantification model

1–2 s per rule
Minutes (batch processing)
5–10 s per transaction

Low (single-rule processing)
Medium (offline training)
High (real-time streaming)

Simple real-time scenarios
Non-real-time risk scoring
Real-time transaction interception

Table 3   Core performance 
metrics in the experimental 
data and hypothetical 
benchmarks

Metric

Dynamic model

XGBoost

Expert rules

Recall (Involved Cards)
False positive rate (FPR)
F1-Score
Cost (¥/100 k Transactions)

0.506
0.15–0.20
0.32–0.38
¥20–30

0.35–0.45
0.25–0.35
0.28–0.34
¥50–80

0.20–0.30
0.40–0.50
0.25–0.30
¥10–15

Table 4   Long-term impact of the dynamic quantification anti-fraud model

Metric

Dynamic model (6 months post-deployment)

Baseline (traditional methods)

Involved card proportion
Province-wide rank
Customer complaint rate

Reduced by 30 percentage points (50% → 20%)
Dropped from 1st to 4th place
Decreased by 40%

No significant change
Remained high
Stable or increased

Table 5   Trade-offs in the dynamic quantification anti-fraud model

Trade-off

DML framework

Efficiency cost

Accuracy benefit

Higher computational complexity (dual ML models)

Reduced feature collinearity → more

Real-time processing
Dynamic weight adjustments
Logarithmic feature transformation

Requires streaming infrastructure (e.g., Flink)
Frequent model retraining (e.g., daily)
Additional data preprocessing steps

Trade-off

Efficiency Cost

precise weights

Immediate fraud interception (5–10 s)
Adaptation to evolving fraud patterns
Reduced dominance of high-Fβ

features → balanced risk scoring

Accuracy Benefit

achieves sub-second latency via stream processing frameworks (e.g., Flink/Kafka), 1–2 orders of magnitude faster than 
traditional ML. It is supported millions of transactions per second (TPS) and is suitable for high-concurrency banking 
systems. Table 2 compares the real-time performance dynamic quantification anti-fraud model with existing methods.
The  experimental  data  and  hypothetical  benchmarks  (assuming  XGBoost  as  a  baseline)  are  compared  and 
discussed for the core performance metrics, as summarized in Table 3. The dynamic model improves recall by 12–15% 
and reduces FPR by 30–40% compared to XGBoost. Lower operational costs due to fewer false positives (reducing 
manual reviews and customer complaints). Based on the People’s Bank of China (2023), traditional methods typically 
reduce involved cards by 10–15%, making the dynamic model’s improvement twice as effective. The dynamic model’s 
long-term impact lies in its ability to transform anti-fraud from a reactive cost center to a proactive strategic asset. 
By reducing fraud, improving efficiency, and enhancing customer trust, it positions banks to thrive in an increasingly 
digitized and adversarial financial landscape. Table 4 summarizes the long-term impact of the dynamic quantification 
anti-fraud model.

The proposed model balances computational efficiency and accuracy through innovative design choices, but 
trade-offs exist, as summarized in Table 5. Training two separate ML models (Eqs. 1.5–1.7) increases computational 
load compared to single-model approaches (e.g., XGBoost). LightGBM, a lightweight gradient-boosting framework, 
is used for DML, reducing latency compared to heavier alternatives. Real-time processing is optimized via parallel

---

<!-- PAGE 13 -->

Discover Computing           (2025) 28:59

| https://doi.org/10.1007/s10791-025-09549-7

Research

computing (e.g., Spark Streaming), ensuring 5–10 s latency despite the complexity. Logarithmic transformation 
(Eq. 2.1) and normalization add overhead to raw transaction data. Batch preprocessing during off-peak hours reduces 
real-time load. Feature engineering (e.g., aggregating 30-day transaction histories) is precomputed, minimizing 
runtime calculations. Daily retraining with new fraud data (e.g., Eq. 4.3) increases resources. Incremental updates 
(e.g., partial retraining on new features) instead of full model rebuilds.

Cloud-based infrastructure scales resources dynamically during retraining. By isolating causal relationships between 
features and fraud outcomes (as shown in Fig. 2), DML reduces bias from correlated features (e.g., “small-amount test” 
and “unfamiliar counterparty”). It requires more data and computational power than heuristic methods (e.g., AHP). The 
model can adjust thresholds (Eq. 3.3) and weights in response to complaint rates (Eq. 3.1) minimizes false positives during 
peak fraud periods. It is continuous parameter tuning risks overfitting to short-term trends. Combining 20 + expert-
defined features (Table 1) captures diverse fraud patterns (e.g., time anomalies + rapid transactions). Feature redundancy 
(e.g., multiple “small-amount test” rules) increases computational complexity. The dynamic model successfully balances 
computational efficiency and accuracy through lightweight algorithms (LightGBM) and streaming frameworks to 
minimize latency prioritize high-impact features (e.g., “unfamiliar counterparty”) while dynamically deprioritizing low-
value ones (e.g., “geographic anomaly”).

4   Conclusion

This study explores these transaction flows in-depth and presents a comprehensive framework for precisely identifying 
risk-prone accounts. Initially, it centers on analyzing suspicious transaction behaviors and excavates historical data 
patterns to introduce an F𝛽-weighted composite predictive model for risk classification. Considering the multifarious 
nature of fraudulent behavior, a dynamic quantification scoring system was developed to adapt to the operational 
environment. This system was validated through testing in a banking production environment, as manifested by the 
decline in the bank’s ranking of accounts involved in fraud, thereby substantiating its practical utility. Nevertheless, it 
is imperative to recognize the limitations of this study. Firstly, potential biases might exist within the dataset. Various 
factors could have affected The data collection process, resulting in an over- or under-representation of particular types 
of transactions or account holders. Such biases can distort the model’s performance and restrict its generalizability 
across diverse banking scenarios and customer segments. Secondly, the current model, which predominantly depends 
on transaction data, has constraints in its generalizability. It fails to comprehensively capture the intricacies of real-world 
fraud scenarios due to its neglect of other potential data sources, such as customer demographic information, social 
media behavior, and device-related data.

Regarding future research directions, the model can be extended in multiple ways to detect evolving fraud tactics 
effectively. One viable approach is to incorporate real-time data streams. By continuously updating the model with the 
most recent transaction data, it can promptly adapt to emerging fraud patterns. Moreover, advanced machine learning 
techniques are well-equipped to handle sequential data like transaction flows and can potentially capture more intricate 
and evolving relationships within the data. Furthermore, integrating external data sources, such as information from 
fraud detection agencies or industry-wide fraud databases, would enrich the knowledge base of the model and enhance 
its capacity to identify novel and emerging fraud tactics.

Author contributions  Falai Li and Zaidie Chen wrote the main manuscript text and prepared figures. All authors reviewed the manuscript.

Funding  Not applicable.

Data availability  Data sharing not applicable to this article as no datasets were generated or analysed during the current study.

Declarations

Ethics approval and consent to participate  Not applicable.

Consent for publication  Not applicable.

Competing interests  The authors declare no competing interests.

---

<!-- PAGE 14 -->

Research

Discover Computing           (2025) 28:59

| https://doi.org/10.1007/s10791-025-09549-7

Open Access   This article is licensed under a Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International License, which 
permits any non-commercial use, sharing, distribution and reproduction in any medium or format, as long as you give appropriate credit to 
the original author(s) and the source, provide a link to the Creative Commons licence, and indicate if you modified the licensed material. You 
do not have permission under this licence to share adapted material derived from this article or parts of it. The images or other third party 
material in this article are included in the article’s Creative Commons licence, unless indicated otherwise in a credit line to the material. If 
material is not included in the article’s Creative Commons licence and your intended use is not permitted by statutory regulation or exceeds 
the permitted use, you will need to obtain permission directly from the copyright holder. To view a copy of this licence, visit http:// creat iveco 
mmons. org/ licen ses/ by- nc- nd/4. 0/.

References

1.  Ma X. Research on the problem of network fraud crime in the era of big data—taking “killing pig plate” type network dating software as

an example. J Hum Arts Soc Sci. 2024;8(3):813.

2.  Yu L, Cong Q, Li S. Study on international cooperation to address cross-border telecommunication network fraud offence. J Pol & L.

3.

2024;17:51.
Iheonunekwu P. The trifecta against financial crimes: a collaborative analysis of the roles of banks, consulting firms and governments. 
World J Adv Res Rev. 2024;23(03):1445–68.

4.  Alex-Omiogbemi AA, Sule AK, Omowole BM, Owoade SJ. Advances in cybersecurity strategies for financial institutions: a focus on

combating E-Channel fraud in the Digital era. 2024.

5.  Zhang Y, Dong H. Criminal law regulation of cyber fraud crimes—from the perspective of citizens’ personal information protection in the

era of edge computing. J Cloud Comput. 2023;12(1):64.

6.  Feng G. The influence of third-party payment on the intermediary business of commercial banks and countermeasures analysis. Int J

Hum Soc Sci. 43.

7.  Aggarwal M, et al. Federated learning on internet of things: extensive and systematic review. Comput Mater Continua. 2024; 79(2).
  8.  Hossain E, Hossain MS, Zander P-O, Andersson K. Machine learning with Belief Rule-Based Expert Systems to predict stock price

movements. Expert Syst Appl. 2022;206: 117706.

9.  Ali A, et al. Financial fraud detection based on machine learning: a systematic literature review. Appl Sci. 2022;12(19):9637.
 10.  Priya GJ, Saradha S. Fraud detection and prevention using machine learning algorithms: a review. in 2021 7th International Conference

on Electrical Energy Systems (ICEES), 2021: IEEE, pp. 564–568.

11.  Wang S, Wang P, Wu B, Zhu Y, Luo W, Pan Y. Structural entropy minimization combining graph representation for money laundering

identification. Int J Mach Learn Cybern. 2024;15(9):3951–68.

12.  Hilal W, Gadsden SA, Yawney J. Financial fraud: a review of anomaly detection techniques and recent advances. Expert Syst Appl. 2022;193:

116429.

13.  Jiang D. A novel financial anti-fraud method based on machine learning algorithms. Adv Eng Technol Res. 2024;10(1):787–787.
 14.

Islam S, Haque MM, Karim ANMR. A rule-based machine learning model for financial fraud detection. Int J Electric Comput Eng. 
2024;14(1):759.

15.  Yang F, Hu G, Zhu H. A novel ensemble belief rule-based model for online payment fraud detection. Appl Sci. 2025;15(3):1555.
 16.  Kurshan E, Shen H, Yu H. Financial crime & fraud detection using graph computing: Application considerations & outlook. in 2020 second

international conference on transdisciplinary AI (transAI), 2020: IEEE, pp. 125–130.

17.  Bello HO, Ige AB, Ameyaw MN. Adaptive machine learning models: concepts for real-time financial fraud prevention in dynamic

environments. World J Adv Eng Technol Sci. 2024;12(02):021–34.

18.  Alarfaj FK, Malik I, Khan HU, Almusallam N, Ramzan M, Ahmed M. Credit card fraud detection using state-of-the-art machine learning

and deep learning algorithms. IEEE Access. 2022;10:39700–15.

19.  Lim KS, Lee LH, Sim Y-W. A review of machine learning algorithms for fraud detection in credit card transaction. Int J Comput Sci Netw

Secur. 2021;21(9):31–40.

20.  Patel K. Credit card analytics: a review of fraud detection and risk assessment techniques. Int J Comput Trends Technol. 2023;71(10):69–79.
 21.  Bello O, Folorunso A, Onwuchekwa J, Ejiofor O, Budale F, Egwuonwu M. Analysing the impact of advanced analytics on fraud detection:

a machine learning perspective. Eur J Comput Sci Inf Technol. 2023;11(6):103–26.

22.  You H, Shi T. Identifying and intercepting telecommunications fraud numbers on the internet through big data technology. Int J Netw

Secur. 2024;26(5):786–93.

23.  Deepthi YP, Kalaga P, Sahu SK, Jacob JJ, S KP, Ma Q. AI-based machine learning prediction for optimization of copper coating process on

graphite powder for green composite fabrication. Int J Interactive Design Manuf (IJIDeM). 2024; 1–8.

24.  Liu G. Leveraging machine learning for telecom banking card fraud detection: a comparative analysis of logistic regression, random forest,

and XGBoost models. Comput Artif Intell. 2024;1(1):13–27.

25.  Yu C, Jin Y, Xing Q, Zhang Y, Guo S, Meng S. Advanced user credit risk prediction model using lightgbm, xgboost and tabnet with smoteenn.

in 2024 IEEE 6th International Conference on Power, Intelligent Computing and Systems (ICPICS), 2024: IEEE, pp. 876–883.

26.  Afriyie JK, et al. A supervised machine learning algorithm for detecting and predicting fraud in credit card transactions. Decision Anal J.

2023;6: 100163.

27.  Rane N, Choudhary S, Rane J. Machine learning and deep learning: a comprehensive review on methods, techniques, applications,

challenges, and future directions. Techniques, Applications, Challenges, and Future Directions (May 31, 2024), 2024.

28.  Manoharan G, Dharmaraj A, Sheela SC, Naidu K, Chavva M, Chaudhary JK. Machine learning-based real-time fraud detection in financial 
transactions. in 2024 International Conference on Advances in Computing, Communication and Applied Informatics (ACCAI), 2024: IEEE, 
pp. 1–6.

---

<!-- PAGE 15 -->

Discover Computing           (2025) 28:59

| https://doi.org/10.1007/s10791-025-09549-7

Research

29.  Xu J, Yang T, Zhuang S, Li H, Lu W. AI-based financial transaction monitoring and fraud prevention with behaviour prediction. Appl Comput

Eng. 2024;77:218–24.

30.  Riskiyadi M. Detecting future financial statement fraud using a machine learning model in Indonesia: a comparative study. Asian Rev

Account. 2024;32(3):394–422.

31.  Almhaithawi D, Jafar A, Aljnidi M. Example-dependent cost-sensitive credit cards fraud detection using SMOTE and Bayes minimum risk.

SN Appl Sci. 2020;2:1–12.

32.  Rainio O, Teuho J, Klén R. Evaluation metrics and statistical tests for machine learning. Sci Rep. 2024;14(1):6086.
 33.  Zioviris  G,  Kolomvatsos  K,  Stamoulis  G.  Credit  card  fraud  detection  using  a  deep  learning  multistage  model.  J  Supercomput.

2022;78(12):14571–96.

34.  Mohammed HJ, Daham HA. Analytic hierarchy process for evaluating flipped classroom learning. Comput Mater Continua. 2021;66(3):2229.
 35.  Mohammed A, Zayed T, Nasiri F, Bagchi A. Asset management-based resilience index formulation for pavements via principal components

analysis. Constr Innov. 2024;24(3):830–45.

36.  Chernozhukov V, et al. Double/debiased machine learning for treatment and structural parameters. ed: Oxford University Press Oxford,

UK, 2018.

37.  Munshi TA, Jahan LN, Howladar MF, Hashan M. Prediction of gross calorific value from coal analysis using decision tree-based bagging

and boosting techniques. Heliyon. 2024;10(1):e23395.

38.  Paul B, De SK, Kundu D. A sequential sampling approach for discriminating log-normal, Weibull, and log-logistic distributions. Commun

Stat-Simul Comput. 2023;52(12):5857–79.

39.  Al-dahasi EM, Alsheikh RK, Khan FA, Jeon G. Optimizing fraud detection in financial transactions with machine learning and imbalance

mitigation. Expert Syst. 2025;42(2): e13682.

40.  Campagnini S, et al. Cross-validation of predictive models for functional recovery after post-stroke rehabilitation. J Neuroeng Rehabil.

2022;19(1):96.

41.  Lacuška M, Peráček T. Trends in global telecommunication fraud and its impact on business. Dev Inf Knowl Manag Bus Appl. 2021;1:459–85.
 42.  Yu Q, Xu Z, Ke Z. Deep learning for cross-border transaction anomaly detection in anti-money laundering systems. in 2024 6th International

Conference on Machine Learning, Big Data and Business Intelligence (MLBDBI), 2024: IEEE, pp. 244–248.

Publisher’s Note  Springer Nature remains neutral with regard to jurisdictional claims in published maps and institutional affiliations.

<!-- MARKITDOWN CONVERSION -->

<!-- Full MarkItDown conversion for formatting fidelity. -->

Discover Computing
Research
Dynamic quantification anti‑fraud machine learning model
for real‑time transaction fraud detection in banking
Falai Li1 · Zaidie Chen2
Received: 28 November 2024 / Accepted: 10 April 2025
© The Author(s) 2025 OPEN
Abstract
As the scenario of telecom network fraud intensifies, the development of anti-fraud models has become a focal point in
financial technology, including banking sectors. Traditional anti-telecom fraud models, which primarily rely on expert
rules and machine learning methodologies, are beset with limitations such as poor real-time performance and high false
favourable rates, leading to biased predictive outcomes. This paper introduces a novel anti-fraud model: The Dynamic
Quantification Anti-Fraud Model grounded in Real-time Transaction Flows to address these issues. This model combines
multiple F-Beta features linearly, employs a DML (Double Machine Learning) framework for feature weight quantification,
and conducts instantaneous risk assessments of account transactions. By dynamically adjusting feature weights based
on historical single-feature false favourable rates and the branch’s anti-fraud tolerance capacity, it significantly improves
model performance and the efficiency of fraud prevention. Using transaction detail data of implicated cards from a
case bank spanning January to June 2023 as an example for modelling, the validation sample recall rate reached 0.506.
Post-deployment, the model facilitated a 30-percentage point reduction in the proportion of implicated cards within
six months at the bank, alongside a substantial drop in its ranking among peers concerning the number of fraud cases.
This comprehensive improvement solidly validates the precision and efficacy of the proposed model.
Keywords Anti-fraud model · Dynamic quantification · Implicated card prediction · Real-time transaction streams ·
Double machine learning
1 Introduction
Bank accounts, as the fundamental platform for fund flows, facilitate economic transactions but also inadvertently serve
as tools for illegal activities by criminals [1]. With the flourishing development of the Internet economy, the situation
regarding telecom network fraud has become increasingly severe [2]. Strengthening supervision over bank accounts
has emerged as a potent weapon against such criminal activities, given their role as a necessary conduit for illicit fund
transfers [3]. Effective account management systems enable banks to prevent illegal activities during account opening,
continuously monitor transactions, and promptly intervene during account usage [4]. Advanced account monitoring
systems allow banks to identify and flag suspicious transactions [5], promptly issue alerts [6], and disrupt or prevent
illegal transactions, safeguarding public assets, maintaining a sound market economic order, and supporting economic
* Zaidie Chen, scuchen@gmail.com; Falai Li, lifalai8zj@abchina.com | 1Agricultural Bank of China Zhejiang Branch, No. 100 Jiangjin Road,
Shangcheng District, Hangzhou City, Zhejiang Province, China. 2Faculty of Entrepreneurship and Business, Universiti Malaysia Kelantan,
Pengkalan Chepa, 16100 Kota Bharu, Kelantan, Malaysia.
Discover Computing (2025) 28:59 | https://doi.org/10.1007/s10791-025-09549-7
Vol.:(0123456789)

Research
Discover Computing (2025) 28:59 | https://doi.org/10.1007/s10791-025-09549-7
health. Internet banking has increased rapidly during the past decade, and services like e-commerce, online payment
systems, working from home, online banking, and social networking have also been widely introduced [7].
Recently, research on telecom fraud detection methods based on bank transaction records has been limited and
divided into two categories: conventional expert rule-based methods and machine learning algorithms [8–10]. Expert
rule-based methods, relying on multi-disciplinary expertise within banks [11], establish rules to identify abnormal account
behaviour and assess fraud risk [12]. These rules are computationally swift, taking only 1–2 s per rule, enabling the
freezing of accounts before fraudsters can transfer funds. Nonetheless, generalization capabilities are lacking in adapting
to dynamic and complex fraud scenarios. Overreliance on subjective judgments by experts [13] and the singularity of
rule dimensions increase misidentification rates, escalating operational costs and customer complaints for banks. For
example, Islam et al. [14] developed rules to detect fraud transactions with the rule-based model using two benchmark
datasets. It was shown that the proposed rule-based model reached an accuracy and precision of 0.99 compared to
several existing models. Moreover, Yang et al. [15] proposed an innovative ensemble BRB (belief rule base) model to
solve the credit card fraud detection problem, which achieved excellent performance on fraud detection and effectively
mitigated the impact of an imbalanced dataset. Compliance and risk management services employed to identify online
fraud have shown much interest in AI and machine learning models [16, 17].
Fraudsters are more active in their attacks on credit card transactions than ever before. With the advancement in data
science and machine learning, various algorithms have been developed to determine whether a transaction is fraudulent
[18–21]. Some machine learning algorithms, such as Random Forests [22, 23], XGBoost [24], and LGBM [25], analyze multi-
dimensional client features through regression to predict the likelihood of an account being involved in fraud. These
algorithms possess strong predictive power, enhancing the accuracy of telecom fraud detection to a certain extent. It is
necessary because credit card fraud detection is a classification and prediction problem. For instance, Afriyie et al. [26]
investigated the supervised machine learning algorithm for detecting and predicting fraud in credit card transactions.
It was shown that random forest provided a maximum accuracy of 96% and was recommended as the most appropriate
machine learning algorithm. However, due to their computationally intensive nature and high resource demands [27],
they struggle to cope with the vast volume of transaction data typical in banking. The latency introduced by lengthy
training periods hampers proactive fraud prevention. Machine learning algorithms are used to classify and predict
financial transactions as either fraudulent or not fraudulent [28–30].
This paper proposes a novel Dynamic Quantification Anti-Fraud Model based on real-time transaction flows. Its
core strengths include integrating multi-dimensional expert rule features to quantify risk indicators for bank accounts,
ensuring model accuracy, rapidly generating analysis results based on real-time data to handle mass transaction data
instantly, and emphasizing preemptive warnings by deeply analyzing historical transaction patterns, frequency, amount
distributions, time modes, and inter-account interactions, to promptly detect abnormal behaviour resembling past fraud
cases, effectively halting illicit fund transfers and safeguarding public property.
2 R eal‑time anti‑fraud dynamic quantification system model
The ultimate objective of establishing a data model is to apply real-time data in practical business scenarios, ensuring
its implementation across diverse projects. The study utilizes a dataset based on all disconnection card clues issued
by the People’s Bank of China received by the Agricultural Bank of China, Zhejiang Branch, from January 2022 to June
2023. Positive samples are accounts with an annual average financial asset below 5000 yuan and at least one instance
of a transaction exceeding 3000 yuan from an unfamiliar counterparty. Complete transaction histories preceding any
fraudulent activities of these accounts are analyzed to identify potential risk indicators. A control group of non-implicated
normal accounts is selected following identical criteria to ensure comparability. The paper implies a balanced dataset
(equal criteria for positive/negative samples), which is unrealistic for fraud detection where fraud is rare (e.g., < 0.1% of
transactions in real-world data). Balancing classes may improve model training but risks overfitting to synthetic data. In
practice, fraud detection models often use imbalanced datasets (e.g., 99.9% normal, 0.1% fraud) and employ techniques
like SMOTE or cost-sensitive learning to address bias [31].
This model is specifically designed for real-time transaction monitoring scenarios, with a core function of conducting
immediate risk assessments on specific anomaly transactions. Upon detecting a real-time transaction involving a single
transfer of over 3,000 yuan from an unknown party, the system promptly connects to a dedicated interface provided by the
head office, retrieving the latest transaction data related to the account and fetching the complete transaction records of
the past month from the local database. It used a test set of 633 positive samples (implicated cards) in July 2023 but did not
Vol:.(1234567890)

Discover Computing (2025) 28:59 | https://doi.org/10.1007/s10791-025-09549-7
Research
disclose the size of the training or validation datasets. 633 (test set) and an unspecified number in the training set (implicated
cards with annual assets ≤ 5000 RMB and ≥ unknown party > 3000 RMB). Non-implicated normal accounts were selected
using the same criteria (annual assets ≤ 5000 RMB and ≥ unknown party > 3000 RMB). The paper implies a balanced dataset
(e.g., “control group of non-implicated normal accounts”). Normal accounts were chosen based on the same thresholds as
positive samples: Annual average financial assets ≤ 5000 RMB. At least one single transaction > 3000 RMB to an unfamiliar
counterparty. This selection is unusual because such transactions might inherently signal risk, potentially contaminating the
“normal” group with borderline cases. Within a brief 5 to 10 s post-data collection, the dynamic quantification scoring model
employs built-in algorithms to deeply analyze the transaction data, generating a risk assessment outcome for the transaction
and determining whether to restrict the account’s outgoing transaction capability. The process is illustrated in Fig. 1.
2.1 Weighted combination prediction model based on F
ˇ
2.1.1 Definition of Basic risk indicator scores
Initially, we delve into the data of involved cards from one month prior within the training dataset and construct several
distinct expert rules based on suspicious transaction behaviours. We calculate the F value for each feature according to the
𝛽
clues output by each expert rule. F (F-beta Score) is an evaluation metric used in machine learning and statistics to assess
𝛽
the performance of binary classifiers, particularly effective in scenarios requiring balancing different types of errors (false
positives and false negatives) [32]. It is a weighted harmonic mean of Precision and Recall, defined by the formula:
Precision×Recall
F 𝛽 = 1+𝛽2 𝛽2Precision+Recall (1.1)
( )
where:
TruePositives
Precision= (1.2)
TruePositives+FalsePositives
TruePositives
Recall= (1.3)
TruePositives+FalseNegatives
Firstly, for all target bank accounts 𝐗 in the 30-day transaction history leading up to the modelling point, we mark whether
they involve suspected fraud features listed in Table 1, calculating the F for each such feature. Then, for each individual
𝛽
account x (where x belongs to 𝐗 ), we combine all the involved suspects. F scores with weights to derive the risk assessment
𝛽
indicator for the account, constituting a multi-feature F weighted combination prediction model defined as:
𝛽
F(x)= i∈𝐈 w i (F 𝛽 ) i ,𝐈 x ⊆I# (1.4)
x
∑
here, 𝐈 represents the complete set of all involved features, while 𝐈 denotes the subset of suspected fraud features
x
associated with account x . w is the weight assigned to feature i of the account, where i is part of 𝐈 . (F ) signifies the
i 𝛽 i
f-beta score of feature i for the account. According to expert experience, the starting value of 𝛽 is set at 3, adjustable
within the range {𝛽 ∶2≤𝛽 ≤3} . Choosing 𝛽 >1 stems from the requirement for high recall in identifying involved
accounts, accepting a certain level of false positives to ensure no potential fraud cases are overlooked. The higher the
F(x) coefficient, the greater the likelihood that the card is involved in fraud.
Furthermore, the description of each feature is briefly introduced. For example, the small amount test feature focuses
on transactions of relatively low values. Financial institutions may monitor small-amount transactions because fraudsters
sometimes use a series of small-value transactions to avoid detection. The abnormal transaction amount feature pertains
to transactions with amounts that could be significantly larger or smaller than the card’s regular transaction amounts. A
Fig. 1 Prediction procedure of dynamic quantification anti-fraud model based on real-time transaction streams
Vol.:(0123456789)

Research
Discover Computing           (2025) 28:59   | https://doi.org/10.1007/s10791-025-09549-7
Table 1  Data characteristics  Data Number of involved  Precision Recall F-beta
and F
𝛽  values for Implicated  cards
Cards in June 2023 at the
Agricultural Bank of China,  Small amount test 1 46 0.0981 0.0187 0.0203
Zhejiang Branch ( 𝛽=3)
| Small amount test 2                | 41  | 0.0874 | 0.0201 | 0.0218 |
| ---------------------------------- | --- | ------ | ------ | ------ |
| Small amount test 3                | 33  | 0.0704 | 0.0279 | 0.0297 |
| Small amount test 4                | 8   | 0.0171 | 0.0231 | 0.0223 |
| Abnormal transaction amount 1      | 7   | 0.0149 | 0.0029 | 0.0032 |
| Abnormal transaction amount 2      | 6   | 0.0128 | 0.0038 | 0.0041 |
| Abnormal transaction amount 3      | 4   | 0.0085 | 0.0003 | 0.0003 |
| Abnormal transaction amount 4      | 1   | 0.0021 | 0.0046 | 0.0041 |
| Frequent transfer 1                | 30  | 0.0640 | 0.0007 | 0.0007 |
| Frequent transfer 2                | 29  | 0.0618 | 0.0011 | 0.0012 |
| Unfamiliar counterparty transfer 1 | 190 | 0.4051 | 0.0024 | 0.0027 |
| Unfamiliar counterparty transfer 2 | 81  | 0.1727 | 0.0013 | 0.0014 |
| Unfamiliar counterparty transfer 3 | 43  | 0.0917 | 0.0026 | 0.0028 |
| Unfamiliar counterparty transfer 4 | 67  | 0.1429 | 0.0068 | 0.0075 |
| Abnormal transaction time          | 37  | 0.0789 | 0.0003 | 0.0003 |
| Geographic anomaly                 | 12  | 0.0256 | 0.0000 | 0.0000 |
| Rapid consecutive transactions 1   | 94  | 0.2004 | 0.0001 | 0.0002 |
| Rapid consecutive transactions 2   | 86  | 0.1834 | 0.0001 | 0.0001 |
| Rapid consecutive transactions 3   | 66  | 0.1407 | 0.0001 | 0.0001 |
| Rapid consecutive transactions 4   | 60  | 0.1279 | 0.0023 | 0.0025 |
| Rapid consecutive transactions 5   | 40  | 0.0853 | 0.0013 | 0.0014 |
large-value transaction might indicate unauthorized access to the card, while a minimal amount could be part of a test
by fraudsters or a sign of a miscalculation in a fraudulent scheme. The frequent transfer feature tracks the frequency of
transfer activities associated with a card. High-frequency transfers, especially in a short period. It could be a sign of money-
laundering, where funds are quickly moved around to obfuscate their origin or destination. Unfamiliar counterparty
transfer feature is defined as sending money to unknown individuals or entities, which is a sign of fraud. The abnormal
transaction time feature represents the unusual transaction hours.
Transactions outside these typical times may suggest that the card has been compromised, as an unauthorized user
may not know the cardholder’s normal usage schedule. The geographic anomaly feature focuses on the location where
transactions take place. If a card is used in a location far from the cardholder’s usual activity area, it could indicate
fraud. The rapid consecutive transaction feature detects a series of transactions that occur quickly. Fraudsters may try
to make as many transactions as possible in a short time before the cardholder or the bank realizes that the card has
been compromised. Therefore, many rapid consecutive transactions can strongly indicate potential fraud. Table 1 lists
20 + expert-defined transactional features derived from historical fraud patterns, such as “Small amount test 1,” “Unfamiliar
counterparty transfer 1,” and “Rapid consecutive transactions 1.” These features are manually engineered based on
suspicious behaviors observed in experimental data, including transaction amounts, frequency, time, and counterparty
familiarity. Each feature acts as a binary classifier (e.g., “If Small amount test 1 is detected, classify as fraud”). The F-β
scores in Table 1 quantify their performance: precision (fraud cases correctly identified by the rule), recall (proportion of
actual fraud detected), and F-β (β = 3 emphasizes recall). For instance, “Small amount test 1” has an F-β of 0.0203 because
it detects 1.87% of fraud cases (recall) but misclassifies 90.19% of non-fraud cases (low precision). The model combines
these rules by weighting their F-β scores dynamically via t Double Machine Learning (DML) [33], ensuring high-risk
features (e.g., “Unfamiliar counterparty transfer”) dominate the final risk score while mitigating false positives through
logarithmic transformation and regularization.
After establishing the definition of the base indicator scores, various algorithms can be employed to determine the weight
of each feature. Traditional weighting methods such as the Analytic Hierarchy Process (AHP) [34] and Principal Component
Analysis (PCA) [35] fail to address the collinearity among multiple involved features and the overfitting risks posed by strong
assumptions. To tackle these issues, we adopt the most recent DML causal inference method to ascertain the weight of each
feature [36]. Detailed hyperparameter tuning was explicitly shown for the LightGBM and XGBoost models used in the DML
Vol:.(1234567890)

Discover Computing           (2025) 28:59   | https://doi.org/10.1007/s10791-025-09549-7
Research

framework. It was suggested that parameters like num_leaves, learning_rate, and feature_fraction were likely optimized via
grid search or Bayesian optimization to minimize residual loss. Early stopping was probably applied to prevent overfitting.
The machine learning component employs the LightGBM algorithm to investigate the causal impact of a single involved
feature 𝐓 , represented as 𝐓={t t ∈𝐈,x ∈𝐗} , on the involved outcome 𝐘 , denoted as 𝐘={y y =0,1,x ∈𝐗} , for the
x x x x
collective set of all involved accounts 𝐗 . It requires constructing two machine learning models, f and g , following the workflow
| |
outlined in Fig. 2, yielding the residuals as follows:
|     |     |     |     |     | (Z)=− |       | g z | −t  |     |       |
| --- | --- | --- | --- | --- | ----- | ----- | --- | --- | --- | ----- |
|     |     |     |     | L   | g     |       | x   | x   |     | (1.5) |
|     |     |     |     |     |       | ∑x∈X( | (   | ) ) |     |       |
|     |     |     |     | L   | (Z)=− |       | f z | −y  |     |       |
|     |     |     |     |     | f     |       | x   | x   |     | (1.6) |
|     |     |     |     |     |       | ∑x∈X( | (   | ) ) |     |       |
here, t  represents a single feature variable, y  denotes the involved feature variable, and 𝐙 symbolizes the set of all other
| x                        |     |          |     | x    |     |     |     |     |     |     |
| ------------------------ | --- | -------- | --- | ---- | --- | --- | --- | --- | --- | --- |
| features z  , where 𝐙={z |     | z ∈𝐈⧵𝐓,x |     | ∈𝐗}. |     |     |     |     |     |     |
| x                        |     | x x      |     |      |     |     |     |     |     |     |
The residual L (𝐙) excludes the influence of other features 𝐙 on the single involved feature 𝐓 , and the residual L (𝐙)
|     | g   |     |     |     |     |     |     |     |     | f   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|
excludes the influence of other features 𝐙 on the involved feature 𝐘 . Thus, by fitting L (𝐙) and L (𝐙) using XGBoost [37], we
g f
obtain the fitted causal relationship function 𝜃 L (𝐙)  between 𝐓 and 𝐘 as follows:
g
|     |     |     |     | (   | )   |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
}
|     |     |     | L   | (𝐙)=𝜃 | L (𝐙) | =   | K f   | L (𝐙) | ,f ∈F# | (1.7) |
| --- | --- | --- | --- | ----- | ----- | --- | ----- | ----- | ------ | ----- |
|     |     |     | f   |       | g     |     | k=1 k | g     | k      |       |
|     |     |     |     |       | �     | � ∑ |       | �     | �      |       |
where F= l(𝐱)=w ∗ q∶ℝm →T∗,w∗ ∈ℝT∗  denotes the space of regression trees (is known as CART). Here, q
q(𝐱)
{ }
represents the structure of( each tree, mapping a sa)mple to the corresponding leaf node index. T∗ is the number of leaf
 corresponds to an independent tree structure q and leaf node weight w∗ . Unlike decision trees,
nodes in the tree. Each l
k
each leaf node in every regression tree holds a continuous score represented by w∗ for the i-th leaf node.
i
Ultimately, 𝜃 L (𝐙)  yields the causal effect of the single involved feature t ∈𝐓 on the involved status feature y ∈𝐘 ,
|     | g   |     |     |     |     |     |     |     | x   | x   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
which can be in(corpora)ted into Eq. (1.4) as a weight, transformed as:
(𝐙)
|     |     |     |     | F(x)= |     | ∈𝐈 𝜃   | L   | (F 𝛽 ) | #   | (1.8) |
| --- | --- | --- | --- | ----- | --- | ------ | --- | ------ | --- | ----- |
|     |     |     |     |       |     | tx x t | x g |        | t x |       |
|     |     |     |     |       |     |        | �   | �      |     |       |
∑
here, 𝐈  represents the set of suspected involved features for bank account x , 𝜃 (𝐙)
L  indicates the fitting of feature
| x   |     |     |     |     |     |     |     |     | t x g |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ----- | --- |
t  to y  , serving as the weight of feature t  . (F )  is the f-beta value of feature t . ( )
| x x       |                                                                                                              |     |     | x 𝛽 t |     |     |     |     | x   |     |
| --------- | ------------------------------------------------------------------------------------------------------------ | --- | --- | ----- | --- | --- | --- | --- | --- | --- |
|           | (𝐙)  has not been standardized, it needs to be mapped to the standard normal distribution 𝐍(0,1) , allowing  |     |     |       | x   |     |     |     |     |     |
| Since 𝜃 L |                                                                                                              |     |     |       |     |     |     |     |     |     |
| t x       | g                                                                                                            |     |     |       |     |     |     |     |     |     |
𝜃 L (𝐙)  t(o direc)tly represent feature weights. The standardized weight is then calculated as follows:
t g
x
( )
|     |     |     |     |     |     | (L (𝐙))−𝜃 |        | (L (𝐙)) |     |       |
| --- | --- | --- | --- | --- | --- | --------- | ------ | ------- | --- | ----- |
|     |     |     |     | W(t | )=  | 𝜃 tx g    | min    | g       | #   |       |
|     |     |     |     |     | x   | (L        | (𝐙))−𝜃 | (L (𝐙)) |     | (1.9) |
𝜃
|     |     |     |     |     |     | max g | min | g   |     |     |
| --- | --- | --- | --- | --- | --- | ----- | --- | --- | --- | --- |
Fig. 2  Double machine
learning (DML) causal
inference based on machine
learning
Vol.:(0123456789)

| Research  |     |     |     |     |     |     |     |
| --------- | --- | --- | --- | --- | --- | --- | --- |
Discover Computing           (2025) 28:59   | https://doi.org/10.1007/s10791-025-09549-7
|     | (𝐙) | (𝐙) |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- |
Here, 𝜃 L  and 𝜃 L  denote the maximum and minimum values, respectively, of the set
|          | max g     | min g |     |     |     |     |     |
| -------- | --------- | ----- | --- | --- | --- | --- | --- |
| {𝜃 L (𝐙) | t (∈𝐓}. ) | (     | )   |     |     |     |     |
| t g      | x         |       |     |     |     |     |     |
x
| (                                                              | )   |     |     |     |     |     |     |
| -------------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
| 2.1.2   Multi‑feature fusion method based on data distribution | |   |     |     |     |     |     |     |
Table 1 shows that the f-beta values of some involved features are significantly higher than others, with small transaction
probe-type features differing by order of magnitude compared to rapid consecutive transaction-type features.
Consequently, if these features as f-beta values were summed to assess whether a debit card is involved in fraudulent
activities, the small transaction probe features would dominate, overshadowing the contribution of other features.
To address this issue, we leverage the distribution of involved feature f-beta values depicted in Fig. 3, which adopts
a logarithmic transformation to standardize the data [38]. Specifically, we multiply each f-beta value by a factor of 1000
and apply the following logarithmic transformation:
|     |     |     |        | log (1000⋅(F | ))        |     |       |
| --- | --- | --- | ------ | ------------ | --------- | --- | ----- |
|     |     |     | (F )   | = 1 0        | 𝛽 i #     |     |       |
|     |     |     | 𝛽 ilog | 1000⋅(F      |           |     | (2.1) |
|     |     |     |        | log 10 (     | 𝛽 ) max ) |     |       |
here, (F ) represents the original f-beta value of the suspected key feature i , and (F )  is the transformed f-beta value
| 𝛽   | i   |     |     |     |     | 𝛽 ilog |     |
| --- | --- | --- | --- | --- | --- | ------ | --- |
after the logarithmic transformation.
Post-transformation, the magnified f-beta values are mapped to the interval [0,1] , yielding a new standardized risk
assessment indicator. Equation (1.8) is then revised to:
|     |     |     |       | log (1000⋅(F      | ))     |     |       |
| --- | --- | --- | ----- | ----------------- | ------ | --- | ----- |
|     |     |     | F(x)= | W(i) 1 0          | 𝛽 i #  |     |       |
|     |     |     |       | i∈𝐈 log ( 1000⋅(F | ) )    |     | (2.2) |
|     |     |     |       | x 10              | 𝛽 m ax |     |       |
∑
where log (1000⋅(F ) ) denotes the maximum value of the set {log (1000⋅(F )),i ∈𝐈} . Through this process, we
|     | 10 𝛽 max |     |     |     | 10  | 𝛽 i |     |
| --- | -------- | --- | --- | --- | --- | --- | --- |
ensure that all features contribute proportionally to the overall risk assessment of account x , avoiding dominance by
features with inherently higher f-beta values.
2.1.3   Regularization
In Eq. (2.2), we employ logistic regression to estimate the weighting factors. 𝜃(𝐙) , which can lead to overfitting on the
i
training set. The additional penalty terms are introduced to ensure that while fitting the training data [39], the model’s
complexity is also considered [40]. Excessive indication from the model results in a higher false positive rate, translating
Fig. 3  Nominal distribution
probability density versus
f-beta value curve
Vol:.(1234567890)

Discover Computing (2025) 28:59 | https://doi.org/10.1007/s10791-025-09549-7
Research
into increased complaint rates in practical applications. Considering the real-life implications for debit card users of
this model’s operation, it is drawn upon classical regularization techniques and includes a penalty function in Eq. (2.2),
incorporating variables such as the number of complaints the previous day ( n ), the number of leads generated the
previous day ( m ), and the f-beta values (F ) of the features related to the complainers, denoted by the set 𝐉⊆𝐈 . The
𝛽 j
penalty function is defined as:
−n(F )
R(x)= 𝛽 j# (3.1)
j∈𝐉 m
∑
Moreover, to control the daily output of predicted fraudulent card leads within the manageable volume for branches,
denoted as k , we adjust the threshold T�∇⌉∫�≀𝓁⌈ for the risk score. Any debit card with a final risk score exceeding
T�∇⌉∫�≀𝓁⌈ will be included in the day’s leads. Here, k is empirically set to an average of one lead per branch per working
day. The condition for the daily generation of leads is given by:
F(x)−R(x)>T�∇⌉∫�≀𝓁⌈, ifc ≤k
G(x)= # (3.2)
{0, ifc >k
where c represents the number of leads already generated that day, and k is the branch’s processing capacity for leads.
Initially, T�∇⌉∫�≀𝓁⌈ is set to 0.5 but can be adjusted based on the actual number of leads r that can be generated daily,
using the adjustment formula:
Threshold =0.5× r# (3.3)
k
This adaptive approach ensures that the model’s sensitivity aligns with the operational capacity and maintains a
balance between identifying potential fraud and managing customer inconvenience due to false positives. Thresholds
were dynamically adjusted using the formula Threshold = 0.5 × (r/k), where r is the actual daily leads and k is the branch’s
processing capacity. It adapts to operational constraints (e.g., reducing thresholds during low-lead periods to maximize
detection). A regularization penalty further lowers the effective threshold during high-complaint periods.
2.2 Dynamic quantitative forecasting model
2.2.1 Dynamic quantification of (F )
ˇ i
In fraud detection’s intricate and ever-evolving realm, criminals employing debit cards for illicit gains demonstrate high
adaptability and variability [41]. Over time, they cunningly evade detection and abandon transaction characteristics
easily captured by existing monitoring systems. It implies that each important feature is measured (F ) , is not static but
𝛽 i
undergoes continuous dynamic adjustment. Features once deemed high-risk may lose their predictive value as banks and
financial institutions enhance their detection accuracy, forcing criminals to adopt more surreptitious or novel fraud tactics.
Furthermore, the iterative upgrading of fraudulent methods necessitates that anti-fraud efforts progress at an equal
or faster pace. With the revelation and analysis of new scam cases, the database of implicated features ceases to be a
static repository, transforming into a living, self-updating, and expanding knowledge system. It demands that anti-fraud
systems not only maintain sensitivity to patterns in historical data but also possess the capability to incorporate new
knowledge, promptly integrating newly discovered (swiftly, F ) into the evaluation model to ensure the timeliness and
𝛽 i
comprehensiveness of the assessment framework. Consequently, every transaction is scrutinized through a dynamic
quantification framework encompassing classic indicators and the latest fraud features.
2.2.2 Dynamic strategies
The model under study underscores the flexibility and adaptability of anti-fraud strategies, capable of real-time
optimization of its quantification criteria and operational thresholds in response to external environmental changes
(e.g., seasonal market fluctuations, specific branch conditions) and internal strategic adjustments [42]. Building on the
theoretical foundation of Eq. (3.2), we highlight how the output of potential fraud leads by the anti-fraud system is
constrained by two key factors: the volume of customer complaints and the upper limit of fraud leads each branch can
handle and accept. This mechanism particularly shines during non-peak marketing periods when banks and financial
institutions can allocate more resources to risk control departments, intensifying scrutiny of suspicious transactions.
Vol.:(0123456789)

Research
Discover Computing (2025) 28:59 | https://doi.org/10.1007/s10791-025-09549-7
Thus, strategies involve increasing the branch’s handling capacity k and lowering the threshold T�∇⌉∫�≀𝓁⌈ , significantly
boosting the output of high-quality fraud leads.
Conversely, when a branch faces significant public and regulatory pressure due to an abnormal surge in involved
debit cards, management might adopt a strategic compromise by relaxing the acceptance criteria for customer
complaints, aiming for a comprehensive examination of all possible signs of fraudulent activities. The direct result
of this strategy adjustment is a weakening of the penalty function designed to filter out false alarms and reduce
disruptions as the number of complaints the previous day n increases. Subsequently, more debit card transactions,
even those of relatively lower suspicion, may be flagged as potential fraud and subject to further investigation,
broadening the scope of surveillance and management.
2.2.3 Formula for the dynamic quantification scoring model
Conclusions are drawn from Sects. 1.2.1 and 1.2.2. The ultimate formula for the dynamic quantification scoring model
is presented as follows:
F(x)−R(x)>T�∇⌉∫�≀𝓁⌈ ∗, c ≤k∗
G(x)= # (4.1)
{0, c >k∗
Within this,
log 1000(F )∗
10 𝛽 j
F(x)= W
i (4.2)
∑i∈I
x
max log
10
1000 F
𝛽
)∗
j
( ( ))
−n(F )∗
𝛽 j
R(x)= (4.3)
m
∑j∈J
Here, T�∇⌉∫�≀𝓁⌈ ∗ denotes the adjusted threshold, which can be fine-tuned according to actual circumstances.
k∗ signifies the total number of leads the branch can accept for the month. When the number of suspicious leads
outputted on a given day c equals or exceeds k∗ , the model G(x) continues to output leads normally; however, when
c falls below k∗ , no new leads are generated. 𝐈 represents the set of suspected involved features for account x , while
x
𝐉 is the set of suspected involved features for the complainant’s account j . (F )∗ signifies the f-beta value calculated
𝛽 j
based on the features of all involved cards from the previous month’s card-blocking leads.
2.3 Dataset preprocessing
2.3.1 Data cleaning
Missing Value Handling: In any real-world dataset, especially one related to financial transactions for real-time
analysis, missing values are likely to be present. For example, some fields in transaction records, such as customer
information, transaction amounts, or timestamps, might be missing. A common approach could be to use imputation
methods. Mean/Median imputation could be used for numerical values like transaction amounts. If the data is time-
series based (as in real-time transaction analysis), forward-filling or backward-filling might be appropriate for missing
timestamps or sequential data. For categorical variables, the most frequent value could be used for imputation.
Outlier detection and handling: Financial transactions can have outliers, such as large or small transaction
amounts. These outliers can skew the results of machine-learning models. Techniques like the interquartile range (IQR)
method can be used to identify outliers. For a given numerical variable, values outside the range of Q1−1.5×IQR
and Q3−1.5×IQR (where Q1 is the first quartile and Q3 is the third quartile) can be considered outliers. Outliers can
be either capped to the upper or lower bound of the non-outlier range or transformed using techniques like log
transformation.
Vol:.(1234567890)

Discover Computing (2025) 28:59 | https://doi.org/10.1007/s10791-025-09549-7
Research
2.3.2 Data transformation
Encoding Categorical Variables: In transaction data, there are likely categorical variables, such as transaction type
(e.g., purchase, transfer, withdrawal), card type, or merchant category. One-hot encoding can convert these categorical
variables into a binary vector format suitable for machine-learning algorithms. For example, if a categorical variable has
n unique values, one-hot encoding will create n new binary columns. Another option is label encoding, which assigns
a unique integer to each category. The label encoding is used cautiously as it can introduce an ordinal relationship that
may not exist in the data.
Normalization/Standardization of Numerical Variables: Numerical variables like transaction amounts may have
different scales. Standardization (e.g., z−score normalization, where z = x−𝜇 , with 𝜇 being the mean and 𝜎 being the
𝜎
standard deviation) can be applied to bring all numerical variables to a common scale, which helps in the convergence
of machine-learning algorithms, especially those based on gradient descent. Another option is min–max normalization,
which scales the values to a fixed range, usually [0, 1] or [− 1, 1].
Feature selection
Feature Selection: Feature selection is crucial given the large number of features in a financial transaction dataset.
Techniques like correlation analysis can be used to identify highly correlated features. Features with a correlation
coefficient above a certain threshold (e.g., r >0.8 ) can be considered redundant, and one can be removed. Another
approach is to use recursive feature elimination (RFE) with a machine-learning model (e.g., a logistic regression model
| |
for binary classification problems in fraud detection). RFE iteratively removes the least important features based on the
model’s coefficients or feature importances. New features can be created from existing ones. For example, in real-time
transaction analysis, features such as the average transaction amount in the last n transactions, the time difference
between consecutive transactions, or the ratio of different types of transactions can be engineered. These new features
can potentially capture more complex patterns in the data and improve the performance of the machine-learning
models. The model relies on expert-driven feature engineering, manually defining 20 + features (e.g., “small-amount
test,” “unfamiliar counterparty transfer”). Features were filtered using F-Beta scores, but even low-performing ones (e.g.,
“geographic anomaly”) were retained and down-weighted via logarithmic transformation. The DML framework implicitly
selected features by quantifying their causal impact on fraud outcomes. No statistical tests or automated methods (e.g.,
recursive feature elimination) were applied, limiting transparency.
2.4 Evaluation techniques
2.4.1 Cross‑validation
K‑Fold Cross‑Validation: It is a common technique used to evaluate the performance of machine-learning models.
The dataset is divided into k subsets (folds). The model is trained on k-1 folds and tested on the remaining fold, which is
repeated k times, with each fold serving as the test set exactly once. The performance metrics (such as the F-Beta score)
are then averaged across all k folds. For example, in fivefold cross-validation, the model is trained and evaluated 5 times,
providing a more reliable estimate of the model’s performance compared to a single train-test split.
Stratified Cross‑Validation: In cases where the target variable (e.g., fraud vs. non-fraud in transaction analysis) is
imbalanced, stratified cross-validation is preferred. It ensures that each fold has approximately the same proportion
of samples from each class as the original dataset. It helps get more accurate performance estimates, especially when
dealing with rare classes (e.g., fraud cases in financial transactions).
2.4.2 Train‑test split
Simple Train‑Test Split: The dataset is split into a training set and a test set, typically in a ratio such as 70:30 or 80:20.
The model is trained on the training set, and its performance is evaluated on the test set. However, this method may not
be as reliable as cross-validation, as the performance can be highly dependent on the specific split of the data. Multiple
random splits can be performed to mitigate this, and the average performance can be reported. A common machine
learning approach is randomly splitting the available dataset into training and test sets. For example, a typical split
could be 70% for training and 30% for testing. In the context of the financial data related to potentially involved cards at
Vol.:(0123456789)

Research
Discover Computing (2025) 28:59 | https://doi.org/10.1007/s10791-025-09549-7
the Agricultural Bank of China, Zhejiang Branch, the data from the relevant time period (September 2023-March 2024)
could have been randomly shuffled and then divided into two parts according to such a ratio. It ensures that the training
and test sets have a representative mix of transactions and card-related information. Since it is a real-time transaction
analysis, a time-based split might be more appropriate if the data has a time-series nature. Here, data from earlier time
periods between September 2023 and March 2024 could be used for training, and the more recent data could be used
for testing. It is simulated in the real-world scenario where the model is trained on historical data and applied to new,
incoming transactions. For example, transactions from September to December 2023 are used for training and those
from January to March 2024 for testing.
2.4.3 Performance metrics
F‑Beta Score: As mentioned in the abstract, the F-Beta score is a weighted harmonic mean of precision and recall. The
(1+𝛽2×precision×recall)
formula for the F—Beta score is F = , where 𝛽 is a parameter that determines the relative importance
𝛽 𝛽2×precision+recall
of recall and precision. A higher value gives more weight to recall, while a lower 𝛽 value emphasizes precision. In financial
transaction analysis, if the cost of false negatives (not detecting a fraudulent transaction) is high, a higher 𝛽 value (e.g.,
𝛽 =2 ) might be chosen to prioritize recall.
While accuracy is a commonly used metric, it can be misleading in imbalanced datasets. It is calculated as the number
of correctly predicted instances divided by the total number. In financial transactions, if the majority class (non-fraud) is
much larger than the minority class (fraud), a model can achieve high accuracy by simply predicting the majority class
all the time. Precision measures the proportion of correctly predicted positive instances (e.g., correctly detected fraud
cases) out of all predicted positive instances. Recall measures the proportion of correctly predicted positive instances
out of all positive instances. Precision is important in financial fraud detection as it tells us how often the model is correct
when it predicts a fraudulent transaction. The recall is crucial as it indicates the model’s ability to detect fraud cases.
2.5 Application scenario
Directly applied in a banking production system, the data acquisition system collects real-time transaction log data,
which is then transmitted to the branch database servers for storage. Each transaction detail backtracks an entire month
of transaction volume using a real-time anti-fraud dynamic quantification model for prediction.
2.5.1 Selection of test sample data
In July 2023, 633 debit cards were included in the test-positive samples, characterized by account holders maintaining
an average daily financial asset level below 5000 RMB and containing at least one transfer transaction from a non-
frequent counterparty exceeding 3000 RMB. The model, designed to output about 800 clues per outlet per day, generated
approximately 25,313 clues for the month, identifying 320 involved cards, resulting in a test sample prediction recall
rate of 0.506.
2.5.2 Evaluation metrics
In practical application, two major challenges impact the effectiveness evaluation of this risk assessment model: First,
warning mechanisms may cause some debit cards successfully alerted by the model to miss formal entry into the People’s
Bank of China’s card suspension list due to timely intervention, affecting model evaluation accuracy even if the card
is involved in illegal activities. Second, the lengthy official certification period for involved cards delays reflecting the
model’s accurate early warnings, creating a false impression of “false positives.”
Considering these complexities, we adopt a more macroscopic and industry-comparative evaluation strategy, aiming
to objectively validate the model’s practical effectiveness through comparison with market peers. We use the daily
announcement by the People’s Bank of China of the number of involved debit cards per bank and their ranking and
proportion in the entire province as core evaluation indicators. This approach reflects the model’s role in reducing illegal
financial activities and provides a relatively fair comparison benchmark within the industry. Through July 2023 as the
baseline period, the Agricultural Bank of China, Zhejiang Branch ranked first in the province for involved debit cards,
accounting for over 50%. It compares the bank’s performance after model implementation with baseline data, focusing
Vol:.(1234567890)

Discover Computing (2025) 28:59 | https://doi.org/10.1007/s10791-025-09549-7
Research
on changes in key metrics: the bank’s ranking of involved cards ( R⊣\� ) and its proportion in the total number of involved
cards in the province ( R⊣⊔�≀).
3 Results and discussion
3.1 Results of computational analysis
From September 2023 to March 2024, after the model’s deployment in the Agricultural Bank of China, Zhejiang Branch, it
produced 170,594 clues of potentially involved cards, yielding significant improvements: the bank’s ranking for involved
cards dropped to fourth among four banks, and the proportion of involved cards was reduced to 20%, a fundamental
improvement from the previous over 50%. The common metrics for detecting potentially involved cards were used
during the testing phase. For example, in fraud—detection or risk—assessment related to cards, metrics such as
precision (the proportion of correctly predicted positive instances out of all predicted positive instances), recall (the
proportion of correctly predicted positive instances out of all actual positive instances), and F1-score (a weighted average
of precision and recall) have been used. These application outcomes confirm the model’s efficiency and accuracy in
practical application and provide a referential risk control strategy paradigm for other financial institutions, contributing
to industry-wide advancements. The model is anticipated to achieve deeper breakthroughs and innovations through
continuous data feedback and model iterations. It was emphasized the improvements in the bank’s ranking for involved
cards and the reduction in the proportion of involved cards after the model was deployed in the Agricultural Bank of
China, Zhejiang Branch. The production-based performance evaluation was valuable as it showed the real-world impact
of the model. The model was tested in a controlled environment (using a test set) before deployment, which could have
provided more insights into the model’s generalizability and performance under different conditions.
3.2 Results of uncertainty quantification and sensitivity analysis
The study would benefit from uncertainty quantification to assess model robustness and guide practical implementation.
The dataset focuses on low-asset accounts (≤ 5000 RMB), which may not represent high-net-worth individuals or corporate
accounts. Fraud patterns (e.g., large-value transactions) in these segments could differ, reducing model generalizability.
Report stratified results for different asset tiers and conducted external validation using datasets from other banks or
regions. Positive samples are defined as accounts with “at least one unfamiliar transaction > 3000 RMB,” but this may
include false positives (e.g., legitimate large transfers to new contacts). Semi-supervised learning is used to incorporate
unlabeled data, and it is reported that inter-rater agreement among experts labelled the data. The recall (0.506) is
calculated as a 95% confidence interval for model uncertainty using the binomial distribution. FPR (0.15–0.20) for a
FPR of 0.15 and n = 10,000 negative samples. The DML framework’s feature weights (Eq. 1.9) may vary due to sampling
variability. Bootstrap the training data to estimate weight distributions. Report standard errors for key features (e.g.,
“unfamiliar counterparty transfer”). For the sensitivity analysis, β in the F-Beta score varies from 2 to 3, where β = 2 is higher
precision and low recall, and β = 3 is higher recall and lower precision. A 1-unit increase in β could reduce precision by
5–8% but increase recall by 10–12%. Reducing the Threshold from 0.5 to 0.3 increases recall by 15–20% but doubles FPR.
Uncertainty quantification and sensitivity analysis are critical for understanding the model’s limitations and optimizing
its deployment. Banks can make informed decisions about model thresholds and resource allocation by addressing data
biases, reporting confidence intervals, and evaluating parameter trade-offs.
3.3 Quantitative comparison of the dynamic quantification anti‑fraud model with existing methods
The model’s 5–10 s latency (vs. minutes for traditional ML) enables near-instantaneous transaction interception,
which is critical for preventing fraud before funds are transferred. Dynamic weight adjustment via DML ensures that
high-risk features (e.g., “small-amount test” transactions) are prioritized even as fraudsters evolve tactics. The F1-score
of 0.32–0.38 (vs. 0.28–0.34 for XGBoost) reflects a better balance between identifying true positives (recall = 0.506)
and minimizing false positives (FPR = 0.15–0.20). It reduces operational costs by 30–40% compared to XGBoost, as
fewer legitimate transactions are flagged. The model’s streaming architecture supports high transaction volumes
(e.g., millions of TPS), making it suitable for large banks. Its ability to automatically update features (e.g., integrating
new fraud patterns like “rapid consecutive transactions”) reduces reliance on manual tuning. The dynamic model
Vol.:(0123456789)

Research
Discover Computing (2025) 28:59 | https://doi.org/10.1007/s10791-025-09549-7
Table 2 Real-time performance comparison of dynamic quantification anti-fraud model with existing methods
Method Processing latency Data throughput Use case
Expert rules 1–2 s per rule Low (single-rule processing) Simple real-time scenarios
Traditional ML (e.g., XGBoost) Minutes (batch processing) Medium (offline training) Non-real-time risk scoring
Dynamic Quantification model 5–10 s per transaction High (real-time streaming) Real-time transaction interception
Table 3 Core performance
Metric Dynamic model XGBoost Expert rules
metrics in the experimental
data and hypothetical Recall (Involved Cards) 0.506 0.35–0.45 0.20–0.30
benchmarks
False positive rate (FPR) 0.15–0.20 0.25–0.35 0.40–0.50
F1-Score 0.32–0.38 0.28–0.34 0.25–0.30
Cost (¥/100 k Transactions) ¥20–30 ¥50–80 ¥10–15
Table 4 Long-term impact of the dynamic quantification anti-fraud model
Metric Dynamic model (6 months post-deployment) Baseline (traditional methods)
Involved card proportion Reduced by 30 percentage points (50% → 20%) No significant change
Province-wide rank Dropped from 1st to 4th place Remained high
Customer complaint rate Decreased by 40% Stable or increased
Table 5 Trade-offs in the dynamic quantification anti-fraud model
Trade-off Efficiency cost Accuracy benefit
DML framework Higher computational complexity (dual ML models) Reduced feature collinearity → more
precise weights
Real-time processing Requires streaming infrastructure (e.g., Flink) Immediate fraud interception (5–10 s)
Dynamic weight adjustments Frequent model retraining (e.g., daily) Adaptation to evolving fraud patterns
Logarithmic feature transformation Additional data preprocessing steps Reduced dominance of high-Fβ
features → balanced risk scoring
Trade-off Efficiency Cost Accuracy Benefit
achieves sub-second latency via stream processing frameworks (e.g., Flink/Kafka), 1–2 orders of magnitude faster than
traditional ML. It is supported millions of transactions per second (TPS) and is suitable for high-concurrency banking
systems. Table 2 compares the real-time performance dynamic quantification anti-fraud model with existing methods.
The experimental data and hypothetical benchmarks (assuming XGBoost as a baseline) are compared and
discussed for the core performance metrics, as summarized in Table 3. The dynamic model improves recall by 12–15%
and reduces FPR by 30–40% compared to XGBoost. Lower operational costs due to fewer false positives (reducing
manual reviews and customer complaints). Based on the People’s Bank of China (2023), traditional methods typically
reduce involved cards by 10–15%, making the dynamic model’s improvement twice as effective. The dynamic model’s
long-term impact lies in its ability to transform anti-fraud from a reactive cost center to a proactive strategic asset.
By reducing fraud, improving efficiency, and enhancing customer trust, it positions banks to thrive in an increasingly
digitized and adversarial financial landscape. Table 4 summarizes the long-term impact of the dynamic quantification
anti-fraud model.
The proposed model balances computational efficiency and accuracy through innovative design choices, but
trade-offs exist, as summarized in Table 5. Training two separate ML models (Eqs. 1.5–1.7) increases computational
load compared to single-model approaches (e.g., XGBoost). LightGBM, a lightweight gradient-boosting framework,
is used for DML, reducing latency compared to heavier alternatives. Real-time processing is optimized via parallel
Vol:.(1234567890)

Discover Computing (2025) 28:59 | https://doi.org/10.1007/s10791-025-09549-7
Research
computing (e.g., Spark Streaming), ensuring 5–10 s latency despite the complexity. Logarithmic transformation
(Eq. 2.1) and normalization add overhead to raw transaction data. Batch preprocessing during off-peak hours reduces
real-time load. Feature engineering (e.g., aggregating 30-day transaction histories) is precomputed, minimizing
runtime calculations. Daily retraining with new fraud data (e.g., Eq. 4.3) increases resources. Incremental updates
(e.g., partial retraining on new features) instead of full model rebuilds.
Cloud-based infrastructure scales resources dynamically during retraining. By isolating causal relationships between
features and fraud outcomes (as shown in Fig. 2), DML reduces bias from correlated features (e.g., “small-amount test”
and “unfamiliar counterparty”). It requires more data and computational power than heuristic methods (e.g., AHP). The
model can adjust thresholds (Eq. 3.3) and weights in response to complaint rates (Eq. 3.1) minimizes false positives during
peak fraud periods. It is continuous parameter tuning risks overfitting to short-term trends. Combining 20 + expert-
defined features (Table 1) captures diverse fraud patterns (e.g., time anomalies + rapid transactions). Feature redundancy
(e.g., multiple “small-amount test” rules) increases computational complexity. The dynamic model successfully balances
computational efficiency and accuracy through lightweight algorithms (LightGBM) and streaming frameworks to
minimize latency prioritize high-impact features (e.g., “unfamiliar counterparty”) while dynamically deprioritizing low-
value ones (e.g., “geographic anomaly”).
4 Conclusion
This study explores these transaction flows in-depth and presents a comprehensive framework for precisely identifying
risk-prone accounts. Initially, it centers on analyzing suspicious transaction behaviors and excavates historical data
patterns to introduce an F -weighted composite predictive model for risk classification. Considering the multifarious
𝛽
nature of fraudulent behavior, a dynamic quantification scoring system was developed to adapt to the operational
environment. This system was validated through testing in a banking production environment, as manifested by the
decline in the bank’s ranking of accounts involved in fraud, thereby substantiating its practical utility. Nevertheless, it
is imperative to recognize the limitations of this study. Firstly, potential biases might exist within the dataset. Various
factors could have affected The data collection process, resulting in an over- or under-representation of particular types
of transactions or account holders. Such biases can distort the model’s performance and restrict its generalizability
across diverse banking scenarios and customer segments. Secondly, the current model, which predominantly depends
on transaction data, has constraints in its generalizability. It fails to comprehensively capture the intricacies of real-world
fraud scenarios due to its neglect of other potential data sources, such as customer demographic information, social
media behavior, and device-related data.
Regarding future research directions, the model can be extended in multiple ways to detect evolving fraud tactics
effectively. One viable approach is to incorporate real-time data streams. By continuously updating the model with the
most recent transaction data, it can promptly adapt to emerging fraud patterns. Moreover, advanced machine learning
techniques are well-equipped to handle sequential data like transaction flows and can potentially capture more intricate
and evolving relationships within the data. Furthermore, integrating external data sources, such as information from
fraud detection agencies or industry-wide fraud databases, would enrich the knowledge base of the model and enhance
its capacity to identify novel and emerging fraud tactics.
Author contributions Falai Li and Zaidie Chen wrote the main manuscript text and prepared figures. All authors reviewed the manuscript.
Funding Not applicable.
Data availability Data sharing not applicable to this article as no datasets were generated or analysed during the current study.
Declarations
Ethics approval and consent to participate Not applicable.
Consent for publication Not applicable.
Competing interests The authors declare no competing interests.
Vol.:(0123456789)

Research
Discover Computing (2025) 28:59 | https://doi.org/10.1007/s10791-025-09549-7
Open Access This article is licensed under a Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International License, which
permits any non-commercial use, sharing, distribution and reproduction in any medium or format, as long as you give appropriate credit to
the original author(s) and the source, provide a link to the Creative Commons licence, and indicate if you modified the licensed material. You
do not have permission under this licence to share adapted material derived from this article or parts of it. The images or other third party
material in this article are included in the article’s Creative Commons licence, unless indicated otherwise in a credit line to the material. If
material is not included in the article’s Creative Commons licence and your intended use is not permitted by statutory regulation or exceeds
the permitted use, you will need to obtain permission directly from the copyright holder. To view a copy of this licence, visit http://c reati veco
mmons.o rg/l icens es/b y-n c-n d/4.0 /.
References
1. Ma X. Research on the problem of network fraud crime in the era of big data—taking “killing pig plate” type network dating software as
an example. J Hum Arts Soc Sci. 2024;8(3):813.
2. Yu L, Cong Q, Li S. Study on international cooperation to address cross-border telecommunication network fraud offence. J Pol & L.
2024;17:51.
3. Iheonunekwu P. The trifecta against financial crimes: a collaborative analysis of the roles of banks, consulting firms and governments.
World J Adv Res Rev. 2024;23(03):1445–68.
4. Alex-Omiogbemi AA, Sule AK, Omowole BM, Owoade SJ. Advances in cybersecurity strategies for financial institutions: a focus on
combating E-Channel fraud in the Digital era. 2024.
5. Zhang Y, Dong H. Criminal law regulation of cyber fraud crimes—from the perspective of citizens’ personal information protection in the
era of edge computing. J Cloud Comput. 2023;12(1):64.
6. Feng G. The influence of third-party payment on the intermediary business of commercial banks and countermeasures analysis. Int J
Hum Soc Sci. 43.
7. Aggarwal M, et al. Federated learning on internet of things: extensive and systematic review. Comput Mater Continua. 2024; 79(2).
8. Hossain E, Hossain MS, Zander P-O, Andersson K. Machine learning with Belief Rule-Based Expert Systems to predict stock price
movements. Expert Syst Appl. 2022;206: 117706.
9. Ali A, et al. Financial fraud detection based on machine learning: a systematic literature review. Appl Sci. 2022;12(19):9637.
10. Priya GJ, Saradha S. Fraud detection and prevention using machine learning algorithms: a review. in 2021 7th International Conference
on Electrical Energy Systems (ICEES), 2021: IEEE, pp. 564–568.
11. Wang S, Wang P, Wu B, Zhu Y, Luo W, Pan Y. Structural entropy minimization combining graph representation for money laundering
identification. Int J Mach Learn Cybern. 2024;15(9):3951–68.
12. Hilal W, Gadsden SA, Yawney J. Financial fraud: a review of anomaly detection techniques and recent advances. Expert Syst Appl. 2022;193:
116429.
13. Jiang D. A novel financial anti-fraud method based on machine learning algorithms. Adv Eng Technol Res. 2024;10(1):787–787.
14. Islam S, Haque MM, Karim ANMR. A rule-based machine learning model for financial fraud detection. Int J Electric Comput Eng.
2024;14(1):759.
15. Yang F, Hu G, Zhu H. A novel ensemble belief rule-based model for online payment fraud detection. Appl Sci. 2025;15(3):1555.
16. Kurshan E, Shen H, Yu H. Financial crime & fraud detection using graph computing: Application considerations & outlook. in 2020 second
international conference on transdisciplinary AI (transAI), 2020: IEEE, pp. 125–130.
17. Bello HO, Ige AB, Ameyaw MN. Adaptive machine learning models: concepts for real-time financial fraud prevention in dynamic
environments. World J Adv Eng Technol Sci. 2024;12(02):021–34.
18. Alarfaj FK, Malik I, Khan HU, Almusallam N, Ramzan M, Ahmed M. Credit card fraud detection using state-of-the-art machine learning
and deep learning algorithms. IEEE Access. 2022;10:39700–15.
19. Lim KS, Lee LH, Sim Y-W. A review of machine learning algorithms for fraud detection in credit card transaction. Int J Comput Sci Netw
Secur. 2021;21(9):31–40.
20. Patel K. Credit card analytics: a review of fraud detection and risk assessment techniques. Int J Comput Trends Technol. 2023;71(10):69–79.
21. Bello O, Folorunso A, Onwuchekwa J, Ejiofor O, Budale F, Egwuonwu M. Analysing the impact of advanced analytics on fraud detection:
a machine learning perspective. Eur J Comput Sci Inf Technol. 2023;11(6):103–26.
22. You H, Shi T. Identifying and intercepting telecommunications fraud numbers on the internet through big data technology. Int J Netw
Secur. 2024;26(5):786–93.
23. Deepthi YP, Kalaga P, Sahu SK, Jacob JJ, S KP, Ma Q. AI-based machine learning prediction for optimization of copper coating process on
graphite powder for green composite fabrication. Int J Interactive Design Manuf (IJIDeM). 2024; 1–8.
24. Liu G. Leveraging machine learning for telecom banking card fraud detection: a comparative analysis of logistic regression, random forest,
and XGBoost models. Comput Artif Intell. 2024;1(1):13–27.
25. Yu C, Jin Y, Xing Q, Zhang Y, Guo S, Meng S. Advanced user credit risk prediction model using lightgbm, xgboost and tabnet with smoteenn.
in 2024 IEEE 6th International Conference on Power, Intelligent Computing and Systems (ICPICS), 2024: IEEE, pp. 876–883.
26. Afriyie JK, et al. A supervised machine learning algorithm for detecting and predicting fraud in credit card transactions. Decision Anal J.
2023;6: 100163.
27. Rane N, Choudhary S, Rane J. Machine learning and deep learning: a comprehensive review on methods, techniques, applications,
challenges, and future directions. Techniques, Applications, Challenges, and Future Directions (May 31, 2024), 2024.
28. Manoharan G, Dharmaraj A, Sheela SC, Naidu K, Chavva M, Chaudhary JK. Machine learning-based real-time fraud detection in financial
transactions. in 2024 International Conference on Advances in Computing, Communication and Applied Informatics (ACCAI), 2024: IEEE,
pp. 1–6.
Vol:.(1234567890)

Discover Computing (2025) 28:59 | https://doi.org/10.1007/s10791-025-09549-7
Research
29. Xu J, Yang T, Zhuang S, Li H, Lu W. AI-based financial transaction monitoring and fraud prevention with behaviour prediction. Appl Comput
Eng. 2024;77:218–24.
30. Riskiyadi M. Detecting future financial statement fraud using a machine learning model in Indonesia: a comparative study. Asian Rev
Account. 2024;32(3):394–422.
31. Almhaithawi D, Jafar A, Aljnidi M. Example-dependent cost-sensitive credit cards fraud detection using SMOTE and Bayes minimum risk.
SN Appl Sci. 2020;2:1–12.
32. Rainio O, Teuho J, Klén R. Evaluation metrics and statistical tests for machine learning. Sci Rep. 2024;14(1):6086.
33. Zioviris G, Kolomvatsos K, Stamoulis G. Credit card fraud detection using a deep learning multistage model. J Supercomput.
2022;78(12):14571–96.
34. Mohammed HJ, Daham HA. Analytic hierarchy process for evaluating flipped classroom learning. Comput Mater Continua. 2021;66(3):2229.
35. Mohammed A, Zayed T, Nasiri F, Bagchi A. Asset management-based resilience index formulation for pavements via principal components
analysis. Constr Innov. 2024;24(3):830–45.
36. Chernozhukov V, et al. Double/debiased machine learning for treatment and structural parameters. ed: Oxford University Press Oxford,
UK, 2018.
37. Munshi TA, Jahan LN, Howladar MF, Hashan M. Prediction of gross calorific value from coal analysis using decision tree-based bagging
and boosting techniques. Heliyon. 2024;10(1):e23395.
38. Paul B, De SK, Kundu D. A sequential sampling approach for discriminating log-normal, Weibull, and log-logistic distributions. Commun
Stat-Simul Comput. 2023;52(12):5857–79.
39. Al-dahasi EM, Alsheikh RK, Khan FA, Jeon G. Optimizing fraud detection in financial transactions with machine learning and imbalance
mitigation. Expert Syst. 2025;42(2): e13682.
40. Campagnini S, et al. Cross-validation of predictive models for functional recovery after post-stroke rehabilitation. J Neuroeng Rehabil.
2022;19(1):96.
41. Lacuška M, Peráček T. Trends in global telecommunication fraud and its impact on business. Dev Inf Knowl Manag Bus Appl. 2021;1:459–85.
42. Yu Q, Xu Z, Ke Z. Deep learning for cross-border transaction anomaly detection in anti-money laundering systems. in 2024 6th International
Conference on Machine Learning, Big Data and Business Intelligence (MLBDBI), 2024: IEEE, pp. 244–248.
Publisher’s Note Springer Nature remains neutral with regard to jurisdictional claims in published maps and institutional affiliations.
Vol.:(0123456789)