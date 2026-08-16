---
conversion_metadata:
  converted_at: "2026-07-21T13:58:16Z"
  converter_tool: "markitdown"
  converter_version: "0.1.6"
  source_pdf: "Li & Gautam.pdf"
  source_pdf_sha256: "83a6beaee34cac57acd8b0474ddd752943a540a202932839f9f9f09751a7b918"
  page_count: 10
  markdown_char_count: 85461
---

<!-- PAGE-AWARE EXTRACTION (via pdfminer.six) -->

<!-- PAGE 1 -->

Segmented Confidence Sequences and Multi-Scale Adaptive
Confidence Segments for Anomaly Detection in Nonstationary
Time Series

Muyan Anna Li
NVIDIA
Santa Clara, USA
annali@nvidia.com

Aditi Gautam
NVIDIA
Santa Clara, USA
adgautam@nvidia.com

Abstract
As time series data become increasingly prevalent in domains such
as manufacturing, IT, and infrastructure monitoring, anomaly de-
tection must adapt to nonstationary environments where statistical
properties shift over time. Traditional static thresholds are easily
rendered obsolete by regime shifts, concept drift, or multi-scale
changes. To address these challenges, we introduce and empirically
evaluate two novel adaptive thresholding frameworks: Segmented
Confidence Sequences (SCS) and Multi-Scale Adaptive Confidence
Segments (MACS). Both leverage statistical online learning and
segmentation principles for local, contextually sensitive adaptation,
maintaining guarantees on false alarm rates even under evolving
distributions. Our experiments across six public benchmark datasets
show significant F1-score improvement compared to traditional
percentile and rolling quantile approaches. This work demonstrates
that robust, statistically principled adaptive thresholds enable re-
liable, interpretable, and timely detection of diverse real-world
anomalies.

CCS Concepts
• Computing methodologies → Machine learning; Anomaly
detection; • Information systems → Data analytics.

Keywords
Anomaly Detection, Adaptive Thresholding, Confidence Sequences,
Multi-Scale Analysis, Nonstationary Time Series

ACM Reference Format:
Muyan Anna Li and Aditi Gautam. 2025. Segmented Confidence Sequences
and Multi-Scale Adaptive Confidence Segments for Anomaly Detection in
Nonstationary Time Series. In 2025 5th International Conference on Artificial
Intelligence and Application Technologies (AIAT 2025), December 04–06, 2025,
Kyoto, Japan. ACM, New York, NY, USA, 10 pages. https://doi.org/10.1145/
3787120.3787130

1 Introduction
Time series data are ubiquitous across modern applications, from in-
dustrial process monitoring and predictive maintenance to financial
markets and sensor-driven systems. Detecting anomalies—unusual
patterns or behaviors that deviate from expected trends—is crucial

This work is licensed under a Creative Commons Attribution 4.0 International License.
AIAT 2025, Kyoto, Japan
© 2025 Copyright held by the owner/author(s).
ACM ISBN 979-8-4007-2290-5/25/12
https://doi.org/10.1145/3787120.3787130

for preventing faults, reducing risk, and ensuring operational relia-
bility [7]. Unlike static datasets, time series often exhibit evolving
behavior, including trends, seasonality, and abrupt regime shifts,
making anomaly detection a particularly challenging problem.

In recent years, researchers have developed advanced techniques
that go beyond simple static thresholds. Approaches such as ro-
bust moving windows, online quantile estimation, and confidence
sequence theory have emerged to provide more adaptive and sta-
tistically principled anomaly detection [9, 13]. These methods aim
to balance computational efficiency with real-time adaptability,
enabling detection systems to respond to changing data dynamics.
However, existing adaptive thresholding methods often struggle
when data exhibit multiple temporal scales or sudden regime shifts.
Fixed-window or global percentile-based strategies may either fail
to capture local variations, leading to missed anomalies, or produce
excessive false positives when the baseline drifts [4]. This highlights
the need for a thresholding framework that can simultaneously
adapt to both abrupt and gradual changes in data distribution.

To address these challenges, we contribute two novel frameworks

for adaptive thresholding.

• Segmented Confidence Sequences (SCS) segments time series
by regime, maintaining distinct confidence-based bounds per
segment, and adapts to local rather than global statistics.
• Multi-Scale Adaptive Confidence Segments (MACS) is an
approach that adapts detection simultaneously at multiple
window lengths, enabling the detection of both rapid bursts
and slow regime changes.

• Comprehensive experimental evaluation supporting statisti-
cally significant improvements over traditional percentile or
fixed adaptive thresholds.

2 Related Work
2.1 Static and Traditional Thresholding
Early approaches relied on fixed global thresholds – often prescribed
as mean ± 𝑘𝜎 or a static quantile – assuming stationarity and i.i.d.
observations [7]. Although easy to implement, these methods fail
under concept drift or dynamic variance and are prone to false
positives in practical systems [5].

Percentile-based approaches, such as the 99th percentile thresh-
old, adjust for heavy tails but still falter under persistent distribu-
tional drift or nonstationarity, as shown in benchmark studies [8].
Methods based on Extreme Value Theory (EVT) and the Peak-Over-
Threshold (POT) model the empirical tail beyond a high threshold
but still assume the threshold regime is quasi-stationary [8].

---

<!-- PAGE 2 -->

AIAT 2025, December 04–06, 2025, Kyoto, Japan

Li and Gautam

2.2 Sliding Windows, Rolling Statistics, and

Moving Quantiles

Adaptive methods using sliding windows recalculate thresholds
over a recent window – updating the mean, standard deviation,
or quantile in an online manner [1]. The exponential weighted
moving average (EWMA) improves rapid adaptation to trends or
regime switches, but window size determines sensitivity and is
often hard to tune [5]. Non-parametric dynamic models further
reduce reliance on distributional assumptions and are superior in
recall [11].

2.3 Model-Based and Machine Learning

Approaches

Forecasting-model-based detection fits models such as ARIMA or
seasonal decomposition, then tests for outliers in the model resid-
uals [6]. More advanced approaches leverage autoencoders, deep
neural networks, or reinforcement learning agents to learn context-
sensitive anomaly scores or directly optimize detection performance
[3, 4, 14]. However, these methods either lack explicit statistical
error guarantees or require considerable labeled anomaly data.

2.4 Confidence Sequences for Online

Adaptation

Confidence sequences (CS) – time-uniform intervals guaranteeing
correct coverage at all times – are a foundation for rigorous thresh-
olding in nonstationary data, allowing error rate control under
arbitrary stopping [9]. Recent algorithms can maintain confidence
bounds for quantiles or means, enabling adaptive anomaly scor-
ing robust to drift, heavy tails, or outliers [13]. Applying CS-based
threshold selection to streaming anomaly detection is a promising
and newly emerging direction [9, 12].

2.5 Segmentation-Based Local Thresholding
Segmenting time series into locally stationary regimes – via APCA
or clustering – brings statistical homogeneity to threshold estima-
tion, allowing each regime to have a locally fitted, adaptive rule
[2, 10]. Recent approaches use clustering (e.g., k-means) on sum-
mary features to capture regime change, but statistical decision
boundaries within each segment remain underexplored.

3 Methods
We focus on two novel, unsupervised adaptive thresholding strate-
gies for streaming time series: Segmented Confidence Sequences
(SCS) and Multi-Scale Adaptive Confidence Segments (MACS). Both
are designed for practical anomaly detection pipelines (see Figure 1
and Figure 2).

3.1 Segmented Confidence Sequences (SCS)
SCS first performs time series segmentation using either Adap-
tive Piecewise Constant Approximation (APCA) - which iteratively
splits at points that minimize reconstruction error - or feature-
based K-means clustering using sliding-window statistics [2]. Each
segment is assumed to be locally stationary, allowing for regime-
specific anomaly detection. Within each segment, an independent

confidence sequence is maintained for anomaly score thresholds, us-
ing Hoeffding’s inequality for non-parametric bounds [9]. Segment-
specific anomaly flags are triggered if new scores exceed the upper
confidence bound or fall below the lower confidence bound.

Figure 1: Illustration of the SCS flow.

SCS begins by partitioning the time series into locally stationary
segments, using either Adaptive Piecewise Constant Approximation
(APCA) or feature-based K-means clustering [2]. APCA operates
by iteratively identifying optimal split points that minimize total
reconstruction error, defined as the sum of squared deviations from
the mean within each segment. Specifically, for a proposed split,
the reconstruction error is calculated as:

total_error = left_error + right_error

left_error =

right_error =

∑︁

∑︁

(𝑥𝑖 − ¯𝑥left)2
(𝑥 𝑗 − ¯𝑥right)2

(1)

(2)

(3)

This process continues recursively until segments fall below a min-
imum length constraint or no further improvement is observed
according to a specified threshold. For flat regions of the time se-
ries, identified by a coefficient of variation below 0.1, APCA defaults
to fixed-length segmentation, where segment size is set to:

max(200,

(cid:107)

)

(cid:106) 𝑛
15

(4)

For more variable data, a candidate split is accepted only if the
minimized reconstruction error satisfies:

min_error < no_split_error ×

improvement_threshold

(5)

The improvement threshold is set to 0.7 for high-variance series
and 0.5 for moderate-variance series.

Alternatively, SCS supports a K-means segmentation approach
that clusters sliding window representations of the time series based
on statistical features. For each window, features including the
mean, standard deviation, median, and skewness are extracted, and
the resulting feature vectors are normalized using StandardScaler.
For multi-dimensional time series data, the dimensionality is re-
duced by averaging across the feature dimensions such that:

data_1d = mean(𝑋, axis = 1)

if 𝑋 ∈ R𝑛×𝑑, 𝑑 > 1

(6)

---

<!-- PAGE 3 -->

Segmented Confidence Sequences and Multi-Scale Adaptive Confidence Segments
for Anomaly Detection in Nonstationary Time Series

AIAT 2025, December 04–06, 2025, Kyoto, Japan

In cases where the clustering process fails due to insufficient vari-
ability or degenerate distributions, the entire sequence is treated as
a single segment to preserve stability.

Within each resulting segment, regardless of the segmentation
method, SCS maintains an independent confidence sequence for
thresholding anomaly scores. These bounds are derived using Hoeffding-
style inequalities [9] and are parameterized by the local standard
deviation of the segment’s scores. The width of the confidence
bound is initially set as:

bound_width = 1.5 × std_score

(7)

It is then scaled by a factor that reflects the desired confidence
level. Specifically, if the confidence level exceeds 95%, the bound is
widened by a factor of 1.2; if it is below 90%, the bound is narrowed
to 0.8. The final confidence interval for each score is given by:

lower_bound = ¯𝑥 − bound_width
upper_bound = ¯𝑥 + bound_width

(8)

(9)

To ensure robustness and avoid false positives from local fluctua-
tions, SCS uses a composite detection criterion: a point is flagged
as anomalous only if it violates both the confidence bounds and
a global percentile threshold. Formally, an intermediate anomaly
indicator is computed as:

anomalies = (𝑥 < lower_bound) ∨

(𝑥 > upper_bound)

The final anomaly decision is made via:

final_anomalies = anomalies ∧

percentile_filter

(10)

(11)

To summarize, the algorithm flow is outlined below:

• Segmentation Phase: Apply APCA or K-means to identify

regime boundaries

• Bound Calculation: Compute confidence bounds for each

segment independently

• Point Assignment: Dynamically assign incoming points to

their corresponding segment

• Anomaly Detection: Compare each point to segment-specific

thresholds

• Filtering: Apply percentile-based filtering for conservative-

ness

(The pseudocode of the algorithm flow is in Appendix A.)

Incoming data points are dynamically assigned to their corre-
sponding segment, and anomalies are detected by comparing each
point to the segment-specific, adaptively updated threshold. This
approach ensures that anomaly detection is locally calibrated to
the current regime, providing robust detection even as the data
distribution shifts over time. The method is unsupervised, requires
no labeled anomalies, and is suitable for both batch and streaming
data.

3.2 Multi-Scale Adaptive Confidence Segments

(MACS)

MACS is designed to capture anomalies occurring at different tem-
poral resolutions by maintaining multiple rolling windows of vary-
ing lengths in parallel.

Figure 2: Illustration of the MACS flow.

Specifically, it tracks short (e.g., 50 steps), medium (e.g., 100 steps),
and long (e.g., 500 steps) time scales, each of which independently
maintains a confidence sequence [5]. This structure enables MACS
to detect a broad spectrum of anomalies, from short-term bursts to
slow-moving regime shifts. To further enhance adaptability, MACS
incorporates an attention mechanism that dynamically weighs the
importance of each temporal scale based on local variance patterns
in the data.

Each temporal scale maintains its own confidence bounds, com-
puted using the segment’s local statistics. For a given window, the
width of the confidence bound is initialized as:

bound_width = 1.5 × std_score

(12)

It is then scaled according to the desired confidence level. Specif-
ically, the bound width is increased by 20% for high-confidence
settings (> 95%) and decreased by 20% for low-confidence settings
(< 90%). The final upper and lower bounds at each scale are then
computed as:

lower_bound = ¯𝑥 − bound_width
upper_bound = ¯𝑥 + bound_width

(13)

(14)

To integrate these multiple scales, MACS uses an attention mech-
anism that adjusts the relative importance of each scale based on
the local variance of the scores. Local variance is estimated using a
rolling variance window, defined as:

window = min(short_window, ⌊𝑛/10⌋)

(15)

Based on the level of local variance, different attention weights are
assigned:

• High variance (> 0.7): [0.6, 0.3, 0.1]
• Medium variance (> 0.3): [0.2, 0.6, 0.2]
• Low variance (≤ 0.3): [0.1, 0.3, 0.6]

MACS combines three temporal views - short, medium, long - to
stay sensitive to both brief spikes and slow drifts without hand-
retuning per dataset. The weighting should (i) favor the scale that
is most informative for the current regime and (ii) remain sta-
ble enough to avoid thrashing or single-scale domination. Short-
window variance rises during bursty, transient anomalies; long-
window variance/slope rise during gradual drifts or level shifts.

---

<!-- PAGE 4 -->

AIAT 2025, December 04–06, 2025, Kyoto, Japan

Li and Gautam

Therefore, in high-variance bursts, short gets more mass (catches
spikes), and in low-variance but trending periods, long gets more
mass (captures drifts). When neither extreme dominates, medium
arbitrates (reduces false positives from over-reactive short and iner-
tia from long). These weights can be fine tuned based on the model
and the dataset. In addition, the weights are used to compute a
combined confidence bound as a weighted sum across scales:

combined_bound =

3
∑︁

𝑖=1

weight𝑖 · bound𝑖

(16)

In addition to confidence sequences, MACS performs regime change
detection using a CUSUM-like procedure based on rolling statistics.
It tracks both the rolling mean and standard deviation over the long
window. A regime change is flagged if the normalized change in
mean exceeds 2.0, or if the change in standard deviation exceeds
1.5, defined respectively as:

mean_change =

std_change =

¯𝑥current − ¯𝑥historical
stdhistorical + 10−8
stdcurrent − stdhistorical
stdhistorical + 10−8

(17)

(18)

When a regime change is detected, MACS applies a conservative
thresholding policy that requires agreement between two indepen-
dent detection mechanisms.

The dual detection approach in MACS enhances robustness by
combining two complementary strategies. First, a threshold viola-
tion counting mechanism flags a point as anomalous if it exceeds
at least two out of three individual scale-specific thresholds:

violation =

3
∑︁

𝑖=1

scale_anomalies𝑖 ≥ 2

(19)

Second, MACS uses the attention-weighted combined bounds
to detect deviations from the contextually prioritized envelope. A
point is flagged as anomalous if its score lies outside this combined
range:

attention_anomalies = (𝑥 < combined_lower) ∨

(𝑥 > combined_upper)

(20)

The final decision rule is regime-aware. Under normal operating
conditions, anomalies are flagged solely based on the attention-
weighted bounds. However, during regime changes, both the thresh-
old violation and the attention anomaly conditions must be satis-
fied simultaneously. Finally, MACS applies an additional percentile-
based filter to avoid over-detection. This step discards low-magnitude
outliers by requiring anomaly scores to exceed a global percentile
threshold. The final anomaly mask is obtained as:

final_anomalies = anomalies ∧

percentile_filter

(21)

This layered structure – combining multi-scale bounds, adaptive at-
tention, regime awareness, and statistical filtering – enables MACS
to balance sensitivity and precision in diverse streaming environ-
ments effectively.

To summarize, the algorithm flow is outlined below:

• Multi-Scale Analysis: Calculate confidence bounds at three

temporal scales

• Attention Calculation: Compute local variance and deter-

mine attention weights

• Bound Combination: Apply attention mechanism to com-

bine multi-scale bounds

• Regime Detection: Identify statistical regime changes using

CUSUM-like logic

• Dual Detection: Apply both threshold violation counting

and attention-weighted bounds

• Regime-Aware Decision: Combine detection methods based

on regime state

• Filtering: Apply percentile-based filtering for conservative-

ness

(The pseudocode of the algorithm flow is in Appendix B.)

3.3 Implementation and Pipeline
Both architectures process the time series as follows:

• Preprocessing: Remove apparent seasonality or fit basic

model to compute residuals (if needed) [6].

• Compute anomaly scores: A scoring function (e.g., abso-
lute changes, reconstruction errors from an autoencoder [3])
is streamed.

• Segmentation (SCS only): Segment incoming data by APCA

or K-means.

• Adaptive thresholding:

– Update segment- or scale-specific confidence sequences.
– Optionally apply additional percentile or mixture model

filtering [11].

• Decision layer: Flag anomalies using composite rules.

4 Experimental Results
We evaluated both SCS and MACS against traditional and state-
of-the-art adaptive methods on public datasets containing ground-
truth anomaly labels. Metrics include the confusion matrix, change
in accuracy, precision, recall, and F1-score compared to baseline.
The experiments run from July 5th, 2025, to July 31st, 2025, over a
month.

4.1 Experiment and Dataset Description
4.1.1 Baseline: Traditional Percentile Thresholding. Our reference
method follows the classic p-percentile rule.

(1) Reconstruction-error vector

Let 𝑥 ′
𝑡 be the output of the diffusion auto-encoder at time 𝑡
and 𝑥𝑡 the original series window. We compute the point-
wise L2 residual:

𝑟𝑡 = ∥𝑥𝑡 − 𝑥 ′

𝑡 ∥2

(22)

(2) Threshold selection

A global cut-off is chosen as the 99th percentile of the residual
distribution on the training split:

𝜃 = Percentile0.99 ({𝑟𝑡 }train)

(23)

(3) Decision rule

A time stamp is labelled anomalous iff 𝑟𝑡 > 𝜃 .

Although computationally trivial, this fixed-quantile rule cannot
adapt to regime shifts or changes in error variance – motivating
the adaptive approaches studied in the remainder of the paper.

---

<!-- PAGE 5 -->

Segmented Confidence Sequences and Multi-Scale Adaptive Confidence Segments
for Anomaly Detection in Nonstationary Time Series

AIAT 2025, December 04–06, 2025, Kyoto, Japan

Table 1: Overview of evaluated datasets

Table 2: Cross-Dataset F1-Score Delta (vs. Baseline)

of

Name
Dataset
Wafer Manufac-
turing

CalIt2

Google Cloud
Platform (GCP)

Science

Mars
Laboratory
(MSL)

Server Machine
Dataset (SMD)

CPU-KPI

Source & Scope

Anomaly Labels

Dataset

SCS APCA SCS KMEANS

MACS

inline

process-
151
control traces recorded
by
semiconductor
sensors during wafer
fabrication
People-count
sensor
at UC-Irvine’s CalIt2
building (15 weeks, 48
half-hour slots per day)
service-category
30
collected from
KPIs
internal
NVIDIA’s
DGX-Cloud
deploy-
ments
NASA Mars Science
Laboratory – 55 teleme-
try
from
channels
Curiosity rover
5-week trace from 28
production servers, 38
KPIs each
Seasonal
CPU-
utilisation KPI released
with Donut
(public
AIOps benchmark)

ground
from fab
(≈10%

Pass/fail
truth
test
lines
defective)

Event file with pe-
riods of abnormally
high footfall
(e.g.,
conferences)
Manually curated
incident tickets

73729 test points
with labelled off-
nominal
events
(10.7% anomalous)
labels
Point-level
(4.2% anomaly) and
attribution masks
Partial point labels
capacity-
from
planning alerts

Wafer Manufacturing
CalIt2
GCP
MSL
SMD
CPU-KPI

1.91 / 2.13
0.46 / 0.42
4.84 / 7.94
4.30 / 5.01
3.59 / 4.43
1.15 / 1.73

0.93 / 1.41
0.70 / 0.24
1.60 / 3.58
0.33 / 1.61
1.93 / 3.25
-0.18 / 0.28

2.17 / 2.23
0.46 / 0.42
4.84 / 7.94
4.30 / 4.98
3.45 / 4.31
1.05 / 1.69

Table 3: Performance delta on Wafer Manufacturing dataset

Method

SCS APCA
(𝛼 = 0.99)

SCS KMEANS
(𝛼 = 0.99)

MACS Multi-Scale
(𝛼 = 0.99)

SCS APCA
(𝛼 = 0.95)

SCS KMEANS
(𝛼 = 0.95)

MACS Multi-Scale
(𝛼 = 0.95)

Δ Accuracy Δ Precision Δ Recall Δ F1-Score

-0.0422

-0.3282

3.9952

1.9074

-0.0260

-0.3999

1.6643

0.9262

-0.0279

-0.1890

3.9952

2.1705

-0.0830

-0.4290

6.1595

2.1289

-0.0545

-0.4656

3.3286

1.4148

-0.0638

-0.3651

5.6595

2.2349

4.1.2 Datasets. Details for all dataset distributions are presented
in Appendix D.

4.1.3 Hyper-parameters and Variants.

• Confidence level 1 − 𝛼 for adaptive confidence sequences:

{0.05, 0.01}.

• Segmentation for SCS: Adaptive Piecewise Constant Approx-

imation (APCA) vs. k-means on residual variance.
• Baseline: fixed 99% percentile rule described above.

4.1.4 Evaluation Protocol. For every dataset we compute:

• Confusion-matrix counts (TP, FP, TN, FN)
• Change in Accuracy, Precision, Recall, F1 compared to base-

line

• Proportional improvement over the baseline, calculated as:

new_method − traditional_method
traditional_method

(24)

4.2 Quantitative Comparison
To provide a balanced assessment and address generalizability, we
evaluated SCS (APCA and K-means) and MACS across six diverse
public benchmark datasets: Wafer Manufacturing, CalIt2, Google
Cloud Platform (GCP), Mars Science Laboratory (MSL), Server Ma-
chine Dataset (SMD), and CPU-KPI (Donut). The main results sum-
marize the F1-score delta over the percentile baseline for each
approach; detailed results for all metrics and datasets appear in
Appendix D.

Table 4: Anomaly count comparison

Method

TP

TN

Traditional Percentile (99th percentile)
SCS APCA (𝛼 = 0.99)
SCS KMEANS (𝛼 = 0.99)
MACS Multi-Scale (𝛼 = 0.99)
SCS APCA (𝛼 = 0.95)
SCS KMEANS (𝛼 = 0.95)
MACS Multi-Scale (𝛼 = 0.95)

6
30
16
30
43
26
40

1608
1516
1556
1539
1437
1500
1471

FP

12
104
64
81
183
120
149

FN

137
113
127
113
100
117
103

Across all datasets, SCS and MACS substantially boost recall
and F1-score over the traditional static percentile baseline. Notably,
improvements are strongest on datasets with pronounced regime
shifts or multiscale anomalies (Wafer, SMD, GCP, MSL), while the
gains are less pronounced but still positive on noisier or more
stationary data (CalIt2, CPU-KPI). Precision consistently declines
in exchange for increased recall, reflecting the enhanced sensitivity
of adaptive thresholds.

Key results (Wafer Manufacturing dataset):

---

<!-- PAGE 6 -->

AIAT 2025, December 04–06, 2025, Kyoto, Japan

Li and Gautam

filtering, which is a fivefold increase over the traditional method
(which detects only six true positive anomalies).

In datasets with more complex temporal dynamics – such as
sudden spikes, short bursts, or overlapping regimes – MACS is
expected to outperform due to its ability to attend to fine-grained
and coarse-grained deviations simultaneously. In contrast, SCS may
be more effective when anomalies are aligned with persistent struc-
tural shifts, as it explicitly isolates and monitors regime-specific
statistics.

The success of both approaches lies in their ability to localize
statistical estimation. SCS adapts quickly to changes by segmenting
the time series into regions with approximately stationary behavior,
which allows for tight confidence bounds within each region. MACS,
on the other hand, incorporates temporal diversity through rolling
windows at multiple resolutions and adaptive attention weighting,
enabling it to respond to anomalies that manifest at different time
scales. Together, these techniques represent a principled move be-
yond static global thresholds and allow for a more interpretable,
robust, and timely anomaly detection in real-world settings.

Finally, while removing the percentile filter maximizes recall
and F1-score, this setting may not always be optimal in practice. In
noisy environments or when false positives carry significant cost,
reintroducing percentile filtering may be desirable to balance inter-
pretability with operational reliability. Thus, both SCS and MACS
offer flexible control over this trade-off depending on deployment
constraints.

5 Discussion
Our empirical findings reinforce the known limitations of static
thresholding techniques such as global percentiles and rolling quan-
tiles when applied to nonstationary time series data. These tradi-
tional approaches fail to account for dynamic distributional shifts,
leading to poor recall and under-detection of relevant anomalies
[9]. In contrast, the proposed SCS and MACS methods substan-
tially improve performance by incorporating structural and tem-
poral adaptivity. Specifically, they address evolving data behav-
ior through segmentation (SCS) and multi-scale temporal analysis
(MACS), yielding significant F1-score gains with only modest re-
ductions in precision.

Figure 5: Illustration of different thresholding strategy

Figure 3: Results for Wafer Manufacturing dataset 𝛼 = 0.99

Figure 4: Results for Wafer Manufacturing dataset 𝛼 = 0.95

4.3 Detailed Analysis
Both Segmented Confidence Sequences (SCS) and Multi-Scale Adap-
tive Confidence Segments (MACS) show significant performance
improvements over the traditional static percentile thresholding
approach across all evaluation metrics. Most notably, the F1-score
of both SCS and MACS with a confidence level of 𝛼 = 0.99 increases
approximately twice compared to the baseline, highlighting the
benefit of adaptive, context-aware thresholds. When the confidence
level is further reduced to 𝛼 = 0.95, recall improves substantially,
leading to an over two times increase in F1-score relative to the
baseline, even at the cost of a moderate decline in precision.

This trade-off between recall and precision reflects a typical pat-
tern in adaptive detection: lowering the confidence threshold leads
to more aggressive anomaly detection, capturing a larger propor-
tion of true positives at the risk of including more false positives.
SCS/MACS shrink local uncertainty when a regime is stable and
widen/shift bounds quickly after drift. This increases the chance
of catching weak, brief anomalies (higher recall). However, during
highly volatile intervals, short-window bounds react aggressively
and may flag noise outliers (lower precision). Interestingly, this
behavior is especially pronounced when the percentile filter is dis-
abled. As shown in the anomaly count comparison, both SCS and
MACS identify 30 true positive anomalies under 𝛼 = 0.99 with no

---

<!-- PAGE 7 -->

Segmented Confidence Sequences and Multi-Scale Adaptive Confidence Segments
for Anomaly Detection in Nonstationary Time Series

AIAT 2025, December 04–06, 2025, Kyoto, Japan

SCS is particularly well-suited to settings characterized by abrupt
regime shifts and piecewise stationarity, where local adaptation
via segmentation captures the changing statistical properties of the
signal. Its regime-specific confidence sequences offer interpretable
bounds and fast detection of contextual outliers. MACS, on the other
hand, is more flexible across a wider range of temporal patterns. By
leveraging multiple rolling windows and variance-sensitive atten-
tion mechanisms, MACS generalizes across both fast transients and
slow drifts. This makes it especially effective in environments with
layered or multi-scale anomaly behavior, such as bursty network
activity or gradual process degradation [13].

A key advantage of both approaches lies in their model-free,
unsupervised nature. Unlike many machine learning-based anom-
aly detectors, which often rely on labeled anomaly instances for
training and hyperparameter tuning, SCS and MACS operate with-
out supervision and retain explicit control over false alarm rates
through statistically principled confidence sequences. This is cru-
cial in high-stakes domains such as manufacturing, infrastructure
monitoring, or cybersecurity, where excessive false positives can
desensitize operators and degrade trust in automated systems [3, 7].
Despite these advantages, our work also highlights some signifi-
cant limitations and open challenges. The performance of SCS, in
particular, is sensitive to the structure of the time series. In datasets
that are highly stationary or exhibit noisy, unstructured behavior,
segmentation may fail to produce meaningful partitions. Poorly
defined segments can blur statistical distinctions and reduce detec-
tion quality. Similarly, while MACS benefits from its multi-scale
architecture, its effectiveness hinges on the appropriate calibration
of attention weights and confidence levels – parameters that may
need tuning depending on the domain and noise profile.

An important direction for future work is the development of
robust online segmentation algorithms capable of operating under
adversarial conditions or extreme nonstationarity. This includes
detecting latent regime transitions that are subtle, overlapping, or
induced by external interventions. Additionally, while this study
used fixed window sizes for MACS, there is potential in exploring
adaptive window scaling or learned attention mechanisms that
adjust over time based on predictive uncertainty or performance
feedback.

6 Conclusion
Adaptive thresholding is a critical component of reliable anomaly
detection in nonstationary time series, where static baselines often
fail to capture evolving data behavior. In this work, we introduced
and systematically evaluated two novel frameworks – Segmented
Confidence Sequences (SCS) and Multi-Scale Adaptive Confidence
Segments (MACS) – that integrate online confidence sequence the-
ory with localized statistical adaptation. By tailoring thresholding
to the structure and scale of the data, both methods deliver sta-
tistically principled, interpretable, and high-performing anomaly
detection.

Our experimental results on benchmark Wafer Manufacturing
datasets demonstrate that SCS and MACS significantly outperform
traditional percentile-based and rolling quantile methods, particu-
larly in terms of recall and F1-score. Both frameworks offer flexible
precision-recall trade-offs through tunable confidence levels and

percentile filtering, while maintaining robustness in unsupervised
settings.

Looking ahead, future work will explore extensions to multi-
variate time series, correlated or structured input streams, and
integration with inference-based anomaly scoring methods. These
directions aim to enhance further the expressiveness, generalizabil-
ity, and deployment readiness of adaptive thresholding strategies
for real-world anomaly detection.

Acknowledgments
This work was supported by DGXC Applied AI Lab, NVIDIA. The
authors thank Aaron Erickson, Saira Qureshi, Sena Ekiz and AIAT
2025 reviewers for their valuable feedback which led to important
improvements, including expanded dataset analysis and method-
ological transparency.

References
[1] Charu C. Aggarwal. 2015. Outlier Analysis (2nd ed.). Springer.
[2] Seyed Amin Aghabozorgi, Ali Seyed Shirkhorshidi, and Teh Ying Wah. 2015.
Time-series clustering – A decade review. Information Systems 53 (2015), 16–38.
[3] Subutai Ahmad, Alexander Lavin, Scott Purdy, and Zuha Agha. 2017. Unsuper-
vised real-time anomaly detection for streaming data. Neurocomputing 262 (2017),
134–147.

[4] Konstantinos Benidis, Yoshua Bengio, Marc Blais, et al. 2022. Machine learning
for time series forecasting: challenges and opportunities. Proc. IEEE 110, 5 (2022),
656–678.

[5] A. Blázquez-García, A. Conde, U. Mori, and J. A. Lozano. 2021. A review on
outlier/anomaly detection in time series data. Comput. Surveys 54, 3 (2021), 1–33.
[6] Peter J. Brockwell and Richard A. Davis. 2016. Time Series: Theory and Methods

(2nd ed.). Springer.

[7] V. Chandola, A. Banerjee, and V. Kumar. 2009. Anomaly detection: A survey.

Comput. Surveys 41, 3 (2009), 1–58.

[8] Marc G. Genton, Yuguo Chen, and William Kleiber. 2021. Statistical methods
for outlier detection. Annual Review of Statistics and Its Application 8 (2021),
297–321.

[9] Steven R. Howard, Aaditya Ramdas, Jasjeet Sekhon, et al. 2021. Time-uniform
Chernoff bounds via nonnegative supermartingales. Probability Surveys 18 (2021),
1–45.

[10] Eamonn Keogh, Kaushik Chakrabarti, Michael Pazzani, and Sharad Mehrotra.
2001. Locally adaptive dimensionality reduction for indexing large time series
databases. In Proceedings of the 2001 ACM SIGMOD International Conference on
Management of Data. 151–162.

[11] Peter J. Rousseeuw, Mia Hubert, and Wesley Schmitt. 2020. Robust statistics for
outlier detection. Wiley Interdisciplinary Reviews: Data Mining and Knowledge
Discovery 10, 5 (2020), e1380.

[12] Sophia Sun, Aaditya Ramdas, and Jing Lei. 2024. Online Adaptive Anomaly
Thresholding with Confidence Sequences. In Proceedings of the 41st International
Conference on Machine Learning (ICML).

[13] Jinlin Wang, Aaditya Ramdas, and Jing Lei. 2023. Robust and adaptive confidence
sequences for heavy-tailed data. J. Amer. Statist. Assoc. (2023). To appear.
[14] Yao Xue, Lingfei Wu, Pin-Yu Chen, and Bo Li. 2023. ADT: Agent-based Dynamic
Thresholding for Anomaly Detection. In Proceedings of the Adaptive and Learning
Agents Workshop (ALA 2023).

Appendix
A. Pseudocode for Segmented Confidence
Sequences (SCS)
# Pseudocode for SCS adaptive thresholding

# Input:
# time_series, window_size, confidence_level,
# n_segments, segmentation_method

# Step 1: Segment the time series
if segmentation_method == "APCA":

segments = APCA_segment(time_series,

---

<!-- PAGE 8 -->

AIAT 2025, December 04–06, 2025, Kyoto, Japan

Li and Gautam

D. Full Results Table
Wafer Manufacturing dataset distribution

Wafer Manufacturing dataset result

Method

SCS APCA
(𝛼 = 0.99)

SCS KMEANS
(𝛼 = 0.99)

MACS Multi-Scale
(𝛼 = 0.99)

SCS APCA
(𝛼 = 0.95)

SCS KMEANS
(𝛼 = 0.95)

MACS Multi-Scale
(𝛼 = 0.95)

Δ Accuracy Δ Precision Δ Recall Δ F1-Score

-0.0422

-0.3282

3.9952

1.9074

-0.0260

-0.3999

1.6643

0.9262

-0.0279

-0.1890

3.9952

2.1705

-0.0830

-0.4290

6.1595

2.1289

-0.0545

-0.4656

3.3286

1.4148

-0.0638

-0.3651

5.6595

2.2349

Calit dataset distribution

n_segments)

elif segmentation_method == "k-means":

segments = kmeans_segment(time_series,
n_segments)

# Step 2: Initialize confidence sequence per
segment
for segment in segments:

scores = compute_anomaly_scores(segment)
conf_bounds = init_confidence_sequence
(scores, confidence_level)...
# Step 3: Online update and anomaly detection

for new_point in stream:

assigned_segment = assign_to_segment
(new_point, segments)
update(assigned_segment, new_point)
if is_anomalous
(new_point, assigned_segment.conf_bounds):

flag_anomaly(new_point)

B. Pseudocode for Multi-Scale Adaptive
Confidence Segments (MACS)
# Pseudocode for MACS

# Input: time_series, short_window, medium_window,
# long_window, confidence_level

# Step 1:
# Maintain sliding windows at multiple scales
scales = [short_window, medium_window, long_window]
for scale in scales:

window_scores[scale] = initialize_window(scale)
conf_bounds[scale] = init_confidence_sequence
(window_scores[scale], confidence_level)

# Step 2: Online anomaly detection
for new_point in stream:
for scale in scales:

window_scores[scale].add(new_point)
update_confidence_sequence
(window_scores[scale],
confidence_level)
# Composite decision rule
violation_count = sum(is_anomalous(new_point,
conf_bounds[scale]) for scale in scales)
if violation_count >= threshold:
flag_anomaly(new_point)

C. Pipeline Diagram (Suggested Structure)

(1) Input: Time Series Data
(2) Preprocessing: Remove seasonality/trend if needed
(3) Segmentation Module:

• APCA or k-means segmentation (SCS)
• Multi-scale rolling windows (MACS)

(4) Adaptive Thresholding:

• Segment-specific/confidence sequence update (SCS)
• Multi-scale online bounds (MACS)

(5) Composite Detection Layer:

• Dual filtering: confidence violation and global percentile
• Anomaly decision based on a composite rule

Calit dataset result

---

<!-- PAGE 9 -->

Segmented Confidence Sequences and Multi-Scale Adaptive Confidence Segments
for Anomaly Detection in Nonstationary Time Series

AIAT 2025, December 04–06, 2025, Kyoto, Japan

Method

SCS APCA
(𝛼 = 0.99)

SCS KMEANS
(𝛼 = 0.99)

MACS Multi-Scale
(𝛼 = 0.99)

SCS APCA
(𝛼 = 0.95)

SCS KMEANS
(𝛼 = 0.95)

MACS Multi-Scale
(𝛼 = 0.95)

Δ Accuracy Δ Precision Δ Recall Δ F1-Score

-0.0542

-0.4799

3.0000

0.4600

-0.0518

-0.3990

3.7135

0.6957

-0.0542

-0.4799

3.0000

0.4600

-0.0772

-0.5286

3.8573

0.4200

-0.0933

-0.5981

3.7135

0.2436

-0.0772

-0.5286

3.8573

0.4200

GCP dataset distribution

MSL dataset result

Method

SCS APCA
(𝛼 = 0.99)

SCS KMEANS
(𝛼 = 0.99)

MACS Multi-Scale
(𝛼 = 0.99)

SCS APCA
(𝛼 = 0.95)

SCS KMEANS
(𝛼 = 0.95)

MACS Multi-Scale
(𝛼 = 0.95)

Δ Accuracy Δ Precision Δ Recall Δ F1-Score

-0.0710

-0.0070

8.0741

4.2980

0.0005

0.2847

0.3333

0.3283

-0.0710

-0.0070

8.0741

4.2980

-0.1109

-0.0685

11.5556

5.0101

-0.0106

0.2276

1.9352

1.6061

-0.1084

-0.0633

11.3611

4.9848

GCP dataset result

SMD dataset distribution

Method

SCS APCA
(𝛼 = 0.99)

SCS KMEANS
(𝛼 = 0.99)

MACS Multi-Scale
(𝛼 = 0.99)

SCS APCA
(𝛼 = 0.95)

SCS KMEANS
(𝛼 = 0.95)

MACS Multi-Scale
(𝛼 = 0.95)

Δ Accuracy Δ Precision Δ Recall Δ F1-Score

-0.0463

0.0585

6.5054

4.8418

-0.0073

0.2319

1.7527

1.6045

-0.0463

0.0585

6.5054

4.8418

-0.0923

0.0654

13.0645

7.9435

-0.0193

0.2723

4.2473

3.5819

-0.0923

0.0654

13.0645

7.9435

MSL dataset distribution

SMD dataset result

---

<!-- PAGE 10 -->

AIAT 2025, December 04–06, 2025, Kyoto, Japan

Li and Gautam

Δ Accuracy Δ Precision Δ Recall Δ F1-Score

CPU dataset result

Method

SCS APCA
(𝛼 = 0.99)

SCS KMEANS
(𝛼 = 0.99)

MACS Multi-Scale
(𝛼 = 0.99)

SCS APCA
(𝛼 = 0.95)

SCS KMEANS
(𝛼 = 0.95)

MACS Multi-Scale
(𝛼 = 0.95)

-0.0594

0.4030

9.2152

3.5938

-0.0146

0.4848

2.8481

1.9297

-0.0596

0.3576

8.8734

3.4453

-0.1199

0.3758

17.7342

4.4297

-0.0376

0.5091

6.5823

3.2500

-0.1198

0.3455

17.2785

4.3125

CPU dataset distribution

Method

SCS APCA
(𝛼 = 0.99)

SCS KMEANS
(𝛼 = 0.99)

MACS Multi-Scale
(𝛼 = 0.99)

SCS APCA
(𝛼 = 0.95)

SCS KMEANS
(𝛼 = 0.95)

MACS Multi-Scale
(𝛼 = 0.95)

Δ Accuracy Δ Precision Δ Recall Δ F1-Score

-0.0538

-0.4667

2.5971

1.1456

-0.0110

-0.5353

-0.0777

-0.1758

-0.0522

-0.4796

2.3932

1.0549

-0.1084

-0.4867

5.4903

1.7335

-0.0279

-0.5495

0.7039

0.2802

-0.1064

-0.4913

5.3155

1.6923

<!-- MARKITDOWN CONVERSION -->

<!-- Full MarkItDown conversion for formatting fidelity. -->

Segmented Confidence Sequences and Multi-Scale Adaptive
Confidence Segments for Anomaly Detection in Nonstationary
Time Series
MuyanAnnaLi AditiGautam
NVIDIA NVIDIA
SantaClara,USA SantaClara,USA
annali@nvidia.com adgautam@nvidia.com
Abstract forpreventingfaults,reducingrisk,andensuringoperationalrelia-
Astimeseriesdatabecomeincreasinglyprevalentindomainssuch bility[7].Unlikestaticdatasets,timeseriesoftenexhibitevolving
asmanufacturing,IT,andinfrastructuremonitoring,anomalyde- behavior,includingtrends,seasonality,andabruptregimeshifts,
tectionmustadapttononstationaryenvironmentswherestatistical makinganomalydetectionaparticularlychallengingproblem.
propertiesshiftovertime.Traditionalstaticthresholdsareeasily Inrecentyears,researchershavedevelopedadvancedtechniques
renderedobsoletebyregimeshifts,conceptdrift,ormulti-scale thatgobeyondsimplestaticthresholds.Approachessuchasro-
changes.Toaddressthesechallenges,weintroduceandempirically bustmovingwindows,onlinequantileestimation,andconfidence
evaluatetwonoveladaptivethresholdingframeworks:Segmented sequencetheoryhaveemergedtoprovidemoreadaptiveandsta-
ConfidenceSequences(SCS)andMulti-ScaleAdaptiveConfidence tisticallyprincipledanomalydetection[9,13].Thesemethodsaim
Segments(MACS).Bothleveragestatisticalonlinelearningand to balance computational efficiency with real-time adaptability,
segmentationprinciplesforlocal,contextuallysensitiveadaptation, enablingdetectionsystemstorespondtochangingdatadynamics.
maintainingguaranteesonfalsealarmratesevenunderevolving However,existingadaptivethresholdingmethodsoftenstruggle
distributions.Ourexperimentsacrosssixpublicbenchmarkdatasets whendataexhibitmultipletemporalscalesorsuddenregimeshifts.
showsignificantF1-scoreimprovementcomparedtotraditional Fixed-windoworglobalpercentile-basedstrategiesmayeitherfail
percentileandrollingquantileapproaches.Thisworkdemonstrates tocapturelocalvariations,leadingtomissedanomalies,orproduce
thatrobust,statisticallyprincipledadaptivethresholdsenablere- excessivefalsepositiveswhenthebaselinedrifts[4].Thishighlights
liable, interpretable, and timely detection of diverse real-world theneedforathresholdingframeworkthatcansimultaneously
anomalies. adapttobothabruptandgradualchangesindatadistribution.
Toaddressthesechallenges,wecontributetwonovelframeworks
CCSConcepts foradaptivethresholding.
•Computingmethodologies→Machinelearning;Anomaly
• SegmentedConfidenceSequences(SCS)segmentstimeseries
detection;•Informationsystems→Dataanalytics.
byregime,maintainingdistinctconfidence-basedboundsper
segment,andadaptstolocalratherthanglobalstatistics.
Keywords
• Multi-ScaleAdaptiveConfidenceSegments(MACS)isan
AnomalyDetection,AdaptiveThresholding,ConfidenceSequences, approachthatadaptsdetectionsimultaneouslyatmultiple
Multi-ScaleAnalysis,NonstationaryTimeSeries windowlengths,enablingthedetectionofbothrapidbursts
andslowregimechanges.
ACMReferenceFormat:
MuyanAnnaLiandAditiGautam.2025.SegmentedConfidenceSequences • Comprehensiveexperimentalevaluationsupportingstatisti-
andMulti-ScaleAdaptiveConfidenceSegmentsforAnomalyDetectionin callysignificantimprovementsovertraditionalpercentileor
NonstationaryTimeSeries.In20255thInternationalConferenceonArtificial fixedadaptivethresholds.
IntelligenceandApplicationTechnologies(AIAT2025),December04–06,2025,
Kyoto,Japan.ACM,NewYork,NY,USA,10pages.https://doi.org/10.1145/
3787120.3787130 2 RelatedWork
2.1 StaticandTraditionalThresholding
1 Introduction
Earlyapproachesreliedonfixedglobalthresholds–oftenprescribed
Timeseriesdataareubiquitousacrossmodernapplications,fromin- asmean±𝑘𝜎orastaticquantile–assumingstationarityandi.i.d.
dustrialprocessmonitoringandpredictivemaintenancetofinancial
observations[7].Althougheasytoimplement,thesemethodsfail
marketsandsensor-drivensystems.Detectinganomalies—unusual
underconceptdriftordynamicvarianceandarepronetofalse
patternsorbehaviorsthatdeviatefromexpectedtrends—iscrucial
positivesinpracticalsystems[5].
Percentile-basedapproaches,suchasthe99thpercentilethresh-
old,adjustforheavytailsbutstillfalterunderpersistentdistribu-
ThisworkislicensedunderaCreativeCommonsAttribution4.0InternationalLicense. tionaldriftornonstationarity,asshowninbenchmarkstudies[8].
AIAT2025,Kyoto,Japan MethodsbasedonExtremeValueTheory(EVT)andthePeak-Over-
©2025Copyrightheldbytheowner/author(s).
Threshold(POT)modeltheempiricaltailbeyondahighthreshold
ACMISBN979-8-4007-2290-5/25/12
https://doi.org/10.1145/3787120.3787130 butstillassumethethresholdregimeisquasi-stationary[8].
6

AIAT2025,December04–06,2025,Kyoto,Japan LiandGautam
2.2 SlidingWindows,RollingStatistics,and confidencesequenceismaintainedforanomalyscorethresholds,us-
MovingQuantiles ingHoeffding’sinequalityfornon-parametricbounds[9].Segment-
specificanomalyflagsaretriggeredifnewscoresexceedtheupper
Adaptivemethodsusingslidingwindowsrecalculatethresholds
confidenceboundorfallbelowthelowerconfidencebound.
overarecentwindow–updatingthemean,standarddeviation,
or quantile in an online manner [1]. The exponential weighted
movingaverage(EWMA)improvesrapidadaptationtotrendsor
regimeswitches,butwindowsizedeterminessensitivityandis
oftenhardtotune[5].Non-parametricdynamicmodelsfurther
reducerelianceondistributionalassumptionsandaresuperiorin
recall[11].
2.3 Model-BasedandMachineLearning
Approaches
Forecasting-model-baseddetectionfitsmodelssuchasARIMAor
seasonaldecomposition,thentestsforoutliersinthemodelresid-
uals[6].Moreadvancedapproachesleverageautoencoders,deep
neuralnetworks,orreinforcementlearningagentstolearncontext-
sensitiveanomalyscoresordirectlyoptimizedetectionperformance
Figure1:IllustrationoftheSCSflow.
[3,4,14].However,thesemethodseitherlackexplicitstatistical
errorguaranteesorrequireconsiderablelabeledanomalydata.
SCSbeginsbypartitioningthetimeseriesintolocallystationary
2.4 ConfidenceSequencesforOnline segments,usingeitherAdaptivePiecewiseConstantApproximation
Adaptation (APCA)orfeature-basedK-meansclustering[2].APCAoperates
byiterativelyidentifyingoptimalsplitpointsthatminimizetotal
Confidencesequences(CS)–time-uniformintervalsguaranteeing
reconstructionerror,definedasthesumofsquareddeviationsfrom
correctcoverageatalltimes–areafoundationforrigorousthresh-
themeanwithineachsegment.Specifically,foraproposedsplit,
olding in nonstationary data, allowing error rate control under
thereconstructionerroriscalculatedas:
arbitrarystopping[9].Recentalgorithmscanmaintainconfidence
boundsforquantilesormeans,enablingadaptiveanomalyscor- total_error=left_error+right_error (1)
ingrobusttodrift,heavytails,oroutliers[13].ApplyingCS-based ∑︁
thresholdselectiontostreaminganomalydetectionisapromising left_error= (𝑥 𝑖 −𝑥¯ left )2 (2)
andnewlyemergingdirection[9,12]. right_error= ∑︁ (𝑥 𝑗 −𝑥¯ right )2 (3)
2.5 Segmentation-BasedLocalThresholding Thisprocesscontinuesrecursivelyuntilsegmentsfallbelowamin-
imumlengthconstraintornofurtherimprovementisobserved
Segmentingtimeseriesintolocallystationaryregimes–viaAPCA
accordingtoaspecifiedthreshold.Forflatregionsofthetimese-
orclustering–bringsstatisticalhomogeneitytothresholdestima-
ries,identifiedbyacoefficientofvariationbelow0.1,APCAdefaults
tion,allowingeachregimetohavealocallyfitted,adaptiverule
tofixed-lengthsegmentation,wheresegmentsizeissetto:
[2,10].Recentapproachesuseclustering(e.g.,k-means)onsum-
(cid:106)𝑛 (cid:107)
maryfeaturestocaptureregimechange,butstatisticaldecision max(200, ) (4)
boundarieswithineachsegmentremainunderexplored. 15
Formorevariabledata,acandidatesplitisacceptedonlyifthe
3 Methods minimizedreconstructionerrorsatisfies:
Wefocusontwonovel,unsupervisedadaptivethresholdingstrate- min_error<no_split_error×
(5)
giesforstreamingtimeseries:SegmentedConfidenceSequences improvement_threshold
(SCS)andMulti-ScaleAdaptiveConfidenceSegments(MACS).Both
aredesignedforpracticalanomalydetectionpipelines(seeFigure1 Theimprovementthresholdissetto0.7forhigh-varianceseries
andFigure2). and0.5formoderate-varianceseries.
Alternatively,SCSsupportsaK-meanssegmentationapproach
thatclustersslidingwindowrepresentationsofthetimeseriesbased
3.1 SegmentedConfidenceSequences(SCS)
on statistical features. For each window, features including the
SCS first performs time series segmentation using either Adap-
mean,standarddeviation,median,andskewnessareextracted,and
tivePiecewiseConstantApproximation(APCA)-whichiteratively
theresultingfeaturevectorsarenormalizedusingStandardScaler.
splits at points that minimize reconstruction error - or feature-
Formulti-dimensionaltimeseriesdata,thedimensionalityisre-
basedK-meansclusteringusingsliding-windowstatistics[2].Each
ducedbyaveragingacrossthefeaturedimensionssuchthat:
segmentisassumedtobelocallystationary,allowingforregime-
specificanomalydetection.Withineachsegment,anindependent data_1d=mean(𝑋,axis=1) if𝑋 ∈R𝑛×𝑑,𝑑 >1 (6)
7

SegmentedConfidenceSequencesandMulti-ScaleAdaptiveConfidenceSegments
forAnomalyDetectioninNonstationaryTimeSeries AIAT2025,December04–06,2025,Kyoto,Japan
Incaseswheretheclusteringprocessfailsduetoinsufficientvari-
abilityordegeneratedistributions,theentiresequenceistreatedas
asinglesegmenttopreservestability.
Withineachresultingsegment,regardlessofthesegmentation
method,SCSmaintainsanindependentconfidencesequencefor
thresholdinganomalyscores.TheseboundsarederivedusingHoeffding-
styleinequalities[9]andareparameterizedbythelocalstandard
deviation of the segment’s scores. The width of the confidence
boundisinitiallysetas:
bound_width=1.5×std_score (7)
Itisthenscaledbyafactorthatreflectsthedesiredconfidence
level.Specifically,iftheconfidencelevelexceeds95%,theboundis
widenedbyafactorof1.2;ifitisbelow90%,theboundisnarrowed
to0.8.Thefinalconfidenceintervalforeachscoreisgivenby:
lower_bound=𝑥¯−bound_width (8)
Figure2:IllustrationoftheMACSflow.
upper_bound=𝑥¯+bound_width (9)
Toensurerobustnessandavoidfalsepositivesfromlocalfluctua- Specifically,ittracksshort(e.g.,50steps),medium(e.g.,100steps),
tions,SCSusesacompositedetectioncriterion:apointisflagged andlong(e.g.,500steps)timescales,eachofwhichindependently
asanomalousonlyifitviolatesboththeconfidenceboundsand maintainsaconfidencesequence[5].ThisstructureenablesMACS
aglobalpercentilethreshold.Formally,anintermediateanomaly todetectabroadspectrumofanomalies,fromshort-termburststo
indicatoriscomputedas: slow-movingregimeshifts.Tofurtherenhanceadaptability,MACS
anomalies=(𝑥 <lower_bound)∨ incorporatesanattentionmechanismthatdynamicallyweighsthe
(𝑥 >upper_bound) (10) importanceofeachtemporalscalebasedonlocalvariancepatterns
inthedata.
Thefinalanomalydecisionismadevia: Eachtemporalscalemaintainsitsownconfidencebounds,com-
final_anomalies=anomalies∧ putedusingthesegment’slocalstatistics.Foragivenwindow,the
(11) widthoftheconfidenceboundisinitializedas:
percentile_filter
bound_width=1.5×std_score (12)
Tosummarize,thealgorithmflowisoutlinedbelow:
Itisthenscaledaccordingtothedesiredconfidencelevel.Specif-
• SegmentationPhase:ApplyAPCAorK-meanstoidentify
ically,theboundwidthisincreasedby20%forhigh-confidence
regimeboundaries
settings(>95%)anddecreasedby20%forlow-confidencesettings
• BoundCalculation:Computeconfidenceboundsforeach
(<90%).Thefinalupperandlowerboundsateachscalearethen
segmentindependently
computedas:
• PointAssignment:Dynamicallyassignincomingpointsto
theircorrespondingsegment lower_bound=𝑥¯−bound_width (13)
• AnomalyDetection:Compareeachpointtosegment-specific upper_bound=𝑥¯+bound_width (14)
thresholds
Tointegratethesemultiplescales,MACSusesanattentionmech-
• Filtering:Applypercentile-basedfilteringforconservative-
anismthatadjuststherelativeimportanceofeachscalebasedon
ness
thelocalvarianceofthescores.Localvarianceisestimatedusinga
(ThepseudocodeofthealgorithmflowisinAppendixA.)
rollingvariancewindow,definedas:
Incomingdatapointsaredynamicallyassignedtotheircorre-
window=min(short_window,⌊𝑛/10⌋) (15)
spondingsegment,andanomaliesaredetectedbycomparingeach
pointtothesegment-specific,adaptivelyupdatedthreshold.This Basedontheleveloflocalvariance,differentattentionweightsare
approachensuresthatanomalydetectionislocallycalibratedto assigned:
thecurrentregime,providingrobustdetectionevenasthedata • Highvariance(>0.7):[0.6,0.3,0.1]
distributionshiftsovertime.Themethodisunsupervised,requires • Mediumvariance(>0.3):[0.2,0.6,0.2]
nolabeledanomalies,andissuitableforbothbatchandstreaming • Lowvariance(≤0.3):[0.1,0.3,0.6]
data.
MACScombinesthreetemporalviews-short,medium,long-to
staysensitivetobothbriefspikesandslowdriftswithouthand-
3.2 Multi-ScaleAdaptiveConfidenceSegments
retuningperdataset.Theweightingshould(i)favorthescalethat
(MACS)
is most informative for the current regime and (ii) remain sta-
MACSisdesignedtocaptureanomaliesoccurringatdifferenttem- bleenoughtoavoidthrashingorsingle-scaledomination.Short-
poralresolutionsbymaintainingmultiplerollingwindowsofvary- windowvariancerisesduringbursty,transientanomalies;long-
inglengthsinparallel. windowvariance/sloperiseduringgradualdriftsorlevelshifts.
8

AIAT2025,December04–06,2025,Kyoto,Japan LiandGautam
Therefore,inhigh-variancebursts,shortgetsmoremass(catches • AttentionCalculation:Computelocalvarianceanddeter-
spikes),andinlow-variancebuttrendingperiods,longgetsmore mineattentionweights
mass(capturesdrifts).Whenneitherextremedominates,medium • BoundCombination:Applyattentionmechanismtocom-
arbitrates(reducesfalsepositivesfromover-reactiveshortandiner- binemulti-scalebounds
tiafromlong).Theseweightscanbefinetunedbasedonthemodel • RegimeDetection:Identifystatisticalregimechangesusing
andthedataset.Inaddition,theweightsareusedtocomputea CUSUM-likelogic
combinedconfidenceboundasaweightedsumacrossscales: • DualDetection:Applyboththresholdviolationcounting
andattention-weightedbounds
3
combined_bound= ∑︁ weight𝑖 ·bound𝑖 (16) • Regime-AwareDecision:Combinedetectionmethodsbased
𝑖=1 onregimestate
• Filtering:Applypercentile-basedfilteringforconservative-
Inadditiontoconfidencesequences,MACSperformsregimechange
ness
detectionusingaCUSUM-likeprocedurebasedonrollingstatistics.
Ittracksboththerollingmeanandstandarddeviationoverthelong (ThepseudocodeofthealgorithmflowisinAppendixB.)
window.Aregimechangeisflaggedifthenormalizedchangein
3.3 ImplementationandPipeline
meanexceeds2.0,orifthechangeinstandarddeviationexceeds
1.5,definedrespectivelyas: Botharchitecturesprocessthetimeseriesasfollows:
mean_change=
𝑥¯current −𝑥¯
historical (17)
• Preprocessing:Removeapparentseasonalityorfitbasic
std +10−8 modeltocomputeresiduals(ifneeded)[6].
historical
std −std • Computeanomalyscores:Ascoringfunction(e.g.,abso-
std_change= s c t u d rrent + h 1 i 0 st − or 8 ical (18) lutechanges,reconstructionerrorsfromanautoencoder[3])
historical
isstreamed.
Whenaregimechangeisdetected,MACSappliesaconservative • Segmentation(SCSonly):SegmentincomingdatabyAPCA
thresholdingpolicythatrequiresagreementbetweentwoindepen-
orK-means.
dentdetectionmechanisms. • Adaptivethresholding:
ThedualdetectionapproachinMACSenhancesrobustnessby
– Updatesegment-orscale-specificconfidencesequences.
combiningtwocomplementarystrategies.First,athresholdviola-
– Optionallyapplyadditionalpercentileormixturemodel
tioncountingmechanismflagsapointasanomalousifitexceeds
filtering[11].
atleasttwooutofthreeindividualscale-specificthresholds: • Decisionlayer:Flaganomaliesusingcompositerules.
3
∑︁
violation= scale_anomalies𝑖 ≥2 (19) 4 ExperimentalResults
𝑖=1
WeevaluatedbothSCSandMACSagainsttraditionalandstate-
Second,MACSusestheattention-weightedcombinedbounds of-the-artadaptivemethodsonpublicdatasetscontainingground-
todetectdeviationsfromthecontextuallyprioritizedenvelope.A truthanomalylabels.Metricsincludetheconfusionmatrix,change
pointisflaggedasanomalousifitsscoreliesoutsidethiscombined inaccuracy,precision,recall,andF1-scorecomparedtobaseline.
range: TheexperimentsrunfromJuly5th,2025,toJuly31st,2025,overa
attention_anomalies=(𝑥 <combined_lower)∨ month.
(20)
(𝑥 >combined_upper)
4.1 ExperimentandDatasetDescription
Thefinaldecisionruleisregime-aware.Undernormaloperating 4.1.1 Baseline:TraditionalPercentileThresholding. Ourreference
conditions,anomaliesareflaggedsolelybasedontheattention- methodfollowstheclassicp-percentilerule.
weightedbounds.However,duringregimechanges,boththethresh-
(1) Reconstruction-errorvector
oldviolationandtheattentionanomalyconditionsmustbesatis- Let𝑥
𝑡
′betheoutputofthediffusionauto-encoderattime𝑡
fiedsimultaneously.Finally,MACSappliesanadditionalpercentile-
and𝑥 𝑡 theoriginalserieswindow.Wecomputethepoint-
basedfiltertoavoidover-detection.Thisstepdiscardslow-magnitude
wiseL2residual:
outliersbyrequiringanomalyscorestoexceedaglobalpercentile
threshold.Thefinalanomalymaskisobtainedas: 𝑟 𝑡 =∥𝑥 𝑡 −𝑥 𝑡 ′∥ 2 (22)
final_anomalies=anomalies∧ (2) Thresholdselection
percentile_filter (21) Aglobalcut-offischosenasthe99thpercentileoftheresidual
distributiononthetrainingsplit:
Thislayeredstructure–combiningmulti-scalebounds,adaptiveat-
tention,regimeawareness,andstatisticalfiltering–enablesMACS 𝜃 =Percentile 0.99 ({𝑟 𝑡} train ) (23)
tobalancesensitivityandprecisionindiversestreamingenviron- (3) Decisionrule
mentseffectively. Atimestampislabelledanomalousiff𝑟 𝑡 >𝜃.
Tosummarize,thealgorithmflowisoutlinedbelow: Althoughcomputationallytrivial,thisfixed-quantilerulecannot
• Multi-ScaleAnalysis:Calculateconfidenceboundsatthree adapttoregimeshiftsorchangesinerrorvariance–motivating
temporalscales theadaptiveapproachesstudiedintheremainderofthepaper.
9

SegmentedConfidenceSequencesandMulti-ScaleAdaptiveConfidenceSegments
forAnomalyDetectioninNonstationaryTimeSeries AIAT2025,December04–06,2025,Kyoto,Japan
Table1:Overviewofevaluateddatasets Table2:Cross-DatasetF1-ScoreDelta(vs.Baseline)
Name of Source&Scope AnomalyLabels Dataset SCSAPCA SCSKMEANS MACS
Dataset
|               |                       |          |           |          | WaferManufacturing |     | 1.91/2.13 | 0.93/1.41 | 2.17/2.23 |
| ------------- | --------------------- | -------- | --------- | -------- | ------------------ | --- | --------- | --------- | --------- |
| WaferManufac- | 151 inline            | process- | Pass/fail | ground   |                    |     |           |           |           |
|               |                       |          |           |          | CalIt2             |     | 0.46/0.42 | 0.70/0.24 | 0.46/0.42 |
| turing        | controltracesrecorded |          | truth     | from fab |                    |     |           |           |           |
by semiconductor test lines (≈10% GCP 4.84/7.94 1.60/3.58 4.84/7.94
|     |                |       |            |     | MSL |     | 4.30/5.01 | 0.33/1.61 | 4.30/4.98 |
| --- | -------------- | ----- | ---------- | --- | --- | --- | --------- | --------- | --------- |
|     | sensors during | wafer | defective) |     |     |     |           |           |           |
|     |                |       |            |     | SMD |     | 3.59/4.43 | 1.93/3.25 | 3.45/4.31 |
fabrication
|              |                       |        |                   |               | CPU-KPI |     | 1.15/1.73 | -0.18/0.28 | 1.05/1.69 |
| ------------ | --------------------- | ------ | ----------------- | ------------- | ------- | --- | --------- | ---------- | --------- |
| CalIt2       | People-count          | sensor | Event             | file with pe- |         |     |           |            |           |
|              | at UC-Irvine’s        | CalIt2 | riodsofabnormally |               |         |     |           |            |           |
|              | building (15          | weeks, | 48 high footfall  | (e.g.,        |         |     |           |            |           |
|              | half-hourslotsperday) |        | conferences)      |               |         |     |           |            |           |
| Google Cloud | 30 service-category   |        | Manually          | curated       |         |     |           |            |           |
Platform(GCP) KPIs collected from incidenttickets Table3:PerformancedeltaonWaferManufacturingdataset
|     | NVIDIA’s  | internal |     |     |     |     |                      |         |           |
| --- | --------- | -------- | --- | --- | --- | --- | -------------------- | ------- | --------- |
|     | DGX-Cloud | deploy-  |     |     |     |     |                      |         |           |
|     |           |          |     |     |     |     | ΔAccuracy ΔPrecision | ΔRecall | ΔF1-Score |
Method
ments
SCSAPCA
| Mars Science | NASA Mars            | Science | 73729         | test points |           |     |         |                |        |
| ------------ | -------------------- | ------- | ------------- | ----------- | --------- | --- | ------- | -------------- | ------ |
|              |                      |         |               |             | (𝛼=0.99)  |     | -0.0422 | -0.3282 3.9952 | 1.9074 |
| Laboratory   | Laboratory–55teleme- |         | with labelled | off-        |           |     |         |                |        |
| (MSL)        | try channels         | from    | nominal       | events      | SCSKMEANS |     |         |                |        |
(𝛼=0.99)
|     |                |     |                  |     |     |     | -0.0260 | -0.3999 1.6643 | 0.9262 |
| --- | -------------- | --- | ---------------- | --- | --- | --- | ------- | -------------- | ------ |
|     | Curiosityrover |     | (10.7%anomalous) |     |     |     |         |                |        |
MACSMulti-Scale
| ServerMachine | 5-week trace | from     | 28 Point-level      | labels |          |     |         |                |        |
| ------------- | ------------ | -------- | ------------------- | ------ | -------- | --- | ------- | -------------- | ------ |
|               |              |          |                     |        | (𝛼=0.99) |     | -0.0279 | -0.1890 3.9952 | 2.1705 |
| Dataset(SMD)  | production   | servers, | 38 (4.2%anomaly)and |        |          |     |         |                |        |
|               | KPIseach     |          | attributionmasks    |        | SCSAPCA  |     |         |                |        |
(𝛼=0.95)
CPU-KPI Seasonal CPU- Partialpointlabels -0.0830 -0.4290 6.1595 2.1289
SCSKMEANS
|     | utilisationKPIreleased |         | from           | capacity- |                 |     |         |                |        |
| --- | ---------------------- | ------- | -------------- | --------- | --------------- | --- | ------- | -------------- | ------ |
|     |                        |         |                |           | (𝛼=0.95)        |     | -0.0545 | -0.4656 3.3286 | 1.4148 |
|     | with Donut             | (public | planningalerts |           |                 |     |         |                |        |
|     | AIOpsbenchmark)        |         |                |           | MACSMulti-Scale |     |         |                |        |
(𝛼=0.95)
|                 |                                               |     |     |     |     |     | -0.0638 | -0.3651 5.6595 | 2.2349 |
| --------------- | --------------------------------------------- | --- | --- | --- | --- | --- | ------- | -------------- | ------ |
| 4.1.2 Datasets. | Detailsforalldatasetdistributionsarepresented |     |     |     |     |     |         |                |        |
inAppendixD.
4.1.3 Hyper-parametersandVariants.
| • Confidencelevel1−𝛼 |     | foradaptiveconfidencesequences: |     |     |     |     |     |     |     |
| -------------------- | --- | ------------------------------- | --- | --- | --- | --- | --- | --- | --- |
Table4:Anomalycountcomparison
{0.05,0.01}.
•
SegmentationforSCS:AdaptivePiecewiseConstantApprox-
|     |     |     |     |     | Method |     |     | TP TN | FP FN |
| --- | --- | --- | --- | --- | ------ | --- | --- | ----- | ----- |
imation(APCA)vs.k-meansonresidualvariance.
|     |     |     |     |     | TraditionalPercentile(99thpercentile) |     |     | 6 1608 | 12 137 |
| --- | --- | --- | --- | --- | ------------------------------------- | --- | --- | ------ | ------ |
• Baseline:fixed99%percentileruledescribedabove.
|                           |                           |     |     |     | SCSAPCA(𝛼   | =0.99) |     | 30 1516 | 104 113 |
| ------------------------- | ------------------------- | --- | --- | --- | ----------- | ------ | --- | ------- | ------- |
| 4.1.4 EvaluationProtocol. | Foreverydatasetwecompute: |     |     |     |             |        |     |         |         |
|                           |                           |     |     |     | SCSKMEANS(𝛼 | =0.99) |     |         |         |
|                           |                           |     |     |     |             |        |     | 16 1556 | 64 127  |
• Confusion-matrixcounts(TP,FP,TN,FN)
|     |     |     |     |     | MACSMulti-Scale(𝛼 |     | =0.99) | 30 1539 | 81 113 |
| --- | --- | --- | --- | --- | ----------------- | --- | ------ | ------- | ------ |
• ChangeinAccuracy,Precision,Recall,F1comparedtobase-
| line |     |     |     |     | SCSAPCA(𝛼 | =0.95) |     | 43 1437 | 183 100 |
| ---- | --- | --- | --- | --- | --------- | ------ | --- | ------- | ------- |
• Proportionalimprovementoverthebaseline,calculatedas: SCSKMEANS(𝛼 =0.95)
|     |     |     |     |     |     |     |     | 26 1500 | 120 117 |
| --- | --- | --- | --- | --- | --- | --- | --- | ------- | ------- |
new_method−traditional_method MACSMulti-Scale(𝛼 =0.95) 40 1471 149 103
(24)
traditional_method
4.2 QuantitativeComparison
Toprovideabalancedassessmentandaddressgeneralizability,we
evaluatedSCS(APCAandK-means)andMACSacrosssixdiverse
publicbenchmarkdatasets:WaferManufacturing,CalIt2,Google
CloudPlatform(GCP),MarsScienceLaboratory(MSL),ServerMa- Acrossalldatasets,SCSandMACSsubstantiallyboostrecall
chineDataset(SMD),andCPU-KPI(Donut).Themainresultssum- andF1-scoreoverthetraditionalstaticpercentilebaseline.Notably,
marize the F1-score delta over the percentile baseline for each improvementsarestrongestondatasetswithpronouncedregime
approach;detailedresultsforallmetricsanddatasetsappearin shiftsormultiscaleanomalies(Wafer,SMD,GCP,MSL),whilethe
AppendixD. gains are less pronounced but still positive on noisier or more
stationarydata(CalIt2,CPU-KPI).Precisionconsistentlydeclines
inexchangeforincreasedrecall,reflectingtheenhancedsensitivity
ofadaptivethresholds.
Keyresults(WaferManufacturingdataset):
10

AIAT2025,December04–06,2025,Kyoto,Japan LiandGautam
filtering,whichisafivefoldincreaseoverthetraditionalmethod
(whichdetectsonlysixtruepositiveanomalies).
Indatasetswithmorecomplextemporaldynamics–suchas
sudden spikes, short bursts, or overlapping regimes – MACS is
expectedtooutperformduetoitsabilitytoattendtofine-grained
andcoarse-graineddeviationssimultaneously.Incontrast,SCSmay
bemoreeffectivewhenanomaliesarealignedwithpersistentstruc-
turalshifts,asitexplicitlyisolatesandmonitorsregime-specific
statistics.
Thesuccessofbothapproachesliesintheirabilitytolocalize
statisticalestimation.SCSadaptsquicklytochangesbysegmenting
thetimeseriesintoregionswithapproximatelystationarybehavior,
whichallowsfortightconfidenceboundswithineachregion.MACS,
ontheotherhand,incorporatestemporaldiversitythroughrolling
Figure3:ResultsforWaferManufacturingdataset𝛼 =0.99
windowsatmultipleresolutionsandadaptiveattentionweighting,
enablingittorespondtoanomaliesthatmanifestatdifferenttime
scales.Together,thesetechniquesrepresentaprincipledmovebe-
yondstaticglobalthresholdsandallowforamoreinterpretable,
robust,andtimelyanomalydetectioninreal-worldsettings.
Finally,whileremovingthepercentilefiltermaximizesrecall
andF1-score,thissettingmaynotalwaysbeoptimalinpractice.In
noisyenvironmentsorwhenfalsepositivescarrysignificantcost,
reintroducingpercentilefilteringmaybedesirabletobalanceinter-
pretabilitywithoperationalreliability.Thus,bothSCSandMACS
offerflexiblecontroloverthistrade-offdependingondeployment
constraints.
5 Discussion
Ourempiricalfindingsreinforcetheknownlimitationsofstatic
thresholdingtechniquessuchasglobalpercentilesandrollingquan-
tileswhenappliedtononstationarytimeseriesdata.Thesetradi-
Figure4:ResultsforWaferManufacturingdataset𝛼 =0.95
tionalapproachesfailtoaccountfordynamicdistributionalshifts,
leadingtopoorrecallandunder-detectionofrelevantanomalies
4.3 DetailedAnalysis [9].Incontrast,theproposedSCSandMACSmethodssubstan-
tiallyimproveperformancebyincorporatingstructuralandtem-
BothSegmentedConfidenceSequences(SCS)andMulti-ScaleAdap-
poral adaptivity. Specifically, they address evolving data behav-
tiveConfidenceSegments(MACS)showsignificantperformance
iorthroughsegmentation(SCS)andmulti-scaletemporalanalysis
improvementsoverthetraditionalstaticpercentilethresholding
(MACS),yieldingsignificantF1-scoregainswithonlymodestre-
approachacrossallevaluationmetrics.Mostnotably,theF1-score
ductionsinprecision.
ofbothSCSandMACSwithaconfidencelevelof𝛼 =0.99increases
approximatelytwicecomparedtothebaseline,highlightingthe
benefitofadaptive,context-awarethresholds.Whentheconfidence
levelisfurtherreducedto𝛼 =0.95,recallimprovessubstantially,
leadingtoanovertwotimesincreaseinF1-scorerelativetothe
baseline,evenatthecostofamoderatedeclineinprecision.
Thistrade-offbetweenrecallandprecisionreflectsatypicalpat-
terninadaptivedetection:loweringtheconfidencethresholdleads
tomoreaggressiveanomalydetection,capturingalargerpropor-
tionoftruepositivesattheriskofincludingmorefalsepositives.
SCS/MACSshrinklocaluncertaintywhenaregimeisstableand
widen/shiftboundsquicklyafterdrift.Thisincreasesthechance
ofcatchingweak,briefanomalies(higherrecall).However,during
highlyvolatileintervals,short-windowboundsreactaggressively
andmayflagnoiseoutliers(lowerprecision).Interestingly,this
behaviorisespeciallypronouncedwhenthepercentilefilterisdis-
abled.Asshownintheanomalycountcomparison,bothSCSand
MACSidentify30truepositiveanomaliesunder𝛼 =0.99withno Figure5:Illustrationofdifferentthresholdingstrategy
11

SegmentedConfidenceSequencesandMulti-ScaleAdaptiveConfidenceSegments
forAnomalyDetectioninNonstationaryTimeSeries AIAT2025,December04–06,2025,Kyoto,Japan
SCSisparticularlywell-suitedtosettingscharacterizedbyabrupt percentilefiltering,whilemaintainingrobustnessinunsupervised
regimeshiftsandpiecewisestationarity,wherelocaladaptation settings.
viasegmentationcapturesthechangingstatisticalpropertiesofthe Lookingahead,futureworkwillexploreextensionstomulti-
signal.Itsregime-specificconfidencesequencesofferinterpretable variate time series, correlated or structured input streams, and
boundsandfastdetectionofcontextualoutliers.MACS,ontheother integrationwithinference-basedanomalyscoringmethods.These
hand,ismoreflexibleacrossawiderrangeoftemporalpatterns.By directionsaimtoenhancefurthertheexpressiveness,generalizabil-
leveragingmultiplerollingwindowsandvariance-sensitiveatten- ity,anddeploymentreadinessofadaptivethresholdingstrategies
tionmechanisms,MACSgeneralizesacrossbothfasttransientsand forreal-worldanomalydetection.
slowdrifts.Thismakesitespeciallyeffectiveinenvironmentswith
layeredormulti-scaleanomalybehavior,suchasburstynetwork Acknowledgments
activityorgradualprocessdegradation[13].
ThisworkwassupportedbyDGXCAppliedAILab,NVIDIA.The
Akeyadvantageofbothapproachesliesintheirmodel-free,
authorsthankAaronErickson,SairaQureshi,SenaEkizandAIAT
unsupervisednature.Unlikemanymachinelearning-basedanom-
2025reviewersfortheirvaluablefeedbackwhichledtoimportant
alydetectors,whichoftenrelyonlabeledanomalyinstancesfor
improvements,includingexpandeddatasetanalysisandmethod-
trainingandhyperparametertuning,SCSandMACSoperatewith-
ologicaltransparency.
outsupervisionandretainexplicitcontroloverfalsealarmrates
throughstatisticallyprincipledconfidencesequences.Thisiscru- References
cialinhigh-stakesdomainssuchasmanufacturing,infrastructure
[1] CharuC.Aggarwal.2015.OutlierAnalysis(2nded.).Springer.
monitoring,orcybersecurity,whereexcessivefalsepositivescan [2] SeyedAminAghabozorgi,AliSeyedShirkhorshidi,andTehYingWah.2015.
desensitizeoperatorsanddegradetrustinautomatedsystems[3,7]. Time-seriesclustering–Adecadereview.InformationSystems53(2015),16–38.
[3] SubutaiAhmad,AlexanderLavin,ScottPurdy,andZuhaAgha.2017.Unsuper-
Despitetheseadvantages,ourworkalsohighlightssomesignifi-
visedreal-timeanomalydetectionforstreamingdata.Neurocomputing262(2017),
cantlimitationsandopenchallenges.TheperformanceofSCS,in 134–147.
particular,issensitivetothestructureofthetimeseries.Indatasets [4] KonstantinosBenidis,YoshuaBengio,MarcBlais,etal.2022.Machinelearning
fortimeseriesforecasting:challengesandopportunities.Proc.IEEE110,5(2022),
thatarehighlystationaryorexhibitnoisy,unstructuredbehavior, 656–678.
segmentationmayfailtoproducemeaningfulpartitions.Poorly [5] A.Blázquez-García,A.Conde,U.Mori,andJ.A.Lozano.2021. Areviewon
outlier/anomalydetectionintimeseriesdata.Comput.Surveys54,3(2021),1–33.
definedsegmentscanblurstatisticaldistinctionsandreducedetec-
[6] PeterJ.BrockwellandRichardA.Davis.2016.TimeSeries:TheoryandMethods
tionquality.Similarly,whileMACSbenefitsfromitsmulti-scale (2nded.).Springer.
architecture,itseffectivenesshingesontheappropriatecalibration [7] V.Chandola,A.Banerjee,andV.Kumar.2009. Anomalydetection:Asurvey.
Comput.Surveys41,3(2009),1–58.
ofattentionweightsandconfidencelevels–parametersthatmay
[8] MarcG.Genton,YuguoChen,andWilliamKleiber.2021. Statisticalmethods
needtuningdependingonthedomainandnoiseprofile. foroutlierdetection. AnnualReviewofStatisticsandItsApplication8(2021),
Animportantdirectionforfutureworkisthedevelopmentof 297–321.
[9] StevenR.Howard,AadityaRamdas,JasjeetSekhon,etal.2021.Time-uniform
robustonlinesegmentationalgorithmscapableofoperatingunder Chernoffboundsvianonnegativesupermartingales.ProbabilitySurveys18(2021),
adversarialconditionsorextremenonstationarity.Thisincludes 1–45.
[10] EamonnKeogh,KaushikChakrabarti,MichaelPazzani,andSharadMehrotra.
detectinglatentregimetransitionsthataresubtle,overlapping,or
2001.Locallyadaptivedimensionalityreductionforindexinglargetimeseries
inducedbyexternalinterventions.Additionally,whilethisstudy databases.InProceedingsofthe2001ACMSIGMODInternationalConferenceon
usedfixedwindowsizesforMACS,thereispotentialinexploring ManagementofData.151–162.
[11] PeterJ.Rousseeuw,MiaHubert,andWesleySchmitt.2020.Robuststatisticsfor
adaptive window scaling or learned attention mechanisms that
outlierdetection.WileyInterdisciplinaryReviews:DataMiningandKnowledge
adjustovertimebasedonpredictiveuncertaintyorperformance Discovery10,5(2020),e1380.
feedback. [12] SophiaSun,AadityaRamdas,andJingLei.2024. OnlineAdaptiveAnomaly
ThresholdingwithConfidenceSequences.InProceedingsofthe41stInternational
ConferenceonMachineLearning(ICML).
[13] JinlinWang,AadityaRamdas,andJingLei.2023.Robustandadaptiveconfidence
6 Conclusion sequencesforheavy-taileddata.J.Amer.Statist.Assoc.(2023). Toappear.
[14] YaoXue,LingfeiWu,Pin-YuChen,andBoLi.2023.ADT:Agent-basedDynamic
Adaptivethresholdingisacriticalcomponentofreliableanomaly ThresholdingforAnomalyDetection.InProceedingsoftheAdaptiveandLearning
detectioninnonstationarytimeseries,wherestaticbaselinesoften AgentsWorkshop(ALA2023).
failtocaptureevolvingdatabehavior.Inthiswork,weintroduced
andsystematicallyevaluatedtwonovelframeworks–Segmented Appendix
ConfidenceSequences(SCS)andMulti-ScaleAdaptiveConfidence A.PseudocodeforSegmentedConfidence
Segments(MACS)–thatintegrateonlineconfidencesequencethe-
Sequences(SCS)
orywithlocalizedstatisticaladaptation.Bytailoringthresholding
tothestructureandscaleofthedata,bothmethodsdeliversta- # Pseudocode for SCS adaptive thresholding
tisticallyprincipled,interpretable,andhigh-performinganomaly
# Input:
detection.
# time_series, window_size, confidence_level,
OurexperimentalresultsonbenchmarkWaferManufacturing
# n_segments, segmentation_method
datasetsdemonstratethatSCSandMACSsignificantlyoutperform
traditionalpercentile-basedandrollingquantilemethods,particu- # Step 1: Segment the time series
larlyintermsofrecallandF1-score.Bothframeworksofferflexible if segmentation_method == "APCA":
precision-recalltrade-offsthroughtunableconfidencelevelsand segments = APCA_segment(time_series,
12

| AIAT2025,December04–06,2025,Kyoto,Japan |               |     |                    |     | LiandGautam |
| --------------------------------------- | ------------- | --- | ------------------ | --- | ----------- |
| n_segments)                             |               |     | D.FullResultsTable |     |             |
| elif segmentation_method                | == "k-means": |     |                    |     |             |
WaferManufacturingdatasetdistribution
| segments | = kmeans_segment(time_series, |     |     |     |     |
| -------- | ----------------------------- | --- | --- | --- | --- |
n_segments)
| # Step 2: | Initialize confidence | sequence per |     |     |     |
| --------- | --------------------- | ------------ | --- | --- | --- |
segment
| for segment              | in segments:                      |                   |     |     |     |
| ------------------------ | --------------------------------- | ----------------- | --- | --- | --- |
| scores                   | = compute_anomaly_scores(segment) |                   |     |     |     |
| conf_bounds              | = init_confidence_sequence        |                   |     |     |     |
| (scores,                 | confidence_level)...              |                   |     |     |     |
| # Step                   | 3: Online update and              | anomaly detection |     |     |     |
| for new_point            | in stream:                        |                   |     |     |     |
| assigned_segment         | = assign_to_segment               |                   |     |     |     |
| (new_point,              | segments)                         |                   |     |     |     |
| update(assigned_segment, | new_point)                        |                   |     |     |     |
if is_anomalous
| (new_point, | assigned_segment.conf_bounds): |     |     |     |     |
| ----------- | ------------------------------ | --- | --- | --- | --- |
flag_anomaly(new_point)
B.PseudocodeforMulti-ScaleAdaptive WaferManufacturingdatasetresult
ConfidenceSegments(MACS)
| # Pseudocode          | for MACS         |                |          |                      |                   |
| --------------------- | ---------------- | -------------- | -------- | -------------------- | ----------------- |
|                       |                  |                |          | ΔAccuracy ΔPrecision | ΔRecall ΔF1-Score |
| # Input: time_series, | short_window,    | medium_window, | Method   |                      |                   |
| # long_window,        | confidence_level |                | SCSAPCA  |                      |                   |
|                       |                  |                | (𝛼=0.99) | -0.0422 -0.3282      | 3.9952 1.9074     |
# Step 1:
SCSKMEANS
| # Maintain              | sliding windows at multiple | scales       | (𝛼=0.99) |                 |               |
| ----------------------- | --------------------------- | ------------ | -------- | --------------- | ------------- |
|                         |                             |              |          | -0.0260 -0.3999 | 1.6643 0.9262 |
| scales = [short_window, | medium_window,              | long_window] |          |                 |               |
MACSMulti-Scale
| for scale            | in scales:                 |     |          |                 |               |
| -------------------- | -------------------------- | --- | -------- | --------------- | ------------- |
|                      |                            |     | (𝛼=0.99) | -0.0279 -0.1890 | 3.9952 2.1705 |
| window_scores[scale] | = initialize_window(scale) |     |          |                 |               |
| conf_bounds[scale]   | = init_confidence_sequence |     | SCSAPCA  |                 |               |
(𝛼=0.95)
(window_scores[scale], confidence_level) -0.0830 -0.4290 6.1595 2.1289
SCSKMEANS
# Step 2: Online anomaly detection (𝛼=0.95) -0.0545 -0.4656 3.3286 1.4148
| for new_point | in stream: |     |     |     |     |
| ------------- | ---------- | --- | --- | --- | --- |
MACSMulti-Scale
| for scale | in scales: |     | (𝛼=0.95) |                 |               |
| --------- | ---------- | --- | -------- | --------------- | ------------- |
|           |            |     |          | -0.0638 -0.3651 | 5.6595 2.2349 |
window_scores[scale].add(new_point)
update_confidence_sequence
(window_scores[scale],
confidence_level)
| # Composite         | decision rule                 |            | Calitdatasetdistribution |     |     |
| ------------------- | ----------------------------- | ---------- | ------------------------ | --- | --- |
| violation_count     | = sum(is_anomalous(new_point, |            |                          |     |     |
| conf_bounds[scale]) | for scale                     | in scales) |                          |     |     |
| if violation_count  | >= threshold:                 |            |                          |     |     |
flag_anomaly(new_point)
C.PipelineDiagram(SuggestedStructure)
(1) Input:TimeSeriesData
(2) Preprocessing:Removeseasonality/trendifneeded
(3) SegmentationModule:
• APCAork-meanssegmentation(SCS)
• Multi-scalerollingwindows(MACS)
(4) AdaptiveThresholding:
• Segment-specific/confidencesequenceupdate(SCS)
•
Multi-scaleonlinebounds(MACS)
(5) CompositeDetectionLayer:
• Dualfiltering:confidenceviolationandglobalpercentile
| • Anomalydecisionbasedonacompositerule |     |     | Calitdatasetresult |     |     |
| -------------------------------------- | --- | --- | ------------------ | --- | --- |
13

SegmentedConfidenceSequencesandMulti-ScaleAdaptiveConfidenceSegments
forAnomalyDetectioninNonstationaryTimeSeries AIAT2025,December04–06,2025,Kyoto,Japan
|     | ΔAccuracy ΔPrecision | ΔRecall ΔF1-Score |     |     |     |
| --- | -------------------- | ----------------- | --- | --- | --- |
Method
SCSAPCA
| (𝛼=0.99) | -0.0542 -0.4799 | 3.0000 0.4600 |     |     |     |
| -------- | --------------- | ------------- | --- | --- | --- |
SCSKMEANS
(𝛼=0.99)
|     | -0.0518 -0.3990 | 3.7135 0.6957 |     |     |     |
| --- | --------------- | ------------- | --- | --- | --- |
MACSMulti-Scale
| (𝛼=0.99) | -0.0542 -0.4799 | 3.0000 0.4600 |     |     |     |
| -------- | --------------- | ------------- | --- | --- | --- |
SCSAPCA
(𝛼=0.95)
|     | -0.0772 -0.5286 | 3.8573 0.4200 |     |     |     |
| --- | --------------- | ------------- | --- | --- | --- |
SCSKMEANS
| (𝛼=0.95) | -0.0933 -0.5981 | 3.7135 0.2436 |     |     |     |
| -------- | --------------- | ------------- | --- | --- | --- |
MACSMulti-Scale
(𝛼=0.95)
|     | -0.0772 -0.5286 | 3.8573 0.4200 |     |     |     |
| --- | --------------- | ------------- | --- | --- | --- |
MSLdatasetresult
GCPdatasetdistribution
|     |     |     | Method | ΔAccuracy ΔPrecision | ΔRecall ΔF1-Score |
| --- | --- | --- | ------ | -------------------- | ----------------- |
SCSAPCA
|     |     |     | (𝛼=0.99) | -0.0710 -0.0070 | 8.0741 4.2980 |
| --- | --- | --- | -------- | --------------- | ------------- |
SCSKMEANS
(𝛼=0.99)
|     |     |     |     | 0.0005 0.2847 | 0.3333 0.3283 |
| --- | --- | --- | --- | ------------- | ------------- |
MACSMulti-Scale
|     |     |     | (𝛼=0.99) | -0.0710 -0.0070 | 8.0741 4.2980 |
| --- | --- | --- | -------- | --------------- | ------------- |
SCSAPCA
(𝛼=0.95)
|     |     |     |     | -0.1109 -0.0685 | 11.5556 5.0101 |
| --- | --- | --- | --- | --------------- | -------------- |
SCSKMEANS
|     |     |     | (𝛼=0.95) | -0.0106 0.2276 | 1.9352 1.6061 |
| --- | --- | --- | -------- | -------------- | ------------- |
MACSMulti-Scale
(𝛼=0.95)
|     |     |     |     | -0.1084 -0.0633 | 11.3611 4.9848 |
| --- | --- | --- | --- | --------------- | -------------- |
GCPdatasetresult
SMDdatasetdistribution
| Method | ΔAccuracy ΔPrecision | ΔRecall ΔF1-Score |     |     |     |
| ------ | -------------------- | ----------------- | --- | --- | --- |
SCSAPCA
(𝛼=0.99)
|     | -0.0463 0.0585 | 6.5054 4.8418 |     |     |     |
| --- | -------------- | ------------- | --- | --- | --- |
SCSKMEANS
| (𝛼=0.99) | -0.0073 0.2319 | 1.7527 1.6045 |     |     |     |
| -------- | -------------- | ------------- | --- | --- | --- |
MACSMulti-Scale
(𝛼=0.99)
|     | -0.0463 0.0585 | 6.5054 4.8418 |     |     |     |
| --- | -------------- | ------------- | --- | --- | --- |
SCSAPCA
| (𝛼=0.95) | -0.0923 0.0654 | 13.0645 7.9435 |     |     |     |
| -------- | -------------- | -------------- | --- | --- | --- |
SCSKMEANS
(𝛼=0.95)
|     | -0.0193 0.2723 | 4.2473 3.5819 |     |     |     |
| --- | -------------- | ------------- | --- | --- | --- |
MACSMulti-Scale
| (𝛼=0.95)               | -0.0923 0.0654 | 13.0645 7.9435 |                  |     |     |
| ---------------------- | -------------- | -------------- | ---------------- | --- | --- |
| MSLdatasetdistribution |                |                | SMDdatasetresult |     |     |
14

AIAT2025,December04–06,2025,Kyoto,Japan LiandGautam
Method ΔAccuracy ΔPrecision ΔRecall ΔF1-Score CPUdatasetresult
SCSAPCA
(𝛼=0.99) -0.0594 0.4030 9.2152 3.5938 Method ΔAccuracy ΔPrecision ΔRecall ΔF1-Score
SCSKMEANS SCSAPCA
(𝛼=0.99) -0.0146 0.4848 2.8481 1.9297 (𝛼=0.99) -0.0538 -0.4667 2.5971 1.1456
MACSMulti-Scale SCSKMEANS
(𝛼=0.99) -0.0596 0.3576 8.8734 3.4453 (𝛼=0.99) -0.0110 -0.5353 -0.0777 -0.1758
SCSAPCA MACSMulti-Scale
(𝛼=0.95) -0.1199 0.3758 17.7342 4.4297 (𝛼=0.99) -0.0522 -0.4796 2.3932 1.0549
SCSKMEANS SCSAPCA
(𝛼=0.95) -0.0376 0.5091 6.5823 3.2500 (𝛼=0.95) -0.1084 -0.4867 5.4903 1.7335
MACSMulti-Scale SCSKMEANS
(𝛼=0.95) -0.1198 0.3455 17.2785 4.3125 (𝛼=0.95) -0.0279 -0.5495 0.7039 0.2802
MACSMulti-Scale
CPUdatasetdistribution (𝛼=0.95) -0.1064 -0.4913 5.3155 1.6923
15