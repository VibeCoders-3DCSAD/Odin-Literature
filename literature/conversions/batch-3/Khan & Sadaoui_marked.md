---
conversion_metadata:
  converted_at: "2026-07-21T13:46:16Z"
  converter_tool: "markitdown"
  converter_version: "0.1.6"
  source_pdf: "Khan & Sadaoui.pdf"
  source_pdf_sha256: "5e3387cc498c2c931ef4f84afe83bf346ee928a326e892c174f861d0ba30f64a"
  page_count: 29
  markdown_char_count: 153320
---

<!-- PAGE-AWARE EXTRACTION (via pdfminer.six) -->

<!-- PAGE 1 -->

6
2
0
2

n
u
J

8
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
6
1
2
0
2
.
6
0
6
2
:
v
i
X
r
a

Learner-based Concept Drift Detection:
Analysis and Evaluation

Md Moman Ul Haque Khan and Samira Sadaoui

Department of Computer Science, University of Regina, Canada
MdMomanUlHaque.Khan@uregina.ca,
Samira.Sadaoui@uregina.ca

Contents

1 Introduction

2 Characteristics of Concept Drift

2.1 Formal Definitions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
2.2 Types of Drifts . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
2.3 Transitions of Drifts

3 Concept Drift Detection

3.1 Active vs. Passive Detection . . . . . . . . . . . . . . . . . . . . . . . . . .
3.2 Learner-based vs. Distribution-based Detection . . . . . . . . . . . . . . .
3.3 Learner-based Detectors . . . . . . . . . . . . . . . . . . . . . . . . . . . .
3.4 A Summary . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

3

4
4
5
5

6
6
7
8
9

4 SPC-based Detection

9
4.1 EDDM . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 10
4.2 FHDDM . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 10
4.3 RDDM . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 11
4.4 EWMA . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 11
4.5 FTDD . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 11

5 Window-Based Detection

12
5.1 ADWIN . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 12
5.2 KSWIN . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 13
5.3 MDDM . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 13
5.4 FPDD . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 14
5.5 WSTD . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 14

1

---

<!-- PAGE 2 -->

5.6 D3 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 15

6 Ensemble-based Detection

15
6.1 AWE . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 16
6.2 AUE . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 16
6.3 ARF . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 17
6.4 DWM . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 17

7 Experiments Setup

18
7.1
Implementation Frameworks . . . . . . . . . . . . . . . . . . . . . . . . . . 18
7.2 Streaming Datasets . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 19

8 Comparison of SPC-based Detectors

9 Comparison of Window-based Detectors

10 Comparison of Ensemble-based Detectors

11 A Summary

12 Conclusions

19

20

21

22

23

Abstract: Machine learning algorithms deployed for evolving streaming environments
must handle the non-stationary data distributions, commonly referred to as concept
drift. The presence of concept drift poses a major challenge for many real-world ap-
plications because it can severely degrade their predictive performance, hindering their
ability to support robust decision-making. Consequently, the timely and efficient detec-
tion of drift events is critical for sustaining high accuracy over time. This study examines
theoretically the concept drift characteristics and numerous drift detection algorithms
across several categories. Furthermore, we evaluate their performance on both synthetic
and real-world datasets exhibiting diverse streaming scenarios and drift characteristics,
such as abrupt and gradual changes. This study aims to enhance understanding of the
complex notion of concept drift characteristics and behavior of drift detectors, along
with their applicability to diverse contexts.

Keywords:

Concept drift types, Transition speeds, Sudden and gradual drifts,
Concept drift detection, Learner-based detection, SPC methods, Windowing methods,
Ensemble methods, Synthetic stream datasets, Implementation frameworks.

2

---

<!-- PAGE 3 -->

1 Introduction

Nowadays, most applications evolve over time, such as fraud detection, network in-
trusion, health monitoring, financial markets, predictive maintenance and environment
monitoring. For example, in e-payment systems, fraudsters often devise new strategies
to manipulate the system’s vulnerabilities, and legitimate buyers adopt new payment
methods (e.g., using new mobile wallets) [36, 10]. Regarding the environment monitor-
ing systems, sensors can result in shifts due to new pollution causes [60, 38]. Health
monitoring devices may also encounter drift because a patient’s lifestyle, age and health
status (health is improving or deteriorating) change over time [34]. Industrial equipment
also experiences drift as it ages and degrades, and monitoring models must detect fail-
ures early [55, 40]. These non-stationary applications process an influx of data produced
non-stop, often quickly, and where data can shift unpredictably. These changes lead to
a divergence between training and operational data-distributions over time [2, 27]. Such
changes in the class distribution and/or feature distribution, known as concept drift [24],
often degrade the performance of predictive models [24]. Indeed, ML models trained on
old data patterns become invalid and obsolete, leading to poor performance and false
alarms.

Concept drift occurs when the statistical properties of the incoming data change or
the relationships between the independent variables (features) and target variable (class
label) change. The evolving data-generating environments present memory and compu-
tational challenges, making it critical to develop adaptive algorithms that can effectively
address them [27]: 1) Data arrives at high speed, necessitating algorithms with fast data
and drift analyzing capabilities, and 2) Data are continuous, making it impractical to
store all the data, which requires algorithms to process each sample individually, or select
the most relevant data or summarize data on the fly. For each specific application, the
model developers must anticipate possible changes in future data and choose the most
effective strategies to adapt ML models to real-time changes in data properties, such as
discarding outdated knowledge and retraining the models on the adjusted feature space.

Our study provides a comprehensive survey of concept drift within the supervised
learning setting, with a particular focus on data stream classification. To support a
clearer understanding of the complex nature of concept drift, we first examine its key
characteristics through several concrete examples, including different drift types, such
as real and virtual drift, as well as different rates of change, such as abrupt, gradual,
incremental and recurring drift. The focus is placed on learner-based drift detection
methods, which are the most widely studied and applied approaches. These methods
typically monitor the behavior or performance of a learning model over time in order to
identify significant changes that may indicate the presence of drift. We outline a general
algorithmic framework for learner-based detection and examine its main categories: Sta-
tistical Control Process (SPC), Window-based and Ensemble-based. For each category,
we review a selection of representative drift detectors (with a tally of 15 methods).

In addition to the survey part, we conduct a thorough empirical evaluation of the
reviewed methods on several synthetic (under gradual and sudden drifts) and real-world

3

---

<!-- PAGE 4 -->

data streams. We choose artificial datasets because the drift locations are known a apri-
ori, which allows for a more precise assessment of each method’s ability to detect both
sudden and gradual drifts. We also consider real-world datasets to evaluate the practical
behavior of the methods under realistic conditions, where drifts may be noisy or difficult
to identify. By combining a robust review with an extensive experimental evaluation
and comparison, our study aims to provide researchers with a clearer and more practical
understanding of learner-based detection methods.

The remainder of the paper is structured as follows. Section 2 presents the formal
definitions of concept drift and discusses its main characteristics using real-world exam-
ples. Section 3 examines different classifications of drift detection methods, including
active vs. passive, online vs. block, learner-based vs. distribution-based, and SPC-
based vs. window-based vs. ensemble-based. Sections 4, 5 and 6 present the theoretical
foundations of SPC-, window- and ensemble-based detectors, respectively. Section 7
describes the existing implementation frameworks for these various methods and also
introduces the stream datasets used in the experimental evaluation. Sections 8, 9, 10
and 11 evaluate and compare the performance of SPC-, window- and ensemble-based
methods. Section 12 concludes our work.

2 Characteristics of Concept Drift

2.1 Formal Definitions

Concept drift occurs when learning from dynamic data streams, defined as continuous
and limitless sequence of samples, [(X0, y0), ...., (Xi, yi)], where X is a multi-dimensional
feature vector with a corresponding label y [54]. The Bayes’ decision theorem allows to
compute the probability that X is an instance of class y [17]:

P (y|X) =

P (X|y)P (y)
P (X)

Here, P (X|y) denotes the likelihood of the input features given the target label, P (y)
is the prior probability distribution of the output variable, and P (X) is the uncondi-
tional probability distribution of the input features. In predictive modeling, a concept
refers to the specific joint probability of input features and target class, P (X, y), which
encompasses the prior class probability P (y) and class-conditional probability P (X|y)
as follows [15, 27]: P (X, y) = P (y)P (X|y)

Concept drift can be defined as a change in the joint probability distribution between
two distinct time steps t and t + w. Here, t represents a specific point or interval in
time, and w denotes the window over which the change in data distribution has been
identified [15, 27]. So, concept drift occurs when Pt(X, y) ̸= Pt+w(X, y) [15, 27].

4

---

<!-- PAGE 5 -->

2.2 Types of Drifts

The types of drift are categorized based on the aspects of the probability distribution
that is changing.

A. Real Drift: Known as actual or true drift, this type occurs when there a change
in the posterior probability P (y|X), which can affect the decision boundary of ML
models. This drift can be a result of changes in the class distribution P (y) and likelihood
It indicates a fundamental change in the concept the model is
distribution P (X|y).
trying to predict, which over time renders the model less effective [15, 27]: Pt(y|X) ̸=
Pt+w(y|X).

An example: We assume we have a model that predicts the likelihood of an illness
based on the symptoms observed (X). In this case, real drift refers to changes in the
conditional probability of the illnesses given the symptoms, i.e. P (Disease|X). For
instance, the changes are due to an update in medical knowledge or emergence of new
illness strains.

B. Virtual Drift: Known as covariate drift, this type refers to changes in the feature-
value distribution P (X), without altering the relationship between the input features
and the label i.e., P (y|X). With this type, the model might encounter samples that are
underrepresented or differ from those in the training dataset, leading to accuracy issues
[15, 27]: Pt(X) ̸= Pt+w(X).

An example: In predicting weather conditions, suppose the model was trained with
data from the autumn season. If the model starts receiving data from winter (without
any change in P (W eather|X)), this would be an instance of virtual drift.

C. Mixed Drift: Both real and virtual drifts can happen simultaneously in real-world
scenarios, involving changes in both the prior probability of classes and probability of
features [61, 59]: Pt(y|X) ̸= Pt+w(y|X) and Pt(X) ̸= Pt+w(X).

An example: In credit card fraud detection, we usually encounter real and virtual
shifts, such as the consumer’s spending habits change during the holiday season (real
drift) and fraudsters change their tactic strategies (virtual drift).

2.3 Transitions of Drifts

Transitions represent the speed of change from the old concept to the new one. They
can be quantified by the number of samples over which the drift occurs until the new
concept is established. These transitions are essential for understanding how to adapt
the decision models to maintain accuracy as data evolves. There are four transition
types [17, 35], and for each type, concrete examples are provided based on studies such
as [15, 36, 35].

• A. Sudden Drift: Occurs when the data distribution changes abruptly from the
old concept to a new one at a precise timestamp, which degrades instantly the
decision models. Abrupt drifts that can drastically impact the learned models.

5

---

<!-- PAGE 6 -->

Examples: 1) A sudden change in consumer behavior due to unexpected events,
like the COVID-19 pandemic and new market regulations, 2) a quick equipment
failure or 3) unforeseen weather conditions.

• B. Gradual Drift: Happens when the data patterns change progressively from
the previous concept to the new one. This type shows a longer transition phase
that involves a mixture of the old and new concepts. The new concept becomes
more predominant over time.

Examples: 1) User preferences for a particular service or product can change
slowly due to evolving trends, 2) the quality of machinery can degrade slowly
over time, and 3) a patient’s health may gradually change due to aging or the
progression of a medical condition over the years.

• C. Incremental Drift: Occurs when the current concept replaces the past con-
cept slowly, by involving intermediate concepts (may not be statistically signifi-
cant). Some researchers consider incremental drift as a variant of gradual drift,
however, what sets incremental drift apart from gradual drift is the absence of a
distinct boundary that separates the old and new concepts.

Examples: 1) The slow change in climate patterns (like in temperatures and
rainfalls) progressively affect agricultural products, and 2) fraudsters in e-payment
systems gradually adopt new tactics by shifting from simple techniques (like stolen
credit cards) to modern ones (like virtual cards and bots).

• D. Recurrent Drift: Happens when a concept that was encountered earlier
reappears after some time has passed. While this shares similarities with gradual
drift in that alteration of two concepts, the key distinction is that the old concept
reappears after some time interval in the recurring drift.

Examples: 1) Seasonal changes in spending behavior, such as increased purchases
during the holiday seasons, and 2) with the winter season comes health changes
due to people becoming less active and having higher heart rates.

3 Concept Drift Detection

3.1 Active vs. Passive Detection

Drift detection methods can be mainly categorized into two folds [23, 53]: active (with an
explicit drift detection mechanism) vs. passive (continuous model adaptation). Active or
informed detectors monitor data streams for drifts and activate some adaptation mecha-
nisms when drifts have occurred, reducing FP and FN rates and saving memory and CPU
resources [28, 4]. Recent examples of active detectors include: 1) probabilistic methods
that specifically identifies real drift [42] and [43], 2) a sum-product NN-based method
that detects both real and virtual drifts [41], and 3) a cross-entropy-based method that
identifies real drifts within noisy data streams [44] . On the other hand, passive meth-
ods continuously update their models with incoming samples without any drift detection

6

---

<!-- PAGE 7 -->

because they consider that drifts may occur constantly or periodically. These methods
can be handy in detecting gradual/incremental shifts, but they are time-consuming. An
example is the incremental feature learning approach introduced in [49] that continu-
ously adjusts a single NN model to new data chunks. The model is composed of several
interconnected sub-NNs, with a new sub-NN optimally created for each incoming chunk.
To prevent unbounded NN growth, only the sub-NNs most relevant to the new data
distribution are retained and re-combined to build the optimal model.

3.2 Learner-based vs. Distribution-based Detection

Drift detectors can also be broadly classified into three main categories: learner-based
(supervised), distribution-based (unsupervised) and hybrid. Each category has specific
advantages and disadvantages [35, 17, 57, 61], as explained below.

• Learner-based: These methods detect drifts by monitoring the performance of
the underlying classifiers, such as the error rates. They are further split into three
groups: Statistical Process Control (SPC), Windowing Techniques and Ensemble
Learning. The pros of these methods are: 1) Directly linked to the predictive
performance of the base models, which makes them intuitive and easy to interpret,
and 2) Effective in scenarios where the drifts directly impact the model accuracy.
Their cons are: 1) May not detect drifts that do not immediately affect model
performance, such as changes in features, 2) Require data to be labeled, and 3)
Can be sensitive to noise and random fluctuations in data.

• Distribution-based: These methods monitor changes in the data distribution
itself over different timestamps to check whether the current and historical data
windows come from the same distribution or not. They often use statistical tests
(like Kullback-Leibler divergence and Kolmogorov-Smirnov Test) to determine if
the data distribution has changed significantly. Their pros are: 1) Detect drifts
that do not immediately affect model performance, 2) Often more robust to noise
in data, and 3) Do not require data to be labeled. On the other hand, their cons
are: 1) May require a large amount of data to detect drifts accurately, 2) More
prone to false alarms, and 3) Can be computationally intensive due to continuous
statistical testing.

• Hybrid: Hybrid detectors combine elements of learner and distribution-based
methods to leverage the strengths of both methods and provide more robust drift
detection mechanisms. Their pros are: 1) Potentially more robust and versatile
in different scenarios, and 2) Can dynamically switch between performance and
distribution-based detection based on the context. Their cons are : 1) Can be
more complex to implement and tune, and 2) May incur higher computational
costs due to the dual nature of detection.

7

---

<!-- PAGE 8 -->

3.3 Learner-based Detectors

This category explicitly manages drift by incorporating mechanisms to forget old data
and retrain or adjust the underlying models to the newly detected concept. To distin-
guish drift from noise, the new concept must remain stable for some time [15]. The
detectors are usually designed to be independent of specific ML algorithms, as they can
adopt various types of learners. The general form of the learner-based detection meth-
ods is summarized in Algorithm 1 using the prequential training scheme (test and then
train). The algorithm is online, so that the drift is identified in real time. The selected
classifier is first pre-trained on an initial robust labeled dateset. The classifier then re-
ceives sequentially and continuously a stream of samples and predicts their labels. Next,
it uses a statistical test method to detect a drift by comparing a drift metric to a prede-
fined statistical threshold. For example, when the error rate (the discrepancy between
predicted and true labels) increases significantly, this determines a drift. Other examples
would be comparing past accuracy or prediction probability (confidence score) with the
accuracy or probability on the new data. Some detectors use a warning threshold to
signal an impending drift and monitor the samples more closely.

Once a significant change is detected, the classifier retrains on recent data, typically
stored in a sliding window or buffer. When the buffer reaches the limit, it forgets old
data. Other methods select the most representative samples from the buffer or use all
the samples but the new data have higher weights so that the detection model focuses
less on old data [2].

Algorithm 1 General Algorithm for Learner-based Drift Detection

1: Inputs: classier,

intialDataset, dataStream (continous), statThreshold, RDSize

(sliding window size)

2: Pre-train classifier with intialDataset
3: recentData ← empty /*window of recent data*/
4: for each newSample in dataStream do
Add newSample to recentData
5:
if (length of recentData > RDSize) then
Remove oldest sample from recentData

6:

7:

8:

9:

10:

11:

12:

13:

14:

end if
Predict sample’s label with classifier
Calculate driftMetric on prediction
if (driftMetric > statThreshold) /*significant difference*/ then

Display ”Drift Detected”
Train classifier on recentData with ground truth
recentData ← empty

end if

15:
16: end for

8

---

<!-- PAGE 9 -->

3.4 A Summary

Table 3.1 compares numerous detectors (those selected for the experiments) based on
their strategies: (1) Active (with an explicit drift detection mechanism) vs. Passive (con-
tinuous model adaptation), (2) Online (processes each sample once and then discarded
it) vs. Block-based (processes a data chunk at once), and (3) types of learner-based
methods: SPC, Window techniques and Ensemble methods.

Method
FTDD [14]
RDDM [7]
FHDDM [46]
EWMA [48]
EDDM [5]
KSWIN [47]
FPDD [14]
WSTD [6]
MDDM [45]
ADWIN [12]
D3 [20]
ARF [19]
AUE [13]
DWM [30]
AWE [56]

Year Passive vs Active Online vs Block Category
2018
2017
2016
2012
2006
2020
2018
2018
2018
2007
2015
2017
2011
2007
2003

Online
Online
Online
Online
Online
Online
Online
Online
Online
Online
Online
Online
Block-based
Online
Block-based

SPC
SPC
SPC
SPC
SPC
Window
Window
Window
Window
Window
Window
Ensemble
Ensemble
Ensemble
Ensemble

Active
Active
Active
Active
Active
Active
Active
Active
Active
Active
Active
Passive
Passive
Active
Active

Table 3.1: A Summary of Learner-based Drift Detection Algorithms

4 SPC-based Detection

SPC detectors treat a model’s performance as a controlled process [15, 39]. They employ
statistical tests to detect deviations from expected behavior or exceedance of predefined
control limits. By monitoring the evolution of a model’s performance, SPCs assess the
quality of the learning process [15, 39]. When performance deteriorates or crosses a
statistically significant threshold, it indicates concept drift. In such cases, SPCs may
trigger classifier retraining or apply alternative strategies to address the drift. This
approach enables real-time monitoring and facilitates prompt responses to changes in
the underlying data. There are different SPC procedures, such as those defined in DDM,
EDDM, RDDM, FHDDM, KAPPA, EWMA, STEPD, FTDD and ACDDM. We describe
the most popular methods in the following sections.

9

---

<!-- PAGE 10 -->

4.1 EDDM

Early Drift Detection Method (EDDM) [5] is an improvement of the DDM [18], designed
to better detect gradual (moderate) changes. Instead of considering the number of errors
as in DDM, EDDM focuses on the distance between two successive errors. At timestamp
t, EDDM calculates [5]:

• pt, which is the average distance between two consecutive errors at time t
• σt, which is the standard deviation of the distances at time t
• pmax and σmax, which track the maximum observed performance and take the

values of pt and σt when (pt + 2σt) reaches its historical maximum value

The study [5] defines the warning and drift levels using α as the threshold for the

warning zone and β as the threshold for the drift zone:

• Warning level: (pt + 2σt)/(pmax + 2σmax) < α, indicating a possible change
• Drift level: (pt + 2σt)/(pmax + 2σmax) < β, signaling a confirmed drift

The paper [5] recommends setting α and β to 0.95 and 0.90 respectively. When the
warning level is detected, the samples are stored in preparation for drift localization.
When the drift level is reached, the classifier along with pmax and σmax are reset. In this
case, the model can use the data collected in the warning zone together with recent post-
drift data to train or update the model. When changes occur gradually at a moderate
pace, EDDM is a better option than DDM. However, DDM is a better option when
dealing with sudden changes. The limitation of EDDM can be pointed out as it is noise
sensitive, which makes it more prone to false positives [39].

4.2 FHDDM

Fast Hoeffding Drift Detection Method (FHDDM) [46] uses the Hoeffding inequality [26]
to detect changes in data streams. It continuously monitors the prediction errors and
uses the Hoeffding bound to determine whether the error rate has increased significantly
or not. FHDDM computes the mean error in this window and compares it with the
minimum error observed so far, and uses the following Hoeffding inequality:

p(| ¯X − µ| ≥ ϵ) ≤ 2e−2nϵ2

where ¯X is the average of the error rates of the current window, µ is the minimum
error rate assuming no drift, n is the size of the sliding window, and ϵ is the acceptable
deviation from the minimum error rate. The method flags a drift when the deviation
| ¯X − µ| is large enough, i.e. greater than or equal to the calculated threshold ϵ, derived
from the Hoeffding bound.

10

---

<!-- PAGE 11 -->

4.3 RDDM

Reactive Drift Detection Method (RDDM) enhances DDM by dynamically adjusting
the detection threshold based on recent error rates [3, 9]. RDDM utilizes the following
strategy, based on the calculated error rate and standard deviation [9]:

• Warning level: pt + σt ≥ pmin + (2 ∗ σmin), for a possible drift; pmin is the historical

minimum error rate and σmin is the standard deviation of pmin

• Drift level: pt + σt ≥ pmin + (3 ∗ σmin), for a detected drift

RDDM continuously recalculates warning and drift statistics, discarding outdated
samples and focusing on recent ones. It identifies concepts that remain active for an
extended period or with a long warning window. This adaptability allows to effectively
identify both sudden and gradual drifts while minimizing false alarms [6, 53]. Compared
to DDM, RDDM achieves higher accuracy in most scenarios, particularly for gradual
drifts, by detecting more drifts and identifying them earlier. However, its increased
complexity and parameter sensitivity may require careful calibration for optimal perfor-
mance in specific applications [15].

4.4 EWMA

The exponentially weighted moving average (EWMA) was proposed in [48]. EWMA for
drift detection is a statistical process that identifies drift by monitoring the error rate of
a streaming classifier [8, 14].The standard deviation of the EWMA estimator zt is [35]:

(cid:114)

p0(1 − p0)

σ2
zt =

λ
2 − λ

(1 − (1 − λ)2t)

Here, zt = (1 − λ)zt−1 + λxt, p0 is the baseline error rate under no-drift conditions,

and λ is a smoothing parameter.

According to EWMA, drift is detected if [15]: zt > µ0 + Lσzt. Here, L is the control
limit, which states the distance zt must deviate from µ0 before a change is flagged. Set-
ting the appropriate smoothing factor (λ) is crucial for achieving optimal performance.
λ = 0.2 has been suggested by [35]. A high λ value increases sensitivity to recent changes
but may make the method susceptible to noise. A low λ value can lead to delayed drift
detection[48]. The main advantage of EWMA is its ability to detect gradual and abrupt
drifts [3]. It is also computationally efficient, with an overhead of O(1) [48].

4.5 FTDD

The Fisher Test Drift Detector (FTDD) is one of three drift detection algorithms pro-
posed by [14], based on an efficient implementation of Fisher’s Exact Test [16]. FTDD
is based on the Sequential Testing with Estimation of Proportion Difference (STEPD)
algorithm [39], but addresses its limitations when dealing with imbalanced data [51]
Unlike STEPD, which uses a test of equal proportions, FTDD employs Fisher’s Exact

11

---

<!-- PAGE 12 -->

test in all comparisons to detect concept drift [6, 8, 15]. The pvalue calculation is a key
feature of FTDD, contributing to its effectiveness in accurately detecting drifts [14]:

p value =

|wr+wp|
|wr|
|wp|

|cr+cp|
|cr|
|cp|

×

p value = p value × constF × 2

Where wr is the number of errors in the recent window, wp is the proportionally
calculated number of errors in past window, cr is the number of correct predictions in
the recent window, cp is the proportionally calculated number of correct predictions in
past window. constF is a constant factor derived from the factorial calculations for the
window size (w). It helps to optimize the p value computation by pre-calculating and
storing a common factor. Here, the probability of observing the specific distribution
of errors and correct predictions in the two windows (recent and past) is calculated
given the assumption that no drift has occurred [14]. The warning is triggered when the
p value falls below the threshold αw = 0.005 and a drift is confirmed when the pvalue is
typically less than αd = 0.003.

5 Window-Based Detection

Windowing detectors handle drifts by monitoring the model performance or other sta-
tistical measures over two data windows (of a fixed or dynamic size) and checking for
significant discrepancies between them [15, 51]. They treat the classifier’s prediction
results as the data stream. They assess the chosen metric on each window and flag drift
when the difference exceeds a predefined threshold or a threshold derived from a statisti-
cal test [15, 51]. The dynamic windowing technique adjusts the size based on the drift’s
length, retaining samples until the drift occurs. It allows for flexibility without the need
to set a predefined window size, which is a difficult task. The decision for window size
is crucial because large windows can increase accuracy but may miss the detection of
rapid drifts, and small windows are more effective in detecting sudden drifts but might
not capture gradual changes. There are different windowing strategies, as described in
the following selected methods: ADWIN, KSWIN, MDDM, FPDD, WSTD and D3.

5.1 ADWIN

ADaptive WINdowing (ADWIN) [12] maintains a sliding window w containing the most
recent errors and tests, after every new instance, whether the average error in an older
window wp differs significantly from that in a newer window wr. ADWIN detects drift
by comparing the mean error rates (µwp for wp, µwr for wr) of the two sub-windows. A
drift is signaled when the difference in error rates exceeds a threshold derived from the
Hoeffding bound [51, 15]: |µwp − µwr | > ϵ, where ϵ is the threshold calculated based on
the Hoeffding bound [12]:

12

---

<!-- PAGE 13 -->

(cid:114)

ϵ =

1
2m

ln(

4|W |
δ

)

Where m is the harmonic mean of the lengths of sub-windows wr and wp, |w| is the
length of the entire window w, δ is a predefined confidence parameter, and ln() is the
natural logarithm. ADWIN has been shown to be effective in detecting both abrupt and
gradual concept drifts [1].

5.2 KSWIN

Kolmogorov–Smirnov Windowing (KSWIN) [47] maintains two sliding windows of error
observations, an older window, wp, and a recent window, wr [44, 40]. After each new
prediction, the sup-norm KS (Kolmogorov–Smirnov) distance, dist(wr, wc) is computed
for sample x, where sup-norm distance is the maximum point-wise gap between two
functions, making it highly sensitive to even a single large deviation and thus effective
for detecting distribution changes [47]:

dist(wp, wr) = sup|fwp(x) − fwr (x)|

Here, f (x) = 1
n

(cid:80)n

i=1 I(−∞,x)(xi) and I(−∞,x)(xi) is an indicator function.

A drift is signaled by KSWIN when the calculated distance exceeds a threshold defined

by the formula below [44, 47]:

dist(wp, wr) >

(cid:114)

−

ln(α)
n

Where α is the significance level representing the probability of incorrectly rejecting
the null hypothesis. Common values for α are 0.05, 0.01, or even smaller depending on
the desired level of confidence, and n is the size of the two sub-windows [47].

5.3 MDDM

McDiarmid Drift Detection Method (MDDM) [45] uses the McDiarmid’s inequality intro-
duced in [37]. MDDM operates under the assumption that in a streaming environment,
recent samples are more relevant than older ones. To reflect this, MDDM uses a sliding
window with a weighting scheme that prioritizes the most recent samples [45]. MDDM
slides a window of size n over the prediction results [22]. This window stores binary
values, where 1 represents an incorrect prediction and 0 represents a correct prediction
[15]. Each element in the window is associated with a weight, where wi < wi+1. While
inputs are processed, the current weighted average of the elements of the window is cal-
culated, i.e. µt, as well as the maximum weighted mean observed so far, i.e. µm. When
µm < µt then µm = µt [51, 45]. Hence, with MDDM, concept drif is declared when [45]:

(µm − µt) ≥ ϵ

13

---

<!-- PAGE 14 -->

where ϵ is the threshold calculated with the McDiarmid’s inequality:

ϵ =

(cid:114) (cid:80)n

i=1 v2
i
2

∗ ln(

1
δ

)

Here, δ is the confidence level, and vi is the weight of the i-th element, calculated as:

vi = wi
(cid:80)n

i=1 wi

[45].

5.4 FPDD

The Fisher Proportions Drift Detector (FPDD)[14] is designed to enhance the perfor-
mance of the Statistical Test of Equal Proportions(STEPD), particularly when dealing
with small sample sizes [15]. It leverages Fisher’s Exact Test to provide a more robust
statistical analysis in these scenarios [8]. This leads to more accurate drift detection
when drifts occur rapidly. Similar to STEPD, FPDD compares two windows, the recent
window (wr) and past window (wp), to analyze the data stream.

The core distinction of FPDD lies in its conditional application of Fisher’s Exact
Test. Suppose the number of errors or correct predictions in either of the two windows
is smaller than five. In this case, FPDD uses Fisher’s Exact Test to assess the statistical
significance of the difference in error rates between the two windows. In cases where
the sample sizes are sufficient(5 or more), FPDD reverts to the standard test of equal
proportions used by STEPD[51]. Based on the chosen statistical test (Fisher’s Exact
Test or the test of equal proportions), FPDD calculates the p value (as computed in
section 4.5), and uses it as follows [14]:

• Drift detected: if p value ≤ αd

• Warning signal: if αd < p value ≤ αw

FPDD uses two similar threshold parameters like STEPD, the significance levels for

the detection of drifts ( αd = 0.003 ) and warning ( αw = 0.05 ).

5.5 WSTD

Wilcoxon Rank Sum Test Drift Detector (WSTD) [7], which closely resembles STEPD,
detects drifts based on an efficient implementation of the Wilcoxon rank sum statistical
test [58], whereas STEPD uses the test of equal proportions [6, 23]. WSTD requires
setting a significance level (α) and applies the normal distribution to evaluate the null
hypothesis. Given two sample set, n1 and n2, they are combined in the ascending order
as below [7]:

• Test statistic is z = (R−µR)
• Population mean is µR = n1 × (n1+n2+1)
• Standard deviation is σR =

(cid:113)

σR

2

n1 × n2 × (n1+n2+1)

12

14

---

<!-- PAGE 15 -->

where R is the smallest sum of the ranks of both sample sets, n1 is the size of the
smallest sample set, and n2 is the size of the largest sample set. The z value is used to
reject the null hypothesis, and the p value (or obtained probability) is also required to
find the z value [3, 7].

Similar to STEPD, WSTD monitors the base learner’s predictions using two windows:
a recent window and an older one. It relies on a statistical test to issue warnings or
confirm drifts. WSTD incorporates three key parameters with default values: the recent
window size (w = 30), the significance level for drift detection (αd = 0.003), and the
significance level for warnings (αw = 0.05) [7].

5.6 D3

Discriminative Drift Detector (D3) [20] detects changes by comparing recent and his-
torical samples. D3 operates on the principle that a change in the underlying data
distribution P (X) will manifest as a difference between recent and historical data. By
training a classifier to distinguish between these sets, D3 can detect drifts when the
classifier performs well, which suggests that the data distributions have diverged. D3
employs a sliding window, denoted as W , to store the most recent samples. The size of
this window is determined by w(1 + ρ), where [20]:

• w is the number of ”old” samples, which correspond to the historical data
• ρ is the fraction of ”new” samples, relative to the size of the old data. This

essentially controls the size of the new dataset within the window

A drift is signaled when the classifier AUC score (trained to distinguish between the
old and new sample) is greater than or equal to the threshold, θ, which is typically set
between 0.5 and 1.0 [50, 20]. The performance of D3 can vary significantly based on the
specific classifier and dataset being used [25]. Additionally, the method’s capability is
constrained to identifying only linear drift patterns within the feature space [21].

6 Ensemble-based Detection

Ensemble-based detectors are a robust approach to handling drifts because combining
the outputs of several learners is more effective to changing data patterns. Many such
detectors adopt the Weighted Majority Algorithm (WMA). The ensemble remains up
to date with new concepts as follows [15, 1]: (1) a new classifier trained on the current
data is added to the ensemble, (2) the learners are then weighted according to their
performance with the current data, and (3) the least-weighted learners, deemed less
effective, are removed from the ensemble. In addition to adding/removing learners, the
ensemble may use incremental learning to adapt the learners. The ensemble approach
is efficient in identifying gradual drifts while maintaining high levels of accuracy [15, 1],
but comes with high computational and memory costs. There are numerous ensemble-
based detectors, which can be categorized as follows: (1) methods that implement their
own detection mechanisms, such as AWE, AUE, ACE and DWM, and (2) methods that

15

---

<!-- PAGE 16 -->

utilize an existing detector, such as ADWIN, which is used in algorithms like ARF. We
describe these methods in the following sections.

6.1 AWE

Accuracy Weighted Ensemble (AWE) [56] selects the most efficient classifiers using the
mean squared error (MSE), which is calculated based on the probabilities of class as-
signments. AWE identifies the top n classifiers based on their performance on the most
recent data chunk [56]. It employs MSE for assigning weights: classifiers that exhibit an
error rate meeting or exceeding a certain threshold are excluded. This method ensures
that only the classifiers most aligned with the current data patterns are retained, thereby
enhancing the ensemble’s overall accuracy. The weight (wi) assigned to a classifier ci is
calculated using the following formulas [15, 51, 30]:

wi = M SEr − M SEi

Here M SEr is the reference MSE calculated based on the class distribution of the

current data chunk Sn [56]:

M SEr =

(cid:88)

c

p(c)(1 − p(c))2

where p(c) is the probability of class c, which is estimated from the distribution of
classes in Sn. M SEi represents the error for the ith classifier, calculated over Sn as
follows [56]:

M SEi =

1
Sn

(cid:88)

(1 − pi

c(x))2

(x,c)ϵSn

where pi

c(x) is the probability that classifier i assigns sample x to class c.

6.2 AUE

Accuracy Updated Ensemble (AUE) [13], an advancement over AWE, updates only the
top k weighted classifiers that meet a certain accuracy threshold on the most recent data
block, rather than updating all classifiers. Additionally, AUE utilizes a more straight-
forward weighting function compared to AWE [51]. AUE incorporates online classifiers,
typically Very Fast Decision Trees (VFDT) or Hoeffding Trees, by updating them in-
dividually in addition to weight modifications. This adaptability ensures that in the
absence of drift across chunks, the classifiers enhance their performance as though they
were trained on a singular, extensive dataset [51]. Consequently, this flexibility permits
a reduction in chunk size without compromising the ensemble’s accuracy. The weighting
function employed in AUE is simplified as below[13]:

wi =

1
M SEi + ϵ

16

---

<!-- PAGE 17 -->

where M SEi is computed in the same manner as in AWE, and ϵ is a small constant
added to facilitate weighting calculations even when M SEi equals zero [13]. The en-
semble size in AUE is typically fixed to a predetermined number, k, of classifiers [51].
Comparative experimental studies have demonstrated that AUE outperforms AWE in
various datasets, except for one instance where both achieved comparable accuracy [13,
51].

6.3 ARF

The Adaptive Random Forest (ARF) algorithm [19] handles evolving data streams by
incorporating several key strategies. ARF extends the traditional random forest algo-
rithm to adapt to changes in the data distribution by replacing under-performing trees
with new ones [29, 35]. ARF uses Hoeffding Trees (HT) as its base learners, which are
a type of very fast decision tree. These trees are incrementally updated with each new
sample, making them suitable for streaming data [19, 13]. ARF employs a resampling
method based on online bagging [53]. Instead of growing each tree sequentially on dif-
ferent subsets of data, as in traditional random forests, ARF simulates sampling with
reposition using a Poisson distribution, specifically Poisson (λ = 6) [19]. ARF handles
concept drift through a combination of online bagging for resampling, drift detectors for
each tree, background training of new trees, and weighted majority voting. These mech-
anisms allow the model to maintain high accuracy when dealing with non-stationary
data streams[23].

6.4 DWM

The Dynamic Weighted Majority (DWM)[30] extends the weighted majority algorithm
[32] by dynamically adjusting the weights of its base classifiers and adding/removing
classifiers based on their performance [31]. DWM is a passive adaptation method that
does not use an explicit drift detection mechanism, but rather continuously adapts its
base learner [27]. This differentiates it from methods that explicitly monitor error rates
or other statistics to detect drift.

With DWM, weights are adjusted after each new classified sample. This online ap-

proach allows DWM to adapt to gradual changes more easily [15, 23]:

• If a base classifier predicts correctly, its weight is multiplicatively increased by a

factor β > 1 i.e., wi(t + 1) = β ∗ wi(t) [51]

• If a base classifier predicts incorrectly, its weight is decreased multiplicatively by

a factor α < 1 i.e., wi(t + 1) = α ∗ wi(t) [51]

where wi(t) is the weight of classifier i at time t, and wi(t + 1) is the updated weight

at time t + 1. Typical values for the parameters can be β = 1.1 and α = 0.9.

17

---

<!-- PAGE 18 -->

7 Experiments Setup

We utilize both artificial and real-world datasets from the Harvard Dataverse [33], under
abrupt and gradual scenarios, to assess the performance of drift detectors of different
categories. These datasets present distinct data characteristics, providing an extensive
testbed. When the drift is identified, the base learners, Naive Bayes and Hoeffding
Tree, are retrained with the most recent samples to ensure that predictions remain
accurate. We assess and compare these detector’s performance using the AUC metric.
AUC is useful for assessing performance degradation caused by drifts. For each detector’s
hyperparameters, we use their default values mentioned in earlier sections. In all the
experiments, we set the window size to 50 and the ensemble size to 15. In the empirical
tables, the best results are shown in red and the worst ones in blue.

7.1 Implementation Frameworks

Table 7.1 provides the implementation frameworks of the 15 selected drift detectors.
These frameworks support a broad collection of ML algorithms, such as classification,
regression, clustering and drift detection. Here, NA indicates that there was no publicly
available implementations found online. Therefore, we implemented the Python code
with the assistance from Github Copilot.

Table 7.1: Drift Detectors and their Implementation Frameworks

URL
Git (Fisher’s Exact Test
Tornado

FTDD [14]
RDDM [7]
FHDDM [46] River
EWMA [48]
EDDM [5]
KSWIN [47]
FPDD [14]
WSTD [6]
MDDM [45]
ADWIN [12]
ARF [19]
D3 [20]
AUE [13]
DWM [30]
AWE [56]

Tornado
River
River
Git (Fisher’s Exact Test)
NA
Tornado
River
River
Git
NA
Scikit-multiflow
Scikit-multiflow

18

---

<!-- PAGE 19 -->

7.2 Streaming Datasets

Our empirical study utilizes synthetic and real datasets, summarized in Table 7.2, to
evaluate the performance of various drift detectors. The six synthetic datasets (balanced
binary class label and without noise) have been produced using three main generators,
Random Tree Stream (RT), SINE and MIXED, by incorporating abrupt and gradual
drifts [33]:

• RT-abrupt and RT-gradual, with the arrangement of 8873985678962563

• Sine-abrupt and Sine-gradual, with the arrangement of 0123

• Mixed-abrupt and Mixed-gradual, with the arrangement of 0101

Each dataset possess four distinct concepts and three drift locations [33]. The sudden
datasets experience abrupt shifts at locations of 10,000, 20,000 and 30,000. The gradual
datasets undergo gradual transitions at locations of 9,500, 20,000 and 30,500, with each
transition having a drift width of 1,000 samples.

On the other hand, we employ two real datasets (balanced binary class label), as
presented in Table 7.2. The Electricity dataset ELEC2, collected from the Australian
New South Wales electricity market, predicts whether the prices (set every five minutes)
of electricity will increase or decrease [11]. The Intrusion Detection Evaluation dataset
CIC-IDS2017 contains network traffic collected for five days, from Monday, July 3, 2017,
at 9am to Friday, July 7, 2017, at 5pm [52].

Dataset Size
RTa
RTg
Sinea
Sineg
M ixeda
M ixedg
ELE
CIC

40,000
40,000
40,000
40,000
40,000
40,000
45,312
28,303

#Drifts
#Features-Modality
3 Abrupt
2-numerical
3 Gradual
2-numerical
3 Abrupt
2-numerical
3 Gradual
2-numerical
3 Abrupt
4-numerical
3 Gradual
4-numerical
8-mixed (6 numerical, 2 categorical)
Unknown
19-mixed (16 numerical, 3 categorical) Unknown

Table 7.2: Configurations of Synthetic and Real-world Datasets

8 Comparison of SPC-based Detectors

For SPC detectors (cf. Table 8.1), on abrupt-drift datasets, NB shows modest per-
formance, with FTDD achieves the highest AUC average, while the other methods all
yield a lower average. With HT, performance is considerably higher across all detec-
tors, confirming the advantage of the more expressive base learner. FTDD performs
best, followed by EWMA, while RDDM shows the lowest performance. On gradual-drift

19

---

<!-- PAGE 20 -->

datasets, NB performance remains uniform across all SPC methods, where HT yields
moderately higher values and EWMA and EDDM tied at the top. On real-world data
streams, NB reveals a notable divergence among detectors: FTDD records the lowest
average, whereas the remaining methods achieve a substantially higher average. For HT,
the results follow a similar pattern: FTTD yields the lowest average AUC, whereas the
other methods achieve comparable performance.

When considering all dataset types together, overall HT surpasses NB. The results
indicate that while FTDD holds an advantage on abrupt-drift data, EWMA and EDDM
deliver the most reliable performance across all dataset types.

NB

HT

FTDD RDDM FHDDM EWMA EDDM FTDD RDDM FHDDM EWMA EDDM

0.57
RTa
0.61
Sinea
M ixeda 0.55
0.58
Avera

RTg
0.63
0.50
Sineg
M ixedg 0.51
0.55
Averg

ELE
CIC
Averr

0.70
0.38
0.54

0.62
0.52
0.52
0.55

0.63
0.50
0.51
0.55

0.75
0.80
0.78

0.63
0.51
0.52
0.55

0.63
0.51
0.51
0.55

0.75
0.80
0.78

0.63
0.51
0.52
0.55

0.63
0.51
0.51
0.55

0.75
0.80
0.78

0.63
0.51
0.52
0.55

0.63
0.51
0.51
0.55

0.75
0.80
0.78

0.60
0.78
0.69
0.69

0.76
0.49
0.50
0.58

0.71
0.71
0.71

0.70
0.50
0.55
0.58

0.77
0.50
0.47
0.58

0.75
0.78
0.77

0.74
0.56
0.56
0.62

0.77
0.49
0.49
0.58

0.75
0.78
0.77

0.75
0.56
0.57
0.63

0.78
0.52
0.49
0.60

0.75
0.78
0.77

0.76
0.56
0.54
0.62

0.78
0.52
0.49
0.60

0.75
0.77
0.76

Table 8.1: Comparisons of SPC-based Methods Combined With Two Base Learners

9 Comparison of Window-based Detectors

For window-based detectors (cf. Table 9.1), on abrupt-drift datasets, NB shows uniform
and modest performance, with all six methods yielding an identical average AUC, offering
no differentiation among detectors. With HT, performance is consistently higher and
slight differences emerge: KSWIN, WSTD and D3 each reach the same top average
value, while FPDD, MDDM and ADWIN obtain a marginally lower average.

On gradual-drift datasets, NB again remains stable and uniform across all methods.
HT yields moderately higher values, where WSTD, MDDM, ADWIN and D3 all reach
the same top average, while KSWIN and FPDD each fall slightly behind.

On real-world data streams, NB reveals a notable divergence among detectors: KSWIN
records the lowest average, driven by a sharp drop on the CIC dataset, whereas the
remaining methods achieve a substantially higher average. For HT, the results follow
a similar pattern: KSWIN yields the lowest average, while the other methods achieve
comparable or slightly higher performance.

20

---

<!-- PAGE 21 -->

When considering all dataset types together, HT surpasses NB across all window-
based methods, though the margin remains modest. Overall, window-based methods
yield similar aggregate performance levels to SPC detectors, and no single window-
based detector emerges as clearly dominant within either base learner when all dataset
types are combined. The results indicate that while KSWIN, WSTD and D3 share an
advantage on abrupt-drift data, WSTD and D3 deliver the most reliable performance
across all dataset types.

KSWIN FPDD WSTD MDDM ADWIN D3 KSWIN FPDD WSTD MDDM ADWIN D3

NB

HT

0.63
RTa
Sinea
0.51
M ixeda 0.52
0.55
Avera

0.64
RTg
Sineg
0.51
M ixedg 0.51
0.55
Averg

ELE
CIC
Averr

0.70
0.38
0.54

0.63
0.50
0.52
0.55

0.63
0.51
0.51
0.55

0.75
0.80
0.78

0.64
0.50
0.52
0.55

0.63
0.51
0.51
0.55

0.75
0.80
0.78

0.63
0.50
0.51
0.55

0.63
0.51
0.51
0.55

0.75
0.80
0.78

0.63
0.50
0.51
0.55

0.63
0.51
0.51
0.55

0.75
0.80
0.78

0.63 0.77
0.50 0.54
0.51 0.52
0.55 0.61

0.63 0.78
0.51 0.51
0.51 0.49
0.55 0.59

0.75 0.71
0.80 0.71
0.78 0.71

0.77
0.53
0.50
0.60

0.79
0.50
0.49
0.59

0.75
0.78
0.77

0.78
0.54
0.50
0.61

0.79
0.51
0.50
0.60

0.75
0.78
0.77

0.78
0.51
0.51
0.60

0.79
0.50
0.50
0.60

0.75
0.78
0.77

0.78
0.52
0.50
0.60

0.80
0.52
0.49
0.60

0.75
0.77
0.76

0.78
0.53
0.51
0.61

0.80
0.50
0.49
0.60

0.75
0.77
0.76

Table 9.1: Comparison of Window-based Methods Combined With Two Base Learners

10 Comparison of Ensemble-based Detectors

The ensemble detectors (cf. Table 10.1) demonstrate considerably higher performance
across most dataset categories compared to SPC and window-based methods. On abrupt-
drift datasets, NB combined with ARF achieves the strongest average, followed by AWE,
AUE, and DWM in descending order. With HT, ARF further improves and continues
to lead, with AWE, AUE, and DWM preserving the same ranking across both learners.
On gradual-drift datasets, NB with ARF again obtains the highest average, followed
by AWE, AUE, and DWM. With HT, ARF continues to lead, followed by AWE, AUE,
and DWM, maintaining a consistent ordering across both base learners.

On real-world data streams, the ranking shifts considerably. With NB, AUE achieves
the highest average, followed by AWE, ARF, and DWM. With HT, AUE becomes the
clear top performer, followed by AWE, DWM, and ARF, indicating that AUE holds a
particular advantage on real-world streams while ARF’s dominance does not transfer
from synthetic data.

When considering all dataset types together, HT surpasses NB across all ensemble
methods. ARF+HT achieves the highest overall average, closely followed by AUE+HT

21

---

<!-- PAGE 22 -->

and AWE+HT, with DWM+HT reaching the lowest among HT-based methods. For NB,
AUE leads, followed by AWE, ARF, and DWM. The results indicate that while ARF
consistently dominates on both abrupt and gradual synthetic drift scenarios, AUE proves
most effective on real-world data, underscoring the importance of dataset characteristics
when selecting an ensemble-based drift detection method.

NB

HT

ARF AUE DWM AWE ARF AUE DWM AWE

0.83
0.95
0.97
0.92

0.76
0.93
0.96
0.88

0.81
0.36
0.59

0.73
0.78
0.68
0.73

0.73
0.81
0.70
0.75

0.88
0.70
0.79

0.65
0.59
0.56
0.60

0.65
0.53
0.53
0.57

0.70
0.37
0.54

0.76
0.90
0.87
0.84

0.78
0.88
0.84
0.83

0.74
0.64
0.69

0.88
0.98
0.97
0.94

0.88
0.97
0.96
0.94

0.82
0.63
0.73

0.74
0.83
0.78
0.78

0.74
0.84
0.79
0.72

0.89
0.87
0.88

0.69
0.80
0.68
0.72

0.76
0.53
0.54
0.61

0.71
0.77
0.74

0.77
0.91
0.89
0.86

0.80
0.90
0.87
0.86

0.75
0.75
0.75

RTa
Sinea
M ixeda
Avera
RTg
Sineg
M ixedg
Averg
ELE
CIC
Averr

Table 10.1: Comparisons of Ensemble-based Methods Combined With Two Base Learn-

ers

11 A Summary

As presented in Table 11, HT generally outperforms NB across most dataset categories
and detector families. However, a notable exception arises on real-world data streams,
where NB achieves equal or slightly superior performance to HT within both SPC and
window-based methods. This suggests that the advantage of a more expressive base
learner is not universal and depends on the nature of the data. Ensemble methods
consistently outperform both SPC and window-based detectors across all dataset types,
and their strongest results are achieved with HT, reinforcing that the choice of base
learner significantly impacts predictive accuracy under concept drift.

Focusing on single-detector families, EWMA+HT and EDDM+HT offer the best over-
all SPC performance (≈ 0.69) and the best gradual-drift accuracy (≈ 0.60). For real-
world streams, NB paired with RDDM, FHDDM, EWMA, or EDDM achieves the high-
est SPC result of approximately 0.78. Within the window-based family, KSWIN+HT,
WSTD+HT, and D3+HT are jointly strongest for abrupt drifts (≈ 0.61), while WSTD+HT,
MDDM+HT, ADWIN+HT and D3+HT perform best on gradual drifts (≈ 0.60). On
real-world streams, all window-based methods paired with NB uniformly achieve the
top result of approximately 0.78. Overall, all window-based methods with HT yield
an identical aggregate performance of 0.68, with no single detector emerging as dom-

22

---

<!-- PAGE 23 -->

Cat.

SPC
SPC
SPC

Window
Window
Window

Drift type Learner Best method

HT
Abrupt
HT
Gradual
Real-world NB
HT
Overall

HT
Abrupt
Gradual
HT
Real-world NB
HT
Overall

FTDD
EWMA/EDDM
RDDM/FHDDM/EWMA/EDDM
EWMA/EDDM

KSWIN/WSTD/D3
WSTD/MDDM/ADWIN/D3
FPDD/WSTD/MDDM/ADWIN/D3
WSTD/D3

HT
Ensemble Abrupt
Ensemble Gradual
HT
Ensemble Real-world HT
HT
Overall

ARF
ARF
AUE
ARF

Table 11.1: Best-performing drift detectors by category, drift type and base learner

inant. Among ensemble-based methods, ARF+HT achieves the strongest results on
both abrupt and gradual drift scenarios (≈ 0.94) and ranks best in overall aggregate
performance (≈ 0.83), while AUE+HT proves most effective on real-world data streams
(≈ 0.88). Overall, although SPC and window-based detectors remain competitive, par-
ticularly on real-world data with NB, the most reliable and consistent improvements
across all drift scenarios come from ensemble-based adaptation mechanisms, especially
ARF+HT.

12 Conclusions

Concept drifts are prevalent in today’s streaming applications where data distributions
and relationships change over time. They have significant consequences in many critical
domains, such as healthcare, banking, finance, cybersecurity, email spam and phishing,
In these applications, drifts can
IoT, sensor networks and recommendation systems.
degrade the performance of decision models and increase the risk of incorrect classifi-
cations. Therefore, accurately identifying such drifts is crucial to prevent classification
models from deteriorating.

The aim of our study is to simplify the description of a broad range of learner-based
concept drift detection algorithms in order to enhance the comprehension of these com-
plex methods. These algorithms are classified into three main groups, Statistical Process
Control (SPC) methods, windowing techniques and ensemble-based approaches. These
methods can operate in either active or passive modes and can be implemented in online
or block-based settings. We have also conducted an extensive evaluation and comparison

23

---

<!-- PAGE 24 -->

of these detectors using both synthetic and real-world datasets to assess their perfor-
mance.

References

[1] Osama A.Mehdi et al. “Roadmap of Concept Drift Adaptation in Data Stream
Mining, Years Later”. In: IEEE Access PP (Jan. 2024), pp. 1–1. doi: 10.1109/
ACCESS.2024.3358817.

[2] Joao Paulo Papa Adriana Sayuri Iwashita. “An Overview on Concept Drift Learn-

ing”. In: IEEE Access (2019).

[3] Supriya Agrahari and Anil Kumar Singh. “Concept Drift Detection in Data Stream
Mining : A literature review”. In: Journal of King Saud University - Computer and
Information Sciences 34.10, Part B (2022), pp. 9523–9540. issn: 1319-1578. doi:
https : / / doi . org / 10 . 1016 / j . jksuci . 2021 . 11 . 006. url: https : / / www .
sciencedirect.com/science/article/pii/S1319157821003062.

[4] Gabriel Aguiar, Bartosz Krawczyk, and Alberto Cano. “A survey on learning from
imbalanced data streams: taxonomy, challenges, empirical study, and reproducible
experimental framework”. In: Machine Learning 113 (June 2023), pp. 1–79. doi:
10.1007/s10994-023-06353-6.

[5] M. Baena-Garcıa et al. “Early drift detection method”. In: International Workshop

on Knowledge Discovery from Data Streams (2006).

[6] R. S. M. Barros and S. G. T. C. Santos. “A large-scale comparison of concept
drift detectors”. In: Information Sciences 451-452 (2018), pp. 348–370. issn: 0020-
0255. doi: https : / / doi . org / 10 . 1016 / j . ins . 2018 . 04 . 014. url: https :
//www.sciencedirect.com/science/article/pii/S0020025518302743.

[7] Roberto Barros, Juan Gonzalez Hidalgo, and Danilo Cabral. “Wilcoxon Rank Sum
Test Drift Detector”. In: Neurocomputing 275 (Jan. 2018), pp. 1954–1963. doi:
10.1016/j.neucom.2017.10.051.

[8] Roberto Barros and Silas Santos. “An Overview and Comprehensive Comparison
of Ensembles for Concept Drift”. In: Information Fusion 52 (Dec. 2019), pp. 213–
244. doi: 10.1016/j.inffus.2019.03.006.

[9] Roberto Barros et al. “RDDM: Reactive drift detection method”. In: Expert Sys-
tems with Applications 90 (Dec. 2017), pp. 344–355. doi: 10.1016/j.eswa.2017.
08.023.

[10] Barı¸s Bayram, Bilge K¨oro˘glu, and Mehmet G¨onen. “Improving Fraud Detection
and Concept Drift Adaptation in Credit Card Transactions Using Incremental
Gradient Boosting Trees”. In: 2020 19th IEEE International Conference on Ma-
chine Learning and Applications (ICMLA). 2020, pp. 545–550. doi: 10 . 1109 /
ICMLA51294.2020.00091.

24

---

<!-- PAGE 25 -->

[11] Alessio Bernardo. Artificial and Real dataset with different concept drift type and
imbalance ratio. Version V1. 2020. doi: 10.7910/DVN/RKY6RD. url: https://
doi.org/10.7910/DVN/RKY6RD.

[12] A. Bifet and R. Gavalda. “Learning from Time-Changing Data with Adaptive

Windowing”. In: SDM (2007).

[13] D. Brzezinski and J. Stefanowski. “Accuracy Updated Ensemble for Data Streams
with Concept Drift”. In: vol. 6679. May 2011, pp. 155–163. isbn: 978-3-642-21221-
5. doi: 10.1007/978-3-642-21222-2_19.

[14] D. R. L. Cabral and R. S. M. Barros. “Concept drift detection based on Fisher’s
Exact test”. In: Information Sciences 442-443 (2018), pp. 220–234. issn: 0020-
0255. doi: https : / / doi . org / 10 . 1016 / j . ins . 2018 . 02 . 054. url: https :
//www.sciencedirect.com/science/article/pii/S0020025518301403.

[15] Andreas Kassler Firas Bayram Bestoun S. Ahmed. “From concept drift to model
degradation: An overview on performance-aware drift detectors”. In: Knowledge-
Based Systems (2022).

[16] R. A. Fisher. “On the Interpretation of X2 from Contingency Tables, and the
Calculation of P”. In: Journal of the Royal Statistical Society 85.1 (1922), pp. 87–
94. issn: 09528385. url: http://www.jstor.org/stable/2340521 (visited on
11/12/2024).

[17] J. Gama et al. “A Survey on Concept Drift Adaptation”. In: ACM Computing

Surveys (CSUR) (2014).

[18] J. Gama et al. “Learning with Drift Detection”. In: Intelligent Data Analysis

(2004).

[20]

[19] Heitor M. Gomes et al. “Correction to: Adaptive random forests for evolving data
stream classification”. In: Mach. Learn. 108.10 (Oct. 2019), pp. 1877–1878. issn:
0885-6125. doi: 10.1007/s10994- 019- 05793- 3. url: https://doi.org/10.
1007/s10994-019-05793-3.
¨Omer G¨oz¨ua¸cik et al. “Unsupervised Concept Drift Detection with a Discrimina-
tive Classifier”. In: Proceedings of the 28th ACM International Conference on In-
formation and Knowledge Management (2019). url: https://api.semanticscholar.
org/CorpusID:207757814.
¨Omer G¨oz¨ua¸cık and Fazli Can. “Concept learning using one-class classifiers for
implicit drift detection in evolving data streams”. In: Artif. Intell. Rev. 54.5 (June
2021), pp. 3725–3747. issn: 0269-2821. doi: 10.1007/s10462-020-09939-x. url:
https://doi.org/10.1007/s10462-020-09939-x.

[21]

[22] Ege Gulcan and Fazli Can. “Unsupervised concept drift detection for multi-label
data streams”. In: Artificial Intelligence Review 56 (July 2022). doi: 10.1007/
s10462-022-10232-2.

25

---

<!-- PAGE 26 -->

[23] Meng Han et al. “A survey of active and passive concept drift handling methods”.
In: Computational Intelligence 38.4 (2022), pp. 1492–1535. doi: https://doi.
org/10.1111/coin.12520. eprint: https://onlinelibrary.wiley.com/doi/
pdf/10.1111/coin.12520. url: https://onlinelibrary.wiley.com/doi/abs/
10.1111/coin.12520.

[24] Tegjyot S. Sethi Hanqing Hu Mehmed Kantardzic. “No Free Lunch Theorem for
concept drift detection in streaming data classification: A review”. In: Wiley In-
terdisciplinary Reviews: Data Mining and Knowledge Discovery (2019).

[25] Fabian Hinder, Valerie Vaquet, and Barbara Hammer. One or Two Things We
know about Concept Drift – A Survey on Monitoring Evolving Environments. 2023.
arXiv: 2310.15826 [cs.LG]. url: https://arxiv.org/abs/2310.15826.

[26] Wassily Hoeffding. “Probability Inequalities for Sums of Bounded Random Vari-
ables”. In: Journal of the American Statistical Association 58.301 (1963), pp. 13–
30. issn: 01621459, 1537274X. url: http://www.jstor.org/stable/2282952
(visited on 10/22/2024).

[27] M. Hammami I. Khamassi M. Sayed-Mouchaweh and K. Gh´edira. “Discussion and
review on evolving data streams and concept drift adapting”. In: Evolving Systems
(2018).

[28] Meenal Jain, Gagandeep Kaur, and Vikas Saxena. “A K-Means clustering and
SVM based hybrid concept drift detection technique for network anomaly detec-
tion”. In: Expert Systems with Applications 193 (2022), p. 116510. issn: 0957-
4174. doi: https : / / doi . org / 10 . 1016 / j . eswa . 2022 . 116510. url: https :
//www.sciencedirect.com/science/article/pii/S0957417422000112.

[29] Botao Jiao et al. “Dynamic Ensemble Selection for Imbalanced Data Streams With
Concept Drift”. In: IEEE Transactions on Neural Networks and Learning Systems
35.1 (2024), pp. 1278–1291. doi: 10.1109/TNNLS.2022.3183120.

[30] J. Zico Kolter and Marcus A. Maloof. “Dynamic Weighted Majority: An Ensemble
Method for Drifting Concepts”. In: J. Mach. Learn. Res. 8 (Dec. 2007), pp. 2755–
2790. issn: 1532-4435.

[31] Bartosz Krawczyk et al. “Ensemble learning for data stream analysis: A survey”.
In: Information Fusion 37 (2017), pp. 132–156. issn: 1566-2535. doi: https://
doi.org/10.1016/j.inffus.2017.02.004. url: https://www.sciencedirect.
com/science/article/pii/S1566253516302329.

[32] N. Littlestone and M.K. Warmuth. “The Weighted Majority Algorithm”. In: Infor-
mation and Computation 108.2 (1994), pp. 212–261. issn: 0890-5401. doi: https:
//doi.org/10.1006/inco.1994.1009. url: https://www.sciencedirect.com/
science/article/pii/S0890540184710091.

[33] Jes´us L´opez Lobo. Synthetic datasets for concept drift detection purposes. url:

https://doi.org/10.7910/DVN/5OWRGB. Harvard Dataverse.

26

---

<!-- PAGE 27 -->

[34] Jie Lu et al. “Data-driven decision support under concept drift in streamed big
data”. In: Complex and Intelligent Systems 6 (2020). doi: 10.1007/s40747-019-
00124-4.

[35] Jie Lu et al. “Learning under Concept Drift: A Review”. In: IEEE Transactions
on Knowledge and Data Engineering 31.12 (2019), pp. 2346–2363. doi: 10.1109/
TKDE.2018.2876857.

[36] Donia Malekian and Mahmoud Reza Hashemi. “An adaptive profile based fraud
detection framework for handling concept drift”. In: 2013 10th International ISC
Conference on Information Security and Cryptology (ISCISC). 2013, pp. 1–6. doi:
10.1109/ISCISC.2013.6767338.

[37] Colin McDiarmid. “Surveys in Combinatorics, 1989: On the method of bounded
differences”. In: 1989. url: https : / / api . semanticscholar . org / CorpusID :
116663483.

[38] Hassan Mehmood et al. “Concept Drift Adaptation Techniques in Distributed
Environment for Real-World Data Streams”. In: Smart Cities (2021). url: https:
//api.semanticscholar.org/CorpusID:233623878.

[39] K. Nishida and K. Yamauchi. “Detecting Concept Drift Using Statistical Testing”.

In: Discovery Science, 10th International Conference, DS 2007 (2007).

[40] Yuri Thomas P. Nunes and Luiz Affonso Guedes. “Concept Drift Detection Based
on Typicality and Eccentricity”. In: IEEE Access 12 (2024), pp. 13795–13808. doi:
10.1109/ACCESS.2024.3355959.

[41] Sirvan Parasteh and Samira Sadaoui. “A Novel Probabilistic Approach for Detect-
ing Concept Drift in Streaming Data”. In: Deep Learning Theory and Applications.
Ed. by Donatello Conte et al. Cham: Springer Nature Switzerland, 2023, pp. 173–
188. isbn: 978-3-031-39059-3.

[42] Sirvan Parasteh and Samira Sadaoui. “A Probabilistic Approach for Detecting
Real Concept Drift.” In: Proc. of 16th International Conference on Agents and
Artificial Intelligence-Volume 2, ICAART (2). 2024, pp. 301–311.

[43] Sirvan Parasteh and Samira Sadaoui. “A Robust Probabilistic Framework for Iden-
tifying and Evaluating Concept Drift in Abrupt and Gradual Scenarios”. In: Agents
and Artificial Intelligence. Ed. by Ana Paula Rocha, Luc Steels, and Jaap van den
Herik. Springer Nature, 2025, pp. 353–367.

[44] Sirvan Parasteh, Samira Sadaoui, and Mohammad Sadegh Khosravani. “Detection
of Real Concept Drift Under Noisy Data Stream”. In: 2023 IEEE Symposium
Series on Computational Intelligence (SSCI). IEEE. 2023, pp. 1316–1321.

[45] A. Pesaranghader, H. Viktor, and E. Paquet. McDiarmid Drift Detection Methods

for Evolving Data Streams. 2018. arXiv: 1710.02030 [stat.ML].

27

---

<!-- PAGE 28 -->

[46] Ali Pesaranghader and Herna L. Viktor. “Fast Hoeffding Drift Detection Method
for Evolving Data Streams”. In: Machine Learning and Knowledge Discovery in
Databases. Cham: Springer International Publishing, 2016, pp. 96–111. isbn: 978-
3-319-46227-1.

[47] C. Raab, M. Heusinger, and F. Schleif. “Reactive Soft Prototype Computing for

Concept Drift Streams”. In: Neurocomputing (2020).

[48] Gordon J. Ross et al. “Exponentially weighted moving average charts for detecting
concept drift”. In: Pattern Recognition Letters 33.2 (2012), pp. 191–198. issn: 0167-
8655. doi: https://doi.org/10.1016/j.patrec.2011.08.019.

[49] Armin Sadreddin and Samira Sadaoui. “Chunk-based incremental feature learn-
ing for credit-card fraud data stream”. In: Journal of Experimental & Theoretical
Artificial Intelligence (2022), pp. 1–19. doi: 10.1080/0952813X.2022.2153277.
url: https://doi.org/10.1080/0952813X.2022.2153277.

[50] Bruno Henrique Schwengber et al. “Learning From Network Data Changes for
Unsupervised Botnet Detection”. In: IEEE Transactions on Network and Service
Management 19.1 (2022), pp. 601–613. doi: 10.1109/TNSM.2021.3109076.

[51] Eyad Elyan Scott Wares John Isaacs. “Data stream mining: methods and chal-

lenges for handling concept drift”. In: SN Applied Sciences (2019).

[52]

Iman Sharafaldin, Arash Habibi Lashkari, and Ali A. Ghorbani. “Toward Gener-
ating a New Intrusion Detection Dataset and Intrusion Traffic Characterization”.
In: International Conference on Information Systems Security and Privacy. 2018.
url: https://api.semanticscholar.org/CorpusID:4707749.

[53] Andr´es L. Su´arez-Cetrulo, David Quintana, and Alejandro Cervantes. “A survey on
machine learning for recurring concept drifting data streams”. In: Expert Systems
with Applications 213 (2023), p. 118934. issn: 0957-4174. doi: https : / / doi .
org/10.1016/j.eswa.2022.118934. url: https://www.sciencedirect.com/
science/article/pii/S0957417422019522.

[54] N.V. Chawla T.R. Hoens R. Polikar. “Learning from streaming data with concept

drift and imbalance: an overview”. In: Progress in Artificial Intelligence (2012).

[55] Maurras Ulbricht Togbe et al. “Anomalies Detection Using Isolation in Concept-
Drifting Data Streams”. In: Computers 10.1 (2021). issn: 2073-431X. doi: 10 .
3390/computers10010013. url: https://www.mdpi.com/2073-431X/10/1/13.

[56] H. Wang et al. “Mining Concept-Drifting Data Streams Using Ensemble Classi-

fiers”. In: (July 2003). doi: 10.1145/956750.956778.

[57] Geoffrey I. Webb et al. “Understanding Concept Drift”. In: ArXiv (2017).

[58] Frank Wilcoxon. “Individual Comparisons by Ranking Methods”. In: Biometrics
Bulletin 1.6 (1945), pp. 80–83. issn: 00994987. url: http://www.jstor.org/
stable/3001968 (visited on 10/28/2024).

28

---

<!-- PAGE 29 -->

[59] Q. Xiang et al. “Concept Drift Adaptation Methods under the Deep Learning
Framework: A Literature Review”. In: Applied Sciences 13 (May 2023), p. 6515.
doi: 10.3390/app13116515.

[60] Lingyu Zhang, Jiabao Zhao, and Wei Li. “Online and Unsupervised Anomaly De-
tection for Streaming Data Using an Array of Sliding Windows and PDDs”. In:
IEEE Transactions on Cybernetics 51.4 (2021), pp. 2284–2289. doi: 10 . 1109 /
TCYB.2019.2935066.
Indre ˇZliobaite. “Learning under Concept Drift: an Overview”. In: ArXiv (2010).

[61]

29

<!-- MARKITDOWN CONVERSION -->

<!-- Full MarkItDown conversion for formatting fidelity. -->

| Learner-based |     |             |     | Concept    |            | Drift  | Detection: |        |     |
| ------------- | --- | ----------- | --- | ---------- | ---------- | ------ | ---------- | ------ | --- |
|               |     | Analysis    |     | and        | Evaluation |        |            |        |     |
|               | Md  | Moman       | Ul  | Haque Khan | and        | Samira | Sadaoui    |        |     |
| Department    |     | of Computer |     | Science,   | University |        | of Regina, | Canada |     |
MdMomanUlHaque.Khan@uregina.ca,
6202 nuJ 81  ]GL.sc[  1v61202.6062:viXra
Samira.Sadaoui@uregina.ca
Contents
| 1 Introduction    |     |            |     |       |     |     |     |     | 3   |
| ----------------- | --- | ---------- | --- | ----- | --- | --- | --- | --- | --- |
| 2 Characteristics |     | of Concept |     | Drift |     |     |     |     | 4   |
2.1 Formal Definitions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4
2.2 Types of Drifts . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 5
2.3 Transitions of Drifts . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 5
| 3 Concept | Drift | Detection |     |     |     |     |     |     | 6   |
| --------- | ----- | --------- | --- | --- | --- | --- | --- | --- | --- |
3.1 Active vs. Passive Detection . . . . . . . . . . . . . . . . . . . . . . . . . . 6
3.2 Learner-based vs. Distribution-based Detection . . . . . . . . . . . . . . . 7
3.3 Learner-based Detectors . . . . . . . . . . . . . . . . . . . . . . . . . . . . 8
3.4 A Summary . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 9
| 4 SPC-based |     | Detection |     |     |     |     |     |     | 9   |
| ----------- | --- | --------- | --- | --- | --- | --- | --- | --- | --- |
4.1 EDDM . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 10
4.2 FHDDM . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 10
4.3 RDDM. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 11
4.4 EWMA . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 11
4.5 FTDD . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 11
| 5 Window-Based |     | Detection |     |     |     |     |     |     | 12  |
| -------------- | --- | --------- | --- | --- | --- | --- | --- | --- | --- |
5.1 ADWIN . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 12
5.2 KSWIN . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 13
5.3 MDDM . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 13
5.4 FPDD . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 14
5.5 WSTD . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 14
1

5.6 D3 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 15
| 6 Ensemble-based |     | Detection |     | 15  |
| ---------------- | --- | --------- | --- | --- |
6.1 AWE . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 16
6.2 AUE . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 16
6.3 ARF . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 17
6.4 DWM . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 17
| 7 Experiments |     | Setup |     | 18  |
| ------------- | --- | ----- | --- | --- |
7.1 Implementation Frameworks . . . . . . . . . . . . . . . . . . . . . . . . . . 18
7.2 Streaming Datasets . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 19
| 8 Comparison   | of  | SPC-based      | Detectors | 19  |
| -------------- | --- | -------------- | --------- | --- |
| 9 Comparison   | of  | Window-based   | Detectors | 20  |
| 10 Comparison  | of  | Ensemble-based | Detectors | 21  |
| 11 A Summary   |     |                |           | 22  |
| 12 Conclusions |     |                |           | 23  |
Abstract: Machine learning algorithms deployed for evolving streaming environments
must handle the non-stationary data distributions, commonly referred to as concept
drift. The presence of concept drift poses a major challenge for many real-world ap-
plications because it can severely degrade their predictive performance, hindering their
ability to support robust decision-making. Consequently, the timely and efficient detec-
tionofdrifteventsiscriticalforsustaininghighaccuracyovertime. Thisstudyexamines
theoretically the concept drift characteristics and numerous drift detection algorithms
across several categories. Furthermore, we evaluate their performance on both synthetic
and real-world datasets exhibiting diverse streaming scenarios and drift characteristics,
such as abrupt and gradual changes. This study aims to enhance understanding of the
complex notion of concept drift characteristics and behavior of drift detectors, along
| with their | applicability | to diverse | contexts. |     |
| ---------- | ------------- | ---------- | --------- | --- |
Keywords: Concept drift types, Transition speeds, Sudden and gradual drifts,
Concept drift detection, Learner-based detection, SPC methods, Windowing methods,
Ensemble methods, Synthetic stream datasets, Implementation frameworks.
2

1 Introduction
Nowadays, most applications evolve over time, such as fraud detection, network in-
trusion, health monitoring, financial markets, predictive maintenance and environment
monitoring. For example, in e-payment systems, fraudsters often devise new strategies
to manipulate the system’s vulnerabilities, and legitimate buyers adopt new payment
methods (e.g., using new mobile wallets) [36, 10]. Regarding the environment monitor-
ing systems, sensors can result in shifts due to new pollution causes [60, 38]. Health
monitoring devices may also encounter drift because a patient’s lifestyle, age and health
status(healthisimprovingordeteriorating)changeovertime[34]. Industrialequipment
also experiences drift as it ages and degrades, and monitoring models must detect fail-
ures early [55, 40]. These non-stationary applications process an influx of data produced
non-stop, often quickly, and where data can shift unpredictably. These changes lead to
a divergence between training and operational data-distributions over time [2, 27]. Such
changesintheclassdistributionand/orfeaturedistribution, knownasconceptdrift[24],
often degrade the performance of predictive models [24]. Indeed, ML models trained on
old data patterns become invalid and obsolete, leading to poor performance and false
alarms.
Concept drift occurs when the statistical properties of the incoming data change or
the relationships between the independent variables (features) and target variable (class
label) change. The evolving data-generating environments present memory and compu-
tational challenges, making it critical to develop adaptive algorithms that can effectively
address them [27]: 1) Data arrives at high speed, necessitating algorithms with fast data
and drift analyzing capabilities, and 2) Data are continuous, making it impractical to
storeallthedata,whichrequiresalgorithmstoprocesseachsampleindividually,orselect
the most relevant data or summarize data on the fly. For each specific application, the
model developers must anticipate possible changes in future data and choose the most
effective strategies to adapt ML models to real-time changes in data properties, such as
discarding outdated knowledge and retraining the models on the adjusted feature space.
Our study provides a comprehensive survey of concept drift within the supervised
learning setting, with a particular focus on data stream classification. To support a
clearer understanding of the complex nature of concept drift, we first examine its key
characteristics through several concrete examples, including different drift types, such
as real and virtual drift, as well as different rates of change, such as abrupt, gradual,
incremental and recurring drift. The focus is placed on learner-based drift detection
methods, which are the most widely studied and applied approaches. These methods
typically monitor the behavior or performance of a learning model over time in order to
identify significant changes that may indicate the presence of drift. We outline a general
algorithmic framework for learner-based detection and examine its main categories: Sta-
tistical Control Process (SPC), Window-based and Ensemble-based. For each category,
we review a selection of representative drift detectors (with a tally of 15 methods).
In addition to the survey part, we conduct a thorough empirical evaluation of the
reviewed methods on several synthetic (under gradual and sudden drifts) and real-world
3

data streams. We choose artificial datasets because the drift locations are known a apri-
ori, which allows for a more precise assessment of each method’s ability to detect both
sudden and gradual drifts. We also consider real-world datasets to evaluate the practical
behavior of the methods under realistic conditions, where drifts may be noisy or difficult
to identify. By combining a robust review with an extensive experimental evaluation
and comparison, our study aims to provide researchers with a clearer and more practical
| understanding | of learner-based |     | detection | methods. |     |
| ------------- | ---------------- | --- | --------- | -------- | --- |
The remainder of the paper is structured as follows. Section 2 presents the formal
definitions of concept drift and discusses its main characteristics using real-world exam-
ples. Section 3 examines different classifications of drift detection methods, including
active vs. passive, online vs. block, learner-based vs. distribution-based, and SPC-
based vs. window-based vs. ensemble-based. Sections 4, 5 and 6 present the theoretical
foundations of SPC-, window- and ensemble-based detectors, respectively. Section 7
describes the existing implementation frameworks for these various methods and also
introduces the stream datasets used in the experimental evaluation. Sections 8, 9, 10
and 11 evaluate and compare the performance of SPC-, window- and ensemble-based
| methods.          | Section 12  | concludes | our     | work. |     |
| ----------------- | ----------- | --------- | ------- | ----- | --- |
| 2 Characteristics |             | of        | Concept | Drift |     |
| 2.1 Formal        | Definitions |           |         |       |     |
Concept drift occurs when learning from dynamic data streams, defined as continuous
and limitless sequence of samples, [(X ,y ),....,(X ,y )], where X is a multi-dimensional
|     |     |     |     | 0 0 | i i |
| --- | --- | --- | --- | --- | --- |
feature vector with a corresponding label y [54]. The Bayes’ decision theorem allows to
| compute | the probability | that | X is | an instance | of class y [17]: |
| ------- | --------------- | ---- | ---- | ----------- | ---------------- |
P(X|y)P(y)
|     |     |     | P(y|X) | =   |     |
| --- | --- | --- | ------ | --- | --- |
P(X)
Here, P(X|y) denotes the likelihood of the input features given the target label, P(y)
is the prior probability distribution of the output variable, and P(X) is the uncondi-
tional probability distribution of the input features. In predictive modeling, a concept
refers to the specific joint probability of input features and target class, P(X,y), which
encompasses the prior class probability P(y) and class-conditional probability P(X|y)
| as follows | [15, 27]: P(X,y) |     | = P(y)P(X|y) |     |     |
| ---------- | ---------------- | --- | ------------ | --- | --- |
Concept drift can be defined as a change in the joint probability distribution between
two distinct time steps t and t + w. Here, t represents a specific point or interval in
time, and w denotes the window over which the change in data distribution has been
identified [15, 27]. So, concept drift occurs when P (X,y) ̸= P (X,y) [15, 27].
t t+w
4

2.2 Types of Drifts
The types of drift are categorized based on the aspects of the probability distribution
that is changing.
A. Real Drift: Known as actual or true drift, this type occurs when there a change
in the posterior probability P(y|X), which can affect the decision boundary of ML
models. ThisdriftcanbearesultofchangesintheclassdistributionP(y)andlikelihood
distribution P(X|y). It indicates a fundamental change in the concept the model is
trying to predict, which over time renders the model less effective [15, 27]: P (y|X) ̸=
t
P (y|X).
t+w
An example: We assume we have a model that predicts the likelihood of an illness
based on the symptoms observed (X). In this case, real drift refers to changes in the
conditional probability of the illnesses given the symptoms, i.e. P(Disease|X). For
instance, the changes are due to an update in medical knowledge or emergence of new
illness strains.
B. Virtual Drift: Knownascovariatedrift,thistypereferstochangesinthefeature-
value distribution P(X), without altering the relationship between the input features
and the label i.e., P(y|X). With this type, the model might encounter samples that are
underrepresented or differ from those in the training dataset, leading to accuracy issues
[15, 27]: P (X) ̸= P (X).
t t+w
An example: In predicting weather conditions, suppose the model was trained with
data from the autumn season. If the model starts receiving data from winter (without
any change in P(Weather|X)), this would be an instance of virtual drift.
C. Mixed Drift: Bothrealandvirtualdriftscanhappensimultaneouslyinreal-world
scenarios, involving changes in both the prior probability of classes and probability of
features [61, 59]: P (y|X) ̸= P (y|X) and P (X) ̸= P (X).
t t+w t t+w
An example: In credit card fraud detection, we usually encounter real and virtual
shifts, such as the consumer’s spending habits change during the holiday season (real
drift) and fraudsters change their tactic strategies (virtual drift).
2.3 Transitions of Drifts
Transitions represent the speed of change from the old concept to the new one. They
can be quantified by the number of samples over which the drift occurs until the new
concept is established. These transitions are essential for understanding how to adapt
the decision models to maintain accuracy as data evolves. There are four transition
types [17, 35], and for each type, concrete examples are provided based on studies such
as [15, 36, 35].
• A. Sudden Drift: Occurs when the data distribution changes abruptly from the
old concept to a new one at a precise timestamp, which degrades instantly the
decision models. Abrupt drifts that can drastically impact the learned models.
5

Examples: 1) A sudden change in consumer behavior due to unexpected events,
like the COVID-19 pandemic and new market regulations, 2) a quick equipment
failure or 3) unforeseen weather conditions.
• B. Gradual Drift: Happens when the data patterns change progressively from
the previous concept to the new one. This type shows a longer transition phase
that involves a mixture of the old and new concepts. The new concept becomes
more predominant over time.
Examples: 1) User preferences for a particular service or product can change
slowly due to evolving trends, 2) the quality of machinery can degrade slowly
over time, and 3) a patient’s health may gradually change due to aging or the
progression of a medical condition over the years.
• C. Incremental Drift: Occurs when the current concept replaces the past con-
cept slowly, by involving intermediate concepts (may not be statistically signifi-
cant). Some researchers consider incremental drift as a variant of gradual drift,
however, what sets incremental drift apart from gradual drift is the absence of a
distinct boundary that separates the old and new concepts.
Examples: 1) The slow change in climate patterns (like in temperatures and
rainfalls) progressively affect agricultural products, and 2) fraudsters in e-payment
systems gradually adopt new tactics by shifting from simple techniques (like stolen
credit cards) to modern ones (like virtual cards and bots).
• D. Recurrent Drift: Happens when a concept that was encountered earlier
reappears after some time has passed. While this shares similarities with gradual
drift in that alteration of two concepts, the key distinction is that the old concept
reappears after some time interval in the recurring drift.
Examples: 1)Seasonalchangesinspendingbehavior, suchasincreasedpurchases
during the holiday seasons, and 2) with the winter season comes health changes
due to people becoming less active and having higher heart rates.
3 Concept Drift Detection
3.1 Active vs. Passive Detection
Driftdetectionmethodscanbemainlycategorizedintotwofolds[23,53]: active(withan
explicitdriftdetectionmechanism)vs. passive(continuousmodeladaptation). Activeor
informed detectors monitor data streams for drifts and activate some adaptation mecha-
nismswhendriftshaveoccurred,reducingFPandFNratesandsavingmemoryandCPU
resources [28, 4]. Recent examples of active detectors include: 1) probabilistic methods
that specifically identifies real drift [42] and [43], 2) a sum-product NN-based method
that detects both real and virtual drifts [41], and 3) a cross-entropy-based method that
identifies real drifts within noisy data streams [44] . On the other hand, passive meth-
odscontinuouslyupdatetheirmodelswithincomingsampleswithoutanydriftdetection
6

because they consider that drifts may occur constantly or periodically. These methods
can be handy in detecting gradual/incremental shifts, but they are time-consuming. An
example is the incremental feature learning approach introduced in [49] that continu-
ously adjusts a single NN model to new data chunks. The model is composed of several
interconnected sub-NNs, with a new sub-NN optimally created for each incoming chunk.
To prevent unbounded NN growth, only the sub-NNs most relevant to the new data
distribution are retained and re-combined to build the optimal model.
3.2 Learner-based vs. Distribution-based Detection
Drift detectors can also be broadly classified into three main categories: learner-based
(supervised), distribution-based (unsupervised) and hybrid. Each category has specific
advantages and disadvantages [35, 17, 57, 61], as explained below.
• Learner-based: These methods detect drifts by monitoring the performance of
the underlying classifiers, such as the error rates. They are further split into three
groups: Statistical Process Control (SPC), Windowing Techniques and Ensemble
Learning. The pros of these methods are: 1) Directly linked to the predictive
performance of the base models, which makes them intuitive and easy to interpret,
and 2) Effective in scenarios where the drifts directly impact the model accuracy.
Their cons are: 1) May not detect drifts that do not immediately affect model
performance, such as changes in features, 2) Require data to be labeled, and 3)
Can be sensitive to noise and random fluctuations in data.
• Distribution-based: These methods monitor changes in the data distribution
itself over different timestamps to check whether the current and historical data
windows come from the same distribution or not. They often use statistical tests
(like Kullback-Leibler divergence and Kolmogorov-Smirnov Test) to determine if
the data distribution has changed significantly. Their pros are: 1) Detect drifts
that do not immediately affect model performance, 2) Often more robust to noise
in data, and 3) Do not require data to be labeled. On the other hand, their cons
are: 1) May require a large amount of data to detect drifts accurately, 2) More
prone to false alarms, and 3) Can be computationally intensive due to continuous
statistical testing.
• Hybrid: Hybrid detectors combine elements of learner and distribution-based
methods to leverage the strengths of both methods and provide more robust drift
detection mechanisms. Their pros are: 1) Potentially more robust and versatile
in different scenarios, and 2) Can dynamically switch between performance and
distribution-based detection based on the context. Their cons are : 1) Can be
more complex to implement and tune, and 2) May incur higher computational
costs due to the dual nature of detection.
7

| 3.3 | Learner-based |     |     | Detectors |     |     |     |
| --- | ------------- | --- | --- | --------- | --- | --- | --- |
This category explicitly manages drift by incorporating mechanisms to forget old data
and retrain or adjust the underlying models to the newly detected concept. To distin-
guish drift from noise, the new concept must remain stable for some time [15]. The
detectors are usually designed to be independent of specific ML algorithms, as they can
adopt various types of learners. The general form of the learner-based detection meth-
ods is summarized in Algorithm 1 using the prequential training scheme (test and then
train). The algorithm is online, so that the drift is identified in real time. The selected
classifier is first pre-trained on an initial robust labeled dateset. The classifier then re-
ceives sequentially and continuously a stream of samples and predicts their labels. Next,
it uses a statistical test method to detect a drift by comparing a drift metric to a prede-
fined statistical threshold. For example, when the error rate (the discrepancy between
predictedandtruelabels)increasessignificantly, thisdeterminesadrift. Otherexamples
would be comparing past accuracy or prediction probability (confidence score) with the
accuracy or probability on the new data. Some detectors use a warning threshold to
| signal | an  | impending |     | drift and | monitor | the samples | more closely. |
| ------ | --- | --------- | --- | --------- | ------- | ----------- | ------------- |
Once a significant change is detected, the classifier retrains on recent data, typically
stored in a sliding window or buffer. When the buffer reaches the limit, it forgets old
data. Other methods select the most representative samples from the buffer or use all
the samples but the new data have higher weights so that the detection model focuses
| less      | on old | data      | [2]. |           |     |               |                 |
| --------- | ------ | --------- | ---- | --------- | --- | ------------- | --------------- |
| Algorithm |        | 1 General |      | Algorithm | for | Learner-based | Drift Detection |
1: Inputs: classier, intialDataset, dataStream (continous), statThreshold, RDSize
|     | (sliding  | window     | size) |      |               |     |     |
| --- | --------- | ---------- | ----- | ---- | ------------- | --- | --- |
|     | Pre-train | classifier |       | with | intialDataset |     |     |
2:
| 3:  | recentData |           | ← empty | /*window      |     | of recent data*/ |     |
| --- | ---------- | --------- | ------- | ------------- | --- | ---------------- | --- |
| 4:  | for each   | newSample |         | in dataStream |     | do               |     |
|     | Add        | newSample |         | to recentData |     |                  |     |
5:
| 6:  | if      | (length | of recentData |        | > RDSize) | then       |     |
| --- | ------- | ------- | ------------- | ------ | --------- | ---------- | --- |
| 7:  |         | Remove  | oldest        | sample | from      | recentData |     |
| 8:  | end     | if      |               |        |           |            |     |
|     | Predict |         | sample’s      | label  | with      | classifier |     |
9:
| 10: | Calculate |     | driftMetric |     | on prediction |     |     |
| --- | --------- | --- | ----------- | --- | ------------- | --- | --- |
11: if (driftMetric > statThreshold) /*significant difference*/ then
|     |     | Display | ”Drift | Detected” |     |     |     |
| --- | --- | ------- | ------ | --------- | --- | --- | --- |
12:
| 13: |     | Train      | classifier | on      | recentData | with ground | truth |
| --- | --- | ---------- | ---------- | ------- | ---------- | ----------- | ----- |
| 14: |     | recentData |            | ← empty |            |             |       |
|     | end | if         |            |         |            |             |       |
15:
| 16: | end | for |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- |
8

3.4 A Summary
Table 3.1 compares numerous detectors (those selected for the experiments) based on
theirstrategies: (1)Active(withanexplicitdriftdetectionmechanism)vs. Passive(con-
tinuous model adaptation), (2) Online (processes each sample once and then discarded
it) vs. Block-based (processes a data chunk at once), and (3) types of learner-based
| methods:    | SPC,    | Window | techniques |         | and              | Ensemble | methods.        |          |            |
| ----------- | ------- | ------ | ---------- | ------- | ---------------- | -------- | --------------- | -------- | ---------- |
|             | Method  |        | Year       | Passive | vs               | Active   | Online          | vs Block | Category   |
|             | FTDD    | [14]   | 2018       | Active  |                  |          | Online          |          | SPC        |
|             | RDDM    | [7]    | 2017       | Active  |                  |          | Online          |          | SPC        |
|             | FHDDM   | [46]   | 2016       | Active  |                  |          | Online          |          | SPC        |
|             | EWMA    | [48]   | 2012       | Active  |                  |          | Online          |          | SPC        |
|             | EDDM    | [5]    | 2006       | Active  |                  |          | Online          |          | SPC        |
|             | KSWIN   | [47]   | 2020       | Active  |                  |          | Online          |          | Window     |
|             | FPDD    | [14]   | 2018       | Active  |                  |          | Online          |          | Window     |
|             | WSTD    | [6]    | 2018       | Active  |                  |          | Online          |          | Window     |
|             | MDDM    | [45]   | 2018       | Active  |                  |          | Online          |          | Window     |
|             | ADWIN   | [12]   | 2007       | Active  |                  |          | Online          |          | Window     |
|             | D3 [20] |        | 2015       | Active  |                  |          | Online          |          | Window     |
|             | ARF     | [19]   | 2017       | Passive |                  |          | Online          |          | Ensemble   |
|             | AUE     | [13]   | 2011       | Passive |                  |          | Block-based     |          | Ensemble   |
|             | DWM     | [30]   | 2007       | Active  |                  |          | Online          |          | Ensemble   |
|             | AWE     | [56]   | 2003       | Active  |                  |          | Block-based     |          | Ensemble   |
|             | Table   | 3.1:   | A Summary  |         | of Learner-based |          | Drift Detection |          | Algorithms |
| 4 SPC-based |         |        | Detection  |         |                  |          |                 |          |            |
SPCdetectorstreatamodel’sperformanceasacontrolledprocess[15, 39]. Theyemploy
statistical tests to detect deviations from expected behavior or exceedance of predefined
control limits. By monitoring the evolution of a model’s performance, SPCs assess the
quality of the learning process [15, 39]. When performance deteriorates or crosses a
statistically significant threshold, it indicates concept drift. In such cases, SPCs may
trigger classifier retraining or apply alternative strategies to address the drift. This
approach enables real-time monitoring and facilitates prompt responses to changes in
theunderlyingdata. TherearedifferentSPCprocedures, suchas thosedefinedinDDM,
EDDM,RDDM,FHDDM,KAPPA,EWMA,STEPD,FTDDandACDDM.Wedescribe
| the | most popular | methods |     | in the | following | sections. |     |     |     |
| --- | ------------ | ------- | --- | ------ | --------- | --------- | --- | --- | --- |
9

4.1 EDDM
EarlyDriftDetectionMethod(EDDM)[5]isanimprovementoftheDDM[18], designed
tobetterdetectgradual(moderate)changes. Insteadofconsideringthenumberoferrors
asinDDM,EDDMfocusesonthedistancebetweentwosuccessiveerrors. Attimestamp
| t, EDDM | calculates [5]: |     |     |     |
| ------- | --------------- | --- | --- | --- |
• p , which is the average distance between two consecutive errors at time t
t
•
| σ t , which | is the standard | deviation | of the distances | at time t |
| ----------- | --------------- | --------- | ---------------- | --------- |
• p and σ , which track the maximum observed performance and take the
| max | max |     |     |     |
| --- | --- | --- | --- | --- |
values of p and σ when (p +2σ ) reaches its historical maximum value
|     | t   | t t | t   |     |
| --- | --- | --- | --- | --- |
The study [5] defines the warning and drift levels using α as the threshold for the
| warning zone | and β as | the threshold | for the drift zone: |     |
| ------------ | -------- | ------------- | ------------------- | --- |
•
Warning level: (p t +2σ t )/(p max +2σ max ) < α, indicating a possible change
• Drift level: (p +2σ )/(p +2σ ) < β, signaling a confirmed drift
|     | t   | t max | max |     |
| --- | --- | ----- | --- | --- |
The paper [5] recommends setting α and β to 0.95 and 0.90 respectively. When the
warning level is detected, the samples are stored in preparation for drift localization.
When the drift level is reached, the classifier along with p and σ are reset. In this
max max
case, themodelcanusethedatacollectedinthewarningzonetogetherwithrecentpost-
drift data to train or update the model. When changes occur gradually at a moderate
pace, EDDM is a better option than DDM. However, DDM is a better option when
dealing with sudden changes. The limitation of EDDM can be pointed out as it is noise
| sensitive, | which makes | it more prone | to false positives | [39]. |
| ---------- | ----------- | ------------- | ------------------ | ----- |
4.2 FHDDM
FastHoeffdingDriftDetectionMethod(FHDDM)[46]usestheHoeffdinginequality[26]
to detect changes in data streams. It continuously monitors the prediction errors and
uses the Hoeffding bound to determine whether the error rate has increased significantly
or not. FHDDM computes the mean error in this window and compares it with the
minimum error observed so far, and uses the following Hoeffding inequality:
|     |     | p(|X¯ −µ| | ≥ ϵ) ≤ 2e−2nϵ2 |     |
| --- | --- | --------- | -------------- | --- |
where X¯ is the average of the error rates of the current window, µ is the minimum
error rate assuming no drift, n is the size of the sliding window, and ϵ is the acceptable
deviation from the minimum error rate. The method flags a drift when the deviation
|X¯ −µ| is large enough, i.e. greater than or equal to the calculated threshold ϵ, derived
| from the Hoeffding | bound. |     |     |     |
| ------------------ | ------ | --- | --- | --- |
10

4.3 RDDM
Reactive Drift Detection Method (RDDM) enhances DDM by dynamically adjusting
the detection threshold based on recent error rates [3, 9]. RDDM utilizes the following
strategy, based on the calculated error rate and standard deviation [9]:
• Warning level: p +σ ≥ p +(2∗σ ), for a possible drift; p is the historical
|         |     | t          | t min | min             |           | min  |
| ------- | --- | ---------- | ----- | --------------- | --------- | ---- |
| minimum |     | error rate | and σ | is the standard | deviation | of p |
|         |     |            |       | min             |           | min  |
•
| Drift | level: | p t +σ t | ≥ p min | +(3∗σ min ), for | a detected drift |     |
| ----- | ------ | -------- | ------- | ---------------- | ---------------- | --- |
RDDM continuously recalculates warning and drift statistics, discarding outdated
samples and focusing on recent ones. It identifies concepts that remain active for an
extended period or with a long warning window. This adaptability allows to effectively
identify both sudden and gradual drifts while minimizing false alarms [6, 53]. Compared
to DDM, RDDM achieves higher accuracy in most scenarios, particularly for gradual
drifts, by detecting more drifts and identifying them earlier. However, its increased
complexity and parameter sensitivity may require careful calibration for optimal perfor-
| mance | in specific | applications | [15]. |     |     |     |
| ----- | ----------- | ------------ | ----- | --- | --- | --- |
4.4 EWMA
The exponentially weighted moving average (EWMA) was proposed in [48]. EWMA for
drift detection is a statistical process that identifies drift by monitoring the error rate of
a streaming classifier [8, 14].The standard deviation of the EWMA estimator z is [35]:
t
(cid:114)
λ
σ2
|     |     |     | =   | p (1−p ) | (1−(1−λ)2t) |     |
| --- | --- | --- | --- | -------- | ----------- | --- |
|     |     |     | zt  | 0 0 2−λ  |             |     |
Here, z t = (1−λ)z t−1 +λx t , p 0 is the baseline error rate under no-drift conditions,
| and λ is | a smoothing | parameter. |     |     |     |     |
| -------- | ----------- | ---------- | --- | --- | --- | --- |
According to EWMA, drift is detected if [15]: z > µ +Lσ . Here, L is the control
|     |     |     |     |     | t 0 | zt  |
| --- | --- | --- | --- | --- | --- | --- |
limit, which states the distance z must deviate from µ before a change is flagged. Set-
|     |     |     |     | t   | 0   |     |
| --- | --- | --- | --- | --- | --- | --- |
ting the appropriate smoothing factor (λ) is crucial for achieving optimal performance.
λ = 0.2hasbeensuggestedby[35]. Ahighλvalueincreasessensitivitytorecentchanges
but may make the method susceptible to noise. A low λ value can lead to delayed drift
detection[48]. The main advantage of EWMA is its ability to detect gradual and abrupt
drifts [3]. It is also computationally efficient, with an overhead of O(1) [48].
4.5 FTDD
The Fisher Test Drift Detector (FTDD) is one of three drift detection algorithms pro-
posed by [14], based on an efficient implementation of Fisher’s Exact Test [16]. FTDD
is based on the Sequential Testing with Estimation of Proportion Difference (STEPD)
algorithm [39], but addresses its limitations when dealing with imbalanced data [51]
Unlike STEPD, which uses a test of equal proportions, FTDD employs Fisher’s Exact
11

test in all comparisons to detect concept drift [6, 8, 15]. The p calculation is a key
value
feature of FTDD, contributing to its effectiveness in accurately detecting drifts [14]:
|     |     |         | |wr+wp| |cr+cp|  |      |
| --- | --- | ------- | ---------------- | ---- |
|     |     |         | |wr|             | |cr| |
|     |     | p value | = ×              |      |
|     |     |         | |w |             | |c | |
|     |     |         | p                | p    |
|     |     | p value | = p value×constF | ×2   |
Where w is the number of errors in the recent window, w is the proportionally
|     | r   |     |     | p   |
| --- | --- | --- | --- | --- |
calculated number of errors in past window, c is the number of correct predictions in
r
the recent window, c is the proportionally calculated number of correct predictions in
p
past window. constF is a constant factor derived from the factorial calculations for the
window size (w). It helps to optimize the p value computation by pre-calculating and
storing a common factor. Here, the probability of observing the specific distribution
of errors and correct predictions in the two windows (recent and past) is calculated
given the assumption that no drift has occurred [14]. The warning is triggered when the
p value falls below the threshold α = 0.005 and a drift is confirmed when the p is
w value
| typically less | than α | = 0.003. |     |     |
| -------------- | ------ | -------- | --- | --- |
d
| 5 Window-Based |     | Detection |     |     |
| -------------- | --- | --------- | --- | --- |
Windowing detectors handle drifts by monitoring the model performance or other sta-
tistical measures over two data windows (of a fixed or dynamic size) and checking for
significant discrepancies between them [15, 51]. They treat the classifier’s prediction
results as the data stream. They assess the chosen metric on each window and flag drift
whenthe differenceexceeds apredefinedthresholdor athresholdderived fromastatisti-
cal test [15, 51]. The dynamic windowing technique adjusts the size based on the drift’s
length, retaining samples until the drift occurs. It allows for flexibility without the need
to set a predefined window size, which is a difficult task. The decision for window size
is crucial because large windows can increase accuracy but may miss the detection of
rapid drifts, and small windows are more effective in detecting sudden drifts but might
not capture gradual changes. There are different windowing strategies, as described in
the following selected methods: ADWIN, KSWIN, MDDM, FPDD, WSTD and D3.
5.1 ADWIN
ADaptive WINdowing (ADWIN) [12] maintains a sliding window w containing the most
recent errors and tests, after every new instance, whether the average error in an older
window w p differs significantly from that in a newer window w r . ADWIN detects drift
by comparing the mean error rates (µ for w , µ for w ) of the two sub-windows. A
|     |     |     | wp p wr | r   |
| --- | --- | --- | ------- | --- |
drift is signaled when the difference in error rates exceeds a threshold derived from the
Hoeffding bound [51, 15]: |µ −µ | > ϵ, where ϵ is the threshold calculated based on
|               |       | wp    | wr  |     |
| ------------- | ----- | ----- | --- | --- |
| the Hoeffding | bound | [12]: |     |     |
12

(cid:114)
|     |     |     | 1       | 4|W| |     |
| --- | --- | --- | ------- | ---- | --- |
|     |     |     | ϵ = ln( | )    |     |
|     |     |     | 2m      | δ    |     |
Where m is the harmonic mean of the lengths of sub-windows w and w , |w| is the
r p
length of the entire window w, δ is a predefined confidence parameter, and ln() is the
natural logarithm. ADWIN has been shown to be effective in detecting both abrupt and
| gradual concept | drifts | [1]. |     |     |     |
| --------------- | ------ | ---- | --- | --- | --- |
5.2 KSWIN
Kolmogorov–Smirnov Windowing (KSWIN) [47] maintains two sliding windows of error
observations, an older window, w , and a recent window, w [44, 40]. After each new
|     |     |     | p   | r   |     |
| --- | --- | --- | --- | --- | --- |
prediction, the sup-norm KS (Kolmogorov–Smirnov) distance, dist(w ,w ) is computed
r c
for sample x, where sup-norm distance is the maximum point-wise gap between two
functions, making it highly sensitive to even a single large deviation and thus effective
| for detecting | distribution | changes | [47]:        |            |     |
| ------------- | ------------ | ------- | ------------ | ---------- | --- |
|               |              | dist(w  | ,w ) = sup|f | (x)−f (x)| |     |
|               |              | p       | r            | wp wr      |     |
(cid:80)n
| Here, f(x) | = 1   | I (x   | ) and I  | (x ) is an indicator | function. |
| ---------- | ----- | ------ | -------- | -------------------- | --------- |
|            | n i=1 | (−∞,x) | i (−∞,x) | i                    |           |
AdriftissignaledbyKSWINwhenthecalculateddistanceexceedsathresholddefined
| by the formula | below | [44, 47]: |     |     |     |
| -------------- | ----- | --------- | --- | --- | --- |
(cid:114)
ln(α)
|     |     | dist(w | ,w ) > | −   |     |
| --- | --- | ------ | ------ | --- | --- |
|     |     |        | p r    | n   |     |
Where α is the significance level representing the probability of incorrectly rejecting
the null hypothesis. Common values for α are 0.05, 0.01, or even smaller depending on
the desired level of confidence, and n is the size of the two sub-windows [47].
5.3 MDDM
McDiarmidDriftDetectionMethod(MDDM)[45]usestheMcDiarmid’sinequalityintro-
duced in [37]. MDDM operates under the assumption that in a streaming environment,
recent samples are more relevant than older ones. To reflect this, MDDM uses a sliding
window with a weighting scheme that prioritizes the most recent samples [45]. MDDM
slides a window of size n over the prediction results [22]. This window stores binary
values, where 1 represents an incorrect prediction and 0 represents a correct prediction
[15]. Each element in the window is associated with a weight, where w < w . While
i i+1
inputs are processed, the current weighted average of the elements of the window is cal-
culated, i.e. µt, as well as the maximum weighted mean observed so far, i.e. µm. When
µm < µt then µm = µt [51, 45]. Hence, with MDDM, concept drif is declared when [45]:
(µm−µt)
≥ ϵ
13

where ϵ is the threshold calculated with the McDiarmid’s inequality:
(cid:114)(cid:80)n
v2 1
ϵ = i=1 i ∗ln( )
2 δ
Here, δ is the confidence level, and v is the weight of the i-th element, calculated as:
i
v = wi [45].
i (cid:80)n
i=1
wi
5.4 FPDD
The Fisher Proportions Drift Detector (FPDD)[14] is designed to enhance the perfor-
mance of the Statistical Test of Equal Proportions(STEPD), particularly when dealing
with small sample sizes [15]. It leverages Fisher’s Exact Test to provide a more robust
statistical analysis in these scenarios [8]. This leads to more accurate drift detection
when drifts occur rapidly. Similar to STEPD, FPDD compares two windows, the recent
window (w ) and past window (w ), to analyze the data stream.
r p
The core distinction of FPDD lies in its conditional application of Fisher’s Exact
Test. Suppose the number of errors or correct predictions in either of the two windows
is smaller than five. In this case, FPDD uses Fisher’s Exact Test to assess the statistical
significance of the difference in error rates between the two windows. In cases where
the sample sizes are sufficient(5 or more), FPDD reverts to the standard test of equal
proportions used by STEPD[51]. Based on the chosen statistical test (Fisher’s Exact
Test or the test of equal proportions), FPDD calculates the p value (as computed in
section 4.5), and uses it as follows [14]:
• Drift detected: if p value ≤ α
d
• Warning signal: if α < p value ≤ α
d w
FPDD uses two similar threshold parameters like STEPD, the significance levels for
the detection of drifts ( α = 0.003 ) and warning ( α = 0.05 ).
d w
5.5 WSTD
Wilcoxon Rank Sum Test Drift Detector (WSTD) [7], which closely resembles STEPD,
detects drifts based on an efficient implementation of the Wilcoxon rank sum statistical
test [58], whereas STEPD uses the test of equal proportions [6, 23]. WSTD requires
setting a significance level (α) and applies the normal distribution to evaluate the null
hypothesis. Given two sample set, n and n , they are combined in the ascending order
1 2
as below [7]:
• Test statistic is z = (R−µR)
σR
• Population mean is µ = n × (n1+n2+1)
R 1 2
(cid:113)
• Standard deviation is σ = n ×n × (n1+n2+1)
R 1 2 12
14

where R is the smallest sum of the ranks of both sample sets, n is the size of the
1
smallest sample set, and n is the size of the largest sample set. The z value is used to
2
reject the null hypothesis, and the p value (or obtained probability) is also required to
find the z value [3, 7].
Similar to STEPD, WSTD monitors the base learner’s predictions using two windows:
a recent window and an older one. It relies on a statistical test to issue warnings or
confirm drifts. WSTD incorporates three key parameters with default values: the recent
window size (w = 30), the significance level for drift detection (α = 0.003), and the
d
significance level for warnings (α = 0.05) [7].
w
5.6 D3
Discriminative Drift Detector (D3) [20] detects changes by comparing recent and his-
torical samples. D3 operates on the principle that a change in the underlying data
distribution P(X) will manifest as a difference between recent and historical data. By
training a classifier to distinguish between these sets, D3 can detect drifts when the
classifier performs well, which suggests that the data distributions have diverged. D3
employs a sliding window, denoted as W, to store the most recent samples. The size of
this window is determined by w(1+ρ), where [20]:
• w is the number of ”old” samples, which correspond to the historical data
• ρ is the fraction of ”new” samples, relative to the size of the old data. This
essentially controls the size of the new dataset within the window
A drift is signaled when the classifier AUC score (trained to distinguish between the
old and new sample) is greater than or equal to the threshold, θ, which is typically set
between 0.5 and 1.0 [50, 20]. The performance of D3 can vary significantly based on the
specific classifier and dataset being used [25]. Additionally, the method’s capability is
constrained to identifying only linear drift patterns within the feature space [21].
6 Ensemble-based Detection
Ensemble-based detectors are a robust approach to handling drifts because combining
the outputs of several learners is more effective to changing data patterns. Many such
detectors adopt the Weighted Majority Algorithm (WMA). The ensemble remains up
to date with new concepts as follows [15, 1]: (1) a new classifier trained on the current
data is added to the ensemble, (2) the learners are then weighted according to their
performance with the current data, and (3) the least-weighted learners, deemed less
effective, are removed from the ensemble. In addition to adding/removing learners, the
ensemble may use incremental learning to adapt the learners. The ensemble approach
is efficient in identifying gradual drifts while maintaining high levels of accuracy [15, 1],
but comes with high computational and memory costs. There are numerous ensemble-
based detectors, which can be categorized as follows: (1) methods that implement their
own detection mechanisms, such as AWE, AUE, ACE and DWM, and (2) methods that
15

utilize an existing detector, such as ADWIN, which is used in algorithms like ARF. We
describe these methods in the following sections.
6.1 AWE
Accuracy Weighted Ensemble (AWE) [56] selects the most efficient classifiers using the
mean squared error (MSE), which is calculated based on the probabilities of class as-
signments. AWE identifies the top n classifiers based on their performance on the most
recent data chunk [56]. It employs MSE for assigning weights: classifiers that exhibit an
error rate meeting or exceeding a certain threshold are excluded. This method ensures
thatonlytheclassifiersmostalignedwiththecurrentdatapatternsareretained,thereby
enhancing the ensemble’s overall accuracy. The weight (w ) assigned to a classifier c is
i i
calculated using the following formulas [15, 51, 30]:
w = MSE −MSE
i r i
Here MSE is the reference MSE calculated based on the class distribution of the
r
current data chunk S [56]:
n
(cid:88)
MSE = p(c)(1−p(c))2
r
c
where p(c) is the probability of class c, which is estimated from the distribution of
classes in S . MSE represents the error for the ith classifier, calculated over S as
n i n
follows [56]:
1 (cid:88)
MSE = (1−pi(x))2
i S c
n
(x,c)ϵSn
where pi(x) is the probability that classifier i assigns sample x to class c.
c
6.2 AUE
Accuracy Updated Ensemble (AUE) [13], an advancement over AWE, updates only the
topk weightedclassifiersthatmeetacertainaccuracythresholdonthemostrecentdata
block, rather than updating all classifiers. Additionally, AUE utilizes a more straight-
forward weighting function compared to AWE [51]. AUE incorporates online classifiers,
typically Very Fast Decision Trees (VFDT) or Hoeffding Trees, by updating them in-
dividually in addition to weight modifications. This adaptability ensures that in the
absence of drift across chunks, the classifiers enhance their performance as though they
were trained on a singular, extensive dataset [51]. Consequently, this flexibility permits
a reduction in chunk size without compromising the ensemble’s accuracy. The weighting
function employed in AUE is simplified as below[13]:
1
w =
i
MSE +ϵ
i
16

where MSE is computed in the same manner as in AWE, and ϵ is a small constant
i
added to facilitate weighting calculations even when MSE equals zero [13]. The en-
i
semble size in AUE is typically fixed to a predetermined number, k, of classifiers [51].
Comparative experimental studies have demonstrated that AUE outperforms AWE in
various datasets, except for one instance where both achieved comparable accuracy [13,
51].
6.3 ARF
The Adaptive Random Forest (ARF) algorithm [19] handles evolving data streams by
incorporating several key strategies. ARF extends the traditional random forest algo-
rithm to adapt to changes in the data distribution by replacing under-performing trees
with new ones [29, 35]. ARF uses Hoeffding Trees (HT) as its base learners, which are
a type of very fast decision tree. These trees are incrementally updated with each new
sample, making them suitable for streaming data [19, 13]. ARF employs a resampling
method based on online bagging [53]. Instead of growing each tree sequentially on dif-
ferent subsets of data, as in traditional random forests, ARF simulates sampling with
reposition using a Poisson distribution, specifically Poisson (λ = 6) [19]. ARF handles
concept drift through a combination of online bagging for resampling, drift detectors for
each tree, background training of new trees, and weighted majority voting. These mech-
anisms allow the model to maintain high accuracy when dealing with non-stationary
data streams[23].
6.4 DWM
The Dynamic Weighted Majority (DWM)[30] extends the weighted majority algorithm
[32] by dynamically adjusting the weights of its base classifiers and adding/removing
classifiers based on their performance [31]. DWM is a passive adaptation method that
does not use an explicit drift detection mechanism, but rather continuously adapts its
base learner [27]. This differentiates it from methods that explicitly monitor error rates
or other statistics to detect drift.
With DWM, weights are adjusted after each new classified sample. This online ap-
proach allows DWM to adapt to gradual changes more easily [15, 23]:
• If a base classifier predicts correctly, its weight is multiplicatively increased by a
factor β > 1 i.e., w (t+1) = β ∗w (t) [51]
i i
• If a base classifier predicts incorrectly, its weight is decreased multiplicatively by
a factor α < 1 i.e., w (t+1) = α∗w (t) [51]
i i
where w (t) is the weight of classifier i at time t, and w (t+1) is the updated weight
i i
at time t+1. Typical values for the parameters can be β = 1.1 and α = 0.9.
17

| 7 Experiments |     | Setup |     |     |     |
| ------------- | --- | ----- | --- | --- | --- |
We utilize both artificial and real-world datasets from the Harvard Dataverse [33], under
abrupt and gradual scenarios, to assess the performance of drift detectors of different
categories. These datasets present distinct data characteristics, providing an extensive
testbed. When the drift is identified, the base learners, Naive Bayes and Hoeffding
Tree, are retrained with the most recent samples to ensure that predictions remain
accurate. We assess and compare these detector’s performance using the AUC metric.
AUCisusefulforassessingperformancedegradationcausedbydrifts. Foreachdetector’s
hyperparameters, we use their default values mentioned in earlier sections. In all the
experiments, we set the window size to 50 and the ensemble size to 15. In the empirical
| tables,            | the best | results are shown | in red and | the worst ones | in blue. |
| ------------------ | -------- | ----------------- | ---------- | -------------- | -------- |
| 7.1 Implementation |          | Frameworks        |            |                |          |
Table 7.1 provides the implementation frameworks of the 15 selected drift detectors.
These frameworks support a broad collection of ML algorithms, such as classification,
regression, clustering and drift detection. Here, NA indicates that there was no publicly
available implementations found online. Therefore, we implemented the Python code
| with the | assistance | from Github          | Copilot. |                      |            |
| -------- | ---------- | -------------------- | -------- | -------------------- | ---------- |
|          | Table      | 7.1: Drift Detectors | and      | their Implementation | Frameworks |
URL
|     |     | FTDD    | [14] Git              | (Fisher’s Exact | Test  |
| --- | --- | ------- | --------------------- | --------------- | ----- |
|     |     | RDDM    | [7] Tornado           |                 |       |
|     |     | FHDDM   | [46] River            |                 |       |
|     |     | EWMA    | [48] Tornado          |                 |       |
|     |     | EDDM    | [5] River             |                 |       |
|     |     | KSWIN   | [47] River            |                 |       |
|     |     | FPDD    | [14] Git              | (Fisher’s Exact | Test) |
|     |     | WSTD    | [6] NA                |                 |       |
|     |     | MDDM    | [45] Tornado          |                 |       |
|     |     | ADWIN   | [12] River            |                 |       |
|     |     | ARF     | [19] River            |                 |       |
|     |     | D3 [20] | Git                   |                 |       |
|     |     | AUE     | [13] NA               |                 |       |
|     |     | DWM     | [30] Scikit-multiflow |                 |       |
|     |     | AWE     | [56] Scikit-multiflow |                 |       |
18

| 7.2 Streaming |     | Datasets |     |     |     |     |     |
| ------------- | --- | -------- | --- | --- | --- | --- | --- |
Our empirical study utilizes synthetic and real datasets, summarized in Table 7.2, to
evaluatetheperformanceofvariousdriftdetectors. Thesixsyntheticdatasets(balanced
binary class label and without noise) have been produced using three main generators,
Random Tree Stream (RT), SINE and MIXED, by incorporating abrupt and gradual
drifts [33]:
•
RT-abrupt and RT-gradual, with the arrangement of 8873985678962563
| • Sine-abrupt  |     | and Sine-gradual,  |     | with the arrangement |             | of 0123 |         |
| -------------- | --- | ------------------ | --- | -------------------- | ----------- | ------- | ------- |
| • Mixed-abrupt |     | and Mixed-gradual, |     | with the             | arrangement |         | of 0101 |
Each dataset possess four distinct concepts and three drift locations [33]. The sudden
datasets experience abrupt shifts at locations of 10,000, 20,000 and 30,000. The gradual
datasets undergo gradual transitions at locations of 9,500, 20,000 and 30,500, with each
| transition | having | a drift width | of  | 1,000 samples. |     |     |     |
| ---------- | ------ | ------------- | --- | -------------- | --- | --- | --- |
On the other hand, we employ two real datasets (balanced binary class label), as
presented in Table 7.2. The Electricity dataset ELEC2, collected from the Australian
New South Wales electricity market, predicts whether the prices (set every five minutes)
of electricity will increase or decrease [11]. The Intrusion Detection Evaluation dataset
CIC-IDS2017containsnetworktrafficcollectedforfivedays,fromMonday,July3,2017,
| at 9am | to Friday, | July 7, 2017, | at                 | 5pm [52]. |     |     |          |
| ------ | ---------- | ------------- | ------------------ | --------- | --- | --- | -------- |
|        | Dataset    | Size          | #Features-Modality |           |     |     | #Drifts  |
|        | RT         | 40,000        | 2-numerical        |           |     |     | 3 Abrupt |
a
|     | RT  | 40,000 | 2-numerical |     |     |     | 3 Gradual |
| --- | --- | ------ | ----------- | --- | --- | --- | --------- |
g
|     | Sine | 40,000 | 2-numerical |     |     |     | 3 Abrupt |
| --- | ---- | ------ | ----------- | --- | --- | --- | -------- |
a
|     | Sine | 40,000 | 2-numerical |     |     |     | 3 Gradual |
| --- | ---- | ------ | ----------- | --- | --- | --- | --------- |
g
|     | Mixed | 40,000 | 4-numerical |     |     |     | 3 Abrupt |
| --- | ----- | ------ | ----------- | --- | --- | --- | -------- |
a
|     | Mixed | 40,000 | 4-numerical |     |     |     | 3 Gradual |
| --- | ----- | ------ | ----------- | --- | --- | --- | --------- |
g
|              | ELE   | 45,312              | 8-mixed  | (6 numerical,  | 2 categorical) |            | Unknown  |
| ------------ | ----- | ------------------- | -------- | -------------- | -------------- | ---------- | -------- |
|              | CIC   | 28,303              | 19-mixed | (16 numerical, | 3 categorical) |            | Unknown  |
|              | Table | 7.2: Configurations |          | of Synthetic   | and            | Real-world | Datasets |
| 8 Comparison |       | of SPC-based        |          | Detectors      |                |            |          |
For SPC detectors (cf. Table 8.1), on abrupt-drift datasets, NB shows modest per-
formance, with FTDD achieves the highest AUC average, while the other methods all
yield a lower average. With HT, performance is considerably higher across all detec-
tors, confirming the advantage of the more expressive base learner. FTDD performs
best, followed by EWMA, while RDDM shows the lowest performance. On gradual-drift
19

datasets, NB performance remains uniform across all SPC methods, where HT yields
moderately higher values and EWMA and EDDM tied at the top. On real-world data
streams, NB reveals a notable divergence among detectors: FTDD records the lowest
average, whereastheremainingmethodsachieveasubstantiallyhigheraverage. ForHT,
the results follow a similar pattern: FTTD yields the lowest average AUC, whereas the
| other | methods | achieve | comparable | performance. |     |     |     |     |
| ----- | ------- | ------- | ---------- | ------------ | --- | --- | --- | --- |
When considering all dataset types together, overall HT surpasses NB. The results
indicate that while FTDD holds an advantage on abrupt-drift data, EWMA and EDDM
| deliver | the most | reliable | performance   | across | all dataset | types. |               |      |
| ------- | -------- | -------- | ------------- | ------ | ----------- | ------ | ------------- | ---- |
|         |          |          | NB            |        |             |        | HT            |      |
|         | FTDD     | RDDM     | FHDDMEWMAEDDM |        | FTDD        | RDDM   | FHDDMEWMAEDDM |      |
| RT      | 0.57     | 0.62     | 0.63          | 0.63   | 0.63 0.60   | 0.70   | 0.74 0.75     | 0.76 |
a
| Sine | 0.61 | 0.52 | 0.51 | 0.51 | 0.51 0.78 | 0.50 | 0.56 0.56 | 0.56 |
| ---- | ---- | ---- | ---- | ---- | --------- | ---- | --------- | ---- |
a
| Mixed | 0.55 | 0.52 | 0.52 | 0.52 | 0.52 0.69 | 0.55 | 0.56 0.57 | 0.54 |
| ----- | ---- | ---- | ---- | ---- | --------- | ---- | --------- | ---- |
a
| Aver | 0.58 | 0.55 | 0.55 | 0.55 | 0.55 0.69 | 0.58 | 0.62 0.63 | 0.62 |
| ---- | ---- | ---- | ---- | ---- | --------- | ---- | --------- | ---- |
a
| RT g   | 0.63   | 0.63 | 0.63 | 0.63 | 0.63 0.76 | 0.77 | 0.77 0.78 | 0.78 |
| ------ | ------ | ---- | ---- | ---- | --------- | ---- | --------- | ---- |
| Sine g | 0.50   | 0.50 | 0.51 | 0.51 | 0.51 0.49 | 0.50 | 0.49 0.52 | 0.52 |
| Mixed  | g 0.51 | 0.51 | 0.51 | 0.51 | 0.51 0.50 | 0.47 | 0.49 0.49 | 0.49 |
| Aver g | 0.55   | 0.55 | 0.55 | 0.55 | 0.55 0.58 | 0.58 | 0.58 0.60 | 0.60 |
| ELE    | 0.70   | 0.75 | 0.75 | 0.75 | 0.75 0.71 | 0.75 | 0.75 0.75 | 0.75 |
| CIC    | 0.38   | 0.80 | 0.80 | 0.80 | 0.80 0.71 | 0.78 | 0.78 0.78 | 0.77 |
| Aver   | 0.54   | 0.78 | 0.78 | 0.78 | 0.78 0.71 | 0.77 | 0.77 0.77 | 0.76 |
r
Table 8.1: Comparisons of SPC-based Methods Combined With Two Base Learners
| 9 Comparison |     | of  | Window-based |     | Detectors |     |     |     |
| ------------ | --- | --- | ------------ | --- | --------- | --- | --- | --- |
For window-based detectors (cf. Table 9.1), on abrupt-drift datasets, NB shows uniform
andmodestperformance,withallsixmethodsyieldinganidenticalaverageAUC,offering
no differentiation among detectors. With HT, performance is consistently higher and
slight differences emerge: KSWIN, WSTD and D3 each reach the same top average
value, while FPDD, MDDM and ADWIN obtain a marginally lower average.
On gradual-drift datasets, NB again remains stable and uniform across all methods.
HT yields moderately higher values, where WSTD, MDDM, ADWIN and D3 all reach
the same top average, while KSWIN and FPDD each fall slightly behind.
Onreal-worlddatastreams,NBrevealsanotabledivergenceamongdetectors: KSWIN
records the lowest average, driven by a sharp drop on the CIC dataset, whereas the
remaining methods achieve a substantially higher average. For HT, the results follow
a similar pattern: KSWIN yields the lowest average, while the other methods achieve
| comparable | or  | slightly | higher | performance. |     |     |     |     |
| ---------- | --- | -------- | ------ | ------------ | --- | --- | --- | --- |
20

When considering all dataset types together, HT surpasses NB across all window-
based methods, though the margin remains modest. Overall, window-based methods
yield similar aggregate performance levels to SPC detectors, and no single window-
based detector emerges as clearly dominant within either base learner when all dataset
types are combined. The results indicate that while KSWIN, WSTD and D3 share an
advantage on abrupt-drift data, WSTD and D3 deliver the most reliable performance
across all dataset types.
NB HT
KSWIN FPDD WSTDMDDM ADWIND3 KSWIN FPDD WSTDMDDM ADWIND3
RT 0.63 0.63 0.64 0.63 0.63 0.63 0.77 0.77 0.78 0.78 0.78 0.78
a
Sine 0.51 0.50 0.50 0.50 0.50 0.50 0.54 0.53 0.54 0.51 0.52 0.53
a
Mixed 0.52 0.52 0.52 0.51 0.51 0.51 0.52 0.50 0.50 0.51 0.50 0.51
a
Aver 0.55 0.55 0.55 0.55 0.55 0.55 0.61 0.60 0.61 0.60 0.60 0.61
a
RT 0.64 0.63 0.63 0.63 0.63 0.63 0.78 0.79 0.79 0.79 0.80 0.80
g
Sine 0.51 0.51 0.51 0.51 0.51 0.51 0.51 0.50 0.51 0.50 0.52 0.50
g
Mixed 0.51 0.51 0.51 0.51 0.51 0.51 0.49 0.49 0.50 0.50 0.49 0.49
g
Aver 0.55 0.55 0.55 0.55 0.55 0.55 0.59 0.59 0.60 0.60 0.60 0.60
g
ELE 0.70 0.75 0.75 0.75 0.75 0.75 0.71 0.75 0.75 0.75 0.75 0.75
CIC 0.38 0.80 0.80 0.80 0.80 0.80 0.71 0.78 0.78 0.78 0.77 0.77
Aver 0.54 0.78 0.78 0.78 0.78 0.78 0.71 0.77 0.77 0.77 0.76 0.76
r
Table 9.1: Comparison of Window-based Methods Combined With Two Base Learners
10 Comparison of Ensemble-based Detectors
The ensemble detectors (cf. Table 10.1) demonstrate considerably higher performance
acrossmostdatasetcategoriescomparedtoSPCandwindow-basedmethods. Onabrupt-
driftdatasets,NBcombinedwithARFachievesthestrongestaverage,followedbyAWE,
AUE, and DWM in descending order. With HT, ARF further improves and continues
to lead, with AWE, AUE, and DWM preserving the same ranking across both learners.
On gradual-drift datasets, NB with ARF again obtains the highest average, followed
by AWE, AUE, and DWM. With HT, ARF continues to lead, followed by AWE, AUE,
and DWM, maintaining a consistent ordering across both base learners.
On real-world data streams, the ranking shifts considerably. With NB, AUE achieves
the highest average, followed by AWE, ARF, and DWM. With HT, AUE becomes the
clear top performer, followed by AWE, DWM, and ARF, indicating that AUE holds a
particular advantage on real-world streams while ARF’s dominance does not transfer
from synthetic data.
When considering all dataset types together, HT surpasses NB across all ensemble
methods. ARF+HT achieves the highest overall average, closely followed by AUE+HT
21

andAWE+HT,withDWM+HTreachingthelowestamongHT-basedmethods. ForNB,
AUE leads, followed by AWE, ARF, and DWM. The results indicate that while ARF
consistentlydominatesonbothabruptandgradualsyntheticdriftscenarios,AUEproves
most effective on real-world data, underscoring the importance of dataset characteristics
| when | selecting an | ensemble-based | drift detection | method.   |           |
| ---- | ------------ | -------------- | --------------- | --------- | --------- |
|      |              |                | NB              |           | HT        |
|      |              | ARF AUE        | DWM AWE         | ARF AUE   | DWM AWE   |
|      | RT           | 0.83 0.73      | 0.65 0.76       | 0.88 0.74 | 0.69 0.77 |
a
|     | Sine a | 0.95 0.78 | 0.59 0.90 | 0.98 0.83 | 0.80 0.91 |
| --- | ------ | --------- | --------- | --------- | --------- |
|     | Mixed  | 0.97 0.68 | 0.56 0.87 | 0.97 0.78 | 0.68 0.89 |
a
|     | Aver | 0.92 0.73 | 0.60 0.84 | 0.94 0.78 | 0.72 0.86 |
| --- | ---- | --------- | --------- | --------- | --------- |
a
|     | RT  | 0.76 0.73 | 0.65 0.78 | 0.88 0.74 | 0.76 0.80 |
| --- | --- | --------- | --------- | --------- | --------- |
g
|     | Sine | 0.93 0.81 | 0.53 0.88 | 0.97 0.84 | 0.53 0.90 |
| --- | ---- | --------- | --------- | --------- | --------- |
g
|     | Mixed | g 0.96 0.70 | 0.53 0.84 | 0.96 0.79 | 0.54 0.87 |
| --- | ----- | ----------- | --------- | --------- | --------- |
|     | Aver  | 0.88 0.75   | 0.57 0.83 | 0.94 0.72 | 0.61 0.86 |
g
|     | ELE  | 0.81 0.88 | 0.70 0.74 | 0.82 0.89 | 0.71 0.75 |
| --- | ---- | --------- | --------- | --------- | --------- |
|     | CIC  | 0.36 0.70 | 0.37 0.64 | 0.63 0.87 | 0.77 0.75 |
|     | Aver | 0.59 0.79 | 0.54 0.69 | 0.73 0.88 | 0.74 0.75 |
r
Table 10.1: Comparisons of Ensemble-based Methods Combined With Two Base Learn-
ers
11 A Summary
As presented in Table 11, HT generally outperforms NB across most dataset categories
and detector families. However, a notable exception arises on real-world data streams,
where NB achieves equal or slightly superior performance to HT within both SPC and
window-based methods. This suggests that the advantage of a more expressive base
learner is not universal and depends on the nature of the data. Ensemble methods
consistently outperform both SPC and window-based detectors across all dataset types,
and their strongest results are achieved with HT, reinforcing that the choice of base
learner significantly impacts predictive accuracy under concept drift.
Focusingonsingle-detectorfamilies,EWMA+HTandEDDM+HTofferthebestover-
all SPC performance (≈ 0.69) and the best gradual-drift accuracy (≈ 0.60). For real-
world streams, NB paired with RDDM, FHDDM, EWMA, or EDDM achieves the high-
est SPC result of approximately 0.78. Within the window-based family, KSWIN+HT,
WSTD+HT,andD3+HTarejointlystrongestforabruptdrifts(≈ 0.61),whileWSTD+HT,
MDDM+HT, ADWIN+HT and D3+HT perform best on gradual drifts (≈ 0.60). On
real-world streams, all window-based methods paired with NB uniformly achieve the
top result of approximately 0.78. Overall, all window-based methods with HT yield
an identical aggregate performance of 0.68, with no single detector emerging as dom-
22

| Cat.     | Drift type | Learner | Best method             |
| -------- | ---------- | ------- | ----------------------- |
| SPC      | Abrupt     | HT      | FTDD                    |
| SPC      | Gradual    | HT      | EWMA/EDDM               |
| SPC      | Real-world | NB      | RDDM/FHDDM/EWMA/EDDM    |
|          | Overall    | HT      | EWMA/EDDM               |
| Window   | Abrupt     | HT      | KSWIN/WSTD/D3           |
| Window   | Gradual    | HT      | WSTD/MDDM/ADWIN/D3      |
| Window   | Real-world | NB      | FPDD/WSTD/MDDM/ADWIN/D3 |
|          | Overall    | HT      | WSTD/D3                 |
| Ensemble | Abrupt     | HT      | ARF                     |
| Ensemble | Gradual    | HT      | ARF                     |
| Ensemble | Real-world | HT      | AUE                     |
|          | Overall    | HT      | ARF                     |
Table 11.1: Best-performing drift detectors by category, drift type and base learner
inant. Among ensemble-based methods, ARF+HT achieves the strongest results on
both abrupt and gradual drift scenarios (≈ 0.94) and ranks best in overall aggregate
performance (≈ 0.83), while AUE+HT proves most effective on real-world data streams
(≈ 0.88). Overall, although SPC and window-based detectors remain competitive, par-
ticularly on real-world data with NB, the most reliable and consistent improvements
across all drift scenarios come from ensemble-based adaptation mechanisms, especially
ARF+HT.
12 Conclusions
Concept drifts are prevalent in today’s streaming applications where data distributions
and relationships change over time. They have significant consequences in many critical
domains, such as healthcare, banking, finance, cybersecurity, email spam and phishing,
IoT, sensor networks and recommendation systems. In these applications, drifts can
degrade the performance of decision models and increase the risk of incorrect classifi-
cations. Therefore, accurately identifying such drifts is crucial to prevent classification
models from deteriorating.
The aim of our study is to simplify the description of a broad range of learner-based
concept drift detection algorithms in order to enhance the comprehension of these com-
plexmethods. Thesealgorithmsareclassifiedintothreemaingroups, StatisticalProcess
Control (SPC) methods, windowing techniques and ensemble-based approaches. These
methods can operate in either active or passive modes and can be implemented in online
orblock-basedsettings. Wehavealsoconductedanextensiveevaluationandcomparison
23

of these detectors using both synthetic and real-world datasets to assess their perfor-
mance.
References
[1] Osama A.Mehdi et al. “Roadmap of Concept Drift Adaptation in Data Stream
Mining, Years Later”. In: IEEE Access PP (Jan. 2024), pp. 1–1. doi: 10.1109/
ACCESS.2024.3358817.
[2] Joao Paulo Papa Adriana Sayuri Iwashita. “An Overview on Concept Drift Learn-
ing”. In: IEEE Access (2019).
[3] SupriyaAgrahariandAnilKumarSingh.“ConceptDriftDetectioninDataStream
Mining:Aliteraturereview”.In:Journal of King Saud University - Computer and
Information Sciences 34.10, Part B (2022), pp. 9523–9540. issn: 1319-1578. doi:
https://doi.org/10.1016/j.jksuci.2021.11.006. url: https://www.
sciencedirect.com/science/article/pii/S1319157821003062.
[4] Gabriel Aguiar, Bartosz Krawczyk, and Alberto Cano. “A survey on learning from
imbalanced data streams: taxonomy, challenges, empirical study, and reproducible
experimental framework”. In: Machine Learning 113 (June 2023), pp. 1–79. doi:
10.1007/s10994-023-06353-6.
[5] M.Baena-Garcıaetal.“Earlydriftdetectionmethod”.In:International Workshop
on Knowledge Discovery from Data Streams (2006).
[6] R. S. M. Barros and S. G. T. C. Santos. “A large-scale comparison of concept
drift detectors”. In: Information Sciences 451-452 (2018), pp. 348–370. issn: 0020-
0255. doi: https://doi.org/10.1016/j.ins.2018.04.014. url: https:
//www.sciencedirect.com/science/article/pii/S0020025518302743.
[7] RobertoBarros,JuanGonzalezHidalgo,andDaniloCabral.“WilcoxonRankSum
Test Drift Detector”. In: Neurocomputing 275 (Jan. 2018), pp. 1954–1963. doi:
10.1016/j.neucom.2017.10.051.
[8] Roberto Barros and Silas Santos. “An Overview and Comprehensive Comparison
of Ensembles for Concept Drift”. In: Information Fusion 52 (Dec. 2019), pp. 213–
244. doi: 10.1016/j.inffus.2019.03.006.
[9] Roberto Barros et al. “RDDM: Reactive drift detection method”. In: Expert Sys-
tems with Applications 90 (Dec. 2017), pp. 344–355. doi: 10.1016/j.eswa.2017.
08.023.
[10] Barı¸s Bayram, Bilge K¨oro˘glu, and Mehmet G¨onen. “Improving Fraud Detection
and Concept Drift Adaptation in Credit Card Transactions Using Incremental
Gradient Boosting Trees”. In: 2020 19th IEEE International Conference on Ma-
chine Learning and Applications (ICMLA). 2020, pp. 545–550. doi: 10.1109/
ICMLA51294.2020.00091.
24

[11] Alessio Bernardo. Artificial and Real dataset with different concept drift type and
imbalance ratio. Version V1. 2020. doi: 10.7910/DVN/RKY6RD. url: https://
doi.org/10.7910/DVN/RKY6RD.
[12] A. Bifet and R. Gavalda. “Learning from Time-Changing Data with Adaptive
Windowing”. In: SDM (2007).
[13] D. Brzezinski and J. Stefanowski. “Accuracy Updated Ensemble for Data Streams
with Concept Drift”. In: vol. 6679. May 2011, pp. 155–163. isbn: 978-3-642-21221-
5. doi: 10.1007/978-3-642-21222-2_19.
[14] D. R. L. Cabral and R. S. M. Barros. “Concept drift detection based on Fisher’s
Exact test”. In: Information Sciences 442-443 (2018), pp. 220–234. issn: 0020-
0255. doi: https://doi.org/10.1016/j.ins.2018.02.054. url: https:
//www.sciencedirect.com/science/article/pii/S0020025518301403.
[15] Andreas Kassler Firas Bayram Bestoun S. Ahmed. “From concept drift to model
degradation: An overview on performance-aware drift detectors”. In: Knowledge-
Based Systems (2022).
[16] R. A. Fisher. “On the Interpretation of X2 from Contingency Tables, and the
Calculation of P”. In: Journal of the Royal Statistical Society 85.1 (1922), pp. 87–
94. issn: 09528385. url: http://www.jstor.org/stable/2340521 (visited on
11/12/2024).
[17] J. Gama et al. “A Survey on Concept Drift Adaptation”. In: ACM Computing
Surveys (CSUR) (2014).
[18] J. Gama et al. “Learning with Drift Detection”. In: Intelligent Data Analysis
(2004).
[19] Heitor M. Gomes et al. “Correction to: Adaptive random forests for evolving data
stream classification”. In: Mach. Learn. 108.10 (Oct. 2019), pp. 1877–1878. issn:
0885-6125. doi: 10.1007/s10994-019-05793-3. url: https://doi.org/10.
1007/s10994-019-05793-3.
[20] O¨mer G¨ozu¨a¸cik et al. “Unsupervised Concept Drift Detection with a Discrimina-
tive Classifier”. In: Proceedings of the 28th ACM International Conference on In-
formationandKnowledgeManagement (2019).url:https://api.semanticscholar.
org/CorpusID:207757814.
[21] O¨mer G¨ozu¨a¸cık and Fazli Can. “Concept learning using one-class classifiers for
implicit drift detection in evolving data streams”. In: Artif. Intell. Rev. 54.5 (June
2021), pp. 3725–3747. issn: 0269-2821. doi: 10.1007/s10462-020-09939-x. url:
https://doi.org/10.1007/s10462-020-09939-x.
[22] Ege Gulcan and Fazli Can. “Unsupervised concept drift detection for multi-label
data streams”. In: Artificial Intelligence Review 56 (July 2022). doi: 10.1007/
s10462-022-10232-2.
25

[23] Meng Han et al. “A survey of active and passive concept drift handling methods”.
In: Computational Intelligence 38.4 (2022), pp. 1492–1535. doi: https://doi.
org/10.1111/coin.12520. eprint: https://onlinelibrary.wiley.com/doi/
pdf/10.1111/coin.12520. url: https://onlinelibrary.wiley.com/doi/abs/
10.1111/coin.12520.
[24] Tegjyot S. Sethi Hanqing Hu Mehmed Kantardzic. “No Free Lunch Theorem for
concept drift detection in streaming data classification: A review”. In: Wiley In-
terdisciplinary Reviews: Data Mining and Knowledge Discovery (2019).
[25] Fabian Hinder, Valerie Vaquet, and Barbara Hammer. One or Two Things We
know about Concept Drift – A Survey on Monitoring Evolving Environments.2023.
arXiv: 2310.15826 [cs.LG]. url: https://arxiv.org/abs/2310.15826.
[26] Wassily Hoeffding. “Probability Inequalities for Sums of Bounded Random Vari-
ables”. In: Journal of the American Statistical Association 58.301 (1963), pp. 13–
30. issn: 01621459, 1537274X. url: http://www.jstor.org/stable/2282952
(visited on 10/22/2024).
[27] M. Hammami I. Khamassi M. Sayed-Mouchaweh and K. Gh´edira. “Discussion and
review on evolving data streams and concept drift adapting”. In: Evolving Systems
(2018).
[28] Meenal Jain, Gagandeep Kaur, and Vikas Saxena. “A K-Means clustering and
SVM based hybrid concept drift detection technique for network anomaly detec-
tion”. In: Expert Systems with Applications 193 (2022), p. 116510. issn: 0957-
4174. doi: https://doi.org/10.1016/j.eswa.2022.116510. url: https:
//www.sciencedirect.com/science/article/pii/S0957417422000112.
[29] BotaoJiaoetal.“DynamicEnsembleSelectionforImbalancedDataStreamsWith
Concept Drift”. In: IEEE Transactions on Neural Networks and Learning Systems
35.1 (2024), pp. 1278–1291. doi: 10.1109/TNNLS.2022.3183120.
[30] J. Zico Kolter and Marcus A. Maloof. “Dynamic Weighted Majority: AnEnsemble
Method for Drifting Concepts”. In: J. Mach. Learn. Res. 8 (Dec. 2007), pp. 2755–
2790. issn: 1532-4435.
[31] Bartosz Krawczyk et al. “Ensemble learning for data stream analysis: A survey”.
In: Information Fusion 37 (2017), pp. 132–156. issn: 1566-2535. doi: https://
doi.org/10.1016/j.inffus.2017.02.004. url: https://www.sciencedirect.
com/science/article/pii/S1566253516302329.
[32] N.LittlestoneandM.K.Warmuth.“TheWeightedMajorityAlgorithm”.In:Infor-
mation and Computation 108.2 (1994), pp. 212–261. issn: 0890-5401. doi: https:
//doi.org/10.1006/inco.1994.1009. url: https://www.sciencedirect.com/
science/article/pii/S0890540184710091.
[33] Jesu´s L´opez Lobo. Synthetic datasets for concept drift detection purposes. url:
https://doi.org/10.7910/DVN/5OWRGB. Harvard Dataverse.
26

[34] Jie Lu et al. “Data-driven decision support under concept drift in streamed big
data”. In: Complex and Intelligent Systems 6 (2020). doi: 10.1007/s40747-019-
00124-4.
[35] Jie Lu et al. “Learning under Concept Drift: A Review”. In: IEEE Transactions
on Knowledge and Data Engineering 31.12 (2019), pp. 2346–2363. doi: 10.1109/
TKDE.2018.2876857.
[36] Donia Malekian and Mahmoud Reza Hashemi. “An adaptive profile based fraud
detection framework for handling concept drift”. In: 2013 10th International ISC
Conference on Information Security and Cryptology (ISCISC). 2013, pp. 1–6. doi:
10.1109/ISCISC.2013.6767338.
[37] Colin McDiarmid. “Surveys in Combinatorics, 1989: On the method of bounded
differences”. In: 1989. url: https://api.semanticscholar.org/CorpusID:
116663483.
[38] Hassan Mehmood et al. “Concept Drift Adaptation Techniques in Distributed
EnvironmentforReal-WorldDataStreams”.In:Smart Cities (2021).url:https:
//api.semanticscholar.org/CorpusID:233623878.
[39] K.NishidaandK.Yamauchi.“DetectingConceptDriftUsingStatisticalTesting”.
In: Discovery Science, 10th International Conference, DS 2007 (2007).
[40] Yuri Thomas P. Nunes and Luiz Affonso Guedes. “Concept Drift Detection Based
onTypicalityandEccentricity”.In:IEEE Access 12(2024),pp.13795–13808.doi:
10.1109/ACCESS.2024.3355959.
[41] Sirvan Parasteh and Samira Sadaoui. “A Novel Probabilistic Approach for Detect-
ingConceptDriftinStreamingData”.In:Deep Learning Theory and Applications.
Ed. by Donatello Conte et al. Cham: Springer Nature Switzerland, 2023, pp. 173–
188. isbn: 978-3-031-39059-3.
[42] Sirvan Parasteh and Samira Sadaoui. “A Probabilistic Approach for Detecting
Real Concept Drift.” In: Proc. of 16th International Conference on Agents and
Artificial Intelligence-Volume 2, ICAART (2). 2024, pp. 301–311.
[43] SirvanParastehandSamiraSadaoui.“ARobustProbabilisticFrameworkforIden-
tifyingandEvaluatingConceptDriftinAbruptandGradualScenarios”.In:Agents
and Artificial Intelligence. Ed. by Ana Paula Rocha, Luc Steels, and Jaap van den
Herik. Springer Nature, 2025, pp. 353–367.
[44] Sirvan Parasteh, Samira Sadaoui, and Mohammad Sadegh Khosravani. “Detection
of Real Concept Drift Under Noisy Data Stream”. In: 2023 IEEE Symposium
Series on Computational Intelligence (SSCI). IEEE. 2023, pp. 1316–1321.
[45] A. Pesaranghader, H. Viktor, and E. Paquet. McDiarmid Drift Detection Methods
for Evolving Data Streams. 2018. arXiv: 1710.02030 [stat.ML].
27

[46] Ali Pesaranghader and Herna L. Viktor. “Fast Hoeffding Drift Detection Method
for Evolving Data Streams”. In: Machine Learning and Knowledge Discovery in
Databases. Cham: Springer International Publishing, 2016, pp. 96–111. isbn: 978-
3-319-46227-1.
[47] C. Raab, M. Heusinger, and F. Schleif. “Reactive Soft Prototype Computing for
Concept Drift Streams”. In: Neurocomputing (2020).
[48] GordonJ.Rossetal.“Exponentiallyweightedmovingaveragechartsfordetecting
conceptdrift”.In:PatternRecognitionLetters 33.2(2012),pp.191–198.issn:0167-
8655. doi: https://doi.org/10.1016/j.patrec.2011.08.019.
[49] Armin Sadreddin and Samira Sadaoui. “Chunk-based incremental feature learn-
ing for credit-card fraud data stream”. In: Journal of Experimental & Theoretical
Artificial Intelligence (2022), pp. 1–19. doi: 10.1080/0952813X.2022.2153277.
url: https://doi.org/10.1080/0952813X.2022.2153277.
[50] Bruno Henrique Schwengber et al. “Learning From Network Data Changes for
Unsupervised Botnet Detection”. In: IEEE Transactions on Network and Service
Management 19.1 (2022), pp. 601–613. doi: 10.1109/TNSM.2021.3109076.
[51] Eyad Elyan Scott Wares John Isaacs. “Data stream mining: methods and chal-
lenges for handling concept drift”. In: SN Applied Sciences (2019).
[52] Iman Sharafaldin, Arash Habibi Lashkari, and Ali A. Ghorbani. “Toward Gener-
ating a New Intrusion Detection Dataset and Intrusion Traffic Characterization”.
In: International Conference on Information Systems Security and Privacy. 2018.
url: https://api.semanticscholar.org/CorpusID:4707749.
[53] Andr´esL.Su´arez-Cetrulo,DavidQuintana,andAlejandroCervantes.“Asurveyon
machine learning for recurring concept drifting data streams”. In: Expert Systems
with Applications 213 (2023), p. 118934. issn: 0957-4174. doi: https://doi.
org/10.1016/j.eswa.2022.118934. url: https://www.sciencedirect.com/
science/article/pii/S0957417422019522.
[54] N.V. Chawla T.R. Hoens R. Polikar. “Learning from streaming data with concept
drift and imbalance: an overview”. In: Progress in Artificial Intelligence (2012).
[55] Maurras Ulbricht Togbe et al. “Anomalies Detection Using Isolation in Concept-
Drifting Data Streams”. In: Computers 10.1 (2021). issn: 2073-431X. doi: 10.
3390/computers10010013. url: https://www.mdpi.com/2073-431X/10/1/13.
[56] H. Wang et al. “Mining Concept-Drifting Data Streams Using Ensemble Classi-
fiers”. In: (July 2003). doi: 10.1145/956750.956778.
[57] Geoffrey I. Webb et al. “Understanding Concept Drift”. In: ArXiv (2017).
[58] Frank Wilcoxon. “Individual Comparisons by Ranking Methods”. In: Biometrics
Bulletin 1.6 (1945), pp. 80–83. issn: 00994987. url: http://www.jstor.org/
stable/3001968 (visited on 10/28/2024).
28

[59] Q. Xiang et al. “Concept Drift Adaptation Methods under the Deep Learning
Framework: A Literature Review”. In: Applied Sciences 13 (May 2023), p. 6515.
doi: 10.3390/app13116515.
[60] Lingyu Zhang, Jiabao Zhao, and Wei Li. “Online and Unsupervised Anomaly De-
tection for Streaming Data Using an Array of Sliding Windows and PDDs”. In:
IEEE Transactions on Cybernetics 51.4 (2021), pp. 2284–2289. doi: 10.1109/
TCYB.2019.2935066.
[61] Indre Zˇliobaite. “Learning under Concept Drift: an Overview”. In: ArXiv (2010).
29