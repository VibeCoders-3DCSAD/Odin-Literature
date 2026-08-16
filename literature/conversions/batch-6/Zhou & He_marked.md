---
conversion_metadata:
  converted_at: "2026-07-21T10:07:16Z"
  converter_tool: "markitdown"
  converter_version: "0.1.6"
  source_pdf: "Zhou & He.pdf"
  source_pdf_sha256: "2de265aa97cc6aff2e7edb4661c9f8cf9eaa3ef681efb8a399ac8a1ddb90c298"
  page_count: 35
  markdown_char_count: 264307
---

<!-- PAGE-AWARE EXTRACTION (via pdfminer.six) -->

<!-- PAGE 1 -->

Rare Category Analysis for Complex Data: A Review

DAWEI ZHOU, Virginia Tech
JINGRUI HE, University of Illinois at Urbana-Champaign

Though the sheer volume of data that is collected is immense, it is the rare categories that are often the most
important in many high-impact domains, ranging from financial fraud detection in online transaction net-
works to emerging trend detection in social networks, from spam image detection on social media platforms
to rare disease diagnosis in medical decision support systems. The unique challenges of rare category analysis
include (1) the highly skewed class distribution; (2) the non-separable nature of the rare categories from the
majority classes; (3) data and task heterogeneity; and (4) the time-evolving property of the input data sources.
This survey reviews state-of-the-art techniques used in complex rare category analysis, where the majority
classes have a smooth distribution while the minority classes exhibit the compactness property in the feature
space or subspace. Rare category analysis aims to identify, characterize, represent, and interpret anomalies
that not only show statistical significance but also exhibit interesting patterns (e.g., compactness, high-order
structures, showing in a burst). We introduce our study, define the problem setting, and describe the unique
challenges of complex rare category analysis. We then present a comprehensive review of recent advances
that are designed for this problem setting, from rare category exploration without any label information to
rare category exposition that characterizes rare examples with a compact representation, from the represen-
tation of rare patterns in a salient embedding space to the interpretation the prediction results and providing
relevant clues for the end-users’ interpretation. Finally we discuss potential challenges and shed light on the
future directions for complex rare category analysis.1

CCS Concepts: • Information systems → Data mining;

Additional Key Words and Phrases: Rare category analysis, imbalanced data distribution, anomaly detection

ACM Reference format:
Dawei Zhou and Jingrui He. 2023. Rare Category Analysis for Complex Data: A Review. ACM Comput. Surv.
56, 5, Article 123 (November 2023), 35 pages.
https://doi.org/10.1145/3626520

1This work was primarily completed during the first author’s PhD studies at the University of Illinois at Urbana-Champaign.

This work is supported by National Science Foundation under Awards No. IIS-1947203, IIS-2002540, IIS-2137468, and IIS-
2117902. The views and conclusions are those of the authors and should not be interpreted as representing the official
policies of the funding agencies or the government.
Authors’ addresses: D. Zhou, Computer Science, Virginia Tech, 620 Drillfield Dr., Blacksburg, VA, 24060; e-mail:
zhoud@vt.edu; J. He, Information Science, University of Illinois at Urbana-Champaign, 501 E. Daniel St, Champaign, IL,
61820-6211; e-mail: jingrui@illinois.edu.
Permission to make digital or hard copies of all or part of this work for personal or classroom use is granted without fee
provided that copies are not made or distributed for profit or commercial advantage and that copies bear this notice and
the full citation on the first page. Copyrights for components of this work owned by others than the author(s) must be
honored. Abstracting with credit is permitted. To copy otherwise, or republish, to post on servers or to redistribute to lists,
requires prior specific permission and/or a fee. Request permissions from permissions@acm.org.
© 2023 Copyright held by the owner/author(s). Publication rights licensed to ACM.
0360-0300/2023/11-ART123 $15.00
https://doi.org/10.1145/3626520

ACM Computing Surveys, Vol. 56, No. 5, Article 123. Publication date: November 2023.

123

---

<!-- PAGE 2 -->

123:2

1 INTRODUCTION

D. Zhou and J. He

The so-called era of big data is defined in part by the sheer volume of multimodel data that are
being collected from various platforms (e.g., graphs, images, text). Yet, it is the rare occurrences—
those data points that are significantly different from other observations in the data—that often
are of greatest importance in many high-impact domains: from financial fraud detection in online
transaction networks to emerging trend detection in social networks, from spam image detection
on social media platforms to rare disease diagnosis in medical decision support systems. Anomaly
detection refers to the process by which these rare occurrences are identified. Many techniques
have been proposed to characterize anomalies in domains such as financial fraud detection [102],
insider threat prediction [66], novelty detection [92], gene disease discovery [17], emerging trend
tracking [28], network intrusion detection [58], astronomy [133], spam image detection [93], and
rare disease diagnosis [117].

1.1 Anomalies vs. Rare Category Examples
The branch of data mining concerned with identifying anomalies or outliers2 has a lengthy history.
In 1980, Douglas M. Hawkins proposed the definition of outliers [47] that is shown in Definition 1.1.
Since this time, the problem of anomaly detection or outlier detection has been generalized and
studied in various contexts, such as those of high-dimensional numerical data [173], sequential
data [27], time-series data [45], graph data [7], and financial data [36, 113]. This wide-ranging
exploration has yielded many domain-specific terms for outliers, including novelties events, sur-
prising changes, frauds outbreak.

Definition 1.1. Hawkins’s Definition of Outliers [47]

An outlier is an observation that differs so much from other observations as to arouse sus-
picion that it was generated by a different mechanism.

Though researchers have had tremendous success applying anomaly detection methods in var-
ious domains, not all anomalies detected are necessarily useful or relevant to the actual events of
interest. In fact, most anomalies are uninteresting data points that either are drawn from a known
distribution of noise or correspond to combinations of features that are irrelevant to downstream
applications [109]. For instance, in Figure 1, we present a set of sky images captured by ground-
based telescopes as part of the Sloan Digital Sky Survey (program).3 According to the Sloan
Digital Sky Survey 99.9% of its captured sky images (e.g., the top row of Figure 1) can be well
explained based on known phenomena of the universe (e.g., discovered stars, comets, nebulae);
only 0.1% of the images (e.g., the bottom row of Figure 1) are anomalies. Moreover, among the
anomalies, 99% of the images (e.g., bottom left image in Figure 1) are of no interest to astronomers
and are caused by diffraction spikes of satellite trails or artifacts of the telescope. Only 1% of the
instances (a minuscule 0.001% of the Sloan Digital Sky Survey database) are useful and may lead
to new scientific discoveries (e.g., the bottom right image in Figure 1). Here, we refer to anomalies
that are not only statistically significant but also interesting as rare category examples and the
problem of studying rare category examples as rare category analysis. Figure 2 illustrates the
relationship among anomalies, uninteresting anomalies, and useful anomalies (i.e., rare category
examples), where rare category examples are a subset of anomalies that are not only statistically
significant but also compact in the feature space.

We provide the following general definition of rare category analysis: Given a dataset D of n
−→
0

examples that come from C distinct classes, without loss of generality, we assume that

(cid:2)
n

i=1 xi =

2In this article, we use “anomalies” and “outliers” interchangeably.
3http://www.sdss.org/iotw/archive.html

ACM Computing Surveys, Vol. 56, No. 5, Article 123. Publication date: November 2023.

---

<!-- PAGE 3 -->

Rare Category Analysis for Complex Data: A Review

123:3

Fig. 1. Anomalies in Sloan data [109]. Top row: known objects. Bottom row: anomalies, 99% of which are
uninteresting patterns, such as diffraction spikes (bottom left) and only 1% of which are interesting pat-
terns that are worthy of future research and may lead to the discovery of extraordinary objects (bottom
right).

Fig. 2. Relationship between anomalies/outliers and rare category examples.

(cid:2)
n

i=1(x j

i )2 = 1, where x j

and 1
i denotes the jth feature of xi . For the sake of simplicity, we assume
n
the class label for the ith node, yi = 0, corresponds to the majority class (i.e., normal examples)
and yi ∈ {1, . . . , C − 1} corresponds to the rare categories (i.e., suspicious examples). Note that
rare category analysis is the problem of studying patterns in the minority classes.4 In particular,
for cases in which more than one majority class is observed, we treat all the majority classes as a
single class once the underlying distribution of each majority class is sufficiently smooth [49]. In
general rare category analysis, we make the following assumptions regarding the support region
of the majority class and minority classes:

Assumption 1. Smoothness Assumption for Majority Class. Given a highly imbalanced

dataset, the distribution of the support region of each majority class is sufficiently smooth.

Assumption 2. Compactness Assumption for Minority Class. Given a highly skewed dataset,

the minority class examples can be represented as a compact cluster in the feature space.

These assumptions are made to ensure that the rare categories are identifiable and meaningful.
To better capture this, let us look first at the example in Figure 3(a), where the majority class
(shown in blue) has a Gaussian distribution with large variance on the left, while the minority

4In this article, we use “rare category” and “m inority class” interchangeably.

ACM Computing Surveys, Vol. 56, No. 5, Article 123. Publication date: November 2023.

---

<!-- PAGE 4 -->

123:4

D. Zhou and J. He

Fig. 3. The support regions of a majority class and a minority class in a one-dimensional synthetic dataset.

class (shown in orange) corresponds to a peak with small variance on the right. If the minority
class is not compact and violates Assumption 2 (e.g., the minority class in Figure 3(b) is uniformly
distributed in the feature space), then no algorithm can perform better than random sampling. If
the distribution of the majority class is not smooth and violates Assumption 1 (e.g., the majority
class in Figure 3(c) consists of multiple narrow and sharp peaks just like the minority class), then
the minority class cannot be identified with a clear clue. Based on the assumptions related to rare
category examples, we propose the following definition of complex rare category analysis:

Definition 1.2. Complex Rare Category Analysis

Complex rare category analysis refers to the problem of detecting, characterizing, repre-
senting, and interpreting rare examples from underrepresented minority classes in a highly
imbalanced dataset.

1.2 Challenges of Rare Category Analysis
We first discuss the key challenges associated with rare category analysis. Unlike the conventional
anomalies, rare category examples have the following unique characteristics:

• C1. Rarity. It is often the case that the patterns of interest are sporadic in the collected data.
For example, in financial fraud detection, the vast majority of financial transactions are le-
gitimate; only a small number may be related to money laundering, and they often exhibit
similar traits. Another example is network intrusion detection. New malicious network ac-
tivities are hidden among huge volumes of routine network traffic, and network intrusions
of the same type are often similar to one another.

• C2. Label Scarcity. Given the high skewness and non-separable nature of rare categories,
labeling rare category examples is extremely expensive. In various real applications, such as
money laundering detection, synthetic identity (ID) detection, and network intrusion detec-
tion, we are usually required to learn from a handful of labeled examples.

• C3. Non-separability. Rare categories are often non-separable from the majority classes in
the feature space. For example, from the alarm of grid hacking (e.g., NotPetya) to the swift
growth in cyber-criminals (e.g., coin-mining attacks), the past several years have served as
a stark reminder of an emerging type of terrorist attack (i.e., adversarial attacks). Such mali-
cious attacks are designed to bypass current detection systems by camouflaging themselves
as normal instances, i.e., the support regions of normal instances, and malicious attacks are
non-separable in the given feature space.

• C4. Data Heterogeneity. To identify the rare categories, we often need to collect raw data
from different sources, at different time stamps using different techniques. Each data source
might have different types of users and attributes. Of such highly heterogeneous raw data,

ACM Computing Surveys, Vol. 56, No. 5, Article 123. Publication date: November 2023.

---

<!-- PAGE 5 -->

Rare Category Analysis for Complex Data: A Review

123:5

Fig. 4. Overview of complex rare category analysis.

only a subset (e.g., data sources, attributes) may be relevant to the identification of the rare
category examples (e.g., security threats).

• C5. Dynamics. The raw input data continuously change over time; thus, extracting and
modeling useful information from such dynamic systems plays an important role in rare
category analysis.

1.3 An Overview of Complex Rare Category Analysis
Complex rare category analysis can be divided into four tasks: detecting, characterizing, repre-
senting, and interpreting rare category examples. Figure 4 presents an overview of rare category
analysis, from the exploration step without any ground truth to the exposition step that aims to
characterize rare examples with a compact representation, from representing rare patterns in a
salient space to providing insightful interpretation over the prediction results.

• T1: Rare Category Exploration. In this task, we start from de-novo and do not have any
label information for the data. The goal is to identify at least one example from each rare
category with minimal help from labeling oracles. We begin with a comprehensive review
of some relevant topics, including anomaly detection [7, 26], outlier detection [57], and pre-
dictive modeling on imbalanced domains [20]; then we elaborate on popular approaches to
rare category exploration in both static and dynamic environments.

• T2: Rare Category Exploitation.

In this task, we use one/a few labeled examples from
each class that may have been obtained from the exploratory step discussed in T1. The pri-
mary goal is to capture a compact representation of the rare categories in various data for-
mats by learning from a few-shot annotated data points. Depending on the availability of
a multimodal representation of examples, rare category detection can be categorized as ho-
mogeneous rare category exploration or heterogeneous rare category exploration. In the
former setting [52, 109], all the examples are homogeneous, as they are collected from the
same data source or have identical traits; in the latter one [41, 79, 160, 163], we aim to identify
rare categories in the presence of data heterogeneity.

• T3: Understanding Rare Categories: This task , which may entail representing rare exam-
ples in a salient embedding space, visualizing the data distribution, or interpreting the under-
lying prediction process in the previous steps (T1 and T2), serves as an investigation step for

ACM Computing Surveys, Vol. 56, No. 5, Article 123. Publication date: November 2023.

---

<!-- PAGE 6 -->

123:6

D. Zhou and J. He

end-users. We systematically discuss recent advances in representation learning [60, 166],
interpretation [30, 84, 89], and visual analytic systems [81, 105] for rare category analysis.

1.4 Previous Work and Our Contributions to the Literature

Extensive literature surveys on the topics of imbalanced classification, anomaly/outlier detection,
and fraud detection have been published in the past decade. In the context of imbalanced classifi-
cation, He and Garcia [48] cover the development of research on learning from imbalanced data.
In the context of anomaly/outlier detection, Hodge and Austin [57] introduces a literature review
of contemporary techniques for outlier detection, and Chandola et al. [26] presents a comprehen-
sive overview of the research on anomaly detection. A series of surveys and special-issue journal
articles that target more specific problems and applications in the context of anomaly/outlier detec-
tion have also been published. In particular, Zimek et al. [173] studies the problem of unsupervised
outlier detection in high-dimensional numerical data, Chandola et al. [27] considers anomalies in
discrete sequences, Gupta et al. [45] focus on outlier detection for temporal data, Akoglu et al. [7]
attends to graph-based anomaly detection algorithms, Chalapathy and Chawla [25] provide an
overview of deep-learning-based anomaly detection techniques, and , Edge and Falcone Sampaio
[36] and Phua et al. [113] survey methodologies of fraud detection.

However, very few works present a comprehensive overview of complex rare category analysis.
He [49] is one of the first to present an end-to-end investigation of rare categories, but the intro-
duced methodologies are largely restricted to the tabular data in the static setting. Responding to
the gap in the literature, here we provide a comprehensive and structured overview of complex
rare category analysis from several perspectives:

• Data Perspective. Unlike the previous surveys on outlier detection, anomaly detection, and
rare category analysis, our study reviews state-of-the-art techniques for handling rich data
types, such as text/blogs, electronic health records, weblink graphs, and streaming data.
• Task Perspective. We provide a comprehensive overview of end-to-end complex rare category
analysis, from rare category exploration without any label information, to rare category ex-
position characterizing rare examples with compact representation, from representing rare
patterns in a salient embedding space to interpreting the prediction results and providing
relevant clues for end-users’ investigation.

1.5 Survey Roadmap
We present our survey in five parts sections. In Section 2, we focus on the de novo step of rare
category analysis, i.e., rare category exploration, which aims to find the initial example from each
minority class in the unsupervised setting. In Section 3, we discuss the following step, rare category
exploitation, which relies on the output of rare category exploration (i.e., initially labeled exam-
ples) to characterize the rare categories. In Section 4, we stress the importance of interpretation in
rare category analysis in various highly regulated industries, such as finance and healthcare. We
systematically discuss how to understand rare category analysis from the following two aspects:
(1) data diagnosis (i.e., How are the data distributed? Which piece of information is most valuable
for a given task?); and (2) model diagnosis (i.e., Why does the model make a certain prediction on a
particular piece of information?). Section 5 enumerates the popular benchmark datasets and repre-
sentative baseline models. In Section 6, we conclude our study and share our thoughts regarding
future research directions, such as how to ensure performance in the presence of noise, missing
data, and adversarial examples and how to generate task-specific rare category examples (e.g.,
money laundering activity) given a specific domain (e.g., transaction networks). A general outline
follows:

ACM Computing Surveys, Vol. 56, No. 5, Article 123. Publication date: November 2023.

---

<!-- PAGE 7 -->

Rare Category Analysis for Complex Data: A Review

123:7

• Section 2: Rare Category Exploration

– 2.1 Rare category exploration for static data

∗ 2.1.1 Tabular data
∗ 2.1.2 Graph-structured data

– 2.2 Rare category exploration for dynamic data

∗ 2.2.1 Time-series data
∗ 2.2.2 Temporal graphs

• Section 3: Rare Category Exploitation

– 3.1 Homogeneous rare category exploitation

∗ 3.1.1 Global approaches
∗ 3.1.2 Local approaches

– 3.2 Heterogeneous rare category exploitation

∗ 3.2.1 Data heterogeneity
∗ 3.2.2 Task heterogeneity

• Section 4: Understanding Rare Categories

– 4.1 Rare category representation
– 4.2 Rare category interpretation

• Section 5: Datasets and Representative Methods

– 5.1 Datasets
– 5.2 Representative methods

• Section 6: Conclusion and Future Directions

2 RARE CATEGORY EXPLORATION

Considered the de novo step in rare category analysis, rare category exploration, a.k.a. rare cate-
gory detection, aims to propose initial rare category examples to the labeling oracle in the given
dataset. Given an unlabeled, imbalanced dataset, the most natural method of rare category explo-
ration is random sampling. In this method we randomly draw examples without replacement to
be labeled by the oracle until at least one example from each minority class has been identified.
However, due to the rarity of rare categories (e.g., the proportion of a rare category is 0.01%), an
extensive number (i.e., 10,000) of labeling requests is required to spot the rare example. It is thus
worthwhile to develop more effective and efficient sampling strategies to address this rare category
exploration problem. In this section, we formally define the problem of rare category exploration.
We primarily aim to address (C1) rarity, (C4) data heterogeneity, and (C5) dynamics in rare category
analysis.

Problem 1. Rare Category Exploration.
Given: (i) an unlabeled dataset D, (ii) a small budget B for querying domain experts.
Find: the set of initial examples Q from each rare category.

In real-world applications of rare category exploration, researchers have customized Problem 1
for different data formats, including tabular data, time-series data, and graph-structured data. In
the following three subsections, we review the existing literature on rare category exploration
from a data perspective (e.g., static data vs. dynamic data, tabular data vs. graph-structured data).

2.1 Rare Category Exploration for Static Patterns

The techniques currently used in the static setting have been primarily designed in active-learning-
based schemes. The general procedure of this paradigm is presented in Figure 5. The key idea
behind the sample-selection-based methods is to learn a detector that can gradually search for the
potential rare examples by learning from the examples labeled by the oracle. We often assume that

ACM Computing Surveys, Vol. 56, No. 5, Article 123. Publication date: November 2023.

---

<!-- PAGE 8 -->

123:8

D. Zhou and J. He

Fig. 5. A conceptual framework for rare category exploration [109].

the labels obtained from the oracles are under a fixed budget B. Thus, the goal is to maximally
improve the prediction accuracy with the minimum number of labeling requests to the oracle. As
shown in Figure 5, rare category exploration proceeds iteratively. In each iteration, the program
starts with the oracle annotating a few samples. Then the sample-selection-based methods are
updated based on the newly labeled examples and further predict a small number of potential
rare category examples in the sense that obtaining labels for them further improves the prediction
accuracy. The program terminates once all the target rare categories have been captured. Next,
we elaborate on the existing rare category exploration algorithms designed for tabular and graph-
structured data.

i , . . . , xd
i

2.1.1 Tabular Data. Given an unlabeled dataset with n samples D = {x1, . . . , xn }, where each
sample xi , i = 1, . . . , n comes with d-dimensional features xi = {x 1
}, our goal is to identify
at least one example from each class y = 1, . . . , m with the minimum number of queries. The work
of Peleg and Moore [109] is one of the first attempts at rare category exploration. The authors
develop a mixture model to fit the data and design a family of hint selection methods to select the
rare examples with the help of a human expert. Experimental results using different hint selection
methods show the efficacy of the proposed rare category detection framework. He and Carbonell
[52] study the rare category exploration problem when the minority classes are non-separable
from the majority classes. Specifically, the authors develop a nearest-neighbor-based rare category
detection algorithm named NNDM, which gradually selects examples with the maximum changes
in the local density on a certain scale and asks for labeling from the oracle. The algorithm works
as follows: Given the prior p of each rare category C, the algorithm first estimates the number of
examples K = n × p in C. Then, the algorithm represents each example xi in terms of a vector that
is composed of the distances from its K-nearest neighbors. By obtaining the minimum distance r
among all samples, the algorithm constructs a hyper-ball with radius r for each example (as center)
and computes the local density as the number of enclosed examples within the hyper-ball:

Hyberball(xi , r ) = {x|x ∈ D, (cid:5)x − xi (cid:5) ≤ r }

(1)

LocalDensity(xi ) = |Hyberball(xi , r )|
(2)
To measure the degree of local density changes around each sample (i.e., hyper-ball), the authors
propose using the difference in the local density between xi and its neighbors:

DensityChange(xi )

=

⎧⎪⎨
⎪
⎩

maxxk ∈Hyberball(xi,r )[LocalDensity(xi ) − LocalDensity(xk )] xi is labeled
−∞
Otherwise

(3)

In particular, the function DensityChange assigns each labeled example’s scores with −∞ to avoid
duplicated labeling requests. Finally, the algorithm returns the examples with the largest local

ACM Computing Surveys, Vol. 56, No. 5, Article 123. Publication date: November 2023.

---

<!-- PAGE 9 -->

Rare Category Analysis for Complex Data: A Review

123:9

density changes to the oracle for labeling:

(4)

Query = argmaxxi ∈ DDensityChange(xi )
Theoretical analysis shows that the methods effectively select examples on both the boundary
and in the interior of the rare categories. In particular, when the rare categories are compact, the
majority class distribution is locally smooth, and the sample space is sufficiently large, NNDM is
guaranteed to identify at least one example coming from each minority class with probability 1 −δ
after (cid:8) 2α
r2

(cid:9) iterations, where δ ∈ (0, 1), α, and r2 are all positive parameters.

Despite the promising results of NNDM with theoretical guarantees, the algorithm’s perfor-
mance largely relies on prior information (e.g., number of classes, proportion of minority classes).
To alleviate the restriction on prior knowledge, He and Carbonell [50] propose a prior-free rare
category detection algorithm named SEDER. The intuition of this algorithm lies in the observation
that a region with an abrupt local density change has a higher probability of observing the rare
classes. Unlike He and Carbonell [52] and He et al. [53], SEDER picks the potential rare examples
with large neighborhood density changes for labeling by performing semi-parametric density es-
timation. SEDER introduces a prior-free DensityChange function, which is defined as the norm of
the gradient of the local density function:

DensityChange(xi ) =

(cid:6)(cid:3)(cid:4)

d(cid:5)

(cid:2)
n
k=1 DensityEstimation(xi )(x l
i

(

− bl x l

k ))2

l =1

((σ l )2bl )2

(5)

i denotes the lth feature of xi , σ l denotes the bandwidth of the

where x l
lth feature,
DensityEstimation is a kernel density estimation function with Gaussian kernel [37], and bl is
a positive parameter. In the presence of noisy data and irrelevant features, He and Carbonell [51]
formulate the rare category exploration problem via a co-selection scheme, which recovers the
relevant features and representative examples from the rare categories. To obtain the optimal sets
of relevant features and rare examples, He and Carbonell propose an effective searching procedure
(i.e., PALM) based on an augmented Lagrangian function to solve the optimization problem. In par-
ticular, PALM is designed in an alternative fashion so that the relevant features and the minority
class examples can be found.

Recently, a paradigm shift has been observed in the data mining community: from how to ac-
curately detect rare categories to how to ensure trustworthiness in rare category exploration. For
instance, Ahmadian and Lindsten [4], Kaur et al. [67], and Liu et al. [83] study how to ensure robust-
ness in detecting rare events, especially in the out-of-distribution setting. Shekhar et al. [120] point
out that algorithmic fairness and rare category exploration are dual problems when encountering
the data imbalance issue. The authors propose a fairness-aware method that jointly optimizes pre-
diction accuracy and statistical parity. Deng et al. [32] study the hardness bias in the autoencoder-
based rare category detection methods and propose a plug-and-play error calibration method to
mitigate the hardness bias issue.

2.1.2 Graph-Structured Data. In many fields, graphs offer a unifying data structure for model-
ing relational data. As a result, extensive research related to rare category exploration has been
conducted to spot the rare category entities in graph-structured data. Formally speaking, given an
unlabeled graph D = G(V, E), where V and E denote the sets of nodes and edges in G, respec-
tively, our target is to identify initial nodes and edges from each of the rare categories. He et al. [53]
extends the idea of He and Carbonell [52] to graph-structured data by proposing a graph-based rare
category detection algorithm named GRADE. The algorithm starts computing a global similarity
matrix S motivated by manifold ranking [169], which is used to obtain a compact representation

ACM Computing Surveys, Vol. 56, No. 5, Article 123. Publication date: November 2023.

---

<!-- PAGE 10 -->

123:10

D. Zhou and J. He

of the examples from the minority classes:

S = (I − αD

− 1

2 AD

−1

− 1
2 )

(6)

where I denotes the identify matrix, D denotes the diagonal matrix, and A denotes the adjacency
matrix of G. A prior-guided k-nearest-neighbor matrix is then computed to capture the sharp
local density changes near the boundary of minority classes and thus make it easier to capture the
rare patterns. In addition to developing GRADE, the authors develop a variation named GRADE-LI,
which requires only an upper bound on the proportion of each rare category. GRADE-LI can work
with the data when a detailed class-membership distribution of the data is not available to the
users.

Except for the plain graphs, data often exhibit node-level and edge-level heterogeneity for var-
ious critical tasks in security, finance, and medicine, among other fields. Each node or edge is
associated with a specific type in such data (referred to as a heterogeneous graph). To accommo-
date heterogeneous graphs, researchers have studied how to detect anomalies and rare events in
the unsupervised setting. For example, Sun et al. [127] propose the notion of neighborhood for-
mation for a bipartite graph, which computes the relevance scores of all nodes to a query node v
and define the neighborhood of v as the set of nodes with higher relevance scores. Based on the
neighborhood formation, the authors develop an anomaly detection algorithm to spot the abnor-
mal nodes with low “normality” scores. Based on similar intuition, Tong and Lin [132] propose
a non-negative residual matrix factorization framework named NrMF, which aims to detect the
malicious group of entities as well as provide interpretation of prediction results for data analysts.
NrMF is built upon the conventional matrix factorization mechanism,

A = FG + R

(7)

where F and G are low-rank factorized matrices, and R is the residual matrix that indicates rare
examples on the bipartite graphs. To interpret the predictions via NrMF, Tong and Lin impose a
non-negative constraint on the residual matrix R, such that all entries in R are larger than 0. Intu-
itively, higher value of the entry in R indicates a higher probability of existing rare and abnormal
examples. To solve the optimization problem of non-negative residual matrix factorization, the au-
thors develop a fast optimization algorithm to incrementally compute the residual matrix via the
rank-1 approximation, which runs in linear w.r.t. the size of the graph.

More recently, extensive attempts have been made to predict rare category events by developing
customized graph neural networks (GNNs) to depict the structure of a graph and learn repre-
sentations of various graph signals (e.g., nodes, edges, subgraphs). GNNs-based approaches are
generally designed based on the message-passing scheme, which is given as follows:

h(l +1)

v

= UPDATE(l ) (h(l )
= UPDATE(l ) (h(l )

v , AGGREGATE(l ) (h(l )
v , m(l )

N (v ) )

u , ∀u ∈ N (v)))

(8)

(9)

v

where h(l +1)
denotes the embedding of node v ∈ V at the (l + 1)th-layer, UPDATE(l ) and
AGGREGATE(l ) are both differentiable functions for the l th-layer, and m(l )
N (v ) is the aggregated “mes-
sage” from node v’s neighborhood N (v). Deng et al. [34] propose a graph convolutional net-
work (GCN)-based framework for predicting emerging events that requires capturing contextual
information from the raw data. The proposed framework first extracts graph representations of
the events; it then documents and learns to predict the occurrence of future events and to identify
the events of interest (i.e., rare categories). Zhong et al. [162] studies the problem of rare category
detection in videos, where each video is decomposed into n snippets (i.e., nodes in the constructed
video graph), the edges between each pair of snippets are defined based on feature similarity, and

ACM Computing Surveys, Vol. 56, No. 5, Article 123. Publication date: November 2023.

---

<!-- PAGE 11 -->

Rare Category Analysis for Complex Data: A Review

123:11

Fig. 6. An illustration of the bi-level rare categories (i.e., rare sequences and rare time segments) in a time-
series database [164].

the rare events are represented as abnormal actions. To solve this problem, a GCN is built to si-
multaneously clean noisy signals in the constructed video graph and predict abnormal actions.
Goodge et al. [42] investigate the relationship between the local outlier methods [69] and the
message-passing framework, which motivates them to develop a GNN-based method to identify
local rare examples.

2.2 Rare Category Exploration for Dynamic Patterns

The existing literature on detecting rare patterns in temporal data is very rich, with no universal
abstract categorization capable of capturing all the developed techniques in this direction. Accord-
ingly, we here focus on rare category exploration for time-series data and temporal graphs.

2.2.1 Time-Series Data. In the setting of time-series data, the rare categories can be observed
at both the sequence level and the segment level, as shown in Figure 6. For example, most electro-
cardiogram (ECG) signals are normal (i.e., collected from healthy people); only a small portion of
them is abnormal (i.e., collected from patients with heart disease). Moreover, within the abnormal
ECG signals, only a few segments are abnormal (e.g., heart arrhythmia); the rest are normal. Early
studies of rare category exploration for time-series data [18, 21, 22, 65, 80, 97, 100, 108, 118, 150]
are closely related to the outlier detection and disorder detection methods. They rely largely on
distanced-based mechanisms [97, 101, 116, 119] that define various similarity measurements [45] of
temporal sequences and segments and then identify rare patterns deviating from the normal ones.
For instance, Cao et al. [22] propose a scalable distance-based detection algorithm for high-volume
data streams. This algorithm has been found to be optimal in terms of CPU costs. Begum and
Keogh [18] study the problem of discovering rare time-series motifs (i.e., repeated subsequences)
from unbounded streams. To address the rarity issue of the time-series motif in a never-ending
stream, Begum and Keogh develop a “sticky cash” algorithm that adopts a Bloom filter to remem-
ber every incoming subsequence and efficiently detects rare motifs in the unbounded real-valued
time series. To facilitate the use of distance-based methods, Yeh et al. [150] introduce a fast compu-
tational algorithm for time-series/subsequence all-pairs-similarity-search that has strong implica-
tions for and promising results for the task of time-series discord discovery. Finally, Goodge et al.
[43] introduce a robust random-cut data structure to produce a sketch or synopsis of time-series
data. Using this structure, the authors propose a scalable anomaly detection algorithm by gradually
updating the time-series sketch in a continuous data stream.

ACM Computing Surveys, Vol. 56, No. 5, Article 123. Publication date: November 2023.

---

<!-- PAGE 12 -->

123:12

D. Zhou and J. He

A key motivation of the aforementioned methods is that the distributions of rare categories
(minorities) deviate from the normal distribution (majorities). However, there are some obvious
limitations to this idea in practice. The identified examples are often not the targets of researchers’
interest, which are drawn from noise or combinations of irrelevant features. Zhou et al. [164] as-
sume that the targets of our interest are rare and drawn from a compact distribution. Under this
assumption, Zhou et al. propose a bi-level generative model that aims to jointly characterize the
rare temporal pattern at the time-series and subsequence levels. Recent advances in deep learning
architectures have led to a surge in research interest related to developing deep models to char-
acterize and detect rare temporal patterns in high-impact applications. Tuor et al. [134] present a
deep unsupervised framework for detecting insider threat in online data streams. This framework
outputs a ranked list of anomaly scores of individual user behaviors; Li et al. [77] develop a gen-
erative adversarial network (GAN) for unsupervised multivariate anomaly detection. Unlike
conventional distance-based methods and supervised methods, the proposed framework detects
rare temporal patterns by using the GAN-trained generator and discriminator to compute the
discrimination and reconstruction anomaly score (DR-Score); Shen et al. [121] propose a re-
current network ensemble called the recurrent autoencoder, which is designed to characterize and
capture the abnormal time-series segments at multiple resolutions; finally, Deng and Hooi [33]
and Zhang et al. [159] propose modeling the between-sensor dependence relationship to identify
abnormal time segments in multivariate time series.

2.2.2 Temporal Graphs. Many real-world systems, including social networks, communication
networks, and gene interaction networks, are intrinsically dynamic and can be represented as
temporal graphs. In the past few years, researchers have proposed several rare category explo-
ration models for temporal graphs [3, 13, 34, 59, 76, 89, 90, 115, 125, 140, 149, 153, 167, 168].
The existing work can be categorized as discrete temporal graphs [154] or continuous temporal
graphs [85, 103, 171] based on the method of data collection used in the particular application
domain.

The discrete temporal graphs are often referred to as a time-evolving graphsn wherein the
˜G = {G (1), G (2), . . . , G (T ) }. Each snapshot
data D is presented as a sequence of snapshots
G (t ) = (V (t ), E (t ) ), t = 1, 2, . . . ,T is composed of a collection of nodes V (t ) and edges E (t ) at
timestamp t. To identify rare examples on ˜G, the static methods are extended to the dynamic
setting. For example, Sun et al. [126] propose a parameter-free model that can monitor grouped
outliers and their changes in a stream of graphs. The algorithm is designed based on minimum
description length (MDL), which allows users to discover the changes in communities as well
as in points in time. Araujo et al. [14] develop a fast incremental tensor analysis approach that can
discover both transient and periodic/repeating communities in dynamic graphs. Sricharan and Das
[125] define a commute-time distance that captures node relationship changes and allows tradi-
tional distance-based methods to be used with discrete temporal graphs. Lee et al. [76] propose a
discrete-time exponential-family random graph model to identify clusters in time-evolving graphs.
Manzoor et al. [90] study the problem of anomaly detection in streaming heterogeneous graphs by
proposing a clustering-based anomaly detection approach that can simultaneously address the het-
erogeneity and streaming nature of the input data. In particular, Manzoor et al. introduce a novel
embedding mechanism that can encode the heterogeneous streaming graph into a vector represen-
tation that is then used to perform clustering and identify anomalous patterns. Appel et al. [13]
proposes a factorization framework that can jointly model the distribution of dynamic connections
and attributes and track the evolution of evolving communities. Despite their success, the detec-
tion algorithms often suffer from high computational costs, especially when extensive snapshots
are given or when the algorithms are applied in the online setting. To address this issue, Zhou

ACM Computing Surveys, Vol. 56, No. 5, Article 123. Publication date: November 2023.

---

<!-- PAGE 13 -->

Rare Category Analysis for Complex Data: A Review

123:13

et al. [167, 168] propose an incremental rare category exploration scheme that aims to gradually
update the static rare category exploration models based on the local changes on a new snapshot
without learning from scratch. In particular, Zhou et al. propose a closed-form solution to update
the global similarity matrix S (defined in Equation (6)) in the dynamic setting:

S(t ) = S(t −1) + α

S(t −1)uvT S(t −1)
I + vT S(t −1)u

(10)

where u and v are one-hot vectors indicating the source nodes and target nodes of the updated
edges, respectively; I denotes the identity matrix; and S(t ) and S(t −1) are the global similarity matri-
ces at the timestamps t and (t −1), respectively. Moreover, to efficiently and effectively compute the
density changes, DensityChange(xi ), a theoretical condition, is provided to determine whether the
hyper-ball Hyberball(xi , r ) is required to update from the previous timestamp. Yasami and Safaei
[149] study the problem of anomaly detection in dynamic social networks, wherein both network
structure and node attributes are observed over time. The proposed framework jointly models two
processes, i.e., (1) the normal modeling component and (2) the anomaly detection component, to
track the abnormal relationship between nodes’ features and link generation in dynamic social
networks. Agarwal et al. [3] introduce a novel community scoring metric called permanence and
proposes an incremental algorithm to track the evolution of network communities in the dynamic
setting. The theoretical analysis shows that the updating procedure of the proposed algorithms
leads to permanence maximization in the dynamic networks. Furthermore, to guarantee model effi-
ciency and algorithmic fairness, Fu et al. [39] introduce a fairness-aware clique-preserving spectral
clustering algorithm that generalizes the static clique clustering methods to the dynamic setting
via fairness-aware edge filtering and incremental eigenpair updating.

Continuous temporal graphs are also called fine-grained temporal graphs or temporal interaction
graphs, where the temporal graph is presented as a sequence of timestamped edges. It is intractable
to directly generalize the static rare category exploration approaches used in discrete temporal
graphs to continuous temporal graphs. For this reason, Manzoor et al. [90] propose to represent
continuous temporal graphs with a vector representation, which is easy to compute and preserves
the contextual information of the continuous temporal graphs. With the learned continuous tem-
poral graph representation, Manzoor et al. develop a fast and memory-efficient detection algo-
rithm to process any incoming nodes and edges and identify anomalies in real time. Hollocou et al.
[59] subsequently studies the problem of identifying grouped anomalies in the edge streaming
setting. In particular, the data are presented as a sequence of streaming edges. The authors pro-
pose a streaming algorithm with the theoretical justification that performs graph clustering with
only three integers per node and does not keep any edge in memory. Amjadi and Tulabandhula
[10] propose a block-structured time-series model for detecting communities on time-evolving
graphs. This approach can capture both the link persistence and community persistence over
time.

3 RARE CATEGORY EXPLOITATION

In the previous section, we introduced the current literature on rare category exploration, a prob-
lem that aims to identify at least one example from each minority class. A follow-up to rare cat-
egory exploration, rare category exploitation aims to learn from the identified examples and cap-
ture all the rare examples in a given dataset. In Figure 7, we present an example of rare category
exploitation on a synthetic dataset with one majority class and four minority classes. The key
observations are as follows: (1) the distribution of the majority class is smooth and (2) the sup-
port regions of the four minority classes are compact. That is, instances in each minority class
are self-similar and form a compact representation. In the past decades, the question of how to

ACM Computing Surveys, Vol. 56, No. 5, Article 123. Publication date: November 2023.

---

<!-- PAGE 14 -->

123:14

D. Zhou and J. He

Fig. 7. An example of rare category exploitation with one majority class and four minority classes [54]. The
labeled minority class examples are shown in green, the labeled majority class examples are shown in red,
and the unlabeled examples are shown in black.

explore the compactness of rare categories has attracted considerable interest from the data mining
and machine learning communities. In this section, we delve into the problem of rare category
exploitation under two scenarios: (1) homogeneous data and (2) heterogeneous data. Whereas
in the former setting, data are collected from the same source and represented in the same for-
mat in the latter setting, we aim to capture rare examples in the presence of data and task
heterogeneity.

3.1 Homogeneous Rare Category Exploitation
Formally, we let X and Y denote the sample space and label space, respectively. We are given a
dataset D = {Dl , Du }, where Dl = {(xi )}Nl
i=1 consists of Nl obtained annotated samples, Du =
{(xj )}Nu
j=1 denotes Nu unlabeled examples, and xi , xj ∈ X, yi ∈ Y. It is often the case that, due to
the (C1) rarity and label (C2) scarcity challenges, annotated data Nl are scarce. In rare category
exploitation, our goal is to produce a prediction function f (·) : X → Y by learning from Dl
and to accurately characterize unknown rare category examples in Du . Given this, we present
the following definition of rare category exploitation in the homogeneous setting. In this problem
setting, we mainly study (C1) rarity, (C2) label scarcity, (C3) non-separability, and (C5) dynamics
in RCA.

Problem 2. Homogeneous Rare Category Exploitation.
Given: a dataset D = {Dl , Du } with scarce labeled examples Dl = {(xi )}Nl
beled examples Du = {(xj )}Nu
j=1.
Find: (i) a prediction function f (·) to characterize rare category examples, (ii) a set of unlabeled
examples that are likely coming from the rare categories.

i=1 and extensive unla-

We categorize the current approaches to homogeneous rare category exploitation as either
global or local. The first category aims to capture the global data distribution for characterizing
rare categories, whereas the second category focuses on exploring rare categories within a single
or a few local regions (e.g., the neighborhood of the identified rare category examples).

3.1.1 Global Approaches. This category of approaches exploits both the labeled and unlabeled
examples to learn the class-membership distribution. Essentially, these methods transform the
rare category exploitation problem into a classification problem with highly skewed data distribu-
tion. However, unlike the well-studied imbalanced classification problem that aims to maximize

ACM Computing Surveys, Vol. 56, No. 5, Article 123. Publication date: November 2023.

---

<!-- PAGE 15 -->

Rare Category Analysis for Complex Data: A Review

123:15

the overall classification accuracy (majority classes and minority classes), rare category exploita-
tion emphasizes learning and characterizing the minority classes. Early rare category exploitation
work addresses the (C1) rarity and (C3) non-separability challenges. One representative approach
is hyper-ball-based rare category exploitation [54, 55]. The key idea behind approaches is to for-
mulate rare category exploitation as an optimization problem: minimizing the radius R of the
hyper-ball that well encloses the rare categories. The general objective function for the binary
case (i.e., one majority class and one minority class) can be written as follows.
R2

(11)

min
R,c
s.t., (cid:5)xi − c(cid:5)2 ≤ R2, xi ∈ Dmaj
(cid:5)xj − c(cid:5)2 ≥ R2, xj ∈ Dmin
l
(cid:5)xk − c(cid:5)2 ≥ R2, xj ∈ Du

l

l

l

where R denotes the radius of the hyper-ball, c denotes the center of the hyper-ball, Dmaj
denotes
the set of labeled majority class examples, and Dmin
denotes the set of labeled minority class
examples. Moreover, to ensure the compactness of the hyper-ball, the authors introduce three
constraints on the optimization problem: (1) the labeled examples from the majority classes should
be outside of the hyper-ball; (2) the labeled examples from the minority class should be inside of
the hyper-ball; and (3) the hyper-ball should enclose as many unlabeled examples as possible. To
tackle the non-separability challenges, RACH [54] provides a relaxed solution of Equation (11) by
introducing slack variables to allow the miss-classified instances and then converting the problem
into a convex optimization problem. The relaxed problem can be easily solved in its dual form via
the projected subgradient method. Following He et al. [54], He et al. [55] introduces a kernelized
rare category exploitation algorithm that, generalizes RACH to model complex shapes of the target
rare categories’ support regions by projecting to the high-dimensional feature space induced by
kernels. The kernel method provides more flexibility when characterizing complex rare categories
in real-world applications.

Several more recent studies consider the problem of rare category exploitation in the presence
of (C2) scarce and noisy labels. Haque et al. [46], study the problem of novel class classification on
data streams. Instead of relying on redundant human-annotated labels or prior knowledge, they
propose a semi-supervised framework to track the confidence changes of classifiers in order to
detect the novel concept drifts and thus identify the novel classes. Zhou et al. [166] propose a bi-
level learning mechanism (shown in Figure 8) in which, a teacher model (i.e., curriculum learning
scheme) gradually augments the training set with pseudo labels, and the student model (i.e., rare
category characterization) returns the prediction results together with the prediction confidence
to the teacher model. In general, the teacher model and the student model are trained in a mutu-
ally beneficial way, enabling the model to achieve better prediction accuracy in both rarity and
label scarcity. Any real-world applications (e.g., video classification [162]), in addition featuring
label scarcity, come with complex data and noisy labels, which require machine learning models
to be trained with only weak supervision [172]. Zhong et al. [162] propose a GCN to clean the
noisy labels. The GCN-based label noise cleaner is designed to provide supervisory signals from
high-confidence snippets to low-confidence snippets, such that the classifier can be trained with
“clean” supervision. Xi et al. [144] study the problem of online transaction fraud detection. To han-
dle the noisy and complex user behavior information, they develop the dual importance-aware
factorization machine (DIFM) that captures field value variations and field interactions simulta-
neously to support online transaction fraud detection. Lin et al. [82] propose a multi-resolution rare
category exploitation approach to identify instances of online credit payment frauds at different

ACM Computing Surveys, Vol. 56, No. 5, Article 123. Publication date: November 2023.

---

<!-- PAGE 16 -->

123:16

D. Zhou and J. He

Fig. 8. A conceptual framework of bi-level learning for rare category exploitation [166] that is composed of
a student learning model and a teacher learning model. The dashed arrows indicate the learning process of
the teacher model that aims to generate pseudo labels; the solid arrows indicate the learning process of the
student model that is designed to predict rare category examples.

granularities. Wu et al. [143] study rare category exploitation under various data contamination,
by proposing an information-theoretic bound of performance degradation in terms of the data
contamination ratio.

3.1.2 Local Approaches. The local algorithms are also referred to as seeded or targeted algo-
rithms [56, 112, 151, 170]. This category of approaches essentially tackles rare category exploita-
tion as a local clustering problem. The key idea is to treat the labeled examples as seeds and return a
compact cluster near the seed examples without exploring the whole dataset. Azmandian et al. [16]
present a local kernel density ratio feature selection framework that seeks a salient feature sub-
space in which the normal data points form a high-density region and the rare examples form
a low-density region. In the learned subspace, the rare examples stand out and are easily distin-
guished by detection algorithms. Spielman and Teng [124], present a design of a local clustering
algorithm for massive graphs. The local algorithm is able to find a compact local cluster near a
seed example and the running time is near-linear with respect to the size of the returned cluster.
Andersen et al. [11], derive a mixing result for PageRank and propose a fast approximation method
to compute PageRank vectors. Using this method, the authors develop an improved local graph
partitioning algorithm that enables polylogarithmic time complexity with respect to the number
of edges in the given graph. Pang et al. [107] propose a local and interactive rare event detec-
tion algorithm, that leverages the feedback from an anomaly-biased simulation environment and
continuously updates the learned abnormality to novel rare categories.

Although the conventional local clustering algorithms are primarily designed for low-order
connectivity patterns (e.g., edge in Table 1), many applications exhibit high-order connectivity
patterns (e.g., star in Table 1). For example, the loop-shaped structure plays a significant role in de-
tecting communities in user-item networks [170]; a cluster of star-shaped structures often serves
a red flag indicating potential instances of synthetic ID fraud in the personal identifiable in-
formation (PII) networks [102]. To account for the crucial high-order connectivity patterns in
real-world systems, Zhou et al. [170] and Yin et al. [152] offer innovative studies of the problem of
local high-order graph clustering. In particular, the authors introduce the notion of high-order con-
ductance and the high-order diffusion kernel with the high-order Markov chain as the underlying
model, which allows end-users to model various types of high-order structures. Moreover, they
generalize the well-known local clustering algorithms [11, 124] to the high-order setting and pro-
vide a theoretical analysis of the effectiveness and scalability of the proposed algorithms. Many
recent studies study the high-order connectivity patterns in more complicated scenarios, such
as modeling evolving high-order structures on fine-grained temporal networks [165], capturing

ACM Computing Surveys, Vol. 56, No. 5, Article 123. Publication date: November 2023.

---

<!-- PAGE 17 -->

Rare Category Analysis for Complex Data: A Review

123:17

Table 1. Illustrative Examples of High-Order Connectivity Patterns and Local Clustering Algorithms

Connectivity Pattern N Illustration Order of N Clustering Algorithms

1st-order
2nd-order

N/A
1st-order

Applications
N/A
Rare category detection [53]

3rd-order

2nd-order

Social community detection [71]

Vertex
Edge

3-node Line

Triangle

k-node Star

k th-order

(k − 1)th-order

Synthetic identity detection [102]

higher-order clusters in heterogeneous networks [23], and tracking high-order structures on time-
evolving graphs [38].

3.2 Heterogeneous Rare Category Exploitation
In the era of big data, many application domains exhibit multiple types of heterogeneity, including
data heterogeneity that originates from multiple information sources and task heterogeneity that
originates from multiple application domains. In this subsection, we organize the existing work in
the context of data heterogeneity and task heterogeneity.

3.2.1 Data heterogeneity. Learning from data heterogeneity is often referred to as multi-view
learning, as the data are collected from different sources, enabling multiple views. In the data
heterogeneity setting, rare category exploitation becomes even more challenging than in the data
homogeneity setting due to the existence of multiple views. It is crucial to leverage multiple views
and identify the relevant features for distinguishing between the majority and minority classes.
With the aim of addressing (C1) rarity, (C2) label scarcity, and (C4) data heterogeneity in rare
category analysis, we formally define the problem as follows:

Problem 3. Multi-View Rare Category Exploitation.
Given: (i) a dataset D collected from V views; (ii) a small set of labeled examples Dl = {(xi )}Nl
i=1.
Find: (i) a prediction function f (·) to characterize rare category examples, (ii) a set of unlabeled
examples that are likely coming from the rare categories.

A pivotal step in addressing Problem 5 is to leverage view consistency and learn a unified rep-
resentation to improve the performance of rare category exploitation. In the past decades, re-
searchers have proposed extensive multi-view learning frameworks [9, 40, 63, 64, 78, 79, 79, 91,
122, 157, 160] for anomaly detection that could potentially solve Problem 5. However, these meth-
ods are mostly unsupervised and/or based on some heuristic functions, which means the methods
might not well capture the characteristics of rare categories. MUVIR [163] is one of the principled
efforts that has been proposed to address Problem 5. MUVIR provides a generic rare category de-
tection solution that is able to integrate the existing single-view rare category exploitation models
in order to compute the overall posterior probability of each example. The key idea is to exploit the
relationship among multiple views and estimate the overall posterior probability of examples com-
ing from rare categories given data from multiple views. In particular, given data with multi-view
features, one can train V distinct rare category exploitation models upon V views and compute
view-specific posterior probability P (y = rare category|xv ) with respect to the vth view. The
authors propose the following theorem to effectively integrate view-specific posterior probability
P (y = rare category|xv ) in a model-agnostic way:

ACM Computing Surveys, Vol. 56, No. 5, Article 123. Publication date: November 2023.

---

<!-- PAGE 18 -->

123:18

D. Zhou and J. He

Theorem 3.1 ([163]). If the features from multiple views have weak dependence given the class

(cid:6)
V

v=1 P (xv |y = rare category), α > 0, then

label yi [1], i.e., P (x|y = rare category) ≥ α
V(cid:7)

P (y = rare category|x) ≥ C (cid:7)
(cid:8)

P (y = rare category|xv )(cid:9)
(cid:10)

× (cid:7)
(cid:8)

v=1

(cid:6)
V
v=1 P (xv )
P (x)

(cid:9)
(cid:10)

(12)

where C =

α

(p2)V −1 is a constant.

Using Theorem 3.1, the overall posterior probability P (y = rare category|x) can be approxi-

mated as follows:

P (y = rare category|x) =

V(cid:7)

v=1

P (y = rare category|xv ) (cid:7)
(cid:8)

(cid:6)
V
v=1 P (xv )
P (x)

d
(cid:9)
(cid:10)

(13)

where the marginal probabilities P (x) and P (xv ) can be estimated via kernel density, and d is a non-
negative parameter that balances the importance of the term related to the marginal probabilities.
A modified version of MUVIR has been proposed for handling problems when the exact priors of mi-
nority classes are unknown. In the past few years, researchers have explored many high-impact ap-
plications of rare category exploitation that can be formulated as multi-view rare category exploita-
tion problems. Among them, Lee et al. [75] propose an attention-based visual question-answering
network to jointly model the input images and corpora and identify system errors or abnormal
events; Chen et al. [29] study the problem of multi-modal video anomaly detection, proposing a
bi-directional predictive network to regularize the prediction task from pixel-wise, cross-modal,
and temporal-sequence levels; and Shen et al. [123] propose an anomaly segmentation network
for localizing defective areas in large-scale industrial manufacturing environments.

Another group of approaches to multi-view rare category exploitation consist of the semi-
supervised classification models. For example, Nie et al. [104] propose a multi-view framework
with adaptive neighborhood learning. The framework integrates multi-view clustering and semi-
supervised classification, which allows learning attention for each view automatically. Zhang
et al. [156] develop a multi-view rare category exploitation framework for Alzheimer’s disease di-
agnosis. They propose a multi-layer multi-view framework that automatically constructs a shared
latent representation across multiple views and learns the mapping functions from the multi-view
features to the prediction labels. Wang and Lan [138] assume the multiple views of the majority
class examples are drawn from a unique distribution with different projection functions. Given
this assumption, the authors propose a hierarchical Bayesian model that computes the outlierness
of unlabeled samples and thus identifies rare examples.

3.2.2 Task heterogeneity. This subsection provides an overview of the rare category exploita-
tion algorithms that have been proposed in the context of task heterogeneity. Formally speaking, in
the presence of multiple tasks, we are given a dataset D = {D1∪. . .∪DS } that comes from S applica-
tions domains, and a small set of labeled examples from each task Ds
l denotes
l
the number of labeled examples in Ds . Our goal is to capture the multimodalities from different
tasks and domains and learn a prediction model to accurately characterize the rare categories from
different tasks and domains. The problem, which aims to address (C1) rarity, (C2) label scarcity,
(C3) non-separability, and (C5) dynamics in rare category analysis, is commonly defined as follows:

i=1, where N s

i )}N s

= {(xs

l

Problem 4. Multi-task Rare Category Exploitation.
Given: (i) a dataset D = {D1 ∪ . . . ∪ DS }, where Ds is the dataset for the sth task, s = 1, . . . , S;
(ii) a small set of labeled examples from each task Ds
l
Find: (i) a prediction function f (·) to characterize rare category examples in each task Ds , (ii) a
set of unlabeled examples that are likely coming from the rare categories in each task Ds .

i )}N s
i=1.

= {(xs

l

ACM Computing Surveys, Vol. 56, No. 5, Article 123. Publication date: November 2023.

---

<!-- PAGE 19 -->

Rare Category Analysis for Complex Data: A Review

123:19

The past decades have produced much literature studying Problem 4. This literature can be
categorized in one of two ways based on its objectives. The first category aims to learn a mixture
of prediction functions that maximize the overall accuracy across all tasks. For example, Yang et al.
[146] study the problem of rare category exploitation in the presence of multiple tasks and multiple
views by proposing a joint optimization framework called M 2LI D. The authors start from a metric
called border degree that is used to capture the sharp changes in density near the boundary of rare
categories in the feature space:

BorderDegree(x) = Hub(x) − Authority(x)

(14)

where Hub(x) and Authority(x) indicate the hub value and authority value [70] of example x,
correspondingly. Intuitively, the larger the border degree is, the higher the probability that x be-
longs to the rare category. To model task relatedness and view consistency, they then formulate
the problem by requiring (1) task-specific learners to behave similarly on the features, (2) view-
based learners to behave similarly on the examples, and (3) the border-degree to be negatively
correlated with the prediction confidence score. Finally, to solve the optimization problem, they
develop a block-coordinate-descent-based method to iteratively update the boundary character-
istics of rare categories and multiple classification functions for different tasks. [62] propose a
multimodel learning algorithm that is based on a mixture of sparse Gaussian graphical models.
[161] aims to tackle the Problem 4 in the presence of data scarcity and adversarial attacks. The
authors propose a federated learning framework that performs multiple tasks simultaneously.

The second category is also referred to as transferable rare category exploitation. Instead of
learning an optimal predictor for all tasks, transferable rare category exploitation heavily em-
phasizes the target tasks. Some typical works includes [8], [12], [72], [129], and [136]. In Appel
et al. [12], the authors systematically evaluate the performance of anomaly detection frameworks
using two types of transfer representation learning paradigms: (1) transfer learning from pre-
trained networks, and (2) transfer learning from auxiliary tasks. Kumagai et al. [72] develop an
autoencoder framework that learns the domain-specific latent vectors and thus improves the per-
formance in detecting rare examples. Unlike most transfer learning models that aim to learn the
transferable representation for the target domain, the work of Vercruyssen et al. [136] proposes
to select a subset of labeled and relevant examples from the source domain to augment the tar-
get tasks. The aforementioned methods all assume the target domains are related to the source
domains. However, there is a more challenging scenario: the so-called out-of-distribution rare cat-
egory exploitation, wherein the test data are unseen or from shifted distributions. To handle the
out-of-distribution scenarios, Morteza and Li [98] propose an analytical framework with provable
guarantees to characterize and understand out-of-distribution detection in open-world applica-
tions. Sun and Wang [128] propose an adaptive in-out-aware learning framework to jointly model
the mixed in-distribution and out-of-distribution data samples. Acharya et al. [2] propose a graph
context reasoning network for out-of-distribution object detection by constructing a representa-
tion graph and a context graph from the input image.

4 UNDERSTANDING RARE CATEGORIES
Although they have been tremendously successful in exploring and exploiting rare category ex-
amples, many advanced methods, especially deep learning models, often remain black-box in na-
ture. This poses a challenge to their application in industries that have to follow highly regu-
lated processes. In these industries, prediction models must be interpretable and the output re-
sults are required to meet compliance standards. Therefore, a natural research question is how to
make existing models transparent to the end-user by identifying the right context (e.g., key fac-
tors, representative entities, critical timestamps). In this section, we systematically discuss how to

ACM Computing Surveys, Vol. 56, No. 5, Article 123. Publication date: November 2023.

---

<!-- PAGE 20 -->

123:20

D. Zhou and J. He

Fig. 9. Rare-category-oriented network representation: the majority and minority classes are not separable
in the original feature space, but become well separated in the embedding space [166].

understand rare category patterns from the following two directions: (1) rare category represen-
tation and (2) rare category interpretation. The first direction aims to diagnose from the data per-
spective (i.e., How is the data distributed? Which piece of information is most valuable for a given
task?), while the second direction aims to diagnose from the model perspective (i.e., Why does the
model make a certain prediction on a particular piece of information?).

4.1 Rare Category Representation
In this task, we aim to learn a rare-category-oriented embedding representation such that the
rare examples (e.g., security threats) are well separated from the majority classes (e.g., normal
activities). Figure 9 presents a typical example of rare category representation learning wherein
the majority class and the minority class are overlapped together in the original features space but
become separated in the learned embedding space. Formally speaking, the problem can be defined
as follows:

Problem 5. Rare Category Representation.
Given: (i) a dataset D that consists of n samples; (ii) a small set of labeled examples Dl = {(xi )}Nl
i=1;
(iii) the user-defined embedding dimension d.
Find: (i) a rare category representation model д(·); (ii) a d-dimensional embedding representation
E ∈ Rn×d that well preserves the underlying distribution of rare categories.

In the past decade, extensive work has been done to develop representation learning methods to
learn the underlying distribution of the rare category patterns. The key idea behind these methods
is to track the “footprints” of rare categories via external information (e.g., supervision from ora-
cles) or prior knowledge (e.g., features indicating local density changes [52, 147]) and then leverage
this information to regularize the representation learning models to extract low-dimensional and
salient embedding for rare category analysis. For instance, Akoglu and Falioutsos [5] propose a
set of egonet features (e.g., weighted and unweighted in- and out-degree, number of neighbors,
number of triangles) from each snapshot of the graph sequence to model the “behavior” of each
node. These features are effective in spotting rare category examples. Manzoor et al. [90] aim to
spot anomalous patterns in a stream of heterogeneous graphs containing different types of nodes
and edges by proposing a clustering-based anomaly detection approach that can simultaneously
address the heterogeneity and streaming nature of the input data. In particular, Manzoor et al. in-
troduce a novel embedding mechanism that can encode the heterogeneous streaming graph into
a vector representation that is then used to perform clustering and identify anomalous patterns.
Huang et al. [60] study the problem of image classification when data in the vision domain exhibit

ACM Computing Surveys, Vol. 56, No. 5, Article 123. Publication date: November 2023.

---

<!-- PAGE 21 -->

Rare Category Analysis for Complex Data: A Review

123:21

Fig. 10. Preliminary results comparing network embedding using various algorithms [166].

a highly skewed class distribution by learning a deep representation such that rare categories
are easily separable from the majority class by contemporary classification methods. In particu-
lar, this article first proposes to learn the data representation by maintaining both inter-cluster
and inter-class margins that reduce the class imbalance inherent in the local data neighborhood.
The proposed framework is built based on a Convolutional neural network (CNN) framework
through a quintuplet sampling scheme and the associated triple-header hinge loss.

More recently, due to the notable success of network-embedding approaches, various network-
embedding-based approaches have been proposed for rare category analysis. For example,
SPARC [166] is one of the first rare-category-oriented network embedding frameworks. SPARC
aims to learn a salient representation to characterize rare category examples. Inspired by the family
of curriculum learning that simulates the cognitive mechanisms of human beings, SPARC gradu-
ally selects the key network contextual information and learns the rare-category-oriented network
representation by shifting from the “easy” concept to the “difficult” concept. The results show that
(1) SPARC enables users to visualize the network layout in a salient embedding space, where the
majority classes and minority classes are well separated; and (2) SPARC is able to identify valu-
able contextual information that provides interpretation and guidance in the task of rare category
characterization. Here we compare SPARC with three state-of-the-art network embedding algo-
rithms, including two unsupervised methods, i.e., DeepWalk [111] and LINE [130], and one semi-
supervised method, i.e., PLANETOID [148]. We first map the given network to a 129-dimensional
space with different embedding methods. Then, we employ the nonlinear dimensionality reduction
method, i.e., t-SNE [88], to encode examples in a two-dimensional space for better visualization,
as shown in Figure 10. We observe that the rare examples are better clustered using the proposed
method than any of the baseline methods.

Following SPARC, Wu et al. [142] propose a biased random walk model named VDRW for learn-
ing imbalanced network representation. VDRW is designed to dynamically adjust the transition

ACM Computing Surveys, Vol. 56, No. 5, Article 123. Publication date: November 2023.

---

<!-- PAGE 22 -->

123:22

D. Zhou and J. He

Fig. 11. User interface of RCLens, which is composed of three key modules: the data explorer module (shown
in subfigure a), the feature explorer module (shown in subfigure b), and the category explorer module (shown
in subfigure c).

probability matrix each time a node is visited by the random particle. Via VDRW, Wu et al. propose
a pair of sampling strategies, i.e., context sampling and balanced-bath sampling, to learn network
representation using skip-gram model [94]. NetWalk [155] is developed for rare event detection by
learning the network representations, which can be updated dynamically as the network evolves.
NetWalk first extracts the dynamic network context and encodes the vertices of the dynamic net-
work to a low-dimensional representation. Then, a clustering-based scheme is employed to incre-
mentally and dynamically track the malicious patterns in the dynamic networks. Deng et al. [34]
propose a GCN-based framework for predicting future events by capturing contextual information
from the raw data. The proposed framework first extracts graph representations of the events doc-
uments and, then learns to predict the occurrence of future events and identify events of interest
(e.g., anomaly patterns).

4.2 Rare Category Interpretation
Interpretability in machine learning models plays a crucial role in many high-impact domains and
rare category analysis. In this task, we aim to characterize the rare categories with a predictive
model and interpret the output from this model by providing relevant clues, such as connectivity
patterns, data sources, features, and timestamps from time-series data. We define the problem
setting as follows:

Problem 6. Rare Category Interpretation.
Given: (i) a dataset D that consists of n samples, (ii) a rare category analysis model f (·).
Find: interpretation over the output from f (·) on D.

Despite the rich literature in the context of explainable artificial intelligence (XAI) [15, 31,
44, 61, 95, 96, 131], interpreting rare category analysis models remains challenging for the follow-
ing reasons: (1) rare category analysis models are naturally “biased” (i.e., focusing on minority

ACM Computing Surveys, Vol. 56, No. 5, Article 123. Publication date: November 2023.

---

<!-- PAGE 23 -->

Rare Category Analysis for Complex Data: A Review

123:23

Fig. 12. User interface of RCAnalyzer, which is composed of (a) the timeline view; (b) the matrices view;
(c) the instance view; (d) the sub-network view; (e) the label result view; (f) the parameter panel; (g) the
encoding panel; and (h) the information panel.

patterns instead of the overall data distribution), (2) rare category analysis model f (·) is
often trained with scarcity labels, and (3) the learning process of rare category analysis
model f (·) may frequently involve oracles and operate in a human-in-the-loop fashion (see
Figure 5 for rare category exploration). Simply replacing f (·) with a conventional interpretable
machine learning models may deteriorate the prediction performance by providing misleading
characterizations or injecting additional bias [74].

There have been a few attempts in the visualization domain to address Problem 6 given the
aforementioned challenges. For example, RCLens [81] is an interactive visual analytic system that is
designed to explore and identify rare category examples with the guidance of end-users. Figure 11
presents the user interface of RCLens, which actively visualizes and interprets the three learning
phases of rare category analysis models to end-users. In the data exploration phase (shown in
subfigure a), the system conducts a personalized visualization of the data via a data querying and
filtering mechanism; in the feature selection phase (shown in subfigure a), the system provides
relevant clues and statistics (e.g., correlations of features) for end-users to investigate the feature
dimensions; and in the rare category analysis model (shown in subfigure c), the system visualizes
the identified rare categories to end-users and then refines the predictions by leveraging the users’
feedback.

Pan et al. [105] proposes a visual analytic system named RCAnalyzer for studying rare cate-
gory patterns in dynamic systems. The user interface of RCAnalyzer is shown in Figure 12, which
includes (a) the timeline view showing an overview of the given dynamic networks; (b) the ma-
trices view showing the neighborhood contextual information of each node; (c) the example view
showing the feature distribution of rare patterns; and (d) the label result view showing the history

ACM Computing Surveys, Vol. 56, No. 5, Article 123. Publication date: November 2023.

---

<!-- PAGE 24 -->

123:24

D. Zhou and J. He

Table 2. Publicly Accessible Real-World Datasets for Rare Category Analysis

Data Type
Tabular Data
Tabular Data
Tabular Data
Tabular Data
Tabular Data
Tabular Data
Tabular Data
Tabular Data
Time-series Data
Time-series Data
Time-series Data
Graph Data
Graph Data
Graph Data

Dataset
20NewsGroup [68]
Donors [106]
Census [35]
Fraud [114]
UNSW-NB 15 [99]
URL [86]
Campaign data [35]
Thyroid [35]
Vandal [73]
Spam [139]
HDFS [145]
Tox21 [87]
ENZYMES [19]
NCI1 [137]

Description of Rare Categories
Rare topics of newspapers
Outstanding projects proposed by K-12 teachers
High-income people in U.S. census bureau database
Fraudulent credit card transaction
Network intrusion
Malicious URLs
Rarely successful campaigning records
Rare disease
Wikipedia vandal warning
Web spams
System errors
Toxic environmental chemicals
Abnormal proteins
Abnormal chemical compounds

prediction results as well as the model diagnosis. To ensure the interpretability of rare category
analysis models, the system is able to actively visualize each identified rare example in context (e.g.,
neighborhood structures in the adjacent timestamps) to help oracles understand and examine the
prediction results.

5 DATASETS AND REPRESENTATIVE METHODS

This section summarizes the popular evaluation datasets and representative algorithms across dif-
ferent data types and downstream tasks.

5.1 Datasets
Although rare categories are prevalent across various domains (e.g., finance), collecting and an-
notating rare examples is extremely time-consuming and labor-intensive (e.g., annotating money
laundering activities). Early studies (e.g., [48, 50, 52, 53, 109]) evaluate their models on synthetic
or semi-synthetic datasets that are either generated from a pre-defined data distribution or ma-
nipulated from public benchmark datasets. However, evaluations performed on synthetic or semi-
synthetic datasets may not reflect the performance of rare category analysis models in real-world
applications. To promote the further development of rare category analysis, Table 2 summarizes
some public benchmark datasets, whose data range from tabular data to graph-structured data,
from static data to dynamic data.

5.2 Representative Methods

Comparison evaluation with representative algorithms serves a pivotal role in the development
of machine learning algorithms. In Table 3, we enumerate and summarize 25 representative rare
category analysis algorithms w.r.t. data type (i.e., tabular data, time-series data, graph data) and
downstream task (i.e., exploration, exploitation, representation, and visualization). Since the meth-
ods in Table 3 have been developed for diverse tasks and datasets, we are unable to provide
a meta-analysis of their performance in a unified setting. Instead, to provide insight and an
in-depth understanding of the methods, we summarize our major observations as follows: (i)
most methods are designed in an unsupervised or semi-supervised setting, (ii) sampling-based
methods [135, 163] and anomaly-detection-based methods [132, 158] are still the mainstream

ACM Computing Surveys, Vol. 56, No. 5, Article 123. Publication date: November 2023.

---

<!-- PAGE 25 -->

Rare Category Analysis for Complex Data: A Review

123:25

Table 3. Representative Algorithms in Data Perspective

Algorithm
NNDB [52]
ACT [141]
SEDER [50]
HMS [135]
MUVIR [163]
RACH [54]
MLAN [104]
RCLens [81]
SUITS [80]
CDLC [18]

Data Type
Tabular Data
Tabular Data
Tabular Data
Tabular Data
Tabular Data
Tabular Data
Tabular Data
Tabular Data
Time-series Data
Time-series Data
Time-series Data MatrixProfile [150]
Time-series Data
Time-series Data
Time-series Data
Graph Data
Graph Data
Graph Data
Graph Data
Graph Data
Graph Data
Graph Data
Graph Data
Graph Data
Graph Data
Graph Data

BIRAD [164]
RRCF [43]
Sand [46]
Oddball [6]
NrMF [132]
HiDDen [158]
FocusCO [110]
BIRD [168]
StreamSpot [90]
AnomRank [153]
SPARC [166]
HOSPLOC [170]
L-MEGA [38]
RCAnalyzer [105]

Task
Rare Category Exploration
Rare Category Exploration
Rare Category Exploration
Rare Category Exploration
Rare Category Exploitation
Rare Category Exploitation
Rare Category Exploitation
Rare Category Visualization
Rare Category Exploration
Rare Category Exploration
Rare Category Exploration
Rare Category Exploration & Exploitation
Rare Category Exploration
Rare Category Exploitation
Rare Category Exploration
Rare Category Exploration
Rare Category Exploration
Rare Category Exploration
Rare Category Exploration
Rare Category Exploration
Rare Category Exploration
Rare Category Exploitation & Representation
Rare Category Exploitation
Rare Category Exploitation
Rare Category Visualization

solutions in rare category exploration, and (iii) rare category visualization and interpretation are
under explored.

6 CONCLUSION AND FUTURE DIRECTIONS

Departing from the previous surveys, this article presented a comprehensive pipeline of recent ad-
vances in rare category analysis. We started from the de-novo step without any label information
and surveyed rare category exploration techniques in the setting of homogeneous data and het-
erogeneous data. Then, we reviewed rare category exploitation methods that aim to characterize
a compact representation of the minority classes in order to discover all the rare examples with
high accuracy. Finally, we discussed the problem of rare category explanation, and in particular,
how to learn a salient representation of rare categories and interpret the prediction results. De-
spite the significant developments in rare category analysis, there remain some exciting research
opportunities

• Rare Category Generation. To meet the dramatically increasing demand for machine learning
systems as service providers (e.g., social networking, online advertising, data security), a mas-
sive amount of data has been generated and collected from a variety of domains. However,
the collected rare data are often noisy, sparse, few-shot annotated, and evolving over time.
Directly training machine learning models from the raw data would introduce inevitable

ACM Computing Surveys, Vol. 56, No. 5, Article 123. Publication date: November 2023.

---

<!-- PAGE 26 -->

123:26

D. Zhou and J. He

model bias and largely degrade the model performance in downstream applications (e.g.,
rare category characterization, rare category explanation). Moreover, the ever-increasing
size of data, together with the difficulty of releasing and sharing them, has made data gener-
ation a fundamental problem that is key for many high-impact applications, including fraud
detection, recommendation, and data security, among others. Hence, it is critical to develop
deep generative models that enable scalable modeling of real data to extract key contextual
information, distill knowledge, and generate plausible patterns for data augmentation in rare
category analysis.

• Long-Tail Category Analysis. In the past decade, deep learning has achieved remarkable suc-
cess in various learning tasks (e.g., image classification, speech recognition, link prediction)
through the training of “big models” on “big data.” However, unlike these well-studied tasks
(e.g., image classification over domestic cats and wild cats) with rich training data, the vast
majority of real-world entities and patterns (e.g., identification of honest employees and
malicious insiders in a large institution) are under explored and lack the observational and
annotated data that often correspond to the “long-tail” categories. Unlike existing works
on rare category analysis that focus on one or a few rare categories, here we face a massive
number of underrepresented categories from a “long-tail” distribution. Moreover, the current
machine learning systems are mostly tailored to specific learning scenarios, prevent them
from delivering on their promises in detecting the targets of interest in the presence of distri-
bution changes (e.g., dynamic systems). Two fundamental research questions thus emerge:
(Q1) How can we comprehend such massive “long-tail” categories given the inherent paucity of
observational and annotated data? (Q2) How can we capture the targets of interest (e.g., rare
category examples) given a novel data distribution?

• Robust Rare Category Analysis. Robust rare category analysis is another fundamental yet
quite open research problem that is attracting a surge of attention from many high-impact
domains (e.g., spam detection, financial fraud, system diagnosis). For example, in financial
fraud detection: How can we measure entity sensitivity, algorithmic robustness, task hardness,
and model generalization, given a prediction model? How can we achieve operational robust-
ness and adversarial robustness in the presence of the external disturbances (e.g., noise, miss-
ing values, outliers, adversarial attacks)? Despite the extensive work on adversarial machine
learning, the vast majority of the previous studies assume a balanced data distribution while
neglecting realistic cases in which the data are highly skewed, and the targets of interest are
underrepresented. Compared to conventional machine learning tools, rare category analysis
models are more sensitive and vulnerable in the presence of adversarial attacks due to the
rarity, non-separability, and label scarcity of rare category examples.

• Human–AI Collaborative Rare Category Analysis. Many industries follow highly regulated
processes that require rare category analysis models to be interpretable and human experts
to be involved in the prediction loop. The human-in-the-loop fashion [24, 52] enables rare
category analysis models to leverage human intelligence to alleviate the label scarcity issue
and improve the prediction performance in high-stake applications, such as failure predic-
tion in safety-critical systems and rare disease diagnosis in health care. However, as hu-
man intelligence is naturally a black box to AI models, a fundamental research question
remains nascent: How can we gain a deeper understanding of the underlying mechanism of
human intelligence, thus enabling unimpeded knowledge transfer between human intelligence
and AI? A promising but challenging research direction lies in how to build an integrated
and interactive system for accurate and trustworthy human–AI collaborative rare category
analysis.

ACM Computing Surveys, Vol. 56, No. 5, Article 123. Publication date: November 2023.

---

<!-- PAGE 27 -->

Rare Category Analysis for Complex Data: A Review

123:27

REFERENCES

[1] Steven P. Abney. 2002. Bootstrapping. In 40th Annual Meeting of the Association for Computational Linguistics (ACL),

pages 360–367.

[2] Manoj Acharya, Anirban Roy, Kaushik Koneripalli, Susmit Jha, Christopher Kanan, and Ajay Divakaran. 2022. De-
tecting out-of-context objects using graph contextual reasoning network. In 31st International Joint Conference
on Artificial Intelligence (IJCAI 2022) (Vienna, Austria, 23–29 July 2022), Luc De Raedt (Ed.). ijcai.org, 629–635.
https://doi.org/10.24963/ijcai.2022/89

[3] Prerna Agarwal, Richa Verma, Ayush Agarwal, and Tanmoy Chakraborty. 2018. DyPerm: Maximizing permanence
for dynamic community detection. In Pacific-Asia Conference on Knowledge Discovery and Data Mining. Springer,
437–449.

[4] Amirhossein Ahmadian and Fredrik Lindsten. 2021. Likelihood-free out-of-distribution detection with invertible gen-
erative models. In 30th International Joint Conference on Artificial Intelligence (IJCAI 2021), (Virtual Event / Montreal,
Canada, 19–27 August 2021), Zhi-Hua Zhou (Ed.). ijcai.org, 2119–2125. https://doi.org/10.24963/ijcai.2021/292
[5] Leman Akoglu and Christos Faloutsos. 2010. Event detection in time series of mobile communication graphs. In

Army Science Conference, Vol. 1.

[6] Leman Akoglu, Mary McGlohon, and Christos Faloutsos. 2010. Oddball: Spotting anomalies in weighted graphs. In

Pacific-Asia Conference on Knowledge Discovery and Data Mining. Springer, 410–421.

[7] Leman Akoglu, Hanghang Tong, and Danai Koutra. 2015. Graph based anomaly detection and description: A survey.

Data Mining and Knowledge Discovery 29, 3 (2015), 626–688.

[8] Samir Al-Stouhi and Chandan K. Reddy. 2016. Transfer learning for class imbalance problems with inadequate data.

Knowl. Inf. Syst. 48, 1 (2016), 201–228. https://doi.org/10.1007/s10115-015-0870-3

[9] Alejandro Marcos Alvarez, Makoto Yamada, Akisato Kimura, and Tomoharu Iwata. 2013. Clustering-based anomaly
detection in multi-view data. In 22nd ACM International Conference on Information and Knowledge Management
(CIKM’13) (San Francisco, CA, October 27–November 1, 2013), Qi He, Arun Iyengar, Wolfgang Nejdl, Jian Pei, and
Rajeev Rastogi (Eds.). ACM, 1545–1548. https://doi.org/10.1145/2505515.2507840

[10] Mehrnaz Amjadi and Theja Tulabandhula. 2018. Block-structure based time-series models for graph sequences. arXiv

preprint arXiv:1804.08796 (2018).

[11] Reid Andersen, Fan R. K. Chung, and Kevin J. Lang. 2006. Local graph partitioning using pagerank vectors. In 47th
Annual IEEE Symposium on Foundations of Computer Science (FOCS 2006) (21–24 October 2006, Berkeley, California).
IEEE Computer Society, 475–486. https://doi.org/10.1109/FOCS.2006.44

[12] Jerone Andrews, Thomas Tanay, Edward J. Morton, and Lewis D. Griffin. 2016. Transfer representation-learning for

anomaly detection. Journal of Machine Learning Research.

[13] Ana Paula Appel, Renato L. F. Cunha, Charu C. Aggarwal, and Marcela Megumi Terakado. 2018. Temporally evolving
community detection and prediction in content-centric networks. In Joint European Conference on Machine Learning
and Knowledge Discovery in Databases. Springer, 3–18.

[14] Miguel Araujo, Spiros Papadimitriou, Stephan Günnemann, Christos Faloutsos, Prithwish Basu, Ananthram Swami,
Evangelos E Papalexakis, and Danai Koutra. 2014. Com2: Fast automatic discovery of temporal (‘comet’) communities.
In Pacific-Asia Conference on Knowledge Discovery and Data Mining. Springer, 271–283.

[15] Alejandro Barredo Arrieta, Natalia Díaz-Rodríguez, Javier Del Ser, Adrien Bennetot, Siham Tabik, Alberto Barbado,
Salvador García, Sergio Gil-López, Daniel Molina, Richard Benjamins, Raja Chatila, and Francisco Herrera. 2020.
Explainable artificial intelligence (XAI): Concepts, taxonomies, opportunities and challenges toward responsible AI.
Information Fusion 58 (2020), 82–115.

[16] Fatemeh Azmandian, Ayse Yilmazer, Jennifer G. Dy, Javed A. Aslam, and David R. Kaeli. 2012. GPU-accelerated
feature selection for outlier detection using the local kernel density ratio. In 12th IEEE International Conference
on Data Mining (ICDM 2012) (Brussels, Belgium, December 10–13, 2012), Mohammed Javeed Zaki, Arno Siebes,
Jeffrey Xu Yu, Bart Goethals, Geoffrey I. Webb, and Xindong Wu (Eds.). IEEE Computer Society, 51–60. https:
//doi.org/10.1109/ICDM.2012.51

[17] Michael J. Bamshad, Sarah B. Ng, Abigail W. Bigham, Holly K. Tabor, Mary J. Emond, Deborah A. Nickerson, and
Jay Shendure. 2011. Exome sequencing as a tool for Mendelian disease gene discovery. Nature Reviews Genetics 12,
11 (2011), 745.

[18] Nurjahan Begum and Eamonn Keogh. 2014. Rare time series motif discovery from unbounded streams. Proceedings

of the VLDB Endowment 8, 2 (2014), 149–160.

[19] Karsten M. Borgwardt, Cheng Soon Ong, Stefan Schönauer, S. V. N. Vishwanathan, Alexander J. Smola, and Hans-
Peter Kriegel. 2005. Protein function prediction via graph kernels. In 13th International Conference on Intelligent Sys-
tems for Molecular Biology 2005 (Detroit, MI, 25–29 June 2005). 47–56. https://doi.org/10.1093/bioinformatics/bti1007
[20] Paula Branco, Luís Torgo, and Rita P. Ribeiro. 2016. A survey of predictive modeling on imbalanced domains. ACM

Computing Surveys (CSUR) 49, 2 (2016), 31.

ACM Computing Surveys, Vol. 56, No. 5, Article 123. Publication date: November 2023.

---

<!-- PAGE 28 -->

123:28

D. Zhou and J. He

[21] Suratna Budalakoti, Ashok N. Srivastava, Ram Akella, and Eugene Turkov. 2006. Anomaly detection in large sets of
high-dimensional symbol sequences. Technical Report NASA TM-2006-214553, NASA Ames Research Center, 2006.
[22] Lei Cao, Di Yang, Qingyang Wang, Yanwei Yu, Jiayuan Wang, and Elke A. Rundensteiner. 2014. Scalable distance-
based outlier detection over high-volume data streams. In 2014 IEEE 30th International Conference on Data Engineering.
IEEE, 76–87.

[23] Aldo G. Carranza, Ryan A. Rossi, Anup Rao, and Eunyee Koh. 2020. Higher-order clustering in complex heteroge-
neous networks. In The 26th ACM SIGKDD Conference on Knowledge Discovery and Data Mining (KDD’20) (Virtual
Event, CA, August 23–27, 2020), Rajesh Gupta, Yan Liu, Jiliang Tang, and B. Aditya Prakash (Eds.). ACM, 25–35.
https://doi.org/10.1145/3394486.3403045

[24] Chengliang Chai, Lei Cao, Guoliang Li, Jian Li, Yuyu Luo, and Samuel Madden. 2020. Human-in-the-loop outlier
detection. In 2020 International Conference on Management of Data (SIGMOD Conference 2020), (Online Conference
[Portland, OR], June 14–19, 2020), David Maier, Rachel Pottinger, AnHai Doan, Wang-Chiew Tan, Abdussalam Alaw-
ini, and Hung Q. Ngo (Eds.). ACM, 19–33. https://doi.org/10.1145/3318464.3389772

[25] Raghavendra Chalapathy and Sanjay Chawla. 2019. Deep learning for anomaly detection: A survey. arXiv preprint

arXiv:1901.03407 (2019).

[26] Varun Chandola, Arindam Banerjee, and Vipin Kumar. 2009. Anomaly detection: A survey. ACM Computing Surveys

(CSUR) 41, 3 (2009), 15.

[27] Varun Chandola, Arindam Banerjee, and Vipin Kumar. 2010. Anomaly detection for discrete sequences: A survey.

IEEE Transactions on Knowledge and Data Engineering 24, 5 (2010), 823–839.

[28] Chaomei Chen. 2006. CiteSpace II: Detecting and visualizing emerging trends and transient patterns in scientific

literature. Journal of the American Society for Information Science and Technology 57, 3 (2006), 359–377.

[29] Chengwei Chen, Yuan Xie, Shaohui Lin, Angela Yao, Guannan Jiang, Wei Zhang, Yanyun Qu, Ruizhi Qiao, Bo Ren, and
Lizhuang Ma. 2022. Comprehensive regularization in a bi-directional predictive network for video anomaly detection.
In 36th AAAI Conference on Artificial Intelligence (AAAI 2022), 34th Conference on Innovative Applications of Artificial
Intelligence (IAAI 2022), 12th Symposium on Educational Advances in Artificial Intelligence (EAAI 2022) (Virtual Event,
February 22–March 1, 2022). AAAI Press, 230–238. https://ojs.aaai.org/index.php/AAAI/article/view/19898

[30] Xuan Hong Dang, Barbora Micenková, Ira Assent, and Raymond T. Ng. 2013. Local outlier detection with interpre-
tation. In Joint European Conference on Machine Learning and Knowledge Discovery in Databases. Springer, 304–320.
[31] Arun Das and Paul Rad. 2020. Opportunities and challenges in explainable artificial intelligence (XAI): A survey.

arXiv preprint arXiv:2006.11371 (2020).

[32] Ailin Deng, Adam Goodge, Lang Yi Ang, and Bryan Hooi. 2022. CADET: Calibrated anomaly detection for mitigating
hardness bias. In 31st International Joint Conference on Artificial Intelligence (IJCAI 2022), (Vienna, Austria, 23–29 July
2022), Luc De Raedt (Ed.). ijcai.org, 2002–2008. https://doi.org/10.24963/ijcai.2022/278

[33] Ailin Deng and Bryan Hooi. 2021. Graph neural network-based anomaly detection in multivariate time series. In
35th AAAI Conference on Artificial Intelligence (AAAI 2021), 33rd Conference on Innovative Applications of Artificial
Intelligence (IAAI 2021), 11th Symposium on Educational Advances in Artificial Intelligence (EAAI 2021), (Virtual Event,
February 2–9, 2021). AAAI Press, 4027–4035. https://ojs.aaai.org/index.php/AAAI/article/view/16523

[34] Songgaojun Deng, Huzefa Rangwala, and Yue Ning. 2019. Learning dynamic context graphs for predicting social
events. In 25th ACM SIGKDD International Conference on Knowledge Discovery & Data Mining. ACM, 1007–1016.

[35] Dheeru Dua and Casey Graff. 2017. UCI Machine Learning Repository. http://archive.ics.uci.edu/ml
[36] Michael Edward Edge and Pedro R. Falcone Sampaio. 2009. A survey of signature based methods for financial fraud

detection. Computers & Security 28, 6 (2009), 381–394.

[37] Bradley Efron and Robert Tibshirani. 1996. Using specially designed exponential families for density estimation. The

Annals of Statistics 24, 6 (1996), 2431–2461.

[38] Dongqi Fu, Dawei Zhou, and Jingrui He. 2020. Local motif clustering on time-evolving graphs. In 26th ACM SIGKDD
Conference on Knowledge Discovery and Data Mining (KDD ’20), (Virtual Event, CA, August 23–27, 2020), Rajesh Gupta,
Yan Liu, Jiliang Tang, and B. Aditya Prakash (Eds.). ACM, 390–400. https://doi.org/10.1145/3394486.3403081

[39] Dongqi Fu, Dawei Zhou, Ross Maciejewski, Arie Croitoru, Marcus Boyd, and Jingrui He. 2023. Fairness-aware clique-
preserving spectral clustering of temporal graphs. In ACM Web Conference 2023 (WWW 2023), (Austin, TX, 30 April
2023–4 May 2023)., Ying Ding, Jie Tang, Juan F. Sequeda, Lora Aroyo, Carlos Castillo, and Geert-Jan Houben (Eds.).
ACM, 3755–3765. https://doi.org/10.1145/3543507.3583423

[40] Jing Gao, Wei Fan, Deepak Turaga, Srinivasan Parthasarathy, and Jiawei Han. 2011. A spectral framework for detect-
ing inconsistency across multi-source object relationships. In 2011 IEEE 11th International Conference on Data Mining
(ICDM). IEEE, 1050–1055.

[41] Yuan Gao, Xiang Wang, Xiangnan He, Zhenguang Liu, Huamin Feng, and Yongdong Zhang. 2023. Addressing het-
erophily in graph anomaly detection: A perspective of graph spectrum. In ACM Web Conference 2023, WWW 2023,
Austin, TX, USA, 30 April 2023–4 May 2023, Ying Ding, Jie Tang, Juan F. Sequeda, Lora Aroyo, Carlos Castillo, and
Geert-Jan Houben (Eds.). ACM, 1528–1538. https://doi.org/10.1145/3543507.3583268

ACM Computing Surveys, Vol. 56, No. 5, Article 123. Publication date: November 2023.

---

<!-- PAGE 29 -->

Rare Category Analysis for Complex Data: A Review

123:29

[42] Adam Goodge, Bryan Hooi, See-Kiong Ng, and Wee Siong Ng. 2022. LUNAR: Unifying local outlier detection
methods via graph neural networks. In 36th AAAI Conference on Artificial Intelligence (AAAI 2022), 34th Con-
ference on Innovative Applications of Artificial Intelligence (IAAI 2022), 12th Symposium on Educational Advances
in Artificial Intelligence (EAAI 2022) (Virtual Event, February 22–March 1, 2022). AAAI Press, 6737–6745. https:
//ojs.aaai.org/index.php/AAAI/article/view/20629

[43] Sudipto Guha, Nina Mishra, Gourav Roy, and Okke Schrijvers. 2016. Robust random cut forest based anomaly detec-

tion on streams. In International Conference on Machine Learning. 2712–2721.

[44] David Gunning, Mark Stefik, Jaesik Choi, Timothy Miller, Simone Stumpf, and Guang-Zhong Yang. 2019. XAI-

explainable artificial intelligence. Science Robotics 4, 37 (2019), eaay7120.

[45] Manish Gupta, Jing Gao, Charu C. Aggarwal, and Jiawei Han. 2013. Outlier detection for temporal data: A survey.

IEEE Transactions on Knowledge and Data Engineering 26, 9 (2013), 2250–2267.

[46] Ahsanul Haque, Latifur Khan, and Michael Baron. 2016. SAND: Semi-supervised adaptive novel class detection and

classification over data stream. In AAAI Conference on Artificial Intelligence.

[47] D. M. Hawkins. 1980. Identification of Outliers. Springer. https://doi.org/10.1007/978-94-015-3994-4
[48] Haibo He and Edwardo A. Garcia. 2009. Learning from imbalanced data. IEEE Transactions on Knowledge and Data

Engineering 21, 9 (2009), 1263–1284.

[49] Jingrui He. 2010. Rare Category Analysis. Ph.D. Dissertation. Carnegie Mellon University, Pittsburgh, PA.
[50] Jingrui He and Jaime Carbonell. 2009. Prior-free rare category detection. In 2009 SIAM International Conference on

Data Mining. SIAM, 155–163.

[51] Jingrui He and Jaime Carbonell. 2010. Coselection of features and instances for unsupervised rare category analysis.

Statistical Analysis and Data Mining: The ASA Data Science Journal 3, 6 (2010), 417–430.

[52] Jingrui He and Jaime G. Carbonell. 2008. Nearest-neighbor-based active learning for rare category detection. In

Advances in Neural Information Processing Systems. 633–640.

[53] Jingrui He, Yan Liu, and Richard Lawrence. 2008. Graph-based rare category detection. In 8th IEEE International

Conference on Data Mining, 2008 (ICDM’08). IEEE, 833–838.

[54] Jingrui He, Hanghang Tong, and Jaime Carbonell. 2010. Rare category characterization. In 10th IEEE International

Conference on Data Mining (ICDM). IEEE, 226–235.

[55] Jingrui He, Hanghang Tong, and Jaime Carbonell. 2012. An effective framework for characterizing rare categories.

Frontiers of Computer Science 6, 2 (2012), 154–165.

[56] Zengyou He, Xiaofei Xu, and Shengchun Deng. 2003. Discovering cluster-based local outliers. Pattern Recognit. Lett.

24, 9-10 (2003), 1641–1650. https://doi.org/10.1016/S0167-8655(03)00003-5

[57] Victoria Hodge and Jim Austin. 2004. A survey of outlier detection methodologies. Artificial Intelligence Review 22,

2 (2004), 85–126.

[58] Steven A. Hofmeyr, Stephanie Forrest, and Anil Somayaji. 1998. Intrusion detection using sequences of system calls.

Journal of Computer Security 6, 3 (1998), 151–180.

[59] Alexandre Hollocou, Julien Maudet, Thomas Bonald, and Marc Lelarge. 2017. A streaming algorithm for graph clus-

tering. CoRR abs/1712.04337 (2017). arXiv:1712.04337 http://arxiv.org/abs/1712.04337

[60] Chen Huang, Yining Li, Chen Change Loy, and Xiaoou Tang. 2016. Learning deep representation for imbalanced

classification. In IEEE Conference on Computer Vision and Pattern Recognition. 5375–5384.

[61] Tsuyoshi Idé, Amit Dhurandhar, Jirí Navrátil, Moninder Singh, and Naoki Abe. 2021. Anomaly attribution with
likelihood compensation. In 35th AAAI Conference on Artificial Intelligence (AAAI 2021), 33rd Conference on Innovative
Applications of Artificial Intelligence (IAAI 2021), 11th Symposium on Educational Advances in Artificial Intelligence
(EAAI 2021), (Virtual Event, February 2–9, 2021). AAAI Press, 4131–4138. https://ojs.aaai.org/index.php/AAAI/article/
view/16535

[62] Tsuyoshi Idé, Dzung T. Phan, and Jayant Kalagnanam. 2017. Multi-task multi-modal models for collective anomaly
detection. In 2017 IEEE International Conference on Data Mining (ICDM 2017) (New Orleans, LA, November 18–21,
2017), Vijay Raghavan, Srinivas Aluru, George Karypis, Lucio Miele, and Xindong Wu (Eds.). IEEE Computer Society,
177–186. https://doi.org/10.1109/ICDM.2017.27

[63] Tomoharu Iwata and Makoto Yamada. 2016. Multi-view anomaly detection via robust probabilistic latent variable

models. In Advances In Neural Information Processing Systems. 1136–1144.

[64] Tomoharu Iwata and Makoto Yamada. 2016. Multi-view anomaly detection via robust probabilistic latent vari-
able models. In Advances in Neural Information Processing Systems 29: Annual Conference on Neural Information
Processing Systems 2016, (December 5–10, 2016, Barcelona, Spain), Daniel D. Lee, Masashi Sugiyama, Ulrike von
Luxburg, Isabelle Guyon, and Roman Garnett (Eds.). 1136–1144. https://proceedings.neurips.cc/paper/2016/hash/
0f96613235062963ccde717b18f97592-Abstract.html

[65] H. V. Jagadish, Nick Koudas, and S. Muthukrishnan. 1999. Mining deviants in a time series database. In VLDB, Vol. 99.

7–10.

ACM Computing Surveys, Vol. 56, No. 5, Article 123. Publication date: November 2023.

---

<!-- PAGE 30 -->

123:30

D. Zhou and J. He

[66] Miltiadis Kandias, Alexios Mylonas, Nikos Virvilis, Marianthi Theoharidou, and Dimitris Gritzalis. 2010. An insider
threat prediction model. In International Conference on Trust, Privacy and Security in Digital Business. Springer, 26–37.
[67] Ramneet Kaur, Susmit Jha, Anirban Roy, Sangdon Park, Edgar Dobriban, Oleg Sokolsky, and Insup Lee. 2022.
iDECODe: In-distribution equivariance for conformal out-of-distribution detection. In 36th AAAI Conference on Ar-
tificial Intelligence (AAAI 2022), 34th Conference on Innovative Applications of Artificial Intelligence (IAAI 2022), 12th
Symposium on Educational Advances in Artificial Intelligence (EAAI 2022) (Virtual Event, February 22–March 1, 2022).
AAAI Press, 7104–7114. https://ojs.aaai.org/index.php/AAAI/article/view/20670

[68] Fabian Keller, Emmanuel Müller, and Klemens Böhm. 2012. HiCS: High contrast subspaces for density-based outlier
ranking. In IEEE 28th International Conference on Data Engineering (ICDE 2012) (Washington, DC, [Arlington, Vir-
ginia], 1–5 April, 2012), Anastasios Kementsietsidis and Marcos Antonio Vaz Salles (Eds.). IEEE Computer Society,
1037–1048. https://doi.org/10.1109/ICDE.2012.88

[69] Kamran Khan, Saif Ur Rehman, Kamran Aziz, Simon Fong, and Sababady Sarasvady. 2014. DBSCAN: Past, present
and future. In 5th International Conference on the Applications of Digital Information and Web Technologies (ICADIWT
2014). IEEE, 232–238.

[70] Jon M. Kleinberg. 1998. Authoritative sources in a hyperlinked environment. In 9th Annual ACM-SIAM Symposium
on Discrete Algorithms (25–27 January 1998, San Francisco, California), Howard J. Karloff (Ed.). ACM/SIAM, 668–677.
http://dl.acm.org/citation.cfm?id=314613.315045

[71] Christine Klymko, David Gleich, and Tamara G. Kolda. 2014. Using triangles to improve community detection in

directed networks. arXiv preprint arXiv:1404.5874 (2014).

[72] Atsutoshi Kumagai, Tomoharu Iwata, and Yasuhiro Fujiwara. 2019. Transfer anomaly detection by inferring latent
domain representations. In Advances in Neural Information Processing Systems 32: Annual Conference on Neural In-
formation Processing Systems 2019 (NeurIPS 2019), (December 8–14, 2019, Vancouver, BC, Canada), Hanna M. Wallach,
Hugo Larochelle, Alina Beygelzimer, Florence d’Alché-Buc, Emily B. Fox, and Roman Garnett (Eds.). 2467–2477.
https://proceedings.neurips.cc/paper/2019/hash/7895fc13088ee37f511913bac71fa66f-Abstract.html

[73] Srijan Kumar, Francesca Spezzano, and V. S. Subrahmanian. 2015. VEWS: A Wikipedia vandal early warning system.
In 21th ACM SIGKDD International Conference on Knowledge Discovery and Data Mining (Sydney, NSW, Australia,
August 10–13, 2015), Longbing Cao, Chengqi Zhang, Thorsten Joachims, Geoffrey I. Webb, Dragos D. Margineantu,
and Graham Williams (Eds.). ACM, 607–616. https://doi.org/10.1145/2783258.2783367

[74] Himabindu Lakkaraju and Osbert Bastani. 2020. “How do I fool you?” Manipulating user trust via misleading black

box explanations. In AAAI/ACM Conference on AI, Ethics, and Society. 79–85.

[75] Doyup Lee, Yeongjae Cheon, and Wook-Shin Han. 2021. Regularizing attention networks for anomaly detection
in visual question answering. In 35th AAAI Conference on Artificial Intelligence (AAAI 2021), 33rd Conference on
Innovative Applications of Artificial Intelligence (IAAI 2021), 11th Symposium on Educational Advances in Artificial
Intelligence (EAAI 2021), (Virtual Event, February 2–9, 2021). AAAI Press, 1845–1853. https://ojs.aaai.org/index.php/
AAAI/article/view/16279

[76] Kevin H. Lee, Lingzhou Xue, and David R. Hunter. 2017. Model-based clustering of time-evolving networks through

temporal exponential-family random graph models. arXiv preprint arXiv:1712.07325 (2017).

[77] Dan Li, Dacheng Chen, Lei Shi, Baihong Jin, Jonathan Goh, and See-Kiong Ng. 2019. MAD-GAN: Multivariate anom-
aly detection for time series data with generative adversarial networks. arXiv preprint arXiv:1901.04997 (2019).
[78] Kai Li, Sheng Li, Zhengming Ding, Weidong Zhang, and Yun Fu. 2018. Latent discriminant subspace representations
for multi-view outlier detection. In 32nd AAAI Conference on Artificial Intelligence, (AAAI-18), 30th Innovative Appli-
cations of Artificial Intelligence (IAAI-18), and 8th AAAI Symposium on Educational Advances in Artificial Intelligence
(EAAI-18) (New Orleans, LA, February 2–7, 2018), Sheila A. McIlraith and Kilian Q. Weinberger (Eds.). AAAI Press,
3522–3529. https://www.aaai.org/ocs/index.php/AAAI/AAAI18/paper/view/17401

[79] Sheng Li, Ming Shao, and Yun Fu. 2015. Multi-view low-rank analysis for outlier detection. In 2015 SIAM International
Conference on Data Mining (Vancouver, BC, Canada, April 30–May 2, 2015), Suresh Venkatasubramanian and Jieping
Ye (Eds.). SIAM, 748–756. https://doi.org/10.1137/1.9781611974010.84

[80] Xiaolei Li and Jiawei Han. 2007. Mining approximate top-k subspace anomalies in multi-dimensional time-series
data. In Proceedings of the 33rd International Conference on Very Large Data Bases. VLDB Endowment, 447–458.
[81] Hanfei Lin, Siyuan Gao, David Gotz, Fan Du, Jingrui He, and Nan Cao. 2018. Rclens: Interactive rare category explo-

ration and identification. IEEE Transactions on Visualization and Computer Graphics 24, 7 (2018), 2223–2237.

[82] Wangli Lin, Li Sun, Qiwei Zhong, Can Liu, Jinghua Feng, Xiang Ao, and Hao Yang. 2021. Online credit payment
fraud detection via structure-aware hierarchical recurrent neural network. In 30th International Joint Conference on
Artificial Intelligence (IJCAI 2021) (Virtual Event/Montreal, Canada, 19–27 August 2021), Zhi-Hua Zhou (Ed.). ijcai.org,
3670–3676. https://doi.org/10.24963/ijcai.2021/505

[83] Boyang Liu, Pang-Ning Tan, and Jiayu Zhou. 2022. Unsupervised anomaly detection by robust density estimation.
In 36th AAAI Conference on Artificial Intelligence (AAAI 2022), 34th Conference on Innovative Applications of Artificial

ACM Computing Surveys, Vol. 56, No. 5, Article 123. Publication date: November 2023.

---

<!-- PAGE 31 -->

Rare Category Analysis for Complex Data: A Review

123:31

Intelligence (IAAI 2022), T12th Symposium on Educational Advances in Artificial Intelligence (EAAI 2022) (Virtual Event,
February 22–March 1, 2022). AAAI Press, 4101–4108. https://ojs.aaai.org/index.php/AAAI/article/view/20328
[84] Ninghao Liu, Donghwa Shin, and Xia Hu. 2017. Contextual outlier interpretation. arXiv preprint arXiv:1711.10589

(2017).

[85] Zhining Liu, Dawei Zhou, Yada Zhu, Jinjie Gu, and Jingrui He. 2020. Towards fine-grained temporal network
representation via time-reinforced random walk. In 34th AAAI Conference on Artificial Intelligence (AAAI 2020),
32nd Innovative Applications of Artificial Intelligence Conference (IAAI 2020), 10th AAAI Symposium on Educational
Advances in Artificial Intelligence (EAAI 2020) (New York, February 7–12, 2020). AAAI Press, 4973–4980. https:
//aaai.org/ojs/index.php/AAAI/article/view/5936

[86] Justin Ma, Lawrence K. Saul, Stefan Savage, and Geoffrey M. Voelker. 2009. Identifying suspicious URLs: An applica-
tion of large-scale online learning. In 26th Annual International Conference on Machine Learning (ICML 2009) (Mon-
treal, Quebec, Canada, June 14–18, 2009) (ACM International Conference Proceeding Series), Andrea Pohoreckyj Dany-
luk, Léon Bottou, and Michael L. Littman (Eds.), Vol. 382. ACM, 681–688. https://doi.org/10.1145/1553374.1553462

[87] Rongrong Ma, Guansong Pang, Ling Chen, and Anton van den Hengel. 2021. Deep graph-level anomaly detection
by glocal knowledge distillation. CoRR abs/2112.10063 (2021). arXiv:2112.10063 https://arxiv.org/abs/2112.10063
[88] Laurens van der Maaten and Geoffrey Hinton. 2008. Visualizing data using t-SNE. Journal of Machine Learning

Research 9 (Nov. 2008), 2579–2605.

[89] Meghanath Macha and Leman Akoglu. 2018. Explaining anomalies in groups with characterizing subspace rules.

Data Mining and Knowledge Discovery 32, 5 (2018), 1444–1480.

[90] Emaad Manzoor, Sadegh M. Milajerdi, and Leman Akoglu. 2016. Fast memory-efficient anomaly detection in stream-
ing heterogeneous graphs. In 22nd ACM SIGKDD International Conference on Knowledge Discovery and Data Mining.
ACM, 1035–1044.

[91] Alejandro Marcos Alvarez, Makoto Yamada, Akisato Kimura, and Tomoharu Iwata. 2013. Clustering-based anom-
aly detection in multi-view data. In 22nd ACM International Conference on Conference on Information & Knowledge
Management. ACM, 1545–1548.

[92] Markos Markou and Sameer Singh. 2003. Novelty detection: A review - Part 1: Statistical approaches. Signal Processing

83, 12 (2003), 2481–2497.

[93] Bhaskar Mehta, Saurabh Nangia, Manish Gupta, and Wolfgang Nejdl. 2008. Detecting image spam using visual fea-

tures and near duplicate detection. In 17th International Conference on World Wide Web. ACM, 497–506.

[94] Tomas Mikolov, Ilya Sutskever, Kai Chen, Greg S. Corrado, and Jeff Dean. 2013. Distributed representations of words

and phrases and their compositionality. In Advances in Neural Information Processing Systems. 3111–3119.

[95] Yifei Ming, Hang Yin, and Yixuan Li. 2022. On the impact of spurious correlation for out-of-distribution detection.
In 36th AAAI Conference on Artificial Intelligence (AAAI 2022), 34th Conference on Innovative Applications of Artificial
Intelligence (IAAI 2022), 12th Symposium on Educational Advances in Artificial Intelligence (EAAI 2022) (Virtual Event,
February 22–March 1, 2022). AAAI Press, 10051–10059. https://ojs.aaai.org/index.php/AAAI/article/view/21244

[96] Christoph Molnar. 2020. Interpretable Machine Learning. Lulu.com.
[97] Hossein Moradi Koupaie, Suhaimi Ibrahim, and Javad Hosseinkhani. 2014. Outlier detection in stream data by clus-
tering method. International Journal of Advanced Computer Science and Information Technology (IJACSIT) 2 (2014),
25–34.

[98] Peyman Morteza and Yixuan Li. 2022. Provable guarantees for understanding out-of-distribution detection. In 36th
AAAI Conference on Artificial Intelligence (AAAI 2022), 34th Conference on Innovative Applications of Artificial Intel-
ligence (IAAI 2022), 12th Symposium on Educational Advances in Artificial Intelligence (EAAI 2022) (Virtual Event,
February 22–March 1, 2022). AAAI Press, 7831–7840. https://ojs.aaai.org/index.php/AAAI/article/view/20752
[99] Nour Moustafa and Jill Slay. 2015. UNSW-NB15: A comprehensive data set for network intrusion detection systems
(UNSW-NB15 network data set). In 2015 Military Communications and Information Systems Conference (MilCIS 2015)
(Canberra, Australia, November 10–12, 2015). IEEE, 1–6. https://doi.org/10.1109/MilCIS.2015.7348942

[100] Shan Muthukrishnan, Rahul Shah, and Jeffrey Scott Vitter. 2004. Mining deviants in time series data streams. In 16th

International Conference on Scientific and Statistical Database Management, 2004. IEEE, 41–50.

[101] Alexandre Nairac, Neil Townsend, Roy Carr, Steve King, Peter Cowley, and Lionel Tarassenko. 1999. A system for

the analysis of jet engine vibration data. Integrated Computer-Aided Engineering 6, 1 (1999), 53–66.

[102] Eric W. T. Ngai, Yong Hu, Yiu Hing Wong, Yijun Chen, and Xin Sun. 2011. The application of data mining techniques
in financial fraud detection: A classification framework and an academic review of literature. Decision Support Sys-
tems 50, 3 (2011), 559–569.

[103] Giang Hoang Nguyen, John Boaz Lee, Ryan A. Rossi, Nesreen K. Ahmed, Eunyee Koh, and Sungchul Kim. 2018.
Continuous-time dynamic network embeddings. In Companion of the Web Conference 2018 (WWW 2018) (Lyon,
France, April 23–27, 2018), Pierre-Antoine Champin, Fabien Gandon, Mounia Lalmas, and Panagiotis G. Ipeirotis
(Eds.). ACM, 969–976. https://doi.org/10.1145/3184558.3191526

ACM Computing Surveys, Vol. 56, No. 5, Article 123. Publication date: November 2023.

---

<!-- PAGE 32 -->

123:32

D. Zhou and J. He

[104] Feiping Nie, Guohao Cai, and Xuelong Li. 2017. Multi-view clustering and semi-supervised classification with adap-
tive neighbours. In 31st AAAI Conference on Artificial Intelligence (February 4–9, 2017, San Francisco, California),
Satinder P. Singh and Shaul Markovitch (Eds.). AAAI Press, 2408–2414. http://aaai.org/ocs/index.php/AAAI/AAAI17/
paper/view/14833

[105] Jiacheng Pan, Dongming Han, Fangzhou Guo, Dawei Zhou, Nan Cao, Jingrui He, Mingliang Xu, and Wei Chen. 2020.
RCAnalyzer: Visual analytics of rare categories in dynamic networks. Frontiers Inf. Technol. Electron. Eng. 21, 4 (2020),
491–506. https://doi.org/10.1631/FITEE.1900310

[106] Guansong Pang, Chunhua Shen, and Anton van den Hengel. 2019. Deep anomaly detection with deviation networks.

In 25th ACM SIGKDD International Conference on Knowledge Discovery & Data Mining. 353–362.

[107] Guansong Pang, Anton van den Hengel, Chunhua Shen, and Longbing Cao. 2021. Toward deep supervised anomaly
detection: Reinforcement learning from partially labeled anomaly data. In 27th ACM SIGKDD Conference on Knowl-
edge Discovery and Data Mining (KDD ’21) (Virtual Event, Singapore, August 14–18, 2021), Feida Zhu, Beng Chin
Ooi, and Chunyan Miao (Eds.). ACM, 1298–1308. https://doi.org/10.1145/3447548.3467417

[108] Dhaval Patel. 2023. Time series anomaly detection tool: Hands of lab. In AAAI Conference on Artificial Intelligence.
[109] Dan Pelleg and Andrew W. Moore. 2005. Active learning for anomaly and rare-category detection. In Advances in

Neural Information Processing Systems. 1073–1080.

[110] Bryan Perozzi, Leman Akoglu, Patricia Iglesias Sánchez, and Emmanuel Müller. 2014. Focused clustering and outlier
detection in large attributed graphs. In 20th ACM SIGKDD International Conference on Knowledge Discovery and Data
Mining. ACM, 1346–1355.

[111] Bryan Perozzi, Rami Al-Rfou, and Steven Skiena. 2014. Deepwalk: Online learning of social representations. In 20th
ACM SIGKDD International Conference on Knowledge Discovery and Data Mining (August 24 - 27, 2014, New York, NY)
ACM, 701–710.

[112] Geo Pertea, Xiaoqiu Huang, Feng Liang, Valentin Antonescu, Razvan Sultana, Svetlana Karamycheva, Yuandan Lee,
Joseph White, Foo Cheung, Babak Parvizi, Jennifer Tsai, and John Quackenbush. 2003. TIGR gene indices clustering
tools (TGICL): A software system for fast clustering of large EST datasets. Bioinform. 19, 5 (2003), 651–652. https:
//doi.org/10.1093/bioinformatics/btg034

[113] Clifton Phua, Vincent Lee, Kate Smith, and Ross Gayler. 2010. A comprehensive survey of data mining-based fraud

detection research. arXiv preprint arXiv:1009.6119 (2010).

[114] Andrea Dal Pozzolo, Olivier Caelen, Reid A. Johnson, and Gianluca Bontempi. 2015. Calibrating probability with
undersampling for unbalanced classification. In IEEE Symposium Series on Computational Intelligence (SSCI 2015)
(Cape Town, South Africa, December 7–10, 2015). IEEE, 159–166. https://doi.org/10.1109/SSCI.2015.33

[115] Stephen Ranshous, Shitian Shen, Danai Koutra, Steve Harenberg, Christos Faloutsos, and Nagiza F. Samatova. 2015.
Anomaly detection in dynamic networks: A survey. Wiley Interdisciplinary Reviews: Computational Statistics 7,
3 (2015), 223–247.

[116] Umaa Rebbapragada, Pavlos Protopapas, Carla E. Brodley, and Charles Alcock. 2009. Finding anomalous periodic

time series. Machine Learning 74, 3 (2009), 281–313.

[117] Maurizio Scarpa, Zsuzsanna Almássy, Michael Beck, Olaf Bodamer, Iain A. Bruce, Linda De Meirleir, Nathalie Guf-
fon, Encarna Guillén-Navarro, Pauline Hensman, Simon Jones, et al. 2011. Mucopolysaccharidosis type II: European
recommendations for the diagnosis and multidisciplinary management of a rare disease. Orphanet Journal of Rare
Diseases 6, 1 (2011), 72.

[118] François Schnitzler, Thomas Liebig, Shie Mannor, Gustavo Souto, Sebastian Bothe, and Hendrik Stange. 2014. Het-
erogeneous stream processing for disaster detection and alarming. In IEEE International Conference on Big Data. IEEE
Press, 914–923.

[119] Karlton Sequeira and Mohammed Zaki. 2002. ADMIT: Anomaly-based data mining for intrusions. In 8th ACM

SIGKDD International Conference on Knowledge Discovery and Data Mining. ACM, 386–395.

[120] Shubhranshu Shekhar, Neil Shah, and Leman Akoglu. 2021. FairOD: Fairness-aware outlier detection. In AAAI/ACM
Conference on AI, Ethics, and Society (AIES ’21) (Virtual Event, May 19–21, 2021) Marion Fourcade, Benjamin Kuipers,
Seth Lazar, and Deirdre K. Mulligan (Eds.). ACM, 210–220. https://doi.org/10.1145/3461702.3462517

[121] Lifeng Shen, Zhongzhong Yu, Qianli Ma, and James T. Kwok. 2021. Time series anomaly detection with multiresolu-
tion ensemble decoding. In 35th AAAI Conference on Artificial Intelligence (AAAI 2021), 33rd Conference on Innovative
Applications of Artificial Intelligence (IAAI 2021), 11th Symposium on Educational Advances in Artificial Intelligence
(EAAI 2021) (Virtual Event, February 2–9, 2021). AAAI Press, 9567–9575. https://ojs.aaai.org/index.php/AAAI/article/
view/17152

[122] Xiang-Rong Sheng, De-Chuan Zhan, Su Lu, and Yuan Jiang. 2019. Multi-view anomaly detection: Neighborhood
in locality matters. In 33rd AAAI Conference on Artificial Intelligence (AAAI 2019), 31st Innovative Applications of
Artificial Intelligence Conference (IAAI 2019), 9th AAAI Symposium on Educational Advances in Artificial Intelligence
(EAAI 2019), (Honolulu, Hawaii, January 27–February 1, 2019). AAAI Press, 4894–4901. https://doi.org/10.1609/aaai.
v33i01.33014894

ACM Computing Surveys, Vol. 56, No. 5, Article 123. Publication date: November 2023.

---

<!-- PAGE 33 -->

Rare Category Analysis for Complex Data: A Review

123:33

[123] Jou Won Song, Kyeongbo Kong, Ye In Park, Seong Gyun Kim, and Suk-Ju Kang. 2021. AnoSeg: Anomaly segmen-
tation network using self-supervised learning. CoRR abs/2110.03396 (2021). arXiv:2110.03396 https://arxiv.org/abs/
2110.03396

[124] Daniel A. Spielman and Shang-Hua Teng. 2013. A local clustering algorithm for massive graphs and its application
to nearly linear time graph partitioning. SIAM J. Comput. 42, 1 (2013), 1–26. https://doi.org/10.1137/080744888
[125] Kumar Sricharan and Kamalika Das. 2014. Localizing anomalous changes in time-evolving graphs. In 2014 ACM

SIGMOD International Conference on Management of Data. ACM, 1347–1358.

[126] Jimeng Sun, Christos Faloutsos, Spiros Papadimitriou, and Philip S. Yu. 2007. Graphscope: Parameter-free mining of
large time-evolving graphs. In 13th ACM SIGKDD International Conference on Knowledge Discovery and Data Mining.
ACM, 687–696.

[127] Jimeng Sun, Huiming Qu, Deepayan Chakrabarti, and Christos Faloutsos. 2005. Neighborhood formation and anom-

aly detection in bipartite graphs. In 5th IEEE International Conference on Data Mining. IEEE, 418–425.

[128] Yi-Xuan Sun and Wei Wang. 2022. Exploiting mixed unlabeled data for detecting samples of seen and unseen out-
of-distribution classes. In 36th AAAI Conference on Artificial Intelligence (AAAI 2022), 34th Conference on Innova-
tive Applications of Artificial Intelligence (IAAI 2022), 12th Symposium on Educational Advances in Artificial Intelli-
gence (EAAI 2022) (Virtual Event, February 22–March 1, 2022). AAAI Press, 8386–8394. https://ojs.aaai.org/index.
php/AAAI/article/view/20814

[129] Ying Sun, Wenjun Wang, Nannan Wu, Wei Yu, and Xue Chen. 2020. Anomaly subgraph detection with feature
transfer. In 29th ACM International Conference on Information and Knowledge Management (CIKM ’20) (Virtual Event,
Ireland, October 19–23, 2020), Mathieu d’Aquin, Stefan Dietze, Claudia Hauff, Edward Curry, and Philippe Cudré-
Mauroux (Eds.). ACM, 1415–1424. https://doi.org/10.1145/3340531.3411968

[130] Jian Tang, Meng Qu, Mingzhe Wang, Ming Zhang, Jun Yan, and Qiaozhu Mei. 2015. LINE: Large-scale information
network embedding. In 24th International Conference on World Wide Web (WWW 2015) (Florence, Italy, May 18–22,
2015). 1067–1077.

[131] Erico Tjoa and Cuntai Guan. 2020. A survey on explainable artificial intelligence (XAI): Toward medical XAI. IEEE

Transactions on Neural Networks and Learning Systems 32, 11 (2020), 4793–4813.

[132] Hanghang Tong and Ching-Yung Lin. 2011. Non-negative residual matrix factorization with application to graph

anomaly detection. In 2011 SIAM International Conference on Data Mining. SIAM, 143–153.

[133] Jason Tumlinson. 2011. Astronomy: A new spin on the first stars. Nature 472, 7344 (2011), 426.
[134] Aaron Tuor, Samuel Kaplan, Brian Hutchinson, Nicole Nichols, and Sean Robinson. 2017. Deep learning for unsuper-
vised insider threat detection in structured cybersecurity data streams. In Workshops at the 31st AAAI Conference on
Artificial Intelligence.

[135] Pavan Vatturi and Weng-Keen Wong. 2009. Category detection using hierarchical mean shift. In 15th ACM SIGKDD

International Conference on Knowledge Discovery and Data Mining. ACM, 847–856.

[136] Vincent Vercruyssen, Wannes Meert, and Jesse Davis. 2020. Transfer learning for anomaly detection through local-
ized and unsupervised instance selection. In 34th Conference on Artificial Intelligence (AAAI 2020), 32nd Innovative
Applications of Artificial Intelligence Conference (IAAI 2020), 10th AAAI Symposium on Educational Advances in Artifi-
cial Intelligence (EAAI 2020) (New York February 7–12, 2020). AAAI Press, 6054–6061. https://aaai.org/ojs/index.php/
AAAI/article/view/6068

[137] Nikil Wale, Ian A. Watson, and George Karypis. 2008. Comparison of descriptor spaces for chemical compound
retrieval and classification. Knowl. Inf. Syst. 14, 3 (2008), 347–375. https://doi.org/10.1007/s10115-007-0103-5
[138] Zhen Wang and Chao Lan. 2020. Towards a hierarchical Bayesian model of multi-view anomaly detection. In 29th
International Joint Conference on Artificial Intelligence (IJCAI 2020), Christian Bessiere (Ed.). ijcai.org, 2420–2426.
https://doi.org/10.24963/ijcai.2020/335

[139] Steve Webb, James Caverlee, and Calton Pu. 2006. Introducing the Webb spam corpus: Using email spam to identify
web spam automatically. In 3rd Conference on Email and Anti-Spam (CEAS 2006) (July 27–28, 2006, Mountain View,
California). http://www.ceas.cc/2006/listabs.html#6.pdf

[140] James D. Wilson, Nathaniel T. Stevens, and William H. Woodall. 2016. Modeling and estimating change in temporal

networks via a dynamic degree corrected stochastic block model. arXiv preprint arXiv:1605.04049 (2016).

[141] Gang Wu and Edward Y. Chang. 2003. Adaptive feature-space conformal transformation for imbalanced-data learn-

ing. In 20th International Conference on Machine Learning (ICML-03). 816–823.

[142] Jun Wu, Jingrui He, and Yongming Liu. 2018. ImVerde: Vertex-diminished random walk for learning imbalanced

network representation. In 2018 IEEE International Conference on Big Data (Big Data). IEEE, 871–880.

[143] Shuang Wu, Jingyu Zhao, and Guangjian Tian. 2022. Understanding and mitigating data contamination in deep
anomaly detection: A kernel-based approach. In 31st International Joint Conference on Artificial Intelligence (IJCAI
2022) (Vienna, Austria, 23–29 July 2022) Luc De Raedt (Ed.). ijcai.org, 2319–2325. https://doi.org/10.24963/ijcai.2022/
322

ACM Computing Surveys, Vol. 56, No. 5, Article 123. Publication date: November 2023.

---

<!-- PAGE 34 -->

123:34

D. Zhou and J. He

[144] Dongbo Xi, Bowen Song, Fuzhen Zhuang, Yongchun Zhu, Shuai Chen, Tianyi Zhang, Yuan Qi, and Qing He. 2021.
Modeling the field value variations and field interactions simultaneously for fraud detection. In 35th AAAI Conference
on Artificial Intelligence (AAAI 2021), 33rd Conference on Innovative Applications of Artificial Intelligence (IAAI 2021),
11th Symposium on Educational Advances in Artificial Intelligence (EAAI 2021) (Virtual Event, February 2–9, 2021).
AAAI Press, 14957–14965. https://ojs.aaai.org/index.php/AAAI/article/view/17755

[145] Wei Xu, Ling Huang, Armando Fox, David A. Patterson, and Michael I. Jordan. 2009. Online system problem detection
by mining patterns of console logs. In 9th IEEE International Conference on Data Mining (ICDM 2009) (Miami, Florida,
6-9 December 2009) Wei Wang, Hillol Kargupta, Sanjay Ranka, Philip S. Yu, and Xindong Wu (Eds.). IEEE Computer
Society, 588–597. https://doi.org/10.1109/ICDM.2009.19

[146] Pei Yang, Jingrui He, and Jia-Yu Pan. 2015. Learning complex rare categories with dual heterogeneity. In 2015 SIAM

International Conference on Data Mining. SIAM, 523–531.

[147] Pei Yang, Hongxia Yang, Haoda Fu, Dawei Zhou, Jieping Ye, Theodoros Lappas, and Jingrui He. 2015. Jointly modeling
label and feature heterogeneity in medical informatics. ACM Transactions on Knowledge Discovery from Data (TKDD-
2015) (2015).

[148] Zhilin Yang, William W. Cohen, and Ruslan Salakhutdinov. 2016. Revisiting semi-supervised learning with graph
embeddings. In 33nd International Conference on Machine Learning (ICML 2016) (New York City, NY, June 19–24,
2016). 40–48.

[149] Yasser Yasami and Farshad Safaei. 2017. A statistical infinite feature cascade-based approach to anomaly detection

for dynamic social networks. Computer Communications 100 (2017), 52–64.

[150] Chin-Chia Michael Yeh, Yan Zhu, Liudmila Ulanova, Nurjahan Begum, Yifei Ding, Hoang Anh Dau, Diego Furtado
Silva, Abdullah Mueen, and Eamonn Keogh. 2016. Matrix profile I: All pairs similarity joins for time series: A unifying
view that includes motifs, discords and shapelets. In 2016 IEEE 16th International Conference on Data Mining (ICDM).
IEEE, 1317–1322.

[151] Hao Yin, Austin R. Benson, Jure Leskovec, and David F. Gleich. 2017. Local higher-order graph clustering. In Proceed-

ings of the 23rd ACM SIGKDD International Conference on Knowledge Discovery and Data Mining. ACM, 555–564.

[152] Hao Yin, Austin R. Benson, Jure Leskovec, and David F. Gleich. 2017. Local higher-order graph clustering. In 23rd
ACM SIGKDD International Conference on Knowledge Discovery and Data Mining (Halifax, NS, Canada, August 13–17,
2017). ACM, 555–564. https://doi.org/10.1145/3097983.3098069

[153] Minji Yoon, Bryan Hooi, Kijung Shin, and Christos Faloutsos. 2019. Fast and accurate anomaly detection in dynamic
graphs with a two-pronged approach. In 25th ACM SIGKDD International Conference on Knowledge Discovery & Data
Mining. ACM, 647–657.

[154] Bing Yu, Haoteng Yin, and Zhanxing Zhu. 2018. Spatio-temporal graph convolutional networks: A deep learning
framework for traffic forecasting. In 27th International Joint Conference on Artificial Intelligence (IJCAI 2018) (July
13–19, 2018, Stockholm, Sweden), Jérôme Lang (Ed.). ijcai.org, 3634–3640. https://doi.org/10.24963/ijcai.2018/505

[155] Wenchao Yu, Wei Cheng, Charu C. Aggarwal, Kai Zhang, Haifeng Chen, and Wei Wang. 2018. Netwalk: A flexible
deep embedding approach for anomaly detection in dynamic networks. In 24th ACM SIGKDD International Confer-
ence on Knowledge Discovery & Data Mining. ACM, 2672–2681.

[156] Changqing Zhang, Ehsan Adeli, Tao Zhou, Xiaobo Chen, and Dinggang Shen. 2018. Multi-layer multi-view classifi-
cation for Alzheimer’s disease diagnosis. In 32nd AAAI Conference on Artificial Intelligence (AAAI-18), 30th Innovative
Applications of Artificial Intelligence (IAAI-18), and 8th AAAI Symposium on Educational Advances in Artificial Intel-
ligence (EAAI-18) (New Orleans, Louisiana, February 2–7, 2018) Sheila A. McIlraith and Kilian Q. Weinberger (Eds.).
AAAI Press, 4406–4413. https://www.aaai.org/ocs/index.php/AAAI/AAAI18/paper/view/16864

[157] Guoxi Zhang, Tomoharu Iwata, and Hisashi Kashima. 2017. Robust multi-view topic modeling by incorporating de-
tecting anomalies. In Joint European Conference on Machine Learning and Knowledge Discovery in Databases. Springer,
238–250.

[158] Si Zhang, Dawei Zhou, Mehmet Yigit Yildirim, Scott Alcorn, Jingrui He, Hasan Davulcu, and Hanghang Tong. 2017.
HiDDen: Hierarchical dense subgraph detection with application to financial fraud detection. In 2017 SIAM Interna-
tional Conference on Data Mining. Society for Industrial and Applied Mathematics, 570–578.

[159] Weiqi Zhang, Chen Zhang, and Fugee Tsung. 2022. GRELEN: Multivariate time series anomaly detection from the
perspective of graph relational learning. In 31st International Joint Conference on Artificial Intelligence (IJCAI 2022)
(Vienna, Austria, 23–29 July 2022), Luc De Raedt (Ed.). ijcai.org, 2390–2397. https://doi.org/10.24963/ijcai.2022/332

[160] Handong Zhao and Yun Fu. 2015. Dual-regularized multi-view outlier detection.. In 24th International Joint Confer-

ence on Artificial Intelligence (IJCAI 2015). 4077–4083.

[161] Ying Zhao, Junjun Chen, Di Wu, Jian Teng, and Shui Yu. 2019. Multi-task network anomaly detection using feder-
ated learning. In 10th International Symposium on Information and Communication Technology (Hanoi, Ha Long Bay,
Vietnam, December 4–6, 2019). ACM, 273–279. https://doi.org/10.1145/3368926.3369705

ACM Computing Surveys, Vol. 56, No. 5, Article 123. Publication date: November 2023.

---

<!-- PAGE 35 -->

Rare Category Analysis for Complex Data: A Review

123:35

[162] Jia-Xing Zhong, Nannan Li, Weijie Kong, Shan Liu, Thomas H. Li, and Ge Li. 2019. Graph convolutional label noise
cleaner: Train a plug-and-play action classifier for anomaly detection. In IEEE Conference on Computer Vision and
Pattern Recognition. 1237–1246.

[163] Dawei Zhou, Jingrui He, K. Seluk Candan, and Hasan Davulcu. 2015. MUVIR: Multi-view rare category detection. In

24th International Joint Conference on Artificial Intelligence (IJCAI-15).

[164] Dawei Zhou, Jingrui He, Yu Cao, and Jae-sun Seo. 2016. Bi-level rare temporal pattern detection. In IEEE International

Conference on Data Mining Series (ICDM2016).

[165] Dawei Zhou, Jingrui He, Hasan Davulcu, and Ross Maciejewski. 2018. Motif-preserving dynamic local graph cut. In
IEEE International Conference on Big Data (Big Data 2018) (Seattle, Washington, December 10–13, 2018), Naoki Abe,
Huan Liu, Calton Pu, Xiaohua Hu, Nesreen K. Ahmed, Mu Qiao, Yang Song, Donald Kossmann, Bing Liu, Kisung Lee,
Jiliang Tang, Jingrui He, and Jeffrey S. Saltz (Eds.). IEEE, 1156–1161. https://doi.org/10.1109/BigData.2018.8622263

[166] Dawei Zhou, Jingrui He, Hongxia Yang, and Wei Fan. 2018. SPARC: Self-paced network representation for few-shot
rare category characterization. In 24th ACM SIGKDD International Conference on Knowledge Discovery & Data Mining.
ACM, 2807–2816.

[167] Dawei Zhou, Arun Karthikeyan, Kangyang Wang, Nan Cao, and Jingrui He. 2017. Discovering rare categories from

graph streams. Data Mining and Knowledge Discovery 31, 2 (2017), 400–423.

[168] Dawei Zhou, Kangyang Wang, Nan Cao, and Jingrui He. 2015. Rare category detection on time-evolving graphs. In

IEEE International Conference on Data Mining (ICDM2015). IEEE.

[169] Dengyong Zhou, Jason Weston, Arthur Gretton, Olivier Bousquet, and Bernhard Schölkopf. 2004. Ranking on data

manifolds. In Advances in Neural Information Processing Systems. 169–176.

[170] Dawei Zhou, Si Zhang, Mehmet Yigit Yildirim, Scott Alcorn, Hanghang Tong, Hasan Davulcu, and Jingrui He. 2017.
A local algorithm for structure-preserving graph cut. In 23rd ACM SIGKDD International Conference on Knowledge
Discovery and Data Mining. ACM, 655–664.

[171] Dawei Zhou, Lecheng Zheng, Jiawei Han, and Jingrui He. 2020. A data-driven graph generative model for temporal
interaction networks. In 26th ACM SIGKDD Conference on Knowledge Discovery and Data Mining (KDD ’20) (Virtual
Event, CA, August 23–27, 2020) Rajesh Gupta, Yan Liu, Jiliang Tang, and B. Aditya Prakash (Eds.). ACM, 401–411.
https://doi.org/10.1145/3394486.3403082

[172] Zhi-Hua Zhou. 2018. A brief introduction to weakly supervised learning. National Science Review 5, 1 (2018), 44–53.
[173] Arthur Zimek, Erich Schubert, and Hans-Peter Kriegel. 2012. A survey on unsupervised outlier detection in high-
dimensional numerical data. Statistical Analysis and Data Mining: The ASA Data Science Journal 5, 5 (2012), 363–387.

Received 15 March 2022; revised 23 May 2023; accepted 18 September 2023

ACM Computing Surveys, Vol. 56, No. 5, Article 123. Publication date: November 2023.

<!-- MARKITDOWN CONVERSION -->

<!-- Full MarkItDown conversion for formatting fidelity. -->

Rare Category Analysis for Complex Data: A Review
DAWEIZHOU,VirginiaTech
JINGRUIHE,UniversityofIllinoisatUrbana-Champaign
Thoughthesheervolumeofdatathatiscollectedisimmense,itistherarecategoriesthatareoftenthemost
importantinmanyhigh-impactdomains,rangingfromfinancialfrauddetectioninonlinetransactionnet-
workstoemergingtrenddetectioninsocialnetworks,fromspamimagedetectiononsocialmediaplatforms
torarediseasediagnosisinmedicaldecisionsupportsystems.Theuniquechallengesofrarecategoryanalysis
include(1)thehighlyskewedclassdistribution;(2)thenon-separablenatureoftherarecategoriesfromthe
majorityclasses;(3)dataandtaskheterogeneity;and(4)thetime-evolvingpropertyoftheinputdatasources.
Thissurveyreviewsstate-of-the-arttechniquesusedincomplexrarecategoryanalysis,wherethemajority
classeshaveasmoothdistributionwhiletheminorityclassesexhibitthecompactnesspropertyinthefeature
spaceorsubspace.Rarecategoryanalysisaimstoidentify,characterize,represent,andinterpretanomalies
thatnotonlyshowstatisticalsignificancebutalsoexhibitinterestingpatterns(e.g.,compactness,high-order
structures,showinginaburst).Weintroduceourstudy,definetheproblemsetting,anddescribetheunique
challengesofcomplexrarecategoryanalysis.Wethenpresentacomprehensivereviewofrecentadvances
thataredesignedforthisproblemsetting,fromrarecategoryexplorationwithoutanylabelinformationto
rarecategoryexpositionthatcharacterizesrareexampleswithacompactrepresentation,fromtherepresen-
tationofrarepatternsinasalientembeddingspacetotheinterpretationthepredictionresultsandproviding
relevantcluesfortheend-users’interpretation.Finallywediscusspotentialchallengesandshedlightonthe
futuredirectionsforcomplexrarecategoryanalysis.1
CCSConcepts:•Informationsystems→Datamining;
AdditionalKeyWordsandPhrases:Rarecategoryanalysis,imbalanceddatadistribution,anomalydetection
ACMReferenceformat:
DaweiZhouandJingruiHe.2023.RareCategoryAnalysisforComplexData:AReview.ACMComput.Surv.
56,5,Article123(November2023),35pages.
https://doi.org/10.1145/3626520
1Thisworkwasprimarilycompletedduringthefirstauthor’sPhDstudiesattheUniversityofIllinoisatUrbana-Champaign.
ThisworkissupportedbyNationalScienceFoundationunderAwardsNo.IIS-1947203,IIS-2002540,IIS-2137468,andIIS-
2117902.Theviewsandconclusionsarethoseoftheauthorsandshouldnotbeinterpretedasrepresentingtheofficial
policiesofthefundingagenciesorthegovernment.
Authors’ addresses: D. Zhou, Computer Science, Virginia Tech, 620 Drillfield Dr., Blacksburg, VA, 24060; e-mail:
zhoud@vt.edu;J.He,InformationScience,UniversityofIllinoisatUrbana-Champaign,501E.DanielSt,Champaign,IL,
61820-6211;e-mail:jingrui@illinois.edu.
Permissiontomakedigitalorhardcopiesofallorpartofthisworkforpersonalorclassroomuseisgrantedwithoutfee
providedthatcopiesarenotmadeordistributedforprofitorcommercialadvantageandthatcopiesbearthisnoticeand
thefullcitationonthefirstpage.Copyrightsforcomponentsofthisworkownedbyothersthantheauthor(s)mustbe
honored.Abstractingwithcreditispermitted.Tocopyotherwise,orrepublish,topostonserversortoredistributetolists,
requirespriorspecificpermissionand/orafee.Requestpermissionsfrompermissions@acm.org.
©2023Copyrightheldbytheowner/author(s).PublicationrightslicensedtoACM.
0360-0300/2023/11-ART123$15.00
https://doi.org/10.1145/3626520
ACMComputingSurveys,Vol.56,No.5,Article123.Publicationdate:November2023.
123

123:2 D.ZhouandJ.He
1 INTRODUCTION
The so-called era of big data is defined in part by the sheer volume of multimodel data that are
beingcollectedfromvariousplatforms(e.g.,graphs,images,text).Yet,itistherareoccurrences—
those data points that are significantly different from other observations in the data—that often
areofgreatestimportanceinmanyhigh-impactdomains:fromfinancialfrauddetectioninonline
transactionnetworkstoemergingtrenddetectioninsocialnetworks,fromspamimagedetection
onsocialmediaplatformstorarediseasediagnosisinmedicaldecisionsupportsystems.Anomaly
detection refers to the process by which these rare occurrences are identified. Many techniques
havebeenproposedtocharacterizeanomaliesindomainssuchasfinancialfrauddetection[102],
insiderthreatprediction[66],noveltydetection[92],genediseasediscovery[17],emergingtrend
tracking[28],networkintrusiondetection[58],astronomy[133],spamimagedetection[93],and
rarediseasediagnosis[117].
1.1 Anomaliesvs.RareCategoryExamples
Thebranchofdataminingconcernedwithidentifyinganomaliesoroutliers2hasalengthyhistory.
In1980,DouglasM.Hawkinsproposedthedefinitionofoutliers[47]thatisshowninDefinition1.1.
Sincethistime,theproblemofanomalydetectionoroutlierdetectionhasbeengeneralizedand
studied in various contexts, such as those of high-dimensional numerical data [173], sequential
data [27], time-series data [45], graph data [7], and financial data [36, 113]. This wide-ranging
explorationhasyieldedmanydomain-specifictermsforoutliers,includingnoveltiesevents,sur-
prisingchanges,fraudsoutbreak.
Definition1.1. Hawkins’sDefinitionofOutliers[47]
Anoutlierisanobservationthatdifferssomuchfromotherobservationsastoarousesus-
picionthatitwasgeneratedbyadifferentmechanism.
Thoughresearchershavehadtremendoussuccessapplyinganomalydetectionmethodsinvar-
iousdomains,notallanomaliesdetectedarenecessarilyusefulorrelevanttotheactualeventsof
interest.Infact,mostanomaliesareuninterestingdatapointsthateitheraredrawnfromaknown
distributionofnoiseorcorrespondtocombinationsoffeaturesthatareirrelevanttodownstream
applications[109].Forinstance,inFigure1,wepresentasetofskyimagescapturedbyground-
based telescopes as part of the Sloan Digital Sky Survey (program).3 According to the Sloan
Digital Sky Survey 99.9% of its captured sky images (e.g., the top row of Figure 1) can be well
explained based on known phenomena of the universe (e.g., discovered stars, comets, nebulae);
only 0.1% of the images (e.g., the bottom row of Figure 1) are anomalies. Moreover, among the
anomalies,99%oftheimages(e.g.,bottomleftimageinFigure1)areofnointeresttoastronomers
andarecausedbydiffractionspikesofsatellitetrailsorartifactsofthetelescope.Only1%ofthe
instances(aminuscule0.001%oftheSloanDigitalSkySurveydatabase)areusefulandmaylead
tonewscientificdiscoveries(e.g.,thebottomrightimageinFigure1).Here,werefertoanomalies
that are not only statistically significant but also interesting as rare category examples and the
problem of studying rare category examples as rare category analysis. Figure 2 illustrates the
relationshipamonganomalies,uninterestinganomalies,andusefulanomalies(i.e.,rarecategory
examples),whererarecategoryexamplesareasubsetofanomaliesthatarenotonlystatistically
significantbutalsocompactinthefeaturespace.
Weprovidethefollowinggeneraldefinitionofrarecategoryanalysis:Givenadataset D ofn
(cid:2) →−
examplesthatcomefromCdistinctclasses,withoutlossofgenerality,weassumethat n x = 0
i=1 i
2Inthisarticle,weuse“anomalies”and“outliers”interchangeably.
3http://www.sdss.org/iotw/archive.html
ACMComputingSurveys,Vol.56,No.5,Article123.Publicationdate:November2023.

RareCategoryAnalysisforComplexData:AReview 123:3
Fig.1. AnomaliesinSloandata[109].Toprow:knownobjects.Bottomrow:anomalies,99%ofwhichare
uninteresting patterns, such as diffraction spikes (bottom left) and only 1% of which are interesting pat-
terns that are worthy of future research and may lead to the discovery of extraordinary objects (bottom
right).
Fig.2. Relationshipbetweenanomalies/outliersandrarecategoryexamples.
(cid:2)
and 1 n (xj)2 =1,wherexj denotesthejthfeatureofx .Forthesakeofsimplicity,weassume
n i=1 i i i
theclasslabelfor theith node,y = 0, correspondsto themajority class(i.e.,normalexamples)
i
andy ∈ {1,...,C −1} corresponds to the rare categories (i.e., suspicious examples). Note that
i
rarecategoryanalysisistheproblemofstudyingpatternsintheminorityclasses.4 Inparticular,
forcasesinwhichmorethanonemajorityclassisobserved,wetreatallthemajorityclassesasa
singleclassoncetheunderlyingdistributionofeachmajorityclassissufficientlysmooth[49].In
generalrarecategoryanalysis,wemakethefollowingassumptionsregardingthesupportregion
ofthemajorityclassandminorityclasses:
Assumption 1. Smoothness Assumption for Majority Class. Given a highly imbalanced
dataset,thedistributionofthesupportregionofeachmajorityclassissufficientlysmooth.
Assumption2. CompactnessAssumptionforMinorityClass.Givenahighlyskeweddataset,
theminorityclassexamplescanberepresentedasacompactclusterinthefeaturespace.
Theseassumptionsaremadetoensurethattherarecategoriesareidentifiableandmeaningful.
To better capture this, let us look first at the example in Figure 3(a), where the majority class
(shown in blue) has a Gaussian distribution with large variance on the left, while the minority
4Inthisarticle,weuse“rarecategory”and“minorityclass”interchangeably.
ACMComputingSurveys,Vol.56,No.5,Article123.Publicationdate:November2023.

123:4 D.ZhouandJ.He
Fig.3. Thesupportregionsofamajorityclassandaminorityclassinaone-dimensionalsyntheticdataset.
class (shown in orange) corresponds to a peak with small variance on the right. If the minority
classisnotcompactandviolatesAssumption2(e.g.,theminorityclassinFigure3(b)isuniformly
distributedinthefeaturespace),thennoalgorithmcanperformbetterthanrandomsampling.If
thedistributionofthemajorityclassisnotsmoothandviolatesAssumption1(e.g.,themajority
classinFigure3(c)consistsofmultiplenarrowandsharppeaksjustliketheminorityclass),then
theminorityclasscannotbeidentifiedwithaclearclue.Basedontheassumptionsrelatedtorare
categoryexamples,weproposethefollowingdefinitionofcomplexrarecategoryanalysis:
Definition1.2. ComplexRareCategoryAnalysis
Complex rare category analysis refers to the problem of detecting, characterizing, repre-
senting,andinterpretingrareexamplesfromunderrepresentedminorityclassesinahighly
imbalanceddataset.
1.2 ChallengesofRareCategoryAnalysis
Wefirstdiscussthekeychallengesassociatedwithrarecategoryanalysis.Unliketheconventional
anomalies,rarecategoryexampleshavethefollowinguniquecharacteristics:
• C1.Rarity.Itisoftenthecasethatthepatternsofinterestaresporadicinthecollecteddata.
Forexample,infinancialfrauddetection,thevastmajorityoffinancialtransactionsarele-
gitimate;onlyasmallnumbermayberelatedtomoneylaundering,andtheyoftenexhibit
similartraits.Anotherexampleisnetworkintrusiondetection.Newmaliciousnetworkac-
tivitiesarehiddenamonghugevolumesofroutinenetworktraffic,andnetworkintrusions
ofthesametypeareoftensimilartooneanother.
• C2.LabelScarcity.Giventhehighskewnessandnon-separablenatureofrarecategories,
labelingrarecategoryexamplesisextremelyexpensive.Invariousrealapplications,suchas
moneylaunderingdetection,syntheticidentity(ID)detection,andnetworkintrusiondetec-
tion,weareusuallyrequiredtolearnfromahandfuloflabeledexamples.
• C3.Non-separability.Rarecategoriesareoftennon-separablefromthemajorityclassesin
thefeaturespace.Forexample,fromthealarmofgridhacking(e.g.,NotPetya)totheswift
growthincyber-criminals(e.g.,coin-miningattacks),thepastseveralyearshaveservedas
astarkreminderofanemergingtypeofterroristattack(i.e.,adversarialattacks).Suchmali-
ciousattacksaredesignedtobypasscurrentdetectionsystemsbycamouflagingthemselves
asnormalinstances,i.e.,thesupportregionsofnormalinstances,andmaliciousattacksare
non-separableinthegivenfeaturespace.
• C4.DataHeterogeneity.Toidentifytherarecategories,weoftenneedtocollectrawdata
fromdifferentsources,atdifferenttimestampsusingdifferenttechniques.Eachdatasource
mighthavedifferenttypesofusersandattributes.Ofsuchhighlyheterogeneousrawdata,
ACMComputingSurveys,Vol.56,No.5,Article123.Publicationdate:November2023.

RareCategoryAnalysisforComplexData:AReview 123:5
Fig.4. Overviewofcomplexrarecategoryanalysis.
onlyasubset(e.g.,datasources,attributes)mayberelevanttotheidentificationoftherare
categoryexamples(e.g.,securitythreats).
• C5. Dynamics. The raw input data continuously change over time; thus, extracting and
modeling useful information from such dynamic systems plays an important role in rare
categoryanalysis.
1.3 AnOverviewofComplexRareCategoryAnalysis
Complex rare category analysis can be divided into four tasks: detecting, characterizing, repre-
senting,andinterpretingrarecategoryexamples.Figure4presentsanoverviewofrarecategory
analysis,fromtheexplorationstepwithoutanygroundtruthtotheexpositionstepthataimsto
characterize rare examples with a compact representation, from representing rare patterns in a
salientspacetoprovidinginsightfulinterpretationoverthepredictionresults.
• T1:RareCategoryExploration. Inthistask,westartfromde-novoanddonothaveany
label information for the data. The goal is to identify at least one example from each rare
categorywithminimalhelpfromlabelingoracles.Webeginwithacomprehensivereview
ofsomerelevanttopics,includinganomalydetection[7,26],outlierdetection[57],andpre-
dictivemodelingonimbalanceddomains[20];thenweelaborateonpopularapproachesto
rarecategoryexplorationinbothstaticanddynamicenvironments.
• T2: Rare Category Exploitation. In this task, we use one/a few labeled examples from
eachclassthatmayhavebeenobtainedfromtheexploratorystepdiscussedinT1.Thepri-
marygoalistocaptureacompactrepresentationoftherarecategoriesinvariousdatafor-
mats by learning from a few-shot annotated data points. Depending on the availability of
amultimodalrepresentationofexamples,rarecategorydetectioncanbecategorizedasho-
mogeneous rare category exploration or heterogeneous rare category exploration. In the
formersetting[52,109],alltheexamplesarehomogeneous,astheyarecollectedfromthe
samedatasourceorhaveidenticaltraits;inthelatterone[41,79,160,163],weaimtoidentify
rarecategoriesinthepresenceofdataheterogeneity.
• T3:UnderstandingRareCategories: Thistask,whichmayentailrepresentingrareexam-
plesinasalientembeddingspace,visualizingthedatadistribution,orinterpretingtheunder-
lyingpredictionprocessintheprevioussteps(T1andT2),servesasaninvestigationstepfor
ACMComputingSurveys,Vol.56,No.5,Article123.Publicationdate:November2023.

123:6 D.ZhouandJ.He
end-users. We systematically discuss recent advances in representation learning [60, 166],
interpretation[30,84,89],andvisualanalyticsystems[81,105]forrarecategoryanalysis.
1.4 PreviousWorkandOurContributionstotheLiterature
Extensiveliteraturesurveysonthetopicsofimbalancedclassification,anomaly/outlierdetection,
andfrauddetectionhavebeenpublishedinthepastdecade.Inthecontextofimbalancedclassifi-
cation,HeandGarcia[48]coverthedevelopmentofresearchonlearningfromimbalanceddata.
Inthecontextofanomaly/outlierdetection,HodgeandAustin[57]introducesaliteraturereview
ofcontemporarytechniquesforoutlierdetection,andChandolaetal.[26]presentsacomprehen-
siveoverviewoftheresearchonanomalydetection.Aseriesofsurveysandspecial-issuejournal
articlesthattargetmorespecificproblemsandapplicationsinthecontextofanomaly/outlierdetec-
tionhavealsobeenpublished.Inparticular,Zimeketal.[173]studiestheproblemofunsupervised
outlierdetectioninhigh-dimensionalnumericaldata,Chandolaetal.[27]considersanomaliesin
discretesequences,Guptaetal.[45]focusonoutlierdetectionfortemporaldata,Akogluetal.[7]
attends to graph-based anomaly detection algorithms, Chalapathy and Chawla [25] provide an
overviewofdeep-learning-basedanomalydetectiontechniques,and,EdgeandFalconeSampaio
[36]andPhuaetal.[113]surveymethodologiesoffrauddetection.
However,veryfewworkspresentacomprehensiveoverviewofcomplexrarecategoryanalysis.
He[49]isoneofthefirsttopresentanend-to-endinvestigationofrarecategories,buttheintro-
ducedmethodologiesarelargelyrestrictedtothetabulardatainthestaticsetting.Respondingto
the gap in the literature, here we provide a comprehensive and structured overview of complex
rarecategoryanalysisfromseveralperspectives:
• DataPerspective.Unliketheprevioussurveysonoutlierdetection,anomalydetection,and
rarecategoryanalysis,ourstudyreviewsstate-of-the-arttechniquesforhandlingrichdata
types,suchastext/blogs,electronichealthrecords,weblinkgraphs,andstreamingdata.
• TaskPerspective.Weprovideacomprehensiveoverviewofend-to-endcomplexrarecategory
analysis,fromrarecategoryexplorationwithoutanylabelinformation,torarecategoryex-
positioncharacterizingrareexampleswithcompactrepresentation,fromrepresentingrare
patterns in a salient embedding space to interpreting the prediction results and providing
relevantcluesforend-users’investigation.
1.5 SurveyRoadmap
We present our survey in five parts sections. In Section 2, we focus on the de novo step of rare
categoryanalysis,i.e.,rarecategoryexploration,whichaimstofindtheinitialexamplefromeach
minorityclassintheunsupervisedsetting.InSection3,wediscussthefollowingstep,rarecategory
exploitation, which relies on the output of rare category exploration (i.e., initially labeled exam-
ples)tocharacterizetherarecategories.InSection4,westresstheimportanceofinterpretationin
rarecategoryanalysisinvarioushighlyregulatedindustries,suchasfinanceandhealthcare.We
systematicallydiscusshowtounderstandrarecategoryanalysisfromthefollowingtwoaspects:
(1) data diagnosis (i.e., How are the data distributed? Which piece of information is most valuable
foragiventask?);and(2)modeldiagnosis(i.e.,Whydoesthemodelmakeacertainpredictionona
particularpieceofinformation?).Section5enumeratesthepopularbenchmarkdatasetsandrepre-
sentativebaselinemodels.InSection6,weconcludeourstudyandshareourthoughtsregarding
futureresearchdirections,suchashowtoensureperformanceinthepresenceofnoise,missing
data, and adversarial examples and how to generate task-specific rare category examples (e.g.,
moneylaunderingactivity)givenaspecificdomain(e.g.,transactionnetworks).Ageneraloutline
follows:
ACMComputingSurveys,Vol.56,No.5,Article123.Publicationdate:November2023.

RareCategoryAnalysisforComplexData:AReview 123:7
• Section2:RareCategoryExploration
– 2.1Rarecategoryexplorationforstaticdata
∗ 2.1.1Tabulardata
∗ 2.1.2Graph-structureddata
– 2.2Rarecategoryexplorationfordynamicdata
∗ 2.2.1Time-seriesdata
∗ 2.2.2Temporalgraphs
• Section3:RareCategoryExploitation
– 3.1Homogeneousrarecategoryexploitation
∗ 3.1.1Globalapproaches
∗ 3.1.2Localapproaches
– 3.2Heterogeneousrarecategoryexploitation
∗ 3.2.1Dataheterogeneity
∗ 3.2.2Taskheterogeneity
• Section4:UnderstandingRareCategories
– 4.1Rarecategoryrepresentation
– 4.2Rarecategoryinterpretation
• Section5:DatasetsandRepresentativeMethods
– 5.1Datasets
– 5.2Representativemethods
• Section6:ConclusionandFutureDirections
2 RARECATEGORYEXPLORATION
Consideredthedenovostepinrarecategoryanalysis,rarecategoryexploration,a.k.a.rarecate-
gorydetection,aimstoproposeinitialrarecategoryexamplestothelabelingoracleinthegiven
dataset.Givenanunlabeled,imbalanceddataset,themostnaturalmethodofrarecategoryexplo-
rationisrandomsampling.Inthismethodwerandomlydrawexampleswithoutreplacementto
be labeled by the oracle until at least one example from each minority class has been identified.
However,duetotherarityofrarecategories(e.g.,theproportionofararecategoryis0.01%),an
extensivenumber(i.e.,10,000)oflabelingrequestsisrequiredtospottherareexample.Itisthus
worthwhiletodevelopmoreeffectiveandefficientsamplingstrategiestoaddressthisrarecategory
explorationproblem.Inthissection,weformallydefinetheproblemofrarecategoryexploration.
Weprimarilyaimtoaddress(C1)rarity,(C4)dataheterogeneity,and(C5)dynamicsinrarecategory
analysis.
Problem1. RareCategoryExploration.
Given:(i)anunlabeleddatasetD,(ii)asmallbudgetBforqueryingdomainexperts.
Find:thesetofinitialexamplesQ fromeachrarecategory.
Inreal-worldapplicationsofrarecategoryexploration,researchershavecustomizedProblem1
fordifferentdataformats,includingtabulardata,time-seriesdata,andgraph-structureddata.In
the following three subsections, we review the existing literature on rare category exploration
fromadataperspective(e.g.,staticdatavs.dynamicdata,tabulardatavs.graph-structureddata).
2.1 RareCategoryExplorationforStaticPatterns
Thetechniquescurrentlyusedinthestaticsettinghavebeenprimarilydesignedinactive-learning-
based schemes. The general procedure of this paradigm is presented in Figure 5. The key idea
behindthesample-selection-basedmethodsistolearnadetectorthatcangraduallysearchforthe
potentialrareexamplesbylearningfromtheexampleslabeledbytheoracle.Weoftenassumethat
ACMComputingSurveys,Vol.56,No.5,Article123.Publicationdate:November2023.

123:8 D.ZhouandJ.He
Fig.5. Aconceptualframeworkforrarecategoryexploration[109].
the labels obtained from the oracles are under a fixed budget B. Thus, the goal is to maximally
improvethepredictionaccuracywiththeminimumnumberoflabelingrequeststotheoracle.As
showninFigure5,rarecategoryexplorationproceedsiteratively.Ineachiteration,theprogram
starts with the oracle annotating a few samples. Then the sample-selection-based methods are
updated based on the newly labeled examples and further predict a small number of potential
rarecategoryexamplesinthesensethatobtaininglabelsforthemfurtherimprovestheprediction
accuracy. The program terminates once all the target rare categories have been captured. Next,
weelaborateontheexistingrarecategoryexplorationalgorithmsdesignedfortabularandgraph-
structureddata.
2.1.1 TabularData. GivenanunlabeleddatasetwithnsamplesD = {x ,...,x },whereeach
1 n
samplex ,i =1,...,ncomeswithd-dimensionalfeaturesx = {x1,...,xd},ourgoalistoidentify
i i i i
atleastoneexamplefromeachclassy =1,...,mwiththeminimumnumberofqueries.Thework
of Peleg and Moore [109] is one of the first attempts at rare category exploration. The authors
developamixturemodeltofitthedataanddesignafamilyofhintselectionmethodstoselectthe
rareexampleswiththehelpofahumanexpert.Experimentalresultsusingdifferenthintselection
methodsshowtheefficacyoftheproposedrarecategorydetectionframework.HeandCarbonell
[52] study the rare category exploration problem when the minority classes are non-separable
fromthemajorityclasses.Specifically,theauthorsdevelopanearest-neighbor-basedrarecategory
detectionalgorithmnamedNNDM,whichgraduallyselectsexampleswiththemaximumchanges
inthelocaldensityonacertainscaleandasksforlabelingfromtheoracle.Thealgorithmworks
asfollows:Giventhepriorp ofeachrarecategoryC,thealgorithmfirstestimatesthenumberof
examplesK =n×pinC.Then,thealgorithmrepresentseachexamplex intermsofavectorthat
i
iscomposedofthedistancesfromitsK-nearestneighbors.Byobtainingtheminimumdistancer
amongallsamples,thealgorithmconstructsahyper-ballwithradiusr foreachexample(ascenter)
andcomputesthelocaldensityasthenumberofenclosedexampleswithinthehyper-ball:
Hyberball(x ,r) = {x|x∈ D,(cid:5)x−x (cid:5) ≤r} (1)
i i
LocalDensity(x ) = |Hyberball(x ,r)| (2)
i i
Tomeasurethedegreeoflocaldensitychangesaroundeachsample(i.e.,hyper-ball),theauthors
proposeusingthedifferenceinthelocaldensitybetweenx anditsneighbors:
i
DensityChange(x )
i
= ⎧⎪ ⎨ ⎪ max xk ∈Hyberball(xi,r) [LocalDensity(x i )−LocalDensity(x k )] x i islabeled (3)
⎩ −∞ Otherwise
Inparticular,thefunctionDensityChangeassignseachlabeledexample’sscoreswith−∞toavoid
duplicated labeling requests. Finally, the algorithm returns the examples with the largest local
ACMComputingSurveys,Vol.56,No.5,Article123.Publicationdate:November2023.

RareCategoryAnalysisforComplexData:AReview 123:9
densitychangestotheoracleforlabeling:
Query=argmax xi ∈D DensityChange(x i ) (4)
Theoretical analysis shows that the methods effectively select examples on both the boundary
andintheinterioroftherarecategories.Inparticular,whentherarecategoriesarecompact,the
majorityclassdistributionislocallysmooth,andthesamplespaceissufficientlylarge,NNDMis
guaranteedtoidentifyatleastoneexamplecomingfromeachminorityclasswithprobability1−δ
after (cid:8)2α(cid:9) iterations,whereδ ∈ (0,1),α,andr areallpositiveparameters.
r2 2
Despite the promising results of NNDM with theoretical guarantees, the algorithm’s perfor-
mancelargelyreliesonpriorinformation(e.g.,numberofclasses,proportionofminorityclasses).
To alleviate the restriction on prior knowledge, He and Carbonell [50] propose a prior-free rare
categorydetectionalgorithmnamedSEDER.Theintuitionofthisalgorithmliesintheobservation
thataregionwithanabruptlocaldensitychangehasahigherprobabilityofobservingtherare
classes.UnlikeHeandCarbonell[52]andHeetal.[53],SEDERpicksthepotentialrareexamples
withlargeneighborhooddensitychangesforlabelingbyperformingsemi-parametricdensityes-
timation.SEDERintroducesaprior-freeDensityChangefunction,whichisdefinedasthenormof
thegradientofthelocaldensityfunction:
(cid:6)(cid:3)(cid:4)
(cid:2)
(cid:5)d ( n DensityEstimation(x )(xl −blxl))2
DensityChange(x ) = k=1 i i k (5)
i
((σl)2bl)2
l=1
where xl denotes the lth feature of x , σl denotes the bandwidth of the lth feature,
i i
DensityEstimationisakerneldensityestimationfunctionwithGaussiankernel[37],andbl is
apositiveparameter.Inthepresenceofnoisydataandirrelevantfeatures,HeandCarbonell[51]
formulate the rare category exploration problem via a co-selection scheme, which recovers the
relevantfeaturesandrepresentativeexamplesfromtherarecategories.Toobtaintheoptimalsets
ofrelevantfeaturesandrareexamples,HeandCarbonellproposeaneffectivesearchingprocedure
(i.e.,PALM)basedonanaugmentedLagrangianfunctiontosolvetheoptimizationproblem.Inpar-
ticular,PALM isdesignedinanalternativefashionsothattherelevantfeaturesandtheminority
classexamplescanbefound.
Recently,aparadigmshifthasbeenobservedinthedataminingcommunity:fromhowtoac-
curatelydetectrarecategoriestohowtoensuretrustworthinessinrarecategoryexploration.For
instance,AhmadianandLindsten[4],Kauretal.[67],andLiuetal.[83]studyhowtoensurerobust-
nessindetectingrareevents,especiallyintheout-of-distributionsetting.Shekharetal.[120]point
outthatalgorithmicfairnessandrarecategoryexplorationaredualproblemswhenencountering
thedataimbalanceissue.Theauthorsproposeafairness-awaremethodthatjointlyoptimizespre-
dictionaccuracyandstatisticalparity.Dengetal.[32]studythehardnessbiasintheautoencoder-
basedrarecategorydetectionmethodsandproposeaplug-and-playerrorcalibrationmethodto
mitigatethehardnessbiasissue.
2.1.2 Graph-StructuredData. Inmanyfields,graphsofferaunifyingdatastructureformodel-
ing relational data. As a result, extensive research related to rare category exploration has been
conductedtospottherarecategoryentitiesingraph-structureddata.Formallyspeaking,givenan
unlabeledgraphD = G(V,E),whereV andE denotethesetsofnodesandedgesinG,respec-
tively,ourtargetistoidentifyinitialnodesandedgesfromeachoftherarecategories.Heetal.[53]
extendstheideaofHeandCarbonell[52]tograph-structureddatabyproposingagraph-basedrare
categorydetectionalgorithmnamedGRADE.Thealgorithmstartscomputingaglobalsimilarity
matrixSmotivatedbymanifoldranking[169],whichisusedtoobtainacompactrepresentation
ACMComputingSurveys,Vol.56,No.5,Article123.Publicationdate:November2023.

123:10 D.ZhouandJ.He
oftheexamplesfromtheminorityclasses:
S= (I−αD −1 2AD − 2 1 ) −1 (6)
whereIdenotestheidentifymatrix,Ddenotesthediagonalmatrix,andAdenotestheadjacency
matrix of G. A prior-guided k-nearest-neighbor matrix is then computed to capture the sharp
localdensitychangesneartheboundaryofminorityclassesandthusmakeiteasiertocapturethe
rarepatterns.InadditiontodevelopingGRADE,theauthorsdevelopavariationnamedGRADE-LI,
whichrequiresonlyanupperboundontheproportionofeachrarecategory.GRADE-LI canwork
with the data when a detailed class-membership distribution of the data is not available to the
users.
Exceptfortheplaingraphs,dataoftenexhibitnode-levelandedge-levelheterogeneityforvar-
ious critical tasks in security, finance, and medicine, among other fields. Each node or edge is
associated with a specific type in such data (referred to as a heterogeneous graph). To accommo-
dateheterogeneousgraphs,researchershavestudiedhowtodetectanomaliesandrareeventsin
the unsupervised setting. For example, Sun et al. [127] propose the notion of neighborhood for-
mationforabipartitegraph,whichcomputestherelevancescoresofallnodestoaquerynodev
anddefinetheneighborhoodofv asthesetofnodeswithhigherrelevancescores.Basedonthe
neighborhoodformation,theauthorsdevelopananomalydetectionalgorithmtospottheabnor-
mal nodes with low “normality” scores. Based on similar intuition, Tong and Lin [132] propose
a non-negative residual matrix factorization framework named NrMF, which aims to detect the
maliciousgroupofentitiesaswellasprovideinterpretationofpredictionresultsfordataanalysts.
NrMF isbuiltupontheconventionalmatrixfactorizationmechanism,
A=FG+R (7)
whereFandGarelow-rankfactorizedmatrices,andR istheresidualmatrixthatindicatesrare
examplesonthebipartitegraphs.TointerpretthepredictionsviaNrMF,TongandLinimposea
non-negativeconstraintontheresidualmatrixR,suchthatallentriesinRarelargerthan0.Intu-
itively,highervalueoftheentryinRindicatesahigherprobabilityofexistingrareandabnormal
examples.Tosolvetheoptimizationproblemofnon-negativeresidualmatrixfactorization,theau-
thorsdevelopafastoptimizationalgorithmtoincrementallycomputetheresidualmatrixviathe
rank-1approximation,whichrunsinlinearw.r.t.thesizeofthegraph.
Morerecently,extensiveattemptshavebeenmadetopredictrarecategoryeventsbydeveloping
customizedgraphneuralnetworks(GNNs)todepictthestructureofagraphandlearnrepre-
sentations of various graph signals (e.g., nodes, edges, subgraphs). GNNs-based approaches are
generallydesignedbasedonthemessage-passingscheme,whichisgivenasfollows:
h(l+1) =UPDATE(l)(h(l),AGGREGATE(l)(h(l),∀u ∈N(v))) (8)
v v u
=UPDATE(l)(h(l),m(l) ) (9)
v N(v)
where h(l+1) denotes the embedding of node v ∈ V at the (l + 1)th-layer, UPDATE(l) and
v
AGGREGATE(l) arebothdifferentiablefunctionsforthelth-layer,andm(l) istheaggregated“mes-
N(v)
sage” from nodev’sneighborhoodN(v). Deng et al. [34] proposea graph convolutional net-
work(GCN)-basedframeworkforpredictingemergingeventsthatrequirescapturingcontextual
information from the raw data. The proposed framework first extracts graph representations of
theevents;itthendocumentsandlearnstopredicttheoccurrenceoffutureeventsandtoidentify
theeventsofinterest(i.e.,rarecategories).Zhongetal.[162]studiestheproblemofrarecategory
detectioninvideos,whereeachvideoisdecomposedintonsnippets(i.e.,nodesintheconstructed
videograph),theedgesbetweeneachpairofsnippetsaredefinedbasedonfeaturesimilarity,and
ACMComputingSurveys,Vol.56,No.5,Article123.Publicationdate:November2023.

RareCategoryAnalysisforComplexData:AReview 123:11
Fig.6. Anillustrationofthebi-levelrarecategories(i.e.,raresequencesandraretimesegments)inatime-
seriesdatabase[164].
the rare events are represented as abnormal actions. To solve this problem, a GCN is built to si-
multaneously clean noisy signals in the constructed video graph and predict abnormal actions.
Goodge et al. [42] investigate the relationship between the local outlier methods [69] and the
message-passingframework,whichmotivatesthemtodevelopaGNN-basedmethodtoidentify
localrareexamples.
2.2 RareCategoryExplorationforDynamicPatterns
Theexistingliteratureondetectingrarepatternsintemporaldataisveryrich,withnouniversal
abstractcategorizationcapableofcapturingallthedevelopedtechniquesinthisdirection.Accord-
ingly,weherefocusonrarecategoryexplorationfortime-seriesdataandtemporalgraphs.
2.2.1 Time-SeriesData. Inthesettingoftime-seriesdata,therarecategoriescanbeobserved
atboththesequencelevelandthesegmentlevel,asshowninFigure6.Forexample,mostelectro-
cardiogram(ECG)signalsarenormal(i.e.,collectedfromhealthypeople);onlyasmallportionof
themisabnormal(i.e.,collectedfrompatientswithheartdisease).Moreover,withintheabnormal
ECGsignals,onlyafewsegmentsareabnormal(e.g.,heartarrhythmia);therestarenormal.Early
studiesofrarecategoryexplorationfortime-seriesdata[18,21,22,65,80,97,100,108,118,150]
arecloselyrelatedtotheoutlierdetectionanddisorderdetectionmethods.Theyrelylargelyon
distanced-basedmechanisms[97,101,116,119]thatdefinevarioussimilaritymeasurements[45]of
temporalsequencesandsegmentsandthenidentifyrarepatternsdeviatingfromthenormalones.
Forinstance,Caoetal.[22]proposeascalabledistance-baseddetectionalgorithmforhigh-volume
data streams. This algorithm has been found to be optimal in terms of CPU costs. Begum and
Keogh[18]studytheproblemofdiscoveringraretime-seriesmotifs(i.e.,repeatedsubsequences)
from unbounded streams. To address the rarity issue of the time-series motif in a never-ending
stream,BegumandKeoghdevelopa“stickycash”algorithmthatadoptsaBloomfiltertoremem-
bereveryincomingsubsequenceandefficientlydetectsraremotifsintheunboundedreal-valued
timeseries.Tofacilitatetheuseofdistance-basedmethods,Yehetal.[150]introduceafastcompu-
tationalalgorithmfortime-series/subsequenceall-pairs-similarity-searchthathasstrongimplica-
tionsforandpromisingresultsforthetaskoftime-seriesdiscorddiscovery.Finally,Goodgeetal.
[43]introducearobustrandom-cutdatastructuretoproduceasketchorsynopsisoftime-series
data.Usingthisstructure,theauthorsproposeascalableanomalydetectionalgorithmbygradually
updatingthetime-seriessketchinacontinuousdatastream.
ACMComputingSurveys,Vol.56,No.5,Article123.Publicationdate:November2023.

123:12 D.ZhouandJ.He
A key motivation of the aforementioned methods is that the distributions of rare categories
(minorities) deviate from the normal distribution (majorities). However, there are some obvious
limitationstothisideainpractice.Theidentifiedexamplesareoftennotthetargetsofresearchers’
interest,whicharedrawnfromnoiseorcombinationsofirrelevantfeatures.Zhouetal.[164]as-
sumethatthetargetsofourinterestarerareanddrawnfromacompactdistribution.Underthis
assumption,Zhouetal.proposeabi-levelgenerativemodelthataimstojointlycharacterizethe
raretemporalpatternatthetime-seriesandsubsequencelevels.Recentadvancesindeeplearning
architectureshave led to a surge in research interest related to developing deep models to char-
acterizeanddetectraretemporalpatternsinhigh-impactapplications.Tuoretal.[134]presenta
deepunsupervisedframeworkfordetectinginsiderthreatinonlinedatastreams.Thisframework
outputsarankedlistofanomalyscoresofindividualuserbehaviors;Lietal.[77]developagen-
erative adversarial network (GAN) for unsupervised multivariate anomaly detection. Unlike
conventional distance-based methods and supervised methods, the proposed framework detects
rare temporal patterns by using the GAN-trained generator and discriminator to compute the
discriminationandreconstructionanomalyscore(DR-Score);Shenetal.[121]proposeare-
currentnetworkensemblecalledtherecurrentautoencoder,whichisdesignedtocharacterizeand
capture the abnormal time-series segments at multiple resolutions; finally, Deng and Hooi [33]
andZhangetal.[159]proposemodelingthebetween-sensordependencerelationshiptoidentify
abnormaltimesegmentsinmultivariatetimeseries.
2.2.2 TemporalGraphs. Manyreal-worldsystems,includingsocialnetworks,communication
networks, and gene interaction networks, are intrinsically dynamic and can be represented as
temporal graphs. In the past few years, researchers have proposed several rare category explo-
ration models for temporal graphs [3, 13, 34, 59, 76, 89, 90, 115, 125, 140, 149, 153, 167, 168].
The existing work can be categorized as discrete temporal graphs [154] or continuous temporal
graphs [85, 103, 171] based on the method of data collection used in the particular application
domain.
The discrete temporal graphs are often referred to as a time-evolving graphsn wherein the
data D is presented as a sequence of snapshots G˜ = {G(1),G(2),...,G(T)}. Each snapshot
G(t) = (V(t),E(t)),t = 1,2,...,T is composed of a collection of nodes V(t) and edges E(t) at
timestamp t. To identify rare examples on G˜, the static methods are extended to the dynamic
setting.Forexample,Sunetal.[126]proposeaparameter-freemodelthatcanmonitorgrouped
outliersandtheirchangesinastreamofgraphs.Thealgorithmisdesignedbasedonminimum
descriptionlength(MDL),whichallowsuserstodiscoverthechangesincommunitiesaswell
asinpointsintime.Araujoetal.[14]developafastincrementaltensoranalysisapproachthatcan
discoverbothtransientandperiodic/repeatingcommunitiesindynamicgraphs.SricharanandDas
[125] define a commute-time distance that captures node relationship changes and allows tradi-
tionaldistance-basedmethodstobeusedwithdiscretetemporalgraphs.Leeetal.[76]proposea
discrete-timeexponential-familyrandomgraphmodeltoidentifyclustersintime-evolvinggraphs.
Manzooretal.[90]studytheproblemofanomalydetectioninstreamingheterogeneousgraphsby
proposingaclustering-basedanomalydetectionapproachthatcansimultaneouslyaddressthehet-
erogeneityandstreamingnatureoftheinputdata.Inparticular,Manzooretal.introduceanovel
embeddingmechanismthatcanencodetheheterogeneousstreaminggraphintoavectorrepresen-
tationthatisthenusedtoperformclusteringandidentifyanomalouspatterns.Appeletal.[13]
proposesafactorizationframeworkthatcanjointlymodelthedistributionofdynamicconnections
andattributesandtracktheevolutionofevolvingcommunities.Despitetheirsuccess,thedetec-
tionalgorithmsoftensufferfromhighcomputationalcosts,especiallywhenextensivesnapshots
are given or when the algorithms are applied in the online setting. To address this issue, Zhou
ACMComputingSurveys,Vol.56,No.5,Article123.Publicationdate:November2023.

RareCategoryAnalysisforComplexData:AReview 123:13
etal.[167,168]proposeanincrementalrarecategoryexplorationschemethataimstogradually
updatethestaticrarecategoryexplorationmodelsbasedonthelocalchangesonanewsnapshot
withoutlearningfromscratch.Inparticular,Zhouetal.proposeaclosed-formsolutiontoupdate
theglobalsimilaritymatrixS(definedinEquation(6))inthedynamicsetting:
S(t) =S(t−1) +α
S(t−1)uvTS(t−1)
(10)
I+vTS(t−1)u
where u and v are one-hot vectors indicating the source nodes and target nodes of the updated
edges,respectively;Idenotestheidentitymatrix;andS(t)andS(t−1)aretheglobalsimilaritymatri-
cesatthetimestampstand(t−1),respectively.Moreover,toefficientlyandeffectivelycomputethe
densitychanges,DensityChange(x ),atheoreticalcondition,isprovidedtodeterminewhetherthe
i
hyper-ballHyberball(x ,r)isrequiredtoupdatefromtheprevioustimestamp.YasamiandSafaei
i
[149]studytheproblemofanomalydetectionindynamicsocialnetworks,whereinbothnetwork
structureandnodeattributesareobservedovertime.Theproposedframeworkjointlymodelstwo
processes,i.e.,(1)thenormalmodelingcomponentand(2)theanomalydetectioncomponent,to
track the abnormal relationship between nodes’ features and link generation in dynamic social
networks.Agarwaletal.[3]introduceanovelcommunityscoringmetriccalledpermanenceand
proposesanincrementalalgorithmtotracktheevolutionofnetworkcommunitiesinthedynamic
setting. The theoretical analysis shows that the updating procedure of the proposed algorithms
leadstopermanencemaximizationinthedynamicnetworks.Furthermore,toguaranteemodeleffi-
ciencyandalgorithmicfairness,Fuetal.[39]introduceafairness-awareclique-preservingspectral
clusteringalgorithmthatgeneralizesthestaticcliqueclusteringmethodstothedynamicsetting
viafairness-awareedgefilteringandincrementaleigenpairupdating.
Continuoustemporalgraphsarealsocalledfine-grainedtemporalgraphsortemporalinteraction
graphs,wherethetemporalgraphispresentedasasequenceoftimestampededges.Itisintractable
to directly generalize the static rare category exploration approaches used in discrete temporal
graphstocontinuoustemporalgraphs.Forthisreason,Manzooretal.[90]proposetorepresent
continuoustemporalgraphswithavectorrepresentation,whichiseasytocomputeandpreserves
thecontextualinformationofthecontinuoustemporalgraphs.Withthelearnedcontinuoustem-
poral graph representation, Manzoor et al. develop a fast and memory-efficient detection algo-
rithmtoprocessanyincomingnodesandedgesandidentifyanomaliesinrealtime.Hollocouetal.
[59] subsequently studies the problem of identifying grouped anomalies in the edge streaming
setting. In particular, the data are presented as a sequence of streaming edges. The authors pro-
poseastreamingalgorithmwiththetheoreticaljustificationthatperformsgraphclusteringwith
onlythreeintegerspernodeanddoesnotkeepanyedgeinmemory.AmjadiandTulabandhula
[10] propose a block-structured time-series model for detecting communities on time-evolving
graphs. This approach can capture both the link persistence and community persistence over
time.
3 RARECATEGORYEXPLOITATION
Intheprevioussection,weintroducedthecurrentliteratureonrarecategoryexploration,aprob-
lemthataimstoidentifyatleastoneexamplefromeachminorityclass.Afollow-uptorarecat-
egoryexploration,rarecategoryexploitationaimstolearnfromtheidentifiedexamplesandcap-
turealltherareexamplesinagivendataset.InFigure7,wepresentanexampleofrarecategory
exploitation on a synthetic dataset with one majority class and four minority classes. The key
observations are as follows: (1) the distribution of the majority class is smooth and (2) the sup-
port regions of the four minority classes are compact. That is, instances in each minority class
are self-similar and form a compact representation. In the past decades, the question of how to
ACMComputingSurveys,Vol.56,No.5,Article123.Publicationdate:November2023.

123:14 D.ZhouandJ.He
Fig.7. Anexampleofrarecategoryexploitationwithonemajorityclassandfourminorityclasses[54].The
labeledminorityclassexamplesareshowningreen,thelabeledmajorityclassexamplesareshowninred,
andtheunlabeledexamplesareshowninblack.
explorethecompactnessofrarecategorieshasattractedconsiderableinterestfromthedatamining
and machine learning communities. In this section, we delve into the problem of rare category
exploitation under two scenarios: (1) homogeneous data and (2) heterogeneous data. Whereas
in the former setting, data are collected from the same source and represented in the same for-
mat in the latter setting, we aim to capture rare examples in the presence of data and task
heterogeneity.
3.1 HomogeneousRareCategoryExploitation
Formally,weletX andY denotethesamplespaceandlabelspace,respectively.Wearegivena
dataset D = {D ,D }, where D = {(x )}Nl consists of N obtained annotated samples, D =
l u l i i=1 l u
{(x )}Nu denotesN unlabeledexamples,andx ,x ∈ X,y ∈ Y.Itisoftenthecasethat,dueto
j j=1 u i j i
the (C1) rarity and label (C2) scarcity challenges, annotated data N are scarce. In rare category
l
exploitation, our goal is to produce a prediction function f(·) : X → Y by learning from D
l
and to accurately characterize unknown rare category examples in D . Given this, we present
u
thefollowingdefinitionofrarecategoryexploitationinthehomogeneoussetting.Inthisproblem
setting,wemainlystudy(C1)rarity,(C2)labelscarcity,(C3)non-separability,and(C5)dynamics
inRCA.
Problem2. HomogeneousRareCategoryExploitation.
Given:adatasetD = {D ,D }withscarcelabeledexamplesD = {(x )}Nl andextensiveunla-
l u l i i=1
beledexamplesD = {(x )}Nu.
u j j=1
Find:(i)apredictionfunction f(·) tocharacterizerarecategoryexamples,(ii)asetofunlabeled
examplesthatarelikelycomingfromtherarecategories.
We categorize the current approaches to homogeneous rare category exploitation as either
global or local. Thefirstcategoryaims to capturetheglobal datadistributionforcharacterizing
rarecategories,whereasthesecondcategoryfocusesonexploringrarecategorieswithinasingle
orafewlocalregions(e.g.,theneighborhoodoftheidentifiedrarecategoryexamples).
3.1.1 GlobalApproaches. Thiscategoryofapproachesexploitsboththelabeledandunlabeled
examples to learn the class-membership distribution. Essentially, these methods transform the
rarecategoryexploitationproblemintoaclassificationproblemwithhighlyskeweddatadistribu-
tion. However, unlike the well-studied imbalanced classification problem that aims to maximize
ACMComputingSurveys,Vol.56,No.5,Article123.Publicationdate:November2023.

RareCategoryAnalysisforComplexData:AReview 123:15
theoverallclassificationaccuracy(majorityclassesandminorityclasses),rarecategoryexploita-
tionemphasizeslearningandcharacterizingtheminorityclasses.Earlyrarecategoryexploitation
workaddressesthe(C1)rarityand(C3)non-separabilitychallenges.Onerepresentativeapproach
ishyper-ball-basedrarecategoryexploitation[54,55].Thekeyideabehindapproachesistofor-
mulate rare category exploitation as an optimization problem: minimizing the radius R of the
hyper-ball that well encloses the rare categories. The general objective function for the binary
case(i.e.,onemajorityclassandoneminorityclass)canbewrittenasfollows.
min R2 (11)
R,c
s.t.,(cid:5)x −c(cid:5)2 ≤R2,x ∈ Dmaj
i i l
(cid:5)x −c(cid:5)2 ≥R2,x ∈ Dmin
j j l
(cid:5)x −c(cid:5)2 ≥R2,x ∈ D
k j u
whereRdenotestheradiusofthehyper-ball,c
denotesthecenterofthehyper-ball,Dmaj
denotes
l
the set of labeled majority class examples, and Dmin denotes the set of labeled minority class
l
examples. Moreover, to ensure the compactness of the hyper-ball, the authors introduce three
constraintsontheoptimizationproblem:(1)thelabeledexamplesfromthemajorityclassesshould
beoutsideofthehyper-ball;(2)thelabeledexamplesfromtheminorityclassshouldbeinsideof
thehyper-ball;and(3)thehyper-ballshouldencloseasmanyunlabeledexamplesaspossible.To
tacklethenon-separabilitychallenges,RACH[54]providesarelaxedsolutionofEquation(11)by
introducingslackvariablestoallowthemiss-classifiedinstancesandthenconvertingtheproblem
intoaconvexoptimizationproblem.Therelaxedproblemcanbeeasilysolvedinitsdualformvia
theprojectedsubgradientmethod.FollowingHeetal.[54],Heetal.[55]introducesakernelized
rarecategoryexploitationalgorithmthat,generalizesRACHtomodelcomplexshapesofthetarget
rarecategories’supportregionsbyprojectingtothehigh-dimensionalfeaturespaceinducedby
kernels.Thekernelmethodprovidesmoreflexibilitywhencharacterizingcomplexrarecategories
inreal-worldapplications.
Severalmorerecentstudiesconsidertheproblemofrarecategoryexploitationinthepresence
of(C2)scarceandnoisylabels.Haqueetal.[46],studytheproblemofnovelclassclassificationon
datastreams.Insteadofrelyingonredundanthuman-annotatedlabelsorpriorknowledge,they
propose a semi-supervised framework to track the confidence changes of classifiers in order to
detectthenovelconceptdriftsandthusidentifythenovelclasses.Zhouetal.[166]proposeabi-
levellearningmechanism(showninFigure8)inwhich,ateachermodel(i.e.,curriculumlearning
scheme)graduallyaugmentsthetrainingsetwithpseudolabels,andthestudentmodel(i.e.,rare
categorycharacterization)returnsthepredictionresultstogetherwiththepredictionconfidence
totheteachermodel.Ingeneral,theteachermodelandthestudentmodelaretrainedinamutu-
ally beneficial way, enabling the model to achieve better prediction accuracy in both rarity and
label scarcity. Any real-world applications (e.g., video classification [162]), in addition featuring
labelscarcity,comewithcomplexdataandnoisylabels,whichrequiremachinelearningmodels
to be trained with only weak supervision [172]. Zhong et al. [162] propose a GCN to clean the
noisylabels.TheGCN-basedlabelnoisecleanerisdesignedtoprovidesupervisorysignalsfrom
high-confidencesnippetstolow-confidencesnippets,suchthattheclassifiercanbetrainedwith
“clean”supervision. Xietal.[144]studytheproblemofonlinetransactionfrauddetection.Tohan-
dlethenoisyandcomplexuserbehaviorinformation,theydevelopthedualimportance-aware
factorizationmachine(DIFM)thatcapturesfieldvaluevariationsandfieldinteractionssimulta-
neouslytosupportonlinetransactionfrauddetection.Linetal.[82]proposeamulti-resolutionrare
categoryexploitationapproachtoidentifyinstancesofonlinecreditpaymentfraudsatdifferent
ACMComputingSurveys,Vol.56,No.5,Article123.Publicationdate:November2023.

123:16 D.ZhouandJ.He
Fig.8. Aconceptualframeworkofbi-levellearningforrarecategoryexploitation[166]thatiscomposedof
astudentlearningmodelandateacherlearningmodel.Thedashedarrowsindicatethelearningprocessof
theteachermodelthataimstogeneratepseudolabels;thesolidarrowsindicatethelearningprocessofthe
studentmodelthatisdesignedtopredictrarecategoryexamples.
granularities.Wuetal.[143]studyrarecategoryexploitationundervariousdatacontamination,
by proposing an information-theoretic bound of performance degradation in terms of the data
contaminationratio.
3.1.2 Local Approaches. The local algorithms are also referred to as seeded or targeted algo-
rithms[56,112,151,170].Thiscategoryofapproachesessentiallytacklesrarecategoryexploita-
tionasalocalclusteringproblem.Thekeyideaistotreatthelabeledexamplesasseedsandreturna
compactclusterneartheseedexampleswithoutexploringthewholedataset.Azmandianetal.[16]
present a local kernel density ratio feature selection framework that seeks a salient feature sub-
space in which the normal data points form a high-density region and the rare examples form
a low-density region. In the learned subspace,therare examples stand out and are easily distin-
guishedbydetectionalgorithms.SpielmanandTeng[124],presentadesignofalocalclustering
algorithm for massive graphs. The local algorithm is able to find a compact local cluster near a
seedexampleandtherunningtimeisnear-linearwithrespecttothesizeofthereturnedcluster.
Andersenetal.[11],deriveamixingresultforPageRankandproposeafastapproximationmethod
to compute PageRank vectors. Using this method, the authors develop an improved local graph
partitioningalgorithmthatenablespolylogarithmictimecomplexitywithrespecttothenumber
of edges in the given graph. Pang et al. [107] propose a local and interactive rare event detec-
tionalgorithm,thatleveragesthefeedbackfromananomaly-biasedsimulationenvironmentand
continuouslyupdatesthelearnedabnormalitytonovelrarecategories.
Although the conventional local clustering algorithms are primarily designed for low-order
connectivity patterns (e.g., edge in Table 1), many applications exhibit high-order connectivity
patterns(e.g.,starinTable1).Forexample,theloop-shapedstructureplaysasignificantroleinde-
tectingcommunitiesinuser-itemnetworks[170];aclusterofstar-shapedstructuresoftenserves
a red flag indicating potential instances of synthetic ID fraud in the personal identifiable in-
formation (PII) networks [102]. To account for the crucial high-order connectivity patterns in
real-worldsystems,Zhouetal.[170]andYinetal.[152]offerinnovativestudiesoftheproblemof
localhigh-ordergraphclustering.Inparticular,theauthorsintroducethenotionofhigh-ordercon-
ductanceandthehigh-orderdiffusionkernelwiththehigh-orderMarkovchainastheunderlying
model, which allows end-users to model various types of high-order structures. Moreover, they
generalizethewell-knownlocalclusteringalgorithms[11,124]tothehigh-ordersettingandpro-
vide a theoretical analysis of the effectiveness and scalability of the proposed algorithms. Many
recent studies study the high-order connectivity patterns in more complicated scenarios, such
as modeling evolving high-order structures on fine-grained temporal networks [165], capturing
ACMComputingSurveys,Vol.56,No.5,Article123.Publicationdate:November2023.

RareCategoryAnalysisforComplexData:AReview 123:17
Table1. IllustrativeExamplesofHigh-OrderConnectivityPatternsandLocalClusteringAlgorithms
ConnectivityPatternN Illustration OrderofN ClusteringAlgorithms Applications
Vertex 1st-order N/A N/A
Edge 2nd-order 1st-order Rarecategorydetection[53]
3-nodeLine
3rd-order 2nd-order Socialcommunitydetection[71]
Triangle
k-nodeStar kth-order (k−1)th-order Syntheticidentitydetection[102]
higher-orderclustersinheterogeneousnetworks[23],andtrackinghigh-orderstructuresontime-
evolvinggraphs[38].
3.2 HeterogeneousRareCategoryExploitation
Intheeraofbigdata,manyapplicationdomainsexhibitmultipletypesofheterogeneity,including
dataheterogeneitythatoriginatesfrommultipleinformationsourcesandtaskheterogeneitythat
originatesfrommultipleapplicationdomains.Inthissubsection,weorganizetheexistingworkin
thecontextofdataheterogeneityandtaskheterogeneity.
3.2.1 Dataheterogeneity. Learningfromdataheterogeneityisoftenreferredtoasmulti-view
learning, as the data are collected from different sources, enabling multiple views. In the data
heterogeneitysetting,rarecategoryexploitationbecomesevenmorechallengingthaninthedata
homogeneitysettingduetotheexistenceofmultipleviews.Itiscrucialtoleveragemultipleviews
and identify the relevant features for distinguishing between the majority and minority classes.
With the aim of addressing (C1) rarity, (C2) label scarcity, and (C4) data heterogeneity in rare
categoryanalysis,weformallydefinetheproblemasfollows:
Problem3. Multi-ViewRareCategoryExploitation.
Given:(i)adatasetD collectedfromV views;(ii)asmallsetoflabeledexamplesD = {(x )}Nl .
l i i=1
Find:(i)apredictionfunction f(·) tocharacterizerarecategoryexamples,(ii)asetofunlabeled
examplesthatarelikelycomingfromtherarecategories.
ApivotalstepinaddressingProblem5istoleverageviewconsistencyandlearnaunifiedrep-
resentation to improve the performance of rare category exploitation. In the past decades, re-
searchers have proposed extensive multi-view learning frameworks [9, 40, 63, 64, 78, 79, 79, 91,
122,157,160]foranomalydetectionthatcouldpotentiallysolveProblem5.However,thesemeth-
odsaremostlyunsupervisedand/orbasedonsomeheuristicfunctions,whichmeansthemethods
mightnotwellcapturethecharacteristicsofrarecategories.MUVIR[163]isoneoftheprincipled
effortsthathasbeenproposedtoaddressProblem5.MUVIRprovidesagenericrarecategoryde-
tectionsolutionthatisabletointegratetheexistingsingle-viewrarecategoryexploitationmodels
inordertocomputetheoverallposteriorprobabilityofeachexample.Thekeyideaistoexploitthe
relationshipamongmultipleviewsandestimatetheoverallposteriorprobabilityofexamplescom-
ingfromrarecategoriesgivendatafrommultipleviews.Inparticular,givendatawithmulti-view
features, one can trainV distinct rare category exploitation models uponV views and compute
view-specific posterior probability P(y = rarecategory|xv) with respect to thevth view. The
authorsproposethefollowingtheoremtoeffectivelyintegrateview-specificposteriorprobability
P(y =rarecategory|xv)inamodel-agnosticway:
ACMComputingSurveys,Vol.56,No.5,Article123.Publicationdate:November2023.

| 123:18 |     |     |     |     |     | D.ZhouandJ.He |     |
| ------ | --- | --- | --- | --- | --- | ------------- | --- |
Theorem 3.1 ([163]). If the features from m(cid:6)ultiple views have weak dependence given the class
|          | [1],i.e.,P(x|y =rarecategory) | ≥α  | V P(xv|y | =rarecategory),α |     |         |     |
| -------- | ----------------------------- | --- | -------- | ---------------- | --- | ------- | --- |
| labely i |                               |     | v=1      |                  |     | >0,then |     |
(cid:6)
|     |                      | (cid:7)V |                       |     |                 | V P(xv)(cid:9) |      |
| --- | -------------------- | -------- | --------------------- | --- | --------------- | -------------- | ---- |
|     |                      | (cid:7)  |                       |     | (cid:9)×(cid:7) | v=1            |      |
|     | P(y =rarecategory|x) | ≥C       | P(y =rarecategory|xv) |     |                 |                | (12) |
P(x)
|        |                  | (cid:8) v=1 |     |     | (cid:10) (cid:8) | (cid:10) |     |
| ------ | ---------------- | ----------- | --- | --- | ---------------- | -------- | --- |
| whereC | = α isaconstant. |             |     |     |                  |          |     |
(p2)V−1
= rarecategory|x)
UsingTheorem3.1,theoverallposteriorprobabilityP(y canbeapproxi-
matedasfollows:
(cid:6)
|     |     | (cid:7)V |     |     | V   | d   |     |
| --- | --- | -------- | --- | --- | --- | --- | --- |
(cid:7) v=1 P(xv)(cid:9)
|     | P(y =rarecategory|x) | =   | P(y =rarecategory|xv) |     |              |          | (13) |
| --- | -------------------- | --- | --------------------- | --- | ------------ | -------- | ---- |
|     |                      |     |                       |     | (cid:8) P(x) | (cid:10) |      |
v=1
wherethemarginalprobabilitiesP(x)andP(xv)canbeestimatedviakerneldensity,anddisanon-
negativeparameterthatbalancestheimportanceofthetermrelatedtothemarginalprobabilities.
AmodifiedversionofMUVIRhasbeenproposedforhandlingproblemswhentheexactpriorsofmi-
norityclassesareunknown.Inthepastfewyears,researchershaveexploredmanyhigh-impactap-
plicationsofrarecategoryexploitationthatcanbeformulatedasmulti-viewrarecategoryexploita-
tionproblems.Amongthem,Leeetal.[75]proposeanattention-basedvisualquestion-answering
network to jointly model the input images and corpora and identify system errors or abnormal
events;Chenetal.[29]studytheproblemofmulti-modalvideoanomalydetection,proposinga
bi-directional predictive network to regularize the prediction task from pixel-wise, cross-modal,
and temporal-sequence levels; and Shen et al. [123] propose an anomaly segmentation network
forlocalizingdefectiveareasinlarge-scaleindustrialmanufacturingenvironments.
Another group of approaches to multi-view rare category exploitation consist of the semi-
supervised classification models. For example, Nie et al. [104] propose a multi-view framework
withadaptiveneighborhoodlearning.Theframeworkintegratesmulti-viewclusteringandsemi-
supervised classification, which allows learning attention for each view automatically. Zhang
etal.[156]developamulti-viewrarecategoryexploitationframeworkforAlzheimer’sdiseasedi-
agnosis.Theyproposeamulti-layermulti-viewframeworkthatautomaticallyconstructsashared
latentrepresentationacrossmultipleviewsandlearnsthemappingfunctionsfromthemulti-view
featurestothepredictionlabels.WangandLan[138]assumethemultipleviewsofthemajority
class examples are drawn from a unique distribution with different projection functions. Given
thisassumption,theauthorsproposeahierarchicalBayesianmodelthatcomputestheoutlierness
ofunlabeledsamplesandthusidentifiesrareexamples.
3.2.2 Task heterogeneity. This subsection provides an overview of the rare category exploita-
tionalgorithmsthathavebeenproposedinthecontextoftaskheterogeneity.Formallyspeaking,in
thepresenceofmultipletasks,wearegivenadatasetD={D1∪...∪DS}thatcomesfromSapplica-
tionsdomains,andasmallsetoflabeledexamplesfromeachtaskDs={(xs)}N s
|     |     |     |     |     |         | l ,whereNs | denotes |
| --- | --- | --- | --- | --- | ------- | ---------- | ------- |
|     |     |     |     |     | l i i=1 | l          |         |
thenumberoflabeledexamplesinDs.Ourgoalistocapturethemultimodalitiesfromdifferent
tasksanddomainsandlearnapredictionmodeltoaccuratelycharacterizetherarecategoriesfrom
different tasks and domains. The problem, which aims to address (C1) rarity, (C2) label scarcity,
(C3)non-separability,and(C5)dynamicsinrarecategoryanalysis,iscommonlydefinedasfollows:
| Problem4. | Multi-taskRareCategoryExploitation. |     |     |     |     |     |     |
| --------- | ----------------------------------- | --- | --- | --- | --- | --- | --- |
Given:(i)adatasetD = {D1∪...∪DS},whereDs isthedatasetforthesthtask,s = 1,...,S;
|                                              |     |     |     | {(xs)}N s |     |     |     |
| -------------------------------------------- | --- | --- | --- | --------- | --- | --- | --- |
| (ii)asmallsetoflabeledexamplesfromeachtaskDs |     |     |     | = l       | .   |     |     |
i i=1
|     |     | f(·) tocharacterizerarecategoryexamplesineachtaskDs,(ii)a | l   |     |     |     |     |
| --- | --- | --------------------------------------------------------- | --- | --- | --- | --- | --- |
Find:(i)apredictionfunction
setofunlabeledexamplesthatarelikelycomingfromtherarecategoriesineachtaskDs.
ACMComputingSurveys,Vol.56,No.5,Article123.Publicationdate:November2023.

RareCategoryAnalysisforComplexData:AReview 123:19
The past decades have produced much literature studying Problem 4. This literature can be
categorizedinoneoftwowaysbasedonitsobjectives.Thefirstcategoryaimstolearnamixture
ofpredictionfunctionsthatmaximizetheoverallaccuracyacrossalltasks.Forexample,Yangetal.
[146]studytheproblemofrarecategoryexploitationinthepresenceofmultipletasksandmultiple
viewsbyproposingajointoptimizationframeworkcalledM2LID.Theauthorsstartfromametric
calledborderdegreethatisusedtocapturethesharpchangesindensityneartheboundaryofrare
categoriesinthefeaturespace:
BorderDegree(x) =Hub(x)−Authority(x) (14)
where Hub(x) and Authority(x) indicate the hub value and authority value [70] of example x,
correspondingly.Intuitively,thelargertheborderdegreeis,thehighertheprobabilitythatxbe-
longstotherarecategory.Tomodeltaskrelatednessandviewconsistency,theythenformulate
the problem by requiring (1) task-specific learners to behave similarly on the features, (2) view-
based learners to behave similarly on the examples, and (3) the border-degree to be negatively
correlated with the prediction confidence score. Finally, to solve the optimization problem, they
develop a block-coordinate-descent-based method to iteratively update the boundary character-
istics of rare categories and multiple classification functions for different tasks. [62] propose a
multimodel learning algorithm that is based on a mixture of sparse Gaussian graphical models.
[161] aims to tackle the Problem 4 in the presence of data scarcity and adversarial attacks. The
authorsproposeafederatedlearningframeworkthatperformsmultipletaskssimultaneously.
The second category is also referred to as transferable rare category exploitation. Instead of
learning an optimal predictor for all tasks, transferable rare category exploitation heavily em-
phasizes the target tasks. Some typical works includes [8], [12], [72], [129], and [136]. In Appel
etal.[12],theauthorssystematicallyevaluatetheperformanceofanomalydetectionframeworks
using two types of transfer representation learning paradigms: (1) transfer learning from pre-
trained networks, and (2) transfer learning from auxiliary tasks. Kumagai et al. [72] develop an
autoencoderframeworkthatlearnsthedomain-specificlatentvectorsandthusimprovestheper-
formanceindetectingrareexamples.Unlikemosttransferlearningmodelsthataimtolearnthe
transferablerepresentationfor thetarget domain, the work of Vercruyssenet al. [136] proposes
to select a subset of labeled and relevant examples from the source domain to augment the tar-
gettasks. Theaforementionedmethodsallassumethetargetdomainsarerelatedtothesource
domains.However,thereisamorechallengingscenario:theso-calledout-of-distributionrarecat-
egory exploitation, wherein the test data are unseen or from shifted distributions. To handle the
out-of-distributionscenarios,MortezaandLi[98]proposeananalyticalframeworkwithprovable
guarantees to characterize and understand out-of-distribution detection in open-world applica-
tions.SunandWang[128]proposeanadaptivein-out-awarelearningframeworktojointlymodel
themixedin-distributionandout-of-distributiondatasamples.Acharyaetal.[2]proposeagraph
contextreasoningnetworkforout-of-distributionobjectdetectionbyconstructingarepresenta-
tiongraphandacontextgraphfromtheinputimage.
4 UNDERSTANDINGRARECATEGORIES
Although they have been tremendously successful in exploring and exploiting rare category ex-
amples,manyadvancedmethods,especiallydeeplearningmodels,oftenremainblack-boxinna-
ture. This poses a challenge to their application in industries that have to follow highly regu-
lated processes. In these industries, prediction models must be interpretable and the output re-
sultsarerequiredtomeetcompliancestandards.Therefore,anaturalresearchquestionishowto
make existing models transparent to the end-user by identifying the right context (e.g., key fac-
tors,representativeentities,criticaltimestamps).Inthissection,wesystematicallydiscusshowto
ACMComputingSurveys,Vol.56,No.5,Article123.Publicationdate:November2023.

123:20 D.ZhouandJ.He
Fig.9. Rare-category-orientednetworkrepresentation:themajorityandminorityclassesarenotseparable
intheoriginalfeaturespace,butbecomewellseparatedintheembeddingspace[166].
understandrarecategorypatternsfromthefollowingtwodirections:(1)rarecategoryrepresen-
tationand(2)rarecategoryinterpretation.Thefirstdirectionaimstodiagnosefromthedataper-
spective(i.e.,How isthedata distributed?Whichpieceof informationismostvaluable fora given
task?),whiletheseconddirectionaimstodiagnosefromthemodelperspective(i.e.,Whydoesthe
modelmakeacertainpredictiononaparticularpieceofinformation?).
4.1 RareCategoryRepresentation
In this task, we aim to learn a rare-category-oriented embedding representation such that the
rare examples (e.g., security threats) are well separated from the majority classes (e.g., normal
activities).Figure 9 presentsa typicalexample of rarecategoryrepresentationlearning wherein
themajorityclassandtheminorityclassareoverlappedtogetherintheoriginalfeaturesspacebut
becomeseparatedinthelearnedembeddingspace.Formallyspeaking,theproblemcanbedefined
asfollows:
Problem5. RareCategoryRepresentation.
Given:(i)adatasetDthatconsistsofnsamples;(ii)asmallsetoflabeledexamplesD = {(x )}Nl ;
l i i=1
(iii)theuser-definedembeddingdimensiond.
Find:(i)ararecategoryrepresentationmodelд(·);(ii)ad-dimensionalembeddingrepresentation
E∈Rn×d
thatwellpreservestheunderlyingdistributionofrarecategories.
Inthepastdecade,extensiveworkhasbeendonetodeveloprepresentationlearningmethodsto
learntheunderlyingdistributionoftherarecategorypatterns.Thekeyideabehindthesemethods
istotrackthe“footprints”ofrarecategoriesviaexternalinformation(e.g.,supervisionfromora-
cles)orpriorknowledge(e.g.,featuresindicatinglocaldensitychanges[52,147])andthenleverage
thisinformationtoregularizetherepresentationlearningmodelstoextractlow-dimensionaland
salient embedding for rare category analysis. For instance, Akoglu and Falioutsos [5] propose a
set of egonet features (e.g., weighted and unweighted in- and out-degree, number of neighbors,
numberoftriangles)fromeachsnapshotofthegraphsequencetomodelthe“behavior”ofeach
node.Thesefeaturesareeffectiveinspottingrarecategoryexamples.Manzooretal.[90]aimto
spotanomalouspatternsinastreamofheterogeneousgraphscontainingdifferenttypesofnodes
andedgesbyproposingaclustering-basedanomalydetectionapproachthatcansimultaneously
addresstheheterogeneityandstreamingnatureoftheinputdata.Inparticular,Manzooretal.in-
troduceanovelembeddingmechanismthatcanencodetheheterogeneousstreaminggraphinto
avectorrepresentationthatisthenusedtoperformclusteringandidentifyanomalouspatterns.
Huangetal.[60]studytheproblemofimageclassificationwhendatainthevisiondomainexhibit
ACMComputingSurveys,Vol.56,No.5,Article123.Publicationdate:November2023.

RareCategoryAnalysisforComplexData:AReview 123:21
Fig.10. Preliminaryresultscomparingnetworkembeddingusingvariousalgorithms[166].
a highly skewed class distribution by learning a deep representation such that rare categories
are easily separable from the majority class by contemporary classification methods. In particu-
lar, this article first proposes to learn the data representation by maintaining both inter-cluster
andinter-classmarginsthatreducetheclassimbalanceinherentinthelocaldataneighborhood.
TheproposedframeworkisbuiltbasedonaConvolutionalneuralnetwork(CNN)framework
throughaquintupletsamplingschemeandtheassociatedtriple-headerhingeloss.
Morerecently,duetothenotablesuccessofnetwork-embeddingapproaches,variousnetwork-
embedding-based approaches have been proposed for rare category analysis. For example,
SPARC [166] is one of the first rare-category-oriented network embedding frameworks. SPARC
aimstolearnasalientrepresentationtocharacterizerarecategoryexamples.Inspiredbythefamily
ofcurriculumlearningthatsimulatesthecognitivemechanismsofhumanbeings,SPARC gradu-
allyselectsthekeynetworkcontextualinformationandlearnstherare-category-orientednetwork
representationbyshiftingfromthe“easy”concepttothe“difficult”concept.Theresultsshowthat
(1)SPARC enablesuserstovisualizethenetworklayoutinasalientembeddingspace,wherethe
majority classes and minority classes are well separated; and (2) SPARC is able to identify valu-
ablecontextualinformationthatprovidesinterpretationandguidanceinthetaskofrarecategory
characterization. Here we compare SPARC with three state-of-the-art network embedding algo-
rithms,includingtwounsupervisedmethods,i.e.,DeepWalk[111]andLINE[130],andonesemi-
supervisedmethod,i.e.,PLANETOID[148].Wefirstmapthegivennetworktoa129-dimensional
spacewithdifferentembeddingmethods.Then,weemploythenonlineardimensionalityreduction
method,i.e.,t-SNE[88],toencodeexamplesinatwo-dimensionalspaceforbettervisualization,
asshowninFigure10.Weobservethattherareexamplesarebetterclusteredusingtheproposed
methodthananyofthebaselinemethods.
FollowingSPARC,Wuetal.[142]proposeabiasedrandomwalkmodelnamedVDRW forlearn-
ing imbalanced network representation.VDRW is designed to dynamically adjust the transition
ACMComputingSurveys,Vol.56,No.5,Article123.Publicationdate:November2023.

123:22 D.ZhouandJ.He
Fig.11. UserinterfaceofRCLens,whichiscomposedofthreekeymodules:thedataexplorermodule(shown
insubfigurea),thefeatureexplorermodule(showninsubfigureb),andthecategoryexplorermodule(shown
insubfigurec).
probabilitymatrixeachtimeanodeisvisitedbytherandomparticle.ViaVDRW,Wuetal.propose
apairofsamplingstrategies,i.e.,contextsamplingandbalanced-bathsampling,tolearnnetwork
representationusingskip-grammodel[94].NetWalk[155]isdevelopedforrareeventdetectionby
learningthenetworkrepresentations,whichcanbeupdateddynamicallyasthenetworkevolves.
NetWalkfirstextractsthedynamicnetworkcontextandencodestheverticesofthedynamicnet-
worktoalow-dimensionalrepresentation.Then,aclustering-basedschemeisemployedtoincre-
mentallyanddynamicallytrackthemaliciouspatternsinthedynamicnetworks.Dengetal.[34]
proposeaGCN-basedframeworkforpredictingfutureeventsbycapturingcontextualinformation
fromtherawdata.Theproposedframeworkfirstextractsgraphrepresentationsoftheeventsdoc-
umentsand,thenlearnstopredicttheoccurrenceoffutureeventsandidentifyeventsofinterest
(e.g.,anomalypatterns).
4.2 RareCategoryInterpretation
Interpretabilityinmachinelearningmodelsplaysacrucialroleinmanyhigh-impactdomainsand
rare category analysis. In this task, we aim to characterize the rare categories with a predictive
modelandinterprettheoutputfromthismodelbyprovidingrelevantclues,suchasconnectivity
patterns, data sources, features, and timestamps from time-series data. We define the problem
settingasfollows:
Problem6. RareCategoryInterpretation.
Given:(i)adatasetD thatconsistsofnsamples,(ii)ararecategoryanalysismodel f(·).
Find:interpretationovertheoutputfrom f(·)onD.
Despitetherichliteratureinthecontextof explainableartificialintelligence(XAI)[15,31,
44,61,95,96,131],interpretingrarecategoryanalysismodelsremainschallengingforthefollow-
ing reasons: (1) rare category analysis models are naturally “biased” (i.e., focusing on minority
ACMComputingSurveys,Vol.56,No.5,Article123.Publicationdate:November2023.

RareCategoryAnalysisforComplexData:AReview 123:23
Fig. 12. User interface of RCAnalyzer, which is composed of (a) the timeline view; (b) the matrices view;
(c) the instance view; (d) the sub-network view; (e) the label result view; (f) the parameter panel; (g) the
encodingpanel;and(h)theinformationpanel.
patterns instead of the overall data distribution), (2) rare category analysis model f(·) is
often trained with scarcity labels, and (3) the learning process of rare category analysis
model f(·) may frequently involve oracles and operate in a human-in-the-loop fashion (see
Figure 5 for rare category exploration). Simply replacing f(·) with a conventional interpretable
machine learning models may deteriorate the prediction performance by providing misleading
characterizationsorinjectingadditionalbias[74].
There have been a few attempts in the visualization domain to address Problem 6 given the
aforementionedchallenges.Forexample,RCLens[81]isaninteractivevisualanalyticsystemthatis
designedtoexploreandidentifyrarecategoryexampleswiththeguidanceofend-users.Figure11
presentstheuserinterfaceofRCLens,whichactivelyvisualizesandinterpretsthethreelearning
phases of rare category analysis models to end-users. In the data exploration phase (shown in
subfigurea),thesystemconductsapersonalizedvisualizationofthedataviaadataqueryingand
filtering mechanism; in the feature selection phase (shown in subfigure a), the system provides
relevantcluesandstatistics(e.g.,correlationsoffeatures)forend-userstoinvestigatethefeature
dimensions;andintherarecategoryanalysismodel(showninsubfigurec),thesystemvisualizes
theidentifiedrarecategoriestoend-usersandthenrefinesthepredictionsbyleveragingtheusers’
feedback.
Pan et al. [105] proposes a visual analytic system named RCAnalyzer for studying rare cate-
gorypatternsindynamicsystems.TheuserinterfaceofRCAnalyzer isshowninFigure12,which
includes (a) the timeline view showing an overview of the given dynamic networks; (b) the ma-
tricesviewshowingtheneighborhoodcontextualinformationofeachnode;(c)theexampleview
showingthefeaturedistributionofrarepatterns;and(d)thelabelresultviewshowingthehistory
ACMComputingSurveys,Vol.56,No.5,Article123.Publicationdate:November2023.

123:24 D.ZhouandJ.He
Table2. PubliclyAccessibleReal-WorldDatasetsforRareCategoryAnalysis
| DataType    | Dataset         | DescriptionofRareCategories |
| ----------- | --------------- | --------------------------- |
| TabularData | 20NewsGroup[68] | Raretopicsofnewspapers      |
TabularData Donors[106] OutstandingprojectsproposedbyK-12teachers
TabularData Census[35] High-incomepeopleinU.S.censusbureaudatabase
| TabularData | Fraud[114]    | Fraudulentcreditcardtransaction |
| ----------- | ------------- | ------------------------------- |
| TabularData | UNSW-NB15[99] | Networkintrusion                |
| TabularData | URL[86]       | MaliciousURLs                   |
TabularData Campaigndata[35] Rarelysuccessfulcampaigningrecords
| TabularData     | Thyroid[35] | Raredisease                 |
| --------------- | ----------- | --------------------------- |
| Time-seriesData | Vandal[73]  | Wikipediavandalwarning      |
| Time-seriesData | Spam[139]   | Webspams                    |
| Time-seriesData | HDFS[145]   | Systemerrors                |
| GraphData       | Tox21[87]   | Toxicenvironmentalchemicals |
| GraphData       | ENZYMES[19] | Abnormalproteins            |
| GraphData       | NCI1[137]   | Abnormalchemicalcompounds   |
predictionresultsaswell as themodel diagnosis. To ensuretheinterpretabilityof rarecategory
analysismodels,thesystemisabletoactivelyvisualizeeachidentifiedrareexampleincontext(e.g.,
neighborhoodstructuresintheadjacenttimestamps)tohelporaclesunderstandandexaminethe
predictionresults.
5 DATASETSANDREPRESENTATIVEMETHODS
Thissectionsummarizesthepopularevaluationdatasetsandrepresentativealgorithmsacrossdif-
ferentdatatypesanddownstreamtasks.
5.1 Datasets
Although rare categories are prevalent across various domains (e.g., finance), collecting and an-
notatingrareexamplesisextremelytime-consumingandlabor-intensive(e.g.,annotatingmoney
launderingactivities).Earlystudies(e.g.,[48,50,52,53,109])evaluatetheirmodelsonsynthetic
or semi-synthetic datasets that are either generated from a pre-defined data distribution or ma-
nipulatedfrompublicbenchmarkdatasets.However,evaluationsperformedonsyntheticorsemi-
syntheticdatasetsmaynotreflecttheperformanceofrarecategoryanalysismodelsinreal-world
applications.Topromotethefurtherdevelopmentofrarecategoryanalysis,Table2summarizes
some public benchmark datasets, whose data range from tabular data to graph-structured data,
fromstaticdatatodynamicdata.
5.2 RepresentativeMethods
Comparison evaluation with representative algorithms serves a pivotal role in the development
ofmachinelearningalgorithms.InTable3,weenumerateandsummarize25representativerare
category analysis algorithms w.r.t. data type (i.e., tabular data, time-series data, graph data) and
downstreamtask(i.e.,exploration,exploitation,representation,andvisualization).Sincethemeth-
ods in Table 3 have been developed for diverse tasks and datasets, we are unable to provide
a meta-analysis of their performance in a unified setting. Instead, to provide insight and an
in-depth understanding of the methods, we summarize our major observations as follows: (i)
most methods are designed in an unsupervised or semi-supervised setting, (ii) sampling-based
methods [135, 163] and anomaly-detection-based methods [132, 158] are still the mainstream
ACMComputingSurveys,Vol.56,No.5,Article123.Publicationdate:November2023.

RareCategoryAnalysisforComplexData:AReview 123:25
Table3. RepresentativeAlgorithmsinDataPerspective
| DataType        | Algorithm          | Task                      |
| --------------- | ------------------ | ------------------------- |
| TabularData     | NNDB[52]           | RareCategoryExploration   |
| TabularData     | ACT [141]          | RareCategoryExploration   |
| TabularData     | SEDER[50]          | RareCategoryExploration   |
| TabularData     | HMS[135]           | RareCategoryExploration   |
| TabularData     | MUVIR[163]         | RareCategoryExploitation  |
| TabularData     | RACH [54]          | RareCategoryExploitation  |
| TabularData     | MLAN [104]         | RareCategoryExploitation  |
| TabularData     | RCLens[81]         | RareCategoryVisualization |
| Time-seriesData | SUITS[80]          | RareCategoryExploration   |
| Time-seriesData | CDLC [18]          | RareCategoryExploration   |
| Time-seriesData | MatrixProfile[150] | RareCategoryExploration   |
Time-seriesData BIRAD[164] RareCategoryExploration&Exploitation
| Time-seriesData | RRCF [43]     | RareCategoryExploration      |
| --------------- | ------------- | ---------------------------- |
| Time-seriesData | Sand [46]     | RareCategoryExploitation     |
| GraphData       | Oddball[6]    | RareCategoryExploration      |
| GraphData       | NrMF [132]    | RareCategoryExploration      |
| GraphData       | HiDDen[158]   | RareCategoryExploration      |
| GraphData       | FocusCO[110]  | RareCategoryExploration      |
| GraphData       | BIRD[168]     | RareCategoryExploration      |
| GraphData       | StreamSpot    | [90] RareCategoryExploration |
| GraphData       | AnomRank[153] | RareCategoryExploration      |
GraphData SPARC [166] RareCategoryExploitation&Representation
| GraphData | HOSPLOC    | [170] RareCategoryExploitation  |
| --------- | ---------- | ------------------------------- |
| GraphData | L-MEGA[38] | RareCategoryExploitation        |
| GraphData | RCAnalyzer | [105] RareCategoryVisualization |
solutionsinrarecategoryexploration,and(iii)rarecategoryvisualizationandinterpretationare
underexplored.
6 CONCLUSIONANDFUTUREDIRECTIONS
Departingfromtheprevioussurveys,thisarticlepresentedacomprehensivepipelineofrecentad-
vancesinrarecategoryanalysis.Westartedfromthede-novostepwithoutanylabelinformation
and surveyed rare category exploration techniques in the setting of homogeneous data and het-
erogeneousdata.Then,wereviewedrarecategoryexploitationmethodsthataimtocharacterize
acompactrepresentationoftheminorityclassesinordertodiscoveralltherareexampleswith
highaccuracy.Finally,wediscussedtheproblemofrarecategoryexplanation,andinparticular,
how to learn a salient representation of rare categories and interpret the prediction results. De-
spitethesignificantdevelopmentsinrarecategoryanalysis,thereremainsomeexcitingresearch
opportunities
•
RareCategoryGeneration.Tomeetthedramaticallyincreasingdemandformachinelearning
systemsasserviceproviders(e.g.,socialnetworking,onlineadvertising,datasecurity),amas-
siveamountofdatahasbeengeneratedandcollectedfromavarietyofdomains.However,
thecollectedraredataareoftennoisy,sparse,few-shotannotated,andevolvingovertime.
Directly training machine learning models from the raw data would introduce inevitable
ACMComputingSurveys,Vol.56,No.5,Article123.Publicationdate:November2023.

123:26 D.ZhouandJ.He
model bias and largely degrade the model performance in downstream applications (e.g.,
rare category characterization, rare category explanation). Moreover, the ever-increasing
sizeofdata,togetherwiththedifficultyofreleasingandsharingthem,hasmadedatagener-
ationafundamentalproblemthatiskeyformanyhigh-impactapplications,includingfraud
detection,recommendation,anddatasecurity,amongothers.Hence,itiscriticaltodevelop
deepgenerativemodelsthatenablescalablemodelingofrealdatatoextractkeycontextual
information,distillknowledge,andgenerateplausiblepatternsfordataaugmentationinrare
categoryanalysis.
• Long-TailCategoryAnalysis.Inthepastdecade,deeplearninghasachievedremarkablesuc-
cessinvariouslearningtasks(e.g.,imageclassification,speechrecognition,linkprediction)
throughthetrainingof“bigmodels”on“bigdata.”However,unlikethesewell-studiedtasks
(e.g.,imageclassificationoverdomesticcatsandwildcats)withrichtrainingdata,thevast
majority of real-world entities and patterns (e.g., identification of honest employees and
maliciousinsidersinalargeinstitution)areunderexploredandlacktheobservationaland
annotated data that often correspond to the “long-tail” categories. Unlike existing works
onrarecategoryanalysisthatfocusononeorafewrarecategories,herewefaceamassive
numberofunderrepresentedcategoriesfroma“long-tail”distribution.Moreover,thecurrent
machine learning systems are mostly tailored to specific learning scenarios, prevent them
fromdeliveringontheirpromisesindetectingthetargetsofinterestinthepresenceofdistri-
butionchanges(e.g.,dynamicsystems).Twofundamentalresearchquestionsthusemerge:
(Q1)Howcanwecomprehendsuchmassive“long-tail”categoriesgiventheinherentpaucityof
observationalandannotateddata? (Q2)Howcanwecapturethetargetsofinterest(e.g.,rare
categoryexamples)givenanoveldatadistribution?
• Robust Rare Category Analysis. Robust rare category analysis is another fundamental yet
quiteopenresearchproblemthatisattractingasurgeofattentionfrommanyhigh-impact
domains(e.g.,spamdetection,financialfraud,systemdiagnosis).Forexample,infinancial
frauddetection:Howcanwemeasureentitysensitivity,algorithmicrobustness,taskhardness,
andmodelgeneralization,givenapredictionmodel? Howcanweachieveoperationalrobust-
ness and adversarial robustness in the presence of the external disturbances (e.g., noise, miss-
ingvalues,outliers,adversarialattacks)? Despitetheextensiveworkonadversarialmachine
learning,thevastmajorityofthepreviousstudiesassumeabalanceddatadistributionwhile
neglectingrealisticcasesinwhichthedataarehighlyskewed,andthetargetsofinterestare
underrepresented.Comparedtoconventionalmachinelearningtools,rarecategoryanalysis
modelsaremoresensitiveandvulnerableinthepresenceofadversarialattacksduetothe
rarity,non-separability,andlabelscarcityofrarecategoryexamples.
• Human–AICollaborativeRareCategoryAnalysis.Manyindustriesfollowhighlyregulated
processesthatrequirerarecategoryanalysismodelstobeinterpretableandhumanexperts
tobeinvolvedinthepredictionloop.Thehuman-in-the-loopfashion[24,52]enablesrare
categoryanalysismodelstoleveragehumanintelligencetoalleviatethelabelscarcityissue
andimprovethepredictionperformanceinhigh-stakeapplications,suchasfailurepredic-
tion in safety-critical systems and rare disease diagnosis in health care. However, as hu-
man intelligence is naturally a black box to AI models, a fundamental research question
remains nascent: How can we gain a deeper understanding of the underlying mechanism of
humanintelligence,thusenablingunimpededknowledgetransferbetweenhumanintelligence
andAI? Apromisingbutchallengingresearchdirectionliesinhowtobuildanintegrated
andinteractivesystemforaccurateandtrustworthyhuman–AIcollaborativerarecategory
analysis.
ACMComputingSurveys,Vol.56,No.5,Article123.Publicationdate:November2023.

RareCategoryAnalysisforComplexData:AReview 123:27
REFERENCES
[1] StevenP.Abney.2002.Bootstrapping.In40thAnnualMeetingoftheAssociationforComputationalLinguistics(ACL),
pages360–367.
[2] ManojAcharya,AnirbanRoy,KaushikKoneripalli,SusmitJha,ChristopherKanan,andAjayDivakaran.2022.De-
tecting out-of-context objects using graph contextual reasoning network. In 31st International Joint Conference
on Artificial Intelligence (IJCAI 2022) (Vienna, Austria, 23–29 July 2022), Luc De Raedt (Ed.). ijcai.org, 629–635.
https://doi.org/10.24963/ijcai.2022/89
[3] PrernaAgarwal,RichaVerma,AyushAgarwal,andTanmoyChakraborty.2018.DyPerm:Maximizingpermanence
fordynamiccommunitydetection.InPacific-AsiaConferenceonKnowledgeDiscoveryandDataMining.Springer,
437–449.
[4] AmirhosseinAhmadianandFredrikLindsten.2021.Likelihood-freeout-of-distributiondetectionwithinvertiblegen-
erativemodels.In30thInternationalJointConferenceonArtificialIntelligence(IJCAI2021),(VirtualEvent/Montreal,
Canada,19–27August2021),Zhi-HuaZhou(Ed.).ijcai.org,2119–2125.https://doi.org/10.24963/ijcai.2021/292
[5] LemanAkogluandChristosFaloutsos.2010.Eventdetectionintimeseriesofmobilecommunicationgraphs.In
ArmyScienceConference,Vol.1.
[6] LemanAkoglu,MaryMcGlohon,andChristosFaloutsos.2010.Oddball:Spottinganomaliesinweightedgraphs.In
Pacific-AsiaConferenceonKnowledgeDiscoveryandDataMining.Springer,410–421.
[7] LemanAkoglu,HanghangTong,andDanaiKoutra.2015.Graphbasedanomalydetectionanddescription:Asurvey.
DataMiningandKnowledgeDiscovery29,3(2015),626–688.
[8] SamirAl-StouhiandChandanK.Reddy.2016.Transferlearningforclassimbalanceproblemswithinadequatedata.
Knowl.Inf.Syst.48,1(2016),201–228.https://doi.org/10.1007/s10115-015-0870-3
[9] AlejandroMarcosAlvarez,MakotoYamada,AkisatoKimura,andTomoharuIwata.2013.Clustering-basedanomaly
detectioninmulti-viewdata.In22ndACMInternationalConferenceonInformationandKnowledgeManagement
(CIKM’13)(SanFrancisco,CA,October27–November1,2013),QiHe,ArunIyengar,WolfgangNejdl,JianPei,and
RajeevRastogi(Eds.).ACM,1545–1548.https://doi.org/10.1145/2505515.2507840
[10] MehrnazAmjadiandThejaTulabandhula.2018.Block-structurebasedtime-seriesmodelsforgraphsequences.arXiv
preprintarXiv:1804.08796(2018).
[11] ReidAndersen,FanR.K.Chung,andKevinJ.Lang.2006.Localgraphpartitioningusingpagerankvectors.In47th
AnnualIEEESymposiumonFoundationsofComputerScience(FOCS2006)(21–24October2006,Berkeley,California).
IEEEComputerSociety,475–486.https://doi.org/10.1109/FOCS.2006.44
[12] JeroneAndrews,ThomasTanay,EdwardJ.Morton,andLewisD.Griffin.2016.Transferrepresentation-learningfor
anomalydetection.JournalofMachineLearningResearch.
[13] AnaPaulaAppel,RenatoL.F.Cunha,CharuC.Aggarwal,andMarcelaMegumiTerakado.2018.Temporallyevolving
communitydetectionandpredictionincontent-centricnetworks.InJointEuropeanConferenceonMachineLearning
andKnowledgeDiscoveryinDatabases.Springer,3–18.
[14] MiguelAraujo,SpirosPapadimitriou,StephanGünnemann,ChristosFaloutsos,PrithwishBasu,AnanthramSwami,
EvangelosEPapalexakis,andDanaiKoutra.2014.Com2:Fastautomaticdiscoveryoftemporal(‘comet’)communities.
InPacific-AsiaConferenceonKnowledgeDiscoveryandDataMining.Springer,271–283.
[15] AlejandroBarredoArrieta,NataliaDíaz-Rodríguez,JavierDelSer,AdrienBennetot,SihamTabik,AlbertoBarbado,
SalvadorGarcía,SergioGil-López,DanielMolina,RichardBenjamins,RajaChatila,andFranciscoHerrera.2020.
Explainableartificialintelligence(XAI):Concepts,taxonomies,opportunitiesandchallengestowardresponsibleAI.
InformationFusion58(2020),82–115.
[16] FatemehAzmandian,AyseYilmazer,JenniferG.Dy,JavedA.Aslam,andDavidR.Kaeli.2012.GPU-accelerated
featureselectionforoutlier detectionusingthelocalkerneldensityratio.In12thIEEEInternationalConference
on Data Mining (ICDM2012) (Brussels, Belgium, December10–13, 2012), Mohammed Javeed Zaki, Arno Siebes,
Jeffrey Xu Yu, Bart Goethals, Geoffrey I. Webb, and Xindong Wu (Eds.). IEEE Computer Society, 51–60. https:
//doi.org/10.1109/ICDM.2012.51
[17] MichaelJ.Bamshad,SarahB.Ng,AbigailW.Bigham,HollyK.Tabor,MaryJ.Emond,DeborahA.Nickerson,and
JayShendure.2011.ExomesequencingasatoolforMendeliandiseasegenediscovery.NatureReviewsGenetics12,
11(2011),745.
[18] NurjahanBegumandEamonnKeogh.2014.Raretimeseriesmotifdiscoveryfromunboundedstreams.Proceedings
oftheVLDBEndowment8,2(2014),149–160.
[19] KarstenM.Borgwardt,ChengSoonOng,StefanSchönauer,S.V.N.Vishwanathan,AlexanderJ.Smola,andHans-
PeterKriegel.2005.Proteinfunctionpredictionviagraphkernels.In13thInternationalConferenceonIntelligentSys-
temsforMolecularBiology2005(Detroit,MI,25–29June2005).47–56.https://doi.org/10.1093/bioinformatics/bti1007
[20] PaulaBranco,LuísTorgo,andRitaP.Ribeiro.2016.Asurveyofpredictivemodelingonimbalanceddomains.ACM
ComputingSurveys(CSUR)49,2(2016),31.
ACMComputingSurveys,Vol.56,No.5,Article123.Publicationdate:November2023.

123:28 D.ZhouandJ.He
[21] SuratnaBudalakoti,AshokN.Srivastava,RamAkella,andEugeneTurkov.2006.Anomalydetectioninlargesetsof
high-dimensionalsymbolsequences.TechnicalReportNASATM-2006-214553,NASAAmesResearchCenter,2006.
[22] LeiCao,DiYang,QingyangWang,YanweiYu,JiayuanWang,andElkeA.Rundensteiner.2014.Scalabledistance-
basedoutlierdetectionoverhigh-volumedatastreams.In2014IEEE30thInternationalConferenceonDataEngineering.
IEEE,76–87.
[23] AldoG.Carranza,RyanA.Rossi,AnupRao,andEunyeeKoh.2020.Higher-orderclusteringincomplexheteroge-
neousnetworks.InThe26thACMSIGKDDConferenceonKnowledgeDiscoveryandDataMining(KDD’20)(Virtual
Event,CA,August23–27,2020),RajeshGupta,YanLiu,JiliangTang,andB.AdityaPrakash(Eds.).ACM,25–35.
https://doi.org/10.1145/3394486.3403045
[24] ChengliangChai,LeiCao,GuoliangLi,JianLi,YuyuLuo,andSamuelMadden.2020.Human-in-the-loopoutlier
detection.In2020InternationalConferenceonManagementofData(SIGMODConference2020),(OnlineConference
[Portland,OR],June14–19,2020),DavidMaier,RachelPottinger,AnHaiDoan,Wang-ChiewTan,AbdussalamAlaw-
ini,andHungQ.Ngo(Eds.).ACM,19–33.https://doi.org/10.1145/3318464.3389772
[25] RaghavendraChalapathyandSanjayChawla.2019.Deeplearningforanomalydetection:Asurvey.arXivpreprint
arXiv:1901.03407(2019).
[26] VarunChandola,ArindamBanerjee,andVipinKumar.2009.Anomalydetection:Asurvey.ACMComputingSurveys
(CSUR)41,3(2009),15.
[27] VarunChandola,ArindamBanerjee,andVipinKumar.2010.Anomalydetectionfordiscretesequences:Asurvey.
IEEETransactionsonKnowledgeandDataEngineering24,5(2010),823–839.
[28] ChaomeiChen.2006.CiteSpaceII:Detectingandvisualizingemergingtrendsandtransientpatternsinscientific
literature.JournaloftheAmericanSocietyforInformationScienceandTechnology57,3(2006),359–377.
[29] ChengweiChen,YuanXie,ShaohuiLin,AngelaYao,GuannanJiang,WeiZhang,YanyunQu,RuizhiQiao,BoRen,and
LizhuangMa.2022.Comprehensiveregularizationinabi-directionalpredictivenetworkforvideoanomalydetection.
In36thAAAIConferenceonArtificialIntelligence(AAAI2022),34thConferenceonInnovativeApplicationsofArtificial
Intelligence(IAAI2022),12thSymposiumonEducationalAdvancesinArtificialIntelligence(EAAI2022)(VirtualEvent,
February22–March1,2022).AAAIPress,230–238.https://ojs.aaai.org/index.php/AAAI/article/view/19898
[30] XuanHongDang,BarboraMicenková,IraAssent,andRaymondT.Ng.2013.Localoutlierdetectionwithinterpre-
tation.InJointEuropeanConferenceonMachineLearningandKnowledgeDiscoveryinDatabases.Springer,304–320.
[31] ArunDasandPaulRad.2020.Opportunitiesandchallengesinexplainableartificialintelligence(XAI):Asurvey.
arXivpreprintarXiv:2006.11371(2020).
[32] AilinDeng,AdamGoodge,LangYiAng,andBryanHooi.2022.CADET:Calibratedanomalydetectionformitigating
hardnessbias.In31stInternationalJointConferenceonArtificialIntelligence(IJCAI2022),(Vienna,Austria,23–29July
2022),LucDeRaedt(Ed.).ijcai.org,2002–2008.https://doi.org/10.24963/ijcai.2022/278
[33] AilinDengandBryanHooi.2021.Graphneuralnetwork-basedanomalydetectioninmultivariatetimeseries.In
35thAAAIConferenceonArtificialIntelligence(AAAI2021),33rdConferenceonInnovativeApplicationsofArtificial
Intelligence(IAAI2021),11thSymposiumonEducationalAdvancesinArtificialIntelligence(EAAI2021),(VirtualEvent,
February2–9,2021).AAAIPress,4027–4035.https://ojs.aaai.org/index.php/AAAI/article/view/16523
[34] SonggaojunDeng,HuzefaRangwala,andYueNing.2019.Learningdynamiccontextgraphsforpredictingsocial
events.In25thACMSIGKDDInternationalConferenceonKnowledgeDiscovery&DataMining.ACM,1007–1016.
[35] DheeruDuaandCaseyGraff.2017.UCIMachineLearningRepository.http://archive.ics.uci.edu/ml
[36] MichaelEdwardEdgeandPedroR.FalconeSampaio.2009.Asurveyofsignaturebasedmethodsforfinancialfraud
detection.Computers&Security28,6(2009),381–394.
[37] BradleyEfronandRobertTibshirani.1996.Usingspeciallydesignedexponentialfamiliesfordensityestimation.The
AnnalsofStatistics24,6(1996),2431–2461.
[38] DongqiFu,DaweiZhou,andJingruiHe.2020.Localmotifclusteringontime-evolvinggraphs.In26thACMSIGKDD
ConferenceonKnowledgeDiscoveryandDataMining(KDD’20),(VirtualEvent,CA,August23–27,2020),RajeshGupta,
YanLiu,JiliangTang,andB.AdityaPrakash(Eds.).ACM,390–400.https://doi.org/10.1145/3394486.3403081
[39] DongqiFu,DaweiZhou,RossMaciejewski,ArieCroitoru,MarcusBoyd,andJingruiHe.2023.Fairness-awareclique-
preservingspectralclusteringoftemporalgraphs.InACMWebConference2023(WWW2023),(Austin,TX,30April
2023–4May2023).,YingDing,JieTang,JuanF.Sequeda,LoraAroyo,CarlosCastillo,andGeert-JanHouben(Eds.).
ACM,3755–3765.https://doi.org/10.1145/3543507.3583423
[40] JingGao,WeiFan,DeepakTuraga,SrinivasanParthasarathy,andJiaweiHan.2011.Aspectralframeworkfordetect-
inginconsistencyacrossmulti-sourceobjectrelationships.In2011IEEE11thInternationalConferenceonDataMining
(ICDM).IEEE,1050–1055.
[41] YuanGao,XiangWang,XiangnanHe,ZhenguangLiu,HuaminFeng,andYongdongZhang.2023.Addressinghet-
erophilyingraphanomalydetection:Aperspectiveofgraphspectrum.InACMWebConference2023,WWW2023,
Austin,TX,USA,30April2023–4May2023,YingDing,JieTang,JuanF.Sequeda,LoraAroyo,CarlosCastillo,and
Geert-JanHouben(Eds.).ACM,1528–1538.https://doi.org/10.1145/3543507.3583268
ACMComputingSurveys,Vol.56,No.5,Article123.Publicationdate:November2023.

RareCategoryAnalysisforComplexData:AReview 123:29
[42] Adam Goodge, Bryan Hooi, See-Kiong Ng, and Wee Siong Ng. 2022. LUNAR: Unifying local outlier detection
methods via graph neural networks. In 36th AAAI Conference on Artificial Intelligence (AAAI 2022), 34th Con-
ference on Innovative Applications of Artificial Intelligence (IAAI 2022), 12th Symposium on Educational Advances
in Artificial Intelligence (EAAI 2022) (Virtual Event, February 22–March 1, 2022). AAAI Press, 6737–6745. https:
//ojs.aaai.org/index.php/AAAI/article/view/20629
[43] SudiptoGuha,NinaMishra,GouravRoy,andOkkeSchrijvers.2016.Robustrandomcutforestbasedanomalydetec-
tiononstreams.InInternationalConferenceonMachineLearning.2712–2721.
[44] David Gunning, Mark Stefik, Jaesik Choi, Timothy Miller, Simone Stumpf, and Guang-Zhong Yang. 2019. XAI-
explainableartificialintelligence.ScienceRobotics4,37(2019),eaay7120.
[45] ManishGupta,JingGao,CharuC.Aggarwal,andJiaweiHan.2013.Outlierdetectionfortemporaldata:Asurvey.
IEEETransactionsonKnowledgeandDataEngineering26,9(2013),2250–2267.
[46] AhsanulHaque,LatifurKhan,andMichaelBaron.2016.SAND:Semi-supervisedadaptivenovelclassdetectionand
classificationoverdatastream.InAAAIConferenceonArtificialIntelligence.
[47] D.M.Hawkins.1980.IdentificationofOutliers.Springer.https://doi.org/10.1007/978-94-015-3994-4
[48] HaiboHeandEdwardoA.Garcia.2009.Learningfromimbalanceddata.IEEETransactionsonKnowledgeandData
Engineering21,9(2009),1263–1284.
[49] JingruiHe.2010.RareCategoryAnalysis.Ph.D.Dissertation.CarnegieMellonUniversity,Pittsburgh,PA.
[50] JingruiHeandJaimeCarbonell.2009.Prior-freerarecategorydetection.In2009SIAMInternationalConferenceon
DataMining.SIAM,155–163.
[51] JingruiHeandJaimeCarbonell.2010.Coselectionoffeaturesandinstancesforunsupervisedrarecategoryanalysis.
StatisticalAnalysisandDataMining:TheASADataScienceJournal3,6(2010),417–430.
[52] JingruiHeandJaimeG.Carbonell.2008.Nearest-neighbor-basedactivelearningforrarecategorydetection.In
AdvancesinNeuralInformationProcessingSystems.633–640.
[53] JingruiHe,YanLiu,andRichardLawrence.2008.Graph-basedrarecategorydetection.In8thIEEEInternational
ConferenceonDataMining,2008(ICDM’08).IEEE,833–838.
[54] JingruiHe,HanghangTong,andJaimeCarbonell.2010.Rarecategorycharacterization.In10thIEEEInternational
ConferenceonDataMining(ICDM).IEEE,226–235.
[55] JingruiHe,HanghangTong,andJaimeCarbonell.2012.Aneffectiveframeworkforcharacterizingrarecategories.
FrontiersofComputerScience6,2(2012),154–165.
[56] ZengyouHe,XiaofeiXu,andShengchunDeng.2003.Discoveringcluster-basedlocaloutliers.PatternRecognit.Lett.
24,9-10(2003),1641–1650.https://doi.org/10.1016/S0167-8655(03)00003-5
[57] VictoriaHodgeandJimAustin.2004.Asurveyofoutlierdetectionmethodologies.ArtificialIntelligenceReview22,
2(2004),85–126.
[58] StevenA.Hofmeyr,StephanieForrest,andAnilSomayaji.1998.Intrusiondetectionusingsequencesofsystemcalls.
JournalofComputerSecurity6,3(1998),151–180.
[59] AlexandreHollocou,JulienMaudet,ThomasBonald,andMarcLelarge.2017.Astreamingalgorithmforgraphclus-
tering.CoRRabs/1712.04337(2017).arXiv:1712.04337http://arxiv.org/abs/1712.04337
[60] ChenHuang,YiningLi,ChenChangeLoy,andXiaoouTang.2016.Learningdeeprepresentationforimbalanced
classification.InIEEEConferenceonComputerVisionandPatternRecognition.5375–5384.
[61] TsuyoshiIdé,AmitDhurandhar,JiríNavrátil,MoninderSingh,andNaokiAbe.2021.Anomalyattributionwith
likelihoodcompensation.In35thAAAIConferenceonArtificialIntelligence(AAAI2021),33rdConferenceonInnovative
ApplicationsofArtificialIntelligence(IAAI2021),11thSymposiumonEducationalAdvancesinArtificialIntelligence
(EAAI2021),(VirtualEvent,February2–9,2021).AAAIPress,4131–4138.https://ojs.aaai.org/index.php/AAAI/article/
view/16535
[62] TsuyoshiIdé,DzungT.Phan,andJayantKalagnanam.2017.Multi-taskmulti-modalmodelsforcollectiveanomaly
detection.In2017IEEEInternationalConferenceonDataMining(ICDM2017)(NewOrleans,LA,November18–21,
2017),VijayRaghavan,SrinivasAluru,GeorgeKarypis,LucioMiele,andXindongWu(Eds.).IEEEComputerSociety,
177–186.https://doi.org/10.1109/ICDM.2017.27
[63] TomoharuIwataandMakotoYamada.2016.Multi-viewanomalydetectionviarobustprobabilisticlatentvariable
models.InAdvancesInNeuralInformationProcessingSystems.1136–1144.
[64] Tomoharu Iwata and Makoto Yamada. 2016. Multi-view anomaly detection via robust probabilistic latent vari-
ablemodels. In Advances in Neural Information Processing Systems 29: AnnualConference onNeural Information
ProcessingSystems2016,(December5–10,2016,Barcelona,Spain),DanielD.Lee,MasashiSugiyama,Ulrikevon
Luxburg, Isabelle Guyon, and Roman Garnett (Eds.). 1136–1144. https://proceedings.neurips.cc/paper/2016/hash/
0f96613235062963ccde717b18f97592-Abstract.html
[65] H.V.Jagadish,NickKoudas,andS.Muthukrishnan.1999.Miningdeviantsinatimeseriesdatabase.InVLDB,Vol.99.
7–10.
ACMComputingSurveys,Vol.56,No.5,Article123.Publicationdate:November2023.

123:30 D.ZhouandJ.He
[66] MiltiadisKandias,AlexiosMylonas,NikosVirvilis,MarianthiTheoharidou,andDimitrisGritzalis.2010.Aninsider
threatpredictionmodel.InInternationalConferenceonTrust,PrivacyandSecurityinDigitalBusiness.Springer,26–37.
[67] Ramneet Kaur, Susmit Jha, Anirban Roy, Sangdon Park, Edgar Dobriban, Oleg Sokolsky, and Insup Lee. 2022.
iDECODe:In-distributionequivarianceforconformalout-of-distributiondetection.In36thAAAIConferenceonAr-
tificialIntelligence(AAAI2022),34thConferenceonInnovativeApplicationsofArtificialIntelligence(IAAI2022),12th
SymposiumonEducationalAdvancesinArtificialIntelligence(EAAI2022)(VirtualEvent,February22–March1,2022).
AAAIPress,7104–7114.https://ojs.aaai.org/index.php/AAAI/article/view/20670
[68] FabianKeller,EmmanuelMüller,andKlemensBöhm.2012.HiCS:Highcontrastsubspacesfordensity-basedoutlier
ranking.InIEEE28thInternationalConferenceonDataEngineering(ICDE2012)(Washington,DC, [Arlington,Vir-
ginia],1–5April,2012),AnastasiosKementsietsidisandMarcosAntonioVazSalles(Eds.).IEEEComputerSociety,
1037–1048.https://doi.org/10.1109/ICDE.2012.88
[69] KamranKhan,SaifUrRehman,KamranAziz,SimonFong,andSababadySarasvady.2014.DBSCAN:Past,present
andfuture.In5thInternationalConferenceontheApplicationsofDigitalInformationandWebTechnologies(ICADIWT
2014).IEEE,232–238.
[70] JonM.Kleinberg.1998.Authoritativesourcesinahyperlinkedenvironment.In9thAnnualACM-SIAMSymposium
onDiscreteAlgorithms(25–27January1998,SanFrancisco,California), HowardJ.Karloff(Ed.).ACM/SIAM,668–677.
http://dl.acm.org/citation.cfm?id=314613.315045
[71] ChristineKlymko,DavidGleich,andTamaraG.Kolda.2014.Usingtrianglestoimprovecommunitydetectionin
directednetworks.arXivpreprintarXiv:1404.5874(2014).
[72] AtsutoshiKumagai,TomoharuIwata,andYasuhiroFujiwara.2019.Transferanomalydetectionbyinferringlatent
domainrepresentations.InAdvancesinNeuralInformationProcessingSystems32:AnnualConferenceonNeuralIn-
formationProcessingSystems2019(NeurIPS2019),(December8–14,2019,Vancouver,BC,Canada),HannaM.Wallach,
HugoLarochelle,AlinaBeygelzimer,Florenced’Alché-Buc,EmilyB.Fox,andRomanGarnett(Eds.).2467–2477.
https://proceedings.neurips.cc/paper/2019/hash/7895fc13088ee37f511913bac71fa66f-Abstract.html
[73] SrijanKumar,FrancescaSpezzano,andV.S.Subrahmanian.2015.VEWS:AWikipediavandalearlywarningsystem.
In21thACMSIGKDDInternationalConferenceonKnowledgeDiscoveryandDataMining(Sydney,NSW,Australia,
August10–13,2015),LongbingCao,ChengqiZhang,ThorstenJoachims,GeoffreyI.Webb,DragosD.Margineantu,
andGrahamWilliams(Eds.).ACM,607–616.https://doi.org/10.1145/2783258.2783367
[74] HimabinduLakkarajuandOsbertBastani.2020.“HowdoIfoolyou?”Manipulatingusertrustviamisleadingblack
boxexplanations.InAAAI/ACMConferenceonAI,Ethics,andSociety.79–85.
[75] DoyupLee,YeongjaeCheon,andWook-ShinHan.2021.Regularizingattentionnetworksforanomalydetection
invisualquestionanswering.In35thAAAIConferenceonArtificialIntelligence(AAAI2021),33rdConferenceon
InnovativeApplicationsofArtificialIntelligence(IAAI2021),11thSymposiumonEducationalAdvancesinArtificial
Intelligence(EAAI2021),(VirtualEvent,February2–9,2021).AAAIPress,1845–1853.https://ojs.aaai.org/index.php/
AAAI/article/view/16279
[76] KevinH.Lee,LingzhouXue,andDavidR.Hunter.2017.Model-basedclusteringoftime-evolvingnetworksthrough
temporalexponential-familyrandomgraphmodels.arXivpreprintarXiv:1712.07325(2017).
[77] DanLi,DachengChen,LeiShi,BaihongJin,JonathanGoh,andSee-KiongNg.2019.MAD-GAN:Multivariateanom-
alydetectionfortimeseriesdatawithgenerativeadversarialnetworks.arXivpreprintarXiv:1901.04997(2019).
[78] KaiLi,ShengLi,ZhengmingDing,WeidongZhang,andYunFu.2018.Latentdiscriminantsubspacerepresentations
formulti-viewoutlierdetection.In32ndAAAIConferenceonArtificialIntelligence,(AAAI-18),30thInnovativeAppli-
cationsofArtificialIntelligence(IAAI-18),and8thAAAISymposiumonEducationalAdvancesinArtificialIntelligence
(EAAI-18)(NewOrleans,LA,February2–7,2018),SheilaA.McIlraithandKilianQ.Weinberger(Eds.).AAAIPress,
3522–3529.https://www.aaai.org/ocs/index.php/AAAI/AAAI18/paper/view/17401
[79] ShengLi,MingShao,andYunFu.2015.Multi-viewlow-rankanalysisforoutlierdetection.In2015SIAMInternational
ConferenceonDataMining(Vancouver,BC,Canada,April30–May2,2015),SureshVenkatasubramanianandJieping
Ye(Eds.).SIAM,748–756.https://doi.org/10.1137/1.9781611974010.84
[80] XiaoleiLiandJiaweiHan.2007.Miningapproximatetop-ksubspaceanomaliesinmulti-dimensionaltime-series
data.InProceedingsofthe33rdInternationalConferenceonVeryLargeDataBases.VLDBEndowment,447–458.
[81] HanfeiLin,SiyuanGao,DavidGotz,FanDu,JingruiHe,andNanCao.2018.Rclens:Interactiverarecategoryexplo-
rationandidentification.IEEETransactionsonVisualizationandComputerGraphics24,7(2018),2223–2237.
[82] WangliLin,LiSun,QiweiZhong,CanLiu,JinghuaFeng,XiangAo,andHaoYang.2021.Onlinecreditpayment
frauddetectionviastructure-awarehierarchicalrecurrentneuralnetwork.In30thInternationalJointConferenceon
ArtificialIntelligence(IJCAI2021)(VirtualEvent/Montreal,Canada,19–27August2021),Zhi-HuaZhou(Ed.).ijcai.org,
3670–3676.https://doi.org/10.24963/ijcai.2021/505
[83] BoyangLiu,Pang-NingTan,andJiayuZhou.2022.Unsupervisedanomalydetectionbyrobustdensityestimation.
In36thAAAIConferenceonArtificialIntelligence(AAAI2022),34thConferenceonInnovativeApplicationsofArtificial
ACMComputingSurveys,Vol.56,No.5,Article123.Publicationdate:November2023.

RareCategoryAnalysisforComplexData:AReview 123:31
Intelligence(IAAI2022),T12thSymposiumonEducationalAdvancesinArtificialIntelligence(EAAI2022)(VirtualEvent,
February22–March1,2022).AAAIPress,4101–4108.https://ojs.aaai.org/index.php/AAAI/article/view/20328
[84] NinghaoLiu,DonghwaShin,andXiaHu.2017.Contextualoutlierinterpretation.arXivpreprintarXiv:1711.10589
(2017).
[85] Zhining Liu, Dawei Zhou, Yada Zhu, Jinjie Gu, and Jingrui He. 2020. Towards fine-grained temporal network
representation via time-reinforced random walk. In 34th AAAI Conference on Artificial Intelligence (AAAI 2020),
32ndInnovativeApplicationsofArtificialIntelligenceConference(IAAI2020),10thAAAISymposiumonEducational
Advances in Artificial Intelligence (EAAI 2020) (New York, February 7–12, 2020). AAAI Press, 4973–4980. https:
//aaai.org/ojs/index.php/AAAI/article/view/5936
[86] JustinMa,LawrenceK.Saul,StefanSavage,andGeoffreyM.Voelker.2009.IdentifyingsuspiciousURLs:Anapplica-
tionoflarge-scaleonlinelearning.In26thAnnualInternationalConferenceonMachineLearning(ICML2009)(Mon-
treal,Quebec,Canada,June14–18,2009)(ACMInternationalConferenceProceedingSeries),AndreaPohoreckyjDany-
luk,LéonBottou,andMichaelL.Littman(Eds.),Vol.382.ACM,681–688.https://doi.org/10.1145/1553374.1553462
[87] RongrongMa,GuansongPang,LingChen,andAntonvandenHengel.2021.Deepgraph-levelanomalydetection
byglocalknowledgedistillation.CoRRabs/2112.10063(2021).arXiv:2112.10063https://arxiv.org/abs/2112.10063
[88] LaurensvanderMaatenandGeoffreyHinton.2008.Visualizingdatausingt-SNE. JournalofMachineLearning
Research9(Nov.2008),2579–2605.
[89] MeghanathMachaandLemanAkoglu.2018.Explaininganomaliesingroupswithcharacterizingsubspacerules.
DataMiningandKnowledgeDiscovery32,5(2018),1444–1480.
[90] EmaadManzoor,SadeghM.Milajerdi,andLemanAkoglu.2016.Fastmemory-efficientanomalydetectioninstream-
ingheterogeneousgraphs.In22ndACMSIGKDDInternationalConferenceonKnowledgeDiscoveryandDataMining.
ACM,1035–1044.
[91] AlejandroMarcosAlvarez,MakotoYamada,AkisatoKimura,andTomoharuIwata.2013.Clustering-basedanom-
alydetectioninmulti-viewdata.In22ndACMInternationalConferenceonConferenceonInformation&Knowledge
Management.ACM,1545–1548.
[92] MarkosMarkouandSameerSingh.2003.Noveltydetection:Areview-Part1:Statisticalapproaches.SignalProcessing
83,12(2003),2481–2497.
[93] BhaskarMehta,SaurabhNangia,ManishGupta,andWolfgangNejdl.2008.Detectingimagespamusingvisualfea-
turesandnearduplicatedetection.In17thInternationalConferenceonWorldWideWeb.ACM,497–506.
[94] TomasMikolov,IlyaSutskever,KaiChen,GregS.Corrado,andJeffDean.2013.Distributedrepresentationsofwords
andphrasesandtheircompositionality.InAdvancesinNeuralInformationProcessingSystems.3111–3119.
[95] YifeiMing,HangYin,andYixuanLi.2022.Ontheimpactofspuriouscorrelationforout-of-distributiondetection.
In36thAAAIConferenceonArtificialIntelligence(AAAI2022),34thConferenceonInnovativeApplicationsofArtificial
Intelligence(IAAI2022),12thSymposiumonEducationalAdvancesinArtificialIntelligence(EAAI2022)(VirtualEvent,
February22–March1,2022).AAAIPress,10051–10059.https://ojs.aaai.org/index.php/AAAI/article/view/21244
[96] ChristophMolnar.2020.InterpretableMachineLearning.Lulu.com.
[97] HosseinMoradiKoupaie,SuhaimiIbrahim,andJavadHosseinkhani.2014.Outlierdetectioninstreamdatabyclus-
teringmethod.InternationalJournalofAdvancedComputerScienceandInformationTechnology(IJACSIT) 2(2014),
25–34.
[98] PeymanMortezaandYixuanLi.2022.Provableguaranteesforunderstandingout-of-distributiondetection.In36th
AAAIConferenceonArtificialIntelligence(AAAI2022),34thConferenceonInnovativeApplicationsofArtificialIntel-
ligence(IAAI2022),12thSymposiumonEducationalAdvancesinArtificialIntelligence(EAAI2022)(VirtualEvent,
February22–March1,2022).AAAIPress,7831–7840.https://ojs.aaai.org/index.php/AAAI/article/view/20752
[99] NourMoustafaandJillSlay.2015.UNSW-NB15:Acomprehensivedatasetfornetworkintrusiondetectionsystems
(UNSW-NB15networkdataset).In2015MilitaryCommunicationsandInformationSystemsConference(MilCIS2015)
(Canberra,Australia,November10–12,2015).IEEE,1–6.https://doi.org/10.1109/MilCIS.2015.7348942
[100] ShanMuthukrishnan,RahulShah,andJeffreyScottVitter.2004.Miningdeviantsintimeseriesdatastreams.In16th
InternationalConferenceonScientificandStatisticalDatabaseManagement,2004.IEEE,41–50.
[101] AlexandreNairac,NeilTownsend,RoyCarr,SteveKing,PeterCowley,andLionelTarassenko.1999.Asystemfor
theanalysisofjetenginevibrationdata.IntegratedComputer-AidedEngineering6,1(1999),53–66.
[102] EricW.T.Ngai,YongHu,YiuHingWong,YijunChen,andXinSun.2011.Theapplicationofdataminingtechniques
infinancialfrauddetection:Aclassificationframeworkandanacademicreviewofliterature.DecisionSupportSys-
tems50,3(2011),559–569.
[103] GiangHoangNguyen,JohnBoazLee,RyanA.Rossi,NesreenK.Ahmed,EunyeeKoh,andSungchulKim.2018.
Continuous-time dynamic network embeddings. In Companion of the Web Conference 2018 (WWW 2018) (Lyon,
France,April23–27,2018),Pierre-AntoineChampin,FabienGandon,MouniaLalmas,andPanagiotisG.Ipeirotis
(Eds.).ACM,969–976.https://doi.org/10.1145/3184558.3191526
ACMComputingSurveys,Vol.56,No.5,Article123.Publicationdate:November2023.

123:32 D.ZhouandJ.He
[104] FeipingNie,GuohaoCai,andXuelongLi.2017.Multi-viewclusteringandsemi-supervisedclassificationwithadap-
tiveneighbours.In31stAAAIConferenceonArtificialIntelligence(February4–9,2017,SanFrancisco,California),
SatinderP.SinghandShaulMarkovitch(Eds.).AAAIPress,2408–2414.http://aaai.org/ocs/index.php/AAAI/AAAI17/
paper/view/14833
[105] JiachengPan,DongmingHan,FangzhouGuo,DaweiZhou,NanCao,JingruiHe,MingliangXu,andWeiChen.2020.
RCAnalyzer:Visualanalyticsofrarecategoriesindynamicnetworks.FrontiersInf.Technol.Electron.Eng.21,4(2020),
491–506.https://doi.org/10.1631/FITEE.1900310
[106] GuansongPang,ChunhuaShen,andAntonvandenHengel.2019.Deepanomalydetectionwithdeviationnetworks.
In25thACMSIGKDDInternationalConferenceonKnowledgeDiscovery&DataMining.353–362.
[107] GuansongPang,AntonvandenHengel,ChunhuaShen,andLongbingCao.2021.Towarddeepsupervisedanomaly
detection:Reinforcementlearningfrompartiallylabeledanomalydata.In27thACMSIGKDDConferenceonKnowl-
edgeDiscoveryandDataMining(KDD’21)(VirtualEvent,Singapore,August14–18,2021),FeidaZhu,BengChin
Ooi,andChunyanMiao(Eds.).ACM,1298–1308.https://doi.org/10.1145/3447548.3467417
[108] DhavalPatel.2023.Timeseriesanomalydetectiontool:Handsoflab.InAAAIConferenceonArtificialIntelligence.
[109] DanPellegandAndrewW.Moore.2005.Activelearningforanomalyandrare-categorydetection.InAdvancesin
NeuralInformationProcessingSystems.1073–1080.
[110] BryanPerozzi,LemanAkoglu,PatriciaIglesiasSánchez,andEmmanuelMüller.2014.Focusedclusteringandoutlier
detectioninlargeattributedgraphs.In20thACMSIGKDDInternationalConferenceonKnowledgeDiscoveryandData
Mining.ACM,1346–1355.
[111] BryanPerozzi,RamiAl-Rfou,andStevenSkiena.2014.Deepwalk:Onlinelearningofsocialrepresentations.In20th
ACMSIGKDDInternationalConferenceonKnowledgeDiscoveryandDataMining(August24-27,2014,NewYork,NY)
ACM,701–710.
[112] GeoPertea,XiaoqiuHuang,FengLiang,ValentinAntonescu,RazvanSultana,SvetlanaKaramycheva,YuandanLee,
JosephWhite,FooCheung,BabakParvizi,JenniferTsai,andJohnQuackenbush.2003.TIGRgeneindicesclustering
tools(TGICL):AsoftwaresystemforfastclusteringoflargeESTdatasets.Bioinform.19,5(2003),651–652.https:
//doi.org/10.1093/bioinformatics/btg034
[113] CliftonPhua,VincentLee,KateSmith,andRossGayler.2010.Acomprehensivesurveyofdatamining-basedfraud
detectionresearch.arXivpreprintarXiv:1009.6119(2010).
[114] AndreaDalPozzolo,OlivierCaelen,ReidA.Johnson,andGianlucaBontempi.2015.Calibratingprobabilitywith
undersamplingforunbalancedclassification.InIEEESymposiumSeriesonComputationalIntelligence(SSCI2015)
(CapeTown,SouthAfrica,December7–10,2015).IEEE,159–166.https://doi.org/10.1109/SSCI.2015.33
[115] StephenRanshous,ShitianShen,DanaiKoutra,SteveHarenberg,ChristosFaloutsos,andNagizaF.Samatova.2015.
Anomaly detection in dynamic networks: A survey. Wiley Interdisciplinary Reviews: Computational Statistics 7,
3(2015),223–247.
[116] UmaaRebbapragada,PavlosProtopapas,CarlaE.Brodley,andCharlesAlcock.2009.Findinganomalousperiodic
timeseries.MachineLearning74,3(2009),281–313.
[117] MaurizioScarpa,ZsuzsannaAlmássy,MichaelBeck,OlafBodamer,IainA.Bruce,LindaDeMeirleir,NathalieGuf-
fon,EncarnaGuillén-Navarro,PaulineHensman,SimonJones,etal.2011.MucopolysaccharidosistypeII:European
recommendationsforthediagnosisandmultidisciplinarymanagementofararedisease.OrphanetJournalofRare
Diseases6,1(2011),72.
[118] FrançoisSchnitzler,ThomasLiebig,ShieMannor,GustavoSouto,SebastianBothe,andHendrikStange.2014.Het-
erogeneousstreamprocessingfordisasterdetectionandalarming.InIEEEInternationalConferenceonBigData.IEEE
Press,914–923.
[119] Karlton Sequeira and Mohammed Zaki. 2002. ADMIT: Anomaly-based data mining for intrusions. In 8th ACM
SIGKDDInternationalConferenceonKnowledgeDiscoveryandDataMining.ACM,386–395.
[120] ShubhranshuShekhar,NeilShah,andLemanAkoglu.2021.FairOD:Fairness-awareoutlierdetection.InAAAI/ACM
ConferenceonAI,Ethics,andSociety(AIES’21)(VirtualEvent,May19–21,2021)MarionFourcade,BenjaminKuipers,
SethLazar,andDeirdreK.Mulligan(Eds.).ACM,210–220.https://doi.org/10.1145/3461702.3462517
[121] LifengShen,ZhongzhongYu,QianliMa,andJamesT.Kwok.2021.Timeseriesanomalydetectionwithmultiresolu-
tionensembledecoding.In35thAAAIConferenceonArtificialIntelligence(AAAI2021),33rdConferenceonInnovative
ApplicationsofArtificialIntelligence(IAAI2021),11thSymposiumonEducationalAdvancesinArtificialIntelligence
(EAAI2021)(VirtualEvent,February2–9,2021).AAAIPress,9567–9575.https://ojs.aaai.org/index.php/AAAI/article/
view/17152
[122] Xiang-RongSheng,De-ChuanZhan,SuLu,andYuanJiang.2019.Multi-viewanomalydetection:Neighborhood
inlocalitymatters.In33rdAAAIConferenceonArtificialIntelligence(AAAI2019),31stInnovativeApplicationsof
ArtificialIntelligenceConference(IAAI2019),9thAAAISymposiumonEducationalAdvancesinArtificialIntelligence
(EAAI2019),(Honolulu,Hawaii,January27–February1,2019).AAAIPress,4894–4901.https://doi.org/10.1609/aaai.
v33i01.33014894
ACMComputingSurveys,Vol.56,No.5,Article123.Publicationdate:November2023.

RareCategoryAnalysisforComplexData:AReview 123:33
[123] JouWonSong,KyeongboKong,YeInPark,SeongGyunKim,andSuk-JuKang.2021.AnoSeg:Anomalysegmen-
tationnetworkusingself-supervisedlearning.CoRRabs/2110.03396(2021).arXiv:2110.03396https://arxiv.org/abs/
2110.03396
[124] DanielA.SpielmanandShang-HuaTeng.2013.Alocalclusteringalgorithmformassivegraphsanditsapplication
tonearlylineartimegraphpartitioning.SIAMJ.Comput.42,1(2013),1–26.https://doi.org/10.1137/080744888
[125] KumarSricharanandKamalikaDas.2014.Localizinganomalouschangesintime-evolvinggraphs.In2014ACM
SIGMODInternationalConferenceonManagementofData.ACM,1347–1358.
[126] JimengSun,ChristosFaloutsos,SpirosPapadimitriou,andPhilipS.Yu.2007.Graphscope:Parameter-freeminingof
largetime-evolvinggraphs.In13thACMSIGKDDInternationalConferenceonKnowledgeDiscoveryandDataMining.
ACM,687–696.
[127] JimengSun,HuimingQu,DeepayanChakrabarti,andChristosFaloutsos.2005.Neighborhoodformationandanom-
alydetectioninbipartitegraphs.In5thIEEEInternationalConferenceonDataMining.IEEE,418–425.
[128] Yi-XuanSunandWeiWang.2022.Exploitingmixedunlabeleddatafordetectingsamplesofseenandunseenout-
of-distributionclasses.In36thAAAIConferenceonArtificialIntelligence(AAAI2022),34thConferenceonInnova-
tiveApplicationsofArtificialIntelligence(IAAI2022),12thSymposiumonEducationalAdvancesinArtificialIntelli-
gence(EAAI2022)(VirtualEvent,February22–March1,2022).AAAIPress,8386–8394.https://ojs.aaai.org/index.
php/AAAI/article/view/20814
[129] YingSun,WenjunWang,NannanWu,WeiYu,andXueChen.2020.Anomalysubgraphdetectionwithfeature
transfer.In29thACMInternationalConferenceonInformationandKnowledgeManagement(CIKM’20)(VirtualEvent,
Ireland,October19–23,2020),Mathieud’Aquin,StefanDietze,ClaudiaHauff,EdwardCurry,andPhilippeCudré-
Mauroux(Eds.).ACM,1415–1424.https://doi.org/10.1145/3340531.3411968
[130] JianTang,MengQu,MingzheWang,MingZhang,JunYan,andQiaozhuMei.2015.LINE:Large-scaleinformation
networkembedding.In24thInternationalConferenceonWorldWideWeb(WWW2015)(Florence,Italy,May18–22,
2015).1067–1077.
[131] EricoTjoaandCuntaiGuan.2020.Asurveyonexplainableartificialintelligence(XAI):TowardmedicalXAI.IEEE
TransactionsonNeuralNetworksandLearningSystems32,11(2020),4793–4813.
[132] HanghangTongandChing-YungLin.2011.Non-negativeresidualmatrixfactorizationwithapplicationtograph
anomalydetection.In2011SIAMInternationalConferenceonDataMining.SIAM,143–153.
[133] JasonTumlinson.2011.Astronomy:Anewspinonthefirststars.Nature472,7344(2011),426.
[134] AaronTuor,SamuelKaplan,BrianHutchinson,NicoleNichols,andSeanRobinson.2017.Deeplearningforunsuper-
visedinsiderthreatdetectioninstructuredcybersecuritydatastreams.InWorkshopsatthe31stAAAIConferenceon
ArtificialIntelligence.
[135] PavanVatturiandWeng-KeenWong.2009.Categorydetectionusinghierarchicalmeanshift.In15thACMSIGKDD
InternationalConferenceonKnowledgeDiscoveryandDataMining.ACM,847–856.
[136] VincentVercruyssen,WannesMeert,andJesseDavis.2020.Transferlearningforanomalydetectionthroughlocal-
izedandunsupervisedinstanceselection.In34thConferenceonArtificialIntelligence(AAAI2020),32ndInnovative
ApplicationsofArtificialIntelligenceConference(IAAI2020),10thAAAISymposiumonEducationalAdvancesinArtifi-
cialIntelligence(EAAI2020)(NewYorkFebruary7–12,2020).AAAIPress,6054–6061.https://aaai.org/ojs/index.php/
AAAI/article/view/6068
[137] NikilWale,IanA.Watson,andGeorgeKarypis.2008.Comparisonofdescriptorspacesforchemicalcompound
retrievalandclassification.Knowl.Inf.Syst.14,3(2008),347–375.https://doi.org/10.1007/s10115-007-0103-5
[138] ZhenWangandChaoLan.2020.TowardsahierarchicalBayesianmodelofmulti-viewanomalydetection.In29th
InternationalJointConferenceonArtificialIntelligence(IJCAI2020),ChristianBessiere(Ed.).ijcai.org,2420–2426.
https://doi.org/10.24963/ijcai.2020/335
[139] SteveWebb,JamesCaverlee,andCaltonPu.2006.IntroducingtheWebbspamcorpus:Usingemailspamtoidentify
webspamautomatically.In3rdConferenceonEmailandAnti-Spam(CEAS2006)(July27–28,2006,MountainView,
California).http://www.ceas.cc/2006/listabs.html#6.pdf
[140] JamesD.Wilson,NathanielT.Stevens,andWilliamH.Woodall.2016.Modelingandestimatingchangeintemporal
networksviaadynamicdegreecorrectedstochasticblockmodel.arXivpreprintarXiv:1605.04049(2016).
[141] GangWuandEdwardY.Chang.2003.Adaptivefeature-spaceconformaltransformationforimbalanced-datalearn-
ing.In20thInternationalConferenceonMachineLearning(ICML-03).816–823.
[142] JunWu,JingruiHe,andYongmingLiu.2018.ImVerde:Vertex-diminishedrandomwalkforlearningimbalanced
networkrepresentation.In2018IEEEInternationalConferenceonBigData(BigData).IEEE,871–880.
[143] ShuangWu,JingyuZhao,andGuangjianTian.2022.Understandingandmitigatingdatacontaminationindeep
anomalydetection:Akernel-basedapproach.In31stInternationalJointConferenceonArtificialIntelligence(IJCAI
2022)(Vienna,Austria,23–29July2022)LucDeRaedt(Ed.).ijcai.org,2319–2325.https://doi.org/10.24963/ijcai.2022/
322
ACMComputingSurveys,Vol.56,No.5,Article123.Publicationdate:November2023.

123:34 D.ZhouandJ.He
[144] DongboXi,BowenSong,FuzhenZhuang,YongchunZhu,ShuaiChen,TianyiZhang,YuanQi,andQingHe.2021.
Modelingthefieldvaluevariationsandfieldinteractionssimultaneouslyforfrauddetection.In35thAAAIConference
onArtificialIntelligence(AAAI2021),33rdConferenceonInnovativeApplicationsofArtificialIntelligence(IAAI2021),
11thSymposiumonEducationalAdvancesinArtificialIntelligence(EAAI2021)(VirtualEvent,February2–9,2021).
AAAIPress,14957–14965.https://ojs.aaai.org/index.php/AAAI/article/view/17755
[145] WeiXu,LingHuang,ArmandoFox,DavidA.Patterson,andMichaelI.Jordan.2009.Onlinesystemproblemdetection
byminingpatternsofconsolelogs.In9thIEEEInternationalConferenceonDataMining(ICDM2009)(Miami,Florida,
6-9December2009)WeiWang,HillolKargupta,SanjayRanka,PhilipS.Yu,andXindongWu(Eds.).IEEEComputer
Society,588–597.https://doi.org/10.1109/ICDM.2009.19
[146] PeiYang,JingruiHe,andJia-YuPan.2015.Learningcomplexrarecategorieswithdualheterogeneity.In2015SIAM
InternationalConferenceonDataMining.SIAM,523–531.
[147] PeiYang,HongxiaYang,HaodaFu,DaweiZhou,JiepingYe,TheodorosLappas,andJingruiHe.2015.Jointlymodeling
labelandfeatureheterogeneityinmedicalinformatics.ACMTransactionsonKnowledgeDiscoveryfromData(TKDD-
2015)(2015).
[148] ZhilinYang,WilliamW.Cohen,andRuslanSalakhutdinov.2016.Revisitingsemi-supervisedlearningwithgraph
embeddings.In33ndInternationalConferenceonMachineLearning(ICML2016)(NewYorkCity,NY,June19–24,
2016).40–48.
[149] YasserYasamiandFarshadSafaei.2017.Astatisticalinfinitefeaturecascade-basedapproachtoanomalydetection
fordynamicsocialnetworks.ComputerCommunications100(2017),52–64.
[150] Chin-ChiaMichaelYeh,YanZhu,LiudmilaUlanova,NurjahanBegum,YifeiDing,HoangAnhDau,DiegoFurtado
Silva,AbdullahMueen,andEamonnKeogh.2016.MatrixprofileI:Allpairssimilarityjoinsfortimeseries:Aunifying
viewthatincludesmotifs,discordsandshapelets.In2016IEEE16thInternationalConferenceonDataMining(ICDM).
IEEE,1317–1322.
[151] HaoYin,AustinR.Benson,JureLeskovec,andDavidF.Gleich.2017.Localhigher-ordergraphclustering.InProceed-
ingsofthe23rdACMSIGKDDInternationalConferenceonKnowledgeDiscoveryandDataMining.ACM,555–564.
[152] HaoYin,AustinR.Benson,JureLeskovec,andDavidF.Gleich.2017.Localhigher-ordergraphclustering.In23rd
ACMSIGKDDInternationalConferenceonKnowledgeDiscoveryandDataMining(Halifax,NS,Canada,August13–17,
2017).ACM,555–564.https://doi.org/10.1145/3097983.3098069
[153] MinjiYoon,BryanHooi,KijungShin,andChristosFaloutsos.2019.Fastandaccurateanomalydetectionindynamic
graphswithatwo-prongedapproach.In25thACMSIGKDDInternationalConferenceonKnowledgeDiscovery&Data
Mining.ACM,647–657.
[154] BingYu,HaotengYin,andZhanxingZhu.2018.Spatio-temporalgraphconvolutionalnetworks:Adeeplearning
frameworkfortrafficforecasting.In27thInternationalJointConferenceonArtificialIntelligence(IJCAI2018)(July
13–19,2018,Stockholm,Sweden),JérômeLang(Ed.).ijcai.org,3634–3640.https://doi.org/10.24963/ijcai.2018/505
[155] WenchaoYu,WeiCheng,CharuC.Aggarwal,KaiZhang,HaifengChen,andWeiWang.2018.Netwalk:Aflexible
deepembeddingapproachforanomalydetectionindynamicnetworks.In24thACMSIGKDDInternationalConfer-
enceonKnowledgeDiscovery&DataMining.ACM,2672–2681.
[156] ChangqingZhang,EhsanAdeli,TaoZhou,XiaoboChen,andDinggangShen.2018.Multi-layermulti-viewclassifi-
cationforAlzheimer’sdiseasediagnosis.In32ndAAAIConferenceonArtificialIntelligence(AAAI-18),30thInnovative
ApplicationsofArtificialIntelligence(IAAI-18),and8thAAAISymposiumonEducationalAdvancesinArtificialIntel-
ligence(EAAI-18)(NewOrleans,Louisiana,February2–7,2018)SheilaA.McIlraithandKilianQ.Weinberger(Eds.).
AAAIPress,4406–4413.https://www.aaai.org/ocs/index.php/AAAI/AAAI18/paper/view/16864
[157] GuoxiZhang,TomoharuIwata,andHisashiKashima.2017.Robustmulti-viewtopicmodelingbyincorporatingde-
tectinganomalies.InJointEuropeanConferenceonMachineLearningandKnowledgeDiscoveryinDatabases.Springer,
238–250.
[158] SiZhang,DaweiZhou,MehmetYigitYildirim,ScottAlcorn,JingruiHe,HasanDavulcu,andHanghangTong.2017.
HiDDen:Hierarchicaldensesubgraphdetectionwithapplicationtofinancialfrauddetection.In2017SIAMInterna-
tionalConferenceonDataMining.SocietyforIndustrialandAppliedMathematics,570–578.
[159] WeiqiZhang,ChenZhang,andFugeeTsung.2022.GRELEN:Multivariatetimeseriesanomalydetectionfromthe
perspectiveofgraphrelationallearning.In31stInternationalJointConferenceonArtificialIntelligence(IJCAI2022)
(Vienna,Austria,23–29July2022),LucDeRaedt(Ed.).ijcai.org,2390–2397.https://doi.org/10.24963/ijcai.2022/332
[160] HandongZhaoandYunFu.2015.Dual-regularizedmulti-viewoutlierdetection..In24thInternationalJointConfer-
enceonArtificialIntelligence(IJCAI2015).4077–4083.
[161] YingZhao,JunjunChen,DiWu,JianTeng,andShuiYu.2019.Multi-tasknetworkanomalydetectionusingfeder-
atedlearning.In10thInternationalSymposiumonInformationandCommunicationTechnology(Hanoi,HaLongBay,
Vietnam,December4–6,2019).ACM,273–279.https://doi.org/10.1145/3368926.3369705
ACMComputingSurveys,Vol.56,No.5,Article123.Publicationdate:November2023.

RareCategoryAnalysisforComplexData:AReview 123:35
[162] Jia-XingZhong,NannanLi,WeijieKong,ShanLiu,ThomasH.Li,andGeLi.2019.Graphconvolutionallabelnoise
cleaner:Trainaplug-and-playactionclassifierforanomalydetection.InIEEEConferenceonComputerVisionand
PatternRecognition.1237–1246.
[163] DaweiZhou,JingruiHe,K.SelukCandan,andHasanDavulcu.2015.MUVIR:Multi-viewrarecategorydetection.In
24thInternationalJointConferenceonArtificialIntelligence(IJCAI-15).
[164] DaweiZhou,JingruiHe,YuCao,andJae-sunSeo.2016.Bi-levelraretemporalpatterndetection.InIEEEInternational
ConferenceonDataMiningSeries(ICDM2016).
[165] DaweiZhou,JingruiHe,HasanDavulcu,andRossMaciejewski.2018.Motif-preservingdynamiclocalgraphcut.In
IEEEInternationalConferenceonBigData(BigData2018)(Seattle,Washington,December10–13,2018),NaokiAbe,
HuanLiu,CaltonPu,XiaohuaHu,NesreenK.Ahmed,MuQiao,YangSong,DonaldKossmann,BingLiu,KisungLee,
JiliangTang,JingruiHe,andJeffreyS.Saltz(Eds.).IEEE,1156–1161.https://doi.org/10.1109/BigData.2018.8622263
[166] DaweiZhou,JingruiHe,HongxiaYang,andWeiFan.2018.SPARC:Self-pacednetworkrepresentationforfew-shot
rarecategorycharacterization.In24thACMSIGKDDInternationalConferenceonKnowledgeDiscovery&DataMining.
ACM,2807–2816.
[167] DaweiZhou,ArunKarthikeyan,KangyangWang,NanCao,andJingruiHe.2017.Discoveringrarecategoriesfrom
graphstreams.DataMiningandKnowledgeDiscovery31,2(2017),400–423.
[168] DaweiZhou,KangyangWang,NanCao,andJingruiHe.2015.Rarecategorydetectionontime-evolvinggraphs.In
IEEEInternationalConferenceonDataMining(ICDM2015).IEEE.
[169] DengyongZhou,JasonWeston,ArthurGretton,OlivierBousquet,andBernhardSchölkopf.2004.Rankingondata
manifolds.InAdvancesinNeuralInformationProcessingSystems.169–176.
[170] DaweiZhou,SiZhang,MehmetYigitYildirim,ScottAlcorn,HanghangTong,HasanDavulcu,andJingruiHe.2017.
Alocalalgorithmforstructure-preservinggraphcut.In23rdACMSIGKDDInternationalConferenceonKnowledge
DiscoveryandDataMining.ACM,655–664.
[171] DaweiZhou,LechengZheng,JiaweiHan,andJingruiHe.2020.Adata-drivengraphgenerativemodelfortemporal
interactionnetworks.In26thACMSIGKDDConferenceonKnowledgeDiscoveryandDataMining(KDD’20)(Virtual
Event,CA,August23–27,2020)RajeshGupta,YanLiu,JiliangTang,andB.AdityaPrakash(Eds.).ACM,401–411.
https://doi.org/10.1145/3394486.3403082
[172] Zhi-HuaZhou.2018.Abriefintroductiontoweaklysupervisedlearning.NationalScienceReview5,1(2018),44–53.
[173] ArthurZimek,ErichSchubert,andHans-PeterKriegel.2012.Asurveyonunsupervisedoutlierdetectioninhigh-
dimensionalnumericaldata.StatisticalAnalysisandDataMining:TheASADataScienceJournal5,5(2012),363–387.
Received15March2022;revised23May2023;accepted18September2023
ACMComputingSurveys,Vol.56,No.5,Article123.Publicationdate:November2023.