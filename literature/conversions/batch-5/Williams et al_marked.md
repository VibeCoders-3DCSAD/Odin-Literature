---
conversion_metadata:
  converted_at: "2026-07-21T09:25:21Z"
  converter_tool: "markitdown"
  converter_version: "0.1.6"
  source_pdf: "Williams et al.pdf"
  source_pdf_sha256: "97b41e0e591d941696dfe7091c5dc350101902404a5e38c6778e42a1326192a7"
  page_count: 9
  markdown_char_count: 98532
---

<!-- PAGE-AWARE EXTRACTION (via pdfminer.six) -->

<!-- PAGE 1 -->

Received 8 August 2023, accepted 2 September 2023, date of publication 20 September 2023, date of current version 4 October 2023.

Digital Object Identifier 10.1109/ACCESS.2023.3317791

Anomaly Detection in Multi-Seasonal
Time Series Data

ASHTON T. WILLIAMS, RYAN E. SPERL, AND SOON M. CHUNG , (Life Member, IEEE)
Department of Computer Science and Engineering, Wright State University, Dayton, OH 45435, USA

Corresponding author: Soon M. Chung (soon.chung@wright.edu)

This work was supported in part by the Air Force Research Laboratory (AFRL)/Defense Associated Graduate Student Innovators (DAGSI)
Research Fellowship.

ABSTRACT Most of today’s time series data contain anomalies and multiple seasonalities, and accurate
anomaly detection in these data is critical to almost any type of business. However, most mainstream
forecasting models used for anomaly detection can only incorporate one or no seasonal component into their
forecasts and cannot capture every known seasonal pattern in time series data. In this paper, we propose a new
multi-seasonal forecasting model for anomaly detection in time series data that extends the popular Seasonal
Autoregressive Integrated Moving Average (SARIMA) model. Our model, named multi-SARIMA, utilizes
a time series dataset’s multiple pre-determined seasonal trends to increase anomaly detection accuracy
even more than the original SARIMA model. Our experimental results demonstrate the higher accuracy
of multi-SARIMA when multiple seasonalities are present than most models with one or no seasonal
component, although with more processing time.

INDEX TERMS Anomaly detection, moving average, multiple seasonalities, multi-SARIMA, time series
data, SARIMA.

I. INTRODUCTION
Nowadays there are many data sources, such as sensors,
producing time series data, which is a sequence of data
points indexed in time order. These data points typically
consist of successive measurements made from the same
source over a fixed time interval and are used to track change
over time [16]. Anomalies (i.e., outliers) are data points that
significantly deviate from their expected value [4], and early
detection of anomalies is important to mitigate these harmful
effects, particularly in critical systems where failure can be
catastrophic [3]. For example, a hospital can detect abnormal
body signals of its patients and notify professionals before it’s
too late.

For anomaly detection in time series data, forecasting mod-
els are used to compare forecasted values to actual values to
determine if a point is anomalous. While some deviation is
expected when comparing a forecasted value to its real coun-
terpart, if the predicted value deviates significantly from the
actual value, then the data point is most likely an anomaly [2].

The associate editor coordinating the review of this manuscript and

approving it for publication was Chao-Yang Chen

.

Some time series data contain a seasonality, which is a
pattern that repeats at specific time intervals [1]. For exam-
ple, CPU usage rate of a server may have a daily seasonal
trend. The popular Seasonal Autoregressive Integrated Mov-
ing Average (SARIMA) forecasting model [18] can represent
a seasonal trend in its forecasting of time series data. How-
ever, SARIMA can implement only one seasonal trend in
its forecasting [1]. Allowing only one seasonal trend is a
major limitation because some time series data contain more
than one seasonality [7]. For example, New York City (NYC)
taxi traffic data has both daily and weekly seasonal trends.
Thus, utilizing all known seasonal effects in time series data
can play an important role in data forecasting and anomaly
detection [1].

In this paper, we propose a new multi-seasonal model,
named multi-SARIMA, for anomaly detection in time series
data that extends the SARIMA model by allowing mul-
tiple seasonal components. The multi-SARIMA utilizes a
dataset’s multiple pre-determined seasonal trends to increase
anomaly detection accuracy. To compare with our multi-
SARIMA, we also implemented other anomaly detection
models, including Moving Average (MA), Seasonal Inte-
the original SARIMA,
grated Moving Average (SIMA),

106456

2023 The Authors. This work is licensed under a Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 License.
For more information, see https://creativecommons.org/licenses/by-nc-nd/4.0/

VOLUME 11, 2023

---

<!-- PAGE 2 -->

A. T. Williams et al.: Anomaly Detection in Multi-Seasonal Time Series Data

Numenta’s Hierarchical Temporal Memory (HTM) [9], [10],
and another multi-seasonal model TBATS which stands for
Trigonometric seasonality, Box-Cox transformation, ARMA
errors, Trend and Seasonal components [8]. Additionally,
we implemented the two-step approach proposed in [2] with
our multi-SARIMA as the second step. The multi-SARIMA
produced better anomaly detection results than the original
SARIMA for every dataset we tested and, in most cases,
outperformed HTM and TBATS.

This paper is organized as follows: Section II defines our
anomaly labeling method and explains the existing anomaly
detection models used in this paper. Section III explains our
proposed multi-SARIMA model and the two-step approach
we proposed in [2] with our multi-SARIMA model as the
second step. Section IV describes the datasets used for testing
and their properties, the Multiple Seasonal-Trend decomposi-
tion using Locally Estimated Scatterplot Smoothing (Loess)
(MSTL) decomposition [7] we used to verify the seasonal
trends in each dataset, and the differencing used on our
datasets. Section V describes the implementation of different
models, single-step and two-step test results, and compar-
isons based on the detection accuracy and runtime. Section VI
contains our final thoughts with a conclusion and possible
future research topics.

II. ANOMALY LABELING AND EXISTING DETECTION
METHODS
A. ANOMALY LABELING
Time series anomaly detection models use a calculated
numeric metric called an anomaly score to determine if a data
point is an anomaly or not [4]. In our case, we determine
the anomaly score using the error between the predicted
value and the actual value. If the anomaly score exceeds the
threshold, the data point is labeled as an anomaly [10].

In some cases, the threshold is fixed, however, a fixed
threshold is not suitable in our case because the variance can
change over time. The dynamic threshold must be calculated
using sample metrics since we cannot assume the detector
has access to the entire dataset as values are collected in
real-time, such that only past values are available. For our
dynamic threshold, we used the mean absolute deviation
(MAD) calculated as:

MAD = median (|Xi − median (X )|)

(1)

where X is the portion of data values in a rolling sample
window to limit the impact of older data values [2]. Unlike the
mean and standard deviation, MAD is robust when anomalies
are present in the data sample, and there is no distortion unless
at least a half of the sample is composed of anomalies [2], [5].
We then multiply the threshold with a constant to adjust the
sensitivity of our anomaly detection, resulting in our anomaly
detection metric defined as:

AnomalyDetected t = |εt | > |s ∗ MAD|
(2)
where εt is the anomaly score measured at time t, and s is the
sensitivity constant [2].

VOLUME 11, 2023

B. MOVING AVERAGE (MA)
Time series data is usually produced by a monitoring
device and can range from spatial data in medical imag-
ing to sequential data in network security [2], [12]. Let
X = {X1, X2, . . . , Xt } be a one-dimensional time series with
evenly spaced discrete time where Xt is a value X at time t
[2], [12]. Values that are before t are considered its lags, such
that Xt−i is the value i steps back in the time series [2], [12].
The backshift operator B yields the lags in a time series and
is defined as:

BiXt = Xt−i

(3)

for all t > i [2], [12].

The moving average (MA) model is a simple and common
approach to forecasting time series data. The moving average
of order q, denoted as MA(q), predicts the value X at time t
as:

Xt = µ + εt +

q
X

i=1

biBiεt

(4)

for all t > q, where εt is the white noise error at time t, µ
(cid:9) is the q
is the mean of the series, and b = (cid:8)b1, b2, . . . , bq
parameters for the model [2], [12].

C. SEASONAL INTEGRATED MOVING AVERAGE (SIMA)
The seasonal integrated moving average (SIMA) model is
an extension of the MA model where one seasonal com-
ponent is considered for the data forecast. SIMA denoted
as SIMA (d, q)
m, forecasts using MA(q) with a seasonally
differenced time series. Differencing is used to eliminate
trends that are apparent in a dataset to make the data stationary
[2]. Differencing is done by replacing every value with the
difference between itself and its first lag [2]. Let ∇X =
{X1, X2, . . . , Xt } be a first-order differenced time series, such
that

∇Xt = Xt − Xt−1 = (1 − B) Xt

(5)

for all t > 1 [2]. The order of differencing can be repre-
sented by a symbol d, such that ∇d Xt denotes the dth-order
differenced time series. For example, when d = 2, it is the
second-order differenced time series [2]. Therefore, a differ-
enced time series can be expressed more generally as:

∇d Xt = (1 − B)d Xt

(6)

for all t > d [2]. However, no amount of differencing
will remove a seasonal trend from data. Seasonal trends can
be eliminated by seasonal differencing, which differences
against the previous season instead of the first lag [2]. Let
∇d
mX be a seasonally differenced time series, where m is the
period of the seasonal trend, then it is defined as:

mXt = (1 − Bm)d Xt
∇d

for all t > d ∗ m [2].

(7)

106457

---

<!-- PAGE 3 -->

D. SEASONAL AUTOREGRESSIVE INTEGRATED MOVING
AVERAGE (SARIMA)
The seasonal autoregressive integrated moving average
(SARIMA) denoted as SARIMA(p, d, q)m is an extension of
the autoregressive integrated moving average model denoted
as ARIMA(p, d, q) by incorporating a seasonal component
into its forecasting model. Both models are based on a com-
bination of the autoregressive model (AR) and the moving
average (MA) model. The autoregressive model predicts X
using its most recent lags [2]. Let AR(p) be an autoregressive
model of order p that predicts the value of X at time t as:

Xt = c + εt +

p
X

i=1

aiBiX t

(8)

for all t > p, where a = {a1, a2, . . . , ap} is the p parameters
for the model [2], [12]. Let ARMA(p, q) be an autoregressive
moving average model (ARMA), where p represents the
order of AR and q represents the order of MA, defined as:

Xt = c + εt +

p
X

i=1

aiBiX t +

q
X

j=1

biBiεt

(9)

for all t > max{p, q} [2], [12]. The ARIMA(p, d, q) model
predicts X by modeling the differenced series ∇d X with an
ARMA(p, q) model [2]. The SARIMA(p, d, q)m model pre-
dicts X by modeling the seasonally differenced series ∇d
mXt
with an ARMA(p, q) model:

Xt = c + εt + (

p
X

aiBi∇d

mX t ) + (

q
X

j=1

biBiεt )

(10)

where Xt = ∇d
mBmXt [2]. Although the
i=0 ∇i
SARIMA model is one of the best and most common time
series forecasting models, it is unable to incorporate more
than one seasonal trend into its forecasting.

i=1
mXt + Pd−1

E. HIERARCHICAL TEMPORAL MEMORY (HTM)
Hierarchical Temporal Memory (HTM)
a neural
is
network-based machine learning algorithm derived from
neuroscience that models spatial and temporal patterns in
streaming data [9]. HTM works by simulating how the
neocortex works in the human brain [13]. It is versatile and
tolerable to noisy data and can detect even the most subtle
anomalies, resulting in a low false positive rate with most
real anomalies detected [3].

The learning of HTM can be broken down into three
main parts: The first part is the encoder and the Sparse
Distributed Representations (SDRs) [3]. SDRs help explain
how brains can make semantic generalizations [13]. SDRs
are represented by vectors that contain thousands of bits,
and the encoder gives the bits meaning by encoding them to
represent the properties of a representation [13]. The encoded
properties of two SDRs are compared, and if they have 1-bit
in the same location, then they share some similarities [13].
The more 1-bits the two SDRs share, the more semantically
similar the two representations are [13].

A. T. Williams et al.: Anomaly Detection in Multi-Seasonal Time Series Data

The second part is the spatial pooler. The spatial pooler is
responsible for learning spatial patterns present in the data.
It starts by taking in a fixed number of encoded SDR bits
then assigns a layer containing columns [13]. Each column
has a set of potential synapses, a connection to the previous
layer representing a subset of the input bits [13]. Connec-
tions between the layers are then determined based on the
comparison between performance values and a performance
threshold [13]. The active synapses of each column are then
determined based on how many connected columns exist
[13]. As more data are collected, the spatial pooler determines
how many connected synapses of each column overlap with
the input SDR bits, and activates columns with the most
overlap [3]. Only active columns update their connections,
then the network boosts or hinders columns accordingly to
prevent columns from being too dominant [2].

The third and final part of the HTM learning model is the
temporal memory. Temporal memory does two things: learns
the sequences of SDRs produced by the spatial pooler and
makes predictions [13]. The temporal memory establishes
connections between cells in the spatial pooler’s columns,
then learns the connections between cells that reside in the
same layer [13]. An active cell forms connections to other
cells that were just active. This way, the cells can predict when
they will likely become active by referring to their current
connections [13].

HTM also calculates its own anomaly score by measuring
the deviation between its predicted input and the actual input
[9]. The anomaly score at time t denoted as st , is given as:

st = 1 −

π (Xt−1) ∗ a(Xt )
|a(Xt )|

(11)

where a(Xt ) is the sparse encoded value of the input at time t,
|a(Xt )| is the total number of 1-bits in a(Xt ), and π (Xt−1) is
the internal prediction of a(Xt ) [10]. The anomaly score will
be 0 if the current input is perfectly predicted or 1 otherwise
[9]. To increase the anomaly detection accuracy, a short-term
average of the prediction errors is computed, then a threshold
is applied to the Gaussian tail probability to determine if
a data point is truly an anomaly [10]. This second step in
determining the anomaly score is the compliment of the tail
probability and is defined as the anomaly likelihood:

Lt = 1 − Q(

µ′

t − µt
σt

)

(12)

Pi=W ′−1
i=0

st−i

j

t =

where µ′
, µt is the mean of the sample of past
anomaly scores, σt is the standard deviation of the sample of
past anomaly scores, µ’t is the short-term average, Q is the
Gaussian tail probability function, and W ′ is a window for a
short term moving average [9], [10].

F. TBATS
The Trigonometric seasonality, Box-Cox transformation,
ARMA errors, Trend and Seasonal components model,
denoted as TBATS, is a forecasting model for complex
time series that can include multiple seasonal periods,

106458

VOLUME 11, 2023

---

<!-- PAGE 4 -->

A. T. Williams et al.: Anomaly Detection in Multi-Seasonal Time Series Data

high-frequency seasonality, non-integer seasonality, and dual
calendar effects [8]. TBATS is currently one of the best
multi-seasonal time series forecasting models and is the
most common [1]. It utilizes a framework that incorporates
Box-Cox transformations, Fourier representations with time-
varying coefficients, and ARMA error correction [8]. The
TBATS model requires pre-specified seasonal periods that are
then modeled by a trigonometric representation based on the
Fourier series [1], [11].

TBATS is an extension of the Box-Cox transformation,
ARMA errors, Trend, and Seasonal components (BATS)
model, where the addition of trigonometric seasonality cre-
ates a more flexible parsimonious approach [8]. BATS,
however, is an extension of exponential smoothing methods
that combine its other components like Box-Cox transfor-
mations and ARMA errors to produce a better forecasting
model [15]. The exponential smoothing in BATS utilizes the
Holt-Winters method that handles time series with a trend
and a single seasonality [8], [15]. The exponential smooth-
ing works by having future values be weighted averages of
past values [15]. The Box-Cox transformation in the model
stabilizes the variance and mean over time, making the time
series stationary. ARMA errors in the model are applied to the
residuals to capture any leftover information [15]. The trend
captures long-term changes in the mean. Lastly, the seasonal
component captures a time series’ periodical variation [15].
The BATS model was improved to forecast time series
with multiple seasonal components with the addition of
trigonometric seasonality as well as updated versions of some
methods used in BATS to create the TBATS model [8],
[15]. The trigonometric seasonality in TBATS represents each
seasonal component in a time series as a trigonometric repre-
sentation based on the Fourier series [8], [15]. This addition
allows the model to fit multiple, larger, and non-integer sea-
sonal components with less run-time than the original BATS
model [15].

The BATS model can be represented as:

y(λ )
t = lt−1 + φbt−1 +

T
X

s(i)
t−mt

+ dt

i=1
αlt = lt−1 + φbt−1 + dt
bt = ϕbt−1 + βdt

dt =

p
X

i=1

φidt−1 +

q
X

i=1

θiet−i + et

(13)

(14)
(15)

(16)

t

where y(λ )
is the Box-Cox transformed time series at time
t, s(i)
is the ith seasonal component, lt is the local level at
t
time t, bt
is the trend with damping at time t, dt
is the
ARIMA(p, q) process, et is white noise, φ and θ are the
ARIMA(p, q) coefficients, φ is the trend damping, α and β
are the smoothing, T is the amount of seasonalities, λ is the
Box-Cox transformation, and mi is the length of the ith sea-
sonal period [8], [11]. The BATS model is then extended by
adding the trigonometric seasonal model and is represented

as seasonal components based on the Fourier series:

s(i)
t =

ki
X

s(i)
j,t

j=1
j,t−1 cos ω(i)
= s(i)
j,t−1 sin ω(i)
= −s(i)

j

j

+ s

∗(i)
j,t−1 sin ω(i)
j,t cos ω(i)
∗(i)
+ s

j

j

+ γ (i)

1 dt
+ γ (i)
2 dt

s(i)
j,t
∗(i)
s
j,t

(17)

(18)

(19)

and γ (i)
2

where γ (i)
is
1
the amount of harmonics for the ith seasonal period, and
ω(i)
j

are the smoothing parameters, ki

= 2π j/mi [8], [11].

III. PROPOSED DETECTION METHODS
A. MULTI-SARIMA
Most forecasting models today include at most one sea-
sonal component, and this unnecessary restriction only
to take full
hinders their potential. Allowing a model
advantage of every known seasonal pattern in a dataset
gives more options and possibilities for it to perform bet-
ter. Our proposed model, named multi-SARIMA, extends
the original SARIMA(p, d, q)m model and is denoted as
× (p2, d2, q2)m2. It predicts X by
SARIMA(p1, d1, q1)m1
modeling the seasonal differenced series ∇d2
m2X with two
SARIMA(p, d, q)m models:
a1,iBm1i(cid:17)
(cid:16)Xpi

Xt =

Xt

∇d2
m2

+

−

+

+

∇d2
m2
a2,iBm2i(cid:17)
Xp1
i=1

i=1
(cid:16)Xp2
i=1
(cid:16)Xp2
j=1
(cid:16)Xq1
b1,iBm1i(cid:17)
i=1
(cid:16)Xq2
Xq1
j=1
i=1
m2 Xt +Pd2−1

∇d2
m2

Xt
a1,ia2,jBm1i+m2j(cid:17)

εt +

(cid:16)Xq2
i=1

b1,ib2,jBm1i+m2j(cid:17)

Xt + εt

∇d2
m2
b2,iBm2i(cid:17)
εt

εt

(20)

where Xt = ∇d2
i=0 Bm2∇i
Xt , m1 is the shorter sea-
m2
sonal period, m2 is the longer seasonal period, d2 is the order
of differencing, a1 is the p parameters for the shorter period,
b1 is the q parameters for the shorter period, q1 is the seasonal
MA order of the shorter period, p1 is the seasonal AR order
for the shorter period, a2 is the p parameters for the longer
period, b2 is the q parameters for the longer period, q2 is the
seasonal MA order of the longer period, and p2 is the seasonal
AR order for the longer period. The multi-SARIMA equation
was derived by extending the original SARIMA equation.
The multi-SARIMA equation contains seasonal AR and MA
terms for individual season lengths m1 and m2 followed by
additional terms that account for the combination of the two
seasonal trends, and the backshift operator being scaled by the
season length. We also included additional factors to account
for the nonseasonal trend (p, d, q) in the multi-SARIMA.
From there, we distribute the factors and solve for the lone Xt
to get the final equation depicted above. We concluded that
we only need to difference using d2 and m2 since differencing
over the longer seasonal trend captures both seasonalities and
makes the data stationary. We set d1 = 0 since we difference

VOLUME 11, 2023

106459

---

<!-- PAGE 5 -->

the data and obtain a stationary version using d2, eliminating
d1 from appearing in the multi-SARIMA equation.

In our approach, the first model is trained on three itera-
tions of the shorter seasonal trend, while the second model
is trained on three iterations of the longer seasonal trend.
From the first model, we obtain the seasonal and non-seasonal
autoregressive and moving average parameters, the residuals,
and the constant. From the second model, we obtain just
the seasonal autoregressive and moving average parameters.
During the prediction, we apply the values from both models
to the multi-SARIMA equation to get the prediction X at
time t.

We expect the multi-SARIMA model to perform well,
compared to other models, when it is used with datasets that
contain two meaningful seasonal trends. If a dataset doesn’t
have meaningful seasonal patterns,
the multi-SARIMA
model is not expected to perform better. If a dataset con-
tains two seasonal trends, but they are insignificant, then the
multi-SARIMA model is not guaranteed to perform better.

Better performance entails that the multi-SARIMA model
has higher anomaly detection accuracy, meaning a higher
true positive rate with a lower false positive rate. With this
higher precision, however, we also expect the runtime of the
multi-SARIMA to be somewhat longer than those of other
models. This is because the multi-SARIMA model requires
more fitting and learning than other models as it uses two
different models and learns over two seasonal periods.

B. TWO-STEP APPROACH
The two-step approach for anomaly detection was initially
proposed by us in [2]. The algorithm consists of a simpler
model that can label data fast with less accuracy and a more
complex model that can label data accurately but requires
more time [2]. In the two-step approach, the first step does
the initial labeling with the faster but less accurate model,
then the second step verifies the first step’s labels with the
slower but more accurate model [2]. The first model must
pick up as many true positives as possible, then the second
step denies most of its false positives and verifies its true
positives [2]. So, this combined approach is limited to the true
positive rate of the first model but reduces the false positive
rate [2]. In the worst case, the first model finds every data
point anomalous, causing the second step to verify every data
point in the dataset [2]. The runtime of the two-step is at best
slightly slower than the first model and at worst slightly faster
than the second model.

Although the two-step approach is not new by itself,
using our multi-SARIMA as the second step in the two-step
approach is. Since we expect our multi-SARIMA to perform
better than other models, when it is used with datasets that
contain two meaningful seasonal trends, we also expect our
multi-SARIMA to perform well when it is used as the second
step in the two-step approach. For the two-step approach,
better results entail maintaining the true positive rate of first
step model while significantly reducing its false positive rate.

A. T. Williams et al.: Anomaly Detection in Multi-Seasonal Time Series Data

TABLE 1. Overview of the datasets.

For our experiments, we used the MA and SIMA models
as our first step to create the initial labeling, then verified
the labels with SARIMA, our multi-SARIMA, and TBATS.
We denote a combination of two models used in the two-step
approach as ‘first step + second step’. For example, a two-
step approach that uses MA as the first step and SARIMA as
the second step is denoted as MA + SARIMA.

IV. DATASETS
We evaluated all models on three different datasets. Two
datasets are from the Numenta Anomaly Benchmark (NAB),
a collection of labeled, univariate, real-world time series data
[6]. The third dataset is a synthetic time series dataset we
created using our data generation tool. Since we are focused
on multi-seasonal anomaly detection in time series data,
the three datasets contain two meaningful seasonal trends,
numerous hand-labeled anomalies, and enough data points to
train and test models on. A general summary of each dataset
is given in Table 1. We used a smaller version of the HotGym
dataset as one anomaly occurred within the first three weeks
of the data causes training issues with some models.

A. MSTL SEASONAL DECOMPOSITION
Since our multi-SARIMA model utilizes two seasonal com-
ponents, we should confirm that our test datasets contain two
meaningful seasonal trends. For that purpose, we used Mul-
tiple Seasonal-Trend decomposition using Locally Estimated
Scatterplot Smoothing (Loess) (MSTL) [7]. There are a few
multi-seasonal time series decomposition methods available,
including Facebook’s Prophet, TBATS, and Seasonal-Trend
Decomposition using Regression (STR); however, we chose
MSTL because it produces the lowest root mean squared
error, is robust to outliers, has the smallest execution time,
and is easy to use as it requires minimal parameters [7], [14].
MSTL decomposes an additive time series into a trend
component, given seasonal components, and a residual com-
ponent [7], [14]. MSTL is an extension of the Seasonal-Trend
decomposition using Loess (STL) model as STL is only able
to decompose time series with one seasonal component [7],
[14]. Loess is a scatterplot smoothing technique that fits a
curve to a scatterplot to determine the degree of the polyno-
mial [14]. STL applies Loess to various transformations of the
given time series and then extracts the trend and one seasonal
component [14]. MSTL extracts each known seasonal com-
ponent in a time series using STL one by one [7], [14]. MSTL

106460

VOLUME 11, 2023

---

<!-- PAGE 6 -->

A. T. Williams et al.: Anomaly Detection in Multi-Seasonal Time Series Data

FIGURE 1. MSTL decomposition of the NYC Taxi dataset for one week of
data. The top graph depicts the dataset’s daily seasonal trend while the
bottom graph depicts its weekly seasonal trend with the weekend
highlighted in red.

FIGURE 2. MSTL decomposition of the Synthetic Dataset for one week of
data. The top graph depicts the dataset’s daily seasonal trend while the
bottom graph depicts its weekly seasonal trend with the weekend
highlighted in red.

first orders the given seasonal periods from shortest to longest
to avoid shorter seasonal periods from being interlaced with
the longer seasonal periods [7]. MSTL then applies STL
iteratively on each identified seasonal period [7]. The MSTL
additive decomposition of a time series can be defined as:
t + · · · + Sn

t + Tt + Rt
where S1
t denotes the seasonal components,
t
Tt denotes the trend, and Rt denotes the remainder [7].
We used Python’s statsmodels MSTL package on a Linux
virtual machine to perform the MSTL decomposition on our
datasets as depicted in Fig. 1–3.

Xt = S1
, S2
t

, . . . , Sn

t + S2

(21)

Fig. 1 depicts one week of MSTL decomposition on the
NYC taxi dataset, where the vertical axis represents the
smoothing for the seasonal component given. The seasonality
in the data follows a typical workweek and makes sense,
considering that the original data represents taxi passengers
in New York City. The daily trend is very low early in the
morning, then has spikes before midday since everyone is
trying to get to work, a dip around noon since no one is out
and about, the highest spikes in the afternoon when everyone
is heading home or traveling around the city, then ends with
very a low dip late at night since everyone is at home. The
weekly trend follows a typical workweek with the weekdays
maintaining the same taxi usage pattern until the weekend
showing a different pattern and higher spikes during later
hours.

Fig. 2 depicts one week of MSTL decomposition on our
Synthetic dataset. We generated our synthetic data to simulate
a typical work schedule. The daily trend shows that the data
values tend to be very low early in the morning, then has
a spike before midday, a small dip around noon, another
spike in the afternoon, and ends with very a low dip late at
night. The weekly trend shows that the trend is consistent
throughout the weekdays, then shifting to having lower values
during the weekend.

Fig. 3 depicts one week of MSTL decomposition on the
HotGym dataset. The seasonality in the data follows a typical

FIGURE 3. MSTL decomposition of the HotGym dataset for one week of
data. The top graph depicts the dataset’s daily seasonal trend while the
bottom graph depicts its weekly seasonal trend with the weekend
highlighted in red.

workweek and makes sense, considering that the original data
represents a gym’s energy consumption in Australia. The
daily trend shows that the data values tend to have a small
spike at midnight and then are very low early in the morning
until midday where there is the highest spike during the
hottest and busiest time of the day, then decreases back down
for the rest of the day as the sun goes down and people go
home. The weekly trend shows that throughout the weekdays,
the trend seems to be somewhat consistent as people tend to
visit the gym regularly during the week, until the weekend
that has no high spikes but very low dips as not many people
are going to the gym or it is closed during different hours.

B. DIFFERENCING
For the differencing of our test datasets in order to make
them stationary, we decided to use seasonal differencing since
they contain apparent seasonal trends, specifically daily and
weekly seasonalities. So, we differenced using first-order
seasonal differencing with a period of one week. This cap-
tures both the daily and weekly seasonal trends and produces

VOLUME 11, 2023

106461

---

<!-- PAGE 7 -->

TABLE 2. Single-step experimental results.

A. T. Williams et al.: Anomaly Detection in Multi-Seasonal Time Series Data

dataset. Since there are a very small number of anomalies
within a large number of data points in each dataset, compar-
ing performance based on accuracy percentage is ineffective
as a model that never labels any data point as anomalous
would achieve more than 90% accuracy [2]. Instead, we focus
on which models produce the most true positives with the
lowest number of false positives. This means, the best models
would be able to label all anomalies correctly while not label-
ing other non-anomalous data points as anomalies. Table 2
shows the final single-step results of all models, and Table 3
shows the final two-step results, where TP is the number of
true positives, FP is the number of false positives, and FN is
the number of false negatives.

A. SINGLE-STEP EXPERIMENTAL RESULTS
For our single-step experimental results shown in Table 2,
our multi-SARIMA model had the highest number of true
positives for every dataset while maintaining fewer false
positives than the SARIMA model for every dataset, although
with longer runtime. Our multi-SARIMA had either the best
or second-best results for every dataset.

The multi-SARIMA had the highest runtime compared to
other models because the multi-SARIMA is the only model
that combines the results from two models which train over
the two seasonal periods of one day and one week, respec-
tively. Since every other seasonal model but TBATS is limited
to one seasonal trend, they are trained over the period of one
day as that is their stronger seasonality. Training two models
and having one training over a week required the extra time
but produced better results. Specifically, the runtime of the
multi-SARIMA on the NYC Taxi dataset was unexpectedly
long. This is because the NYC Taxi dataset is the only dataset
with a data point every 30 minutes instead of every hour,
causing the 3-week training data to contain a large amount
of data for the models to train on. The other multi-seasonal
model, TBATS, was also slow and had the second longest
runtime for every dataset. TBATS may be a more refined
model, but it still requires more time since that is the nature
of learning multiple seasonal patterns.

Our multi-SARIMA was the only model that achieved
the same number of true positives as HTM for the NYC
Taxi dataset and outperformed every model for the HotGym

FIGURE 4. NYC Taxi dataset after first-order seasonal differencing with a
period of 1 week. Anomalies are depicted by the red lines.

stationary data. Fig. 4 depicts our NYC Taxi datasets after the
first-order seasonal differencing was applied. The beginning
of the graph has a flat line because the first week has no prior
data to difference against [2].

V. EXPERIMENTAL RESULTS
To properly compare our multi-SARIMA model, we used
existing forecasting models MA, SIMA, SARIMA, TBATS,
and HTM. MA, SIMA, SARIMA, TBATS, and our pro-
posed multi-SARIMA were implemented in Python 3.8.5 on
a Windows 10 computer with an Intel i7 8-core processor
operating at 3.80 GHz, 16 GB of memory, and a 1 TB SSD.
Numenta’s HTM algorithm was implemented on the same
machine, using Python 2.7. The optimal parameters for each
model were determined by a grid search, and we compared
the best performances of all models in this section. We used
open-source python libraries provided by their authors for
our implementations of HTM and TBATS. For MA, SIMA,
and SARIMA we used Python’s statsmodels package. For the
two-step approach, we used MA and SIMA as the first step,
and SARIMA, TBATS, and our proposed multi-SARIMA as
the second step.

All models were trained on the first three weeks of the data,
then evaluated on the remaining data. We made sure there
were no anomalies present in the training portion of each

106462

VOLUME 11, 2023

---

<!-- PAGE 8 -->

A. T. Williams et al.: Anomaly Detection in Multi-Seasonal Time Series Data

TABLE 3. Two-step experimental results.

dataset. The multi-SARIMA doubled the true positive rate
of HTM and TBATS for the HotGym dataset while still
maintaining the second lowest false positive rate among all
models.

Expectedly, the two multi-seasonal models performed the
best for the Synthetic dataset. Most models detected all five
anomalies, but TBATS and multi-SARIMA did so with under
ten false positives. HTM performed very poorly with this
dataset, and we think that is because the dataset was created
using randomness, throwing off the learning of HTM.

Notably, TBATS had either the same or higher true posi-
tive rate than the original SARIMA for every dataset, while
maintaining a lower false positive rate.

B. TWO-STEP EXPERIMENTAL RESULTS
For our two-step experimental results shown in Table 3, all
two-step algorithms, each of which uses a combination of two
models, have less false positives than their standalone first
step results shown in Table 2, except for MA + SARIMA
for the Synthetic dataset which produced the same results
as MA. This is because MA’s false positives were already
very low for that dataset. Also, most two-step algorithms have
significantly less false positives than their standalone second
step results shown in Table 2, but have less true positives
because they are limited to the true positive rate of the first
step.

Although with more processing time, the multi-SARIMA
as the second step produced significantly less false pos-
itives than the original SARIMA as the second step for
every dataset. The only case that produced less false pos-
itives than the multi-SARIMA is TBATS for the Synthetic
dataset, which was expected as TBATS did better on that
dataset. Also, the two-step approach using multi-SARIMA
as the second step improved the runtime, compared to the
standalone multi-SARIMA, as it worked on less data points.
Notably, TBATS did better as the second step than the original
SARIMA for every dataset, but worse than multi-SARIMA
for two of the three datasets.

All two-step algorithms could not detect the four true
positives that MA originally detected for the HotGym dataset.
We believe this is because other models could not detect the

fourth anomaly detected by MA, causing them to label it as
non-anomalous when they were used in the second step.

VI. CONCLUSION AND FUTURE TOPICS
When data contains repeated patterns such as seasonality,
they can be learned and applied to a forecasting model to
improve the accuracy of the model. Today, time series data
containing multiple seasonalities are common in real-world
applications [7]. However, most existing models for anomaly
detection in time series data can include just one or no sea-
sonal component, so they cannot capture every seasonal trend
that appears in datasets.

Our multi-SARIMA model takes the original SARIMA
model one step forward by including multiple seasonal com-
ponents instead of just one. The multi-SARIMA produced
better anomaly detection results than the original SARIMA
for every dataset we tested and, in most cases, outperformed
well-known HTM and TBATS. Also, we proved that our
multi-SARIMA produces better results than SARIMA when
used as the second step in the two-step approach we proposed
in [2].

In addition to our multi-SARIMA model, we showed the
anomaly detecting capability of an existing multi-seasonal
forecasting model TBATS, which also outperformed
SARIMA and HTM.

Different time series datasets have different characteristics,
such that no one model could be the best for every case.
However, our multi-SARIMA model showed very accurate
detection performance on various datasets we used for evalu-
ation and better overall results than other models.

In the future, we would like to incorporate some improve-
ments to the multi-SARIMA model, including the runtime
reduction, the ability to capture more than two seasonal
trends, and a better way to choose optimal parameters.
Moreover, we plan to compare the performance of our
multi-SARIMA model with those of deep learning methods,
such as Temporal Convolutional Networks (TCN) [17].

REFERENCES
[1] T. Xie and J. Ding, ‘‘Forecasting with multiple seasonality,’’ in Proc. IEEE

Int. Conf. Big Data, Dec. 2020, pp. 240–245.

[2] R. E. Sperl and S. M. Chung, ‘‘Two-step anomaly detection for time series

data,’’ in Proc. Int. Conf. Data Softw. Eng. (ICoDSE), Nov. 2019.

VOLUME 11, 2023

106463

---

<!-- PAGE 9 -->

[3] Z. Hasani, ‘‘Robust anomaly detection algorithms for real-time big data:
Comparison of algorithms,’’ in Proc. 6th Medit. Conf. Embedded Comput.
(MECO), Jun. 2017.

[4] C. C. Aggarwal, Data Mining: The Textbook. Cham, Switzerland: Springer,

2015.

[5] J. Hochenbaum, O. S. Vallis, and A. Kejariwal, ‘‘Automatic anomaly

detection in the cloud via statistical learning,’’ 2017, arXiv:1704.07706.

[6] A. Lavin and S. Ahmad, ‘‘Evaluating real-time anomaly detection
algorithms—The Numenta anomaly benchmark,’’ in Proc. IEEE 14th Int.
Conf. Mach. Learn. Appl. (ICMLA), Dec. 2015, pp. 38–44.

[7] K. Bandara, R. J. Hyndman, and C. Bergmeir, ‘‘MSTL: A seasonal-trend
decomposition algorithm for time series with multiple seasonal patterns,’’
2021, arXiv:2107.13462.

[8] A. M. De Livera, R. J. Hyndman, and R. D. Snyder, ‘‘Forecasting time
series with complex seasonal patterns using exponential smoothing,’’
J. Amer. Stat. Assoc., vol. 106, no. 496, pp. 1513–1527, Dec. 2011.
[9] S. Ahmad and S. Purdy, ‘‘Real-time anomaly detection for streaming

analytics,’’ 2016, arXiv:1607.02480.

[10] S. Ahmad, A. Lavin, S. Purdy, and Z. Agha, ‘‘Unsupervised real-
time anomaly detection for streaming data,’’ Neurocomputing, vol. 262,
pp. 134–147, Nov. 2017.

[11] G. Skorupa. Forecasting Time Series With Multiple Seasonalities Using
TBATS in Python. Accessed: Oct. 24, 2022. [Online]. Available: https://
medium.com/intive-developers/forecasting-time-series-with-multiple-
seasonalities-using-tbats-in-python-398a00ac0e8a

[12] F. Orneholm, ‘‘Anomaly detection in seasonal ARIMA models,’’ Dept.
Math., Uppsala Univ., Uppsala, Sweden, Project Rep. 2019:18, 2019.
[13] J. Hawkins et al. (2020). Biological and Machine Intelligence. Release
0.4. [Online]. Available: https://numenta.com/resources/biological-and-
machine-intelligence/

[14] K. Manani. Multi-Seasonal Time Series Decomposition Using MSTL in
Python. Accessed: Dec. 5, 2022. [Online]. Available: https://towardsdata
science.com/multi-seasonal-time-series-decomposition-using-mstl-in-
python-136630e67530

[15] M. Peixeiro. How to Forecast Time Series With Multiple Seasonalities.
Accessed: Dec. 6, 2022. [Online]. Available: https://towardsdatascience.
com/how-to-forecast-time-series-with-multiple-seasonalities-
23c77152347e

[16] P. Dix, ‘‘What time series matters for metrics, real-time and sensor data?’’

InfluxData, San Francisco, CA, USA, to be published.

[17] Y. He and J. Zhao, ‘‘Temporal convolutional networks for anomaly detec-
tion in time series,’’ J. Phys., Conf. Ser., vol. 1213, no. 4, Jun. 2019.
[18] R. J. Hyndman and G. Athanasopoulos, Forecasting: Principles and Prac-

tice, 3rd ed. Otexts, 2021.

A. T. Williams et al.: Anomaly Detection in Multi-Seasonal Time Series Data

ASHTON T. WILLIAMS received the B.S. and
M.S. degrees in computer science from Wright
State University, Dayton, OH, USA, in 2022 and
2023, respectively. He is currently a software
engineer.

RYAN E. SPERL received the B.S. and M.S. degrees in computer science
from Wright State University, Dayton, OH, USA, in 2019 and 2020, respec-
tively. He is currently a software engineer.

SOON M. CHUNG (Life Member, IEEE) received
the B.S. degree in electronic engineering from
Seoul National University, South Korea, in 1979,
the M.S. degree in electrical engineering from the
Korea Advanced Institute of Science and Technol-
ogy, South Korea, in 1981, and the Ph.D. degree in
computer engineering from Syracuse University,
Syracuse, NY, USA, in 1990. He is currently a Pro-
fessor with the Department of Computer Science
and Engineering, Wright State University, Dayton,
OH, USA. His current research interests include database, data mining, text
mining, information security, data grid, multimedia database, and parallel
and distributed processing.

106464

VOLUME 11, 2023

<!-- MARKITDOWN CONVERSION -->

<!-- Full MarkItDown conversion for formatting fidelity. -->

Received8August2023,accepted2September2023,dateofpublication20September2023,dateofcurrentversion4October2023.
DigitalObjectIdentifier10.1109/ACCESS.2023.3317791
Anomaly Detection in Multi-Seasonal
Time Series Data
ASHTONT.WILLIAMS,RYANE.SPERL,ANDSOONM.CHUNG ,(LifeMember,IEEE)
DepartmentofComputerScienceandEngineering,WrightStateUniversity,Dayton,OH45435,USA
Correspondingauthor:SoonM.Chung(soon.chung@wright.edu)
ThisworkwassupportedinpartbytheAirForceResearchLaboratory(AFRL)/DefenseAssociatedGraduateStudentInnovators(DAGSI)
ResearchFellowship.
ABSTRACT Most of today’s time series data contain anomalies and multiple seasonalities, and accurate
anomaly detection in these data is critical to almost any type of business. However, most mainstream
forecastingmodelsusedforanomalydetectioncanonlyincorporateoneornoseasonalcomponentintotheir
forecastsandcannotcaptureeveryknownseasonalpatternintimeseriesdata.Inthispaper,weproposeanew
multi-seasonalforecastingmodelforanomalydetectionintimeseriesdatathatextendsthepopularSeasonal
AutoregressiveIntegratedMovingAverage(SARIMA)model.Ourmodel,namedmulti-SARIMA,utilizes
a time series dataset’s multiple pre-determined seasonal trends to increase anomaly detection accuracy
even more than the original SARIMA model. Our experimental results demonstrate the higher accuracy
of multi-SARIMA when multiple seasonalities are present than most models with one or no seasonal
component,althoughwithmoreprocessingtime.
INDEX TERMS Anomalydetection,movingaverage,multipleseasonalities,multi-SARIMA,timeseries
data,SARIMA.
I. INTRODUCTION Some time series data contain a seasonality, which is a
Nowadays there are many data sources, such as sensors, pattern that repeats at specific time intervals [1]. For exam-
producing time series data, which is a sequence of data ple, CPU usage rate of a server may have a daily seasonal
points indexed in time order. These data points typically trend.ThepopularSeasonalAutoregressiveIntegratedMov-
consist of successive measurements made from the same ingAverage(SARIMA)forecastingmodel[18]canrepresent
sourceoverafixedtimeintervalandareusedtotrackchange a seasonal trend in its forecasting of time series data. How-
overtime[16].Anomalies(i.e.,outliers)aredatapointsthat ever, SARIMA can implement only one seasonal trend in
significantlydeviatefromtheirexpectedvalue[4],andearly its forecasting [1]. Allowing only one seasonal trend is a
detectionofanomaliesisimportanttomitigatetheseharmful majorlimitationbecausesometimeseriesdatacontainmore
effects, particularly in critical systems where failure can be thanoneseasonality[7].Forexample,NewYorkCity(NYC)
catastrophic[3].Forexample,ahospitalcandetectabnormal taxi traffic data has both daily and weekly seasonal trends.
bodysignalsofitspatientsandnotifyprofessionalsbeforeit’s Thus,utilizingallknownseasonaleffectsintimeseriesdata
toolate. can play an important role in data forecasting and anomaly
Foranomalydetectionintimeseriesdata,forecastingmod- detection[1].
elsareusedtocompareforecastedvaluestoactualvaluesto In this paper, we propose a new multi-seasonal model,
determine if a point is anomalous. While some deviation is namedmulti-SARIMA,foranomalydetectionintimeseries
expectedwhencomparingaforecastedvaluetoitsrealcoun- data that extends the SARIMA model by allowing mul-
terpart,ifthepredictedvaluedeviatessignificantlyfromthe tiple seasonal components. The multi-SARIMA utilizes a
actualvalue,thenthedatapointismostlikelyananomaly[2]. dataset’smultiplepre-determinedseasonaltrendstoincrease
anomaly detection accuracy. To compare with our multi-
SARIMA, we also implemented other anomaly detection
The associate editor coordinating the review of this manuscript and models, including Moving Average (MA), Seasonal Inte-
approvingitforpublicationwasChao-YangChen . grated Moving Average (SIMA), the original SARIMA,
2023TheAuthors.ThisworkislicensedunderaCreativeCommonsAttribution-NonCommercial-NoDerivatives4.0License.
106456 Formoreinformation,seehttps://creativecommons.org/licenses/by-nc-nd/4.0/ VOLUME11,2023

A.T.Williamsetal.:AnomalyDetectioninMulti-SeasonalTimeSeriesData
Numenta’sHierarchicalTemporalMemory(HTM)[9],[10], B. MOVINGAVERAGE(MA)
| and another |     | multi-seasonal | model | TBATS |     | which stands | for |             |      |            |     |          |     |              |     |
| ----------- | --- | -------------- | ----- | ----- | --- | ------------ | --- | ----------- | ---- | ---------- | --- | -------- | --- | ------------ | --- |
|             |     |                |       |       |     |              |     | Time series | data | is usually |     | produced | by  | a monitoring |     |
Trigonometricseasonality,Box-Coxtransformation,ARMA device and can range from spatial data in medical imag-
errors, Trend and Seasonal components [8]. Additionally, ing to sequential data in network security [2], [12]. Let
|     |     |     |     |     |     |     |     | ,X  | ,...,X |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ------ | --- | --- | --- | --- | --- | --- |
weimplementedthetwo-stepapproachproposedin[2]with X = {X }beaone-dimensionaltimeserieswith
|     |     |     |     |     |     |     |     | 1   | 2   | t   |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
ourmulti-SARIMAasthesecondstep.Themulti-SARIMA evenly spaced discrete time where X is a value X at time t
t
| produced | better | anomaly | detection | results |     | than the | original |     |     |     |     |     |     |     |     |
| -------- | ------ | ------- | --------- | ------- | --- | -------- | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
[2],[12].Valuesthatarebeforetareconsidereditslags,such
SARIMA for every dataset we tested and, in most cases, thatX t−i isthevalueistepsbackinthetimeseries[2],[12].
outperformedHTMandTBATS. ThebackshiftoperatorByieldsthelagsinatimeseriesand
| Thispaperisorganizedasfollows:SectionIIdefinesour |     |     |     |     |     |     |     | isdefinedas: |     |     |     |     |     |     |     |
| ------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | ------------ | --- | --- | --- | --- | --- | --- | --- |
anomalylabelingmethodandexplainstheexistinganomaly
detectionmodelsusedinthispaper.SectionIIIexplainsour BiX =X t−i (3)
t
| proposed    | multi-SARIMA |        | model    | and          | the two-step | approach |        |                     |     |     |     |     |     |     |     |
| ----------- | ------------ | ------ | -------- | ------------ | ------------ | -------- | ------ | ------------------- | --- | --- | --- | --- | --- | --- | --- |
|             |              |        |          |              |              |          |        | forallt >i[2],[12]. |     |     |     |     |     |     |     |
| we proposed |              | in [2] | with our | multi-SARIMA |              | model    | as the |                     |     |     |     |     |     |     |     |
Themovingaverage(MA)modelisasimpleandcommon
secondstep.SectionIVdescribesthedatasetsusedfortesting
approachtoforecastingtimeseriesdata.Themovingaverage
andtheirproperties,theMultipleSeasonal-Trenddecomposi-
|     |     |     |     |     |     |     |     | oforderq,denotedasMA(q),predictsthevalueX |     |     |     |     |     |     | attimet |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------------------------------------- | --- | --- | --- | --- | --- | --- | ------- |
tionusingLocallyEstimatedScatterplotSmoothing(Loess)
as:
| (MSTL) | decomposition |          | [7] | we used          | to verify | the seasonal |        |     |     |     |     |     |     |     |     |
| ------ | ------------- | -------- | --- | ---------------- | --------- | ------------ | ------ | --- | --- | --- | --- | --- | --- | --- | --- |
| trends | in each       | dataset, | and | the differencing |           | used         | on our |     |     |     |     | q   |     |     |     |
X
|     |     |     |     |     |     |     |     |     |     | X =µ+ε | +   | b   | Biε |     | (4) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------ | --- | --- | --- | --- | --- |
datasets.SectionVdescribestheimplementationofdifferent t t i t
models, single-step and two-step test results, and compar- i=1
isonsbasedonthedetectionaccuracyandruntime.SectionVI
|     |     |     |     |     |     |     |     | for all t > | q, where | ε   | is the | white noise | error | at  | time t, µ |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------- | -------- | --- | ------ | ----------- | ----- | --- | --------- |
t
contains our final thoughts with a conclusion and possible is the mean of the series, and b = (cid:8) b ,b ,...,b (cid:9) is the q
|     |     |     |     |     |     |     |     |     |     |     |     |     | 1 2 | q   |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
futureresearchtopics.
parametersforthemodel[2],[12].
II. ANOMALYLABELINGANDEXISTINGDETECTION
|     |     |     |     |     |     |     |     | C. SEASONALINTEGRATEDMOVINGAVERAGE(SIMA) |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
METHODS
|     |     |     |     |     |     |     |     | The seasonal | integrated |     | moving | average | (SIMA) |     | model is |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------ | ---------- | --- | ------ | ------- | ------ | --- | -------- |
A. ANOMALYLABELING
|      |        |         |           |        |     |              |     | an extension | of         | the MA | model | where          | one | seasonal | com-    |
| ---- | ------ | ------- | --------- | ------ | --- | ------------ | --- | ------------ | ---------- | ------ | ----- | -------------- | --- | -------- | ------- |
| Time | series | anomaly | detection | models | use | a calculated |     |              |            |        |       |                |     |          |         |
|      |        |         |           |        |     |              |     | ponent is    | considered | for    | the   | data forecast. |     | SIMA     | denoted |
numericmetriccalledananomalyscoretodetermineifadata as SIMA(d,q) , forecasts using MA(q) with a seasonally
m
| point       | is an | anomaly | or not    | [4]. In our | case,   | we determine  |     |             |      |         |              |     |         |     |           |
| ----------- | ----- | ------- | --------- | ----------- | ------- | ------------- | --- | ----------- | ---- | ------- | ------------ | --- | ------- | --- | --------- |
|             |       |         |           |             |         |               |     | differenced | time | series. | Differencing |     | is used | to  | eliminate |
| the anomaly |       | score   | using the | error       | between | the predicted |     |             |      |         |              |     |         |     |           |
trendsthatareapparentinadatasettomakethedatastationary
valueandtheactualvalue.Iftheanomalyscoreexceedsthe
|     |     |     |     |     |     |     |     | [2]. Differencing |     | is done | by replacing |     | every | value | with the |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------------- | --- | ------- | ------------ | --- | ----- | ----- | -------- |
threshold,thedatapointislabeledasananomaly[10].
|     |      |            |           |           |          |     |         | difference   | between                                   | itself | and | its first | lag | [2]. Let | ∇X = |
| --- | ---- | ---------- | --------- | --------- | -------- | --- | ------- | ------------ | ----------------------------------------- | ------ | --- | --------- | --- | -------- | ---- |
| In  | some | cases, the | threshold | is fixed, | however, |     | a fixed |              |                                           |        |     |           |     |          |      |
|     |      |            |           |           |          |     |         | {X ,X ,...,X | }beafirst-orderdifferencedtimeseries,such |        |     |           |     |          |      |
|     |      |            |           |           |          |     |         | 1 2          | t                                         |        |     |           |     |          |      |
thresholdisnotsuitableinourcasebecausethevariancecan
that
changeovertime.Thedynamicthresholdmustbecalculated
using sample metrics since we cannot assume the detector ∇X =X −X t−1 =(1−B)X (5)
|            |     |               |         |     |        |               |     |     |     | t t |     |     |     | t   |     |
| ---------- | --- | ------------- | ------- | --- | ------ | ------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| has access |     | to the entire | dataset | as  | values | are collected | in  |     |     |     |     |     |     |     |     |
real-time, such that only past values are available. For our for all t > 1 [2]. The order of differencing can be repre-
sentedbyasymbold,suchthat∇dX
dynamic threshold, we used the mean absolute deviation t denotesthedth-order
(MAD)calculatedas: differenced time series. For example, when d = 2, it is the
second-orderdifferencedtimeseries[2].Therefore,adiffer-
|     | MAD=median(|X |     |     | −median(X)|) |     |     |     |     |     |     |     |     |     |     |     |
| --- | ------------- | --- | --- | ------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|     |               |     |     | i            |     |     | (1) |     |     |     |     |     |     |     |     |
encedtimeseriescanbeexpressedmoregenerallyas:
| where                                                | X is | the portion | of data | values | in  | a rolling | sample |     |     |     |          |     |     |     |     |
| ---------------------------------------------------- | ---- | ----------- | ------- | ------ | --- | --------- | ------ | --- | --- | --- | -------- | --- | --- | --- | --- |
|                                                      |      |             |         |        |     |           |        |     |     | ∇dX | =(1−B)dX |     |     |     | (6) |
| windowtolimittheimpactofolderdatavalues[2].Unlikethe |      |             |         |        |     |           |        |     |     |     | t        |     | t   |     |     |
meanandstandarddeviation,MADisrobustwhenanomalies
|     |     |     |     |     |     |     |     | for all t | > d | [2]. However, |     | no amount |     | of differencing |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --------- | --- | ------------- | --- | --------- | --- | --------------- | --- |
arepresentinthedatasample,andthereisnodistortionunless
willremoveaseasonaltrendfromdata.Seasonaltrendscan
atleastahalfofthesampleiscomposedofanomalies[2],[5].
|     |     |     |     |     |     |     |     | be eliminated | by  | seasonal | differencing, |     | which | differences |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------- | --- | -------- | ------------- | --- | ----- | ----------- | --- |
Wethenmultiplythethresholdwithaconstanttoadjustthe
|                                                        |     |     |     |     |     |     |     | against the | previous | season | instead | of  | the | first lag | [2]. Let |
| ------------------------------------------------------ | --- | --- | --- | --- | --- | --- | --- | ----------- | -------- | ------ | ------- | --- | --- | --------- | -------- |
| sensitivityofouranomalydetection,resultinginouranomaly |     |     |     |     |     |     |     | ∇dX         |          |        |         |     |     |           |          |
beaseasonallydifferencedtimeseries,wheremisthe
| detectionmetricdefinedas: |     |     |     |     |     |     |     | m   |     |     |     |     |     |     |     |
| ------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
periodoftheseasonaltrend,thenitisdefinedas:
=|ε |>|s∗MAD|
|     | AnomalyDetected |     | t   | t   |     |     | (2) |     |     |     |           |     |     |     |     |
| --- | --------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --------- | --- | --- | --- | --- |
|     |                 |     |     |     |     |     |     |     |     | ∇dX | =(1−Bm)dX |     |     |     | (7) |
|     |                 |     |     |     |     |     |     |     |     | m   | t         |     | t   |     |     |
whereε istheanomalyscoremeasuredattimet,andsisthe
t
|                         |     |     |     |     |     |     |     | >d      | ∗m[2]. |     |     |     |     |     |        |
| ----------------------- | --- | --- | --- | --- | --- | --- | --- | ------- | ------ | --- | --- | --- | --- | --- | ------ |
| sensitivityconstant[2]. |     |     |     |     |     |     |     | forallt |        |     |     |     |     |     |        |
| VOLUME11,2023           |     |     |     |     |     |     |     |         |        |     |     |     |     |     | 106457 |

A.T.Williamsetal.:AnomalyDetectioninMulti-SeasonalTimeSeriesData
D. SEASONALAUTOREGRESSIVEINTEGRATEDMOVING Thesecondpartisthespatialpooler.Thespatialpooleris
AVERAGE(SARIMA) responsible for learning spatial patterns present in the data.
The seasonal autoregressive integrated moving average It starts by taking in a fixed number of encoded SDR bits
(SARIMA)denotedasSARIMA(p,d,q) isanextensionof then assigns a layer containing columns [13]. Each column
m
theautoregressiveintegratedmovingaveragemodeldenoted hasasetofpotentialsynapses,aconnectiontotheprevious
as ARIMA(p,d,q) by incorporating a seasonal component layer representing a subset of the input bits [13]. Connec-
intoitsforecastingmodel.Bothmodelsarebasedonacom- tions between the layers are then determined based on the
bination of the autoregressive model (AR) and the moving comparisonbetweenperformancevaluesandaperformance
average (MA) model. The autoregressive model predicts X threshold[13].Theactivesynapsesofeachcolumnarethen
usingitsmostrecentlags[2].LetAR(p)beanautoregressive determined based on how many connected columns exist
modeloforderpthatpredictsthevalueofX attimetas: [13].Asmoredataarecollected,thespatialpoolerdetermines
howmanyconnectedsynapsesofeachcolumnoverlapwith
p
X =c+ε + X aBiX (8) the input SDR bits, and activates columns with the most
t t i t
overlap [3]. Only active columns update their connections,
i=1
then the network boosts or hinders columns accordingly to
forallt > p,wherea = {a ,a ,...,a }isthepparameters
1 2 p preventcolumnsfrombeingtoodominant[2].
forthemodel[2],[12].LetARMA(p,q)beanautoregressive
ThethirdandfinalpartoftheHTMlearningmodelisthe
moving average model (ARMA), where p represents the
temporalmemory.Temporalmemorydoestwothings:learns
orderofARandqrepresentstheorderofMA,definedas:
the sequences of SDRs produced by the spatial pooler and
p q makes predictions [13]. The temporal memory establishes
X X
X =c+ε + aBiX + bBiε (9)
t t i t i t connections between cells in the spatial pooler’s columns,
i=1 j=1 then learns the connections between cells that reside in the
for all t > max{p,q} [2], [12]. The ARIMA(p,d,q) model same layer [13]. An active cell forms connections to other
predicts X by modeling the differenced series ∇dX with an cellsthatwerejustactive.Thisway,thecellscanpredictwhen
ARMA(p,q)model[2].TheSARIMA(p,d,q) modelpre- they will likely become active by referring to their current
m
dictsX bymodelingtheseasonallydifferencedseries∇dX connections[13].
m t
withanARMA(p,q)model: HTMalsocalculatesitsownanomalyscorebymeasuring
thedeviationbetweenitspredictedinputandtheactualinput
p q
X =c+ε +( X aBi∇dX )+( X bBiε ) (10) [9].Theanomalyscoreattimet denotedass t ,isgivenas:
t t i m t i t
i=1 j=1 s =1− π(X t−1 )∗a(X t ) (11)
where X = ∇dX + Pd−1∇i BmX [2]. Although the
t |a(X
t
)|
t m t i=0 m t
wherea(X )isthesparseencodedvalueoftheinputattimet,
SARIMA model is one of the best and most common time t
series forecasting models, it is unable to incorporate more
|a(X
t
)|isthetotalnumberof1-bitsina(X
t
),andπ(X
t−1
)is
theinternalpredictionofa(X )[10].Theanomalyscorewill
thanoneseasonaltrendintoitsforecasting. t
be0ifthecurrentinputisperfectlypredictedor1otherwise
[9].Toincreasetheanomalydetectionaccuracy,ashort-term
E. HIERARCHICALTEMPORALMEMORY(HTM)
averageofthepredictionerrorsiscomputed,thenathreshold
Hierarchical Temporal Memory (HTM) is a neural
is applied to the Gaussian tail probability to determine if
network-based machine learning algorithm derived from
a data point is truly an anomaly [10]. This second step in
neuroscience that models spatial and temporal patterns in
determiningtheanomalyscoreisthecomplimentofthetail
streaming data [9]. HTM works by simulating how the
probabilityandisdefinedastheanomalylikelihood:
neocortex works in the human brain [13]. It is versatile and
tolerable to noisy data and can detect even the most subtle L =1−Q( µ′ t −µ t ) (12)
anomalies, resulting in a low false positive rate with most t σ
t
rea
T
l
h
a
e
no
l
m
ea
a
r
l
n
ie
in
s
g
de
o
te
f
c
H
te
T
d
M
[3].
can be broken down into three whereµ′ t =
Pi
i
=
=
W
0
′
j
−1st−i,µ
t isthemeanofthesampleofpast
main parts: The first part is the encoder and the Sparse anomalyscores,σ t isthestandarddeviationofthesampleof
Distributed Representations (SDRs) [3]. SDRs help explain past anomaly scores, µ’ t is the short-term average, Q is the
how brains can make semantic generalizations [13]. SDRs Gaussiantailprobabilityfunction,andW′ isawindowfora
are represented by vectors that contain thousands of bits, shorttermmovingaverage[9],[10].
andtheencodergivesthebitsmeaningbyencodingthemto
representthepropertiesofarepresentation[13].Theencoded F. TBATS
propertiesoftwoSDRsarecompared,andiftheyhave1-bit The Trigonometric seasonality, Box-Cox transformation,
inthesamelocation,thentheysharesomesimilarities[13]. ARMA errors, Trend and Seasonal components model,
Themore1-bitsthetwoSDRsshare,themoresemantically denoted as TBATS, is a forecasting model for complex
similarthetworepresentationsare[13]. time series that can include multiple seasonal periods,
106458 VOLUME11,2023

A.T.Williamsetal.:AnomalyDetectioninMulti-SeasonalTimeSeriesData
high-frequencyseasonality,non-integerseasonality,anddual asseasonalcomponentsbasedontheFourierseries:
calendar effects [8]. TBATS is currently one of the best
multi-seasonal time series forecasting models and is the s (i) = X
ki
s (i) (17)
most common [1]. It utilizes a framework that incorporates t j,t
j=1
Box-Coxtransformations,Fourierrepresentationswithtime-
varying coefficients, and ARMA error correction [8]. The s ( j, i t ) =s ( j, i t ) −1 cosω j (i)+s ∗ j, ( t i − ) 1 sinω j (i)+γ 1 (i) d t (18)
TBATSmodelrequirespre-specifiedseasonalperiodsthatare s ∗(i) =−s (i) sinω(i) +s ∗(i) cosω(i) +γ(i) d (19)
thenmodeledbyatrigonometricrepresentationbasedonthe j,t j,t−1 j j,t j 2 t
Fourierseries[1],[11].
where
γ(i)
and
γ(i)
are the smoothing parameters, k is
TBATS is an extension of the Box-Cox transformation, 1 2 i
the amount of harmonics for the ith seasonal period, and
ARMA errors, Trend, and Seasonal components (BATS) ω(i) =2πj/m [8],[11].
model, where the addition of trigonometric seasonality cre- j i
ates a more flexible parsimonious approach [8]. BATS,
III. PROPOSEDDETECTIONMETHODS
however,isanextensionofexponentialsmoothingmethods
A. MULTI-SARIMA
that combine its other components like Box-Cox transfor-
Most forecasting models today include at most one sea-
mations and ARMA errors to produce a better forecasting
sonal component, and this unnecessary restriction only
model[15].TheexponentialsmoothinginBATSutilizesthe
hinders their potential. Allowing a model to take full
Holt-Winters method that handles time series with a trend
advantage of every known seasonal pattern in a dataset
and a single seasonality [8], [15]. The exponential smooth-
gives more options and possibilities for it to perform bet-
ing works by having future values be weighted averages of
ter. Our proposed model, named multi-SARIMA, extends
past values [15]. The Box-Cox transformation in the model
the original SARIMA(p,d,q) model and is denoted as
stabilizesthevarianceandmeanovertime,makingthetime m
SARIMA(p ,d ,q ) × (p ,d ,q ) . It predicts X by
seriesstationary.ARMAerrorsinthemodelareappliedtothe 1 1 1 m1 2 2 2 m2
modeling the seasonal differenced series
∇d2X
with two
residualstocaptureanyleftoverinformation[15].Thetrend m2
SARIMA(p,d,q) models:
captureslong-termchangesinthemean.Lastly,theseasonal m
com
Th
p
e
on
B
e
A
nt
T
c
S
ap
m
tu
o
r
d
e
e
s
l
a
w
ti
a
m
s
e
im
se
p
ri
r
e
o
s
v
’
e
p
d
er
t
i
o
od
f
i
o
c
r
a
e
l
c
v
a
a
s
r
t
ia
ti
t
m
io
e
n[
s
1
e
5
ri
]
e
.
s ∇ m d2 2 X t =
(cid:16)Xp
i= i 1 a 1,i Bm1i
(cid:17)
∇ m d2 2 X t
w tri i g th on m om ul e t t i r p i l c e se s a e s a o s n o a n l a i l ty c a o s m w p e o ll n a e s n u ts pd w at i e th dv t e h r e sio a n d s di o ti f o s n om o e f + (cid:16)Xp i= 2 1 a 2,i Bm2i (cid:17) ∇ m d2 2 X t
m [1 e 5 t ] h . o T d h s et u r s ig e o d no in me B t A ri T c S sea to son c a re li a t t y e in th T e BA T T B S AT re S pre m s o en d t e s l e [ a 8 c ] h , − (cid:16)Xp j= 2 1 Xp i= 1 1 a 1,i a 2,j Bm1i+m2j (cid:17) ∇ m d2 2 X t +ε t
seasonalcomponentinatimeseriesasatrigonometricrepre- +
(cid:16)Xq1
b 1,i Bm1i
(cid:17)
ε t +
(cid:16)Xq2
b 2,i Bm2i
(cid:17)
ε t
i=1 i=1
s a e ll n o t w at s io t n he b m as o e d d e o l n to th fi e t F m o u u l r t i i e p r le s , e l r a ie rg s e [ r 8 , ] a , n [ d 15 n ] o . n T - h in is te a g d e d r i s ti e o a n - + (cid:16)Xq2 Xq1 b 1,i b 2,j Bm1i+m2j (cid:17) ε t (20)
j=1 i=1
sonalcomponentswithlessrun-timethantheoriginalBATS
model[15]. whereX t =∇ m d2 2 X t +Pd i= 2 − 0 1Bm2∇ m i 2 X t ,m 1 istheshortersea-
TheBATSmodelcanberepresentedas: sonalperiod,m isthelongerseasonalperiod,d istheorder
2 2
ofdifferencing,a isthepparametersfortheshorterperiod,
1
y ( t λ) =l t−1 +φb t−1 + X T s ( t i − ) mt +d t (13) M b 1 A is o th rd e e q r p o a f ra th m e e s t h er o s rt f e o r r p th e e ri s o h d o , r p te 1 r i p s e t r h io e d s , e q a 1 so is n t a h l e A s R eas o o rd n e a r l
i=1 for the shorter period, a is the p parameters for the longer
2
αl t =l t−1 +φb t−1 +d t (14) period,b
2
istheqparametersforthelongerperiod,q
2
isthe
b t =ϕb t−1 +βd t (15) seasonalMAorderofthelongerperiod,andp 2 istheseasonal
p q ARorderforthelongerperiod.Themulti-SARIMAequation
X X
d t = φ i d t−1 + θ i e t−i +e t (16) was derived by extending the original SARIMA equation.
i=1 i=1 Themulti-SARIMAequationcontainsseasonalARandMA
terms for individual season lengths m and m followed by
1 2
where y
(λ)
is the Box-Cox transformed time series at time additionaltermsthataccountforthecombinationofthetwo
t
(i)
t, s is the ith seasonal component, l is the local level at seasonaltrends,andthebackshiftoperatorbeingscaledbythe
t t
time t, b is the trend with damping at time t, d is the seasonlength.Wealsoincludedadditionalfactorstoaccount
t t
ARIMA(p,q) process, e is white noise, φ and θ are the for the nonseasonal trend (p,d,q) in the multi-SARIMA.
t
ARIMA(p,q) coefficients, φ is the trend damping, α and β Fromthere,wedistributethefactorsandsolvefortheloneX
t
arethesmoothing,T istheamountofseasonalities,λ isthe to get the final equation depicted above. We concluded that
Box-Coxtransformation,andm isthelengthoftheithsea- weonlyneedtodifferenceusingd andm sincedifferencing
i 2 2
sonalperiod[8],[11].TheBATSmodelisthenextendedby overthelongerseasonaltrendcapturesbothseasonalitiesand
adding the trigonometric seasonal model and is represented makesthedatastationary.Wesetd =0sincewedifference
1
VOLUME11,2023 106459

A.T.Williamsetal.:AnomalyDetectioninMulti-SeasonalTimeSeriesData
thedataandobtainastationaryversionusingd 2 ,eliminating TABLE1. Overviewofthedatasets.
d fromappearinginthemulti-SARIMAequation.
1
In our approach, the first model is trained on three itera-
tions of the shorter seasonal trend, while the second model
is trained on three iterations of the longer seasonal trend.
Fromthefirstmodel,weobtaintheseasonalandnon-seasonal
autoregressiveandmovingaverageparameters,theresiduals,
and the constant. From the second model, we obtain just
theseasonalautoregressiveandmovingaverageparameters.
Duringtheprediction,weapplythevaluesfrombothmodels
to the multi-SARIMA equation to get the prediction X at
timet. For our experiments,we used the MA and SIMAmodels
We expect the multi-SARIMA model to perform well, as our first step to create the initial labeling, then verified
comparedtoothermodels,whenitisusedwithdatasetsthat thelabelswithSARIMA,ourmulti-SARIMA,andTBATS.
containtwomeaningfulseasonaltrends.Ifadatasetdoesn’t Wedenoteacombinationoftwomodelsusedinthetwo-step
have meaningful seasonal patterns, the multi-SARIMA approach as ‘first step + second step’. For example, a two-
model is not expected to perform better. If a dataset con- stepapproachthatusesMAasthefirststepandSARIMAas
tainstwoseasonaltrends,buttheyareinsignificant,thenthe
thesecondstepisdenotedasMA+SARIMA.
multi-SARIMAmodelisnotguaranteedtoperformbetter.
Betterperformanceentailsthatthemulti-SARIMAmodel IV. DATASETS
has higher anomaly detection accuracy, meaning a higher We evaluated all models on three different datasets. Two
true positive rate with a lower false positive rate. With this datasetsarefromtheNumentaAnomalyBenchmark(NAB),
higherprecision,however,wealsoexpecttheruntimeofthe acollectionoflabeled,univariate,real-worldtimeseriesdata
multi-SARIMA to be somewhat longer than those of other [6]. The third dataset is a synthetic time series dataset we
models. This is because the multi-SARIMA model requires createdusingourdatagenerationtool.Sincewearefocused
more fitting and learning than other models as it uses two on multi-seasonal anomaly detection in time series data,
differentmodelsandlearnsovertwoseasonalperiods. the three datasets contain two meaningful seasonal trends,
numeroushand-labeledanomalies,andenoughdatapointsto
trainandtestmodelson.Ageneralsummaryofeachdataset
B. TWO-STEPAPPROACH isgiveninTable1.WeusedasmallerversionoftheHotGym
The two-step approach for anomaly detection was initially datasetasoneanomalyoccurredwithinthefirstthreeweeks
proposed by us in [2]. The algorithm consists of a simpler ofthedatacausestrainingissueswithsomemodels.
modelthatcanlabeldatafastwithlessaccuracyandamore
complex model that can label data accurately but requires A. MSTLSEASONALDECOMPOSITION
more time [2]. In the two-step approach, the first step does Sinceourmulti-SARIMAmodelutilizestwoseasonalcom-
the initial labeling with the faster but less accurate model, ponents,weshouldconfirmthatourtestdatasetscontaintwo
then the second step verifies the first step’s labels with the meaningfulseasonaltrends.Forthatpurpose,weusedMul-
slower but more accurate model [2]. The first model must tipleSeasonal-TrenddecompositionusingLocallyEstimated
pick up as many true positives as possible, then the second ScatterplotSmoothing(Loess)(MSTL)[7].Thereareafew
step denies most of its false positives and verifies its true multi-seasonaltimeseriesdecompositionmethodsavailable,
positives[2].So,thiscombinedapproachislimitedtothetrue including Facebook’s Prophet, TBATS, and Seasonal-Trend
positiverateofthefirstmodelbutreducesthefalsepositive DecompositionusingRegression(STR);however,wechose
rate [2]. In the worst case, the first model finds every data MSTL because it produces the lowest root mean squared
pointanomalous,causingthesecondsteptoverifyeverydata error, is robust to outliers, has the smallest execution time,
pointinthedataset[2].Theruntimeofthetwo-stepisatbest andiseasytouseasitrequiresminimalparameters[7],[14].
slightlyslowerthanthefirstmodelandatworstslightlyfaster MSTL decomposes an additive time series into a trend
thanthesecondmodel. component,givenseasonalcomponents,andaresidualcom-
Although the two-step approach is not new by itself, ponent[7],[14].MSTLisanextensionoftheSeasonal-Trend
usingourmulti-SARIMAasthesecondstepinthetwo-step decompositionusingLoess(STL)modelasSTLisonlyable
approachis.Sinceweexpectourmulti-SARIMAtoperform todecomposetimeseries withoneseasonalcomponent[7],
better than other models, when it is used with datasets that [14]. Loess is a scatterplot smoothing technique that fits a
contain two meaningful seasonal trends, we also expect our curvetoascatterplottodeterminethedegreeofthepolyno-
multi-SARIMAtoperformwellwhenitisusedasthesecond mial[14].STLappliesLoesstovarioustransformationsofthe
step in the two-step approach. For the two-step approach, giventimeseriesandthenextractsthetrendandoneseasonal
betterresultsentailmaintainingthetruepositiverateoffirst component [14]. MSTL extracts each known seasonal com-
stepmodelwhilesignificantlyreducingitsfalsepositiverate. ponentinatimeseriesusingSTLonebyone[7],[14].MSTL
106460 VOLUME11,2023

A.T.Williamsetal.:AnomalyDetectioninMulti-SeasonalTimeSeriesData
FIGURE1. MSTLdecompositionoftheNYCTaxidatasetforoneweekof
data.Thetopgraphdepictsthedataset’sdailyseasonaltrendwhilethe FIGURE2. MSTLdecompositionoftheSyntheticDatasetforoneweekof
data.Thetopgraphdepictsthedataset’sdailyseasonaltrendwhilethe
bottomgraphdepictsitsweeklyseasonaltrendwiththeweekend
highlightedinred. bottomgraphdepictsitsweeklyseasonaltrendwiththeweekend
highlightedinred.
firstordersthegivenseasonalperiodsfromshortesttolongest
toavoidshorterseasonalperiodsfrombeinginterlacedwith
| the longer | seasonal | periods | [7]. | MSTL | then applies | STL |     |     |     |     |     |
| ---------- | -------- | ------- | ---- | ---- | ------------ | --- | --- | --- | --- | --- | --- |
iterativelyoneachidentifiedseasonalperiod[7].TheMSTL
additivedecompositionofatimeseriescanbedefinedas:
|     | X =S1+S2+···+Sn+T |     |     |     | +R  | (21) |     |     |     |     |     |
| --- | ----------------- | --- | --- | --- | --- | ---- | --- | --- | --- | --- | --- |
|     | t                 | t   | t   | t   | t t |      |     |     |     |     |     |
S1,S2,...,Sn
| where     |          |             | denotes       | the seasonal | components,   |            |     |     |     |     |     |
| --------- | -------- | ----------- | ------------- | ------------ | ------------- | ---------- | --- | --- | --- | --- | --- |
|           | t t      | t           |               |              |               |            |     |     |     |     |     |
| T denotes | the      | trend,      | and R denotes |              | the remainder | [7].       |     |     |     |     |     |
| t         |          |             | t             |              |               |            |     |     |     |     |     |
| We used   | Python’s | statsmodels | MSTL          |              | package       | on a Linux |     |     |     |     |     |
virtualmachinetoperformtheMSTLdecompositiononour
datasetsasdepictedinFig.1–3.
| Fig. | 1 depicts | one week | of MSTL | decomposition |     | on the |     |     |     |     |     |
| ---- | --------- | -------- | ------- | ------------- | --- | ------ | --- | --- | --- | --- | --- |
FIGURE3. MSTLdecompositionoftheHotGymdatasetforoneweekof
| NYC | taxi dataset, | where | the vertical |     | axis represents | the |     |     |     |     |     |
| --- | ------------- | ----- | ------------ | --- | --------------- | --- | --- | --- | --- | --- | --- |
data.Thetopgraphdepictsthedataset’sdailyseasonaltrendwhilethe
smoothingfortheseasonalcomponentgiven.Theseasonality bottomgraphdepictsitsweeklyseasonaltrendwiththeweekend
highlightedinred.
| in the      | data follows | a typical    | workweek    |            | and makes | sense,     |     |     |     |     |     |
| ----------- | ------------ | ------------ | ----------- | ---------- | --------- | ---------- | --- | --- | --- | --- | --- |
| considering | that         | the original | data        | represents | taxi      | passengers |     |     |     |     |     |
| in New      | York City.   | The          | daily trend | is very    | low early | in the     |     |     |     |     |     |
morning, then has spikes before midday since everyone is workweekandmakessense,consideringthattheoriginaldata
|     |     |     |     |     |     |     | represents | a gym’s energy | consumption | in Australia. | The |
| --- | --- | --- | --- | --- | --- | --- | ---------- | -------------- | ----------- | ------------- | --- |
tryingtogettowork,adiparoundnoonsincenooneisout
|     |     |     |     |     |     |     | daily trend | shows that | the data values | tend to have | a small |
| --- | --- | --- | --- | --- | --- | --- | ----------- | ---------- | --------------- | ------------ | ------- |
andabout,thehighestspikesintheafternoonwheneveryone
isheadinghomeortravelingaroundthecity,thenendswith spikeatmidnightandthenareverylowearlyinthemorning
|        |         |               |       |          |       |           | until midday | where there | is the highest | spike during | the |
| ------ | ------- | ------------- | ----- | -------- | ----- | --------- | ------------ | ----------- | -------------- | ------------ | --- |
| very a | low dip | late at night | since | everyone | is at | home. The |              |             |                |              |     |
weeklytrendfollowsatypicalworkweekwiththeweekdays hottestandbusiesttimeoftheday,thendecreasesbackdown
maintaining the same taxi usage pattern until the weekend for the rest of the day as the sun goes down and people go
home.Theweeklytrendshowsthatthroughouttheweekdays,
| showing | a different | pattern  | and     | higher        | spikes during | later  |                                                   |               |                  |           |         |
| ------- | ----------- | -------- | ------- | ------------- | ------------- | ------ | ------------------------------------------------- | ------------- | ---------------- | --------- | ------- |
| hours.  |             |          |         |               |               |        | thetrendseemstobesomewhatconsistentaspeopletendto |               |                  |           |         |
|         |             |          |         |               |               |        | visit the                                         | gym regularly | during the week, | until the | weekend |
| Fig.    | 2 depicts   | one week | of MSTL | decomposition |               | on our |                                                   |               |                  |           |         |
Syntheticdataset.Wegeneratedoursyntheticdatatosimulate thathasnohighspikesbutverylowdipsasnotmanypeople
atypicalworkschedule.Thedailytrendshowsthatthedata aregoingtothegymoritisclosedduringdifferenthours.
| values | tend to | be very | low early | in the | morning, | then has |     |     |     |     |     |
| ------ | ------- | ------- | --------- | ------ | -------- | -------- | --- | --- | --- | --- | --- |
a spike before midday, a small dip around noon, another B. DIFFERENCING
spike in the afternoon, and ends with very a low dip late at For the differencing of our test datasets in order to make
night. The weekly trend shows that the trend is consistent themstationary,wedecidedtouseseasonaldifferencingsince
throughouttheweekdays,thenshiftingtohavinglowervalues theycontainapparentseasonaltrends,specificallydailyand
duringtheweekend. weekly seasonalities. So, we differenced using first-order
Fig. 3 depicts one week of MSTL decomposition on the seasonal differencing with a period of one week. This cap-
HotGymdataset.Theseasonalityinthedatafollowsatypical turesboththedailyandweeklyseasonaltrendsandproduces
| VOLUME11,2023 |     |     |     |     |     |     |     |     |     |     | 106461 |
| ------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------ |

A.T.Williamsetal.:AnomalyDetectioninMulti-SeasonalTimeSeriesData
TABLE2. Single-stepexperimentalresults.
dataset. Since there are a very small number of anomalies
withinalargenumberofdatapointsineachdataset,compar-
ingperformancebasedonaccuracypercentageisineffective
as a model that never labels any data point as anomalous
wouldachievemorethan90%accuracy[2].Instead,wefocus
on which models produce the most true positives with the
lowestnumberoffalsepositives.Thismeans,thebestmodels
wouldbeabletolabelallanomaliescorrectlywhilenotlabel-
ing other non-anomalous data points as anomalies. Table 2
showsthefinalsingle-stepresultsofallmodels,andTable3
showsthefinaltwo-stepresults,whereTPisthenumberof
truepositives,FPisthenumberoffalsepositives,andFNis
thenumberoffalsenegatives.
FIGURE4. NYCTaxidatasetafterfirst-orderseasonaldifferencingwitha
periodof1week.Anomaliesaredepictedbytheredlines. A. SINGLE-STEPEXPERIMENTALRESULTS
For our single-step experimental results shown in Table 2,
our multi-SARIMA model had the highest number of true
stationarydata.Fig.4depictsourNYCTaxidatasetsafterthe positives for every dataset while maintaining fewer false
first-orderseasonaldifferencingwasapplied.Thebeginning positivesthantheSARIMAmodelforeverydataset,although
ofthegraphhasaflatlinebecausethefirstweekhasnoprior withlongerruntime.Ourmulti-SARIMAhadeitherthebest
datatodifferenceagainst[2]. orsecond-bestresultsforeverydataset.
Themulti-SARIMAhadthehighestruntimecomparedto
V. EXPERIMENTALRESULTS othermodelsbecausethemulti-SARIMAistheonlymodel
To properly compare our multi-SARIMA model, we used thatcombinestheresultsfromtwomodelswhichtrainover
existingforecastingmodelsMA,SIMA,SARIMA,TBATS, the two seasonal periods of one day and one week, respec-
and HTM. MA, SIMA, SARIMA, TBATS, and our pro- tively.SinceeveryotherseasonalmodelbutTBATSislimited
posedmulti-SARIMAwereimplementedinPython3.8.5on tooneseasonaltrend,theyaretrainedovertheperiodofone
a Windows 10 computer with an Intel i7 8-core processor dayasthatistheirstrongerseasonality.Trainingtwomodels
operatingat3.80GHz,16GBofmemory,anda1TBSSD. andhavingonetrainingoveraweekrequiredtheextratime
Numenta’s HTM algorithm was implemented on the same but produced better results. Specifically, the runtime of the
machine,usingPython2.7.Theoptimalparametersforeach multi-SARIMA on the NYC Taxi dataset was unexpectedly
model were determined by a grid search, and we compared long.ThisisbecausetheNYCTaxidatasetistheonlydataset
thebestperformancesofallmodelsinthissection.Weused with a data point every 30 minutes instead of every hour,
open-source python libraries provided by their authors for causing the 3-week training data to contain a large amount
our implementations of HTM and TBATS. For MA, SIMA, of data for the models to train on. The other multi-seasonal
andSARIMAweusedPython’sstatsmodelspackage.Forthe model, TBATS, was also slow and had the second longest
two-stepapproach,weusedMAandSIMAasthefirststep, runtime for every dataset. TBATS may be a more refined
andSARIMA,TBATS,andourproposedmulti-SARIMAas model,butitstillrequiresmoretimesincethatisthenature
thesecondstep. oflearningmultipleseasonalpatterns.
Allmodelsweretrainedonthefirstthreeweeksofthedata, Our multi-SARIMA was the only model that achieved
then evaluated on the remaining data. We made sure there the same number of true positives as HTM for the NYC
were no anomalies present in the training portion of each TaxidatasetandoutperformedeverymodelfortheHotGym
106462 VOLUME11,2023

A.T.Williamsetal.:AnomalyDetectioninMulti-SeasonalTimeSeriesData
TABLE3. Two-stepexperimentalresults.
dataset. The multi-SARIMA doubled the true positive rate fourthanomalydetectedbyMA,causingthemtolabelitas
of HTM and TBATS for the HotGym dataset while still non-anomalouswhentheywereusedinthesecondstep.
| maintaining | the | second | lowest | false positive | rate | among all |                               |     |     |     |     |     |     |
| ----------- | --- | ------ | ------ | -------------- | ---- | --------- | ----------------------------- | --- | --- | --- | --- | --- | --- |
| models.     |     |        |        |                |      |           | VI. CONCLUSIONANDFUTURETOPICS |     |     |     |     |     |     |
Expectedly,thetwomulti-seasonalmodelsperformedthe When data contains repeated patterns such as seasonality,
bestfortheSyntheticdataset.Mostmodelsdetectedallfive they can be learned and applied to a forecasting model to
anomalies,butTBATSandmulti-SARIMAdidsowithunder improve the accuracy of the model. Today, time series data
ten false positives. HTM performed very poorly with this containing multiple seasonalities are common in real-world
dataset,andwethinkthatisbecausethedatasetwascreated applications[7].However,mostexistingmodelsforanomaly
usingrandomness,throwingoffthelearningofHTM. detection in time series data can include just one or no sea-
Notably, TBATS had either the same or higher true posi- sonalcomponent,sotheycannotcaptureeveryseasonaltrend
tiverate thantheoriginalSARIMAfor everydataset,while thatappearsindatasets.
maintainingalowerfalsepositiverate. Our multi-SARIMA model takes the original SARIMA
modelonestepforwardbyincludingmultipleseasonalcom-
|     |     |     |     |     |     |     | ponents | instead | of just one. | The | multi-SARIMA |     | produced |
| --- | --- | --- | --- | --- | --- | --- | ------- | ------- | ------------ | --- | ------------ | --- | -------- |
B. TWO-STEPEXPERIMENTALRESULTS better anomaly detection results than the original SARIMA
foreverydatasetwetestedand,inmostcases,outperformed
| For our | two-step | experimental |     | results | shown | in Table 3, all |            |     |            |     |       |           |          |
| ------- | -------- | ------------ | --- | ------- | ----- | --------------- | ---------- | --- | ---------- | --- | ----- | --------- | -------- |
|         |          |              |     |         |       |                 | well-known | HTM | and TBATS. |     | Also, | we proved | that our |
two-stepalgorithms,eachofwhichusesacombinationoftwo
multi-SARIMAproducesbetterresultsthanSARIMAwhen
| models, | have less | false | positives | than | their standalone | first |     |     |     |     |     |     |     |
| ------- | --------- | ----- | --------- | ---- | ---------------- | ----- | --- | --- | --- | --- | --- | --- | --- |
usedasthesecondstepinthetwo-stepapproachweproposed
| step results | shown     | in Table | 2,    | except          | for MA | + SARIMA     |             |           |                  |     |             |                |            |
| ------------ | --------- | -------- | ----- | --------------- | ------ | ------------ | ----------- | --------- | ---------------- | --- | ----------- | -------------- | ---------- |
| for the      | Synthetic | dataset  | which | produced        | the    | same results | in[2].      |           |                  |     |             |                |            |
|              |           |          |       |                 |        |              | In addition | to        | our multi-SARIMA |     | model,      | we             | showed the |
| as MA.       | This is   | because  | MA’s  | false positives |        | were already |             |           |                  |     |             |                |            |
|              |           |          |       |                 |        |              | anomaly     | detecting | capability       | of  | an existing | multi-seasonal |            |
verylowforthatdataset.Also,mosttwo-stepalgorithmshave
|     |     |     |     |     |     |     | forecasting | model | TBATS, | which |     | also outperformed |     |
| --- | --- | --- | --- | --- | --- | --- | ----------- | ----- | ------ | ----- | --- | ----------------- | --- |
significantlylessfalsepositivesthantheirstandalonesecond
SARIMAandHTM.
| step results | shown | in Table | 2,  | but have | less | true positives |     |     |     |     |     |     |     |
| ------------ | ----- | -------- | --- | -------- | ---- | -------------- | --- | --- | --- | --- | --- | --- | --- |
because they are limited to the true positive rate of the first Differenttimeseriesdatasetshavedifferentcharacteristics,
|     |     |     |     |     |     |     | such that | no one | model | could be | the best | for | every case. |
| --- | --- | --- | --- | --- | --- | --- | --------- | ------ | ----- | -------- | -------- | --- | ----------- |
step.
|     |     |     |     |     |     |     | However, | our multi-SARIMA |     | model | showed | very | accurate |
| --- | --- | --- | --- | --- | --- | --- | -------- | ---------------- | --- | ----- | ------ | ---- | -------- |
Althoughwithmoreprocessingtime,themulti-SARIMA
as the second step produced significantly less false pos- detectionperformanceonvariousdatasetsweusedforevalu-
ationandbetteroverallresultsthanothermodels.
| itives than | the | original | SARIMA | as  | the second | step for |     |     |     |     |     |     |     |
| ----------- | --- | -------- | ------ | --- | ---------- | -------- | --- | --- | --- | --- | --- | --- | --- |
Inthefuture,wewouldliketoincorporatesomeimprove-
| every dataset. |       | The only     | case | that produced | less | false pos-     |            |                  |            |         |           |      |              |
| -------------- | ----- | ------------ | ---- | ------------- | ---- | -------------- | ---------- | ---------------- | ---------- | ------- | --------- | ---- | ------------ |
|                |       |              |      |               |      |                | ments to   | the multi-SARIMA |            | model,  | including |      | the runtime  |
| itives than    | the   | multi-SARIMA |      | is TBATS      | for  | the Synthetic  |            |                  |            |         |           |      |              |
|                |       |              |      |               |      |                | reduction, | the              | ability to | capture | more      | than | two seasonal |
| dataset,       | which | was expected |      | as TBATS      | did  | better on that |            |                  |            |         |           |      |              |
dataset. Also, the two-step approach using multi-SARIMA trends, and a better way to choose optimal parameters.
|               |     |               |     |              |          |        | Moreover, | we  | plan to | compare | the performance |     | of our |
| ------------- | --- | ------------- | --- | ------------ | -------- | ------ | --------- | --- | ------- | ------- | --------------- | --- | ------ |
| as the second |     | step improved |     | the runtime, | compared | to the |           |     |         |         |                 |     |        |
multi-SARIMAmodelwiththoseofdeeplearningmethods,
standalonemulti-SARIMA,asitworkedonlessdatapoints.
suchasTemporalConvolutionalNetworks(TCN)[17].
Notably,TBATSdidbetterasthesecondstepthantheoriginal
| SARIMA                    | for every | dataset, | but | worse | than multi-SARIMA |     |            |     |     |     |     |     |     |
| ------------------------- | --------- | -------- | --- | ----- | ----------------- | --- | ---------- | --- | --- | --- | --- | --- | --- |
| fortwoofthethreedatasets. |           |          |     |       |                   |     | REFERENCES |     |     |     |     |     |     |
[1] T.XieandJ.Ding,‘‘Forecastingwithmultipleseasonality,’’inProc.IEEE
| All two-step |     | algorithms | could | not | detect | the four true |     |     |     |     |     |     |     |
| ------------ | --- | ---------- | ----- | --- | ------ | ------------- | --- | --- | --- | --- | --- | --- | --- |
Int.Conf.BigData,Dec.2020,pp.240–245.
positivesthatMAoriginallydetectedfortheHotGymdataset.
[2] R.E.SperlandS.M.Chung,‘‘Two-stepanomalydetectionfortimeseries
Webelievethisisbecauseothermodelscouldnotdetectthe data,’’inProc.Int.Conf.DataSoftw.Eng.(ICoDSE),Nov.2019.
| VOLUME11,2023 |     |     |     |     |     |     |     |     |     |     |     |     | 106463 |
| ------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------ |

A.T.Williamsetal.:AnomalyDetectioninMulti-SeasonalTimeSeriesData
[3] Z.Hasani,‘‘Robustanomalydetectionalgorithmsforreal-timebigdata: ASHTON T. WILLIAMS received the B.S. and
Comparisonofalgorithms,’’inProc.6thMedit.Conf.EmbeddedComput. M.S. degrees in computer science from Wright
(MECO),Jun.2017. StateUniversity,Dayton,OH,USA,in2022and
[4] C.C.Aggarwal,DataMining:TheTextbook.Cham,Switzerland:Springer, 2023, respectively. He is currently a software
2015. engineer.
[5] J. Hochenbaum, O. S. Vallis, and A. Kejariwal, ‘‘Automatic anomaly
detectioninthecloudviastatisticallearning,’’2017,arXiv:1704.07706.
[6] A. Lavin and S. Ahmad, ‘‘Evaluating real-time anomaly detection
algorithms—TheNumentaanomalybenchmark,’’inProc.IEEE14thInt.
Conf.Mach.Learn.Appl.(ICMLA),Dec.2015,pp.38–44.
[7] K.Bandara,R.J.Hyndman,andC.Bergmeir,‘‘MSTL:Aseasonal-trend
decompositionalgorithmfortimeserieswithmultipleseasonalpatterns,’’
2021,arXiv:2107.13462.
[8] A.M.DeLivera,R.J.Hyndman,andR.D.Snyder,‘‘Forecastingtime
series with complex seasonal patterns using exponential smoothing,’’
J.Amer.Stat.Assoc.,vol.106,no.496,pp.1513–1527,Dec.2011.
[9] S. Ahmad and S. Purdy, ‘‘Real-time anomaly detection for streaming
analytics,’’2016,arXiv:1607.02480.
[10] S. Ahmad, A. Lavin, S. Purdy, and Z. Agha, ‘‘Unsupervised real- RYAN E. SPERL receivedtheB.S.andM.S.degreesincomputerscience
timeanomalydetectionforstreamingdata,’’Neurocomputing,vol.262, fromWrightStateUniversity,Dayton,OH,USA,in2019and2020,respec-
pp.134–147,Nov.2017. tively.Heiscurrentlyasoftwareengineer.
[11] G.Skorupa.ForecastingTimeSeriesWithMultipleSeasonalitiesUsing
TBATSinPython.Accessed:Oct.24,2022.[Online].Available:https://
medium.com/intive-developers/forecasting-time-series-with-multiple-
seasonalities-using-tbats-in-python-398a00ac0e8a
[12] F. Orneholm, ‘‘Anomaly detection in seasonal ARIMA models,’’ Dept.
Math.,UppsalaUniv.,Uppsala,Sweden,ProjectRep.2019:18,2019.
[13] J.Hawkinsetal.(2020).BiologicalandMachineIntelligence.Release
0.4. [Online]. Available: https://numenta.com/resources/biological-and-
machine-intelligence/ SOONM.CHUNG(LifeMember,IEEE)received
[14] K.Manani.Multi-SeasonalTimeSeriesDecompositionUsingMSTLin the B.S. degree in electronic engineering from
Python.Accessed:Dec.5,2022.[Online].Available:https://towardsdata SeoulNationalUniversity,SouthKorea,in1979,
science.com/multi-seasonal-time-series-decomposition-using-mstl-in-
theM.S.degreeinelectricalengineeringfromthe
python-136630e67530
KoreaAdvancedInstituteofScienceandTechnol-
[15] M.Peixeiro.HowtoForecastTimeSeriesWithMultipleSeasonalities.
ogy,SouthKorea,in1981,andthePh.D.degreein
Accessed:Dec.6,2022. [Online]. Available: https://towardsdatascience.
computer engineering from Syracuse University,
com/how-to-forecast-time-series-with-multiple-seasonalities-
Syracuse,NY,USA,in1990.HeiscurrentlyaPro-
23c77152347e
[16] P.Dix,‘‘Whattimeseriesmattersformetrics,real-timeandsensordata?’’ fessorwiththeDepartmentofComputerScience
InfluxData,SanFrancisco,CA,USA,tobepublished. andEngineering,WrightStateUniversity,Dayton,
[17] Y.HeandJ.Zhao,‘‘Temporalconvolutionalnetworksforanomalydetec- OH,USA.Hiscurrentresearchinterestsincludedatabase,datamining,text
tionintimeseries,’’J.Phys.,Conf.Ser.,vol.1213,no.4,Jun.2019. mining,informationsecurity,datagrid,multimediadatabase,andparallel
[18] R.J.HyndmanandG.Athanasopoulos,Forecasting:PrinciplesandPrac- anddistributedprocessing.
tice,3rded.Otexts,2021.
106464 VOLUME11,2023