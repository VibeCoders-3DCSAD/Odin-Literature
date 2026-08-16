---
conversion_metadata:
  converted_at: "2026-07-21T14:12:11Z"
  converter_tool: "markitdown"
  converter_version: "0.1.6"
  source_pdf: "Martin J. et al.pdf"
  source_pdf_sha256: "9dc1183d421b561686c5dd4b940a1c514f77177443e379cb5dcfa4b2d1136427"
  page_count: 26
  markdown_char_count: 147052
---

<!-- PAGE-AWARE EXTRACTION (via pdfminer.six) -->

<!-- PAGE 1 -->

Annals of Operations Research
https://doi.org/10.1007/s10479-025-06514-x

O R I G I N A L R E S E A R C H

A novel ﬁnancial performance metric to minimize
misclassiﬁcation costs in model selection

John Martin1 · Mali Abdollahian1 · Sona Taheri1

· David Akman1

Received: 3 January 2023 / Accepted: 28 January 2025
© The Author(s) 2025

Abstract
A novel ﬁnancial performance metric (FPM) is introduced seeking to minimise the misclas-
siﬁcation cost arising from false positives and false negatives in credit risk assessment. Using
the German Credit Dataset (GCD), important ﬁnancial variables are simulated according to
four different asset classes to enable a more accurate and reliable, multidimensional model
selection. The misclassiﬁcation cost arising from FPM is compared with commonly used sta-
tistical metrics and the credit scoring example dependent cost matrix (CSEDCM) metric. The
results show that CSEDCM underestimates false prediction costs by as much as 99% com-
pared to the FPM. A range of high- performance machine learning methods was compared
using FPM and statistical metrics. The Multi-Layer Perceptron outperformed other methods
on statistical metrics and overall on ﬁnancial costs, while a mix of algorithms worked best
on either side of the decision threshold. The results conﬁrmed that the proposed FPM would
provide a signiﬁcant ﬁnancial beneﬁt to organisations.

Keywords Credit scorecard · Financial performance metric · Machine learning · German
credit

1 Introduction

A credit default is a negative event for both borrowers and lenders, but can also impact the
broader economy. Because credit is a key driver of the economy, essential for the stability
and growth of the global ﬁnancial system, no economy, irrespective of how advanced it may
be, can develop in its absence (Banu, 2013). As the global ﬁnancial crisis and more recent
events such as the COVID-19 pandemic have demonstrated, credit losses related to loans can
have a signiﬁcant detrimental impact on the broader economy (Cantrell et al., 2014).

B Sona Taheri

sona.taheri@rmit.edu.au

John Martin
S3801949@student.rmit.edu.au

Mali Abdollahian
mali.abdollahian@rmit.edu.au

David Akman
david.akman@rmit.edu.au

1

School of Science, RMIT University, Melbourne, VIC, Australia

123

---

<!-- PAGE 2 -->

Annals of Operations Research

To protect against losses, lenders seek to maintain robust lending practices through opti-
mising credit risk assessment. Indeed, the centrality of credit to the monetary economy
throughout the economic cycle underscores the importance of accurate credit assessment.
Historically, creditworthiness was evaluated using human judgement. However, the scale of
lending has increased over time such that contemporaneously, most lenders deploy classiﬁ-
cation models to perform this task at scale.

Scorecard models are one of the main applications of classiﬁcation models in credit risk.
Used to assess creditworthiness, scorecard models associate historical characteristics like
prior loan performance with default to estimate the probability of default. Once this has has
been derived it is then compared to cut-off thresholds to determine the outcome: approval or
rejection.

A great deal of prior research has been published detailing the comparative performance
of various statistical and machine learning algorithms. Martin et al. (2024) compared a
wide range of individual and ensemble algorithms for credit scoring. They showed that the
best individual performer was a Generalised Additive Model and the best overall performer
was a Random Forest and K-Nearest Neighbour ensemble. Similarly, hybrid models have
performed well on public datasets such as German credit. Tripathi et al. (2020) used an
Extreme machine learning approach. Mahbobi et al. (2023) found that the Support Vector
Machine algorithm performed best under a K-Nearest Neighbour sampling approach.

We consider methods which have recently been shown to outperform other approaches in
credit risk modelling research including Random Forest (RF), Gradient Boosting Machine
(GBM), Artiﬁcial Neural Networks, speciﬁcally the Multi-Layer Perceptron (MLP), Decision
Trees (DTR) and Support Vector Machine (SVM). We compare the performance of these ﬁve
algorithms with that of the gold standard used in industry, Logistic Regression (LR), using
the statistical and cost performance criteria discussed in the next sections.

Main contributions of this paper are:

1. Introducing a new Financial Performance Metric (FPM) to estimate the true costs arising

from both false positives and false negatives;

2. Providing insights on cost dynamics as a consideration in the model selection, and opti-

mising the selection by combining statistical methods with the developed FPM;

3. Evaluating the suitability of a publicly available German Credit Dataset (GCD) for credit
risk modelling, and simulating important ﬁnancial variables which are often not available
in public datasets;

4. Comparing the proposed FPM with an existing metric, credit scoring example dependent

cost matrix (CSEDCM) metric, as well as commonly used statistical criteria;

5. Comparing cost dynamics across four simulated asset classes observed at large banks to
understand the impact of default and opportunity cost across different loan values;
6. Comparing the performance of Logistic Regression with a selection of high-performance
machine learning algorithms utilizing the commonly used statistical criteria and the
proposed FPM, and determining which algorithm outperforms in estimating costs arising
from both false positives and false negatives.

The rest of the paper is organised as follows. First, we provide a brief introduction on
the research work in Sect. 1. In Sect. 2, we present an overview of commonly used statistical
measures of performance. Section 3 presents an overview on cost performance measures and
introduces a new approach. In Sect. 4, the machine learning methods used are provided. The
dataset and numerical results are described in Sect. 5. The discussion, conclusion and some
future direction are provided in Sect. 6.

123

---

<!-- PAGE 3 -->

Annals of Operations Research

2 Statistical performance

Traditionally the focus in credit risk modelling research has been to optimise the identiﬁcation
of true positives, that is, optimizing alignment between the prediction and observation of
default, with scant regard for ‘non-defaults’. Researchers and industry practitioners alike
have mainly relied on the use of statistical metrics to measure model performance and select
the strongest model.

Conceptually, the underlying logic to this practice is that by selecting the model with the
strongest metrics modellers can identify the model which is most ﬁt for purpose. In industry
and academia alike, classical statistical performance criteria including the Area under the
Receiver Operating Curve (AUC), Accuracy (ACC) and Somers’ Delta (Gini) are amongst
the most widely used model metrics reported and used for model selection.

However, prior research has identiﬁed some problematic features of AUC, ACC and Gini,
which suggest their use can lead to incorrect conclusions (see, for example, Verbraken et al.,
2014). The Gini statistic has a linear relationship with AUC, yet both are commonly reported
despite the obvious redundancy of reporting directly related performance metrics. Gini is
deﬁned as

Gini = 1 −

n+m(cid:2)

(cid:3)(cid:4)

Fm.B ADk

(cid:5)

− Fm.B ADk−1
(cid:5)(cid:6)
,

− Fn.G O O Dk−1

k=2
(cid:4)

Fn.G O O Dk

×

(Fn.G O O Dk

) is the kth vector value of the empirical distribution function
where Fm.B ADk
of bad (good) applicants, while m and n are the number of elements of the bad and good
distributions, respectively. Further details can be found, for example in Thomas et al. (2002).
Hand (2009) states that Gini may not be suitable as a measure of performance of application
scorecards since it (as well as some other commonly used metrics including the Kolmogorov–
Smirnov (KS) statistic and Information Value (IV)) uses irrelevant information. It fails to
measure information on the bad rate among accepts which is the aspect of performance we
are actually interested in.

The Receiver Operating Curve (ROC) is a graphical tool used to visualise the trade-
off between sensitivity and speciﬁcity, while the AUC is a scalar measure of aggregate
performance which summarises the ROC into a single value. In Anagnostopoulos et al.
(2019), the AUC is criticised for how it handles the trade-off between false positives and false
negatives whereby the relative severities of misclassiﬁcations are treated differently between
different classiﬁers. Moreover, Marzban (2004) showed that AUC discriminates well between
‘good’ and ‘bad’ models, but not between good models. Hand and Anagnostopoulos (2013)
dismiss AUC as a portmanteau measure, equivalent to integrating over a range of possible
values, concluding that the ROC is an incoherent performance measure. The AUC is deﬁned
as

AU C = 1
2

× (Sensitivit y + Speci f icit y),

where sensitivity is the True Positive Rate (TPR) and speciﬁcity is the True Negative Rate
(TNR), with Sensitivity (TPR) = True Positives/Total Positives ×100, whereas Speciﬁcity
(TNR) = True Negatives/Total Negatives ×100.

As stated above, there is a linear relationship between AUC and Gini, and each can be
easily calculated from the other using the following equation, suggesting redundancy in the

123

---

<!-- PAGE 4 -->

Annals of Operations Research

common practice of presenting both measures for model evaluation and/or selection:

AU C = Gini + 1

2

.

On the other hand, ACC works by effectively summing accurate classiﬁcations as a proportion
of all classiﬁcations, which is problematic in scenarios characterised by severely imbalanced
target variables typical in credit modelling research. For example, for an observed default
rate of 0.05 a model may predict all observations as non-defaults, yet still receive an ACC
of 0.95. While a common solution is to perform sampling to increase the minority class
representation. This rarely fully deals with the class imbalance bias in real-situations and
creates further complications downstream in terms of model monitoring. The ACC is deﬁned
as

ACC =

T P + T N
T P + T N + F P + F N

,

where TP is equal to True Positive, TN equals True Negative, FP equals False Positive and
FN equals False Negative.

3 Cost performance

As discussed in the previous section, the most commonly used statistical metrics have some
serious drawbacks which raises questions around their value in model selection, particularly
in relation to commercial applications such as credit risk. Moreover, focusing only on this
aspect of performance ignores some very important practical considerations. In classiﬁcation
research the correct selection of performance metrics is one of the most important issues in
evaluating a classiﬁer’s performance (Liu et al., 2014). Indeed, a vast array of alternative
metrics are available and optimizing the wrong metric directly translates into lost revenue
(Dmitriev & Wu, 2016).

The most important objective in banking is proﬁt, and therefore once a model has been
determined as functional the comparative costs must be considered. Selecting the optimal
approach is not possible using standard classiﬁcation metrics because they treat the costs
of misclassiﬁcations the same, which is not true in real credit risk management (see, for
example, Fiore et al., 2017). Credit risk is particularly well aligned to the use of proﬁt-
based or ﬁnancial loss-related measures (Maldonado et al., 2017), which seek to optimise a
commercial outcome as opposed to a statistical metric.

Cost sensitive learning seeks to optimise decision-making where misclassiﬁcation costs
incur different penalties. While a valid application of cost sensitive learning can assume
the same misclassiﬁcation cost, Elkan (2001) suggested that a more realistic problem exists
where misclassiﬁcation costs are example-dependent, in the sense that the costs vary among
examples and not only among classes. This is particularly so for credit risk, where misclas-
siﬁcation costs vary both within and between response classes.

Indeed, researchers have long been aware of the proﬁt motive as a central driving factor
in model selection in credit risk yet only a handful have sought to ﬁnd ways to incorporate
this perspective into model selection. One of the biggest obstacles has been the dearth of
available datasets containing the necessary ﬁnancial information to compare performance on
cost (Aodha & Brostow, 2013), leading to a variety of approaches to overcome this shortfall.
For example, Xia et al. (2017) simply assumed that the costs of misclassifying a defaulting
borrower are larger than that of misclassifying a good one. Schebesch and Stecking (2005)

123

---

<!-- PAGE 5 -->

Annals of Operations Research

Table 1 CSEDCM model, given in Eq. (1)

Predicted positive
ci = 1
Predicted negative
ci = 0

Actual positive yi = 1

Actual negative yi = 0

CT Pi

= 0

C F Pi

= ri + C a

F P

C F N i

= Cli · LG D

CT Pi

= 0

simpliﬁed this problem by assuming that the misclassiﬁcation costs of a bad borrower as a
good borrower as ﬁve times more costly than misclassiﬁcation of a good borrower as a bad
borrower, yet without data neither paper was able to empirically evaluate this assumption.

Other researchers with access to data containing ﬁnancial performance variables have
constructed cost metrics using a variety of different approaches. For instance, Zhang et al.
(2018) applied the Multiple Instance Learning method, proposing a cost sensitive optimiza-
tion approach which sought to minimise misclassiﬁcation costs. In this work, instead of
quantifying differences in misclassiﬁcation costs, the authors weighted misclassiﬁcations by
similarity according to demographic features and transactional behaviour.

3.1 Existing cost metrics

Wang et al. (2021) proposed an approach to estimate costs associated with risk based pricing,
whereby similar groups of exposures were assigned increasing levels of interest relative to
their risk in peer-to-peer lending. They assigned a cost matrix to pooled risks for differential
pricing, which sought to assign differential misclassiﬁcation cost matrices, with the lower
triangular C1 assigned the economic costs with a predicted ‘good defaulting’, and C2 the
additive cost of misclassifying an applicant to the wrong pool and the opportunity cost of
lost business. Nevertheless, the uncertainty arising from new business in opportunity costs
was not considered in this work.

By contrast, Bahnsen et al. (2015) and Verbraken et al. (2014) both sought to assign a cost
matrix with differential costs according to each outcome. Bahsen et al. (2015) focused on
(cid:7)
(xi , yi ) ∈
misclassiﬁcation only, where true predictions were assumed to cost nothing. Let
Rn × R, i = 1, . . . , N
be a set of predictor (explanatory) variables x and response (indicator)
variable y. The Bahnsen et al. (2014, 2015) credit scoring example dependent cost matrix
(CSEDCM) metric is given below:

(cid:8)

(cid:4)

(cid:5)
)

f (x ∗
i

Cost

(cid:9)
ci CT P + (1 − ci )C F N

(cid:10)

= yi

(cid:9)
+ (1 − yi )

ci C F P + (1 − ci )CT N

(cid:10)
,

(1)

where ci , i = 1, . . . , N are predicted labels, and values CT P , CT N , C F N , C F P indicate the
costs of true positive, true negative, false negative, and false positive, respectively. Note that
CT P = CT N = 0 as the true prediction do not accrue any misclassication cost. C F N shows
losses if the customer i defaults to be proportional to his credit line, whereas C F P is minus
proﬁt plus the expected loss if the customer does not default.

Table 1 sets out the CSEDCM approach according to the four outcomes for a binary

classiﬁcation model.

123

---

<!-- PAGE 6 -->

Annals of Operations Research

= −¯r · π0 + ¯Cl · LG D · π1.

Here, ri is the loss in proﬁt by rejecting what would have been a good customer, yet this
value must be present valued. The term C a
F P is minus the proﬁt of an average alternative
customer (¯r ) times the probability they will not default (π0), plus the average credit line
( ¯Cl) times Loss Given Default (LGD) times the probability they will default (π1), that is
C a

F P
Taking a slightly different route, Verbraken et al. (2014) sought to estimate costs compared
to a model where all applicants are approved, that is where no credit scoring takes place.
More speciﬁcally, they proposed the Expected Maximum Proﬁt (EMP) model assigning a
beneﬁt in correctly identifying a defaulter, b0, which is the fraction of the loan amount which
is lost after default as

b0 = LG D × E AD

A

,

where EAD is Exposure at Default, and A is Principal Exposure. By contrast, the costs
associated with misclassifying a good applicant as a defaulter are equal to the Return on
Investment (ROI) of the loan, deﬁned as follows:

R O I =

r M
1 − (1 + r )−M

− 1,

where r is the Interest Rate, and M is Maturity.

Further, Verbraken et al. (2014) proposed that LGD follows a uniform distribution, and

the EMP metric is given below:

(cid:11)

E M P =

0

1

P(T (θ ); b0, R O I ) × π0 F0(t) − h(b0)db0,

where t is the deﬁned cutoff threshold value, T is the optimal cutoff value under the given
circumstances, θ is the cost-beneﬁt ratio, π0 F0(t) is a true positive case, h(b0)db0 is the
probability distribution associated with correctly identifying a defaulter, and

P(t; b0, R O I ) = b0 × π0 F0(t) − R O I × π1 F1(t),

with π1 F1(t) indicating a false positive case.

3.2 Proposed financial performance metric

In this section, we introduce a more realistic estimate of the misclassiﬁcation costs arising
from credit risk, the ﬁnancial performance metric (FPM). We formulate the FPM based on
the prior research, in particular the contributions of Bahnsen et al. (2015) and Verbraken et
al. (2014). The FPM seeks to incorporate elements which have hitherto been omitted. We
summarise our approach below and highlight differences with the existing approaches.

Loss estimation in credit risk has matured signiﬁcantly thanks to advances required by
regulatory regimes such as IFRS9, published in 2014 (IASB, 2014). IFRS9 was the interna-
tional accounting standard board’s response to the ﬁnancial crisis, aimed at improving the
accounting and reporting of ﬁnancial assets and liabilities (Gea-Carrasco, 2015). We note
that while lost interest is sometimes recognised in some formulations of realised LGD, we
have separated out this component to make it more explicit.

While we agree that LGD must be incorporated into cost estimates to obtain a true view of
the potential loss, Bahnsen’s CSEDCM metric uses maximum credit line in all estimates of
losses, yet it is clear that EAD must be evaluated since EAD is the actual amount the lender
has at risk. Moreover, the CSEDCM approach ignores the interest lost from a default which

123

---

<!-- PAGE 7 -->

Annals of Operations Research

is an important consideration, noting the proﬁt component as a key motivation for being in
the business of lending.

Furthermore, in estimating the cost of a false positive, there is some debate on how
to incorporate the portfolio level uncertainty for the alternative customer (the cost of the
‘next customer’ who the model deems the credit worthy). We have chosen to incorporate an
amended version of the average expected loss for the portfolio using the expected loss for-
mula, as these costs can reasonably be expected over time and have incorporated a measure of
the uncertainty of future proﬁts. In the results section we describe a comparison between the
proposed approach and the CSEDCM approach to demonstrate the model selection implica-
tions.

Similarly, Verbraken’s model presents some opportunity for reﬁnement to improve the
estimation of expected costs. For example, ROI cannot possibly be as simple as multiplying
the interest rate against the principle for the loan term. The fact that there is a default rate
means that a proportion of the portfolio will never reach its contractually agreed maturity
term. Thus remaining months on book must be considered to accurately assess the true value
lost. While averages are sometimes unavoidable where speciﬁc information isn’t available,
the gross value of interest revenue lost from a mortgage customer who defaults at two months
is vastly different from one who defaults at the 320th month. Moreover, the ﬁnancial proﬁles
of the underlying customers who form these two disparate scenarios will be very different.
Therefore, ignoring the remaining months on book would systematically underpredict costs
for identiﬁable customer groups.

In addition, since credit decisions that result in default and opportunity costs (that is,
positive and negative misclassiﬁcations) occur simultaneously, they should be summed rather
than subtracted. Finally, it is unrealistic to assume a starting position of the no credit risk
model as even prior to the wide-scale adoption of classiﬁcation models expert judgment was
used to score applicants.

Our proposed FPM advances cost-sensitive learning as it applies to credit scorecards by
developing a more realistic evaluation of the ﬁnancial costs arising from each misclassiﬁca-
tion. These differences can be potentially huge when considered at a portfolio level that might
comprise hundreds of thousands of customers. Splitting costs on either side of the decision
boundary also imparts positive beneﬁts. It provides the capability to optimise the threshold by
minimising cost. Any systematic weakness in a chosen model could be identiﬁed and indeed
overcome by potentially adding variables or even ‘beeﬁng up’ the predictive capability by
combining models. Thus, the cost of a false negative, misclassifying a bad customer as good,
is equal to

F N C =

N(cid:2)

i=1

P( ˆyi < t | yi = 1) × LG D × E AD + P V (R O I × R M O B),

where yi is the observed outcome (actual output), ˆyi is the estimated outcome (modeled
output), and P( ˆyi < t | yi = 1) are the false negative cases, the function P V is a present
value which depends on R O I and R M O B, with R M O B being the remaining months on
book, a measure of the number of months remaining on the repayment terms of the loan
agreement.

123

---

<!-- PAGE 8 -->

On the other hand the cost of a false positive, misclassifying a good customer as bad, is

Annals of Operations Research

equal to

F PC =

N(cid:2)

i=1

P( ˆyi > t | yi = 0) × P V (R O I ) − (R O I + ¯y × E AD × LG D),

where P( ˆyi > t | yi = 0) are the false positive cases, R O I is the average interest revenue
for the portfolio, ¯y is the average default rate for the portfolio, y = (y1, . . . , yN ), E AD is
the average EAD and LG D is the average LGD.

Note that our proposed approach allows us to split false estimates above and below the
decision threshold which provides additional insights on model performance. In addition, it
considers both in terms of making judgements on model selection as well as the overall view.
The proposed Financial Performance Metric (FPM) for calculates the misclassiﬁcation cost
by:

F P M = F N C + F PC.

(2)

4 Methods used

We utilise six widely used machine learning algorithms of varying complexity on a publicly
available dataset (GCD) to evaluate which performs best according to our proposed FPM.
The methods compared include: Logistic Regression, Random Forest, Gradient Boosting
Machine, Decision Trees, Support Vector Machine and Artiﬁcial Neural Network Multilayer
Perceptron. Next, we give a brief description of each algorithm and refer to the references
provided for more details.

4.1 Logistic regression

Logistic Regression (LR) is the gold standard in credit risk modelling in industry and is
typically the baseline model in credit scoring model comparison studies (Yhip & Alaghe-
band, 2017). However, it has received criticism for its inability to detect non-linear or
non-monotonic relationships. The LR is an extension of linear regression, using a logit
function to make the distance between two binary points continuous. The logit function is a
transformation between the linear model and the probability of the binary outcome. The LR
is formulated as

ln( p/1 − p) = β0 + β1x1 + ....βn xn,

where p is the probability of the event occurring, β0 is the y-intercept, and βi , i = 1, . . . , n
are the coefﬁcient of the independent variable xi .

4.2 Decision tree

Decision Trees (DTRs) utilise a ﬂowchart or tree-like decision making approach that is easily
visualised from left to right and is composed of “burst” nodes split into different paths. The
three types of nodes include Root nodes, which compile the entire sample and are then divided

123

---

<!-- PAGE 9 -->

Annals of Operations Research

into multiple sets; Decision nodes, which are typically represented by squares, represent sub-
nodes that diverge further into further possibilities; and Terminal nodes, which represent the
outcome that cannot be categorized further. The tree structure is built from the top down by
selecting the best decision node to split ﬁrst, and then after, based on Measures of entropy
and information gain are used to select the best decision to node ﬁrst and then subsequent
decisions. Weights are calculated for each chance node by estimating the conditional (joint)
probabilities. DTRs and variants thereof have been shown to be highly effective for credit
risk modelling (Dumitrescu et al., 2022; Tian et al., 2020). DTRs are formulated as

(X , y) = (x1, x2, x3, ...xn, Y ),

where x1, x2, x3, ...xn are the independent variables, and Y is the target variable.

4.3 Random forests

Random Forest (RF) (Breiman, 2001) is a more complex bagging implementation of DTRs.
It grows and combines multiple DTRs to create a “forest”. The RF has demonstrated supe-
rior model performance when applied to credit modelling research (Lessman et al., 2015).
Formally, an RF is a predictor consisting of a collection of randomised base regression trees,
as given below:

r n(X , Dn) = Eθ [rn(X , θm, Dn)],

where Eθ represents the expectation taken with respect to the random parameter θ , con-
ditioned on X and the dataset Dn. The parameters (θ1, θ2, . . . , θm) are independent and
identically distributed (i.i.d.) realizations of the randomizing variable θ . Each tree is built
independently by randomizing over subsets of the data or features, and the ﬁnal output
r n(X , Dn) aggregates predictions across the ensemble.

4.4 Gradient boosting machine

Gradient Boosting Machine (GBM) is an implementation of boosting, an iterative technique
which adjusts the weight of an observation based on the last classiﬁcation (Friedman, 2001).
GBM and its variants such as Extreme Gradient Boosting have also performed strongly in the
comparative classiﬁcation literature (Odegua, 2020). The main idea of GBM is to add new
models to the ensemble sequentially. At each particular iteration, a new weak, base-learner
model is trained with respect to the error of the whole ensemble so far. One can arbitrarily
specify both the loss function and the base-learner models on demand. The general update
rule in GBM can be expressed as

Fm(x) = Fm−1(x) + γm hm(x), m = 1, 2, ..., M,

where where Fm(x) is the model prediction after m iterations (or trees), and

F0(x) = arg min
γ

n(cid:2)

L(yi , γ ),

i=1
and decision tree hm(x) is ﬁtted to the residuals by

hm(x) ≈ r

(m)
i

.

123

---

<!-- PAGE 10 -->

Annals of Operations Research

Here, the pseudo-residuals is computed using

(m)
i

r

= −

(cid:12)

(cid:13)

,

)

(m−1)
∂ L(yi , ˆy
i
(m−1)
∂ ˆy
i

(m)
where yi is the actual class label of the i-th data point, ˆy
is the predicted probability of the
i
i-th data point belonging to the positive class after m iterations, xi is the i-th input feature
vector, γm is the weight or learning rate for the m-th tree and controls the step size at each
iteration, and L is the loss function.

4.5 Support vector machine

Support Vector Machines (SVMs) are supervised learning models which work by constructing
hyperplanes in a multidimensional space to separates cases of different class labels (Vapnik,
1996). The samples that lie on boundaries of different classes are referred to as support vectors.
The underlying principle behind SVM-based classiﬁcation is to maximize the margin between
the support vectors using kernel functions. SVMs have achieved superior performance in both
retail (Obare & Muraya, 2018) and non-retail credit risk assessment (Teles et al., 2021). The
SVM is formulated as

f (x) =

P(cid:2)

i=1

ai K (x, xi ),

where P is the number of support vectors, ai is an element of the parameter vector, xi is
a vector of regressors, K is a function referred to as the kernel and ai is the number of
parameters. The kernel can be a Radial Basis Function, polynomial or a two-layer neural
network.

4.6 Multilayer perceptron

Multilayer Perceptron (MLP) is an Artiﬁcial Neural Network characterised by a back-
propagation algorithm which uses a special class of feedforward networks (Baum, 1988).
MLP has more than one hidden layer and the network moves only in the forward direction,
with no loopback. These neural networks are good for both classiﬁcation and prediction.
MLP has been successfully deployed in credit risk modelling research achieving superior
performance. MLP composes the ﬁnal output function of a network using

fk(x) = fk(ak(x)).

The function is applied to an input activation function consisting of ak(x). The input fre-
quently comprises a computation of the form

a(x) = W h(x) + b,

where x is the input vector, b is the bias vector, W is the weight matrix and h is the activation
function output. The function a(x) takes a vector argument and returns a vector as a result,
note that ak(x) is just one of the elements of a(x).

123

---

<!-- PAGE 11 -->

Annals of Operations Research

5 Datsets and numerical results

In this section, we describe GCD and Home Credit Dataset (HCD), the sampling procedure,
the data modelling and the simulation process. This is followed by presenting the results of
our numerical experiments.

5.1 Dataset and sampling

The publicly available German Credit Dataset (GCD) (Hofmann, 1994) is used in our exper-
iments. It contains 1000 observations across 20 predictor variables and a response variable,
indicating goods (i.e. negatives) and bads (i.e. positives). Due to conﬁdentiality which is
characteristic of ﬁnancial data most research is carried out using publicly available datasets
such as the GCD, which is among the most widely used public datasets for credit risk research
(see for examples, Beque et al., 2017; Due & Graff, 2019; Khashman, 2010; Dong et al.,
2010).

According to Ramezan et al. (2021), the size of the training data set is a major determi-
nant in the classiﬁcation performance. The authors compared the error of prediction across
different sample sizes for a variety of algorithms including RF, GBM and MLP. They found
that all these algorithms achieved more than 95% accuracy with a training sample of 625.

Alam et al. (2010) developed an approach for power estimation in LR to determine whether
a parameter is signiﬁcantly different to zero, combining the prior work of Whittemore (1981)
and Hsieh et al. (1998). Their results show that a sample size of 655 is needed to achieve a
statistical power of 0.9630.

These studies suggest that using a training sample of at least 655 will achieve strong
accuracy for machine learning models and adequate statistical power for models incorporating
hypothesis testing as per LR. Thus, the training sample of 712 used should be large enough
to minimise the error of prediction and to determine the real signiﬁcance of one or more
parameters.

5.2 Modelling data

In this section, we describe modelling the GCD. Predictors in this data include: • Status of
existing checking account • Duration in month • Credit history • Purpose • Credit amount •
Savings account • Present employment since • Installment rate in percentage of disposable
income • Personal status and sex • Other debtors • Present residence since • Property • Age
in years • Other installment plans • Housing • Number of existing credits at this bank • Job
• Number of dependents • Telephone • Foreign worker.

Prior to modelling, all predictor variables are transformed according to the Weights of Evi-
dence (WoE) discretization approach which is widely used in industry. While LR is the only
approach utilised that requires the monotonicity provided by WoE transformation, discretiza-
tion was performed to ensure that data aligned to industry practice as much as possible. Note
that making explanatory variables either strictly increasing or strictly decreasing (i.e. mono-
tonic) is a critical requirement for scorecard models; as indicators for riskiness each retained
variable must be linearly related to default for face validity in credit provision environments.
The formula for WoE discretization is given below:

(cid:14)

W oExi

= ln

% o f y = 0, wher e x = i
% o f y = 1, wher e x = i

(cid:15)

.

123

---

<!-- PAGE 12 -->

Annals of Operations Research

Table 2 Gamma parameters for
simulated EAD

Asset class

Shape

Scale

CC

SL

Mo

LL/SME

3

3

3

3

5000
50,000
400,000
1,000,000

5.3 Simulation of data

Next, we discuss the simulation of the GCD. Due to the lack of information necessary to
evaluate cost parameters, simulated variables representing four different asset classes were
incorporated into the GCD. Importantly, only the 20 original predictors and the target default
variable were accessible to the model. This ensured that all models operated with identical
default class information within each condition, whether training or testing. The simulated
variables were used exclusively for cost calculations, which informed model selection deci-
sions. To build on the GCD, we simulated the key missing variables required for cost analysis
across the 1000 observations that comprise the underlying dataset.

Furthermore, we simulate EAD values according to a Gamma distribution (see, for exam-

ples Jimenez & Mencia, 2007; Assadsolimani & Chetalova, 2017) given below:

f (z) = za−1e−bz
(cid:7)(a)

ba

,

z > 0, a, b > 0,

where (cid:7)(a) is the gamma function, a is the shape parameter, and b denotes the rate parameter.
We use the Gamma distribution to simulate four different EAD ranges representing typ-
ical magnitudes of exposure observed in a selection of different economies. Our review of
lending statistics from jurisdictions such as Australia (Australian Bureau of Statistics, 2024),
the UK (Bank of England, 2024), and the USA (Ostrowski, 2024) revealed signiﬁcant dis-
parities both between and within these regions. For instance, in the USA, average mortgage
lending exposures in California are over three times higher than those in Indiana. Further
complicating generalizations across jurisdictions are factors such as variations in exposure
pricing, exchange rates, regulatory practices, and the risk appetites of individual lenders.
To ensure representative asset classes, we selected scale-appropriate ranges that encompass
typical portfolios observed in Australia, the UK, and the USA.

The primary objective in evaluating these portfolios was to examine the inﬂuence of
model metrics, including FPM, between portfolios of varying sizes. Speciﬁcally, we sought
to determine whether larger interest payments inﬂuenced model selection decisions. The
simulated ranges across different portfolio scales provided meaningful differentiation to
support this analysis.

By modelling different exposures according to a Credit Card (CC), Small Loan (SL),
Mortgage (Mo) and Large Loan/Small to Medium Enterprise Loan (LL/SME), we seek
to observe the impact of different default and opportunity cost ranges. This follows from
Lessman et al. (2015) who found that the impact of failing to consider the bias towards true
positives was magniﬁed the larger the cost of a false positive.

After setting the seed to ensure values are reproducible, EAD distributions were simulated

using the parameters given in Table 2.

123

---

<!-- PAGE 13 -->

Annals of Operations Research

Table 3 Descriptive statistics of
simulated assets (GCD)

Asset class

Mean

Median

Standard deviation

CC

SL

Mo

LL/SME

$12,039
$152,263
$1,185,477
$2,996,111

$10,419
$139,396
$1,034,473
$2,679,932

$7134
$86,212
$698,810
$1,723,469

Table 4 Observed counts and
default rate (GCD)

Dataset

Good

Training

Test

502

198

Bad

210

90

Total

Default (%)

712

288

29.49

31.25

The proportion of the loan already paid (used to calculate Loan principal) is simulated

according to a Beta distribution, that is:

f (z) =

1
β(a, b)

za−1(1 − z)b−1, 0 ≤ z ≤ 1,

where β(a, b) is the beta function, a > 0 and b > 0 are shape parameters. The Beta
distribution was simulated with both shape parameters equal to one. In the asymptotic sample
this translates to a roughly uniform distribution between zero and one with some random
variation.

Monthly payment (Pmt) amounts are calculated according to the payment equation

detailed in Finlay (2009) as

Pmt = Pr × r /12 × (1 + r /12)12t

(1 + r /12)12t − 1

,

where Pr = Principal, r = Annual interest and t = Term of the loan in years.

We also keep the underlying data as realistic as possible according to the aforementioned
hypothetical asset classes, basing distributions on real portfolios observed at Australian and
European banks. Despite these efforts, some differences are still apparent in the data. The
relatively high default rate observed in the GCD clearly sets it apart from datasets observed in
industry. However, given well-known constraints with classiﬁcation modelling it is common
practice to perform sampling on credit risk data such that the minority class (ie defaults) is
markedly increased. Therefore, we can simply view the larger than normal minority class
as being the result of prior sampling to address the class imbalance. In Table 3, we provide
descriptive statistics for the four simulated asset classes; CC, SL, Mo and LL/SME.

In Table 4, we provide the split between the training and test datasets. It includes counts
of good (non-defaulting) and bad (defaulting) observations as well as the percent of each
outcome condition. Random sampling between the training and test datasets led to slight
variations in defaulting proportions. Initial testing revealed no signiﬁcant differences in results
between equally sampled classes and randomly sampled ones. Therefore, to maintain realistic
conditions, we opted for the randomly sampled approach, which is commonly used in industry
practices.

A ﬁnal potential deviation from reality relates to the credit card asset class, whereby it
was treated like a one-off loan held for a set number of months. This is not realistic since on
average credit card customers tend to draw down credit continuously, implying that we may

123

---

<!-- PAGE 14 -->

Annals of Operations Research

Table 5 Descriptive statistics of Home Credit Dataset (HCD)

Asset class

Mean

Median

Standard deviation

Various product types

$1,203,458

$1,069,602

$697,163

Table 6 Observed counts and
default rate (HCD)

Dataset

Good

Bad

Total

Default (%)

Training

Test

197,910
84,876

17,448
7377

215,258
92,253

8.10

7.99

have under represented the interest which might normally be collected over the life of this
asset class.

To further demonstrate the robustness of the proposed FPM, we applied it to the HCD also
used in other studies, such as Wang et al. (2020). This data, available on Kaggle (Montoya
et al., 2018), highlights Home Credit strives to expand ﬁnancial inclusion for the unbanked
population, featuring a distinct loss structure unlike typical lending portfolios. Since the
HCD encompasses various lending products with different loss dynamics, this introduces
some noise into predictions. However, it contains information similar to the GCD, covering
a larger dataset of 307,501 rows in the fully labelled subset.

For the comparison purpose, we analysed a single portfolio consisting of various product
types in the HCD rather than multiple single asset classes, using the same simulation approach
as with the GCD. In Table 5, we provide descriptive statistics for the non-speciﬁc portfolio
from the HCD.

Table 6 displays information on the counts of good (non-defaulting) and bad (defaulting)
observations, the percentage of each outcome condition and the rate of default in the training
and test splits of the HCD.

5.4 Implementation

The ﬁnal decision prior to modelling was to either optimise thresholds according to speciﬁc
models which would have enhanced realism yet reduced comparability, or to hold the thresh-
old constant at t = 0.5 to focus on the differential capabilities of each algorithm and the
performance metrics; we opted for the latter. Furthermore, while preliminary model tuning
produced some small increases in model statistical performance, it came at the cost of over-
ﬁtting to the training dataset. Thus, as all six models achieved acceptably strong performance
according to the statistical metrics only minor model tuning was performed. Statistical met-
rics were calculated ﬁrst using automated outputs from R software and then recalculated
manually according to the relevant equations.

5.5 Results

In this section, we present the results of our numerical experiments. We start by comparing
the performance of our proposed cost metric with that of the commonly used approach by
Bahnsen et al., and noting differences and similarities in model ranking between the two
approaches.

123

---

<!-- PAGE 15 -->

Annals of Operations Research

Table 7 False prediction costs using Bahnsen’s approach (CSEDCM) as a percentage of proposed cost metric
(FPM), Eq. (3)

Threshold (cost)

Methods

CC (%)

SL (%)

Mo (%)

LL/SME (%)

Default

Default

Default

Default

Default

Default

Opportunity

Opportunity

Opportunity

Opportunity

Opportunity

Opportunity

Overall

Overall

Overall

Overall

Overall

Overall

MLP

DTR

GBM

LR

RF

SVM

MLP

DTR

GBM

LR

RF

SVM

MLP

DTR

GBM

LR

RF

SVM

1.04
1.29
1.02
1.21
1.20
1.28
30.72
41.15
25.56
30.91
31.74
29.88
17.30
19.26
13.48
13.62
11.70
21.51

7.67
8.20
7.05
9.77
8.98
5.74
43.43
43.50
45.47
49.62
44.61
14.06
33.63
27.54
33.08
35.54
26.39
10.95

7.10
8.50
7.63
7.20
8.21
11.22
38.09
33.34
31.16
44.61
39.45
29.94
29.61
21.59
22.40
30.01
22.56
24.61

8.09
11.34
9.14
10.76
13.87
15.51
40.50
35.01
38.96
46.39
22.33
45.09
30.87
24.11
27.65
32.63
17.21
39.91

We calculated the cost of false predictions using both the proposed FPM and that put
forward by the CSEDCM. Noting that all of CSEDCM’s cost estimates were smaller than
the FPM, we then calculated the percentage for each model and threshold position using the
following equation:

Cost% = C S E DC M

× 100.

(3)

F P M
In Table 7, we report the results obtained using this equation. The ﬁrst two columns in
this table are the cost types and the six algorithms used in our comparison, and the last
four columns are the simulated asset classes. The results show that Bahnsen’s approach
routinely underestimates the true costs of false predictions, with under prediction sometimes
as different as one hundredth of the proposed FPM. For example, in estimating the default
cost of false prediction for the GBM, Bahnsen’s estimate was just 1.02% of the FPM.

The huge disparity in false prediction costs drastically increases the likelihood for
inadvertently selecting the wrong model under the belief it presents the lowest cost of misclas-
siﬁcation. We’ve further enhanced the model selection process by demonstrating performance
measurement differentials on either sides of the decision boundary, whereas most industry
practitioners as well as researchers consider only the overall view, and that is usually done
comparing averaged statistical metrics such as Gini and AUC. Based on the cost of false
prediction estimated by the CSEDCM compared to the cost of false prediction estimated by
the FPM from this table, we will utilise our proposed cost metric FPM for further analysis.
If the proposed FPM is utilized to estimate the cost of false prediction (the results presented
in Table 8), the MLP demonstrates the lowest misclassiﬁcation costs across all four asset
classes (CC, $17.4m; SL, $42.2m; Mo, $260.7m; LL/SME, $488.7m), and is therefore the

123

---

<!-- PAGE 16 -->

Annals of Operations Research

best performing model. By contrast, if the CSEDCM was used for model selection, the RF
would be selected for the CC ($2.6m) and LL/SME ($91.8m) asset classes and the SVM for
small loans ($5.1m) and DTR for mortgages ($72.1m). Interestingly, when we peel back the
cover to examine performance on either side of the decision boundary, both cost approaches
favor the MLP for default cost, and RF performs best for opportunity cost, yet the considerable
differences in the magnitude of false prediction costs result in differences at the aggregate
level across the decision boundary, which is the level at which the CSEDCM approach
operates at.

Now, we discuss the comparison between each respective method according to the ﬁnancial
cost of losses calculated on false predictions. The losses associated with false negatives
(applicants the model predicts as good but who later default; the default cost), as well as false
positives (applicants the model predicts as bad yet who do not default; the opportunity cost and
mostly comprise the interest revenue foregone by rejecting an otherwise good applicant), are
included. Separating observations into false positives versus false negatives required splitting
the sample above and below the threshold which enhanced comparisons with the statistical
metrics.

The comparison results, the costs associated with individual components and the overall
FPM, are provided in Table 8. The ‘Above’ column represents false positive misclassiﬁca-
tion costs, incurred when the model incorrectly classiﬁes individuals as defaulters who did
not default. The ‘Below’ column captures false negative misclassiﬁcation costs, summing
the losses from applicants classiﬁed as low risk but who ultimately defaulted. Finally, the
‘Overall’ column represents the total misclassiﬁcation costs, combining both false positives
and false negatives, comprising the proposed metric.

Next, we provide the results of the classical statistical performance metrics in Table 9,
where the ﬁrst two columns show the six methods used and the threshold split, and the last
three columns are the statistical metrics. Typically these are only presented at the overall level,
which is effectively an average across all observations, however we additionally estimate
performance measures above and below the threshold. Splitting the performance metrics in
this manner provides further insight into each method and how they perform on either side
of the decision threshold as well as the measurements themselves.

The results from Table 9 show that when we rank each algorithm by statistical performance
seeking to identify the best method, we see that the method rankings are very different
comparing either side of the threshold with overall. For example, Gini shows that the GBM
performed best above the threshold while the LR was superior below, yet it was the MLP
that came out on top according to this metric.

Further, the Gini and AUC result in identical rankings, reinforcing the notion that the
practise of presenting both metrics together is redundant. By contrast, the accuracy of methods
almost always ranks methods differently to Gini/AUC, reﬂecting the different philosophy in
taking the proportion of true predictions from all predictions, versus discriminating between
goods and bads using the number of concordant pairs.

The routine use of these statistical metrics in isolation is problematic because as has
already been established, while they may be useful in distinguishing between a good and
a bad model, they are not useful for making selections between good models. Moreover,
they do not provide insight on the real parameter of interest which is minimising the false
predictions, in particular their cost in a credit scoring environment. Furthermore, ‘overall’
estimates effectively average across the decision boundary thus obscuring important details
of model performance.

We note that when used in the traditional manner assessing statistical performance overall,
the MLP was the clear winner overall, yet only marginally stronger than the LR. The marginal

123

---

<!-- PAGE 17 -->

Annals of Operations Research

Table 8 Financial cost metrics
(per $1000) by methods, asset
class and threshold using test
dataset (GCD)

Method

Assets

Above

Below

Overall

DTR

GBM

LR

MLP

RF

SVM

DTR

GBM

LR

MLP

RF

SVM

DTR

GBM

LR

MLP

RF

SVM

DTR

GBM

LR

MLP

RF

SVM

CC

CC

CC

CC

CC

CC

SL

SL

SL

SL

SL

SL

Mo

Mo

Mo

Mo

Mo

Mo

LL/SME

LL/SME

LL/SME

LL/SME

LL/SME

LL/SME

$11,233
$10,656
$8134

$9541

$7749
$13,662
$30,664
$38,119
$29,245
$30,607
$25,031
$29,145
$176,080
$204,541
$180,241
$189,427
$155,153
$242,131
$314,838
$402,095
$324,782
$343,546
$210,919
$537,818

$13,686
$10,335
$11,337
$7882
$14,784
$5652
$25,311
$18,163
$15,973
$11,557
$26,199
$17,368
$158,013
$121,299
$115,443
$71,316
$182,587
$96,377
$268,673
$245,552
$204,305
$145,248
$322,532
$114,113

$24,919
$20,991
$19,471
$17,423
$22,533
$19,314
$55,975
$56,283
$45,218
$42,164
$51,230
$46,513
$334,093
$325,840
$295,684
$260,743
$337,741
$338,508
$583,511
$647,647
$529,087
$488,795
$533,451
$651,931

statistical improvement obtained from the MLP would usually be discarded in favour of the
simpler and more easily implemented and understood LR. Indeed, when used in conjunction
with the FPM, the true cost of selection decisions can be easily understood.

In addition, the differential performance on either side of the threshold provides some
insight into how each algorithm works, and, where each performs strongest. For instance, it
is notable that according to ACC the SVM performed amongst the best below the threshold,
yet it was also the worst above the threshold. The observed variation in method ranking
between model metrics underscores the notion that using traditional performance measures
blindly results in suboptimal method selections. Certainly averaging metrics across the deci-
sion boundary obscures important details on performance. Thus, the traditional performance
measures present challenges for method selection and must be used with caution.

From the results, a notable observation supports the ﬁndings by Verbraken et al. (2015),
whereby the larger the magnitude of the principal loan amount, the more important that
opportunity costs become. Given the scale of the largest asset class we simulated and the
consequent magnitude of interest revenue that would be lost, our ﬁndings show that for these
data opportunity costs are larger than default costs. The disparity between opportunity and
default cost is largest where the initial exposure is smallest, in the credit card asset class, and
diminishes as the average size of the asset class increases. This suggests that the larger the

123

---

<!-- PAGE 18 -->

Table 9 Statistical metrics by
threshold and methods using test
dataset (GCD)

Method

Threshold

Gini

MLP

DTR

GBM

LR

RF

SVM

MLP

DTR

GBM

LR

RF

SVM

MLP

DTR

GBM

LR

RF

SVM

Above

Above

Above

Above

Above

Above

Below

Below

Below

Below

Below

Below

Overall

Overall

Overall

Overall

Overall

Overall

0.3273
0.3906
0.4131
0.3681
0.3279
0.3628
0.8358
0.8224
0.8224
0.8558
0.8014
0.7682
0.8914
0.8517
0.8561
0.8903
0.8523
0.8392

Annals of Operations Research

ACC

0.7835
0.7619
0.7553
0.8046
0.7922
0.71
0.9319
0.8725
0.8969
0.9005
0.8863
0.9198
0.8819
0.8403
0.8507
0.8715
0.8611
0.8467

AUC

0.6636
0.6953
0.7065
0.684
0.6639
0.6814
0.9179
0.9112
0.9112
0.9279
0.9007
0.8841
0.9457
0.9259
0.9281
0.9452
0.9262
0.9196

credit contract, the more careful lenders must be to avoid misclassifying a good credit risk
as bad.

However, this is in a limited sample of 1000 customers, whereas in a real credit portfo-
lio products like CC and SL customers may number in their millions. While our ﬁndings
support the notion that opportunity costs become increasingly important the larger the prin-
ciple. However, given the volume of low value lending products like CC this may not hold,
particularly in unsecured lending in which the LGD tends to be signiﬁcantly higher.

From a method selection perspective, the algorithm resulting in the smallest loss was
the winner, in line with the proﬁt-based motive which characterises commercial enterprise.
Results show that the RF posed the lowest misclassiﬁcation cost across all asset classes
related to false positives, that is for applicants that the model has scored above the decision
threshold who do not default. By contrast, the SVM posed the lowest misclassiﬁcation costs
for two asset classes (CC and LL). The MLP misclassiﬁcation cost was lowest for SL and
Mo for applicants who the method approves, that is applicants who score below the decision
threshold, yet who later default. Overall, the MLP performed the best across all four asset
classes.

We conclude by discussing the power curve that is used to empirically determine the
statistical power in our training sample. More precisely, the curve is produced to determine
whether the GCD provides adequate statistical power with which to make inferences about
model performance. While hypothesis testing is only a feature of statistical modelling, and
therefore, only relates to the LR algorithm, it is instructive for comparison purposes with the
other methods investigated. Note that the statistical power was calculated using two assumed
target variable probabilities, the required inputs for this calculation. However, under both
probability assumptions, the statistical power approached 100% prior to the training sample
reaching 700. Thus, the power curve demonstrates that the training sample selected at random

123

---

<!-- PAGE 19 -->

Annals of Operations Research

Fig. 1 Sample size power curve for classiﬁcation

from the GCD was sufﬁciently large to provide adequate statistical power with which to
estimate one or more parameters using LR. Figure 1 depicts the results of the power analysis.
Furthermore, as machine learning algorithms do not formally perform hypothesis testing
as statistical models do, true power analysis is not possible. Instead, we calculate the error
of prediction over a range of training sample sizes to test whether the sample size used was
large enough. The determination of the adequacy of the size was made by observing whether
the error rate was still declining as the training sample grew, or whether it ﬂattened out. Each
model was tested on each of nine training samples extracted from the GCD ranging in size
from 100 to 900. After each subset was extracted to form the training data, the remaining
proportion comprised the test data. Thus, where the training dataset was 100, the test dataset
was 900; where the training dataset was 200, the test dataset was 800, and so on until the
maximum split whereby the training dataset was 900 and the test dataset was 100. The
sample size versus error rate charts for all six methods are shown in Figs. 2, 3, 4, 5, 6 and 7,
respectively. Note that in Fig. 1, the power greater than 0.8 is generally considered acceptable,
while for Figs. 2, 3, 4, 5, 6 and 7 the lower the error rate the better quality the method.

In early method testing, model tuning appeared to improve the ﬁt to the training dataset
yet reduced performance on the test data. Thus, to minimise overﬁtting to the training dataset
only basic model tuning was performed. The sample size by error plots for each respective
model reveals that the training and test datasets achieved similar performance irrespective
of sample size, with only the smallest training sample size of 100 (test = 900) resulting in a
maximum error of prediction approaching 0.2.

The two methods which showed elevated error rates were the GBM and the SVM. Contrary
to the converging performance between training and test datasets observed for the other four
methods, the error of prediction for these methods were substantially larger for the test dataset
irrespective of its relative size in comparison to the training data. For example, for the GBM
there is at least a 10% difference in performance even when the training data was at its
maximum of 900.

While performance never converges across any sample size it is noteworthy that the error
rate in the test data is generally declining for both the GBM and the SVM as the size of the

123

---

<!-- PAGE 20 -->

Annals of Operations Research

Fig. 2 LR sample size versus error rate

Fig. 3 RF sample size versus error rate

training dataset increases, and relatively ﬂat for the other four methods. While performance
may have continued to improve if the training sample was even larger, it implies that the
GBM and the SVM may require larger training datasets to control the error in test data. An
alternative interpretation is that the GBM and the SVM formulations did not generalise to
this speciﬁc dataset as well as the other algorithms.

Similar levels of the performance for both test and training datasets were observed for
LR, RF, MLP and DTR, yet for the GBM the actual magnitude of difference in error was
only around 0.1 by the time training data was around 700, and roughly 0.06 for the SVM.
Taken together these results support the notion that the training dataset was sufﬁciently large
to produce reliable results for all algorithms tested.

123

---

<!-- PAGE 21 -->

Annals of Operations Research

Fig. 4 GBM sample size versus error rate

Fig. 5 MLP sample size versus error rate

As mentioned earlier, we used the HCD with a single portfolio of various product types

to further demonstrate the robustness of the FPM.

Table 10 presents model performance on the HCD including a statistical accuracy metric
and the difference from the LR algorithm for reference. Using a classical statistical perfor-
mance approach, SVM would typically be chosen. However, the accuracy differences among
the six algorithms are trivial. In contrast, the ﬁnancial losses from false predictions in the
FPM reveals signiﬁcant differences across algorithms. This is consistent with the observa-
tions for the GCD. The FPM identiﬁed RF as the best-performing model, closely followed by
the MLP. The results also indicate that utilizing the FPM would achieve a signiﬁcant saving
of approximately $321 million and $297 million over the LR, respectively.

123

---

<!-- PAGE 22 -->

Annals of Operations Research

Fig. 6 DTR sample size versus error rate

Fig. 7 SVM sample size versus error rate

Table 10 Financial cost metrics (per $1000) by methods using test dataset HCD

Method

Accuracy

Above

Below

Overall

Differ from LR

DTR

GBM

LR

MLP

RF

SVM

0.9197

0.9201

0.9200

0.9200

0.9200

0.9155

$353,830

$310,680

$318,150

$204,900

$138,990

$185,810

$635,740

$498,620

$473,180

$289,330

$330,380

$316,250

$989,570

$809,300

$791,330

$494,230

$469,370

$502,060

−$198,240
−$17,970
–

$297,100

$321,960

$289,270

123

---

<!-- PAGE 23 -->

Annals of Operations Research

6 Discussion and conclusion

In this section, we provide discussion on the results presented in this paper and conclude
with future research directions.

Publicly available datasets enable industry practitioners to emulate the results achieved
in published literature more easily, thus expediting the uptake of new research. This study
shows that even relatively small, publicly available datasets like the GCD and the HCD are
not only large enough to provide sufﬁcient statistical power with which to train statistical
models but also to minimise the error of prediction arising from the application of machine
learning algorithms on training samples anywhere above 100 observations.

Moreover, we demonstrated that where necessary ﬁnancial information is not available, it
can be simulated to provide insights on cost dynamics as a consideration in model selection
particularly where these are calibrated to real lending portfolios. While our cost dynamics are
estimated on simulated data, the results from tests on statistical power and error of prediction
show that these samples are sufﬁciently large to avoid sampling bias and therefore, make
inferences on ﬁnancial losses.

Furthermore, by splitting results on either side of the decision threshold, we showed
how model performance differs according to which algorithm has been used, thus providing
additional insights into algorithm selection and performance metrics alike. The model ranking
according to the classical performance metrics varied greatly when split in this manner.

The present study has focused on individual algorithms. However, as model performance
and ranking were highly variable on either side of the decision boundary, a stacking approach
may well outperform single algorithms. By combining the strengths of algorithms on either
side of the threshold it may be possible to eliminate or at least mitigate their weaknesses to
develop a stronger overall prediction system.

In addition, building on previous research, we have sought to propose the most realistic
estimates of false prediction costs yet. Although we utilised relatively small datasets of few
observations, the proposed FPM could be extended and applied to larger lending portfolios
which could potentially provide a signiﬁcant ﬁnancial beneﬁt to organizations.

Taking the example of the mortgage asset class, the best performing algorithm overall
was, for example, the MLP in the GCD, and selecting that over the next best algorithm (LR)
resulted in a beneﬁt of approximately 35 million on a dataset of <300 applicants. While this
is a large enough difference to be meaningful in selecting the most ﬁt-for-purpose model,
a real-life mortgage portfolio could easily be a thousand times larger. Applying the ratio of
1:1000 puts the value of selecting MLP over LR at $35 Billion, a massive ﬁnancial beneﬁt
for even the largest corporations trading on a global scale.

Furthermore, we have noted the extant issues with the three most popular performance
metrics, AUC, Gini, and ACC. Prior research suggests these measures are unsuitable for
model selection. For example, although AUC may be able to differentiate a good model from
a bad one it is unable to distinguish between good ones. While it is coherent at separating class
membership, it is also incoherent on the costs of those classes, and the actual loss resulting
from false predictions. Although these incoherent approaches may be useful as a hurdle
to differentiate between good and bad candidate models, the ﬁnancial loss should be used
for identifying the best performer. Therefore, we propose an optimal system whereby once
candidate models achieve a minimum performance threshold, the ﬁnancial loss measures
should be used to select the best-performing model.

Using the proposed Financial Performance Metric (FPM) enables industry practitioners
to select models which best align with their motives for using the models in the ﬁrst place for

123

---

<!-- PAGE 24 -->

Annals of Operations Research

proﬁt. As it is demonstrated herein for credit scorecards, the same principles can be applied
to any commercial application of classiﬁcation models in which the loss function is more
nuanced than simply separating goods and bads.

Most of the published credit modelling research focuses on application scorecards, never-
theless, they are not the most material models used by banks globally. Future research should
deeply examine behavioral models which measure the ongoing risk once applicants become
customers. Both point in time, as well as through the economic cycle models are important
considerations required by prudential authorities. These models have a huge impact on not
only retained solvency capital, but also the overall health of the ﬁnancial system. We tested
our ﬁndings on a comparison dataset, but further testing including replacing simulated vari-
ables with real-time measurements may serve to underscore the value of using the ﬁnancial
performance metric. Lastly, there is a dearth of published research on optimal monitoring
solutions for credit models over time, which is an urgent priority for industry.

Funding Open Access funding enabled and organized by CAUL and its Member Institutions This research
received no external funding.

Declarations

Conﬂict of interest The authors declare that they have no known competing ﬁnancial interests or personal
relationships that could have appeared to inﬂuence the work reported in this paper.

Ethical approval This article does not contain any studies with human participants or animals performed by
any of the authors.

Open Access This article is licensed under a Creative Commons Attribution 4.0 International License, which
permits use, sharing, adaptation, distribution and reproduction in any medium or format, as long as you give
appropriate credit to the original author(s) and the source, provide a link to the Creative Commons licence,
and indicate if changes were made. The images or other third party material in this article are included in the
article’s Creative Commons licence, unless indicated otherwise in a credit line to the material. If material is
not included in the article’s Creative Commons licence and your intended use is not permitted by statutory
regulation or exceeds the permitted use, you will need to obtain permission directly from the copyright holder.
To view a copy of this licence, visit http://creativecommons.org/licenses/by/4.0/.

References

Aodha, O. M., & Brostow, G. J. (2013). Revisiting example dependent cost sensitive learning with decision
trees. In 2013 IEEE international conference on computer vision (pp. 193–200). Washington, DC, USA.
Assadsolimani, M. & Chetalova, D. (2017). Estimating VaR in credit risk: Aggregate vs single loss distribution.
Australian Bureau of Statistics. (September 2024). Lending Indicators, ABS Website. Accessed 10 December

2024.

Bahnsen, A. C., Aouada, D., & Ottersten, B. (2014). Example-dependent cost-sensitive logistic regression for
credit scoring. In 13th international conference on machine learning and applications (pp. 263–269).
https://doi.org/10.1109/ICMLA.2014.48

Bahnsen, A. C., Aouada, D., & Ottersten, B. (2015). Example-dependent cost-sensitive decision trees. Expert

Systems with Applications, 42(19), 6609–6619. https://doi.org/10.1016/j.eswa.2015.04.042

Bank of England. (November 2024). Money and Lending, Bank of England website. Accessed 10 December

2024.

Banu, I. M. (2013). The impact of credit on economic growth in the global crisis context. Procedia Economics

and Finance, 6, 25–30.

Baum, E. (1988). On the capacity of multilayer perceptron. Journal of Complexity, 4, 193–215.
Bequé, A., Coussement, K., Gayler, R., & Lessmann, S. (2017). Approaches for credit scorecard calibration:

An empirical analysis. Knowledge-Based Systems, 134, 213–227.

Breiman, L. (2001). Random forests. Machine Learning, 45, 5–32. https://doi.org/10.1023/A:1010933404324

123

---

<!-- PAGE 25 -->

Annals of Operations Research

Cantrell, B. W., McInnis, J. M., & Yust, C. G. (2014). Predicting credit losses: Loan fair values versus historical

costs. The Accounting Review, 89(1), 147–176. https://doi.org/10.2308/accr-50593

Dmitriev, P., & Wu, X. (2016). Measuring metrics. In Proceedings of the 25th ACM international on conference
on information and knowledge management (CIKM ’16). Association for Computing Machinery, New
York, NY, USA (pp. 429–437). https://doi.org/10.1145/2983323.2983356

Dong, G., Lai, K. K., & Yen, J. (2010). Credit scorecard based on logistic regression with random coefﬁcients.

Procedia Computer Science, 1(1), 2463–2468.

Dua, D., & Graff, C. (2019). UCI machine learning repository. School of Information and Computer Science,

University of California, Irvine, CA. https://archive.ics.uci.edu/ml/datasets

Dumitrescu, E., Hué, S., Hurlin, C., & Tokpavi, S. (2022). Machine learning for credit scoring: Improving
logistic regression with non-linear decision-tree effects. European Journal of Operational Research,
297(3), 1178–1192. https://doi.org/10.1016/j.ejor.2021.06.053

Elkan, C. (2001). The foundations of cost-sensitive learning. In Seventeenth international joint conference on

artiﬁcial intelligence (pp. 973-978).

Finlay, S. (2009). Consumer credit fundamentals (2nd ed.). Palgrave MacMillan.
Fiore, U., De Santis, A., Perla, F., Zanetti, P., & Palmieri, F. (2017). Using generative adversarial networks for
improving classiﬁcation effectiveness in credit card fraud detection. Information Sciences, 479, 448–455.
https://doi.org/10.1016/j.ins.2017.12.030

Friedman, J. H. (2001). Greedy function approximation: A gradient boosting machine. Annals of Statistics,

29(5), 1189–1232.

Gea-Carrasco, C. (2015). IFRS 9 will signiﬁcantly impact banks’ provisions and ﬁnancial statements. In

Moody’s analytics risk perspectives (Vol. V).

Hand, D. J. (2009). Measuring classiﬁer performance: A coherent alternative to the area under the ROC curve.

Machine Learning, 77, 103–123. https://doi.org/10.1007/s10994-009-5119-5

Hofmann, H. (1994). Statlog (German Credit Data) [Dataset]. UCI machine learning repository. https://doi.

org/10.24432/C5NC77

IASB. (2014). IFRS standard 9: Financial instruments, International Accounting Standards Board.
Khashman, A. (2010). Neural networks for credit risk evaluation: Investigation of different neural models and

learning schemes. Expert Systems with Applications, 37(9), 6233–6239.

Lessmann, S., Baesens, B., Seow, H. V., & Thomas, L. C. (2015). Benchmarking state-of-the-art classiﬁcation
algorithms for credit scoring: An update of research. European Journal of Operational Research, 247(1),
124–136. https://doi.org/10.1016/j.ejor.2015.05.030

Liu, Y., Zhou, Y., Wen, S., & Tang, C. (2014). A strategy on selecting performance metrics for classiﬁer
evaluation. International Journal of Mobile Computing and Multimedia Communications, 6, 20–35.
https://doi.org/10.4018/IJMCMC.2014100102

Mahbobi, M., Kimiagari, S., & Vasudevan, M. (2023). Credit risk classiﬁcation: An integrated predictive
accuracy algorithm using artiﬁcial and deep neural networks. Annals of Operations Research, 330(1),
609–37.

Maldonado, S., Bravo, C., López, J., & Pérez, J. (2017). Integrated framework for proﬁt-based feature selection

and SVM classiﬁcation in credit scoring. Decision Support Systems, 104, 113–121.

Martin, J., Taheri, S., & Abdollahian, M. (2024). Optimizing ensemble learning to reduce misclassiﬁcation
costs in credit risk scorecards. Mathematics, 12(6), 855. https://doi.org/10.3390/math12060855
Marzban, C. (2004). The ROC curve and the area under it as performance measures. Weather and Forecasting,

19(6), 1106–1114.

Mencia, J., & Jimenez, G. (2007). Modeling the distribution of credit losses with observable and latent factors
(April 18, 2007). In Banco de España Research Papers. Available at SSRN. https://doi.org/10.2139/ssrn.
981109

Montoya, A., Odintsov, K., & Kotek. M. (2018). Home Credit Default Risk. https://kaggle.com/competitions/

home-credit-default-risk, Kaggle

Obare, D. M., & Muraya, M. M. (2018). Comparison of accuracy of support vector machine model and logistic
regression model in predicting individual loan defaults. American Journal of Applied Mathematics and
Statistics, 6(6), 266–271. https://doi.org/10.12691/ajams-6-6-8

Odegua, R. (2020). Predicting bank loan default with extreme gradient boosting.
Ostrowski, J. (2024). Average mortgage debt in 2024, Bankrate website. Accessed on 10 December 2024.
Ramezan, C. A., Warner, T. A., Maxwell, A. E., & Price, B. S. (2021). Effects of training set size on supervised
machine-learning land-cover classiﬁcation of large-area high-resolution remotely sensed data. Remote
Sensing, 13, 368. https://doi.org/10.3390/rs13030368

Schebesch, K., & Stecking, R. (2005). Support vector machines for classifying and describing credit applicants:
Detecting typical and critical regions. Journal of The Operational Research Society, 56, 1082–1088.
https://doi.org/10.1057/palgrave.jors.2602023

123

---

<!-- PAGE 26 -->

Annals of Operations Research

Tripathi, D., Edla, D. R., Kuppili, V., & Bablani, A. (2020). Evolutionary extreme learning machine with novel

activation function for credit scoring. Engineering Applications of Artiﬁcial Intelligence, 96, 103980.

Teles, G., Rodrigues, J. J. P. C., Rabêlo, R. A. L., & Kozlov, S. A. (2021). Comparative study of support vector
machines and random forests machine learning algorithms on credit operation. Software: Practice and
Experience, 51, 2492–2500. https://doi.org/10.1002/spe.2842

Thomas, L. C., Edelman, D. B., & Crook, J. N. (2002). Credit scoring and its applications. Philadelphia:

SIAM Monographs on Mathematical Modeling and Computation.

Tian, Z., Xiao, J., Feng, H., & Wei, Y. (2020). Credit risk assessment based on gradient boosting decision tree.

Procedia Computer Science, 174, 150–160. https://doi.org/10.1016/j.procs.2020.06.070

Vapnik, V. (1996). The nature of statistical learning theory. Springer.
Verbraken, T., Bravo, C., Weber, R., & Baesens, B. (2014). Development and application of consumer credit
scoring models using proﬁt-based classiﬁcation measures. European Journal of Operational Research,
238(2), 505–513. https://doi.org/10.1016/j.ejor.2014.04.001

Wang, C., Deng, C., & Wang, S. (2020). Imbalance-XGBoost: Leveraging weighted and focal losses for binary
label-imbalanced classiﬁcation with XGBoost. Pattern Recognition Letters, 136, 190–197. https://doi.
org/10.1016/j.patrec.2020.05.035

Wang, H., Kou, G., & Peng, Y. (2021). Multi-class misclassiﬁcation cost matrix for credit ratings in peer-
to-peer lending. Journal of the Operational Research Society, 72(4), 923–934. https://doi.org/10.1080/
01605682.2019.1705193

Xia, Y., Liu, C., & Liu, N. (2017). Cost-sensitive boosted tree for loan evaluation in peer-to-peer lending.
Electronic Commerce Research and Applications, 24, 30–49. https://doi.org/10.1016/j.elerap.2017.06.
004

Yhip, T. M., & Alagheband, B. M. D. (2017). The practice of lending. Palgrave Macmillan. https://doi.org/

10.1007/978-3-030-32197-0

Zhang, T., Zhang, W., Xu, W., & Hao, H. (2018). Multiple instance learning for credit risk assessment with

transaction data. Knowledge-Based Systems. https://doi.org/10.1016/j.knosys.2018.07.030

Publisher’s Note Springer Nature remains neutral with regard to jurisdictional claims in published maps and
institutional afﬁliations.

123

<!-- MARKITDOWN CONVERSION -->

<!-- Full MarkItDown conversion for formatting fidelity. -->

AnnalsofOperationsResearch
https://doi.org/10.1007/s10479-025-06514-x
ORIGINAL RESEARCH
Anovelfinancialperformancemetrictominimize
misclassificationcostsinmodelselection
John Martin1·Mali Abdollahian1·Sona Taheri1 ·David Akman1
Received:3January2023/Accepted:28January2025
©TheAuthor(s)2025
Abstract
Anovelfinancialperformancemetric(FPM)isintroducedseekingtominimisethemisclas-
sificationcostarisingfromfalsepositivesandfalsenegativesincreditriskassessment.Using
theGermanCreditDataset(GCD),importantfinancialvariablesaresimulatedaccordingto
fourdifferentassetclassestoenableamoreaccurateandreliable,multidimensionalmodel
selection.ThemisclassificationcostarisingfromFPMiscomparedwithcommonlyusedsta-
tisticalmetricsandthecreditscoringexampledependentcostmatrix(CSEDCM)metric.The
resultsshowthatCSEDCMunderestimatesfalsepredictioncostsbyasmuchas99%com-
paredtotheFPM.Arangeofhigh-performancemachinelearningmethodswascompared
usingFPMandstatisticalmetrics.TheMulti-LayerPerceptronoutperformedothermethods
onstatisticalmetricsandoverallonfinancialcosts,whileamixofalgorithmsworkedbest
oneithersideofthedecisionthreshold.TheresultsconfirmedthattheproposedFPMwould
provideasignificantfinancialbenefittoorganisations.
Keywords Creditscorecard·Financialperformancemetric·Machinelearning·German
credit
1 Introduction
Acreditdefaultisanegativeeventforbothborrowersandlenders,butcanalsoimpactthe
broadereconomy.Becausecreditisakeydriveroftheeconomy,essentialforthestability
andgrowthoftheglobalfinancialsystem,noeconomy,irrespectiveofhowadvanceditmay
be,candevelopinitsabsence(Banu,2013).Astheglobalfinancialcrisisandmorerecent
eventssuchastheCOVID-19pandemichavedemonstrated,creditlossesrelatedtoloanscan
haveasignificantdetrimentalimpactonthebroadereconomy(Cantrelletal.,2014).
B
SonaTaheri
sona.taheri@rmit.edu.au
JohnMartin
S3801949@student.rmit.edu.au
MaliAbdollahian
mali.abdollahian@rmit.edu.au
DavidAkman
david.akman@rmit.edu.au
1 SchoolofScience,RMITUniversity,Melbourne,VIC,Australia
123

AnnalsofOperationsResearch
Toprotectagainstlosses,lendersseektomaintainrobustlendingpracticesthroughopti-
mising credit risk assessment. Indeed, the centrality of credit to the monetary economy
throughout the economic cycle underscores the importance of accurate credit assessment.
Historically,creditworthinesswasevaluatedusinghumanjudgement.However,thescaleof
lendinghasincreasedovertimesuchthatcontemporaneously,mostlendersdeployclassifi-
cationmodelstoperformthistaskatscale.
Scorecardmodelsareoneofthemainapplicationsofclassificationmodelsincreditrisk.
Used to assess creditworthiness, scorecard models associate historical characteristics like
priorloanperformancewithdefaulttoestimatetheprobabilityofdefault.Oncethishashas
beenderiveditisthencomparedtocut-offthresholdstodeterminetheoutcome:approvalor
rejection.
Agreatdealofpriorresearchhasbeenpublisheddetailingthecomparativeperformance
of various statistical and machine learning algorithms. Martin et al. (2024) compared a
widerangeofindividualandensemblealgorithmsforcreditscoring.Theyshowedthatthe
bestindividualperformerwasaGeneralisedAdditiveModelandthebestoverallperformer
was a Random Forest and K-Nearest Neighbour ensemble. Similarly, hybrid models have
performed well on public datasets such as German credit. Tripathi et al. (2020) used an
Extrememachinelearningapproach.Mahbobietal.(2023)foundthattheSupportVector
MachinealgorithmperformedbestunderaK-NearestNeighboursamplingapproach.
Weconsidermethodswhichhaverecentlybeenshowntooutperformotherapproachesin
creditriskmodellingresearchincludingRandomForest(RF),GradientBoostingMachine
(GBM),ArtificialNeuralNetworks,specificallytheMulti-LayerPerceptron(MLP),Decision
Trees(DTR)andSupportVectorMachine(SVM).Wecomparetheperformanceofthesefive
algorithmswiththatofthegoldstandardusedinindustry,LogisticRegression(LR),using
thestatisticalandcostperformancecriteriadiscussedinthenextsections.
Maincontributionsofthispaperare:
1. IntroducinganewFinancialPerformanceMetric(FPM)toestimatethetruecostsarising
frombothfalsepositivesandfalsenegatives;
2. Providinginsightsoncostdynamicsasaconsiderationinthemodelselection,andopti-
misingtheselectionbycombiningstatisticalmethodswiththedevelopedFPM;
3. EvaluatingthesuitabilityofapubliclyavailableGermanCreditDataset(GCD)forcredit
riskmodelling,andsimulatingimportantfinancialvariableswhichareoftennotavailable
inpublicdatasets;
4. ComparingtheproposedFPMwithanexistingmetric,creditscoringexampledependent
costmatrix(CSEDCM)metric,aswellascommonlyusedstatisticalcriteria;
5. Comparingcostdynamicsacrossfoursimulatedassetclassesobservedatlargebanksto
understandtheimpactofdefaultandopportunitycostacrossdifferentloanvalues;
6. ComparingtheperformanceofLogisticRegressionwithaselectionofhigh-performance
machine learning algorithms utilizing the commonly used statistical criteria and the
proposedFPM,anddeterminingwhichalgorithmoutperformsinestimatingcostsarising
frombothfalsepositivesandfalsenegatives.
The rest of the paper is organised as follows. First, we provide a brief introduction on
theresearchworkinSect.1.InSect.2,wepresentanoverviewofcommonlyusedstatistical
measuresofperformance.Section3presentsanoverviewoncostperformancemeasuresand
introducesanewapproach.InSect.4,themachinelearningmethodsusedareprovided.The
datasetandnumericalresultsaredescribedinSect.5.Thediscussion,conclusionandsome
futuredirectionareprovidedinSect.6.
123

AnnalsofOperationsResearch
2 Statisticalperformance
Traditionallythefocusincreditriskmodellingresearchhasbeentooptimisetheidentification
of true positives, that is, optimizing alignment between the prediction and observation of
default, with scant regard for ‘non-defaults’. Researchers and industry practitioners alike
havemainlyreliedontheuseofstatisticalmetricstomeasuremodelperformanceandselect
thestrongestmodel.
Conceptually,theunderlyinglogictothispracticeisthatbyselectingthemodelwiththe
strongestmetricsmodellerscanidentifythemodelwhichismostfitforpurpose.Inindustry
and academia alike, classical statistical performance criteria including the Area under the
ReceiverOperatingCurve(AUC),Accuracy(ACC)andSomers’Delta(Gini)areamongst
themostwidelyusedmodelmetricsreportedandusedformodelselection.
However,priorresearchhasidentifiedsomeproblematicfeaturesofAUC,ACCandGini,
whichsuggesttheirusecanleadtoincorrectconclusions(see,forexample,Verbrakenetal.,
2014).TheGinistatistichasalinearrelationshipwithAUC,yetbotharecommonlyreported
despite the obvious redundancy of reporting directly related performance metrics. Gini is
definedas
n(cid:2)+m(cid:3)(cid:4) (cid:5)
Gini =1− F m.BADk −F m.BADk−1
(cid:4)
k=2
(cid:5)(cid:6)
× F n.GOODk −F n.GOODk−1 ,
where F m.BADk (F n.GOODk ) is the kth vector value of the empirical distribution function
of bad (good) applicants, while m and n are the number of elements of the bad and good
distributions,respectively.Furtherdetailscanbefound,forexampleinThomasetal.(2002).
Hand(2009)statesthatGinimaynotbesuitableasameasureofperformanceofapplication
scorecardssinceit(aswellassomeothercommonlyusedmetricsincludingtheKolmogorov–
Smirnov (KS) statistic and Information Value (IV)) uses irrelevant information. It fails to
measureinformationonthebadrateamongacceptswhichistheaspectofperformancewe
areactuallyinterestedin.
The Receiver Operating Curve (ROC) is a graphical tool used to visualise the trade-
off between sensitivity and specificity, while the AUC is a scalar measure of aggregate
performance which summarises the ROC into a single value. In Anagnostopoulos et al.
(2019),theAUCiscriticisedforhowithandlesthetrade-offbetweenfalsepositivesandfalse
negativeswherebytherelativeseveritiesofmisclassificationsaretreateddifferentlybetween
differentclassifiers.Moreover,Marzban(2004)showedthatAUCdiscriminateswellbetween
‘good’and‘bad’models,butnotbetweengoodmodels.HandandAnagnostopoulos(2013)
dismissAUCasaportmanteaumeasure,equivalenttointegratingoverarangeofpossible
values,concludingthattheROCisanincoherentperformancemeasure.TheAUCisdefined
as
1
AUC = ×(Sensitivity+Specificity),
2
wheresensitivityistheTruePositiveRate(TPR)andspecificityistheTrueNegativeRate
(TNR),withSensitivity(TPR)=TruePositives/TotalPositives×100,whereasSpecificity
(TNR)=TrueNegatives/TotalNegatives×100.
Asstatedabove,thereisalinearrelationshipbetweenAUCandGini,andeachcanbe
easilycalculatedfromtheotherusingthefollowingequation,suggestingredundancyinthe
123

AnnalsofOperationsResearch
commonpracticeofpresentingbothmeasuresformodelevaluationand/orselection:
Gini +1
AUC = .
2
Ontheotherhand,ACCworksbyeffectivelysummingaccurateclassificationsasaproportion
ofallclassifications,whichisproblematicinscenarioscharacterisedbyseverelyimbalanced
target variables typical in credit modelling research. For example, for an observeddefault
rateof0.05amodelmaypredictall observationsasnon-defaults,yetstillreceiveanACC
of 0.95. While a common solution is to perform sampling to increase the minority class
representation. This rarely fully deals with the class imbalance bias in real-situations and
createsfurthercomplicationsdownstreamintermsofmodelmonitoring.TheACCisdefined
as
TP+TN
ACC = ,
TP+TN +FP+FN
whereTPisequaltoTruePositive,TNequalsTrueNegative,FPequalsFalsePositiveand
FNequalsFalseNegative.
3 Costperformance
Asdiscussedintheprevioussection,themostcommonlyusedstatisticalmetricshavesome
seriousdrawbackswhichraisesquestionsaroundtheirvalueinmodelselection,particularly
inrelationtocommercialapplicationssuchascreditrisk.Moreover,focusingonlyonthis
aspectofperformanceignoressomeveryimportantpracticalconsiderations.Inclassification
researchthecorrectselectionofperformancemetricsisoneofthemostimportantissuesin
evaluating a classifier’s performance (Liu et al., 2014). Indeed, a vast array of alternative
metricsareavailableandoptimizingthewrongmetricdirectlytranslatesintolostrevenue
(Dmitriev&Wu,2016).
Themostimportantobjectiveinbankingisprofit,andthereforeonceamodelhasbeen
determined as functional the comparative costs must be considered. Selecting the optimal
approach is not possible using standard classification metrics because they treat the costs
of misclassifications the same, which is not true in real credit risk management (see, for
example, Fiore et al., 2017). Credit risk is particularly well aligned to the use of profit-
basedorfinancialloss-relatedmeasures(Maldonadoetal.,2017),whichseektooptimisea
commercialoutcomeasopposedtoastatisticalmetric.
Costsensitivelearningseekstooptimisedecision-makingwheremisclassificationcosts
incur different penalties. While a valid application of cost sensitive learning can assume
thesamemisclassificationcost,Elkan(2001)suggestedthatamorerealisticproblemexists
wheremisclassificationcostsareexample-dependent,inthesensethatthecostsvaryamong
examplesandnotonlyamongclasses.Thisisparticularlysoforcreditrisk,wheremisclas-
sificationcostsvarybothwithinandbetweenresponseclasses.
Indeed,researchershavelongbeenawareoftheprofitmotiveasacentraldrivingfactor
inmodelselectionincreditriskyetonlyahandfulhavesoughttofindwaystoincorporate
this perspective into model selection. One of the biggest obstacles has been the dearth of
availabledatasetscontainingthenecessaryfinancialinformationtocompareperformanceon
cost(Aodha&Brostow,2013),leadingtoavarietyofapproachestoovercomethisshortfall.
Forexample,Xiaetal.(2017)simplyassumedthatthecostsofmisclassifyingadefaulting
borrowerarelargerthanthatofmisclassifyingagoodone.SchebeschandStecking(2005)
123

AnnalsofOperationsResearch
Table1 CSEDCMmodel,giveninEq.(1)
|                   |     | Actualpositiveyi |     | =1      | Actualnegativeyi | =0      |     |
| ----------------- | --- | ---------------- | --- | ------- | ---------------- | ------- | --- |
| Predictedpositive |     |                  |     | CTPi =0 | CFPi             | =ri +Ca |     |
FP
ci =1
| Predictednegative |     | CFNi | =Cli | ·LGD |     | CTPi =0 |     |
| ----------------- | --- | ---- | ---- | ---- | --- | ------- | --- |
ci =0
simplifiedthisproblembyassumingthatthemisclassificationcostsofabadborrowerasa
goodborrowerasfivetimesmorecostlythanmisclassificationofagoodborrowerasabad
borrower,yetwithoutdataneitherpaperwasabletoempiricallyevaluatethisassumption.
Other researchers with access to data containing financial performance variables have
constructedcostmetricsusingavarietyofdifferentapproaches.Forinstance,Zhangetal.
(2018)appliedtheMultipleInstanceLearningmethod,proposingacostsensitiveoptimiza-
tion approach which sought to minimise misclassification costs. In this work, instead of
quantifyingdifferencesinmisclassificationcosts,theauthorsweightedmisclassificationsby
similarityaccordingtodemographicfeaturesandtransactionalbehaviour.
3.1 Existingcostmetrics
Wangetal.(2021)proposedanapproachtoestimatecostsassociatedwithriskbasedpricing,
wherebysimilargroupsofexposureswereassignedincreasinglevelsofinterestrelativeto
theirriskinpeer-to-peerlending.Theyassignedacostmatrixtopooledrisksfordifferential
pricing,whichsoughttoassigndifferential misclassification costmatrices, withthelower
triangular C1 assigned the economic costs with a predicted ‘good defaulting’, and C2 the
additivecostofmisclassifyinganapplicanttothewrongpoolandtheopportunitycostof
lostbusiness.Nevertheless,theuncertaintyarisingfromnewbusinessinopportunitycosts
wasnotconsideredinthiswork.
Bycontrast,Bahnsenetal.(2015)andVerbrakenetal.(2014)bothsoughttoassignacost
matrixwithdifferentialcostsaccordingtoeachoutcome.Bahsenetal.(2015)f(cid:7)ocusedon
(x ,y )∈
misclassificationonly,(cid:8)wheretruepredictionswereassumedtocostnothing.Let
i i
Rn×R,i =1,...,N beasetofpredictor(explanatory)variablesxandresponse(indicator)
variable y.TheBahnsenetal.(2014,2015)creditscoringexampledependentcostmatrix
(CSEDCM)metricisgivenbelow:
|     |     | (cid:4) | (cid:5) | (cid:9) | (cid:10) |     |     |
| --- | --- | ------- | ------- | ------- | -------- | --- | --- |
∗)
|            | Cost | f(x | = y   | c C +(1−c | )C       |          |     |
| ---------- | ---- | --- | ----- | --------- | -------- | -------- | --- |
|            |      | i   | i     | i TP      | i FN     |          |     |
|            |      |     |       | (cid:9)   |          | (cid:10) |     |
|            |      |     | +(1−y | ) c C     | +(1−c )C | ,        | (1) |
|            |      |     |       | i i FP    | i        | TN       |     |
| , =1,...,N |      |     |       |           | ,C       | ,C ,C    |     |
wherec i i arepredictedlabels,andvaluesC TP TN FN FP indicatethe
costsoftruepositive,truenegative,falsenegative,andfalsepositive,respectively.Notethat
C =C =0asthetruepredictiondonotaccrueanymisclassicationcost.C shows
| TP TN |     |     |     |     |     | FN  |     |
| ----- | --- | --- | --- | --- | --- | --- | --- |
lossesifthecustomeri defaultstobeproportionaltohiscreditline,whereasC FP isminus
profitplustheexpectedlossifthecustomerdoesnotdefault.
Table 1 sets out the CSEDCM approach according to the four outcomes for a binary
classificationmodel.
123

AnnalsofOperationsResearch
Here,r isthelossinprofitbyrejectingwhatwouldhavebeenagoodcustomer,yetthis
i
value must be present valued. The term Ca is minus the profit of an average alternative
FP
customer (r¯) times the probability they will not default (π ), plus the average credit line
0
(C ¯ l) times Loss Given Default (LGD) times the probability they will default (π ), that is
1
Ca =−r¯·π +C ¯ l·LGD·π .
FP 0 1
Takingaslightlydifferentroute,Verbrakenetal.(2014)soughttoestimatecostscompared
to a model where all applicants are approved, that is where no credit scoring takes place.
Morespecifically,theyproposedtheExpectedMaximumProfit(EMP)modelassigninga
benefitincorrectlyidentifyingadefaulter,b ,whichisthefractionoftheloanamountwhich
0
islostafterdefaultas
LGD×EAD
b = ,
0
A
where EAD is Exposure at Default, and A is Principal Exposure. By contrast, the costs
associated with misclassifying a good applicant as a defaulter are equal to the Return on
Investment(ROI)oftheloan,definedasfollows:
rM
ROI = −1,
1−(1+r)−M
wherer istheInterestRate,andM isMaturity.
Further,Verbrakenetal.(2014)proposedthatLGDfollowsauniformdistribution,and
theEMPmetricisgivenbelow:
(cid:11)
1
EMP = P(T(θ);b ,ROI)×π F (t)−h(b )db ,
0 0 0 0 0
0
wheret isthedefinedcutoffthresholdvalue,T istheoptimalcutoffvalueunderthegiven
circumstances, θ is the cost-benefit ratio, π F (t) is a true positive case, h(b )db is the
0 0 0 0
probabilitydistributionassociatedwithcorrectlyidentifyingadefaulter,and
P(t;b ,ROI)=b ×π F (t)−ROI ×π F (t),
0 0 0 0 1 1
withπ F (t)indicatingafalsepositivecase.
1 1
3.2 Proposedfinancialperformancemetric
Inthissection,weintroduceamorerealisticestimateofthemisclassificationcostsarising
fromcreditrisk,thefinancialperformancemetric(FPM).WeformulatetheFPMbasedon
thepriorresearch,inparticularthecontributionsofBahnsenetal.(2015)andVerbrakenet
al. (2014).The FPMseeks to incorporate elements which have hitherto been omitted. We
summariseourapproachbelowandhighlightdifferenceswiththeexistingapproaches.
Loss estimation in credit risk has matured significantly thanks to advancesrequired by
regulatoryregimessuchasIFRS9,publishedin2014(IASB,2014).IFRS9wastheinterna-
tionalaccountingstandardboard’sresponsetothefinancialcrisis,aimedatimprovingthe
accounting and reporting of financial assets and liabilities (Gea-Carrasco, 2015). We note
thatwhilelostinterestissometimesrecognisedinsomeformulationsofrealisedLGD,we
haveseparatedoutthiscomponenttomakeitmoreexplicit.
WhileweagreethatLGDmustbeincorporatedintocostestimatestoobtainatrueviewof
thepotentialloss,Bahnsen’sCSEDCMmetricusesmaximumcreditlineinallestimatesof
losses,yetitisclearthatEADmustbeevaluatedsinceEADistheactualamountthelender
hasatrisk.Moreover,theCSEDCMapproachignorestheinterestlostfromadefaultwhich
123

AnnalsofOperationsResearch
isanimportantconsideration,notingtheprofitcomponentasakeymotivationforbeingin
thebusinessoflending.
Furthermore, in estimating the cost of a false positive, there is some debate on how
to incorporate the portfolio level uncertainty for the alternative customer (the cost of the
‘nextcustomer’whothemodeldeemsthecreditworthy).Wehavechosentoincorporatean
amendedversionoftheaverageexpectedlossfortheportfoliousingtheexpectedlossfor-
mula,asthesecostscanreasonablybeexpectedovertimeandhaveincorporatedameasureof
theuncertaintyoffutureprofits.Intheresultssectionwedescribeacomparisonbetweenthe
proposedapproachandtheCSEDCMapproachtodemonstratethemodelselectionimplica-
tions.
Similarly, Verbraken’s model presents some opportunity for refinement to improve the
estimationofexpectedcosts.Forexample,ROIcannotpossiblybeassimpleasmultiplying
theinterestrateagainsttheprinciplefortheloanterm.Thefactthatthereisadefaultrate
means that a proportion of the portfolio will never reach its contractually agreed maturity
term.Thusremainingmonthsonbookmustbeconsideredtoaccuratelyassessthetruevalue
lost.Whileaveragesaresometimesunavoidablewherespecificinformationisn’tavailable,
thegrossvalueofinterestrevenuelostfromamortgagecustomerwhodefaultsattwomonths
isvastlydifferentfromonewhodefaultsatthe320thmonth.Moreover,thefinancialprofiles
oftheunderlyingcustomerswhoformthesetwodisparatescenarioswillbeverydifferent.
Therefore,ignoringtheremainingmonthsonbookwouldsystematicallyunderpredictcosts
foridentifiablecustomergroups.
In addition, since credit decisions that result in default and opportunity costs (that is,
positiveandnegativemisclassifications)occursimultaneously,theyshouldbesummedrather
than subtracted. Finally, it is unrealistic to assume a starting position of the no credit risk
modelasevenpriortothewide-scaleadoptionofclassificationmodelsexpertjudgmentwas
usedtoscoreapplicants.
OurproposedFPMadvancescost-sensitivelearningasitappliestocreditscorecardsby
developingamorerealisticevaluationofthefinancialcostsarisingfromeachmisclassifica-
tion.Thesedifferencescanbepotentiallyhugewhenconsideredataportfoliolevelthatmight
comprisehundredsofthousandsofcustomers.Splittingcostsoneithersideofthedecision
boundaryalsoimpartspositivebenefits.Itprovidesthecapabilitytooptimisethethresholdby
minimisingcost.Anysystematicweaknessinachosenmodelcouldbeidentifiedandindeed
overcomebypotentiallyaddingvariablesoreven‘beefingup’thepredictivecapabilityby
combiningmodels.Thus,thecostofafalsenegative,misclassifyingabadcustomerasgood,
isequalto
(cid:2)N
FNC = P(yˆ <t | y =1)×LGD×EAD+PV(ROI ×RMOB),
i i
i=1
where y is the observed outcome (actual output), yˆ is the estimated outcome (modeled
i i
output),and P(yˆ < t | y = 1)arethefalsenegativecases,thefunction PV isapresent
i i
valuewhichdependson ROI and RMOB,with RMOB beingtheremainingmonthson
book, a measure of the number of months remaining on the repayment terms of the loan
agreement.
123

AnnalsofOperationsResearch
Ontheotherhandthecostofafalsepositive,misclassifyingagoodcustomerasbad,is
equalto
(cid:2)N
|     | = P(yˆ | >t | =0)×PV(ROI)−(ROI |     | +y¯×EAD×LGD), |     |
| --- | ------ | --------------------- | --- | ------------- | --- |
| FPC |        | i y i                 |     |               |     |
i=1
| P(yˆ  | > |     | = 0)arethefalsepositivecases, |     |                             |     |
| ----- | ------- | ----------------------------- | --- | --------------------------- | --- |
| where | i t y i |                               | ROI | istheaverageinterestrevenue |     |
fortheportfolio, y¯ istheaveragedefaultratefortheportfolio, y = (y ,...,y ), EAD is
|     |     |     |     |     | 1 N |
| --- | --- | --- | --- | --- | --- |
theaverageEADandLGDistheaverageLGD.
Notethatourproposedapproachallowsustosplitfalseestimatesaboveandbelowthe
decisionthresholdwhichprovidesadditionalinsightsonmodelperformance.Inaddition,it
considersbothintermsofmakingjudgementsonmodelselectionaswellastheoverallview.
TheproposedFinancialPerformanceMetric(FPM)forcalculatesthemisclassificationcost
by:
= FNC+FPC.
FPM (2)
4 Methodsused
Weutilisesixwidelyusedmachinelearningalgorithmsofvaryingcomplexityonapublicly
availabledataset(GCD)toevaluatewhichperformsbestaccordingtoourproposedFPM.
The methods compared include: Logistic Regression, Random Forest, Gradient Boosting
Machine,DecisionTrees,SupportVectorMachineandArtificialNeuralNetworkMultilayer
Perceptron.Next,wegiveabriefdescriptionofeachalgorithmandrefertothereferences
providedformoredetails.
4.1 Logisticregression
Logistic Regression (LR) is the gold standard in credit risk modelling in industry and is
typicallythebaselinemodelincreditscoringmodelcomparisonstudies(Yhip&Alaghe-
band, 2017). However, it has received criticism for its inability to detect non-linear or
non-monotonic relationships. The LR is an extension of linear regression, using a logit
functiontomakethedistancebetweentwobinarypointscontinuous.Thelogitfunctionisa
transformationbetweenthelinearmodelandtheprobabilityofthebinaryoutcome.TheLR
isformulatedas
|     |     | ln(p/1− p)=β | +β +....β | ,     |     |
| --- | --- | ------------ | --------- | ----- | --- |
|     |     |              | 0 1 x 1   | n x n |     |
pistheprobabilityoftheeventoccurring,β isthey-intercept,andβ , =1,...,n
| where                                      |     |     | 0   |     | i i |
| ------------------------------------------ | --- | --- | --- | --- | --- |
| arethecoefficientoftheindependentvariablex |     |     | i . |     |     |
4.2 Decisiontree
DecisionTrees(DTRs)utiliseaflowchartortree-likedecisionmakingapproachthatiseasily
visualisedfromlefttorightandiscomposedof“burst”nodessplitintodifferentpaths.The
threetypesofnodesincludeRootnodes,whichcompiletheentiresampleandarethendivided
123

AnnalsofOperationsResearch
intomultiplesets;Decisionnodes,whicharetypicallyrepresentedbysquares,representsub-
nodesthatdivergefurtherintofurtherpossibilities;andTerminalnodes,whichrepresentthe
outcomethatcannotbecategorizedfurther.Thetreestructureisbuiltfromthetopdownby
selectingthebestdecisionnodetosplitfirst,andthenafter,basedonMeasuresofentropy
andinformationgainareusedtoselectthebestdecisiontonodefirstandthensubsequent
decisions.Weightsarecalculatedforeachchancenodebyestimatingtheconditional(joint)
probabilities.DTRsandvariantsthereofhavebeenshowntobehighlyeffectiveforcredit
riskmodelling(Dumitrescuetal.,2022;Tianetal.,2020).DTRsareformulatedas
(X,y)=(x ,x ,x ,...x ,Y),
1 2 3 n
wherex ,x ,x ,...x aretheindependentvariables,andY isthetargetvariable.
1 2 3 n
4.3 Randomforests
RandomForest(RF)(Breiman,2001)isamorecomplexbaggingimplementationofDTRs.
ItgrowsandcombinesmultipleDTRstocreatea“forest”.TheRFhasdemonstratedsupe-
riormodelperformancewhenappliedtocreditmodellingresearch(Lessmanetal.,2015).
Formally,anRFisapredictorconsistingofacollectionofrandomisedbaseregressiontrees,
asgivenbelow:
r
n
(X,D
n
)= Eθ [r
n
(X,θ
m
,D
n
)],
where Eθ represents the expectation taken with respect to the random parameter θ, con-
ditioned on X and the dataset D . The parameters (θ ,θ ,...,θ ) are independent and
n 1 2 m
identically distributed (i.i.d.) realizations of the randomizing variable θ. Each tree is built
independently by randomizing over subsets of the data or features, and the final output
r (X,D )aggregatespredictionsacrosstheensemble.
n n
4.4 Gradientboostingmachine
GradientBoostingMachine(GBM)isanimplementationofboosting,aniterativetechnique
whichadjuststheweightofanobservationbasedonthelastclassification(Friedman,2001).
GBManditsvariantssuchasExtremeGradientBoostinghavealsoperformedstronglyinthe
comparativeclassificationliterature(Odegua,2020).ThemainideaofGBMistoaddnew
modelstotheensemblesequentially.Ateachparticulariteration,anewweak,base-learner
modelistrainedwithrespecttotheerrorofthewholeensemblesofar.Onecanarbitrarily
specifyboththelossfunctionandthebase-learnermodelsondemand.Thegeneralupdate
ruleinGBMcanbeexpressedas
F m (x)= F m−1 (x)+γ m h m (x), m =1,2,...,M,
wherewhere F (x)isthemodelpredictionaftermiterations(ortrees),and
m
(cid:2)n
F (x)=argmin L(y ,γ),
0 γ i
i=1
anddecisiontreeh (x)isfittedtotheresidualsby
m
h (x)≈r (m).
m i
123

AnnalsofOperationsResearch
Here,thepseudo-residualsiscomputedusing
(cid:12) (cid:13)
r (m) =−
∂L(y
i
,yˆ
i
(m−1))
,
i ∂yˆ(m−1)
i
wherey
istheactualclasslabelofthei-thdatapoint,yˆ(m)
isthepredictedprobabilityofthe
i i
i-thdatapointbelongingtothepositiveclassafterm iterations, x isthei-thinputfeature
i
vector,γ istheweightorlearningrateforthem-thtreeandcontrolsthestepsizeateach
m
iteration,andL isthelossfunction.
4.5 Supportvectormachine
SupportVectorMachines(SVMs)aresupervisedlearningmodelswhichworkbyconstructing
hyperplanesinamultidimensionalspacetoseparatescasesofdifferentclasslabels(Vapnik,
1996).Thesamplesthatlieonboundariesofdifferentclassesarereferredtoassupportvectors.
TheunderlyingprinciplebehindSVM-basedclassificationistomaximizethemarginbetween
thesupportvectorsusingkernelfunctions.SVMshaveachievedsuperiorperformanceinboth
retail(Obare&Muraya,2018)andnon-retailcreditriskassessment(Telesetal.,2021).The
SVMisformulatedas
(cid:2)P
f(x)= a K(x,x ),
i i
i=1
where P is the number of support vectors, a is an element of the parameter vector, x is
i i
a vector of regressors, K is a function referred to as the kernel and a is the number of
i
parameters. The kernel can be a Radial Basis Function, polynomial or a two-layer neural
network.
4.6 Multilayerperceptron
Multilayer Perceptron (MLP) is an Artificial Neural Network characterised by a back-
propagation algorithm which uses a special class of feedforward networks (Baum, 1988).
MLPhasmorethanonehiddenlayerandthenetworkmovesonlyintheforwarddirection,
with no loopback. These neural networks are good for both classification and prediction.
MLP has been successfully deployed in credit risk modelling research achieving superior
performance.MLPcomposesthefinaloutputfunctionofanetworkusing
f (x) = f (a (x)).
k k k
The function is applied to an input activation function consisting of a (x). The input fre-
k
quentlycomprisesacomputationoftheform
a(x) = Wh(x) + b,
wherexistheinputvector,bisthebiasvector,W istheweightmatrixandhistheactivation
functionoutput.Thefunctiona(x)takesavectorargumentandreturnsavectorasaresult,
notethata (x)isjustoneoftheelementsofa(x).
k
123

AnnalsofOperationsResearch
5 Datsetsandnumericalresults
Inthissection,wedescribeGCDandHomeCreditDataset(HCD),thesamplingprocedure,
thedatamodellingandthesimulationprocess.Thisisfollowedbypresentingtheresultsof
ournumericalexperiments.
5.1 Datasetandsampling
ThepubliclyavailableGermanCreditDataset(GCD)(Hofmann,1994)isusedinourexper-
iments.Itcontains1000observationsacross20predictorvariablesandaresponsevariable,
indicating goods (i.e. negatives) and bads (i.e. positives). Due to confidentiality which is
characteristicoffinancialdatamostresearchiscarriedoutusingpubliclyavailabledatasets
suchastheGCD,whichisamongthemostwidelyusedpublicdatasetsforcreditriskresearch
(see for examples, Beque et al., 2017; Due & Graff, 2019; Khashman, 2010; Dong et al.,
2010).
AccordingtoRamezanetal.(2021),thesizeofthetrainingdatasetisamajordetermi-
nantintheclassificationperformance.Theauthorscomparedtheerrorofpredictionacross
differentsamplesizesforavarietyofalgorithmsincludingRF,GBMandMLP.Theyfound
thatallthesealgorithmsachievedmorethan95%accuracywithatrainingsampleof625.
Alametal.(2010)developedanapproachforpowerestimationinLRtodeterminewhether
aparameterissignificantlydifferenttozero,combiningthepriorworkofWhittemore(1981)
andHsiehetal.(1998).Theirresultsshowthatasamplesizeof655isneededtoachievea
statisticalpowerof0.9630.
These studies suggest that using a training sample of at least 655 will achieve strong
accuracyformachinelearningmodelsandadequatestatisticalpowerformodelsincorporating
hypothesistestingasperLR.Thus,thetrainingsampleof712usedshouldbelargeenough
to minimise the error of prediction and to determine the real significance of one or more
parameters.
5.2 Modellingdata
Inthissection,wedescribemodellingtheGCD.Predictorsinthisdatainclude:•Statusof
existingcheckingaccount•Durationinmonth•Credithistory•Purpose•Creditamount•
Savingsaccount•Presentemploymentsince•Installmentrateinpercentageofdisposable
income•Personalstatusandsex•Otherdebtors•Presentresidencesince•Property•Age
inyears•Otherinstallmentplans•Housing•Numberofexistingcreditsatthisbank•Job
•Numberofdependents•Telephone•Foreignworker.
Priortomodelling,allpredictorvariablesaretransformedaccordingtotheWeightsofEvi-
dence(WoE)discretizationapproachwhichiswidelyusedinindustry.WhileLRistheonly
approachutilisedthatrequiresthemonotonicityprovidedbyWoEtransformation,discretiza-
tionwasperformedtoensurethatdataalignedtoindustrypracticeasmuchaspossible.Note
thatmakingexplanatoryvariableseitherstrictlyincreasingorstrictlydecreasing(i.e.mono-
tonic)isacriticalrequirementforscorecardmodels;asindicatorsforriskinesseachretained
variablemustbelinearlyrelatedtodefaultforfacevalidityincreditprovisionenvironments.
TheformulaforWoEdiscretizationisgivenbelow:
(cid:14) (cid:15)
%of y =0,wherex =i
WoE =ln .
xi %of y =1,wherex =i
123

AnnalsofOperationsResearch
Table2 Gammaparametersfor
Assetclass Shape Scale
simulatedEAD
CC 3 5000
SL 3 50,000
Mo 3 400,000
LL/SME 3 1,000,000
5.3 Simulationofdata
Next, we discuss the simulation of the GCD. Due to the lack of information necessary to
evaluatecostparameters,simulatedvariablesrepresentingfourdifferentassetclasseswere
incorporatedintotheGCD.Importantly,onlythe20originalpredictorsandthetargetdefault
variablewereaccessibletothemodel.Thisensuredthatallmodelsoperatedwithidentical
defaultclassinformationwithineachcondition,whethertrainingortesting.Thesimulated
variableswereusedexclusivelyforcostcalculations,whichinformedmodelselectiondeci-
sions.TobuildontheGCD,wesimulatedthekeymissingvariablesrequiredforcostanalysis
acrossthe1000observationsthatcomprisetheunderlyingdataset.
Furthermore,wesimulateEADvaluesaccordingtoaGammadistribution(see,forexam-
plesJimenez&Mencia,2007;Assadsolimani&Chetalova,2017)givenbelow:
za−1e −bz ba
f(z) = , z >0, a, b>0,
(cid:7)(a)
where(cid:7)(a)isthegammafunction,aistheshapeparameter,andbdenotestherateparameter.
WeusetheGammadistributiontosimulatefourdifferentEADrangesrepresentingtyp-
icalmagnitudesofexposureobservedinaselectionofdifferenteconomies.Ourreviewof
lendingstatisticsfromjurisdictionssuchasAustralia(AustralianBureauofStatistics,2024),
theUK(BankofEngland,2024),andtheUSA(Ostrowski,2024)revealedsignificantdis-
paritiesbothbetweenandwithintheseregions.Forinstance,intheUSA,averagemortgage
lending exposures in California are over three times higher than those in Indiana. Further
complicatinggeneralizationsacrossjurisdictionsarefactorssuchasvariationsinexposure
pricing, exchange rates, regulatory practices, and the risk appetites of individual lenders.
Toensurerepresentativeassetclasses,weselectedscale-appropriaterangesthatencompass
typicalportfoliosobservedinAustralia,theUK,andtheUSA.
The primary objective in evaluating these portfolios was to examine the influence of
modelmetrics,includingFPM,betweenportfoliosofvaryingsizes.Specifically,wesought
to determine whether larger interest payments influenced model selection decisions. The
simulated ranges across different portfolio scales provided meaningful differentiation to
supportthisanalysis.
By modelling different exposures according to a Credit Card (CC), Small Loan (SL),
Mortgage (Mo) and Large Loan/Small to Medium Enterprise Loan (LL/SME), we seek
to observe the impact of different default and opportunity cost ranges. This follows from
Lessmanetal.(2015)whofoundthattheimpactoffailingtoconsiderthebiastowardstrue
positiveswasmagnifiedthelargerthecostofafalsepositive.
Aftersettingtheseedtoensurevaluesarereproducible,EADdistributionsweresimulated
usingtheparametersgiveninTable2.
123

AnnalsofOperationsResearch
Table3 Descriptivestatisticsof
|     | Assetclass |     | Mean | Median |     | Standarddeviation |     |
| --- | ---------- | --- | ---- | ------ | --- | ----------------- | --- |
simulatedassets(GCD)
|     | CC  |     | $12,039  | $10,419  |     | $7134   |     |
| --- | --- | --- | -------- | -------- | --- | ------- | --- |
|     |     |     | $152,263 | $139,396 |     | $86,212 |     |
SL
|     | Mo  |     | $1,185,477 | $1,034,473 |     | $698,810   |     |
| --- | --- | --- | ---------- | ---------- | --- | ---------- | --- |
|     |     |     | $2,996,111 | $2,679,932 |     | $1,723,469 |     |
LL/SME
Table4 Observedcountsand
|     | Dataset |     | Good | Bad | Total |     | Default(%) |
| --- | ------- | --- | ---- | --- | ----- | --- | ---------- |
defaultrate(GCD)
|     | Training |     | 502 | 210 | 712 |     | 29.49 |
| --- | -------- | --- | --- | --- | --- | --- | ----- |
|     | Test     |     | 198 | 90  | 288 |     | 31.25 |
Theproportionof the loan alreadypaid (usedto calculate Loanprincipal) is simulated
accordingtoaBetadistribution,thatis:
1
| f(z) | =   | za−1(1−z)b−1, |     | 0≤z | ≤1, |     |     |
| ---- | --- | ------------- | --- | --- | --- | --- | --- |
β(a,b)
where β(a,b) is the beta function, a > 0 and b > 0 are shape parameters. The Beta
distributionwassimulatedwithbothshapeparametersequaltoone.Intheasymptoticsample
this translates to a roughly uniform distribution between zero and one with some random
variation.
Monthly payment (Pmt) amounts are calculated according to the payment equation
detailedinFinlay(2009)as
|     |     | × r/12 | ×(1 + | r/12)12t |     |     |     |
| --- | --- | ------ | ----- | -------- | --- | --- | --- |
P r
| Pmt | =   |     |            |     | ,   |     |     |
| --- | --- | --- | ---------- | --- | --- | --- | --- |
|     |     | (1  | + r/12)12t | −   |     |     |     |
1
where P =Principal,r=Annualinterestandt=Termoftheloaninyears.
r
Wealsokeeptheunderlyingdataasrealisticaspossibleaccordingtotheaforementioned
hypotheticalassetclasses,basingdistributionsonrealportfoliosobservedatAustralianand
Europeanbanks.Despitetheseefforts,somedifferencesarestillapparentinthedata.The
relativelyhighdefaultrateobservedintheGCDclearlysetsitapartfromdatasetsobservedin
industry.However,givenwell-knownconstraintswithclassificationmodellingitiscommon
practicetoperformsamplingoncreditriskdatasuchthattheminorityclass(iedefaults)is
markedly increased. Therefore, we can simply view the larger than normal minority class
asbeingtheresultofpriorsamplingtoaddresstheclassimbalance.InTable3,weprovide
descriptivestatisticsforthefoursimulatedassetclasses;CC,SL,MoandLL/SME.
InTable4,weprovidethesplitbetweenthetrainingandtestdatasets.Itincludescounts
of good (non-defaulting) and bad (defaulting) observations as well as the percent of each
outcome condition. Random sampling between the training and test datasets led to slight
variationsindefaultingproportions.Initialtestingrevealednosignificantdifferencesinresults
betweenequallysampledclassesandrandomlysampledones.Therefore,tomaintainrealistic
conditions,weoptedfortherandomlysampledapproach,whichiscommonlyusedinindustry
practices.
Afinalpotentialdeviationfromrealityrelatestothecreditcardassetclass,wherebyit
wastreatedlikeaone-offloanheldforasetnumberofmonths.Thisisnotrealisticsinceon
averagecreditcardcustomerstendtodrawdowncreditcontinuously,implyingthatwemay
123

AnnalsofOperationsResearch
Table5 DescriptivestatisticsofHomeCreditDataset(HCD)
Assetclass Mean Median Standarddeviation
Variousproducttypes $1,203,458 $1,069,602 $697,163
Table6 Observedcountsand
Dataset Good Bad Total Default(%)
defaultrate(HCD)
Training 197,910 17,448 215,258 8.10
Test 84,876 7377 92,253 7.99
haveunderrepresentedtheinterestwhichmightnormallybecollectedoverthelifeofthis
assetclass.
TofurtherdemonstratetherobustnessoftheproposedFPM,weappliedittotheHCDalso
usedinotherstudies,suchasWangetal.(2020).Thisdata,availableonKaggle(Montoya
etal.,2018),highlightsHomeCreditstrivestoexpandfinancialinclusionfortheunbanked
population, featuring a distinct loss structure unlike typical lending portfolios. Since the
HCD encompasses various lending products with different loss dynamics, this introduces
somenoiseintopredictions.However,itcontainsinformationsimilartotheGCD,covering
alargerdatasetof307,501rowsinthefullylabelledsubset.
Forthecomparisonpurpose,weanalysedasingleportfolioconsistingofvariousproduct
typesintheHCDratherthanmultiplesingleassetclasses,usingthesamesimulationapproach
aswiththeGCD.InTable5,weprovidedescriptivestatisticsforthenon-specificportfolio
fromtheHCD.
Table6displaysinformationonthecountsofgood(non-defaulting)andbad(defaulting)
observations,thepercentageofeachoutcomeconditionandtherateofdefaultinthetraining
andtestsplitsoftheHCD.
5.4 Implementation
Thefinaldecisionpriortomodellingwastoeitheroptimisethresholdsaccordingtospecific
modelswhichwouldhaveenhancedrealismyetreducedcomparability,ortoholdthethresh-
old constant at t = 0.5 to focus on the differential capabilities of each algorithm and the
performancemetrics;weoptedforthelatter.Furthermore,whilepreliminarymodeltuning
producedsomesmallincreasesinmodelstatisticalperformance,itcameatthecostofover-
fittingtothetrainingdataset.Thus,asallsixmodelsachievedacceptablystrongperformance
accordingtothestatisticalmetricsonlyminormodeltuningwasperformed.Statisticalmet-
rics were calculated first using automated outputs from R software and then recalculated
manuallyaccordingtotherelevantequations.
5.5 Results
Inthissection,wepresenttheresultsofournumericalexperiments.Westartbycomparing
theperformanceofourproposedcostmetricwiththatofthecommonlyusedapproachby
Bahnsen et al., and noting differences and similarities in model ranking between the two
approaches.
123

AnnalsofOperationsResearch
Table7 FalsepredictioncostsusingBahnsen’sapproach(CSEDCM)asapercentageofproposedcostmetric
(FPM),Eq.(3)
| Threshold(cost) | Methods | CC(%) | SL(%) | Mo(%) | LL/SME(%) |
| --------------- | ------- | ----- | ----- | ----- | --------- |
| Default         | MLP     | 1.04  | 7.67  | 7.10  | 8.09      |
|                 |         | 1.29  | 8.20  | 8.50  | 11.34     |
| Default         | DTR     |       |       |       |           |
| Default         | GBM     | 1.02  | 7.05  | 7.63  | 9.14      |
|                 |         | 1.21  | 9.77  | 7.20  | 10.76     |
| Default         | LR      |       |       |       |           |
| Default         | RF      | 1.20  | 8.98  | 8.21  | 13.87     |
|                 |         | 1.28  | 5.74  | 11.22 | 15.51     |
| Default         | SVM     |       |       |       |           |
| Opportunity     | MLP     | 30.72 | 43.43 | 38.09 | 40.50     |
| Opportunity     | DTR     | 41.15 | 43.50 | 33.34 | 35.01     |
| Opportunity     | GBM     | 25.56 | 45.47 | 31.16 | 38.96     |
| Opportunity     | LR      | 30.91 | 49.62 | 44.61 | 46.39     |
|                 |         | 31.74 | 44.61 | 39.45 | 22.33     |
| Opportunity     | RF      |       |       |       |           |
| Opportunity     | SVM     | 29.88 | 14.06 | 29.94 | 45.09     |
|                 |         | 17.30 | 33.63 | 29.61 | 30.87     |
| Overall         | MLP     |       |       |       |           |
| Overall         | DTR     | 19.26 | 27.54 | 21.59 | 24.11     |
| Overall         | GBM     | 13.48 | 33.08 | 22.40 | 27.65     |
| Overall         | LR      | 13.62 | 35.54 | 30.01 | 32.63     |
| Overall         | RF      | 11.70 | 26.39 | 22.56 | 17.21     |
|                 |         | 21.51 | 10.95 | 24.61 | 39.91     |
| Overall         | SVM     |       |       |       |           |
We calculated the cost of false predictions using both the proposed FPM and that put
forwardbytheCSEDCM.NotingthatallofCSEDCM’scostestimatesweresmallerthan
theFPM,wethencalculatedthepercentageforeachmodelandthresholdpositionusingthe
followingequation:
CSEDCM
|     | Cost%= |     | ×100. |     |     |
| --- | ------ | --- | ----- | --- | --- |
(3)
FPM
InTable7,wereporttheresultsobtainedusingthisequation.Thefirsttwocolumnsin
this table are the cost types and the six algorithms used in our comparison, and the last
four columns are the simulated asset classes. The results show that Bahnsen’s approach
routinelyunderestimatesthetruecostsoffalsepredictions,withunderpredictionsometimes
asdifferentasonehundredthoftheproposedFPM.Forexample,inestimatingthedefault
costoffalsepredictionfortheGBM,Bahnsen’sestimatewasjust1.02%oftheFPM.
The huge disparity in false prediction costs drastically increases the likelihood for
inadvertentlyselectingthewrongmodelunderthebeliefitpresentsthelowestcostofmisclas-
sification.We’vefurtherenhancedthemodelselectionprocessbydemonstratingperformance
measurementdifferentialsoneithersidesofthedecisionboundary,whereasmostindustry
practitionersaswellasresearchersconsideronlytheoverallview,andthatisusuallydone
comparing averaged statistical metrics such as Gini and AUC. Based on the cost of false
predictionestimatedbytheCSEDCMcomparedtothecostoffalsepredictionestimatedby
theFPMfromthistable,wewillutiliseourproposedcostmetricFPMforfurtheranalysis.
IftheproposedFPMisutilizedtoestimatethecostoffalseprediction(theresultspresented
in Table 8), the MLP demonstrates the lowest misclassification costs across all four asset
classes(CC,$17.4m;SL,$42.2m;Mo,$260.7m;LL/SME,$488.7m),andisthereforethe
123

AnnalsofOperationsResearch
bestperformingmodel.Bycontrast,iftheCSEDCMwasusedformodelselection,theRF
wouldbeselectedfortheCC($2.6m)andLL/SME($91.8m)assetclassesandtheSVMfor
smallloans($5.1m)andDTRformortgages($72.1m).Interestingly,whenwepeelbackthe
covertoexamineperformanceoneithersideofthedecisionboundary,bothcostapproaches
favortheMLPfordefaultcost,andRFperformsbestforopportunitycost,yettheconsiderable
differencesinthemagnitudeoffalsepredictioncostsresultindifferencesattheaggregate
level across the decision boundary, which is the level at which the CSEDCM approach
operatesat.
Now,wediscussthecomparisonbetweeneachrespectivemethodaccordingtothefinancial
cost of losses calculated on false predictions. The losses associated with false negatives
(applicantsthemodelpredictsasgoodbutwholaterdefault;thedefaultcost),aswellasfalse
positives(applicantsthemodelpredictsasbadyetwhodonotdefault;theopportunitycostand
mostlycomprisetheinterestrevenueforegonebyrejectinganotherwisegoodapplicant),are
included.Separatingobservationsintofalsepositivesversusfalsenegativesrequiredsplitting
thesampleaboveandbelowthethresholdwhichenhancedcomparisonswiththestatistical
metrics.
Thecomparisonresults,thecostsassociatedwithindividualcomponentsandtheoverall
FPM,areprovidedinTable8.The‘Above’columnrepresentsfalsepositivemisclassifica-
tioncosts,incurredwhenthemodelincorrectlyclassifiesindividualsasdefaulterswhodid
not default. The ‘Below’ column captures false negative misclassification costs, summing
the losses from applicants classified as low risk but who ultimately defaulted. Finally, the
‘Overall’columnrepresentsthetotalmisclassificationcosts,combiningbothfalsepositives
andfalsenegatives,comprisingtheproposedmetric.
Next, we provide the results of the classical statistical performance metrics in Table 9,
wherethefirsttwocolumnsshowthesixmethodsusedandthethresholdsplit,andthelast
threecolumnsarethestatisticalmetrics.Typicallytheseareonlypresentedattheoveralllevel,
which is effectively an average across all observations, however we additionally estimate
performancemeasuresaboveandbelowthethreshold.Splittingtheperformancemetricsin
thismannerprovidesfurtherinsightintoeachmethodandhowtheyperformoneitherside
ofthedecisionthresholdaswellasthemeasurementsthemselves.
TheresultsfromTable9showthatwhenwerankeachalgorithmbystatisticalperformance
seeking to identify the best method, we see that the method rankings are very different
comparingeithersideofthethresholdwithoverall.Forexample,GinishowsthattheGBM
performedbestabovethethresholdwhiletheLRwassuperiorbelow,yetitwastheMLP
thatcameoutontopaccordingtothismetric.
Further, the Gini and AUC result in identical rankings, reinforcing the notion that the
practiseofpresentingbothmetricstogetherisredundant.Bycontrast,theaccuracyofmethods
almostalwaysranksmethodsdifferentlytoGini/AUC,reflectingthedifferentphilosophyin
takingtheproportionoftruepredictionsfromallpredictions,versusdiscriminatingbetween
goodsandbadsusingthenumberofconcordantpairs.
The routine use of these statistical metrics in isolation is problematic because as has
already been established, while they may be useful in distinguishing between a good and
a bad model, they are not useful for making selections between good models. Moreover,
theydonotprovideinsightontherealparameterofinterestwhichisminimisingthefalse
predictions,inparticulartheircostinacreditscoringenvironment.Furthermore,‘overall’
estimateseffectivelyaverageacrossthedecisionboundarythusobscuringimportantdetails
ofmodelperformance.
Wenotethatwhenusedinthetraditionalmannerassessingstatisticalperformanceoverall,
theMLPwastheclearwinneroverall,yetonlymarginallystrongerthantheLR.Themarginal
123

AnnalsofOperationsResearch
Table8 Financialcostmetrics
|     | Method Assets | Above | Below | Overall |
| --- | ------------- | ----- | ----- | ------- |
(per$1000)bymethods,asset
| classandthresholdusingtest | DTR CC | $11,233 | $13,686 | $24,919 |
| -------------------------- | ------ | ------- | ------- | ------- |
dataset(GCD)
|     |     | $10,656 | $10,335 | $20,991 |
| --- | --- | ------- | ------- | ------- |
GBM CC
|     | LR CC | $8134 | $11,337 | $19,471 |
| --- | ----- | ----- | ------- | ------- |
$17,423
|     | MLP CC | $9541   | $7882   |         |
| --- | ------ | ------- | ------- | ------- |
|     | RF CC  | $7749   | $14,784 | $22,533 |
|     | SVM CC | $13,662 | $5652   | $19,314 |
|     |        | $30,664 | $25,311 | $55,975 |
DTR SL
|     | GBM SL | $38,119 | $18,163 | $56,283 |
| --- | ------ | ------- | ------- | ------- |
|     |        | $29,245 | $15,973 | $45,218 |
LR SL
|     | MLP SL | $30,607 | $11,557 | $42,164 |
| --- | ------ | ------- | ------- | ------- |
|     |        | $25,031 | $26,199 | $51,230 |
RF SL
|     | SVM SL | $29,145  | $17,368  | $46,513  |
| --- | ------ | -------- | -------- | -------- |
|     | DTR Mo | $176,080 | $158,013 | $334,093 |
|     | GBM Mo | $204,541 | $121,299 | $325,840 |
|     | LR Mo  | $180,241 | $115,443 | $295,684 |
|     |        | $189,427 | $71,316  | $260,743 |
MLP Mo
|     | RF Mo | $155,153 | $182,587 | $337,741 |
| --- | ----- | -------- | -------- | -------- |
|     |       | $242,131 | $96,377  | $338,508 |
SVM Mo
|     | DTR LL/SME | $314,838 | $268,673 | $583,511 |
| --- | ---------- | -------- | -------- | -------- |
|     |            | $402,095 | $245,552 | $647,647 |
GBM LL/SME
|     | LR LL/SME  | $324,782 | $204,305 | $529,087 |
| --- | ---------- | -------- | -------- | -------- |
|     | MLP LL/SME | $343,546 | $145,248 | $488,795 |
|     | RF LL/SME  | $210,919 | $322,532 | $533,451 |
|     | SVM LL/SME | $537,818 | $114,113 | $651,931 |
statisticalimprovementobtainedfromtheMLPwouldusuallybediscardedinfavourofthe
simplerandmoreeasilyimplementedandunderstoodLR.Indeed,whenusedinconjunction
withtheFPM,thetruecostofselectiondecisionscanbeeasilyunderstood.
In addition, the differential performance on either side of the threshold provides some
insightintohoweachalgorithmworks,and,whereeachperformsstrongest.Forinstance,it
isnotablethataccordingtoACCtheSVMperformedamongstthebestbelowthethreshold,
yet it was also the worst above the threshold. The observed variation in method ranking
betweenmodelmetricsunderscoresthenotionthatusingtraditionalperformancemeasures
blindlyresultsinsuboptimalmethodselections.Certainlyaveragingmetricsacrossthedeci-
sionboundaryobscuresimportantdetailsonperformance.Thus,thetraditionalperformance
measurespresentchallengesformethodselectionandmustbeusedwithcaution.
Fromtheresults,anotableobservationsupportsthefindingsbyVerbrakenetal.(2015),
whereby the larger the magnitude of the principal loan amount, the more important that
opportunity costs become. Given the scale of the largest asset class we simulated and the
consequentmagnitudeofinterestrevenuethatwouldbelost,ourfindingsshowthatforthese
dataopportunitycostsarelargerthandefaultcosts.Thedisparitybetweenopportunityand
defaultcostislargestwheretheinitialexposureissmallest,inthecreditcardassetclass,and
diminishesastheaveragesizeoftheassetclassincreases.Thissuggeststhatthelargerthe
123

AnnalsofOperationsResearch
Table9 Statisticalmetricsby
|     | Method | Threshold | Gini ACC | AUC |
| --- | ------ | --------- | -------- | --- |
thresholdandmethodsusingtest
| dataset(GCD) | MLP | Above   | 0.3273 0.7835 | 0.6636 |
| ------------ | --- | ------- | ------------- | ------ |
|              |     |         | 0.3906 0.7619 | 0.6953 |
|              | DTR | Above   |               |        |
|              | GBM | Above   | 0.4131 0.7553 | 0.7065 |
|              |     |         | 0.3681 0.8046 | 0.684  |
|              | LR  | Above   |               |        |
|              | RF  | Above   | 0.3279 0.7922 | 0.6639 |
|              | SVM | Above   | 0.3628 0.71   | 0.6814 |
|              |     |         | 0.8358 0.9319 | 0.9179 |
|              | MLP | Below   |               |        |
|              | DTR | Below   | 0.8224 0.8725 | 0.9112 |
|              |     |         | 0.8224 0.8969 | 0.9112 |
|              | GBM | Below   |               |        |
|              | LR  | Below   | 0.8558 0.9005 | 0.9279 |
|              |     |         | 0.8014 0.8863 | 0.9007 |
|              | RF  | Below   |               |        |
|              | SVM | Below   | 0.7682 0.9198 | 0.8841 |
|              | MLP | Overall | 0.8914 0.8819 | 0.9457 |
|              | DTR | Overall | 0.8517 0.8403 | 0.9259 |
|              | GBM | Overall | 0.8561 0.8507 | 0.9281 |
|              |     |         | 0.8903 0.8715 | 0.9452 |
|              | LR  | Overall |               |        |
|              | RF  | Overall | 0.8523 0.8611 | 0.9262 |
|              |     |         | 0.8392 0.8467 | 0.9196 |
|              | SVM | Overall |               |        |
creditcontract,themorecarefullendersmustbetoavoidmisclassifyingagoodcreditrisk
asbad.
However,thisisinalimitedsampleof1000customers,whereasinarealcreditportfo-
lio products like CC and SL customers may number in their millions. While our findings
supportthenotionthatopportunitycostsbecomeincreasinglyimportantthelargertheprin-
ciple.However,giventhevolumeoflowvaluelendingproductslikeCCthismaynothold,
particularlyinunsecuredlendinginwhichtheLGDtendstobesignificantlyhigher.
From a method selection perspective, the algorithm resulting in the smallest loss was
thewinner,inlinewiththeprofit-basedmotivewhichcharacterisescommercialenterprise.
Results show that the RF posed the lowest misclassification cost across all asset classes
relatedtofalsepositives,thatisforapplicantsthatthemodelhasscoredabovethedecision
thresholdwhodonotdefault.Bycontrast,theSVMposedthelowestmisclassificationcosts
fortwoassetclasses(CCandLL).TheMLPmisclassificationcostwaslowestforSLand
Moforapplicantswhothemethodapproves,thatisapplicantswhoscorebelowthedecision
threshold,yetwholaterdefault.Overall,theMLPperformedthebestacrossallfourasset
classes.
We conclude by discussing the power curve that is used to empirically determine the
statisticalpowerinourtrainingsample.Moreprecisely,thecurveisproducedtodetermine
whethertheGCDprovidesadequatestatisticalpowerwithwhichtomakeinferencesabout
modelperformance.Whilehypothesistestingisonlyafeatureofstatisticalmodelling,and
therefore,onlyrelatestotheLRalgorithm,itisinstructiveforcomparisonpurposeswiththe
othermethodsinvestigated.Notethatthestatisticalpowerwascalculatedusingtwoassumed
target variable probabilities, the required inputs for this calculation. However, under both
probabilityassumptions,thestatisticalpowerapproached100%priortothetrainingsample
reaching700.Thus,thepowercurvedemonstratesthatthetrainingsampleselectedatrandom
123

AnnalsofOperationsResearch
Fig.1 Samplesizepowercurveforclassification
from the GCD was sufficiently large to provide adequate statistical power with which to
estimateoneormoreparametersusingLR.Figure1depictstheresultsofthepoweranalysis.
Furthermore,asmachinelearningalgorithmsdonotformallyperformhypothesistesting
asstatisticalmodelsdo,truepoweranalysisisnotpossible.Instead,wecalculatetheerror
ofpredictionoverarangeoftrainingsamplesizestotestwhetherthesamplesizeusedwas
largeenough.Thedeterminationoftheadequacyofthesizewasmadebyobservingwhether
theerrorratewasstilldecliningasthetrainingsamplegrew,orwhetheritflattenedout.Each
modelwastestedoneachofninetrainingsamplesextractedfromtheGCDranginginsize
from100to900.Aftereachsubsetwasextractedtoformthetrainingdata,theremaining
proportioncomprisedthetestdata.Thus,wherethetrainingdatasetwas100,thetestdataset
was900;wherethetrainingdatasetwas200,thetestdatasetwas800,andsoonuntilthe
maximum split whereby the training dataset was 900 and the test dataset was 100. The
samplesizeversuserrorratechartsforallsixmethodsareshowninFigs.2,3,4,5,6and7,
respectively.NotethatinFig.1,thepowergreaterthan0.8isgenerallyconsideredacceptable,
whileforFigs.2,3,4,5,6and7thelowertheerrorratethebetterqualitythemethod.
Inearlymethodtesting,modeltuningappearedtoimprovethefittothetrainingdataset
yetreducedperformanceonthetestdata.Thus,tominimiseoverfittingtothetrainingdataset
onlybasicmodeltuningwasperformed.Thesamplesizebyerrorplotsforeachrespective
modelrevealsthatthetrainingandtestdatasetsachievedsimilarperformanceirrespective
ofsamplesize,withonlythesmallesttrainingsamplesizeof100(test=900)resultingina
maximumerrorofpredictionapproaching0.2.
ThetwomethodswhichshowedelevatederrorratesweretheGBMandtheSVM.Contrary
totheconvergingperformancebetweentrainingandtestdatasetsobservedfortheotherfour
methods,theerrorofpredictionforthesemethodsweresubstantiallylargerforthetestdataset
irrespectiveofitsrelativesizeincomparisontothetrainingdata.Forexample,fortheGBM
there is at least a 10% difference in performance even when the training data was at its
maximumof900.
Whileperformanceneverconvergesacrossanysamplesizeitisnoteworthythattheerror
rateinthetestdataisgenerallydecliningforboththeGBMandtheSVMasthesizeofthe
123

AnnalsofOperationsResearch
Fig.2 LRsamplesizeversuserrorrate
Fig.3 RFsamplesizeversuserrorrate
trainingdatasetincreases,andrelativelyflatfortheotherfourmethods.Whileperformance
may have continued to improve if the training sample was even larger, it implies that the
GBMandtheSVMmayrequirelargertrainingdatasetstocontroltheerrorintestdata.An
alternativeinterpretationisthattheGBMandtheSVMformulationsdidnotgeneraliseto
thisspecificdatasetaswellastheotheralgorithms.
Similar levels of the performance for both test and training datasets were observed for
LR,RF,MLPandDTR,yetfortheGBMtheactualmagnitudeofdifferenceinerrorwas
onlyaround0.1bythetimetrainingdatawasaround700,androughly0.06fortheSVM.
Takentogethertheseresultssupportthenotionthatthetrainingdatasetwassufficientlylarge
toproducereliableresultsforallalgorithmstested.
123

AnnalsofOperationsResearch
Fig.4 GBMsamplesizeversuserrorrate
Fig.5 MLPsamplesizeversuserrorrate
Asmentionedearlier,weusedtheHCDwithasingleportfolioofvariousproducttypes
tofurtherdemonstratetherobustnessoftheFPM.
Table10presentsmodelperformanceontheHCDincludingastatisticalaccuracymetric
andthedifferencefromtheLRalgorithmforreference.Usingaclassicalstatisticalperfor-
manceapproach,SVMwouldtypicallybechosen.However,theaccuracydifferencesamong
the six algorithms are trivial. In contrast, the financial losses from false predictions in the
FPMrevealssignificantdifferencesacrossalgorithms.Thisisconsistentwiththeobserva-
tionsfortheGCD.TheFPMidentifiedRFasthebest-performingmodel,closelyfollowedby
theMLP.TheresultsalsoindicatethatutilizingtheFPMwouldachieveasignificantsaving
ofapproximately$321millionand$297millionovertheLR,respectively.
123

AnnalsofOperationsResearch
Fig.6 DTRsamplesizeversuserrorrate
Fig.7 SVMsamplesizeversuserrorrate
Table10 Financialcostmetrics(per$1000)bymethodsusingtestdatasetHCD
| Method | Accuracy | Above    | Below    | Overall  | DifferfromLR |
| ------ | -------- | -------- | -------- | -------- | ------------ |
| DTR    | 0.9197   | $353,830 | $635,740 | $989,570 | −$198,240    |
−$17,970
| GBM | 0.9201 | $310,680 | $498,620 | $809,300 |          |
| --- | ------ | -------- | -------- | -------- | -------- |
| LR  | 0.9200 | $318,150 | $473,180 | $791,330 | –        |
| MLP | 0.9200 | $204,900 | $289,330 | $494,230 | $297,100 |
| RF  | 0.9200 | $138,990 | $330,380 | $469,370 | $321,960 |
| SVM | 0.9155 | $185,810 | $316,250 | $502,060 | $289,270 |
123

AnnalsofOperationsResearch
6 Discussionandconclusion
In this section, we provide discussion on the results presented in this paper and conclude
withfutureresearchdirections.
Publiclyavailabledatasetsenableindustrypractitionerstoemulatetheresultsachieved
inpublishedliteraturemoreeasily,thusexpeditingtheuptakeofnewresearch.Thisstudy
showsthatevenrelativelysmall,publiclyavailabledatasetsliketheGCDandtheHCDare
not only large enough to provide sufficient statistical power with which to train statistical
modelsbutalsotominimisetheerrorofpredictionarisingfromtheapplicationofmachine
learningalgorithmsontrainingsamplesanywhereabove100observations.
Moreover,wedemonstratedthatwherenecessaryfinancialinformationisnotavailable,it
canbesimulatedtoprovideinsightsoncostdynamicsasaconsiderationinmodelselection
particularlywherethesearecalibratedtoreallendingportfolios.Whileourcostdynamicsare
estimatedonsimulateddata,theresultsfromtestsonstatisticalpoweranderrorofprediction
show that these samples are sufficiently large to avoid sampling bias and therefore, make
inferencesonfinanciallosses.
Furthermore, by splitting results on either side of the decision threshold, we showed
howmodelperformancediffersaccordingtowhichalgorithmhasbeenused,thusproviding
additionalinsightsintoalgorithmselectionandperformancemetricsalike.Themodelranking
accordingtotheclassicalperformancemetricsvariedgreatlywhensplitinthismanner.
Thepresentstudyhasfocusedonindividualalgorithms.However,asmodelperformance
andrankingwerehighlyvariableoneithersideofthedecisionboundary,astackingapproach
maywelloutperformsinglealgorithms.Bycombiningthestrengthsofalgorithmsoneither
sideofthethresholditmaybepossibletoeliminateoratleastmitigatetheirweaknessesto
developastrongeroverallpredictionsystem.
Inaddition,buildingonpreviousresearch,wehavesoughttoproposethemostrealistic
estimatesoffalsepredictioncostsyet.Althoughweutilisedrelativelysmalldatasetsoffew
observations,theproposedFPMcouldbeextendedandappliedtolargerlendingportfolios
whichcouldpotentiallyprovideasignificantfinancialbenefittoorganizations.
Taking the example of the mortgage asset class, the best performing algorithm overall
was,forexample,theMLPintheGCD,andselectingthatoverthenextbestalgorithm(LR)
resultedinabenefitofapproximately35milliononadatasetof<300applicants.Whilethis
is a large enough difference to be meaningful in selecting the most fit-for-purpose model,
areal-lifemortgageportfoliocouldeasilybeathousandtimeslarger.Applyingtheratioof
1:1000putsthevalueofselectingMLPoverLRat$35Billion,amassivefinancialbenefit
foreventhelargestcorporationstradingonaglobalscale.
Furthermore,wehavenotedtheextantissueswiththethreemostpopularperformance
metrics, AUC, Gini, and ACC. Prior research suggests these measures are unsuitable for
modelselection.Forexample,althoughAUCmaybeabletodifferentiateagoodmodelfrom
abadoneitisunabletodistinguishbetweengoodones.Whileitiscoherentatseparatingclass
membership,itisalsoincoherentonthecostsofthoseclasses,andtheactuallossresulting
from false predictions. Although these incoherent approaches may be useful as a hurdle
todifferentiatebetweengoodandbadcandidatemodels,thefinanciallossshouldbeused
foridentifyingthebestperformer.Therefore,weproposeanoptimalsystemwherebyonce
candidate models achieve a minimum performance threshold, the financial loss measures
shouldbeusedtoselectthebest-performingmodel.
UsingtheproposedFinancialPerformanceMetric(FPM)enablesindustrypractitioners
toselectmodelswhichbestalignwiththeirmotivesforusingthemodelsinthefirstplacefor
123

AnnalsofOperationsResearch
profit.Asitisdemonstratedhereinforcreditscorecards,thesameprinciplescanbeapplied
to any commercial application of classification models in which the loss function is more
nuancedthansimplyseparatinggoodsandbads.
Mostofthepublishedcreditmodellingresearchfocusesonapplicationscorecards,never-
theless,theyarenotthemostmaterialmodelsusedbybanksglobally.Futureresearchshould
deeplyexaminebehavioralmodelswhichmeasuretheongoingriskonceapplicantsbecome
customers.Bothpointintime,aswellasthroughtheeconomiccyclemodelsareimportant
considerationsrequiredbyprudentialauthorities.Thesemodelshaveahugeimpactonnot
onlyretainedsolvencycapital,butalsotheoverallhealthofthefinancialsystem.Wetested
ourfindingsonacomparisondataset,butfurthertestingincludingreplacingsimulatedvari-
ableswithreal-timemeasurementsmayservetounderscorethevalueofusingthefinancial
performance metric. Lastly, there is a dearth of published research on optimal monitoring
solutionsforcreditmodelsovertime,whichisanurgentpriorityforindustry.
Funding OpenAccessfundingenabledandorganizedbyCAULanditsMemberInstitutionsThisresearch
receivednoexternalfunding.
Declarations
Conflictofinterest Theauthorsdeclarethattheyhavenoknowncompetingfinancialinterestsorpersonal
relationshipsthatcouldhaveappearedtoinfluencetheworkreportedinthispaper.
Ethicalapproval Thisarticledoesnotcontainanystudieswithhumanparticipantsoranimalsperformedby
anyoftheauthors.
OpenAccess ThisarticleislicensedunderaCreativeCommonsAttribution4.0InternationalLicense,which
permitsuse,sharing,adaptation,distributionandreproductioninanymediumorformat,aslongasyougive
appropriatecredittotheoriginalauthor(s)andthesource,providealinktotheCreativeCommonslicence,
andindicateifchangesweremade.Theimagesorotherthirdpartymaterialinthisarticleareincludedinthe
article’sCreativeCommonslicence,unlessindicatedotherwiseinacreditlinetothematerial.Ifmaterialis
notincludedinthearticle’sCreativeCommonslicenceandyourintendeduseisnotpermittedbystatutory
regulationorexceedsthepermitteduse,youwillneedtoobtainpermissiondirectlyfromthecopyrightholder.
Toviewacopyofthislicence,visithttp://creativecommons.org/licenses/by/4.0/.
References
Aodha,O.M.,&Brostow,G.J.(2013).Revisitingexampledependentcostsensitivelearningwithdecision
trees.In2013IEEEinternationalconferenceoncomputervision(pp.193–200).Washington,DC,USA.
Assadsolimani,M.&Chetalova,D.(2017).EstimatingVaRincreditrisk:Aggregatevssinglelossdistribution.
AustralianBureauofStatistics.(September2024).LendingIndicators,ABSWebsite.Accessed10December
2024.
Bahnsen,A.C.,Aouada,D.,&Ottersten,B.(2014).Example-dependentcost-sensitivelogisticregressionfor
creditscoring.In13thinternationalconferenceonmachinelearningandapplications(pp.263–269).
https://doi.org/10.1109/ICMLA.2014.48
Bahnsen,A.C.,Aouada,D.,&Ottersten,B.(2015).Example-dependentcost-sensitivedecisiontrees.Expert
SystemswithApplications,42(19),6609–6619.https://doi.org/10.1016/j.eswa.2015.04.042
BankofEngland.(November2024).MoneyandLending,BankofEnglandwebsite.Accessed10December
2024.
Banu,I.M.(2013).Theimpactofcreditoneconomicgrowthintheglobalcrisiscontext.ProcediaEconomics
andFinance,6,25–30.
Baum,E.(1988).Onthecapacityofmultilayerperceptron.JournalofComplexity,4,193–215.
Bequé,A.,Coussement,K.,Gayler,R.,&Lessmann,S.(2017).Approachesforcreditscorecardcalibration:
Anempiricalanalysis.Knowledge-BasedSystems,134,213–227.
Breiman,L.(2001).Randomforests.MachineLearning,45,5–32.https://doi.org/10.1023/A:1010933404324
123

AnnalsofOperationsResearch
Cantrell,B.W.,McInnis,J.M.,&Yust,C.G.(2014).Predictingcreditlosses:Loanfairvaluesversushistorical
costs.TheAccountingReview,89(1),147–176.https://doi.org/10.2308/accr-50593
Dmitriev,P.,&Wu,X.(2016).Measuringmetrics.InProceedingsofthe25thACMinternationalonconference
oninformationandknowledgemanagement(CIKM’16).AssociationforComputingMachinery,New
York,NY,USA(pp.429–437).https://doi.org/10.1145/2983323.2983356
Dong,G.,Lai,K.K.,&Yen,J.(2010).Creditscorecardbasedonlogisticregressionwithrandomcoefficients.
ProcediaComputerScience,1(1),2463–2468.
Dua,D.,&Graff,C.(2019).UCImachinelearningrepository.SchoolofInformationandComputerScience,
UniversityofCalifornia,Irvine,CA.https://archive.ics.uci.edu/ml/datasets
Dumitrescu,E.,Hué,S.,Hurlin,C.,&Tokpavi,S.(2022).Machinelearningforcreditscoring:Improving
logisticregressionwithnon-lineardecision-treeeffects.EuropeanJournalofOperationalResearch,
297(3),1178–1192.https://doi.org/10.1016/j.ejor.2021.06.053
Elkan,C.(2001).Thefoundationsofcost-sensitivelearning.InSeventeenthinternationaljointconferenceon
artificialintelligence(pp.973-978).
Finlay,S.(2009).Consumercreditfundamentals(2nded.).PalgraveMacMillan.
Fiore,U.,DeSantis,A.,Perla,F.,Zanetti,P.,&Palmieri,F.(2017).Usinggenerativeadversarialnetworksfor
improvingclassificationeffectivenessincreditcardfrauddetection.InformationSciences,479,448–455.
https://doi.org/10.1016/j.ins.2017.12.030
Friedman,J.H.(2001).Greedyfunctionapproximation:Agradientboostingmachine.AnnalsofStatistics,
29(5),1189–1232.
Gea-Carrasco, C. (2015). IFRS 9 will significantly impact banks’ provisions and financial statements. In
Moody’sanalyticsriskperspectives(Vol.V).
Hand,D.J.(2009).Measuringclassifierperformance:AcoherentalternativetotheareaundertheROCcurve.
MachineLearning,77,103–123.https://doi.org/10.1007/s10994-009-5119-5
Hofmann,H.(1994).Statlog(GermanCreditData)[Dataset].UCImachinelearningrepository.https://doi.
org/10.24432/C5NC77
IASB.(2014).IFRSstandard9:Financialinstruments,InternationalAccountingStandardsBoard.
Khashman,A.(2010).Neuralnetworksforcreditriskevaluation:Investigationofdifferentneuralmodelsand
learningschemes.ExpertSystemswithApplications,37(9),6233–6239.
Lessmann,S.,Baesens,B.,Seow,H.V.,&Thomas,L.C.(2015).Benchmarkingstate-of-the-artclassification
algorithmsforcreditscoring:Anupdateofresearch.EuropeanJournalofOperationalResearch,247(1),
124–136.https://doi.org/10.1016/j.ejor.2015.05.030
Liu,Y.,Zhou,Y.,Wen,S.,&Tang,C.(2014).Astrategyonselectingperformancemetricsforclassifier
evaluation. International Journal of Mobile Computing and Multimedia Communications, 6, 20–35.
https://doi.org/10.4018/IJMCMC.2014100102
Mahbobi,M.,Kimiagari,S.,&Vasudevan,M.(2023).Creditriskclassification:Anintegratedpredictive
accuracyalgorithmusingartificialanddeepneuralnetworks.AnnalsofOperationsResearch,330(1),
609–37.
Maldonado,S.,Bravo,C.,López,J.,&Pérez,J.(2017).Integratedframeworkforprofit-basedfeatureselection
andSVMclassificationincreditscoring.DecisionSupportSystems,104,113–121.
Martin,J.,Taheri,S.,&Abdollahian,M.(2024).Optimizingensemblelearningtoreducemisclassification
costsincreditriskscorecards.Mathematics,12(6),855.https://doi.org/10.3390/math12060855
Marzban,C.(2004).TheROCcurveandtheareaunderitasperformancemeasures.WeatherandForecasting,
19(6),1106–1114.
Mencia,J.,&Jimenez,G.(2007).Modelingthedistributionofcreditlosseswithobservableandlatentfactors
(April18,2007).InBancodeEspañaResearchPapers.AvailableatSSRN.https://doi.org/10.2139/ssrn.
981109
Montoya,A.,Odintsov,K.,&Kotek.M.(2018).HomeCreditDefaultRisk.https://kaggle.com/competitions/
home-credit-default-risk,Kaggle
Obare,D.M.,&Muraya,M.M.(2018).Comparisonofaccuracyofsupportvectormachinemodelandlogistic
regressionmodelinpredictingindividualloandefaults.AmericanJournalofAppliedMathematicsand
Statistics,6(6),266–271.https://doi.org/10.12691/ajams-6-6-8
Odegua,R.(2020).Predictingbankloandefaultwithextremegradientboosting.
Ostrowski,J.(2024).Averagemortgagedebtin2024,Bankratewebsite.Accessedon10December2024.
Ramezan,C.A.,Warner,T.A.,Maxwell,A.E.,&Price,B.S.(2021).Effectsoftrainingsetsizeonsupervised
machine-learningland-coverclassificationoflarge-areahigh-resolutionremotelysenseddata.Remote
Sensing,13,368.https://doi.org/10.3390/rs13030368
Schebesch,K.,&Stecking,R.(2005).Supportvectormachinesforclassifyinganddescribingcreditapplicants:
Detectingtypicalandcriticalregions.JournalofTheOperationalResearchSociety,56,1082–1088.
https://doi.org/10.1057/palgrave.jors.2602023
123

AnnalsofOperationsResearch
Tripathi,D.,Edla,D.R.,Kuppili,V.,&Bablani,A.(2020).Evolutionaryextremelearningmachinewithnovel
activationfunctionforcreditscoring.EngineeringApplicationsofArtificialIntelligence,96,103980.
Teles,G.,Rodrigues,J.J.P.C.,Rabêlo,R.A.L.,&Kozlov,S.A.(2021).Comparativestudyofsupportvector
machinesandrandomforestsmachinelearningalgorithmsoncreditoperation.Software:Practiceand
Experience,51,2492–2500.https://doi.org/10.1002/spe.2842
Thomas,L.C.,Edelman,D.B.,&Crook,J.N.(2002).Creditscoringanditsapplications.Philadelphia:
SIAMMonographsonMathematicalModelingandComputation.
Tian,Z.,Xiao,J.,Feng,H.,&Wei,Y.(2020).Creditriskassessmentbasedongradientboostingdecisiontree.
ProcediaComputerScience,174,150–160.https://doi.org/10.1016/j.procs.2020.06.070
Vapnik,V.(1996).Thenatureofstatisticallearningtheory.Springer.
Verbraken,T.,Bravo,C.,Weber,R.,&Baesens,B.(2014).Developmentandapplicationofconsumercredit
scoringmodelsusingprofit-basedclassificationmeasures.EuropeanJournalofOperationalResearch,
238(2),505–513.https://doi.org/10.1016/j.ejor.2014.04.001
Wang,C.,Deng,C.,&Wang,S.(2020).Imbalance-XGBoost:Leveragingweightedandfocallossesforbinary
label-imbalancedclassificationwithXGBoost.PatternRecognitionLetters,136,190–197.https://doi.
org/10.1016/j.patrec.2020.05.035
Wang,H.,Kou,G.,&Peng,Y.(2021).Multi-classmisclassificationcostmatrixforcreditratingsinpeer-
to-peerlending.JournaloftheOperationalResearchSociety,72(4),923–934.https://doi.org/10.1080/
01605682.2019.1705193
Xia,Y.,Liu,C.,&Liu,N.(2017).Cost-sensitiveboostedtreeforloanevaluationinpeer-to-peerlending.
ElectronicCommerceResearchandApplications,24,30–49.https://doi.org/10.1016/j.elerap.2017.06.
004
Yhip,T.M.,&Alagheband,B.M.D.(2017).Thepracticeoflending.PalgraveMacmillan.https://doi.org/
10.1007/978-3-030-32197-0
Zhang,T.,Zhang,W.,Xu,W.,&Hao,H.(2018).Multipleinstancelearningforcreditriskassessmentwith
transactiondata.Knowledge-BasedSystems.https://doi.org/10.1016/j.knosys.2018.07.030
Publisher’sNote SpringerNatureremainsneutralwithregardtojurisdictionalclaimsinpublishedmapsand
institutionalaffiliations.
123