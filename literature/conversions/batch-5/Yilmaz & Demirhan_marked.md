---
conversion_metadata:
  converted_at: "2026-07-21T09:29:58Z"
  converter_tool: "markitdown"
  converter_version: "0.1.6"
  source_pdf: "Yilmaz & Demirhan.pdf"
  source_pdf_sha256: "22d2e950ad4e14666b906e604af1ac90882f7b6f780901e44ec9deb9accce010"
  page_count: 16
  markdown_char_count: 189584
---

<!-- PAGE-AWARE EXTRACTION (via pdfminer.six) -->

<!-- PAGE 1 -->

Applied Soft Computing 134 (2023) 110020

Contents lists available at ScienceDirect

Applied Soft Computing

journal homepage: www.elsevier.com/locate/asoc

Weighted kappa measures for ordinal multi-class classification
performance
Ayfer Ezgi Yilmaz a, Haydar Demirhan b,∗

a Department of Statistics, Hacettepe University, Ankara, Turkey
b Mathematical Sciences Discipline, School of Science, RMIT University, Melbourne, Australia

a r t i c l e

i n f o

a b s t r a c t

Article history:
Received 10 March 2022
Received in revised form 18 December 2022
Accepted 5 January 2023
Available online 13 January 2023

Keywords:
Accuracy
Agreement measures
Evaluation metric
Matthews correlation coefficient
Performance metric
Ordinal classifier
Ordinal labels

Assessing the classification performance of ordinal classifiers is a challenging problem under imbal-
anced data compositions. Considering the critical impact of the metrics on the choice of classifiers,
employing a metric with the highest performance is crucial. Although Cohen’s kappa measure is
used for performance assessment, there are better-performing agreement measures under different
formations of ordinal confusion matrices. This research implements weighted agreement measures as
evaluation metrics for ordinal classifiers. The applicability of agreement and mainstream performance
metrics to various practice fields under challenging data compositions is assessed. The sensitivity
of the metrics in detecting subtle distinctions between ordinal classifiers is analyzed. Five kappa-
like agreement measures with six weighting schemes are employed as evaluation metrics. Their
reliability/usefulness is compared to the mainstream and recently proposed metrics, including F1,
Matthews correlation coefficient, and informational agreement. The performance of 37 metrics is
analyzed in two extensive numerical studies, including synthetic confusion matrices and real datasets.
Promising metrics under practical circumstances are identified, and recommendations about the best
metric to evaluate ordinal classifiers under different conditions are made. Overall, the weighted Scott’s
pi-measure is found useful, sensitive to small differences in the classification performance, and reliable
under general conditions.

© 2023 The Author(s). Published by Elsevier B.V. This is an open access article under the CC BY-NC-ND
license (http://creativecommons.org/licenses/by-nc-nd/4.0/).

1. Introduction

Classifying subjects into multiple ordinal classes, namely or-
dinal multi-class classification or ordinal classification, is one of
the most frequent exercises of automatic classification systems in
pattern recognition, machine learning, and deep learning systems.
The problem considered here is to assign each object in a sample
to one of the ordered classes of a categorical response variable
using an ordinal classifier. In pattern recognition, ordinal multi-
class classification is used in the classification of different types
of images such as hyperspectral images [1], data-like images [2],
radar images [3], or images from medical diagnosis systems [4].
Accurate evaluation of ordinal classifiers’ performance is a chal-
lenge under different circumstances of data. Therefore, many
metrics have been proposed to evaluate classifiers. The quality of
training a model or network is related to the preciseness of the
classifier against true classes in a labeled dataset [4]. A metric
can also be used as a loss function to optimize in an image
classification system [4]. In this sense, it is crucial to evaluate

∗

Corresponding author.
E-mail addresses: ezgiyilmaz@hacettepe.edu.tr (A.E. Yilmaz),

haydar.demirhan@rmit.edu.au (H. Demirhan).

the performance of ordinal classifiers with the highest possible
accuracy.

The evaluation of ordinal classifiers’ performance is directly
related to the used evaluation metric and the characteristics of
the training or test dataset, which we call ‘‘the composition of
the dataset’’ throughout the manuscript. When the distribution of
subjects into ordinal classes is imbalanced, mainstream metrics
such as accuracy, precision, and recall are negatively impacted;
hence, they do not precisely assess classifiers’ performance [5,6].
Therefore, the use of other measures such as F1 score [7], Cohen’s
(weighted) κ (kappa)-measure [8] and Matthews correlation co-
efficient (MCC) [9] is proposed. MCC is observed to perform
better than the F1 score and κ-measure for binary classifica-
tion [10,11]. For multi-class classification, Rácz et al. [6] identify
better performance for F1 score than MCC and find that MCC is
more sensitive to the data composition. Although Rácz et al. [6]
include Cohen’s unweighted κ in their study, they do not give any
specific inference about the comparison of Cohen’s unweighted
κ-measure to F1 score and MCC for ordinal classifiers. The use of
Cohen’s linear or quadratic weighted and unweighted κ-measures
is found suitable for assessing the performance of multi-class
classifiers [8]. However, Czodrowski [8] do not distinguish or-
dinal classifiers. Cohen’s unweighted κ-measure is compared to

https://doi.org/10.1016/j.asoc.2023.110020
1568-4946/© 2023 The Author(s). Published by Elsevier B.V. This is an open access article under the CC BY-NC-ND license (http://creativecommons.org/licenses/by-
nc-nd/4.0/).

---

<!-- PAGE 2 -->

A.E. Yilmaz and H. Demirhan

Applied Soft Computing 134 (2023) 110020

a bunch of metrics, including the F1 score in the accuracy of
assessing the performance of binary and multi-class classifiers
for balanced and imbalanced data compositions by Ferri et al.
[5], without specifically accounting for ordinal classifiers. It is
observed that the unweighted κ-measure shows similar per-
formance as the metric called accuracy for multi-class classi-
fiers in general. However, it shows similar performance with
the F1 score for large datasets with more than 1000 observa-
tions [5]. Serious concerns have also been raised against the use
of Cohen’s κ-measure in assessing the performance of multi-
class classifiers. There is a strong correlation between Cohen’s
unweighted κ-measure and MCC, and high κ values are observed
for poorly performing classifiers with imbalanced data while MCC
was insensitive to this case [12]. Specifically, mean absolute er-
ror (MAE), its variations, and mean squared error (MSE) are
considered for the evaluation of ordinal classification perfor-
mance under imbalanced data compositions [13,14]. Cardoso and
Sousa [15] propose an ordinal classification index (OCI), consider
Misclassification Error Rate (MER) for ordinal classification per-
formance, and compare MER with MAE and MSE. However, they
do not consider mainstream and (weighted) agreement metrics
for ordinal classification performance.

In image classification studies, Cohen’s κ-measure is found
useful for assessing multi-class classifiers’ performance. Some
performance comparisons among well-known metrics, F1 score
and Cohen’s κ are reported. The grounds for using kappa-like
agreement measures to assess multi-class classifiers’ performance
is that the confusion matrix is essentially a cross table showing
the agreement between two raters, represented by the obser-
vations and estimations. In this case, the confusion matrix is
taken as an ‘‘agreement table’’ that shows the classification of
two raters into multiple classes of an outcome variable. Then, the
level of agreement between two raters is equivalent to the level of
goodness of classification. In this sense, all kappa-like agreement
measures can be considered as an evaluation metric for ordinal
classifiers. However, Cohen’s κ-measure is proposed to be used
when there is no ordering among the classes of the variable of
interest (nominal type classes). Thus, it does not consider the
degree of deviance from the main diagonal of the classification.
For example, in classifying objects in images into the classes
‘‘bicycle’’, ‘‘car’’, ‘‘airplane’’, three classes are of nominal type since
there is no hierarchy among them. When there is a hierarchy
among the classes (ordinal type classes), we need to consider this
hierarchy in the analysis. For example, diabetic retinopathy is a
serious disease that may lead to visual impairment and can be
prevented if detected early. For the detection, lesions related to
the disease are screened in retinal images, and a classification is
done based on the severity of stages using automatic image clas-
sification techniques [4]. Due to the natural hierarchy among the
severity stages, we deal with an ordinal multi-class classification
problem. In this case, the weighted version of Cohen’s κ-measure,
which includes the impact of the distance from the main diagonal,
is available for use. Since Cohen’s (weighted) κ-measure has
some drawbacks [16,17], other measures such as Gwet’s AC2,
Scott’s π (pi), Brennan–Prediger’s BP, and Krippendorff’s α (alpha)
are proposed in the agreement studies [18]. However, they are
not considered as an evaluation metric for ordinal classifiers
in the literature. When we consider ordinal classes, there are
other weighting schemes besides linear and quadratic weights,
such as ordinal, radical, ratio, circular, and bipolar weights to
be used with weighted versions of the agreement measures to
account for the ordinality of the classes [18]. Due to the interac-
tion between the assumptions behind agreement measures and
weighting schemes, each weighted agreement measure would
perform satisfactorily in measuring a classifier’s performance un-
der a different data composition. Therefore, the aims of this

2

research are to (i) explore the precision/usefulness of weighted
agreement measures as evaluation metrics for ordinal classi-
fiers, (ii) compare the versatility of agreement metrics and the
mainstream metrics under challenging compositions of confusion
matrices in different fields of practice for ordinal classification,
and (iii) identify the promising metrics under practical circum-
stances and make recommendations about the best metric to use
for the evaluation of ordinal classifiers.

To fulfill the aims, our objectives are to (i) implement the
weighted agreement measures for the evaluation of ordinal clas-
sifiers for balanced and imbalanced data compositions, (ii) con-
duct a numerical study with synthetic confusion matrices to see
the quality of the metrics under contesting compositions of con-
fusion matrices, and (iii) run a second numerical study with the
outputs of ordinal classifiers with real data from a vast variety of
the fields to assess the sensitivity of metrics to small differences
between ordinal classifiers. Under these objectives, we consider
weighted versions of κ, π , α, BP and AC2 metrics and compare
their performance against the mainstream metrics accuracy, re-
call, precision, F1, MCC and the recently proposed informational
agreement through two extensive numerical studies. In total, we
consider 37 metrics and assess them under artificially created
scenarios composed of the true performance of the classifier, the
degree of imbalance in the data (the composition of data), and
different misclassification scenarios for the classes of the ordinal
dependent feature in the first numerical study. This numerical
study reveals the metrics’ performance/usefulness under various
confusion matrix formations. In the second numerical study, we
compare the metrics in terms of their sensitivity in distinguish-
ing two classifiers with similar classification performance using
40 real datasets, including balanced, imbalanced, and extremely
imbalanced data compositions from social science, life sciences,
engineering, and other areas of practice. This numerical study
is important to observe the ability of metrics to perceive even
small differences in classification performance, which is a highly
desired quality for an evaluation metric. The contributions of this
study are that (i) we explore the performance of a wide range
of unweighted and weighted agreement measures as metrics
for ordinal multi-class classifiers, (ii) comparatively examine the
performance of the mainstream metrics, and (iii) identify a metric
that is superior to the mainstream metrics that can be used under
different data compositions and areas of practice as a generic
metric.

Section 2 outlines the related works in the literature. Section 3
describes the metrics considered in this study. Sections 4 and 5
present the numerical studies with synthetic confusion matrices
and real data. Section 6 is devoted to the general recommenda-
tions and discussions.

2. Related works

The use of weighted κ and MCC as a loss function in deep
learning models for
image classification is considered by
de La Torre et al. [4] for general image classification and Kook
et al. [2] for the classification of complex data like images into
ordinal classes. However, they only consider quadratic weights
and Cohen’s κ while there are better-performing alternatives. For
hyperspectral image classification, both Deng et al. [1] and Sel-
lami and Tabbone [19] employ accuracy and unweighted κ to
evaluate their proposed methods for multi-class classification.

Ben-David [20] focus on the expert systems for cost-sensitive
applications and propose a new strategy based on weighted κ-
measure to assess the performance of multi-class classifiers. They
only consider unweighted, linear and quadratic weighted Co-
hen’s κ-measure without distinguishing imbalance in data and
comparing the accuracy of κ-measure to others such as accu-
racy, precision, recall, and F1 score. García et al. [21] consider

---

<!-- PAGE 3 -->

A.E. Yilmaz and H. Demirhan

Applied Soft Computing 134 (2023) 110020

Cohen’s unweighted κ-measure and classification rate for multi-
class classifiers for genetics-based machine learning implementa-
tions. This study shows that the precision of metrics can vary for
classification problems in different fields of application.

Ferri et al. [5] conduct an extensive experimental study to
assess the reliability of 18 metrics in classification problems. They
present very detailed background information about the different
types of metrics, including their taxonomy. They only consider
the unweighted version of κ-measure and do not include MCC in
the comparison study. Some similarities between the F1 score and
κ-measure, and accuracy and κ-measure are observed for differ-
ent compositions of data by Ferri et al. [5]. Czodrowski [8] studies
the advantages and disadvantages of Cohen’s unweighted κ as a
metric of performance for the classification problem in machine
learning and cheminformatics. He creates various data compo-
sitions to compare the reaction of precision, recall, accuracy, κ,
prevalence, and bias and observes that κ-measure is a useful
metric within this set of metrics. Saito and Rehmsmeier [22]
compare the performance of precision/recall plots to Receiver
Operating Characteristics (ROC) plots in assessing the binary clas-
sifiers on imbalanced data. They consider the metrics computed
using the information in the confusion matrix, such as accuracy,
F1 score, MCC, and precision and observe that performance of
precision/recall plots is superior to ROC plots. Korotcov et al. [23]
compare the performance of deep neural networks to that of
mainstream machine learning methods by using AUC, F1 score,
Cohen’s unweighted κ and MCC. They observe similar κ and
MCC values for implementing deep learning and machine learn-
ing methods with pharmaceutical data. Since we work with the
metrics relying on the qualitative understanding of error that
take the number of false classifications into account [5] in this
study, we do not consider either ROC or AUC. The metrics, such
as logarithmic loss, require prediction probabilities. However,
we directly work with the confusion matrices for better gener-
alizability instead of working with a specific model. Therefore,
metrics requiring prediction probabilities are not considered in
this study.

For ordinal multi-class classification, it is essential to account
for the severity of the error. In that sense, the use of metrics
that do not count for the magnitude of the error, such as ac-
curacy metric, is not suitable [13,15]. Gaudette and Japkowicz
[13] consider MAE and MSE to capture the magnitude of the
error and find that MAE and MSE perform better than the metric
accuracy for imbalanced datasets. Baccianella et al. [14] propose
macro-averaged versions of MAE for imbalanced datasets but
do not compare them with the mainstream metrics. When the
number of ordinal levels increases, it is appropriate to use MAE
and MSE based on the approximation to the continuous scale.
However, when the number of levels is not large enough to
support such an approximation, it is essential to identify the
promising metrics that capture the magnitude of error for ordinal
classification. Cardoso and Sousa [15] define OCI directly using
the confusion matrix and consider the relative ordering of true
and predicted classes (concordant and discordant pairs) and their
deviation from the main diagonal of the confusion matrix. The
weighted agreement metrics considered in this study capture
concordance and discordance in the confusion matrix and account
for the magnitude of discrepancy between the observed and
predicted classification of the labels, in addition to the degree of
similarity between them. Thus, figuring out the usefulness and
efficiency of the weighted agreement metrics in the evaluation of
ordinal classification performance is an important contribution.

Boughorbel et al. [9] propose optimizing the metrics to han-
dle the imbalance in data and develop a new binary classifier
based on the optimization of MCC for imbalanced data. They
compare MCC, AUC, Accuracy, and F1 under imbalanced data

composition and observe that AUC and MCC have consistent
performance across different classifiers with imbalanced data
composition. Rácz et al. [6] conduct a statistical analysis on
the performance of 28 metrics, including unweighted κ, MCC,
F1 score, accuracy, diagnostic odds ratio, and AUC by taking
data composition (imbalanced/balanced), level of classification
(binary/multi-class), and the performance of metric as factors
against the sum of ranking differences over three datasets. They
observe that most of the metrics are sensitive to the composition
of the dataset and the F1 score and the diagnostic odds ratio are
the least sensitive ones. Wardhani et al. [24] focus on imbalanced
data composition and compare the reliability of F1 score, g-mean,
MCC, unweighted κ, and AUC metrics over an empirical study on
the cabbage image classification. They observe that accuracy, F1
score, g-mean, MCC, and κ provide similar results for different
confusion matrices while AUC is sensitive to the changes. When
the degree of imbalance is high, Wardhani et al. [24] suggest
not to use MCC and unweighted κ-measure to avoid misleading
results.

In recent studies, Casagrande et al. [25] propose a new metric
called informational agreement (IA) to measure the strength be-
tween two assessors for binary and multi-class labels to avoid the
disadvantages of κ-measure. They test IA under the cases where
the κ-measure gives problematic results by taking two diagnostic
classifiers as assessors. Delgado and Tibau [12] focus on the sim-
ilarities and differences between Cohen’s unweighted κ-measure
and MCC under various compositions of the confusion matrix for
binary and multi-class classifiers. They theoretically and numeri-
cally study the equivalence between MCC and unweighted κ and
figure out the formations of confusion matrix where unweighted
κ should be avoided. Chicco and Jurman [11] consider MCC and
observe its advantages over the F1 score and accuracy for binary
classification. They conclude that MCC is a more reliable metric
for assessing performance for binary classifiers and should be
preferred over accuracy and F1 score.

There is a close theoretical relationship between κ-measure
and MCC [12,26] when the confusion matrix is symmetric. Del-
gado and Tibau [12] also observe that κ-measure differs from
MCC and is not reliable under imbalanced compositions of data.
This result motivates us to explore other alternatives of
κ-measure to identify a better metric for assessing the perfor-
mance of multi-class classifiers with imbalanced datasets. Dif-
ferent to the existing studies, we consider four alternatives of
the κ-measure with six weighting schemes under different data
compositions in this study.

In general, different studies in different areas have produced
contradictory conclusions on the suitability of MCC and Cohen’s
κ-measure. Although the characteristics of different areas are
influential in this contradiction, these studies are limited to their
simulation or numerical experimentation spaces. This is another
motivation for conducting extensive numerical studies with syn-
thetic and real data from different fields to explore the preci-
sion/usefulness of other weighted agreement measures as metrics
for multi-class classifiers for ordinal labels.

3. Performance metrics for multi-class classifiers

Evaluation metrics differ according to the way they handle the
error. The measures based on the qualitative understanding of
error take into account the number of false classifications. Those
regarding the probabilistic understanding of error are based on
the distance from the true probability and are mostly used in
reliability studies. The metrics related to the ranking accuracy of
the model are used when the classifiers are evaluated on how
well they select a given number of best labels/subjects from a
dataset such as recommender systems [5]. In this article, we focus
on the metrics relying on the qualitative understanding of error.

3

---

<!-- PAGE 4 -->

A.E. Yilmaz and H. Demirhan

Table 1
The confusion matrix for a classifier.

Actual class

1
2
.
.
.
R

Column margin

3.1. Mainstream metrics

Predicted class

1

n11
n21
.
.
.
nR1

n.1

2

n12
n22
.
.
.
nR2

n.2

. . .

. . .
. . .
. . .
. . .

. . .

R

n1R
n2R
.
.
.
nRR

n.R

Row

margin

n1.
n2.
.
.
.
nR.

n

The confusion matrix for a multi-class classifier assigning n
labels into R classes is shown in Table 1. The rows of the confusion
matrix represent the actual classes, and the columns show the
predicted classes. In Table 1, nij denotes the number of labels
that are actually in class i and predicted to be in class j, where
i, j = 1, 2, . . . , R. The corresponding cell probability is pij =
nij/n. The row and column totals are shown as row and column
margins, respectively. Marginal row and column probabilities
are pi. = ni./n and p.j = n.j/n, respectively. Since the row-
totals of the confusion matrix are fixed by the frequencies in
the dataset, the sampling scheme we are working with is the
product-multinomial sampling [27].

Using the confusion matrix in Table 1, the mainstream metrics

considered in this article are calculated as follows:

• Accuracy is the most common metric defined as the ratio of
correctly predicted labels to the total number of labels.

Applied Soft Computing 134 (2023) 110020

class memberships of labels using the cell counts of the con-
fusion matrix. It takes values in [−1, 1] where −1 represents
the poorest, and 1 shows perfect classification performance:

.

√

(6)

MCC =

i=1 n2
.i)

n ∑R
(n2 − ∑R

i=1 nii − ∑R
i=1 n2

i=1 ni.n.i
i.)(n2 − ∑R
• Informational agreement has recently been proposed by
Casagrande et al. [25] and is based on the amount of in-
formation (entropy) exchanged between the raters in the
agreement context. In the classification performance assess-
ment, the higher the agreement between a classifier and
the actual distribution of labels, the higher the classification
performance of the classifier. It is computed as

IA =

MI(X, Y )
min{H(X ), H(Y )}

,

MI(X, Y ) =

R
∑

i,j=1

pij logR

)

,

( pij
pi.p.i

H(X ) = −

R
∑

i=1

pi. logR(pi.), and H(Y ) = −

3.2. Weighted agreement coefficients

(7)

R
∑

i=1

p.i logR(p.i).

The weighted agreement coefficients are essentially used to
evaluate the level of agreement between two raters who clas-
sified the subjects into ordered categories. The general form for
agreement coefficients (A) is defined as follows:

Acc =

∑R

i=1 nii
n

.

(1)

A =

Po − Pe(A)
1 − Pe(A)

,

Po =

R
∑

i,j=1

wijpij,

(8)

• Macro-average recall is also called balanced accuracy and
computed as the arithmetic mean of recalls for all classes.

M.Recall =

∑R

i=1 recalli
R

,

and

recalli =

R
∑

i=1

nii/ni..

(2)

The macro-average recall is called ‘‘recall’’ in the rest of the
article.

• Macro-average precision is defined as the arithmetic mean of

precisions over R classes.

M.precision =

∑R

i=1 precisioni
R

,

and

precisioni =

R
∑

i=1

nii/n.i.

(3)

Macro-average precision is called ‘‘precision’’ in the rest of
the article.

• Mean F1-score is calculated as the arithmetic mean of F1-

scores over R classes.

MeanF 1 =

∑R

i=1 F 1i
R

,

and

F 1i = 2×

( precisioni × recalli
precisioni + recalli

)

.

(4)

• Macro F1-score is computed as the harmonic mean of macro-
averaged precision and macro-averaged recall, defined in
Eqs. (2) and (3), respectively.

M.F 1 = 2 ×

( M.precision × M.recall
M.precision + M.recall

)

.

(5)

• Matthews correlation coefficient [9] given in Eq. (6) measures
the degree of correlation between the predicted and actual

where Po is the observed agreement, Pe is the proportion agree-
ment expected by chance, wij shows the weight assigned to cell
(i, j) of the confusion matrix, and Pe depends on the agreement
coefficient and is calculated as given in Table 2.

The general formulation of Krippendorff’s α measure is as

follows [18]:
(1 − 1
n¯r

αw =

) pa0 + 1
n¯r
1 − ∑R

− ∑R

k,l=1
wklπkπk

k,l=1

wklπkπk

,

where

pa0 =

1

n

πk =

rik(¯rik. − 1)
¯r(ri − 1)

,

¯rik. =

R
∑

l=1

wklril,

and

n
∑

R
∑

k=1

i=1
n
∑

1

n

i=1

rik ¯r.

(9)

(10)

While computing Krippendorff’s α for a confusion matrix, rik =

2 and ri = ¯r = 2 · R in Eqs. (9) and (10).

The critical distinction between agreement metrics is the as-
sumption about the marginal distributions of assessors, which
corresponds to the confusion matrix’s margins in the classifica-
tion performance context. One of the margins of the confusion
matrix is fixed by the total class frequencies in the data. There-
fore, the agreement coefficients calculated assuming that one of
the margins is fixed are expected to perform better in the classifi-
cation performance evaluation. However, none of the agreement
coefficients has this assumption straightforwardly. Scott’s πw as-
sumes the homogeneity of margins [28]; hence, it is expected to
be a precise metric when the margins of the confusion matrix
get closer. Krippendorff’s α does not require the margins of the
confusion matrix to be homogeneous. It instead counts where the

4

---

<!-- PAGE 5 -->

A.E. Yilmaz and H. Demirhan

Applied Soft Computing 134 (2023) 110020

Table 2
The calculation of the proportion agreement expected by chance.

Coefficient

Symbol

Weighted kappa

Scott’s pi

Gwet

Brennan–Prediger

κw

πw

AC 2

BPw

Pe

Pe =

Pe =

R
∑

i,j=1

R
∑

i,j=1

wijpi.p.j

wijpipj,

pi =

(pi. + p.i)
2

Pe =

1
R(R − 1)

( R

∑

) R

∑

wij

i,j=1

i=1

pi(1 − pi),

pi =

(pi. + p.i)
2

Pe =

1
R2

R
∑

i,j=1

wij

classifier matches with the data in classifying the labels. There-
fore, α is expected to be highly sensitive to misclassifications.
Brennan–Prediger’s BP assumes that the marginal distributions of
the confusion matrix are uniform. Thus, BP is expected to work
well with balanced data compositions. Since Gwet’s AC2 adjusts
uniformity regarding the variation in each class, it can handle the
unbalanced data compositions to produce precise results [29].

The weighting schemes (wij) considered in this article are
computed as given in Eqs. (11)–(15), where wij = 1 when i = j
for i, j = 1, 2, . . . , R [18].

• Unweighted: wij = 1.
• Linear weights:
|i − j|
R − 1

wij = 1 −

.

• Quadratic weights:

wij = 1 −

(i − j)2
(R − 1)2

.

• Ordinal weights:

wij = 1 −

, Mij = max(i, j) − min(i, j) + 1

and

Mij
Mmax

Mmax = max(Mij).

• Radical weights:

wij = 1 −

√
√

|i − j|
|R − 1|

.

• Bipolar weights:

wij = 1 −

(i − j)2
M(i + j − 2)(2R − i − j)

,

where M is the maximum value of
pairs of (i, j).

(

(i−j)2
(i+j−2)(2R−i−j)

)

over the

Linear weights are proportional to the degree of misclas-
sification made by the classifier. If a classifier assigns a label
farther away from its true class, the penalty applied by linear
weights increases. The degree of penalty due to misclassification
increases quadratically with the quadratic weights, while the
radical weights penalize misclassification at a degree between the
linear and quadratic weights. Since the ordinal weights account
for the ranks of assignments done by the classifier, only the ranks
are reflected in the weights. Bipolar weights produce a similar

5

(11)

(12)

(13)

(14)

(15)

pattern as linear weights but with higher values of weights. They
get closer to quadratic weights toward the end of scale [18]. In
terms of the relationship between Cohen’s κ-measure with no
weight, linear, and quadratic weights, Warrens [26] shows that
‘‘Cohen’s unweighted κ < Cohen’s linear weighted κ < Cohen’s
quadratic weighted κ’’. The selection of weights is discussed in
the later sections.

To implement the agreement coefficients as evaluation met-
rics, any agreement coefficient in Table 2 is calculated with one
of the weighting schemes described in Eqs. (11)–(15) using the
counts in the confusion table given in Table 1. Since this cal-
culation is straightforward and does not require any iterative
algorithms, there is no difference between the computational cost
of the agreement and the mainstream evaluation metrics.

4. Numerical experiments with synthetic confusion matrices

4.1. Experiment space and data generation

In this numerical study, we create synthetic confusion matri-
ces to examine the behavior of the evaluation metrics mentioned
in Section 3 against different formations of the confusion matrix
for a classification task into three ordinal classes. We generate
confusion matrices with different characteristics for a given true
classification performance, calculate evaluation metrics, and com-
pare evaluation metrics with the true classification performance.
The generation of confusion matrices, independent of a specific
model and classifier, allows us to examine a wide range of con-
fusion matrix formations that can be observed in real practice;
hence, it provides sufficient generalizability.

The generated scenarios include high (0.8), moderate (0.5),
and low (0.2) levels of true accuracy for a classifier which also
translate into high, moderate, and low performance in practice.
Here, the true accuracy/performance (TA) is defined as the ratio of
correctly classified labels to the number of labels in each class in
the data (either test or training set). Therefore, the metric called
accuracy is expected to give similar values to TA subject to some
random variation from replicating the experiments. In this sense,
accuracy will be used as a control metric to assess if the data
generation approach is sufficient to generate the desired levels
of accuracy, and the metric accuracy is not compared to other
metrics.

Since one of the main factors impacting the metrics is the
balancedness of the distribution of labels into the target classes,
balanced, imbalanced, and extremely imbalanced structures are
created in combination with the true accuracy. This factor is
called the structure of the table (ST) in the rest of the manuscript.
Based on the classifier’s performance and the area of interest, the
accuracy of classification may differ across the ordinal classes. To

---

<!-- PAGE 6 -->

A.E. Yilmaz and H. Demirhan

Applied Soft Computing 134 (2023) 110020

account for this, the following cases are created by using different
pij settings:

1. Labels belonging to all 3 classes are classified with an accu-

racy close to the true accuracy.

2. Labels belonging to 2 out of 3 classes are classified with
an accuracy close to the true accuracy, and the last one is
classified with low accuracy.

3. Labels belonging to only one of 3 classes are classified with
an accuracy close to the true accuracy, and the remaining
ones are classified with low accuracy.

This factor is named ‘‘Case’’ in the numerical study and denoted
as Case 1, 2, and 3 throughout the manuscript. Case 1 is the best
scenario where the classifier performs equally well for all classes.
Thus, we expect a metric value close to the given true accuracy.
In Cases 2 and 3, the classifier fails to work sufficiently for at
least one of the three classes. So, even for high true accuracy, the
classifier’s performance is poor for Case 2 and poorer for Case 3.
Since the classifier does not perform well, we expect lower values
than the given true accuracy in Cases 2 and 3.

The confusion matrices are generated using the product-
multinomial sampling scheme for the sample sizes of 50, 100,
200, and 500 for each combination of ST, TA, and Case. Each
scenario is replicated 1000 times. The pij values are created to
reflect the ordinal classes, and the combinations of ST, TA, and
Case are used as inputs of the rTable.RxC() function of rTableICC
package of R software [27]. We arbitrarily distort the given true
accuracy in Cases 2 and 3 to create situations that can occur
in real practice. The resulting synthetic confusion matrices are
shown in Table A.1 of Appendix A. To generate ordinal classes, we
follow the approach explained by Tran et al. [17, see p. 996–997].
We use mean absolute error (MAE) and root mean squared
error (RMSE) given in Eq. (16) to compare the metrics under each
simulation scenario.

MAE =

1

r

r
∑

i=1

|X − ˆXi|

and

RMSE =




√

1

r

r
∑

(X − ˆXi)2,

(16)

i=1

where r is the number of replications, X is the true value of ac-
curacy, and ˆXi is the performance or weighted agreement metric
estimation in the ith replication.

4.2. Results

The mainstream metrics’ RMSE and MAE values for all sam-
ple sizes, balanced, imbalanced, and extremely imbalanced data
compositions are given in Table A.2, A.4, . . . , A.12 of Appendix A.
Those for the weighted agreement metrics are given in Table A.3,
A.5, . . . , A.13 of Appendix A. In this section, ‘‘mainstream metrics’’
refer to the metrics described in Section 3.1 except accuracy.
Since we use the definition of accuracy to generate confusion
matrices, we exclude it from the inferences in this section. For
a full picture of comparisons between the mainstream and the
weighted agreement metrics, the reader should refer to pairs of
Table A.2 and A.3, A.4 and A.5, and so on. The inferences in this
section are also made by considering these pairs of tables.

The results in Appendix A show that accuracy is very close to
TA, as expected in all the scenarios considered. When the data
composition is balanced, mainstream metrics except for MCC and
IA and most agreement metrics produce accurate measurements
of classifier performance for Case 1 for all levels of TA and sample
sizes. MCC and IA produce large MAEs and RMSEs, in general.
As the classifier’s performance becomes heterogeneous across the
classes (moving from Case 1 to 2 and 3) and TA reduces to lower
levels (the classification task gets harder), mainstream metrics

6

get worse in accurately capturing true accuracy. For high and
moderate true accuracy, Cohen’s κ and Scott’s π with ordinal
weights measure the classification performance accurately for all
cases. When the true accuracy is low, unweighted or quadratic
weighted AC2 performs better than other measures for all cases.
We observe that mainstream metrics have a slightly better or
similar performance for balanced situations with high true ac-
curacy than ordinal weighted Cohen’s κ and Scott’s π measures.
However, if the true accuracy is at lower levels and the classi-
fication accuracy is not distributed evenly as in Cases 2 and 3,
ordinal weighted Cohen’s κ and Scott’s π and quadratic weighted
AC2 perform better for balanced data compositions. Following the
theoretical results of Delgado and Tibau [12], Cohen’s unweighted
κ produces similar values to MCC in all the scenarios for balanced
data composition. There are small deviations between Cohen’s
unweighted κ and MCC for Cases 2 and 3. As expected, MAE and
RMSE values get slightly smaller as the sample size increases for
all metrics.

The results for imbalanced data compositions are generally
similar to those observed for balanced datasets. MCC and IA
produce high error values for high and moderate levels of TA.
Mainstream metrics perform well when the classifier’s perfor-
mance is homogeneous across the ordinal levels and the true
accuracy is high or moderate. The mean F1 is the best-performing
mainstream classifier. Cohen’s κ and Scott’s π with quadratic
weights have very similar MAE and RMSE values to mainstream
metrics except for MCC and IA for these scenarios. However,
when the TA is reduced, and the classifier’s performance is better
for some classes and worse for the other classes (Cases 2 and 3),
quadratic or ordinal weighted Cohen’s κ and Scott’s π produce a
promising performance that is better than mainstream metrics
for most of the scenarios. For low TA under imbalanced data
composition, AC2, BP, and Krippendorff’s α perform better than
the mainstream and other agreement metrics when only one of
the classes is captured with an accuracy close to 0.2. We observe
slight decreases in MAE and RMSE for increasing sample sizes
with imbalanced data composition.

When the data composition is extremely imbalanced, MAE and
RMSE values of the mainstream metrics considerably increase if
the classifier does not perform equally well in all classes. For het-
erogeneous classifier performance across the classes, quadratic
weighted Cohen’s κ and Scott’s π generate better performance
estimates than mainstream metrics for all sample sizes. For lower
TA, the unweighted AC2 is the best metric among the agreement
metrics for all cases. It performs better than the mainstream
metrics for sample sizes greater than 50.

4.3. Conclusions

Among the mainstream metrics, MCC and IA produce no-
tably larger MAE and RMSE values than most of the metrics in
most scenarios. The mainstream metrics, except for MCC and
IA, successfully identify the performance of classifiers when the
data composition is balanced, and all three ordinal classes are
captured equally successfully. For the scenarios that deviate from
these ideal conditions, error margins increase for the mainstream
metrics.

For the agreement measures, we observe the theoretical re-
lationship between MCC and Cohen’s κ demonstrated by [12,26]
in practice through the synthetic datasets when all the classes
are assigned with similar success by the classifier and the data
composition is balanced. However, this theoretical relationship
is not observed under the deviations from this well-balanced
scenario.

For the rest of the weighted agreement measures, a wide
range of different values are observed, implying that agreement

---

<!-- PAGE 7 -->

A.E. Yilmaz and H. Demirhan

Applied Soft Computing 134 (2023) 110020

measures are sensitive to different data compositions and true
accuracy levels and have the potential to be used as reliable,
useful metrics for multi-class classifiers. Specifically, Cohen’s κ
and Scott’s π with quadratic weights show the best MAE and
RMSE performance for high and moderate true agreement, data
composition scenarios, and classification cases. Since Scott’s π
assumes the homogeneity of margins [28], it returns low error
values when the margins of the confusion matrix get closer (the
true agreement is moderate or high under all cases). However,
when the true agreement is low, we deviate from this case; hence,
other agreement measures perform better. When the true agree-
ment is low, and data composition is imbalanced or extremely
imbalanced, we observe that AC2 gives low MAE and RMSE values
with different weights. The reason for Gwet’s AC2 to perform
better is that AC2 adjusts uniformity due to the variation created
by the low true agreement and imbalance in the data [29].

All the considered mainstream and agreement metrics are
sensitive to the sample size. We get smaller MAE and RMSE values
as the sample increases. The benefit of increasing sample size
on MAE and RMSE becomes notable when the true accuracy is
high or moderate with balanced data composition. When the
imbalance increases and one or two of the classes are correctly
classified (Case 2 and 3), increasing the sample size does not help
reduce the values of MAE and RMSE by a considerable margin.

Overall, when the data composition is imbalanced for the syn-
thetic confusion matrices, the agreement measures mostly with
ordinal weights produce lower error measures than the main-
stream metrics and IA for most cases. They are more sensitive
than MCC against unsuccessful classification in at least one of the
classes. However, we need to study the response of agreement
metrics to the composition of data in a generalizable setting
to identify which agreement measure and weighting scheme
combination can be used for performance assessment of ordinal
multi-class classifiers and how their usage is compared to that of
the mainstream metrics, MCC and the recently introduced metric
IA. For this purpose, we conduct an extensive numerical study
with real datasets in the next section.

5. Numerical experiments with real data

5.1. Datasets and classifiers

In the numerical study with real data, the sensitivity of 37
metrics of Section 3 is assessed in distinguishing ordinal classi-
fiers. Since there is no unique metric to be used as the gold stan-
dard for determining the superiority of one metric over another,
we focus on the sensitivity of metrics to the slight difference
between the performance of two classifiers. It is a desired quality
for a metric to distinguish subtle differences in the classification
performance.

We use 40 real datasets having dependent features with mul-
tiple ordinal classes. For the generalizability of the results, we
gather datasets from the main areas of practice: social sciences
(16),
life sciences (13), engineering (4) and other areas (7).
Datasets and their web links are given in Table B.1 of Appendix
B. Summary information about the datasets is given in Table B.2
of Appendix B. The sample size of each dataset is given under
the ‘‘# Labels’’ column of Table B.2. For the datasets having more
than 5000 labels, a sub-sample of size 1000 is taken randomly.
Data composition for each dataset is qualified based on the bal-
ancedness of marginal probabilities. Overall, we have 6 balanced,
8 imbalanced, and 26 extremely imbalanced datasets. We have
sufficient coverage of the number of features ranging from 3
to 56 and the number of ordinal classes from 3 to 11 among
the datasets. There are very small samples as well as very large
samples from a wide range of areas of practice included in this
numerical study.

We aim to create 10 folds of data from each dataset if it has
more than 100 labels. Since the confusion matrix becomes very
sparse for the datasets with less than 100 labels, we create 2
folds for lsci2, lsci4, lsci13, eng1, other2, and other7 datasets. We
run the computations separately for the full dataset, balanced,
imbalanced, extremely imbalanced, life sciences, social science,
engineering, and other areas datasets for each fold. Since we
cannot create 10 folds for every dataset, we have a different
number of replications for each run composed of datasets and
their folds, as given in Table 3. For example, for the run with
‘‘All datasets’’, we have 10 folds for 34 datasets and 2 folds for
6 datasets; in total, we run 352 replications for all datasets. For
the run with ‘‘Only ENG’’ datasets, there are 10 folds for 3 out of 4
datasets and 2 folds for 1 dataset, resulting in 32 replications. We
utilize the runs for the folds as replications to conduct statistical
hypothesis tests.

In the implementation, we employ pairs of classifiers devel-
oped for ordinal data. The classifiers are selected by considering
that they have similar overall classification performances. We as-
sess if the metrics are able to differentiate between the classifiers.
The difference between the actual performances of classifiers is
an important consideration in assessing the precision/usefulness
of the metrics. Conceivably, in real practice, the precision of
metrics is not a very important issue if one of the classifiers is
performing far better than the other. The success of a metric lies
in its ability to distinguish the classifiers when their performances
are close to each other. Therefore, to create two classifiers with
similar performance, we use two classifiers from the same classi-
fication method with slight changes in their parameter settings.
We consider support vector machines with ordered partitions
(SVMOP), which is developed for classification into ordinal classes
by Waegeman et al. [30], weighted K-nearest neighbors for or-
dinal classification (WKNNOR) proposed by Hechenbichler and
Schliep [31], and kernel discriminant learning for ordinal regres-
sion (KDLOR) proposed by Sun et al. [32]. There can be other
choices of ordinal classifiers. However, since we are not com-
paring the performance of actual classifiers/classification meth-
ods and need to get just confusion matrices out of classifiers,
the choice of SVMOP, WKNNOR, and KDLOR classifiers does not
pose any problem with the generalizability of the results on the
performance of the metrics.

The parameters γ and cost impact the performance of SVMOP
classifiers, which use the Gaussian radial basis kernel function.
The γ parameter adjusts the scale of the Gaussian kernel. A large
scale γ for a given cost creates wide classification boundaries.
For smaller scales, under-fitting occurs if classification boundaries
become more focused under limited regions of the space [33, see
p. 347–348]. An increased under-fitting reduces the classification
performance with the test set. We set the cost value for both
SVMOPs to 1 and use the γ parameter to create classifiers that
have similar overall performance but make mistakes on ordinal
classes. We set the SVMOP classifiers to use with γ = 1 and 10
with cost = 1 for SVMOP1 and SVMOP2, respectively.

For WKNNOR classifiers, we use the Euclidean distance and
Gaussian kernel for both classifiers and set the number of neigh-
bors differently to create two classifiers with slightly different
performances. A KNN with a small number of neighbors tends
to over-fit, but a large value of the number of neighbors has the
potential to create under-fit [33, see p. 160 and 352]. We set the
number of neighbors to 20 for WKNNOR1 and 5 for WKNNOR2
to create a small discrepancy between the performances of the
classifiers that we expect the evaluation metrics to distinguish.

For KDLOR classifiers, we use the Gaussian kernel with dif-
ferent scales to create KDLOR1 and KDLOR2 classifiers. We set
the scale of the Gaussian kernel to 1 and 5 for KDLOR1 and
KDLOR2, respectively. Since KDLOR is a kernel-based method,

7

---

<!-- PAGE 8 -->

A.E. Yilmaz and H. Demirhan

Applied Soft Computing 134 (2023) 110020

Table 3
Runs, datasets, and the corresponding number of replications.

Runs with

All datasets
Only balanced
Only imbalanced
Only extremely
Imbalanced
Only SSCI
Only ENG
Only LSCI
Only OTHER

Number of datasets

Dataset number

Replications

40
6
8
26

16
4
13
7

1 to 40
3, 9, 12, 17, 20, 39
2, 4, 5, 6, 11, 14, 38, 40
1, 7, 8, 10, 13, 15, 16,
18, 19, 21 to 37
14 to 29
30 to 33
1 to 13
34 to 40

352
52
72
228

160
32
106
138

Fig. 1. Flow diagram of the numerical study with real data. Here, n shows the number of datasets in each particular run as given in the second column of Table 3,
k = 2, 10, and the values of m are shown in the last column of Table 3 for each run.

its performance is characterized by the kernel. The scale of the
Gaussian kernel specifies the boundaries of the regions created
for classification, similar to SVMOPs.

It should be noted that these settings do not ensure that either
Classifier1 or Classifier2 under each ordinal classification method
will have superior performance. The superiority issue is outside
the focus of this numerical study since we only need to have one
of the classifiers perform slightly differently.

We employ svmofit(), wknnor(), and kdlortrain() functions
from OCAPIS R package [34] for the implementation of SVMOP,
WKNNOR, and KDLOR classifiers, respectively. The flow diagram
of implementation is given in Fig. 1. We create k-folds, k = 2, 10
of each dataset and implement k-fold cross-validation without
aggregating the results coming out of the folds.

5.2. Results

Results are composed of the values of 37 metrics observed
over 2 sub-classifiers under each of 3 main classification meth-
ods, 40 real datasets, and replications from k-folds. The real
datasets are also divided into categories based on their balanced-
ness and the field of application. We follow Demšar [35] to
provide statistical evidence on the significance of the difference
between metrics across the factors used for comparisons. We use
multi-way analysis of variance (ANOVA) and Tukey’s pairwise
comparison test to identify the metrics that produce significantly
different values between classifiers under each main classifica-
tion method. In this way, we identify the sensitive metrics to
separate the classification performance of two similar classifiers
from each other. The normality and homogeneity of variances
assumptions of ANOVA [35] need to be ensured to get valid
inferences from ANOVA. For this aim, the Kolmogorov–Smirnov
normality test and Leneve test for the homogeneity of variances
are implemented using notest [36] and car [37] R packages,
respectively.

5.2.1. Visual inspection

The means of metrics, calculated by aggregating over 40
datasets and folds, are given in Figs. 2, 3, and 4 for SVMOP,
WKNNOR, and KDLOR classifiers, respectively, along with and the
± standard error limits. Note that the statistical significance of
differences is thoroughly discussed in the parts following these
figures. In Figs. 2, 3, and 4, we see different behaviors for each
group of metrics, namely, mainstream, Cohen’s κ, Scott’s π , AC2,
BP and Krippendorff’s α for all the ordinal classification methods.
There is no clear distinction between the values of metrics with
different weights. For all the main classification methods, SVMOP,
WKNNOR, and KDLOR, almost all metrics show that Classifier1 has
slightly better performance than Classifier2.

For SVMOP classifiers (Fig. 2), weighted π metrics have no-
tably different behavior than all the other metrics. Weighted κ
and α metrics show similar results, while weighted AC2 and BP
metrics indicate a similar level of performance to each other.
However, AC2 and BP metrics do not distinguish SVMOP1 and
SVMOP2, which is not the desired result. In this sense, weighted
π metrics show the highest difference between the classifiers.
Among the mainstream metrics, macro recall, macro precision,
and macro F1 are close to each other, while IA and accuracy
show a similar performance. MCC is the only mainstream metric
that shows a slight difference between the classifiers. Overall,
weighted π metrics are able to distinguish the classifiers as
desired, while none of the mainstream metrics is capable of for
the SVMOP method.

For WKNNOR classifiers (Fig. 3), weighted AC2 and BP indicate
considerably higher performance for both classifiers than the
other metrics. The first classifier is found to be slightly better by
all the agreement measures. Since the mean metric values have
the lowest standard errors for the WKNNOR classifiers, distin-
guishing between two classifiers becomes even more challenging.
The mainstream metrics, except accuracy and IA, are insensitive
to the difference between WKNNOR1 and WKNNOR2. BP is the
most sensitive metric to the difference between two WKNNOR
classifiers. Weights have no impact on the α metric and little

8

---

<!-- PAGE 9 -->

A.E. Yilmaz and H. Demirhan

Applied Soft Computing 134 (2023) 110020

Fig. 2. Mean of metrics for the SVMOP classifiers. The mean is calculated over 40 datasets and folds. Bars show the limits of mean ± standard error.

Fig. 3. Mean of metrics for the WKNNOR classifiers. The mean is calculated over 40 datasets and folds. Bars show the limits of mean ± standard error.

impact on κ and BP metrics. Overall, while most mainstream
metrics are insensitive to the slight difference between WKNNOR

classifiers, all agreement measures show some degree of differ-
ence between the performances of WKNNOR1 and WKNNOR2. BP

9

---

<!-- PAGE 10 -->

A.E. Yilmaz and H. Demirhan

Applied Soft Computing 134 (2023) 110020

Fig. 4. Mean of metrics for the KDLOR classifiers. The mean is calculated over 40 datasets and folds. Bars show the limits of mean ± standard error.

shows the best sensitivity when the metric values are very close
to each other (very small standard errors).

For KDLOR classifiers (Fig. 4), we observe higher standard
errors among the values of metrics that increase the sensitivity of
the metrics to the slight difference between KDLOR1 and KDLOR2
classifiers. All the metrics are sensitive to the difference between
the classifiers. The α metric is not impacted by the weights for
KDLOR classifiers too. The π metrics show the highest sensitivity,
and the weights do not influence the degree of their sensitivity.
Although MCC has the highest sensitivity among the mainstream
metrics, it is considerably lower than the difference indicated by
the π metric. Overall, MCC, κ, and π metrics show similar levels
of performance, while π distinguishes KDLOR1 and KDLOR2 as
desired.

When the standard errors of metric values are high, the π
metric is able to distinguish classifiers with similar performance
as seen for SVMOP and KDLOR methods. However, when the met-
ric values are less variable, BP indicates the difference between
WKNNOR classifiers better than π . Regarding the level of differ-
ence captured by the metrics, the weighting scheme does not
have a notable influence on both π and BP metrics. However, it
impacts the classification performance indicated by these metrics.
Since the data composition and the field of application are
two important features of the datasets, we need to consider
these factors for the inferences. Figs. 5 and 6 show the mean
metric values and their standard error limits aggregated over
all the classifiers and the ordinal classification methods. From
these plots, we observe that both the data composition and the
application field considerably impact the mean metric values
generated for the classifiers since the metrics react differently
to each of balanced, imbalanced, and extremely imbalanced data
compositions and datasets from different fields. Note that since
the aggregation is done over very different ordinal classification
methods for Figs. 5 and 6, it is not appropriate to interpret
the differences between the data compositions and application
fields without looking into the data composition for each ordinal

classification method and the application field for each ordinal
classification method. However, Figs. 5 and 6 demonstrate that
we need to consider each data composition for each ordinal
classification method.

5.2.2. Statistical tests

In order to give detailed significance test results for the dif-
ference between two sub-classifiers, we first apply ANOVA with
metrics and sub-classifiers, ensure the normality and homogene-
ity of variances assumptions of ANOVA, and then apply Tukey’s
pairwise comparison tests to identify the metrics for which the
sub-classifiers are giving different results. The results of these
tests are given in Table B.3 of Appendix B. Suppose we refer to
Tukey’s pairwise comparison test result for the metric MCC. The
test indicates whether there is a significant difference between
MCC values computed for Classifier1 and Classifier2. If there is
a significant difference, we can conclude that MCC is able to
distinguish the performance difference between Classifier1 and
Classifier2 as desired. In this way, we gather statistical evidence
to identify the metrics that perform as desired in distinguishing
two classifiers with similar performance. If a pairwise comparison
of two metrics is insignificant, we conclude that both metrics
are unsuccessful in distinguishing classifiers; hence, they are
insensitive to the difference between them.

For SVMOP classifiers, the p-values of Tukey’s pairwise com-
parison tests are given in Fig. 7 in the breakdown of data compo-
sitions. For balanced datasets, pairwise comparisons of all main-
stream metrics except MCC and IA are insignificant, implying
that they are insensitive to the difference between SVMOP1 and
SVMOP2 classifiers. All weighted κ and π metrics and some
weighted AC2 metrics are significantly different from the main-
stream metrics, while BP and some α metrics are not. All the
weighted π metrics are significantly different from the other
mainstream and agreement metrics. When the composition of
data becomes imbalanced, mean F1, MCC, and IA metrics give

10

---

<!-- PAGE 11 -->

A.E. Yilmaz and H. Demirhan

Applied Soft Computing 134 (2023) 110020

Fig. 5. Mean of metrics according to the data composition. The mean is calculated over all classifiers and folds. Bars show the limits of mean ± standard error.

Fig. 6. Mean of metrics according to the application fields of the datasets. The mean is calculated over all classifiers and folds. Bars show the limits of mean ±
standard error.

significantly different values between SVMOP1 and SVMOP2 clas-
sifiers among the mainstream metrics. κ and α metrics are not
significantly different from MCC, while all other agreement met-
rics are significantly different from MCC and all other mainstream
metrics. For extremely imbalanced datasets, in addition to the

inferences given for imbalanced data composition, we see mean
F1 becomes significantly different from other mainstream and
agreement metrics.

The p-values of Tukey’s pairwise comparison tests for metrics
are given in Fig. 8 in the breakdown of the field of application

11

---

<!-- PAGE 12 -->

A.E. Yilmaz and H. Demirhan

Applied Soft Computing 134 (2023) 110020

Fig. 7. The p-values of Tukey’s pairwise comparison tests for SVMOP classifiers in the breakdown of data composition. The axes of the plots show the metrics
calculated for SVMOP1 and SVMOP2 classifiers.

for SVMOP classifiers. We get different patterns of the pairwise
comparisons’ p-values across the application fields; hence, the
application field makes a difference in the usefulness of the
metrics. Among the mainstream metrics, only MCC is significantly
different across two SVMOP classifiers for social sciences datasets.
Since all κ, π , and α metrics are significantly different from the
mainstream metrics, their behavior against two similar SVMOP
classifiers differs. Also, there are significant differences between
all weighted κ and π metrics. All weighted α metrics are not
significantly different from κ but show the difference for the rest
of the agreement measures. Some weighted AC2 and BP metrics
also show a similar result. We observe very similar results for
life sciences datasets. In addition to MCC, the only difference is
that mean F1 and IA metrics also show significant differences
among the mainstream metrics. The results of datasets catego-
rized in other application fields are similar to life sciences, but

accuracy is also sensitive to the difference between SVMOP1 and
SVMOP2 classifiers. For engineering datasets, the metric accuracy
significantly differs from all other mainstream metrics, κ, π , and
α metrics. There is no significant difference between accuracy
and weighted AC2 and BP metrics. Consistently, weighted ver-
sions of AC2 and BP metrics are significantly different from the
mainstream metrics except for accuracy.

For WKNNOR classifiers, the p-values of Tukey’s pairwise com-
parison tests are given in Figure B.1 of Appendix B in the break-
down of data compositions and Figure B.3 of Appendix B in
the breakdown of application fields. We get similar results for
balanced and imbalanced datasets. For both data compositions,
all the agreement metrics are significantly different from each
other and mainstream metrics. Among the mainstream metrics,
mean F1, MCC, and IA are sensitive to the differences between

12

---

<!-- PAGE 13 -->

A.E. Yilmaz and H. Demirhan

Applied Soft Computing 134 (2023) 110020

Fig. 8. The p-values of Tukey’s pairwise comparison tests for SVMOP classifiers in the breakdown of the field of application. The axes of the plots show the metrics
calculated for SVMOP1 and SVMOP2 classifiers.

WKNNOR1 and WKNNOR2 classifiers. Only accuracy shows a sig-
nificant difference among the mainstream metrics for extremely
imbalanced datasets. Some of κ, most of π , and all AC2, BP, and
α metrics are sensitive to the difference between two WKNNOR
classifiers. Scott’s π metrics are not significantly different from κ
and α metrics. We observe different patterns of p-values across
the fields of application in Figure B.3 of Appendix B. For social
science datasets, κ metrics are not significantly different from
the mainstream metrics except for accuracy. Scott’s π and Krip-
pendorff’s α metrics show sensitivity to the discrepancy between
the classifiers compared to mainstream metrics. AC2 and BP
metrics are significantly different from the mainstream and other
agreement metrics. When it comes to engineering datasets, only
accuracy, AC2, and BP metrics are significantly sensitive to the
difference between WKNNOR1 and WKNNOR2 classifiers, and α
shows significant differences from these metrics. Scott’s π and
Cohen’s κ metrics are insensitive for engineering datasets. For
life sciences and other datasets, we see similar patterns of p-
values. All the metrics except macro recall and macro precision

are sensitive to the difference between WKNNOR1 and WKNNOR2
classifiers.

For KDLOR classifiers, the p-values of Tukey’s tests are given
in Figure B.2 and B.4 of Appendix B in terms of data compositions
and application fields, respectively. For balanced datasets, MCC is
the only sensitive metric to the difference between KDLOR1 and
KDLOR2 classifiers. While κ, π , and α metrics are not significantly
different from MCC, AC2 and BP metrics are different. π and
α show significant differences from all other metrics except κ
for balanced datasets. For imbalanced datasets, mean F1, MCC,
IA, and all agreement metrics differ significantly from the main-
stream metrics. The metric α shows different behavior than the
other agreement metrics. When the data composition becomes
extremely imbalanced, MCC, κ, π , and α metrics are sensitive
to the difference between KDLOR classifiers, and the difference
between this group of metrics and AC2 and BP is significant. For
the application fields, we observe different patterns of p-values
for social sciences, engineering, and life sciences datasets, while
datasets from other application areas produce a similar pattern

13

---

<!-- PAGE 14 -->

A.E. Yilmaz and H. Demirhan

Applied Soft Computing 134 (2023) 110020

as the life sciences datasets. MCC, π , and α metrics produce
significantly different results for KDLOR1 and KDLOR2 classifiers
for social sciences datasets. AC2 and BP metrics are significantly
different from the rest of the agreement and mainstream met-
rics. For engineering datasets, interestingly, only unweighted and
radical weighted versions of the π metrics show a significant
difference for the KDLOR classifiers in addition to AC2 and BP
metrics. None of the mainstream and κ metrics is sensitive to the
difference between KDLOR1 and KDLOR2. Most metrics are sensi-
tive to the difference between KDLOR classifiers for life sciences
and other datasets. Only accuracy, macro recall and macro F1 are
insensitive.

5.2.3. Impact of the number of features

To further investigate the sensitivity of the metrics against
different numbers of features, we worked with datasets ssci15,
ssci14, other3, eng2, ssci13, ssci11, lsci4, lsci5, lsci11 from Table
B.2 of Appendix B. The numbers of features of ssci15 and ssci11
are reduced to 2 and 7, respectively, to have f = 2, 3, . . . , 10 fea-
tures in the considered datasets. The procedure outlined in Fig. 1
is implemented with SVMOP, WKNNOR, and KDLOR classifiers for
each dataset. The two-sample t-test is used to assess if there is a
significant difference between Classifier1 and Classifier2. The p-
values of the tests are given in Table B.4, B.5 and B.6 of Appendix
B for SVMOP, WKNNOR, and KDLOR classifiers, respectively.

In Table B.4, B.5 and B.6 of Appendix B, cells with bold font
show the metrics that produce a significant difference between
the two classifiers; hence, they are sensitive to the slight dif-
ference between the classification performance of classifiers. For
all classification methods of SVMOP, WKNNOR, and KDLOR, the
sensitivity of all the metrics is not impacted by the increasing
number of features. For SVMOP, the mainstream metrics are
insensitive for all the considered number of features. Weighted
κ and π metrics detect the difference just for the dataset with
seven features. Metrics are more sensitive to the difference be-
tween WKNNOR classifiers. While the mainstream metrics are
sensitive to the difference between WKNNOR classifiers with 6
features, weighted agreement metrics are sensitive for multiple
numbers of features. The best sensitivity results are seen for the
weighted BP metric, which detects the difference for 2, 5, 6, and
7 features. For KDLOR classifiers, the weighted κ and π metrics
show sensitivity, with the datasets having 5 and 7 features.

5.3. Conclusions

Under different data compositions, Scott’s π metrics are con-
sistently sensitive to the difference between classifiers for all
ordinal classification methods, while mainstream metrics, except
MCC and IA are not, in general. Other agreement metrics are
as consistent as Scott’s π in distinguishing classifiers under dif-
ferent data compositions. Specifically, metrics have difficulty in
separating the performance of classifiers for extremely imbal-
anced datasets where Scott’s π metric works best. Among the
agreement metrics, while κ, π , and α generally have similar
behavior, AC2 and BP have similar responses to the slight dif-
ference between the classifiers. All the metrics perform better
in distinguishing the classifiers for the SVMOP method and the
worst performance for the KDLOR classifiers.

Engineering datasets produce notably different pairwise com-
parison results for all ordinal classification methods than the
other fields of application. The results for the datasets catego-
rized as other fields of application or life sciences are generally
similar. Among the agreement metrics, π and κ metrics do not
work as desired for engineering datasets, while AC2 and BP are
mostly sensitive to the differences between the classifiers. For
the mainstream metrics, only the accuracy metric is sensitive for

SVMOP and WKNNOR classifiers for engineering datasets. For all
the other categories of datasets, κ, π , and α metrics are sensitive
to the difference between classifiers. From the set of mainstream
metrics, only MCC is consistently sensitive across different fields
of application.

The mainstream metrics are generally insensitive to the differ-
ence between the classifiers, except for MCC. The mean F1 and
MCC show sensitivity against the slight difference between the
classifiers for some ordinal classifiers and application fields.

The number of features has no impact on the ability of both
mainstream and weighted agreement metrics to distinguish the
multi-class classification performance of classifiers. The sensitiv-
ity of the metrics is highly related to the characteristics of the
datasets as investigated in Sections 5.2.1 and 5.2.2.

6. Discussion

Assessing the performance of classifiers in supervised ma-
chine/deep learning is crucial to choosing the classifier to employ.
This problem gets challenging when the classification task is a
multi-class classification with ordinal classes. In this work, we
focused on the metrics used to assess the performance of ordinal
multi-class classifiers based on the qualitative understanding of
error. Cohen’s κ-measure has been used in applications as one of
the promising metrics for classifiers without distinguishing the
type of multi-class categorical responses as ordinal or nominal.
Many other agreement measures and their weighted versions for
ordinal data are proposed in the literature. Furthermore, from
the previous works, it is known that there are better perform-
ing measures than Cohen’s κ in the area of agreement studies.
Considering these, we conducted two extensive numerical studies
with 37 metrics composed of the mainstream and agreement
metrics to investigate the reliability/usefulness of the agreement
measures as evaluation metrics for ordinal multi-class classifiers.
We identified Scott’s weighted π -measure as a strong alternative
to Cohen’s weighted κ.

In the first numerical study, the ability of metrics to capture
the classification performance as close as the true accuracy is
analyzed through randomly generated synthetic confusion ma-
trices under different data compositions and different levels of
accuracy in the classification performance. Ordinal multi-class
classification processes are not perfect. Thus, they are prone to
the composition of ordinal response and sample size. We show
that the composition of data considerably influences the accuracy
of metrics. The mainstream metrics, except MCC, are observed to
be insensitive to capture different types of misclassification. In
contrast, the metrics based on agreement measures react better
to misclassification in individual classes of the dependent feature.
Since the mainstream metrics have the main diagonal of the con-
fusion matrix and one of its margins in their formulations, they do
not capture the misclassification that occurs in the off-diagonal
cells. Only MCC takes both margins into account and shows better
sensitivity than the other mainstream metrics. On the other hand,
(weighted) agreement metrics consider diagonal and off-diagonal
cells and margins (row and column totals) of the confusion table
to capture the correct classifications as well as the magnitude
of divergence from the correct classifications. The level of true
accuracy is another important factor on the performance of met-
rics. When the true accuracy is low, the metrics’ margin of error
to evaluate the classification performance increases, mainstream
metrics become highly insensitive to misclassification, and the
range of agreement measures increases. Therefore, the reliability
of all metrics is higher when they indicate high performance. The
case with a low true accuracy is challenging because it pushes the
cell counts to off-diagonal cells of the confusion table. The metrics
that do not incorporate off-diagonal cells of the confusion table

14

---

<!-- PAGE 15 -->

A.E. Yilmaz and H. Demirhan

Applied Soft Computing 134 (2023) 110020

in their formulation got more negatively impacted in detecting
a low level of accuracy. Cohen’s κ and Scott’s π with quadratic
weights perform better than all the considered mainstream met-
rics and agreement measures under the most challenging data
compositions.

The second numerical study uses 40 real datasets, including
balanced, imbalanced, and extremely imbalanced data composi-
tions from social sciences, life sciences, engineering, and other
areas, to create replications via cross-validation. In this study,
we examined the sensitivity of metrics to small differences be-
tween two similar classifiers from the same ordinal classification
method. A useful metric is expected to be sensitive enough to
distinguish such classifiers. We observed that MCC successfully
discriminates two classifiers with similar performance. However,
it generates high margins of error when the data composition is
imbalanced or extremely imbalanced. Scott’s quadratic weighted
π and Cohen’s quadratic weighted κ metrics show promising
sensitivity for challenging cases, including extremely imbalanced
data compositions.

The quadratic weights penalize misclassification quadratically;
hence, the agreement metrics with quadratic weights are highly
sensitive to misclassification. Scott’s π does not have a uniformity
assumption on the row and column totals of the confusion table.
Instead, it assumes the homogeneity of margins. If the margins of
a confusion table are considerably non-homogeneous, it implies
that the classifier assigns objects to the wrong labels at a notably
high rate. This translates into very poor performance, and the
metrics can capture this case straightforwardly. Thus, in general,
Scott’s π is not impacted by the composition of data. Cohen’s
κ does not have restrictive assumptions on the margins of the
confusion table as well. Therefore, Scott’s quadratic weighted
π and Cohen’s κ generally show satisfactory preciseness. How-
ever, the assumptions, such as the uniformity of the margins
of the confusion table BP or AC2, limits their preciseness for
imbalanced data compositions. Due to the theoretical relationship
between Cohen’s κ and MCC for symmetric confusion matri-
ces, MCC also show satisfactory preciseness when the confusion
matrix is near-symmetric.

Based on the results of both numerical studies, Scott’s π and
Cohen’s κ metrics with quadratic weights are both sensitive to
the small differences between classifiers and produce close values
to the true level of accuracy in most of the considered scenar-
ios. Therefore, they are recommended to be used in practice, in
general. Specifically for engineering applications and low true
performance, the use of quadratic weighted AC2 metric is recom-
mended. We recommend avoiding accuracy, recall, precision, and
macro F1 for extremely imbalanced datasets. Mean F1 has a better
performance than macro F1 but is not as good as Scott’s weighted
π . In some cases, the recently proposed metric, IA, is useful in the
performance assessment of ordinal classifiers. However, it is not
recommended for general use.

This study focuses on a performance analysis of the evaluation
metrics readily computed using a given confusion matrix. The
computation of all the evaluation metrics requires straightfor-
ward analytical calculations without any iterative method, done
in milliseconds without consuming a noticeable computer mem-
ory. Therefore, the space and time complexity of calculating eval-
uation metrics is outside the focus of our study. The main limita-
tions of our study include the simulation space of synthetic data
study and the number of datasets and replications of the real-
data study. Although we cover many scenarios of true accuracy,
data composition, misclassification, and application areas, there
can still be other application-specific characteristics to influence
the performance of metrics.

In addition to the theoretical results on the similarity of un-
weighted Cohen’s κ and MCC, we numerically observed that

15

Scott’s unweighted π produces close values to MCC under some
scenarios. Besides, Gwet’s unweighted AC2, Brennan–Prediger’s
unweighted BP, and Krippendorff’s α metrics produce very close
values to IA when the true agreement is high and, in some cases of
low and moderate agreement. A theoretical investigation of these
results is a future direction.

Another future direction is using Scott’s quadratic weighted π
as a loss function for ordinal image classification and regression.
Cohen’s weighted κ showed improved generalization ability for
image classification [4] when used as a loss function. In this sense,
the use of Scott’s quadratic weighted π as a loss function would
provide further improvement.

CRediT authorship contribution statement

Ayfer Ezgi Yilmaz: Conceptualization, Methodology, Soft-
ware, Data curation, Writing – original draft, Review. Haydar
Demirhan: Conceptualization, Methodology, Software, Data
curation, Writing – original draft, Review.

Declaration of competing interest

The authors declare that they have no known competing
interests or personal relationships that could have

financial
appeared to influence the work reported in this paper.

Data availability

Data will be made available on request.

Acknowledgments

The authors would like to thank three reviewers for their

comments that considerably improved the clarity of the article.

Appendix A. Supplementary data

Supplementary material related to this article can be found
online at https://doi.org/10.1016/j.asoc.2023.110020. Tables A.1
to A.14, Tables B.15 to B.17 and Figures B.1 to B.3 are given in
the Supplementary Material.

References

[1] C. Deng, X. Liu, C. Li, D. Tao, Active multi-kernel domain adaptation for

hyperspectral image classification, Pattern Recognit. 77 (2018) 306–315.

[2] L. Kook, L. Herzog, T. Hothorn, O. Dürr, B. Sick, Deep and interpretable
regression models for ordinal outcomes, Pattern Recognit. 122 (2022)
108263.

[3] L. Li, L. Ma, L. Jiao, F. Liu, Q. Sun, J. Zhao, Complex contourlet-CNN for
polarimetric SAR image classification, Pattern Recognit. 100 (2020) 107110.
J. de La Torre, D. Puig, A. Valls, Weighted kappa loss function for multi-
class classification of ordinal data in deep learning, Pattern Recognit. Lett.
105 (2018) 144–154.

[4]

[5] C. Ferri, J. Hernández-Orallo, R. Modroiu, An experimental comparison
of performance measures for classification, Pattern Recognit. Lett. 30 (1)
(2009) 27–38.

[6] A. Rácz, D. Bajusz, K. Héberger, Multi-level comparison of machine learning
classifiers and their performance metrics, Molecules 24 (15) (2019) 2811.
[7] Y. Sasaki, R. Fellow, The Truth of the F-Measure, University of Manchester:

MIB-School of Computer Science, 2007.

[8] P. Czodrowski, Count on kappa, J. Comput. Aided Mol. Des. 28 (11) (2014)

1049–1055.

[9] S. Boughorbel, F. Jarray, M. El-Anbari, Optimal classifier for imbalanced
data using Matthews Correlation Coefficient metric, PLoS One 12 (6) (2017)
e0177678.

[10] D. Chicco, M.J. Warrens, G. Jurman, The Matthews correlation coefficient
(MCC) is more informative than Cohen’s Kappa and Brier score in binary
classification assessment, IEEE Access (2021).

---

<!-- PAGE 16 -->

A.E. Yilmaz and H. Demirhan

Applied Soft Computing 134 (2023) 110020

[24] N.W.S. Wardhani, M.Y. Rochayani, A. Iriany, A.D. Sulistyono, P. Lestantyo,
Cross-validation metrics for evaluating classification performance on im-
balanced data, in: 2019 International Conference on Computer, Control,
Informatics and Its Applications (IC3INA), IEEE, 2019, pp. 14–18.

[25] A. Casagrande, F. Fabris, R. Girometti, Beyond kappa: an informa-
index for diagnostic agreement in dichotomous and multivalue
(2020)

tional
ordered-categorical ratings, Med. Biol. Eng. Comput. 58 (12)
3089–3099.

[26] M.J. Warrens, A comparison of Cohen’s kappa and agreement coefficients

by Corrado Gini, Int. J. Res. Rev. Appl. Sci. 16 (2013) 345–351.

[27] H. Demirhan, rTableICC: An R package for random generation of 2x2xK

and RxC contingency tables, R J. 8 (1) (2016) 48–63.

[28] R. Artstein, M. Poesio, Inter-coder agreement for computational linguistics,

Comput. Linguist. 34 (4) (2008) 555–596.

[29] K.L. Gwet, Computing inter-rater reliability and its variance in the presence
of high agreement, Br. J. Math. Stat. Psychol. 61 (1) (2008) 29–48.
[30] W. Waegeman, L. Boullart, et al., An ensemble of weighted support vector
machines for ordinal regression, Int. J. Comput. Syst. Sci. Eng. 3 (1) (2009)
47–51.

[31] K. Hechenbichler, K. Schliep, Weighted K-Nearest-Neighbor Techniques and
Ordinal Classification, Collaborative Research Center 386, Discussion Paper
399, 2004, http://dx.doi.org/10.5282/ubm/epub.1769.

[32] B.-Y. Sun,

J. Li, D.D. Wu, X.-M. Zhang, W.-B. Li, Kernel discriminant
learning for ordinal regression, IEEE Trans. Knowl. Data Eng. 22 (6) (2010)
906–910.

[33] M. Kuhn, K. Johnson, et al., Applied Predictive Modeling, Vol. 26, Springer,

2013.

[35]

[34] M.C. Heredia-Gómez, S. García, P.A. Gutiérrez, F. Herrera, Ocapis: R package
for ordinal classification and preprocessing in scala, Prog. Artif. Intell. 8 (3)
(2019) 287–292.
J. Demšar, Statistical comparisons of classifiers over multiple data sets, J.
Mach. Learn. Res. 7 (2006) 1–30.
J. Gross, U. Ligges, nortest: Tests for normality, 2015, URL: https://CRAN.R-
project.org/package=nortest, R package version 1.0-4.
J. Fox, S. Weisberg, An R Companion To Applied Regression, third ed., Sage,
Thousand Oaks CA, 2019.

[36]

[37]

[11] D. Chicco, G. Jurman, The advantages of the Matthews correlation coeffi-
cient (MCC) over F1 score and accuracy in binary classification evaluation,
BMC Genomics 21 (1) (2020) 6.

[12] R. Delgado, X.-A. Tibau, Why Cohen’s Kappa should be avoided as
performance measure in classification, PLoS One 14 (9) (2019) e0222916.
[13] L. Gaudette, N. Japkowicz, Evaluation methods for ordinal classification,
in: Y. Gao, N. Japkowicz (Eds.), Advances in Artificial Intelligence, Springer
Berlin Heidelberg, Berlin, Heidelberg, 2009, pp. 207–210.

[14] S. Baccianella, A. Esuli, F. Sebastiani, Evaluation measures for ordinal
regression, in: 2009 Ninth International Conference on Intelligent Systems
Design and Applications, IEEE, 2009, pp. 283–287.
J.S. Cardoso, R. Sousa, Measuring the performance of ordinal classification,
Int. J. Pattern Recognit. Artif. Intell. 25 (08) (2011) 1173–1195.

[15]

[16] A.E. Yilmaz, T. Saracbasi, Assessing agreement between raters from the
point of coefficients and log-linear models, J. Data Sci. 15 (1) (2017) 1–24.
[17] D. Tran, A. Dolgun, H. Demirhan, Weighted inter-rater agreement measures
for ordinal outcomes, Comm. Statist. Simulation Comput. 49 (4) (2020)
989–1003.

[18] K.L. Gwet, Handbook of Inter-Rater Reliability: The Definitive Guide To
Measuring the Extent of Agreement Among Raters, Advanced Analytics,
LLC, 2014.

[19] A. Sellami, S. Tabbone, Deep neural networks-based relevant latent repre-
sentation learning for hyperspectral image classification, Pattern Recognit.
121 (2022) 108224.

[20] A. Ben-David, Comparison of classification accuracy using Cohen’s

Weighted Kappa, Expert Syst. Appl. 34 (2) (2008) 825–832.

[21] S. García, A. Fernández, J. Luengo, F. Herrera, A study of statistical tech-
niques and performance measures for genetics-based machine learning:
accuracy and interpretability, Soft Comput. 13 (10) (2009) 959.

[22] T. Saito, M. Rehmsmeier, The precision-recall plot is more informative than
the ROC plot when evaluating binary classifiers on imbalanced datasets,
PLoS One 10 (3) (2015) e0118432.

[23] A. Korotcov, V. Tkachenko, D.P. Russo, S. Ekins, Comparison of deep
learning with multiple machine learning methods and metrics using
diverse drug discovery data sets, Mol. Pharm. 14 (12) (2017) 4462–4475.

16

<!-- MARKITDOWN CONVERSION -->

<!-- Full MarkItDown conversion for formatting fidelity. -->

AppliedSoftComputing134(2023)110020
ContentslistsavailableatScienceDirect
AppliedSoftComputing
journalhomepage:www.elsevier.com/locate/asoc
Weightedkappameasuresforordinalmulti-classclassification
performance
AyferEzgiYilmaza,HaydarDemirhanb,∗
aDepartmentofStatistics,HacettepeUniversity,Ankara,Turkey
bMathematicalSciencesDiscipline,SchoolofScience,RMITUniversity,Melbourne,Australia
a r t i c l e i n f o a b s t r a c t
Articlehistory: Assessing the classification performance of ordinal classifiers is a challenging problem under imbal-
Received10March2022 anced data compositions. Considering the critical impact of the metrics on the choice of classifiers,
Receivedinrevisedform18December2022 employing a metric with the highest performance is crucial. Although Cohen’s kappa measure is
Accepted5January2023 used for performance assessment, there are better-performing agreement measures under different
Availableonline13January2023
formationsofordinalconfusionmatrices.Thisresearchimplementsweightedagreementmeasuresas
Keywords: evaluationmetricsforordinalclassifiers.Theapplicabilityofagreementandmainstreamperformance
Accuracy metrics to various practice fields under challenging data compositions is assessed. The sensitivity
Agreementmeasures of the metrics in detecting subtle distinctions between ordinal classifiers is analyzed. Five kappa-
Evaluationmetric like agreement measures with six weighting schemes are employed as evaluation metrics. Their
Matthewscorrelationcoefficient reliability/usefulness is compared to the mainstream and recently proposed metrics, including F1,
Performancemetric Matthews correlation coefficient, and informational agreement. The performance of 37 metrics is
Ordinalclassifier
analyzedintwoextensivenumericalstudies,includingsyntheticconfusionmatricesandrealdatasets.
Ordinallabels
Promisingmetricsunderpracticalcircumstancesareidentified,andrecommendationsaboutthebest
metrictoevaluateordinalclassifiersunderdifferentconditionsaremade.Overall,theweightedScott’s
pi-measureisfounduseful,sensitivetosmalldifferencesintheclassificationperformance,andreliable
undergeneralconditions.
©2023TheAuthor(s).PublishedbyElsevierB.V.ThisisanopenaccessarticleundertheCCBY-NC-ND
license(http://creativecommons.org/licenses/by-nc-nd/4.0/).
1. Introduction the performance of ordinal classifiers with the highest possible
accuracy.
Classifying subjects into multiple ordinal classes, namely or- The evaluation of ordinal classifiers’ performance is directly
dinal multi-class classification or ordinal classification, is one of related to the used evaluation metric and the characteristics of
themostfrequentexercisesofautomaticclassificationsystemsin the training or test dataset, which we call ‘‘the composition of
patternrecognition,machinelearning,anddeeplearningsystems. thedataset’’throughoutthemanuscript.Whenthedistributionof
Theproblemconsideredhereistoassigneachobjectinasample subjects into ordinal classes is imbalanced, mainstream metrics
to one of the ordered classes of a categorical response variable such as accuracy, precision, and recall are negatively impacted;
using an ordinal classifier. In pattern recognition, ordinal multi- hence,theydonotpreciselyassessclassifiers’performance[5,6].
class classification is used in the classification of different types Therefore,theuseofothermeasuressuchasF1score[7],Cohen’s
ofimagessuchashyperspectralimages[1],data-likeimages[2], (weighted)κ (kappa)-measure[8]andMatthewscorrelationco-
radar images [3], or images from medical diagnosis systems [4]. efficient (MCC) [9] is proposed. MCC is observed to perform
Accurate evaluation of ordinal classifiers’ performance is a chal- better than the F1 score and κ-measure for binary classifica-
lenge under different circumstances of data. Therefore, many tion[10,11].Formulti-classclassification,Ráczetal.[6]identify
metricshavebeenproposedtoevaluateclassifiers.Thequalityof better performance for F1 score than MCC and find that MCC is
training a model or network is related to the preciseness of the more sensitive to the data composition. Although Rácz et al. [6]
classifier against true classes in a labeled dataset [4]. A metric
includeCohen’sunweightedκintheirstudy,theydonotgiveany
can also be used as a loss function to optimize in an image specific inference about the comparison of Cohen’s unweighted
classification system [4]. In this sense, it is crucial to evaluate
κ-measuretoF1scoreandMCCforordinalclassifiers.Theuseof
Cohen’slinearorquadraticweightedandunweightedκ-measures
∗ is found suitable for assessing the performance of multi-class
Correspondingauthor.
classifiers [8]. However, Czodrowski [8] do not distinguish or-
E-mailaddresses: ezgiyilmaz@hacettepe.edu.tr(A.E.Yilmaz),
haydar.demirhan@rmit.edu.au(H.Demirhan). dinal classifiers. Cohen’s unweighted κ-measure is compared to
https://doi.org/10.1016/j.asoc.2023.110020
1568-4946/©2023TheAuthor(s). PublishedbyElsevierB.V.ThisisanopenaccessarticleundertheCCBY-NC-NDlicense(http://creativecommons.org/licenses/by-
nc-nd/4.0/).

A.E.YilmazandH.Demirhan AppliedSoftComputing134(2023)110020
a bunch of metrics, including the F1 score in the accuracy of research are to (i) explore the precision/usefulness of weighted
assessing the performance of binary and multi-class classifiers agreement measures as evaluation metrics for ordinal classi-
for balanced and imbalanced data compositions by Ferri et al. fiers, (ii) compare the versatility of agreement metrics and the
[5], without specifically accounting for ordinal classifiers. It is mainstreammetricsunderchallengingcompositionsofconfusion
observed that the unweighted κ-measure shows similar per- matrices in different fields of practice for ordinal classification,
formance as the metric called accuracy for multi-class classi- and (iii) identify the promising metrics under practical circum-
fiers in general. However, it shows similar performance with stancesandmakerecommendationsaboutthebestmetrictouse
the F1 score for large datasets with more than 1000 observa- fortheevaluationofordinalclassifiers.
tions[5].Seriousconcernshavealsobeenraisedagainsttheuse To fulfill the aims, our objectives are to (i) implement the
of Cohen’s κ-measure in assessing the performance of multi- weightedagreementmeasuresfortheevaluationofordinalclas-
class classifiers. There is a strong correlation between Cohen’s sifiers for balanced and imbalanced data compositions, (ii) con-
unweightedκ-measureandMCC,andhighκ valuesareobserved ductanumericalstudywithsyntheticconfusionmatricestosee
forpoorlyperformingclassifierswithimbalanceddatawhileMCC thequalityofthemetricsundercontestingcompositionsofcon-
was insensitive to this case [12]. Specifically, mean absolute er- fusion matrices, and (iii) run a second numerical study with the
ror (MAE), its variations, and mean squared error (MSE) are outputsofordinalclassifierswithrealdatafromavastvarietyof
considered for the evaluation of ordinal classification perfor- thefieldstoassessthesensitivityofmetricstosmalldifferences
manceunderimbalanceddatacompositions[13,14].Cardosoand between ordinal classifiers. Under these objectives, we consider
Sousa[15]proposeanordinalclassificationindex(OCI),consider weighted versions of κ, π, α, BP and AC2 metrics and compare
Misclassification Error Rate (MER) for ordinal classification per- their performance against the mainstream metrics accuracy, re-
formance,andcompareMERwithMAEandMSE.However,they call, precision, F1, MCC and the recently proposed informational
do not consider mainstream and (weighted) agreement metrics agreementthroughtwoextensivenumericalstudies.Intotal,we
consider 37 metrics and assess them under artificially created
forordinalclassificationperformance.
In image classification studies, Cohen’s κ-measure is found scenarioscomposedofthetrueperformanceoftheclassifier,the
degree of imbalance in the data (the composition of data), and
useful for assessing multi-class classifiers’ performance. Some
differentmisclassificationscenariosfortheclassesoftheordinal
performance comparisons among well-known metrics, F1 score
and Cohen’s κ are reported. The grounds for using kappa-like dependent feature in the first numerical study. This numerical
studyrevealsthemetrics’performance/usefulnessundervarious
agreementmeasurestoassessmulti-classclassifiers’performance
confusion matrix formations. In the second numerical study, we
is that the confusion matrix is essentially a cross table showing
compare the metrics in terms of their sensitivity in distinguish-
the agreement between two raters, represented by the obser-
ing two classifiers with similar classification performance using
vations and estimations. In this case, the confusion matrix is
40 real datasets, including balanced, imbalanced, and extremely
taken as an ‘‘agreement table’’ that shows the classification of
imbalanced data compositions from social science, life sciences,
tworatersintomultipleclassesofanoutcomevariable.Then,the
engineering, and other areas of practice. This numerical study
levelofagreementbetweentworatersisequivalenttothelevelof
is important to observe the ability of metrics to perceive even
goodnessofclassification.Inthissense,allkappa-likeagreement
smalldifferencesinclassificationperformance,whichisahighly
measures can be considered as an evaluation metric for ordinal
classifiers. However, Cohen’s κ-measure is proposed to be used desiredqualityforanevaluationmetric.Thecontributionsofthis
study are that (i) we explore the performance of a wide range
when there is no ordering among the classes of the variable of
of unweighted and weighted agreement measures as metrics
interest (nominal type classes). Thus, it does not consider the
forordinalmulti-classclassifiers,(ii)comparativelyexaminethe
degree of deviance from the main diagonal of the classification.
performanceofthemainstreammetrics,and(iii)identifyametric
For example, in classifying objects in images into the classes
thatissuperiortothemainstreammetricsthatcanbeusedunder
‘‘bicycle’’,‘‘car’’,‘‘airplane’’,threeclassesareofnominaltypesince
different data compositions and areas of practice as a generic
there is no hierarchy among them. When there is a hierarchy
metric.
amongtheclasses(ordinaltypeclasses),weneedtoconsiderthis
Section2outlinestherelatedworksintheliterature.Section3
hierarchy in the analysis. For example, diabetic retinopathy is a
describes the metrics considered in this study. Sections 4 and 5
serious disease that may lead to visual impairment and can be
presentthenumericalstudieswithsyntheticconfusionmatrices
prevented if detected early. For the detection, lesions related to
and real data. Section 6 is devoted to the general recommenda-
thediseasearescreenedinretinalimages,andaclassificationis
tionsanddiscussions.
donebasedontheseverityofstagesusingautomaticimageclas-
sificationtechniques[4].Duetothenaturalhierarchyamongthe 2. Relatedworks
severitystages,wedealwithanordinalmulti-classclassification
problem.Inthiscase,theweightedversionofCohen’sκ-measure, The use of weighted κ and MCC as a loss function in deep
whichincludestheimpactofthedistancefromthemaindiagonal, learning models for image classification is considered by
is available for use. Since Cohen’s (weighted) κ-measure has de La Torre et al. [4] for general image classification and Kook
some drawbacks [16,17], other measures such as Gwet’s AC2, et al. [2] for the classification of complex data like images into
Scott’sπ(pi),Brennan–Prediger’sBP,andKrippendorff’sα(alpha)
ordinal classes. However, they only consider quadratic weights
are proposed in the agreement studies [18]. However, they are andCohen’sκ whiletherearebetter-performingalternatives.For
not considered as an evaluation metric for ordinal classifiers hyperspectral image classification, both Deng et al. [1] and Sel-
in the literature. When we consider ordinal classes, there are lami and Tabbone [19] employ accuracy and unweighted κ to
other weighting schemes besides linear and quadratic weights, evaluatetheirproposedmethodsformulti-classclassification.
such as ordinal, radical, ratio, circular, and bipolar weights to Ben-David[20]focusontheexpertsystemsforcost-sensitive
be used with weighted versions of the agreement measures to applications and propose a new strategy based on weighted κ-
accountfortheordinalityoftheclasses[18].Duetotheinterac- measuretoassesstheperformanceofmulti-classclassifiers.They
tion between the assumptions behind agreement measures and only consider unweighted, linear and quadratic weighted Co-
weighting schemes, each weighted agreement measure would hen’s κ-measure without distinguishing imbalance in data and
performsatisfactorilyinmeasuringaclassifier’sperformanceun- comparing the accuracy of κ-measure to others such as accu-
der a different data composition. Therefore, the aims of this racy, precision, recall, and F1 score. García et al. [21] consider
2

A.E.YilmazandH.Demirhan AppliedSoftComputing134(2023)110020
Cohen’sunweightedκ-measureandclassificationrateformulti- composition and observe that AUC and MCC have consistent
classclassifiersforgenetics-basedmachinelearningimplementa- performance across different classifiers with imbalanced data
tions.Thisstudyshowsthattheprecisionofmetricscanvaryfor composition. Rácz et al. [6] conduct a statistical analysis on
classificationproblemsindifferentfieldsofapplication. the performance of 28 metrics, including unweighted κ, MCC,
Ferri et al. [5] conduct an extensive experimental study to F1 score, accuracy, diagnostic odds ratio, and AUC by taking
assessthereliabilityof18metricsinclassificationproblems.They data composition (imbalanced/balanced), level of classification
presentverydetailedbackgroundinformationaboutthedifferent (binary/multi-class), and the performance of metric as factors
types of metrics, including their taxonomy. They only consider againstthesumofrankingdifferencesoverthreedatasets.They
theunweightedversionofκ-measureanddonotincludeMCCin observethatmostofthemetricsaresensitivetothecomposition
thecomparisonstudy.SomesimilaritiesbetweentheF1scoreand ofthedatasetandtheF1scoreandthediagnosticoddsratioare
κ-measure,andaccuracyandκ-measureareobservedfordiffer- theleastsensitiveones.Wardhanietal.[24]focusonimbalanced
entcompositionsofdatabyFerrietal.[5].Czodrowski[8]studies datacompositionandcomparethereliabilityofF1score,g-mean,
theadvantagesanddisadvantagesofCohen’sunweightedκ asa MCC,unweightedκ,andAUCmetricsoveranempiricalstudyon
metric of performance for the classification problem in machine the cabbage image classification. They observe that accuracy, F1
learning and cheminformatics. He creates various data compo- score, g-mean, MCC, and κ provide similar results for different
sitions to compare the reaction of precision, recall, accuracy, κ, confusionmatriceswhileAUCissensitivetothechanges.When
prevalence, and bias and observes that κ-measure is a useful the degree of imbalance is high, Wardhani et al. [24] suggest
metric within this set of metrics. Saito and Rehmsmeier [22] not to use MCC and unweighted κ-measure to avoid misleading
compare the performance of precision/recall plots to Receiver results.
OperatingCharacteristics(ROC)plotsinassessingthebinaryclas- Inrecentstudies,Casagrandeetal.[25]proposeanewmetric
sifiers on imbalanced data. They consider the metrics computed calledinformationalagreement(IA)tomeasurethestrengthbe-
tweentwoassessorsforbinaryandmulti-classlabelstoavoidthe
usingtheinformationintheconfusionmatrix,suchasaccuracy,
disadvantagesofκ-measure.TheytestIAunderthecaseswhere
F1 score, MCC, and precision and observe that performance of
theκ-measuregivesproblematicresultsbytakingtwodiagnostic
precision/recallplotsissuperiortoROCplots.Korotcovetal.[23]
classifiersasassessors.DelgadoandTibau[12]focusonthesim-
compare the performance of deep neural networks to that of
ilaritiesanddifferencesbetweenCohen’sunweightedκ-measure
mainstream machine learning methods by using AUC, F1 score,
Cohen’s unweighted κ and MCC. They observe similar κ and andMCCundervariouscompositionsoftheconfusionmatrixfor
binaryandmulti-classclassifiers.Theytheoreticallyandnumeri-
MCCvaluesforimplementingdeeplearningandmachinelearn-
callystudytheequivalencebetweenMCCandunweightedκ and
ing methods with pharmaceutical data. Since we work with the
figureouttheformationsofconfusionmatrixwhereunweighted
metrics relying on the qualitative understanding of error that
κ should be avoided. Chicco and Jurman [11] consider MCC and
take the number of false classifications into account [5] in this
observeitsadvantagesovertheF1scoreandaccuracyforbinary
study, we do not consider either ROC or AUC. The metrics, such
classification. They conclude that MCC is a more reliable metric
as logarithmic loss, require prediction probabilities. However,
for assessing performance for binary classifiers and should be
we directly work with the confusion matrices for better gener-
preferredoveraccuracyandF1score.
alizability instead of working with a specific model. Therefore, There is a close theoretical relationship between κ-measure
metrics requiring prediction probabilities are not considered in
and MCC [12,26] when the confusion matrix is symmetric. Del-
thisstudy. gado and Tibau [12] also observe that κ-measure differs from
Forordinalmulti-classclassification,itisessentialtoaccount
MCC and is not reliable under imbalanced compositions of data.
for the severity of the error. In that sense, the use of metrics
This result motivates us to explore other alternatives of
that do not count for the magnitude of the error, such as ac- κ-measure to identify a better metric for assessing the perfor-
curacy metric, is not suitable [13,15]. Gaudette and Japkowicz
mance of multi-class classifiers with imbalanced datasets. Dif-
[13] consider MAE and MSE to capture the magnitude of the
ferent to the existing studies, we consider four alternatives of
errorandfindthatMAEandMSEperformbetterthanthemetric the κ-measure with six weighting schemes under different data
accuracyforimbalanceddatasets.Baccianellaetal.[14]propose
compositionsinthisstudy.
macro-averaged versions of MAE for imbalanced datasets but
In general, different studies in different areas have produced
do not compare them with the mainstream metrics. When the
contradictory conclusions on the suitability of MCC and Cohen’s
number of ordinal levels increases, it is appropriate to use MAE κ-measure. Although the characteristics of different areas are
and MSE based on the approximation to the continuous scale.
influentialinthiscontradiction,thesestudiesarelimitedtotheir
However, when the number of levels is not large enough to
simulationornumericalexperimentationspaces.Thisisanother
support such an approximation, it is essential to identify the
motivationforconductingextensivenumericalstudieswithsyn-
promisingmetricsthatcapturethemagnitudeoferrorforordinal thetic and real data from different fields to explore the preci-
classification. Cardoso and Sousa [15] define OCI directly using sion/usefulnessofotherweightedagreementmeasuresasmetrics
the confusion matrix and consider the relative ordering of true formulti-classclassifiersforordinallabels.
andpredictedclasses(concordantanddiscordantpairs)andtheir
deviation from the main diagonal of the confusion matrix. The 3. Performancemetricsformulti-classclassifiers
weighted agreement metrics considered in this study capture
concordanceanddiscordanceintheconfusionmatrixandaccount Evaluationmetricsdifferaccordingtothewaytheyhandlethe
for the magnitude of discrepancy between the observed and error. The measures based on the qualitative understanding of
predictedclassificationofthelabels,inadditiontothedegreeof errortakeintoaccountthenumberoffalseclassifications.Those
similarity between them. Thus, figuring out the usefulness and regarding the probabilistic understanding of error are based on
efficiencyoftheweightedagreementmetricsintheevaluationof the distance from the true probability and are mostly used in
ordinalclassificationperformanceisanimportantcontribution. reliabilitystudies.Themetricsrelatedtotherankingaccuracyof
Boughorbel et al. [9] propose optimizing the metrics to han- the model are used when the classifiers are evaluated on how
dle the imbalance in data and develop a new binary classifier well they select a given number of best labels/subjects from a
based on the optimization of MCC for imbalanced data. They datasetsuchasrecommendersystems[5].Inthisarticle,wefocus
compare MCC, AUC, Accuracy, and F1 under imbalanced data onthemetricsrelyingonthequalitativeunderstandingoferror.
3

A.E.YilmazandH.Demirhan AppliedSoftComputing134(2023)110020
Table1 classmembershipsoflabelsusingthecellcountsofthecon-
Theconfusionmatrixforaclassifier. fusionmatrix.Ittakesvaluesin[−1,1]where−1represents
Predictedclass Row thepoorest,and1showsperfectclassificationperformance:
Actualclass 1 2 . . . 1 n n . . . 1 2 1 1 2 n n . . . 1 2 2 2 . . . .. . . . . . . . n R n . . . 1 2 R R n n . . . m 1 2 a . . rgin MCC = √ (n2 n − ∑ ∑ R i=1 R i= n 1 ii n − 2 i.)( ∑ n2 R i= − 1 n ∑ i.n R i= .i 1 n2 .i ) . (6)
R nR1 nR2 ... nRR nR. • Informational agreement has recently been proposed by
Columnmargin n.1 n.2 ... n.R n Casagrande et al. [25] and is based on the amount of in-
formation (entropy) exchanged between the raters in the
agreementcontext.Intheclassificationperformanceassess-
ment, the higher the agreement between a classifier and
3.1. Mainstreammetrics theactualdistributionoflabels,thehighertheclassification
performanceoftheclassifier.Itiscomputedas
The confusion matrix for a multi-class classifier assigning n
labelsintoRclassesisshowninTable1.Therowsoftheconfusion MI(X,Y) ∑ R ( p )
matrix represent the actual classes, and the columns show the IA= , MI(X,Y)= p log ij ,
predicted classes. In Table 1, n ij denotes the number of labels
min{H(X),H(Y)}
i,j=1
ij R p i.p.i
that are actually in class i and predicted to be in class j, where
i,j = 1,2,...,R. The corresponding cell probability is p = (7)
ij
n ij /n. The row and column totals are shown as row and column ∑ R ∑ R
m
ar
a
e
rg
p
i
i
n
.
s,
=
re
n
sp
i. /
e
n
cti
a
v
n
e
d
ly.
p.
M
j
a
=
rgin
n
a
.j
l
/n
r
,
ow
res
a
p
n
e
d
ctiv
co
e
l
l
u
y.
m
S
n
in
p
ce
ro
t
b
h
a
e
bi
r
li
o
ti
w
es
-
H(X)=−
i=1
p i.log
R
(p i.), andH(Y)=−
i=1
p.i log
R
(p.i ).
totals of the confusion matrix are fixed by the frequencies in
the dataset, the sampling scheme we are working with is the 3.2. Weightedagreementcoefficients
product-multinomialsampling[27].
UsingtheconfusionmatrixinTable1,themainstreammetrics The weighted agreement coefficients are essentially used to
consideredinthisarticlearecalculatedasfollows: evaluate the level of agreement between two raters who clas-
sified the subjects into ordered categories. The general form for
• Accuracyisthemostcommonmetricdefinedastheratioof
agreementcoefficients(A)isdefinedasfollows:
correctlypredictedlabelstothetotalnumberoflabels.
Acc = ∑R i= n 1 n ii. (1) A= P 1 o − − P P e e ( ( A A ) ) , P o = i ∑ ,j R =1 w ij p ij , (8)
• Macro-average recall is also called balanced accuracy and where P is the observed agreement, P is the proportion agree-
o e
computedasthearithmeticmeanofrecallsforallclasses. ment expected by chance, w shows the weight assigned to cell
ij
M.Recall= ∑R i=1 R recall i, and recall i = ∑ R n ii /n i. . (2) ( c i o , e j T ) ff h i o c e f ie t g n h e t e n a e c n r o d a n l f i u s fo s c i r a o m l n c u u m l l a a t a t i t e o r d n ix a , o s a f g n K i d v r e i P p n e p i d e n e n p T d a e o b n r l f d e f s ’s 2 o . α n t m he ea a s g u r r e e em is en as t
i=1
follows[18]:
Themacro-averagerecalliscalled‘‘recall’’intherestofthe
• p a M r r a t e i c c c r i l o s e i - . o a n v s er o a v g e e r p R re c c l i a si s o s n es i . sdefinedasthearithmeticmeanof α w = ( 1− n 1 r¯ ) 1 p − a0 ∑ + R k n , 1 r l ¯ = − 1 w ∑ kl π R k, k l= π 1 k w kl π k π k, (9)
where
M.precision=
∑R
i=1 p R recision i, and precision i = ∑ i=
R
1 n ii /n.i . p a0 = 1 n ∑ n ∑ R r i r k ¯ ( ( r r ¯ ik − . − 1 1 ) ) , r¯ ik. = ∑ R w kl r il , and
(3)
i=1 k=1 i l=1
(10)
n
1∑
Macro-average precision is called ‘‘precision’’ in the rest of π k = r ik r¯.
n
thearticle. i=1
• Mean F1-score is calculated as the arithmetic mean of F1- WhilecomputingKrippendorff’sαforaconfusionmatrix,r =
ik
scoresoverRclasses. 2andr =r¯ =2·RinEqs.(9)and(10).
i
∑R F1 ( precision ×recall ) The critical distinction between agreement metrics is the as-
MeanF1= i=1 i, and F1 =2× i i . sumption about the marginal distributions of assessors, which
R i precision i +recall i corresponds to the confusion matrix’s margins in the classifica-
(4) tion performance context. One of the margins of the confusion
matrix is fixed by the total class frequencies in the data. There-
• MacroF1-scoreiscomputedastheharmonicmeanofmacro-
fore, the agreement coefficients calculated assuming that one of
averaged precision and macro-averaged recall, defined in
themarginsisfixedareexpectedtoperformbetterintheclassifi-
Eqs.(2)and(3),respectively.
cationperformanceevaluation.However,noneoftheagreement
( M.precision×M.recall ) coefficientshasthisassumptionstraightforwardly.Scott’sπ w as-
M.F1=2× M.precision+M.recall . (5) sumesthehomogeneityofmargins[28];hence,itisexpectedto
be a precise metric when the margins of the confusion matrix
• Matthewscorrelationcoefficient [9]giveninEq.(6)measures get closer. Krippendorff’s α does not require the margins of the
thedegreeofcorrelationbetweenthepredictedandactual confusionmatrixtobehomogeneous.Itinsteadcountswherethe
4

| A.E.YilmazandH.Demirhan |     |     |     |     |     |     |     | AppliedSoftComputing134(2023)110020 |     |     |     |
| ----------------------- | --- | --- | --- | --- | --- | --- | --- | ----------------------------------- | --- | --- | --- |
Table2
Thecalculationoftheproportionagreementexpectedbychance.
|     | Coefficient |     | Symbol | Pe  |     |     |     |     |     |     |     |
| --- | ----------- | --- | ------ | --- | --- | --- | --- | --- | --- | --- | --- |
∑R
|     |               |     | κ   | w             |     |     |     |     |     |     |     |
| --- | ------------- | --- | --- | ------------- | --- | --- | --- | --- | --- | --- | --- |
|     | Weightedkappa |     | w   | Pe = ijpi.p.j |     |     |     |     |     |     |     |
i,j=1
|     |           |     |     | ∑R        |      | (pi.+     |     |       |      |     |     |
| --- | --------- | --- | --- | --------- | ---- | --------- | --- | ----- | ---- | --- | --- |
|     |           |     | π   | = w       | ,    | = p.i)    |     |       |      |     |     |
|     | Scott’spi |     | w   | Pe ijpipj | pi   |           |     |       |      |     |     |
|     |           |     |     | i,j=1     |      | 2         |     |       |      |     |     |
|     |           |     |     | 1         | ( ∑R | ) ∑R      |     | (pi.+ | p.i) |     |     |
|     | Gwet      |     | AC2 | Pe =      | w    | pi(1−pi), |     | pi =  |      |     |     |
|     |           |     |     | R(R −1)   |      | ij        |     |       | 2    |     |     |
i,j=1 i=1
∑R
1 w
|     | Brennan–Prediger |     | BPw | Pe = | ij  |     |     |     |     |     |     |
| --- | ---------------- | --- | --- | ---- | --- | --- | --- | --- | --- | --- | --- |
R 2
i,j=1
classifier matches with the data in classifying the labels. There- patternaslinearweightsbutwithhighervaluesofweights.They
α get closer to quadratic weights toward the end of scale [18]. In
| fore, is expected | to be highly | sensitive | to misclassifications. |     |     |     |     |     |     |     |     |
| ----------------- | ------------ | --------- | ---------------------- | --- | --- | --- | --- | --- | --- | --- | --- |
κ-measure
Brennan–Prediger’sBPassumesthatthemarginaldistributionsof terms of the relationship between Cohen’s with no
the confusion matrix are uniform. Thus, BP is expected to work weight, linear, and quadratic weights, Warrens [26] shows that
|     |     |     |     |     |     | κ   | <   |     |     | κ   | <   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
well with balanced data compositions. Since Gwet’s AC2 adjusts ‘‘Cohen’s unweighted Cohen’s linear weighted Cohen’s
κ’’.
uniformityregardingthevariationineachclass,itcanhandlethe quadratic weighted The selection of weights is discussed in
unbalanceddatacompositionstoproducepreciseresults[29]. thelatersections.
The weighting schemes (w ) considered in this article are To implement the agreement coefficients as evaluation met-
ij
computed as given in Eqs. (11)–(15), where w = 1 when i = j rics, any agreement coefficient in Table 2 is calculated with one
ij
fori,j=1,2,...,R[18]. of the weighting schemes described in Eqs. (11)–(15) using the
|     |     |     |     | counts in | the | confusion | table | given | in Table | 1. Since | this cal- |
| --- | --- | --- | --- | --------- | --- | --------- | ----- | ----- | -------- | -------- | --------- |
• Unweighted:w =1. culation is straightforward and does not require any iterative
ij
• Linearweights: algorithms,thereisnodifferencebetweenthecomputationalcost
oftheagreementandthemainstreamevaluationmetrics.
|i−j|
| w =1− | .   |     |      |     |     |     |     |     |     |     |     |
| ----- | --- | --- | ---- | --- | --- | --- | --- | --- | --- | --- | --- |
| ij    |     |     | (11) |     |     |     |     |     |     |     |     |
R−1
4. Numericalexperimentswithsyntheticconfusionmatrices
• Quadraticweights:
4.1. Experimentspaceanddatageneration
(i−j)2
| w =1− | .      |     |      |                                                       |     |     |     |     |     |     |     |
| ----- | ------ | --- | ---- | ----------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
| ij    |        |     | (12) |                                                       |     |     |     |     |     |     |     |
|       | (R−1)2 |     |      | Inthisnumericalstudy,wecreatesyntheticconfusionmatri- |     |     |     |     |     |     |     |
cestoexaminethebehavioroftheevaluationmetricsmentioned
• Ordinalweights:
inSection3againstdifferentformationsoftheconfusionmatrix
|     |     |     |     | for a classification |     | task | into three | ordinal | classes. | We  | generate |
| --- | --- | --- | --- | -------------------- | --- | ---- | ---------- | ------- | -------- | --- | -------- |
M ij
w =1− , M =max(i,j)−min(i,j)+1 and confusionmatriceswithdifferentcharacteristicsforagiventrue
| ij  | M ij |     |     |     |     |     |     |     |     |     |     |
| --- | ---- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
max classificationperformance,calculateevaluationmetrics,andcom-
=max(M ).
M max ij pareevaluationmetricswiththetrueclassificationperformance.
|     |     |     |     | The generation |     | of confusion | matrices, |     | independent | of  | a specific |
| --- | --- | --- | --- | -------------- | --- | ------------ | --------- | --- | ----------- | --- | ---------- |
(13)
|     |     |     |     | model and | classifier, | allows | us  | to examine | a wide | range | of con- |
| --- | --- | --- | --- | --------- | ----------- | ------ | --- | ---------- | ------ | ----- | ------- |
• Radicalweights:
|     |     |     |     | fusion matrix |     | formations | that | can be | observed | in real | practice; |
| --- | --- | --- | --- | ------------- | --- | ---------- | ---- | ------ | -------- | ------- | --------- |
√
|       | |i−j| |     |     | hence,itprovidessufficientgeneralizability. |     |     |     |     |     |     |     |
| ----- | ----- | --- | --- | ------------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
| w =1− | √ .   |     |     |                                             |     |     |     |     |     |     |     |
ij (14) The generated scenarios include high (0.8), moderate (0.5),
|R−1|
|     |     |     |     | and low | (0.2) | levels of | true accuracy |     | for a classifier | which | also |
| --- | --- | --- | --- | ------- | ----- | --------- | ------------- | --- | ---------------- | ----- | ---- |
• Bipolarweights: translate into high, moderate, and low performance in practice.
Here,thetrueaccuracy/performance(TA)isdefinedastheratioof
(i−j)2
w , correctlyclassifiedlabelstothenumberoflabelsineachclassin
| =1− |     |     | (15) |     |     |     |     |     |     |     |     |
| --- | --- | --- | ---- | --- | --- | --- | --- | --- | --- | --- | --- |
ij M(i+j−2)(2R−i−j) thedata(eithertestortrainingset).Therefore,themetriccalled
|     |     | (   | )   | accuracyisexpectedtogivesimilarvaluestoTAsubjecttosome |     |     |     |     |     |     |     |
| --- | --- | --- | --- | ------------------------------------------------------ | --- | --- | --- | --- | --- | --- | --- |
i− 2
whereM isthemaximumvalueof ( j) overthe randomvariationfromreplicatingtheexperiments.Inthissense,
|     |     | (i+j− | 2 )(2 R −i−j) |     |     |     |     |     |     |     |     |
| --- | --- | ----- | ------------- | --- | --- | --- | --- | --- | --- | --- | --- |
pairsof(i,j). accuracy will be used as a control metric to assess if the data
|                 |                    |                 |                    | generation   | approach | is         | sufficient | to  | generate        | the desired | levels   |
| --------------- | ------------------ | --------------- | ------------------ | ------------ | -------- | ---------- | ---------- | --- | --------------- | ----------- | -------- |
| Linear weights  | are proportional   | to the          | degree of misclas- |              |          |            |            |     |                 |             |          |
|                 |                    |                 |                    | of accuracy, | and      | the metric | accuracy   |     | is not compared |             | to other |
| sification made | by the classifier. | If a classifier | assigns a label    |              |          |            |            |     |                 |             |          |
metrics.
farther away from its true class, the penalty applied by linear Since one of the main factors impacting the metrics is the
weightsincreases.Thedegreeofpenaltyduetomisclassification balancednessofthedistributionoflabelsintothetargetclasses,
increases quadratically with the quadratic weights, while the balanced, imbalanced, and extremely imbalanced structures are
radicalweightspenalizemisclassificationatadegreebetweenthe created in combination with the true accuracy. This factor is
linear and quadratic weights. Since the ordinal weights account calledthestructureofthetable(ST)intherestofthemanuscript.
fortheranksofassignmentsdonebytheclassifier,onlytheranks Basedontheclassifier’sperformanceandtheareaofinterest,the
are reflected in the weights. Bipolar weights produce a similar accuracyofclassificationmaydifferacrosstheordinalclasses.To
5

A.E.YilmazandH.Demirhan AppliedSoftComputing134(2023)110020
accountforthis,thefollowingcasesarecreatedbyusingdifferent get worse in accurately capturing true accuracy. For high and
p settings: moderate true accuracy, Cohen’s κ and Scott’s π with ordinal
ij
weightsmeasuretheclassificationperformanceaccuratelyforall
1. Labelsbelongingtoall3classesareclassifiedwithanaccu- cases. When the true accuracy is low, unweighted or quadratic
racyclosetothetrueaccuracy. weightedAC2performsbetterthanothermeasuresforallcases.
2. Labels belonging to 2 out of 3 classes are classified with We observe that mainstream metrics have a slightly better or
anaccuracyclosetothetrueaccuracy,andthelastoneis similar performance for balanced situations with high true ac-
classifiedwithlowaccuracy. curacythanordinalweightedCohen’sκ andScott’sπ measures.
3. Labelsbelongingtoonlyoneof3classesareclassifiedwith However, if the true accuracy is at lower levels and the classi-
an accuracy close to the true accuracy, and the remaining fication accuracy is not distributed evenly as in Cases 2 and 3,
onesareclassifiedwithlowaccuracy. ordinalweightedCohen’sκ andScott’sπ andquadraticweighted
AC2performbetterforbalanceddatacompositions.Followingthe
Thisfactorisnamed‘‘Case’’inthenumericalstudyanddenoted
theoreticalresultsofDelgadoandTibau[12],Cohen’sunweighted
asCase1,2,and3throughoutthemanuscript.Case1isthebest κproducessimilarvaluestoMCCinallthescenariosforbalanced
scenariowheretheclassifierperformsequallywellforallclasses. data composition. There are small deviations between Cohen’s
Thus,weexpectametricvalueclosetothegiventrueaccuracy. unweightedκ andMCCforCases2and3.Asexpected,MAEand
In Cases 2 and 3, the classifier fails to work sufficiently for at RMSEvaluesgetslightlysmallerasthesamplesizeincreasesfor
leastoneofthethreeclasses.So,evenforhightrueaccuracy,the allmetrics.
classifier’sperformanceispoorforCase2andpoorerforCase3. The results for imbalanced data compositions are generally
Sincetheclassifierdoesnotperformwell,weexpectlowervalues similar to those observed for balanced datasets. MCC and IA
thanthegiventrueaccuracyinCases2and3. produce high error values for high and moderate levels of TA.
The confusion matrices are generated using the product- Mainstream metrics perform well when the classifier’s perfor-
multinomial sampling scheme for the sample sizes of 50, 100, mance is homogeneous across the ordinal levels and the true
200, and 500 for each combination of ST, TA, and Case. Each accuracyishighormoderate.ThemeanF1isthebest-performing
scenario is replicated 1000 times. The p ij values are created to mainstream classifier. Cohen’s κ and Scott’s π with quadratic
reflect the ordinal classes, and the combinations of ST, TA, and weights have very similar MAE and RMSE values to mainstream
CaseareusedasinputsoftherTable.RxC()functionofrTableICC metrics except for MCC and IA for these scenarios. However,
package of R software [27]. We arbitrarily distort the given true whentheTAisreduced,andtheclassifier’sperformanceisbetter
accuracy in Cases 2 and 3 to create situations that can occur forsomeclassesandworsefortheotherclasses(Cases2and3),
in real practice. The resulting synthetic confusion matrices are quadraticorordinalweightedCohen’sκ andScott’sπ producea
showninTableA.1ofAppendixA.Togenerateordinalclasses,we promising performance that is better than mainstream metrics
followtheapproachexplainedbyTranetal.[17,seep.996–997]. for most of the scenarios. For low TA under imbalanced data
We use mean absolute error (MAE) and root mean squared composition, AC2, BP, and Krippendorff’s α perform better than
error(RMSE)giveninEq.(16)tocomparethemetricsundereach the mainstream and other agreement metrics when only one of
simulationscenario. theclassesiscapturedwithanaccuracycloseto0.2.Weobserve

r  r slight decreases in MAE and RMSE for increasing sample sizes
MAE = 1∑ |X−X ˆ| and RMSE =  √ 1∑ (X−X ˆ )2, (16) withimbalanceddatacomposition.
i i
r r Whenthedatacompositionisextremelyimbalanced,MAEand
i=1 i=1
RMSE values of the mainstream metrics considerably increase if
where r is the number of replications, X is the true value of ac- theclassifierdoesnotperformequallywellinallclasses.Forhet-
ˆ
curacy,andX i istheperformanceorweightedagreementmetric erogeneous classifier performance across the classes, quadratic
estimationintheithreplication. weighted Cohen’s κ and Scott’s π generate better performance
estimatesthanmainstreammetricsforallsamplesizes.Forlower
4.2. Results TA,theunweightedAC2isthebestmetricamongtheagreement
metrics for all cases. It performs better than the mainstream
The mainstream metrics’ RMSE and MAE values for all sam- metricsforsamplesizesgreaterthan50.
ple sizes, balanced, imbalanced, and extremely imbalanced data
compositionsaregiveninTableA.2,A.4,...,A.12ofAppendixA. 4.3. Conclusions
ThosefortheweightedagreementmetricsaregiveninTableA.3,
A.5,...,A.13ofAppendixA.Inthissection,‘‘mainstreammetrics’’ Among the mainstream metrics, MCC and IA produce no-
refer to the metrics described in Section 3.1 except accuracy. tably larger MAE and RMSE values than most of the metrics in
Since we use the definition of accuracy to generate confusion most scenarios. The mainstream metrics, except for MCC and
matrices, we exclude it from the inferences in this section. For IA, successfully identify the performance of classifiers when the
a full picture of comparisons between the mainstream and the data composition is balanced, and all three ordinal classes are
weighted agreement metrics, the reader should refer to pairs of capturedequallysuccessfully.Forthescenariosthatdeviatefrom
Table A.2 and A.3, A.4 and A.5, and so on. The inferences in this theseidealconditions,errormarginsincreaseforthemainstream
sectionarealsomadebyconsideringthesepairsoftables. metrics.
TheresultsinAppendixAshowthataccuracyisverycloseto For the agreement measures, we observe the theoretical re-
TA, as expected in all the scenarios considered. When the data lationshipbetweenMCCandCohen’sκ demonstratedby[12,26]
compositionisbalanced,mainstreammetricsexceptforMCCand in practice through the synthetic datasets when all the classes
IAandmostagreementmetricsproduceaccuratemeasurements are assigned with similar success by the classifier and the data
ofclassifierperformanceforCase1foralllevelsofTAandsample composition is balanced. However, this theoretical relationship
sizes. MCC and IA produce large MAEs and RMSEs, in general. is not observed under the deviations from this well-balanced
Astheclassifier’sperformancebecomesheterogeneousacrossthe scenario.
classes(movingfromCase1to2and3)andTAreducestolower For the rest of the weighted agreement measures, a wide
levels (the classification task gets harder), mainstream metrics range of different values are observed, implying that agreement
6

| A.E.YilmazandH.Demirhan |     |     |     |     |     |     |     |     |     |     | AppliedSoftComputing134(2023)110020 |     |     |     |     |
| ----------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----------------------------------- | --- | --- | --- | --- |
measures are sensitive to different data compositions and true We aim to create 10 folds of data from each dataset if it has
accuracy levels and have the potential to be used as reliable, more than 100 labels. Since the confusion matrix becomes very
useful metrics for multi-class classifiers. Specifically, Cohen’s κ sparse for the datasets with less than 100 labels, we create 2
and Scott’s π with quadratic weights show the best MAE and foldsforlsci2,lsci4,lsci13,eng1,other2,andother7datasets.We
RMSE performance for high and moderate true agreement, data run the computations separately for the full dataset, balanced,
| composition | scenarios,      |     | and classification |         | cases.   | Since   | Scott’s π |              |           |       |                |      |           |        |          |
| ----------- | --------------- | --- | ------------------ | ------- | -------- | ------- | --------- | ------------ | --------- | ----- | -------------- | ---- | --------- | ------ | -------- |
|             |                 |     |                    |         |          |         |           | imbalanced,  | extremely |       | imbalanced,    | life | sciences, | social | science, |
| assumes     | the homogeneity |     | of                 | margins | [28], it | returns | low error |              |           |       |                |      |           |        |          |
|             |                 |     |                    |         |          |         |           | engineering, | and       | other | areas datasets |      | for each  | fold.  | Since we |
valueswhenthemarginsoftheconfusionmatrixgetcloser(the
|     |     |     |     |     |     |     |     | cannot | create | 10 folds | for every | dataset, | we  | have | a different |
| --- | --- | --- | --- | --- | --- | --- | --- | ------ | ------ | -------- | --------- | -------- | --- | ---- | ----------- |
true agreement is moderate or high under all cases). However, number of replications for each run composed of datasets and
whenthetrueagreementislow,wedeviatefromthiscase;hence, their folds, as given in Table 3. For example, for the run with
otheragreementmeasuresperformbetter.Whenthetrueagree- ‘‘All datasets’’, we have 10 folds for 34 datasets and 2 folds for
ment is low, and data composition is imbalanced or extremely 6 datasets; in total, we run 352 replications for all datasets. For
imbalanced,weobservethatAC2giveslowMAEandRMSEvalues therunwith‘‘OnlyENG’’datasets,thereare10foldsfor3outof4
with different weights. The reason for Gwet’s AC2 to perform datasetsand2foldsfor1dataset,resultingin32replications.We
betteristhatAC2adjustsuniformityduetothevariationcreated utilizetherunsforthefoldsasreplicationstoconductstatistical
bythelowtrueagreementandimbalanceinthedata[29]. hypothesistests.
| All the | considered | mainstream |     | and | agreement |     | metrics are |        |                 |     |           |     |          |             |        |
| ------- | ---------- | ---------- | --- | --- | --------- | --- | ----------- | ------ | --------------- | --- | --------- | --- | -------- | ----------- | ------ |
|         |            |            |     |     |           |     |             | In the | implementation, |     | we employ |     | pairs of | classifiers | devel- |
sensitivetothesamplesize.WegetsmallerMAEandRMSEvalues
opedforordinaldata.Theclassifiersareselectedbyconsidering
| as the sample | increases. |     | The | benefit | of increasing |     | sample size |     |     |     |     |     |     |     |     |
| ------------- | ---------- | --- | --- | ------- | ------------- | --- | ----------- | --- | --- | --- | --- | --- | --- | --- | --- |
thattheyhavesimilaroverallclassificationperformances.Weas-
| on MAE | and RMSE | becomes | notable |     | when the | true | accuracy is |     |     |     |     |     |     |     |     |
| ------ | -------- | ------- | ------- | --- | -------- | ---- | ----------- | --- | --- | --- | --- | --- | --- | --- | --- |
sessifthemetricsareabletodifferentiatebetweentheclassifiers.
| high or   | moderate  | with | balanced | data | composition.   |     | When the  |                |     |         |            |              |     |                |     |
| --------- | --------- | ---- | -------- | ---- | -------------- | --- | --------- | -------------- | --- | ------- | ---------- | ------------ | --- | -------------- | --- |
|           |           |      |          |      |                |     |           | The difference |     | between | the actual | performances |     | of classifiers | is  |
| imbalance | increases | and  | one or   | two  | of the classes | are | correctly |                |     |         |            |              |     |                |     |
animportantconsiderationinassessingtheprecision/usefulness
classified(Case2and3),increasingthesamplesizedoesnothelp
|     |     |     |     |     |     |     |     | of the metrics. |     | Conceivably, | in  | real practice, |     | the precision | of  |
| --- | --- | --- | --- | --- | --- | --- | --- | --------------- | --- | ------------ | --- | -------------- | --- | ------------- | --- |
reducethevaluesofMAEandRMSEbyaconsiderablemargin. metrics is not a very important issue if one of the classifiers is
Overall,whenthedatacompositionisimbalancedforthesyn- performingfarbetterthantheother.Thesuccessofametriclies
thetic confusion matrices, the agreement measures mostly with initsabilitytodistinguishtheclassifierswhentheirperformances
ordinal weights produce lower error measures than the main- are close to each other. Therefore, to create two classifiers with
| stream metrics |     | and IA | for most | cases. | They | are more | sensitive |     |     |     |     |     |     |     |     |
| -------------- | --- | ------ | -------- | ------ | ---- | -------- | --------- | --- | --- | --- | --- | --- | --- | --- | --- |
similarperformance,weusetwoclassifiersfromthesameclassi-
thanMCCagainstunsuccessfulclassificationinatleastoneofthe
|          |          |             |     |       |                    |     |           | fication    | method  | with slight | changes         | in  | their | parameter | settings.  |
| -------- | -------- | ----------- | --- | ----- | ------------------ | --- | --------- | ----------- | ------- | ----------- | --------------- | --- | ----- | --------- | ---------- |
| classes. | However, | we need     | to  | study | the response       | of  | agreement |             |         |             |                 |     |       |           |            |
|          |          |             |     |       |                    |     |           | We consider | support |             | vector machines |     | with  | ordered   | partitions |
| metrics  | to the   | composition | of  | data  | in a generalizable |     | setting   |             |         |             |                 |     |       |           |            |
(SVMOP),whichisdevelopedforclassificationintoordinalclasses
| to identify | which | agreement |                 | measure | and        | weighting | scheme     |                      |     |              |          |           |     |               |         |
| ----------- | ----- | --------- | --------------- | ------- | ---------- | --------- | ---------- | -------------------- | --- | ------------ | -------- | --------- | --- | ------------- | ------- |
|             |       |           |                 |         |            |           |            | by Waegeman          |     | et al. [30], | weighted | K-nearest |     | neighbors     | for or- |
| combination | can   | be used   | for performance |         | assessment |           | of ordinal |                      |     |              |          |           |     |               |         |
|             |       |           |                 |         |            |           |            | dinal classification |     | (WKNNOR)     |          | proposed  | by  | Hechenbichler | and     |
multi-classclassifiersandhowtheirusageiscomparedtothatof
Schliep[31],andkerneldiscriminantlearningforordinalregres-
themainstreammetrics,MCCandtherecentlyintroducedmetric
|              |          |     |         |     |           |           |       | sion (KDLOR) |            | proposed     | by Sun   | et al. | [32]. There | can    | be other |
| ------------ | -------- | --- | ------- | --- | --------- | --------- | ----- | ------------ | ---------- | ------------ | -------- | ------ | ----------- | ------ | -------- |
| IA. For this | purpose, | we  | conduct | an  | extensive | numerical | study |              |            |              |          |        |             |        |          |
|              |          |     |         |     |           |           |       | choices      | of ordinal | classifiers. | However, |        | since       | we are | not com- |
withrealdatasetsinthenextsection.
|     |     |     |     |     |     |     |     | paring the | performance |     | of actual | classifiers/classification |     |     | meth- |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------- | ----------- | --- | --------- | -------------------------- | --- | --- | ----- |
5. Numericalexperimentswithrealdata ods and need to get just confusion matrices out of classifiers,
|     |     |     |     |     |     |     |     | the choice | of SVMOP, |     | WKNNOR, | and KDLOR |     | classifiers | does not |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------- | --------- | --- | ------- | --------- | --- | ----------- | -------- |
poseanyproblemwiththegeneralizabilityoftheresultsonthe
5.1. Datasetsandclassifiers
performanceofthemetrics.
Theparametersγ
|         |            |       |          |                   |           |             |         |              |       | andcost | impacttheperformanceofSVMOP |        |       |        |           |
| ------- | ---------- | ----- | -------- | ----------------- | --------- | ----------- | ------- | ------------ | ----- | ------- | --------------------------- | ------ | ----- | ------ | --------- |
| In the  | numerical  | study | with     | real              | data, the | sensitivity | of 37   |              |       |         |                             |        |       |        |           |
|         |            |       |          |                   |           |             |         | classifiers, | which | use     | the Gaussian                | radial | basis | kernel | function. |
| metrics | of Section | 3 is  | assessed | in distinguishing |           | ordinal     | classi- |              |       |         |                             |        |       |        |           |
Theγ parameteradjuststhescaleoftheGaussiankernel.Alarge
fiers.Sincethereisnouniquemetrictobeusedasthegoldstan-
|     |     |     |     |     |     |     |     | scale γ | for a | given cost | creates | wide | classification |     | boundaries. |
| --- | --- | --- | --- | --- | --- | --- | --- | ------- | ----- | ---------- | ------- | ---- | -------------- | --- | ----------- |
dardfordeterminingthesuperiorityofonemetricoveranother,
Forsmallerscales,under-fittingoccursifclassificationboundaries
| we focus | on the | sensitivity | of  | metrics | to the | slight | difference |     |     |     |     |     |     |     |     |
| -------- | ------ | ----------- | --- | ------- | ------ | ------ | ---------- | --- | --- | --- | --- | --- | --- | --- | --- |
becomemorefocusedunderlimitedregionsofthespace[33,see
betweentheperformanceoftwoclassifiers.Itisadesiredquality
p.347–348].Anincreasedunder-fittingreducestheclassification
forametrictodistinguishsubtledifferencesintheclassification
performance. performance with the test set. We set the cost value for both
γ
Weuse40realdatasetshavingdependentfeatureswithmul- SVMOPs to 1 and use the parameter to create classifiers that
tiple ordinal classes. For the generalizability of the results, we have similar overall performance but make mistakes on ordinal
γ =
gather datasets from the main areas of practice: social sciences classes. We set the SVMOP classifiers to use with 1 and 10
(16), life sciences (13), engineering (4) and other areas (7). withcost =1forSVMOP andSVMOP ,respectively.
|     |     |     |     |     |     |     |     |     |     |     | 1   | 2   |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Datasets and their web links are given in Table B.1 of Appendix For WKNNOR classifiers, we use the Euclidean distance and
B.SummaryinformationaboutthedatasetsisgiveninTableB.2 Gaussiankernelforbothclassifiersandsetthenumberofneigh-
|             |     |            |      |         |         |     |             | bors differently |     | to create | two          | classifiers | with | slightly     | different |
| ----------- | --- | ---------- | ---- | ------- | ------- | --- | ----------- | ---------------- | --- | --------- | ------------ | ----------- | ---- | ------------ | --------- |
| of Appendix | B.  | The sample | size | of each | dataset | is  | given under |                  |     |           |              |             |      |              |           |
|             |     |            |      |         |         |     |             | performances.    |     | A KNN     | with a small | number      |      | of neighbors | tends     |
the‘‘#Labels’’columnofTableB.2.Forthedatasetshavingmore
toover-fit,butalargevalueofthenumberofneighborshasthe
| than 5000 | labels, | a sub-sample |     | of size | 1000 | is taken | randomly. |     |     |     |     |     |     |     |     |
| --------- | ------- | ------------ | --- | ------- | ---- | -------- | --------- | --- | --- | --- | --- | --- | --- | --- | --- |
potentialtocreateunder-fit[33,seep.160and352].Wesetthe
| Data composition |     | for each | dataset | is  | qualified | based | on the bal- |     |     |     |     |     |     |     |     |
| ---------------- | --- | -------- | ------- | --- | --------- | ----- | ----------- | --- | --- | --- | --- | --- | --- | --- | --- |
ancednessofmarginalprobabilities.Overall,wehave6balanced, number of neighbors to 20 for WKNNOR 1 and 5 for WKNNOR 2
8 imbalanced, and 26 extremely imbalanced datasets. We have to create a small discrepancy between the performances of the
sufficient coverage of the number of features ranging from 3 classifiersthatweexpecttheevaluationmetricstodistinguish.
to 56 and the number of ordinal classes from 3 to 11 among For KDLOR classifiers, we use the Gaussian kernel with dif-
the datasets. There are very small samples as well as very large ferent scales to create KDLOR and KDLOR classifiers. We set
|     |     |     |     |     |     |     |     |     |     |     | 1   |     | 2   |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
samples from a wide range of areas of practice included in this the scale of the Gaussian kernel to 1 and 5 for KDLOR and
1
numericalstudy. KDLOR , respectively. Since KDLOR is a kernel-based method,
2
7

A.E.YilmazandH.Demirhan AppliedSoftComputing134(2023)110020
Table3
Runs,datasets,andthecorrespondingnumberofreplications.
Runswith Numberofdatasets Datasetnumber Replications
Alldatasets 40 1to40 352
Onlybalanced 6 3,9,12,17,20,39 52
Onlyimbalanced 8 2,4,5,6,11,14,38,40 72
Onlyextremely 26 1,7,8,10,13,15,16, 228
Imbalanced 18,19,21to37
OnlySSCI 16 14to29 160
OnlyENG 4 30to33 32
OnlyLSCI 13 1to13 106
OnlyOTHER 7 34to40 138
Fig.1. Flowdiagramofthenumericalstudywithrealdata.Here,nshowsthenumberofdatasetsineachparticularrunasgiveninthesecondcolumnofTable3,
k=2,10,andthevaluesofmareshowninthelastcolumnofTable3foreachrun.
its performance is characterized by the kernel. The scale of the 5.2.1. Visualinspection
Gaussian kernel specifies the boundaries of the regions created The means of metrics, calculated by aggregating over 40
forclassification,similartoSVMOPs. datasets and folds, are given in Figs. 2, 3, and 4 for SVMOP,
Itshouldbenotedthatthesesettingsdonotensurethateither WKNNOR,andKDLORclassifiers,respectively,alongwithandthe
Classifier orClassifier undereachordinalclassificationmethod ± standard error limits. Note that the statistical significance of
1 2
will have superior performance. The superiority issue is outside differences is thoroughly discussed in the parts following these
thefocusofthisnumericalstudysinceweonlyneedtohaveone figures. In Figs. 2, 3, and 4, we see different behaviors for each
oftheclassifiersperformslightlydifferently.
groupofmetrics,namely,mainstream,Cohen’sκ,Scott’sπ,AC2,
BPandKrippendorff’sαforalltheordinalclassificationmethods.
We employ svmofit(), wknnor(), and kdlortrain() functions
There is no clear distinction between the values of metrics with
from OCAPIS R package [34] for the implementation of SVMOP,
differentweights.Forallthemainclassificationmethods,SVMOP,
WKNNOR, and KDLOR classifiers, respectively. The flow diagram
ofimplementationisgiveninFig.1.Wecreatek-folds,k=2,10 WKNNOR,andKDLOR,almostallmetricsshowthatClassifier 1 has
slightlybetterperformancethanClassifier .
of each dataset and implement k-fold cross-validation without For SVMOP classifiers (Fig. 2), weighte 2 d π metrics have no-
aggregatingtheresultscomingoutofthefolds. tably different behavior than all the other metrics. Weighted κ
and α metrics show similar results, while weighted AC2 and BP
5.2. Results metrics indicate a similar level of performance to each other.
However, AC2 and BP metrics do not distinguish SVMOP and
1
SVMOP ,whichisnotthedesiredresult.Inthissense,weighted
Results are composed of the values of 37 metrics observed 2
π metrics show the highest difference between the classifiers.
over 2 sub-classifiers under each of 3 main classification meth-
Among the mainstream metrics, macro recall, macro precision,
ods, 40 real datasets, and replications from k-folds. The real
and macro F1 are close to each other, while IA and accuracy
datasetsarealsodividedintocategoriesbasedontheirbalanced-
showasimilarperformance.MCCistheonlymainstreammetric
ness and the field of application. We follow Demšar [35] to
that shows a slight difference between the classifiers. Overall,
provide statistical evidence on the significance of the difference weighted π metrics are able to distinguish the classifiers as
betweenmetricsacrossthefactorsusedforcomparisons.Weuse
desired, while none of the mainstream metrics is capable of for
multi-way analysis of variance (ANOVA) and Tukey’s pairwise
theSVMOPmethod.
comparisontesttoidentifythemetricsthatproducesignificantly
ForWKNNORclassifiers(Fig.3),weightedAC2andBPindicate
different values between classifiers under each main classifica-
considerably higher performance for both classifiers than the
tion method. In this way, we identify the sensitive metrics to othermetrics.Thefirstclassifierisfoundtobeslightlybetterby
separate the classification performance of two similar classifiers all the agreement measures. Since the mean metric values have
from each other. The normality and homogeneity of variances the lowest standard errors for the WKNNOR classifiers, distin-
assumptions of ANOVA [35] need to be ensured to get valid guishingbetweentwoclassifiersbecomesevenmorechallenging.
inferences from ANOVA. For this aim, the Kolmogorov–Smirnov The mainstream metrics, except accuracy and IA, are insensitive
normalitytestandLenevetestforthehomogeneityofvariances to the difference between WKNNOR and WKNNOR . BP is the
1 2
are implemented using notest [36] and car [37] R packages, most sensitive metric to the difference between two WKNNOR
respectively. classifiers. Weights have no impact on the α metric and little
8

A.E.YilmazandH.Demirhan AppliedSoftComputing134(2023)110020
Fig.2. MeanofmetricsfortheSVMOPclassifiers.Themeaniscalculatedover40datasetsandfolds.Barsshowthelimitsofmean±standarderror.
Fig.3. MeanofmetricsfortheWKNNORclassifiers.Themeaniscalculatedover40datasetsandfolds.Barsshowthelimitsofmean±standarderror.
impact on κ and BP metrics. Overall, while most mainstream classifiers, all agreement measures show some degree of differ-
metricsareinsensitivetotheslightdifferencebetweenWKNNOR encebetweentheperformancesofWKNNOR andWKNNOR .BP
1 2
9

| A.E.YilmazandH.Demirhan |     |     |     |     |     |     |     |     |     |     |     | AppliedSoftComputing134(2023)110020 |     |     |     |
| ----------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----------------------------------- | --- | --- | --- |
MeanofmetricsfortheKDLORclassifiers.Themeaniscalculatedover40datasetsandfolds.Barsshowthelimitsofmean±standarderror.
Fig.4.
showsthebestsensitivitywhenthemetricvaluesareveryclose classification method and the application field for each ordinal
toeachother(verysmallstandarderrors). classification method. However, Figs. 5 and 6 demonstrate that
For KDLOR classifiers (Fig. 4), we observe higher standard we need to consider each data composition for each ordinal
errorsamongthevaluesofmetricsthatincreasethesensitivityof classificationmethod.
| themetricstotheslightdifferencebetweenKDLOR |     |     |     |     |     | andKDLOR |     |     |     |     |     |     |     |     |     |
| ------------------------------------------- | --- | --- | --- | --- | --- | -------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|                                             |     |     |     |     |     | 1        | 2   |     |     |     |     |     |     |     |     |
classifiers.Allthemetricsaresensitivetothedifferencebetween
|                  |     |          |        |          |     |             |     | 5.2.2. | Statisticaltests |         |          |              |              |     |          |
| ---------------- | --- | -------- | ------ | -------- | --- | ----------- | --- | ------ | ---------------- | ------- | -------- | ------------ | ------------ | --- | -------- |
| the classifiers. | The | α metric | is not | impacted | by  | the weights | for |        |                  |         |          |              |              |     |          |
|                  |     |          |        |          |     |             |     | In     | order            | to give | detailed | significance | test results | for | the dif- |
KDLORclassifierstoo.Theπ
metricsshowthehighestsensitivity, ference between two sub-classifiers, we first apply ANOVA with
and the weights do not influence the degree of their sensitivity. metricsandsub-classifiers,ensurethenormalityandhomogene-
AlthoughMCChasthehighestsensitivityamongthemainstream
|     |     |     |     |     |     |     |     | ity of | variances | assumptions |     | of ANOVA, | and then | apply | Tukey’s |
| --- | --- | --- | --- | --- | --- | --- | --- | ------ | --------- | ----------- | --- | --------- | -------- | ----- | ------- |
metrics,itisconsiderablylowerthanthedifferenceindicatedby
theπ metric.Overall,MCC,κ,andπ pairwise comparison tests to identify the metrics for which the
metricsshowsimilarlevels
π sub-classifiers are giving different results. The results of these
| of performance, | while | distinguishes |     | KDLOR |     | and KDLOR | as  |     |     |     |     |     |     |     |     |
| --------------- | ----- | ------------- | --- | ----- | --- | --------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
1 2 tests are given in Table B.3 of Appendix B. Suppose we refer to
desired.
Tukey’spairwisecomparisontestresultforthemetricMCC.The
| When | the standard | errors | of metric | values |     | are high, | the π |      |           |         |       |                  |            |     |         |
| ---- | ------------ | ------ | --------- | ------ | --- | --------- | ----- | ---- | --------- | ------- | ----- | ---------------- | ---------- | --- | ------- |
|      |              |        |           |        |     |           |       | test | indicates | whether | there | is a significant | difference |     | between |
metricisabletodistinguishclassifierswithsimilarperformance
|                                                   |     |     |     |     |     |     |     | MCC | values | computed | for Classifier |     | and Classifier | . If | there is |
| ------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | ------ | -------- | -------------- | --- | -------------- | ---- | -------- |
| asseenforSVMOPandKDLORmethods.However,whenthemet- |     |     |     |     |     |     |     |     |        |          |                |     | 1              | 2    |          |
ric values are less variable, BP indicates the difference between a significant difference, we can conclude that MCC is able to
WKNNORclassifiersbetterthanπ.Regardingthelevelofdiffer- distinguish the performance difference between Classifier 1 and
|               |        |          |     |           |        |      |     | Classifier | as  | desired. | In this | way, we | gather statistical |     | evidence |
| ------------- | ------ | -------- | --- | --------- | ------ | ---- | --- | ---------- | --- | -------- | ------- | ------- | ------------------ | --- | -------- |
| ence captured | by the | metrics, | the | weighting | scheme | does | not |            | 2   |          |         |         |                    |     |          |
π to identify the metrics that perform as desired in distinguishing
| have a notable | influence | on  | both | and BP | metrics. | However, | it  |     |     |     |     |     |     |     |     |
| -------------- | --------- | --- | ---- | ------ | -------- | -------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
twoclassifierswithsimilarperformance.Ifapairwisecomparison
impactstheclassificationperformanceindicatedbythesemetrics.
|               |          |             |               |           |         |             |          | of two | metrics      | is  | insignificant, | we  | conclude that | both   | metrics  |
| ------------- | -------- | ----------- | ------------- | --------- | ------- | ----------- | -------- | ------ | ------------ | --- | -------------- | --- | ------------- | ------ | -------- |
| Since the     | data     | composition | and           | the field | of      | application | are      |        |              |     |                |     |               |        |          |
|               |          |             |               |           |         |             |          | are    | unsuccessful | in  | distinguishing |     | classifiers;  | hence, | they are |
| two important | features | of          | the datasets, |           | we need | to          | consider |        |              |     |                |     |               |        |          |
these factors for the inferences. Figs. 5 and 6 show the mean insensitivetothedifferencebetweenthem.
metric values and their standard error limits aggregated over For SVMOP classifiers, the p-values of Tukey’s pairwise com-
all the classifiers and the ordinal classification methods. From parisontestsaregiveninFig.7inthebreakdownofdatacompo-
these plots, we observe that both the data composition and the sitions.Forbalanceddatasets,pairwisecomparisonsofallmain-
application field considerably impact the mean metric values stream metrics except MCC and IA are insignificant, implying
|     |     |     |     |     |     |     |     | that | they are | insensitive | to  | the difference | between | SVMOP | and |
| --- | --- | --- | --- | --- | --- | --- | --- | ---- | -------- | ----------- | --- | -------------- | ------- | ----- | --- |
generated for the classifiers since the metrics react differently 1
|                                                        |     |     |     |     |     |     |     | SVMOP | classifiers. |     | All weighted | κ   | and π metrics | and | some |
| ------------------------------------------------------ | --- | --- | --- | --- | --- | --- | --- | ----- | ------------ | --- | ------------ | --- | ------------- | --- | ---- |
| toeachofbalanced,imbalanced,andextremelyimbalanceddata |     |     |     |     |     |     |     |       | 2            |     |              |     |               |     |      |
compositions and datasets from different fields. Note that since weighted AC2 metrics are significantly different from the main-
α
the aggregation is done over very different ordinal classification stream metrics, while BP and some metrics are not. All the
π
methods for Figs. 5 and 6, it is not appropriate to interpret weighted metrics are significantly different from the other
the differences between the data compositions and application mainstream and agreement metrics. When the composition of
fieldswithoutlookingintothedatacompositionforeachordinal data becomes imbalanced, mean F1, MCC, and IA metrics give
10

A.E.YilmazandH.Demirhan AppliedSoftComputing134(2023)110020
Fig.5. Meanofmetricsaccordingtothedatacomposition.Themeaniscalculatedoverallclassifiersandfolds.Barsshowthelimitsofmean±standarderror.
Fig. 6. Mean of metrics according to the application fields of the datasets. The mean is calculated over all classifiers and folds. Bars show the limits of mean ±
standarderror.
significantlydifferentvaluesbetweenSVMOP andSVMOP clas- inferences given for imbalanced data composition, we see mean
1 2
sifiers among the mainstream metrics. κ and α metrics are not F1 becomes significantly different from other mainstream and
significantlydifferentfromMCC,whileallotheragreementmet- agreementmetrics.
ricsaresignificantlydifferentfromMCCandallothermainstream Thep-valuesofTukey’spairwisecomparisontestsformetrics
metrics. For extremely imbalanced datasets, in addition to the are given in Fig. 8 in the breakdown of the field of application
11

| A.E.YilmazandH.Demirhan |     |     |     |     |     |     |     |     | AppliedSoftComputing134(2023)110020 |     |     |
| ----------------------- | --- | --- | --- | --- | --- | --- | --- | --- | ----------------------------------- | --- | --- |
Fig. 7. The p-values of Tukey’s pairwise comparison tests for SVMOP classifiers in the breakdown of data composition. The axes of the plots show the metrics
| calculatedforSVMOP1 |     | andSVMOP2 | classifiers. |     |     |     |     |     |     |     |     |
| ------------------- | --- | --------- | ------------ | --- | --- | --- | --- | --- | --- | --- | --- |
for SVMOP classifiers. We get different patterns of the pairwise accuracyisalsosensitivetothedifferencebetweenSVMOP and
1
| comparisons’ | p-values | across | the application |     | fields; | hence, the |     |     |     |     |     |
| ------------ | -------- | ------ | --------------- | --- | ------- | ---------- | --- | --- | --- | --- | --- |
SVMOP 2 classifiers.Forengineeringdatasets,themetricaccuracy
application field makes a difference in the usefulness of the significantlydiffersfromallothermainstreammetrics,κ,π,and
α
metrics.Amongthemainstreammetrics,onlyMCCissignificantly metrics. There is no significant difference between accuracy
differentacrosstwoSVMOPclassifiersforsocialsciencesdatasets. and weighted AC2 and BP metrics. Consistently, weighted ver-
|     | κ, π, | α   |     |     |     |     |     |     |     |     |     |
| --- | ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Since all and metrics are significantly different from the sions of AC2 and BP metrics are significantly different from the
| mainstream | metrics, | their | behavior | against | two similar | SVMOP |     |     |     |     |     |
| ---------- | -------- | ----- | -------- | ------- | ----------- | ----- | --- | --- | --- | --- | --- |
mainstreammetricsexceptforaccuracy.
| classifiers  | differs. | Also, there | are significant |          | differences | between |                                                       |     |     |     |     |
| ------------ | -------- | ----------- | --------------- | -------- | ----------- | ------- | ----------------------------------------------------- | --- | --- | --- | --- |
|              | κ        | π           |                 |          | α           |         | ForWKNNORclassifiers,thep-valuesofTukey’spairwisecom- |     |     |     |     |
| all weighted | and      | metrics.    | All             | weighted | metrics     | are not |                                                       |     |     |     |     |
significantlydifferentfromκ parisontestsaregiveninFigureB.1ofAppendixBinthebreak-
butshowthedifferencefortherest
|     |     |     |     |     |     |     | down of data | compositions | and Figure | B.3 of Appendix | B in |
| --- | --- | --- | --- | --- | --- | --- | ------------ | ------------ | ---------- | --------------- | ---- |
oftheagreementmeasures.SomeweightedAC2andBPmetrics
|           |           |         |            |      |         |             | the breakdown | of application | fields. We | get similar results | for |
| --------- | --------- | ------- | ---------- | ---- | ------- | ----------- | ------------- | -------------- | ---------- | ------------------- | --- |
| also show | a similar | result. | We observe | very | similar | results for |               |                |            |                     |     |
life sciences datasets. In addition to MCC, the only difference is balanced and imbalanced datasets. For both data compositions,
that mean F1 and IA metrics also show significant differences all the agreement metrics are significantly different from each
among the mainstream metrics. The results of datasets catego- other and mainstream metrics. Among the mainstream metrics,
rized in other application fields are similar to life sciences, but mean F1, MCC, and IA are sensitive to the differences between
12

| A.E.YilmazandH.Demirhan |     |     |     |     | AppliedSoftComputing134(2023)110020 |     |     |
| ----------------------- | --- | --- | --- | --- | ----------------------------------- | --- | --- |
Fig.8. Thep-valuesofTukey’spairwisecomparisontestsforSVMOPclassifiersinthebreakdownofthefieldofapplication.Theaxesoftheplotsshowthemetrics
| calculatedforSVMOP1 andSVMOP2 | classifiers. |     |     |     |     |     |     |
| ----------------------------- | ------------ | --- | --- | --- | --- | --- | --- |
WKNNOR andWKNNOR classifiers.Onlyaccuracyshowsasig- aresensitivetothedifferencebetweenWKNNOR andWKNNOR
| 1                                                       | 2   |     |              |     |     | 1   | 2   |
| ------------------------------------------------------- | --- | --- | ------------ | --- | --- | --- | --- |
| nificantdifferenceamongthemainstreammetricsforextremely |     |     | classifiers. |     |     |     |     |
imbalanceddatasets.Someofκ,mostofπ,andallAC2,BP,and For KDLOR classifiers, the p-values of Tukey’s tests are given
α metricsaresensitivetothedifferencebetweentwoWKNNOR inFigureB.2andB.4ofAppendixBintermsofdatacompositions
classifiers.Scott’sπ metricsarenotsignificantlydifferentfromκ andapplicationfields,respectively.Forbalanceddatasets,MCCis
and α metrics. We observe different patterns of p-values across theonlysensitivemetrictothedifferencebetweenKDLOR and
1
the fields of application in Figure B.3 of Appendix B. For social KDLOR classifiers.Whileκ,π,andαmetricsarenotsignificantly
2
science datasets, κ metrics are not significantly different from different from MCC, AC2 and BP metrics are different. π and
|     |     | π   | α   |     |     |     | κ   |
| --- | --- | --- | --- | --- | --- | --- | --- |
the mainstream metrics except for accuracy. Scott’s and Krip- show significant differences from all other metrics except
pendorff’sαmetricsshowsensitivitytothediscrepancybetween
|     |     |     | for balanced | datasets. | For imbalanced datasets, | mean F1, | MCC, |
| --- | --- | --- | ------------ | --------- | ------------------------ | -------- | ---- |
the classifiers compared to mainstream metrics. AC2 and BP IA,andallagreementmetricsdiffersignificantlyfromthemain-
α
metricsaresignificantlydifferentfromthemainstreamandother stream metrics. The metric shows different behavior than the
agreementmetrics.Whenitcomestoengineeringdatasets,only other agreement metrics. When the data composition becomes
|     |     |     |     |     | κ, π, α |     |     |
| --- | --- | --- | --- | --- | ------- | --- | --- |
accuracy, AC2, and BP metrics are significantly sensitive to the extremely imbalanced, MCC, and metrics are sensitive
α
difference between WKNNOR and WKNNOR classifiers, and to the difference between KDLOR classifiers, and the difference
|     | 1 2 | π   |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- |
shows significant differences from these metrics. Scott’s and betweenthisgroupofmetricsandAC2andBPissignificant.For
κ
Cohen’s metrics are insensitive for engineering datasets. For the application fields, we observe different patterns of p-values
life sciences and other datasets, we see similar patterns of p- for social sciences, engineering, and life sciences datasets, while
values. All the metrics except macro recall and macro precision datasets from other application areas produce a similar pattern
13

A.E.YilmazandH.Demirhan AppliedSoftComputing134(2023)110020
as the life sciences datasets. MCC, π, and α metrics produce SVMOPandWKNNORclassifiersforengineeringdatasets.Forall
significantly different results for KDLOR and KDLOR classifiers theothercategoriesofdatasets,κ,π,andαmetricsaresensitive
1 2
forsocialsciencesdatasets.AC2andBPmetricsaresignificantly tothedifferencebetweenclassifiers.Fromthesetofmainstream
different from the rest of the agreement and mainstream met- metrics,onlyMCCisconsistentlysensitiveacrossdifferentfields
rics.Forengineeringdatasets,interestingly,onlyunweightedand ofapplication.
radical weighted versions of the π metrics show a significant Themainstreammetricsaregenerallyinsensitivetothediffer-
difference for the KDLOR classifiers in addition to AC2 and BP ence between the classifiers, except for MCC. The mean F1 and
metrics.Noneofthemainstreamandκ metricsissensitivetothe MCC show sensitivity against the slight difference between the
differencebetweenKDLOR andKDLOR .Mostmetricsaresensi- classifiersforsomeordinalclassifiersandapplicationfields.
1 2
tivetothedifferencebetweenKDLORclassifiersforlifesciences The number of features has no impact on the ability of both
andotherdatasets.Onlyaccuracy,macrorecallandmacroF1are mainstream and weighted agreement metrics to distinguish the
insensitive. multi-classclassificationperformanceofclassifiers.Thesensitiv-
ity of the metrics is highly related to the characteristics of the
5.2.3. Impactofthenumberoffeatures datasetsasinvestigatedinSections5.2.1and5.2.2.
To further investigate the sensitivity of the metrics against
different numbers of features, we worked with datasets ssci15, 6. Discussion
ssci14,other3,eng2,ssci13,ssci11,lsci4,lsci5,lsci11fromTable
B.2 of Appendix B. The numbers of features of ssci15 and ssci11 Assessing the performance of classifiers in supervised ma-
arereducedto2and7,respectively,tohavef =2,3,...,10fea- chine/deeplearningiscrucialtochoosingtheclassifiertoemploy.
turesintheconsidereddatasets.TheprocedureoutlinedinFig.1 This problem gets challenging when the classification task is a
isimplementedwithSVMOP,WKNNOR,andKDLORclassifiersfor multi-class classification with ordinal classes. In this work, we
eachdataset.Thetwo-samplet-testisusedtoassessifthereisa focusedonthemetricsusedtoassesstheperformanceofordinal
significant difference between Classifier and Classifier . The p- multi-class classifiers based on the qualitative understanding of
1 2
valuesofthetestsaregiveninTableB.4,B.5andB.6ofAppendix error.Cohen’sκ-measurehasbeenusedinapplicationsasoneof
BforSVMOP,WKNNOR,andKDLORclassifiers,respectively. the promising metrics for classifiers without distinguishing the
In Table B.4, B.5 and B.6 of Appendix B, cells with bold font type of multi-class categorical responses as ordinal or nominal.
show the metrics that produce a significant difference between Manyotheragreementmeasuresandtheirweightedversionsfor
the two classifiers; hence, they are sensitive to the slight dif- ordinal data are proposed in the literature. Furthermore, from
ferencebetweentheclassificationperformanceofclassifiers.For the previous works, it is known that there are better perform-
all classification methods of SVMOP, WKNNOR, and KDLOR, the ing measures than Cohen’s κ in the area of agreement studies.
sensitivity of all the metrics is not impacted by the increasing Consideringthese,weconductedtwoextensivenumericalstudies
number of features. For SVMOP, the mainstream metrics are with 37 metrics composed of the mainstream and agreement
insensitive for all the considered number of features. Weighted metricstoinvestigatethereliability/usefulnessoftheagreement
κ and π metrics detect the difference just for the dataset with measuresasevaluationmetricsforordinalmulti-classclassifiers.
seven features. Metrics are more sensitive to the difference be- WeidentifiedScott’sweightedπ-measureasastrongalternative
tween WKNNOR classifiers. While the mainstream metrics are toCohen’sweightedκ.
sensitive to the difference between WKNNOR classifiers with 6 In the first numerical study, the ability of metrics to capture
features, weighted agreement metrics are sensitive for multiple the classification performance as close as the true accuracy is
numbersoffeatures.Thebestsensitivityresultsareseenforthe analyzed through randomly generated synthetic confusion ma-
weightedBPmetric,whichdetectsthedifferencefor2,5,6,and trices under different data compositions and different levels of
7 features. For KDLOR classifiers, the weighted κ and π metrics accuracy in the classification performance. Ordinal multi-class
showsensitivity,withthedatasetshaving5and7features. classification processes are not perfect. Thus, they are prone to
the composition of ordinal response and sample size. We show
5.3. Conclusions thatthecompositionofdataconsiderablyinfluencestheaccuracy
ofmetrics.Themainstreammetrics,exceptMCC,areobservedto
Underdifferentdatacompositions,Scott’sπ metricsarecon- be insensitive to capture different types of misclassification. In
sistently sensitive to the difference between classifiers for all contrast, the metrics based on agreement measures react better
ordinalclassificationmethods,whilemainstreammetrics,except tomisclassificationinindividualclassesofthedependentfeature.
MCC and IA are not, in general. Other agreement metrics are Sincethemainstreammetricshavethemaindiagonalofthecon-
as consistent as Scott’s π in distinguishing classifiers under dif- fusionmatrixandoneofitsmarginsintheirformulations,theydo
ferent data compositions. Specifically, metrics have difficulty in not capture the misclassification that occurs in the off-diagonal
separating the performance of classifiers for extremely imbal- cells.OnlyMCCtakesbothmarginsintoaccountandshowsbetter
anced datasets where Scott’s π metric works best. Among the sensitivitythantheothermainstreammetrics.Ontheotherhand,
agreement metrics, while κ, π, and α generally have similar (weighted)agreementmetricsconsiderdiagonalandoff-diagonal
behavior, AC2 and BP have similar responses to the slight dif- cellsandmargins(rowandcolumntotals)oftheconfusiontable
ference between the classifiers. All the metrics perform better to capture the correct classifications as well as the magnitude
in distinguishing the classifiers for the SVMOP method and the of divergence from the correct classifications. The level of true
worstperformancefortheKDLORclassifiers. accuracyisanotherimportantfactorontheperformanceofmet-
Engineeringdatasetsproducenotablydifferentpairwisecom- rics.Whenthetrueaccuracyislow,themetrics’marginoferror
parison results for all ordinal classification methods than the toevaluatetheclassificationperformanceincreases,mainstream
other fields of application. The results for the datasets catego- metrics become highly insensitive to misclassification, and the
rized as other fields of application or life sciences are generally rangeofagreementmeasuresincreases.Therefore,thereliability
similar. Among the agreement metrics, π and κ metrics do not ofallmetricsishigherwhentheyindicatehighperformance.The
work as desired for engineering datasets, while AC2 and BP are casewithalowtrueaccuracyischallengingbecauseitpushesthe
mostly sensitive to the differences between the classifiers. For cellcountstooff-diagonalcellsoftheconfusiontable.Themetrics
themainstreammetrics,onlytheaccuracymetricissensitivefor that do not incorporate off-diagonal cells of the confusion table
14

| A.E.YilmazandH.Demirhan |     |     |     |     |     |     |     |     |     | AppliedSoftComputing134(2023)110020 |     |     |     |     |
| ----------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----------------------------------- | --- | --- | --- | --- |
Scott’sunweightedπ
in their formulation got more negatively impacted in detecting producesclosevaluestoMCCundersome
a low level of accuracy. Cohen’s κ and Scott’s π with quadratic scenarios. Besides, Gwet’s unweighted AC2, Brennan–Prediger’s
weightsperformbetterthanalltheconsideredmainstreammet- unweightedBP,andKrippendorff’sα metricsproduceveryclose
rics and agreement measures under the most challenging data valuestoIAwhenthetrueagreementishighand,insomecasesof
compositions. lowandmoderateagreement.Atheoreticalinvestigationofthese
The second numerical study uses 40 real datasets, including resultsisafuturedirection.
AnotherfuturedirectionisusingScott’squadraticweightedπ
| balanced, | imbalanced, | and | extremely | imbalanced |     | data composi- |     |     |     |     |     |     |     |     |
| --------- | ----------- | --- | --------- | ---------- | --- | ------------- | --- | --- | --- | --- | --- | --- | --- | --- |
tions from social sciences, life sciences, engineering, and other asalossfunctionforordinalimageclassificationandregression.
κ
areas, to create replications via cross-validation. In this study, Cohen’s weighted showed improved generalization ability for
we examined the sensitivity of metrics to small differences be- imageclassification[4]whenusedasalossfunction.Inthissense,
tweentwosimilarclassifiersfromthesameordinalclassification theuseofScott’squadraticweightedπ asalossfunctionwould
method. A useful metric is expected to be sensitive enough to providefurtherimprovement.
| distinguish | such | classifiers. | We  | observed | that MCC | successfully |     |     |     |     |     |     |     |     |
| ----------- | ---- | ------------ | --- | -------- | -------- | ------------ | --- | --- | --- | --- | --- | --- | --- | --- |
discriminatestwoclassifierswithsimilarperformance.However,
CRediTauthorshipcontributionstatement
itgenerateshighmarginsoferrorwhenthedatacompositionis
imbalancedorextremelyimbalanced.Scott’squadraticweighted
|     |     |     |     |     |     |     | Ayfer | Ezgi | Yilmaz: | Conceptualization, |     | Methodology, |     | Soft- |
| --- | --- | --- | --- | --- | --- | --- | ----- | ---- | ------- | ------------------ | --- | ------------ | --- | ----- |
| π   |     |     |     | κ   |     |     |       |      |         |                    |     |              |     |       |
and Cohen’s quadratic weighted metrics show promising ware, Data curation, Writing – original draft, Review. Haydar
sensitivityforchallengingcases,includingextremelyimbalanced Demirhan: Conceptualization, Methodology, Software, Data
| datacompositions. |     |     |     |     |     |     | curation,Writing–originaldraft,Review. |     |     |     |     |     |     |     |
| ----------------- | --- | --- | --- | --- | --- | --- | -------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
Thequadraticweightspenalizemisclassificationquadratically;
hence,theagreementmetricswithquadraticweightsarehighly Declarationofcompetinginterest
sensitivetomisclassification.Scott’sπ
doesnothaveauniformity
assumptionontherowandcolumntotalsoftheconfusiontable.
|     |     |     |     |     |     |     | The authors |     | declare | that they | have | no known | competing |     |
| --- | --- | --- | --- | --- | --- | --- | ----------- | --- | ------- | --------- | ---- | -------- | --------- | --- |
Instead,itassumesthehomogeneityofmargins.Ifthemarginsof
|             |       |                  |     |                  |     |            | financial | interests | or  | personal | relationships | that | could | have |
| ----------- | ----- | ---------------- | --- | ---------------- | --- | ---------- | --------- | --------- | --- | -------- | ------------- | ---- | ----- | ---- |
| a confusion | table | are considerably |     | non-homogeneous, |     | it implies |           |           |     |          |               |      |       |      |
appearedtoinfluencetheworkreportedinthispaper.
thattheclassifierassignsobjectstothewronglabelsatanotably
| high rate. | This translates |     | into very | poor | performance, | and the |     |     |     |     |     |     |     |     |
| ---------- | --------------- | --- | --------- | ---- | ------------ | ------- | --- | --- | --- | --- | --- | --- | --- | --- |
Dataavailability
metricscancapturethiscasestraightforwardly.Thus,ingeneral,
π
| Scott’s          | is not       | impacted    | by the      | composition    | of                | data. Cohen’s |                                   |     |       |         |             |           |     |       |
| ---------------- | ------------ | ----------- | ----------- | -------------- | ----------------- | ------------- | --------------------------------- | --- | ----- | ------- | ----------- | --------- | --- | ----- |
| κ                |              |             |             |                |                   |               | Datawillbemadeavailableonrequest. |     |       |         |             |           |     |       |
| does not         | have         | restrictive | assumptions | on             | the margins       | of the        |                                   |     |       |         |             |           |     |       |
| confusion        | table        | as well.    | Therefore,  | Scott’s        | quadratic         | weighted      |                                   |     |       |         |             |           |     |       |
| π                | κ            |             |             |                |                   |               | Acknowledgments                   |     |       |         |             |           |     |       |
| and Cohen’s      |              | generally   | show        | satisfactory   | preciseness.      | How-          |                                   |     |       |         |             |           |     |       |
| ever, the        | assumptions, | such        | as          | the uniformity | of                | the margins   |                                   |     |       |         |             |           |     |       |
|                  |              |             |             |                |                   |               | The authors                       |     | would | like to | thank three | reviewers | for | their |
| of the confusion |              | table BP    | or AC2,     | limits         | their preciseness | for           |                                   |     |       |         |             |           |     |       |
commentsthatconsiderablyimprovedtheclarityofthearticle.
imbalanceddatacompositions.Duetothetheoreticalrelationship
| between Cohen’s |     | κ and | MCC for | symmetric | confusion | matri- |     |     |     |     |     |     |     |     |
| --------------- | --- | ----- | ------- | --------- | --------- | ------ | --- | --- | --- | --- | --- | --- | --- | --- |
ces, MCC also show satisfactory preciseness when the confusion AppendixA. Supplementarydata
matrixisnear-symmetric.
|          |     |            |      |           |          | π           | Supplementary |     | material | related | to this | article | can be | found |
| -------- | --- | ---------- | ---- | --------- | -------- | ----------- | ------------- | --- | -------- | ------- | ------- | ------- | ------ | ----- |
| Based on | the | results of | both | numerical | studies, | Scott’s and |               |     |          |         |         |         |        |       |
κ online at https://doi.org/10.1016/j.asoc.2023.110020. Tables A.1
| Cohen’s | metrics | with quadratic |     | weights | are both | sensitive to |          |        |         |          |         |            |           |     |
| ------- | ------- | -------------- | --- | ------- | -------- | ------------ | -------- | ------ | ------- | -------- | ------- | ---------- | --------- | --- |
|         |         |                |     |         |          |              | to A.14, | Tables | B.15 to | B.17 and | Figures | B.1 to B.3 | are given | in  |
thesmalldifferencesbetweenclassifiersandproduceclosevalues
theSupplementaryMaterial.
| to the true           | level | of accuracy     | in  | most of the  | considered | scenar-         |            |     |     |     |     |     |     |     |
| --------------------- | ----- | --------------- | --- | ------------ | ---------- | --------------- | ---------- | --- | --- | --- | --- | --- | --- | --- |
| ios. Therefore,       | they  | are recommended |     | to be        | used       | in practice, in |            |     |     |     |     |     |     |     |
| general. Specifically |       | for engineering |     | applications |            | and low true    | References |     |     |     |     |     |     |     |
performance,theuseofquadraticweightedAC2metricisrecom-
mended.Werecommendavoidingaccuracy,recall,precision,and [1] C. Deng, X. Liu, C. Li, D. Tao, Active multi-kernel domain adaptation for
hyperspectralimageclassification,PatternRecognit.77(2018)306–315.
macroF1forextremelyimbalanceddatasets.MeanF1hasabetter
|     |     |     |     |     |     |     | [2] L. Kook, | L. Herzog, | T.  | Hothorn, | O. Dürr, B. | Sick, Deep | and interpretable |     |
| --- | --- | --- | --- | --- | --- | --- | ------------ | ---------- | --- | -------- | ----------- | ---------- | ----------------- | --- |
performancethanmacroF1butisnotasgoodasScott’sweighted
|     |     |     |     |     |     |     | regression | models | for | ordinal outcomes, |     | Pattern Recognit. | 122 | (2022) |
| --- | --- | --- | --- | --- | --- | --- | ---------- | ------ | --- | ----------------- | --- | ----------------- | --- | ------ |
π.Insomecases,therecentlyproposedmetric,IA,isusefulinthe
108263.
performanceassessmentofordinalclassifiers.However,itisnot [3] L. Li, L. Ma, L. Jiao, F. Liu, Q. Sun, J. Zhao, Complex contourlet-CNN for
polarimetricSARimageclassification,PatternRecognit.100(2020)107110.
recommendedforgeneraluse.
|     |     |     |     |     |     |     | [4] J. de | La Torre, | D. Puig, | A. Valls, | Weighted | kappa loss function | for | multi- |
| --- | --- | --- | --- | --- | --- | --- | --------- | --------- | -------- | --------- | -------- | ------------------- | --- | ------ |
Thisstudyfocusesonaperformanceanalysisoftheevaluation
classclassificationofordinaldataindeeplearning,PatternRecognit.Lett.
| metrics readily | computed |     | using | a given confusion |     | matrix. The |     |     |     |     |     |     |     |     |
| --------------- | -------- | --- | ----- | ----------------- | --- | ----------- | --- | --- | --- | --- | --- | --- | --- | --- |
105(2018)144–154.
computation of all the evaluation metrics requires straightfor- [5] C. Ferri, J. Hernández-Orallo, R. Modroiu, An experimental comparison
ward analytical calculations without any iterative method, done of performance measures for classification, Pattern Recognit. Lett. 30 (1)
inmillisecondswithoutconsuminganoticeablecomputermem- (2009)27–38.
ory.Therefore,thespaceandtimecomplexityofcalculatingeval- [6] A.Rácz,D.Bajusz,K.Héberger,Multi-levelcomparisonofmachinelearning
uationmetricsisoutsidethefocusofourstudy.Themainlimita- classifiersandtheirperformancemetrics,Molecules24(15)(2019)2811.
[7] Y.Sasaki,R.Fellow,TheTruthoftheF-Measure,UniversityofManchester:
tionsofourstudyincludethesimulationspaceofsyntheticdata
MIB-SchoolofComputerScience,2007.
study and the number of datasets and replications of the real- [8] P.Czodrowski,Countonkappa,J.Comput.AidedMol.Des.28(11)(2014)
| data study. | Although | we cover | many | scenarios | of  | true accuracy, | 1049–1055. |     |     |     |     |     |     |     |
| ----------- | -------- | -------- | ---- | --------- | --- | -------------- | ---------- | --- | --- | --- | --- | --- | --- | --- |
data composition, misclassification, and application areas, there [9] S. Boughorbel, F. Jarray, M. El-Anbari, Optimal classifier for imbalanced
datausingMatthewsCorrelationCoefficientmetric,PLoSOne12(6)(2017)
canstillbeotherapplication-specificcharacteristicstoinfluence
e0177678.
theperformanceofmetrics.
|             |     |                 |     |            |                |        | [10] D. Chicco, | M.J. | Warrens, | G. Jurman, | The Matthews | correlation | coefficient |     |
| ----------- | --- | --------------- | --- | ---------- | -------------- | ------ | --------------- | ---- | -------- | ---------- | ------------ | ----------- | ----------- | --- |
| In addition | to  | the theoretical |     | results on | the similarity | of un- |                 |      |          |            |              |             |             |     |
(MCC)ismoreinformativethanCohen’sKappaandBrierscoreinbinary
weighted Cohen’s κ and MCC, we numerically observed that classificationassessment,IEEEAccess(2021).
15

| A.E.YilmazandH.Demirhan |     |     |     |     |     |     |     |     | AppliedSoftComputing134(2023)110020 |     |
| ----------------------- | --- | --- | --- | --- | --- | --- | --- | --- | ----------------------------------- | --- |
[11] D.Chicco,G.Jurman,TheadvantagesoftheMatthewscorrelationcoeffi- [24] N.W.S.Wardhani,M.Y.Rochayani,A.Iriany,A.D.Sulistyono,P.Lestantyo,
cient(MCC)overF1scoreandaccuracyinbinaryclassificationevaluation, Cross-validation metrics for evaluating classification performance on im-
BMCGenomics21(1)(2020)6. balanced data, in: 2019 International Conference on Computer, Control,
InformaticsandItsApplications(IC3INA),IEEE,2019,pp.14–18.
| [12] R. Delgado, | X.-A. | Tibau, | Why Cohen’s | Kappa | should | be avoided as |     |     |     |     |
| ---------------- | ----- | ------ | ----------- | ----- | ------ | ------------- | --- | --- | --- | --- |
performancemeasureinclassification,PLoSOne14(9)(2019)e0222916. [25] A. Casagrande, F. Fabris, R. Girometti, Beyond kappa: an informa-
[13] L. Gaudette, N. Japkowicz, Evaluation methods for ordinal classification, tional index for diagnostic agreement in dichotomous and multivalue
in:Y.Gao,N.Japkowicz(Eds.),AdvancesinArtificialIntelligence,Springer ordered-categorical ratings, Med. Biol. Eng. Comput. 58 (12) (2020)
3089–3099.
BerlinHeidelberg,Berlin,Heidelberg,2009,pp.207–210.
[14] S. Baccianella, A. Esuli, F. Sebastiani, Evaluation measures for ordinal [26] M.J.Warrens,AcomparisonofCohen’skappaandagreementcoefficients
regression,in:2009NinthInternationalConferenceonIntelligentSystems byCorradoGini,Int.J.Res.Rev.Appl.Sci.16(2013)345–351.
|     |     |     |     |     |     |     | [27] H. Demirhan, | rTableICC: | An R package for | random generation of 2x2xK |
| --- | --- | --- | --- | --- | --- | --- | ----------------- | ---------- | ---------------- | -------------------------- |
DesignandApplications,IEEE,2009,pp.283–287.
andRxCcontingencytables,RJ.8(1)(2016)48–63.
[15] J.S.Cardoso,R.Sousa,Measuringtheperformanceofordinalclassification,
Int.J.PatternRecognit.Artif.Intell.25(08)(2011)1173–1195. [28] R.Artstein,M.Poesio,Inter-coderagreementforcomputationallinguistics,
[16] A.E. Yilmaz, T. Saracbasi, Assessing agreement between raters from the Comput.Linguist.34(4)(2008)555–596.
[29] K.L.Gwet,Computinginter-raterreliabilityanditsvarianceinthepresence
pointofcoefficientsandlog-linearmodels,J.DataSci.15(1)(2017)1–24.
ofhighagreement,Br.J.Math.Stat.Psychol.61(1)(2008)29–48.
[17] D.Tran,A.Dolgun,H.Demirhan,Weightedinter-rateragreementmeasures
[30] W.Waegeman,L.Boullart,etal.,Anensembleofweightedsupportvector
for ordinal outcomes, Comm. Statist. Simulation Comput. 49 (4) (2020) machinesforordinalregression,Int.J.Comput.Syst.Sci.Eng.3(1)(2009)
989–1003.
47–51.
| [18] K.L. Gwet, | Handbook | of Inter-Rater | Reliability: |     | The Definitive | Guide To |     |     |     |     |
| --------------- | -------- | -------------- | ------------ | --- | -------------- | -------- | --- | --- | --- | --- |
[31] K.Hechenbichler,K.Schliep,WeightedK-Nearest-NeighborTechniquesand
| Measuring | the Extent | of Agreement | Among | Raters, | Advanced | Analytics, |     |     |     |     |
| --------- | ---------- | ------------ | ----- | ------- | -------- | ---------- | --- | --- | --- | --- |
OrdinalClassification,CollaborativeResearchCenter386,DiscussionPaper
| LLC,2014. |     |     |     |     |     |     | 399,2004,http://dx.doi.org/10.5282/ubm/epub.1769. |     |     |     |
| --------- | --- | --- | --- | --- | --- | --- | ------------------------------------------------- | --- | --- | --- |
[19] A.Sellami,S.Tabbone,Deepneuralnetworks-basedrelevantlatentrepre-
|     |     |     |     |     |     |     | [32] B.-Y. | Sun, J. Li, D.D. | Wu, X.-M. Zhang, W.-B. | Li, Kernel discriminant |
| --- | --- | --- | --- | --- | --- | --- | ---------- | ---------------- | ---------------------- | ----------------------- |
sentationlearningforhyperspectralimageclassification,PatternRecognit.
learningforordinalregression,IEEETrans.Knowl.DataEng.22(6)(2010)
| 121(2022)108224. |     |     |     |     |     |     | 906–910. |     |     |     |
| ---------------- | --- | --- | --- | --- | --- | --- | -------- | --- | --- | --- |
[20] A. Ben-David, Comparison of classification accuracy using Cohen’s [33] M.Kuhn,K.Johnson,etal.,AppliedPredictiveModeling,Vol.26,Springer,
WeightedKappa,ExpertSyst.Appl.34(2)(2008)825–832.
2013.
| [21] S. García, | A. Fernández, | J. Luengo, | F. Herrera, | A   | study of | statistical tech- |     |     |     |     |
| --------------- | ------------- | ---------- | ----------- | --- | -------- | ----------------- | --- | --- | --- | --- |
[34] M.C.Heredia-Gómez,S.García,P.A.Gutiérrez,F.Herrera,Ocapis:Rpackage
niques and performance measures for genetics-based machine learning: forordinalclassificationandpreprocessinginscala,Prog.Artif.Intell.8(3)
| accuracyandinterpretability,SoftComput.13(10)(2009)959. |     |     |     |     |     |     | (2019)287–292. |     |     |     |
| ------------------------------------------------------- | --- | --- | --- | --- | --- | --- | -------------- | --- | --- | --- |
[22] T.Saito,M.Rehmsmeier,Theprecision-recallplotismoreinformativethan
[35] J.Demšar,Statisticalcomparisonsofclassifiersovermultipledatasets,J.
the ROC plot when evaluating binary classifiers on imbalanced datasets, Mach.Learn.Res.7(2006)1–30.
PLoSOne10(3)(2015)e0118432. [36] J.Gross,U.Ligges,nortest:Testsfornormality,2015,URL: https://CRAN.R-
[23] A. Korotcov, V. Tkachenko, D.P. Russo, S. Ekins, Comparison of deep project.org/package=nortest,Rpackageversion1.0-4.
| learning | with multiple | machine | learning | methods | and | metrics using |     |     |     |     |
| -------- | ------------- | ------- | -------- | ------- | --- | ------------- | --- | --- | --- | --- |
[37] J.Fox,S.Weisberg,AnRCompanionToAppliedRegression,thirded.,Sage,
diversedrugdiscoverydatasets,Mol.Pharm.14(12)(2017)4462–4475. ThousandOaksCA,2019.
16