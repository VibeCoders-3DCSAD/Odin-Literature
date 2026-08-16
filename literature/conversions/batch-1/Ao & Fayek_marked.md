---
conversion_metadata:
  converted_at: "2026-07-22T11:58:16Z"
  converter_tool: "markitdown"
  converter_version: "0.1.6"
  source_pdf: "Ao & Fayek.pdf"
  source_pdf_sha256: "ef8d0eba409d5c259a7a45f54fdfc0175c2fc302570e94bffbf0017e321d09e3"
  page_count: 32
  markdown_char_count: 266899
---

<!-- PAGE-AWARE EXTRACTION (via pdfminer.six) -->

<!-- PAGE 1 -->

Systematic Review
Continual Deep Learning for Time Series Modeling

Sio-Iong Ao 1,* and Haytham Fayek 2

1

2

International Association of Engineers, Unit 1, 1/F, Hung To Road, Hong Kong
School of Computing Technologies, RMIT University, Building 14, Melbourne, VIC 3000, Australia;
haytham.fayek@rmit.edu.au

* Correspondence: siao@graduate.hku.hk

Abstract: The multi-layer structures of Deep Learning facilitate the processing of higher-level abstrac-
tions from data, thus leading to improved generalization and widespread applications in diverse
domains with various types of data. Each domain and data type presents its own set of challenges.
Real-world time series data may have a non-stationary data distribution that may lead to Deep
Learning models facing the problem of catastrophic forgetting, with the abrupt loss of previously
learned knowledge. Continual learning is a paradigm of machine learning to handle situations when
the stationarity of the datasets may no longer be true or required. This paper presents a systematic
review of the recent Deep Learning applications of sensor time series, the need for advanced prepro-
cessing techniques for some sensor environments, as well as the summaries of how to deploy Deep
Learning in time series modeling while alleviating catastrophic forgetting with continual learning
methods. The selected case studies cover a wide collection of various sensor time series applications
and can illustrate how to deploy tailor-made Deep Learning, advanced preprocessing techniques,
and continual learning algorithms from practical, real-world application aspects.

Keywords: deep learning; continual learning; sensor; time series; preprocessing; non-stationary;
catastrophic forgetting

Citation: Ao, S.-I.; Fayek, H.

Continual Deep Learning for Time

Series Modeling. Sensors 2023, 23,

7167. https://doi.org/10.3390/

s23167167

Academic Editors: Chiman Kwan

and Anabela Oliveira

Received: 12 June 2023

Revised: 31 July 2023

Accepted: 10 August 2023

Published: 14 August 2023

Copyright: © 2023 by the authors.

Licensee MDPI, Basel, Switzerland.

This article is an open access article

distributed under

the terms and

conditions of the Creative Commons

Attribution (CC BY) license (https://

creativecommons.org/licenses/by/

4.0/).

1. Introduction

Time series modeling is a challenging task in data mining and machine learning.
Popular time series modeling tasks include classiﬁcation, anomaly detection, regression,
forecasting, and clustering. A time series is a sequence of measurements taken at various
times. Spatial time series data refers to multiple time series data corresponding to different
spatial locations. The spatial–temporal models face difﬁculties in addressing not only the
short-term and long-term patterns but also the spatial patterns [1]. Time series datasets
have the property of temporal ordering by nature [2]. Generally speaking, time series
models have the capability to utilize the fact that observations closer together in time relate
more closely. Time series modeling has many real-world applications like environment and
trafﬁc tasks, and successful modeling for the time series has become increasingly important.
For example, wind time series forecasting is essential for the decision-making of electric
system operators.

Time series analysis models can be divided broadly into time domain models and
frequency domain models. The time domain model investigates the data with respect
to time, while the frequency domain models focus the analysis on frequency instead of
time [2]. Statistical models like autoregressive models and the moving average models are
popular time domain models. Preprocessing operations like data cleaning, normalization,
differencing, feature selection, etc., are also popular time domain models. For the frequency
domain methods, mathematical models are employed to convert the time series data
between the time and frequency domains. The Fourier transform is a popular, simple,
and basic transforming tool for computing the frequency domain representation of a time

Sensors 2023, 23, 7167. https://doi.org/10.3390/s23167167

https://www.mdpi.com/journal/sensors

---

<!-- PAGE 2 -->

Sensors 2023, 23, 7167

2 of 32

series. Other popular preprocessing of frequency domain are wavelet transformation (WT),
empirical mode decomposition (EMD), etc.

Over the last decade, smart sensors have been deployed on a very large scale, and
huge amounts of continuous data have been generated [3]. Machine learning (ML) methods
can extract valuable information from datasets and have been widely employed for sensory
data in the industry, such as in the sensing and condition monitoring ﬁelds [4]. In the
knowledge discovery process, feedback is generated at each iteration with the goal that
further improvement can be achieved [5]. Deep Learning (DL), a particular type of machine
learning algorithm with multi-layer structures for processing higher-level abstractions
from the input dataset [6], is very well suited for very large datasets, as most of its layer
computations can be implemented in parallel and distributed computing techniques can be
applied easily. Deep Learning models have been shown to perform satisfactorily for many
time series analysis tasks like forecasting.

Deep Learning (DL) has been developed from traditional neural networks with large-
sized deep structures since 2006. Compared with traditional machine learning, DL learns
through a general-purpose learning procedure of multiple levels of representation and
identiﬁes features automatically [7]. In each layer, the representation is obtained from the
representation of the previous layer, involving updating process with a back-propagation
algorithm. Different from the more traditional ML methods, the addition of more layers
in the Deep Learning model can further enable the deep network to cope with scenarios
of increasing complexity, thus leading to improved generalization. A multi-layer learn-
ing structure enables very high performance in complex situations like video, speech,
classiﬁcation problems, and multi-sensor aggregation.

Deep Learning models have been shown to perform satisfactorily for many time
series analysis tasks. For example, Deep Learning has proven excellent in human activity
recognition (HAR) tasks, where wearable sensors can connect people with the cyber–
physical system through HAR [8]. Deep Learning has also been employed for tipping-
point prediction, with performance better than traditional early warning systems [9].
Nevertheless, the reliability of these forecasting methods is not guaranteed [10]. Deep
Learning methods may also face the overﬁtting problem. Common preprocessing methods
like smoothing, transformation, and estimation can remove the noise in time series signals in
advance and improve the overall performance of the time series models. The performance
of Deep Learning models may improve with preprocessing of time series inputs, usually
on conditions that the data distribution at test time is similar to that at training time.

When building ML models, it is usually assumed that the distribution of the data is
stationary. When the statistical properties of a time series do not depend on time, the time
series is called stationary [2]. It is possible that a time series is stationary in terms of one
characteristic while non-stationary for another characteristic. Mathematically, a time series
TS(yt) is deﬁned to be (weakly) stationary if all time t:

E(yt) = E[(yt−1)] = µ,

Var(yt) = σ2 < ∞,

Cov(yt, yt−k) = γ(k),

where the expected value µ is represented by E(.), the variance σ2 by Var(.), and the
covariance γ by Cov(.), respectively [11]. If the stationary conditions are no longer true, the
non-stationary behaviors may pose signiﬁcant difﬁculties for time series applications like
remote sensing [12].

In many real-world applications, the stationarity of the datasets may no longer be true.
There are four basic components that can cause the non-stationarity in some time series.
These four components are trend, seasonal, cyclical, and irregular components [13]. The
trend component refers to long-term increases or decreases over time, with examples like
long-term population growth. The seasonal component refers to the existence of seasonality

---

<!-- PAGE 3 -->

Sensors 2023, 23, 7167

3 of 32

patterns, like, for example, time series with yearly, quarterly, or monthly patterns. The
cyclical component refers to the patterns of ups and downs of a time series over the duration
of a cycle. The economic time series data of economic growth and then economic recession
may have a cyclical component. The irregular component is due to unpredictable factors
and does not repeat with particular patterns. For some time series data that exhibit a simple
trend, seasonal, and cyclical components, DL methods may be deployed directly with
satisfactory results, as seen in the ﬁrst part of Section 2. For some more complicated sensor
time series datasets, advanced preprocessing tools may be needed, as seen in the second
part of Section 2. Among the time series datasets that can not be handled well with both
advanced preprocessing and DL methods, some may ﬁt the scenarios for the deployment
of CL methods, which are described in detail in Section 3.

Continual learning is a paradigm of machine learning that may handle some of the
non-stationary situations while imitating the capability of human intelligence to handle new
situations from the old experiences learned. CL algorithms are developed to mimic human
intelligence that will rarely forget all of the learned information, as the natural system will
only gradually lose the learned information [14]. On the other hand, traditional neural
networks (NNs), while mimicking human cognition, lack this ability and face catastrophic
forgetting (CF). If Deep Learning methods are naively employed in CL tasks, learning on
shifted distribution may lead to CF problems. The capability of how to learn continually is
one of the biggest unsolved issues in ML [15], while forgetting learned knowledge is the
key obstacle to continual learning [16].

This survey focuses solely on real-world practical time series applications with DL
and CL. Lange et al. [17] presented a survey on CL about the stability–plasticity trade-off
and focused on the problems of classiﬁcation only. The motivation for them to limit the
discussion to classiﬁcation alone is that NN has been very well-established for classiﬁcation
tasks. In the survey [18], it was highlighted that the most recent surveys usually covered
continual learning partially, like biological underpinnings [19–22], visual classiﬁcation
tasks [23–26], NLP tasks [27,28], and RL [29]. Wang et al. [18] talked about only ﬁve
tasks of practical CL applications, i.e., object detection, semantic segmentation, conditional
generation, reinforcement learning, and NLP. None of the above-mentioned recent CL
surveys focused on time series analysis tasks like time series forecasting. The focus of this
survey is solely on the current application case studies of DL for sensor time series datasets.
It provides a summary of the difﬁculties that the DL faces in deployment for real-world
sensor applications and the advanced preprocessing techniques for how to address some of
these practical difﬁculties. There are some cases that typical DL approaches, together with
advanced preprocessing techniques, can handle well. Nevertheless, in some other time
series application cases, continual learning is found to be suitable for deployment. The
topic of deploying CL for sensor time series modeling has not been systemically covered in
these previous surveys.

This paper is organized with the following sections, covering the recent time series
applications of Deep Learning and continual learning. In Section 2, ﬁrstly, the focus is on
the current advances in deploying Deep Learning methods for sensor time series modeling.
Then, the recent sensor case studies that still require data preprocessing techniques for DL
modules are highlighted. In Section 3, a summary of the sensor time series datasets and
environments that suit the deployment of continual learning methods is undertaken.

2. Advances in Deep Learning Methods for Time Series Modeling

Deep Learning is capable of modeling the complex non-linear relationships among
the variables, while traditional neural network needs to assume that all input vectors are
independent, which may lead to its ineffectiveness for sequential data prediction [30]. Com-
paring DL with the conventional time series methods [13,31], it is found that Deep Learning
models can give better representation and classiﬁcation. Cai et al. [31](2019) investigated
the day-ahead multi-step load prediction of commercial buildings with RNN and CNN
against autoregressive integrated moving average with exogenous inputs (ARIMAX), a

---

<!-- PAGE 4 -->

Sensors 2023, 23, 7167

4 of 32

popular traditional time series method for the time series modeling of load forecasting.
The results show that the CNN approach with a direct multi-step procedure can perform
better than the seasonal ARIMAX by a 22.6% improvement in prediction accuracy. This
illustrated that the Deep Learning hierarchical structure may have the capability to han-
dle data-dependent uncertainty better. It is also shown that the long-term trends can be
explored better when the preprocessing tool of the moving averages method is deployed
for smoothing the short-term ﬂuctuations. Mahmoud and Mohammed [13] presented a
survey of Deep Learning models, such as CNN, RNN, LSTM, GRU, deep autoencoders
(AEs), restricted Boltzmann machines (RBM), deep belief networks (DBNs), in the time
series forecasting of electricity load and price, solar power, and ﬁnance, with comparison
results showing that DL performs better than classical methods.

After discussing the advantages of deploying DL methods with time series data, the
following Table 1 shows a synthetic summary of the advances in Deep Learning techniques
for real-world sensor time series applications, followed by a detailed description of the
corresponding methods, motivations, and advantages. The following Figure 1 shows
the tree diagram grouping the popular Deep Learning methods for sensor time series
classiﬁcation and forecasting tasks covered in this survey.

Table 1. Summary of the advances in DL techniques for sensor time series applications.

Ref. First Author

Year

[32]

Choi

2021

Application
Field

Time series
anomaly
detection

Datasets

Deep Learning
Models

Accuracy

Details

Water treatment
test-bed, water
distribution pipelines,
Mars Science
Laboratory rover

RNN, CNN, hybrid,
attention

No clear
one-size-ﬁts-all
method

[33]

Deng

2021

Detecting
deviation from
normal
patterns

Sensor time series
datasets of water
treatment systems
(SWaT and WADI)

Graph Deviation
Network

[34]

Jiang

2020

Time series
classiﬁcation

UCR Time Series
Classiﬁcation Archive

MLP, CNN,
ResNet

[35]

Ismail Fawaz

2019

Time series
classiﬁcation

Univariate
time series datasets of
the UCR/UEA archive

MLP, CNN, Echo
State Network

[36]

Han

2022

Leaf and wood
terrestrial laser
scanning time
series
classiﬁcation

Seven broad-leaved
trees (Ulmus
americana) with a Rigel
VZ-400i

Fully Convolutional
Neural Network,
LSTM-FCN, ResNet

[37]

Campos-
Taberner

2020

Classiﬁcation
of land use

Sentinel-2 time series
data

2-layer Bi-LSTM
network

54% better
F-measure than the
next best baseline

Not signiﬁcantly
better than 1-NN
classiﬁers with
dynamic time
warping

SOA performance
achieved with
CNN and deep
Residual Networks

Accurate
separation of leaf
and woody
components from
point clouds

Achieving best
overall accuracy of
98.7%

Compare DL anomaly
detection time series
models with
benchmark datasets

Combine graph neural
networks with
structured learning
approach

Conduct comparison
between nearest
neighbor and DL
models

Conduct empirical
study of DNNs for TSC

Compare DL models
on leaf and wood
classiﬁcation with a
time series of geometric
features

Evaluate deep
recurrent network
2-BiLSTM for land use
classiﬁcation

[38]

Naqvi

2020

[39]

Zheng

2020

Real-time
classiﬁcation of
normal and
abnormal
driving

Trafﬁc ﬂow
time series
forecasting

Database of driver
facial emotion and gaze

Trafﬁc ﬂow time series
from OpenITS

CNN

LSTM

Superior
performance vs.
previous methods

Apply CNN to ﬁnd
changes in gaze from
driver’s images

Outperform the
ARIMA and BPNN

Deploy LSTM for
trafﬁc ﬂow forecasting

---

<!-- PAGE 5 -->

Employ DNN
framework for
reliability evaluation of
cylinder

Conduct survey of
common encoders and
decoders for time series
forecasting

Employ generative
adversarial predictive
network for leaf and
root predictive
segmentation

Deploy deep network
for detecting common
patterns for
classiﬁcation and
regression tasks

Sensors 2023, 23, 7167

5 of 32

Table 1. Cont.

Ref. First Author

Year

[40]

Hua

2019

[41]

Chen

2020

Application
Field

Trafﬁc
prediction and
user mobility
of telecommu-
nication
problems

Equipment
reliability
prediction

Datasets

Deep Learning
Models

Accuracy

Details

Trafﬁc time series

Random
Connectivity LSTM

Reduced
computing
complexity by 30%

Deploy the Random
Connectivity LSTM for
trafﬁc and user
mobility prediction

Reliability test data of a
cylinder in the small
trolley of vehicle
assembly plant

Deep Learning
method based on
MLP

Signiﬁcant
improvement over
PCA and HMM

[42]

Lim

2021

Time series
forecasting

M4 competition (Smyl,
2020)

Exponential
smoothing RNN

[43]

Yasrab

2021

Plant growth
forecasting

Public datasets
(Arabidopsis and
Brassica rapa plants)

Generative
Adversarial Network

Hybrid model with
better performance
than pure methods

Strong
performance
matching expert
annotation

[44]

El-Sappagh

2020

Alzheimer’s
disease
progression
detection

Time series data from
Alzheimer’s Disease
Neuroimaging
Initiative

Ensemble of stacked
CNN and
Bidirectional LSTM

Much better than
conventional ML

[45]

Lara-Benitez

2021

[46]

Cao

2020

[30]

Rajagukguk

2020

Twelve time
series
forecasting
tasks

Investigating
temporal
correlations of
intra-series
and the
correlations of
inter-series

Prediction of
solar
irradiance and
photovoltaic

Twelve public
datasets cover time
series applications like
ﬁnance, industry, solar
energy, tourism, trafﬁc,
and
internet trafﬁc

MLP, Elman RNN,
LSTM, Echo State
Network, GRU,
CNN, Temporal
Convolutional
Network

LSTM and CNN
are the best choices

Evaluate seven popular
DL models in terms of
efﬁciency and accuracy

Time series datasets
from energy,
electrocardiogram, and
trafﬁc sectors

Spectral Temporal
Graph Neural
Network

Outstanding
forecasting results,
plus advantage of
interpretability

Time series data of
temperature, humidity,
and wind speed

RNN, LSTM, GRU,
CNN-LSTM

Better prediction
results than
conventional ML

Develop the Spectral
Temporal Graph
Neural Network for
multivariable time
series forecasting

Evaluate models based
on accuracy, forecasting
horizon, training time,
etc.

[47]

Torres

2018

Solar energy
generation
forecasting

Two-year time series of
PV power from a
rooftop PV plant

[48]

Xiao

2019

Prediction of
sea surface
temperature
(SST)

SST time series
data from 36-year
observations by
satellite

Deep Learning
approach, based on
the H20 package
with the grid search
method for
hyper-parameter
optimization

Convolutional Long
Short-Term Memory

Particularly
suitable for big
solar data, given its
strong computing
behavior

Deploy DL approach
for solar photovoltaic
power forecasting for
the next day

Outperform
persistence model,
SVR, and two
LSTM models

Deploy ConvLSTM to
capture correlations of
SST across both space
and time

Multi-layer perceptron (MLP), recurrent neural network (RNN), Long Short-Term
Memory network (LSTM), convolutional neural network (CNN), graph neural networks
(GNN), deep belief network (DBN), autoencoder (AE), and neural networks with an
attention mechanism are popular DL methods that have been used by the authors in
this survey.

---

<!-- PAGE 6 -->

Sensors 2023, 23, 7167

6 of 32

Figure 1. Tree diagram for grouping the popular Deep Learning methods for sensor time series
classiﬁcation and forecasting tasks covered in this survey [30,32–48] (note: if a paper uses two
methods separately with similar satisfactory results, the paper will be listed under both groups).

2.1. Multi-Layer Perceptron

MLP is the most conventional and simplest Deep Learning structure and is fully
connected (FC) between layers. All the neurons in one layer are connected to every neuron
in the nearby next layer. This means that each time series record is assigned its own weight,
and the temporal information is not utilized [35]. During the training phase of the MLP,
the weight between the neurons of two nearby layers can be estimated by the minimization

---

<!-- PAGE 7 -->

Sensors 2023, 23, 7167

7 of 32

of cost function through gradient descent optimization. The computing of the gradient of
the cost function is used in the back-propagation algorithm.

Jiang [34] conducted a comprehensive evaluation of the Deep Learning methods
(MLP, CNN, and ResNet) against a conventional machine learning method—the nearest
neighbor. The 1-NN classiﬁers are deployed with eight different distance measures. A
total of 128 univariate time series datasets about image, motion, and sensor from the UCR
Time Series Classiﬁcation Archive [49] were tested for the classiﬁcation performance of
the models. The experimental results showed that the Deep Learning methods could have
better performance than the nearest neighbor, but their difference is not signiﬁcant when
appropriate distance measures are deployed for the nearest neighbor based on the types of
the time series datasets.

Ismail Fawaz et al. [35] comprehensively evaluated the performance of three popular
structures of Deep Learning for time series classiﬁcation (TSC), i.e., MLP, CNN, and Echo
State Network (ESN). The Deep Learning models for TSC tasks can be classiﬁed as gen-
erative and discriminative approaches. The essential structure of ESN is the reservoir, a
sparsely connected random RNN with random initialization in the hidden layers. Jaeger
and Haas [50] invented the ESN in 2004 for time series forecasting for wireless communica-
tion tasks. The evaluation was conducted with the 85 univariate time series datasets of the
UCR/UEA archive [51] and 13 MTS datasets from Baydogan’s archive [52]. For univariate
time series applications, a one-dimensional CNN model is used, and the ﬁlter can be
viewed as performing a non-linear transformation for the time series. For multivariate time
series, the dimensions of the ﬁlter are set to be the number of dimensions of the time series.
For time series classiﬁcation, the ﬁnal layer is the discriminative layer which can assign
probability distribution for the class variables of the time series concerned. The results
supported that end-to-end Deep Learning is able to reach state-of-the-art performance for
TSC tasks.

Chen et al. [41] presented a Deep Learning method based on MLP for equipment
reliability prediction with sensor time series data. Condition monitoring for equipment and
its maintenance prediction is important for smart manufacturing. It is desirable to conduct
maintenance before the machine failure happens. The experiment was conducted with a
reliability test of a cylinder in the small trolley of vehicle assembly plant. As it takes longer
to complete each operation for an aging cylinder, the cylinder operation duration can serve
as the time series inputs for the Deep Learning method. The results show that the Deep
Learning method can perform much better than conventional machine learning methods.
Lara-Benitez et al. [45] compared the performance of seven popular Deep Learning
algorithms against twelve time series forecasting tasks. Time series forecasting is the
process of utilizing relevant historical time records to determine future values. When
deploying CNN for time series modeling, causal convolutional ﬁlters are used to ensure
that forecasting is made only based on past information in the time series [53]. The same
as standard CNN, temporal CNN also shares the same assumption that the relationships
among the time series variables are time-invariant. In attention mechanisms, the temporal
features of the time series signals can be aggregated with the dynamical generation of
weights by the attention layers. The attention network can pay more attention to the
signiﬁcant historical event, no matter how far back it is in the key-value lookup window.
The Deep Learning models are MLP, four models of recurrent networks (Elman RNN,
LSTM, Echo State Network, GRU), and two convolutional networks (CNN and Temporal
Convolutional Network). The twelve public datasets cover time series applications like
ﬁnance, industry, solar energy, tourism, trafﬁc, and internet trafﬁc. The evaluation results
showed that LSTM performs the best, while CNN can also make accurate and stable
forecasting with less computational requirements. Another performance comparison of
Deep Learning methods can be found in Torres et al. [54], making a summary of the
satisfactory time series forecasting applications of the popular Deep Learning models
(ENN, LSTM, GRU, BRNN, MLP, CNN, and TCN) in the sectors like energy, environment,
ﬁnance, health, industry, and image. The practical tip on how to set hyper-parameters

---

<!-- PAGE 8 -->

Sensors 2023, 23, 7167

8 of 32

has also been covered. The four main types of hyper-parameter optimization methods are
trial-error, grid, random and probabilistic.

Torres et al. [47] proposed a Deep Learning approach that was based on the H20
package written in R with the grid search method for hyper-parameter optimization and
implemented in the Apache Spark cluster environment. As the manufacturing cost for solar
panels decreases, solar energy is becoming much more popular. It is predicted that 30%
of the total electricity sources will be from solar energy in Australia by the year 2050 [55].
Factors like cloud cover, rainfall, solar radiation, and temperature can affect the gener-
ation of solar energy signiﬁcantly and make the forecasting of solar energy generation
difﬁcult. The dataset is the two-year time series of PV power with 30 min observation
interval. Its performance was compared with pattern-sequence-based forecasting (PSF) and
conventional neural networks. The experimental results supported that the Deep Learning
approach is very suitable for the solar energy forecasting task.

2.2. Recurrent Neural Network

RNN is designed with a state for the information at time steps such that it can handle
sequence data element-wise [56]. As it can maintain the dependencies among the time
series elements, RNN has gained success in different ﬁelds such as image captioning,
machine learning translation, speech recognition [57], and weather forecasting [58]. Elman
Neural Network (ENN) is an RNN model with a new hidden layer called the context layer,
which makes it capable of data sequence prediction. Nevertheless, RNN faces difﬁculties
due to the vanishing and exploding gradient problems during its training process. This
disadvantage of the vanishing gradient problem can be ampliﬁed when considering long-
range dependent relationships.

Choi et al. [32] focused on the frontier time series anomaly detection methods and
described how the methods model the interrelationship among variables and how the
temporal context was learned. Time series anomaly detection is about the identiﬁcation
of unexpected events from the time series data. Because of their learning capability for
large-scale sequences, Deep Learning methods contribute signiﬁcantly to multivariate time
series anomaly detection. Nevertheless, most of these methods have been developed for
very speciﬁc applications, and sufﬁcient domain knowledge is necessary [32]. Benchmark
datasets of the water treatment test-bed, the water distribution pipelines, and the Mars
Science Laboratory rover were used to compare the performance of the methods (RNN,
CNN, hybrid, and attention). The result highlights that there is no single Deep Learning
method that can ﬁt universally with all the time series tasks. Even though emerging Deep
Learning methods show encouraging results for multivariate time series anomaly detection,
most of these methods cannot explain the relationships among the sensors and thus have
limited ability to explain the deviations of the anomalous events.

Lim and Zohren [42] summarized the recent trends of Deep Learning models and hy-
brid models. Hybrid methods combining quantitative time series models with Deep Learn-
ing may address these limitations and improve the overall forecasting performance [42].
A hybrid model may be able to incorporate domain experts to feed the Deep Learning
model with prior information while addressing the issues associated with small datasets
and overﬁtting. Exponential smoothing RNN (ES-RNN) serves as a good example of how
the exponential smoothing module can help the RNN by addressing the non-stationary
trends of the time series by winning the M4 competition [59].

El-Sappagh et al. [44] presented an ensemble Deep Learning approach of stacked CNN
and Bidirectional LSTM (Bi-LSTM) models for AD progression detection. The temporal
information from sensor monitoring of chronic disease can be helpful for progression
detection, while the progression of chronic Alzheimer’s disease (AD) may be delayed if
it can be predicted at an early stage. The data of AD patients are heterogeneous multi-
modalities. Bi-LSTM is a special type of LSTM that can explore the dependencies of both
previous and future states [6]. For time series prediction with Bidirectional LSTM, once a
forecast is available in training, this value can be utilized for the subsequent readjustment

---

<!-- PAGE 9 -->

Sensors 2023, 23, 7167

9 of 32

process. This may result in a deeper understanding of the context concerned. The model
can handle the fusion of the ﬁve different types of time series data along with background
knowledge. The stacked CNN and Bi-LSTM models are capable of extracting both local
and longitudinal features of the modality, and the system can make predictions based on
these resultant features. The time series data from the Alzheimer’s Disease Neuroimaging
Initiative were used, and the results support the superior performance of the proposed
ensemble Deep Learning approach. For traditional methods to succeed in structural health
monitoring, suitable preprocessing of the raw sensor time series data is nearly always
needed. Dang et al. [60] applied four popular Deep Learning models, i.e., MLP, LSTM, 1D
CNN, and CNN, for structural damage detection with raw time series data. No feature
engineering procedure like extracting structural characteristics was performed. Three
different structures covering small to large structures were tested. The experimental results
support that 2D CNN is the most reliable, even though the computational time of 2D CNN
is also the highest among the models.

2.3. Long Short-Term Memory

Hochreiter and Schmidhuber [61] designed a new RNN model, called Long Short-
Term Memory (LSTM), with an internal memory unit and gate mechanism, for addressing
the issues of vanishing and exploding gradient during RNN training. A self-feeding loop is
used in the inner layers of LSTM that can learn time-based correlations such that knowledge
from previous inputs can be used in the analysis of the present inputs. The three gates
implementation [6] of LSTM can reduce the effects of the vanishing gradient problem
faced by RNN. The three gates are the forget gate, update gate, and output gate. The
forget gate is to determine what information should be kept or not. The update gate is
to determine what new information should be utilized for updating the memory state.
The output gate is to determine the output value that will serve as the input in the next
hidden unit. This design can enable the keeping of longstanding related information
while forgetting unrelated information. Thus, LSTM has the capability to process the long-
term dependencies of information in temporal datasets and is deployed for applications
like speech recognition, trafﬁc prediction, and weather forecasting. The Gated Recurrent
Unit (GRU) is designed with a less complex RNN structure than LSTM [62] but can also
remember useful information and explore the long-term dependencies of the variables. A
GRU has only two gates, i.e., the update gate and the relevance gate. The update gate is to
determine if the memory state is to update or not. The relevance gate is to determine how
related the previous memory state is for computing the next candidate. As GRU has only
two gates, it requires fewer parameters and computational time than LSTM [63] while still
keeping the capability for handling very long-range relationships among the time series.

Han and Sanchez-Azofeifa [36] investigated the leaf and wood terrestrial laser scan-
ning (TLS) time series classiﬁcation with Fully Convolutional Neural Network (FCN),
LSTM-FCN, and Residual Network (ResNet). CNN has been found to be capable of per-
forming time series classiﬁcation satisfactorily, as its multiple ﬁlters can produce multiple
discrimination features for classiﬁcation from the temporal inputs [35]. It is also found
that the combined LSTM-FCN method can further improve the time series classiﬁcation
results by FCN [64]. TLS point cloud data are useful for classifying the leaf and woody
components, and thus the leaf area index and wood area index. The TLS time series point
clouds were observed from seven broad-leaved trees (Ulmus americana). The experimental
results showed that all three models work better with multivariable time series than with
univariable time series. The three models can also work better than previous methods, and
all these three models produce similar performances on the testing time series.

Campos-Taberner et al. [37] investigated the interpretability of a 2-layer Bi-LSTM
network for the classiﬁcation of land use in Valencia, Spain, with Sentinel-2 time series data.
Added-noise permutation procedure was employed in both temporal and spectral domains
for evaluating the impact of different spectral and temporal features on the accuracy
rate. The experimental results showed that the overall accuracy of 98.7% achieved by the

---

<!-- PAGE 10 -->

Sensors 2023, 23, 7167

10 of 32

proposed method is better than other classiﬁcation approaches. The proposed system can
also show the relevance of predictors and highlight that the red and near-infrared Sentinel-2
bands contain the most helpful information, while the summer time series data is most
useful among the temporal information.

Zheng and Huang [39] deployed the Deep Learning LSTM network for the forecasting
of trafﬁc ﬂow time series. In an intelligent trafﬁc system, the accurate forecasting of trafﬁc
ﬂow may help to reduce urban congestion. The trafﬁc ﬂow time series from OpenITS
with 5 min intervals in ten days was used, and its performance was evaluated with the
traditional statistical method (ARIMA) and the conventional machine learning method
(BPNN). The results support the superior prediction accuracy of the LSTM model, with
the mean absolute percentage errors of ARIMA, BPNN, and LSTM at 20.97%, 9.06%, and
4.82%, respectively.

Hua et al. [40] deployed the Random Connectivity LSTM (RCLSTM) for trafﬁc predic-
tion and user mobility of telecommunication problems in order to reduce the computational
requirement of LSTM. In RCLSTM, the neurons are connected stochastically, and some
sparsity can be achieved in this random sparse graph model to reduce computing time.
RCLSTM is found to be suitable for latency-stringent tasks like trafﬁc time series. Another
similar task is the evaluation of the trafﬁc time series data from the GEANT backbone
network by Uhlig et al. [65]. The experimental results showed that the forecasting per-
formance of RCLSTM is similar to the traditional LSTM while successfully reducing the
computational time.

Rajagukguk et al. [30] investigated the prediction performance of solar irradiance and
photovoltaic (PV) power with four Deep Learning models against conventional machine
learning methods. As solar energy is renewable, solar photovoltaics has gained popularity
in the generation of electricity. For the PV prediction, the popular input time series data
are the temperature, humidity, and wind speed. The experimental results conﬁrmed that
all four Deep Learning models, i.e., RNN, LSTM, GRU, and CNN-LSTM, can perform
the prediction better, with CNN-LSTM achieving the best performance but also needing
the longest training time period. In the hybrid model CNN-LSTM, the CNN layers can
perform the feature extraction of the input time series, while LSTM for sequence prediction.
CNN-LSTM has been designed with the capability to handle temporal prediction tasks and
applied in many real-world applications. Experimental results like [66] also supported the
consistently better performance by CNN-LSTM over LSTM for precipitation prediction.

2.4. Convolutional Neural Network

CNN is another popular neural network for time series modeling. CNN is a DL
method of interconnected feedforward network architectures consisting of a sequence of
convolution, pooling, activation layers, and, ﬁnally, fully connected layers [67]. Filtering
operation is performed in the convolutional layers through a feature map. Local conﬂuences
of features are identiﬁed from the preceding layer through discrete convolution. Thus, this
type of model becomes known as a convolutional neural network. The pooling layer is
for reducing the input size and avoiding overﬁtting. The input for the last dense layer is
the ﬂattened features from the convolutional and pooling layers, and the forecasting is
made in this dense layer. 1D CNN can be deployed for simple applications, while more
sophisticated models, like CNN-Net, Enoded-Net, and CNN-LSTM, have more advanced
structures like larger kernel size and denser layers.

Naqvi et al. [38] deployed a CNN model for detecting changes in gaze from the
face and left- and right-eye images. Driver time series data is helpful for the real-time
classiﬁcation of normal and abnormal driving and, thus, for reducing aggressive driving.
The near-infrared (NIR) camera sensor is employed here to construct a large database of
driver facial emotion and gaze. The Dlib facial feature trackers were employed to identify
the region of interest (ROI) before feeding to the CNN model. The experimental results
supported the outstanding performance of the CNN model.

---

<!-- PAGE 11 -->

Sensors 2023, 23, 7167

11 of 32

2.5. Graph Neural Network

GNN is a neural network that processes the data with representation in graph domains,
like in chemical compounds, images, and web [68]. Graphs can be classiﬁed as cyclic,
directed, undirected, or a combination of these three. GNNs have been found useful for
applications including chemistry, citation networks, environmental condition forecasting,
molecular biology, physics, and social networks. A few DNN topologies may indeed be
viewed as GNN, for example, with CNN considered as a GNN with graphs of pixel-per-
grid grids.

Deng and Hooi [33] developed a Graph Deviation Network (GDN) model for discov-
ering the relationship graph among the sensors and for detecting deviation from normal
patterns. Graph neural networks can model the complex patterns in data of graph structure,
with the node state inﬂuenced by its neighbor note states. Velickovic et al. [69] developed
the graph attention network (GAT), which employed the attention function for evalu-
ating the various weights for various neighbors during aggregation. A difﬁculty for a
typical GNN model is that the graph structure is needed as an input, while this struc-
ture may not be known in advance. The proposed system consists of sensor embedding,
graph-structured learning, graph-attention-based forecasting, and graph deviation scoring.
The system is tested with two large-scale sensor time series datasets of water treatment
systems (SWaT and WADI). The experimental results supported the performance of the
proposed system, while the interpretable output can assist users in better understanding
and localizing anomalies.

Cao et al. [46] presented Spectral Temporal Graph Neural Network (StemGNN) with
Graph Fourier Transform (GFT) for capturing inter-series correlations and Discrete Fourier
Transform (DFT) for temporal correlations. A difﬁculty for multivariate time series is the
complexity involving both the temporal correlations of intra-series and the correlations of
inter-series simultaneously. The spectral representations obtained with GFT and DFT enable
the Deep Learning modules to have clear enough patterns for the analysis. The experimental
results from ten real-world time series public datasets (from energy, electrocardiogram, and
trafﬁc sectors) conﬁrm the performance of the proposed StemGNN.

2.6. Others and Hybrids

Hinton and Osindero et al. [70] developed the ﬁrst model and training algorithm for a
deep belief network (DBN) in 2006. DBN has a hierarchical structure with a large number
of stacked restricted Boltzmann machines (RBMs) and utilizes a greedy layer-by-layer
learning approach with ﬁne-tuning. The RBMs can efﬁciently extract the features for the
initialization of feedforward neural networks, hence improving the network generalization
capability. In each RBM, there is both a visible layer and a concealed layer consisting of
neurons. While the RBM’s layers are interconnected with each other, the units among each
layer are not. The updating of the network parameters can be done with a SoftMax classiﬁer.
Autoencoder utilizes a feature learning paradigm that can learn para-metric maps
directly from inputs to corresponding representation [71,72]. An AE consists of an encoder
and a decoder. The encoder is for feature extraction, while the decoder is for mapping the
feature space back to the input space. The structure of the encoder and decoder is an input
layer, hidden layers, and an output layer. Back-propagation algorithm is deployed for
updating the weights of the hidden layers. Deep AE can serve as a data-driven approach
for learning feature extraction automatically.

Neural networks with an attention mechanism have succeeded in time series appli-
cations [73]. These networks can dynamically control the mapping from the inputs to the
outputs intelligently with other knowledge of the task. The transformer model is based
on an encoder–decoder architecture of these networks. The input is fed to the encoder,
which consists of a stack of encoders. Then, the transformer can generate the output based
on the encoded input and previous outputs in the decoder as well. A clear advantage of
transformers is the access to any points in the past, no matter how far their distances are,
leading to the capability to discover the long-term dependencies among the time series data.

---

<!-- PAGE 12 -->

Sensors 2023, 23, 7167

12 of 32

Yasrab et al. [43] designed a Generative Adversarial Network (GAN) for forecasting
the expected growth of the plant. Plant phenotyping is the investigation of plant trait
growth and other quantitative parameters and may be automated with the help of Deep
Learning. GAN is usually developed from CNN and is formed with two networks, i.e., the
generator and the discriminator. Both networks can learn together by competing with each
other to generate new examples of synthetic data. Segmentation masks of shoot and root
were generated to predict the plant system in the future. Two public datasets (Arabidopsis
and Brassica rapa plants) were used. The evaluation results illustrated that the proposed
system can reach the level with annotation by an expert.

Xiao et al. [48] developed a Convolutional Long Short-Term Memory (ConvLSTM)
model to utilize the spatiotemporal correlations of sea surface temperature (SST) for its
short and mid-term prediction. In the global ocean, SST has a signiﬁcant inﬂuence on
the marine ecosystem. SST time series data from 36-year observations by satellite was
used to evaluate the ConvLSTM against the persistence model, support vector regression
model, and LSTM models. When handling spatiotemporal data by fully connected LSTM
(FC-LSTM), it is noted that the spatial correlations can be lost [66]. To address this issue,
the ConvLSTM replaces the FC-LSTM matric multiplication with convolution operation
in the transitions. This is to ensure that the model can explore both spatial and temporal
correlations. The experimental results conﬁrmed that ConvLSTM performs better than
other methods for the one-to-ten-day-ahead prediction of SST time series.

2.7. Advanced Preprocessing and Deep Learning Applications

Feature engineering can be very important in the data preprocessing stage before
feeding data to the Deep Learning models by signiﬁcantly reducing the computational
requirements for unnecessary features. Its importance is highlighted in the work of Elsayed
and Thyssens et al. [74], which evaluated the time series forecasting performance of eight
Deep Learning methods against the traditional machine learning method—the Gradient
Boosting Regression Tree (GBRT). External features were utilized for the target values, and
data ﬂattening can obtain the one input instance for GBRT. The evaluation was conducted
with nine datasets covering air quality, electricity, ﬁnance, solar energy, and trafﬁc. The
results showed that the window-based transformation could enable GBRT to achieve the
best forecasting performance over the Deep Learning models, covering various types like
matrix factorization, RNNs, LSTMs, and bi-directional LSTM models. It is shown that
simpler machine learning models with efﬁcient feature engineering can outperform the
frontier Deep Learning methods without feature engineering. Dablander and Bury [9]
highlighted the importance of preprocessing by showing that the DL model cannot extract
enough relevant features for classifying the stationary AR(1) processes without detrending
or with a Gaussian ﬁlter. The results showed that the method might learn unique features
related to a Lowess ﬁlter instead of the relevant features of the system near the bifurcation.
Thus, careful planning is needed when deploying the preprocessing models.

The following Table 2 highlights the most recent case studies that advanced prepro-
cessing is still needed, along with the Deep Learning methods, for modeling different
popular types of sensor time series. In Table 2, a synthetic summary of the application
ﬁelds, the advanced preprocessing techniques, the DL methods, accuracy, and brief appli-
cation details is presented, followed by a more detailed description of the corresponding
methods, motivations, and advantages. The following Figure 2 shows the tree diagram
for grouping the popular preprocessing methods for sensor time series classiﬁcation and
forecasting tasks covered in this survey.

---

<!-- PAGE 13 -->

Sensors 2023, 23, 7167

13 of 32

Table 2. Summary of the importance of advanced preprocessing techniques for real-world sensor
time series DL applications.

Ref.

First Author

Year

Application Field

Preprocessing
Methods

Deep Learning
Models

Accuracy

Details

[75]

Kanani

2020

[76]

Kisa

2020

[8]

Zheng

2018

ECG time series
signals for
monitoring and
classiﬁcation of
cardiovascular
health

Surface
electromyography
time series of
human muscles for
gesture
classiﬁcation

Classifying eight
daily activities
from wearable
sensors

Squeezing and
stretching of the signal
along the time axis

1D convolution

Achieved more
than 99%
accuracy

Develop a DL
architecture for the
preprocessing process
for increased training
stability

Empirical mode
decomposition

Segmentation and
transformation
methods

CNN

CNN

Worst results
for original
signal vs. all
IMFs images

Deploy EMD to
segmented signal to
obtain the Intrinsic
Mode Functions (IMFs)
images for CNN

Achieved best
results with
multichannel
method

Evaluate the impact of
segmentation and
transformation
methods on DL models

[77]

Castro Filho

2020

Synthetic Aperture
Radar images for
rice crop detection

3D-Gamma
ﬁlter and method of
Savitzky and Golay

LSTM,
Bidirectional
LSTM

High accuracy
and Kappa
(>97%)

[78]

ReBwurm

2020

Classifying crop
type based on raw
and preprocessed
Sentinel 2 satellite
time series data

Atmospheric
correction, ﬁltering of
cloud temporal
observations, focusing
on vegetative periods,
and masking of cloud

1D-convolutions,
RNN,
self-attention
model

Preprocessing
can increase
classiﬁcation
performance
for all models

[79]

Kingphai

2022

Classifying mental
workload levels
from EEG time
series signals

Independent
component analysis
based on ADJUST

[80]

Yokkampon

2022

Anomaly detection
of multivariate
sensor time series

Multi-scale attribute
matrices

[58]

Barrera-
Animas

2022

Rainfall prediction

[81]

Mishra

2020

Wind predictions

[10]

Livieris

2020

Time series data
from energy
section, stock
market, and
cryptocurrency

Correlation matrix with
the Pearson correlation
coefﬁcient

Discrete wavelet
transformation, fast
Fourier
Transformation, inverse
transformation

Iterative
transformations and
Augmented
Dickey–Fuller test

CNN, Stacked
GRU,
Bidirectional
GRU,
BGRU-GRU,
LSTM, BiLSTM,
BiLSTM-LSTM

Most effective
model
performance
can be
achieved

Multi-scale
convolutional
variational
autoencoder

Achieved
superior
performance
and robustness

LSTM,
Stacked-LSTM,
Bidirectional
LSTM

Attention, DCN,
DFF, RNN,
LSTM

LSTM,
CNN-LSTM

Retained the
main features
of DL models

Performed best
for attention
and DCN with
wavelet or FFT
signal

Considerably
improved the
DL forecasting
performance

[1]

Asadi

2020

Trafﬁc ﬂow
time series

Time series
decomposition method

Convolution-
LSTM

Outperformed
SOA models

Apply 3D
spatial–temporal ﬁlters
and smoothing with
Savitzky–Golay ﬁlter to
minimize noise

Present the
preprocessing pipeline,
including atmospheric
correction, temporal
selection of cloud-free
observations, cloud
masking, etc.

Deploy automatic
ICA-ADJUST to
remove the frequently
contaminated artifacts
components before
applying DL models

Develop a new
ERR-based threshold
setting strategy to
optimize anomaly
detection performance

Apply Pearson
correlation matric for
unsupervised feature
selection

Propose a
preprocessing model of
discrete wavelet
transformation and fast
Fourier transformation

Propose transformation
method for
enforcement of
stationarity of the time
series

Deploy time series
decomposition method
for separating
short-term, long-term,
and spatial patterns

---

<!-- PAGE 14 -->

Sensors 2023, 23, 7167

14 of 32

Table 2. Cont.

Ref.

First Author

Year

Application Field

Preprocessing
Methods

Deep Learning
Models

Accuracy

Details

[82]

Wen

2021

Survey of data
augmentation
methods

[83]

Azar

2020

Wireless network
with smart sensors

Data augmentation
methods (like time
domain and frequency
domain),
decomposition-based
methods, statistical
generative models

Deep generative
models

Show
successes in
time series
tasks

Compare data
augmentation methods
for enhancing the
quality of training data

Discrete wavelet
transform and the
error-bound
compressor Squeeze

Resnet,
LSTM-FCN,
GRU-FCN, FCN

Achieve the
optimal
trade-off
between data
compression
and quality

Develop a compression
approach with discrete
wavelet transform and
error-bound
compressor

Kanani and Padole [75] presented a preprocessing framework that can increase the
electrocardiogram (ECG) classiﬁcation accuracy of the Deep Learning methods signiﬁcantly,
with a higher than 99% accuracy rate. ECG time series signals are very efﬁcient for the
monitoring of cardiovascular health, with abnormal heartbeats detected from the ECG
patterns. The labeled MIT-BIH Arrhythmia dataset, which has ECG time series signals of
ﬁve different classes, was tested. The proposed preprocessing steps include the squeezing
and stretching of the signal along the time axis and the amplifying and shrinking of the am-
plitude of the signal. It is shown that these transformations do not change the characteristics
of the signals and can be regarded as completely lossless transformations here.

Kisa et al. [76] deployed an adaptive preprocessing method with empirical mode
decomposition (EMD) was proposed to handle this nonstationary time series, as the sur-
face electromyography (sEMG) time series is nonstationary and nonlinear. sEMG can be
employed to measure the electrical activity of human muscles. The recognition of human
movements is useful for applications like human–computer interaction (HCI). The sEMG
hand gesture time series data was obtained with a sensor device of surface bipolar elec-
trodes with 30 healthy volunteers. EMD can serve as a non-linear ﬁlter to decompose the
input time series into several intrinsic mode functions (IMFs). The outputs of the IMFs
were then fed into the Deep Learning model CNN based on Residual Networks (ResNet)
for gesture classiﬁcation. It is found that the IMFs can improve the validation accuracy of
the original time series from 94.22% to a maximum of 99.73%.

Zheng et al. [8] investigated the segmentation and transformation methods for their
effectiveness in data preprocessing for Deep Learning algorithms. In HAR tasks, segmen-
tation methods are essential as raw inertial time series can have very large ﬂuctuations.
Five segmentation options of ﬁve different segment lengths were evaluated with four
transformation methods, i.e., raw plot, multichannel, spectrogram, and spectrogram with
shallow features. The experiment was conducted with datasets of eight daily activities
from wearable sensors, car workshop maintenance activity data, etc. The results showed
that the classiﬁcation accuracy increases along with an increase in segment length, and
the multichannel method can perform the best for the HAR tasks. The overall accuracy is
97.2%, which is better than many other machine learning models.

Castro Filho et al. [77] applied a two-stage noise scheme for preprocessing SAR time
series, as there are inevitable noises like speckles for Synthetic Aperture Radar (SAR) images.
SAR sensors can be employed for mapping the rice-growing regions and constructing
continuous time series data. The SAR data is very useful for monitoring short phenological
stages and raising the classiﬁcation capacity. 3D-Gamma ﬁlter was used to eliminate the
speckle, and the method of Savitzky and Golay [84] was employed to smooth the time
series. The processed time series was fed to two Deep Learning methods, the Long Short-
Term Memory model and the Bidirectional LSTM model, for mapping rice crops with SAR
sensor time series from West Rio Grande do Sul (Brazil). The results were compared with

---

<!-- PAGE 15 -->

Sensors 2023, 23, 7167

15 of 32

conventional machine learning models, with BiLSTM showing the best performance in the
McNemar test.

Figure 2. Tree diagram for grouping the popular preprocessing methods for sensor time series
classiﬁcation and forecasting tasks covered in this survey [1,8,10,58,75–83] (note: if a paper uses
two methods separately with similar satisfactory results, the paper will be listed under both groups).

ReBwurm and Korner [78] investigated the effectiveness of Deep Learning models
for the classiﬁcation of crop type based on raw and preprocessed Sentinel 2 satellite
time series data. With the advance of remote sensing technologies, the amount of the
Earth observation time series data has been greatly increasing over recent years. While
many traditional models for remote sensing applications require preprocessing and feature

---

<!-- PAGE 16 -->

Sensors 2023, 23, 7167

16 of 32

extraction, ReBwurm and Korner [78] checked if the current Deep Learning methods are
able to utilize the raw time series data directly without data preprocessing. Atmospheric
correction, ﬁltering of cloud temporal observations, focusing on vegetative periods, and
masking of clouds, which are typical preprocessing methods for satellite time series, have
been applied. Additionally, 1D-convolutions, recurrent neural networks (RNN), and
the self-attention model of the encoder architecture of the Transformer network [85] are
deployed and evaluated. The results show that self-attention and RNN can perform better
for raw data, while the preprocessing process can improve the results for all three methods
satisfactorily.

Kingphai and Moshfeghi [79] employed seven Deep Learning models, i.e., convolu-
tional neural network (CNN), Stacked Gated Recurrent Unit (SGRU), Bidirectional GRU
(BGRU), BGRU-GRU, LSTM), Bidirectional LSTM (BiLSTM), and BiLSTM-LSTM, for clas-
sifying mental workload (MWL) levels from electroencephalography (EEG) time series
signals. MWL can lead to a better understanding of human performance in complex envi-
ronments. EEG time series can be utilized for classifying the mental workload level of a
human subject. The dataset STEW contains signals from 48 subjects in the resting and work-
ing states. Preprocessing is needed because there is usually noise in the EEG signals. The
independent component analysis based on ADJUST (ICA-ADJUST) by Mognon et al. [86]
was found to be the most effective preprocessing tool for this dataset by Kingphai and
Moshfeghi [87]. Kingphai and Moshfeghi [79] extracted four groups of features (frequency
domain, time domain, linear domain, and non-linear domain) for the Deep Learning mod-
els. The results showed that BiLSTM-LSTM performed best with 94.75% accuracy for
classifying resting vs. working states, while BGRU-GRU was best for classifying low vs.
moderate vs. high MWL levels with 83.03% accuracy.

Yokkampon et al. [80] deployed multi-scale attribute matrices as the preprocessing
tool for transforming the multivariate time series to develop a multi-scale convolutional
variational autoencoder for unsupervised anomaly detection of multivariate sensor time
series datasets. The attribute matrices can utilize the pair-wise inner product of the time
series among segments and effectively characterize system states of the time series. The
identiﬁcation of anomalies is about detecting data points that deviate signiﬁcantly from
their expected values. There are three types of time series anomalies: (1) point anomalies,
which refer to outlier points; (2) contextual anomalies, which differ signiﬁcantly from
typical points of the same context; and (3) collective anomalies, which refer to the existence
of a subset of time series data points with a signiﬁcant difference from the other points in
the whole dataset [88]. Anomaly detection can be employed in many real-world cases, like
fraudulent transaction detection, sensor network fault analysis, and abnormal equipment
monitoring. The proposed model was tested with four publicly available benchmark
datasets: the time series data by the Australian Centre for Remote Sensing, the Wafer time
series dataset of semiconductor microelectronics fabrication, the Emotiv EEG Neuroheadset
time series dataset, and Opt handwriting dataset. The experimental results show that the
model performed better than other baseline methods.

In the investigation by Barrera-Animas et al. [58], before feeding the time series data
into the DL models, the feature selection process was achieved with the correlation matrix
(CM), which is computed with the Pearson correlation coefﬁcient for the 43-dimensional
datasets. Rainfall prediction is complicated because of its nonlinear characters. Spa-
tial information like latitude and longitude and atmospheric information like humidity,
pressure, temperature, and wind speed may be utilized for the forecasting models. Barrera-
Animas et al. investigated the effectiveness of Deep Learning models, including LSTM,
Stacked-LSTM, and Bidirectional LSTM, with the conventional machine learning (ML)
model XGBoost, and also automated machine learning (AutoML) with the TPOT tool [89],
which can be regarded here as an ensemble of ML models. OpenWeather data of ﬁve UK
cities from 2000 to 2020 were evaluated. Highly correlated features will be eliminated. The
experimental results highlighted that the Stacked-LSTM with two hidden layers and the
Bidirectional LSTM could obtain the best performance in rainfall forecasting.

---

<!-- PAGE 17 -->

Sensors 2023, 23, 7167

17 of 32

Mishra et al. [81](2020) evaluated the wind predictions with ﬁve Deep Learning meth-
ods against three data preprocessing tools. The ﬁve methods are the attention mechanism
(Attention) of sequence-to-sequence encoder–decoder architecture [90], deep convolutional
network (DCN), deep feed Forward (DFF), recurrent neural network (RNN), and LSTM.
The dataset is the time series of the temperature and wind power variable. Discrete wavelet
transformation and fast Fourier transformation (FFT) are employed to transform the time
series dataset before feeding to the Deep Learning models, while inverse transformation
was applied to the DL model outputs before making predictions. The experimental results
showed that Attention and DCN work the best with wavelet and FFT, while some other
models work better with no need for data preprocessing.

Livieris et al. [10] proposed a preprocessing framework to further improve the ef-
ﬁciency and reliability of the Deep Learning methods.
Iterative transformations and
augmented Dickey–Fuller test were applied to the time series data for obtaining stationary
processed time series data before feeding to the Deep Learning model. The Ljung–Box
Q test was employed to check the autocorrelation of the model’s errors. Time series data
from energy section, stock market, and cryptocurrency were tested, and the experimental
results showed that the proposed preprocessing framework could enhance the efﬁciency,
accuracy, and reliability of the Deep Learning LSTM and CNN-LSTM models considerably.
Livieris et al. [91] continued their work on the investigation of the preprocessing frame-
work for Deep Learning models. On top of their previous focus on the transformation of
non-stationary time series to stationary by differencing the time series, the raw time series
is now subject ﬁrstly subject to the exponential smoothing method, which can transform
the raw data to a de-noised version. This process is to increase the quality of the time series
data and thus improve the prediction capability of the Deep Learning model CNN-LSTM.
The experimental results with cryptocurrency, energy, and stock markets conﬁrmed that the
preprocessing framework could signiﬁcantly achieve its objective of further improvement
for the Deep Learning models.

Asadi and Regan [1] employed the time series decomposition method to obtain the
short-term, long-term, and spatial patterns in the proposed preprocessing framework.
The short-term patterns of the spatial time series were explored with the fuzzy clustering
method, which can group neighboring time series together according to the checks on the
residuals of the time series. These residuals in spatial time series can provide meaningful
patterns with neighboring locations, like showing how the trafﬁc is evolving in the road
network. The trafﬁc ﬂow time series dataset was tested, and the method can obtain better
results than both the baseline and state-of-the-art methods.

Wen et al. [82] presented a survey of the data augmentation methods that are specif-
ically designed for handling time series datasets. Because many real-world applications
like medical time series or anomaly detection time series face the problem of not having
enough labeled data, it can be very helpful to have an effective way that can enlarge the
size and improve the quality of the training data during deploying Deep Learning on time
series datasets. Data augmentation has been found very suitable for this task, as it can
generate data synthetically for unexplored input space with correct labels. Not only basic
data augmentation methods, like time domain and frequency domain, but also advanced
methods, like decomposition-based methods, statistical generative models, and deep gen-
erative models, are covered in the survey by Wen et al. These augmentation methods are
found to be effective in time series classiﬁcation, time series anomaly detection, and time
series forecasting.

Azar et al. [83] developed a compression module for both univariate and multivari-
ate time series data with the discrete wavelet transform and the error-bound compressor
Squeeze (SZ). On-board processing and compression algorithms can reduce the problems
associated with the transmission of large data volumes in applications of the Internet of
Things (IoT). This preprocessing procedure is especially important for the sensor systems
in IoT, as they may only have very limited bandwidth, memory, and computational power.
The processed time series data is then sent to the Deep Learning models (Resnet, LSTM-

---

<!-- PAGE 18 -->

Sensors 2023, 23, 7167

18 of 32

FCN, GRU-FCN, FCN) for time series classiﬁcation. The Fully Convolutional Network
(FCN) deployed here consists of a convolutional layer with ﬁlters, a batch normalization
layer, and then a ReLU activation layer. The experiment was conducted with time series
datasets (UCR, UCI, and UEA) from sensors of ECG, motion, etc. The results supported
that the compression approach can achieve a high compression ratio, while its time series
denoising capability enables the Deep Learning module to achieve satisfactory classiﬁca-
tion accuracy.

3. Advances in Continual Learning Methods for Time Series Modeling

In the previous section, applications of Deep Learning models and preprocessing
methods in different real-world time series scenarios have been reviewed. Limitations of
Deep Learning models include a strict static requirement for the underlying process [92].
Post-deployment changes are not uncommon in the real world, but the DL methods are
usually of ﬁxed network structure after being deployed. When DL models are fed with data
not following the independent and identically distributed (i.i.d.) assumption, destructive
interference may occur and cause performance degradation [93]. Continual learning may be
deployed to address these difﬁculties faced by DL models in such a way that Deep Learning
models may beneﬁt from continual learning to become capable of learning continually
with adaptability.

A major characteristic of continual learning is its sequential learning process. At each
time, only a small amount of the input data is available. Other names for CL include lifelong
learning, sequential learning, and incremental learning. Mathematically, the continual
learning for both classiﬁcation and time series regression problems can be expressed as
follows [94]: Let T = (T1, . . . , Tm) represent the m tasks that arrive in sequence. For task
Ti(i = 1, 2, . . . , m), there exist N instances of labeled time series data Di = {(xi,r, yi,r)}N
r = 1.
Here, time series xi,r ∈ Xi is associated with the corresponding target yi,r ∈ Yi. For
classiﬁcation tasks, the target space Yi refers to class labels. For time series regression tasks,
the target space Yi refers to real numbers. A constraint of continual learning is that for
any task Ti, there exists no access to the data of previous tasks Tj(j = 1, . . . , i − 1). The
common goal of each task is to learn a solver model Mi, such that Mi : Xi → Yi , with
trainable parameters θi and estimated target ˆyi,r = Mi(xi,r; θi). Let L(yi,r, ˆyi,r; θi) represent
the training objectives. For classiﬁcation problems, this can be the standard cross-entropy
loss, while for time series regression problems, this can be the squared-error loss. Then,

Li =

q
N

N
∑
r=1

L(yi,r, ˆyi,r; θi) +

(cid:18) 1 − q

(i − 1)N

(cid:19)i−1
∑
j=1

N
∑
r=1

L(cid:0)yj,r, Mi

(cid:0) ˆxj,r; θi

(cid:1); θi

(cid:1)

where N refers to the number of instances, and 0 < q ≤ 1 refers to the importance assigned
to data from Ti.

There are several popular CL scenarios, like Instance-Incremental Learning (IIL),
Domain-Incremental Learning (DIL), Task-Incremental Learning (TIL), Class-Incremental
Learning (CIL), Task-Free Continual Learning (TFCL), and Online Continual Learning
(OCL). This taxonomy is based on how the incremental batches are divided and which
task identiﬁes are available [18]. IIL refers to scenarios where all training samples arrive in
batches and belong to the same task. DIL refers to scenarios where task identities are not
needed; tasks have different input distributions but the same data label space. TIL refers to
scenarios where task identities are available during both training and testing, and tasks
have disjoint data label spaces. CIL refers to scenarios where task identities are available
only during training and tasks have disjoint data label spaces. TFCL refers to scenarios
where no task identity is available and tasks have disjoint data label spaces. OCL refers to
scenarios where training samples for each task arrive from the data stream one by one, and
tasks have disjoint data label spaces.

Flesch et al. [95] highlighted that for human continual learning, the extensive back-
ground statistical knowledge gained from previous unsupervised training might be utilized

---

<!-- PAGE 19 -->

Sensors 2023, 23, 7167

19 of 32

for rule learning at later stages, though with several conditions, while DNN suffers catas-
trophic forgetting (CF) problems. CF can be viewed as an issue stemming from the NN
stability–plasticity dilemma, and the CF effect is associated with the abrupt loss of previ-
ously learned knowledge [17]. Plasticity refers to the NN’s ability to learn new knowledge,
while stability means the storing of learned knowledge. CL can be employed in supervised
learning, semi-supervised learning, unsupervised learning, and reinforcement learning as
well. Shaheen et al. [96] discussed the applications of continual learning for autonomous
systems. The real-world systems of vehicles with self-driving capability, unmanned aerial
vehicles, and autonomous robotics were highlighted.

Various degrees of constraint simpliﬁcation for solving the CF issue are imposed in
the current methods. There are constraints such as memory, computational power, and
data privacy. Nevertheless, there are issues when applying these methods, for example,
too rigid constraints that may break the idea of learning continually or too tailor-made
for solving a particular type of problem only. Pfulb and Gepperth [97] investigated the
CF problems in DNN with a very large number of datasets in visual classiﬁcation. The
large-scale experiments show that no model and dataset is free of the CF problems, whilst
a few potential workarounds may enable a few models to become practicable in a few
application-level environments. Inspired by open-set recognition, Prabhu et al. [98] pre-
sented a model called GDumb, which is not tailor-made for CL tasks. GDumb starts with
storing samples greedily in memory as they arrive, and during testing, it proceeds with new
model training with samples only in the memory. GDumb is shown to outperform many CL
approaches and may serve as an alert to the current progress in CL for classiﬁcation, with
the oversimpliﬁcations by some existing CL approaches to the problems resulting in little
real-world application value. In the deep autoencoder NN for time series forecasting [99],
buffers were deployed with online elastic weight consolidation to learn the probability
distribution of the data stream sequentially. A CL model with explicit memory structure
was used to address CF in their FFNN model for making long-term ﬁnancial investment
decisions [100]. Chen et al. [101] employed graph neural networks with CL strategies—data
replay and parameter smoothing—for transferring learned knowledge to the current model
in their trafﬁc ﬂow forecasting framework.

The relationship between neural network architectures and CF was investigated, and
it was found that the network width has a signiﬁcant effect on forgetting. Nevertheless,
when increasing the width to address CF, inefﬁciency problems like long computation time
and large energy waste inevitably appear. Lange et al. [17] investigated model capacity,
weight decay, dropout regularization, and the stability–plasticity trade-off among continual
learners. Lesort et al. [102] investigated the effects of the parameterizations of the DNN
output layer on learning and forgetting in CL. The evaluation is conducted in a simpliﬁed
learning environment, decomposing the model as a classiﬁer part for the output layer and
a feature extractor part for the rest of the DNN. Weights modiﬁcations, interference, and
projection drift can be the causes of CF in the output layer. More knowledge is gained
about the continual learning in output layers. Instead of focusing solely on continual
learning, Mundt et al. [103] presented a framework combining concepts from CL, open
set recognition, and active learning. This holistic approach shows promising results in
addressing catastrophic forgetting and robustness for open-world applications.

Current limitations for CL applications include the predominant closed-world as-
sumption when deploying models, which requires that any new data follows the same
distribution as those used during training. When this closed-world assumption is no longer
valid, the neural networks may give false predictions with unknown situations or with
corrupted data [103]. Another limitation is that many current works in CL may not often
consider the scalability issue in potential applications, which may have a very large number
of sub-tasks and, consequently, huge amounts of samples.

Whilst most of the recent works on CL focus on supervised tasks, the over-specializing
of CL training for a single set of environments limits CL generalization to other types of
applications [104]. With most recent research focusing on the CL applications for classiﬁca-

---

<!-- PAGE 20 -->

Sensors 2023, 23, 7167

20 of 32

tion tasks, this lack of attention may hinder time series applications like renewable energy
forecasting with CL models [99]. Deep Learning methods without the ability to remember
old knowledge may not handle well in real-world applications of time series forecasting
with non-stationary sequential data [105]. On the other hand, the current CL projects on
different time series regression tasks are showing encouraging results. Pham et al. [105]
designed a fast and slow learning network for online time series forecasting, with the
per-layer adapter for fast learning and associative memory for remembering and recalling
repeating past events. CL may be very useful for addressing ﬁnancial time series problems,
which can appear everywhere and are commonly non-stationary [100], and for trafﬁc ﬂow
time series forecasting, which is essential for smart transportation. Most current methods of
trafﬁc ﬂow forecasting assume static networks [101]. Yet, real-world trafﬁc ﬂow networks
change constantly, like possible network modiﬁcation and the addition of new parts [106].
After the above discussion illustrates the importance of continual learning among the
Deep Learning time series applications, a synthetic summary of the advances in continual
learning techniques for time series applications is presented in Table 3, followed by a
detailed description of the corresponding methods, motivations, accuracy, and brief details.
The following Figure 3 shows the tree diagram of the taxonomy of the continual learning
methods for sensor time series classiﬁcation and forecasting.

Table 3. Summary of the advances in continual learning techniques for time series applications.

Ref. First Author

Year

Application
Field

Motivations for
Deploying CL

Continual Learning
Models

Accuracy

Details

[107]

Sah

2022

Wearable sensors
for activity
recognition

Addressing the
catastrophic forgetting
in the non-stationary
sequential learning
process

A-GEM, ER-Ring,
MC-SGD

Still need
improvement for
multitask
training

Compare CL
approaches for sensor
systems

Overcoming the
non-stationary
environments

Replay, elastic weight
consolidation,
learning without
forgetting, naive and
cumulative strategies

Existing
strategies
struggle to
accumulate
knowledge

Assess the ability of
existing CL methods
for knowledge
accumulation over time

[108] Matteoni

2022

[93]

Kiyasseh

2021

[109]

Kwon

2021

Human state
monitoring of
domain-
incremental
scenario

Multiple clinics
with various
sensors for
cardiac
arrhythmia
classiﬁcation

Deployment in
mobile and
embedded
sensing
devices

Temporal data in clinics
are often
non-stationary

Buffer strategy to
construct the
continual learning
model CLOPS

Outperform
GEM and MIR

Addressing the
resources requirements
and limitations of the
mobile and embedded
sensing devices

CL approaches-
regularization, replay
and replay with
examples

Best results for
replay with
exemplars
schemes

[110]

Cossu

2021

Sensors of the
robotics system

Achieving walk
learning in different
environments

Continual learning in
RNNs

Highlight the
importance of a
clear
speciﬁcation

[111]

He

2022

Identiﬁcation of
anomalies

Addressing the lack of
transparency for CL
modules

Explainability
module based on
dimension reduction
methods and
visualization
methods

Proposed
evaluation score
based on metric

Propose the conceptual
design of explainability
module for CL
techniques

Apply
uncertainty-based
acquisition functions,
for instance, replay

Compare three main
CL approaches for
mobile and embedded
sensing applications
like activity
recognition

Evaluate CL
approaches in
class-incremental
scenarios for speech
recognition and
sequence classiﬁcation

---

<!-- PAGE 21 -->

Sensors 2023, 23, 7167

21 of 32

Table 3. Cont.

Ref. First Author

Year

Application
Field

Motivations for
Deploying CL

Continual Learning
Models

Accuracy

Details

[112]

Doshi

2022

Video anomaly
detection (VAD)

Overcoming
practical VAD
challenges

Incremental updating
of the memory
module,
experience replay

Outperform
existing methods
signiﬁcantly

[113] Maschler

2021

Metal-forming
time series
dataset of a
discrete
manufacturing

Providing automatic
capability for adapting
formerly learned
knowledge to new
settings

Continual learning
approach based on
regularization
strategies

Improved
performance vs.
no regularization

Develop a two-stage
CL approach with
feature embedding and
kNN-based RNN
model

Compare CL
approaches of
regularization
strategies on industrial
metal-forming data for
fault prediction

[114] Maschler

2020

Fault prediction
in a distributed
environment

Real-world restrictions
like industrial
espionage and legal
privacy concern
prevent the centralizing
of data from factories
for the DL training

LSTM algorithm with
elastic weight
consolidation

Promising results
for industrial
automation
scenarios

Apply elastic weight
consolidation for
distributed,
cooperative learning

[115]

Bayram

2020

Auditory scene
analysis

Addressing high-value
background noise and
high computational
demands

Continual learning
approach based on
Hidden Markov
Model

Achieve high
accuracy

Develop an
HMM-based CL
approach with UED
and retraining for time
series classiﬁcation

[106]

Xiao

2022

[116]

Schillaci

2021

Evolving
long-term
streaming trafﬁc
ﬂow

Addressing the
non-stationary data
distribution during
policy evolution

Transferring the
knowledge
gained from the
greenhouse
research facilities
to greenhouses

Addressing problems
like the requirement of
large-scale re-training
in the new facility

Prioritized
experience replay
strategy for
transferring learned
knowledge
into the model

Continual learning
RNN model with
episodic memory
replay and
consolidation

[94]

Gupta

2021

In-process
quality
prediction by
manufacturers

Addressing the lack of
practical variability
among industrial
sensor networks

Generator-based
RNN continual
learning module

Able to
continuously
learn and predict
trafﬁc ﬂow over
time

Formulate the trafﬁc
ﬂow prediction
problem as continuous
reinforcement learning
task

Outperform
standard
memory
consolidation
approaches

Possible
signiﬁcant
performance
enhancement

Present a CL approach
of an episodic memory
system and memory
consolidation

Deploy task-speciﬁc
generative models to
augment data for target
tasks

As it is NP-Hard to ﬁnd the optimal CL algorithms which can completely avoid
catastrophic forgetting [117], polynomial time heuristic algorithms have been proposed to
address the CF problems. These CL algorithms can be classiﬁed into three families, i.e.,
regularization-based methods, replay methods, and parameter isolation methods, accord-
ing to the storage and usage method for task-speciﬁc information during the sequential
learning process [17]. Combined approaches refer to the mixing of the methods together,
and outstanding results can be obtained on benchmark datasets [103]. Another possible
taxonomy is of regularization-based approach, replay-based approach, optimization-based
approach, representation-based approach, and architecture-based approach [18]. This
survey will follow the taxonomy of Lange et al. [17] and Mundt et al. [103].

---

<!-- PAGE 22 -->

Sensors 2023, 23, 7167

22 of 32

Figure 3. Tree diagram of the taxonomy of the continual learning methods for sensor time series
classiﬁcation and forecasting [93,94,106–116] (note: if a paper uses two methods separately with
similar satisfactory results, the paper will be listed under both groups).

---

<!-- PAGE 23 -->

Sensors 2023, 23, 7167

23 of 32

3.1. Regularization-Based Methods

Regularization-based methods need to utilize an extra regularization term in the loss
function for combining previous knowledge during the learning process of new data.
Regularization methods focused on how to preserve previous knowledge. Extra loss terms
can be deployed to preserve the important weights gained from the learning of former
tasks. Elastic weight consolidation (EWC) [118], learning without forgetting (LWF) [119],
and knowledge distillation [120] are popular regularization approaches.

Sah et al. [107] investigated the performance of three recent continual learning ap-
proaches (A-GEM [121], ER-Ring [122], and MC-SGD [123]) for addressing the catastrophic
forgetting in wearable sensors for activity recognition. In a wearable sensor system, it
is necessary to have the capability to monitor and recognize activities across users. This
sequential learning process is non-stationary and challenging for Deep Learning methods.
The PAMAP2 dataset [124] of human activity recognition, consisting of sensor time series
data of eight subjects and twelve daily activities, is used for the evaluation. The results
showed that MC-SGD performed the best by reducing nearly 29% of the forgetting, while
its computational time is still much less than the joint-task training time.

Matteoni et al. [108] developed two benchmarks of human state monitoring of domain-
incremental scenarios for CL models. In non-stationary environments, recurrent neural
networks for time series data can be of large importance [110], and investigation of the
network properties in these situations may lead to a better understanding and applications
of CL models. A signiﬁcant obstacle that hinders the development of CL models is the
shortage of enough standard benchmarks of time series datasets for the evaluation of the
CL models. The two benchmarks were derived from datasets WESAD [125] and ASCER-
TAIN [126] of time series classiﬁcation from physiological sequence data. Different CL
models were investigated with these two benchmarks to understand the effects of catas-
trophic forgetting on recurrent neural networks. Four common CL models, i.e., replay [20],
elastic weight consolidation (EWC) [118], learning without forgetting (LwF) [119], and
naive and cumulative strategies, were tested. The results showed that all the CL models can
mitigate forgetting, but besides the replay model, all other models still can not accumulate
knowledge over time.

Kwon et al. [109] comprehensively investigated the performance of three CL approaches
—regularization, replay, and replay with examples for deployment in mobile and embedded
sensing devices. Most of the existing continual learning methods do not consider the
resource requirements and limitations of mobile and embedded sensing devices [127].
Three datasets of human activity recognition, two datasets of gesture recognition, and one
dataset of emotion recognition were investigated to ﬁnd the trade-offs between system
performance, storage requirements, computational power requirements, and peak memory
requirements among the CL approaches. The results showed that the CL approach of
replying with exemplars works best after considering all the trade-offs.

Maschler et al. [113] evaluated the performance of a continual learning approach
based on regularization strategies, which mimic the human brain synaptic consolidation,
for industrial application. Existing methods for anomaly detection often lack the ﬂexibility
to adapt to changes in the manufacturing processes [113], while continual learning can
help overcome this issue by providing the automatic capability for adapting formerly
learned knowledge to new settings. Real-world metal-forming time series dataset of a
discrete manufacturing process was tested, showing promising results for the regularization
strategies over the multilayer LSTM approach with no regularization. Online elastic weight
consolidation is found to provide better performance than elastic weight consolidation.
Maschler et al. [128] evaluated the performance of the regularization strategies against
the open-access lithium-ion battery degradation dataset [129] with the LSTM approach
for remaining useful lifetime prediction for lithium-ion batteries. The results of these
degradation datasets reinforce the ﬁndings for the discrete manufacturing process. Network
monitoring can produce a huge amount of multivariate time series data that are useful
for usage, like network anomaly detection. Gonzalez et al. [130] outlined their conceptual

---

<!-- PAGE 24 -->

Sensors 2023, 23, 7167

24 of 32

framework of variational autoencoders and dilated convolutional networks for network
anomaly detection. The deep generative replay is explored for extending the continual
learning capability to the proposed system. The teacher generative model can create
synthetic data to imitate previous training examples, while the new student model can
learn from current new data and also these synthetic data at the same time. This continual
learning module may help to address catastrophic forgetting.

Maschler et al. [114] proposed an LSTM algorithm with elastic weight consolidation for
fault prediction in a distributed environment. Continual learning has the potential to serve
as a distributed approach for fulﬁlling the industrial automation need, with Deep Learning
performing fault prediction for industrial automation. This is because many real-world
restrictions like industrial espionage and legal privacy concern prevent the centralizing of
data from factories for the training of the Deep Learning models. NASA turbofan engine
dataset [131] was used for performance evaluation. The experimental results showed that
their approach could perform effectively with distributed datasets with no requirement for
centralized data storage, satisfying the requirements of many real-world manufacturers.

Schillaci et al. [116] developed a continual learning RNN model with episodic memory
replay and consolidation driven by prediction errors for transferring the knowledge gained
from the greenhouse research facilities to real-world greenhouses. Without the CL capability,
this process may otherwise be expensive and risky for the crop due to problems like the
requirement of large-scale re-training in the new facility. Sensor time series data may help
to better understand the causal models of a dynamic system, and this is very useful for
real-world applications. Currently, popular causal discovery methods utilize only static
data or pre-processed time series data in advance, making them not very suitable for real-
world robotics cases. Continual learning may address this limitation in the causal discovery
methods [132] but is under-investigated for robot application [133]. Castri et al. [133]
focused on the constraint-based methods for causal discovery and outlined their approach
of re-learning the causal model during observed scenario changes and during a new set of
interventions. The new inference matric of the causal model is checked against the matric
of the old causal model to discover the still valid causal links from the old model for the
new model. This approach of only small incremental changes can help the robotic system
address the CF problem. CL module can also help the robotic system address the hardware
resource limitation. Sensors in a greenhouse can produce time series data like climate
time series and leave temperature time series. A better understanding of the complex
greenhouse and modeling of these greenhouse time series data can help to predict the
effects of intervention better, thus increasing the crop yield. Memory retention is based on
congruence against prior knowledge retained in the model, and the experimental results
showed that this memory replay strategy could enhance the performance of standard
memory consolidation approaches.

3.2. Replay Methods

Replay methods need to store either the raw samples or the generated pseudo-samples
from the generative algorithm. These stored previous samples can be replayed to address
forgetting during the learning of new tasks. Difﬁculties for this approach may include the
demand for resources of large storage capability and the privacy concerns for storing and
deploying samples in real-world applications. Pseudo-rehearsal techniques can handle
these difﬁculties with a generative model instead of storing past samples directly.

Kiyasseh et al. [93] utilized the replay buffer strategy to construct the continual learning
model CLOPS from the temporal data in clinics, which is often non-stationary, as multiple
clinical sites with various sensors are involved. Acquisition based on uncertainty was
deployed for the replay of buffer instances. Four clinical environments involving transitions
between data modalities, diseases, clinics, and time are suitable non-stationary scenarios
to test the performance of the continual learning approach. The results show that CLOPS
performs better in three scenarios than the two other frontier methods—GEM [134] and
MIR [135]. He [111] also focused on the target-domain incremental application scenario

---

<!-- PAGE 25 -->

Sensors 2023, 23, 7167

25 of 32

and data-domain incremental application scenario of continual learning and described
how their previous framework, CLeaR, can be extended to learn inputs successively. The
framework utilizes the storage of buffered data by a novelty detector. The application of
continual learning to the regression scenario for power forecasting was outlined.

Doshi and Yilmaz [112] proposed a new continual learning approach for video
anomaly detection. Sensors and cameras in CCTV systems are generating huge amounts of
real-time video temporal data, and data size may be too big to be investigated by humans.
There is currently limited research on the continual learning of the new video data [112].
The CL capability was achieved in two ways, by the incremental updating of the memory
module and by experience replay. A new, more comprehensive dataset was created, con-
sisting of training segments in splits and test segments taken from a camera in a street in
New Orleans, USA. Three existing benchmark datasets, i.e., UCSD Ped 2, CUHK Avenue,
and ShanghaiTech, are also evaluated. The experimental results show that the proposed
approach can perform excellently in overcoming practical VAD challenges.

Xiao et al. [106] have recently formulated the evolving long-term streaming trafﬁc
ﬂow problem of sensor time series data as a continuous reinforcement learning task. With
the advances in Deep Q-Networks (DQNs), which enable the learning of complicated rein-
forcement tasks, the research on reinforcement learning (RL) has grown enormously [136].
Agents in Deep RL have shown outstanding performance in settings with narrow tasks,
but RL agents face problems like the over-ﬁtting tendency and the lack of generalization
capability to new variations [137]. This is in sharp contrast with the human ability to
learn continually and be adaptive to new scenarios over a lifetime, which is called CL.
DQNs face CF problems [118]. With the policy evolution leading to the non-stationary
data distribution, the CL concept can be applied in RL [104]. In this way, CL methods
may be used to address the CF, and solving this issue is crucial if the artiﬁcial agents are
going to have the capability to learn continuously [138]. The continual learner has the
advantage of adapting and recovering efﬁciently to changes encountered over time [29].
Here, the next ﬂow value predictor is the agent, the next time series ﬂow value in the sensor
is the agent, and the dynamical sensor and transportation network is the environment state.
The goal is to teach the autonomous agent to mimic sensor patterns and to plan the next
visit according to the sensor proﬁle. Prioritized experience replay strategy is deployed to
transfer learned knowledge into the model, and KL divergence to utilize long-term pattern
into model induction.

3.3. Parameter Isolation Methods

In parameter isolation methods, speciﬁc model parameters are assigned to each task
such that possible forgetting can be avoided. The methods address the CF issues with
the isolation of task-speciﬁc parameters and then dynamically adapt the structure of the
model. New modules are deployed for the learning of new tasks while keeping the formerly
learned parameters unchanged. A problem associated with this approach is the potential
growth of network parameters required. Progressive networks [139] and dynamically
expandable networks [140] are popular architectural methods.

3.4. Combined Approaches

Combined approaches refer to the mixing of the methods together [103].
Cossu et al. [110] conducted a review and evaluation of the continual learning in
RNNs, different from the typical CL focuses on feedforward and convolutional models.
Sequential data is very popular in real-world applications like robotics. The sensors of the
robotics system can feed the robot with time series input for its walk, learning in different
environments. Yet, as the current focus of continual learning is on reinforcement learning
through computer vision, there is not much research on sequential data processing for
continual learning [110]. Two benchmarks of speech recognition and hand-drawn sketches
were proposed for the evaluation of different CL methods. The results show that the
forgetting issues become more serious for longer sequences.

---

<!-- PAGE 26 -->

Sensors 2023, 23, 7167

26 of 32

He [111] presented the outline of their explainability module based on techniques
like dimension reduction methods and visualization methods. Currently, there is not
much research with a focus on the explainability of the continual learning algorithms [141],
resulting in the problems like a lack of transparency for the CL modules. The module can
not only provide the capability of explanation and visualization for the updated neural
network of the CL module but also for the identiﬁed anomalies as well. The identiﬁcation
of anomalies can be achieved with machine learning approaches like the Deep Support
Vector Data Description algorithm, unsupervised forest algorithm, and transformer-based
unsupervised algorithm. The basic guideline is that novelties of scores higher than the
threshold should be labeled as anomalies instead of labeling them as new tasks for the CL.
Bayram and Ince [115] presented a continual learning approach based on the Hidden
Markov Model (HMM) for the auditory scene analysis (ASA) task. Sensor systems can
be deployed to measure the time series data of dynamical acoustic events, and event
recognition is about the identiﬁcation of the events from these acoustic signals. High-value
background noise and high computational demands restrict the deployment of continual
learning approaches for this real-world ASA. A hierarchical HMM module is employed to
evaluate acoustic event recognition and unknown event detection. The new knowledge
gained from the HMM module is used for the retraining of a new HMM model in real-
time in the continual learning module. Multiple acoustic events were evaluated with
the proposed approach in real-time, and promising results of high effectiveness and high
accuracy were obtained.

Gupta et al. [94] addressed the lack of practical variability among the industrial sensor
networks by deploying an additional, conditional module to their generator-based RNN
continual learning module. Real-time sensor time series data may be used for the in-process
quality prediction by manufacturers. There are difﬁculties in limiting the applications of
Deep Learning methods for quality prediction, with the main difﬁculties being the con-
tinuous changes in the manufacturing environments. In real-world applications of Deep
Learning algorithms, various factories may have various settings, and their sensor environ-
ments may be different. Nevertheless, the current continual learning approaches do not
consider the practical variability among the total numbers and types of sensors deployed
in different manufacturing environments [94]. In injection molding, it is not uncommon
to produce new products, and the pre-trained models cannot adapt to this new process
well. Tercan et al. [142] developed a CL approach for this manufacturing scenario based on
the memory-aware synapses method for the training of ANN with various manufacturing
products. The experimental results of injection molding production support that the trans-
fer of network weights gained from similar tasks can effectively raise the efﬁciency of the
proposed approach. Graph neural network was employed in this conditioning module to
control the deployment dynamics of their continual learning module such that the overall
system can adapt to the different sensor settings in different real-world manufacturing envi-
ronments [94]. Real-world datasets (DSADS [143], HAR [144], and Turbofan—FD001 [145])
were tested by randomly removing 40% of the sensors for each task. The experimental
results support that their proposed conditioning GNN module can effectively enhance the
capability of the continual learning module.

To summarize, promising results were obtained by the most recent research of CL
applications with sensor time series data records for time series classiﬁcation and time
series forecasting tasks.

4. Conclusions

This survey has presented an overview of how to deploy Deep Learning methods,
advanced preprocessing methods, and continual learning methods for time series classiﬁca-
tion and forecasting in different real-world practical scenarios. The review has summarized
the encouraging results that CL can be deployed in ﬁelds beyond classiﬁcation tasks. The
non-stationary nature of the datasets in many ﬁelds poses challenges for conventional
machine learning and Deep Learning while serving as good platforms for innovative CL

---

<!-- PAGE 27 -->

Sensors 2023, 23, 7167

27 of 32

applications in future works. Another very interesting direction is that further experiments
may be done to assess the impact of architectures versus preprocessing algorithms such that
the role of speciﬁc algorithms can be better understood. This is because, as observed in this
survey, here, the majority of the authors focus on the practical deployment of DL and DL
models solely, without further evaluating the inﬂuences of with and without preprocessing
algorithms in each sensor environment.

Author Contributions: Conceptualization, S.-I.A.; formal analysis, S.-I.A. and H.F.; investigation,
S.-I.A. and H.F.; methodology, S.-I.A. and H.F.; writing, S.-I.A. and H.F. All authors have read and
agreed to the published version of the manuscript.

Funding: This research received no external funding.

Institutional Review Board Statement: Not applicable.

Informed Consent Statement: Not applicable.

Data Availability Statement: Data sharing is not applicable to this article as no new data were
created or analyzed in this study.

Conﬂicts of Interest: The authors declare no conﬂict of interest.

References

1.

2.

3.

4.

5.
6.
7.
8.

9.

Asadi, R.; Regan, A. A Spatial-Temporal Decomposition Based Deep Neural Network for Time Series Forecasting. Appl. Soft
Comput. 2020, 87, 105963. [CrossRef]
Ao, S.I. Applied Time Series Analysis and Innovative Computing; Springer: Dordrecht, The Netherlands, 2010; ISBN 978-90-481-8768-3.
[CrossRef]
Plageras, A.P.; Psannis, K.E.; Stergiou, C.; Wang, H.; Gupta, B.B. Efﬁcient IoT-Based Sensor Big Data Collection-Processing and
Analysis in Smart Buildings. Future Gener. Comput. Syst. 2018, 82, 349–357. [CrossRef]
Ao, S.I.; Gelman, L.; Karimi, H.R.; Tiboni, M. Advances in Machine Learning for Sensing and Condition Monitoring. Appl. Sci.
2022, 12, 12392. [CrossRef]
Ao, S.I. Data Mining and Applications in Genomics; Springer: Dordrecht, The Netherlands, 2008; ISBN 978-1402089749. [CrossRef]
Goodfellow, I.; Bengio, Y.; Courville, A. Deep Learning; MIT Press: Cambridge, MA, USA, 2016.
LeCun, Y.; Bengio, Y.; Hinton, G. Deep Learning. Nature 2015, 521, 436–444. [CrossRef]
Zheng, X.C.; Wang, M.; Ordieres-Meré, J. Comparison of Data Preprocessing Approaches for Applying Deep Learning to Human
Activity Recognition in the Context of Industry 4.0. Sensors 2018, 18, 2146. [CrossRef] [PubMed]
Dablander, F.; Bury, T. Deep Learning for Tipping Points: Preprocessing Matters. Proc. Natl. Acad. Sci. USA 2022, 119, e2207720119.
[CrossRef]

10. Livieris, I.E.; Stavroyiannis, S.; Pintelas, E.; Pintelas, P. A Novel Validation Framework to Enhance Deep Learning Models in

Time-Series Forecasting. Neural Comput. Appl. 2020, 32, 17149–17167. [CrossRef]

11. Guerrier, S.; Molinari, R.; Xu, H.; Zhang, Y. Applied Time Series Analysis with R. 2019. Available online: http://ts.smac-group.com

(accessed on 28 July 2023).

12. Rhif, M.; Abbes, A.B.; Farah, I.R.; Martinez, B.; Sang, Y. Wavelet Transform Application for/in Non-Stationary Time-Series

Analysis: A Review. Appl. Sci. 2019, 9, 1345. [CrossRef]

13. Mahmoud, A.; Mohammed, A. A Survey on Deep Learning for Time-Series Forecasting. Machine Learning and Big Data Analytics

Paradigms: Analysis, Applications and Challenges. Stud. Big Data 2021, 77, 365–392.
French, R. Catastrophic Forgetting in Connectionist Networks. Trends Cogn. Sci. 1999, 3, 128–135. [CrossRef]

14.
15. Lee, S.; Goldt, S.; Saxe, A. Continual Learning in the Teacher-Student Setup: Impact of Task Similarity. In Proceedings of the 38th

International Conference on Machine Learning, PMLR, Virtual, 18–24 July 2021; Volume 139.
Shin, H.; Lee, J.K.; Kim, J.; Kim, J. Continual Learning with Deep Generative Replay. arXiv 2017, arXiv:1705.08690.

16.
17. De Lange, M.; Aljundi, R.; Masana, M.; Parisot, S.; Jia, X.; Leonardis, A.; Slabaugh, G.; Tuytelaars, T. A Continual Learning Survey:

Defying Forgetting in Classiﬁcation Tasks. IEEE Trans. Pattern Anal. Mach. Intell. 2022, 44, 3366–3385.

18. Wang, L.; Zhang, X.; Su, H.; Zhu, J. A Comprehensive Survey of Continual Learning: Theory, Method and Application. arXiv

2023, arXiv:2302.00487v2.

19. Hadsell, R.; Rao, D.; Rusu, A.A.; Pascanu, R. Embracing Change: Continual Learning in Deep Neural Networks. Trends Cogn. Sci.

2020, 24, 1028–1040. [CrossRef]

20. Hayes, T.L.; Krishnan, G.P.; Bazhenov, M.; Siegelmann, H.T.; Sejnowski, T.J.; Kanan, C. Replay in Deep Learning: Current

21.

Approaches and Missing Biological Elements. Neural Comput. 2021, 33, 2908–2950. [PubMed]
Jedlicka, P.; Tomko, M.; Robins, A.; Abraham, W.C. Contributions by Metaplasticity to Solving the Catastrophic Forgetting
Problem. Trends Neurosci. 2022, 45, 656–666. [CrossRef] [PubMed]

---

<!-- PAGE 28 -->

Sensors 2023, 23, 7167

28 of 32

22. Kudithipudi, D.; Aguilar-Simon, M.; Babb, J.; Bazhenov, M.; Blackiston, D.; Bongard, J.; Brna, A.P.; Chakravarthi Raja, S.; Cheney,
N.; Clune, J.; et al. Biological Underpinnings for Lifelong Learning Machines. Nat. Mach. Intell. 2022, 4, 196–210. [CrossRef]
23. Kilickaya, M.; Weijer, J.V.; Asano, Y. Towards Label-Efﬁcient Incremental Learning: A survey. arXiv 2023, arXiv:2302.00353.
24. Mai, Z.; Li, R.; Jeong, J.; Quispe, D.; Kim, H.; Sanner, S. Online Continual Learning in Image Classiﬁcation: An Empirical Survey.

Neurocomputing 2022, 469, 28–51. [CrossRef]

25. Masana, M.; Twardowski, B.; Weijer, J.V. On Class Orderings for Incremental Learning. arXiv 2020, arXiv:2007.02145.
26. Qu, H.; Rahmani, H.; Xu, L.; Williams, B.; Liu, J. Recent Advances of Continual Learning in Computer Vision: An Overview.

arXiv 2021, arXiv:2109.11369.

27. Biesialska, M.; Biesialska, K.; Costajussa, M.R. Continual Lifelong Learning in Natural Language Processing: A survey. In Proceed-
ings of the 28th International Conference on Computational Linguistics, Barcelona, Spain, 8–13 December 2020; pp. 6523–6541.

28. Ke, Z.; Liu, B. Continual Learning of Natural Language Processing Tasks: A Survey. arXiv 2022, arXiv:2211.12701.
29. Khetarpal, K.; Riemer, M.; Rish, I.; Precup, D. Towards Continual Reinforcement Learning: A Review and Perspectives. J. Artif.

Intell. Res. 2022, 75, 1401–1476. [CrossRef]

30. Rajagukguk, R.A.; Ramadhan, R.A.A.; Lee, H.J. A Review on Deep Learning Models for Forecasting Time Series Data of Solar

Irradiance and Photovoltaic Power. Energies 2020, 13, 6623. [CrossRef]

31. Cai, M.; Pipattanasomporn, M.; Rahman, S. Day-Ahead Building-Level Load Forecasts using Deep Learning vs. Traditional

Time-Series Techniques. Appl. Energy 2019, 236, 1078–1088. [CrossRef]

32. Choi, K.; Yi, J.; Park, C.; Yoon, S. Deep Learning for Anomaly Detection in Time-Series Data: Review, Analysis, and Guidelines.

IEEE Access 2021, 9, 120043–120065.

33. Deng, A.; Hooi, B. Graph Neural Network-Based Anomaly Detection in Multivariate Time Series.

In Proceedings of the

34.
35.

Thirty-Fifth AAAI Conference on Artiﬁcial Intelligence, Online, 2–9 February 2021.
Jiang, W. Time Series Classiﬁcation: Nearest Neighbor versus Deep Learning Models. SN Appl. Sci. 2020, 2, 721.
Ismail Fawaz, H.; Forestier, G.; Weber, J.; Idoumghar, L.; Muller, P.A. Deep Learning for Time Series Classiﬁcation: A Review.
Data Min. Knowl. Discov. 2019, 33, 917–963.

36. Han, T.; Sanchez-Azofeifa, G.A. A Deep Learning Time Series Approach for Leaf and Wood Classiﬁcation from Terrestrial LiDAR

Point Clouds. Remote Sens. 2022, 14, 3157. [CrossRef]

37. Campos-Taberner, M.; García-Haro, F.J.; Martínez, B.; Izquierdo-Verdiguier, E.; Atzberger, C.; Camps-Valls, G.; Gilabert, M.A.

Understanding Deep Learning in Land Use Classiﬁcation Based on Sentinel-2 Time Series. Sci. Rep. 2020, 10, 17188.

38. Naqvi, R.A.; Arsalan, M.; Rehman, A.; Rehman, A.U.; Loh, W.K.; Paul, A. Deep Learning-Based Drivers Emotion Classiﬁcation

System in Time Series Data for Remote Applications. Remote Sens. 2020, 12, 587. [CrossRef]

39. Zheng, J.; Huang, M. Trafﬁc Flow Forecast through Time Series Analysis Based on Deep Learning. IEEE Access 2020, 8, 82562–82570.

[CrossRef]

40. Hua, Y.; Zhao, Z.; Li, R.; Chen, X.; Liu, Z.; Zhang, H. Deep Learning with Long Short-Term Memory for Time Series Prediction.

IEEE Commun. Mag. 2019, 57, 114–119. [CrossRef]

41. Chen, B.; Liu, Y.; Zhang, C.; Wang, Z. Time Series Data for Equipment Reliability Analysis with Deep Learning. IEEE Access 2020,

8, 105484–105493. [CrossRef]

42. Lim, B.; Zohren, S. Time Series Forecasting with Deep Learning: A Survey. Phil. Trans. R. Soc. A 2021, 379, 20200209.
43. Yasrab, R.; Zhang, J.; Smyth, P.; Pound, M. Predicting Plant Growth from Time-Series Data Using Deep Learning. Remote Sens.

2021, 13, 331. [CrossRef]

44. El-Sappagh, S.; Abuhmed, T.; Riazul Islam, S.M.; Kwak, K.S. Multimodal Multitask Deep Learning Model for Alzheimer’s Disease

Progression Detection Based on Time Series Data. Neurocomputing 2020, 412, 197–215.

45. Lara-Benitez, P.; Carranza-Garcia, M.; Riquelme, J. An Experimental Review on Deep Learning Architectures for Time Series

Forecasting. Int. J. Neural Syst. 2021, 31, 2130001. [CrossRef]

46. Cao, D.; Wang, Y.; Duan, J.; Zhang, C.; Zhu, X.; Huang, C.; Tong, Y.; Xu, B.; Bai, J.; Tong, J.; et al. Spectral Temporal Graph Neural
Network for Multivariate Time-series Forecasting. In Proceedings of the 34th Conference on Neural Information Processing
Systems, Vancouver, BC, Canada, 6–12 December 2020.

47. Torres, J.F.; Troncoso, A.; Koprinska, I.; Wang, Z.; Martínez-Álvarez, F. Deep Learning for Big Data Time Series Forecasting Applied
to Solar Power. In Proceedings of the International Joint Conference SOCO’18-CISIS’18-ICEUTE’18. SOCO’18-CISIS’18-ICEUTE’18
2018, San Sebastián, Spain, 6–8 June 2018; Advances in Intelligent Systems and Computing. Springer: Cham, Switzerland, 2019;
Volume 771.

48. Xiao, C.; Chen, N.; Hu, C.; Wang, K.; Xu, Z.; Gai, Y.; Xu, L.; Chen, Z.; Gong, J. A Spatiotemporal Deep Learning Model for Sea
Surface Temperature Field Prediction using Time-series Satellite Data. Environ. Model. Softw. 2019, 120, 104502. [CrossRef]
49. Dau, H.A.; Keogh, E.; Kamgar, K.; Yeh, C.C.M.; Zhu, Y.; Gharghabi, S.; Ratanamahatana, C.A.; Chen, Y.; Hu, B.; Begum, N.; et al.
The UCR Time Series Classiﬁcation Archive. 2018. Available online: https://www.cs.ucr.edu/~eamonn/time_series_data_2018/
(accessed on 20 May 2023).
Jaeger, H.; Haas, H. Harnessing Nonlinearity: Predicting Chaotic Systems and Saving Energy in Wireless Communication. Science
2004, 304, 78–80.

50.

51. Bagnall, A.; Lines, J.; Bostrom, A.; Large, J.; Keogh, E. The Great Time Series Classiﬁcation Bake off: A Review and Experimental

Evaluation of Recent Algorithmic Advances. Data Min. Knowl. Discov. 2017, 31, 606–660. [PubMed]

---

<!-- PAGE 29 -->

Sensors 2023, 23, 7167

29 of 32

52. Baydogan, M.G. Multivariate Time Series Classiﬁcation Datasets. 2015. Available online: http://www.mustafabaydogan.com

(accessed on 28 February 2019).

53. Borovykh, A.; Bohte, S.; Oosterlee, C.W. Conditional Time Series Forecasting with Convolutional Neural Networks. arXiv 2017,

arXiv:1703.04691.

54. Torres, J.F.; Hadjout, D.; Sebaa, A.; Martinez-Alvarez, F.; Troncoso, A. Deep Learning for Time Series Forecasting: A Survey. Big

Data 2021, 9, 3–21. [PubMed]

55. Climate Commission. The Critical Decade: Australia’s Future—Solar Energy; Climate Commission: Manila, Philippines, 2013.
56. Chollet, F.; Allaire, J. Deep Learning with R; Manning Publications: Shelter Island, NY, USA, 2018.
57.

Fan, C.; Wang, J.; Gang, W.; Li, S. Assessment of deep recurrent neural network-based strategies for short-term building energy
predictions. Appl. Energy 2019, 236, 700–710. [CrossRef]

58. Barrera-Animas, A.Y.; Oyedele, L.O.; Bilal, M.; Akinosho, T.D.; Delgado, J.M.D.; Akanbi, L.A. Rainfall prediction: A comparative

59.

analysis of modern machine learning algorithms for time-series forecasting. Mach. Learn. Appl. 2022, 7, 100204.
Smyl, S. A Hybrid Method of Exponential Smoothing and Recurrent Neural Networks for Time Series Forecasting. Int. J. Forecast.
2020, 36, 75–85. [CrossRef]

60. Dang, H.V.; MKohsin, R.; Nguyen, T.V.; Bui-Tien, T.; Nguyen, H.X. Deep Learning-Based Detection of Structural Damage using

Time-Series Data. Structure and Infrastructure Engineering. Struct. Infrastruct. Eng. 2021, 17, 1474–1493. [CrossRef]

61. Hochreiter, S.; Schmidhuber, J. Long Short-Term Memory. Neural Comput. 1997, 9, 1735–1780. [CrossRef]
62. Cho, K.; Van Merrienboer, B.; Gulcehre, C.; Bahdanau, D.; Bougares, F.; Schwenk, H.; Bengio, Y. Learning phrase representations
using RNN encoder-decoder for statistical machine translation. In Proceedings of the 2014 Conference on Empirical Methods in
Natural Language Processing (EMNLP), Doha, Qatar, 14–21 October 2014; pp. 1724–1734.

63. Wang, F.; Yu, Y.; Zhang, Z.; Li, J.; Zhen, Z.; Li, K. Wavelet Decomposition and Convolutional LSTM Networks Based Improved

Deep Learning Model for Solar Irradiance Forecasting. Appl. Sci. 2018, 8, 1286. [CrossRef]

64. He, K.; Zhang, X.; Ren, S.; Sun, J. Deep Residual Learning for Image Recognition. Indian J. Chem.-Sect. B Org. Med. Chem. 2015, 45,

1951–1954.

65. Uhlig, S.; Quoitin, B.; Lepropre, J.; Balon, S. Providing Public Intradomain Trafﬁc Matrices to the Research Community. SIGCOMM

66.

Comput. Commun. Rev. 2006, 36, 83–86. [CrossRef]
Shi, X.; Chen, Z.; Wang, H.; Yeung, D.Y.; Wong, W.K.; Woo, W.C. Convolutional LSTM Network: A Machine Learning Approach
for Precipitation nowcasting. Adv. Neural Inf. Process. Syst. 2015, 28, 802–810.

67. Yamashita, R.; Nishio, M.; Do, R.K.G.; Togashi, K. Convolutional Neural Networks: An Overview and Application in Radiology.

68.

Insights Imaging 2018, 9, 611–629. [PubMed]
Scarselli, F.; Gori, M.; Tsoi, A.C.; Hagenbuchner, M. The Graph Neural Network Model. IEEE Trans. Neural Netw. 2009, 20, 61–80.
[CrossRef] [PubMed]

69. Velickovic, P.; Cucurull, G.; Casanova, A.; Romero, A.; Lio, P.; Bengio, Y. Graph Attention Networks. arXiv 2017, arXiv:1710.10903.
70. Hinton, G.E.; Osindero, S.; Teh, Y.-W. A Fast Learning Algorithm for Deep Belief Nets. Neural Comput. 2006, 18, 1527–1554.

[CrossRef]

71. Ma, M.; Sun, C.; Chen, X. Deep Coupling Autoencoder for Fault Diagnosis with Multimodal Sensory Data. IEEE Trans. Ind.

Inform. 2018, 14, 1137–1145. [CrossRef]

72. Lei, Y.; Karimi, H.R.; Cen, L.; Chen, X.; Xie, Y. Processes soft modeling based on stacked autoencoders and wavelet extreme

learning machine for aluminum plant-wide application. Control Eng. Pract. 2021, 108, 104706. [CrossRef]

73. Mohammdi Farsani, E.; Pazouki, E. A Transformer Self Attention Model for Time Series Forecasting. J. Electr. Comput. Eng. Innov.

2021, 9, 1–10.

74. Elsayed, S.; Thyssens, D.; Rashed, A.; Jomaa, H.S.; Schmidt-Thieme, L. Do We Really Need Deep Learning Models for Time Series

Forecasting? arXiv 2021, arXiv:2101.02118v2.

75. Kanani, P.; Padole, M. ECG Heartbeat Arrhythmia Classiﬁcation Using Time-Series Augmented Signals and Deep Learning

Approach. Procedia Comput. Sci. 2020, 171, 524–531. [CrossRef]

76. Kisa, D.H.; Ozdemir, M.A.; Guren, O.; Akan, A. EMG based Hand Gesture Classiﬁcation using Empirical Mode Decom-
In Proceedings of the 2020 Medical Technologies Congress, Antalya, Turkey,

position Time-Series and Deep Learning.
19–20 November 2020.

77. Castro Filho, H.C.; Carvalho Junior, O.A.; Carvalho, O.L.F.; Bem, P.P.; Moura, R.S.; Albuquerque, A.O.; Silva, C.R.; Ferreira, P.H.G.;
Guimaraes, R.F.; Gomes, R.A.T. Rice Crop Detection Using LSTM, Bi-LSTM, and Machine Learning Models from Sentinel-1 Time
Series. Remote Sens. 2020, 12, 2655. [CrossRef]

78. RuBwurm, M.; Korner, M. Self-Attention for Raw Optical Satellite Time Series Classiﬁcation. J. Photogramm. Remote Sens. 2020,

169, 421–435.

79. Kingphai, K.; Moshfeghi, Y. EEG-based Mental Workload Level Estimation using Deep Learning Models. In Ergonomics & Human

Factors; CIEHF: Birmingham, UK, 2022.

80. Yokkampon, U.; Mowshowitz, A.; Chumkamon, S.; Hayashi, E. Robust Unsupervised Anomaly Detection with Variational

Autoencoder in Multivariate Time Series Data. IEEE Access 2022, 10, 57835–57849. [CrossRef]

81. Mishra, S.; Bordin, C.; Taharaguchi, K.; Palu, I. Comparison of Deep Learning Models for Multivariate Prediction of Time Series

Wind Power Generation and Temperature. Energy Rep. 2020, 6, 273–286. [CrossRef]

---

<!-- PAGE 30 -->

Sensors 2023, 23, 7167

30 of 32

82. Wen, Q.S.; Sun, L.; Yang, F.; Song, X.; Gao, J.; Wang, X.; Xu, H. Time Series Data Augmentation for Deep Learning: A Survey.
In Proceedings of the Thirtieth International Joint Conference on Artiﬁcial Intelligence (IJCAI-21), Montréal, QC, Canada,
19–27 August 2021; pp. 4653–4660.

83. Azar, J.; Makhoul, A.; Couturier, R.; Demerjian, J. Robust IoT Time Series Classiﬁcation with Data Compression and Deep

84.

Learning. Neurocomputing 2020, 398, 222–234. [CrossRef]
Savitzky, A.; Golay, M.J.E. Smoothing and Dierentiation of Data by Simpliﬁed Least Squares Procedures. Anal. Chem. 1964, 36,
1627–1639. [CrossRef]

85. Vaswani, A.; Shazeer, N.; Parmar, N.; Uszkoreit, J.; Jones, L.; Gomez, A.N.; Kaiser, L.; Polosukhin, I. Attention is all you
need. In Proceedings of the Advances in Neural Information Processing Systems, Long Beach, CA, USA, 4–9 December 2017;
pp. 5998–6008.

86. Mognon, A.; Jovicich, J.; Bruzzone, L.; Buiatti, M. Adjust: An Automatic EEG Artifact Detector Based on the Joint Use of Spatial

and Temporal Features. Psychophysiology 2011, 48, 229–240.

87. Kingphai, K.; Moshfeghi, Y. On EEG Preprocessing Role in Deep Learning Effectiveness for Mental Workload Classiﬁcation.
In International Symposium on Human Mental Workload: Models and Applications; Springer: Berlin/Heidelberg, Germany, 2021;
pp. 81–98.

88. Chalapathy, R.; Chawla, S. Deep Learning for Anomaly Detection: A Survey. arXiv 2019, arXiv:1901.03407.
89. Le, T.T.; Fu, W.; Moore, J.H. Scaling Tree-Based Automated Machine Learning to Biomedical Big Data with a Feature Set Selector.

Bioinformatics 2020, 36, 250–256. [CrossRef]

90. Bahdanau, D.; Cho, K.; Bengio, Y. Neural Machine Translation by Jointly Learning to Align and Translate. arXiv 2014,

arXiv:1409.0473.

91. Livieris, I.; Stavroyiannis, S.; Iliadis, L.; Pintelas, P. Smoothing and Stationarity Enforcement Framework for Deep Learning

Time-Series Forecasting. Neural Comput. Appl. 2021, 33, 14021–14035. [CrossRef] [PubMed]

92. He, Y.; Huang, Z.; Sick, B. Toward Application of Continuous Power Forecasts in a Regional Flexibility Market. In Proceedings of

the 2021 International Joint Conference on Neural Networks (IJCNN), Shenzhen, China, 18–22 July 2021; pp. 1–8.

93. Kiyasseh, D.; Zhu, T.; Clifton, D. A Clinical Deep Learning Framework for Continually Learning from Cardiac Signals across

Diseases, Time, Modalities, and Institutions. Nat. Commun. 2021, 12, 4221. [CrossRef]

94. Gupta, V.; Narwariya, J.; Malhotra, P.; Vig, L.; Shroff, G. Continual Learning for Multivariate Time Series Tasks with Variable
Input Dimensions. In Proceedings of the 2021 IEEE International Conference on Data Mining (ICDM), Auckland, New Zealand,
7–10 December 2021; pp. 161–170.
Flesch, T.; Balaguer, J.; Dekker, R.; Nili, H.; Summerﬁeld, C. Comparing Continual Task Learning in Minds and Machines. Proc.
Natl. Acad. Sci. USA 2018, 115, E10313–E10322. [CrossRef] [PubMed]
Shaheen, K.; Hanif, M.A.; Hasan, O.; Shaﬁque, M. Continual Learning for Real-World Autonomous Systems: Algorithms,
Challenges and Frameworks. J. Intell. Robot. Syst. 2022, 105, 9.

96.

95.

97. Pfulb, B.; Gepperth, A. A Comprehensive, Application-Oriented Study of Catastrophic Forgetting in DNNs. In Proceedings of the

International Conference on Learning Representations (ICLR), New Orleans, LA, USA, 6–9 May 2019.

98. Prabhu, A.; Torr, P.; Dokania, P. Gdumb: A Simple Approach that Questions Our Progress in Continual Learning. In European

Conference on Computer Vision; Springer: Berlin/Heidelberg, Germany, 2020; pp. 524–540.

99. He, Y.; Sick, B. CLeaR: An Adaptive Continual Learning Framework for Regression Tasks. AI Perspect. 2021, 3, 2.
100. Philps, D.; Weyde, T.; Garcez, A.D.A.; Batchelor, R. Continual Learning Augmented Investment Decisions. arXiv 2019,

arXiv:1812.02340v4.

101. Chen, X.; Wang, J.; Xie, K. TrafﬁcStream: A Streaming Trafﬁc Flow Forecasting Framework Based on Graph Neural Networks
and Continual Learning. In Proceedings of the Thirtieth International Joint Conference on Artiﬁcial Intelligence, Montreal, QC,
Canada, 19–27 August 2021.

102. Lesort, T.; George, T.; Rish, I. Continual learning in Deep Neural Networks: An Analysis of the Last Layer. arXiv 2021,

arXiv:2106.01834.

103. Mundt, M.; Hong, Y.; Pliushch, I.; Ramesh, V. A Wholistic View of Continual Learning with Deep Neural Networks: Forgotten

Lessons and the Bridge to Active and Open World Learning. Neural Netw. 2023, 160, 306–336.

104. Bagus, B.; Gepperth, A.; Lesort, T. Beyond Supervised Continual Learning: A Review. In Proceedings of the European Symposium

on Artiﬁcial Neural Networks, Computational Intelligence and Machine Learning, Bruges, Belgium, 5–7 October 2022.

105. Pham, Q.; Liu, C.; Sahoo, D.; Hoi, S.C. Learning Fast and Slow for Online Time Series Forecasting. arXiv 2022, arXiv:2202.11672v2.
106. Xiao, Y.; Liu, M.; Zhang, Z.; Jiang, L.; Yin, M.; Wang, J. Streaming Trafﬁc Flow Prediction Based on Continuous Reinforcement

Learning. arXiv 2022, arXiv:2212.12767v1.

107. Sah, R.K.; Mirzadeh, S.I.; Ghasemzadeh, H. Continual Learning for Activity Recognition. In Proceedings of the 2022 44th
Annual International Conference of the IEEE Engineering in Medicine & Biology Society (EMBC), Scotland, UK, 11–15 July 2022;
pp. 2416–2420.

108. Matteoni, F.; Cossu, A.; Gallicchio, C.; Lomonaco, V.; Bacciu, D. Continual Learning for Human State Monitoring. In Proceedings
of the ESANN 2022 Proceedings, European Symposium on Artiﬁcial Neural Networks, Computational Intelligence and Machine
Learning, Bruges, Belgium, 5–7 October 2022.

---

<!-- PAGE 31 -->

Sensors 2023, 23, 7167

31 of 32

109. Kwon, Y.D.; Chauhan, J.; Kumar, A.; Hui, P.; Mascolo, C. Exploring System Performance of Continual Learning for Mobile and
Embedded Sensing Applications. In Proceedings of the 2021 IEEE/ACM Symposium on Edge Computing (SEC), San Jose, CA,
USA, 14–17 December 2021; pp. 319–332.

110. Cossu, A.; Carta, A.; Lomonaco, V.; Bacciu, D. Continual Learning for Recurrent Neural Networks: An Empirical Evaluation.

Neural Netw. 2021, 143, 607–627. [CrossRef] [PubMed]

111. He, Y. Adaptive Explainable Continual Learning Framework for Regression Problems with Focus on Power Forecasts. arXiv 2022,

arXiv:2108.10781v2.

112. Doshi, K.; Yilmaz, Y. Rethinking Video Anomaly Detection—A Continual Learning Approach. In Proceedings of the 2022
IEEE/CVF Winter Conference on Applications of Computer Vision (WACV), Waikoloa, HI, USA, 4–8 January 2022; pp. 3036–3045.
113. Maschler, B.; Pham, T.T.H.; Weyrich, M. Regularization-based Continual Learning for Anomaly Detection in Discrete Manufac-
turing. In Proceedings of the 54th CIRP Conference on Manufacturing Systems, Procedia CIRP, Virtual, 22–24 September 2021;
Volume 104, pp. 452–457.

114. Maschler, B.; Vietz, H.; Jazdi, N.; Weyrich, M. Continual Learning of Fault Prediction for Turbofan Engines using Deep Learning
with Elastic Weight Consolidation. In Proceedings of the 2020 25th IEEE International Conference on Emerging Technologies and
Factory Automation, Vienna, Austria, 8–11 September 2020; pp. 959–966.

115. Bayram, B.; Ince, G. Real Time Auditory Scene Analysis using Continual Learning in Real Environments. Eur. J. Sci. Technol. 2020,

215–226, Ejosat Special Issue 2020 (HORA). [CrossRef]

116. Schillaci, G.; Schmidt, U.; Miranda, L. Prediction Error-Driven Memory Consolidation for Continual Learning: On the Case of

Adaptive Greenhouse Models. KI—Künstliche Intell. 2021, 35, 71–80.

117. Knoblauch, J.; Husain, H.; Diethe, T. Optimal Continual Learning has Perfect Memory and is NP-HARD. In Proceedings of the

37th International Conference on Machine Learning, Virtual, 13–18 July 2020; pp. 5327–5337.

118. Kirkpatrick, J.; Pascanu, R.; Rabinowitz, N.; Veness, J.; Desjardins, G.; Rusu, A.A.; Milan, K.; Quan, J.; Ramalho, T.; Grabska-
Barwinska, A.; et al. Overcoming Catastrophic Forgetting in Neural Networks. Proc. Natl. Acad. Sci. USA 2017, 114, 3521–3526.
[CrossRef]

119. Li, Z.; Hoiem, D. Learning without Forgetting. IEEE Trans. Pattern Anal. Mach. Intell. 2017, 40, 2935–2947. [CrossRef]
120. Wei, H.R.; Huang, S.; Wang, R.; Dai, X.; Chen, J. Online Distilling from Checkpoints for Neural Machine Translation. In Proceedings
of the 2019 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language
Technologies, Minneapolis, MN, USA, 2–7 June 2019; Volume 1, pp. 1932–1941.

121. Chaudhry, A.; Ranzato, M.; Rohrbach, M.; Elhoseiny, M. Efﬁcient Lifelong Learning with A-GEM. In Proceedings of the

International Conference on Learning Representations, Vancouver, Canada, 30 April-3 May 2018.

122. Chaudhry, A.; Rohrbach, M.; Elhoseiny, M.; Ajanthan, T.; Dokania, P.K.; Torr, P.H.S.; Ranzato, M. On Tiny Episodic Memories in

Continual Learning. arXiv 2019, arXiv:1902.10486.

123. Mirzadeh, S.I.; Farajtabar, M.; Gorur, D.; Pascanu, R.; Ghasemzadeh, H. Linear Mode Connectivity in Multitask and Contin-
ual Learning. In Proceedings of the ICLR 2021: The Ninth International Conference on Learning Representations, Virtual,
3–7 May 2021.

124. Reiss, A.; Stricker, D. Introducing a New Benchmarked Dataset for Activity Monitoring. In Proceedings of the 16th International

Symposium on Wearable Computers, Newcastle UK, 18–22 June 2012; pp. 108–109.

125. Schmidt, P.; Reiss, A.; Duerichen, R.; Marberger, C.; Van Laerhoven, K. Introducing WESAD, a Multimodal Dataset for Wearable
Stress and Affect Detection. In Proceedings of the 20th ACM International Conference on Multimodal Interaction, ICMI 2018,
New York, NY, USA, 16–20 October 2018; pp. 400–408.

126. Subramanian, R.; Wache, J.; Abadi, M.K.; Vieriu, R.L.; Winkler, S.; Sebe, N. ASCERTAIN: Emotion and Personality Recognition

using Commercial Sensors. IEEE Trans. Affect. Comput. 2018, 9, 147–160. [CrossRef]

127. Lee, S.W.; Kim, J.H.; Jun, J.; Ha, J.W.; Zhang, B.T. Overcoming Catastrophic Forgetting by Incremental Moment Matching.
In Advances in Neural Information Processing Systems; Curran Associates, Inc.: Red Hook, NY, USA, 2017; Volume 30, pp. 4652–4662.
128. Maschler, B.; Tatiyosyan, S.; Weyrich, M. Regularization-Based Continual Learning for Fault Prediction in Lithium-Ion Batteries.

Procedia CIRP 2022, 112, 513–518. [CrossRef]

129. Eker, O.; Camci, F.; Jennions, I. Major Challenges in Prognostics: Study on Benchmarking Prognostics Datasets. In Proceedings
of the 2012 1st European Conference of the Prognostics and Health Management Society, Dresden, Germany, 3–6 July 2012;
pp. 148–155.

130. Gonzalez, G.G.; Casas, P.; Fernandez, A.; Gomez, G. Steps towards Continual Learning in Multivariate Time-Series Anomaly
Detection using Variational Autoencoders. In Proceedings of the 22nd ACM Internet Measurement Conference, IMC ’22, Nice,
France, 25–27 October 2022.

131. Saxena, A.; Goebel, K. Turbofan Engine Degradation Simulation Data Set; NASA Ames Prognostics Data Repository: Moffett Field,

CA, USA, 2008.

132. Glymour, C.; Zhang, K.; Spirtes, P. Review of Causal Discovery Methods Based on Graphical Models. Front. Genet. 2019, 10, 524.

[CrossRef] [PubMed]

133. Castri, L.; Mghames, S.; Bellotto, N. From Continual Learning to Causal Discovery in Robotics. arXiv 2023, arXiv:2301.03886v1.
134. Lopez-Paz, D.; Ranzato, M. Gradient Episodic Memory for Continual Learning. Adv. Neural. Inf. Process. Syst. 2017, 30, 6467–6476.

---

<!-- PAGE 32 -->

Sensors 2023, 23, 7167

32 of 32

135. Aljundi, R.; Caccia, L.; Belilovsky, E.; Caccia, M.; Lin, M.; Charlin, L.; Tuytelaars, T. Online Continual Learning with Maximal

Interfered Retrieval. Adv. Neural. Inf. Process. Syst. 2019, 32, 11849–11860.

136. Mnih, V.; Kavukcuoglu, K.; Silver, D.; Rusu, A.A.; Veness, J.; Bellemare, M.G.; Graves, A.; Riedmiller, M.; Fidjeland, A.K.;
Ostrovski, G.; et al. Human-Level Control through Deep Reinforcement Learning. Nature 2015, 518, 529–533. [CrossRef]
137. Bengio, E.; Pineau, J.; Precup, D. Interference and Generalization in Temporal Difference Learning. arXiv 2020, arXiv:2003.06350.
138. Atkinson, C.; McCane, B.; Szymanski, L.; Robins, A. Pseudo-Rehearsal: Achieving Deep Reinforcement Learning without

Catastrophic Forgetting. Neurocomputing 2021, 428, 291–307.

139. Rusu, A.A.; Rabinowitz, N.C.; Desjardins, G.; Soyer, H.; Kirkpatrick, J.; Kavukcuoglu, K.; Pascanu, R.; Hadsell, R. Progressive

Neural Networks. arXiv 2016, arXiv:1606.04671.

140. Yoon, J.; Yang, E.; Lee, J.; Hwang, S.J. Lifelong Learning with Dynamically Expandable Networks. arXiv 2017, arXiv:1708.01547.
141. He, Y.; Huang, Z.; Sick, B. Design of Explainability Module with Experts in the Loop for Visualization and Dynamic Adjustment
In Proceedings of the AAAI-22 Workshop on Interactive Machine Learning, Vancouver, Canada,

of Continual Learning.
28 February-1 March 2022.

142. Tercan, H.; Deibert, P.; Meisen, T. Continual Learning of Neural Networks for Quality Prediction in Production Using Memory

Aware Synapses and Weight Transfer. J. Intell. Manuf. 2022, 33, 283–292. [CrossRef]

143. Altun, K.; Barshan, B. Human Activity Recognition using Inertial/Magnetic Sensor Units. In International Workshop on Human

Behavior Understanding; Springer: Berlin/Heidelberg, Germany, 2010; pp. 38–51.

144. Anguita, D.; Ghio, A.; Oneto, L.; Parra, X.; Reyes-Ortiz, J.L. Human Activity Recognition on Smartphones using a Multiclass
Hardware-Friendly Support Vector Machine. In International Workshop on Ambient Assisted Living; Springer: Berlin/Heidelberg,
Germany, 2012; pp. 216–223.

145. Saxena, A.; Goebel, K.; Simon, D.; Eklund, N. Damage Propagation Modeling for Aircraft Engine Run-to-Failure Simulation.
In Proceedings of the 2008 International Conference on Prognostics and Health Management, Denver, CO, USA, 6–9 October
2008; pp. 1–9.

Disclaimer/Publisher’s Note: The statements, opinions and data contained in all publications are solely those of the individual
author(s) and contributor(s) and not of MDPI and/or the editor(s). MDPI and/or the editor(s) disclaim responsibility for any injury to
people or property resulting from any ideas, methods, instructions or products referred to in the content.

<!-- MARKITDOWN CONVERSION -->

<!-- Full MarkItDown conversion for formatting fidelity. -->

sensors
SystematicReview
Continual Deep Learning for Time Series Modeling
Sio-IongAo1,*andHaythamFayek2
1 InternationalAssociationofEngineers,Unit1,1/F,HungToRoad,HongKong
2 SchoolofComputingTechnologies,RMITUniversity,Building14,Melbourne,VIC3000,Australia;
haytham.fayek@rmit.edu.au
* Correspondence:siao@graduate.hku.hk
Abstract:Themulti-layerstructuresofDeepLearningfacilitatetheprocessingofhigher-levelabstrac-
tionsfromdata,thusleadingtoimprovedgeneralizationandwidespreadapplicationsindiverse
domainswithvarioustypesofdata.Eachdomainanddatatypepresentsitsownsetofchallenges.
Real-world time series data may have a non-stationary data distribution that may lead to Deep
Learningmodelsfacingtheproblemofcatastrophicforgetting,withtheabruptlossofpreviously
learnedknowledge.Continuallearningisaparadigmofmachinelearningtohandlesituationswhen
thestationarityofthedatasetsmaynolongerbetrueorrequired.Thispaperpresentsasystematic
reviewoftherecentDeepLearningapplicationsofsensortimeseries,theneedforadvancedprepro-
cessingtechniquesforsomesensorenvironments,aswellasthesummariesofhowtodeployDeep
Learningintimeseriesmodelingwhilealleviatingcatastrophicforgettingwithcontinuallearning
methods.Theselectedcasestudiescoverawidecollectionofvarioussensortimeseriesapplications
andcanillustratehowtodeploytailor-madeDeepLearning,advancedpreprocessingtechniques,
andcontinuallearningalgorithmsfrompractical,real-worldapplicationaspects.
Keywords: deeplearning; continuallearning; sensor; timeseries; preprocessing; non-stationary;
catastrophicforgetting
1. Introduction
Time series modeling is a challenging task in data mining and machine learning.
Citation:Ao,S.-I.;Fayek,H.
Populartimeseriesmodelingtasksincludeclassification,anomalydetection,regression,
ContinualDeepLearningforTime
SeriesModeling.Sensors2023,23, forecasting,andclustering. Atimeseriesisasequenceofmeasurementstakenatvarious
7167. https://doi.org/10.3390/ times. Spatialtimeseriesdatareferstomultipletimeseriesdatacorrespondingtodifferent
s23167167 spatiallocations. Thespatial–temporalmodelsfacedifficultiesinaddressingnotonlythe
short-termandlong-termpatternsbutalsothespatialpatterns[1]. Timeseriesdatasets
AcademicEditors:ChimanKwan
have the property of temporal ordering by nature [2]. Generally speaking, time series
andAnabelaOliveira
modelshavethecapabilitytoutilizethefactthatobservationsclosertogetherintimerelate
Received:12June2023 moreclosely. Timeseriesmodelinghasmanyreal-worldapplicationslikeenvironmentand
Revised:31July2023 traffictasks,andsuccessfulmodelingforthetimeserieshasbecomeincreasinglyimportant.
Accepted:10August2023 Forexample,windtimeseriesforecastingisessentialforthedecision-makingofelectric
Published:14August2023 systemoperators.
Time series analysismodels can be dividedbroadlyinto time domain modelsand
frequency domain models. The time domain model investigates the data with respect
totime,whilethefrequencydomainmodelsfocustheanalysisonfrequencyinsteadof
Copyright: © 2023 by the authors.
time[2]. Statisticalmodelslikeautoregressivemodelsandthemovingaveragemodelsare
Licensee MDPI, Basel, Switzerland.
populartimedomainmodels. Preprocessingoperationslikedatacleaning,normalization,
This article is an open access article
differencing,featureselection,etc.,arealsopopulartimedomainmodels. Forthefrequency
distributed under the terms and
domain methods, mathematical models are employed to convert the time series data
conditionsoftheCreativeCommons
between the time and frequency domains. The Fourier transform is a popular, simple,
Attribution(CCBY)license(https://
andbasictransformingtoolforcomputingthefrequencydomainrepresentationofatime
creativecommons.org/licenses/by/
4.0/).
Sensors2023,23,7167.https://doi.org/10.3390/s23167167 https://www.mdpi.com/journal/sensors

Sensors2023,23,7167 2of32
series. Otherpopularpreprocessingoffrequencydomainarewavelettransformation(WT),
empiricalmodedecomposition(EMD),etc.
Overthelastdecade,smartsensorshavebeendeployedonaverylargescale,and
hugeamountsofcontinuousdatahavebeengenerated[3].Machinelearning(ML)methods
canextractvaluableinformationfromdatasetsandhavebeenwidelyemployedforsensory
data in the industry, such as in the sensing and condition monitoring fields [4]. In the
knowledgediscoveryprocess,feedbackisgeneratedateachiterationwiththegoalthat
furtherimprovementcanbeachieved[5]. DeepLearning(DL),aparticulartypeofmachine
learning algorithm with multi-layer structures for processing higher-level abstractions
fromtheinputdataset[6],isverywellsuitedforverylargedatasets,asmostofitslayer
computationscanbeimplementedinparallelanddistributedcomputingtechniquescanbe
appliedeasily. DeepLearningmodelshavebeenshowntoperformsatisfactorilyformany
timeseriesanalysistaskslikeforecasting.
DeepLearning(DL)hasbeendevelopedfromtraditionalneuralnetworkswithlarge-
sizeddeepstructuressince2006. Comparedwithtraditionalmachinelearning,DLlearns
through a general-purpose learning procedure of multiple levels of representation and
identifiesfeaturesautomatically[7]. Ineachlayer,therepresentationisobtainedfromthe
representationofthepreviouslayer,involvingupdatingprocesswithaback-propagation
algorithm. DifferentfromthemoretraditionalMLmethods,theadditionofmorelayers
intheDeepLearningmodelcanfurtherenablethedeepnetworktocopewithscenarios
ofincreasingcomplexity,thusleadingtoimprovedgeneralization. Amulti-layerlearn-
ing structure enables very high performance in complex situations like video, speech,
classificationproblems,andmulti-sensoraggregation.
Deep Learning models have been shown to perform satisfactorily for many time
seriesanalysistasks. Forexample,DeepLearninghasprovenexcellentinhumanactivity
recognition (HAR) tasks, where wearable sensors can connect people with the cyber–
physical system through HAR [8]. Deep Learning has also been employed for tipping-
point prediction, with performance better than traditional early warning systems [9].
Nevertheless, the reliability of these forecasting methods is not guaranteed [10]. Deep
Learningmethodsmayalsofacetheoverfittingproblem. Commonpreprocessingmethods
likesmoothing,transformation,andestimationcanremovethenoiseintimeseriessignalsin
advanceandimprovetheoverallperformanceofthetimeseriesmodels. Theperformance
ofDeepLearningmodelsmayimprovewithpreprocessingoftimeseriesinputs,usually
onconditionsthatthedatadistributionattesttimeissimilartothatattrainingtime.
WhenbuildingMLmodels,itisusuallyassumedthatthedistributionofthedatais
stationary. Whenthestatisticalpropertiesofatimeseriesdonotdependontime,thetime
seriesiscalledstationary[2]. Itispossiblethatatimeseriesisstationaryintermsofone
characteristicwhilenon-stationaryforanothercharacteristic. Mathematically,atimeseries
TS(y )isdefinedtobe(weakly)stationaryifalltimet:
t
E(y t )=E[(y t−1 )]=µ,
Var(y )=σ2<∞,
t
Cov(y
t
,y
t−k
)=γ(k),
where the expected value µ is represented by E(.), the variance σ2 by Var(.), and the
covarianceγbyCov(.),respectively[11]. Ifthestationaryconditionsarenolongertrue,the
non-stationarybehaviorsmayposesignificantdifficultiesfortimeseriesapplicationslike
remotesensing[12].
Inmanyreal-worldapplications,thestationarityofthedatasetsmaynolongerbetrue.
Therearefourbasiccomponentsthatcancausethenon-stationarityinsometimeseries.
Thesefourcomponentsaretrend,seasonal,cyclical,andirregularcomponents[13]. The
trendcomponentreferstolong-termincreasesordecreasesovertime,withexampleslike
long-termpopulationgrowth.Theseasonalcomponentreferstotheexistenceofseasonality

Sensors2023,23,7167 3of32
patterns, like, forexample, timeserieswithyearly, quarterly, ormonthlypatterns. The
cyclicalcomponentreferstothepatternsofupsanddownsofatimeseriesovertheduration
ofacycle. Theeconomictimeseriesdataofeconomicgrowthandtheneconomicrecession
mayhaveacyclicalcomponent. Theirregularcomponentisduetounpredictablefactors
anddoesnotrepeatwithparticularpatterns. Forsometimeseriesdatathatexhibitasimple
trend, seasonal, and cyclical components, DL methods may be deployed directly with
satisfactoryresults,asseeninthefirstpartofSection2. Forsomemorecomplicatedsensor
timeseriesdatasets,advancedpreprocessingtoolsmaybeneeded,asseeninthesecond
partofSection2. Amongthetimeseriesdatasetsthatcannotbehandledwellwithboth
advancedpreprocessingandDLmethods,somemayfitthescenariosforthedeployment
ofCLmethods,whicharedescribedindetailinSection3.
Continuallearningisaparadigmofmachinelearningthatmayhandlesomeofthe
non-stationarysituationswhileimitatingthecapabilityofhumanintelligencetohandlenew
situationsfromtheoldexperienceslearned. CLalgorithmsaredevelopedtomimichuman
intelligencethatwillrarelyforgetallofthelearnedinformation,asthenaturalsystemwill
onlygraduallylosethelearnedinformation[14]. Ontheotherhand, traditionalneural
networks(NNs),whilemimickinghumancognition,lackthisabilityandfacecatastrophic
forgetting(CF).IfDeepLearningmethodsarenaivelyemployedinCLtasks,learningon
shifteddistributionmayleadtoCFproblems. Thecapabilityofhowtolearncontinuallyis
oneofthebiggestunsolvedissuesinML[15],whileforgettinglearnedknowledgeisthe
keyobstacletocontinuallearning[16].
Thissurveyfocusessolelyonreal-worldpracticaltimeseriesapplicationswithDL
andCL.Langeetal.[17]presentedasurveyonCLaboutthestability–plasticitytrade-off
andfocusedontheproblemsofclassificationonly. Themotivationforthemtolimitthe
discussiontoclassificationaloneisthatNNhasbeenverywell-establishedforclassification
tasks. Inthesurvey[18],itwashighlightedthatthemostrecentsurveysusuallycovered
continual learning partially, like biological underpinnings [19–22], visual classification
tasks [23–26], NLP tasks [27,28], and RL [29]. Wang et al. [18] talked about only five
tasksofpracticalCLapplications,i.e.,objectdetection,semanticsegmentation,conditional
generation, reinforcement learning, and NLP. None of the above-mentioned recent CL
surveysfocusedontimeseriesanalysistasksliketimeseriesforecasting. Thefocusofthis
surveyissolelyonthecurrentapplicationcasestudiesofDLforsensortimeseriesdatasets.
ItprovidesasummaryofthedifficultiesthattheDLfacesindeploymentforreal-world
sensorapplicationsandtheadvancedpreprocessingtechniquesforhowtoaddresssomeof
thesepracticaldifficulties. TherearesomecasesthattypicalDLapproaches,togetherwith
advancedpreprocessingtechniques,canhandlewell. Nevertheless,insomeothertime
seriesapplicationcases,continuallearningisfoundtobesuitablefordeployment. The
topicofdeployingCLforsensortimeseriesmodelinghasnotbeensystemicallycoveredin
theseprevioussurveys.
Thispaperisorganizedwiththefollowingsections,coveringtherecenttimeseries
applicationsofDeepLearningandcontinuallearning. InSection2,firstly,thefocusison
thecurrentadvancesindeployingDeepLearningmethodsforsensortimeseriesmodeling.
Then,therecentsensorcasestudiesthatstillrequiredatapreprocessingtechniquesforDL
modulesarehighlighted. InSection3,asummaryofthesensortimeseriesdatasetsand
environmentsthatsuitthedeploymentofcontinuallearningmethodsisundertaken.
2. AdvancesinDeepLearningMethodsforTimeSeriesModeling
DeepLearningiscapableofmodelingthecomplexnon-linearrelationshipsamong
thevariables,whiletraditionalneuralnetworkneedstoassumethatallinputvectorsare
independent,whichmayleadtoitsineffectivenessforsequentialdataprediction[30]. Com-
paringDLwiththeconventionaltimeseriesmethods[13,31],itisfoundthatDeepLearning
modelscangivebetterrepresentationandclassification. Caietal.[31](2019)investigated
theday-aheadmulti-steploadpredictionofcommercialbuildingswithRNNandCNN
againstautoregressiveintegratedmovingaveragewithexogenousinputs(ARIMAX),a

Sensors2023,23,7167 4of32
populartraditionaltimeseriesmethodforthetimeseriesmodelingofloadforecasting.
TheresultsshowthattheCNNapproachwithadirectmulti-stepprocedurecanperform
betterthantheseasonalARIMAXbya22.6%improvementinpredictionaccuracy. This
illustratedthattheDeepLearninghierarchicalstructuremayhavethecapabilitytohan-
dledata-dependentuncertaintybetter. Itisalsoshownthatthelong-termtrendscanbe
exploredbetterwhenthepreprocessingtoolofthemovingaveragesmethodisdeployed
forsmoothingtheshort-termfluctuations. MahmoudandMohammed[13]presenteda
surveyofDeepLearningmodels,suchasCNN,RNN,LSTM,GRU,deepautoencoders
(AEs),restrictedBoltzmannmachines(RBM),deepbeliefnetworks(DBNs),inthetime
seriesforecastingofelectricityloadandprice,solarpower,andfinance,withcomparison
resultsshowingthatDLperformsbetterthanclassicalmethods.
AfterdiscussingtheadvantagesofdeployingDLmethodswithtimeseriesdata,the
followingTable1showsasyntheticsummaryoftheadvancesinDeepLearningtechniques
forreal-worldsensortimeseriesapplications,followedbyadetaileddescriptionofthe
corresponding methods, motivations, and advantages. The following Figure 1 shows
the tree diagram grouping the popular Deep Learning methods for sensor time series
classificationandforecastingtaskscoveredinthissurvey.
Table1.SummaryoftheadvancesinDLtechniquesforsensortimeseriesapplications.
|                  | Application |          | DeepLearning |          |         |
| ---------------- | ----------- | -------- | ------------ | -------- | ------- |
| Ref. FirstAuthor | Year        | Datasets |              | Accuracy | Details |
|                  | Field       |          | Models       |          |         |
Watertreatment
CompareDLanomaly
|     | Timeseries | test-bed,water |                 | Noclear |                     |
| --- | ---------- | -------------- | --------------- | ------- | ------------------- |
|     |            |                | RNN,CNN,hybrid, |         | detectiontimeseries |
[32] Choi 2021 anomaly distributionpipelines, one-size-fits-all
|     |           |             | attention |        | modelswith |
| --- | --------- | ----------- | --------- | ------ | ---------- |
|     | detection | MarsScience |           | method |            |
benchmarkdatasets
Laboratoryrover
|           | Detecting     | Sensortimeseries |                | 54%better        | Combinegraphneural |
| --------- | ------------- | ---------------- | -------------- | ---------------- | ------------------ |
|           | deviationfrom | datasetsofwater  | GraphDeviation |                  | networkswith       |
| [33] Deng | 2021          |                  |                | F-measurethanthe |                    |
|           | normal        | treatmentsystems | Network        |                  | structuredlearning |
nextbestbaseline
|     | patterns | (SWaTandWADI) |     |     | approach |
| --- | -------- | ------------- | --- | --- | -------- |
Notsignificantly
Conductcomparison
betterthan1-NN
|            | Timeseries     | UCRTimeSeries         | MLP,CNN, |                 | betweennearest |
| ---------- | -------------- | --------------------- | -------- | --------------- | -------------- |
| [34] Jiang | 2020           |                       |          | classifierswith |                |
|            | classification | ClassificationArchive | ResNet   |                 | neighborandDL  |
dynamictime
models
warping
SOAperformance
Univariate
|                  | Timeseries     |                      | MLP,CNN,Echo | achievedwith | Conductempirical  |
| ---------------- | -------------- | -------------------- | ------------ | ------------ | ----------------- |
| [35] IsmailFawaz | 2019           | timeseriesdatasetsof |              |              |                   |
|                  | classification |                      | StateNetwork | CNNanddeep   | studyofDNNsforTSC |
theUCR/UEAarchive
ResidualNetworks
|     | Leafandwood |     |     | Accurate | CompareDLmodels |
| --- | ----------- | --- | --- | -------- | --------------- |
Sevenbroad-leaved
terrestriallaser FullyConvolutional separationofleaf onleafandwood
trees(Ulmus
[36] Han 2022 scanningtime NeuralNetwork, andwoody classificationwitha
americana)withaRigel
|     | series |     | LSTM-FCN,ResNet | componentsfrom | timeseriesofgeometric |
| --- | ------ | --- | --------------- | -------------- | --------------------- |
VZ-400i
|     | classification |     |     | pointclouds | features |
| --- | -------------- | --- | --- | ----------- | -------- |
Evaluatedeep
Achievingbest
Campos- Classification Sentinel-2timeseries 2-layerBi-LSTM recurrentnetwork
| [37]     | 2020      |      |         | overallaccuracyof |                    |
| -------- | --------- | ---- | ------- | ----------------- | ------------------ |
| Taberner | oflanduse | data | network |                   | 2-BiLSTMforlanduse |
98.7%
classification
Real-time
|     | classificationof |     |     | Superior | ApplyCNNtofind |
| --- | ---------------- | --- | --- | -------- | -------------- |
Databaseofdriver
[38] Naqvi 2020 normaland CNN performancevs. changesingazefrom
facialemotionandgaze
|     | abnormal |     |     | previousmethods | driver’simages |
| --- | -------- | --- | --- | --------------- | -------------- |
driving
Trafficflow
|            |                 | Trafficflowtimeseries |      | Outperformthe | DeployLSTMfor          |
| ---------- | --------------- | --------------------- | ---- | ------------- | ---------------------- |
| [39] Zheng | 2020 timeseries |                       | LSTM |               |                        |
|            |                 | fromOpenITS           |      | ARIMAandBPNN  | trafficflowforecasting |
forecasting

Sensors2023,23,7167 5of32
Table1.Cont.
|                  | Application |          | DeepLearning |          |         |
| ---------------- | ----------- | -------- | ------------ | -------- | ------- |
| Ref. FirstAuthor | Year        | Datasets |              | Accuracy | Details |
|                  | Field       |          | Models       |          |         |
Traffic
|     | predictionand |     |     |     | DeploytheRandom |
| --- | ------------- | --- | --- | --- | --------------- |
Reduced
|     | usermobility |     | Random |     | ConnectivityLSTMfor |
| --- | ------------ | --- | ------ | --- | ------------------- |
[40] Hua 2019 oftelecommu- Traffictimeseries ConnectivityLSTM computing trafficanduser
complexityby30%
|     | nication |     |     |     | mobilityprediction |
| --- | -------- | --- | --- | --- | ------------------ |
problems
|           |                  | Reliabilitytestdataofa |               |                 | EmployDNN               |
| --------- | ---------------- | ---------------------- | ------------- | --------------- | ----------------------- |
|           | Equipment        |                        | DeepLearning  | Significant     |                         |
|           |                  | cylinderinthesmall     |               |                 | frameworkfor            |
| [41] Chen | 2020 reliability |                        | methodbasedon | improvementover |                         |
|           |                  | trolleyofvehicle       |               |                 | reliabilityevaluationof |
|           | prediction       |                        | MLP           | PCAandHMM       |                         |
|           |                  | assemblyplant          |               |                 | cylinder                |
Conductsurveyof
Hybridmodelwith
[42] Lim 2021 Timeseries M4competition(Smyl, Exponential betterperformance commonencodersand
|     | forecasting | 2020) | smoothingRNN |     | decodersfortimeseries |
| --- | ----------- | ----- | ------------ | --- | --------------------- |
thanpuremethods
forecasting
Employgenerative
Strong
|             |             | Publicdatasets      |                    |                | adversarialpredictive |
| ----------- | ----------- | ------------------- | ------------------ | -------------- | --------------------- |
|             | Plantgrowth |                     | Generative         | performance    |                       |
| [43] Yasrab | 2021        | (Arabidopsisand     |                    |                | networkforleafand     |
|             | forecasting |                     | AdversarialNetwork | matchingexpert |                       |
|             |             | Brassicarapaplants) |                    |                | rootpredictive        |
annotation
segmentation
Deploydeepnetwork
Alzheimer’s Timeseriesdatafrom Ensembleofstacked fordetectingcommon
|                 | disease     | Alzheimer’sDisease |                   | Muchbetterthan |                   |
| --------------- | ----------- | ------------------ | ----------------- | -------------- | ----------------- |
| [44] El-Sappagh | 2020        |                    | CNNand            |                | patternsfor       |
|                 | progression | Neuroimaging       |                   | conventionalML |                   |
|                 |             |                    | BidirectionalLSTM |                | classificationand |
|                 | detection   | Initiative         |                   |                |                   |
regressiontasks
Twelvepublic
MLP,ElmanRNN,
datasetscovertime
|     | Twelvetime |                        | LSTM,EchoState |            |                      |
| --- | ---------- | ---------------------- | -------------- | ---------- | -------------------- |
|     |            | seriesapplicationslike |                |            | Evaluatesevenpopular |
|     | series     |                        | Network,GRU,   | LSTMandCNN |                      |
[45] Lara-Benitez 2021 finance,industry,solar DLmodelsintermsof
|     | forecasting |                         | CNN,Temporal  | arethebestchoices |                       |
| --- | ----------- | ----------------------- | ------------- | ----------------- | --------------------- |
|     |             | energy,tourism,traffic, |               |                   | efficiencyandaccuracy |
|     | tasks       | and                     | Convolutional |                   |                       |
Network
internettraffic
Investigating
|          | temporal          |                       |                  |                     | DeveloptheSpectral |
| -------- | ----------------- | --------------------- | ---------------- | ------------------- | ------------------ |
|          |                   | Timeseriesdatasets    |                  | Outstanding         |                    |
|          | correlationsof    |                       | SpectralTemporal |                     | TemporalGraph      |
|          |                   | fromenergy,           |                  | forecastingresults, |                    |
| [46] Cao | 2020 intra-series |                       | GraphNeural      |                     | NeuralNetworkfor   |
|          |                   | electrocardiogram,and |                  | plusadvantageof     |                    |
|          | andthe            |                       | Network          |                     | multivariabletime  |
|          |                   | trafficsectors        |                  | interpretability    |                    |
|          | correlationsof    |                       |                  |                     | seriesforecasting  |
inter-series
|                 | Predictionof  |                       |               |                  | Evaluatemodelsbased    |
| --------------- | ------------- | --------------------- | ------------- | ---------------- | ---------------------- |
|                 |               | Timeseriesdataof      |               | Betterprediction |                        |
|                 | solar         |                       | RNN,LSTM,GRU, |                  | onaccuracy,forecasting |
| [30] Rajagukguk | 2020          | temperature,humidity, |               | resultsthan      |                        |
|                 | irradianceand |                       | CNN-LSTM      |                  | horizon,trainingtime,  |
|                 |               | andwindspeed          |               | conventionalML   |                        |
|                 | photovoltaic  |                       |               |                  | etc.                   |
DeepLearning
|     |     |     | approach,basedon | Particularly |     |
| --- | --- | --- | ---------------- | ------------ | --- |
DeployDLapproach
|     | Solarenergy | Two-yeartimeseriesof | theH20package | suitableforbig |     |
| --- | ----------- | -------------------- | ------------- | -------------- | --- |
forsolarphotovoltaic
[47] Torres 2018 generation PVpowerfroma withthegridsearch solardata,givenits
powerforecastingfor
forecasting rooftopPVplant methodfor strongcomputing thenextday
|     |     |     | hyper-parameter | behavior |     |
| --- | --- | --- | --------------- | -------- | --- |
optimization
|     | Predictionof | SSTtimeseries |     | Outperform | DeployConvLSTMto |
| --- | ------------ | ------------- | --- | ---------- | ---------------- |
seasurface datafrom36-year ConvolutionalLong persistencemodel, capturecorrelationsof
| [48] Xiao | 2019 |     |     |     |     |
| --------- | ---- | --- | --- | --- | --- |
temperature observationsby Short-TermMemory SVR,andtwo SSTacrossbothspace
|     | (SST) | satellite |     | LSTMmodels | andtime |
| --- | ----- | --------- | --- | ---------- | ------- |
Multi-layer perceptron (MLP), recurrent neural network (RNN), Long Short-Term
Memorynetwork(LSTM),convolutionalneuralnetwork(CNN),graphneuralnetworks
(GNN), deep belief network (DBN), autoencoder (AE), and neural networks with an
attention mechanism are popular DL methods that have been used by the authors in
thissurvey.

Sensors 2023, 23, x FOR PEER REVIEW 7 of 35
Sensors2023,23,7167 6of32
Figure1. TreediagramforgroupingthepopularDeepLearningmethodsforsensortimeseries
classification and forecasting tasks covered in this survey [30,32–48] (note: if a paper uses two
methodsseparatelywithsimilarsatisfactoryresults,thepaperwillbelistedunderbothgroups).
2.1. Multi-LayerPerceptron
MLP is the most conventional and simplest Deep Learning structure and is fully
connected(FC)betweenlayers. Alltheneuronsinonelayerareconnectedtoeveryneuron
inthenearbynextlayer. Thismeansthateachtimeseriesrecordisassigneditsownweight,
andthetemporalinformationisnotutilized[35]. DuringthetrainingphaseoftheMLP,
theweightbetweentheneuronsoftwonearbylayerscanbeestimatedbytheminimization

Sensors2023,23,7167 7of32
ofcostfunctionthroughgradientdescentoptimization. Thecomputingofthegradientof
thecostfunctionisusedintheback-propagationalgorithm.
Jiang [34] conducted a comprehensive evaluation of the Deep Learning methods
(MLP,CNN,andResNet)againstaconventionalmachinelearningmethod—thenearest
neighbor. The 1-NN classifiers are deployed with eight different distance measures. A
totalof128univariatetimeseriesdatasetsaboutimage,motion,andsensorfromtheUCR
TimeSeriesClassificationArchive[49]weretestedfortheclassificationperformanceof
themodels. TheexperimentalresultsshowedthattheDeepLearningmethodscouldhave
betterperformancethanthenearestneighbor,buttheirdifferenceisnotsignificantwhen
appropriatedistancemeasuresaredeployedforthenearestneighborbasedonthetypesof
thetimeseriesdatasets.
IsmailFawazetal.[35]comprehensivelyevaluatedtheperformanceofthreepopular
structuresofDeepLearningfortimeseriesclassification(TSC),i.e.,MLP,CNN,andEcho
StateNetwork(ESN).TheDeepLearningmodelsforTSCtaskscanbeclassifiedasgen-
erativeanddiscriminativeapproaches. TheessentialstructureofESNisthereservoir,a
sparselyconnectedrandomRNNwithrandominitializationinthehiddenlayers. Jaeger
andHaas[50]inventedtheESNin2004fortimeseriesforecastingforwirelesscommunica-
tiontasks. Theevaluationwasconductedwiththe85univariatetimeseriesdatasetsofthe
UCR/UEAarchive[51]and13MTSdatasetsfromBaydogan’sarchive[52]. Forunivariate
time series applications, a one-dimensional CNN model is used, and the filter can be
viewedasperforminganon-lineartransformationforthetimeseries. Formultivariatetime
series,thedimensionsofthefilteraresettobethenumberofdimensionsofthetimeseries.
Fortimeseriesclassification,thefinallayeristhediscriminativelayerwhichcanassign
probabilitydistributionfortheclassvariablesofthetimeseriesconcerned. Theresults
supportedthatend-to-endDeepLearningisabletoreachstate-of-the-artperformancefor
TSCtasks.
Chen et al. [41] presented a Deep Learning method based on MLP for equipment
reliabilitypredictionwithsensortimeseriesdata. Conditionmonitoringforequipmentand
itsmaintenancepredictionisimportantforsmartmanufacturing. Itisdesirabletoconduct
maintenancebeforethemachinefailurehappens. Theexperimentwasconductedwitha
reliabilitytestofacylinderinthesmalltrolleyofvehicleassemblyplant. Asittakeslonger
tocompleteeachoperationforanagingcylinder,thecylinderoperationdurationcanserve
asthetimeseriesinputsfortheDeepLearningmethod. TheresultsshowthattheDeep
Learningmethodcanperformmuchbetterthanconventionalmachinelearningmethods.
Lara-Benitezetal.[45]comparedtheperformanceofsevenpopularDeepLearning
algorithms against twelve time series forecasting tasks. Time series forecasting is the
process of utilizing relevant historical time records to determine future values. When
deployingCNNfortimeseriesmodeling,causalconvolutionalfiltersareusedtoensure
thatforecastingismadeonlybasedonpastinformationinthetimeseries[53]. Thesame
asstandardCNN,temporalCNNalsosharesthesameassumptionthattherelationships
amongthetimeseriesvariablesaretime-invariant. Inattentionmechanisms,thetemporal
features of the time series signals can be aggregated with the dynamical generation of
weights by the attention layers. The attention network can pay more attention to the
significanthistoricalevent,nomatterhowfarbackitisinthekey-valuelookupwindow.
The Deep Learning models are MLP, four models of recurrent networks (Elman RNN,
LSTM,EchoStateNetwork,GRU),andtwoconvolutionalnetworks(CNNandTemporal
ConvolutionalNetwork). Thetwelvepublicdatasetscovertimeseriesapplicationslike
finance,industry,solarenergy,tourism,traffic,andinternettraffic. Theevaluationresults
showed that LSTM performs the best, while CNN can also make accurate and stable
forecastingwithlesscomputationalrequirements. Anotherperformancecomparisonof
Deep Learning methods can be found in Torres et al. [54], making a summary of the
satisfactory time series forecasting applications of the popular Deep Learning models
(ENN,LSTM,GRU,BRNN,MLP,CNN,andTCN)inthesectorslikeenergy,environment,
finance, health, industry, and image. The practical tip on how to set hyper-parameters

Sensors2023,23,7167 8of32
hasalsobeencovered. Thefourmaintypesofhyper-parameteroptimizationmethodsare
trial-error,grid,randomandprobabilistic.
Torres et al. [47] proposed a Deep Learning approach that was based on the H20
packagewritteninRwiththegridsearchmethodforhyper-parameteroptimizationand
implementedintheApacheSparkclusterenvironment. Asthemanufacturingcostforsolar
panelsdecreases,solarenergyisbecomingmuchmorepopular. Itispredictedthat30%
ofthetotalelectricitysourceswillbefromsolarenergyinAustraliabytheyear2050[55].
Factors like cloud cover, rainfall, solar radiation, and temperature can affect the gener-
ation of solar energy significantly and make the forecasting of solar energy generation
difficult. The dataset is the two-year time series of PV power with 30 min observation
interval. Itsperformancewascomparedwithpattern-sequence-basedforecasting(PSF)and
conventionalneuralnetworks. TheexperimentalresultssupportedthattheDeepLearning
approachisverysuitableforthesolarenergyforecastingtask.
2.2. RecurrentNeuralNetwork
RNNisdesignedwithastatefortheinformationattimestepssuchthatitcanhandle
sequence data element-wise [56]. As it can maintain the dependencies among the time
series elements, RNN has gained success in different fields such as image captioning,
machinelearningtranslation,speechrecognition[57],andweatherforecasting[58]. Elman
NeuralNetwork(ENN)isanRNNmodelwithanewhiddenlayercalledthecontextlayer,
whichmakesitcapableofdatasequenceprediction. Nevertheless,RNNfacesdifficulties
duetothevanishingandexplodinggradientproblemsduringitstrainingprocess. This
disadvantageofthevanishinggradientproblemcanbeamplifiedwhenconsideringlong-
rangedependentrelationships.
Choietal.[32]focusedonthefrontiertimeseriesanomalydetectionmethodsand
described how the methods model the interrelationship among variables and how the
temporalcontextwaslearned. Timeseriesanomalydetectionisabouttheidentification
ofunexpectedeventsfromthetimeseriesdata. Becauseoftheirlearningcapabilityfor
large-scalesequences,DeepLearningmethodscontributesignificantlytomultivariatetime
seriesanomalydetection. Nevertheless,mostofthesemethodshavebeendevelopedfor
veryspecificapplications,andsufficientdomainknowledgeisnecessary[32]. Benchmark
datasetsofthewatertreatmenttest-bed,thewaterdistributionpipelines,andtheMars
ScienceLaboratoryroverwereusedtocomparetheperformanceofthemethods(RNN,
CNN,hybrid,andattention). TheresulthighlightsthatthereisnosingleDeepLearning
methodthatcanfituniversallywithallthetimeseriestasks. EventhoughemergingDeep
Learningmethodsshowencouragingresultsformultivariatetimeseriesanomalydetection,
mostofthesemethodscannotexplaintherelationshipsamongthesensorsandthushave
limitedabilitytoexplainthedeviationsoftheanomalousevents.
LimandZohren[42]summarizedtherecenttrendsofDeepLearningmodelsandhy-
bridmodels. HybridmethodscombiningquantitativetimeseriesmodelswithDeepLearn-
ingmayaddresstheselimitationsandimprovetheoverallforecastingperformance[42].
A hybrid model may be able to incorporate domain experts to feed the Deep Learning
modelwithpriorinformationwhileaddressingtheissuesassociatedwithsmalldatasets
andoverfitting. ExponentialsmoothingRNN(ES-RNN)servesasagoodexampleofhow
theexponentialsmoothingmodulecanhelptheRNNbyaddressingthenon-stationary
trendsofthetimeseriesbywinningtheM4competition[59].
El-Sappaghetal.[44]presentedanensembleDeepLearningapproachofstackedCNN
andBidirectionalLSTM(Bi-LSTM)modelsforADprogressiondetection. Thetemporal
information from sensor monitoring of chronic disease can be helpful for progression
detection,whiletheprogressionofchronicAlzheimer’sdisease(AD)maybedelayedif
it can be predicted at an early stage. The data of AD patients are heterogeneous multi-
modalities. Bi-LSTMisaspecialtypeofLSTMthatcanexplorethedependenciesofboth
previousandfuturestates[6]. FortimeseriespredictionwithBidirectionalLSTM,oncea
forecastisavailableintraining,thisvaluecanbeutilizedforthesubsequentreadjustment

Sensors2023,23,7167 9of32
process. Thismayresultinadeeperunderstandingofthecontextconcerned. Themodel
canhandlethefusionofthefivedifferenttypesoftimeseriesdataalongwithbackground
knowledge. ThestackedCNNandBi-LSTMmodelsarecapableofextractingbothlocal
andlongitudinalfeaturesofthemodality,andthesystemcanmakepredictionsbasedon
theseresultantfeatures. ThetimeseriesdatafromtheAlzheimer’sDiseaseNeuroimaging
Initiativewereused,andtheresultssupportthesuperiorperformanceoftheproposed
ensembleDeepLearningapproach. Fortraditionalmethodstosucceedinstructuralhealth
monitoring, suitable preprocessing of the raw sensor time series data is nearly always
needed. Dangetal.[60]appliedfourpopularDeepLearningmodels,i.e.,MLP,LSTM,1D
CNN,andCNN,forstructuraldamagedetectionwithrawtimeseriesdata. Nofeature
engineering procedure like extracting structural characteristics was performed. Three
differentstructurescoveringsmalltolargestructuresweretested. Theexperimentalresults
supportthat2DCNNisthemostreliable,eventhoughthecomputationaltimeof2DCNN
isalsothehighestamongthemodels.
2.3. LongShort-TermMemory
Hochreiterand Schmidhuber [61]designedanewRNNmodel, calledLongShort-
TermMemory(LSTM),withaninternalmemoryunitandgatemechanism,foraddressing
theissuesofvanishingandexplodinggradientduringRNNtraining. Aself-feedingloopis
usedintheinnerlayersofLSTMthatcanlearntime-basedcorrelationssuchthatknowledge
frompreviousinputscanbeusedintheanalysisofthepresentinputs. Thethreegates
implementation [6] of LSTM can reduce the effects of the vanishing gradient problem
faced by RNN. The three gates are the forget gate, update gate, and output gate. The
forgetgateistodeterminewhatinformationshouldbekeptornot. Theupdategateis
to determine what new information should be utilized for updating the memory state.
Theoutputgateistodeterminetheoutputvaluethatwillserveastheinputinthenext
hidden unit. This design can enable the keeping of longstanding related information
whileforgettingunrelatedinformation. Thus,LSTMhasthecapabilitytoprocessthelong-
termdependenciesofinformationintemporaldatasetsandisdeployedforapplications
likespeechrecognition,trafficprediction,andweatherforecasting. TheGatedRecurrent
Unit(GRU)isdesignedwithalesscomplexRNNstructurethanLSTM[62]butcanalso
rememberusefulinformationandexplorethelong-termdependenciesofthevariables. A
GRUhasonlytwogates,i.e.,theupdategateandtherelevancegate. Theupdategateisto
determineifthememorystateistoupdateornot. Therelevancegateistodeterminehow
relatedthepreviousmemorystateisforcomputingthenextcandidate. AsGRUhasonly
twogates,itrequiresfewerparametersandcomputationaltimethanLSTM[63]whilestill
keepingthecapabilityforhandlingverylong-rangerelationshipsamongthetimeseries.
HanandSanchez-Azofeifa[36]investigatedtheleafandwoodterrestriallaserscan-
ning (TLS) time series classification with Fully Convolutional Neural Network (FCN),
LSTM-FCN,andResidualNetwork(ResNet). CNNhasbeenfoundtobecapableofper-
formingtimeseriesclassificationsatisfactorily,asitsmultiplefilterscanproducemultiple
discriminationfeaturesforclassificationfromthetemporalinputs[35]. Itisalsofound
thatthecombinedLSTM-FCNmethodcanfurtherimprovethetimeseriesclassification
resultsbyFCN[64]. TLSpointclouddataareusefulforclassifyingtheleafandwoody
components,andthustheleafareaindexandwoodareaindex. TheTLStimeseriespoint
cloudswereobservedfromsevenbroad-leavedtrees(Ulmusamericana). Theexperimental
resultsshowedthatallthreemodelsworkbetterwithmultivariabletimeseriesthanwith
univariabletimeseries. Thethreemodelscanalsoworkbetterthanpreviousmethods,and
allthesethreemodelsproducesimilarperformancesonthetestingtimeseries.
Campos-Taberner et al. [37] investigated the interpretability of a 2-layer Bi-LSTM
networkfortheclassificationoflanduseinValencia,Spain,withSentinel-2timeseriesdata.
Added-noisepermutationprocedurewasemployedinbothtemporalandspectraldomains
for evaluating the impact of different spectral and temporal features on the accuracy
rate. Theexperimentalresultsshowedthattheoverallaccuracyof98.7%achievedbythe

Sensors2023,23,7167 10of32
proposedmethodisbetterthanotherclassificationapproaches. Theproposedsystemcan
alsoshowtherelevanceofpredictorsandhighlightthattheredandnear-infraredSentinel-2
bandscontainthemosthelpfulinformation,whilethesummertimeseriesdataismost
usefulamongthetemporalinformation.
ZhengandHuang[39]deployedtheDeepLearningLSTMnetworkfortheforecasting
oftrafficflowtimeseries. Inanintelligenttrafficsystem,theaccurateforecastingoftraffic
flow may help to reduce urban congestion. The traffic flow time series from OpenITS
with5minintervalsintendayswasused,anditsperformancewasevaluatedwiththe
traditionalstatisticalmethod(ARIMA)andtheconventionalmachinelearningmethod
(BPNN).TheresultssupportthesuperiorpredictionaccuracyoftheLSTMmodel,with
themeanabsolutepercentageerrorsofARIMA,BPNN,andLSTMat20.97%,9.06%,and
4.82%,respectively.
Huaetal.[40]deployedtheRandomConnectivityLSTM(RCLSTM)fortrafficpredic-
tionandusermobilityoftelecommunicationproblemsinordertoreducethecomputational
requirementofLSTM.InRCLSTM,theneuronsareconnectedstochastically, andsome
sparsitycanbeachievedinthisrandomsparsegraphmodeltoreducecomputingtime.
RCLSTMisfoundtobesuitableforlatency-stringenttasksliketraffictimeseries. Another
similar task is the evaluation of the traffic time series data from the GEANT backbone
network by Uhlig et al. [65]. The experimental results showed that the forecasting per-
formanceofRCLSTMissimilartothetraditionalLSTMwhilesuccessfullyreducingthe
computationaltime.
Rajagukguketal.[30]investigatedthepredictionperformanceofsolarirradianceand
photovoltaic(PV)powerwithfourDeepLearningmodelsagainstconventionalmachine
learningmethods. Assolarenergyisrenewable,solarphotovoltaicshasgainedpopularity
inthegenerationofelectricity. ForthePVprediction,thepopularinputtimeseriesdata
arethetemperature,humidity,andwindspeed. Theexperimentalresultsconfirmedthat
all four Deep Learning models, i.e., RNN, LSTM, GRU, and CNN-LSTM, can perform
thepredictionbetter,withCNN-LSTMachievingthebestperformancebutalsoneeding
thelongesttrainingtimeperiod. InthehybridmodelCNN-LSTM,theCNNlayerscan
performthefeatureextractionoftheinputtimeseries,whileLSTMforsequenceprediction.
CNN-LSTMhasbeendesignedwiththecapabilitytohandletemporalpredictiontasksand
appliedinmanyreal-worldapplications. Experimentalresultslike[66]alsosupportedthe
consistentlybetterperformancebyCNN-LSTMoverLSTMforprecipitationprediction.
2.4. ConvolutionalNeuralNetwork
CNN is another popular neural network for time series modeling. CNN is a DL
methodofinterconnectedfeedforwardnetworkarchitecturesconsistingofasequenceof
convolution,pooling,activationlayers,and,finally,fullyconnectedlayers[67]. Filtering
operationisperformedintheconvolutionallayersthroughafeaturemap.Localconfluences
offeaturesareidentifiedfromtheprecedinglayerthroughdiscreteconvolution. Thus,this
typeofmodelbecomesknownasaconvolutionalneuralnetwork. Thepoolinglayeris
forreducingtheinputsizeandavoidingoverfitting. Theinputforthelastdenselayeris
theflattenedfeaturesfromtheconvolutionalandpoolinglayers, andtheforecastingis
madeinthisdenselayer. 1DCNNcanbedeployedforsimpleapplications,whilemore
sophisticatedmodels,likeCNN-Net,Enoded-Net,andCNN-LSTM,havemoreadvanced
structureslikelargerkernelsizeanddenserlayers.
Naqvi et al. [38] deployed a CNN model for detecting changes in gaze from the
face and left- and right-eye images. Driver time series data is helpful for the real-time
classificationofnormalandabnormaldrivingand,thus,forreducingaggressivedriving.
Thenear-infrared(NIR)camerasensorisemployedheretoconstructalargedatabaseof
driverfacialemotionandgaze. TheDlibfacialfeaturetrackerswereemployedtoidentify
theregionofinterest(ROI)beforefeedingtotheCNNmodel. Theexperimentalresults
supportedtheoutstandingperformanceoftheCNNmodel.

Sensors2023,23,7167 11of32
2.5. GraphNeuralNetwork
GNNisaneuralnetworkthatprocessesthedatawithrepresentationingraphdomains,
like in chemical compounds, images, and web [68]. Graphs can be classified as cyclic,
directed,undirected,oracombinationofthesethree. GNNshavebeenfoundusefulfor
applicationsincludingchemistry,citationnetworks,environmentalconditionforecasting,
molecularbiology,physics,andsocialnetworks. AfewDNNtopologiesmayindeedbe
viewedasGNN,forexample,withCNNconsideredasaGNNwithgraphsofpixel-per-
gridgrids.
DengandHooi[33]developedaGraphDeviationNetwork(GDN)modelfordiscov-
eringtherelationshipgraphamongthesensorsandfordetectingdeviationfromnormal
patterns.Graphneuralnetworkscanmodelthecomplexpatternsindataofgraphstructure,
withthenodestateinfluencedbyitsneighbornotestates. Velickovicetal.[69]developed
the graph attention network (GAT), which employed the attention function for evalu-
ating the various weights for various neighbors during aggregation. A difficulty for a
typical GNN model is that the graph structure is needed as an input, while this struc-
turemaynotbeknowninadvance. Theproposedsystemconsistsofsensorembedding,
graph-structuredlearning,graph-attention-basedforecasting,andgraphdeviationscoring.
Thesystemistestedwithtwolarge-scalesensortimeseriesdatasetsofwatertreatment
systems(SWaTandWADI).Theexperimentalresultssupportedtheperformanceofthe
proposedsystem,whiletheinterpretableoutputcanassistusersinbetterunderstanding
andlocalizinganomalies.
Caoetal.[46]presentedSpectralTemporalGraphNeuralNetwork(StemGNN)with
GraphFourierTransform(GFT)forcapturinginter-seriescorrelationsandDiscreteFourier
Transform(DFT)fortemporalcorrelations. Adifficultyformultivariatetimeseriesisthe
complexityinvolvingboththetemporalcorrelationsofintra-seriesandthecorrelationsof
inter-seriessimultaneously.ThespectralrepresentationsobtainedwithGFTandDFTenable
theDeepLearningmodulestohaveclearenoughpatternsfortheanalysis.Theexperimental
resultsfromtenreal-worldtimeseriespublicdatasets(fromenergy,electrocardiogram,and
trafficsectors)confirmtheperformanceoftheproposedStemGNN.
2.6. OthersandHybrids
HintonandOsinderoetal.[70]developedthefirstmodelandtrainingalgorithmfora
deepbeliefnetwork(DBN)in2006. DBNhasahierarchicalstructurewithalargenumber
of stacked restricted Boltzmann machines (RBMs) and utilizes a greedy layer-by-layer
learningapproachwithfine-tuning. TheRBMscanefficientlyextractthefeaturesforthe
initializationoffeedforwardneuralnetworks,henceimprovingthenetworkgeneralization
capability. IneachRBM,thereisbothavisiblelayerandaconcealedlayerconsistingof
neurons. WhiletheRBM’slayersareinterconnectedwitheachother,theunitsamongeach
layerarenot.TheupdatingofthenetworkparameterscanbedonewithaSoftMaxclassifier.
Autoencoderutilizesafeaturelearningparadigmthatcanlearnpara-metricmaps
directlyfrominputstocorrespondingrepresentation[71,72]. AnAEconsistsofanencoder
andadecoder. Theencoderisforfeatureextraction,whilethedecoderisformappingthe
featurespacebacktotheinputspace. Thestructureoftheencoderanddecoderisaninput
layer, hidden layers, and an output layer. Back-propagation algorithm is deployed for
updatingtheweightsofthehiddenlayers. DeepAEcanserveasadata-drivenapproach
forlearningfeatureextractionautomatically.
Neuralnetworkswithanattentionmechanismhavesucceededintimeseriesappli-
cations[73]. Thesenetworkscandynamicallycontrolthemappingfromtheinputstothe
outputsintelligentlywithotherknowledgeofthetask. Thetransformermodelisbased
on an encoder–decoder architecture of these networks. The input is fed to the encoder,
whichconsistsofastackofencoders. Then,thetransformercangeneratetheoutputbased
ontheencodedinputandpreviousoutputsinthedecoderaswell. Aclearadvantageof
transformersistheaccesstoanypointsinthepast,nomatterhowfartheirdistancesare,
leadingtothecapabilitytodiscoverthelong-termdependenciesamongthetimeseriesdata.

Sensors2023,23,7167 12of32
Yasrabetal.[43]designedaGenerativeAdversarialNetwork(GAN)forforecasting
the expected growth of the plant. Plant phenotyping is the investigation of plant trait
growthandotherquantitativeparametersandmaybeautomatedwiththehelpofDeep
Learning. GANisusuallydevelopedfromCNNandisformedwithtwonetworks,i.e.,the
generatorandthediscriminator. Bothnetworkscanlearntogetherbycompetingwitheach
othertogeneratenewexamplesofsyntheticdata. Segmentationmasksofshootandroot
weregeneratedtopredicttheplantsysteminthefuture. Twopublicdatasets(Arabidopsis
andBrassicarapaplants)wereused. Theevaluationresultsillustratedthattheproposed
systemcanreachthelevelwithannotationbyanexpert.
Xiaoetal.[48]developedaConvolutionalLongShort-TermMemory(ConvLSTM)
modeltoutilizethespatiotemporalcorrelationsofseasurfacetemperature(SST)forits
short and mid-term prediction. In the global ocean, SST has a significant influence on
the marine ecosystem. SST time series data from 36-year observations by satellite was
usedtoevaluatetheConvLSTMagainstthepersistencemodel,supportvectorregression
model,andLSTMmodels. WhenhandlingspatiotemporaldatabyfullyconnectedLSTM
(FC-LSTM),itisnotedthatthespatialcorrelationscanbelost[66]. Toaddressthisissue,
theConvLSTMreplacestheFC-LSTMmatricmultiplicationwithconvolutionoperation
inthetransitions. Thisistoensurethatthemodelcanexplorebothspatialandtemporal
correlations. TheexperimentalresultsconfirmedthatConvLSTMperformsbetterthan
othermethodsfortheone-to-ten-day-aheadpredictionofSSTtimeseries.
2.7. AdvancedPreprocessingandDeepLearningApplications
Feature engineering can be very important in the data preprocessing stage before
feedingdatatotheDeepLearning modelsbysignificantlyreducingthecomputational
requirementsforunnecessaryfeatures. ItsimportanceishighlightedintheworkofElsayed
andThyssensetal.[74],whichevaluatedthetimeseriesforecastingperformanceofeight
DeepLearningmethodsagainstthetraditionalmachinelearningmethod—theGradient
BoostingRegressionTree(GBRT).Externalfeatureswereutilizedforthetargetvalues,and
dataflatteningcanobtaintheoneinputinstanceforGBRT.Theevaluationwasconducted
withninedatasetscoveringairquality,electricity,finance,solarenergy,andtraffic. The
resultsshowedthatthewindow-basedtransformationcouldenableGBRTtoachievethe
bestforecastingperformanceovertheDeepLearningmodels,coveringvarioustypeslike
matrix factorization, RNNs, LSTMs, and bi-directional LSTM models. It is shown that
simplermachinelearningmodelswithefficientfeatureengineeringcanoutperformthe
frontier Deep Learning methods without feature engineering. Dablander and Bury [9]
highlightedtheimportanceofpreprocessingbyshowingthattheDLmodelcannotextract
enoughrelevantfeaturesforclassifyingthestationaryAR(1)processeswithoutdetrending
orwithaGaussianfilter. Theresultsshowedthatthemethodmightlearnuniquefeatures
relatedtoaLowessfilterinsteadoftherelevantfeaturesofthesystemnearthebifurcation.
Thus,carefulplanningisneededwhendeployingthepreprocessingmodels.
ThefollowingTable2highlightsthemostrecentcasestudiesthatadvancedprepro-
cessing is still needed, along with the Deep Learning methods, for modeling different
popular typesof sensortime series. In Table 2, asynthetic summary ofthe application
fields,theadvancedpreprocessingtechniques,theDLmethods,accuracy,andbriefappli-
cationdetailsispresented,followedbyamoredetaileddescriptionofthecorresponding
methods,motivations,andadvantages. ThefollowingFigure2showsthetreediagram
forgroupingthepopularpreprocessingmethodsforsensortimeseriesclassificationand
forecastingtaskscoveredinthissurvey.

Sensors2023,23,7167 13of32
Table2. Summaryoftheimportanceofadvancedpreprocessingtechniquesforreal-worldsensor
timeseriesDLapplications.
|     |     | Preprocessing | DeepLearning |     |     |
| --- | --- | ------------- | ------------ | --- | --- |
Ref. FirstAuthor Year ApplicationField Methods Models Accuracy Details
ECGtimeseries
DevelopaDL
signalsfor
|     |     | Squeezingand |     | Achievedmore | architectureforthe |
| --- | --- | ------------ | --- | ------------ | ------------------ |
monitoringand
[75] Kanani 2020 stretchingofthesignal 1Dconvolution than99% preprocessingprocess
classificationof
|     |     | alongthetimeaxis |     | accuracy | forincreasedtraining |
| --- | --- | ---------------- | --- | -------- | -------------------- |
cardiovascular
stability
health
Surface
DeployEMDto
|           | electromyography |               |     | Worstresults | segmentedsignalto  |
| --------- | ---------------- | ------------- | --- | ------------ | ------------------ |
|           | timeseriesof     | Empiricalmode |     | fororiginal  |                    |
| [76] Kisa | 2020             |               | CNN |              | obtaintheIntrinsic |
|           | humanmusclesfor  | decomposition |     | signalvs.all |                    |
ModeFunctions(IMFs)
gesture IMFsimages
imagesforCNN
classification
|     | Classifyingeight |     |     | Achievedbest | Evaluatetheimpactof |
| --- | ---------------- | --- | --- | ------------ | ------------------- |
Segmentationand
|           | dailyactivities |                |     | resultswith  | segmentationand |
| --------- | --------------- | -------------- | --- | ------------ | --------------- |
| [8] Zheng | 2018            | transformation | CNN |              |                 |
|           | fromwearable    |                |     | multichannel | transformation  |
methods
|     | sensors |     |     | method | methodsonDLmodels |
| --- | ------- | --- | --- | ------ | ----------------- |
Apply3D
SyntheticAperture 3D-Gamma LSTM, Highaccuracy spatial–temporalfilters
[77] CastroFilho 2020 Radarimagesfor filterandmethodof Bidirectional andKappa andsmoothingwith
ricecropdetection SavitzkyandGolay LSTM (>97%) Savitzky–Golayfilterto
minimizenoise
Presentthe
Atmospheric
|     | Classifyingcrop |                        |                  | Preprocessing | preprocessingpipeline, |
| --- | --------------- | ---------------------- | ---------------- | ------------- | ---------------------- |
|     |                 | correction,filteringof | 1D-convolutions, |               |                        |
|     | typebasedonraw  |                        |                  | canincrease   | includingatmospheric   |
|     |                 | cloudtemporal          | RNN,             |               |                        |
[78] ReBwurm 2020 andpreprocessed classification correction,temporal
|     |     | observations,focusing | self-attention |     |     |
| --- | --- | --------------------- | -------------- | --- | --- |
Sentinel2satellite onvegetativeperiods, model performance selectionofcloud-free
|     | timeseriesdata |     |     | forallmodels | observations,cloud |
| --- | -------------- | --- | --- | ------------ | ------------------ |
andmaskingofcloud
masking,etc.
CNN,Stacked
Deployautomatic
|               |                   |                   | GRU,          | Mosteffective |                       |
| ------------- | ----------------- | ----------------- | ------------- | ------------- | --------------------- |
|               | Classifyingmental |                   |               |               | ICA-ADJUSTto          |
|               |                   | Independent       | Bidirectional | model         |                       |
|               | workloadlevels    |                   |               |               | removethefrequently   |
| [79] Kingphai | 2022              | componentanalysis | GRU,          | performance   |                       |
|               | fromEEGtime       |                   |               |               | contaminatedartifacts |
|               |                   | basedonADJUST     | BGRU-GRU,     | canbe         |                       |
|               | seriessignals     |                   |               |               | componentsbefore      |
|               |                   |                   | LSTM,BiLSTM,  | achieved      |                       |
|               |                   |                   | BiLSTM-LSTM   |               | applyingDLmodels      |
Developanew
|                |                     |                      | Multi-scale   | Achieved      |                    |
| -------------- | ------------------- | -------------------- | ------------- | ------------- | ------------------ |
|                | Anomalydetection    |                      |               |               | ERR-basedthreshold |
|                |                     | Multi-scaleattribute | convolutional | superior      |                    |
| [80] Yokkampon | 2022 ofmultivariate |                      |               |               | settingstrategyto  |
|                |                     | matrices             | variational   | performance   |                    |
|                | sensortimeseries    |                      |               |               | optimizeanomaly    |
|                |                     |                      | autoencoder   | androbustness |                    |
detectionperformance
|          |     |                       | LSTM,         |             | ApplyPearson         |
| -------- | --- | --------------------- | ------------- | ----------- | -------------------- |
|          |     | Correlationmatrixwith |               | Retainedthe |                      |
| Barrera- |     |                       | Stacked-LSTM, |             | correlationmatricfor |
[58] 2022 Rainfallprediction thePearsoncorrelation mainfeatures
| Animas |     |                     | Bidirectional  |               | unsupervisedfeature  |
| ------ | --- | ------------------- | -------------- | ------------- | -------------------- |
|        |     | coefficient         | LSTM           | ofDLmodels    | selection            |
|        |     | Discretewavelet     |                | Performedbest | Proposea             |
|        |     | transformation,fast | Attention,DCN, | forattention  | preprocessingmodelof |
[81] Mishra 2020 Windpredictions Fourier DFF,RNN, andDCNwith discretewavelet
|     |                | Transformation,inverse | LSTM | waveletorFFT | transformationandfast |
| --- | -------------- | ---------------------- | ---- | ------------ | --------------------- |
|     |                | transformation         |      | signal       | Fouriertransformation |
|     | Timeseriesdata |                        |      |              | Proposetransformation |
|     |                | Iterative              |      | Considerably |                       |
fromenergy methodfor
|     |     | transformationsand | LSTM, | improvedthe |     |
| --- | --- | ------------------ | ----- | ----------- | --- |
[10] Livieris 2020 section,stock Augmented CNN-LSTM DLforecasting enforcementof
market,and stationarityofthetime
|     |                | Dickey–Fullertest |     | performance |        |
| --- | -------------- | ----------------- | --- | ----------- | ------ |
|     | cryptocurrency |                   |     |             | series |
Deploytimeseries
decompositionmethod
|           | Trafficflow | Timeseries          | Convolution- | Outperformed |               |
| --------- | ----------- | ------------------- | ------------ | ------------ | ------------- |
| [1] Asadi | 2020        |                     |              |              | forseparating |
|           | timeseries  | decompositionmethod | LSTM         | SOAmodels    |               |
short-term,long-term,
andspatialpatterns

Sensors2023,23,7167 14of32
Table2.Cont.
|                  |                       | Preprocessing | DeepLearning |          |         |
| ---------------- | --------------------- | ------------- | ------------ | -------- | ------- |
| Ref. FirstAuthor | Year ApplicationField |               |              | Accuracy | Details |
|                  |                       | Methods       | Models       |          |         |
Dataaugmentation
methods(liketime
|     |              |                    |     | Show | Comparedata |
| --- | ------------ | ------------------ | --- | ---- | ----------- |
|     | Surveyofdata | domainandfrequency |     |      |             |
[82] Wen 2021 augmentation domain), Deepgenerative successesin augmentationmethods
|     |     |     | models | timeseries | forenhancingthe |
| --- | --- | --- | ------ | ---------- | --------------- |
methods decomposition-based
|     |     |     |     | tasks | qualityoftrainingdata |
| --- | --- | --- | --- | ----- | --------------------- |
methods,statistical
generativemodels
Achievethe
Developacompression
|           |                  | Discretewavelet   |             | optimal     |                      |
| --------- | ---------------- | ----------------- | ----------- | ----------- | -------------------- |
|           |                  |                   | Resnet,     |             | approachwithdiscrete |
|           | Wirelessnetwork  | transformandthe   |             | trade-off   |                      |
| [83] Azar | 2020             |                   | LSTM-FCN,   |             | wavelettransformand  |
|           | withsmartsensors | error-bound       |             | betweendata |                      |
|           |                  |                   | GRU-FCN,FCN |             | error-bound          |
|           |                  | compressorSqueeze |             | compression |                      |
|           |                  |                   |             | andquality  | compressor           |
KananiandPadole[75]presentedapreprocessingframeworkthatcanincreasethe
electrocardiogram(ECG)classificationaccuracyoftheDeepLearningmethodssignificantly,
withahigherthan99%accuracyrate. ECGtimeseriessignalsareveryefficientforthe
monitoring of cardiovascular health, with abnormal heartbeats detected from the ECG
patterns. ThelabeledMIT-BIHArrhythmiadataset,whichhasECGtimeseriessignalsof
fivedifferentclasses,wastested. Theproposedpreprocessingstepsincludethesqueezing
andstretchingofthesignalalongthetimeaxisandtheamplifyingandshrinkingoftheam-
plitudeofthesignal.Itisshownthatthesetransformationsdonotchangethecharacteristics
ofthesignalsandcanberegardedascompletelylosslesstransformationshere.
Kisa et al. [76] deployed an adaptive preprocessing method with empirical mode
decomposition(EMD)wasproposedtohandlethisnonstationarytimeseries,asthesur-
faceelectromyography(sEMG)timeseriesisnonstationaryandnonlinear. sEMGcanbe
employedtomeasuretheelectricalactivityofhumanmuscles. Therecognitionofhuman
movementsisusefulforapplicationslikehuman–computerinteraction(HCI).ThesEMG
handgesturetimeseriesdatawasobtainedwithasensordeviceofsurfacebipolarelec-
trodeswith30healthyvolunteers. EMDcanserveasanon-linearfiltertodecomposethe
inputtimeseriesintoseveralintrinsicmodefunctions(IMFs). TheoutputsoftheIMFs
werethenfedintotheDeepLearningmodelCNNbasedonResidualNetworks(ResNet)
forgestureclassification. ItisfoundthattheIMFscanimprovethevalidationaccuracyof
theoriginaltimeseriesfrom94.22%toamaximumof99.73%.
Zhengetal.[8]investigatedthesegmentationandtransformationmethodsfortheir
effectivenessindatapreprocessingforDeepLearningalgorithms. InHARtasks,segmen-
tationmethodsareessentialasrawinertialtimeseriescanhaveverylargefluctuations.
Five segmentation options of five different segment lengths were evaluated with four
transformationmethods,i.e.,rawplot,multichannel,spectrogram,andspectrogramwith
shallowfeatures. Theexperimentwasconductedwithdatasetsofeightdailyactivities
fromwearablesensors,carworkshopmaintenanceactivitydata,etc. Theresultsshowed
thattheclassificationaccuracyincreasesalongwithanincreaseinsegmentlength, and
themultichannelmethodcanperformthebestfortheHARtasks. Theoverallaccuracyis
97.2%,whichisbetterthanmanyothermachinelearningmodels.
CastroFilhoetal.[77]appliedatwo-stagenoiseschemeforpreprocessingSARtime
series,asthereareinevitablenoiseslikespecklesforSyntheticApertureRadar(SAR)images.
SAR sensors can be employed for mapping the rice-growing regions and constructing
continuoustimeseriesdata. TheSARdataisveryusefulformonitoringshortphenological
stagesandraisingtheclassificationcapacity. 3D-Gammafilterwasusedtoeliminatethe
speckle, and the method of Savitzky and Golay [84] was employed to smooth the time
series. TheprocessedtimeserieswasfedtotwoDeepLearningmethods,theLongShort-
TermMemorymodelandtheBidirectionalLSTMmodel,formappingricecropswithSAR
sensortimeseriesfromWestRioGrandedoSul(Brazil). Theresultswerecomparedwith

Sensors 2023, 23, x FOR PEER REVIEW 17 of 35
Sensors2023,23,7167 15of32
conventionalmachinelearningmodels,withBiLSTMshowingthebestperformanceinthe
McNemartest.
Figure 2. Tree diagram for grouping the popular preprocessing methods for sensor time series
classificationandforecastingtaskscoveredinthissurvey[1,8,10,58,75–83](note: ifapaperuses
twomethodsseparatelywithsimilarsatisfactoryresults,thepaperwillbelistedunderbothgroups).
ReBwurmandKorner[78]investigatedtheeffectivenessofDeepLearningmodels
for the classification of crop type based on raw and preprocessed Sentinel 2 satellite
time series data. With the advance of remote sensing technologies, the amount of the
Earthobservationtimeseriesdatahasbeengreatlyincreasingoverrecentyears. While
manytraditionalmodelsforremotesensingapplicationsrequirepreprocessingandfeature

Sensors2023,23,7167 16of32
extraction,ReBwurmandKorner[78]checkedifthecurrentDeepLearningmethodsare
abletoutilizetherawtimeseriesdatadirectlywithoutdatapreprocessing. Atmospheric
correction,filteringofcloudtemporalobservations,focusingonvegetativeperiods,and
maskingofclouds,whicharetypicalpreprocessingmethodsforsatellitetimeseries,have
been applied. Additionally, 1D-convolutions, recurrent neural networks (RNN), and
theself-attentionmodeloftheencoderarchitectureoftheTransformernetwork[85]are
deployedandevaluated. Theresultsshowthatself-attentionandRNNcanperformbetter
forrawdata,whilethepreprocessingprocesscanimprovetheresultsforallthreemethods
satisfactorily.
KingphaiandMoshfeghi[79]employedsevenDeepLearningmodels,i.e.,convolu-
tionalneuralnetwork(CNN),StackedGatedRecurrentUnit(SGRU),BidirectionalGRU
(BGRU),BGRU-GRU,LSTM),BidirectionalLSTM(BiLSTM),andBiLSTM-LSTM,forclas-
sifyingmentalworkload(MWL)levelsfromelectroencephalography(EEG)timeseries
signals. MWLcanleadtoabetterunderstandingofhumanperformanceincomplexenvi-
ronments. EEGtimeseriescanbeutilizedforclassifyingthementalworkloadlevelofa
humansubject. ThedatasetSTEWcontainssignalsfrom48subjectsintherestingandwork-
ingstates. PreprocessingisneededbecausethereisusuallynoiseintheEEGsignals. The
independentcomponentanalysisbasedonADJUST(ICA-ADJUST)byMognonetal.[86]
was found to be the most effective preprocessing tool for this dataset by Kingphai and
Moshfeghi[87]. KingphaiandMoshfeghi[79]extractedfourgroupsoffeatures(frequency
domain,timedomain,lineardomain,andnon-lineardomain)fortheDeepLearningmod-
els. The results showed that BiLSTM-LSTM performed best with 94.75% accuracy for
classifyingrestingvs. workingstates,whileBGRU-GRUwasbestforclassifyinglowvs.
moderatevs. highMWLlevelswith83.03%accuracy.
Yokkamponetal.[80]deployedmulti-scaleattributematricesasthepreprocessing
toolfortransformingthemultivariatetimeseriestodevelopamulti-scaleconvolutional
variationalautoencoderforunsupervisedanomalydetectionofmultivariatesensortime
seriesdatasets. Theattributematricescanutilizethepair-wiseinnerproductofthetime
seriesamongsegmentsandeffectivelycharacterizesystemstatesofthetimeseries. The
identificationofanomaliesisaboutdetectingdatapointsthatdeviatesignificantlyfrom
theirexpectedvalues. Therearethreetypesoftimeseriesanomalies: (1)pointanomalies,
which refer to outlier points; (2) contextual anomalies, which differ significantly from
typicalpointsofthesamecontext;and(3)collectiveanomalies,whichrefertotheexistence
ofasubsetoftimeseriesdatapointswithasignificantdifferencefromtheotherpointsin
thewholedataset[88]. Anomalydetectioncanbeemployedinmanyreal-worldcases,like
fraudulenttransactiondetection,sensornetworkfaultanalysis,andabnormalequipment
monitoring. The proposed model was tested with four publicly available benchmark
datasets: thetimeseriesdatabytheAustralianCentreforRemoteSensing,theWafertime
seriesdatasetofsemiconductormicroelectronicsfabrication,theEmotivEEGNeuroheadset
timeseriesdataset,andOpthandwritingdataset. Theexperimentalresultsshowthatthe
modelperformedbetterthanotherbaselinemethods.
IntheinvestigationbyBarrera-Animasetal.[58],beforefeedingthetimeseriesdata
intotheDLmodels,thefeatureselectionprocesswasachievedwiththecorrelationmatrix
(CM),whichiscomputedwiththePearsoncorrelationcoefficientforthe43-dimensional
datasets. Rainfall prediction is complicated because of its nonlinear characters. Spa-
tialinformationlikelatitudeandlongitudeandatmosphericinformationlikehumidity,
pressure,temperature,andwindspeedmaybeutilizedfortheforecastingmodels. Barrera-
Animasetal. investigatedtheeffectivenessofDeepLearningmodels,includingLSTM,
Stacked-LSTM, and Bidirectional LSTM, with the conventional machine learning (ML)
modelXGBoost,andalsoautomatedmachinelearning(AutoML)withtheTPOTtool[89],
whichcanberegardedhereasanensembleofMLmodels. OpenWeatherdataoffiveUK
citiesfrom2000to2020wereevaluated. Highlycorrelatedfeatureswillbeeliminated. The
experimentalresultshighlightedthattheStacked-LSTMwithtwohiddenlayersandthe
BidirectionalLSTMcouldobtainthebestperformanceinrainfallforecasting.

Sensors2023,23,7167 17of32
Mishraetal.[81](2020)evaluatedthewindpredictionswithfiveDeepLearningmeth-
odsagainstthreedatapreprocessingtools. Thefivemethodsaretheattentionmechanism
(Attention)ofsequence-to-sequenceencoder–decoderarchitecture[90],deepconvolutional
network(DCN),deepfeedForward(DFF),recurrentneuralnetwork(RNN),andLSTM.
Thedatasetisthetimeseriesofthetemperatureandwindpowervariable. Discretewavelet
transformationandfastFouriertransformation(FFT)areemployedtotransformthetime
seriesdatasetbeforefeedingtotheDeepLearningmodels,whileinversetransformation
wasappliedtotheDLmodeloutputsbeforemakingpredictions. Theexperimentalresults
showedthatAttentionandDCNworkthebestwithwaveletandFFT,whilesomeother
modelsworkbetterwithnoneedfordatapreprocessing.
Livieris et al. [10] proposed a preprocessing framework to further improve the ef-
ficiency and reliability of the Deep Learning methods. Iterative transformations and
augmentedDickey–Fullertestwereappliedtothetimeseriesdataforobtainingstationary
processed time series data before feeding to the Deep Learning model. The Ljung–Box
Qtestwasemployedtochecktheautocorrelationofthemodel’serrors. Timeseriesdata
fromenergysection,stockmarket,andcryptocurrencyweretested,andtheexperimental
resultsshowedthattheproposedpreprocessingframeworkcouldenhancetheefficiency,
accuracy,andreliabilityoftheDeepLearningLSTMandCNN-LSTMmodelsconsiderably.
Livierisetal.[91]continuedtheirworkontheinvestigationofthepreprocessingframe-
workforDeepLearningmodels. Ontopoftheirpreviousfocusonthetransformationof
non-stationarytimeseriestostationarybydifferencingthetimeseries,therawtimeseries
isnowsubjectfirstlysubjecttotheexponentialsmoothingmethod,whichcantransform
therawdatatoade-noisedversion. Thisprocessistoincreasethequalityofthetimeseries
dataandthusimprovethepredictioncapabilityoftheDeepLearningmodelCNN-LSTM.
Theexperimentalresultswithcryptocurrency,energy,andstockmarketsconfirmedthatthe
preprocessingframeworkcouldsignificantlyachieveitsobjectiveoffurtherimprovement
fortheDeepLearningmodels.
AsadiandRegan[1]employedthetimeseriesdecompositionmethodtoobtainthe
short-term, long-term, and spatial patterns in the proposed preprocessing framework.
Theshort-termpatternsofthespatialtimeserieswereexploredwiththefuzzyclustering
method,whichcangroupneighboringtimeseriestogetheraccordingtothechecksonthe
residualsofthetimeseries. Theseresidualsinspatialtimeseriescanprovidemeaningful
patternswithneighboringlocations,likeshowinghowthetrafficisevolvingintheroad
network. Thetrafficflowtimeseriesdatasetwastested,andthemethodcanobtainbetter
resultsthanboththebaselineandstate-of-the-artmethods.
Wenetal.[82]presentedasurveyofthedataaugmentationmethodsthatarespecif-
icallydesignedforhandlingtimeseriesdatasets. Becausemanyreal-worldapplications
likemedicaltimeseriesoranomalydetectiontimeseriesfacetheproblemofnothaving
enoughlabeleddata,itcanbeveryhelpfultohaveaneffectivewaythatcanenlargethe
sizeandimprovethequalityofthetrainingdataduringdeployingDeepLearningontime
seriesdatasets. Dataaugmentationhasbeenfoundverysuitableforthistask, asitcan
generatedatasyntheticallyforunexploredinputspacewithcorrectlabels. Notonlybasic
dataaugmentationmethods,liketimedomainandfrequencydomain,butalsoadvanced
methods,likedecomposition-basedmethods,statisticalgenerativemodels,anddeepgen-
erativemodels,arecoveredinthesurveybyWenetal. Theseaugmentationmethodsare
foundtobeeffectiveintimeseriesclassification,timeseriesanomalydetection,andtime
seriesforecasting.
Azaretal.[83]developedacompressionmoduleforbothunivariateandmultivari-
atetimeseriesdatawiththediscretewavelettransformandtheerror-boundcompressor
Squeeze(SZ).On-boardprocessingandcompressionalgorithmscanreducetheproblems
associatedwiththetransmissionoflargedatavolumesinapplicationsoftheInternetof
Things(IoT).Thispreprocessingprocedureisespeciallyimportantforthesensorsystems
inIoT,astheymayonlyhaveverylimitedbandwidth,memory,andcomputationalpower.
TheprocessedtimeseriesdataisthensenttotheDeepLearningmodels(Resnet,LSTM-

Sensors2023,23,7167 18of32
FCN,GRU-FCN,FCN)fortimeseriesclassification. TheFullyConvolutionalNetwork
(FCN)deployedhereconsistsofaconvolutionallayerwithfilters,abatchnormalization
layer,andthenaReLUactivationlayer. Theexperimentwasconductedwithtimeseries
datasets(UCR,UCI,andUEA)fromsensorsofECG,motion,etc. Theresultssupported
thatthecompressionapproachcanachieveahighcompressionratio,whileitstimeseries
denoisingcapabilityenablestheDeepLearningmoduletoachievesatisfactoryclassifica-
tionaccuracy.
3. AdvancesinContinualLearningMethodsforTimeSeriesModeling
In the previous section, applications of Deep Learning models and preprocessing
methodsindifferentreal-worldtimeseriesscenarioshavebeenreviewed. Limitationsof
DeepLearningmodelsincludeastrictstaticrequirementfortheunderlyingprocess[92].
Post-deploymentchangesarenotuncommonintherealworld,buttheDLmethodsare
usuallyoffixednetworkstructureafterbeingdeployed.WhenDLmodelsarefedwithdata
notfollowingtheindependentandidenticallydistributed(i.i.d.) assumption,destructive
interferencemayoccurandcauseperformancedegradation[93].Continuallearningmaybe
deployedtoaddressthesedifficultiesfacedbyDLmodelsinsuchawaythatDeepLearning
models may benefit from continual learning to become capable of learning continually
withadaptability.
Amajorcharacteristicofcontinuallearningisitssequentiallearningprocess. Ateach
time,onlyasmallamountoftheinputdataisavailable.OthernamesforCLincludelifelong
learning, sequential learning, and incremental learning. Mathematically, the continual
learningforbothclassificationandtimeseriesregressionproblemscanbeexpressedas
follows[94]: LetT = (T ,...,T )representthemtasksthatarriveinsequence. Fortask
1 m
T(i =1,2,...,m),thereexistNinstancesoflabeledtimeseriesdataD = {(x ,y )}N .
i i i,r i,r r=1
Here, time series x ∈ X is associated with the corresponding target y ∈ Y. For
i,r i i,r i
classificationtasks,thetargetspaceY referstoclasslabels. Fortimeseriesregressiontasks,
i
the target spaceY refers to real numbers. A constraint of continual learning is that for
i
any task T, there exists no access to the data of previous tasks T(j =1,...,i−1). The
i j
common goal of each task is to learn a solver model M, such that M : X →Y , with
i i i i
trainableparametersθ andestimatedtargetyˆ = M(x ;θ ). LetL(y ,yˆ ;θ )represent
i i,r i i,r i i,r i,r i
thetrainingobjectives. Forclassificationproblems,thiscanbethestandardcross-entropy
loss,whilefortimeseriesregressionproblems,thiscanbethesquared-errorloss. Then,
q ∑ N (cid:18) 1−q (cid:19)i ∑ −1 ∑ N (cid:0) (cid:0) (cid:1) (cid:1)
L = L(y ,yˆ ;θ )+ L y ,M xˆ ;θ ;θ
i N i,r i,r i (i−1)N j,r i j,r i i
r=1 j=1r=1
whereNreferstothenumberofinstances,and0< q ≤1referstotheimportanceassigned
todatafromT.
i
There are several popular CL scenarios, like Instance-Incremental Learning (IIL),
Domain-IncrementalLearning(DIL),Task-IncrementalLearning(TIL),Class-Incremental
Learning (CIL), Task-Free Continual Learning (TFCL), and Online Continual Learning
(OCL).Thistaxonomyisbasedonhowtheincrementalbatchesaredividedandwhich
taskidentifiesareavailable[18]. IILreferstoscenarioswherealltrainingsamplesarrivein
batchesandbelongtothesametask. DILreferstoscenarioswheretaskidentitiesarenot
needed;taskshavedifferentinputdistributionsbutthesamedatalabelspace. TILrefersto
scenarioswheretaskidentitiesareavailableduringbothtrainingandtesting,andtasks
havedisjointdatalabelspaces. CILreferstoscenarioswheretaskidentitiesareavailable
onlyduringtrainingandtaskshavedisjointdatalabelspaces. TFCLreferstoscenarios
wherenotaskidentityisavailableandtaskshavedisjointdatalabelspaces. OCLrefersto
scenarioswheretrainingsamplesforeachtaskarrivefromthedatastreamonebyone,and
taskshavedisjointdatalabelspaces.
Fleschetal.[95]highlightedthatforhumancontinuallearning,theextensiveback-
groundstatisticalknowledgegainedfrompreviousunsupervisedtrainingmightbeutilized

Sensors2023,23,7167 19of32
forrulelearningatlaterstages,thoughwithseveralconditions,whileDNNsufferscatas-
trophicforgetting(CF)problems. CFcanbeviewedasanissuestemmingfromtheNN
stability–plasticitydilemma,andtheCFeffectisassociatedwiththeabruptlossofprevi-
ouslylearnedknowledge[17]. PlasticityreferstotheNN’sabilitytolearnnewknowledge,
whilestabilitymeansthestoringoflearnedknowledge. CLcanbeemployedinsupervised
learning,semi-supervisedlearning,unsupervisedlearning,andreinforcementlearningas
well. Shaheenetal.[96]discussedtheapplicationsofcontinuallearningforautonomous
systems. Thereal-worldsystemsofvehicleswithself-drivingcapability,unmannedaerial
vehicles,andautonomousroboticswerehighlighted.
VariousdegreesofconstraintsimplificationforsolvingtheCFissueareimposedin
thecurrentmethods. Thereareconstraintssuchasmemory,computationalpower,and
dataprivacy. Nevertheless,thereareissueswhenapplyingthesemethods,forexample,
toorigidconstraintsthatmaybreaktheideaoflearningcontinuallyortootailor-made
forsolvingaparticulartypeofproblemonly. PfulbandGepperth[97]investigatedthe
CFproblemsinDNNwithaverylargenumberofdatasetsinvisualclassification. The
large-scaleexperimentsshowthatnomodelanddatasetisfreeoftheCFproblems,whilst
a few potential workarounds may enable a few models to become practicable in a few
application-levelenvironments. Inspiredbyopen-setrecognition,Prabhuetal.[98]pre-
sentedamodelcalledGDumb,whichisnottailor-madeforCLtasks. GDumbstartswith
storingsamplesgreedilyinmemoryastheyarrive,andduringtesting,itproceedswithnew
modeltrainingwithsamplesonlyinthememory.GDumbisshowntooutperformmanyCL
approachesandmayserveasanalerttothecurrentprogressinCLforclassification,with
theoversimplificationsbysomeexistingCLapproachestotheproblemsresultinginlittle
real-worldapplicationvalue. InthedeepautoencoderNNfortimeseriesforecasting[99],
buffers were deployed with online elastic weight consolidation to learn the probability
distributionofthedatastreamsequentially. ACLmodelwithexplicitmemorystructure
wasusedtoaddressCFintheirFFNNmodelformakinglong-termfinancialinvestment
decisions[100].Chenetal.[101]employedgraphneuralnetworkswithCLstrategies—data
replayandparametersmoothing—fortransferringlearnedknowledgetothecurrentmodel
intheirtrafficflowforecastingframework.
TherelationshipbetweenneuralnetworkarchitecturesandCFwasinvestigated,and
itwasfoundthatthenetworkwidthhasasignificanteffectonforgetting. Nevertheless,
whenincreasingthewidthtoaddressCF,inefficiencyproblemslikelongcomputationtime
andlargeenergywasteinevitablyappear. Langeetal.[17]investigatedmodelcapacity,
weightdecay,dropoutregularization,andthestability–plasticitytrade-offamongcontinual
learners. Lesortetal.[102]investigatedtheeffectsoftheparameterizationsoftheDNN
outputlayeronlearningandforgettinginCL.Theevaluationisconductedinasimplified
learningenvironment,decomposingthemodelasaclassifierpartfortheoutputlayerand
afeatureextractorpartfortherestoftheDNN.Weightsmodifications,interference,and
projection drift can be the causes of CF in the output layer. More knowledge is gained
about the continual learning in output layers. Instead of focusing solely on continual
learning,Mundtetal.[103]presentedaframeworkcombiningconceptsfromCL,open
set recognition, and active learning. This holistic approach shows promising results in
addressingcatastrophicforgettingandrobustnessforopen-worldapplications.
Current limitations for CL applications include the predominant closed-world as-
sumptionwhendeployingmodels, whichrequiresthatanynewdatafollowsthesame
distributionasthoseusedduringtraining. Whenthisclosed-worldassumptionisnolonger
valid,theneuralnetworksmaygivefalsepredictionswithunknownsituationsorwith
corrupteddata[103]. AnotherlimitationisthatmanycurrentworksinCLmaynotoften
considerthescalabilityissueinpotentialapplications,whichmayhaveaverylargenumber
ofsub-tasksand,consequently,hugeamountsofsamples.
WhilstmostoftherecentworksonCLfocusonsupervisedtasks,theover-specializing
ofCLtrainingforasinglesetofenvironmentslimitsCLgeneralizationtoothertypesof
applications[104]. WithmostrecentresearchfocusingontheCLapplicationsforclassifica-

Sensors2023,23,7167 20of32
tiontasks,thislackofattentionmayhindertimeseriesapplicationslikerenewableenergy
forecastingwithCLmodels[99]. DeepLearningmethodswithouttheabilitytoremember
oldknowledgemaynothandlewellinreal-worldapplicationsoftimeseriesforecasting
withnon-stationarysequentialdata[105]. Ontheotherhand,thecurrentCLprojectson
differenttimeseriesregressiontasksareshowingencouragingresults. Phametal.[105]
designed a fast and slow learning network for online time series forecasting, with the
per-layeradapterforfastlearningandassociativememoryforrememberingandrecalling
repeatingpastevents. CLmaybeveryusefulforaddressingfinancialtimeseriesproblems,
whichcanappeareverywhereandarecommonlynon-stationary[100],andfortrafficflow
timeseriesforecasting,whichisessentialforsmarttransportation. Mostcurrentmethodsof
trafficflowforecastingassumestaticnetworks[101]. Yet,real-worldtrafficflownetworks
changeconstantly,likepossiblenetworkmodificationandtheadditionofnewparts[106].
Aftertheabovediscussionillustratestheimportanceofcontinuallearningamongthe
DeepLearningtimeseriesapplications,asyntheticsummaryoftheadvancesincontinual
learning techniques for time series applications is presented in Table 3, followed by a
detaileddescriptionofthecorrespondingmethods,motivations,accuracy,andbriefdetails.
ThefollowingFigure3showsthetreediagramofthetaxonomyofthecontinuallearning
methodsforsensortimeseriesclassificationandforecasting.
Table3.Summaryoftheadvancesincontinuallearningtechniquesfortimeseriesapplications.
|                  | Application | Motivationsfor | ContinualLearning |          |         |
| ---------------- | ----------- | -------------- | ----------------- | -------- | ------- |
| Ref. FirstAuthor | Year        |                |                   | Accuracy | Details |
|                  | Field       | DeployingCL    | Models            |          |         |
Addressingthe
|     | Wearablesensors | catastrophicforgetting |                | Stillneed      | CompareCL |
| --- | --------------- | ---------------------- | -------------- | -------------- | --------- |
|     |                 |                        | A-GEM,ER-Ring, | improvementfor |           |
[107] Sah 2022 foractivity inthenon-stationary approachesforsensor
|     |             |                    | MC-SGD | multitask |         |
| --- | ----------- | ------------------ | ------ | --------- | ------- |
|     | recognition | sequentiallearning |        |           | systems |
training
process
|     | Humanstate |     | Replay,elasticweight | Existing |     |
| --- | ---------- | --- | -------------------- | -------- | --- |
Assesstheabilityof
|     | monitoringof | Overcomingthe | consolidation, | strategies |     |
| --- | ------------ | ------------- | -------------- | ---------- | --- |
existingCLmethods
[108] Matteoni 2022 domain- non-stationary learningwithout struggleto
forknowledge
|     | incremental | environments | forgetting,naiveand | accumulate |     |
| --- | ----------- | ------------ | ------------------- | ---------- | --- |
accumulationovertime
|     | scenario |     | cumulativestrategies | knowledge |     |
| --- | -------- | --- | -------------------- | --------- | --- |
Multipleclinics
|     | withvarious |     | Bufferstrategyto |     | Apply |
| --- | ----------- | --- | ---------------- | --- | ----- |
Temporaldatainclinics
|               | sensorsfor |          | constructthe      | Outperform | uncertainty-based     |
| ------------- | ---------- | -------- | ----------------- | ---------- | --------------------- |
| [93] Kiyasseh | 2021       | areoften |                   |            |                       |
|               | cardiac    |          | continuallearning | GEMandMIR  | acquisitionfunctions, |
non-stationary
|     | arrhythmia |     | modelCLOPS |     | forinstance,replay |
| --- | ---------- | --- | ---------- | --- | ------------------ |
classification
Comparethreemain
|     | Deploymentin | Addressingthe         |               |                |                 |
| --- | ------------ | --------------------- | ------------- | -------------- | --------------- |
|     |              |                       | CLapproaches- | Bestresultsfor | CLapproachesfor |
|     | mobileand    | resourcesrequirements |               |                |                 |
[109] Kwon 2021 embedded andlimitationsofthe regularization,replay replaywith mobileandembedded
|     |         |                   | andreplaywith | exemplars | sensingapplications |
| --- | ------- | ----------------- | ------------- | --------- | ------------------- |
|     | sensing | mobileandembedded |               |           |                     |
|     |         |                   | examples      | schemes   | likeactivity        |
|     | devices | sensingdevices    |               |           |                     |
recognition
EvaluateCL
|     |     |     |     | Highlightthe | approachesin |
| --- | --- | --- | --- | ------------ | ------------ |
Achievingwalk
Sensorsofthe Continuallearningin importanceofa class-incremental
| [110] Cossu | 2021           | learningindifferent |      |       |                    |
| ----------- | -------------- | ------------------- | ---- | ----- | ------------------ |
|             | roboticssystem |                     | RNNs | clear | scenariosforspeech |
environments
|     |     |     |     | specification | recognitionand |
| --- | --- | --- | --- | ------------- | -------------- |
sequenceclassification
Explainability
|          |                  |                     | modulebasedon      |                 | Proposetheconceptual   |
| -------- | ---------------- | ------------------- | ------------------ | --------------- | ---------------------- |
|          |                  | Addressingthelackof |                    | Proposed        |                        |
|          | Identificationof |                     | dimensionreduction |                 | designofexplainability |
| [111] He | 2022             | transparencyforCL   |                    | evaluationscore |                        |
|          | anomalies        |                     | methodsand         |                 | moduleforCL            |
|          |                  | modules             |                    | basedonmetric   |                        |
|          |                  |                     | visualization      |                 | techniques             |
methods

Sensors2023,23,7167 21of32
Table3.Cont.
|                  | Application | Motivationsfor | ContinualLearning |          |         |
| ---------------- | ----------- | -------------- | ----------------- | -------- | ------- |
| Ref. FirstAuthor | Year        |                |                   | Accuracy | Details |
|                  | Field       | DeployingCL    | Models            |          |         |
Developatwo-stage
Incrementalupdating
|     |              | Overcoming |             | Outperform | CLapproachwith |
| --- | ------------ | ---------- | ----------- | ---------- | -------------- |
|     | Videoanomaly |            | ofthememory |            |                |
[112] Doshi 2022 practicalVAD existingmethods featureembeddingand
|     | detection(VAD) | challenges | module, | significantly | kNN-basedRNN |
| --- | -------------- | ---------- | ------- | ------------- | ------------ |
experiencereplay
model
CompareCL
|     | Metal-forming | Providingautomatic    |                   |          |                |
| --- | ------------- | --------------------- | ----------------- | -------- | -------------- |
|     |               |                       | Continuallearning |          | approachesof   |
|     | timeseries    | capabilityforadapting |                   | Improved |                |
|     |               |                       | approachbasedon   |          | regularization |
[113] Maschler 2021 datasetofa formerlylearned performancevs.
|     |               |                | regularization |                  | strategiesonindustrial |
| --- | ------------- | -------------- | -------------- | ---------------- | ---------------------- |
|     | discrete      | knowledgetonew |                | noregularization |                        |
|     |               |                | strategies     |                  | metal-formingdatafor   |
|     | manufacturing | settings       |                |                  |                        |
faultprediction
Real-worldrestrictions
likeindustrial
|     |                 |                   |                   | Promisingresults | Applyelasticweight |
| --- | --------------- | ----------------- | ----------------- | ---------------- | ------------------ |
|     | Faultprediction | espionageandlegal | LSTMalgorithmwith |                  |                    |
|     |                 |                   |                   | forindustrial    | consolidationfor   |
[114] Maschler 2020 inadistributed privacyconcern elasticweight
|     |             |                        |               | automation | distributed,        |
| --- | ----------- | ---------------------- | ------------- | ---------- | ------------------- |
|     | environment | preventthecentralizing | consolidation |            |                     |
|     |             |                        |               | scenarios  | cooperativelearning |
ofdatafromfactories
fortheDLtraining
Developan
|     |     | Addressinghigh-value | Continuallearning |     |     |
| --- | --- | -------------------- | ----------------- | --- | --- |
HMM-basedCL
|     | Auditoryscene | backgroundnoiseand | approachbasedon | Achievehigh |     |
| --- | ------------- | ------------------ | --------------- | ----------- | --- |
[115] Bayram 2020 analysis highcomputational HiddenMarkov accuracy approachwithUED
andretrainingfortime
|     |     | demands | Model |     |     |
| --- | --- | ------- | ----- | --- | --- |
seriesclassification
Prioritized
|            |                  |                    |                     | Ableto          | Formulatethetraffic   |
| ---------- | ---------------- | ------------------ | ------------------- | --------------- | --------------------- |
|            | Evolving         | Addressingthe      | experiencereplay    |                 |                       |
|            |                  |                    |                     | continuously    | flowprediction        |
|            | long-term        | non-stationarydata | strategyfor         |                 |                       |
| [106] Xiao | 2022             |                    |                     | learnandpredict | problemascontinuous   |
|            | streamingtraffic | distributionduring | transferringlearned |                 |                       |
|            |                  |                    |                     | trafficflowover | reinforcementlearning |
|            | flow             | policyevolution    | knowledge           |                 |                       |
|            |                  |                    |                     | time            | task                  |
intothemodel
Transferringthe
|                 |                    |                        | Continuallearning | Outperform    |                    |
| --------------- | ------------------ | ---------------------- | ----------------- | ------------- | ------------------ |
|                 | knowledge          | Addressingproblems     |                   |               | PresentaCLapproach |
|                 |                    |                        | RNNmodelwith      | standard      |                    |
|                 | gainedfromthe      | liketherequirementof   |                   |               | ofanepisodicmemory |
| [116] Schillaci | 2021               |                        | episodicmemory    | memory        |                    |
|                 | greenhouse         | large-scalere-training |                   |               | systemandmemory    |
|                 |                    |                        | replayand         | consolidation |                    |
|                 | researchfacilities | inthenewfacility       |                   |               | consolidation      |
|                 |                    |                        | consolidation     | approaches    |                    |
togreenhouses
|     | In-process | Addressingthelackof |     | Possible | Deploytask-specific |
| --- | ---------- | ------------------- | --- | -------- | ------------------- |
Generator-based
|            | quality | practicalvariability |              | significant | generativemodelsto |
| ---------- | ------- | -------------------- | ------------ | ----------- | ------------------ |
| [94] Gupta | 2021    |                      | RNNcontinual |             |                    |
predictionby amongindustrial performance augmentdatafortarget
manufacturers sensornetworks learningmodule enhancement tasks
As it is NP-Hard to find the optimal CL algorithms which can completely avoid
catastrophicforgetting[117],polynomialtimeheuristicalgorithmshavebeenproposedto
addresstheCFproblems. TheseCLalgorithmscanbeclassifiedintothreefamilies,i.e.,
regularization-basedmethods,replaymethods,andparameterisolationmethods,accord-
ingtothestorageandusagemethodfortask-specificinformationduringthesequential
learningprocess[17]. Combinedapproachesrefertothemixingofthemethodstogether,
andoutstandingresultscanbeobtainedonbenchmarkdatasets[103]. Anotherpossible
taxonomyisofregularization-basedapproach,replay-basedapproach,optimization-based
approach, representation-based approach, and architecture-based approach [18]. This
surveywillfollowthetaxonomyofLangeetal.[17]andMundtetal.[103].

Sensors 2023, 23, x FOR PEER REVIEW 25 of 35
Sensors2023,23,7167 22of32
Figure3. Treediagramofthetaxonomyofthecontinuallearningmethodsforsensortimeseries
classificationandforecasting[93,94,106–116](note: ifapaperusestwomethodsseparatelywith
similarsatisfactoryresults,thepaperwillbelistedunderbothgroups).

Sensors2023,23,7167 23of32
3.1. Regularization-BasedMethods
Regularization-basedmethodsneedtoutilizeanextraregularizationtermintheloss
function for combining previous knowledge during the learning process of new data.
Regularizationmethodsfocusedonhowtopreservepreviousknowledge. Extralossterms
canbedeployedtopreservetheimportantweightsgainedfromthelearningofformer
tasks. Elasticweightconsolidation(EWC)[118],learningwithoutforgetting(LWF)[119],
andknowledgedistillation[120]arepopularregularizationapproaches.
Sah et al. [107] investigated the performance of three recent continual learning ap-
proaches(A-GEM[121],ER-Ring[122],andMC-SGD[123])foraddressingthecatastrophic
forgetting in wearable sensors for activity recognition. In a wearable sensor system, it
isnecessarytohavethecapabilitytomonitorandrecognizeactivitiesacrossusers. This
sequentiallearningprocessisnon-stationaryandchallengingforDeepLearningmethods.
ThePAMAP2dataset[124]ofhumanactivityrecognition,consistingofsensortimeseries
dataofeightsubjectsandtwelvedailyactivities,isusedfortheevaluation. Theresults
showedthatMC-SGDperformedthebestbyreducingnearly29%oftheforgetting,while
itscomputationaltimeisstillmuchlessthanthejoint-tasktrainingtime.
Matteonietal.[108]developedtwobenchmarksofhumanstatemonitoringofdomain-
incrementalscenariosforCLmodels. Innon-stationaryenvironments,recurrentneural
networksfortimeseriesdatacanbeoflargeimportance[110], andinvestigationofthe
networkpropertiesinthesesituationsmayleadtoabetterunderstandingandapplications
ofCLmodels. AsignificantobstaclethathindersthedevelopmentofCLmodelsisthe
shortageofenoughstandardbenchmarksoftimeseriesdatasetsfortheevaluationofthe
CLmodels. ThetwobenchmarkswerederivedfromdatasetsWESAD[125]andASCER-
TAIN [126] of time series classification from physiological sequence data. Different CL
modelswereinvestigatedwiththesetwobenchmarkstounderstandtheeffectsofcatas-
trophicforgettingonrecurrentneuralnetworks. FourcommonCLmodels,i.e.,replay[20],
elastic weight consolidation (EWC) [118], learning without forgetting (LwF) [119], and
naiveandcumulativestrategies,weretested. TheresultsshowedthatalltheCLmodelscan
mitigateforgetting,butbesidesthereplaymodel,allothermodelsstillcannotaccumulate
knowledgeovertime.
Kwonetal.[109]comprehensivelyinvestigatedtheperformanceofthreeCLapproaches
—regularization,replay,andreplaywithexamplesfordeploymentinmobileandembedded
sensing devices. Most of the existing continual learning methods do not consider the
resource requirements and limitations of mobile and embedded sensing devices [127].
Threedatasetsofhumanactivityrecognition,twodatasetsofgesturerecognition,andone
datasetofemotionrecognitionwereinvestigatedtofindthetrade-offsbetweensystem
performance,storagerequirements,computationalpowerrequirements,andpeakmemory
requirements among the CL approaches. The results showed that the CL approach of
replyingwithexemplarsworksbestafterconsideringallthetrade-offs.
Maschler et al. [113] evaluated the performance of a continual learning approach
basedonregularizationstrategies,whichmimicthehumanbrainsynapticconsolidation,
forindustrialapplication. Existingmethodsforanomalydetectionoftenlacktheflexibility
toadapttochangesinthemanufacturingprocesses[113], whilecontinuallearningcan
help overcome this issue by providing the automatic capability for adapting formerly
learned knowledge to new settings. Real-world metal-forming time series dataset of a
discretemanufacturingprocesswastested,showingpromisingresultsfortheregularization
strategiesoverthemultilayerLSTMapproachwithnoregularization. Onlineelasticweight
consolidationisfoundtoprovidebetterperformancethanelasticweightconsolidation.
Maschler et al. [128] evaluated the performance of the regularization strategies against
theopen-accesslithium-ionbatterydegradationdataset[129]withtheLSTMapproach
for remaining useful lifetime prediction for lithium-ion batteries. The results of these
degradationdatasetsreinforcethefindingsforthediscretemanufacturingprocess.Network
monitoringcanproduceahugeamountofmultivariatetimeseriesdatathatareuseful
forusage,likenetworkanomalydetection. Gonzalezetal.[130]outlinedtheirconceptual

Sensors2023,23,7167 24of32
frameworkofvariationalautoencodersanddilatedconvolutionalnetworksfornetwork
anomalydetection. Thedeepgenerativereplayisexploredforextendingthecontinual
learning capability to the proposed system. The teacher generative model can create
syntheticdatatoimitateprevioustrainingexamples, whilethenewstudentmodelcan
learnfromcurrentnewdataandalsothesesyntheticdataatthesametime. Thiscontinual
learningmodulemayhelptoaddresscatastrophicforgetting.
Maschleretal.[114]proposedanLSTMalgorithmwithelasticweightconsolidationfor
faultpredictioninadistributedenvironment. Continuallearninghasthepotentialtoserve
asadistributedapproachforfulfillingtheindustrialautomationneed,withDeepLearning
performingfaultpredictionforindustrialautomation. Thisisbecausemanyreal-world
restrictionslikeindustrialespionageandlegalprivacyconcernpreventthecentralizingof
datafromfactoriesforthetrainingoftheDeepLearningmodels. NASAturbofanengine
dataset[131]wasusedforperformanceevaluation. Theexperimentalresultsshowedthat
theirapproachcouldperformeffectivelywithdistributeddatasetswithnorequirementfor
centralizeddatastorage,satisfyingtherequirementsofmanyreal-worldmanufacturers.
Schillacietal.[116]developedacontinuallearningRNNmodelwithepisodicmemory
replayandconsolidationdrivenbypredictionerrorsfortransferringtheknowledgegained
fromthegreenhouseresearchfacilitiestoreal-worldgreenhouses.WithouttheCLcapability,
thisprocessmayotherwisebeexpensiveandriskyforthecropduetoproblemslikethe
requirementoflarge-scalere-traininginthenewfacility. Sensortimeseriesdatamayhelp
tobetterunderstandthecausalmodelsofadynamicsystem,andthisisveryusefulfor
real-worldapplications. Currently,popularcausaldiscoverymethodsutilizeonlystatic
dataorpre-processedtimeseriesdatainadvance,makingthemnotverysuitableforreal-
worldroboticscases. Continuallearningmayaddressthislimitationinthecausaldiscovery
methods [132] but is under-investigated for robot application [133]. Castri et al. [133]
focusedontheconstraint-basedmethodsforcausaldiscoveryandoutlinedtheirapproach
ofre-learningthecausalmodelduringobservedscenariochangesandduringanewsetof
interventions. Thenewinferencematricofthecausalmodelischeckedagainstthematric
oftheoldcausalmodeltodiscoverthestillvalidcausallinksfromtheoldmodelforthe
newmodel. Thisapproachofonlysmallincrementalchangescanhelptheroboticsystem
addresstheCFproblem. CLmodulecanalsohelptheroboticsystemaddressthehardware
resource limitation. Sensors in a greenhouse can produce time series data like climate
time series and leave temperature time series. A better understanding of the complex
greenhouse and modeling of these greenhouse time series data can help to predict the
effectsofinterventionbetter,thusincreasingthecropyield. Memoryretentionisbasedon
congruenceagainstpriorknowledgeretainedinthemodel,andtheexperimentalresults
showed that this memory replay strategy could enhance the performance of standard
memoryconsolidationapproaches.
3.2. ReplayMethods
Replaymethodsneedtostoreeithertherawsamplesorthegeneratedpseudo-samples
fromthegenerativealgorithm. Thesestoredprevioussamplescanbereplayedtoaddress
forgettingduringthelearningofnewtasks. Difficultiesforthisapproachmayincludethe
demandforresourcesoflargestoragecapabilityandtheprivacyconcernsforstoringand
deployingsamplesinreal-worldapplications. Pseudo-rehearsaltechniquescanhandle
thesedifficultieswithagenerativemodelinsteadofstoringpastsamplesdirectly.
Kiyassehetal.[93]utilizedthereplaybufferstrategytoconstructthecontinuallearning
modelCLOPSfromthetemporaldatainclinics,whichisoftennon-stationary,asmultiple
clinical sites with various sensors are involved. Acquisition based on uncertainty was
deployedforthereplayofbufferinstances.Fourclinicalenvironmentsinvolvingtransitions
betweendatamodalities,diseases,clinics,andtimearesuitablenon-stationaryscenarios
totesttheperformanceofthecontinuallearningapproach. TheresultsshowthatCLOPS
performsbetterinthreescenariosthanthetwootherfrontiermethods—GEM[134]and
MIR[135]. He[111]alsofocusedonthetarget-domainincrementalapplicationscenario

Sensors2023,23,7167 25of32
and data-domain incremental application scenario of continual learning and described
howtheirpreviousframework,CLeaR,canbeextendedtolearninputssuccessively. The
frameworkutilizesthestorageofbuffereddatabyanoveltydetector. Theapplicationof
continuallearningtotheregressionscenarioforpowerforecastingwasoutlined.
Doshi and Yilmaz [112] proposed a new continual learning approach for video
anomalydetection. SensorsandcamerasinCCTVsystemsaregeneratinghugeamountsof
real-timevideotemporaldata,anddatasizemaybetoobigtobeinvestigatedbyhumans.
Thereiscurrentlylimitedresearchonthecontinuallearningofthenewvideodata[112].
TheCLcapabilitywasachievedintwoways,bytheincrementalupdatingofthememory
moduleandbyexperiencereplay. Anew,morecomprehensivedatasetwascreated,con-
sistingoftrainingsegmentsinsplitsandtestsegmentstakenfromacamerainastreetin
NewOrleans,USA.Threeexistingbenchmarkdatasets,i.e.,UCSDPed2,CUHKAvenue,
andShanghaiTech,arealsoevaluated. Theexperimentalresultsshowthattheproposed
approachcanperformexcellentlyinovercomingpracticalVADchallenges.
Xiao et al. [106] have recently formulated the evolving long-term streaming traffic
flowproblemofsensortimeseriesdataasacontinuousreinforcementlearningtask. With
theadvancesinDeepQ-Networks(DQNs),whichenablethelearningofcomplicatedrein-
forcementtasks,theresearchonreinforcementlearning(RL)hasgrownenormously[136].
AgentsinDeepRLhaveshownoutstandingperformanceinsettingswithnarrowtasks,
butRLagentsfaceproblemsliketheover-fittingtendencyandthelackofgeneralization
capability to new variations [137]. This is in sharp contrast with the human ability to
learn continually and be adaptive to new scenarios over a lifetime, which is called CL.
DQNs face CF problems [118]. With the policy evolution leading to the non-stationary
data distribution, the CL concept can be applied in RL [104]. In this way, CL methods
maybeusedtoaddresstheCF,andsolvingthisissueiscrucialiftheartificialagentsare
going to have the capability to learn continuously [138]. The continual learner has the
advantageofadaptingandrecoveringefficientlytochangesencounteredovertime[29].
Here,thenextflowvaluepredictoristheagent,thenexttimeseriesflowvalueinthesensor
istheagent,andthedynamicalsensorandtransportationnetworkistheenvironmentstate.
Thegoalistoteachtheautonomousagenttomimicsensorpatternsandtoplanthenext
visitaccordingtothesensorprofile. Prioritizedexperiencereplaystrategyisdeployedto
transferlearnedknowledgeintothemodel,andKLdivergencetoutilizelong-termpattern
intomodelinduction.
3.3. ParameterIsolationMethods
Inparameterisolationmethods,specificmodelparametersareassignedtoeachtask
such that possible forgetting can be avoided. The methods address the CF issues with
theisolationoftask-specificparametersandthendynamicallyadaptthestructureofthe
model.Newmodulesaredeployedforthelearningofnewtaskswhilekeepingtheformerly
learnedparametersunchanged. Aproblemassociatedwiththisapproachisthepotential
growth of network parameters required. Progressive networks [139] and dynamically
expandablenetworks[140]arepopulararchitecturalmethods.
3.4. CombinedApproaches
Combinedapproachesrefertothemixingofthemethodstogether[103].
Cossu et al. [110] conducted a review and evaluation of the continual learning in
RNNs,differentfromthetypicalCLfocusesonfeedforwardandconvolutionalmodels.
Sequentialdataisverypopularinreal-worldapplicationslikerobotics. Thesensorsofthe
roboticssystemcanfeedtherobotwithtimeseriesinputforitswalk,learningindifferent
environments. Yet,asthecurrentfocusofcontinuallearningisonreinforcementlearning
through computer vision, there is not much research on sequential data processing for
continuallearning[110]. Twobenchmarksofspeechrecognitionandhand-drawnsketches
were proposed for the evaluation of different CL methods. The results show that the
forgettingissuesbecomemoreseriousforlongersequences.

Sensors2023,23,7167 26of32
He [111] presented the outline of their explainability module based on techniques
like dimension reduction methods and visualization methods. Currently, there is not
muchresearchwithafocusontheexplainabilityofthecontinuallearningalgorithms[141],
resultingintheproblemslikealackoftransparencyfortheCLmodules. Themodulecan
notonlyprovidethecapabilityofexplanationandvisualizationfortheupdatedneural
networkoftheCLmodulebutalsofortheidentifiedanomaliesaswell. Theidentification
ofanomaliescanbeachievedwithmachinelearningapproachesliketheDeepSupport
VectorDataDescriptionalgorithm,unsupervisedforestalgorithm,andtransformer-based
unsupervisedalgorithm. Thebasicguidelineisthatnoveltiesofscoreshigherthanthe
thresholdshouldbelabeledasanomaliesinsteadoflabelingthemasnewtasksfortheCL.
BayramandInce[115]presentedacontinuallearningapproachbasedontheHidden
MarkovModel(HMM)fortheauditorysceneanalysis(ASA)task. Sensorsystemscan
be deployed to measure the time series data of dynamical acoustic events, and event
recognitionisabouttheidentificationoftheeventsfromtheseacousticsignals. High-value
backgroundnoiseandhighcomputationaldemandsrestrictthedeploymentofcontinual
learningapproachesforthisreal-worldASA.AhierarchicalHMMmoduleisemployedto
evaluateacousticeventrecognitionandunknowneventdetection. Thenewknowledge
gainedfromtheHMMmoduleisusedfortheretrainingofanewHMMmodelinreal-
time in the continual learning module. Multiple acoustic events were evaluated with
theproposedapproachinreal-time,andpromisingresultsofhigheffectivenessandhigh
accuracywereobtained.
Guptaetal.[94]addressedthelackofpracticalvariabilityamongtheindustrialsensor
networksbydeployinganadditional,conditionalmoduletotheirgenerator-basedRNN
continuallearningmodule.Real-timesensortimeseriesdatamaybeusedforthein-process
qualitypredictionbymanufacturers. Therearedifficultiesinlimitingtheapplicationsof
DeepLearningmethodsforqualityprediction,withthemaindifficultiesbeingthecon-
tinuouschangesinthemanufacturingenvironments. Inreal-worldapplicationsofDeep
Learningalgorithms,variousfactoriesmayhavevarioussettings,andtheirsensorenviron-
mentsmaybedifferent. Nevertheless,thecurrentcontinuallearningapproachesdonot
considerthepracticalvariabilityamongthetotalnumbersandtypesofsensorsdeployed
indifferentmanufacturingenvironments[94]. Ininjectionmolding,itisnotuncommon
toproducenewproducts,andthepre-trainedmodelscannotadapttothisnewprocess
well. Tercanetal.[142]developedaCLapproachforthismanufacturingscenariobasedon
thememory-awaresynapsesmethodforthetrainingofANNwithvariousmanufacturing
products. Theexperimentalresultsofinjectionmoldingproductionsupportthatthetrans-
ferofnetworkweightsgainedfromsimilartaskscaneffectivelyraisetheefficiencyofthe
proposedapproach. Graphneuralnetworkwasemployedinthisconditioningmoduleto
controlthedeploymentdynamicsoftheircontinuallearningmodulesuchthattheoverall
systemcanadapttothedifferentsensorsettingsindifferentreal-worldmanufacturingenvi-
ronments[94]. Real-worlddatasets(DSADS[143],HAR[144],andTurbofan—FD001[145])
weretestedbyrandomlyremoving40%ofthesensorsforeachtask. Theexperimental
resultssupportthattheirproposedconditioningGNNmodulecaneffectivelyenhancethe
capabilityofthecontinuallearningmodule.
To summarize, promising results were obtained by the most recent research of CL
applications with sensor time series data records for time series classification and time
seriesforecastingtasks.
4. Conclusions
ThissurveyhaspresentedanoverviewofhowtodeployDeepLearningmethods,
advancedpreprocessingmethods,andcontinuallearningmethodsfortimeseriesclassifica-
tionandforecastingindifferentreal-worldpracticalscenarios. Thereviewhassummarized
theencouragingresultsthatCLcanbedeployedinfieldsbeyondclassificationtasks. The
non-stationary nature of the datasets in many fields poses challenges for conventional
machinelearningandDeepLearningwhileservingasgoodplatformsforinnovativeCL

Sensors2023,23,7167 27of32
applicationsinfutureworks. Anotherveryinterestingdirectionisthatfurtherexperiments
maybedonetoassesstheimpactofarchitecturesversuspreprocessingalgorithmssuchthat
theroleofspecificalgorithmscanbebetterunderstood. Thisisbecause,asobservedinthis
survey,here,themajorityoftheauthorsfocusonthepracticaldeploymentofDLandDL
modelssolely,withoutfurtherevaluatingtheinfluencesofwithandwithoutpreprocessing
algorithmsineachsensorenvironment.
AuthorContributions: Conceptualization,S.-I.A.;formalanalysis,S.-I.A.andH.F.;investigation,
S.-I.A.andH.F.;methodology,S.-I.A.andH.F.;writing,S.-I.A.andH.F.Allauthorshavereadand
agreedtothepublishedversionofthemanuscript.
Funding:Thisresearchreceivednoexternalfunding.
InstitutionalReviewBoardStatement:Notapplicable.
InformedConsentStatement:Notapplicable.
Data Availability Statement: Data sharing is not applicable to this article as no new data were
createdoranalyzedinthisstudy.
ConflictsofInterest:Theauthorsdeclarenoconflictofinterest.
References
1. Asadi,R.;Regan,A.ASpatial-TemporalDecompositionBasedDeepNeuralNetworkforTimeSeriesForecasting. Appl. Soft
Comput.2020,87,105963.[CrossRef]
2. Ao,S.I.AppliedTimeSeriesAnalysisandInnovativeComputing;Springer:Dordrecht,TheNetherlands,2010;ISBN978-90-481-8768-3.
[CrossRef]
3. Plageras,A.P.;Psannis,K.E.;Stergiou,C.;Wang,H.;Gupta,B.B.EfficientIoT-BasedSensorBigDataCollection-Processingand
AnalysisinSmartBuildings.FutureGener.Comput.Syst.2018,82,349–357.[CrossRef]
4. Ao,S.I.;Gelman,L.;Karimi,H.R.;Tiboni,M.AdvancesinMachineLearningforSensingandConditionMonitoring.Appl.Sci.
2022,12,12392.[CrossRef]
5. Ao,S.I.DataMiningandApplicationsinGenomics;Springer:Dordrecht,TheNetherlands,2008;ISBN978-1402089749.[CrossRef]
6. Goodfellow,I.;Bengio,Y.;Courville,A.DeepLearning;MITPress:Cambridge,MA,USA,2016.
7. LeCun,Y.;Bengio,Y.;Hinton,G.DeepLearning.Nature2015,521,436–444.[CrossRef]
8. Zheng,X.C.;Wang,M.;Ordieres-Meré,J.ComparisonofDataPreprocessingApproachesforApplyingDeepLearningtoHuman
ActivityRecognitionintheContextofIndustry4.0.Sensors2018,18,2146.[CrossRef][PubMed]
9. Dablander,F.;Bury,T.DeepLearningforTippingPoints:PreprocessingMatters.Proc.Natl.Acad.Sci.USA2022,119,e2207720119.
[CrossRef]
10. Livieris,I.E.;Stavroyiannis,S.;Pintelas,E.;Pintelas,P.ANovelValidationFrameworktoEnhanceDeepLearningModelsin
Time-SeriesForecasting.NeuralComput.Appl.2020,32,17149–17167.[CrossRef]
11. Guerrier,S.;Molinari,R.;Xu,H.;Zhang,Y.AppliedTimeSeriesAnalysiswithR.2019.Availableonline:http://ts.smac-group.com
(accessedon28July2023).
12. Rhif, M.; Abbes,A.B.; Farah,I.R.; Martinez, B.; Sang, Y.WaveletTransformApplicationfor/inNon-StationaryTime-Series
Analysis:AReview.Appl.Sci.2019,9,1345.[CrossRef]
13. Mahmoud,A.;Mohammed,A.ASurveyonDeepLearningforTime-SeriesForecasting.MachineLearningandBigDataAnalytics
Paradigms:Analysis,ApplicationsandChallenges.Stud.BigData2021,77,365–392.
14. French,R.CatastrophicForgettinginConnectionistNetworks.TrendsCogn.Sci.1999,3,128–135.[CrossRef]
15. Lee,S.;Goldt,S.;Saxe,A.ContinualLearningintheTeacher-StudentSetup:ImpactofTaskSimilarity.InProceedingsofthe38th
InternationalConferenceonMachineLearning,PMLR,Virtual,18–24July2021;Volume139.
16. Shin,H.;Lee,J.K.;Kim,J.;Kim,J.ContinualLearningwithDeepGenerativeReplay.arXiv2017,arXiv:1705.08690.
17. DeLange,M.;Aljundi,R.;Masana,M.;Parisot,S.;Jia,X.;Leonardis,A.;Slabaugh,G.;Tuytelaars,T.AContinualLearningSurvey:
DefyingForgettinginClassificationTasks.IEEETrans.PatternAnal.Mach.Intell.2022,44,3366–3385.
18. Wang,L.;Zhang,X.;Su,H.;Zhu,J.AComprehensiveSurveyofContinualLearning:Theory,MethodandApplication.arXiv
2023,arXiv:2302.00487v2.
19. Hadsell,R.;Rao,D.;Rusu,A.A.;Pascanu,R.EmbracingChange:ContinualLearninginDeepNeuralNetworks.TrendsCogn.Sci.
2020,24,1028–1040.[CrossRef]
20. Hayes, T.L.; Krishnan, G.P.; Bazhenov, M.; Siegelmann, H.T.; Sejnowski, T.J.; Kanan, C.ReplayinDeepLearning: Current
ApproachesandMissingBiologicalElements.NeuralComput.2021,33,2908–2950.[PubMed]
21. Jedlicka,P.; Tomko,M.; Robins,A.; Abraham,W.C.ContributionsbyMetaplasticitytoSolvingtheCatastrophicForgetting
Problem.TrendsNeurosci.2022,45,656–666.[CrossRef][PubMed]

Sensors2023,23,7167 28of32
22. Kudithipudi,D.;Aguilar-Simon,M.;Babb,J.;Bazhenov,M.;Blackiston,D.;Bongard,J.;Brna,A.P.;ChakravarthiRaja,S.;Cheney,
N.;Clune,J.;etal.BiologicalUnderpinningsforLifelongLearningMachines.Nat.Mach.Intell.2022,4,196–210.[CrossRef]
23. Kilickaya,M.;Weijer,J.V.;Asano,Y.TowardsLabel-EfficientIncrementalLearning:Asurvey.arXiv2023,arXiv:2302.00353.
24. Mai,Z.;Li,R.;Jeong,J.;Quispe,D.;Kim,H.;Sanner,S.OnlineContinualLearninginImageClassification:AnEmpiricalSurvey.
Neurocomputing2022,469,28–51.[CrossRef]
25. Masana,M.;Twardowski,B.;Weijer,J.V.OnClassOrderingsforIncrementalLearning.arXiv2020,arXiv:2007.02145.
26. Qu,H.;Rahmani,H.;Xu,L.;Williams,B.;Liu,J.RecentAdvancesofContinualLearninginComputerVision: AnOverview.
arXiv2021,arXiv:2109.11369.
27. Biesialska,M.;Biesialska,K.;Costajussa,M.R.ContinualLifelongLearninginNaturalLanguageProcessing:Asurvey.InProceed-
ingsofthe28thInternationalConferenceonComputationalLinguistics,Barcelona,Spain,8–13December2020;pp.6523–6541.
28. Ke,Z.;Liu,B.ContinualLearningofNaturalLanguageProcessingTasks:ASurvey.arXiv2022,arXiv:2211.12701.
29. Khetarpal,K.;Riemer,M.;Rish,I.;Precup,D.TowardsContinualReinforcementLearning:AReviewandPerspectives.J.Artif.
Intell.Res.2022,75,1401–1476.[CrossRef]
30. Rajagukguk,R.A.;Ramadhan,R.A.A.;Lee,H.J.AReviewonDeepLearningModelsforForecastingTimeSeriesDataofSolar
IrradianceandPhotovoltaicPower.Energies2020,13,6623.[CrossRef]
31. Cai,M.;Pipattanasomporn,M.;Rahman,S.Day-AheadBuilding-LevelLoadForecastsusingDeepLearningvs. Traditional
Time-SeriesTechniques.Appl.Energy2019,236,1078–1088.[CrossRef]
32. Choi,K.;Yi,J.;Park,C.;Yoon,S.DeepLearningforAnomalyDetectioninTime-SeriesData:Review,Analysis,andGuidelines.
IEEEAccess2021,9,120043–120065.
33. Deng, A.; Hooi, B. Graph Neural Network-Based Anomaly Detection in Multivariate Time Series. In Proceedings of the
Thirty-FifthAAAIConferenceonArtificialIntelligence,Online,2–9February2021.
34. Jiang,W.TimeSeriesClassification:NearestNeighborversusDeepLearningModels.SNAppl.Sci.2020,2,721.
35. IsmailFawaz,H.;Forestier,G.;Weber,J.;Idoumghar,L.;Muller,P.A.DeepLearningforTimeSeriesClassification:AReview.
DataMin.Knowl.Discov.2019,33,917–963.
36. Han,T.;Sanchez-Azofeifa,G.A.ADeepLearningTimeSeriesApproachforLeafandWoodClassificationfromTerrestrialLiDAR
PointClouds.RemoteSens.2022,14,3157.[CrossRef]
37. Campos-Taberner,M.;García-Haro,F.J.;Martínez,B.;Izquierdo-Verdiguier,E.;Atzberger,C.;Camps-Valls,G.;Gilabert,M.A.
UnderstandingDeepLearninginLandUseClassificationBasedonSentinel-2TimeSeries.Sci.Rep.2020,10,17188.
38. Naqvi,R.A.;Arsalan,M.;Rehman,A.;Rehman,A.U.;Loh,W.K.;Paul,A.DeepLearning-BasedDriversEmotionClassification
SysteminTimeSeriesDataforRemoteApplications.RemoteSens.2020,12,587.[CrossRef]
39. Zheng,J.;Huang,M.TrafficFlowForecastthroughTimeSeriesAnalysisBasedonDeepLearning.IEEEAccess2020,8,82562–82570.
[CrossRef]
40. Hua,Y.;Zhao,Z.;Li,R.;Chen,X.;Liu,Z.;Zhang,H.DeepLearningwithLongShort-TermMemoryforTimeSeriesPrediction.
IEEECommun.Mag.2019,57,114–119.[CrossRef]
41. Chen,B.;Liu,Y.;Zhang,C.;Wang,Z.TimeSeriesDataforEquipmentReliabilityAnalysiswithDeepLearning.IEEEAccess2020,
8,105484–105493.[CrossRef]
42. Lim,B.;Zohren,S.TimeSeriesForecastingwithDeepLearning:ASurvey.Phil.Trans.R.Soc.A2021,379,20200209.
43. Yasrab,R.;Zhang,J.;Smyth,P.;Pound,M.PredictingPlantGrowthfromTime-SeriesDataUsingDeepLearning.RemoteSens.
2021,13,331.[CrossRef]
44. El-Sappagh,S.;Abuhmed,T.;RiazulIslam,S.M.;Kwak,K.S.MultimodalMultitaskDeepLearningModelforAlzheimer’sDisease
ProgressionDetectionBasedonTimeSeriesData.Neurocomputing2020,412,197–215.
45. Lara-Benitez,P.;Carranza-Garcia,M.;Riquelme,J.AnExperimentalReviewonDeepLearningArchitecturesforTimeSeries
Forecasting.Int.J.NeuralSyst.2021,31,2130001.[CrossRef]
46. Cao,D.;Wang,Y.;Duan,J.;Zhang,C.;Zhu,X.;Huang,C.;Tong,Y.;Xu,B.;Bai,J.;Tong,J.;etal.SpectralTemporalGraphNeural
NetworkforMultivariateTime-seriesForecasting. InProceedingsofthe34thConferenceonNeuralInformationProcessing
Systems,Vancouver,BC,Canada,6–12December2020.
47. Torres,J.F.;Troncoso,A.;Koprinska,I.;Wang,Z.;Martínez-Álvarez,F.DeepLearningforBigDataTimeSeriesForecastingApplied
toSolarPower.InProceedingsoftheInternationalJointConferenceSOCO’18-CISIS’18-ICEUTE’18.SOCO’18-CISIS’18-ICEUTE’18
2018,SanSebastián,Spain,6–8June2018;AdvancesinIntelligentSystemsandComputing.Springer:Cham,Switzerland,2019;
Volume771.
48. Xiao,C.;Chen,N.;Hu,C.;Wang,K.;Xu,Z.;Gai,Y.;Xu,L.;Chen,Z.;Gong,J.ASpatiotemporalDeepLearningModelforSea
SurfaceTemperatureFieldPredictionusingTime-seriesSatelliteData.Environ.Model.Softw.2019,120,104502.[CrossRef]
49. Dau,H.A.;Keogh,E.;Kamgar,K.;Yeh,C.C.M.;Zhu,Y.;Gharghabi,S.;Ratanamahatana,C.A.;Chen,Y.;Hu,B.;Begum,N.;etal.
TheUCRTimeSeriesClassificationArchive.2018.Availableonline:https://www.cs.ucr.edu/~eamonn/time_series_data_2018/
(accessedon20May2023).
50. Jaeger,H.;Haas,H.HarnessingNonlinearity:PredictingChaoticSystemsandSavingEnergyinWirelessCommunication.Science
2004,304,78–80.
51. Bagnall,A.;Lines,J.;Bostrom,A.;Large,J.;Keogh,E.TheGreatTimeSeriesClassificationBakeoff:AReviewandExperimental
EvaluationofRecentAlgorithmicAdvances.DataMin.Knowl.Discov.2017,31,606–660.[PubMed]

Sensors2023,23,7167 29of32
52. Baydogan,M.G.MultivariateTimeSeriesClassificationDatasets.2015.Availableonline:http://www.mustafabaydogan.com
(accessedon28February2019).
53. Borovykh,A.;Bohte,S.;Oosterlee,C.W.ConditionalTimeSeriesForecastingwithConvolutionalNeuralNetworks.arXiv2017,
arXiv:1703.04691.
54. Torres,J.F.;Hadjout,D.;Sebaa,A.;Martinez-Alvarez,F.;Troncoso,A.DeepLearningforTimeSeriesForecasting:ASurvey.Big
Data2021,9,3–21.[PubMed]
55. ClimateCommission.TheCriticalDecade:Australia’sFuture—SolarEnergy;ClimateCommission:Manila,Philippines,2013.
56. Chollet,F.;Allaire,J.DeepLearningwithR;ManningPublications:ShelterIsland,NY,USA,2018.
57. Fan,C.;Wang,J.;Gang,W.;Li,S.Assessmentofdeeprecurrentneuralnetwork-basedstrategiesforshort-termbuildingenergy
predictions.Appl.Energy2019,236,700–710.[CrossRef]
58. Barrera-Animas,A.Y.;Oyedele,L.O.;Bilal,M.;Akinosho,T.D.;Delgado,J.M.D.;Akanbi,L.A.Rainfallprediction:Acomparative
analysisofmodernmachinelearningalgorithmsfortime-seriesforecasting.Mach.Learn.Appl.2022,7,100204.
59. Smyl,S.AHybridMethodofExponentialSmoothingandRecurrentNeuralNetworksforTimeSeriesForecasting.Int.J.Forecast.
2020,36,75–85.[CrossRef]
60. Dang,H.V.;MKohsin,R.;Nguyen,T.V.;Bui-Tien,T.;Nguyen,H.X.DeepLearning-BasedDetectionofStructuralDamageusing
Time-SeriesData.StructureandInfrastructureEngineering.Struct.Infrastruct.Eng.2021,17,1474–1493.[CrossRef]
61. Hochreiter,S.;Schmidhuber,J.LongShort-TermMemory.NeuralComput.1997,9,1735–1780.[CrossRef]
62. Cho,K.;VanMerrienboer,B.;Gulcehre,C.;Bahdanau,D.;Bougares,F.;Schwenk,H.;Bengio,Y.Learningphraserepresentations
usingRNNencoder-decoderforstatisticalmachinetranslation.InProceedingsofthe2014ConferenceonEmpiricalMethodsin
NaturalLanguageProcessing(EMNLP),Doha,Qatar,14–21October2014;pp.1724–1734.
63. Wang,F.;Yu,Y.;Zhang,Z.;Li,J.;Zhen,Z.;Li,K.WaveletDecompositionandConvolutionalLSTMNetworksBasedImproved
DeepLearningModelforSolarIrradianceForecasting.Appl.Sci.2018,8,1286.[CrossRef]
64. He,K.;Zhang,X.;Ren,S.;Sun,J.DeepResidualLearningforImageRecognition.IndianJ.Chem.-Sect.BOrg.Med.Chem.2015,45,
1951–1954.
65. Uhlig,S.;Quoitin,B.;Lepropre,J.;Balon,S.ProvidingPublicIntradomainTrafficMatricestotheResearchCommunity.SIGCOMM
Comput.Commun.Rev.2006,36,83–86.[CrossRef]
66. Shi,X.;Chen,Z.;Wang,H.;Yeung,D.Y.;Wong,W.K.;Woo,W.C.ConvolutionalLSTMNetwork:AMachineLearningApproach
forPrecipitationnowcasting.Adv.NeuralInf.Process.Syst.2015,28,802–810.
67. Yamashita,R.;Nishio,M.;Do,R.K.G.;Togashi,K.ConvolutionalNeuralNetworks:AnOverviewandApplicationinRadiology.
InsightsImaging2018,9,611–629.[PubMed]
68. Scarselli,F.;Gori,M.;Tsoi,A.C.;Hagenbuchner,M.TheGraphNeuralNetworkModel.IEEETrans.NeuralNetw.2009,20,61–80.
[CrossRef][PubMed]
69. Velickovic,P.;Cucurull,G.;Casanova,A.;Romero,A.;Lio,P.;Bengio,Y.GraphAttentionNetworks.arXiv2017,arXiv:1710.10903.
70. Hinton,G.E.;Osindero,S.;Teh,Y.-W.AFastLearningAlgorithmforDeepBeliefNets. NeuralComput. 2006,18,1527–1554.
[CrossRef]
71. Ma,M.;Sun,C.;Chen,X.DeepCouplingAutoencoderforFaultDiagnosiswithMultimodalSensoryData. IEEETrans. Ind.
Inform.2018,14,1137–1145.[CrossRef]
72. Lei,Y.;Karimi,H.R.;Cen,L.;Chen,X.;Xie,Y.Processessoftmodelingbasedonstackedautoencodersandwaveletextreme
learningmachineforaluminumplant-wideapplication.ControlEng.Pract.2021,108,104706.[CrossRef]
73. MohammdiFarsani,E.;Pazouki,E.ATransformerSelfAttentionModelforTimeSeriesForecasting.J.Electr.Comput.Eng.Innov.
2021,9,1–10.
74. Elsayed,S.;Thyssens,D.;Rashed,A.;Jomaa,H.S.;Schmidt-Thieme,L.DoWeReallyNeedDeepLearningModelsforTimeSeries
Forecasting?arXiv2021,arXiv:2101.02118v2.
75. Kanani,P.;Padole,M.ECGHeartbeatArrhythmiaClassificationUsingTime-SeriesAugmentedSignalsandDeepLearning
Approach.ProcediaComput.Sci.2020,171,524–531.[CrossRef]
76. Kisa, D.H.; Ozdemir, M.A.; Guren, O.; Akan, A. EMG based Hand Gesture Classification using Empirical Mode Decom-
position Time-Series and Deep Learning. In Proceedings of the 2020 Medical Technologies Congress, Antalya, Turkey,
19–20November2020.
77. CastroFilho,H.C.;CarvalhoJunior,O.A.;Carvalho,O.L.F.;Bem,P.P.;Moura,R.S.;Albuquerque,A.O.;Silva,C.R.;Ferreira,P.H.G.;
Guimaraes,R.F.;Gomes,R.A.T.RiceCropDetectionUsingLSTM,Bi-LSTM,andMachineLearningModelsfromSentinel-1Time
Series.RemoteSens.2020,12,2655.[CrossRef]
78. RuBwurm,M.;Korner,M.Self-AttentionforRawOpticalSatelliteTimeSeriesClassification.J.Photogramm.RemoteSens.2020,
169,421–435.
79. Kingphai,K.;Moshfeghi,Y.EEG-basedMentalWorkloadLevelEstimationusingDeepLearningModels.InErgonomics&Human
Factors;CIEHF:Birmingham,UK,2022.
80. Yokkampon,U.; Mowshowitz,A.; Chumkamon,S.; Hayashi,E.RobustUnsupervisedAnomalyDetectionwithVariational
AutoencoderinMultivariateTimeSeriesData.IEEEAccess2022,10,57835–57849.[CrossRef]
81. Mishra,S.;Bordin,C.;Taharaguchi,K.;Palu,I.ComparisonofDeepLearningModelsforMultivariatePredictionofTimeSeries
WindPowerGenerationandTemperature.EnergyRep.2020,6,273–286.[CrossRef]

Sensors2023,23,7167 30of32
82. Wen,Q.S.;Sun,L.;Yang,F.;Song,X.;Gao,J.;Wang,X.;Xu,H.TimeSeriesDataAugmentationforDeepLearning: ASurvey.
In Proceedings of the Thirtieth International Joint Conference on Artificial Intelligence (IJCAI-21), Montréal, QC, Canada,
19–27August2021;pp.4653–4660.
83. Azar, J.; Makhoul, A.; Couturier, R.; Demerjian, J.RobustIoTTimeSeriesClassificationwithDataCompressionandDeep
Learning.Neurocomputing2020,398,222–234.[CrossRef]
84. Savitzky,A.;Golay,M.J.E.SmoothingandDierentiationofDatabySimplifiedLeastSquaresProcedures.Anal.Chem.1964,36,
1627–1639.[CrossRef]
85. Vaswani, A.; Shazeer, N.; Parmar, N.; Uszkoreit, J.; Jones, L.; Gomez, A.N.; Kaiser, L.; Polosukhin, I. Attention is all you
need.InProceedingsoftheAdvancesinNeuralInformationProcessingSystems,LongBeach,CA,USA,4–9December2017;
pp.5998–6008.
86. Mognon,A.;Jovicich,J.;Bruzzone,L.;Buiatti,M.Adjust:AnAutomaticEEGArtifactDetectorBasedontheJointUseofSpatial
andTemporalFeatures.Psychophysiology2011,48,229–240.
87. Kingphai,K.;Moshfeghi,Y.OnEEGPreprocessingRoleinDeepLearningEffectivenessforMentalWorkloadClassification.
InInternationalSymposiumonHumanMentalWorkload: ModelsandApplications;Springer: Berlin/Heidelberg,Germany,2021;
pp.81–98.
88. Chalapathy,R.;Chawla,S.DeepLearningforAnomalyDetection:ASurvey.arXiv2019,arXiv:1901.03407.
89. Le,T.T.;Fu,W.;Moore,J.H.ScalingTree-BasedAutomatedMachineLearningtoBiomedicalBigDatawithaFeatureSetSelector.
Bioinformatics2020,36,250–256.[CrossRef]
90. Bahdanau, D.; Cho, K.; Bengio, Y. Neural Machine Translation by Jointly Learning to Align and Translate. arXiv 2014,
arXiv:1409.0473.
91. Livieris,I.;Stavroyiannis,S.;Iliadis,L.;Pintelas,P.SmoothingandStationarityEnforcementFrameworkforDeepLearning
Time-SeriesForecasting.NeuralComput.Appl.2021,33,14021–14035.[CrossRef][PubMed]
92. He,Y.;Huang,Z.;Sick,B.TowardApplicationofContinuousPowerForecastsinaRegionalFlexibilityMarket.InProceedingsof
the2021InternationalJointConferenceonNeuralNetworks(IJCNN),Shenzhen,China,18–22July2021;pp.1–8.
93. Kiyasseh,D.;Zhu,T.;Clifton,D.AClinicalDeepLearningFrameworkforContinuallyLearningfromCardiacSignalsacross
Diseases,Time,Modalities,andInstitutions.Nat.Commun.2021,12,4221.[CrossRef]
94. Gupta,V.;Narwariya,J.;Malhotra,P.;Vig,L.;Shroff,G.ContinualLearningforMultivariateTimeSeriesTaskswithVariable
InputDimensions.InProceedingsofthe2021IEEEInternationalConferenceonDataMining(ICDM),Auckland,NewZealand,
7–10December2021;pp.161–170.
95. Flesch,T.;Balaguer,J.;Dekker,R.;Nili,H.;Summerfield,C.ComparingContinualTaskLearninginMindsandMachines.Proc.
Natl.Acad.Sci.USA2018,115,E10313–E10322.[CrossRef][PubMed]
96. Shaheen, K.; Hanif, M.A.; Hasan, O.; Shafique, M. Continual Learning for Real-World Autonomous Systems: Algorithms,
ChallengesandFrameworks.J.Intell.Robot.Syst.2022,105,9.
97. Pfulb,B.;Gepperth,A.AComprehensive,Application-OrientedStudyofCatastrophicForgettinginDNNs.InProceedingsofthe
InternationalConferenceonLearningRepresentations(ICLR),NewOrleans,LA,USA,6–9May2019.
98. Prabhu,A.;Torr,P.;Dokania,P.Gdumb:ASimpleApproachthatQuestionsOurProgressinContinualLearning.InEuropean
ConferenceonComputerVision;Springer:Berlin/Heidelberg,Germany,2020;pp.524–540.
99. He,Y.;Sick,B.CLeaR:AnAdaptiveContinualLearningFrameworkforRegressionTasks.AIPerspect.2021,3,2.
100. Philps, D.; Weyde, T.; Garcez, A.D.A.; Batchelor, R. Continual Learning Augmented Investment Decisions. arXiv 2019,
arXiv:1812.02340v4.
101. Chen,X.;Wang,J.;Xie,K.TrafficStream:AStreamingTrafficFlowForecastingFrameworkBasedonGraphNeuralNetworks
andContinualLearning.InProceedingsoftheThirtiethInternationalJointConferenceonArtificialIntelligence,Montreal,QC,
Canada,19–27August2021.
102. Lesort, T.; George, T.; Rish, I. Continual learning in Deep Neural Networks: An Analysis of the Last Layer. arXiv 2021,
arXiv:2106.01834.
103. Mundt,M.;Hong,Y.;Pliushch,I.;Ramesh,V.AWholisticViewofContinualLearningwithDeepNeuralNetworks:Forgotten
LessonsandtheBridgetoActiveandOpenWorldLearning.NeuralNetw.2023,160,306–336.
104. Bagus,B.;Gepperth,A.;Lesort,T.BeyondSupervisedContinualLearning:AReview.InProceedingsoftheEuropeanSymposium
onArtificialNeuralNetworks,ComputationalIntelligenceandMachineLearning,Bruges,Belgium,5–7October2022.
105. Pham,Q.;Liu,C.;Sahoo,D.;Hoi,S.C.LearningFastandSlowforOnlineTimeSeriesForecasting.arXiv2022,arXiv:2202.11672v2.
106. Xiao,Y.;Liu,M.;Zhang,Z.;Jiang,L.;Yin,M.;Wang,J.StreamingTrafficFlowPredictionBasedonContinuousReinforcement
Learning.arXiv2022,arXiv:2212.12767v1.
107. Sah, R.K.; Mirzadeh, S.I.; Ghasemzadeh, H. Continual Learning for Activity Recognition. In Proceedings of the 2022 44th
AnnualInternationalConferenceoftheIEEEEngineeringinMedicine&BiologySociety(EMBC),Scotland,UK,11–15July2022;
pp.2416–2420.
108. Matteoni,F.;Cossu,A.;Gallicchio,C.;Lomonaco,V.;Bacciu,D.ContinualLearningforHumanStateMonitoring.InProceedings
oftheESANN2022Proceedings,EuropeanSymposiumonArtificialNeuralNetworks,ComputationalIntelligenceandMachine
Learning,Bruges,Belgium,5–7October2022.

Sensors2023,23,7167 31of32
109. Kwon,Y.D.;Chauhan,J.;Kumar,A.;Hui,P.;Mascolo,C.ExploringSystemPerformanceofContinualLearningforMobileand
EmbeddedSensingApplications.InProceedingsofthe2021IEEE/ACMSymposiumonEdgeComputing(SEC),SanJose,CA,
USA,14–17December2021;pp.319–332.
110. Cossu,A.;Carta,A.;Lomonaco,V.;Bacciu,D.ContinualLearningforRecurrentNeuralNetworks:AnEmpiricalEvaluation.
NeuralNetw.2021,143,607–627.[CrossRef][PubMed]
111. He,Y.AdaptiveExplainableContinualLearningFrameworkforRegressionProblemswithFocusonPowerForecasts.arXiv2022,
arXiv:2108.10781v2.
112. Doshi, K.; Yilmaz, Y. Rethinking Video Anomaly Detection—A Continual Learning Approach. In Proceedings of the 2022
IEEE/CVFWinterConferenceonApplicationsofComputerVision(WACV),Waikoloa,HI,USA,4–8January2022;pp.3036–3045.
113. Maschler,B.;Pham,T.T.H.;Weyrich,M.Regularization-basedContinualLearningforAnomalyDetectioninDiscreteManufac-
turing.InProceedingsofthe54thCIRPConferenceonManufacturingSystems,ProcediaCIRP,Virtual,22–24September2021;
Volume104,pp.452–457.
114. Maschler,B.;Vietz,H.;Jazdi,N.;Weyrich,M.ContinualLearningofFaultPredictionforTurbofanEnginesusingDeepLearning
withElasticWeightConsolidation.InProceedingsofthe202025thIEEEInternationalConferenceonEmergingTechnologiesand
FactoryAutomation,Vienna,Austria,8–11September2020;pp.959–966.
115. Bayram,B.;Ince,G.RealTimeAuditorySceneAnalysisusingContinualLearninginRealEnvironments.Eur.J.Sci.Technol.2020,
215–226,EjosatSpecialIssue2020(HORA).[CrossRef]
116. Schillaci,G.;Schmidt,U.;Miranda,L.PredictionError-DrivenMemoryConsolidationforContinualLearning:OntheCaseof
AdaptiveGreenhouseModels.KI—KünstlicheIntell.2021,35,71–80.
117. Knoblauch,J.;Husain,H.;Diethe,T.OptimalContinualLearninghasPerfectMemoryandisNP-HARD.InProceedingsofthe
37thInternationalConferenceonMachineLearning,Virtual,13–18July2020;pp.5327–5337.
118. Kirkpatrick,J.;Pascanu,R.;Rabinowitz,N.;Veness,J.;Desjardins,G.;Rusu,A.A.;Milan,K.;Quan,J.;Ramalho,T.;Grabska-
Barwinska,A.;etal.OvercomingCatastrophicForgettinginNeuralNetworks.Proc.Natl.Acad.Sci.USA2017,114,3521–3526.
[CrossRef]
119. Li,Z.;Hoiem,D.LearningwithoutForgetting.IEEETrans.PatternAnal.Mach.Intell.2017,40,2935–2947.[CrossRef]
120. Wei,H.R.;Huang,S.;Wang,R.;Dai,X.;Chen,J.OnlineDistillingfromCheckpointsforNeuralMachineTranslation.InProceedings
ofthe2019ConferenceoftheNorthAmericanChapteroftheAssociationforComputationalLinguistics: HumanLanguage
Technologies,Minneapolis,MN,USA,2–7June2019;Volume1,pp.1932–1941.
121. Chaudhry, A.; Ranzato, M.; Rohrbach, M.; Elhoseiny, M. Efficient Lifelong Learning with A-GEM. In Proceedings of the
InternationalConferenceonLearningRepresentations,Vancouver,Canada,30April-3May2018.
122. Chaudhry,A.;Rohrbach,M.;Elhoseiny,M.;Ajanthan,T.;Dokania,P.K.;Torr,P.H.S.;Ranzato,M.OnTinyEpisodicMemoriesin
ContinualLearning.arXiv2019,arXiv:1902.10486.
123. Mirzadeh,S.I.;Farajtabar,M.;Gorur,D.;Pascanu,R.;Ghasemzadeh,H.LinearModeConnectivityinMultitaskandContin-
ual Learning. In Proceedings of the ICLR 2021: The Ninth International Conference on Learning Representations, Virtual,
3–7May2021.
124. Reiss,A.;Stricker,D.IntroducingaNewBenchmarkedDatasetforActivityMonitoring.InProceedingsofthe16thInternational
SymposiumonWearableComputers,NewcastleUK,18–22June2012;pp.108–109.
125. Schmidt,P.;Reiss,A.;Duerichen,R.;Marberger,C.;VanLaerhoven,K.IntroducingWESAD,aMultimodalDatasetforWearable
StressandAffectDetection.InProceedingsofthe20thACMInternationalConferenceonMultimodalInteraction,ICMI2018,
NewYork,NY,USA,16–20October2018;pp.400–408.
126. Subramanian,R.;Wache,J.;Abadi,M.K.;Vieriu,R.L.;Winkler,S.;Sebe,N.ASCERTAIN:EmotionandPersonalityRecognition
usingCommercialSensors.IEEETrans.Affect.Comput.2018,9,147–160.[CrossRef]
127. Lee, S.W.; Kim, J.H.; Jun, J.; Ha, J.W.; Zhang, B.T. Overcoming Catastrophic Forgetting by Incremental Moment Matching.
InAdvancesinNeuralInformationProcessingSystems;CurranAssociates,Inc.:RedHook,NY,USA,2017;Volume30,pp.4652–4662.
128. Maschler,B.;Tatiyosyan,S.;Weyrich,M.Regularization-BasedContinualLearningforFaultPredictioninLithium-IonBatteries.
ProcediaCIRP2022,112,513–518.[CrossRef]
129. Eker,O.;Camci,F.;Jennions,I.MajorChallengesinPrognostics:StudyonBenchmarkingPrognosticsDatasets.InProceedings
ofthe20121stEuropeanConferenceofthePrognosticsandHealthManagementSociety,Dresden,Germany,3–6July2012;
pp.148–155.
130. Gonzalez,G.G.;Casas,P.;Fernandez,A.;Gomez,G.StepstowardsContinualLearninginMultivariateTime-SeriesAnomaly
DetectionusingVariationalAutoencoders.InProceedingsofthe22ndACMInternetMeasurementConference,IMC’22,Nice,
France,25–27October2022.
131. Saxena,A.;Goebel,K.TurbofanEngineDegradationSimulationDataSet;NASAAmesPrognosticsDataRepository:MoffettField,
CA,USA,2008.
132. Glymour,C.;Zhang,K.;Spirtes,P.ReviewofCausalDiscoveryMethodsBasedonGraphicalModels.Front.Genet.2019,10,524.
[CrossRef][PubMed]
133. Castri,L.;Mghames,S.;Bellotto,N.FromContinualLearningtoCausalDiscoveryinRobotics.arXiv2023,arXiv:2301.03886v1.
134. Lopez-Paz,D.;Ranzato,M.GradientEpisodicMemoryforContinualLearning.Adv.Neural.Inf.Process.Syst.2017,30,6467–6476.

Sensors2023,23,7167 32of32
135. Aljundi,R.;Caccia,L.;Belilovsky,E.;Caccia,M.;Lin,M.;Charlin,L.;Tuytelaars,T.OnlineContinualLearningwithMaximal
InterferedRetrieval.Adv.Neural.Inf.Process.Syst.2019,32,11849–11860.
136. Mnih, V.; Kavukcuoglu, K.; Silver, D.; Rusu, A.A.; Veness, J.; Bellemare, M.G.; Graves, A.; Riedmiller, M.; Fidjeland, A.K.;
Ostrovski,G.;etal.Human-LevelControlthroughDeepReinforcementLearning.Nature2015,518,529–533.[CrossRef]
137. Bengio,E.;Pineau,J.;Precup,D.InterferenceandGeneralizationinTemporalDifferenceLearning.arXiv2020,arXiv:2003.06350.
138. Atkinson, C.; McCane, B.; Szymanski, L.; Robins, A. Pseudo-Rehearsal: Achieving Deep Reinforcement Learning without
CatastrophicForgetting.Neurocomputing2021,428,291–307.
139. Rusu,A.A.;Rabinowitz,N.C.;Desjardins,G.;Soyer,H.;Kirkpatrick,J.;Kavukcuoglu,K.;Pascanu,R.;Hadsell,R.Progressive
NeuralNetworks.arXiv2016,arXiv:1606.04671.
140. Yoon,J.;Yang,E.;Lee,J.;Hwang,S.J.LifelongLearningwithDynamicallyExpandableNetworks.arXiv2017,arXiv:1708.01547.
141. He,Y.;Huang,Z.;Sick,B.DesignofExplainabilityModulewithExpertsintheLoopforVisualizationandDynamicAdjustment
of Continual Learning. In Proceedings of the AAAI-22 Workshop on Interactive Machine Learning, Vancouver, Canada,
28February-1March2022.
142. Tercan,H.;Deibert,P.;Meisen,T.ContinualLearningofNeuralNetworksforQualityPredictioninProductionUsingMemory
AwareSynapsesandWeightTransfer.J.Intell.Manuf.2022,33,283–292.[CrossRef]
143. Altun,K.;Barshan,B.HumanActivityRecognitionusingInertial/MagneticSensorUnits.InInternationalWorkshoponHuman
BehaviorUnderstanding;Springer:Berlin/Heidelberg,Germany,2010;pp.38–51.
144. Anguita,D.;Ghio,A.;Oneto,L.;Parra,X.;Reyes-Ortiz,J.L.HumanActivityRecognitiononSmartphonesusingaMulticlass
Hardware-FriendlySupportVectorMachine.InInternationalWorkshoponAmbientAssistedLiving;Springer:Berlin/Heidelberg,
Germany,2012;pp.216–223.
145. Saxena,A.;Goebel,K.;Simon,D.;Eklund,N.DamagePropagationModelingforAircraftEngineRun-to-FailureSimulation.
InProceedingsofthe2008InternationalConferenceonPrognosticsandHealthManagement,Denver,CO,USA,6–9October
2008;pp.1–9.
Disclaimer/Publisher’s Note: The statements, opinions and data contained in all publications are solely those of the individual
author(s)andcontributor(s)andnotofMDPIand/ortheeditor(s).MDPIand/ortheeditor(s)disclaimresponsibilityforanyinjuryto
peopleorpropertyresultingfromanyideas,methods,instructionsorproductsreferredtointhecontent.