---
conversion_metadata:
  converted_at: "2026-07-21T10:06:24Z"
  converter_tool: "markitdown"
  converter_version: "0.1.6"
  source_pdf: "Zhang et al.pdf"
  source_pdf_sha256: "33617c7d44c1cb12c6146c6c4f3618737b7d4a1f365f14fde3e32ec2a7b0c6f2"
  page_count: 14
  markdown_char_count: 193770
---

<!-- PAGE-AWARE EXTRACTION (via pdfminer.six) -->

<!-- PAGE 1 -->

An Experimental Evaluation of Anomaly Detection in Time
Series

Aoqian Zhang
Beijing Institute of Technology
aoqian.zhang@bit.edu.cn

Shuqing Deng
Beijing Institute of Technology
shuqing.deng@bit.edu.cn

Dongping Cui
Beijing Institute of Technology
dongping.cui@bit.edu.cn

Ye Yuan
Beijing Institute of Technology
yuan-ye@bit.edu.cn

Guoren Wang
Beijing Institute of Technology
wanggr@bit.edu.cn

ABSTRACT
Anomaly detection in time series data has been studied for dec-
ades in both statistics and computer science. Various algorithms
have been proposed for different scenarios, such as fraud detec-
tion, environmental monitoring, manufacturing, and healthcare.
However, there is a lack of comparative evaluation of these state-
of-the-art approaches, especially in the same test environment and
with the same benchmark, making it difficult for users to select an
appropriate method for real-world applications. In this paper, we
present a taxonomy of anomaly detection methods based on the
main features, i.e., data dimension, processing technique, and an-
omaly type and six inner classes. We perform systematic intra- and
inter-class comparisons of seventeen state-of-the-art algorithms on
real and synthetic datasets with a point metric commonly used in
classification problems and a range metric specifically designed for
subsequence anomalies in time series data. We analyze the prop-
erties of these algorithms and test them in terms of effectiveness,
efficiency, and robustness to anomaly rates, data sizes, number of
dimensions, anomaly patterns, and threshold settings. We also test
their performance in different use cases. Finally, we provide a prac-
tical guide for detecting anomalies in time series and discussions.

PVLDB Reference Format:
Aoqian Zhang, Shuqing Deng, Dongping Cui, Ye Yuan, and Guoren Wang.
An Experimental Evaluation of Anomaly Detection in Time Series. PVLDB,
17(3): 483-496, 2023.
doi:10.14778/3632093.3632110

PVLDB Artifact Availability:
The source code, data, and/or other artifacts have been made available at
https://github.com/zaqthss/experiment-tsad.

1 INTRODUCTION
Time series is one of the most commonly used data types in recent
decades. Time series analysis involves methods of data analysis to
gain valuable insights. Anomaly detection aims to find rare obser-
vations that deviate significantly from the majority of data [23] and
is the most important part of time series analysis (mining). It has

This work is licensed under the Creative Commons BY-NC-ND 4.0 International
License. Visit https://creativecommons.org/licenses/by-nc-nd/4.0/ to view a copy of
this license. For any use beyond those covered by this license, obtain permission by
emailing info@vldb.org. Copyright is held by the owner/author(s). Publication rights
licensed to the VLDB Endowment.
Proceedings of the VLDB Endowment, Vol. 17, No. 3 ISSN 2150-8097.
doi:10.14778/3632093.3632110

been studied in various applications, such as fraud detection [9],
environmental monitoring alerting [18] and industrial manufac-
turing [10], cyber attack identification [36], etc. Unfortunately, an
anomaly is rather challenging to define, especially in the context
of time series data [54]. For the following reasons, it is difficult to
evaluate the performance of an anomaly detection method and to
select the suitable one (with appropriate parameters) for handling
anomalies in real-world scenarios.

The first reason is the complexity and diversity of time series
data [29]. A single timeseries data may be univariate or multivari-
ate, and the latter may have a number of dimensions. Moreover,
the anomalies encountered may be of different types [22]. Several
algorithms have been proposed to detect anomalous behavior using
different techniques, but they often focus on a specific case. For
instance, [25] is only able to find anomalous data points in uni-
variate time series. [7] can handle univariate data streams, but can
only detect anomalous patterns of a certain length. Therefore, after
analyzing the state-of-the-art anomaly detection algorithms, we
classify them into three facets representing the three main features
[5], i.e., data dimension, processing technique, and anomaly type.
We can further divide them into classes under a particular facet, as
shown in Figure 1, to make more detailed comparisons.

The second reason is the lack of thorough testing with the same
datasets on the same platform and with the same metrics. Different
works provide comparisons with different scores, even with the
same basic precision-recall-F1 metric [2]. For example, [52] calcu-
lates F1 score using average precision and average recall, whereas
[1] considers F1 score after threshold adjustment. In addition, the
baselines being compared may be written in a different language
or use different data structures. Therefore, for a fair performance
comparison, systematic experiments should be performed between
methods of the same class in the same test environment, which is
called intra-class comparison.

The third reason arises from the observation that some recent
papers [1, 3, 52, 58] evaluate their methods under point metrics on
datasets with subsequence anomaly. These are essentially point
methods, as an anomaly score is assigned to each data point and
those points whose score is above a threshold are reported as an
anomaly. In addition, to interpret the detection on a subsequence,
they modify the prediction results before evaluation using the point-
adjust [62] method. However, a comprehensive experiment should
be employed to analyze the effects of these measures. In terms of
efficiency, especially in big data applications where time series data
have high dimensions (more than 50) and large scales (more than

483

---

<!-- PAGE 2 -->

100k), the trade-off between effectiveness and efficiency should be
considered. In particular, the possibility of implementing univariate
models on each data dimension [28] and finding out to what extent
online detectors approximate the performance of batch methods
[12, 44] could receive special attention. Therefore, comparisons
between classes in the same facet, which we call inter-class com-
parisons, are also useful. Finally, the essential features of anomaly
detection algorithms, including robustness in terms of threshold
setting, should be captured in terms of practical applications. Sys-
tematic experiments with different real cases and analysis of the
behavior of these algorithms will be helpful for users.

1.1 Contributions
To the best of our knowledge, this is the first in-depth experimental
study to provide both intra-class and inter-class evaluations. Our
main contributions in this paper are summarized as follows.
(1) We propose a taxonomy of methods for detecting anomalies in
time series based on their essential features in three facets and
six inner classes in Section 2.

(2) We present brief descriptions of 17 state-of-the-art methods
in Section 3. Furthermore, we re-implement 10 of them with
JAVA, refactor all methods with the same code structure, and
build a testing framework to avoid the potential impact.
(3) We provide systematic intra-class comparisons under different
scenarios with real-world and synthetic datasets in Section 4.2,
including (a) effectiveness with point- and range-based metrics,
(b) anomaly rates, (c) data sizes (scalability), (d) dimensions, (e)
anomaly patterns.

(4) We employ inter-class comparisons and draw interesting find-
ings in Section 4.3, like (a) point anomaly methods can also
perform well under subsequence anomaly cases, (b) using range
metrics on subsequence data can lead to more reasonable and
robust results, (c) point-adjust method tends to report ‘false’
higher accuracy results and may mislead analysis.

(5) We analyze the capability of methods under different applic-
ation cases, consisting of (a) the false positives and negatives
they generate, (b) whether they can detect anomalies as early
as possible and provide recommendations in Section 5.

1.2 Related Work

Table 1: Comparison of TAD Experimental Surveys

Exp Survey

DODDS [57]
MD [12]
TUD [8]
TODS [31]
Exathlon [29]
TSB-UAD [47]
Meta [44]
HPI [49]
Our work

Dimension
<Uni, Mul, Inter>
<(cid:37), (cid:33), (cid:37)>
<(cid:33), (cid:37), (cid:37)>
<(cid:33), (cid:37), (cid:37)>
<(cid:37), (cid:33), (cid:37)>
<(cid:37), (cid:33), (cid:37)>
<(cid:33), (cid:37), (cid:37)>
<(cid:37), (cid:33), (cid:37)>
<(cid:33), (cid:33), (cid:37)>
<(cid:33), (cid:33), (cid:33)>

Processing
<Batch, Online, Inter>
<(cid:37), (cid:33), (cid:37)>
<(cid:37), (cid:33), (cid:37)>
<(cid:33), (cid:37), (cid:37)>
<(cid:33), (cid:37), (cid:37)>
<(cid:33), (cid:37), (cid:37)>
<(cid:33), (cid:37), (cid:37)>
<(cid:33),(cid:33), (cid:33)>
<(cid:33), (cid:37), (cid:37)>
<(cid:33),(cid:33), (cid:33)>

Anomaly Type
<Point, Range, Inter>
<(cid:33), (cid:37), (cid:37)>
<(cid:33), (cid:33), (cid:37)>
<(cid:33), (cid:37), (cid:37)>
<(cid:33), (cid:33), (cid:33)>
<(cid:37), (cid:33), (cid:37)>
<(cid:33), (cid:33), (cid:37)>
<(cid:33), (cid:33), (cid:37)>
<(cid:33), (cid:33), (cid:37)>
<(cid:33), (cid:33), (cid:33)>

Threshold
Robustness
(cid:37)
(cid:37)
(cid:37)
(cid:37)
(cid:33)
(cid:37)
(cid:37)
(cid:37)
(cid:33)

Application
Guideline
(cid:37)
(cid:33)
(cid:33)
(cid:37)
(cid:33)
(cid:37)
(cid:33)
(cid:33)
(cid:33)

We summarize 8 previous experimental studies on time series
anomaly detection and our work in Table 1. The first three columns
represent the fundamental facets covered in the study, e.g., in the
first column, Uni indicates that the work includes univariate detec-
tion methods, Mul stands for multivariate detection methods, while

Inter represents the consideration of comparisons between uni-
variate and multivariate methods. Similarly, <Batch, Online, Inter>
refers to the processing technique, while <Point, Range, Inter>
focuses on the type of target anomaly. Thresholds Robustness in-
dicates whether the work examines the robustness of the compared
methods to thresholding. Finally, Application Guideline indicates
whether the work provides practical guidelines for method selection
in real-world scenarios with different requirements.

In [57], distance-based online detection methods of point out-
liers in data streams are evaluated. However, only efficiency factors
such as CPU time and leakage memory are tested under different
parameters. MD [12] compares runtime and efficacy of different
detection methods for four types of anomalies in real streaming
cases. It serves as a guide for selecting the ‘best’ univariate tech-
nique in terms of real-time and accuracy, but lacks considerations
for the characteristics of the datasets and the type of application.
TUD [8] focuses on supervised methods for univariate data. TODS
[31] revises outlier definitions and proposes a new taxonomy for
anomaly types. It tests batch methods under different anomaly
rates for different types of anomalies, but omits evaluations under
other factors such as data dimensions. Exathlon [29] generates a
novel benchmarking platform. Three deep learning methods are
tested on the proposed datasets with range anomalies and eval-
uated by range metrics [53]. Its major difference to others is the
capability of evaluating explanation discovery results, which is not
covered by our work. Nevertheless, it fails to compare more types
of anomaly detection methods and provide more comprehensive
analysis. TSB-UAD [47] establishes a new benchmark to facilitate
the evaluation of univariate methods and evaluates several batch
methods to demonstrate the robustness of the proposed benchmark,
but does not address multivariate time series cases. The aforemen-
tioned TODS, Exathlon, and TSB-UAD provide novel benchmarks
based on different techniques that present the main contributions
and differences from other studies. Meta [44] presents a qualitative
review of online detectors from different families and proposes a
fair evaluation environment for online and offline detectors over
multivariate data. The goal is to find out to what extent online de-
tectors approximate the performance of offline detectors. However,
it focuses only on unsupervised methods for detecting point anom-
alies (including range anomalies with point metrics) and leaves out
(semi)supervised methods.

HPI [49] makes an exhaustive evaluation of 71 anomaly detec-
tion methods and evaluates them on various datasets with different
types of anomalies. Although it provides a comprehensive evalu-
ation, it still has some untouched areas, which we extend as follows:
(1) They optimize the parameters of all methods globally over the
same well-labeled synthetic dataset, but we tune these parameters
per dataset to get a fairer evaluation with their best performance;
(2) They do not consider the translation of anomaly scores to an-
omaly labels via thresholding, however, we analyze the robustness
of using different thresholding techniques since anomaly identi-
fication is crucial in most real-world scenarios; (3) They simply
implement point and range metrics for point and subsequence an-
omalies, respectively, without deeper analysis. We also perform
the inter-class comparison using a point metric for subsequence
anomalies, which has been widely used in previous studies, and
find insightful results; (4) Their research insights can help users

484

---

<!-- PAGE 3 -->

2.2 Analysis Facets
The anomaly analysis problems can be categorized in various ways
[22]. In this work, we propose a comprehensive taxonomy consist-
ing of the following three facets, i.e., data dimension, processing
technique, and anomaly type, as shown in Figure 1. For each facet,
we further divide detection methods into classes. The details of
these facets and classes are presented in this section.

2.2.1 Data dimension. The number of time-dependent variables
that an anomaly detection method can consider simultaneously is
its essential feature [5]. Following Definition 2.1, 𝑿 is called as a
univariate time series if 𝐷 = 1 while 𝑿 is a multivariate time
series if 𝐷 > 1.

Scenario 1: High dimension. Theoretically, multivariate methods
can exploit correlations between dimensions, resulting in better
accuracy than univariate methods, which can only treat each di-
mension separately. However, multivariate methods require much
more time, as univariate methods can achieve high efficiency by
parallelizing each dimension. The test on Swat (51 dimensions)
shows that, the univariate method IDK costs 16.50s, while the mul-
tivariate method PBAD takes 125.17s, almost 10 times the time. On
the other hand, [28] implements the LSTM model on each dimen-
sion of the satellite dataset, since LSTMs have difficulty predicting
m-dimensional results accurately when m is large. Therefore, a
systematic inter-class comparisons should be performed to test the
possibility of using univariate methods on multivariate data.

2.2.2 Processing Techniques. A time series can also have an infinite
number of data points (stream). Methods that can handle infinite
time series are called online methods, while those that cannot are
called batch methods. The sliding window is the technique most
commonly used by online methods [57].

Scenario 2: Large Scale. Theoretically, batch methods have higher
accuracy because they can compare all data simultaneously. In con-
trast, online methods can run faster because they process only the
data points in the current window.On the one hand, online meth-
ods can continuously update their models for incremental anomaly
detection to account for the fact that time series characteristics
evolve over time [21, 44]. On the other hand, the efficiency gap,
especially for large datasets, should also be taken into account[40].
Therefore, like [44], we are interested in the extent to which online
methods approximate the performance of batch methods and what
the trade-off between effectiveness and efficiency is.

2.2.3 Anomaly Types. In a time series, data points that deviate
significantly from other observations are called point anomalies.
Subsequences of the time series with less similarity compared to
others are called as subsequence anomalies. The capability of a
method must be evaluated by an appropriate metric related to the
type of anomaly, otherwise misleading results may be obtained
[45, 53]. To compare methods in different cases, we further divide
point and subsequence anomalies into the following patterns [31].

Point Anomaly. Given a time series 𝑿 = {𝒙1, . . . , 𝒙𝑛 }. Let |𝒙𝑡 −
𝒙𝑡ˆ | > 𝛿, where 𝛿 is a threshold and 𝒙𝑡ˆ is the expected value. Global
anomaly indicates that 𝛿 ∼ 𝜎 (𝑿 ), where 𝜎 (𝑿 ) is the standard
deviation of the whole time series. Contextual anomaly with 𝛿 ∼

Figure 1: Facets and classes of anomaly detection algorithms

Figure 2: (a) time series and (b) online processing technique

select the optimal algorithm for specific anomaly types, such as
extremum anomalies. We also analyze real-world applications that
are more interested in positive, negative, and early detection cases,
and provide a practical guide for method selection.

The above papers investigate problems of time series anomaly
detection (TAD) from various aspects, but leave room for further
analysis. Theoretical surveys [5, 11, 14, 22] provide a structured
overview of research methods with different emphases. In contrast,
we consider the state-of-the-art methods not covered in these stud-
ies, perform a comprehensive analysis on wider ranges as shown
in Table 1, and obtain contributions as indicated in Section 1.1.

The original papers proposing anomaly detection algorithms
that we compare in our work [1, 3, 6, 7, 17, 19, 24–26, 39, 42, 50,
52, 55, 58, 66, 67] also consist of empirical comparisons. However,
these experiments are limited in terms of datasets, competitors, and
thorough analyzes of precision/recall, efficiency, and sensitivity
compared to our study. We use datasets from these works and
benchmarks from Numenta [34], Exathlon [29], and TODS [31].

2 PRELIMINARIES
2.1 Problem Definition
Anomaly detection in time series data can be defined as follows.

Definition 2.1 (Time series). A time series is a series of data points
indexed in time order. Consider a time series of 𝑛 observations, 𝑿 =
{𝒙1, . . . , 𝒙𝑛 }. The 𝑖-th observation (data point) 𝒙𝑖 ∈ R𝐷 consists
of 𝐷 dimensions {𝑥 1
𝑖 } and is observed at timestamp 𝑡𝑖 . A
subsequence 𝑿𝑖,ℓ = {𝒙𝑖, . . . , 𝒙ℓ−𝑖+1} is a subset of consecutive time
points from time series 𝑿 starting at position 𝑖 with length ℓ.

𝑖 , . . . , 𝑥 𝐷

Definition 2.2 (Anomaly Detection in Time Series). An anomaly
is an observation (or subset of observations) which appears to be
inconsistent with the remainder of that set of data [4]. Anomaly
detection in time series involves finding the abnormal data points
𝒙𝑖 or subsequences 𝑿𝑖,ℓ in the given time series.

485

---

<!-- PAGE 4 -->

Table 2: Anomaly detection methods considered here

e
c
n
a
t
s
i
D

n
r
e
t
t
a
P

Algorithm

NETS [66]
STARE [67]
NP [24]
MERLIN [42]

PBAD [19]
LRRDS [26]
SAND [7]
NormA [6]
GrammarViz [50]
IDK [55]
SHESD [25]

g BeatGAN [39]
n
i
n
r
a
e
L
p
e
e
D

Omni [52]
USAD [3]
GDN [17]
RCoder [1]
TranAD [58]

Mul
✓
✓
-
-
✓
✓
-
-
-
-
-
✓
✓
✓
✓
✓
✓

Process

Anomaly

online
online
batch
batch

batch
batch
online
batch
batch
batch
batch

batch
batch
batch
batch
batch
batch

point
point
subsequence
subsequence

subsequence
subsequence
subsequence
subsequence
subsequence
subsequence
point

subsequence
point
point
point
point
point

Threshold
𝜃𝑘
top-𝜃𝐾
top-𝜃𝐾
top-𝜃𝐾
top-𝜃𝐾
cluster
top-𝜃𝐾
top-𝜃𝐾
top-𝜃𝐾
top-𝜃𝐾
𝜃𝑘 , top-𝜃𝐾
top-𝜃𝐾
𝜃𝜏
𝜃𝜏
𝜃𝜏
𝜃𝜏
𝜃𝜏

Code

Speedup

JAVA
JAVA
python
matlab

python
r
C & python
C & python
JAVA
python
JAVA

python
python
python
python
python
python

-
-
1.5
60

2.5
1
0.3
-
-
20

-
-
-
-
-
-

𝜎 (𝑿𝑡 −𝑘,𝑡 +𝑘 ) denotes that the such anomaly point is different from
its neighbors in a specific range (window size 𝑘).

Subsequence Anomaly. Here, we assume that the subsequence
𝑋𝑖,𝑗 = 𝜌 (2𝜋𝜔𝑇𝑖,𝑗 ) + 𝜏 (𝑇𝑖,𝑗 ), where 𝜌, 𝜔 and 𝜏 represents the basic
shape, trend and seasonality, respectively. Global(shapelet) anomaly
refers to the subsequences with dissimilar basic shapes, which can
be defined as 𝑠 (𝜌, 𝜌ˆ ) > 𝛿, where 𝑠 is the similarity function [31].
Seasonal anomaly with 𝑠 (𝜔, 𝜔ˆ ) > 𝛿 means that those subsequences
have unusual seasonality compared to the whole series. Trend an-
omaly indicates the subsequences that significantly alter the trend
of the time series, leading to a permanent shift in the mean of the
data, which can be denoted as 𝑠 (𝜏, 𝜏ˆ) > 𝛿.

Scenario 3: Parameter relaxation. Nevertheless, it is difficult to
find a specific pattern of an anomaly in real datasets. Current sub-
sequence methods require the length of the target subsequence
as input [5–7]. However, it is rather difficult to determine such
a parameter without sufficient prior knowledge. In contrast, the
point methods do not require such additional input (the length is
1). Hence, we wonder (1) how powerful point methods are in the
presence of anomalies in subsequences; (2) how well the methods
can detect different patterns of anomalies.

Example 2.3. Point and subsequence anomalies can be univariate
or multivariate. Figure 2(a) shows two univariate point anomalies,
𝑂1 (global) and 𝑂5 (contextual). In terms of patterns, 𝑂3 is a trend
anomaly as it leads to a permanent shift with a lower mean, 𝑂2 is
a seasonal anomaly and 𝑂4, 𝑂6 are global anomalies. Data points
in univariate time series 𝑋 = {𝑥1, . . . , 𝑥6} are observed at time
1, 2, 3, 5, 7, 8 in Figure 2(b).Let us set the window size 𝜃𝑊 = 4, slide
size 𝜃𝑆 = 2. The online method will first process the data points
{𝑥1, . . . , 𝑥4} in the current window. After the processing, {𝑥1, 𝑥2}
in the first slide will be expired and {𝑥5, 𝑥6} in the new slide will
come in, forming a new window containing {𝑥3, . . . , 𝑥6}.

3 ALGORITHMS
Following the proposed taxonomy, we choose the latest represent-
atives for each class: 11/17 of these methods are published since
2020 and 12/17 are not compared in prior works in Section 1.2. We
will briefly introduce them in the class of detection techniques,
i.e., distance, pattern, and deep learning-based and extract their
critical factors. Table 2 lists the properties of each algorithm. The
‘threshold’ column indicates how the threshold for anomalies is set.

3.1 Distance-based Methods
Distance-based algorithms [57] in the literature can detect both
point and subsequence anomalies, but for simplicity we only refer
to point anomalies in the following definitions.

Definition 3.1 (Neighbor). Given a distance threshold 𝜃𝑅, a data
point 𝑥𝑖 is a neighbor of data point 𝑥 𝑗 (𝑥𝑖 ≠ 𝑥 𝑗 ) if the distance
𝑑 (𝑥𝑖, 𝑥 𝑗 ) ≤ 𝜃𝑅.

Definition 3.2 (Distance-based Outlier). Given a time series 𝑋 ,
a count threshold 𝜃𝑘 and a distance threshold 𝜃𝑅, distance-based
outliers are set of data points that have less than 𝜃𝑘 neighbors.

The key factors are the distance threshold 𝜃𝑅 and the count
threshold 𝜃𝑘 , determining the neighbors for each data point and the
anomalies. For online methods, the factors window size 𝜃𝑊 and the
slide size 𝜃𝑆 affect the performance and are usually set depending
on the size of the dataset. Distance methods for point anomalies
often focus on the scalability problem [57] and utilize different
structures to save running times. NETS [66] employs a set-based
approach following net effect, that data points in a short period of
time are likely to be concentrated in a set of small regions in the
data space. STARE [67] observes that data distributions in many
regions of the data space change little across window slides and
thus skips updating densities in local regions that do not change
significantly. NP [24] uses bagging to robustly discover frequent and
rare subsequences. A nearest neighbor ball technique that replaces
the nearest neighbor distance which is too small with the radius of
such a ball is proposed to provide a robust estimation and solve the
twin freak problem [24], which is not solved in matrix profile [65].
DRAG [64] creates a candidate discord set 𝐶 and then searches it for
a list of discords whose nearest neighbor distance is greater than a
hyper-parameter 𝑟 . MERLIN [42] provides a structured search to
set such 𝑟 . Since NETS and MERLIN dominates DRAG, respectively,
in almost all the datasets and hence we only report the former two
here.

3.2 Pattern-based Methods
The so-called pattern represents the regularities in the data, such
as an ordered set of data points that occur frequently in the data,
or a particular distribution. Pattern-based methods [14] are usu-
ally proposed to find subsequence anomalies, which we use in the
following definitions. Point anomalies can be found if the pattern
indicates a distribution.

Definition 3.3 (Pattern-based Outlier). Given a time series 𝑋 , an
anomaly length ℓ and a count threshold 𝜃𝐾 , pattern-based outliers
are the set of top-𝜃𝐾 subsequences with length ℓ and the lowest
similarity to the patterns extracted from 𝑋 .

The factors for pattern methods vary depending on how they
define patterns, support, and threshold for anomalies. In general, the
key factors are the support threshold 𝜃𝑠𝑢𝑝 , the anomaly threshold
𝜃𝜏 , or the count threshold 𝜃𝐾 , which represent the minimum occur-
rence of a pattern, the border of an anomaly, and the rank of scores
that an anomaly achieves, respectively.

ESD [48] computes the Extreme Studentized Deviate test stat-
istic to find anomaly points. SHESD [25] extends ESD by using

486

---

<!-- PAGE 5 -->

STL decomposition [13] and replacing the mean and standard de-
viation with more robust median and median absolute deviation.
Considering the seasonality, SHESD outperforms ESD and hence
we only report SHESD. NormA [6], SAND [7] and IDK [55] learn a
normal model (clustering the distribution of normal patterns) and
the similarity distance to the normal model is used as the anomaly
scores for target subsequences. SAND further extends the k-Shape
clustering [46] so that the normal model can be updated from one
batch to the next, making itself an online method. IDK uses Isol-
ation Distributional Kernel [56] to compute the similarity. PBAD
[19] and GrammarViz [50] use rules to extract the normal patterns.
The former presents frequent pattern mining research [68] to find
frequent patterns (whose support is greater than 𝜃𝑠𝑢𝑝 ) while the
latter implements two grammar induction methods [33, 43] to gen-
erate a context-free grammar. LRRDS [26] uses recurrence plot
[69] and extracts the subsequence set from the local recurrence
rates (LREC) [63]. The anomaly score is computed by comparing
similarities between statistics in the LREC curve.

3.3 Deep Learning-based Methods
Recently, several deep learning-based methods have been proposed
to detect anomalies in time series [15]. Various architectures have
been developed to capture latent information from temporal and
dimensional aspects.

For reconstruction based methods, after learning a model of the
normal data in the latent space, the test time series is first trans-
formed to the latent space and then reconstructed to the data space.
Finally, the reconstructed values that have a larger distance from
observations will be identified as anomalies. OmniAnomaly(Omni)
[52] proposes a stochastic recurrent neural network by using GRU
to capture complex temporal dependencies between multivariate
observations in data space, and a variational autoencoder (VAE)
to map observations to stochastic variables. USAD [3] presents an
encoder-decoder architecture within a two-phase adversarial train-
ing system (GAN). BeatGAN [39] also provides an interpretable
method that combines autoencoders and GAN to detect anom-
alous subsequences. RCoder [1] introduces an encoder-decoder
framework to learn the bounds of reconstructed signals. The key
difference is that its size of latent space is 1 and a spectral ana-
lysis with Fast Fourier Transform is then applied. TranAD [58]
combines transformer-based encoder-decoder networks with ad-
versarial training. Prediction base methods learn a model from nor-
mal data and then predicts the target value based on the model and
observations before the target time. Finally, the difference between
the predicted value and observation is used as the anomaly score.
GDN [17] employs the Graph Neural Network to learn the de-
pendency relationship between different dimensions and use graph
attention mechanism to make predictions.

3.4 Implementation Notes
Some widely used systems, such as Apache IoTDB [59], can only
support JAVA as built-in functions, and hence we rewrite all non-
deep learning methods in JAVA (except NormA, the existing toolkit
runs differently). We also refactor NETS, STARE, GrammarViz, and
SHESD (in JAVA) and deep learning methods (in Python) with our
data structures to avoid potential impact on efficiency. We remove

Table 3: Real-world and synthetic datasets summary

t
n
i
o
P

e
c
n
e
u
q
e
s
b
u
S

Real-world

Yahoo [35]
Twitter [25]
Stock [57]
Tao [57]
SMTP [38]
DLR [67]
ECG [67]

Power [30]
Sed [7]
Taxi [53]
Machine [53]
Exercise [19]
Exathlon [29]
Swat [41]
Smd [52]

Synthetic

Size
1.5k
14k
10k
568k
95k
23k
112k

35k
100k
10k
22k
10k
3k
90k
28k

Size

#Dim Rate%

Pattern

Avg Length

1
1
1
3
3
9
32

1
1
1
1
3
19
51
38

0.7
0.7
5 - 25
5 - 25
0.03
2.2
16.3

8.6
3.0
10
10
15.1
17.4
12
9.5

Contextual
Global
Mixed
Mixed
Mixed
Contextual
Global

Seasonal
Global
Global+Seasonal
Global+Seasonal
Mixed
Mixed
Mixed
Mixed

-
-
-
-
-
-
-

750
64
207
567
140.2
64.1
317.2
336.8

#Dim Rate%

Pattern

Avg Length

t Uni-point-g
n
Uni-point-c
Mul-point

i
o
P

e
c
n
e
u
q
e
s
b
u
S

Uni-sub-g
Uni-sub-s
Uni-sub-t
Mul-sub-g
Mul-sub-s
Mul-cor-g
Mul-ncor-g

1k-100k
1k
1k-100k

1k-100k
1k-100k
1k-100k
1k-100k
1k-100k
5k
5k

1
1
32

1
1
1
3/50
3/50
3
3

5 - 25
5 - 25
5 - 25

5 - 25
5 - 25
5 - 25
5 - 25
5 - 25
10
10

Global
Contextual
Global

Global
Seasonal
Trend
Global
Seasonal
Global
Global

-
-
-

50
50
50
50
50
50
50

POT [51] (selecting threshold automatically) and point-adjust [62]
(modifying predictions before evaluation) to make a fair compar-
ison. Analysis on these changes can be found in Section 4.3.4 and
4.3.5, respectively. The ’Code’ column in Table 2 shows the original
language in which each method was written, while the ‘Speedup’
column shows the increase in efficiency after our implementation
(except SAND, the decomposition tools runs far more slowly). We
verify that the reported anomalies of the methods before and after
our refactor are identical and guarantee reproducibility.

4 EXPERIMENT
This section will first show the experimental settings. Then, insights
found over intra-class and inter-class comparisons are explained.
Similar to [49], we try our best to describe findings from experi-
mental results. However, if a method performs poorly in our evalu-
ation, it does not necessarily mean that its theory is bad, because
the metric and the situation are quite different.

4.1 Settings
We run experiments on a Windows 10 server with a 3.79GHz 12
Core CPU and 128GB RAM. Deep-learning methods are employed
with GPU without comparing the efficiency. Others are tested under
a single-core environment to compare running times.

4.1.1 Datasets. We employ widely used real-world datasets with
labels as benchmarks, 7 with point and 8 with subsequence anom-
alies with various sizes, dimensions, anomaly rates (lengths) and
patterns. We also generate synthetic datasets whose base type is
sine, with different anomaly patterns (See Section 2.2.3) according
to the guideline in [31] for the case of the unreliability of anomaly
labels [61]. For point anomaly, we inject global(g) and contextual(c)
outliers. For subsequence anomaly, we add global(g), seasonal(s)
and trend(t) outliers, respectively. The average length is set to 50 by
default, so any algorithm is applicable. In order to avoid the effect
of randomness, we run experiments on synthetic datasets 10 times

487

---

<!-- PAGE 6 -->

Figure 3: Time cost over various datasets

with different generating seeds and report the average results. The
summary of all datasets can be found in Table 3.

4.1.2 Evaluation Metrics.

𝑇 𝑃

𝑇 𝑃 +𝐹 𝑃 and 𝑅𝑒𝑐𝑎𝑙𝑙 =

Accuracy. Different metrics are used with respect to anomaly
types. 𝑃𝑟𝑒𝑐𝑖𝑠𝑖𝑜𝑛 = 𝑇 𝑃
𝑇 𝑃 +𝐹 𝑁 [2] are utilized as
point metrics, where TP, FP, FN are the number of true positives,
false positives, and false negatives, respectively. We choose a re-
cent metric proposed for subsequence anomaly which focuses on
the overlap of predicted anomaly and true anomaly [53] as range
(or subsequence) metric. Specifically, given a set of real anomaly
ranges 𝑅 = {𝑅1, . . . , 𝑅𝑁𝑟 } and a set of predicted anomaly ranges
𝑃 = {𝑃1, . . . , 𝑃𝑁𝑝 }, we have 𝑅𝑒𝑐𝑎𝑙𝑙𝑇 (𝑅, 𝑃) =
∑︁𝑁𝑝
𝑖=1

𝑃𝑟𝑒𝑐𝑖𝑠𝑖𝑜𝑛𝑇 (𝑅, 𝑃) =
. In general, the default set-
ting Flat bias [53] is employed. 𝐹 − 𝑚𝑒𝑎𝑠𝑢𝑟𝑒 = 2∗𝑃𝑟𝑒𝑐𝑖𝑠𝑖𝑜𝑛∗𝑅𝑒𝑐𝑎𝑙𝑙
𝑃𝑟𝑒𝑐𝑖𝑠𝑖𝑜𝑛+𝑅𝑒𝑐𝑎𝑙𝑙
applies for both metrics.

𝑃𝑟𝑒𝑐𝑖𝑠𝑖𝑜𝑛𝑇 (𝑅,𝑃𝑖 )

𝑅𝑒𝑐𝑎𝑙𝑙𝑇 (𝑅𝑖,𝑃 )

∑︁𝑁𝑟
𝑖=1

and

𝑁𝑝

𝑁𝑟

Efficiency. Apart from loading the data from the file and result
evaluation, the total time of all the other procedures will be added
and reported as the time cost of the target method.

4.1.3 Parameter Search. In order to compare methods fairly and
precisely (under best configurations), though all of them are unsu-
pervised methods, we still employ a systematic (hyper)-parameter
search process. Specifically, we design a search space for each para-
meter (including threshold) according to the suggestions in their
paper, e.g., for USAD we tune the latent size with {2, 5, 10, 20} [3]
or based on the distributions of the target dataset. We then split
the dataset into training, validation and test set with a ‘4:1:5’ ra-
tio. It’s worth noting that the training sets are anomaly-free, as
required by [3, 17, 52, 58]. The parameter with the best performance
in validation set will be settled for testing.

4.2 Intra-class Comparisons
As mentioned earlier, articles presenting new methods often include
such comparisons, but the variety of cases with respect to factors
and datasets is often limited. For simplicity, we use "Point" to
denote the results of point methods and "Sub" of subsequence
methods. "Summary" stands for the take-away conclusions.

4.2.1 Varying Datasets. We first evaluate the performance of all
methods on different datasets with their best parameters. To obtain
the results of the univariate methods on multivariate data, we run
them separately on each dimension (similar to [52]), and combine
all the reported anomalies. Results are shown in Table 4.

488

Figure 4: Varying rates on (a-b) Uni-point-g (c-d) Tao

Point. We can see that NETS always have high accuracy across
all datasets. Stare relies heavily on the parameter indicating the
number of anomaly points in each window. Complex distributions
of real anomalies results in its relatively lower accuracy. As for
deep learning methods, all except RCoder are close to NETS on
Yahoo and perform worse on others. RCoder, which cannot be
used for univariate data due to its mechanism, performs best on
ECG with 32 dimensions but poorly on others whose dimensions
are smaller than nine. Overall, it is surprising that deep learning
methods do not behave well. The possible reason is that the number
of data instances and dimensions are not sufficient to learn a good
model. Figure 3(a) shows the efficiency of each method. We only
show the first 4 datasets, since others are similar. NETS computes
on a selected sub-dimension, making it the most efficient method.
TranAD shows the best time efficiency due to its architecture.
Sub. Multivariate methods PBAD and BeatGAN achieve higher
accuracy than univariate methods on multivariate data. In partic-
ular, univariate methods have high recall but very low precision.
LRRDS performs better than PBAD and BeatGAN only on Sed. This
is because the mean of abnormal patterns in Sed is obviously lower
than that of normal patterns, so LRRDS is easier to identify with
embedding techniques than simple mean and length features. As for
univariate methods, NormA can perform quite well on all univariate
data. MERLIN performs exceptionally well on Power, showing the
capability over seasonality. SAND does not perform well on long
anomalies (e.g., the length of the anomaly in Power is 750). It has to
decompose a large matrix many times if the anomaly has a large
length. We note that it takes much more time when the length of
the anomaly is greater than 100. Both GrammarViz and PBAD use
a pattern mining approach to identify sequence patterns, so they
are comparable on univariate datasets.
Summary. (1) There is no super-algorithm that is suitable for all
cases. (2) Given proper parameters, NETS can perform best in most
cases. (3) PBAD and BeatGAN have better overall accuracy but cost
more time. (4) Deep learning methods do not outperform others on
datasets with complex anomaly patterns.

---

<!-- PAGE 7 -->

Table 4: Accuracy over various datasets

Dataset

Yahoo
Twitter

SMTP
DLR
ECG

Dataset

Power
Sed
Taxi
Machine

Exercise
Exathlon
Swat
Smd

NETS
R

1
0.878

0.375
0.424
0.441

PBAD
R

0.758
0.800
0.664
0.500

1
0.856
0.566
0.303

P

0.727
0.739

0.400
0.468
0.484

P

0.262
0.310
0.143
0.227

0.495
0.515
0.185
0.294

F

P

0.842
0.802

0.387
0.445
0.462

0.429
0.203

0.294
0.109
0.239

Stare
R

0.375
0.959

0.313
0.517
0.267

F

P

SHESD
R

F

P

TranAD
R

F

P

0.400
0.335

0.303
0.179
0.252

1
0.260

0.001
0.061
0.373

0.625
0.176

1
1
0.430

0.769
0.210

0.003
0.115
0.399

0.368
0.737

0.001
0.115
0.160

0.875
0.189

0.188
0.224
0.557

0.519
0.301

0.003
0.152
0.248

0.368
0.205

0.001
0.115
0.280

USAD
R

0.875
0.412

0.222
0.224
0.293

F

P

0.518
0.274

0.002
0.154
0.286

0.368
0.484

0.004
0.118
0.232

GDN
R

0.875
0.419

0.022
0.852
0.328

F

P

0.519
0.449

0.007
0.060
0.272

0.471
0.079

0.250
0.180
0.347

Omni
R

1
0.878

0.375
0.180
0.165

F

0.64
0.145

0.300
0.180
0.224

RCoder
R

-
-

F

-
-

P

-
-

0.001
0.030
0.640

0.312
0.252
0.426

0.001
0.053
0.512

F

P

LRRDS
R

F

P

BeatGAN
R

F

0.389
0.446
0.235
0.312

0.662
0.643
0.279
0.298

0.415
0.597
0.164
0.073

0.283
0.197
0.286
0.676

0.248
0.972
0.463
0.500

0.656
0.341
0.124
0.098

0.310
0.739
0.242
0.127

0.396
0.250
0.173
0.171

0.498
0.690
0.354
0.521

0.756
0.299
0.340
0.273

0.340
0.723
0.437
0.471

0.760
0.694
0.233
0.235

0.404
0.706
0.391
0.495

0.758
0.418
0.276
0.253

SAND
R

0.156
0.769
0.242
0.106

0.672
1
0.993
0.925

P

0.159
0.657
0.250
0.100

0.293
0.206
0.082
0.070

F

P

0.157
0.708
0.246
0.103

0.408
0.341
0.151
0.129

0.575
0.695
0.468
0.009

0.309
0.149
0.055
0.082

NP
R

0.575
0.814
0.498
0.018

0.983
0.993
1
0.980

F

P

MERLIN
R

F

GrammarViz
R

F

P

0.575
0.750
0.482
0.012

0.470
0.259
0.104
0.151

0.936
0.505
0.460
0.143

0.377
0.200
-
0.063

0.998
0.829
0.460
0.429

0.971
1
-
0.732

0.966
0.627
0.460
0.215

0.543
0.334
-
0.116

0.453
0.435
0.333
0.197

0.553
0.147
0.137
0.018

0.222
0.533
0.135
1

0.745
1
1
1

0.298
0.479
0.192
0.33

0.635
0.256
0.242
0.035

NormA
R

F

P

0.810
0.669
0.533
0.332

0.743
0.849
0.529
0.742

0.838
0.527
0.482
0.226

0.420
0.170
0.113
0.157

0.343
0.938
0.498
0.429

0.171
0.169
0.041
0.085

P

0.868
0.435
0.441
0.171

0.292
0.095
0.063
0.088

IDK
R

0.244
0.938
0.373
0.454

0.405
1
1
0.799

F

0.285
0.938
0.427
0.441

0.245
0.289
0.079
0.154

Figure 5: Varying rates on (a-b) Uni-sub-g (c-d) Mul-sub-s

Figure 6: Varying sizes on (a-b) Uni-point-g (c-d) Tao

4.2.2 Varying Anomaly Rate 𝑎%. [61] claims that current datasets
contain too few anomalies for even a simple method to find them.
However, the majority of the data should be normal. Therefore, we
vary anomaly rates from 5% to 25% to test the sensitivity of the
methods on synthetic datasets. The data size is 10k for point and
5k for subsequence anomalies.
Point. As illustrated in Figures 4(a, c), all non-deep learning meth-
ods are relatively stable. NETS perform a bit worse on Tao when the
anomaly rate achieves 25%. Since it is difficult to set an appropriate
𝜃𝑘 and 𝜃𝑅 to identify the anomalous points because they also have
a similar number of neighbors as normal points. On the contrary,
most deep learning methods achieve a better result with increasing
anomaly rate. This may be because TranAD, USAD, and GDN fail to
learn a good model (even with the best parameter via grid search)
and tend to predict more points as anomalies. Therefore, more false
positives become true positives when the anomaly rate increases.
Omini and RCoder manage to learn a better model and perform
well on Uni-point-g and Tao, respectively.
Sub. Figures 5(b, d) show that, the time costs of all methods re-
main constant for both univariate and multivariate data, except
for MERLIN and GrammarViz, which is due to the fact that the

time complexity of MERLIN and GrammarViz is linearly related
to the number of anomalous subsequences. When we compare the
results of the different methods, we find that most of them, such as
PBAD, remain stable or perform better when the anomaly rate is
lower, but gradually become worse as the anomaly rate increases.
In contrast, LRRDS and BeatGAN performs even better at a higher
anomaly rate, which is due to the reduction of false positives caused
by rough recognition of anomaly point.
Summary. (1) Methods are stable when anomaly is rare (< 25%),
which is different to the statements about random detection in [44].
(2) A method may perform better as anomaly rate increases since
the large number of the reported false positives can become true
positives. (3) Anomaly rate shows little effect on the efficiency.

4.2.3 Varying Data Size 𝑛. To check the sensitivity and scalability
against the data size, we run experiments by varying data sizes
from 1k to 100k on real and synthetic datasets with 10% anomalies.
Point. The results in Figures 6(b, d) show that all methods cost
more time as the data size increases. In terms of accuracy, they
show consistent results against the data size. It is noted that SHESD
makes exceptions in some cases. Stare and NETS are the two fastest

489

---

<!-- PAGE 8 -->

Figure 7: Varying sizes on (a-b) Uni-sub-g (c-d) Mul-sub-s

Figure 9: Varying patterns on (a-b) point (c-d) subsequence

Figure 10: Critical difference diagram on subg

4.2.4 Varying Data Dimension |𝐷 |. Here we perform experiments
on real datasets by varying the dimensions of the data.
Point. Figures 8(a-b) show that all methods have better results with
larger dimensions. Besides, we need to adjust the parameter 𝜃𝑅 with
the change in dimension to get a reasonable result. We also retrain
the models of the deep learning methods, which results in all but
RCoder remaining stable as the data dimension increases. RCoder
has more reference data and estimators with more data dimensions,
which significantly increases its accuracy. In terms of efficiency, all
distance-based methods cost more time as the dimension increases,
since it is more expensive to compute the distance.
Sub. The result of the subsequence anomaly can be checked in
Figure 8(c-d). LRRDS applies dimensional compression and exhibits
great scalability. In contrast, PBAD must extract the features in each
dimension, which results in a significantly higher time overhead as
the dimension increases. Since the anomaly is localized differently
in each dimension of Swat, it is not surprising that performance
varies widely across all methods, including BeatGAN.
Summary. (1)LRRDS scales well with data dimension, while NETS,
Stare, and PBAD are significantly affected by it. (2) The sparsity
problem can be handled by a good parameter setting. (3) Since the
number of estimators increases with the data dimension, RCoder
achieves better results with higher dimensions. (4) NETS is recom-
mended when data dimension is limited (< 30). (5) RCoder is a good
choice when data dimension is large (> 30).

4.2.5 Varying Anomaly Patterns. Finally, we test the selected al-
gorithms for different patterns of anomalies.
Point. As shown in Figures 9(a-b), all methods achieve better ac-
curacy for global anomaly (0.618) than contextual anomaly (0.551),

Figure 8: Varying dimensions on (a-b) ECG (c-d) Swat

methods. The latter two algorithms take advantage of the “set effect"
that skips additional updates when new data arrives.
Sub. As can be seen in Figure 7, most pattern-based methods show
unstable results for small (e.g., 5k) because it is difficult to extract
patterns. When the data is large enough, the results of the sub-
sequence methods are usually quite consistent. LRRDS reflects the
same trend in Section 4.2.2. We do not report the results of LRRDS
after 20k because it is out of memory and do not report the results
of MERLIN after 10k because it takes more than a day to run. Both
of them show poor scalability.
Summary. (1) Stare, NETS, and NormA have good efficiency (also
referred to the results in Figure 3). (2) Small data size (< 10k) may
lead to unstable results for subsequence methods. (3) We recom-
mend IDK when the data size is more than 50k because it provides
good scalability and stable performance.

490

---

<!-- PAGE 9 -->

which is consistent with the common sense. They have similar
efficiency for these two anomaly patterns.
Sub. The result for the subsequence case is shown in Figures 9(c-d).
The average f-measures are 0.550, 0.619, and 0.398 for global, sea-
sonal, and trend anomaly, respectively. Consistent with previous
observations, PBAD and NormA has stable performance across all
patterns. SAND and NP perform particularly well on global and sea-
sonal outliers. Detecting trend outliers is challenging for BeatGAN
and IDK, reflecting the need for improvement of non-stationary
time series. To find out whether there are methods that fit all pat-
terns, we apply the Friedman test [20] and a post-hoc Wilcoxon
test [60] (with 𝛼 = 0.05) to the f-measures for different anomaly pat-
terns. First, the Friedman tests yield a p-value greater than 0.05 and
thus do not indicate that these methods are significantly different.
Figure 10 shows the critical difference diagram[16] for the global
anomaly as an example. Methods that are not connected by a bold
line differ significantly in their average ranks. This proves that for
a single anomaly pattern there is a particular method that clearly
outperforms the others. For example, NP not only achieves first
place for global outliers, but also significantly outperforms others.
Summary. (1) In point methods, global anomalies are easier to
detect than contextual ones. (2) In subsequence methods, seasonal
anomalies are easiest to find, while trend anomalies are hardest
to find. (3) No one method fits all patterns. But certain methods
are clearly better than others for a particular anomaly pattern, e.g.,
NP performs best for the global anomaly. (4) SAND and IDK are
not suitable for non-stationary time series (with trend anomaly).
(5) Distance-based methods are well suited for global and seasonal
anomalies. (6) IDK can also work well for global anomaly, which is
different from RI(8) in [49].

4.3 Inter-class Comparisons
In this section, we will test the performance of methods between
different classes under the same facet. In the data dimension facet,
we run univariate methods separately for each dimension of the
multivariate data and then combine the results. In the processing
technique facet, we run online methods across different window and
slide sizes on datasets larger than 100k and with dimensions larger
than 30. In the anomaly type facet, as mentioned in Section 1, we run
both point and subsequence methods on datasets with subsequence
anomalies under different evaluation metrics to analyze the impact
of the metrics and the adjustment in predictions. In addition, we
also test the impact of thresholds and performance under different
application aspects.

Table 5: Performance on single dimension and combination

Dataset

Exercise
Combination
E_A1
E_A2
E_A3

Mul_ncor_g
Combination
M_A1
M_A2
M_A3

P

0.495
0.220
0.357
0.389
0.352

0.684
0.097
0.092
0.083
0.107

PBAD
R

F

P

BeatGAN
R

F

SAND
R

P

F

P

1
1
1
1
0.719

1
1
0.300
0.390
0.402

0.662
0.360
0.526
0.560
0.473

0.813
0.178
0.140
0.137
0.168

0.756
0.332
0.708
0.505
0.249

0.514
0.215
0.219
0.222
0.223

0.760
0.997
0.72
0.498
0.248

0.753
0.861
0.246
0.355
0.358

0.758
0.498
0.714
0.501
0.248

0.611
0.344
0.232
0.273
0.275

0.293
0.483
0.27
0.192

0.250
0.315
0.261
0.311

0.672
0.513
0.275
0.204

0.897
0.329
0.353
0.42

0.408
0.498
0.272
0.197

0.391
0.322
0.300
0.357

0.309
0.894
0.222
0.196

0.279
0.377
0.245
0.217

NP
R

0.983
0.943
0.224
0.202

0.941
0.463
0.368
0.325

F

0.47
0.918
0.223
0.199

0.431
0.416
0.294
0.260

Figure 11: Varying (a-b) window sizes (c-d) slide sizes on ECG

4.3.1 Univariate Methods in Multivariate Datasets. As reported in
Section 4.2.1, the point method SHESD lags far behind multivariate
ones, therefore, we focus on the subsequence case.
Settings. If the detected anomalies in different dimensions overlap
after combination, we merge them into a large range(subsequence)
as the final result. Following the same logic, we also run multivariate
methods (PBAD and BeatGAN) for each dimension separately and
combine the detected anomalies for direct comparison, the results
of which are displayed in the ‘Combination’ column in Table 5.
We note that anomalies in Exercise (similar results are observed
in other real datasets) always occur in all dimensions at the same
position. Therefore, we test the effects of such ‘overlap’ on another
synthetic data. The ‘ncor’ indicates that positions of the generated
anomalies are different in each dimension. ‘A1-A3’ denote the three
dimensions.
Results. Compared with the results on each dimension and after
combination, most of the methods have a promotion on recall but
a sharp reduction on precision, since the aggregation in each di-
mension will involve in more predicted anomalies (cover more real
anomalies but also much more false positives). Compared with
combined results on the synthetic data, we find out that anomaly
positions (co-occur or not) do not clearly impact the effectiveness
and efficiency. Univariate methods can achieve good results on
some specific dimensions but acts poorly overall, while multivariate
ones perform the opposite, showing the advantage of considering
relationships over dimensions.
Summary. Promotion on efficiency cannot compensate for the
sharp drop in accuracy (we omit efficiency results and show one in
motivating scenario 1). Multivariate methods are better, unless we
have sufficient prior knowledge about specific dimensions.

4.3.2 Online Methods in Batched Time Series. As explained in Sec-
tion 4.2.1, the online method SAND suffers from the iterations of
eigenvalue decompositions and its efficiency is significantly af-
fected. Thus, we focus on the point case.
Settings. We run two experiments in ECG varying window sizes
𝜃𝑊 and slide sizes 𝜃𝑆 . Similar results are observed in other datasets.
𝜃𝑆 = 150 in the first case and 𝜃𝑊 = 3𝑘 in the second. It should be

491

---

<!-- PAGE 10 -->

Figure 12: Varying lengths on (a-b) Uni-sub-g (c-d) Uni-sub-s

noted that 𝜃𝑆 ≤ 𝜃𝑊 always holds. The batch method SHESD is
used as a baseline.
Results. Figure 11(a) shows that the accuracy of NETS first in-
creases and then decreases with increasing window size. The reason
is that if the window size is too small, it is difficult to find enough
neighbors even for a normal data point, leading to false positives.
If the window size is too large, the number of neighbors for a local
anomaly point may exceed the predefined threshold 𝜃𝑘 , leading to
false negatives. As can be seen in Figure 11(b), as expected, a lar-
ger window size causes the methods to consume more data points,
which costs more time. One possible explanation for Figure 11(c) is
that a larger slide size increases the variation in the number of an-
omaly points, which decreases the accuracy of Stare. On the other
hand, if the slide size is too large, the intermediate information
stored for NETS changes too much, which also negatively affects
the accuracy. Regarding the efficiency shown in Figure 11(d), Stare
take less time as the slide size increases. NETS cannot exploit the
‘net effect’ when the slide size is equal to the window size. There-
fore, it can take the least time for a medium 𝜃𝑆 . It is noted that even
the fastest online method NETS will be ten times slower than the
simple batch method SHESD when 𝜃𝑊 = 10𝑘.
Summary. (1) Larger sizes do not necessarily produce better res-
ults, but cost more time. (2) Online methods can outperform batch
methods under a proper setting, due to the evolvement character-
istic of time series.

4.3.3 Point Methods in Subsequence Anomalies. Subsequence meth-
ods always consider the anomaly length ℓ as an input parameter [7].
However, this affects accuracy to some extent, since subsequence
anomalies in real time series data rarely have a fixed length. In con-
trast, point anomaly methods require no such input (the length is 1).
Therefore, we would like to know the effect of anomaly length and
whether we can perform point methods for subsequence anomalies.
Settings. We use univariate data with injected global and seasonal
anomalies to avoid the effect of dimensions. We omit trend because
they have similar results to seasonal. For brevity, we report only
NETS and TranAD, as other point methods perform similarly.

Figure 13: Case study on (a) Uni-sub-g (b) Uni-sub-s

Figure 14: Point-adjust method

Results. Figure 12 shows the sensitivity of the methods to the
anomaly length ℓ. PBAD does not identify the subsequence whose
length is exactly ℓ, making it different from others. Other methods
claim to achieve the best accuracy when ℓ is similar to the actual
length (ℓ = 50) of the anomalies, which can be seen in Figures 12(a,
c). IDK demonstrates robustness for the input length, while the best
input length at NormA is difficult to predict. It is interesting that
NETS under global patterns (in Figure 12(a)) can also give good
results with much less time (in Figure 12(b)). In Figure 13(a), we
zoom in on 400 data points in the Uni-sub-g dataset and highlight
the actual anomaly in green, while the anomaly identified by the
different methods is highlighted in red. We find out that PBAD
and SAND can cover the whole anomaly subsequence. NETS is
also able to match some true anomaly (on the right), while the
subsequence methods usually have a lag in the result. We perform
another experiment with Uni-sub-s and find similar results for the
subsequence methods in terms of length ℓ. However, point methods
can not give accurate results in such complex cases (in Figure 12(c)).
Combining these two observations, we argue that point methods
facilitate the detection of some global outliers, while anomalous
patterns requiring long-term context are hard to detect.
Summary. (1) Point methods can also work well for global sub-
sequence anomalies with extreme values, which may help relax
the length input requirement. (2) The length parameter ℓ, which
is close to the actual anomaly length, gives good results. Adaptive
input length are needed to deal with real-world situations.

4.3.4 Effect of Metrics and Adjustment. Using point metrics for
datasets with subsequence anomaly will bias the accuracy of many
time series anomaly detection systems by not capturing specific
properties [53]. For a real-time application, it might be more im-
portant to detect the earlier part of an anomaly to reduce response

492

---

<!-- PAGE 11 -->

Table 6: F-measure w/o point-adjust under different metrics

Algorithm

TranAD
TranAD∗
USAD
USAD∗
Omni
Omni∗
RCoder
RCoder∗
GDN
GDN∗

NETS
NETS∗
Stare
Stare∗
SHESD
SHESD∗

Point Metric

Range Metric

Twitter

ECG inc/alg

Exathlon Uni-sub-g

inc/alg

Exathlon Uni-sub-g

inc/alg

0.455
0.466
0.274
0.289
0.138
0.166
-
-
0.449
0.460

0.802
0.852
0.334
0.334
0.209
0.510

0.224
0.397
0.286
0.448
0.318
0.483
0.441
0.631
0.274
0.410

0.461
0.666
0.252
0.589
0.339
0.488

39.7%

31.0%

36.4%

43.0%

26.9%

25.3%

66.6%

82.8%

0.245
0.246
0.246
0.246
0.245
0.246
-
-
0.238
0.246

0.286
0.754
0.253
0.312
0.257
0.776

18.5%

0.299
0.414
0.330
0.452
0.267
0.553
-
-
0.267
0.554

0.942
1
0.653
0.725
0.978
1

12.5%

6.1%

6.1%

14.3%

-

14.7%

42.8%

14.5%

43.8%

0.484
0.246
0.245
0.245
0.409
0.246
-
-
0.851
0.246

0.217
0.080
0.189
0.018
0.227
0.090

0.345
0.039
0.365
0.038
0.240
0.079
-
-
0.239
0.079

0.942
1
0.438
0.090
0.979
1

-68.9%

-44.8%

-53.5%

-

-69.1%

-28.5%

-85.0%

-29.0%

-53.4%

-54.8%

inc/data

23.1%

58.3%

time [32]. Therefore, the overlap of predicted anomalies and ac-
tual anomalies should be addressed. To deal with interpretations of
such overlaps and the problem of label imbalance, some methods
[3, 52, 58] use a point-adjust method [62] that converts false negat-
ives to true positives. As shown in Figure 14, for each point in the
anomaly segment of the ground truth, if it is detected as an anom-
aly by the proposed algorithm, all observations in the subsequence
will be considered to have been correctly detected as anomalies.
Therefore, such a method ignores latency and reports much higher
accuracy than it actually is. RCoder proposes a different way to
adjust predictions [1]. However, we focus on analyzing the more
widely used point-adjust method in this work.
Settings. We conduct experiments with both point (Twitter, ECG)
and subsequence datasets (Exathlon, Uni-sub-g). The results of point
datasets are evaluated by the point metric and the results of sub-
sequence datasets are evaluated by both point and range metrics.
Results with the point-adjust method are denoted by ∗.
Results. Table 6 shows the f-measure in different cases. ‘inc/alg’
gives the average promotion after applying point-adjust method
per method and ‘inc/data’ shows this promotion per data. Point-
adjust method can have a great impact on the evaluation as follows:
(1) Overall, the algorithm will have an average promotion of 27.0%
for point datasets and a higher promotion of 31.2% for subsequence
datasets under point metrics. (2) For subsequence datasets with
range metrics, the algorithms have an average negative promotion
of −67.6%. (3) TranAD and Omni have a higher f-measure (0.245)
than GDN (0.238) under the point metric, but GDN performs far
better (0.851) than TranAD (0.484) and Omni (0.409) on Exathlon
under range metric. (4) Stare has a higher f-measure (0.334) than
SHESD (0.209), but after the adjustment, SHESD will perform better
(0.510) than Stare (0.334) on Twitter. Such inversions can confuse an-
omaly detection systems and influence user preferences in selecting
appropriate methods..
Summary. (1) point-adjust method tends to report ‘false’ higher
results for algorithms and can lead to misleading analyzes. (2) The
use of range metrics on datasets with subsequence anomalies is
preferable as it leads to more reasonable and robust results.

4.3.5 Effect of Threshold. Threshold is a key hyper-parameter for
anomaly detection problems whose effect has seldom been dis-
cussed in existing works, as stated in Section 1.2. We will test the

Figure 15: Varying thresholds on (a-b) ECG (c-d) Uni-sub-g

Table 7: F-measure w/o POT method

Data Set TranAD TranAD-P USAD USAD-P Omni Omni-P GDN GDN-P

ECG
DLR
TAO
UNI

0.248
0.152
0.181
0.179

0.350
0.007
0.181
0.182

0.286
0.154
0.180
0.158

0.338
0.070
0.181
0.182

0.224
0.065
0.181
0.660

0.345
0.070
0.181
0.181

0.271
0.060
0.012
0.181

0.353
0.069
0.181
0.183

robustness of each algorithm w.r.t. threshold and the impact of the
POT [51] method for automatic threshold selection.
Settings. We unify the threshold setting for all methods in the
following way: let the threshold be the ratio of points/sequences
identified as anomalies. 0% means all are normal, while 100% means
all are anomalies. However, NETS , Stare, and SHESD have different
logic in identifying anomalies (more than one factor is considered),
so we report only other methods in this part. The overall perform-
ance is the area included by the recall and precision curves. Besides,
the results of using POT method are presented in Table 7.
Results. Figure 15(c, d) show the results on Uni-sub-g. We note
that NP, despite having a better best F-measure than NormA, drops
sharply as the threshold approaches 20%. In contrast, NormA shows
better robustness as the curve is smoother. It is interesting to note
that IDK performs best in this experiment, but does not outperform
in Figure 9. The reason for this is that in all other experiments
we perform a grid search on the validation set to find the proper
(hyper)-parameters, but there is a small difference between the
validation set and the test set. As for the point methods shown in
Figures 15(a, b), RCoder shows the overall best performance among
all the deep learning methods, while Omni shows better robustness.
In terms of the impact of POT method, GDN always have a better
result after using it. Other methods show different preferences on
different datasets. In around 55% cases, POT can achieve similar or
slightly better results than grid search on validation set.
Summary. (1) Automatic threshold selection methods can still be
improved to take effect in practical uses. (2) IDK has the best overall

493

---

<!-- PAGE 12 -->

Figure 16: FPR and FNR on real datasets

Figure 18: A practical guide for timeseries anomaly detec-
tion

Figure 17: Early detection under Front metric

performance, while NormA is more robust, specifically when the
threshold is above 20%. (3) RCoder has the best overall performance,
while Omni is more robust.

4.3.6 Application. In this section, we focus on anomaly detection
in real-world applications. Scenario 1: Some applications are more
interested in positive outcomes, such as cancer detection, where
we do not want cancer patients to go undetected. Others are more
interested in negative outcomes, such as when we do not want a
good email to become spam. Scenario 2: In the previous study, we
assumed that all positions of an outlier range are equally important.
Therefore, larger overlaps lead to a higher score of the metric. How-
ever, in practice, there are many situations where early response is
critical, e.g., cancer detection or real-time systems.
Settings. We employ experiments on all real datasets with point
𝐹 𝑃
and subsequence methods for Scenario 1, where 𝐹 𝑃𝑅 =
𝑇 𝑁 +𝐹 𝑃 ,
𝐹 𝑁 𝑅 = 𝐹 𝑁
𝑇 𝑃 +𝐹 𝑁 . Scenario 2 is particularly suitable for subsequence
methods. Flat denotes the metric with the same score for all posi-
tions, while Front assigns more weight to the early positions of the
subsequence anomaly [53].
Results. All algorithms generally have a higher false negative rate
and a lower false positive rate, as can be seen in Figure 16. This
suggests that they are more suitable for negative applications (not
reporting false anomalies) and are more capable of detecting normal
samples than abnormal samples. In particular, NETS and Omni have
low FPR and are recommended for negative cases such as spam de-
tection. On the other hand, TranAD and RCoder are recommended
for positive applications since they manage to report all anomalies.
Similarly, PBAD is more suitable than BeatGAN for such cases due
to its lower FNR.

Figure 17(a) shows the performance of the algorithms under Flat
and Front metrics on Power. (Similar results are observed on other
real-world datasets.) BeatGAN has a higher f-measure than PBAD
under the Flat metric, but achieves a lower score when the Front
metric is used, indicating that it is not suitable for early detection.

We see similar results in Figure 17(b), where the average compar-
ison is tested over all real datasets. BeatGAN scores a 49% drop
compared to its performance under the Flat metric, showing that it
captures outliers with latency. NP appears to be the best performing
algorithm for early detection, with a performance improvement of
10.99%.
Summary. (1) Specific metrics are required for different scenarios.
(2) All subsequence methods are better suited for negative applica-
tions and PBAD can be selected for positive cases. (3) NP is recom-
mended for early detection. (4) Omni is recommended for negative
applications, while RCoder is better for positive ones.

5 DISCUSSIONS
In this paper, a taxonomy of anomaly detection methods is presen-
ted and systematic experimental intra- and inter-class comparisons
are proposed. Detailed findings are shown in the Summary part of
Section 4. We first summarize these findings into a practical guide
and finally highlight some research opportunities below.
A Practical Guide. A practical guide for timeseries anomaly de-
tection is presented in Figure 18 based on the experimental findings
on various aspects like type of anomaly, dimensionality, type of
application etc. Such a guide is formed according to current work
and future work is still encouraged.
Explainability. The explainability of anomaly detection methods
has raised many concerns in recent years [37]. A decision maker
may be more interested in the cause of the occurrence of outliers so
that they can take appropriate action, especially in the area of IoT
data [27]. Developing a method that provides both high accuracy
and reasonable explainability may be of interest for future work.

ACKNOWLEDGMENTS
Aoqian Zhang is supported by the NSFC (Grant Nos. 6210070801,
U21B2007). Guoren Wang is supported by the NSFC (Grant Nos.
61732003, U2001211). Ye Yuan is supported by the National Key R&D
Program of China(Grant No. 2022YFB2702100), the NSFC (Grant
Nos. 61932004, 62225203, U21A20516) and the DITDP (Grant No.
JCKY2021211B017). We also thank all the members of our com-
munity who open sourced their data and codes, which help us a lot
on this work.

494

---

<!-- PAGE 13 -->

REFERENCES
[1] Ahmed Abdulaal, Zhuanghua Liu, and Tomer Lancewicki. 2021. Practical Ap-
proach to Asynchronous Multivariate Time Series Anomaly Detection and Loc-
alization. In KDD. ACM, 2485–2494.

[2] Charu C. Aggarwal. 2013. Outlier Analysis. Springer.
[3]

Julien Audibert, Pietro Michiardi, Frédéric Guyard, Sébastien Marti, and Maria A.
Zuluaga. 2020. USAD: UnSupervised Anomaly Detection on Multivariate Time
Series. In KDD. ACM, 3395–3404.

[4] Vic Barnett, Toby Lewis, et al. 1994. Outliers in statistical data. Vol. 3. Wiley New

York.

[5] Ane Blázquez-García, Angel Conde, Usue Mori, and José Antonio Lozano. 2021.
A Review on Outlier/Anomaly Detection in Time Series Data. ACM Comput.
Surv. 54, 3 (2021), 56:1–56:33.

[6] Paul Boniol, Michele Linardi, Federico Roncallo, Themis Palpanas, Mohammed
Meftah, and Emmanuel Remy. 2021. Unsupervised and scalable subsequence
anomaly detection in large data series. VLDB J. 30, 6 (2021), 909–931.

[7] Paul Boniol, John Paparrizos, Themis Palpanas, and Michael J. Franklin. 2021.
SAND: Streaming Subsequence Anomaly Detection. Proc. VLDB Endow. 14, 10
(2021), 1717–1729.

[8] Mohammad Braei and Sebastian Wagner. 2020. Anomaly Detection in Univariate
Time-series: A Survey on the State-of-the-Art. CoRR abs/2004.00433 (2020).
[9] Bernardo Branco, Pedro Abreu, Ana Sofia Gomes, Mariana S. C. Almeida, João Ti-
ago Ascensão, and Pedro Bizarro. 2020. Interleaved Sequence RNNs for Fraud
Detection. In KDD. ACM, 3101–3109.

[10] Mikel Canizo, Isaac Triguero, Angel Conde, and Enrique Onieva. 2019. Multi-
head CNN-RNN for multi-time series anomaly detection: An industrial case
study. Neurocomputing 363 (2019), 246–260.

[11] Raghavendra Chalapathy and Sanjay Chawla. 2019. Deep Learning for Anomaly

Detection: A Survey. CoRR abs/1901.03407 (2019).

[12] Dhruv Choudhary, Arun Kejariwal, and Francois Orsini. 2017. On the Runtime-
Efficacy Trade-off of Anomaly Detection Techniques for Real-Time Streaming
Data. CoRR abs/1710.04735 (2017).

[13] Robert B Cleveland, William S Cleveland, Jean E McRae, and Irma Terpenning.
1990. STL: A seasonal-trend decomposition. J. Off. Stat 6, 1 (1990), 3–73.
[14] Andrew A. Cook, Goksel Misirli, and Zhong Fan. 2020. Anomaly Detection for
IoT Time-Series Data: A Survey. IEEE Internet Things J. 7, 7 (2020), 6481–6494.
[15] Zahra Zamanzadeh Darban, Geoffrey I. Webb, Shirui Pan, Charu C. Aggarwal,
and Mahsa Salehi. 2022. Deep Learning for Time Series Anomaly Detection: A
Survey. CoRR abs/2211.05244 (2022).
Janez Demsar. 2006. Statistical Comparisons of Classifiers over Multiple Data
Sets. J. Mach. Learn. Res. 7 (2006), 1–30.

[16]

[17] Ailin Deng and Bryan Hooi. 2021. Graph Neural Network-Based Anomaly
Detection in Multivariate Time Series. In AAAI. AAAI Press, 4027–4035.
[18] Ethan W. Dereszynski and Thomas G. Dietterich. 2011. Spatiotemporal Models
for Data-Anomaly Detection in Dynamic Environmental Monitoring Campaigns.
ACM Trans. Sens. Networks 8, 1 (2011), 3:1–3:36.

[19] Len Feremans, Vincent Vercruyssen, Boris Cule, Wannes Meert, and Bart Goeth-
als. 2019. Pattern-Based Anomaly Detection in Mixed-Type Time Series. In
ECML/PKDD (1) (Lecture Notes in Computer Science), Vol. 11906. Springer, 240–
256.

[20] Milton Friedman. 1937. The use of ranks to avoid the assumption of normality
implicit in the analysis of variance. Journal of the american statistical association
32, 200 (1937), 675–701.

[21] Markus Goldstein and Seiichi Uchida. 2016. A comparative evaluation of un-
supervised anomaly detection algorithms for multivariate data. PloS one 11, 4
(2016), e0152173.

[22] Manish Gupta, Jing Gao, Charu C. Aggarwal, and Jiawei Han. 2014. Outlier
Detection for Temporal Data: A Survey. IEEE Trans. Knowl. Data Eng. 26, 9 (2014),
2250–2267.

[23] D. M. Hawkins. 1980. Identification of Outliers. Springer.
[24] Yuanduo He, Xu Chu, and Yasha Wang. 2020. Neighbor Profile: Bagging Nearest
Neighbors for Unsupervised Time Series Mining. In ICDE. IEEE, 373–384.
Jordan Hochenbaum, Owen S. Vallis, and Arun Kejariwal. 2017. Automatic
Anomaly Detection in the Cloud Via Statistical Learning. CoRR abs/1704.07706
(2017).

[25]

[26] Min Hu, Xiaowei Feng, Zhiwei Ji, Ke Yan, and Shengchen Zhou. 2019. A novel
computational approach for discord search with local recurrence rates in mul-
tivariate time series. Inf. Sci. 477 (2019), 220–233.

[27] Ruihong Huang, Zhiwei Chen, Zhicheng Liu, Shaoxu Song, and Jianmin Wang.
2019. TsOutlier: Explaining Outliers with Uniform Profiles over IoT Data. In
IEEE BigData. IEEE, 2024–2027.

[28] Kyle Hundman, Valentino Constantinou, Christopher Laporte, Ian Colwell, and
Tom Söderström. 2018. Detecting Spacecraft Anomalies Using LSTMs and Non-
parametric Dynamic Thresholding. In KDD. ACM, 387–395.

[29] Vincent Jacob, Fei Song, Arnaud Stiegler, Bijan Rad, Yanlei Diao, and Nesime
Tatbul. 2021. Exathlon: A Benchmark for Explainable Anomaly Detection over
Time Series. Proc. VLDB Endow. 14, 11 (2021), 2613–2626.

[30] Eamonn J. Keogh, Jessica Lin, Sang-Hee Lee, and Helga Van Herle. 2007. Finding
the most unusual time series subsequence: algorithms and applications. Knowl.
Inf. Syst. 11, 1 (2007), 1–27. https://doi.org/10.1007/s10115-006-0034-6

[31] Kwei-Herng Lai, Daochen Zha, Junjie Xu, Yue Zhao, Guanchu Wang, and Xia
Hu. 2021. Revisiting Time Series Outlier Detection: Definitions and Benchmarks.
In Thirty-fifth Conference on Neural Information Processing Systems Datasets and
Benchmarks Track (Round 1). https://openreview.net/forum?id=r8IvOsnHchr

[32] Nikolay Laptev, Saeed Amizadeh, and Ian Flint. 2015. Generic and Scalable
Framework for Automated Time-series Anomaly Detection. In KDD. ACM, 1939–
1947.

[33] N. Jesper Larsson and Alistair Moffat. 1999. Offline Dictionary-Based Compres-
sion. In Data Compression Conference, DCC 1999, Snowbird, Utah, USA, March
29-31, 1999. IEEE Computer Society, 296–305.

[34] Alexander Lavin and Subutai Ahmad. 2015. Evaluating Real-Time Anomaly
Detection Algorithms - The Numenta Anomaly Benchmark. In ICMLA. IEEE,
38–44.

[35] Kim-Hung Le and Paolo Papotti. 2020. User-driven Error Detection for Time

Series with Events. In ICDE. IEEE, 745–757.

[36] Dan Li, Dacheng Chen, Baihong Jin, Lei Shi, Jonathan Goh, and See-Kiong Ng.
2019. MAD-GAN: Multivariate Anomaly Detection for Time Series Data with
Generative Adversarial Networks. In ICANN (4) (Lecture Notes in Computer
Science), Vol. 11730. Springer, 703–716.

[37] Zhong Li, Yuxuan Zhu, and Matthijs van Leeuwen. 2022. A Survey on Explainable

Anomaly Detection. CoRR abs/2210.06959 (2022).

[38] Fei Tony Liu, Kai Ming Ting, and Zhi-Hua Zhou. 2008. Isolation Forest. In ICDM.

IEEE Computer Society, 413–422.

[39] Shenghua Liu, Bin Zhou, Quan Ding, Bryan Hooi, Zheng bo Zhang, Huawei
Shen, and Xueqi Cheng. 2022. Time series anomaly detection with adversarial
reconstruction networks. IEEE Transactions on Knowledge and Data Engineering
(2022).

[40] Yue Lu, Renjie Wu, Abdullah Mueen, Maria A. Zuluaga, and Eamonn J. Keogh.
2022. Matrix Profile XXIV: Scaling Time Series Anomaly Detection to Trillions
of Datapoints and Ultra-fast Arriving Data Streams. In KDD ’22: The 28th ACM
SIGKDD Conference on Knowledge Discovery and Data Mining, Washington, DC,
USA, August 14 - 18, 2022, Aidong Zhang and Huzefa Rangwala (Eds.). ACM,
1173–1182.

[41] Aditya P. Mathur and Nils Ole Tippenhauer. 2016. SWaT: a water treatment
testbed for research and training on ICS security. In 2016 International Workshop
on Cyber-physical Systems for Smart Water Networks, CySWater@CPSWeek 2016,
Vienna, Austria, April 11, 2016. IEEE Computer Society, 31–36. https://doi.org/
10.1109/CySWater.2016.7469060

[42] Takaaki Nakamura, Makoto Imamura, Ryan Mercer, and Eamonn J. Keogh. 2020.
MERLIN: Parameter-Free Discovery of Arbitrary Length Anomalies in Massive
Time Series Archives. In 20th IEEE International Conference on Data Mining,
ICDM 2020, Sorrento, Italy, November 17-20, 2020. IEEE, 1190–1195.

[43] Craig G. Nevill-Manning and Ian H. Witten. 1997.

Identifying Hierarchical
Structure in Sequences: A linear-time algorithm. J. Artif. Intell. Res. 7 (1997),
67–82.

[45]

[46]

[44] Antonios Ntroumpogiannis, Michail Giannoulis, Nikolaos Myrtakis, Vassilis
Christophides, Eric Simon, and Ioannis Tsamardinos. 2023. A meta-level analysis
of online anomaly detectors. VLDB J. 32, 4 (2023), 845–886.
John Paparrizos, Paul Boniol, Themis Palpanas, Ruey S Tsay, Aaron Elmore, and
Michael J Franklin. 2022. Volume under the surface: a new accuracy evaluation
measure for time-series anomaly detection. Proceedings of the VLDB Endowment
15, 11 (2022), 2774–2787.
John Paparrizos and Luis Gravano. 2015. k-Shape: Efficient and Accurate Clus-
tering of Time Series. In Proceedings of the 2015 ACM SIGMOD International
Conference on Management of Data, Melbourne, Victoria, Australia, May 31 - June
4, 2015, Timos K. Sellis, Susan B. Davidson, and Zachary G. Ives (Eds.). ACM,
1855–1870.
John Paparrizos, Yuhao Kang, Paul Boniol, Ruey S. Tsay, Themis Palpanas, and Mi-
chael J. Franklin. 2022. TSB-UAD: An End-to-End Benchmark Suite for Univariate
Time-Series Anomaly Detection. Proc. VLDB Endow. 15, 8 (2022), 1697–1711.

[47]

[48] Bernard Rosner. 1975. On the detection of many outliers. Technometrics 17, 2

(1975), 221–227.

[49] Sebastian Schmidl, Phillip Wenig, and Thorsten Papenbrock. 2022. Anomaly
Detection in Time Series: A Comprehensive Evaluation. Proc. VLDB Endow. 15, 9
(2022), 1779–1797.

[50] Pavel Senin, Jessica Lin, Xing Wang, Tim Oates, Sunil Gandhi, Arnold P. Boedi-
hardjo, Crystal Chen, and Susan Frankenstein. 2018. GrammarViz 3.0: Interactive
Discovery of Variable-Length Time Series Patterns. ACM Trans. Knowl. Discov.
Data 12, 1 (2018), 10:1–10:28.

[51] Alban Siffer, Pierre-Alain Fouque, Alexandre Termier, and Christine Largouët.
2017. Anomaly Detection in Streams with Extreme Value Theory. In KDD. ACM,
1067–1075.

[52] Ya Su, Youjian Zhao, Chenhao Niu, Rong Liu, Wei Sun, and Dan Pei. 2019. Robust
Anomaly Detection for Multivariate Time Series through Stochastic Recurrent
Neural Network. In KDD. ACM, 2828–2837.

495

---

<!-- PAGE 14 -->

[53] Nesime Tatbul, Tae Jun Lee, Stan Zdonik, Mejbah Alam, and Justin Gottschlich.

2018. Precision and Recall for Time Series. In NeurIPS. 1924–1934.

[54] Markus Thill, Wolfgang Konen, and Thomas Bäck. 2017. Online anomaly detec-
tion on the webscope S5 dataset: A comparative study. In EAIS. IEEE, 1–8.
[55] Kai Ming Ting, Zongyou Liu, Hang Zhang, and Ye Zhu. 2022. A New Distribu-
tional Treatment for Time Series and An Anomaly Detection Investigation. Proc.
VLDB Endow. 15, 11 (2022), 2321–2333.

[56] Kai Ming Ting, Bi-Cun Xu, Takashi Washio, and Zhi-Hua Zhou. 2020. Isolation
Distributional Kernel: A New Tool for Kernel based Anomaly Detection. In KDD
’20: The 26th ACM SIGKDD Conference on Knowledge Discovery and Data Mining,
Virtual Event, CA, USA, August 23-27, 2020, Rajesh Gupta, Yan Liu, Jiliang Tang,
and B. Aditya Prakash (Eds.). ACM, 198–206.

[57] Luan Tran, Liyue Fan, and Cyrus Shahabi. 2016. Distance-based Outlier Detection

in Data Streams. Proc. VLDB Endow. 9, 12 (2016), 1089–1100.

[58] Shreshth Tuli, Giuliano Casale, and Nicholas R. Jennings. 2022. TranAD: Deep
Transformer Networks for Anomaly Detection in Multivariate Time Series Data.
Proc. VLDB Endow. 15, 6 (2022), 1201–1214.

[59] Chen Wang, Xiangdong Huang, Jialin Qiao, Tian Jiang, Lei Rui, Jinrui Zhang,
Rong Kang, Julian Feinauer, Kevin Mcgrail, Peng Wang, Diaohan Luo, Jun Yuan,
Jianmin Wang, and Jiaguang Sun. 2020. Apache IoTDB: Time-series database for
Internet of Things. Proc. VLDB Endow. 13, 12 (2020), 2901–2904.

[60] Frank Wilcoxon. 1992. Individual comparisons by ranking methods. In Break-

throughs in statistics. Springer, 196–202.

[61] Renjie Wu and Eamonn Keogh. 2021. Current time series anomaly detection
benchmarks are flawed and are creating the illusion of progress. IEEE Transactions
on Knowledge and Data Engineering (2021).

[62] Haowen Xu, Wenxiao Chen, Nengwen Zhao, Zeyan Li, Jiahao Bu, Zhihan Li, Ying
Liu, Youjian Zhao, Dan Pei, Yang Feng, Jie Chen, Zhaogang Wang, and Honglin
Qiao. 2018. Unsupervised Anomaly Detection via Variational Auto-Encoder for
Seasonal KPIs in Web Applications. In WWW. ACM, 187–196.

[63] Hui Yang, Satish T. S. Bukkapatnam, and Leandro G. Barajas. 2011. Local re-
currence based performance prediction and prognostics in the nonlinear and
nonstationary systems. Pattern Recognit. 44, 8 (2011), 1834–1840.

[64] Dragomir Yankov, Eamonn J. Keogh, and Umaa Rebbapragada. 2008. Disk aware
discord discovery: finding unusual time series in terabyte sized datasets. Knowl.
Inf. Syst. 17, 2 (2008), 241–262.

[65] Chin-Chia Michael Yeh, Yan Zhu, Liudmila Ulanova, Nurjahan Begum, Yifei Ding,
Hoang Anh Dau, Diego Furtado Silva, Abdullah Mueen, and Eamonn J. Keogh.
2016. Matrix Profile I: All Pairs Similarity Joins for Time Series: A Unifying
View That Includes Motifs, Discords and Shapelets. In IEEE 16th International
Conference on Data Mining, ICDM 2016, December 12-15, 2016, Barcelona, Spain.
IEEE Computer Society, 1317–1322.

[66] Susik Yoon, Jae-Gil Lee, and Byung Suk Lee. 2019. NETS: Extremely Fast Outlier
Detection from a Data Stream via Set-Based Processing. Proc. VLDB Endow. 12,
11 (2019), 1303–1315.

[67] Susik Yoon, Jae-Gil Lee, and Byung Suk Lee. 2020. Ultrafast Local Outlier De-
tection from a Data Stream with Stationary Region Skipping. In KDD. ACM,
1181–1191.

[68] Mohammed J. Zaki and Wagner Meira Jr. 2014. Data Mining and Analysis:

Fundamental Concepts and Algorithms. Cambridge University Press.

[69] Yong Zou, Marco Thiel, M. Carmen Romano, and Jürgen Kurths. 2007. Ana-
lytical Description of Recurrence Plots of Dynamical Systems with Nontrivial
Recurrences. Int. J. Bifurc. Chaos 17, 12 (2007), 4273–4283.

496

<!-- MARKITDOWN CONVERSION -->

<!-- Full MarkItDown conversion for formatting fidelity. -->

An Experimental Evaluation of Anomaly Detection in Time
Series
AoqianZhang ShuqingDeng DongpingCui
BeijingInstituteofTechnology BeijingInstituteofTechnology BeijingInstituteofTechnology
aoqian.zhang@bit.edu.cn shuqing.deng@bit.edu.cn dongping.cui@bit.edu.cn
YeYuan GuorenWang
BeijingInstituteofTechnology BeijingInstituteofTechnology
yuan-ye@bit.edu.cn wanggr@bit.edu.cn
ABSTRACT beenstudiedinvariousapplications,suchasfrauddetection[9],
Anomalydetectionintimeseriesdatahasbeenstudiedfordec- environmentalmonitoringalerting[18]andindustrialmanufac-
adesinbothstatisticsandcomputerscience.Variousalgorithms turing[10],cyberattackidentification[36],etc.Unfortunately,an
havebeenproposedfordifferentscenarios,suchasfrauddetec- anomalyisratherchallengingtodefine,especiallyinthecontext
tion,environmentalmonitoring,manufacturing,andhealthcare. oftimeseriesdata[54].Forthefollowingreasons,itisdifficultto
However,thereisalackofcomparativeevaluationofthesestate- evaluatetheperformanceofananomalydetectionmethodandto
of-the-artapproaches,especiallyinthesametestenvironmentand selectthesuitableone(withappropriateparameters)forhandling
withthesamebenchmark,makingitdifficultforuserstoselectan anomaliesinreal-worldscenarios.
appropriatemethodforreal-worldapplications.Inthispaper,we Thefirstreasonisthecomplexityanddiversityoftimeseries
presentataxonomyofanomalydetectionmethodsbasedonthe data[29].Asingletimeseriesdatamaybeunivariateormultivari-
mainfeatures,i.e.,datadimension,processingtechnique,andan- ate,andthelattermayhaveanumberofdimensions.Moreover,
omalytypeandsixinnerclasses.Weperformsystematicintra-and theanomaliesencounteredmaybeofdifferenttypes[22].Several
inter-classcomparisonsofseventeenstate-of-the-artalgorithmson algorithmshavebeenproposedtodetectanomalousbehaviorusing
realandsyntheticdatasetswithapointmetriccommonlyusedin differenttechniques,buttheyoftenfocusonaspecificcase.For
classificationproblemsandarangemetricspecificallydesignedfor instance,[25]isonlyabletofindanomalousdatapointsinuni-
subsequenceanomaliesintimeseriesdata.Weanalyzetheprop- variatetimeseries.[7]canhandleunivariatedatastreams,butcan
ertiesofthesealgorithmsandtestthemintermsofeffectiveness, onlydetectanomalouspatternsofacertainlength.Therefore,after
efficiency,androbustnesstoanomalyrates,datasizes,numberof analyzingthestate-of-the-artanomalydetectionalgorithms,we
dimensions,anomalypatterns,andthresholdsettings.Wealsotest classifythemintothreefacetsrepresentingthethreemainfeatures
theirperformanceindifferentusecases.Finally,weprovideaprac- [5],i.e.,datadimension,processingtechnique,andanomalytype.
ticalguidefordetectinganomaliesintimeseriesanddiscussions. Wecanfurtherdividethemintoclassesunderaparticularfacet,as
showninFigure1,tomakemoredetailedcomparisons.
PVLDBReferenceFormat: Thesecondreasonisthelackofthoroughtestingwiththesame
AoqianZhang,ShuqingDeng,DongpingCui,YeYuan,andGuorenWang. datasetsonthesameplatformandwiththesamemetrics.Different
AnExperimentalEvaluationofAnomalyDetectioninTimeSeries.PVLDB, worksprovidecomparisonswithdifferentscores,evenwiththe
17(3):483-496,2023. samebasicprecision-recall-F1metric[2].Forexample,[52]calcu-
doi:10.14778/3632093.3632110 latesF1scoreusingaverageprecisionandaveragerecall,whereas
[1]considersF1scoreafterthresholdadjustment.Inaddition,the
PVLDBArtifactAvailability:
baselinesbeingcomparedmaybewritteninadifferentlanguage
Thesourcecode,data,and/orotherartifactshavebeenmadeavailableat
orusedifferentdatastructures.Therefore,forafairperformance
https://github.com/zaqthss/experiment-tsad.
comparison,systematicexperimentsshouldbeperformedbetween
methodsofthesameclassinthesametestenvironment,whichis
1 INTRODUCTION
calledintra-classcomparison.
Timeseriesisoneofthemostcommonlyuseddatatypesinrecent Thethirdreasonarisesfromtheobservationthatsomerecent
decades.Timeseriesanalysisinvolvesmethodsofdataanalysisto papers[1,3,52,58]evaluatetheirmethodsunderpointmetricson
gainvaluableinsights.Anomalydetectionaimstofindrareobser- datasetswithsubsequenceanomaly.Theseareessentiallypoint
vationsthatdeviatesignificantlyfromthemajorityofdata[23]and methods,asananomalyscoreisassignedtoeachdatapointand
isthemostimportantpartoftimeseriesanalysis(mining).Ithas thosepointswhosescoreisaboveathresholdarereportedasan
anomaly.Inaddition,tointerpretthedetectiononasubsequence,
ThisworkislicensedundertheCreativeCommonsBY-NC-ND4.0International theymodifythepredictionresultsbeforeevaluationusingthepoint-
License.Visithttps://creativecommons.org/licenses/by-nc-nd/4.0/toviewacopyof
thislicense.Foranyusebeyondthosecoveredbythislicense,obtainpermissionby adjust[62]method.However,acomprehensiveexperimentshould
emailinginfo@vldb.org.Copyrightisheldbytheowner/author(s).Publicationrights beemployedtoanalyzetheeffectsofthesemeasures.Intermsof
licensedtotheVLDBEndowment.
efficiency,especiallyinbigdataapplicationswheretimeseriesdata
ProceedingsoftheVLDBEndowment,Vol.17,No.3ISSN2150-8097.
doi:10.14778/3632093.3632110 havehighdimensions(morethan50)andlargescales(morethan
483

100k),thetrade-offbetweeneffectivenessandefficiencyshouldbe Interrepresentstheconsiderationofcomparisonsbetweenuni-
considered.Inparticular,thepossibilityofimplementingunivariate variateandmultivariatemethods.Similarly,<Batch,Online,Inter>
modelsoneachdatadimension[28]andfindingouttowhatextent refers to the processing technique, while <Point, Range, Inter>
onlinedetectorsapproximatetheperformanceofbatchmethods focusesonthetypeoftargetanomaly.ThresholdsRobustnessin-
[12,44]couldreceivespecialattention.Therefore,comparisons dicateswhethertheworkexaminestherobustnessofthecompared
betweenclassesinthesamefacet,whichwecallinter-classcom- methodstothresholding.Finally,ApplicationGuidelineindicates
parisons,arealsouseful.Finally,theessentialfeaturesofanomaly whethertheworkprovidespracticalguidelinesformethodselection
detectionalgorithms,includingrobustnessintermsofthreshold inreal-worldscenarioswithdifferentrequirements.
setting,shouldbecapturedintermsofpracticalapplications.Sys- In[57],distance-basedonlinedetectionmethodsofpointout-
tematicexperimentswithdifferentrealcasesandanalysisofthe liersindatastreamsareevaluated.However,onlyefficiencyfactors
behaviorofthesealgorithmswillbehelpfulforusers. suchasCPUtimeandleakagememoryaretestedunderdifferent
parameters.MD[12]comparesruntimeandefficacyofdifferent
1.1 Contributions detectionmethodsforfourtypesofanomaliesinrealstreaming
Tothebestofourknowledge,thisisthefirstin-depthexperimental cases.Itservesasaguideforselectingthe‘best’univariatetech-
studytoprovidebothintra-classandinter-classevaluations.Our niqueintermsofreal-timeandaccuracy,butlacksconsiderations
maincontributionsinthispaperaresummarizedasfollows. forthecharacteristicsofthedatasetsandthetypeofapplication.
TUD[8]focusesonsupervisedmethodsforunivariatedata.TODS
(1) Weproposeataxonomyofmethodsfordetectinganomaliesin
[31]revisesoutlierdefinitionsandproposesanewtaxonomyfor
timeseriesbasedontheiressentialfeaturesinthreefacetsand
anomaly types. It tests batch methods under different anomaly
sixinnerclassesinSection2.
ratesfordifferenttypesofanomalies,butomitsevaluationsunder
(2) Wepresentbriefdescriptionsof17state-of-the-artmethods
otherfactorssuchasdatadimensions.Exathlon[29]generatesa
inSection3.Furthermore,were-implement10ofthemwith
novelbenchmarkingplatform.Threedeeplearningmethodsare
JAVA,refactorallmethodswiththesamecodestructure,and
testedontheproposeddatasetswithrangeanomaliesandeval-
buildatestingframeworktoavoidthepotentialimpact.
uatedbyrangemetrics[53].Itsmajordifferencetoothersisthe
(3) Weprovidesystematicintra-classcomparisonsunderdifferent
capabilityofevaluatingexplanationdiscoveryresults,whichisnot
scenarioswithreal-worldandsyntheticdatasetsinSection4.2,
coveredbyourwork.Nevertheless,itfailstocomparemoretypes
including(a)effectivenesswithpoint-andrange-basedmetrics,
ofanomalydetectionmethodsandprovidemorecomprehensive
(b)anomalyrates,(c)datasizes(scalability),(d)dimensions,(e)
analysis.TSB-UAD[47]establishesanewbenchmarktofacilitate
anomalypatterns.
theevaluationofunivariatemethodsandevaluatesseveralbatch
(4) Weemployinter-classcomparisonsanddrawinterestingfind-
methodstodemonstratetherobustnessoftheproposedbenchmark,
ingsinSection4.3,like(a)pointanomalymethodscanalso
butdoesnotaddressmultivariatetimeseriescases.Theaforemen-
performwellundersubsequenceanomalycases,(b)usingrange
tionedTODS,Exathlon,andTSB-UADprovidenovelbenchmarks
metricsonsubsequencedatacanleadtomorereasonableand
basedondifferenttechniquesthatpresentthemaincontributions
robustresults,(c)point-adjustmethodtendstoreport‘false’
anddifferencesfromotherstudies.Meta[44]presentsaqualitative
higheraccuracyresultsandmaymisleadanalysis.
reviewofonlinedetectorsfromdifferentfamiliesandproposesa
(5) Weanalyzethecapabilityofmethodsunderdifferentapplic-
fairevaluationenvironmentforonlineandofflinedetectorsover
ationcases,consistingof(a)thefalsepositivesandnegatives
multivariatedata.Thegoalistofindouttowhatextentonlinede-
theygenerate,(b)whethertheycandetectanomaliesasearly
tectorsapproximatetheperformanceofofflinedetectors.However,
aspossibleandproviderecommendationsinSection5.
itfocusesonlyonunsupervisedmethodsfordetectingpointanom-
1.2 RelatedWork alies(includingrangeanomalieswithpointmetrics)andleavesout
(semi)supervisedmethods.
Table1:ComparisonofTADExperimentalSurveys HPI[49]makesanexhaustiveevaluationof71anomalydetec-
tionmethodsandevaluatesthemonvariousdatasetswithdifferent
typesofanomalies.Althoughitprovidesacomprehensiveevalu-
Dimension Processing AnomalyType Threshold Application
ExpSurvey <Uni,Mul,Inter> <Batch,Online,Inter> <Point,Range,Inter> Robustness Guideline ation,itstillhassomeuntouchedareas,whichweextendasfollows:
DODDS[57] <(cid:37),(cid:33),(cid:37)> <(cid:37),(cid:33),(cid:37)> <(cid:33),(cid:37),(cid:37)> (cid:37) (cid:37) (1)Theyoptimizetheparametersofallmethodsgloballyoverthe
MD[12] <(cid:33),(cid:37),(cid:37)> <(cid:37),(cid:33),(cid:37)> <(cid:33),(cid:33),(cid:37)> (cid:37) (cid:33)
TUD[8] <(cid:33),(cid:37),(cid:37)> <(cid:33),(cid:37),(cid:37)> <(cid:33),(cid:37),(cid:37)> (cid:37) (cid:33) samewell-labeledsyntheticdataset,butwetunetheseparameters
TODS[31] <(cid:37),(cid:33),(cid:37)> <(cid:33),(cid:37),(cid:37)> <(cid:33),(cid:33),(cid:33)> (cid:37) (cid:37)
Exathlon[29] <(cid:37),(cid:33),(cid:37)> <(cid:33),(cid:37),(cid:37)> <(cid:37),(cid:33),(cid:37)> (cid:33) (cid:33) perdatasettogetafairerevaluationwiththeirbestperformance;
TSB-UAD[47] <(cid:33),(cid:37),(cid:37)> <(cid:33),(cid:37),(cid:37)> <(cid:33),(cid:33),(cid:37)> (cid:37) (cid:37) (2)Theydonotconsiderthetranslationofanomalyscorestoan-
Meta[44] <(cid:37),(cid:33),(cid:37)> <(cid:33),(cid:33),(cid:33)> <(cid:33),(cid:33),(cid:37)> (cid:37) (cid:33)
HPI[49] <(cid:33),(cid:33),(cid:37)> <(cid:33),(cid:37),(cid:37)> <(cid:33),(cid:33),(cid:37)> (cid:37) (cid:33) omalylabelsviathresholding,however,weanalyzetherobustness
Ourwork <(cid:33),(cid:33),(cid:33)> <(cid:33),(cid:33),(cid:33)> <(cid:33),(cid:33),(cid:33)> (cid:33) (cid:33) ofusingdifferentthresholdingtechniquessinceanomalyidenti-
ficationiscrucialinmostreal-worldscenarios;(3)Theysimply
Wesummarize8previousexperimentalstudiesontimeseries implementpointandrangemetricsforpointandsubsequencean-
anomalydetectionandourworkinTable1.Thefirstthreecolumns omalies,respectively,withoutdeeperanalysis.Wealsoperform
representthefundamentalfacetscoveredinthestudy,e.g.,inthe theinter-classcomparisonusingapointmetricforsubsequence
firstcolumn,Uniindicatesthattheworkincludesunivariatedetec- anomalies,whichhasbeenwidelyusedinpreviousstudies,and
tionmethods,Mulstandsformultivariatedetectionmethods,while findinsightfulresults;(4)Theirresearchinsightscanhelpusers
484

2.2 AnalysisFacets
Theanomalyanalysisproblemscanbecategorizedinvariousways
[22].Inthiswork,weproposeacomprehensivetaxonomyconsist-
ingofthefollowingthreefacets,i.e.,datadimension,processing
technique,andanomalytype,asshowninFigure1.Foreachfacet,
Figure1:Facetsandclassesofanomalydetectionalgorithms
wefurtherdividedetectionmethodsintoclasses.Thedetailsof
thesefacetsandclassesarepresentedinthissection.
| 12.5 |     |       |     | 2.2.1 Datadimension. | Thenumberoftime-dependentvariables |     |     |
| ---- | --- | ----- | --- | -------------------- | ---------------------------------- | --- | --- |
|      | O2  | U n i |     |                      |                                    |     |     |
O3 D i m 1 thatananomalydetectionmethodcanconsidersimultaneouslyis
| 10.0 |     | D i m 2 |     |                                                 |     |     |             |
| ---- | --- | ------- | --- | ----------------------------------------------- | --- | --- | ----------- |
|      |     |         |     | itsessentialfeature[5].FollowingDefinition2.1,𝑿 |     |     | iscalledasa |
eulav 7.5
|     |     | O4  |     | univariatetimeseriesif𝐷 | =   | 1while𝑿 isamultivariatetime |     |
| --- | --- | --- | --- | ----------------------- | --- | --------------------------- | --- |
5.0
seriesif𝐷 >1.
| 2.5 | O1  | O6  |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- |
|     | O5  | O7  |     |     |     |     |     |
0.0 Scenario1:Highdimension. Theoretically,multivariatemethods
| 1   | 6 11 16 21 | 26 31 36 41 |     |     |     |     |     |
| --- | ---------- | ----------- | --- | --- | --- | --- | --- |
timestamp canexploitcorrelationsbetweendimensions,resultinginbetter
(a) Univariate(above)/Multivariate(below) time series
accuracythanunivariatemethods,whichcanonlytreateachdi-
Figure2:(a)timeseriesand(b)onlineprocessingtechnique
mensionseparately.However,multivariatemethodsrequiremuch
moretime,asunivariatemethodscanachievehighefficiencyby
|     |     |     |     | parallelizing each | dimension. | The test on Swat | (51 dimensions) |
| --- | --- | --- | --- | ------------------ | ---------- | ---------------- | --------------- |
showsthat,theunivariatemethodIDKcosts16.50s,whilethemul-
selecttheoptimalalgorithmforspecificanomalytypes,suchas tivariatemethodPBADtakes125.17s,almost10timesthetime.On
extremumanomalies.Wealsoanalyzereal-worldapplicationsthat theotherhand,[28]implementstheLSTMmodeloneachdimen-
aremoreinterestedinpositive,negative,andearlydetectioncases,
sionofthesatellitedataset,sinceLSTMshavedifficultypredicting
andprovideapracticalguideformethodselection.
m-dimensionalresultsaccuratelywhenmislarge.Therefore,a
Theabovepapersinvestigateproblemsoftimeseriesanomaly systematicinter-classcomparisonsshouldbeperformedtotestthe
detection(TAD)fromvariousaspects,butleaveroomforfurther possibilityofusingunivariatemethodsonmultivariatedata.
analysis.Theoreticalsurveys[5,11,14,22]provideastructured
overviewofresearchmethodswithdifferentemphases.Incontrast, 2.2.2 ProcessingTechniques. Atimeseriescanalsohaveaninfinite
weconsiderthestate-of-the-artmethodsnotcoveredinthesestud- numberofdatapoints(stream).Methodsthatcanhandleinfinite
ies,performacomprehensiveanalysisonwiderrangesasshown timeseriesarecalledonlinemethods,whilethosethatcannotare
calledbatchmethods.Theslidingwindowisthetechniquemost
inTable1,andobtaincontributionsasindicatedinSection1.1.
Theoriginalpapersproposinganomalydetectionalgorithms commonlyusedbyonlinemethods[57].
thatwecompareinourwork[1,3,6,7,17,19,24–26,39,42,50,
|     |     |     |     | Scenario2:LargeScale. | Theoretically,batchmethodshavehigher |     |     |
| --- | --- | --- | --- | --------------------- | ------------------------------------ | --- | --- |
52,55,58,66,67]alsoconsistofempiricalcomparisons.However,
accuracybecausetheycancomparealldatasimultaneously.Incon-
theseexperimentsarelimitedintermsofdatasets,competitors,and
trast,onlinemethodscanrunfasterbecausetheyprocessonlythe
thoroughanalyzesofprecision/recall,efficiency,andsensitivity
datapointsinthecurrentwindow.Ontheonehand,onlinemeth-
| compared | to our study. | We use datasets from | these works and |     |     |     |     |
| -------- | ------------- | -------------------- | --------------- | --- | --- | --- | --- |
odscancontinuouslyupdatetheirmodelsforincrementalanomaly
benchmarksfromNumenta[34],Exathlon[29],andTODS[31].
detectiontoaccountforthefactthattimeseriescharacteristics
evolveovertime[21,44].Ontheotherhand,theefficiencygap,
2 PRELIMINARIES especiallyforlargedatasets,shouldalsobetakenintoaccount[40].
2.1 ProblemDefinition Therefore,like[44],weareinterestedintheextenttowhichonline
methodsapproximatetheperformanceofbatchmethodsandwhat
Anomalydetectionintimeseriesdatacanbedefinedasfollows.
thetrade-offbetweeneffectivenessandefficiencyis.
| Definition2.1(Timeseries).                              |     | Atimeseriesisaseriesofdatapoints |     |                     |                                     |     |     |
| ------------------------------------------------------- | --- | -------------------------------- | --- | ------------------- | ----------------------------------- | --- | --- |
|                                                         |     |                                  |     | 2.2.3 AnomalyTypes. | Inatimeseries,datapointsthatdeviate |     |     |
| indexedintimeorder.Consideratimeseriesof𝑛observations,𝑿 |     |                                  | =   |                     |                                     |     |     |
significantlyfromotherobservationsarecalledpointanomalies.
| {𝒙1 ,...,𝒙𝑛}.The𝑖-thobservation(datapoint)𝒙𝑖 |     |     | ∈ R𝐷 consists |     |     |     |     |
| -------------------------------------------- | --- | --- | ------------- | --- | --- | --- | --- |
Subsequencesofthetimeserieswithlesssimilaritycomparedto
| of𝐷 dimensions{𝑥 | 1,...,𝑥 | 𝐷}andisobservedattimestamp𝑡 |     |     |     |     |     |
| ---------------- | ------- | --------------------------- | --- | --- | --- | --- | --- |
𝑖 𝑖 𝑖.A othersarecalledassubsequenceanomalies.Thecapabilityofa
,...,𝒙ℓ−𝑖+1
subsequence𝑿𝑖,ℓ ={𝒙𝑖 }isasubsetofconsecutivetime methodmustbeevaluatedbyanappropriatemetricrelatedtothe
| pointsfromtimeseries𝑿 |     | startingatposition𝑖withlengthℓ. |     |     |     |     |     |
| --------------------- | --- | ------------------------------- | --- | --- | --- | --- | --- |
typeofanomaly,otherwisemisleadingresultsmaybeobtained
[45,53].Tocomparemethodsindifferentcases,wefurtherdivide
| Definition2.2(AnomalyDetectioninTimeSeries). |     |     | Ananomaly |     |     |     |     |
| -------------------------------------------- | --- | --- | --------- | --- | --- | --- | --- |
pointandsubsequenceanomaliesintothefollowingpatterns[31].
isanobservation(orsubsetofobservations)whichappearstobe
inconsistentwiththeremainderofthatsetofdata[4].Anomaly ={𝒙1 ,...,𝒙𝑛}.Let|𝒙𝑡 −
|     |     |     |     | PointAnomaly. | Givenatimeseries𝑿 |     |     |
| --- | --- | --- | --- | ------------- | ----------------- | --- | --- |
>𝛿,where𝛿isathresholdand𝒙ˆ𝑡
detectionintimeseriesinvolvesfindingtheabnormaldatapoints 𝒙ˆ𝑡| istheexpectedvalue.Global
𝒙𝑖 orsubsequences𝑿𝑖,ℓ inthegiventimeseries. anomaly indicates that𝛿 ∼ 𝜎(𝑿), where 𝜎(𝑿) is the standard
deviationofthewholetimeseries.Contextualanomalywith𝛿 ∼
485

Table2:Anomalydetectionmethodsconsideredhere 3.1 Distance-basedMethods
Distance-basedalgorithms[57]intheliteraturecandetectboth
Algorithm Mul Process Anomaly Threshold Code Speedup pointandsubsequenceanomalies,butforsimplicityweonlyrefer
|     |     | ✓   |     |     | 𝜃𝑘  |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
ecnatsiD NETS[66] ✓ online point JAVA - topointanomaliesinthefollowingdefinitions.
|     | STARE[67]  |     | online | point       | top-𝜃𝐾 JAVA   | -   |     |                          |     |                          |     |     |         |
| --- | ---------- | --- | ------ | ----------- | ------------- | --- | --- | ------------------------ | --- | ------------------------ | --- | --- | ------- |
|     | NP[24]     | -   | batch  | subsequence | top-𝜃𝐾 python | 1.5 |     |                          |     |                          |     |     |         |
|     | MERLIN[42] | -   | batch  | subsequence | top-𝜃𝐾 matlab | 60  |     |                          |     |                          |     |     |         |
|     |            |     |        |             |               |     |     | Definition3.1(Neighbor). |     | Givenadistancethreshold𝜃 |     |     | 𝑅,adata |
|     | PBAD[19]   | ✓   | batch  | subsequence | top-𝜃𝐾 python | 2.5 |     |                          |     |                          |     |     |         |
LRRDS[26] ✓ batch subsequence cluster r 1 point𝑥 is a neighbor of datapoint𝑥 𝑗(𝑥 ≠ 𝑥 𝑗) if the distance
|     | nrettaP SAND[7] | -   | online | subsequence | top-𝜃𝐾 C&python | 0.3 |     | 𝑖        |     |     | 𝑖   |     |     |
| --- | --------------- | --- | ------ | ----------- | --------------- | --- | --- | -------- | --- | --- | --- | --- | --- |
|     |                 |     |        |             | top-𝜃𝐾          |     | 𝑑(𝑥 | ,𝑥 𝑗) ≤𝜃 |     |     |     |     |     |
|     | NormA[6]        | -   | batch  | subsequence | C&python        | -   |     | 𝑖        | 𝑅.  |     |     |     |     |
|     | GrammarViz[50]  | -   | batch  | subsequence | top-𝜃𝐾 JAVA     | -   |     |          |     |     |     |     |     |
|     | IDK[55]         | -   | batch  | subsequence | top-𝜃𝐾 python   | 20  |     |          |     |     |     |     |     |
SHESD[25] - batch point 𝜃𝑘,top-𝜃𝐾 JAVA Definition3.2(Distance-basedOutlier). Givenatimeseries𝑋,
gninraeLpeeD Be a tG A N [ 3 9] ✓ b a t c h subs e q u e nce top - 𝜃𝐾 p y t h o n - acountthreshold𝜃 andadistancethreshold𝜃 𝑅,distance-based
|     | O m n i [5 | 2 ] ✓ | b a t c h | p o i n t | 𝜃 𝜏 p y t h o | n - |     |     | 𝑘   |     |     |     |     |
| --- | ---------- | ----- | --------- | --------- | ------------- | --- | --- | --- | --- | --- | --- | --- | --- |
U SA D [3 ] ✓ b a t c h p o i n t 𝜃 p y t h o n - outliersaresetofdatapointsthathavelessthan𝜃
|     |           | ✓   |           |           | 𝜃 𝜏         |     |     |     |     |     |     | 𝑘   | neighbors. |
| --- | --------- | --- | --------- | --------- | ----------- | --- | --- | --- | --- | --- | --- | --- | ---------- |
|     | G D N [1  | 7 ] | b a t c h | p o i n t | 𝜏 p y t h o | n - |     |     |     |     |     |     |            |
|     | RCoder[1] | ✓   | batch     | point     | 𝜃𝜏 python   | -   |     |     |     |     |     |     |            |
TranAD[58] ✓ batch point 𝜃𝜏 python - The key factors are the distance threshold𝜃 and the count
𝑅
threshold𝜃 𝑘,determiningtheneighborsforeachdatapointandthe
𝜎(𝑿𝑡−𝑘,𝑡+𝑘)denotesthatthesuchanomalypointisdifferentfrom anomalies.Foronlinemethods,thefactorswindowsize𝜃
𝑊 andthe
slidesize𝜃
itsneighborsinaspecificrange(windowsize𝑘). 𝑆 affecttheperformanceandareusuallysetdepending
onthesizeofthedataset.Distancemethodsforpointanomalies
| SubsequenceAnomaly. |                  |     | Here,weassumethatthesubsequence |     |      |     |       |       |                    |         |      |             |           |
| ------------------- | ---------------- | --- | ------------------------------- | --- | ---- | --- | ----- | ----- | ------------------ | ------- | ---- | ----------- | --------- |
|                     |                  |     |                                 |     |      |     | often | focus | on the scalability | problem | [57] | and utilize | different |
| 𝑋                   | =𝜌(2𝜋𝜔𝑇 𝑖,𝑗)+𝜏(𝑇 |     | 𝑖,𝑗),where𝜌,𝜔                   |     | and𝜏 |     |       |       |                    |         |      |             |           |
𝑖,𝑗 representsthebasic structurestosaverunningtimes.NETS[66]employsaset-based
shape,trendandseasonality,respectively.Global(shapelet)anomaly
approachfollowingneteffect,thatdatapointsinashortperiodof
referstothesubsequenceswithdissimilarbasicshapes,whichcan
timearelikelytobeconcentratedinasetofsmallregionsinthe
| bedefinedas𝑠(𝜌,𝜌ˆ) |     | >   | 𝛿,where𝑠 | isthesimilarityfunction[31]. |     |     |     |     |     |     |     |     |     |
| ------------------ | --- | --- | -------- | ---------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
dataspace.STARE[67]observesthatdatadistributionsinmany
| Seasonalanomalywith𝑠(𝜔,𝜔ˆ) |     |     |     | >𝛿meansthatthosesubsequences |     |     |     |     |     |     |     |     |     |
| -------------------------- | --- | --- | --- | ---------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
regionsofthedataspacechangelittleacrosswindowslidesand
haveunusualseasonalitycomparedtothewholeseries.Trendan- thusskipsupdatingdensitiesinlocalregionsthatdonotchange
omalyindicatesthesubsequencesthatsignificantlyalterthetrend
significantly.NP[24]usesbaggingtorobustlydiscoverfrequentand
ofthetimeseries,leadingtoapermanentshiftinthemeanofthe
raresubsequences.Anearestneighborballtechniquethatreplaces
| data,whichcanbedenotedas𝑠(𝜏,𝜏ˆ) |     |     |     |     | >𝛿. |     |     |     |     |     |     |     |     |
| ------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
thenearestneighbordistancewhichistoosmallwiththeradiusof
Scenario3:Parameterrelaxation. Nevertheless,itisdifficultto suchaballisproposedtoprovidearobustestimationandsolvethe
twinfreakproblem[24],whichisnotsolvedinmatrixprofile[65].
findaspecificpatternofananomalyinrealdatasets.Currentsub-
DRAG[64]createsacandidatediscordset𝐶andthensearchesitfor
| sequencemethodsrequirethelength |     |     |     |     | ofthetargetsubsequence |     |     |     |     |     |     |     |     |
| ------------------------------- | --- | --- | --- | --- | ---------------------- | --- | --- | --- | --- | --- | --- | --- | --- |
asinput[5–7].However,itisratherdifficulttodeterminesuch alistofdiscordswhosenearestneighbordistanceisgreaterthana
aparameterwithoutsufficientpriorknowledge.Incontrast,the hyper-parameter𝑟.MERLIN[42]providesastructuredsearchto
pointmethodsdonotrequiresuchadditionalinput(thelengthis setsuch𝑟.SinceNETSandMERLINdominatesDRAG,respectively,
inalmostallthedatasetsandhenceweonlyreporttheformertwo
1).Hence,wewonder(1)howpowerfulpointmethodsareinthe
| presenceofanomaliesinsubsequences;(2)howwellthemethods |     |     |     |     |     |     | here. |     |     |     |     |     |     |
| ------------------------------------------------------ | --- | --- | --- | --- | --- | --- | ----- | --- | --- | --- | --- | --- | --- |
candetectdifferentpatternsofanomalies.
3.2 Pattern-basedMethods
| Example2.3. |     | Pointandsubsequenceanomaliescanbeunivariate |     |     |     |     |     |     |     |     |     |     |     |
| ----------- | --- | ------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
ormultivariate.Figure2(a)showstwounivariatepointanomalies, Theso-calledpatternrepresentstheregularitiesinthedata,such
𝑂1(global)and𝑂5(contextual).Intermsofpatterns,𝑂3isatrend asanorderedsetofdatapointsthatoccurfrequentlyinthedata,
anomalyasitleadstoapermanentshiftwithalowermean,𝑂2is oraparticulardistribution.Pattern-basedmethods[14]areusu-
aseasonalanomalyand𝑂4,𝑂6areglobalanomalies.Datapoints allyproposedtofindsubsequenceanomalies,whichweuseinthe
in univariate time series𝑋 = {𝑥 ,...,𝑥 } are observed at time followingdefinitions.Pointanomaliescanbefoundifthepattern
|     |     |     |     | 1   | 6   |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
1,2,3,5,7,8inFigure2(b).Letussetthewindowsize𝜃 𝑊 =4,slide indicatesadistribution.
size𝜃 = 2.Theonlinemethodwillfirstprocessthedatapoints
|       | 𝑆           |     |     |     |     |           |     | Definition3.3(Pattern-basedOutlier). |     |     | Givenatimeseries𝑋,an |     |     |
| ----- | ----------- | --- | --- | --- | --- | --------- | --- | ------------------------------------ | --- | --- | -------------------- | --- | --- |
| { 𝑥 , | . . . , 𝑥 } |     |     |     |     | { 𝑥 , 𝑥 } |     |                                      |     |     |                      |     |     |
1 4 i n th e c u r r e n t w i n do w . A f t e r t h e p r o c e s s i n g , 1 2 ℓ 𝜃
𝑥 , 𝑥 a n o m a l y le n g t h a n d a c o u n t t h r e s h o ld 𝐾 , p a t ter n - b as e d o u t lie r s
i n t h e fi r s t s l i d e w i l l b e e x p i r e d a n d { 5 6 } i n t h e n e w s l id e w il l 𝜃 ℓ
|       |                    |           |           |           |                       |           | a r  | e t h e s e   | t o f t o p - 𝐾 s u    | b s e q u e n c e s | w i th le n | g t h a | n d t h e l o w e s t |
| ----- | ------------------ | --------- | --------- | --------- | --------------------- | --------- | ---- | ------------- | ---------------------- | ------------------- | ----------- | ------- | --------------------- |
| c o m | e i n , f o r m in | g a n e w | w i n d o | w c o n t | a i n i n g { 𝑥 , . . | . , 𝑥 } . |      |               |                        |                     |             |         |                       |
|       |                    |           |           |           | 3                     | 6         | si m | i l a r i t y | t o t h e p a t t er n | s e x tr a c t e d  | fr o m 𝑋 .  |         |                       |
3 ALGORITHMS
Thefactorsforpatternmethodsvarydependingonhowthey
Followingtheproposedtaxonomy,wechoosethelatestrepresent- definepatterns,support,andthresholdforanomalies.Ingeneral,the
ativesforeachclass:11/17ofthesemethodsarepublishedsince keyfactorsarethesupportthreshold𝜃 𝑠𝑢𝑝,theanomalythreshold
2020and12/17arenotcomparedinpriorworksinSection1.2.We 𝜃 𝜏,orthecountthreshold𝜃 𝐾,whichrepresenttheminimumoccur-
willbrieflyintroducethemintheclassofdetectiontechniques, renceofapattern,theborderofananomaly,andtherankofscores
i.e.,distance,pattern,anddeeplearning-basedandextracttheir thatananomalyachieves,respectively.
criticalfactors.Table2liststhepropertiesofeachalgorithm.The ESD[48]computestheExtremeStudentizedDeviateteststat-
‘threshold’columnindicateshowthethresholdforanomaliesisset. istictofindanomalypoints.SHESD[25]extendsESDbyusing
486

STLdecomposition[13]andreplacingthemeanandstandardde- Table3:Real-worldandsyntheticdatasetssummary
viationwithmorerobustmedianandmedianabsolutedeviation.
Consideringtheseasonality,SHESDoutperformsESDandhence Real-world Size #Dim Rate% Pattern AvgLength
1.5k 0.7
weonlyreportSHESD.NormA[6],SAND[7]andIDK[55]learna Yahoo[35] 1 Contextual -
|     |     |     |     | Twitter[25] | 14k 1 0.7 Global | -   |
| --- | --- | --- | --- | ----------- | ---------------- | --- |
normalmodel(clusteringthedistributionofnormalpatterns)and Stock[57] 10k 1 5-25 Mixed -
tnioP
thesimilaritydistancetothenormalmodelisusedastheanomaly Tao[57] 568k 3 5-25 Mixed -
|     |     |     |     | SMTP[38] | 95k 3 0.03 Mixed     | -   |
| --- | --- | --- | --- | -------- | -------------------- | --- |
|     |     |     |     | DLR[67]  | 23k 9 2.2 Contextual | -   |
scoresfortargetsubsequences.SANDfurtherextendsthek-Shape
|     |     |     |     | ECG[67] 112k | 32 16.3 Global | -   |
| --- | --- | --- | --- | ------------ | -------------- | --- |
clustering[46]sothatthenormalmodelcanbeupdatedfromone
|     |     |     |     | Power[30] | 35k 1 8.6 Seasonal | 750 |
| --- | --- | --- | --- | --------- | ------------------ | --- |
batchtothenext,makingitselfanonlinemethod.IDKusesIsol- ecneuqesbuS Sed[7] 100k 1 3.0 Global 64
|     |     |     |     | Taxi[53] | 10k 1 10 Global+Seasonal | 207 |
| --- | --- | --- | --- | -------- | ------------------------ | --- |
ationDistributionalKernel[56]tocomputethesimilarity.PBAD
|     |     |     |     | Machine[53] | 22k 1 10 Global+Seasonal | 567 |
| --- | --- | --- | --- | ----------- | ------------------------ | --- |
[19]andGrammarViz[50]userulestoextractthenormalpatterns. Exercise[19] 10k 3 15.1 Mixed 140.2
|     |     |     |     | Exathlon[29] | 3k 19 17.4 Mixed | 64.1 |
| --- | --- | --- | --- | ------------ | ---------------- | ---- |
Theformerpresentsfrequentpatternminingresearch[68]tofind
|     |     |     |     | Swat[41] | 90k 51 12 Mixed | 317.2 |
| --- | --- | --- | --- | -------- | --------------- | ----- |
frequentpatterns(whosesupportisgreaterthan𝜃 Smd[52] 28k 38 9.5 Mixed 336.8
𝑠𝑢𝑝)whilethe
|     |     |     |     | Synthetic | Size #Dim Rate% Pattern | AvgLength |
| --- | --- | --- | --- | --------- | ----------------------- | --------- |
latterimplementstwogrammarinductionmethods[33,43]togen-
|     |     |     |     | tnioP Uni-point-g 1k-100k | 1 5-25 Global | -   |
| --- | --- | --- | --- | ------------------------- | ------------- | --- |
erate a context-freegrammar. LRRDS [26] usesrecurrenceplot Uni-point-c 1k 1 5-25 Contextual -
[69]andextractsthesubsequencesetfromthelocalrecurrence Mul-point 1k-100k 32 5-25 Global -
|     |     |     |     | Uni-sub-g 1k-100k | 1 5-25 Global | 50  |
| --- | --- | --- | --- | ----------------- | ------------- | --- |
rates(LREC)[63].Theanomalyscoreiscomputedbycomparing
|     |     |     |     | ecneuqesbuS Uni-sub-s 1k-100k | 1 5-25 Seasonal | 50  |
| --- | --- | --- | --- | ----------------------------- | --------------- | --- |
|     |     |     |     | Uni-sub-t 1k-100k             | 1 5-25 Trend    | 50  |
similaritiesbetweenstatisticsintheLRECcurve. Mul-sub-g 1k-100k 3/50 5-25 Global 50
|     |     |     |     | Mul-sub-s 1k-100k | 3/50 5-25 Seasonal | 50  |
| --- | --- | --- | --- | ----------------- | ------------------ | --- |
|     |     |     |     | Mul-cor-g         | 5k 3 10 Global     | 50  |
3.3 DeepLearning-basedMethods
|     |     |     |     | Mul-ncor-g | 5k 3 10 Global | 50  |
| --- | --- | --- | --- | ---------- | -------------- | --- |
Recently,severaldeeplearning-basedmethodshavebeenproposed
todetectanomaliesintimeseries[15].Variousarchitectureshave
POT[51](selectingthresholdautomatically)andpoint-adjust[62]
beendevelopedtocapturelatentinformationfromtemporaland
(modifyingpredictionsbeforeevaluation)tomakeafaircompar-
dimensionalaspects.
ison.AnalysisonthesechangescanbefoundinSection4.3.4and
Forreconstructionbasedmethods,afterlearningamodelofthe
4.3.5,respectively.The’Code’columninTable2showstheoriginal
normaldatainthelatentspace,thetesttimeseriesisfirsttrans-
languageinwhicheachmethodwaswritten,whilethe‘Speedup’
formedtothelatentspaceandthenreconstructedtothedataspace.
columnshowstheincreaseinefficiencyafterourimplementation
Finally,thereconstructedvaluesthathavealargerdistancefrom
(exceptSAND,thedecompositiontoolsrunsfarmoreslowly).We
observationswillbeidentifiedasanomalies.OmniAnomaly(Omni)
verifythatthereportedanomaliesofthemethodsbeforeandafter
[52]proposesastochasticrecurrentneuralnetworkbyusingGRU
ourrefactorareidenticalandguaranteereproducibility.
tocapturecomplextemporaldependenciesbetweenmultivariate
observationsindataspace,andavariationalautoencoder(VAE)
4 EXPERIMENT
tomapobservationstostochasticvariables.USAD[3]presentsan
Thissectionwillfirstshowtheexperimentalsettings.Then,insights
encoder-decoderarchitecturewithinatwo-phaseadversarialtrain-
foundoverintra-classandinter-classcomparisonsareexplained.
ingsystem(GAN).BeatGAN[39]alsoprovidesaninterpretable
Similarto[49],wetryourbesttodescribefindingsfromexperi-
| method that | combines autoencoders | and GAN | to detect anom- |     |     |     |
| ----------- | --------------------- | ------- | --------------- | --- | --- | --- |
aloussubsequences. RCoder[1]introducesanencoder-decoder mentalresults.However,ifamethodperformspoorlyinourevalu-
ation,itdoesnotnecessarilymeanthatitstheoryisbad,because
frameworktolearntheboundsofreconstructedsignals.Thekey
themetricandthesituationarequitedifferent.
differenceisthatitssizeoflatentspaceis1andaspectralana-
| lysis with | Fast Fourier Transform | is then applied. | TranAD [58] |     |     |     |
| ---------- | ---------------------- | ---------------- | ----------- | --- | --- | --- |
4.1 Settings
combinestransformer-basedencoder-decodernetworkswithad-
versarialtraining.Predictionbasemethodslearnamodelfromnor- WerunexperimentsonaWindows10serverwitha3.79GHz12
CoreCPUand128GBRAM.Deep-learningmethodsareemployed
maldataandthenpredictsthetargetvaluebasedonthemodeland
observationsbeforethetargettime.Finally,thedifferencebetween withGPUwithoutcomparingtheefficiency.Othersaretestedunder
thepredictedvalueandobservationisusedastheanomalyscore. asingle-coreenvironmenttocomparerunningtimes.
| GDN [17] | employs the Graph | Neural Network | to learn the de- |     |     |     |
| -------- | ----------------- | -------------- | ---------------- | --- | --- | --- |
4.1.1 Datasets. Weemploywidelyusedreal-worlddatasetswith
pendencyrelationshipbetweendifferentdimensionsandusegraph
labelsasbenchmarks,7withpointand8withsubsequenceanom-
attentionmechanismtomakepredictions.
alieswithvarioussizes,dimensions,anomalyrates(lengths)and
patterns.Wealsogeneratesyntheticdatasetswhosebasetypeis
3.4 ImplementationNotes
sine,withdifferentanomalypatterns(SeeSection2.2.3)according
Somewidelyusedsystems,suchasApacheIoTDB[59],canonly totheguidelinein[31]forthecaseoftheunreliabilityofanomaly
supportJAVAasbuilt-infunctions,andhencewerewriteallnon- labels[61].Forpointanomaly,weinjectglobal(g)andcontextual(c)
deeplearningmethodsinJAVA(exceptNormA,theexistingtoolkit outliers.Forsubsequenceanomaly,weaddglobal(g),seasonal(s)
runsdifferently).WealsorefactorNETS,STARE,GrammarViz,and andtrend(t)outliers,respectively.Theaveragelengthissetto50by
SHESD(inJAVA)anddeeplearningmethods(inPython)withour default,soanyalgorithmisapplicable.Inordertoavoidtheeffect
datastructurestoavoidpotentialimpactonefficiency.Weremove ofrandomness,werunexperimentsonsyntheticdatasets10times
487

|     | NETS | SHESD USAD | Omni |     | PBAD SAND | MERLIN | NormA |     |     |     |     |
| --- | ---- | ---------- | ---- | --- | --------- | ------ | ----- | --- | --- | --- | --- |
Stare TranAD GDN RCoder LRRDS NP GrammarViz IDK NETS SHESD USAD Omni
|     |     |     |     | 103 |     |     |     |     | Stare TranAD | GDN RCoder |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------ | ---------- | --- |
103
| )s( tsoc emiT |     |     |     | )s( tsoc emiT 102 |     |     |     | 1.00 |     | 100 |     |
| ------------- | --- | --- | --- | ----------------- | --- | --- | --- | ---- | --- | --- | --- |
101
|      |     |     |     | 101 |     |     |     |                |     | )s( tsoc emiT |     |
| ---- | --- | --- | --- | --- | --- | --- | --- | -------------- | --- | ------------- | --- |
| 10−1 |     |     |     |     |     |     |     | erusaem-F 0.75 |     |               |     |
100
0.50
| 10−3 | Yahoo | Twitter SMTP | DLR | 0   | Power Sed | Taxi | Machine |     |     | 10−1 |     |
| ---- | ----- | ------------ | --- | --- | --------- | ---- | ------- | --- | --- | ---- | --- |
0.25
|     |     | Dataset                          |     |     |                                  | Dataset |     |     |     |     |     |
| --- | --- | -------------------------------- | --- | --- | -------------------------------- | ------- | --- | --- | --- | --- | --- |
|     |     | (a) Time cost with point anomaly |     |     | (b) Time cost with range anomaly |         |     |     |     |     |     |
0.00
10−2
|     |     |     |     |     |     |     |     | 5 7.5 | 1012.51517.52022.525 | 5 7.5 1012.51517.52022.525 |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ----- | -------------------- | -------------------------- | --- |
Figure3:Timecostovervariousdatasets Anomaly rate % Anomaly rate %
|     |     |     |     |     |     |     |     | (a) F-measure on Uni-poing-g |     | (b) Time cost on Uni-point-g |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------------------------- | --- | ---------------------------- | --- |
withdifferentgeneratingseedsandreporttheaverageresults.The
summaryofalldatasetscanbefoundinTable3.
4.1.2 EvaluationMetrics.
|                 | Accuracy. | Differentmetricsareusedwithrespecttoanomaly |               |     |                          |     |     |     |     |     |     |
| --------------- | --------- | ------------------------------------------- | ------------- | --- | ------------------------ | --- | --- | --- | --- | --- | --- |
| types.𝑃𝑟𝑒𝑐𝑖𝑠𝑖𝑜𝑛 |           | =                                           | 𝑇 𝑃 and𝑅𝑒𝑐𝑎𝑙𝑙 |     | = 𝑇 𝑃 𝐹𝑁[2]areutilizedas |     |     |     |     |     |     |
|                 |           | 𝑇𝑃                                          | + 𝐹𝑃          |     | 𝑇𝑃 +                     |     |     |     |     |     |     |
pointmetrics,whereTP,FP,FNarethenumberoftruepositives, Figure4:Varyingrateson(a-b)Uni-point-g(c-d)Tao
falsepositives,andfalsenegatives,respectively.Wechooseare-
centmetricproposedforsubsequenceanomalywhichfocuseson
theoverlapofpredictedanomalyandtrueanomaly[53]asrange
(orsubsequence)metric.Specifically,givenasetofrealanomaly Point.WecanseethatNETSalwayshavehighaccuracyacross
ranges𝑅 {𝑅 ,...,𝑅 }andasetofpredictedanomalyranges alldatasets.Starereliesheavilyontheparameterindicatingthe
|     |     | = 1 | 𝑁𝑟  |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
𝑁
𝑃 {𝑃 ,...,𝑃 },wehave𝑅𝑒𝑐𝑎𝑙𝑙 𝑇(𝑅,𝑃) ∑︁ 𝑟 𝑅𝑒𝑐 𝑎 𝑙𝑙𝑇(𝑅𝑖,𝑃) numberofanomalypointsineachwindow.Complexdistributions
|     | = 1 | 𝑁𝑝  |     |     | = 𝑖 | = 1 𝑁 | and |                                                          |     |     |     |
| --- | --- | --- | --- | --- | --- | ----- | --- | -------------------------------------------------------- | --- | --- | --- |
|     |     |     |     |     |     | 𝑟     |     | ofrealanomaliesresultsinitsrelativelyloweraccuracy.Asfor |     |     |     |
∑︁ 𝑁 𝑝
𝑃𝑟𝑒𝑐𝑖𝑠𝑖𝑜𝑛 𝑇(𝑅,𝑃)= 𝑖 𝑃𝑟𝑒𝑐 𝑖𝑠 𝑖𝑜𝑛𝑇(𝑅,𝑃𝑖) deeplearningmethods,allexceptRCoderareclosetoNETSon
|                              |     |     | = 1 | 𝑁        | .Ingeneral,thedefaultset- |                    |     |                                                       |                  |                       |           |
| ---------------------------- | --- | --- | --- | -------- | ------------------------- | ------------------ | --- | ----------------------------------------------------- | ---------------- | --------------------- | --------- |
|                              |     |     |     | 𝑝        |                           |                    |     | Yahoo and                                             | perform worse on | others. RCoder, which | cannot be |
| tingFlatbias[53]isemployed.𝐹 |     |     |     | −𝑚𝑒𝑎𝑠𝑢𝑟𝑒 |                           | 2∗𝑃𝑟𝑒𝑐𝑖𝑠𝑖𝑜𝑛∗𝑅𝑒𝑐𝑎𝑙𝑙 |     |                                                       |                  |                       |           |
|                              |     |     |     |          | =                         | 𝑃𝑟𝑒𝑐𝑖𝑠𝑖𝑜𝑛+𝑅𝑒𝑐𝑎𝑙𝑙   |     | usedforunivariatedataduetoitsmechanism,performsbeston |                  |                       |           |
appliesforbothmetrics.
ECGwith32dimensionsbutpoorlyonotherswhosedimensions
aresmallerthannine.Overall,itissurprisingthatdeeplearning
|     | Efficiency. | Apartfromloadingthedatafromthefileandresult |     |     |     |     |     |     |     |     |     |
| --- | ----------- | ------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
methodsdonotbehavewell.Thepossiblereasonisthatthenumber
evaluation,thetotaltimeofalltheotherprocedureswillbeadded
ofdatainstancesanddimensionsarenotsufficienttolearnagood
andreportedasthetimecostofthetargetmethod.
model.Figure3(a)showstheefficiencyofeachmethod.Weonly
showthefirst4datasets,sinceothersaresimilar.NETScomputes
| 4.1.3 | ParameterSearch. |     | Inordertocomparemethodsfairlyand |     |     |     |     |     |     |     |     |
| ----- | ---------------- | --- | -------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- |
precisely(underbestconfigurations),thoughallofthemareunsu- onaselectedsub-dimension,makingitthemostefficientmethod.
pervisedmethods,westillemployasystematic(hyper)-parameter TranADshowsthebesttimeefficiencyduetoitsarchitecture.
searchprocess.Specifically,wedesignasearchspaceforeachpara- Sub.MultivariatemethodsPBADandBeatGANachievehigher
meter(includingthreshold)accordingtothesuggestionsintheir accuracythanunivariatemethodsonmultivariatedata.Inpartic-
ular,univariatemethodshavehighrecallbutverylowprecision.
paper,e.g.,forUSADwetunethelatentsizewith{2,5,10,20}[3]
orbasedonthedistributionsofthetargetdataset.Wethensplit LRRDSperformsbetterthanPBADandBeatGANonlyonSed.This
thedatasetintotraining,validationandtestsetwitha‘4:1:5’ra- isbecausethemeanofabnormalpatternsinSedisobviouslylower
tio.It’sworthnotingthatthetrainingsetsareanomaly-free,as thanthatofnormalpatterns,soLRRDSiseasiertoidentifywith
requiredby[3,17,52,58].Theparameterwiththebestperformance embeddingtechniquesthansimplemeanandlengthfeatures.Asfor
invalidationsetwillbesettledfortesting. univariatemethods,NormAcanperformquitewellonallunivariate
data.MERLINperformsexceptionallywellonPower,showingthe
4.2 Intra-classComparisons capabilityoverseasonality.SANDdoesnotperformwellonlong
anomalies(e.g.,thelengthoftheanomalyinPoweris750).Ithasto
Asmentionedearlier,articlespresentingnewmethodsofteninclude
decomposealargematrixmanytimesiftheanomalyhasalarge
suchcomparisons,butthevarietyofcaseswithrespecttofactors
length.Wenotethatittakesmuchmoretimewhenthelengthof
| and | datasets | is often | limited. | For simplicity, |     | we use | "Point" to |     |     |     |     |
| --- | -------- | -------- | -------- | --------------- | --- | ------ | ---------- | --- | --- | --- | --- |
denote the results of point methods and "Sub" of subsequence theanomalyisgreaterthan100.BothGrammarVizandPBADuse
apatternminingapproachtoidentifysequencepatterns,sothey
methods."Summary"standsforthetake-awayconclusions.
arecomparableonunivariatedatasets.
4.2.1 VaryingDatasets. Wefirstevaluatetheperformanceofall Summary.(1)Thereisnosuper-algorithmthatissuitableforall
methodsondifferentdatasetswiththeirbestparameters.Toobtain cases.(2)Givenproperparameters,NETScanperformbestinmost
theresultsoftheunivariatemethodsonmultivariatedata,werun cases.(3)PBADandBeatGANhavebetteroverallaccuracybutcost
themseparatelyoneachdimension(similarto[52]),andcombine moretime.(4)Deeplearningmethodsdonotoutperformotherson
allthereportedanomalies.ResultsareshowninTable4. datasetswithcomplexanomalypatterns.
488

Table4:Accuracyovervariousdatasets
|         | NETS |     | Stare | SHESD |     | TranAD |     | USAD |     | GDN |     | Omni |     | RCoder |
| ------- | ---- | --- | ----- | ----- | --- | ------ | --- | ---- | --- | --- | --- | ---- | --- | ------ |
| Dataset | P R  | F   | P R F | P     | R F | P R    | F   | P R  | F   | P R | F   | P R  | F   | P R F  |
Yahoo 0.727 1 0.842 0.429 0.375 0.400 1 0.625 0.769 0.368 0.875 0.519 0.368 0.875 0.518 0.368 0.875 0.519 0.471 1 0.64 - - -
Twitter 0.739 0.878 0.802 0.203 0.959 0.335 0.260 0.176 0.210 0.737 0.189 0.301 0.205 0.412 0.274 0.484 0.419 0.449 0.079 0.878 0.145 - - -
SMTP 0.400 0.375 0.387 0.294 0.313 0.303 0.001 1 0.003 0.001 0.188 0.003 0.001 0.222 0.002 0.004 0.022 0.007 0.250 0.375 0.300 0.001 0.312 0.001
DLR 0.468 0.424 0.445 0.109 0.517 0.179 0.061 1 0.115 0.115 0.224 0.152 0.115 0.224 0.154 0.118 0.852 0.060 0.180 0.180 0.180 0.030 0.252 0.053
ECG 0.484 0.441 0.462 0.239 0.267 0.252 0.373 0.430 0.399 0.160 0.557 0.248 0.280 0.293 0.286 0.232 0.328 0.272 0.347 0.165 0.224 0.640 0.426 0.512
Dataset PBAD LRRDS BeatGAN SAND NP MERLIN GrammarViz NormA IDK
|     | P R | F P | R F P | R   | F P | R F | P R | F P | R   | F P | R F | P R | F   | P R F |
| --- | --- | --- | ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----- |
Power 0.262 0.758 0.389 0.415 0.248 0.310 0.498 0.340 0.404 0.159 0.156 0.157 0.575 0.575 0.575 0.936 0.998 0.966 0.453 0.222 0.298 0.868 0.810 0.838 0.343 0.244 0.285
Sed 0.310 0.800 0.446 0.597 0.972 0.739 0.690 0.723 0.706 0.657 0.769 0.708 0.695 0.814 0.750 0.505 0.829 0.627 0.435 0.533 0.479 0.435 0.669 0.527 0.938 0.938 0.938
Taxi 0.143 0.664 0.235 0.164 0.463 0.242 0.354 0.437 0.391 0.250 0.242 0.246 0.468 0.498 0.482 0.460 0.460 0.460 0.333 0.135 0.192 0.441 0.533 0.482 0.498 0.373 0.427
Machine 0.227 0.500 0.312 0.073 0.500 0.127 0.521 0.471 0.495 0.100 0.106 0.103 0.009 0.018 0.012 0.143 0.429 0.215 0.197 1 0.33 0.171 0.332 0.226 0.429 0.454 0.441
Exercise 0.495 1 0.662 0.283 0.656 0.396 0.756 0.760 0.758 0.293 0.672 0.408 0.309 0.983 0.470 0.377 0.971 0.543 0.553 0.745 0.635 0.292 0.743 0.420 0.171 0.405 0.245
Exathlon 0.515 0.856 0.643 0.197 0.341 0.250 0.299 0.694 0.418 0.206 1 0.341 0.149 0.993 0.259 0.200 1 0.334 0.147 1 0.256 0.095 0.849 0.170 0.169 1 0.289
Swat 0.185 0.566 0.279 0.286 0.124 0.173 0.340 0.233 0.276 0.082 0.993 0.151 0.055 1 0.104 - - - 0.137 1 0.242 0.063 0.529 0.113 0.041 1 0.079
Smd 0.294 0.303 0.298 0.676 0.098 0.171 0.273 0.235 0.253 0.070 0.925 0.129 0.082 0.980 0.151 0.063 0.732 0.116 0.018 1 0.035 0.088 0.742 0.157 0.085 0.799 0.154
|     | PBAD  | BeatGAN | NP     | GrammarViz |     | IDK |     |      | NETS  | SHESD  |     | USAD | Omni   |     |
| --- | ----- | ------- | ------ | ---------- | --- | --- | --- | ---- | ----- | ------ | --- | ---- | ------ | --- |
|     | LRRDS | SAND    | MERLIN | NormA      |     |     |     |      | Stare | TranAD |     | GDN  | Rcoder |     |
| 1.0 |       |         |        |            |     |     |     | 1.00 |       |        |     | 101  |        |     |
102
0.8
| erusaem-F |     |     | )s( tsoc emiT |     |     |     | erusaem-F | 0.75 |     |     | )s( tsoc emiT | 100 |     |     |
| --------- | --- | --- | ------------- | --- | --- | --- | --------- | ---- | --- | --- | ------------- | --- | --- | --- |
| 0.6       |     |     | 101           |     |     |     |           |      |     |     |               |     |     |     |
|           |     |     |               |     |     |     |           | 0.50 |     |     | 10−1          |     |     |     |
0.4
|     |     |     | 100  |     |     |     |     |      |     |     | 10−2 |     |     |     |
| --- | --- | --- | ---- | --- | --- | --- | --- | ---- | --- | --- | ---- | --- | --- | --- |
| 0.2 |     |     |      |     |     |     |     | 0.25 |     |     |      |     |     |     |
| 0.0 |     |     | 10−1 |     |     |     |     | 0.00 |     |     | 10−3 |     |     |     |
5 7.5 1012.51517.52022.525 5 7.5 1012.51517.52022.525 1k 2k 5k 10k 20k 50k 100k 1k 2k 5k 10k 20k 50k 100k
|     | Anomaly rate % |     |     | Anomaly rate % |     |     |     |     | Data size |     |     |     | Data size |     |
| --- | -------------- | --- | --- | -------------- | --- | --- | --- | --- | --------- | --- | --- | --- | --------- | --- |
(a) F-measure on Uni-sub-g (b) Time cost on Uni-sub-g (b) Time cost on Uni-point-g
(a) F-measure on Uni-poing-g
| 0.8 |     |     | 101 |     |     |     |     |     |     |     |     | 103 |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
1.00
| 0.6       |     |     | )s( tsoc emiT |     |     |     |           | 0.75 |     |     | )s( tsoc emiT |     |     |     |
| --------- | --- | --- | ------------- | --- | --- | --- | --------- | ---- | --- | --- | ------------- | --- | --- | --- |
| erusaem-F |     |     |               |     |     |     | erusaem-F |      |     |     |               | 101 |     |     |
| 0.4       |     |     |               |     |     |     |           | 0.50 |     |     |               |     |     |     |
10−1
| 0.2 |     |     |     |     |     |     |     | 0.25 |     |     |      |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ---- | --- | --- | ---- | --- | --- | --- |
| 0.0 |     |     | 100 |     |     |     |     | 0.00 |     |     | 10−3 |     |     |     |
5 7.5 1012.51517.52022.525 5 7.5 1012.51517.52022.525 1k 2k 5k 10k 20k 50k 100k 1k 2k 5k 10k 20k 50k 100k
|     | Anomaly rate % |     |     | Anomaly rate % |     |     |     |     | Data size |     |     |     | Data size |     |
| --- | -------------- | --- | --- | -------------- | --- | --- | --- | --- | --------- | --- | --- | --- | --------- | --- |
(c) F-measure on Mul-sub-s (d) Time cost on Mul-sub-s (c) F-measure on TAO (d) Time cost on TAO
Figure5:Varyingrateson(a-b)Uni-sub-g(c-d)Mul-sub-s Figure6:Varyingsizeson(a-b)Uni-point-g(c-d)Tao
| 4.2.2 | VaryingAnomalyRate𝑎%. |     | [61]claimsthatcurrentdatasets |     |     |     |                  |     |     |                                      |     |     |     |     |
| ----- | --------------------- | --- | ----------------------------- | --- | --- | --- | ---------------- | --- | --- | ------------------------------------ | --- | --- | --- | --- |
|       |                       |     |                               |     |     |     | timecomplexityof |     |     | MERLINandGrammarVizislinearlyrelated |     |     |     |     |
containtoofewanomaliesforevenasimplemethodtofindthem.
tothenumberofanomaloussubsequences.Whenwecomparethe
However,themajorityofthedatashouldbenormal.Therefore,we resultsofthedifferentmethods,wefindthatmostofthem,suchas
varyanomalyratesfrom5%to25%totestthesensitivityofthe
PBAD,remainstableorperformbetterwhentheanomalyrateis
methodsonsyntheticdatasets.Thedatasizeis10kforpointand
lower,butgraduallybecomeworseastheanomalyrateincreases.
5kforsubsequenceanomalies.
Incontrast,LRRDSandBeatGANperformsevenbetteratahigher
Point.AsillustratedinFigures4(a,c),allnon-deeplearningmeth-
anomalyrate,whichisduetothereductionoffalsepositivescaused
odsarerelativelystable.NETSperformabitworseonTaowhenthe byroughrecognitionofanomalypoint.
anomalyrateachieves25%.Sinceitisdifficulttosetanappropriate Summary.(1)Methodsarestablewhenanomalyisrare(<25%),
| 𝜃 𝑘 and𝜃 | 𝑅 toidentifytheanomalouspointsbecausetheyalsohave |     |     |     |     |     |     |     |     |     |     |     |     |     |
| -------- | ------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
whichisdifferenttothestatementsaboutrandomdetectionin[44].
asimilarnumberofneighborsasnormalpoints.Onthecontrary,
(2)Amethodmayperformbetterasanomalyrateincreasessince
mostdeeplearningmethodsachieveabetterresultwithincreasing
thelargenumberofthereportedfalsepositivescanbecometrue
anomalyrate.ThismaybebecauseTranAD,USAD,andGDNfailto positives.(3)Anomalyrateshowslittleeffectontheefficiency.
learnagoodmodel(evenwiththebestparameterviagridsearch)
andtendtopredictmorepointsasanomalies.Therefore,morefalse 4.2.3 VaryingDataSize𝑛. Tocheckthesensitivityandscalability
positivesbecometruepositiveswhentheanomalyrateincreases. againstthedatasize,werunexperimentsbyvaryingdatasizes
OminiandRCodermanagetolearnabettermodelandperform from1kto100konrealandsyntheticdatasetswith10%anomalies.
wellonUni-point-gandTao,respectively. Point.TheresultsinFigures6(b,d)showthatallmethodscost
Sub.Figures5(b,d)showthat,thetimecostsofallmethodsre- moretimeasthedatasizeincreases.Intermsofaccuracy,they
mainconstantforbothunivariateandmultivariatedata,except showconsistentresultsagainstthedatasize.ItisnotedthatSHESD
forMERLINandGrammarViz,whichisduetothefactthatthe makesexceptionsinsomecases.StareandNETSarethetwofastest
489

|     | PBAD  | BeatGAN |     | NP GrammarViz |     | IDK | NETS  | SHESD  | Rcoder GDN |     |      |      |             |
| --- | ----- | ------- | --- | ------------- | --- | --- | ----- | ------ | ---------- | --- | ---- | ---- | ----------- |
|     |       |         |     |               |     |     | Stare | TranAD | USAD Omni  |     |      | NETS | Stare SHESD |
|     | LRRDS | SAND    |     | MERLIN NormA  |     |     | 1.00  |        |            |     | 10−1 |      |             |
104
| 1.0 |     |     |     |     |     |     | 0.75 |     |     | )s(tsoc emiT |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ---- | --- | --- | ------------ | --- | --- | --- |
erusaem-F
| 0.8       |     |     | )s( tsoc emiT |     |     |     |      |     |     |     |     |     |     |
| --------- | --- | --- | ------------- | --- | --- | --- | ---- | --- | --- | --- | --- | --- | --- |
| erusaem-F |     |     |               | 102 |     |     | 0.50 |     |     |     |     |     |     |
0.6
0.25
| 0.4 |     |     |     |     |     |     |     |     |     |     | 10−2 |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---- | --- | --- |
100
|     |     |     |     |     |     |     | 0.00 | Global                 | Contextual |     |     | Global                 | Contextual |
| --- | --- | --- | --- | --- | --- | --- | ---- | ---------------------- | ---------- | --- | --- | ---------------------- | ---------- |
| 0.2 |     |     |     |     |     |     |      | Anomaly pattern        |            |     |     | Anomaly pattern        |            |
|     |     |     |     |     |     |     |      | (a) F-measure on Stock |            |     |     | (b) Time cost on Stock |            |
0.0
1k 2k 5k 10k 20k 50k 100k 1k 2k 5k 10k 20k 50k 100k PBAD SAND MERLIN NormA PBAD SAND MERLIN NormA
Data size Data size LRRDS NP GrammarViz IDK LRRDS NP GrammarViz IDK
|     | (a) F-measure on Uni-sub-g |     |     | (b) Time cost on Uni-sub-g |     |     | BeatGAN |     |     |     |     |     |     |
| --- | -------------------------- | --- | --- | -------------------------- | --- | --- | ------- | --- | --- | --- | --- | --- | --- |
1.00
| 1.0           |     |     |               | 103 |     |     |                |     |     |              |     |     |     |
| ------------- | --- | --- | ------------- | --- | --- | --- | -------------- | --- | --- | ------------ | --- | --- | --- |
|               |     |     |               |     |     |     | erusaem-F 0.75 |     |     | )s(tsoc emiT | 101 |     |     |
| erusaem-F 0.8 |     |     | )s( tsoc emiT | 102 |     |     | 0.50           |     |     |              |     |     |     |
100
| 0.6 |       |                |      | 101       |         |          | 0.25        |                          |       |     |        |                          |       |
| --- | ----- | -------------- | ---- | --------- | ------- | -------- | ----------- | ------------------------ | ----- | --- | ------ | ------------------------ | ----- |
| 0.4 |       |                |      | 100       |         |          | 0.00 Global | Seasonal                 | Trend |     | Global | Seasonal                 | Trend |
|     |       |                |      |           |         |          |             | Anomaly pattern          |       |     |        | Anomaly pattern          |       |
|     |       |                |      |           |         |          |             | (c) F-measure on Uni-sub |       |     |        | (d) Time cost on Uni-sub |       |
| 0.2 |       |                |      | 10−1      |         |          |             |                          |       |     |        |                          |       |
|     | 1k 2k | 5k 10k 20k 50k | 100k | 1k 2k 5k  | 10k 20k | 50k 100k |             |                          |       |     |        |                          |       |
|     |       | Data size      |      | Data size |         |          |             |                          |       |     |        |                          |       |
(c) F-measure on Mul-sub-s (d) Time cost on Mul-sub-s Figure9:Varyingpatternson(a-b)point(c-d)subsequence
Figure7:Varyingsizeson(a-b)Uni-sub-g(c-d)Mul-sub-s
|     |     |     |     |     |     |     |            | 9          | 8 7 | 6 5 | 4 3 | 2 1      |     |
| --- | --- | --- | --- | --- | --- | --- | ---------- | ---------- | --- | --- | --- | -------- | --- |
|     |     |     |     |     |     |     |            | MERLIN 8.9 |     |     |     | 1.0 NP   |     |
|     |     |     |     |     |     |     |            | LRRDS 8.1  |     |     |     | 2.4 SAND |     |
|     |     |     |     |     |     |     | BeatGAN    | 6.9        |     |     |     | 3.2 IDK  |     |
|     |     |     |     |     |     |     | GrammarViz | 5.9        |     |     |     | 3.4 PBAD |     |
|     |     |     |     |     |     |     |            | NormA 5.2  |     |     |     |          |     |
Figure10:Criticaldifferencediagramonsubg
|     |     |     |     |     |     |     | 4.2.4 VaryingDataDimension|𝐷|. |     |     |     | Hereweperformexperiments |     |     |
| --- | --- | --- | --- | --- | --- | --- | ------------------------------ | --- | --- | --- | ------------------------ | --- | --- |
onrealdatasetsbyvaryingthedimensionsofthedata.
Point.Figures8(a-b)showthatallmethodshavebetterresultswith
|     |     | PBAD | LRRDS | BeatGAN |     |     |     |     |     |     |     |     |     |
| --- | --- | ---- | ----- | ------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
0.3 largerdimensions.Besides,weneedtoadjusttheparameter𝜃 𝑅with
102
)s( tsoc emiT thechangeindimensiontogetareasonableresult.Wealsoretrain
erusaem-F 0.2
themodelsofthedeeplearningmethods,whichresultsinallbut
|     |     |     |     | 101 |     |     | RCoderremainingstableasthedatadimensionincreases.RCoder |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ------------------------------------------------------- | --- | --- | --- | --- | --- | --- |
0.1
hasmorereferencedataandestimatorswithmoredatadimensions,
100 whichsignificantlyincreasesitsaccuracy.Intermsofefficiency,all
| 0.0 | 1 5 | 10 20 30 40 | 50  | 1 5 10 | 20 30 | 40 50 |     |     |     |     |     |     |     |
| --- | --- | ----------- | --- | ------ | ----- | ----- | --- | --- | --- | --- | --- | --- | --- |
Data dimension Data dimension distance-basedmethodscostmoretimeasthedimensionincreases,
|     | (c) F-measure on Swat |     |     | (d) Time cost on Swat |     |     |     |     |     |     |     |     |     |
| --- | --------------------- | --- | --- | --------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
sinceitismoreexpensivetocomputethedistance.
Sub.Theresultofthesubsequenceanomalycanbecheckedin
Figure8:Varyingdimensionson(a-b)ECG(c-d)Swat
Figure8(c-d).LRRDSappliesdimensionalcompressionandexhibits
greatscalability.Incontrast,PBADmustextractthefeaturesineach
dimension,whichresultsinasignificantlyhighertimeoverheadas
methods.Thelattertwoalgorithmstakeadvantageofthe“seteffect"
thedimensionincreases.Sincetheanomalyislocalizeddifferently
thatskipsadditionalupdateswhennewdataarrives.
ineachdimensionofSwat,itisnotsurprisingthatperformance
Sub.AscanbeseeninFigure7,mostpattern-basedmethodsshow varieswidelyacrossallmethods,includingBeatGAN.
unstableresultsforsmall(e.g.,5k)becauseitisdifficulttoextract Summary.(1)LRRDSscaleswellwithdatadimension,whileNETS,
patterns.Whenthedataislargeenough,theresultsofthesub-
Stare,andPBADaresignificantlyaffectedbyit.(2)Thesparsity
sequencemethodsareusuallyquiteconsistent.LRRDSreflectsthe
problemcanbehandledbyagoodparametersetting.(3)Sincethe
| sametrendinSection4.2.2.Wedonotreporttheresultsof |     |     |     |     |     | LRRDS |     |     |     |     |     |     |     |
| ------------------------------------------------- | --- | --- | --- | --- | --- | ----- | --- | --- | --- | --- | --- | --- | --- |
numberofestimatorsincreaseswiththedatadimension,RCoder
after20kbecauseitisoutofmemoryanddonotreporttheresults achievesbetterresultswithhigherdimensions.(4)NETSisrecom-
ofMERLINafter10kbecauseittakesmorethanadaytorun.Both
mendedwhendatadimensionislimited(<30).(5)RCoderisagood
ofthemshowpoorscalability.
choicewhendatadimensionislarge(>30).
Summary.(1)Stare,NETS,andNormAhavegoodefficiency(also
referredtotheresultsinFigure3).(2)Smalldatasize(<10k)may 4.2.5 VaryingAnomalyPatterns. Finally,wetesttheselectedal-
leadtounstableresultsforsubsequencemethods.(3)Werecom- gorithmsfordifferentpatternsofanomalies.
mendIDKwhenthedatasizeismorethan50kbecauseitprovides Point.AsshowninFigures9(a-b),allmethodsachievebetterac-
goodscalabilityandstableperformance. curacyforglobalanomaly(0.618)thancontextualanomaly(0.551),
490

which is consistent with the common sense. They have similar NETS Stare SHESD
efficiencyforthesetwoanomalypatterns.
|     |     |     |     |     |     |     | 0.4 |     |     | )sm( tsoc emiT |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | -------------- | --- | --- |
Sub.TheresultforthesubsequencecaseisshowninFigures9(c-d). erusaem-F 103
| Theaveragef-measuresare0.550,0.619,and0.398forglobal,sea- |     |     |     |     |     |     | 0.3 |     |     |     |     |     |
| --------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
sonal,andtrendanomaly,respectively.Consistentwithprevious
|     |     |     |     |     |     |     | 0.2 |     |     | 101 |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
observations,PBADandNormAhasstableperformanceacrossall
0.1
patterns.SANDandNPperformparticularlywellonglobalandsea- 200 1000 2000 5000 800010000 200 1000 2000 5000 800010000
|     |     |     |     |     |     |     |     | Window size |     |     | Winidow size |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------- | --- | --- | ------------ | --- |
sonaloutliers.DetectingtrendoutliersischallengingforBeatGAN (c) F-measure on ECG (d) Time cost on ECG
andIDK,reflectingtheneedforimprovementofnon-stationary 0.6 104
timeseries.Tofindoutwhethertherearemethodsthatfitallpat- )sm( tsoc emiT
erusaem-F
| terns,weapplytheFriedmantest[20]andapost-hocWilcoxon |     |     |     |     |     |     | 0.4 |     |     |     |     |     |
| ---------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
test[60](with𝛼=0.05)tothef-measuresfordifferentanomalypat- 102
0.2
terns.First,theFriedmantestsyieldap-valuegreaterthan0.05and
thusdonotindicatethatthesemethodsaresignificantlydifferent. 0.0 100
|     |     |     |     |     |     |     | 30 300 | 600 | 750 1500 | 3000 30 | 300 600 750 | 1500 3000 |
| --- | --- | --- | --- | --- | --- | --- | ------ | --- | -------- | ------- | ----------- | --------- |
Figure10showsthecriticaldifferencediagram[16]fortheglobal Silde size Silde size
anomalyasanexample.Methodsthatarenotconnectedbyabold (c) F-measure on ECG (d) Time cost on ECG
linediffersignificantlyintheiraverageranks.Thisprovesthatfor
Figure11:Varying(a-b)windowsizes(c-d)slidesizesonECG
asingleanomalypatternthereisaparticularmethodthatclearly
outperformstheothers.Forexample,NPnotonlyachievesfirst
placeforglobaloutliers,butalsosignificantlyoutperformsothers. 4.3.1 UnivariateMethodsinMultivariateDatasets. Asreportedin
| Summary.(1)Inpointmethods,global |     |     |     | anomaliesareeasierto |     |     |     |     |     |     |     |     |
| -------------------------------- | --- | --- | --- | -------------------- | --- | --- | --- | --- | --- | --- | --- | --- |
Section4.2.1,thepointmethodSHESDlagsfarbehindmultivariate
detectthancontextualones.(2)Insubsequencemethods,seasonal ones,therefore,wefocusonthesubsequencecase.
anomaliesareeasiesttofind,whiletrend anomaliesarehardest Settings.Ifthedetectedanomaliesindifferentdimensionsoverlap
tofind.(3)Noonemethodfitsallpatterns.Butcertainmethods aftercombination,wemergethemintoalargerange(subsequence)
areclearlybetterthanothersforaparticularanomalypattern,e.g.,
asthefinalresult.Followingthesamelogic,wealsorunmultivariate
| NP performsbestfortheglobalanomaly.(4) |     |     |     | SAND | andIDKare |     |     |     |     |     |     |     |
| -------------------------------------- | --- | --- | --- | ---- | --------- | --- | --- | --- | --- | --- | --- | --- |
methods(PBADandBeatGAN)foreachdimensionseparatelyand
notsuitablefornon-stationarytimeseries(withtrend anomaly). combinethedetectedanomaliesfordirectcomparison,theresults
(5)Distance-basedmethodsarewellsuitedforglobalandseasonal ofwhicharedisplayedinthe‘Combination’columninTable5.
anomalies.(6)IDKcanalsoworkwellforglobalanomaly,whichis WenotethatanomaliesinExercise(similarresultsareobserved
differentfromRI(8)in[49].
inotherrealdatasets)alwaysoccurinalldimensionsatthesame
position.Therefore,wetesttheeffectsofsuch‘overlap’onanother
4.3 Inter-classComparisons
syntheticdata.The‘ncor’indicatesthatpositionsofthegenerated
anomaliesaredifferentineachdimension.‘A1-A3’denotethethree
Inthissection,wewilltesttheperformanceofmethodsbetween
dimensions.
differentclassesunderthesamefacet.Inthedatadimensionfacet,
werununivariatemethodsseparatelyforeachdimensionofthe Results.Comparedwiththeresultsoneachdimensionandafter
multivariatedataandthencombinetheresults.Intheprocessing combination,mostofthemethodshaveapromotiononrecallbut
techniquefacet,werunonlinemethodsacrossdifferentwindowand asharpreductiononprecision,sincetheaggregationineachdi-
slidesizesondatasetslargerthan100kandwithdimensionslarger mensionwillinvolveinmorepredictedanomalies(covermorereal
|     |     |     |     |     |     |     | anomalies | but also | much more | false positives). | Compared | with |
| --- | --- | --- | --- | --- | --- | --- | --------- | -------- | --------- | ----------------- | -------- | ---- |
than30.Intheanomalytypefacet,asmentionedinSection1,werun
combinedresultsonthesyntheticdata,wefindoutthatanomaly
bothpointandsubsequencemethodsondatasetswithsubsequence
anomaliesunderdifferentevaluationmetricstoanalyzetheimpact positions(co-occurornot)donotclearlyimpacttheeffectiveness
ofthemetricsandtheadjustmentinpredictions.Inaddition,we and efficiency. Univariate methods can achieve good results on
alsotesttheimpactofthresholdsandperformanceunderdifferent somespecificdimensionsbutactspoorlyoverall,whilemultivariate
onesperformtheopposite,showingtheadvantageofconsidering
applicationaspects.
relationshipsoverdimensions.
|     |     |     |     |     |     |     | Summary. | Promotion | on efficiency | cannot | compensate | for the |
| --- | --- | --- | --- | --- | --- | --- | -------- | --------- | ------------- | ------ | ---------- | ------- |
sharpdropinaccuracy(weomitefficiencyresultsandshowonein
Table5:Performanceonsingledimensionandcombination
motivatingscenario1).Multivariatemethodsarebetter,unlesswe
havesufficientpriorknowledgeaboutspecificdimensions.
| Dataset  | PBAD          | BeatGAN |             | SAND |     | NP  |                                         |     |     |     |                   |     |
| -------- | ------------- | ------- | ----------- | ---- | --- | --- | --------------------------------------- | --- | --- | --- | ----------------- | --- |
|          | P R           | F P     | R F         | P R  | F P | R F |                                         |     |     |     |                   |     |
|          |               |         |             |      |     |     | 4.3.2 OnlineMethodsinBatchedTimeSeries. |     |     |     | AsexplainedinSec- |     |
| Exercise | 0.495 1 0.662 | 0.756   | 0.760 0.758 |      |     |     |                                         |     |     |     |                   |     |
Combination 0.220 1 0.360 0.332 0.997 0.498 0.293 0.672 0.408 0.309 0.983 0.47 tion4.2.1,theonlinemethodSANDsuffersfromtheiterationsof
| E_A1 | 0.357 1 0.526 | 0.708 | 0.72 0.714  | 0.483 0.513 0.498 | 0.894 | 0.943 0.918 |            |                |     |                    |                  |     |
| ---- | ------------- | ----- | ----------- | ----------------- | ----- | ----------- | ---------- | -------------- | --- | ------------------ | ---------------- | --- |
|      |               |       |             |                   |       |             | eigenvalue | decompositions |     | and its efficiency | is significantly | af- |
| E_A2 | 0.389 1 0.560 | 0.505 | 0.498 0.501 | 0.27 0.275 0.272  | 0.222 | 0.224 0.223 |            |                |     |                    |                  |     |
E_A3 0.352 0.719 0.473 0.249 0.248 0.248 0.192 0.204 0.197 0.196 0.202 0.199 fected.Thus,wefocusonthepointcase.
| Mul_ncor_g | 0.684 1 0.813 | 0.514 | 0.753 0.611 |     |     |     |     |     |     |     |     |     |
| ---------- | ------------- | ----- | ----------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Combination 0.097 1 0.178 0.215 0.861 0.344 0.250 0.897 0.391 0.279 0.941 0.431 Settings.WeruntwoexperimentsinECGvaryingwindowsizes
| M_A1 | 0.092 0.300 0.140 | 0.219 | 0.246 0.232 | 0.315 0.329 0.322 | 0.377 | 0.463 0.416 |                    |     |                                             |     |     |     |
| ---- | ----------------- | ----- | ----------- | ----------------- | ----- | ----------- | ------------------ | --- | ------------------------------------------- | --- | --- | --- |
|      |                   |       |             |                   |       |             | 𝜃 𝑊 andslidesizes𝜃 |     | 𝑆.Similarresultsareobservedinotherdatasets. |     |     |     |
| M_A2 | 0.083 0.390 0.137 | 0.222 | 0.355 0.273 | 0.261 0.353 0.300 | 0.245 | 0.368 0.294 |                    |     |                                             |     |     |     |
M_A3 0.107 0.402 0.168 0.223 0.358 0.275 0.311 0.42 0.357 0.217 0.325 0.260 𝜃 𝑆 =150inthefirstcaseand𝜃 𝑊 =3𝑘inthesecond.Itshouldbe
491

|           |     | PBAD NP    | IDK           | TranAD |     | noitavresbO | 2.5 |     | 2.5  |     |     |
| --------- | --- | ---------- | ------------- | ------ | --- | ----------- | --- | --- | ---- | --- | --- |
|           |     | SAND NormA | NETS          |        |     |             | 0.0 |     | 0.0  |     |     |
| 1.0       |     |            | 102           |        |     | −2.5        |     |     | −2.5 |     |     |
| 0.8       |     |            | )s( tsoc emiT |        |     |             | 2.5 |     | 2.5  |     |     |
| erusaem-F |     |            |               |        |     | DABP        |     |     |      |     |     |
| 0.6       |     |            | 100           |        |     |             | 0.0 |     | 0.0  |     |     |
| 0.4       |     |            |               |        |     | −2.5        |     |     | −2.5 |     |     |
|           |     |            |               |        |     |             | 2.5 |     | 2.5  |     |     |
10−2
| 0.2 |                            |                |     |                            |              | DNAS | 0.0 |     | 0.0  |     |     |
| --- | -------------------------- | -------------- | --- | -------------------------- | ------------ | ---- | --- | --- | ---- | --- | --- |
| 0.0 |                            |                |     |                            |              | −2.5 |     |     | −2.5 |     |     |
|     | 20 30                      | 40 50 60 70    | 100 | 20 30 40                   | 50 60 70 100 |      |     |     |      |     |     |
|     |                            | Anomaly length |     | Anomaly length             |              |      | 2.5 |     | 2.5  |     |     |
|     | (a) F-measure on Uni-sub-g |                |     | (b) Time cost on Uni-sub-g |              | STEN |     |     |      |     |     |
|     |                            |                |     |                            |              |      | 0.0 |     | 0.0  |     |     |
| 1.0 |                            |                | 102 |                            |              |      |     |     |      |     |     |
|     |                            |                |     |                            |              | −2.5 |     |     | −2.5 |     |     |
0.8
| erusaem-F |     |     | )s( tsoc emiT 101 |     |     | DAnarT | 2.5 |     | 2.5 |     |     |
| --------- | --- | --- | ----------------- | --- | --- | ------ | --- | --- | --- | --- | --- |
0.6
|     |     |     |     |     |     |     | 0.0 |     | 0.0 |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
100
| 0.4 |     |     |      |     |     | −2.5 |     |               | −2.5    |               |     |
| --- | --- | --- | ---- | --- | --- | ---- | --- | ------------- | ------- | ------------- | --- |
|     |     |     |      |     |     |      | 200 | 300 400 500   | 600 200 | 300 400 500   | 600 |
| 0.2 |     |     | 10−1 |     |     |      |     | Timestamp     |         | Timestamp     |     |
|     |     |     |      |     |     |      |     | (a) Uni-sub-g |         | (b) Uni-sub-s |     |
0.0
|     | 20 30 | 40 50 60 70    | 100 | 20 30 40       | 50 60 70 100 |     |     |     |     |     |     |
| --- | ----- | -------------- | --- | -------------- | ------------ | --- | --- | --- | --- | --- | --- |
|     |       | Anomaly length |     | Anomaly length |              |     |     |     |     |     |     |
(c) F-measure on Uni-sub-s (d) Time cost on Uni-sub-s Figure13:Casestudyon(a)Uni-sub-g(b)Uni-sub-s
Figure12:Varyinglengthson(a-b)Uni-sub-g(c-d)Uni-sub-s
|            |     |     |     |     |     |     | Ground Truth      | 0 1 1 1 1 0                                | 0 1 1 1 1 1 1 0 0 1 | 1 0 0 1 1 1 1 1 0 |     |
| ---------- | --- | --- | --- | --- | --- | --- | ----------------- | ------------------------------------------ | ------------------- | ----------------- | --- |
|            |     |     |     |     |     |     | TP P :3 r ,  e FN | d :1 ic 2, t  F i 1 o :0 n .30 0 0 0 0 0 0 | 0 0 1 0 0 0 0 0 0 0 | 0 0 0 0 1 0 1 0 0 |     |
| notedthat𝜃 |     | 𝜃   |     |     |     |     |                   |                                            | After point-adjust  |                   |     |
𝑆 ≤ 𝑊 alwaysholds.ThebatchmethodSHESDis A d j u s t   R e s u lt 0 0 0 0 0 0 0 1 1 1 1 1 1 0 0 0 0 0 0 1 1 1 1 1 0
|     |     |     |     |     |     |     | T P :1 1 , F | N : 4 ,  F1 :0 .7 9 |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ------------ | ------------------- | --- | --- | --- |
usedasabaseline.
| Results.Figure11(a)showsthattheaccuracyof |     |     |     |     | NETSfirstin- |     |     |     |     |     |     |
| ----------------------------------------- | --- | --- | --- | --- | ------------ | --- | --- | --- | --- | --- | --- |
Figure14:Point-adjustmethod
creasesandthendecreaseswithincreasingwindowsize.Thereason
isthatifthewindowsizeistoosmall,itisdifficulttofindenough
neighborsevenforanormaldatapoint,leadingtofalsepositives. Results. Figure 12 shows the sensitivity of the methods to the
Ifthewindowsizeistoolarge,thenumberofneighborsforalocal anomalylengthℓ.PBADdoesnotidentifythesubsequencewhose
anomalypointmayexceedthepredefinedthreshold𝜃 𝑘,leadingto lengthisexactlyℓ,makingitdifferentfromothers.Othermethods
falsenegatives.AscanbeseeninFigure11(b),asexpected,alar- claimtoachievethebestaccuracywhenℓissimilartotheactual
| gerwindowsizecausesthemethodstoconsumemoredatapoints, |     |     |     |     |     | length(ℓ |     |     |     |     |     |
| ----------------------------------------------------- | --- | --- | --- | --- | --- | -------- | --- | --- | --- | --- | --- |
=50)oftheanomalies,whichcanbeseeninFigures12(a,
whichcostsmoretime.OnepossibleexplanationforFigure11(c)is c).IDKdemonstratesrobustnessfortheinputlength,whilethebest
thatalargerslidesizeincreasesthevariationinthenumberofan- inputlengthatNormAisdifficulttopredict.Itisinterestingthat
omalypoints,whichdecreasestheaccuracyofStare.Ontheother NETSunderglobal patterns(inFigure12(a))canalsogivegood
hand,iftheslidesizeistoolarge,theintermediateinformation resultswithmuchlesstime(inFigure12(b)).InFigure13(a),we
storedforNETSchangestoomuch,whichalsonegativelyaffects
zoominon400datapointsintheUni-sub-gdatasetandhighlight
theaccuracy.RegardingtheefficiencyshowninFigure11(d),Stare theactualanomalyingreen,whiletheanomalyidentifiedbythe
takelesstimeastheslidesizeincreases.NETScannotexploitthe differentmethodsishighlightedinred.WefindoutthatPBAD
‘neteffect’whentheslidesizeisequaltothewindowsize.There- andSANDcancoverthewholeanomalysubsequence.NETSis
fore,itcantaketheleasttimeforamedium𝜃 𝑆.Itisnotedthateven alsoabletomatchsometrueanomaly(ontheright),whilethe
thefastestonlinemethodNETSwillbetentimesslowerthanthe
subsequencemethodsusuallyhavealagintheresult.Weperform
| simplebatchmethodSHESDwhen𝜃 |     |     |     | =10𝑘. |     |                                                           |     |     |     |     |     |
| --------------------------- | --- | --- | --- | ----- | --- | --------------------------------------------------------- | --- | --- | --- | --- | --- |
|                             |     |     | 𝑊   |       |     | anotherexperimentwithUni-sub-sandfindsimilarresultsforthe |     |     |     |     |     |
Summary.(1)Largersizesdonotnecessarilyproducebetterres- subsequencemethodsintermsoflengthℓ.However,pointmethods
ults,butcostmoretime.(2)Onlinemethodscanoutperformbatch cannotgiveaccurateresultsinsuchcomplexcases(inFigure12(c)).
methodsunderapropersetting,duetotheevolvementcharacter- Combiningthesetwoobservations,wearguethatpointmethods
isticoftimeseries.
facilitatethedetectionofsomeglobaloutliers,whileanomalous
patternsrequiringlong-termcontextarehardtodetect.
| 4.3.3 | PointMethodsinSubsequenceAnomalies. |     |     | Subsequencemeth- |     |                                                 |     |     |     |     |      |
| ----- | ----------------------------------- | --- | --- | ---------------- | --- | ----------------------------------------------- | --- | --- | --- | --- | ---- |
|       |                                     |     |     |                  |     | Summary.(1)Pointmethodscanalsoworkwellforglobal |     |     |     |     | sub- |
odsalwaysconsidertheanomalylengthℓasaninputparameter[7].
sequenceanomalieswithextremevalues,whichmayhelprelax
However,thisaffectsaccuracytosomeextent,sincesubsequence
thelengthinputrequirement.(2)Thelengthparameterℓ,which
anomaliesinrealtimeseriesdatararelyhaveafixedlength.Incon-
isclosetotheactualanomalylength,givesgoodresults.Adaptive
trast,pointanomalymethodsrequirenosuchinput(thelengthis1).
inputlengthareneededtodealwithreal-worldsituations.
Therefore,wewouldliketoknowtheeffectofanomalylengthand
whetherwecanperformpointmethodsforsubsequenceanomalies. 4.3.4 EffectofMetricsandAdjustment. Usingpointmetricsfor
Settings.Weuseunivariatedatawithinjectedglobalandseasonal
datasetswithsubsequenceanomalywillbiastheaccuracyofmany
anomaliestoavoidtheeffectofdimensions.Weomittrendbecause timeseriesanomalydetectionsystemsbynotcapturingspecific
theyhavesimilarresultstoseasonal.Forbrevity,wereportonly properties[53].Forareal-timeapplication,itmightbemoreim-
NETSandTranAD,asotherpointmethodsperformsimilarly. portanttodetecttheearlierpartofananomalytoreduceresponse
492

Table6:F-measurew/opoint-adjustunderdifferentmetrics
|     |     |     |     |     |     |     |     |     |     | RCoder Omni | GDN | TranAD | USAD |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----------- | --- | ------ | ---- |
0.5
1.0
| Algorithm |         |             | PointMetric        |         |          | RangeMetric |         | 0.4       |     |     | 0.8       |     |     |
| --------- | ------- | ----------- | ------------------ | ------- | -------- | ----------- | ------- | --------- | --- | --- | --------- | --- | --- |
|           |         |             |                    |         |          |             |         | erusaem-F |     |     | noisicerP |     |     |
|           | Twitter | ECG inc/alg | Exathlon Uni-sub-g | inc/alg | Exathlon | Uni-sub-g   | inc/alg | 0.3       |     |     |           |     |     |
| TranAD    | 0.455   | 0.224       | 0.245 0.299        |         | 0.484    | 0.345       |         |           |     |     | 0.6       |     |     |
|           |         | 39.7%       |                    | 6.1%    |          |             | -68.9%  |           |     |     |           |     |     |
| TranAD∗   | 0.466   | 0.397       | 0.246 0.414        |         | 0.246    | 0.039       |         | 0.2       |     |     | 0.4       |     |     |
| USAD      | 0.274   | 0.286       | 0.246 0.330        |         | 0.245    | 0.365       |         |           |     |     |           |     |     |
USAD∗ 0.289 0.448 31.0% 0.246 0.452 6.1% 0.245 0.038 -44.8% 0.1 0.2
| Omni  | 0.138 | 0.318 36.4% | 0.245 0.267 | 14.3% | 0.409 | 0.240 | -53.5% |     |     |     |     |     |     |
| ----- | ----- | ----------- | ----------- | ----- | ----- | ----- | ------ | --- | --- | --- | --- | --- | --- |
| Omni∗ | 0.166 | 0.483       | 0.246 0.553 |       | 0.246 | 0.079 |        | 0.0 |     |     | 0.0 |     |     |
RCoder - 0.441 - - - - 0% 20% 40% 60% 80% 100% 0.0 0.2 0.4 0.6 0.8 1.0
| RCoder∗ |       | 43.0%       |             |       | -     |       | -      |     |                      | Threshold |        |                     | Recall |
| ------- | ----- | ----------- | ----------- | ----- | ----- | ----- | ------ | --- | -------------------- | --------- | ------ | ------------------- | ------ |
|         | -     | 0.631       | -           | -     | -     | -     |        |     | (a) F-measure on ECG |           |        | (b) PR Curve on ECG |        |
| GDN     | 0.449 | 0.274       | 0.238 0.267 |       | 0.851 | 0.239 |        |     |                      |           |        |                     |        |
| GDN∗    | 0.460 | 0.410 26.9% | 0.246 0.554 | 14.7% | 0.246 | 0.079 | -69.1% |     |                      |           |        |                     |        |
|         |       |             |             |       |       |       |        |     |                      | NP        | MERLIN | NormA               | IDK    |
| NETS    | 0.802 | 0.461       | 0.286 0.942 |       | 0.217 | 0.942 |        |     |                      |           |        |                     |        |
| NETS∗   | 0.852 | 0.666 25.3% |             | 42.8% |       |       | -28.5% |     |                      |           | 1.0    |                     |        |
|         |       |             | 0.754       | 1     | 0.080 | 1     |        | 0.8 |                      |           |        |                     |        |
| Stare   | 0.334 | 0.252 66.6% | 0.253 0.653 | 14.5% | 0.189 | 0.438 | -85.0% |     |                      |           |        |                     |        |
| Stare∗  | 0.334 | 0.589       | 0.312 0.725 |       | 0.018 | 0.090 |        |     |                      |           | 0.8    |                     |        |
SHESD 0.209 0.339 0.257 0.978 0.227 0.979 erusaem-F 0.6 noisicerP
| SHESD∗ |       | 82.8% |       | 43.8% |       |     | -29.0% |     |     |     | 0.6 |     |     |
| ------ | ----- | ----- | ----- | ----- | ----- | --- | ------ | --- | --- | --- | --- | --- | --- |
|        | 0.510 | 0.488 | 0.776 | 1     | 0.090 | 1   |        |     |     |     |     |     |     |
0.4
| inc/data | 23.1% | 58.3% | 18.5% 12.5% |     | -53.4% | -54.8% |     |     |     |     | 0.4 |     |     |
| -------- | ----- | ----- | ----------- | --- | ------ | ------ | --- | --- | --- | --- | --- | --- | --- |
|          |       |       |             |     |        |        |     | 0.2 |     |     | 0.2 |     |     |
|          |       |       |             |     |        |        |     | 0.0 |     |     | 0.0 |     |     |
time[32].Therefore,theoverlapofpredictedanomaliesandac- 0% 20% 40% 60% 80% 100% 0.0 0.2 0.4 0.6 0.8 1.0
tualanomaliesshouldbeaddressed.Todealwithinterpretationsof Threshold Recall
|     |     |     |     |     |     |     |     |     | (c) F-measure on Uni-sub-g |     |     | (d) PR Curve on Uni-sub-g |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | -------------------------- | --- | --- | ------------------------- | --- |
suchoverlapsandtheproblemoflabelimbalance,somemethods
[3,52,58]useapoint-adjustmethod[62]thatconvertsfalsenegat- Figure15:Varyingthresholdson(a-b)ECG(c-d)Uni-sub-g
ivestotruepositives.AsshowninFigure14,foreachpointinthe
anomalysegmentofthegroundtruth,ifitisdetectedasananom-
Table7:F-measurew/oPOTmethod
alybytheproposedalgorithm,allobservationsinthesubsequence
willbeconsideredtohavebeencorrectlydetectedasanomalies.
|     |     |     |     |     |     |     |     | DataSet | TranAD | TranAD-P USAD | USAD-P | Omni Omni-P | GDN GDN-P |
| --- | --- | --- | --- | --- | --- | --- | --- | ------- | ------ | ------------- | ------ | ----------- | --------- |
Therefore,suchamethodignoreslatencyandreportsmuchhigher
|     |     |     |     |     |     |     |     | ECG | 0.248 | 0.350 0.286 | 0.338 | 0.224 0.345 | 0.271 0.353 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ----- | ----------- | ----- | ----------- | ----------- |
accuracythanitactuallyis.RCoderproposesadifferentwayto
|     |     |     |     |     |     |     |     | DLR | 0.152 | 0.007 0.154 | 0.070 | 0.065 0.070 | 0.060 0.069 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ----- | ----------- | ----- | ----------- | ----------- |
adjustpredictions[1].However,wefocusonanalyzingthemore TAO 0.181 0.181 0.180 0.181 0.181 0.181 0.012 0.181
widelyusedpoint-adjustmethodinthiswork. UNI 0.179 0.182 0.158 0.182 0.660 0.181 0.181 0.183
Settings.Weconductexperimentswithbothpoint(Twitter,ECG)
andsubsequencedatasets(Exathlon,Uni-sub-g).Theresultsofpoint
robustnessofeachalgorithmw.r.t.thresholdandtheimpactofthe
datasetsareevaluatedbythepointmetricandtheresultsofsub-
POT[51]methodforautomaticthresholdselection.
sequencedatasetsareevaluatedbybothpointandrangemetrics.
|     |     |     |     |     |     |     |     | Settings. | We  | unify the threshold | setting | for all | methods in the |
| --- | --- | --- | --- | --- | --- | --- | --- | --------- | --- | ------------------- | ------- | ------- | -------------- |
Resultswiththepoint-adjustmethodaredenotedby∗.
followingway:letthethresholdbetheratioofpoints/sequences
Results.Table6showsthef-measureindifferentcases.‘inc/alg’
identifiedasanomalies.0%meansallarenormal,while100%means
givestheaveragepromotionafterapplyingpoint-adjustmethod
|     |     |     |     |     |     |     |     | allareanomalies.However, |     |     | NETS,Stare,andSHESDhavedifferent |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------------------ | --- | --- | -------------------------------- | --- | --- |
permethodand‘inc/data’showsthispromotionperdata.Point-
logicinidentifyinganomalies(morethanonefactorisconsidered),
adjustmethodcanhaveagreatimpactontheevaluationasfollows:
sowereportonlyothermethodsinthispart.Theoverallperform-
(1)Overall,thealgorithmwillhaveanaveragepromotionof27.0%
anceistheareaincludedbytherecallandprecisioncurves.Besides,
forpointdatasetsandahigherpromotionof31.2%forsubsequence
theresultsofusingPOTmethodarepresentedinTable7.
datasetsunderpointmetrics.(2)Forsubsequencedatasetswith
Results.Figure15(c,d)showtheresultsonUni-sub-g.Wenote
rangemetrics,thealgorithmshaveanaveragenegativepromotion
thatNP,despitehavingabetterbestF-measurethanNormA,drops
of−67.6%.(3)TranADandOmnihaveahigherf-measure(0.245)
sharplyasthethresholdapproaches20%.Incontrast,NormAshows
thanGDN(0.238)underthepointmetric,butGDNperformsfar
betterrobustnessasthecurveissmoother.Itisinterestingtonote
better(0.851)thanTranAD(0.484)andOmni(0.409)onExathlon
underrangemetric.(4)Starehasahigherf-measure(0.334)than thatIDKperformsbestinthisexperiment,butdoesnotoutperform
SHESD(0.209),butaftertheadjustment,SHESDwillperformbetter inFigure9.Thereasonforthisisthatinallotherexperiments
weperformagridsearchonthevalidationsettofindtheproper
(0.510)thanStare(0.334)onTwitter.Suchinversionscanconfusean-
|     |     |     |     |     |     |     |     | (hyper)-parameters, |     | but there | is a small | difference | between the |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------------- | --- | --------- | ---------- | ---------- | ----------- |
omalydetectionsystemsandinfluenceuserpreferencesinselecting
validationsetandthetestset.Asforthepointmethodsshownin
appropriatemethods..
Figures15(a,b),RCodershowstheoverallbestperformanceamong
Summary.(1)point-adjustmethodtendstoreport‘false’higher
allthedeeplearningmethods,whileOmnishowsbetterrobustness.
resultsforalgorithmsandcanleadtomisleadinganalyzes.(2)The
IntermsoftheimpactofPOTmethod,GDNalwayshaveabetter
useofrangemetricsondatasetswithsubsequenceanomaliesis
resultafterusingit.Othermethodsshowdifferentpreferenceson
preferableasitleadstomorereasonableandrobustresults.
differentdatasets.Inaround55%cases,POTcanachievesimilaror
4.3.5 EffectofThreshold. Thresholdisakeyhyper-parameterfor slightlybetterresultsthangridsearchonvalidationset.
anomaly detection problems whose effect has seldom been dis- Summary.(1)Automaticthresholdselectionmethodscanstillbe
cussedinexistingworks,asstatedinSection1.2.Wewilltestthe improvedtotakeeffectinpracticaluses.(2)IDKhasthebestoverall
493

|     |     | FPR | FNR |     |     | FPR | FNR |     | Input :  |     |     |     | N   |     | NETS |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | -------- | --- | --- | --- | --- | --- | ---- |
TimeSeries x
| 1.00 |     |     |     | 1.00 |     |     |     |     |     |     |     |     |     | Y   |     |
| ---- | --- | --- | --- | ---- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
RCoder
| 0.75  |     |     |     | 0.75  |     |     |     |              |                     |       |                |                 | P o     | s i t iv e      |            |
| ----- | --- | --- | --- | ----- | --- | --- | --- | ------------ | ------------------- | ----- | -------------- | --------------- | ------- | --------------- | ---------- |
|       |     |     |     |       |     |     |     | Anomaly type |                     | Point | High Dimension |                 | Y  ap p | l i c a t ion N | Omni       |
| eulaV |     |     |     | eulaV |     |     |     |              |                     |       |                |                 |         |                 |            |
| 0.50  |     |     |     | 0.50  |     |     |     | Subsequence  |                     |       |                |                 |         | Y               | NP         |
| 0.25  |     |     |     | 0.25  |     |     |     |              |                     |       |                | N               | E       | a rl y N        | M E R L IN |
|       |     |     |     |       |     |     |     | K n          | o w l e d g e   of  |       |                |                 | De te   | c t io n        |            |
|       |     |     |     |       |     |     |     |              | a n o m a l y       | Y     | P              | o s i t iv e    |         | Y               | P B A D    |
| 0.00  |     |     |     | 0.00  |     |     |     |              |                     |       |  ap            | p l i c a t ion |         |                 |            |
NETS Stare TranAD RCoder USAD GDN Omni PBAD LRRD B SAND NPMER G N IDK d i s t r i b u t i o n Y
|     |     |     |     |     | S eatGAN |     | LI r N ammar o rmA |     |     |      |                |     |               |             | SAND |
| --- | --- | --- | --- | --- | -------- | --- | ------------------ | --- | --- | ---- | -------------- | --- | ------------- | ----------- | ---- |
|     |     |     |     |     |          |     | V iz               |     | N   | S ta | ti o n a r y   | Y   | K n o w l e d | g e   o f   |      |
(a) Point Methods (b) Subsequence Methods t im e   se r i e s a n o m a l y  l e n g t h N IDK
|     |     |     |     |     |     |     |     |     |     |     |     | N   |     |     | NormA |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----- |
Figure16:FPRandFNRonrealdatasets
|     |     |     |     |     |     |     |     | Figure | 18: A | practical | guide | for | timeseries | anomaly | detec- |
| --- | --- | --- | --- | --- | --- | --- | --- | ------ | ----- | --------- | ----- | --- | ---------- | ------- | ------ |
tion
20%
| 1.00           | Flat  |     |     | erusaem-F fo niaG |               | 10.99% |               |     |     |     |     |     |     |     |     |
| -------------- | ----- | --- | --- | ----------------- | ------------- | ------ | ------------- | --- | --- | --- | --- | --- | --- | --- | --- |
|                | Front |     |     |                   | 4.75%         | 1.87%  |               |     |     |     |     |     |     |     |     |
| erusaem-F 0.75 |       |     |     | 0%                |               |        |               |     |     |     |     |     |     |     |     |
|                |       |     |     |                   | -7.30% -7.59% |        | -4.50% -1.72% |     |     |     |     |     |     |     |     |
-13.96%
| 0.50 |     |     |     | -20% |     |     |     |     |     |     |     |     |     |     |     |
| ---- | --- | --- | --- | ---- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
0.25
-40%
0.00
PBAD LRRD B eatGAN SAND NPMERG N IDK PBAD LRRD B eatGAN -48.76% SAND NPMERG N IDK WeseesimilarresultsinFigure17(b),wheretheaveragecompar-
|     |     | S   | Lr I a Nmmar o rmA |     | S   | Lr IN | ammar o rmA |     |     |     |     |     |     |     |     |
| --- | --- | --- | ------------------ | --- | --- | ----- | ----------- | --- | --- | --- | --- | --- | --- | --- | --- |
V iz V iz isonistestedoverallrealdatasets.BeatGANscoresa49%drop
|     | (a) F-measure on power |     |     | (b) Front compared to Flat on all real datasets |     |     |     |     |     |     |     |     |     |     |     |
| --- | ---------------------- | --- | --- | ----------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
comparedtoitsperformanceundertheFlatmetric,showingthatit
capturesoutlierswithlatency.NPappearstobethebestperforming
Figure17:EarlydetectionunderFrontmetric
algorithmforearlydetection,withaperformanceimprovementof
10.99%.
performance,whileNormAismorerobust,specificallywhenthe Summary.(1)Specificmetricsarerequiredfordifferentscenarios.
thresholdisabove20%.(3)RCoderhasthebestoverallperformance, (2)Allsubsequencemethodsarebettersuitedfornegativeapplica-
whileOmniismorerobust.
tionsandPBADcanbeselectedforpositivecases.(3)NPisrecom-
4.3.6 Application. Inthissection,wefocusonanomalydetection mendedforearlydetection.(4)Omniisrecommendedfornegative
applications,whileRCoderisbetterforpositiveones.
inreal-worldapplications.Scenario1:Someapplicationsaremore
interestedinpositiveoutcomes,suchascancerdetection,where
wedonotwantcancerpatientstogoundetected.Othersaremore 5 DISCUSSIONS
interestedinnegativeoutcomes,suchaswhenwedonotwanta
Inthispaper,ataxonomyofanomalydetectionmethodsispresen-
goodemailtobecomespam.Scenario2:Inthepreviousstudy,we
tedandsystematicexperimentalintra-andinter-classcomparisons
assumedthatallpositionsofanoutlierrangeareequallyimportant.
areproposed.DetailedfindingsareshownintheSummarypartof
Therefore,largeroverlapsleadtoahigherscoreofthemetric.How-
Section4.Wefirstsummarizethesefindingsintoapracticalguide
ever,inpractice,therearemanysituationswhereearlyresponseis
andfinallyhighlightsomeresearchopportunitiesbelow.
critical,e.g.,cancerdetectionorreal-timesystems.
APracticalGuide.Apracticalguidefortimeseriesanomalyde-
Settings.Weemployexperimentsonallrealdatasetswithpoint
|                                            |     |     |     |     |     |     | 𝐹 𝑃   | tectionispresentedinFigure18basedontheexperimentalfindings |     |     |     |     |     |     |     |
| ------------------------------------------ | --- | --- | --- | --- | --- | --- | ----- | ---------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
| andsubsequencemethodsforScenario1,where𝐹𝑃𝑅 |     |     |     |     |     |     | = 𝐹𝑃, |                                                            |     |     |     |     |     |     |     |
|                                            |     |     |     |     |     |     | 𝑇𝑁 +  | onvariousaspectsliketypeofanomaly,dimensionality,typeof    |     |     |     |     |     |     |     |
𝐹𝑁𝑅= 𝐹 𝑁
𝑇𝑃 + 𝐹𝑁.Scenario2isparticularlysuitableforsubsequence applicationetc.Suchaguideisformedaccordingtocurrentwork
methods.Flatdenotesthemetricwiththesamescoreforallposi- andfutureworkisstillencouraged.
tions,whileFrontassignsmoreweighttotheearlypositionsofthe Explainability.Theexplainabilityofanomalydetectionmethods
subsequenceanomaly[53].
hasraisedmanyconcernsinrecentyears[37].Adecisionmaker
Results.Allalgorithmsgenerallyhaveahigherfalsenegativerate
maybemoreinterestedinthecauseoftheoccurrenceofoutliersso
andalowerfalsepositiverate,ascanbeseeninFigure16.This thattheycantakeappropriateaction,especiallyintheareaofIoT
suggeststhattheyaremoresuitablefornegativeapplications(not data[27].Developingamethodthatprovidesbothhighaccuracy
reportingfalseanomalies)andaremorecapableofdetectingnormal andreasonableexplainabilitymaybeofinterestforfuturework.
samplesthanabnormalsamples.Inparticular,NETSandOmnihave
lowFPRandarerecommendedfornegativecasessuchasspamde-
ACKNOWLEDGMENTS
tection.Ontheotherhand,TranADandRCoderarerecommended
forpositiveapplicationssincetheymanagetoreportallanomalies. AoqianZhangissupportedbytheNSFC(GrantNos.6210070801,
Similarly,PBADismoresuitablethanBeatGANforsuchcasesdue U21B2007).GuorenWangissupportedbytheNSFC(GrantNos.
toitslowerFNR. 61732003,U2001211).YeYuanissupportedbytheNationalKeyR&D
Figure17(a)showstheperformanceofthealgorithmsunderFlat ProgramofChina(GrantNo.2022YFB2702100),theNSFC(Grant
andFrontmetricsonPower.(Similarresultsareobservedonother Nos.61932004,62225203,U21A20516)andtheDITDP(GrantNo.
real-worlddatasets.)BeatGANhasahigherf-measurethanPBAD JCKY2021211B017).Wealsothankallthemembersofourcom-
undertheFlatmetric,butachievesalowerscorewhentheFront munitywhoopensourcedtheirdataandcodes,whichhelpusalot
| metricisused,indicatingthatitisnotsuitableforearlydetection. |     |     |     |     |     |     |     | onthiswork. |     |     |     |     |     |     |     |
| ------------------------------------------------------------ | --- | --- | --- | --- | --- | --- | --- | ----------- | --- | --- | --- | --- | --- | --- | --- |
494

REFERENCES
[30] EamonnJ.Keogh,JessicaLin,Sang-HeeLee,andHelgaVanHerle.2007.Finding
[1] AhmedAbdulaal,ZhuanghuaLiu,andTomerLancewicki.2021.PracticalAp- themostunusualtimeseriessubsequence:algorithmsandapplications.Knowl.
proachtoAsynchronousMultivariateTimeSeriesAnomalyDetectionandLoc- Inf.Syst.11,1(2007),1–27. https://doi.org/10.1007/s10115-006-0034-6
alization.InKDD.ACM,2485–2494. [31] Kwei-HerngLai,DaochenZha,JunjieXu,YueZhao,GuanchuWang,andXia
[2] CharuC.Aggarwal.2013.OutlierAnalysis.Springer. Hu.2021.RevisitingTimeSeriesOutlierDetection:DefinitionsandBenchmarks.
[3] JulienAudibert,PietroMichiardi,FrédéricGuyard,SébastienMarti,andMariaA. InThirty-fifthConferenceonNeuralInformationProcessingSystemsDatasetsand
Zuluaga.2020.USAD:UnSupervisedAnomalyDetectiononMultivariateTime BenchmarksTrack(Round1). https://openreview.net/forum?id=r8IvOsnHchr
Series.InKDD.ACM,3395–3404. [32] NikolayLaptev,SaeedAmizadeh,andIanFlint.2015. GenericandScalable
[4] VicBarnett,TobyLewis,etal.1994.Outliersinstatisticaldata.Vol.3.WileyNew FrameworkforAutomatedTime-seriesAnomalyDetection.InKDD.ACM,1939–
York. 1947.
[5] AneBlázquez-García,AngelConde,UsueMori,andJoséAntonioLozano.2021. [33] N.JesperLarssonandAlistairMoffat.1999.OfflineDictionary-BasedCompres-
AReviewonOutlier/AnomalyDetectioninTimeSeriesData. ACMComput. sion.InDataCompressionConference,DCC1999,Snowbird,Utah,USA,March
Surv.54,3(2021),56:1–56:33. 29-31,1999.IEEEComputerSociety,296–305.
[6] PaulBoniol,MicheleLinardi,FedericoRoncallo,ThemisPalpanas,Mohammed [34] AlexanderLavinandSubutaiAhmad.2015. EvaluatingReal-TimeAnomaly
Meftah,andEmmanuelRemy.2021. Unsupervisedandscalablesubsequence DetectionAlgorithms-TheNumentaAnomalyBenchmark.InICMLA.IEEE,
anomalydetectioninlargedataseries.VLDBJ.30,6(2021),909–931. 38–44.
[7] PaulBoniol,JohnPaparrizos,ThemisPalpanas,andMichaelJ.Franklin.2021. [35] Kim-HungLeandPaoloPapotti.2020. User-drivenErrorDetectionforTime
SAND:StreamingSubsequenceAnomalyDetection.Proc.VLDBEndow.14,10 SerieswithEvents.InICDE.IEEE,745–757.
(2021),1717–1729. [36] DanLi,DachengChen,BaihongJin,LeiShi,JonathanGoh,andSee-KiongNg.
[8] MohammadBraeiandSebastianWagner.2020.AnomalyDetectioninUnivariate 2019.MAD-GAN:MultivariateAnomalyDetectionforTimeSeriesDatawith
Time-series:ASurveyontheState-of-the-Art.CoRRabs/2004.00433(2020). GenerativeAdversarialNetworks.InICANN(4)(LectureNotesinComputer
[9] BernardoBranco,PedroAbreu,AnaSofiaGomes,MarianaS.C.Almeida,JoãoTi- Science),Vol.11730.Springer,703–716.
agoAscensão,andPedroBizarro.2020.InterleavedSequenceRNNsforFraud [37] ZhongLi,YuxuanZhu,andMatthijsvanLeeuwen.2022.ASurveyonExplainable
Detection.InKDD.ACM,3101–3109. AnomalyDetection.CoRRabs/2210.06959(2022).
[10] MikelCanizo,IsaacTriguero,AngelConde,andEnriqueOnieva.2019.Multi- [38] FeiTonyLiu,KaiMingTing,andZhi-HuaZhou.2008.IsolationForest.InICDM.
headCNN-RNNformulti-timeseriesanomalydetection:Anindustrialcase IEEEComputerSociety,413–422.
study.Neurocomputing363(2019),246–260. [39] ShenghuaLiu,BinZhou,QuanDing,BryanHooi,ZhengboZhang,Huawei
[11] RaghavendraChalapathyandSanjayChawla.2019.DeepLearningforAnomaly Shen,andXueqiCheng.2022.Timeseriesanomalydetectionwithadversarial
Detection:ASurvey.CoRRabs/1901.03407(2019). reconstructionnetworks.IEEETransactionsonKnowledgeandDataEngineering
[12] DhruvChoudhary,ArunKejariwal,andFrancoisOrsini.2017.OntheRuntime- (2022).
EfficacyTrade-offofAnomalyDetectionTechniquesforReal-TimeStreaming [40] YueLu,RenjieWu,AbdullahMueen,MariaA.Zuluaga,andEamonnJ.Keogh.
Data.CoRRabs/1710.04735(2017). 2022.MatrixProfileXXIV:ScalingTimeSeriesAnomalyDetectiontoTrillions
[13] RobertBCleveland,WilliamSCleveland,JeanEMcRae,andIrmaTerpenning. ofDatapointsandUltra-fastArrivingDataStreams.InKDD’22:The28thACM
1990.STL:Aseasonal-trenddecomposition.J.Off.Stat6,1(1990),3–73. SIGKDDConferenceonKnowledgeDiscoveryandDataMining,Washington,DC,
[14] AndrewA.Cook,GokselMisirli,andZhongFan.2020.AnomalyDetectionfor USA,August14-18,2022,AidongZhangandHuzefaRangwala(Eds.).ACM,
IoTTime-SeriesData:ASurvey.IEEEInternetThingsJ.7,7(2020),6481–6494. 1173–1182.
[15] ZahraZamanzadehDarban,GeoffreyI.Webb,ShiruiPan,CharuC.Aggarwal, [41] AdityaP.MathurandNilsOleTippenhauer.2016. SWaT:awatertreatment
andMahsaSalehi.2022.DeepLearningforTimeSeriesAnomalyDetection:A testbedforresearchandtrainingonICSsecurity.In2016InternationalWorkshop
Survey.CoRRabs/2211.05244(2022). onCyber-physicalSystemsforSmartWaterNetworks,CySWater@CPSWeek2016,
[16] JanezDemsar.2006.StatisticalComparisonsofClassifiersoverMultipleData Vienna,Austria,April11,2016.IEEEComputerSociety,31–36. https://doi.org/
Sets.J.Mach.Learn.Res.7(2006),1–30. 10.1109/CySWater.2016.7469060
[17] AilinDengandBryanHooi.2021. GraphNeuralNetwork-BasedAnomaly [42] TakaakiNakamura,MakotoImamura,RyanMercer,andEamonnJ.Keogh.2020.
DetectioninMultivariateTimeSeries.InAAAI.AAAIPress,4027–4035. MERLIN:Parameter-FreeDiscoveryofArbitraryLengthAnomaliesinMassive
[18] EthanW.DereszynskiandThomasG.Dietterich.2011.SpatiotemporalModels TimeSeriesArchives.In20thIEEEInternationalConferenceonDataMining,
forData-AnomalyDetectioninDynamicEnvironmentalMonitoringCampaigns. ICDM2020,Sorrento,Italy,November17-20,2020.IEEE,1190–1195.
ACMTrans.Sens.Networks8,1(2011),3:1–3:36. [43] CraigG.Nevill-ManningandIanH.Witten.1997. IdentifyingHierarchical
[19] LenFeremans,VincentVercruyssen,BorisCule,WannesMeert,andBartGoeth- StructureinSequences:Alinear-timealgorithm. J.Artif.Intell.Res.7(1997),
als.2019. Pattern-BasedAnomalyDetectioninMixed-TypeTimeSeries.In 67–82.
ECML/PKDD(1)(LectureNotesinComputerScience),Vol.11906.Springer,240– [44] AntoniosNtroumpogiannis,MichailGiannoulis,NikolaosMyrtakis,Vassilis
256. Christophides,EricSimon,andIoannisTsamardinos.2023.Ameta-levelanalysis
[20] MiltonFriedman.1937.Theuseofrankstoavoidtheassumptionofnormality ofonlineanomalydetectors.VLDBJ.32,4(2023),845–886.
implicitintheanalysisofvariance.Journaloftheamericanstatisticalassociation [45] JohnPaparrizos,PaulBoniol,ThemisPalpanas,RueySTsay,AaronElmore,and
32,200(1937),675–701. MichaelJFranklin.2022.Volumeunderthesurface:anewaccuracyevaluation
[21] MarkusGoldsteinandSeiichiUchida.2016. Acomparativeevaluationofun- measurefortime-seriesanomalydetection.ProceedingsoftheVLDBEndowment
supervisedanomalydetectionalgorithmsformultivariatedata.PloSone11,4 15,11(2022),2774–2787.
(2016),e0152173. [46] JohnPaparrizosandLuisGravano.2015.k-Shape:EfficientandAccurateClus-
[22] ManishGupta,JingGao,CharuC.Aggarwal,andJiaweiHan.2014. Outlier teringofTimeSeries.InProceedingsofthe2015ACMSIGMODInternational
DetectionforTemporalData:ASurvey.IEEETrans.Knowl.DataEng.26,9(2014), ConferenceonManagementofData,Melbourne,Victoria,Australia,May31-June
2250–2267. 4,2015,TimosK.Sellis,SusanB.Davidson,andZacharyG.Ives(Eds.).ACM,
[23] D.M.Hawkins.1980.IdentificationofOutliers.Springer. 1855–1870.
[24] YuanduoHe,XuChu,andYashaWang.2020.NeighborProfile:BaggingNearest [47] JohnPaparrizos,YuhaoKang,PaulBoniol,RueyS.Tsay,ThemisPalpanas,andMi-
NeighborsforUnsupervisedTimeSeriesMining.InICDE.IEEE,373–384. chaelJ.Franklin.2022.TSB-UAD:AnEnd-to-EndBenchmarkSuiteforUnivariate
[25] JordanHochenbaum,OwenS.Vallis,andArunKejariwal.2017. Automatic Time-SeriesAnomalyDetection.Proc.VLDBEndow.15,8(2022),1697–1711.
AnomalyDetectionintheCloudViaStatisticalLearning.CoRRabs/1704.07706 [48] BernardRosner.1975.Onthedetectionofmanyoutliers.Technometrics17,2
(2017). (1975),221–227.
[26] MinHu,XiaoweiFeng,ZhiweiJi,KeYan,andShengchenZhou.2019.Anovel [49] SebastianSchmidl,PhillipWenig,andThorstenPapenbrock.2022. Anomaly
computationalapproachfordiscordsearchwithlocalrecurrenceratesinmul- DetectioninTimeSeries:AComprehensiveEvaluation.Proc.VLDBEndow.15,9
tivariatetimeseries.Inf.Sci.477(2019),220–233. (2022),1779–1797.
[27] RuihongHuang,ZhiweiChen,ZhichengLiu,ShaoxuSong,andJianminWang. [50] PavelSenin,JessicaLin,XingWang,TimOates,SunilGandhi,ArnoldP.Boedi-
2019. TsOutlier:ExplainingOutlierswithUniformProfilesoverIoTData.In hardjo,CrystalChen,andSusanFrankenstein.2018.GrammarViz3.0:Interactive
IEEEBigData.IEEE,2024–2027. DiscoveryofVariable-LengthTimeSeriesPatterns.ACMTrans.Knowl.Discov.
[28] KyleHundman,ValentinoConstantinou,ChristopherLaporte,IanColwell,and Data12,1(2018),10:1–10:28.
TomSöderström.2018.DetectingSpacecraftAnomaliesUsingLSTMsandNon- [51] AlbanSiffer,Pierre-AlainFouque,AlexandreTermier,andChristineLargouët.
parametricDynamicThresholding.InKDD.ACM,387–395. 2017.AnomalyDetectioninStreamswithExtremeValueTheory.InKDD.ACM,
[29] VincentJacob,FeiSong,ArnaudStiegler,BijanRad,YanleiDiao,andNesime 1067–1075.
Tatbul.2021.Exathlon:ABenchmarkforExplainableAnomalyDetectionover [52] YaSu,YoujianZhao,ChenhaoNiu,RongLiu,WeiSun,andDanPei.2019.Robust
TimeSeries.Proc.VLDBEndow.14,11(2021),2613–2626. AnomalyDetectionforMultivariateTimeSeriesthroughStochasticRecurrent
NeuralNetwork.InKDD.ACM,2828–2837.
495

[53] NesimeTatbul,TaeJunLee,StanZdonik,MejbahAlam,andJustinGottschlich. [62] HaowenXu,WenxiaoChen,NengwenZhao,ZeyanLi,JiahaoBu,ZhihanLi,Ying
2018.PrecisionandRecallforTimeSeries.InNeurIPS.1924–1934. Liu,YoujianZhao,DanPei,YangFeng,JieChen,ZhaogangWang,andHonglin
[54] MarkusThill,WolfgangKonen,andThomasBäck.2017.Onlineanomalydetec- Qiao.2018.UnsupervisedAnomalyDetectionviaVariationalAuto-Encoderfor
tiononthewebscopeS5dataset:Acomparativestudy.InEAIS.IEEE,1–8. SeasonalKPIsinWebApplications.InWWW.ACM,187–196.
[55] KaiMingTing,ZongyouLiu,HangZhang,andYeZhu.2022.ANewDistribu- [63] HuiYang,SatishT.S.Bukkapatnam,andLeandroG.Barajas.2011. Localre-
tionalTreatmentforTimeSeriesandAnAnomalyDetectionInvestigation.Proc. currencebasedperformancepredictionandprognosticsinthenonlinearand
VLDBEndow.15,11(2022),2321–2333. nonstationarysystems.PatternRecognit.44,8(2011),1834–1840.
[56] KaiMingTing,Bi-CunXu,TakashiWashio,andZhi-HuaZhou.2020.Isolation [64] DragomirYankov,EamonnJ.Keogh,andUmaaRebbapragada.2008.Diskaware
DistributionalKernel:ANewToolforKernelbasedAnomalyDetection.InKDD discorddiscovery:findingunusualtimeseriesinterabytesizeddatasets.Knowl.
’20:The26thACMSIGKDDConferenceonKnowledgeDiscoveryandDataMining, Inf.Syst.17,2(2008),241–262.
VirtualEvent,CA,USA,August23-27,2020,RajeshGupta,YanLiu,JiliangTang, [65] Chin-ChiaMichaelYeh,YanZhu,LiudmilaUlanova,NurjahanBegum,YifeiDing,
andB.AdityaPrakash(Eds.).ACM,198–206. HoangAnhDau,DiegoFurtadoSilva,AbdullahMueen,andEamonnJ.Keogh.
[57] LuanTran,LiyueFan,andCyrusShahabi.2016.Distance-basedOutlierDetection 2016. MatrixProfileI:AllPairsSimilarityJoinsforTimeSeries:AUnifying
inDataStreams.Proc.VLDBEndow.9,12(2016),1089–1100. ViewThatIncludesMotifs,DiscordsandShapelets.InIEEE16thInternational
[58] ShreshthTuli,GiulianoCasale,andNicholasR.Jennings.2022.TranAD:Deep ConferenceonDataMining,ICDM2016,December12-15,2016,Barcelona,Spain.
TransformerNetworksforAnomalyDetectioninMultivariateTimeSeriesData. IEEEComputerSociety,1317–1322.
Proc.VLDBEndow.15,6(2022),1201–1214. [66] SusikYoon,Jae-GilLee,andByungSukLee.2019.NETS:ExtremelyFastOutlier
[59] ChenWang,XiangdongHuang,JialinQiao,TianJiang,LeiRui,JinruiZhang, DetectionfromaDataStreamviaSet-BasedProcessing.Proc.VLDBEndow.12,
RongKang,JulianFeinauer,KevinMcgrail,PengWang,DiaohanLuo,JunYuan, 11(2019),1303–1315.
JianminWang,andJiaguangSun.2020.ApacheIoTDB:Time-seriesdatabasefor [67] SusikYoon,Jae-GilLee,andByungSukLee.2020.UltrafastLocalOutlierDe-
InternetofThings.Proc.VLDBEndow.13,12(2020),2901–2904. tectionfromaDataStreamwithStationaryRegionSkipping.InKDD.ACM,
[60] FrankWilcoxon.1992.Individualcomparisonsbyrankingmethods.InBreak- 1181–1191.
throughsinstatistics.Springer,196–202. [68] MohammedJ.ZakiandWagnerMeiraJr.2014. DataMiningandAnalysis:
[61] RenjieWuandEamonnKeogh.2021. Currenttimeseriesanomalydetection FundamentalConceptsandAlgorithms.CambridgeUniversityPress.
benchmarksareflawedandarecreatingtheillusionofprogress.IEEETransactions [69] YongZou,MarcoThiel,M.CarmenRomano,andJürgenKurths.2007. Ana-
onKnowledgeandDataEngineering(2021). lyticalDescriptionofRecurrencePlotsofDynamicalSystemswithNontrivial
Recurrences.Int.J.Bifurc.Chaos17,12(2007),4273–4283.
496