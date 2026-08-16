---
conversion_metadata:
  converted_at: "2026-07-21T08:37:40Z"
  converter_tool: "markitdown"
  converter_version: "0.1.6"
  source_pdf: "Schwartz et al.pdf"
  source_pdf_sha256: "3fbc8a0ca70c3a9bf5a2543e3da46d60ce4485cddbd46ec83ed18d2de4ebf4bf"
  page_count: 17
  markdown_char_count: 104518
---

<!-- PAGE-AWARE EXTRACTION (via pdfminer.six) -->

<!-- PAGE 1 -->

Enhancing ML Interpretability for Credit
Scoring

Sagi Schwartz1, Qinling Wang2, Fang Fang2,3
1Dept. of Computer Science, Delft University of Technology
2Dept. of Applied Mathematics, Delft University of Technology
3FF Quant Advisory B.V., Utrecht
s.schvarcz@student.tudelft.nl, q.wang-7@tudelft.nl, f.fang@tudelft.nl

Word count: 4813
Number of figures and tables: 8

5
2
0
2

p
e
S
4
1

]

G
L
.
s
c
[

1
v
9
8
3
1
1
.
9
0
5
2
:
v
i
X
r
a

---

<!-- PAGE 2 -->

Abstract

Predicting default is essential for banks to ensure profitability and financial stabil-
ity. While modern machine learning methods often outperform traditional regression
techniques, their lack of transparency limits their use in regulated environments. Ex-
plainable artificial intelligence (XAI) has emerged as a solution in domains like credit
scoring. However, most XAI research focuses on post-hoc interpretation of black-box
models, which does not produce models lightweight or transparent enough to meet
regulatory requirements, such as those for Internal Ratings-Based (IRB) models.

This paper proposes a hybrid approach: post-hoc interpretations of black-box mod-
els guide feature selection, followed by training glass-box models that maintain both
predictive power and transparency.

Using the Lending Club dataset, we demonstrate that this approach achieves per-
formance comparable to a benchmark black-box model while using only 10 features - an
88.5% reduction. In our example, SHapley Additive exPlanations (SHAP) is used for
feature selection, eXtreme Gradient Boosting (XGBoost) serves as the benchmark and
the base black-box model, and Explainable Boosting Machine (EBM) and Penalized
Logistic Tree Regression (PLTR) are the investigated glass-box models.

We also show that model refinement using feature interaction analysis, correlation

checks, and expert input can further enhance model interpretability and robustness.

Keywords: credit scoring, explainable AI, glass-box models, feature selection, regulatory
compliance, default modeling.

Key Messages

• Transparent, lightweight ML models better meet regulatory and practical needs.

• Our approach can cut features by 80%+ without reducing predictive accuracy.

• Post-hoc tools are used for selecting key features from black-box models.

• The resulting reduced glass-box models ensure transparency and accuracy.

1

Introduction

Credit scoring is one of the core tasks in the financial sector. While traditional statis-
tical models remain widely used, there is a growing trend among banks to incorporate
artificial intelligence (AI) into credit scoring processes. As of November 2024, 54.12% of
European banks were leveraging AI for credit scoring and creditworthiness assessment (Eu-
ropean Banking Authority, 2024). Regarding the performance of AI based models, Alonso
and Carbo (2020, 2021) reported that machine learning (ML) techniques can significantly
improve predictive power, potentially leading to a 12.4% to 17% reduction in regulatory
capital requirements.

Despite these advances, logistic regression and other generalized linear models remain dom-
inant in probability of default (PD) modeling. This is primarily due to their inherent
interpretability, which is a desirable and sometimes mandatory property for models used in
regulated environments, as emphasized in legal frameworks such as the EU GDPR Recital
71 and the U.S. Equal Credit Opportunity Act.

1

---

<!-- PAGE 3 -->

Recent studies have applied ML models extensively to credit scoring tasks (Ariza-Garzon
et al., 2020; De Lange et al., 2022; Misheva et al., 2021), often using post-hoc explanation
methods such as SHapley Additive exPlanations (SHAP) (S. Lundberg & Lee, 2017) and
Local Interpretable Model-agnostic Explanations (LIME) (Ribeiro et al., 2016). These tools
help interpret model predictions by identifying important features and explaining model
behavior in ways that align with domain knowledge and human intuition. For example,
top-ranked features identified via SHAP often correspond to variables already recognized by
practitioners as relevant financial indicators.

However, despite these interpretive efforts, the inherent complexity of black-box ML models
remains a major obstacle. These models typically involve numerous feature interactions
and exhibit non-linear relationships that are difficult to understand and communicate, par-
ticularly to model owners and regulatory supervisors. There are two primary sources of
this complexity: the high dimensionality of input data and the structural intricacies of the
algorithms themselves. This paper proposes a framework that addresses both.

Our approach begins by training a high-performing black-box ML model using the full
feature set, which serves as both a performance benchmark and the basis for feature selection.
We then apply a post-hoc interpretation tool, specifically SHAP in our testing example, to
rank the features by importance. A subset of top-ranked features is selected and used to
train interpretable, glass-box ML models, such as the Explainable Boosting Machine (EBM)
and Penalized Logistic Tree Regression (PLTR). Finally, the resulting simple models can
be fine-tuned via feature interaction analysis, correlation analysis, and expert opinion, for
further enhancement of the model performance.

This approach ultimately produces explainable and technically transparent models that align
more closely with the expectations of both regulators and practitioners in the credit risk
domain.

2

Industry Benchmark: Logistic Regression

Laying the groundwork for high-performance interpretable machine learning algorithms, we
begin by examining logistic regression, the preferred modeling technique in the industry.
Logistic regression is a statistical model that estimates the log-odds of an event occurring as
a linear combination of independent variables. The estimated log-odds is then transformed
into a probability that the event will take place. By setting a threshold for this probability,
logistic regression can be used as a binary classifier, where outcomes above and below the
threshold correspond to two distinct classes.

Briefly, logistic regression is a generalized linear model that estimates the probability of a
binary outcome:

p = P (Y = 1 | X = x),
where X = (X1, X2, . . . , Xd) is the vector of features and x = (x1, x2, . . . , xd) is a realization
of these features. The logistic regression model provides an estimate of p given by

ˆp ≜ σ(cid:0)z(β, x)(cid:1) =

1
1 + e−z(β,x)

,

(1)

where σ(·) is the sigmoid function and the linear component is

z(β, x) = β0 + β1x1 + β2x2 + · · · + βdxd,

2

---

<!-- PAGE 4 -->

with parameter vector β = (β0, β1, . . . , βd).
The model is typically trained by minimizing the negative log-likelihood (log-loss) function:

L(β) = −

1
n

n
(cid:88)

i=1

(cid:104)
yi ln ˆpi + (1 − yi) ln(1 − ˆpi)

(cid:105)
,

(2)

where n is the number of training samples, yi ∈ {0, 1}, ˆpi = σ(z(β, xi)), and xi is the i-th
feature vector. This cost function penalizes confident but incorrect predictions. Optimiza-
tion is usually performed via gradient descent or related algorithms to obtain parameter
estimates ˆβ.
One of the key advantages of logistic regression is interpretability. By rearranging Eq. (1)
in terms of fitted log-odds, we have

(cid:18) ˆp

ln

1 − ˆp

(cid:19)

= z(β, x) = β0 + β1x1 + · · · + βdxd.

This expresses a linear relationship between the features and the log-odds of the positive
class. Holding all other features constant, a one-unit increase in feature xi multiplies the
odds of being in the positive class by eβi. The intercept β0 represents the log-odds when all
features x1, x2, . . . , xd are zero, corresponding to odds of eβ0.
However, a key limitation of logistic regression is that the resulting model is often too simple
to accurately capture complex data patterns, which may lead to poor performance compared
to more flexible ML models (Alonso & Carbo, 2020, 2021; De Lange et al., 2022; Moscatelli
et al., 2019; Schmitt, 2024).

3 Existing Explainable AI Models

There have been continuous advancements both in terms of complexity and capability of
machine learning algorithms in recent years. On the one hand, these algorithms enable
faster and more accurate data modeling; on the other, they pose challenges in terms of
explainability and trust.

In the existing literature, there are two main approaches in interpreting and explaining
ML models. The first approach is to use inherently interpretable methods - also known as
glass-box models - such as linear regression, decision trees, and generalized additive models
(GAMs). While these methods offer desirable transparency, their predictive performance
may be insufficient. The second approach involves model-agnostic interpretation tools that
can be applied to any supervised machine learning model, also known as post-hoc methods.

In the subsections that follow, we briefly recall some key post-hoc explainable AI (XAI)
methods, along with recent advances in glass-box models reported in the literature. These
will lay the foundation for the approach we will propose in Section 4.1.

3.1 Post-Hoc Explanation Methods

In the literature of credit scoring, two post-hoc explainable XAI methods are mostly studied:
Locally Interpretable Model-Agnostic Explanations (LIME) and SHapley Additive exPlana-
tions (SHAP).

3

---

<!-- PAGE 5 -->

LIME, introduced by Ribeiro et al., 2016, provides explanations for individual predictions
by fitting a simple local model around the observation being explained, using similar data
points. The local model is typically chosen from interpretable classes such as linear models
or decision trees.

SHAP, introduced by S. Lundberg and Lee, 2017, computes Shapley values and presents
them as an additive feature attribution method, which is effectively a linear model. A
notable advantage of SHAP is its visualization tools, including the SHAP summary plot
and dependence plot, which are very handy to use and greatly enhance the interpretation
of the model outcomes.

Other interpretation methods include Partial Dependence Plots, Accumulated Local Effects
(ALE) Plots, Functional Decomposition, and Permutation Feature Importance, among oth-
ers. We will not explore these methods in this paper but refer the reader to Molnar, 2022
for relevant details.

Here we elaborate further on SHAP, one of the most widely used methods for providing
global explanations of black-box models and a key component of our experiments. SHAP
is based on the Shapley values from game theory. More precisely, it uses Shapely values to
determine the contribution of each feature to a final prediction made by a model.

Let F = {1, 2, . . . , d} be the set of indices for all features, and let x ∈ Rd be a feature vector.
For a given feature with number j ∈ F , the Shapley value of this feature is defined as

ϕj(x) =

(cid:88)

S⊆F \{j}

|S|! (|F | − |S| − 1)!
|F |!

(cid:104)

fS∪{j}(xS∪{j}) − fS(xS)

(cid:105)

,

where |S| is the cardinality of the subset S, i.e. the number of elements in S; xS ∈ R|S| is the
subvector of x restricted to the indices in S; fS : R|S| → R denotes the model restricted to
the feature set S (with all other features marginalized out or fixed according to a baseline).
The weight w(S) = |S|! (|F |−|S|−1)!
is the fraction of feature orderings in which the subset S
appears before j.

|F |!

The computational complexity for Shapley values grows exponentially in the number of
features. To address this issue, SHAP provides two efficient approximation methods for
Shapley values: model agnostic Kernel SHAP and tree-based Tree SHAP. The latter, intro-
duced in S. M. Lundberg et al., 2019, dramatically reduces computation time by exploiting
the structure of tree-based models.

3.2 Black-box Models with Post-Hoc Explanations

One of the best performing black-box models for credit scoring - as well as for other appli-
cations in finance such as time-series prediction - is XGBoost (eXtreme Gradient Boosting).
Alonso and Carbo (2021) showed that XGBoost, along with random forest, consistently
outperformed other models examined in terms of AUC-ROC. In addition, Jones et al., 2015
demonstrated that gradient boosting trees were among the top-performing ML classifiers
for the credit scoring task conducted in their study. Similar results were also reported by
De Lange et al. (2022) and Moscatelli et al. (2019).

XGBoost is an optimized implementation of the gradient boosting framework developed
It constructs an ensemble of K regularized Classification
by Chen and Guestrin (2016).

4

---

<!-- PAGE 6 -->

And Regression Trees (CARTs) to solve supervised learning tasks, including regression and
classification. The prediction for an instance xi is given by

ˆyi =

K
(cid:88)

k=1

fk(xi),

fk ∈ F,

(3)

where K is the number of trees, and F is the space of all CARTs. Each tree fk maps the
input feature vector xi ∈ Rd to a predicted score, and the ensemble prediction is obtained by
summing the outputs of all trees. The model is trained to minimize a regularized objective
function

L(ϕ) =

n
(cid:88)

i=1

l(yi, ˆyi) +

K
(cid:88)

k=1

Ω(fk).

Here l is a differentiable convex loss function that quantifies the difference between the
ground truth yi and the prediction ˆyi. It is squared error for regression and logistic loss
for classification. For binary classification, the logistic loss corresponds to the negative
log-likelihood, which is very similar to Eq. (2):

(cid:104)
l(yi, ˆyi) = −

yi ln σ(ˆyi) + (1 − yi) ln (cid:0)1 − σ(ˆyi)(cid:1)(cid:105)
,

where σ(·) is again the sigmoid function.

The second term, Ω(f ), penalizes model complexity such that the model favors simpler
2 λ∥w∥2, where T is the number of
but predictive functions, and is given by Ω(f ) = γT + 1
leaves in the tree, w is the vector of leaf weights, and γ and λ are respective regularization
parameters.

The objective function above is equivalent to L(t) = (cid:80)
+ ft(xi)) + Ω(ft), with
ft(xi) being the CART added at iteration t. To simplify the optimization, a second-order
Taylor expansion is applied around the current prediction ˆy(t−1)

i l(yi, ˆy(t−1)

, which gives

i

i

L(t) ≃

(cid:88)

(cid:104)
l(yi, ˆy(t−1)
i

i

where

) + gift(xi) + 1

2 hif 2

(cid:105)
t (xi)

+ Ω(ft),

∂l(yi, ˆy(t−1)
i
∂ ˆy(t−1)
i
Dropping constant terms independent of ft yields the simplified objective
(cid:104)

∂2l(yi, ˆy(t−1)
i
∂(ˆy(t−1)
)2
i

hi =

gi =

)

)

,

.

(cid:88)

(cid:101)L(t) ≃

gift(xi) + 1

2 hif 2

(cid:105)
t (xi)

+ Ω(ft).

For the logistic loss, these derivatives are explicitly

i

gi = σ(ˆy(t−1)

i

) − yi,

hi = σ(ˆy(t−1)

i

)(cid:0)1 − σ(ˆy(t−1)

i

)(cid:1).

Since gradient boosting models consist of an ensemble of decision trees, where each tree may
utilize multiple features to make predictions, it is challenging to gauge the contribution of
individual features to the model’s predictions.

5

---

<!-- PAGE 7 -->

To address this model transparency issue, XGBoost library is equipped with several fea-
ture importance metrics that can be used to obtain more knowledge on the model’s inner
workings. The most commonly used metric is the gain, which measures how much a feature
improves the model’s objective function (e.g., by reducing error or loss) when it is used for a
split. Features with higher gain values are considered more important, since they contribute
more to improving the model’s accuracy. Another metric is cover, which reflects how many
training samples are influenced by a split using a particular feature. In practice, this means
that features used higher up in the trees, which affect larger groups of samples, tend to have
higher cover values. The last metric is frequency, which simply counts how often a feature
is used to split the data across all trees in the model. A higher frequency indicates that the
feature is frequently chosen as a useful splitting criterion.

Although these feature importance metrics provide some insight into which features the
model relies on most, they miss several key aspects. First, none of these metrics explains
how a feature influences the model’s prediction. In other words, they do not reveal how a
change in the value of a specific feature would affect the output. For example, would an
increase in a particular feature make a client more likely to default, or would it make the loan
appear safer? Secondly, these metrics do not offer intuition about the model’s behavior in
the absence of a feature. Would the predictions of the model change significantly if certain
features were excluded? Lastly, they fail to capture the impact of interactions between
features on the final prediction.

These limitations underscore the need for more advanced tools such as SHAP to interpret
the inner workings of complex models. As noted earlier, especially the Tree SHAP method
is particularly designed for fast calculation of Shapley values for tree-based models.

XAI models that combine ensemble tree-based algorithms with SHAP have become increas-
ingly prevalent in recent credit scoring literature, as demonstrated by Misheva et al. (2021),
Zhu et al. (2024), and Alonso and Carbo (2021).

3.3 Glass-Box Models from Recent Years

At the other end of the transparency spectrum are the glass-box models. This category
includes traditional methods such as regression and decision trees, as well as more recent
models that incorporate additional complexity while maintaining transparency.

Our literature review identifies two glass-box models from recent years that show promis-
ing performance: Explainable Boosting Machine (EBM) and Explainable Boosting Machine
(EBM) and Penalized Logistic Tree Regression (PLTR). EBM, developed by Nori et al.
(2019), is a supervised machine learning algorithm specifically designed to balance inter-
pretability and predictive power.
It offers model intelligibility while achieving accuracy
comparable to state-of-the-art algorithms such as XGBoost. PLTR, introduced by Du-
mitrescu et al. (2022), uses predictors derived from shallow decision trees as inputs to a
penalized logistic regression, offering a hybrid approach that enhances both interpretability
and predictive performance.

3.3.1 Explainable Boosting Machine (EBM)

The EBM algorithm belongs to the family of generalized additive models (GAMs), which
extend generalized linear models (GLMs) by modeling the expected value of the target
variable as a sum of smooth, non-linear functions of the predictors.

6

---

<!-- PAGE 8 -->

EBM trains the model iteratively in a round-robin fashion: in each iteration, a small tree
is fitted to capture the effect of one feature on the residuals, and the residuals are updated
accordingly. This process is repeated across the features one by one, completing one round-
robin pass through the dataset. A small learning rate ensures that the order in which features
are included does not significantly influence the final model. As a result, the training process
requires many iterations, as many as ten thousand, to reach convergence. The result is an
ensemble of small trees per feature, which can be aggregated collectively to capture the
relationship between the feature and each target variable.

In mathematical terms, the prediction function reads

g(E[Y ]) = β0 +

d
(cid:88)

j=1

fj(xj),

(4)

where g is a link function and each fj denotes a smooth function representing the effect of
j-th feature, i.e. xj, on the target variable. Worth noting that, the difference between Eq.
(4) and Eq. (3) is that the functions involved in EBM prediction are uni-variate functions,
while those involved in XGBoost take multiple features as inputs. Each marginal function
fj(·) is stored after training and can be visualized in plots. These stored functions are
eventually used for predictions later on.

Building on this concept, Lou et al. (2013) introduced Generalized Additive Model plus
Interactions (GA2M), which incorporates pairwise feature interactions as follows:

g(E[Y ]) = β0 +

d
(cid:88)

j=1

fj(xj) +

(cid:88)

fj,q(xj, xq)

1≤j<q≤d

(5)

Despite the added complexity, GA2Ms remain interpretable due to their additive structure
and the use of small CARTs or shallow trees to model each term. EBM can identify and
incorporate feature interactions by training pairwise interaction terms, if enabled, using a
similar iterative process but built on Eq. (5).

Finally, the EBM library generates visualizations that illustrate feature importance and
interactions that provide insights into the model’s inner workings.

Testing results in Dessain et al., 2023 show that EBM performs comparably to black-box
gradient boosting models, such as XGBoost. This result appears to be consistent in models
used outside the scope of credit scoring and finance (Caruana et al., 2015).

3.3.2 Penalized Logistic Tree Regression (PLTR)

The other powerful and explainable model is called Penalized Logistic Tree Regression, or
PLTR for short. It is introduced in Dumitrescu et al., 2022 for a credit scoring model. The
model is constructed in two steps.

In the first step, binary features are created using short-depth decision trees with one or
two splits. Based on single-split trees, each feature xj generates a new binary feature ν(j)
for logistic regression, which takes the value 1 if the j-th feature of the i-th sample exceeds
the threshold from the single-split tree, and 0 otherwise. From two-split trees involving two
features xj and xq, with xj assumed to be more informative, we first define ν(j) as in the
single-split case, then we define a second binary feature ξ(j,q), which takes the value 1 if xj

7

---

<!-- PAGE 9 -->

is below its threshold and xq is above its threshold. The final set of features used in the
model thus consists of original set of features xj, binary features from the single-split trees
ν(j), and binary features from the two-split trees ξ(j,q).

In the second step, a penalized logistic regression is applied to this expanded set of features.
Recall the logistic regression log-likelihood in Eq. (2), we have

L(θ) =

1
n

n
(cid:104)
(cid:88)

i=1

(cid:105)
yi ln [σ (z(θ, ˜xi))] + (1 − yi) ln [1 − σ (z(θ, ˜xi))]

,

(6)

for all j ̸= q, and θ is the respective set of model parameters.

where ˜xi is the extended feature vector from the i-th sample, containing all xj, ν(j)
ξ(j,q)
i
To prevent over-fitting, we introduce regularization or penalization by adding a penalty term
to the negative log-likelihood function:

and

i

˜L(θ) = −L(θ) + λP (θ),

where P (θ) is the additional penalty term and λ is the tuning parameter controlling the
strength of the penalty. There are many choices of P (θ), Zou, 2006 proposed the adaptive
lasso estimator.

4 Comparing the Models, Is There a Silver Bullet?

As summarized in the discussion paper from European Banking Authority, 2023, a cen-
tral challenge in applying machine learning techniques to regulated areas such as IRB PD
modeling lies in their complexity, which hinders explainability. In particular, that discussion
paper recommends institutions to avoid, among others, including an excessive number of ex-
planatory drivers or drivers with no significant predictive information, and overly complex
modeling choices if simpler approaches yielding similar results are available.

While existing XAI approaches, such as combining black-box models with post-hoc inter-
pretability tools like SHAP, provide some insights and certain level of understanding of the
model behaviors, they do not automatically meet those guidelines. These models typically
involve a large number of features. Nonlinear behaviors combined with numerous feature
interactions are difficult to interpret and communicate, particularly for model owners and
regulatory supervisors. Even when using inherently interpretable models like EBM, intro-
ducing feature interactions can result in patterns that defy financial intuition.

To address this gap, we propose a hybrid approach that leverages the feature rankings pro-
duced by post-hoc interpretability tools applied to black-box models, and then uses these
insights to construct interpretable, glass-box models. This method maintains predictive per-
formance while significantly reducing model complexity and feature count. The resulting
model based on the proposed approach is potentially more suitable for regulated environ-
ments than existing XAI models.

In the following subsections, we present the proposed method, describe the dataset and
experimental setup, compare our lightweight models against benchmarks in terms of both
accuracy and interpretability, and finally show how domain expertise and further analyses
(e.g., feature interactions and correlations) can be used to fine-tune the model.

8

---

<!-- PAGE 10 -->

4.1 Our Proposal

We propose the following approach:

- Step 1: train a well performing black-box machine learning model using the full feature
set. This we name as the “base” model, which serves both as a performance benchmark
as well as the basis for feature selection for step 2.

- Step 2: rank features by their importance in the base model, by for example applying

a post-hoc interpretation tool like SHAP.

- Step 3: select a few, such as 10 or 20, top-ranked features to train a glass-box model,

which can be EBM or PLTR for example.

- Step 4: based on interaction analysis, correlation analysis, and/or expert opinion,

refine the selection of top-ranked features and repeat step 3.

The result is explainable and technically transparent models that better align with the
expectations of both regulators and practitioners in the credit risk domain.

To evaluate the potential of this approach for credit scoring, we used the top-performing
classifiers introduced in Section 3.2 as benchmarks.

Note that, as our goal is to propose a general method to simplify and "glassify" black-box
models while preserving their predictive power, we did not extensively optimize the base
models. Nor did we aim to reconfirm that tree boosting algorithms outperform logistic
regression in credit scoring - an already well-established result.

4.2 Data Preparation and Base Models

Our experiments were based on data from the Lending Club peer-to-peer lending platform,
which operated until the end of 2020. This dataset has been widely used in prior studies on
explainable machine learning methods, allowing us to compare against established methods
and focus on persistent challenges in interpreting ML models in financial applications.

We preprocessed Lending Club data following similar steps to those taken in Ariza-Garzon
et al. (2020). As for the target variable, we decided to consider only ‘Fully Paid’ and
‘Charged Off’ categories of the variable loan_amount, encoding them as 0 and 1 respec-
tively. We also took the average of fico_range_high and fico_range_low to create the fea-
ture fico_range_low, while removing the original features. The features home_ownership,
purpose, addr_state and emp_length were encoded using one-hot encoding. Where neces-
sary, missing values were imputed with the mean of the corresponding feature.

The split between training data and test data was done based on issue_d feature, such that
the train data consisted of data up to July 2015, and the test set consisted of data from
August 2015 to December 2018. The overall default rate observed in the data was around
20%, and the total number of features was 87. Using the preprocessed data, we built three
baseline models employing the algorithms previously discussed:
logistic regression (LR),
XGBoost (XGB) and EBM. Since the data at hand is imbalanced - in the sense that the de-
faulting class is significantly smaller than the non-defaulting class, we assigned class weights
to each model. This approach typically enhances the model’s ability to correctly classify the
minority class, often at the expense of performance on the majority class. However, in the

9

---

<!-- PAGE 11 -->

Model AUPRC AUROC F1 score Balanced Accuracy

0.3389
LR
0.3436
XGB
EBM 0.3518

0.6653
0.6687
0.6744

0.42
0.4160
0.4211

0.6187
0.6203
0.6251

Table 1: Performance of base models (with all features included)

context of credit risk modeling, prioritizing the accurate identification of default events is
both acceptable and desirable.

For evaluating the performance of the different models, we used multiple performance met-
rics. However, we placed greater emphasis on metrics that appropriately account for the
performance on the minority class. In addition to balanced accuracy, we included AUROC
(Area Under the Receiver Operating Characteristic curve), F1 scores and AUPRC (Area
Under the Precision Recall Curve).

Table 1 summarizes the performance of the models which we aim to preserve in our simplified,
interpretable approach.

4.3

Issue in Interpreting Base Models

Given the volume of features and the complex, implicit interactions captured by the model,
validating whether the model’s decisions align with domain knowledge becomes a daunting
task. Top features identified by SHAP can help in explaining the scoring result for each
individual client. However, it is challenging to explain how much the interactions between
features affect the final score and why a large number of features are still needed.

Moreover, even when using inherently interpretable models like EBM, introducing feature
interactions can result in patterns that defy financial intuition. As shown in Figure 1, the
model suggests that applicants with lower loan amounts and higher salaries are more likely
to default than those with higher loan amounts and lower salaries. This contradicts basic
financial reasoning. However, when we examine the individual effects of these two features,
loan amount and annual income, separately, their impact aligns much more closely with
human expectations and established financial logic.

As illustrated in Figure 2 and Figure 3, we observe a clear and intuitive trend: higher loan
amounts are generally associated with a higher probability of default, while higher annual
incomes correspond to a lower probability of default. This motivates us to largely reduce
the number of features, aligning with the guidelines given by earlier mentioned discussion
paper, so as to minimize feature interactions.

4.4 Feature Importance

Having built the three base models, we now proceed to Step 2 as described in Section 4.1,
where we rank the features based on their importance.

For the logistic regression (LR) model, feature importance is determined using the model
coefficients after normalizing the input features. In the case of XGBoost, we rely on tree-
SHAP values to obtain feature attributions. For the EBM model, we use its inherent feature
importance scores. The resulting feature rankings are summarized in Table 2. They are

10

---

<!-- PAGE 12 -->

Figure 1: Loan amount and annual income feature interaction (from SHAP)

Rank LR

XGB
fico_range_high
loan_amnt
annual_inc
dti

fico_range_high
loan_amnt
dti
annual_inc
home_ownership_RENT purpose_credit_card
purpose_credit_card
emp_length_nan
purpose_debt_consolid.
purpose_other
adde_state_NY

1
2
3
4
5
6
7
8
9
10

home_ownership_RENT purpose_debt_consolid.
home_ownership_MORT. home_ownership_RENT
home_ownership_MORT.
purpose_debt_consolid.
emp_length_nan
emp_length_nan
adde_state_NY
adde_state_NY

EBM
loan_amnt
fico_range_high
annual_inc
purpose_credit_card
dti

Table 2: Top features in different models

largely consistent across all three models, with only minor differences in the ordering (note
that for EBM, interaction terms were initially excluded from the ranking).

Remark: Among the three, XGBoost provided the fastest computation of feature impor-
tance, making it a practical choice for feature selection.

4.5 Light-weight Glass-box Models

After obtaining the feature importance rankings discussed above, we proceeded to build
glass-box models using subsets of the top-ranked features of varying sizes, i.e. Step 3 of our
approach as described in Section 4.1. The glass-box models we considered were EBM and
PLTR.

By plotting performance metrics against the number of included features, we could identify
a practical cut-off point for constructing a reduced model. Figure 4 displays the progression
of AUPRC, AUROC, and F1 scores as a function of the number of features. In the case of
the Lending Club data, we observe that adding more than 10 features yields no substantial
improvement in model performance. This insight allowed us to reduce the dimensionality
from 86 features to just 10, without significantly compromising predictive power.

11

---

<!-- PAGE 13 -->

Figure 2: Loan amount attribution (from SHAP)

Notably, EBM consistently achieves performance that is at least on par with XGBoost, while
offering significantly greater transparency. PLTR also improves interpretability relative to
XGBoost but underperforms compared to both EBM and XGBoost in terms of predictive
accuracy. As a result, EBM emerges as the most favorable model in our study, providing a
strong balance between explainability and performance.

4.6 Refinements

Once the reduced EBM model is obtained, both global and local analyses can be conducted
with ease. Since EBM stores all marginal functions used in its predictions and the reduced
EBM model uses a limited number of features, interpreting the model becomes straightfor-
ward. These insights can, in turn, be used to further refine and enhance the model.

4.6.1 Feature Interaction Analysis

As shown earlier, even pairwise interactions can lead to counterintuitive or misleading con-
clusions, like in the case of the Lending Club data.

To further assess the impact of pairwise interactions on model performance, we built a
series of ancillary models, each incorporating a different number of pairwise interactions,
ranging from zero up to nine. Figure 5 summarizes the different performance metrics as a
function of the number of pairwise interactions from these ancillary models. The maximum
improvement was measured using F1 score and amounted to 0.4% when all nice pair-wise
interactions were included, which is a very marginal gain. This analysis suggests that, in
some cases, practitioners may confidently exclude all feature interactions and still obtain a
glass-box model that outperforms the logistic regression benchmark.

12

---

<!-- PAGE 14 -->

Figure 3: Annual income attribution (from SHAP)

Figure 4: Sensitivity analysis: Performance w.r.t. the number of (top) features included

4.6.2 Correlation Analysis

It is important to note that while SHAP analysis provides a robust, data-driven estimation
of feature importance, it also has certain limitations. A notable weakness lies in its handling
of correlated features. When features are highly correlated, SHAP sometimes distributes
a positive SHAP value to one of the correlated pair, while a negative SHAP value to the
other, or distribute the importance across them. This makes it difficult to fully trust the
top feature list selected using SHAP. To mitigate this limitation, we recommend to combine
SHAP with correlation analysis.

We computed the correlation matrix among the top 25 most important features identified
by SHAP. For each pair of highly correlated features, we removed the lower-ranked one if
it was not among the top 10 most important features. This process was repeated until we
obtained a revised set of 20 features. It is important to note that we never removed any of
the original top 10 SHAP-ranked features, even if they were part of a highly correlated pair.
Empirical results show that removing one of the top 10 features often leads to a decline in
model performance, supporting the decision to keep them. The results in the Table 3 also
suggested that this method can imporve the performance of the model.

13

---

<!-- PAGE 15 -->

Figure 5: Sensitivity analysis: EBM performance w.r.t the number of pairwise interactions

Model
XGB
XGB
EBM
EBM Correlation Analysis

Method
Original
Correlation Analysis
Original

AUPRC AUROC F1 score Balanced Accuracy
0.4139
0.3412
0.4145
0.3418
0.4186
0.3487
0.4193
0.3493

0.6641
0.6658
0.6720
0.6725

0.6185
0.6190
0.6226
0.6233

Table 3: Performance comparison for XGBoost and EBM: using original top 20 features
without correlation analysis vs using top 20 features after correlation analysis

5 Conclusion

In this study, we proposed an approach that has the potential to assist banks and financial
institutions in developing more transparent and reliable models with fewer features, meeting
both practical needs and regulatory expectations for Probability of Default (PD) models.

Using the Lending Club dataset, we demonstrated that, following our approach, it is possible
to construct a lightweight glass-box model comprising only a small subset of features, while
achieving predictive performance comparable to a black-box model utilizing the full feature
set.

For future research, we recommend testing the effectiveness and robustness of this approach
across diverse datasets to validate its generalizability and applicability in varied financial
contexts.

Declaration of Interest

The authors report no conflicts of interest. The authors alone are responsible for the content
and writing of the paper.

References
Alonso, A., & Carbo, J. M. (2020). Machine Learning in Credit Risk: Measuring the Dilemma
Between Prediction and Supervisory Cost. SSRN Electronic Journal. https://doi.
org/10.2139/ssrn.3724374

Alonso, A., & Carbo, J. M. (2021). Understanding the Performance of Machine Learning
Models to Predict Credit Default: A Novel Approach for Supervisory Evaluation.
SSRN Electronic Journal. https://doi.org/10.2139/ssrn.3774075

14

---

<!-- PAGE 16 -->

Ariza-Garzon, M. J., Arroyo, J., Caparrini, A., & Segovia-Vargas, M.-J. (2020). Explainabil-
ity of a Machine Learning Granting Scoring Model in Peer-to-Peer Lending. IEEE
Access, 8, 64873–64890. https://doi.org/10.1109/ACCESS.2020.2984412
Caruana, R., Lou, Y., Gehrke, J., Koch, P., Sturm, M., & Elhadad, N. (2015). Intelligible
Models for HealthCare: Predicting Pneumonia Risk and Hospital 30-day Readmis-
sion. Proceedings of the 21th ACM SIGKDD International Conference on Knowledge
Discovery and Data Mining, 1721–1730. https://doi.org/10.1145/2783258.2788613

Chen, T., & Guestrin, C. (2016). XGBoost: A Scalable Tree Boosting System [arXiv:1603.02754

[cs]]. Proceedings of the 22nd ACM SIGKDD International Conference on Knowl-
edge Discovery and Data Mining, 785–794. https : / / doi . org / 10 . 1145 / 2939672 .
2939785
Comment: KDD’16 changed all figures to type1.

De Lange, P. E., Melsom, B., VennerÃžd, C. B., & Westgaard, S. (2022). Explainable AI for
Credit Assessment in Banks. Journal of Risk and Financial Management, 15 (12),
556. https://doi.org/10.3390/jrfm15120556

Dessain, J., Bentaleb, N., & Vinas, F. (2023). Cost of Explainability in AI: An Example
with Credit Scoring Models [Series Title: Communications in Computer and Infor-
mation Science]. In L. Longo (Ed.), Explainable Artificial Intelligence (pp. 498–516,
Vol. 1901). Springer Nature Switzerland. https://doi.org/10.1007/978-3-031-44064-
9_26

Dumitrescu, E., Hué, S., Hurlin, C., & Tokpavi, S. (2022). Machine learning for credit
scoring: Improving logistic regression with non-linear decision-tree effects. European
Journal of Operational Research, 297 (3), 1178–1192.

European Banking Authority. (2023, August). Machine learning for irb models: Follow-up
report from the consultation on the discussion paper on machine learning for irb
models [Accessed: 2025-05-25]. https://www.eba.europa.eu/sites/default/files/
document_library/Publications/Reports/2023/1061483/Follow- up%20report%
20on%20machine%20learning%20for%20IRB%20models.pdf

European Banking Authority. (2024, November). Risk assessment report - november 2024

(Report). European Banking Authority.

Jones, S., Johnstone, D., & Wilson, R. (2015). An empirical evaluation of the performance
of binary classifiers in the prediction of credit ratings changes. Journal of Banking
& Finance, 56, 72–85. https://doi.org/10.1016/j.jbankfin.2015.02.006

Lou, Y., Caruana, R., Gehrke, J., & Hooker, G. (2013). Accurate intelligible models with
pairwise interactions. Proceedings of the 19th ACM SIGKDD international confer-
ence on Knowledge discovery and data mining, 623–631. https://doi.org/10.1145/
2487575.2487579

Lundberg, S., & Lee, S.-I. (2017, November). A Unified Approach to Interpreting Model

Predictions [arXiv:1705.07874 [cs]]. https://doi.org/10.48550/arXiv.1705.07874
Comment: To appear in NIPS 2017.

Lundberg, S. M., Erion, G. G., & Lee, S.-I. (2019, March). Consistent Individualized Feature
Attribution for Tree Ensembles [arXiv:1802.03888 [cs]]. https://doi.org/10.48550/
arXiv.1802.03888
Comment: Follow-up to 2017 ICML Workshop arXiv:1706.06060.

Misheva, B. H., Osterrieder, J., Hirsa, A., Kulkarni, O., & Lin, S. F. (2021, March). Explain-
able AI in Credit Risk Management [arXiv:2103.00949 [q-fin]]. https://doi.org/10.
48550/arXiv.2103.00949

15

---

<!-- PAGE 17 -->

Molnar, C. (2022). Interpretable machine learning: A guide for making black box models ex-
plainable [Available online: https://christophm.github.io/interpretable-ml-book/].
Lulu.com.

Moscatelli, M., Narizzano, S., Parlapiano, F., & Viggiano, G. (2019, December). Corporate
default forecasting with machine learning. Banca d’Italia. Retrieved December 12,
2024, from https://doi.org/10.32057/0.TD.2019.1256

Nori, H., Jenkins, S., Koch, P., & Caruana, R. (2019, September). InterpretML: A Unified
Framework for Machine Learning Interpretability [arXiv:1909.09223 [cs]]. https://
doi.org/10.48550/arXiv.1909.09223

Ribeiro, M. T., Singh, S., & Guestrin, C. (2016, August). "Why Should I Trust You?":
Explaining the Predictions of Any Classifier [arXiv:1602.04938 [cs]]. https://doi.
org/10.48550/arXiv.1602.04938

Schmitt, M. (2024, February). Explainable Automated Machine Learning for Credit Deci-
sions: Enhancing Human Artificial Intelligence Collaboration in Financial Engineer-
ing [arXiv:2402.03806 [q-fin]]. https://doi.org/10.48550/arXiv.2402.03806
Zhu, M., Zhang, Y., Gong, Y., Xing, K., Yan, X., & Song, J. (2024, February). Ensemble
Methodology:Innovations in Credit Default Prediction Using LightGBM, XGBoost,
and LocalEnsemble [arXiv:2402.17979 [cs]]. https://doi.org/10.48550/arXiv.2402.
17979

Zou, H. (2006). The adaptive lasso and its oracle properties. Journal of the American sta-

tistical association, 101 (476), 1418–1429.

16

<!-- MARKITDOWN CONVERSION -->

<!-- Full MarkItDown conversion for formatting fidelity. -->

| Enhancing |     | ML  | Interpretability |     |     | for Credit |
| --------- | --- | --- | ---------------- | --- | --- | ---------- |
Scoring
5202 peS 41  ]GL.sc[  1v98311.9052:viXra
|     |        | Sagi Schwartz1,         | Qinling        | Wang2,           | Fang       | Fang2,3       |
| --- | ------ | ----------------------- | -------------- | ---------------- | ---------- | ------------- |
|     | 1Dept. | of Computer             | Science,       | Delft University |            | of Technology |
|     | 2Dept. | of Applied Mathematics, |                | Delft            | University | of Technology |
|     |        | 3FF                     | Quant Advisory | B.V.,            | Utrecht    |               |
s.schvarcz@student.tudelft.nl, q.wang-7@tudelft.nl, f.fang@tudelft.nl
Word count: 4813
| Number of | figures and | tables: 8 |     |     |     |     |
| --------- | ----------- | --------- | --- | --- | --- | --- |

Abstract
|     | Predicting |     | default | is essential | for | banks to | ensure profitability | and | financial | stabil- |
| --- | ---------- | --- | ------- | ------------ | --- | -------- | -------------------- | --- | --------- | ------- |
ity. While modern machine learning methods often outperform traditional regression
techniques, their lack of transparency limits their use in regulated environments. Ex-
plainable artificial intelligence (XAI) has emerged as a solution in domains like credit
scoring. However, most XAI research focuses on post-hoc interpretation of black-box
models, which does not produce models lightweight or transparent enough to meet
|     | regulatory                        | requirements, |     | such | as those | for Internal                           | Ratings-Based | (IRB) | models. |     |
| --- | --------------------------------- | ------------- | --- | ---- | -------- | -------------------------------------- | ------------- | ----- | ------- | --- |
|     | Thispaperproposesahybridapproach: |               |     |      |          | post-hocinterpretationsofblack-boxmod- |               |       |         |     |
els guide feature selection, followed by training glass-box models that maintain both
|     | predictive | power | and     | transparency. |     |                |           |          |          |      |
| --- | ---------- | ----- | ------- | ------------- | --- | -------------- | --------- | -------- | -------- | ---- |
|     | Using      | the   | Lending | Club dataset, |     | we demonstrate | that this | approach | achieves | per- |
formancecomparabletoabenchmarkblack-boxmodelwhileusingonly10features-an
88.5% reduction. In our example, SHapley Additive exPlanations (SHAP) is used for
featureselection,eXtremeGradientBoosting(XGBoost)servesasthebenchmarkand
the base black-box model, and Explainable Boosting Machine (EBM) and Penalized
|     | Logistic | Tree      | Regression | (PLTR) | are        | the investigated | glass-box           | models.   |     |             |
| --- | -------- | --------- | ---------- | ------ | ---------- | ---------------- | ------------------- | --------- | --- | ----------- |
|     | We       | also show | that       | model  | refinement | using            | feature interaction | analysis, |     | correlation |
checks, and expert input can further enhance model interpretability and robustness.
Keywords: credit scoring, explainable AI, glass-box models, feature selection, regulatory
| compliance, |     | default | modeling. |     |     |     |     |     |     |     |
| ----------- | --- | ------- | --------- | --- | --- | --- | --- | --- | --- | --- |
Key Messages
• Transparent, lightweight ML models better meet regulatory and practical needs.
• Our approach can cut features by 80%+ without reducing predictive accuracy.
| •   | Post-hoc      | tools | are     | used for  | selecting | key features | from black-box |     | models.   |     |
| --- | ------------- | ----- | ------- | --------- | --------- | ------------ | -------------- | --- | --------- | --- |
| •   | The resulting |       | reduced | glass-box | models    | ensure       | transparency   | and | accuracy. |     |
1 Introduction
Credit scoring is one of the core tasks in the financial sector. While traditional statis-
tical models remain widely used, there is a growing trend among banks to incorporate
artificial intelligence (AI) into credit scoring processes. As of November 2024, 54.12% of
European banks were leveraging AI for credit scoring and creditworthiness assessment (Eu-
ropean Banking Authority, 2024). Regarding the performance of AI based models, Alonso
and Carbo (2020, 2021) reported that machine learning (ML) techniques can significantly
improve predictive power, potentially leading to a 12.4% to 17% reduction in regulatory
capital requirements.
Despite these advances, logistic regression and other generalized linear models remain dom-
inant in probability of default (PD) modeling. This is primarily due to their inherent
interpretability, which is a desirable and sometimes mandatory property for models used in
regulated environments, as emphasized in legal frameworks such as the EU GDPR Recital
| 71 and | the | U.S. Equal | Credit | Opportunity |     | Act. |     |     |     |     |
| ------ | --- | ---------- | ------ | ----------- | --- | ---- | --- | --- | --- | --- |
1

Recent studies have applied ML models extensively to credit scoring tasks (Ariza-Garzon
et al., 2020; De Lange et al., 2022; Misheva et al., 2021), often using post-hoc explanation
methods such as SHapley Additive exPlanations (SHAP) (S. Lundberg & Lee, 2017) and
LocalInterpretableModel-agnosticExplanations(LIME)(Ribeiroetal.,2016). Thesetools
help interpret model predictions by identifying important features and explaining model
behavior in ways that align with domain knowledge and human intuition. For example,
top-rankedfeaturesidentifiedviaSHAPoftencorrespondtovariablesalreadyrecognizedby
| practitioners | as  | relevant | financial | indicators. |     |     |     |     |
| ------------- | --- | -------- | --------- | ----------- | --- | --- | --- | --- |
However,despitetheseinterpretiveefforts,theinherentcomplexityofblack-boxMLmodels
remains a major obstacle. These models typically involve numerous feature interactions
and exhibit non-linear relationships that are difficult to understand and communicate, par-
ticularly to model owners and regulatory supervisors. There are two primary sources of
this complexity: the high dimensionality of input data and the structural intricacies of the
algorithms themselves. This paper proposes a framework that addresses both.
Our approach begins by training a high-performing black-box ML model using the full
featureset,whichservesasbothaperformancebenchmarkandthebasisforfeatureselection.
We then apply a post-hoc interpretation tool, specifically SHAP in our testing example, to
rank the features by importance. A subset of top-ranked features is selected and used to
traininterpretable,glass-boxMLmodels,suchastheExplainableBoostingMachine(EBM)
and Penalized Logistic Tree Regression (PLTR). Finally, the resulting simple models can
be fine-tuned via feature interaction analysis, correlation analysis, and expert opinion, for
| further enhancement |     | of  | the model | performance. |     |     |     |     |
| ------------------- | --- | --- | --------- | ------------ | --- | --- | --- | --- |
Thisapproachultimatelyproducesexplainableandtechnicallytransparentmodelsthatalign
more closely with the expectations of both regulators and practitioners in the credit risk
domain.
| 2 Industry |     | Benchmark: |     |     | Logistic | Regression |     |     |
| ---------- | --- | ---------- | --- | --- | -------- | ---------- | --- | --- |
Laying the groundwork for high-performance interpretable machine learning algorithms, we
begin by examining logistic regression, the preferred modeling technique in the industry.
Logisticregressionisastatisticalmodelthatestimatesthelog-oddsofaneventoccurringas
a linear combination of independent variables. The estimated log-odds is then transformed
into a probability that the event will take place. By setting a threshold for this probability,
logistic regression can be used as a binary classifier, where outcomes above and below the
| threshold | correspond |     | to two distinct |     | classes. |     |     |     |
| --------- | ---------- | --- | --------------- | --- | -------- | --- | --- | --- |
Briefly, logistic regression is a generalized linear model that estimates the probability of a
binary outcome:
|     |     |     |     | p=P(Y | =1|X=x), |     |     |     |
| --- | --- | --- | --- | ----- | -------- | --- | --- | --- |
whereX=(X ,X ,...,X )isthevectoroffeaturesandx=(x ,x ,...,x )isarealization
|     | 1   | 2   | d   |     |     |     | 1 2 d |     |
| --- | --- | --- | --- | --- | --- | --- | ----- | --- |
of these features. The logistic regression model provides an of given by
estimate p
1
|     |     |     |     | pˆ≜σ (cid:0) | z(β,x) (cid:1) | =   | ,   | (1) |
| --- | --- | --- | --- | ------------ | -------------- | --- | --- | --- |
1+e−z(β,x)
| where σ(·) | is the | sigmoid | function | and | the linear | component   | is  |     |
| ---------- | ------ | ------- | -------- | --- | ---------- | ----------- | --- | --- |
|            |        |         | z(β,x)=β |     | +β x       | +β x +···+β | x , |     |
|            |        |         |          |     | 0 1 1      | 2 2         | d d |     |
2

| with parameter |     | vector | β =(β | ,β ,...,β |     | ).  |     |     |
| -------------- | --- | ------ | ----- | --------- | --- | --- | --- | --- |
|                |     |        |       | 0 1       | d   |     |     |     |
The model is typically trained by minimizing the negative log-likelihood (log-loss) function:
|     |     |     |     | 1   | (cid:88)(cid:104) n |     |     | (cid:105) |
| --- | --- | --- | --- | --- | ------------------- | --- | --- | --------- |
(2)
|     |     |     | L(β)=− |     | y   | lnpˆ +(1−y | )ln(1−pˆ) | ,   |
| --- | --- | --- | ------ | --- | --- | ---------- | --------- | --- |
|     |     |     |        | n   |     | i i        | i         | i   |
i=1
where n is the number of training samples, y ∈ {0,1}, pˆ = σ(z(β,x )), and x is the i-th
|     |     |     |     |     |     | i   | i   | i i |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
feature vector. This cost function penalizes confident but incorrect predictions. Optimiza-
tion is usually performed via gradient descent or related algorithms to obtain parameter
| estimates | βˆ. |     |     |     |     |     |     |     |
| --------- | --- | --- | --- | --- | --- | --- | --- | --- |
One of the key advantages of logistic regression is interpretability. By rearranging Eq. (1)
| in terms | of fitted | log-odds, | we          | have      |     |      |              |         |
| -------- | --------- | --------- | ----------- | --------- | --- | ---- | ------------ | ------- |
|          |           |           | (cid:18) pˆ | (cid:19)  |     |      |              |         |
|          |           |           | ln          | =z(β,x)=β |     | 0 +β | 1 x 1 +···+β | d x d . |
1−pˆ
This expresses a linear relationship between the features and the log-odds of the positive
class. Holding all other features constant, a one-unit increase in feature x multiplies the
i
odds of being in the positive class by eβi . The intercept β represents the log-odds when all
0
| features | x ,x ,...,x |     | are zero, | corresponding |     | to odds | of eβ0 | .   |
| -------- | ----------- | --- | --------- | ------------- | --- | ------- | ------ | --- |
1 2 d
However,akeylimitationoflogisticregressionisthattheresultingmodelisoftentoosimple
toaccuratelycapturecomplexdatapatterns,whichmayleadtopoorperformancecompared
to more flexible ML models (Alonso & Carbo, 2020, 2021; De Lange et al., 2022; Moscatelli
| et al., 2019; | Schmitt, | 2024).      |     |     |     |        |     |     |
| ------------- | -------- | ----------- | --- | --- | --- | ------ | --- | --- |
| 3 Existing    |          | Explainable |     |     | AI  | Models |     |     |
There have been continuous advancements both in terms of complexity and capability of
machine learning algorithms in recent years. On the one hand, these algorithms enable
faster and more accurate data modeling; on the other, they pose challenges in terms of
| explainability | and | trust. |     |     |     |     |     |     |
| -------------- | --- | ------ | --- | --- | --- | --- | --- | --- |
In the existing literature, there are two main approaches in interpreting and explaining
ML models. The first approach is to use inherently interpretable methods - also known as
glass-box models - such as linear regression, decision trees, and generalized additive models
(GAMs). While these methods offer desirable transparency, their predictive performance
may be insufficient. The second approach involves model-agnostic interpretation tools that
can be applied to any supervised machine learning model, also known as post-hoc methods.
In the subsections that follow, we briefly recall some key post-hoc explainable AI (XAI)
methods, along with recent advances in glass-box models reported in the literature. These
| will lay     | the foundation |             | for the | approach |         | we will propose | in Section | 4.1. |
| ------------ | -------------- | ----------- | ------- | -------- | ------- | --------------- | ---------- | ---- |
| 3.1 Post-Hoc |                | Explanation |         |          | Methods |                 |            |      |
Intheliteratureofcreditscoring,twopost-hocexplainableXAImethodsaremostlystudied:
LocallyInterpretableModel-AgnosticExplanations(LIME)andSHapleyAdditiveexPlana-
tions (SHAP).
3

LIME, introduced by Ribeiro et al., 2016, provides explanations for individual predictions
by fitting a simple local model around the observation being explained, using similar data
points. The local model is typically chosen from interpretable classes such as linear models
| or decision | trees. |     |     |     |     |     |
| ----------- | ------ | --- | --- | --- | --- | --- |
SHAP, introduced by S. Lundberg and Lee, 2017, computes Shapley values and presents
them as an additive feature attribution method, which is effectively a linear model. A
notable advantage of SHAP is its visualization tools, including the SHAP summary plot
and dependence plot, which are very handy to use and greatly enhance the interpretation
| of the model | outcomes. |     |     |     |     |     |
| ------------ | --------- | --- | --- | --- | --- | --- |
OtherinterpretationmethodsincludePartialDependencePlots, AccumulatedLocalEffects
(ALE) Plots, Functional Decomposition, and Permutation Feature Importance, among oth-
ers. We will not explore these methods in this paper but refer the reader to Molnar, 2022
| for relevant | details. |     |     |     |     |     |
| ------------ | -------- | --- | --- | --- | --- | --- |
Here we elaborate further on SHAP, one of the most widely used methods for providing
global explanations of black-box models and a key component of our experiments. SHAP
is based on the Shapley values from game theory. More precisely, it uses Shapely values to
determine the contribution of each feature to a final prediction made by a model.
LetF ={1,2,...,d}bethesetofindicesforallfeatures,andletx∈Rd beafeaturevector.
For a given feature with number j ∈F, the Shapley value of this feature is defined as
|     |         | (cid:88) |S|!(|F|−|S|−1)! |     | (cid:104)   |        | (cid:105) |
| --- | ------- | ------------------------- | --- | ----------- | ------ | --------- |
|     | ϕ (x) = |                           |     | f (x        | )−f (x | ) ,       |
|     | j       |                           |     | S∪{j} S∪{j} | S      | S         |
|F|!
S⊆F\{j}
where|S|isthecardinalityofthesubsetS,i.e. thenumberofelementsinS;x ∈R|S| isthe
S
subvector of restricted to the indices in S; :R|S| →R denotes the model restricted to
|     | x   |     | f   |     |     |     |
| --- | --- | --- | --- | --- | --- | --- |
S
the feature set S (with all other features marginalized out or fixed according to a baseline).
|S|!(|F|−|S|−1)!
The weight w(S)= is the fraction of feature orderings in which the subset S
|F|!
| appears | before j. |     |     |     |     |     |
| ------- | --------- | --- | --- | --- | --- | --- |
The computational complexity for Shapley values grows exponentially in the number of
features. To address this issue, SHAP provides two efficient approximation methods for
Shapley values: model agnostic Kernel SHAP and tree-based Tree SHAP. The latter, intro-
duced in S. M. Lundberg et al., 2019, dramatically reduces computation time by exploiting
| the structure | of tree-based | models.     |          |              |     |     |
| ------------- | ------------- | ----------- | -------- | ------------ | --- | --- |
| 3.2 Black-box |               | Models with | Post-Hoc | Explanations |     |     |
One of the best performing black-box models for credit scoring - as well as for other appli-
cationsinfinancesuchastime-seriesprediction-isXGBoost(eXtremeGradientBoosting).
Alonso and Carbo (2021) showed that XGBoost, along with random forest, consistently
outperformed other models examined in terms of AUC-ROC. In addition, Jones et al., 2015
demonstrated that gradient boosting trees were among the top-performing ML classifiers
for the credit scoring task conducted in their study. Similar results were also reported by
| De Lange | et al. (2022) | and Moscatelli | et al. (2019). |     |     |     |
| -------- | ------------- | -------------- | -------------- | --- | --- | --- |
XGBoost is an optimized implementation of the gradient boosting framework developed
by Chen and Guestrin (2016). It constructs an ensemble of K regularized Classification
4

And Regression Trees (CARTs) to solve supervised learning tasks, including regression and
| classification. | The | prediction | for | an instance |     | is given | by  |     |     |     |
| --------------- | --- | ---------- | --- | ----------- | --- | -------- | --- | --- | --- | --- |
x i
K
|     |     |     |     | (cid:88) |      |      |     |     |     | (3) |
| --- | --- | --- | --- | -------- | ---- | ---- | --- | --- | --- | --- |
|     |     |     |     | yˆ =     | f (x | ), f | ∈F, |     |     |     |
|     |     |     |     | i        | k    | i    | k   |     |     |     |
k=1
where K is the number of trees, and F is the space of all CARTs. Each tree f maps the
k
inputfeaturevectorx ∈Rd toapredictedscore,andtheensemblepredictionisobtainedby
i
summing the outputs of all trees. The model is trained to minimize a regularized objective
function
|     |     |     |       | n        |           |     | K        |     |     |     |
| --- | --- | --- | ----- | -------- | --------- | --- | -------- | --- | --- | --- |
|     |     |     |       | (cid:88) |           |     | (cid:88) |     |     |     |
|     |     |     | L(ϕ)= |          | l(y ,yˆ)+ |     | Ω(f      | ).  |     |     |
|     |     |     |       |          | i         | i   | k        |     |     |     |
|     |     |     |       | i=1      |           |     | k=1      |     |     |     |
Here l is a differentiable convex loss function that quantifies the difference between the
ground truth and the prediction yˆ. It is squared error for regression and logistic loss
y
|     |     | i   |     | i   |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
for classification. For binary classification, the logistic loss corresponds to the negative
| log-likelihood, | which    | is very     | similar | to             | Eq. (2): |     |                     |     |                  |     |
| --------------- | -------- | ----------- | ------- | -------------- | -------- | --- | ------------------- | --- | ---------------- | --- |
|                 |          |             |         | (cid:104)      |          |     |                     |     | (cid:1)(cid:105) |     |
|                 |          | l(y         | ,yˆ)=−  | y lnσ(yˆ)+(1−y |          |     | )ln (cid:0) 1−σ(yˆ) |     | ,                |     |
|                 |          | i           | i       | i              | i        |     | i                   | i   |                  |     |
| where σ(·)      | is again | the sigmoid |         | function.      |          |     |                     |     |                  |     |
The second term, Ω(f), penalizes model complexity such that the model favors simpler
but predictive functions, and is given by Ω(f) = γT + 1λ∥w∥2, where T is the number of
leaves in the tree, is the vector of leaf weights, and 2 and are respective regularization
|     |     | w   |     |     |     |     | γ   | λ   |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
parameters.
(cid:80)
The objective function above is equivalent to L(t) = l(y ,yˆ(t−1)+f (x ))+Ω(f ), with
|     |     |     |     |     |     |     | i   | i i | t i | t   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
f (x ) being the CART added at iteration t. To simplify the optimization, a second-order
t i
| Taylor expansion |     | is applied | around | the | current | prediction | yˆ(t−1), | which | gives |     |
| ---------------- | --- | ---------- | ------ | --- | ------- | ---------- | -------- | ----- | ----- | --- |
i
|     |     |        | (cid:88)(cid:104) |             |     |         |         | (cid:105) |     |     |
| --- | --- | ------ | ----------------- | ----------- | --- | ------- | ------- | --------- | --- | --- |
|     |     | L(t) ≃ | l(y               | ,yˆ(t−1))+g |     | f (x )+ | 1h f2(x | ) +Ω(f    | ),  |     |
|     |     |        |                   | i i         | i   | t i     | 2 i t   | i         | t   |     |
i
where
|          |          |       |             | ,yˆ(t−1)) |          |     | ∂2l(y ,yˆ(t−1)) |           |     |     |
| -------- | -------- | ----- | ----------- | --------- | -------- | --- | --------------- | --------- | --- | --- |
|          |          |       |             | ∂l(y i    |          |     | i               |           |     |     |
|          |          |       | g =         | i         | ,        | h = |                 | i .       |     |     |
|          |          |       | i           | ∂yˆ(t−1)  |          | i   | ∂(yˆ(t−1))2     |           |     |     |
|          |          |       |             | i         |          |     | i               |           |     |     |
| Dropping | constant | terms | independent | of        | f yields | the | simplified      | objective |     |     |
t
|     |     |     |                  | (cid:88)(cid:104) |       |       | (cid:105)  |     |     |     |
| --- | --- | --- | ---------------- | ----------------- | ----- | ----- | ---------- | --- | --- | --- |
|     |     |     | L(cid:101) (t) ≃ | g f               | (x )+ | 1 h f | 2(x ) +Ω(f | ).  |     |     |
|     |     |     |                  | i                 | t i   | 2 i   | t i        | t   |     |     |
i
| For the logistic |     | loss, these   | derivatives | are | explicitly  |     |                      |     |         |     |
| ---------------- | --- | ------------- | ----------- | --- | ----------- | --- | -------------------- | --- | ------- | --- |
|                  |     | =σ(yˆ(t−1))−y |             |     | =σ(yˆ(t−1)) |     | (cid:0) 1−σ(yˆ(t−1)) |     | (cid:1) |     |
|                  |     | g             |             | ,   | h           |     |                      |     | .       |     |
|                  |     | i             | i           | i   | i           | i   |                      | i   |         |     |
Sincegradientboostingmodelsconsistofanensembleofdecisiontrees,whereeachtreemay
utilize multiple features to make predictions, it is challenging to gauge the contribution of
| individual | features | to the | model’s | predictions. |     |     |     |     |     |     |
| ---------- | -------- | ------ | ------- | ------------ | --- | --- | --- | --- | --- | --- |
5

To address this model transparency issue, XGBoost library is equipped with several fea-
ture importance metrics that can be used to obtain more knowledge on the model’s inner
workings. The most commonly used metric is the gain, which measures how much a feature
improvesthemodel’sobjectivefunction(e.g.,byreducingerrororloss)whenitisusedfora
split. Featureswithhighergainvaluesareconsideredmoreimportant,sincetheycontribute
more to improving the model’s accuracy. Another metric is cover, which reflects how many
training samples are influenced by a split using a particular feature. In practice, this means
thatfeaturesusedhigherupinthetrees,whichaffectlargergroupsofsamples,tendtohave
higher cover values. The last metric is frequency, which simply counts how often a feature
is used to split the data across all trees in the model. A higher frequency indicates that the
feature is frequently chosen as a useful splitting criterion.
Although these feature importance metrics provide some insight into which features the
model relies on most, they miss several key aspects. First, none of these metrics explains
how a feature influences the model’s prediction. In other words, they do not reveal how a
change in the value of a specific feature would affect the output. For example, would an
increaseinaparticularfeaturemakeaclientmorelikelytodefault,orwoulditmaketheloan
appear safer? Secondly, these metrics do not offer intuition about the model’s behavior in
the absence of a feature. Would the predictions of the model change significantly if certain
features were excluded? Lastly, they fail to capture the impact of interactions between
features on the final prediction.
These limitations underscore the need for more advanced tools such as SHAP to interpret
the inner workings of complex models. As noted earlier, especially the Tree SHAP method
is particularly designed for fast calculation of Shapley values for tree-based models.
XAImodelsthatcombineensembletree-basedalgorithmswithSHAPhavebecomeincreas-
inglyprevalentinrecentcreditscoringliterature, asdemonstratedbyMishevaetal.(2021),
Zhu et al. (2024), and Alonso and Carbo (2021).
3.3 Glass-Box Models from Recent Years
At the other end of the transparency spectrum are the glass-box models. This category
includes traditional methods such as regression and decision trees, as well as more recent
models that incorporate additional complexity while maintaining transparency.
Our literature review identifies two glass-box models from recent years that show promis-
ingperformance: ExplainableBoostingMachine(EBM)andExplainableBoostingMachine
(EBM) and Penalized Logistic Tree Regression (PLTR). EBM, developed by Nori et al.
(2019), is a supervised machine learning algorithm specifically designed to balance inter-
pretability and predictive power. It offers model intelligibility while achieving accuracy
comparable to state-of-the-art algorithms such as XGBoost. PLTR, introduced by Du-
mitrescu et al. (2022), uses predictors derived from shallow decision trees as inputs to a
penalized logistic regression, offering a hybrid approach that enhances both interpretability
and predictive performance.
3.3.1 Explainable Boosting Machine (EBM)
The EBM algorithm belongs to the family of generalized additive models (GAMs), which
extend generalized linear models (GLMs) by modeling the expected value of the target
variable as a sum of smooth, non-linear functions of the predictors.
6

EBM trains the model iteratively in a round-robin fashion: in each iteration, a small tree
is fitted to capture the effect of one feature on the residuals, and the residuals are updated
accordingly. This process is repeated across the features one by one, completing one round-
robinpassthroughthedataset. Asmalllearningrateensuresthattheorderinwhichfeatures
areincludeddoesnotsignificantlyinfluencethefinalmodel. Asaresult,thetrainingprocess
requires many iterations, as many as ten thousand, to reach convergence. The result is an
ensemble of small trees per feature, which can be aggregated collectively to capture the
| relationship    | between |        | the feature | and        | each     | target | variable. |     |     |     |
| --------------- | ------- | ------ | ----------- | ---------- | -------- | ------ | --------- | --- | --- | --- |
| In mathematical |         | terms, | the         | prediction | function |        | reads     |     |     |     |
d
|     |     |     |     |           |     |     | (cid:88) |         |     | (4) |
| --- | --- | --- | --- | --------- | --- | --- | -------- | ------- | --- | --- |
|     |     |     |     | g(E[Y])=β |     | 0 + | f j      | (x j ), |     |     |
j=1
where is a link function and each denotes a smooth function representing the effect of
| g   |     |     |     |     | f   |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
j
j-th feature, i.e. x , on the target variable. Worth noting that, the difference between Eq.
j
(4) and Eq. (3) is that the functions involved in EBM prediction are uni-variate functions,
while those involved in XGBoost take multiple features as inputs. Each marginal function
f (·) is stored after training and can be visualized in plots. These stored functions are
j
| eventually | used | for predictions |     | later | on. |     |     |     |     |     |
| ---------- | ---- | --------------- | --- | ----- | --- | --- | --- | --- | --- | --- |
Building on this concept, Lou et al. (2013) introduced Generalized Additive Model plus
Interactions (GA2M), which incorporates pairwise feature interactions as follows:
d
|     |     |     |           |     | (cid:88) |      | (cid:88) |     |         |     |
| --- | --- | --- | --------- | --- | -------- | ---- | -------- | --- | ------- | --- |
|     |     |     | g(E[Y])=β |     | +        | f (x | )+       | f   | (x ,x ) | (5) |
|     |     |     |           | 0   |          | j j  |          | j,q | j q     |     |
|     |     |     |           |     | j=1      |      | 1≤j<q≤d  |     |         |     |
Despite the added complexity, GA2Ms remain interpretable due to their additive structure
and the use of small CARTs or shallow trees to model each term. EBM can identify and
incorporate feature interactions by training pairwise interaction terms, if enabled, using a
| similar iterative |     | process | but | built | on Eq. | (5). |     |     |     |     |
| ----------------- | --- | ------- | --- | ----- | ------ | ---- | --- | --- | --- | --- |
Finally, the EBM library generates visualizations that illustrate feature importance and
| interactions | that | provide | insights | into | the | model’s | inner | workings. |     |     |
| ------------ | ---- | ------- | -------- | ---- | --- | ------- | ----- | --------- | --- | --- |
Testing results in Dessain et al., 2023 show that EBM performs comparably to black-box
gradient boosting models, such as XGBoost. This result appears to be consistent in models
| used outside | the       | scope    | of credit | scoring |            | and finance | (Caruana |     | et al., 2015). |     |
| ------------ | --------- | -------- | --------- | ------- | ---------- | ----------- | -------- | --- | -------------- | --- |
| 3.3.2        | Penalized | Logistic |           | Tree    | Regression |             | (PLTR)   |     |                |     |
The other powerful and explainable model is called Penalized Logistic Tree Regression, or
PLTR for short. It is introduced in Dumitrescu et al., 2022 for a credit scoring model. The
| model is | constructed |     | in two | steps. |     |     |     |     |     |     |
| -------- | ----------- | --- | ------ | ------ | --- | --- | --- | --- | --- | --- |
In the first step, binary features are created using short-depth decision trees with one or
two splits. Based on single-split trees, each feature generates a new binary feature ν(j)
x j
for logistic regression, which takes the value 1 if the j-th feature of the i-th sample exceeds
the threshold from the single-split tree, and 0 otherwise. From two-split trees involving two
features and , with assumed to be more informative, we first define ν(j) as in the
|     | x   | x   | x   |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|     | j   | q   | j   |     |     |     |     |     |     |     |
single-split case, then we define a second binary feature ξ(j,q), which takes the value 1 if x
j
7

is below its threshold and x is above its threshold. The final set of features used in the
q
model thus consists of original set of features , binary features from the single-split trees
x j
| ν(j), and | binary features | from the two-split | trees ξ(j,q). |     |     |     |
| --------- | --------------- | ------------------ | ------------- | --- | --- | --- |
Inthesecondstep,apenalizedlogisticregressionisappliedtothisexpandedsetoffeatures.
| Recall the | logistic | regression log-likelihood | in Eq. | (2), we have |     |     |
| ---------- | -------- | ------------------------- | ------ | ------------ | --- | --- |
n
|     |       | 1 (cid:88)(cid:104) |          |                | (cid:105) |     |
| --- | ----- | ------------------- | -------- | -------------- | --------- | --- |
|     | L(θ)= | y ln[σ(z(θ,x˜       | ))]+(1−y | )ln[1−σ(z(θ,x˜ | ))] ,     | (6) |
|     |       | n i                 | i        | i              | i         |     |
i=1
where is the extended feature vector from the i-th sample, containing all , ν(j) and
| x˜         |          |                       |              |             | x   |     |
| ---------- | -------- | --------------------- | ------------ | ----------- | --- | --- |
|            | i        |                       |              |             | j   | i   |
| ξ(j,q) for | all ̸=q, | and is the respective | set of model | parameters. |     |     |
|            | j        | θ                     |              |             |     |     |
i
Topreventover-fitting,weintroduceregularizationorpenalizationbyaddingapenaltyterm
| to the negative | log-likelihood | function: |     |     |     |     |
| --------------- | -------------- | --------- | --- | --- | --- | --- |
L˜(θ)=−L(θ)+λP(θ),
where P(θ) is the additional penalty term and λ is the tuning parameter controlling the
strength of the penalty. There are many choices of P(θ), Zou, 2006 proposed the adaptive
lasso estimator.
| 4 Comparing |     | the Models, | Is There | a Silver | Bullet? |     |
| ----------- | --- | ----------- | -------- | -------- | ------- | --- |
As summarized in the discussion paper from European Banking Authority, 2023, a cen-
tral challenge in applying machine learning techniques to regulated areas such as IRB PD
modelingliesintheircomplexity,whichhindersexplainability. Inparticular,thatdiscussion
paperrecommendsinstitutionstoavoid,amongothers,includinganexcessivenumberofex-
planatory drivers or drivers with no significant predictive information, and overly complex
| modeling | choices if | simpler approaches | yielding similar | results are available. |     |     |
| -------- | ---------- | ------------------ | ---------------- | ---------------------- | --- | --- |
While existing XAI approaches, such as combining black-box models with post-hoc inter-
pretability tools like SHAP, provide some insights and certain level of understanding of the
model behaviors, they do not automatically meet those guidelines. These models typically
involve a large number of features. Nonlinear behaviors combined with numerous feature
interactions are difficult to interpret and communicate, particularly for model owners and
regulatory supervisors. Even when using inherently interpretable models like EBM, intro-
ducing feature interactions can result in patterns that defy financial intuition.
To address this gap, we propose a hybrid approach that leverages the feature rankings pro-
duced by post-hoc interpretability tools applied to black-box models, and then uses these
insightstoconstructinterpretable,glass-boxmodels. Thismethodmaintainspredictiveper-
formance while significantly reducing model complexity and feature count. The resulting
model based on the proposed approach is potentially more suitable for regulated environ-
| ments than | existing | XAI models. |     |     |     |     |
| ---------- | -------- | ----------- | --- | --- | --- | --- |
In the following subsections, we present the proposed method, describe the dataset and
experimental setup, compare our lightweight models against benchmarks in terms of both
accuracy and interpretability, and finally show how domain expertise and further analyses
(e.g., feature interactions and correlations) can be used to fine-tune the model.
8

| 4.1 Our    | Proposal |           |           |     |     |     |     |     |
| ---------- | -------- | --------- | --------- | --- | --- | --- | --- | --- |
| We propose | the      | following | approach: |     |     |     |     |     |
- Step1: trainawellperformingblack-boxmachinelearningmodelusingthefullfeature
set. Thiswenameasthe“base” model,whichservesbothasaperformancebenchmark
| as  | well as | the basis | for | feature | selection | for step | 2.  |     |
| --- | ------- | --------- | --- | ------- | --------- | -------- | --- | --- |
- Step 2: rank features by their importance in the base model, by for example applying
| a post-hoc |     | interpretation |     | tool | like SHAP. |     |     |     |
| ---------- | --- | -------------- | --- | ---- | ---------- | --- | --- | --- |
- Step 3: select a few, such as 10 or 20, top-ranked features to train a glass-box model,
| which | can | be EBM | or  | PLTR | for example. |     |     |     |
| ----- | --- | ------ | --- | ---- | ------------ | --- | --- | --- |
- Step 4: based on interaction analysis, correlation analysis, and/or expert opinion,
| refine | the | selection | of  | top-ranked | features | and | repeat | step 3. |
| ------ | --- | --------- | --- | ---------- | -------- | --- | ------ | ------- |
The result is explainable and technically transparent models that better align with the
| expectations | of  | both regulators |     | and | practitioners | in  | the credit | risk domain. |
| ------------ | --- | --------------- | --- | --- | ------------- | --- | ---------- | ------------ |
To evaluate the potential of this approach for credit scoring, we used the top-performing
| classifiers | introduced |     | in Section | 3.2 | as benchmarks. |     |     |     |
| ----------- | ---------- | --- | ---------- | --- | -------------- | --- | --- | --- |
Note that, as our goal is to propose a general method to simplify and "glassify" black-box
models while preserving their predictive power, we did not extensively optimize the base
models. Nor did we aim to reconfirm that tree boosting algorithms outperform logistic
| regression | in credit   | scoring |     | - an already | well-established |        | result. |     |
| ---------- | ----------- | ------- | --- | ------------ | ---------------- | ------ | ------- | --- |
| 4.2 Data   | Preparation |         |     | and          | Base             | Models |         |     |
Our experiments were based on data from the Lending Club peer-to-peer lending platform,
which operated until the end of 2020. This dataset has been widely used in prior studies on
explainable machine learning methods, allowing us to compare against established methods
and focus on persistent challenges in interpreting ML models in financial applications.
We preprocessed Lending Club data following similar steps to those taken in Ariza-Garzon
et al. (2020). As for the target variable, we decided to consider only ‘Fully Paid’ and
‘Charged Off’ categories of the variable loan_amount, encoding them as 0 and 1 respec-
tively. We also took the average of fico_range_high and fico_range_low to create the fea-
ture fico_range_low, while removing the original features. The features home_ownership,
purpose, addr_state and emp_length were encoded using one-hot encoding. Where neces-
sary, missing values were imputed with the mean of the corresponding feature.
Thesplitbetweentrainingdataandtestdatawasdonebasedonissue_d feature,suchthat
the train data consisted of data up to July 2015, and the test set consisted of data from
August 2015 to December 2018. The overall default rate observed in the data was around
20%, and the total number of features was 87. Using the preprocessed data, we built three
baseline models employing the algorithms previously discussed: logistic regression (LR),
XGBoost(XGB)andEBM.Sincethedataathandisimbalanced-inthesensethatthede-
faultingclassissignificantlysmallerthanthenon-defaultingclass,weassignedclassweights
toeachmodel. Thisapproachtypicallyenhancesthemodel’sabilitytocorrectlyclassifythe
minority class, often at the expense of performance on the majority class. However, in the
9

|     | Model |                | AUPRC  | AUROC   |        | F1 score Balanced | Accuracy           |
| --- | ----- | -------------- | ------ | ------- | ------ | ----------------- | ------------------ |
|     |       | LR             | 0.3389 | 0.6653  |        | 0.42              | 0.6187             |
|     | XGB   |                | 0.3436 | 0.6687  |        | 0.4160            | 0.6203             |
|     | EBM   |                | 0.3518 | 0.6744  |        | 0.4211            | 0.6251             |
|     | Table | 1: Performance |        | of base | models | (with all         | features included) |
context of credit risk modeling, prioritizing the accurate identification of default events is
| both acceptable |     | and desirable. |     |     |     |     |     |
| --------------- | --- | -------------- | --- | --- | --- | --- | --- |
For evaluating the performance of the different models, we used multiple performance met-
rics. However, we placed greater emphasis on metrics that appropriately account for the
performance on the minority class. In addition to balanced accuracy, we included AUROC
(Area Under the Receiver Operating Characteristic curve), F1 scores and AUPRC (Area
| Under the | Precision | Recall | Curve). |     |     |     |     |
| --------- | --------- | ------ | ------- | --- | --- | --- | --- |
Table1summarizestheperformanceofthemodelswhichweaimtopreserveinoursimplified,
| interpretable | approach. |              |     |      |        |     |     |
| ------------- | --------- | ------------ | --- | ---- | ------ | --- | --- |
| 4.3 Issue     | in        | Interpreting |     | Base | Models |     |     |
Given the volume of features and the complex, implicit interactions captured by the model,
validating whether the model’s decisions align with domain knowledge becomes a daunting
task. Top features identified by SHAP can help in explaining the scoring result for each
individual client. However, it is challenging to explain how much the interactions between
features affect the final score and why a large number of features are still needed.
Moreover, even when using inherently interpretable models like EBM, introducing feature
interactions can result in patterns that defy financial intuition. As shown in Figure 1, the
model suggests that applicants with lower loan amounts and higher salaries are more likely
to default than those with higher loan amounts and lower salaries. This contradicts basic
financial reasoning. However, when we examine the individual effects of these two features,
loan amount and annual income, separately, their impact aligns much more closely with
| human expectations |     | and | established | financial |     | logic. |     |
| ------------------ | --- | --- | ----------- | --------- | --- | ------ | --- |
As illustrated in Figure 2 and Figure 3, we observe a clear and intuitive trend: higher loan
amounts are generally associated with a higher probability of default, while higher annual
incomes correspond to a lower probability of default. This motivates us to largely reduce
the number of features, aligning with the guidelines given by earlier mentioned discussion
| paper, so   | as to minimize |            | feature | interactions. |     |     |     |
| ----------- | -------------- | ---------- | ------- | ------------- | --- | --- | --- |
| 4.4 Feature |                | Importance |         |               |     |     |     |
Having built the three base models, we now proceed to Step 2 as described in Section 4.1,
| where we | rank the | features | based | on their | importance. |     |     |
| -------- | -------- | -------- | ----- | -------- | ----------- | --- | --- |
For the logistic regression (LR) model, feature importance is determined using the model
coefficients after normalizing the input features. In the case of XGBoost, we rely on tree-
SHAPvaluestoobtainfeatureattributions. FortheEBMmodel,weuseitsinherentfeature
importance scores. The resulting feature rankings are summarized in Table 2. They are
10

|      | Figure                | 1: Loan | amount | and annual          | income feature | interaction | (from SHAP)         |
| ---- | --------------------- | ------- | ------ | ------------------- | -------------- | ----------- | ------------------- |
| Rank | LR                    |         |        | XGB                 |                |             | EBM                 |
|      | 1 fico_range_high     |         |        | fico_range_high     |                |             | loan_amnt           |
|      | 2 loan_amnt           |         |        | loan_amnt           |                |             | fico_range_high     |
|      | 3 dti                 |         |        | annual_inc          |                |             | annual_inc          |
|      | 4 annual_inc          |         |        | dti                 |                |             | purpose_credit_card |
|      | 5 home_ownership_RENT |         |        | purpose_credit_card |                |             | dti                 |
6 purpose_credit_card home_ownership_RENT purpose_debt_consolid.
|     | 7 emp_length_nan |     |     | home_ownership_MORT. |     |     | home_ownership_RENT |
| --- | ---------------- | --- | --- | -------------------- | --- | --- | ------------------- |
8 purpose_debt_consolid. purpose_debt_consolid. home_ownership_MORT.
|     | 9 purpose_other  |     |       | emp_length_nan  |              |        | emp_length_nan |
| --- | ---------------- | --- | ----- | --------------- | ------------ | ------ | -------------- |
|     | 10 adde_state_NY |     |       | adde_state_NY   |              |        | adde_state_NY  |
|     |                  |     | Table | 2: Top features | in different | models |                |
largely consistent across all three models, with only minor differences in the ordering (note
| that | for EBM, | interaction | terms | were initially | excluded | from | the ranking). |
| ---- | -------- | ----------- | ----- | -------------- | -------- | ---- | ------------- |
Remark: Among the three, XGBoost provided the fastest computation of feature impor-
| tance, | making       | it a | practical choice | for feature | selection. |     |     |
| ------ | ------------ | ---- | ---------------- | ----------- | ---------- | --- | --- |
| 4.5    | Light-weight |      | Glass-box        | Models      |            |     |     |
After obtaining the feature importance rankings discussed above, we proceeded to build
glass-box models using subsets of the top-ranked features of varying sizes, i.e. Step 3 of our
approach as described in Section 4.1. The glass-box models we considered were EBM and
PLTR.
By plotting performance metrics against the number of included features, we could identify
apracticalcut-offpointforconstructingareducedmodel. Figure4displaystheprogression
of AUPRC, AUROC, and F1 scores as a function of the number of features. In the case of
the Lending Club data, we observe that adding more than 10 features yields no substantial
improvement in model performance. This insight allowed us to reduce the dimensionality
from 86 features to just 10, without significantly compromising predictive power.
11

|     |     | Figure | 2:  | Loan amount | attribution | (from SHAP) |
| --- | --- | ------ | --- | ----------- | ----------- | ----------- |
Notably,EBMconsistentlyachievesperformancethatisatleastonparwithXGBoost,while
offering significantly greater transparency. PLTR also improves interpretability relative to
XGBoost but underperforms compared to both EBM and XGBoost in terms of predictive
accuracy. As a result, EBM emerges as the most favorable model in our study, providing a
| strong balance | between |     | explainability | and | performance. |     |
| -------------- | ------- | --- | -------------- | --- | ------------ | --- |
4.6 Refinements
Once the reduced EBM model is obtained, both global and local analyses can be conducted
with ease. Since EBM stores all marginal functions used in its predictions and the reduced
EBM model uses a limited number of features, interpreting the model becomes straightfor-
ward. These insights can, in turn, be used to further refine and enhance the model.
| 4.6.1 Feature |     | Interaction |     | Analysis |     |     |
| ------------- | --- | ----------- | --- | -------- | --- | --- |
As shown earlier, even pairwise interactions can lead to counterintuitive or misleading con-
| clusions, | like in the | case | of the | Lending Club | data. |     |
| --------- | ----------- | ---- | ------ | ------------ | ----- | --- |
To further assess the impact of pairwise interactions on model performance, we built a
series of ancillary models, each incorporating a different number of pairwise interactions,
ranging from zero up to nine. Figure 5 summarizes the different performance metrics as a
function of the number of pairwise interactions from these ancillary models. The maximum
improvement was measured using F1 score and amounted to 0.4% when all nice pair-wise
interactions were included, which is a very marginal gain. This analysis suggests that, in
some cases, practitioners may confidently exclude all feature interactions and still obtain a
| glass-box | model | that outperforms |     | the logistic | regression | benchmark. |
| --------- | ----- | ---------------- | --- | ------------ | ---------- | ---------- |
12

|     | Figure | 3: Annual | income attribution | (from SHAP) |
| --- | ------ | --------- | ------------------ | ----------- |
Figure 4: Sensitivity analysis: Performance w.r.t. the number of (top) features included
| 4.6.2 Correlation | Analysis |     |     |     |
| ----------------- | -------- | --- | --- | --- |
It is important to note that while SHAP analysis provides a robust, data-driven estimation
offeatureimportance,italsohascertainlimitations. Anotableweaknessliesinitshandling
of correlated features. When features are highly correlated, SHAP sometimes distributes
a positive SHAP value to one of the correlated pair, while a negative SHAP value to the
other, or distribute the importance across them. This makes it difficult to fully trust the
topfeaturelistselectedusingSHAP.Tomitigatethislimitation, werecommendtocombine
| SHAP with | correlation | analysis. |     |     |
| --------- | ----------- | --------- | --- | --- |
We computed the correlation matrix among the top 25 most important features identified
by SHAP. For each pair of highly correlated features, we removed the lower-ranked one if
it was not among the top 10 most important features. This process was repeated until we
obtained a revised set of 20 features. It is important to note that we never removed any of
theoriginaltop10SHAP-rankedfeatures,eveniftheywerepartofahighlycorrelatedpair.
Empirical results show that removing one of the top 10 features often leads to a decline in
model performance, supporting the decision to keep them. The results in the Table 3 also
| suggested that | this method | can imporve | the performance | of the model. |
| -------------- | ----------- | ----------- | --------------- | ------------- |
13

Figure 5: Sensitivity analysis: EBM performance w.r.t the number of pairwise interactions
| Model           | Method   | AUPRC AUROC   | F1 score Balanced | Accuracy |
| --------------- | -------- | ------------- | ----------------- | -------- |
| XGB             | Original | 0.3412 0.6641 | 0.4139            | 0.6185   |
| XGB Correlation | Analysis | 0.3418 0.6658 | 0.4145            | 0.6190   |
| EBM             | Original | 0.3487 0.6720 | 0.4186            | 0.6226   |
| EBM Correlation | Analysis | 0.3493 0.6725 | 0.4193            | 0.6233   |
Table 3: Performance comparison for XGBoost and EBM: using original top 20 features
without correlation analysis vs using top 20 features after correlation analysis
5 Conclusion
In this study, we proposed an approach that has the potential to assist banks and financial
institutionsindevelopingmoretransparentandreliablemodelswithfewerfeatures,meeting
both practical needs and regulatory expectations for Probability of Default (PD) models.
UsingtheLendingClubdataset,wedemonstratedthat,followingourapproach,itispossible
to construct a lightweight glass-box model comprising only a small subset of features, while
achieving predictive performance comparable to a black-box model utilizing the full feature
set.
Forfutureresearch,werecommendtestingtheeffectivenessandrobustnessofthisapproach
across diverse datasets to validate its generalizability and applicability in varied financial
contexts.
| Declaration | of Interest |     |     |     |
| ----------- | ----------- | --- | --- | --- |
Theauthorsreportnoconflictsofinterest. Theauthorsaloneareresponsibleforthecontent
| and writing of | the paper. |     |     |     |
| -------------- | ---------- | --- | --- | --- |
References
Alonso,A.,&Carbo,J.M.(2020).MachineLearninginCreditRisk:MeasuringtheDilemma
Between Prediction and Supervisory Cost. Journal. https://doi.
SSRN Electronic
org/10.2139/ssrn.3724374
Alonso, A., & Carbo, J. M. (2021). Understanding the Performance of Machine Learning
Models to Predict Credit Default: A Novel Approach for Supervisory Evaluation.
| SSRN | Electronic Journal. | https://doi.org/10.2139/ssrn.3774075 |     |     |
| ---- | ------------------- | ------------------------------------ | --- | --- |
14

Ariza-Garzon,M.J.,Arroyo,J.,Caparrini,A.,&Segovia-Vargas,M.-J.(2020).Explainabil-
| ity of a Machine | Learning | Granting Scoring | Model in Peer-to-Peer | Lending. |     |
| ---------------- | -------- | ---------------- | --------------------- | -------- | --- |
IEEE
| Access, 8, | 64873–64890. https://doi.org/10.1109/ACCESS.2020.2984412 |     |     |     |     |
| ---------- | -------------------------------------------------------- | --- | --- | --- | --- |
Caruana, R., Lou, Y., Gehrke, J., Koch, P., Sturm, M., & Elhadad, N. (2015). Intelligible
Models for HealthCare: Predicting Pneumonia Risk and Hospital 30-day Readmis-
sion.Proceedingsofthe21thACMSIGKDDInternationalConferenceonKnowledge
|           | Mining,  | 1721–1730. https://doi.org/10.1145/2783258.2788613 |     |     |     |
| --------- | -------- | -------------------------------------------------- | --- | --- | --- |
| Discovery | and Data |                                                    |     |     |     |
Chen,T.,&Guestrin,C.(2016).XGBoost:AScalableTreeBoostingSystem[arXiv:1603.02754
[cs]]. Proceedings of the 22nd ACM SIGKDD International Conference on Knowl-
|                |          | Mining, 785–794. | https://doi.org/10.1145/2939672. |     |     |
| -------------- | -------- | ---------------- | -------------------------------- | --- | --- |
| edge Discovery | and Data |                  |                                  |     |     |
2939785
| Comment: | KDD’16 changed | all figures to | type1. |     |     |
| -------- | -------------- | -------------- | ------ | --- | --- |
DeLange,P.E.,Melsom,B.,VennerÃžd,C.B.,&Westgaard,S.(2022).ExplainableAIfor
Credit Assessment in Banks. Journal of Risk and Financial Management, 15(12),
556. https://doi.org/10.3390/jrfm15120556
Dessain, J., Bentaleb, N., & Vinas, F. (2023). Cost of Explainability in AI: An Example
with Credit Scoring Models [Series Title: Communications in Computer and Infor-
| mationScience].InL.Longo(Ed.),Explainable |     |     |                         | (pp.498–516, |     |
| ----------------------------------------- | --- | --- | ----------------------- | ------------ | --- |
|                                           |     |     | Artificial Intelligence |              |     |
Vol.1901).SpringerNatureSwitzerland.https://doi.org/10.1007/978-3-031-44064-
9_26
Dumitrescu, E., Hué, S., Hurlin, C., & Tokpavi, S. (2022). Machine learning for credit
scoring:Improvinglogisticregressionwithnon-lineardecision-treeeffects.European
|            | Research,   | 297(3), | 1178–1192. |     |     |
| ---------- | ----------- | ------- | ---------- | --- | --- |
| Journal of | Operational |         |            |     |     |
European Banking Authority. (2023, August). Machine learning for irb models: Follow-up
report from the consultation on the discussion paper on machine learning for irb
models [Accessed: 2025-05-25]. https://www.eba.europa.eu/sites/default/files/
document_library/Publications/Reports/2023/1061483/Follow-up%20report%
20on%20machine%20learning%20for%20IRB%20models.pdf
European Banking Authority. (2024, November). Risk assessment report - november 2024
| (Report). | European Banking | Authority. |     |     |     |
| --------- | ---------------- | ---------- | --- | --- | --- |
Jones, S., Johnstone, D., & Wilson, R. (2015). An empirical evaluation of the performance
of binary classifiers in the prediction of credit ratings changes. Journal of Banking
| Finance, | 56, 72–85. https://doi.org/10.1016/j.jbankfin.2015.02.006 |     |     |     |     |
| -------- | --------------------------------------------------------- | --- | --- | --- | --- |
&
Lou, Y., Caruana, R., Gehrke, J., & Hooker, G. (2013). Accurate intelligible models with
pairwise interactions.
|     | Proceedings | of the 19th | ACM SIGKDD | international | confer- |
| --- | ----------- | ----------- | ---------- | ------------- | ------- |
ence on Knowledge discovery and data mining, 623–631. https://doi.org/10.1145/
2487575.2487579
Lundberg, S., & Lee, S.-I. (2017, November). A Unified Approach to Interpreting Model
Predictions [arXiv:1705.07874 [cs]]. https://doi.org/10.48550/arXiv.1705.07874
| Comment: | To appear in NIPS | 2017. |     |     |     |
| -------- | ----------------- | ----- | --- | --- | --- |
Lundberg,S.M.,Erion,G.G.,&Lee,S.-I.(2019,March).ConsistentIndividualizedFeature
Attribution for Tree Ensembles [arXiv:1802.03888 [cs]]. https://doi.org/10.48550/
arXiv.1802.03888
| Comment: | Follow-up to 2017 | ICML Workshop | arXiv:1706.06060. |     |     |
| -------- | ----------------- | ------------- | ----------------- | --- | --- |
Misheva,B.H.,Osterrieder,J.,Hirsa,A.,Kulkarni,O.,&Lin,S.F.(2021,March).Explain-
able AI in Credit Risk Management [arXiv:2103.00949 [q-fin]]. https://doi.org/10.
48550/arXiv.2103.00949
15

Molnar, C. (2022). Interpretable machine learning: A guide for making black box models ex-
|     | [Available | online: https://christophm.github.io/interpretable-ml-book/]. |     |     |     |
| --- | ---------- | ------------------------------------------------------------- | --- | --- | --- |
plainable
Lulu.com.
Moscatelli, M., Narizzano, S., Parlapiano, F., & Viggiano, G. (2019, December). Corporate
|         |                                              |              | learning. Banca | d’Italia. Retrieved | December 12, |
| ------- | -------------------------------------------- | ------------ | --------------- | ------------------- | ------------ |
| default | forecasting                                  | with machine |                 |                     |              |
| 2024,   | from https://doi.org/10.32057/0.TD.2019.1256 |              |                 |                     |              |
Nori, H., Jenkins, S., Koch, P., & Caruana, R. (2019, September). InterpretML: A Unified
Framework for Machine Learning Interpretability [arXiv:1909.09223 [cs]]. https://
doi.org/10.48550/arXiv.1909.09223
Ribeiro, M. T., Singh, S., & Guestrin, C. (2016, August). "Why Should I Trust You?":
Explaining the Predictions of Any Classifier [arXiv:1602.04938 [cs]]. https://doi.
org/10.48550/arXiv.1602.04938
Schmitt, M. (2024, February). Explainable Automated Machine Learning for Credit Deci-
sions:EnhancingHumanArtificialIntelligenceCollaborationinFinancialEngineer-
| ing | [arXiv:2402.03806 | [q-fin]]. https://doi.org/10.48550/arXiv.2402.03806 |     |     |     |
| --- | ----------------- | --------------------------------------------------- | --- | --- | --- |
Zhu, M., Zhang, Y., Gong, Y., Xing, K., Yan, X., & Song, J. (2024, February). Ensemble
Methodology:InnovationsinCreditDefaultPredictionUsingLightGBM,XGBoost,
and LocalEnsemble [arXiv:2402.17979 [cs]]. https://doi.org/10.48550/arXiv.2402.
17979
| Zou, H. (2006). | The adaptive | lasso and            | its oracle properties. |            |                   |
| --------------- | ------------ | -------------------- | ---------------------- | ---------- | ----------------- |
|                 |              |                      |                        | Journal of | the American sta- |
| tistical        | association, | 101(476), 1418–1429. |                        |            |                   |
16