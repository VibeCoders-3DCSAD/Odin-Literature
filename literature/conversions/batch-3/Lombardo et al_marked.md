---
conversion_metadata:
  converted_at: "2026-07-21T14:05:08Z"
  converter_tool: "markitdown"
  converter_version: "0.1.6"
  source_pdf: "Lombardo et al.pdf"
  source_pdf_sha256: "cda2da3dfb9a03885fb459a44bd9de95dba86e73dd57d8b69d3e38079c0e9a41"
  page_count: 24
  markdown_char_count: 164882
---

<!-- PAGE-AWARE EXTRACTION (via pdfminer.six) -->

<!-- PAGE 1 -->

6
2
0
2

y
a
M
6
2

]

G
L
.
s
c
[

2
v
6
1
0
2
2
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

Cost-Sensitive Evaluation for Binary Classifiers

Pierangelo Lombardo1, Antonio Casoli1, Cristian Cingolani2, Shola
Oshodi2, and Michele Zanatta2

1Eutelsat, Paris, France
2Reply, Rome, Italy

Abstract

Selecting an appropriate evaluation metric for classifiers is crucial for model
comparison, parameter optimization, and deployment decisions, yet there is no
consensus on a broadly accepted evaluation paradigm explicitly aligned with
Total Classification Cost (TCC) minimization. At the same time, class imbal-
ance is often treated as a problem to be corrected per se, potentially causing
misalignments with TCC minimization.

To address these limitations, (i) we define Weighted Accuracy (WA), an
evaluation metric for binary classifiers with a straightforward interpretation
as a weighted version of accuracy and (ii) we propose a general reweighting
framework for handling class imbalance in cost-sensitive scenarios, providing an
alternative to resampling techniques. This framework applies to any evalua-
tion metric or loss function that can be expressed as a linear combination of
example-dependent quantities; it enables meaningful comparison of evaluation
results obtained on different datasets and accounts for discrepancies between the
development dataset, used for training, validation, and testing, and the target
dataset, where the model will be deployed. Within this framework, we derive
the conditions under which standard rebalancing techniques remain coherent
with TCC minimization, and when they may instead become misleading.

We prove that, under example-independent Unit Classification Costs, maxi-
mizing WA is equivalent to minimizing TCC. Finally, we analyze the robustness
of WA in realistic example-dependent cost scenarios by studying its correlation
with TCC across a broad range of class imbalance and cost regimes. The results
show that WA maintains robust alignment with TCC across almost all examined
scenarios.

Keywords— Machine Learning, Binary Classification, Imbalanced Dataset, Cost-Sensitive

Learning, Return on Investment, Total Classification Cost, Unit Classification Cost, Weighted
Accuracy, Evaluation Metric, Example-Dependent Cost

1 Introduction

Selecting the evaluation metric for a Machine Learning (ML) use case is a fundamental step,
as it guides the choice of the optimal model and its hyperparameters [14, 34, 42, 15, 31, 36].
However, this task is still complex: numerous metrics exist, and they can rank models in
completely different ways [22], with no consensus on the optimal choice [15, 34, 42, 31,
36, 27]. In classification tasks, model performance is typically described using the confusion
matrix and evaluated using derived metrics such as accuracy, F-measure, Receiver Operating

1

---

<!-- PAGE 2 -->

Characteristic-Area Under the Curve (ROC-AUC), and Cohen’s kappa [15, 34, 38, 36, 27].
Changing the evaluation metric often leads to selecting a different optimal classifier. This is
related to the fact that these metrics implicitly define the Unit Classification Costs (UCCs),
i.e., the cost of classifying an example of class i as class j, in an uncontrolled and potentially
incorrect manner. For example, in binary classification, accuracy implies equal costs for false
positives and false negatives, while ROC-AUC corresponds to variable cost distributions
across classifiers [14].

Moreover, most real-world datasets are moderately or heavily imbalanced: this is com-
mon in domains such as medical diagnosis [21, 37, 19, 23], biochemical forecasting (e.g., pro-
tein sequences, gene expression) [19, 26], image processing [36], intrusion detection [4, 21],
fraud detection (e.g., banking, telecommunications) [21, 37, 19, 23], telecommunications ap-
plications [5, 19], information retrieval [37], and anomaly detection in manufacturing [37].
In such cases, many standard metrics can distort results, making model ranking even more
challenging [5, 26, 38]. Class imbalance is widely recognized as one of the major challenges in
ML research [37, 19, 23, 29] and several approaches have been proposed to mitigate its effects,
including undersampling, oversampling, hybrid sampling strategies (e.g., retaining difficult-
to-learn samples), and Cost-Sensitive Machine Learning (CSML) [6, 8, 4, 5, 37, 11, 30, 23, 40].
CSML involves explicitly defining a cost matrix whose entries are the UCCs, in contrast
with traditional machine learning, where such costs are only implicitly defined through the
evaluation metric. Empirical studies have shown that when UCCs are explicitly estimated,
they often exhibit substantial imbalances across real-world use cases such as medical diag-
nosis [20, 13, 35], bankruptcy prediction [1, 10], loan credit rating [43], cybersecurity [27],
biometric identity recognition [28], consumer credit scoring [28], and database marketing [7].
In business applications, a concept closely tied to the reduction of total cost in machine
learning is Return on Investment (RoI). A similar principle applies in healthcare, where
costs may include not only economic expenses but also health risks or limited availability of
treatments [20, 13, 35].

Within the umbrella of CSML, two distinct research directions exist: (i) studies that
aim to estimate and minimize the Total Classification Cost (TCC) [1, 20, 16, 29], which is
the key for RoI optimization, and (ii) studies that use misclassification costs primarily to
address class imbalance, often with the goal of maximizing specific metrics (e.g., accuracy,
F1, specificity, sensitivity) on a rebalanced dataset [17, 21, 32, 37, 33, 35, 23, 41, 2]; this
second line of research exists because the highest UCC is often associated with misclassifying
the minority class: in such cases, addressing class imbalance may also reduce TCC [29].

However, when the goal is to maximize RoI and minimize TCC, correcting class im-
balance per se may not be beneficial, especially if the minority classes are associated with
misclassification costs comparable to, or lower than, those of the majority classes, and the
class distribution in the target dataset (i.e., the real-world data where the model will be
deployed) is similar to that of the development dataset (used for training, validation, and
testing). Conceptually, the ideal approach to optimize a classifier with the final goal of max-
imizing RoI would be (i) estimating the UCC for each class pair (i, j), and (ii) minimizing
the TCC computed from the UCCs and the confusion matrix. However, this purely cost-
based approach suffers from limitations: (i) estimating UCCs may be challenging; (ii) TCC
depends on the dataset it is measured on, making it unsuitable for comparing classifiers
across datasets; (iii) there is no guarantee that minimizing TCC on the development dataset
will also minimize it on the target dataset; and (iv) in many real-world use cases UCCs
depend on the specific example, challenging the assumptions underlying confusion-matrix-
based evaluation approaches.

Our work provides three main contributions addressing these limitations: (i) as an al-
ternative to existing metrics, we introduce Weighted Accuracy (WA), an evaluation metric
for binary classifiers with a straightforward interpretation as a weighted version of the well-
known accuracy metric, whose maximization we prove to be equivalent to TCC minimization
under example-independent UCCs; (ii) we formalize a reweighting framework for handling

2

---

<!-- PAGE 3 -->

class imbalance in cost-sensitive evaluation scenarios, providing an alternative to rebalanc-
ing techniques; this framework can be applied to any linear example-dependent metric,
formalizes WA as a cost-based reweighted version of standard accuracy, enables consistent
comparison of results obtained on different datasets, and naturally accounts for discrepan-
cies between the class distributions in the development and target datasets; and (iii) we
provide empirical evidence of the robustness of WA by analyzing its correlation with TCC
across diverse example-dependent scenarios, while also studying the validity limits of the
example-independent approximation underlying WA and other confusion-matrix-based eval-
uation methods.

2 Related Work

2.1 Confusion Matrix-Based Metrics

The prediction output of a binary classifier is typically described in terms of a 2×2 confusion
matrix, as shown in Table 1, where TP (TN) denotes the count of true positives (true

Table 1: Confusion matrix N for a binary classifier.

Predicted + Predicted −

Actual +
Actual −

TP
FP

FN
TN

negatives), FP (FN) denotes the count of false positives (false negatives), while P = TP+FN
(N = TN + FP) is the number of positive (negative) examples, and Ntot = P + N the total
number of examples.

A wide range of evaluation metrics, summarized in Table 2, are derived from the con-
fusion matrix, including accuracy, Jaccard’s similarity index, F-measure, recall, precision,
specificity, Negative Predictive Value (NPV), informedness, markedness, Matthews Correla-
tion Coefficient (MCC), Cohen’s Kappa, G-Mean, and ROC-AUC. Despite their widespread
use, each of these metrics has received criticism [14, 38]. To mitigate these issues, various
techniques have been proposed, such as resampling strategies and cost-sensitive learning.
However, resampling may alter the statistical properties of the original dataset, introduce
redundancy, and increase computational cost [7, 37, 11, 29].

Recent work has focused on defining confusion-matrix-based metrics to better handle
class imbalance [11, 30, 31]; table 2 includes several such metrics; among these are Class
Balance Accuracy (CBA) and Imbalance Accuracy Metric (IAM) [30], the P4 metric [38],
Bayesian ROC (B-ROC) curves [4].

In addition, several cost-sensitive metrics have been proposed to explicitly incorporate
misclassification costs; these are also summarized in Table 2 and will be described in Section
2.2.

2.2 Cost-Sensitive Evaluation and Classification Costs

As discussed in Section 1, the ideal strategy for selecting the optimal classifier in a given
use case – particularly when the goal is maximizing the RoI – is to minimize the TCC. In
general, TCC may depend on the specific examples that are misclassified1 [43] and for binary

1For instance, in churn prediction, the cost of a false negative may vary depending on which is

the misclassified customer.

3

---

<!-- PAGE 4 -->

Table 2: Summary of confusion-matrix-based metrics for binary classifiers. Top:
standard metrics; middle: recently introduced metrics; bottom: cost-sensitive metrics.

Name

Formula

Accuracy (A)
Recall (Sensitivity)
Precision
Specificity
NPV
Jaccard’s similarity
F-measure (Fβ )
Informedness
Markedness
MCC
Cohen’s kappa (κ)
G-Mean
ROC-AUC (single param.)1

CBA
IAM
P4
B-ROC (single param.)1

WCA2
WRA
ACD
C-score
MSU
H

Standard CM metrics

(TP + TN)/Ntot
TP/P
TP/(TP + FP)
TN/N
TN/(TN + FN)
TP/(TP + FP + FN)
(1 + β2) · TP/ (cid:2)TP + β2 · P + FP(cid:3)
TP/P − FP/N
TP/(TP + FP) − FN/(TN + FN)
(TP · TN − FP · FN)/(cid:112)(TP + FP) · P · N · (TN + FN)
2 · (TP · TN − FN · FP)/ [(TP + FP) · N + P · (FN + TN)]
(cid:112)TP · TN/(P · N)
(TP/P + TN/N)/2

Recently proposed CM metrics

TP−max(FP,FN)

[TP/ max(P, TP + FP) + TN/ max(N, TN + FN)] /2
2 max(P,TP+FP) + TN−max(FP,FN)
(4 · TP · TN)/ [4 · TP · TN + (TP + TN) · (FP + FN)]
[TP/P + TP/(FP + TP)] /2

2 max(N,TN+FN)

Cost-sensitive metrics

w · TP/P + (1 − w) · TN/N
[4 · (TP/P − FP/N)N · CFP/(P · CFN)] / [1 + N · CFP/(P CFN)]2
(cid:112)(1 − A)2 + (TCC/TCCmax)2
TCC/(P · CFP)
1 − [TCC − TCCmin]/TCCmax

1 − (cid:82) 1

0 dc u(c) TCC(c)/ (cid:82) 1

0 dc u(c) TCCmax(c)

1ROC-AUC and B-ROC are defined for parametric classifiers. For single-parameter classifiers, they
can be computed as the area under the segments connecting the classifier point to (0,0) and (1,1)
in the (TP-rate, FP-rate) or (TP-rate, False Alarm Rate) plane [34].

2In WCA definition, w is the sample importance, which can be identified with CFN/(CFN + CFP).

classification can be defined as

TCC =

(cid:88)

a∈S+

(cid:16)

a δo(a),−1 + dTP
dFN

a δo(a),1

(cid:17)

+

(cid:88)

a∈S−

(cid:16)

a δo(a),−1 + eFP
eTN

a δo(a),1

(cid:17)

,

(1)

where S+ (S−) is the set of positive (negative) examples, dFN
a ) is the UCC for incorrect
(correct) classification of positive example a, eFP
a ) is the UCC for incorrect (correct)
classification of negative example a, o(a) is the classifier output for example a, and δjk is
the Kronecker delta.

(dTP

(eTN

a

a

a = cFP, and eTN

In most literature, UCCs are assumed to be example-independent, i.e., dFN

a = cFN,
dTP
a = cTP, eFP
a = cTN. Under this assumption, the TCC can be expressed
in terms of the confusion matrix: TCC = cTP · TP + cFN · FN + cFP · FP + cTN · TN. To ensure
economic coherence, we require cTP < cFN and cTN < cFP [9] and thus we can simplify the
notation, introducing the shifted UCCs CFN = cFN − cTP and CFP = cFP − cTN, obtaining

TCC = CFN · FN + CFP · FP + TCCmin,

(2)

where TCCmin = cTN · N + cTP · P is the minimum achievable cost, corresponding to perfect
classification.

4

---

<!-- PAGE 5 -->

Several studies have proposed evaluation metrics explicitly depending on TCC, as sum-
marized in Table 2, including Accuracy-Cost-Distance (ACD) [12], Weighted Relative Accu-
racy (WRA) [18], Weighted Classification Accuracy (WCA) [26], and C-score [27], a rescaled
and dimensionless version of the TCC that correctly captures the TCC ranking, albeit its
unbounded nature may pose challenges for interpretability and cross-dataset comparability.
In the context of decision theory, [28] defined Mean Subjective Utility (MSU) as a normal-
ized transformation of the utility matrix; when adapted to the cost formalism adopted in
this work, MSU becomes proportional to TCC and ranges from 1 (minimum TCC) to the
lower bound −TCCmin/TCCmax (maximum TCC), which depends on the dataset and cost
matrix.

Finally, [14] proposed a cost-aware alternative to ROC-AUC for parametric classifiers,
expressing TCC in terms of the UCC ratio c = CFP/(CFP + CFN), distributed according
to a probability density function u(c). The resulting metric is defined in Table 2, where
TCC(c) = b[c FP + (1 − c)FN] and TCCmax(c) = b[c N + (1 − c)P], with b = CFP + CFN.
The H measure can be interpreted as a generalization of MSU, extending it from the edge
case where c is known, to scenarios where it is uncertain. In the limit case in which no prior
information about c is available, [14] propose modeling u(c) using a Beta distribution with
parameters α = β = 2.

Among the existing evaluation metrics, C-score, MSU, and H stand out for their lin-
ear relation with TCC, allowing for model ranking coherent with TCC. However, each has
limitations. C-score, while dimensionless, lacks an upper bound, which can complicate com-
parisons across different datasets, as its magnitude depends on dataset-specific properties,
such as the number of examples and the proportion of actual positives. MSU and H are
normalized within the [0, 1] interval only when TCCmin = 0; if this condition is not met, the
absence of a consistent lower bound may affect interpretability and comparability.

As a better alternative to C-score, MSU, and H, in the next section we propose a weighted
In the case of
version of the well-known accuracy metric, normalized between 0 and 1.
example-independent Unit Classification Costs (UCCs), this metric not only ranks classi-
fiers consistently with the Total Classification Cost (TCC), but also enables performance
comparison across different datasets and supports TCC minimization on the target dataset,
provided that the ratio of positive examples (or the prior probability of a positive outcome)
can be estimated.

3 Weighted Accuracy and Cost-Sensitive Reweight-

ing

3.1 Weighted Accuracy

Accuracy, as defined in Table 2, is a standard performance indicator, widely used to evaluate
classifiers due to its simplicity:
it measures the proportion of correct predictions over the
total number of examples. However, it assumes equal importance for all types of classification
outcomes, deviating from TCC in the presence of unequal misclassification costs, and it is
often considered inappropriate in imbalanced scenarios.

To address these limitations, we define a Weighted Accuracy (WA), which assigns different

importance to positive and negative examples

WA =

w TP + (1 − w)TN
w P + (1 − w)N

,

(3)

where w is the normalized weight assigned to actual positives (true positives and false nega-
tives), and 1−w is the weight assigned to actual negatives (false positives and true negatives).
If we choose the weight w as the UCC ratio, i.e.,

w = rC ,

5

(4)

---

<!-- PAGE 6 -->

with

rC =

CFN
CFN + CFP

,

(5)

then WA becomes linearly related to the TCC defined in Eq. 2; indeed, substituting Eqs. 4
and 5 into Eq. 3, we obtain

WA = 1 −

TCC − TCCmin
TCCmax − TCCmin

,

(6)

where TCCmax = CFNP+CFPN is the maximum possible classification cost. This expression
shows that WA is analogous to the C-score, MSU, and H metrics discussed in Section 2.2,
while providing a more intuitive interpretation and a more consistent normalization scheme.
It also demonstrates that Eq. 3 offers a more principled way to introduce cost-based weighting
into accuracy than, for example, WCA (see Table 2).

Consider a scenario in which the UCC of a false negative is nine times larger than that
associated with a false positive (rC = 0.9), and assume that positive examples constitute 20%
of the dataset. Let M1 denote a classifier that always predicts the negative label, and M2
a classifier characterized by TP = 15, FN = 5, TN = 50, and FP = 30; the corresponding
accuracies are 80% and 65%, respectively, while WA(M1) ≃ 30% and WA(M2) ≃ 71%.

Importantly, the failure of accuracy in this example does not arise because predicting only
the majority class should per se be penalized. Rather, it results from the strong asymmetry in
the UCCs, which makes false negatives substantially more costly than false positives; indeed,
when UCCs are balanced (rC = 0.5), WA coincides with accuracy for any classification
outcome.

For example-independent UCCs, WA with the weight in Eq. 5 ranks confusion matrices in
the exact reverse order of TCC. Therefore, maximizing WA is equivalent to minimizing TCC
and, by extension, maximizing RoI. By construction, WA is normalized to the interval [0, 1]
and is independent of the test set size; this makes it suitable for comparing models evaluated
on different datasets, as long as the class distribution (i.e., P/Ntot) remains the same. In
Sections 3.3 and 3.4, we show how WA can be straightforwardly adapted to compare results
across datasets with different class distributions by appropriately adjusting the weight w.

3.2 Expected Weighted Accuracy

When the value of w cannot be precisely determined, a probabilistic approach may be
adopted: we introduce a probability density function u(w) over the weight w, allowing
us to define the Expected Weighted Accuracy (EWA)

EWA =

(cid:90) 1

0

dw WA(w) u(w).

(7)

Although this formulation shares similarities with the H-measure introduced in [42, 14], it is
not equivalent, since in the H-measure, the integrals of TCC(c) and TCCmax(c) are computed
separately, as shown in Table 2.

Depending on the available information about the cost distribution, u(w) can be modeled
using a Beta distribution (as discussed in Section 2.2), or constructed as a custom distribution
over a plausible range of w values. If the support of u(w) is narrow – e.g., u(w) > 0 only
within a small interval – then EWA can be approximated by WA. For instance, for a narrow
interval [ ¯w − δ, ¯w + δ], we have EWA = WA( ¯w) + O(δ2), which implies that EWA can be
well approximated by evaluating WA at the midpoint ¯w of the interval.

3.3 Handling Class Imbalance through Reweighting

We propose a reweighting approach for handling class imbalance in classifier evaluation that
avoids resampling, thereby preserving the original dataset and its statistical properties.

6

---

<!-- PAGE 7 -->

Consider a generic performance metric that can be expressed as a weighted average:

K =

(cid:80)

a vaka
(cid:80)
a va

,

(8)

where ka is the contribution of example a, va its associated weight, and the sum runs over
all examples in the original set S.

Accuracy and WA are special cases of this formulation, with ka = 1 (0) if example a is

correctly (incorrectly) classified. For accuracy, all examples contribute uniformly:

while WA (defined in Eq. 3) introduces class-dependent weights:

va(accuracy) =

1
Ntot

,

(cid:40)

va(WA) =

w

wP+(1−w)N if a ∈ S+
wP+(1−w)N if a ∈ S−

1−w

.

(9)

(10)

Assume that we wish to estimate the value of K on a balanced version of S containing
the same number of positive and negative examples2. Rather than explicitly constructing
such a dataset through rebalancing techniques, we can equivalently rescale each weight va
according to the relative frequency of its class; after normalization, this procedure yields

vbalanced
a

=

(cid:40) N va

N V++P V−
P va
N V++P V−

if a ∈ S+

if a ∈ S−

,

(11)

where V+ = (cid:80)

a∈S+

va and V− = (cid:80)

a∈S−

va.

This formulation is consistent with previous findings [21, 32, 33, 23, 41]. Although the
focus of this work is on classifier evaluation, the proposed reweighting framework applies to
any metric of the form in Eq. 8, including loss functions (see Section 4.4.1).

In particular, for accuracy, the rebalanced weights become

vbalanced
a

(accuracy) =

(cid:40) 1
if a ∈ S+
2P
1
2N if a ∈ S−

,

(12)

which corresponds to evaluating accuracy on a perfectly balanced dataset.

3.4 Cost-Based Reweighting

We now extend the metric in Eq. 8 to the case of unequal, example-independent UCCs
CFN and CFP; to account for asymmetric UCCs, we introduce a class-dependent reweighting
scheme in which positive and negative examples are weighted proportionally to CFN and
CFP, respectively. After normalization, the transformed weights become

vUCC
a

=

(cid:40)

rC va
rC V++(1−rC )V−
(1−rC )va
rC V++(1−rC )V−

if a ∈ S+

if a ∈ S−

.

(13)

Applying this cost-based reweighting scheme to accuracy yields

vUCC
a

(accuracy) =

(cid:40)

rC

rC P+(1−rC )N if a ∈ S+
rC P+(1−rC )N if a ∈ S−

1−rC

.

(14)

Equation 14 coincides with Eq. 10 when the weight w is defined as in Eq. 4; therefore,
WA can be interpreted as a cost-reweighted version of standard accuracy according to the
proposed framework.

2The generalization to arbitrary class ratios is discussed in Section 3.5.

7

---

<!-- PAGE 8 -->

As discussed in Section 3.1, maximizing WA is equivalent to minimizing TCC in the pres-
ence of example-independent UCCs (see Eq. 6). Comparing the balancing-based reweight-
ing in Eq. 12 with the cost-based reweighting in Eq. 14, we conclude that maximizing
accuracy on a rebalanced dataset is equivalent to minimizing TCC only when 1/(2P) ≃
rC / [rC P + (1 − rC )N], i.e., when

rC ≃

.

(15)

N
Ntot

This condition is implicitly assumed by standard rebalancing techniques and by several
metrics designed to correct class imbalance, yet it does not hold in general; when Eq. 15 is
violated, such approaches may produce substantially misleading evaluations.

3.5 Target Dataset Reweighting

The weighting scheme defined in Eq. 11 aims to correct class imbalance, or equivalently
estimating the metric after positive and negative classes are balanced to the same fraction
of examples. However, for cost-sensitive evaluation, the relevant quantity is the class dis-
tribution in the target dataset, i.e., the dataset on which the classifier will be deployed and
decisions will be made. This could correspond to a production environment in business or
a patient population in healthcare. Let us then distinguish between: (i) the development
dataset, with Ntot examples and ratio of positive examples r+ = P/Ntot, used for training,
validation, and testing and (ii) the target dataset, with Nt
tot examples and ratio of positive
examples rt
+ = Pt/N t
If the target dataset is not directly
accessible, rt
+ can be interpreted as a base rate, i.e., the prior probability of a positive out-
come [27].

tot, which may differ from r+.

To estimate a metric on the target dataset using the development dataset, we generalize

Eq. 11 as:

vt
a =






Rt
+va
+V++Rt
Rt
−va
+V++Rt

Rt

Rt

−V−

−V−

if a ∈ S+

if a ∈ S−

,

(16)

where Rt
the target dataset is perfectly balanced, i.e., if rt

+/r+ and Rt

− = (1 − rt

+ = rt

+ = 0.5.

+)/(1 − r+). As expected, Eq. 16 reduces to Eq. 11 if

This rescaling also enables consistent comparison of metrics calculated across datasets

with different class distributions by mapping them to a common target distribution.

To further extend Eq. 16 to the case of unequal, example-independent UCCs CFN and
CFP, we combine target-distribution reweighting with the cost-based reweighting scheme
introduced in Eq. 13, obtaining

vt,UCC
a

=






Rt

+rC va

−(1−rC )V−

Rt

Rt

+rC V++Rt
Rt
+rC V++Rt

−(1−rC )va

−(1−rC )V−

if a ∈ S+

if a ∈ S−

,

(17)

where rC is defined in Eq. 5.

Equation 17 provides a unified framework to estimate metrics of the form in Eq. 8 while
jointly accounting for unequal UCCs and differences between the class distributions of the
development and target datasets. If misclassification costs are equal (rC = 1/2), it reduces
to Eq. 16; on the other hand, if the class proportion in target and development datasets
coincide (rt

+ = r+), it reduces to Eq. 13.

Applying Eq. 17 to the uniform weights of accuracy (Eq. 9) yields a WA formulation

(Eq. 10) with class weight

wt =

Rt

+rC

Rt

+rC + Rt

−(1 − rC )

.

(18)

Equation 18 determines the WA weight provided that the UCC ratio rC and the ratio of
+ in the target dataset can be estimated. In Appendix A, we describe a procedure

positives rt

8

---

<!-- PAGE 9 -->

to estimate the weight w in the presence of uncertainty in rC . If substantial uncertainty on
w remains after this estimation procedure, the probabilistic approach introduced in Section
3.2 can be adopted.

Finally, Eq. 18 shows that a weighting scheme (or, alternatively, class rebalancing) is

required for accuracy unless

r+ ≃

rt
+rC
+ − rC + 2rt

+rC

1 − rt

(19)

which is therefore the condition under which standard accuracy is equivalent to TCC. If the
target dataset has the same positive rate as the development dataset (rt
+ ≃ r+), Eq. 19
reduces to the equal-UCCs condition (rC ≃ 1/2).

3.6 Example-Dependent Unit Classification Costs

Although most confusion-matrix-based literature assumes that UCCs are example-independent,
in many real-world use cases they actually depend on the individual example a [44, 43]. In
such cases, evaluating the TCC (see Eq. 1) requires specifying the set SFN (SFP) of misclas-
sified positive (negative) examples, rather than simply their count FN (FP). This implies
that the same confusion matrix may correspond to different TCC values depending on which
examples are misclassified.

a

a∈SFN

a + (cid:80)

a − eTN

a = dFN

as EFP
(cid:80)

and DFN
EFP

We can extend the shifted UCCs defined in Section 2.2 to the example-dependent case
a = eFP
a ; this allows us to rewrite Eq. 1 as TCC =
a + (cid:80)
dTP
DFN
is the
minimum achievable cost, corresponding to perfect classification. If we express the UCCs
as DFN
a = CFP + ϵa – where CFN (CFP) is the average cost over
the positives (negatives) of the target dataset3, and δa and ϵa represent example-dependent
deviations – we obtain

a + TCCmin, where TCCmin = (cid:80)

a = CFN + δa and EFP

a − dTP

eTN
a

a∈SFP

a∈S−

a∈S+

TCC = CFN · FN + CFP · FP + TCCmin +

(cid:88)

δa +

(cid:88)

ϵa.

a∈SFN

a∈SFP

(20)

Equation 20 extends Eq. 2 by adding terms that depend on the specific misclassified ex-
amples; Eq. 2 is exact for a given classification outcome only if the averages CFN and CFP are
computed on the subset of misclassified positives and misclassified negatives, respectively.
Since UCCs are typically estimated a priori, without knowing which examples will be mis-
classified, deviations between Eq. 20 and Eq. 2 are therefore expected. For instance, in the
limiting case where a subset of massive examples accounts for most of the TCC, the counts
FN and FP become largely uninformative for determining the TCC, and the dominant fac-
tor is whether these massive examples are correctly classified. In this regime, systematically
analyzed in Section 4.3, the fluctuations terms δa and ϵa become decisive.

In many practical situations, however, the terms (cid:80)

a ϵa are not prominent,
even when the single fluctuations δa or ϵa are comparable to or larger than the averages
CFN and CFP. In Section 4 we illustrate this behavior through two representative use cases,
covering all possible regimes in terms of r+ and rC .

a δa and (cid:80)

4 Empirical Evaluation against Total Classification

Cost

Here, we compare WA, EWA (introduced in Section 3.2), and the metrics described in Table
2, using TCC as a reference in two example-dependent scenarios.

3If these averages are not known for the target dataset, they may be estimated from the devel-

opment dataset.

9

---

<!-- PAGE 10 -->

The TCC is computed according to Eq. 20, while the cost-sensitive metrics WCA, WRA,
ACD, WA, EWA are calculated using average UCCs. The H metric is computed using
a Beta distribution with α = β = 2 for the UCC ratio, as recommended by [14] when
no prior information about the cost distribution is available. H informed and EWA are
computed using a Beta distribution whose mean and variance match those of the empirical
u(c) distribution4. MSU and C-score are not explicitly computed, as they rank classification
outcomes identically to WA, differing only in their normalization schemes.

To quantify the similarity between each metric and TCC, we identify a sample of classi-
fication outcomes and rank them according to the metric and TCC, respectively; hence we
compute the correlation between the two rankings, using:

• the standard Spearman coefficient [39], which corresponds to the Pearson correlation

between rank variables;

• the weighted Spearman coefficient [25, 24], which assigns greater importance to the
correct ordering of top-ranked outcomes, i.e., those with low TCC or high metric
values, which are typically the focus during model selection and validation; for this
coefficient we use an additive weighting scheme and n0 = 2.

4.1 Experimental Setup

Real-world classification problems vary substantially in terms of both the target dataset,
particularly its imbalance ratio, and the UCCs. Two key quantities characterizing each
scenario are the ratio of positive examples r+ and the UCC ratio rC , both ranging in [0, 1].
To systematically explore the full range of possible (rC , r+) scenarios, we construct a discrete
two-dimensional grid over the domain [0, 1] × [0, 1]. For each pair (rC , r+) in the grid, we
generate 100 samples by randomly assigning the positive label (churn) to a subset of P =
round(r+Ntot) examples in each sample. For each sample, we generate Ntot + 1 classification
outcomes by iterating over all possible numbers Ppred of predicted positives and assigning
the Ppred predicted positive labels to a random subset of examples in the sample.

For each metric Y , these outcomes are ranked according to both TCC and Y , generating
two rankings that are compared using the correlation coefficients described above. The
correlations obtained for the 100 samples are then averaged, yielding a mean correlation
value for each metric Y and each point in the (r+, rC ) grid.

The code used to run the experiments and generate the results described in this work
is available at https://github.com/plombardML/weighted-accuracy. Experiments were
conducted on a Windows machine with 16 GB RAM and an Intel(R) Core(TM) i5-102100U
CPU @ 1.60 GHz 2.10 GHz, using Python, the scipy library, and the implementation in [24]
for computing the weighted Spearman coefficient.

4.1.1 Use Cases

To work with data that are as realistic and relatable as possible, we consider two well-
known use cases characterized by example-dependent costs; for each use case, we tune a
cost parameter so that the resulting UCC ratio rC matches the values specified by the grid
described above (see Appendix B).

1. The first use case is churn prediction, where the model predicts whether a customer will
churn within a forthcoming time window. The cost of a false positive includes the time
and effort of the commercial team to contact the customer and implement a retention
measure as well as the cost of that measure. Conversely, the cost of a false negative
depends on the revenue the company would have earned had the customer not churned;

4To approximate the empirical distribution u(c) with a Beta distribution f (c; α, β), we set α =
c − ¯c and β = α(1 − ¯c)/¯c. With this choice, u and f share the same mean ¯c and variance

¯c2(1 − ¯c)/σ2
σ2
c .

10

---

<!-- PAGE 11 -->

this depends on the customer’s revenue and on the probability of effectiveness of the
retention measure. Customer revenues are sampled uniformly and without repetition
from the monthly charges in the Telco Customer Churn dataset from Kaggle5, while
the remaining parameters are estimated as described in Appendix B.1.

2. The second use case is credit scoring, where the model predicts whether a customer will
default on a contracted financial obligation. The cost of a false negative is proportional
to the customer’s debt (credit line). In contrast, the cost of a false positive reflects
the loss of profit from rejecting a customer who would not default; since, in case of
rejection, the institution typically lends to an alternative customer, this cost depends
on the expected average profit and risk of a representative customer. The customers’
monthly income and debt ratio are sampled uniformly and without repetition from the
dataset of the 2011 Kaggle competition Give Me Some Credit 6, while the remaining
parameters are estimated as described in Appendix B.2.

In both use cases, the average UCCs and their fluctuations strongly depend on the pair
(rC , r+). Comparing the standard deviations σδ and σϵ of δa and ϵa with the corresponding
average costs CFN and CFP, we observe substantial variability. For churn prediction, the ratio
σδ/CFN ranges from 0.03 to 47 (median 0.79). For credit scoring, it ranges from 0.0002 to
51 (median 0.16), while σϵ/CFP ranges from 0.005 to 2800 (median 2.38). In many (rC , r+)
scenarios the fluctuations are therefore substantial, and a close agreement between Eq. 2
and Eq. 20 – that is, between WA and the example-dependent TCC – cannot be assumed
a priori. In both cases the target dataset is assumed to be equivalent to the development
dataset in terms of ratio of positives (r+ = rt
+), with the latter containing 200 examples
(Ntot = 200).

4.2 Results

The results of this correlation analysis are shown in Figures 1 and 2 for the standard Spear-
man correlation in the churn prediction and credit scoring use cases, respectively, and in Fig-
ures 3 and 4 for the corresponding weighted Spearman correlation. Several metrics – namely
accuracy, MCC, Kappa, G-mean, ROC-AUC, CBA, IAM, P4, WCA, WRA, ACD, H, H
informed, WA, and EWA exhibit symmetry under relabeling of class + and −, reflected in
the heatmaps as qualitative symmetry under the transformation (r+, rC ) → (1−r+, 1−rC )7.
While symmetry is often considered desirable, our focus here is on robustness of correlation
with TCC. Thus, we classify metrics based on the qualitative pattern of their correlation.

4.2.1 Anti-Diagonal Robust Metrics

As discussed in Section 3.4 for example-independent costs, when the ratio of positives in
the development and target dataset is the same, standard accuracy is perfectly consistent
with TCC if rC = 1/2. However, we can also expect a good alignment with TCC when the
majority class has the larger misclassification cost (i.e., rC and r+ are both small or both
large):
in this case balancing techniques are counterproductive. Indeed, in these regions,
accuracy outperforms many sophisticated metrics, particularly those designed to handle
class imbalance per se, without considering the UCC ratio. Besides standard accuracy, also
CBA, IAM, WCA, and H exhibit strong correlation with TCC close to the anti-diagonal of
the heatmap (i.e., the line rC = r+). More precisely, accuracy, CBA, IAM, and H diverge
significantly from TCC in two regions: (i) r+ ≲ 0.5 with rC ≳ 1 − r+ and (ii) r+ ≳ 0.5 with
rC ≲ 1 − r+. WCA exhibits a slightly different pattern, diverging from TCC in (i) r+ ≲ 0.5,
with 0.5 ≲ rC ≲ 1 − r+ and (ii) r+ ≳ 0.5, with 1 − r+ ≲ rC ≲ 0.5. Standard and weighted

5Dataset available at https://www.kaggle.com/datasets/blastchar/telco-customer-churn
6Dataset available at https://www.kaggle.com/c/GiveMeSomeCredit
7The symmetry is qualitative, as the asymmetric cost distributions break exact symmetry.

11

---

<!-- PAGE 12 -->

Figure 1: Heatmaps showing standard Spearman correlation between TCC and
the metrics in Table 2 and Section 3.1 over a grid of values of r+ (horizontal axis)
and rC (vertical axis) for the churn prediction use case. To improve readability,
correlation coefficients are multiplied by 10 and rounded.

Spearman coefficients (Figures 1, 2, 3, and 4) display analogous patterns for this group of
metrics.

4.2.2 Main Diagonal Symmetric Metrics

Several metrics exhibit qualitatively symmetric or antisymmetric correlation patterns with
respect to reflection along the main diagonal (rC = 1 − r+). According to the findings in
Section 3.3, metrics designed to compensate for class imbalance without accounting for UCCs
are expected to show good correlation with TCC only for rC ≃ 1 − r+, i.e., close to the main
diagonal. This pattern is observed for informedness, markedness, MCC, Cohen’s Kappa,
WRA and ROC-AUC (single parameter), which we thus refer to as rebalancing metrics. In
the weighted case, the decline in correlation away from the diagonal is more pronounced for
informedness, ROC-AUC, WRA, and even stronger for Kappa.

Recall, F1, and B-ROC show instead strong correlation with TCC above the main diag-
onal and strong anticorrelation below (less pronounced for F1 in the standard correlation),
while specificity shows the opposite behavior. Precision and NPV behave differently de-
pending on whether the standard or weighted correlation coefficient is used: in the former
case (Figures 1 and 2), they behave as rebalancing metrics, with good correlation along the
diagonal, which fades toward uncorrelation or even anticorrelation at the extremes of r+.
When considering the weighted correlation coefficient (Figures 3 and 4), the line of maximal
correlation shifts slightly above (for precision) or below (for NPV), with the diagonal itself
dividing the heatmap into two regions qualitatively similar to recall and specificity. P4 and
G-mean, when analyzed with the standard correlation (Figures 1 and 2), behave as the re-

12

---

<!-- PAGE 13 -->

Figure 2: Heatmaps showing standard Spearman correlation between TCC and the
metrics in Table 2 and Section 3.1 over a grid of values for r+ (horizontal axis) and
rC (vertical axis) for the credit scoring use case. Values with rC ≥ 1/(1 + r+) are
omitted due to consistency conditions (more details in Appendix B.2). To improve
readability, correlation coefficients are multiplied by 10 and rounded.

balancing metrics, with overall lower correlation. Under the weighted correlation (Figures 3
and 4), they exhibit a reversed pattern, with low correlation along the diagonal and stronger
correlation elsewhere.

4.2.3 Globally Robust Metrics

ACD, H informed, WA, and EWA are the top-performing metrics, showing strong correlation
with TCC across nearly all scenarios. ACD performs slightly worse than the others in
this group, particularly under the weighted correlation (Figures 3 and 4), where it exhibits
weaknesses qualitatively similar to those of accuracy, CBA, IAM, and H. The robustness
of this group of metrics was to some extent expected, as they incorporate the example-
independent TCC (Eq. 2, with TCCmin = 0). However, Figures 1, 2, 3, and 4 show robust
and consistent correlation with the example-dependent cost (Eq. 20), indicating that the
fluctuation terms are negligible in this scenario. We omit the heatmaps for MSU and C-
score because they are linearly related to WA.

4.3 Validity Limits of the Example-Independent Approxima-

tion

To quantitatively assess the limits of the example-independent approximation (see also Sec-
tion 3.6), we consider highly skewed, long-tailed distribution of UCCs. This scenario builds
from the first use case (churn prediction) described in Section 4.1.1, by introducing a subset

13

---

<!-- PAGE 14 -->

Figure 3: Heatmaps showing weighted Spearman correlation between TCC and
the metrics in Table 2 and Section 3.1 over a grid of values of r+ (horizontal axis)
and rC (vertical axis) for the churn prediction use case. To improve readability,
correlation coefficients are multiplied by 10 and rounded.

of massive customers, whose revenue dominates the overall distribution. Specifically, we
define Nmc massive customers whose combined revenue accounts for a fraction fr of the total
revenue.

Two quantities characterize the degree of skewness and tail heaviness of the revenue

distribution: the fraction of massive customers

fmc =

Nmc
Ntot

and the fraction fr of the total revenue generated by these customers. We therefore analyze
a grid of fr, fmc values, with fr ranging from 20% to 99% and fmc ranging from 1% to 20%.
Figure 5 reports the standard Spearman correlation between TCC and WA for differ-
ent combinations of fr and fmc. As expected, WA exhibits increasing discrepancies with
TCC as the revenue distribution becomes more concentrated and heavy-tailed; i.e., these
discrepancies are significant for large values of fr (≳ 0.6) and small values of fmc (≲ 0.02).
Conversely, when the revenue fraction associated with the massive customers is more
moderate (fr ≲ 0.4) or the fraction of massive customers is sufficiently large (fmc ≳ 0.05),
WA maintains relatively strong correlation and near-consistent behavior with respect to
TCC. These experiments provide therefore an empirical estimation of the validity limits of
WA, and more generally of confusion-matrix-based evaluation metrics, in the presence of
example-dependent costs with highly skewed distributions. The procedure to explore the
rC , r+ parameter grid is the same as that described in Section 4.1 and the code is contained
in the same repository.

14

---

<!-- PAGE 15 -->

Figure 4: Heatmaps showing weighted Spearman correlation between TCC and the
metrics in Table 2 and Section 3.1 over a grid of values for r+ (horizontal axis) and
rC (vertical axis) for the credit scoring use case. Values with rC ≥ 1/(1 + r+) are
omitted due to consistency conditions (more details in Appendix B.2). To improve
readability, correlation coefficients are multiplied by 10 and rounded.

4.4 Practical Guidelines for Classifier Evaluation

The proposed evaluation framework is applicable across all stages in which classifier perfor-
mance is assessed: primarily model validation and testing, but also model training.

4.4.1 Model Training

Model training typically relies on surrogate loss functions that are differentiable and, in
many cases, convex. Common choices for binary classification include binary cross entropy,
hinge loss, squared loss, and exponential loss. All these loss functions can be expressed in
the form of Eq. 8 with uniform weights va = 1/Ntot; their per-example contributions are

• binary cross entropy: ka = −[ya log(pa) + (1 − ya) log(1 − pa)];
• hinge loss: ka = max(0, 1 − yapa);
• squared loss: ka = (ya − pa)2;
• exponential loss: ka = exp(−yapa).

Here, ya denotes the true label of example a (0 or 1) and pa the corresponding model output,
e.g., the predicted probability of a being in positive class.

The reweighting framework introduced in Sections 3.3, 3.4, and 3.5 can therefore be
directly applied to these loss functions, enabling principled handling of class imbalance and
unequal UCCs.

15

---

<!-- PAGE 16 -->

Figure 5: Heatmaps showing standard Spearman correlation between TCC and
WA over a grid of values for r+ (horizontal axis) and rC (vertical axis) for the churn
prediction with extreme statistics use case. Results are reported for different
values of the fraction fmc of massive customers and the fraction fr of total revenue
associated with them. To improve readability, correlation coefficients are multiplied
by 10 and rounded.

This requires estimating the ratio of positives rt

+ in the target dataset and the UCCs ratio
rC . The latter can be estimated using the procedure described in Appendix A; conversely,
when the target distribution is unavailable, rt
+ can be approximated by the positive fraction
r+ observed in the training set, provided that no substantial distribution shift is expected
between the development and target datasets. The reweighted loss function is obtained by
rescaling the original weights va according to Eq. 17.

If the original loss is consistent with TCC minimization under balanced conditions and
equal UCCs, the previously discussed reweighted loss remains consistent in the more general
setting characterized by class imbalance (rt
+ ̸= r+) and asymmetric misclassification costs
(rC ̸= 1/2).

4.4.2 Model Validation and Testing

During model validation and testing, the results presented in Section 4.2 indicate that WA
(or EWA in the presence of substantial uncertainty in UCCs) is well aligned with TCC
minimization. This holds not only for example-independent UCCs, for which the equivalence
is formally established in Eq. 6, but also for example-dependent UCCs, provided that their
distribution does not exhibit extremely long tails (see Section 4.3).

In contrast, the use of alternative metrics, included several widely adopted evaluation
measures, may lead to sub-optimal model selection, with a potentially significant impact in
terms of TCC; in the following, we quantify this effect.

Consider a validation setting in which classifier hyperparameters must be selected. To

16

---

<!-- PAGE 17 -->

emulate model performance across different hyperparameter configurations, we assume a
parametric relationship between the True Positive Rate (TPR, i.e., TP/P) and the False
Positive Rate (FPR, i.e., FP/N), namely TPR = (FPR)2, which corresponds to an area
under the ROC curve of 2/3. The candidate models are generated from this FPR-TPR
relationship, by uniformly sampling FPR in the interval [0,1] with step size 0.01.

We analyze four representative scenarios:

1. mild class imbalance (r+ = 0.2) with substantially higher cost associated with false

positives (rC = 0.01);

2. mild imbalance (r+ = 0.2) with substantially higher cost associated with false nega-

tives (rC = 0.99);

3. strong imbalance (r+ = 0.01) with higher cost associated with false negatives (rC =

0.9);

4. strong imbalance (r+ = 0.01) with higher cost associated with false positives (rC =

0.1).

For each scenario, we select, from the previously described set of candidates, the optimal
model according to each evaluation metric X under consideration. We then compute the
performance gap ∆TCC, defined as the difference between the TCC of the model selected by
metric X and the minimum achievable TCC among all candidate models. Therefore, ∆TCC
quantifies the economical cost induced by the sub-optimal classifier performance, due to the
use of metric X during model selection.

To incorporate example-dependent UCCs, we adopt the cost structure introduced in the
first use case in Section 4.1.1; for each configuration, the sets of true positives and false
positives are generated via uniform random sampling consistent with the specified TPR and
FPR values. The computation of ∆TCC is repeated over 1000 independent trials, and Table
3 reports the corresponding mean values.

Most metrics exhibit large ∆TCC values in at least one scenario, indicating that their
use for model selection may lead to substantial economical losses. In contrast, only a limited
subset of metrics consistently yields low ∆TCC across all analyzed scenarios, namely the
globally robust metrics, in particular WA, H informed, and EWA; ACD, while generally
competitive, exhibits a non-negligible ∆TCC in Scenario 2.

Since minimizing ∆TCC is equivalent to maximizing RoI, these results also indicate that
using WA, H informed, or EWA for model selection yields the highest RoI across the analyzed
scenarios.

5 Conclusion

In Section 3 we introduced WA, an evaluation metric for binary classifiers that can be
interpreted as a cost-consistent weighted version of accuracy, together with a reweighting
framework – applicable to any metric or loss function that, like WA, can be expressed as a
linear combination of example-dependent quantities – for handling class imbalance in cost-
sensitive settings without relying on resampling techniques. Within this framework, we
established several key results for the case of example-independent UCCs:

• in Section 3.1 we proved that maximizing WA is equivalent to minimizing TCC;
• in Section 3.4, we derived the condition under which metrics and rebalancing tech-
niques designed to compensate class imbalance remain coherent with TCC minimiza-
tion, namely rC ≃ 1 − r+ (Eq. 15);

• in Section 3.5, we generalized the framework to handle development and target datasets
with different ratios of positives and discussed the corresponding validity limits of
standard accuracy.

17

---

<!-- PAGE 18 -->

Table 3: For each metric X, we provide the difference between the TCC of the
model selected by optimizing X and the minimal TCC in the four validation scenarios
described in Section 4.4.2.

Metric
Accuracy
CBA
IAM
H
WCA
Kappa
Informedness
ROC-AUC
WRA
MCC
Markedness
Precision
NPV
P4
G-mean
Jaccard
F1
Recall
B-ROC
Specificity
ACD
WA
H informed
EWA

Scenario 1
0
795
795
0
0
0
0
0
0
0
3842
3916
0
2778
2778
3916
3916
3916
3916
0
0
0
0
0

Scenario 2
591
565
565
591
1
591
591
591
591
591
17
1
591
292
292
1
1
1
1
591
110
1
1
1

Scenario 3
7
7
7
7
253
253
253
253
253
253
253
253
253
253
154
253
253
253
253
7
7
7
7
7

Scenario 4
0
0
0
0
0
3155
3155
3155
3155
3155
3155
3155
3155
3155
1853
3155
3155
3155
3155
0
0
0
0
0

Since most real-world applications involve example-dependent UCCs, Section 4 focused
on realistic use cases characterized by heterogeneous costs, systematically exploring the full
range of possible values for the cost ratio (rC ) and the ratio of positives (r+), and analyzing
the correlation between several evaluation metrics and TCC.

The empirical behavior of rebalancing metrics observed in Section 4.2.2 qualitatively
extends to a broad range of example-dependent scenarios the theoretical condition derived
for example-independent UCCs, namely that rebalancing-based approaches remain coher-
ent with TCC minimization only near the regime rC ≃ 1 − r+ (Eq. 15). More generally,
this result suggests that widely adopted methods for handling class imbalance, including
standard undersampling and oversampling techniques, implicitly rely on assumptions about
the relationship between class imbalance and misclassification costs that may not hold in
realistic applications.

Among the analyzed confusion-matrix-based metrics, only H informed, EWA, WA, C-
score, and MSU exhibit robust correlation with TCC across all tested scenarios, thereby
reducing the risk of misleading model assessments. H informed and EWA require the addi-
tional complexity of a probabilistic formulation, which increases computational cost without
providing clear advantages in the analyzed scenarios. WA, in contrast, combines robust
empirical behavior with a straightforward interpretation, cross-dataset comparability, and
a natural extension to scenarios in which the target and development datasets differ; these
properties make WA suitable both for comparing models evaluated on different datasets and

18

---

<!-- PAGE 19 -->

for validation-based hyperparameter tuning. In Section 4.4.2, we further quantified the prac-
tical impact of metric choice by measuring the RoI advantage obtained when WA is used for
model validation instead of alternative evaluation metrics.

The experimental results in Sections 4.2 also indicate that the example-independent
approximation of TCC, obtained by neglecting the fluctuation terms in Eq. 20, remains
consistent and reliable in all examined scenarios. This observation is particularly relevant
because such an approximation is implicitly assumed by any evaluation framework based on
the confusion matrix formalism. Motivated by this consideration, Section 4.3 systematically
investigated the validity limits of this approximation in the presence of highly skewed and
heavy-tailed cost distributions, i.e., scenarios in which a very small fraction of massive exam-
ples accounts for a relevant fraction of the total cost. The results show that near-consistent
behavior is still observed when either the fraction of total cost associated with the massive
examples remains moderate or the fraction of examples being massive is sufficiently large.

Appendix A Estimation of the WA Weight

In an ideal scenario, the UCCs defined in Section 2.2 can be assessed by estimating the
cost associated to the actions taken in response to each type of classification outcome (false
positive, true positive, etc.). Note that the cost matrix may include opportunity costs, i.e.,
foregone benefits due to missed opportunities, as in the examples described in Section 4.1.1;
costs or benefits can be measured relatively to any baseline. However, the baseline must
remain fixed, i.e., the reference point for zero cost should not change [9].

In practice, estimating the full confusion matrix may be challenging. Therefore, we often
focus on the more attainable goal of estimating the weight w in Eq. 3, or equivalently, the
UCC ratio ρ = CFN/CFP, which suffices for computing WA in Eq. 3. We propose therefore
a procedure to estimate the weight range wmin ≤ w ≤ wmax. Here, we assume that the
development and target datasets have the same ratio of positive examples; the generalization
to r+ ̸= rt

+ is described in Eq. 18.

A.1 Unit Misclassification Costs Ratio

The first approach to estimating the weight range is via the UCC ratio ρ – i.e., estimating
how many false positives are, on average, equivalent to a single false negative – and using the
equivalence w = ρ/(ρ + 1). For instance, in bankruptcy prediction, a false negative – where
an auditor incorrectly assesses a company as solvent – may result in liability to creditors and
shareholders. Conversely, a false positive – where a solvent company is incorrectly assessed
as insolvent – may lead to reduced access to credit and increased uncertainty. Based on
these considerations, [1] and [10] estimated ρ ≃ 35 (i.e., w ≃ 0.97) and 10 ≲ ρ ≲ 50 (i.e.,
0.91 ≲ w ≲ 0.98), respectively.

A.2 Constraints from Ranking of Emblematic Models

If the previous approach is not feasible, an alternative method is to infer constraints on w by
ranking a set of emblematic classification results. Even if we cannot estimate the costs CFP
and CFN (or their ratio), we may still be able to determine whether one specific outcome is
more costly than another.

A.2.1 Construction of the Emblematic Model Set

The choice of emblematic models may depend on the use case and the ratio of positive
examples. Ideally, we should select a small set of models, sufficiently simple to avoid over-
complexity in the ranking of the outcomes, yet diverse enough to yield meaningful constraints
on w. As a baseline, we consider the models described in Table 4: (i) M+ and M−, which

19

---

<!-- PAGE 20 -->

always predict the same class; (ii) Mbad, which misclassifies a fraction α of examples in both
classes; (iii) Mbad− and Mbad+, which misclassify a fraction α of negatives or positives,
respectively, while perfectly classifying the other class.

Table 4: Set of emblematic models to determine constraints on w. Anum is the
numerator in Eq. 3.

Name

Description

Anum

Dummy model always predicting class +.
Dummy model always predicting class −.
Misclassifies a fraction α of examples in both classes.

M+
M−
Mbad
Mbad− Misclassifies a fraction α of negatives, perfect on positives.
Mbad+ Misclassifies a fraction α of positives, perfect on negatives.

wP
(1 − w)N
(1 − α)[wP + (1 − w)N]
wP + (1 − α)(1 − w)N
(1 − α)wP + (1 − w)N

The parameter α, representing the fraction of misclassified examples, can be chosen ad
hoc to facilitate model ranking. To derive meaningful constraints on w, we recommend
choosing α in the range 0.5 ≲ α ≲ 0.75.

A.2.2 Ranking of Emblematic Models

To rank the models previously identified, we must understand the use case from a business
perspective. For example, is it preferable to correctly identify all positives (as in Mbad−)
or all negatives (as in Mbad+)? For illustrative purposes, let us assume a ratio r+ = 0.05
of positive examples, and let us use the models from Table 4 with α = 0.6. Suppose it is
impractical to react to a large number of predicted positives (e.g., contacting many customers
in churn prediction, treating many patients in cancer detection, etc.). In this scenario, the
worst outcome is likely M+, and we expect A(Mbad−) ≲ A(Mbad+).

Moreover, M−, which predicts only negatives, may be slightly preferable to Mbad, since
its output could still be useful if a future positive prediction occurs. To complete the ranking,
we assume Mbad− is preferable to M−, as the former misclassifies a fraction α of negatives
and no positive example, and therefore produces a more informative output compared to the
latter, which misclassifies all positives.

In summary, we obtain the following ranking:

A(M+) ≲ A(Mbad) ≲ A(M−) ≲ A(Mbad−) ≲ A(Mbad+).

(21)

A.2.3 Inferring the Constraints from the Ranking

Since P and N are fixed for a given dataset, ranking the models by WA is equivalent to
ranking them by the numerator Anum in Table 4. For α ≥ 0.5, the resulting constraints on
w are:

(cid:21)−1

(cid:20)

1 +

P
α N

≲ w ≲

(cid:20)

1 +

α P
(1 − α)N

(cid:21)−1

.

(22)

For α = 0.6 and r+ = 0.05, Eq. 22 becomes 0.919 ≲ w ≲ 0.927, where the upper bound
follows from the condition A(M+) ≲ A(Mbad), and the lower bound from A(Mbad−) ≲
A(Mbad+).

Appendix B Use Cases Details

B.1 Churn Prediction

Each customer a predicted as positive causes a cost M for the retention measure, which
includes the time and effort of the commercial team to contact the customer and implement

20

---

<!-- PAGE 21 -->

the measure. Here we assume that this retention cost is example-independent, so eFP
a =
dTP
a = M . Since the experiment described in Section 4.1 requires spanning all possible UCC
ratios rC , we tune the cost of the retention measure M accordingly.

Conversely, for a customer a predicted as negative, the cost (or missing income) is RaPeff ,
where Peff is the probability of effectiveness of the retention measure (assumed example-
independent and fixed to 25%), while Ra is the revenue the company would have earned from
a had the customer not churned, and is assumed proportional to the customer’s revenue.

To avoid negative values on the false negative costs, we clip each DFN

to positive values,
a = max(0, Ra Peff − M ). To obtain the desired value for rC , we must
a max(M, Peff Ra), with γ = (1 − rC )/Ntot, whose solution is
a=A+1 Peff Ra/(1 − γA), subject to the constraint Peff RA ≤ M ≤ Peff RA+1. Under
avg Peff − M , where Rclip
avg
a = max(Ra, M/Peff ) over the target dataset, while the

i.e., we set DFN
solve the equation M = γ (cid:80)
M = γ (cid:80)Ntot
these assumptions, the average UCCs are CFP = M and CFN = Rclip
denotes the expected value of Rclip
fluctuations are δa = Peff (Rclip

avg ) and ϵa = 0.

a − Rclip

a

B.2 Credit Scoring

a

and eTN

a = dFN
a
a = eFP
a

For credit scoring, we use the approach described in [3]. In that framework, the costs of
correct classifications, dTP
a , are assumed to be zero for every customer a. The loss
DFN
if the customer a defaults is proportional to their credit line, while the cost
EFP
of a false positive is the sum of two financial components, Ra and Gavg. The
first term is the loss of profit from rejecting a customer who would have repaid the loan;
it depends on the loan parameters (see [3] for details). Differently from [3], we introduce
clipping of the customer debt ratio to the interval [0, 1], ensuring data consistency.

The term Gavg reflects the assumption that the financial institution does not keep the
capital of a rejected customer idle, but instead allocates it to an alternative customer. Since
no additional information about this alternative customer is available, we assume that the
customer defaults with probability equal to the prior positive rate r+. Under this assumption,
Gavg = −Ravg · (1 − r+) + Cl · Lgd · r+, where Cl is the average credit line, Ravg the average
profit, and Lgd the loss-given-default ratio, i.e., the fraction of the customer’s debt that is
lost in case of default.

The parameter used to tune the UCC ratio rC is Lgd. To ensure that Lgd remains non-
negative, the analysis must be restricted to the domain rC < 1/(1 + r+), hence the missing
values in the top right corner of each heatmap in Figures 2 and 4.

References

[1] Edward I. Altman, Robert G. Haldeman, and P. Narayanan. ZETATM analysis A
new model to identify bankruptcy risk of corporations. Jour. of Banking & Finance,
1(1):29–54, 1977.

[2] Yuri Sousa Aurelio, Gustavo Matheus de Almeida, Cristiano Leite de Castro, et al.
Cost-sensitive learning based on performance metric for imbalanced data. Neural Proc.
Lett., 54(4):3097–3114, 2022.

[3] Alejandro Correa Bahnsen, Djamia Aouada, and Bj¨orn Ottersten. Example-dependent
cost-sensitive logistic regression for credit scoring. In 2014 13th International conference
on machine learning and applications, pages 263–269. IEEE, 2014.

[4] Alvaro A C´ardenas and John S Baras. B-ROC curves for the assessment of classifiers
over imbalanced data sets. In Proc. of the national Conf. on Art. Int., volume 21, page
1581, 2006.

[5] Nitesh V Chawla. Data mining for imbalanced datasets: An overview, pages 853–867.

Springer US, Boston, MA, 2005.

21

---

<!-- PAGE 22 -->

[6] Nitesh V Chawla, Kevin W Bowyer, Lawrence O Hall, and W Philip Kegelmeyer. Smote:
synthetic minority over-sampling technique. Journal of artificial intelligence research,
16:321–357, 2002.

[7] Pedro Domingos. MetaCost: A general method for making classifiers cost-sensitive.
In Proc. of the 5th ACM SIGKDD Int. Conf. on Know. Disc. and Data Min., pages
155–164, 1999.

[8] Chris Drummond and Robert C Holte. C4.5, class imbalance, and cost sensitivity: why
under-sampling beats over-sampling. In Int. Conf. on Mach. Learn., volume 11, 2003.

[9] Charles Elkan. The foundations of cost-sensitive learning. In Int. joint Conf. on Art.

Int., volume 17, pages 973–978, 2001.

[10] Harlan L Etheridge, Ram S Sriram, and HY Kathy Hsu. A comparison of selected
artificial neural networks that help auditors evaluate client financial viability. Decision
Sciences, 31(2):531–550, 2000.

[11] L´eo Gautheron, Amaury Habrard, Emilie Morvant, et al. Metric learning from im-
balanced data. In 2019 IEEE 31st Int. Conf. on Tools with Art. Int. (ICTAI), pages
923–930. IEEE, 2019.

[12] Nysia I George, Tzu-Pin Lu, and Ching-Wei Chang. Cost-sensitive performance metric

for comparing multiple ordinal classifiers. Art. Int. Res., 5(1):135–143, 2016.

[13] Bishwadip Ghosh and Joseph Hasley. Using asymmetric classification cost matrices in

predicting diabetes. In ICDSS 2007 Proceedings, 2007.

[14] David J Hand. Measuring classifier performance: a coherent alternative to the area

under the ROC curve. Mach. Learn., 77(1):103–123, 2009.

[15] Mohammad Hossin and Md Nasir Sulaiman. A review on evaluation metrics for data
Int. Jour. of Data Min. & Know. Manag. process, 5(2):1,

classification evaluations.
2015.

[16] Jungeun Kim, Keunho Choi, Gunwoo Kim, et al. Classification cost: An empirical
comparison among traditional classifier, cost-sensitive classifier, and MetaCost. Exp.
Syst. with Appl., 39(4):4013–4019, 2012.

[17] Matjaz Kukar and Igor Kononenko. Cost-sensitive learning with neural networks. In

Proc. of the 13th European Conf. on Art. Int. (ECAI 98), pages 445–449, 1998.

[18] Nada Lavraˇc, Peter Flach, and Blaz Zupan. Rule evaluation measures: A unifying view.

In Int. Conf. on inductive logic programming, pages 174–185. Springer, 1999.

[19] Guillaume Lemaˆıtre, Fernando Nogueira, and Christos K Aridas.

Imbalanced-learn:
A python toolbox to tackle the curse of imbalanced datasets in mach. learn. Jour. of
Mach. Learn. Res., 18(17):1–5, 2017.

[20] Charles X Ling, Victor S Sheng, and Qiang Yang. Test strategies for cost-sensitive

decision trees. IEEE Trans. on Know. and Data Eng., 18(8):1055–1067, 2006.

[21] Xu-Ying Liu and Zhi-Hua Zhou. The influence of class imbalance on cost-sensitive
learning: An empirical study. In 6ht Int. Conf. on Data Min. (ICDM’06), pages 970–
974. IEEE, 2006.

[22] Yangguang Liu, Yangming Zhou, Shiting Wen, et al. A strategy on selecting perfor-
Int. Jour. of Mobile Comp. and Multimedia

mance metrics for classifier evaluation.
Communications (IJMCMC), 6(4):20–35, 2014.

[23] Lucas Loezer, Fabr´ıcio Enembreck, Jean Paul Barddal, et al. Cost-sensitive learning
for imbalanced data streams. In Proc. of the 35th annual ACM symposium on applied
Comp., pages 498–504, 2020.

[24] Pierangelo Lombardo. Standardization of weighted ranking correlation coefficients.

CoRR abs/2504.08428, 2025.

22

---

<!-- PAGE 23 -->

[25] Pierangelo Lombardo, Alessio Boiardi, Luca Colombo, et al. Top-rank-focused adaptive
vote collection for the evaluation of domain-specific semantic models. In Proc. of the
2020 Conf. on Empirical Methods in Natural Language Proc. (EMNLP), pages 3081–
3093, 2020.

[26] Huijuan Lu, Yige Xu, Minchao Ye, et al. Learning misclassification costs for imbalanced

classification on gene expression data. BMC bioinformatics, 20:1–10, 2019.

[27] Manish Marwah, Asad Narayanan, Stephen Jou, et al. Is F1 score suboptimal for cy-
bersecurity models? introducing Cscore, a cost-aware alternative for model assessment.
In Conf. on Applied Mach. Learn. for Inf. Security, volume 3920, pages 190–209, 2024.

[28] Ross A McDonald. The mean subjective utility score, a novel metric for cost-sensitive

classifier evaluation. Pattern Recognition Lett., 27(13):1472–1477, 2006.

[29] Ibomoiye Domor Mienye and Yanxia Sun. Performance analysis of cost-sensitive learning

methods with application to imbalanced medical data. Artif Intell Rev, 57(80), 2024.

[30] Ebrahim Mortaz. Imbalance accuracy metric for model selection in multi-class imbal-

ance classification problems. Know.-Based Syst., 210:106490, 2020.

[31] Mihaela Muntean and Florin-Daniel Militaru. Metrics for evaluating classification algo-
rithms. In Education, Res. and Business Tech.: Proc. of 21st Int. Conf. on Informatics
in Economy (IE 2022), pages 307–317. Springer, 2023.

[32] Deirdre B O’Brien, Maya R Gupta, and Robert M Gray. Cost-sensitive multi-class
In Proc. of the 25th Int. Conf. on Mach.

classification from probability estimates.
Learn. (ICML), pages 712–719, 2008.

[33] Stjepan Picek, Annelie Heuser, Alan Jovic, et al. The curse of class imbalance and
conflicting metrics with machine learning for side-channel evaluations. IACR Trans. on
Cryptographic Hardware and Embedded Syst., 2019(1):209–237, 2018.

[34] David Powers. Evaluation: From precision, recall and F-measure to ROC, informedness,

markedness & correlation. Jour. of Mach. Learn. Tech., 2(1):37–63, 2011.

[35] Badiuzzaman Pranto, Sk Maliha Mehnaz, Sifat Momen, et al. Prediction of diabetes
using cost sensitive learning and oversampling techniques on bangladeshi and indian
female patients. In 2020 5th Int. Conf. on Inf. Tech. Res. (ICITR), pages 1–6. IEEE,
2020.

[36] Oona Rainio, Jarmo Teuho, and Riku Kl´en. Evaluation metrics and statistical tests for

machine learning. Scientific Reports, 14(1):6086, 2024.

[37] D Ramyachitra and Parasuraman Manikandan. Imbalanced dataset classification and
solutions: a review. Int. Jour. of Comp. and Business Res. (IJCBR), 5(4):1–29, 2014.

[38] Mikolaj Sitarz. Extending F1 metric, probabilistic approach. CoRR abs/2210.11997,

2022.

[39] Charles Spearman. The proof and measurement of association between two things. The

American Jour. of Psychology, 15(1):72–101, 1904.

[40] Seba Susan and Amitesh Kumar. The balancing trick: Optimized sampling of imbal-
anced datasets—a brief survey of the recent state of the art. Eng. Reports, 3(4):e12298,
2021.

[41] Akbar Telikani, Amir H Gandomi, Kim-Kwang Raymond Choo, et al. A cost-sensitive
deep learning-based approach for network traffic classification. IEEE Trans. on Network
and Service Manag., 19(1):661–670, 2022.

[42] Thomas Verbraken, Wouter Verbeke, and Bart Baesens. A novel profit maximizing
metric for measuring classification performance of customer churn prediction models.
IEEE Trans. on Know. and Data Eng., 25(5):961–973, 2013.

23

---

<!-- PAGE 24 -->

[43] Haomin Wang, Gang Kou, and Yi Peng. Multi-class misclassification cost matrix for
credit ratings in peer-to-peer lending. Jour. of the Operational Res. Society, 72(4):923–
934, 2021.

[44] Yuri Zelenkov. Example-dependent cost-sensitive adaptive boosting. Exp. Syst. Appl.,

135:71–82, 2019.

24

<!-- MARKITDOWN CONVERSION -->

<!-- Full MarkItDown conversion for formatting fidelity. -->

Cost-Sensitive Evaluation for Binary Classifiers
Pierangelo Lombardo1, Antonio Casoli1, Cristian Cingolani2, Shola
Oshodi2, and Michele Zanatta2
1Eutelsat, Paris, France
2Reply, Rome, Italy
Abstract
Selectinganappropriateevaluationmetricforclassifiersiscrucialformodel
comparison, parameter optimization, and deployment decisions, yet there is no
consensus on a broadly accepted evaluation paradigm explicitly aligned with
Total Classification Cost (TCC) minimization. At the same time, class imbal-
ance is often treated as a problem to be corrected per se, potentially causing
misalignments with TCC minimization.
To address these limitations, (i) we define Weighted Accuracy (WA), an
evaluation metric for binary classifiers with a straightforward interpretation
as a weighted version of accuracy and (ii) we propose a general reweighting
frameworkforhandlingclassimbalanceincost-sensitivescenarios,providingan
alternative to resampling techniques. This framework applies to any evalua-
tion metric or loss function that can be expressed as a linear combination of
example-dependent quantities; it enables meaningful comparison of evaluation
resultsobtainedondifferentdatasetsandaccountsfordiscrepanciesbetweenthe
development dataset, used for training, validation, and testing, and the target
dataset, where the model will be deployed. Within this framework, we derive
the conditions under which standard rebalancing techniques remain coherent
with TCC minimization, and when they may instead become misleading.
Weprovethat,underexample-independentUnitClassificationCosts,maxi-
mizingWAisequivalenttominimizingTCC.Finally,weanalyzetherobustness
of WA in realistic example-dependent cost scenarios by studying its correlation
withTCCacrossabroadrangeofclassimbalanceandcostregimes. Theresults
showthatWAmaintainsrobustalignmentwithTCCacrossalmostallexamined
scenarios.
Keywords— MachineLearning,BinaryClassification,ImbalancedDataset,Cost-Sensitive
Learning,ReturnonInvestment,TotalClassificationCost,UnitClassificationCost,Weighted
Accuracy, Evaluation Metric, Example-Dependent Cost
1 Introduction
SelectingtheevaluationmetricforaMachineLearning(ML)usecaseisafundamentalstep,
asitguidesthechoiceoftheoptimalmodelanditshyperparameters[14,34,42,15,31,36].
However, this task is still complex: numerous metrics exist, and they can rank models in
completely different ways [22], with no consensus on the optimal choice [15, 34, 42, 31,
36,27]. Inclassificationtasks,modelperformanceistypicallydescribedusingtheconfusion
matrixandevaluatedusingderivedmetricssuchasaccuracy,F-measure,ReceiverOperating
1
6202
yaM
62
]GL.sc[
2v61022.0152:viXra

Characteristic-Area Under the Curve (ROC-AUC), and Cohen’s kappa [15, 34, 38, 36, 27].
Changingtheevaluationmetricoftenleadstoselectingadifferentoptimalclassifier. Thisis
relatedtothefactthatthesemetricsimplicitlydefinetheUnitClassificationCosts(UCCs),
i.e.,thecostofclassifyinganexampleofclassiasclassj,inanuncontrolledandpotentially
incorrectmanner. Forexample,inbinaryclassification,accuracyimpliesequalcostsforfalse
positives and false negatives, while ROC-AUC corresponds to variable cost distributions
across classifiers [14].
Moreover, most real-world datasets are moderately or heavily imbalanced: this is com-
monindomainssuchasmedicaldiagnosis[21,37,19,23],biochemicalforecasting(e.g.,pro-
tein sequences, gene expression) [19, 26], image processing [36], intrusion detection [4, 21],
frauddetection(e.g.,banking,telecommunications)[21,37,19,23],telecommunicationsap-
plications [5, 19], information retrieval [37], and anomaly detection in manufacturing [37].
In such cases, many standard metrics can distort results, making model ranking even more
challenging[5,26,38]. Classimbalanceiswidelyrecognizedasoneofthemajorchallengesin
MLresearch[37,19,23,29]andseveralapproacheshavebeenproposedtomitigateitseffects,
including undersampling, oversampling, hybrid sampling strategies (e.g., retaining difficult-
to-learnsamples),andCost-SensitiveMachineLearning(CSML)[6,8,4,5,37,11,30,23,40].
CSMLinvolvesexplicitlydefiningacostmatrixwhoseentriesaretheUCCs,incontrast
with traditional machine learning, where such costs are only implicitly defined through the
evaluation metric. Empirical studies have shown that when UCCs are explicitly estimated,
they often exhibit substantial imbalances across real-world use cases such as medical diag-
nosis [20, 13, 35], bankruptcy prediction [1, 10], loan credit rating [43], cybersecurity [27],
biometricidentityrecognition[28],consumercreditscoring[28],anddatabasemarketing[7].
In business applications, a concept closely tied to the reduction of total cost in machine
learning is Return on Investment (RoI). A similar principle applies in healthcare, where
costsmayincludenotonlyeconomicexpensesbutalsohealthrisksorlimitedavailabilityof
treatments [20, 13, 35].
Within the umbrella of CSML, two distinct research directions exist: (i) studies that
aim to estimate and minimize the Total Classification Cost (TCC) [1, 20, 16, 29], which is
the key for RoI optimization, and (ii) studies that use misclassification costs primarily to
address class imbalance, often with the goal of maximizing specific metrics (e.g., accuracy,
F1, specificity, sensitivity) on a rebalanced dataset [17, 21, 32, 37, 33, 35, 23, 41, 2]; this
secondlineofresearchexistsbecausethehighestUCCisoftenassociatedwithmisclassifying
the minority class: in such cases, addressing class imbalance may also reduce TCC [29].
However, when the goal is to maximize RoI and minimize TCC, correcting class im-
balance per se may not be beneficial, especially if the minority classes are associated with
misclassification costs comparable to, or lower than, those of the majority classes, and the
class distribution in the target dataset (i.e., the real-world data where the model will be
deployed) is similar to that of the development dataset (used for training, validation, and
testing). Conceptually,theidealapproachtooptimizeaclassifierwiththefinalgoalofmax-
imizing RoI would be (i) estimating the UCC for each class pair (i,j), and (ii) minimizing
the TCC computed from the UCCs and the confusion matrix. However, this purely cost-
based approach suffers from limitations: (i) estimating UCCs may be challenging; (ii) TCC
depends on the dataset it is measured on, making it unsuitable for comparing classifiers
acrossdatasets;(iii)thereisnoguaranteethatminimizingTCConthedevelopmentdataset
will also minimize it on the target dataset; and (iv) in many real-world use cases UCCs
depend on the specific example, challenging the assumptions underlying confusion-matrix-
based evaluation approaches.
Our work provides three main contributions addressing these limitations: (i) as an al-
ternative to existing metrics, we introduce Weighted Accuracy (WA), an evaluation metric
forbinaryclassifierswithastraightforwardinterpretationasaweightedversionofthewell-
knownaccuracymetric,whosemaximizationweprovetobeequivalenttoTCCminimization
under example-independent UCCs; (ii) we formalize a reweighting framework for handling
2

class imbalance in cost-sensitive evaluation scenarios, providing an alternative to rebalanc-
ing techniques; this framework can be applied to any linear example-dependent metric,
formalizes WA as a cost-based reweighted version of standard accuracy, enables consistent
comparison of results obtained on different datasets, and naturally accounts for discrepan-
cies between the class distributions in the development and target datasets; and (iii) we
provide empirical evidence of the robustness of WA by analyzing its correlation with TCC
across diverse example-dependent scenarios, while also studying the validity limits of the
example-independentapproximationunderlyingWAandotherconfusion-matrix-basedeval-
uation methods.
| 2 Related     |     | Work         |     |     |         |     |     |
| ------------- | --- | ------------ | --- | --- | ------- | --- | --- |
| 2.1 Confusion |     | Matrix-Based |     |     | Metrics |     |     |
Thepredictionoutputofabinaryclassifieristypicallydescribedintermsofa2×2confusion
matrix, as shown in Table 1, where TP (TN) denotes the count of true positives (true
|     | Table |        | 1: Confusion | matrix    | N   | for a binary classifier. |     |
| --- | ----- | ------ | ------------ | --------- | --- | ------------------------ | --- |
|     |       |        |              | Predicted |     | + Predicted −            |     |
|     |       | Actual | +            |           | TP  | FN                       |     |
|     |       | Actual | −            |           | FP  | TN                       |     |
negatives),FP(FN)denotesthecountoffalsepositives(falsenegatives),whileP=TP+FN
(N=TN+FP) is the number of positive (negative) examples, and N =P+N the total
tot
| number | of examples. |     |     |     |     |     |     |
| ------ | ------------ | --- | --- | --- | --- | --- | --- |
A wide range of evaluation metrics, summarized in Table 2, are derived from the con-
fusion matrix, including accuracy, Jaccard’s similarity index, F-measure, recall, precision,
specificity,NegativePredictiveValue(NPV),informedness,markedness,MatthewsCorrela-
tionCoefficient(MCC),Cohen’sKappa,G-Mean,andROC-AUC.Despitetheirwidespread
use, each of these metrics has received criticism [14, 38]. To mitigate these issues, various
techniques have been proposed, such as resampling strategies and cost-sensitive learning.
However, resampling may alter the statistical properties of the original dataset, introduce
| redundancy, | and increase |     | computational | cost | [7, 37, | 11, 29]. |     |
| ----------- | ------------ | --- | ------------- | ---- | ------- | -------- | --- |
Recent work has focused on defining confusion-matrix-based metrics to better handle
class imbalance [11, 30, 31]; table 2 includes several such metrics; among these are Class
Balance Accuracy (CBA) and Imbalance Accuracy Metric (IAM) [30], the P4 metric [38],
| Bayesian | ROC (B-ROC) |     | curves [4]. |     |     |     |     |
| -------- | ----------- | --- | ----------- | --- | --- | --- | --- |
In addition, several cost-sensitive metrics have been proposed to explicitly incorporate
misclassificationcosts;thesearealsosummarizedinTable2andwillbedescribedinSection
2.2.
| 2.2 Cost-Sensitive |     |     | Evaluation |     | and | Classification | Costs |
| ------------------ | --- | --- | ---------- | --- | --- | -------------- | ----- |
As discussed in Section 1, the ideal strategy for selecting the optimal classifier in a given
use case – particularly when the goal is maximizing the RoI – is to minimize the TCC. In
general,TCCmaydependonthespecificexamplesthataremisclassified1[43]andforbinary
1For instance, in churn prediction, the cost of a false negative may vary depending on which is
themisclassifiedcustomer.
3

Table 2: Summary of confusion-matrix-based metrics for binary classifiers. Top:
standardmetrics;middle: recentlyintroducedmetrics;bottom: cost-sensitivemetrics.
|                        |                     | Name |     |                                       |                       |               | Formula                       |               |         |     |
| ---------------------- | ------------------- | ---- | --- | ------------------------------------- | --------------------- | ------------- | ----------------------------- | ------------- | ------- | --- |
|                        |                     |      |     | Standard                              | CM                    | metrics       |                               |               |         |     |
|                        | Accuracy(A)         |      |     |                                       |                       | (TP+TN)/Ntot  |                               |               |         |     |
|                        | Recall(Sensitivity) |      |     |                                       |                       |               | TP/P                          |               |         |     |
|                        | Precision           |      |     |                                       |                       |               | TP/(TP+FP)                    |               |         |     |
|                        | Specificity         |      |     |                                       |                       |               | TN/N                          |               |         |     |
|                        |                     | NPV  |     |                                       |                       |               | TN/(TN+FN)                    |               |         |     |
|                        | Jaccard’ssimilarity |      |     |                                       |                       | TP/(TP+FP+FN) |                               |               |         |     |
|                        |                     |      |     |                                       | (1+β2)·TP/            |               | (cid:2) TP+β2·P+FP            |               | (cid:3) |     |
|                        | F-measure(F         |      | β ) |                                       |                       |               |                               |               |         |     |
|                        | Informedness        |      |     |                                       |                       |               | TP/P−FP/N                     |               |         |     |
|                        | Markedness          |      |     |                                       | TP/(TP+FP)−FN/(TN+FN) |               |                               |               |         |     |
|                        |                     | MCC  |     | (TP·TN−FP·FN)/                        |                       |               | (cid:112) (TP+FP)·P·N·(TN+FN) |               |         |     |
|                        | Cohen’skappa(κ)     |      |     | 2·(TP·TN−FN·FP)/[(TP+FP)·N+P·(FN+TN)] |                       |               |                               |               |         |     |
|                        | G-Mean              |      |     |                                       |                       | (cid:112)     | TP·TN/(P·N)                   |               |         |     |
| ROC-AUC(singleparam.)1 |                     |      |     |                                       |                       | (TP/P+TN/N)/2 |                               |               |         |     |
|                        |                     |      |     | Recently                              | proposed              | CM            | metrics                       |               |         |     |
|                        |                     | CBA  |     | [TP/max(P,TP+FP)+TN/max(N,TN+FN)]/2   |                       |               |                               |               |         |     |
|                        |                     | IAM  |     |                                       | TP−max(FP,FN)         |               | +                             | TN−max(FP,FN) |         |     |
|                        |                     |      |     |                                       | 2max(P,TP+FP)         |               |                               | 2max(N,TN+FN) |         |     |
|                        |                     | P4   |     | (4·TP·TN)/[4·TP·TN+(TP+TN)·(FP+FN)]   |                       |               |                               |               |         |     |
B-ROC(singleparam.)1
[TP/P+TP/(FP+TP)]/2
|     |         |     |     | Cost-sensitive                                 |                            | metrics              |             |                           |     |     |
| --- | ------- | --- | --- | ---------------------------------------------- | -------------------------- | -------------------- | ----------- | ------------------------- | --- | --- |
|     | WCA2    |     |     |                                                |                            | w·TP/P+(1−w)·TN/N    |             |                           |     |     |
|     |         | WRA |     | [4·(TP/P−FP/N)N·CFP/(P·CFN)]/[1+N·CFP/(PCFN)]2 |                            |                      |             |                           |     |     |
|     |         | ACD |     |                                                | (cid:112)                  | (1−A)2+(TCC/TCCmax)2 |             |                           |     |     |
|     | C-score |     |     |                                                |                            |                      | TCC/(P·CFP) |                           |     |     |
|     |         | MSU |     |                                                | 1−[TCC−TCCmin]/TCCmax      |                      |             |                           |     |     |
|     |         | H   |     |                                                | 1− (cid:82) 1dcu(c)TCC(c)/ |                      |             | (cid:82) 1dcu(c)TCCmax(c) |     |     |
|     |         |     |     |                                                | 0                          |                      |             | 0                         |     |     |
1ROC-AUCandB-ROCaredefinedforparametricclassifiers. Forsingle-parameterclassifiers,they
canbecomputedastheareaunderthesegmentsconnectingtheclassifierpointto(0,0)and(1,1)
inthe(TP-rate,FP-rate)or(TP-rate,FalseAlarmRate)plane[34].
2InWCAdefinition,w isthesampleimportance,whichcanbeidentifiedwithCFN/(CFN+CFP).
| classification |      | can be   | defined as    |       |        |                   |               |         |          |          |
| -------------- | ---- | -------- | ------------- | ----- | ------ | ----------------- | ------------- | ------- | -------- | -------- |
|                |      | (cid:88) | (cid:16) dFNδ | +dTPδ |        | (cid:17) (cid:88) | (cid:16) eTNδ |         | +eFPδ    | (cid:17) |
|                | TCC= |          |               |       |        | +                 |               |         |          | , (1)    |
|                |      |          | a o(a),−1     | a     | o(a),1 |                   | a             | o(a),−1 | a o(a),1 |          |
|                |      | a∈S+     |               |       |        | a∈S−              |               |         |          |          |
whereS (S )isthesetofpositive(negative)examples,dFN (dTP)istheUCCforincorrect
|     | +   | −   |     |     |     |     | a   | a   |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
(correct) classification of positive example a, eFP (eTN) is the UCC for incorrect (correct)
a a
classification of negative example a, o(a) is the classifier output for example a, and δ is
jk
| the | Kronecker | delta. |     |     |     |     |     |     |     |     |
| --- | --------- | ------ | --- | --- | --- | --- | --- | --- | --- | --- |
In most literature, UCCs are assumed to be example-independent, i.e., dFN = c FN ,
a
dTP =c , eFP =c , and eTN =c . Under this assumption, the TCC can be expressed
| a   | TP  | a   | FP a | TN  |     |     |     |     |     |     |
| --- | --- | --- | ---- | --- | --- | --- | --- | --- | --- | --- |
intermsoftheconfusionmatrix: TCC=c ·TP+c ·FN+c ·FP+c ·TN.Toensure
|     |     |     |     |     | TP  | FN  |     | FP  | TN  |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
economic coherence, we require c <c and c <c [9] and thus we can simplify the
|     |     |     |     | TP  | FN  | TN  | FP  |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
notation, introducing the shifted UCCs C FN =c FN −c TP and C FP =c FP −c TN , obtaining
|     |     |     | TCC=C | ·FN+C |     | ·FP+TCC |     | ,   |     | (2) |
| --- | --- | --- | ----- | ----- | --- | ------- | --- | --- | --- | --- |
|     |     |     |       | FN    |     | FP      |     | min |     |     |
whereTCC =c ·N+c ·Pistheminimumachievablecost,correspondingtoperfect
|     | min | TN  | TP  |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
classification.
4

Several studies have proposed evaluation metrics explicitly depending on TCC, as sum-
marizedinTable2,includingAccuracy-Cost-Distance(ACD)[12],WeightedRelativeAccu-
racy(WRA)[18],WeightedClassificationAccuracy(WCA)[26],andC-score[27],arescaled
and dimensionless version of the TCC that correctly captures the TCC ranking, albeit its
unbounded nature may pose challenges for interpretability and cross-dataset comparability.
In the context of decision theory, [28] defined Mean Subjective Utility (MSU) as a normal-
ized transformation of the utility matrix; when adapted to the cost formalism adopted in
this work, MSU becomes proportional to TCC and ranges from 1 (minimum TCC) to the
lower bound −TCC /TCC (maximum TCC), which depends on the dataset and cost
min max
matrix.
Finally, [14] proposed a cost-aware alternative to ROC-AUC for parametric classifiers,
expressing TCC in terms of the UCC ratio c = C /(C +C ), distributed according
FP FP FN
to a probability density function u(c). The resulting metric is defined in Table 2, where
TCC(c) = b[cFP+(1−c)FN] and TCC (c) = b[cN+(1−c)P], with b = C +C .
max FP FN
The H measure can be interpreted as a generalization of MSU, extending it from the edge
casewherecisknown,toscenarioswhereitisuncertain. Inthelimitcaseinwhichnoprior
information about c is available, [14] propose modeling u(c) using a Beta distribution with
parameters α=β =2.
Among the existing evaluation metrics, C-score, MSU, and H stand out for their lin-
ear relation with TCC, allowing for model ranking coherent with TCC. However, each has
limitations. C-score,whiledimensionless,lacksanupperbound,whichcancomplicatecom-
parisons across different datasets, as its magnitude depends on dataset-specific properties,
such as the number of examples and the proportion of actual positives. MSU and H are
normalizedwithinthe[0,1]intervalonlywhenTCC =0;ifthisconditionisnotmet,the
min
absence of a consistent lower bound may affect interpretability and comparability.
AsabetteralternativetoC-score,MSU,andH,inthenextsectionweproposeaweighted
version of the well-known accuracy metric, normalized between 0 and 1. In the case of
example-independent Unit Classification Costs (UCCs), this metric not only ranks classi-
fiers consistently with the Total Classification Cost (TCC), but also enables performance
comparisonacrossdifferentdatasetsandsupportsTCCminimizationonthetargetdataset,
providedthattheratioofpositiveexamples(orthepriorprobabilityofapositiveoutcome)
can be estimated.
3 Weighted Accuracy and Cost-Sensitive Reweight-
ing
3.1 Weighted Accuracy
Accuracy,asdefinedinTable2,isastandardperformanceindicator,widelyusedtoevaluate
classifiers due to its simplicity: it measures the proportion of correct predictions over the
totalnumberofexamples. However,itassumesequalimportanceforalltypesofclassification
outcomes, deviating from TCC in the presence of unequal misclassification costs, and it is
often considered inappropriate in imbalanced scenarios.
Toaddresstheselimitations,wedefineaWeightedAccuracy(WA),whichassignsdifferent
importance to positive and negative examples
wTP+(1−w)TN
WA= , (3)
wP+(1−w)N
wherew isthenormalizedweightassignedtoactualpositives(truepositivesandfalsenega-
tives),and1−wistheweightassignedtoactualnegatives(falsepositivesandtruenegatives).
If we choose the weight w as the UCC ratio, i.e.,
w=r , (4)
C
5

with
C
|     |     |     | r = | FN , |     | (5) |
| --- | --- | --- | --- | ---- | --- | --- |
C
C FN +C FP
then WA becomes linearly related to the TCC defined in Eq. 2; indeed, substituting Eqs. 4
| and 5 into | Eq. 3, | we obtain |     |     |     |     |
| ---------- | ------ | --------- | --- | --- | --- | --- |
TCC−TCC min
|     |     |     | WA=1− |     | ,   | (6) |
| --- | --- | --- | ----- | --- | --- | --- |
TCC −TCC
|     |     |     |     | max | min |     |
| --- | --- | --- | --- | --- | --- | --- |
whereTCC max =C FN P+C FP Nisthemaximumpossibleclassificationcost. Thisexpression
shows that WA is analogous to the C-score, MSU, and H metrics discussed in Section 2.2,
whileprovidingamoreintuitiveinterpretationandamoreconsistentnormalizationscheme.
ItalsodemonstratesthatEq.3offersamoreprincipledwaytointroducecost-basedweighting
| into accuracy | than, | for example, | WCA (see | Table 2). |     |     |
| ------------- | ----- | ------------ | -------- | --------- | --- | --- |
Consider a scenario in which the UCC of a false negative is nine times larger than that
associatedwithafalsepositive(r C =0.9),andassumethatpositiveexamplesconstitute20%
of the dataset. Let M denote a classifier that always predicts the negative label, and M
|     |     | 1   |     |     |     | 2   |
| --- | --- | --- | --- | --- | --- | --- |
a classifier characterized by TP = 15, FN = 5, TN = 50, and FP = 30; the corresponding
accuracies are 80% and 65%, respectively, while WA(M )≃30% and WA(M )≃71%.
1 2
Importantly,thefailureofaccuracyinthisexampledoesnotarisebecausepredictingonly
themajorityclassshouldpersebepenalized. Rather,itresultsfromthestrongasymmetryin
theUCCs,whichmakesfalsenegativessubstantiallymorecostlythanfalsepositives;indeed,
when UCCs are balanced (r = 0.5), WA coincides with accuracy for any classification
C
outcome.
Forexample-independentUCCs,WAwiththeweightinEq.5ranksconfusionmatricesin
theexactreverseorderofTCC.Therefore,maximizingWAisequivalenttominimizingTCC
and,byextension,maximizingRoI.Byconstruction,WAisnormalizedtotheinterval[0,1]
andisindependentofthetestsetsize;thismakesitsuitableforcomparingmodelsevaluated
on different datasets, as long as the class distribution (i.e., P/N ) remains the same. In
tot
Sections3.3and3.4,weshowhowWAcanbestraightforwardlyadaptedtocompareresults
across datasets with different class distributions by appropriately adjusting the weight w.
| 3.2 Expected |     | Weighted | Accuracy |     |     |     |
| ------------ | --- | -------- | -------- | --- | --- | --- |
When the value of w cannot be precisely determined, a probabilistic approach may be
adopted: we introduce a probability density function u(w) over the weight w, allowing
| us to define | the Expected |     | Weighted Accuracy | (EWA)        |     |     |
| ------------ | ------------ | --- | ----------------- | ------------ | --- | --- |
|              |              |     | (cid:90)          | 1            |     |     |
|              |              |     | EWA=              | dwWA(w)u(w). |     | (7) |
0
AlthoughthisformulationsharessimilaritieswiththeH-measureintroducedin[42,14],itis
notequivalent,sinceintheH-measure,theintegralsofTCC(c)andTCC max (c)arecomputed
| separately, | as shown | in Table | 2.  |     |     |     |
| ----------- | -------- | -------- | --- | --- | --- | --- |
Dependingontheavailableinformationaboutthecostdistribution,u(w)canbemodeled
usingaBetadistribution(asdiscussedinSection2.2),orconstructedasacustomdistribution
over a plausible range of w values. If the support of u(w) is narrow – e.g., u(w) > 0 only
withinasmallinterval–thenEWAcanbeapproximatedbyWA.Forinstance,foranarrow
interval [w¯−δ,w¯+δ], we have EWA = WA(w¯)+O(δ2), which implies that EWA can be
| well approximated |     | by evaluating | WA at the | midpoint | w¯ of the interval. |     |
| ----------------- | --- | ------------- | --------- | -------- | ------------------- | --- |
| 3.3 Handling      |     | Class         | Imbalance | through  | Reweighting         |     |
Weproposeareweightingapproachforhandlingclassimbalanceinclassifierevaluationthat
avoids resampling, thereby preserving the original dataset and its statistical properties.
6

Consider a generic performance metric that can be expressed as a weighted average:
|     |     |     |     |     |     | (cid:80) v | k   |     |     |     |
| --- | --- | --- | --- | --- | --- | ---------- | --- | --- | --- | --- |
|     |     |     |     |     | K = | a a        | a,  |     |     | (8) |
(cid:80)
|     |     |     |     |     |     | v   | a   |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
a
where k is the contribution of example a, v its associated weight, and the sum runs over
|     | a        |                 |     |     |     | a   |     |     |     |     |
| --- | -------- | --------------- | --- | --- | --- | --- | --- | --- | --- | --- |
| all | examples | in the original | set | S.  |     |     |     |     |     |     |
Accuracy and WA are special cases of this formulation, with k =1 (0) if example a is
a
correctly (incorrectly) classified. For accuracy, all examples contribute uniformly:
1
|     |     |     |     |     | v (accuracy)= |     | ,   |     |     | (9) |
| --- | --- | --- | --- | --- | ------------- | --- | --- | --- | --- | --- |
|     |     |     |     |     | a             |     | N   |     |     |     |
tot
| while | WA (defined | in  | Eq. 3) | introduces | class-dependent |     |     | weights: |     |     |
| ----- | ----------- | --- | ------ | ---------- | --------------- | --- | --- | -------- | --- | --- |
(cid:40)
|     |     |     |     |         |           | w   | if a∈S |     |     |      |
| --- | --- | --- | --- | ------- | --------- | --- | ------ | --- | --- | ---- |
|     |     |     |     |         | wP+(1−w)N |     |        | +   |     |      |
|     |     |     | v   | a (WA)= |           |     |        | .   |     | (10) |
|     |     |     |     |         |           | 1−w | if a∈S |     |     |      |
|     |     |     |     |         | wP+(1−w)N |     |        | −   |     |      |
Assume that we wish to estimate the value of K on a balanced version of S containing
the same number of positive and negative examples2. Rather than explicitly constructing
such a dataset through rebalancing techniques, we can equivalently rescale each weight v
a
according to the relative frequency of its class; after normalization, this procedure yields
(cid:40)
|       |              |      |           |            |         | Nva | if a∈S |     |     |      |
| ----- | ------------ | ---- | --------- | ---------- | ------- | --- | ------ | --- | --- | ---- |
|       |              |      | vbalanced |            | NV++PV− |     |        | +   |     |      |
|       |              |      |           |            | =       |     |        | ,   |     | (11) |
|       |              |      |           | a          |         | Pva | if a∈S |     |     |      |
|       |              |      |           |            | NV++PV− |     |        | −   |     |      |
| where | V = (cid:80) | v    | and V     | = (cid:80) | v       | .   |        |     |     |      |
|       | +            | a∈S+ | a         | −          | a∈S−    | a   |        |     |     |      |
This formulation is consistent with previous findings [21, 32, 33, 23, 41]. Although the
focus of this work is on classifier evaluation, the proposed reweighting framework applies to
| any | metric of      | the form | in Eq.    | 8, including |            | loss functions |        | (see Section | 4.4.1). |     |
| --- | -------------- | -------- | --------- | ------------ | ---------- | -------------- | ------ | ------------ | ------- | --- |
|     | In particular, | for      | accuracy, | the          | rebalanced | weights        | become |              |         |     |
(cid:40)
|     |     |     |                      |     |     |     | 1 if | a∈S   |     |      |
| --- | --- | --- | -------------------- | --- | --- | --- | ---- | ----- | --- | ---- |
|     |     |     | vbalanced(accuracy)= |     |     |     | 2P   | +     | ,   | (12) |
|     |     |     | a                    |     |     |     | 1    |       |     |      |
|     |     |     |                      |     |     |     | if   | a∈S − |     |      |
2N
| which | corresponds | to  | evaluating  | accuracy |     | on a perfectly |     | balanced | dataset. |     |
| ----- | ----------- | --- | ----------- | -------- | --- | -------------- | --- | -------- | -------- | --- |
| 3.4   | Cost-Based  |     | Reweighting |          |     |                |     |          |          |     |
We now extend the metric in Eq. 8 to the case of unequal, example-independent UCCs
C andC ;toaccountforasymmetricUCCs,weintroduceaclass-dependentreweighting
| FN  | FP  |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
scheme in which positive and negative examples are weighted proportionally to C and
FN
| C FP | , respectively. | After | normalization, |     | the      | transformed |     | weights | become |     |
| ---- | --------------- | ----- | -------------- | --- | -------- | ----------- | --- | ------- | ------ | --- |
|      |                 |       |                |     | (cid:40) | rCva        | if  | a∈S     |        |     |
+
|     |          |                 | vUCC | =           | rCV++(1−rC)V− |     |          | .      |     | (13) |
| --- | -------- | --------------- | ---- | ----------- | ------------- | --- | -------- | ------ | --- | ---- |
|     |          |                 | a    |             | (1−rC)va      |     | if       | a∈S    |     |      |
|     |          |                 |      |             | rCV++(1−rC)V− |     |          | −      |     |      |
|     | Applying | this cost-based |      | reweighting | scheme        | to  | accuracy | yields |     |      |
(cid:40)
|     |     |     |                 |     |     | rC          |     | if a∈S |     |      |
| --- | --- | --- | --------------- | --- | --- | ----------- | --- | ------ | --- | ---- |
|     |     |     | vUCC(accuracy)= |     |     | rCP+(1−rC)N |     |        | + . | (14) |
|     |     |     | a               |     |     | 1−rC        |     |        |     |      |
|     |     |     |                 |     |     |             |     | if a∈S | −   |      |
rCP+(1−rC)N
Equation 14 coincides with Eq. 10 when the weight w is defined as in Eq. 4; therefore,
WA can be interpreted as a cost-reweighted version of standard accuracy according to the
proposed framework.
2ThegeneralizationtoarbitraryclassratiosisdiscussedinSection3.5.
7

AsdiscussedinSection3.1,maximizingWAisequivalenttominimizingTCCinthepres-
ence of example-independent UCCs (see Eq. 6). Comparing the balancing-based reweight-
ing in Eq. 12 with the cost-based reweighting in Eq. 14, we conclude that maximizing
accuracy on a rebalanced dataset is equivalent to minimizing TCC only when 1/(2P) ≃
| r C /[r C P+(1−r | C   | )N], i.e., | when |     |     |     |     |     |     |
| ---------------- | --- | ---------- | ---- | --- | --- | --- | --- | --- | --- |
N
|     |     |     |     | r   | C ≃ | .   |     |     | (15) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ---- |
N
tot
This condition is implicitly assumed by standard rebalancing techniques and by several
metrics designed to correct class imbalance, yet it does not hold in general; when Eq. 15 is
| violated,  | such approaches |         | may produce | substantially |     | misleading |     | evaluations. |     |
| ---------- | --------------- | ------- | ----------- | ------------- | --- | ---------- | --- | ------------ | --- |
| 3.5 Target |                 | Dataset | Reweighting |               |     |            |     |              |     |
The weighting scheme defined in Eq. 11 aims to correct class imbalance, or equivalently
estimating the metric after positive and negative classes are balanced to the same fraction
of examples. However, for cost-sensitive evaluation, the relevant quantity is the class dis-
tribution in the target dataset, i.e., the dataset on which the classifier will be deployed and
decisions will be made. This could correspond to a production environment in business or
a patient population in healthcare. Let us then distinguish between: (i) the development
dataset, with N examples and ratio of positive examples r =P/N , used for training,
|     | tot |     |     |     |     |     | +   | tot |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Nt
validation, and testing and (ii) the target dataset, with tot examples and ratio of positive
examples rt = P /Nt , which may differ from r . If the target dataset is not directly
|     | +   | t tot |     |     |     | +   |     |     |     |
| --- | --- | ----- | --- | --- | --- | --- | --- | --- | --- |
accessible, rt can be interpreted as a base rate, i.e., the prior probability of a positive out-
+
come [27].
Toestimateametriconthetargetdatasetusingthedevelopmentdataset,wegeneralize
Eq. 11 as:
|     |     |     |     |      | t          |        |     |     |      |
| --- | --- | --- | --- | ----- | ---------- | ------ | --- | --- | ---- |
|     |     |     |     |       | R + v a    | if a∈S |     |     |      |
|     |     |     |     |  tV  | t          |        | +   |     |      |
|     |     |     | vt  | = R + | + + R − V− |        | ,   |     | (16) |
|     |     |     | a   |       | R t v      |        |     |     |      |
|     |     |     |     |      | − a        | if a∈S |     |     |      |
|     |     |     |     | R tV  | + R t V−   |        | −   |     |      |
|     |     |     |     | +     | + −        |        |     |     |      |
where Rt =rt/r + and Rt =(1−rt)/(1−r + ). As expected, Eq. 16 reduces to Eq. 11 if
|            | + +     |              | −         | +   |             |       |     |     |     |
| ---------- | ------- | ------------ | --------- | --- | ----------- | ----- | --- | --- | --- |
| the target | dataset | is perfectly | balanced, |     | i.e., if rt | =0.5. |     |     |     |
+
This rescaling also enables consistent comparison of metrics calculated across datasets
with different class distributions by mapping them to a common target distribution.
To further extend Eq. 16 to the case of unequal, example-independent UCCs C FN and
C FP , we combine target-distribution reweighting with the cost-based reweighting scheme
| introduced | in Eq.     | 13, obtaining |     |         |                 |       |        |     |      |
| ---------- | ---------- | ------------- | --- | ------- | --------------- | ----- | ------ | --- | ---- |
|            |            |               |     |        | t               |       |        |     |      |
|            |            |               |     |         | R + rC v a      |       | if a∈S |     |      |
|            |            |               |     |  trCV+ | t               |       |        | +   |      |
|            |            | vt,UCC        | =   | R +     | + R − (1 −rC)V− |       |        | ,   | (17) |
|            |            | a             |     | R       | t (1 − rC )     | va    |        |     |      |
|            |            |               |     |        | −               |       | if a∈S |     |      |
|            |            |               |     | R trC V | ++ R t (1 −     | rC)V− |        | −   |      |
|            |            |               |     | +       | −               |       |        |     |      |
| where r    | is defined | in Eq.        | 5.  |         |                 |       |        |     |      |
C
Equation17providesaunifiedframeworktoestimatemetricsoftheforminEq.8while
jointly accounting for unequal UCCs and differences between the class distributions of the
development and target datasets. If misclassification costs are equal (r =1/2), it reduces
C
to Eq. 16; on the other hand, if the class proportion in target and development datasets
| coincide | (rt =r ), | it reduces | to  | Eq. 13. |     |     |     |     |     |
| -------- | --------- | ---------- | --- | ------- | --- | --- | --- | --- | --- |
+ +
Applying Eq. 17 to the uniform weights of accuracy (Eq. 9) yields a WA formulation
| (Eq. 10) | with class | weight |     |      |       |      |     |     |      |
| -------- | ---------- | ------ | --- | ---- | ----- | ---- | --- | --- | ---- |
|          |            |        |     |      | Rt    | r    |     |     |      |
|          |            |        |     | w =  | +     | C    | .   |     | (18) |
|          |            |        |     | t Rt | r +Rt | (1−r | )   |     |      |
|          |            |        |     | +    | C −   | C    |     |     |      |
Equation18determinestheWAweightprovidedthattheUCCratior andtheratioof
C
positivesrt inthetargetdatasetcanbeestimated. InAppendixA,wedescribeaprocedure
+
8

to estimate the weight w in the presence of uncertainty in r . If substantial uncertainty on
C
w remains after this estimation procedure, the probabilistic approach introduced in Section
3.2 can be adopted.
Finally, Eq. 18 shows that a weighting scheme (or, alternatively, class rebalancing) is
required for accuracy unless
rtr
r ≃ + C (19)
+ 1−rt −r +2rtr
+ C + C
whichisthereforetheconditionunderwhichstandardaccuracyisequivalenttoTCC.Ifthe
target dataset has the same positive rate as the development dataset (rt ≃ r ), Eq. 19
+ +
reduces to the equal-UCCs condition (r ≃1/2).
C
3.6 Example-Dependent Unit Classification Costs
Althoughmostconfusion-matrix-basedliteratureassumesthatUCCsareexample-independent,
in many real-world use cases they actually depend on the individual example a [44, 43]. In
suchcases,evaluatingtheTCC(seeEq.1)requiresspecifyingthesetS (S )ofmisclas-
FN FP
sified positive (negative) examples, rather than simply their count FN (FP). This implies
thatthesameconfusionmatrixmaycorrespondtodifferentTCCvaluesdependingonwhich
examples are misclassified.
We can extend the shifted UCCs defined in Section 2.2 to the example-dependent case
as EFP = eFP −eTN and DFN = dFN −dTP; this allows us to rewrite Eq. 1 as TCC =
a a a a a a
(cid:80) DFN+ (cid:80) EFP+TCC , where TCC = (cid:80) dTP+ (cid:80) eTN is the
a∈SFN a a∈SFP a min min a∈S+ a a∈S− a
minimum achievable cost, corresponding to perfect classification. If we express the UCCs
as DFN = C +δ and EFP = C +ϵ – where C (C ) is the average cost over
a FN a a FP a FN FP
thepositives(negatives)ofthetargetdataset3, andδ andϵ representexample-dependent
a a
deviations – we obtain
(cid:88) (cid:88)
TCC=C ·FN+C ·FP+TCC + δ + ϵ . (20)
FN FP min a a
a∈SFN a∈SFP
Equation20extendsEq.2byaddingtermsthatdependonthespecificmisclassifiedex-
amples;Eq.2isexactforagivenclassificationoutcomeonlyiftheaveragesC andC are
FN FP
computed on the subset of misclassified positives and misclassified negatives, respectively.
Since UCCs are typically estimated a priori, without knowing which examples will be mis-
classified, deviations between Eq. 20 and Eq. 2 are therefore expected. For instance, in the
limiting case where a subset of massive examples accounts for most of the TCC, the counts
FN and FP become largely uninformative for determining the TCC, and the dominant fac-
toriswhetherthesemassiveexamplesarecorrectlyclassified. Inthisregime,systematically
analyzed in Section 4.3, the fluctuations terms δ and ϵ become decisive.
a a
(cid:80) (cid:80)
In many practical situations, however, the terms δ and ϵ are not prominent,
a a a a
even when the single fluctuations δ or ϵ are comparable to or larger than the averages
a a
C andC . InSection4weillustratethisbehaviorthroughtworepresentativeusecases,
FN FP
covering all possible regimes in terms of r and r .
+ C
4 Empirical Evaluation against Total Classification
Cost
Here,wecompareWA,EWA(introducedinSection3.2),andthemetricsdescribedinTable
2, using TCC as a reference in two example-dependent scenarios.
3If these averages are not known for the target dataset, they may be estimated from the devel-
opmentdataset.
9

TheTCCiscomputedaccordingtoEq.20,whilethecost-sensitivemetricsWCA,WRA,
ACD, WA, EWA are calculated using average UCCs. The H metric is computed using
a Beta distribution with α = β = 2 for the UCC ratio, as recommended by [14] when
no prior information about the cost distribution is available. H informed and EWA are
computed using a Beta distribution whose mean and variance match those of the empirical
u(c)distribution4. MSUandC-scorearenotexplicitlycomputed,astheyrankclassification
| outcomes | identically | to  | WA, differing |     | only in their | normalization | schemes. |
| -------- | ----------- | --- | ------------- | --- | ------------- | ------------- | -------- |
ToquantifythesimilaritybetweeneachmetricandTCC,weidentifyasampleofclassi-
fication outcomes and rank them according to the metric and TCC, respectively; hence we
| compute | the correlation |     | between | the two | rankings, | using: |     |
| ------- | --------------- | --- | ------- | ------- | --------- | ------ | --- |
•
the standard Spearman coefficient [39], which corresponds to the Pearson correlation
| between | rank | variables; |     |     |     |     |     |
| ------- | ---- | ---------- | --- | --- | --- | --- | --- |
•
the weighted Spearman coefficient [25, 24], which assigns greater importance to the
correct ordering of top-ranked outcomes, i.e., those with low TCC or high metric
values, which are typically the focus during model selection and validation; for this
| coefficient |     | we use | an additive | weighting |     | scheme and n | =2. |
| ----------- | --- | ------ | ----------- | --------- | --- | ------------ | --- |
0
| 4.1 Experimental |     |     | Setup |     |     |     |     |
| ---------------- | --- | --- | ----- | --- | --- | --- | --- |
Real-world classification problems vary substantially in terms of both the target dataset,
particularly its imbalance ratio, and the UCCs. Two key quantities characterizing each
scenario are the ratio of positive examples r and the UCC ratio r , both ranging in [0,1].
|     |     |     |     |     | +   |     | C   |
| --- | --- | --- | --- | --- | --- | --- | --- |
Tosystematicallyexplorethefullrangeofpossible(r C ,r + )scenarios,weconstructadiscrete
two-dimensional grid over the domain [0,1]×[0,1]. For each pair (r C ,r + ) in the grid, we
generate 100 samples by randomly assigning the positive label (churn) to a subset of P =
round(r N )examplesineachsample. Foreachsample,wegenerateN +1classification
| +   | tot |     |     |     |     |     | tot |
| --- | --- | --- | --- | --- | --- | --- | --- |
outcomes by iterating over all possible numbers P of predicted positives and assigning
pred
the P pred predicted positive labels to a random subset of examples in the sample.
ForeachmetricY,theseoutcomesarerankedaccordingtobothTCCandY,generating
two rankings that are compared using the correlation coefficients described above. The
correlations obtained for the 100 samples are then averaged, yielding a mean correlation
| value for | each metric | Y   | and each | point | in the | (r ,r ) grid. |     |
| --------- | ----------- | --- | -------- | ----- | ------ | ------------- | --- |
+ C
The code used to run the experiments and generate the results described in this work
is available at https://github.com/plombardML/weighted-accuracy. Experiments were
conductedonaWindowsmachinewith16GBRAMandanIntel(R)Core(TM)i5-102100U
CPU@1.60GHz2.10GHz,usingPython,thescipylibrary,andtheimplementationin[24]
| for computing | the       | weighted | Spearman |     | coefficient. |     |     |
| ------------- | --------- | -------- | -------- | --- | ------------ | --- | --- |
| 4.1.1         | Use Cases |          |          |     |              |     |     |
To work with data that are as realistic and relatable as possible, we consider two well-
known use cases characterized by example-dependent costs; for each use case, we tune a
cost parameter so that the resulting UCC ratio r matches the values specified by the grid
C
| described | above | (see Appendix |     | B). |     |     |     |
| --------- | ----- | ------------- | --- | --- | --- | --- | --- |
1. Thefirstusecaseischurnprediction,wherethemodelpredictswhetheracustomerwill
churnwithinaforthcomingtimewindow. Thecostofafalsepositiveincludesthetime
andeffortofthecommercialteamtocontactthecustomerandimplementaretention
measure as well as the cost of that measure. Conversely, the cost of a false negative
dependsontherevenuethecompanywouldhaveearnedhadthecustomernotchurned;
4To approximate the empirical distribution u(c) with a Beta distribution f(c;α,β), we set α=
c¯2(1−c¯)/σ2−c¯andβ=α(1−c¯)/c¯. Withthischoice,uandf sharethesamemeanc¯andvariance
| σ2. | c   |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- |
c
10

this depends on the customer’s revenue and on the probability of effectiveness of the
retention measure. Customer revenues are sampled uniformly and without repetition
from the monthly charges in the Telco Customer Churn dataset from Kaggle5, while
the remaining parameters are estimated as described in Appendix B.1.
2. Thesecondusecaseiscreditscoring,wherethemodelpredictswhetheracustomerwill
defaultonacontractedfinancialobligation. Thecostofafalsenegativeisproportional
to the customer’s debt (credit line). In contrast, the cost of a false positive reflects
the loss of profit from rejecting a customer who would not default; since, in case of
rejection, the institution typically lends to an alternative customer, this cost depends
on the expected average profit and risk of a representative customer. The customers’
monthlyincomeanddebtratioaresampleduniformlyandwithoutrepetitionfromthe
dataset of the 2011 Kaggle competition Give Me Some Credit6, while the remaining
parameters are estimated as described in Appendix B.2.
In both use cases, the average UCCs and their fluctuations strongly depend on the pair
(r ,r ). Comparingthestandarddeviationsσ andσ ofδ andϵ withthecorresponding
C + δ ϵ a a
averagecostsC andC ,weobservesubstantialvariability. Forchurnprediction,theratio
FN FP
σ /C ranges from 0.03 to 47 (median 0.79). For credit scoring, it ranges from 0.0002 to
δ FN
51 (median 0.16), while σ /C ranges from 0.005 to 2800 (median 2.38). In many (r ,r )
ϵ FP C +
scenarios the fluctuations are therefore substantial, and a close agreement between Eq. 2
and Eq. 20 – that is, between WA and the example-dependent TCC – cannot be assumed
a priori. In both cases the target dataset is assumed to be equivalent to the development
dataset in terms of ratio of positives (r = rt), with the latter containing 200 examples
+ +
(N =200).
tot
4.2 Results
TheresultsofthiscorrelationanalysisareshowninFigures1and2forthestandardSpear-
mancorrelationinthechurnpredictionandcreditscoringusecases,respectively,andinFig-
ures3and4forthecorrespondingweightedSpearmancorrelation. Severalmetrics–namely
accuracy, MCC, Kappa, G-mean, ROC-AUC, CBA, IAM, P4, WCA, WRA, ACD, H, H
informed, WA, and EWA exhibit symmetry under relabeling of class + and −, reflected in
theheatmapsasqualitativesymmetryunderthetransformation(r ,r )→(1−r ,1−r )7.
+ C + C
Whilesymmetryisoftenconsidereddesirable, ourfocushereisonrobustnessofcorrelation
with TCC. Thus, we classify metrics based on the qualitative pattern of their correlation.
4.2.1 Anti-Diagonal Robust Metrics
As discussed in Section 3.4 for example-independent costs, when the ratio of positives in
the development and target dataset is the same, standard accuracy is perfectly consistent
with TCC if r =1/2. However, we can also expect a good alignment with TCC when the
C
majority class has the larger misclassification cost (i.e., r and r are both small or both
C +
large): in this case balancing techniques are counterproductive. Indeed, in these regions,
accuracy outperforms many sophisticated metrics, particularly those designed to handle
class imbalance per se, without considering the UCC ratio. Besides standard accuracy, also
CBA, IAM, WCA, and H exhibit strong correlation with TCC close to the anti-diagonal of
the heatmap (i.e., the line r = r ). More precisely, accuracy, CBA, IAM, and H diverge
C +
significantlyfromTCCintworegions: (i)r ≲0.5withr ≳1−r and(ii)r ≳0.5with
+ C + +
r ≲1−r . WCAexhibitsaslightlydifferentpattern,divergingfromTCCin(i)r ≲0.5,
C + +
with 0.5≲r ≲1−r and (ii) r ≳0.5, with 1−r ≲r ≲0.5. Standard and weighted
C + + + C
5Datasetavailableathttps://www.kaggle.com/datasets/blastchar/telco-customer-churn
6Datasetavailableathttps://www.kaggle.com/c/GiveMeSomeCredit
7Thesymmetryisqualitative,astheasymmetriccostdistributionsbreakexactsymmetry.
11

Figure 1: Heatmaps showing standard Spearman correlation between TCC and
the metrics in Table 2 and Section 3.1 over a grid of values of r (horizontal axis)
+
and r (vertical axis) for the churn prediction use case. To improve readability,
C
correlation coefficients are multiplied by 10 and rounded.
Spearman coefficients (Figures 1, 2, 3, and 4) display analogous patterns for this group of
metrics.
4.2.2 Main Diagonal Symmetric Metrics
Several metrics exhibit qualitatively symmetric or antisymmetric correlation patterns with
respect to reflection along the main diagonal (r = 1−r ). According to the findings in
C +
Section3.3,metricsdesignedtocompensateforclassimbalancewithoutaccountingforUCCs
areexpectedtoshowgoodcorrelationwithTCConlyforr ≃1−r ,i.e.,closetothemain
C +
diagonal. This pattern is observed for informedness, markedness, MCC, Cohen’s Kappa,
WRA and ROC-AUC (single parameter), which we thus refer to as rebalancing metrics. In
theweightedcase,thedeclineincorrelationawayfromthediagonalismorepronouncedfor
informedness, ROC-AUC, WRA, and even stronger for Kappa.
Recall,F1,andB-ROCshowinsteadstrongcorrelationwithTCCabovethemaindiag-
onal and strong anticorrelation below (less pronounced for F1 in the standard correlation),
while specificity shows the opposite behavior. Precision and NPV behave differently de-
pending on whether the standard or weighted correlation coefficient is used: in the former
case (Figures 1 and 2), they behave as rebalancing metrics, with good correlation along the
diagonal, which fades toward uncorrelation or even anticorrelation at the extremes of r .
+
Whenconsideringtheweightedcorrelationcoefficient(Figures3and4),thelineofmaximal
correlation shifts slightly above (for precision) or below (for NPV), with the diagonal itself
dividing the heatmap into two regions qualitatively similar to recall and specificity. P4 and
G-mean, when analyzed with the standard correlation (Figures 1 and 2), behave as the re-
12

Figure2: HeatmapsshowingstandardSpearmancorrelationbetweenTCCandthe
metrics in Table 2 and Section 3.1 over a grid of values for r + (horizontal axis) and
r (vertical axis) for the credit scoring use case. Values with r ≥ 1/(1+r ) are
| C   |     |     |     | C   | +   |
| --- | --- | --- | --- | --- | --- |
omitted due to consistency conditions (more details in Appendix B.2). To improve
| readability, | correlation coefficients | are multiplied | by 10 and rounded. |     |     |
| ------------ | ------------------------ | -------------- | ------------------ | --- | --- |
balancingmetrics,withoveralllowercorrelation. Undertheweightedcorrelation(Figures3
and4),theyexhibitareversedpattern,withlowcorrelationalongthediagonalandstronger
| correlation | elsewhere.      |         |     |     |     |
| ----------- | --------------- | ------- | --- | --- | --- |
| 4.2.3       | Globally Robust | Metrics |     |     |     |
ACD,Hinformed,WA,andEWAarethetop-performingmetrics,showingstrongcorrelation
with TCC across nearly all scenarios. ACD performs slightly worse than the others in
this group, particularly under the weighted correlation (Figures 3 and 4), where it exhibits
weaknesses qualitatively similar to those of accuracy, CBA, IAM, and H. The robustness
of this group of metrics was to some extent expected, as they incorporate the example-
independent TCC (Eq. 2, with TCC =0). However, Figures 1, 2, 3, and 4 show robust
min
and consistent correlation with the example-dependent cost (Eq. 20), indicating that the
fluctuation terms are negligible in this scenario. We omit the heatmaps for MSU and C-
| score because | they are linearly | related to WA.             |     |            |     |
| ------------- | ----------------- | -------------------------- | --- | ---------- | --- |
| 4.3 Validity  | Limits            | of the Example-Independent |     | Approxima- |     |
tion
Toquantitativelyassessthelimitsoftheexample-independentapproximation(seealsoSec-
tion 3.6), we consider highly skewed, long-tailed distribution of UCCs. This scenario builds
fromthefirstusecase(churnprediction)describedinSection4.1.1,byintroducingasubset
13

Figure 3: Heatmaps showing weighted Spearman correlation between TCC and
the metrics in Table 2 and Section 3.1 over a grid of values of r (horizontal axis)
+
and r (vertical axis) for the churn prediction use case. To improve readability,
C
correlation coefficients are multiplied by 10 and rounded.
of massive customers, whose revenue dominates the overall distribution. Specifically, we
defineN massivecustomerswhosecombinedrevenueaccountsforafractionf ofthetotal
mc r
revenue.
Two quantities characterize the degree of skewness and tail heaviness of the revenue
distribution: the fraction of massive customers
N
f = mc
mc N
tot
andthefractionf ofthetotalrevenuegeneratedbythesecustomers. Wethereforeanalyze
r
agridoff ,f values,withf rangingfrom20%to99%andf rangingfrom1%to20%.
r mc r mc
Figure 5 reports the standard Spearman correlation between TCC and WA for differ-
ent combinations of f and f . As expected, WA exhibits increasing discrepancies with
r mc
TCC as the revenue distribution becomes more concentrated and heavy-tailed; i.e., these
discrepancies are significant for large values of f (≳0.6) and small values of f (≲0.02).
r mc
Conversely, when the revenue fraction associated with the massive customers is more
moderate (f ≲ 0.4) or the fraction of massive customers is sufficiently large (f ≳ 0.05),
r mc
WA maintains relatively strong correlation and near-consistent behavior with respect to
TCC. These experiments provide therefore an empirical estimation of the validity limits of
WA, and more generally of confusion-matrix-based evaluation metrics, in the presence of
example-dependent costs with highly skewed distributions. The procedure to explore the
r ,r parametergridisthesameasthatdescribedinSection4.1andthecodeiscontained
C +
in the same repository.
14

Figure4: HeatmapsshowingweightedSpearmancorrelationbetweenTCCandthe
metrics in Table 2 and Section 3.1 over a grid of values for r + (horizontal axis) and
r (vertical axis) for the credit scoring use case. Values with r ≥ 1/(1+r ) are
| C   |     |     |     |     | C   | +   |
| --- | --- | --- | --- | --- | --- | --- |
omitted due to consistency conditions (more details in Appendix B.2). To improve
| readability,  | correlation | coefficients | are multiplied | by 10 and  | rounded. |     |
| ------------- | ----------- | ------------ | -------------- | ---------- | -------- | --- |
| 4.4 Practical |             | Guidelines   | for Classifier | Evaluation |          |     |
The proposed evaluation framework is applicable across all stages in which classifier perfor-
mance is assessed: primarily model validation and testing, but also model training.
| 4.4.1 | Model | Training |     |     |     |     |
| ----- | ----- | -------- | --- | --- | --- | --- |
Model training typically relies on surrogate loss functions that are differentiable and, in
many cases, convex. Common choices for binary classification include binary cross entropy,
hinge loss, squared loss, and exponential loss. All these loss functions can be expressed in
the form of Eq. 8 with uniform weights v a =1/N tot ; their per-example contributions are
•
| binary | cross | entropy: | k a =−[y a log(p a )+(1−y | a )log(1−p | a )]; |     |
| ------ | ----- | -------- | ------------------------- | ---------- | ----- | --- |
•
| hinge   | loss: | k a =max(0,1−y | a p a ); |     |     |     |
| ------- | ----- | -------------- | -------- | --- | --- | --- |
| •       |       |                | )2;      |     |     |     |
| squared | loss: | k a =(y a      | −p a     |     |     |     |
•
| exponential |     | loss: k a =exp(−y | a p a ). |     |     |     |
| ----------- | --- | ----------------- | -------- | --- | --- | --- |
Here,y a denotesthetruelabelofexamplea(0or1)andp a thecorrespondingmodeloutput,
| e.g., the | predicted | probability | of a being in positive | class. |     |     |
| --------- | --------- | ----------- | ---------------------- | ------ | --- | --- |
The reweighting framework introduced in Sections 3.3, 3.4, and 3.5 can therefore be
directly applied to these loss functions, enabling principled handling of class imbalance and
unequal UCCs.
15

Figure 5: Heatmaps showing standard Spearman correlation between TCC and
WAovera gridofvaluesfor r (horizontal axis)andr (vertical axis)for the churn
+ C
prediction with extreme statistics use case. Results are reported for different
values of the fraction f of massive customers and the fraction f of total revenue
mc r
associated with them. To improve readability, correlation coefficients are multiplied
by 10 and rounded.
Thisrequiresestimatingtheratioofpositivesrt inthetargetdatasetandtheUCCsratio
+
r . The latter can be estimated using the procedure described in Appendix A; conversely,
C
whenthetargetdistributionisunavailable,rt canbeapproximatedbythepositivefraction
+
r observed in the training set, provided that no substantial distribution shift is expected
+
between the development and target datasets. The reweighted loss function is obtained by
rescaling the original weights v according to Eq. 17.
a
If the original loss is consistent with TCC minimization under balanced conditions and
equalUCCs,thepreviouslydiscussedreweightedlossremainsconsistentinthemoregeneral
setting characterized by class imbalance (rt ̸= r ) and asymmetric misclassification costs
+ +
(r ̸=1/2).
C
4.4.2 Model Validation and Testing
During model validation and testing, the results presented in Section 4.2 indicate that WA
(or EWA in the presence of substantial uncertainty in UCCs) is well aligned with TCC
minimization. Thisholdsnotonlyforexample-independentUCCs,forwhichtheequivalence
is formally established in Eq. 6, but also for example-dependent UCCs, provided that their
distribution does not exhibit extremely long tails (see Section 4.3).
In contrast, the use of alternative metrics, included several widely adopted evaluation
measures, may lead to sub-optimal model selection, with a potentially significant impact in
terms of TCC; in the following, we quantify this effect.
Consider a validation setting in which classifier hyperparameters must be selected. To
16

emulate model performance across different hyperparameter configurations, we assume a
parametric relationship between the True Positive Rate (TPR, i.e., TP/P) and the False
Positive Rate (FPR, i.e., FP/N), namely TPR = (FPR)2, which corresponds to an area
under the ROC curve of 2/3. The candidate models are generated from this FPR-TPR
relationship, by uniformly sampling FPR in the interval [0,1] with step size 0.01.
We analyze four representative scenarios:
1. mild class imbalance (r = 0.2) with substantially higher cost associated with false
+
positives (r =0.01);
C
2. mild imbalance (r = 0.2) with substantially higher cost associated with false nega-
+
tives (r =0.99);
C
3. strong imbalance (r = 0.01) with higher cost associated with false negatives (r =
+ C
0.9);
4. strong imbalance (r = 0.01) with higher cost associated with false positives (r =
+ C
0.1).
Foreachscenario,weselect,fromthepreviouslydescribedsetofcandidates,theoptimal
model according to each evaluation metric X under consideration. We then compute the
performancegap∆TCC,definedasthedifferencebetweentheTCCofthemodelselectedby
metricX andtheminimumachievableTCCamongallcandidatemodels. Therefore,∆TCC
quantifiestheeconomicalcostinducedbythesub-optimalclassifierperformance,duetothe
use of metric X during model selection.
Toincorporateexample-dependentUCCs,weadoptthecoststructureintroducedinthe
first use case in Section 4.1.1; for each configuration, the sets of true positives and false
positivesaregeneratedviauniformrandomsamplingconsistentwiththespecifiedTPRand
FPRvalues. Thecomputationof∆TCCisrepeatedover1000independenttrials,andTable
3 reports the corresponding mean values.
Most metrics exhibit large ∆TCC values in at least one scenario, indicating that their
useformodelselectionmayleadtosubstantialeconomicallosses. Incontrast,onlyalimited
subset of metrics consistently yields low ∆TCC across all analyzed scenarios, namely the
globally robust metrics, in particular WA, H informed, and EWA; ACD, while generally
competitive, exhibits a non-negligible ∆TCC in Scenario 2.
Sinceminimizing∆TCCisequivalenttomaximizingRoI,theseresultsalsoindicatethat
usingWA,Hinformed,orEWAformodelselectionyieldsthehighestRoIacrosstheanalyzed
scenarios.
5 Conclusion
In Section 3 we introduced WA, an evaluation metric for binary classifiers that can be
interpreted as a cost-consistent weighted version of accuracy, together with a reweighting
framework – applicable to any metric or loss function that, like WA, can be expressed as a
linear combination of example-dependent quantities – for handling class imbalance in cost-
sensitive settings without relying on resampling techniques. Within this framework, we
established several key results for the case of example-independent UCCs:
• in Section 3.1 we proved that maximizing WA is equivalent to minimizing TCC;
• in Section 3.4, we derived the condition under which metrics and rebalancing tech-
niques designed to compensate class imbalance remain coherent with TCC minimiza-
tion, namely r ≃1−r (Eq. 15);
C +
• inSection3.5,wegeneralizedtheframeworktohandledevelopment andtarget datasets
with different ratios of positives and discussed the corresponding validity limits of
standard accuracy.
17

Table 3: For each metric X, we provide the difference between the TCC of the
modelselectedbyoptimizingX andtheminimalTCCinthefourvalidationscenarios
| described | in Section 4.4.2. |          |            |            |              |
| --------- | ----------------- | -------- | ---------- | ---------- | ------------ |
|           | Metric            | Scenario | 1 Scenario | 2 Scenario | 3 Scenario 4 |
|           | Accuracy          | 0        | 591        | 7          | 0            |
|           | CBA               | 795      | 565        | 7          | 0            |
|           | IAM               | 795      | 565        | 7          | 0            |
|           | H                 | 0        | 591        | 7          | 0            |
|           | WCA               | 0        | 1          | 253        | 0            |
|           | Kappa             | 0        | 591        | 253        | 3155         |
|           | Informedness      | 0        | 591        | 253        | 3155         |
|           | ROC-AUC           | 0        | 591        | 253        | 3155         |
|           | WRA               | 0        | 591        | 253        | 3155         |
|           | MCC               | 0        | 591        | 253        | 3155         |
|           | Markedness        | 3842     | 17         | 253        | 3155         |
|           | Precision         | 3916     | 1          | 253        | 3155         |
|           | NPV               | 0        | 591        | 253        | 3155         |
|           | P4                | 2778     | 292        | 253        | 3155         |
|           | G-mean            | 2778     | 292        | 154        | 1853         |
|           | Jaccard           | 3916     | 1          | 253        | 3155         |
|           | F1                | 3916     | 1          | 253        | 3155         |
|           | Recall            | 3916     | 1          | 253        | 3155         |
|           | B-ROC             | 3916     | 1          | 253        | 3155         |
|           | Specificity       | 0        | 591        | 7          | 0            |
|           | ACD               | 0        | 110        | 7          | 0            |
|           | WA                | 0        | 1          | 7          | 0            |
|           | H informed        | 0        | 1          | 7          | 0            |
|           | EWA               | 0        | 1          | 7          | 0            |
Since most real-world applications involve example-dependent UCCs, Section 4 focused
on realistic use cases characterized by heterogeneous costs, systematically exploring the full
rangeofpossiblevaluesforthecostratio(r C )andtheratioofpositives(r + ),andanalyzing
| the correlation | between | several evaluation | metrics and | TCC. |     |
| --------------- | ------- | ------------------ | ----------- | ---- | --- |
The empirical behavior of rebalancing metrics observed in Section 4.2.2 qualitatively
extends to a broad range of example-dependent scenarios the theoretical condition derived
for example-independent UCCs, namely that rebalancing-based approaches remain coher-
ent with TCC minimization only near the regime r C ≃ 1−r + (Eq. 15). More generally,
this result suggests that widely adopted methods for handling class imbalance, including
standardundersamplingandoversamplingtechniques,implicitlyrelyonassumptionsabout
the relationship between class imbalance and misclassification costs that may not hold in
realistic applications.
Among the analyzed confusion-matrix-based metrics, only H informed, EWA, WA, C-
score, and MSU exhibit robust correlation with TCC across all tested scenarios, thereby
reducing the risk of misleading model assessments. H informed and EWA require the addi-
tionalcomplexityofaprobabilisticformulation,whichincreasescomputationalcostwithout
providing clear advantages in the analyzed scenarios. WA, in contrast, combines robust
empirical behavior with a straightforward interpretation, cross-dataset comparability, and
a natural extension to scenarios in which the target and development datasets differ; these
propertiesmakeWAsuitablebothforcomparingmodelsevaluatedondifferentdatasetsand
18

forvalidation-basedhyperparametertuning. InSection4.4.2,wefurtherquantifiedtheprac-
ticalimpactofmetricchoicebymeasuringtheRoIadvantageobtainedwhenWAisusedfor
model validation instead of alternative evaluation metrics.
The experimental results in Sections 4.2 also indicate that the example-independent
approximation of TCC, obtained by neglecting the fluctuation terms in Eq. 20, remains
consistent and reliable in all examined scenarios. This observation is particularly relevant
becausesuchanapproximationisimplicitlyassumedbyanyevaluationframeworkbasedon
theconfusionmatrixformalism. Motivatedbythisconsideration,Section4.3systematically
investigated the validity limits of this approximation in the presence of highly skewed and
heavy-tailedcostdistributions,i.e.,scenariosinwhichaverysmallfractionofmassiveexam-
ples accountsforarelevantfractionofthetotalcost. Theresultsshowthatnear-consistent
behavior is still observed when either the fraction of total cost associated with the massive
examples remains moderate or the fraction of examples being massive is sufficiently large.
Appendix A Estimation of the WA Weight
In an ideal scenario, the UCCs defined in Section 2.2 can be assessed by estimating the
costassociatedtotheactionstakeninresponsetoeachtypeofclassificationoutcome(false
positive, true positive, etc.). Note that the cost matrix may include opportunity costs, i.e.,
foregonebenefitsduetomissedopportunities,asintheexamplesdescribedinSection4.1.1;
costs or benefits can be measured relatively to any baseline. However, the baseline must
remain fixed, i.e., the reference point for zero cost should not change [9].
Inpractice,estimatingthefullconfusionmatrixmaybechallenging. Therefore,weoften
focus on the more attainable goal of estimating the weight w in Eq. 3, or equivalently, the
UCC ratio ρ=C /C , which suffices for computing WA in Eq. 3. We propose therefore
FN FP
a procedure to estimate the weight range w ≤ w ≤ w . Here, we assume that the
min max
developmentandtargetdatasetshavethesameratioofpositiveexamples;thegeneralization
to r ̸=rt is described in Eq. 18.
+ +
A.1 Unit Misclassification Costs Ratio
The first approach to estimating the weight range is via the UCC ratio ρ – i.e., estimating
howmanyfalsepositivesare,onaverage,equivalenttoasinglefalsenegative–andusingthe
equivalence w=ρ/(ρ+1). For instance, in bankruptcy prediction, a false negative – where
anauditorincorrectlyassessesacompanyassolvent–mayresultinliabilitytocreditorsand
shareholders. Conversely, a false positive – where a solvent company is incorrectly assessed
as insolvent – may lead to reduced access to credit and increased uncertainty. Based on
these considerations, [1] and [10] estimated ρ ≃ 35 (i.e., w ≃ 0.97) and 10 ≲ ρ ≲ 50 (i.e.,
0.91≲w≲0.98), respectively.
A.2 Constraints from Ranking of Emblematic Models
Ifthepreviousapproachisnotfeasible,analternativemethodistoinferconstraintsonwby
ranking a set of emblematic classification results. Even if we cannot estimate the costs C
FP
and C (or their ratio), we may still be able to determine whether one specific outcome is
FN
more costly than another.
A.2.1 Construction of the Emblematic Model Set
The choice of emblematic models may depend on the use case and the ratio of positive
examples. Ideally, we should select a small set of models, sufficiently simple to avoid over-
complexityintherankingoftheoutcomes,yetdiverseenoughtoyieldmeaningfulconstraints
on w. As a baseline, we consider the models described in Table 4: (i) M and M , which
+ −
19

alwayspredictthesameclass;(ii)M ,whichmisclassifiesafractionαofexamplesinboth
bad
classes; (iii) M and M , which misclassify a fraction α of negatives or positives,
|               |       | bad−      |     | bad+        |     |              |     |     |     |     |
| ------------- | ----- | --------- | --- | ----------- | --- | ------------ | --- | --- | --- | --- |
| respectively, | while | perfectly |     | classifying | the | other class. |     |     |     |     |
Table 4: Set of emblematic models to determine constraints on w. A is the
num
| numerator | in  | Eq. 3.                            |     |             |     |     |     |     |        |     |
| --------- | --- | --------------------------------- | --- | ----------- | --- | --- | --- | --- | ------ | --- |
| Name      |     |                                   |     | Description |     |     |     |     | Anum   |     |
| M+        |     | Dummymodelalwayspredictingclass+. |     |             |     |     |     |     | wP     |     |
| M−        |     | Dummymodelalwayspredictingclass−. |     |             |     |     |     |     | (1−w)N |     |
M Misclassifiesafractionαofexamplesinbothclasses. (1−α)[wP+(1−w)N]
bad
M Misclassifiesafractionαofnegatives,perfectonpositives. wP+(1−α)(1−w)N
bad−
M Misclassifiesafractionαofpositives,perfectonnegatives. (1−α)wP+(1−w)N
bad+
The parameter α, representing the fraction of misclassified examples, can be chosen ad
hoc to facilitate model ranking. To derive meaningful constraints on w, we recommend
0.5≲α≲0.75.
| choosing | α in the | range |            |     |        |     |     |     |     |     |
| -------- | -------- | ----- | ---------- | --- | ------ | --- | --- | --- | --- | --- |
| A.2.2    | Ranking  | of    | Emblematic |     | Models |     |     |     |     |     |
To rank the models previously identified, we must understand the use case from a business
perspective. For example, is it preferable to correctly identify all positives (as in M )
bad−
or all negatives (as in M )? For illustrative purposes, let us assume a ratio r = 0.05
|     |     |     | bad+ |     |     |     |     |     |     | +   |
| --- | --- | --- | ---- | --- | --- | --- | --- | --- | --- | --- |
of positive examples, and let us use the models from Table 4 with α = 0.6. Suppose it is
impracticaltoreacttoalargenumberofpredictedpositives(e.g.,contactingmanycustomers
in churn prediction, treating many patients in cancer detection, etc.). In this scenario, the
| worst outcome |     | is likely | M , | and we | expect | A(M )≲A(M |     | ).   |     |     |
| ------------- | --- | --------- | --- | ------ | ------ | --------- | --- | ---- | --- | --- |
|               |     |           | +   |        |        | bad−      |     | bad+ |     |     |
Moreover,M ,whichpredictsonlynegatives,maybeslightlypreferabletoM ,since
|     |     | −   |     |     |     |     |     |     | bad |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
itsoutputcouldstillbeusefulifafuturepositivepredictionoccurs. Tocompletetheranking,
we assume M bad− is preferable to M − , as the former misclassifies a fraction α of negatives
andnopositiveexample,andthereforeproducesamoreinformativeoutputcomparedtothe
| latter, which | misclassifies |           | all             | positives. |          |                  |       |      |     |      |
| ------------- | ------------- | --------- | --------------- | ---------- | -------- | ---------------- | ----- | ---- | --- | ---- |
| In summary,   |               | we obtain | the             | following  | ranking: |                  |       |      |     |      |
|               |               | A(M       | )≲A(M           |            | )≲A(M    | )≲A(M            | )≲A(M |      | ).  | (21) |
|               |               |           | +               | bad        |          | −                | bad−  | bad+ |     |      |
| A.2.3         | Inferring     |           | the Constraints |            |          | from the Ranking |       |      |     |      |
Since P and N are fixed for a given dataset, ranking the models by WA is equivalent to
ranking them by the numerator A in Table 4. For α≥0.5, the resulting constraints on
num
w are:
|     |     |     | (cid:20) |     | (cid:21)−1 | (cid:20) | (cid:21)−1 |     |     |      |
| --- | --- | --- | -------- | --- | ---------- | -------- | ---------- | --- | --- | ---- |
|     |     |     |          | P   | ≲w≲        | αP       |            |     |     |      |
|     |     |     | 1+       |     |            | 1+       |            | .   |     | (22) |
|     |     |     |          | αN  |            | (1−α)N   |            |     |     |      |
|     |     |     |          |     |            | ≲        | ≲          |     |     |      |
For α = 0.6 and r + = 0.05, Eq. 22 becomes 0.919 w 0.927, where the upper bound
follows from the condition A(M ) ≲ A(M ), and the lower bound from A(M ) ≲
|     |     |     |     | +   |     | bad |     |     |     | bad− |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---- |
A(M ).
bad+
| Appendix |       | B          | Use | Cases |     | Details |     |     |     |     |
| -------- | ----- | ---------- | --- | ----- | --- | ------- | --- | --- | --- | --- |
| B.1      | Churn | Prediction |     |       |     |         |     |     |     |     |
Each customer a predicted as positive causes a cost M for the retention measure, which
includesthetimeandeffortofthecommercialteamtocontactthecustomerandimplement
20

the measure. Here we assume that this retention cost is example-independent, so eFP =
a
dTP =M. SincetheexperimentdescribedinSection4.1requiresspanningallpossibleUCC
a
| ratios | r , we | tune the | cost | of the retention |     | measure M | accordingly. |     |
| ------ | ------ | -------- | ---- | ---------------- | --- | --------- | ------------ | --- |
C
Conversely,foracustomerapredictedasnegative,thecost(ormissingincome)isR P ,
a eff
where P eff is the probability of effectiveness of the retention measure (assumed example-
independentandfixedto25%),whileR istherevenuethecompanywouldhaveearnedfrom
a
a had the customer not churned, and is assumed proportional to the customer’s revenue.
Toavoidnegativevaluesonthefalsenegativecosts,weclipeachDFN topositivevalues,
a
i.e., we set DFN = max(0,R P − M). To obtain the desired value for r , we must
|     |     | a   |     | a eff |     |     |     | C   |
| --- | --- | --- | --- | ----- | --- | --- | --- | --- |
(cid:80)
solve the equation M = γ max(M,P eff R a ), with γ = (1−r C )/N tot , whose solution is
|      | (cid:80)Ntot |     |                                 | a   |     |     |       |              |
| ---- | ------------ | --- | ------------------------------- | --- | --- | --- | ----- | ------------ |
| M =γ |              | P R | /(1−γA),subjecttotheconstraintP |     |     |     | R ≤M  | ≤P R . Under |
|      | a=A+1        | eff | a                               |     |     |     | eff A | eff A+1      |
=RclipP Rclip
these assumptions, the average UCCs are C FP =M and C FN avg eff −M, where avg
Rclip
denotes the expected value of = max(R a ,M/P eff ) over the target dataset, while the
a
| fluctuations |        | are δ =P | (Rclip−Rclip) |     | and | ϵ =0. |     |     |
| ------------ | ------ | -------- | ------------- | --- | --- | ----- | --- | --- |
|              |        | a        | eff           | a   | avg | a     |     |     |
| B.2          | Credit | Scoring  |               |     |     |       |     |     |
For credit scoring, we use the approach described in [3]. In that framework, the costs of
|     |     |     | dTP | eTN, |     |     |     |     |
| --- | --- | --- | --- | ---- | --- | --- | --- | --- |
correct classifications, and are assumed to be zero for every customer a. The loss
|     |     |     | a   | a   |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
DFN = dFN if the customer a defaults is proportional to their credit line, while the cost
a a
EFP = eFP of a false positive is the sum of two financial components, R and G . The
| a   | a   |     |     |     |     |     |     | a avg |
| --- | --- | --- | --- | --- | --- | --- | --- | ----- |
first term is the loss of profit from rejecting a customer who would have repaid the loan;
it depends on the loan parameters (see [3] for details). Differently from [3], we introduce
clipping of the customer debt ratio to the interval [0,1], ensuring data consistency.
The term G reflects the assumption that the financial institution does not keep the
avg
capitalofarejectedcustomeridle,butinsteadallocatesittoanalternativecustomer. Since
no additional information about this alternative customer is available, we assume that the
customerdefaultswithprobabilityequaltothepriorpositiverater . Underthisassumption,
+
G avg =−R avg ·(1−r + )+Cl·L gd ·r + ,whereClistheaveragecreditline,R avg theaverage
profit, and L the loss-given-default ratio, i.e., the fraction of the customer’s debt that is
gd
| lost in | case | of default. |     |     |     |     |     |     |
| ------- | ---- | ----------- | --- | --- | --- | --- | --- | --- |
The parameter used to tune the UCC ratio r is L . To ensure that L remains non-
|     |     |     |     |     |     | C   | gd  | gd  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
negative, the analysis must be restricted to the domain r <1/(1+r ), hence the missing
|        |        |           |        |         |         |            | C +      |     |
| ------ | ------ | --------- | ------ | ------- | ------- | ---------- | -------- | --- |
| values | in the | top right | corner | of each | heatmap | in Figures | 2 and 4. |     |
References
[1] Edward I. Altman, Robert G. Haldeman, and P. Narayanan. ZETATM analysis A
new model to identify bankruptcy risk of corporations. Jour. of Banking & Finance,
|     | 1(1):29–54, | 1977. |     |     |     |     |     |     |
| --- | ----------- | ----- | --- | --- | --- | --- | --- | --- |
[2] Yuri Sousa Aurelio, Gustavo Matheus de Almeida, Cristiano Leite de Castro, et al.
Cost-sensitivelearningbasedonperformancemetricforimbalanceddata. Neural Proc.
|     | Lett., 54(4):3097–3114, |     |     | 2022. |     |     |     |     |
| --- | ----------------------- | --- | --- | ----- | --- | --- | --- | --- |
[3] AlejandroCorreaBahnsen,DjamiaAouada,andBjo¨rnOttersten. Example-dependent
cost-sensitivelogisticregressionforcreditscoring.In201413thInternationalconference
|     | on machine | learning | and | applications, |     | pages 263–269. | IEEE, 2014. |     |
| --- | ---------- | -------- | --- | ------------- | --- | -------------- | ----------- | --- |
[4] Alvaro A Ca´rdenas and John S Baras. B-ROC curves for the assessment of classifiers
overimbalanceddatasets. InProc. of the national Conf. on Art. Int.,volume21,page
|     | 1581, 2006. |     |     |     |     |     |     |     |
| --- | ----------- | --- | --- | --- | --- | --- | --- | --- |
[5] Nitesh V Chawla. Data mining for imbalanced datasets: An overview, pages 853–867.
|     | Springer | US, Boston, | MA, | 2005. |     |     |     |     |
| --- | -------- | ----------- | --- | ----- | --- | --- | --- | --- |
21

[6] NiteshVChawla,KevinWBowyer,LawrenceOHall,andWPhilipKegelmeyer.Smote:
synthetic minority over-sampling technique. Journal of artificial intelligence research,
| 16:321–357, | 2002. |     |     |     |     |     |     |     |
| ----------- | ----- | --- | --- | --- | --- | --- | --- | --- |
[7] Pedro Domingos. MetaCost: A general method for making classifiers cost-sensitive.
In Proc. of the 5th ACM SIGKDD Int. Conf. on Know. Disc. and Data Min., pages
155–164, 1999.
[8] ChrisDrummondandRobertCHolte. C4.5,classimbalance,andcostsensitivity: why
under-sampling beats over-sampling. In Int. Conf. on Mach. Learn., volume 11, 2003.
[9] Charles Elkan. The foundations of cost-sensitive learning. In Int. joint Conf. on Art.
| Int., volume | 17, | pages | 973–978, | 2001. |     |     |     |     |
| ------------ | --- | ----- | -------- | ----- | --- | --- | --- | --- |
[10] Harlan L Etheridge, Ram S Sriram, and HY Kathy Hsu. A comparison of selected
artificialneuralnetworksthathelpauditorsevaluateclientfinancialviability. Decision
| Sciences, | 31(2):531–550, |     | 2000. |     |     |     |     |     |
| --------- | -------------- | --- | ----- | --- | --- | --- | --- | --- |
[11] L´eo Gautheron, Amaury Habrard, Emilie Morvant, et al. Metric learning from im-
balanced data. In 2019 IEEE 31st Int. Conf. on Tools with Art. Int. (ICTAI), pages
| 923–930. | IEEE, | 2019. |     |     |     |     |     |     |
| -------- | ----- | ----- | --- | --- | --- | --- | --- | --- |
[12] NysiaIGeorge,Tzu-PinLu,andChing-WeiChang. Cost-sensitiveperformancemetric
| for comparing | multiple |     | ordinal | classifiers. | Art. | Int. Res., | 5(1):135–143, | 2016. |
| ------------- | -------- | --- | ------- | ------------ | ---- | ---------- | ------------- | ----- |
[13] Bishwadip Ghosh and Joseph Hasley. Using asymmetric classification cost matrices in
| predicting | diabetes. | In  | ICDSS | 2007 Proceedings, |     | 2007. |     |     |
| ---------- | --------- | --- | ----- | ----------------- | --- | ----- | --- | --- |
[14] David J Hand. Measuring classifier performance: a coherent alternative to the area
| under the | ROC | curve. | Mach. | Learn., | 77(1):103–123, | 2009. |     |     |
| --------- | --- | ------ | ----- | ------- | -------------- | ----- | --- | --- |
[15] Mohammad Hossin and Md Nasir Sulaiman. A review on evaluation metrics for data
classification evaluations. Int. Jour. of Data Min. & Know. Manag. process, 5(2):1,
2015.
[16] Jungeun Kim, Keunho Choi, Gunwoo Kim, et al. Classification cost: An empirical
comparison among traditional classifier, cost-sensitive classifier, and MetaCost. Exp.
| Syst. with | Appl., | 39(4):4013–4019, |     | 2012. |     |     |     |     |
| ---------- | ------ | ---------------- | --- | ----- | --- | --- | --- | --- |
[17] Matjaz Kukar and Igor Kononenko. Cost-sensitive learning with neural networks. In
| Proc. of | the 13th | European | Conf. | on  | Art. Int. | (ECAI | 98), pages 445–449, | 1998. |
| -------- | -------- | -------- | ----- | --- | --------- | ----- | ------------------- | ----- |
[18] NadaLavraˇc,PeterFlach,andBlazZupan. Ruleevaluationmeasures: Aunifyingview.
| In Int. Conf. | on  | inductive | logic | programming, |     | pages 174–185. | Springer, | 1999. |
| ------------- | --- | --------- | ----- | ------------ | --- | -------------- | --------- | ----- |
[19] Guillaume Lemaˆıtre, Fernando Nogueira, and Christos K Aridas. Imbalanced-learn:
A python toolbox to tackle the curse of imbalanced datasets in mach. learn. Jour. of
| Mach. Learn. | Res., | 18(17):1–5, |     | 2017. |     |     |     |     |
| ------------ | ----- | ----------- | --- | ----- | --- | --- | --- | --- |
[20] Charles X Ling, Victor S Sheng, and Qiang Yang. Test strategies for cost-sensitive
| decision | trees. IEEE | Trans. | on  | Know. | and Data | Eng., | 18(8):1055–1067, | 2006. |
| -------- | ----------- | ------ | --- | ----- | -------- | ----- | ---------------- | ----- |
[21] Xu-Ying Liu and Zhi-Hua Zhou. The influence of class imbalance on cost-sensitive
learning: An empirical study. In 6ht Int. Conf. on Data Min. (ICDM’06), pages 970–
| 974. IEEE, | 2006. |     |     |     |     |     |     |     |
| ---------- | ----- | --- | --- | --- | --- | --- | --- | --- |
[22] Yangguang Liu, Yangming Zhou, Shiting Wen, et al. A strategy on selecting perfor-
mance metrics for classifier evaluation. Int. Jour. of Mobile Comp. and Multimedia
| Communications |     | (IJMCMC), |     | 6(4):20–35, | 2014. |     |     |     |
| -------------- | --- | --------- | --- | ----------- | ----- | --- | --- | --- |
[23] Lucas Loezer, Fabr´ıcio Enembreck, Jean Paul Barddal, et al. Cost-sensitive learning
for imbalanced data streams. In Proc. of the 35th annual ACM symposium on applied
| Comp., | pages 498–504, |     | 2020. |     |     |     |     |     |
| ------ | -------------- | --- | ----- | --- | --- | --- | --- | --- |
[24] Pierangelo Lombardo. Standardization of weighted ranking correlation coefficients.
| CoRR abs/2504.08428, |     |     | 2025. |     |     |     |     |     |
| -------------------- | --- | --- | ----- | --- | --- | --- | --- | --- |
22

[25] PierangeloLombardo,AlessioBoiardi,LucaColombo,etal. Top-rank-focusedadaptive
vote collection for the evaluation of domain-specific semantic models. In Proc. of the
2020 Conf. on Empirical Methods in Natural Language Proc. (EMNLP), pages 3081–
3093, 2020.
[26] HuijuanLu,YigeXu,MinchaoYe,etal. Learningmisclassificationcostsforimbalanced
| classification | on  | gene expression |     | data. | BMC bioinformatics, |     | 20:1–10, | 2019. |
| -------------- | --- | --------------- | --- | ----- | ------------------- | --- | -------- | ----- |
[27] Manish Marwah, Asad Narayanan, Stephen Jou, et al. Is F1 score suboptimal for cy-
bersecuritymodels? introducingCscore,acost-awarealternativeformodelassessment.
InConf. on Applied Mach. Learn. for Inf. Security,volume3920,pages190–209,2024.
[28] Ross A McDonald. The mean subjective utility score, a novel metric for cost-sensitive
| classifier | evaluation. | Pattern | Recognition |     | Lett., | 27(13):1472–1477, |     | 2006. |
| ---------- | ----------- | ------- | ----------- | --- | ------ | ----------------- | --- | ----- |
[29] IbomoiyeDomorMienyeandYanxiaSun.Performanceanalysisofcost-sensitivelearning
methods with application to imbalanced medical data. Artif Intell Rev, 57(80), 2024.
[30] Ebrahim Mortaz. Imbalance accuracy metric for model selection in multi-class imbal-
| ance classification |     | problems. | Know.-Based |     | Syst., | 210:106490, | 2020. |     |
| ------------------- | --- | --------- | ----------- | --- | ------ | ----------- | ----- | --- |
[31] MihaelaMunteanandFlorin-DanielMilitaru. Metricsforevaluatingclassificationalgo-
rithms. InEducation, Res. and Business Tech.: Proc. of 21st Int. Conf. on Informatics
| in Economy | (IE | 2022), | pages 307–317. |     | Springer, | 2023. |     |     |
| ---------- | --- | ------ | -------------- | --- | --------- | ----- | --- | --- |
[32] Deirdre B O’Brien, Maya R Gupta, and Robert M Gray. Cost-sensitive multi-class
classification from probability estimates. In Proc. of the 25th Int. Conf. on Mach.
| Learn. (ICML), |     | pages 712–719, |     | 2008. |     |     |     |     |
| -------------- | --- | -------------- | --- | ----- | --- | --- | --- | --- |
[33] Stjepan Picek, Annelie Heuser, Alan Jovic, et al. The curse of class imbalance and
conflictingmetricswithmachinelearningforside-channelevaluations. IACRTrans.on
| Cryptographic | Hardware |     | and Embedded |     | Syst., | 2019(1):209–237, |     | 2018. |
| ------------- | -------- | --- | ------------ | --- | ------ | ---------------- | --- | ----- |
[34] DavidPowers.Evaluation: Fromprecision,recallandF-measuretoROC,informedness,
| markedness | & correlation. |     | Jour. | of Mach. | Learn. | Tech., | 2(1):37–63, | 2011. |
| ---------- | -------------- | --- | ----- | -------- | ------ | ------ | ----------- | ----- |
[35] Badiuzzaman Pranto, Sk Maliha Mehnaz, Sifat Momen, et al. Prediction of diabetes
using cost sensitive learning and oversampling techniques on bangladeshi and indian
female patients. In 2020 5th Int. Conf. on Inf. Tech. Res. (ICITR), pages 1–6. IEEE,
2020.
[36] OonaRainio,JarmoTeuho,andRikuKl´en. Evaluationmetricsandstatisticaltestsfor
| machine | learning. | Scientific | Reports, | 14(1):6086, |     | 2024. |     |     |
| ------- | --------- | ---------- | -------- | ----------- | --- | ----- | --- | --- |
[37] D Ramyachitra and Parasuraman Manikandan. Imbalanced dataset classification and
solutions: a review. Int. Jour. of Comp. and Business Res. (IJCBR), 5(4):1–29, 2014.
[38] Mikolaj Sitarz. Extending F1 metric, probabilistic approach. CoRR abs/2210.11997,
2022.
[39] CharlesSpearman. Theproofandmeasurementofassociationbetweentwothings. The
| American | Jour. | of Psychology, | 15(1):72–101, |     |     | 1904. |     |     |
| -------- | ----- | -------------- | ------------- | --- | --- | ----- | --- | --- |
[40] Seba Susan and Amitesh Kumar. The balancing trick: Optimized sampling of imbal-
anceddatasets—abriefsurveyoftherecentstateoftheart. Eng.Reports,3(4):e12298,
2021.
[41] Akbar Telikani, Amir H Gandomi, Kim-Kwang Raymond Choo, et al. A cost-sensitive
deeplearning-basedapproachfornetworktrafficclassification.IEEETrans.onNetwork
| and Service | Manag., | 19(1):661–670, |     | 2022. |     |     |     |     |
| ----------- | ------- | -------------- | --- | ----- | --- | --- | --- | --- |
[42] Thomas Verbraken, Wouter Verbeke, and Bart Baesens. A novel profit maximizing
metric for measuring classification performance of customer churn prediction models.
| IEEE Trans. | on  | Know. | and Data | Eng., | 25(5):961–973, | 2013. |     |     |
| ----------- | --- | ----- | -------- | ----- | -------------- | ----- | --- | --- |
23

[43] Haomin Wang, Gang Kou, and Yi Peng. Multi-class misclassification cost matrix for
creditratingsinpeer-to-peerlending. Jour. of the Operational Res. Society,72(4):923–
934, 2021.
[44] Yuri Zelenkov. Example-dependent cost-sensitive adaptive boosting. Exp. Syst. Appl.,
135:71–82, 2019.
24