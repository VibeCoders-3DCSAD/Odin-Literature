---
conversion_metadata:
  converted_at: "2026-07-22T13:28:13Z"
  converter_tool: "markitdown"
  converter_version: "0.1.6"
  source_pdf: "Guido et al.pdf"
  source_pdf_sha256: "dad8c3b45acb2a76d1cc90ea36160db578f42bd49525a2da41ad9ad5cb022ade"
  page_count: 19
  markdown_char_count: 172261
---

<!-- PAGE-AWARE EXTRACTION (via pdfminer.six) -->

<!-- PAGE 1 -->

Soft Computing (2023) 27:12863–12881
https://doi.org/10.1007/s00500-022-06768-8

F O C U S

A hyper-parameter tuning approach for cost-sensitive support vector
machine classiﬁers

Rosita Guido1

· Maria Carmela Groccia1 · Domenico Conforti1

Accepted: 10 January 2022 / Published online: 2 February 2022
© The Author(s) 2022

Abstract
In machine learning, hyperparameter tuning is strongly useful to improve model performance. In our research, we concentrate
our attention on classifying imbalanced data by cost-sensitive support vector machines. We propose a multi-objective approach
that optimizes model’s hyper-parameters. The approach is devised for imbalanced data. Three SVM model’s performance
measures are optimized. We present the algorithm in a basic version based on genetic algorithms, and as an improved version
based on genetic algorithms combined with decision trees. We tested the basic and the improved approach on benchmark
datasets either as serial and parallel version. The improved version strongly reduces the computational time needed for ﬁnding
optimized hyper-parameters. The results empirically show that suitable evaluation measures should be used in assessing the
classiﬁcation performance of classiﬁcation models with imbalanced data.

Keywords Multi-objective optimization · Support vector machine · Hyper-parameter optimization · Imbalanced datasets ·
Genetic algorithms

1 Introduction

Classiﬁcation problems may be encountered in different
domains. One of these is the disease diagnosis, which estab-
lishes the presence or absence of a given disease according
to referred symptoms and results of medical exams. Machine
learning approaches can be employed to support experts in
diseases diagnosis. Many researches aim to propose new
methods to improve or enhance the outcomes of existing
ones.

Support vector machines (SVM) are one of the best
machine learning (ML) models for solving several real-life
classiﬁcation problems (Vapnik 1998; Cristianini and Shawe-
Taylor 2000). The choice of hyper-parameters of a ML model

Communicated by Dario Pacciarelli.
B Rosita Guido

rosita.guido@unical.it

Maria Carmela Groccia
mariacarmela.groccia@unical.it

Domenico Conforti
domenico.conforti@unical.it

1 Department of Mechanical, Energy and Management

Engineering, University of Calabria, Ponte Pietro Bucci,
87036 Rende, Cosenza, Italy

can signiﬁcantly affect the resulting model’s performance.
Generally, hyper-parameters are adjusted for each model in
order to ﬁnd a hyper-parameter setting that maximizes the
model performances and so that the ML model can predict
unknown data accurately. The goal of hyper-parameter opti-
mization is to ﬁnd a set of values that minimizes a predeﬁned
loss function.

Usually, a good set of hyper-parameters are determined
by a grid search. The grid search strategy is based on
testing all hyper-parameter combinations speciﬁed in a multi-
dimensional grid. During the search, the hyper-parameters
are varied, with ﬁxed step-size, in a given range of values. The
performance of a combination of hyperparameters is evalu-
ated using a performance metric. The conﬁguration with the
best performance is selected and used to train the ML model
on the whole dataset. However, this kind of search is very
time consuming and it is suitable for the adjustment of few
hyper-parameters.

Another big challenge in data mining that is attracting
increasing interest of researchers is dealing with imbal-
anced data sets (Japkowicz and Stephen 2002). A dataset is
imbalanced when one or more classes have very low propor-
tions in the data as compared to the other classes. The ﬁrst
class is called as minority class with respect to the major-
ity class(ess). The main interest is in correctly classifying

123

---

<!-- PAGE 2 -->

12864

R. Guido et al.

the minority class. The existing methods for classiﬁcation of
imbalanced data can be categorized as algorithm-level cate-
gory, data-level category, and cost-sensitive methods that lie
between the above two categories (Galar et al. 2012). The
ﬁrst category includes methods modiﬁed or designed to han-
dle imbalanced data; the second category includes methods
that try to transform data in order to balance classes and
use then standard classiﬁcation algorithms. Down-sampling
approaches, which reduce the majority class in the training
subset, and over-sampling approaches, which increase the
size of the minority class in the training subset, belong to
this category. Finally, the third category includes methods
designed for weighting differently the classes by introducing
misclassiﬁcation costs.

It is important to point out that the most commonly used
model evaluation metric is the accuracy. However, it can be
very misleading when data are imbalanced. In such cases, dif-
ferent evaluation metrics should be considered. We tested in
(Guido et al. 2021) two evaluation model metrics, i.e., accu-
racy and G-Mean, on two imbalanced benchmark datasets
by optimizing hyper-parameters of support vector machines
by genetic algorithms (GAs). Comparing the results, we
observed empirically that G-Mean is more suitable than accu-
racy to evaluate model performance in case of imbalanced
data, especially when data refers to medical domains, like
diagnosis. The results encouraged us to continue exploring
this research ﬁeld.

This

research paper addresses

the optimal hyper-
parameters problem as a multi-objective problem. It has a
twofold contribution:

1. The main goal is to investigate methods for improving
hyper-parameter tuning of SVM. We propose a novel
approach for optimal hyper-parameter tuning that con-
sists of a genetic algorithm combined with a decision
tree. The basic idea is that some chromosomes are similar
among them and they have thus the same ﬁtness value.
A decision tree (DT), trained in a suitable manner, is
exploited to reduce the number of k-fold cross-validation
to be performed and thus the overall computational time.
As we will see, GAs were chosen even because they
allow for an easy parallelization of the problem, which is
tremendously helpful. The approach that combines GAs
and DT strongly reduces the overall computational time,
as described in Sect. 5.

2. It focuses on testing and optimizing, at the same time,
more suitable performance measures in addition to the
accuracy. This is important for application domains
where one data class is of more interest than others.

The paper is structured as follows. A short review of the
state-of-the-art of the literature focusing on imbalanced data
sets is in Sect. 2. We give a short description of support vec-

123

tor machines and decision trees in Sect. 3, and discuss some
metrics commonly used to evaluate model performance. In
Sect. 4, we introduce multi-objective optimization prob-
lems and the Non-dominated Sorting Genetic Algorithm-II
(NSGA-II). In Sect. 5, we detail our approach that com-
bines genetic algorithms and a heuristic procedure based
on decision tree in order to ﬁnd optimal hyper-parameters.
Three objective functions are optimized. We perform several
computational experiments aimed at ﬁnding the best hyper-
parameter tuning for six benchmark datasets. The best results
along with a discussion and comparison with other results of
the literature are reported in Sect. 6. Finally, the conclusions
are given in Sect. 7.

2 Related work on imbalanced data

classiﬁcation and cost-sensitive learning
problems

Let D = {(x1, y1), (x2, y2), . . . , (xl , yl )}, be a dataset where
xi ∈ (cid:3)L is a pattern (even called example) drawn from a
domain X and yi ∈ Y is its related class label. An example is
thus a vector. In a binary classiﬁcation domain, an example
can be either positive, denoted by a label y = 1, or negative,
denoted by y = −1. Generally, the goal of a binary classiﬁer
is to map feature vectors x ∈ X to class labels y ∈ {±1}.
In terms of functions, a classiﬁer can be written as h(x) =
sign[ p(x)], where the function p : X → R is denoted as the
classiﬁer predictor.

Classiﬁers generally perform poorly on imbalanced
datasets and, as a consequence, often they classify almost
all instances as negative. In recent years, imbalanced data
classiﬁcation has been studied by many researchers with dif-
ferent methods (Jo and Japkowicz 2004; Galar et al. 2012).
These methods can be distinguished into two categories
based on data and algorithms. Data-based methods focus on
data pre-processing to reduce imbalanced data. For instance,
up-sampling and under-sampling are two methods that mod-
ify instance distribution. Up-sampling methods increase the
minority samples, whereas under-sampling methods reduce
the majority samples. Synthetic Minority Oversampling
Technique is an oversampling method that balances data by
generating new samples similar to the minority samples and
their neighbors (Chawla et al. 2002).

Hereafter, a positive instance belongs to the minority class,
whereas a negative instance to the majority class. In many
real-world applications, misclassiﬁcations may have differ-
ent costs, such as for instance disease diagnosis and business
decision making. The related classiﬁcation problem, called
cost-sensitive learning problem, aims at minimizing the total
misclassiﬁcation costs. The issue of classifying imbalanced
data by an SVM was addressed in (Veropoulos et al. 1999) by
a biased-SVM. This method uses two penalty coefﬁcients for

---

<!-- PAGE 3 -->

A hyper-parameter tuning approach...

12865

misclassiﬁed positive instances and negative instances. Since
the positive instances usually belong to the minority class,
the used penalty coefﬁcient for this class is bigger than the
penalty coefﬁcient associated with the majority class. In this
way, the SVM classiﬁer aims at reducing misclassiﬁcation
rate of the minority class.

The performance of an SVM model even depends, for
instance, on the used kernel function, which maps instances-
vectors from the original input space to higher dimensional
spaces to deal with nonlinearly separable data (Scholkopf and
Smola 2001). Accordingly, two parameters of SVM, i.e., C
and the kernel parameter were found by an exhaustive search
approach in (Mehrbakhsh et al. 2019). Iranmehr et al. (2019)
extended the SVM with cost-sensitive learning consider-
ing example dependent costs. They performed experimental
analysis on class imbalance, cost-sensitive learning with
a given class and example costs and showed that their
proposed algorithm provides superior generalization perfor-
mance compared to conventional methods. Qi et al. (2013)
proposed a new Cost-Sensitive Laplacian SVM and tested its
effectiveness via experiments on public datasets. They eval-
uate the algorithms performance by the Average Cost. Tao
et al. (2019) developed a novel self-adaptive cost weights-
based SVM cost-sensitive ensemble for imbalanced datasets
classiﬁcation tasks. The approach was tested on synthetic
datasets and on public datasets showing higher classiﬁcation
accuracy than the other existing imbalanced classiﬁcation
methods in terms of G-Mean and F-Measure.

Evolutionary algorithms are ﬂexible and commonly used
for a plethora of machine learning problems and tasks
(Bergstra et al. 2011; Goldberg and Holland 1988). Evolu-
tionary optimization-based techniques solve the ﬁlter design
task as an optimization problem. They are used success-
fully in different real-world optimization problems related
to Finite Impulse Response (FIR) and Inﬁnite Impulse
Response (IIR) digital ﬁlters design. The goal is to minimize
an error function that quantiﬁes deviation between a ﬁlter and
a desired response. This error is reduced by updating itera-
tively a set of ﬁlter coefﬁcients such that given speciﬁcations
are met. Dwivedi et al. (2018) provided a comprehensive
review of the various evolutionary optimization-based tech-
niques for FIR ﬁlter design. Approaches to design IIR ﬁlters
based on evolutionary techniques were proposed in (Agrawal
et al. 2018, 2017). Evolutionary algorithms are even used
to automatically tune several parameters. Lessmann et al.
(2005) used a GA in order to tune SVMs. Phienthrakul and
Kijsirikul (2010) improved the accuracy of SVM by a non-
linear combination of multiple RBF kernels to obtain more
ﬂexible kernel functions. The hyperparameters are chosen
by an evolutionary strategy where the objective functions are
based on training accuracy, bounding of generalization error,
and subset cross-validation on training accuracy. The result-

ing kernel allows better discrimination in the feature space
than that of a single RBF kernel.

One of the ﬁrst research papers on cost-sensitive approach
tackled with an evolutionary process is due to Turney (1995).
Recently, Noia et al. (2020) applied SVM, k-Nearest Neigh-
bors and k-means as clustering techniques to predict the
probability of contracting a given disease starting from both
workplace-related (using Ateco and Istat codes) and worker-
related characteristics (i.e., age at hiring, age at disease
certiﬁcation, gender, employment duration). They used a GA
to ﬁnd the best values of the used methods. Misclassiﬁca-
tion error rate is used as ﬁtness function. However, since the
classes were not evenly distributed among the instances, they
used a second ﬁtness function that reduces the misclassiﬁca-
tion error rate of the minority class.

An exhaustive search of papers addressing evaluation of
ML algorithms on classiﬁcation is due to Sokolova et al.
(2006). These authors showed that the clear “leaders” are
those papers in which evaluation is performed on data from
the UCI repository, in biomedical and medical sciences,
visual and text classiﬁcation, and language applications.
The most used evaluation measures are accuracy, precision,
recall, F-score, and the Receiver Operating Characteristic
(ROC).

3 Learning model classiﬁers

We optimize hyper-parameters of SVM classiﬁers with Gaus-
sian kernel in order to correctly compare our results found on
public and well-known datasets with those reported in the lit-
erature. Our approach, as it is better detailed in Sect. 5, trains
and uses random trees to reduce the overall computational
time.

In this section, we brieﬂy introduce SVM and decision
trees. Thus, we report the most used performance metrics of a
ML model and discuss their suitability in case of imbalanced
datasets.

3.1 Support vector machine

The SVM was introduced by Cortes and Vapnik (1995) and
is based on statistical learning theory (Vapnik 1998). SVMs
are a class of algorithms for classiﬁcation, regression and
other applications (Cristianini and Shawe-Taylor 2000) and
they are among the most used ML techniques.

Let X , be a dataset with L instances X = (x1, . . . , xL ),
where xi ∈ (cid:3)m, denotes an instance with m features, and
yi ∈ {±1} its label, i = 1, . . . , L. In a binary classiﬁcation
problem, an SVM basically searches for an optimal hyper-
plane that separates patterns of the two classes by maximizing
the margin w ∈ (cid:3)m. Finding the optimal hyperplane means
solving the quadratic programming model (1)-(3), which is
known as soft-margin SVM

123

---

<!-- PAGE 4 -->

12866

min

1
2

||w||2 + C

L(cid:2)

ξi

1

yi (wT φ(xi ) + b) − 1 + ξi ≥ 0 i = 1, . . . , L
ξi ≥ 0 i = 1, . . . , L

(1)

(2)

(3)

where C, named penalty parameter, is a trade-off between
the size of the margin of separation w and the training errors
ξ ; b is the bias and it indicates the offset of the hyperplane
from the origin. Constraints (2) state that when a training
example xi lies on the wrong side of the hyperplane, the
corresponding slack variable ξi is greater than 1. Small values
of C increase the training errors, whereas larger values bring
it closer to the hard-margin SVM. In case of nonlinearly
separable datasets, the SVM basically maps input vectors
into high-dimensional feature spaces by the so-called kernel
functions (Hofmann et al. 2008). A kernel function, denoted
(cid:4)
as K (xi , x j ) =
, is an inner product in a feature
space where it measures similarity between any pair of inputs
xi and x j . A kernel function can take many different forms
(Hofmann et al. 2008), such as

φ(xi ), φ(x j )

(cid:3)

• Linear kernel K (xi , x j ) = (x T
i x j )d
• Polynomial kernel K (xi , x j ) = (x T
• Radial Basis Function (RBF) kernel K (xi , x j ) =

i x j + a)d

ex p(−γ (cid:6)xi − x j (cid:6)2)

The decision function, i.e., the classiﬁer, is speciﬁed by a
subset of training instances, the so-called support vectors,
that are the only vectors that “support” the optimal separating
hyperplane.

It is well known that the performance of most machine
learning algorithms on a given dataset depends on well-tuned
hyper-parameter. In setting up an SVM model, for instance,
two problems are encountered: (1) how to select the kernel
function, and (2) how to select its hyper-parameter. An SVM
with polynomial kernel has three parameters that need to be
optimized: the regularization parameter C, the parameter a,
and the degree d. The optimization of these three parameters
if 50 steps should be performed, requires an amount of time
to test the total 503 = 125000 combinations. The greater the
number of parameters to be set, the greater is the number of
combinations.

The cost-sensitive SVM (CS-SVM) uses two penalty
weights for the two classes. Let C1, be the cost of a false nega-
tive. It penalizes misclassiﬁcation of instances of the minority
class. Analogously, let C−1, be the cost of a false positive. It
penalizes misclassiﬁcation of instances of the majority class.
The optimization model CS-SVM is (4)-(6).

(cid:6)w(cid:6)2 + C[C1

(cid:2)

]ξ i + C−1

(cid:2)

i|yi =1

i|yi =−1

ξi ]

(4)

argmin
w,b,ξ

1
2

123

R. Guido et al.

yi (wT x + b) ≥ 1 − ξi
ξi ≥ 0 i = 1, . . . , L

i = 1, . . . , L

(5)

(6)

Observe that the cost matrices has the diagonal elements
as zero— because of the assumption that a correct classiﬁca-
tion has no cost—and the off-diagonal elements are positive
numbers. However, the range of possibilities for CS-SVM
hyper-parameter can be huge.

Datta and Das (2015) proposes a Near-Bayesian Sup-
port Vector Machine (NBSVM) for imbalanced classiﬁcation
problems by combining decision boundary shift and unequal
regularization costs. Extensive comparison with standard
SVM and some state-of-the-art methods is furnished as a
proof of the ability of the NBSVM to perform competitively
on imbalanced datasets.

3.2 Decision tree

A decision tree is a supervised learning algorithm for regres-
sion and classiﬁcation problems (Breiman et al. 1984) and is
the most popular form of rule-based classiﬁers (Witten and
Frank 2005). It has a set of elements called nodes and is built
top-down from a root node. Each node represents a single
input attribute: leaf nodes contain an output attribute, which
is used to make a prediction; the other nodes are split points
of an attribute. The data is partitioned into homogeneous sub-
sets, i.e., they contain instances with similar values. Given
a new input, the tree is traversed by evaluating the speciﬁc
input started at the root node of the tree.

3.3 Performance evaluation and some limitations

To estimate the generalization performance of an SVM
model, generally one evaluates accuracy measure on data
not used for training the model. The k-fold cross-validation
(k-CV) is the most used procedure. It consists on partitioning
data into k disjoint sets of approximately equal size. An SVM
is thus trained k times: at the i − th iteration, all the disjoint
sets are used as training set except the i − th set, which is
used to evaluate the performance of the model. The errors
observed in this process are averaged yielding the k-fold CV
error.

Before introducing the most used evaluation measures, it
is useful to revise the confusion matrix of binary classiﬁcation
problems. A general confusion matrix is illustrated in Table
1. The two columns refer to the predicted classes, whereas the
two rows refer to the actual classes. True Positives (TP) is the
number of positive instances correctly classiﬁed and False
Negatives (FN) is the number of positive instances incor-
rectly classiﬁed as negative. These two numbers refer to the
minority class. Similarly, True Negatives (TN) is the number
of negative instances correctly classiﬁed, and False Positives

---

<!-- PAGE 5 -->

A hyper-parameter tuning approach...

12867

Table 1 Confusion matrix for a binary problem

Predicted

positive class

negative class

Actual

positive class

negative class

TP

FP

FN

TN

(FP) is the number of negative instances incorrectly classi-
ﬁed as positive class. These two numbers refer to the majority
class. Observe that, in case of data related to patients, a false
negative means that patient has the disease but the diagnosis
result says that it does not have.

The most common evaluation measures used are listed

below.

Accuracy deﬁned as the ratio between the number of
instances correctly classiﬁed and the total number of instances.
It assesses the overall effectiveness of the model by showing
the probability of the true value of the class label

Accuracy =

T P + T N
T P + F P + T n + F N

Other two measures that separately estimate a classiﬁer’s per-
formance on different classes are sensitivity and speciﬁcity.
They are often employed in medical and bio-medical appli-
cations.

Sensitivity (true positive rate) is deﬁned as the ratio between
the number of positive instances correctly classiﬁed as such
and the number of positive instances

Sensitivit y =

T P
T P + F N

Speciﬁcity (true negative rate) is deﬁned as the ratio between
the number of negative instances correctly classiﬁed as such
and the number of negative instances

Speci f icit y =

T N
T N + F P

Precision is deﬁned as the ratio of TP to the number of all
instances predicted as positive

Pr ecision =

T P
T P + F P

As reported especially recently in some papers (e.g., Tao
et al. 2019), the accuracy-based evaluation measure is not
suitable for classiﬁcation of imbalanced data as the minority
class has very little effect on the accuracy compared to the
majority class. For imbalanced classiﬁcation problems, the
correct classiﬁcation of instances of the minority class is usu-
ally the most important measure. There are further interesting

classiﬁcation evaluation measures that allow to balance false
positive rate and false negative rate. Here, among these mea-
sures, we evaluate even F-Measure, the Geometric Mean, the
average cost, the Youden’s index, and the balanced accuracy.
They are deﬁned as follows.

F-Measure integrates sensitivity and precision into an aver-
age by a harmonic mean

F − Measur e = 2Sensitivit y × Pr ecision
Sensitivit y + Pr ecision

The harmonic mean of two numbers tends to be closer to the
smaller number. A high F-Measure value means that both
Sensitivity and Precision are high.

Geometric Mean(G-Mean) is suggested as the balanced per-
formance between the two classes. It is intrinsically deﬁned
as the geometric mean of sensitivity and speciﬁcity. If the
G-Mean value is high, both Sensitivity and Speciﬁcity are
expected to be high simultaneously

(cid:5)

G − Mean =

Sensitivit y × Speci f icit y

Average Cost(AC) is expressed as

Average Cost = C1 × F N + C−1 × F P
T P + T N + F P + F N

where C1 and C−1 are the two costs used in the objective
function of CS-SVM.

Youden’s index Y equally weights the algorithm’s perfor-
mance on positive and negative instances:

Y = sensitivit y + speci f icit y − 1

Balanced accuracy(BA) is the average of sensitivity and
speciﬁcity:

Balanced accuracy = sensitivit y + speci f icit y

2

4 Multi-objective optimization problems

and Genetic algorithms

Multi-objective optimization problems consist of more than
one criterion, often conﬂicting, for which any solution exist-
ing on the Pareto front of criterion trade-offs is considered
optimal.

In this section, we introduce multi-objective optimization
problems and the cornerstone concept of Pareto optimality.
A multi-objective problem consists of minimizing and/or
maximizing two or more objective functions subject to

123

---

<!-- PAGE 6 -->

12868

R. Guido et al.

inequality and/or equality constraints. The objective func-
tions are conﬂicting among them and a solution is a trade-off
in the objective function space.

Deﬁnition 1 A solution is deﬁned Pareto optimal if there
does not exist any other solution in the objective space which
improves the value of any of its objective functions without
deteriorating at least one other objective function value.

In other words, a non-dominated solution provides a suit-
able compromise between all objectives without degrading
any of them. The multi-objective optimization process is
looking for a set of alternative solutions that represent the
Pareto optimal solution. A set of non-dominated individuals
form a Pareto-optimal front.

From the mathematical point of view, the deﬁnition of
the dominance between two solutions x1 and x2 is that x1 is
no worse than x2 in all objectives fi , i ∈ {1, . . . , m} of the
problem. This concept can be expressed as x1 dominates x2
if fi (x1) ≤ fi (x2) ∀i ∈ {1, . . . , m} and ∃ j ∈ {1, . . . , m} :
f j (x1) ≤ f j (x2).

The genetic algorithms were developed by Holland and his
collaborators (Holland 1975) as a model based on Charles
Darwin’s theory of natural selection. They are heuristic
search techniques, successfully applied to different domains
(e.g., Guido and Conforti 2017; Bao-De et al. 2021). Fur-
thermore, they demonstrated a large amount of inherent
parallelism that makes them attractive mainly for solving
problems deﬁned in large feature spaces, as that one here
addressed. The evolutionary process usually starts from a
population of randomly generated individuals, which are the
chromosomes. It is an iterative process. One iteration is one
generation. In each generation, the ﬁtness of every individual
in the population is evaluated. The ﬁtness value of a chromo-
some is a measure of its goodness. The ﬁtness is usually the
value of the objective function in the optimization problem
being solved. Usually, operators such as selection, crossover,
mutation and recombination are applied during the evolu-
tionary process over the generated populations to ﬁnd better
chromosomes, which optimize the ﬁtness function till a ter-
mination condition is reached. The offsprings in a population
act like independent agents so that they explore the search
space in many directions.

As well known, genetic algorithms have some disadvan-
tages mainly due to the choice of parameters such as the
mutation rate and crossover rate that should be carried out
carefully. The crossover operator is one of the most impor-
tant operators because it determines the global convergence
of the genetic algorithm.

4.1 NSGA-II

Srinivas and Deb (1994) proposed an algorithm based
on non-dominated sorting for solving multiobjective prob-

123

lems. This algorithm was called non-dominated sorting
genetic-algorithm (NSGA). Deb et al. (2002) improved it
by proposing NSGA-II. The key features of NSGA-II are
elitism, diversity-preserving mechanisms, and emphasis on
non-dominated solutions. In NSGA-II, the N offsprings are
created from the N parents using standard genetic algorithms.
The new population at the next generation is given by select-
ing the non-dominated solutions for the Pareto front with the
highest diversity while discarding the rest of the solutions.

Tournament selection This is a procedure that imitates sur-
vival of the ﬁttest in nature. Indeed, each individual competes
in two tournaments with randomly selected individuals. The
crowded tournament selection is based on ranking and dis-
tance: if a solution has a better rank than another one, it will
be selected; if the ranks are the same but the crowding dis-
tance is not, the solution with better crowding distance is
selected.

Crowding distance The crowding distance metric of an indi-
vidual proposed by Deb and Goel (2001) aims to select
potential individuals to construct a new population. It is
essentially based on the cardinality of a solution sets and
their distance to solution boundaries. More speciﬁcally, it
is deﬁned as the perimeter of the rectangle with its nearest
neighbors at diagonally opposite corners. Two individuals
with a same rank are better if they have a larger crowding
distance.

Crossover and mutation Crossover and mutation are
employed to obtain the offspring population.

Algorithm 1 shows the framework of NSGA-II. The main

steps of NSGA-II can be summarized as follows:

Step 1 Create a new population by combining parents and
offsprings and apply non-dominated sorting

Step 2 Identify different fronts
Step 3 Generate the new population by exploiting the fronts

given at the previous step until size N

Step 4 Use the crowd distance to carry out a crowding sort

applied to the fronts

Step 5 Generate new offspring from the current population
via the genetic operators crossover, mutation, and
selection

5 Proposed approach

In this section, is ﬁrstly introduced a basic approach for
hyper-parameter optimization. Then, a novel algorithm for
hyper-parameters tuning based on GA and DT is proposed.
The core of the algorithm is a ﬁtness function evaluation
procedure along with a similarity procedure.

---

<!-- PAGE 7 -->

A hyper-parameter tuning approach...

Algorithm 1 NSGA-II
Require:

Random population P0; a child population Q0 is generated from the
population of parents P0 using genetic operators such as crossover
and mutation

12869

Rt = Pt ∪ Qt
fast-non-dominated-sort (Rt )
Pt+1 = ∅; i = 1;
while |Pt+1|+|Fi |< N do

1: while any stopping criterion is not reached do
2:
3:
4:
5:
6:
7:
8:
9:
10:
11:
12:
13:
14: end while

end while
Sort (Fi , < N )
Pt+1 ← Pt+1 ∪ Fi [1 : (N − |Pt + 1|)]
Qt+1 ← create NewPop Pt+1
t ← t + 1

Apply crowding-distance-assignment Fi
Pt+1 ← Pt+1 ∪ Fi
i ← i + 1

Fig. 2 Framework of the improved hyper-parameters algorithm

out is 4800 and the computational time may be extremely
high.

There are two main issues: the ﬁrst one is related to the
time needed to carry out k-fold CV; the second one, is related
to the fact that often a chromosome is slightly different from
another one already evaluated and with equal ﬁtness. We
try to overcome these two issues by introducing a proce-
dure in the NSGA-II algorithm that exploits a suitable and
trained DT. The proposed algorithm, described in the follow-
ing, reduces considerably the overall number of performed
k-fold CV by combining NSGA-II with a DT. The goal is to
evaluate only a small set of chromosomes at each generation
by a k-fold CV. This procedure does not affect convergence of
the algorithm and strongly reduces the overall computational
time.

5.2 Improved hyper-parameters algorithm

The above basic approach has been modiﬁed in order to
evaluate the ﬁtness function only of some individuals of a
population by a k-fold CV. Figure 2 provides an intuitive
understanding of the proposed algorithm framework.

Each chromosome consists of a number of genes that
represent the hyper-parameters of CS-SVM. The algorithm

123

Fig. 1 Main steps of NSGA-II

5.1 Basic approach

The basic approach consists on using NSGA-II algorithm for
solving a multi-objective hyper-parameter tuning problem. A
set of hyper-parameter codiﬁed as a chromosome is evalu-
ated by a k-fold CV approach. A ﬁtness function evaluation
is thus performed at each generation, i.e., each chromosome
has its ﬁtness functions evaluated. However, this approach is
quite time consuming. Indeed, let N , be the number of chro-
mosomes of a population, and G the number of generations.
At each generation, the number of carried out k-fold CV is
N , one per each chromosome. The overall number of per-
formed k-fold CV is thus N × G. For example, if N = 24
and G = 200, the overall number of k-fold CV to be carried

---

<!-- PAGE 8 -->

12870

R. Guido et al.

starts from an initial population Pop0. It consists of the fol-
lowing ﬁve main steps.

Algorithm 2 Proposed hyper-parameters algorithm
1: Step 1 Initialization
2: Step 1.1 Deﬁne GenSet as a set of numbers of generations
3: Step 1.2 Create an initial population Pop0
4: Step 2 (Fitness function evaluation) Evaluate the ﬁtness value of

each chromosome in the current population.

5: if the current generation Gen ∈ GenSet then go to Step 2.1
6: else go to Step 2.2
7: end if
8: Step 2.1 Perform a k-CV
9: Step 2.2 (Similarity procedure) Compare each chromosome with

the ones of the previous population

10: if Similarity= True then assign a ﬁtness value to it by the trained

DT

11: else go to Step 2.1
12: end if
13: Step 3 Termination criteria. If at least one of the stopping conditions

is meet, the algorithm stops

14: Step 4 Train Decision Tree. The current population is used to train

a Decision Tree.

15: Step 5 Reproduce a new population. The operators of selection,
crossover and mutation are applied over the generated population to
ﬁnd better chromosomes.

The core of Algorithm 2 is the ﬁtness evaluation procedure

at Step 2, explained in the following.

Step2: Fitness evaluation procedure The aim of the ﬁtness
evaluation step is to provide a procedure that reduces the
number of ﬁtness evaluations and consequently the number
of carried out k-fold CV. To this purpose, a DT is trained
at each generation and used to predict the ﬁtness value of
some chromosomes, as explained below. Indeed, the ﬁtness
of a chromosome in a population is evaluated or assigned:
A whole population is evaluated by k-fold CV only at those
generations well-deﬁned in the set GenSet. This means that
the cost-sensitive learning classiﬁer SVM-based is built using
the hyper-parameters codiﬁed as chromosomes of the popula-
tion; for every chromosomes, a k-fold CV is used to estimate
the generalization ability of the related build model. The set
GenSet has at least two elements, i.e., the ﬁrst and the last
generation. A procedure based on a learned DT takes place
at those generations not in the set GenSet.

The ﬁtness evaluation procedure is depicted in Fig. 3. To
reduce the overall computational time, the procedure veriﬁes
if each chromosome has already a ﬁtness value (because it
has been evaluated previously). If so, the procedure analyzes
next chromosome; otherwise, the chromosome is compared,
at Step 2.2, with the chromosomes of the previous popu-
lation in order to discover similarity. If the chromosome is
similar at least to one chromosome, the DT trained on the
previous population predicts its ﬁtness value; this value is
thus assigned as predicted value. Otherwise, if no similarity

123

Fig. 3 Fitness evaluation procedure

is found, a cost-sensitive learning classiﬁer SVM-based is
built and the ﬁtness value is evaluated by k-fold CV.

Similarity between two chromosomes can be estimated by
various distance measurement methods. Here, we designed
a procedure that evaluates similarity between two chromo-
somes as follows. Let chr1 and chr2, be two chromosomes
represented as vectors. The procedure compares each corre-
sponding couple of genes of chr1 and chr2, as detailed in
Algorithm 3. More speciﬁcally, the difference between the
i −th gene of chr1 and the corresponding gene of chr2 is com-
puted. If this difference is less than a given threshold ti , the
next couple of genes of the two chromosomes are compared;
otherwise, the procedure stops and the two chromosomes are
not similar.

Figure 4 depicts an example of DT trained to predict a

given ﬁtness function.

6 Experimental results and analysis

In this study, we test the proposed Algorithm 2 for on six
benchmark imbalanced datasets binary classiﬁcation task to
compare the performance of different classiﬁcation methods

---

<!-- PAGE 9 -->

A hyper-parameter tuning approach...

Fig. 4 An example of trained
decision tree

12871

Algorithm 3 Similarity procedure
Require:

Two chromosomes chr1, chr2 ∈ Rk . Threshold ti , i = 1, . . . , k.

else

if |chri1 − chri2|< ti then

i ← i + 1

1: i = 1; similarit y ← tr ue
2: while i ≤ k do
3:
4:
5:
6:
7:
end if
8:
9: end while
10: return similarit y

i ← k
similarit y ← f alse

in the literature with our results. They are related to medical
diagnosis represented as binary classiﬁcation problems and
have different sample sizes, attributes, and imbalance ratio
(IR), deﬁned as m/M (Amin et al. 2016), where m is the
number of the minority instances and M is the number of
majority instances.

We conducted experiments to answer the following

research questions empirically:

1. Does multi-objective optimization ﬁnd much sparser solu-
tions without a major loss in predictive performance
compared to single-objective optimization?
2. Are there alternative metrics to the accuracy?
3. May the computational time be reduced by a machine

learning technique?

A brief description of the datasets is in Sect. 6.1. Details on
the algorithms embedded in our approach and the hyper-
parameter spaces of the several CS-SVM that are being

investigated and tuned over are reported in Sect. 6.2. Exper-
imental results are listed in Sect. 6.3.

6.1 Benchmark datasets

The datasets are from the University of California Irvine
(UCI) Repository
of Machine Learning Databases
(https://archive.ics.uci.edu/ml/datasets.php). They have diver-
sity in the number of attributes and imbalance ratio. More-
over, the datasets have both continuous and categorical
attributes, and some of them have missing values.

Appendicitis dataset consists of 106 instances and 8

attributes. The attributes are results of laboratory test.

Haberman dataset describes the ﬁve-year or greater sur-
vival of breast cancer patients. The study was conducted
between 1958 and 1970 at the University of Chicago’s
Billings Hospital. The dataset consists of 306 instances and
4 attributes. The outcome is patient survival. There are no
missing values.

Hepatitis dataset is used to classify patients with hepati-
tis in the two classes, live or die. It consists of 155 instances
and 19 attributes, 14 nominal attributes and 6 multi-valued
attributes. It requires the determination of whether patients
with hepatitis will either live or die. The problem aims to pre-
dict the presence or absence of hepatitis by using the results
of various medical tests carried out on a patient. The dataset
has missing values.

Pima Indian Diabetes dataset is used to predict whether
or not a patient has diabetes. All patients are female, are at
least 21 years old, and are of Pima Indian heritage. It has 8
laboratory features.

123

---

<!-- PAGE 10 -->

12872

R. Guido et al.

Table 2 Datasets and their main characteristics in terms of number of
attributes (No. A), number of the minority instances (m), number of the
majority instances (M), index ratio I R = m/M

Dataset

No. A

Appendicitis

Haberman

Hepatitis

Pima

WDBC

WPBC

8

4

19

9

10

32

m

21

81

70

268

241

47

M

85

225

85

500

458

151

I R

0.25

0.36

0.82

0.53

0.53

0.33

Wisconsin Diagnostic Breast Cancer (WDBC) dataset
consists of 30 features computed by digitized image of ﬁne
needle aspirate of a breast mass index. The problem aims to
predict whether or not the patient has breast cancer.

Wisconsin Prognostic Breast Cancer (WPBC) dataset has
198 instances that represent follow-up data for one breast can-
cer case, only those cases exhibiting invasive breast cancer
and no evidence of distant metastases at the time of diagno-
sis. It is used in this paper to classify patients as recurrences
before 24 months (positive class) or non-recurrence beyond
24 months (negative class). We removed the feature named
“Time” from the dataset because it is the recurrence time for
instances in the positive class and the disease-free time for
the instances of the negative class.

Table 2 summarizes, per each dataset, the number of
attributes, the number of minority instances (diseased exam-
ples), the number of the majority instances (non-diseased
examples), and the index ratio.

6.2 Learning algorithms and hyperparameters

optimization

We considered several model classiﬁers CS-SVM with Gaus-
sian kernel tuned by the optimization algorithm proposed.
The experiments were performed by the ML algorithms of
Waikato Environment for Knowledge Analysis (WEKA).
WEKA is an open-source collection of ML algorithms and
data processing tools. We used Sequential minimal optimiza-
tion algorithm for SVM and Random Tree algorithm for
DT. For that concerning NSGA-II algorithm, we used the
framework named Java Class Library for Evolutionary Com-
putation (JCLEC) Ramírez et al. (2015, 2019), which is a
Java suite for solving multi-objective optimization problems
using evolutionary algorithms.

Algorithm 2 has been coded in Java using the NSGA
II algorithm of the JCLEC framework. We executed both
the sequential and the parallel version of the NSGA-II. The
parallel version is more efﬁcient since it performs function
evaluations of different individuals in parallel. The experi-

123

Fig. 5 Representation of a chromosome

ments were run on a PC Intel Xeon E5 1620 CPUs with 4
cores at 3.50 GHz and 32 GB RAM.

6.2.1 Parameter setting

Algorithm 2 starts from an initial population Pop0 of chro-
mosomes randomly generated. Each chromosome has four
genes representing the hyper-parameter of CS-SVM, as
depicted in Fig. 5. All experiments have the same random
initial population; the number of generations is the only one
stopping criterion.

Table 3 lists the search population size, crossover probabil-
ity pc, gene mutation probability pm, number of generations
along with the design parameters (decision variables) and
the range of their variations. We tested two population sizes
and created the initial parent population randomly by select-
ing solutions from the ranges deﬁned for the parameters
C, C1, C2, γ , where C1 and C2 are the costs of the minority
class and majority class, respectively.

The multi-objective problem that we formulated and
solved has three ﬁtness functions (7–9), given by accuracy,
G-mean, and Average Cost, respectively:

f1 = max

f2 = max

f3 = min

T P + T N
T P + F P + T N + F N
(cid:5)

Sensitivit y × Speci f icit y
C1 × F N + C2 × F P
T P + T N + F P + F N

(7)

(8)

(9)

All the experiments are conducted by 10-fold cross-validation.

6.3 Computational results

To assess our approach, we performed both Algorithm 1 and
Algorithm 2 on the six datasets and compared the results.
The computational experiments were carried out using the
JCLEC sequential algorithm and its parallelized version. The
only difference we noticed was the reduced computational
time of the parallelized version with respect to the sequential
algorithm. We report in this section only the results found by
the parallel version.

Table 4 reports the best ﬁtness values per each dataset.
From the second to the fourth column there is the value of
accuracy, G-Mean, and average cost, respectively. We com-
pare in this table our results with the best ones of the literature
by selecting those papers that optimized hyper-parameter of

---

<!-- PAGE 11 -->

A hyper-parameter tuning approach...

Table 3 NSGA-II parameters
and hyper-parameters spaces of
CS-SVM with RBF kernel

12873

NSGA-II parameters

CS-SVM hyper-parameter space

Popsi ze

24

48

pc

0.8

pm

0.25

Num Gen

Cost

100

200

1000

C ∈ {1 − 50}
C1 ∈ {1 − 20}
C2 ∈ {1 − 10}

γ

{0.001 − 1}

Table 4 Best metric values by
the optimized hyper-parameters
compared to the best results of
the literature. [1] (Yu and Wang
2017); [2] (Qi et al. 2013);
[3](Tao et al. 2019). Hyphen
means that the authors did not
test that dataset

Dataset

Accuracy

G-Mean

AC

Appendicitis

Haberman

Hepatitis

Pima

WDBC

WPBC

89.62

76.14

87.10

78.13

97.42

77.78

82.54

67.70

84.06

76.54

97.73

61.54

0.11

0.26

0.14

0.22

0.03

0.22

Bold indicates the best accuracy values

Acc
[1]

–

–

83.22

76.27

–

81.28

AC
[2]

–

–

0.208

0.457

–

–

G-Meana
[3]

G-Meanb
[3]

60.77±3.89

66.71±1.67

64.60±3.16
92.41±2.44
27.38±11.69

75.13±1.67
96.91±1.79
67.53±3.71

SVM with RBF kernel. Under these conditions, experimen-
tal evidence shows that our algorithm ﬁnds similar results or
outperforms the other algorithms proposed in the literature.
The best results in terms of accuracy on Hepatitis, Pima, and
WPBC datasets are found in (Yu and Wang 2017) by optimiz-
ing the parameters of the SVM with RBF kernel by a novel
ensemble differential evolution approach that they proposed.
Several approaches were tested in (Tao et al. 2019) and the
results were reported in terms of G-Mean. In Table 4, we
denoted with G-Meana and G-Meanb the values found by
CS-SVM and their self-adaptive cost weights-based support
vector machine cost-sensitive ensemble approach, respec-
tively. It is helpful to notice that they reported these results
on the datasets by modifying imbalanced data ratio of 10:1.
Tables 5, 6, 7, 8 list only some of the found non-dominated
solutions of the Pareto front of our experimental results.
These results refer to the experiments carried out with the
related parallelized version of Algorithms 1 and 2. The ﬁrst
and second column of these tables report the population size
and the number of carried out generations; the next three
columns show the ﬁtness function values associated with
the optimal hyper-parameter conﬁguration, which is reported
in the next four columns. The eleventh and twelfth column
reports the sensitivity and speciﬁcity values, whereas the next
four columns report the ROC area, the F-Measure, the bal-
anced accuracy, and the Youden’s index, respectively. Finally,
the last column shows the average computational time, in
minutes.

As already observed in the literature, the accuracy is not
a suitable measure for imbalanced data. Indeed, we noticed
that in the Haberman dataset, for instance, there is a hyper-
parameter conﬁguration that allows to have a good accuracy
equal to 75.53%, but the speciﬁcity is zero as well as the

G-mean value. Similar cases are on the Hepatitis and WPBC
datasets.

Tables 5 and 6 show the results found by Algorithm 1
on the six datasets along with the related optimized hyper-
parameter conﬁguration. For the Appendicitis dataset, for
instance, the best accuracy in Table 5 is f1 = 89.62; the best
G-Mean is f2 = 82.54, and the best average cost is f3 =
0.11. As expected, the improvement of a ﬁtness function
implies a worsening in the other two. We observe that the
single optimal ﬁtness values are found with different hyper-
parameter tuning. Moreover, the best results are found in
all the experiments even if number of population size and
generation number is increased.

Tables 7 and 8 show the results found by Algorithm 2
on the six datasets along with the related optimized hyper-
parameter conﬁguration. These results were found in very
contracted computational time if compared to the previous
ones. Observe that there has been a reduction over 70%
in some experiments. These results show that the proposed
Algorithm 2 is efﬁcient.

The results evidenced that: (1) both algorithms converge
and ﬁnd the same best values for the three ﬁtness functions;
(2) the number of optimal non-dominated solutions of the
Pareto front found by Algorithm 1 is greater than the num-
ber found by Algorithm 2. To better understand our ﬁnding,
we illustrate in Figs. 6 and 7 the Pareto points of Tables 7
and 8 per each dataset with the six performance measures.
The Pareto points are shown considering decreasing Sen-
sitivity. As depicted in these two ﬁgures, generally balance
accuracy decreases as Sensitivity decreases while Sensitivity
increases. The best Pareto points related to medical datasets,
as those tested in this paper, should be the points with high
balance accuracy or high sensitivity values.

123

---

<!-- PAGE 12 -->

R. Guido et al.

12874

e
m
T

i

s
c
i
r
t
e
m
e
c
n
a
m
r
o
f
r
e
P

r
a
p
-
r
e
p
y
H
d
e
z
i
m

i
t
p
O

s
n
o
i
t
c
n
u
f

s
s
e
n
t
i
F

.

m
a
r
a
p

.
n
e
G

t
e
s
a
t
a
D

s
t
e
s
a
t
a
d
s
i
t
i
t
a
p
e
H
d
n
a

,

n
a
m
r
e
b
a
H

,
s
i
t
i
c
i
d
n
e
p
p
A
n
o
s
t
l
u
s
e
r

l
a
t
n
e
m

i
r
e
p
x
E

:
1
m
h
t
i
r
o
g
l
A

5
e
l
b
a
T

6
7
.
0

2
4
.
1

9
0
.
7

4
4
.
1

3
8
.
2

3
1
.
4
1

1
4
.
4

2
0
.
9

6
9
.
7
3

4
8
5
.
0

6
5
6
.
0

6
3
5
.
0

4
8
5
.
0

6
5
6
.
0

6
3
5
.
0

4
8
5
.
0

6
5
6
.
0

6
3
5
.
0

4
8
5
.
0

7
4
5
.
0

6
5
6
.
0

3
4
6
.
0

4
8
5
.
0

7
4
5
.
0

4
8
5
.
0

7
4
5
.
0

6
5
6
.
0

5
1
3
.
0

8
2
3
.
0

3
8
0
.
0

5
1
3
.
0

2
3
3
.
0

3
8
0
.
0

5
1
3
.
0

9
4
3
.
0

7
8
0
.
0

2
9
7
.
0

8
2
8
.
0

8
6
7
.
0

2
9
7
.
0

8
2
8
.
0

8
6
7
.
0

2
9
7
.
0

8
2
8
.
0

8
6
7
.
0

2
9
7
.
0

3
7
7
.
0

8
2
8
.
0

5
1
2
8
.
0

2
9
7
.
0

3
7
7
.
0

2
9
7
.
0

3
7
7
.
0

8
2
8
.
0

7
5
6
.
0

4
6
6
.
0

1
4
5
.
0

7
5
6
.
0

6
6
6
.
0

1
4
5
.
0

7
5
6
.
0

4
7
6
.
0

5
3
4
5
.
0

7
.
0

7
.
0

7
6
.
0

7
.
0

7
.
0

7
6
.
0

7
.
0

7
.
0

7
6
.
0

7
.
0

9
6
.
0

7
.
0

1
7
.
0

7
.
0

9
6
.
0

7
.
0

9
6
.
0

7
.
0

9
4
.
0

1
5
.
0

2
.
0

9
4
.
0

1
5
.
0

2
.
0

9
4
.
0

2
5
.
0

2
.
0

2
9
7
.
0

8
2
8
.
0

8
6
7
.
0

2
9
7
.
0

8
2
8
.
0

8
6
7
.
0

2
9
7
.
0

8
2
8
.
0

8
6
7
.
0

2
9
7
.
0

4
7
7
.
0

8
2
8
.
0

2
2
8
.
0

2
9
7
.
0

4
7
7
.
0

2
9
7
.
0

4
7
7
.
0

8
2
8
.
0

8
5
6
.
0

4
6
6
.
0

2
4
5
.
0

8
5
6
.
0

6
6
6
.
0

2
4
5
.
0

8
5
6
.
0

4
7
6
.
0

4
4
5
.
0

5
6
9
.
0

4
9
8
.
0

5
6
9
.
0

5
6
9
.
0

4
9
8
.
0

5
6
9
.
0

5
6
9
.
0

4
9
8
.
0

5
6
9
.
0

5
6
9
.
0

6
7
9
.
0

4
9
8
.
0

9
2
9
.
0

5
6
9
.
0

6
7
9
.
0

5
6
9
.
0

6
7
9
.
0

4
9
8
.
0

1
7
8
.
0

6
7
.
0

6
9
.
0

1
7
8
.
0

4
6
7
.
0

6
9
.
0

1
7
8
.
0

6
5
7
.
0

4
6
9
.
0

9
1
6
0

.

2
6
7
0

.

1
7
5
0

.

9
1
6
0

.

2
6
7
0

.

1
7
5
0

.

9
1
6
0

.

2
6
7
0

.

1
7
5
0

.

9
1
6
0

.

1
7
5
0

.

2
6
7
0

.

4
1
7
0

.

9
1
6
0

.

1
7
5
0

.

9
1
6
0

.

1
7
5
0

.

2
6
7
0

.

4
4
4
0

.

8
6
5
0

.

3
2
1
0

.

4
4
4
0

.

8
6
5
0

.

3
2
1
0

.

4
4
4
0

.

3
9
5
0

.

3
2
1
0

.

2

4

1

2

4

1

2

4

1

2

1

4

8
1

2

1

2

1

4

2

3
1

1

2

3
1

1

2

3
1

1

1

1

1

1

1

1

1

1

1

1

1

1

5

1

1

1

1

1

1

4

1

1

4

1

1

4

1

Y

A
B

M
-
F

a
e
r
a
C
O
R

c
e
p
S

s
n
e
S

2
C

1
C

1
0
0

.

8
3
0

.

8
1
0

.

8
1
0

.

8
3
0

.

8
3
0

.

8
1
0

.

8
3
0

.

8
3
0

.

1
0
0

.

2
1
0

.

4
0

.

1
0
0

.

1
0
0

.

2
1
0

.

1
0
0

.

2
1
0

.

4
0

.

6
8
0

.

3
5
0

.

4
7
0

.

6
8
0

.

3
5
0

.

4
7
0

.

6
8
0

.

6
8
0

.

6
8
0

.

γ

C

3
3

9

5
4

2

9

0
1

2

9

5
1

9
3

9
3

0
1

3

6
2

9
3

6
2

9
3

1
1

9
4

9
4

8
4

6
4

8
3

9
2

6
4

3
1

3
2

3
f

8
1
0

.

7
2
0

.

1
1
0

.

8
1
0

.

7
2
0

.

1
1
0

.

8
1
0

.

7
2
0

.

1
1
0

.

8
1
0

.

1
0

.

7
2
0

.

3
1

.

8
1
0

.

1
0

.

8
1
0

.

1
0

.

7
2
0

.

9
3
0

.

9
1
2

.

6
2
0

.

9
3
0

.

8
1
2

.

6
2
0

.

9
3
0

.

2
1
2

.

6
2
0

.

2
f

1
f

n
e
G

e
z
i
s

p
o
P

8
2
7
7

.

4
5
2
8

.

5
2
4
7

.

8
2
7
7

.

4
5
2
8

.

5
2
4
7

.

8
2
7
7

.

4
5
2
8

.

5
2
4
7

.

8
2
7
7

.

.

7
4
7

4
5
2
8

.

8
4
1
8

.

8
2
7
7

.

.

7
4
7

8
2
7
7

.

.

7
4
7

4
5
2
8

.

2
2
2
6

.

.

7
5
6

3
4
4
3

.

2
2
2
6

.

9
8
5
6

.

3
4
4
3

.

2
2
2
6

.

1
9
6
6

.

1
5
4
3

.

2
6
.
9
8

9
7
.
6
8

8
6
.
8
8

2
6
.
9
8

9
7
.
6
8

8
6
.
8
8

2
6
.
9
8

9
7
.
6
8

8
6
.
8
8

2
6
.
9
8

2
6
.
9
8

9
7
.
6
8

8
6
.
8
8

2
6
.
9
8

2
6
.
9
8

2
6
.
9
8

2
6
.
9
8

9
7
.
6
8

2
8
.
5
7

2
9
.
0
7

6
8
.
3
7

2
8
.
5
7

4
2
.
1
7

6
8
.
3
7

2
8
.
5
7

4
2
.
1
7

8
1
.
4
7

0
0
2

0
0
0
1

0
0
2

0
0
0
1

0
0
1

8
4

0
0
1

4
2

s
i
t
i
c
i
d
n
e
p
p
A

0
0
2

0
0
0
1

0
0
1

4
2

n
a
m
r
e
b
a
H

123

---

<!-- PAGE 13 -->

A hyper-parameter tuning approach...

12875

e
m
T

i

8
7
.
6

5
3
.
3
1

2
9
.
6
6

4
9
.
0

8
7
.
1

3
0
.
9

2
8
.
1

5
4
.
3

6
8
.
6
1

2
3
.
0

3
5
3
.
0

9
9
0
.
0

2
3
.
0

3
5
3
.
0

9
9
0
.
0

8
0
.
0

2
3
.
0

6
6
3
.
0

9
9
0
.
0

1
2
6
.
0

9
5
6
.
0

4
4
5
.
0

1
2
6
.
0

9
5
6
.
0

4
4
5
.
0

3
6
.
0

1
8
6
.
0

4
4
5
.
0

3
6
.
0

5
7
6
.
0

1
2
5
.
0

3
6
.
0

5
7
6
.
0

4
4
5
.
0

3
6
.
0

1
8
6
.
0

4
4
5
.
0

6
6
.
0

6
7
6
.
0

9
4
5
.
0

6
6
.
0

6
7
6
.
0

9
4
5
.
0

4
5
.
0

6
6
.
0

3
8
6
.
0

9
4
5
.
0

0
1
8
.
0

9
2
8
.
0

2
7
7
.
0

0
1
8
.
0

9
2
8
.
0

2
7
7
.
0

5
1
8
.
0

0
4
8
.
0

2
7
7
.
0

5
1
8
.
0

7
3
8
.
0

0
6
7
.
0

5
1
8
.
0

7
3
8
.
0

2
7
7
.
0

5
1
8
.
0

5
0
4
8
.
0

2
7
7
.
0

5
.
0

3
5
.
0

3
2
.
0

5
.
0

3
5
.
0

3
2
.
0

9
1
.
0

5
.
0

3
5
.
0

3
2
.
0

9
6
.
0

8
6
.
0

5
6
.
0

9
6
.
0

8
6
.
0

5
6
.
0

7
.
0

8
6
.
0

5
6
.
0

7
.
0

9
6
.
0

3
6
.
0

7
.
0

9
6
.
0

5
6
.
0

7
.
0

8
6
.
0

5
6
.
0

6
6
.
0

7
7
6
.
0

5
5
.
0

6
6
.
0

7
7
6
.
0

5
5
.
0

4
5
.
0

6
6
.
0

3
8
6
.
0

5
5
.
0

1
1
8
.
0

9
2
8
.
0

2
7
7
.
0

1
1
8
.
0

9
2
8
.
0

2
7
7
.
0

5
1
8
.
0

1
4
8
.
0

2
7
7
.
0

5
1
8
.
0

7
3
8
.
0

6
7
.
0

5
1
8
.
0

7
3
8
.
0

2
7
7
.
0

5
1
8
.
0

1
4
8
.
0

2
7
7
.
0

6
7
8
.
0

1
1
7
.
0

1
5
9
.
0

6
7
8
.
0

1
1
7
.
0

1
5
9
.
0

9
6
9
.
0

6
7
8
.
0

3
7
7
.
0

1
5
9
.
0

2
0
9
.
0

6
4
8
.
0

9
1
9
.
0

2
0
9
.
0

6
4
8
.
0

9
1
9
.
0

1
1
9
.
0

7
3
8
.
0

9
1
9
.
0

1
1
9
.
0

2
6
8
.
0

7
2
9
.
0

1
1
9
.
0

2
6
8
.
0

9
1
9
.
0

1
1
9
.
0

7
3
8
.
0

9
1
9
.
0

4
4
4
0

.

2
4
6
0

.

8
4
1
0

.

4
4
4
0

.

2
4
6
0

.

8
4
1
0

.

1
1
1
0

.

4
4
4
0

.

3
9
5
0

.

8
4
1
0

.

9
1
7
0

.

3
1
8
0

.

5
2
6
0

.

9
1
7
0

.

3
1
8
0

.

5
2
6
0

.

9
1
7
0

.

4
4
8
0

.

5
2
6
0

.

9
1
7
0

.

3
1
8
0

.

4
9
5
0

.

9
1
7
0

.

3
1
8
0

.

5
2
6
0

.

9
1
7
0

.

4
4
8
0

.

5
2
6
0

.

2

7

1

2

7

1

1

2

3
1

1

2

2

1

2

2

1

2

1

1

2

2

1

2

2

1

2

1

1

1

2

1

1

2

1

1

1

4

1

3

9

1

3

9

1

3

5

1

3

7

1

3

7

1

3

5

1

Y

A
B

M
-
F

a
e
r
a
C
O
R

c
e
p
S

s
n
e
S

2
C

1
C

4
9
0

.

2
4
0

.

4
9
0

.

4
9
0

.

2
4
0

.

4
9
0

.

2
5
0

.

4
9
0

.

4
9
0

.

4
9
0

.

1
0
0

.

1
0
0

.

1
0
0

.

1
0
0

.

1
0
0

.

1
0
0

.

1
0
0

.

1
0
0

.

1
0
0

.

1
0
0

.

1
0
0

.

2
3
0

.

1
0
0

.

1
0
0

.

1
0
0

.

1
0
0

.

1
0
0

.

1
0
0

.

γ

C

9
4

9
3

9
4

9
4

9
3

9
4

7
4

9
4

2

9
4

0
4

8

7
4

9
3

8

7
4

5
3

8

7
4

2
3

0
1

0
1

2
3

0
1

7
4

2
3

8

7
4

3
f

9
3
0

.

9
0
1

.

6
2
0

.

9
3
0

.

9
0
1

.

6
2
0

.

6
2
0

.

9
3
0

.

7
0
2

.

6
2
0

.

3
3
0

.

9
5
0

.

4
1
0

.

3
3
0

.

9
5
0

.

4
1
0

.

2
3
0

.

9
2
0

.

4
1
0

.

2
3
0

.

9
4
0

.

4
1
0

.

2
3
0

.

9
4
0

.

4
1
0

.

2
3
0

.

9
2
0

.

4
1
0

.

8
3
2
6

.

7
5
7
6

.

4
5
7
3

.

8
3
2
6

.

7
5
7
6

.

4
5
7
3

.

1
8
2
3

.

8
3
2
6

.

.

7
7
6

4
5
7
3

.

4
5
0
8

.

8
8
2
8

.

8
7
5
7

.

4
5
0
8

.

8
8
2
8

.

8
7
5
7

.

.

9
0
8

6
0
4
8

.

8
7
5
7

.

.

9
0
8

8
6
3
8

.

8
1
4
7

.

.

9
0
8

8
6
3
8

.

8
7
5
7

.

.

9
0
8

6
0
4
8

.

8
7
5
7

.

4
1
.
6
7

8
2
.
9
6

6
8
.
3
7

4
1
.
6
7

8
2
.
9
6

6
8
.
3
7

8
1
.
4
7

4
1
.
6
7

5
5
.
2
7

6
8
.
3
7

5
4
.
6
8

7
8
.
3
8

1
8
.
5
8

5
4
.
6
8

7
8
.
3
8

1
8
.
5
8

1
.
7
8

7
8
.
3
8

1
8
.
5
8

1
.
7
8

6
1
.
5
8

1
8
.
5
8

1
.
7
8

6
1
.
5
8

1
8
.
5
8

1
.
7
8

7
8
.
3
8

1
8
.
5
8

2
f

1
f

n
e
G

0
0
1

0
0
2

0
0
0
1

e
z
i
s

p
o
P

8
4

0
0
1

4
2

s
i
t
i
t
a
p
e
H

0
0
2

0
0
0
1

0
0
2

0
0
0
1

0
0
1

8
4

s
c
i
r
t
e
m
e
c
n
a
m
r
o
f
r
e
P

r
a
p
-
r
e
p
y
H
d
e
z
i
m

i
t
p
O

s
n
o
i
t
c
n
u
f

s
s
e
n
t
i
F

.

m
a
r
a
p

.
n
e
G

t
e
s
a
t
a
D

d
e
u
n
i
t
n
o
c

5
e
l
b
a
T

123

---

<!-- PAGE 14 -->

12876

R. Guido et al.

Table 6 Algorithm 1: Experimental results on the datasets Pima, WDBC, and WPBC

Dataset Gen. param.

Fitness functions

Optimized Hyper-par

Performance metrics

Time

C1 C2

Sens

Spec

ROC area F-M BA

Y

7

1

5

1

7

1

5

1

7

1

7

1

1

7

1

1

7

1

1

10

7

1

2

1

2

1

2

1

1

1

1

1

3

1

1

1

3

1

1

3

6

1

2

1

6

1

2

1

6

1

3

1

1

3

1

1

3

1

1

9

3

1

5

5

5

5

5

2

3

3

3

4

1

5

4

8

1

4

8

1

0.604

0.874

0.739

0.56

0.898

0.729

0.843

0.69

0.767

0.571

0.886

0.728

0.604

0.874

0.739

0.56

0.898

0.729

0.843

0.69

0.767

0.571

0.886

0.728

0.604

0.874

0.739

0.56

0.898

0.729

0.832

0.704

0.768

0.66

0.64

0.7

0.64

0.66

0.64

0.7

0.64

0.66

0.64

0.7

0.739

0.729

0.766

0.728

0.739

0.729

0.766

0.728

0.739

0.729

0.768

0.571

0.89

0.73

0.64

0.730

0.478

10.19

0.458

0.533

0.457

0.478

20.31

0.458

0.533

0.457

0.478

100.99

0.458

0.536

0.461

0.556

0.902

0.729

0.64

0.729

0.458

21.26

0.832

0.704

0.768

0.571

0.89

0.73

0.556

0.902

0.729

0.832

0.704

0.768

0.571

0.89

0.73

0.556

0.902

0.729

0.593

0.882

0.738

0.832

0.704

0.768

0.7

0.64

0.64

0.7

0.64

0.64

0.65

0.7

0.768

0.730

0.729

0.768

0.730

0.729

0.737

0.768

0.575

0.89

0.732

0.65

0.732

0.536

0.461

0.458

41.87

0.536

0.461

0.458

210.71

0.475

0.536

0.465

0.988

0.967

0.977

0.996

0.959

0.977

0.988

0.967

0.977

0.996

0.959

0.977

0.988

0.967

0.977

0.983

0.967

0.975

0.988

0.967

0.977

0.988

0.967

0.977

0.988

0.967

0.977

0.085

0.993

0.539

0.489

0.762

0.625

0.021

1

0.511

0.085

0.993

0.539

0.064

1

0.532

0.489

0.762

0.625

0.085

0.993

0.064

1

0.489

0.762

150

151

115

0.96

0.96

0.96

0.96

0.96

0.96

0.96

0.96

0.96

0.15

0.43

0.04

0.15

0.12

0.43

0.15

0.12

0.43

0.9775

0.955

2.26

0.9775

0.955

0.9775

0.955

7.49

0.9775

0.955

0.9775

0.955

30.76

0.975

0.95

0.9775

0.955

0.9775

0.955

9.44

11.8

0.9775

0.955

50.86

0.539

0.078

1.65

0.6255

0.251

0.5105

0.021

0.539

0.532

0.078

3.25

0.064

0.6255

0.251

0.539

0.532

0.078

16.17

0.064

0.6255

0.251

Pop size Gen

f1

f2

f3

Pima

24

100

77.99

72.69

77.99

70.9

74.35

76.28

77.6

71.12

200

77.99

72.69

77.99

70.9

74.35

76.28

77.6

71.12

1000

77.99

72.69

77.99

70.9

74.87

76.54

77.86

71.28

48

100

78.13

70.82

74.87

76.54

77.86

71.28

200

78.13

70.82

74.87

76.54

77.86

71.28

1000

78.13

70.82

78.13

72.34

74.87

76.54

77.99

71.51

WDBC 24

100

97.42

97.73

97.14

97.7

200

97.42

97.73

97.14

97.7

1000

97.42

97.73

97.28

97.53

100

200

97.42

97.73

97.42

97.73

1000

97.42

97.73

48

WPBC 24

100

77.78

29.08

69.7

61.05

76.77

14.59

200

77.78

29.08

77.78

25.26

69.7

61.05

1000

77.78

29.08

77.78

25.26

69.7

61.05

1.46

0.22

0.68

0.22

1.46

0.22

0.68

0.22

1.46

0.22

0.99

0.22

0.22

0.99

0.22

0.22

0.99

0.22

0.22

2.11

0.99

0.22

0.06

0.03

0.06

0.03

0.06

0.03

0.03

0.03

0.03

0.24

0.55

0.23

0.24

0.22

0.55

0.24

0.22

0.55

C

5

4

5

10

5

4

5

10

5

4

4

15

4

4

19

4

4

19

4

4

4

18

10

6

10

6

8

5

8

8

8

38

1

38

44

32

1

18

32

1

γ

0.24

0.53

0.53

0.53

0.24

0.53

0.53

0.53

0.24

0.53

0.53

0.53

0.47

0.47

0.47

0.47

0.47

0.47

0.47

0.47

0.47

0.47

0.42

0.42

0.42

0.42

0.42

0.42

0.09

0.09

0.09

0.24

0.24

0.24

0.24

0.42

0.24

0.42

0.42

0.24

123

---

<!-- PAGE 15 -->

A hyper-parameter tuning approach...

Table 6 continued

Dataset Gen. param.

Fitness functions

Optimized Hyper-par

Performance metrics

12877

Time

Pop size Gen

f1

f2

f3

48

100

77.78

25.26

77.78

29.08

68.69

61.54

200

77.78

29.08

77.78

25.26

68.69

61.54

1000

77.78

29.08

77.78

25.26

68.69

61.54

0.22

0.24

1.75

0.24

0.22

1.75

0.23

0.22

1.75

C

47

32

46

33

33

44

21

33

48

γ

0.33

0.32

0.01

0.32

0.32

0.01

0.32

0.32

0.01

C1 C2

Sens

Spec

ROC area F-M BA

Y

1

1

10

1

1

10

1

1

10

9

5

3

5

6

3

3

6

3

0.064

1

0.532

0.085

0.993

0.539

0.511

0.742

0.626

0.085

0.993

0.539

0.064

1

0.532

0.511

0.742

0.626

0.085

0.993

0.539

0.064

1

0.532

0.511

0.742

0.626

0.12

0.15

0.44

0.15

0.12

0.44

0.15

0.12

0.44

0.532

0.539

0.064

3.15

0.078

0.6265

0.253

0.539

0.532

0.078

6.34

0.064

0.6265

0.253

0.539

0.532

0.078

31.85

0.064

0.6265

0.253

Table 7 Algorithm 2: Experimental results on the datasets Appendicitis, Haberman, and Hepatitis

Dataset

Gen. param.

Fitness functions

Optimized Hyper-par

Performance metrics

Time

Pop size Gen

f1

f2

f3

C γ

C1 C2

Sens

Spec ROC area F-M BA

Y

Appendicitis 24

100

89.62 77.28 0.18

23 0.01 1

86.79 80.44 0.3

10 0.01 1

84.91 60.62 0.15

24 0.01 1

200

89.62 77.28 0.36

35 0.01 2

86.79 82.54 0.32

28 0.13 1

1000 89.62 77.28 0.18

38 0.01 1

87.74 80.96 0.29

8

0.01 1

48

100

89.62 77.28 0.36

29 0.01 2

87.74 80.96 0.29

29 0.01 1

86.79 67.78 0.13

36 0.01 1

200

89.62 77.28 0.18

11 0.01 1

2

4

1

4

5

2

4

4

4

1

2

86.79 82.54 1.19

9

0.47 4

18

1000 89.62 77.28 0.18

18 0.01 1

87.74 80.96 0.29

8

0.01 1

84.91 57.05 0.15

22 0.01 1

Haberman

24

100

76.14 62.38 0.39

68.3

66.49 1.12

42 1

11 1

1

2

73.53 0

0.26

23 0.94 2

200

76.14 57.81 1.38

29 0.12 3

67.32 66.29 1.13

3

0.94 2

75.82 62.22 0.39

42 0.94 1

1000 76.14 62.38 0.39

35 0.94 1

2

4

1

2

7

1

7

7

2

2

0.619 0.965 0.792

0.7

0.792 0.584 0.37

0.714 0.906 0.81

0.68 0.81

0.62

0.381 0.965 0.673

0.619 0.965 0.792

0.762 0.894 0.828

0.619 0.965 0.792

0.714 0.918 0.816

0.619 0.965 0.792

0.714 0.918 0.816

0.5

0.7

0.7

0.7

0.7

0.7

0.7

0.673 0.346

0.792 0.584 0.55

0.828 0.656

0.792 0.584 1.94

0.816 0.632

0.792 0.584 0.61

0.816 0.632

0.476 0.965 0.72

0.59 0.720 0.441

0.619 0.965 0.792

0.762 0.894 0.828

0.619 0.965 0.792

0.714 0.918 0.816

0.7

0.7

0.7

0.7

0.792 0.584 0.91

0.828 0.656

0.792 0.584 3.07

0.816 0.632

0.333 0.976 0.655

0.47 0.654 0.309

0.444 0.876 0.66

0.5

0.66

0.32

1.82

0.63

0.702 0.666

0.51 0.666 0.332

0

1

0.5

0

0.5

0

0.37

0.902 0.636

0.45 0.636 0.272 3.8

0.642 0.684 0.663

0.51 0.663 0.326

0.444 0.871 0.658

0.49 0.657 0.315

0.444 0.876 0.66

0.5

0.66

0.32

19.47

70.92 67.21 1.6

11 0.94 3

10

0.605 0.747 0.676

0.52 0.676 0.352

73.86 37.54 0.26

49 0.94 1

48

100

76.14 62.38 0.39

49 0.94 1

68.95 67.35 1.09

15 0.63 2

73.86 37.54 0.26

49 0.94 1

200

76.14 62.38 0.39

49 0.94 1

69.28 67.57 1.09

24 0.63 2

73.86 34.43 0.26

49 0.56 1

1

2

7

1

2

7

1

0.148 0.951 0.55

0.23 0.549 0.099

0.444 0.876 0.66

0.5

0.66

0.32

4.29

0.642 0.707 0.674

0.52 0.674 0.349

0.148 0.951 0.55

0.23 0.549 0.099

0.444 0.876 0.66

0.5

0.66

0.32

6.74

0.642 0.711 0.677

0.53 0.676 0.353

0.123 0.96

0.542

0.2

0.541 0.083

123

---

<!-- PAGE 16 -->

12878

Table 7 continued

R. Guido et al.

Dataset

Gen. param.

Fitness functions

Optimized Hyper-par

Performance metrics

Time

Pop size Gen

f1

f2

f3

1000

76.14

62.38

0.39

69.61

67.33

2.7

Hepatitis

24

100

87.1

79.47

73.53

0

83.23

82.49

83.23

67.78

200

87.1

80.9

83.23

82.49

84.52

71.89

1000

87.1

80.9

83.87

84.06

79.35

0

48

100

86.45

80.54

83.23

83.65

85.81

74.18

200

87.1

80.9

81.94

81.68

84.52

71.89

1000

87.1

80.9

83.87

84.06

84.52

71.89

0.26

0.45

0.61

0.17

0.32

0.61

0.15

0.32

0.29

0.21

0.33

0.59

0.14

0.32

0.71

0.15

0.32

0.29

0.15

C

34

9

10

28

6

28

32

6

32

35

8

8

13

7

26

35

15

34

32

8

34

γ

0.94

1

0.94

0.01

0.01

0.01

0.01

0.01

0.01

0.01

0.01

0.01

0.02

0.01

0.02

0.01

0.01

0.01

0.01

0.01

0.01

C1 C2

Sens

Spec

ROC area F-M BA

Y

1

5

7

4

9

1

3

9

1

3

5

1

3

10

1

3

11

1

3

5

1

2

17

0.444

0.876

0.66

0.5

0.66

0.63

0.72

0.675

0.52

0.675

27.73

0.32

0.35

1

3

2

1

2

2

1

2

1

3

2

2

1

2

2

1

2

1

1

0

1

0.5

0.688

0.919

0.803

0.813

0.837

0.825

0.5

0.919

0.709

0.719

0.911

0.815

0

0.69

0.67

0.55

0.7

0.5

0

0.803

0.607

0.4

0.825

0.65

0.709

0.419

0.815

0.58

0.63

0.65

0.813

0.837

0.825

0.67

0.825

0.563

0.919

0.741

0.719

0.911

0.815

0.6

0.7

0.741

0.482

0.815

0.63

1.9

0.844

0.837

0.841

0.68

0.840

0.681

0

1

0.5

0

0.5

0

0.719

0.902

0.811

0.844

0.829

0.837

0.594

0.927

0.76

0.719

0.911

0.815

0.69

0.68

0.63

0.7

0.810

0.621

0.74

0.836

0.673

0.760

0.521

0.815

0.63

1.1

0.813

0.821

0.817

0.65

0.817

0.634

0.563

0.919

0.741

0.719

0.911

0.815

0.6

0.7

0.741

0.482

0.815

0.63

4.03

0.844

0.837

0.841

0.68

0.840

0.681

0.563

0.919

0.741

0.6

0.741

0.482

Table 8 Algorithm 2: Experimental results on the datasets Pima, WDBC, and WPBC

Dataset Gen. param.

Fitness functions

Optimized Hyper-par

Performance metrics

Time

Pop size Gen

f1

f2

f3

Pima

24

100

77.73

73.2

74.35

76.28

77.08

70.34

77.47

70.26

200

77.99

70.9

74.35

76.28

74.74

58.03

1000

77.47

70.89

77.47

70.1

74.48

76.33

48

100

78.13

71.13

74.35

76.28

200

78.13

71.13

75.13

75.44

74.35

76.22

1000

78.13

71.13

78.13

72.34

1.02

0.68

0.23

0.23

0.44

0.68

0.28

0.45

0.23

0.68

0.22

0.68

0.22

0.33

0.68

0.22

2.11

74.22

75.93

0.7

C

5

5

23

23

4

5

5

48

12

48

3

3

3

10

2

3

1

3

γ

0.24

0.53

0.32

0.24

0.53

0.53

0.53

0.24

0.24

0.13

0.63

0.58

0.63

0.42

0.63

0.63

0.63

0.42

C1 C2

Sens

Spec

ROC area F-M BA

Y

5

5

1

1

2

5

1

2

1

5

1

5

1

2

5

1

10

5

4

2

1

1

2

2

2

2

1

2

1

2

1

1

2

1

9

2

0.623

0.843

0.86

0.69

0.742

0.767

0.56

0.884

0.722

0.552

0.894

0.723

0.56

0.898

0.729

0.843

0.351

0.69

0.96

0.767

0.655

0.567

0.886

0.727

0.549

0.896

0.722

0.84

0.694

0.767

0.66

0.741

0.483

7.8

0.7

0.63

0.63

0.64

0.7

0.49

0.64

0.63

0.7

0.766

0.533

0.722

0.444

0.723

0.446

0.729

0.458

12.41

0.766

0.533

0.655

0.311

0.726

0.453

52.83

0.722

0.445

0.767

0.534

0.563

0.898

0.731

0.64

0.730

0.461

9.86

0.843

0.69

0.767

0.563

0.898

0.731

0.765

0.744

0.754

0.84

0.692

0.766

0.563

0.898

0.731

0.593

0.882

0.738

0.828

0.696

0.762

0.7

0.64

0.68

0.7

0.64

0.65

0.69

0.766

0.533

0.730

0.461

15.34

0.754

0.509

0.766

0.532

0.730

0.461

62.73

0.737

0.475

0.762

0.524

123

---

<!-- PAGE 17 -->

A hyper-parameter tuning approach...

Table 8 continued

Dataset Gen. param.

Fitness functions

Optimized Hyper-par

Performance metrics

12879

Time

Pop size Gen

f1

f2

f3

WDBC 24

100

97.42

97.73

97.14

97.7

200

97.42

97.73

97.28

97.43

97.14

97.7

1000

97.42

97.73

97.14

97.7

48

100

97.42

97.73

97.28

97.43

97.14

97.7

200

97.42

97.73

97.28

97.43

97.14

97.7

1000

97.42

97.73

97.14

97.13

WPBC 24

100

76.26

0

69.19

60.78

200

77.27

48.83

65.15

62.29

76.26

0

1000

77.27

48.83

65.15

62.29

76.26

48

100

76.26

0

0

76.26

55.17

200

77.78

29.08

77.78

25.26

67.17

60.71

1000

76.26

0

65.15

59.59

0.09

0.04

0.09

0.04

0.04

0.09

0.03

0.09

0.04

0.04

0.09

0.04

0.04

0.16

0.03

0.24

0.55

3.36

2.95

0.24

3.36

2.95

0.24

0.24

0.39

0.25

0.22

3.04

0.24

3.25

C

19

4

19

4

4

14

14

19

4

4

19

4

4

16

4

49

1

9

5

42

9

5

5

41

14

49

48

47

28

37

γ

0.24

0.18

0.24

0.01

0.18

0.24

0.24

0.24

0.01

0.18

0.24

0.01

0.18

0.27

0.27

0.01

0.18

0.01

0.01

0.01

0.01

0.01

0.01

0.09

0.09

0.27

0.27

0.01

0.01

0.01

C1 C2

Sens

Spec

ROC area F-M BA

Y

3

1

3

1

1

3

1

3

1

1

3

1

1

5

1

1

3

17

17

1

17

17

1

1

2

1

1

17

1

18

7

7

7

3

7

7

4

7

3

7

7

3

7

12

1

1

1

7

5

7

7

5

9

2

1

6

7

5

7

5

0.988

0.967

0.977

0.996

0.959

0.977

0.988

0.967

0.977

0.979

0.969

0.974

0.996

0.959

0.977

0.988

0.967

0.977

0.996

0.959

0.977

0.988

0.967

0.977

0.979

0.969

0.974

0.996

0.959

0.977

0.988

0.967

0.977

0.979

0.969

0.974

0.996

0.959

0.977

0.988

0.967

0.977

0.971

0.972

0.971

0

1

0.5

0.489

0.755

0.622

0.255

0.934

0.595

0.574

0.675

0.625

0

1

0.5

0.255

0.934

0.595

0.574

0.675

0.625

0

0

1

1

0.5

0.5

0.34

0.894

0.617

0.085

0.993

0.539

0.064

1

0.532

0.511

0.722

0.616

0

1

0.5

0.96

0.96

0.96

0.96

0.96

0.96

0.96

0.96

0.96

0.96

0.96

0.96

0.96

0.96

0.96

0

0.43

0.35

0.44

0

0.35

0.44

0

0

0.41

0.15

0.12

0.42

0

0.977

0.955

0.87

0.977

0.955

0.977

0.955

2.59

0.974

0.948

0.977

0.955

0.977

0.955

13.77

0.977

0.955

0.977

0.955

2.52

0.974

0.948

0.977

0.955

0.977

0.955

5.37

0.974

0.948

0.977

0.955

0.977

0.955

25.72

0.971

0.943

0.5

0

0.96

0.622

0.244

0.594

0.189

1.61

0.624

0.249

0.5

0

0.594

0.189

4.47

0.624

0.249

0.5

0.5

0

0

1.77

0.617

0.234

0.539

0.078

2.64

0.532

0.064

0.616

0.233

0.5

0

8.55

0.511

0.695

0.603

0.41

0.603

0.206

7 Conclusion

Support vector machines are one of the best ML models for
solving several real-life classiﬁcation problems. However, as
in other ML techniques, their performance depends on hyper-
parameters.

In this paper, we have investigated and proposed an
approach that combines genetic algorithms and decision trees
to optimize hyper-parameters of C-SVMs. The optimum val-
ues of the regularization parameter, costs of classes and the
parameters of the RBF kernel function are searched for SVM.
We tested the algorithm on six benchmark datasets, which
are imbalanced. We evaluated the performance of the mod-
els by several performance metrics. The framework is better

or equivalent to other algorithms proposed in the literature
for CS-SVM hyper-parameters optimization. Overall, taking
into account three predictive metrics, i.e., accuracy, G-Mean,
and average cost, the best hyper-parameter conﬁguration is
found in short computational time, mainly if compared with
grid search approach. Hence, this approach can be considered
as a good solution for addressing imbalanced dataset classi-
ﬁcation and hyper-parameter tuning, as they are challenging
problems in classiﬁcation research.

We suggest evaluating the performance of classiﬁers on
medical data by suitable measures other than accuracy. Our
future work is to extend and assess the proposed approach
to investigate hyper-parameter tuning of different machine
learning methods.

123

---

<!-- PAGE 18 -->

12880

R. Guido et al.

Fig. 6 Values of the six performance measures of the Pareto points found for Appendicitis, Haberman, Hepatitis, and Pima datasets

Fig. 7 Values of the six performance measures of the Pareto points found for WDBC and WPBC datasets

Acknowledgements The research has been partially supported by the
research project SI.F.I.PA.CRO.DE. Sviluppo e industrializzazione far-
maci innovativi per terapia molecolare personalizzata PA.CRO.DE.
(PON A R S01_00568, CUP: B29C20000360005, CONCESSIONE
RNA-COR: 4646672), Italian Ministry of University and Research,
2021.

Declaration

Conﬂict of interest The authors of the manuscript declare that they have
no afﬁliations with or involvement in any organization or entity with
any ﬁnancial interest (such as honoraria; educational grants; partici-
pation in speakers’ bureaus; membership, employment, consultancies,
stock ownership, or other equity interest; and expert testimony or patent-
licensing arrangements), or non-ﬁnancial interest (such as personal or

professional relationships, afﬁliations, knowledge or beliefs) in the sub-
ject matter or materials discussed in this manuscript.

Open Access This article is licensed under a Creative Commons
Attribution 4.0 International License, which permits use, sharing, adap-
tation, distribution and reproduction in any medium or format, as
long as you give appropriate credit to the original author(s) and the
source, provide a link to the Creative Commons licence, and indi-
cate if changes were made. The images or other third party material
in this article are included in the article’s Creative Commons licence,
unless indicated otherwise in a credit line to the material. If material
is not included in the article’s Creative Commons licence and your
intended use is not permitted by statutory regulation or exceeds the
permitted use, you will need to obtain permission directly from the copy-
right holder. To view a copy of this licence, visit http://creativecomm
ons.org/licenses/by/4.0/.

123

---

<!-- PAGE 19 -->

A hyper-parameter tuning approach...

References

Agrawal N, Kumar A, Bajaj V (2017) A new design method for stable
IIR ﬁlters with nearly linear-phase response based on fractional
derivative and swarm intelligence. IEEE Transactions on Emerging
Topics in Computational Intelligence 1(6):464–477

Agrawal N, Kumar A, Bajaj V (2018) Design of digital IIR ﬁlter with
low quantization error using hybrid optimization technique. Soft
Comput 22(9):2953–2971

Amin A, Anwar S, Aea Adnan (2016) Comparing oversampling tech-
niques to handle the class imbalance problem: a customer churn
prediction case study. IEEE Access 4:7940–7957

Bao-De L, Xin-Yang Z, Mei Z et al (2021) Improved genetic algorithm-
based research on optimization of least square support vec-
tor machines: an application of load forecasting. Soft Comput
10(1007):5674–9

Bergstra J, Bardenet R, Bengio Y, et al (2011) Algorithms for hyper-
parameter optimization. In: and CAI (ed) Proceedings of the 24th
international conference on neural information processing sys-
tems. USA, pp 2546–2554

Breiman L, Friedman JH, Olshen R, et al (1984) R. A. and Stone, C.J.

Classiﬁcation and regression trees. CRC press

Chawla N, Bowyer K, Lea Hall (2002) Smote: Synthetic minority over-

sampling technique. J Artif Intell Res 16:321–357

Cortes C, Vapnik V (1995) Support-vector network. Mach Learn

20:273–297

Cristianini N, Shawe-Taylor J (2000) An Introduction to Support Vector
Machines and other kernel-based learning methods. Cambridge
University Press

Datta S, Das S (2015) Near-bayesian support vector machines for imbal-
anced data classiﬁcation with equal or unequal misclassiﬁcation
costs. Neural Netw 70:39–52

Deb K, Goel T (2001) Controlled elitist non-dominated sorting genetic
algorithms for better convergence. In: Lothar T, Kalyanmoy D,
Coello C et al (eds) Zitzler Eckart. Evolutionary Multi-Criterion
Optimization, Springer, Berlin Heidelberg, pp 67–81

Deb K, Pratap A, Agarwal S et al (2002) A fast and elitist multiobjective
genetic algorithm: NSGA-II. IEEE Trans Evol Comput 6:182–197
Dwivedi AK, Ghosh S, Londhe ND (2018) Review and analysis of
evolutionary optimization-based techniques for ﬁr ﬁlter design.
Circuits Syst Signal Process 37(10):4409–4430

Galar M, Fernandez A, Barrenechea E et al (2012) A review on ensem-
bles for the class imbalance problem: Bagging, boosting, and
hybrid-based approaches, systems, man, and cybernetics, part c:
Applications and reviews. IEEE Trans 42(4):463–484

Goldberg DE, Holland J (1988) Genetic algorithms and machine learn-

ing. Mach Learn 3(2):95–99

Guido R, Conforti D (2017) Hybrid genetic approach for solving an
integrated multi-objective operating room planning and scheduling
problem. Comput Oper Res 87:270–282

Guido R, Groccia MC, Conforti D (2021) Hyper-Parameter Optimiza-
tion in Support Vector Machine on unbalanced datasets using
Genetic Algorithms. In: Optimization in Artiﬁcial Intelligence and
Data Sciences, AIRO Springer Series (in press)

Hofmann T, Scholkopf B, Smola AJ (2008) Kernel methods in machine

learning. Ann Statist pp 1171–1220

Holland JH (1975) Adaptation in natural and artiﬁcial systems: An
introductory analysis with applications to biology, control, and
artiﬁcial intelligence. Michigan Press

Iranmehr A, Masnadi-Shirazi H, Vasconcelos N (2019) Cost-sensitive

support vector machines. Neurocomputing 343:50–64

Japkowicz N, Stephen S (2002) The class imbalance problem: a sys-

tematic study. Intell Data Anal 6:429–449

Jo T, Japkowicz N (2004) Class imbalances versus small disjuncts. ACM

SIGKDD Explorations Newslett 6:40–49

12881

Lessmann S, Stahlbock R, Crone R (2005) Optimizing hyperparameters
of support vector machines by genetic algorithms. In: IC-AI pp
74–82

Mehrbakhsh N, Hossein A, Leila S et al (2019) A predictive method for
hepatitis disease diagnosis using ensembles of neuro-fuzzy tech-
nique. J Infect Public Health 12(1):13–20

Noia A, Martino A, Montanari P et al (2020) Supervised machine learn-
ing techniques and genetic optimization for occupational diseases
risk prediction. Soft Comput 24:4393–4406

Phienthrakul T, Kijsirikul B (2010) Evolutionary strategies for hyper-
parameters of support vector machines based on multi-scale radial
basis function kernels. Soft Comput 14:681–699

Qi Z, Tiana Y, Shia Y et al (2013) Cost-sensitive support vector machine
for semi-supervised learning. Procedia Comput Sci 18:1684–1689
Ramírez A, Romero JR, Ventura S (2015) An extensible JCLEC-based
solution for the implementation of multi-objective evolutionary
algorithms. In: proceedings of the companion publication of the
2015 annual conference on genetic and evolutionary computation,
pp 1085–1092

Ramírez A, Romero JR, García-Martínez C et al (2019) JCLEC-MO:
a java suite for solving many-objective optimization engineering
problems. Eng Appl Artif Intell 81:14–28

Scholkopf B, Smola AJ (2001) Learning with Kernels: Support Vector
Machines, Regularization, Optimization, and Beyond. MIT Press,
Cambridge, MA, USA

Sokolova M, Japkowicz N, Szpakowicz S (2006) Beyond accuracy,
F-score and ROC: A family of discriminant measures for per-
formance evaluation. In: Sattar A, Kang B (eds) Advances in
Artiﬁcial Intelligence. Lecture Notes in Computer Science, vol
4304. Springer, Berlin, Heidelberg

Srinivas N, Deb K (1994) Multiobjective optimization using nondomi-

nated sorting in genetic algorithms. Evol Comput 2(3):221–248

Tao X, Li Q, Guo W et al (2019) Self-adaptive cost weights-based
support vector machine cost-sensitive ensemble for imbalanced
data classiﬁcation. Inf Sci 487:31–56

Turney PD (1995) Cost-sensitive classiﬁcation: empirical evaluation of
a hybrid genetic decision tree induction algorithm. J Artif Int Res
2:369–409

Vapnik V (1998) Statistical Learning Theory. Wiley, John Sons Inc
Veropoulos K, Campbell C, Cristianini N (1999) Controlling the
sensitivity of support vector machines. In: proceedings of the inter-
national joint conference on AL, pp 55–60

Witten I, Frank E (2005) Data Mining Practical Machine Learning Tools

and Techniques. Morgan Kaufmann Publishers, CA

Yu X, Wang X (2017) A novel hybrid classiﬁcation framework using
svm and differential evolution. Soft Comput 21:4029–4044

Publisher’s Note Springer Nature remains neutral with regard to juris-
dictional claims in published maps and institutional afﬁliations.

123

<!-- MARKITDOWN CONVERSION -->

<!-- Full MarkItDown conversion for formatting fidelity. -->

SoftComputing(2023)27:12863–12881
https://doi.org/10.1007/s00500-022-06768-8
FOCUS
A hyper-parameter tuning approach for cost-sensitive support vector
machine classifiers
Rosita Guido1 ·Maria Carmela Groccia1·Domenico Conforti1
Accepted:10January2022/Publishedonline:2February2022
©TheAuthor(s)2022
Abstract
Inmachinelearning,hyperparametertuningisstronglyusefultoimprovemodelperformance.Inourresearch,weconcentrate
ourattentiononclassifyingimbalanceddatabycost-sensitivesupportvectormachines.Weproposeamulti-objectiveapproach
that optimizes model’s hyper-parameters. The approach is devised for imbalanced data. Three SVM model’s performance
measuresareoptimized.Wepresentthealgorithminabasicversionbasedongeneticalgorithms,andasanimprovedversion
based on genetic algorithms combined with decision trees. We tested the basic and the improved approach on benchmark
datasetseitherasserialandparallelversion.Theimprovedversionstronglyreducesthecomputationaltimeneededforfinding
optimizedhyper-parameters.Theresultsempiricallyshowthatsuitableevaluationmeasuresshouldbeusedinassessingthe
classificationperformanceofclassificationmodelswithimbalanceddata.
Keywords Multi-objectiveoptimization·Supportvectormachine·Hyper-parameteroptimization·Imbalanceddatasets·
Geneticalgorithms
1 Introduction can significantly affect the resulting model’s performance.
Generally,hyper-parametersareadjustedforeachmodelin
Classification problems may be encountered in different order to find a hyper-parameter setting that maximizes the
domains.Oneoftheseisthediseasediagnosis,whichestab- model performances and so that the ML model can predict
lishesthepresenceorabsenceofagivendiseaseaccording unknowndataaccurately.Thegoalofhyper-parameteropti-
toreferredsymptomsandresultsofmedicalexams.Machine mizationistofindasetofvaluesthatminimizesapredefined
learning approaches can be employed to support experts in lossfunction.
diseases diagnosis. Many researches aim to propose new Usually, a good set of hyper-parameters are determined
methods to improve or enhance the outcomes of existing by a grid search. The grid search strategy is based on
ones. testingallhyper-parametercombinationsspecifiedinamulti-
Support vector machines (SVM) are one of the best dimensional grid. During the search, the hyper-parameters
machine learning (ML) models for solving several real-life arevaried,withfixedstep-size,inagivenrangeofvalues.The
classificationproblems(Vapnik1998;CristianiniandShawe- performanceofacombinationofhyperparametersisevalu-
Taylor2000).Thechoiceofhyper-parametersofaMLmodel atedusingaperformancemetric.Theconfigurationwiththe
bestperformanceisselectedandusedtotraintheMLmodel
CommunicatedbyDarioPacciarelli. on the whole dataset. However, this kind of search is very
B timeconsuminganditissuitablefortheadjustmentoffew
RositaGuido
hyper-parameters.
rosita.guido@unical.it
Another big challenge in data mining that is attracting
MariaCarmelaGroccia
increasing interest of researchers is dealing with imbal-
mariacarmela.groccia@unical.it
anceddatasets(JapkowiczandStephen2002).Adatasetis
DomenicoConforti
imbalancedwhenoneormoreclasseshaveverylowpropor-
domenico.conforti@unical.it
tions in the data as compared to the other classes. The first
1 DepartmentofMechanical,EnergyandManagement class is called as minority class with respect to the major-
Engineering,UniversityofCalabria,PontePietroBucci, ity class(ess). The main interest is in correctly classifying
87036Rende,Cosenza,Italy
123

12864 R.Guidoetal.
theminorityclass.Theexistingmethodsforclassificationof tormachinesanddecisiontreesinSect.3,anddiscusssome
imbalanceddatacanbecategorizedasalgorithm-levelcate- metrics commonly used to evaluate model performance. In
gory,data-levelcategory,andcost-sensitivemethodsthatlie Sect. 4, we introduce multi-objective optimization prob-
between the above two categories (Galar et al. 2012). The lems and the Non-dominated Sorting Genetic Algorithm-II
firstcategoryincludesmethodsmodifiedordesignedtohan- (NSGA-II). In Sect. 5, we detail our approach that com-
dleimbalanceddata;thesecondcategoryincludesmethods bines genetic algorithms and a heuristic procedure based
that try to transform data in order to balance classes and on decision tree in order to find optimal hyper-parameters.
usethenstandardclassificationalgorithms.Down-sampling Threeobjectivefunctionsareoptimized.Weperformseveral
approaches,whichreducethemajorityclassinthetraining computationalexperimentsaimedatfindingthebesthyper-
subset, and over-sampling approaches, which increase the parametertuningforsixbenchmarkdatasets.Thebestresults
size of the minority class in the training subset, belong to alongwithadiscussionandcomparisonwithotherresultsof
this category. Finally, the third category includes methods theliteraturearereportedinSect.6.Finally,theconclusions
designedforweightingdifferentlytheclassesbyintroducing aregiveninSect.7.
misclassificationcosts.
Itisimportanttopointoutthatthemostcommonlyused
modelevaluationmetricistheaccuracy.However,itcanbe 2 Relatedworkonimbalanceddata
verymisleadingwhendataareimbalanced.Insuchcases,dif- classificationandcost-sensitivelearning
ferentevaluationmetricsshouldbeconsidered.Wetestedin problems
(Guidoetal.2021)twoevaluationmodelmetrics,i.e.,accu-
racy and G-Mean, on two imbalanced benchmark datasets LetD ={(x ,y ),(x ,y ),...,(x ,y)},beadatasetwhere
1 1 2 2 l l
byoptimizinghyper-parametersofsupportvectormachines x ∈ (cid:3)L is a pattern (even called example) drawn from a
i
by genetic algorithms (GAs). Comparing the results, we domainX andy ∈Y isitsrelatedclasslabel.Anexampleis
i
observedempiricallythatG-Meanismoresuitablethanaccu- thusavector.Inabinaryclassificationdomain,anexample
racy to evaluate model performance in case of imbalanced canbeeitherpositive,denotedbyalabely =1,ornegative,
data, especially when data refers to medical domains, like denotedbyy =−1.Generally,thegoalofabinaryclassifier
diagnosis. The results encouraged us to continue exploring is to map feature vectors x ∈ X to class labels y ∈ {±1}.
thisresearchfield. In terms of functions, a classifier can be written as h(x) =
This research paper addresses the optimal hyper- sign[p(x)],wherethefunction p : X → Risdenotedasthe
parameters problem as a multi-objective problem. It has a classifierpredictor.
twofoldcontribution: Classifiers generally perform poorly on imbalanced
datasets and, as a consequence, often they classify almost
1. The main goal is to investigate methods for improving all instances as negative. In recent years, imbalanced data
hyper-parameter tuning of SVM. We propose a novel classificationhasbeenstudiedbymanyresearcherswithdif-
approach for optimal hyper-parameter tuning that con- ferentmethods(JoandJapkowicz2004;Galaretal.2012).
sists of a genetic algorithm combined with a decision These methods can be distinguished into two categories
tree.Thebasicideaisthatsomechromosomesaresimilar basedondataandalgorithms.Data-basedmethodsfocuson
among them and they have thus the same fitness value. datapre-processingtoreduceimbalanceddata.Forinstance,
A decision tree (DT), trained in a suitable manner, is up-samplingandunder-samplingaretwomethodsthatmod-
exploitedtoreducethenumberofk-foldcross-validation ifyinstancedistribution.Up-samplingmethodsincreasethe
tobeperformedandthustheoverallcomputationaltime. minoritysamples,whereasunder-samplingmethodsreduce
As we will see, GAs were chosen even because they the majority samples. Synthetic Minority Oversampling
allowforaneasyparallelizationoftheproblem,whichis Techniqueisanoversamplingmethodthatbalancesdataby
tremendouslyhelpful.TheapproachthatcombinesGAs generatingnewsamplessimilartotheminoritysamplesand
andDTstronglyreducestheoverallcomputationaltime, theirneighbors(Chawlaetal.2002).
asdescribedinSect. 5. Hereafter,apositiveinstancebelongstotheminorityclass,
2. It focuses on testing and optimizing, at the same time, whereas a negative instance to the majority class. In many
more suitable performance measures in addition to the real-world applications, misclassifications may have differ-
accuracy. This is important for application domains entcosts,suchasforinstancediseasediagnosisandbusiness
whereonedataclassisofmoreinterestthanothers. decision making. The related classification problem, called
cost-sensitivelearningproblem,aimsatminimizingthetotal
Thepaperisstructuredasfollows.Ashortreviewofthe misclassificationcosts.Theissueofclassifyingimbalanced
state-of-the-artoftheliteraturefocusingonimbalanceddata databyanSVMwasaddressedin(Veropoulosetal.1999)by
setsisinSect. 2.Wegiveashortdescriptionofsupportvec- abiased-SVM.Thismethodusestwopenaltycoefficientsfor
123

Ahyper-parametertuningapproach... 12865
misclassifiedpositiveinstancesandnegativeinstances.Since ing kernel allows better discrimination in the feature space
the positive instances usually belong to the minority class, thanthatofasingleRBFkernel.
theusedpenaltycoefficientforthisclassisbiggerthanthe Oneofthefirstresearchpapersoncost-sensitiveapproach
penaltycoefficientassociatedwiththemajorityclass.Inthis tackledwithanevolutionaryprocessisduetoTurney(1995).
way, the SVM classifier aims at reducing misclassification Recently,Noiaetal.(2020)appliedSVM,k-NearestNeigh-
rateoftheminorityclass. bors and k-means as clustering techniques to predict the
The performance of an SVM model even depends, for probabilityofcontractingagivendiseasestartingfromboth
instance,ontheusedkernelfunction,whichmapsinstances- workplace-related(usingAtecoandIstatcodes)andworker-
vectorsfromtheoriginalinputspacetohigherdimensional related characteristics (i.e., age at hiring, age at disease
spacestodealwithnonlinearlyseparabledata(Scholkopfand certification,gender,employmentduration).TheyusedaGA
Smola2001).Accordingly,twoparametersofSVM,i.e.,C to find the best values of the used methods. Misclassifica-
andthekernelparameterwerefoundbyanexhaustivesearch tionerrorrateisusedasfitnessfunction.However,sincethe
approachin(Mehrbakhshetal.2019).Iranmehretal.(2019) classeswerenotevenlydistributedamongtheinstances,they
extended the SVM with cost-sensitive learning consider- usedasecondfitnessfunctionthatreducesthemisclassifica-
ingexampledependentcosts.Theyperformedexperimental tionerrorrateoftheminorityclass.
analysis on class imbalance, cost-sensitive learning with Anexhaustive searchofpapers addressingevaluation of
a given class and example costs and showed that their ML algorithms on classification is due to Sokolova et al.
proposedalgorithmprovidessuperiorgeneralizationperfor- (2006). These authors showed that the clear “leaders” are
mance compared to conventional methods. Qi et al. (2013) thosepapersinwhichevaluationisperformedondatafrom
proposedanewCost-SensitiveLaplacianSVMandtestedits the UCI repository, in biomedical and medical sciences,
effectivenessviaexperimentsonpublicdatasets.Theyeval- visual and text classification, and language applications.
uate the algorithms performance by the Average Cost. Tao Themostusedevaluationmeasuresareaccuracy,precision,
et al. (2019) developed a novel self-adaptive cost weights- recall, F-score, and the Receiver Operating Characteristic
| basedSVMcost-sensitiveensembleforimbalanceddatasets |        |     |          |            |              | (ROC). |     |     |     |
| --------------------------------------------------- | ------ | --- | -------- | ---------- | ------------ | ------ | --- | --- | --- |
| classification                                      | tasks. | The | approach | was tested | on synthetic |        |     |     |     |
datasetsandonpublicdatasetsshowinghigherclassification
3 Learningmodelclassifiers
| accuracy | than | the other | existing | imbalanced | classification |     |     |     |     |
| -------- | ---- | --------- | -------- | ---------- | -------------- | --- | --- | --- | --- |
methodsintermsofG-MeanandF-Measure.
Weoptimizehyper-parametersofSVMclassifierswithGaus-
Evolutionaryalgorithmsareflexibleandcommonlyused
siankernelinordertocorrectlycompareourresultsfoundon
| for a plethora |     | of machine | learning | problems | and tasks |     |     |     |     |
| -------------- | --- | ---------- | -------- | -------- | --------- | --- | --- | --- | --- |
publicandwell-knowndatasetswiththosereportedinthelit-
| (Bergstra | et al. | 2011; Goldberg | and | Holland | 1988). Evolu- |     |     |     |     |
| --------- | ------ | -------------- | --- | ------- | ------------- | --- | --- | --- | --- |
erature.Ourapproach,asitisbetterdetailedinSect.5,trains
tionaryoptimization-basedtechniquessolvethefilterdesign
|         |                 |     |          |      |                   | and uses random | trees to reduce | the | overall computational |
| ------- | --------------- | --- | -------- | ---- | ----------------- | --------------- | --------------- | --- | --------------------- |
| task as | an optimization |     | problem. | They | are used success- |                 |                 |     |                       |
time.
| fully in  | different | real-world | optimization |     | problems related |                  |            |           |                  |
| --------- | --------- | ---------- | ------------ | --- | ---------------- | ---------------- | ---------- | --------- | ---------------- |
|           |           |            |              |     |                  | In this section, | we briefly | introduce | SVM and decision |
| to Finite | Impulse   | Response   | (FIR)        | and | Infinite Impulse |                  |            |           |                  |
trees.Thus,wereportthemostusedperformancemetricsofa
Response(IIR)digitalfiltersdesign.Thegoalistominimize
MLmodelanddiscusstheirsuitabilityincaseofimbalanced
anerrorfunctionthatquantifiesdeviationbetweenafilterand
datasets.
adesiredresponse.Thiserrorisreducedbyupdatingitera-
tivelyasetoffiltercoefficientssuchthatgivenspecifications 3.1 Supportvectormachine
| are met. | Dwivedi | et al. | (2018) provided |     | a comprehensive |     |     |     |     |
| -------- | ------- | ------ | --------------- | --- | --------------- | --- | --- | --- | --- |
reviewofthevariousevolutionaryoptimization-basedtech- TheSVMwasintroducedbyCortesandVapnik(1995)and
niquesforFIRfilterdesign.ApproachestodesignIIRfilters isbasedonstatisticallearningtheory(Vapnik1998).SVMs
basedonevolutionarytechniqueswereproposedin(Agrawal are a class of algorithms for classification, regression and
et al. 2018, 2017). Evolutionary algorithms are even used otherapplications(CristianiniandShawe-Taylor2000)and
to automatically tune several parameters. Lessmann et al. theyareamongthemostusedMLtechniques.
|     |     |     |     |     |     |     |     |     | = (x ,...,x ), |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | -------------- |
(2005)usedaGAinordertotuneSVMs.Phienthrakuland Let X, be a dataset with L instances X 1 L
Kijsirikul(2010)improvedtheaccuracyofSVMbyanon- where x ∈ (cid:3)m, denotes an instance with m features, and
i
|                                                   |     |     |     |     |     | ∈ {±1}itslabel,i | = 1,...,L.Inabinaryclassification |     |     |
| ------------------------------------------------- | --- | --- | --- | --- | --- | ---------------- | --------------------------------- | --- | --- |
| linearcombinationofmultipleRBFkernelstoobtainmore |     |     |     |     |     | y i              |                                   |     |     |
flexible kernel functions. The hyperparameters are chosen problem, an SVM basically searches for an optimal hyper-
byanevolutionarystrategywheretheobjectivefunctionsare planethatseparatespatternsofthetwoclassesbymaximizing
basedontrainingaccuracy,boundingofgeneralizationerror, themarginw ∈(cid:3)m.Findingtheoptimalhyperplanemeans
andsubsetcross-validationontrainingaccuracy.Theresult- solvingthequadraticprogrammingmodel(1)-(3),whichis
knownassoft-marginSVM
123

| 12866        |          |     |     |     |     |      |          |     |          | R.Guidoetal. |     |
| ------------ | -------- | --- | --- | --- | --- | ---- | -------- | --- | -------- | ------------ | --- |
|              | (cid:2)L |     |     |     |     | (wTx | +b)≥1−ξ  |     | =1,...,L |              |     |
| 1            |          |     |     |     |     | y i  |          |     | i i      |              | (5) |
| min ||w||2+C |          | ξ   |     | (1) |     |      |          |     |          |              |     |
|              |          | i   |     |     |     | ξ ≥0 | =1,...,L |     |          |              |     |
| 2            |          |     |     |     |     | i    | i        |     |          |              | (6) |
1
| (wTφ(x )+b)−1+ξ |     | ≥0  | =1,...,L |     |     |     |     |     |     |     |     |
| --------------- | --- | --- | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
| y i i           |     | i   | i        | (2) |     |     |     |     |     |     |     |
Observethatthecostmatriceshasthediagonalelements
ξ ≥0 =1,...,L
| i i |     |     |     | (3) |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
aszero—becauseoftheassumptionthatacorrectclassifica-
tionhasnocost—andtheoff-diagonalelementsarepositive
| where C, named | penalty | parameter, | is a trade-off | between |          |          |     |       |                  |     |        |
| -------------- | ------- | ---------- | -------------- | ------- | -------- | -------- | --- | ----- | ---------------- | --- | ------ |
|                |         |            |                |         | numbers. | However, | the | range | of possibilities | for | CS-SVM |
thesizeofthemarginofseparationwandthetrainingerrors
hyper-parametercanbehuge.
ξ;b isthebiasanditindicatestheoffsetofthehyperplane
|     |     |     |     |     | Datta | and | Das (2015) | proposes | a Near-Bayesian |     | Sup- |
| --- | --- | --- | --- | --- | ----- | --- | ---------- | -------- | --------------- | --- | ---- |
from the origin. Constraints (2) state that when a training portVectorMachine(NBSVM)forimbalancedclassification
| example x | lies on the | wrong side | of the hyperplane, | the |                                                    |     |     |     |     |     |     |
| --------- | ----------- | ---------- | ------------------ | --- | -------------------------------------------------- | --- | --- | --- | --- | --- | --- |
| i         |             |            |                    |     | problemsbycombiningdecisionboundaryshiftandunequal |     |     |     |     |     |     |
correspondingslackvariableξ
i isgreaterthan1.Smallvalues regularization costs. Extensive comparison with standard
ofCincreasethetrainingerrors,whereaslargervaluesbring
|     |     |     |     |     | SVM | and some | state-of-the-art |     | methods | is furnished | as a |
| --- | --- | --- | --- | --- | --- | -------- | ---------------- | --- | ------- | ------------ | ---- |
it closer to the hard-margin SVM. In case of nonlinearly proofoftheabilityoftheNBSVMtoperformcompetitively
| separable datasets, | the | SVM basically | maps | input vectors |     |     |     |     |     |     |     |
| ------------------- | --- | ------------- | ---- | ------------- | --- | --- | --- | --- | --- | --- | --- |
onimbalanceddatasets.
intohigh-dimensionalfeaturespacesbytheso-calledkernel
functions(Hofm(cid:3)annetal.200(cid:4)8).Akernelfunction,denoted
3.2 Decisiontree
| asK(x ,x )= | φ(x | ),φ(x ),isaninnerproductinafeature |     |     |     |     |     |     |     |     |     |
| ----------- | --- | ---------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| i j         | i   | j                                  |     |     |     |     |     |     |     |     |     |
spacewhereitmeasuressimilaritybetweenanypairofinputs
Adecisiontreeisasupervisedlearningalgorithmforregres-
x i and x j .Akernelfunctioncantakemanydifferentforms
sionandclassificationproblems(Breimanetal.1984)andis
(Hofmannetal.2008),suchas
themostpopularformofrule-basedclassifiers(Wittenand
Frank2005).Ithasasetofelementscallednodesandisbuilt
| •   | K(x | ,x )=(xTx | )d  |     |     |     |     |     |     |     |     |
| --- | --- | --------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Linearkernel i j j top-down from a root node. Each node represents a single
i
| • Polynomialkernel |     | K(x ,x )=(xTx | +a)d |     |     |     |     |     |     |     |     |
| ------------------ | --- | ------------- | ---- | --- | --- | --- | --- | --- | --- | --- | --- |
i j i j inputattribute:leafnodescontainanoutputattribute,which
| •   |     |     | K(x | ,x ) = |     |     |     |     |     |     |     |
| --- | --- | --- | --- | ------ | --- | --- | --- | --- | --- | --- | --- |
Radial Basis Function (RBF) kernel i j isusedtomakeaprediction;theothernodesaresplitpoints
| exp(−γ(cid:6)x | −x  | (cid:6)2) |     |     |                                                       |            |                   |     |              |         |       |
| -------------- | --- | --------- | --- | --- | ----------------------------------------------------- | ---------- | ----------------- | --- | ------------ | ------- | ----- |
|                | i j |           |     |     | ofanattribute.Thedataispartitionedintohomogeneoussub- |            |                   |     |              |         |       |
|                |     |           |     |     | sets,                                                 | i.e., they | contain instances |     | with similar | values. | Given |
The decision function, i.e., the classifier, is specified by a a new input, the tree is traversed by evaluating the specific
subset of training instances, the so-called support vectors, inputstartedattherootnodeofthetree.
thataretheonlyvectorsthat“support”theoptimalseparating
hyperplane.
3.3 Performanceevaluationandsomelimitations
| It is well | known that | the performance | of most | machine |     |     |     |     |     |     |     |
| ---------- | ---------- | --------------- | ------- | ------- | --- | --- | --- | --- | --- | --- | --- |
learningalgorithmsonagivendatasetdependsonwell-tuned
|     |     |     |     |     | To estimate |     | the generalization |     | performance | of  | an SVM |
| --- | --- | --- | --- | --- | ----------- | --- | ------------------ | --- | ----------- | --- | ------ |
hyper-parameter.InsettingupanSVMmodel,forinstance, model, generally one evaluates accuracy measure on data
twoproblemsareencountered:(1)howtoselectthekernel
notusedfortrainingthemodel.Thek-foldcross-validation
function,and(2)howtoselectitshyper-parameter.AnSVM (k-CV)isthemostusedprocedure.Itconsistsonpartitioning
withpolynomialkernelhasthreeparametersthatneedtobe
dataintokdisjointsetsofapproximatelyequalsize.AnSVM
optimized:theregularizationparameterC,theparametera, isthustrainedktimes:atthei−thiteration,allthedisjoint
| andthedegreed.Theoptimizationofthesethreeparameters |     |     |     |     |      |          |             |            |       | −th  |          |
| --------------------------------------------------- | --- | --- | --- | --- | ---- | -------- | ----------- | ---------- | ----- | ---- | -------- |
|                                                     |     |     |     |     | sets | are used | as training | set except | the i | set, | which is |
if50stepsshouldbeperformed,requiresanamountoftime used to evaluate the performance of the model. The errors
| totestthetotal503 | =125000combinations.Thegreaterthe |     |     |     |     |     |     |     |     |     |     |
| ----------------- | --------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
observedinthisprocessareaveragedyieldingthek-foldCV
numberofparameterstobeset,thegreateristhenumberof
error.
combinations.
Beforeintroducingthemostusedevaluationmeasures,it
| The cost-sensitive |     | SVM (CS-SVM) | uses | two penalty |     |     |     |     |     |     |     |
| ------------------ | --- | ------------ | ---- | ----------- | --- | --- | --- | --- | --- | --- | --- |
isusefultorevisetheconfusionmatrixofbinaryclassification
| weightsforthetwoclasses.LetC |     |     | ,bethecostofafalsenega- |     |                                                      |     |     |     |     |     |     |
| ---------------------------- | --- | --- | ----------------------- | --- | ---------------------------------------------------- | --- | --- | --- | --- | --- | --- |
|                              |     |     | 1                       |     | problems.AgeneralconfusionmatrixisillustratedinTable |     |     |     |     |     |     |
tive.Itpenalizesmisclassificationofinstancesoftheminority
1.Thetwocolumnsrefertothepredictedclasses,whereasthe
| class.Analogously,letC−1 |     | ,bethecostofafalsepositive.It |     |     |     |     |     |     |     |     |     |
| ------------------------ | --- | ----------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
tworowsrefertotheactualclasses.TruePositives(TP)isthe
penalizesmisclassificationofinstancesofthemajorityclass.
|     |     |     |     |     | number | of positive | instances | correctly | classified |     | and False |
| --- | --- | --- | --- | --- | ------ | ----------- | --------- | --------- | ---------- | --- | --------- |
TheoptimizationmodelCS-SVMis(4)-(6).
|     |     |     |     |     | Negatives | (FN) | is the number |     | of positive | instances | incor- |
| --- | --- | --- | --- | --- | --------- | ---- | ------------- | --- | ----------- | --------- | ------ |
rectlyclassifiedasnegative.Thesetwonumbersrefertothe
|     |     | (cid:2) | (cid:2) |     |     |     |     |     |     |     |     |
| --- | --- | ------- | ------- | --- | --- | --- | --- | --- | --- | --- | --- |
1
argmin (cid:6)w(cid:6)2+C[C ]ξ +C−1 ξ ] (4) minorityclass.Similarly,TrueNegatives(TN)isthenumber
|     |     | 1   | i   | i   |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
w,b,ξ 2 ofnegativeinstancescorrectlyclassified,andFalsePositives
|     |     | i|yi =1 | i|yi =−1 |     |     |     |     |     |     |     |     |
| --- | --- | ------- | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
123

| Ahyper-parametertuningapproach... |     |     |     |     |     |     |     |     |     |     |     |     |     | 12867 |
| --------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----- |
Table1 Confusionmatrixforabinaryproblem classificationevaluationmeasuresthatallowtobalancefalse
positiverateandfalsenegativerate.Here,amongthesemea-
Predicted
sures,weevaluateevenF-Measure,theGeometricMean,the
positiveclass negativeclass averagecost,theYouden’sindex,andthebalancedaccuracy.
| Actual | positiveclass |     |     | TP  |     | FN  |     | Theyaredefinedasfollows. |     |     |     |     |     |     |
| ------ | ------------- | --- | --- | --- | --- | --- | --- | ------------------------ | --- | --- | --- | --- | --- | --- |
negativeclass FP TN F-Measureintegratessensitivityandprecisionintoanaver-
agebyaharmonicmean
| (FP) is the | number | of  | negative | instances | incorrectly |     | classi- |     |     |               |     |           |     |     |
| ----------- | ------ | --- | -------- | --------- | ----------- | --- | ------- | --- | --- | ------------- | --- | --------- | --- | --- |
|             |        |     |          |           |             |     |         |     |     | 2Sensitivity× |     | Precision |     |     |
−Measure=
| fiedaspositiveclass.Thesetwonumbersrefertothemajority |     |     |     |     |     |     |     | F   |     |              |     |           |     |     |
| ----------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------ | --- | --------- | --- | --- |
|                                                       |     |     |     |     |     |     |     |     |     | Sensitivity+ |     | Precision |     |     |
class.Observethat,incaseofdatarelatedtopatients,afalse
negativemeansthatpatienthasthediseasebutthediagnosis
Theharmonicmeanoftwonumberstendstobeclosertothe
resultsaysthatitdoesnothave.
|     |             |     |            |          |     |          |        | smaller number. |     | A high | F-Measure | value | means | that both |
| --- | ----------- | --- | ---------- | -------- | --- | -------- | ------ | --------------- | --- | ------ | --------- | ----- | ----- | --------- |
| The | most common |     | evaluation | measures |     | used are | listed |                 |     |        |           |       |       |           |
SensitivityandPrecisionarehigh.
below.
GeometricMean(G-Mean)issuggestedasthebalancedper-
| Accuracy | defined | as  | the ratio | between |     | the number | of  |     |     |     |     |     |     |     |
| -------- | ------- | --- | --------- | ------- | --- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- |
formancebetweenthetwoclasses.Itisintrinsicallydefined
instancescorrectlyclassifiedandthetotalnumberofinstances.
|     |     |     |     |     |     |     |     | as the geometric |     | mean of | sensitivity | and | specificity. | If the |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------------- | --- | ------- | ----------- | --- | ------------ | ------ |
Itassessestheoveralleffectivenessofthemodelbyshowing
|     |     |     |     |     |     |     |     | G-Mean value | is  | high, both | Sensitivity |     | and Specificity | are |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------ | --- | ---------- | ----------- | --- | --------------- | --- |
theprobabilityofthetruevalueoftheclasslabel
expectedtobehighsimultaneously
|     |     |     | +TN |     |     |     |     |     | (cid:5) |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ------- | --- | --- | --- | --- | --- |
TP
| Accuracy | =   |     |        |     |     |     |     | G−Mean | =   | Sensitivity×Specificity |     |     |     |     |
| -------- | --- | --- | ------ | --- | --- | --- | --- | ------ | --- | ----------------------- | --- | --- | --- | --- |
|          |     | +FP | +Tn+FN |     |     |     |     |        |     |                         |     |     |     |     |
TP
Othertwomeasuresthatseparatelyestimateaclassifier’sper- AverageCost(AC)isexpressedas
formanceondifferentclassesaresensitivityandspecificity.
|     |     |     |     |     |     |     |     |     |     | C ×FN | +C−1 | ×FP |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----- | ---- | --- | --- | --- |
Theyareoftenemployedinmedicalandbio-medicalappli- AverageCost = 1
| cations. |     |     |     |     |     |     |     |     |     | TP +TN | +FP | +FN |     |     |
| -------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------ | --- | --- | --- | --- |
Sensitivity(truepositiverate)isdefinedastheratiobetween where C and C−1 are the two costs used in the objective
1
thenumberofpositiveinstancescorrectlyclassifiedassuch
functionofCS-SVM.
andthenumberofpositiveinstances
|             |     |     |     |     |     |     |     | Youden’s index                       | Y   | equally | weights | the | algorithm’s | perfor- |
| ----------- | --- | --- | --- | --- | --- | --- | --- | ------------------------------------ | --- | ------- | ------- | --- | ----------- | ------- |
|             |     | TP  |     |     |     |     |     | manceonpositiveandnegativeinstances: |     |         |         |     |             |         |
| Sensitivity | =   |     |     |     |     |     |     |                                      |     |         |         |     |             |         |
+FN
TP
Y =sensitivity+specificity−1
Specificity(truenegativerate)isdefinedastheratiobetween
thenumberofnegativeinstancescorrectlyclassifiedassuch Balanced accuracy(BA) is the average of sensitivity and
andthenumberofnegativeinstances
specificity:
|             |            | T N |           |       |        |        |        |          |          |     | sensitivity+ | specificity |     |     |
| ----------- | ---------- | --- | --------- | ----- | ------ | ------ | ------ | -------- | -------- | --- | ------------ | ----------- | --- | --- |
| Specificity | =          |     |           |       |        |        |        |          |          | =   |              |             |     |     |
|             |            | +   |           |       |        |        |        | Balanced | accuracy |     |              |             |     |     |
|             |            | TN  | FP        |       |        |        |        |          |          |     |              | 2           |     |     |
| Precision   | is defined | as  | the ratio | of TP | to the | number | of all |          |          |     |              |             |     |     |
instancespredictedaspositive
4 Multi-objectiveoptimizationproblems
andGeneticalgorithms
TP
=
Precision
TP +FP
Multi-objectiveoptimizationproblemsconsistofmorethan
Asreportedespeciallyrecentlyinsomepapers(e.g.,Tao onecriterion,oftenconflicting,forwhichanysolutionexist-
et al. 2019), the accuracy-based evaluation measure is not ing on the Pareto front of criterion trade-offs is considered
| suitableforclassificationofimbalanceddataastheminority |     |     |     |     |     |     |     | optimal. |     |     |     |     |     |     |
| ------------------------------------------------------ | --- | --- | --- | --- | --- | --- | --- | -------- | --- | --- | --- | --- | --- | --- |
class has very little effect on the accuracy compared to the Inthissection,weintroducemulti-objectiveoptimization
majority class. For imbalanced classification problems, the problemsandthecornerstoneconceptofParetooptimality.
correctclassificationofinstancesoftheminorityclassisusu- Amulti-objectiveproblemconsistsofminimizingand/or
allythemostimportantmeasure.Therearefurtherinteresting maximizing two or more objective functions subject to
123

12868 R.Guidoetal.
inequality and/or equality constraints. The objective func- lems. This algorithm was called non-dominated sorting
tionsareconflictingamongthemandasolutionisatrade-off genetic-algorithm (NSGA). Deb et al. (2002) improved it
intheobjectivefunctionspace. by proposing NSGA-II. The key features of NSGA-II are
elitism, diversity-preserving mechanisms, and emphasis on
Definition1 A solution is defined Pareto optimal if there
non-dominatedsolutions.InNSGA-II,the N offspringsare
doesnotexistanyothersolutionintheobjectivespacewhich
createdfromtheNparentsusingstandardgeneticalgorithms.
improvesthevalueofanyofitsobjectivefunctionswithout
Thenewpopulationatthenextgenerationisgivenbyselect-
deterioratingatleastoneotherobjectivefunctionvalue.
ingthenon-dominatedsolutionsfortheParetofrontwiththe
Inotherwords,anon-dominatedsolutionprovidesasuit- highestdiversitywhilediscardingtherestofthesolutions.
able compromise between all objectives without degrading
Tournament selection This is a procedure that imitates sur-
any of them. The multi-objective optimization process is
vivalofthefittestinnature.Indeed,eachindividualcompetes
looking for a set of alternative solutions that represent the
intwotournamentswithrandomlyselectedindividuals.The
Paretooptimalsolution.Asetofnon-dominatedindividuals
crowded tournament selection is based on ranking and dis-
formaPareto-optimalfront.
tance:ifasolutionhasabetterrankthananotherone,itwill
From the mathematical point of view, the definition of
beselected;iftheranksarethesamebutthecrowdingdis-
thedominancebetweentwosolutionsx andx isthatx is
1 2 1 tance is not, the solution with better crowding distance is
noworsethan x inallobjectives f ,i ∈ {1,...,m}ofthe
2 i selected.
problem.Thisconceptcanbeexpressedasx dominatesx
1 2
if f (x ) ≤ f (x )∀i ∈ {1,...,m}and ∃ j ∈ {1,...,m} : CrowdingdistanceThecrowdingdistancemetricofanindi-
i 1 i 2
f (x )≤ f (x ). vidual proposed by Deb and Goel (2001) aims to select
j 1 j 2
ThegeneticalgorithmsweredevelopedbyHollandandhis potential individuals to construct a new population. It is
collaborators (Holland 1975) as a model based on Charles essentially based on the cardinality of a solution sets and
Darwin’s theory of natural selection. They are heuristic their distance to solution boundaries. More specifically, it
searchtechniques,successfullyappliedtodifferentdomains is defined as the perimeter of the rectangle with its nearest
(e.g., Guido and Conforti 2017; Bao-De et al. 2021). Fur- neighbors at diagonally opposite corners. Two individuals
thermore, they demonstrated a large amount of inherent with a same rank are better if they have a larger crowding
parallelism that makes them attractive mainly for solving distance.
problems defined in large feature spaces, as that one here
Crossover and mutation Crossover and mutation are
addressed. The evolutionary process usually starts from a
employedtoobtaintheoffspringpopulation.
populationofrandomlygeneratedindividuals,whicharethe
Algorithm1showstheframeworkofNSGA-II.Themain
chromosomes.Itisaniterativeprocess.Oneiterationisone
stepsofNSGA-IIcanbesummarizedasfollows:
generation.Ineachgeneration,thefitnessofeveryindividual
inthepopulationisevaluated.Thefitnessvalueofachromo-
Step1 Create a new population by combining parents and
someisameasureofitsgoodness.Thefitnessisusuallythe
offspringsandapplynon-dominatedsorting
valueoftheobjectivefunctionintheoptimizationproblem
Step2 Identifydifferentfronts
beingsolved.Usually,operatorssuchasselection,crossover,
Step3 Generatethenewpopulationbyexploitingthefronts
mutation and recombination are applied during the evolu-
givenatthepreviousstepuntilsize N
tionaryprocessoverthegeneratedpopulationstofindbetter
Step4 Usethecrowddistancetocarryoutacrowdingsort
chromosomes,whichoptimizethefitnessfunctiontillater-
appliedtothefronts
minationconditionisreached.Theoffspringsinapopulation
Step5 Generatenewoffspringfromthecurrentpopulation
act like independent agents so that they explore the search
via the genetic operators crossover, mutation, and
spaceinmanydirections.
selection
Aswellknown,geneticalgorithmshavesomedisadvan-
tages mainly due to the choice of parameters such as the
mutation rate and crossover rate that should be carried out
carefully.Thecrossoveroperatorisoneofthemostimpor-
tantoperatorsbecauseitdeterminestheglobalconvergence 5 Proposedapproach
ofthegeneticalgorithm.
In this section, is firstly introduced a basic approach for
4.1 NSGA-II hyper-parameter optimization. Then, a novel algorithm for
hyper-parameterstuningbasedonGAandDTisproposed.
Srinivas and Deb (1994) proposed an algorithm based The core of the algorithm is a fitness function evaluation
on non-dominated sorting for solving multiobjective prob- procedurealongwithasimilarityprocedure.
123

| Ahyper-parametertuningapproach... |     |     |     |     |     |     |     | 12869 |
| --------------------------------- | --- | --- | --- | --- | --- | --- | --- | ----- |
Algorithm1NSGA-II
Require:
RandompopulationP0;achildpopulationQ0isgeneratedfromthe
| populationofparents | P0usinggeneticoperatorssuchascrossover |     |     |     |     |     |     |     |
| ------------------- | -------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
andmutation
1: whileanystoppingcriterionisnotreacheddo
| 2: Rt = | Pt ∪Qt |     |     |     |     |     |     |     |
| ------- | ------ | --- | --- | --- | --- | --- | --- | --- |
3: fast-non-dominated-sort(Rt)
| 4: Pt+1       | =∅;i =1;     |     |     |     |     |     |     |     |
| ------------- | ------------ | --- | --- | --- | --- | --- | --- | --- |
| 5: while|Pt+1 | |+|Fi |<N do |     |     |     |     |     |     |     |
6: Applycrowding-distance-assignmentFi
| 7: Pt+1 | ← Pt+1 ∪Fi |     |     |     |     |     |     |     |
| ------- | ---------- | --- | --- | --- | --- | --- | --- | --- |
8: i ←i+1
9: endwhile
| 10: Sort(Fi | ,<N)                 |       |     |     |     |     |     |     |
| ----------- | -------------------- | ----- | --- | --- | --- | --- | --- | --- |
| 11: Pt+1    | ← Pt+1 ∪Fi [1:(N−|Pt | +1|)] |     |     |     |     |     |     |
| 12: Qt+1    | ←createNewPopPt+1    |       |     |     |     |     |     |     |
13: t ←t+1
14: endwhile
Fig.2 Frameworkoftheimprovedhyper-parametersalgorithm
|     |     |     |     | out is 4800 | and the computational |     | time may | be extremely |
| --- | --- | --- | --- | ----------- | --------------------- | --- | -------- | ------------ |
high.
|     |     |     |     | There | are two main | issues: the | first one | is related to the |
| --- | --- | --- | --- | ----- | ------------ | ----------- | --------- | ----------------- |
timeneededtocarryoutk-foldCV;thesecondone,isrelated
tothefactthatoftenachromosomeisslightlydifferentfrom
|     |     |     |     | another         | one already evaluated | and        | with equal     | fitness. We    |
| --- | --- | --- | --- | --------------- | --------------------- | ---------- | -------------- | -------------- |
|     |     |     |     | try to overcome | these                 | two issues | by introducing | a proce-       |
|     |     |     |     | dure in the     | NSGA-II               | algorithm  | that exploits  | a suitable and |
Fig.1 MainstepsofNSGA-II trainedDT.Theproposedalgorithm,describedinthefollow-
|     |     |     |     | ing, reduces | considerably | the overall | number | of performed |
| --- | --- | --- | --- | ------------ | ------------ | ----------- | ------ | ------------ |
k-foldCVbycombiningNSGA-IIwithaDT.Thegoalisto
5.1 Basicapproach
evaluateonlyasmallsetofchromosomesateachgeneration
byak-foldCV.Thisproceduredoesnotaffectconvergenceof
ThebasicapproachconsistsonusingNSGA-IIalgorithmfor
thealgorithmandstronglyreducestheoverallcomputational
solvingamulti-objectivehyper-parametertuningproblem.A
time.
| set of hyper-parameter | codified | as a chromosome | is evalu- |     |     |     |     |     |
| ---------------------- | -------- | --------------- | --------- | --- | --- | --- | --- | --- |
atedbyak-foldCVapproach.Afitnessfunctionevaluation
isthusperformedateachgeneration,i.e.,eachchromosome 5.2 Improvedhyper-parametersalgorithm
hasitsfitnessfunctionsevaluated.However,thisapproachis
quitetimeconsuming.Indeed,letN,bethenumberofchro- The above basic approach has been modified in order to
mosomesofapopulation,andGthenumberofgenerations. evaluate the fitness function only of some individuals of a
Ateachgeneration,thenumberofcarriedoutk-foldCVis population by a k-fold CV. Figure 2 provides an intuitive
N, one per each chromosome. The overall number of per- understandingoftheproposedalgorithmframework.
|     |     | ×G.Forexample,if | =   |     |     |     |     |     |
| --- | --- | ---------------- | --- | --- | --- | --- | --- | --- |
formedk-foldCVisthus N N 24 Each chromosome consists of a number of genes that
andG =200,theoverallnumberofk-foldCVtobecarried representthehyper-parameters ofCS-SVM.Thealgorithm
123

12870 R.Guidoetal.
startsfromaninitialpopulation Pop .Itconsistsofthefol-
0
lowingfivemainsteps.
Algorithm2Proposedhyper-parametersalgorithm
1: Step1Initialization
2: Step1.1DefineGenSetasasetofnumbersofgenerations
3: Step1.2CreateaninitialpopulationPop0
4: Step 2 (Fitness function evaluation) Evaluate the fitness value of
eachchromosomeinthecurrentpopulation.
5: ifthecurrentgenerationGen∈GenSetthengotoStep2.1
6: elsegotoStep2.2
7: endif
8: Step2.1Performak-CV
9: Step2.2(Similarityprocedure)Compareeachchromosomewith
theonesofthepreviouspopulation
10: if Similarity=Truethenassignafitnessvaluetoitbythetrained
DT
11: elsegotoStep2.1
12: endif
13: Step3Terminationcriteria.Ifatleastoneofthestoppingconditions
ismeet,thealgorithmstops
14: Step4TrainDecisionTree.Thecurrentpopulationisusedtotrain
aDecisionTree.
15: Step 5 Reproduce a new population. The operators of selection,
crossoverandmutationareappliedoverthegeneratedpopulationto
findbetterchromosomes.
ThecoreofAlgorithm2isthefitnessevaluationprocedure
atStep2,explainedinthefollowing.
Step2: Fitness evaluation procedure The aim of the fitness
Fig.3 Fitnessevaluationprocedure
evaluation step is to provide a procedure that reduces the
numberoffitnessevaluationsandconsequentlythenumber
of carried out k-fold CV. To this purpose, a DT is trained is found, a cost-sensitive learning classifier SVM-based is
at each generation and used to predict the fitness value of builtandthefitnessvalueisevaluatedbyk-foldCV.
somechromosomes,asexplainedbelow.Indeed,thefitness Similaritybetweentwochromosomescanbeestimatedby
of a chromosome in a population is evaluated or assigned: various distance measurement methods. Here, we designed
Awholepopulationisevaluatedbyk-foldCVonlyatthose a procedure that evaluates similarity between two chromo-
generationswell-definedinthesetGenSet.Thismeansthat somesasfollows.Letchr 1 andchr 2 ,betwochromosomes
thecost-sensitivelearningclassifierSVM-basedisbuiltusing representedasvectors.Theprocedurecompareseachcorre-
thehyper-parameterscodifiedaschromosomesofthepopula- sponding couple of genes of chr 1 and chr 2 , as detailed in
tion;foreverychromosomes,ak-foldCVisusedtoestimate Algorithm 3. More specifically, the difference between the
thegeneralizationabilityoftherelatedbuildmodel.Theset i−thgeneofchr 1 andthecorrespondinggeneofchr 2 iscom-
GenSet hasatleasttwoelements,i.e.,thefirstandthelast puted.Ifthisdifferenceislessthanagiventhresholdt i ,the
generation.AprocedurebasedonalearnedDTtakesplace nextcoupleofgenesofthetwochromosomesarecompared;
atthosegenerationsnotinthesetGenSet. otherwise,theprocedurestopsandthetwochromosomesare
ThefitnessevaluationprocedureisdepictedinFig.3.To notsimilar.
reducetheoverallcomputationaltime,theprocedureverifies Figure 4 depicts an example of DT trained to predict a
if each chromosome has already a fitness value (because it givenfitnessfunction.
hasbeenevaluatedpreviously).Ifso,theprocedureanalyzes
nextchromosome;otherwise,thechromosomeiscompared,
at Step 2.2, with the chromosomes of the previous popu- 6 Experimentalresultsandanalysis
lation in order to discover similarity. If the chromosome is
similar at least to one chromosome, the DT trained on the In this study, we test the proposed Algorithm 2 for on six
previous population predicts its fitness value; this value is benchmarkimbalanceddatasetsbinaryclassificationtaskto
thusassignedaspredictedvalue.Otherwise,ifnosimilarity comparetheperformanceofdifferentclassificationmethods
123

| Ahyper-parametertuningapproach... |     |     |     |     |     |     |     |     |     |     | 12871 |
| --------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----- |
Fig.4 Anexampleoftrained
decisiontree
Algorithm3Similarityprocedure investigatedandtunedoverarereportedinSect.6.2.Exper-
| Require: |     |     |                        |              | imentalresultsarelistedinSect.6.3. |     |     |     |     |     |     |
| -------- | --- | --- | ---------------------- | ------------ | ---------------------------------- | --- | --- | --- | --- | --- | --- |
|          |     |     | ,chr2 ∈ Rk.Thresholdti | ,i =1,...,k. |                                    |     |     |     |     |     |     |
Twochromosomeschr1
=1;similarity←true
1: i
≤kdo
2: whilei
| if|chri1 | −chri2 | |<ti |      |     | 6.1 Benchmarkdatasets |     |     |     |     |     |     |
| -------- | ------ | ---- | ---- | --- | --------------------- | --- | --- | --- | --- | --- | --- |
| 3:       |        |      | then |     |                       |     |     |     |     |     |     |
←i+1
4: i
5: else The datasets are from the University of California Irvine
←k
| 6:  | i   |     |     |     | (UCI) | Repository |     | of Machine |     | Learning | Databases |
| --- | --- | --- | --- | --- | ----- | ---------- | --- | ---------- | --- | -------- | --------- |
similarity←
| 7:  |     | false |     |     |     |     |     |     |     |     |     |
| --- | --- | ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
(https://archive.ics.uci.edu/ml/datasets.php).Theyhavediver-
8: endif
|     |     |     |     |     | sity in the | number | of  | attributes | and | imbalance | ratio. More- |
| --- | --- | --- | --- | --- | ----------- | ------ | --- | ---------- | --- | --------- | ------------ |
9: endwhile
10: returnsimilarity over, the datasets have both continuous and categorical
attributes,andsomeofthemhavemissingvalues.
|     |     |     |     |     | Appendicitis |     | dataset | consists | of  | 106 | instances and 8 |
| --- | --- | --- | --- | --- | ------------ | --- | ------- | -------- | --- | --- | --------------- |
intheliteraturewithourresults.Theyarerelatedtomedical attributes.Theattributesareresultsoflaboratorytest.
diagnosisrepresentedasbinaryclassificationproblemsand
|     |     |     |     |     | Haberman |     | datasetdescribesthefive-yearorgreatersur- |     |     |     |     |
| --- | --- | --- | --- | --- | -------- | --- | ----------------------------------------- | --- | --- | --- | --- |
have different sample sizes, attributes, and imbalance ratio vival of breast cancer patients. The study was conducted
| (IR), defined | as  | m/M | (Amin et al. 2016), | where m is the |         |      |          |     |                |     |              |
| ------------- | --- | --- | ------------------- | -------------- | ------- | ---- | -------- | --- | -------------- | --- | ------------ |
|               |     |     |                     |                | between | 1958 | and 1970 | at  | the University |     | of Chicago’s |
number of the minority instances and M is the number of BillingsHospital.Thedatasetconsistsof306instancesand
majorityinstances.
|              |     |             |           |               | 4 attributes.  | The | outcome | is  | patient | survival. | There are no |
| ------------ | --- | ----------- | --------- | ------------- | -------------- | --- | ------- | --- | ------- | --------- | ------------ |
| We conducted |     | experiments | to answer | the following | missingvalues. |     |         |     |         |           |              |
researchquestionsempirically:
|     |     |     |     |     | Hepatitis | datasetisusedtoclassifypatientswithhepati- |     |     |     |     |     |
| --- | --- | --- | --- | --- | --------- | ------------------------------------------ | --- | --- | --- | --- | --- |
tisinthetwoclasses,liveordie.Itconsistsof155instances
1. Doesmulti-objectiveoptimizationfindmuchsparsersolu-
|     |     |     |     |     | and 19 attributes, |     | 14 nominal |     | attributes | and | 6 multi-valued |
| --- | --- | --- | --- | --- | ------------------ | --- | ---------- | --- | ---------- | --- | -------------- |
tions without a major loss in predictive performance attributes. It requires the determination of whether patients
comparedtosingle-objectiveoptimization?
withhepatitiswilleitherliveordie.Theproblemaimstopre-
2. Aretherealternativemetricstotheaccuracy? dictthepresenceorabsenceofhepatitisbyusingtheresults
| 3. May | the computational |     | time be reduced | by a machine |     |     |     |     |     |     |     |
| ------ | ----------------- | --- | --------------- | ------------ | --- | --- | --- | --- | --- | --- | --- |
ofvariousmedicaltestscarriedoutonapatient.Thedataset
| learningtechnique? |     |     |     |     | hasmissingvalues. |        |          |         |     |         |                 |
| ------------------ | --- | --- | --- | --- | ----------------- | ------ | -------- | ------- | --- | ------- | --------------- |
|                    |     |     |     |     | Pima              | Indian | Diabetes | dataset | is  | used to | predict whether |
AbriefdescriptionofthedatasetsisinSect.6.1.Detailson ornotapatienthasdiabetes.Allpatientsarefemale,areat
the algorithms embedded in our approach and the hyper- least21yearsold,andareofPimaIndianheritage.Ithas8
parameter spaces of the several CS-SVM that are being laboratoryfeatures.
123

| 12872 |     |     |     |     |     |     |     |     |     |     |     |     | R.Guidoetal. |
| ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------ |
Table2 Datasetsandtheirmaincharacteristicsintermsofnumberof
attributes(No.A),numberoftheminorityinstances(m),numberofthe
majorityinstances(M),indexratioIR=m/M
| Dataset |     | No.A |     | m   | M   | IR  |     |     |     |     |     |     |     |
| ------- | --- | ---- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Fig.5 Representationofachromosome
| Appendicitis |     | 8   |     | 21  | 85  | 0.25 |     |     |     |     |     |     |     |
| ------------ | --- | --- | --- | --- | --- | ---- | --- | --- | --- | --- | --- | --- | --- |
| Haberman     |     | 4   |     | 81  | 225 | 0.36 |     |     |     |     |     |     |     |
Hepatitis 19 70 85 0.82 ments were run on a PC Intel Xeon E5 1620 CPUs with 4
| Pima |     | 9   |     | 268 | 500 | 0.53 | coresat3.50GHzand32GBRAM.               |     |     |     |     |     |         |
| ---- | --- | --- | --- | --- | --- | ---- | --------------------------------------- | --- | --- | --- | --- | --- | ------- |
| WDBC |     | 10  |     | 241 | 458 | 0.53 |                                         |     |     |     |     |     |         |
| WPBC |     | 32  |     | 47  | 151 | 0.33 | 6.2.1 Parametersetting                  |     |     |     |     |     |         |
|      |     |     |     |     |     |      | Algorithm2startsfromaninitialpopulation |     |     |     |     | Pop | ofchro- |
0
|           |     |            |        |        |        |         | mosomes | randomly     | generated. |                 | Each chromosome |            | has four |
| --------- | --- | ---------- | ------ | ------ | ------ | ------- | ------- | ------------ | ---------- | --------------- | --------------- | ---------- | -------- |
| Wisconsin |     | Diagnostic | Breast | Cancer | (WDBC) | dataset |         |              |            |                 |                 |            |          |
|           |     |            |        |        |        |         | genes   | representing | the        | hyper-parameter |                 | of CS-SVM, | as       |
consistsof30featurescomputedbydigitizedimageoffine
|     |     |     |     |     |     |     | depicted | in Fig. | 5. All | experiments | have | the same | random |
| --- | --- | --- | --- | --- | --- | --- | -------- | ------- | ------ | ----------- | ---- | -------- | ------ |
needleaspirateofabreastmassindex.Theproblemaimsto
initialpopulation;thenumberofgenerationsistheonlyone
predictwhetherornotthepatienthasbreastcancer.
stoppingcriterion.
WisconsinPrognosticBreastCancer(WPBC)datasethas
Table3liststhesearchpopulationsize,crossoverprobabil-
198instancesthatrepresentfollow-updataforonebreastcan-
|     |     |     |     |     |     |     | ity p ,genemutationprobability |     |     |     | p ,numberofgenerations |     |     |
| --- | --- | --- | --- | --- | --- | --- | ------------------------------ | --- | --- | --- | ---------------------- | --- | --- |
cer case, only those cases exhibiting invasive breast cancer c m
|     |     |     |     |     |     |     | along | with the | design | parameters | (decision | variables) | and |
| --- | --- | --- | --- | --- | --- | --- | ----- | -------- | ------ | ---------- | --------- | ---------- | --- |
andnoevidenceofdistantmetastasesatthetimeofdiagno-
therangeoftheirvariations.Wetestedtwopopulationsizes
sis.Itisusedinthispapertoclassifypatientsasrecurrences
andcreatedtheinitialparentpopulationrandomlybyselect-
before24months(positiveclass)ornon-recurrencebeyond
|     |     |     |     |     |     |     | ing solutions | from | the | ranges | defined | for the | parameters |
| --- | --- | --- | --- | --- | --- | --- | ------------- | ---- | --- | ------ | ------- | ------- | ---------- |
24months(negativeclass).Weremovedthefeaturenamed
C,C ,C ,γ,whereC
|                                                     |     |     |     |     |     |     |     |     |     | andC | arethecostsoftheminority |     |     |
| --------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---- | ------------------------ | --- | --- |
| “Time”fromthedatasetbecauseitistherecurrencetimefor |     |     |     |     |     |     | 1   | 2   | 1   | 2    |                          |     |     |
classandmajorityclass,respectively.
| instances | in the | positive | class | and | the disease-free | time for |     |     |     |     |     |     |     |
| --------- | ------ | -------- | ----- | --- | ---------------- | -------- | --- | --- | --- | --- | --- | --- | --- |
theinstancesofthenegativeclass. The multi-objective problem that we formulated and
solvedhasthreefitnessfunctions(7–9),givenbyaccuracy,
| Table | 2 summarizes, |     | per | each | dataset, the | number of |     |     |     |     |     |     |     |
| ----- | ------------- | --- | --- | ---- | ------------ | --------- | --- | --- | --- | --- | --- | --- | --- |
attributes,thenumberofminorityinstances(diseasedexam- G-mean,andAverageCost,respectively:
| ples), the                  | number | of  | the majority |     | instances (non-diseased |     |      |        |        |     |     |     |     |
| --------------------------- | ------ | --- | ------------ | --- | ----------------------- | --- | ---- | ------ | ------ | --- | --- | --- | --- |
|                             |        |     |              |     |                         |     |      |        | TP +TN |     |     |     |     |
| examples),andtheindexratio. |        |     |              |     |                         |     | =max |        |        |     |     |     |     |
|                             |        |     |              |     |                         |     | f 1  |        |        |     |     |     | (7) |
|                             |        |     |              |     |                         |     |      | TP +FP | +TN    | +FN |     |     |     |
(cid:5)
|     |     |     |     |     |     |     | f =max | Sensitivity×Specificity |     |     |     |     | (8) |
| --- | --- | --- | --- | --- | --- | --- | ------ | ----------------------- | --- | --- | --- | --- | --- |
2
| 6.2 Learningalgorithmsandhyperparameters |     |     |     |     |     |     |        | C ×FN | +C  | ×FP |     |     |     |
| ---------------------------------------- | --- | --- | --- | --- | --- | --- | ------ | ----- | --- | --- | --- | --- | --- |
|                                          |     |     |     |     |     |     | f =min | 1     |     | 2   |     |     | (9) |
| optimization                             |     |     |     |     |     |     | 3      | +TN   | +FP | +FN |     |     |     |
TP
WeconsideredseveralmodelclassifiersCS-SVMwithGaus- Alltheexperimentsareconductedby10-foldcross-validation.
| sian kernel | tuned | by  | the optimization |     | algorithm | proposed. |     |     |     |     |     |     |     |
| ----------- | ----- | --- | ---------------- | --- | --------- | --------- | --- | --- | --- | --- | --- | --- | --- |
The experiments were performed by the ML algorithms of 6.3 Computationalresults
| Waikato | Environment |     | for Knowledge |     | Analysis | (WEKA). |     |     |     |     |     |     |     |
| ------- | ----------- | --- | ------------- | --- | -------- | ------- | --- | --- | --- | --- | --- | --- | --- |
WEKA isanopen-source collection of MLalgorithms and Toassessourapproach,weperformedbothAlgorithm1and
dataprocessingtools.WeusedSequentialminimaloptimiza- Algorithm 2 on the six datasets and compared the results.
tion algorithm for SVM and Random Tree algorithm for The computational experiments were carried out using the
DT. For that concerning NSGA-II algorithm, we used the JCLECsequentialalgorithmanditsparallelizedversion.The
frameworknamedJavaClassLibraryforEvolutionaryCom- only difference we noticed was the reduced computational
putation (JCLEC) Ramírez et al. (2015, 2019), which is a timeoftheparallelizedversionwithrespecttothesequential
Javasuiteforsolvingmulti-objectiveoptimizationproblems algorithm.Wereportinthissectiononlytheresultsfoundby
| usingevolutionaryalgorithms. |     |     |     |     |     |     | theparallelversion. |     |     |     |     |     |     |
| ---------------------------- | --- | --- | --- | --- | --- | --- | ------------------- | --- | --- | --- | --- | --- | --- |
Algorithm 2 has been coded in Java using the NSGA Table 4 reports the best fitness values per each dataset.
II algorithm of the JCLEC framework. We executed both From the second to the fourth column there is the value of
thesequentialandtheparallelversionoftheNSGA-II.The accuracy,G-Mean,andaveragecost,respectively.Wecom-
parallel version is more efficient since it performs function pareinthistableourresultswiththebestonesoftheliterature
evaluations of different individuals in parallel. The experi- byselectingthosepapersthatoptimizedhyper-parameterof
123

Ahyper-parametertuningapproach... 12873
Table3 NSGA-IIparameters
|     | NSGA-IIparameters |     |     |     | CS-SVMhyper-parameterspace |     |     |
| --- | ----------------- | --- | --- | --- | -------------------------- | --- | --- |
andhyper-parametersspacesof
| CS-SVMwithRBFkernel | Popsize | pc  | pm   | NumGen | Cost      |     | γ         |
| ------------------- | ------- | --- | ---- | ------ | --------- | --- | --------- |
|                     | 24      | 0.8 | 0.25 | 100    | C ∈{1−50} |     | {0.001−1} |
∈{1−20}
|     | 48  |     |     | 200  | C1         |     |     |
| --- | --- | --- | --- | ---- | ---------- | --- | --- |
|     |     |     |     | 1000 | C2 ∈{1−10} |     |     |
Table4 Bestmetricvaluesby
|     | Dataset | Accuracy | G-Mean | AC  | Acc AC | G-Meana | G-Meanb |
| --- | ------- | -------- | ------ | --- | ------ | ------- | ------- |
theoptimizedhyper-parameters
|     |     |     |     |     | [1] [2] | [3] | [3] |
| --- | --- | --- | --- | --- | ------- | --- | --- |
comparedtothebestresultsof
theliterature.[1](YuandWang
|     | Appendicitis | 89.62 | 82.54 | 0.11 | – – |     |     |
| --- | ------------ | ----- | ----- | ---- | --- | --- | --- |
2017);[2](Qietal.2013);
|                          |          |       |       |      |     | 60.77±3.89 | 66.71±1.67 |
| ------------------------ | -------- | ----- | ----- | ---- | --- | ---------- | ---------- |
| [3](Taoetal.2019).Hyphen | Haberman | 76.14 | 67.70 | 0.26 | – – |            |            |
meansthattheauthorsdidnot Hepatitis 87.10 84.06 0.14 83.22 0.208
testthatdataset
|     | Pima | 78.13 | 76.54 | 0.22 | 76.27 0.457 | 64.60±3.16  | 75.13±1.67 |
| --- | ---- | ----- | ----- | ---- | ----------- | ----------- | ---------- |
|     |      |       |       |      |             | 92.41±2.44  | 96.91±1.79 |
|     | WDBC | 97.42 | 97.73 | 0.03 | – –         |             |            |
|     | WPBC | 77.78 | 61.54 | 0.22 | 81.28 –     | 27.38±11.69 | 67.53±3.71 |
Boldindicatesthebestaccuracyvalues
SVMwithRBFkernel.Undertheseconditions,experimen- G-meanvalue.SimilarcasesareontheHepatitisandWPBC
| talevidenceshowsthatouralgorithmfindssimilarresultsor |     |     | datasets. |     |     |     |     |
| ----------------------------------------------------- | --- | --- | --------- | --- | --- | --- | --- |
outperformstheotheralgorithmsproposedintheliterature. Tables 5 and 6 show the results found by Algorithm 1
ThebestresultsintermsofaccuracyonHepatitis,Pima,and on the six datasets along with the related optimized hyper-
WPBCdatasetsarefoundin(YuandWang2017)byoptimiz- parameter configuration. For the Appendicitis dataset, for
ingtheparametersoftheSVMwithRBFkernelbyanovel instance,thebestaccuracyinTable5is f =89.62;thebest
1
ensembledifferentialevolutionapproachthattheyproposed. G-Mean is f = 82.54, and the best average cost is f =
2 3
Severalapproachesweretestedin(Taoetal.2019)andthe 0.11. As expected, the improvement of a fitness function
results were reported in terms of G-Mean. In Table 4, we implies a worsening in the other two. We observe that the
denoted with G-Meana and G-Meanb the values found by singleoptimalfitnessvaluesarefoundwithdifferenthyper-
CS-SVMandtheirself-adaptivecostweights-basedsupport parameter tuning. Moreover, the best results are found in
vector machine cost-sensitive ensemble approach, respec- all the experiments even if number of population size and
tively.Itishelpfultonoticethattheyreportedtheseresults generationnumberisincreased.
onthedatasetsbymodifyingimbalanceddataratioof10:1. Tables 7 and 8 show the results found by Algorithm 2
Tables5,6,7,8listonlysomeofthefoundnon-dominated on the six datasets along with the related optimized hyper-
solutions of the Pareto front of our experimental results. parameter configuration. These results were found in very
These results refer to the experiments carried out with the contracted computational time if compared to the previous
relatedparallelizedversionofAlgorithms1and2.Thefirst ones. Observe that there has been a reduction over 70%
andsecondcolumnofthesetablesreportthepopulationsize in some experiments. These results show that the proposed
and the number of carried out generations; the next three Algorithm2isefficient.
columns show the fitness function values associated with Theresultsevidencedthat:(1)bothalgorithmsconverge
theoptimalhyper-parameterconfiguration,whichisreported andfindthesamebestvaluesforthethreefitnessfunctions;
in thenext four columns. The eleventh and twelfthcolumn (2) the number of optimal non-dominated solutions of the
reportsthesensitivityandspecificityvalues,whereasthenext ParetofrontfoundbyAlgorithm1isgreaterthanthenum-
four columns report the ROC area, the F-Measure, the bal- berfoundbyAlgorithm2.Tobetterunderstandourfinding,
ancedaccuracy,andtheYouden’sindex,respectively.Finally, we illustrate in Figs. 6 and 7 the Pareto points of Tables 7
the last column shows the average computational time, in and 8pereachdatasetwiththesixperformancemeasures.
minutes. The Pareto points are shown considering decreasing Sen-
Asalreadyobservedintheliterature,theaccuracyisnot sitivity.Asdepictedinthesetwofigures,generallybalance
asuitablemeasureforimbalanceddata.Indeed,wenoticed accuracydecreasesasSensitivitydecreaseswhileSensitivity
thatintheHabermandataset,forinstance,thereisahyper- increases.ThebestParetopointsrelatedtomedicaldatasets,
parameterconfigurationthatallowstohaveagoodaccuracy asthosetestedinthispaper,shouldbethepointswithhigh
equal to 75.53%, but the specificity is zero as well as the balanceaccuracyorhighsensitivityvalues.
123

12874 R.Guidoetal.
stesatadsititapeHdna,namrebaH,siticidneppAnostluserlatnemirepxE:1mhtiroglA
5elbaT
emiT
scirtemecnamrofreP
rap-repyHdezimitpO
snoitcnufssentiF
.marap.neG
tesataD
Y
AB
M-F
aeraCOR
cepS
sneS
2C
1C
γ
C
3f
2f
1f
neG
ezispoP
67.0
485.0
297.0
7.0
297.0
569.0
916.0
2
1
10.0
33
81.0
82.77
26.98
001
42
siticidneppA
656.0
828.0
7.0
828.0
498.0
267.0
4
1
83.0
9
72.0
45.28
97.68
635.0
867.0
76.0
867.0
569.0
175.0
1
1
81.0
54
11.0
52.47
86.88
24.1
485.0
297.0
7.0
297.0
569.0
916.0
2
1
81.0
2
81.0
82.77
26.98
002
656.0
828.0
7.0
828.0
498.0
267.0
4
1
83.0
9
72.0
45.28
97.68
635.0
867.0
76.0
867.0
569.0
175.0
1
1
83.0
01
11.0
52.47
86.88
90.7
485.0
297.0
7.0
297.0
569.0
916.0
2
1
81.0
2
81.0
82.77
26.98
0001
656.0
828.0
7.0
828.0
498.0
267.0
4
1
83.0
9
72.0
45.28
97.68
635.0
867.0
76.0
867.0
569.0
175.0
1
1
83.0
51
11.0
52.47
86.88
44.1
485.0
297.0
7.0
297.0
569.0
916.0
2
1
10.0
93
81.0
82.77
26.98
001
84
745.0
377.0
96.0
477.0
679.0
175.0
1
1
21.0
93
1.0
7.47
26.98
656.0
828.0
7.0
828.0
498.0
267.0
4
1
4.0
01
72.0
45.28
97.68
346.0
5128.0
17.0
228.0
929.0
417.0
81
5
10.0
3
3.1
84.18
86.88
38.2
485.0
297.0
7.0
297.0
569.0
916.0
2
1
10.0
62
81.0
82.77
26.98
002
745.0
377.0
96.0
477.0
679.0
175.0
1
1
21.0
93
1.0
7.47
26.98
31.41
485.0
297.0
7.0
297.0
569.0
916.0
2
1
10.0
62
81.0
82.77
26.98
0001
745.0
377.0
96.0
477.0
679.0
175.0
1
1
21.0
93
1.0
7.47
26.98
656.0
828.0
7.0
828.0
498.0
267.0
4
1
4.0
11
72.0
45.28
97.68
14.4
513.0
756.0
94.0
856.0
178.0
444.0
2
1
68.0
94
93.0
22.26
28.57
001
42
namrebaH
823.0
466.0
15.0
466.0
67.0
865.0
31
4
35.0
94
91.2
7.56
29.07
380.0
145.0
2.0
245.0
69.0
321.0
1
1
47.0
84
62.0
34.43
68.37
20.9
513.0
756.0
94.0
856.0
178.0
444.0
2
1
68.0
64
93.0
22.26
28.57
002
233.0
666.0
15.0
666.0
467.0
865.0
31
4
35.0
83
81.2
98.56
42.17
380.0
145.0
2.0
245.0
69.0
321.0
1
1
47.0
92
62.0
34.43
68.37
69.73
513.0
756.0
94.0
856.0
178.0
444.0
2
1
68.0
64
93.0
22.26
28.57
0001
943.0
476.0
25.0
476.0
657.0
395.0
31
4
68.0
31
21.2
19.66
42.17
780.0
5345.0
2.0
445.0
469.0
321.0
1
1
68.0
32
62.0
15.43
81.47
123

Ahyper-parametertuningapproach... 12875
|      |      | 53.31 | 29.66 |           |      |      |      | 68.61 |
| ---- | ---- | ----- | ----- | --------- | ---- | ---- | ---- | ----- |
| emiT | 87.6 |       |       | 49.0 87.1 | 30.9 | 28.1 | 54.3 |       |
353.0 990.0 353.0 990.0 663.0 990.0 126.0 956.0 445.0 126.0 956.0 445.0 186.0 445.0 576.0 125.0 576.0 445.0 186.0 445.0
|     | 23.0 | 23.0 | 80.0 23.0 |     | 36.0 | 36.0 | 36.0 | 36.0 |
| --- | ---- | ---- | --------- | --- | ---- | ---- | ---- | ---- |
Y
5048.0
676.0 945.0 676.0 945.0 386.0 945.0 018.0 928.0 277.0 018.0 928.0 277.0 518.0 048.0 277.0 518.0 738.0 067.0 518.0 738.0 277.0 518.0 277.0
|     | 66.0 | 66.0 | 45.0 66.0 |     |     |     |     |     |
| --- | ---- | ---- | --------- | --- | --- | --- | --- | --- |
AB
M-F 35.0 32.0 35.0 32.0 91.0 35.0 32.0 96.0 86.0 56.0 96.0 86.0 56.0 86.0 56.0 96.0 36.0 96.0 56.0 86.0 56.0
|     | 5.0 | 5.0 | 5.0 |     | 7.0 | 7.0 | 7.0 | 7.0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
aeraCOR
66.0 776.0 55.0 66.0 776.0 55.0 45.0 66.0 386.0 55.0 118.0 928.0 277.0 118.0 928.0 277.0 518.0 148.0 277.0 518.0 738.0 67.0 518.0 738.0 277.0 518.0 148.0 277.0
scirtemecnamrofreP
678.0 117.0 159.0 678.0 117.0 159.0 969.0 678.0 377.0 159.0 209.0 648.0 919.0 209.0 648.0 919.0 119.0 738.0 919.0 119.0 268.0 729.0 119.0 268.0 919.0 119.0 738.0 919.0
cepS
sneS 444.0 246.0 841.0 444.0 246.0 841.0 111.0 444.0 395.0 841.0 917.0 318.0 526.0 917.0 318.0 526.0 917.0 448.0 526.0 917.0 318.0 495.0 917.0 318.0 526.0 917.0 448.0 526.0
2C
|     | 2 7 | 1 2 7 | 1 1 2 31 | 1 2 2 1 2 2 | 1 2 1 | 1 2 2 | 1 2 2 | 1 2 1 1 |
| --- | --- | ----- | -------- | ----------- | ----- | ----- | ----- | ------- |
rap-repyHdezimitpO 1C
|     | 1 2 | 1 1 2 | 1 1 1 4 | 1 3 9 1 3 9 | 1 3 5 | 1 3 7 | 1 3 7 | 1 3 5 1 |
| --- | --- | ----- | ------- | ----------- | ----- | ----- | ----- | ------- |
49.0 24.0 49.0 49.0 24.0 49.0 25.0 49.0 49.0 49.0 10.0 10.0 10.0 10.0 10.0 10.0 10.0 10.0 10.0 10.0 10.0 23.0 10.0 10.0 10.0 10.0 10.0 10.0
γ
C 94 93 94 94 93 94 74 94 2 94 04 8 74 93 8 74 53 8 74 23 01 01 23 01 74 23 8 74
93.0 90.1 62.0 93.0 90.1 62.0 62.0 93.0 70.2 62.0 33.0 95.0 41.0 33.0 95.0 41.0 23.0 92.0 41.0 23.0 94.0 41.0 23.0 94.0 41.0 23.0 92.0 41.0
3f
snoitcnufssentiF 83.26 75.76 45.73 83.26 75.76 45.73 18.23 83.26 45.73 45.08 88.28 87.57 45.08 88.28 87.57 60.48 87.57 86.38 81.47 86.38 87.57 60.48 87.57
|     |     |     | 7.76 |     | 9.08 | 9.08 | 9.08 | 9.08 |
| --- | --- | --- | ---- | --- | ---- | ---- | ---- | ---- |
2f
41.67 82.96 68.37 41.67 82.96 68.37 81.47 41.67 55.27 68.37 54.68 78.38 18.58 54.68 78.38 18.58 78.38 18.58 61.58 18.58 61.58 18.58 78.38 18.58
|     |     |     |     |     | 1.78 | 1.78 | 1.78 | 1.78 |
| --- | --- | --- | --- | --- | ---- | ---- | ---- | ---- |
1f
|     |         |     | 0001 |         | 0001 |     |     | 0001 |
| --- | ------- | --- | ---- | ------- | ---- | --- | --- | ---- |
|     | neG 001 | 002 |      | 001 002 |      | 001 | 002 |      |
.marap.neG
ezispoP
deunitnoc
|     | 84  |     |     | 42  |     | 84  |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
sititapeH
5elbaT tesataD
123

| 12876 |     |     |     |     |     | R.Guidoetal. |
| ----- | --- | --- | --- | --- | --- | ------------ |
Table6 Algorithm1:ExperimentalresultsonthedatasetsPima,WDBC,andWPBC
Dataset Gen.param. Fitnessfunctions OptimizedHyper-par Performancemetrics Time
|             | f1 f2 | f3 γ | C1 C2 |           |             |      |
| ----------- | ----- | ---- | ----- | --------- | ----------- | ---- |
| Popsize Gen |       | C    |       | Sens Spec | ROCarea F-M | BA Y |
Pima 24 100 77.99 72.69 1.46 5 0.24 7 6 0.604 0.874 0.739 0.66 0.739 0.478 10.19
|     | 77.99 70.9  | 0.22 4 0.53 | 1 1 | 0.56 0.898 | 0.729 0.64 | 0.729 0.458 |
| --- | ----------- | ----------- | --- | ---------- | ---------- | ----------- |
|     | 74.35 76.28 | 0.68 5 0.53 | 5 2 | 0.843 0.69 | 0.767 0.7  | 0.766 0.533 |
77.6 71.12 0.22 10 0.53 1 1 0.571 0.886 0.728 0.64 0.728 0.457
200 77.99 72.69 1.46 5 0.24 7 6 0.604 0.874 0.739 0.66 0.739 0.478 20.31
|     | 77.99 70.9  | 0.22 4 0.53 | 1 1 | 0.56 0.898 | 0.729 0.64 | 0.729 0.458 |
| --- | ----------- | ----------- | --- | ---------- | ---------- | ----------- |
|     | 74.35 76.28 | 0.68 5 0.53 | 5 2 | 0.843 0.69 | 0.767 0.7  | 0.766 0.533 |
77.6 71.12 0.22 10 0.53 1 1 0.571 0.886 0.728 0.64 0.728 0.457
1000 77.99 72.69 1.46 5 0.24 7 6 0.604 0.874 0.739 0.66 0.739 0.478 100.99
|     | 77.99 70.9 | 0.22 4 0.53 | 1 1 | 0.56 0.898 | 0.729 0.64 | 0.729 0.458 |
| --- | ---------- | ----------- | --- | ---------- | ---------- | ----------- |
74.87 76.54 0.99 4 0.53 7 3 0.832 0.704 0.768 0.7 0.768 0.536
77.86 71.28 0.22 15 0.53 1 1 0.571 0.89 0.73 0.64 0.730 0.461
48 100 78.13 70.82 0.22 4 0.47 1 1 0.556 0.902 0.729 0.64 0.729 0.458 21.26
74.87 76.54 0.99 4 0.47 7 3 0.832 0.704 0.768 0.7 0.768 0.536
77.86 71.28 0.22 19 0.47 1 1 0.571 0.89 0.73 0.64 0.730 0.461
200 78.13 70.82 0.22 4 0.47 1 1 0.556 0.902 0.729 0.64 0.729 0.458 41.87
74.87 76.54 0.99 4 0.47 7 3 0.832 0.704 0.768 0.7 0.768 0.536
77.86 71.28 0.22 19 0.47 1 1 0.571 0.89 0.73 0.64 0.730 0.461
1000 78.13 70.82 0.22 4 0.47 1 1 0.556 0.902 0.729 0.64 0.729 0.458 210.71
78.13 72.34 2.11 4 0.47 10 9 0.593 0.882 0.738 0.65 0.737 0.475
74.87 76.54 0.99 4 0.47 7 3 0.832 0.704 0.768 0.7 0.768 0.536
77.99 71.51 0.22 18 0.47 1 1 0.575 0.89 0.732 0.65 0.732 0.465
WDBC 24 100 97.42 97.73 0.06 10 0.42 2 5 0.988 0.967 0.977 0.96 0.9775 0.955 2.26
97.14 97.7 0.03 6 0.42 1 5 0.996 0.959 0.977 0.96 0.9775 0.955
200 97.42 97.73 0.06 10 0.42 2 5 0.988 0.967 0.977 0.96 0.9775 0.955 7.49
97.14 97.7 0.03 6 0.42 1 5 0.996 0.959 0.977 0.96 0.9775 0.955
1000 97.42 97.73 0.06 8 0.42 2 5 0.988 0.967 0.977 0.96 0.9775 0.955 30.76
97.28 97.53 0.03 5 0.42 1 2 0.983 0.967 0.975 0.96 0.975 0.95
48 100 97.42 97.73 0.03 8 0.09 1 3 0.988 0.967 0.977 0.96 0.9775 0.955 9.44
200 97.42 97.73 0.03 8 0.09 1 3 0.988 0.967 0.977 0.96 0.9775 0.955 11.8
1000 97.42 97.73 0.03 8 0.09 1 3 0.988 0.967 0.977 0.96 0.9775 0.955 50.86
WPBC 24 100 77.78 29.08 0.24 38 0.24 1 4 0.085 0.993 0.539 0.15 0.539 0.078 1.65
69.7 61.05 0.55 1 0.24 3 1 0.489 0.762 0.625 0.43 0.6255 0.251
|     | 76.77 14.59 | 0.23 38 0.24 | 1 5 | 0.021 1 | 0.511 0.04 | 0.5105 0.021 |
| --- | ----------- | ------------ | --- | ------- | ---------- | ------------ |
200 77.78 29.08 0.24 44 0.24 1 4 0.085 0.993 0.539 0.15 0.539 0.078 3.25
|     | 77.78 25.26 | 0.22 32 0.42 | 1 8 | 0.064 1 | 0.532 0.12 | 0.532 0.064 |
| --- | ----------- | ------------ | --- | ------- | ---------- | ----------- |
69.7 61.05 0.55 1 0.24 3 1 0.489 0.762 0.625 0.43 0.6255 0.251
1000 77.78 29.08 0.24 18 0.42 1 4 0.085 0.993 150 0.15 0.539 0.078 16.17
|     | 77.78 25.26 | 0.22 32 0.42 | 1 8 | 0.064 1     | 151 0.12 | 0.532 0.064  |
| --- | ----------- | ------------ | --- | ----------- | -------- | ------------ |
|     | 69.7 61.05  | 0.55 1 0.24  | 3 1 | 0.489 0.762 | 115 0.43 | 0.6255 0.251 |
123

Ahyper-parametertuningapproach... 12877
Table6 continued
Dataset Gen.param. Fitnessfunctions OptimizedHyper-par Performancemetrics Time
Popsize Gen f1 f2 f3 C γ C1 C2 Sens Spec ROCarea F-M BA Y
48 100 77.78 25.26 0.22 47 0.33 1 9 0.064 1 0.532 0.12 0.532 0.064 3.15
77.78 29.08 0.24 32 0.32 1 5 0.085 0.993 0.539 0.15 0.539 0.078
68.69 61.54 1.75 46 0.01 10 3 0.511 0.742 0.626 0.44 0.6265 0.253
200 77.78 29.08 0.24 33 0.32 1 5 0.085 0.993 0.539 0.15 0.539 0.078 6.34
77.78 25.26 0.22 33 0.32 1 6 0.064 1 0.532 0.12 0.532 0.064
68.69 61.54 1.75 44 0.01 10 3 0.511 0.742 0.626 0.44 0.6265 0.253
1000 77.78 29.08 0.23 21 0.32 1 3 0.085 0.993 0.539 0.15 0.539 0.078 31.85
77.78 25.26 0.22 33 0.32 1 6 0.064 1 0.532 0.12 0.532 0.064
68.69 61.54 1.75 48 0.01 10 3 0.511 0.742 0.626 0.44 0.6265 0.253
Table7 Algorithm2:ExperimentalresultsonthedatasetsAppendicitis,Haberman,andHepatitis
Dataset Gen.param. Fitnessfunctions OptimizedHyper-par Performancemetrics Time
Popsize Gen f1 f2 f3 C γ C1 C2 Sens Spec ROCarea F-M BA Y
Appendicitis 24 100 89.62 77.28 0.18 23 0.01 1 2 0.619 0.965 0.792 0.7 0.792 0.584 0.37
86.79 80.44 0.3 10 0.01 1 4 0.714 0.906 0.81 0.68 0.81 0.62
84.91 60.62 0.15 24 0.01 1 1 0.381 0.965 0.673 0.5 0.673 0.346
200 89.62 77.28 0.36 35 0.01 2 4 0.619 0.965 0.792 0.7 0.792 0.584 0.55
86.79 82.54 0.32 28 0.13 1 5 0.762 0.894 0.828 0.7 0.828 0.656
1000 89.62 77.28 0.18 38 0.01 1 2 0.619 0.965 0.792 0.7 0.792 0.584 1.94
87.74 80.96 0.29 8 0.01 1 4 0.714 0.918 0.816 0.7 0.816 0.632
48 100 89.62 77.28 0.36 29 0.01 2 4 0.619 0.965 0.792 0.7 0.792 0.584 0.61
87.74 80.96 0.29 29 0.01 1 4 0.714 0.918 0.816 0.7 0.816 0.632
86.79 67.78 0.13 36 0.01 1 1 0.476 0.965 0.72 0.59 0.720 0.441
200 89.62 77.28 0.18 11 0.01 1 2 0.619 0.965 0.792 0.7 0.792 0.584 0.91
86.79 82.54 1.19 9 0.47 4 18 0.762 0.894 0.828 0.7 0.828 0.656
1000 89.62 77.28 0.18 18 0.01 1 2 0.619 0.965 0.792 0.7 0.792 0.584 3.07
87.74 80.96 0.29 8 0.01 1 4 0.714 0.918 0.816 0.7 0.816 0.632
84.91 57.05 0.15 22 0.01 1 1 0.333 0.976 0.655 0.47 0.654 0.309
Haberman 24 100 76.14 62.38 0.39 42 1 1 2 0.444 0.876 0.66 0.5 0.66 0.32 1.82
68.3 66.49 1.12 11 1 2 7 0.63 0.702 0.666 0.51 0.666 0.332
73.53 0 0.26 23 0.94 2 1 0 1 0.5 0 0.5 0
200 76.14 57.81 1.38 29 0.12 3 7 0.37 0.902 0.636 0.45 0.636 0.272 3.8
67.32 66.29 1.13 3 0.94 2 7 0.642 0.684 0.663 0.51 0.663 0.326
75.82 62.22 0.39 42 0.94 1 2 0.444 0.871 0.658 0.49 0.657 0.315
1000 76.14 62.38 0.39 35 0.94 1 2 0.444 0.876 0.66 0.5 0.66 0.32 19.47
70.92 67.21 1.6 11 0.94 3 10 0.605 0.747 0.676 0.52 0.676 0.352
73.86 37.54 0.26 49 0.94 1 1 0.148 0.951 0.55 0.23 0.549 0.099
48 100 76.14 62.38 0.39 49 0.94 1 2 0.444 0.876 0.66 0.5 0.66 0.32 4.29
68.95 67.35 1.09 15 0.63 2 7 0.642 0.707 0.674 0.52 0.674 0.349
73.86 37.54 0.26 49 0.94 1 1 0.148 0.951 0.55 0.23 0.549 0.099
200 76.14 62.38 0.39 49 0.94 1 2 0.444 0.876 0.66 0.5 0.66 0.32 6.74
69.28 67.57 1.09 24 0.63 2 7 0.642 0.711 0.677 0.53 0.676 0.353
73.86 34.43 0.26 49 0.56 1 1 0.123 0.96 0.542 0.2 0.541 0.083
123

| 12878 |     |     |     |     |     | R.Guidoetal. |
| ----- | --- | --- | --- | --- | --- | ------------ |
Table7 continued
Dataset Gen.param. Fitnessfunctions OptimizedHyper-par Performancemetrics Time
| Popsize Gen | f1 f2 | f3 C γ | C1 C2 | Sens Spec | ROCarea F-M | BA Y |
| ----------- | ----- | ------ | ----- | --------- | ----------- | ---- |
1000 76.14 62.38 0.39 34 0.94 1 2 0.444 0.876 0.66 0.5 0.66 0.32 27.73
|     | 69.61 67.33 | 2.7 9 1      | 5 17 | 0.63 0.72 | 0.675 0.52 | 0.675 0.35 |
| --- | ----------- | ------------ | ---- | --------- | ---------- | ---------- |
|     | 73.53 0     | 0.26 10 0.94 | 7 1  | 0 1       | 0.5 0      | 0.5 0      |
Hepatitis 24 100 87.1 79.47 0.45 28 0.01 4 3 0.688 0.919 0.803 0.69 0.803 0.607 0.4
83.23 82.49 0.61 6 0.01 9 2 0.813 0.837 0.825 0.67 0.825 0.65
83.23 67.78 0.17 28 0.01 1 1 0.5 0.919 0.709 0.55 0.709 0.419
200 87.1 80.9 0.32 32 0.01 3 2 0.719 0.911 0.815 0.7 0.815 0.63 0.58
83.23 82.49 0.61 6 0.01 9 2 0.813 0.837 0.825 0.67 0.825 0.65
84.52 71.89 0.15 32 0.01 1 1 0.563 0.919 0.741 0.6 0.741 0.482
1000 87.1 80.9 0.32 35 0.01 3 2 0.719 0.911 0.815 0.7 0.815 0.63 1.9
83.87 84.06 0.29 8 0.01 5 1 0.844 0.837 0.841 0.68 0.840 0.681
|     | 79.35 0 | 0.21 8 0.01 | 1 3 | 0 1 | 0.5 0 | 0.5 0 |
| --- | ------- | ----------- | --- | --- | ----- | ----- |
48 100 86.45 80.54 0.33 13 0.02 3 2 0.719 0.902 0.811 0.69 0.810 0.621 0.74
83.23 83.65 0.59 7 0.01 10 2 0.844 0.829 0.837 0.68 0.836 0.673
85.81 74.18 0.14 26 0.02 1 1 0.594 0.927 0.76 0.63 0.760 0.521
200 87.1 80.9 0.32 35 0.01 3 2 0.719 0.911 0.815 0.7 0.815 0.63 1.1
81.94 81.68 0.71 15 0.01 11 2 0.813 0.821 0.817 0.65 0.817 0.634
84.52 71.89 0.15 34 0.01 1 1 0.563 0.919 0.741 0.6 0.741 0.482
1000 87.1 80.9 0.32 32 0.01 3 2 0.719 0.911 0.815 0.7 0.815 0.63 4.03
83.87 84.06 0.29 8 0.01 5 1 0.844 0.837 0.841 0.68 0.840 0.681
84.52 71.89 0.15 34 0.01 1 1 0.563 0.919 0.741 0.6 0.741 0.482
Table8 Algorithm2:ExperimentalresultsonthedatasetsPima,WDBC,andWPBC
Dataset Gen.param. Fitnessfunctions OptimizedHyper-par Performancemetrics Time
γ
| Popsize Gen | f1 f2 | f3 C | C1 C2 | Sens Spec | ROCarea F-M | BA Y |
| ----------- | ----- | ---- | ----- | --------- | ----------- | ---- |
Pima 24 100 77.73 73.2 1.02 5 0.24 5 4 0.623 0.86 0.742 0.66 0.741 0.483 7.8
|     | 74.35 76.28 | 0.68 5 0.53 | 5 2 | 0.843 0.69 | 0.767 0.7 | 0.766 0.533 |
| --- | ----------- | ----------- | --- | ---------- | --------- | ----------- |
77.08 70.34 0.23 23 0.32 1 1 0.56 0.884 0.722 0.63 0.722 0.444
77.47 70.26 0.23 23 0.24 1 1 0.552 0.894 0.723 0.63 0.723 0.446
200 77.99 70.9 0.44 4 0.53 2 2 0.56 0.898 0.729 0.64 0.729 0.458 12.41
|     | 74.35 76.28 | 0.68 5 0.53 | 5 2 | 0.843 0.69 | 0.767 0.7 | 0.766 0.533 |
| --- | ----------- | ----------- | --- | ---------- | --------- | ----------- |
74.74 58.03 0.28 5 0.53 1 2 0.351 0.96 0.655 0.49 0.655 0.311
1000 77.47 70.89 0.45 48 0.24 2 2 0.567 0.886 0.727 0.64 0.726 0.453 52.83
77.47 70.1 0.23 12 0.24 1 1 0.549 0.896 0.722 0.63 0.722 0.445
74.48 76.33 0.68 48 0.13 5 2 0.84 0.694 0.767 0.7 0.767 0.534
48 100 78.13 71.13 0.22 3 0.63 1 1 0.563 0.898 0.731 0.64 0.730 0.461 9.86
|     | 74.35 76.28 | 0.68 3 0.58 | 5 2 | 0.843 0.69 | 0.767 0.7 | 0.766 0.533 |
| --- | ----------- | ----------- | --- | ---------- | --------- | ----------- |
200 78.13 71.13 0.22 3 0.63 1 1 0.563 0.898 0.731 0.64 0.730 0.461 15.34
75.13 75.44 0.33 10 0.42 2 1 0.765 0.744 0.754 0.68 0.754 0.509
|     | 74.35 76.22 | 0.68 2 0.63 | 5 2 | 0.84 0.692 | 0.766 0.7 | 0.766 0.532 |
| --- | ----------- | ----------- | --- | ---------- | --------- | ----------- |
1000 78.13 71.13 0.22 3 0.63 1 1 0.563 0.898 0.731 0.64 0.730 0.461 62.73
78.13 72.34 2.11 1 0.63 10 9 0.593 0.882 0.738 0.65 0.737 0.475
74.22 75.93 0.7 3 0.42 5 2 0.828 0.696 0.762 0.69 0.762 0.524
123

Ahyper-parametertuningapproach... 12879
Table8 continued
Dataset Gen.param. Fitnessfunctions OptimizedHyper-par Performancemetrics Time
Popsize Gen f1 f2 f3 C γ C1 C2 Sens Spec ROCarea F-M BA Y
WDBC 24 100 97.42 97.73 0.09 19 0.24 3 7 0.988 0.967 0.977 0.96 0.977 0.955 0.87
97.14 97.7 0.04 4 0.18 1 7 0.996 0.959 0.977 0.96 0.977 0.955
200 97.42 97.73 0.09 19 0.24 3 7 0.988 0.967 0.977 0.96 0.977 0.955 2.59
97.28 97.43 0.04 4 0.01 1 3 0.979 0.969 0.974 0.96 0.974 0.948
97.14 97.7 0.04 4 0.18 1 7 0.996 0.959 0.977 0.96 0.977 0.955
1000 97.42 97.73 0.09 14 0.24 3 7 0.988 0.967 0.977 0.96 0.977 0.955 13.77
97.14 97.7 0.03 14 0.24 1 4 0.996 0.959 0.977 0.96 0.977 0.955
48 100 97.42 97.73 0.09 19 0.24 3 7 0.988 0.967 0.977 0.96 0.977 0.955 2.52
97.28 97.43 0.04 4 0.01 1 3 0.979 0.969 0.974 0.96 0.974 0.948
97.14 97.7 0.04 4 0.18 1 7 0.996 0.959 0.977 0.96 0.977 0.955
200 97.42 97.73 0.09 19 0.24 3 7 0.988 0.967 0.977 0.96 0.977 0.955 5.37
97.28 97.43 0.04 4 0.01 1 3 0.979 0.969 0.974 0.96 0.974 0.948
97.14 97.7 0.04 4 0.18 1 7 0.996 0.959 0.977 0.96 0.977 0.955
1000 97.42 97.73 0.16 16 0.27 5 12 0.988 0.967 0.977 0.96 0.977 0.955 25.72
97.14 97.13 0.03 4 0.27 1 1 0.971 0.972 0.971 0.96 0.971 0.943
WPBC 24 100 76.26 0 0.24 49 0.01 1 1 0 1 0.5 0 0.5 0 0.96
69.19 60.78 0.55 1 0.18 3 1 0.489 0.755 0.622 0.43 0.622 0.244
200 77.27 48.83 3.36 9 0.01 17 7 0.255 0.934 0.595 0.35 0.594 0.189 1.61
65.15 62.29 2.95 5 0.01 17 5 0.574 0.675 0.625 0.44 0.624 0.249
76.26 0 0.24 42 0.01 1 7 0 1 0.5 0 0.5 0
1000 77.27 48.83 3.36 9 0.01 17 7 0.255 0.934 0.595 0.35 0.594 0.189 4.47
65.15 62.29 2.95 5 0.01 17 5 0.574 0.675 0.625 0.44 0.624 0.249
76.26 0 0.24 5 0.01 1 9 0 1 0.5 0 0.5 0
48 100 76.26 0 0.24 41 0.09 1 2 0 1 0.5 0 0.5 0 1.77
76.26 55.17 0.39 14 0.09 2 1 0.34 0.894 0.617 0.41 0.617 0.234
200 77.78 29.08 0.25 49 0.27 1 6 0.085 0.993 0.539 0.15 0.539 0.078 2.64
77.78 25.26 0.22 48 0.27 1 7 0.064 1 0.532 0.12 0.532 0.064
67.17 60.71 3.04 47 0.01 17 5 0.511 0.722 0.616 0.42 0.616 0.233
1000 76.26 0 0.24 28 0.01 1 7 0 1 0.5 0 0.5 0 8.55
65.15 59.59 3.25 37 0.01 18 5 0.511 0.695 0.603 0.41 0.603 0.206
7 Conclusion or equivalent to other algorithms proposed in the literature
forCS-SVMhyper-parametersoptimization.Overall,taking
SupportvectormachinesareoneofthebestMLmodelsfor intoaccountthreepredictivemetrics,i.e.,accuracy,G-Mean,
solvingseveralreal-lifeclassificationproblems.However,as and average cost,thebest hyper-parameter configuration is
inotherMLtechniques,theirperformancedependsonhyper- foundinshortcomputationaltime,mainlyifcomparedwith
parameters. gridsearchapproach.Hence,thisapproachcanbeconsidered
In this paper, we have investigated and proposed an asagoodsolutionforaddressingimbalanceddatasetclassi-
approachthatcombinesgeneticalgorithmsanddecisiontrees ficationandhyper-parametertuning,astheyarechallenging
tooptimizehyper-parametersofC-SVMs.Theoptimumval- problemsinclassificationresearch.
uesoftheregularizationparameter,costsofclassesandthe We suggest evaluating the performance of classifiers on
parametersoftheRBFkernelfunctionaresearchedforSVM. medicaldatabysuitablemeasuresotherthanaccuracy.Our
Wetestedthealgorithmonsixbenchmarkdatasets,which future work is to extend and assess the proposed approach
areimbalanced.Weevaluatedtheperformanceofthemod- to investigate hyper-parameter tuning of different machine
elsbyseveralperformancemetrics.Theframeworkisbetter learningmethods.
123

12880 R.Guidoetal.
Fig.6 ValuesofthesixperformancemeasuresoftheParetopointsfoundforAppendicitis,Haberman,Hepatitis,andPimadatasets
Fig.7 ValuesofthesixperformancemeasuresoftheParetopointsfoundforWDBCandWPBCdatasets
Acknowledgements Theresearchhasbeenpartiallysupportedbythe professionalrelationships,affiliations,knowledgeorbeliefs)inthesub-
researchprojectSI.F.I.PA.CRO.DE.Sviluppoeindustrializzazionefar- jectmatterormaterialsdiscussedinthismanuscript.
maci innovativi per terapia molecolare personalizzata PA.CRO.DE.
(PON ARS01_00568, CUP: B29C20000360005, CONCESSIONE Open Access This article is licensed under a Creative Commons
RNA-COR: 4646672), Italian Ministry of University and Research, Attribution4.0InternationalLicense,whichpermitsuse,sharing,adap-
2021. tation, distribution and reproduction in any medium or format, as
long as you give appropriate credit to the original author(s) and the
Declaration source, provide a link to the Creative Commons licence, and indi-
cateifchangesweremade.Theimagesorotherthirdpartymaterial
inthisarticleareincludedinthearticle’sCreativeCommonslicence,
Conflictofinterest Theauthorsofthemanuscriptdeclarethattheyhave
unlessindicatedotherwiseinacreditlinetothematerial.Ifmaterial
noaffiliationswithorinvolvementinanyorganizationorentitywith
is not included in the article’s Creative Commons licence and your
any financial interest (such as honoraria; educational grants; partici-
intended use is not permitted by statutory regulation or exceeds the
pationinspeakers’bureaus;membership,employment,consultancies,
permitteduse,youwillneedtoobtainpermissiondirectlyfromthecopy-
stockownership,orotherequityinterest;andexperttestimonyorpatent-
rightholder.Toviewacopyofthislicence,visithttp://creativecomm
licensingarrangements),ornon-financialinterest(suchaspersonalor
ons.org/licenses/by/4.0/.
123

Ahyper-parametertuningapproach... 12881
References LessmannS,StahlbockR,CroneR(2005)Optimizinghyperparameters
ofsupportvectormachinesbygeneticalgorithms.In:IC-AIpp
AgrawalN,KumarA,BajajV(2017)Anewdesignmethodforstable 74–82
IIRfilterswithnearlylinear-phaseresponsebasedonfractional MehrbakhshN,HosseinA,LeilaSetal(2019)Apredictivemethodfor
derivativeandswarmintelligence.IEEETransactionsonEmerging hepatitisdiseasediagnosisusingensemblesofneuro-fuzzytech-
TopicsinComputationalIntelligence1(6):464–477 nique.JInfectPublicHealth12(1):13–20
AgrawalN,KumarA,BajajV(2018)DesignofdigitalIIRfilterwith NoiaA,MartinoA,MontanariPetal(2020)Supervisedmachinelearn-
lowquantizationerrorusinghybridoptimizationtechnique.Soft ingtechniquesandgeneticoptimizationforoccupationaldiseases
Comput22(9):2953–2971 riskprediction.SoftComput24:4393–4406
AminA,AnwarS,AeaAdnan(2016)Comparingoversamplingtech- PhienthrakulT,KijsirikulB(2010)Evolutionarystrategiesforhyper-
niquestohandletheclassimbalanceproblem:acustomerchurn parametersofsupportvectormachinesbasedonmulti-scaleradial
predictioncasestudy.IEEEAccess4:7940–7957 basisfunctionkernels.SoftComput14:681–699
Bao-DeL,Xin-YangZ,MeiZetal(2021)Improvedgeneticalgorithm- QiZ,TianaY,ShiaYetal(2013)Cost-sensitivesupportvectormachine
based research on optimization of least square support vec- forsemi-supervisedlearning.ProcediaComputSci18:1684–1689
tor machines: an application of load forecasting. Soft Comput RamírezA,RomeroJR,VenturaS(2015)AnextensibleJCLEC-based
10(1007):5674–9 solution for the implementation of multi-objective evolutionary
BergstraJ,BardenetR,BengioY,etal(2011)Algorithmsforhyper- algorithms.In:proceedingsofthecompanionpublicationofthe
parameteroptimization.In:andCAI(ed)Proceedingsofthe24th 2015annualconferenceongeneticandevolutionarycomputation,
international conference on neural information processing sys- pp1085–1092
tems.USA,pp2546–2554 RamírezA,RomeroJR,García-MartínezCetal(2019)JCLEC-MO:
BreimanL,FriedmanJH,OlshenR,etal(1984)R.A.andStone,C.J. ajavasuiteforsolvingmany-objectiveoptimizationengineering
Classificationandregressiontrees.CRCpress problems.EngApplArtifIntell81:14–28
ChawlaN,BowyerK,LeaHall(2002)Smote:Syntheticminorityover- ScholkopfB,SmolaAJ(2001)LearningwithKernels:SupportVector
samplingtechnique.JArtifIntellRes16:321–357 Machines,Regularization,Optimization,andBeyond.MITPress,
Cortes C, Vapnik V (1995) Support-vector network. Mach Learn Cambridge,MA,USA
20:273–297 Sokolova M, Japkowicz N, Szpakowicz S (2006) Beyond accuracy,
CristianiniN,Shawe-TaylorJ(2000)AnIntroductiontoSupportVector F-score and ROC: A family of discriminant measures for per-
Machines and other kernel-based learning methods. Cambridge formance evaluation. In: Sattar A, Kang B (eds) Advances in
UniversityPress Artificial Intelligence. Lecture Notes in Computer Science, vol
DattaS,DasS(2015)Near-bayesiansupportvectormachinesforimbal- 4304.Springer,Berlin,Heidelberg
anceddataclassificationwithequalorunequalmisclassification SrinivasN,DebK(1994)Multiobjectiveoptimizationusingnondomi-
costs.NeuralNetw70:39–52 natedsortingingeneticalgorithms.EvolComput2(3):221–248
DebK,GoelT(2001)Controlledelitistnon-dominatedsortinggenetic Tao X, Li Q, Guo W et al (2019) Self-adaptive cost weights-based
algorithms for better convergence. In: Lothar T, Kalyanmoy D, support vector machine cost-sensitive ensemble for imbalanced
CoelloCetal(eds)ZitzlerEckart.EvolutionaryMulti-Criterion dataclassification.InfSci487:31–56
Optimization,Springer,BerlinHeidelberg,pp67–81 TurneyPD(1995)Cost-sensitiveclassification:empiricalevaluationof
DebK,PratapA,AgarwalSetal(2002)Afastandelitistmultiobjective ahybridgeneticdecisiontreeinductionalgorithm.JArtifIntRes
geneticalgorithm:NSGA-II.IEEETransEvolComput6:182–197 2:369–409
Dwivedi AK, Ghosh S, Londhe ND (2018) Review and analysis of VapnikV(1998)StatisticalLearningTheory.Wiley,JohnSonsInc
evolutionary optimization-based techniques for fir filter design. Veropoulos K, Campbell C, Cristianini N (1999) Controlling the
CircuitsSystSignalProcess37(10):4409–4430 sensitivityofsupportvectormachines.In:proceedingsoftheinter-
GalarM,FernandezA,BarrenecheaEetal(2012)Areviewonensem- nationaljointconferenceonAL,pp55–60
bles for the class imbalance problem: Bagging, boosting, and WittenI,FrankE(2005)DataMiningPracticalMachineLearningTools
hybrid-basedapproaches,systems,man,andcybernetics,partc: andTechniques.MorganKaufmannPublishers,CA
Applicationsandreviews.IEEETrans42(4):463–484 YuX,WangX(2017)Anovelhybridclassificationframeworkusing
GoldbergDE,HollandJ(1988)Geneticalgorithmsandmachinelearn- svmanddifferentialevolution.SoftComput21:4029–4044
ing.MachLearn3(2):95–99
GuidoR,ConfortiD(2017)Hybridgeneticapproachforsolvingan
Publisher’sNote SpringerNatureremainsneutralwithregardtojuris-
integratedmulti-objectiveoperatingroomplanningandscheduling
dictionalclaimsinpublishedmapsandinstitutionalaffiliations.
problem.ComputOperRes87:270–282
GuidoR,GrocciaMC,ConfortiD(2021)Hyper-ParameterOptimiza-
tion in Support Vector Machine on unbalanced datasets using
GeneticAlgorithms.In:OptimizationinArtificialIntelligenceand
DataSciences,AIROSpringerSeries(inpress)
HofmannT,ScholkopfB,SmolaAJ(2008)Kernelmethodsinmachine
learning.AnnStatistpp1171–1220
Holland JH (1975) Adaptation in natural and artificial systems: An
introductory analysis with applications to biology, control, and
artificialintelligence.MichiganPress
IranmehrA,Masnadi-ShiraziH,VasconcelosN(2019)Cost-sensitive
supportvectormachines.Neurocomputing343:50–64
JapkowiczN,StephenS(2002)Theclassimbalanceproblem:asys-
tematicstudy.IntellDataAnal6:429–449
JoT,JapkowiczN(2004)Classimbalancesversussmalldisjuncts.ACM
SIGKDDExplorationsNewslett6:40–49
123