---
conversion_metadata:
  converted_at: "2026-07-21T09:16:18Z"
  converter_tool: "markitdown"
  converter_version: "0.1.6"
  source_pdf: "Wang Y..pdf"
  source_pdf_sha256: "137c4f550424f871ee61ffca78c0677b3cf6d2bed42a23d572a14846f1653aa1"
  page_count: 145
  markdown_char_count: 711862
---

<!-- PAGE-AWARE EXTRACTION (via pdfminer.six) -->

<!-- PAGE 1 -->

New developments in sequential change point detection for time

series and spatio-temporal analysis

by

Yanzhao Wang

A PhD Dissertation

Submitted to the Faculty

of the

WORCESTER POLYTECHNIC INSTITUTE

In partial fulfillment of the requirements for the

Degree of Doctor of Philosophy

in

Statistics

May, 2023

APPROVED:

Professor Jian Zou, Advisor
Department of Mathematical Sciences
Worcester Polytechnic Institute

Professor Nalini Ravishanker
Department of Statistics
University of Connecticut

Professor Zheyang Wu
Department of Mathematical Sciences
Worcester Polytechnic Institute

Professor Fangfang Wang
Department of Mathematical Sciences
Worcester Polytechnic Institute

Professor Qingshuo Song
Department of Mathematical Sciences
Worcester Polytechnic Institute

---

<!-- PAGE 2 -->

Abstract

Abrupt aberrations in stochastic systems often result from external factors of interest, such

as changes in trading intensity patterns or outbreaks of infectious diseases. These factors can

introduce abnormal observations into the corresponding data collection systems. However, the

data being monitored typically involve multiple sources, high dimensionality, and convoluted

mutual dependence. To promptly detect any change points within complex streaming data,

my dissertation research focuses on developing efficient methods for sequential change point

detection and multivariate time series modeling.

First, we focus on the study of online structural break detection in financial durations.

We propose an ensemble non-parametric methodology that leverages asymptotic theories and

re-sampling approaches for robust structural break detection, integrated with semi-parametric

model inference techniques. By detecting changes in the pattern of financial durations, practi-

tioners can take advantage of short-term profit opportunities through volatility-related option

trading or adjust their position to mitigate the impact of sell-offs in the high-frequency financial

market.

Second, we develop a Bayesian hierarchical framework with bivariate temporal effect and

latent level-correlated effect for multivariate discrete-valued financial time series. Our framework

enables the analysis of how count data relates to relevant covariates and provides forecasts for

future individual count data. Additionally, it establishes a connection between time-varying

observational correlation and latent correlations to more accurately quantify the association

between transaction counts at various risk levels. The INLA implementation of this framework

grants computational efficiency and flexibility for large-scale numerical studies.

Third, to address the complexity of the surveillance data, such as the spatio-temporal in-

terdependence, we synthesize relevant techniques from the previous two research projects and

propose an iterative sequential outbreak detection procedure for online spatio-temporal daily

count data. Specifically, we develop a Bayesian online spatio-temporal outbreak detection with

prior updating and p-value adaptation (BOSTON-PUPA) procedure. This iterative procedure

involves the generalized Poisson distribution (GPD) model and supports synchronous surveil-

lance over multiple locations with a controlled false detection rate as well as high sensitivity

against outbreaks in a wide range of signal-to-noise ratios.

Our research tackles various sequential change point problems across different scenarios,

providing efficient modeling for multivariate time series and corresponding sequential change

point detection techniques for time-dependent and spatio-temporal data. These methodologies

1

---

<!-- PAGE 3 -->

have been successfully applied in real-world applications such as finance and public health, where

they offer high-quality statistical inference in an online fashion and can be easily extended to

other domains using a similar framework.

2

---

<!-- PAGE 4 -->

Acknowledgements

Having my five-year Ph.D. journey was both a challenging and rewarding experience. Seeking

research-oriented solutions to advanced real-world problems required not only individual tenacity

but also a significant amount of support and guidance from different great people along this road.

Firstly, I want to express my sincere gratitude towards my Ph.D. advisor, Professor Jian Zou.

Not only does he share a wealth of research experience and communication skills with me profession-

ally, but also demonstrates his exemplary work ethic and family commitment in a well coordinated

manner. As his Ph.D. student, I was lucky to have his heartfelt cheers for my research as well

as career achievements and I also felt blessed to receive his encouragement during my hardships.

With his advice and feedback, the progress of my dissertation was made much smoother and more

efficient. Professor Zou set an excellent example to me about being an outstanding statistician with

a combined trait of decent statistical background and high interpersonal intelligence, which I will

admire for my own career development in the future.

Secondly, I also want to thank the rest of my dissertation committee members, Professor Nalini

Ravishanker, Professor Fangfang Wang, Professor Zheyang Wu and Professor Qingshuo Song for

their generous inputs to my dissertation research.

It was a very fulfilling experience for me to

collaborate with and learn from Professor Ravishanker since her high-standard requirements for

research deliverable and manuscript writing inspired me to take extra miles to justify and refine

my work. Expertise of Professor Wang and Professor Wu was a key motivating factor for me to

delve into advanced research areas such as multvariate time series analysis in spatial econometric

research and correlated p-value combination methods in genetic study. With Professor Song’s

affluent financial modeling experience and unique insights into article organzation, numerous edits

of my dissertation were stemming from his constructive suggestions. Their significant impacts on

my dissertation accomplishment are invaluable and are deeply appreciated.

I am also grateful for having Professor Balgobin Nandram as my independent study instructor

for advanced Bayesian statistics. His dedication and mastery towards Bayesian statistics expedited

my understanding of this field in a solid fashion. My special appreciation goes to Ziji Yu, Jianchang

Lin from Takeda and Yaohua Zhang from Vertex as my external career influencers, since their

contribution to solving real world problems as prestigious industrial biostatisticians broadened my

3

---

<!-- PAGE 5 -->

horizon over the real application of statistics.

In addition, I want to send my thankfulness to

other faculty members and staff who helped me along my journey, especially Rhonda Podell for her

administrative support and Mike Malone for his technical support, when I was a Teaching Assistant.

I also appreciated the quality time with my Ph.D. peers from various majors taking advanced

courses, brainstorming project problems, discussing career plans, and having fun together.

At last, I want to give my genuine thanks to my Dad Tanggui Wang, my Mom Jijuan Hu, and

my cousin Cheng Wang for their unconditional love and support, which is a crucial driving force

for me to persevere in the face of various obstacles and barriers.

4

---

<!-- PAGE 6 -->

Contents

1 Introduction

12

1.1 Sequential change point detection . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 12

1.2 Multivariate time series analysis

. . . . . . . . . . . . . . . . . . . . . . . . . . . . . 12

1.3 Fast Bayesian inference approximation . . . . . . . . . . . . . . . . . . . . . . . . . . 14

1.4 Summary . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 14

2 Online structural break point detection

16

2.1 Background . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 16

2.2 Literature review . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 16

2.2.1 Log ACD model

. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 17

2.2.2 Change point detection . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 18

2.3 E-PEF detection . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 19

2.3.1 Model Framework . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 20

2.3.2 Parameter estimation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 20

2.3.3 Detector statistic . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 22

2.3.3.1

Spillover effect . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 23

2.3.4 Hypothesis testing . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 25

2.3.5 Ensemble detection . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 27

2.3.5.1 Motivation of ensemble detection . . . . . . . . . . . . . . . . . . . . 27

2.3.5.2 Ensemble detection scheme . . . . . . . . . . . . . . . . . . . . . . . 30

2.4 Numerical study . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 32

2.4.1

Simulation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 32

2.4.1.1 Monitoring horizon . . . . . . . . . . . . . . . . . . . . . . . . . . . 34

2.4.1.2 Detection probability and Delay . . . . . . . . . . . . . . . . . . . . 35

2.4.1.3 Robust performance for non-stationary scenarios . . . . . . . . . . . 36

2.4.2 Real application . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 40

2.5 Summary . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 43

5

---

<!-- PAGE 7 -->

3 Multivariate latent level correlation model (LCM) for financial high frequency

count time series

45

3.1 Background . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 45

3.2 Literature review . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 46

3.2.1 Discrete time series modeling . . . . . . . . . . . . . . . . . . . . . . . . . . . 46

3.2.2

Integrated Nested Laplace Approximation (INLA)

. . . . . . . . . . . . . . . 48

3.3 BVAR(1)-LCM model

. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 49

3.3.1 Model framework . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 50

3.3.2

INLA implementation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 53

3.4 Numerical study . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 57

3.4.1

Simulation study: INLA v.s STAN . . . . . . . . . . . . . . . . . . . . . . . . 57

3.4.2 Real application . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 60

3.4.2.1 High-frequency trading (HFT) background . . . . . . . . . . . . . . 64

3.4.2.2 High-frequency count data description . . . . . . . . . . . . . . . . . 65

3.4.2.3 Model adequacy and prediction accuracy comparisons . . . . . . . . 68

3.4.2.4 An illustration of BVRW(1)-LCM framework . . . . . . . . . . . . . 71

3.5 Summary . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 83

4 Sequential Bayesian spatio-temporal outbreak detection

84

4.1 Background . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 84

4.2 Literature review . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 85

4.2.1 Change point detection in public health surveillance system . . . . . . . . . . 85

4.2.2 Traditional outbreak detection methods . . . . . . . . . . . . . . . . . . . . . 86

4.2.3 Modern outbreak detection methods . . . . . . . . . . . . . . . . . . . . . . . 89

4.3 BOSTON-PUPA procedure . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 91

4.3.1

Step 1: Bayesian model inference and in-sample prediction . . . . . . . . . . 92

4.3.2

Step 2: Latent aberration assessment . . . . . . . . . . . . . . . . . . . . . . . 96

4.3.3

Step 3: P-value adaptation . . . . . . . . . . . . . . . . . . . . . . . . . . . . 97

4.3.4

Step 4: Decision-making and algorithm update . . . . . . . . . . . . . . . . . 99

4.4 Numerical study . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 101

6

---

<!-- PAGE 8 -->

4.4.1

Simulation study . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 101

4.4.1.1 Model parameter recovery and in-sample model prediction . . . . . 102

4.4.1.2 Outbreak detection performance . . . . . . . . . . . . . . . . . . . . 105

4.4.2 Real application . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 117

4.4.2.1 COVID-19 Data description . . . . . . . . . . . . . . . . . . . . . . 117

4.4.2.2

Implementation of BOSTON-PUPA . . . . . . . . . . . . . . . . . . 120

4.4.2.3 Remarks

. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 122

4.5 Summary . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 122

5 Discussion and Future Work

6 Appendix

124

140

6.1 Derivation of conditional correlation . . . . . . . . . . . . . . . . . . . . . . . . . . . 140

6.1.1 Conditional Mean of Yj,st

. . . . . . . . . . . . . . . . . . . . . . . . . . . . . 140

6.1.2 Conditional variance of Yj,st . . . . . . . . . . . . . . . . . . . . . . . . . . . . 141

6.1.3 Conditional covariance between Yi,st and Yj,st . . . . . . . . . . . . . . . . . . 142

6.1.4 Conditional correlation between counts

. . . . . . . . . . . . . . . . . . . . . 142

6.2 Additional figures . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 142

List of Tables

1

2

3

4

5

Sampled time series from block bootstrap . . . . . . . . . . . . . . . . . . . . . . . . . . 26

Detector statistics computed from resampled time series from block bootstrap . . . . . . . 26

Detection probabilities in the monitoring horizon study. M2 is the length of training

period. k is the monitoring time point in the monitoring period after the training.

The false detection rate control α = 0.05.

. . . . . . . . . . . . . . . . . . . . . . . . 35

Detection probabilities at different monitoring time under different scenarios. τ is

the true break point. k is the monitoring time point in the monitoring period. . . . . 36

Summary statistics of average delay under different scenarios for different break

points. τ is the true break point. False detection rate control is α = 0.05. The

length of training period is M2 = 2500. . . . . . . . . . . . . . . . . . . . . . . . . . . 37

7

---

<!-- PAGE 9 -->

6

7

8

9

Parameters for different Scenarios . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 57

Parameter recovery rate comparison between INLA and STAN for correlated tem-

poral effects ω1 and ω2 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 61

Parameter recovery rate comparison between INLA and STAN for level-correlated

effects α1 and α2 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 62

In-sample prediction and computational time comparison between INLA and STAN 63

10 An example of raw data for the stock ABT . . . . . . . . . . . . . . . . . . . . . . . 66

11 Data structure for INLA modeling. count data for stock ABT between 9:30 and 9:34

a.m. on 01/02/2013.

. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 67

12 Percentage of the 63 data sets favoring each model regarding in-sample model ade-

quacy and out-of-sample prediction accuracy . . . . . . . . . . . . . . . . . . . . . . 71

13 Hyperparameters with restricted support and their internal representation . . . . . . 94

14

Iterative prior updating procedure with tracked mean and overdispersion . . . . . . 96

15 Parameter setup throughout the simulation study . . . . . . . . . . . . . . . . . . . . 102

16 County populations in Massachusetts in 2018 . . . . . . . . . . . . . . . . . . . . . . 102

17 Parameter recovery rate under different combinations of sliding window size and

prior discounting factor

. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 104

18 MSE for the last-day prediction in the sliding window . . . . . . . . . . . . . . . . . 104

19 Performance comparison between Prior Updating (PU) approach (T = 28, a0 = .25)

and Cumulative Fitting (CF) approach. Computation time is calculated as the

average computation time in seconds for individual model fittings in the iterative

process.

. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 105

20 Relative frequencies of detecting an outbreak out of 200 simulations for each location

using different methods for different signal-to-noise ratios.

. . . . . . . . . . . . . . . 110

21 Earliest detection days across different counties using HMP and CCT method.

. . . 121

List of Figures

1

Scatter plot of detector statistics at time stamp M2 + k = 3000 when τ = 3500. The red dots

are observed detector statistic and black dots are bootstrap samples of the detector statistics 28

8

---

<!-- PAGE 10 -->

2

3

4

5

6

7

8

9

Scatter plot of detector statistics at time stamp M2 + k = 4000 when τ = 3500. The red dots

are observed detector statistic and black dots are bootstrap samples of the detector statistics 28

The trace plot of duration of duration in the calendar time. The x-axis is calendar time (in seconds).

The y-axis denotes the value of duration. The lag between time indices of true break and detected

break is 200 and the delay time in the calendar time is 261.1051 s.

. . . . . . . . . . . . . . . . 30

Break detection outcome from 500 simulations of in a monitoring period of length 5000. X-axis

stands for the monitoring period starting at M2 = 2500. Y-axis stands for the empirical detection

probability at a specific time point. The blue dashed lines stand for the true break point τ = 2700,

3000, 3500, and 4000. The red dashed lines stand for the significance level αoverall = 0.05. . . . . . 39

(a) A single realization of Scenario 1 with true break at τ = 3500;(b) The trace plot for the individual

GM2
j

(k) with the confidence intervals based on the Wiener process and bootstrap thresholds in green

bands; (c) The trace plot for the Mahalanobis distance d2

M (k), with bootstrap threshold d2

1−αM (k)

(red horizonal line); (d) The trace plot for the binary indicator of break detection δ(k)

. . . . . . 40

Structural break points detected (red vertical dash lines) in the duration time series of IBM,

BAC, MMM and GE respectively.

. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 43

Diurnal pattern exhibited in observed counts and averaged duration in 2-min inter-

vals for stock ABT on 01/02/2023.

. . . . . . . . . . . . . . . . . . . . . . . . . . . . 68

Count data for three GICS sectors: Energy, Health care, Industrials

. . . . . . . . . 69

The association between averaged durations and counts

. . . . . . . . . . . . . . . . 74

10 The association between averaged log trading size and counts . . . . . . . . . . . . . 74

11 The estimated ρωωω with their 95% credible interval across all three sectors in January

2013 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 75

12 The dot plot of estimated variances, σ2

ω1 and σ2

ω2, of the latent temporal effects on

different days of a week across all three sectors in January 2013 . . . . . . . . . . . . 76

13 The estimated ρααα with their 95% credible interval across all three sectors in January

2013 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 77

14 The dot plot of estimated variances of the latent level effects on different days of

week across all three sectors in January 2013 . . . . . . . . . . . . . . . . . . . . . . 78

15 The variances of the observed counts on different days of week across all three sectors

in January 2013 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 78

9

---

<!-- PAGE 11 -->

16 The trace plot of daily aggregated model-based and empirical correlations in the

Healthcare sector throughout January 2023 . . . . . . . . . . . . . . . . . . . . . . . 80

17 Box plots for the square root of MSE comparison in the Energy sector between

BVRW(1)-LCM and Simple Linear Regression in January 2023 . . . . . . . . . . . . 81

18 The comparison between Spearman’s rank correlation and the latent level correlation

across three sectors.

. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 82

19

Signal-to-ratio vs Aggregated Performance Measurements

. . . . . . . . . . . . . . . 107

20 Empirical density plots of BOSTON-PUPA detected outbreak time point where the

first non-zero δs,T +k occurs in county s for different methods with different signal-

to-noise ratios (> 1). The red vertical lines represent the true outbreak time points

given in the simulation study, 103, 99, 95, 82, 102, 102, 91, 89, 97, 109, 100, and 87

for each location respectively.

. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 111

21

Signal-to-ratio vs Evaluation Metrics for different combined p-value methods: Fisher’s,

Stouffer’s, Lancaster’s, HMP and CCT when P-value Adaptation is implemented. . . 112

22 Traceplot of outbreak detection probabilities from day 29 to day 200 across 13 re-

gions. Five combined p-value methods are compared at the nominal level α = 0.05,

represented by the red dashed horizontal lines.

. . . . . . . . . . . . . . . . . . . . . 113

23 Traceplot of outbreak detection probabilities from day 29 to day 200 across 13 re-

gions. Five combined p-value methods are compared at the nominal level α = 0.05.

The red dashed lines stand for an ideal detection probability pattern of maintaining

at the nominal level before any outbreaks occur and spiking up promptly to 1 when

there are any outbreaks.

. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 114

24 Trajectories of sequential estimation of overdispersion parameter λ without any out-

breaks introduced (SNR =1) in the simulation study. Green lines stand for ˆλk, blue
¯ˆλk, and the red line represents the actual value of the overdispersion

lines stand for

parameter λ = .4448 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 115

10

---

<!-- PAGE 12 -->

25 Trajectories of sequential estimation of overdispersion parameter λ with different
¯ˆλk, and

SNRs in the simulation study. Green lines stand for ˆλk, blue lines stand for

the red line represents the actual value of the overdispersion parameter λ = .4448.

The two black vertical dashed lines stand for τ4 = 82 and τ11 + T = 109 + 28 = 137

accordingly.

. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 116

26 COVID-19 daily case count in different counties in Massachusetts from the dashboard118

27 P-values of Moran’s I and Geary’s C at every time stamp. The red dashed line

represents the significance level of 0.05. . . . . . . . . . . . . . . . . . . . . . . . . . . 119

28 ACF and PACF estimates for different counties in Massachusetts. Spatial IDs 1∼13

correspond to the following counties in order: Plymouth, Berkshire, Barnstable, Nor-

folk, Bristol, Suffolk, Franklin, Hampshire, Essex, Hampden, Dukes and Nantucket,

Middlesex, and Worcester. The red dashed lines represent the boundaries of a 95%

confidence interval for ACF and PACF.

. . . . . . . . . . . . . . . . . . . . . . . . . 120

29 Calculated outbreak detection indicators δs,T +k using HMP and CCT across all

counties in the BOSTON-PUPA procedure.

. . . . . . . . . . . . . . . . . . . . . . . 121

30 Trace plot of daily COVID-19 case counts in MA, 2020, with detected outbreaks using

BOSTON-PUPA procedure. Red line represents a state-wise outbreak indicator from

the news . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 123

31 The trace plot of daily aggregated model-based and empirical correlations in the

Healthcare sector throughout January 2023 . . . . . . . . . . . . . . . . . . . . . . . 143

32 The trace plot of daily aggregated model-based and empirical correlations in the

Industrials sector throughout January 2023 . . . . . . . . . . . . . . . . . . . . . . . 143

33 Box plots for the square root of MSE comparison in the Health care sector between

BVRW(1)-LCM and Simple Linear Regression in January 2023 . . . . . . . . . . . . 144

34 Box plots for the square root of MSE comparison in the Industrials sector between

BVRW(1)-LCM and Simple Linear Regression in January 2023 . . . . . . . . . . . . 144

11

---

<!-- PAGE 13 -->

1

Introduction

1.1 Sequential change point detection

In real life, abrupt behavioral changes in a stochastic system are usually related to some trigger-

ing events and people need to take prompt action at the occurrence of such events. Therefore,

online change point detection in many fields is an important research topic. Nowadays, with the

advancement of technology, it is common for streaming data to have high-dimensional structures

with time-dependence and intercorrelation. To make timely and accurate inference on change point,

analyses of such modern streaming data with increased complexity and sizes are in great demand

of methodological innovation beyond traditional statistical techniques.

Early online change point detection method originated from Abraham Wald’s sequential design

(Wald, 1947), which aimed for early termination of an unpromising experiment with fewer obser-

vations. Page (1954) made further improvement and proposed CUSUM-type method for quality

control application in industry, with hypothesis testing on the CUSUM-type test statistic under

null hypothesis of no change points. Such hypothesis testing procedures are usually considered

distribution-free and no model fitting is needed (Mikl´os and Lajos, 1997; Bai, 1999; Banerjee and

Urga, 2005; D¨oring, 2011; Robbins et al., 2016). Despite its easy implementation, such testing

procedures are conducted under the assumption of independent samples. For time-dependent data,

there is a plethora of literature providing solutions within a Gaussian stochastic linear system

framework, such as a combination of Kalman filter and generalized likelihood ratio (GLR) (Lai

and Shan, 1999). Under some parametric assumptions, detector statistic can take the form of

additive changes based on likelihood or innovations. Furthermore, non-likelihood-based detector

statistics are discussed and implemented but such studies considered asymptotic Gaussian property

for statistical inference. In the situations of change point detection in modern online data of ele-

vated complexity, the current trend of corresponding solutions lies in a linear system or parametric

framework, incorporating Gaussian property for inference on the detector statistics.

1.2 Multivariate time series analysis

Time series analysis is a popular research topic in various fields such as finance, econometrics,

climatology, epidemiology, clinical trials as well as interdisciplinary areas because the statistical

12

---

<!-- PAGE 14 -->

models under the independent assumptions usually lack sufficient accountability for the corre-

sponding chronological pattern. Due to the escalated demand of studying multiple measurements

as a whole, multivariate time series analysis becomes a natural tendency for correlation study for

multiple time-dependent data and draw universal inference on the latent dynamics from a collec-

tion of associated time series. In this dissertation, we propose our methods to address the research

problems arising in the financial time series and public health surveillance data.

With the advent of high-frequency trading, technological advancement allows people to record

and store a larger amount of transaction data within a short time interval. Transaction arrival times

as well as measurements of interest can be studied as time series. However, market signals are not

salient among the high volume of raw data. For example, within a short period of time, numerous

transactions on an asset can be made but the asset price fluctuations are negligible. To study

the price change in a high-frequency setting, one can easily reach some biased conclusion from a

statistical model fitted with excessive insignificant price changes. Another feature of high-frequency

financial data is irregularity. Unlike conventional time series data with standard time index, the

arrival times in high-frequency data can be randomly spaced. We need to take special care of data

processing in high-frequency financial market to study its micro-structure. Additionally, assets

prices usually are not only dependent on its own historical observations but also by some other

factors such as the overall market performance or other affiliated assets. Therefore, multivariate

time series analysis is an important tool to reveal the interrelations among multiple high-frequency

financial time series and unveil both macro-structure of the market behavior via the associated

individual assets and its micro-structure in granulated time period.

Public health surveillance analysis is a traditional research field, and its recent development

brings up new statistical challenges. Syndromic surveillance is one of the useful tools in public

health systems, which supports the monitoring of public health impacts and raise speedy alarms

at their occurrences. Preliminary diagnosis from syndromic surveillance uncovers potential onsets

of infectious outbreaks prior to a monitoring regime requiring laboratory confirmation (Hughes

et al., 2020). A decent syndromic system incorporates covariate information, spatial and temporal

dynamics of a disease, as well as integration of data from multiple sources. Therefore, the real-time

monitoring of an infectious disease such as COVID-19 in a large geographical area requires unique

accommodation for the spatio-temporal intricacy. Conventional methods either don’t account for

13

---

<!-- PAGE 15 -->

the spatial and temporal dynamics such as CUSUM (Page, 1954) or lack measure of uncertainty

for identified disease cluster (Kulldorff, 1997). Within a spatio-temporal framework, one needs to

not only overcome more complex configuration of graph structure in the model, but also keep the

implementation at a reasonable computational cost. Thanks to the advancement of technology,

Bayesian inference gains its popularity in complex modeling problems. Bayesian technique grants

the flexibility of incorporating historical information into the priors so that this approach can

alleviate the computational burden for complex Bayesian model inference. With a few stationarity

assumptions on the time series data, one is able to aim for historical information integration via

prior distributions.

1.3 Fast Bayesian inference approximation

Bayesian statistical analysis regained its popularity with the advancements in Markov chain Monte

Carlo (MCMC) sampling method during 1950s. Traditional Bayesian applications rely on the joint

posterior distribution of the model parameters. One of common concerns for the MCMC method is

about its computational efficiency. When the complexity of the model increases with the number of

parameters, the joint posterior distribution in a high dimension parameter space raises the difficulty

level for practitioners to draw samples from. In addition, posterior distribution without a closed

form will also lead an intensive computation for the traditional Bayesian inference.

However, in many situations, individual posterior marginals are often sufficient for adequate

statistical inference (G´omez-Rubio, 2020). Rue et al. (2009) proposed an approximate Bayesian

inference for latent Gaussian models by Integrated Nested Laplace Approximation (INLA). Not only

is the inference based on posterior marginals as good as the inference based on the joint posterior

distribution, but also the computational cost can be enhanced to a large extent, especially for a

sparse Gaussian Markov Random Field (GMRF) in a high dimensional parameter space. Since

our Bayesian model frameworks involve GMRF, we will be able to implement customized GMRF

random effects using INLA and enjoy the benefit of speedy computation.

1.4 Summary

For the two prevalent research directions, new challenges are burgeoning in their combinations,

where practitioners need adequate modeling for the complicated real-time data to proactively make

14

---

<!-- PAGE 16 -->

decisions on the basis of the exhibited behavioral change therefrom. Innovative methodologies are

expected to support elaborate statistical models and enjoy easy implementation with an agreeable

running time.

To solve these problems in sequential change point detection as well as multivariare time series

analysis in finance and public health, the dissertation is organized as follows. In Chapter 2, we deal

with the online change point detection problem in high-frequency market and propose an ensemble

framework for sequential analysis within univaritare time series.

In Chapter 3, we introduce a

Bayesian framework to account for the association among multiple assets, as well as capture the

behavior of the market from multivariate time series analysis. In Chapter 4, we conduct the se-

quential analysis of infectious outbreak via multivariate time series in the public health surveillance

data. We conclude our work and discuss future work in Chapter 5.

15

---

<!-- PAGE 17 -->

2 Online structural break point detection

2.1 Background

Automated high-frequency trading deals with a large number of trading orders. For each asset,

prices at these transactions form an irregularly spaced time series (Wang and Zou, 2014). Therefore,

a good awareness of the volatility alternation of an asset is crucial to martket participants, especially

in a high-frequency setting. An important practical focus for investors will be monitoring the

volatile financial market quickly and assessing accurately any behavioral change in an online fashion,

so that reliable inference can be maintained with updated model parameters.

A financial duration is defined as the difference in arrival time between two consecutive events

of interest. An event can be defined as, but is not limited to, a single transaction, a return beyond a

certain percentage, or a price change exceeding a certain amount. The i-th duration can be observed

as xi = ti − ti−1, where ti denotes the timing of the i-th event. The irregularity of arrival times of

transactions can provide useful information for the market participants. For example, if transactions

happen rapidly for an asset, then the durations between transactions will be in the form of numerous

short time intervals, while infrequent transactions will provide a sequence of longer durations.

Further, higher frequency of the transactions implies higher volatility in price fluctuations, Easley

and O’hara (1992) discussed the link between the existence of information, the timing of trading

and price movement. Thus the negative influence of long durations on returns and variances of

asset price has predictive power for ultra-high-frequency volatility jointly with a GARCH model for

the price movement (Engle and Russell, 1997; Engle, 2000). When a structural break is detected,

practitioners can update their time series model and modify their trading algorithm with financial

domain knowledge. Therefore, We address this problem of structural breaks in time series of

durations and describe an online approach for detection but the embedding of detected breaks into

a specific trading strategy is upon the practitioners.

2.2 Literature review

With the definition of inter-trade durations, the objective is to detect structural breaks in the

duration time series from financial market, in a fast online fashion.

In this subsection, we are

going to introduce the literature on the approaches for duration time series modeling and various

16

---

<!-- PAGE 18 -->

contributions in change point detection topic, which lay the foundation of our method.

2.2.1 Log ACD model

Modeling inter-event duration is a popular direction for statistical application in high-frequency

trading (Dutta et al., 2022). One of the prevalent frameworks to model time series of durations

is via conditional duration models. Starting from the seminal work of (Engle and Russell, 1998)

on auto-regressive conditional duration (ACD) models, there is a rich literature extension of ACD

models from different perspectives. Linear ACD modeling is rather common but restrictive, and

include the Exponential ACD (EACD), Weibull ACD (WACD), and Gamma ACD (GACD), etc.

Non-linear ACD models include the Log ACD models (Bauwens and Giot, 2000), the Stochastic

Conditional Duration, or SCD (p, q) models (Bauwens and Veredas, 2004) and Augmented ACD

(AACD) models through Box-Cox transformation (Fernandes and Grammig, 2006). In order to

address the long memory dependence exhibited in durations, Jasiak (1999) proposed a class of

fractionally integrated ACD (FIACD) models, and Deo et al. (2010) introduced a parametric,

latent-variable, long memory stochastic duration (LMSD) to handle the long memory feature of

inter-trade durations better than ordinary ACD models. For extreme value modeling in durations,

Zheng et al. (2016) incorporated Fr´echet innovations in the usual ACD model, and demonstrated

a better fit with Fr´echet ACD model than the Weibull ACD model. Pacurar (2008) discusses

detailed theoretical properties and applications of duration models. A plethora of literature has

showed the versatility of duration models in the fields of Finance, Econometrics, etc. Our work is

hence established under log ACD model framework for online structural break detection problems

in the financial durations.

Useful approaches for parameter estimation for the ACD models are maximum likelihood es-

timation (MLE), generalized method of moments (GMM) estimation, quasi-maximum likelihood

estimation (QMLE) and estimating function (EF) estimation (Engle and Russell, 1998; Grammig

and Wellner, 2002; Allen et al., 2008; Liang et al., 2011). Thavaneswaran et al. (2015) proposed a

combined martingale EF approach for recursive parameter estimation of generalized duration mod-

els. Zhang et al. (2019) proposed a penalized estimating function (PEF) for the aforementioned

recursive parameter estimation for the log ACD models. To enhance the efficiency of parameter

estimation, we will adopt a distribution-free approach using the penalized estimation function for

17

---

<!-- PAGE 19 -->

a robust outcome.

The key idea of ACD model can be described as following. Let xi = ti − ti−1, where i = 1, 2, . . .

denote the financial duration time series, and let F x

i−1 denote the information set of past durations.

The ACD model explaines the time dependence between xi and past observations through the

conditional expectation of xi on F x

i−1. Then the ACD(p, q) model is

xi = ψiεi, where ψi = ω +

p
(cid:88)

j=1

αjxi−j +

q
(cid:88)

j=1

βjψi−j.

(2.1)

In the Eq (2.1), the parameters are θθθ = (ω, α1, . . . , αp, β1, . . . , βq). The weak stationarity of

this non-negative process is guaranteed by the conditions of ω > 0, αj ≥ 0 for j = 1, . . . , p, βj ≥ 0
for j = 1, . . . , q and (cid:80)p

j=1 βj < 1. The innovations εi are assume to be independent

j=1 αj + (cid:80)q

and indentically distributed non-negative random variables with E(ε) = 1 and density fε(.) and

independent of F x

i−1. Log ACD model takes a similar form except that xi = exp (ψi)εi, and its

elaboration will be discussed in the unified E-PEF framework subsection.

2.2.2 Change point detection

There is a plethora of literature on change point detection, which can be classified into retrospec-

tive analysis and sequential (or online) analysis. As for the detection approach for the specific

monitoring process, online change point detection fits the needs of high-frequency traders in a real-

time setting because they need to make decisions promptly with streaming data. Some viewpoints

from retrospective detection (with complete data) inspire us in our endeavor. The seminal work of

change point detection originated in quality control (Page, 1954, 1955), with the main considera-

tion as hypothesis testing on the CUSUM-type test statistic under the null hypothesis of no break

points. Such hypothesis testing procedures are usually considered distribution-free and require no

model fitting (Mikl´os and Lajos, 1997; Bai, 1999; Banerjee and Urga, 2005; D¨oring, 2011; Robbins

et al., 2016). In financial applications, Zhang et al. (2001) proposed a threshold ACD model and

improved several inadequacies of the original ACD models. Zhang et al. (2018) implemented a pe-

nalized estimating function (PEF) approach for recursive estimation of log ACD model parameters

and applied a FindPeaks procedure to detect the structural breaks on the trajectory of the recur-

sively estimated parameter values. However, this retrospective study requires that the complete

18

---

<!-- PAGE 20 -->

observations are available.

In the online change detection field, the Kalman filter and its extensions have gained its pop-

ularity for Gaussian linear dynamic systems. Besides innovation-based methodologies, generalized

likelihood ratio (GLR) based testing is another direction to achieve online detection (Willsky and

Jones, 1976; Lai and Shan, 1999). Chu et al. (1996) discussed two sequential tests for the online

monitoring of economic behavior via linear regression models. The break detection was determined

by the fluctuation of the online sequential parameter estimates. However, the aforementioned on-

line detection methodologies handle the additive changes through either likelihood or innovations

under a parametric modeling framework with specific distributional assumptions.

In addition, an asymptotic Gaussian non-likelihood statistic is developed for online detection

in signal processing and adaptive control (Benveniste et al., 1987, 2012). Berkes et al. (2004)

extended online sequential change point detection via a quasi-likelihood function based approach,

and applied it to GARCH (p, q) models in a financial application. The test statistic for a structural

break consists of a standardized partial sum of the quasi-likelihood score function; The critical

value can be approximated via a Wiener process (Heyde, 1997). Huˇskov´a et al. (2007) investigated

the limiting behavior of test statistics based on various functionals of the partial sums of weighted

residuals. Aue et al. (2009) put forward a change point testing procedure for the volatility and

cross-volatility of multivariate time series via a vectorized CUSUM-type statistic. Horv´ath and

Rice (2014); Xie et al. (2021) give a broad review of change point detection methodologies across

different areas and their extensions.

2.3 E-PEF detection

The literature mentioned before addressed the change point detection in sequential data, under

a linear system or parametric framework, or through the asymptotic Gaussian property of the

detector statistics. Therefore, we propose an innovative ensemble penalized estimating function

(E-PEF) approach to solve the detection problem. Our contribution is a non-Gaussian detector

statistic based on the penalized estimation function for the log ACD models when the asymptotic

property is not well obtained from finite samples. This ensemble approach complements a non-

Gaussian distribution with the empirical bootstrap distribution to control the false detection rate

in the online setting, while still enjoying its computational speed. Based on our straightforward and

19

---

<!-- PAGE 21 -->

well-grounded detection mechanism, practitioners can effortlessly monitor online transaction-level

financial data, and make strategic investment with sound statistical support.

2.3.1 Model Framework

For a duration time series xi, i = 1, 2, . . . , we aim to detect the first break point (τ ) such that

x1, x2, . . . , xτ are generated from one process and xτ +1, xτ +2, . . . , are generated from a different

porcess. Consider the log ACD framework (Thavaneswaran et al., 2015), in a high-frequency

setting, a penalized log ACD (p, 0) model with large p generally provides better computational

speed and precision gain of parameter estimation than a penalized log ACD (p, q) framework does.

For simplicity, we take the log ACD (p, 0) model as an illustration.

xi =

exp(ψi)
µε

εi, i = 1, 2, . . . ,

E(xi|F x

i−1) =

exp(ψi)
µε

,

ψi = ω +

p
(cid:88)

j=1

αj log xi−j,

(2.2)

where ϵi is the non-negative innovation term with mean µϵ, F x

i−1 denotes the information set

associated with {x1, x2, . . . , xi−1}, ω, α1, . . . , αp are the AR coefficients in the log ACD model. For
weak stationarity of the log ACD process, we let (cid:80)p

j=1 αj < 1. To complete the detection of any

potential structural break point τ in the streaming time series of durations, there are three steps

to take: parameter estimation, detector statistic monitoring, and hypothesis testing, as described

below.

2.3.2 Parameter estimation

We apply the quasi-likelihood-type method (Berkes et al., 2004) to detect the structural break on the

level of parameter change in the log ACD model. The structural break point detection is based upon

the PEF (Zhang et al., 2019) for the parameters in the log ACD model. Let θθθ = (ω, α1, α2, . . . , αp)′

be the parameters in the log ACD (p, 0) model and p be the order of the log ACD model. p is

chosen to be a large number (to capture potential AR structure for the underlying log ACD model

as well as to approximate the MA structure of the log ACD model, if any). The total number of

20

---

<!-- PAGE 22 -->

parameters involved is d = p + 1.

For a comprehensive procedure of recursive martingale PEF estimation, we need to introduce

a few required quantities involved in the PEF, with detailed definitions from Zhang et al. (2019).

Suppose xi, i = 1, 2, . . . , n is a realization of a duration process with parameters in θθθ, define linear

and quadratic martingale differences respectively as,

mi(θθθ) = xi − µi(θθθ),

(2.3)

Qi(θθθ) = m2

i (θθθ) − σ2

i (θθθ),

where µi(θθθ) and σ2

i (θθθ) are conditional mean and variance of xi correspondingly. Quadratic variations

and covariation of mi and Qi are defined as,

⟨m⟩i = E[m2

i (θθθ)|F x

i−1] = σ2

i (θθθ),

⟨Q⟩i = E[m4

i (θθθ)|F x

i−1] − (E[m2

i (θθθ)|F x

i−1])2 = κi(θθθ) − σ4

i (θθθ),

(2.4)

⟨m, Q⟩i = E[m3

i (θθθ)|F x

i−1] = γi(θθθ),

where κi(θθθ) and γi(θθθ) are the third and fourth central moments of xi respectively. Next, Tha-

vaneswaran et al. (2015) derived the optimal (Godambe-Durbin) combined martingale EF,

g∗
C(θθθ) =

n
(cid:88)

i=1

g∗
i (θθθ) =

n
(cid:88)

i=1

(cid:0)a∗

i−1mi(θθθ) + b∗

i−1Qi(θθθ)(cid:1) ,

(cid:18)

−

∂µi(θθθ)
∂θθθ
(cid:18) ∂µi(θθθ)
∂θθθ

1
⟨m⟩i
(cid:18)

ηi +

E

(cid:18)

−

E

(cid:20) ∂(m2

i (θθθ))

(cid:21)

−

F x

i−1

∂E[(m2

(cid:20) ∂(m2

i (θθθ) − σ2
∂θθθ

(cid:21)

−

F x

i−1

∂E[(m2

i (θθθ) − σ2
∂θθθ

i (θθθ) − σ2
∂θθθ
i (θθθ))

i (θθθ))|F x

i−1]

i (θθθ) − σ2
∂θθθ
i (θθθ))|F x

i−1]

where

i−1(θθθ) = ρ2
a∗
i

i−1(θθθ) = ρ2
b∗
i

with

(2.5)

(cid:19)

(cid:19)

ηi

,

(cid:19) 1

⟨Q⟩ i

(cid:19)

,

(2.6)

(2.7)

(cid:18)

1 −

ρ2
i =

(cid:19)−1

⟨m, Q⟩2
i
⟨m⟩i⟨Q⟩i

, ηi =

⟨m, Q⟩i
⟨m⟩i⟨Q⟩i

.

21

---

<!-- PAGE 23 -->

Based on (2.5), the PEF is,

C,λ(θθθ) = g∗
g∗

C(θθθ) − np′

λ(θθθ),

(2.8)

with the first derivative of the SCAD penalty (Fan and Li, 2001) for a > 2 and penalty parameter

λ,

p′
λ(|θθθ|) = λ{I(|θθθ| ≤ λ) +

(aλ − |θθθ|)+
(a − 1)λ

I(|θ| > λ)}.

(2.9)

The choice depends on the liquidity of a stock which is proportional to n, and details on how to

select a and the tuning parameter λ are discussed in (Zhang et al., 2019). For (2.3) - (2.8), µi(θθθ),

i (θθθ), γi(θθθ), κi(θθθ), ⟨m⟩i, ⟨M ⟩i, ⟨m, M ⟩i, ρ2
σ2

i , ηi are scalars, while θθθ, g∗

C,λ(θθθ), a∗

i−1(θθθ), b∗

i−1(θθθ) are

d × 1 vectors. In the parameter estimation stage, streaming time series of durations recursively

updates the estimation of θθθ.

2.3.3 Detector statistic

Consider the observed durations x1, x2, . . . , xM2 for model training, the estimation of θθθ is recursively
updated to ˆθˆθˆθM2. As the new observations xM2+1, xM2+2, . . . , xM2+k arrive, we will sequentially

evaluate their behavioral pattern and assess the occurrence of any structural breaks through a

detector statistic.

Similar to Berkes et al. (2004), our proposed detector statistic relies on the PEF. It is a d-

dimensional column vector,

GGGM2(k) =

(cid:16)

GM2
1

(k), GM2

2

(k), . . . , GM2

d (k)

(cid:17)′

,

(2.10)

where

with

GM2
j

(k) =

(cid:88)

M2<i≤M2+k

(cid:16)

(cid:17)
i,λ(ˆθj,M2)
g∗

/

(cid:114)

ˆDDD

(M1,M2)
j,j

, k ∈ N+, j = 1, 2, . . . , d,

(2.11)

(M1,M2)

ˆDDD

=

1
M2 − M1

(cid:88)

(cid:16)

i,λ(ˆθθθM2)
g∗

(cid:17) (cid:16)

i,λ(ˆθθθM2)′(cid:17)
g∗

i,λ(ˆθθθM2) = g∗
g∗

i (ˆθθθM2) − p′

M1<i≤M 2
λ(|ˆθθθM2|).

,

(2.12)

22

---

<!-- PAGE 24 -->

being ˆDˆDˆD(M1,M2). ˆDˆDˆD(M1,M2) is regarded as the sample covariance matrix of g∗

From (2.10) to (2.12), the detector is in the form of a standardized PEF, with the scaling matrix
i,λ(ˆθˆθˆθM2). M2 is the
training sample size of the durations. M1 (M1 < M2) serves as a length of burn-in period, which is

part of the training period, because PEF approach takes a certain number of iterations to reach to

a relative stable stage of θθθ estimation. Truncating the burn-in period of the parameter estimation

stabilizes the scaling matrix ˆDˆDˆD(M1,M 2). Consequently, after the training period M2, the detector

statistic GGGM2(k) at the time M2 + k is accessible as a function value of estimated parameters from
training period, ˆθˆθˆθM2, new observed data {xM2+1, xM2+2, . . . , xM2+k}, and tuning parameter λ.

2.3.3.1 Spillover effect The detector statistic in (2.10) contains the partial derivatives of

the martingale estimating function for each parameters. However, any parameter change doesn’t

coincide with just the change of an individual component of the detector statistic due to the inter-

correlation among the components, known as the spillover effect.

Spillover effect theoretical justification: For the two major terms aside from the penalty

expression p′

λ(|θθθ|) in the penalized estimating function in (2.5), each element of the two vectors is

involved with the terms ⟨m⟩i, ⟨Q⟩i and ηi, and they can’t be canceled in the computation. In the

structure of ψi in (2.2), any parameter change will lead to a change on the value of ψi. In a log

ACD (p, 0) framework (2.2), the derivative of ψi with respect to θθθ = (ω, α1, α2, . . . , αp)T becomes,

∂ψi
∂θθθ

= (1, log xi−1, log xi−2, . . . , log xi−p)′.

(2.13)

In the expressions of a∗

i−1(θθθ) and b∗

i−1(θθθ) in (2.6), the conditional mean of xi is,

µi(θθθ) = E[xi|F x

i−1] = exp{ψi} ·

µϵ
µϵ

,

(2.14)

and the derivative of µi(θθθ) with repect to θθθ = (ω, α1, α2, . . . , αp)T can be derived using the

chain rule,

∂µi(θθθ)
∂θθθ

=

∂µi(θθθ)
∂ψi

·

∂ψi
∂θθθ

= exp{ψi}(1, log xi−1, log xi−2, . . . , log xi−p)′.

(2.15)

23

---

<!-- PAGE 25 -->

For the quadratic variation and covariation, they can also be expressed in terms of ψi

⟨m⟩i = σ2

i (θθθ) = exp{2ψi}

σ2
ϵ
µ2
ϵ

,

⟨Q⟩i = κi(θθθ) − σ4

i (θθθ) = exp{4ψi}

κϵ
µ4
ϵ

,

⟨m, Q⟩i = γi(θθθ) = exp{3ψi}

γϵ
µ3
ϵ

,

(2.16)

where µϵ, σ2

ϵ , γϵ, κϵ are the mean, variance, third and fourth moments of the error ϵi in (2.2),

respectively.

Inserting the quantities into (2.6), we have,

a∗
i−1(θθθ) =

(cid:18)

1 −

(cid:18)

=

1 −

b∗
i−1(θθθ) =

(cid:18)

1 −

(cid:18)

=

1 −

γ2
ϵ
σ2
ϵ · κϵ

γ2
ϵ
σ2
ϵ · κϵ

γ2
ϵ
σ2
ϵ · κϵ

γ2
ϵ
σ2
ϵ · κϵ

(cid:19)−1 
−

∂ψi
∂θθθ

·

(cid:19)−1



−

·

∂ψi
∂θθθ

1
exp{ψi} · σ2
ϵ
µ2
ϵ

1
exp{ψi} · σ2
ϵ
µ2
ϵ

γϵ · µ2
ϵ

+ 2 exp{2ψi}

σ2
ϵ
µ2
ϵ

·

∂ψi
∂θθθ

·

γϵ · µ2
ϵ

exp{3ψi} · σ2

ϵ · κϵ





+ 2

γϵ
exp{ψi} · κϵ



 ,

(cid:19)−1 (cid:34)

∂ψi
∂θθθ

(cid:19)−1

·

∂ψi
∂θθθ

ϵ · κϵ

exp{3ψi} · σ2
(cid:34)

γϵ · µ2
ϵ

exp{3ψi} · σ2

ϵ · κϵ

− 2 exp{2ψi}

σ2
ϵ
µ2
ϵ

−

2σ2
ϵ
exp{2ψi} κ
µ2
ϵ

(cid:35)

∂ψi
∂θθθ

·

1
exp{4ψi} κ
µ4
ϵ

·

(cid:35)

.

Therefore, g∗

i,λ(θθθ) can be found as

g∗
i,λ(θθθ) =

(cid:19)−1

(cid:18)

1 −

γ2
ϵ
σ2
ϵ · κϵ

·

∂ψi
∂θθθ



−

1
exp{ψi} · σ2
ϵ
µ2
ϵ

+ 2

γϵ
exp{ψi} · κϵ



 · (xi − exp{ψi})+

γϵ · µ2
ϵ

exp{3ψi} · σ2

ϵ · κϵ

−

2σ2
ϵ
exp{2ψi} κ
µ2
ϵ

(cid:35)

(cid:18)

·

(xi − exp{ψi})2 − exp{2ψi} ·

(cid:19)−1

(cid:18)

1 −

γ2
ϵ
σ2
ϵ · κϵ

(cid:34)

·

∂ψi
∂θθθ

− p′

λ(|θθθ|),

(2.17)

(cid:19)

σ2
ϵ
µ2
ϵ

(2.18)

where we note that the existence of ψi will have an impact on every element of the penalized

estimating function. This helps to justify the spillover effect. As such, our online detection algo-

24

---

<!-- PAGE 26 -->

rithm will mainly focus on the detection of the existence of parameter change instead of specifying

any particular varying parameters.

2.3.4 Hypothesis testing

In the hypothesis test of the detector statistic, we need to set up thresholds to decide if the break

point has occurred. Consequently, some alarm will be raised when |GM2

j

(k)| > Tα where Tα is a

threshold based on the significance level α.

Wiener process threshold: According to (Heyde, 1997), the estimating functions preserve

asymptotic normality property and (M2−M1)−1/2GM2

j

(k) can be approximated by

(cid:16)

(1 + k)Wj( k

1+k )

(cid:17)

, k ∈

[0, ∞) under the null hypothesis, where Wj(·), j = 1, 2, . . . , d are independent standard Wiener pro-

cess. The threshold for |GM2

j

(k)| can be chosen as Tα,W (k) = (M2 −M1)

1

2 (1+k/(M2 −M1))g(k, M2)

and (Berkes et al., 2004) proposed that a constant boundary function g(k, M2) = c is sufficient. As

an asymptotic result, Wiener process threshold has a loss of accuracy if the sample size is limited.

To accommodate scenarios with small sample sizes, we will consider the empirical distribution of

the detector statistic under the null hypothesis.

Bootstrap threshold: Note that GGGM2(k) is a standardized partial sum of g∗

i,λ(ˆθθθM2). When
i,λ(ˆθθθM2) becomes a function of only xi, with λ being
ˆθθθM2 is calculated from the training period, g∗
given. Therefore, GGGM2(k)|ˆθθθM2 can be regarded as a function f (xM2+1, xM2+2, . . . , xM2+k|ˆθθθM2, λ).

Under the null hypothesis, we will implement a bootstrap method to sample from the stationary

time series in the training period, {x1, x2, x3, . . . , xM2}. Inserting the bootstrap sampled time series

into the GGG function provides the empirical distribution of the quasi-score function GGGM2(k), and its

empirical quantiles become accessbile as bootstrap thresholds. There is an abundance of literature

of the bootstrap method on time series analysis (B¨uhlmann, 2002; Politis, 2003). We will apply

the block bootstrap resampling approach with a random block length (Politis and Romano, 1994)

to obtain resampled time series for the monitoring period from the training period and summarize
a distribution for GGGM2(k)|ˆθθθM2, λ. The procedure is illustrated as follows: 1) Based on the training

series samples x∗

period {x1, x2, . . . , xM2}, we implement the block bootstrap sampling method to collect the times
(M2+k)b∗, k = 1, 2, . . . , b∗ = 1, 2, . . . , nb, of sample size, nb, for the monitoring period
as shown in Table 1. 2) Through insertion of the time series samples, we obtain the samples of

GM2
j

(k), j = 1, 2, . . . , d in the monitoring period, i.e, {GM2

j,b∗(k)}, j = 1, 2, . . . , d, b∗ = 1, 2, . . . , nb.

25

---

<!-- PAGE 27 -->

(cid:97)(cid:97)(cid:97)(cid:97)(cid:97)(cid:97)(cid:97)

B

t

M2 + 1
M2 + 2
M2 + 3
M2 + 4
M2 + 5
...
M2 + k
...

1

2

3

x∗
(M2+1)1
x∗
(M2+2)1
x∗
(M2+3)1
x∗
(M2+4)1
x∗
(M2+5)1

...

x∗
(M2+1)2
x∗
(M2+2)2
x∗
(M2+3)2
x∗
(M2+4)2
x∗
(M2+5)2

...

x∗
(M2+1)3
x∗
(M2+2)3
x∗
(M2+3)3
x∗
(M2+4)3
x∗
(M2+5)3

...

(M2+k)1 x∗
x∗

(M2+k)2 x∗

(M2+k)3

...

...

...

. . .

. . .
. . .
. . .
. . .
. . .
...
. . .
...

nb

x∗
(M2+1)nb
x∗
(M2+2)nb
x∗
(M2+3)nb
x∗
(M2+4)nb
x∗
(M2+5)nb

...

x∗
(M2+k)nb

...

Table 1: Sampled time series from block bootstrap

See Table 2. 3) The bootstrap threshold, Tα,j,B(k) at time t = M2 + k, can be evaluated as the

empirical α-quantile of GM2

j

(k), j = 1, 2, . . . , d.

(cid:97)(cid:97)(cid:97)(cid:97)(cid:97)(cid:97)(cid:97)

k

j

1
2
3
4
5
...
k
...

{GM2
{GM2
{GM2
{GM2
{GM2

b∗=1

b∗=1

b∗=1

1
1,b∗(1)}b∗=nb
1,b∗(2)}b∗=nb
1,b∗(3)}b∗=nb
1,b∗(4)}b∗=nb
1,b∗(5)}b∗=nb
...
1,b∗(k)}b∗=nb
...

b∗=1

b∗=1

b∗=1

{GM2

{GM2
{GM2
{GM2
{GM2
{GM2

b∗=1

b∗=1

b∗=1

2
2,b∗(1)}b∗=nb
2,b∗(2)}b∗=nb
2,b∗(3)}b∗=nb
2,b∗(4)}b∗=nb
2,b∗(5)}b∗=nb
...
2,b∗(k)}b∗=nb
...

b∗=1

b∗=1

b∗=1

{GM2

{GM2
{GM2
{GM2
{GM2
{GM2

b∗=1

b∗=1

b∗=1

3
3,b∗(1)}b∗=nb
3,b∗(2)}b∗=nb
3,b∗(3)}b∗=nb
3,b∗(4)}b∗=nb
3,b∗(5)}b∗=nb
...
3,b∗(k)}b∗=nb
...

b∗=1

b∗=1

b∗=1

{GM2

. . .

. . .
. . .
. . .
. . .
. . .

. . .

{GM2
{GM2
{GM2
{GM2
{GM2

b∗=1

b∗=1

b∗=1

d
d,b∗(1)}b∗=nb
d,b∗(2)}b∗=nb
d,b∗(3)}b∗=nb
d,b∗(4)}b∗=nb
d,b∗(5)}b∗=nb
...
d,b∗(k)}b∗=nb
...

b∗=1

b∗=1

b∗=1

{GM2

Table 2: Detector statistics computed from resampled time series from block bootstrap

Mahalanobis distance threshold: In the computation of the bootstrap threshold proce-

dure above, there is one concern when we collect the bootstrap samples for the j-th parameter,

{GM2

j,b∗(k)}b∗=nb

b∗=1 , j = 1, 2, . . . , d, at time point M2 + k. Due to the correlation among the vec-
tor GGGM2(k) known as the spillover effect, the computation of bootstrap threshold for individual

GM2
j

(k) doesn’t take this correlation structure into account, and results in a conservative threshold

from individual {GM2

j,b∗(k)} independently. To remedy the lack of association among the individ-

ual bootstrap thresholds, we will use a Mahalanobis distance based threshold to incorporate the

spillover effect within the detector statistics GGGM2(k). We regard the bootstrap samples of the

vectors {(GM2

1,b∗(k), GM2

2,b∗(k), . . . , GM2

d,b∗(k))′}b∗=nb

b∗=1 as the empirical multivariate distribution of the

26

---

<!-- PAGE 28 -->

M,b∗(k)}b∗=nb
GGG (GGGM2

b∗=1

detector statistic GGGM2(k) at monitoring timestamp M2 + k and compute the Mahalanobis distance

(Aggarwal, 2017). The Mahalanobis distance threshold can be found in the following steps,

Step 1 At time stamp t= M2 + k, collect bootstrap samples of the vector of detector statistics

{GGGM2

b∗ (k)}b∗=nb

b∗=1 = {(GM2

1,b∗(k), GM2

2,b∗(k), . . . , GM2

d,b∗(k))T }b∗=nb
b∗=1 .

Step 2 Compute the sample mean µµµGGG and the sample covariance matrix SSSGGG of {GGGM2

b∗ (k)}b∗=nb

b∗=1 , and

use them to approximate population mean and covariance matrix of the empirical multivariate

distribution for GGGM2(k).

Step 3 Compute the squared Mahalanobis distances d2

b∗ (k) − µµµGGG),
b∗ (k) is the vector of detector statistics on the b∗-th bootstrap sample time series.

b∗ (k) − µµµGGG)T SSS−1

M,b∗(k) = (GGGM2

GGG (GGGM2

where GGGM2

Step 4 Compute the desired quantile, e.g, the 95% quantile, from {d2

to compare with

the observed Mahalanobis distance d2

M(k) = (GGGM2

obs (k)−µµµGGG)T SSS−1

obs (k)−µµµGGG) where GGGM2

obs (k)

is the observed detector statistic at M2 + k computed from the real-time data stream in the

monitoring period.

Remark: We opt for the empirical threshold of the Mahalanobis distance instead of using a

Chi-square distribution quantile as an approximation, because the normality assumption for the

multivariate bootstrap samples is not always satisfied in real applications. See Figure 1 and 2 from

a single realization example of some simulated time series for illustration. We note that not all

the marginal bivariate distributions have the characteristics of bivariate Gaussian. We can also

see that when the monitoring period (starting at M2 + 1 = 2501) is before the true break point

τ = 3500, the observed detector statistics GM2

j

(k) fall within the clusters of bootstrap samples of

GM2

j,b∗(k). However, when the monitoring process is past the true break point τ = 3500, some of the

observed detector statistics GM2

j

(k) will deviate from the clusters of bootstrap samples of GM2

j,b∗(k).

The Mahalanobis distance takes the observed vector detector statistic as an entirety to detect the

outlier at a multi-dimensional level.

2.3.5 Ensemble detection

2.3.5.1 Motivation of ensemble detection We’ve listed three types of thresholds for hy-

pothesis testing and each type of threshold has its own pros and cons.

27

---

<!-- PAGE 29 -->

Figure 1: Scatter plot of detector statistics at time stamp M2 + k = 3000 when τ = 3500. The red dots are
observed detector statistic and black dots are bootstrap samples of the detector statistics

Figure 2: Scatter plot of detector statistics at time stamp M2 + k = 4000 when τ = 3500. The red dots are
observed detector statistic and black dots are bootstrap samples of the detector statistics

1. Wiener process thresholds are convenient for quick computation and have a good control of

the type I error at the onset of the monitoring period but it can be quickly exceeded by the

detector statistics in the absence of a structural break.

2. Bootstrap thresholds are conservative and provide delayed detection of structural break due

to the lack of the consideration for the correlation among the individual detector statistics

GM2
j

(k).

3. Mahalanobis distance threshold is able to account for the correlation among the individual

detector statistics. However, the distribution of Mahalanobis distance has a centroid and

spread approximated by bootstrap sample mean vector and covariance matrix. Using thresh-

28

---

<!-- PAGE 30 -->

olds biased by sample outliers will impact the accuracy of break point detection performance.

To improve the overall performance of detection, we propose an ensemble detection scheme

to combine the three aforementioned thresholds in a unified framework. By consolidating all the

advantages of the three methods, we aim to maintain a high power of detection with a well-controlled

type I error. Prior to a detailed description of our method, we would like to clarify the objectives

of handling type I error and delay of detection in online financial duration time series.

Type I error: In the context of break point detection, the type I error is false detection before

the true break point, which means the break point is incorrectly declared while the structure of

the time series still remains identical to the training period. The type I error can be related to

several cases: 1) The detection scheme is too sensitive to noise in the monitoring period. 2) The

stationarity of the time series before the true break point doesn’t hold. 3) The monitoring period

is too long before the true break point occurs, so the accumulative noise in the long monitoring

period eventually drives the detector statistic to pass the threshold. Our ensemble scheme can

make adaptations to the extreme fluctuation in the first case scenario whereas the other two cases

raise concerns for general online methods. For this research, our ensemble scheme will provide a

viable solution to address the type I error issue.

Delay: The most ideal performance of any detection methods will declare a change point as

soon as the structure of the time series changes. We can achieve quick and accurate detection when

there is a dramatic change or jump at the break point. In general, for a mixture of signal and

noise in the time series, its signal-to-noise ratio determines the speed of a break point detection.

The bootstrap threshold is based upon the resampled time series from the training period, so data

from a different generating process will eventually trigger the bootstrap threshold in the monitoring

period. Due to the irregularity of the duration time series in our study, the delay between detection

and actual change points differs from real calendar time difference. For example, if the true break

is τ = 3500 and the detected break point is ˆτ = 3700, the time index lag is 200 but the calculation
of real delay is Ddelay = (cid:80)ˆτ

i=τ xi = x3501 + x3502 + · · · + x3700, which is data dependent. See Figure

3. In real applications, when the market is active and trading intensity is high, the online financial

durations are observed in small values with high frequency, if the average durations between events

are roughly 0.1 seconds, the delay of 200 durations will result in a 20-second delay in the real

29

---

<!-- PAGE 31 -->

calendar time. Similarly, the trading intensity shifts from high to low, the delay in calendar time

can be longer but this type of transition of the financial durations are of less interest to the decision-

makers and delay can be more tolerable.

Figure 3: The trace plot of duration of duration in the calendar time. The x-axis is calendar time (in seconds).
The y-axis denotes the value of duration. The lag between time indices of true break and detected break is 200 and
the delay time in the calendar time is 261.1051 s.

2.3.5.2 Ensemble detection scheme This detection scheme is described as a pseudo algo-

rithm below. The break point alarms are recorded in a sequence of δ(k), k = 1, 2, . . . .

Algorithm E-PEF detection
Input: {xk}∞
Output: {δ(k)}∞

k=M2+1

k=M2+1

1−αM

Compute observed GGGM2
olds, d2
bootstrap samples respectively.
if d2
(cid:16)

M(k) > d2
1−αM
TαB/2,j,B(k) < GM2
δ(k) = 1, k ← k+1

I

j

obs (k), Mahalanobis distance d2

M(k). Find out the corresponding thresh-
(k), {T1−αW ,W (k)} and {TαB/2,j,B(k), T1−αB/2,j,B(k)}, j = 1, 2, . . . , d, through the

(k) and ∃j ∈ {1, . . . , d}, s.t, I(|GM2
(cid:17)

j

(k) < T1−αB/2,j,B(k)

= 0 then

(k)| > T1−αW ,W (k)) = 1 and

else

δ(k) = 0, k ← k+1

end if

Remarks:

1. As mentioned before, the reason of using bootstrap threshold of Mahalanobis distance is

that the asymptotic normality of the GGGM2(k) may not be a valid assumption, although each

individual GM2

j

(k) preserves a roughly symmetric and bell-shaped distribution. The critical

30

---

<!-- PAGE 32 -->

value of a Chi-squared distribution will give a lower threshold comparing with a heavier-tailed

distribution.

2. Structrual break at M2+k will be declared only when both the observed Mahalanobis distance

d2
M(k) exceeds the Mahalanobis distance threshold d2
GM2
j

(k) exceeds its Wierner process and bootstrap thresholds.

1−αM

, and at least one of the individual

3. The algorithm contains multiple hypothesis testings, we take the Bonferroni’s method to

control the overall false discovery rate.

To have a detailed illustration of the type I error rate from the aforementioned algorithm, we

denote the following events at monitoring time t = M2 + k:

• A(k) : d2

M(k) > d2

1−αM

(k)

• Bj(k) : I(|GM2

j

(k)| > T1−αW ,W (k)) ·

(cid:16)

1 − I(TαB/2,j,B(k) < GM2

j

(cid:17)
(k) < T1−αB/2,j,B(k))

= 1 1

We use δ(k) to denote the break point detection indicator at t = M2 + k. Then the theoretical

type I error under the null hypothesis of no break point can be derived and controlled as:

P r(δ(k) = 1|H0) = P r




A(k)



d
(cid:91)

(cid:92)
{

j=1

Bj(k)}H0






< P (A(k)|H0) + P (

d
(cid:91)

Bj(k)|H0)

j=1

≤ αM +

d
(cid:88)

j=1

P (Bj(k)|H0)

d
(cid:88)

(cid:16)

≤ αM +

P ({|GM2

j

(k)| > T1−αW ,W (k)} ∩ {T1−αB/2,j(k) < GM2

j

(cid:17)
(k) < TαB/2,j(k)}c)

≤ αM +

j=1

d
(cid:88)

j=1

(αW + αB) = αM + d · αW + d · αB

(2.19)

From E.q (2.19), we can control the type I error by choosing the proper αM, αW , and αB. In

the simulation study, we set αM = d · αW = d · αB = αoverall/3 to control the type I error under

αoverall = 0.05. Given the motivation and theoretical support, the performance of our E-PEF

method will be evaluated in the next subsections.

1I(.) is the indicator of an event.

31

---

<!-- PAGE 33 -->

2.4 Numerical study

In this section, the performance of E-PEF method is evaluated through extensive simulation study.

Some empirical guidelines can be provided for practical implementation. The real application of

E-PEF method is demonstrated through monitoring inter-trade duration time series from WRDS

Trade and Quote data.

2.4.1 Simulation

For simulation studies,we will demonstrate E-PEF method through three different aspects. The

first aspect addresses the common limitation of online detection studies, i.e., the false detection rate

control can only be controlled within a finite monitoring window. We also show this feature of our

method. Second aspect deals with the operating characteristics in terms of detection probabilities

for different structural breaks. The detection probabilities is regarded as false detection (type I

error) rate before the true break, and detection power after the true break. The last aspect is

associated with real application. We will show the robustness of E-PEF method when the data is

non-stationary to address the non-stationarity concern for the real data.

The simulations are based upon the following model:

xi = exp(ψ(j)
i )

ϵ(j)
i
µ(j)
ϵ

,

where

ψ(j)
i = ω(j) +

pj
(cid:88)

k=1

α(j)
k log xi−k +

qj
(cid:88)

k=1

k ψ(j)
β(j)

i−k, j = 1, 2,

(2.20)

(2.21)

j = 1 is the model before the true break point τ and j = 2 is the model after the true break

point.

To illustrate the performance of our algorithm, we apply our method according to different

types of the model alteration. Below are the results for the ensemble detection outcomes for the

four scenarios of 500 simulations with different true break points (τ = 2700, 3000, 3500, 4000). The

tuning parameter λ is determined by grid search. Among a list of λ candidates from 0.1 to 100, we

select the model with the smallest Mean Absolute Deviation measure, i.e, M AD = 1
M2

(cid:80)M2

i=1 |xi−ˆxi|.

Then we conduct the E-PEF method upon the model of our choice.

32

---

<!-- PAGE 34 -->

Scenario 1:

ψi =




0.2 + 0.1 log xi−1 + 0.2 log xi−2,

1 < i ≤ τ



0.2 + 0.1 log xi−1 + 0.5 log xi−2,

τ + 1 ≤ i ≤ 7500

(2.22)

ϵ ∼ Weibull(.6, .7) for both segments.

Scenario 2:

ψi =




0.2 + 0.1 log xi−1,

1 < i ≤ τ



0.2 + 0.4 log xi−1,

τ + 1 ≤ i ≤ 7500

(2.23)

ϵ ∼ Gamma(.5, .5) for both segments.

Scenario 3:

ψi =





0.2 + 0.1 log xi−1 + 0.2ψi−1,

0.2 + 0.1 log xi−1 + 0.5 log xi−2,

1 < i ≤ τ

τ + 1 ≤ i ≤ 7500

(2.24)

ϵ ∼ Gamma(.5, .5) for both segments.

Scenario 4:

ψi =




0.6 + 0.1 log xi−1 + 0.2 log xi−2, 1 < i ≤ τ



0.2 + 0.1 log xi−1 + 0.2 log xi−2,

τ + 1 ≤ i ≤ 7500

(2.25)

ϵ ∼ Weibull(.8, .9) for both segments.

For Scenarios 1 and 2, transitions before and after the break point are only based upon one of

the AR coefficients within the log ACD framework of the same order. The different distributions

(Weibull and Gamma distributions) assigned on the innovations are used to justify the robustness

of our algorithm. Scenario 3 shows that when the model framework changes from an ARMA model

to an AR model, our method is also able to detect the change point in a timely manner. We

use Scenario 4 to mimic some of real data scenarios where the durations change from a long and

infrequent pattern to a short and volatile state, which is similar to the market with increasing

33

---

<!-- PAGE 35 -->

trading intensity. We select a higher intercept before the structural break point and a lower one

afterwards.

2.4.1.1 Monitoring horizon We first investigate the performance of E-PEF detection under

the circumstance of no break for different scenarios. We also implement our method using different

sizes of training data. Monitoring horizon (Berkes et al., 2004) stands for the maximum length

of the monitoring window if there is no structural break in the data generating process, i.e., the

detection probability is below the desired false detection (type I error) rate under the H0 of no break

point in the data. Therefore, as long as there is no structural break detected within the monitoring

horizon, practitioner can use the ongoing time series model to make statistical inference, with the

confidence that the parameters of the current model remain stable. However, extended monitoring

period beyond the monitoring horizon will inflate the false detection rate because cumulative noise

from the prolonged monitoring distorts the structural break detection. The monitoring horizon is

summarized in Table 3.

There are three main takeaways in the table, 1) the false detection rate can only be controlled

under a desired level within a monitoring window of finite length. Longer monitoring period leads

to a greater inflation of false detection rate, though the false detection rate increases slowly as the

monitoring window length increases. 2) a longer training period tends to prolong the monitoring

horizon in general, except for some tiny fluctuation in the detection probability at different k, which

is caused by the randomness for the bootstrap sampling. 3) As an empirical guidance for choosing

a practical length of monitoring period, a monitoring window of length 250-500 is preferred for a

desired false detection rate control when the training data is small (M2 < 2500), while practitioners

can expect a longer monitoring horizon of about 750-1000 if M2 ≥ 2500. Further trade-offs between

false detection rate and power will also influence the monitoring window, according to specific

demands from the practitioners.

In addition, it can be observed in Table 3 that ARMA framework (Scenario 3) as a data

generating process is more robust against false detection, so it has a longer monitoring horizon.

That means approximation using a high-order AR model works better when the online data are

generated under an ARMA framework than under a low-order AR framework.

34

---

<!-- PAGE 36 -->

Scenarios M2

(k =) 250

500

750

1000

1250

1500

1750

2000

2250

2500

1

2

3

4

2000
2500
3000
3500

2000
2500
3000
3500

2000
2500
3000
3500

2000
2500
3000
3500

0.004
0.012
0.01
0.006

0.004
0.006
0
0.016

0.006
0.012
0.006
0.016

0.028
0.012
0.01
0.01

0.018
0.008
0.016
0.014

0.014
0.016
0.022
0.01

0.02
0.016
0.008
0.014

0.036
0.02
0.016
0.014

0.03
0.014
0.016
0.018

0.018
0.022
0.022
0.012

0.028
0.018
0.024
0.022

0.034
0.038
0.018
0.016

0.024
0.022
0.014
0.024

0.034
0.026
0.026
0.012

0.036
0.028
0.018
0.022

0.048
0.026
0.022
0.012

0.03
0.026
0.016
0.02

0.04
0.034
0.03
0.014

0.04
0.038
0.028
0.026

0.064
0.03
0.03
0.02

0.034
0.032
0.03
0.026

0.046
0.036
0.032
0.02

0.056
0.046
0.034
0.026

0.066
0.038
0.024
0.024

0.054
0.04
0.026
0.026

0.072
0.042
0.044
0.026

0.086
0.052
0.038
0.036

0.076
0.046
0.036
0.032

0.06
0.044
0.026
0.03

0.082
0.044
0.046
0.038

0.092
0.052
0.04
0.032

0.074
0.062
0.044
0.044

0.072
0.058
0.034
0.046

0.088
0.06
0.058
0.054

0.102
0.058
0.044
0.038

0.086
0.064
0.054
0.056

0.078
0.062
0.042
0.052

0.102
0.08
0.07
0.048

0.116
0.064
0.054
0.038

0.098
0.084
0.046
0.068

Table 3: Detection probabilities in the monitoring horizon study. M2 is the length of training
period. k is the monitoring time point in the monitoring period after the training. The false
detection rate control α = 0.05.

2.4.1.2 Detection probability and Delay According to the result from monitoring horizon

summary, we choose the training period to be M2 = 2500, with the burn-in period M1 = 1500

for the detection simulation study. The performance of E-PEF is presented through two measures,

1) detection probabilities at different monitoring times. The false detection and power refer to

the detection probabilities before and after the true break points correspondingly. 2) Summary

statistics of average delay. Average delay reflects the sensitivity of the detection algorithm after

the occurrence of a structural break. These results are exhibited in Table 4 and Table 5.

From Table 4, E-PEF controls the false detection rate under the nominal level, α = 0.05 and

increases the detection power rapidly after the true structural breaks occur in the monitoring pro-

cedure. The E-PEF method has an overall satisfactory performance of detection, and a significant

detection power can be expected when there is a structural break involved with framework change,

e.g., from ARMA to AR in scenario 3. Detection power spikes up to 1 in a short period.

From Table 5, E-PEF method has different sensitivity levels for the different kinds of structural

breaks. For Scenario 1, 2, and 4, parameter changes within the same AR framework are detected

slower than the framework changes as in Scenario 3. In scenario 4, belated true break associated

35

---

<!-- PAGE 37 -->

Scenarios

τ

(M2 + k =) 2750

3000

3250

3500

3750

4000

4250

4500

4750

5000

1

2

3

4

2700
3000
3500
4000

2700
3000
3500
4000

2700
3000
3500
4000

2700
3000
3500
4000

0.02
0.012
0.01
0.012

0.02
0.006
0.006
0.004

0.06
0.01
0.01
0.01

0.008
0.012
0.014
0.014

0.636
0.014
0.012
0.008

0.548
0.016
0.018
0.018

0.996
0.012
0.014
0.012

0.442
0.026
0.022
0.02

0.962
0.324
0.012
0.006

0.924
0.192
0.02
0.024

1
0.882
0.02
0.02

0.918
0.184
0.034
0.028

0.99
0.854
0.018
0.026

0.98
0.724
0.028
0.036

1
1
0.028
0.024

0.996
0.686
0.026
0.028

1
0.982
0.228
0.02

0.998
0.922
0.134
0.036

1
1
0.636
0.044

1
0.946
0.152
0.032

1
1
0.724
0.03

1
0.978
0.492
0.046

1
1
0.998
0.042

1
0.998
0.538
0.038

1
1
0.932
0.2

1
1
0.812
0.132

1
1
1
0.486

1
1
0.844
0.13

1
1
0.982
0.59

1
0.998
0.936
0.368

1
1
1
0.952

1
1
0.962
0.442

1
1
0.998
0.876

1
1
0.986
0.698

1
1
1
0.998

1
1
0.994
0.746

1
1
1
0.968

1
1
0.994
0.87

1
1
1
1

1
1
1
0.924

Table 4: Detection probabilities at different monitoring time under different scenarios. τ is the true
break point. k is the monitoring time point in the monitoring period.

with a prolonged monitoring period, tends to give more false detection. For the application of

E-PEF, the delay in calendar time is data-dependent, so its conversion from the delay in the

time index doesn’t demonstrate the timeliness of the E-PEF detection without the summation

of durations between true break and the detected break. On the other hand, detection of minor

parameter changes within the same framework takes more streaming data for sufficient evidence but

the consequence of drawing inference from a slightly biased model is not too grave if practitioners

are just using the same model framework with subtle differences between the parameters. Since

our method has a high sensitivity to the model framework change, timely parameters update can

be made at the occurrence of such significant structural breaks.

2.4.1.3 Robust performance for non-stationary scenarios Since E-PEF method involves

stationary log ACD models, it is difficult for data in real application to abide by the stationarity

assumption. Therefore, we will demonstrate the robust performance of E-PEF method for non-

stationary data. Although non-stationary data can come in various forms, local non-stationarity

can be still described by a linear trend of quadratic trend. For a small size of monitoring horizon in

36

---

<!-- PAGE 38 -->

Scenarios

τ

(Delay) Mean

SD Min

Q1

Q2

Q3

1

2

3

4

2700
3000
3500
4000

2700
3000
3500
4000

2700
3000
3500
4000

2700
3000
3500
4000

264.61
326.45
391.14
445.36

294.25
387.09
511.92
570.34

116.46
162.77
214.87
249.72

329.49
411.03
490.85
561.95

126.30
159.08
200.63
245.48

147.70
184.97
261.74
312.38

49.02
72.36
96.01
118.72

141.60
182.23
242.63
287.58

97
109
71
65

106
135
136
82

48
60
63
37

131
130
117
142

173.5
211.5
251.75
269.75

185.75
251
325.75
332

82
109
140.5
167

221
278.5
311.25
341.75

240
301.5
372
424

266.5
359
480.5
545.5

109
153.5
202
247.5

309
390
459
519.5

328.25
412.75
501.25
585.25

372.25
485.75
656
749

143
206.25
283.25
327

422
531.25
643.25
743

Max

825
943
1257
1368

1167
1191
1780
1685

325
463
548
651

900
1032
1344
1596

Table 5: Summary statistics of average delay under different scenarios for different break points. τ
is the true break point. False detection rate control is α = 0.05. The length of training period is
M2 = 2500.

practice, it will sufficient to display the robust performance of E-PEF against non-stationary data

with a linear trend or quadratic trend.

The linear time trend and quadratic time trend are introduced in both segments before and

after the structural breaks as follows,

Scenario 1:

ψi =




0.2 + 0.05 log(i) + 0.1 log xi−1 + 0.2 log xi−2,

1 < i ≤ τ



0.2 + 0.05 log(i) + 0.1 log xi−1 + 0.5 log xi−2,

τ + 1 ≤ i ≤ 7500

(2.26)

ϵ ∼ Weibull(.6, .7) for both segments.

37

---

<!-- PAGE 39 -->

Scenario 2:

ψi =




0.2 + 0.1 log(i) + 0.1 log xi−1, 1 < i ≤ τ



0.2 + 0.1 log(i) + 0.4 log xi−1,

τ + 1 ≤ i ≤ 7500

(2.27)

ϵ ∼ Gamma(.5, .5) for both segments.

Scenario 3:

ψi =





0.2 + 0.05 log(i) − 0.01 log2(i) + 0.1 log xi−1 + 0.2ψi−1,

0.2 + 0.05 log(i) − 0.01 log2(i) + 0.1 log xi−1 + 0.5 log xi−2,

1 < i ≤ τ

τ + 1 ≤ i ≤ 7500

(2.28)

ϵ ∼ Gamma(.5, .5) for both segments.

Scenario 4:

ψi =




0.6 + 0.1 log(i) − 0.01 log2(i) + 0.1 log xi−1 + 0.2 log xi−2, 1 < i ≤ τ



0.2 + 0.1 log(i) − 0.01 log2(i) + 0.1 log xi−1 + 0.2 log xi−2,

τ + 1 ≤ i ≤ 7500

(2.29)

ϵ ∼ Weibull(.8, .9) for both segments.

For the non-stationary settings of 2.26,2.27,2.28,2.29, we consider assigning small coefficients

for the linear trend and the quadratic trend for two reasons, 1) large coefficient for a time trend can

quickly shrink the durations to zero or cause the overflow of the durations. 2) Small coefficients for

the trend terms can generate similar ranges of the durations, which are consistent with the ones

for real data.

Since our method performs universally well in all four scenarios with or without stationarity

assumption, we demonstrate the model results in Figure 4 (Scenario 1) for brevity. All the monitor-

ing processes start at M2 = 2500 and the structural break detection probabilities can be accessed

at different phases in the monitoring period. For the scenarios with different structural breaks, our

algorithm shows a good control of type I error under 0.05 before the true structural breaks occur.

Meanwhile, the detection probability increases quickly after the occurrences of the true structural

38

---

<!-- PAGE 40 -->

breaks.

For illustration, the intermediate steps are shown in the Figure 5 by a single time series realiza-

tion example from Scenario 1. (a) shows the observations xi with true break point at 3500 (at the

red vertical dashed line). (b) and (c) depict the trajectory of the observed detector statistic GGGM2(k)

and the Mahalanobis distance. The green shaded area in (b) is the combined confidence interval

based on the theoretical Wiener process threshold and the empirical bootstrap sample threshold.

The red horizontal line in (c) is the empirical bootstrap sample threshold for the Mahalanobis dis-

tance. (d) gives the binary results of break detection at each time point in the monitoring process

from i = 2500. From (d), the detected break point is around 3700, which is close to the true break

point τ = 3500.

Figure 4: Break detection outcome from 500 simulations of in a monitoring period of length 5000. X-axis stands
for the monitoring period starting at M2 = 2500. Y-axis stands for the empirical detection probability at a specific
time point. The blue dashed lines stand for the true break point τ = 2700, 3000, 3500, and 4000. The red dashed
lines stand for the significance level αoverall = 0.05.

For practical implementation, these results provide useful guidance for the decision-makers to

adjust their tolerance of the type I error and the preference of the sensitivity of the break detection.

These results also show that in Scenarios 1 and 2 where there is only one parameter change within

the same log ACD model framework, our algorithm is able to detect the structural break rapidly and

accurately. In Scenario 3 where there is a change on the type of the log ACD model, the detection

probability increases more quickly to 100% after the structural break occurs. Finally, since the

39

---

<!-- PAGE 41 -->

(a)

(b)

(c)

(d)

Figure 5: (a) A single realization of Scenario 1 with true break at τ = 3500;(b) The trace plot for the individual
GM2
(k) with the confidence intervals based on the Wiener process and bootstrap thresholds in green bands; (c) The
j
trace plot for the Mahalanobis distance d2
1−αM (k) (red horizonal line); (d) The trace
plot for the binary indicator of break detection δ(k)

M (k), with bootstrap threshold d2

detector statistic is based upon the quasi-score change instead of prediction on the observational

level, for Scenario 4 we are able to implement the structural break detection if there is an increasing

trading intensity between two phases of financial duration time series. Additional simulation results

for Scenarios 2, 3, and 4 are provided in the supplemental material.

2.4.2 Real application

In addition to the extensive simulation study to illustrate our method in different scenarios, we also

implement it for some real financial duration data. We are able to detect the structural breaks and

associate them with some financial information that may trigger these structural breaks. Nonethe-

less, real data applications of our method need attentions to different aspects of implementation.

To get a meaningful monitoring process and identify outbreaks of interest, practitioners need to

consider the general features of the financial durations and idiosyncratic characteristics of different

assets.

In existing retrospective studies of structural break detection, the raw time series data can be

adjusted universally to filter out some common structures and enhance the model’s adequacy. For

40

---

<!-- PAGE 42 -->

example, Zhang et al. (2018) performed structural break detection in a retrospective fashion, and the

complete intra-day financial durations were adjusted through a linear regression to accommodate

the diurnal effect, which is displayed as higher trading intensity in the opening and closing period

of the stock market. However, since our ensemble method processes real-time streaming data in

practice, we cannot replicate the same retrospective adjustment for online break detection. If the

aim is to detect some non-diurnal-effect-related structural breaks, we suggest discarding the first

and last 30-minute time windows and applying the algorithm to diminish the diurnal effect.

Due to the flexible definition of a financial event, users can feel free to choose the price or

return changes as the target events to collect the online duration time series based on individual

risk tolerance and trading preferences. Besides, we also recommend market participants customize

their monitoring process according to the characteristics of individual assets and set proper tuning

parameters for the monitoring such as the length of the training period.

As illustrated in the examples in real applications, we apply our break detection method to four

specific stocks: IBM, BAC, MMM, and GE, and explore the dynamic structures underlying the

financial durations. We choose the price changes between two successive transactions exceeding a

pre-specified amount, δ, as the financial events. The financial durations are computed from the

WRDS Trade and Quote data in June 2013 (Zou et al., 2015). Following a common approach used

by financial professionals, we used the data from the previous month (May 2013) to calculate the

average turnover ratio as average daily volume divided by total shares outstanding. Therefore,

δ = 0.00377, 0.004, 0.00376, 0.00408 for GE, BAC, IBM, and MMM respectively.

When it comes to the tuning parameters, a meaningful monitoring process needs to accommo-

date the liquidity of the assets. GE and BAC are liquid stocks with high trading volumes (100,000

to 200,000 transactions per day on average) and a relatively low price spread of about $ 0.5 per day

on average. Meanwhile, IBM is also a liquid stock with a medium number of average transactions

per day (around 20,000) with an absolute price spread between $3 and $4. MMM has variable low

numbers of transactions (between 4000 and 15,000 per day) and absolute price spread of about $1.5.

In practice, for the liquid assets, we choose a longer training period for better model adequacy. But

for the less liquid assets such as MMM, the number of transactions can be very small. Therefore,

we suggest choosing a shorter training period and λ candidates of large values in the penalty term

p′
λ(|θθθ|) of the penalized estimating function for grid search, in order to enhance model stability in

41

---

<!-- PAGE 43 -->

the recursive estimation procedure during the training period.

To reflect the market behaviour and trading intensity through the pattern change of financial

durations, we apply the ensemble detection method to a log ACD (20, 0) as the training model for

the break detection. All transactions are selected from 10:00 a.m. and 3:30 p.m.. We are able to

detect some structural breaks, and benchmark with published financial news for these companies

on the same day, or during off hours before. With the detected breaks shown in Figure 6, We list

the break detection results as well as their related financial news for stocks IBM, BAC, MMM, and

GE respectively.

On June 4th, the structrural break of IBM was detected at around 1:01 p.m.. A piece of

financial news about IBM was released on June 4th at 9:11 a.m.. From The New York Times,“

I.B.M. announced on Tuesday that it had agreed to buy SoftLayer Technologies, a cloud computing

company, in an effort to strengthen I.B.M.’s position in the fast-growing market for computing sold

to businesses as a service delivered over the Internet.”.

On June 5th, the structrural break of BAC was detected at around 10:33 a.m.. We have also

found a piece of financial news about Bank of America on June 4th at 9:47 p.m was as follows.

From Reuters, “NEW YORK, June 4 (Reuters) - American International Group Inc argued on

Tuesday that a proposed $8.5 billion settlement between Bank of America Corp and investors in

Countrywide Financial Corp mortgage-backed securities was not big enough.”.

On June 10th, the structrural break of MMM was detected at around 13:10 p.m.. The CEO

of MMM reclaimed the company was research-driven and invested a large amount of money in its

research development on June 10th at 6.53 a.m. From CNBC, “In a lab in St. Paul, Minnesota,

engineers test solar panels and connectors. A half a mile away, a technician smashes the windows

of a car coated with 3M protective film, watching to see if the glass shatters or holds together. Else-

where, there are scientists working on more aerodynamic products for airplanes, software systems

to run a municipality’s department of motor vehicles, and light-sensor technology to create new

crowns for teeth in under 2 hours.”.

On June 24th, the structrural break of GE was detected at around 12:54 p.m., A recent event

that happened to GE incorporation was on June 22th (Saturday). From military aerospace, “Trans-

Digm Group Inc. (NYSE:TDG) has entered into a definitive agreement to acquire the assets of GE

Aviation’s Electromechanical Actuation Division for approximately $150 million in cash.”.

42

---

<!-- PAGE 44 -->

(a)

(b)

(c)

(d)

Figure 6: Structural break points detected (red vertical dash lines) in the duration time series of IBM,
BAC, MMM and GE respectively.

From real applications, our E-PEF method is able to detect break points in duration time series

and offers an adaptive framework incorporating different asset features. With detected change

points from online data, the practitioners can act proactively and seek for more evidence from

different sources of information such as market news to evaluate the asset or market behaviors.

With the combination of statistically detected break points and real world information, E-PEF

method can reassure practitioners to use adequate models for the online data and make subsequent

transactional decisions.

2.5 Summary

In a high-frequency trading setting, the financial duration models can give a reasonable interpre-

tation on the volatile behavior of the market in terms of trading intensity. Therefore, accurate

awareness of the structural breaks will provide helpful insights for the market participants to up-

date the statistical model as soon as a structural break is detected. In this article, we propose

an innovative E-PEF method in the online detection strategy for the log ACD model, which is a

prevalent tool for modeling financial durations. In the parameter estimation stage for the training

period, we take advantage of the PEF recursive estimation approach for the log ACD model regard-

43

---

<!-- PAGE 45 -->

less of the distribution of the innovations. In the online monitoring stage, we propose an ensemble

algorithm combining three different types of thresholds for the quasi-score functions to facilitate

structural break detection in the financial duration time series. We illustrate the performance of our

ensemble approach by extensive simulations under different scenarios. We implement our method

in real data applications to monitor the duration time series and detect some structural breaks

with various sources of financial information for a better interpretation of the market behavior.

Our contribution lies in the innovative ensemble online detection framework for financial du-

ration time series. This framework enjoys a distribution-free statistical inference on the log ACD

model with penalized estimating functions. The block bootstrap method provides the empirical

distribution of PEF from the observed training time series without additional parametric assump-

tions. Resampled data further lead to the incorporation of two new thresholds, the bootstrap

threshold and the Mahalanobis distance threshold, into the monitoring procedure. The detection

rule is formulated in an ensemble fashion integrating all three types of thresholds. The combined

advantages of both asymptotic and empirical properties of the online detector test statistic facilitate

the reduction of the false discovery rate. The E-PEF approach shows that the type I error can be

well controlled under a specific level while preserving a high power to detect any true breakpoints.

The merit of our method focuses on timely structural break detection under parameter changes in

an online fashion.

44

---

<!-- PAGE 46 -->

3 Multivariate latent level correlation model (LCM) for financial

high frequency count time series

3.1 Background

Volatility analysis helps investors navigate their asset positions to optimize their gains in the fi-

nancial market. As high-frequency, intra-day asset pricing data become increasingly available,

exploration and explanation for the micro-structure of the financial market behavior forms an im-

portant and popular research direction. The volatility study of the general financial data involved

with irregularity and intricacy already requires non-trivial methods for delicate statistical infer-

ence. The advancement of high frequency trading escalates the challenge with increased data size

as well as dimension. Prompt inference on high frequency financial data is in great demand for

the market participants. In a high frequency trading setting, the raw transactions are made within

milliseconds, and the corresponding price changes occur with various magnitudes of fluctuation.

Therefore, log returns for the asset price can be calculated based on these price changes. In ad-

dition to other different research-related definitions, our study use the count of the transactions

with extreme log return to describe the market volatility, and the extremeness of a log return is

determined by practitioners according to their interest. Within a given time interval, an asset with

higher volatility tend to have a larger count, which motivates one to implement discrete time series

model to account for the underlying market volatility.

Specifically, we convert transaction-by-transaction log returns to a multivariate count time

series by using a threshold τ > 0. During a given period of time, the transactions with the

absolute log return exceeding τ are categorized as high risk level, while the other are categorized

as low risk level. Therefore, for a specific asset, two types of count will be observed and studied

simultaneously. Under general circumstance of high frequency trading trading, the price changes

don’t have significant fluctuation thus the transactions of low risk level are expected to have a large

number of count, and such count has its own time dependent property. The count for transactions

of high risk level provide more insights on the volatility but the count may not be as abundant

as the former, due to the asset idiosyncrasy or the choice of τ . With the access to a plenitude

of low-risk-level transaction data, practitioners could have more options to adjust and refine their

45

---

<!-- PAGE 47 -->

investment strategy if they have a sound comprehension of the co-movement between these two

types of counts.

3.2 Literature review

3.2.1 Discrete time series modeling

Count time series arise naturally in numerous applied scientific fields such as finance, epidemiology,

agriculture, etc., and the analysis of such non-Gaussian data has been an active research area for

a long time. There is a rich literature on univariate modeling of count time series, both in the

frequentist and Bayesian frameworks. The frequentist approaches include discrete auto-regressive

moving average (DARMA) models (Jacobs and Lewis, 1983), integer-valued auto-regressive (INAR)

models (Al-Osh and Alzaid, 1987), and integer-valued GARCH (INGARCH) models (Ferland et al.,

2006). West et al. (1985) and Gamerman et al. (2013) have discussed Bayesian dynamic general-

ized linear models (DGLM). Financial applications of univariate count time series models include

Heinen (2003) who implemented the double exponential family GLM of Efron (1986) by introducing

the auto-regressive conditional Poisson model. They applied the model for volatility modeling of

price change count time series of IBM returns, exploiting the ability of the model to explain the

autocorrelation and overdispersion in the data. Liesenfeld et al. (2006) used an integer count hurdle

model with a negative binomial sampling distribution for stock transaction price changes. How-

ever, it is now widely accepted that financial data are time-dependent across assets and markets.

Although the aforementioned methodologies deal with univariate time series, their perspectives of

approaching the univariate time series modeling still facilitate the extension of multivariate time

series framework.

For analyzing multivariate count time series, we need models that not only explain the temporal

correlation within each series, while accommodating possible overdisperison, but also explain cross-

sectional correlation between the components. Pedeli and Karlis (2013) extended the INAR(1)

framework to the bivariate case. Karlis and Meligkotsidou (2005) discussed a multivariate Poisson

(MVP) distribution with a two-way covariance structure, while Karlis and Meligkotsidou (2007)

described a finite mixture of multivariate Poisson distributions which allows for both positive and

negative covariances between components. Ravishanker et al. (2014) used MVP sampling distribu-

46

---

<!-- PAGE 48 -->

tions and Gibbs sampling for hierarchical dynamic modeling for multivariate time series of counts

of gastropod abundance. Jung et al. (2011) proposed a parameter-driven approach for multivariate

count financial time series through a dynamic factor model incorporating both common and id-

iosyncratic factors in the conditional Poisson mean. Quoreshi (2017) fit a bivariate integer-valued

fractionally integrated moving average model to time series of counts of transactions in equally

spaced time intervals, and managed to accommodate the long-memory pattern of the integer-valued

time series. Aktekin et al. (2018) combined dynamic temporal parameters and individual static

parameters into a product as the Poisson means in the multivariate Poisson-scaled beta model,

and used forward filtering backward sampling (FFBS) and particle learning algorithms setting in

the dynamic online Bayesian updating. See Soyer and Zhang (2021) for an excellent review of

recent advances in multivariate count time series modeling. Despite the existent methodologies for

multivariate count time series, the concern about computational feasibility arises when it comes to

the high-dimension time series modeling, whether or not in frequentist or Bayesian approach. For

multivariate INAR or MVP, the computation for the probability mass function of a multivariate

discrete random variable requires a large number of summations from inverse mapping. As a con-

sequence, Expectation-Maximization (EM) algorithm for maximum likelihood estimation will be

slowed down significantly due to the increase of dimension even though the utilisation of recursive

relationships to calculate the conditional expectation can alleviate some of the computational bur-

den. For Bayesian approach, exact inference for joint posterior by MCMC sampling is also of great

difficulty because it is not uncommon for the posteriors to be intractable. Hence, the computation

of high dimensional integrals suffers from the posteriors that are not in a closed form.

A few alternative ideas have been proposed to carry out fast Bayesian modeling. West (2020)

proposed a decouple/recouple idea in DGLM for computational efficiency and model adequacy for

node-node dependency based upon the complete sets of posterior samples of the dynamic coeffi-

cients. Lavine et al. (2020) introduced copula modeling to multi-step, multi-scale, and dynamic

latent factors, using variational Bayes’ (VB) optimization (Blei et al., 2017). Being appealing to

provide comparable accuracy to Gibbs sampling at greater speed, VB approach often requires a

large amount of work to derive the set of equations for iterative parameter update. Therefore,

An alternative to VB for fast, approximate Bayesian modeling can be considered for statistical

inference, which is the integrated nested Laplace approximation, see Rue et al. (2009) or Rue et al.

47

---

<!-- PAGE 49 -->

(2017).

3.2.2 Integrated Nested Laplace Approximation (INLA)

A wide variety of models can be fit by INLA (G´omez-Rubio, 2020). In general, for a vector of n

observations yyy = (y1, . . . , yn), mean µi of observations yi can be related to the linear predictor ηi

through different link functions,.

ηi = α +

nβ
(cid:88)

j=1

βjzji +

nf
(cid:88)

k=1

f (k)(uki) + εi; i = 1, . . . , n,

(3.1)

where α is the intercept, βj, j = 1, . . . , nβ, are coefficients of the covariates {zzzj}nβ
f (k)(u) define nf random effects on the covariates {uuuk}nf

k=1. εi is the error term, and it can be

j=1, functions

missing depending on the likelihood. The vector of latent effect x is defined as,

xxx = (η1, . . . , ηn, α, β1, . . . ).

(3.2)

The distributions of yyy are dependent on the latent effect xxx and some hyperparameters θθθ1, and

the precision matrix for the Gaussian Markov Random Field (GMRF) of xxx is determined by some

other hyperparameters θθθ2. With the assumptions that xxx has a sparse structure of GMRF (Rue and

Held, 2005) as well as that yi’s are independent to each other given xxx, INLA will take advantage of

the sparse structure and conditional independence properties of GMRF to enhance computational

efficiency. Let θθθ = (θθθ1, θθθ2). Instead of obtaining the inference from the joint posterior distribution of

(xxx, θθθ), INLA focuses on the marginal inference on the latent effects and hyperparameters. Starting

with the form of joint posterior density of xxx and θθθ,

π(xxx, θθθ|yyy) ∝ π(θθθ)|QQQ(θ)|1/2 exp

(cid:26)

−

1
2

xxxT QQQ(θθθ)xxx

(cid:27) (cid:89)

i∈I

π(yi|xi, θθθ) =

π(θθθ)|QQQ(θ)|1/2 exp

−

(cid:40)

xxxT QQQ(θθθ)xxx +

1
2

(cid:88)

i∈I

log(π(yi|xi, θθθ))

(cid:41)
.

(3.3)

In order to get the posterior marginals, the approximation of the joint posterior of θθθ, ˜π(θθθ|yyy), is

proposed as,

˜π(θθθ|yyy) ∝

π(xxx, θθθ, yyy)
˜πG(xxx|θθθ, yyy)

|xxx=xxx∗(θθθ),

48

(3.4)

---

<!-- PAGE 50 -->

where ˜πG(xxx|θθθ, yyy) can be a Gaussian approximation or Laplace approximation at the model of the

full conditiona, xxx∗(θθθ) . Hence, the marginals for the individual latent effect xl and hyperparameter

θk become available,

(cid:90)

(cid:90)

π(xl|yyy) =

π(θk|yyy) =

π(xl|θθθ, yyy)˜π(θθθ|yyy)dθθθ,

˜π(θθθ|yyy)dθθθ−k.

(3.5)

INLA has been widely used in several applications of time series. Ruiz-C´ardenas et al. (2012)

discussed a variety of state-space dynamic models, including count time series modeling. Schr¨odle

and Held (2011) described disease count data modeling through incidence rates, while Salmon et al.

(2015) discussed a Bayesian approach for detecting outbreak in an infectious disease surveillance

system. Sadykova et al. (2017) used zero-inflated and hurdle Poisson spatio-temporal models for

predator-prey and competitor species habitat. Serhiyenko et al. (2018) implemented a latent level

correlation model (LCM) using INLA for dynamic modeling of multivariate counts in a marketing

application involving monthly prescriptions written by physicians for a pharmaceutical company’s

drugs. Riebler and Held (2017) used the INLA approach for age-period-cohort analysis. Raman

et al. (2020) explored different univariate static and dynamic models using INLA for evaluating

promotions of marketing schemes.

3.3 BVAR(1)-LCM model

In this chapter, we propose a fast and accurate Bayesian framework for correlated bi-variate count

time series with latent level correlation (BVAR(1)-LCM) using the INLA approach. The aim is to

describe the association between the two count time series across multiple assets and exhibit some

model parameters of interest to better explain the microstructure of the financial market. Despite

the elevated model complexity, our method enjoys computational speediness due to the sparsity of

Gaussian Markov Random Field (GMRF) among the model parameters. Fast Bayesian inference

approximation can be obtained with good quality, and practitioners can study the dynamics within

and between the count time series in a higher dimension efficiently.

49

---

<!-- PAGE 51 -->

3.3.1 Model framework

Let {Yj,st} denote the count for j-th type of transaction for s-th asset in the t-th time interval, j =

1, 2, . . . , J, s = 1, 2, . . . , S and t = 1, 2, . . . , T . Since we study the association between transaction

count with a low-risk level and the one with a high-risk level, J = 2. S is the total number of

assets involved in the framework and T is the total number of time intervals. To account for

the temporal and cross-sectional association among the assets, we implement a Bayesian Poisson

Lognormal framework conditioned on various sources of fixed or random effects:

Yj,st|λj,st

ind∼ P ois(λj,st),

ηj,st = log λj,st = ZZZjβββj + γj,t + αj,st,

γj,t = ϕjγj,t−1 + ωj,t,




ωωωt =

ΣΣΣωωω =









ω1,t

ω2,t


 ∼ N (000, ΣΣΣωωω) ,




 ,

σ2
ω1

ρωωωσω1σω2

ρωωωσω1σω2



σ2
ω2

αααst =




α1,st

α2,st


 ∼ N (000, ΣΣΣααα) ,






ΣΣΣααα =

σ2
α1

ρααασα1σα2

ρααασα1σα2

σ2
α2




 .

(3.6)

In (3.6), ZZZj and βββj are respectively covariates (intercept included) and coefficients. γj,t is the

temporal random effect with an AR process for j-th type of count. Since they are two types of

count involved, j takes values of either 1 or 2. The innovation terms ωj,t for the two AR processes

have the correlation coefficient, ρω. σ2

ω1 and σ2

ω2 are correspondingly the variances for the AR

innovations. αααst is the level correlated random effect, ΣΣΣααα is its variance-covariance matrix.

The benefit of Poisson-Lognormal distribution has been discussion in Aitchison and Ho (1989).

It not only retains the interpretability of the parameters in the model but also it well addresses

the overdispersion issue encountered by a standard Poisson distribution. Considering a simple

50

---

<!-- PAGE 52 -->

univariate Poisson-Lognormal random variable:

Y |λ ∼ P ois(λ),

log λ|µ, σ2 ∼ N (µ, σ2).

(3.7)

Using the laws of total expectation and variance we can easily derive the conditional expectation

E(Y |µ, σ2) and the conditional variance V ar(Y |µ, σ2).

For E(Y |µ, σ2), we have,

E(Y |µ, σ2) = Eλ|µ,σ2

(cid:0)E(Y |λ, µ, σ2)(cid:1)

= Eλ|µ,σ2 (E(Y |λ)) = Eλ|µ,σ2(λ)

= Eλ|µ,σ2(elog λ) = eµ+σ2/2.

For V ar(Y |µ, σ2), we have,

V ar(Y |µ, σ2) = Eλ|µ,σ2

(cid:0)V ar(Y |λ, µ, σ2)(cid:1) + V arλ|µ,σ2

(cid:0)E(Y |λ, µ, σ2)(cid:1)

= Eλ|µ,σ2 (V ar(Y |λ)) + V arλ|µ,σ2 (E(Y |λ))

= Eλ|µ,σ2(λ) + V arλ|µ,σ2(λ)

= Eλ|µ,σ2(elog λ) + V arλ|µ,σ2(elog λ)

= eµ+σ2/2 + (e2µ+2σ2

− e2µ+σ2

)

= E(Y |µ, σ2) + e2µeσ2

(eσ2

− 1).

(3.8)

(3.9)

From Equations 3.8 and 3.9, σ2 can well account for the overdispersion or underdispersion of

distribution through the sign of eσ2 − 1.

In the d-dimensional multivariate setting for Poisson-Lognormal distribution denoted by P Λd(µ, Σµ, Σµ, Σ),

with µµµ = (µ1, . . . , µd)′ and ΣΣΣ = (σii)d×d (Aitchison and Ho, 1989; Serhiyenko et al., 2018), another

advantage of this distribution is that it can recover both positive and negative correlation between

two count variables, which presents the bottleneck to a bivariate Poisson distribution. For a mul-

tivariate Poisson-Lognormal variable YYY = (y1, . . . , yd)′, its probability density function could be

expressed through the integration of the latent variable λλλ = (λ1, . . . , λd)′,

51

---

<!-- PAGE 53 -->

p(YYY |µ, Σµ, Σµ, Σ) =

(cid:90)

d
(cid:89)

Rd
+

i=1

f (yi|λi) · N d(λλλ|µ, Σµ, Σµ, Σ)dλλλ.

(3.10)

The expectation, variance and correlation between each pair of the count variable are found as:

E(Yi|µ, Σµ, Σµ, Σ) = exp(µi + σii/2) = mi,

V ar(Yi|µ, Σµ, Σµ, Σ) = mi + m2

i (exp(σii) − 1),

Corr(Yi, Yj|µ, Σµ, Σµ, Σ) =

(cid:104)
(exp(σii) − 1 + m−1

exp(σij) − 1
i )(exp(σjj) − 1 + m−1
j )

(cid:105)1/2

(3.11)

.

For the count data, there is a lower bound zero thus leading to the difficulty of recovering a

strong negative correlation between two count variables, i.e, when one approaches infinity, the other

one will approach zero instead of exploding into negative infinity. However, Poisson-Lognormal

distribution still exhibits a wide range of correlation coverage and works impressively well when

there exists a positive correlation between two count variables.

Incorporating the latent level correlation structure, represented by ΣΣΣ, is inspired by the fact

that in real life many other important covariates are not collected or even not observable but have a

significant impact on the count variables. Therefore, neglecting the potential correlation structure

can gravitate to a biased inference and prediction. With the interrelated multivariate Poisson-

Lognormal model for each specific count variable, we can explain the inherent pattern across the

different count data. In the noisy high-frequency financial data, the incorporation of latent level

correlation helps reduce biased inference.

The applications of multivariate Poisson-Lognormal distribution have been demonstrated in

transportation crash counts using MCMC approach for inference (Park and Lord, 2007; Ma et al.,

2008) . However, their approach only handles the crash counts of different severity levels but with

no temporal random effect.

In other words, the size of crash count data is much smaller than

the high-frequency count data due to the absence of time index. In volatility analysis, temporal

dependence is commonly considered and so does our method. As a consequence, high-frequency

count data with a larger size pose an even bigger computational challenge for MCMC approach

especially when more parameters and latent effects are considered in the model. We will next

52

---

<!-- PAGE 54 -->

address this problem with Integrated Nested Laplace Approximation (INLA) approach.

3.3.2 INLA implementation

As mentioned in the previous work, despite the benefits of Poisson-Lognormal models, the com-

plexity of such models influences their computational cost, especially when a larger number of

parameters need to be incorporated. MCMC method can become very computationally expensive

as it computes the joint posterior distribution of model parameters in a high dimension space. How-

ever, INLA approach instead targets the individual posterior marginals, which usually are sufficient

for statistical inference on the model parameters and latent effect, and there is no need to handle

complicated joint posterior distributions. Fortunately, the parameters in the Poisson-Lognormal

framework can be regarded as a Gaussian Markov Random Field (GMRF), i.e, a finite-dimensional

random vector following a multivariate Gaussian distribution (Rue and Held, 2005). With the

conditional independence assumptions, INLA takes advantage of the sparsity of the precision ma-

trix for the GMRF and use efficient Bayesian approximation inference for the parameters. As an

illustration, we describe the detailed INLA implementation proposed by Rue et al. (2009) for the

(3.6).

Let the vector of latent effect be xxx = (βββ, γ1,1, γ1,2, . . . , γ1,T , γ2,1, γ2,2, . . . , γ2,T , ααα1,1, . . . , αααS,T ) and

the vector of hyperparameters be θθθ = (ϕ1, ϕ2, ΣΣΣωωω, ΣΣΣααα). Within framework, this latent structure is

a GMRF of zero mean and precision matrix detemined by θθθ. Based upon the joint probability

density,

π(xxx, YYY , θθθ) ∝ π(θθθ)π(xxx|θθθ)

(cid:89)

π(Yi|xi, θθθ)

∝ π(θθθ)π(βββ)

i∈I

f (γγγt|γγγt−1, ϕω1, ϕω2, ΣΣΣωωω)

T
(cid:89)

t=1

S
(cid:89)

s=1

N (αααst; 000, ΣΣΣ)

2
(cid:89)

j=1

λYj,st
j,st e−λj,st
Yj,st!



 ,

(3.12)

where π(θθθ) is the prior density for the hypermeters θθθ, we use the default priors, Gaussian prior

for the internal transformed hyperparameter, log

(cid:17)

(cid:16) 1+ϕj
1−ϕj

, j = 1, 2. and Wishart priors for the

precision matrices, ΣΣΣ−1

ωωω , ΣΣΣ−1

ααα . π(βββ) is a Gaussian prior for the intercepts and coefficients βββ,

(cid:81)T

t=1 f (γγγt|γγγt−1, ϕ1, ϕ2, ΣΣΣωωω) is the Gaussian likelihood for the correlated temporal random effects

γj, j = 1, 2, and N (; ) is the bivariate Gaussian density.

53

---

<!-- PAGE 55 -->

The posterior marginal density for the hyperparameters θθθ can be obtained by the Laplace

approximation,

˜π(θθθ|YYY ) ∝

π(xxx, YYY , θθθ)
˜πG(xxx|θθθ, YYY ) xxx=xxx∗(θθθ),

(3.13)

where ˜πG(xxx|θθθ, YYY ) is the Laplace approximation of π(xxx|θθθ, YYY ), xxx∗(θθθ) is the mode of the conditional

posterior density π(xxx|θθθ, YYY ).

Next, using the approximation of π(θθθ|YYY ), the discrete integration can provide us with the

approximation of the posterior marginal densities of interest π(xi|YYY ),

˜π(xi|YYY ) =

(cid:88)

k

˜π(xi|θθθk, YYY )˜π(θθθk|YYY )∆k,

(3.14)

Where ˜π(xi|θθθk, Y ) is the marginal Gaussian density for the approximation of π(xi|θθθk, Y ) derived

from ˜πG(xxx|θθθ, YYY ), ∆k is the area weights in the discrete integration.

Since correlated bivariate AR process is not available in the current INLA package, we need to

derive the precision matrix from (cid:81)T

t=1 f (γγγt|γγγt−1, ϕ1, ϕ2, ΣΣΣωωω) is the Gaussian likelihood for the corre-

lated temporal random effects γj, j = 1, 2, and define this specific latent effect using inla.rgeneric()

function in INLA. For the bivariate AR(1) process according to (3.6),





γ1,t = ϕ1γ1,t−1 + ω1,t

γ2,t = ϕ2γ2,t−1 + ω2,t

, −1 < ϕ1, ϕ2 < 1, ωωωt =








ω1,t

ω2,t


 ∼ N (000, ΣΣΣωωω) ,

(3.15)

we have the analytical form of the Gaussian likelihood as,

f (γγγt|γγγt−1, ϕ1, ϕ2, ΣΣΣωωω) = f (γγγ1|ϕ1, ϕ2, ΣΣΣωωω)

T
(cid:89)

f (γγγt|γγγt−1, ϕ1, ϕ2, ΣΣΣωωω)

T
(cid:89)

t=1

t=2
(cid:32)

(cid:40)

=

(cid:112)(1 − ϕ2
ω1σ2

(cid:0)2π(cid:112)σ2
T
(cid:26)
(cid:89)

exp

−

·

−

1
2(1 − ρ2
ω)

1)(1 − ϕ2
2)
ω)(cid:1)T exp
ω2 (1 − ρ2
(cid:18) (γ1,t − ϕ1γ1,t−1)2
1
σ2
2(1 − ρ2
ω)
ω1

t=2

1)γ2
1,1

(1 − ϕ2
σ2
ω1

+

2)γ2
2,1

(1 − ϕ2
σ2
ω2

−

2ρωγ1,1γ2,1

(cid:112)1 − ϕ2
σω1σω2

1

(cid:112)1 − ϕ2

2

(cid:33)(cid:41)

+

(γ2,t − ϕ2γ2,t−1)2
σ2
ω2

−

2ρω(γ1,t − ϕ1γ1,t−1)(γ2,t − ϕ2γ2,t−1)
σω1σω2

(cid:19)(cid:27)
,

(3.16)

54

---

<!-- PAGE 56 -->

(3.16) can be treated as the Gaussian likelihood for the random vector,






















VVV =

γ1,1
σω1
γ2,1
σω2
γ1,1
σω1
γ2,1
σω2

2

1

(cid:112)1 − ϕ2
(cid:112)1 − ϕ2
γ1,2
σω1
γ2,2
σω2

− ϕ1

− ϕ2
...

γ1,T
σω1
γ2,T
σω2

− ϕ1

− ϕ2

γ1,T −1
σω1
γ2,T −1
σω2






















,

with its precision matrix,

ΛΛΛ =

1
1 − ρ2
ω






















1

−ρω

−ρω

0

0

0

0

1

0

0
...

0

0

0

0

1

0

0

−ρω

−ρω
...

0

0

1

0

0

. . .

. . .

. . .

. . .

0

0

0

0
...

1

0

0

0

0

−ρω

−ρω

1






















2T ×2T

(3.17)

(3.18)

To implement latent effect VVV with INLA, we also need to find the linear transformation between

VVV and its internal representation UUU ,

VVV = AUAUAU ,

(3.19)

55

---

<!-- PAGE 57 -->

where






















√

1−ϕ2
1
σω1
0

− ϕ1
σω1
0

0

0

AAA =

. . .

. . .

. . .

0

0

1
σω1
0

. . .
...
. . . − ϕ1
σω1
. . .

0


























γ1,1

γ1,2
...

γ1,T

γ2,1

γ2,2
...

γ2,T


























,

0

√

1−ϕ2
2
σω2
0

0

0

0

− ϕ1
σω2

1
σω2

UUU =

0

0

0

0

1
σω1
0

0

0

0

. . . − ϕ1
σω2

1
σω2

(3.20)

(3.21)






















2T ×2T

. . .

. . .

. . .

. . .
...

. . .

0

0

0

0

0

Using sparse matrix arithmetic in R, we can easily compute the covariance matrix of UUU through

matrix multiplication,

Cov(UUU ) = AAA−1Cov(VVV )(AAA−1)T ,

where Cov(VVV ) = ΛΛΛ−1. Then the complete implementation of bivariate AR(1) latent effect will be

done through the rgeneric() function in the R package, INLA. The choice of the prior distribution

can be customized via an appropriate reparameterization approach with its corresponding Jacobian

matrix. Bivariate random walk of order 1 can be done similarly except for the distributional

assumption on the initial γγγ1. The Gaussian likelihood part of RW(1) is exactly the same as the

AR(1)’s, with ϕ1 = ϕ2 = 1. Implementation of multivariate AR temporal effect with higher orders

in INLA is also feasible, as long as the precision matrix of the latent effect can be analytically

specified, meanwhile the dimension of its precision matrix will increase quickly as a product of the

latent vector dimension and the length of the time series, with an expected higher computational

cost. However, that is beyond the scope of this paper. In the next section, the performance of

56

---

<!-- PAGE 58 -->

parameter recovery, in-sample prediction, and computational cost are demonstrated through an

extensive simulation study before one can apply this method practically.

3.4 Numerical study

3.4.1 Simulation study: INLA v.s STAN

Bayesian hierarchical models focus on the inference of sampled parameters from their joint poste-

rior distribution. However, computational efficiency can be of great concern if accurate statistical

inference is needed shortly in real applications. In this section, we conduct a comparison simulation

study through a simplified framework from (3.6), where no additional covariates are involved in the

link function to the conditional Poisson means. The comparison aims at showing the competitive

performance of INLA regarding parameter recovery and in-sample prediction at a much lower com-

putational cost versus the traditional MCMC method. In addition, the results also will encourage

the practitioners to implement customized latent effects via rgeneric() function with a correctly

specified precision matrix for accurate parameter inference. We have 200 simulations for each com-

bination of different numbers of assets (S = 10, 15, 20) and time intervals (T = 50, 100, 150) in

three different scenarios. The parameter setup is summarized in Table 6.

Scenario

1
2
3

ϕ1

0.5
0.5
0.5

ϕ2

0.8
0.8
0.8

σ−2
ω1
6
6
6

σ−2
ω2
7
7
7

ρωωω

0.6
0.6
0.6

σ−2
α1
10
10
10

σ−2
α2
10
10
10

ρααα

0.6
0.2
-0.6

Table 6: Parameters for different Scenarios

Since the latent level correlation is of more interest to the practitioners for real application, we

explore the model inference performance by using different values of ρααα =0.6,0.2, and -0.6, which

displays the different strengths and directions of the correlation between the level-correlated effects.

As for the correlated temporal effect, we set a moderate correlation ρωωω = 0.6 to describe the overall

market behavior. Practitioners can always use one identical or two different uncorrelated temporal

effects to account for the extremely strong or weak temporal correlations via the default setting

in INLA, but the BVAR(1) framework provides more flexibility to implement a wider range of

latent temporal correlations. The AR coefficients are set to be ϕ1 = .5 and ϕ2 = .8 to indicate

57

---

<!-- PAGE 59 -->

a decent temporal dependence for each of the temporal effects. The precision parameters for the

latent effects are set to be relatively large so that their variances are all controlled under 1 to

avoid unreasonably extreme values generated in the simulation study. The conventional Bayesian

inference is implemented in STAN because of its high-quality chain provided by NUTS Hamiltonian

Monte Carlo (HMC) sampler, compared with JAGS or NIMBLE (Beraha et al., 2021), whose default

samplers are the Gibbs samplers and Metropolis-Hastings sampler. We set the posterior sample

size to be 1000 after 1000 burn-ins for the traditional MCMC method. The choice of the priors for

the parameters between INLA and STAN are identical,

log

(cid:19)

(cid:18) 1 + ϕi
1 − ϕi

∼ N (0, 2), i = 1, 2,

ΣωΣωΣω ∼ W2 (4, III 2×2) ,

ΣαΣαΣα ∼ W2 (4, III 2×2) ,

(3.22)

where III 2×2 is an identity matrix. Between our framework and the traditional MCMC method,

we will evaluate their performances including parameter recovery rate, Mean Square Error (MSE),

Mean Absolute Error (MAE), Weighted Mean Absolute Percentage Error (WMAPE), and com-

putational cost. The parameter recovery rate is defined as the frequency of the true parameter

being captured in the default 95% credible interval out of these 200 simulations. MSE, MAE, and

WMAPE measure the average in-sample deviation between true count Yj,st with predicted count
ˆYj,st.MSE, MAE, and WMAPE are calculated as,

MSE =

MAE =

1
n

1
n

n
(cid:88)

(ypred,i − yi)2,

i=1
n
(cid:88)

|ypred,i − yi|,

WMAPE =

i=1

(cid:80)n

i=1 |ypred,i − yi|
i=1 |yi|

(cid:80)n

(3.23)

.

The parameter recovery performances among different scenarios are summarized in Table 7 and

8. The parameter recovery rate reflects the credibility of the proposed framework in terms of the

statistical inference on the parameters of interest. Regarding the in-sample prediction accuracy

and computational cost, the comparison results are in Table 9.

58

---

<!-- PAGE 60 -->

Regarding the parameter recovery performance, our framework shows a competitive perfor-

mance. First of all, the latent correlation recovery rate is comparable to the STAN’s performance.

For the temporal correlation, both of these two methods have a recovery rate as high as over

90% for most scenarios. For the latent level correlation, the parameter recovery is better (around

95%) when the true value is near 0 (ρααα = 0.2) but is less satisfactory when ρααα is close to 1 (75%

to 90% in Scenario 1 and Scenario 3). Since the temporal effects have slightly larger variances

(σ−2

α1 = 6, σ−2

α2 = 7) than the level-correlated effects do (σ−2

ω1 = 10, σ−2

ω2 = 10) in the simulation

setup, a larger sample size, i.e., a larger value of T will enhance the recovery of level correlation.

Second, the recovery rates for the precision parameters for both latent effects are satisfactory re-

gardless of ρααα. The recovery rates of the AR coefficients are also okay with the INLA but we need

to point out that the recovery of ϕω2 is not as ideal as the MCMC approach when the latent level

correlation ρααα is negative. However, in real applications, a positive correlation between different

types of counts is more common as both transactions of different risk levels are usually driven by

the trading intensity of the corresponding asset in a positive manner. This scenario is just for the

illustration of an overall satisfactory parameter recovery performance of the INLA implementation

of the BVAR(1)-LCM framework. In addition, the temporal effects are explained as the overall

market behavior and the direct interpretation of AR coefficients in the latent state is of less inter-

est to the practitioners, as long as the AR coefficients have reasonable estimates and the overall

model adequacy and prediction are satisfactory. Despite a few exceptions, the INLA method, as an

approximate Bayesian inference tool, has a competitive parameter recovery performance in general

compared with the full Bayesian inference approach based on the joint posterior distribution.

We’ve also considered the in-sample performance and computational time between the INLA

method and the STAN method. In Table 9, There is no significant difference between the in-sample

deviations from the true count data under various measurements. With similar in-sample prediction

performance, the INLA method has superior computational efficiency over the STAN method. The

current MCMC sampling size is 2000 including the 1000 burn-in samples. The MCMC sampling

procedure can still take more than the ten-fold computational time consumed by the INLA method.

As the dimension of financial data increases, higher computational costs can be expected by the

STAN method. When dealing the financial data containing S = 20 assets with each count time

series with length T = 150, the STAN method takes on average over 2000 seconds to make inferences

59

---

<!-- PAGE 61 -->

based on 1000 posterior samples. As for the irregularity of the computational time of the INLA

method, the main reason could be caused by the randomness in the simulation study. In the internal

computing procedure, when the generated data deviates too much from the prior distribution, the

default initial value will impact the convergence speed of the model, and sometimes a problematic

initial value can definitely cause a re-initialization of the computing procedure thus leading to a

longer computational time. Even though the computational time is not proportionally related to

the data dimension for the INLA method, its computational cost reduction is already significant

enough that the STAN method is no match in this perspective.

In this simulation study, we compared the INLA method with the traditional MCMC method

for model implementation in three aspects: parameter recovery rate, in-sample prediction accuracy,

and computational efficiency. We have shown the INLA method provides satisfactory performance

in parameter recovery except for a few cases, with similar in-sample prediction accuracy, and much

lower computational cost. In real applications in the HFT market, practitioners need to model

financial data on a large scale and make reasonable decisions promptly, so the INLA method can

provide a better trade-off between computational efficiency and statistical inference accuracy. As

for the evaluation of out-of-sample prediction, we will conduct the study on real data across different

models for real applications. We will adopt the INLA method for model implementation due to

the size of the real financial data to save computational time.

3.4.2 Real application

Before we illustrate how to apply our model to the high-frequency financial market, we will first

give a brief background introduction to the financial market including how high-frequency trading

(HFT) firms make profits and some empirical patterns of financial data. Then, we are going to apply

our model framework to investigate the market dynamics of different stock sectors. Meanwhile, we

will also compare additional existing model candidates for model selection. Next, we will account

for the interrelation among the multiple stocks within the same sector, via correlated temporal

effect and level-correlated effect, including exogenous covariates of interest. Finally, we will provide

market behavior interpretations using our model and some perspectives on what benefits our model

can bring to practitioners.

60

---

<!-- PAGE 62 -->

Scenario

S

T

σ−2
ω1

ρωωω
INLA STAN INLA STAN INLA STAN INLA STAN INLA STAN

ϕω1

ϕω2

σ−2
ω2

10

1(ρααα = .6)

15

20

10

2(ρααα = .2)

15

20

10

3(ρααα = −.6)

15

20

50
100
150
50
100
150
50
100
150

50
100
150
50
100
150
50
100
150

50
100
150
50
100
150
50
100
150

0.78
0.89
0.89
0.85
0.89
0.91
0.8
0.87
0.92

0.84
0.9
0.94
0.86
0.86
0.91
0.81
0.9
0.9

0.83
0.88
0.92
0.83
0.9
0.94
0.81
0.88
0.9

0.93
0.96
0.96
0.95
0.94
0.96
0.94
0.94
0.96

0.96
0.92
0.96
0.96
0.95
0.94
0.96
0.96
0.95

0.97
0.94
0.94
0.95
0.94
0.96
0.94
0.94
0.96

0.8
0.92
0.89
0.76
0.87
0.9
0.82
0.89
0.9

0.83
0.86
0.95
0.77
0.88
0.89
0.86
0.9
0.9

0.84
0.88
0.9
0.84
0.92
0.86
0.79
0.88
0.88

0.93
0.95
0.92
0.93
0.94
0.94
0.92
0.94
0.92

0.96
0.92
0.96
0.94
0.94
0.92
0.97
0.92
0.93

0.94
0.9
0.92
0.92
0.94
0.92
0.94
0.97
0.93

0.92
0.94
0.98
0.94
0.95
0.95
0.94
0.95
0.96

0.9
0.96
0.92
0.92
0.94
0.91
0.94
0.96
0.94

0.85
0.91
0.88
0.88
0.95
0.92
0.94
0.92
0.92

0.91
0.92
0.95
0.93
0.93
0.94
0.92
0.92
0.94

0.86
0.94
0.92
0.9
0.94
0.92
0.9
0.93
0.92

0.86
0.88
0.85
0.84
0.93
0.91
0.92
0.9
0.9

0.82
0.94
0.94
0.86
0.94
0.92
0.84
0.96
0.92

0.83
0.94
0.94
0.8
0.94
0.94
0.88
0.92
0.92

0.85
0.94
0.94
0.88
0.92
0.9
0.84
0.92
0.94

0.94
0.94
0.96
0.96
0.96
0.95
0.95
0.98
0.93

0.95
0.94
0.96
0.94
0.98
0.94
0.94
0.96
0.94

0.97
0.95
0.94
0.93
0.96
0.94
0.98
0.97
0.95

0.88
0.86
0.9
0.78
0.89
0.92
0.82
0.89
0.89

0.84
0.84
0.88
0.82
0.86
0.86
0.84
0.84
0.77

0.9
0.88
0.86
0.85
0.82
0.78
0.76
0.69
0.62

0.98
0.94
0.96
0.95
0.94
0.95
0.98
0.95
0.96

0.92
0.94
0.95
0.96
0.96
0.94
0.94
0.96
0.92

0.97
0.95
0.96
0.95
0.94
0.94
0.96
0.94
0.92

Table 7: Parameter recovery rate comparison between INLA and STAN for correlated temporal
effects ω1 and ω2

61

---

<!-- PAGE 63 -->

Scenario

S

T

σ−2
α1

σ−2
α2
INLA STAN INLA STAN INLA STAN

ρααα

10

1(ρααα = .6)

15

20

10

2(ρααα = .2)

15

20

10

3(ρααα = −.6)

15

20

50
100
150
50
100
150
50
100
150

50
100
150
50
100
150
50
100
150

50
100
150
50
100
150
50
100
150

0.9
0.93
0.92
0.92
0.95
0.96
0.92
0.94
0.92

0.96
0.95
0.96
0.95
0.97
0.94
0.96
0.96
0.94

0.95
0.94
0.94
0.92
0.95
0.94
0.92
0.93
0.96

0.9
0.92
0.91
0.92
0.92
0.94
0.93
0.93
0.92

0.95
0.94
0.96
0.97
0.95
0.96
0.94
0.96
0.96

0.92
0.94
0.92
0.92
0.96
0.94
0.92
0.92
0.94

0.96
0.96
0.96
0.92
0.92
0.97
0.94
0.94
0.95

0.98
0.96
0.96
0.94
0.94
0.96
0.94
0.92
0.94

0.93
0.96
0.94
0.91
0.93
0.93
0.94
0.96
0.96

0.94
0.94
0.96
0.9
0.9
0.96
0.9
0.93
0.95

0.96
0.94
0.94
0.96
0.92
0.96
0.96
0.95
0.94

0.92
0.96
0.94
0.9
0.92
0.91
0.94
0.96
0.96

0.74
0.84
0.84
0.83
0.84
0.87
0.81
0.87
0.88

0.95
0.93
0.98
0.92
0.95
0.94
0.93
0.97
0.96

0.66
0.79
0.84
0.78
0.82
0.9
0.81
0.86
0.9

0.72
0.82
0.84
0.8
0.84
0.84
0.8
0.89
0.86

0.94
0.94
0.96
0.95
0.96
0.95
0.93
0.96
0.95

0.61
0.75
0.83
0.74
0.8
0.84
0.8
0.83
0.86

Table 8: Parameter recovery rate comparison between INLA and STAN for level-correlated effects
α1 and α2

62

---

<!-- PAGE 64 -->

Scenario

S

T

MAE

MSE

WMAPE

CPU.used

INLA STAN INLA STAN INLA STAN INLA

STAN

10

1(ρααα = .6)

15

20

10

2(ρααα = .2)

15

20

10

3(ρααα = −.6)

15

20

50
100
150
50
100
150
50
100
150

50
100
150
50
100
150
50
100
150

50
100
150
50
100
150
50
100
150

1.524
1.573
1.595
1.558
1.613
1.63
1.594
1.633
1.646

0.98
0.982
1.008
0.984
1.009
1.01
0.988
1.013
1.011

1.476
1.537
1.585
1.55
1.601
1.625
1.572
1.639
1.66

1.533
1.576
1.593
1.569
1.609
1.626
1.599
1.632
1.642

0.985
0.985
0.989
0.994
0.991
0.992
1.014
1.002
0.993

1.483
1.544
1.583
1.651
1.603
1.624
1.577
1.639
1.659

3.691
3.947
4.026
3.876
4.126
4.217
4.062
4.238
4.316

1.444
1.446
1.508
1.457
1.512
1.515
1.466
1.525
1.518

3.586
3.927
4.156
3.977
4.257
4.399
4.119
4.49
4.616

3.772
4.005
4.084
3.979
4.177
4.268
4.121
4.308
4.364

1.504
1.501
1.511
1.551
1.519
1.521
1.631
1.568
1.523

3.651
3.997
4.213
19.226
4.345
4.457
4.173
4.554
4.673

0.168
0.173
0.176
0.176
0.179
0.18
0.177
0.181
0.182

0.094
0.095
0.095
0.094
0.097
0.096
0.095
0.097
0.097

0.124
0.127
0.124
0.126
0.127
0.129
0.132
0.129
0.128

0.169
0.175
0.176
0.178
0.178
0.18
0.177
0.181
0.182

0.094
0.095
0.093
0.096
0.095
0.095
0.097
0.096
0.095

0.125
0.127
0.124
0.133
0.127
0.129
0.132
0.129
0.128

5.849
19.458
9.016
6.742
6.323
11.162
16.811
7.366
13.754

11.92
27.974
21.403
9.118
9.571
16.254
28.657
14.959
21.812

6.962
31.864
10.757
13.785
9.615
11.927
26.201
15.304
14.68

146.802
402.746
603.799
249.312
444.649
1147.675
358.517
676.496
1868.829

232.927
474.528
1407.225
260.872
488.026
1147.024
507.624
1093.478
2124.168

319.741
586.252
1454.869
1134.083
1662.712
2428.919
1399.757
2331.487
4687.846

Table 9: In-sample prediction and computational time comparison between INLA and STAN

63

---

<!-- PAGE 65 -->

3.4.2.1 High-frequency trading (HFT) background According to Carrion (2013) and

Dutta et al. (2022), one source of profit-making in HFT is related to intraday market time skills,

buying when prices are temporarily low and selling when prices are temporarily high. This is not

solely driven by very short-term signals or trading at fleeting prices, but by the existence of eco-

nomically significant predictability in intraday prices. HFTs execute their trades at better prices

than non-HFTs, have lower processing costs, and have some ability to avoid adverse selection costs

on larger trades when supplying liquidity. To cover these fixed processing costs, the HFT firms

earn very small profits per trade but place large volumes of orders, making profits based upon small

amounts of predictive power on large trading volumes.

From the empirical data analysis of the raw transaction-level data, the price fluctuation regard-

ing log price return within short time intervals only has a small range, and there are numerous

transactions made with zero returns. Therefore, the practitioners in the market need to acknowl-

edge that making a profit through a significantly high price return in HFT is not supported by

the intrinsic market dynamics, and they can strategically place orders according to the numbers of

transactions with zero return and non-zero return in a short term. For example, if the number of

non-zero returns is large, it implies the asset price is volatile and short-term profit can be expected

by supplying liquidity according to the price movement prediction with other models. Otherwise,

buy-in opportunities can be considered at the occurrence of an abundance of zero returns since the

price is temporarily stable.

In addition, HFT improves liquidity (Hendershott and Riordan, 2013), reduces volatility (Has-

brouck and Saar, 2013), and yields a different market microstructure than the conventional finan-

cial market without HFT (Ammar et al., 2020). There has been some research work conducted

to account for the association between volatility and liquidity in the conventional financial market

(Deuskar, 2006; Bedowska-S´ojka and Kliber, 2019). Although there is only a general confirmation

that liquidity and volatility are strongly associated, we can as well explore their relationship in the

HFT setting with count data. Since there are various types of measurements to quantify liquidity

and volatility, it is explicable that their relationship can take many forms. O’hara (1998) points

out that liquidity is generally defined as the ability to trade large volumes quickly at low cost, and

usually such trading doesn’t cause a drastic impact on price change. We can use the total number

of transactions within a fixed short time interval as a surrogate measurement of volatility for count

64

---

<!-- PAGE 66 -->

data because the trading volumes among these short intervals are generally large and don’t have a

significant difference, the total trading volume can be roughly regarded as a multiple of the number

of transactions. From this perspective, our method can account for this short-term association

between liquidity and volatility in a time-dependent manner.

3.4.2.2 High-frequency count data description The transaction-level data for our analysis

are retrieved from the Trade and Quote (TAQ) database from Wharton Research Data Services

(WRDS). The TAQ database contains intraday transactions (trades and quotes) data for all secu-

rities listed on the New York Stock Exchange (NYSE) and American Stock Exchange (AMEX), as

well as Nasdaq National Market System (NMS) and Small-Cap issues. Among all the HFT data,

we focus only on the trading data from three GICS sectors in January 2013, Healthcare, Energy,

and Industrials.

We first pre-process the raw HFT data. Let t = 1, . . . , T denote the order of the fixed time

intervals (e.g., 2-minute intervals in our study) within a trading day, let it = 1, . . . , Nt be the order

of the transactions within the time interval t due to the idiosyncrasy of high-frequency financial

data and the fact that the number of transactions in a given interval is random. Let Tit, Pit, and

Rit be the corresponding transaction time, price, and log returns at the itth transaction, with

Rit =

Pit − P(i−1)t
P(i−1)t

.

We construct two new variables, YH,t and YL,t, i.e., transaction count of high-risk level and count

of low-risk level respectively. For a user-defined threshold τ > 0, let the incidence and count of the

log return being greater than τ in the time interval t be

Bit =





1 if |Rit| > τ,

0 if |Rit| ≤ τ,





YH,t = (cid:80)Nt

it=1 Bit

YL,t = Nt − YH,t

then

(3.24)

(3.25)

Choice of τ : Due to limited literature resources on HFT data, the threshold selection for

65

---

<!-- PAGE 67 -->

defining high-risk level counts is data-driven or of practitioners’ interest. The larger the threshold

τ , the sparser the count of high-risk level will be, and dealing with inflated zeros will require specific

caution. In the following simple example of the stock ABT on 01/02/2013, in Table 10, τ = 0.0005,

or five basis points. The definition of extremeness can be determined by practitioners, for example,

Brogaard et al. (2018) defined the extreme price movement in HFT using 99.9% quantile of the

return distribution.Baron et al. (2019) selected 0.1% quantile of the distribution of response time

(time-stamp difference) to define Decision-Latency to capture the fastest reaction time. Due to

limited literature on the distribution of high-frequency price log returns, we are going to select

τ = 0 and categorize the transactions with non-zero log returns into the high-risk group and the

ones with zero log returns into the low-risk group. Such a choice of τ = 0 has a natural interpretation

of the price volatility and can prevent imbalanced count data with excessive zero counts on high-risk

levels if the threshold is not selected appropriately. Since the number of transactions with zero log

returns takes a significant proportion under the high-frequency circumstance, the real applications

in this paper will be based on τ = 0 for demonstration. However, customization of τ for different

assets is feasible as long as extra financial domain knowledge and the data empirical characteristics

justify the threshold specification.

i
1
2
3
4
5
...
652
653
654
655
656

Time (Ti)
9:30:00.531
9:30:03.167
9:30:08.307
9:30:08.311
9:30:08.313
...
9:31:58.736
9:31:58.886
9:31:59.287
9:31:59.611
9:31:59.909

Price (Pi) Log returns (Ri)
32.3300
32.3000
32.3500
32.3250
32.3525
...
32.2300
32.2300
32.2300
32.2200
32.2300

NaN
-0.000929
0.000463
0.000308
-0.000001
...
0.000310
0.000000
0.000000
-0.000310
0.000310

Table 10: An example of raw data for the stock ABT

Let YYY st = (YH,st, YL,st)′ be a 2-dimensional vector of count responses of high-risk transactions

and low-risk ones for the sth stock at equally spaced times t, for s = 1, . . . , S and t = 1, . . . , T

(T = 195). The data includes D = 21 trading days in January 2013. For each trading day, there

are 195 time intervals (2 minutes). Take the stock ABT on 01/02/2013 in the time window from

66

---

<!-- PAGE 68 -->

Stock Count

Type

Time Duration mean (in seconds)

logsize mean

ABT
ABT
ABT
ABT
ABT
ABT

413
306
269
244
218
234

High risk
High risk
High risk
Low risk
Low risk
Low risk

9:30
9:32
9:34
9:30
9:32
9:34

0.283
0.392
0.446
0.452
0.553
0.513

5.241
5.168
5.194
5.196
5.189
5.061

Table 11: Data structure for INLA modeling. count data for stock ABT between 9:30 and 9:34
a.m. on 01/02/2013.

9:30 to 9:34 for example as in Table 11:

In Table 11, the last two columns are the two covariates of our interest. Duration mean is

the average duration between two consecutive transactions of the same type. The i-th financial

duration, xi, within an interval is defined as,

xi = ti − ti−1,

where ti is the time point when the i-th financial event occurs.

In our study, financial events

are defined as transactions of different risk levels. Within a time interval, a large collection of

successive short durations usually reflect a high trading intensity in the market thus leading to a

large count of transactions. It would be useful to investigate and quantify the association between

count and average duration. In addition, a common delineation for the intra-day periodic trading

patterns is the phenomenon of high trading intensity (shorter durations) during the opening and

closing periods of a trading day and relatively lower trading activity around noon. In Figure 7, the

diurnal effect can be observed as a U-shape pattern in the intra-day count data and an upside-down

U-shape pattern in the average duration data. Therefore, including average duration as a covariate

in our model facilitates the accommodation for diurnal effect explanation. Another covariate of our

interest is related to trade size. Due to the wide range of trade sizes for the transactions, we choose

a logarithmic transformation on the trade size and calculate the average log trade size for the time

intervals. Since price changes fluctuate significantly when a large number of shares are traded, it

is also of our interest to account for this relationship between count and log trade size.

Similar stocks being in each sector, the co-movement of these time series is related to market

67

---

<!-- PAGE 69 -->

Figure 7: Diurnal pattern exhibited in observed counts and averaged duration in 2-min intervals
for stock ABT on 01/02/2023.

behavior evaluation for the corresponding industry, the multi-asset pattern is shown in Figure 8.

Before further investigation of the market micro-structure, we will implement different models on

the real data, and evaluate model adequacy and out-of-sample prediction in the next step.

3.4.2.3 Model adequacy and prediction accuracy comparisons

In addition to our pro-

posed framework, we include a list of other model candidates to be considered. To begin with, the

correlated bi-variate AR process with level correlation model (BVAR(1)-LCM) from (3.6) is one

of the candidates. However, due to the non-stationary feature of count data, it is not uncommon

to use a random walk (RW) process instead of an AR process to model the long memory tem-

poral dependence. Therefore, the correlated bi-variate RW process with a level correlation model

(BVRW(1)-LCM) with fewer parameters becomes another one of the model candidates. We also

consider AR and RW processes with uncorrelated latent temporal effect with ρωωω = 0 as a spe-

cial case. In addition, we include the last candidate, proposed by Ma et al. (2008), which can be

regarded as an existing method using only the level correlation model (LCM) using the MCMC

method, as a static LCM model without temporal latent effect γj,t in (3.6). As for the fixed ef-

fects, we incorporate different fixed effects for the conditional mean of the count at different risk

68

---

<!-- PAGE 70 -->

Figure 8: Count data for three GICS sectors: Energy, Health care, Industrials

levels. These model candidates will be compared from two aspects:

in-sample model adequacy

and out-of-sample prediction accuracy. To compare the in-sample model adequacy, we use the

Watanabe-Akaike Information Criterion (WAIC) (Watanabe, 2010; Gelman et al., 2014) and De-

viance Information Criterion (DIC). WAIC and DIC are predictive information criteria for Bayesian

models, smaller values indicate a better model. WAIC (Watanabe-Akaike information criterion) is

computed as,

WAIC = −2 log ppost(y) + 2pWAIC,

(3.26)

where pWAIC is the correction for the effective number of parameters to adjust for overfitting

69

---

<!-- PAGE 71 -->

and there are two approaches available for the correction.

pWAIC1 = 2

n
(cid:88)

(log(Epostp(yi|θ)) − Epost(log p(yi|θ))) ,

i=1
n
(cid:88)

varpost(log p(yi|θ)).

pWAIC2 =

i=1

DIC is computed as,

DIC = −2 log p(y|ˆθBayes) + 2pDIC,

(3.27)

(3.28)

where ˆθBayes is the posterior mean of the parameter and pDIC is the correction for the effective

number of parameters,

pDIC = 2(log p(y|ˆθBayes) − Epost(log p(y|θ))).

(3.29)

For out-of-sample prediction, we use the first 180 observations as a training set to predict

the last 15 observations, i.e., the count data in the last 30 minutes of a trading day. A smaller

value of MAE, MSE, and WMAPE regarding the prediction and actual count indicates a better

out-of-sample prediction performance.

There are three sectors of count data in our analysis, and each sector contains 21 days trading

days. The total number of data sets will be 3 × 21 = 63. Applying the described criteria above, we

select the best model under each measurement. Table 12 shows the model comparison results. The

percentage in the table is the proportion out of the 63 data sets that favor the specific measurement

regarding the model adequacy or out-of-sample performance accuracy. Around 80% of the data sets

favor the BVAR(1)-LCM or BVRW(1)-LCM model regarding model adequacy and more than 90%

regarding the out-of-sample prediction performance. Even though the other candidates perform

better either in terms of model adequacy or prediction accuracy, our proposed model, especially

the mode with correlated bivariate RW process with level-correlated (BVRW(1)-LCM) is favored

by the majority of the data sets in both aspects. Next, we are going to use the BVRW(1)-LCM

model to study the microstructure of the count data with long memory dependence.

70

---

<!-- PAGE 72 -->

Metric

BVAR(1)-LCM BVRW(1)-LCM AR(1)-LCM RW(1)-LCM Static LCM

WAIC
DIC
MAE
MSE
WMAPE

9.5%
19.0%
4.8%
4.8%
4.8%

69.8%
63.5%
88.8%
90.4%
88.8%

1.6%
1.6%
0.0%
0.0%
0.0%

19.1%
15.9%
4.8%
3.2%
4.8%

0.0%
0.0%
1.6%
1.6%
1.6%

Table 12: Percentage of the 63 data sets favoring each model regarding in-sample model adequacy
and out-of-sample prediction accuracy

3.4.2.4 An illustration of BVRW(1)-LCM framework From the previous result of the

model comparison, we will analyze the count data using the following model,

Yj,st|λj,st

ind∼ P ois(λj,st),

ηj,st = log λj,st = β0,j + βdur,jdurj,st + βsize,jsizej,st + γj,t + αj,st,

γj,t = ϕjγj,t−1 + ωj,t,








ω1,t

ω2,t


 ∼ N (000, ΣΣΣωωω) ,

(3.30)

ωωωt =



ΣΣΣωωω =







 ,

σ2
ω1

σω1σω2

σω1σω2


σ2
ω2



αααst =




α1,st

α2,st


 ∼ N (000, ΣΣΣααα) ,

where durj,st is the averaged durations between the transactions associated with risk levels of

the j-th type for the s-th asset in the t-th time interval, and sizej,st is the averaged logarithmic

trading size (number of traded shares) in transactions associated with risk levels of the j-th type

for the s-th asset in the t-th time interval. We apply the priors in (3.22) for the hyperparameters

and weakly informative normal priors for the fixed effects. The statistical inference is summarized

in terms of fixed effects and hyperparameters. We’ve also investigated the conditional posterior

correlation between the count data by integrating the inference on the fixed effects and random

effects. Finally, we provide some remarks for our model application.

Fixed effects of averaged durations and logarithmic trading size The fixed effects from

71

---

<!-- PAGE 73 -->

the averaged durations can provide some insights for the practitioners from four aspects in Figure

9. Firstly, We’ve found that averaged durations and different count data are negatively correlated

because their coefficients are estimated to be below zero. The overall negative association reflects

how the trading intensity influences the number of transactions. When the averaged durations are

observed to be short, it means transactions are made frequently in the market, causing larger counts

of transactions at different risk levels. Secondly, the averaged durations have a stronger impact

on the high-risk counts across all sectors except for the Energy sector on Monday because the

magnitude of the estimated coefficients for the high-risk counts is larger than the one for the low-

risk counts. Since the low-risk counts tend to be driven by the liquidity feature of the corresponding

asset, it is less impacted by the averaged durations. Therefore, the increased trading intensity will

provide more high-risk counts than low-risk counts, and practitioners can be aware of the short-

term proportion of transactions at both levels and evaluate the volatility of the market. Thirdly,

the Energy and Healthcare sectors with a larger magnitude of the fixed effect are more sensitive

to trading intensity than the Industrials sector with respect to the counts. The Healthcare sector

has more consistent sensitivity to the averaged durations because the estimated fixed effect has a

narrower range, while the counts from the other two sectors can react to the averaged durations

to different degrees throughout the month. Such differences in price fluctuation related to trading

intensity help practitioners design their option trading strategies for different sectors because option

pricing depends heavily on how drastically the asset price fluctuates. Fourthly, in terms of the Day

of Week effect, the counts tend to be impacted more from Tuesday to Thursday with a larger

magnitude of the fixed effect from averaged duration, than Monday and Friday.

In addition to averaged durations, we will also describe and explain the impact of the averaged

log trading size on the counts with several aspects in Figure 10. To start with, a higher averaged

trading size is associated with a higher number of counts, since the fixed effects are significantly

larger than zero. The average trading size is the average number of traded shares per transaction

which is positively associated with the trading volume, which is the product of the number of

transactions and their corresponding trading size. Hence, such a relationship infers that the asset

with a higher trading volume tends to have a larger count of transactions. Secondly, we’ve also

noticed that the averaged trading size within a time interval has a greater impact on the low-risk

counts, which means orders put to trade more shares don’t necessarily correlate with the high-risk

72

---

<!-- PAGE 74 -->

counts as strongly as with the low-risk counts. It can be related to the behavior of the market

makers, quoting both a buy and sell price of the asset in the inventory, with the purpose of making

a profit on a tiny margin of bid-ask spread via a high trading volume. Nevertheless, the positive

impact of trading size on the high-risk counts still aligns with the common sense that the price

change tends to be affected to a certain degree by the trading volume. Thirdly, among the three

sectors, the counts in the Industrials sector are more sensitive to the trading volume and such

sensitivity is more consistent over the month than the other two sectors. Practitioners can expect

more volatile behavior in the Industrial sector than in the other two sectors. Lastly, there is no

clear pattern regarding the Day of Week effect but we’ve seen that the high-risk counts on Fridays

are impacted more by the trading volume on Fridays, especially in the Healthcare sector and the

Industrials sector.

Since the fixed effects are directly related to the conditional mean of count data, such influences

on the count data can be quantified by its coefficients. Holding other effects unchanged in the t-th

time interval for the s-th asset, the difference of the βdur,1 and βdur,2 provides the estimation of

ratios of conditional means of different types of count as exp(βdur,1dur1,st −βdur,2dur2,st). The fixed

effect of the averaged log trading size can be applied in this manner as well. With a better under-

standing of the ratio between different counts within a given interval, practitioners may evaluate

their probability of making a profit regarding the dynamic volatility and customize their trading

strategy in different time intervals. As for the prediction on the count data with averaged dura-

tions and log trading sizes, one can either use lagged observations in the past with the stationarity

assumption or use non-negative time series models, such as log ACD models, to make predictions

on future observations in the upcoming time intervals.

Hyperparameters: latent correlation and variance Since the hyperparameters describe

the latent patterns of the random effect, they don’t contribute to the direct estimation of the

conditional mean of the count but they explain the uncertainty and association of the conditional

mean functions. The hyperparameters we are going to study are the correlation between the latent

temporal effects, ρωωω, and the correlation between the level random effects, ρααα, as well as the precision

parameters for the random effects.

According to our model results, the latent temporal effects are highly correlated in this month.

In Figure 11, the correlation coefficients present a strong relationship (ˆρωωω >.75) between the latent

73

---

<!-- PAGE 75 -->

Figure 9: The association between averaged durations and counts

Figure 10: The association between averaged log trading size and counts

temporal effects for counts with different types. In the Energy sector, the correlations could be

estimated at over .9 on some days such as 01/04/2013 (Day 3). A higher correlation ρωωω indicates that

the count data share some similarities regarding the market behavior. Therefore, the assumption

74

---

<!-- PAGE 76 -->

of uncorrelated latent temporal effects between count data can cause biased model inference and

introduce more uncertainty to model prediction at the significant existence of such correlation.

Figure 11: The estimated ρωωω with their 95% credible interval across all three sectors in January
2013

The variances of the latent temporal effects have small estimated values in Figure 12. There are

two possible reasons for the small variance estimation. First, due to the long memory property of an

RW process, the cumulative variance of the marginal temporal effects throughout a trading day is

increasingly significant as V ar(γi,t) = t2σ2

ωi is dependent on the time index t. A large estimation of

the variance is more likely to cause an inconsistent spread for the true time series. The second reason

can be associated with the covariates included in the model. We have shown that the averaged

durations and log trading size have significant fixed effects on the count data and a large proportion

of data variability can be accounted for by the covariates, leaving less variation to be captured by

the latent temporal effects. Even though the covariates are treated as the attributes for a specific

type of count for a given asset in a time interval, the existent temporal dependence among the

covariates also contributes to the overall temporal pattern, especially for the averaged durations.

Between the two types of counts, the low-risk counts have more uncertain latent temporal effects

than the ones at high-risk levels. Holding the covariates and the level-correlated random effect

unchanged, the change in the ratios of the conditional mean of the counts at t-th interval can be

75

---

<!-- PAGE 77 -->

determined by exp(γ1,t − γ2,t) with V ar(γ1,t − γ2,t) = t2(σ2

ω1 + σ2

ω2 − ρωωωσω1σω2). Even with the

small estimation of variance on the temporal effects across all three sectors, the market behaviors

for the Healthcare and Industrials are more stable than the Energy sector as the temporal effects

vary less on the high-risk counts than on the low-risk counts, which implies the big pharmaceutical

companies in the Healthcare sector and giant conglomerate corporations in the Industrials sector

are less volatile in a sense of the common environment in January 2013. On the other hand, the

Energy sector is considered more volatile regarding its market behavior, which could be related to

the oscillation in the crude oil price.

Figure 12: The dot plot of estimated variances, σ2
different days of a week across all three sectors in January 2013

ω1 and σ2

ω2, of the latent temporal effects on

The number of covariates plays an important role in capturing the association between the

response and explanatory variables. However, a small number of covariates are likely to explain a

limited amount of data variation while a large number of covariates tend to cause an overfitting issue.

Therefore, practitioners can select a moderate number of covariates of interest to be included in the

model, and incorporate level-correlated random effect for the correlated count data to supplement

the interpretation of the additional data variation that is not explained by the fixed effects. Such

random effects can be regarded to come from unobservable financial factors or covariates that

practitioners haven’t taken into account. In Figure 13, the correlations between latent level effects

76

---

<!-- PAGE 78 -->

remain at a high level throughout the entire month and such strong association helps account for

the correlation among the two different types of counts as well. The variance estimation for the level

effects is shown in Figure 14. Similar to the pattern for the temporal effect, the latent level effects

on the low-risk counts have a larger variance, leading to higher variability in the corresponding

counts. Even though the market behavior mentioned above describes the Industrials sector as

stabler than the Energy sector, a higher variance of the high-risk latent level effects indicates more

volatility in the Industrials sector than in the Energy sector, which means the unobservable factors

such as financial news and regulatory policies are idiosyncratic in different sectors. In Figure 15,

the variances in the raw counts are shown to be in a similar range in all three sectors, which means

that the variance comparison on the observational level does not provide distinctive guidance on

the customized investing strategy for different sectors. Using our framework, practitioners will

be able to uncover more latent patterns among different sectors even though the inference on the

observational level doesn’t differ significantly.

Figure 13: The estimated ρααα with their 95% credible interval across all three sectors in January
2013

Correlation between observed counts Based on the inference of the fixed effects and

random effects, we are also able to find the conditional relationship between the two types of

counts. According to (3.11), the conditional posterior correlation between the two counts can be

77

---

<!-- PAGE 79 -->

Figure 14: The dot plot of estimated variances of the latent level effects on different days of week
across all three sectors in January 2013

Figure 15: The variances of the observed counts on different days of week across all three sectors
in January 2013

calculated given the conditional posterior marginal mean and variance of each type of count. The

derivation of the correlation between the two count variables can be found in the Appendix section.

78

---

<!-- PAGE 80 -->

It is not appropriate to build a linear regression model between two count variables, especially when

the observed counts are not large enough. However, it is not uncommon to observe a large number

of transactions within a short time interval thus leading to a large number of counts at different

risk levels, and the Poisson distributions with a large mean can be still approximated by normal

distributions. If we use simple linear regression to describe the relationship between YH,st (counts

with non-zero log returns) and YL,st ((counts with zero log returns)), we can build a linear model

on the raw counts,

ˆYH,st = ˆb0,s + ˆb1,sYL,st.

For each individual asset, the R-squared value can be calculated as,





R2

s =

(cid:80)(YH,st − ¯YH,s)(YL,st − ¯YL,s)
((cid:80)(YH,st − ¯YH,s)2)((cid:80)(YL,st − ¯YL,s)2)

(cid:113)



2



,

(3.31)

(3.32)

where ¯YH,s and ¯YL,s are the sample mean of the counts for asset s. In a simple linear regression

model, the R-squared value stands for the proportion of the variation in the response variable

explained by the regressor, and it is equivalent to the squared correlation coefficient. A high

R-squared value is associated with a higher correlation coefficient.

Based on the inference of the fixed effects and random effects, we are also able to find the model-

based conditional relationship. In Figure 16, the conditional correlation between counts derived

by the latent effects varies throughout a trading day compared with the unconditional correlation

between the counts. The unconditional correlations are directly computed based on the count

data on the observational level as empirical correlations, and they are universally higher than the

conditional posterior correlation computed from our model (BVRW(1)-LCM) in the Energy sector.

The solid lines and curves stand for the aggregated mean of the estimated unconditional/conditional

correlation over one month while the bands stand for a margin with ±2 standard errors for the

estimated correlations. Similar patterns are also displayed in the Healthcare and Industrials sectors,

see Figures 31 and 32 in the Appendix section.

We can also compare the RMSE between the SLR prediction (3.31) and BVRW(1)-LCM-based

conditional regression,

H,st = b∗
Y ∗

0,st + b∗

1,stYL,st,

(3.33)

79

---

<!-- PAGE 81 -->

Figure 16: The trace plot of daily aggregated model-based and empirical correlations in the Health-
care sector throughout January 2023

where b∗

1,st and b∗

0,st are approximated by,

b∗
1,st = Corr(YH,st, YL,st|Data)

sd(YH,st|Data)
sd(YL,st|Data)

,

0,st = E(YH,st|Data) − b∗
b∗

1,st · E(YL,st|Data).

(3.34)

In the Energy sector shown in Figure 17, the RMSE based on the approximated conditional regres-

sion based on BVRW(1)-LCM is significantly lower than the RMSE of the SLR model. Therefore,

imposing a constant correlation between the count data can be a strong assumption for real appli-

cations. BVRW(1)-LCM-based regression also has a better performance in the other two sectors,

see Figures 33 and 34 in the Appendix section.

Across all sectors, the two types of counts have a stronger correlation at the opening and clos-

ing hours on a trading day and are less correlated in the middle of the day. Some assets such

as APC, DVN in the Energy sector, MDT, BAX, and BIIB in the Healthcare sector, and FDX,

UNP, and RTN in the industrials sector, their middle-day correlation estimation remains stable

throughout the month because the standard errors are smaller compared with other time points

and other assets. Such correlation estimation with reduced uncertainty can be useful for the prac-

80

---

<!-- PAGE 82 -->

Figure 17: Box plots for the square root of MSE comparison in the Energy sector between
BVRW(1)-LCM and Simple Linear Regression in January 2023

titioners to specifically adjust their investment scheme for these stocks in these time intervals. For

example, when the correlation between these two counts is estimated to be high, the ratio of the

estimated counts will be more reliable for the corresponding time interval thus the practitioners

can evaluate whether or not the underlying asset price is actively fluctuating instead of staying

steady with a large proportion of zero log returns. As a measurement for the association between

count data, correlation describes the linear relationship between two variables and has a satisfac-

tory performance when the count data are large but it is sensitive to outliers or non-linearity and

has a poor performance when the counts are small or even close to zero. The unconditional corre-

lations obtained from the raw count are also overestimated and unrealistic for practice. Therefore,

we’ve also investigated Spearman’s rank correlation between the two types of counts to measure

the monotonic association between the count data. In Figure 18, the empirical Spearman’s rank

correlations on the observational level are aggregated means based on different stocks within the

same sector. Although it indicates that the two types of counts have a fairly strong monotone rela-

tionship (correlation around .75), practitioners won’t be able to make additional inferences barely

with Spearman’s rank correlation. Nonetheless, the estimated latent level correlation ρααα from the

BVRW(1)-LCM model can account for the correlation on the observational level as a hidden factor.

81

---

<!-- PAGE 83 -->

Figure 18: The comparison between Spearman’s rank correlation and the latent level correlation
across three sectors.

Although it is meaningless to compare the magnitude between Spearman’s rank correlation and the

latent level correlation as two different correlation measurements, their trajectories are observed

to share some similarity and it will be more convincing to use the BVRW(1)-LCM model to make

inference and prediction when the pattern of correlation between the counts is preserved.

Remarks Since liquidity reflects the ability of an asset to be traded frequently without a

significant price change, the counts of transactions at a low-risk level (the magnitude of log return

less than τ ) can describe this property in a short-term manner. While volatility delineates how

drastically the price of an asset fluctuates given a time interval, the counts of transactions at a

high-risk level (the magnitude of log return greater than τ ) displays the frequencies of trades with

extreme price changes for which such extremity is pre-defined by the practitioners. In our study, we

can observe positive correlations between these two types of counts as all conditional correlations are

greater than zero with τ = 0, which implies a positive association between liquidity and volatility

in such a setting. However, the choice of τ = 0 is just for the illustration of our model framework,

and the definitions for the different types of counts can be customized by practitioners with their

interests. The number of types depends on the number of thresholds and each individual asset can

also be assigned separate thresholds as well because the price change patterns of different assets

82

---

<!-- PAGE 84 -->

can differ a lot from each other and a common threshold applied to define the counts can cause

data imbalance issues with excessive zeros for some assets so that the unified conditional Poisson

model framework needs to be adapted by some potential zero-inflated models.

In practice, the

prediction of the count data at different risk levels is not directly related to a profit-making trading

algorithm as the model focuses more on the variability of the price fluctuation in a discrete manner,

but the instant ratio between different counts within a short term provides statistical evidence on

the volatility of the market. For investors in the HFT market, such information facilitates their

decision on the strategies of trade and hold within a short period. A detailed trading algorithm

can be a combination of other price-movement prediction models and our framework, but this is

beyond the scope of this dissertation.

3.5 Summary

In this chapter, We proposed a Bayesian Poisson lognormal hierarchical model for multivariate

count time series in the paper. The incorporation of latent temporal effects and level random effects

helps to account for different sources of variation as well as the correlation among the counts. The

model inference is achieved by the approximated Bayesian inference approach, INLA, of which the

performances of model parameter recovery and computation cost are shown to be competitive with

the traditional MCMC method in the simulation study. Although our model framework targets

bivariate count data in this paper, it is feasible to extend our framework to count data with a

higher dimension by correctly specifying the precision matrix of high dimensional latent temporal

effects. Since such precision matrices are usually sparse, their inverse computation can enjoy an

efficient algorithm via sparse representation. Due to its computational efficiency, the scalability of

the model inference can also be achieved through parallel computing, which can save much more

computational time than a fully Bayesian approach. In real applications, we use our framework

to account for the microstructure of the HFT data, including the interpretation of the covariates,

hyperparameters of latent effects, and conditional correlation between count data with the latent

inference, which are not straightforward based on the counts on the observational level. Finally,

We also provide our opinions on the potential usage of the framework in the real financial market.

83

---

<!-- PAGE 85 -->

4 Sequential Bayesian spatio-temporal outbreak detection

The first two topics discussed in Chapters 2 and 3 are related to statistical research problems from

the high-frequency financial market. Online structural break detection via a CUSUM-like quasi-

score detector statistic in financial durations helps monitor the trading intensity in the market

and multivariate count time series modeling establishes a connection between observed counts via

latent interdependent random effect. Motivated by relevant techniques from uni-variate online

change point detection and efficient multivariate count data modeling, we are going to extend

the online change point detection framework to the multivariate level. For Chapter 4, we aim at

developing online outbreak detection framework for public health surveillance data with spatio-

temporal interdependence.

4.1 Background

Public health plays an important role in protecting and improving the health of individuals and

communities. One of the public health functions is disease prevention and control. Through vac-

cination programs, disease surveillance, and infection control measures, public health efforts can

help control and prevent the spread of infectious diseases, such as the flu and COVID-19. Public

health authorities use surveillance systems to monitor and track the occurrence of diseases, health

conditions, and other health-related events in a population. Surveillance systems provide statis-

tical insights into the trends, patterns, and risk factors for disease, as well as the evaluation of

the effectiveness of public health interventions. For infectious diseases, early outbreak detection

allows public health officials to take timely action to prevent the spread of the disease. A practical

implementation of surveillance is the disease dashboard such as the one for COVID-19. Provid-

ing real-time tracking of the pandemic, such dashboards inform early warning of outbreaks with

improved transparency and communication. Despite the concern about data quality and accuracy

due to data collection or reporting processes, dashboards still give people access to a wealth of

data. As long as practitioners handle such surveillance data with careful interpretation and bias

adjustment, a dashboard can be a valuable resource, to facilitate public health decision-making on

a disease outbreak from one of the various aspects. Tsui et al. (2008) gave a comprehensive review

of different types of surveillance systems and Li et al. (2022a) summarized modern challenges and

84

---

<!-- PAGE 86 -->

opportunities in public health data surveillance and forecasting. The motivation of this chapter is

to deliver an accurate early outbreak detection framework to monitor the occurrence of infectious

disease outbreaks based on the multivariate discrete dashboard data for an ongoing pandemic and

contribute to the collaboration with researchers in many different fields including epidemiology,

computer science, and public health.

4.2 Literature review

4.2.1 Change point detection in public health surveillance system

The early outbreak detection problem in surveillance systems can be regarded as the research topic

of online change point detection, also known as sequential or quickest change point detection because

an outbreak of an infectious data can be represented as a data pattern change, such as the changes

of trend, mean level, and variation. The main goal of online change point detection is to detect

the change from sequential data in real-time as soon as possible. Online change point detection

procedure deals with sequential data or streaming data and detects any change point shortly after

its occurrence and stops at the detection while the offline procedure has access to the full data and

aims at identifying and localizing the changes in data sequence in a retrospective manner. Although

online change detection procedure is better aligned with the need for early outbreak detection in

surveillance systems, statistical methodologies from both research lines provide an abundance of

inspiration for our paper.

All the methods are usually designed based on the average detection delay, probability of false

alarm, false alarm rate, and etc. Existing sequential change point detection methods can be di-

vided into two categories, such as Bayesian in which the distribution of the change-point time

is known and non-Bayesian (minimax) methods in which the change-point time is non-random

and unknown. Johnson et al. (2017) provided a review of optimal change-point detection theory

in both Bayesian and non-Bayesian settings recently. Regression methods of outbreak detection

have been widely used, both for detecting outbreaks in surveillance systems based on laboratory

reports and notified infections, and for syndromic surveillance. Farrington et al. (1996) described

the detection of outbreaks to boost other more intensive surveillance methods by routinely scanned

data using linear regression model but its weakness was insensitivity when the baseline values on

85

---

<!-- PAGE 87 -->

which the threshold calculation is based coincide with past outbreaks. Some methodological is-

sues involved in outbreak detection using examples from different statistical techniques which are

focused on infectious diseases such as monitoring birth defects were described by Farrington and

Andrews (2003) while Diggle et al. (2009) illustrated how spatial statistical methods can be used

on developing online surveillance systems for common diseases by the nature of the data. A sys-

tematic and comprehensive review of the advancement of aberration detection algorithms used in

public health surveillance for the last decade was given by Yuan et al. (2019). Beside the classi-

cal stochastic process control methods and regression-based methods, modern surveillance system

evolves to adopt more sophisticated monitoring regimens via such as Bayesian hierarchical models

and machine learning frameworks as solutions to handle the increased complexity and volume of

surveillance data. Another important line of related research, offline detection, handles the change

point detection as well, but in a completely different fashion. What differentiates the online and

offline change point detection problems most is type of data availability, sequential update versus

complete retrospection.

4.2.2 Traditional outbreak detection methods

Traditional outbreak detection methods include stochastic process control (SPC)-related approaches

and regression-based models. Early statistical applications in public health surveillance systems

were based on the analysis of the reported data from clinicians or laboratories. Therefore, statistical

methods stemming from stochastic process control in industrial manufacturing gained their popu-

larity. Traditional control charts are common tools for change point detection problems. Shewhart

control chart (Shewhart, 1929) as one of the earliest change point detection tools, uses previous

data to calculate a threshold based upon normality assumption (Montgomery, 2020). Due to its

easy-to-compute-and-interpret feature, Early Aberration Reporting System (EARS) software in

Centers for Disease Control (CDC) of the United States employed Shewhart control chart as one

of the surveillance tools to conduct near real-time monitoring. Instead of possessing congruence

and stationarity as the production data from a stable manufacturing process, surveillance data

can exhibit strong time trends, cyclic patterns, and other time-dependent effects, depending on the

data aggregation, population behaviors as well as other environmental factors. To take into account

these factors for valid applications, Shewhart control chart was adjusted to accommodate the mean

86

---

<!-- PAGE 88 -->

and standard deviation with a short sliding window of historical data, such as C and W algorithms,

which capture the recent data pattern by consecutive days. However, Shewhart control chart and

its extensions can have compromised performance because of inappropriate data preprocessing and

violation of methodological assumptions. For example, the normality assumption is a strong one

for surveillance time series especially the observations are small count data. Although Shore (2000)

implemented an inverse normal transformation approach to handle non-Gaussian data, such ap-

proach may suffer from different application where larger data sets are required for a more accurate

estimation for higher-order moment.

As another well-adopted SPC method for detecting change-points, CUSUM chart introduced

by Page (1954) is able to detect small shift from mean for industrial quality control data more

quickly than Shewhart chart. The idea of using cumulative information for detection is further

extended or modified to solve various research problems. When dealing with discrete surveillance

data, such as count data of health events, Rossi et al. (1999) proposed a approximation CUSUM

procedure for a Poisson process for practicality and convenience, of which the main idea is to

transform a Poisson variate through standardization and get an approximated Gaussian variate.

When surveillance data are in the form of correlated count data, He et al. (2014) discussed the

implementation of Multivariate Poisson CUSUM chart, and provided the control chart design based

on log-likelihood ratios with in-control parameters for baseline and design parameters for the shift.

As the common limitation, the SPC and SPC-related methods are more related to industry quality

control, where a in-control process can be defined in full detail and usually don’t need additional

covariate information to enhance accountability. The stationary assumption of public health data

may not be valid, and integration of various data sources facilitates a better understanding of the

baseline process and a better performance of early outbreak detection. Nevertheless, SPC methods

can be synthesized into regression-based methods to monitor the pattern of model residuals, scores,

or quasi-scores (Berkes et al., 2004).

Regression-based methods enable the incorporation of external covariates and explain temporal

dependence from past observations. Generalized linear models (GLMs) with distribution-specific

links to the mean function grant the versatility to handle a variety of surveillance data. Apart

from the well-known linear regression with independent Gaussian residuals for continuous data,

count data can also be modeled by GLM with corresponding link functions to various discrete

87

---

<!-- PAGE 89 -->

distributions such as Poisson, negative binomial as well as their zero-inflated variants etc. The

incorporation of additional factors of interest into GLMs enhances model forecast performance as

well as interpretability. Temporal dynamics such as day of week effect or seasonality are usually

elucidated via a dummy variable specifying different kinds of days or trigonometric term resem-

bling the sinusoidal data pattern (Serfling, 1963). Farrington et al. (1996) developed a regression

algorithm to assist outbreak detection by using the threshold predicted from the modeled baseline.

Adaptive GLM frameworks with a short sliding window of historical data address the limitations

of assuming static model parameters via sequential updating parameter estimates according to a

sliding baseline pattern (Burkom et al., 2007; Xing et al., 2011).

Auto-regressive integrated moving average (ARIMA) models (Box et al., 2015) and integer-

valued auto-regressive (INAR) models (Alzaid and Al-Osh, 1988), as special regression-based meth-

ods, account for the time dependence through a combination of past observations. For continuous-

valued time series, the time-dependence is illustrated by a ARIMA(p,d,q) model,

(cid:32)

1 −

p
(cid:88)

i=1

(cid:33)



ϕiBi

(1−B)d(Yt − µY ) =

1 +



θjBi

 ϵt,

q
(cid:88)

j=1

ϵt ∼ N (0, σ2

ϵ ),

where Yt and µY are the observation at time t and its expectation, and ϕi, θi, and σ2

ϵ are respectively

the auto-regressive (AR) coefficients, moving average (MA) coefficients, and the variance of the

white noise ϵt. B is a backshift operator, i.e., BiYt = Yt−i. p and q denotes the AR and MA orders,

indicating the number of lagged historical observations included in the model, while d is the order

of differencing to stabilize non-stationary time series. For integer-valued time series, the temporal

association between counts can be modeled via INAR(p) model with a binomial thinning technique,

Yt =

p
(cid:88)

i=1

αi ◦ Yt−i + ϵt,

where the binomial thinning operator αi ◦ Yt−i = (cid:80)Yt−i

k=1 Bk, Bk

i.i.d∼ Bernoulli(αi). ϵt is an in-

dependent non-negative integer-valued random error. Besides the flexibility of using seasonally

lagged observations and exogenous variable to explain the seasonality and external impact, the

88

---

<!-- PAGE 90 -->

auto-regressive framework alleviates the reliance on independent assumption and appreciates the

accountability pertaining to the unobserved and latent factors contained in historical data.

In

addition, smoothing methods orginated from the moving average (MA) methods with exponential

weights such as Exponential Weighted Moving Average (EWMA) and Holt-Winters method (Win-

ters, 1960). Such smoothing methods are commonly as part of data preprocessing to smooth out

seasonal effect and trend by applying other methods.

However, the aforementioned methods have different limitations. For example, SPC-related

methods rely on normality and stationary assumptions for their valid implementation. When

surveillance data are discrete, a common choice of model fitting is still the standard Poisson model,

even though it has been suggested in numerous literature that the data overdispersion issue can be

remedied by imposing a gamma prior on the Poisson mean or using a negative binomial model.

4.2.3 Modern outbreak detection methods

Over the last decade, statistical surveillance algorithms for online outbreak detection have a sub-

stantial evolution with the complexity of surveillance data and the advancement of computational

technology. To expedite early outbreak detection, public health authorities have already begun

to take advantage of pre-diagnostic or syndromic data such as patient counts with disease-related

symptoms recorded by hospitals or healthcare-related search information via electronic online plat-

forms. The expanding volume and variety of such data sources place both more valuable pre-

pandemic information and more challenging problems for efficient statistical models than traditional

laboratory diagnostics. Therefore, a burgeoning research line of Bayesian models in public health

surveillance offers several advantages over traditional methods including historical information bor-

rowing, domain knowledge a priori incorporation, computational solution to complex hierarchical

models, and natural interpretations of posterior probability for outbreak detection.

Bayesian Hidden Markov Models (HMM) enable practitioners to classify the surveillance data

into a non-epidemic phase and an epidemic phase via a binary latent state variable Z (Mart´ınez-

Beneito et al., 2008; Watkins et al., 2009; Conesa et al., 2015) and a suspiciously anomalous obser-

vation with a large value of P r(Z = 1) can trigger further investigation before finalizing a public

outbreak announcement. Since it is common to observe spatio-temporal patterns in surveillance

areal-type data, a common approach to introduce temporal dependence in the model is via an

89

---

<!-- PAGE 91 -->

ARMA association among latent temporal effects. Meanwhile, to account for the spatial correla-

tion, data from neighboring locations are assumed to behave similarly. Such spatial patterns can

be explained through the incorporation of latent spatial effects from different locations. It would

become natural for practitioners to account for the spatial association of the areal unit data. Con-

ditional auto-regressive model (Besag, 1974) is a prevalent choice as a prior distribution for random

spatial effect. Besag et al. (1991), Gelfand and Vounatsou (2003) and Jin et al. (2005) have addi-

tional discussions on the extension of CAR model, including the discussion of the special case of the

CAR model, Instrinc Auto-regressive (IAR) model with an extra constraint on the random effects,

efficient computation for the determinant of the precision matrix, as well as the multivariate CAR

model which is though more computationally demanding.

Uni-variate HMMs can be extended their multivariate version by incorporating spatio-temporal

random effects (Heaton et al., 2012; Zou et al., 2012, 2014) and iterative update formula of

P r(Z = 1) was also provided to circumvent parameter re-estimation when new observations arrive.

Dimension reduction also needs to be considered when the number of spatial locations is large

and there are many areas with small counts. Zou et al. (2018) addressed this issue via a semi-

parametric Dirichlet process for clustering similar regions and applied the particle filter approach

to make inferences on latent variables. A real-time Bayesian spatio-temporal syndromic surveil-

lance framework was also applied to small companion animals as an auxiliary source for public

health surveillance (Hale et al., 2019). Other Bayesian approaches such as Bayesian scan statistics

(Neill, 2011), Bayesian networks (Cooper et al., 2015) and Bayesian disease mapping (Anderson

et al., 2017) are also prevalent choices in public health surveillance systems to handle such as point-

reference spatial data Banerjee et al. (2003), individual-level medical records, etc. Point-referenced

data are also known as geostatistical data containing precise location information for individual

data points, and the public health surveillance systems may usually aggregate the individual data

points over a set of disjoint areas due to privacy concerns.

One important concern regarding the Bayesian frameworks is their computational cost. Most

of public health surveillance literature using Bayesian frameworks adopted MCMC method as the

computational tool, which can be significantly time-consuming if data dimension increases or the

complex model structure is poorly specified. Although Rue et al. (2009) proposed Integrated

Nested Laplace Approximation as an efficient computational tool, there is limited literature to our

90

---

<!-- PAGE 92 -->

knowledge that employed INLA implementation in public health surveillance (Manitz and H¨ohle,

2013; Salmon et al., 2015).

With the enhancement of computational power, machine learn methods in disease monitoring

provides another solution to address the complex dynamics involving both social and biological

systems. During the pandemic of COVID-19, it becomes more challenging and numerous early

outbreak detection applications are delivered in this research area. Deep Learning-based models

were also used. Saqib (2021) proposed a hybrid machine learning model that is not only pre-

dicted with good accuracy but also takes care of uncertainty of predictions using Bayesian Ridge

Regression. Radev et al. (2021) presented a simulation-based Bayesian inference framework for

complex epidemiological models using neural network which utilized short time-series samples to

obtain early warning signals while Li et al. (2022b) introduced a model-based method. Most of

these methods have limitations due to the number of data availability. According to Coughlin

et al. (2021),they identified possible change or turning points as indicated by the dynamics of daily

COVID-19 incidences which the identified change points were combined with the spline-fitted trend

which interprets the behavior of the change points; it may have provided better prediction dates

for the implementation of public restrictive interventions in each country but not appropriate for

all nations. Even Guan et al. (2021) added prediction method using mobility data which helps to

determine when and where outbreaks will occur, it has several limitations such as smoothing, miss-

ing data, and based on information about only known cases but not undetected cases. However,

the practical limitations facing machine learning methods include the vast amount of training data,

risk of over-fitting, and accurate labels for outbreaks in the training data.

4.3 BOSTON-PUPA procedure

To address complex and dynamic spatio-temporal patterns of streaming surveillance data, we pro-

pose a consolidated Bayesian Online Spatio-Temporal Outbreak detecitoN framework with Prior

Updating and P-value Adaptation (BOSTON-PUPA) techniques to effectively achieve both global

and local sequential monitoring over a cluster of regions at risk. The streaming data of confirmed

case counts take a spatio-temporal format as they are reported from various locations on a daily

basis. As an iterative process with a fixed-size sliding window, the BOSTON-PUPA framework

accounts for the spatio-temporal association and overdispersion of the count data via a Bayesian

91

---

<!-- PAGE 93 -->

hierarchical generalized Poisson distribution (GPD) model with Integrated Nested Laplace Ap-

proximation (INLA) method. The Prior Updating technique leverages past information and the

current sliding window sequentially for integrated inference with a reduction of computational bur-

dens. The P-value Adaptation technique enhances the significance of a true outbreak to address

potential imbalance issues for spatial data, especially for the regions with small counts. The incor-

poration of eclectic techniques results in decent false detection control while preserving a robustly

high detection power and efficiency against different signal-to-noise ratios.

Our proposed Bayesian Online Spatio-Temporal Outbreak detectioN with Prior Updating and

P-value Adaptation (BOSTON-PUPA) framework is an iterative procedure with a sliding window

for the training data modeling with window length T + 1. The streaming data are monitored

consecutively with a one-day-ahead sliding pace and only the observed counts on the last day in

the sliding window will be involved in the outbreak detection procedure. With the initial sliding

window containing observed data from day 1 and day T + 1, the outbreak detection procedure aims

at testing the null and the alternative hypotheses H (s)

0,k versus H (s)

a,k, k = 1, 2, ..., as below,





H (s)

0,k : No significant outbreak has occurred yet in the s-th location by the (T + k)-th day.

H (s)

a,k : An outbreak has occurred significantly in the s-th location by the (T + k)-th day.

(4.1)

The iterative outbreak detection procedure involves four steps: 1) Bayesian model inference and

in-sample prediction. 2) Latent aberration assessment. 3) P-value adaptation. 4) Decision-making

and algorithm update. To elucidate the detection procedure, we elaborate on each step at the k-th

iteration for instance.

4.3.1 Step 1: Bayesian model inference and in-sample prediction

First, we will introduce the model framework for the surveillance data under the null hypothesis

of no outbreak at any location. Let {Ys,t} denote the daily case count at day t at location s.

We propose the following conditional generalized Poisson distribution (GPD) framework for the

92

---

<!-- PAGE 94 -->

multivariate count time series,

Ys,t|θs,t, λ ind∼ GP D(θs,t, λ),
(cid:18) θs,t
1 − λ

ηs,t = log µs,t = log

(cid:19)

= Ps + XsβXsβXsβ + ϕs + εt,



ϕs|ϕϕϕ−s ∼ N

ρϕ

(cid:88)

j̸=s

wsj
ws+

ϕj,



 ,

σ2
ϕ
ws+

εt = ρεεt−1 + ωt, ωt ∼ N (0, σ2

ε ),

(4.2)

ΘΘΘ = (λ, βββ, ρϕ, ρε, σ2

ϕ, σ2

ε ) ∼ π(ΘΘΘ).

In (4.2), s = 1, 2, . . . , S, t = 1, 2, . . . , T , where S is the total number of locations and T is the

total number of days in the sliding window. Ps is the offset term for location s and it accounts

for differences in expected values or exposures at each location.

In our study, we choose the

logarithmic population as the offset term. XsXsXs is the covariate vector of interest for location s and

βββ is the corresponding fixed effect vector. ϕϕϕ = (ϕ1, ϕ2, . . . , ϕs) are the spatial effects and account

for the neighboring association among all the spatial units. WWW = (wsj)S×S is the adjacency matrix

for these locations,

wsj =






1, if location s and location j are adjacent

0, otherwise.

The diagonal elements of WWW are zeros and ws+ = (cid:80)S

j=1 wsj. εt is the common temporal latent effect,

describing the shared dynamics by the mean functions of the counts from different locations. We

assign the Conditional Autoregressive (CAR) prior and an AR(1) process prior to the spatial and

temporal latent effects correspondingly. ΘΘΘ contains all the parameters in the Bayesian hierarchical

framework. The prior distribution for ΘΘΘ is π(ΘΘΘ), which will be discussed shortly in detail.

Considering the potential dispersion of count data, We select a conditional GPD for the count

data. The point mass function of a conditional GPD (Consul and Jain, 1973) given as

P r(Ys,t = y|θs,t, λ) =






θs,t(θs,t+λy)y−1
y!

· exp (−(θs,t + λy)), y = 0, 1, 2, ...

(4.3)

0 for y > m, when λ < 0

93

---

<!-- PAGE 95 -->

with mean µs,t = θs,t/(1 − λ) and variance σ2

s,t = µs,t · (1 − λ)−2, max(−1, −θs,t/m) < λ < 1

and m(≥ 4) is the largest positive integer for which θs,t + mλ > 0 when λ is negative. Since our

framework focuses on the overdispersion pattern in the count data, the range of λ is restricted

within [0, 1). When λ = 0, the GPD becomes a standard Poisson distribution. Such flexibility

can better accommodate the small counts, especially when θs,t is close to zero. When the mean

parameter θs,t approaches zero, the underlying distribution will face a degeneracy issue, with a

dominant probability on P (Ys,t = 0|θs,t, λ) ≈ 1. For the observed small counts at some locations,

a detection procedure attributed to such a point mass distribution will deliver an extreme test

statistic under H (s)

0,k even if the magnitude of the counts doesn’t qualify for an outbreak claim.

Compared with the standard Poisson distribution, a GPD with an overdispersion parameter will

be less likely to reach a false alarm of an outbreak because it can account for larger variations in

the counts than a standard Poisson distribution does.

In the INLA implementation of (4.2), all the parameters with restricted support will be inter-

nally transformed into the ones with support on R as described in Table 13. Such a reparame-

terization technique grants efficient computation of the internal parameters on their unrestricted

supports. Therefore, we assign the internal hyperparameters, ϑϑϑ = (ξ, βββ, ϑρϕ, ϑρε, ϑσ2

ϕ

, ϑσ2

ε

), in (4.2)

with Gaussian priors. The variances of the Gaussian priors quantify the uncertainty about the

internal parameters. In order not to cause further confusion in the rest of the paper, we use the

parameters/internal parameters to include the covariate coefficients and the hyperparameters.

Hyperparameter Support

Internal representation

λ

ρϕ

ρε
σ2
ϕ
σ2
ε

(0, 1)

(0, 1)

(−1, 1)

(0, ∞)
(0, ∞)

(cid:17)

ξ = log

ϑρϕ = log

(cid:16) λ
1−λ
(cid:16) ρϕ
1−ρϕ
(cid:16) 1+ρε
1−ρε
= log(σ2
ϕ)
= log(σ2
ε )

ϑρε = log
ϑσ2
ϑσ2

ϕ

ε

(cid:17)

(cid:17)

Table 13: Hyperparameters with restricted support and their internal representation

In a sliding window of size T + 1 at the k-th iteration, (4.2) is fitted on the training data

94

---

<!-- PAGE 96 -->

DDDk = {YYY k+t}T

t=0, with YYY k+t = {Y1,k+t, Y2,k+t, . . . , YS,k+t} with a prior π(ΘΘΘ) = π(ϑϑϑ)| ∂ϑϑϑ

∂ΘΘΘ |,

π(ϑϑϑ) =






πG(ϑϑϑ), 1 ≤ k ≤ T + 1

πa0
G (ϑϑϑ|DDD∗

k−T −1), k ≥ T + 2

(4.4)

where πG(ϑϑϑ) corresponds to a vague internal Gaussian prior with a large variance, used in the first

(T + 1) iterations. After the (T + 1)-th iteration, π(ϑϑϑ) = πa0

G (ϑϑϑ|DDD∗

k−T −1) becomes a historical-

data-related Gaussian prior raised to a discounting factor a0(0 < a0 ≤ 1), where DDD∗

k−T −1 is the

past cumulative information set up to the (k − T − 1)-th iteration and has no overlap with the

current training data DDDk. Since (4.2) doesn’t have a closed form for the posteriors of its parameters

or hyperparameters, we intend to only borrow the historical information via a Gaussian prior,

πG(ϑϑϑ|DDD∗

k−T −1), which shares the first two moments with the corresponding posterior as in (4.5) for

the purpose of prior updating in our iterative detection procedure,

(cid:90)

(cid:90)

ϑ∗πG(ϑ∗|DDD∗

k−T −1)dϑ∗ =

(cid:90)

ϑ∗π(ϑ∗|DDD∗

k−T −1)dϑ∗

(ϑ∗)2πG(ϑ∗|DDD∗

k−T −1)dϑ∗ =

(cid:90)

(ϑ∗)2π(ϑ∗|DDD∗

k−T −1)dϑ∗,

(4.5)

where πG(.) denotes a Gaussian density and π(ϑ∗|DDD∗

k−T −1) corresponds to the actual posterior
density for the internal parameter ϑ∗ in ϑϑϑ. After the k-th iteration of model fitting, three pieces of

information will be tracked, ˆηˆηˆηT +k, ( ˆξk, ˆσ2
ξk

), and the posterior distributions for internal parameters.

ˆηˆηˆηT +k = (ˆη1,T +k, ˆη2,T +k, . . . , ˆηS,T +k) denotes the transformed posterior mean vector of YYY T +k|DDDk in
(4.2). ˆξk and ˆσ2
ξk

are the internal posterior mean and variance for the overdispersion parameter

in Table 13. An illustration of Step 1 is summarized from Table 14 in which the model inference

and in-sample prediction refer to the columns, “Mean”, “Overdispersion”, and “Posterior”. The

“Posterior” column in Table 14 refers to the posterior distribution for the internal parameter ϑϑϑ and

π(ϑϑϑ|DDD∗

k−T −1) = π(ϑϑϑ|DDDk−T −1, DDDk−2T −2, DDDk−3T −3, . . . ), where DDDk−T −1∩DDDk−2T −2∩DDDk−3T −3∩· · · = Ø.

95

---

<!-- PAGE 97 -->

Iteration (k) Training data

Prior

Mean Overdispersion

Posterior

1
2
...
T + 1
T + 2
...
2T + 2
2T + 3
...

DDD1
DDD2
...
DDDT +1
DDDT +2
...
DDD2T +2
DDD2T +3
...

πG(ϑϑϑ)
πG(ϑϑϑ)
...
πG(ϑϑϑ)
πa0
G (ϑϑϑ|DDD1)
...
πa0
G (ϑϑϑ|DDDT +1)
πa0
G (ϑϑϑ|DDDT +2, DDD1)
...

ˆηˆηˆηT +1
ˆηˆηˆηT +2
...
ˆηˆηˆη2T +1
ˆηˆηˆη2T +2
...
ˆηˆηˆη3T +2
ˆηˆηˆη3T +3
...

)
)

( ˆξ1, ˆσ2
ξ1
( ˆξ2, ˆσ2
ξ2
...

( ˆξT +1, ˆσ2
( ˆξT +2, ˆσ2

ξT +1

ξT +2

)
)

( ˆξ2T +2, ˆσ2
( ˆξ2T +3, ˆσ2

ξ2T +2

ξ2T +3

)
)

...

...

π(ϑϑϑ|DDD1)
π(ϑϑϑ|DDD2)
...
π(ϑϑϑ|DDDT +1)
π(ϑϑϑ|DDDT +2, DDD1)
...
π(ϑϑϑ|DDD2T +2, DDDT +1)
π(ϑϑϑ|DDD2T +3, DDDT +2, DDD1)
...

Table 14: Iterative prior updating procedure with tracked mean and overdispersion

4.3.2 Step 2: Latent aberration assessment

During the iterative procedure with a sliding window, two types of latent aberrations are monitored

simultaneously: global latent aberration and local latent aberration. Latent aberrations in the

detection procedure are assessed via binary indicators stemming from comparisons between Z-

score-based statistics and a user-specified threshold. The aberration indicators calculated in this

step facilitate the subsequent p-value adaptation process.

To indicate the latent aberration at the k-th iteration, two latent estimates are of interest: the

estimates of overdispersion parameter ˆλk and location-wise GPD mean ˆµs,T +k. The global latent

aberration is associated with the overdispersion parameter λ in (4.2) because the spatio-temporal

data share the common overdispersion parameter and any extreme counts observed from either

location will contribute to a larger estimate for the overdispersion parameter, signaling a global

latent aberration that certain location(s) can be experiencing unusual case counts. To specify the

local latent aberrations, ˆµs,T +k will be compared with its historical estimates, and a larger value

of ˆµs,T +k tend to deviate from its historical pattern thus raising an alarm. Since binary aberration
indicators are Z-score-based, the corresponding internal representations, ˆξk and ˆηs,T +k, are used in

the calculation due to their unrestricted supports.

There are two sorts of collections involved to keep track of those two types of historical estimates.

The collection of the estimates for the overdispersion, ΞΞΞk =

(cid:110)
( ˆξ1, ˆσ2
ξ1

), ( ˆξ2, ˆσ2
ξ2

), . . . , ( ˆξk, ˆσ2
ξk

)

(cid:111)

, refers

to the “Overdispersion” column in Table 14, where the posterior estimates of mean and variance are

96

---

<!-- PAGE 98 -->

gathered sequentially. Meanwhile, the collection of posterior mean estimates refers to the “Mean”

column in Table 14. HHHs,k = {ˆηs,T +1, ˆηs,T +2, . . . , ˆηs,T +k} denotes the historical estimates set for the

s-th location. When k = 1, ΞΞΞk = HHH1,k = · · · = HHHS,k = Ø. When k ≥ 3, the global and local latent

aberration indicators, δ ˆξk

and δˆηs,T +k , s = 1, 2, . . . , S, are calculated respectively in (4.6),

δ ˆξk

= I

(cid:32) ˆξk −

¯ˆξk−1

¯ˆσξk−1

(cid:33)

> z

¯ˆξk−1 =

,

1
k − 1

k−1
(cid:88)

i=1

ˆξi, ¯ˆσξk−1 =

(cid:115) (cid:80)k−1

i=1 ˆσ2
ξi
k − 1

.

and (4.7),

δˆηs,T +k = I

(cid:32)

ˆηs,T +k − ¯ˆηs,T +k−1
σHHHs,k−1

(cid:33)

> z

, ¯ˆηs,T +k−1 =

1
k − 1

k−1
(cid:88)

i=1

ˆηs,T +i,

σHHHs,k−1 =

(cid:115)

(cid:80)k−1

i=1 (ˆηs,T +i − ¯ˆηs,T +k−1)2
k − 2

.

(4.6)

(4.7)

In (4.6) and (4.7), I(·) denotes an indicator function, and z was chosen to be 2 with empirical

normal approximations for the internal parameters. When k = 1, 2, δ ˆξk
of the historical estimates for the overdispersion parameter and GPD means aims at providing

= δˆηs,T +k . The collection

a baseline pattern when no outbreaks have happened during the monitoring procedure. The true

posteriors for those latent parameters don’t have analytic expression thus the normal approximation

technique acts as a rudimentary screening for potential outbreaks. Nonetheless, such preliminary Z-

score-based aberration indicators contribute to a refined p-value-based outbreak detection approach

in the next step.

4.3.3 Step 3: P-value adaptation

Since an outbreak is associated with the occurrence in a region of cases of an illness or health-

related events clearly in excess of normal expectancy, public health practitioners are more likely to

claim a disease outbreak when the observed incidence count in a region is unusually high or takes

a drastic jump, regarding the early outbreak detection application.

It would be meaningless to

claim an outbreak when no significant deviation takes place from the past data pattern. Therefore,

one-sided p-values become a natural measurement for the outbreak evidence against H (s)

0,k. Not only

97

---

<!-- PAGE 99 -->

can the p-values be converted to binary outcomes given a user-defined threshold as in Farrington’s

algorithm, but also provide the magnitude of extremeness for the observations under the null

hypotheses. However, p-values will have reduced significance at a contaminated baseline estimate

when the sliding window contains a mixture of non-epidemic and epidemic data. To boost the signal

of a potential outbreak, we propose an adapted p-value computation with the latent aberration

indicators obtained in Step 2. In the k-th iteration, the adapted p-value at location s with the

observed count ys,T +k is calculated as in (4.8),

p∗
s,T +k =

where

˜ps,T +k =





˜ps,T +k,

ps,T +k,

if δ ˆξk

= 1.

if δ ˆξk

= 0.




P r

(cid:16)

Ys,T +k > ys,T +k|¯ˆηs,T +k−1,

¯ˆξk−1, H (s)

0,k

(cid:17)

,

if δˆηs,T +k = 1.



ps,T +k,

if δˆηs,T +k = 0.

(4.8)

The adaptation for the p-value in (4.8) is determined by δ ˆξk

and δˆηs,T +k . When both the global

and local latent aberrations for location s are triggered, the corresponding p-value will be adaptively

calculated using smaller estimates of baseline GPD mean and overdispersion, in order to increase the

significance of a potential outbreak. Otherwise, the regular Bayesian posterior predictive p-values

are computed to quantify the evidence against H (s)

0,k as in (4.9),

ps,T +k = P r

(cid:16)

Ys,T +k > ys,T +k|DDDk, DDD∗

k−T −1, H (s)

0,k

(cid:17)

I (Ys,T +k > ys,T +k) p(Ys,T +k|DDDk, DDD∗

k−T −1, H (s)
0,k)

(cid:88)

Ys,T +k


(cid:90)



(cid:88)

=

=

=

=

I (Ys,T +k > ys,T +k) p(Ys,T +k|ΘΘΘ)


 p(ΘΘΘ|DDDk, DDD∗

k−T −1, H (s)

0,k)dΘΘΘ

(4.9)

Ys,T +k

(cid:90)

P r (Ys,T +k > ys,T +k|ΘΘΘ) p(ΘΘΘ|DDDk, DDD∗

k−T −1, H (s)

0,k)dΘΘΘ

(cid:90) (cid:90)

P r (Ys,T +k > ys,T +k|ηs,T +k, ξk) p(ηs,T +k, ξk|DDDk, DDD∗

k−T −1, H (s)

0,k)dηs,T +kdξk.

The p-value adaptation step has two major benefits in the detection procedure. First of all,

it can avoid weakening signals of potential outbreaks if the sliding window contains a mixture of

98

---

<!-- PAGE 100 -->

baseline data and outbreak data. When the (4.2) is fitted on the count data contaminated by

unusually large observations, the conditional GPD mean µs,T +k will be overestimated as well as

its overdispersion parameter λk thus leading to an overestimated variance µs,T +k/(1 − λk)2, which
yields a large p-value weakening the evidence against H (s)

0,k. Secondly, When no aberration alarms

are raised, the Bayesian posterior predictive p-value incorporates the uncertainty of the model

parameters by integrating the conventional p-value over their joint posterior density. Hence, the

Bayesian posterior predictive p-value provides a baseline significance level of rejecting H (s)

0,k when

no outbreak occurs. In (4.9), ηs,T +k and ξk are sufficient for the computation of Bayesian p-value

because ηs,T +k is a function of all other parameters and ps,T +k can be approximated by the average

of p-values conditional on the joint posterior samples of ηs,T +k and ξk. Next, the adapted p-values

can be accumulated recursively for outbreak detection in the following step.

4.3.4 Step 4: Decision-making and algorithm update

The decision-making step is based on combined p-values for two reasons: 1) some individual p-values

obtained with small magnitude during the iterative procedure will not be necessarily caused by an

outbreak, especially if the monitored data have a highly overdispersed pattern and the procedure

hasn’t encountered any extreme observations due to overdispersion. 2) The successive modeling

fitting procedure with a sliding window has training data set with overlaps, which introduces a

dependent association among the sequential hypothesis tests. For example, the intersection of two

consecutive training data sets, DDDk−1 and DDDk, is DDDk−1 ∩ DDDk = {YYY k+t}T −1

t=0 . Therefore, such decision-

making in the online outbreak detection procedure will integrate dependent historical information

to assess the ongoing dynamics in the surveillance system via a combined p-value approach. The

combined p-value approach is known as the global test (also named omnibus test) of p-values and

it is a popular technique in high-dimensional genetic data analysis for multiple hypothesis tests. A

plethora of research work has been done to combine independent and dependent p-values for the

global test in the genetic study. Instead of combining all available p-values and performing a single

global test, the online procedure keeps updating recent p-values sequentially until an outbreak is

detected thus leading to a series of affiliated global tests. With the adapted p-value calculated in

99

---

<!-- PAGE 101 -->

the previous step, the k-th cumulative detector statistics will be updated as in (4.10),

Qs,T +k = Qs,T +k−1 + g(p∗

s,T +k)

where

Qs,T +k−1 =

k−1
(cid:88)

i=1

g(p∗

s,T +i) and Qs,T +0 = 0.

(4.10)

In (4.10), g(·) is a transformation function of the p-values. In the conventional tests of combined

p-values, the classical choices for g(·) include log transformation (Fisher, 1932), inverse Gaussian

transformation (Stouffer et al., 1949) and inverse gamma transformation (Lancaster, 1961). When

p-values follow the identical and independent uniform distribution under the global null hypoth-

esis, Qs,T +k will have simple limiting distributions. However, When p-values are dependent, the

resulting distribution of Qs,T +k becomes complicated and adjustments can be made to account for

the dependence via using an effective number of tests (Cheverud, 2001; Nyholt, 2004; Li and Ji,

2005; Gao et al., 2008; Galwey, 2009), using re-sampling methods such as permutation tests for an

empirical distributional approximation for the combined p-values (Westfall and Young, 1993; Good,

2013), or applying generalized multivariate theory to the classical choices of g(·) under dependence

(Brown, 1975; Kost and McDermott, 2002; Yang et al., 2016). Recent powerful combined p-value

tests include the Harmonic Mean P-value (HMP) approach (Wilson, 2019) and Cauchy Combina-

tion Test (CCT) approach (Liu and Xie, 2020), which can handle arbitrary correlation structure

among the test statistics although HMP approach doesn’t have the exact additive property shown

in (4.10).

Therefore, the real-time outbreak detection indicator δs,T +k for county s at iteration k is deter-

mined as in (4.11),

δs,T +k =




0,

I(Qs,T +k > qα

s,T +k), ∃ k∗ ≤ k, s.t. δ ˆξk∗ = 1,

(4.11)

otherwise,

where qα

s,T +k is the threshold associated with the corresponding method and α is the nominal level

for false detection control pre-determined by practitioners. Such a decision rule aims at controlling

false detection rates due to data overdispersion and increasing detection power when outbreaks

100

---

<!-- PAGE 102 -->

happen. At the end of iteration k, The baseline-resembling sets for the overdispersion parameter

and the conditional GDP mean are updated as follows,

HHHs,k = HHHs,k−1 ∪ (cid:8)(cid:0)1 − δˆηs,T +k

ΞΞΞs,k = ΞΞΞs,k−1 ∪

(cid:110)(cid:16)

(1 − δ ˆξk

(cid:1) ˆηs,T +k + δˆηs,T +k
¯ˆξk−1, (1 − δ ˆξk

) ˆξk + δ ˆξk

¯ˆηs,T +k−1

(cid:9)

)ˆσξk + δ ˆξk

¯ˆσξk−1

(cid:17)(cid:111)

(4.12)

The main purpose of (4.12) is to obviate contamination of the baseline collection by any aberrant

estimates thus enhancing the sensitivity of the algorithm. Meanwhile, the posterior inference will

also be collected in Table 14 for future use as prior information. In the next subsection, we are

going to implement the eclectic framework via numerical studies and demonstrate its performance

in different aspects.

4.4 Numerical study

4.4.1 Simulation study

In our simulation, we are going to illustrate the performance of the BOSTON-PUPA approach from

two aspects: (1) Model parameter recovery and in-sample model prediction; (2) Online outbreak

detection. For a better replication of the actual data pattern, the parameters in the model in (4.2)

is based on the model inference on the partial real data of daily confirmed COVID-19 case count

starting from June 15, 2020, which we assume to be in the non-outbreak phase before the news

report of an outbreak in the fall. The Boston Globe reported on October 26, that COVID-19 cases

in the state had risen sharply on October 22,

”After a sudden jump Thursday, Massachusetts coronavirus cases have been maintaining levels we

haven’t seen in months, raising concern among experts that the state might need to consider

rolling back some parts of its reopening process.”

A detailed real data description will be given in the real application section. The parameters

include fixed effects βden (related to county-wise population density, a ratio of its population to

the corresponding area), βDOW (related to the Day of Week effect), and βtime (related to a linear

time trend), as well as other spatio-temporal hyperparameters for the random effects. They are

summarized in Table 15. For constant terms, W is based on the border-sharing adjacency of 14

101

---

<!-- PAGE 103 -->

counties in Massachusetts. Due to the small populations of Dukes and Nantucket, we merged

these two neighboring island counties into one to avoid extreme population imbalance, and Ps are

logarithms of the county populations recorded in 2018 in Table 16.

Parameter

Symbol Value

Hyperparameter

Symbol Value

Intercept
Population density effect βden
Day of Week effect
Time trend effect

β0

βDOW
βtime

-13.5752 Overdispersion
.2905
.1762
.3056

λ
Temporal correlation ρϵ
σ2
Temporal variance
ϵ
ρϕ
Spatial correlation
σ2
Spatial variance
ϕ

.4448
.5123
.2609
.3588
.7275

Table 15: Parameter setup throughout the simulation study

Spatial ID County name

Population log(Population) (Ps)

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
11
12
13

Plymouth
Berkshire
Barnstable
Norfolk
Bristol
Suffolk
Franklin
Hampshire
Essex
Hampden
Dukes and Nantucket
Middlesex
Worcester

518132
126348
213413
705388
564022
807252
70963
161355
790638
470406
28679
1614710
830839

13.1580
11.7468
12.2710
13.4665
13.2428
13.6014
11.1699
11.9914
13.5806
13.0614
10.2639
14.2947
13.6302

Table 16: County populations in Massachusetts in 2018

4.4.1.1 Model parameter recovery and in-sample model prediction Due to the iterative

feature of the BOSTON-PUPA framework, the quality of model inference and prediction is influ-

enced by choices of the sliding window size (T ) and historical information discounting factor a0. For

a proof of concept, we conducted different combinations of sliding window sizes T = 14, 21, 28, 35, 42

and discounting factors a0 = 0.25, 0.5, 1. The total number of simulations is 200. For each simu-

lation, the total number of simulated case counts at each location is T0 = 200. To illustrate the

performance of parameter recovery for the baseline data, we only simulated the data without any

outbreak, and outbreak detection performance will be demonstrated in the next subsection. The

102

---

<!-- PAGE 104 -->

measurement of the parameter recovery is defined as a binary outcome of whether or not the true

parameters from the setup are captured by their corresponding 95% posterior credible interval in

the BOSTON-PUPA procedure. As for the measurement of in-sample prediction, we measure the

Mean-Squared-Error (MSE) between the true observation and in-sample prediction for the last day

in the sliding window, because latent aberration assessment in step 2 is dependent on the last-day

estimates ˆηs,T +k and historical baseline estimates ¯ˆηs,T +k−1 in (4.7). Therefore, there are in total

(T0 − T ) × 200 model fittings in the simulation study, from which we summarized the performance

of parameter recovery and in-sample model prediction. The results are shown in Table 17 and 18,

From Table 17, we can see that all the fixed effect and hyperparameter recovery rates increase

with a larger sliding window size (T ) and a smaller discounting factor (a0), except for the temporal

variance (σ2

ϵ ). For the majority of the parameters, a sliding window with a larger width provides

more information in the training data, which can enhance the model inference. Meanwhile, a smaller

discounting factor dampens the certainty of historical information prior and grants more flexibility

for the INLA solver to explore the posterior distribution for the current training data. Since all the

internal parameter representations are assigned with a Gaussian prior, the original variance σ2 in

the prior turns into σ2/a0 after discounting and shows complete historical information (a0=1) does

not yield good model inference according to Table 17. However, since the logarithmic GDP mean in

(4.2) contains a summation of separable spatial effect and temporal effect, a larger sliding window

size tends to reduce more uncertainty about the spatial effect than the temporal effect, which can

explain why there is an opposite relationship between parameter recovery rate and sliding window

size for the temporal variance (σ2

ϵ ). Although the hyperparameter recovery rates for the spatial

effects and the temporal effects are not as good as the other parameters, it is still satisfactory to get

recovery rates above 70% for these second-level parameters with appropriate selections for T and

a0. From Table 18, the choice of discounting factor has a negligible impact on the MSE. Although

there tends to be a slight positive relationship between sliding window size and MSE, the increments

are not significant and it is related to different total numbers of model fittings ((T0 − T ) × 200) in

the MSE calculation.

An appropriate selection of sliding window size is a trade-off between methodological efficiency

and detection timeliness. As is demonstrated in Farrington and Andrews (2003), the size of train-

ing data to reflect a baseline pattern ranges from 2 to 8 weeks, depending on the specifics in the

103

---

<!-- PAGE 105 -->

Parameter

a0

(T=)14

21

28

35

42

β0

βden

βDOW

βtime

λ

ρϵ

σ2
ϵ

ρϕ

σ2
ϕ

0.25
0.5
1

0.25
0.5
1

0.25
0.5
1

0.25
0.5
1

0.25
0.5
1

0.25
0.5
1

0.25
0.5
1

0.25
0.5
1

0.25
0.5
1

0.9910
0.9703
0.5159

0.9442
0.9234
0.6557

0.9485
0.9620
0.9088

0.9870
0.9701
0.5428

0.9633
0.9691
0.9313

0.8921
0.9010
0.6213

0.8448
0.8269
0.4845

0.5702
0.5535
0.5157

0.8796
0.3681
0.1349

0.9900
0.9658
0.6509

0.9439
0.9209
0.7469

0.9546
0.9639
0.9303

0.9855
0.9703
0.6732

0.9650
0.9702
0.9413

0.9163
0.9122
0.7358

0.8340
0.7998
0.5213

0.6649
0.6348
0.6242

0.8963
0.4372
0.1983

0.9907
0.9692
0.7458

0.9419
0.9210
0.7938

0.9544
0.9616
0.9352

0.9857
0.9710
0.7756

0.9668
0.9695
0.9453

0.9276
0.9262
0.8137

0.8178
0.7711
0.5471

0.7343
0.7044
0.6912

0.9128
0.5365
0.2714

0.9870
0.9643
0.8068

0.9403
0.9194
0.8240

0.9544
0.9605
0.9377

0.9824
0.9671
0.8363

0.9642
0.9663
0.9502

0.9328
0.9297
0.8592

0.7934
0.7452
0.5658

0.7587
0.7501
0.7542

0.9206
0.6554
0.3561

0.9847
0.9673
0.8458

0.9394
0.9181
0.8462

0.9509
0.9580
0.9348

0.9785
0.9672
0.8690

0.9633
0.9659
0.9478

0.9352
0.9360
0.8735

0.7643
0.7206
0.5722

0.7935
0.8020
0.7947

0.9267
0.7435
0.4446

Table 17: Parameter recovery rate under different combinations of sliding window size and prior
discounting factor

(cid:97)(cid:97)(cid:97)(cid:97)(cid:97)(cid:97)(cid:97)(cid:97)(cid:97)(cid:97)(cid:97)

a0

T

14

21

28

35

42

0.25
0.5
1

9.1479
9.1456
9.1395

9.3548
9.3497
9.3471

9.4971
9.4958
9.4942

9.6074
9.6064
9.6051

9.7028
9.7019
9.7009

Table 18: MSE for the last-day prediction in the sliding window

104

---

<!-- PAGE 106 -->

surveillance system such as the disease outbreak span or data format from regulatory authorities.

The computational cost is another criterion to choose a better combination of tuning parameters.

However, due to the initial value self-correction feature of the internal rinla program, the time con-

sumption can have a wide range in different simulations, which is less reliable to quantify the model

computational speed. In general, a larger sliding window tends to have a higher computational cost.

Taking into account all the combinations of sliding window sizes and discounting factors, we can

moderately select T = 28 and a0 = 0.25 for the procedure BOSTON-PUPA. Since the optimal

tuning parameter selection for our proposed framework is not the focus of this dissertation, we

will just proceed with the outbreak detection performance evaluation with a reasonable choice for

T and a0. As a comparison, we also considered using all historical data in a sequential approach

in which the window size increases with newly observed data and weakly informative priors are

maintained throughout the procedure. In Table 19, our Prior Updating (PU) approach with T = 28

and a0 = 0.25 have an overall better performance than the cumulative fitting (CF) approach in

terms of parameter recovery and in-sample prediction accuracy.

Performance

PU

CF

Performance

PU

CF

β0 recovery rate
βden recovery rate
βDOW recovery rate
βtime recovery rate
λ recovery rate
ρϵ recovery rate

.9907
.9419
.9544
.9857
.9668
.9276

ϵ recovery rate
ρϕ recovery rate
ϕ recovery rate

.9450 σ2
.9408
.9505 σ2
.9315 MSE
.9473 Computational time
.9159

.8178
.7343
.9128
9.4971
74.3770 (s)

.5631
.9715
.9646
27.3535
133.0322 (s)

Table 19: Performance comparison between Prior Updating (PU) approach (T = 28, a0 = .25) and
Cumulative Fitting (CF) approach. Computation time is calculated as the average computation
time in seconds for individual model fittings in the iterative process.

4.4.1.2 Outbreak detection performance Next, we will demonstrate the outbreak detection

performance of the BOSTON-PUPA framework under different scenarios of signal-to-noise ratio

(SNR). We keep the parameter setup in the previous section and introduce disease outbreaks at

different locations.

In the data generation process, the outbreak occurring time stamps τs, s = 1, 2, . . . , 13, were

randomly generated from a Poisson distribution with mean 100 as 103, 99, 95, 82, 102, 102, 102,

91, 89, 97, 109, 100 and 87, which divided the 13 locations into non-outbreak and outbreak phases

105

---

<!-- PAGE 107 -->

correspondingly. Baseline counts were generated for each location throughout T0 = 200 days and

outbreaks were introduced after the outbreak time stamps accordingly given the SNR in (4.13),

Ys,t|θs,t, λ ∼ GP D(θs,t + δs,tθ∗

s,t, λ),

θ∗
s,t = (r − 1)θs,t,

(4.13)

where SNR is r = V ar(Ys,t|rθs,t, λ)/V ar(Ys,t|θs,t, λ) and δs,t is a binary outbreak indicator for

location s on day t. We also considered numerical adjustment by adding 5 to θ∗

s,t when introducing

outbreak into baseline data, because the multiplicative association between θs,t and θ∗

s,t won’t

add meaningful outbreak to the baseline data when θs,t is close to zero. For real application in

surveillance systems, practitioners will also set a minimum bar for the observed counts before

claiming a reasonable outbreak.

In Step 4 of the BOSTON-PUPA procedure, we chose both classical and recent combined p-value

for dependent hypothesis tests: Fisher’s, Lancaster’s, and Stouffer’s approaches adjusted with the

effective number of hypothesis tests (Li and Ji, 2005), P-value (HMP) and Cauchy Combination Test

(CCT) approach from existing R packages, poolr, ACAT, and harmonicmeanp. Four measurements

were taken to evaluate the outbreak detection performance among these methods with/without

p-value adaptation: Sensitivity = TP/(TP+FN), Specificity = TN/(TN+FP), Proportion of False

Positive (PropFP) = FP/(TP+FP), and Global Error (GE) = (FP+FN)/(TN+TP+FP+FN). We

set α = 0.05 for the false detection control and investigate the detection performance when SNR =

1 (No outbreak), 1.25, 1.5, 1.75, and 2 with 200 simulations for each scenario. We will summarize

the outbreak detection performance of the BOSTON-PUPA procedure from the following four

perspectives:

1. Performance enhancement by P-value Adaptation (PA). To illustrate the detection

performance enhancement by PA technique, four evaluation measurements are aggregated by

different combined p-value methods as well as all spatial locations, compared only regarding

whether incorporation of PA technique is applied in the outbreak detection procedure. In Fig-

ure 19, there is a significant improvement in increasing Sensitivity and GE with PA technique.

When SNR ranges from 1.25 to 2, a larger SNR leads to less variation on those four perfor-

106

---

<!-- PAGE 108 -->

mance measurements especially for Sensitivity and GE, as the outbreak signal strengthens.

Although PA technique doesn’t give a superior Specificity and PropFP over its exclusion, the

benefit of PA technique can still be asserted. According to the formulae of the Specificity and

PropFP, a high value of Specificity or a low value of PropFP implies a small portion of false

positives are produced in the detection procedure, which is expected for an ideal outbreak

detection procedure. However, with comparable Specificity and PropFP, the incorporation of

PA technique with higher Sensitivity measurement has a higher power than No-PA technique.

Instead of being overly conservative in the detection procedure, PA technique can boost the

outbreak signal and actively facilitate accurate outbreak claims, which is a crucial attribute

of an efficient online outbreak detection procedure. It is worth mentioning that PA technique

grants an average of Sensitivity as high as about 75% even when the SNR = 1.25.

Figure 19: Signal-to-ratio vs Aggregated Performance Measurements

2. Empirical detection power and delay. Regarding the empirical detection power, the

relative frequencies of detecting an outbreak out of 200 simulations using the BOSTON-PUPA

107

---

<!-- PAGE 109 -->

procedure are collected in Table 20. When SNR = 1, the relative frequencies can be regarded

as empirical false detection rates accordingly for each location. For all of combined p-value

methods, the empirical false detection rates are controlled at α = 5% or with slight inflation

(5.5% ∼ 6.5%) except for locations with spatial IDs, 2, 3, 7, 8, and 11, which correspond

to the ones with the first five smallest populations in the study. HMP and CCT methods

have a better false detection control (< 5%) for these less populated locations than the other

methods (4% ∼ 16%) using the adjustment of effective numbers of tests and Stouffer’s method

has the most inflated false detection rates (12.5% ∼ 16%).

When SNR = 1.25, 1.5, 1.75, and 2, the relative frequencies can be interpreted as empirical

detection powers. BOSTON-PUPA procedure demonstrates its powerful detection perfor-

mance for all methods for outbreaks with different signal-to-ratios. The detection powers

reach as high as over 80% when SNR starts at 1.25 and increase to nearly 100% for larger

SNRs. HMP and CCT methods are uniformly more powerful than Fisher’s, Stouffer’s, and

Lancaster’s methods for locations with large populations. Although Fisher’s, Stouffer’s and

Lancaster’s methods demonstrate their high power in those less populated locations, such

high powers also result from their excessive false detection rates so that outbreaks detected

by HMP and CCT methods have more credibility.

When outbreaks are detected for the streaming data, it is also important to study the dis-

tributions of the detected outbreak time points for detection delay evaluation. Figure 20

presents empirical distributions for the detection delays. For the locations with large popu-

lations, the outbreak indicators are triggered around the actual outbreak time points given

in the simulation study. As SNR increases, the empirical distributions of detected outbreaks

tend to concentrate more on the true values. For the less populated locations, 2, 3, 7, 8, and

11, outbreaks are detected before their true occurrences, while detected outbreaks have a

wider spread for the rest of the locations. For the locations with small populations, the

false detection was made almost at the earliest true break, τ4 = 82, because the combined

p-values based on Fisher’s, Stouffer’s, and Lancaster’s methods had already been below α be-

fore the global aberration indicator was triggered at τ4 = 82. According to the decision rule

in Step 4, these regional outbreaks will be claimed immediately when the global aberration

108

---

<!-- PAGE 110 -->

alarm is triggered, which leads to the regional outbreak indicators δs,T +k dominated by the

global aberration indicator δ ˆξk
the global indicator but the false outbreaks were way too early detected and could even be

. We have also run simulations with decision rule not involving

claimed at the beginning of the monitoring process. Therefore, such domination helps avoid

false detection too early before true outbreaks for those three methods in small areas. From

this perspective, we need to acknowledge the limitation that controlled false detection rates

for the less populated areas only remain until a global aberration alarm is raised, because the

baseline GPD expectations have low or close to zero estimates, false outbreak detection is

very sensitive to small counts. We have done the simulations as well for early (around day 50)

and late (around day 150) outbreaks across 13 locations and observed similar performance

among these methods. As a comparison, HMP and CCT methods show more robustness

against random fluctuations caused by data overdispersion.

Based on the empirical detection delays, it is also flexible for practitioners to customize

decision-making rules for individual locations. Rather than a proactive outbreak detection

strategy with the first non-zero δs,T +k, a scheme via aggregating the real-time outbreak

indicators using a screening window can help reduce the false detection but unavoidably

prolong the detection delay. Such trade-off strategies between low false detection rate and

short detection delay are more related to decision theory, and it is beyond the scope of this

dissertation.

3. Recommendations for combined p-value methods We would also like to compare dif-

ferent existing combined p-value methods and make recommendations to implement the

BOSTON-PUPA procedure. Figure 21 demonstrates the spatially aggregated detection per-

formance among those five methods when PA technique is incorporated. While Stouffer’s

method slightly falls short of the performance, the other four methods present competitive

performance. Fisher’s and Lancaster’s methods perform better than HMP and CCT meth-

ods regarding Sensitivity and GE, whereas the latter two methods have better Specificity

and PropFP. Before a final recommendation is made, the spatial detection performance can

be taken into consideration due to potential population imbalance for online spatio-temporal

data.

109

---

<!-- PAGE 111 -->

Method

SNR 1

Fisher

Stouffer

Lancaster

HMP

CCT

1
1.25
1.5
1.75
2

1
1.25
1.5
1.75
2

1
1.25
1.5
1.75
2

1
1.25
1.5
1.75
2

1
1.25
1.5
1.75
2

0.035
0.765
0.895
0.97
0.98

0.02
0.745
0.905
0.955
0.99

0.04
0.765
0.9
0.97
0.98

0.065
0.83
0.95
0.985
0.99

0.065
0.84
0.955
0.985
0.99

3

4

5

6

Spatial ID
8

7

9

10

0.045
0.93
0.985
1
1

0.125
0.98
1
1
1

0.04
0.915
0.98
1
1

0.035
0.8
0.93
0.97
0.98

0.035
0.84
0.945
0.98
0.99

0.04
0.815
0.985
1
1

0.03
0.79
0.97
1
1

0.04
0.835
0.98
1
1

0.05
0.87
0.99
1
1

0.05
0.87
0.99
1
1

0.04
0.78
0.92
0.96
0.985

0.04
0.695
0.875
0.95
0.96

0.045
0.79
0.925
0.965
0.985

0.065
0.845
0.97
0.985
1

0.065
0.85
0.97
0.985
1

0.05
0.73
0.89
0.97
0.985

0.025
0.465
0.725
0.87
0.945

0.05
0.765
0.93
0.975
0.985

0.06
0.865
0.975
0.99
0.995

0.06
0.865
0.975
0.99
0.995

0.16
0.99
1
1
1

0.16
0.99
1
1
1

0.155
0.99
1
1
1

0.02
0.885
0.925
0.97
0.97

0.025
0.91
0.955
0.985
0.995

0.095
0.985
1
1
1

0.155
0.99
1
1
1

0.06
0.985
1
1
1

0.035
0.81
0.955
0.975
0.985

0.045
0.855
0.97
0.975
0.99

0.04
0.84
0.96
0.99
0.995

0.035
0.685
0.895
0.985
0.995

0.04
0.84
0.97
0.99
0.995

0.05
0.865
0.985
0.995
0.995

0.05
0.87
0.985
0.995
0.995

0.055
0.83
0.945
0.98
1

0.065
0.85
0.95
0.97
0.99

0.045
0.825
0.95
0.975
0.995

0.05
0.855
0.965
0.99
1

0.05
0.86
0.97
0.99
1

2

0.14
0.99
1
1
1

0.16
0.99
1
1
1

0.125
0.985
1
1
1

0.015
0.83
0.88
0.945
0.97

0.025
0.855
0.915
0.96
0.98

11

0.16
0.99
1
1
1

0.16
0.99
1
1
1

0.16
0.99
1
1
1

0.025
0.935
0.95
0.975
0.98

0.03
0.955
0.96
0.985
0.99

12

13

0.035
0.75
0.9
0.97
0.99

0.02
0.45
0.745
0.895
0.94

0.05
0.785
0.925
0.98
0.995

0.06
0.86
0.98
0.99
1

0.06
0.86
0.98
0.99
1

0.045
0.8
0.975
0.995
0.995

0.025
0.745
0.93
0.995
1

0.05
0.805
0.975
0.995
0.995

0.06
0.875
0.99
0.995
0.995

0.06
0.88
0.99
0.995
0.995

Table 20: Relative frequencies of detecting an outbreak out of 200 simulations for each location
using different methods for different signal-to-noise ratios.

Figure 22 and 23 demonstrate the performance of BOSTON-PUPA across different regions

with/without outbreaks. Since there was no outbreak added in the simulation study when

SNR = 1, the detection probabilities in Figure 24 only stand for false outbreak detection or

type I error. While the detection procedure maintains a controlled false detection rate for

regions 1, 4, 5, 6, 9, 10, 12, and 13, the false detection rates are inflated (greater than 5%

but less than 20%) in the rest of the regions for the classical methods: Fisher’s, Stouffer’s,

and Lancaster’s. The regions with excessive false positives correspond to the ones with the

first five smallest populations in Table 16, which implies that small populations can have

an impact on these classical combined p-value methods. Detection probabilities in Figure

110

---

<!-- PAGE 112 -->

Figure 20: Empirical density plots of BOSTON-PUPA detected outbreak time point where the first
non-zero δs,T +k occurs in county s for different methods with different signal-to-noise ratios (> 1).
The red vertical lines represent the true outbreak time points given in the simulation study, 103,
99, 95, 82, 102, 102, 91, 89, 97, 109, 100, and 87 for each location respectively.

23 can be interpreted as false detection rate before the true outbreak timing and detection

power after the true outbreak. The red lines portray the expected performance of an ideal

detection procedure, which has controlled false detection rates at level α before any outbreaks

happen and enjoys a timely spike-up in detection power when there are any outbreaks. For

different regions and signal-to-noise ratios, HMP and CCT methods have better controlled

false detection rates and provide a more better resemblance of the ideal detection pattern.

Therefore, we recommend HMP or CCT method be implemented in the detection procedure

to handle inflated false detection rates in the regions with smaller populations.

4. Remarks We would also like to make two remarks on our detection framework regarding its

111

---

<!-- PAGE 113 -->

Figure 21: Signal-to-ratio vs Evaluation Metrics for different combined p-value methods: Fisher’s,
Stouffer’s, Lancaster’s, HMP and CCT when P-value Adaptation is implemented.

implementation and property: (1) Correlation matrix calculation for dependent hypotheses

testing; (2) Sequential estimation of the overdispersion parameter λ.

• Correlation matrix calculation. As is pointed out in Cinar and Viechtbauer (2022), the

adjustment for k dependent hypothesis tests the Fisher’s, Stouffer’s, and Lancaster’s

combined p-value methods stems from the scenario where a smaller number (< k) of

independent hypothesis tests are conducted, known as the effective number of tests.

The computation effective number of tests is mainly achieved through PCA of the k × k

correlation matrix Rt for the dependent hypothesis tests, which is based on test statis-

tics t1, t2, . . . , tk under multivariate normality assumption. However, Rt can be consis-

tently approximated by RY under the regularity of the multivariate central limit theorem

(Van der Vaart, 2000; H¨ardle and Simar, 2019), where RY is the k × k correlation matrix

of the observations, Y1, Y2, . . . , Yk even if the observations are not normal. Hence, we

112

---

<!-- PAGE 114 -->

Figure 22: Traceplot of outbreak detection probabilities from day 29 to day 200 across 13 regions.
Five combined p-value methods are compared at the nominal level α = 0.05, represented by the
red dashed horizontal lines.

supplied RYs by calculating the (T0 − T ) × (T0 − T ) correlation matrix of standardized

Ys,t, t = T + 1, T + 2, . . . , T0 for region s with adapted GPD mean and overdispersion

respectively from the simulation study without outbreak added, which was thought to

represent the baseline dependency among the hypothesis tests.

Although it has been shown the GPD model is almost symmetrical in shape, resembling

a normal distribution, when the values of θs,t are as high as 8 and 0 < λ < 0.5 (Con-

sul and Jain, 1973), the dynamic adaptation on the GPD mean and overdispersion can

distort the asymptotic normality of standardized Ys,t and the efficient number of simu-

lations for a good baseline estimation of Rt is yet to be determined. Therefore, we need

to acknowledge from another four aspects the limitation of calculating the correlation

matrix of RY in the BOSTON-PUPA procedure if one uses either adjusted Fisher’s,

Stouffer’s, or Lancaster’s method: (1) The normality assumption for the test statis-

113

---

<!-- PAGE 115 -->

Figure 23: Traceplot of outbreak detection probabilities from day 29 to day 200 across 13 regions.
Five combined p-value methods are compared at the nominal level α = 0.05. The red dashed lines
stand for an ideal detection probability pattern of maintaining at the nominal level before any
outbreaks occur and spiking up promptly to 1 when there are any outbreaks.

tics is compensated by the approximated normality of the GPD model. (2) Estimation

accuracy of RY is dependent on the simulation size, which is not the scope of this disser-

tation. (3) Practical concern. In the simulation study, all the parameters are provided

and fixed beforehand but they will be estimated sequentially in the online detection

procedure, which requires further criteria to select reasonable parameter estimates for a

good baseline representation for RY . (4) The approaches calculating effective numbers

of hypothesis tests are rather ad hoc than principled techniques and should be applied

with caution (Dudbridge and Koeleman, 2004; Salyakina et al., 2005). These limitations

can convince practitioners to adopt the combined p-value methods handling arbitrary

correlation structures such as HMP or CCT method without dependency on Rt.

114

---

<!-- PAGE 116 -->

• Sequential estimation of the overdispersion parameter The decision rule described in Step

4 of the BOSTON-PUPA procedure involves the latent global aberration indicator δξk

to ensure better control of potential false detection caused by data overdispersion. To

illustrate the importance of the global aberration indicator, we also collected from the
simulation study the sequential estimation of ˆλk = e ˆξk /(1 + e ˆξk ) and its adapted version
¯ˆλk := e

¯ˆξk ) in PA technique in Figure 24 and 25.

¯ˆξk /(1 + e

Figure 24: Trajectories of sequential estimation of overdispersion parameter λ without any out-
breaks introduced (SNR =1) in the simulation study. Green lines stand for ˆλk, blue lines stand for
¯ˆλk, and the red line represents the actual value of the overdispersion parameter λ = .4448

Apart from a few numerical outliers in the computation, ˆλk shares common trajectories
¯ˆλk when SNR =1 in Figure 24, which implies that δξk = 1 for most of the time
and agrees with the underlying fact of no outbreak. The aforementioned benefit of the

with

false detection control using the BOSTON-PUPA procedure can be supported by the

pattern of the estimated and adapted λ because small p-values caused by overdispersion

will not lead to an outbreak claim unless the first occurrence of a global aberration in

115

---

<!-- PAGE 117 -->

Figure 25: Trajectories of sequential estimation of overdispersion parameter λ with different SNRs
¯ˆλk, and the red line represents
in the simulation study. Green lines stand for ˆλk, blue lines stand for
the actual value of the overdispersion parameter λ = .4448. The two black vertical dashed lines
stand for τ4 = 82 and τ11 + T = 109 + 28 = 137 accordingly.

the process. Therefore, such a setup in the decision rule guarantees a long monitoring

horizon where the false detection rate is controlled before any true outbreaks occur. In

Figure 25, there are humps in the trajectories of ˆλk for different SNRs, starting at around

the earliest outbreak day (τ4 = 82) in the simulation study, which indicates that at least

one of the regions is experiencing abnormally large confirmed case counts and triggers

a global aberration alarm for any subsequent outbreak detection for the regions at risk.

When the green trajectories deviate from the blue, region-specific Bayesian p-values get

boosted significance from adaptations for both the abnormal overdispersion and GPD

means.

The U-shape pattern of ˆλ implies another property of modeling a mixture of GPD data

116

---

<!-- PAGE 118 -->

with identical λ but different θ in the sliding window. The humps in Figure 25 die down

at around the day τ11 + T = 137, where τ11 = 109 is the last outbreak onset day in the

simulation study. Empirically, it can be observed that the overdispersion parameter (1)

is estimated consistently around its true value when the sliding window only contains

non-outbreak data. (2) is overestimated when the sliding window contains a mixture of

non-outbreak and outbreak data even though they are generated by identical λ, which

provides helpful information for outbreak detection. (3) returns to a consistent estimate

slightly larger than the true value when the sliding window contains only the outbreak

data. Such property can be further investigated with theoretical evidence but it won’t

be discussed in this dissertation.

4.4.2 Real application

For the real application part, we will implement the BOSTON-PUPA procedure for COVID-19

daily case count data in Massachusetts with HMP and CCT methods for p-value combination.

Firstly, we will conduct empirical data analysis to assert the validity of using a spatio-temporal

model framework. Secondly, we implement the BOSTON-PUPA procedure to real data and report

the detected outbreaks for each county.

4.4.2.1 COVID-19 Data description The daily COVID-19 confirmed case count data is

available in the COVID-19 Dashboard Data Repository created by the Center for Systems Science

and Engineering (CSSE) at Johns Hopkins University (Dong et al., 2020).

In the evolution of

the pandemic, the frequency of the case count report has shifted from a daily basis to a weekly

basis. We focus on the daily case count data for the different counties in Massachusetts. To avoid

excessive zero daily counts, we combine the two adjacent island counties, Dukes and Nantucket

into one. The period of raw data we chose is between June 15th, 2020, and Dec 31st, 2020, with

only missing values on two days, Nov 31st (Thanksgiving) and Dec 25th (Christmas), while the

daily case counts on the following days Nov 27th and Dec 26th are nearly twice as usual. The total

number of days in our study will be T = 200 from summer to the end of the year 2020. Let Ys,t
denote the daily case count of county s on day t. Our imputation for the missing values ˆYs,t1 and

117

---

<!-- PAGE 119 -->

ˆYs,t2 and data adjustment are as follows 2:




ˆYs,t1 = ⌊Ys,t1+1/2⌉

; ˆYs,t1+1 = ⌊Ys,t1+1/2⌉



ˆYs,t2 = ⌊Ys,t2+1/2⌉

; ˆYs,t2+1 = ⌊Ys,t2+1/2⌉

Figure 26 presents the evolution of daily confirmed case counts. Across all the regions, the

daily count data have remained roughly stable or a slightly positive time trend on the mean level

throughout the summer months from June to Sept until spikes happen around some time points

in the fall. The positive time trend could be explained by the fluctuation of temperature, which is

negatively associated with the COVID-19 mortality rate (Quilodran et al., 2021).

Figure 26: COVID-19 daily case count in different counties in Massachusetts from the dashboard

The spatio-temporal pattern of the count data can be verified through empirical data analysis.

For the areal type of spatial data, there are two standard statistics to measure the spatial correlation,

Moran’s I and Geary’s C (Banerjee et al., 2003) which take the forms as shown in equations (2.1)

and (2.2) respectively,

2⌊·⌉ denotes rounding to the nearest integer.

118

---

<!-- PAGE 120 -->

I =

while Geary’s C takes the form,

n (cid:80)
(cid:80)
i
(cid:16)(cid:80)

j wij(Yi − ¯Y )(Yj − ¯Y )
i̸=j wij

i(Yi − ¯Y )

(cid:17) (cid:80)

,

(4.14)

C =

(cid:80)

(n − 1) (cid:80)
i
(cid:16)(cid:80)

2

i̸=j wij

j wij(Yi − Yj)2
(cid:17) (cid:80)
i(Yi − ¯Y )2

,

(4.15)

where wij are the entries of the adjacency matrix W . We computed Moran’s I and Geary’s C as well

as their p-values throughout all 200 days using moran.test() and geary.test() from the spdep package

in R. Figure 27 shows that among the spatial data from 200 days, 95% of Moran’s statistics and

92.5% of Geary’s statistics have a p-value less than the default significance level 0.05. Therefore,

it is reasonable to account for the spatial association among the count data in a statistical model.

Figure 27: P-values of Moran’s I and Geary’s C at every time stamp. The red dashed line represents
the significance level of 0.05.

Figure 28 shows the estimates of the Autocorrelation Function (ACF) and Partial Autocorrela-

tion Function (PACF) across different regions. The red dashed line represents the 95% boundaries

for the correlation functions. Based on the sample estimates, both types of correlation functions

indicate a significant temporal dependence in the case data. Therefore, The temporal dependence

119

---

<!-- PAGE 121 -->

among lagged data is also important to be incorporated for the multivariate time series data.

Figure 28: ACF and PACF estimates for different counties in Massachusetts. Spatial IDs 1∼13
correspond to the following counties in order: Plymouth, Berkshire, Barnstable, Norfolk, Bristol,
Suffolk, Franklin, Hampshire, Essex, Hampden, Dukes and Nantucket, Middlesex, and Worcester.
The red dashed lines represent the boundaries of a 95% confidence interval for ACF and PACF.

4.4.2.2

Implementation of BOSTON-PUPA For the implementation of BOSTON-PUPA

on the real data, we adopted the findings from the simulation study by choosing the sliding window

size T = 28 and discounting factor a0 = 0.25. We chose HMP and CCT methods in Step 4 to

compute combined p-values. The first iteration of model fitting starts on 06/15/2020 (Day 1) and

the first binary outbreak detection indicator on 07/13/2020 (Day 29) for all the counties. Figure

29 shows the calculated outbreak detection indicators in (4.11) in the iterative procedure. Table

21 summarizes the earliest outbreak detection days ˆτs for each county. The results are very similar

between HMP and CCT methods except for Suffolk County.

As a reference, the news report of a sharp case count increase was released on 10/22/2020, which

corresponds to τ = 130 in the data. To assess the credibility of ˆτs, we also provided trace plots of

daily case counts with both ˆτs and τ in Figure 30, and the plots were separated by population size

to avoid imbalanced observation scales. In Figure 30, the BOSTON-PUPA procedure detected the

anomalous counts in counties with large populations such as Bristol, Suffolk, Essex, and Middlesex

120

---

<!-- PAGE 122 -->

Figure 29: Calculated outbreak detection indicators δs,T +k using HMP and CCT across all counties
in the BOSTON-PUPA procedure.

Spatial ID County name

HMP

CCT

Earliest detection days

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
11
12
13

Plymouth
Berkshire
Barnstable
Norfolk
Bristol
Suffolk
Franklin
Hampshire
Essex
Hampden
Dukes and Nantucket
Middlesex
Worcester

130
149
82
145
82
82
186
152
97
130
152
109
132

130
149
82
145
82
172
181
152
97
130
147
109
132

Table 21: Earliest detection days across different counties using HMP and CCT method.

several weeks before the day of the reported outbreak with the HMP method, while CCT method

reported another significant spike after τ as the detected outbreak. The anomalous escalation of

case counts in Plymouth, Norfolk, Hampden, and Worcester was captured right at or near the time

of the reported outbreak. As for the counties with small populations, Berkshire, Hampshire, Dukes,

121

---

<!-- PAGE 123 -->

and Nantucket had the detected outbreaks of about 2 ∼ 4 weeks later than τ = 130. Meanwhile,

Barnstable and Franklin had an early and a more delayed detection correspondingly.

4.4.2.3 Remarks There is no ground truth available about the exact outbreak timing even

though a news report may be chosen as a reference for the state-wise declared outbreak. However,

one important takeaway from this real application is that instead of making an outbreak claim

based on the entire state, public health surveillance systems can account for the spatio-temporal

pattern of case count in each county and monitor the online data spatially. From this perspective,

the BOTSON-PUPA procedure enjoys an improvement in the granularity and timeliness of disease

surveillance. A detected outbreak in one of the counties can stimulate further investigation for the

suspicious outbreak pattern before the onset of a real pandemic. This can help public health officials

customize region-specific strategies to combat the pandemic, protect people at risk, and preserve

normal societal functions in the regions which have not been impacted by the disease outbreak from

elsewhere. In addition, we also would like to point out that the BOSTON-PUPA procedure only

handles the anomalous data dynamics from the presumed baseline pattern. Nonetheless, statistical

significance cannot determine the final policy decision if the statistically detected outbreak does

not align with domain knowledge such as epidemiology, public health, etc.

4.5 Summary

In this chapter, we proposed a 4-step online outbreak detection framework, BOSTON-PUPA. This

iterative procedure accounts for spatio-temporal data dependence and overdispersion via a gener-

alized Poisson distribution model. Prior Updating (PU) technique ensures good-quality statistical

inference drawn from a fixed-size sliding window by leveraging historical information. P-value Adap-

tation (PA) technique is able to boost the significance of a true outbreak thus leading to timely on-

line outbreak detection. The global aberration indicator, stemming from the sequential estimation

of the overdispersion, provides reliable outbreak surveillance for all involved locations and facilitates

a strict false detection control locally. Implementation of combined p-values in sequential analysis

enables (1) Better information preservation about outbreak severity than dichotomized detection

strategies solely based on upper boundaries for data prediction. (2) Dependence among individual

p-values, whereas residual-combining approaches are often under the assumption of residuals being

122

---

<!-- PAGE 124 -->

Figure 30: Trace plot of daily COVID-19 case counts in MA, 2020, with detected outbreaks using
BOSTON-PUPA procedure. Red line represents a state-wise outbreak indicator from the news

independent or uncorrelated. As a holistic framework, the BOSTON-PUPA procedure is able to

perform robust outbreak detection of the count data against different signal-to-noise ratios on spa-

tially imbalanced scales. In addition, the inherent computational efficiency of the INLA method

grants practitioners the flexibility to straightforwardly implement the BOSTON-PUPA procedure

for real application and to conduct relevant research via large-scale simulations.

123

---

<!-- PAGE 125 -->

5 Discussion and Future Work

This dissertation contributes new methodological developments in online change point detection

and spatio-temporal analysis. Chapter 2 and 3 focus on the innovative statistical methods with

applications for high-frequency financial market microstructure analysis. E-PEF method from

Chapter 2 aims at robustly detecting structural breaks in financial duration time series with a fixed-

size of training data via a semi-parametric detection algorithm, and detected structural breaks can

inform the practitioners the change of market trading intensity so that corresponding transactional

strategies can be deployed promptly to adjust for an advantageous asset position. BVAR(1)-LCM

Bayesian hierarchical model from Chapter 3 accounts for the association between transaction counts

at different risk levels across multiple assets. The data interdependence on the observational level

can be further elaborated via correlated latent random effects. Specified Gaussian Markov Random

Field with sparsity enables fast parametric inference via INLA method thus leading to scaled-

up analyses for a large number of assets in a single model. By synthesizing relevant techniques

involved in univariate online change point detection and multivariate count time series modeling,

BOSTON-PUPA procedure from Chapter 4 took a further step to deal with spatio-temporal online

outbreak detection problems in public health surveillance. This iterative detection procedure enjoys

fast computational speed with fundamental historical information retaining via Prior Updating

(PU) technique. Meabwhile, streaming surveillance data are monitored by a global and location

aberration indicators with P-value Adaptation (PA) technique, which enforces a satisfactory false

detection control and provide timeliness and granularity for the powerful disease surveillance over

multiple geographically related locations even if there is a data imbalance issue with the count

observations.

As future work based on the three proposed frameworks, three potential directions are worth

extended research attention.

• First, as a univariate online structural break detection procedure, the E-PEF method is

able to achieve a single structural break detection given a fixed amount of training data.

However, in the volatile high-frequency financial market, a fixed amount of data doesn’t

provide a sustainable representation of the baseline pattern for change point detection thus the

monitoring horizon is limited and monitoring longer time series requires updates of training

124

---

<!-- PAGE 126 -->

data.

In order to develop a multiple structural break detection framework, one needs to

study the monitoring horizon of the E-PEF method to ensure a controlled false detection rate

in a monitoring window of reasonable length. Subsequently, a clock resetting regimen can

be introduced to recursively update the latest training data to capture the recent baseline

pattern when (1) The incoming observations are beyond the monitoring horizon, or (2) A

structural break is detected within the monitoring horizon.

• Second, BOSTON-PUPA procedure involves a sliding window as a baseline pattern without

the concern about monitoring horizon for online outbreak detection, but for its multiple

change point detection, a resetting rule is also very helpful because of the findings of the

sequential estimation for the overdispersion parameter for generalized Poisson distribution.

The sequential estimation of the overdispersion is stationary when the sliding window contains

only non-epidemic or epidemic data, so that changes over the trajectory of the overdispersion

parameter estimates can be good indicators when the procedure enters a transition stage

between two phases. Therefore, the resetting rule can be placed over the baseline behavior of

the sequential overdispersion estimation when the estimate begins to deviate from its baseline

pattern. With appropriately specified p-value calculation, BOSTON-PUPA procedure with

a resetting rule will have promising performance to detect not only the onset of a pandemic

but also its sign of ending.

• Third, BVAR(1)-LCM framework is involved in financial application but the main idea is

based on the correct specification of precision matrix for the random effects with convoluted

association and numerous future research can be considered when an innovative data inter-

dependent structure is developed. By taking advantage of computational efficiency, one can

use the INLA method to make high-quality inference on the parameters and latent effects

from sparse Gaussian Markov Random Field as long as their precision matrix is reasonably

formulated. For example, the spatio-temporal framework in BOSTON-PUPA involve naive

separable spatial and temporal effects also with a symmetric adjacency matrix establishing

an equal influence between two neighboring regions. To demonstrate and model more com-

plex space and time association, one can consider a non-separable spatio-temporal effects

as in (Zou et al., 2012) and an asymmetrically weighted spatial-dependence matrix as in a

125

---

<!-- PAGE 127 -->

Simultaneous Auto-regressive (SAR) model in (Arab et al., 2008).

References

C. C. Aggarwal. An introduction to outlier analysis. In Outlier Analysis, pages 1–34. Springer,

2017.

J. Aitchison and C. Ho. The multivariate Poisson-log normal distribution. Biometrika, 76(4):

643–653, 1989.

T. Aktekin, N. Polson, and R. Soyer. Sequential Bayesian analysis of multivariate count data.

Bayesian Analysis, 13(2):385–409, 2018.

M. A. Al-Osh and A. A. Alzaid. First-order integer-valued autoregressive (INAR (1)) process.

Journal of Time Series Analysis, 8(3):261–275, 1987.

D. Allen, F. Chan, M. McAleer, and S. Peiris. Finite sample properties of the QMLE for the

Log-ACD model: application to Australian stocks. Journal of Econometrics, 147(1):163–185,

2008.

A. Alzaid and M. Al-Osh. First-order integer-valued autoregressive (INAR (1)) process: distribu-

tional and regression properties. Statistica Neerlandica, 42(1):53–61, 1988.

I. B. Ammar, S. Hellara, and I. Ghadhab. High-frequency trading and stock liquidity: An intraday

analysis. Research in International Business and Finance, 53:101235, 2020.

C. Anderson, D. Lee, and N. Dean. Spatial clustering of average risks and risk trends in bayesian

disease mapping. Biometrical Journal, 59(1):41–56, 2017.

A. Arab, M. B. Hooten, and C. K. Wikle. Hierarchical spatial models. Encyclopedia of GIS, 14(1):

425–431, 2008.

A. Aue, S. H¨ormann, L. Horv´ath, and M. Reimherr. Break detection in the covariance structure

of multivariate time series models. The Annals of Statistics, 37(6B):4046–4087, 2009.

J. Bai. Likelihood ratio tests for multiple structural changes. Journal of Econometrics, 91(2):

299–323, 1999.

126

---

<!-- PAGE 128 -->

A. Banerjee and G. Urga. Modelling structural breaks, long memory and stock market volatility:

an overview. Journal of Econometrics, 129(1-2):1–34, 2005.

S. Banerjee, B. P. Carlin, and A. E. Gelfand. Hierarchical modeling and analysis for spatial data.

Chapman and Hall/CRC, 2003.

M. Baron, J. Brogaard, B. Hagstr¨omer, and A. Kirilenko. Risk and return in high-frequency trading.

Journal of Financial and Quantitative Analysis, 54(3):993–1024, 2019.

L. Bauwens and P. Giot. The logarithmic ACD model: an application to the bid-ask quote process

of three nyse stocks. Annales d’Economie et de Statistique, pages 117–149, 2000.

L. Bauwens and D. Veredas. The stochastic conditional duration model: a latent variable model

for the analysis of financial durations. Journal of Econometrics, 119(2):381–412, 2004.

B. Bedowska-S´ojka and A. Kliber. The causality between liquidity and volatility in the polish stock

market. Finance Research Letters, 30:110–115, 2019.

A. Benveniste, M. Basseville, and G. Moustakides. The asymptotic local approach to change

detection and model validation. IEEE Transactions on Automatic Control, 32(7):583–592, 1987.

A. Benveniste, M. M´etivier, and P. Priouret. Adaptive Algorithms and Stochastic Approximations,

volume 22. Springer Science & Business Media, 2012.

M. Beraha, D. Falco, and A. Guglielmi. JAGS, NIMBLE, Stan: a detailed comparison among

bayesian mcmc software. arXiv preprint arXiv:2107.09357, 2021.

I. Berkes, E. Gombay, L. Horv´ath, and P. Kokoszka. Sequential change-point detection in GARCH

(p, q) models. Econometric Theory, 20(6):1140–1167, 2004.

J. Besag. Spatial interaction and the statistical analysis of lattice systems. Journal of the Royal

Statistical Society: Series B (Methodological), 36(2):192–225, 1974.

J. Besag, J. York, and A. Molli´e. Bayesian image restoration, with two applications in spatial

statistics. Annals of the Institute of Statistical Mathematics, 43(1):1–20, 1991.

127

---

<!-- PAGE 129 -->

D. M. Blei, A. Kucukelbir, and J. D. McAuliffe. Variational inference: A review for statisticians.

Journal of the American Statistical Association, 112(518):859–877, 2017. doi: 10.1080/01621459.

2017.1285773.

G. E. Box, G. M. Jenkins, G. C. Reinsel, and G. M. Ljung. Time Series Analysis: Forecasting and

Control. John Wiley & Sons, 2015.

J. Brogaard, A. Carrion, T. Moyaert, R. Riordan, A. Shkilko, and K. Sokolov. High frequency

trading and extreme price movements. Journal of Financial Economics, 128(2):253–265, 2018.

M. B. Brown. 400: A method for combining non-independent, one-sided tests of significance.

Biometrics, pages 987–992, 1975.

P. B¨uhlmann. Bootstraps for time series. Statistical Science, pages 52–72, 2002.

H. S. Burkom, S. P. Murphy, and G. Shmueli. Automated time series forecasting for biosurveillance.

Statistics in Medicine, 26(22):4202–4218, 2007.

A. Carrion. Very fast money: High-frequency trading on the NASDAQ. Journal of Financial

Markets, 16(4):680–711, 2013.

J. M. Cheverud. A simple correction for multiple comparisons in interval mapping genome scans.

Heredity, 87(1):52–58, 2001.

C.-S. J. Chu, M. Stinchcombe, and H. White. Monitoring structural change. Econometrica: Journal

of the Econometric Society, pages 1045–1065, 1996.

O. Cinar and W. Viechtbauer. The poolr package for combining independent and dependent p

values. Journal of Statistical Software, 101:1–42, 2022.

D. Conesa, M. Mart´ınez-Beneito, R. Amor´os, and A. L´opez-Qu´ılez. Bayesian hierarchical pois-

son models with a hidden markov structure for the detection of influenza epidemic outbreaks.

Statistical Methods in Medical Research, 24(2):206–223, 2015.

P. C. Consul and G. C. Jain. A generalization of the poisson distribution. Technometrics, 15(4):

791–799, 1973.

128

---

<!-- PAGE 130 -->

G. F. Cooper, R. Villamarin, F.-C. R. Tsui, N. Millett, J. U. Espino, and M. M. Wagner. A method

for detecting and characterizing outbreaks of infectious disease from clinical reports. Journal of

Biomedical Informatics, 53:15–26, 2015.

S. S. Coughlin, A. Yiˇgiter, H. Xu, A. E. Berman, and J. Chen. Early detection of change patterns

in COVID-19 incidence and the implementation of public health policies: A multi-national study.

Public Health in Practice, 2:100064, 2021.

R. Deo, M. Hsieh, and C. M. Hurvich. Long memory in intertrade durations, counts and realized

volatility of nyse stocks. Journal of Statistical Planning and Inference, 140(12):3715–3733, 2010.

P. Deuskar. Extrapolative expectations: Implications for volatility and liquidity.

In AFA 2007

Chicago Meetings Paper, 2006.

P. Diggle, L. Knorr-Held, B. Rowlingson, T. L. Su, P. Hawtin, and T. N. Bryant. On-line monitoring

of public health surveillance data. In Monitoring the health of populations: Statistical principles

and methods for public health surveillance. Oxford University Press, 2009.

E. Dong, H. Du, and L. Gardner. An interactive web-based dashboard to track covid-19 in real

time. The Lancet Infectious Diseases, 20(5):533–534, 2020.

M. D¨oring. Convergence in distribution of multiple change point estimators. Journal of Statistical

Planning and Inference, 141(7):2238–2248, 2011.

F. Dudbridge and B. P. Koeleman. Efficient computation of significance levels for multiple associa-

tions in large studies of correlated data, including genomewide association studies. The American

Journal of Human Genetics, 75(3):424–435, 2004.

C. Dutta, K. Karpman, S. Basu, and N. Ravishanker. Review of statistical approaches for modeling

high-frequency trading data. Sankhya B, pages 1–48, 2022.

D. Easley and M. O’hara. Time and the process of security price adjustment. The Journal of

Finance, 47(2):577–605, 1992.

B. Efron. Double exponential families and their use in generalized linear regression. Journal of the

American Statistical Association, 81(395):709–721, 1986.

129

---

<!-- PAGE 131 -->

R. F. Engle. The econometrics of ultra-high-frequency data. Econometrica, 68(1):1–22, 2000.

R. F. Engle and J. R. Russell. Forecasting the frequency of changes in quoted foreign exchange

prices with the autoregressive conditional duration model. Journal of Empirical Finance, 4(2-3):

187–212, 1997.

R. F. Engle and J. R. Russell. Autoregressive conditional duration: a new model for irregularly

spaced transaction data. Econometrica, pages 1127–1162, 1998.

J. Fan and R. Li. Variable selection via nonconcave penalized likelihood and its oracle properties.

Journal of the American Statistical Association, 96(456):1348–1360, 2001.

C. Farrington, N. J. Andrews, A. Beale, and M. Catchpole. A statistical algorithm for the early

detection of outbreaks of infectious disease. Journal of the Royal Statistical Society: Series A

(Statistics in Society), 159(3):547–563, 1996.

P. Farrington and N. Andrews. Application to infectious. Monitoring the Health of Populations:

Statistical Principles and Methods for Public Health Surveillance, page 203, 2003.

R. Ferland, A. Latour, and D. Oraichi. Integer-valued GARCH process. Journal of Time Series

Analysis, 27(6):923–942, 2006.

M. Fernandes and J. Grammig. A family of autoregressive conditional duration models. Journal

of Econometrics, 130(1):1–23, 2006.

R. Fisher. Statistical methods for research workers (london: Oliver and boyd). Legends to Figures,

1932.

N. W. Galwey. A new measure of the effective number of tests, a practical tool for comparing

families of non-independent significance tests. Genetic Epidemiology: The Official Publication of

the International Genetic Epidemiology Society, 33(7):559–568, 2009.

D. Gamerman, T. R. dos Santos, and G. C. Franco. A non-Gaussian family of state-space models

with exact marginal likelihood. Journal of Time Series Analysis, 34(6):625–645, 2013.

130

---

<!-- PAGE 132 -->

X. Gao, J. Starmer, and E. R. Martin. A multiple testing correction method for genetic association

studies using correlated single nucleotide polymorphisms. Genetic Epidemiology: The Official

Publication of the International Genetic Epidemiology Society, 32(4):361–369, 2008.

A. E. Gelfand and P. Vounatsou. Proper multivariate conditional autoregressive models for spatial

data analysis. Biostatistics, 4(1):11–15, 2003.

A. Gelman, J. Hwang, and A. Vehtari. Understanding predictive information criteria for Bayesian

models. Statistics and Computing, 24(6):997–1016, 2014.

V. G´omez-Rubio. Bayesian Inference with INLA. CRC Press, 2020.

P. Good. Permutation tests: a practical guide to resampling methods for testing hypotheses. Springer

Science & Business Media, 2013.

J. Grammig and M. Wellner. Modeling the interdependence of volatility and inter-transaction

duration processes. Journal of Econometrics, 106(2):369–400, 2002.

G. Guan, Y. Dery, M. Yechezkel, I. Ben-Gal, D. Yamin, and M. L. Brandeau. Early detection of

covid-19 outbreaks using human mobility data. PloS one, 16(7):e0253865, 2021.

A. C. Hale, F. S´anchez-Vizca´ıno, B. Rowlingson, A. D. Radford, E. Giorgi, S. J. O’Brien, and P. J.

Diggle. A real-time spatio-temporal syndromic surveillance system with application to small

companion animals. Scientific reports, 9(1):1–14, 2019.

W. K. H¨ardle and L. Simar. Applied Multivariate Statistical Analysis. Springer Nature, 2019.

J. Hasbrouck and G. Saar. Low-latency trading. Journal of Financial Markets, 16(4):646–679,

2013.

S. He, Z. He, and G. A. Wang. CUSUM control charts for multivariate Poisson distribution.

Communications in Statistics-Theory and Methods, 43(6):1192–1208, 2014.

M. J. Heaton, D. L. Banks, J. Zou, A. F. Karr, G. Datta, J. Lynch, and F. Vera. A spatio-temporal

absorbing state model for disease and syndromic surveillance. Statistics in Medicine, 31(19):

2123–2136, 2012.

131

---

<!-- PAGE 133 -->

A. Heinen. Modelling time series count data: an autoregressive conditional Poisson model. Available

at SSRN 1117187, 2003.

T. Hendershott and R. Riordan. Algorithmic trading and the market for liquidity. Journal of

Financial and Quantitative Analysis, 48(4):1001–1024, 2013.

C. C. Heyde. Quasi-likelihood and its application: a general approach to optimal parameter esti-

mation. Springer, 1997.

L. Horv´ath and G. Rice. Extensions of some classical methods in change point analysis. Test, 23

(2):219–255, 2014.

H. E. Hughes, O. Edeghere, S. J. O’Brien, R. Vivancos, and A. J. Elliot. Emergency department

syndromic surveillance systems: a systematic review. BMC Public Health, 20(1):1–15, 2020.

M. Huˇskov´a, Z. Pr´aˇskov´a, and J. Steinebach. On the detection of changes in autoregressive time

series i. asymptotics. Journal of Statistical Planning and Inference, 137(4):1243–1259, 2007.

P. A. Jacobs and P. A. Lewis. Stationary discrete autoregressive-moving average time series gen-

erated by mixtures. Journal of Time Series Analysis, 4(1):19–36, 1983.

J. Jasiak. Persistence in intertrade durations. In Finance, 1999.

X. Jin, B. P. Carlin, and S. Banerjee. Generalized hierarchical multivariate car models for areal

data. Biometrics, 61(4):950–961, 2005.

P. Johnson, J. Moriarty, and G. Peskir. Detecting changes in real-time data: a user’s guide to

optimal detection. Philosophical Transactions of the Royal Society A: Mathematical, Physical

and Engineering Sciences, 375(2100):20160298, 2017.

R. C. Jung, R. Liesenfeld, and J.-F. Richard. Dynamic factor models for multivariate count data:

An application to stock-market trading activity. Journal of Business & Economic Statistics, 29

(1):73–85, 2011.

D. Karlis and L. Meligkotsidou. Multivariate Poisson regression with covariance structure. Statistics

and Computing, 15(4):255–265, 2005.

132

---

<!-- PAGE 134 -->

D. Karlis and L. Meligkotsidou. Finite mixtures of multivariate Poisson distributions with appli-

cation. Journal of Statistical Planning and Inference, 137(6):1942–1960, 2007.

J. T. Kost and M. P. McDermott. Combining dependent p-values. Statistics & Probability Letters,

60(2):183–190, 2002.

M. Kulldorff. A spatial scan statistic. Communications in Statistics-Theory and methods, 26(6):

1481–1496, 1997.

T. L. Lai and J. Z. Shan. Efficient recursive algorithms for detection of abrupt changes in signals

and control systems. IEEE Transactions on Automatic Control, 44(5):952–966, 1999.

H. Lancaster. The combination of probabilities: an application of orthonormal functions. Australian

Journal of Statistics, 3(1):20–33, 1961.

I. Lavine, A. Cron, and M. West. Bayesian computation in dynamic latent factor models. arXiv

preprint arXiv:2007.04956, 2020.

J. Li and L. Ji. Adjusting multiple testing in multilocus analyses using the eigenvalues of a corre-

lation matrix. Heredity, 95(3):221–227, 2005.

L. Li, K.-L. Tsui, and Y. Zhao. An overview and general framework for spatiotemporal modeling

and applications in transportation and public health. Artificial Intelligence, Big Data and Data

Science in Statistics, pages 195–226, 2022a.

M. Li, S. Ma, and Z. Liu. A novel method to detect the early warning signal of COVID-19

transmission. BMC Infectious Diseases, 22(1):1–12, 2022b.

Y. Liang, A. Thavaneswaran, and B. Abraham. Joint estimation using quadratic estimating func-

tion. Journal of Probability and Statistics, 2011, 2011.

R. Liesenfeld, I. Nolte, and W. Pohlmeier. Modelling financial transaction price movements: a

dynamic integer count data model. Empirical Economics, 30(4):795–825, 2006.

Y. Liu and J. Xie. Cauchy combination test: a powerful test with analytic p-value calculation

under arbitrary dependency structures. Journal of the American Statistical Association, 115

(529):393–402, 2020.

133

---

<!-- PAGE 135 -->

J. Ma, K. M. Kockelman, and P. Damien. A multivariate Poisson-lognormal regression model for

prediction of crash counts by severity, using Bayesian methods. Accident Analysis & Prevention,

40(3):964–975, 2008.

J. Manitz and M. H¨ohle. Bayesian outbreak detection algorithm for monitoring reported cases of

campylobacteriosis in germany. Biometrical Journal, 55(4):509–526, 2013.

M. A. Mart´ınez-Beneito, D. Conesa, A. L´opez-Qu´ılez, and A. L´opez-Maside. Bayesian markov

switching models for the early detection of influenza epidemics. Statistics in Medicine, 27(22):

4455–4468, 2008.

C. Mikl´os and H. Lajos. Limit theorems in change-point analysis. John Wiley and Sons, 1997.

D. C. Montgomery. Introduction to statistical quality control. John Wiley & Sons, 2020.

D. B. Neill. Fast Bayesian scan statistics for multivariate event detection and visualization. Statistics

in Medicine, 30(5):455–469, 2011.

D. R. Nyholt. A simple correction for multiple testing for single-nucleotide polymorphisms in linkage

disequilibrium with each other. The American Journal of Human Genetics, 74(4):765–769, 2004.

M. O’hara. Market microstructure theory. John Wiley & Sons, 1998.

M. Pacurar. Autoregressive conditional duration models in finance: a survey of the theoretical and

empirical literature. Journal of Economic Surveys, 22(4):711–751, 2008.

E. Page. A test for a change in a parameter occurring at an unknown point. Biometrika, 42(3/4):

523–527, 1955.

E. S. Page. Continuous inspection schemes. Biometrika, 41(1/2):100–115, 1954.

E. S. Park and D. Lord. Multivariate Poisson-lognormal models for jointly modeling crash frequency

by severity. Transportation Research Record, 2019(1):1–6, 2007.

X. Pedeli and D. Karlis. On estimation of the bivariate Poisson INAR process. Communications

in Statistics-Simulation and Computation, 42(3):514–533, 2013.

134

---

<!-- PAGE 136 -->

D. N. Politis. The impact of bootstrap methods on time series analysis. Statistical Science, pages

219–230, 2003.

D. N. Politis and J. P. Romano. The stationary bootstrap. Journal of the American Statistical

Association, 89(428):1303–1313, 1994.

C. S. Quilodran, M. Currat, and J. I. Montoya-Burgos. Air temperature influences early covid-19

outbreak as indicated by worldwide mortality. Science of The Total Environment, 792:148312,

2021.

A. S. Quoreshi. A bivariate integer-valued long-memory model for high-frequency financial count

data. Communications in Statistics-Theory and Methods, 46(3):1080–1089, 2017.

S. T. Radev, F. Graw, S. Chen, N. T. Mutters, V. M. Eichel, T. B¨arnighausen, and U. K¨othe.

Outbreakflow: Model-based Bayesian inference of disease outbreak dynamics with invertible

neural networks and its application to the COVID-19 pandemics in germany. PLoS Computational

Biology, 17(10):e1009472, 2021.

B. Raman, N. Ravishanker, R. Soyer, V. Gorti, and K. Sen. Dynamic Bayesian modeling of multiple

count time series using R-INLA. Journal of the Indian Statistical Association, 58(2):137–173,

2020.

N. Ravishanker, V. Serhiyenko, and M. R. Willig. Hierarchical dynamic models for multivariate

times series of counts. Statistics and its Interface, 7(4):559–570, 2014.

A. Riebler and L. Held. Projecting the future burden of cancer: Bayesian age–period–cohort analysis

with integrated nested Laplace approximations. Biometrical Journal, 59(3):531–549, 2017.

M. W. Robbins, C. M. Gallagher, and R. B. Lund. A general regression changepoint test for time

series data. Journal of the American Statistical Association, 111(514):670–683, 2016.

G. Rossi, L. Lampugnani, and M. Marchi. An approximate cusum procedure for surveillance of

health events. Statistics in Medicine, 18(16):2111–2122, 1999.

H. Rue and L. Held. Gaussian Markov random fields:

theory and applications. Chapman and

Hall/CRC, 2005.

135

---

<!-- PAGE 137 -->

H. Rue, S. Martino, and N. Chopin. Approximate Bayesian inference for latent Gaussian models by

using integrated nested Laplace approximations. Journal of the Royal Statistical Society: Series

B (Statistical Methodology), 71(2):319–392, 2009.

H. Rue, A. Riebler, S. H. Sørbye, J. B. Illian, D. P. Simpson, and F. K. Lindgren. Bayesian

computing with INLA: a review. Annual Review of Statistics and Its Application, 4:395–421,

2017.

R. Ruiz-C´ardenas, E. T. Krainski, and H. Rue. Direct fitting of dynamic models using integrated

nested Laplace approximations—INLA. Computational Statistics & Data Analysis, 56(6):1808–

1828, 2012.

D. Sadykova, B. E. Scott, M. De Dominicis, S. L. Wakelin, A. Sadykov, and J. Wolf. Bayesian

joint models with INLA exploring marine mobile predator–prey and competitor species habitat

overlap. Ecology and Evolution, 7(14):5212–5226, 2017.

M. Salmon, D. Schumacher, K. Stark, and M. H¨ohle. Bayesian outbreak detection in the presence

of reporting delays. Biometrical Journal, 57(6):1051–1067, 2015.

D. Salyakina, S. R. Seaman, B. L. Browning, F. Dudbridge, and B. M¨uller-Myhsok. Evaluation of

nyholt’s procedure for multiple testing correction. Human Heredity, 60(1):19–25, 2005.

M. Saqib. Forecasting covid-19 outbreak progression using hybrid polynomial-bayesian ridge re-

gression model. Applied Intelligence, 51(5):2703–2713, 2021.

B. Schr¨odle and L. Held. Spatio-temporal disease mapping using INLA. Environmetrics, 22(6):

725–734, 2011.

R. E. Serfling. Methods for current statistical analysis of excess pneumonia-influenza deaths. Public

Health Reports, 78(6):494, 1963.

V. Serhiyenko, N. Ravishanker, and R. Venkatesan. Multi-stage multivariate modeling of temporal

patterns in prescription counts for competing drugs in a therapeutic category. Applied Stochastic

Models in Business and Industry, 34(1):61–78, 2018.

W. A. Shewhart. Control of quality of manufactured product. 1929.

136

---

<!-- PAGE 138 -->

H. Shore. General control charts for variables. International Journal of Production Research, 38

(8):1875–1897, 2000.

R. Soyer and D. Zhang. Bayesian modeling of multivariate time series of counts. Wiley Interdisci-

plinary Reviews: Computational Statistics, page e1559, 2021.

S. A. Stouffer, E. A. Suchman, L. C. DeVinney, S. A. Star, and R. M. Williams Jr. The American

soldier: Adjustment during army life.(studies in social psychology in World War II), vol. 1. 1949.

A. Thavaneswaran, N. Ravishanker, and Y. Liang. Generalized duration models and optimal

estimation using estimating functions. Annals of the Institute of Statistical Mathematics, 67(1):

129–156, 2015.

K.-L. Tsui, W. Chiu, P. Gierlich, D. Goldsman, X. Liu, and T. Maschek. A review of healthcare,

public health, and syndromic surveillance. Quality Engineering, 20(4):435–450, 2008.

A. W. Van der Vaart. Asymptotic statistics, volume 3. Cambridge University Press, 2000.

A. Wald. Foundations of a general theory of sequential decision functions. Econometrica, Journal

of the Econometric Society, pages 279–313, 1947.

Y. Wang and J. Zou. Volatility analysis in high-frequency financial data. Wiley Interdisciplinary

Reviews: Computational Statistics, 6(6):393–404, 2014.

S. Watanabe. Asymptotic equivalence of Bayes cross validation and widely applicable information

criterion in singular learning theory. Journal of Machine Learning Research, 11:3571–3594, 2010.

R. E. Watkins, S. Eagleson, B. Veenendaal, G. Wright, and A. J. Plant. Disease surveillance using

a hidden markov model. BMC Medical Informatics and Decision Making, 9(1):1–12, 2009.

M. West. Bayesian forecasting of multivariate time series: scalability, structure uncertainty and

decisions. Annals of the Institute of Statistical Mathematics, 72(1):1–31, 2020.

M. West, P. J. Harrison, and H. S. Migon. Dynamic generalized linear models and Bayesian

forecasting. Journal of the American Statistical Association, 80(389):73–83, 1985.

P. H. Westfall and S. S. Young. Resampling-based multiple testing: Examples and methods for

p-value adjustment, volume 279. John Wiley & Sons, 1993.

137

---

<!-- PAGE 139 -->

A. Willsky and H. Jones. A generalized likelihood ratio approach to the detection and estimation

of jumps in linear systems. IEEE Transactions on Automatic Control, 21(1):108–112, 1976.

D. J. Wilson. The harmonic mean p-value for combining dependent tests. Proceedings of the

National Academy of Sciences, 116(4):1195–1200, 2019.

P. R. Winters. Forecasting sales by exponentially weighted moving averages. Management Science,

6(3):324–342, 1960.

L. Xie, S. Zou, Y. Xie, and V. V. Veeravalli. Sequential (quickest) change detection: Classical results

and new directions. IEEE Journal on Selected Areas in Information Theory, 2(2):494–514, 2021.

J. Xing, H. Burkom, and J. Tokars. Method selection and adaptation for distributed monitoring

of infectious diseases for syndromic surveillance. Journal of Biomedical Informatics, 44(6):1093–

1101, 2011.

J. J. Yang, J. Li, L. K. Williams, and A. Buu. An efficient genome-wide association test for

multivariate phenotypes based on the fisher combination function. BMC Bioinformatics, 17:

1–11, 2016.

M. Yuan, N. Boston-Fisher, Y. Luo, A. Verma, and D. L. Buckeridge. A systematic review of aber-

ration detection algorithms used in public health surveillance. Journal of Biomedical Informatics,

94:103181, 2019.

M. Y. Zhang, J. R. Russell, and R. S. Tsay. A nonlinear autoregressive conditional duration model

with applications to financial transaction data. Journal of Econometrics, 104(1):179–207, 2001.

Y. Zhang, N. Ravishanker, and J. Zou. Structural break detection in financial durations. Applied

Stochastic Models in Business and Industry, 34(6):992–1006, 2018.

Y. Zhang, J. Zou, N. Ravishanker, and A. Thavaneswaran. Modeling financial durations using

penalized estimating functions. Computational Statistics & Data Analysis, 131:145–158, 2019.

Y. Zheng, Y. Li, and G. Li. On fr´echet autoregressive conditional duration models. Journal of

Statistical Planning and Inference, 175:51–66, 2016.

138

---

<!-- PAGE 140 -->

J. Zou, A. F. Karr, D. Banks, M. J. Heaton, G. Datta, J. Lynch, and F. Vera. Bayesian methodology

for the analysis of spatial–temporal surveillance data. Statistical Analysis and Data Mining: The

ASA Data Science Journal, 5(3):194–204, 2012.

J. Zou, A. F. Karr, G. Datta, J. Lynch, and S. Grannis. A Bayesian spatio–temporal approach for

real–time detection of disease outbreaks: a case study. BMC Medical Informatics and Decision

Making, 14(1):1–18, 2014.

J. Zou, Y. An, and H. Yan. Volatility matrix inference in high-frequency finance with regularization

and efficient computations. In 2015 IEEE International Conference on Big Data (Big Data),

pages 2437–2444. IEEE, 2015.

J. Zou, Z. Zhang, and H. Yan. A hybrid hierarchical bayesian model for spatiotemporal surveillance

data. Statistics in Medicine, 37(28):4216–4233, 2018.

139

---

<!-- PAGE 141 -->

6 Appendix

6.1 Derivation of conditional correlation

For a BVAR(1)-LCM model, we have

Yj,st|λj,st

ind∼ P ois(λj,st),

ηj,st = log λj,st = ZZZjβββj + γj,t + αj,st,

γj,t = ϕjγj,t−1 + ωj,t,









ωωωt =




ω1,t

ω2,t


 ∼ N (000, ΣΣΣωωω), αααst =




α1,st

α2,st


 ∼ N (000, ΣΣΣααα),

(6.1)






ΣΣΣωωω =

σ2
ω1

ρωωωσω1σω2

ρωωωσω1σω2

σ2
ω2

γj,t ⊥⊥ αj,st.






 , ΣΣΣααα =




σ2
α1

ρααασα1σα2

ρααασα1σα2

σ2
α2






we are aiming at deriving the conditional correlation between the count data in the BVAR(1)-

LCM model. We are going to derive the conditional mean, variance, and covariance in three

subsections.

6.1.1 Conditional Mean of Yj,st

The conditional mean of Yj,st given the covariates and covariance matrix of the latent effects is

expressed as,

E (Yj,st|ZZZjβββj, ΣΣΣωωω, ΣΣΣααα) = Eγj,t,αj,st|ΣΣΣωωω,ΣΣΣααα [E(Yj,st|γj,t, αj,st, ZZZjβββj, ΣΣΣωωω, ΣΣΣααα)]

= Eγj,t,αj,st|ΣΣΣωωω,ΣΣΣααα [λj,st] = Eγj,t,αj,st|ΣΣΣωωω,ΣΣΣααα [exp (ZZZjβββj + γj,t + αj,st)]

(6.2)

= exp (ZZZjβββj)Eγj,t|ΣΣΣωωω [exp (γj,t)] Eαj,st|ΣΣΣααα [exp (αj,st)]

For an AR(1) process (ϕj ̸= 1), the conditional distribution of γj,t given lag-one observation is,

γj,t|γj,t−1, ΣΣΣωωω ∼ N (ϕjγj,t−1, σ2

ωj )

(6.3)

140

---

<!-- PAGE 142 -->

The marginal distribution of γj,t is,

(cid:32)

γj,t|ΣΣΣωωω ∼ N

0,

(cid:33)

σ2
ωj
1 − ϕ2
j

For a Poisson lognormal model, we have

Lemma 6.1 If

then,

Y |λ ∼ P ois(λ), log(λ)|µ, σ2 ∼ N (µ, σ2),

E(Y |µ, σ2) = exp (µ + σ2/2)

V ar(Y |µ, σ2) = E(Y |µ, σ2) + exp (2µ) exp (σ2)(exp (σ2) − 1)

(6.4)

(6.5)

(6.6)

From lemma 6.1, the conditional expectation of Yj,st given ZZZjβββj, ΣΣΣωωω, ΣΣΣααα in (6.2) will be,

E (Yj,st|ZZZjβββj, ΣΣΣωωω, ΣΣΣααα) = exp (ZZZjβββj) exp

(cid:33)

(cid:32) σ2
ωj
2(1 − ϕ2
j )

(cid:33)

(cid:32) σ2
αj
2

exp

= mj,st

(6.7)

6.1.2 Conditional variance of Yj,st

With (6.7 ),the conditional variance of Yj,st given ZZZjβββj, ΣΣΣωωω, ΣΣΣααα is expressed as,

V ar(Yj,st|ZZZjβββj, ΣΣΣωωω, ΣΣΣααα) = E(Y 2

j,st|ZZZjβββj, ΣΣΣωωω, ΣΣΣααα) − (E[Yj,st|ZZZjβββj, ΣΣΣωωω, ΣΣΣααα])2

= E(Y 2

j,st|ZZZjβββj, ΣΣΣωωω, ΣΣΣααα) − m2

j,st

= Eγj,t,αj,st|ΣΣΣωωω,ΣΣΣααα

(cid:2)E(Y 2

j,st|γj,t, αj,st, ZZZjβββj, ΣΣΣωωω, ΣΣΣααα)(cid:3) − m2

j,st

= Eγj,t,αj,st|ΣΣΣωωω,ΣΣΣααα

(cid:2)λ2

j,st + λj,st

(cid:3) − m2

j,st

= Eγj,t,αj,st|ΣΣΣωωω,ΣΣΣααα [exp (2ZZZjβββj + 2γj,t + 2αj,st) + exp (ZZZjβββj + γj,t + αj,st)] − m2

= exp (2ZZZjβββj) exp

(cid:32)

= mj,st + m2

j,st

exp

(cid:33)

(cid:32) 2σ2
ωj
1 − ϕ2
j
(cid:32) σ2
ωj
1 − ϕ2
j

exp

(cid:17)

(cid:16)

2σ2
αj

+ exp (ZZZjβββj) exp

(cid:33)

(cid:32) σ2
ωj
2(1 − ϕ2
j )

exp

(cid:33)

(cid:33)

exp (σ2

αj ) − 1

141

j,st
(cid:32) σ2
αj
2

(cid:33)

− m2

j,st

(6.8)

---

<!-- PAGE 143 -->

6.1.3 Conditional covariance between Yi,st and Yj,st

With (6.7), the conditional covariance between Yi,st and Yj,st is expressed as,

Cov(Yi,st, Yj,st|ZZZiβββi, ZZZjβββj, ΣΣΣωωω, ΣΣΣααα) = Eγγγ,ααα|ΣΣΣωωω,ΣΣΣααα[Cov(Yi,st, Yj,st|γγγ, ααα, ZZZiβββi, ZZZjβββj, ΣΣΣωωω, ΣΣΣααα)]

+ Covγγγ,ααα|ΣΣΣωωω,ΣΣΣααα(E[Yi,st|γγγ, ααα, ZZZiβββi, ΣΣΣωωω, ΣΣΣααα)], E[Yj,st|γγγ, ααα, ZZZjβββj, ΣΣΣωωω, ΣΣΣααα)])

= 0 + Covγγγ,ααα|ΣΣΣωωω,ΣΣΣααα(exp (ZZZiβββi + γi,t + αi,st), exp (ZZZjβββj + γj,t + αj,st))

(cid:18)

= mi,stmj,st

exp

(cid:18) ρωωωσωiσωj
1 − ϕiϕj

(cid:19)

(cid:19)

+ ρααασαiσαj

− 1

Since the joint marginal distribution of γi,t and γj,t is,








 ∼ N


000,









γi,t

γj,t

σ2
ωi
1−ϕi
ρωωωσωi σωj
1−ϕiϕj











ρωωωσωi σωj
1−ϕiϕj
σ2
ωj
1−ϕj

With (6.9) and (6.10), we have

(6.9)

(6.10)

Cov(Yi,st, Yj,st|ZZZiβββi, ZZZjβββj, ΣΣΣωωω, ΣΣΣααα) = Covγγγ,ααα|ΣΣΣωωω,ΣΣΣααα(exp (ZZZiβββi + γi,t + αi,st), exp (ZZZjβββj + γj,t + αj,st))

(cid:18)

= mi,stmj,st

exp

(cid:18) ρωωωσωiσωj
1 − ϕiϕj

(cid:19)

(cid:19)

+ ρααασαiσαj

− 1

(6.11)

6.1.4 Conditional correlation between counts

Combining the results from (6.7), (6.8) and (6.11), we will be able to compute the conditional

correlation for the s-th stock and the t-th time interval,

Corr (Yi,st, Yj,st|ZZZiβββi, ZZZjβββj, ΣΣΣωωω, ΣΣΣααα) =

mi,stmj,st

(cid:16)

exp

(cid:115)

(cid:16)

mi,st + m2

i,st

(cid:16)

exp

(cid:16) σ2
ωi
1−ϕ2
i

(cid:17)

+ σ2
αi

6.2 Additional figures

(cid:16) ρωωωσωi σωj
1−ϕiϕj
(cid:17)(cid:17) (cid:18)

− 1

+ ρααασαiσαj

(cid:17)

− 1

(6.12)

mj,st + m2

j,st

exp

(cid:18) σ2
ωj
1−ϕ2
j

(cid:19)

(cid:19)(cid:19)

− 1

+ σ2
αj

(cid:17)

(cid:18)

142

---

<!-- PAGE 144 -->

Figure 31: The trace plot of daily aggregated model-based and empirical correlations in the Health-
care sector throughout January 2023

Figure 32: The trace plot of daily aggregated model-based and empirical correlations in the Indus-
trials sector throughout January 2023

143

---

<!-- PAGE 145 -->

Figure 33: Box plots for the square root of MSE comparison in the Health care sector between
BVRW(1)-LCM and Simple Linear Regression in January 2023

Figure 34: Box plots for the square root of MSE comparison in the Industrials sector between
BVRW(1)-LCM and Simple Linear Regression in January 2023

144

<!-- MARKITDOWN CONVERSION -->

<!-- Full MarkItDown conversion for formatting fidelity. -->

New developments in sequential change point detection for time
|     |     | series | and | spatio-temporal |     |     | analysis |     |
| --- | --- | ------ | --- | --------------- | --- | --- | -------- | --- |
by
|     |     |            |             | Yanzhao     |              | Wang          |           |         |
| --- | --- | ---------- | ----------- | ----------- | ------------ | ------------- | --------- | ------- |
|     |     |            |             | A PhD       | Dissertation |               |           |         |
|     |     |            |             | Submitted   | to           | the Faculty   |           |         |
|     |     |            |             |             | of the       |               |           |         |
|     |     | WORCESTER  |             | POLYTECHNIC |              |               | INSTITUTE |         |
|     |     | In partial | fulfillment |             | of the       | requirements  |           | for the |
|     |     |            | Degree      | of          | Doctor       | of Philosophy |           |         |
in
Statistics
|     |     |     |     |     | May, 2023 |     |     |     |
| --- | --- | --- | --- | --- | --------- | --- | --- | --- |
APPROVED:
| Professor  | Jian        | Zou, Advisor |           |          | Professor  |     | Nalini   | Ravishanker |
| ---------- | ----------- | ------------ | --------- | -------- | ---------- | --- | -------- | ----------- |
| Department | of          | Mathematical |           | Sciences | Department |     | of       | Statistics  |
| Worcester  | Polytechnic |              | Institute |          | University |     | of       | Connecticut |
| Professor  | Zheyang     | Wu           |           |          | Professor  |     | Fangfang | Wang        |
Department of Mathematical Sciences Department of Mathematical Sciences
Worcester Polytechnic Institute Worcester Polytechnic Institute
| Professor  | Qingshuo    | Song         |           |          |     |     |     |     |
| ---------- | ----------- | ------------ | --------- | -------- | --- | --- | --- | --- |
| Department | of          | Mathematical |           | Sciences |     |     |     |     |
| Worcester  | Polytechnic |              | Institute |          |     |     |     |     |

Abstract
Abrupt aberrations in stochastic systems often result from external factors of interest, such
as changes in trading intensity patterns or outbreaks of infectious diseases. These factors can
introduce abnormal observations into the corresponding data collection systems. However, the
data being monitored typically involve multiple sources, high dimensionality, and convoluted
mutual dependence. To promptly detect any change points within complex streaming data,
my dissertation research focuses on developing efficient methods for sequential change point
detection and multivariate time series modeling.
First, we focus on the study of online structural break detection in financial durations.
We propose an ensemble non-parametric methodology that leverages asymptotic theories and
re-sampling approaches for robust structural break detection, integrated with semi-parametric
model inference techniques. By detecting changes in the pattern of financial durations, practi-
tioners can take advantage of short-term profit opportunities through volatility-related option
tradingoradjusttheirpositiontomitigatetheimpactofsell-offsinthehigh-frequencyfinancial
market.
Second, we develop a Bayesian hierarchical framework with bivariate temporal effect and
latentlevel-correlatedeffectformultivariatediscrete-valuedfinancialtimeseries. Ourframework
enables the analysis of how count data relates to relevant covariates and provides forecasts for
future individual count data. Additionally, it establishes a connection between time-varying
observational correlation and latent correlations to more accurately quantify the association
between transaction counts at various risk levels. The INLA implementation of this framework
grants computational efficiency and flexibility for large-scale numerical studies.
Third, to address the complexity of the surveillance data, such as the spatio-temporal in-
terdependence, we synthesize relevant techniques from the previous two research projects and
propose an iterative sequential outbreak detection procedure for online spatio-temporal daily
count data. Specifically, we develop a Bayesian online spatio-temporal outbreak detection with
prior updating and p-value adaptation (BOSTON-PUPA) procedure. This iterative procedure
involves the generalized Poisson distribution (GPD) model and supports synchronous surveil-
lance over multiple locations with a controlled false detection rate as well as high sensitivity
against outbreaks in a wide range of signal-to-noise ratios.
Our research tackles various sequential change point problems across different scenarios,
providing efficient modeling for multivariate time series and corresponding sequential change
point detection techniques for time-dependent and spatio-temporal data. These methodologies
1

havebeensuccessfullyappliedinreal-worldapplicationssuchasfinanceandpublichealth,where
they offer high-quality statistical inference in an online fashion and can be easily extended to
| other domains | using a similar | framework. |
| ------------- | --------------- | ---------- |
2

Acknowledgements
Having my five-year Ph.D. journey was both a challenging and rewarding experience. Seeking
research-oriented solutions to advanced real-world problems required not only individual tenacity
but also a significant amount of support and guidance from different great people along this road.
Firstly, I want to express my sincere gratitude towards my Ph.D. advisor, Professor Jian Zou.
Notonlydoesheshareawealthofresearchexperienceandcommunicationskillswithmeprofession-
ally, but also demonstrates his exemplary work ethic and family commitment in a well coordinated
manner. As his Ph.D. student, I was lucky to have his heartfelt cheers for my research as well
as career achievements and I also felt blessed to receive his encouragement during my hardships.
With his advice and feedback, the progress of my dissertation was made much smoother and more
efficient. ProfessorZousetanexcellentexampletomeaboutbeinganoutstandingstatisticianwith
a combined trait of decent statistical background and high interpersonal intelligence, which I will
admire for my own career development in the future.
Secondly, I also want to thank the rest of my dissertation committee members, Professor Nalini
Ravishanker, Professor Fangfang Wang, Professor Zheyang Wu and Professor Qingshuo Song for
their generous inputs to my dissertation research. It was a very fulfilling experience for me to
collaborate with and learn from Professor Ravishanker since her high-standard requirements for
research deliverable and manuscript writing inspired me to take extra miles to justify and refine
my work. Expertise of Professor Wang and Professor Wu was a key motivating factor for me to
delve into advanced research areas such as multvariate time series analysis in spatial econometric
research and correlated p-value combination methods in genetic study. With Professor Song’s
affluent financial modeling experience and unique insights into article organzation, numerous edits
of my dissertation were stemming from his constructive suggestions. Their significant impacts on
my dissertation accomplishment are invaluable and are deeply appreciated.
I am also grateful for having Professor Balgobin Nandram as my independent study instructor
for advanced Bayesian statistics. His dedication and mastery towards Bayesian statistics expedited
myunderstandingofthisfieldinasolidfashion. MyspecialappreciationgoestoZijiYu, Jianchang
Lin from Takeda and Yaohua Zhang from Vertex as my external career influencers, since their
contribution to solving real world problems as prestigious industrial biostatisticians broadened my
3

horizon over the real application of statistics. In addition, I want to send my thankfulness to
other faculty members and staff who helped me along my journey, especially Rhonda Podell for her
administrativesupportandMikeMaloneforhistechnicalsupport,whenIwasaTeachingAssistant.
I also appreciated the quality time with my Ph.D. peers from various majors taking advanced
courses, brainstorming project problems, discussing career plans, and having fun together.
At last, I want to give my genuine thanks to my Dad Tanggui Wang, my Mom Jijuan Hu, and
my cousin Cheng Wang for their unconditional love and support, which is a crucial driving force
for me to persevere in the face of various obstacles and barriers.
4

Contents
1 Introduction 12
1.1 Sequential change point detection . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 12
1.2 Multivariate time series analysis . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 12
1.3 Fast Bayesian inference approximation . . . . . . . . . . . . . . . . . . . . . . . . . . 14
1.4 Summary . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 14
2 Online structural break point detection 16
2.1 Background . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 16
2.2 Literature review . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 16
2.2.1 Log ACD model . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 17
2.2.2 Change point detection . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 18
2.3 E-PEF detection . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 19
2.3.1 Model Framework . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 20
2.3.2 Parameter estimation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 20
2.3.3 Detector statistic . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 22
2.3.3.1 Spillover effect . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 23
2.3.4 Hypothesis testing . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 25
2.3.5 Ensemble detection . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 27
2.3.5.1 Motivation of ensemble detection . . . . . . . . . . . . . . . . . . . . 27
2.3.5.2 Ensemble detection scheme . . . . . . . . . . . . . . . . . . . . . . . 30
2.4 Numerical study . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 32
2.4.1 Simulation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 32
2.4.1.1 Monitoring horizon . . . . . . . . . . . . . . . . . . . . . . . . . . . 34
2.4.1.2 Detection probability and Delay . . . . . . . . . . . . . . . . . . . . 35
2.4.1.3 Robust performance for non-stationary scenarios . . . . . . . . . . . 36
2.4.2 Real application . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 40
2.5 Summary . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 43
5

3 Multivariate latent level correlation model (LCM) for financial high frequency
count time series 45
3.1 Background . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 45
3.2 Literature review . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 46
3.2.1 Discrete time series modeling . . . . . . . . . . . . . . . . . . . . . . . . . . . 46
3.2.2 Integrated Nested Laplace Approximation (INLA) . . . . . . . . . . . . . . . 48
3.3 BVAR(1)-LCM model . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 49
3.3.1 Model framework . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 50
3.3.2 INLA implementation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 53
3.4 Numerical study . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 57
3.4.1 Simulation study: INLA v.s STAN . . . . . . . . . . . . . . . . . . . . . . . . 57
3.4.2 Real application . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 60
3.4.2.1 High-frequency trading (HFT) background . . . . . . . . . . . . . . 64
3.4.2.2 High-frequency count data description . . . . . . . . . . . . . . . . . 65
3.4.2.3 Model adequacy and prediction accuracy comparisons . . . . . . . . 68
3.4.2.4 An illustration of BVRW(1)-LCM framework . . . . . . . . . . . . . 71
3.5 Summary . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 83
4 Sequential Bayesian spatio-temporal outbreak detection 84
4.1 Background . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 84
4.2 Literature review . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 85
4.2.1 Change point detection in public health surveillance system . . . . . . . . . . 85
4.2.2 Traditional outbreak detection methods . . . . . . . . . . . . . . . . . . . . . 86
4.2.3 Modern outbreak detection methods . . . . . . . . . . . . . . . . . . . . . . . 89
4.3 BOSTON-PUPA procedure . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 91
4.3.1 Step 1: Bayesian model inference and in-sample prediction . . . . . . . . . . 92
4.3.2 Step 2: Latent aberration assessment . . . . . . . . . . . . . . . . . . . . . . . 96
4.3.3 Step 3: P-value adaptation . . . . . . . . . . . . . . . . . . . . . . . . . . . . 97
4.3.4 Step 4: Decision-making and algorithm update . . . . . . . . . . . . . . . . . 99
4.4 Numerical study . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 101
6

4.4.1 Simulation study . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 101
4.4.1.1 Model parameter recovery and in-sample model prediction . . . . . 102
4.4.1.2 Outbreak detection performance . . . . . . . . . . . . . . . . . . . . 105
4.4.2 Real application . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 117
4.4.2.1 COVID-19 Data description . . . . . . . . . . . . . . . . . . . . . . 117
4.4.2.2 Implementation of BOSTON-PUPA . . . . . . . . . . . . . . . . . . 120
4.4.2.3 Remarks . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 122
4.5 Summary . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 122
5 Discussion and Future Work 124
6 Appendix 140
6.1 Derivation of conditional correlation . . . . . . . . . . . . . . . . . . . . . . . . . . . 140
6.1.1 Conditional Mean of Y . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 140
j,st
6.1.2 Conditional variance of Y . . . . . . . . . . . . . . . . . . . . . . . . . . . . 141
j,st
6.1.3 Conditional covariance between Y and Y . . . . . . . . . . . . . . . . . . 142
i,st j,st
6.1.4 Conditional correlation between counts . . . . . . . . . . . . . . . . . . . . . 142
6.2 Additional figures . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 142
List of Tables
1 Sampled time series from block bootstrap . . . . . . . . . . . . . . . . . . . . . . . . . . 26
2 Detector statistics computed from resampled time series from block bootstrap . . . . . . . 26
3 Detection probabilities in the monitoring horizon study. M is the length of training
2
period. k is the monitoring time point in the monitoring period after the training.
The false detection rate control α = 0.05. . . . . . . . . . . . . . . . . . . . . . . . . 35
4 Detection probabilities at different monitoring time under different scenarios. τ is
the true break point. k is the monitoring time point in the monitoring period. . . . . 36
5 Summary statistics of average delay under different scenarios for different break
points. τ is the true break point. False detection rate control is α = 0.05. The
length of training period is M = 2500. . . . . . . . . . . . . . . . . . . . . . . . . . . 37
2
7

6 Parameters for different Scenarios . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 57
7 Parameter recovery rate comparison between INLA and STAN for correlated tem-
poral effects ω and ω . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 61
1 2
8 Parameter recovery rate comparison between INLA and STAN for level-correlated
effects α and α . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 62
1 2
9 In-sample prediction and computational time comparison between INLA and STAN 63
10 An example of raw data for the stock ABT . . . . . . . . . . . . . . . . . . . . . . . 66
11 Data structure for INLA modeling. count data for stock ABT between 9:30 and 9:34
a.m. on 01/02/2013. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 67
12 Percentage of the 63 data sets favoring each model regarding in-sample model ade-
quacy and out-of-sample prediction accuracy . . . . . . . . . . . . . . . . . . . . . . 71
13 Hyperparameters with restricted support and their internal representation . . . . . . 94
14 Iterative prior updating procedure with tracked mean and overdispersion . . . . . . 96
15 Parameter setup throughout the simulation study . . . . . . . . . . . . . . . . . . . . 102
16 County populations in Massachusetts in 2018 . . . . . . . . . . . . . . . . . . . . . . 102
17 Parameter recovery rate under different combinations of sliding window size and
prior discounting factor . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 104
18 MSE for the last-day prediction in the sliding window . . . . . . . . . . . . . . . . . 104
19 Performance comparison between Prior Updating (PU) approach (T = 28,a = .25)
0
and Cumulative Fitting (CF) approach. Computation time is calculated as the
average computation time in seconds for individual model fittings in the iterative
process. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 105
20 Relativefrequenciesofdetectinganoutbreakoutof200simulationsforeachlocation
using different methods for different signal-to-noise ratios. . . . . . . . . . . . . . . . 110
21 Earliest detection days across different counties using HMP and CCT method. . . . 121
List of Figures
1 ScatterplotofdetectorstatisticsattimestampM +k =3000whenτ =3500. Thereddots
2
are observed detector statistic and black dots are bootstrap samples of the detector statistics 28
8

2 ScatterplotofdetectorstatisticsattimestampM +k =4000whenτ =3500. Thereddots
2
are observed detector statistic and black dots are bootstrap samples of the detector statistics 28
3 Thetraceplotofdurationofdurationinthecalendartime. Thex-axisiscalendartime(inseconds).
The y-axis denotes the value of duration. The lag between time indices of true break and detected
break is 200 and the delay time in the calendar time is 261.1051 s. . . . . . . . . . . . . . . . . 30
4 Break detection outcome from 500 simulations of in a monitoring period of length 5000. X-axis
stands for the monitoring period starting at M =2500. Y-axis stands for the empirical detection
2
probabilityataspecifictimepoint. Thebluedashedlinesstandforthetruebreakpointτ =2700,
3000, 3500, and 4000. The red dashed lines stand for the significance level α = 0.05. . . . . . 39
overall
5 (a)AsinglerealizationofScenario1withtruebreakatτ =3500;(b)Thetraceplotfortheindividual
GM2(k)withtheconfidenceintervalsbasedontheWienerprocessandbootstrapthresholdsingreen
j
bands; (c) The trace plot for the Mahalanobis distance d2 (k), with bootstrap threshold d2 (k)
M 1−αM
(red horizonal line); (d) The trace plot for the binary indicator of break detection δ(k) . . . . . . 40
6 Structuralbreakpointsdetected(redverticaldashlines)inthedurationtimeseriesofIBM,
BAC, MMM and GE respectively. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 43
7 Diurnal pattern exhibited in observed counts and averaged duration in 2-min inter-
vals for stock ABT on 01/02/2023. . . . . . . . . . . . . . . . . . . . . . . . . . . . . 68
8 Count data for three GICS sectors: Energy, Health care, Industrials . . . . . . . . . 69
9 The association between averaged durations and counts . . . . . . . . . . . . . . . . 74
10 The association between averaged log trading size and counts . . . . . . . . . . . . . 74
11 The estimated ρ with their 95% credible interval across all three sectors in January
ωωω
2013 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 75
12 The dot plot of estimated variances, σ2 and σ2 , of the latent temporal effects on
ω1 ω2
different days of a week across all three sectors in January 2013 . . . . . . . . . . . . 76
13 The estimated ρ with their 95% credible interval across all three sectors in January
ααα
2013 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 77
14 The dot plot of estimated variances of the latent level effects on different days of
week across all three sectors in January 2013 . . . . . . . . . . . . . . . . . . . . . . 78
15 Thevariancesoftheobservedcountsondifferentdaysofweekacrossallthreesectors
in January 2013 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 78
9

16 The trace plot of daily aggregated model-based and empirical correlations in the
Healthcare sector throughout January 2023 . . . . . . . . . . . . . . . . . . . . . . . 80
17 Box plots for the square root of MSE comparison in the Energy sector between
BVRW(1)-LCM and Simple Linear Regression in January 2023 . . . . . . . . . . . . 81
18 ThecomparisonbetweenSpearman’srankcorrelationandthelatentlevelcorrelation
across three sectors. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 82
19 Signal-to-ratio vs Aggregated Performance Measurements . . . . . . . . . . . . . . . 107
20 Empirical density plots of BOSTON-PUPA detected outbreak time point where the
first non-zero δ occurs in county s for different methods with different signal-
s,T+k
to-noise ratios (> 1). The red vertical lines represent the true outbreak time points
given in the simulation study, 103, 99, 95, 82, 102, 102, 91, 89, 97, 109, 100, and 87
for each location respectively. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 111
21 Signal-to-ratiovsEvaluationMetricsfordifferentcombinedp-valuemethods: Fisher’s,
Stouffer’s, Lancaster’s, HMP and CCT when P-value Adaptation is implemented. . . 112
22 Traceplot of outbreak detection probabilities from day 29 to day 200 across 13 re-
gions. Five combined p-value methods are compared at the nominal level α = 0.05,
represented by the red dashed horizontal lines. . . . . . . . . . . . . . . . . . . . . . 113
23 Traceplot of outbreak detection probabilities from day 29 to day 200 across 13 re-
gions. Five combined p-value methods are compared at the nominal level α = 0.05.
The red dashed lines stand for an ideal detection probability pattern of maintaining
at the nominal level before any outbreaks occur and spiking up promptly to 1 when
there are any outbreaks. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 114
24 Trajectories of sequential estimation of overdispersion parameter λ without any out-
breaks introduced (SNR =1) in the simulation study. Green lines stand for λˆ , blue
k
lines stand for λ
¯ˆ
, and the red line represents the actual value of the overdispersion
k
parameter λ = .4448 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 115
10

25 Trajectories of sequential estimation of overdispersion parameter λ with different
SNRs in the simulation study. Green lines stand for λˆ , blue lines stand for λ ¯ˆ , and
k k
the red line represents the actual value of the overdispersion parameter λ = .4448.
The two black vertical dashed lines stand for τ = 82 and τ +T = 109+28 = 137
4 11
accordingly. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 116
26 COVID-19 daily case count in different counties in Massachusetts from the dashboard118
27 P-values of Moran’s I and Geary’s C at every time stamp. The red dashed line
represents the significance level of 0.05.. . . . . . . . . . . . . . . . . . . . . . . . . . 119
28 ACF and PACF estimates for different counties in Massachusetts. Spatial IDs 1∼13
correspondtothefollowingcountiesinorder: Plymouth,Berkshire,Barnstable,Nor-
folk, Bristol, Suffolk, Franklin, Hampshire, Essex, Hampden, Dukes and Nantucket,
Middlesex, and Worcester. The red dashed lines represent the boundaries of a 95%
confidence interval for ACF and PACF. . . . . . . . . . . . . . . . . . . . . . . . . . 120
29 Calculated outbreak detection indicators δ using HMP and CCT across all
s,T+k
counties in the BOSTON-PUPA procedure. . . . . . . . . . . . . . . . . . . . . . . . 121
30 TraceplotofdailyCOVID-19casecountsinMA,2020,withdetectedoutbreaksusing
BOSTON-PUPAprocedure. Redlinerepresentsastate-wiseoutbreakindicatorfrom
the news . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 123
31 The trace plot of daily aggregated model-based and empirical correlations in the
Healthcare sector throughout January 2023 . . . . . . . . . . . . . . . . . . . . . . . 143
32 The trace plot of daily aggregated model-based and empirical correlations in the
Industrials sector throughout January 2023 . . . . . . . . . . . . . . . . . . . . . . . 143
33 Box plots for the square root of MSE comparison in the Health care sector between
BVRW(1)-LCM and Simple Linear Regression in January 2023 . . . . . . . . . . . . 144
34 Box plots for the square root of MSE comparison in the Industrials sector between
BVRW(1)-LCM and Simple Linear Regression in January 2023 . . . . . . . . . . . . 144
11

1 Introduction
1.1 Sequential change point detection
In real life, abrupt behavioral changes in a stochastic system are usually related to some trigger-
ing events and people need to take prompt action at the occurrence of such events. Therefore,
online change point detection in many fields is an important research topic. Nowadays, with the
advancement of technology, it is common for streaming data to have high-dimensional structures
withtime-dependenceandintercorrelation. Tomaketimelyandaccurateinferenceonchangepoint,
analyses of such modern streaming data with increased complexity and sizes are in great demand
of methodological innovation beyond traditional statistical techniques.
Early online change point detection method originated from Abraham Wald’s sequential design
(Wald, 1947), which aimed for early termination of an unpromising experiment with fewer obser-
vations. Page (1954) made further improvement and proposed CUSUM-type method for quality
control application in industry, with hypothesis testing on the CUSUM-type test statistic under
null hypothesis of no change points. Such hypothesis testing procedures are usually considered
distribution-free and no model fitting is needed (Mikl´os and Lajos, 1997; Bai, 1999; Banerjee and
Urga, 2005; D¨oring, 2011; Robbins et al., 2016). Despite its easy implementation, such testing
procedures are conducted under the assumption of independent samples. For time-dependent data,
there is a plethora of literature providing solutions within a Gaussian stochastic linear system
framework, such as a combination of Kalman filter and generalized likelihood ratio (GLR) (Lai
and Shan, 1999). Under some parametric assumptions, detector statistic can take the form of
additive changes based on likelihood or innovations. Furthermore, non-likelihood-based detector
statisticsarediscussedandimplementedbutsuchstudiesconsideredasymptoticGaussianproperty
for statistical inference. In the situations of change point detection in modern online data of ele-
vated complexity, the current trend of corresponding solutions lies in a linear system or parametric
framework, incorporating Gaussian property for inference on the detector statistics.
1.2 Multivariate time series analysis
Time series analysis is a popular research topic in various fields such as finance, econometrics,
climatology, epidemiology, clinical trials as well as interdisciplinary areas because the statistical
12

models under the independent assumptions usually lack sufficient accountability for the corre-
sponding chronological pattern. Due to the escalated demand of studying multiple measurements
as a whole, multivariate time series analysis becomes a natural tendency for correlation study for
multiple time-dependent data and draw universal inference on the latent dynamics from a collec-
tion of associated time series. In this dissertation, we propose our methods to address the research
problems arising in the financial time series and public health surveillance data.
With the advent of high-frequency trading, technological advancement allows people to record
andstorealargeramountoftransactiondatawithinashorttimeinterval. Transactionarrivaltimes
as well as measurements of interest can be studied as time series. However, market signals are not
salient among the high volume of raw data. For example, within a short period of time, numerous
transactions on an asset can be made but the asset price fluctuations are negligible. To study
the price change in a high-frequency setting, one can easily reach some biased conclusion from a
statisticalmodelfittedwithexcessiveinsignificantpricechanges. Anotherfeatureofhigh-frequency
financial data is irregularity. Unlike conventional time series data with standard time index, the
arrival times in high-frequency data can be randomly spaced. We need to take special care of data
processing in high-frequency financial market to study its micro-structure. Additionally, assets
prices usually are not only dependent on its own historical observations but also by some other
factors such as the overall market performance or other affiliated assets. Therefore, multivariate
time series analysis is an important tool to reveal the interrelations among multiple high-frequency
financial time series and unveil both macro-structure of the market behavior via the associated
individual assets and its micro-structure in granulated time period.
Public health surveillance analysis is a traditional research field, and its recent development
brings up new statistical challenges. Syndromic surveillance is one of the useful tools in public
health systems, which supports the monitoring of public health impacts and raise speedy alarms
at their occurrences. Preliminary diagnosis from syndromic surveillance uncovers potential onsets
of infectious outbreaks prior to a monitoring regime requiring laboratory confirmation (Hughes
et al., 2020). A decent syndromic system incorporates covariate information, spatial and temporal
dynamics of a disease, as well as integration of data from multiple sources. Therefore, the real-time
monitoring of an infectious disease such as COVID-19 in a large geographical area requires unique
accommodation for the spatio-temporal intricacy. Conventional methods either don’t account for
13

the spatial and temporal dynamics such as CUSUM (Page, 1954) or lack measure of uncertainty
for identified disease cluster (Kulldorff, 1997). Within a spatio-temporal framework, one needs to
not only overcome more complex configuration of graph structure in the model, but also keep the
implementation at a reasonable computational cost. Thanks to the advancement of technology,
Bayesian inference gains its popularity in complex modeling problems. Bayesian technique grants
the flexibility of incorporating historical information into the priors so that this approach can
alleviate the computational burden for complex Bayesian model inference. With a few stationarity
assumptions on the time series data, one is able to aim for historical information integration via
prior distributions.
1.3 Fast Bayesian inference approximation
Bayesian statistical analysis regained its popularity with the advancements in Markov chain Monte
Carlo (MCMC) sampling method during 1950s. Traditional Bayesian applications rely on the joint
posterior distribution of the model parameters. One of common concerns for the MCMC method is
about its computational efficiency. When the complexity of the model increases with the number of
parameters,thejointposteriordistributioninahighdimensionparameterspaceraisesthedifficulty
level for practitioners to draw samples from. In addition, posterior distribution without a closed
form will also lead an intensive computation for the traditional Bayesian inference.
However, in many situations, individual posterior marginals are often sufficient for adequate
statistical inference (G´omez-Rubio, 2020). Rue et al. (2009) proposed an approximate Bayesian
inferenceforlatentGaussianmodelsbyIntegratedNestedLaplaceApproximation(INLA).Notonly
is the inference based on posterior marginals as good as the inference based on the joint posterior
distribution, but also the computational cost can be enhanced to a large extent, especially for a
sparse Gaussian Markov Random Field (GMRF) in a high dimensional parameter space. Since
our Bayesian model frameworks involve GMRF, we will be able to implement customized GMRF
random effects using INLA and enjoy the benefit of speedy computation.
1.4 Summary
For the two prevalent research directions, new challenges are burgeoning in their combinations,
where practitioners need adequate modeling for the complicated real-time data to proactively make
14

decisions on the basis of the exhibited behavioral change therefrom. Innovative methodologies are
expected to support elaborate statistical models and enjoy easy implementation with an agreeable
running time.
To solve these problems in sequential change point detection as well as multivariare time series
analysis in finance and public health, the dissertation is organized as follows. In Chapter 2, we deal
with the online change point detection problem in high-frequency market and propose an ensemble
framework for sequential analysis within univaritare time series. In Chapter 3, we introduce a
Bayesian framework to account for the association among multiple assets, as well as capture the
behavior of the market from multivariate time series analysis. In Chapter 4, we conduct the se-
quential analysis of infectious outbreak via multivariate time series in the public health surveillance
data. We conclude our work and discuss future work in Chapter 5.
15

2 Online structural break point detection
2.1 Background
Automated high-frequency trading deals with a large number of trading orders. For each asset,
pricesatthesetransactionsformanirregularlyspacedtimeseries(WangandZou,2014). Therefore,
agoodawarenessofthevolatilityalternationofanassetiscrucialtomartketparticipants,especially
in a high-frequency setting. An important practical focus for investors will be monitoring the
volatilefinancialmarketquicklyandassessingaccuratelyanybehavioralchangeinanonlinefashion,
so that reliable inference can be maintained with updated model parameters.
A financial duration is defined as the difference in arrival time between two consecutive events
ofinterest. Aneventcanbedefinedas, butisnotlimitedto, asingletransaction, areturnbeyonda
certainpercentage,orapricechangeexceedingacertainamount. Thei-thdurationcanbeobserved
as x = t −t , where t denotes the timing of the i-th event. The irregularity of arrival times of
i i i−1 i
transactionscanprovideusefulinformationforthemarketparticipants. Forexample,iftransactions
happenrapidlyforanasset,thenthedurationsbetweentransactionswillbeintheformofnumerous
short time intervals, while infrequent transactions will provide a sequence of longer durations.
Further, higher frequency of the transactions implies higher volatility in price fluctuations, Easley
and O’hara (1992) discussed the link between the existence of information, the timing of trading
and price movement. Thus the negative influence of long durations on returns and variances of
asset price has predictive power for ultra-high-frequency volatility jointly with a GARCH model for
the price movement (Engle and Russell, 1997; Engle, 2000). When a structural break is detected,
practitioners can update their time series model and modify their trading algorithm with financial
domain knowledge. Therefore, We address this problem of structural breaks in time series of
durations and describe an online approach for detection but the embedding of detected breaks into
a specific trading strategy is upon the practitioners.
2.2 Literature review
With the definition of inter-trade durations, the objective is to detect structural breaks in the
duration time series from financial market, in a fast online fashion. In this subsection, we are
going to introduce the literature on the approaches for duration time series modeling and various
16

contributions in change point detection topic, which lay the foundation of our method.
2.2.1 Log ACD model
Modeling inter-event duration is a popular direction for statistical application in high-frequency
trading (Dutta et al., 2022). One of the prevalent frameworks to model time series of durations
is via conditional duration models. Starting from the seminal work of (Engle and Russell, 1998)
on auto-regressive conditional duration (ACD) models, there is a rich literature extension of ACD
models from different perspectives. Linear ACD modeling is rather common but restrictive, and
include the Exponential ACD (EACD), Weibull ACD (WACD), and Gamma ACD (GACD), etc.
Non-linear ACD models include the Log ACD models (Bauwens and Giot, 2000), the Stochastic
Conditional Duration, or SCD (p,q) models (Bauwens and Veredas, 2004) and Augmented ACD
(AACD) models through Box-Cox transformation (Fernandes and Grammig, 2006). In order to
address the long memory dependence exhibited in durations, Jasiak (1999) proposed a class of
fractionally integrated ACD (FIACD) models, and Deo et al. (2010) introduced a parametric,
latent-variable, long memory stochastic duration (LMSD) to handle the long memory feature of
inter-trade durations better than ordinary ACD models. For extreme value modeling in durations,
Zheng et al. (2016) incorporated Fre´chet innovations in the usual ACD model, and demonstrated
a better fit with Fre´chet ACD model than the Weibull ACD model. Pacurar (2008) discusses
detailed theoretical properties and applications of duration models. A plethora of literature has
showed the versatility of duration models in the fields of Finance, Econometrics, etc. Our work is
hence established under log ACD model framework for online structural break detection problems
in the financial durations.
Useful approaches for parameter estimation for the ACD models are maximum likelihood es-
timation (MLE), generalized method of moments (GMM) estimation, quasi-maximum likelihood
estimation (QMLE) and estimating function (EF) estimation (Engle and Russell, 1998; Grammig
and Wellner, 2002; Allen et al., 2008; Liang et al., 2011). Thavaneswaran et al. (2015) proposed a
combined martingale EF approach for recursive parameter estimation of generalized duration mod-
els. Zhang et al. (2019) proposed a penalized estimating function (PEF) for the aforementioned
recursive parameter estimation for the log ACD models. To enhance the efficiency of parameter
estimation, we will adopt a distribution-free approach using the penalized estimation function for
17

| a robust | outcome. |     |     |     |     |     |     |
| -------- | -------- | --- | --- | --- | --- | --- | --- |
The key idea of ACD model can be described as following. Let x = t −t , where i = 1,2,...
i i i−1
Fx
denote the financial duration time series, and let denote the information set of past durations.
i−1
The ACD model explaines the time dependence between x and past observations through the
i
| conditional | expectation | of x on   | Fx . Then     | the ACD(p,q) | model       | is          |       |
| ----------- | ----------- | --------- | ------------- | ------------ | ----------- | ----------- | ----- |
|             |             | i         | i−1           |              |             |             |       |
|             |             |           |               | p            |             | q           |       |
|             |             |           |               | (cid:88)     | (cid:88)    |             |       |
|             |             | x i = ψ i | ε i , where ψ | i = ω+       | α j x i−j + | β j ψ i−j . | (2.1) |
|             |             |           |               | j=1          | j=1         |             |       |
In the Eq (2.1), the parameters are θθθ = (ω,α ,...,α ,β ,...,β ). The weak stationarity of
|     |     |     |     | 1   | p 1 | q   |     |
| --- | --- | --- | --- | --- | --- | --- | --- |
this non-negative process is guaranteed by the conditions of ω > 0,α j ≥ 0 for j = 1,...,p,β j ≥ 0
|     |     | (cid:80)p | (cid:80)q |     |     |     |     |
| --- | --- | --------- | --------- | --- | --- | --- | --- |
for j = 1,...,q and α + β < 1. The innovations ε are assume to be independent
|     |     | j=1 j | j=1 j |     |     | i   |     |
| --- | --- | ----- | ----- | --- | --- | --- | --- |
and indentically distributed non-negative random variables with E(ε) = 1 and density f (.) and
ε
Fx
independent of . Log ACD model takes a similar form except that x = exp(ψ )ε , and its
|     | i−1 |     |     |     |     | i   | i i |
| --- | --- | --- | --- | --- | --- | --- | --- |
elaboration will be discussed in the unified E-PEF framework subsection.
| 2.2.2 | Change point | detection |     |     |     |     |     |
| ----- | ------------ | --------- | --- | --- | --- | --- | --- |
There is a plethora of literature on change point detection, which can be classified into retrospec-
tive analysis and sequential (or online) analysis. As for the detection approach for the specific
monitoring process, online change point detection fits the needs of high-frequency traders in a real-
time setting because they need to make decisions promptly with streaming data. Some viewpoints
from retrospective detection (with complete data) inspire us in our endeavor. The seminal work of
change point detection originated in quality control (Page, 1954, 1955), with the main considera-
tion as hypothesis testing on the CUSUM-type test statistic under the null hypothesis of no break
points. Such hypothesis testing procedures are usually considered distribution-free and require no
model fitting (Mikl´os and Lajos, 1997; Bai, 1999; Banerjee and Urga, 2005; D¨oring, 2011; Robbins
et al., 2016). In financial applications, Zhang et al. (2001) proposed a threshold ACD model and
improved several inadequacies of the original ACD models. Zhang et al. (2018) implemented a pe-
nalized estimating function (PEF) approach for recursive estimation of log ACD model parameters
and applied a FindPeaks procedure to detect the structural breaks on the trajectory of the recur-
sively estimated parameter values. However, this retrospective study requires that the complete
18

observations are available.
In the online change detection field, the Kalman filter and its extensions have gained its pop-
ularity for Gaussian linear dynamic systems. Besides innovation-based methodologies, generalized
likelihood ratio (GLR) based testing is another direction to achieve online detection (Willsky and
Jones, 1976; Lai and Shan, 1999). Chu et al. (1996) discussed two sequential tests for the online
monitoring of economic behavior via linear regression models. The break detection was determined
by the fluctuation of the online sequential parameter estimates. However, the aforementioned on-
line detection methodologies handle the additive changes through either likelihood or innovations
under a parametric modeling framework with specific distributional assumptions.
In addition, an asymptotic Gaussian non-likelihood statistic is developed for online detection
in signal processing and adaptive control (Benveniste et al., 1987, 2012). Berkes et al. (2004)
extended online sequential change point detection via a quasi-likelihood function based approach,
and applied it to GARCH (p,q) models in a financial application. The test statistic for a structural
break consists of a standardized partial sum of the quasi-likelihood score function; The critical
value can be approximated via a Wiener process (Heyde, 1997). Huˇskov´a et al. (2007) investigated
the limiting behavior of test statistics based on various functionals of the partial sums of weighted
residuals. Aue et al. (2009) put forward a change point testing procedure for the volatility and
cross-volatility of multivariate time series via a vectorized CUSUM-type statistic. Horv´ath and
Rice (2014); Xie et al. (2021) give a broad review of change point detection methodologies across
different areas and their extensions.
2.3 E-PEF detection
The literature mentioned before addressed the change point detection in sequential data, under
a linear system or parametric framework, or through the asymptotic Gaussian property of the
detector statistics. Therefore, we propose an innovative ensemble penalized estimating function
(E-PEF) approach to solve the detection problem. Our contribution is a non-Gaussian detector
statistic based on the penalized estimation function for the log ACD models when the asymptotic
property is not well obtained from finite samples. This ensemble approach complements a non-
Gaussian distribution with the empirical bootstrap distribution to control the false detection rate
intheonlinesetting, whilestillenjoyingitscomputationalspeed. Basedonourstraightforwardand
19

well-grounded detection mechanism, practitioners can effortlessly monitor online transaction-level
financial data, and make strategic investment with sound statistical support.
| 2.3.1 | Model Framework |     |     |     |     |     |
| ----- | --------------- | --- | --- | --- | --- | --- |
For a duration time series x ,i = 1,2,..., we aim to detect the first break point (τ) such that
i
x ,x ,...,x are generated from one process and x ,x ,..., are generated from a different
| 1 2 | τ   |     |     |     | τ+1 τ+2 |     |
| --- | --- | --- | --- | --- | ------- | --- |
porcess. Consider the log ACD framework (Thavaneswaran et al., 2015), in a high-frequency
setting, a penalized log ACD (p,0) model with large p generally provides better computational
speed and precision gain of parameter estimation than a penalized log ACD (p,q) framework does.
| For simplicity, | we take | the log ACD | (p,0) | model as | an illustration. |     |
| --------------- | ------- | ----------- | ----- | -------- | ---------------- | --- |
|                 |         |             | exp(ψ | )        |                  |     |
i
|     |     |     | x = | ε ,i | = 1,2,..., |     |
| --- | --- | --- | --- | ---- | ---------- | --- |
|     |     |     | i   | µ i  |            |     |
ε
|     |     |     |       | exp(ψ | )   |       |
| --- | --- | --- | ----- | ----- | --- | ----- |
|     |     |     | |Fx   |       | i   |       |
|     |     |     | E(x i | ) =   | ,   | (2.2) |
|     |     |     |       | i−1   | µ   |       |
ε
p
(cid:88)
|     |     |     | ψ = ω+ | α   | logx , |     |
| --- | --- | --- | ------ | --- | ------ | --- |
|     |     |     | i      | j   | i−j    |     |
j=1
where ϵ is the non-negative innovation term with mean µ , Fx denotes the information set
|     | i   |     |     |     | ϵ   |     |
| --- | --- | --- | --- | --- | --- | --- |
i−1
associated with {x ,x ,...,x }, ω,α ,...,α are the AR coefficients in the log ACD model. For
|     | 1 2 | i−1 | 1   | p   |     |     |
| --- | --- | --- | --- | --- | --- | --- |
(cid:80)p
weak stationarity of the log ACD process, we let α < 1. To complete the detection of any
|     |     |     |     |     | j=1 j |     |
| --- | --- | --- | --- | --- | ----- | --- |
potential structural break point τ in the streaming time series of durations, there are three steps
to take: parameter estimation, detector statistic monitoring, and hypothesis testing, as described
below.
| 2.3.2 | Parameter estimation |     |     |     |     |     |
| ----- | -------------------- | --- | --- | --- | --- | --- |
Weapplythequasi-likelihood-typemethod(Berkesetal.,2004)todetectthestructuralbreakonthe
levelofparameterchangeinthelogACDmodel. Thestructuralbreakpointdetectionisbasedupon
the PEF (Zhang et al., 2019) for the parameters in the log ACD model. Letθθθ = (ω,α ,α ,...,α )′
1 2 p
be the parameters in the log ACD (p,0) model and p be the order of the log ACD model. p is
chosen to be a large number (to capture potential AR structure for the underlying log ACD model
as well as to approximate the MA structure of the log ACD model, if any). The total number of
20

| parameters | involved |     | is d | = p+1. |     |     |     |     |     |     |     |     |     |
| ---------- | -------- | --- | ---- | ------ | --- | --- | --- | --- | --- | --- | --- | --- | --- |
For a comprehensive procedure of recursive martingale PEF estimation, we need to introduce
a few required quantities involved in the PEF, with detailed definitions from Zhang et al. (2019).
Suppose x ,i = 1,2,...,n is a realization of a duration process with parameters in θθθ, define linear
i
| and quadratic |     | martingale |     | differences | respectively |           | as,    |          |     |     |     |     |     |
| ------------- | --- | ---------- | --- | ----------- | ------------ | --------- | ------ | -------- | --- | --- | --- | --- | --- |
|               |     |            |     |             | m            | i (θθθ) = | x i −µ | i (θθθ), |     |     |     |     |     |
(2.3)
m2(θθθ)−σ2(θθθ),
Q i (θθθ) =
|     |     |     |     |     |     |     | i   | i   |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
whereµ (θθθ)andσ2(θθθ)areconditionalmeanandvarianceofx correspondingly. Quadraticvariations
|     | i   |     |     |     |     |     |     |     | i   |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
i
| and covariation |     | of m | and | Q are        | defined | as,             |          |     |     |                |     |     |       |
| --------------- | --- | ---- | --- | ------------ | ------- | --------------- | -------- | --- | --- | -------------- | --- | --- | ----- |
|                 |     |      | i   | i            |         |                 |          |     |     |                |     |     |       |
|                 |     |      |     | E[m2(θθθ)|Fx |         |                 | σ2(θθθ), |     |     |                |     |     |       |
|                 |     |      | ⟨m⟩ | =            |         | ] =             |          |     |     |                |     |     |       |
|                 |     |      | i   | i            |         | i−1             | i        |     |     |                |     |     |       |
|                 |     |      |     | E[m4(θθθ)|Fx |         | ]−(E[m2(θθθ)|Fx |          |     | ])2 | (θθθ)−σ4(θθθ), |     |     |       |
|                 |     |      | ⟨Q⟩ | =            |         |                 |          |     | =   | κ              |     |     | (2.4) |
|                 |     |      | i   | i            |         | i−1             | i        | i−1 |     | i              | i   |     |       |
E[m3(θθθ)|Fx
|     |     |     | ⟨m,Q⟩ | =   |     | ]   | = γ (θθθ), |     |     |     |     |     |     |
| --- | --- | --- | ----- | --- | --- | --- | ---------- | --- | --- | --- | --- | --- | --- |
|     |     |     |       | i   | i   | i−1 | i          |     |     |     |     |     |     |
where κ i (θθθ) and γ i (θθθ) are the third and fourth central moments of x i respectively. Next, Tha-
vaneswaran et al. (2015) derived the optimal (Godambe-Durbin) combined martingale EF,
|     |     |     |         |     | n        |     | n               |            |     |         |         |     |       |
| --- | --- | --- | ------- | --- | -------- | --- | --------------- | ---------- | --- | ------- | ------- | --- | ----- |
|     |     |     |         |     | (cid:88) |     | (cid:88)(cid:0) |            |     |         | (cid:1) |     |       |
|     |     |     | g∗(θθθ) | =   | g∗(θθθ)  | =   | a∗              | m (θθθ)+b∗ |     | Q (θθθ) | ,       |     | (2.5) |
|     |     |     |         | C   | i        |     | i−1             | i          | i−1 | i       |         |     |       |
|     |     |     |         |     | i=1      |     | i=1             |            |     |         |         |     |       |
where
(cid:18) (cid:18) (cid:20) ∂(m2(θθθ)−σ2(θθθ)) (cid:21) ∂E[(m2(θθθ)−σ2(θθθ))|Fx ](cid:19) (cid:19)
|          |      | ∂µ  | i (θθθ) | 1     |     |     |      |     |     |     |      |     |     |
| -------- | ---- | --- | ------- | ----- | --- | --- | ---- | --- | --- | --- | ---- | --- | --- |
| a∗ (θθθ) | = ρ2 | −   |         | −     | E   | i   | i    | Fx  | −   | i   | i    | i−1 | η , |
| i−1      | i    |     |         |       |     |     |      | i−1 |     |     |      |     | i   |
|          |      |     | ∂θθθ    | ⟨m⟩ i |     |     | ∂θθθ |     |     |     | ∂θθθ |     |     |
(cid:18) (cid:18) (cid:20) (cid:21) ∂E[(m2(θθθ)−σ2(θθθ))|Fx ](cid:19) (cid:19)
|          |      | ∂µ   | (θθθ) |     | ∂(m2(θθθ)−σ2(θθθ)) |      |      |     |     |      |       | 1   |     |
| -------- | ---- | ---- | ----- | --- | ------------------ | ---- | ---- | --- | --- | ---- | ----- | --- | --- |
| b∗ (θθθ) | = ρ2 | i    | η     | + E | i                  |      | i Fx | −   |     | i    | i i−1 |     | ,   |
| i−1      | i    |      | i     |     |                    |      |      | i−1 |     |      |       |     |     |
|          |      | ∂θθθ |       |     |                    | ∂θθθ |      |     |     | ∂θθθ |       | ⟨Q⟩ |     |
i
(2.6)
with
|     |     |     |     |     | (cid:18) | ⟨m,Q⟩2  | (cid:19)−1 |      | ⟨m,Q⟩   |     |     |     |       |
| --- | --- | --- | --- | --- | -------- | ------- | ---------- | ---- | ------- | --- | --- | --- | ----- |
|     |     |     |     | ρ2  |          |         | i          |      |         | i   |     |     |       |
|     |     |     |     | =   | 1−       |         |            | ,η = |         | .   |     |     | (2.7) |
|     |     |     |     | i   |          | ⟨m⟩ ⟨Q⟩ |            | i    | ⟨m⟩ ⟨Q⟩ |     |     |     |       |
|     |     |     |     |     |          | i       | i          |      | i       | i   |     |     |       |
21

| Based on | (2.5), the | PEF | is, |     |          |               |     |        |     |     |     |       |
| -------- | ---------- | --- | --- | --- | -------- | ------------- | --- | ------ | --- | --- | --- | ----- |
|          |            |     |     |     | g∗ (θθθ) | = g∗(θθθ)−np′ |     | (θθθ), |     |     |     | (2.8) |
|          |            |     |     |     | C,λ      | C             |     | λ      |     |     |     |       |
with the first derivative of the SCAD penalty (Fan and Li, 2001) for a > 2 and penalty parameter
λ,
(aλ−|θθθ|)
|     |     |     | p′ (|θθθ|) | = λ{I(|θθθ| |     | ≤ λ)+ |     | +   | I(|θ| | > λ)}. |     | (2.9) |
| --- | --- | --- | ---------- | ----------- | --- | ----- | --- | --- | ----- | ------ | --- | ----- |
λ
(a−1)λ
The choice depends on the liquidity of a stock which is proportional to n, and details on how to
select a and the tuning parameter λ are discussed in (Zhang et al., 2019). For (2.3) - (2.8), µ (θθθ),
i
| σ2(θθθ), |     |     |     |     |     | ρ2, |     |     |     | g∗ a∗ | b∗  |     |
| -------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----- | --- | --- |
γ (θθθ), κ (θθθ), ⟨m⟩ , ⟨M⟩ , ⟨m,M⟩ , η are scalars, while θθθ, (θθθ), (θθθ), (θθθ) are
| i i | i   |     | i   | i   | i   | i i |     |     |     | C,λ i−1 | i−1 |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------- | --- | --- |
d×1 vectors. In the parameter estimation stage, streaming time series of durations recursively
| updates        | the estimation |           | of θθθ. |     |     |     |     |     |     |     |     |     |
| -------------- | -------------- | --------- | ------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2.3.3 Detector |                | statistic |         |     |     |     |     |     |     |     |     |     |
Considertheobserveddurationsx ,x ,...,x formodeltraining,theestimationofθθθisrecursively
|     |     |     |     | 1   | 2   | M2  |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
θθθˆˆˆ
updated to . As the new observations x ,x ,...,x arrive, we will sequentially
|     | M2  |     |     |     |     | M2+1 | M2+2 |     | M2+k |     |     |     |
| --- | --- | --- | --- | --- | --- | ---- | ---- | --- | ---- | --- | --- | --- |
evaluate their behavioral pattern and assess the occurrence of any structural breaks through a
| detector | statistic. |     |     |     |     |     |     |     |     |     |     |     |
| -------- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Similar to Berkes et al. (2004), our proposed detector statistic relies on the PEF. It is a d-
| dimensional | column | vector, |          |     |                          |     |     |     |     |           |     |        |
| ----------- | ------ | ------- | -------- | --- | ------------------------ | --- | --- | --- | --- | --------- | --- | ------ |
|             |        |         |          |     | (cid:16)                 |     |     |     |     | (cid:17)′ |     |        |
|             |        |         | GGGM2(k) |     | GM2(k),GM2(k),...,GM2(k) |     |     |     |     |           |     |        |
|             |        |         |          | =   |                          |     |     |     |     | ,         |     | (2.10) |
|             |        |         |          |     | 1                        |     | 2   |     | d   |           |     |        |
where
(cid:114)
|     |        |     |          | (cid:16) |        | (cid:17) |          |     |      |              |     |        |
| --- | ------ | --- | -------- | -------- | ------ | -------- | -------- | --- | ---- | ------------ | --- | ------ |
|     | GM2(k) |     | (cid:88) |          | g∗ (θˆ |          | ˆ(M1,M2) |     |      | N+,j         |     |        |
|     |        | =   |          |          |        | )        | / DDD    |     | ,k ∈ | = 1,2,...,d, |     | (2.11) |
|     | j      |     |          |          | i,λ    | j,M2     |          | j,j |      |              |     |        |
M2<i≤M2+k
with
|     |     |          |     |     | 1   |          | (cid:16) |        | (cid:17)(cid:16) | (cid:17) |     |     |
| --- | --- | -------- | --- | --- | --- | -------- | -------- | ------ | ---------------- | -------- | --- | --- |
|     |     | ˆ(M1,M2) |     |     |     | (cid:88) | g∗       | (θθˆ   | g∗               | (θθˆ )′  |     |     |
|     |     | DDD      |     | =   |     |          |          | θ      | )                | θ ,      |     |     |
|     |     |          |     | M   | −M  |          |          | i,λ M2 |                  | i,λ M2   |     |     |
|     |     |          |     | 2   | 1   |          |          |        |                  |          |     |     |
M1<i≤M2
|     |     | g∗  | (θθˆ | g∗(θθˆ | )−p′ | (|θθˆ |     |     |     |     |     |        |
| --- | --- | --- | ---- | ------ | ---- | ----- | --- | --- | --- | --- | --- | ------ |
|     |     |     | θ )  | = θ    |      | θ     | |). |     |     |     |     | (2.12) |
|     |     | i,λ | M2   | i      | M2   | λ     | M2  |     |     |     |     |        |
22

From (2.10) to (2.12), the detector is in the form of a standardized PEF, with the scaling matrix
being DDDˆˆˆ(M1,M2). DDDˆˆˆ(M1,M2) is regarded as the sample covariance matrix of g ∗ (θθθˆˆˆ ). M is the
|     |     |     |     |     |     |     |     |     |     | i ,λ | M2  | 2   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---- | --- | --- |
training sample size of the durations. M 1 (M 1 < M 2 ) serves as a length of burn-in period, which is
part of the training period, because PEF approach takes a certain number of iterations to reach to
a relative stable stage of θθθ estimation. Truncating the burn-in period of the parameter estimation
DDDˆˆˆ(M1,M2).
stabilizes the scaling matrix Consequently, after the training period M , the detector
2
statistic GGGM2(k) at the time M +k is accessible as a function value of estimated parameters from
2
θθθˆˆˆ
training period, M2 , new observed data {x M2+1 ,x M2+2 ,...,x M2+k }, and tuning parameter λ.
2.3.3.1 Spillover effect The detector statistic in (2.10) contains the partial derivatives of
the martingale estimating function for each parameters. However, any parameter change doesn’t
coincide with just the change of an individual component of the detector statistic due to the inter-
| correlation | among | the | components, |     | known | as the spillover | effect. |     |     |     |     |     |
| ----------- | ----- | --- | ----------- | --- | ----- | ---------------- | ------- | --- | --- | --- | --- | --- |
Spillover effect theoretical justification: For the two major terms aside from the penalty
expression p′ (|θθθ|) in the penalized estimating function in (2.5), each element of the two vectors is
λ
involved with the terms ⟨m⟩ ,⟨Q⟩ and η , and they can’t be canceled in the computation. In the
|     |     |     |     | i i | i   |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
structure of ψ i in (2.2), any parameter change will lead to a change on the value of ψ i . In a log
ACD (p,0) framework (2.2), the derivative of ψ with respect to θθθ = (ω,α ,α ,...,α )T becomes,
|     |     |     |     |     |     | i   |     |     | 1   | 2   | p   |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
∂ψ
i
|     |     |     |     | =    | (1,logx | ,logx   | ,...,logx | )′. |     |     |     | (2.13) |
| --- | --- | --- | --- | ---- | ------- | ------- | --------- | --- | --- | --- | --- | ------ |
|     |     |     |     | ∂θθθ |         | i−1 i−2 |           | i−p |     |     |     |        |
In the expressions of a∗ (θθθ) and b∗ (θθθ) in (2.6), the conditional mean of x is,
|     |     |     | i−1 |     | i−1 |     |     |     |     | i   |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
µ
|     |     |     |     |         |       | |Fx   |          | ϵ   |     |     |     |        |
| --- | --- | --- | --- | ------- | ----- | ----- | -------- | --- | --- | --- | --- | ------ |
|     |     |     |     | µ (θθθ) | = E[x | ] =   | exp{ψ }· | ,   |     |     |     | (2.14) |
|     |     |     |     | i       |       | i i−1 | i        | µ   |     |     |     |        |
ϵ
)T
and the derivative of µ (θθθ) with repect to θθθ = (ω,α ,α ,...,α can be derived using the
|     |     |     | i   |     |     |     | 1   | 2 p |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
chain rule,
|     |     | ∂µ (θθθ) | ∂µ  | (θθθ) ∂ψ |         |            |           |               |     |     |     |        |
| --- | --- | -------- | --- | -------- | ------- | ---------- | --------- | ------------- | --- | --- | --- | ------ |
|     |     | i        |     | i        | i       |            |           |               |     |     | )′. |        |
|     |     |          | =   | ·        | = exp{ψ | i }(1,logx | i−1 ,logx | i−2 ,...,logx |     | i−p |     | (2.15) |
|     |     | ∂θθθ     | ∂ψ  |          | ∂θθθ    |            |           |               |     |     |     |        |
i
23

For the quadratic variation and covariation, they can also be expressed in terms of ψ
i
σ2
⟨m⟩ = σ2(θθθ) = exp{2ψ } ϵ,
i i i µ2
ϵ
κ
⟨Q⟩ = κ (θθθ)−σ4(θθθ) = exp{4ψ } ϵ , (2.16)
i i i i µ4
ϵ
γ
ϵ
⟨m,Q⟩ = γ (θθθ) = exp{3ψ } ,
i i i µ3
ϵ
where µ ,σ2,γ ,κ are the mean, variance, third and fourth moments of the error ϵ in (2.2),
ϵ ϵ ϵ ϵ i
respectively.
Inserting the quantities into (2.6), we have,
 
(cid:18) γ2 (cid:19)−1 ∂ψ 1 σ2 ∂ψ γ ·µ2
a∗ i−1 (θθθ) = 1− σ ϵ 2· ϵ κ ϵ − ∂θθθ i · exp{ψ i }· σ µ ϵ 2 2 +2exp{2ψ i } µ ϵ 2 ϵ · ∂θθθ i · exp{3ψ ϵ i }· ϵ σ ϵ 2·κ ϵ 
ϵ
 
(cid:18) γ2 (cid:19)−1 ∂ψ 1 γ
= 1− ϵ · i − +2 ϵ ,
σ ϵ 2·κ ϵ ∂θθθ exp{ψ i }· σ µ ϵ 2 2 exp{ψ i }·κ ϵ
ϵ
(cid:34) (cid:35)
(cid:18) γ2 (cid:19)−1 ∂ψ γ ·µ2 σ2 ∂ψ 1
b∗ (θθθ) = 1− ϵ i ϵ ϵ −2exp{2ψ } ϵ · i ·
i−1 σ2·κ ∂θθθ exp{3ψ }·σ2·κ i µ2 ∂θθθ exp{4ψ } κ
ϵ ϵ i ϵ ϵ ϵ i µ4
ϵ
(cid:34) (cid:35)
(cid:18) γ2 (cid:19)−1 ∂ψ γ ·µ2 2σ2
= 1− ϵ · i ϵ ϵ − ϵ .
σ2·κ ∂θθθ exp{3ψ }·σ2·κ exp{2ψ } κ
ϵ ϵ i ϵ ϵ i µ2
ϵ
(2.17)
Therefore, g∗ (θθθ) can be found as
i,λ
 
(cid:18) γ2 (cid:19)−1 ∂ψ 1 γ
g
i
∗
,λ
(θθθ) = 1−
σ ϵ 2·
ϵ
κ ϵ
·
∂θθθ
i −
exp{ψ i }· σ µ ϵ 2 2
+2
exp{ψ
ϵ
i }·κ ϵ
·(x
i
−exp{ψ
i
})+
ϵ
(cid:34) (cid:35)
(cid:18) γ2 (cid:19)−1 ∂ψ γ ·µ2 2σ2 (cid:18) σ2(cid:19)
1− ϵ · i ϵ ϵ − ϵ · (x −exp{ψ })2−exp{2ψ }· ϵ
σ2·κ ∂θθθ exp{3ψ }·σ2·κ exp{2ψ } κ i i i µ2
ϵ ϵ i ϵ ϵ i µ2 ϵ
ϵ
−p′ (|θθθ|),
λ
(2.18)
where we note that the existence of ψ will have an impact on every element of the penalized
i
estimating function. This helps to justify the spillover effect. As such, our online detection algo-
24

rithm will mainly focus on the detection of the existence of parameter change instead of specifying
| any particular   | varying | parameters. |     |     |     |     |     |     |     |
| ---------------- | ------- | ----------- | --- | --- | --- | --- | --- | --- | --- |
| 2.3.4 Hypothesis |         | testing     |     |     |     |     |     |     |     |
In the hypothesis test of the detector statistic, we need to set up thresholds to decide if the break
|GM2(k)|
point has occurred. Consequently, some alarm will be raised when > T where T is a
|           |              |              |          |     |     |     | j   | α   | α   |
| --------- | ------------ | ------------ | -------- | --- | --- | --- | --- | --- | --- |
| threshold | based on the | significance | level α. |     |     |     |     |     |     |
Wiener process threshold: According to (Heyde, 1997), the estimating functions preserve
|     |     |     |     |     |     |     |     | (cid:16) | (cid:17) |
| --- | --- | --- | --- | --- | --- | --- | --- | -------- | -------- |
)−1/2GM2(k)canbeapproximatedby
| asymptoticnormalitypropertyand(M |     |     | −M  |     |     |     |     | (1+k)W | ( k ) ,k ∈ |
| -------------------------------- | --- | --- | --- | --- | --- | --- | --- | ------ | ---------- |
|                                  |     |     | 2   | 1   | j   |     |     |        | j 1+k      |
[0,∞) under the null hypothesis, where W (·),j = 1,2,...,d are independent standard Wiener pro-
j
| Thethresholdfor|GM |     |     |     |     |     |     | 1   |     |     |
| ------------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- |
cess. 2(k)|canbechosenasT (k) = (M −M ) 2(1+k/(M −M ))g(k,M )
|     |     | j   |     |     | α,W | 2   | 1   | 2 1 | 2   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
and (Berkes et al., 2004) proposed that a constant boundary function g(k,M ) = c is sufficient. As
2
an asymptotic result, Wiener process threshold has a loss of accuracy if the sample size is limited.
To accommodate scenarios with small sample sizes, we will consider the empirical distribution of
| the detector | statistic | under the | null hypothesis. |     |     |     |     |        |     |
| ------------ | --------- | --------- | ---------------- | --- | --- | --- | --- | ------ | --- |
|              |           |           | GGGM2(k)         |     |     |     |     | ∗ (θθˆ |     |
Bootstrap threshold: Note that is a standardized partial sum of g θ M2 ). When
i ,λ
| θθˆ |     |     |     | (θθˆ |     |     |     |     |     |
| --- | --- | --- | --- | ---- | --- | --- | --- | --- | --- |
θ is calculated from the training period, g∗ θ ) becomes a function of only x , with λ being
| M2  |     |     |     | i,λ | M2  |     |     | i   |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
given. Therefore, GGGM2(k)|θθˆ θ can be regarded as a function f(x ,x ,...,x |θθˆ θ ,λ).
|     |     | M2  |     |     |     | M2+1 | M2+2 | M2+k | M2  |
| --- | --- | --- | --- | --- | --- | ---- | ---- | ---- | --- |
Under the null hypothesis, we will implement a bootstrap method to sample from the stationary
timeseriesinthetrainingperiod, {x ,x ,x ,...,x }. Insertingthebootstrapsampledtimeseries
|     |     |     | 1 2 | 3   | M2  |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
GGGM2(k),
into the GGG function provides the empirical distribution of the quasi-score function and its
empirical quantiles become accessbile as bootstrap thresholds. There is an abundance of literature
of the bootstrap method on time series analysis (Bu¨hlmann, 2002; Politis, 2003). We will apply
the block bootstrap resampling approach with a random block length (Politis and Romano, 1994)
to obtain resampled time series for the monitoring period from the training period and summarize
GGGM2(k)|θθˆ
a distribution for θ M2 ,λ. The procedure is illustrated as follows: 1) Based on the training
period {x ,x ,...,x }, we implement the block bootstrap sampling method to collect the times
1 2 M2
series samples x∗ ,k = 1,2,...,b∗ = 1,2,...,n , of sample size, n , for the monitoring period
|     | (M2+k)b∗ |     |     |     | b   |     | b   |     |     |
| --- | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
as shown in Table 1. 2) Through insertion of the time series samples, we obtain the samples of
GM2(k),j = 1,2,...,d in the monitoring period, i.e, {GM2(k)},j = 1,2,...,d,b∗ = 1,2,...,n .
| j   |     |     |     |     | j,b∗ |     |     |     | b   |
| --- | --- | --- | --- | --- | ---- | --- | --- | --- | --- |
25

(cid:97)
(cid:97)
|     |     |     | (cid:97)          | B                |     |             |         |                 |     |         |     |     |
| --- | --- | --- | ----------------- | ---------------- | --- | ----------- | ------- | --------------- | --- | ------- | --- | --- |
|     |     |     | (cid:97) (cid:97) |                  | 1   | 2           |         | 3               | ... | n       |     |     |
|     |     | t   |                   | (cid:97)(cid:97) |     |             |         |                 |     | b       |     |     |
|     |     |     |                   | x∗               |     | x∗          | x∗      |                 |     | x∗      |     |     |
|     |     | M   | 2 +1              |                  |     |             |         |                 | ... |         |     |     |
|     |     |     |                   | (M2+1)1          |     | (M2+1)2     | (M2+1)3 |                 |     | (M2+1)n | b   |     |
|     |     |     |                   | x∗               |     | x∗          | x∗      |                 |     | x∗      |     |     |
|     |     | M   | 2 +2              |                  |     |             |         |                 | ... |         |     |     |
|     |     |     |                   | (M2+2)1          |     | (M2+2)2     | (M2+2)3 |                 |     | (M2+2)n | b   |     |
|     |     |     |                   | x∗               |     | x∗          | x∗      |                 |     | x∗      |     |     |
|     |     | M   | 2 +3              |                  |     |             |         |                 | ... |         |     |     |
|     |     |     |                   | (M2+3)1          |     | (M2+3)2     | (M2+3)3 |                 |     | (M2+3)n |     |     |
|     |     |     |                   | x∗               |     | x∗          | x∗      |                 |     | x∗      | b   |     |
|     |     | M   | +4                |                  |     |             |         |                 | ... |         |     |     |
|     |     |     | 2                 | (M2+4)1          |     | (M2+4)2     | (M2+4)3 |                 |     | (M2+4)n |     |     |
|     |     |     |                   | x∗               |     | x∗          | x∗      |                 |     | x∗      | b   |     |
|     |     | M   | +5                |                  |     |             |         |                 | ... |         |     |     |
|     |     |     | 2                 | (M2+5)1          |     | (M2+5)2     | (M2+5)3 |                 |     | (M2+5)n |     |     |
|     |     |     | .                 |                  | .   | .           |         | .               | .   | .       | b   |     |
|     |     |     | .                 |                  | .   | .           |         | .               | .   | .       |     |     |
|     |     |     | .                 |                  | .   | .           |         | .               | .   | .       |     |     |
|     |     |     |                   | x∗               |     | x∗          | x∗      |                 |     | x∗      |     |     |
|     |     | M   | 2 +k              |                  |     |             |         |                 | ... |         |     |     |
|     |     |     |                   | (M2+k)1          |     | (M2+k)2     | (M2+k)3 |                 |     | (M2+k)n | b   |     |
|     |     |     | .                 |                  | .   | .           |         | .               | .   | .       |     |     |
|     |     |     | .                 |                  | .   | .           |         | .               | .   | .       |     |     |
|     |     |     | .                 |                  | .   | .           |         | .               | .   | .       |     |     |
|     |     |     | Table             | 1: Sampled       |     | time series | from    | block bootstrap |     |         |     |     |
See Table 2. 3) The bootstrap threshold, T (k) at time t = M +k, can be evaluated as the
|     |     |     |     |     |     | α,j,B |     |     | 2   |     |     |     |
| --- | --- | --- | --- | --- | --- | ----- | --- | --- | --- | --- | --- | --- |
GM2(k),j
| empirical | α-quantile |     | of  | =   | 1,2,...,d. |     |     |     |     |     |     |     |
| --------- | ---------- | --- | --- | --- | ---------- | --- | --- | --- | --- | --- | --- | --- |
j
(cid:97)
|     | (cid:97) (cid:97) |     |     |     |     |     |     |     |     |     |     |     |
| --- | ----------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|     | (cid:97)          | j   | 1   |     |     | 2   |     | 3   |     | ... | d   |     |
| k   | (cid:97)          |     |     |     |     |     |     |     |     |     |     |     |
(cid:97)(cid:97)
1 {GM2 (1)}b∗=n b {GM2 (1)}b∗=n b {GM2 (1)}b∗=n b ... {GM2 (1)}b∗=n b
|     |     |      | 1,b∗     | b∗=1 | 2,b∗ | b∗=1     |        | 3,b∗     | b∗=1 |     | d,b∗          | b∗=1 |
| --- | --- | ---- | -------- | ---- | ---- | -------- | ------ | -------- | ---- | --- | ------------- | ---- |
|     |     | {GM2 | (2)}b∗=n |      | {GM2 | (2)}b∗=n | {GM2   | (2)}b∗=n |      |     | {GM2 (2)}b∗=n |      |
|     | 2   |      |          | b    |      |          | b      |          | b    | ... |               | b    |
|     |     |      | 1,b∗     | b∗=1 | 2,b∗ | b∗=1     |        | 3,b∗     | b∗=1 |     | d,b∗          | b∗=1 |
|     |     | {GM2 | (3)}b∗=n |      | {GM2 | (3)}b∗=n | {GM2   | (3)}b∗=n |      |     | {GM2 (3)}b∗=n |      |
|     | 3   |      |          | b    |      |          | b      |          | b    | ... |               | b    |
|     |     |      | 1,b∗     | b∗=1 | 2,b∗ | b∗=1     |        | 3,b∗     | b∗=1 |     | d,b∗          | b∗=1 |
|     |     | {GM2 | (4)}b∗=n |      | {GM2 | (4)}b∗=n | {GM2   | (4)}b∗=n |      |     | {GM2 (4)}b∗=n |      |
|     | 4   |      |          | b    |      |          | b      |          | b    | ... |               | b    |
|     |     |      | 1,b∗     | b∗=1 | 2,b∗ | b∗=1     |        | 3,b∗     | b∗=1 |     | d,b∗          | b∗=1 |
|     |     |      | (5)}b∗=n |      |      | (5)}b∗=n |        | (5)}b∗=n |      |     | (5)}b∗=n      |      |
|     | 5   | {GM2 |          | b    | {GM2 |          | b {GM2 |          | b    | ... | {GM2          | b    |
|     |     |      | 1,b∗     | b∗=1 | 2,b∗ | b∗=1     |        | 3,b∗     | b∗=1 |     | d,b∗          | b∗=1 |
|     | . . |      | . .      |      |      | . .      |        | . .      |      |     | . .           |      |
|     | .   |      | .        |      |      | .        |        | .        |      |     | .             |      |
|     |     | {GM2 | (k)}b∗=n |      | {GM2 | (k)}b∗=n | {GM2   | (k)}b∗=n |      | ... | {GM2 (k)}b∗=n |      |
|     | k   |      |          | b    |      |          | b      |          | b    |     |               | b    |
|     |     |      | 1,b∗     | b∗=1 | 2,b∗ | b∗=1     |        | 3,b∗     | b∗=1 |     | d,b∗          | b∗=1 |
|     | .   |      | .        |      |      | .        |        | .        |      |     | .             |      |
|     | .   |      | .        |      |      | .        |        | .        |      |     | .             |      |
|     | .   |      | .        |      |      | .        |        | .        |      |     | .             |      |
Table 2: Detector statistics computed from resampled time series from block bootstrap
Mahalanobis distance threshold: In the computation of the bootstrap threshold proce-
dure above, there is one concern when we collect the bootstrap samples for the j-th parameter,
{GM2(k)}b∗=n
b,j = 1,2,...,d, at time point M + k. Due to the correlation among the vec-
| j,b∗ | b∗=1 |     |     |     |     |     | 2   |     |     |     |     |     |
| ---- | ---- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
tor GGGM2(k) known as the spillover effect, the computation of bootstrap threshold for individual
GM2(k)
doesn’t take this correlation structure into account, and results in a conservative threshold
j
from individual {GM2(k)} independently. To remedy the lack of association among the individ-
j,b∗
ual bootstrap thresholds, we will use a Mahalanobis distance based threshold to incorporate the
spillover effect within the detector statistics GGGM2(k). We regard the bootstrap samples of the
vectors {(GM2 (k),GM2 (k),...,GM2 (k))′}b∗=n b as the empirical multivariate distribution of the
|     | 1,b∗ |     | 2,b∗ | d,b∗ |     | b∗=1 |     |     |     |     |     |     |
| --- | ---- | --- | ---- | ---- | --- | ---- | --- | --- | --- | --- | --- | --- |
26

detector statisticGGGM2(k) at monitoring timestamp M +k and compute the Mahalanobis distance
2
(Aggarwal, 2017). The Mahalanobis distance threshold can be found in the following steps,
Step 1 At time stamp t= M 2 + k, collect bootstrap samples of the vector of detector statistics
|     | {GGGM2(k)}b∗=n |         | {(GM2 | (k),GM2 | (k),...,GM2 |      | (k))T}b∗=n |      |     |     |     |     |     |
| --- | -------------- | ------- | ----- | ------- | ----------- | ---- | ---------- | ---- | --- | --- | --- | --- | --- |
|     |                |         | b =   |         |             |      |            |      | b.  |     |     |     |     |
|     |                | b∗ b∗=1 |       | 1,b∗    | 2,b∗        | d,b∗ |            | b∗=1 |     |     |     |     |     |
{GGGM2(k)}b∗=n
Step 2 Compute the sample mean µµµ and the sample covariance matrix SSS of b, and
|     |     |     |     | GGG |     |     |     |     |     | GGG | b∗  | b∗=1 |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---- | --- |
usethemtoapproximatepopulationmeanandcovariancematrixoftheempiricalmultivariate
GGGM2(k).
|      | distribution | for |         |             |           |     |      |               |     |     |                      |     |     |
| ---- | ------------ | --- | ------- | ----------- | --------- | --- | ---- | ------------- | --- | --- | -------------------- | --- | --- |
|      |              |     |         |             |           |     |      | (GGGM2(k)−µµµ |     |     | )TSSS−1(GGGM2(k)−µµµ |     |     |
| Step | 3 Compute    | the | squared | Mahalanobis | distances | d2  | (k)  | =             |     |     |                      |     | ),  |
|      |              |     |         |             |           |     | M,b∗ |               | b∗  | GGG | GGG                  | b∗  | GGG |
where GGGM2(k) is the vector of detector statistics on the b∗-th bootstrap sample time series.
b∗
(k)}b∗=n
Step 4 Compute the desired quantile, e.g, the 95% quantile, from {d2 b to compare with
|     |     |     |     |     |     |     |     |     | M,b∗ | b∗=1 |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ---- | ---- | --- | --- | --- |
theobservedMahalanobisdistanced2 (GGGM2(k)−µµµ )TSSS−1(GGGM2(k)−µµµ )whereGGGM2(k)
|     |     |     |     |     | (k) | =   |     | GGG |     |     | GGG |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|     |     |     |     |     | M   |     | obs |     | GGG | obs |     |     | obs |
is the observed detector statistic at M +k computed from the real-time data stream in the
2
|     | monitoring | period. |     |     |     |     |     |     |     |     |     |     |     |
| --- | ---------- | ------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Remark: We opt for the empirical threshold of the Mahalanobis distance instead of using a
Chi-square distribution quantile as an approximation, because the normality assumption for the
multivariate bootstrap samples is not always satisfied in real applications. See Figure 1 and 2 from
a single realization example of some simulated time series for illustration. We note that not all
the marginal bivariate distributions have the characteristics of bivariate Gaussian. We can also
see that when the monitoring period (starting at M +1 = 2501) is before the true break point
2
τ = 3500, the observed detector statistics GM2(k) fall within the clusters of bootstrap samples of
j
GM2(k).
However, when the monitoring process is past the true break point τ = 3500, some of the
j,b∗
|     |     |     |     | GM2(k) |     |     |     |     |     |     |     | GM2(k). |     |
| --- | --- | --- | --- | ------ | --- | --- | --- | --- | --- | --- | --- | ------- | --- |
observed detector statistics will deviate from the clusters of bootstrap samples of
|     |     |     |     | j   |     |     |     |     |     |     |     |     | j,b∗ |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---- |
The Mahalanobis distance takes the observed vector detector statistic as an entirety to detect the
| outlier | at  | a multi-dimensional |           | level. |     |     |     |     |     |     |     |     |     |
| ------- | --- | ------------------- | --------- | ------ | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2.3.5   |     | Ensemble            | detection |        |     |     |     |     |     |     |     |     |     |
2.3.5.1 Motivation of ensemble detection We’ve listed three types of thresholds for hy-
| pothesis |     | testing and | each type | of threshold | has | its own | pros | and | cons. |     |     |     |     |
| -------- | --- | ----------- | --------- | ------------ | --- | ------- | ---- | --- | ----- | --- | --- | --- | --- |
27

G_omega
001
04
0
08
04
0
0 40 80
051
05
0 40 80 120 0 40 80 50 100150200
G_alpha1
G_alpha2
G_alpha3
G_alpha4
0 50 100 150 0 50100
08
04
0
051
05
0
001
0
G_alpha5
Figure 1: Scatter plot of detector statistics at time stamp M +k =3000 when τ =3500. The red dots are
2
observed detector statistic and black dots are bootstrap samples of the detector statistics
G_omega
002
001
0
052
001
0
0 50 150
053
002
0 50 150 0 100 200 200 300 400
G_alpha1
G_alpha2
G_alpha3
G_alpha4
100 300 200 300 400
002
001
0
003
001
053
002
G_alpha5
Figure 2: Scatter plot of detector statistics at time stamp M +k =4000 when τ =3500. The red dots are
2
observed detector statistic and black dots are bootstrap samples of the detector statistics
1. Wiener process thresholds are convenient for quick computation and have a good control of
the type I error at the onset of the monitoring period but it can be quickly exceeded by the
detector statistics in the absence of a structural break.
2. Bootstrap thresholds are conservative and provide delayed detection of structural break due
to the lack of the consideration for the correlation among the individual detector statistics
GM2(k).
j
3. Mahalanobis distance threshold is able to account for the correlation among the individual
detector statistics. However, the distribution of Mahalanobis distance has a centroid and
spread approximated by bootstrap sample mean vector and covariance matrix. Using thresh-
28

olds biased by sample outliers will impact the accuracy of break point detection performance.
To improve the overall performance of detection, we propose an ensemble detection scheme
to combine the three aforementioned thresholds in a unified framework. By consolidating all the
advantagesofthethreemethods,weaimtomaintainahighpowerofdetectionwithawell-controlled
type I error. Prior to a detailed description of our method, we would like to clarify the objectives
of handling type I error and delay of detection in online financial duration time series.
Type I error: In the context of break point detection, the type I error is false detection before
the true break point, which means the break point is incorrectly declared while the structure of
the time series still remains identical to the training period. The type I error can be related to
several cases: 1) The detection scheme is too sensitive to noise in the monitoring period. 2) The
stationarity of the time series before the true break point doesn’t hold. 3) The monitoring period
is too long before the true break point occurs, so the accumulative noise in the long monitoring
period eventually drives the detector statistic to pass the threshold. Our ensemble scheme can
make adaptations to the extreme fluctuation in the first case scenario whereas the other two cases
raise concerns for general online methods. For this research, our ensemble scheme will provide a
viable solution to address the type I error issue.
Delay: The most ideal performance of any detection methods will declare a change point as
soon as the structure of the time series changes. We can achieve quick and accurate detection when
there is a dramatic change or jump at the break point. In general, for a mixture of signal and
noise in the time series, its signal-to-noise ratio determines the speed of a break point detection.
The bootstrap threshold is based upon the resampled time series from the training period, so data
fromadifferentgeneratingprocesswilleventuallytriggerthebootstrapthresholdinthemonitoring
period. Due to the irregularity of the duration time series in our study, the delay between detection
and actual change points differs from real calendar time difference. For example, if the true break
is τ = 3500 and the detected break point is τˆ = 3700, the time index lag is 200 but the calculation
of real delay is D =
(cid:80)τˆ
x = x +x +···+x , which is data dependent. See Figure
delay i=τ i 3501 3502 3700
3. In real applications, when the market is active and trading intensity is high, the online financial
durations are observed in small values with high frequency, if the average durations between events
are roughly 0.1 seconds, the delay of 200 durations will result in a 20-second delay in the real
29

calendar time. Similarly, the trading intensity shifts from high to low, the delay in calendar time
canbelongerbutthistypeoftransitionofthefinancialdurationsareoflessinteresttothedecision-
| makers | and | delay | can | be more tolerable. |     |     |     |
| ------ | --- | ----- | --- | ------------------ | --- | --- | --- |
7.5
col
Before Break
|     |     |     |     | 5.0 |     |     | True Break   |
| --- | --- | --- | --- | --- | --- | --- | ------------ |
|     |     |     |     | y   |     |     | Delay Period |
Estimated Break
After Detection
2.5
0.0
|     |     |     |     | 0   | 2500 5000 | 7500 |     |
| --- | --- | --- | --- | --- | --------- | ---- | --- |
time
Figure 3:
The trace plot of duration of duration in the calendar time. The x-axis is calendar time (in seconds).
The y-axis denotes the value of duration. The lag between time indices of true break and detected break is 200 and
| the | delay time | in  | the calendar | time is 261.1051 | s.  |     |     |
| --- | ---------- | --- | ------------ | ---------------- | --- | --- | --- |
2.3.5.2 Ensemble detection scheme This detection scheme is described as a pseudo algo-
rithm below. The break point alarms are recorded in a sequence of δ(k),k = 1,2,....
| Algorithm |     | E-PEF | detection |     |     |     |     |
| --------- | --- | ----- | --------- | --- | --- | --- | --- |
| Input:    | {x  | }∞    |           |     |     |     |     |
k k=M2+1
| Output: |     | {δ(k)}∞ |     |     |     |     |     |
| ------- | --- | ------- | --- | --- | --- | --- | --- |
k=M2+1
Compute observed GGGM2(k), Mahalanobis distance d2 (k). Find out the corresponding thresh-
M
obs
olds, d2 (k), {T (k)} and {T (k),T (k)},j = 1,2,...,d, through the
|           |     | 1−αM    |               | 1−αW,W | αB/2,j,B | 1−αB/2,j,B |     |
| --------- | --- | ------- | ------------- | ------ | -------- | ---------- | --- |
| bootstrap |     | samples | respectively. |        |          |            |     |
if d2 (k) > d2 (k) and ∃j ∈ {1,...,d},s.t,I(|GM2(k)| > T (k)) = 1 and
1−αW,W
|     | M        |      | 1−αM     |              |              |     | j   |
| --- | -------- | ---- | -------- | ------------ | ------------ | --- | --- |
|     | (cid:16) |      |          |              | (cid:17)     |     |     |
| I   | T        | (k)  | < GM2(k) | < T          | (k) = 0 then |     |     |
|     | αB/2,j,B |      |          | j 1−αB/2,j,B |              |     |     |
|     | δ(k)     | = 1, | k ← k+1  |              |              |     |     |
else
|     | δ(k) | = 0, | k ← k+1 |     |     |     |     |
| --- | ---- | ---- | ------- | --- | --- | --- | --- |
end if
Remarks:
1. As mentioned before, the reason of using bootstrap threshold of Mahalanobis distance is
that the asymptotic normality of the GGGM2(k) may not be a valid assumption, although each
individual GM2(k) preserves a roughly symmetric and bell-shaped distribution. The critical
j
30

valueofaChi-squareddistributionwillgivealowerthresholdcomparingwithaheavier-tailed
distribution.
2. StructrualbreakatM +k willbedeclaredonlywhenboththeobservedMahalanobisdistance
2
d2 (k) exceeds the Mahalanobis distance threshold d2 , and at least one of the individual
M 1−αM
GM2(k) exceeds its Wierner process and bootstrap thresholds.
j
3. The algorithm contains multiple hypothesis testings, we take the Bonferroni’s method to
control the overall false discovery rate.
To have a detailed illustration of the type I error rate from the aforementioned algorithm, we
denote the following events at monitoring time t = M +k:
2
• A(k) : d2 (k) > d2 (k)
M 1−αM
(cid:16) (cid:17)
• B (k) : I(|GM2(k)| > T (k))· 1−I(T (k) < GM2(k) < T (k)) = 1 1
j j 1−αW,W αB/2,j,B j 1−αB/2,j,B
We use δ(k) to denote the break point detection indicator at t = M +k. Then the theoretical
2
type I error under the null hypothesis of no break point can be derived and controlled as:
 
d d
 (cid:92) (cid:91)  (cid:91)
Pr(δ(k) = 1|H ) = Pr A(k) { B (k)}H < P(A(k)|H )+P( B (k)|H )
0 j 0 0 j 0
 
j=1 j=1
d
(cid:88)
≤ α + P(B (k)|H )
M j 0
j=1
d
(cid:88)(cid:16) (cid:17)
≤ α + P({|GM2(k)| > T (k)}∩{T (k) < GM2(k) < T (k)}c)
M j 1−αW,W 1−αB/2,j j αB/2,j
j=1
d
(cid:88)
≤ α + (α +α ) = α +d·α +d·α (2.19)
M W B M W B
j=1
From E.q (2.19), we can control the type I error by choosing the proper α , α , and α . In
M W B
the simulation study, we set α = d·α = d·α = α /3 to control the type I error under
M W B overall
α = 0.05. Given the motivation and theoretical support, the performance of our E-PEF
overall
method will be evaluated in the next subsections.
1I(.) is the indicator of an event.
31

| 2.4 Numerical | study |     |     |     |     |     |
| ------------- | ----- | --- | --- | --- | --- | --- |
In this section, the performance of E-PEF method is evaluated through extensive simulation study.
Some empirical guidelines can be provided for practical implementation. The real application of
E-PEF method is demonstrated through monitoring inter-trade duration time series from WRDS
| Trade and Quote | data. |     |     |     |     |     |
| --------------- | ----- | --- | --- | --- | --- | --- |
2.4.1 Simulation
For simulation studies,we will demonstrate E-PEF method through three different aspects. The
firstaspectaddressesthecommonlimitationofonlinedetectionstudies, i.e., thefalsedetectionrate
control can only be controlled within a finite monitoring window. We also show this feature of our
method. Second aspect deals with the operating characteristics in terms of detection probabilities
for different structural breaks. The detection probabilities is regarded as false detection (type I
error) rate before the true break, and detection power after the true break. The last aspect is
associated with real application. We will show the robustness of E-PEF method when the data is
non-stationary to address the non-stationarity concern for the real data.
| The simulations | are based | upon | the following | model: |     |     |
| --------------- | --------- | ---- | ------------- | ------ | --- | --- |
(j)
(j) ϵ
|     |     |     | x = exp(ψ | ) i , |     | (2.20) |
| --- | --- | --- | --------- | ----- | --- | ------ |
|     |     |     | i         | i (j) |     |        |
µ
ϵ
where
|     |       |         | pj         | qj       |                     |        |
| --- | ----- | ------- | ---------- | -------- | ------------------- | ------ |
|     |       |         | (cid:88)   | (cid:88) |                     |        |
|     | ψ (j) | = ω(j)+ | α (j) logx | + β      | (j) ψ (j) ,j = 1,2, | (2.21) |
|     | i     |         |            | i−k      |                     |        |
|     |       |         | k          |          | k i−k               |        |
|     |       |         | k=1        | k=1      |                     |        |
j = 1 is the model before the true break point τ and j = 2 is the model after the true break
point.
To illustrate the performance of our algorithm, we apply our method according to different
types of the model alteration. Below are the results for the ensemble detection outcomes for the
four scenarios of 500 simulations with different true break points (τ = 2700,3000,3500,4000). The
tuning parameter λ is determined by grid search. Among a list of λ candidates from 0.1 to 100, we
selectthemodelwiththesmallestMeanAbsoluteDeviationmeasure,i.e,MAD = 1 (cid:80)M2 |x −xˆ |.
i=1 i i
M2
| Then we conduct | the E-PEF | method | upon the | model of our | choice. |     |
| --------------- | --------- | ------ | -------- | ------------ | ------- | --- |
32

Scenario 1:


|  0.2+0.1logx |     | +0.2logx |     | , 1 | < i ≤ τ |     |
| -------------- | --- | -------- | --- | --- | ------- | --- |
|                |     | i−1      |     | i−2 |         |     |
ψ =
i
|                  |     |              |           |         |               | (2.22) |
| ------------------ | --- | ------------ | --------- | ------- | ------------- | ------ |
| 0.2+0.1logx       |     | i−1 +0.5logx |           | i−2 , τ | +1 ≤ i ≤ 7500 |        |
| ϵ ∼ Weibull(.6,.7) |     | for both     | segments. |         |               |        |
Scenario 2:


|     |  0.2+0.1logx |     | ,   | 1 < i ≤ | τ   |     |
| --- | -------------- | --- | --- | ------- | --- | --- |
i−1
ψ =
i

|     |  0.2+0.4logx |     | ,   | τ +1 ≤ | i ≤ 7500 | (2.23) |
| --- | -------------- | --- | --- | ------ | -------- | ------ |
i−1
| ϵ   | ∼ Gamma(.5,.5) | for | both | segments. |     |     |
| --- | -------------- | --- | ---- | --------- | --- | --- |
Scenario 3:


|  0.2+0.1logx |     | i−1 +0.2ψ | i−1 | , 1 | < i ≤ τ |     |
| -------------- | --- | --------- | --- | --- | ------- | --- |
ψ =
i
|                 |     |          |           |     |               | (2.24) |
| ---------------- | --- | -------- | --------- | --- | ------------- | ------ |
|  0.2+0.1logx   |     | +0.5logx |           | , τ | +1 ≤ i ≤ 7500 |        |
|                  |     | i−1      |           | i−2 |               |        |
| ϵ ∼ Gamma(.5,.5) |     | for both | segments. |     |               |        |
Scenario 4:

|   0.6+0.1logx |     | +0.2logx |     | , 1 | < i ≤ τ |     |
| ---------------- | --- | -------- | --- | --- | ------- | --- |
|                  |     | i−1      |     | i−2 |         |     |
ψ i =
|                  |     |              |           |         |               | (2.25) |
| ------------------ | --- | ------------ | --------- | ------- | ------------- | ------ |
| 0.2+0.1logx       |     | i−1 +0.2logx |           | i−2 , τ | +1 ≤ i ≤ 7500 |        |
| ϵ ∼ Weibull(.8,.9) |     | for both     | segments. |         |               |        |
For Scenarios 1 and 2, transitions before and after the break point are only based upon one of
the AR coefficients within the log ACD framework of the same order. The different distributions
(Weibull and Gamma distributions) assigned on the innovations are used to justify the robustness
of our algorithm. Scenario 3 shows that when the model framework changes from an ARMA model
to an AR model, our method is also able to detect the change point in a timely manner. We
use Scenario 4 to mimic some of real data scenarios where the durations change from a long and
infrequent pattern to a short and volatile state, which is similar to the market with increasing
33

trading intensity. We select a higher intercept before the structural break point and a lower one
afterwards.
2.4.1.1 Monitoring horizon We first investigate the performance of E-PEF detection under
the circumstance of no break for different scenarios. We also implement our method using different
sizes of training data. Monitoring horizon (Berkes et al., 2004) stands for the maximum length
of the monitoring window if there is no structural break in the data generating process, i.e., the
detectionprobabilityisbelowthedesiredfalsedetection(typeIerror)rateundertheH ofnobreak
0
point in the data. Therefore, as long as there is no structural break detected within the monitoring
horizon, practitioner can use the ongoing time series model to make statistical inference, with the
confidence that the parameters of the current model remain stable. However, extended monitoring
period beyond the monitoring horizon will inflate the false detection rate because cumulative noise
from the prolonged monitoring distorts the structural break detection. The monitoring horizon is
summarized in Table 3.
There are three main takeaways in the table, 1) the false detection rate can only be controlled
under a desired level within a monitoring window of finite length. Longer monitoring period leads
to a greater inflation of false detection rate, though the false detection rate increases slowly as the
monitoring window length increases. 2) a longer training period tends to prolong the monitoring
horizoningeneral, exceptforsometinyfluctuationinthedetectionprobabilityatdifferentk, which
is caused by the randomness for the bootstrap sampling. 3) As an empirical guidance for choosing
a practical length of monitoring period, a monitoring window of length 250-500 is preferred for a
desiredfalsedetectionratecontrolwhenthetrainingdataissmall(M < 2500), whilepractitioners
2
canexpectalongermonitoringhorizonofabout750-1000ifM ≥ 2500. Furthertrade-offsbetween
2
false detection rate and power will also influence the monitoring window, according to specific
demands from the practitioners.
In addition, it can be observed in Table 3 that ARMA framework (Scenario 3) as a data
generating process is more robust against false detection, so it has a longer monitoring horizon.
That means approximation using a high-order AR model works better when the online data are
generated under an ARMA framework than under a low-order AR framework.
34

Scenarios M (k =) 250 500 750 1000 1250 1500 1750 2000 2250 2500
2
2000 0.004 0.018 0.03 0.024 0.03 0.034 0.054 0.06 0.072 0.078
2500 0.012 0.008 0.014 0.022 0.026 0.032 0.04 0.044 0.058 0.062
1
3000 0.01 0.016 0.016 0.014 0.016 0.03 0.026 0.026 0.034 0.042
3500 0.006 0.014 0.018 0.024 0.02 0.026 0.026 0.03 0.046 0.052
2000 0.004 0.014 0.018 0.034 0.04 0.046 0.072 0.082 0.088 0.102
2500 0.006 0.016 0.022 0.026 0.034 0.036 0.042 0.044 0.06 0.08
2
3000 0 0.022 0.022 0.026 0.03 0.032 0.044 0.046 0.058 0.07
3500 0.016 0.01 0.012 0.012 0.014 0.02 0.026 0.038 0.054 0.048
2000 0.006 0.02 0.028 0.036 0.04 0.056 0.086 0.092 0.102 0.116
2500 0.012 0.016 0.018 0.028 0.038 0.046 0.052 0.052 0.058 0.064
3
3000 0.006 0.008 0.024 0.018 0.028 0.034 0.038 0.04 0.044 0.054
3500 0.016 0.014 0.022 0.022 0.026 0.026 0.036 0.032 0.038 0.038
2000 0.028 0.036 0.034 0.048 0.064 0.066 0.076 0.074 0.086 0.098
2500 0.012 0.02 0.038 0.026 0.03 0.038 0.046 0.062 0.064 0.084
4
3000 0.01 0.016 0.018 0.022 0.03 0.024 0.036 0.044 0.054 0.046
3500 0.01 0.014 0.016 0.012 0.02 0.024 0.032 0.044 0.056 0.068
Table 3: Detection probabilities in the monitoring horizon study. M is the length of training
2
period. k is the monitoring time point in the monitoring period after the training. The false
detection rate control α = 0.05.
2.4.1.2 Detection probability and Delay According to the result from monitoring horizon
summary, we choose the training period to be M = 2500, with the burn-in period M = 1500
2 1
for the detection simulation study. The performance of E-PEF is presented through two measures,
1) detection probabilities at different monitoring times. The false detection and power refer to
the detection probabilities before and after the true break points correspondingly. 2) Summary
statistics of average delay. Average delay reflects the sensitivity of the detection algorithm after
the occurrence of a structural break. These results are exhibited in Table 4 and Table 5.
From Table 4, E-PEF controls the false detection rate under the nominal level, α = 0.05 and
increases the detection power rapidly after the true structural breaks occur in the monitoring pro-
cedure. The E-PEF method has an overall satisfactory performance of detection, and a significant
detection power can be expected when there is a structural break involved with framework change,
e.g., from ARMA to AR in scenario 3. Detection power spikes up to 1 in a short period.
From Table 5, E-PEF method has different sensitivity levels for the different kinds of structural
breaks. For Scenario 1, 2, and 4, parameter changes within the same AR framework are detected
slower than the framework changes as in Scenario 3. In scenario 4, belated true break associated
35

Scenarios τ (M +k =) 2750 3000 3250 3500 3750 4000 4250 4500 4750 5000
2
|     | 2700 | 0.02  | 0.636 0.962 | 0.99 1      | 1 1 | 1 1 | 1   |
| --- | ---- | ----- | ----------- | ----------- | --- | --- | --- |
|     | 3000 | 0.012 | 0.014 0.324 | 0.854 0.982 | 1 1 | 1 1 | 1   |
1
|     | 3500 | 0.01  | 0.012 0.012 | 0.018 0.228 | 0.724 0.932 | 0.982 0.998 | 1     |
| --- | ---- | ----- | ----------- | ----------- | ----------- | ----------- | ----- |
|     | 4000 | 0.012 | 0.008 0.006 | 0.026 0.02  | 0.03 0.2    | 0.59 0.876  | 0.968 |
|     | 2700 | 0.02  | 0.548 0.924 | 0.98 0.998  | 1 1         | 1 1         | 1     |
|     | 3000 | 0.006 | 0.016 0.192 | 0.724 0.922 | 0.978 1     | 0.998 1     | 1     |
2
3500 0.006 0.018 0.02 0.028 0.134 0.492 0.812 0.936 0.986 0.994
4000 0.004 0.018 0.024 0.036 0.036 0.046 0.132 0.368 0.698 0.87
|     | 2700 | 0.06 | 0.996 1     | 1 1 | 1 1 | 1 1 | 1   |
| --- | ---- | ---- | ----------- | --- | --- | --- | --- |
|     | 3000 | 0.01 | 0.012 0.882 | 1 1 | 1 1 | 1 1 | 1   |
3
|     | 3500 | 0.01  | 0.014 0.02  | 0.028 0.636 | 0.998 1     | 1 1         | 1   |
| --- | ---- | ----- | ----------- | ----------- | ----------- | ----------- | --- |
|     | 4000 | 0.01  | 0.012 0.02  | 0.024 0.044 | 0.042 0.486 | 0.952 0.998 | 1   |
|     | 2700 | 0.008 | 0.442 0.918 | 0.996 1     | 1 1         | 1 1         | 1   |
|     | 3000 | 0.012 | 0.026 0.184 | 0.686 0.946 | 0.998 1     | 1 1         | 1   |
4
|     | 3500 | 0.014 | 0.022 0.034 | 0.026 0.152 | 0.538 0.844 | 0.962 0.994 | 1   |
| --- | ---- | ----- | ----------- | ----------- | ----------- | ----------- | --- |
4000 0.014 0.02 0.028 0.028 0.032 0.038 0.13 0.442 0.746 0.924
Table 4: Detection probabilities at different monitoring time under different scenarios. τ is the true
| break point. | k is the monitoring | time | point in the | monitoring period. |     |     |     |
| ------------ | ------------------- | ---- | ------------ | ------------------ | --- | --- | --- |
with a prolonged monitoring period, tends to give more false detection. For the application of
E-PEF, the delay in calendar time is data-dependent, so its conversion from the delay in the
time index doesn’t demonstrate the timeliness of the E-PEF detection without the summation
of durations between true break and the detected break. On the other hand, detection of minor
parameterchangeswithinthesameframeworktakesmorestreamingdataforsufficientevidencebut
the consequence of drawing inference from a slightly biased model is not too grave if practitioners
are just using the same model framework with subtle differences between the parameters. Since
our method has a high sensitivity to the model framework change, timely parameters update can
| be made | at the occurrence | of such significant | structural | breaks. |     |     |     |
| ------- | ----------------- | ------------------- | ---------- | ------- | --- | --- | --- |
2.4.1.3 Robust performance for non-stationary scenarios Since E-PEF method involves
stationary log ACD models, it is difficult for data in real application to abide by the stationarity
assumption. Therefore, we will demonstrate the robust performance of E-PEF method for non-
stationary data. Although non-stationary data can come in various forms, local non-stationarity
can be still described by a linear trend of quadratic trend. For a small size of monitoring horizon in
36

|     | Scenarios | τ    | (Delay) Mean | SD     | Min | Q1    | Q2    | Q3     | Max |
| --- | --------- | ---- | ------------ | ------ | --- | ----- | ----- | ------ | --- |
|     |           | 2700 | 264.61       | 126.30 | 97  | 173.5 | 240   | 328.25 | 825 |
|     |           | 3000 | 326.45       | 159.08 | 109 | 211.5 | 301.5 | 412.75 | 943 |
1
|     |     | 3500 | 391.14 | 200.63 | 71  | 251.75 | 372   | 501.25 | 1257 |
| --- | --- | ---- | ------ | ------ | --- | ------ | ----- | ------ | ---- |
|     |     | 4000 | 445.36 | 245.48 | 65  | 269.75 | 424   | 585.25 | 1368 |
|     |     | 2700 | 294.25 | 147.70 | 106 | 185.75 | 266.5 | 372.25 | 1167 |
|     |     | 3000 | 387.09 | 184.97 | 135 | 251    | 359   | 485.75 | 1191 |
2
|     |     | 3500 | 511.92 | 261.74 | 136 | 325.75 | 480.5 | 656    | 1780 |
| --- | --- | ---- | ------ | ------ | --- | ------ | ----- | ------ | ---- |
|     |     | 4000 | 570.34 | 312.38 | 82  | 332    | 545.5 | 749    | 1685 |
|     |     | 2700 | 116.46 | 49.02  | 48  | 82     | 109   | 143    | 325  |
|     |     | 3000 | 162.77 | 72.36  | 60  | 109    | 153.5 | 206.25 | 463  |
3
|     |     | 3500 | 214.87 | 96.01  | 63  | 140.5 | 202   | 283.25 | 548  |
| --- | --- | ---- | ------ | ------ | --- | ----- | ----- | ------ | ---- |
|     |     | 4000 | 249.72 | 118.72 | 37  | 167   | 247.5 | 327    | 651  |
|     |     | 2700 | 329.49 | 141.60 | 131 | 221   | 309   | 422    | 900  |
|     |     | 3000 | 411.03 | 182.23 | 130 | 278.5 | 390   | 531.25 | 1032 |
4
|     |     | 3500 | 490.85 | 242.63 | 117 | 311.25 | 459   | 643.25 | 1344 |
| --- | --- | ---- | ------ | ------ | --- | ------ | ----- | ------ | ---- |
|     |     | 4000 | 561.95 | 287.58 | 142 | 341.75 | 519.5 | 743    | 1596 |
Table 5: Summary statistics of average delay under different scenarios for different break points. τ
is the true break point. False detection rate control is α = 0.05. The length of training period is
M = 2500.
2
practice, it will sufficient to display the robust performance of E-PEF against non-stationary data
| with | a linear trend | or quadratic | trend. |     |     |     |     |     |     |
| ---- | -------------- | ------------ | ------ | --- | --- | --- | --- | --- | --- |
The linear time trend and quadratic time trend are introduced in both segments before and
| after    | the structural | breaks as | follows, |     |     |     |     |     |     |
| -------- | -------------- | --------- | -------- | --- | --- | --- | --- | --- | --- |
| Scenario | 1:             |           |          |     |     |     |     |     |     |


|     |     |  0.2+0.05log(i)+0.1logx |     |     | i−1 +0.2logx | i−2 , | 1 < | i ≤ τ |     |
| --- | --- | ------------------------- | --- | --- | ------------ | ----- | --- | ----- | --- |
ψ =
i
|     |     |                          |          |           |          |     |      |            | (2.26) |
| --- | --- | ------------------------- | -------- | --------- | -------- | --- | ---- | ---------- | ------ |
|     |     |  0.2+0.05log(i)+0.1logx |          |           | +0.5logx | ,   | τ +1 | ≤ i ≤ 7500 |        |
|     |     |                           |          |           | i−1      | i−2 |      |            |        |
|     | ϵ   | ∼ Weibull(.6,.7)          | for both | segments. |          |     |      |            |        |
37

Scenario 2:


|     |  0.2+0.1log(i)+0.1logx | , 1 | < i ≤ τ |     |
| --- | ------------------------ | --- | ------- | --- |
i−1
ψ =
i
  (2.27)
|     | 0.2+0.1log(i)+0.4logx  | i−1 , τ   | +1 ≤ i ≤ 7500 |     |
| --- | ----------------------- | --------- | ------------- | --- |
| ϵ   | ∼ Gamma(.5,.5) for both | segments. |               |     |
Scenario 3:

 0.2+0.05log(i)−0.01log2(i)+0.1logx
|    |     | +0.2ψ | , 1 | < i ≤ τ |
| --- | --- | ----- | --- | ------- |
|     |     | i−1   | i−1 |         |
ψ =
i

 0.2+0.05log(i)−0.01log2(i)+0.1logx +0.5logx , τ +1 ≤ i ≤ 7500 (2.28)
|                  |                    | i−1 | i−2 |     |
| ---------------- | ------------------ | --- | --- | --- |
| ϵ ∼ Gamma(.5,.5) | for both segments. |     |     |     |
Scenario 4:

|   0.6+0.1log(i)−0.01log2(i)+0.1logx |     | +0.2logx | , 1 | < i ≤ τ |
| -------------------------------------- | --- | -------- | --- | ------- |
|                                        |     | i−1      | i−2 |         |
ψ i =
 0.2+0.1log(i)−0.01log2(i)+0.1logx (2.29)
|                   |                    | i−1 +0.2logx | i−2 , τ | +1 ≤ i ≤ 7500 |
| ------------------ | ------------------ | ------------ | ------- | ------------- |
| ϵ ∼ Weibull(.8,.9) | for both segments. |              |         |               |
For the non-stationary settings of 2.26,2.27,2.28,2.29, we consider assigning small coefficients
for the linear trend and the quadratic trend for two reasons, 1) large coefficient for a time trend can
quickly shrink the durations to zero or cause the overflow of the durations. 2) Small coefficients for
the trend terms can generate similar ranges of the durations, which are consistent with the ones
for real data.
Since our method performs universally well in all four scenarios with or without stationarity
assumption, wedemonstratethemodelresultsinFigure4(Scenario1)forbrevity. Allthemonitor-
ing processes start at M = 2500 and the structural break detection probabilities can be accessed
2
at different phases in the monitoring period. For the scenarios with different structural breaks, our
algorithm shows a good control of type I error under 0.05 before the true structural breaks occur.
Meanwhile, the detection probability increases quickly after the occurrences of the true structural
38

breaks.
For illustration, the intermediate steps are shown in the Figure 5 by a single time series realiza-
tion example from Scenario 1. (a) shows the observations x i with true break point at 3500 (at the
redverticaldashedline). (b)and(c)depictthetrajectoryoftheobserveddetectorstatisticGGGM2(k)
and the Mahalanobis distance. The green shaded area in (b) is the combined confidence interval
based on the theoretical Wiener process threshold and the empirical bootstrap sample threshold.
The red horizontal line in (c) is the empirical bootstrap sample threshold for the Mahalanobis dis-
tance. (d) gives the binary results of break detection at each time point in the monitoring process
from i = 2500. From (d), the detected break point is around 3700, which is close to the true break
| point τ = | 3500. |                                      |                     |                                      |           |
| --------- | ----- | ------------------------------------ | ------------------- | ------------------------------------ | --------- |
|           |       | True break is at 2700 in Scienario 1 |                     | True break is at 3000 in Scienario 1 |           |
|           |       | 1.00                                 |                     | 1.00                                 |           |
|           |       | 0.75                                 |                     | 0.75                                 |           |
|           |       | borp                                 | borp                |                                      |           |
|           |       | 0.50                                 |                     | 0.50                                 |           |
|           |       | 0.25                                 |                     | 0.25                                 |           |
|           |       | 0.00                                 |                     | 0.00                                 |           |
|           |       | 3000                                 | 4000 5000 6000 7000 | 3000 4000 5000                       | 6000 7000 |
|           |       |                                      | time                | time                                 |           |
|           |       | True break is at 3500 in Scienario 1 |                     | True break is at 4000 in Scienario 1 |           |
|           |       | 1.00                                 |                     | 1.00                                 |           |
|           |       | 0.75                                 |                     | 0.75                                 |           |
|           |       | borp                                 | borp                |                                      |           |
|           |       | 0.50                                 |                     | 0.50                                 |           |
|           |       | 0.25                                 |                     | 0.25                                 |           |
|           |       | 0.00                                 |                     | 0.00                                 |           |
|           |       | 3000                                 | 4000 5000 6000 7000 | 3000 4000 5000                       | 6000 7000 |
|           |       |                                      | time                | time                                 |           |
Figure 4:
Break detection outcome from 500 simulations of in a monitoring period of length 5000. X-axis stands
for the monitoring period starting at M =2500. Y-axis stands for the empirical detection probability at a specific
2
time point. The blue dashed lines stand for the true break point τ = 2700, 3000, 3500, and 4000. The red dashed
| lines stand | for the significance | level α | = 0.05. |     |     |
| ----------- | -------------------- | ------- | ------- | --- | --- |
overall
For practical implementation, these results provide useful guidance for the decision-makers to
adjusttheir toleranceof thetype Ierror andthe preferenceof thesensitivity ofthe breakdetection.
These results also show that in Scenarios 1 and 2 where there is only one parameter change within
thesamelogACDmodelframework,ouralgorithmisabletodetectthestructuralbreakrapidlyand
accurately. In Scenario 3 where there is a change on the type of the log ACD model, the detection
probability increases more quickly to 100% after the structural break occurs. Finally, since the
39

|     |     |     |     | omega alpha1 | alpha2 |
| --- | --- | --- | --- | ------------ | ------ |
0
|     |     | 20  |     | −1000 |     |
| --- | --- | --- | --- | ----- | --- |
−2000
−3000
15
|     |     | noitarud | G devresbO | −4000 |     |
| --- | --- | -------- | ---------- | ----- | --- |
−5000
|     |     |     |     | alpha3 alpha4 | alpha5 |
| --- | --- | --- | --- | ------------- | ------ |
10
0
−1000
−2000
|     |     | 5   |     | −3000 |     |
| --- | --- | --- | --- | ----- | --- |
−4000
|     |     | 0      |           | −5000                                        |                               |
| --- | --- | ------ | --------- | -------------------------------------------- | ----------------------------- |
|     |     |        |           | 0003 0004 0005 0006 0007 0003 0004 0005 0006 | 0007 0003 0004 0005 0006 0007 |
|     |     | 0 2000 | 4000 6000 |                                              |                               |
|     |     |        | time      | time                                         |                               |
|     |     |        | (a)       | (b)                                          |                               |
1.00
400
0.75
300
aham_2d
noitceted
0.50
200
0.25
100
|     |     | 0    |                     | 0.00           |           |
| --- | --- | ---- | ------------------- | -------------- | --------- |
|     |     | 3000 | 4000 5000 6000 7000 | 3000 4000 5000 | 6000 7000 |
|     |     |      | time                | time           |           |
|     |     |      | (c)                 | (d)            |           |
Figure 5: (a) A single realization of Scenario 1 with true break at τ = 3500;(b) The trace plot for the individual
GM2(k)withtheconfidenceintervalsbasedontheWienerprocessandbootstrapthresholdsingreenbands;
(c)The
j
traceplotfortheMahalanobisdistanced2 (k),withbootstrapthresholdd2 (k)(redhorizonalline);(d)Thetrace
|              |                  |                    | M    | 1−αM |     |
| ------------ | ---------------- | ------------------ | ---- | ---- | --- |
| plot for the | binary indicator | of break detection | δ(k) |      |     |
detector statistic is based upon the quasi-score change instead of prediction on the observational
level, forScenario4weareabletoimplementthestructuralbreakdetectionifthereisanincreasing
tradingintensitybetweentwophasesoffinancialdurationtimeseries. Additionalsimulationresults
| for Scenarios | 2, 3, and   | 4 are provided | in the supplemental | material. |     |
| ------------- | ----------- | -------------- | ------------------- | --------- | --- |
| 2.4.2 Real    | application |                |                     |           |     |
In addition to the extensive simulation study to illustrate our method in different scenarios, we also
implement it for some real financial duration data. We are able to detect the structural breaks and
associate them with some financial information that may trigger these structural breaks. Nonethe-
less, real data applications of our method need attentions to different aspects of implementation.
To get a meaningful monitoring process and identify outbreaks of interest, practitioners need to
consider the general features of the financial durations and idiosyncratic characteristics of different
assets.
In existing retrospective studies of structural break detection, the raw time series data can be
adjusted universally to filter out some common structures and enhance the model’s adequacy. For
40

example,Zhangetal.(2018)performedstructuralbreakdetectioninaretrospectivefashion,andthe
complete intra-day financial durations were adjusted through a linear regression to accommodate
the diurnal effect, which is displayed as higher trading intensity in the opening and closing period
of the stock market. However, since our ensemble method processes real-time streaming data in
practice, we cannot replicate the same retrospective adjustment for online break detection. If the
aim is to detect some non-diurnal-effect-related structural breaks, we suggest discarding the first
and last 30-minute time windows and applying the algorithm to diminish the diurnal effect.
Due to the flexible definition of a financial event, users can feel free to choose the price or
return changes as the target events to collect the online duration time series based on individual
risk tolerance and trading preferences. Besides, we also recommend market participants customize
their monitoring process according to the characteristics of individual assets and set proper tuning
parameters for the monitoring such as the length of the training period.
As illustrated in the examples in real applications, we apply our break detection method to four
specific stocks: IBM, BAC, MMM, and GE, and explore the dynamic structures underlying the
financial durations. We choose the price changes between two successive transactions exceeding a
pre-specified amount, δ, as the financial events. The financial durations are computed from the
WRDS Trade and Quote data in June 2013 (Zou et al., 2015). Following a common approach used
by financial professionals, we used the data from the previous month (May 2013) to calculate the
average turnover ratio as average daily volume divided by total shares outstanding. Therefore,
δ = 0.00377,0.004,0.00376,0.00408 for GE, BAC, IBM, and MMM respectively.
When it comes to the tuning parameters, a meaningful monitoring process needs to accommo-
date the liquidity of the assets. GE and BAC are liquid stocks with high trading volumes (100,000
to 200,000 transactions per day on average) and a relatively low price spread of about $ 0.5 per day
on average. Meanwhile, IBM is also a liquid stock with a medium number of average transactions
per day (around 20,000) with an absolute price spread between $3 and $4. MMM has variable low
numbersoftransactions(between4000and15,000perday)andabsolutepricespreadofabout$1.5.
In practice, for the liquid assets, we choose a longer training period for better model adequacy. But
for the less liquid assets such as MMM, the number of transactions can be very small. Therefore,
we suggest choosing a shorter training period and λ candidates of large values in the penalty term
p′ (|θθθ|) of the penalized estimating function for grid search, in order to enhance model stability in
λ
41

the recursive estimation procedure during the training period.
To reflect the market behaviour and trading intensity through the pattern change of financial
durations, we apply the ensemble detection method to a log ACD (20,0) as the training model for
the break detection. All transactions are selected from 10:00 a.m. and 3:30 p.m.. We are able to
detect some structural breaks, and benchmark with published financial news for these companies
on the same day, or during off hours before. With the detected breaks shown in Figure 6, We list
the break detection results as well as their related financial news for stocks IBM, BAC, MMM, and
GE respectively.
On June 4th, the structrural break of IBM was detected at around 1:01 p.m.. A piece of
financial news about IBM was released on June 4th at 9:11 a.m.. From The New York Times,“
I.B.M. announced on Tuesday that it had agreed to buy SoftLayer Technologies, a cloud computing
company, in an effort to strengthen I.B.M.’s position in the fast-growing market for computing sold
to businesses as a service delivered over the Internet.”.
On June 5th, the structrural break of BAC was detected at around 10:33 a.m.. We have also
found a piece of financial news about Bank of America on June 4th at 9:47 p.m was as follows.
From Reuters, “NEW YORK, June 4 (Reuters) - American International Group Inc argued on
Tuesday that a proposed $8.5 billion settlement between Bank of America Corp and investors in
Countrywide Financial Corp mortgage-backed securities was not big enough.”.
On June 10th, the structrural break of MMM was detected at around 13:10 p.m.. The CEO
of MMM reclaimed the company was research-driven and invested a large amount of money in its
research development on June 10th at 6.53 a.m. From CNBC, “In a lab in St. Paul, Minnesota,
engineers test solar panels and connectors. A half a mile away, a technician smashes the windows
of a car coated with 3M protective film, watching to see if the glass shatters or holds together. Else-
where, there are scientists working on more aerodynamic products for airplanes, software systems
to run a municipality’s department of motor vehicles, and light-sensor technology to create new
crowns for teeth in under 2 hours.”.
On June 24th, the structrural break of GE was detected at around 12:54 p.m., A recent event
thathappenedtoGEincorporationwasonJune22th(Saturday). Frommilitaryaerospace, “Trans-
Digm Group Inc. (NYSE:TDG) has entered into a definitive agreement to acquire the assets of GE
Aviation’s Electromechanical Actuation Division for approximately $150 million in cash.”.
42

| IBM on 20130604 |     | BAC on 20130605 |
| --------------- | --- | --------------- |
30
| 40  |     | 358.54:33:01 |
| --- | --- | ------------ |
80.15:0:31
| 30        |     | 20        |
| --------- | --- | --------- |
| snoitarud |     | snoitarud |
20
10
10
| 0   |     | 0   |
| --- | --- | --- |
0005 00001 00051
| 0 0002 0004     | 0006 0008 | 0              |
| --------------- | --------- | -------------- |
| time            |           | time           |
| (a)             |           | (b)            |
| MMM on 20130610 |           | GE on 20130624 |
80
471.44:01:31 751.03:45:21
| 60        |     | 20        |
| --------- | --- | --------- |
| snoitarud |     | snoitarud |
40
10
20
0
0
| 0001 | 0002 0003 | 0005 00001 |
| ---- | --------- | ---------- |
| 0    |           | 0          |
| time |           | time       |
| (c)  |           | (d)        |
Figure 6: Structural break points detected (red vertical dash lines) in the duration time series of IBM,
BAC, MMM and GE respectively.
From real applications, our E-PEF method is able to detect break points in duration time series
and offers an adaptive framework incorporating different asset features. With detected change
points from online data, the practitioners can act proactively and seek for more evidence from
different sources of information such as market news to evaluate the asset or market behaviors.
With the combination of statistically detected break points and real world information, E-PEF
method can reassure practitioners to use adequate models for the online data and make subsequent
transactional decisions.
2.5 Summary
In a high-frequency trading setting, the financial duration models can give a reasonable interpre-
tation on the volatile behavior of the market in terms of trading intensity. Therefore, accurate
awareness of the structural breaks will provide helpful insights for the market participants to up-
date the statistical model as soon as a structural break is detected. In this article, we propose
an innovative E-PEF method in the online detection strategy for the log ACD model, which is a
prevalent tool for modeling financial durations. In the parameter estimation stage for the training
period, wetakeadvantageofthePEFrecursiveestimationapproachforthelogACDmodelregard-
43

less of the distribution of the innovations. In the online monitoring stage, we propose an ensemble
algorithm combining three different types of thresholds for the quasi-score functions to facilitate
structuralbreakdetectioninthefinancialdurationtimeseries. Weillustratetheperformanceofour
ensemble approach by extensive simulations under different scenarios. We implement our method
in real data applications to monitor the duration time series and detect some structural breaks
with various sources of financial information for a better interpretation of the market behavior.
Our contribution lies in the innovative ensemble online detection framework for financial du-
ration time series. This framework enjoys a distribution-free statistical inference on the log ACD
model with penalized estimating functions. The block bootstrap method provides the empirical
distribution of PEF from the observed training time series without additional parametric assump-
tions. Resampled data further lead to the incorporation of two new thresholds, the bootstrap
threshold and the Mahalanobis distance threshold, into the monitoring procedure. The detection
rule is formulated in an ensemble fashion integrating all three types of thresholds. The combined
advantagesofbothasymptoticandempiricalpropertiesoftheonlinedetectorteststatisticfacilitate
the reduction of the false discovery rate. The E-PEF approach shows that the type I error can be
well controlled under a specific level while preserving a high power to detect any true breakpoints.
The merit of our method focuses on timely structural break detection under parameter changes in
an online fashion.
44

3 Multivariate latent level correlation model (LCM) for financial
high frequency count time series
3.1 Background
Volatility analysis helps investors navigate their asset positions to optimize their gains in the fi-
nancial market. As high-frequency, intra-day asset pricing data become increasingly available,
exploration and explanation for the micro-structure of the financial market behavior forms an im-
portant and popular research direction. The volatility study of the general financial data involved
with irregularity and intricacy already requires non-trivial methods for delicate statistical infer-
ence. The advancement of high frequency trading escalates the challenge with increased data size
as well as dimension. Prompt inference on high frequency financial data is in great demand for
the market participants. In a high frequency trading setting, the raw transactions are made within
milliseconds, and the corresponding price changes occur with various magnitudes of fluctuation.
Therefore, log returns for the asset price can be calculated based on these price changes. In ad-
dition to other different research-related definitions, our study use the count of the transactions
with extreme log return to describe the market volatility, and the extremeness of a log return is
determined by practitioners according to their interest. Within a given time interval, an asset with
higher volatility tend to have a larger count, which motivates one to implement discrete time series
model to account for the underlying market volatility.
Specifically, we convert transaction-by-transaction log returns to a multivariate count time
series by using a threshold τ > 0. During a given period of time, the transactions with the
absolute log return exceeding τ are categorized as high risk level, while the other are categorized
as low risk level. Therefore, for a specific asset, two types of count will be observed and studied
simultaneously. Under general circumstance of high frequency trading trading, the price changes
don’t have significant fluctuation thus the transactions of low risk level are expected to have a large
number of count, and such count has its own time dependent property. The count for transactions
of high risk level provide more insights on the volatility but the count may not be as abundant
as the former, due to the asset idiosyncrasy or the choice of τ. With the access to a plenitude
of low-risk-level transaction data, practitioners could have more options to adjust and refine their
45

investment strategy if they have a sound comprehension of the co-movement between these two
types of counts.
3.2 Literature review
3.2.1 Discrete time series modeling
Count time series arise naturally in numerous applied scientific fields such as finance, epidemiology,
agriculture, etc., and the analysis of such non-Gaussian data has been an active research area for
a long time. There is a rich literature on univariate modeling of count time series, both in the
frequentist and Bayesian frameworks. The frequentist approaches include discrete auto-regressive
movingaverage(DARMA)models(JacobsandLewis,1983),integer-valuedauto-regressive(INAR)
models(Al-OshandAlzaid,1987),andinteger-valuedGARCH(INGARCH)models(Ferlandetal.,
2006). West et al. (1985) and Gamerman et al. (2013) have discussed Bayesian dynamic general-
ized linear models (DGLM). Financial applications of univariate count time series models include
Heinen(2003)whoimplementedthedoubleexponentialfamilyGLMofEfron(1986)byintroducing
the auto-regressive conditional Poisson model. They applied the model for volatility modeling of
price change count time series of IBM returns, exploiting the ability of the model to explain the
autocorrelationandoverdispersioninthedata. Liesenfeldetal.(2006)usedanintegercounthurdle
model with a negative binomial sampling distribution for stock transaction price changes. How-
ever, it is now widely accepted that financial data are time-dependent across assets and markets.
Although the aforementioned methodologies deal with univariate time series, their perspectives of
approaching the univariate time series modeling still facilitate the extension of multivariate time
series framework.
Foranalyzingmultivariatecounttimeseries, weneedmodelsthatnotonlyexplainthetemporal
correlation within each series, while accommodating possible overdisperison, but also explain cross-
sectional correlation between the components. Pedeli and Karlis (2013) extended the INAR(1)
framework to the bivariate case. Karlis and Meligkotsidou (2005) discussed a multivariate Poisson
(MVP) distribution with a two-way covariance structure, while Karlis and Meligkotsidou (2007)
described a finite mixture of multivariate Poisson distributions which allows for both positive and
negative covariances between components. Ravishanker et al. (2014) used MVP sampling distribu-
46

tions and Gibbs sampling for hierarchical dynamic modeling for multivariate time series of counts
of gastropod abundance. Jung et al. (2011) proposed a parameter-driven approach for multivariate
count financial time series through a dynamic factor model incorporating both common and id-
iosyncratic factors in the conditional Poisson mean. Quoreshi (2017) fit a bivariate integer-valued
fractionally integrated moving average model to time series of counts of transactions in equally
spacedtimeintervals,andmanagedtoaccommodatethelong-memorypatternoftheinteger-valued
time series. Aktekin et al. (2018) combined dynamic temporal parameters and individual static
parameters into a product as the Poisson means in the multivariate Poisson-scaled beta model,
and used forward filtering backward sampling (FFBS) and particle learning algorithms setting in
the dynamic online Bayesian updating. See Soyer and Zhang (2021) for an excellent review of
recent advances in multivariate count time series modeling. Despite the existent methodologies for
multivariate count time series, the concern about computational feasibility arises when it comes to
the high-dimension time series modeling, whether or not in frequentist or Bayesian approach. For
multivariate INAR or MVP, the computation for the probability mass function of a multivariate
discrete random variable requires a large number of summations from inverse mapping. As a con-
sequence, Expectation-Maximization (EM) algorithm for maximum likelihood estimation will be
slowed down significantly due to the increase of dimension even though the utilisation of recursive
relationships to calculate the conditional expectation can alleviate some of the computational bur-
den. For Bayesian approach, exact inference for joint posterior by MCMC sampling is also of great
difficulty because it is not uncommon for the posteriors to be intractable. Hence, the computation
of high dimensional integrals suffers from the posteriors that are not in a closed form.
A few alternative ideas have been proposed to carry out fast Bayesian modeling. West (2020)
proposed a decouple/recouple idea in DGLM for computational efficiency and model adequacy for
node-node dependency based upon the complete sets of posterior samples of the dynamic coeffi-
cients. Lavine et al. (2020) introduced copula modeling to multi-step, multi-scale, and dynamic
latent factors, using variational Bayes’ (VB) optimization (Blei et al., 2017). Being appealing to
provide comparable accuracy to Gibbs sampling at greater speed, VB approach often requires a
large amount of work to derive the set of equations for iterative parameter update. Therefore,
An alternative to VB for fast, approximate Bayesian modeling can be considered for statistical
inference, which is the integrated nested Laplace approximation, see Rue et al. (2009) or Rue et al.
47

(2017).
| 3.2.2 Integrated |     | Nested | Laplace |     | Approximation |     | (INLA) |     |     |
| ---------------- | --- | ------ | ------- | --- | ------------- | --- | ------ | --- | --- |
A wide variety of models can be fit by INLA (G´omez-Rubio, 2020). In general, for a vector of n
observations yyy = (y ,...,y ), mean µ of observations y can be related to the linear predictor η
|                   |     | 1                | n    |          | i        |        | i      |            | i     |
| ----------------- | --- | ---------------- | ---- | -------- | -------- | ------ | ------ | ---------- | ----- |
| through different |     | link functions,. |      |          |          |        |        |            |       |
|                   |     |                  |      | n        | n        |        |        |            |       |
|                   |     |                  |      | β        |          | f      |        |            |       |
|                   |     |                  |      | (cid:88) | (cid:88) | f(k)(u |        |            |       |
|                   |     | η                | = α+ | β        | z +      |        | )+ε ;i | = 1,...,n, | (3.1) |
|                   |     | i                |      |          | j ji     |        | ki i   |            |       |
|                   |     |                  |      | j=1      | k=1      |        |        |            |       |
n β
where α is the intercept, β j ,j = 1,...,n β , are coefficients of the covariates {zzz j } , functions
j=1
n
f(k)(u) define n random effects on the covariates {uuu } f . ε is the error term, and it can be
|     | f   |     |     |     |     |     | k k=1 | i   |     |
| --- | --- | --- | --- | --- | --- | --- | ----- | --- | --- |
missing depending on the likelihood. The vector of latent effect x is defined as,
|     |     |     |     | xxx | = (η ,...,η |     | ,α,β ,...). |     | (3.2) |
| --- | --- | --- | --- | --- | ----------- | --- | ----------- | --- | ----- |
|     |     |     |     |     | 1           | n   | 1           |     |       |
The distributions of yyy are dependent on the latent effect xxx and some hyperparameters θθθ , and
1
the precision matrix for the Gaussian Markov Random Field (GMRF) of xxx is determined by some
other hyperparametersθθθ . With the assumptions thatxxx has a sparse structure of GMRF (Rue and
2
Held, 2005) as well as that y ’s are independent to each other givenxxx, INLA will take advantage of
i
the sparse structure and conditional independence properties of GMRF to enhance computational
efficiency. Letθθθ = (θθθ ,θθθ ). Insteadofobtainingtheinferencefromthejointposteriordistributionof
|     |     | 1 2 |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
(xxx,θθθ),
INLA focuses on the marginal inference on the latent effects and hyperparameters. Starting
| with the form | of  | joint posterior |                        | density | of xxx and | θθθ,     |                 |                |     |
| ------------- | --- | --------------- | ---------------------- | ------- | ---------- | -------- | --------------- | -------------- | --- |
|               |     |                 |                        |         |            | (cid:26) | (cid:27)        |                |     |
|               |     |                 |                        |         |            |          | 1               | (cid:89)       |     |
|               |     | π(xxx,θθθ|yyy)  | ∝ π(θθθ)|QQQ(θ)|1/2exp |         |            | −        | xxxTQQQ(θθθ)xxx | π(y |x ,θθθ) = |     |
i i
2
i∈I
|     |     |     |     | (cid:40) |     |     |     | (cid:41) | (3.3) |
| --- | --- | --- | --- | -------- | --- | --- | --- | -------- | ----- |
1
|     |     | π(θθθ)|QQQ(θ)|1/2exp |     |     | xxxTQQQ(θθθ)xxx+ |     | (cid:88) |             |     |
| --- | --- | -------------------- | --- | --- | ---------------- | --- | -------- | ----------- | --- |
|     |     |                      |     |     | −                |     | log(π(y  | |x ,θθθ)) . |     |
|     |     |                      |     |     | 2                |     |          | i i         |     |
i∈I
In order to get the posterior marginals, the approximation of the joint posterior of θθθ, π˜(θθθ|yyy), is
| proposed as, |     |     |     |     |     |     |     |     |     |
| ------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- |
π(xxx,θθθ,yyy)
|     |     |     |     | π˜(θθθ|yyy) | ∝   |               | | ,           |     | (3.4) |
| --- | --- | --- | --- | ----------- | --- | ------------- | ------------- | --- | ----- |
|     |     |     |     |             | π˜  | (xxx|θθθ,yyy) | xxx=xxx∗(θθθ) |     |       |
G
48

where π˜ (xxx|θθθ,yyy) can be a Gaussian approximation or Laplace approximation at the model of the
G
full conditiona,xxx∗(θθθ) . Hence, the marginals for the individual latent effect x and hyperparameter
l
| θ k become | available, |     |     |     |
| ---------- | ---------- | --- | --- | --- |
(cid:90)
|     |     | π(x | |yyy) = π(x |θθθ,yyy)π˜(θθθ|yyy)dθθθ, |     |
| --- | --- | --- | ------------------------------------- | --- |
|     |     |     | l l                                   |     |
(3.5)
(cid:90)
|     |     | π(θ | k |yyy) = π˜(θθθ|yyy)dθθθ | −k . |
| --- | --- | --- | ------------------------- | ---- |
INLA has been widely used in several applications of time series. Ruiz-C´ardenas et al. (2012)
discussed a variety of state-space dynamic models, including count time series modeling. Schr¨odle
andHeld(2011)describeddiseasecountdatamodelingthroughincidencerates, whileSalmonetal.
(2015) discussed a Bayesian approach for detecting outbreak in an infectious disease surveillance
system. Sadykova et al. (2017) used zero-inflated and hurdle Poisson spatio-temporal models for
predator-prey and competitor species habitat. Serhiyenko et al. (2018) implemented a latent level
correlation model (LCM) using INLA for dynamic modeling of multivariate counts in a marketing
application involving monthly prescriptions written by physicians for a pharmaceutical company’s
drugs. Riebler and Held (2017) used the INLA approach for age-period-cohort analysis. Raman
et al. (2020) explored different univariate static and dynamic models using INLA for evaluating
| promotions      | of marketing | schemes. |     |     |
| --------------- | ------------ | -------- | --- | --- |
| 3.3 BVAR(1)-LCM |              | model    |     |     |
In this chapter, we propose a fast and accurate Bayesian framework for correlated bi-variate count
time series with latent level correlation (BVAR(1)-LCM) using the INLA approach. The aim is to
describe the association between the two count time series across multiple assets and exhibit some
model parameters of interest to better explain the microstructure of the financial market. Despite
the elevated model complexity, our method enjoys computational speediness due to the sparsity of
Gaussian Markov Random Field (GMRF) among the model parameters. Fast Bayesian inference
approximation can be obtained with good quality, and practitioners can study the dynamics within
| and between | the count | time series in | a higher dimension | efficiently. |
| ----------- | --------- | -------------- | ------------------ | ------------ |
49

3.3.1 Model framework
Let {Y j,st } denote the count for j-th type of transaction for s-th asset in the t-th time interval, j =
1,2,...,J,s = 1,2,...,S and t = 1,2,...,T. Since we study the association between transaction
count with a low-risk level and the one with a high-risk level, J = 2. S is the total number of
assets involved in the framework and T is the total number of time intervals. To account for
the temporal and cross-sectional association among the assets, we implement a Bayesian Poisson
Lognormal framework conditioned on various sources of fixed or random effects:
ind
|      | Y      | |λ ∼ Pois(λ | ),       |
| ---- | ------ | ----------- | -------- |
|      | j,st   | j,st        | j,st     |
| η    | = logλ | =ZZZ βββ    | +γ +α ,  |
| j,st |        | j,st j j    | j,t j,st |
|      | γ      | = ϕ γ +ω    | ,        |
|      | j,t    | j j,t−1     | j,t      |
|      |       |            |          |
ω
1,t
|     | ωωω =  |  ∼ N (000,ΣΣΣ | ),  |
| --- | ------- | -------------- | --- |
|     | t      |               | ωωω |
ω
2,t
|     |    |     |    |
| --- | --- | --- | --- |
(3.6)
|     |     | σ2 ρ   | σ σ     |
| --- | --- | ------ | ------- |
|     |     | ω1 ωωω | ω1 ω2, |
ΣΣΣ = 
|     | ωωω  |           |    |
| --- | ----- | --------- | --- |
|     |       | ρ σ σ     | σ2  |
|     |       | ωωω ω1 ω2 | ω2  |
|     |       |         |     |
α
1,st
|     | ααα | =   ∼ N | (000,ΣΣΣ ), |
| --- | --- | --------- | ----------- |
|     | st  |         | ααα         |
α
2,st
|     |    |        |        |
| --- | --- | ------ | ------- |
|     |     | σ2 ρ   | σ σ     |
|     |     | α1 ααα | α1 α2. |
ΣΣΣ = 
|     | ααα  |           |    |
| --- | ----- | --------- | --- |
|     |       | ρ σ σ     | σ2  |
|     |       | ααα α1 α2 | α2  |
In (3.6), ZZZ and βββ are respectively covariates (intercept included) and coefficients. γ is the
j j j,t
temporal random effect with an AR process for j-th type of count. Since they are two types of
count involved, j takes values of either 1 or 2. The innovation terms ω for the two AR processes
j,t
have the correlation coefficient, ρ . σ2 and σ2 are correspondingly the variances for the AR
|     | ω   | ω1 ω2 |     |
| --- | --- | ----- | --- |
innovations. ααα is the level correlated random effect, ΣΣΣ is its variance-covariance matrix.
st ααα
The benefit of Poisson-Lognormal distribution has been discussion in Aitchison and Ho (1989).
It not only retains the interpretability of the parameters in the model but also it well addresses
the overdispersion issue encountered by a standard Poisson distribution. Considering a simple
50

| univariate | Poisson-Lognormal |     | random | variable: |          |     |     |     |
| ---------- | ----------------- | --- | ------ | --------- | -------- | --- | --- | --- |
|            |                   |     |        | Y|λ ∼     | Pois(λ), |     |     |     |
(3.7)
|     |     |     |     | logλ|µ,σ2 | ∼ N(µ,σ2). |     |     |     |
| --- | --- | --- | --- | --------- | ---------- | --- | --- | --- |
Usingthelawsoftotalexpectationandvariancewecaneasilyderivetheconditionalexpectation
| E(Y|µ,σ2) | and the conditional |           | variance | Var(Y|µ,σ2). |                     |         |     |     |
| --------- | ------------------- | --------- | -------- | ------------ | ------------------- | ------- | --- | --- |
| For       | E(Y|µ,σ2), we       | have,     |          |              |                     |         |     |     |
|           |                     | E(Y|µ,σ2) |          |              | (cid:0) E(Y|λ,µ,σ2) | (cid:1) |     |     |
|           |                     |           |          | = E          |                     |         |     |     |
λ|µ,σ2
(3.8)
|     |     |     |     | = E    | (E(Y|λ)) | = E      | (λ) |     |
| --- | --- | --- | --- | ------ | -------- | -------- | --- | --- |
|     |     |     |     | λ|µ,σ2 |          | λ|µ,σ2   |     |     |
|     |     |     |     |        | (elogλ)  | eµ+σ2/2. |     |     |
|     |     |     |     | = E    |          | =        |     |     |
λ|µ,σ2
Var(Y|µ,σ2),
| For |             | we have, |        |                |        |          |             |         |
| --- | ----------- | -------- | ------ | -------------- | ------ | -------- | ----------- | ------- |
|     |             |          |        | (cid:0)        |        | (cid:1)  | (cid:0)     | (cid:1) |
|     | Var(Y|µ,σ2) |          | = E    | Var(Y|λ,µ,σ2)  |        | +Var     | E(Y|λ,µ,σ2) |         |
|     |             |          | λ|µ,σ2 |                |        | λ|µ,σ2   |             |         |
|     |             |          | = E    | (Var(Y|λ))+Var |        | (E(Y|λ)) |             |         |
|     |             |          | λ|µ,σ2 |                |        | λ|µ,σ2   |             |         |
|     |             |          | = E    | (λ)+Var        |        | (λ)      |             |         |
|     |             |          | λ|µ,σ2 |                | λ|µ,σ2 |          |             |         |
(3.9)
|     |     |     |     | (elogλ)+Var |     | (elogλ) |     |     |
| --- | --- | --- | --- | ----------- | --- | ------- | --- | --- |
= E
|     |     |     | λ|µ,σ2           |     | λ|µ,σ2  |      |     |     |
| --- | --- | --- | ---------------- | --- | ------- | ---- | --- | --- |
|     |     |     | eµ+σ2/2+(e2µ+2σ2 |     | −e2µ+σ2 |      |     |     |
|     |     |     | =                |     |         | )    |     |     |
|     |     |     | E(Y|µ,σ2)+e2µeσ2 |     | (eσ2    |      |     |     |
|     |     |     | =                |     |         | −1). |     |     |
σ2
From Equations 3.8 and 3.9, can well account for the overdispersion or underdispersion of
| distribution | through | the sign | of eσ2 | −1. |     |     |     |     |
| ------------ | ------- | -------- | ------ | --- | --- | --- | --- | --- |
Inthed-dimensionalmultivariatesettingforPoisson-LognormaldistributiondenotedbyPΛd(µµµ,,,ΣΣΣ),
withµµµ = (µ ,...,µ )′ andΣΣΣ = (σ ) (Aitchison and Ho, 1989; Serhiyenko et al., 2018), another
|     | 1 d |     | ii  | d×d |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
advantage of this distribution is that it can recover both positive and negative correlation between
two count variables, which presents the bottleneck to a bivariate Poisson distribution. For a mul-
tivariate Poisson-Lognormal variable YYY = (y ,...,y )′, its probability density function could be
|     |     |     |     |     | 1   | d   |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
expressed through the integration of the latent variable λλλ = (λ ,...,λ )′,
|     |     |     |     |     |     | 1   | d   |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
51

|     |     |     | (cid:90) | d   |     |     |
| --- | --- | --- | -------- | --- | --- | --- |
(cid:89)
|     |     | p(YYY|µµµ,,,ΣΣΣ) | =   | f(y |λ )·Nd(λλλ|µµµ,,,ΣΣΣ)dλλλ. |     | (3.10) |
| --- | --- | ---------------- | --- | ------------------------------- | --- | ------ |
i i
Rd
+i=1
The expectation, variance and correlation between each pair of the count variable are found as:
|µµµ,,,ΣΣΣ)
|     | E(Y   | i = exp(µ   | i +σ ii /2) | = m i ,  |     |        |
| --- | ----- | ----------- | ----------- | -------- | --- | ------ |
|     |       | |µµµ,,,ΣΣΣ) | +m2(exp(σ   |          |     |        |
|     | Var(Y | i =         | m i         | ii )−1), |     |        |
|     |       |             | i           |          |     | (3.11) |
exp(σ )−1
ij
|     | Corr(Y | ,Y |µµµ,,,ΣΣΣ) | =         |     | .            |     |
| --- | ------ | -------------- | --------- | --- | ------------ | --- |
|     |        | i j            | (cid:104) |     | (cid:105)1/2 |     |
)−1+m−1)(exp(σ )−1+m−1)
|     |     |     | (exp(σ | ii jj |     |     |
| --- | --- | --- | ------ | ----- | --- | --- |
|     |     |     |        | i     | j   |     |
For the count data, there is a lower bound zero thus leading to the difficulty of recovering a
strongnegativecorrelationbetweentwocountvariables, i.e, whenoneapproachesinfinity, theother
one will approach zero instead of exploding into negative infinity. However, Poisson-Lognormal
distribution still exhibits a wide range of correlation coverage and works impressively well when
| there exists | a positive | correlation | between | two count variables. |     |     |
| ------------ | ---------- | ----------- | ------- | -------------------- | --- | --- |
Incorporating the latent level correlation structure, represented by ΣΣΣ, is inspired by the fact
thatinreallifemanyotherimportantcovariatesarenotcollectedorevennotobservablebuthavea
significant impact on the count variables. Therefore, neglecting the potential correlation structure
can gravitate to a biased inference and prediction. With the interrelated multivariate Poisson-
Lognormal model for each specific count variable, we can explain the inherent pattern across the
different count data. In the noisy high-frequency financial data, the incorporation of latent level
| correlation | helps reduce | biased | inference. |     |     |     |
| ----------- | ------------ | ------ | ---------- | --- | --- | --- |
The applications of multivariate Poisson-Lognormal distribution have been demonstrated in
transportation crash counts using MCMC approach for inference (Park and Lord, 2007; Ma et al.,
2008) . However, their approach only handles the crash counts of different severity levels but with
no temporal random effect. In other words, the size of crash count data is much smaller than
the high-frequency count data due to the absence of time index. In volatility analysis, temporal
dependence is commonly considered and so does our method. As a consequence, high-frequency
count data with a larger size pose an even bigger computational challenge for MCMC approach
especially when more parameters and latent effects are considered in the model. We will next
52

address this problem with Integrated Nested Laplace Approximation (INLA) approach.
3.3.2 INLA implementation
As mentioned in the previous work, despite the benefits of Poisson-Lognormal models, the com-
plexity of such models influences their computational cost, especially when a larger number of
parameters need to be incorporated. MCMC method can become very computationally expensive
asitcomputesthejointposteriordistributionofmodelparametersinahighdimensionspace. How-
ever, INLAapproachinsteadtargetstheindividualposteriormarginals, whichusuallyaresufficient
for statistical inference on the model parameters and latent effect, and there is no need to handle
complicated joint posterior distributions. Fortunately, the parameters in the Poisson-Lognormal
framework can be regarded as a Gaussian Markov Random Field (GMRF), i.e, a finite-dimensional
random vector following a multivariate Gaussian distribution (Rue and Held, 2005). With the
conditional independence assumptions, INLA takes advantage of the sparsity of the precision ma-
trix for the GMRF and use efficient Bayesian approximation inference for the parameters. As an
illustration, we describe the detailed INLA implementation proposed by Rue et al. (2009) for the
(3.6).
Letthevectoroflatenteffectbexxx = (βββ,γ ,γ ,...,γ ,γ ,γ ,...,γ ,ααα ,...,ααα )and
1,1 1,2 1,T 2,1 2,2 2,T 1,1 S,T
the vector of hyperparameters be θθθ = (ϕ ,ϕ ,ΣΣΣ ,ΣΣΣ ). Within framework, this latent structure is
1 2 ωωω ααα
a GMRF of zero mean and precision matrix detemined by θθθ. Based upon the joint probability
density,
(cid:89)
π(xxx,YYY,θθθ) ∝ π(θθθ)π(xxx|θθθ) π(Y |x ,θθθ)
i i
i∈I
  (3.12)
(cid:89)
T
(cid:89)
S
(cid:89)
2 λ Y
j,
j
s
,
t
ste−λj,st
∝ π(θθθ)π(βββ) f(γγγ
t
|γγγ
t−1
,ϕ
ω1
,ϕ
ω2
,ΣΣΣ
ωωω
) N(ααα
st
;000,ΣΣΣ)
Y !
,
j,st
t=1 s=1 j=1
where π(θθθ) is the prior density for the hypermeters θθθ, we use the default priors, Gaussian prior
(cid:16) (cid:17)
for the internal transformed hyperparameter, log
1+ϕj
,j = 1,2. and Wishart priors for the
1−ϕj
precision matrices, ΣΣΣ−1,ΣΣΣ−1. π(βββ) is a Gaussian prior for the intercepts and coefficients βββ,
ωωω ααα
(cid:81)T
f(γγγ |γγγ ,ϕ ,ϕ ,ΣΣΣ ) is the Gaussian likelihood for the correlated temporal random effects
t=1 t t−1 1 2 ωωω
γ ,j = 1,2, and N(;) is the bivariate Gaussian density.
j
53

The posterior marginal density for the hyperparameters θθθ can be obtained by the Laplace
approximation,
π(xxx,YYY,θθθ)
π˜(θθθ|YYY) ∝ , (3.13)
π˜
(xxx|θθθ,YYY)xxx=xxx∗(θθθ)
G
whereπ˜ (xxx|θθθ,YYY)istheLaplaceapproximationofπ(xxx|θθθ,YYY),xxx∗(θθθ)isthemodeoftheconditional
G
posterior density π(xxx|θθθ,YYY).
Next, using the approximation of π(θθθ|YYY), the discrete integration can provide us with the
approximation of the posterior marginal densities of interest π(x |YYY),
i
(cid:88)
π˜(x i |YYY) = π˜(x i |θθθ k ,YYY)π˜(θθθ k |YYY)∆ k , (3.14)
k
Whereπ˜(x |θθθ ,Y)isthemarginalGaussiandensityfortheapproximationofπ(x |θθθ ,Y)derived
i k i k
from π˜ (xxx|θθθ,YYY), ∆ is the area weights in the discrete integration.
G k
Since correlated bivariate AR process is not available in the current INLA package, we need to
derivetheprecisionmatrixfrom
(cid:81)T
f(γγγ |γγγ ,ϕ ,ϕ ,ΣΣΣ )istheGaussianlikelihoodforthecorre-
t=1 t t−1 1 2 ωωω
lated temporal random effects γ ,j = 1,2, and define this specific latent effect using inla.rgeneric()
j
function in INLA. For the bivariate AR(1) process according to (3.6),

 

  γ 1,t = ϕ 1 γ 1,t−1 +ω 1,t ω 1,t
,−1 < ϕ ,ϕ < 1,ωωω =   ∼ N (000,ΣΣΣ ), (3.15)
1 2 t   ωωω
   γ 2,t = ϕ 2 γ 2,t−1 +ω 2,t ω 2,t
we have the analytical form of the Gaussian likelihood as,
T T
(cid:89) (cid:89)
f(γγγ |γγγ ,ϕ ,ϕ ,ΣΣΣ ) = f(γγγ |ϕ ,ϕ ,ΣΣΣ ) f(γγγ |γγγ ,ϕ ,ϕ ,ΣΣΣ )
t t−1 1 2 ωωω 1 1 2 ωωω t t−1 1 2 ωωω
t=1 t=2
(cid:112) (1−ϕ2)(1−ϕ2) (cid:40) 1 (cid:32) (1−ϕ2)γ2 (1−ϕ2)γ2 2ρ γ γ (cid:112) 1−ϕ2 (cid:112) 1−ϕ2 (cid:33)(cid:41)
= 1 2 exp − 1 1,1 + 2 2,1 − ω 1,1 2,1 1 2
(cid:0) 2π (cid:112) σ ω 2 1 σ ω 2 2 (1−ρ2 ω ) (cid:1)T 2(1−ρ2 ω ) σ ω 2 1 σ ω 2 2 σ ω1 σ ω2
(cid:89) T (cid:26) 1 (cid:18) (γ 1,t −ϕ 1 γ 1,t−1 )2 (γ 2,t −ϕ 2 γ 2,t−1 )2 2ρ ω (γ 1,t −ϕ 1 γ 1,t−1 )(γ 2,t −ϕ 2 γ 2,t−1 ) (cid:19)(cid:27)
· exp − + − ,
2(1−ρ2) σ2 σ2 σ σ
t=2 ω ω1 ω2 ω1 ω2
(3.16)
54

(3.16) can be treated as the Gaussian likelihood for the random vector,
|     |     |     |     |    |     |     |    |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
(cid:112)
1−ϕ2γ1,1
1σω1
|     |     |     |     |    |                    |         |    |     |        |
| --- | --- | --- | --- | --- | ------------------ | ------- | --- | --- | ------ |
|     |     |     |     |    | (cid:112) 1−ϕ2γ2,1 |         |    |     |        |
|     |     |     |     |    |                    |         |    |     |        |
|     |     |     |     |    |                    | 2σω2    |    |     |        |
|     |     |     |     |    |                    |         |    |     |        |
|     |     |     |     |     | γ1,2               | γ1,1    |     |     |        |
|     |     |     |     |    |                    | −ϕ      |    |     |        |
|     |     |     |     |    | σω1                | 1σω1    |    |     |        |
|     |     |     |     |    |                    |         |    |     |        |
|     |     |     | VVV | =  | γ2,2               | −ϕ γ2,1 | ,  |     | (3.17) |
|     |     |     |     |    |                    | 2σω2    |    |     |        |
|     |     |     |     |    | σω2                |         |    |     |        |
.
|     |     |     |     |    |      | .       |    |     |     |
| --- | --- | --- | --- | --- | ---- | ------- | --- | --- | --- |
|     |     |     |     |    |      | .       |    |     |     |
|     |     |     |     |    |      |         |    |     |     |
|     |     |     |     |    | γ1,T | γ1,T−1 |    |     |     |
|     |     |     |     |    | −ϕ   |         |     |     |     |
|     |     |     |     |    | σω1  | 1 σω1   |    |     |     |
|     |     |     |     |    |      |         |    |     |     |
|     |     |     |     |     | γ2,T | γ2,T−1  |     |     |     |
−ϕ 2
|                    |         |     |     |     | σω2 | σω2 |     |     |     |
| ------------------ | ------- | --- | --- | --- | --- | --- | --- | --- | --- |
| with its precision | matrix, |     |     |     |     |     |     |     |     |
|                    |         |     |    |     |     |     |     |    |     |
|                    |         |     | 1   | −ρ  | 0   | 0   | 0   | 0   |     |
ω
|     |       |     |    |     |     |     |       |     |        |
| --- | ----- | --- | --- | --- | --- | --- | ----- | ---- | ------ |
|     |       |     |    |     |     |     |       |     |        |
|     |       |     | −ρ | 1   | 0   | 0   | ... 0 | 0   |        |
|     |       |     |  ω |     |     |     |       |     |        |
|     |       |     |    |     |     |     |       |     |        |
|     |       |     |  0 | 0   | 1   | −ρ  | ... 0 | 0   |        |
|     |       |     |    |     |     | ω   |       |     |        |
|     |       | 1   |    |     |     |     |       |     |        |
|     | ΛΛΛ = |     |  0 | 0   | −ρ  | 1   | 0     | 0   | (3.18) |
|     | 1−ρ2  |     |    |     | ω   |     |       |     |        |
|     |       |     |    |     |     |     |       |     |        |
|     |       | ω   |     | .   | .   |     | ... . |      |        |
|     |       |     |    | .   | .   |     | .     |     |        |
|     |       |     |    | .   | .   |     | .     |     |        |
|     |       |     |    |     |     |     |       |     |        |
|     |       |     |    |     |     |     |       |     |        |
|     |       |     |  0 | 0   | 0   | 0   | ... 1 | −ρ  |        |
|     |       |     |    |     |     |     |       | ω   |        |
|     |       |     |    |     |     |     |       |     |        |
|     |       |     | 0   | 0   | 0   | 0   | −ρ    | ω 1  |        |
2T×2T
VVV
To implement latent effect with INLA, we also need to find the linear transformation between
| VVV and its internal | representation |     | UUU, |     |              |     |     |     |        |
| -------------------- | -------------- | --- | ---- | --- | ------------ | --- | --- | --- | ------ |
|                      |                |     |      |     | VVV =AAAUUU, |     |     |     | (3.19) |
55

where
|     |     |     |     |    |    |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
γ
1,1
|     |     |     |     |    |    |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|     |     |     |     |    |    |     |     |     |     |
|     |     |     |     | γ  |    |     |     |     |     |
1,2

|     |     |     |     |    | .  |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|     |     |     |     |    | .  |     |     |     |     |
.
|     |     |     |     |    |    |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|     |     |     |     |    |    |     |     |     |     |
|     |     |     |     |    |    |     |     |     |     |
γ
1,T
|     |     |     |     | UUU =  | ,  |     |     |     | (3.20) |
| --- | --- | --- | --- | ------- | --- | --- | --- | --- | ------ |
|     |     |     |     |        |    |     |     |     |        |
|     |     |     |     | γ      |    |     |     |     |        |
 2,1
|     |     |     |     |    |    |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|     |     |     |     |    |    |     |     |     |     |
γ
 2,2
|     |     |     |     |    |    |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|     |     |     |     |    | .  |     |     |     |     |
.
|     |     |     |     |    | .  |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|     |     |     |     |    |    |     |     |     |     |
|     |     |     |     |    |    |     |     |     |     |
γ
2,T
√
|     |    |     |     |     |     |     |     |    |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
1−ϕ2
|     |     | 1 0 |     | ... 0 | 0    | 0   | ... | 0   |     |
| --- | --- | --- | --- | ----- | ---- | --- | --- | --- | --- |
|     | σω1 |     |     |       | √    |     |     |     |     |
|     |    |     |     |       |      |     |     |    |     |
|     |    |     |     |       | 1−ϕ2 |     |     |    |     |
|     |  0 | 0   |     | ... 0 | 2    | 0   | ... | 0  |     |
σω2
|       |      |     |     |         |     |     |      |    |        |
| ----- | ----- | --- | --- | ------- | --- | --- | ---- | --- | ------ |
|       |      |     |     |         |     |     |      |    |        |
|       |  ϕ1  | 1   |     |         |     |     |      |    |        |
|       | −     |     |     | ... 0   | 0   | 0   | ...  | 0   |        |
|       |  σω1 | σω1 |     |         |     |     |      |    |        |
|       |      |     |     |         |     |     |      |    |        |
|       |      |     |     |         | ϕ1  |     |      |    |        |
| AAA = | 0     | 0   |     | ... 0   | −   | 1   | ...  | 0   | (3.21) |
|       |      |     |     |         | σω2 | σω2 |      |    |        |
|       |      |     |     |         |     |     |      |    |        |
|       |      |     |     | . .     |     |     | . .  |    |        |
|       |      |     |     | .       |     |     | .    |    |        |
|       |      |     |     |         |     |     |      |    |        |
|       |      |     |     |         |     |     |      |    |        |
|       |      |     |     | ϕ1 1    |     |     |      |    |        |
|       | 0     | ... | −   |         | 0   | 0   | ...  | 0   |        |
|       |      |     |     | σω1 σω1 |     |     |      |    |        |
|       |      |     |     |         |     |     |      |    |        |
|       | 0     | 0   |     | ... 0   | 0   | ... | − ϕ1 | 1   |        |
|       |       |     |     |         |     |     | σω2  | σω2 |        |
2T×2T
Using sparse matrix arithmetic in R, we can easily compute the covariance matrix of UUU through
matrix multiplication,
|     |     |     | Cov(UUU) | =AAA−1Cov(VVV)(AAA−1)T, |     |     |     |     |     |
| --- | --- | --- | -------- | ----------------------- | --- | --- | --- | --- | --- |
=ΛΛΛ−1.
where Cov(VVV) Then the complete implementation of bivariate AR(1) latent effect will be
done through the rgeneric() function in the R package, INLA. The choice of the prior distribution
canbecustomizedviaanappropriatereparameterizationapproachwithitscorrespondingJacobian
matrix. Bivariate random walk of order 1 can be done similarly except for the distributional
assumption on the initial γγγ . The Gaussian likelihood part of RW(1) is exactly the same as the
1
AR(1)’s, with ϕ 1 = ϕ 2 = 1. Implementation of multivariate AR temporal effect with higher orders
in INLA is also feasible, as long as the precision matrix of the latent effect can be analytically
specified, meanwhile the dimension of its precision matrix will increase quickly as a product of the
latent vector dimension and the length of the time series, with an expected higher computational
cost. However, that is beyond the scope of this paper. In the next section, the performance of
56

parameter recovery, in-sample prediction, and computational cost are demonstrated through an
extensive simulation study before one can apply this method practically.
| 3.4 Numerical    | study  |     |          |      |     |     |     |
| ---------------- | ------ | --- | -------- | ---- | --- | --- | --- |
| 3.4.1 Simulation | study: |     | INLA v.s | STAN |     |     |     |
Bayesian hierarchical models focus on the inference of sampled parameters from their joint poste-
rior distribution. However, computational efficiency can be of great concern if accurate statistical
inferenceisneededshortlyinrealapplications. Inthissection, weconductacomparisonsimulation
study through a simplified framework from (3.6), where no additional covariates are involved in the
link function to the conditional Poisson means. The comparison aims at showing the competitive
performance of INLA regarding parameter recovery and in-sample prediction at a much lower com-
putational cost versus the traditional MCMC method. In addition, the results also will encourage
the practitioners to implement customized latent effects via rgeneric() function with a correctly
specified precision matrix for accurate parameter inference. We have 200 simulations for each com-
bination of different numbers of assets (S = 10,15,20) and time intervals (T = 50,100,150) in
three different scenarios. The parameter setup is summarized in Table 6.
|     |          |       |               | σ−2 | σ−2           | σ−2 σ−2   |       |
| --- | -------- | ----- | ------------- | --- | ------------- | --------- | ----- |
|     | Scenario |       | ϕ ϕ           |     | ρ ωωω         |           | ρ ααα |
|     |          |       | 1 2           | ω1  | ω2            | α1 α2     |       |
|     |          | 1     | 0.5 0.8       | 6   | 7 0.6         | 10 10     | 0.6   |
|     |          | 2     | 0.5 0.8       | 6   | 7 0.6         | 10 10     | 0.2   |
|     |          | 3     | 0.5 0.8       | 6   | 7 0.6         | 10 10     | -0.6  |
|     |          | Table | 6: Parameters |     | for different | Scenarios |       |
Since the latent level correlation is of more interest to the practitioners for real application, we
explore the model inference performance by using different values of ρ ααα =0.6,0.2, and -0.6, which
displaysthedifferentstrengthsanddirectionsofthecorrelationbetweenthelevel-correlatedeffects.
As for the correlated temporal effect, we set a moderate correlation ρ ωωω = 0.6 to describe the overall
market behavior. Practitioners can always use one identical or two different uncorrelated temporal
effects to account for the extremely strong or weak temporal correlations via the default setting
in INLA, but the BVAR(1) framework provides more flexibility to implement a wider range of
latent temporal correlations. The AR coefficients are set to be ϕ = .5 and ϕ = .8 to indicate
|     |     |     |     |     |     | 1   | 2   |
| --- | --- | --- | --- | --- | --- | --- | --- |
57

a decent temporal dependence for each of the temporal effects. The precision parameters for the
latent effects are set to be relatively large so that their variances are all controlled under 1 to
avoid unreasonably extreme values generated in the simulation study. The conventional Bayesian
inferenceisimplementedinSTANbecauseofitshigh-qualitychainprovidedbyNUTSHamiltonian
MonteCarlo(HMC)sampler,comparedwithJAGSorNIMBLE(Berahaetal.,2021),whosedefault
samplers are the Gibbs samplers and Metropolis-Hastings sampler. We set the posterior sample
size to be 1000 after 1000 burn-ins for the traditional MCMC method. The choice of the priors for
| the parameters | between INLA | and STAN | are identical, |     |     |
| -------------- | ------------ | -------- | -------------- | --- | --- |
|                |              | (cid:18) | 1+ϕ (cid:19)   |     |     |
i
|     |     | log | ∼   | N(0,2),i = 1,2, |     |
| --- | --- | --- | --- | --------------- | --- |
1−ϕ
i
(3.22)
|     |     |     | ΣΣΣ ∼ | W (4,III ), |     |
| --- | --- | --- | ----- | ----------- | --- |
|     |     |     | ωωω   | 2 2×2       |     |
|     |     |     | ΣΣΣ ∼ | W (4,III ), |     |
|     |     |     | ααα   | 2 2×2       |     |
where III is an identity matrix. Between our framework and the traditional MCMC method,
2×2
we will evaluate their performances including parameter recovery rate, Mean Square Error (MSE),
Mean Absolute Error (MAE), Weighted Mean Absolute Percentage Error (WMAPE), and com-
putational cost. The parameter recovery rate is defined as the frequency of the true parameter
being captured in the default 95% credible interval out of these 200 simulations. MSE, MAE, and
WMAPE measure the average in-sample deviation between true count Y with predicted count
j,st
Yˆ
| j,st .MSE, MAE, | and WMAPE | are calculated | as, |     |     |
| --------------- | --------- | -------------- | --- | --- | --- |
n
1
|     |     |     | (cid:88) | )2,      |     |
| --- | --- | --- | -------- | -------- | --- |
|     |     | MSE | = (y     | −y       |     |
|     |     |     | n        | pred,i i |     |
i=1
n
1 (cid:88)
|     |     | MAE | =   | |y −y |, | (3.23) |
| --- | --- | --- | --- | -------- | ------ |
|     |     |     | n   | pred,i i |        |
i=1
|     |     |       | (cid:80)n | |y −y |      |     |
| --- | --- | ----- | --------- | ------------ | --- |
|     |     |       |           | i=1 pred,i i |     |
|     |     | WMAPE | =         | .            |     |
(cid:80)n |y |
i=1 i
The parameter recovery performances among different scenarios are summarized in Table 7 and
8. The parameter recovery rate reflects the credibility of the proposed framework in terms of the
statistical inference on the parameters of interest. Regarding the in-sample prediction accuracy
| and computational | cost, the | comparison | results | are in Table 9. |     |
| ----------------- | --------- | ---------- | ------- | --------------- | --- |
58

Regarding the parameter recovery performance, our framework shows a competitive perfor-
mance. First of all, the latent correlation recovery rate is comparable to the STAN’s performance.
For the temporal correlation, both of these two methods have a recovery rate as high as over
90% for most scenarios. For the latent level correlation, the parameter recovery is better (around
95%) when the true value is near 0 (ρ = 0.2) but is less satisfactory when ρ is close to 1 (75%
ααα ααα
to 90% in Scenario 1 and Scenario 3). Since the temporal effects have slightly larger variances
(σ−2 = 6,σ−2 = 7) than the level-correlated effects do (σ−2 = 10,σ−2 = 10) in the simulation
α1 α2 ω1 ω2
setup, a larger sample size, i.e., a larger value of T will enhance the recovery of level correlation.
Second, the recovery rates for the precision parameters for both latent effects are satisfactory re-
gardless of ρ . The recovery rates of the AR coefficients are also okay with the INLA but we need
ααα
to point out that the recovery of ϕ is not as ideal as the MCMC approach when the latent level
ω2
correlation ρ is negative. However, in real applications, a positive correlation between different
ααα
types of counts is more common as both transactions of different risk levels are usually driven by
the trading intensity of the corresponding asset in a positive manner. This scenario is just for the
illustration of an overall satisfactory parameter recovery performance of the INLA implementation
of the BVAR(1)-LCM framework. In addition, the temporal effects are explained as the overall
market behavior and the direct interpretation of AR coefficients in the latent state is of less inter-
est to the practitioners, as long as the AR coefficients have reasonable estimates and the overall
model adequacy and prediction are satisfactory. Despite a few exceptions, the INLA method, as an
approximate Bayesian inference tool, has a competitive parameter recovery performance in general
compared with the full Bayesian inference approach based on the joint posterior distribution.
We’ve also considered the in-sample performance and computational time between the INLA
methodandtheSTANmethod. InTable9, Thereisnosignificantdifferencebetweenthein-sample
deviationsfromthetruecountdataundervariousmeasurements. Withsimilarin-sampleprediction
performance, the INLA method has superior computational efficiency over the STAN method. The
current MCMC sampling size is 2000 including the 1000 burn-in samples. The MCMC sampling
procedurecanstilltakemorethantheten-foldcomputationaltimeconsumedbytheINLAmethod.
As the dimension of financial data increases, higher computational costs can be expected by the
STAN method. When dealing the financial data containing S = 20 assets with each count time
serieswithlengthT = 150,theSTANmethodtakesonaverageover2000secondstomakeinferences
59

based on 1000 posterior samples. As for the irregularity of the computational time of the INLA
method,themainreasoncouldbecausedbytherandomnessinthesimulationstudy. Intheinternal
computing procedure, when the generated data deviates too much from the prior distribution, the
default initial value will impact the convergence speed of the model, and sometimes a problematic
initial value can definitely cause a re-initialization of the computing procedure thus leading to a
longer computational time. Even though the computational time is not proportionally related to
the data dimension for the INLA method, its computational cost reduction is already significant
enough that the STAN method is no match in this perspective.
In this simulation study, we compared the INLA method with the traditional MCMC method
formodelimplementationinthreeaspects: parameterrecoveryrate, in-samplepredictionaccuracy,
and computational efficiency. We have shown the INLA method provides satisfactory performance
in parameter recovery except for a few cases, with similar in-sample prediction accuracy, and much
lower computational cost. In real applications in the HFT market, practitioners need to model
financial data on a large scale and make reasonable decisions promptly, so the INLA method can
provide a better trade-off between computational efficiency and statistical inference accuracy. As
fortheevaluationofout-of-sampleprediction,wewillconductthestudyonrealdataacrossdifferent
models for real applications. We will adopt the INLA method for model implementation due to
the size of the real financial data to save computational time.
3.4.2 Real application
Before we illustrate how to apply our model to the high-frequency financial market, we will first
give a brief background introduction to the financial market including how high-frequency trading
(HFT)firmsmakeprofitsandsomeempiricalpatternsoffinancialdata. Then,wearegoingtoapply
our model framework to investigate the market dynamics of different stock sectors. Meanwhile, we
will also compare additional existing model candidates for model selection. Next, we will account
for the interrelation among the multiple stocks within the same sector, via correlated temporal
effect and level-correlated effect, including exogenous covariates of interest. Finally, we will provide
marketbehaviorinterpretationsusingourmodelandsomeperspectivesonwhatbenefitsourmodel
can bring to practitioners.
60

|          |     |     |      | σ−2  |      | σ−2  |      |      |      |      |      |          |
| -------- | --- | --- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | -------- |
|          |     |     |      |      |      |      |      | ρ    |      | ϕ    |      | ϕ        |
| Scenario | S   | T   |      | ω1   |      | ω2   |      | ωωω  |      | ω1   |      | ω2       |
|          |     |     | INLA | STAN | INLA | STAN | INLA | STAN | INLA | STAN | INLA | STAN     |
|          |     | 50  | 0.78 | 0.93 | 0.8  | 0.93 | 0.92 | 0.91 | 0.82 | 0.94 | 0.88 | 0.98     |
|          | 10  | 100 | 0.89 | 0.96 | 0.92 | 0.95 | 0.94 | 0.92 | 0.94 | 0.94 | 0.86 | 0.94     |
|          |     | 150 | 0.89 | 0.96 | 0.89 | 0.92 | 0.98 | 0.95 | 0.94 | 0.96 |      | 0.9 0.96 |
|          |     | 50  | 0.85 | 0.95 | 0.76 | 0.93 | 0.94 | 0.93 | 0.86 | 0.96 | 0.78 | 0.95     |
1(ρ = .6) 15 100 0.89 0.94 0.87 0.94 0.95 0.93 0.94 0.96 0.89 0.94
ααα
|     |     | 150 | 0.91 | 0.96 | 0.9  | 0.94 | 0.95 | 0.94 | 0.92 | 0.95     | 0.92 | 0.95 |
| --- | --- | --- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | -------- | ---- | ---- |
|     |     | 50  | 0.8  | 0.94 | 0.82 | 0.92 | 0.94 | 0.92 | 0.84 | 0.95     | 0.82 | 0.98 |
|     | 20  | 100 | 0.87 | 0.94 | 0.89 | 0.94 | 0.95 | 0.92 | 0.96 | 0.98     | 0.89 | 0.95 |
|     |     | 150 | 0.92 | 0.96 | 0.9  | 0.92 | 0.96 | 0.94 | 0.92 | 0.93     | 0.89 | 0.96 |
|     |     | 50  | 0.84 | 0.96 | 0.83 | 0.96 | 0.9  | 0.86 | 0.83 | 0.95     | 0.84 | 0.92 |
|     | 10  | 100 | 0.9  | 0.92 | 0.86 | 0.92 | 0.96 | 0.94 | 0.94 | 0.94     | 0.84 | 0.94 |
|     |     | 150 | 0.94 | 0.96 | 0.95 | 0.96 | 0.92 | 0.92 | 0.94 | 0.96     | 0.88 | 0.95 |
|     |     | 50  | 0.86 | 0.96 | 0.77 | 0.94 | 0.92 | 0.9  |      | 0.8 0.94 | 0.82 | 0.96 |
2(ρ ααα = .2) 15 100 0.86 0.95 0.88 0.94 0.94 0.94 0.94 0.98 0.86 0.96
|     |     | 150 | 0.91 | 0.94 | 0.89 | 0.92 | 0.91 | 0.92 | 0.94 | 0.94 | 0.86 | 0.94     |
| --- | --- | --- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | -------- |
|     |     | 50  | 0.81 | 0.96 | 0.86 | 0.97 | 0.94 | 0.9  | 0.88 | 0.94 | 0.84 | 0.94     |
|     | 20  | 100 | 0.9  | 0.96 | 0.9  | 0.92 | 0.96 | 0.93 | 0.92 | 0.96 | 0.84 | 0.96     |
|     |     | 150 | 0.9  | 0.95 | 0.9  | 0.93 | 0.94 | 0.92 | 0.92 | 0.94 | 0.77 | 0.92     |
|     |     | 50  | 0.83 | 0.97 | 0.84 | 0.94 | 0.85 | 0.86 | 0.85 | 0.97 |      | 0.9 0.97 |
|     | 10  | 100 | 0.88 | 0.94 | 0.88 | 0.9  | 0.91 | 0.88 | 0.94 | 0.95 | 0.88 | 0.95     |
|     |     | 150 | 0.92 | 0.94 | 0.9  | 0.92 | 0.88 | 0.85 | 0.94 | 0.94 | 0.86 | 0.96     |
|     |     | 50  | 0.83 | 0.95 | 0.84 | 0.92 | 0.88 | 0.84 | 0.88 | 0.93 | 0.85 | 0.95     |
3(ρ = −.6) 15 100 0.9 0.94 0.92 0.94 0.95 0.93 0.92 0.96 0.82 0.94
ααα
|     |     | 150 | 0.94 | 0.96 | 0.86 | 0.92 | 0.92 | 0.91 |      | 0.9 0.94 | 0.78 | 0.94 |
| --- | --- | --- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | -------- | ---- | ---- |
|     |     | 50  | 0.81 | 0.94 | 0.79 | 0.94 | 0.94 | 0.92 | 0.84 | 0.98     | 0.76 | 0.96 |
|     | 20  | 100 | 0.88 | 0.94 | 0.88 | 0.97 | 0.92 | 0.9  | 0.92 | 0.97     | 0.69 | 0.94 |
|     |     | 150 | 0.9  | 0.96 | 0.88 | 0.93 | 0.92 | 0.9  | 0.94 | 0.95     | 0.62 | 0.92 |
Table 7: Parameter recovery rate comparison between INLA and STAN for correlated temporal
| effects ω and | ω   |     |     |     |     |     |     |     |     |     |     |     |
| ------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1             | 2   |     |     |     |     |     |     |     |     |     |     |     |
61

|     |     |     | σ−2 |     | σ−2 |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- |
ρ
| Scenario  | S T    |      | α1   |      | α2   |      | ααα  |
| --------- | ------ | ---- | ---- | ---- | ---- | ---- | ---- |
|           |        | INLA | STAN | INLA | STAN | INLA | STAN |
|           | 50     | 0.9  | 0.9  | 0.96 | 0.94 | 0.74 | 0.72 |
|           | 10 100 | 0.93 | 0.92 | 0.96 | 0.94 | 0.84 | 0.82 |
|           | 150    | 0.92 | 0.91 | 0.96 | 0.96 | 0.84 | 0.84 |
|           | 50     | 0.92 | 0.92 | 0.92 | 0.9  | 0.83 | 0.8  |
| 1(ρ = .6) | 15 100 | 0.95 | 0.92 | 0.92 | 0.9  | 0.84 | 0.84 |
ααα
|               | 150    | 0.96 | 0.94 | 0.97 | 0.96 | 0.87 | 0.84 |
| ------------- | ------ | ---- | ---- | ---- | ---- | ---- | ---- |
|               | 50     | 0.92 | 0.93 | 0.94 | 0.9  | 0.81 | 0.8  |
|               | 20 100 | 0.94 | 0.93 | 0.94 | 0.93 | 0.87 | 0.89 |
|               | 150    | 0.92 | 0.92 | 0.95 | 0.95 | 0.88 | 0.86 |
|               | 50     | 0.96 | 0.95 | 0.98 | 0.96 | 0.95 | 0.94 |
|               | 10 100 | 0.95 | 0.94 | 0.96 | 0.94 | 0.93 | 0.94 |
|               | 150    | 0.96 | 0.96 | 0.96 | 0.94 | 0.98 | 0.96 |
|               | 50     | 0.95 | 0.97 | 0.94 | 0.96 | 0.92 | 0.95 |
| 2(ρ ααα = .2) | 15 100 | 0.97 | 0.95 | 0.94 | 0.92 | 0.95 | 0.96 |
|               | 150    | 0.94 | 0.96 | 0.96 | 0.96 | 0.94 | 0.95 |
|               | 50     | 0.96 | 0.94 | 0.94 | 0.96 | 0.93 | 0.93 |
|               | 20 100 | 0.96 | 0.96 | 0.92 | 0.95 | 0.97 | 0.96 |
|               | 150    | 0.94 | 0.96 | 0.94 | 0.94 | 0.96 | 0.95 |
|               | 50     | 0.95 | 0.92 | 0.93 | 0.92 | 0.66 | 0.61 |
|               | 10 100 | 0.94 | 0.94 | 0.96 | 0.96 | 0.79 | 0.75 |
|               | 150    | 0.94 | 0.92 | 0.94 | 0.94 | 0.84 | 0.83 |
|               | 50     | 0.92 | 0.92 | 0.91 | 0.9  | 0.78 | 0.74 |
| 3(ρ = −.6)    | 15 100 | 0.95 | 0.96 | 0.93 | 0.92 | 0.82 | 0.8  |
ααα
|     | 150    | 0.94 | 0.94 | 0.93 | 0.91 | 0.9  | 0.84 |
| --- | ------ | ---- | ---- | ---- | ---- | ---- | ---- |
|     | 50     | 0.92 | 0.92 | 0.94 | 0.94 | 0.81 | 0.8  |
|     | 20 100 | 0.93 | 0.92 | 0.96 | 0.96 | 0.86 | 0.83 |
|     | 150    | 0.96 | 0.94 | 0.96 | 0.96 | 0.9  | 0.86 |
Table 8: Parameter recovery rate comparison between INLA and STAN for level-correlated effects
α and α
1 2
62

|     |     | MAE |     | MSE | WMAPE |     | CPU.used |     |
| --- | --- | --- | --- | --- | ----- | --- | -------- | --- |
Scenario S T
|        | INLA  | STAN  | INLA  | STAN  | INLA  | STAN  | INLA   | STAN    |
| ------ | ----- | ----- | ----- | ----- | ----- | ----- | ------ | ------- |
| 50     | 1.524 | 1.533 | 3.691 | 3.772 | 0.168 | 0.169 | 5.849  | 146.802 |
| 10 100 | 1.573 | 1.576 | 3.947 | 4.005 | 0.173 | 0.175 | 19.458 | 402.746 |
| 150    | 1.595 | 1.593 | 4.026 | 4.084 | 0.176 | 0.176 | 9.016  | 603.799 |
| 50     | 1.558 | 1.569 | 3.876 | 3.979 | 0.176 | 0.178 | 6.742  | 249.312 |
1(ρ ααα = .6) 15 100 1.613 1.609 4.126 4.177 0.179 0.178 6.323 444.649
| 150    | 1.63  | 1.626 | 4.217 | 4.268 | 0.18  | 0.18  | 11.162 | 1147.675 |
| ------ | ----- | ----- | ----- | ----- | ----- | ----- | ------ | -------- |
| 50     | 1.594 | 1.599 | 4.062 | 4.121 | 0.177 | 0.177 | 16.811 | 358.517  |
| 20 100 | 1.633 | 1.632 | 4.238 | 4.308 | 0.181 | 0.181 | 7.366  | 676.496  |
| 150    | 1.646 | 1.642 | 4.316 | 4.364 | 0.182 | 0.182 | 13.754 | 1868.829 |
| 50     | 0.98  | 0.985 | 1.444 | 1.504 | 0.094 | 0.094 | 11.92  | 232.927  |
| 10 100 | 0.982 | 0.985 | 1.446 | 1.501 | 0.095 | 0.095 | 27.974 | 474.528  |
| 150    | 1.008 | 0.989 | 1.508 | 1.511 | 0.095 | 0.093 | 21.403 | 1407.225 |
| 50     | 0.984 | 0.994 | 1.457 | 1.551 | 0.094 | 0.096 | 9.118  | 260.872  |
2(ρ = .2) 15 100 1.009 0.991 1.512 1.519 0.097 0.095 9.571 488.026
ααα
| 150    | 1.01  | 0.992 | 1.515 | 1.521  | 0.096 | 0.095 | 16.254 | 1147.024 |
| ------ | ----- | ----- | ----- | ------ | ----- | ----- | ------ | -------- |
| 50     | 0.988 | 1.014 | 1.466 | 1.631  | 0.095 | 0.097 | 28.657 | 507.624  |
| 20 100 | 1.013 | 1.002 | 1.525 | 1.568  | 0.097 | 0.096 | 14.959 | 1093.478 |
| 150    | 1.011 | 0.993 | 1.518 | 1.523  | 0.097 | 0.095 | 21.812 | 2124.168 |
| 50     | 1.476 | 1.483 | 3.586 | 3.651  | 0.124 | 0.125 | 6.962  | 319.741  |
| 10 100 | 1.537 | 1.544 | 3.927 | 3.997  | 0.127 | 0.127 | 31.864 | 586.252  |
| 150    | 1.585 | 1.583 | 4.156 | 4.213  | 0.124 | 0.124 | 10.757 | 1454.869 |
| 50     | 1.55  | 1.651 | 3.977 | 19.226 | 0.126 | 0.133 | 13.785 | 1134.083 |
3(ρ = −.6) 15 100 1.601 1.603 4.257 4.345 0.127 0.127 9.615 1662.712
ααα
| 150    | 1.625 | 1.624 | 4.399 | 4.457 | 0.129 | 0.129 | 11.927 | 2428.919 |
| ------ | ----- | ----- | ----- | ----- | ----- | ----- | ------ | -------- |
| 50     | 1.572 | 1.577 | 4.119 | 4.173 | 0.132 | 0.132 | 26.201 | 1399.757 |
| 20 100 | 1.639 | 1.639 | 4.49  | 4.554 | 0.129 | 0.129 | 15.304 | 2331.487 |
| 150    | 1.66  | 1.659 | 4.616 | 4.673 | 0.128 | 0.128 | 14.68  | 4687.846 |
Table 9: In-sample prediction and computational time comparison between INLA and STAN
63

3.4.2.1 High-frequency trading (HFT) background According to Carrion (2013) and
Dutta et al. (2022), one source of profit-making in HFT is related to intraday market time skills,
buying when prices are temporarily low and selling when prices are temporarily high. This is not
solely driven by very short-term signals or trading at fleeting prices, but by the existence of eco-
nomically significant predictability in intraday prices. HFTs execute their trades at better prices
than non-HFTs, have lower processing costs, and have some ability to avoid adverse selection costs
on larger trades when supplying liquidity. To cover these fixed processing costs, the HFT firms
earnverysmallprofitspertradebutplacelargevolumesoforders, makingprofitsbaseduponsmall
amounts of predictive power on large trading volumes.
From the empirical data analysis of the raw transaction-level data, the price fluctuation regard-
ing log price return within short time intervals only has a small range, and there are numerous
transactions made with zero returns. Therefore, the practitioners in the market need to acknowl-
edge that making a profit through a significantly high price return in HFT is not supported by
the intrinsic market dynamics, and they can strategically place orders according to the numbers of
transactions with zero return and non-zero return in a short term. For example, if the number of
non-zero returns is large, it implies the asset price is volatile and short-term profit can be expected
by supplying liquidity according to the price movement prediction with other models. Otherwise,
buy-in opportunities can be considered at the occurrence of an abundance of zero returns since the
price is temporarily stable.
In addition, HFT improves liquidity (Hendershott and Riordan, 2013), reduces volatility (Has-
brouck and Saar, 2013), and yields a different market microstructure than the conventional finan-
cial market without HFT (Ammar et al., 2020). There has been some research work conducted
to account for the association between volatility and liquidity in the conventional financial market
(Deuskar, 2006; Bedowska-S´ojka and Kliber, 2019). Although there is only a general confirmation
that liquidity and volatility are strongly associated, we can as well explore their relationship in the
HFT setting with count data. Since there are various types of measurements to quantify liquidity
and volatility, it is explicable that their relationship can take many forms. O’hara (1998) points
out that liquidity is generally defined as the ability to trade large volumes quickly at low cost, and
usually such trading doesn’t cause a drastic impact on price change. We can use the total number
of transactions within a fixed short time interval as a surrogate measurement of volatility for count
64

data because the trading volumes among these short intervals are generally large and don’t have a
significant difference, the total trading volume can be roughly regarded as a multiple of the number
of transactions. From this perspective, our method can account for this short-term association
| between | liquidity and | volatility in | a time-dependent | manner. |     |
| ------- | ------------- | ------------- | ---------------- | ------- | --- |
3.4.2.2 High-frequency count data description The transaction-level data for our analysis
are retrieved from the Trade and Quote (TAQ) database from Wharton Research Data Services
(WRDS). The TAQ database contains intraday transactions (trades and quotes) data for all secu-
rities listed on the New York Stock Exchange (NYSE) and American Stock Exchange (AMEX), as
well as Nasdaq National Market System (NMS) and Small-Cap issues. Among all the HFT data,
we focus only on the trading data from three GICS sectors in January 2013, Healthcare, Energy,
and Industrials.
We first pre-process the raw HFT data. Let t = 1,...,T denote the order of the fixed time
intervals (e.g., 2-minute intervals in our study) within a trading day, let i t = 1,...,N t be the order
of the transactions within the time interval t due to the idiosyncrasy of high-frequency financial
data and the fact that the number of transactions in a given interval is random. Let T , P , and
it it
R it be the corresponding transaction time, price, and log returns at the i t th transaction, with
|     |     |     | P   | −P  |     |
| --- | --- | --- | --- | --- | --- |
it (i−1)t.
R it =
P
(i−1)t
We construct two new variables, Y H,t and Y L,t , i.e., transaction count of high-risk level and count
of low-risk level respectively. For a user-defined threshold τ > 0, let the incidence and count of the
| log return | being greater | than τ in | the time interval | t be |     |
| ---------- | ------------- | --------- | ----------------- | ---- | --- |


|     |     |     |  1 if |R | | > τ, |     |
| --- | --- | --- | ---------- | ------ | --- |
it
|     |     | B   | =   | then | (3.24) |
| --- | --- | --- | --- | ---- | ------ |
it
|     |     |     |   0 if |R | | ≤ τ, |     |
| --- | --- | --- | ------------ | ------ | --- |
it

|     |     |     |   Y = | (cid:80)N t B |     |
| --- | --- | --- | -------- | ------------- | --- |
|     |     |     | H,t      | it            |     |
it= 1
(3.25)

|     |     |     |  Y = | N −Y  |     |
| --- | --- | --- | ------ | ----- | --- |
|     |     |     | L,t    | t H,t |     |
Choice of τ: Due to limited literature resources on HFT data, the threshold selection for
65

defining high-risk level counts is data-driven or of practitioners’ interest. The larger the threshold
τ, thesparserthecountofhigh-risklevelwillbe, anddealingwithinflatedzeroswillrequirespecific
caution. In the following simple example of the stock ABT on 01/02/2013, in Table 10, τ = 0.0005,
or five basis points. The definition of extremeness can be determined by practitioners, for example,
Brogaard et al. (2018) defined the extreme price movement in HFT using 99.9% quantile of the
return distribution.Baron et al. (2019) selected 0.1% quantile of the distribution of response time
(time-stamp difference) to define Decision-Latency to capture the fastest reaction time. Due to
limited literature on the distribution of high-frequency price log returns, we are going to select
τ = 0 and categorize the transactions with non-zero log returns into the high-risk group and the
oneswithzerologreturnsintothelow-riskgroup. Suchachoiceofτ = 0hasanaturalinterpretation
ofthepricevolatilityandcanpreventimbalancedcountdatawithexcessivezerocountsonhigh-risk
levels if the threshold is not selected appropriately. Since the number of transactions with zero log
returns takes a significant proportion under the high-frequency circumstance, the real applications
in this paper will be based on τ = 0 for demonstration. However, customization of τ for different
assets is feasible as long as extra financial domain knowledge and the data empirical characteristics
justify the threshold specification.
| i Time          | (T )       | Price   | (P ) | Log returns   | (R ) |
| --------------- | ---------- | ------- | ---- | ------------- | ---- |
|                 | i          |         | i    |               | i    |
| 1 9:30:00.531   |            | 32.3300 |      | NaN           |      |
| 2 9:30:03.167   |            | 32.3000 |      | -0.000929     |      |
| 3 9:30:08.307   |            | 32.3500 |      | 0.000463      |      |
| 4 9:30:08.311   |            | 32.3250 |      | 0.000308      |      |
| 5 9:30:08.313   |            | 32.3525 |      | -0.000001     |      |
| ...             | ...        | ...     |      | ...           |      |
| 652 9:31:58.736 |            | 32.2300 |      | 0.000310      |      |
| 653 9:31:58.886 |            | 32.2300 |      | 0.000000      |      |
| 654 9:31:59.287 |            | 32.2300 |      | 0.000000      |      |
| 655 9:31:59.611 |            | 32.2200 |      | -0.000310     |      |
| 656 9:31:59.909 |            | 32.2300 |      | 0.000310      |      |
| Table 10:       | An example | of raw  | data | for the stock | ABT  |
Let YYY = (Y ,Y )′ be a 2-dimensional vector of count responses of high-risk transactions
st H,st L,st
and low-risk ones for the sth stock at equally spaced times t, for s = 1,...,S and t = 1,...,T
(T = 195). The data includes D = 21 trading days in January 2013. For each trading day, there
are 195 time intervals (2 minutes). Take the stock ABT on 01/02/2013 in the time window from
66

Stock Count Type Time Duration mean (in seconds) logsize mean
|     | ABT 413 | High | risk 9:30 | 0.283 | 5.241 |
| --- | ------- | ---- | --------- | ----- | ----- |
|     | ABT 306 | High | risk 9:32 | 0.392 | 5.168 |
|     | ABT 269 | High | risk 9:34 | 0.446 | 5.194 |
|     | ABT 244 | Low  | risk 9:30 | 0.452 | 5.196 |
|     | ABT 218 | Low  | risk 9:32 | 0.553 | 5.189 |
|     | ABT 234 | Low  | risk 9:34 | 0.513 | 5.061 |
Table 11: Data structure for INLA modeling. count data for stock ABT between 9:30 and 9:34
| a.m. on      | 01/02/2013. |       |           |     |     |
| ------------ | ----------- | ----- | --------- | --- | --- |
| 9:30 to 9:34 | for example | as in | Table 11: |     |     |
In Table 11, the last two columns are the two covariates of our interest. Duration mean is
the average duration between two consecutive transactions of the same type. The i-th financial
| duration, | x , within | an interval | is defined as, |     |     |
| --------- | ---------- | ----------- | -------------- | --- | --- |
i
|     |     |     | x = t −t | ,   |     |
| --- | --- | --- | -------- | --- | --- |
i i i−1
where t i is the time point when the i-th financial event occurs. In our study, financial events
are defined as transactions of different risk levels. Within a time interval, a large collection of
successive short durations usually reflect a high trading intensity in the market thus leading to a
large count of transactions. It would be useful to investigate and quantify the association between
count and average duration. In addition, a common delineation for the intra-day periodic trading
patterns is the phenomenon of high trading intensity (shorter durations) during the opening and
closing periods of a trading day and relatively lower trading activity around noon. In Figure 7, the
diurnaleffectcanbeobservedasaU-shapepatternintheintra-daycountdataandanupside-down
U-shape pattern in the average duration data. Therefore, including average duration as a covariate
in our model facilitates the accommodation for diurnal effect explanation. Another covariate of our
interest is related to trade size. Due to the wide range of trade sizes for the transactions, we choose
a logarithmic transformation on the trade size and calculate the average log trade size for the time
intervals. Since price changes fluctuate significantly when a large number of shares are traded, it
is also of our interest to account for this relationship between count and log trade size.
Similar stocks being in each sector, the co-movement of these time series is related to market
67

ABT
400
200
0
0 50 100 150 200
Time interval
tnuoC
ABT
7.5
5.0
2.5
0.0
0 50 100 150 200
Time interval
noitarud
degarevA
Count type High−risk Low−risk
Figure 7: Diurnal pattern exhibited in observed counts and averaged duration in 2-min intervals
for stock ABT on 01/02/2023.
behavior evaluation for the corresponding industry, the multi-asset pattern is shown in Figure 8.
Before further investigation of the market micro-structure, we will implement different models on
the real data, and evaluate model adequacy and out-of-sample prediction in the next step.
3.4.2.3 Model adequacy and prediction accuracy comparisons In addition to our pro-
posed framework, we include a list of other model candidates to be considered. To begin with, the
correlated bi-variate AR process with level correlation model (BVAR(1)-LCM) from (3.6) is one
of the candidates. However, due to the non-stationary feature of count data, it is not uncommon
to use a random walk (RW) process instead of an AR process to model the long memory tem-
poral dependence. Therefore, the correlated bi-variate RW process with a level correlation model
(BVRW(1)-LCM) with fewer parameters becomes another one of the model candidates. We also
consider AR and RW processes with uncorrelated latent temporal effect with ρ = 0 as a spe-
ωωω
cial case. In addition, we include the last candidate, proposed by Ma et al. (2008), which can be
regarded as an existing method using only the level correlation model (LCM) using the MCMC
method, as a static LCM model without temporal latent effect γ in (3.6). As for the fixed ef-
j,t
fects, we incorporate different fixed effects for the conditional mean of the count at different risk
68

Energy on 20130102 Healthcare on 20130102 Industrials on 20130102
|     | APC COP | CVX |     | ABT | AMGN | BAX | BIIB |     | BA  | CAT | EMR | FDX |
| --- | ------- | --- | --- | --- | ---- | --- | ---- | --- | --- | --- | --- | --- |
800
|     |     |     |     | 750 |     |     |     | 750 |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 600 |     |     |     | 500 |     |     |     | 500 |     |     |     |     |
|     |     |     |     | 250 |     |     |     | 250 |     |     |     |     |
400
|     |     |     |     | 0   |     |     |     |     | 0   |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
200
|     |     |     |     | BMY | CELG | GILD | JNJ |     | GD  | GE  | HON | LMT |
| --- | --- | --- | --- | --- | ---- | ---- | --- | --- | --- | --- | --- | --- |
0
|     |         |     |     | 750 |     |     |     | 750 |     |     |     |     |
| --- | ------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|     | DVN HAL | OXY |     |     |     |     |     |     |     |     |     |     |
|     |         |     |     | 500 |     |     |     | 500 |     |     |     |     |
800
|       |     |     |       | 250 |     |     |     | 250   |     |     |     |     |
| ----- | --- | --- | ----- | --- | --- | --- | --- | ----- | --- | --- | --- | --- |
| 600   |     |     |       | 0   |     |     |     |       | 0   |     |     |     |
| tnuoC |     |     | tnuoC |     |     |     |     | tnuoC |     |     |     |     |
| 400   |     |     |       | LLY | MDT | MRK | PFE |       | MMM | NSC | RTN | UNP |
200
|     |         |          |         | 750 |     |     |     | 750 |     |     |     |     |
| --- | ------- | -------- | ------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|     | 0       |          |         | 500 |     |     |     | 500 |     |     |     |     |
|     |         | 0 05 001 | 051 002 | 250 |     |     |     | 250 |     |     |     |     |
|     | SLB XOM |          |         |     |     |     |     |     |     |     |     |     |
|     |         |          |         | 0   |     |     |     |     | 0   |     |     |     |
800
|     |     |     |     |     | 0 05 001 | 051 002 0 05 001 | 051 002 0 05 001 | 051 002 |     |     | 0 05 001 051 002 0 | 05 001 051 002 |
| --- | --- | --- | --- | --- | -------- | ---------------- | ---------------- | ------- | --- | --- | ------------------ | -------------- |
|     |     |     |     | UNH |          |                  |                  |         | UPS | UTX |                    |                |
600
|     |     |     |     | 750 |     |     |     | 750 |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
400
|     |     |     |     | 500 |     |     |     | 500 |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
200
|     |     |     |     | 250 |     |     |     | 250 |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|     | 0   |     |     | 0   |     |     |     |     | 0   |     |     |     |
0 05 001 051 002 0 05 001 051 002 0 05 001 051 002 0 05 001 051 002 0 05 001 051 002
|     | Time interval |     |            |     | Time interval |     |          |     |     | Time interval |     |     |
| --- | ------------- | --- | ---------- | --- | ------------- | --- | -------- | --- | --- | ------------- | --- | --- |
|     |               |     | Count type |     | High−risk     |     | Low−risk |     |     |               |     |     |
Figure 8: Count data for three GICS sectors: Energy, Health care, Industrials
levels. These model candidates will be compared from two aspects: in-sample model adequacy
and out-of-sample prediction accuracy. To compare the in-sample model adequacy, we use the
Watanabe-Akaike Information Criterion (WAIC) (Watanabe, 2010; Gelman et al., 2014) and De-
vianceInformationCriterion(DIC).WAICandDICarepredictiveinformationcriteriaforBayesian
models, smaller values indicate a better model. WAIC (Watanabe-Akaike information criterion) is
| computed | as, |     |     |     |     |     |     |     |     |     |     |     |
| -------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
(3.26)
|     |     |     | WAIC | = −2logp | post | (y)+2p | WAIC | ,   |     |     |     |     |
| --- | --- | --- | ---- | -------- | ---- | ------ | ---- | --- | --- | --- | --- | --- |
where p is the correction for the effective number of parameters to adjust for overfitting
WAIC
69

| and there | are two | approaches | available | for the | correction. |     |     |
| --------- | ------- | ---------- | --------- | ------- | ----------- | --- | --- |
n
(cid:88)
|     |     | p WAIC1 | = 2 | (log(E post | p(y i |θ))−E | post (logp(y i |θ))), |        |
| --- | --- | ------- | --- | ----------- | ------------ | --------------------- | ------ |
|     |     |         |     | i=1         |              |                       | (3.27) |
n
(cid:88)
|     |     | p     | =   | var (logp(y | |θ)). |     |     |
| --- | --- | ----- | --- | ----------- | ----- | --- | --- |
|     |     | WAIC2 |     | post        | i     |     |     |
i=1
| DIC is | computed | as, |     |               |       |     |        |
| ------ | -------- | --- | --- | ------------- | ----- | --- | ------ |
|        |          |     | DIC | = −2logp(y|θˆ | )+2p  | ,   | (3.28) |
|        |          |     |     |               | Bayes | DIC |        |
θˆ
where is the posterior mean of the parameter and p is the correction for the effective
|           | Bayes       |     |     |             |      | DIC           |        |
| --------- | ----------- | --- | --- | ----------- | ---- | ------------- | ------ |
| number of | parameters, |     |     |             |      |               |        |
|           |             |     | p = | 2(logp(y|θˆ | )−E  | (logp(y|θ))). | (3.29) |
|           |             |     | DIC | Bayes       | post |               |        |
For out-of-sample prediction, we use the first 180 observations as a training set to predict
the last 15 observations, i.e., the count data in the last 30 minutes of a trading day. A smaller
value of MAE, MSE, and WMAPE regarding the prediction and actual count indicates a better
| out-of-sample | prediction | performance. |     |     |     |     |     |
| ------------- | ---------- | ------------ | --- | --- | --- | --- | --- |
There are three sectors of count data in our analysis, and each sector contains 21 days trading
days. The total number of data sets will be 3×21 = 63. Applying the described criteria above, we
select the best model under each measurement. Table 12 shows the model comparison results. The
percentageinthetableistheproportionoutofthe63datasetsthatfavorthespecificmeasurement
regardingthemodeladequacyorout-of-sampleperformanceaccuracy. Around80%ofthedatasets
favor the BVAR(1)-LCM or BVRW(1)-LCM model regarding model adequacy and more than 90%
regarding the out-of-sample prediction performance. Even though the other candidates perform
better either in terms of model adequacy or prediction accuracy, our proposed model, especially
the mode with correlated bivariate RW process with level-correlated (BVRW(1)-LCM) is favored
by the majority of the data sets in both aspects. Next, we are going to use the BVRW(1)-LCM
model to study the microstructure of the count data with long memory dependence.
70

Metric BVAR(1)-LCM BVRW(1)-LCM AR(1)-LCM RW(1)-LCM Static LCM
|     | WAIC  | 9.5%  |     | 69.8% | 1.6% | 19.1% |     | 0.0% |
| --- | ----- | ----- | --- | ----- | ---- | ----- | --- | ---- |
|     | DIC   | 19.0% |     | 63.5% | 1.6% | 15.9% |     | 0.0% |
|     | MAE   | 4.8%  |     | 88.8% | 0.0% | 4.8%  |     | 1.6% |
|     | MSE   | 4.8%  |     | 90.4% | 0.0% | 3.2%  |     | 1.6% |
|     | WMAPE | 4.8%  |     | 88.8% | 0.0% | 4.8%  |     | 1.6% |
Table 12: Percentage of the 63 data sets favoring each model regarding in-sample model adequacy
| and | out-of-sample | prediction | accuracy |     |     |     |     |     |
| --- | ------------- | ---------- | -------- | --- | --- | --- | --- | --- |
3.4.2.4 An illustration of BVRW(1)-LCM framework From the previous result of the
model comparison, we will analyze the count data using the following model,
ind
|     |     | Y j,st |λ | j,st ∼ Pois(λ  | j,st ),            |                |                  |         |     |
| --- | --- | --------- | -------------- | ------------------ | -------------- | ---------------- | ------- | --- |
|     |     | η j,st =  | logλ j,st =    | β 0,j +β dur,j dur | j,st +β size,j | size j,st +γ j,t | +α j,st | ,   |
|     |     | γ j,t =   | ϕ j γ j,t−1 +ω | j,t ,              |                |                  |         |     |
|     |     |           |              |                    |                |                  |         |     |
ω
|     |     |       |  1,t  |             |     |     |     |        |
| --- | --- | ----- | ------- | ----------- | --- | --- | --- | ------ |
|     |     | ωωω = | ∼ N     | (000,ΣΣΣ ), |     |     |     |        |
|     |     | t     |       | ωωω         |     |     |     |        |
|     |     |       | ω       |             |     |     |     | (3.30) |
2,t
|     |     |    |     |    |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
σ2 σ σ
|     |     |    | ω1 ω1 | ω2, |     |     |     |     |
| --- | --- | --- | ----- | ---- | --- | --- | --- | --- |
ΣΣΣ ωωω =
|     |     |    |      |    |     |     |     |     |
| --- | --- | --- | ---- | --- | --- | --- | --- | --- |
|     |     | σ   | σ σ2 |     |     |     |     |     |
ω1 ω2 ω2
|     |     |     |   |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
α
|     |     |          |  1,st  |                   |     |     |     |     |
| --- | --- | -------- | -------- | ----------------- | --- | --- | --- | --- |
|     |     | ααα st = | ∼        | N (000,ΣΣΣ ααα ), |     |     |     |     |
|     |     |          |        |                   |     |     |     |     |
α
2,st
where dur is the averaged durations between the transactions associated with risk levels of
j,st
the j-th type for the s-th asset in the t-th time interval, and size is the averaged logarithmic
j,st
trading size (number of traded shares) in transactions associated with risk levels of the j-th type
for the s-th asset in the t-th time interval. We apply the priors in (3.22) for the hyperparameters
and weakly informative normal priors for the fixed effects. The statistical inference is summarized
in terms of fixed effects and hyperparameters. We’ve also investigated the conditional posterior
correlation between the count data by integrating the inference on the fixed effects and random
| effects. | Finally, | we provide | some remarks | for our model | application. |     |     |     |
| -------- | -------- | ---------- | ------------ | ------------- | ------------ | --- | --- | --- |
Fixed effects of averaged durations and logarithmic trading size Thefixedeffectsfrom
71

the averaged durations can provide some insights for the practitioners from four aspects in Figure
9. Firstly, We’ve found that averaged durations and different count data are negatively correlated
because their coefficients are estimated to be below zero. The overall negative association reflects
how the trading intensity influences the number of transactions. When the averaged durations are
observedtobeshort,itmeanstransactionsaremadefrequentlyinthemarket,causinglargercounts
of transactions at different risk levels. Secondly, the averaged durations have a stronger impact
on the high-risk counts across all sectors except for the Energy sector on Monday because the
magnitude of the estimated coefficients for the high-risk counts is larger than the one for the low-
riskcounts. Sincethelow-riskcountstendtobedrivenbytheliquidityfeatureofthecorresponding
asset, it is less impacted by the averaged durations. Therefore, the increased trading intensity will
provide more high-risk counts than low-risk counts, and practitioners can be aware of the short-
term proportion of transactions at both levels and evaluate the volatility of the market. Thirdly,
the Energy and Healthcare sectors with a larger magnitude of the fixed effect are more sensitive
to trading intensity than the Industrials sector with respect to the counts. The Healthcare sector
has more consistent sensitivity to the averaged durations because the estimated fixed effect has a
narrower range, while the counts from the other two sectors can react to the averaged durations
to different degrees throughout the month. Such differences in price fluctuation related to trading
intensityhelppractitionersdesigntheiroptiontradingstrategiesfordifferentsectorsbecauseoption
pricing depends heavily on how drastically the asset price fluctuates. Fourthly, in terms of the Day
of Week effect, the counts tend to be impacted more from Tuesday to Thursday with a larger
magnitude of the fixed effect from averaged duration, than Monday and Friday.
In addition to averaged durations, we will also describe and explain the impact of the averaged
log trading size on the counts with several aspects in Figure 10. To start with, a higher averaged
trading size is associated with a higher number of counts, since the fixed effects are significantly
larger than zero. The average trading size is the average number of traded shares per transaction
which is positively associated with the trading volume, which is the product of the number of
transactions and their corresponding trading size. Hence, such a relationship infers that the asset
with a higher trading volume tends to have a larger count of transactions. Secondly, we’ve also
noticed that the averaged trading size within a time interval has a greater impact on the low-risk
counts, which means orders put to trade more shares don’t necessarily correlate with the high-risk
72

counts as strongly as with the low-risk counts. It can be related to the behavior of the market
makers, quoting both a buy and sell price of the asset in the inventory, with the purpose of making
a profit on a tiny margin of bid-ask spread via a high trading volume. Nevertheless, the positive
impact of trading size on the high-risk counts still aligns with the common sense that the price
change tends to be affected to a certain degree by the trading volume. Thirdly, among the three
sectors, the counts in the Industrials sector are more sensitive to the trading volume and such
sensitivity is more consistent over the month than the other two sectors. Practitioners can expect
more volatile behavior in the Industrial sector than in the other two sectors. Lastly, there is no
clear pattern regarding the Day of Week effect but we’ve seen that the high-risk counts on Fridays
are impacted more by the trading volume on Fridays, especially in the Healthcare sector and the
Industrials sector.
Since the fixed effects are directly related to the conditional mean of count data, such influences
on the count data can be quantified by its coefficients. Holding other effects unchanged in the t-th
time interval for the s-th asset, the difference of the β and β provides the estimation of
dur,1 dur,2
ratiosofconditionalmeansofdifferenttypesofcountasexp(β dur −β dur ). Thefixed
dur,1 1,st dur,2 2,st
effect of the averaged log trading size can be applied in this manner as well. With a better under-
standing of the ratio between different counts within a given interval, practitioners may evaluate
their probability of making a profit regarding the dynamic volatility and customize their trading
strategy in different time intervals. As for the prediction on the count data with averaged dura-
tions and log trading sizes, one can either use lagged observations in the past with the stationarity
assumption or use non-negative time series models, such as log ACD models, to make predictions
on future observations in the upcoming time intervals.
Hyperparameters: latent correlation and variance Since the hyperparameters describe
the latent patterns of the random effect, they don’t contribute to the direct estimation of the
conditional mean of the count but they explain the uncertainty and association of the conditional
mean functions. The hyperparameters we are going to study are the correlation between the latent
temporaleffects,ρ ,andthecorrelationbetweenthelevelrandomeffects,ρ ,aswellastheprecision
ωωω ααα
parameters for the random effects.
According to our model results, the latent temporal effects are highly correlated in this month.
In Figure 11, the correlation coefficients present a strong relationship (ρˆ >.75) between the latent
ωωω
73

|     | Energy |     | Healthcare | Industrials |     |     |
| --- | ------ | --- | ---------- | ----------- | --- | --- |
−0.10
−0.15
Count type
rud
| −0.20 |     |     |     |     |     | High−risk |
| ----- | --- | --- | --- | --- | --- | --------- |
b
Low−risk
−0.25
−0.30
|     | M T W | R F | M T W R | F M T W | R F |     |
| --- | ----- | --- | ------- | ------- | --- | --- |
Day of week
| Figure | 9: The | association | between    | averaged durations | and | counts |
| ------ | ------ | ----------- | ---------- | ------------------ | --- | ------ |
|        | Energy |             | Healthcare | Industrials        |     |        |
0.8
0.6
Count type
ezis
| 0.4 |     |     |     |     |     | High−risk |
| --- | --- | --- | --- | --- | --- | --------- |
b
Low−risk
0.2
0.0
| M   | T W | R F M | T W R F | M T W | R F |     |
| --- | --- | ----- | ------- | ----- | --- | --- |
Day of week
Figure 10: The association between averaged log trading size and counts
temporal effects for counts with different types. In the Energy sector, the correlations could be
estimatedatover.9onsomedayssuchas01/04/2013(Day3). Ahighercorrelationρ indicatesthat
ωωω
the count data share some similarities regarding the market behavior. Therefore, the assumption
74

of uncorrelated latent temporal effects between count data can cause biased model inference and
introduce more uncertainty to model prediction at the significant existence of such correlation.
Energy Healthcare Industrials
1.00
0.75
0.50
0.25
0.00
0 5 10 15 20 0 5 10 15 20 0 5 10 15 20
Day
r
w
Figure 11: The estimated ρ with their 95% credible interval across all three sectors in January
ωωω
2013
The variances of the latent temporal effects have small estimated values in Figure 12. There are
twopossiblereasonsforthesmallvarianceestimation. First,duetothelongmemorypropertyofan
RW process, the cumulative variance of the marginal temporal effects throughout a trading day is
increasingly significant as Var(γ ) = t2σ2 is dependent on the time index t. A large estimation of
i,t ωi
thevarianceismorelikelytocauseaninconsistentspreadforthetruetimeseries. Thesecondreason
can be associated with the covariates included in the model. We have shown that the averaged
durationsandlogtradingsizehavesignificantfixedeffectsonthecountdataandalargeproportion
of data variability can be accounted for by the covariates, leaving less variation to be captured by
the latent temporal effects. Even though the covariates are treated as the attributes for a specific
type of count for a given asset in a time interval, the existent temporal dependence among the
covariates also contributes to the overall temporal pattern, especially for the averaged durations.
Between the two types of counts, the low-risk counts have more uncertain latent temporal effects
than the ones at high-risk levels. Holding the covariates and the level-correlated random effect
unchanged, the change in the ratios of the conditional mean of the counts at t-th interval can be
75

determined by exp(γ −γ ) with Var(γ −γ ) = t2(σ2 +σ2 −ρ σ σ ). Even with the
1,t 2,t 1,t 2,t ω1 ω2 ωωω ω1 ω2
small estimation of variance on the temporal effects across all three sectors, the market behaviors
for the Healthcare and Industrials are more stable than the Energy sector as the temporal effects
vary less on the high-risk counts than on the low-risk counts, which implies the big pharmaceutical
companies in the Healthcare sector and giant conglomerate corporations in the Industrials sector
are less volatile in a sense of the common environment in January 2013. On the other hand, the
Energy sector is considered more volatile regarding its market behavior, which could be related to
the oscillation in the crude oil price.
Energy Healthcare Industrials
0.0100
0.0075
0.0050
0.0025
M T W R F M T W R F M T W R F
Day of week
2
s
w
Count type
High−risk
Low−risk
Figure 12: The dot plot of estimated variances, σ2 and σ2 , of the latent temporal effects on
ω1 ω2
different days of a week across all three sectors in January 2013
The number of covariates plays an important role in capturing the association between the
response and explanatory variables. However, a small number of covariates are likely to explain a
limitedamountofdatavariationwhilealargenumberofcovariatestendtocauseanoverfittingissue.
Therefore, practitioners can select a moderate number of covariates of interest to be included in the
model, and incorporate level-correlated random effect for the correlated count data to supplement
the interpretation of the additional data variation that is not explained by the fixed effects. Such
random effects can be regarded to come from unobservable financial factors or covariates that
practitioners haven’t taken into account. In Figure 13, the correlations between latent level effects
76

remain at a high level throughout the entire month and such strong association helps account for
thecorrelationamongthetwodifferenttypesofcountsaswell. Thevarianceestimationforthelevel
effects is shown in Figure 14. Similar to the pattern for the temporal effect, the latent level effects
on the low-risk counts have a larger variance, leading to higher variability in the corresponding
counts. Even though the market behavior mentioned above describes the Industrials sector as
stabler than the Energy sector, a higher variance of the high-risk latent level effects indicates more
volatility in the Industrials sector than in the Energy sector, which means the unobservable factors
such as financial news and regulatory policies are idiosyncratic in different sectors. In Figure 15,
the variances in the raw counts are shown to be in a similar range in all three sectors, which means
that the variance comparison on the observational level does not provide distinctive guidance on
the customized investing strategy for different sectors. Using our framework, practitioners will
be able to uncover more latent patterns among different sectors even though the inference on the
observational level doesn’t differ significantly.
Energy Healthcare Industrials
1.00
0.75
0.50
0.25
0.00
0 5 10 15 20 0 5 10 15 20 0 5 10 15 20
Day
r
a
Figure 13: The estimated ρ with their 95% credible interval across all three sectors in January
ααα
2013
Correlation between observed counts Based on the inference of the fixed effects and
random effects, we are also able to find the conditional relationship between the two types of
counts. According to (3.11), the conditional posterior correlation between the two counts can be
77

|     | Energy |     | Healthcare | Industrials |     |
| --- | ------ | --- | ---------- | ----------- | --- |
0.2
Count type
2 a High−risk
s
Low−risk
0.1
|     | M T W | R F M | T W R F | M T W | R F |
| --- | ----- | ----- | ------- | ----- | --- |
Day of week
Figure 14: The dot plot of estimated variances of the latent level effects on different days of week
| across all three | sectors in January | 2013 |            |             |     |
| ---------------- | ------------------ | ---- | ---------- | ----------- | --- |
|                  | Energy             |      | Healthcare | Industrials |     |
12000
9000
stnuoc fo ecnairaV
Count type
High−risk
6000
Low−risk
3000
|     | M T W | R F M | T W R F | M T W | R F |
| --- | ----- | ----- | ------- | ----- | --- |
Day of week
Figure 15: The variances of the observed counts on different days of week across all three sectors
| in January 2013 |     |     |     |     |     |
| --------------- | --- | --- | --- | --- | --- |
calculated given the conditional posterior marginal mean and variance of each type of count. The
derivation of the correlation between the two count variables can be found in the Appendix section.
78

Itisnotappropriatetobuildalinearregressionmodelbetweentwocountvariables, especiallywhen
the observed counts are not large enough. However, it is not uncommon to observe a large number
of transactions within a short time interval thus leading to a large number of counts at different
risk levels, and the Poisson distributions with a large mean can be still approximated by normal
distributions. If we use simple linear regression to describe the relationship between Y (counts
H,st
with non-zero log returns) and Y ((counts with zero log returns)), we can build a linear model
L,st
| on the | raw counts,     |        |               |          |       |     |            |            |     |        |
| ------ | --------------- | ------ | ------------- | -------- | ----- | --- | ---------- | ---------- | --- | ------ |
|        |                 |        |               | Yˆ       | =ˆb   | +ˆb |            |            |     |        |
|        |                 |        |               | H,st     |       | 0,s | 1,s Y L,st | .          |     | (3.31) |
| For    | each individual | asset, | the R-squared |          | value | can | be         | calculated | as, |        |
|        |                 |        |              |          |       |     |            |            | 2  |        |
|        |                 |        |               | (cid:80) | −Y¯   |     |            | −Y¯        |     |        |
|        |                 |        |               | (Y       | H,st  | H,s | )(Y L,st   | L,s        | )   |        |
|        |                 | R 2    | = (cid:113)  |          |       |     |            |            |  , | (3.32) |
s
|     |     |     | (cid:80) |         | −Y¯ | )2)( | (cid:80) | −Y¯  | )2) |     |
| --- | --- | --- | -------- | ------- | --- | ---- | -------- | ---- | --- | --- |
|     |     |     | (        | (Y H,st |     | H,s  | (Y       | L,st | L,s |     |
where Y¯ and Y¯ are the sample mean of the counts for asset s. In a simple linear regression
|     | H,s L,s |     |     |     |     |     |     |     |     |     |
| --- | ------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
model, the R-squared value stands for the proportion of the variation in the response variable
explained by the regressor, and it is equivalent to the squared correlation coefficient. A high
| R-squared | value is | associated | with | a higher | correlation |     | coefficient. |     |     |     |
| --------- | -------- | ---------- | ---- | -------- | ----------- | --- | ------------ | --- | --- | --- |
Basedontheinferenceofthefixedeffectsandrandomeffects,wearealsoabletofindthemodel-
based conditional relationship. In Figure 16, the conditional correlation between counts derived
by the latent effects varies throughout a trading day compared with the unconditional correlation
between the counts. The unconditional correlations are directly computed based on the count
data on the observational level as empirical correlations, and they are universally higher than the
conditional posterior correlation computed from our model (BVRW(1)-LCM) in the Energy sector.
Thesolidlinesandcurvesstandfortheaggregatedmeanoftheestimatedunconditional/conditional
correlation over one month while the bands stand for a margin with ±2 standard errors for the
estimatedcorrelations. SimilarpatternsarealsodisplayedintheHealthcareandIndustrialssectors,
| see Figures | 31 and | 32 in the | Appendix | section. |     |     |     |     |     |     |
| ----------- | ------ | --------- | -------- | -------- | --- | --- | --- | --- | --- | --- |
We can also compare the RMSE between the SLR prediction (3.31) and BVRW(1)-LCM-based
| conditional | regression, |     |     |      |     |      |        |     |     |        |
| ----------- | ----------- | --- | --- | ---- | --- | ---- | ------ | --- | --- | ------ |
|             |             |     |     | Y∗   | b∗  | +b∗  |        |     |     |        |
|             |             |     |     |      | =   |      | Y L,st | ,   |     | (3.33) |
|             |             |     |     | H,st |     | 0,st | 1,st   |     |     |        |
79

Energy
|     |     | APC | COP | CVX |     |
| --- | --- | --- | --- | --- | --- |
1.00
0.75
0.50
0.25
0.00
|     |     | DVN | HAL | OXY |     |
| --- | --- | --- | --- | --- | --- |
noitalerroC 1.00
TYPE
0.75
|     | 0.50 |     |     |     | Model−based |
| --- | ---- | --- | --- | --- | ----------- |
|     | 0.25 |     |     |     | Empirical   |
0.00
|     |     |     |     | 0 50 100 150 | 200 |
| --- | --- | --- | --- | ------------ | --- |
|     |     | SLB | XOM |              |     |
1.00
0.75
0.50
0.25
0.00
|     | 0   | 50 100 150 2000 | 50 100 150 200 |     |     |
| --- | --- | --------------- | -------------- | --- | --- |
Time interval
Figure16: Thetraceplotofdailyaggregatedmodel-basedandempiricalcorrelationsintheHealth-
| care sector | throughout | January 2023     |     |             |     |
| ----------- | ---------- | ---------------- | --- | ----------- | --- |
| where b∗    | and b∗     | are approximated | by, |             |     |
|             | 1,st 0,st  |                  |     |             |     |
|             |            |                  |     | sd(Y |Data) |     |
H,st
|     |     | b∗ = Corr(Y | ,Y |Data) |             | ,   |
| --- | --- | ----------- | --------- | ----------- | --- |
|     |     | 1,st        | H,st L,st | sd(Y |Data) |     |
L,st
(3.34)
|     |     | b∗ = E(Y | |Data)−b∗ | ·E(Y |Data). |     |
| --- | --- | -------- | --------- | ------------ | --- |
|     |     | 0,st     | H,st      | 1,st L,st    |     |
In the Energy sector shown in Figure 17, the RMSE based on the approximated conditional regres-
sion based on BVRW(1)-LCM is significantly lower than the RMSE of the SLR model. Therefore,
imposing a constant correlation between the count data can be a strong assumption for real appli-
cations. BVRW(1)-LCM-based regression also has a better performance in the other two sectors,
| see Figures | 33 and | 34 in the Appendix | section. |     |     |
| ----------- | ------ | ------------------ | -------- | --- | --- |
Across all sectors, the two types of counts have a stronger correlation at the opening and clos-
ing hours on a trading day and are less correlated in the middle of the day. Some assets such
as APC, DVN in the Energy sector, MDT, BAX, and BIIB in the Healthcare sector, and FDX,
UNP, and RTN in the industrials sector, their middle-day correlation estimation remains stable
throughout the month because the standard errors are smaller compared with other time points
and other assets. Such correlation estimation with reduced uncertainty can be useful for the prac-
80

APC COP CVX
50
40
30
20
10
DVN HAL OXY
50
40
30
20
10
BVRW(1)−LCM SLR
SLB XOM
50
40
30
20
10
BVRW(1)−LCM SLR BVRW(1)−LCM SLR
MODEL
ESMR
Energy
Figure 17: Box plots for the square root of MSE comparison in the Energy sector between
BVRW(1)-LCM and Simple Linear Regression in January 2023
titioners to specifically adjust their investment scheme for these stocks in these time intervals. For
example, when the correlation between these two counts is estimated to be high, the ratio of the
estimated counts will be more reliable for the corresponding time interval thus the practitioners
can evaluate whether or not the underlying asset price is actively fluctuating instead of staying
steady with a large proportion of zero log returns. As a measurement for the association between
count data, correlation describes the linear relationship between two variables and has a satisfac-
tory performance when the count data are large but it is sensitive to outliers or non-linearity and
has a poor performance when the counts are small or even close to zero. The unconditional corre-
lations obtained from the raw count are also overestimated and unrealistic for practice. Therefore,
we’ve also investigated Spearman’s rank correlation between the two types of counts to measure
the monotonic association between the count data. In Figure 18, the empirical Spearman’s rank
correlations on the observational level are aggregated means based on different stocks within the
same sector. Although it indicates that the two types of counts have a fairly strong monotone rela-
tionship (correlation around .75), practitioners won’t be able to make additional inferences barely
with Spearman’s rank correlation. Nonetheless, the estimated latent level correlation ρ from the
ααα
BVRW(1)-LCM model can account for the correlation on the observational level as a hidden factor.
81

Energy Healthcare Industrials
1.00
0.75
0.50
0.25
0.00
0 5 10 15 20 0 5 10 15 20 0 5 10 15 20
Day
r
Correlation type
Spearman's r
BVRW(1)−LCM r a
Figure 18: The comparison between Spearman’s rank correlation and the latent level correlation
across three sectors.
AlthoughitismeaninglesstocomparethemagnitudebetweenSpearman’srankcorrelationandthe
latent level correlation as two different correlation measurements, their trajectories are observed
to share some similarity and it will be more convincing to use the BVRW(1)-LCM model to make
inference and prediction when the pattern of correlation between the counts is preserved.
Remarks Since liquidity reflects the ability of an asset to be traded frequently without a
significant price change, the counts of transactions at a low-risk level (the magnitude of log return
less than τ) can describe this property in a short-term manner. While volatility delineates how
drastically the price of an asset fluctuates given a time interval, the counts of transactions at a
high-risk level (the magnitude of log return greater than τ) displays the frequencies of trades with
extremepricechangesforwhichsuchextremityispre-definedbythepractitioners. Inourstudy, we
canobservepositivecorrelationsbetweenthesetwotypesofcountsasallconditionalcorrelationsare
greater than zero with τ = 0, which implies a positive association between liquidity and volatility
in such a setting. However, the choice of τ = 0 is just for the illustration of our model framework,
and the definitions for the different types of counts can be customized by practitioners with their
interests. The number of types depends on the number of thresholds and each individual asset can
also be assigned separate thresholds as well because the price change patterns of different assets
82

can differ a lot from each other and a common threshold applied to define the counts can cause
data imbalance issues with excessive zeros for some assets so that the unified conditional Poisson
model framework needs to be adapted by some potential zero-inflated models. In practice, the
prediction of the count data at different risk levels is not directly related to a profit-making trading
algorithmas themodelfocusesmoreon thevariability oftheprice fluctuationinadiscrete manner,
but the instant ratio between different counts within a short term provides statistical evidence on
the volatility of the market. For investors in the HFT market, such information facilitates their
decision on the strategies of trade and hold within a short period. A detailed trading algorithm
can be a combination of other price-movement prediction models and our framework, but this is
beyond the scope of this dissertation.
3.5 Summary
In this chapter, We proposed a Bayesian Poisson lognormal hierarchical model for multivariate
counttimeseriesinthepaper. Theincorporationoflatenttemporaleffectsandlevelrandomeffects
helps to account for different sources of variation as well as the correlation among the counts. The
model inference is achieved by the approximated Bayesian inference approach, INLA, of which the
performances of model parameter recovery and computation cost are shown to be competitive with
the traditional MCMC method in the simulation study. Although our model framework targets
bivariate count data in this paper, it is feasible to extend our framework to count data with a
higher dimension by correctly specifying the precision matrix of high dimensional latent temporal
effects. Since such precision matrices are usually sparse, their inverse computation can enjoy an
efficient algorithm via sparse representation. Due to its computational efficiency, the scalability of
the model inference can also be achieved through parallel computing, which can save much more
computational time than a fully Bayesian approach. In real applications, we use our framework
to account for the microstructure of the HFT data, including the interpretation of the covariates,
hyperparameters of latent effects, and conditional correlation between count data with the latent
inference, which are not straightforward based on the counts on the observational level. Finally,
We also provide our opinions on the potential usage of the framework in the real financial market.
83

4 Sequential Bayesian spatio-temporal outbreak detection
The first two topics discussed in Chapters 2 and 3 are related to statistical research problems from
the high-frequency financial market. Online structural break detection via a CUSUM-like quasi-
score detector statistic in financial durations helps monitor the trading intensity in the market
and multivariate count time series modeling establishes a connection between observed counts via
latent interdependent random effect. Motivated by relevant techniques from uni-variate online
change point detection and efficient multivariate count data modeling, we are going to extend
the online change point detection framework to the multivariate level. For Chapter 4, we aim at
developing online outbreak detection framework for public health surveillance data with spatio-
temporal interdependence.
4.1 Background
Public health plays an important role in protecting and improving the health of individuals and
communities. One of the public health functions is disease prevention and control. Through vac-
cination programs, disease surveillance, and infection control measures, public health efforts can
help control and prevent the spread of infectious diseases, such as the flu and COVID-19. Public
health authorities use surveillance systems to monitor and track the occurrence of diseases, health
conditions, and other health-related events in a population. Surveillance systems provide statis-
tical insights into the trends, patterns, and risk factors for disease, as well as the evaluation of
the effectiveness of public health interventions. For infectious diseases, early outbreak detection
allows public health officials to take timely action to prevent the spread of the disease. A practical
implementation of surveillance is the disease dashboard such as the one for COVID-19. Provid-
ing real-time tracking of the pandemic, such dashboards inform early warning of outbreaks with
improved transparency and communication. Despite the concern about data quality and accuracy
due to data collection or reporting processes, dashboards still give people access to a wealth of
data. As long as practitioners handle such surveillance data with careful interpretation and bias
adjustment, a dashboard can be a valuable resource, to facilitate public health decision-making on
a disease outbreak from one of the various aspects. Tsui et al. (2008) gave a comprehensive review
of different types of surveillance systems and Li et al. (2022a) summarized modern challenges and
84

opportunities in public health data surveillance and forecasting. The motivation of this chapter is
to deliver an accurate early outbreak detection framework to monitor the occurrence of infectious
disease outbreaks based on the multivariate discrete dashboard data for an ongoing pandemic and
contribute to the collaboration with researchers in many different fields including epidemiology,
computer science, and public health.
4.2 Literature review
4.2.1 Change point detection in public health surveillance system
The early outbreak detection problem in surveillance systems can be regarded as the research topic
ofonlinechangepointdetection,alsoknownassequentialorquickestchangepointdetectionbecause
an outbreak of an infectious data can be represented as a data pattern change, such as the changes
of trend, mean level, and variation. The main goal of online change point detection is to detect
the change from sequential data in real-time as soon as possible. Online change point detection
procedure deals with sequential data or streaming data and detects any change point shortly after
its occurrence and stops at the detection while the offline procedure has access to the full data and
aimsatidentifyingandlocalizingthechangesindatasequenceinaretrospectivemanner. Although
online change detection procedure is better aligned with the need for early outbreak detection in
surveillance systems, statistical methodologies from both research lines provide an abundance of
inspiration for our paper.
All the methods are usually designed based on the average detection delay, probability of false
alarm, false alarm rate, and etc. Existing sequential change point detection methods can be di-
vided into two categories, such as Bayesian in which the distribution of the change-point time
is known and non-Bayesian (minimax) methods in which the change-point time is non-random
and unknown. Johnson et al. (2017) provided a review of optimal change-point detection theory
in both Bayesian and non-Bayesian settings recently. Regression methods of outbreak detection
have been widely used, both for detecting outbreaks in surveillance systems based on laboratory
reports and notified infections, and for syndromic surveillance. Farrington et al. (1996) described
the detection of outbreaks to boost other more intensive surveillance methods by routinely scanned
data using linear regression model but its weakness was insensitivity when the baseline values on
85

which the threshold calculation is based coincide with past outbreaks. Some methodological is-
sues involved in outbreak detection using examples from different statistical techniques which are
focused on infectious diseases such as monitoring birth defects were described by Farrington and
Andrews (2003) while Diggle et al. (2009) illustrated how spatial statistical methods can be used
on developing online surveillance systems for common diseases by the nature of the data. A sys-
tematic and comprehensive review of the advancement of aberration detection algorithms used in
public health surveillance for the last decade was given by Yuan et al. (2019). Beside the classi-
cal stochastic process control methods and regression-based methods, modern surveillance system
evolves to adopt more sophisticated monitoring regimens via such as Bayesian hierarchical models
and machine learning frameworks as solutions to handle the increased complexity and volume of
surveillance data. Another important line of related research, offline detection, handles the change
point detection as well, but in a completely different fashion. What differentiates the online and
offline change point detection problems most is type of data availability, sequential update versus
complete retrospection.
4.2.2 Traditional outbreak detection methods
Traditionaloutbreakdetectionmethodsincludestochasticprocesscontrol(SPC)-relatedapproaches
and regression-based models. Early statistical applications in public health surveillance systems
werebasedontheanalysisofthereporteddatafromcliniciansorlaboratories. Therefore,statistical
methods stemming from stochastic process control in industrial manufacturing gained their popu-
larity. Traditional control charts are common tools for change point detection problems. Shewhart
control chart (Shewhart, 1929) as one of the earliest change point detection tools, uses previous
data to calculate a threshold based upon normality assumption (Montgomery, 2020). Due to its
easy-to-compute-and-interpret feature, Early Aberration Reporting System (EARS) software in
Centers for Disease Control (CDC) of the United States employed Shewhart control chart as one
of the surveillance tools to conduct near real-time monitoring. Instead of possessing congruence
and stationarity as the production data from a stable manufacturing process, surveillance data
can exhibit strong time trends, cyclic patterns, and other time-dependent effects, depending on the
dataaggregation, populationbehaviorsaswellasotherenvironmentalfactors. Totakeintoaccount
these factors for valid applications, Shewhart control chart was adjusted to accommodate the mean
86

and standard deviation with a short sliding window of historical data, such as C and W algorithms,
which capture the recent data pattern by consecutive days. However, Shewhart control chart and
its extensions can have compromised performance because of inappropriate data preprocessing and
violation of methodological assumptions. For example, the normality assumption is a strong one
for surveillance time series especially the observations are small count data. Although Shore (2000)
implemented an inverse normal transformation approach to handle non-Gaussian data, such ap-
proach may suffer from different application where larger data sets are required for a more accurate
estimation for higher-order moment.
As another well-adopted SPC method for detecting change-points, CUSUM chart introduced
by Page (1954) is able to detect small shift from mean for industrial quality control data more
quickly than Shewhart chart. The idea of using cumulative information for detection is further
extended or modified to solve various research problems. When dealing with discrete surveillance
data, such as count data of health events, Rossi et al. (1999) proposed a approximation CUSUM
procedure for a Poisson process for practicality and convenience, of which the main idea is to
transform a Poisson variate through standardization and get an approximated Gaussian variate.
When surveillance data are in the form of correlated count data, He et al. (2014) discussed the
implementationofMultivariatePoissonCUSUMchart, andprovidedthecontrolchartdesignbased
on log-likelihood ratios with in-control parameters for baseline and design parameters for the shift.
As the common limitation, the SPC and SPC-related methods are more related to industry quality
control, where a in-control process can be defined in full detail and usually don’t need additional
covariate information to enhance accountability. The stationary assumption of public health data
may not be valid, and integration of various data sources facilitates a better understanding of the
baseline process and a better performance of early outbreak detection. Nevertheless, SPC methods
can be synthesized into regression-based methods to monitor the pattern of model residuals, scores,
or quasi-scores (Berkes et al., 2004).
Regression-based methods enable the incorporation of external covariates and explain temporal
dependence from past observations. Generalized linear models (GLMs) with distribution-specific
links to the mean function grant the versatility to handle a variety of surveillance data. Apart
from the well-known linear regression with independent Gaussian residuals for continuous data,
count data can also be modeled by GLM with corresponding link functions to various discrete
87

distributions such as Poisson, negative binomial as well as their zero-inflated variants etc. The
incorporation of additional factors of interest into GLMs enhances model forecast performance as
well as interpretability. Temporal dynamics such as day of week effect or seasonality are usually
elucidated via a dummy variable specifying different kinds of days or trigonometric term resem-
bling the sinusoidal data pattern (Serfling, 1963). Farrington et al. (1996) developed a regression
algorithm to assist outbreak detection by using the threshold predicted from the modeled baseline.
Adaptive GLM frameworks with a short sliding window of historical data address the limitations
of assuming static model parameters via sequential updating parameter estimates according to a
| sliding baseline | pattern | (Burkom | et al., | 2007; | Xing et | al., 2011). |     |     |
| ---------------- | ------- | ------- | ------- | ----- | ------- | ----------- | --- | --- |
Auto-regressive integrated moving average (ARIMA) models (Box et al., 2015) and integer-
valuedauto-regressive(INAR)models(AlzaidandAl-Osh,1988), asspecialregression-basedmeth-
ods, account for the time dependence through a combination of past observations. For continuous-
valued time series, the time-dependence is illustrated by a ARIMA(p,d,q) model,
|     |     | (cid:32) | (cid:33) |          |     |        |          |     |
| --- | --- | -------- | -------- | -------- | --- | ------- | --------- | --- |
|     |     |          | p        |          |     |         | q         |     |
|     |     | (cid:88) |          |          |     |         | (cid:88)  |     |
|     |     | 1−       | ϕ Bi     | (1−B)d(Y | −µ  | ) = 1+ | θ Bi ϵ , |     |
|     |     |          | i        |          | t Y |         | j t       |     |
|     |     | i=1      |          |          |     |         | j=1       |     |
ϵ ∼ N(0,σ2),
|     |     |     |     | t   | ϵ   |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
whereY andµ aretheobservationattimetanditsexpectation,andϕ ,θ ,andσ2 arerespectively
| t   | Y   |     |     |     |     |     | i i | ϵ   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
the auto-regressive (AR) coefficients, moving average (MA) coefficients, and the variance of the
white noise ϵ . B is a backshift operator, i.e., BiY = Y . p and q denotes the AR and MA orders,
|     | t   |     |     |     | t   | t−i |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
indicating the number of lagged historical observations included in the model, while d is the order
of differencing to stabilize non-stationary time series. For integer-valued time series, the temporal
associationbetweencountscanbemodeledviaINAR(p)modelwithabinomialthinningtechnique,
p
(cid:88)
|     |     |     |     | Y = | α ◦Y  | +ϵ , |     |     |
| --- | --- | --- | --- | --- | ----- | ---- | --- | --- |
|     |     |     |     | t   | i t−i | t    |     |     |
i=1
where the binomial thinning operator α ◦ Y = (cid:80)Yt−iB ,B i. ∼ i.d Bernoulli(α ). ϵ is an in-
|     |     |     |     | i   | t−i | k   | k   | i t |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
k=1
dependent non-negative integer-valued random error. Besides the flexibility of using seasonally
lagged observations and exogenous variable to explain the seasonality and external impact, the
88

auto-regressive framework alleviates the reliance on independent assumption and appreciates the
accountability pertaining to the unobserved and latent factors contained in historical data. In
addition, smoothing methods orginated from the moving average (MA) methods with exponential
weights such as Exponential Weighted Moving Average (EWMA) and Holt-Winters method (Win-
ters, 1960). Such smoothing methods are commonly as part of data preprocessing to smooth out
seasonal effect and trend by applying other methods.
However, the aforementioned methods have different limitations. For example, SPC-related
methods rely on normality and stationary assumptions for their valid implementation. When
surveillance data are discrete, a common choice of model fitting is still the standard Poisson model,
even though it has been suggested in numerous literature that the data overdispersion issue can be
remedied by imposing a gamma prior on the Poisson mean or using a negative binomial model.
4.2.3 Modern outbreak detection methods
Over the last decade, statistical surveillance algorithms for online outbreak detection have a sub-
stantial evolution with the complexity of surveillance data and the advancement of computational
technology. To expedite early outbreak detection, public health authorities have already begun
to take advantage of pre-diagnostic or syndromic data such as patient counts with disease-related
symptoms recorded by hospitals or healthcare-related search information via electronic online plat-
forms. The expanding volume and variety of such data sources place both more valuable pre-
pandemicinformationandmorechallengingproblemsforefficientstatisticalmodelsthantraditional
laboratory diagnostics. Therefore, a burgeoning research line of Bayesian models in public health
surveillance offers several advantages over traditional methods including historical information bor-
rowing, domain knowledge a priori incorporation, computational solution to complex hierarchical
models, and natural interpretations of posterior probability for outbreak detection.
Bayesian Hidden Markov Models (HMM) enable practitioners to classify the surveillance data
into a non-epidemic phase and an epidemic phase via a binary latent state variable Z (Mart´ınez-
Beneito et al., 2008; Watkins et al., 2009; Conesa et al., 2015) and a suspiciously anomalous obser-
vation with a large value of Pr(Z = 1) can trigger further investigation before finalizing a public
outbreak announcement. Since it is common to observe spatio-temporal patterns in surveillance
areal-type data, a common approach to introduce temporal dependence in the model is via an
89

ARMA association among latent temporal effects. Meanwhile, to account for the spatial correla-
tion, data from neighboring locations are assumed to behave similarly. Such spatial patterns can
be explained through the incorporation of latent spatial effects from different locations. It would
become natural for practitioners to account for the spatial association of the areal unit data. Con-
ditional auto-regressive model (Besag, 1974) is a prevalent choice as a prior distribution for random
spatial effect. Besag et al. (1991), Gelfand and Vounatsou (2003) and Jin et al. (2005) have addi-
tionaldiscussionsontheextensionofCARmodel, includingthediscussionofthespecialcaseofthe
CAR model, Instrinc Auto-regressive (IAR) model with an extra constraint on the random effects,
efficient computation for the determinant of the precision matrix, as well as the multivariate CAR
model which is though more computationally demanding.
Uni-variate HMMs can be extended their multivariate version by incorporating spatio-temporal
random effects (Heaton et al., 2012; Zou et al., 2012, 2014) and iterative update formula of
Pr(Z = 1) was also provided to circumvent parameter re-estimation when new observations arrive.
Dimension reduction also needs to be considered when the number of spatial locations is large
and there are many areas with small counts. Zou et al. (2018) addressed this issue via a semi-
parametric Dirichlet process for clustering similar regions and applied the particle filter approach
to make inferences on latent variables. A real-time Bayesian spatio-temporal syndromic surveil-
lance framework was also applied to small companion animals as an auxiliary source for public
health surveillance (Hale et al., 2019). Other Bayesian approaches such as Bayesian scan statistics
(Neill, 2011), Bayesian networks (Cooper et al., 2015) and Bayesian disease mapping (Anderson
et al., 2017) are also prevalent choices in public health surveillance systems to handle such as point-
reference spatial data Banerjee et al. (2003), individual-level medical records, etc. Point-referenced
data are also known as geostatistical data containing precise location information for individual
data points, and the public health surveillance systems may usually aggregate the individual data
points over a set of disjoint areas due to privacy concerns.
One important concern regarding the Bayesian frameworks is their computational cost. Most
of public health surveillance literature using Bayesian frameworks adopted MCMC method as the
computational tool, which can be significantly time-consuming if data dimension increases or the
complex model structure is poorly specified. Although Rue et al. (2009) proposed Integrated
Nested Laplace Approximation as an efficient computational tool, there is limited literature to our
90

knowledge that employed INLA implementation in public health surveillance (Manitz and H¨ohle,
2013; Salmon et al., 2015).
With the enhancement of computational power, machine learn methods in disease monitoring
provides another solution to address the complex dynamics involving both social and biological
systems. During the pandemic of COVID-19, it becomes more challenging and numerous early
outbreak detection applications are delivered in this research area. Deep Learning-based models
were also used. Saqib (2021) proposed a hybrid machine learning model that is not only pre-
dicted with good accuracy but also takes care of uncertainty of predictions using Bayesian Ridge
Regression. Radev et al. (2021) presented a simulation-based Bayesian inference framework for
complex epidemiological models using neural network which utilized short time-series samples to
obtain early warning signals while Li et al. (2022b) introduced a model-based method. Most of
these methods have limitations due to the number of data availability. According to Coughlin
et al. (2021),they identified possible change or turning points as indicated by the dynamics of daily
COVID-19incidenceswhichtheidentifiedchangepointswerecombinedwiththespline-fittedtrend
which interprets the behavior of the change points; it may have provided better prediction dates
for the implementation of public restrictive interventions in each country but not appropriate for
all nations. Even Guan et al. (2021) added prediction method using mobility data which helps to
determine when and where outbreaks will occur, it has several limitations such as smoothing, miss-
ing data, and based on information about only known cases but not undetected cases. However,
the practical limitations facing machine learning methods include the vast amount of training data,
risk of over-fitting, and accurate labels for outbreaks in the training data.
4.3 BOSTON-PUPA procedure
To address complex and dynamic spatio-temporal patterns of streaming surveillance data, we pro-
pose a consolidated Bayesian Online Spatio-Temporal Outbreak detecitoN framework with Prior
Updating and P-value Adaptation (BOSTON-PUPA) techniques to effectively achieve both global
and local sequential monitoring over a cluster of regions at risk. The streaming data of confirmed
case counts take a spatio-temporal format as they are reported from various locations on a daily
basis. As an iterative process with a fixed-size sliding window, the BOSTON-PUPA framework
accounts for the spatio-temporal association and overdispersion of the count data via a Bayesian
91

hierarchical generalized Poisson distribution (GPD) model with Integrated Nested Laplace Ap-
proximation (INLA) method. The Prior Updating technique leverages past information and the
current sliding window sequentially for integrated inference with a reduction of computational bur-
dens. The P-value Adaptation technique enhances the significance of a true outbreak to address
potential imbalance issues for spatial data, especially for the regions with small counts. The incor-
poration of eclectic techniques results in decent false detection control while preserving a robustly
high detection power and efficiency against different signal-to-noise ratios.
Our proposed Bayesian Online Spatio-Temporal Outbreak detectioN with Prior Updating and
P-value Adaptation (BOSTON-PUPA) framework is an iterative procedure with a sliding window
for the training data modeling with window length T + 1. The streaming data are monitored
consecutively with a one-day-ahead sliding pace and only the observed counts on the last day in
the sliding window will be involved in the outbreak detection procedure. With the initial sliding
window containing observed data from day 1 and day T+1, the outbreak detection procedure aims
(s) (s)
at testing the null and the alternative hypotheses H versus H ,k = 1,2,..., as below,
0,k a,k

   H (s) : No significant outbreak has occurred yet in the s-th location by the (T +k)-th day.
0,k
   H (s) : An outbreak has occurred significantly in the s-th location by the (T +k)-th day.
a,k
(4.1)
Theiterativeoutbreakdetectionprocedureinvolvesfoursteps: 1)Bayesianmodelinferenceand
in-sample prediction. 2) Latent aberration assessment. 3) P-value adaptation. 4) Decision-making
and algorithm update. To elucidate the detection procedure, we elaborate on each step at the k-th
iteration for instance.
4.3.1 Step 1: Bayesian model inference and in-sample prediction
First, we will introduce the model framework for the surveillance data under the null hypothesis
of no outbreak at any location. Let {Y } denote the daily case count at day t at location s.
s,t
We propose the following conditional generalized Poisson distribution (GPD) framework for the
92

| multivariate | count | time series, |     |     |     |     |     |     |     |     |     |
| ------------ | ----- | ------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- |
ind
|     |     | Y   | |θ ,λ | ∼   | GPD(θ | ,λ),     |          |     |     |     |     |
| --- | --- | --- | ----- | --- | ----- | -------- | -------- | --- | --- | --- | --- |
|     |     | s,t | s,t   |     |       | s,t      |          |     |     |     |     |
|     |     |     |       |     |       | (cid:18) | (cid:19) |     |     |     |     |
θ
|     |     | η   | = logµ |     | = log | s,t | = P | +XXX βββ | +ϕ +ε | ,   |     |
| --- | --- | --- | ------ | --- | ----- | --- | --- | -------- | ----- | --- | --- |
|     |     | s,t |        | s,t |       |     | s   | sss      | s     | t   |     |
1−λ
|     |     |     |           |     |          |     |         |     |     |     |       |
| --- | --- | --- | --------- | ---- | -------- | --- | -------- | --- | --- | --- | ----- |
|     |     |     |           |      |          | w   | σ 2      |     |     |     |       |
|     |     |     |           |      | (cid:88) | sj  | ϕ        |     |     |     | (4.2) |
|     |     | ϕ s | |ϕϕϕ −s ∼ | N ρ |          |     | ϕ j , , |     |     |     |       |
|     |     |     |           |      | ϕ        | w   | w        |     |     |     |       |
|     |     |     |           |      |          | s+  | s+       |     |     |     |       |
j̸=s
|     |     | ε   | = ρ ε | +ω  | ,ω  | ∼ N(0,σ2), |     |     |     |     |     |
| --- | --- | --- | ----- | --- | --- | ---------- | --- | --- | --- | --- | --- |
|     |     | t   | ε     | t−1 | t   | t          | ε   |     |     |     |     |
,σ2,σ2)
|     |     | ΘΘΘ | = (λ,βββ,ρ |     | ,ρ  | ∼   | π(ΘΘΘ). |     |     |     |     |
| --- | --- | --- | ---------- | --- | --- | --- | ------- | --- | --- | --- | --- |
|     |     |     |            | ϕ   | ε   | ϕ ε |         |     |     |     |     |
In (4.2), s = 1,2,...,S,t = 1,2,...,T, where S is the total number of locations and T is the
total number of days in the sliding window. P is the offset term for location s and it accounts
s
for differences in expected values or exposures at each location. In our study, we choose the
logarithmic population as the offset term. XXX is the covariate vector of interest for location s and
sss
βββ is the corresponding fixed effect vector. ϕϕϕ = (ϕ ,ϕ ,...,ϕ ) are the spatial effects and account
|     |     |     |     |     |     |     | 1 2 | s   |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
WWW
for the neighboring association among all the spatial units. = (w sj ) S×S is the adjacency matrix
| for these | locations, |     |     |     |     |     |     |     |     |     |     |
| --------- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |


|     |     |     |   | 1,if | location | s   | and location | j are | adjacent |     |     |
| --- | --- | --- | --- | ---- | -------- | --- | ------------ | ----- | -------- | --- | --- |
w =
sj

|     |     |     |    | 0,otherwise. |     |     |     |     |     |     |     |
| --- | --- | --- | --- | ------------ | --- | --- | --- | --- | --- | --- | --- |

ThediagonalelementsofWWW arezerosandw = (cid:80)S w . ε isthecommontemporallatenteffect,
|     |     |     |     |     |     | s+  | sj  | t   |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
j=1
describing the shared dynamics by the mean functions of the counts from different locations. We
assign the Conditional Autoregressive (CAR) prior and an AR(1) process prior to the spatial and
temporal latent effects correspondingly. ΘΘΘ contains all the parameters in the Bayesian hierarchical
framework. The prior distribution for ΘΘΘ is π(ΘΘΘ), which will be discussed shortly in detail.
Considering the potential dispersion of count data, We select a conditional GPD for the count
data. The point mass function of a conditional GPD (Consul and Jain, 1973) given as

|     |      |       |     |    | θs,t(θs,t | + λy)y−1 |          |     |         |             |       |
| --- | ---- | ----- | --- | --- | --------- | -------- | -------- | --- | ------- | ----------- | ----- |
|     |      |       |     |   |           |          | ·exp(−(θ |     | +λy)),y | = 0,1,2,... |       |
|     |      |       |     |     |           | y !      |          | s,t |         |             |       |
|     | Pr(Y | = y|θ | ,λ) | =   |           |          |          |     |         |             | (4.3) |
|     | s,t  |       | s,t |     |           |          |          |     |         |             |       |

|     |     |     |     |   | 0 for | y > | m,when | λ < 0 |     |     |     |
| --- | --- | --- | --- | --- | ----- | --- | ------ | ----- | --- | --- | --- |
93

with mean µ = θ /(1 − λ) and variance σ2 = µ · (1 − λ)−2, max(−1,−θ /m) < λ < 1
|     | s,t | s,t | s,t | s,t |     | s,t |
| --- | --- | --- | --- | --- | --- | --- |
and m(≥ 4) is the largest positive integer for which θ +mλ > 0 when λ is negative. Since our
s,t
framework focuses on the overdispersion pattern in the count data, the range of λ is restricted
within [0,1). When λ = 0, the GPD becomes a standard Poisson distribution. Such flexibility
can better accommodate the small counts, especially when θ is close to zero. When the mean
s,t
parameter θ approaches zero, the underlying distribution will face a degeneracy issue, with a
s,t
dominant probability on P(Y = 0|θ ,λ) ≈ 1. For the observed small counts at some locations,
|     |     | s,t s,t |     |     |     |     |
| --- | --- | ------- | --- | --- | --- | --- |
a detection procedure attributed to such a point mass distribution will deliver an extreme test
(s)
statistic under H even if the magnitude of the counts doesn’t qualify for an outbreak claim.
0,k
Compared with the standard Poisson distribution, a GPD with an overdispersion parameter will
be less likely to reach a false alarm of an outbreak because it can account for larger variations in
| the counts | than a standard | Poisson distribution |     | does. |     |     |
| ---------- | --------------- | -------------------- | --- | ----- | --- | --- |
In the INLA implementation of (4.2), all the parameters with restricted support will be inter-
nally transformed into the ones with support on R as described in Table 13. Such a reparame-
terization technique grants efficient computation of the internal parameters on their unrestricted
supports. Therefore, we assign the internal hyperparameters, ϑϑϑ = (ξ,βββ,ϑ ρ ,ϑ ρε ,ϑ 2 ,ϑ 2 ), in (4.2)
|     |     |     |     |     | ϕ   | σ σ ε |
| --- | --- | --- | --- | --- | --- | ----- |
ϕ
with Gaussian priors. The variances of the Gaussian priors quantify the uncertainty about the
internal parameters. In order not to cause further confusion in the rest of the paper, we use the
parameters/internal parameters to include the covariate coefficients and the hyperparameters.
|     |     | Hyperparameter | Support | Internal representation |          |     |
| --- | --- | -------------- | ------- | ----------------------- | -------- | --- |
|     |     |                |         | (cid:16)                | (cid:17) |     |
λ
|     |     | λ   | (0,1) | ξ = log |     |     |
| --- | --- | --- | ----- | ------- | --- | --- |
1−λ
(cid:16) (cid:17)
ρ
|     |     | ρ   | (0,1) | ϑ = log | ϕ   |     |
| --- | --- | --- | ----- | ------- | --- | --- |
|     |     | ϕ   |       | ρ ϕ     | 1−ρ |     |
(cid:16) ϕ(cid:17)
1+ρε
|     |     | ρ ε | (−1,1) | ϑ ρε = log |     |     |
| --- | --- | --- | ------ | ---------- | --- | --- |
1−ρε
|     |     | σ2  | (0,∞) | ϑ = log(σ2) |     |     |
| --- | --- | --- | ----- | ----------- | --- | --- |
|     |     | ϕ   |       | σ2          | ϕ   |     |
ϕ
|     |     | σ2  | (0,∞) | ϑ = log(σ2) |     |     |
| --- | --- | --- | ----- | ----------- | --- | --- |
|     |     | ε   |       | σ2          | ε   |     |
ε
Table 13: Hyperparameters with restricted support and their internal representation
In a sliding window of size T + 1 at the k-th iteration, (4.2) is fitted on the training data
94

|     |        | }T      |     |           |       |        |        |         |          | π(ϑϑϑ)|∂ϑϑϑ|, |     |
| --- | ------ | ------- | --- | --------- | ----- | ------ | ------ | ------- | -------- | ------------- | --- |
| DDD | = {YYY | , with  | YYY | = {Y      | ,Y    | ,...,Y | } with | a prior | π(ΘΘΘ) = |               |     |
| k   |        | k+t t=0 |     | k+t 1,k+t | 2,k+t | S,k+t  |        |         |          | ∂ΘΘΘ          |     |


|     |     |     |     |     |  π | (ϑϑϑ),1 ≤ | k ≤ T | +1  |     |     |     |
| --- | --- | --- | --- | --- | --- | --------- | ----- | --- | --- | --- | --- |
 G
|     |     |     |     | π(ϑϑϑ) = |     |     |     |     |     |     | (4.4) |
| --- | --- | --- | --- | -------- | --- | --- | --- | --- | --- | --- | ----- |

|     |     |     |     |     |  πa0(ϑϑϑ|DDD∗ |         | ),k | ≥ T +2 |     |     |     |
| --- | --- | --- | --- | --- | -------------- | ------- | --- | ------ | --- | --- | --- |
|     |     |     |     |     |               | G k−T−1 |     |        |     |     |     |
where π (ϑϑϑ) corresponds to a vague internal Gaussian prior with a large variance, used in the first
G
πa0(ϑϑϑ|DDD∗
(T + 1) iterations. After the (T + 1)-th iteration, π(ϑϑϑ) = ) becomes a historical-
|     |     |     |     |     |     |     |     | G   | k−T−1 |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ----- | --- | --- |
data-related Gaussian prior raised to a discounting factor a (0 < a ≤ 1), where DDD∗ is the
|     |     |     |     |     |     |     |     | 0   | 0   |     | k−T−1 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----- |
past cumulative information set up to the (k − T − 1)-th iteration and has no overlap with the
current training dataDDD . Since (4.2) doesn’t have a closed form for the posteriors of its parameters
k
or hyperparameters, we intend to only borrow the historical information via a Gaussian prior,
(ϑϑϑ|DDD∗
π G ), which shares the first two moments with the corresponding posterior as in (4.5) for
k−T−1
| the | purpose | of prior | updating | in our       | iterative | detection | procedure,  |       |      |     |     |
| --- | ------- | -------- | -------- | ------------ | --------- | --------- | ----------- | ----- | ---- | --- | --- |
|     |         |          | (cid:90) |              |           | (cid:90)  |             |       |      |     |     |
|     |         |          |          | ϑ∗π (ϑ∗|DDD∗ | )dϑ∗      | =         | ϑ∗π(ϑ∗|DDD∗ |       | )dϑ∗ |     |     |
|     |         |          |          | G k−T−1      |           |           |             | k−T−1 |      |     |     |
(4.5)
|     |     |     | (cid:90) |          |     | (cid:90) |                |     |       |     |     |
| --- | --- | --- | -------- | -------- | --- | -------- | -------------- | --- | ----- | --- | --- |
|     |     |     | (ϑ∗)2π   | (ϑ∗|DDD∗ |     | )dϑ∗     | (ϑ∗)2π(ϑ∗|DDD∗ |     | )dϑ∗, |     |     |
=
|     |     |     |     | G   | k−T−1 |     |     | k−T−1 |     |     |     |
| --- | --- | --- | --- | --- | ----- | --- | --- | ----- | --- | --- | --- |
where π (.) denotes a Gaussian density and π(ϑ∗|DDD∗ ) corresponds to the actual posterior
|     | G   |     |     |     |        |     | k−T−1 |     |     |     |     |
| --- | --- | --- | --- | --- | ------ | --- | ----- | --- | --- | --- | --- |
|     |     |     |     | ϑ∗  | inϑϑϑ. |     |       |     |     |     |     |
density for the internal parameter After the k-th iteration of model fitting, three pieces of
(ξˆ
information will be tracked,ηηηˆˆˆ , ,σˆ2 ), and the posterior distributions for internal parameters.
|     |     |     |     | T+k | k ξ |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
k
ηηηˆˆˆ = (ηˆ ,ηˆ ,...,ηˆ ) denotes the transformed posterior mean vector of YYY |DDD in
| T+k |     | 1,T+k 2,T+k |     | S,T+k |     |     |     |     |     |     | T+k k |
| --- | --- | ----------- | --- | ----- | --- | --- | --- | --- | --- | --- | ----- |
|     | ξˆ  | σˆ2         |     |       |     |     |     |     |     |     |       |
(4.2). and are the internal posterior mean and variance for the overdispersion parameter
|     | k   | ξ k |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
in Table 13. An illustration of Step 1 is summarized from Table 14 in which the model inference
and in-sample prediction refer to the columns, “Mean”, “Overdispersion”, and “Posterior”. The
“Posterior” column in Table 14 refers to the posterior distribution for the internal parameterϑϑϑ and
π(ϑϑϑ|DDD∗ ) = π(ϑϑϑ|DDD ,DDD ,DDD ,...),whereDDD ∩DDD ∩DDD ∩··· = Ø.
|     | k−T−1 |     | k−T−1 | k−2T−2 | k−3T−3 |     |     | k−T−1 | k−2T−2 | k−3T−3 |     |
| --- | ----- | --- | ----- | ------ | ------ | --- | --- | ----- | ------ | ------ | --- |
95

Iteration (k) Training data Prior Mean Overdispersion Posterior
1 DDD π (ϑϑϑ) ηηηˆˆˆ (ξˆ,σˆ2 ) π(ϑϑϑ|DDD )
1 G T+1 1 ξ1 1
2 DDD π (ϑϑϑ) ηηηˆˆˆ (ξˆ,σˆ2 ) π(ϑϑϑ|DDD )
2 G T+2 2 ξ2 2
. . . . . .
. . . . . .
. . . . . .
T +1 DDD π (ϑϑϑ) ηηηˆˆˆ (ξˆ ,σˆ2 ) π(ϑϑϑ|DDD )
T+1 G 2T+1 T+1 ξT+1 T+1
T +2 DDD πa0(ϑϑϑ|DDD ) ηηηˆˆˆ (ξˆ ,σˆ2 ) π(ϑϑϑ|DDD ,DDD )
T+2 G 1 2T+2 T+2 ξT+2 T+2 1
. . . . . .
. . . . . .
. . . . . .
2T +2 DDD πa0(ϑϑϑ|DDD ) ηηηˆˆˆ (ξˆ ,σˆ2 ) π(ϑϑϑ|DDD ,DDD )
2T+2 G T+1 3T+2 2T+2 ξ2T+2 2T+2 T+1
2T +3 DDD πa0(ϑϑϑ|DDD ,DDD ) ηηηˆˆˆ (ξˆ ,σˆ2 ) π(ϑϑϑ|DDD ,DDD ,DDD )
2T+3 G T+2 1 3T+3 2T+3 ξ2T+3 2T+3 T+2 1
. . . . . .
. . . . . .
. . . . . .
Table 14: Iterative prior updating procedure with tracked mean and overdispersion
4.3.2 Step 2: Latent aberration assessment
Duringtheiterativeprocedurewithaslidingwindow, twotypesoflatentaberrationsaremonitored
simultaneously: global latent aberration and local latent aberration. Latent aberrations in the
detection procedure are assessed via binary indicators stemming from comparisons between Z-
score-based statistics and a user-specified threshold. The aberration indicators calculated in this
step facilitate the subsequent p-value adaptation process.
To indicate the latent aberration at the k-th iteration, two latent estimates are of interest: the
estimates of overdispersion parameter λˆ and location-wise GPD mean µˆ . The global latent
k s,T+k
aberration is associated with the overdispersion parameter λ in (4.2) because the spatio-temporal
data share the common overdispersion parameter and any extreme counts observed from either
location will contribute to a larger estimate for the overdispersion parameter, signaling a global
latent aberration that certain location(s) can be experiencing unusual case counts. To specify the
local latent aberrations, µˆ will be compared with its historical estimates, and a larger value
s,T+k
of µˆ tend to deviate from its historical pattern thus raising an alarm. Since binary aberration
s,T+k
indicators are Z-score-based, the corresponding internal representations, ξˆ and ηˆ , are used in
k s,T+k
the calculation due to their unrestricted supports.
Therearetwosortsofcollectionsinvolvedtokeeptrackofthosetwotypesofhistoricalestimates.
(cid:110) (cid:111)
Thecollectionoftheestimatesfortheoverdispersion,ΞΞΞ = (ξˆ,σˆ2 ),(ξˆ,σˆ2 ),...,(ξˆ ,σˆ2 ) ,refers
k 1 ξ1 2 ξ2 k ξ
k
tothe“Overdispersion”columninTable14,wheretheposteriorestimatesofmeanandvarianceare
96

gathered sequentially. Meanwhile, the collection of posterior mean estimates refers to the “Mean”
column in Table 14. HHH = {ηˆ ,ηˆ ,...,ηˆ } denotes the historical estimates set for the
|     |     | s,k |     | s,T+1 | s,T+2 |     | s,T+k |     |     |     |     |
| --- | --- | --- | --- | ----- | ----- | --- | ----- | --- | --- | --- | --- |
s-th location. When k = 1, ΞΞΞ k =HHH 1,k = ··· =HHH S,k = Ø. When k ≥ 3, the global and local latent
aberration indicators, δ and δ ,s = 1,2,...,S, are calculated respectively in (4.6),
|     |     | ξˆ  |     | ηˆ s,T+k |     |     |     |     |     |     |     |
| --- | --- | --- | --- | -------- | --- | --- | --- | --- | --- | --- | --- |
k
(cid:115)
|     |      | (cid:32) | ξˆ  | ¯ˆ  | (cid:33) |       |     | k−1      |     | (cid:80)k − 1σˆ 2 |       |
| --- | ---- | -------- | --- | --- | -------- | ----- | --- | -------- | --- | ----------------- | ----- |
|     |      |          | −ξ  |     | ¯ˆ       |       | 1   | (cid:88) |     |                   |       |
|     |      |          | k   | k−1 |          |       |     | ξˆ,σ¯ˆ   |     | i= 1 ξ i.         |       |
|     | δ ξˆ | = I      |     | >   | z ,ξ     | k−1 = |     | i        | ξ = |                   | (4.6) |
|     | k    |          | σ¯ˆ |     |          |       | k−1 |          | k−1 | k−1               |       |
ξ
|     |     |     | k−1 |     |     |     |     | i=1 |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
and (4.7),
|     |          |     | (cid:32) |       |         |     | (cid:33) |         |     |          |     |
| --- | -------- | --- | -------- | ----- | ------- | --- | -------- | ------- | --- | -------- | --- |
|     |          |     | ηˆ       | −η¯ˆ  |         |     |          |         |     | 1 k−1    |     |
|     |          |     |          | s,T+k | s,T+k−1 |     | ,η¯ˆ     |         |     | (cid:88) |     |
|     | δ        | =   | I        |       |         | >   | z        |         | =   | ηˆ ,     |     |
|     | ηˆ s,T+k |     |          | σ     |         |     |          | s,T+k−1 | k−1 | s,T+i    |     |
HHH
|     |     |     |     | s,k−1 |     |     |     |     |     | i=1 |     |
| --- | --- | --- | --- | ----- | --- | --- | --- | --- | --- | --- | --- |
(4.7)
(cid:115)
|     |     |     | (cid:80)k−1(ηˆ |       | −η¯ˆ |         | )2  |     |     |     |     |
| --- | --- | --- | -------------- | ----- | ---- | ------- | --- | --- | --- | --- | --- |
|     |     |     |                | s,T+i |      | s,T+k−1 |     |     |     |     |     |
|     | σ   | =   |                | i=1   |      |         | .   |     |     |     |     |
HHH
|     |     | s,k−1 |     |     | k−2 |     |     |     |     |     |     |
| --- | --- | ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
In (4.6) and (4.7), I(·) denotes an indicator function, and z was chosen to be 2 with empirical
normal approximations for the internal parameters. When k = 1,2, δ = δ . The collection
|     |     |     |     |     |     |     |     |     |     | ξˆ ηˆ s,T+k |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----------- | --- |
k
of the historical estimates for the overdispersion parameter and GPD means aims at providing
a baseline pattern when no outbreaks have happened during the monitoring procedure. The true
posteriorsforthoselatentparametersdon’thaveanalyticexpressionthusthenormalapproximation
techniqueactsasarudimentaryscreeningforpotentialoutbreaks. Nonetheless,suchpreliminaryZ-
score-basedaberrationindicatorscontributetoarefinedp-value-basedoutbreakdetectionapproach
| in the next | step.      |     |            |     |     |     |     |     |     |     |     |
| ----------- | ---------- | --- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- |
| 4.3.3 Step  | 3: P-value |     | adaptation |     |     |     |     |     |     |     |     |
Since an outbreak is associated with the occurrence in a region of cases of an illness or health-
related events clearly in excess of normal expectancy, public health practitioners are more likely to
claim a disease outbreak when the observed incidence count in a region is unusually high or takes
a drastic jump, regarding the early outbreak detection application. It would be meaningless to
claim an outbreak when no significant deviation takes place from the past data pattern. Therefore,
one-sidedp-valuesbecomeanaturalmeasurementfortheoutbreakevidenceagainstH (s) . Notonly
0,k
97

can the p-values be converted to binary outcomes given a user-defined threshold as in Farrington’s
algorithm, but also provide the magnitude of extremeness for the observations under the null
hypotheses. However, p-values will have reduced significance at a contaminated baseline estimate
whentheslidingwindowcontainsamixtureofnon-epidemicandepidemicdata. Toboostthesignal
of a potential outbreak, we propose an adapted p-value computation with the latent aberration
indicators obtained in Step 2. In the k-th iteration, the adapted p-value at location s with the
| observed | count | y   | is  | calculated | as in | (4.8), |     |     |     |     |     |     |     |
| -------- | ----- | --- | --- | ---------- | ----- | ------ | --- | --- | --- | --- | --- | --- | --- |
s,T+k


|     |     |     |  p˜ |       | , if δ = | 1.  |     |     |     |     |     |     |     |
| --- | --- | --- | ----- | ----- | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
|     |     |     |       | s,T+k | ξˆ       |     |     |     |     |     |     |     |     |
|     |     | p∗  | =     |       | k        |     |     |     |     |     |     |     |     |
s,T+k
|     |     |     |   p |       | , if δ = | 0.  |     |     |     |     |     |     |     |
| --- | --- | --- | ------ | ----- | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
|     |     |     |        | s,T+k | ξˆ       |     |     |     |     |     |     |     |     |
k
|     |     | where |     |     |     |     |     |     |     |     |     |     | (4.8) |
| --- | --- | ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----- |

|     |     |     |       | (cid:16) |       |       |         |     | (cid:17) |      |          |      |     |
| --- | --- | --- | ----- | -------- | ----- | ----- | ------- | --- | -------- | ---- | -------- | ---- | --- |
|     |     |     |      |          |       | |η¯ˆ  |         | ¯ˆ  | (s )     |      |          |      |     |
|     |     |     |  Pr | Y        | > y   |       |         | ,ξ  | ,H       | , if | δ        | = 1. |     |
|     |     |     |       |          | s,T+k | s,T+k | s,T+k−1 | k−1 | 0 ,k     |      | ηˆ s,T+k |      |     |
|     |     | p˜  | =     |          |       |       |         |     |          |      |          |      |     |
s,T+k

|     |     |     |  p |       | ,   |     |     |     |     | if  | δ        | = 0. |     |
| --- | --- | --- | ---- | ----- | --- | --- | --- | --- | --- | --- | -------- | ---- | --- |
|     |     |     |      | s,T+k |     |     |     |     |     |     | ηˆ s,T+k |      |     |
The adaptation for the p-value in (4.8) is determined by δ and δ . When both the global
|     |     |     |     |     |     |     |     |     | ξˆ  | ηˆ s,T+k |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | -------- | --- | --- | --- |
k
andlocallatentaberrationsforlocationsaretriggered,thecorrespondingp-valuewillbeadaptively
calculatedusingsmallerestimatesofbaselineGPDmeanandoverdispersion,inordertoincreasethe
significance of a potential outbreak. Otherwise, the regular Bayesian posterior predictive p-values
| are computed |     | to quantify |     | the evidence | against |     | H (s) as | in (4.9), |     |     |     |     |     |
| ------------ | --- | ----------- | --- | ------------ | ------- | --- | -------- | --------- | --- | --- | --- | --- | --- |
0,k
|       |     | (cid:16) |       |       |            |     | (cid:17) |     |     |     |     |     |     |
| ----- | --- | -------- | ----- | ----- | ---------- | --- | -------- | --- | --- | --- | --- | --- | --- |
| p     | =   | Pr Y     | >     | y     | |DDD ,DDD∗ | ,H  | (s)      |     |     |     |     |     |     |
| s,T+k |     |          | s,T+k | s,T+k | k k−T−1    |     |          |     |     |     |     |     |     |
0,k
(cid:88)
|     |     |     |           |     |            |            | ,DDD∗ |     | (s)  |     |     |     |     |
| --- | --- | --- | --------- | --- | ---------- | ---------- | ----- | --- | ---- | --- | --- | --- | --- |
|     | =   |     | I(Y s,T+k | > y | s,T+k )p(Y | s,T+k |DDD | k     |     | ,H ) |     |     |     |     |
|     |     |     |           |     |            |            | k−T−1 |     | 0,k  |     |     |     |     |
Y s,T+k
|     |     |    |     |     |     |     |     |    |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
(cid:90)
(cid:88)
|     | =   |     | I(Y |       | > y   | )p(Y  | |ΘΘΘ)p(ΘΘΘ|DDD |     | ,DDD∗ |       | ,H (s ) | )dΘΘΘ | (4.9) |
| --- | --- | --- | --- | ----- | ----- | ----- | --------------- | --- | ----- | ----- | ------- | ----- | ----- |
|     |     |    |     | s,T+k | s,T+k | s,T+k |                 |     | k     | k−T−1 | 0 ,k    |       |       |
Y
s,T+k
(cid:90)
|     |     |      |       |           | |ΘΘΘ)p(ΘΘΘ|DDD | ,DDD∗ |       | (s) | )dΘΘΘ |     |     |     |     |
| --- | --- | ---- | ----- | --------- | -------------- | ----- | ----- | --- | ----- | --- | --- | --- | --- |
|     | =   | Pr(Y | s,T+k | > y s,T+k |                | k     |       | ,H  |       |     |     |     |     |
|     |     |      |       |           |                |       | k−T−1 | 0,k |       |     |     |     |     |
(cid:90) (cid:90)
|     | =   | Pr(Y |       | >   | y |η        | ,ξ  | )p(η  | ,ξ  | |DDD ,DDD∗ |       | ,H (s) | )dη   | dξ . |
| --- | --- | ---- | ----- | --- | ----------- | --- | ----- | --- | ---------- | ----- | ------ | ----- | ---- |
|     |     |      | s,T+k |     | s,T+k s,T+k | k   | s,T+k |     | k k        | k−T−1 | 0,k    | s,T+k | k    |
The p-value adaptation step has two major benefits in the detection procedure. First of all,
it can avoid weakening signals of potential outbreaks if the sliding window contains a mixture of
98

baseline data and outbreak data. When the (4.2) is fitted on the count data contaminated by
unusually large observations, the conditional GPD mean µ will be overestimated as well as
s,T+k
its overdispersion parameter λ thus leading to an overestimated variance µ /(1−λ )2, which
k s,T+k k
(s)
yields a large p-value weakening the evidence against H . Secondly, When no aberration alarms
0,k
are raised, the Bayesian posterior predictive p-value incorporates the uncertainty of the model
parameters by integrating the conventional p-value over their joint posterior density. Hence, the
(s)
Bayesian posterior predictive p-value provides a baseline significance level of rejecting H when
0,k
no outbreak occurs. In (4.9), η and ξ are sufficient for the computation of Bayesian p-value
s,T+k k
because η is a function of all other parameters and p can be approximated by the average
s,T+k s,T+k
of p-values conditional on the joint posterior samples of η and ξ . Next, the adapted p-values
s,T+k k
can be accumulated recursively for outbreak detection in the following step.
4.3.4 Step 4: Decision-making and algorithm update
Thedecision-makingstepisbasedoncombinedp-valuesfortworeasons: 1)someindividualp-values
obtained with small magnitude during the iterative procedure will not be necessarily caused by an
outbreak, especially if the monitored data have a highly overdispersed pattern and the procedure
hasn’t encountered any extreme observations due to overdispersion. 2) The successive modeling
fitting procedure with a sliding window has training data set with overlaps, which introduces a
dependent association among the sequential hypothesis tests. For example, the intersection of two
consecutive training data sets,DDD andDDD , isDDD ∩DDD = {YYY }T−1. Therefore, such decision-
k−1 k k−1 k k+t t=0
making in the online outbreak detection procedure will integrate dependent historical information
to assess the ongoing dynamics in the surveillance system via a combined p-value approach. The
combined p-value approach is known as the global test (also named omnibus test) of p-values and
it is a popular technique in high-dimensional genetic data analysis for multiple hypothesis tests. A
plethora of research work has been done to combine independent and dependent p-values for the
global test in the genetic study. Instead of combining all available p-values and performing a single
global test, the online procedure keeps updating recent p-values sequentially until an outbreak is
detected thus leading to a series of affiliated global tests. With the adapted p-value calculated in
99

the previous step, the k-th cumulative detector statistics will be updated as in (4.10),
Q = Q +g(p∗ )
s,T+k s,T+k−1 s,T+k
where
(4.10)
k−1
(cid:88)
Q = g(p∗ ) and Q = 0.
s,T+k−1 s,T+i s,T+0
i=1
In (4.10), g(·) is a transformation function of the p-values. In the conventional tests of combined
p-values, the classical choices for g(·) include log transformation (Fisher, 1932), inverse Gaussian
transformation (Stouffer et al., 1949) and inverse gamma transformation (Lancaster, 1961). When
p-values follow the identical and independent uniform distribution under the global null hypoth-
esis, Q will have simple limiting distributions. However, When p-values are dependent, the
s,T+k
resulting distribution of Q becomes complicated and adjustments can be made to account for
s,T+k
the dependence via using an effective number of tests (Cheverud, 2001; Nyholt, 2004; Li and Ji,
2005; Gao et al., 2008; Galwey, 2009), using re-sampling methods such as permutation tests for an
empiricaldistributionalapproximationforthecombinedp-values(WestfallandYoung,1993;Good,
2013), or applying generalized multivariate theory to the classical choices of g(·) under dependence
(Brown, 1975; Kost and McDermott, 2002; Yang et al., 2016). Recent powerful combined p-value
tests include the Harmonic Mean P-value (HMP) approach (Wilson, 2019) and Cauchy Combina-
tion Test (CCT) approach (Liu and Xie, 2020), which can handle arbitrary correlation structure
among the test statistics although HMP approach doesn’t have the exact additive property shown
in (4.10).
Therefore, the real-time outbreak detection indicator δ for county s at iteration k is deter-
s,T+k
mined as in (4.11),

δ =
  I(Q
s,T+k
> q
s
α
,T+k
), ∃ k∗ ≤ k,s.t. δ
ξˆ k∗
= 1,
(4.11)
s,T+k

 0, otherwise,
where qα is the threshold associated with the corresponding method and α is the nominal level
s,T+k
for false detection control pre-determined by practitioners. Such a decision rule aims at controlling
false detection rates due to data overdispersion and increasing detection power when outbreaks
100

happen. At the end of iteration k, The baseline-resembling sets for the overdispersion parameter
| and the | conditional | GDP |       | mean are | updated            |       | as follows, |       |         |         |     |
| ------- | ----------- | --- | ----- | -------- | ------------------ | ----- | ----------- | ----- | ------- | ------- | --- |
|         |             | HHH | =HHH  | ∪        | (cid:8)(cid:0) 1−δ |       | (cid:1) ηˆ  | +δ    | η¯ˆ     | (cid:9) |     |
|         |             | s,k | s,k−1 |          |                    | ηˆ    | s,T+k       | ηˆ    | s,T+k−1 |         |     |
|         |             |     |       |          |                    | s,T+k |             | s,T+k |         |         |     |
(4.12)
|     |     |     |       | (cid:110)(cid:16) |      |     |      | ¯ˆ    |     |     | (cid:17)(cid:111) |
| --- | --- | --- | ----- | ----------------- | ---- | --- | ---- | ----- | --- | --- | ----------------- |
|     |     | ΞΞΞ | =ΞΞΞ  | ∪                 | (1−δ | )ξˆ | +δ ξ | ,(1−δ | )σˆ | +δ  | σ¯ˆ               |
|     |     | s,k | s,k−1 |                   |      | ξˆ  | k ξˆ | k−1   | ξˆ  | ξ   | ξˆ ξ              |
|     |     |     |       |                   |      | k   | k    |       | k   | k   | k k−1             |
Themainpurposeof(4.12)istoobviatecontaminationofthebaselinecollectionbyanyaberrant
estimates thus enhancing the sensitivity of the algorithm. Meanwhile, the posterior inference will
also be collected in Table 14 for future use as prior information. In the next subsection, we are
going to implement the eclectic framework via numerical studies and demonstrate its performance
| in different  | aspects.   |       |       |     |     |     |     |     |     |     |     |
| ------------- | ---------- | ----- | ----- | --- | --- | --- | --- | --- | --- | --- | --- |
| 4.4 Numerical |            | study |       |     |     |     |     |     |     |     |     |
| 4.4.1         | Simulation |       | study |     |     |     |     |     |     |     |     |
Inoursimulation, wearegoingtoillustratetheperformanceoftheBOSTON-PUPAapproachfrom
two aspects: (1) Model parameter recovery and in-sample model prediction; (2) Online outbreak
detection. For a better replication of the actual data pattern, the parameters in the model in (4.2)
is based on the model inference on the partial real data of daily confirmed COVID-19 case count
starting from June 15, 2020, which we assume to be in the non-outbreak phase before the news
report of an outbreak in the fall. The Boston Globe reported on October 26, that COVID-19 cases
| in the state | had | risen | sharply | on  | October | 22, |     |     |     |     |     |
| ------------ | --- | ----- | ------- | --- | ------- | --- | --- | --- | --- | --- | --- |
”After a sudden jump Thursday, Massachusetts coronavirus cases have been maintaining levels we
haven’t seen in months, raising concern among experts that the state might need to consider
|     |     |     | rolling | back | some | parts | of its | reopening | process.” |     |     |
| --- | --- | --- | ------- | ---- | ---- | ----- | ------ | --------- | --------- | --- | --- |
A detailed real data description will be given in the real application section. The parameters
include fixed effects β (related to county-wise population density, a ratio of its population to
den
the corresponding area), β (related to the Day of Week effect), and β (related to a linear
|     |     |     |     | DOW |     |     |     |     |     |     | time |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---- |
time trend), as well as other spatio-temporal hyperparameters for the random effects. They are
summarized in Table 15. For constant terms, W is based on the border-sharing adjacency of 14
101

counties in Massachusetts. Due to the small populations of Dukes and Nantucket, we merged
these two neighboring island counties into one to avoid extreme population imbalance, and P are
s
| logarithms |           | of  | the county | populations |        | recorded | in 2018        | in Table | 16. |     |              |
| ---------- | --------- | --- | ---------- | ----------- | ------ | -------- | -------------- | -------- | --- | --- | ------------ |
|            | Parameter |     |            |             | Symbol | Value    | Hyperparameter |          |     |     | Symbol Value |
|            | Intercept |     |            |             | β      | -13.5752 | Overdispersion |          |     |     | λ .4448      |
0
Population density effect β den .2905 Temporal correlation ρ ϵ .5123
|     | Day  | of Week | effect |     | β    | .1762 | Temporal |     | variance    |     | σ2 .2609 |
| --- | ---- | ------- | ------ | --- | ---- | ----- | -------- | --- | ----------- | --- | -------- |
|     |      |         |        |     | DOW  |       |          |     |             |     | ϵ        |
|     | Time | trend   | effect |     | β    | .3056 | Spatial  |     | correlation |     | ρ .3588  |
|     |      |         |        |     | time |       |          |     |             |     | ϕ        |
σ2
|     |     |     |     |     |     |     | Spatial |     | variance |     | .7275 |
| --- | --- | --- | --- | --- | --- | --- | ------- | --- | -------- | --- | ----- |
ϕ
|     |     |     | Table   | 15:       | Parameter | setup | throughout | the | simulation      |     | study |
| --- | --- | --- | ------- | --------- | --------- | ----- | ---------- | --- | --------------- | --- | ----- |
|     |     |     | Spatial | ID County | name      |       | Population |     | log(Population) |     | (P )  |
s
|     |     |     | 1   | Plymouth   |        |             | 518132  |               | 13.1580 |         |     |
| --- | --- | --- | --- | ---------- | ------ | ----------- | ------- | ------------- | ------- | ------- | --- |
|     |     |     | 2   | Berkshire  |        |             | 126348  |               | 11.7468 |         |     |
|     |     |     | 3   | Barnstable |        |             | 213413  |               | 12.2710 |         |     |
|     |     |     | 4   | Norfolk    |        |             | 705388  |               | 13.4665 |         |     |
|     |     |     | 5   | Bristol    |        |             | 564022  |               | 13.2428 |         |     |
|     |     |     | 6   | Suffolk    |        |             | 807252  |               | 13.6014 |         |     |
|     |     |     | 7   | Franklin   |        |             | 70963   |               | 11.1699 |         |     |
|     |     |     | 8   | Hampshire  |        |             | 161355  |               | 11.9914 |         |     |
|     |     |     | 9   | Essex      |        |             | 790638  |               | 13.5806 |         |     |
|     |     |     | 10  | Hampden    |        |             | 470406  |               | 13.0614 |         |     |
|     |     |     | 11  | Dukes      | and    | Nantucket   | 28679   |               | 10.2639 |         |     |
|     |     |     | 12  | Middlesex  |        |             | 1614710 |               | 14.2947 |         |     |
|     |     |     | 13  | Worcester  |        |             | 830839  |               | 13.6302 |         |     |
|     |     |     |     | Table 16:  | County | populations | in      | Massachusetts |         | in 2018 |     |
4.4.1.1 Model parameter recovery and in-sample model prediction Duetotheiterative
feature of the BOSTON-PUPA framework, the quality of model inference and prediction is influ-
encedbychoicesoftheslidingwindowsize(T)andhistoricalinformationdiscountingfactora . For
0
aproofofconcept,weconducteddifferentcombinationsofslidingwindowsizesT = 14,21,28,35,42
and discounting factors a = 0.25,0.5,1. The total number of simulations is 200. For each simu-
0
lation, the total number of simulated case counts at each location is T = 200. To illustrate the
0
performance of parameter recovery for the baseline data, we only simulated the data without any
outbreak, and outbreak detection performance will be demonstrated in the next subsection. The
102

measurement of the parameter recovery is defined as a binary outcome of whether or not the true
parameters from the setup are captured by their corresponding 95% posterior credible interval in
the BOSTON-PUPA procedure. As for the measurement of in-sample prediction, we measure the
Mean-Squared-Error (MSE) between the true observation and in-sample prediction for the last day
in the sliding window, because latent aberration assessment in step 2 is dependent on the last-day
estimates ηˆ and historical baseline estimates η¯ˆ in (4.7). Therefore, there are in total
s,T+k s,T+k−1
(T −T)×200 model fittings in the simulation study, from which we summarized the performance
0
of parameter recovery and in-sample model prediction. The results are shown in Table 17 and 18,
From Table 17, we can see that all the fixed effect and hyperparameter recovery rates increase
with a larger sliding window size (T) and a smaller discounting factor (a ), except for the temporal
0
variance (σ2). For the majority of the parameters, a sliding window with a larger width provides
ϵ
moreinformationinthetrainingdata,whichcanenhancethemodelinference. Meanwhile,asmaller
discounting factor dampens the certainty of historical information prior and grants more flexibility
for the INLA solver to explore the posterior distribution for the current training data. Since all the
internal parameter representations are assigned with a Gaussian prior, the original variance σ2 in
the prior turns into σ2/a after discounting and shows complete historical information (a =1) does
0 0
notyieldgoodmodelinferenceaccordingtoTable17. However, sincethelogarithmicGDPmeanin
(4.2) contains a summation of separable spatial effect and temporal effect, a larger sliding window
size tends to reduce more uncertainty about the spatial effect than the temporal effect, which can
explain why there is an opposite relationship between parameter recovery rate and sliding window
size for the temporal variance (σ2). Although the hyperparameter recovery rates for the spatial
ϵ
effectsandthetemporaleffectsarenotasgoodastheotherparameters, itisstillsatisfactorytoget
recovery rates above 70% for these second-level parameters with appropriate selections for T and
a . From Table 18, the choice of discounting factor has a negligible impact on the MSE. Although
0
theretendstobeaslightpositiverelationshipbetweenslidingwindowsizeandMSE,theincrements
are not significant and it is related to different total numbers of model fittings ((T −T)×200) in
0
the MSE calculation.
An appropriate selection of sliding window size is a trade-off between methodological efficiency
and detection timeliness. As is demonstrated in Farrington and Andrews (2003), the size of train-
ing data to reflect a baseline pattern ranges from 2 to 8 weeks, depending on the specifics in the
103

| Parameter | a   | (T=)14 | 21  | 28  | 35  | 42  |
| --------- | --- | ------ | --- | --- | --- | --- |
0
|     | 0.25 | 0.9910 | 0.9900 | 0.9907 | 0.9870 | 0.9847 |
| --- | ---- | ------ | ------ | ------ | ------ | ------ |
| β   | 0.5  | 0.9703 | 0.9658 | 0.9692 | 0.9643 | 0.9673 |
0
|     | 1    | 0.5159 | 0.6509 | 0.7458 | 0.8068 | 0.8458 |
| --- | ---- | ------ | ------ | ------ | ------ | ------ |
|     | 0.25 | 0.9442 | 0.9439 | 0.9419 | 0.9403 | 0.9394 |
| β   | 0.5  | 0.9234 | 0.9209 | 0.9210 | 0.9194 | 0.9181 |
den
|     | 1    | 0.6557 | 0.7469 | 0.7938 | 0.8240 | 0.8462 |
| --- | ---- | ------ | ------ | ------ | ------ | ------ |
|     | 0.25 | 0.9485 | 0.9546 | 0.9544 | 0.9544 | 0.9509 |
| β   | 0.5  | 0.9620 | 0.9639 | 0.9616 | 0.9605 | 0.9580 |
DOW
|        | 1    | 0.9088 | 0.9303 | 0.9352 | 0.9377 | 0.9348 |
| ------ | ---- | ------ | ------ | ------ | ------ | ------ |
|        | 0.25 | 0.9870 | 0.9855 | 0.9857 | 0.9824 | 0.9785 |
| β time | 0.5  | 0.9701 | 0.9703 | 0.9710 | 0.9671 | 0.9672 |
|        | 1    | 0.5428 | 0.6732 | 0.7756 | 0.8363 | 0.8690 |
|        | 0.25 | 0.9633 | 0.9650 | 0.9668 | 0.9642 | 0.9633 |
| λ      | 0.5  | 0.9691 | 0.9702 | 0.9695 | 0.9663 | 0.9659 |
|        | 1    | 0.9313 | 0.9413 | 0.9453 | 0.9502 | 0.9478 |
|        | 0.25 | 0.8921 | 0.9163 | 0.9276 | 0.9328 | 0.9352 |
| ρ      | 0.5  | 0.9010 | 0.9122 | 0.9262 | 0.9297 | 0.9360 |
ϵ
|     | 1    | 0.6213 | 0.7358 | 0.8137 | 0.8592 | 0.8735 |
| --- | ---- | ------ | ------ | ------ | ------ | ------ |
|     | 0.25 | 0.8448 | 0.8340 | 0.8178 | 0.7934 | 0.7643 |
| σ2  | 0.5  | 0.8269 | 0.7998 | 0.7711 | 0.7452 | 0.7206 |
ϵ
|     | 1    | 0.4845 | 0.5213 | 0.5471 | 0.5658 | 0.5722 |
| --- | ---- | ------ | ------ | ------ | ------ | ------ |
|     | 0.25 | 0.5702 | 0.6649 | 0.7343 | 0.7587 | 0.7935 |
| ρ   | 0.5  | 0.5535 | 0.6348 | 0.7044 | 0.7501 | 0.8020 |
ϕ
|     | 1    | 0.5157 | 0.6242 | 0.6912 | 0.7542 | 0.7947 |
| --- | ---- | ------ | ------ | ------ | ------ | ------ |
|     | 0.25 | 0.8796 | 0.8963 | 0.9128 | 0.9206 | 0.9267 |
σ2
|     | 0.5 | 0.3681 | 0.4372 | 0.5365 | 0.6554 | 0.7435 |
| --- | --- | ------ | ------ | ------ | ------ | ------ |
ϕ
|     | 1   | 0.1349 | 0.1983 | 0.2714 | 0.3561 | 0.4446 |
| --- | --- | ------ | ------ | ------ | ------ | ------ |
Table 17: Parameter recovery rate under different combinations of sliding window size and prior
discounting factor
(cid:97)
(cid:97) (cid:97)
| (cid:97) |     | T   |     |     |     |     |
| -------- | --- | --- | --- | --- | --- | --- |
(cid:97)
(cid:97)
|     | (cid:97) (cid:97) | 14  | 21  | 28  | 35  | 42  |
| --- | ----------------- | --- | --- | --- | --- | --- |
(cid:97)
| a         | (cid:97) |              |            |        |             |        |
| --------- | -------- | ------------ | ---------- | ------ | ----------- | ------ |
| 0         |          | (cid:97)     |            |        |             |        |
| 0.25      |          | 9.1479       | 9.3548     | 9.4971 | 9.6074      | 9.7028 |
| 0.5       |          | 9.1456       | 9.3497     | 9.4958 | 9.6064      | 9.7019 |
| 1         |          | 9.1395       | 9.3471     | 9.4942 | 9.6051      | 9.7009 |
| Table 18: | MSE for  | the last-day | prediction | in     | the sliding | window |
104

surveillance system such as the disease outbreak span or data format from regulatory authorities.
The computational cost is another criterion to choose a better combination of tuning parameters.
However, due to the initial value self-correction feature of the internal rinla program, the time con-
sumption can have a wide range in different simulations, which is less reliable to quantify the model
computationalspeed. Ingeneral,alargerslidingwindowtendstohaveahighercomputationalcost.
Taking into account all the combinations of sliding window sizes and discounting factors, we can
moderately select T = 28 and a = 0.25 for the procedure BOSTON-PUPA. Since the optimal
0
tuning parameter selection for our proposed framework is not the focus of this dissertation, we
will just proceed with the outbreak detection performance evaluation with a reasonable choice for
T and a . As a comparison, we also considered using all historical data in a sequential approach
0
in which the window size increases with newly observed data and weakly informative priors are
maintainedthroughouttheprocedure. InTable19, ourPriorUpdating(PU)approachwithT = 28
and a = 0.25 have an overall better performance than the cumulative fitting (CF) approach in
0
| terms of parameter | recovery | and   | in-sample | prediction  | accuracy. |       |       |
| ------------------ | -------- | ----- | --------- | ----------- | --------- | ----- | ----- |
| Performance        |          | PU    | CF        | Performance |           | PU    | CF    |
| β recovery         | rate     | .9907 | .9450     | σ2 recovery | rate      | .8178 | .5631 |
| 0                  |          |       |           | ϵ           |           |       |       |
| β recovery         | rate     | .9419 | .9408     | ρ recovery  | rate      | .7343 | .9715 |
| den                |          |       |           | ϕ           |           |       |       |
σ2
| β DOW | recovery rate | .9544 | .9505 | recovery | rate | .9128 | .9646 |
| ----- | ------------- | ----- | ----- | -------- | ---- | ----- | ----- |
ϕ
| β recovery | rate | .9857 | .9315 | MSE |     | 9.4971 | 27.3535 |
| ---------- | ---- | ----- | ----- | --- | --- | ------ | ------- |
time
λ recovery rate .9668 .9473 Computational time 74.3770 (s) 133.0322 (s)
| ρ recovery | rate | .9276 | .9159 |     |     |     |     |
| ---------- | ---- | ----- | ----- | --- | --- | --- | --- |
ϵ
Table 19: Performance comparison between Prior Updating (PU) approach (T = 28,a = .25) and
0
Cumulative Fitting (CF) approach. Computation time is calculated as the average computation
| time in seconds | for individual | model | fittings | in the | iterative process. |     |     |
| --------------- | -------------- | ----- | -------- | ------ | ------------------ | --- | --- |
4.4.1.2 Outbreak detection performance Next,wewilldemonstratetheoutbreakdetection
performance of the BOSTON-PUPA framework under different scenarios of signal-to-noise ratio
(SNR). We keep the parameter setup in the previous section and introduce disease outbreaks at
| different locations. |     |     |     |     |     |     |     |
| -------------------- | --- | --- | --- | --- | --- | --- | --- |
In the data generation process, the outbreak occurring time stamps τ ,s = 1,2,...,13, were
s
randomly generated from a Poisson distribution with mean 100 as 103, 99, 95, 82, 102, 102, 102,
91, 89, 97, 109, 100 and 87, which divided the 13 locations into non-outbreak and outbreak phases
105

correspondingly. Baseline counts were generated for each location throughout T = 200 days and
0
outbreaks were introduced after the outbreak time stamps accordingly given the SNR in (4.13),
Y |θ ,λ ∼ GPD(θ +δ θ∗ ,λ),
s,t s,t s,t s,t s,t
(4.13)
θ∗ = (r−1)θ ,
s,t s,t
where SNR is r = Var(Y |rθ ,λ)/Var(Y |θ ,λ) and δ is a binary outbreak indicator for
s,t s,t s,t s,t s,t
location s on day t. We also considered numerical adjustment by adding 5 to θ∗ when introducing
s,t
outbreak into baseline data, because the multiplicative association between θ and θ∗ won’t
s,t s,t
add meaningful outbreak to the baseline data when θ is close to zero. For real application in
s,t
surveillance systems, practitioners will also set a minimum bar for the observed counts before
claiming a reasonable outbreak.
InStep4oftheBOSTON-PUPAprocedure,wechosebothclassicalandrecentcombinedp-value
for dependent hypothesis tests: Fisher’s, Lancaster’s, and Stouffer’s approaches adjusted with the
effectivenumberofhypothesistests(LiandJi,2005),P-value(HMP)andCauchyCombinationTest
(CCT) approach from existing R packages, poolr, ACAT, and harmonicmeanp. Four measurements
were taken to evaluate the outbreak detection performance among these methods with/without
p-value adaptation: Sensitivity = TP/(TP+FN), Specificity = TN/(TN+FP), Proportion of False
Positive (PropFP) = FP/(TP+FP), and Global Error (GE) = (FP+FN)/(TN+TP+FP+FN). We
set α = 0.05 for the false detection control and investigate the detection performance when SNR =
1 (No outbreak), 1.25, 1.5, 1.75, and 2 with 200 simulations for each scenario. We will summarize
the outbreak detection performance of the BOSTON-PUPA procedure from the following four
perspectives:
1. Performance enhancement by P-value Adaptation (PA). To illustrate the detection
performance enhancement by PA technique, four evaluation measurements are aggregated by
different combined p-value methods as well as all spatial locations, compared only regarding
whetherincorporationofPAtechniqueisappliedintheoutbreakdetectionprocedure. InFig-
ure19, thereisasignificantimprovementinincreasingSensitivityandGEwithPAtechnique.
When SNR ranges from 1.25 to 2, a larger SNR leads to less variation on those four perfor-
106

mance measurements especially for Sensitivity and GE, as the outbreak signal strengthens.
Although PA technique doesn’t give a superior Specificity and PropFP over its exclusion, the
benefit of PA technique can still be asserted. According to the formulae of the Specificity and
PropFP, a high value of Specificity or a low value of PropFP implies a small portion of false
positives are produced in the detection procedure, which is expected for an ideal outbreak
detection procedure. However, with comparable Specificity and PropFP, the incorporation of
PAtechniquewithhigherSensitivitymeasurementhasahigherpowerthanNo-PAtechnique.
Instead of being overly conservative in the detection procedure, PA technique can boost the
outbreak signal and actively facilitate accurate outbreak claims, which is a crucial attribute
of an efficient online outbreak detection procedure. It is worth mentioning that PA technique
grants an average of Sensitivity as high as about 75% even when the SNR = 1.25.
| 1.00 |     |     | 1.00 |     |     |     |
| ---- | --- | --- | ---- | --- | --- | --- |
| 0.75 |     |     | 0.75 |     |     |     |
ytivitisneS yticificepS
| 0.50 |          |     | 0.50 |     |      |     |
| ---- | -------- | --- | ---- | --- | ---- | --- |
| 0.25 |          |     | 0.25 |     |      |     |
| 0.00 |          |     | 0.00 |     |      |     |
| 1.25 | 1.5 1.75 | 2   | 1.25 | 1.5 | 1.75 | 2   |
|      | SNR      |     |      | SNR |      |     |
| 1.00 |          |     | 1.00 |     |      |     |
| 0.75 |          |     | 0.75 |     |      |     |
PFporP
| 0.50 |          | EG  | 0.50 |     |      |     |
| ---- | -------- | --- | ---- | --- | ---- | --- |
| 0.25 |          |     | 0.25 |     |      |     |
| 0.00 |          |     | 0.00 |     |      |     |
| 1.25 | 1.5 1.75 | 2   | 1.25 | 1.5 | 1.75 | 2   |
|      | SNR      |     |      | SNR |      |     |
Adaptation
|        |                     | Adaptation    | No−adaptation |              |     |     |
| ------ | ------------------- | ------------- | ------------- | ------------ | --- | --- |
| Figure | 19: Signal-to-ratio | vs Aggregated | Performance   | Measurements |     |     |
2. Empirical detection power and delay. Regarding the empirical detection power, the
relativefrequenciesofdetectinganoutbreakoutof200simulationsusingtheBOSTON-PUPA
107

procedure are collected in Table 20. When SNR = 1, the relative frequencies can be regarded
as empirical false detection rates accordingly for each location. For all of combined p-value
methods, the empirical false detection rates are controlled at α = 5% or with slight inflation
(5.5% ∼ 6.5%) except for locations with spatial IDs, 2, 3, 7, 8, and 11, which correspond
to the ones with the first five smallest populations in the study. HMP and CCT methods
have a better false detection control (< 5%) for these less populated locations than the other
methods(4% ∼ 16%)usingtheadjustmentofeffectivenumbersoftestsandStouffer’smethod
has the most inflated false detection rates (12.5% ∼ 16%).
When SNR = 1.25,1.5,1.75, and 2, the relative frequencies can be interpreted as empirical
detection powers. BOSTON-PUPA procedure demonstrates its powerful detection perfor-
mance for all methods for outbreaks with different signal-to-ratios. The detection powers
reach as high as over 80% when SNR starts at 1.25 and increase to nearly 100% for larger
SNRs. HMP and CCT methods are uniformly more powerful than Fisher’s, Stouffer’s, and
Lancaster’s methods for locations with large populations. Although Fisher’s, Stouffer’s and
Lancaster’s methods demonstrate their high power in those less populated locations, such
high powers also result from their excessive false detection rates so that outbreaks detected
by HMP and CCT methods have more credibility.
When outbreaks are detected for the streaming data, it is also important to study the dis-
tributions of the detected outbreak time points for detection delay evaluation. Figure 20
presents empirical distributions for the detection delays. For the locations with large popu-
lations, the outbreak indicators are triggered around the actual outbreak time points given
in the simulation study. As SNR increases, the empirical distributions of detected outbreaks
tend to concentrate more on the true values. For the less populated locations, 2,3,7,8, and
11, outbreaks are detected before their true occurrences, while detected outbreaks have a
wider spread for the rest of the locations. For the locations with small populations, the
false detection was made almost at the earliest true break, τ = 82, because the combined
4
p-values based on Fisher’s, Stouffer’s, and Lancaster’s methods had already been below α be-
fore the global aberration indicator was triggered at τ = 82. According to the decision rule
4
in Step 4, these regional outbreaks will be claimed immediately when the global aberration
108

alarm is triggered, which leads to the regional outbreak indicators δ dominated by the
s,T+k
global aberration indicator δ . We have also run simulations with decision rule not involving
ξˆ
k
the global indicator but the false outbreaks were way too early detected and could even be
claimed at the beginning of the monitoring process. Therefore, such domination helps avoid
false detection too early before true outbreaks for those three methods in small areas. From
this perspective, we need to acknowledge the limitation that controlled false detection rates
for the less populated areas only remain until a global aberration alarm is raised, because the
baseline GPD expectations have low or close to zero estimates, false outbreak detection is
very sensitive tosmall counts. Wehavedone the simulations aswell for early(around day50)
and late (around day 150) outbreaks across 13 locations and observed similar performance
among these methods. As a comparison, HMP and CCT methods show more robustness
against random fluctuations caused by data overdispersion.
Based on the empirical detection delays, it is also flexible for practitioners to customize
decision-making rules for individual locations. Rather than a proactive outbreak detection
strategy with the first non-zero δ , a scheme via aggregating the real-time outbreak
s,T+k
indicators using a screening window can help reduce the false detection but unavoidably
prolong the detection delay. Such trade-off strategies between low false detection rate and
short detection delay are more related to decision theory, and it is beyond the scope of this
dissertation.
3. Recommendations for combined p-value methods We would also like to compare dif-
ferent existing combined p-value methods and make recommendations to implement the
BOSTON-PUPA procedure. Figure 21 demonstrates the spatially aggregated detection per-
formance among those five methods when PA technique is incorporated. While Stouffer’s
method slightly falls short of the performance, the other four methods present competitive
performance. Fisher’s and Lancaster’s methods perform better than HMP and CCT meth-
ods regarding Sensitivity and GE, whereas the latter two methods have better Specificity
and PropFP. Before a final recommendation is made, the spatial detection performance can
be taken into consideration due to potential population imbalance for online spatio-temporal
data.
109

|        |       |     |       | Spatial | ID  |       |       |
| ------ | ----- | --- | ----- | ------- | --- | ----- | ----- |
| Method | SNR 1 | 2   | 3 4 5 | 6 7     | 8 9 | 10 11 | 12 13 |
1 0.035 0.14 0.045 0.04 0.04 0.05 0.16 0.095 0.04 0.055 0.16 0.035 0.045
1.25 0.765 0.99 0.93 0.815 0.78 0.73 0.99 0.985 0.84 0.83 0.99 0.75 0.8
Fisher 1.5 0.895 1 0.985 0.985 0.92 0.89 1 1 0.96 0.945 1 0.9 0.975
|     | 1.75 0.97 | 1   | 1 1 0.96  | 0.97 1  | 1 0.99  | 0.98 1 | 0.97 0.995 |
| --- | --------- | --- | --------- | ------- | ------- | ------ | ---------- |
|     | 2 0.98    | 1   | 1 1 0.985 | 0.985 1 | 1 0.995 | 1 1    | 0.99 0.995 |
1 0.02 0.16 0.125 0.03 0.04 0.025 0.16 0.155 0.035 0.065 0.16 0.02 0.025
1.25 0.745 0.99 0.98 0.79 0.695 0.465 0.99 0.99 0.685 0.85 0.99 0.45 0.745
Stouffer 1.5 0.905 1 1 0.97 0.875 0.725 1 1 0.895 0.95 1 0.745 0.93
|     | 1.75 0.955 | 1   | 1 1 0.95 | 0.87 1  | 1 0.985 | 0.97 1 | 0.895 0.995 |
| --- | ---------- | --- | -------- | ------- | ------- | ------ | ----------- |
|     | 2 0.99     | 1   | 1 1 0.96 | 0.945 1 | 1 0.995 | 0.99 1 | 0.94 1      |
1 0.04 0.125 0.04 0.04 0.045 0.05 0.155 0.06 0.04 0.045 0.16 0.05 0.05
1.25 0.765 0.985 0.915 0.835 0.79 0.765 0.99 0.985 0.84 0.825 0.99 0.785 0.805
Lancaster 1.5 0.9 1 0.98 0.98 0.925 0.93 1 1 0.97 0.95 1 0.925 0.975
|     | 1.75 0.97 | 1   | 1 1 0.965 | 0.975 1 | 1 0.99  | 0.975 1 | 0.98 0.995  |
| --- | --------- | --- | --------- | ------- | ------- | ------- | ----------- |
|     | 2 0.98    | 1   | 1 1 0.985 | 0.985 1 | 1 0.995 | 0.995 1 | 0.995 0.995 |
1 0.065 0.015 0.035 0.05 0.065 0.06 0.02 0.035 0.05 0.05 0.025 0.06 0.06
1.25 0.83 0.83 0.8 0.87 0.845 0.865 0.885 0.81 0.865 0.855 0.935 0.86 0.875
HMP 1.5 0.95 0.88 0.93 0.99 0.97 0.975 0.925 0.955 0.985 0.965 0.95 0.98 0.99
1.75 0.985 0.945 0.97 1 0.985 0.99 0.97 0.975 0.995 0.99 0.975 0.99 0.995
|     | 2 0.99 | 0.97 | 0.98 1 1 | 0.995 0.97 | 0.985 0.995 | 1 0.98 | 1 0.995 |
| --- | ------ | ---- | -------- | ---------- | ----------- | ------ | ------- |
1 0.065 0.025 0.035 0.05 0.065 0.06 0.025 0.045 0.05 0.05 0.03 0.06 0.06
1.25 0.84 0.855 0.84 0.87 0.85 0.865 0.91 0.855 0.87 0.86 0.955 0.86 0.88
CCT 1.5 0.955 0.915 0.945 0.99 0.97 0.975 0.955 0.97 0.985 0.97 0.96 0.98 0.99
1.75 0.985 0.96 0.98 1 0.985 0.99 0.985 0.975 0.995 0.99 0.985 0.99 0.995
|     | 2 0.99 | 0.98 | 0.99 1 1 | 0.995 0.995 | 0.99 0.995 | 1 0.99 | 1 0.995 |
| --- | ------ | ---- | -------- | ----------- | ---------- | ------ | ------- |
Table 20: Relative frequencies of detecting an outbreak out of 200 simulations for each location
|     | using different | methods | for different signal-to-noise | ratios. |     |     |     |
| --- | --------------- | ------- | ----------------------------- | ------- | --- | --- | --- |
Figure 22 and 23 demonstrate the performance of BOSTON-PUPA across different regions
with/without outbreaks. Since there was no outbreak added in the simulation study when
SNR = 1, the detection probabilities in Figure 24 only stand for false outbreak detection or
type I error. While the detection procedure maintains a controlled false detection rate for
regions 1, 4, 5, 6, 9, 10, 12, and 13, the false detection rates are inflated (greater than 5%
but less than 20%) in the rest of the regions for the classical methods: Fisher’s, Stouffer’s,
and Lancaster’s. The regions with excessive false positives correspond to the ones with the
first five smallest populations in Table 16, which implies that small populations can have
an impact on these classical combined p-value methods. Detection probabilities in Figure
110

| 1                                     | 2   | 3   | 4                                    | 1   | 2   | 3   | 4   |
| ------------------------------------- | --- | --- | ------------------------------------ | --- | --- | --- | --- |
| 0.20                                  |     |     | 0.20                                 |     |     |     |     |
| 0.15                                  |     |     | 0.15                                 |     |     |     |     |
| 0.10                                  |     |     | 0.10                                 |     |     |     |     |
| )52.1 = RNS( ytisned ytilibaborP 0.05 |     |     | )5.1 = RNS( ytisned ytilibaborP 0.05 |     |     |     |     |
| 0.00                                  |     |     | 0.00                                 |     |     |     |     |
| 5                                     | 6   | 7   | 8                                    | 5   | 6   | 7   | 8   |
| 0.20                                  |     |     | 0.20                                 |     |     |     |     |
| 0.15                                  |     |     | 0.15                                 |     |     |     |     |
| 0.10                                  |     |     | 0.10                                 |     |     |     |     |
| 0.05                                  |     |     | 0.05                                 |     |     |     |     |
| 0.00                                  |     |     | 0.00                                 |     |     |     |     |
| 9                                     | 10  | 11  | 12                                   | 9   | 10  | 11  | 12  |
| 0.20                                  |     |     | 0.20                                 |     |     |     |     |
| 0.15                                  |     |     | 0.15                                 |     |     |     |     |
| 0.10                                  |     |     | 0.10                                 |     |     |     |     |
| 0.05                                  |     |     | 0.05                                 |     |     |     |     |
| 0.00                                  |     |     | 0.00                                 |     |     |     |     |
13 50 100 150 200 50 100 150 200 50 100 150 200 13 50 100 150 200 50 100 150 200 50 100 150 200
| 0.20                                  |     |     | 0.20                               |                |     |     |     |
| ------------------------------------- | --- | --- | ---------------------------------- | -------------- | --- | --- | --- |
| 0.15                                  |     |     | 0.15                               |                |     |     |     |
| 0.10                                  |     |     | 0.10                               |                |     |     |     |
| 0.05                                  |     |     | 0.05                               |                |     |     |     |
| 0.00                                  |     |     | 0.00                               |                |     |     |     |
| 50 100 150 200                        |     |     |                                    | 50 100 150 200 |     |     |     |
|                                       | Day |     |                                    |                | Day |     |     |
| 1                                     | 2   | 3   | 4                                  | 1              | 2   | 3   | 4   |
| 0.20                                  |     |     | 0.20                               |                |     |     |     |
| 0.15                                  |     |     | 0.15                               |                |     |     |     |
| 0.10                                  |     |     | 0.10                               |                |     |     |     |
| )57.1 = RNS( ytisned ytilibaborP 0.05 |     |     | 0.05                               |                |     |     |     |
| 0.00                                  |     |     | )2 = RNS( ytisned ytilibaborP 0.00 |                |     |     |     |
| 0.20 5                                | 6   | 7   | 8 0.20                             | 5              | 6   | 7   | 8   |
| 0.15                                  |     |     | 0.15                               |                |     |     |     |
| 0.10                                  |     |     | 0.10                               |                |     |     |     |
| 0.05                                  |     |     | 0.05                               |                |     |     |     |
| 0.00                                  |     |     | 0.00                               |                |     |     |     |
| 9                                     | 10  | 11  | 12                                 | 9              | 10  | 11  | 12  |
| 0.20                                  |     |     | 0.20                               |                |     |     |     |
| 0.15                                  |     |     | 0.15                               |                |     |     |     |
| 0.10                                  |     |     | 0.10                               |                |     |     |     |
| 0.05                                  |     |     | 0.05                               |                |     |     |     |
| 0.00                                  |     |     | 0.00                               |                |     |     |     |
13 50 100 150 200 50 100 150 200 50 100 150 200 13 50 100 150 200 50 100 150 200 50 100 150 200
| 0.20           |     |               | 0.20               |                |     |     |     |
| -------------- | --- | ------------- | ------------------ | -------------- | --- | --- | --- |
| 0.15           |     |               | 0.15               |                |     |     |     |
| 0.10           |     |               | 0.10               |                |     |     |     |
| 0.05           |     |               | 0.05               |                |     |     |     |
| 0.00           |     |               | 0.00               |                |     |     |     |
| 50 100 150 200 |     |               |                    | 50 100 150 200 |     |     |     |
|                | Day |               |                    |                | Day |     |     |
|                |     | Method Fisher | Stouffer Lancaster | HMP            | CCT |     |     |
Figure20: EmpiricaldensityplotsofBOSTON-PUPAdetectedoutbreaktimepointwherethefirst
non-zero δ occurs in county s for different methods with different signal-to-noise ratios (> 1).
s,T+k
The red vertical lines represent the true outbreak time points given in the simulation study, 103,
99, 95, 82, 102, 102, 91, 89, 97, 109, 100, and 87 for each location respectively.
23 can be interpreted as false detection rate before the true outbreak timing and detection
power after the true outbreak. The red lines portray the expected performance of an ideal
detectionprocedure, whichhascontrolledfalsedetectionratesatlevelαbeforeanyoutbreaks
happen and enjoys a timely spike-up in detection power when there are any outbreaks. For
different regions and signal-to-noise ratios, HMP and CCT methods have better controlled
false detection rates and provide a more better resemblance of the ideal detection pattern.
Therefore, we recommend HMP or CCT method be implemented in the detection procedure
to handle inflated false detection rates in the regions with smaller populations.
4. Remarks We would also like to make two remarks on our detection framework regarding its
111

| 1.00        |     |      |     | 1.00        |      |     |      |     |
| ----------- | --- | ---- | --- | ----------- | ---- | --- | ---- | --- |
| 0.75        |     |      |     | 0.75        |      |     |      |     |
| ytivitisneS |     |      |     | yticificepS |      |     |      |     |
| 0.50        |     |      |     | 0.50        |      |     |      |     |
| 0.25        |     |      |     | 0.25        |      |     |      |     |
| 0.00        |     |      |     | 0.00        |      |     |      |     |
| 1.25        | 1.5 | 1.75 | 2   |             | 1.25 | 1.5 | 1.75 | 2   |
|             |     | SNR  |     |             |      | SNR |      |     |
| 1.00        |     |      |     | 1.00        |      |     |      |     |
| 0.75        |     |      |     | 0.75        |      |     |      |     |
PFporP
EG
| 0.50 |        |        |          | 0.50      |      |     |      |     |
| ---- | ------ | ------ | -------- | --------- | ---- | --- | ---- | --- |
| 0.25 |        |        |          | 0.25      |      |     |      |     |
| 0.00 |        |        |          | 0.00      |      |     |      |     |
| 1.25 | 1.5    | 1.75   | 2        |           | 1.25 | 1.5 | 1.75 | 2   |
|      |        | SNR    |          |           |      | SNR |      |     |
|      | Method | Fisher | Stouffer | Lancaster | HMP  | CCT |      |     |
Figure 21: Signal-to-ratio vs Evaluation Metrics for different combined p-value methods: Fisher’s,
Stouffer’s, Lancaster’s, HMP and CCT when P-value Adaptation is implemented.
implementation and property: (1) Correlation matrix calculation for dependent hypotheses
| testing; | (2) Sequential | estimation | of the overdispersion |     | parameter | λ.  |     |     |
| -------- | -------------- | ---------- | --------------------- | --- | --------- | --- | --- | --- |
•
Correlation matrix calculation. As is pointed out in Cinar and Viechtbauer (2022), the
adjustment for k dependent hypothesis tests the Fisher’s, Stouffer’s, and Lancaster’s
combined p-value methods stems from the scenario where a smaller number (< k) of
independent hypothesis tests are conducted, known as the effective number of tests.
The computation effective number of tests is mainly achieved through PCA of the k×k
correlation matrix R for the dependent hypothesis tests, which is based on test statis-
t
tics t ,t ,...,t under multivariate normality assumption. However, R can be consis-
|     | 1 2 | k   |     |     |     |     | t   |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
tentlyapproximatedbyR undertheregularityofthemultivariatecentrallimittheorem
Y
(Van der Vaart, 2000; H¨ardle and Simar, 2019), where R is the k×k correlation matrix
Y
of the observations, Y ,Y ,...,Y even if the observations are not normal. Hence, we
|     |     | 1   | 2 k |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
112

1 2 3 4
0.20
0.15
0.10
0.05
0.00
5 6 7 8
0.20
0.15
0.10
0.05
0.00
9 10 11 12
0.20
0.15
0.10
0.05
0.00
13 50 100 150 200 50 100 150 200 50 100 150 200
0.20
0.15
0.10
0.05
0.00
50 100 150 200
Day
)1
=
RNS(
ytilibaborP
noitceteD
Method
Fisher
Stouffer
Lancaster
HMP
CCT
Figure 22: Traceplot of outbreak detection probabilities from day 29 to day 200 across 13 regions.
Five combined p-value methods are compared at the nominal level α = 0.05, represented by the
red dashed horizontal lines.
supplied R by calculating the (T −T)×(T −T) correlation matrix of standardized
Ys 0 0
Y ,t = T +1,T +2,...,T for region s with adapted GPD mean and overdispersion
s,t 0
respectively from the simulation study without outbreak added, which was thought to
represent the baseline dependency among the hypothesis tests.
Although it has been shown the GPD model is almost symmetrical in shape, resembling
a normal distribution, when the values of θ are as high as 8 and 0 < λ < 0.5 (Con-
s,t
sul and Jain, 1973), the dynamic adaptation on the GPD mean and overdispersion can
distort the asymptotic normality of standardized Y and the efficient number of simu-
s,t
lations for a good baseline estimation of R is yet to be determined. Therefore, we need
t
to acknowledge from another four aspects the limitation of calculating the correlation
matrix of R in the BOSTON-PUPA procedure if one uses either adjusted Fisher’s,
Y
Stouffer’s, or Lancaster’s method: (1) The normality assumption for the test statis-
113

| 1                                  | 2   | 3   | 4                                 | 1   | 2   | 3   | 4   |
| ---------------------------------- | --- | --- | --------------------------------- | --- | --- | --- | --- |
| 1.00                               |     |     | 1.00                              |     |     |     |     |
| 0.75                               |     |     | 0.75                              |     |     |     |     |
| 0.50                               |     |     | 0.50                              |     |     |     |     |
| )52.1 = RNS( ytilibaborP noitceteD |     |     | )5.1 = RNS( ytilibaborP noitceteD |     |     |     |     |
| 0.25                               |     |     | 0.25                              |     |     |     |     |
| 0.00                               |     |     | 0.00                              |     |     |     |     |
| 5                                  | 6   | 7   | 8                                 | 5   | 6   | 7   | 8   |
| 1.00                               |     |     | 1.00                              |     |     |     |     |
| 0.75                               |     |     | 0.75                              |     |     |     |     |
| 0.50                               |     |     | 0.50                              |     |     |     |     |
| 0.25                               |     |     | 0.25                              |     |     |     |     |
| 0.00                               |     |     | 0.00                              |     |     |     |     |
| 9                                  | 10  | 11  | 12                                | 9   | 10  | 11  | 12  |
| 1.00                               |     |     | 1.00                              |     |     |     |     |
| 0.75                               |     |     | 0.75                              |     |     |     |     |
| 0.50                               |     |     | 0.50                              |     |     |     |     |
| 0.25                               |     |     | 0.25                              |     |     |     |     |
| 0.00                               |     |     | 0.00                              |     |     |     |     |
13 50 100 150 200 50 100 150 200 50 100 150 200 13 50 100 150 200 50 100 150 200 50 100 150 200
| 1.00                                    |     |     | 1.00                                 |                |     |     |     |
| --------------------------------------- | --- | --- | ------------------------------------ | -------------- | --- | --- | --- |
| 0.75                                    |     |     | 0.75                                 |                |     |     |     |
| 0.50                                    |     |     | 0.50                                 |                |     |     |     |
| 0.25                                    |     |     | 0.25                                 |                |     |     |     |
| 0.00                                    |     |     | 0.00                                 |                |     |     |     |
| 50 100 150 200                          |     |     |                                      | 50 100 150 200 |     |     |     |
|                                         | Day |     |                                      |                | Day |     |     |
| 1                                       | 2   | 3   | 4                                    | 1              | 2   | 3   | 4   |
| 1.00                                    |     |     | 1.00                                 |                |     |     |     |
| 0.75                                    |     |     | 0.75                                 |                |     |     |     |
| )57.1 = RNS( ytilibaborP noitceteD 0.50 |     |     | 0.50                                 |                |     |     |     |
| 0.25                                    |     |     | )2 = RNS( ytilibaborP noitceteD 0.25 |                |     |     |     |
| 0.00                                    |     |     | 0.00                                 |                |     |     |     |
| 1.00 5                                  | 6   | 7   | 8 1.00                               | 5              | 6   | 7   | 8   |
| 0.75                                    |     |     | 0.75                                 |                |     |     |     |
| 0.50                                    |     |     | 0.50                                 |                |     |     |     |
| 0.25                                    |     |     | 0.25                                 |                |     |     |     |
| 0.00                                    |     |     | 0.00                                 |                |     |     |     |
| 9                                       | 10  | 11  | 12                                   | 9              | 10  | 11  | 12  |
| 1.00                                    |     |     | 1.00                                 |                |     |     |     |
| 0.75                                    |     |     | 0.75                                 |                |     |     |     |
| 0.50                                    |     |     | 0.50                                 |                |     |     |     |
| 0.25                                    |     |     | 0.25                                 |                |     |     |     |
| 0.00                                    |     |     | 0.00                                 |                |     |     |     |
13 50 100 150 200 50 100 150 200 50 100 150 200 13 50 100 150 200 50 100 150 200 50 100 150 200
| 1.00           |     |               | 1.00               |                |     |     |     |
| -------------- | --- | ------------- | ------------------ | -------------- | --- | --- | --- |
| 0.75           |     |               | 0.75               |                |     |     |     |
| 0.50           |     |               | 0.50               |                |     |     |     |
| 0.25           |     |               | 0.25               |                |     |     |     |
| 0.00           |     |               | 0.00               |                |     |     |     |
| 50 100 150 200 |     |               |                    | 50 100 150 200 |     |     |     |
|                | Day |               |                    |                | Day |     |     |
|                |     | Method Fisher | Stouffer Lancaster | HMP            | CCT |     |     |
Figure 23: Traceplot of outbreak detection probabilities from day 29 to day 200 across 13 regions.
Five combined p-value methods are compared at the nominal level α = 0.05. The red dashed lines
stand for an ideal detection probability pattern of maintaining at the nominal level before any
outbreaks occur and spiking up promptly to 1 when there are any outbreaks.
tics is compensated by the approximated normality of the GPD model. (2) Estimation
accuracy of R is dependent on the simulation size, which is not the scope of this disser-
Y
tation. (3) Practical concern. In the simulation study, all the parameters are provided
and fixed beforehand but they will be estimated sequentially in the online detection
procedure, which requires further criteria to select reasonable parameter estimates for a
good baseline representation for R . (4) The approaches calculating effective numbers
Y
of hypothesis tests are rather ad hoc than principled techniques and should be applied
with caution (Dudbridge and Koeleman, 2004; Salyakina et al., 2005). These limitations
can convince practitioners to adopt the combined p-value methods handling arbitrary
correlation structures such as HMP or CCT method without dependency on R .
t
114

• Sequentialestimationoftheoverdispersionparameter ThedecisionruledescribedinStep
4 of the BOSTON-PUPA procedure involves the latent global aberration indicator δ
ξ
k
to ensure better control of potential false detection caused by data overdispersion. To
illustrate the importance of the global aberration indicator, we also collected from the
simulation study the sequential estimation of λˆ
k
= eξˆ k/(1+eξˆ k) and its adapted version
λ
¯ˆ
k
:= eξ
¯ˆ
k/(1+eξ
¯ˆ
k) in PA technique in Figure 24 and 25.
0.6
0.4
0.2
50 100 150 200
Day
^
)1=RNS(
l
Overdispersion
Estimated
Adapted
True value
Figure 24: Trajectories of sequential estimation of overdispersion parameter λ without any out-
breaks introduced (SNR =1) in the simulation study. Green lines stand for λˆ , blue lines stand for
k
λ
¯ˆ
, and the red line represents the actual value of the overdispersion parameter λ = .4448
k
Apart from a few numerical outliers in the computation, λˆ shares common trajectories
k
with λ
¯ˆ
when SNR =1 in Figure 24, which implies that δ = 1 for most of the time
k ξ
k
and agrees with the underlying fact of no outbreak. The aforementioned benefit of the
false detection control using the BOSTON-PUPA procedure can be supported by the
pattern of the estimated and adapted λ because small p-values caused by overdispersion
will not lead to an outbreak claim unless the first occurrence of a global aberration in
115

| 0.6         |     |     |     | 0.6        |     |     |     |     |
| ----------- | --- | --- | --- | ---------- | --- | --- | --- | --- |
| )52.1=RNS(  |     |     |     | )5.1=RNS(  |     |     |     |     |
| 0.4         |     |     |     | 0.4        |     |     |     |     |
| ^l          |     |     |     | ^l         |     |     |     |     |
0.2
0.2
|     | 50  | 100 | 150 | 200 | 50  | 100 | 150 | 200 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
|     |     | Day |     |     |     | Day |     |     |
0.8
| 0.6 |     |     |     | 0.6 |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
)57.1=RNS(
)2=RNS(
0.4
^l 0.4
^l
0.2
0.2
|     | 50  | 100 | 150            | 200               | 50         | 100 | 150 | 200 |
| --- | --- | --- | -------------- | ----------------- | ---------- | --- | --- | --- |
|     |     | Day |                |                   |            | Day |     |     |
|     |     |     | Overdispersion | Estimated Adapted | True value |     |     |     |
Figure 25: Trajectories of sequential estimation of overdispersion parameter λ with different SNRs
|     |     | Greenlinesstandforλˆ |     |     |     | ¯ˆ  |     |     |
| --- | --- | -------------------- | --- | --- | --- | --- | --- | --- |
inthesimulationstudy. , bluelinesstandforλ , andtheredlinerepresents
|     |     |     |     | k   |     | k   |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
the actual value of the overdispersion parameter λ = .4448. The two black vertical dashed lines
| stand for | τ = 82 and | τ +T | = 109+28 | = 137 accordingly. |     |     |     |     |
| --------- | ---------- | ---- | -------- | ------------------ | --- | --- | --- | --- |
|           | 4          | 11   |          |                    |     |     |     |     |
the process. Therefore, such a setup in the decision rule guarantees a long monitoring
horizon where the false detection rate is controlled before any true outbreaks occur. In
Figure25,therearehumpsinthetrajectoriesofλˆ
fordifferentSNRs,startingataround
k
the earliest outbreak day (τ = 82) in the simulation study, which indicates that at least
4
one of the regions is experiencing abnormally large confirmed case counts and triggers
a global aberration alarm for any subsequent outbreak detection for the regions at risk.
When the green trajectories deviate from the blue, region-specific Bayesian p-values get
boosted significance from adaptations for both the abnormal overdispersion and GPD
means.
λˆ
The U-shape pattern of implies another property of modeling a mixture of GPD data
116

with identical λ but different θ in the sliding window. The humps in Figure 25 die down
at around the day τ +T = 137, where τ = 109 is the last outbreak onset day in the
11 11
simulation study. Empirically, it can be observed that the overdispersion parameter (1)
is estimated consistently around its true value when the sliding window only contains
non-outbreak data. (2) is overestimated when the sliding window contains a mixture of
non-outbreak and outbreak data even though they are generated by identical λ, which
provides helpful information for outbreak detection. (3) returns to a consistent estimate
slightly larger than the true value when the sliding window contains only the outbreak
data. Such property can be further investigated with theoretical evidence but it won’t
be discussed in this dissertation.
4.4.2 Real application
For the real application part, we will implement the BOSTON-PUPA procedure for COVID-19
daily case count data in Massachusetts with HMP and CCT methods for p-value combination.
Firstly, we will conduct empirical data analysis to assert the validity of using a spatio-temporal
model framework. Secondly, we implement the BOSTON-PUPA procedure to real data and report
the detected outbreaks for each county.
4.4.2.1 COVID-19 Data description The daily COVID-19 confirmed case count data is
available in the COVID-19 Dashboard Data Repository created by the Center for Systems Science
and Engineering (CSSE) at Johns Hopkins University (Dong et al., 2020). In the evolution of
the pandemic, the frequency of the case count report has shifted from a daily basis to a weekly
basis. We focus on the daily case count data for the different counties in Massachusetts. To avoid
excessive zero daily counts, we combine the two adjacent island counties, Dukes and Nantucket
into one. The period of raw data we chose is between June 15th, 2020, and Dec 31st, 2020, with
only missing values on two days, Nov 31st (Thanksgiving) and Dec 25th (Christmas), while the
daily case counts on the following days Nov 27th and Dec 26th are nearly twice as usual. The total
number of days in our study will be T = 200 from summer to the end of the year 2020. Let Y
s,t
denote the daily case count of county s on day t. Our imputation for the missing values Yˆ and
s,t1
117

Yˆ
| and | data adjustment |     | are as follows | 2:  |     |     |     |     |     |
| --- | --------------- | --- | -------------- | --- | --- | --- | --- | --- | --- |
s,t2

|     |     |     |  Yˆ |        | ;Yˆ    |        |     |     |     |
| --- | --- | --- | ----- | ------ | ------ | ------ | --- | --- | --- |
|     |     |     |  =   | ⌊Y /2⌉ |        | = ⌊Y   | /2⌉ |     |     |
|     |     |     | s,t1  | s,t1+1 | s,t1+1 | s,t1+1 |     |     |     |

|     |     |     |  Yˆ = | ⌊Y /2⌉ | ;Yˆ    | = ⌊Y   | /2⌉ |     |     |
| --- | --- | --- | ------- | ------ | ------ | ------ | --- | --- | --- |
|     |     |     | s,t2    | s,t2+1 | s,t2+1 | s,t2+1 |     |     |     |
Figure 26 presents the evolution of daily confirmed case counts. Across all the regions, the
daily count data have remained roughly stable or a slightly positive time trend on the mean level
throughout the summer months from June to Sept until spikes happen around some time points
in the fall. The positive time trend could be explained by the fluctuation of temperature, which is
negatively associated with the COVID-19 mortality rate (Quilodran et al., 2021).
|     |     | Plymouth |     | Berkshire |     | Barnstable |     | Norfolk |     |
| --- | --- | -------- | --- | --------- | --- | ---------- | --- | ------- | --- |
1000
500
0
|     |                           | Bristol |     | Suffolk |     | Franklin |     | Hampshire |     |
| --- | ------------------------- | ------- | --- | ------- | --- | -------- | --- | --------- | --- |
|     | tnuoc esac demrifnoC 1000 |         |     |         |     |          |     |           |     |
500
0
|     |     | Essex |     | Hampden |     | Dukes and Nantucket |     | Middlesex |     |
| --- | --- | ----- | --- | ------- | --- | ------------------- | --- | --------- | --- |
1000
500
0
|     |     |     | Jul | Oct | Jan | Jul Oct | Jan Jul | Oct | Jan |
| --- | --- | --- | --- | --- | --- | ------- | ------- | --- | --- |
Worcester
1000
500
0
|     | Jul | Oct | Jan |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Day
Figure 26: COVID-19 daily case count in different counties in Massachusetts from the dashboard
The spatio-temporal pattern of the count data can be verified through empirical data analysis.
Forthearealtypeofspatialdata,therearetwostandardstatisticstomeasurethespatialcorrelation,
Moran’s I and Geary’s C (Banerjee et al., 2003) which take the forms as shown in equations (2.1)
and (2.2) respectively,
| 2⌊·⌉ denotes | rounding | to the | nearest integer. |     |     |     |     |     |     |
| ------------ | -------- | ------ | ---------------- | --- | --- | --- | --- | --- | --- |
118

|               |         |           | n (cid:80) (cid:80) | w (Y −Y¯)(Y       | −Y¯)  |     |        |
| ------------- | ------- | --------- | ------------------- | ----------------- | ----- | --- | ------ |
|               |         |           |                     | ij i              | j     |     |        |
|               |         | I         | = i                 | j                 | ,     |     | (4.14) |
|               |         |           | (cid:16)            | (cid:17)          |       |     |        |
|               |         |           | (cid:80)            | w (cid:80) (Y     | −Y¯)  |     |        |
|               |         |           |                     | ij                | i     |     |        |
|               |         |           |                     | i̸=j i            |       |     |        |
| while Geary’s | C takes | the form, |                     |                   |       |     |        |
|               |         |           |                     | (cid:80) (cid:80) |       |     |        |
|               |         |           | (n−1)               | w (Y              | −Y )2 |     |        |
|               |         |           |                     | i j ij            | i j   |     |        |
|               |         | C         | = (cid:16)          | (cid:17)          | ,     |     | (4.15) |
|               |         |           | (cid:80)            | (cid:80)          | −Y¯)2 |     |        |
|               |         |           | 2                   | w (Y              |       |     |        |
|               |         |           |                     | i̸=j ij i         | i     |     |        |
wherew ij aretheentriesoftheadjacencymatrixW. WecomputedMoran’sIandGeary’sCaswell
astheirp-valuesthroughoutall200daysusingmoran.test() andgeary.test() fromthespdep package
in R. Figure 27 shows that among the spatial data from 200 days, 95% of Moran’s statistics and
92.5% of Geary’s statistics have a p-value less than the default significance level 0.05. Therefore,
it is reasonable to account for the spatial association among the count data in a statistical model.
0.6
Tests
seulav p
0.4
Geary's C
Moran' I
0.2
0.0
|     | Jul |     |     | Oct |     | Jan |     |
| --- | --- | --- | --- | --- | --- | --- | --- |
Day
Figure27: P-valuesofMoran’sIandGeary’sCateverytimestamp. Thereddashedlinerepresents
| the significance | level of 0.05. |     |     |     |     |     |     |
| ---------------- | -------------- | --- | --- | --- | --- | --- | --- |
Figure 28 shows the estimates of the Autocorrelation Function (ACF) and Partial Autocorrela-
tion Function (PACF) across different regions. The red dashed line represents the 95% boundaries
for the correlation functions. Based on the sample estimates, both types of correlation functions
indicate a significant temporal dependence in the case data. Therefore, The temporal dependence
119

among lagged data is also important to be incorporated for the multivariate time series data.
|     | 1 2  | 3   | 4    | 1 2 | 3 4 |
| --- | ---- | --- | ---- | --- | --- |
|     | 1.00 |     | 0.9  |     |     |
|     | 0.75 |     | 0.6  |     |     |
|     | 0.50 |     | 0.3  |     |     |
|     | 0.25 |     | 0.0  |     |     |
|     | 0.00 |     | −0.3 |     |     |
|     | 5 6  | 7   | 8    | 5 6 | 7 8 |
|     | 1.00 |     | 0.9  |     |     |
|     | 0.75 |     | 0.6  |     |     |
0.50
0.3
|     | 0.25       |          | 0.0     |            |                  |
| --- | ---------- | -------- | ------- | ---------- | ---------------- |
|     | 0.00       |          | −0.3    |            |                  |
| FCA |            |          | FCAP    |            |                  |
|     | 9 10       | 11       | 12      | 9 10       | 11 12            |
|     | 1.00       |          | 0.9     |            |                  |
|     | 0.75       |          | 0.6     |            |                  |
|     | 0.50       |          | 0.3     |            |                  |
|     | 0.25       |          | 0.0     |            |                  |
|     | 0.00       |          | −0.3    |            |                  |
|     | 0 51015200 | 51015200 | 5101520 | 0 51015200 | 51015200 5101520 |
|     | 13         |          |         | 13         |                  |
1.00
0.9
|     | 0.75      |      | 0.6  |           |     |
| --- | --------- | ---- | ---- | --------- | --- |
|     | 0.50      |      | 0.3  |           |     |
|     | 0.25      |      | 0.0  |           |     |
|     | 0.00      |      | −0.3 |           |     |
|     | 0 5101520 |      |      | 0 5101520 |     |
|     |           | Lags |      | Lags      |     |
Figure 28: ACF and PACF estimates for different counties in Massachusetts. Spatial IDs 1∼13
correspond to the following counties in order: Plymouth, Berkshire, Barnstable, Norfolk, Bristol,
Suffolk, Franklin, Hampshire, Essex, Hampden, Dukes and Nantucket, Middlesex, and Worcester.
The red dashed lines represent the boundaries of a 95% confidence interval for ACF and PACF.
4.4.2.2 Implementation of BOSTON-PUPA For the implementation of BOSTON-PUPA
on the real data, we adopted the findings from the simulation study by choosing the sliding window
size T = 28 and discounting factor a = 0.25. We chose HMP and CCT methods in Step 4 to
0
compute combined p-values. The first iteration of model fitting starts on 06/15/2020 (Day 1) and
the first binary outbreak detection indicator on 07/13/2020 (Day 29) for all the counties. Figure
29 shows the calculated outbreak detection indicators in (4.11) in the iterative procedure. Table
21 summarizes the earliest outbreak detection days τˆ for each county. The results are very similar
s
| between HMP | and CCT methods | except | for Suffolk County. |     |     |
| ----------- | --------------- | ------ | ------------------- | --- | --- |
Asareference,thenewsreportofasharpcasecountincreasewasreleasedon10/22/2020,which
corresponds to τ = 130 in the data. To assess the credibility of τˆ , we also provided trace plots of
s
daily case counts with both τˆ and τ in Figure 30, and the plots were separated by population size
s
to avoid imbalanced observation scales. In Figure 30, the BOSTON-PUPA procedure detected the
anomalous counts in counties with large populations such as Bristol, Suffolk, Essex, and Middlesex
120

| Plymouth | Berkshire |     | Barnstable | Norfolk |
| -------- | --------- | --- | ---------- | ------- |
1.00
0.75
0.50
0.25
0.00
| Bristol | Suffolk |     | Franklin | Hampshire |
| ------- | ------- | --- | -------- | --------- |
rotacidni noitceted kaerbtuO 1.00
0.75
0.50
0.25
Method
0.00
HMP
| Essex | Hampden |     | Dukes and Nantucket | Middlesex |
| ----- | ------- | --- | ------------------- | --------- |
1.00 CCT
0.75
0.50
0.25
0.00
|     | 50 100 | 150 200 | 50 100 150 200 | 50 100 150 200 |
| --- | ------ | ------- | -------------- | -------------- |
Worcester
1.00
0.75
0.50
0.25
0.00
| 50 100 150 | 200 |     |     |     |
| ---------- | --- | --- | --- | --- |
Day
Figure29: Calculated outbreakdetection indicatorsδ usingHMP andCCT acrossall counties
s,T+k
in the BOSTON-PUPA procedure.
|            |            |           | Earliest | detection days |
| ---------- | ---------- | --------- | -------- | -------------- |
| Spatial ID | County     | name      | HMP      | CCT            |
| 1          | Plymouth   |           | 130      | 130            |
| 2          | Berkshire  |           | 149      | 149            |
| 3          | Barnstable |           | 82       | 82             |
| 4          | Norfolk    |           | 145      | 145            |
| 5          | Bristol    |           | 82       | 82             |
| 6          | Suffolk    |           | 82       | 172            |
| 7          | Franklin   |           | 186      | 181            |
| 8          | Hampshire  |           | 152      | 152            |
| 9          | Essex      |           | 97       | 97             |
| 10         | Hampden    |           | 130      | 130            |
| 11         | Dukes and  | Nantucket | 152      | 147            |
| 12         | Middlesex  |           | 109      | 109            |
| 13         | Worcester  |           | 132      | 132            |
Table 21: Earliest detection days across different counties using HMP and CCT method.
several weeks before the day of the reported outbreak with the HMP method, while CCT method
reported another significant spike after τ as the detected outbreak. The anomalous escalation of
case counts in Plymouth, Norfolk, Hampden, and Worcester was captured right at or near the time
ofthereportedoutbreak. Asforthecountieswithsmallpopulations, Berkshire, Hampshire, Dukes,
121

and Nantucket had the detected outbreaks of about 2 ∼ 4 weeks later than τ = 130. Meanwhile,
Barnstable and Franklin had an early and a more delayed detection correspondingly.
4.4.2.3 Remarks There is no ground truth available about the exact outbreak timing even
though a news report may be chosen as a reference for the state-wise declared outbreak. However,
one important takeaway from this real application is that instead of making an outbreak claim
based on the entire state, public health surveillance systems can account for the spatio-temporal
pattern of case count in each county and monitor the online data spatially. From this perspective,
the BOTSON-PUPA procedure enjoys an improvement in the granularity and timeliness of disease
surveillance. A detected outbreak in one of the counties can stimulate further investigation for the
suspiciousoutbreakpatternbeforetheonsetofarealpandemic. Thiscanhelppublichealthofficials
customize region-specific strategies to combat the pandemic, protect people at risk, and preserve
normalsocietalfunctionsintheregionswhichhavenotbeenimpactedbythediseaseoutbreakfrom
elsewhere. In addition, we also would like to point out that the BOSTON-PUPA procedure only
handles the anomalous data dynamics from the presumed baseline pattern. Nonetheless, statistical
significance cannot determine the final policy decision if the statistically detected outbreak does
not align with domain knowledge such as epidemiology, public health, etc.
4.5 Summary
In this chapter, we proposed a 4-step online outbreak detection framework, BOSTON-PUPA. This
iterative procedure accounts for spatio-temporal data dependence and overdispersion via a gener-
alized Poisson distribution model. Prior Updating (PU) technique ensures good-quality statistical
inferencedrawnfromafixed-sizeslidingwindowbyleveraginghistoricalinformation. P-valueAdap-
tation (PA) technique is able to boost the significance of a true outbreak thus leading to timely on-
line outbreak detection. The global aberration indicator, stemming from the sequential estimation
oftheoverdispersion,providesreliableoutbreaksurveillanceforallinvolvedlocationsandfacilitates
a strict false detection control locally. Implementation of combined p-values in sequential analysis
enables (1) Better information preservation about outbreak severity than dichotomized detection
strategies solely based on upper boundaries for data prediction. (2) Dependence among individual
p-values, whereas residual-combining approaches are often under the assumption of residuals being
122

| 2   | 3   | 7   | 1   | 4   | 5   |
| --- | --- | --- | --- | --- | --- |
150
1000
| )noitalupop llams( tnuoc esac demrifnoC |     | )noitalupop egral( tnuoc esac demrifnoC |     |     |     |
| --------------------------------------- | --- | --------------------------------------- | --- | --- | --- |
| 100                                     |     | 500                                     |     |     |     |
0
50
|     |     |      | 6   | 9   | 10  |
| --- | --- | ---- | --- | --- | --- |
| 0   |     | 1000 |     |     |     |
50 100 150 200
| 8   | 11  |     |     |     |     |
| --- | --- | --- | --- | --- | --- |
500
150
0
50 100 150 200
|     |     |     | 12  | 13  |     |
| --- | --- | --- | --- | --- | --- |
100
1000
50
500
| 0          |                    |            | 0          |                    |     |
| ---------- | ------------------ | ---------- | ---------- | ------------------ | --- |
| 50 100 150 | 200 50 100 150 200 |            | 50 100 150 | 200 50 100 150 200 |     |
|            | Day                |            |            | Day                |     |
|            |                    | Method HMP | CCT        |                    |     |
Figure 30: Trace plot of daily COVID-19 case counts in MA, 2020, with detected outbreaks using
BOSTON-PUPA procedure. Red line represents a state-wise outbreak indicator from the news
independent or uncorrelated. As a holistic framework, the BOSTON-PUPA procedure is able to
perform robust outbreak detection of the count data against different signal-to-noise ratios on spa-
tially imbalanced scales. In addition, the inherent computational efficiency of the INLA method
grants practitioners the flexibility to straightforwardly implement the BOSTON-PUPA procedure
for real application and to conduct relevant research via large-scale simulations.
123

5 Discussion and Future Work
This dissertation contributes new methodological developments in online change point detection
and spatio-temporal analysis. Chapter 2 and 3 focus on the innovative statistical methods with
applications for high-frequency financial market microstructure analysis. E-PEF method from
Chapter2aimsatrobustlydetectingstructuralbreaksinfinancialdurationtimeserieswithafixed-
size of training data via a semi-parametric detection algorithm, and detected structural breaks can
inform the practitioners the change of market trading intensity so that corresponding transactional
strategies can be deployed promptly to adjust for an advantageous asset position. BVAR(1)-LCM
BayesianhierarchicalmodelfromChapter3accountsfortheassociationbetweentransactioncounts
at different risk levels across multiple assets. The data interdependence on the observational level
can be further elaborated via correlated latent random effects. Specified Gaussian Markov Random
Field with sparsity enables fast parametric inference via INLA method thus leading to scaled-
up analyses for a large number of assets in a single model. By synthesizing relevant techniques
involved in univariate online change point detection and multivariate count time series modeling,
BOSTON-PUPA procedure from Chapter 4 took a further step to deal with spatio-temporal online
outbreakdetectionproblemsinpublichealthsurveillance. Thisiterativedetectionprocedureenjoys
fast computational speed with fundamental historical information retaining via Prior Updating
(PU) technique. Meabwhile, streaming surveillance data are monitored by a global and location
aberration indicators with P-value Adaptation (PA) technique, which enforces a satisfactory false
detection control and provide timeliness and granularity for the powerful disease surveillance over
multiple geographically related locations even if there is a data imbalance issue with the count
observations.
As future work based on the three proposed frameworks, three potential directions are worth
extended research attention.
• First, as a univariate online structural break detection procedure, the E-PEF method is
able to achieve a single structural break detection given a fixed amount of training data.
However, in the volatile high-frequency financial market, a fixed amount of data doesn’t
provideasustainablerepresentationofthebaselinepatternforchangepointdetectionthusthe
monitoring horizon is limited and monitoring longer time series requires updates of training
124

data. In order to develop a multiple structural break detection framework, one needs to
study the monitoring horizon of the E-PEF method to ensure a controlled false detection rate
in a monitoring window of reasonable length. Subsequently, a clock resetting regimen can
be introduced to recursively update the latest training data to capture the recent baseline
pattern when (1) The incoming observations are beyond the monitoring horizon, or (2) A
structural break is detected within the monitoring horizon.
• Second, BOSTON-PUPA procedure involves a sliding window as a baseline pattern without
the concern about monitoring horizon for online outbreak detection, but for its multiple
change point detection, a resetting rule is also very helpful because of the findings of the
sequential estimation for the overdispersion parameter for generalized Poisson distribution.
Thesequentialestimationoftheoverdispersionisstationarywhentheslidingwindowcontains
only non-epidemic or epidemic data, so that changes over the trajectory of the overdispersion
parameter estimates can be good indicators when the procedure enters a transition stage
between two phases. Therefore, the resetting rule can be placed over the baseline behavior of
thesequentialoverdispersionestimationwhentheestimatebeginstodeviatefromitsbaseline
pattern. With appropriately specified p-value calculation, BOSTON-PUPA procedure with
a resetting rule will have promising performance to detect not only the onset of a pandemic
but also its sign of ending.
• Third, BVAR(1)-LCM framework is involved in financial application but the main idea is
based on the correct specification of precision matrix for the random effects with convoluted
association and numerous future research can be considered when an innovative data inter-
dependent structure is developed. By taking advantage of computational efficiency, one can
use the INLA method to make high-quality inference on the parameters and latent effects
from sparse Gaussian Markov Random Field as long as their precision matrix is reasonably
formulated. For example, the spatio-temporal framework in BOSTON-PUPA involve naive
separable spatial and temporal effects also with a symmetric adjacency matrix establishing
an equal influence between two neighboring regions. To demonstrate and model more com-
plex space and time association, one can consider a non-separable spatio-temporal effects
as in (Zou et al., 2012) and an asymmetrically weighted spatial-dependence matrix as in a
125

| Simultaneous |     | Auto-regressive | (SAR) model | in (Arab | et al., 2008). |
| ------------ | --- | --------------- | ----------- | -------- | -------------- |
References
C. C. Aggarwal. An introduction to outlier analysis. In Outlier Analysis, pages 1–34. Springer,
2017.
J. Aitchison and C. Ho. The multivariate Poisson-log normal distribution. Biometrika, 76(4):
| 643–653, | 1989. |     |     |     |     |
| -------- | ----- | --- | --- | --- | --- |
T. Aktekin, N. Polson, and R. Soyer. Sequential Bayesian analysis of multivariate count data.
| Bayesian | Analysis, | 13(2):385–409, | 2018. |     |     |
| -------- | --------- | -------------- | ----- | --- | --- |
M. A. Al-Osh and A. A. Alzaid. First-order integer-valued autoregressive (INAR (1)) process.
| Journal | of Time | Series Analysis, | 8(3):261–275, | 1987. |     |
| ------- | ------- | ---------------- | ------------- | ----- | --- |
D. Allen, F. Chan, M. McAleer, and S. Peiris. Finite sample properties of the QMLE for the
Log-ACD model: application to Australian stocks. Journal of Econometrics, 147(1):163–185,
2008.
A. Alzaid and M. Al-Osh. First-order integer-valued autoregressive (INAR (1)) process: distribu-
tional and regression properties. Statistica Neerlandica, 42(1):53–61, 1988.
I. B. Ammar, S. Hellara, and I. Ghadhab. High-frequency trading and stock liquidity: An intraday
analysis. Research in International Business and Finance, 53:101235, 2020.
C. Anderson, D. Lee, and N. Dean. Spatial clustering of average risks and risk trends in bayesian
| disease | mapping. | Biometrical | Journal, 59(1):41–56, | 2017. |     |
| ------- | -------- | ----------- | --------------------- | ----- | --- |
A. Arab, M. B. Hooten, and C. K. Wikle. Hierarchical spatial models. Encyclopedia of GIS, 14(1):
| 425–431, | 2008. |     |     |     |     |
| -------- | ----- | --- | --- | --- | --- |
A. Aue, S. H¨ormann, L. Horv´ath, and M. Reimherr. Break detection in the covariance structure
of multivariate time series models. The Annals of Statistics, 37(6B):4046–4087, 2009.
J. Bai. Likelihood ratio tests for multiple structural changes. Journal of Econometrics, 91(2):
| 299–323, | 1999. |     |     |     |     |
| -------- | ----- | --- | --- | --- | --- |
126

A. Banerjee and G. Urga. Modelling structural breaks, long memory and stock market volatility:
| an overview. |     | Journal | of Econometrics, |     | 129(1-2):1–34, |     | 2005. |     |     |
| ------------ | --- | ------- | ---------------- | --- | -------------- | --- | ----- | --- | --- |
S. Banerjee, B. P. Carlin, and A. E. Gelfand. Hierarchical modeling and analysis for spatial data.
| Chapman | and | Hall/CRC, | 2003. |     |     |     |     |     |     |
| ------- | --- | --------- | ----- | --- | --- | --- | --- | --- | --- |
M.Baron,J.Brogaard,B.Hagstr¨omer,andA.Kirilenko. Riskandreturninhigh-frequencytrading.
| Journal | of Financial |     | and Quantitative |     | Analysis, | 54(3):993–1024, |     |     | 2019. |
| ------- | ------------ | --- | ---------------- | --- | --------- | --------------- | --- | --- | ----- |
L. Bauwens and P. Giot. The logarithmic ACD model: an application to the bid-ask quote process
of three nyse stocks. Annales d’Economie et de Statistique, pages 117–149, 2000.
L. Bauwens and D. Veredas. The stochastic conditional duration model: a latent variable model
for the analysis of financial durations. Journal of Econometrics, 119(2):381–412, 2004.
B. Bedowska-S´ojka and A. Kliber. The causality between liquidity and volatility in the polish stock
| market. | Finance | Research | Letters, |     | 30:110–115, | 2019. |     |     |     |
| ------- | ------- | -------- | -------- | --- | ----------- | ----- | --- | --- | --- |
A. Benveniste, M. Basseville, and G. Moustakides. The asymptotic local approach to change
detection and model validation. IEEE Transactions on Automatic Control, 32(7):583–592, 1987.
A. Benveniste, M. M´etivier, and P. Priouret. Adaptive Algorithms and Stochastic Approximations,
| volume | 22. | Springer | Science | & Business | Media, | 2012. |     |     |     |
| ------ | --- | -------- | ------- | ---------- | ------ | ----- | --- | --- | --- |
M. Beraha, D. Falco, and A. Guglielmi. JAGS, NIMBLE, Stan: a detailed comparison among
| bayesian | mcmc | software. | arXiv | preprint | arXiv:2107.09357, |     |     | 2021. |     |
| -------- | ---- | --------- | ----- | -------- | ----------------- | --- | --- | ----- | --- |
I. Berkes, E. Gombay, L. Horv´ath, and P. Kokoszka. Sequential change-point detection in GARCH
| (p, q) | models. | Econometric |     | Theory, | 20(6):1140–1167, |     | 2004. |     |     |
| ------ | ------- | ----------- | --- | ------- | ---------------- | --- | ----- | --- | --- |
J. Besag. Spatial interaction and the statistical analysis of lattice systems. Journal of the Royal
| Statistical | Society: | Series | B   | (Methodological), |     | 36(2):192–225, |     |     | 1974. |
| ----------- | -------- | ------ | --- | ----------------- | --- | -------------- | --- | --- | ----- |
J. Besag, J. York, and A. Molli´e. Bayesian image restoration, with two applications in spatial
statistics. Annals of the Institute of Statistical Mathematics, 43(1):1–20, 1991.
127

D. M. Blei, A. Kucukelbir, and J. D. McAuliffe. Variational inference: A review for statisticians.
Journal of the American Statistical Association, 112(518):859–877, 2017. doi: 10.1080/01621459.
2017.1285773.
G. E. Box, G. M. Jenkins, G. C. Reinsel, and G. M. Ljung. Time Series Analysis: Forecasting and
| Control. | John | Wiley | & Sons, | 2015. |     |     |     |
| -------- | ---- | ----- | ------- | ----- | --- | --- | --- |
J. Brogaard, A. Carrion, T. Moyaert, R. Riordan, A. Shkilko, and K. Sokolov. High frequency
trading and extreme price movements. Journal of Financial Economics, 128(2):253–265, 2018.
M. B. Brown. 400: A method for combining non-independent, one-sided tests of significance.
| Biometrics, |     | pages | 987–992, | 1975. |     |     |     |
| ----------- | --- | ----- | -------- | ----- | --- | --- | --- |
P. Bu¨hlmann. Bootstraps for time series. Statistical Science, pages 52–72, 2002.
H.S.Burkom,S.P.Murphy,andG.Shmueli. Automatedtimeseriesforecastingforbiosurveillance.
| Statistics | in  | Medicine, | 26(22):4202–4218, |     | 2007. |     |     |
| ---------- | --- | --------- | ----------------- | --- | ----- | --- | --- |
A. Carrion. Very fast money: High-frequency trading on the NASDAQ. Journal of Financial
| Markets, | 16(4):680–711, |     | 2013. |     |     |     |     |
| -------- | -------------- | --- | ----- | --- | --- | --- | --- |
J. M. Cheverud. A simple correction for multiple comparisons in interval mapping genome scans.
| Heredity, | 87(1):52–58, |     | 2001. |     |     |     |     |
| --------- | ------------ | --- | ----- | --- | --- | --- | --- |
C.-S.J.Chu,M.Stinchcombe,andH.White. Monitoringstructuralchange. Econometrica: Journal
| of the | Econometric |     | Society, | pages 1045–1065, |     | 1996. |     |
| ------ | ----------- | --- | -------- | ---------------- | --- | ----- | --- |
O. Cinar and W. Viechtbauer. The poolr package for combining independent and dependent p
| values. | Journal | of  | Statistical | Software, | 101:1–42, | 2022. |     |
| ------- | ------- | --- | ----------- | --------- | --------- | ----- | --- |
D. Conesa, M. Mart´ınez-Beneito, R. Amor´os, and A. L´opez-Qu´ılez. Bayesian hierarchical pois-
son models with a hidden markov structure for the detection of influenza epidemic outbreaks.
| Statistical | Methods |     | in Medical | Research, | 24(2):206–223, |     | 2015. |
| ----------- | ------- | --- | ---------- | --------- | -------------- | --- | ----- |
P. C. Consul and G. C. Jain. A generalization of the poisson distribution. Technometrics, 15(4):
| 791–799, | 1973. |     |     |     |     |     |     |
| -------- | ----- | --- | --- | --- | --- | --- | --- |
128

G.F.Cooper, R.Villamarin, F.-C.R.Tsui, N.Millett, J.U.Espino, andM.M.Wagner. Amethod
for detecting and characterizing outbreaks of infectious disease from clinical reports. Journal of
| Biomedical | Informatics, |     | 53:15–26, 2015. |     |     |
| ---------- | ------------ | --- | --------------- | --- | --- |
S. S. Coughlin, A. Yiˇgiter, H. Xu, A. E. Berman, and J. Chen. Early detection of change patterns
inCOVID-19incidenceandtheimplementationofpublichealthpolicies: Amulti-nationalstudy.
| Public | Health in | Practice, | 2:100064, 2021. |     |     |
| ------ | --------- | --------- | --------------- | --- | --- |
R. Deo, M. Hsieh, and C. M. Hurvich. Long memory in intertrade durations, counts and realized
volatility of nyse stocks. Journal of Statistical Planning and Inference, 140(12):3715–3733, 2010.
P. Deuskar. Extrapolative expectations: Implications for volatility and liquidity. In AFA 2007
| Chicago | Meetings | Paper, | 2006. |     |     |
| ------- | -------- | ------ | ----- | --- | --- |
P.Diggle,L.Knorr-Held,B.Rowlingson,T.L.Su,P.Hawtin,andT.N.Bryant. On-linemonitoring
of public health surveillance data. In Monitoring the health of populations: Statistical principles
and methods for public health surveillance. Oxford University Press, 2009.
E. Dong, H. Du, and L. Gardner. An interactive web-based dashboard to track covid-19 in real
| time. The | Lancet | Infectious | Diseases, | 20(5):533–534, | 2020. |
| --------- | ------ | ---------- | --------- | -------------- | ----- |
M. D¨oring. Convergence in distribution of multiple change point estimators. Journal of Statistical
| Planning | and Inference, |     | 141(7):2238–2248, | 2011. |     |
| -------- | -------------- | --- | ----------------- | ----- | --- |
F. Dudbridge and B. P. Koeleman. Efficient computation of significance levels for multiple associa-
tionsinlargestudiesofcorrelateddata, includinggenomewideassociationstudies. The American
| Journal | of Human | Genetics, | 75(3):424–435, | 2004. |     |
| ------- | -------- | --------- | -------------- | ----- | --- |
C.Dutta, K.Karpman, S.Basu, andN.Ravishanker. Reviewofstatisticalapproachesformodeling
| high-frequency | trading | data. | Sankhya | B, pages | 1–48, 2022. |
| -------------- | ------- | ----- | ------- | -------- | ----------- |
D. Easley and M. O’hara. Time and the process of security price adjustment. The Journal of
| Finance, | 47(2):577–605, |     | 1992. |     |     |
| -------- | -------------- | --- | ----- | --- | --- |
B. Efron. Double exponential families and their use in generalized linear regression. Journal of the
| American | Statistical | Association, | 81(395):709–721, |     | 1986. |
| -------- | ----------- | ------------ | ---------------- | --- | ----- |
129

R. F. Engle. The econometrics of ultra-high-frequency data. Econometrica, 68(1):1–22, 2000.
R. F. Engle and J. R. Russell. Forecasting the frequency of changes in quoted foreign exchange
prices with the autoregressive conditional duration model. Journal of Empirical Finance, 4(2-3):
| 187–212, | 1997. |     |     |     |
| -------- | ----- | --- | --- | --- |
R. F. Engle and J. R. Russell. Autoregressive conditional duration: a new model for irregularly
| spaced | transaction | data. Econometrica, | pages 1127–1162, | 1998. |
| ------ | ----------- | ------------------- | ---------------- | ----- |
J. Fan and R. Li. Variable selection via nonconcave penalized likelihood and its oracle properties.
Journal of the American Statistical Association, 96(456):1348–1360, 2001.
C. Farrington, N. J. Andrews, A. Beale, and M. Catchpole. A statistical algorithm for the early
detection of outbreaks of infectious disease. Journal of the Royal Statistical Society: Series A
| (Statistics | in Society), | 159(3):547–563, | 1996. |     |
| ----------- | ------------ | --------------- | ----- | --- |
P. Farrington and N. Andrews. Application to infectious. Monitoring the Health of Populations:
Statistical Principles and Methods for Public Health Surveillance, page 203, 2003.
R. Ferland, A. Latour, and D. Oraichi. Integer-valued GARCH process. Journal of Time Series
| Analysis, | 27(6):923–942, | 2006. |     |     |
| --------- | -------------- | ----- | --- | --- |
M. Fernandes and J. Grammig. A family of autoregressive conditional duration models. Journal
| of Econometrics, | 130(1):1–23, | 2006. |     |     |
| ---------------- | ------------ | ----- | --- | --- |
R. Fisher. Statistical methods for research workers (london: Oliver and boyd). Legends to Figures,
1932.
N. W. Galwey. A new measure of the effective number of tests, a practical tool for comparing
families of non-independent significance tests. Genetic Epidemiology: The Official Publication of
| the International | Genetic | Epidemiology | Society, 33(7):559–568, | 2009. |
| ----------------- | ------- | ------------ | ----------------------- | ----- |
D. Gamerman, T. R. dos Santos, and G. C. Franco. A non-Gaussian family of state-space models
with exact marginal likelihood. Journal of Time Series Analysis, 34(6):625–645, 2013.
130

X. Gao, J. Starmer, and E. R. Martin. A multiple testing correction method for genetic association
studies using correlated single nucleotide polymorphisms. Genetic Epidemiology: The Official
Publication of the International Genetic Epidemiology Society, 32(4):361–369, 2008.
A. E. Gelfand and P. Vounatsou. Proper multivariate conditional autoregressive models for spatial
| data analysis. |     | Biostatistics, | 4(1):11–15, | 2003. |     |     |     |
| -------------- | --- | -------------- | ----------- | ----- | --- | --- | --- |
A. Gelman, J. Hwang, and A. Vehtari. Understanding predictive information criteria for Bayesian
| models.          | Statistics | and Computing, |           | 24(6):997–1016, |     | 2014.      |       |
| ---------------- | ---------- | -------------- | --------- | --------------- | --- | ---------- | ----- |
| V. G´omez-Rubio. |            | Bayesian       | Inference | with INLA.      |     | CRC Press, | 2020. |
P.Good. Permutationtests: apracticalguidetoresamplingmethodsfortestinghypotheses. Springer
| Science | & Business | Media, | 2013. |     |     |     |     |
| ------- | ---------- | ------ | ----- | --- | --- | --- | --- |
J. Grammig and M. Wellner. Modeling the interdependence of volatility and inter-transaction
| duration | processes. | Journal | of  | Econometrics, | 106(2):369–400, |     | 2002. |
| -------- | ---------- | ------- | --- | ------------- | --------------- | --- | ----- |
G. Guan, Y. Dery, M. Yechezkel, I. Ben-Gal, D. Yamin, and M. L. Brandeau. Early detection of
covid-19 outbreaks using human mobility data. PloS one, 16(7):e0253865, 2021.
A. C. Hale, F. S´anchez-Vizca´ıno, B. Rowlingson, A. D. Radford, E. Giorgi, S. J. O’Brien, and P. J.
Diggle. A real-time spatio-temporal syndromic surveillance system with application to small
| companion | animals. | Scientific | reports, | 9(1):1–14, |     | 2019. |     |
| --------- | -------- | ---------- | -------- | ---------- | --- | ----- | --- |
W. K. H¨ardle and L. Simar. Applied Multivariate Statistical Analysis. Springer Nature, 2019.
J. Hasbrouck and G. Saar. Low-latency trading. Journal of Financial Markets, 16(4):646–679,
2013.
S. He, Z. He, and G. A. Wang. CUSUM control charts for multivariate Poisson distribution.
Communications in Statistics-Theory and Methods, 43(6):1192–1208, 2014.
M. J. Heaton, D. L. Banks, J. Zou, A. F. Karr, G. Datta, J. Lynch, and F. Vera. A spatio-temporal
absorbing state model for disease and syndromic surveillance. Statistics in Medicine, 31(19):
| 2123–2136, | 2012. |     |     |     |     |     |     |
| ---------- | ----- | --- | --- | --- | --- | --- | --- |
131

A.Heinen. Modellingtimeseriescountdata: anautoregressiveconditionalPoissonmodel. Available
| at SSRN 1117187, | 2003. |     |     |     |
| ---------------- | ----- | --- | --- | --- |
T. Hendershott and R. Riordan. Algorithmic trading and the market for liquidity. Journal of
| Financial and | Quantitative | Analysis, 48(4):1001–1024, |     | 2013. |
| ------------- | ------------ | -------------------------- | --- | ----- |
C. C. Heyde. Quasi-likelihood and its application: a general approach to optimal parameter esti-
| mation. Springer, | 1997. |     |     |     |
| ----------------- | ----- | --- | --- | --- |
L. Horv´ath and G. Rice. Extensions of some classical methods in change point analysis. Test, 23
| (2):219–255, | 2014. |     |     |     |
| ------------ | ----- | --- | --- | --- |
H. E. Hughes, O. Edeghere, S. J. O’Brien, R. Vivancos, and A. J. Elliot. Emergency department
syndromic surveillance systems: a systematic review. BMC Public Health, 20(1):1–15, 2020.
M. Huˇskov´a, Z. Pr´aˇskov´a, and J. Steinebach. On the detection of changes in autoregressive time
series i. asymptotics. Journal of Statistical Planning and Inference, 137(4):1243–1259, 2007.
P. A. Jacobs and P. A. Lewis. Stationary discrete autoregressive-moving average time series gen-
erated by mixtures. Journal of Time Series Analysis, 4(1):19–36, 1983.
| J. Jasiak. Persistence | in intertrade | durations. | In Finance, | 1999. |
| ---------------------- | ------------- | ---------- | ----------- | ----- |
X. Jin, B. P. Carlin, and S. Banerjee. Generalized hierarchical multivariate car models for areal
| data. Biometrics, | 61(4):950–961, | 2005. |     |     |
| ----------------- | -------------- | ----- | --- | --- |
P. Johnson, J. Moriarty, and G. Peskir. Detecting changes in real-time data: a user’s guide to
optimal detection. Philosophical Transactions of the Royal Society A: Mathematical, Physical
| and Engineering | Sciences, | 375(2100):20160298, | 2017. |     |
| --------------- | --------- | ------------------- | ----- | --- |
R. C. Jung, R. Liesenfeld, and J.-F. Richard. Dynamic factor models for multivariate count data:
An application to stock-market trading activity. Journal of Business & Economic Statistics, 29
| (1):73–85, | 2011. |     |     |     |
| ---------- | ----- | --- | --- | --- |
D.KarlisandL.Meligkotsidou. MultivariatePoissonregressionwithcovariancestructure. Statistics
| and Computing, | 15(4):255–265, | 2005. |     |     |
| -------------- | -------------- | ----- | --- | --- |
132

D. Karlis and L. Meligkotsidou. Finite mixtures of multivariate Poisson distributions with appli-
cation. Journal of Statistical Planning and Inference, 137(6):1942–1960, 2007.
J. T. Kost and M. P. McDermott. Combining dependent p-values. Statistics & Probability Letters,
| 60(2):183–190, | 2002. |     |     |     |
| -------------- | ----- | --- | --- | --- |
M. Kulldorff. A spatial scan statistic. Communications in Statistics-Theory and methods, 26(6):
| 1481–1496, | 1997. |     |     |     |
| ---------- | ----- | --- | --- | --- |
T. L. Lai and J. Z. Shan. Efficient recursive algorithms for detection of abrupt changes in signals
and control systems. IEEE Transactions on Automatic Control, 44(5):952–966, 1999.
H.Lancaster. Thecombinationofprobabilities: anapplicationoforthonormalfunctions. Australian
| Journal | of Statistics, 3(1):20–33, | 1961. |     |     |
| ------- | -------------------------- | ----- | --- | --- |
I. Lavine, A. Cron, and M. West. Bayesian computation in dynamic latent factor models. arXiv
| preprint | arXiv:2007.04956, | 2020. |     |     |
| -------- | ----------------- | ----- | --- | --- |
J. Li and L. Ji. Adjusting multiple testing in multilocus analyses using the eigenvalues of a corre-
| lation matrix. | Heredity, | 95(3):221–227, | 2005. |     |
| -------------- | --------- | -------------- | ----- | --- |
L. Li, K.-L. Tsui, and Y. Zhao. An overview and general framework for spatiotemporal modeling
and applications in transportation and public health. Artificial Intelligence, Big Data and Data
| Science | in Statistics, pages | 195–226, | 2022a. |     |
| ------- | -------------------- | -------- | ------ | --- |
M. Li, S. Ma, and Z. Liu. A novel method to detect the early warning signal of COVID-19
| transmission. | BMC Infectious | Diseases, | 22(1):1–12, | 2022b. |
| ------------- | -------------- | --------- | ----------- | ------ |
Y. Liang, A. Thavaneswaran, and B. Abraham. Joint estimation using quadratic estimating func-
| tion. Journal | of Probability | and Statistics, | 2011, | 2011. |
| ------------- | -------------- | --------------- | ----- | ----- |
R. Liesenfeld, I. Nolte, and W. Pohlmeier. Modelling financial transaction price movements: a
dynamic integer count data model. Empirical Economics, 30(4):795–825, 2006.
Y. Liu and J. Xie. Cauchy combination test: a powerful test with analytic p-value calculation
under arbitrary dependency structures. Journal of the American Statistical Association, 115
| (529):393–402, | 2020. |     |     |     |
| -------------- | ----- | --- | --- | --- |
133

J. Ma, K. M. Kockelman, and P. Damien. A multivariate Poisson-lognormal regression model for
prediction of crash counts by severity, using Bayesian methods. Accident Analysis & Prevention,
| 40(3):964–975, | 2008. |     |     |     |
| -------------- | ----- | --- | --- | --- |
J. Manitz and M. H¨ohle. Bayesian outbreak detection algorithm for monitoring reported cases of
campylobacteriosis in germany. Biometrical Journal, 55(4):509–526, 2013.
M. A. Mart´ınez-Beneito, D. Conesa, A. L´opez-Qu´ılez, and A. L´opez-Maside. Bayesian markov
switching models for the early detection of influenza epidemics. Statistics in Medicine, 27(22):
| 4455–4468, | 2008. |     |     |     |
| ---------- | ----- | --- | --- | --- |
C. Mikl´os and H. Lajos. Limit theorems in change-point analysis. John Wiley and Sons, 1997.
D. C. Montgomery. Introduction to statistical quality control. John Wiley & Sons, 2020.
D.B.Neill.FastBayesianscanstatisticsformultivariateeventdetectionandvisualization.Statistics
| in Medicine, | 30(5):455–469, | 2011. |     |     |
| ------------ | -------------- | ----- | --- | --- |
D.R.Nyholt. Asimplecorrectionformultipletestingforsingle-nucleotidepolymorphismsinlinkage
disequilibrium with each other. The American Journal of Human Genetics, 74(4):765–769, 2004.
| M. O’hara. | Market microstructure | theory. | John Wiley & | Sons, 1998. |
| ---------- | --------------------- | ------- | ------------ | ----------- |
M. Pacurar. Autoregressive conditional duration models in finance: a survey of the theoretical and
empirical literature. Journal of Economic Surveys, 22(4):711–751, 2008.
E. Page. A test for a change in a parameter occurring at an unknown point. Biometrika, 42(3/4):
| 523–527, | 1955. |     |     |     |
| -------- | ----- | --- | --- | --- |
E. S. Page. Continuous inspection schemes. Biometrika, 41(1/2):100–115, 1954.
E.S.ParkandD.Lord. MultivariatePoisson-lognormalmodelsforjointlymodelingcrashfrequency
| by severity. | Transportation | Research Record, | 2019(1):1–6, | 2007. |
| ------------ | -------------- | ---------------- | ------------ | ----- |
X. Pedeli and D. Karlis. On estimation of the bivariate Poisson INAR process. Communications
| in Statistics-Simulation |     | and Computation, | 42(3):514–533, | 2013. |
| ------------------------ | --- | ---------------- | -------------- | ----- |
134

D. N. Politis. The impact of bootstrap methods on time series analysis. Statistical Science, pages
| 219–230, | 2003. |     |     |     |     |
| -------- | ----- | --- | --- | --- | --- |
D. N. Politis and J. P. Romano. The stationary bootstrap. Journal of the American Statistical
| Association, | 89(428):1303–1313, |     | 1994. |     |     |
| ------------ | ------------------ | --- | ----- | --- | --- |
C. S. Quilodran, M. Currat, and J. I. Montoya-Burgos. Air temperature influences early covid-19
outbreak as indicated by worldwide mortality. Science of The Total Environment, 792:148312,
2021.
A. S. Quoreshi. A bivariate integer-valued long-memory model for high-frequency financial count
data. Communications in Statistics-Theory and Methods, 46(3):1080–1089, 2017.
S. T. Radev, F. Graw, S. Chen, N. T. Mutters, V. M. Eichel, T. B¨arnighausen, and U. K¨othe.
Outbreakflow: Model-based Bayesian inference of disease outbreak dynamics with invertible
neuralnetworksanditsapplicationtotheCOVID-19pandemicsingermany.PLoSComputational
| Biology, | 17(10):e1009472, | 2021. |     |     |     |
| -------- | ---------------- | ----- | --- | --- | --- |
B.Raman,N.Ravishanker,R.Soyer,V.Gorti,andK.Sen. DynamicBayesianmodelingofmultiple
count time series using R-INLA. Journal of the Indian Statistical Association, 58(2):137–173,
2020.
N. Ravishanker, V. Serhiyenko, and M. R. Willig. Hierarchical dynamic models for multivariate
| times series | of counts. | Statistics | and its Interface, | 7(4):559–570, | 2014. |
| ------------ | ---------- | ---------- | ------------------ | ------------- | ----- |
A.RieblerandL.Held.Projectingthefutureburdenofcancer: Bayesianage–period–cohortanalysis
with integrated nested Laplace approximations. Biometrical Journal, 59(3):531–549, 2017.
M. W. Robbins, C. M. Gallagher, and R. B. Lund. A general regression changepoint test for time
series data. Journal of the American Statistical Association, 111(514):670–683, 2016.
G. Rossi, L. Lampugnani, and M. Marchi. An approximate cusum procedure for surveillance of
| health events. | Statistics | in Medicine, | 18(16):2111–2122, | 1999. |     |
| -------------- | ---------- | ------------ | ----------------- | ----- | --- |
H. Rue and L. Held. Gaussian Markov random fields: theory and applications. Chapman and
| Hall/CRC, | 2005. |     |     |     |     |
| --------- | ----- | --- | --- | --- | --- |
135

H. Rue, S. Martino, and N. Chopin. Approximate Bayesianinference for latent Gaussianmodels by
using integrated nested Laplace approximations. Journal of the Royal Statistical Society: Series
| B (Statistical | Methodology), |     |     | 71(2):319–392, | 2009. |     |     |
| -------------- | ------------- | --- | --- | -------------- | ----- | --- | --- |
H. Rue, A. Riebler, S. H. Sørbye, J. B. Illian, D. P. Simpson, and F. K. Lindgren. Bayesian
computing with INLA: a review. Annual Review of Statistics and Its Application, 4:395–421,
2017.
R. Ruiz-C´ardenas, E. T. Krainski, and H. Rue. Direct fitting of dynamic models using integrated
nested Laplace approximations—INLA. Computational Statistics & Data Analysis, 56(6):1808–
1828, 2012.
D. Sadykova, B. E. Scott, M. De Dominicis, S. L. Wakelin, A. Sadykov, and J. Wolf. Bayesian
joint models with INLA exploring marine mobile predator–prey and competitor species habitat
| overlap. | Ecology | and Evolution, |     | 7(14):5212–5226, |     | 2017. |     |
| -------- | ------- | -------------- | --- | ---------------- | --- | ----- | --- |
M. Salmon, D. Schumacher, K. Stark, and M. H¨ohle. Bayesian outbreak detection in the presence
| of reporting | delays. | Biometrical |     | Journal, | 57(6):1051–1067, |     | 2015. |
| ------------ | ------- | ----------- | --- | -------- | ---------------- | --- | ----- |
D. Salyakina, S. R. Seaman, B. L. Browning, F. Dudbridge, and B. Mu¨ller-Myhsok. Evaluation of
nyholt’s procedure for multiple testing correction. Human Heredity, 60(1):19–25, 2005.
M. Saqib. Forecasting covid-19 outbreak progression using hybrid polynomial-bayesian ridge re-
| gression | model. | Applied | Intelligence, | 51(5):2703–2713, |     | 2021. |     |
| -------- | ------ | ------- | ------------- | ---------------- | --- | ----- | --- |
B. Schr¨odle and L. Held. Spatio-temporal disease mapping using INLA. Environmetrics, 22(6):
| 725–734, | 2011. |     |     |     |     |     |     |
| -------- | ----- | --- | --- | --- | --- | --- | --- |
R.E.Serfling. Methodsforcurrentstatisticalanalysisofexcesspneumonia-influenzadeaths. Public
| Health Reports, |     | 78(6):494, | 1963. |     |     |     |     |
| --------------- | --- | ---------- | ----- | --- | --- | --- | --- |
V. Serhiyenko, N. Ravishanker, and R. Venkatesan. Multi-stage multivariate modeling of temporal
patterns in prescription counts for competing drugs in a therapeutic category. Applied Stochastic
| Models in       | Business | and | Industry,  | 34(1):61–78,    |     | 2018.    |       |
| --------------- | -------- | --- | ---------- | --------------- | --- | -------- | ----- |
| W. A. Shewhart. | Control  |     | of quality | of manufactured |     | product. | 1929. |
136

H. Shore. General control charts for variables. International Journal of Production Research, 38
| (8):1875–1897, | 2000. |     |     |
| -------------- | ----- | --- | --- |
R. Soyer and D. Zhang. Bayesian modeling of multivariate time series of counts. Wiley Interdisci-
| plinary Reviews: | Computational | Statistics, | page e1559, 2021. |
| ---------------- | ------------- | ----------- | ----------------- |
S. A. Stouffer, E. A. Suchman, L. C. DeVinney, S. A. Star, and R. M. Williams Jr. The American
soldier: Adjustment during army life.(studies in social psychology in World War II), vol. 1. 1949.
A. Thavaneswaran, N. Ravishanker, and Y. Liang. Generalized duration models and optimal
estimation using estimating functions. Annals of the Institute of Statistical Mathematics, 67(1):
| 129–156, 2015. |     |     |     |
| -------------- | --- | --- | --- |
K.-L. Tsui, W. Chiu, P. Gierlich, D. Goldsman, X. Liu, and T. Maschek. A review of healthcare,
public health, and syndromic surveillance. Quality Engineering, 20(4):435–450, 2008.
A. W. Van der Vaart. Asymptotic statistics, volume 3. Cambridge University Press, 2000.
A. Wald. Foundations of a general theory of sequential decision functions. Econometrica, Journal
| of the Econometric | Society, pages | 279–313, | 1947. |
| ------------------ | -------------- | -------- | ----- |
Y. Wang and J. Zou. Volatility analysis in high-frequency financial data. Wiley Interdisciplinary
| Reviews: Computational | Statistics, | 6(6):393–404, | 2014. |
| ---------------------- | ----------- | ------------- | ----- |
S. Watanabe. Asymptotic equivalence of Bayes cross validation and widely applicable information
criterion in singular learning theory. Journal of Machine Learning Research, 11:3571–3594, 2010.
R. E. Watkins, S. Eagleson, B. Veenendaal, G. Wright, and A. J. Plant. Disease surveillance using
a hidden markov model. BMC Medical Informatics and Decision Making, 9(1):1–12, 2009.
M. West. Bayesian forecasting of multivariate time series: scalability, structure uncertainty and
decisions. Annals of the Institute of Statistical Mathematics, 72(1):1–31, 2020.
M. West, P. J. Harrison, and H. S. Migon. Dynamic generalized linear models and Bayesian
forecasting. Journal of the American Statistical Association, 80(389):73–83, 1985.
P. H. Westfall and S. S. Young. Resampling-based multiple testing: Examples and methods for
| p-value adjustment, | volume 279. | John Wiley | & Sons, 1993. |
| ------------------- | ----------- | ---------- | ------------- |
137

A. Willsky and H. Jones. A generalized likelihood ratio approach to the detection and estimation
of jumps in linear systems. IEEE Transactions on Automatic Control, 21(1):108–112, 1976.
D. J. Wilson. The harmonic mean p-value for combining dependent tests. Proceedings of the
National Academy of Sciences, 116(4):1195–1200, 2019.
P. R. Winters. Forecasting sales by exponentially weighted moving averages. Management Science,
6(3):324–342, 1960.
L.Xie,S.Zou,Y.Xie,andV.V.Veeravalli. Sequential(quickest)changedetection: Classicalresults
and new directions. IEEE Journal on Selected Areas in Information Theory, 2(2):494–514, 2021.
J. Xing, H. Burkom, and J. Tokars. Method selection and adaptation for distributed monitoring
of infectious diseases for syndromic surveillance. Journal of Biomedical Informatics, 44(6):1093–
1101, 2011.
J. J. Yang, J. Li, L. K. Williams, and A. Buu. An efficient genome-wide association test for
multivariate phenotypes based on the fisher combination function. BMC Bioinformatics, 17:
1–11, 2016.
M. Yuan, N. Boston-Fisher, Y. Luo, A. Verma, and D. L. Buckeridge. A systematic review of aber-
rationdetectionalgorithmsusedinpublichealthsurveillance. Journal of Biomedical Informatics,
94:103181, 2019.
M. Y. Zhang, J. R. Russell, and R. S. Tsay. A nonlinear autoregressive conditional duration model
with applications to financial transaction data. Journal of Econometrics, 104(1):179–207, 2001.
Y. Zhang, N. Ravishanker, and J. Zou. Structural break detection in financial durations. Applied
Stochastic Models in Business and Industry, 34(6):992–1006, 2018.
Y. Zhang, J. Zou, N. Ravishanker, and A. Thavaneswaran. Modeling financial durations using
penalized estimating functions. Computational Statistics & Data Analysis, 131:145–158, 2019.
Y. Zheng, Y. Li, and G. Li. On fr´echet autoregressive conditional duration models. Journal of
Statistical Planning and Inference, 175:51–66, 2016.
138

J.Zou,A.F.Karr,D.Banks,M.J.Heaton,G.Datta,J.Lynch,andF.Vera. Bayesianmethodology
for the analysis of spatial–temporal surveillance data. Statistical Analysis and Data Mining: The
| ASA Data | Science Journal, | 5(3):194–204, | 2012. |
| -------- | ---------------- | ------------- | ----- |
J. Zou, A. F. Karr, G. Datta, J. Lynch, and S. Grannis. A Bayesian spatio–temporal approach for
real–time detection of disease outbreaks: a case study. BMC Medical Informatics and Decision
| Making, | 14(1):1–18, 2014. |     |     |
| ------- | ----------------- | --- | --- |
J.Zou, Y.An, andH.Yan. Volatilitymatrixinferenceinhigh-frequencyfinancewithregularization
and efficient computations. In 2015 IEEE International Conference on Big Data (Big Data),
| pages 2437–2444. | IEEE, | 2015. |     |
| ---------------- | ----- | ----- | --- |
J.Zou, Z.Zhang, andH.Yan. Ahybridhierarchicalbayesianmodelforspatiotemporalsurveillance
| data. Statistics | in Medicine, | 37(28):4216–4233, | 2018. |
| ---------------- | ------------ | ----------------- | ----- |
139

6 Appendix
| 6.1 Derivation    |     | of  | conditional |         | correlation |     |     |     |     |     |     |     |
| ----------------- | --- | --- | ----------- | ------- | ----------- | --- | --- | --- | --- | --- | --- | --- |
| For a BVAR(1)-LCM |     |     | model,      | we have |             |     |     |     |     |     |     |     |
ind
|     |     | Y j,st  | |λ j,st | ∼ Pois(λ      | j,st  | ),          |        |               |       |        |     |       |
| --- | --- | ------- | ------- | ------------- | ----- | ----------- | ------ | ------------- | ----- | ------ | --- | ----- |
|     |     | η j,st  | = logλ  | j,st =ZZZ     | j βββ | j +γ j,t +α | j,st , |               |       |        |     |       |
|     |     | γ j,t = | ϕ j γ   | j,t−1 +ω      | j,t , |             |        |               |       |        |     |       |
|     |     |         |        |              |       |             |       |              |       |        |     |       |
|     |     |         | ω       |               |       |             | α      |               |       |        |     |       |
|     |     |         | 1,t     |               |       |             | 1,st   |               |       |        |     |       |
|     |     | ωωω =   |        |  ∼ N(000,ΣΣΣ |       | ),ααα =     |       |  ∼ N(000,ΣΣΣ |       | ),     |     | (6.1) |
|     |     | t       |        |              |       | ωωω st      |       |              |       | ααα    |     |       |
|     |     |         | ω       |               |       |             | α      |               |       |        |     |       |
|     |     |         | 2,t     |               |       |             | 2,st   |               |       |        |     |       |
|     |     |         |        |               |       |            |        |              |       |        |    |       |
|     |     |         |         | σ2            | ρ     | σ σ         |        | σ2            |       | ρ σ    | σ   |       |
|     |     |         |         | ω1            | ωωω   | ω1 ω2,ΣΣΣ  |        |               | α1    | ααα α1 | α2 |       |
|     |     | ΣΣΣ =   |        |               |       |             | =      |              |       |        |     |       |
|     |     | ωωω     |        |               |       |            | ααα    |              |       |        |    |       |
|     |     |         | ρ       | σ σ           |       | σ2          |        | ρ σ           | σ     | σ2     |     |       |
|     |     |         | ωωω     | ω1 ω2         |       | ω2          |        | ααα           | α1 α2 | α2     |     |       |
|     |     | γ ⊥⊥    | α       | .             |       |             |        |               |       |        |     |       |
|     |     | j,t     | j,st    |               |       |             |        |               |       |        |     |       |
we are aiming at deriving the conditional correlation between the count data in the BVAR(1)-
LCM model. We are going to derive the conditional mean, variance, and covariance in three
subsections.
| 6.1.1 Conditional |     |     | Mean | of Y | j,st |     |     |     |     |     |     |     |
| ----------------- | --- | --- | ---- | ---- | ---- | --- | --- | --- | --- | --- | --- | --- |
The conditional mean of Y given the covariates and covariance matrix of the latent effects is
j,st
| expressed | as, |     |     |     |     |     |     |     |     |     |     |     |
| --------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
E(Y |ZZZ βββ ,ΣΣΣ ,ΣΣΣ ) = E [E(Y |γ ,α ,ZZZ βββ ,ΣΣΣ ,ΣΣΣ )]
|     |     | j,st                     | j j    | ωωω ααα     |        | γj,t,αj,st|ΣΣΣωωω,ΣΣΣααα |        | j,st     | j,t j,st | j   | j ωωω ααα |       |
| --- | --- | ------------------------ | ------ | ----------- | ------ | ------------------------ | ------ | -------- | -------- | --- | --------- | ----- |
|     | =   | E                        |        | [λ          | ] =    | E                        |        | [exp(ZZZ | βββ +γ   | +α  | )]        | (6.2) |
|     |     | γj,t,αj,st|ΣΣΣωωω,ΣΣΣααα |        | j,st        |        | γj,t,αj,st|ΣΣΣωωω,ΣΣΣααα |        |          | j j      | j,t | j,st      |       |
|     | =   | exp(ZZZ                  | βββ )E |             | [exp(γ | )]E                      | [exp(α |          | )]       |     |           |       |
|     |     |                          | j j    | γj,t|ΣΣΣωωω |        | j,t αj,st|ΣΣΣααα         |        | j,st     |          |     |           |       |
For an AR(1) process (ϕ j ̸= 1), the conditional distribution of γ j,t given lag-one observation is,
,σ2
|     |     |     |     | γ   | j,t |γ j,t−1 | ,ΣΣΣ ωωω ∼ | N(ϕ j γ | j,t−1 | )   |     |     | (6.3) |
| --- | --- | --- | --- | --- | ------------ | ---------- | ------- | ----- | --- | --- | --- | ----- |
ωj
140

The marginal distribution of γ is,
j,t
(cid:32) (cid:33)
σ2
γ |ΣΣΣ ∼ N 0,
ωj
(6.4)
j,t ωωω 1−ϕ2
j
For a Poisson lognormal model, we have
Lemma 6.1 If
Y|λ ∼ Pois(λ),log(λ)|µ,σ2 ∼ N(µ,σ2), (6.5)
then,
E(Y|µ,σ2) = exp(µ+σ2/2)
(6.6)
Var(Y|µ,σ2) = E(Y|µ,σ2)+exp(2µ)exp(σ2)(exp(σ2)−1)
From lemma 6.1, the conditional expectation of Y given ZZZ βββ ,ΣΣΣ ,ΣΣΣ in (6.2) will be,
j,st j j ωωω ααα
(cid:32) (cid:33) (cid:32) (cid:33)
σ2 σ2
E(Y |ZZZ βββ ,ΣΣΣ ,ΣΣΣ ) = exp(ZZZ βββ )exp
ωj
exp
αj
= m (6.7)
j,st j j ωωω ααα j j 2(1−ϕ2) 2 j,st
j
6.1.2 Conditional variance of Y
j,st
With (6.7 ),the conditional variance of Y given ZZZ βββ ,ΣΣΣ ,ΣΣΣ is expressed as,
j,st j j ωωω ααα
Var(Y |ZZZ βββ ,ΣΣΣ ,ΣΣΣ ) = E(Y2 |ZZZ βββ ,ΣΣΣ ,ΣΣΣ )−(E[Y |ZZZ βββ ,ΣΣΣ ,ΣΣΣ ])2
j,st j j ωωω ααα j,st j j ωωω ααα j,st j j ωωω ααα
= E(Y2 |ZZZ βββ ,ΣΣΣ ,ΣΣΣ )−m2
j,st j j ωωω ααα j,st
= E (cid:2) E(Y2 |γ ,α ,ZZZ βββ ,ΣΣΣ ,ΣΣΣ ) (cid:3) −m2
γj,t,αj,st|ΣΣΣωωω,ΣΣΣααα j,st j,t j,st j j ωωω ααα j,st
= E (cid:2) λ2 +λ (cid:3) −m2
γj,t,αj,st|ΣΣΣωωω,ΣΣΣααα j,st j,st j,st
= E [exp(2ZZZ βββ +2γ +2α )+exp(ZZZ βββ +γ +α )]−m2
γj,t,αj,st|ΣΣΣωωω,ΣΣΣααα j j j,t j,st j j j,t j,st j,st
(cid:32) (cid:33) (cid:32) (cid:33) (cid:32) (cid:33)
2σ2
(cid:16) (cid:17)
σ2 σ2
= exp(2ZZZ βββ )exp ωj exp 2σ2 +exp(ZZZ βββ )exp ωj exp αj −m2
j j 1−ϕ2 αj j j 2(1−ϕ2) 2 j,st
j j
(cid:32) (cid:32) (cid:33) (cid:33)
σ2
= m +m2 exp ωj exp(σ2 )−1
j,st j,st 1−ϕ2 αj
j
(6.8)
141

| 6.1.3 | Conditional |     | covariance |     |     | between | Y    | and | Y    |     |     |     |     |
| ----- | ----------- | --- | ---------- | --- | --- | ------- | ---- | --- | ---- | --- | --- | --- | --- |
|       |             |     |            |     |     |         | i,st |     | j,st |     |     |     |     |
With (6.7), the conditional covariance between Y i,st and Y j,st is expressed as,
Cov(Y ,Y |ZZZ βββ ,ZZZ βββ ,ΣΣΣ ,ΣΣΣ ) = E [Cov(Y ,Y |γγγ,ααα,ZZZ βββ ,ZZZ βββ ,ΣΣΣ ,ΣΣΣ )]
i,st j,st i i j j ωωω ααα γγγ,ααα|ΣΣΣωωω,ΣΣΣααα i,st j,st i i j j ωωω ααα
|     | +Cov |                       | (E[Y | |γγγ,ααα,ZZZ | βββ | ,ΣΣΣ ,ΣΣΣ | )],E[Y | |γγγ,ααα,ZZZ |     | βββ ,ΣΣΣ | ,ΣΣΣ )]) |     |     |
| --- | ---- | --------------------- | ---- | ------------ | --- | --------- | ------ | ------------ | --- | -------- | -------- | --- | --- |
|     |      | γγγ,ααα|ΣΣΣωωω,ΣΣΣααα |      | i,st         | i   | i ωωω     | ααα    | j,st         |     | j j      | ωωω ααα  |     |     |
(6.9)
|     | = 0+Cov |                       |           | (exp(ZZZ | βββ +γ | +α     | ),exp(ZZZ |          | βββ +γ | +α  | ))   |     |     |
| --- | ------- | --------------------- | --------- | -------- | ------ | ------ | --------- | -------- | ------ | --- | ---- | --- | --- |
|     |         | γγγ,ααα|ΣΣΣωωω,ΣΣΣααα |           |          | i i    | i,t    | i,st      |          | j j    | j,t | j,st |     |     |
|     |         | (cid:18)              | (cid:18)ρ |          |        |        | (cid:19)  | (cid:19) |        |     |      |     |     |
|     |         |                       |           | ωωω σ ωi | σ ωj   |        |           |          |        |     |      |     |     |
|     | = m     | m                     | exp       |          | +ρ     | σ σ    | −1        |          |        |     |      |     |     |
|     | i,st    | j,st                  |           |          |        | ααα αi | αj        |          |        |     |      |     |     |
|     |         |                       |           | 1−ϕ      | ϕ      |        |           |          |        |     |      |     |     |
i j
|     | Since the | joint | marginal | distribution |     | of  | γ and | γ   | is,     |     |     |     |     |
| --- | --------- | ----- | -------- | ------------ | --- | --- | ----- | --- | ------- | --- | --- | --- | --- |
|     |           |       |          |              |     |     | i,t   | j,t |         |     |     |     |     |
|     |           |       |          |             |    |    |      |     |         |     |   |     |     |
|     |           |       |          |              |     |     |       | σ 2 | ρωωωσωi | σωj |     |     |     |
|     |           |       |          |              | γ   |     |       | ω i |         |     |     |     |     |
i,t
|     |            |     |         |    |     | ∼ N 000, |          | 1−ϕi   | 1−ϕiϕj |      |   |     | (6.10) |
| --- | ---------- | --- | ------- | --- | ---- | ---------- | -------- | ------ | ------ | ---- | --- | --- | ------ |
|     |            |     |         |    |     |           | ρωωωσωi |        |        | 2    |   |     |        |
|     |            |     |         |     |      |            |          | σωj    |        | σ ω  |     |     |        |
|     |            |     |         |     | γ    |            |          |        |        | j    |     |     |        |
|     |            |     |         |     | j,t  |            |          | 1−ϕiϕj |        | 1−ϕj |     |     |        |
|     | With (6.9) | and | (6.10), | we  | have |            |          |        |        |      |     |     |        |
Cov(Y ,Y |ZZZ βββ ,ZZZ βββ ,ΣΣΣ ,ΣΣΣ ) = Cov (exp(ZZZ βββ +γ +α ),exp(ZZZ βββ +γ +α ))
i,st j,st i i j j ωωω ααα γγγ,ααα|ΣΣΣωωω,ΣΣΣααα i i i,t i,st j j j,t j,st
|     |           | (cid:18) | (cid:18)ρ |           |     |       | (cid:19) (cid:19) |     |     |     |     |     |     |
| --- | --------- | -------- | --------- | --------- | --- | ----- | ----------------- | --- | --- | --- | --- | --- | --- |
|     |           |          | ωωω       | σ ωi σ ωj |     |       |                   |     |     |     |     |     |     |
| =   | m m       | exp      |           |           | +ρ  | σ σ   | −1                |     |     |     |     |     |     |
|     | i,st j,st |          |           |           | ααα | αi αj |                   |     |     |     |     |     |     |
|     |           |          | 1−ϕ       | ϕ         |     |       |                   |     |     |     |     |     |     |
i j
(6.11)
| 6.1.4 | Conditional |     | correlation |     |     | between | counts |     |     |     |     |     |     |
| ----- | ----------- | --- | ----------- | --- | --- | ------- | ------ | --- | --- | --- | --- | --- | --- |
Combining the results from (6.7), (6.8) and (6.11), we will be able to compute the conditional
| correlation |        | for the | s-th        | stock            | and the    | t-th            | time | interval, |     |          |          |     |        |
| ----------- | ------ | ------- | ----------- | ---------------- | ---------- | --------------- | ---- | --------- | --- | -------- | -------- | --- | ------ |
|             | Corr(Y | i,st ,Y | j,st |ZZZ i | βββ i ,ZZZ j βββ | j ,ΣΣΣ ωωω | ,ΣΣΣ ααα ) =    |      |           |     |          |          |     |        |
|             |        |         |             |                  | (cid:16)   | (cid:16)ρωωωσωi | σωj  |           |     | (cid:17) | (cid:17) |     |        |
|             |        |         |             | m                | m          | exp             |      | +ρ        | σ σ | −1       |          |     |        |
|             |        |         |             | i,st             | j,st       |                 |      | ααα       | αi  | αj       |          |     | (6.12) |
1−ϕiϕj
(cid:115)
|     |            |      |          |            |         |          | (cid:18)         |       |      | (cid:18) | (cid:18) | (cid:19) (cid:19)(cid:19) |     |
| --- | ---------- | ---- | -------- | ---------- | ------- | -------- | ---------------- | ----- | ---- | -------- | -------- | ------------------------- | --- |
|     | (cid:16)   |      | (cid:16) | (cid:16) σ | 2       | (cid:17) | (cid:17)(cid:17) |       |      |          | σ 2      |                           |     |
|     | m          | +m2  | exp      |            | ω i +σ2 | −1       |                  | m +m2 |      | exp      | ω j +σ2  | −1                        |     |
|     |            | i,st | i,st     | 1−ϕ2       |         | αi       |                  | j,st  | j,st |          | 1−ϕ2     | αj                        |     |
|     |            |      |          |            | i       |          |                  |       |      |          | j        |                           |     |
| 6.2 | Additional |      | figures  |            |         |          |                  |       |      |          |          |                           |     |
142

Healthcare
|     |     | ABT | AMGN | BAX | BIIB |     |
| --- | --- | --- | ---- | --- | ---- | --- |
1.00
0.75
0.50
0.25
0.00
|     |     | BMY | CELG | GILD | JNJ |     |
| --- | --- | --- | ---- | ---- | --- | --- |
1.00
0.75
0.50
|     | noitalerroC 0.25 |     |     |     |     | TYPE |
| --- | ---------------- | --- | --- | --- | --- | ---- |
0.00
|     |     | LLY | MDT | MRK | PFE | Model−based |
| --- | --- | --- | --- | --- | --- | ----------- |
1.00
|     | 0.75 |     |     |     |     | Empirical |
| --- | ---- | --- | --- | --- | --- | --------- |
0.50
0.25
0.00
|     |     |     | 0 501001502000 | 501001502000 | 50100150200 |     |
| --- | --- | --- | -------------- | ------------ | ----------- | --- |
UNH
1.00
0.75
0.50
0.25
0.00
0 50100150200
Time interval
Figure31: Thetraceplotofdailyaggregatedmodel-basedandempiricalcorrelationsintheHealth-
| care sector | throughout | January | 2023 |     |     |     |
| ----------- | ---------- | ------- | ---- | --- | --- | --- |
Industrials
|     |     | BA  | CAT | EMR | FDX |     |
| --- | --- | --- | --- | --- | --- | --- |
1.00
0.75
0.50
0.25
0.00
|     |     | GD  | GE  | HON | LMT |     |
| --- | --- | --- | --- | --- | --- | --- |
1.00
0.75
0.50
noitalerroC
|     | 0.25 |     |     |     |     | TYPE |
| --- | ---- | --- | --- | --- | --- | ---- |
0.00
Model−based
|     |      | MMM | NSC | RTN | UNP |           |
| --- | ---- | --- | --- | --- | --- | --------- |
|     | 1.00 |     |     |     |     | Empirical |
0.75
0.50
0.25
0.00
|     |     |     |     | 0 501001502000 | 50100150200 |     |
| --- | --- | --- | --- | -------------- | ----------- | --- |
|     |     | UPS | UTX |                |             |     |
1.00
0.75
0.50
0.25
0.00
|     | 0   | 501001502000 | 50100150200 |     |     |     |
| --- | --- | ------------ | ----------- | --- | --- | --- |
Time interval
Figure 32: The trace plot of daily aggregated model-based and empirical correlations in the Indus-
| trials sector | throughout | January | 2023 |     |     |     |
| ------------- | ---------- | ------- | ---- | --- | --- | --- |
143

ABT AMGN BAX BIIB
50
40
30
20
10
BMY CELG GILD JNJ
50
40
30
20
10
LLY MDT MRK PFE
50
40
30
20
10
BVRW(1)−LCMSLR BVRW(1)−LCMSLR BVRW(1)−LCMSLR
UNH
50
40
30
20
10
BVRW(1)−LCMSLR
MODEL
ESMR
Health care
Figure 33: Box plots for the square root of MSE comparison in the Health care sector between
BVRW(1)-LCM and Simple Linear Regression in January 2023
BA CAT EMR FDX
80
60
40
20
0
GD GE HON LMT
80
60
40
20
0
MMM NSC RTN UNP
80
60
40
20
0
BVRW(1)−LCMSLR BVRW(1)−LCMSLR
UPS UTX
80
60
40
20
0
BVRW(1)−LCMSLR BVRW(1)−LCMSLR
MODEL
ESMR
Industrials
Figure 34: Box plots for the square root of MSE comparison in the Industrials sector between
BVRW(1)-LCM and Simple Linear Regression in January 2023
144