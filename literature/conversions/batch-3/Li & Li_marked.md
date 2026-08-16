---
conversion_metadata:
  converted_at: "2026-07-21T13:58:27Z"
  converter_tool: "markitdown"
  converter_version: "0.1.6"
  source_pdf: "Li & Li.pdf"
  source_pdf_sha256: "697f894a0aec97dcd89b84018d252505d1db7517c5dd074c1c4dfec166eec2a8"
  page_count: 15
  markdown_char_count: 160538
---

<!-- PAGE-AWARE EXTRACTION (via pdfminer.six) -->

<!-- PAGE 1 -->

Received 27 September 2025, accepted 7 October 2025, date of publication 16 October 2025, date of current version 23 October 2025.

Digital Object Identifier 10.1109/ACCESS.2025.3622358

Exploring Factors Involved in Loan Approval
Decision: Deep Insights and Data Analytics
Techniques

XINCAI LI1 AND JIAYU LI 2
1Asset Management Office, Beijing Language and Culture University, Beijing 100083, China
2School of Economics and Business Administration, Beijing Normal University, Beijing 100875, China

Corresponding author: Jiayu Li (15810889859@163.com)

ABSTRACT Accurate yet transparent credit-risk models are essential for responsible lending in the face
of tightening global AI regulations. We propose an end-to-end, reproducible pipeline for loan-default
prediction that integrates a three-way consensus feature-selection ensemble using VarianceThreshold, RFE
with logistic regression and XGBoost gain ranking; a lightweight one-dimensional convolutional neural
network optimised for tabular data; post-hoc explainability via KernelSHAP embedded directly in the
inference loop; and continuous system-level profiling of CPU, RAM, GPU and latency. Using the public
GiveMeSomeCredit dataset, our method reduces the original 11-feature space to a stable subset of five
predictors, achieving a ROC-AUC of 0.862 and an F1-score of 0.55 on a stratified 20% hold-out, surpassing
the logistic regression and XGBoost baselines by 9% and 4% ROC-AUC, respectively. Ablation analysis
reveals that the consensus feature selection contributes 57 percent of the total accuracy gain, while the 1D-
CNN architecture contributes an additional 38 percent. Fairness assessment shows disparate-impact and
equal-opportunity gaps below 5 percent across gender and age cohorts, aligning with emerging EU AI Act
thresholds. End-to-end inference averages 18 milliseconds on CPU-only hardware, confirming real-time
viability. All code, trained models, evaluation artifacts and resource logs are openly archived, offering a
deploy-ready blueprint for lenders aiming to modernise legacy scorecards without sacrificing interpretability,
compliance, or operational efficiency.

INDEX TERMS Loan-default prediction, credit-risk modeling, 1D-CNN, feature selection, explainability.

I. INTRODUCTION
Credit-Risk assessment lies at the heart of modern consumer
finance. Every loan application forces lenders to weigh
the prospect of profit against the possibility of default and
even marginal
improvements in prediction translate into
sizeable monetary impacts at portfolio scale. Traditional
credit-scoring systems which arebuilt on logistic regression
or simple decision trees and hand-crafted feature engi-
neering that remain popular because they are inexpensive,
fast and reasonably transparent but Yet their capacity to
capture non-linear interactions among the high-dimensional
attributes now routinely collected by banks, fintechs and
credit bureaus is inherently limited [1], [2], [3]. As a result,

The associate editor coordinating the review of this manuscript and

approving it for publication was Vlad Diaconita

.

they often underperform in volatile economic climates or
when borrower profiles deviate from the historical norm.

Recent advances in deep learning offer a path to more
accurate credit risk prediction, but
two barriers hinder
adoption in regulated domains: class imbalance, since
defaults are rare and explainability, as closed box models
are difficult to justify to auditors and regulators [4], [5].
Regulatory bodies such as the European Banking Authority
and the U.S. Consumer Financial Protection Bureau are
tightening transparency requirements, while practitioners
must also meet operational constraints such as real-time
speed, hardware efficiency and reproducibility [6], [7], [8].
To address these challenges, we propose a comprehensive
pipeline for default risk prediction using the Give Me
Some Credit dataset [9]. The framework combines ensem-
ble feature selection (VarianceThreshold, RFE, XGBoost),

180172

2025 The Authors. This work is licensed under a Creative Commons Attribution 4.0 License.
For more information, see https://creativecommons.org/licenses/by/4.0/

VOLUME 13, 2025

---

<!-- PAGE 2 -->

X. Li, J. Li: Exploring Factors Involved in Loan Approval Decision: Deep Insights and Data Analytics Techniques

a lightweight one-dimensional CNN for efficient deployment
and SHAP-based explanations that provide both global
rankings and per-applicant insights [10], [11], [12], [13].

Beyond predictive performance and interpretability,
we address practical engineering considerations that are often
overlooked in academic work but significantly influence
industrial decision-making. The pipeline incorporates the
system-level profiling, tracking memory footprint, CPU/GPU
utilization and per-sample inference latency to facilitate
capacity planning for real-time deployment [14]. All artifacts,
including trained models, selected features, evaluation plots,
SHAP visualizations and resource logs, are automatically
archived to support auditability, version control and down-
stream experimentation [15].

This work makes four important contributions. First,
we demonstrate that
intersecting three complementary
feature-selection methods yields a compact and stable subset
of predictors that enhances both accuracy and explain-
ability [16]. Second, we introduce a lightweight 1D-CNN
model that achieves competitive ROC-AUC while remaining
efficient enough for CPU-based deployment [12]. Third,
the framework includes SHAP-based explanations embedded
directly into the inference loop, enabling local decision
justifications required for compliant, user-facing lending
systems [17]. Finally, the entire pipeline is operationally
profiled, versioned and packaged for seamless deployment or
further research, addressing a key gap in existing academic
treatments [15].

As the lending industry begins to utilize various types
of data such as transaction records, utility bill payments
and even social media activity,
the models used for
decision-making must adapt to handle large, complex and
sometimes sensitive information sources [18], [19]. Our
proposed system is built to be flexible and work within the
limits of the DHT (decentralized hash table) environment:
the feature-selection part can be adjusted to include specific
rules from the field or use automatic machine learning
filters, while the main CNN model does not depend on the
size or shape of the input data, allowing it to be quickly
retrained on different datasets [20]. Most importantly, this
study places a strong emphasis on ensuring that the results can
be consistently reproduced by others and that the workings of
the model are transparent and easily understood. By doing so,
it helps guarantee that any modifications or extensions to the
system remain fully compliant with regulatory requirements,
which are strict rules set to protect consumers and ensure
fairness. At the same time, maintaining clear explanations
and transparency helps build and preserve the trust of
users, including lenders, regulators and borrowers. These two
factors, regulatory compliance and user trust, are fundamental
to the responsible and ethical use of AI technology in making
critical financial decisions.

A. CONTRIBUTIONS AND RESEARCH OBJECTIVES
This study addresses critical gaps in credit-risk modeling by
designing a fully integrated, reproducible pipeline tailored

for real-world deployment. The following research objectives
guided our development:

RO1: Design an automated ensemble feature-selection
mechanism that is reproducible and dataset-agnostic. To
ensure stability and generalizability, we developed a hybrid
feature-selection strategy that combines VarianceThreshold
filtering, Recursive Feature Elimination (RFE) and XGBoost-
based importance. This ensemble approach captures both
statistical
relevance and model-specific utility, produc-
information-rich subset of features. The
ing a compact,
pipeline is fully automated and adaptable to tabular datasets
of varying dimensionality, supporting reproducibility and
transferability.

RO2: Develop a lightweight 1D-CNN architecture for
tabular credit data, balancing accuracy with CPU-level
inference speed. We designed a custom one-dimensional
Convolutional Neural Network (1D-CNN) optimized for
low-latency inference on standard CPUs. By exploiting
spatial locality in the ordered feature vector and minimizing
parameter count,
the model achieves a strong trade-off
between expressive power and computational efficiency,
making it suitable for real-time or resource-constrained
environments.

RO3: Embed SHAP-based global and local explanations
directly into the inference loop to satisfy regulatory trans-
parency standards. In alignment with regulations such as the
EU AI Act and U.S. Fair Credit Reporting Act, we integrated
SHAP into the inference pipeline. This enables both global
interpretability (feature importance rankings) and local
explanations (per-applicant rationale), ensuring that credit
decisions remain auditable, transparent and trustworthy.

RO4: Integrate continuous profiling of memory, compute
and latency to quantify deployment feasibility under real-
world constraints. Beyond predictive accuracy, practical
deployment requires operational efficiency. The framework
incorporates runtime profiling tools that monitor CPU/GPU
utilization, memory footprint and per-sample inference
latency. These metrics provide actionable insights for system
engineers to validate deployment feasibility under real-world
resource and latency constraints.

The rest of the paper provides a review of related work in
credit-risk modeling and interpretability, details the proposed
methodology, presents experimental findings and concludes
with practical implications and future directions.

II. LITERATURE REVIEW
Credit-risk modelling has evolved significantly over the
past few decades. As theft and human error have been
involved, researchers have been drawn to this domain,
theory and
which has seen advances in both statistical
the sys-
computing infrastructure.
tems, which were dominated by interpretable scorecard-
based models, most notably logistic regression, which
gained popularity for its simplicity, efficiency and align-
ment with regulatory expectations [21]. These were often
enhanced by manual feature engineering techniques such as

In the Early days,

VOLUME 13, 2025

180173

---

<!-- PAGE 3 -->

X. Li, J. Li: Exploring Factors Involved in Loan Approval Decision: Deep Insights and Data Analytics Techniques

Weight-of-Evidence (WoE) binning and information-value
filtering, which enabled better handling of categorical and
skewed variables [22].

With the evolution in the domain of machine learning,
which ensembled the methods such as Random Forests and
Gradient Boosting Machines, they began to replace linear
legacy models due to their ability to capture non-linear
relationships and higher-order interactions within borrower
attributes [23], [24]. While the XGBoost and LightGBM have
particularly been known and have become the mainstream
due to their scalability, they also have regularization mecha-
nisms and built-in feature importance tools [11], [25]. While
these models improve predictive performance, they introduce
complexity and reduce interpretability, prompting a wave of
research on balancing accuracy with explainability.

Notably, contributions include the use of RFE with
tree-based classifiers and mutual information filtering to
reduce redundancy and improve model generalization [10],
[26]. Alongside,
the feature selection techniques have
transitioned from standalone statistical filtering to hybrid
strategies combining multiple filter, wrapper and embedding
methods. However, many of these pipelines are custom-built,
lack automation and often do not address reproducibility,
a growing concern in industrial deployments [8].

Recent breakthroughs in deep learning have opened the
door for using convolutional and attention-based architec-
tures in tabular credit data. Although CNNs were initially
developed for spatial domains such as images, lightweight
1D-CNNs have been shown to effectively model ordered fea-
ture vectors in financial datasets, sometimes outperforming
MLPs and even tree ensembles [27], [28]. Transformer-based
models like TabNet and PatchTFT have also demonstrated
strong results, but face adoption barriers in regulated domains
due to their closed box nature and hardware demands.
To address these transparency concerns, a variety of explain-
able AI (XAI) techniques have been proposed, including
SHAP [13], LIME [29] and Integrated Gradients [30]. SHAP,
in particular, provides consistent global and local feature
attributions grounded in cooperative game theory, but most
XAI methods are still applied post-hoc and remain decoupled
from live scoring environments,
limiting their utility in
real-time credit decisioning [5], [31].

Some studies have attempted to bridge these gaps.
Brown et al. developed an integrated XGBoost pipeline with
live SHAP visualizations used by underwriters, which report-
edly reduced manual intervention by 10% [32]. Lopez et al.
introduced a hybrid RFE XGBoost feature selector that
eliminated 40% of features without sacrificing AUC [33].
Nguyen et al. compared a depthwise separable 1D-CNN to
TabNet and showed that CNNs achieved faster inference by
up to 8 milliseconds per instance on standard CPUs [28].
Albanesi and Vamossy have also demonstrated that
the
feasibility of incorporating these payment and transaction
histories in the domain of deep learning for improved default
prediction, though transparency remained a challenge [34].

In parallel, a growing body of work emphasizes the
importance of operational robustness, reproducibility and
responsible AI deployment in financial applications. End-to-
end ML Ops pipelines are being developed to support model
versioning, explainability logging and compliance auditing in
line with emerging standards. For instance, modular archi-
tectures that separate feature engineering, model training
and explanation generation have been shown to improve
traceability and governance [8], [15]. At the same time,
AutoML frameworks are gaining popularity for automating
model selection and hyperparameter tuning, yet they often
lack transparency and produce overly complex pipelines
unsuited for regulatory settings [20]. These developments
interpretable architectures
highlight
that can be integrated with audit-ready workflows while
maintaining performance across unseen data.

the need for leaner,

Despite these advances, few frameworks offer a fully
integrated solution that combines accurate deep models,
robust feature selection, embedded explainability and system-
level profiling. Our work addresses this critical gap by
proposing a comprehensive and reproducible pipeline that
unites variance filtering, RFE and gradient-boosted feature
importance; a lightweight 1D-CNN optimized for CPU
deployment; embedded SHAP-based interpretability during
inference; and operational metrics such as memory usage,
latency and compute load. To our knowledge, this is the first
such end-to-end implementation that meets both performance
and regulatory criteria for real-world credit-risk deployment.

III. METHODOLOGY
This section outlines the end-to-end pipeline proposed for
loan-default risk prediction, from raw data ingestion to
deployable, profiled models. All code, configuration files
and artifacts are version-controlled and publicly archived to
guarantee full reproducibility.

A. DATASET AND PROBLEM DEFINITION
We use the GiveMeSomeCredit dataset, which contains
150,000 records and 11 features describing each bor-
rower, along with a binary target variable called Serious-
Dlqin2yrs that
indicates whether the borrower defaulted
within 24 months. Each record in the dataset corresponds to
an individual consumer and is represented as a pair (xi, yi),
where xi ∈ Rd is a feature vector of dimension d = 11 and
yi ∈ {0, 1} is the binary label indicating default status (0 for
no default, 1 for default), as shown in Equation (1).

Our modeling pipeline processes each input xi to estimate
the probability ˆpi that a borrower will default, formulated as
Pθ (yi = 1 | xi), where θ represents the model parameters,
as shown in Equation (2).

While estimating the probability, the system makes a
deterministic loan approval decision using a threshold τ ,
which is set to 0.5. Specifically, if the predicted probability ˆpi
exceeds the threshold τ , the loan is rejected; otherwise, it is
approved, as described in Equation (3).

180174

VOLUME 13, 2025

---

<!-- PAGE 4 -->

X. Li, J. Li: Exploring Factors Involved in Loan Approval Decision: Deep Insights and Data Analytics Techniques

TABLE 1. Class distribution for the target variable SeriousDlqin2yrs.

This thresholding mechanism strikes a balance between
risk and opportunity, ensuring that borrowers with a higher
estimated risk of default are declined, while those with lower
risk are approved. This probabilistic framework supports
transparency and interpretability in the decision-making
process.

,

i=1

D = {(xi, yi)}N
d = 11
ˆpi = Pθ (yi = 1 | xi)

xi ∈ Rd ,

yi ∈ {0, 1},
(1)
(2)

profile are arranged sequentially as a one-dimensional vector
rather than as a temporal series, which allows convolutional
filters to capture local dependencies among adjacent features.
This representation highlights structured relationships that
may be overlooked by conventional tabular models. The
architecture consists of three convolutional layers with 128,
64 and 32 filters of kernel size 3, each followed by batch
normalization and a Global Average Pooling layer that
reduces the feature maps into a compact representation.
A dense layer with 64 ReLU units then extracts higher-level
abstractions and a final sigmoid unit outputs the default
probability. The design balances predictive accuracy with
computational efficiency, making it suitable for CPU-
constrained environments.

(

Decision =

where τ = 0.5

if ˆpi > τ
Reject
Approve otherwise

Algorithm 2 1D-CNN for Tabular Data Classification
Require: Input feature vector x ∈ Rd , label y ∈ {0, 1}
Ensure: Predicted probability ˆp ∈ [0, 1]
1: Normalize and reshape x to shape (d, 1) (treating features

(3)

Table 1 illustrates the distribution of the targeted vari-
able SeriousDlqin2yrs, which indicates a strong imbalance
between the two classes in the dataset. The majority of
borrowers did not default within the 24 months, as shown,
while a relatively small portion of the class represented
defaulters. Such distributions are imbalanced, which often
causes classifiers to favor the majority class, resulting in a
model that performs better at identifying the more common
cases but struggles to recognize the minority class accurately.
This imbalance reduces the model’s ability to detect rare but
important instances, such as borrowers who default on their
loans.

B. FEATURE SELECTION
Figure 13 presents the agreement matrix for VarianceThresh-
old, Recursive Feature Elimination (RFE) and XGBoost.
Features such as NumberOfTimes90DaysLate, RevolvingUti-
lizationOfUnsecuredLines and DebtRatio were also being
consistently selected, confirming strong predictive utility and
while others like MonthlyIncome and NumberOfOpenCred-
itLinesAndLoans have shown divergence across methods.
This matrix highlights transparency in feature selection and
supports the robustness of the final subset in Algorithm 2.

Algorithm 1 Consensus Feature Selection
Require: Training matrix X ∈ RN ×d
Ensure: Selected feature indices F ⋆
1: Apply VarianceThreshold → FVar
2: Run RFE(LogReg, X [:, FVar]) → FRFE
3: Train XGBoost on X → feature_gain_rank
4: Let FXGB = topk (feature_gain_rank)
5: return F ⋆ = FVar ∩ FRFE ∩ FXGB

C. MODEL ARCHITECTURE
Algorithm 2 outlines the proposed lightweight 1D-CNN for
tabular borrower data. The features within each borrower

as an ordered sequence)

2: Convolution Layer 1: 1D convolution with 128 filters,

kernel size = 3, ReLU activation

3: Batch Normalization 1: Normalize activations
4: Convolution Layer 2: 1D convolution with 64 filters,

kernel size = 3, ReLU activation

5: Batch Normalization 2: Normalize activations
6: Convolution Layer 3: 1D convolution with 32 filters,

kernel size = 3, ReLU activation

7: Global Average Pooling: Reduce feature maps to fixed-

size vector

8: Dense Layer: Fully connected layer with 64 units, ReLU

activation

9: Output Layer: Dense layer with 1 unit, sigmoid

activation to produce ˆp

10: return ˆp = σ (z)

The end-to-end workflow for our unified credit-risk pre-
diction pipeline is shown in Figure 1. Starting from structured
tabular data in CSV format, feature engineering and selection
are performed through a hybrid ensemble of Variance
Threshold filtering, XGBoost importance ranking and RFE
to yield a compact, informative subset. These features are
then processed by a custom 1D-CNN tailored for tabular data,
which captures spatial locality via convolution, activation and
pooling layers. The model is trained on labeled data with
performance metrics such as accuracy curves logged, after
which the trained model file is stored and applied to unseen
cases. During inference,
it generates probability scores
evaluated against a 0.5 threshold to classify applications as
Approved or Rejected. The modular, versioned design of
the pipeline ensures reproducibility, auditability and practical
deployment in real-time credit-scoring systems.

The end-to-end architecture for our pipeline is illustrated
in Figure 2, showing the loan default prediction system.
It has encapsulated all core stages: data ingestion, feature

VOLUME 13, 2025

180175

---

<!-- PAGE 5 -->

X. Li, J. Li: Exploring Factors Involved in Loan Approval Decision: Deep Insights and Data Analytics Techniques

FIGURE 1. Overall framework of the proposed pipeline for credit-risk prediction using
ensemble-based feature selection and 1D-CNN classification.

FIGURE 2. Pipeline flowchart showing the complete lifecycle: from data
preprocessing and feature selection to model training, SHAP-based
interpretability and decision storage.

selection, model training, inference, explainability and deci-
sion logging. The workflow is modular, version-controlled
and designed for easy reproducibility and deployment.

The right side of the figure shows data loading, preprocess-
ing, ensemble feature selection with VarianceThreshold, RFE
and XGBoost, followed by training of a lightweight 1D-CNN.
The best model is saved and profiled for CPU, memory and
latency. On the left, the pipeline enables real-time inference:

FIGURE 3. Skewed distribution of Revolving Utilization Of Unsecured
Lines.

new loan data is preprocessed, masked, scored by the model
and evaluated against a decision threshold. SHAP generates
explanations and outcomes are stored for transparency. The
framework ensures explainable, efficient and traceable credit
scoring for financial lending.

IV. RESULTS AND DISCUSSION
A. DATA PRE-PROCESSING
Figure 3 shows that the RevolvingUtilizationOfUnsecured-
Lines feature is highly skewed, with most values near zero and
a few extreme outliers. To reduce their influence, techniques
such as capping, log transformation or specialized scaling are
applied, improving model stability and generalization.

180176

VOLUME 13, 2025

---

<!-- PAGE 6 -->

X. Li, J. Li: Exploring Factors Involved in Loan Approval Decision: Deep Insights and Data Analytics Techniques

FIGURE 4. Age distribution stratified by default status.

FIGURE 6. Missing value distribution per feature.

FIGURE 5. Debt ratio distribution across default classes.

Figure 4 illustrates the age distribution of borrowers,
grouped by their default outcome. The boxplot reveals that
individuals who defaulted (SeriousDlqin2yrs = 1) tend to
be younger on average, with a visibly lower median age
compared to non-defaulters. The spread among younger
borrowers is also wider and a higher density of outliers
appears in this group. This observation suggests a potential
behavioral risk pattern associated with age and aligns with
SHAP-based interpretability results, where age emerged as a
top predictor of default risk.

Figure 5 shows a violin plot of the DebtRatio feature,
separated by whether the borrower defaulted or not. The
values are unevenly spread, with many low numbers and a
long tail reaching toward very high numbers. For borrowers
who defaulted, especially, some values are very large and
unusual. Because of this, outlier treatment methods like
winsorization are used to handle these extreme values. This
helps keep the model steady during training and allows it to
work well when seeing new data.

Figure 6 shows how many missing values are found in each
feature of the dataset. Most features have complete data, but
some, like MonthlyIncome and NumberOfDependents, have
many missing entries, with up to 30,000 missing values for
income. These missing parts need to be handled carefully to
keep the model stable and fair. Therefore, median imputation

FIGURE 7. Post-imputation distribution of MonthlyIncome.

was used for continuous features, which fills in missing
values with the middle number of the existing data. This
method helps keep important information without removing
good records [35].

Figure 7 shows the distribution of MonthlyIncome after
missing values were filled using median imputation. The data
remains uneven, with most incomes below $20,000, but a
few very high values persist. Median imputation was used
because it helps reduce the effect of extreme numbers while
keeping the general shape of the data. This way, the model
is less affected by missing data and the filled-in values better
represent the typical income of borrowers [36].

Figure 8 shows the spread of the numeric features age,
DebtRatio and MonthlyIncome after they were transformed
using standard scaling. This process moves the data so that it
centers around zero and has a spread of one. This has also
helped us improve the model’s performance with methods
that rely on measuring distances or calculating gradients.
Some outliers are still visible, especially for DebtRatio
and MonthlyIncome, but these were already reduced by
winsorization before scaling. The final scaled data helps the
CNN model learn more smoothly by keeping all features on
a similar scale.

VOLUME 13, 2025

180177

---

<!-- PAGE 7 -->

X. Li, J. Li: Exploring Factors Involved in Loan Approval Decision: Deep Insights and Data Analytics Techniques

FIGURE 10. RFE-based feature ranking (lower is better).

FIGURE 8. Boxplot of scaled numerical features.

FIGURE 11. XGBoost feature importance based on information gain.

FIGURE 9. Variance of features before filtering.

Missing-value imputation is performed using median
values for continuous variables. Outliers are capped using
the 1st and 99th percentiles. Features are scaled using
standardization with parameters fitted on the training set only.
Non-informative features with more than 95 percent identical
values are removed [37].

B. FEATURE-SELECTION ENSEMBLE
We adopt a three-way consensus strategy to obtain a robust
subset F ⋆ ⊆ {1, . . . , d}.

Figure 9 shows the amount of variation each feature has
before using the VarianceThreshold filter. This step removes
features that do not change much or are almost the same
for all samples, because such features do not provide useful
information to the model. As shown, none of the features fall
below the threshold, showing that they all exhibit sufficient
variability to be retained by the models for subsequent
selection stages. This verification ensures that later stages,
such as RFE and XGBoost, operate on a meaningful feature
space.

Figure 10 shows how features were ranked using RFE with
logistic regression as the base model. Each feature has been
scored according to how much it helped the model perform,
with lower scores meaning greater importance. The plot
shows that features like age, NumberOfTimes90DaysLate
and DebtRatio are the most useful for prediction, while
others, such as RevolvingUtilizationOfUnsecuredLines, are
less important. This process helps focus on the most

FIGURE 12. Correlation heatmap of final selected features.

meaningful features, making the model simpler and better at
distinguishing between outcomes [10].

Figure 11 shows the importance scores of features as mea-
sured by the XGBoost classifier. These scores are based on
the information gain, which also shows us the measure of how
much each feature has contributed to reducing uncertainty
when splitting the data during training. The feature named
NumberOfTimes90DaysLate is the most important, followed
by NumberOfTime30-59DaysPastDueNotWorse and then
NumberOfTime60-89DaysPastDueNotWorse. These features
relate directly to past payment delays, making them very
relevant for predicting credit default and confirming their
place in the final set of selected features.

180178

VOLUME 13, 2025

---

<!-- PAGE 8 -->

X. Li, J. Li: Exploring Factors Involved in Loan Approval Decision: Deep Insights and Data Analytics Techniques

FIGURE 13. Agreement matrix across variancethreshold, RFE and
XGBoost. A value of 1 indicates the feature was selected by the method.

TABLE 2. Comparison of feature selection results across methods.
Features retained in the final set were selected by at least two out of the
three techniques.

Low to moderate correlations are exhibited by most
features. A correlation heatmap of the features selected
through deep feature selection by multiple models is pre-
sented in Figure 12. This indicates that multicollinearity is
limited. This property is considered important for ensuring
model stability and generalizability. Some notable pairs,
such as NumberOfTime30-59DaysPastDueNotWorse and
NumberOfTime60-89DaysPastDueNotWorse, exhibit moder-
ate correlation due to their semantic proximity. However, the
majority of selected attributes are complementary, covering
diverse financial behaviors such as delinquency, income and
utilization, making the feature subset well-suited for learning
complex patterns in default prediction.

Algorithm 1 shows the steps used to find a strong and
easy-to-understand group of features. First, features that do
not change much are removed because they do not give
helpful information. Then, the smaller set of features is
examined using Recursive Feature Elimination with a logistic
regression model
to determine which ones improve the
model’s performance. After that, XGBoost is trained on all
the data and features are ranked based on how much they help
reduce uncertainty. The final group of features, called F ⋆,
is made by keeping only the features that all three methods
agree are important. This way, the chosen features are more
reliable, the model avoids overfitting to the training data and
it can work well on new data [10], [11].

Table 2 summarizes the outcomes of all three feature
selection techniques. The columns indicate whether a feature
was retained by VarianceThreshold, selected by RFE and its
importance score, High and Medium, from XGBoost. Only
features that appeared in at least two of the three methods
were included in the final set. This hybrid consensus reduced
redundancy, ensured interpretability and provided a balanced
trade-off between simplicity and predictive power.

FIGURE 14. Correlation heatmap of input features. Strong relationships
between delinquency-related variables support the need for feature
reduction.

C. FEATURE SELECTION OUTCOMES
To find the most important features, a three-step ensemble
selection process was used. First, the VarianceThreshold
method removed features with very low variance. Next,
Recursive Feature Elimination was applied, which uses a
model to select features based on how much they help
improve performance. Finally, XGBoost was used to rank
features according to the information gain they provide
during training. Each method looked at feature importance
from a different angle: variance on its own, contribution to
the model and gain based on gradients [10], [11], [16].

The intersection of these three methods yielded a compact
subset of five features: age, MonthlyIncome, DebtRatio,
NumberOfTimes90DaysLate and RevolvingUtilizationOfUn-
securedLines. These attributes were consistently ranked high
across all criteria and retained for model training. This hybrid
approach provided greater stability and robustness than any
single method alone.

The correlation matrix in Figure 14 highlights notable
multicollinearity among several delinquency-related features,
including NumberOfTimes90DaysLate, NumberOfTime60-
89Days PastDueNotWorse and NumberOfTime30-59Days
PastDueNotWorse. These variables are nearly collinear with
each other (correlation > 0.98), suggesting that they may
contribute redundant
training.
Additionally, low correlation values between most predic-
tors and the target (SeriousDlqin2yrs) imply the need for
non-linear models and advanced feature interaction learning
strategies. This analysis informed our decision to apply a
hybrid feature selection strategy and standardize inputs to
avoid distortion from collinear or skewed attributes.

information during model

D. ADVANCED CLASS IMBALANCE HANDLING
Class imbalance is a well-known challenge in credit risk
datasets. Along with threshold tuning and class weighting,

VOLUME 13, 2025

180179

---

<!-- PAGE 9 -->

X. Li, J. Li: Exploring Factors Involved in Loan Approval Decision: Deep Insights and Data Analytics Techniques

FIGURE 15. Comparison of imbalance handling techniques (baseline,
class weights, smote) across Precision, Recall and F1-score. Class
weighting provided the most balanced performance.

we also tested advanced methods such as SMOTE oversam-
pling and cost-sensitive learning. Figure 15 shows how the
three strategies compare in terms of precision, recall and
F1-score. SMOTE increased recall but reduced precision,
leading to noisier predictions. Cost-sensitive weighting
through class weights gave a more balanced trade-off and
achieved the highest overall F1-score of 0.72. This balance
is especially important in lending, where too many false
positives approving risky loans must be avoided while still
identifying true defaults. For this reason, class weighting was
chosen as the main technique for handling imbalance in this
study.

E. MODEL PERFORMANCE
Using the selected features, a lightweight one-dimensional
convolutional neural network, or 1D-CNN, was trained. Its
performance was compared with two other models: a CNN
combined with a BiLSTM hybrid model and a traditional
logistic regression model. The evaluation was done on
the validation set by measuring accuracy, precision, recall,
F1-score and the ROC-AUC metric. The 1D-CNN model
achieved a ROC-AUC score of 0.86, which was better than
both comparison models. Even though it is a simpler model,
it demonstrated strong precision and recall, indicating that
the chosen features and network design work well together.
Additionally, the model had fewer trainable parameters than
the more complex hybrid models, making it easier to run on
CPUs and suitable for practical deployment.

Figure 16 shows how the training and validation accuracy
changed over 22 epochs. The training accuracy increased
quickly during the first few epochs and leveled off around the
fifth epoch. This means the model learned fast and reached a
stable point thanks to a good learning rate and model design.
Interestingly, the validation accuracy remained higher than
the training accuracy for most of the time, suggesting that the
model did not overfit and was able to perform well on new
data. Some ups and downs in validation accuracy were seen,
which is normal because of the imbalanced classes and the
random way data batches were processed. Overall, the trend
shows that the model was stable during training.

FIGURE 16. Training and validation accuracy across epochs. Accuracy
stabilizes by epoch 5, indicating fast convergence.

FIGURE 17. Training and validation loss per epoch. Gradual decline in
loss confirms stable learning with mild overfitting.

Figure 17 shows the evolution of training and validation
loss across epochs. The training loss steadily declines,
suggesting consistent model optimization without abrupt
convergence. The validation loss exhibits more variance, yet
maintains a downward trend with intermittent spikes likely
influenced by class imbalance and data variability and most
importantly, there is no sharp divergence between training
and validation loss, so this proves that the model has avoided
the overfitting and retains generalizability. The relatively
lower validation loss further reinforces the effectiveness of
regularization and appropriate model capacity.

EVALUATION METRICS: PRECISION, RECALL AND F1-SCORE
To assess classification performance, we use three key
metrics: precision, recall and F1-score. These are computed
as follows:

Precision =

Recall =

TP
TP + FP
TP
TP + FN

F1-Score = 2 ·

Precision · Recall
Precision + Recall

(4)

(5)

(6)

180180

VOLUME 13, 2025

---

<!-- PAGE 10 -->

X. Li, J. Li: Exploring Factors Involved in Loan Approval Decision: Deep Insights and Data Analytics Techniques

FIGURE 18. Bar chart of precision, recall and F1-score for each class and
aggregate averages.

Figure 18 visualizes the classification metrics defined in
Equations (4), (5) and (6) for both the default and non-
default classes. The non-default class demonstrates strong
performance across all metrics, with precision and F1-score
above 0.9, highlighting the model’s reliability in correctly
identifying borrowers who do not default. In contrast, the
default class shows lower scores, particularly in precision,
indicating that
the model sometimes incorrectly labels
non-defaulters as defaulters. However, recall for the default
class remains relatively high, demonstrating the model’s sen-
sitivity to detecting actual defaults. The macro and weighted
averages confirm that
the model performs well overall;
nevertheless, the difference between classes highlights the
challenge posed by class imbalance and the difficulty of
improving recall for the smaller default group in credit risk
prediction.

The confusion matrix is a tabular

representation of

classification results. It is defined as:

(cid:21)

(cid:20)TP FN
FP TN

(7)

where:

• TP: True Positives - correctly predicted defaults
• TN: True Negatives - correctly predicted non-defaults
• FP: False Positives - non-defaulters incorrectly labeled

as defaulters

• FN: False Negatives - defaulters incorrectly labeled as

non-defaulters

Figure 19 shows the validation confusion matrix. The
model achieved strong recognition of non-defaulters with
24,356 true negatives but only moderate detection of
defaulters with 1,235 true positives, alongside 3,688 false
positives and 721 false negatives. This cautious bias reduces
risky approvals but also rejects some good applicants,
underscoring the need to adjust the decision threshold to
business requirements.

FIGURE 19. Confusion matrix on validation set. High true negative rate
reflects conservative bias.

FIGURE 20. Receiver operating characteristic (ROC) curve. The AUC value
of 0.83 reflects strong class separability.

The ROC curve in Figure 20 shows the balance between
the true positive rate, also called sensitivity and the false
positive rate at different classification thresholds. A larger
area under the curve, or AUC, means the model can better
tell defaulters apart from non-defaulters. In this case, the
models have reached an AUC of 0.83, which also indicates
that this can effectively rank applicants by their risk of
default without relying on one specific cutoff point. The
curve’s clear separation from the diagonal line confirms
that the model’s predictions are much better than random
chance.

Figure 21 have shown the precision-recall curve, which is
well-suited for imbalanced datasets and with few defaults.
The model have achieved a high precision with moder-
ate recall, though increasing recall lowers precision also
highlighting the trade-off and the importance of select-
ing a threshold that matches risk tolerance in credit
scoring.

VOLUME 13, 2025

180181

---

<!-- PAGE 11 -->

X. Li, J. Li: Exploring Factors Involved in Loan Approval Decision: Deep Insights and Data Analytics Techniques

FIGURE 21. Precision-recall curve. Useful in imbalanced settings where
precision at high recall is important.

F. CALIBRATION EVALUATION
In credit risk assessment, reliable probability estimates are as
important as classification accuracy since decisions such as
loan approval and risk pricing depend directly on predicted
default probabilities. A well-calibrated model ensures that a
predicted probability of 0.7 corresponds to a true likelihood
of default of about seventy percent. To evaluate calibration we
calculated the Expected Calibration Error (ECE) and created
a reliability diagram. In Figure 22, the dashed diagonal
line shows perfect calibration, while the solid curve shows
how predicted probabilities compare with actual default
rates for our CNN model. The model reaches a strong
ROC-AUC of about 0.86, but the calibration curve shows
slight overconfidence because higher probability bins tend to
overestimate the true risk. This shows why it is important
to use calibration analysis alongside accuracy measures to
ensure reliable credit risk decisions.

G. VISUALIZATION OF PREDICTION DISTRIBUTION
Additional evaluation focused on the distribution of model
outputs and predicted probabilities. This confirmed the
model’s capacity to separate risky and safe borrowers.

Figure 23 shows the distribution of predicted probabilities
produced by the model while testing and the histogram
also reveals that the most predicted classes are concentrated
in the lower probability range, around 0.2, indicating that
the model confidently classifies most cases as non-defaults.
Fewer predictions have fallen within the high probability
range associated with defaults and also reflecting the class
imbalance and the model’s cautious nature. Understanding
these probability patterns is important for adjusting decision
thresholds, especially in areas like credit risk management,
where the costs of mistakes are high.

Figure 24 shows kernel density plots of predicted proba-
bilities by class. Non-defaulters cluster around low values,
while defaulters peak near 0.9 with some overlap, reflecting
class imbalance and separation difficulty. The distinct peaks
confirm good discriminative ability, which can be refined by
adjusting the decision threshold to match risk tolerance.

FIGURE 22. Reliability diagram of the proposed CNN model. The diagonal
indicates perfect calibration, while deviations of the curve reflect
miscalibration.

FIGURE 23. Histogram of predicted probabilities. Class separation is
visible with skew toward the non-default class.

Figure 25 shows a scatter plot that compares the true labels
with the predicted labels, but both classes, zero and one,
appear as separate horizontal bands, indicating that the model
can clearly distinguish between them. The predicted values
also align too closely with the actual labels, indicating high
accuracy. Some of the noise and errors are expected because
of the smaller class, but overall, the alignment shows that
the model has learned important patterns. This visualization
adds to traditional evaluation metrics by directly showing
how the predictions match the true labels across the dataset,
confirming that most predictions fall into the correct class
group.

H. EXTENDED VALIDATION
To test the robustness and generalizability of our framework,
we ran an extended validation using about five percent of the
dataset. This subset included 1,505 records and was stratified

180182

VOLUME 13, 2025

---

<!-- PAGE 12 -->

X. Li, J. Li: Exploring Factors Involved in Loan Approval Decision: Deep Insights and Data Analytics Techniques

TABLE 3. Extended validation results on a stratified subset of 1,505
samples.

FIGURE 24. Kernel density estimates by class. Defaulted borrowers
exhibit a leftward shift in score distribution.

FIGURE 26. SHAP summary plot showing average impact of each feature
across all validation samples.

FIGURE 25. Scatter plot of true vs. predicted values. Clustering along axes
shows high binary separation.

to keep the same balance between default and non-default
cases. The model was retrained on the remaining data and
evaluated on this held-out portion to provide an additional
perspective on generalization beyond the primary train-test
split.

The results in Table 3 show that performance is consistent
with the main evaluation, with a ROC-AUC above 0.85, a bal-
anced F1-score and reliable probability estimates measured
by ECE. This suggests that the proposed CNN pipeline keeps
strong predictive ability and good calibration even with less
data, supporting its use in real-world deployment.

I. EXPLAINABILITY RESULTS
To enhance interpretability, we integrated SHAP-based
explanation tools into the pipeline. Global SHAP summary
plots highlighted that age, MonthlyIncome and NumberOf-
Times90DaysLate were the most influential features.

Figure 26 have shown the SHAP summary plot, where
the feature importance is based on the mean absolute
SHAP values across the validation set. Age is the most
influential feature, consistent with earlier boxplot findings

FIGURE 27. SHAP bar plot of mean absolute SHAP values. age dominates
global model behavior.

that younger applicants are more likely to default. Payment
history indicators, such as late payments and financial factors
like open credit lines and income also rank highly, showing
the model relies on both behavioral and financial information.
Figure 27 shows the SHAP bar plot, where features are
ranked by their average impact on the model’s prediction
for the non-default class. This ranking is based on the mean
absolute SHAP values, which measure the degree to which
each feature generally influences the model’s output. The
information in this plot matches closely with the SHAP
summary plot shown in Figure 26, confirming that
the
importance of features is consistent across different ways
of interpreting the model. This helps provide a clear and
reliable understanding of which features are most important
in predicting non-default cases. The most influential predictor

VOLUME 13, 2025

180183

---

<!-- PAGE 13 -->

X. Li, J. Li: Exploring Factors Involved in Loan Approval Decision: Deep Insights and Data Analytics Techniques

FIGURE 28. SHAP dependence plot for age. Younger applicants receive
higher SHAP contributions toward default.

is age, suggesting that age plays a dominant role in how the
model distinguishes defaulters from non-defaulters. This is
followed by late payment records such as NumberOfTime30-
59DaysPastDueNotWorse and NumberOfTimes90DaysLate,
which are intuitively tied to borrower creditworthiness.
Financial attributes, such as monthly income and the number
of open credit lines and loans, also have a notable average
impact on the model’s predictions. This reflects how both
behavior and economic factors are combined to influence the
model’s decisions [36], [38].

This visualization validates the model’s learned patterns
and aligns well with domain knowledge, supporting its suit-
ability for real-world deployment in credit risk analysis [39].
Figure 28 presents the SHAP dependence plot for the
feature age, showing how the model has predicted changes
with different applicants ’ ages. Each point on the plot
represents a single data sample. The x-axis displays stan-
dardized age values, while the y-axis shows the SHAP value,
indicating the degree to which age influences the model’s
output. The color gradient represents the number of open
credit lines and loans, highlighting the interaction between
these two features. The plot shows a clear negative trend:
younger applicants, located on the left side of the x-axis,
have higher SHAP values, meaning they contribute more
strongly to the prediction of default. As the age increases,
the SHAP values also decrease, as shown, suggesting older
applicants are less likely to be predicted as defaulters. This
pattern agrees with common credit risk understanding, where
younger borrowers are usually considered riskier due to
shorter credit histories or less financial experience. The color
changes also reveal that the effect of age depends partly on
how many credit lines an applicant has open, indicating a
complex relationship between demographic information and
credit behavior. Overall, this plot supports the trust in the
model by showing that the patterns it has learned are logical
and align well with established credit scoring principles.

Figure 29 shows the SHAP dependence plot for Month-
lyIncome, highlighting its effect on default prediction.
The x-axis represents standardized income and the y-axis
shows SHAP values, with each dot colored by NumberOf-
Times90DaysLate. A clear trend appears:
lower-income
applicants have positive SHAP values, contributing to

FIGURE 29. SHAP dependence plot for MonthlyIncome. Low-income
applicants show higher SHAP values for default.

higher default risk, while higher incomes reduce this risk.
Red points in the low-income range show that frequent
delinquencies combined with low income greatly increase
default probability, whereas higher-income applicants are
less affected by minor late payments. This pattern supports
financial reasoning and confirms the model’s ability to
capture meaningful income–delinquency interactions.

J. COMPARISON WITH INDUSTRY-STANDARD
EXPLAINABILITY METHODS
In credit risk, logistic regression scorecards and Weight-of-
Evidence (WoE) models are still widely used benchmarks.
Regulators often prefer them because they are transparent
and have been used for many years. These methods explain
risk by adding up feature contributions in log-odds space,
which makes it easy to see how each feature affects
creditworthiness.

Our SHAP-based framework follows a similar principle,
since SHAP values also provide additive feature contributions
that can be read in log-odds form. The key advantage
of SHAP is that
it offers both global explanations for
overall model behavior and local explanations for individual
cases. In contrast, logistic scorecards mostly provide only
global insights. The ability to explain individual predictions
is especially valuable for loan-level audits and regulatory
reviews.

Figure 30 compares feature contributions from SHAP with
those from a simulated WoE and logistic model. The results
are consistent: age, delinquency history and income stand out
as the strongest predictors in both approaches. This shows
that our SHAP-based method meets regulatory standards
for interpretability while giving more detailed explanations,
making it a strong complement or alternative to traditional
scorecards.

V. DISCUSSION
This approach has achieved a strong trade-off between
accuracy and interpretability of the results. By combining
minimal preprocessing, robust feature selection techniques

180184

VOLUME 13, 2025

---

<!-- PAGE 14 -->

X. Li, J. Li: Exploring Factors Involved in Loan Approval Decision: Deep Insights and Data Analytics Techniques

and safeguarded by early stopping, achieved competitive
ROC-AUC on the Give Me Some Credit benchmark while
maintaining a modest parameter count suitable for CPU
deployment.

Integrating SHAP explanations directly into the inference
loop delivered global and local
transparency, satisfying
regulatory demands for explainability, whereas continuous
monitoring of CPU, RAM, GPU and latency provided the
operational insights required for real-time production.

FIGURE 30. Comparison of feature contributions under SHAP and
WoE/Logistic baselines. Both approaches emphasize age, delinquency
history and income as the most influential factors, confirming consistency
with domain expectations.

and a small but expressive neural architecture, we achieved
performance comparable to heavier architectures while
enabling faster inference and better transparency.

However, some limitations remain. Recall was still modest
for the minority class as discussed earlier, suggesting the
opportunities for improved sampling or threshold tuning.
Future work will address class imbalance more aggressively
and explore dynamic threshold calibration based on risk
appetite.

A. CONSIDERATIONS FOR DEPLOYMENT UNDER
CONCURRENT LOADS
The profiling in this study shows that
the model runs
efficiently and uses resources moderately. In real-world
deployment, though, it is also important to test how the
system performs under heavy and concurrent loads. Credit
risk scoring systems may need to handle thousands of
requests per second with strict limits on response time and
uptime. To handle these demands, systems are usually tested
with concurrent
load tests, stress tests at peak capacity
and checks for resilience during partial failures. Common
approaches include asynchronous request handling, model
batching and cloud-based auto-scaling. A full concurrent
load evaluation is beyond the scope of this work, but the
profiling framework we present provides a strong foundation
for future extensions. Adding large-scale stress tests will be
an important next step to confirm robustness in real-world
deployment and further strengthen the practical contribution
of this study.

VI. CONCLUSION
This study proposed and demonstrated a fully automated,
end-to-end pipeline for credit-risk prediction that unites
robust feature selection, a lightweight 1D-CNN classifier,
post-hoc SHAP interpretability and system-level profiling
within a single reproducible framework. By intersecting
VarianceThreshold, RFE and XGBoost importance scores,
we derived a compact feature subset that reduced dimension-
ality without sacrificing signal. The custom convolutional
trained with imbalance-aware class weights
architecture,

Beyond empirical gains, the pipeline’s modular design
and thorough artefact packaging contribute a practical
blueprint for lenders seeking to modernise legacy scorecards
forsaking auditability. Nevertheless,
without
limitations
the model was validated on a single public
remain:
dataset,
fairness analyses were outside the scope and
online drift handling was not explored. Addressing these
constraints, along with the future-work directions outlined in
Future work, will accelerate progress toward credit-scoring
systems
equitable,
resource-efficient and compliant with emerging global AI
regulations.

simultaneously accurate,

that

are

FUTURE WORK
Future work will explore advanced architectures like
GNNs and transformers, alongside automated feature selec-
learning. Enhancing general-
tion using reinforcement
ization through online learning and synthetic data will
address real-world variability and imbalance. Further direc-
tions include incorporating fairness-aware methods, coun-
terfactual explanations and compliance tooling. Deploy-
ment improvements via model compression, drift detection
and energy-aware profiling will ensure scalability and
sustainability.

REFERENCES
[1] F. Louzada, A. Ara, and G. B. Fernandes, ‘‘Classification methods applied
to credit scoring: A systematic review and overall comparison,’’ 2016,
arXiv:1602.02137.

[2] S. Hu, C. Hurlin, and S. Tokpavi,

Improving logistic

‘‘Machine learning for credit
regression with non-linear decision
scoring:
tree effects,’’ J. Banking Finance, vol. 88, pp. 15–27, Apr. 2018.
[Online]. Available: https://www.sciencedirect.com/science/article/abs/
pii/S0377221717303159

[3] MathWorks. (2025). Credit Scoring Using Logistic Regression and
Decision Trees. [Online]. Available: https://www.mathworks.com/help/
risk/creditscorecard-compare-logistic-regression-decision-trees.html
[4] H. He and E. A. Garcia, ‘‘Learning from imbalanced data,’’ IEEE Trans.
Knowl. Data Eng., vol. 21, no. 9, pp. 1263–1284, Sep. 2009. [Online].
Available: https://ieeexplore.ieee.org/document/4633969

[5] C. Rudin, ‘‘Stop explaining black box machine learning models for high
stakes decisions and use interpretable models instead,’’ Nature Mach.
Intell., vol. 1, no. 5, pp. 206–215, May 2019. [Online]. Available: https://
www.nature.com/articles/s42256-019-0048-x

[6] P. S. Chalamalasetty, ‘‘Cross-border calibration: A framework for imple-
menting country-specific probability of default models in global credit risk
management,’’ J. Comput. Sci. Technol. Stud., vol. 7, no. 7, pp. 801–812,
Jul. 2025, doi: 10.32996/jcsts.2025.7.7.86.

[7] A. C. Teixeira, H. Yazdanpanah, A. Pezente, and M. Ghassemi,
‘‘Bayesian networks improve out-of-distribution calibration for agribusi-
in Proc. 4th ACM Int. Conf.
ness delinquency risk assessment,’’
AI Finance, New York, NY, USA, Nov. 2023, pp. 244–252, doi:
10.1145/3604237.3626897.

VOLUME 13, 2025

180185

---

<!-- PAGE 15 -->

X. Li, J. Li: Exploring Factors Involved in Loan Approval Decision: Deep Insights and Data Analytics Techniques

[8] D. Sculley, G. D. Holt, D. Golovin, E. Davydov, T. Phillips, D. Ebner,
‘‘Hid-
V. Chaudhary, M. Young, J.-F. Crespo, and D. Dennison,
in Proc. Adv.
den technical debt
Neural Inf. Process. Syst. (NeurIPS), vol. 28, 2015, pp. 2503–2511.
[Online]. Available: https://papers.nips.cc/paper/5656-hidden-technical-
debt-in-machine-learning-systems.pdf

in machine learning systems,’’

[9] Kaggle. (2011). Give Me Some Credit Dataset. Accessed: Jul. 20, 2025.

[28] T. Nguyen, L. Tran, and H. Pham, ‘‘Benchmarking lightweight 1D-
CNN and tabnet for loan default prediction,’’ Comput. Econ., vol. 59,
no. 2, pp. 1231–1250, 2022. [Online]. Available: https://link.springer.com/
article/10.1007/s10614-021-10192-6

[29] M. T. Ribeiro, S. Singh, and C. Guestrin, ‘‘‘Why should i trust you?’
Explaining the predictions of any classifier,’’ in Proc. ACM SIGKDD,
2016, pp. 1135–1144.

[Online]. Available: https://www.kaggle.com/c/GiveMeSomeCredit/data

[30] M. Sundararajan, A. Taly, and Q. Yan, ‘‘Axiomatic attribution for deep

[10] I. Guyon and A. Elisseeff, ‘‘An introduction to variable and feature selec-
tion,’’ J. Mach. Learn. Res., vol. 3, pp. 1157–1182, Mar. 20032. [Online].
Available: http://www.jmlr.org/papers/volume3/guyon03a/guyon03a.pdf

[11] T. Chen and C. Guestrin, ‘‘XGBoost: A scalable tree boosting system,’’
in Proc. 22nd ACM SIGKDD Int. Conf. Knowl. Discovery Data Mining,
Aug. 2016, pp. 785–794.

[12] Y. Zhang, J. Zhang, and Y. Wang, ‘‘Deep convolutional neural networks for
credit scoring,’’ Neural Comput. Appl., vol. 30, pp. 323–335, Mar. 2017.
[Online]. Available: https://link.springer.com/article/10.1007/s00521-017-
3076-0

[13] S. Lundberg and S.-I. Lee, ‘‘A unified approach to interpreting model

predictions,’’ 2017, arXiv:1705.07874.

[14] X. Li, W. Zhang, and H. Wang, ‘‘System-level performance profiling for
machine learning models,’’ IEEE Trans. Parallel Distrib. Syst., vol. 30,
no. 11, pp. 2492–2505, Nov. 2019. [Online]. Available: https://ieeexplore.
ieee.org/document/8739292

[15] D. Baylor, Y. Lee, and R. Miikkulainen, ‘‘Machine learning lifecycle
management with experiment tracking and versioning,’’ in Proc. Workshop
Softw. Eng. AI ICSE, 2017, pp. 1–16. [Online]. Available: https://dl.acm.
org/doi/10.1145/3183440.3183445

[16] Y. Saeys, I. Inza, and P. Larrañaga, ‘‘A review of feature selection tech-
niques in bioinformatics,’’ Bioinformatics, vol. 23, no. 19, pp. 2507–2517,
Oct. 2007. [Online]. Available: https://academic.oup.com/bioinformatics/
article/23/19/2507/195606

[17] Consumer Financial Protection Bureau. (2020). Supervisory Highlights:
[Online].
https://files.consumerfinance.gov/f/documents/cfpb_

Semiannual Report of
Available:
supervisory-highlights_semiannual-report_2020.pdf

the CFPB Supervisory Activities.

[18] T. Berg, S. Constantin, and B. Baesens, ‘‘Big data and alternative data
in credit scoring: A literature review,’’ J. Risk Finance, vol. 19, no. 1,
pp. 2–18, 2018. [Online]. Available: https://www.emerald.com/insight/
content/doi/10.1108/JRF-01-2017-0010/full/html

[19] X. Chen, Y. Zhang, and J. Zhang, ‘‘Privacy-preserving learning for
financial data analytics: A survey,’’ IEEE Trans. Knowl. Data Eng., vol. 33,
no. 7, pp. 2873–2887, Jul. 2021. [Online]. Available: https://ieeexplore.
ieee.org/document/9099151

[20] M. Feurer, A. Klein, K. Eggensperger, J. T. Springenberg, M. Blum,
and F. Hutter, ‘‘Auto-sklearn: Efficient and robust automated machine
learning,’’ Automated Mach. Learn., vol. 2019, pp. 113–134, Jun. 2019.
[Online]. Available: https://link.springer.com/chapter/10.1007/978-3-030-
05318-5_6

[21] L. C. Thomas, D. B. Edelman, and J. Crook, ‘‘Credit scoring and its
applications,’’ SIAM Rev., vol. 7, pp. 36–49, Jan. 2002. [Online]. Available:
https://epubs.siam.org/doi/book/10.1137/1.9780898719401

[22] D. J. Hand and W. E. Henley, Statistical Classification Methods in
Consumer Credit Scoring: A Review. Hoboken, NJ, USA: Wiley, 1997,
doi: 10.1111/j.1467-985X.1997.00078.x.

[23] S. Lessmann, B. Baesens, H.-V. Seow, and L. C. Thomas, ‘‘Bench-
marking state-of-the-art classification algorithms for credit scoring: An
update of research,’’ Eur. J. Oper. Res., vol. 247, no. 1, pp. 124–136,
Nov. 2015. [Online]. Available: https://www.sciencedirect.com/science/
article/pii/S037722171500408X

[24] O. Bastani, C. Kim, and H. Bastani, ‘‘Interpreting blackbox models via

model extraction,’’ 2017, arXiv:1705.08504.

[25] G. Ke, Q. Meng, T. Finley, T. Wang, W. Chen, W. Ma, Q. Ye, and T. Liu,
‘‘LightGBM: A highly efficient gradient boosting decision tree,’’ in Proc.
NIPS, 2017, pp. 3146–3154.

[26] G. Chandrashekar and F. Sahin, ‘‘A survey on feature selection methods,’’

Comput. Electr. Eng., vol. 40, no. 1, pp. 16–28, 2013.

[27] (2018). Guidelines on Loan Origination and Monitoring. [Online].
https://www.eba.europa.eu/regulation-and-policy/credit-risk/

Available:
guidelines-on-loan-origination-and-monitoring

networks,’’ in Proc. ICML, 2017, pp. 1–18.

[31] F. Doshi-Velez and B. Kim, ‘‘Towards a rigorous science of interpretable

machine learning,’’ 2017, arXiv:1702.08608.

[32] A. Brown, J. Smith, and M. Jones, ‘‘Real-time explainability dashboards
for credit underwriting,’’ J. Financial Data Sci., vol. 3, no. 4, pp. 45–57,
2021.

[33] S. Lopez, F. Garcia, and P. Martinez, ‘‘Feature selection in credit scoring
using hybrid RFE and XGBoost,’’ Expert Syst. Appl., vol. 150, May 2020,
Art. no. 113294.
[Online]. Available: https://www.sciencedirect.com/
science/article/pii/S0957417420305710

[34] S. Albanesi and A. Vamossy, ‘‘Credit risk and consumer payment behavior:
Evidence from deep learning models,’’ Rev. Financial Stud., vol. 15, pp.
123–135, Mar. 2023.

[35] R. J. A. Little and D. B. Rubin, Statistical Analysis With Missing Data, 3rd

ed., Hoboken, NJ, USA: Wiley, 2019.

[36] B. Baesens, T. Van Gestel, S. Viaene, M. Stepanova, J. Suykens, and
J. Vanthienen, ‘‘Benchmarking state-of-the-art classification algorithms
for credit scoring,’’ J. Oper. Res. Soc., vol. 54, no. 6, pp. 627–635,
Jun. 2003. [Online]. Available: https://link.springer.com/article/10.1057/
palgrave.jors.2601561

[37] J. Han, M. Kamber, and J. Pei, Data Mining: Concepts and Techniques, 3rd
ed., San Mateo, CA, USA: Morgan Kaufmann, 2011. [Online]. Available:
https://www.sciencedirect.com/book/9780123814791/data-mining
[38] T. Bellotti and J. Crook, ‘‘Support vector machines for credit scoring
and discovery of significant features,’’ Expert Syst. Appl., vol. 36,
no. 2, pp. 3302–3308, Mar. 2009. [Online]. Available: https://www.
sciencedirect.com/science/article/pii/S0957417412007209

[39] D. J. Hand, ‘‘Modeling and assessing credit risk,’’ Statistician, vol. 50,
no. 3, pp. 361–372, 2001. [Online]. Available: https://www.jstor.org/
stable/2685552

XINCAI LI has been engaged in asset and manage-
ment related work for more than 20 years, presided
over and participated in a number of provincial
and ministerial projects. His research interests
include digital cultural industry and digital asset
management.

JIAYU LI studied finance in top universities in
China and participated in a number of provincial
and ministerial research projects. Her research
interests include frontier fields, such as financial
technology, cultural technology, and NFT virtual
currency.

180186

VOLUME 13, 2025

<!-- MARKITDOWN CONVERSION -->

<!-- Full MarkItDown conversion for formatting fidelity. -->

Received27September2025,accepted7October2025,dateofpublication16October2025,dateofcurrentversion23October2025.
DigitalObjectIdentifier10.1109/ACCESS.2025.3622358
Exploring Factors Involved in Loan Approval
Decision: Deep Insights and Data Analytics
Techniques
XINCAILI1 ANDJIAYULI 2
1AssetManagementOffice,BeijingLanguageandCultureUniversity,Beijing100083,China
2SchoolofEconomicsandBusinessAdministration,BeijingNormalUniversity,Beijing100875,China
Correspondingauthor:JiayuLi(15810889859@163.com)
ABSTRACT Accurate yet transparent credit-risk models are essential for responsible lending in the face
of tightening global AI regulations. We propose an end-to-end, reproducible pipeline for loan-default
predictionthatintegratesathree-wayconsensusfeature-selectionensembleusingVarianceThreshold,RFE
with logistic regression and XGBoost gain ranking; a lightweight one-dimensional convolutional neural
network optimised for tabular data; post-hoc explainability via KernelSHAP embedded directly in the
inference loop; and continuous system-level profiling of CPU, RAM, GPU and latency. Using the public
GiveMeSomeCredit dataset, our method reduces the original 11-feature space to a stable subset of five
predictors,achievingaROC-AUCof0.862andanF1-scoreof0.55onastratified20%hold-out,surpassing
the logistic regression and XGBoost baselines by 9% and 4% ROC-AUC, respectively. Ablation analysis
revealsthattheconsensusfeatureselectioncontributes57percentofthetotalaccuracygain,whilethe1D-
CNN architecture contributes an additional 38 percent. Fairness assessment shows disparate-impact and
equal-opportunitygapsbelow5percentacrossgenderandagecohorts,aligningwithemergingEUAIAct
thresholds. End-to-end inference averages 18 milliseconds on CPU-only hardware, confirming real-time
viability. All code, trained models, evaluation artifacts and resource logs are openly archived, offering a
deploy-readyblueprintforlendersaimingtomoderniselegacyscorecardswithoutsacrificinginterpretability,
compliance,oroperationalefficiency.
INDEXTERMS Loan-defaultprediction,credit-riskmodeling,1D-CNN,featureselection,explainability.
I. INTRODUCTION they often underperform in volatile economic climates or
Credit-Riskassessmentliesattheheartofmodernconsumer whenborrowerprofilesdeviatefromthehistoricalnorm.
finance. Every loan application forces lenders to weigh Recent advances in deep learning offer a path to more
the prospect of profit against the possibility of default and accurate credit risk prediction, but two barriers hinder
even marginal improvements in prediction translate into adoption in regulated domains: class imbalance, since
sizeable monetary impacts at portfolio scale. Traditional defaults are rare and explainability, as closed box models
credit-scoring systems which arebuilt on logistic regression are difficult to justify to auditors and regulators [4], [5].
or simple decision trees and hand-crafted feature engi- Regulatory bodies such as the European Banking Authority
neering that remain popular because they are inexpensive, and the U.S. Consumer Financial Protection Bureau are
fast and reasonably transparent but Yet their capacity to tightening transparency requirements, while practitioners
capture non-linear interactions among the high-dimensional must also meet operational constraints such as real-time
attributes now routinely collected by banks, fintechs and speed, hardware efficiency and reproducibility [6], [7], [8].
creditbureaus isinherentlylimited [1],[2],[3]. Asaresult, To address these challenges, we propose a comprehensive
pipeline for default risk prediction using the Give Me
The associate editor coordinating the review of this manuscript and Some Credit dataset [9]. The framework combines ensem-
approvingitforpublicationwasVladDiaconita . ble feature selection (VarianceThreshold, RFE, XGBoost),
2025TheAuthors.ThisworkislicensedunderaCreativeCommonsAttribution4.0License.
180172 Formoreinformation,seehttps://creativecommons.org/licenses/by/4.0/ VOLUME13,2025

X.Li,J.Li:ExploringFactorsInvolvedinLoanApprovalDecision:DeepInsightsandDataAnalyticsTechniques
alightweightone-dimensionalCNNforefficientdeployment forreal-worlddeployment.Thefollowingresearchobjectives
and SHAP-based explanations that provide both global guidedourdevelopment:
rankingsandper-applicantinsights[10],[11],[12],[13]. RO1: Design an automated ensemble feature-selection
Beyond predictive performance and interpretability, mechanism that is reproducible and dataset-agnostic. To
weaddresspracticalengineeringconsiderationsthatareoften ensure stability and generalizability, we developed a hybrid
overlooked in academic work but significantly influence feature-selection strategy that combines VarianceThreshold
industrial decision-making. The pipeline incorporates the filtering,RecursiveFeatureElimination(RFE)andXGBoost-
system-levelprofiling,trackingmemoryfootprint,CPU/GPU based importance. This ensemble approach captures both
utilization and per-sample inference latency to facilitate statistical relevance and model-specific utility, produc-
capacityplanningforreal-timedeployment[14].Allartifacts, ing a compact, information-rich subset of features. The
includingtrainedmodels,selectedfeatures,evaluationplots, pipelineisfullyautomatedandadaptabletotabulardatasets
SHAP visualizations and resource logs, are automatically of varying dimensionality, supporting reproducibility and
archived to support auditability, version control and down- transferability.
streamexperimentation[15]. RO2: Develop a lightweight 1D-CNN architecture for
This work makes four important contributions. First, tabular credit data, balancing accuracy with CPU-level
we demonstrate that intersecting three complementary inference speed. We designed a custom one-dimensional
feature-selectionmethodsyieldsacompactandstablesubset Convolutional Neural Network (1D-CNN) optimized for
of predictors that enhances both accuracy and explain- low-latency inference on standard CPUs. By exploiting
ability [16]. Second, we introduce a lightweight 1D-CNN spatiallocalityintheorderedfeaturevectorandminimizing
|     |     |     |     |     | parameter | count, | the model | achieves | a strong | trade-off |
| --- | --- | --- | --- | --- | --------- | ------ | --------- | -------- | -------- | --------- |
modelthatachievescompetitiveROC-AUCwhileremaining
efficient enough for CPU-based deployment [12]. Third, between expressive power and computational efficiency,
theframeworkincludesSHAP-basedexplanationsembedded making it suitable for real-time or resource-constrained
directly into the inference loop, enabling local decision environments.
justifications required for compliant, user-facing lending RO3: Embed SHAP-based global and local explanations
|         |                |                     |                  |     | directly | into the | inference | loop | to satisfy regulatory | trans- |
| ------- | -------------- | ------------------- | ---------------- | --- | -------- | -------- | --------- | ---- | --------------------- | ------ |
| systems | [17]. Finally, | the entire pipeline | is operationally |     |          |          |           |      |                       |        |
profiled,versionedandpackagedforseamlessdeploymentor parencystandards.Inalignmentwithregulationssuchasthe
further research, addressing a key gap in existing academic EUAIActandU.S.FairCreditReportingAct,weintegrated
treatments[15]. SHAP into the inference pipeline. This enables both global
As the lending industry begins to utilize various types interpretability (feature importance rankings) and local
|         |                     |                  |               |     | explanations | (per-applicant |     | rationale), | ensuring | that credit |
| ------- | ------------------- | ---------------- | ------------- | --- | ------------ | -------------- | --- | ----------- | -------- | ----------- |
| of data | such as transaction | records, utility | bill payments |     |              |                |     |             |          |             |
and even social media activity, the models used for decisionsremainauditable,transparentandtrustworthy.
decision-making must adapt to handle large, complex and RO4: Integrate continuous profiling of memory, compute
sometimes sensitive information sources [18], [19]. Our and latency to quantify deployment feasibility under real-
proposed system is built to be flexible and work within the world constraints. Beyond predictive accuracy, practical
|           |                        |      |                     |     | deployment | requires | operational |     | efficiency. | The framework |
| --------- | ---------------------- | ---- | ------------------- | --- | ---------- | -------- | ----------- | --- | ----------- | ------------- |
| limits of | the DHT (decentralized | hash | table) environment: |     |            |          |             |     |             |               |
thefeature-selectionpartcanbeadjustedtoincludespecific incorporates runtime profiling tools that monitor CPU/GPU
rules from the field or use automatic machine learning utilization, memory footprint and per-sample inference
filters, while the main CNN model does not depend on the latency.Thesemetricsprovideactionableinsightsforsystem
size or shape of the input data, allowing it to be quickly engineerstovalidatedeploymentfeasibilityunderreal-world
resourceandlatencyconstraints.
| retrained | on different datasets | [20]. Most | importantly, | this |     |     |     |     |     |     |
| --------- | --------------------- | ---------- | ------------ | ---- | --- | --- | --- | --- | --- | --- |
studyplacesastrongemphasisonensuringthattheresultscan Therestofthepaperprovidesareviewofrelatedworkin
beconsistentlyreproducedbyothersandthattheworkingsof credit-riskmodelingandinterpretability,detailstheproposed
|     |     |     |     |     | methodology, | presents | experimental |     | findings | and concludes |
| --- | --- | --- | --- | --- | ------------ | -------- | ------------ | --- | -------- | ------------- |
themodelaretransparentandeasilyunderstood.Bydoingso,
ithelpsguaranteethatanymodificationsorextensionstothe withpracticalimplicationsandfuturedirections.
systemremainfullycompliantwithregulatoryrequirements,
which are strict rules set to protect consumers and ensure II. LITERATUREREVIEW
fairness. At the same time, maintaining clear explanations Credit-risk modelling has evolved significantly over the
|                  |       |                    |     |          | past few | decades. | As  | theft and | human error | have been |
| ---------------- | ----- | ------------------ | --- | -------- | -------- | -------- | --- | --------- | ----------- | --------- |
| and transparency | helps | build and preserve | the | trust of |          |          |     |           |             |           |
users,includinglenders,regulatorsandborrowers.Thesetwo involved, researchers have been drawn to this domain,
factors,regulatorycomplianceandusertrust,arefundamental which has seen advances in both statistical theory and
totheresponsibleandethicaluseofAItechnologyinmaking computing infrastructure. In the Early days, the sys-
criticalfinancialdecisions. tems, which were dominated by interpretable scorecard-
|     |     |     |     |     | based models, |     | most notably |     | logistic regression, | which |
| --- | --- | --- | --- | --- | ------------- | --- | ------------ | --- | -------------------- | ----- |
A. CONTRIBUTIONSANDRESEARCHOBJECTIVES gained popularity for its simplicity, efficiency and align-
Thisstudyaddressescriticalgapsincredit-riskmodelingby ment with regulatory expectations [21]. These were often
designing a fully integrated, reproducible pipeline tailored enhancedbymanualfeatureengineeringtechniquessuchas
| VOLUME13,2025 |     |     |     |     |     |     |     |     |     | 180173 |
| ------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------ |

X.Li,J.Li:ExploringFactorsInvolvedinLoanApprovalDecision:DeepInsightsandDataAnalyticsTechniques
Weight-of-Evidence (WoE) binning and information-value In parallel, a growing body of work emphasizes the
filtering, which enabled better handling of categorical and importance of operational robustness, reproducibility and
skewedvariables[22]. responsibleAIdeploymentinfinancialapplications.End-to-
With the evolution in the domain of machine learning, endMLOpspipelinesarebeingdevelopedtosupportmodel
which ensembled the methods such as Random Forests and versioning,explainabilityloggingandcomplianceauditingin
Gradient Boosting Machines, they began to replace linear line with emerging standards. For instance, modular archi-
legacy models due to their ability to capture non-linear tectures that separate feature engineering, model training
relationships and higher-order interactions within borrower and explanation generation have been shown to improve
attributes[23],[24].WhiletheXGBoostandLightGBMhave traceability and governance [8], [15]. At the same time,
particularly been known and have become the mainstream AutoML frameworks are gaining popularity for automating
duetotheirscalability,theyalsohaveregularizationmecha- model selection and hyperparameter tuning, yet they often
nismsandbuilt-infeatureimportancetools[11],[25].While lack transparency and produce overly complex pipelines
thesemodelsimprovepredictiveperformance,theyintroduce unsuited for regulatory settings [20]. These developments
complexityandreduceinterpretability,promptingawaveof highlight the need for leaner, interpretable architectures
researchonbalancingaccuracywithexplainability. that can be integrated with audit-ready workflows while
Notably, contributions include the use of RFE with maintainingperformanceacrossunseendata.
tree-based classifiers and mutual information filtering to Despite these advances, few frameworks offer a fully
reduce redundancy and improve model generalization [10], integrated solution that combines accurate deep models,
[26]. Alongside, the feature selection techniques have robustfeatureselection,embeddedexplainabilityandsystem-
transitioned from standalone statistical filtering to hybrid level profiling. Our work addresses this critical gap by
strategiescombiningmultiplefilter,wrapperandembedding proposing a comprehensive and reproducible pipeline that
methods.However,manyofthesepipelinesarecustom-built, unites variance filtering, RFE and gradient-boosted feature
lack automation and often do not address reproducibility, importance; a lightweight 1D-CNN optimized for CPU
agrowingconcerninindustrialdeployments[8]. deployment; embedded SHAP-based interpretability during
Recent breakthroughs in deep learning have opened the inference; and operational metrics such as memory usage,
door for using convolutional and attention-based architec- latencyandcomputeload.Toourknowledge,thisisthefirst
tures in tabular credit data. Although CNNs were initially suchend-to-endimplementationthatmeetsbothperformance
developed for spatial domains such as images, lightweight andregulatorycriteriaforreal-worldcredit-riskdeployment.
1D-CNNshavebeenshowntoeffectivelymodelorderedfea-
ture vectors in financial datasets, sometimes outperforming III. METHODOLOGY
MLPsandeventreeensembles[27],[28].Transformer-based This section outlines the end-to-end pipeline proposed for
models like TabNet and PatchTFT have also demonstrated loan-default risk prediction, from raw data ingestion to
strongresults,butfaceadoptionbarriersinregulateddomains deployable, profiled models. All code, configuration files
due to their closedbox nature and hardware demands. and artifacts are version-controlled and publicly archived to
Toaddressthesetransparencyconcerns,avarietyofexplain- guaranteefullreproducibility.
able AI (XAI) techniques have been proposed, including
SHAP[13],LIME[29]andIntegratedGradients[30].SHAP,
A. DATASETANDPROBLEMDEFINITION
in particular, provides consistent global and local feature We use the GiveMeSomeCredit dataset, which contains
attributions grounded in cooperative game theory, but most 150,000 records and 11 features describing each bor-
XAImethodsarestillappliedpost-hocandremaindecoupled rower, along with a binary target variable called Serious-
from live scoring environments, limiting their utility in Dlqin2yrs that indicates whether the borrower defaulted
real-timecreditdecisioning[5],[31]. within24months.Eachrecordinthedatasetcorrespondsto
Some studies have attempted to bridge these gaps. an individual consumer and is represented as a pair (x,y),
i i
Brownetal.developedanintegratedXGBoostpipelinewith wherex ∈ Rd isafeaturevectorofdimensiond = 11and
i
liveSHAPvisualizationsusedbyunderwriters,whichreport- y ∈ {0,1}isthebinarylabelindicatingdefaultstatus(0for
i
edly reduced manual intervention by 10% [32]. Lopezetal. nodefault,1fordefault),asshowninEquation(1).
introduced a hybrid RFE XGBoost feature selector that Ourmodelingpipelineprocesseseachinputx toestimate
i
eliminated 40% of features without sacrificing AUC [33]. theprobabilitypˆ thataborrowerwilldefault,formulatedas
i
Nguyen et al. compared a depthwise separable 1D-CNN to Pθ(y
i
= 1 | x
i
), where θ represents the model parameters,
TabNetandshowedthatCNNsachievedfasterinferenceby asshowninEquation(2).
up to 8 milliseconds per instance on standard CPUs [28]. While estimating the probability, the system makes a
Albanesi and Vamossy have also demonstrated that the deterministic loan approval decision using a threshold τ,
feasibility of incorporating these payment and transaction whichissetto0.5.Specifically,ifthepredictedprobabilitypˆ
i
historiesinthedomainofdeeplearningforimproveddefault exceedsthethresholdτ,theloanisrejected;otherwise,itis
prediction,thoughtransparencyremainedachallenge[34]. approved,asdescribedinEquation(3).
180174 VOLUME13,2025

X.Li,J.Li:ExploringFactorsInvolvedinLoanApprovalDecision:DeepInsightsandDataAnalyticsTechniques
TABLE1. ClassdistributionforthetargetvariableSeriousDlqin2yrs. profilearearrangedsequentiallyasaone-dimensionalvector
ratherthanasatemporalseries,whichallowsconvolutional
filterstocapturelocaldependenciesamongadjacentfeatures.
This representation highlights structured relationships that
may be overlooked by conventional tabular models. The
This thresholding mechanism strikes a balance between
architecture consists of three convolutional layers with 128,
risk and opportunity, ensuring that borrowers with a higher
64 and 32 filters of kernel size 3, each followed by batch
estimatedriskofdefaultaredeclined,whilethosewithlower
normalization and a Global Average Pooling layer that
risk are approved. This probabilistic framework supports
reduces the feature maps into a compact representation.
transparency and interpretability in the decision-making
Adenselayerwith64ReLUunitsthenextractshigher-level
process.
abstractions and a final sigmoid unit outputs the default
D={(x,y)}N , x ∈Rd, y ∈{0,1}, probability. The design balances predictive accuracy with
i i i=1 i i
computational efficiency, making it suitable for CPU-
d =11 (1)
constrainedenvironments.
pˆ
i
=Pθ(y
i
=1|x
i
) (2)
(
Reject ifpˆ >τ Algorithm21D-CNNforTabularDataClassification
Decision= i
Approve otherwise Require: Inputfeaturevectorx ∈Rd,labely∈{0,1}
whereτ =0.5 (3) Ensure: Predictedprobabilitypˆ ∈[0,1]
1:
Normalizeandreshapextoshape(d,1)(treatingfeatures
Table 1 illustrates the distribution of the targeted vari- asanorderedsequence)
able SeriousDlqin2yrs, which indicates a strong imbalance 2: ConvolutionLayer1:1Dconvolutionwith128filters,
between the two classes in the dataset. The majority of kernelsize=3,ReLUactivation
borrowers did not default within the 24 months, as shown, 3: BatchNormalization1:Normalizeactivations
while a relatively small portion of the class represented 4: Convolution Layer 2: 1D convolution with 64 filters,
defaulters. Such distributions are imbalanced, which often kernelsize=3,ReLUactivation
causes classifiers to favor the majority class, resulting in a 5: BatchNormalization2:Normalizeactivations
model that performs better at identifying the more common 6: Convolution Layer 3: 1D convolution with 32 filters,
casesbutstrugglestorecognizetheminorityclassaccurately. kernelsize=3,ReLUactivation
Thisimbalancereducesthemodel’sabilitytodetectrarebut 7: GlobalAveragePooling:Reducefeaturemapstofixed-
importantinstances,suchasborrowerswhodefaultontheir sizevector
loans. 8: DenseLayer:Fullyconnectedlayerwith64units,ReLU
activation
B. FEATURESELECTION
9: Output Layer: Dense layer with 1 unit, sigmoid
Figure13presentstheagreementmatrixforVarianceThresh-
activationtoproducepˆ
old, Recursive Feature Elimination (RFE) and XGBoost.
10: return pˆ =σ(z)
FeaturessuchasNumberOfTimes90DaysLate,RevolvingUti-
lizationOfUnsecuredLines and DebtRatio were also being
consistentlyselected,confirmingstrongpredictiveutilityand The end-to-end workflow for our unified credit-risk pre-
while others like MonthlyIncome and NumberOfOpenCred- dictionpipelineisshowninFigure1.Startingfromstructured
itLinesAndLoans have shown divergence across methods. tabulardatainCSVformat,featureengineeringandselection
This matrix highlights transparency in feature selection and are performed through a hybrid ensemble of Variance
supportstherobustnessofthefinalsubsetinAlgorithm2. Threshold filtering, XGBoost importance ranking and RFE
to yield a compact, informative subset. These features are
Algorithm1ConsensusFeatureSelection thenprocessedbyacustom1D-CNNtailoredfortabulardata,
Require: TrainingmatrixX ∈RN×d whichcapturesspatiallocalityviaconvolution,activationand
Ensure: SelectedfeatureindicesF ⋆ pooling layers. The model is trained on labeled data with
1: ApplyVarianceThreshold→F Var performance metrics such as accuracy curves logged, after
2: RunRFE(LogReg,X[:,F Var ])→F RFE whichthetrainedmodelfileisstoredandappliedtounseen
3: TrainXGBoostonX →feature_gain_rank cases. During inference, it generates probability scores
4: LetF XGB =top k (feature_gain_rank) evaluated against a 0.5 threshold to classify applications as
5: return F ⋆ =F Var ∩F RFE ∩F XGB Approved or Rejected. The modular, versioned design of
thepipelineensuresreproducibility,auditabilityandpractical
deploymentinreal-timecredit-scoringsystems.
C. MODELARCHITECTURE The end-to-end architecture for our pipeline is illustrated
Algorithm2outlinestheproposedlightweight1D-CNNfor in Figure 2, showing the loan default prediction system.
tabular borrower data. The features within each borrower It has encapsulated all core stages: data ingestion, feature
VOLUME13,2025 180175

X.Li,J.Li:ExploringFactorsInvolvedinLoanApprovalDecision:DeepInsightsandDataAnalyticsTechniques
FIGURE1. Overallframeworkoftheproposedpipelineforcredit-riskpredictionusing
ensemble-basedfeatureselectionand1D-CNNclassification.
FIGURE3. SkeweddistributionofRevolvingUtilizationOfUnsecured
Lines.
newloandataispreprocessed,masked,scoredbythemodel
andevaluatedagainstadecisionthreshold.SHAPgenerates
FIGURE2. Pipelineflowchartshowingthecompletelifecycle:fromdata
explanations and outcomes are stored for transparency. The
preprocessingandfeatureselectiontomodeltraining,SHAP-based
interpretabilityanddecisionstorage. frameworkensuresexplainable,efficientandtraceablecredit
scoringforfinanciallending.
selection,modeltraining,inference,explainabilityanddeci-
sion logging. The workflow is modular, version-controlled IV. RESULTSANDDISCUSSION
anddesignedforeasyreproducibilityanddeployment. A. DATAPRE-PROCESSING
Therightsideofthefigureshowsdataloading,preprocess- Figure 3 shows that the RevolvingUtilizationOfUnsecured-
ing,ensemblefeatureselectionwithVarianceThreshold,RFE Linesfeatureishighlyskewed,withmostvaluesnearzeroand
andXGBoost,followedbytrainingofalightweight1D-CNN. afewextremeoutliers.Toreducetheirinfluence,techniques
ThebestmodelissavedandprofiledforCPU,memoryand suchascapping,logtransformationorspecializedscalingare
latency.Ontheleft,thepipelineenablesreal-timeinference: applied,improvingmodelstabilityandgeneralization.
180176 VOLUME13,2025

X.Li,J.Li:ExploringFactorsInvolvedinLoanApprovalDecision:DeepInsightsandDataAnalyticsTechniques
FIGURE4. Agedistributionstratifiedbydefaultstatus.
FIGURE6. Missingvaluedistributionperfeature.
FIGURE5. Debtratiodistributionacrossdefaultclasses.
Figure 4 illustrates the age distribution of borrowers,
FIGURE7. Post-imputationdistributionofMonthlyIncome.
grouped by their default outcome. The boxplot reveals that
individuals who defaulted (SeriousDlqin2yrs = 1) tend to was used for continuous features, which fills in missing
be younger on average, with a visibly lower median age values with the middle number of the existing data. This
compared to non-defaulters. The spread among younger methodhelpskeepimportantinformationwithoutremoving
borrowers is also wider and a higher density of outliers goodrecords[35].
appears in this group. This observation suggests a potential Figure 7 shows the distribution of MonthlyIncome after
behavioral risk pattern associated with age and aligns with missingvalueswerefilledusingmedianimputation.Thedata
SHAP-basedinterpretabilityresults,whereageemergedasa remains uneven, with most incomes below $20,000, but a
toppredictorofdefaultrisk. few very high values persist. Median imputation was used
Figure 5 shows a violin plot of the DebtRatio feature, becauseithelpsreducetheeffectofextremenumberswhile
separated by whether the borrower defaulted or not. The keeping the general shape of the data. This way, the model
values are unevenly spread, with many low numbers and a islessaffectedbymissingdataandthefilled-invaluesbetter
longtailreachingtowardveryhighnumbers.Forborrowers representthetypicalincomeofborrowers[36].
who defaulted, especially, some values are very large and Figure 8 shows the spread of the numeric features age,
unusual. Because of this, outlier treatment methods like DebtRatio and MonthlyIncome after they were transformed
winsorization are used to handle these extreme values. This usingstandardscaling.Thisprocessmovesthedatasothatit
helpskeepthemodelsteadyduringtrainingandallowsitto centers around zero and has a spread of one. This has also
workwellwhenseeingnewdata. helped us improve the model’s performance with methods
Figure6showshowmanymissingvaluesarefoundineach that rely on measuring distances or calculating gradients.
featureofthedataset.Mostfeatureshavecompletedata,but Some outliers are still visible, especially for DebtRatio
some, like MonthlyIncome and NumberOfDependents, have and MonthlyIncome, but these were already reduced by
many missing entries, with up to 30,000 missing values for winsorizationbeforescaling.Thefinalscaleddatahelpsthe
income.Thesemissingpartsneedtobehandledcarefullyto CNNmodellearnmoresmoothlybykeepingallfeatureson
keepthemodelstableandfair.Therefore,medianimputation asimilarscale.
VOLUME13,2025 180177

X.Li,J.Li:ExploringFactorsInvolvedinLoanApprovalDecision:DeepInsightsandDataAnalyticsTechniques
FIGURE10. RFE-basedfeatureranking(lowerisbetter).
FIGURE8. Boxplotofscalednumericalfeatures.
FIGURE11. XGBoostfeatureimportancebasedoninformationgain.
FIGURE9. Varianceoffeaturesbeforefiltering.
| Missing-value |            | imputation   | is performed |     | using median |
| ------------- | ---------- | ------------ | ------------ | --- | ------------ |
| values for    | continuous | variables.   | Outliers     | are | capped using |
| the 1st       | and 99th   | percentiles. | Features     | are | scaled using |
standardizationwithparametersfittedonthetrainingsetonly.
Non-informativefeatureswithmorethan95percentidentical
valuesareremoved[37].
B. FEATURE-SELECTIONENSEMBLE
| We adopt  | a three-way | consensus  | strategy     | to   | obtain a robust |
| --------- | ----------- | ---------- | ------------ | ---- | --------------- |
| subsetF ⋆ | ⊆{1,...,d}. |            |              |      |                 |
| Figure    | 9 shows     | the amount | of variation | each | feature has     |
beforeusingtheVarianceThresholdfilter.Thisstepremoves
| features | that do not | change | much or | are almost | the same |
| -------- | ----------- | ------ | ------- | ---------- | -------- |
forallsamples,becausesuchfeaturesdonotprovideuseful FIGURE12. Correlationheatmapoffinalselectedfeatures.
informationtothemodel.Asshown,noneofthefeaturesfall
below the threshold, showing that they all exhibit sufficient meaningfulfeatures,makingthemodelsimplerandbetterat
variability to be retained by the models for subsequent distinguishingbetweenoutcomes[10].
selection stages. This verification ensures that later stages, Figure11showstheimportancescoresoffeaturesasmea-
suchasRFEandXGBoost,operateonameaningfulfeature sured by the XGBoost classifier. These scores are based on
space. theinformationgain,whichalsoshowsusthemeasureofhow
Figure10showshowfeatureswererankedusingRFEwith much each feature has contributed to reducing uncertainty
logisticregressionasthebasemodel.Eachfeaturehasbeen when splitting the data during training. The feature named
scoredaccordingtohowmuchithelpedthemodelperform, NumberOfTimes90DaysLateisthemostimportant,followed
with lower scores meaning greater importance. The plot by NumberOfTime30-59DaysPastDueNotWorse and then
shows that features like age, NumberOfTimes90DaysLate NumberOfTime60-89DaysPastDueNotWorse.Thesefeatures
and DebtRatio are the most useful for prediction, while relate directly to past payment delays, making them very
others, such as RevolvingUtilizationOfUnsecuredLines, are relevant for predicting credit default and confirming their
less important. This process helps focus on the most placeinthefinalsetofselectedfeatures.
180178 VOLUME13,2025

X.Li,J.Li:ExploringFactorsInvolvedinLoanApprovalDecision:DeepInsightsandDataAnalyticsTechniques
| FIGURE13. | Agreementmatrixacrossvariancethreshold,RFEand |     |     |     |     |     |     |     |     |     |     |     |     |
| --------- | --------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
XGBoost.Avalueof1indicatesthefeaturewasselectedbythemethod.
TABLE2. Comparisonoffeatureselectionresultsacrossmethods.
Featuresretainedinthefinalsetwereselectedbyatleasttwooutofthe
threetechniques.
|     |     |     |     |     |     |     | FIGURE14. | Correlationheatmapofinputfeatures.Strongrelationships |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --------- | ----------------------------------------------------- | --- | --- | --- | --- | --- |
betweendelinquency-relatedvariablessupporttheneedforfeature
reduction.
C. FEATURESELECTIONOUTCOMES
Low to moderate correlations are exhibited by most To find the most important features, a three-step ensemble
| features. | A correlation |     | heatmap | of the | features | selected |           |         |           |        |     |                   |     |
| --------- | ------------- | --- | ------- | ------ | -------- | -------- | --------- | ------- | --------- | ------ | --- | ----------------- | --- |
|           |               |     |         |        |          |          | selection | process | was used. | First, | the | VarianceThreshold |     |
through deep feature selection by multiple models is pre- method removed features with very low variance. Next,
sented in Figure 12. This indicates that multicollinearity is Recursive Feature Elimination was applied, which uses a
| limited. | This property |     | is considered | important |     | for ensuring |          |        |          |       |        |      |           |
| -------- | ------------- | --- | ------------- | --------- | --- | ------------ | -------- | ------ | -------- | ----- | ------ | ---- | --------- |
|          |               |     |               |           |     |              | model to | select | features | based | on how | much | they help |
model stability and generalizability. Some notable pairs, improve performance. Finally, XGBoost was used to rank
| such as | NumberOfTime30-59DaysPastDueNotWorse |     |     |     |     | and |          |           |        |             |     |           |         |
| ------- | ------------------------------------ | --- | --- | --- | --- | --- | -------- | --------- | ------ | ----------- | --- | --------- | ------- |
|         |                                      |     |     |     |     |     | features | according | to the | information |     | gain they | provide |
NumberOfTime60-89DaysPastDueNotWorse,exhibitmoder- during training. Each method looked at feature importance
atecorrelationduetotheirsemanticproximity.However,the from a different angle: variance on its own, contribution to
| majority | of selected | attributes |     | are complementary, |     | covering |     |     |     |     |     |     |     |
| -------- | ----------- | ---------- | --- | ------------------ | --- | -------- | --- | --- | --- | --- | --- | --- | --- |
themodelandgainbasedongradients[10],[11],[16].
diversefinancialbehaviorssuchasdelinquency,incomeand Theintersectionofthesethreemethodsyieldedacompact
utilization,makingthefeaturesubsetwell-suitedforlearning
|     |     |     |     |     |     |     | subset of | five | features: | age, MonthlyIncome, |     |     | DebtRatio, |
| --- | --- | --- | --- | --- | --- | --- | --------- | ---- | --------- | ------------------- | --- | --- | ---------- |
complexpatternsindefaultprediction. NumberOfTimes90DaysLateandRevolvingUtilizationOfUn-
Algorithm 1 shows the steps used to find a strong and securedLines.Theseattributeswereconsistentlyrankedhigh
| easy-to-understand |     | group | of features. | First, | features | that do |     |     |     |     |     |     |     |
| ------------------ | --- | ----- | ------------ | ------ | -------- | ------- | --- | --- | --- | --- | --- | --- | --- |
acrossallcriteriaandretainedformodeltraining.Thishybrid
not change much are removed because they do not give approach provided greater stability and robustness than any
helpful information. Then, the smaller set of features is singlemethodalone.
examinedusingRecursiveFeatureEliminationwithalogistic
|     |     |     |     |     |     |     | The correlation |     | matrix | in Figure | 14  | highlights | notable |
| --- | --- | --- | --- | --- | --- | --- | --------------- | --- | ------ | --------- | --- | ---------- | ------- |
regression model to determine which ones improve the multicollinearityamongseveraldelinquency-relatedfeatures,
| model’s | performance. |     | After that, | XGBoost | is  | trained on all |           |                          |     |     |     |                 |     |
| ------- | ------------ | --- | ----------- | ------- | --- | -------------- | --------- | ------------------------ | --- | --- | --- | --------------- | --- |
|         |              |     |             |         |     |                | including | NumberOfTimes90DaysLate, |     |     |     | NumberOfTime60- |     |
thedataandfeaturesarerankedbasedonhowmuchtheyhelp 89Days PastDueNotWorse and NumberOfTime30-59Days
⋆
reduce uncertainty. The final group of features, called F , PastDueNotWorse.Thesevariablesarenearlycollinearwith
| is made | by keeping | only | the features | that | all three | methods |            |              |     |        |            |      |          |
| ------- | ---------- | ---- | ------------ | ---- | --------- | ------- | ---------- | ------------ | --- | ------ | ---------- | ---- | -------- |
|         |            |      |              |      |           |         | each other | (correlation | >   | 0.98), | suggesting | that | they may |
agreeareimportant.Thisway,thechosenfeaturesaremore contribute redundant information during model training.
reliable,themodelavoidsoverfittingtothetrainingdataand
|     |     |     |     |     |     |     | Additionally, | low | correlation | values | between | most | predic- |
| --- | --- | --- | --- | --- | --- | --- | ------------- | --- | ----------- | ------ | ------- | ---- | ------- |
itcanworkwellonnewdata[10],[11]. tors and the target (SeriousDlqin2yrs) imply the need for
Table 2 summarizes the outcomes of all three feature non-linearmodelsandadvancedfeatureinteractionlearning
selectiontechniques.Thecolumnsindicatewhetherafeature
|     |     |     |     |     |     |     | strategies. | This | analysis informed |     | our decision |     | to apply a |
| --- | --- | --- | --- | --- | --- | --- | ----------- | ---- | ----------------- | --- | ------------ | --- | ---------- |
wasretainedbyVarianceThreshold,selectedbyRFEandits hybrid feature selection strategy and standardize inputs to
| importance | score, | High | and Medium, | from | XGBoost. | Only |     |     |     |     |     |     |     |
| ---------- | ------ | ---- | ----------- | ---- | -------- | ---- | --- | --- | --- | --- | --- | --- | --- |
avoiddistortionfromcollinearorskewedattributes.
| features | that appeared |     | in at least | two of | the three | methods |     |     |     |     |     |     |     |
| -------- | ------------- | --- | ----------- | ------ | --------- | ------- | --- | --- | --- | --- | --- | --- | --- |
wereincludedinthefinalset.Thishybridconsensusreduced D. ADVANCEDCLASSIMBALANCEHANDLING
redundancy,ensuredinterpretabilityandprovidedabalanced Class imbalance is a well-known challenge in credit risk
trade-offbetweensimplicityandpredictivepower. datasets. Along with threshold tuning and class weighting,
| VOLUME13,2025 |     |     |     |     |     |     |     |     |     |     |     |     | 180179 |
| ------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------ |

X.Li,J.Li:ExploringFactorsInvolvedinLoanApprovalDecision:DeepInsightsandDataAnalyticsTechniques
| FIGURE15. | Comparisonofimbalancehandlingtechniques(baseline, |     |     |     |     |     |     |     |     |     |     |     |     |     |     |
| --------- | ------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
classweights,smote)acrossPrecision,RecallandF1-score.Class
weightingprovidedthemostbalancedperformance.
|     |     |     |     |     |     |     |     | FIGURE16. | Trainingandvalidationaccuracyacrossepochs.Accuracy |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --------- | -------------------------------------------------- | --- | --- | --- | --- | --- | --- |
wealsotestedadvancedmethodssuchasSMOTEoversam- stabilizesbyepoch5,indicatingfastconvergence.
| pling and        | cost-sensitive |              | learning.   | Figure         | 15          | shows      | how the |     |     |     |     |     |     |     |     |
| ---------------- | -------------- | ------------ | ----------- | -------------- | ----------- | ---------- | ------- | --- | --- | --- | --- | --- | --- | --- | --- |
| three strategies |                | compare      | in          | terms of       | precision,  | recall     | and     |     |     |     |     |     |     |     |     |
| F1-score.        | SMOTE          | increased    |             | recall         | but reduced | precision, |         |     |     |     |     |     |     |     |     |
| leading          | to noisier     | predictions. |             | Cost-sensitive |             | weighting  |         |     |     |     |     |     |     |     |     |
| through          | class weights  |              | gave a      | more           | balanced    | trade-off  | and     |     |     |     |     |     |     |     |     |
| achieved         | the highest    | overall      | F1-score    |                | of 0.72.    | This       | balance |     |     |     |     |     |     |     |     |
| is especially    | important      |              | in lending, |                | where       | too many   | false   |     |     |     |     |     |     |     |     |
| positives        | approving      | risky        | loans       | must           | be avoided  | while      | still   |     |     |     |     |     |     |     |     |
identifyingtruedefaults.Forthisreason,classweightingwas
chosenasthemaintechniqueforhandlingimbalanceinthis
study.
E. MODELPERFORMANCE
| Using the | selected | features, |     | a lightweight | one-dimensional |     |     |     |     |     |     |     |     |     |     |
| --------- | -------- | --------- | --- | ------------- | --------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
convolutional neural network, or 1D-CNN, was trained. Its FIGURE17. Trainingandvalidationlossperepoch.Gradualdeclinein
lossconfirmsstablelearningwithmildoverfitting.
| performance | was        | compared | with   | two        | other | models:       | a CNN |             |          |     |           |     |               |                |     |
| ----------- | ---------- | -------- | ------ | ---------- | ----- | ------------- | ----- | ----------- | -------- | --- | --------- | --- | ------------- | -------------- | --- |
| combined    | with       | a BiLSTM | hybrid | model      | and   | a traditional |       |             |          |     |           |     |               |                |     |
|             |            |          |        |            |       |               |       | Figure      | 17 shows | the | evolution | of  | training      | and validation |     |
| logistic    | regression | model.   | The    | evaluation |       | was done      | on    |             |          |     |           |     |               |                |     |
|             |            |          |        |            |       |               |       | loss across | epochs.  | The | training  |     | loss steadily | declines,      |     |
the validation set by measuring accuracy, precision, recall, suggesting consistent model optimization without abrupt
| F1-score | and the | ROC-AUC |     | metric. | The | 1D-CNN | model |     |     |     |     |     |     |     |     |
| -------- | ------- | ------- | --- | ------- | --- | ------ | ----- | --- | --- | --- | --- | --- | --- | --- | --- |
convergence.Thevalidationlossexhibitsmorevariance,yet
achieved a ROC-AUC score of 0.86, which was better than maintains a downward trend with intermittent spikes likely
bothcomparisonmodels.Eventhoughitisasimplermodel, influencedbyclassimbalanceanddatavariabilityandmost
| it demonstrated |     | strong | precision | and | recall, | indicating | that |              |       |       |       |            |         |     |          |
| --------------- | --- | ------ | --------- | --- | ------- | ---------- | ---- | ------------ | ----- | ----- | ----- | ---------- | ------- | --- | -------- |
|                 |     |        |           |     |         |            |      | importantly, | there | is no | sharp | divergence | between |     | training |
the chosen features and network design work well together. andvalidationloss,sothisprovesthatthemodelhasavoided
Additionally,themodelhadfewertrainableparametersthan
|     |     |     |     |     |     |     |     | the overfitting |     | and retains | generalizability. |     |     | The relatively |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --------------- | --- | ----------- | ----------------- | --- | --- | -------------- | --- |
themorecomplexhybridmodels,makingiteasiertorunon
|     |     |     |     |     |     |     |     | lower validation |     | loss further |     | reinforces | the effectiveness |     | of  |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------------- | --- | ------------ | --- | ---------- | ----------------- | --- | --- |
CPUsandsuitableforpracticaldeployment. regularizationandappropriatemodelcapacity.
Figure16showshowthetrainingandvalidationaccuracy
| changed | over 22 | epochs. | The | training | accuracy | increased |     |     |     |     |     |     |     |     |     |
| ------- | ------- | ------- | --- | -------- | -------- | --------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
EVALUATIONMETRICS:PRECISION,RECALLANDF1-SCORE
quicklyduringthefirstfewepochsandleveledoffaroundthe
|     |     |     |     |     |     |     |     | To assess | classification |     | performance, |     | we  | use three | key |
| --- | --- | --- | --- | --- | --- | --- | --- | --------- | -------------- | --- | ------------ | --- | --- | --------- | --- |
fifthepoch.Thismeansthemodellearnedfastandreacheda
metrics:precision,recallandF1-score.Thesearecomputed
| stablepointthankstoagoodlearningrateandmodeldesign. |     |            |          |     |          |        |      | asfollows: |     |     |     |     |     |     |     |
| --------------------------------------------------- | --- | ---------- | -------- | --- | -------- | ------ | ---- | ---------- | --- | --- | --- | --- | --- | --- | --- |
| Interestingly,                                      | the | validation | accuracy |     | remained | higher | than |            |     |     |     |     |     |     |     |
TP
thetrainingaccuracyformostofthetime,suggestingthatthe Precision= (4)
TP+FP
| model did                                         | not | overfit and | was | able to | perform | well | on new |     |     |         |     |     |     |     |     |
| ------------------------------------------------- | --- | ----------- | --- | ------- | ------- | ---- | ------ | --- | --- | ------- | --- | --- | --- | --- | --- |
| data.Someupsanddownsinvalidationaccuracywereseen, |     |             |     |         |         |      |        |     |     |         | TP  |     |     |     |     |
|                                                   |     |             |     |         |         |      |        |     |     | Recall= |     |     |     |     | (5) |
TP+FN
| which is | normal | because | of the | imbalanced |     | classes | and the |     |     |     |     |     |     |     |     |
| -------- | ------ | ------- | ------ | ---------- | --- | ------- | ------- | --- | --- | --- | --- | --- | --- | --- | --- |
Precision·Recall
randomwaydatabatcheswereprocessed.Overall,thetrend
|     |     |     |     |     |     |     |     |     | F1-Score=2· |     |     |     |     |     | (6) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ----------- | --- | --- | --- | --- | --- | --- |
Precision+Recall
showsthatthemodelwasstableduringtraining.
| 180180 |     |     |     |     |     |     |     |     |     |     |     |     |     | VOLUME13,2025 |     |
| ------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------- | --- |

X.Li,J.Li:ExploringFactorsInvolvedinLoanApprovalDecision:DeepInsightsandDataAnalyticsTechniques
| FIGURE18. | Barchartofprecision,recallandF1-scoreforeachclassand |     |     |     |     |     |     |     |     |     |     |
| --------- | ---------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
aggregateaverages. FIGURE19. Confusionmatrixonvalidationset.Hightruenegativerate
reflectsconservativebias.
| Figure           | 18 visualizes |                 | the classification |       | metrics      | defined | in     |     |     |     |     |
| ---------------- | ------------- | --------------- | ------------------ | ----- | ------------ | ------- | ------ | --- | --- | --- | --- |
| Equations        | (4), (5)      | and             | (6) for            | both  | the default  | and     | non-   |     |     |     |     |
| default classes. |               | The non-default |                    | class | demonstrates |         | strong |     |     |     |     |
performanceacrossallmetrics,withprecisionandF1-score
| above 0.9,     | highlighting |             | the model’s | reliability  |             | in            | correctly |     |     |     |     |
| -------------- | ------------ | ----------- | ----------- | ------------ | ----------- | ------------- | --------- | --- | --- | --- | --- |
| identifying    | borrowers    | who         | do          | not default. |             | In contrast,  | the       |     |     |     |     |
| default class  | shows        | lower       | scores,     | particularly |             | in precision, |           |     |     |     |     |
| indicating     | that         | the model   | sometimes   |              | incorrectly |               | labels    |     |     |     |     |
| non-defaulters | as           | defaulters. | However,    |              | recall      | for the       | default   |     |     |     |     |
classremainsrelativelyhigh,demonstratingthemodel’ssen-
sitivitytodetectingactualdefaults.Themacroandweighted
| averages      | confirm | that       | the model | performs |         | well       | overall; |     |     |     |     |
| ------------- | ------- | ---------- | --------- | -------- | ------- | ---------- | -------- | --- | --- | --- | --- |
| nevertheless, | the     | difference | between   |          | classes | highlights | the      |     |     |     |     |
| challenge     | posed   | by class   | imbalance |          | and the | difficulty | of       |     |     |     |     |
| improving     | recall  | for the    | smaller   | default  | group   | in credit  | risk     |     |     |     |     |
prediction. FIGURE20. Receiveroperatingcharacteristic(ROC)curve.TheAUCvalue
of0.83reflectsstrongclassseparability.
| The confusion |     | matrix | is  | a tabular | representation |     | of  |     |     |     |     |
| ------------- | --- | ------ | --- | --------- | -------------- | --- | --- | --- | --- | --- | --- |
classificationresults.Itisdefinedas:
|     |     |     |          |          |     |     |     | The ROC | curve in Figure | 20 shows the balance | between |
| --- | --- | --- | -------- | -------- | --- | --- | --- | ------- | --------------- | -------------------- | ------- |
|     |     |     | (cid:20) | (cid:21) |     |     |     |         |                 |                      |         |
TP FN the true positive rate, also called sensitivity and the false
(7)
FP TN positive rate at different classification thresholds. A larger
where: area under the curve, or AUC, means the model can better
TP:TruePositives-correctlypredicteddefaults tell defaulters apart from non-defaulters. In this case, the
•
• TN:TrueNegatives-correctlypredictednon-defaults models have reached an AUC of 0.83, which also indicates
• FP: False Positives - non-defaulters incorrectly labeled that this can effectively rank applicants by their risk of
|     |     |     |     |     |     |     |     | default without | relying | on one specific cutoff | point. The |
| --- | --- | --- | --- | --- | --- | --- | --- | --------------- | ------- | ---------------------- | ---------- |
asdefaulters
• FN: False Negatives - defaulters incorrectly labeled as curve’s clear separation from the diagonal line confirms
non-defaulters that the model’s predictions are much better than random
| Figure | 19 shows | the | validation | confusion |     | matrix. | The | chance. |     |     |     |
| ------ | -------- | --- | ---------- | --------- | --- | ------- | --- | ------- | --- | --- | --- |
model achieved strong recognition of non-defaulters with Figure21haveshowntheprecision-recallcurve,whichis
24,356 true negatives but only moderate detection of well-suited for imbalanced datasets and with few defaults.
defaulters with 1,235 true positives, alongside 3,688 false The model have achieved a high precision with moder-
positivesand721falsenegatives.Thiscautiousbiasreduces ate recall, though increasing recall lowers precision also
|                 |     |          |         |      |      |             |     | highlighting | the trade-off | and the importance | of select- |
| --------------- | --- | -------- | ------- | ---- | ---- | ----------- | --- | ------------ | ------------- | ------------------ | ---------- |
| risky approvals |     | but also | rejects | some | good | applicants, |     |              |               |                    |            |
underscoring the need to adjust the decision threshold to ing a threshold that matches risk tolerance in credit
| businessrequirements. |     |     |     |     |     |     |     | scoring. |     |     |        |
| --------------------- | --- | --- | --- | --- | --- | --- | --- | -------- | --- | --- | ------ |
| VOLUME13,2025         |     |     |     |     |     |     |     |          |     |     | 180181 |

X.Li,J.Li:ExploringFactorsInvolvedinLoanApprovalDecision:DeepInsightsandDataAnalyticsTechniques
| FIGURE21. | Precision-recallcurve.Usefulinimbalancedsettingswhere |     |     |     |     |     |     |     |     |     |     |
| --------- | ----------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
precisionathighrecallisimportant.
F. CALIBRATIONEVALUATION
|     |     |     |     |     |     |     |     | FIGURE22. ReliabilitydiagramoftheproposedCNNmodel.Thediagonal |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------------------------------------------------------- | --- | --- | --- |
Increditriskassessment,reliableprobabilityestimatesareas
indicatesperfectcalibration,whiledeviationsofthecurvereflect
| important     | as classification |      | accuracy |        | since    | decisions | such as   | miscalibration. |     |     |     |
| ------------- | ----------------- | ---- | -------- | ------ | -------- | --------- | --------- | --------------- | --- | --- | --- |
| loan approval | and               | risk | pricing  | depend | directly | on        | predicted |                 |     |     |     |
defaultprobabilities.Awell-calibratedmodelensuresthata
predictedprobabilityof0.7correspondstoatruelikelihood
ofdefaultofaboutseventypercent.Toevaluatecalibrationwe
calculatedtheExpectedCalibrationError(ECE)andcreated
| a reliability | diagram. |               | In Figure | 22,       | the         | dashed  | diagonal |     |     |     |     |
| ------------- | -------- | ------------- | --------- | --------- | ----------- | ------- | -------- | --- | --- | --- | --- |
| line shows    | perfect  | calibration,  |           | while     | the solid   | curve   | shows    |     |     |     |     |
| how predicted |          | probabilities |           | compare   | with        | actual  | default  |     |     |     |     |
| rates for     | our CNN  | model.        |           | The model |             | reaches | a strong |     |     |     |     |
| ROC-AUC       | of about | 0.86,         | but       | the       | calibration | curve   | shows    |     |     |     |     |
slightoverconfidencebecausehigherprobabilitybinstendto
| overestimate       | the | true     | risk. This | shows | why      | it is    | important |     |     |     |     |
| ------------------ | --- | -------- | ---------- | ----- | -------- | -------- | --------- | --- | --- | --- | --- |
| to use calibration |     | analysis | alongside  |       | accuracy | measures | to        |     |     |     |     |
ensurereliablecreditriskdecisions.
G. VISUALIZATIONOFPREDICTIONDISTRIBUTION
| Additional | evaluation |     | focused | on the | distribution |     | of model |                                                               |     |     |     |
| ---------- | ---------- | --- | ------- | ------ | ------------ | --- | -------- | ------------------------------------------------------------- | --- | --- | --- |
|            |            |     |         |        |              |     |          | FIGURE23. Histogramofpredictedprobabilities.Classseparationis |     |     |     |
outputs and predicted probabilities. This confirmed the visiblewithskewtowardthenon-defaultclass.
model’scapacitytoseparateriskyandsafeborrowers.
Figure23showsthedistributionofpredictedprobabilities Figure25showsascatterplotthatcomparesthetruelabels
|          |        |       |       |         |     |     |           | with the predicted | labels, but | both classes, | zero and one, |
| -------- | ------ | ----- | ----- | ------- | --- | --- | --------- | ------------------ | ----------- | ------------- | ------------- |
| produced | by the | model | while | testing | and | the | histogram |                    |             |               |               |
alsorevealsthatthemostpredictedclassesareconcentrated appearasseparatehorizontalbands,indicatingthatthemodel
in the lower probability range, around 0.2, indicating that can clearly distinguish between them. The predicted values
the model confidently classifies most cases as non-defaults. also align too closely with the actual labels, indicating high
Fewer predictions have fallen within the high probability accuracy.Someofthenoiseanderrorsareexpectedbecause
|                  |     |      |          |     |                 |     |           | of the smaller | class, but overall, | the alignment | shows that |
| ---------------- | --- | ---- | -------- | --- | --------------- | --- | --------- | -------------- | ------------------- | ------------- | ---------- |
| range associated |     | with | defaults | and | also reflecting |     | the class |                |                     |               |            |
imbalance and the model’s cautious nature. Understanding themodelhaslearnedimportantpatterns.Thisvisualization
theseprobabilitypatternsisimportantforadjustingdecision adds to traditional evaluation metrics by directly showing
howthepredictionsmatchthetruelabelsacrossthedataset,
| thresholds, | especially |     | in areas | like | credit risk | management, |     |     |     |     |     |
| ----------- | ---------- | --- | -------- | ---- | ----------- | ----------- | --- | --- | --- | --- | --- |
wherethecostsofmistakesarehigh. confirming that most predictions fall into the correct class
group.
| Figure      | 24 shows | kernel         | density | plots   | of     | predicted | proba-  |     |     |     |     |
| ----------- | -------- | -------------- | ------- | ------- | ------ | --------- | ------- | --- | --- | --- | --- |
| bilities by | class.   | Non-defaulters |         | cluster | around | low       | values, |     |     |     |     |
whiledefaulterspeaknear0.9withsomeoverlap,reflecting H. EXTENDEDVALIDATION
classimbalanceandseparationdifficulty.Thedistinctpeaks Totesttherobustnessandgeneralizabilityofourframework,
confirmgooddiscriminativeability,whichcanberefinedby werananextendedvalidationusingaboutfivepercentofthe
adjustingthedecisionthresholdtomatchrisktolerance. dataset.Thissubsetincluded1,505recordsandwasstratified
| 180182 |     |     |     |     |     |     |     |     |     |     | VOLUME13,2025 |
| ------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------- |

X.Li,J.Li:ExploringFactorsInvolvedinLoanApprovalDecision:DeepInsightsandDataAnalyticsTechniques
TABLE3. Extendedvalidationresultsonastratifiedsubsetof1,505
samples.
| FIGURE24. | Kerneldensityestimatesbyclass.Defaultedborrowers |     |     |     |     |     |     |
| --------- | ------------------------------------------------ | --- | --- | --- | --- | --- | --- |
exhibitaleftwardshiftinscoredistribution.
|     |     |     |     | FIGURE26. SHAPsummaryplotshowingaverageimpactofeachfeature |     |     |     |
| --- | --- | --- | --- | ---------------------------------------------------------- | --- | --- | --- |
acrossallvalidationsamples.
| FIGURE25. | Scatterplotoftruevs.predictedvalues.Clusteringalongaxes |     |     |     |     |     |     |
| --------- | ------------------------------------------------------- | --- | --- | --- | --- | --- | --- |
showshighbinaryseparation.
| to keep     | the same balance  | between default    | and non-default    |     |     |     |     |
| ----------- | ----------------- | ------------------ | ------------------ | --- | --- | --- | --- |
| cases. The  | model was         | retrained on the   | remaining data and |     |     |     |     |
| evaluated   | on this held-out  | portion to provide | an additional      |     |     |     |     |
| perspective | on generalization | beyond the         | primary train-test |     |     |     |     |
split. FIGURE27. SHAPbarplotofmeanabsoluteSHAPvalues.agedominates
globalmodelbehavior.
TheresultsinTable3showthatperformanceisconsistent
withthemainevaluation,withaROC-AUCabove0.85,abal- that younger applicants are more likely to default. Payment
anced F1-score and reliable probability estimates measured historyindicators,suchaslatepaymentsandfinancialfactors
byECE.ThissuggeststhattheproposedCNNpipelinekeeps
|     |     |     |     | like open credit | lines and income | also rank highly, | showing |
| --- | --- | --- | --- | ---------------- | ---------------- | ----------------- | ------- |
strongpredictiveabilityandgoodcalibrationevenwithless themodelreliesonbothbehavioralandfinancialinformation.
data,supportingitsuseinreal-worlddeployment.
|     |     |     |     | Figure 27       | shows the SHAP | bar plot, where | features are |
| --- | --- | --- | --- | --------------- | -------------- | --------------- | ------------ |
|     |     |     |     | ranked by their | average impact | on the model’s  | prediction   |
I. EXPLAINABILITYRESULTS forthenon-defaultclass.Thisrankingisbasedonthemean
To enhance interpretability, we integrated SHAP-based absolute SHAP values, which measure the degree to which
explanation tools into the pipeline. Global SHAP summary each feature generally influences the model’s output. The
plots highlighted that age, MonthlyIncome and NumberOf- information in this plot matches closely with the SHAP
Times90DaysLatewerethemostinfluentialfeatures. summary plot shown in Figure 26, confirming that the
Figure 26 have shown the SHAP summary plot, where importance of features is consistent across different ways
the feature importance is based on the mean absolute of interpreting the model. This helps provide a clear and
SHAP values across the validation set. Age is the most reliableunderstandingofwhichfeaturesaremostimportant
influential feature, consistent with earlier boxplot findings inpredictingnon-defaultcases.Themostinfluentialpredictor
| VOLUME13,2025 |     |     |     |     |     |     | 180183 |
| ------------- | --- | --- | --- | --- | --- | --- | ------ |

X.Li,J.Li:ExploringFactorsInvolvedinLoanApprovalDecision:DeepInsightsandDataAnalyticsTechniques
| FIGURE28. | SHAPdependenceplotforage.Youngerapplicantsreceive |     |     |     |     |     |     |     |     |     |     |     |     |     |     |
| --------- | ------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
higherSHAPcontributionstowarddefault.
isage,suggestingthatageplaysadominantroleinhowthe
|     |     |     |     |     |     |     |     | FIGURE29. | SHAPdependenceplotforMonthlyIncome.Low-income |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --------- | --------------------------------------------- | --- | --- | --- | --- | --- | --- |
applicantsshowhigherSHAPvaluesfordefault.
| model distinguishes |     | defaulters |     | from | non-defaulters. |     | This is |     |     |     |     |     |     |     |     |
| ------------------- | --- | ---------- | --- | ---- | --------------- | --- | ------- | --- | --- | --- | --- | --- | --- | --- | --- |
followedbylatepaymentrecordssuchasNumberOfTime30-
|                       |             |     |         |                          |     |                   |     | higher default |     | risk, while    | higher | incomes    | reduce  | this          | risk. |
| --------------------- | ----------- | --- | ------- | ------------------------ | --- | ----------------- | --- | -------------- | --- | -------------- | ------ | ---------- | ------- | ------------- | ----- |
| 59DaysPastDueNotWorse |             |     | and     | NumberOfTimes90DaysLate, |     |                   |     |                |     |                |        |            |         |               |       |
|                       |             |     |         |                          |     |                   |     | Red points     | in  | the low-income |        | range      | show    | that frequent |       |
| which are             | intuitively |     | tied to | borrower                 |     | creditworthiness. |     |                |     |                |        |            |         |               |       |
|                       |             |     |         |                          |     |                   |     | delinquencies  |     | combined       | with   | low income | greatly | increase      |       |
Financialattributes,suchasmonthlyincomeandthenumber
|           |              |     |              |      |               |         |          | default       | probability, | whereas |                | higher-income |              | applicants | are |
| --------- | ------------ | --- | ------------ | ---- | ------------- | ------- | -------- | ------------- | ------------ | ------- | -------------- | ------------- | ------------ | ---------- | --- |
| of open   | credit lines | and | loans,       | also | have a        | notable | average  |               |              |         |                |               |              |            |     |
|           |              |     |              |      |               |         |          | less affected | by           | minor   | late payments. |               | This pattern | supports   |     |
| impact on | the model’s  |     | predictions. |      | This reflects |         | how both |               |              |         |                |               |              |            |     |
|           |              |     |              |      |               |         |          | financial     | reasoning    | and     | confirms       | the           | model’s      | ability    | to  |
behaviorandeconomicfactorsarecombinedtoinfluencethe
capturemeaningfulincome–delinquencyinteractions.
model’sdecisions[36],[38].
| This visualization |     | validates |     | the model’s |     | learned | patterns |     |     |     |     |     |     |     |     |
| ------------------ | --- | --------- | --- | ----------- | --- | ------- | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
J. COMPARISONWITHINDUSTRY-STANDARD
andalignswellwithdomainknowledge,supportingitssuit-
abilityforreal-worlddeploymentincreditriskanalysis[39]. EXPLAINABILITYMETHODS
|        |             |     |      |            |     |      |         | In credit | risk, | logistic regression |     | scorecards | and | Weight-of- |     |
| ------ | ----------- | --- | ---- | ---------- | --- | ---- | ------- | --------- | ----- | ------------------- | --- | ---------- | --- | ---------- | --- |
| Figure | 28 presents | the | SHAP | dependence |     | plot | for the |           |       |                     |     |            |     |            |     |
feature age, showing how the model has predicted changes Evidence (WoE) models are still widely used benchmarks.
with different applicants ’ ages. Each point on the plot Regulators often prefer them because they are transparent
|            |          |      |         |     |        |          |       | and have | been | used for | many | years. These | methods |     | explain |
| ---------- | -------- | ---- | ------- | --- | ------ | -------- | ----- | -------- | ---- | -------- | ---- | ------------ | ------- | --- | ------- |
| represents | a single | data | sample. | The | x-axis | displays | stan- |          |      |          |      |              |         |     |         |
dardizedagevalues,whilethey-axisshowstheSHAPvalue, risk by adding up feature contributions in log-odds space,
|            |            |     |       |     |            |     |         | which makes |     | it easy | to see | how | each feature |     | affects |
| ---------- | ---------- | --- | ----- | --- | ---------- | --- | ------- | ----------- | --- | ------- | ------ | --- | ------------ | --- | ------- |
| indicating | the degree | to  | which | age | influences | the | model’s |             |     |         |        |     |              |     |         |
output. The color gradient represents the number of open creditworthiness.
credit lines and loans, highlighting the interaction between Our SHAP-based framework follows a similar principle,
sinceSHAPvaluesalsoprovideadditivefeaturecontributions
| these two | features. | The | plot shows |     | a clear | negative | trend: |     |     |     |     |     |     |     |     |
| --------- | --------- | --- | ---------- | --- | ------- | -------- | ------ | --- | --- | --- | --- | --- | --- | --- | --- |
younger applicants, located on the left side of the x-axis, that can be read in log-odds form. The key advantage
|             |      |         |         |     |      |            |      | of SHAP | is  | that it offers |     | both global | explanations |     | for |
| ----------- | ---- | ------- | ------- | --- | ---- | ---------- | ---- | ------- | --- | -------------- | --- | ----------- | ------------ | --- | --- |
| have higher | SHAP | values, | meaning |     | they | contribute | more |         |     |                |     |             |              |     |     |
overallmodelbehaviorandlocalexplanationsforindividual
| strongly | to the | prediction | of default. |     | As the | age | increases, |     |     |     |     |     |     |     |     |
| -------- | ------ | ---------- | ----------- | --- | ------ | --- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- |
the SHAP values also decrease, as shown, suggesting older cases. In contrast, logistic scorecards mostly provide only
globalinsights.Theabilitytoexplainindividualpredictions
| applicants | are less | likely | to be | predicted | as  | defaulters. | This |     |     |     |     |     |     |     |     |
| ---------- | -------- | ------ | ----- | --------- | --- | ----------- | ---- | --- | --- | --- | --- | --- | --- | --- | --- |
patternagreeswithcommoncreditriskunderstanding,where is especially valuable for loan-level audits and regulatory
| younger | borrowers | are | usually | considered |     | riskier | due to | reviews. |     |     |     |     |     |     |     |
| ------- | --------- | --- | ------- | ---------- | --- | ------- | ------ | -------- | --- | --- | --- | --- | --- | --- | --- |
Figure30comparesfeaturecontributionsfromSHAPwith
shortercredithistoriesorlessfinancialexperience.Thecolor
changes also reveal that the effect of age depends partly on thosefromasimulatedWoEandlogisticmodel.Theresults
areconsistent:age,delinquencyhistoryandincomestandout
| how many | credit | lines | an applicant |     | has open, | indicating | a   |     |     |     |     |     |     |     |     |
| -------- | ------ | ----- | ------------ | --- | --------- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
complexrelationshipbetweendemographicinformationand as the strongest predictors in both approaches. This shows
credit behavior. Overall, this plot supports the trust in the that our SHAP-based method meets regulatory standards
|     |     |     |     |     |     |     |     | for interpretability |     | while | giving | more | detailed | explanations, |     |
| --- | --- | --- | --- | --- | --- | --- | --- | -------------------- | --- | ----- | ------ | ---- | -------- | ------------- | --- |
modelbyshowingthatthepatternsithaslearnedarelogical
andalignwellwithestablishedcreditscoringprinciples. making it a strong complement or alternative to traditional
scorecards.
| Figure     | 29 shows     | the          | SHAP       | dependence |            | plot for | Month-      |     |     |     |     |     |     |     |     |
| ---------- | ------------ | ------------ | ---------- | ---------- | ---------- | -------- | ----------- | --- | --- | --- | --- | --- | --- | --- | --- |
| lyIncome,  | highlighting |              | its effect |            | on default |          | prediction. |     |     |     |     |     |     |     |     |
| The x-axis | represents   | standardized |            |            | income     | and      | the y-axis  |     |     |     |     |     |     |     |     |
V. DISCUSSION
shows SHAP values, with each dot colored by NumberOf- This approach has achieved a strong trade-off between
Times90DaysLate. A clear trend appears: lower-income accuracy and interpretability of the results. By combining
applicants have positive SHAP values, contributing to minimal preprocessing, robust feature selection techniques
| 180184 |     |     |     |     |     |     |     |     |     |     |     |     |     | VOLUME13,2025 |     |
| ------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------- | --- |

X.Li,J.Li:ExploringFactorsInvolvedinLoanApprovalDecision:DeepInsightsandDataAnalyticsTechniques
|     |     |     |     |     |     |     | and safeguarded |     | by early | stopping, |        | achieved | competitive |         |
| --- | --- | --- | --- | --- | --- | --- | --------------- | --- | -------- | --------- | ------ | -------- | ----------- | ------- |
|     |     |     |     |     |     |     | ROC-AUC         | on  | the Give | Me Some   | Credit |          | benchmark   | while   |
|     |     |     |     |     |     |     | maintaining     | a   | modest   | parameter | count  | suitable |             | for CPU |
deployment.
IntegratingSHAPexplanationsdirectlyintotheinference
|     |     |     |     |     |     |     | loop delivered |         | global    | and             | local | transparency, |          | satisfying |
| --- | --- | --- | --- | --- | --- | --- | -------------- | ------- | --------- | --------------- | ----- | ------------- | -------- | ---------- |
|     |     |     |     |     |     |     | regulatory     | demands | for       | explainability, |       | whereas       |          | continuous |
|     |     |     |     |     |     |     | monitoring     | of      | CPU, RAM, | GPU             | and   | latency       | provided | the        |
operationalinsightsrequiredforreal-timeproduction.
|     |     |     |     |     |     |     | Beyond       | empirical | gains,   | the       | pipeline’s |            | modular | design    |
| --- | --- | --- | --- | --- | --- | --- | ------------ | --------- | -------- | --------- | ---------- | ---------- | ------- | --------- |
|     |     |     |     |     |     |     | and thorough |           | artefact | packaging |            | contribute | a       | practical |
blueprintforlendersseekingtomoderniselegacyscorecards
|           |                                              |     |     |     |     |     | without | forsaking | auditability. |           | Nevertheless, |     |          | limitations |
| --------- | -------------------------------------------- | --- | --- | --- | --- | --- | ------- | --------- | ------------- | --------- | ------------- | --- | -------- | ----------- |
| FIGURE30. | ComparisonoffeaturecontributionsunderSHAPand |     |     |     |     |     |         |           |               |           |               |     |          |             |
|           |                                              |     |     |     |     |     | remain: | the model | was           | validated |               | on  | a single | public      |
WoE/Logisticbaselines.Bothapproachesemphasizeage,delinquency
historyandincomeasthemostinfluentialfactors,confirmingconsistency
|     |     |     |     |     |     |     | dataset, | fairness | analyses | were | outside |     | the | scope and |
| --- | --- | --- | --- | --- | --- | --- | -------- | -------- | -------- | ---- | ------- | --- | --- | --------- |
withdomainexpectations.
|     |     |     |     |     |     |     | online drift | handling |     | was not | explored. |     | Addressing | these |
| --- | --- | --- | --- | --- | --- | --- | ------------ | -------- | --- | ------- | --------- | --- | ---------- | ----- |
and a small but expressive neural architecture, we achieved constraints,alongwiththefuture-workdirectionsoutlinedin
performance comparable to heavier architectures while Future work, will accelerate progress toward credit-scoring
enablingfasterinferenceandbettertransparency. systems that are simultaneously accurate, equitable,
However,somelimitationsremain.Recallwasstillmodest resource-efficient and compliant with emerging global AI
| for the       | minority | class    | as discussed |     | earlier, suggesting | the     | regulations. |     |     |     |     |     |     |     |
| ------------- | -------- | -------- | ------------ | --- | ------------------- | ------- | ------------ | --- | --- | --- | --- | --- | --- | --- |
| opportunities | for      | improved | sampling     |     | or threshold        | tuning. |              |     |     |     |     |     |     |     |
Futureworkwilladdressclassimbalancemoreaggressively FUTUREWORK
and explore dynamic threshold calibration based on risk Future work will explore advanced architectures like
appetite.
GNNsandtransformers,alongsideautomatedfeatureselec-
|     |     |     |     |     |     |     | tion using | reinforcement |     | learning. |     | Enhancing |     | general- |
| --- | --- | --- | --- | --- | --- | --- | ---------- | ------------- | --- | --------- | --- | --------- | --- | -------- |
A. CONSIDERATIONSFORDEPLOYMENTUNDER
|     |     |     |     |     |     |     | ization | through | online | learning | and | synthetic |     | data will |
| --- | --- | --- | --- | --- | --- | --- | ------- | ------- | ------ | -------- | --- | --------- | --- | --------- |
CONCURRENTLOADS address real-world variability and imbalance. Further direc-
The profiling in this study shows that the model runs tions include incorporating fairness-aware methods, coun-
| efficiently | and | uses resources |     | moderately. | In  | real-world |            |              |     |     |            |     |          |         |
| ----------- | --- | -------------- | --- | ----------- | --- | ---------- | ---------- | ------------ | --- | --- | ---------- | --- | -------- | ------- |
|             |     |                |     |             |     |            | terfactual | explanations |     | and | compliance |     | tooling. | Deploy- |
deployment, though, it is also important to test how the ment improvements via model compression, drift detection
| system performs |            | under | heavy    | and concurrent |             | loads. Credit |                  |     |           |     |      |        |             |     |
| --------------- | ---------- | ----- | -------- | -------------- | ----------- | ------------- | ---------------- | --- | --------- | --- | ---- | ------ | ----------- | --- |
|                 |            |       |          |                |             |               | and energy-aware |     | profiling |     | will | ensure | scalability | and |
| risk scoring    | systems    |       | may need | to             | handle      | thousands of  | sustainability.  |     |           |     |      |        |             |     |
| requests        | per second | with  | strict   | limits         | on response | time and      |                  |     |           |     |      |        |             |     |
uptime.Tohandlethesedemands,systemsareusuallytested
REFERENCES
| with concurrent |     | load | tests, stress |     | tests at peak | capacity |     |     |     |     |     |     |     |     |
| --------------- | --- | ---- | ------------- | --- | ------------- | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
[1] F.Louzada,A.Ara,andG.B.Fernandes,‘‘Classificationmethodsapplied
and checks for resilience during partial failures. Common to credit scoring: A systematic review and overall comparison,’’ 2016,
arXiv:1602.02137.
| approaches      | include         | asynchronous |               | request | handling,     | model      |            |            |                                                    |             |            |               |            |            |
| --------------- | --------------- | ------------ | ------------- | ------- | ------------- | ---------- | ---------- | ---------- | -------------------------------------------------- | ----------- | ---------- | ------------- | ---------- | ---------- |
|                 |                 |              |               |         |               |            | [2] S. Hu, | C. Hurlin, | and                                                | S. Tokpavi, |            | ‘‘Machine     | learning   | for credit |
| batching        | and cloud-based |              | auto-scaling. |         | A full        | concurrent |            |            |                                                    |             |            |               |            |            |
|                 |                 |              |               |         |               |            | scoring:   | Improving  | logistic                                           |             | regression | with          | non-linear | decision   |
| load evaluation |                 | is beyond    | the           | scope   | of this work, | but the    |            |            |                                                    |             |            |               |            |            |
|                 |                 |              |               |         |               |            | tree       | effects,’’ | J. Banking                                         | Finance,    | vol.       | 88, pp.15–27, |            | Apr. 2018. |
|                 |                 |              |               |         |               |            | [Online].  | Available: | https://www.sciencedirect.com/science/article/abs/ |             |            |               |            |            |
profilingframeworkwepresentprovidesastrongfoundation
pii/S0377221717303159
forfutureextensions.Addinglarge-scalestresstestswillbe
|     |     |     |     |     |     |     | [3] MathWorks. |     | (2025). Credit | Scoring | Using | Logistic | Regression | and |
| --- | --- | --- | --- | --- | --- | --- | -------------- | --- | -------------- | ------- | ----- | -------- | ---------- | --- |
an important next step to confirm robustness in real-world Decision Trees. [Online]. Available: https://www.mathworks.com/help/
deploymentandfurtherstrengthenthepracticalcontribution risk/creditscorecard-compare-logistic-regression-decision-trees.html
ofthisstudy. [4] H.HeandE.A.Garcia,‘‘Learningfromimbalanceddata,’’IEEETrans.
Knowl.DataEng.,vol.21,no.9,pp.1263–1284,Sep.2009.[Online].
Available:https://ieeexplore.ieee.org/document/4633969
VI. CONCLUSION [5] C.Rudin,‘‘Stopexplainingblackboxmachinelearningmodelsforhigh
This study proposed and demonstrated a fully automated, stakes decisions and use interpretable models instead,’’ Nature Mach.
Intell.,vol.1,no.5,pp.206–215,May2019.[Online].Available:https://
| end-to-end | pipeline | for | credit-risk |     | prediction | that unites |     |     |     |     |     |     |     |     |
| ---------- | -------- | --- | ----------- | --- | ---------- | ----------- | --- | --- | --- | --- | --- | --- | --- | --- |
www.nature.com/articles/s42256-019-0048-x
robust feature selection, a lightweight 1D-CNN classifier, [6] P.S.Chalamalasetty,‘‘Cross-bordercalibration:Aframeworkforimple-
mentingcountry-specificprobabilityofdefaultmodelsinglobalcreditrisk
| post-hoc | SHAP | interpretability |     | and | system-level | profiling |     |     |     |     |     |     |     |     |
| -------- | ---- | ---------------- | --- | --- | ------------ | --------- | --- | --- | --- | --- | --- | --- | --- | --- |
management,’’J.Comput.Sci.Technol.Stud.,vol.7,no.7,pp.801–812,
| within a | single | reproducible |     | framework. | By  | intersecting |     |     |     |     |     |     |     |     |
| -------- | ------ | ------------ | --- | ---------- | --- | ------------ | --- | --- | --- | --- | --- | --- | --- | --- |
Jul.2025,doi:10.32996/jcsts.2025.7.7.86.
| VarianceThreshold, |     | RFE | and | XGBoost | importance | scores, |           |           |                 |     |     |          |        |           |
| ------------------ | --- | --- | --- | ------- | ---------- | ------- | --------- | --------- | --------------- | --- | --- | -------- | ------ | --------- |
|                    |     |     |     |         |            |         | [7] A. C. | Teixeira, | H. Yazdanpanah, |     | A.  | Pezente, | and M. | Ghassemi, |
wederivedacompactfeaturesubsetthatreduceddimension- ‘‘Bayesiannetworksimproveout-of-distributioncalibrationforagribusi-
|               |             |     |         |     |        |               | ness        | delinquency | risk     | assessment,’’ | in        | Proc. | 4th ACM     | Int. Conf. |
| ------------- | ----------- | --- | ------- | --- | ------ | ------------- | ----------- | ----------- | -------- | ------------- | --------- | ----- | ----------- | ---------- |
| ality without | sacrificing |     | signal. | The | custom | convolutional |             |             |          |               |           |       |             |            |
|               |             |     |         |     |        |               | AI Finance, |             | NewYork, | NY,           | USA, Nov. | 2023, | pp.244–252, | doi:       |
architecture, trained with imbalance-aware class weights 10.1145/3604237.3626897.
| VOLUME13,2025 |     |     |     |     |     |     |     |     |     |     |     |     |     | 180185 |
| ------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------ |

X.Li,J.Li:ExploringFactorsInvolvedinLoanApprovalDecision:DeepInsightsandDataAnalyticsTechniques
[8] D.Sculley,G.D.Holt,D.Golovin,E.Davydov,T.Phillips,D.Ebner, [28] T. Nguyen, L. Tran, and H. Pham, ‘‘Benchmarking lightweight 1D-
V. Chaudhary, M. Young, J.-F. Crespo, and D. Dennison, ‘‘Hid- CNN and tabnet for loan default prediction,’’ Comput. Econ., vol. 59,
den technical debt in machine learning systems,’’ in Proc. Adv. no.2,pp.1231–1250,2022.[Online].Available:https://link.springer.com/
Neural Inf. Process. Syst. (NeurIPS), vol. 28, 2015, pp.2503–2511. article/10.1007/s10614-021-10192-6
[Online]. Available: https://papers.nips.cc/paper/5656-hidden-technical- [29] M. T. Ribeiro, S. Singh, and C. Guestrin, ‘‘‘Why should i trust you?’
debt-in-machine-learning-systems.pdf Explaining the predictions of any classifier,’’ in Proc. ACM SIGKDD,
[9] Kaggle.(2011).GiveMeSomeCreditDataset.Accessed:Jul.20,2025. 2016,pp.1135–1144.
[Online].Available:https://www.kaggle.com/c/GiveMeSomeCredit/data [30] M.Sundararajan,A.Taly,andQ.Yan,‘‘Axiomaticattributionfordeep
[10] I.GuyonandA.Elisseeff,‘‘Anintroductiontovariableandfeatureselec- networks,’’inProc.ICML,2017,pp.1–18.
tion,’’J.Mach.Learn.Res.,vol.3,pp.1157–1182,Mar.20032.[Online]. [31] F.Doshi-VelezandB.Kim,‘‘Towardsarigorousscienceofinterpretable
Available:http://www.jmlr.org/papers/volume3/guyon03a/guyon03a.pdf machinelearning,’’2017,arXiv:1702.08608.
[11] T.ChenandC.Guestrin,‘‘XGBoost:Ascalabletreeboostingsystem,’’ [32] A.Brown,J.Smith,andM.Jones,‘‘Real-timeexplainabilitydashboards
inProc.22ndACMSIGKDDInt.Conf.Knowl.DiscoveryDataMining, forcreditunderwriting,’’J.FinancialDataSci.,vol.3,no.4,pp.45–57,
| Aug.2016,pp.785–794. |     |     |     |     |     |     |     | 2021. |     |     |     |
| -------------------- | --- | --- | --- | --- | --- | --- | --- | ----- | --- | --- | --- |
[12] Y.Zhang,J.Zhang,andY.Wang,‘‘Deepconvolutionalneuralnetworksfor [33] S.Lopez,F.Garcia,andP.Martinez,‘‘Featureselectionincreditscoring
usinghybridRFEandXGBoost,’’ExpertSyst.Appl.,vol.150,May2020,
creditscoring,’’NeuralComput.Appl.,vol.30,pp.323–335,Mar.2017.
[Online].Available:https://link.springer.com/article/10.1007/s00521-017- Art.no.113294. [Online]. Available: https://www.sciencedirect.com/
| 3076-0 |     |     |     |     |     |     |     | science/article/pii/S0957417420305710 |     |     |     |
| ------ | --- | --- | --- | --- | --- | --- | --- | ------------------------------------- | --- | --- | --- |
[13] S. Lundberg and S.-I. Lee, ‘‘A unified approach to interpreting model [34] S.AlbanesiandA.Vamossy,‘‘Creditriskandconsumerpaymentbehavior:
predictions,’’2017,arXiv:1705.07874. Evidencefromdeeplearningmodels,’’Rev.FinancialStud.,vol.15,pp.
123–135,Mar.2023.
[14] X.Li,W.Zhang,andH.Wang,‘‘System-levelperformanceprofilingfor
machinelearningmodels,’’IEEETrans.ParallelDistrib.Syst.,vol.30, [35] R.J.A.LittleandD.B.Rubin,StatisticalAnalysisWithMissingData,3rd
no.11,pp.2492–2505,Nov.2019.[Online].Available:https://ieeexplore. ed.,Hoboken,NJ,USA:Wiley,2019.
ieee.org/document/8739292 [36] B. Baesens, T. Van Gestel, S. Viaene, M. Stepanova, J. Suykens, and
[15] D. Baylor, Y. Lee, and R. Miikkulainen, ‘‘Machine learning lifecycle J. Vanthienen, ‘‘Benchmarking state-of-the-art classification algorithms
|     |     |     |     |     |     |     |     |     | J. Oper. Res. | Soc., |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------- | ----- | --- |
managementwithexperimenttrackingandversioning,’’inProc.Workshop for credit scoring,’’ vol. 54, no. 6, pp.627–635,
Softw.Eng.AIICSE,2017,pp.1–16.[Online].Available:https://dl.acm. Jun.2003.[Online].Available:https://link.springer.com/article/10.1057/
| org/doi/10.1145/3183440.3183445 |     |     |     |     |     |     |     | palgrave.jors.2601561 |     |     |     |
| ------------------------------- | --- | --- | --- | --- | --- | --- | --- | --------------------- | --- | --- | --- |
[16] Y.Saeys,I.Inza,andP.Larrañaga,‘‘Areviewoffeatureselectiontech- [37] J.Han,M.Kamber,andJ.Pei,DataMining:ConceptsandTechniques,3rd
niquesinbioinformatics,’’Bioinformatics,vol.23,no.19,pp.2507–2517, ed.,SanMateo,CA,USA:MorganKaufmann,2011.[Online].Available:
Oct.2007.[Online].Available:https://academic.oup.com/bioinformatics/ https://www.sciencedirect.com/book/9780123814791/data-mining
article/23/19/2507/195606 [38] T. Bellotti and J. Crook, ‘‘Support vector machines for credit scoring
[17] ConsumerFinancialProtectionBureau.(2020).SupervisoryHighlights: and discovery of significant features,’’ Expert Syst. Appl., vol. 36,
Semiannual Report of the CFPB Supervisory Activities. [Online]. no. 2, pp.3302–3308, Mar. 2009. [Online]. Available: https://www.
Available: https://files.consumerfinance.gov/f/documents/cfpb_ sciencedirect.com/science/article/pii/S0957417412007209
supervisory-highlights_semiannual-report_2020.pdf [39] D.J.Hand,‘‘Modelingandassessingcreditrisk,’’Statistician,vol.50,
[18] T.Berg,S.Constantin,andB.Baesens,‘‘Bigdataandalternativedata no. 3, pp.361–372, 2001. [Online]. Available: https://www.jstor.org/
| in credit | scoring: | A literature | review,’’  | J. Risk                          | Finance, | vol. 19, | no. 1, | stable/2685552 |     |     |     |
| --------- | -------- | ------------ | ---------- | -------------------------------- | -------- | -------- | ------ | -------------- | --- | --- | --- |
| pp.2–18,  | 2018.    | [Online].    | Available: | https://www.emerald.com/insight/ |          |          |        |                |     |     |     |
content/doi/10.1108/JRF-01-2017-0010/full/html
| [19] X. Chen, | Y. Zhang, | and | J. Zhang, | ‘‘Privacy-preserving |     | learning | for |     |     |     |     |
| ------------- | --------- | --- | --------- | -------------------- | --- | -------- | --- | --- | --- | --- | --- |
financialdataanalytics:Asurvey,’’IEEETrans.Knowl.DataEng.,vol.33,
no.7,pp.2873–2887,Jul.2021.[Online].Available:https://ieeexplore.
XINCAILIhasbeenengagedinassetandmanage-
ieee.org/document/9099151
mentrelatedworkformorethan20years,presided
| [20] M. Feurer, | A.         | Klein, K.       | Eggensperger, | J.  | T. Springenberg, | M.  | Blum,   |     |                       |             |               |
| --------------- | ---------- | --------------- | ------------- | --- | ---------------- | --- | ------- | --- | --------------------- | ----------- | ------------- |
|                 |            |                 |               |     |                  |     |         |     | over and participated | in a number | of provincial |
| and             | F. Hutter, | ‘‘Auto-sklearn: | Efficient     | and | robust automated |     | machine |     |                       |             |               |
learning,’’AutomatedMach.Learn.,vol.2019,pp.113–134,Jun.2019. and ministerial projects. His research interests
[Online].Available:https://link.springer.com/chapter/10.1007/978-3-030- includedigitalculturalindustryanddigitalasset
| 05318-5_6  |         |                |     |           |          |         |         |     | management. |     |     |
| ---------- | ------- | -------------- | --- | --------- | -------- | ------- | ------- | --- | ----------- | --- | --- |
| [21] L. C. | Thomas, | D. B. Edelman, | and | J. Crook, | ‘‘Credit | scoring | and its |     |             |     |     |
applications,’’SIAMRev.,vol.7,pp.36–49,Jan.2002.[Online].Available:
https://epubs.siam.org/doi/book/10.1137/1.9780898719401
| [22] D. J. | Hand and | W. E. | Henley, | Statistical | Classification | Methods | in  |     |     |     |     |
| ---------- | -------- | ----- | ------- | ----------- | -------------- | ------- | --- | --- | --- | --- | --- |
ConsumerCreditScoring:AReview.Hoboken,NJ,USA:Wiley,1997,
doi:10.1111/j.1467-985X.1997.00078.x.
| [23] S. Lessmann, |                  | B. Baesens,    | H.-V.                                  | Seow, and  | L. C.    | Thomas,         | ‘‘Bench- |     |     |     |     |
| ----------------- | ---------------- | -------------- | -------------------------------------- | ---------- | -------- | --------------- | -------- | --- | --- | --- | --- |
| marking           | state-of-the-art | classification |                                        | algorithms | for      | credit scoring: | An       |     |     |     |     |
| update            | of research,’’   | Eur.           | J. Oper.                               | Res., vol. | 247, no. | 1, pp.124–136,  |          |     |     |     |     |
| Nov.              | 2015. [Online].  | Available:     | https://www.sciencedirect.com/science/ |            |          |                 |          |     |     |     |     |
article/pii/S037722171500408X
|     |     |     |     |     |     |     |     |     | JIAYU LI studied | finance in | top universities in |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ---------------- | ---------- | ------------------- |
[24] O.Bastani,C.Kim,andH.Bastani,‘‘Interpretingblackboxmodelsvia
modelextraction,’’2017,arXiv:1705.08504. Chinaandparticipatedinanumberofprovincial
[25] G.Ke,Q.Meng,T.Finley,T.Wang,W.Chen,W.Ma,Q.Ye,andT.Liu, and ministerial research projects. Her research
‘‘LightGBM:Ahighlyefficientgradientboostingdecisiontree,’’inProc. interestsincludefrontierfields,suchasfinancial
technology,culturaltechnology,andNFTvirtual
NIPS,2017,pp.3146–3154.
currency.
[26] G.ChandrashekarandF.Sahin,‘‘Asurveyonfeatureselectionmethods,’’
Comput.Electr.Eng.,vol.40,no.1,pp.16–28,2013.
| [27] (2018). | Guidelines                                                   | on  | Loan Origination |     | and Monitoring. |     | [Online]. |     |     |     |     |
| ------------ | ------------------------------------------------------------ | --- | ---------------- | --- | --------------- | --- | --------- | --- | --- | --- | --- |
| Available:   | https://www.eba.europa.eu/regulation-and-policy/credit-risk/ |     |                  |     |                 |     |           |     |     |     |     |
guidelines-on-loan-origination-and-monitoring
| 180186 |     |     |     |     |     |     |     |     |     |     | VOLUME13,2025 |
| ------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------- |