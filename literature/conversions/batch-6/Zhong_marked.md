---
conversion_metadata:
  converted_at: "2026-07-21T10:07:07Z"
  converter_tool: "markitdown"
  converter_version: "0.1.6"
  source_pdf: "Zhong.pdf"
  source_pdf_sha256: "2f725d1b7d7412c203d3e9e27d6458ef7284a32e18974ce5491ad5c056c29096"
  page_count: 10
  markdown_char_count: 95514
---

<!-- PAGE-AWARE EXTRACTION (via pdfminer.six) -->

<!-- PAGE 1 -->

Adaptive Anomaly Detection Threshold for Financial Data
Quality Monitoring Based on Time Series Features
Minju Zhong∗
M.S. in Analytics
University of Chicago
Chicago, USA
jack33361@gmail.com

Abstract
As financial data streams evolve continuously with changing
anomalous patterns and customer behaviors, traditional static
threshold-based anomaly detection systems exhibit significant limi-
tations in adapting to distributional shifts, leading to elevated false
positives and compromised detection accuracy. In the context of
financial transaction monitoring, it becomes crucial to distinguish
between natural distribution changes and genuine anomalies while
maintaining operational efficiency. This paper addresses the chal-
lenge of training with only normal data initially, while subsequent
streaming data contains both normal and anomalous instances, ne-
cessitating adaptive threshold management. We propose a dynamic
threshold adjustment framework that leverages time series feature
extraction combined with unsupervised learning techniques to cal-
ibrate detection thresholds based on evolving data characteristics
automatically. Our methodology integrates sliding window sta-
tistical analysis with Bayesian change point detection algorithms
to identify significant pattern shifts. At the same time, ensemble
approaches combining Isolation Forest, DBSCAN clustering, and
Local Outlier Factor provide robust anomaly scoring mechanisms.
The framework uses seasonal decomposition and trend analysis to
capture temporal dependencies in financial transaction data. Exper-
imental results on synthetic financial datasets demonstrate superior
performance compared to fixed threshold approaches, achieving a
precision of 0.847, a recall of 0.891, and an F1-score of 0.868, with
a substantial 46.5% reduction in false favorable rates while main-
taining real-time processing capabilities for regulatory compliance
requirements.

CCS Concepts
• Computing methodologies → Machine learning; Learning
paradigms.

Keywords
Adaptive threshold, financial data quality, Time series anomaly
detection, Unsupervised learning

∗Corresponding author

This work is licensed under a Creative Commons Attribution 4.0 International License.
AICSS 2025, Beijing, China
© 2025 Copyright held by the owner/author(s).
ACM ISBN 979-8-4007-2100-7/2025/09
https://doi.org/10.1145/3776759.3776850

ACM Reference Format:
Minju Zhong. 2025. Adaptive Anomaly Detection Threshold for Financial
Data Quality Monitoring Based on Time Series Features. In 2025 Interna-
tional Symposium on Artificial Intelligence and Computational Social Sciences
(AICSS 2025), September 19–21, 2025, Beijing, China. ACM, New York, NY,
USA, 10 pages. https://doi.org/10.1145/3776759.3776850

1 INTRODUCTION
1.1 Research Background and Motivation
With millions of transactions being processed every day by banks,
the data is vast and needs to be monitored with one eye looking for
expected activity and the other looking for anomalies. A service ob-
serving the current data quality is not sufficient for the development
of transaction patterns and more complex anomalous patterns [1].
Threshold-based recognition fails to adapt to dynamic transaction
patterns, which leads to high false positives and missed detections.
The complexity of financial data streams makes it hard to utilize
traditional monitoring means directly. Transaction systems have
specific difficulties regarding temporal changes; the spending be-
haviour calendar of a given consumer can indeed vary along the
year, and also customer demographics are somewhat moving tar-
gets; and last but not least, new anomalous methods may make
one’s gained efficiency over specific static threshold settings be-
come out of date [2]. Adaptive threshold evolution is the next step
in addressing these operational issues and continues to support the
system’s effective performance. However, the challenges of quality
for financial firms are not only in operations but also extend to
how the firm enforces regulations and manages risk. Supervisory
stress testing regimes such as CCAR and DFAST impose stringent
requirements on the validation process and have made the accurate
identification of anomalies an integral aspect of satisfying regula-
tion [3]. Solution: Innovative, evolutionary adaptive thresholds that
satisfy these conditions offer a more effective choice for detecting
novel anomalous patterns.

1.2 Problem Statement and Objectives
The static threshold-based treatment in payment card surveillance
systems has an inherent weakness for all types of transaction pat-
terns, ranging from slow upsurges to complete trend reversals, as
well as from the related customer lifestyle changes. Static threshold
settings do not adapt to genuine differences in purchasing policies,
seasonal buying, or evolving customer preferences, leading to many
false alarms, increased operational costs, and reduced system ef-
ficiency [4]. Therefore, the primary focus of the study here is on
how to develop an adaptive threshold architecture, which is capa-
ble of dynamically changing detection parameters to adapt to the

---

<!-- PAGE 2 -->

AICSS 2025, September 19–21, 2025, Beijing, China

Minju Zhong

time-series patterns of the financial transaction data. At its heart,
it is an attempt to increase detection reliability and minimize false
positives through wise calibration of thresholds based on temporal
transaction patterns [5]. The paper serves a practical purpose of
adaptively adjusting the threshold of the peak detector based on the
environment without constantly requiring manual recalibration.
Expected research contributions include better data governance,
which will be achieved by having a better anomaly detection per-
formance, a reduction of operational burden due to decreasing false
positives in anomaly detection, or better regulatory compliance
due to accurate detection of real quality issues for users.

1.3 Paper Structure and Contributions
Some new features of our adaptive threshold framework are not
available for financial transaction analysis. The problem is much
more complex if nonstationary settings are to be considered. In
this Paper, we make the following contributions: (1) we propose
a dynamic threshold learning technique by analyzing the sliding
window statistical properties; (2) we combine different unsuper-
vised learning techniques to improve the anomaly score; (3) we
propose a way of automatically tuning the parameters to tackle
changes in data characteristics [6] [7]. The time series features ex-
traction techniques considered in this work for the detection of
financial transaction sequences able to describe the temporal pat-
terns characteristic of these sequences are the frequency domain,
seasonal decomposition, and statistical trend analysis. All of these
perceptual aspects of behavior tune a finer-grained threshold and
discover the requisite exceptions in various transactional scenarios,
such as customer behaviour [8]. The proposed framework can be
applied to quality control systems requiring regulatory compliance,
operational cost reduction through decreased false positives, and
enhanced risk management capabilities.

2 RELATED WORK AND LITERATURE

REVIEW

2.1 Time Series Anomaly Detection in the

Financial Domain

The seminal literature on the detection of financial anomalies is
grounded in statistical control models, for which the origin is rooted
in the idea of control charts. The concept was to use abnormality
detection (e.g., control charts and weighted moving averages) in
the same manner as it had become successful for the application
in quality control processes. Some attempts have been made in
the introduced set of methods to at least provide a point of depar-
ture for dealing with this problem. Still, they limit themselves to
simple cases when complex time dependence and more complex
nonstationary motion of high-dimensional financial data are typical
[9]. With time series transaction monitoring, powered by machine
learning, these methods have completely flipped the field on its
head. For example, the learning architectures of ensemble methods
and deep learning can now discern extremely subtle patterns in fi-
nancial streams of data. Adaptive anomaly detection has succeeded
in RL-based approaches [10]. Moreover, in comparison to conven-
tional rule-based approaches, GNNs can better be used to detect
anomalies in an evolving network setting. These results show that

the adaptability of financial anomaly detection systems is becoming
more and more emphasized. Anomaly detection in banking: We
notice a significant difference across banking anomaly detection
systems in terms of characteristics in data undertaking and the op-
erating environment. Sequential analysis by a deep learned LSTM
architecture experienced enhanced detection, especially under early
stopping to prevent overfitting on dynamic financial markets. Fed-
erated learning algorithms have been considered to be an approach
with the best performance for private anomaly detection in the
significantly different environments of different banks.

2.2 Adaptive Threshold Techniques and

Applications

Thresholding of adaptivity in stream processing has developed
from simple statistical algorithms to complex machine learning al-
gorithms processing non-trivial temporal patterns and concept drift.
Rule-based decision lists in federated learning for credit card anom-
aly detection. This present work represents a notable advancement
as the decision list acts as an adaptive thresholding application to
improve prediction accuracy under the privacy constraint or pri-
vacy preservation. Setting thresholds continuously in a changing
environment based on machine learning, reinforcement learning,
and neural networks, swarm intelligence was employed to detect
and tune the parameters of streaming data characteristics automati-
cally. In the domain of credit card anomaly detection, architectures
that can provide explanations and interpretations, such as TabNet,
are particularly promising in the sense that they not only can offer
explanations and interpretations while detecting but also have per-
formance not worse than any state-of-the-art methods reported so
far. Adaptive thresholding in financial anomaly detection systems
has led to significant breakthroughs in detection rate as well as
operational efficiency. Some GRU network-based methods working
in the past few years showed satisfactory results in such a field as
financial anomaly detection, especially together with ensembling,
when a couple of algorithms met in the centre in order to have
another algorithm to decide whose side it is. What these develop-
ments reinforce is the need for agile responses in order to address
upcoming anomalies and evolving consumer behaviour.

2.3 Financial Data Quality Monitoring Systems
The current practice of financial data (1) governance (i.e., data
quality control) is to generate automated monitoring components
tasked with a massive scale of transactions at high accuracy and
efficiency requirements. Having learned about these insights, the
machine-learning-based algorithms behind credit card anomaly
detection return that knowledge to the flow of new transactions
in real-time, where all sorts of transaction patterns can be seen.
Banking’s data quality asks are growing to ask for end-to-end vali-
dation frameworks—not only for source systems to operating sys-
tems, but around the operating systems. Structural data quality
challenges stemming from the consolidation of large and growing
monitoring datasets are also mainly due to supervisory-led stress
testing programs (e.g., CCAR, DFAST) that necessitate strong data
quality practices, which mandate the ability to detect and resolve
exceptions early enough to prevent downstream adverse effects, i.e.,
reporting or regulatory penalties. Banking competition requires

---

<!-- PAGE 3 -->

Adaptive Anomaly Detection Threshold for Financial Data Quality Monitoring Based on Time Series Features

AICSS 2025, September 19–21, 2025, Beijing, China

Table 1: Adaptive Threshold Algorithm Parameters

Parameter

Window Size (W)
Sensitivity Factor (𝛼)
Decay Factor (𝛽)
Change Point Threshold (𝛾)

Description

Default Value

Range

Number of observations in the sliding window
Threshold adjustment sensitivity
Historical weight decay rate
Statistical significance for pattern changes

1000
0.15
0.95
0.01

500-5000
0.05-0.30
0.80-0.99
0.001-0.05

these standards to correspond to more sophisticated techniques of
anomaly detection. The combination of different types of corpo-
rates, located in different financial data systems, into one financial
(IT) system is a complex challenge in the sense that it needs moni-
toring capabilities that cross such technological borders and data
sources. Under the context of deep learning, LSTM, as a sequence
analysis, shows better performance in dynamic financial system
detection, and it has been enhanced by early stopping to avoid
overfitting [11].

3 METHODOLOGY
3.1 Adaptive Threshold Framework Design
Our algorithm uses sliding window statistical analysis to calculate
both global and local parameters for threshold adjustment. The
framework employs a multi-module design where sliding window
analysis continuously monitors transaction patterns. Each module
processes incoming transaction data to calculate statistical param-
eters for threshold adjustment. Through this adaptive learning
process, threshold boundaries automatically adjust based on de-
tected changes in data characteristics.

Time series segmentation becomes an essential component of
adaptive thresholds and uses statistical change point detection
algorithms to determine major pattern shifts that require adjust-
ment in detected thresholds. Thus, the process of segmentation
is done with Bayesian change point detection detectors that are
used together with information-theoretical criteria and evidence
for detected changes.

The system continuously evaluates detection performance and
automatically adjusts threshold parameters to minimize both false
positives and missed detections while maintaining system efficiency.
The key parameters of the adaptive threshold algorithm are sum-
marized in Table 1.

Note that the number of its transactions is a measure of the
Window Size. Sensitivity Factor and Decay Factor are both di-
mensionless ratios. However, the Change Point Threshold is the
statistical significance level (𝛼-levels) for pattern shifts: its default
value was set by cross-validation tests on synthetic financial data.
The adaptive threshold 𝜏(t) at time t is computed using an exponen-
tial decay function:

𝜏 (𝑡) = 𝜇 (𝑡) + 𝛼 × 𝜎 (𝑡) × 𝛽 (𝑡 − 𝑡0)
(1)
where 𝜇(t) is the mean of observations in the current window, 𝜎(t)
is the standard deviation, 𝛼 is the sensitivity factor controlling
threshold strictness, 𝛽 is the decay factor (0 < 𝛽 < 1) that reduces
the influence of historical information, and t0 is the reference time
point. This formulation enables automatic threshold adjustment
based on current data characteristics while maintaining stability

through historical context weighting. Additionally, robust parame-
ter estimation within each window employs estimators that were
designed to minimize the impact of ”outliers” but remain sensitive
to fundamental pattern changes.

3.2 Time Series Feature Extraction for Financial

Data

To infer the timing of credit card transaction patterns requires a full
investigation of how timing can express itself in transactions. The
feature extraction process analyzes temporal relationships within
transaction sequences to identify characteristic patterns. This pro-
cess captures various statistical properties and temporal dependen-
cies that define normal transaction behavior. With the development
of technology in the past few years, people have applied many new
techniques for financial time series trend analysis, including ad-
vanced statistical methods.

How does volatility change over the time profile of transactions?
Features of various distributions—statistical feature engineering on
transaction amount and frequency analysis includes calculations
for moving averages (rolling stats), methods that are based on the
percentiles, and measures to capture the essential properties of
transaction sequences. The feature extraction algorithm carries out
statistical computations that change with time—such as moving
average levels and standard deviations, skewness, and kurtosis over
different horizons—providing a comprehensive characterization of
transaction patterns.

Formally, for a transaction sequence X = {x₁, x₂, …, xₙ}, we com-

pute:

𝑀𝑜𝑣𝑖𝑛𝑔𝐴𝑣𝑒𝑟𝑎𝑔𝑒 : 𝑀𝐴 (𝑡) = (1/𝑊 ) ·

(cid:213)

𝑖=1

𝑊+1𝑡 · 𝑥𝑖

𝑀𝑜𝑣𝑖𝑛𝑔𝑆𝑡𝑎𝑛𝑑𝑎𝑟𝑑𝐷𝑒𝑣𝑖𝑎𝑡𝑖𝑜𝑛 :
𝜎 (𝑡) =

[(1/𝑊 ) (cid:205)𝑖=1 𝑊+1𝑡 (𝑥𝑖 − 𝑀𝐴 (𝑡))]

√

(2)

(3)

𝑆𝑘𝑒𝑤𝑛𝑒𝑠𝑠 : 𝛾1 (𝑡) = 𝐸 (cid:2)(𝑋 − 𝜇)3(cid:3) /𝜎3
𝐾𝑢𝑟𝑡𝑜𝑠𝑖𝑠 : 𝛾2 (𝑡) = 𝐸 (cid:2)(𝑋 − 𝜇)4(cid:3) /𝜎4
(5)
where W is the window size, E[·] denotes expectation, 𝜇 is the mean,
and 𝜎 is the standard deviation.

(4)

Figure 1 illustrates the architecture of our time series feature ex-
traction pipeline. The core decomposition process involves seasonal
analysis, exponential smoothing techniques, and trend analysis.

The core decomposition process involves seasonal analysis, expo-
nential smoothing techniques, and trend analysis. To disassemble
the time series of transactions, we use different decomposing tech-
niques to separate its trends, seasonality components, and residu-
als. The inputs for threshold amount adjustment methods, which
will adapt predictably according to known seasonal changes and

---

<!-- PAGE 4 -->

AICSS 2025, September 19–21, 2025, Beijing, China

Minju Zhong

Figure 1: Time Series Feature Extraction Pipeline Architecture

underlying trend patterns, are these components that have been
decomposed into their constituent parts.

The feature extraction pipeline will integrate multiple parallel
processing streams to offer a full-thumbnail characterization of
transaction patterns, both for computational efficiency in real-time
applications and to ensure recognizability. Each processing stream
studies different aspects of transactional behaviour, including its
time dependencies, statistical properties, and frequency domain
patterns characteristic of transaction sequences that contribute to
adaptive threshold computation.

while at the same time being sensitive to unconventional behaviour
[13].

Integrated ensemble methods are adopting multiple unsuper-
vised algorithms. It gives better robustness and accuracy through
the weighted combination of each individual algorithm. The ensem-
ble approach integrates Isolation Forest, DBSCAN clustering, and
Local Outlier Factor algorithms, with dynamic weight adjustment
depending on different data regimes and transaction modes.

The ensemble anomaly score S(x) for transaction x combines

multiple algorithms:

3.3 Unsupervised Learning Integration
Robust anomaly detection capabilities that complement the adap-
tive threshold mechanism are provided by the implementation of
an Isolation Forest for outlier score computation. The former only
makes binary judgments, while the latter generates continuous
anomalies. Isolation Forest’s parameters are subjected to dynamic
optimisation based on data characteristics, with contamination rates
and tree depth parameters being optimised through cross-validation
techniques that consider temporal dependencies in financial data
[12].

DBSCAN clustering for transaction pattern identification lays
the foundations for adaptive batch- and cross-customer calibration.
Adaptive transaction type-based behavioural groupings are made
in order to help establish thresholds. Clustering is able to apply
distance metrics that consider transaction proximity as well as
volume to achieve effective classification of similar transactions

𝑆 (𝑥) = Σ𝑀
𝑗=1

𝑤 𝑗 × 𝑠 𝑗 (𝑥)

(6)

where M is the number of algorithms (M=3: Isolation Forest, DB-
SCAN, Local Outlier Factor), 𝑠 𝑗 (𝑥) is the normalized anomaly score
from algorithm j, and 𝑤 𝑗 is the dynamic weight satisfying (cid:205) 𝑤 𝑗 =
1. Weights are updated based on algorithm reliability:

𝑤 𝑗 (𝑡) = 𝐴𝑈𝐶_𝑅𝑂𝐶 𝑗 (𝑡) /Σ𝑀
𝑘=1

𝐴𝑈𝐶_𝑅𝑂𝐶𝑘 (𝑡)

(7)

where 𝐴𝑈𝐶_𝑅𝑂𝐶 𝑗 (𝑡) is the area under the ROC curve for algorithm
j at time t, evaluated on recent validation data. The detailed configu-
ration parameters and optimization methods for each unsupervised
learning algorithm are presented in Table 2.

The integration framework you designed serves not only to
balance weights between the different unsupervised algorithms but
to provide seamless coordination among them within a real-time
processing scenario. The algorithm output is combined through
weighted voting, considering the reliability of individual algorithms
in addition to performance-dependent on the nature of the data.

---

<!-- PAGE 5 -->

Adaptive Anomaly Detection Threshold for Financial Data Quality Monitoring Based on Time Series Features

AICSS 2025, September 19–21, 2025, Beijing, China

Table 2: Unsupervised Learning Algorithm Configuration

Algorithm

Isolation Forest
DBSCAN
Local Outlier Factor

Key Parameters

Optimization Method

Performance Metric

n_estimators=200, contamination=auto
eps=adaptive, min_samples=10
n_neighbors=20, contamination=0.1

Grid Search CV
Silhouette Analysis
Bayesian Optimization

AUC-ROC
Cluster Validity
Precision-Recall

Dynamically adjust DBSCAN’s parameters for Adaptive Selec-

tion:

DBSCAN’s 𝜖 parameter adapts to local data density through:
𝜀 (𝑖) = 𝑃𝑒𝑟𝑐𝑒𝑛𝑡𝑖𝑙𝑒90 (𝐷_𝑘 (𝑊𝑖 ))
where D_k(Wᵢ) = {d_k(p) | p ∈ Wᵢ} represents the set of k-nearest
neighbor distances for all points p in window Wᵢ, and d_k(p) is
the distance from point p to its kth nearest neighbor. The 90th
percentile ensures robustness across varying transaction densities
while maintaining sensitivity to outlier patterns. The min_samples
parameter is fixed at 10 to ensure reliable cluster formation while
detecting irregular transaction patterns.

(8)

4 EXPERIMENTAL DESIGN AND

IMPLEMENTATION

4.1 Dataset Description and Preprocessing
As a result, we routinely create simulated Monte Carlo transactions.
These transactions, using the attributes of everyday sales items, pay-
ment for various commodities, position in a working day or season
of the year (occasions such as birthdays and Christmas, contracep-
tives, etc.), and various forms of transactional anomalies, including
unusual transaction amounts and timing patterns that represent
data quality issues in standard credit cards. After statistical models
of real transactions are turned into records in the manner above,
they have to be transferred into a particular form of publicised mask
that cannot be commonly recognised. The synthetic data genera-
tion process incorporates various anomaly patterns that challenge
detection systems, including those designed for interpretable archi-
tectures such as TabNet[14], ensuring comprehensive evaluation of
the proposed adaptive threshold framework. The comprehensive
characteristics and statistics of our synthetic dataset are detailed in
Table 3.

Before we go on, remember that handling missing data points in a
data preprocessing task of such magnitude is just one step. Missing
values are handled by the code with methods such as temporal
interpolation, which preserve statistical properties embedded in
the sequences of transactions. Noise reduction algorithms use
adaptive filtering to distinguish between measurement noise and
the legitimate transaction variance, so as to retain the essential
pattern information based on sound data quality considerations.
Feature standardization methods use robust scaling techniques that
are less susceptible to outliers but still allow relative transaction
characteristic relationships to be kept. Precise timed registration
processing needs to be described so that the time index of each data
source is consistent with real-world financial data streams. Also, the
processing-induced operation delays and system latencies found in
such streams must not be lost. Naturally, different versions of data
often have time indexing that deviates from each other. Therefore,

we alter the time indices produced by long delays and poor network
bandwidth of actual financial data streams to generate data sets
that are more in line with our own research personnel’s physical
medium.

This synthetic dataset contains multiple types of anomalies, in-
cluding sudden increase gaps, atypical geographical backgrounds,
the time of year when this happens being nonseasonal, and devi-
ations from the everyday trading categories scenarios. Statistical
verification suggests that we have effectively captured in this ar-
tificial material not just the facts about transactions but also their
realistic interrelationships and dependencies from the original au-
thentic material.

Synthetic Data Limitations and Real-World Considerations.
4.1.1
While synthetic datasets enable controlled experimentation and
reproducibility, several important distinctions from real financial
data warrant discussion:

Data Distribution Characteristics: Real financial transaction data
exhibits complex, evolving patterns influenced by macroeconomic
factors, regulatory changes, and emergent fraud tactics that are dif-
ficult to fully capture in synthetic generation models. Our synthetic
data approximates statistical properties of real transactions through
parametric modeling, but may not fully represent the long-tail dis-
tributions and rare event combinations present in actual financial
systems.

Temporal Dependencies: Real-world financial data contains in-
tricate temporal correlations spanning multiple time scales—from
intraday trading patterns to multi-year economic cycles. While
our synthetic generation incorporates daily and seasonal patterns
based on statistical models, it may not capture all nuanced temporal
dependencies present in operational financial systems, particularly
those arising from external economic shocks or unprecedented
market events.

Anomaly Representation: The synthetic anomalies in our dataset
are generated based on known patterns (unusual amounts, timing
deviations, geographical inconsistencies). Real-world anomalies
may exhibit novel characteristics not represented in historical pat-
terns, presenting additional challenges for detection systems. This
limitation is partially mitigated by our adaptive threshold frame-
work’s unsupervised learning approach, which can identify de-
viations from learned normal patterns without requiring labeled
anomaly examples.

Privacy and Data Access Constraints: The use of synthetic data
was necessitated by privacy regulations and proprietary constraints
preventing access to real financial transaction data. While this
limits direct validation against operational systems, it enables re-
producible research and algorithm comparison without exposing
sensitive customer information or institutional data.

---

<!-- PAGE 6 -->

AICSS 2025, September 19–21, 2025, Beijing, China

Minju Zhong

Table 3: Dataset Characteristics and Statistics

Characteristic

Training Set

Validation Set

Total Transactions
Anomaly Rate (%)
Temporal Span (days)
Customer Accounts
Transaction Types
Average Daily Volume
Peak Daily Volume
Minimum Daily Volume

2,847,392
2.14 ± 0.08
365
48,750
16
7,801 ± 342
12,847
4,231

356,741
2.31 ± 0.12
45
12,188
14
7,927 ± 289
11,203
4,892

Test Set

445,928
1.97 ± 0.09
60
15,235
15
7,432 ± 401
10,891
4,567

Validation Strategy: To address these limitations, our experimen-
tal design incorporates statistical validation ensuring the synthetic
dataset preserves key distributional properties, temporal correla-
tions, and anomaly characteristics representative of real financial
systems. Future work should include validation on anonymized real
transaction data where regulatory frameworks permit, to confirm
the framework’s effectiveness in operational environments with
full complexity of real-world financial data streams.

4.2 Performance Evaluation Metrics
Detection precision, recall, and F1-score of anomalies analysis uses
temporal cross-validation techniques to look at time-dependent
patterns in financial data, so evaluation coefficients actually reflect
actual performance characteristics. The evaluation framework in-
troduces sliding window validation approaches that respect tempo-
ral orderings but still give reliable performance evaluations across
different periods and types of data [15]. This platform was created
with the intention of keeping fast detection rates from harming
system performance. Introducing a tradeoff between detection sen-
sitivity and operating efficiency is its defining characteristic—and it
requires evaluation frameworks which will not fail to take into con-
sideration costs (of any kind). The optimisation procedure achieves
the objective of minimising false positive rates while not making de-
tection levels unacceptable by simultaneously using multi-objective
optimisation techniques.

End-to-end processing needs involve calculations of performance
measures such as efficiency analysis, throughput measurements,
latency, and resource utilization evaluation indexes, typically in-
volving transferring data from different system platforms and load
formats. Performance measurements occur under test conditions
laid down by standard benchmarks, which can be found at financial
institutions, to make the results of performance measurements bul-
letins trustworthy. Our multidimensional performance evaluation
framework is illustrated in Figure 2, which encompasses detection
accuracy, computational efficiency, and system robustness metrics.
In this framework, statistical significance testing has been in-
corporated directly so that the differences in performance between
algorithms are, in fact, real improvements and not just chance vari-
ation. By using the technique of bootstrap resampling combined
with techniques for statistical confidence interval construction, it
is possible to put robust comparisons of algorithm performance
directly before readers.

Figure 2: Multidimensional Performance Evaluation Frame-
work

4.2.1 Metric Definitions. We employ standard binary classification
metrics to evaluate anomaly detection performance:

Precision measures the proportion of correctly identified anom-

alies among all flagged transactions:

𝑃𝑟𝑒𝑐𝑖𝑠𝑖𝑜𝑛 = 𝑇 𝑃/(𝑇 𝑃 + 𝐹 𝑃)

(9)

Recall (or sensitivity) measures the proportion of actual anom-

alies successfully detected:

𝑅𝑒𝑐𝑎𝑙𝑙 = 𝑇 𝑃/(𝑇 𝑃 + 𝐹 𝑁 )

(10)

F1-Score provides the harmonic mean of precision and recall,

balancing both metrics:

𝐹 1 − 𝑆𝑐𝑜𝑟𝑒 = 2 × (𝑃𝑟𝑒𝑐𝑖𝑠𝑖𝑜𝑛 × 𝑅𝑒𝑐𝑎𝑙𝑙)/(𝑃𝑟𝑒𝑐𝑖𝑠𝑖𝑜𝑛 + 𝑅𝑒𝑐𝑎𝑙𝑙)

(11)

False Positive Rate (FPR) quantifies the proportion of normal

transactions incorrectly flagged as anomalies:

𝐹 𝑃𝑅 = 𝐹 𝑃/(𝐹 𝑃 + 𝑇 𝑁 )

(12)

where TP (True Positives) represents correctly detected anom-
alies, FP (False Positives) represents normal transactions incorrectly
flagged, FN (False Negatives) represents missed anomalies, and TN
(True Negatives) represents correctly identified normal transac-
tions.

---

<!-- PAGE 7 -->

Adaptive Anomaly Detection Threshold for Financial Data Quality Monitoring Based on Time Series Features

AICSS 2025, September 19–21, 2025, Beijing, China

Table 4: Comparative Analysis Results Summary

Method

Precision

Recall

F1-Score

FPR

Processing
Time (ms/1000
trans)

Significance
(p-value)

Fixed Threshold
Statistical
ML-based
Adaptive
Proposed
Framework

0.724 ± 0.031
0.789 ± 0.028
0.812 ± 0.025

0.831 ± 0.024
0.856 ± 0.021
0.873 ± 0.018

0.774 ± 0.022
0.821 ± 0.019
0.841 ± 0.017

0.142 ± 0.008
0.098 ± 0.006
0.089 ± 0.005

12.3 ± 1.4
18.7 ± 2.1
24.1 ± 2.8

-
p < 0.01*
p < 0.001

0.847 ± 0.023

0.891 ± 0.016

0.868 ± 0.015

0.076 ± 0.004

21.5 ± 2.3

p < 0.001

Figure 3: Algorithm Performance Comparison Across Multiple Dimensions

Processing Time measures computational efficiency in millisec-

onds per 1000 transactions, critical for real-time deployment.

4.3 Comparative Analysis Setup
Baseline comparisons with fixed threshold methods include overall
assessments that cover most anomaly detection systems commonly
prescribed in finance, causing statistical charts, percentiles, and
rule-based detection systems to be made to make a comprehensive
evaluation. The comparison framework makes sure to equalize
evaluation by using identical data sets and inspection criteria for
all methods.

Performance achieved by benchmarking against established
adaptive threshold algorithms incorporates the latest research find-
ings in dynamic threshold adjustment. Benchmark procedures
apply standardised norms of evaluation, which consider the require-
ments of various algorithms and their optimisation procedures with
rigour to ensure a comprehensive and fair performance comparison.

Sensitivity analysis on different financial data characteristics ex-
amines linkages between the algorithm’s performance and chang-
ing market conditions in the data. Studying factorial design method-
ologies has been used for this kind of inspection work. It allows
us to compare and contrast performance sensitivity under multiple
data conditions at the same time. Table 4 presents a comprehensive
summary of the comparative analysis results across all evaluated
methods.

Results represent mean ± standard deviation over 10 independent
runs. Statistical significance was determined using McNemar’s
test for model comparison and a 5x2-fold cross-validation paired
t-test with Bonferroni correction for multiple comparisons. Non-
parametric bootstrap resampling (n=1000) was applied to estimate
confidence intervals for performance metrics. *p < 0.01, p < 0.001.
FPR = False Positive Rate. Processing time measured per 1000
transactions on Intel Xeon E5-2680 v4 @ 2.40GHz with 32GB RAM.
Figure 3 provides a visual comparison of algorithm performance
across multiple evaluation dimensions, demonstrating the proposed
framework’s superiority in precision, recall, F1-score, and false
positive rate reduction compared to baseline methods.

---

<!-- PAGE 8 -->

AICSS 2025, September 19–21, 2025, Beijing, China

Minju Zhong

The framework for comparative analysis employs statistical test-
ing techniques to determine whether the performance of various
pairs of methods is very different under paired statistical tests and
effect size measurements, which can be regarded as the real-world
significance of improvements made in performance.

5 RESULTS ANALYSIS AND DISCUSSION
5.1 Experimental Results and Performance

Analysis

According to objective measures, in contrast to traditional, fixed
threshold methods, proposed adaptive thresholding frameworks
had superior performance. In this regard:

·False positive rate reductions by fully 46.5% and improvements
in F1-score accuracy increased to 12.1% were recorded; this demon-
strates improved discriminative capability in distinguishing gen-
uine anomalies from normal transaction variations.

Compared to traditional methods, the adaptive framework shows
noticeable advances in both computational efficiency and scalability.
In practice, it has better decoding speed than its old fixed-threshold
counterparts; we have to take note that memory usage analysis indi-
cates resource requirements are 23 percent lower than conventional
threshold methods. It makes adaptable thresholds suitable even
when deployed within resource-poor operational environments.

Flat growth characteristics: We have been able to show that at
different data volumes, the time to process information is extended
in a direction proportional to business size, but without sacrificing
accuracy in detection. The framework was stable across different
customer segments and transaction types, something that is crucial
for practical use in diverse financial environments requiring fault-
tolerance as a mandatory minimum criterion.

5.2 Case Study Applications
Actually, this Viewpoint paper offers an advanced method to imple-
ment adaptive thresholds, and it is this functionality of the system
which we will now present in a series of three examples designed
to show how the framework operates at ground level.

Regulatory Compliance Monitoring
Financial institutions operating under regulatory frameworks
such as CCAR and DFAST require continuous monitoring of trans-
action data quality to assure accurate stress testing and reporting.
Traditional static threshold systems often generate excessive false
positives during periods of market volatility or seasonal transaction
pattern changes, forcing manual review that consumes significant
operational resources. The adaptive threshold framework solves
this problem by automatically adjusting detection parameters based
on emerging market conditions and customer behavior patterns.

In regulatory reporting contexts, the framework’s seasonal de-
composition capabilities prove particularly valuable. Transaction
volumes and patterns show predictable variations during periods
such as year-end financial activity or holiday shopping seasons,
which static systems wrongly flag as anomalies. The adaptive way
recognizes such legitimate pattern shifts and offsetting thresholds,
while maintaining sensitivity to genuine data quality problems,
reduces false alarms.

5.2.1 Real-time Transaction Processing. Data-quality monitoring in
large-scale payment-processing environments presents particular
problems, thanks to the glaring amount and fleetness of incoming
streams that affect transaction integrity. The framework’s sliding
window approach makes continuous observation of transaction
patterns possible without needing batch processing delay, which
could disturb system performance. That ensemble method brings
Isolation Forest, DBSCAN clustering, and Local Outlier Factor algo-
rithms together to make a comprehensive anomaly scoring system,
capable of adjusting itself as transaction characteristics change in
real time.

The framework’s computational efficiency can be crucial in these
environments. Time measurements indicate that the adaptive ap-
proach can still meet very tight latency criteria under high load,
making it suitable for deployment in systems with stringent re-
sponse time requirements. The mechanism for dynamically adjust-
ing parameters ensures stable detection precision notwithstanding
how operating conditions fluctuate.

5.2.2 Cross-institutional Data Quality Assessment. Data quality
monitoring has become increasingly important for financial insti-
tutions, and this responsibility is compounded by the fact that the
information might stem across a variety of sources and jurisdic-
tional boundaries. The adaptive threshold framework’s unsuper-
vised learning approach allows it to be used in federated environ-
ments, where labeled training data can be scarce or absent. The
framework’s ability to learn normal transaction patterns from unla-
beled data streams makes it particularly suitable for establishments
implementing new monitoring systems or setting their sights on
transaction types not previously covered.

The framework’s parameter tuning capabilities enable it to be
adjusted according to different institutional settings; it can still
carry out the basic function of detection. Institutions can change
sensitivity factors and window sizes to suit their specific level of risk
without needing to retrain the underlying model. Such flexibility
means the thing can be carried out in an organization possessing
different structures and existing regulations.

5.2.3
Implementation Considerations. In practice, it is necessary
to carefully consider how the adaptive threshold framework fits
into an institution’s ongoing operations. The framework’s modular
design enables it to be integrated with existing data quality monitor-
ing infrastructure while also allowing institutions that have already
made investments in this area to pave the way for further develop-
ments. Logging of performance monitoring results and changes in
threshold settings gives insight into the decision-making processes
of the system, which supports demands for audits or the need to
supervise operations.

The framework’s capacity to conserve historical pattern informa-
tion while moving to new conditions makes sure that its detection
capabilities develop correctly with changes in the business situation.
This is a crucial compromise between flexibility and stability, allow-
ing continuous high-quality data monitoring no matter what the
prevailing market conditions or stage of growth for your institute.

---

<!-- PAGE 9 -->

Adaptive Anomaly Detection Threshold for Financial Data Quality Monitoring Based on Time Series Features

AICSS 2025, September 19–21, 2025, Beijing, China

5.3 Limitations and Future Research Directions
The problem with the proposed adaptive threshold algorithm is
that if the market is abnormal and entirely unexpected behaviour
should occur in the markets, then this approach does not handle it
well. Additionally, the evaluation on synthetic datasets, while en-
abling controlled experimentation, introduces limitations regarding
generalization to real-world financial systems. The synthetic data
generation process, though statistically calibrated to mirror real
transaction characteristics, cannot fully capture the complexity of
actual financial ecosystems, including rare combination anomalies,
emergent fraud patterns, and the full spectrum of temporal de-
pendencies present in operational data. Validation on anonymized
real-world datasets from financial institutions would provide crucial
evidence of the framework’s operational effectiveness and iden-
tify additional edge cases requiring algorithmic refinement. The
framework may face challenges when encountering unprecedented
market conditions or regulatory changes that fundamentally alter
transaction patterns beyond historical norms. Future research direc-
tions include incorporating external data sources such as social me-
dia sentiment indicators and macroeconomic statistics to enhance
feature extraction capabilities. These additional data sources could
improve detection accuracy under changing market conditions.
External data sources require preprocessing through advanced fea-
ture engineering and selection techniques. Future implementations
could incorporate federated learning approaches to enable privacy-
preserving collaboration across institutions. This approach allows
for multiple financial institutions to collaborate on anomaly de-
tection while maintaining regulatory compliance and data privacy
requirements. The use of federative approaches can improve detec-
tion accuracy, but it should also be strictly in line with requirements
for data confidentiality.

6 CONCLUSION
This research presents a comprehensive adaptive threshold frame-
work for financial data quality monitoring that successfully ad-
dresses the limitations of traditional static threshold approaches.
The proposed methodology integrates sliding window statistical
analysis with ensemble unsupervised learning techniques, achiev-
ing significant improvements in anomaly detection performance.
Experimental results demonstrate that our framework outperforms
conventional methods with a precision of 0.847, recall of 0.891, and
F1-score of 0.868, while achieving a substantial 46.5% reduction
in false positive rates. The framework’s ability to automatically
adjust detection parameters based on evolving transaction patterns
represents a significant advancement in financial data quality moni-
toring, particularly for institutions operating under strict regulatory
requirements such as CCAR and DFAST compliance.

The practical implications of this work extend beyond improved
detection accuracy to encompass operational efficiency and regu-
latory compliance benefits. The framework’s real-time processing
capabilities and modular design enable seamless integration into
existing financial monitoring infrastructure while reducing the
operational burden associated with manual threshold recalibra-
tion. However, the approach faces limitations when encountering
unprecedented market conditions that deviate significantly from

historical patterns. Future research directions should focus on in-
corporating external economic indicators and exploring federated
learning approaches to enable privacy-preserving collaboration
across financial institutions. Additionally, investigating the frame-
work’s adaptability to emerging financial technologies and transac-
tion types will be crucial for maintaining long-term effectiveness
in the rapidly evolving financial landscape.

Acknowledgments
I am grateful for the helpful study that Iqbal developed last year
with Amin, R., Alsubaei, F.S., and Alzahrani. Their research focuses
on an abnormal intelligent centre using cloud monitoring data of
multivariate time series, which is made easier than ever before
by using deep ensemble method models. ”Anomaly detection in
multivariate time series data using deep ensemble models” Paper
reported in Plos One (2024) [1]. As a result, my understanding
of the deep ensemble method in time series anomaly detection
has been deepened, and this has changed how I look at advanced
techniques for multivariate financial data analysis. Included are
also notes, which I acknowledge Asmar, M., and Aqel, B.Y., for their
study on credit card anomaly detection analysis from a process
and techniques perspective. The paper ”Analysis of credit card
anomaly detection: process and techniques perspective” appeared
in Artificial Intelligence (AI) and Finance (2023) [2]. Their analysis
of the procedure and means of infection for detection processing,
however, has enhanced my understanding of financial anomaly
detection systems and research into adaptive methods of financial
data quality monitoring with abnormal detection frameworks.

References
[1] Iqbal, A., Amin, R., Alsubaei, F. S., & Alzahrani, A. (2024). Anomaly detection
in multivariate time series data using deep ensemble models. Plos one, 19(6),
e0303890.

[2] Asmar, M., & Aqel, B. Y. (2023). Analysis of credit card anomaly detection: process
and techniques perspective. In Artificial Intelligence (AI) and Finance (pp. 899-
911). Cham: Springer Nature Switzerland.

[3] Liu, H. (2025). Multi-variable time-series anomaly detection for intelligent opera-
tion and maintenance. In 2025, the 5th International Symposium on Computer
Technology and Information Science (ISCTIS) (pp. 1030-1034, 2025, May). IEEE.
[4] Jain, J.S., Sapra, A., Gupta, A., Dagar, L., & Niranjan, V. (2025). Performance
Analysis of Machine Learning Models and Deep Learning Models for Credit Card
Anomaly Detection. In 2025, the 3rd International Conference on Communication,
Security, and Artificial Intelligence (ICCSAI) (Vol. 3, pp. 1533-1538, 2025, April).
IEEE.

[5] Chen, Z., Wang, S., Yan, D., & Li, Y. (2023). Research and implementation of
a bank credit card anomaly detection system based on reinforcement learning
and LSTM. In 2023, the 3rd International Conference on Mobile Networks and
Wireless Communications (ICMNWC) (pp. 1-8, 2023, December). IEEE.

[6] Ida, S. J., & Balasubadra, K. (2024). Enhancing credit card anomaly detection
through LSTM-based sequential analysis with early stopping. In 2024 2nd In-
ternational Conference on Networking and Communications (ICNWC) (pp. 1-6,
2024, April). IEEE.

[7] Chen, Y., Zhao, C., Xu, Y., & Nie, C. (2025). Year-over-year developments in
financial anomaly detection via deep learning: A systematic literature review.
arXiv preprint arXiv:2502.00201.

[8] Sathe, R., & Shinde, S. (2024,). A Deep Learning Framework for Effective Anomaly
Detection in Time Series Data. In 2024 4th Asian Conference on Innovation in
Technology (ASIANCON) (pp. 1-7, 2024, August). IEEE.

[9] Cui, Y., Han, X., Chen, J., Zhang, X., Yang, J., & Zhang, X. (2025). FraudGNN-RL: a
graph neural network with reinforcement learning for adaptive financial anomaly
detection. IEEE Open Journal of the Computer Society.

[10] Suganthi, V., & Jebathangam, J. (2024). A Novel Approach for Credit Card anomaly
detection using Gated Recurrent Unit (GRU) Networks. In 2024 8th International
Conference on I-SMAC (IoT in Social, Mobile, Analytics and Cloud) (I-SMAC)
(pp. 1716-1721, 2024, October). IEEE.

---

<!-- PAGE 10 -->

AICSS 2025, September 19–21, 2025, Beijing, China

Minju Zhong

[11] Tang, Y., & Liu, Z. (2024). A Credit Card anomaly detection Algorithm Based on

IEEE/CAA Journal of Automatica Sinica.

SDT and Federated Learning. IEEE Access, 12, 182547-182560.

[12] Chidambaranathan, P., & MuthuPriya, V. (2024). Risk Prediction in Financial
Transactions Using IoT Big Data Analytics. In 2024 5th International Conference
on Electronics and Sustainable Communication Systems (ICESC) (pp. 328-332,
2024, August). IEEE.

[13] Xie, Y., Zhou, M., Liu, G., Wei, L., Zhu, H., & De Meo, P. (2025). A transactional-
behavior-based hierarchical gated network for credit card anomaly detection.

[14] Meng, C. C., Lim, K. M., Lee, C. P., & Lim, J. Y. (2023, August). Credit Card anomaly
detection using TabNet. In 2023 11th International Conference on Information
and Communication Technology (ICoICT) (pp. 394-399). IEEE.

[15] Alamri, M. A., & Ykhlef, M. A. (2023). A Machine Learning-Based Framework
for Detecting Credit Card Anomalies and Fraud. In 2023 27th International
Conference on Information Technology (IT) (pp. 1-7, 2023, February). IEEE.

<!-- MARKITDOWN CONVERSION -->

<!-- Full MarkItDown conversion for formatting fidelity. -->

Adaptive Anomaly Detection Threshold for Financial Data
Quality Monitoring Based on Time Series Features
∗
MinjuZhong
M.S.inAnalytics
UniversityofChicago
Chicago,USA
jack33361@gmail.com
Abstract ACMReferenceFormat:
As financial data streams evolve continuously with changing MinjuZhong.2025.AdaptiveAnomalyDetectionThresholdforFinancial
DataQualityMonitoringBasedonTimeSeriesFeatures.In2025Interna-
anomalous patterns and customer behaviors, traditional static
tionalSymposiumonArtificialIntelligenceandComputationalSocialSciences
threshold-basedanomalydetectionsystemsexhibitsignificantlimi-
(AICSS2025),September19–21,2025,Beijing,China.ACM,NewYork,NY,
tationsinadaptingtodistributionalshifts,leadingtoelevatedfalse
USA,10pages.https://doi.org/10.1145/3776759.3776850
positivesandcompromiseddetectionaccuracy. Inthecontextof
financialtransactionmonitoring,itbecomescrucialtodistinguish 1 INTRODUCTION
betweennaturaldistributionchangesandgenuineanomalieswhile
1.1 ResearchBackgroundandMotivation
maintainingoperationalefficiency.Thispaperaddressesthechal-
lengeoftrainingwithonlynormaldatainitially,whilesubsequent Withmillionsoftransactionsbeingprocessedeverydaybybanks,
streamingdatacontainsbothnormalandanomalousinstances,ne- thedataisvastandneedstobemonitoredwithoneeyelookingfor
cessitatingadaptivethresholdmanagement.Weproposeadynamic expectedactivityandtheotherlookingforanomalies.Aserviceob-
thresholdadjustmentframeworkthatleveragestimeseriesfeature servingthecurrentdataqualityisnotsufficientforthedevelopment
extractioncombinedwithunsupervisedlearningtechniquestocal- oftransactionpatternsandmorecomplexanomalouspatterns[1].
ibratedetectionthresholdsbasedonevolvingdatacharacteristics Threshold-basedrecognitionfailstoadapttodynamictransaction
automatically. Ourmethodologyintegratesslidingwindowsta- patterns,whichleadstohighfalsepositivesandmisseddetections.
tisticalanalysiswithBayesianchangepointdetectionalgorithms Thecomplexityoffinancialdatastreamsmakesithardtoutilize
toidentifysignificantpatternshifts. Atthesametime,ensemble traditionalmonitoringmeansdirectly.Transactionsystemshave
approachescombiningIsolationForest,DBSCANclustering,and specificdifficultiesregardingtemporalchanges;thespendingbe-
LocalOutlierFactorproviderobustanomalyscoringmechanisms. haviourcalendarofagivenconsumercanindeedvaryalongthe
Theframeworkusesseasonaldecompositionandtrendanalysisto year,andalsocustomerdemographicsaresomewhatmovingtar-
capturetemporaldependenciesinfinancialtransactiondata.Exper- gets;andlastbutnotleast,newanomalousmethodsmaymake
imentalresultsonsyntheticfinancialdatasetsdemonstratesuperior one’sgainedefficiencyoverspecificstaticthresholdsettingsbe-
performancecomparedtofixedthresholdapproaches,achievinga comeoutofdate[2].Adaptivethresholdevolutionisthenextstep
precisionof0.847,arecallof0.891,andanF1-scoreof0.868,with inaddressingtheseoperationalissuesandcontinuestosupportthe
asubstantial46.5%reductioninfalsefavorablerateswhilemain- system’seffectiveperformance.However,thechallengesofquality
tainingreal-timeprocessingcapabilitiesforregulatorycompliance forfinancialfirmsarenotonlyinoperationsbutalsoextendto
requirements. howthefirmenforcesregulationsandmanagesrisk.Supervisory
stresstestingregimessuchasCCARandDFASTimposestringent
CCSConcepts requirementsonthevalidationprocessandhavemadetheaccurate
• Computing methodologies → Machine learning; Learning identificationofanomaliesanintegralaspectofsatisfyingregula-
tion[3].Solution:Innovative,evolutionaryadaptivethresholdsthat
paradigms.
satisfytheseconditionsofferamoreeffectivechoicefordetecting
novelanomalouspatterns.
Keywords
Adaptivethreshold, financialdataquality, Timeseriesanomaly 1.2 ProblemStatementandObjectives
detection,Unsupervisedlearning
Thestaticthreshold-basedtreatmentinpaymentcardsurveillance
systemshasaninherentweaknessforalltypesoftransactionpat-
∗Correspondingauthor terns,rangingfromslowupsurgestocompletetrendreversals,as
wellasfromtherelatedcustomerlifestylechanges.Staticthreshold
settingsdonotadapttogenuinedifferencesinpurchasingpolicies,
seasonalbuying,orevolvingcustomerpreferences,leadingtomany
ThisworkislicensedunderaCreativeCommonsAttribution4.0InternationalLicense. falsealarms,increasedoperationalcosts,andreducedsystemef-
AICSS2025,Beijing,China ficiency[4]. Therefore,theprimaryfocusofthestudyhereison
©2025Copyrightheldbytheowner/author(s).
howtodevelopanadaptivethresholdarchitecture,whichiscapa-
ACMISBN979-8-4007-2100-7/2025/09
https://doi.org/10.1145/3776759.3776850 bleofdynamicallychangingdetectionparameterstoadapttothe
578

AICSS2025,September19–21,2025,Beijing,China MinjuZhong
time-seriespatternsofthefinancialtransactiondata. Atitsheart, theadaptabilityoffinancialanomalydetectionsystemsisbecoming
itisanattempttoincreasedetectionreliabilityandminimizefalse moreandmoreemphasized. Anomalydetectioninbanking: We
positivesthroughwisecalibrationofthresholdsbasedontemporal noticeasignificantdifferenceacrossbankinganomalydetection
transactionpatterns[5]. Thepaperservesapracticalpurposeof systemsintermsofcharacteristicsindataundertakingandtheop-
adaptivelyadjustingthethresholdofthepeakdetectorbasedonthe eratingenvironment. SequentialanalysisbyadeeplearnedLSTM
environmentwithoutconstantlyrequiringmanualrecalibration. architectureexperiencedenhanceddetection,especiallyunderearly
Expectedresearchcontributionsincludebetterdatagovernance, stoppingtopreventoverfittingondynamicfinancialmarkets.Fed-
whichwillbeachievedbyhavingabetteranomalydetectionper- eratedlearningalgorithmshavebeenconsideredtobeanapproach
formance,areductionofoperationalburdenduetodecreasingfalse withthebestperformanceforprivateanomalydetectioninthe
positivesinanomalydetection,orbetterregulatorycompliance significantlydifferentenvironmentsofdifferentbanks.
duetoaccuratedetectionofrealqualityissuesforusers.
2.2 AdaptiveThresholdTechniquesand
1.3 PaperStructureandContributions Applications
Somenewfeaturesofouradaptivethresholdframeworkarenot Thresholding of adaptivity in stream processing has developed
availableforfinancialtransactionanalysis. Theproblemismuch fromsimplestatisticalalgorithmstocomplexmachinelearningal-
morecomplexifnonstationarysettingsaretobeconsidered. In gorithmsprocessingnon-trivialtemporalpatternsandconceptdrift.
thisPaper,wemakethefollowingcontributions: (1)wepropose Rule-baseddecisionlistsinfederatedlearningforcreditcardanom-
adynamicthresholdlearningtechniquebyanalyzingthesliding alydetection.Thispresentworkrepresentsanotableadvancement
windowstatisticalproperties;(2)wecombinedifferentunsuper- asthedecisionlistactsasanadaptivethresholdingapplicationto
visedlearningtechniquestoimprovetheanomalyscore;(3)we improvepredictionaccuracyundertheprivacyconstraintorpri-
proposeawayofautomaticallytuningtheparameterstotackle vacypreservation. Settingthresholdscontinuouslyinachanging
changesindatacharacteristics[6][7].Thetimeseriesfeaturesex- environmentbasedonmachinelearning,reinforcementlearning,
tractiontechniquesconsideredinthisworkforthedetectionof andneuralnetworks,swarmintelligencewasemployedtodetect
financialtransactionsequencesabletodescribethetemporalpat- andtunetheparametersofstreamingdatacharacteristicsautomati-
ternscharacteristicofthesesequencesarethefrequencydomain, cally.Inthedomainofcreditcardanomalydetection,architectures
seasonaldecomposition,andstatisticaltrendanalysis.Allofthese thatcanprovideexplanationsandinterpretations,suchasTabNet,
perceptualaspectsofbehaviortuneafiner-grainedthresholdand areparticularlypromisinginthesensethattheynotonlycanoffer
discovertherequisiteexceptionsinvarioustransactionalscenarios, explanationsandinterpretationswhiledetectingbutalsohaveper-
suchascustomerbehaviour[8]. Theproposedframeworkcanbe formancenotworsethananystate-of-the-artmethodsreportedso
appliedtoqualitycontrolsystemsrequiringregulatorycompliance, far. Adaptivethresholdinginfinancialanomalydetectionsystems
operationalcostreductionthroughdecreasedfalsepositives,and hasledtosignificantbreakthroughsindetectionrateaswellas
enhancedriskmanagementcapabilities. operationalefficiency.SomeGRUnetwork-basedmethodsworking
inthepastfewyearsshowedsatisfactoryresultsinsuchafieldas
2 RELATEDWORKANDLITERATURE financialanomalydetection,especiallytogetherwithensembling,
whenacoupleofalgorithmsmetinthecentreinordertohave
REVIEW
anotheralgorithmtodecidewhosesideitis.Whatthesedevelop-
2.1 TimeSeriesAnomalyDetectioninthe mentsreinforceistheneedforagileresponsesinordertoaddress
FinancialDomain upcominganomaliesandevolvingconsumerbehaviour.
Theseminalliteratureonthedetectionoffinancialanomaliesis
2.3 FinancialDataQualityMonitoringSystems
groundedinstatisticalcontrolmodels,forwhichtheoriginisrooted
intheideaofcontrolcharts. Theconceptwastouseabnormality The current practice of financial data (1) governance (i.e., data
detection(e.g.,controlchartsandweightedmovingaverages)in qualitycontrol)istogenerateautomatedmonitoringcomponents
thesamemannerasithadbecomesuccessfulfortheapplication taskedwithamassivescaleoftransactionsathighaccuracyand
inqualitycontrolprocesses. Someattemptshavebeenmadein efficiencyrequirements.Havinglearnedabouttheseinsights,the
theintroducedsetofmethodstoatleastprovideapointofdepar- machine-learning-basedalgorithmsbehindcreditcardanomaly
turefordealingwiththisproblem. Still,theylimitthemselvesto detectionreturnthatknowledgetotheflowofnewtransactions
simplecaseswhencomplextimedependenceandmorecomplex inreal-time,whereallsortsoftransactionpatternscanbeseen.
nonstationarymotionofhigh-dimensionalfinancialdataaretypical Banking’sdataqualityasksaregrowingtoaskforend-to-endvali-
[9].Withtimeseriestransactionmonitoring,poweredbymachine dationframeworks—notonlyforsourcesystemstooperatingsys-
learning,thesemethodshavecompletelyflippedthefieldonits tems,butaroundtheoperatingsystems. Structuraldataquality
head.Forexample,thelearningarchitecturesofensemblemethods challengesstemmingfromtheconsolidationoflargeandgrowing
anddeeplearningcannowdiscernextremelysubtlepatternsinfi- monitoringdatasetsarealsomainlyduetosupervisory-ledstress
nancialstreamsofdata.Adaptiveanomalydetectionhassucceeded testingprograms(e.g.,CCAR,DFAST)thatnecessitatestrongdata
inRL-basedapproaches[10]. Moreover,incomparisontoconven- qualitypractices,whichmandatetheabilitytodetectandresolve
tionalrule-basedapproaches,GNNscanbetterbeusedtodetect exceptionsearlyenoughtopreventdownstreamadverseeffects,i.e.,
anomaliesinanevolvingnetworksetting.Theseresultsshowthat reportingorregulatorypenalties. Bankingcompetitionrequires
579

AdaptiveAnomalyDetectionThresholdforFinancialDataQualityMonitoringBasedonTimeSeriesFeatures AICSS2025,September19–21,2025,Beijing,China
Table1:AdaptiveThresholdAlgorithmParameters
Parameter Description DefaultValue Range
WindowSize(W) Numberofobservationsintheslidingwindow 1000 500-5000
SensitivityFactor(𝛼) Thresholdadjustmentsensitivity 0.15 0.05-0.30
DecayFactor(𝛽) Historicalweightdecayrate 0.95 0.80-0.99
ChangePointThreshold(𝛾) Statisticalsignificanceforpatternchanges 0.01 0.001-0.05
thesestandardstocorrespondtomoresophisticatedtechniquesof throughhistoricalcontextweighting.Additionally,robustparame-
anomalydetection. Thecombinationofdifferenttypesofcorpo- terestimationwithineachwindowemploysestimatorsthatwere
rates,locatedindifferentfinancialdatasystems,intoonefinancial designedtominimizetheimpactof”outliers”butremainsensitive
(IT)systemisacomplexchallengeinthesensethatitneedsmoni- tofundamentalpatternchanges.
toringcapabilitiesthatcrosssuchtechnologicalbordersanddata
sources.Underthecontextofdeeplearning,LSTM,asasequence 3.2 TimeSeriesFeatureExtractionforFinancial
analysis,showsbetterperformanceindynamicfinancialsystem Data
detection, andithasbeenenhancedbyearlystoppingtoavoid
Toinferthetimingofcreditcardtransactionpatternsrequiresafull
overfitting[11].
investigationofhowtimingcanexpressitselfintransactions.The
featureextractionprocessanalyzestemporalrelationshipswithin
3 METHODOLOGY
transactionsequencestoidentifycharacteristicpatterns.Thispro-
3.1 AdaptiveThresholdFrameworkDesign cesscapturesvariousstatisticalpropertiesandtemporaldependen-
Ouralgorithmusesslidingwindowstatisticalanalysistocalculate ciesthatdefinenormaltransactionbehavior.Withthedevelopment
bothglobalandlocalparametersforthresholdadjustment. The oftechnologyinthepastfewyears,peoplehaveappliedmanynew
frameworkemploysamulti-moduledesignwhereslidingwindow techniquesforfinancialtimeseriestrendanalysis,includingad-
analysiscontinuouslymonitorstransactionpatterns.Eachmodule vancedstatisticalmethods.
processesincomingtransactiondatatocalculatestatisticalparam- Howdoesvolatilitychangeoverthetimeprofileoftransactions?
eters for threshold adjustment. Through this adaptive learning Featuresofvariousdistributions—statisticalfeatureengineeringon
process,thresholdboundariesautomaticallyadjustbasedonde- transactionamountandfrequencyanalysisincludescalculations
tectedchangesindatacharacteristics. formovingaverages(rollingstats),methodsthatarebasedonthe
Timeseriessegmentationbecomesanessentialcomponentof percentiles, andmeasurestocapturetheessentialpropertiesof
adaptive thresholds and uses statistical change point detection transactionsequences.Thefeatureextractionalgorithmcarriesout
algorithmstodeterminemajorpatternshiftsthatrequireadjust- statisticalcomputationsthatchangewithtime—suchasmoving
mentindetectedthresholds. Thus,theprocessofsegmentation averagelevelsandstandarddeviations,skewness,andkurtosisover
isdonewithBayesianchangepointdetectiondetectorsthatare differenthorizons—providingacomprehensivecharacterizationof
usedtogetherwithinformation-theoreticalcriteriaandevidence transactionpatterns.
fordetectedchanges.
Formally,foratransactionsequenceX={x₁,x₂,…,xₙ},wecom-
Thesystemcontinuouslyevaluatesdetectionperformanceand pute:
a p u o t s o it m iv a e t s ic a a n l d ly m a i d s j s u e s d ts de th te r c e t s i h o o n l s d w p h a i r l a e m m e a t i e n r t s ai t n o in m g in sy im st i e z m eb e o ffi th cie fa n l c s y e . 𝑀𝑜𝑣𝑖𝑛𝑔𝐴𝑣𝑒𝑟𝑎𝑔𝑒 :𝑀𝐴(𝑡)=(1/𝑊)· (cid:213) 𝑖=1 𝑊 +1 𝑡·𝑥 𝑖 (2)
Thekeyparametersoftheadaptivethresholdalgorithmaresum- 𝑀𝑜𝑣𝑖𝑛𝑔𝑆𝑡𝑎𝑛𝑑𝑎𝑟𝑑𝐷𝑒𝑣𝑖𝑎𝑡𝑖𝑜𝑛:
marizedinTable1. 𝜎(𝑡)= √ [(1/𝑊)(cid:205)
𝑖=1
𝑊
+1
𝑡(𝑥
𝑖
−𝑀𝐴(𝑡))] (3)
Note that the number of its transactions is a measure of the
Window Size. Sensitivity Factor and Decay Factor are both di- 𝑆𝑘𝑒𝑤𝑛𝑒𝑠𝑠 :𝛾 1 (𝑡)=𝐸(cid:2) (𝑋 −𝜇)3(cid:3) /𝜎3 (4)
m sta e t n is s t i i o c n a l l e s s i s gn ra ifi ti c o a s n . c H e o le w v e e v l e (𝛼 r, -l t e h v e e C ls h ) a fo n r g p e a P tt o e i r n n t s Th hi r ft e s s : h i o ts ld de is fa t u h l e t 𝐾𝑢𝑟𝑡𝑜𝑠𝑖𝑠 :𝛾 2 (𝑡)=𝐸(cid:2) (𝑋 −𝜇)4(cid:3) /𝜎4 (5)
valuewassetbycross-validationtestsonsyntheticfinancialdata.
whereWisthewindowsize,E[·]denotesexpectation,𝜇isthemean,
Theadaptivethreshold𝜏(t)attimetiscomputedusinganexponen- and𝜎isthestandarddeviation.
tialdecayfunction: Figure1illustratesthearchitectureofourtimeseriesfeatureex-
tractionpipeline.Thecoredecompositionprocessinvolvesseasonal
𝜏(𝑡)=𝜇(𝑡)+𝛼×𝜎(𝑡)×𝛽(𝑡−𝑡 0 ) (1) analysis,exponentialsmoothingtechniques,andtrendanalysis.
where𝜇(t)isthemeanofobservationsinthecurrentwindow,𝜎(t) Thecoredecompositionprocessinvolvesseasonalanalysis,expo-
is the standard deviation, 𝛼 is the sensitivity factor controlling nentialsmoothingtechniques,andtrendanalysis. Todisassemble
thresholdstrictness,𝛽isthedecayfactor(0<𝛽<1)thatreduces thetimeseriesoftransactions,weusedifferentdecomposingtech-
theinfluenceofhistoricalinformation,andt0isthereferencetime niquestoseparateitstrends,seasonalitycomponents,andresidu-
point. Thisformulationenablesautomaticthresholdadjustment als.Theinputsforthresholdamountadjustmentmethods,which
basedoncurrentdatacharacteristicswhilemaintainingstability willadaptpredictablyaccordingtoknownseasonalchangesand
580

| AICSS2025,September19–21,2025,Beijing,China |     |     |     |     |     |     |     | MinjuZhong |
| ------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | ---------- |
Figure1:TimeSeriesFeatureExtractionPipelineArchitecture
underlyingtrendpatterns,arethesecomponentsthathavebeen whileatthesametimebeingsensitivetounconventionalbehaviour
| decomposedintotheirconstituentparts. |     |     |     |     | [13]. |     |     |     |
| ------------------------------------ | --- | --- | --- | --- | ----- | --- | --- | --- |
Thefeatureextractionpipelinewillintegratemultipleparallel Integratedensemblemethodsareadoptingmultipleunsuper-
processingstreamstoofferafull-thumbnailcharacterizationof visedalgorithms.Itgivesbetterrobustnessandaccuracythrough
transactionpatterns,bothforcomputationalefficiencyinreal-time theweightedcombinationofeachindividualalgorithm.Theensem-
applicationsandtoensurerecognizability.Eachprocessingstream bleapproachintegratesIsolationForest,DBSCANclustering,and
studiesdifferentaspectsoftransactionalbehaviour,includingits
LocalOutlierFactoralgorithms,withdynamicweightadjustment
timedependencies,statisticalproperties,andfrequencydomain dependingondifferentdataregimesandtransactionmodes.
patternscharacteristicoftransactionsequencesthatcontributeto TheensembleanomalyscoreS(x)fortransactionxcombines
| adaptivethresholdcomputation. |     |     |     |     | multiplealgorithms: |     |     |     |
| ----------------------------- | --- | --- | --- | --- | ------------------- | --- | --- | --- |
=Σ𝑀
|     |     |     |     |     |     | 𝑆(𝑥) | 𝑤 𝑗 ×𝑠 𝑗 (𝑥) | (6) |
| --- | --- | --- | --- | --- | --- | ---- | ------------ | --- |
𝑗=1
3.3 UnsupervisedLearningIntegration whereMisthenumberofalgorithms(M=3:IsolationForest,DB-
|     |     |     |     |     | SCAN,LocalOutlierFactor),𝑠 | 𝑗(𝑥)isthenormalizedanomalyscore |     |     |
| --- | --- | --- | --- | --- | -------------------------- | ------------------------------- | --- | --- |
Robustanomalydetectioncapabilitiesthatcomplementtheadap-
|     |     |     |     |     | fromalgorithmj,and𝑤 | isthedynamicweightsatisfying(cid:205)𝑤 |     | =   |
| --- | --- | --- | --- | --- | ------------------- | -------------------------------------- | --- | --- |
𝑗 𝑗
tivethresholdmechanismareprovidedbytheimplementationof
1.Weightsareupdatedbasedonalgorithmreliability:
anIsolationForestforoutlierscorecomputation.Theformeronly
m a k es b i n a r y j u d g m e n t s , w h i l e t h e la tt e r g e n e r a t e s c on t in u ou s 𝑤 (𝑡)=𝐴𝑈𝐶_𝑅𝑂𝐶 (𝑡)/Σ 𝑀 𝐴𝑈𝐶_𝑅𝑂𝐶 (𝑡)
|                |                         |                         |                          |                  | 𝑗   | 𝑗   | 𝑘 =1 | 𝑘 (7) |
| -------------- | ----------------------- | ----------------------- | ------------------------ | ---------------- | --- | --- | ---- | ----- |
| an o m al ie s | . I s ol a t io n F o r | e s t’ s p a r a m e te | rs a r e s u b j e c t e | d to d y n am ic |     |     |      |       |
optimisationbasedondatacharacteristics,withcontaminationrates where𝐴𝑈𝐶_𝑅𝑂𝐶 𝑗(𝑡)istheareaundertheROCcurveforalgorithm
andtreedepthparametersbeingoptimisedthroughcross-validation
jattimet,evaluatedonrecentvalidationdata.Thedetailedconfigu-
techniquesthatconsidertemporaldependenciesinfinancialdata rationparametersandoptimizationmethodsforeachunsupervised
| [12]. |     |     |     |     | learningalgorithmarepresentedinTable2. |     |     |     |
| ----- | --- | --- | --- | --- | -------------------------------------- | --- | --- | --- |
DBSCANclusteringfortransactionpatternidentificationlays The integration framework you designed serves not only to
thefoundationsforadaptivebatch-andcross-customercalibration. balanceweightsbetweenthedifferentunsupervisedalgorithmsbut
Adaptivetransactiontype-basedbehaviouralgroupingsaremade toprovideseamlesscoordinationamongthemwithinareal-time
inordertohelpestablishthresholds. Clusteringisabletoapply processingscenario. Thealgorithmoutputiscombinedthrough
distance metrics that consider transaction proximity as well as weightedvoting,consideringthereliabilityofindividualalgorithms
volumetoachieveeffectiveclassificationofsimilartransactions inadditiontoperformance-dependentonthenatureofthedata.
581

AdaptiveAnomalyDetectionThresholdforFinancialDataQualityMonitoringBasedonTimeSeriesFeatures AICSS2025,September19–21,2025,Beijing,China
Table2:UnsupervisedLearningAlgorithmConfiguration
Algorithm KeyParameters OptimizationMethod PerformanceMetric
IsolationForest n_estimators=200,contamination=auto GridSearchCV AUC-ROC
DBSCAN eps=adaptive,min_samples=10 SilhouetteAnalysis ClusterValidity
LocalOutlierFactor n_neighbors=20,contamination=0.1 BayesianOptimization Precision-Recall
DynamicallyadjustDBSCAN’sparametersforAdaptiveSelec- wealterthetimeindicesproducedbylongdelaysandpoornetwork
tion: bandwidthofactualfinancialdatastreamstogeneratedatasets
DBSCAN’s𝜖parameteradaptstolocaldatadensitythrough: thataremoreinlinewithourownresearchpersonnel’sphysical
𝜀(𝑖)=𝑃𝑒𝑟𝑐𝑒𝑛𝑡𝑖𝑙𝑒 90 (𝐷_𝑘(𝑊 𝑖)) (8) medium.
Thissyntheticdatasetcontainsmultipletypesofanomalies,in-
whereD_k(Wᵢ)={d_k(p)|p∈Wᵢ}representsthesetofk-nearest
cludingsuddenincreasegaps,atypicalgeographicalbackgrounds,
neighbordistancesforallpointspinwindowWᵢ,andd_k(p)is thetimeofyearwhenthishappensbeingnonseasonal,anddevi-
thedistancefrompointptoitskthnearestneighbor. The90th ationsfromtheeverydaytradingcategoriesscenarios. Statistical
percentileensuresrobustnessacrossvaryingtransactiondensities verificationsuggeststhatwehaveeffectivelycapturedinthisar-
whilemaintainingsensitivitytooutlierpatterns.Themin_samples tificialmaterialnotjustthefactsabouttransactionsbutalsotheir
parameterisfixedat10toensurereliableclusterformationwhile realisticinterrelationshipsanddependenciesfromtheoriginalau-
detectingirregulartransactionpatterns. thenticmaterial.
4 EXPERIMENTALDESIGNAND
IMPLEMENTATION 4.1.1 SyntheticDataLimitationsandReal-WorldConsiderations.
Whilesyntheticdatasetsenablecontrolledexperimentationand
4.1 DatasetDescriptionandPreprocessing
reproducibility,severalimportantdistinctionsfromrealfinancial
Asaresult,weroutinelycreatesimulatedMonteCarlotransactions. datawarrantdiscussion:
Thesetransactions,usingtheattributesofeverydaysalesitems,pay- DataDistributionCharacteristics:Realfinancialtransactiondata
mentforvariouscommodities,positioninaworkingdayorseason exhibitscomplex,evolvingpatternsinfluencedbymacroeconomic
oftheyear(occasionssuchasbirthdaysandChristmas,contracep- factors,regulatorychanges,andemergentfraudtacticsthataredif-
tives,etc.),andvariousformsoftransactionalanomalies,including ficulttofullycaptureinsyntheticgenerationmodels.Oursynthetic
unusualtransactionamountsandtimingpatternsthatrepresent dataapproximatesstatisticalpropertiesofrealtransactionsthrough
dataqualityissuesinstandardcreditcards.Afterstatisticalmodels parametricmodeling,butmaynotfullyrepresentthelong-taildis-
ofrealtransactionsareturnedintorecordsinthemannerabove, tributionsandrareeventcombinationspresentinactualfinancial
theyhavetobetransferredintoaparticularformofpublicisedmask systems.
thatcannotbecommonlyrecognised. Thesyntheticdatagenera- TemporalDependencies:Real-worldfinancialdatacontainsin-
tionprocessincorporatesvariousanomalypatternsthatchallenge tricatetemporalcorrelationsspanningmultipletimescales—from
detectionsystems,includingthosedesignedforinterpretablearchi- intradaytradingpatternstomulti-yeareconomiccycles. While
tecturessuchasTabNet[14],ensuringcomprehensiveevaluationof oursyntheticgenerationincorporatesdailyandseasonalpatterns
theproposedadaptivethresholdframework.Thecomprehensive basedonstatisticalmodels,itmaynotcaptureallnuancedtemporal
characteristicsandstatisticsofoursyntheticdatasetaredetailedin dependenciespresentinoperationalfinancialsystems,particularly
Table3. those arising from external economic shocks or unprecedented
Beforewegoon,rememberthathandlingmissingdatapointsina marketevents.
datapreprocessingtaskofsuchmagnitudeisjustonestep.Missing AnomalyRepresentation:Thesyntheticanomaliesinourdataset
valuesarehandledbythecodewithmethodssuchastemporal aregeneratedbasedonknownpatterns(unusualamounts,timing
interpolation,whichpreservestatisticalpropertiesembeddedin deviations,geographicalinconsistencies). Real-worldanomalies
the sequences of transactions. Noise reduction algorithms use mayexhibitnovelcharacteristicsnotrepresentedinhistoricalpat-
adaptivefilteringtodistinguishbetweenmeasurementnoiseand terns,presentingadditionalchallengesfordetectionsystems. This
thelegitimatetransactionvariance, soastoretaintheessential limitationispartiallymitigatedbyouradaptivethresholdframe-
patterninformationbasedonsounddataqualityconsiderations. work’s unsupervised learning approach, which can identify de-
Featurestandardizationmethodsuserobustscalingtechniquesthat viationsfromlearnednormalpatternswithoutrequiringlabeled
arelesssusceptibletooutliersbutstillallowrelativetransaction anomalyexamples.
characteristicrelationshipstobekept.Precisetimedregistration PrivacyandDataAccessConstraints: Theuseofsyntheticdata
processingneedstobedescribedsothatthetimeindexofeachdata wasnecessitatedbyprivacyregulationsandproprietaryconstraints
sourceisconsistentwithreal-worldfinancialdatastreams.Also,the preventingaccess to real financial transaction data. While this
processing-inducedoperationdelaysandsystemlatenciesfoundin limitsdirectvalidationagainstoperationalsystems,itenablesre-
suchstreamsmustnotbelost.Naturally,differentversionsofdata producibleresearchandalgorithmcomparisonwithoutexposing
oftenhavetimeindexingthatdeviatesfromeachother.Therefore, sensitivecustomerinformationorinstitutionaldata.
582

| AICSS2025,September19–21,2025,Beijing,China |     |     |     | MinjuZhong |     |
| ------------------------------------------- | --- | --- | --- | ---------- | --- |
Table3:DatasetCharacteristicsandStatistics
|     | Characteristic     | TrainingSet | ValidationSet | TestSet   |     |
| --- | ------------------ | ----------- | ------------- | --------- | --- |
|     | TotalTransactions  | 2,847,392   | 356,741       | 445,928   |     |
|     | AnomalyRate(%)     | 2.14±0.08   | 2.31±0.12     | 1.97±0.09 |     |
|     | TemporalSpan(days) | 365         | 45            | 60        |     |
|     | CustomerAccounts   | 48,750      | 12,188        | 15,235    |     |
|     | TransactionTypes   | 16          | 14            | 15        |     |
|     | AverageDailyVolume | 7,801±342   | 7,927±289     | 7,432±401 |     |
|     | PeakDailyVolume    | 12,847      | 11,203        | 10,891    |     |
|     | MinimumDailyVolume | 4,231       | 4,892         | 4,567     |     |
ValidationStrategy:Toaddresstheselimitations,ourexperimen-
taldesignincorporatesstatisticalvalidationensuringthesynthetic
datasetpreserveskeydistributionalproperties,temporalcorrela-
tions,andanomalycharacteristicsrepresentativeofrealfinancial
systems.Futureworkshouldincludevalidationonanonymizedreal
transactiondatawhereregulatoryframeworkspermit,toconfirm
theframework’seffectivenessinoperationalenvironmentswith
fullcomplexityofreal-worldfinancialdatastreams.
4.2 PerformanceEvaluationMetrics
Detectionprecision,recall,andF1-scoreofanomaliesanalysisuses
temporalcross-validationtechniquestolookattime-dependent
patternsinfinancialdata,soevaluationcoefficientsactuallyreflect
actualperformancecharacteristics. Theevaluationframeworkin-
troducesslidingwindowvalidationapproachesthatrespecttempo-
ralorderingsbutstillgivereliableperformanceevaluationsacross
differentperiodsandtypesofdata[15].Thisplatformwascreated
Figure2:MultidimensionalPerformanceEvaluationFrame-
withtheintentionofkeepingfastdetectionratesfromharming work
systemperformance.Introducingatradeoffbetweendetectionsen-
sitivityandoperatingefficiencyisitsdefiningcharacteristic—andit
requiresevaluationframeworkswhichwillnotfailtotakeintocon- 4.2.1 MetricDefinitions. Weemploystandardbinaryclassification
siderationcosts(ofanykind).Theoptimisationprocedureachieves metricstoevaluateanomalydetectionperformance:
theobjectiveofminimisingfalsepositiverateswhilenotmakingde- Precisionmeasurestheproportionofcorrectlyidentifiedanom-
aliesamongallflaggedtransactions:
tectionlevelsunacceptablebysimultaneouslyusingmulti-objective
| optimisationtechniques. |     |     | 𝑃𝑟𝑒𝑐𝑖𝑠𝑖𝑜𝑛=𝑇𝑃/(𝑇𝑃+𝐹𝑃) |     | (9) |
| ----------------------- | --- | --- | -------------------- | --- | --- |
End-to-endprocessingneedsinvolvecalculationsofperformance
Recall(orsensitivity)measurestheproportionofactualanom-
measuressuchasefficiencyanalysis,throughputmeasurements,
latency,andresourceutilizationevaluationindexes,typicallyin- aliessuccessfullydetected:
𝑅𝑒𝑐𝑎𝑙𝑙 =𝑇𝑃/(𝑇𝑃+𝐹𝑁)
volvingtransferringdatafromdifferentsystemplatformsandload (10)
formats.Performancemeasurementsoccurundertestconditions
F1-Scoreprovidestheharmonicmeanofprecisionandrecall,
laiddownbystandardbenchmarks,whichcanbefoundatfinancial
balancingbothmetrics:
institutions,tomaketheresultsofperformancemeasurementsbul-
letinstrustworthy.Ourmultidimensionalperformanceevaluation 𝐹1−𝑆𝑐𝑜𝑟𝑒 =2×(𝑃𝑟𝑒𝑐𝑖𝑠𝑖𝑜𝑛×𝑅𝑒𝑐𝑎𝑙𝑙)/(𝑃𝑟𝑒𝑐𝑖𝑠𝑖𝑜𝑛+𝑅𝑒𝑐𝑎𝑙𝑙) (11)
frameworkisillustratedinFigure2,whichencompassesdetection FalsePositiveRate(FPR)quantifiestheproportionofnormal
accuracy,computationalefficiency,andsystemrobustnessmetrics. transactionsincorrectlyflaggedasanomalies:
Inthisframework,statisticalsignificancetestinghasbeenin-
|     |     |     | 𝐹𝑃𝑅=𝐹𝑃/(𝐹𝑃+𝑇𝑁) |     | (12) |
| --- | --- | --- | -------------- | --- | ---- |
corporateddirectlysothatthedifferencesinperformancebetween
algorithmsare,infact,realimprovementsandnotjustchancevari- where TP (True Positives) represents correctly detected anom-
ation. Byusingthetechniqueofbootstrapresamplingcombined alies,FP(FalsePositives)representsnormaltransactionsincorrectly
withtechniquesforstatisticalconfidenceintervalconstruction,it flagged,FN(FalseNegatives)representsmissedanomalies,andTN
ispossibletoputrobustcomparisonsofalgorithmperformance (TrueNegatives)representscorrectlyidentifiednormaltransac-
directlybeforereaders. tions.
583

AdaptiveAnomalyDetectionThresholdforFinancialDataQualityMonitoringBasedonTimeSeriesFeatures AICSS2025,September19–21,2025,Beijing,China
Table4:ComparativeAnalysisResultsSummary
Method Precision Recall F1-Score FPR Processing Significance
Time(ms/1000 (p-value)
trans)
FixedThreshold 0.724±0.031 0.831±0.024 0.774±0.022 0.142±0.008 12.3±1.4 -
Statistical 0.789±0.028 0.856±0.021 0.821±0.019 0.098±0.006 18.7±2.1 p<0.01*
ML-based 0.812±0.025 0.873±0.018 0.841±0.017 0.089±0.005 24.1±2.8 p<0.001
Adaptive
Proposed 0.847±0.023 0.891±0.016 0.868±0.015 0.076±0.004 21.5±2.3 p<0.001
Framework
Figure3:AlgorithmPerformanceComparisonAcrossMultipleDimensions
ProcessingTimemeasurescomputationalefficiencyinmillisec- Sensitivityanalysisondifferentfinancialdatacharacteristicsex-
ondsper1000transactions,criticalforreal-timedeployment. amineslinkagesbetweenthealgorithm’sperformanceandchang-
ingmarketconditionsinthedata.Studyingfactorialdesignmethod-
ologieshasbeenusedforthiskindofinspectionwork. Itallows
ustocompareandcontrastperformancesensitivityundermultiple
dataconditionsatthesametime.Table4presentsacomprehensive
summaryofthecomparativeanalysisresultsacrossallevaluated
4.3 ComparativeAnalysisSetup
methods.
Baselinecomparisonswithfixedthresholdmethodsincludeoverall Resultsrepresentmean±standarddeviationover10independent
assessmentsthatcovermostanomalydetectionsystemscommonly runs. Statistical significance was determined using McNemar’s
prescribedinfinance,causingstatisticalcharts,percentiles,and testformodelcomparisonanda5x2-foldcross-validationpaired
rule-baseddetectionsystemstobemadetomakeacomprehensive t-testwithBonferronicorrectionformultiplecomparisons. Non-
evaluation. Thecomparisonframeworkmakessuretoequalize parametricbootstrapresampling(n=1000)wasappliedtoestimate
evaluationbyusingidenticaldatasetsandinspectioncriteriafor confidenceintervalsforperformancemetrics. *p<0.01,p<0.001.
allmethods. FPR = False Positive Rate. Processing time measured per 1000
Performance achieved by benchmarking against established transactionsonIntelXeonE5-2680v4@2.40GHzwith32GBRAM.
adaptivethresholdalgorithmsincorporatesthelatestresearchfind- Figure3providesavisualcomparisonofalgorithmperformance
ings in dynamic threshold adjustment. Benchmark procedures acrossmultipleevaluationdimensions,demonstratingtheproposed
applystandardisednormsofevaluation,whichconsidertherequire- framework’ssuperiority in precision, recall, F1-score, and false
mentsofvariousalgorithmsandtheiroptimisationprocedureswith positiveratereductioncomparedtobaselinemethods.
rigourtoensureacomprehensiveandfairperformancecomparison.
584

AICSS2025,September19–21,2025,Beijing,China MinjuZhong
Theframeworkforcomparativeanalysisemploysstatisticaltest- 5.2.1 Real-timeTransactionProcessing. Data-qualitymonitoringin
ingtechniquestodeterminewhethertheperformanceofvarious large-scalepayment-processingenvironmentspresentsparticular
pairsofmethodsisverydifferentunderpairedstatisticaltestsand problems,thankstotheglaringamountandfleetnessofincoming
effectsizemeasurements,whichcanberegardedasthereal-world streamsthataffecttransactionintegrity.Theframework’ssliding
significanceofimprovementsmadeinperformance. windowapproachmakescontinuousobservationoftransaction
patternspossiblewithoutneedingbatchprocessingdelay,which
coulddisturbsystemperformance. Thatensemblemethodbrings
5 RESULTSANALYSISANDDISCUSSION IsolationForest,DBSCANclustering,andLocalOutlierFactoralgo-
5.1 ExperimentalResultsandPerformance rithmstogethertomakeacomprehensiveanomalyscoringsystem,
capableofadjustingitselfastransactioncharacteristicschangein
Analysis
realtime.
Accordingtoobjectivemeasures,incontrasttotraditional,fixed Theframework’scomputationalefficiencycanbecrucialinthese
thresholdmethods,proposedadaptivethresholdingframeworks environments.Timemeasurementsindicatethattheadaptiveap-
hadsuperiorperformance.Inthisregard: proachcanstillmeetverytightlatencycriteriaunderhighload,
·Falsepositiveratereductionsbyfully46.5%andimprovements makingitsuitablefordeploymentinsystemswithstringentre-
inF1-scoreaccuracyincreasedto12.1%wererecorded;thisdemon- sponsetimerequirements. Themechanismfordynamicallyadjust-
stratesimproveddiscriminativecapabilityindistinguishinggen- ingparametersensuresstabledetectionprecisionnotwithstanding
uineanomaliesfromnormaltransactionvariations. howoperatingconditionsfluctuate.
Comparedtotraditionalmethods,theadaptiveframeworkshows
noticeableadvancesinbothcomputationalefficiencyandscalability.
Inpractice,ithasbetterdecodingspeedthanitsoldfixed-threshold
5.2.2 Cross-institutional Data Quality Assessment. Data quality
counterparts;wehavetotakenotethatmemoryusageanalysisindi-
monitoringhasbecomeincreasinglyimportantforfinancialinsti-
catesresourcerequirementsare23percentlowerthanconventional
tutions,andthisresponsibilityiscompoundedbythefactthatthe
thresholdmethods. Itmakesadaptablethresholdssuitableeven
informationmightstemacrossavarietyofsourcesandjurisdic-
whendeployedwithinresource-pooroperationalenvironments.
tionalboundaries. Theadaptivethresholdframework’sunsuper-
Flatgrowthcharacteristics: Wehavebeenabletoshowthatat
visedlearningapproachallowsittobeusedinfederatedenviron-
differentdatavolumes,thetimetoprocessinformationisextended
ments,wherelabeledtrainingdatacanbescarceorabsent. The
inadirectionproportionaltobusinesssize,butwithoutsacrificing
framework’sabilitytolearnnormaltransactionpatternsfromunla-
accuracyindetection.Theframeworkwasstableacrossdifferent
beleddatastreamsmakesitparticularlysuitableforestablishments
customersegmentsandtransactiontypes,somethingthatiscrucial
implementingnewmonitoringsystemsorsettingtheirsightson
forpracticaluseindiversefinancialenvironmentsrequiringfault-
transactiontypesnotpreviouslycovered.
toleranceasamandatoryminimumcriterion.
Theframework’sparametertuningcapabilitiesenableittobe
adjustedaccordingtodifferentinstitutionalsettings; itcanstill
5.2 CaseStudyApplications carryoutthebasicfunctionofdetection. Institutionscanchange
sensitivityfactorsandwindowsizestosuittheirspecificlevelofrisk
Actually,thisViewpointpaperoffersanadvancedmethodtoimple-
withoutneedingtoretraintheunderlyingmodel.Suchflexibility
mentadaptivethresholds,anditisthisfunctionalityofthesystem
meansthethingcanbecarriedoutinanorganizationpossessing
whichwewillnowpresentinaseriesofthreeexamplesdesigned
differentstructuresandexistingregulations.
toshowhowtheframeworkoperatesatgroundlevel.
RegulatoryComplianceMonitoring
Financialinstitutionsoperatingunderregulatoryframeworks
suchasCCARandDFASTrequirecontinuousmonitoringoftrans- 5.2.3 ImplementationConsiderations. Inpractice,itisnecessary
actiondataqualitytoassureaccuratestresstestingandreporting. tocarefullyconsiderhowtheadaptivethresholdframeworkfits
Traditionalstaticthresholdsystemsoftengenerateexcessivefalse intoaninstitution’songoingoperations.Theframework’smodular
positivesduringperiodsofmarketvolatilityorseasonaltransaction designenablesittobeintegratedwithexistingdataqualitymonitor-
patternchanges,forcingmanualreviewthatconsumessignificant inginfrastructurewhilealsoallowinginstitutionsthathavealready
operationalresources. Theadaptivethresholdframeworksolves madeinvestmentsinthisareatopavethewayforfurtherdevelop-
thisproblembyautomaticallyadjustingdetectionparametersbased ments.Loggingofperformancemonitoringresultsandchangesin
onemergingmarketconditionsandcustomerbehaviorpatterns. thresholdsettingsgivesinsightintothedecision-makingprocesses
Inregulatoryreportingcontexts,theframework’sseasonalde- ofthesystem,whichsupportsdemandsforauditsortheneedto
compositioncapabilitiesproveparticularlyvaluable.Transaction superviseoperations.
volumesandpatternsshowpredictablevariationsduringperiods Theframework’scapacitytoconservehistoricalpatterninforma-
suchasyear-endfinancialactivityorholidayshoppingseasons, tionwhilemovingtonewconditionsmakessurethatitsdetection
whichstaticsystemswronglyflagasanomalies. Theadaptiveway capabilitiesdevelopcorrectlywithchangesinthebusinesssituation.
recognizessuchlegitimatepatternshiftsandoffsettingthresholds, Thisisacrucialcompromisebetweenflexibilityandstability,allow-
whilemaintainingsensitivitytogenuinedataqualityproblems, ingcontinuoushigh-qualitydatamonitoringnomatterwhatthe
reducesfalsealarms. prevailingmarketconditionsorstageofgrowthforyourinstitute.
585

AdaptiveAnomalyDetectionThresholdforFinancialDataQualityMonitoringBasedonTimeSeriesFeatures AICSS2025,September19–21,2025,Beijing,China
5.3 LimitationsandFutureResearchDirections historicalpatterns. Futureresearchdirectionsshouldfocusonin-
Theproblemwiththeproposedadaptivethresholdalgorithmis corporatingexternaleconomicindicatorsandexploringfederated
thatifthemarketisabnormalandentirelyunexpectedbehaviour learningapproachestoenableprivacy-preservingcollaboration
shouldoccurinthemarkets,thenthisapproachdoesnothandleit acrossfinancialinstitutions. Additionally,investigatingtheframe-
well.Additionally,theevaluationonsyntheticdatasets,whileen- work’sadaptabilitytoemergingfinancialtechnologiesandtransac-
ablingcontrolledexperimentation,introduceslimitationsregarding tiontypeswillbecrucialformaintaininglong-termeffectiveness
generalizationtoreal-worldfinancialsystems.Thesyntheticdata intherapidlyevolvingfinanciallandscape.
generationprocess,thoughstatisticallycalibratedtomirrorreal
transactioncharacteristics,cannotfullycapturethecomplexityof Acknowledgments
actualfinancialecosystems,includingrarecombinationanomalies,
IamgratefulforthehelpfulstudythatIqbaldevelopedlastyear
emergent fraud patterns, and the full spectrum of temporal de-
withAmin,R.,Alsubaei,F.S.,andAlzahrani.Theirresearchfocuses
pendenciespresentinoperationaldata. Validationonanonymized
onanabnormalintelligentcentreusingcloudmonitoringdataof
real-worlddatasetsfromfinancialinstitutionswouldprovidecrucial
multivariatetimeseries, which ismadeeasier thaneverbefore
evidenceoftheframework’soperationaleffectivenessandiden-
byusingdeepensemblemethodmodels. ”Anomalydetectionin
tifyadditionaledgecasesrequiringalgorithmicrefinement. The
multivariatetimeseriesdatausingdeepensemblemodels”Paper
frameworkmayfacechallengeswhenencounteringunprecedented
reportedinPlosOne(2024)[1]. Asaresult, myunderstanding
marketconditionsorregulatorychangesthatfundamentallyalter
of the deep ensemble method in time series anomaly detection
transactionpatternsbeyondhistoricalnorms.Futureresearchdirec-
hasbeendeepened,andthishaschangedhowIlookatadvanced
tionsincludeincorporatingexternaldatasourcessuchassocialme-
techniquesformultivariatefinancialdataanalysis. Includedare
diasentimentindicatorsandmacroeconomicstatisticstoenhance
alsonotes,whichIacknowledgeAsmar,M.,andAqel,B.Y.,fortheir
featureextractioncapabilities. Theseadditionaldatasourcescould
studyoncreditcardanomalydetectionanalysisfromaprocess
improve detection accuracy under changing market conditions.
and techniques perspective. The paper ”Analysis of credit card
Externaldatasourcesrequirepreprocessingthroughadvancedfea-
anomalydetection:processandtechniquesperspective”appeared
tureengineeringandselectiontechniques.Futureimplementations
inArtificialIntelligence(AI)andFinance(2023)[2].Theiranalysis
couldincorporatefederatedlearningapproachestoenableprivacy-
oftheprocedureandmeansofinfectionfordetectionprocessing,
preservingcollaborationacrossinstitutions. Thisapproachallows
however, hasenhancedmyunderstandingoffinancialanomaly
formultiplefinancialinstitutionstocollaborateonanomalyde-
detectionsystemsandresearchintoadaptivemethodsoffinancial
tectionwhilemaintainingregulatorycomplianceanddataprivacy
dataqualitymonitoringwithabnormaldetectionframeworks.
requirements. Theuseoffederativeapproachescanimprovedetec-
tionaccuracy,butitshouldalsobestrictlyinlinewithrequirements
fordataconfidentiality. References
[1] Iqbal,A.,Amin,R.,Alsubaei,F.S.,&Alzahrani,A.(2024).Anomalydetection
inmultivariatetimeseriesdatausingdeepensemblemodels.Plosone,19(6),
e0303890.
6 CONCLUSION [2] Asmar,M.,&Aqel,B.Y.(2023).Analysisofcreditcardanomalydetection:process
andtechniquesperspective.InArtificialIntelligence(AI)andFinance(pp.899-
Thisresearchpresentsacomprehensiveadaptivethresholdframe- 911).Cham:SpringerNatureSwitzerland.
workforfinancialdataqualitymonitoringthatsuccessfullyad- [3] Liu,H.(2025).Multi-variabletime-seriesanomalydetectionforintelligentopera-
tionandmaintenance.In2025,the5thInternationalSymposiumonComputer
dressesthelimitationsoftraditionalstaticthresholdapproaches. TechnologyandInformationScience(ISCTIS)(pp.1030-1034,2025,May).IEEE.
Theproposedmethodologyintegratesslidingwindowstatistical [4] Jain,J.S.,Sapra,A.,Gupta,A.,Dagar,L.,&Niranjan,V.(2025).Performance
AnalysisofMachineLearningModelsandDeepLearningModelsforCreditCard
analysiswithensembleunsupervisedlearningtechniques,achiev-
AnomalyDetection.In2025,the3rdInternationalConferenceonCommunication,
ingsignificantimprovementsinanomalydetectionperformance. Security,andArtificialIntelligence(ICCSAI)(Vol.3,pp.1533-1538,2025,April).
Experimentalresultsdemonstratethatourframeworkoutperforms IEEE.
[5] Chen,Z.,Wang,S.,Yan,D.,&Li,Y.(2023).Researchandimplementationof
conventionalmethodswithaprecisionof0.847,recallof0.891,and
abankcreditcardanomalydetectionsystembasedonreinforcementlearning
F1-scoreof0.868,whileachievingasubstantial46.5%reduction andLSTM.In2023,the3rdInternationalConferenceonMobileNetworksand
infalsepositiverates. Theframework’sabilitytoautomatically WirelessCommunications(ICMNWC)(pp.1-8,2023,December).IEEE.
[6] Ida,S.J.,&Balasubadra,K.(2024).Enhancingcreditcardanomalydetection
adjustdetectionparametersbasedonevolvingtransactionpatterns throughLSTM-basedsequentialanalysiswithearlystopping.In20242ndIn-
representsasignificantadvancementinfinancialdataqualitymoni- ternationalConferenceonNetworkingandCommunications(ICNWC)(pp.1-6,
2024,April).IEEE.
toring,particularlyforinstitutionsoperatingunderstrictregulatory
[7] Chen,Y.,Zhao,C.,Xu,Y.,&Nie,C.(2025).Year-over-yeardevelopmentsin
requirementssuchasCCARandDFASTcompliance. financialanomalydetectionviadeeplearning:Asystematicliteraturereview.
Thepracticalimplicationsofthisworkextendbeyondimproved arXivpreprintarXiv:2502.00201.
[8] Sathe,R.,&Shinde,S.(2024,).ADeepLearningFrameworkforEffectiveAnomaly
detectionaccuracytoencompassoperationalefficiencyandregu-
DetectioninTimeSeriesData.In20244thAsianConferenceonInnovationin
latorycompliancebenefits.Theframework’sreal-timeprocessing Technology(ASIANCON)(pp.1-7,2024,August).IEEE.
capabilitiesandmodulardesignenableseamlessintegrationinto [9] Cui,Y.,Han,X.,Chen,J.,Zhang,X.,Yang,J.,&Zhang,X.(2025).FraudGNN-RL:a
graphneuralnetworkwithreinforcementlearningforadaptivefinancialanomaly
existing financial monitoring infrastructure while reducing the detection.IEEEOpenJournaloftheComputerSociety.
operational burden associated with manual threshold recalibra- [10] Suganthi,V.,&Jebathangam,J.(2024).ANovelApproachforCreditCardanomaly
detectionusingGatedRecurrentUnit(GRU)Networks.In20248thInternational
tion. However,theapproachfaceslimitationswhenencountering
ConferenceonI-SMAC(IoTinSocial,Mobile,AnalyticsandCloud)(I-SMAC)
unprecedentedmarketconditionsthatdeviatesignificantlyfrom (pp.1716-1721,2024,October).IEEE.
586

AICSS2025,September19–21,2025,Beijing,China MinjuZhong
[11] Tang,Y.,&Liu,Z.(2024).ACreditCardanomalydetectionAlgorithmBasedon IEEE/CAAJournalofAutomaticaSinica.
SDTandFederatedLearning.IEEEAccess,12,182547-182560. [14] Meng,C.C.,Lim,K.M.,Lee,C.P.,&Lim,J.Y.(2023,August).CreditCardanomaly
[12] Chidambaranathan,P.,&MuthuPriya,V.(2024).RiskPredictioninFinancial detectionusingTabNet.In202311thInternationalConferenceonInformation
TransactionsUsingIoTBigDataAnalytics.In20245thInternationalConference andCommunicationTechnology(ICoICT)(pp.394-399).IEEE.
onElectronicsandSustainableCommunicationSystems(ICESC)(pp.328-332, [15] Alamri,M.A.,&Ykhlef,M.A.(2023).AMachineLearning-BasedFramework
2024,August).IEEE. forDetectingCreditCardAnomaliesandFraud.In202327thInternational
[13] Xie,Y.,Zhou,M.,Liu,G.,Wei,L.,Zhu,H.,&DeMeo,P.(2025).Atransactional- ConferenceonInformationTechnology(IT)(pp.1-7,2023,February).IEEE.
behavior-basedhierarchicalgatednetworkforcreditcardanomalydetection.
587