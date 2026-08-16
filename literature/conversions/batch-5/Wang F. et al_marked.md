---
conversion_metadata:
  converted_at: "2026-07-21T09:13:22Z"
  converter_tool: "markitdown"
  converter_version: "0.1.6"
  source_pdf: "Wang F. et al.pdf"
  source_pdf_sha256: "bc7e6e17da94d05767debb0079cc7a1db28bcf9e23157de1047585b8f4ccf466"
  page_count: 27
  markdown_char_count: 196471
---

<!-- PAGE-AWARE EXTRACTION (via pdfminer.six) -->

<!-- PAGE 1 -->

Review
A Survey of Deep Anomaly Detection in Multivariate Time
Series: Taxonomy, Applications, and Directions

Fengling Wang 1, Yiyue Jiang 1, Rongjie Zhang 2, Aimin Wei 3, Jingming Xie 4,* and Xiongwen Pang 2,*

1

2

3

School of Artificial Intelligence, South China Normal University, Foshan 528000, China;
wfl314159@163.com (F.W.); jiangyy@m.scnu.edu.cn (Y.J.)
School of Computer Science, South China Normal University, Guangzhou 510555, China; zrj22127@gmail.com
School of Architectural Engineering, Guangzhou Panyu Polytechnic College, Guangzhou 511483, China;
weiam@gzpyp.edu.cn

4 Doctoral Workstation, Guangdong Songshan Polytechnic, Shaoguan 512126, China
* Correspondence: xiejm@gdsspt.edu.cn (J.X.); augepang@scnu.edu.cn (X.P.)

Abstract: Multivariate time series anomaly detection (MTSAD) can effectively identify
and analyze anomalous behavior in complex systems, which is particularly important in
fields such as financial monitoring, industrial equipment fault detection, and cybersecu-
rity. MTSAD requires simultaneously analyze temporal dependencies and inter-variable
relationships have prompted researchers to develop specialized deep learning models to
detect anomalous patterns. In this paper, we conducted a structured and comprehensive
overview of the latest techniques in deep learning for multivariate time series anomaly
detection methods. Firstly, we proposed a taxonomy for the anomaly detection strategies
from the perspectives of learning paradigms and deep learning models, and then provide a
systematic review that emphasizes their advantages and drawbacks. We also organized the
public datasets for time series anomaly detection along with their respective application
domains. Finally, open issues for future research on MTSAD were identified.

Keywords: anomaly detection; deep learning network; multivariate time series

Academic Editors: Jongmyon Kim

and George D. Magoulas

1. Introduction

Received: 19 November 2024

Revised: 25 December 2024

Accepted: 30 December 2024

Published: 1 January 2025

Citation: Wang, F.; Jiang, Y.; Zhang,

R.; Wei, A.; Xie, J.; Pang, X. A Survey

of Deep Anomaly Detection in

Multivariate Time Series: Taxonomy,

Applications, and Directions. Sensors

2025, 25, 190. https://doi.org/

10.3390/s25010190

Copyright: © 2025 by the authors.

Licensee MDPI, Basel, Switzerland.

This article is an open access article

distributed under the terms and

conditions of the Creative Commons

Attribution (CC BY) license

(https://creativecommons.org/

licenses/by/4.0/).

Time series anomaly detection is crucial in data analysis, focusing on identifying
unusual patterns in time series data that significantly differ from expected behavior [1,2].
This task becomes more intricate in MTSAD, which it involves multiple channels or variates
of data. The evolution of sensing technologies and enhancements in data storage have
propelled the adoption of anomaly detection across a spectrum of sectors. For example, In
the financial services sector, it is used in financial services to identify fraudulent transactions
and market fluctuations, protecting customer funds [3]. In the industrial sector, it monitors
equipment status to detect faults early, reducing downtime and maintenance costs [4].

Multivariate time series anomaly detection has been studied in a variety of application
domains and has experienced significant progress. There exist various methods proposed
for MTSAD, including statistical methods, classical methods, distance-based methods [5],
distributional-based methods [6], and density-based methods [7], are still a viable choice
of algorithm. Statistical techniques typically involve moving averages(MA) and the au-
toregressive integrated moving average (ARIMA) [8]. MA reduce the impact of random
fluctuations by calculating the average value within a specific time window, thereby reveal-
ing trends and patterns in the data. The ARIMA model is a popular time series forecasting
method that combines three components: AutoRegressive (AR), Integrated (I), and MA,

Sensors 2025, 25, 190

https://doi.org/10.3390/s25010190

---

<!-- PAGE 2 -->

Sensors 2025, 25, 190

2 of 27

which are used to model and predict time series data. Classical machine learning methods
include One-Class Support Vector Machine (OCSVM) [9] and Support Vector Data Descrip-
tion (SVDD) [10]. SVDD is similar to OCSVM, but instead of finding just a boundary, it cre-
ates a hypersphere that contains the normal data. Any data points outside this hypersphere
are considered anomalies. Distance-based techniques assess the deviation of observations
from representative data points using distance metrics, while distributional methods focus
on identifying anomalies through points with low likelihood. Density-based methods are
based on the local density of data points. If a data point has significantly lower local density
compared to its neighboring area, it may be flagged as an anomaly. However, as target
systems grow in size and complexity, these methods encounter challenges, particularly
their limitations in handling multidimensional data and the lack of labeled anomalies [11].
The challenge of MTSAD lies in the need to consider both the dynamic changes along
the temporal dimension and the interrelationships between observations simultaneously.
Recently, deep learning-based techniques have advanced the field of anomaly detection
within multi-dimensional datasets. These methods exploit powerful deep learning models
like Transformers [12–14], GNN [15], VAEs [16], GANs [17], Diffusion [18] etc., are adept at
representing intricate, non-linear relationships among various sensors and are proficient in
capturing temporal correlations and ependencies effectively [19]. These advanced models
leverage the capabilities of deep learning to identify and learn subtle patterns in data,
enabling accurate identification and early warning of anomalous behaviors across various
fields such as financial transaction monitoring, cybersecurity threat detection, industrial
equipment maintenance forecasting, and healthcare monitoring. The progress of these
technologies allows us to better understand and analyze the complex dynamics within
multi-dimensional datasets, providing powerful tools for real-time anomaly detection and
decision support systems.

In this paper, we aim to address the current knowledge gap by exploring features of
time series, types of anomalies, and offering a thorough overview of recent advancements
in deep learning techniques for MTSAD. It reviews the latest deep learning methods for
this purpose from three perspectives and offers a comprehensive discussion about the
classification of deep learning models. Additionally, it compiles and organizes public
datasets for time series anomaly detection, along with their respective application domains.
Finally, the paper wraps up by highlighting possible directions for future research to further
develop the field.

In summary, the contributions of this paper include:
(1) The investigation and review of anomaly categories in multivariate time series

have proposed a new classification;

(2) Focusing on learning paradigms and neural network architectures, we conducted
a comprehensive review of the latest deep learning methods from three strategies and
proposed a new taxonomy for MTSAD;

(3) An exploration of future research opportunities for MTSAD.

2. Background and Preliminary
2.1. Problem Definition

MTSAD refers to the process of identifying anomalous behavior or patterns that devi-
ate significantly from historical patterns within the context of multiple related time series.
Compared to univariate time series anomaly detection, multivariate anomaly detection is
more complex as it requires consideration of the relationships and temporal dependencies
between multiple variables simultaneously [20]. Anomaly score is an indicator used to
measure the degree of anomaly of a time point or time windows. The higher the anomaly
score, the more likely the data point is to be anomalous.

---

<!-- PAGE 3 -->

Sensors 2025, 25, 190

3 of 27

We consider a collection of MTS denoted as X. Hence, the definition can be expressed

as follows:

X = (x1, x2, ..., xC)

xc = (x1, x2, ..., xT)

(1)

(2)

where xc ∈ RT represents an T-dimensional vector, each data point xt ∈ R is acquired at
a certain timestamp t from a sensor. T represents the length of lookback windows and C
represents the number of dimensions or variables(C > 1).

Given a multidimensional time series dataset X ∈ RTXC, the goal is to find a method

to compute anomaly scores:

S = (s1, s2, ..., sT)

(3)

where st ∈ R denotes the anomaly score at time point t. This allows us to identify anomalous
data points that deviate from normal behavior.

2.2. Anomaly Types in MTS

MTS consists of a set of univariate time series(metric), each of which describes different
parts or attributes of a complex entity. Therefore, it not only has temporal dependencies
within the metrics, manifested as periodic, trend, and other inherent patterns of each
metric, but also inter-metrics dependencies within the entity, representing the linear or
nonlinear relationships between all metrics of the entity at each time point [2,21]. Thus,
anomalies in MTS can be divided into intra-metric anomalies (temporal anomalies) and
inter-metric anomalies. The overall classification framework for anomaly types is shown in
Figure 1. Temporal anomalies occur in multivariate, affecting multiple or all dimensions.
Temporal anomalies primarily focus on individual data points and subsequences. Point-
wise anomalies refer to unexpected events at a single time point, where the anomalous
behavior of a time point can be a spike or glitch. Pattern-wise anomalies are anomalous
subsequences, usually discordant or disharmonious. Here are the definitions of types
of anomalies:

Figure 1. The overall classification framework diagram for multivariate time series anomaly types.

2.2.1. Point-Wise Anomalies

Global point anomaly: Global point anomaly is an anomaly in which a single data
point is significantly different from other data. They are typically spikes in the entire
sequence. Considering a threshold δ, it can be described as:

|xt − ˆxt| > δ

(4)

---

<!-- PAGE 4 -->

Sensors 2025, 25, 190

4 of 27

where xt is expected value and ˆxt is the output of the model, δ = λ ∗ G(xt), G represents
the variance of the context over xt, and λ is the threshold adjustment coefficient.

Local point Anomaly: Local point anomaly refers to abnormal situations that occur
within specific environments or contexts. Detecting local point anomaly typically involves
analyzing both the point and its associated contextual information to identify behavior
that deviates from the expected norms within a given context. This type of anomaly can be
defined as:

δ ≈ λ ∗ L(xt−k : xt+k)

(5)

where xt−k : xt+k = (xt−k, xt−k+1, ..., xt+k) refers to the context of the data point xt with
a window size k, L represents the variance of this local context. An example of point
anomalies are shown on Figure 2a, global point anomalies typically stand out against the
backdrop of the entire time series, while local point anomalies contrast more with the data
points immediately adjacent to them.

Figure 2. (a) Point-wise anomalies, the red dots indicate anomalies, and (b) Patten-wise anomalies,
the red areas represent anomalies.

2.2.2. Pattern-Wise Anomalies

Shapelet anomaly: Shapelet anomalies are circumstance that occurs in a particular
environment or context. Unlike individual data point anomalies, shapelet anomaliy indi-
cates that the collective behavior of a group of related data significantly deviates from the
expected or normal pattern, as shown in Figure 2b.

dissp(p, ˆp) > δ

(6)

where ˆp specifies the expected shape of the subsequence. diss is a function that measures
the difference between two subsequences.

Trend anomaly: Trend anomalies focus on sudden changes or deviations from the
long-term trend in the data. These anomalies may result from sudden events, systemic
changes, or other factors leading to abrupt shifts or abnormal growth or decline in the
trend direction.

dissτ(τ, ˆτ) > δ

(7)

where ˆτ is the trend of normal subsequences.

Cycle Anomaly: Cycle anomalies occur when there are abnormal changes in the
periodic patterns of time series data. For example, there is anomaly in the frequency or
intensity of a seasonal event.

disss(s, ˆs) > δ

(8)

---

<!-- PAGE 5 -->

Sensors 2025, 25, 190

5 of 27

where ˆs is the cyclicity of expected subsequences.

2.2.3. Inter-Metric Anomalies

Global intermetric anomaly: Certain metrics in MTS experience significant changes,
with a length matching the entire sequence. This type of anomaly typically occurs when
initial parameters or system states deviate from the normal range. When the change in a
key metric triggers a series of abnormal fluctuations in related metrics, the entire sequence
reflects this anomaly. An example of an entire sequence anomaly is shown in Figure 3a, as
its behavior significantly deviates from that of other metrics.

disscorr(corr(xi, xj)) > δ

(9)

where xi, and xj are different metrics, and corr represents the degree of correlation be-
tween them.

Figure 3. (a) Global intermetric anomalies. (b) The red-highlighted area on the left indicates local
intermetric anomalies, while the red-highlighted area on the right indicates temporal-local intermet-
ric anomalies.

Local intermetric anomaly: There is correlation between metrics within the entity,
which can be linear or nonlinear, such as the relationship between temperature and electric-
ity consumption. If these correlations are disrupted, MTS will exhibit anomalous behavior.
During a certain time period, the relationships between metrics significantly deviate from
historical patterns, suggesting a change in the interdependencies among the metrics. For
example, in Figure 3b, there is initially a positive correlation between two metrics, but the
highlighted red area on the left clearly breaks this relationship, leading to anomalies.

disscorr(corr(xi, xj), corr(xi

t:t+k, x

j
t:t+k) > δ

(10)

where k is the time window. If the correlation is disrupted from t to t + k, it indicates that
the correlation coefficient has exceeded the threshold compared to the normal value.

Temporal-local intermetric anomaly: The anomalies violate the dependencies between
metrics and temporal relationships, focusing on how a specific metric breaks its correlation
and deviates from its historical trend within a certain time period, as indicated by the
highlighted red area on the right side of Figure 3b.

2.3. Time/Frequency Domain Analysis

Time series frequency domain analysis involves transforming a time domain signal,
which is a signal that varies over time, into a frequency-domain representation. This
conversion allows for a better understanding of the signal’s frequency components and
periodicity. Frequency domain analysis reveals the different frequency components within

---

<!-- PAGE 6 -->

Sensors 2025, 25, 190

6 of 27

a time series, which helps in identifying cyclic patterns, trends, and anomalies. The most
commonly used formula is the Discrete Fourier Transform (DFT):

Xk =

T−1
∑
t=0

xte−i2πkt/T,

k = 0, . . . , T − 1

(11)

where Xk is the discrete complex amplitude at frequency k, xt is the time series signal, and
i is the imaginary unit.

The Fast Fourier Transform (FFT) typically uses Formula (11) to convert the time
domain into the frequency domain. FFT is an efficient computational algorithm for the DFT,
it can convert the original time series into a spectrum and sort it by coefficients, obtaining
the seasonal cycle by reversing the highest frequency. Most programming languages and
mathematical libraries provide built-in FFT functions that can be directly used to compute
the DFT.

3. Taxonomy of MTSAD Methods

To summarize the existing deep multivariate time series anomaly detection methods,
we proposed a taxonomy for the anomaly detection strategies from the perspectives of
learning paradigms and deep learning models. We present a general pipeline as illus-
trated in Figure 4. We categorize anomaly detection methods into forecasting, reconstruc-
tion and contrastive types. A forecasting-based model uses next timestamp predictions,
whereas a reconstruction-based model uses latent representations of the whole time series.
Contrastive-based methods rely on calculating the similarity or dissimilarity between data
points to conduct analysis and prediction. Table 1 offers a more detailed overview of
these methods.

3.1. Temporal/Spatial

Temporal analysis focuses on how variables change over time, while spatial analysis
examines how these variables vary across different locations or spatial units. Temporal and
spatial perspectives offer a more thorough understanding of the underlying relationships
and patterns in MTS.

Figure 4. The general pipeline for MTSAD using deep learning models. Given a source data, we
first process the source data using a data processing module that performs basic data cleaning and
normalization tasks. Subsequently, we utilize the anomaly detection strategies from the perspectives
of learning paradigms and deep learning models to obtain representations for executing anomaly
detection tasks across different application domains.

---

<!-- PAGE 7 -->

Sensors 2025, 25, 190

7 of 27

Table 1. Multivariate Deep Anomaly Detection Models in Time Series. T/S: Temporal/Spatial|Values:
[S: Spatial, T: Temporal, ST: Spatio-Temporal], T/F: Time/Frequency domain|Values: [T: Time,
F: Frequency], LP: Learn Paradigms|Values: [Su: Supervised, Un: Unsupervised, Semi: Semi-
supervised, Self: Self-supervised], Input: Model Input|Values: [P: Point, W: Window].

Model

DeepAnt [22]
TCN-ms [23]
TimesNet [24]
LSTM-NDT [25]
LGMAD [26]
THOC [27]
AD-LTI [28]
MTAD-GAT [29]
GDN [30]
FuSAGNet [31]
DVGCRN [32]
DyGraphAD [33]
MAD [34]
CLFormer [35]
AnomalyBERT [36]

DAGMM [37]
MSCRED [38]
USAD [39]
NPSR [40]
LSTM-VAE [41]
OmniAnomaly [42]
InterFusion [43]
SLA-VAE [44]
LARA [16]
MAD-GAN [45]
TadGAN [46]
MIM-GAN [47]
DAEMON [48]
DCGAN [17]
DiffusionAE [49]
D3R [18]
TransAnomaly [50]
Anomaly Transformer [51]
TranAD [52]
MEMTO [53]
Dual-TF [54]
CATCH [55]

AnomalyLLM [56]
aLLM4TS [57]
AnomalyLLM [58]
PatchAD [59]
TRL-CPC [60]
RESIST [61]
Dcdetector [13]
SimAD [62]
RESTAD [63]

LP

S/T T/F

Input Code

Language

Un
Semi
Un
Un
Semi
Self
Un
Self
Un
Un
Un
Un
Self
Un
Self

Venue

IEEE’2018
IOP’2019
ICLR’2023
KDD’2018
Elsevier’2019
NeurIPS’2020
TKDE’2020
ICDM’2020
AAAI’2021
KDD’2022
ICML’2022
ACM’2024
IJCNN’2022
EAAI’2023
ICLR’2023

Bonkbone
Forecasting
CNN
CNN
CNN
RNN
RNN
RNN
RNN
GNN
GNN
GNN
GNN
GNN
Transformer
Transformer
Transformer
Reconstruction
AE
AE
AE,GAN

VAE,RNN
VAE,GRU
VAE
VAE
VAE
GAN
GAN,LSTM
GAN,LSTM
GAN,AE
GAN,CNN

ICLR’2018
AAAI’2019
KDD’2020
NeurIPS’2024 AE
IEEE’2018
KDD’2019
KDD’2021
WWW’2022
WWW’2024
ICANN’2019
IEEE’2020
IEEE’2023
WSDM’2023
AAAI’2024
ICDMW’2023 Diffusion,AE
NeurIPS’2024 Diffusion
CCDC’2021
ICLR’2022
VLDB’2022
NeurIPS’2023
WWW’2024
arXiv’2024

Un
Semi
Un
Un
Semi
Semi
Un
Semi
Un
Un
Un
Un
Un
Un
Un
Un
Transformer,VAE Un
Un
Transformer
Un
Transformer
Un
Transformer
Un
Transformer
Transformer
Un
Contrastive
LLMs
LLMs
LLMs
MLP-Mixer
Transformer
Transformer
Transformer
Transformer
Transformer

arXiv’2024
ICML’2024
IJCAI’2024
arXiv’2024
Elsevier’2022
Springer’2022
KDD’2023
arXiv’2024
arXiv’2024

Un
Self
Self
Un
Un
Un
Self
Un
Un

T
T
T
T
T
T
T
ST
S
ST
ST
ST
T
ST
T

T
T
T
T
T
T
T
T
T
ST
T
T
T
T
T
ST
T
T
T
T
T
T

ST
T
T
T
T
T
T
T
T

T
T
F
T
T
T
F
T
T
T
T
T
T
T
T

W
W
W
W
P
W
P
W
W
W
W
W
W
W
W

P
T
W
T
W
T
W
T
P
T
W
T
W
T
W
T
W
T
W
T
W
T
W
T
W
T
W
T
W
T
W
F
W
T
W
T
W
T
T
W
TF W
TF W

T
T
T
T
T
T
T
T
T

W
W
W
W
W
W
W
W
W

✓
–
✓
✓
–
–
–
✓
✓
–
–
–
–
–
✓

✓
✓
✓
✓
✓
✓
✓
✓
✓
✓
✓
✓
✓
✓
✓
✓
✓
✓
✓
✓
✓
✓

✓
✓
–
✓
–
–
✓
✓
✓

Pytorch
–
Pytorch
Tensorflow
–
–
–
Tensorflow
Pytorch
–
–
–
–
–
Pytorch

Pytorch
Tensorflow
Pytorch
Pytorch
Tensorflow
Tensorflow
Tensorflow
Pytorch
Pytorch
Tensorflow
Pytorch
Tensorflow
Pytorch
Pytorch
Pytorch
Pytorch
Pytorch
Pytorch
Pytorch
Pytorch
Pytorch
Pytorch

Pytorch
Pytorch
–
Pytorch
–
–
Pytorch
Pytorch
Pytorch

3.2. Related Learning Paradigms

Unsupervised, semi-supervised and self-supervised methods are common learning
paradigms in MTSAD, and they can be distinguished according to the label information of
the data and the degree of supervision:

---

<!-- PAGE 8 -->

Sensors 2025, 25, 190

8 of 27

Unsupervised Learning: Unsupervised anomaly detection does not rely on any labeled
anomalous data for training. It attempts to discover anomalous patterns by analyzing
the features of the time series, which means it needs to use only normal data during the
training phase.

Semi-unsupervised Learning: In semi-supervised learning, only part of the training
data has label information, while the other part of the sample has no label information,
the model uses the sample with label information to learn during the training process,
and tries to improve the performance through the unlabeled sample. In the multivariate
time series anomaly detection, the semi-supervised learning method can use the labeled
anomaly sample the original and unlabeled normal samples are trained to distinguish
between normal and abnormal time series patterns.

Self-supervised Learning: Self-supervised methods utilize unlabeled data to train
models by creating supervisory signals from the data itself. These methods typically
involve predicting missing parts or properties of the input based on the observed data,
allowing the model to learn useful representations without requiring explicit labels, which
can then be applied to various downstream tasks.

3.3. Model Input

The model input of multivariate time series anomaly detection can be time steps or
windows (sliding windows).Time steps refer to individual points in time where observa-
tions are recorded for each variable in the multivariate time series. Each time step includes
measurements for all variables at that specific moment. Window is subsets of consecutive
time steps with a fixed size. These windows are used to aggregate data over time, capturing
temporal patterns and relationships among variables within each window. In real world,
there are often complex structures such as noise, seasonality, trends, etc., and anomalies
usually do not appear at a single point in time, but persist or present a pattern over a period
of time. Therefore, the most recent MTSAD model takes a window instead of a single point
as the model input.

4. Forecasting Methods

Forecasting-based methods use historical data of time series to train a predictive
model that can forecast future data points. This method assesses the anomaly level by
comparing predicted values with actual values, considering anomalies as a significant
increase in prediction error, as illustrated in Figure 5a. This section will explore predictive
anomaly detection methods, focusing primarily on four types: CNN-based, RNN-based,
GNN-based, and Transformer-based models.

Figure 5. The examples of each type of anomaly criteria: (a) a forecasting loss; (b) a reconstruction
loss; and (c) a contrastive loss.

---

<!-- PAGE 9 -->

Sensors 2025, 25, 190

9 of 27

4.1. CNN-Based Models

DeepAnt [22] proposes an unsupervised anomaly detection method based on CNN,
which does not require labeled training data. This method uses CNN to automatically learn
the representation of time series data and identifies anomalies using reconstruction error.
Compared to traditional CNNs, Temporal Convolutional Networks(TCN) can better handle
the temporal characteristics of time series, TCN-ms [23] uses TCN for anomaly detection,
emphasizing the importance of temporal information. By introducing causal convolution
and dilated convolution in the convolution operation to process time series data, it helps to
capture long distance dependencies. However, the aforementioned methods only consider
the one-dimensional changes of the time series. To enhance the model’s understanding of
the structure of time series, TimesNet [24] extends the analysis of temporal changes to 2D
space by innovatively incorporates Fast Fourier Transform, making it easy to model 2D
changes with 2D kernels, and providing a new perspective for more complex time series
analysis. It not only improves the accuracy of anomaly detection but also enhances the
model’s generalization ability of the model for time series data.

4.2. RNN-Based Models

LSTM-NAT [25] represents an innovative application of RNNs for spacecraft telemetry
analysis, emphasizing the use of LSTM [64] to identify anomalies within complex data.
Unlike traditional methods, LSTM-NAT employs a non-parametric dynamic thresholding
method, utilizing an unsupervised approach to assess residuals and determine whether
prediction errors indicate spacecraft anomalies. However, its reliance on one-dimensional
outputs limits its ability to handle high-dimensional data in multivariate scenarios. Build-
ing upon this foundation, LGMAD [26] integrates LSTM with the Gaussian Mixture Model
(GMM) [65], providing a comprehensive solution for low-dimensional system characteris-
tics. This method not only enhances the efficiency of anomaly detection through the health
factor but also expands its application to the processing of MTS by leveraging the strengths
of both LSTM and GMM in capturing temporal dynamics and analyzing feature correla-
tions. Another notable advancement in capturing temporal dynamics is the THOC [27].
By introducing the Temporal Hierarchical One-Class network, which uses a dilated RNN
with skip connections [66], the limitations of LSTM in capturing multi-scale temporal
dynamics are addressed. The hierarchical clustering process of THOC and the introduction
of a self-supervision task in the temporal domain significantly enhance the model’s ability
to detect anomalies in real-world time series data. However, these schemes may require
adjustments for specific types of multi-seasonal time series data to ensure their accuracy
and efficiency. Wu et al. [28] proposed an unsupervised scheme with multi-seasonality.
AD-LTI introduced a new metric—Local Trend Inconsistency (LTI), which can be computed
efficiently and robustly scores the probability of anomalies for each data point. It overcomes
the challenges of requiring labeled data and the computational intensity of processing large
volumes of data, making it suitable for a variety of event-sensitive scenarios.

4.3. GNN-Based Models

In the field of MTSAD, capturing the complex relationships and dynamic changes
in MTS is crucial. The MTAD-GAT [29] model learns complex dependencies on both the
feature and temporal dimensions via a graph attention network [67] and achieves high
performance in MTSAD through a joint optimization strategy. However, it may encounter
issues with efficiency and scalability when dealing with large-scale datasets. GDN [30]
leverages graph neural networks to learn a dependency graph among sensors and enhances
the interpretability of anomaly detection through attention weights. However, it fails to
fully capture the spatial and temporal correlations between sensors when processing sensor

---

<!-- PAGE 10 -->

Sensors 2025, 25, 190

10 of 27

data. To address these issues, Chen et al. [31] proposed DVGCRN, effectively models
the spatial and temporal correlations of time series by combining an Embedding-Guided
Probabilistic Generative Network(DEPN) with an adaptive variational graph convolutional
recurrent network(GCRN), demonstrating superior performance in anomaly detection.
FuSAGNet [32] integrates feature selection with GNNs to effectively identify and model
the relationships between different time series features. The model constructs an inter-
series adjacency matrix based on the latent feature representations generated by a sparse
auto-encoder, enhancing its ability to detect anomalies. The DyGraphAD [33] framework
strengthens the capture of short-term and long-term dependency relationships in time
series through dynamic graph forecasting, thereby improving detection accuracy.

4.4. Transformer-Based Models

Transformer-based models, with their self-attention mechanisms, have become a
cornerstone in a variety of sequence modeling tasks [12], including time series analysis.
These models are particularly adept at capturing the inherent temporal dynamics and
complex patterns in time series data.

AnomalyBERT [36] utilizes a self-supervised method, which does not require labeled
data, a common scenario in real-world situations. Its innovative data degradation scheme
introduces synthetic outliers, enhancing the model’s ability to detect various types of
anomalies while effectively capturing temporal dependencies and contextual information
using the Transformer architecture. However, the model may face challenges in training
due to the complexity of the Transformer architecture and the need to balance the data
degradation scheme. MAD [34] also adopts a self-supervised learning approach, eliminat-
ing the need for labeled data. However, MAD focuses on masked modeling, simplifying
the training process by learning representations of normality, which reduces the complexity
introduced by the integration of synthetic outliers. MAD improves upon the traditional
Next Step Prediction (NSP) task by using masked inputs, allowing the model to learn from
bidirectional contexts. Nevertheless, compared to NSP models, MAD is slower during the
inference process, especially when masking all steps sequentially. To enhance inference
speed while maintaining accuracy, CLformer [35] proposes a lightweight Transformer,
enhancing local feature extraction through multi-scale causal convolution and reducing
error accumulation. Additionally, the block recurrent prediction strategy decreases time
and space complexity, leading to faster inference.

4.5. Pros and Cons

This section explores the advantages and disadvantages of prediction-based time series
anomaly detection methods. CNNs excel as feature extractors for capturing local features in
time series data; however, their kernel size and operational mechanisms limit their ability
to capture global dependencies, which restricts their performance as a backbone for time
series data. RNN-based models perform well in capturing long-term dependencies, but
face scalability challenges when processing long sequences due to their sequential nature
and memory limitations. GNN-based models provide deep insights into spatio-temporal
dynamics, but their increased computational complexity poses additional challenges when
handling large-scale or high-dimensional data, and they may not be suitable for non-graph
or fuzzy graph structures. In contrast, Transformer-based Models typically outperform
others in anomaly detection tasks, as they are better at handling long-range dependencies
and achieving parallel processing. However, these models may require further adjustments
to ensure that important contextual information is not overlooked.

---

<!-- PAGE 11 -->

Sensors 2025, 25, 190

11 of 27

5. Reconstruction Methods

Reconstruction-based methods use a normal dataset to train a model that attempts
to encode the data into a latent space and then reconstruct the original data from this
representation. Reconstruction loss is calculated by comparing the differences between the
reconstructed data and the original data, as illustrated in Figure 5b. This section delves into
reconstruction anomaly detection methods, focusing on four types: AE-based, VAE-based,
GAN-based, Transformer-based, and Diffusion-based models.

5.1. AE-Based Models

As an innovative application in the field of unsupervised learning, models based on
autoencoders (AE) [68] have made significant progress in the area of AD. DAGMM [37]
is the pioneering model that integrates deep AE with GMM [65] for unsupervised anomaly
detection. Unlike traditional techniques that perform density estimation after dimen-
sionality reduction, DAGMM optimizes both processes simultaneously, ensuring that
key information for anomaly detection is preserved. However, DAGMM relies on deep
autoencoders, which face challenges in escaping local optima and require substantial com-
putational resources. To address this issue, USAD [39] was proposed, utilizing adversarial
training to enhance the stability and speed of autoencoder-based anomaly detection. The
architecture of USAD enables it to train quickly and isolate anomalies effectively, mak-
ing it suitable for large-scale applications. However, USAD may struggle with detecting
subtle anomalies because it focuses on reconstruction error. In response to this challenge,
Zhang et al. [38] introduced MSCRED, which incorporates a multi-scale convolutional
recurrent encoder-decoder framework to capture temporal dependencies and inter-sensor
correlations within multivariate time series data. Its approach using signature matrices
and an attention mechanism allows the model to robustly diagnose anomalies of varying
severity levels. However, the complexity of the model may pose challenges when deal-
ing with extremely high-dimensional data or real-time applications. The next method
NPSR, proposed by Lai et al. [40], also faces the challenge of handling the complexity of
high-dimensional data. NPSR modulates the anomaly detection process by introducing a
Nominality Score, balancing the detection of point and contextual anomalies. The NPSR
framework includes both point-based and sequence-based reconstruction models, and
its performance surpasses existing techniques, offering a theoretically grounded method
for anomaly detection. Further optimization is still needed for its application in high-
dimensional settings to ensure computational efficiency.

5.2. VAE-Based Models

Variational Autoencoders (VAEs) [69] use an encoder to map input data into a space
of latent random variables, and then reconstruct the data from this space with a decoder.
LSTM-VAE [41], the former network is replaced by LSTM in VAE. However, LSTM-VAE
ignores the temporal dependence between stochastic variates. Hence, OmniAnomaly [42]
was proposed, the model is the first MTSAD algorithm capable of handling explicit tem-
poral dependencies among random variables. It provides a novel method for entity-level
anomaly explanation through stochastic recurrent neural networks, the objective is to
learn the normal patterns of data and utilize reconstruction probability for anomaly de-
tection. Additionally, InterFusion [43] is an unsupervised method that models both the
inter-dependency and temporal dependency of MTS simultaneously. Its core idea involves
modeling the normal patterns within data using a hierarchical VAE with two stochas-
tic latent variables, each learning low-dimensional embeddings of either inter-metric or
temporal aspects. Unsupervised VAE is vulnerable to the influence of anomalous inputs.
SLA-VAE [44] addresses the challenge of obtaining labeled data in InterFusion through

---

<!-- PAGE 12 -->

Sensors 2025, 25, 190

12 of 27

semi-supervised learning, utilizing active learning to leverage a small number of highly
uncertain samples for learning and updating online system anomaly detection models.
LARA [16] solves the need for online systems to quickly adapt to new distributions with a
lightweight retraining approach. LARA designs the retraining process as a convex problem
to prevent overfitting and ensure rapid convergence. It also has the capability to utilize
historical data without the need for storage.

5.3. GAN-Based Models

The principle of GAN [70] is based on a framework known as adversarial training,
which consists of two components: a generator designed to mimic the distribution of real
data, and a discriminator tasked with distinguishing between generated and authentic data.
MAD-GAN [45] employs LSTM-RNNs as both the generator and discriminator within
a GAN framework to seize the temporal relationships between time series distributions,
while also taking into account the complete dataset to uncover the underlying interactions
among them. MAD-GAN using standard adversarial loss suffers from gradient explosion
and mode collapse. Hence, TadGAN [46] combines wasserstein loss [71] and cycle consis-
tency loss [72] to form the final minmax objective, the former aims to match the distribution
of generated time series with the data distribution of the target domain, while the latter
prevents conflicting outputs between the two generators. Additionally, MIM-GAN [47]
introduces an exponential information metric into the loss function of GANs to avoid local
optimal solution and model collapse. It considers a discriminative reconstruction score
composed of discriminative and reconstruction loss. MIM-GAN employs LSTM-based gen-
erators and discriminators to capture temporal relationships within the data. Soft-DTW [73]
is used as a differentiable alternative for the reconstruction loss, and the combination of
reconstruction loss and the prior probability distribution of the latent space serves as the
anomaly score. DCGANs [17] can adjust the generator to produce samples closer to real
data by minimizing the Soft-DTW loss. DCGANs utilize CNNs in both the generator and
discriminator networks, while performing parallel computation for the reconstruction of
multiple points, effectively alleviating performance bottlenecks (i.e., Mode Collapse). In
complex systems, the data generated by devices exhibit complex patterns and a scarcity of
labeled data, making anomaly detection a significant challenge. DAEMON [48] employs
two discriminators to adversarially train an autoencoder to learn the normal patterns of
time series, using reconstruction errors to identify anomalies. Its robustness is ensured
through regularization of hidden variables and reconstructed data.

5.4. Transformer-Based Models

Due to the complex temporal characteristics (i.e., temporal dependency, inter-variable
correlations, and noise) in multivariate time series, many different hybrid schemes have
been proposed. TransAnomaly [50] is the first model combining Transformer and VAE for
time series data. TransAnomaly enables more parallelization and reduces learning costs.
TranAD [52] proposes the use of attention-based sequence encoders for rapid inference,
combined with adaptive conditioning and adversarial training to enhance the stability of
the model. However, the problem of over-generalization persists. MEMTO [53] introduces
a novel memory module that can learn how each memory item should be updated in
response to input data, adapting to diverse normal patterns. Due to the rarity of anomalies
in time series data and the difficulty of establishing non-trivial associations from anomalies
to the entire series, Anomaly Transformer [51] calculates association discrepancy through a
new Anomaly-Attention mechanism and enhances the distinguishability between normal
and abnormal points with a minimax strategy, demonstrating the potential of Transformers
in capturing associations of anomaly points in time series.

---

<!-- PAGE 13 -->

Sensors 2025, 25, 190

13 of 27

The aforementioned methods are all in the time domain and do not utilize frequency
domain information. Recent studies have attempted to improve the accuracy of anomaly
detection by combining information from both the time and frequency domains. Dual-
TF [54] proposes a Nested-Sliding Windows (NS-window) technique, where anomaly
scores in the time domain are calculated within the outer window, and anomaly scores
in the frequency domain are calculated within the inner window, achieving alignment of
anomaly scores at the granularity of individual data points. CATCH [55] performs patching
operations in the frequency domain to capture fine-grained frequency characteristics and
uses a Channel Fusion Module (CFM) to perceive correlations between channels. It uses
Frequency-Enhanced Point-Granularity Scoring technology [54] to calculate the anomaly
score for each time point, which involves patch scanning and frequency reconstruction
within the input window.

5.5. Diffusion-Based Models

Diffusion models perturb the observed data by gradually adding Gaussian noise [74]

and then utilize a learnable transformation to recover the original data.

DiffusionAE [49] conditions the diffusion process on autoencoder reconstructions
rather than the original data. DiffusionAE achieves greater robustness to varying training
anomaly ratios and better handling of multiple anomaly types (i.e., point anomaly) in
the dataset. The diffusion process smooths out abnormal fragment, resulting in higher
reconstruction errors, which in turn improves performance. However, the training cost to
adjust the information bottleneck in the reconstruction process is high. D3R [18] introduces
a method called noise diffusion to externally manage the information bottleneck. Diffu-
sion reframes the bottleneck by treating noise as the limiting factor and uncontaminated
information as a condition. As the bottleneck is no longer inherent to the model, it can be
adjusted in size without requiring retraining.

5.6. Pros and Cons

This section describes the advantages and limitations of the aforementioned anomaly
detection models for time series data. AE-based methods automatically extract data features
but cannot capture all the complexities of the data and have difficulty interpreting the
meaning of reconstruction errors. VAE is adept at explicitly modeling probabilities and
provide a theoretical foundation for understanding data distributions. However, the models
rely on the assumption of Gaussian distributions, which may limit the expressive power of
these models. GAN-based models learn complex data distributions through adversarial
training, maintaining an impressive fidelity to the original data distributions. Nevertheless,
they are very challenging to train due to issues like vanishing gradients [75], which can
hinder model stability and convergence. Diffusion models perform well when facing noise
and missing data, as they can infer missing parts during the generation process, allowing
them to better understand the distribution of normal data when detecting anomalies.
However, when handling the boundary between missing and observed parts, the model
may exhibit inconsistencies [49]. Additionally, capturing the dynamic characteristics of
time series may require further adjustments and improvements.

6. Contrastive Methods

Contrastive methods operate within the framework of contrastive learning, which
typically involves a dual-tower model. Time series data is input into two distinct represen-
tation learning networks to generate two representation vectors. During the representation
learning phase, representations of the time series are extracted from different perspectives,
it is necessary to use a contrastive fusion module (such as upsampling) to align the rep-

---

<!-- PAGE 14 -->

Sensors 2025, 25, 190

14 of 27

resentations to each timestep. Subsequently, a contrastive loss is employed to calculate
the similarity between different representations. As illustrated in Figure 5c. The method
is commonly used in unsupervised or self-supervised learning tasks. This section delves
into contrastive anomaly detection methods, focusing on three types: Transformer-based,
MLP-based models, LLMs-bsed.

6.1. LLMs-Based Models

Recently, LLMs have gained popularity in time series Analysis [76,77]. Refs. [56,58]
papers share the same model name, AnomalyLLM, but they adopt different strategies to
address anomaly detection issues in their respective fields. The former AnomalyLLM [56]
involves pre-training a dynamic-aware encoder to generate representations of edges in
dynamic graphs. This includes constructing structural-temporal subgraphs and optimizing
with contrastive loss to capture the structural and temporal information of the edges.
By selecting word embeddings related to dynamic graphs and clustering them into text
prototypes, these text prototypes are then used to reprogram edge embeddings to align the
semantics between dynamic graphs and LLMs. A prompt template is designed to encode
the information of a few labeled samples into the LLM, enabling the model to adapt to
various types of anomalies without updating model parameters. The latter, proposed by
Liu et al. [58], introduces a knowledge distillation-based method where a student network
is trained to mimic the output of a teacher network that is pre-trained on a large-scale
dataset. During the testing phase, anomalies are detected when there is a significant
discrepancy between the outputs of the student and teacher networks. To consolidate
normal feature extraction, prototypical signals are incorporated into the student network,
making it more focused on historical normal patterns. Synthetic anomalies are generated
through data augmentation techniques to expand the representation gap between the two
networks. Additionally, a contrastive loss is used to bring the representations of original
and augmented samples in the teacher network closer together, serving as a regularization
term to encourage the teacher network to capture more general patterns.

aLLM4TS [57] adapts LLMs for time series through a two-stage training strategy. Ini-
tially, it undergoes causal continuous pre-training on various time series datasets, followed
by fine-tuning for multi-patch prediction in specific time series contexts. A distinctive
feature of this framework is the patch-wise decoding layer, which converts individual data
patches (segments) directly into time series, thereby significantly enhancing the model’s
ability to master time series representations based on temporal patches.

6.2. MLP Mixer-Based Models

Recently, analyses of time series prediction have shown that the MLP-Mixer can effec-
tively handle sequential data [78–80]. PatchAD [59] represents a departure from traditional
reconstruction-based approaches. The model consists of four distinct MLP Mixers, specifi-
cally designed to achieve efficiency and light-weight using the MLP architecture. PatchAD
innovatively introduces a dual-projection constraint module to alleviate potential model
degradation. For practitioners and researchers seeking the latest and potentially more
effective methods for MTSAD, this paper may be valuable reading material.

6.3. Transformer-Based Models

Existing reconstruction-methods frequently fail to handle sufficient temporal context
and inadequate representation of normal patterns, hindering their effectiveness in identify-
ing abnormal behaviors. The TRL-CPC [60] explores the integration of contrastive learning
into time series analysis. In TRL-CPC, the context vectors represent observation windows
in MTS. The latent representations of subsequent time steps are obtained through nonlinear
transformations of these context vectors are contrasted with the latent representations of

---

<!-- PAGE 15 -->

Sensors 2025, 25, 190

15 of 27

the encoder for multivariate time series to maximize positive density. RESIST [61] relies
on a robust loss function based on contrastive learning to train a Transformer that models
the expected behavior of network activity, without the need for an anomaly-free training
subset. It automatically mitigates the impact of atypical corrupted training data to reduce
their influence on training optimization. DCdetector [13] employs a contrastive learning
framework to learn representations of time series data. By utilizing a dual-attention mecha-
nism, it obtains representations of the input time series from two branches (the in-patch
branch and the patch-wise branch). The contrastive loss function is defined by measuring
the similarity of representations from these two different perspectives, thus acquiring
permutation-invariant representations with superior discriminative capabilities.

Recent research has begun to combine reconstruction and contrastive learning to create
a comprehensive integrated anomaly score that can capture deviations from expected
patterns and effectively identify subtle anomalies. SimAD [62] combines a sophisticated
feature extractor adept at handling extended time windows, integrates normal behavior
patterns comprehensively using the EmbedPatch encoder, and introduces an innovative
ContrastFusion module aimed at highlighting distribution differences between normal
and abnormal data to enhance the robustness of AD. RESTAD [63] implements a Radial
Basis Function (RBF) neuron layer in the Transformer model to represent a non-parametric
density in the latent space. A high output from the RBF indicates similarity with normal
training data. Additionally, RESTAD merges RBF similarity scores with reconstruction
errors to enhance anomaly detection sensitivity.

6.4. Pros and Cons

This section describes the advantages and limitations of the aforementioned anomaly
detection models for time series data. MLP Mixer-based methods feature a simple structure
that is easy to implement and can be adapted to various data complexities by adjusting
the number of layers and neurons [78]. Although MLP can capture nonlinear relationships,
they may not effectively handle extremely complex data distributions. LLMs-based models
have learned a wealth of semantic knowledge through pre-training on large text datasets,
possessing strong representational capabilities. They are adaptable to a variety of down-
stream tasks and can also perform well in few-shot learning scenarios, but directly applying
LLMs for TSAD is not effective. It requires the design of prompting strategies and proper
fine-tuning to enhance their ability to detect and interpret anomalies [76]. Moreover, LLMs
may struggle with more complex, context-related anomalies and may hallucinate when
indexing and explaining anomaly points.

7. Datasets

This section compiles and summarizes a variety of datasets and evaluation benchmarks
for MTSAD, aiming to provide comprehensive research resources for researchers in this
field. These datasets include both general and specialized time series datasets that can be
used for the evaluation of anomaly detection tasks, with the latter being applicable under
certain assumptions or specific customizations. Each dataset or benchmark is described
in detail through multiple dimensions and their inherent characteristics. In Table 2, we
have collected and analyzed datasets that are well known or frequently cited in the field of
MTSAD, which have been tested by a series of deep learning models.

Applications typically produce data via a sequence of data generation processes that
mirror system operations or offer insights into the behavior of various entities. Anomalies
frequently emerge as a consequence of irregularities in these data generation processes,
highlighting unusual aspects of the systems and entities involved. Identifying such atypical

---

<!-- PAGE 16 -->

Sensors 2025, 25, 190

16 of 27

Datasets/Benchmark

MSL [25]
NASA Shuttle Valve Data [81]
IOnsphere [82]
SWAN-SF [83]
SMAP [25]
OPPORTUNITY [82]
GECCO [84]
CICIDS [85]
Kitsune [82]
Http (KDDCUP99) [86]
Smtp (KDDCUP99) [86]
NAB-realAdExchange [87]
Creditcard [88]
Genesis [89]
GHL [90]
SWaT [91,92]
WADI [93]
trimSyn [38]
MSDS [94]
Arrhythmia [95]
MBA [96]
Thyroid [97]
SVDB [98]
Daphnet [82,99]
Callt2 [82,100]
Metro [82]
NYC [101]
Occupancy [82]
Exathlon [102]
MBD [103]
MMS [103]
PSM [104]
SMD [105]

traits can yield valuable insights across diverse applications. The deep learning models
outlined below are categorized based on their respective application domains.

Table 2. Public dataset/benchmark used mostly for MTSAD. R/S: The source of the data, whether
it is real world data or synthetic data. Samples: Individual data points or observations within a
dataset. Entities: Independent observation unit or object, such as sensors, machines, devices, etc.
Dims: The number of features or variables in the data. Rate: The proportion of anomalous samples
within the dataset.

R/S

Samples

Entities Dims Rate Domain

Real
Real
Real
Real
Real
Real
Real
Real
Real
Real
Real
Real
Real
Real
Synth
Real
Real
Synth
Real
Real
Real
Real
Real
Real
Real
Real
Real
Real
Real
Real
Real
Real
Real

132,046
49,097
351
355,330
562,800
36,224
138,521
170,231
3,018,973
567,479
95,156
9616
284,807
16,220
200,001
946,719
957,372
17,680
292,860
452
200,000
3772
230,400
32,594
10,080
48,204
17,520
6208
47,530
8640
4370
132,480
1,416,825

27
1

5
55
24
1

9

3
1
1
48
1
1
1
1
1
8

78
35
2
1

2
39
5
50
1
28

55
9
33
51
25
133
9
72
115
3
3
2
29
18
22
51
123
35
10
274
2
6
2
3
2
5
3
8
45
26
7
25
38

10.48 Aerospace
Aerospace
7.0
Astronomy
36.0
Astronomy
23.8
Environmental science
12.83
Environmental science
3.4
Internet of things (IoT)
1.25
Internet of things (IoT)
1.28
Cybersecurity
17.0
Cybersecurity
0.4
Cybersecurity
0.03
Business and finance
Business and finance
Industrial control systems
Industrial control systems
Industrial control systems
Industrial control systems
Industrial control systems
Industrial control systems
Healthcare
Healthcare
Healthcare
Healthcare
Healthcare
Infrastructure
Infrastructure
Infrastructure
Infrastructure
Server monitoring
Server monitoring
Server monitoring
Server monitoring
Server monitoring

0.17
0.3
0.4
11.98
5.99
2.34
5.37
15.0
0.14
2.5
13.6
13.2
4.1
0.1
0.57
28.7
18.3

27.76
4.16

7.1. Astronomy

In the field of astronomy, datasets typically include various observational and sim-
ulation data, mainly used to study phenomena such as the universe, galaxies, stars, and
planets [106,107]. The Ionosphere dataset [82] comes from the UCI Machine Learning
Repository and is used for a binary classification task, with the goal of determining whether
there are electrons present in the ionosphere based on received signals. The dataset includes
individual feature information as well as ionosphere thresholds. It contains 351 samples and
33 features, where each sample represents a measurement of a radar echo signal. Various
classification algorithms can be used for model training and validation when working with
the Ionosphere dataset. The dataset has a high feature dimension, which may lead to the
“curse of dimensionality” during model training. Additionally, handling noise and outliers
in the dataset is another important challenge. The AERO [14] model can distinguish normal
temporal patterns from potential anomalies in astronomical observations, effectively differ-
entiate concurrent noise, and reduce the number of false alarms. SWAN-SF (Space Weather

---

<!-- PAGE 17 -->

Sensors 2025, 25, 190

17 of 27

Analytics for Solar Flares) [83] is a multivariate time series benchmark dataset designed
for the field of solar physics. The dataset contains 4075 solar active regions, spanning the
9-year operational period of the Solar Dynamics Observatory (SDO). Accurate prediction of
solar flares is crucial for astronauts, space equipment, and satellite communication systems.

7.2. Aerospace

In the aerospace field, MTSAD datasets are typically used to monitor the performance
parameters and telemetry data of aircraft, satellites, spacecraft, and other related equipment.
Aerospace datasets are crucial for predicting equipment failures and ensuring mission
success. By conducting in-depth analysis of this time series data, anomaly detection
algorithms can be developed and tested to enhance the reliability and performance of
aerospace systems [108,109]. For instance, the NASA Shuttle Valve Data [81] includes
telemetry data from shuttle valves, which is used to analyze the health condition of the
valves and predict potential malfunctions. The MSL (Mars Science Laboratory) dataset [25],
collected by NASA, contains time-series data from 27 channels, each with 55 dimensions.
The data is anonymized, standardized to a range of 0–1, and recorded every minute. Except
for the telemetry values, which are continuous, most variables are binary (indicating
whether commands were sent). An LSTM-based model can be used for anomaly detection
in this dataset. Hundman et al. [25] proposed the LSTM-NDT, an unsupervised method
for univariate time series anomaly detection, which serves as a non-parametric anomaly
threshold method for NASA datasets.

7.3. Environmental Science

Datasets in the field of environmental science are primarily used for monitoring and
managing natural resources, environmental quality, and the health of ecosystems [110,111].
For instance, the SMAP [25] provides measurements of soil moisture and temperature,
which are crucial for understanding the water cycle, crop health, and climate change.
By conducting in-depth analysis of this time series data, we can better understand the
dynamics of environmental systems and provide data support for sustainable development.
The OPPORTUNITY dataset [82] contains data from 23 body-worn sensors, 12 object-
placement sensors, and 21 environmental sensors, used to measure the daily activities of
four subjects. The OPPORTUNITY dataset is widely used in research in the fields of deep
learning and artificial intelligence, particularly in activity recognition, and has become an
important benchmark dataset. It is often utilized with CNNs and LSTMs combined with
spatio-temporal feature extraction to capture complex activity patterns.

7.4. Internet of Things (IoT)

In the field of IoT, time series anomaly detection datasets are primarily used for
monitoring and analyzing data streams generated by a vast array of interconnected devices
and sensors. This allows for the timely detection of equipment failures, network anomalies,
or unexpected behaviors [112]. The GECCO IoT [84] dataset, for instance, contains sensor
data from smart home or industrial IoT devices, which is utilized for detecting device
anomalies and system malfunctions. The CICIDS dataset [85] contains samples of various
network attacks and normal traffic. It includes data from normal activities and simulated
malicious attacks collected over five days. The data was generated using the CICFlowMeter
tool and provides rich labeled data. Deep learning based models on the CICIDS dataset
have significantly improved the accuracy of intrusion detection. Researchers have explored
deep learning methods, such as multilayer perceptrons and convolutional neural networks,
to enhance detection accuracy and efficiency.

In the IoT, millions of connected devices and smart sensors generate highly dynamic,
large-scale, heterogeneous, and timestamped data. This timestamped data is at the core of

---

<!-- PAGE 18 -->

Sensors 2025, 25, 190

18 of 27

IoT automation and has the potential to significantly impact industrial processes. Effec-
tively detecting anomalies in time-series data and providing real-time actionable insights to
drive improvements in industrial processes presents significant challenges. Liu et al. [113]
proposed the AMCNN-LSTM model, which emphasizes communication efficiency and
federated learning (FL) methods on devices, enabling distributed edge devices to collabora-
tively train an anomaly detection model. To achieve real-time anomaly detection, Nizam
et al. [114] proposed a hybrid end-to-end deep anomaly detection framework that leverages
CNN and LSTM networks to develop an advanced anomaly detection system. The system
architecture consists of three layers: sensors and machines in the industrial setting, an edge
layer for real-time data processing, and a cloud layer for offloading processing tasks. The
framework is designed to accurately detect anomalies and extremely rare events in IoT
streaming data.

7.5. Business and Finance

In the business and finance sector, time series datasets are crucial for identifying and
preventing fraud, market anomalies, credit risks, and other financial issues [3]. The NAB-
realAdExchange dataset [87] is part of the Numenta Anomaly Benchmark (NAB). This
dataset records online advertisement click-through rates, with the metric being cost per
click (CPC). It contains one file with no anomalies and another file with anomalies, designed
to evaluate the performance of anomaly detection algorithms on real-time streaming data.
The Credit Card dataset [88] contains records of credit card transactions, primarily used for
identifying and detecting anomalous transactions, that is, potential fraudulent activities.

When dealing with financial time series involving various market risk factors, a major
issue is the presence of anomalies. These anomalies can lead to calibration errors in mod-
els used for quantifying and managing risk, resulting in potential misestimations of risk.
Crépey et al. [115] proposed an anomaly detection method for financial time series that
combines Principal Component Analysis (PCA) and neural networks. By reducing dimen-
sionality with PCA, this approach effectively extracts key features from high-dimensional
financial time series data, simplifying the subsequent anomaly detection process. Neural
networks are then applied to identify nonlinear relationships and complex patterns. To
detect anomalies in more practical business scenarios in the real world, contextual infor-
mation is needed for accurate prediction. Time-CAD [116] is a context-aware deep time
series decomposition framework that uses deep learning techniques to decompose time
series data and incorporates contextual information to improve the accuracy of anomaly
detection. This method is capable of effectively detecting anomalies in business processes.

7.6. Cybersecurity

In the field of cybersecurity, time series anomaly detection datasets are primarily used
for monitoring and analyzing network traffic, user behavior, and system logs to promptly
identify security threats, intrusion attempts, and abnormal activities. The KDDCUP99 [86]
is a classic cybersecurity dataset widely used for research in network anomaly detection. It
contains various types of cyber attacks, such as DoS (Denial of Service), Probe, R2L (Remote
to Local), U2R (User to Root), as well as traffic data from normal behavior. The Kitsune
dataset [82] is a dataset used for network intrusion detection, containing both normal
and anomalous network traffic data. This dataset is used to train and test deep learning
models to differentiate between normal and malicious traffic. KitNET [117] is a deep
learning model that uses a set of autoencoders for online network intrusion detection. This
unsupervised method can learn to distinguish the characteristics of normal and anomalous
network traffic without the need for expert-labeled traffic data.

---

<!-- PAGE 19 -->

Sensors 2025, 25, 190

19 of 27

7.7. Industrial Control Systems

In the field of Industrial Control Systems (ICS), time series datasets are commonly used
for monitoring and analyzing the operational status of industrial equipment. This facilitates
the timely detection of equipment failures, prediction of maintenance needs, optimization
of production processes, and ensuring production safety. The WADI (Water Distribution)
dataset [93], collected and open-sourced by the iTrust institute of the Singapore University
of Technology and Design (SUTD), is used to simulate water treatment and distribution
networks.This dataset includes sensor data and network data, covering multiple stages
of the water treatment process, such as raw water intake, chemical treatment, filtration,
dechlorination, and reverse osmosis. The SWaT (Secure Water Treatment) [91] is also
provided by the iTrust institute of SUTD and serves as a test platform for research in the
field of ISC for water treatment processes. The SWaT dataset contains sensor data from
various stages of the water treatment process.

Industrial Control Systems (ICS) are widely used and are crucial to both industry and
society. Failures in these systems can have severe impacts on the economy and human life.
As a result, these systems have become attractive targets for both physical and cyberattacks.
Kravchik et al. [118] proposed an efficient method for detecting network attacks in ICS,
which combines lightweight neural networks with Principal Component Analysis (PCA).
This approach aims to reduce computational resource consumption while maintaining
high detection accuracy, which is particularly important in resource-constrained ICS en-
vironments. Anomaly detection is critical for preventing cybersecurity intrusions and
system attacks. Many AI-based anomaly detection methods have been proposed with
high detection performance, but they remain a “black box” that is difficult to interpret.
Hoang et al. [119] used explainable artificial intelligence (XAI) to enhance the perspective
and reliability of an LSTM-based Autoencoder-OCSVM learning model for anomaly de-
tection in ICS. This model is capable of providing detailed information about detected
anomalies, helping security teams make informed decisions.

7.8. Healthcare

In the healthcare domain, time series anomaly detection datasets are primarily uti-
lized for monitoring and analyzing an individual’s physiological parameters. This allows
for the timely detection of health issues, abnormalities in diseases, or malfunctions in
medical equipment. For instance, the MIT-BIH Arrhythmia Database (ECG) [95] contains
a vast collection of electrocardiogram (ECG) records that are used for the detection and
analysis of cardiac arrhythmias. The SVDB [98] offers a range of standard and variant
electrocardiogram recordings, which are employed in research on cardiac health and the
detection of arrhythmias. These datasets are instrumental in advancing our understanding
of heart conditions and in developing more effective diagnostic and monitoring tools for
healthcare professionals.

Electrocardiogram (ECG) signals are commonly used to assess heart health. The
heart, being a complex organ, can exhibit many different types of arrhythmias. Therefore,
applying anomaly detection methods to analyze ECG signals can be highly beneficial.
ANNet [120] utilizes LSTM networks and MLP to process ECG signals, and improves
the accuracy of anomaly detection by combining feature vectors. The study also includes
preprocessing steps for ECG signals, such as denoising with Discrete Wavelet Transform
(DWT) and using a 60Hz notch filter to remove power line interference (PLI). Similarly,
Alamr et al. [121] proposed an unsupervised transformer-based anomaly detection method.
The model architecture consists of two parts: a transformer model for feature extraction
and a classifier for anomaly scoring, which is used to evaluate and detect anomalies in
ECG signals.

---

<!-- PAGE 20 -->

Sensors 2025, 25, 190

20 of 27

7.9. Server Monitoring

Time series anomaly detection datasets within the domain of server monitoring are
primarily used to monitor the performance metrics of server systems to promptly identify
performance bottlenecks, system failures, or security issues. For instance, SMD dataset [105]
gathers a variety of server performance indicators, such as CPU usage, memory consump-
tion, disk I/O, etc., for anomaly detection and performance analysis. Exathlon dataset [102]
may collect performance data of servers under high load conditions to detect perfor-
mance anomalies.

Large companies need to monitor various metrics (such as page views and revenue) of
their applications and services in real time. At Microsoft, a time-series anomaly detection
service has been developed to help customers continuously monitor time-series data and
promptly alert potential incidents. Den et al. [122] proposed a novel algorithm based on
Spectral Residual and CNN, which is the first attempt to apply the SR model, originally
from the visual saliency detection domain, to time-series anomaly detection. The approach
aims to provide an accurate, efficient, and general solution. Netzer et al. [123] proposed a
segment-based time series anomaly detection method for monitoring machining processes.
This approach detects anomalies by using subprocess-specific thresholds, enabling more
precise identification and localization of abnormal behaviors in the machining process.

7.10. Infrastructure

Security is the foundation of sustainable urban development. The process of urban con-
struction and operation involves a large amount of multidimensional time-series data. By
detecting anomalies in MTS, decision support for urban construction and operational risk
warning can be provided. Given the complexity of urban infrastructure, there is an urgent
need for fast and accurate anomaly detection. Wu et al. [124] proposed a real-time anomaly
detection algorithm based on an improved distance measure, called RADIM. RADIM
preserves the relationships between dimensions in the multidimensional subsequences
and uses an extended Frobenius norm with local weights and Euclidean distance based on
multidimensional data to measure the similarity of MTS. In addition, a threshold update
mechanism based on the first-order mean difference (TMFD) is designed to detect real-time
anomalies by assessing deviations. This method has been applied in tunnel construction.
At the same time, most current models still face challenges in perceiving high-frequency
data, and the most challenging task is processing large volumes of data in an extremely
short time. Liu et al. [125] proposed an anomaly detection method for high-frequency
sensor data in traffic infrastructure monitoring systems based on a fine-tuned model. The
researchers demonstrated that converting data into images can improve anomaly detection
speed, but training deep learning models is still time-consuming. Therefore, they designed
a four-stage model and compared the proposed CNN with four widely used fine-tuned
CNNs using confusion matrices to rapidly detect anomalies in high-frequency data.

8. Conclusions and Future Direction

This article provides a comprehensive survey and review of multivariate time series
anomaly detection, exploring types of anomalies and deep architectures for anomaly detec-
tion. It analyzes and organizes deep learning model architectures for anomaly detection
from three perspectives, proposes a new classification of anomaly detection strategies, and
discusses 46 deep learning models in depth. In addition, it compiles public datasets for
multivariate time series anomaly detection, along with their respective application domains.
To advance the field, the article concludes with a discussion of potential directions for future
research exploration.

---

<!-- PAGE 21 -->

Sensors 2025, 25, 190

21 of 27

Discrepancy: The contrastive learning has attracted considerable attention across
various domains, as it is capable of training models by contrasting positive pairs with
negative pairs. Recent research has been focusing on highlighting discrepancies [59,62],
and further exploration in this direction is expected.

Integration of domain knowledge: Integrating existing knowledge from the statistical
domain with deep learning can further enhance the model’s capability for time series
anomaly detection. FCVAE [126] selects the most useful information from the frequency
domain to achieve better short-term trend construction. Future work could leverage
insights from the frequency domain, combined with domain knowledge, to strengthen the
analysis of time series data.

Benchmarking and evaluation metrics: The development and use of diverse pub-
lic datasets that simulate real-world anomaly situations, with clear subset divisions
for training and testing. At the same time, the design of intuitive, interpretable, and
parameter-adjustment-free evaluation metrics to adapt to different types of time series
anomaly detection.

Leveraging techniques from LLMs: Recently, LLMs have gained popularity in time
series analysis [127]. LLMs exhibit exceptional generalization capabilities, demonstrating
robust predictive performance even with scarce datasets. This characteristic is particularly
valuable in the context of MTSAD. By leveraging multimodal knowledge, such as incorpo-
rating additional textual information to generate multimodal embeddings, LLMs effectively
bridge the gap between normal and anomalous data in anomaly detection. This modeling
approach enriches the anomaly detection process by providing a more comprehensive
data representation, enabling the inclusion of diverse data sources and fostering more
detailed and context-aware anomaly detection. Exploring LLMs in MTSAD is a promising
avenue that could significantly enhance the accuracy and efficiency of detecting anomalies
in multivariate time series data.

Author Contributions: Writing—–original draft preparation, F.W.; writing–—review and editing,
F.W., Y.J., R.Z., A.W. and J.X.; supervision, X.P.; Project Administration, A.W.; Funding Acquisition,
J.X. All authors have read and agreed to the published version of the manuscript.

Funding: This research was funded by the 2021 Key Research Platforms and Projects of Colleges and
Universities by the Department of Education of Guangdong Province: Research on the Construction
of Knowledge Graph Models for Vocational College Architectural Education Supported by Artificial
Intelligence (Project No.: 2021ZDZX1112).

Institutional Review Board Statement: Not applicable.

Informed Consent Statement: Not applicable.

Data Availability Statement: The data presented in this study are available on the source mentioned
in the text.

Conflicts of Interest: The authors declare no conflicts of interest.

References

1.

2.

3.

4.

Belay, M.A.; Blakseth, S.S.; Rasheed, A.; Salvo Rossi, P. Unsupervised Anomaly Detection for IoT–Based Multivariate Time Series:
Existing Solutions, Performance Analysis and Future Directions. Sensors 2023, 23, 2844. [CrossRef]
Correia, L.; Goos, J.C.; Klein, P.; Bäck, T.; Kononova, A.V. Online model–based anomaly detection in multivariate time series:
Taxonomy, survey, research challenges and future directions. Eng. Appl. Artif. Intell. 2024, 138, 109323. [CrossRef]
Hilal, W.; Gadsden, S.A.; Yawney, J. Financial fraud: A review of anomaly detection techniques and recent advances. Expert Syst.
Appl. 2022, 193, 116429. [CrossRef]
Cook, A.A.; Misirli, G.; Fan, Z. Anomaly Detection for IoT Time–Series Data: A Survey. IEEE Internet Things J. 2020, 7, 6481–6494.
[CrossRef]

---

<!-- PAGE 22 -->

Sensors 2025, 25, 190

22 of 27

5.

6.

7.

Angiulli, F.; Pizzuti, C. Fast outlier detection in high dimensional spaces. In Proceedings of the 6th European Conference on
Principles of Data Mining and Knowledge Discovery, Berlin/Heidelberg, Germany, 19–23 August 2002; pp. 15–27.
Schölkopf, B.; Platt, J.C.; Shawe–Taylor, J. Estimating the support of a high–dimensional distribution. Neural Comput. 2001, 13,
1443–1471. [CrossRef] [PubMed]
Breunig, M.M.; Kriegel, H.P.; Ng, R.T.; Sander, J. LOF: Identifying density–based local outliers. In Proceedings of the 2000 ACM
SIGMOD International Conference on Management of Data, Dallas, TX, USA, 15–18 May 2000; pp. 93–104.

8. Nelson, B.K. Time series analysis using autoregressive integrated moving average (ARIMA) models. Acad. Emerg. Med. 1998, 5,

739–744. [CrossRef] [PubMed]

9. Ma, J.; Perkins, S. Time–series novelty detection using one–class support vector machines. In Proceedings of the International

Joint Conference on Neural Networks, Portland, OR, USA, 20–24 July 2003; Volume 3, pp. 1741–1745.

10. Tax, D.M.J.; Duin, R.P.W. Support vector data description. Mach. Learn. 2004, 54, 45–66. [CrossRef]
11. Munir, M.; Chattha, M.A.; Dengel, A.; Ahmed, S. A comparative analysis of traditional and deep learning–based anomaly
detection methods for streaming data. In Proceedings of the 18th IEEE International Conference on Machine Learning and
Applications (ICMLA), Boca Raton, FL, USA, 16–19 December 2019; pp. 561–566.

12. Vaswani, A. Attention is all you need. In Proceedings of the 31st International Conference on Neural Information Processing

Systems, Long Beach, CA, USA, 4–9 December 2017.

13. Yang, Y.; Zhang, C.; Zhou, T.; Wen, Q.; Sun, L. Dcdetector: Dual attention contrastive representation learning for time series
anomaly detection. In Proceedings of the 29th ACM SIGKDD Conference on Knowledge Discovery and Data Mining, Long Beach,
CA, USA, 6–10 August 2023; pp. 3033–3045.

14. Hao, X.; Chen, Y.; Yang, C.; Du, Z.; Ma, C.; Wu, C.; Meng, X. From Chaos to Clarity: Time Series Anomaly Detection in

Astronomical Observations. arXiv 2024, arXiv:2403.10220.

15. Huang, X.; Chen, N.; Deng, Z.; Huang, S. Multivariate time series anomaly detection via dynamic graph attention network and

Informer. Appl. Intell. 2024, 54, 7636–7658. [CrossRef]

16. Chen, F.; Qin, Z.; Zhou, M.; Zhang, Y.; Deng, S.; Fan, L.; Wen, Q. LARA: A Light and Anti–overfitting Retraining Approach for
Unsupervised Time Series Anomaly Detection. In Proceedings of the ACM on Web Conference 2024, Singapore, 13–17 May 2024;
pp. 4138–4149.

17. Prabhu, H.; Valadi, J.; Arjunan, P. Generative Adversarial Network with Soft–Dynamic Time Warping and Parallel Reconstruction

for Energy Time Series Anomaly Detection. arXiv 2024, arXiv:2402.14384.

18. Wang, C.; Zhuang, Z.; Qi, Q.; Wang, J.; Wang, X.; Sun, H.; Liao, J. Drift doesn’t matter: Dynamic decomposition with diffusion
reconstruction for unstable multivariate time series anomaly detection. In Proceedings of the 37th International Conference on
Neural Information Processing Systems, New Orleans, LA, USA, 10–16 December 2023; pp. 10758–10774.

19. Pang, G.; Shen, C.; Cao, L.; Hengel, A.V.D. Deep learning for anomaly detection: A review. ACM Comput. Surv. 2021, 54, 1–38.

[CrossRef]

20. Ma, S.; Guan, S.; He, Z.; Nie, J.; Gao, M. TPAD: Temporal pattern based neural network model for anomaly detection in

multivariate time series. IEEE Sens. J. 2023, 23, 30668–30682. [CrossRef]

21. Zamanzadeh Darban, Z.; Webb, G.I.; Pan, S.; Aggarwal, C.; Salehi, M. Deep learning for time series anomaly detection: A survey.

ACM Comput. Surv. 2024, 57, 1–42. [CrossRef]

22. Munir, M.; Siddiqui, S.A.; Dengel, A.; Ahmed, S. DeepAnT: A deep learning approach for unsupervised anomaly detection in

time series. IEEE Access 2018, 7, 1991–2005. [CrossRef]

23. He, Y.; Zhao, J. Temporal convolutional networks for anomaly detection in time series. J. Phys. Conf. Ser. 2019, 1213, 042050.

[CrossRef]

24. Wu, H.; Hu, T.; Liu, Y.; Zhou, H.; Wang, J.; Long, M. Timesnet: Temporal 2d–variation modeling for general time series analysis.

In Proceedings of the Eleventh International Conference on Learning Representations, Kigali, Rwanda, 1–5 May 2023.

25. Hundman, K.; Constantinou, V.; Laporte, C.; Colwell, I.; Soderstrom, T. Detecting spacecraft anomalies using lstms and
nonparametric dynamic thresholding. In Proceedings of the 24th ACM SIGKDD International Conference on Knowledge
Discovery and Data Mining, KDD ’18, London, UK, 19–23 August 2018; pp. 387–395.

26. Ding, N.; Ma, H.; Gao, H.; Ma, Y.; Tan, G. Real–time anomaly detection based on long short–Term memory and Gaussian Mixture

27.

Model. Comput. Electr. Eng. 2019, 79, 106458. [CrossRef]
Shen, L.; Li, Z.; Kwok, J. Timeseries anomaly detection using temporal hierarchical one–class network. In Proceedings of the 34th
International Conference on Neural Information Processing Systems, Vancouver, BC, Canada, 6–12 December 2020; Volume 33,
pp. 13016–13026.

28. Wu, W.; He, L.; Lin, W.; Su, Y.; Cui, Y.; Maple, C.; Jarvis, S. Developing an unsupervised real–time anomaly detection scheme for

time series with multi–seasonality. IEEE Trans. Knowl. Data Eng. 2020, 34, 4147–4160. [CrossRef]

---

<!-- PAGE 23 -->

Sensors 2025, 25, 190

23 of 27

29. Zhao, H.; Wang, Y.; Duan, J.; Huang, C.; Cao, D.; Tong, Y.; Xu, B.; Bai, J.; Tong, J.; Zhang, Q. Multivariate time–series anomaly
detection via graph attention network. In Proceedings of the IEEE International Conference on Data Mining, ICDM, Sorrento,
Italy, 17–20 November 2020; pp. 841–850.

30. Deng, A.; Hooi, B. Graph Neural Network–Based Anomaly Detection in Multivariate Time Series. Proc. AAAI Conf. Artif. Intell.

2021, 35, 4027–4035. [CrossRef]

31. Chen, W.; Tian, L.; Chen, B.; Dai, L.; Duan, Z.; Zhou, M. Deep variational graph convolutional recurrent network for multivariate
time series anomaly detection. In Proceedings of the 39th International Conference on Machine Learning, Baltimore, MD, USA,
17–23 July 2022; pp. 3621–3633.

32. Han, S.; Woo, S.S. Learning sparse latent graph representations for anomaly detection in multivariate time series. In Proceedings
of the 28th ACM SIGKDD Conference on Knowledge Discovery and Data Mining, Washington, DC, USA, 14–18 August 2022;
pp. 2977–2986.

33. Chen, K.; Feng, M.; Wirjanto, T.S. Multivariate time series anomaly detection via dynamic graph forecasting. arXiv 2023,

34.

arXiv:2302.02051.
Fu, Y.; Xue, F. Mad: Self–supervised masked anomaly detection task for multivariate time series.
International Joint Conference on Neural Networks, IJCNN, Padua, Italy, 18–23 July 2022; pp. 1–8.

In Proceedings of the

35. Wu, Y.; Dong, Y.; Zhu, W.; Zhang, J.; Liu, S.; Lu, D.; Li, Y. CLformer: Constraint–based Locality enhanced Transformer for anomaly

36.

detection of ancient building structures. Eng. Appl. Artif. Intell. 2023, 126, 107072. [CrossRef]
Jeong, Y.; Yang, E.; Ryu, J.H.; Park, I.; Kang, M. Anomalybert: Self–supervised transformer for time series anomaly detection
using data degradation scheme. arXiv 2023, arXiv:2305.04468.

37. Zong, B.; Song, Q.; Renqiang Min, M.; Cheng, W.; Lumezanu, C.; Cho, D.; Chen, H. Deep autoencoding gaussian mixture model
for unsupervised anomaly detection. In Proceedings of the International Conference on Learning Representations, Vancouver,
BC, Canada, 30 April–3 May 2018.

38. Zhang, C.; Song, D.; Chen, Y.; Feng, X.; Lumezanu, C.; Cheng, W.; Chawla, N.V. A deep neural network for unsupervised anomaly
detection and diagnosis in multivariate time series data. In Proceedings of the AAAI Conference on Artificial Intelligence,
Honolulu, HI, USA, 27 January–1 February 2019; Volume 33, pp. 1409–1416.

39. Audibert, J.; Michiardi, P.; Guyard, F.; Marti, S.; Zuluaga, M.A. Usad: Unsupervised anomaly detection on multivariate time
series. In Proceedings of the 26th ACM SIGKDD International Conference on Knowledge Discovery and Data Mining, Virtual
Event, CA, USA, 23–27 August 2020; pp. 3395–3404.

40. Lai, C.Y.A.; Sun, F.K.; Gao, Z.; Lang, J.H.; Boning, D. Nominality score conditioned time series anomaly detection by
point/sequential reconstruction. In Proceedings of the 37th Conference on Neural Information Processing Systems, New Orleans,
LA, USA, 10–16 December 2023; pp. 76637–76655.

41. Park, D.; Hoshi, Y.; Kemp, C.C. A multimodal anomaly detector for robot–assisted feeding using an lstm–based variational

42.

autoencoder. IEEE Robot. Autom. Lett. 2018, 3, 1544–1551. [CrossRef]
Su, Y.; Zhao, Y.; Niu, C.; Liu, R.; Sun, W.; Pei, D. Robust anomaly detection for multivariate time series through stochastic
recurrent neural network. In Proceedings of the 25th ACM SIGKDD International Conference on Knowledge Discovery and Data
Mining, Anchorage, AK, USA, 4–8 August 2019; pp. 2828–2837.

43. Li, Z.; Zhao, Y.; Han, J.; Su, Y.; Jiao, R.; Wen, X.; Pei, D. Multivariate time series anomaly detection and interpretation using
hierarchical inter–metric and temporal embedding. In Proceedings of the ACM SIGKDD International Conference on Knowledge
Discovery and Data Mining, Virtual Event, Singapore, 14–18 August 2021; pp. 3220–3230.

44. Huang, T.; Chen, P.; Li, R. A semi–supervised vae based active anomaly detection framework in multivariate time series for online
systems. In Proceedings of the ACM Web Conference, WWW’22, Virtual Event, Lyon, France, 25–29 April 2022; pp. 1797–1806.
45. Li, D.; Chen, D.; Jin, B.; Shi, L.; Goh, J.; Ng, S.K. MAD–GAN: Multivariate anomaly detection for time series data with generative

adversarial networks. Int. Conf. Artif. Neural Netw. 2019, 11730, 703–716.

46. Geiger, A.; Liu, D.; Alnegheimish, S.; Cuesta–Infante, A.; Veeramachaneni, K. Tadgan: Time series anomaly detection using
generative adversarial networks. In Proceedings of the IEEE International Conference on Data Mining, Atlanta, GA, USA,
10–13 December 2020; pp. 33–43.

47. Lu, S.; Dong, Z.; Cai, D.; Fang, F.; Zhao, D. MIM–GAN–based Anomaly Detection for Multivariate Time Series Data. In
Proceedings of the IEEE Vehicular Technology Conference (VTC2023–Fall), Hong Kong, China, 10–13 October 2023; pp. 1–7.
48. Chen, X.; Deng, L.; Zhao, Y.; Zheng, K. Adversarial autoencoder for unsupervised time series anomaly detection and interpretation.
In Proceedings of the 16th ACM International Conference on Web Search and Data Mining, Singapore, 27 February–3 March 2023;
pp. 267–275.

49. Pintilie, I.; Manolache, A.; Brad, F. Time series anomaly detection using diffusion–based models. In Proceedings of the IEEE

International Conference on Data Mining, Shanghai, China, 1–4 December 2023; pp. 570–578.

---

<!-- PAGE 24 -->

Sensors 2025, 25, 190

24 of 27

50. Zhang, H.; Xia, Y.; Yan, T.; Liu, G. Unsupervised anomaly detection in multivariate time series through transformer–based
variational autoencoder. In Proceedings of the 33rd Chinese Control and Decision Conference (CCDC), Kunming, China,
22–24 May 2021; pp. 281–286.

51. Xu, J. Anomaly transformer: Time series anomaly detection with association discrepancy. In Proceedings of the International

Conference on Learning Representations, Virtual Event, 25–29 April 2022.

52. Tuli, S.; Casale, G.; Jennings, N.R. Tranad: Deep transformer networks for anomaly detection in multivariate time series data.

53.

Proc. VLDB Endow. 2022, 15, 1201–1214. [CrossRef]
Song, J.; Kim, K.; Oh, J.; Cho, S. Memto: Memory–guided transformer for multivariate time series anomaly detection.
In Proceedings of the 37th International Conference on Neural Information Processing Systems, New Orleans, LA, USA,
10–16 December 2023; Volume 36, pp. 57947–57963.

54. Nam, Y.; Yoon, S.; Shin, Y.; Bae, M.; Song, H.; Lee, J.G.; Lee, B.S. Breaking the Time–Frequency Granularity Discrepancy in
Time–Series Anomaly Detection. In Proceedings of the ACM on Web Conference 2024, WWW ’24, Singapore, 13–17 May 2024;
pp. 4204–4215.

55. Wu, X.; Qiu, X.; Li, Z.; Wang, Y.; Hu, J.; Guo, C.; Yang, B. CATCH: Channel–Aware Multivariate Time Series Anomaly Detection

via Frequency Patching. arXiv 2024, arXiv:2410.12261.

56. Liu, S.; Yao, D.; Fang, L.; Li, Z.; Li, W.; Feng, K.; Bi, J. AnomalyLLM: Few–Shot Anomaly Edge Detection for Dynamic Graphs

using Large Language Models. arXiv 2024, arXiv:2405.07626.

57. Bian, Y.; Ju, X.; Li, J.; Xu, Z.; Cheng, D.; Xu, Q. Multi–patch prediction: Adapting llms for time series representation learning.
In Proceedings of the 41st International Conference on Machine Learning, Vienna, Austria, 21–27 July 2024; Volume 235,
pp. 3889–3912.

58. Liu, C.; He, S.; Zhou, Q.; Li, S.; Meng, W. Large language model guided knowledge distillation for time series anomaly detection.
In Proceedings of the Thirty–Third International Joint Conference on Artificial Intelligence (IJCAI–24), Jeju, Republic of Korea,
3–9 August 2024; pp. 2162–2170.

59. Zhong, Z.; Yu, Z.; Yang, Y.; Wang, W.; Yang, K. PatchAD: Patch–Based MLP–Mixer for Time Series Anomaly Detection. arXiv

2024, arXiv:2401.09793.

60. Pranavan, T.; Sim, T.; Ambikapathi, A.; Ramasamy, S. Contrastive predictive coding for anomaly detection in multi–variate time

series data. arXiv 2022, arXiv:2202.03639.

61. Najari, N.; Berlemont, S.; Lefebvre, G.; Duffner, S.; Garcia, C. RESIST: Robust transformer for unsupervised time series anomaly
detection. In Proceedings of the Advanced Analytics and Learning on Temporal Data: 7th ECML PKDD Workshop, Grenoble,
France, 19–23 September 2022; pp. 66–82.

62. Zhong, Z.; Yu, Z.; Xi, X.; Xu, Y.; Chen, J.; Yang, K. SimAD: A Simple Dissimilarity–Based Approach for Time Series Anomaly

Detection. arXiv 2024, arXiv:2405.11238.

63. Ghorbani, R.; Reinders, M.J.; Tax, D.M. RESTAD: REconstruction and Similarity based Transformer for time series Anomaly

Detection. arXiv 2024, arXiv:2405.07509.

64. Hochreiter, S.; Schmidhuber, J. Long Short–Term Memory. Neural Comput. 1997, 9, 1735–1780. [CrossRef] [PubMed]
65. Reynolds, D.A. Gaussian mixture models. Encycl. Biom. 2009, 741, 659–663.
66. Orhan, A.E.; Pitkow, X. Skip connections eliminate singularities. arXiv 2017, arXiv:1701.09175.
67. Velickovic, P.; Cucurull, G.; Casanova, A.; Romero, A.; Lio, P.; Bengio, Y. Graph attention networks. arXiv 2017, arXiv:1710.10903.
68. Bank, D.; Koenigstein, N.; Giryes, R. Autoencoders. In Machine Learning for Data Science Handbook: Data Mining and Knowledge

Discovery Handbook; Springer: Cham, Switzerland, 2023; pp. 353–374.

69. Doersch, C. Tutorial on variational autoencoders. arXiv 2016, arXiv:1606.05908.
70. Goodfellow, I.; Pouget–Abadie, J.; Mirza, M.; Xu, B.; Warde–Farley, D.; Ozair, S.; Bengio, Y. Generative adversarial networks.

71.

Commun. ACM 2020, 63, 139–144. [CrossRef]
Frogner, C.; Zhang, C.; Mobahi, H.; Araya, M.; Poggio, T.A. Learning with a Wasserstein loss. In Proceedings of the 28th
International Conference on Neural Information Processing Systems, Montreal, QC, Canada, 7–12 December 2015; Volume 2,
pp. 2053–2061.

72. Dwibedi, D.; Aytar, Y.; Tompson, J.; Sermanet, P.; Zisserman, A. Temporal cycle–consistency learning. In Proceedings of the
IEEE/CVF Conference on Conference on Computer Vision and Pattern Recognition(CVPR), Long Beach, CA, USA, 15–20 June
2019; pp. 1801–1810.

73. Cuturi, M.; Blondel, M. Soft–dtw: A differentiable loss function for time–series. In Proceedings of the 34th International

Conference on Machine Learning, Sydney, Australia, 6–11 August 2017; pp. 894–903.

74. MacKay, D.J. Introduction to Gaussian processes. NATO ASI Ser. F Comput. Syst. Sci. 1998, 168, 133–166.

---

<!-- PAGE 25 -->

Sensors 2025, 25, 190

25 of 27

75. Yoon, J.; Zame, W.R.; van der Schaar, M. Estimating missing data in temporal data streams using multi–directional recurrent

neural networks. IEEE Trans. Biomed. Eng. 2018, 66, 1477–1490. [CrossRef]

76. Dong, M.; Huang, H.; Cao, L. Can LLMs Serve As Time Series Anomaly Detectors? arXiv 2024, arXiv:2408.03475.
77. Alnegheimish, S.; Nguyen, L.; Berti–Equille, L.; Veeramachaneni, K. Large language models can be zero–shot anomaly detectors

for time series? arXiv 2024, arXiv:2405.14755.

78. Zhong, S.; Song, S.; Zhuo, W.; Li, G.; Liu, Y.; Chan, S.H.G. A multi–scale decomposition mlp–mixer for time series analysis. arXiv

2023, arXiv:2310.11959. [CrossRef]

79. Gong, Z.; Tang, Y.; Liang, J. Patchmixer: A patch–mixing architecture for long–term time series forecasting. arXiv 2023,

arXiv:2310.00655.

80. Ekambaram, V.; Jati, A.; Nguyen, N.; Sinthong, P.; Kalagnanam, J. Tsmixer: Lightweight mlp–mixer model for multivariate time
series forecasting. In Proceedings of the 29th ACM SIGKDD Conference on Knowledge Discovery and Data Mining, Long Beach,
CA, USA, 6–10 August 2023; pp. 459–469.
Ferrell, B.; Santuro, S. NASA Shuttle Valve Data; Florida Tech: Melbourne, FL, USA, 2005.

81.
82. Asuncion, A.; Newman, D. UCI Machine Learning Repository. 2007. Available online: https://ergodicity.net/2013/07/ (accessed

on 8 November 2024).

83. Angryk, R.A.; Martens, P.C.; Aydin, B.; Kempton, D.; Mahajan, S.S.; Basodi, S.; Georgoulis, M.K. Multivariate time series dataset

for space weather data analytics. Sci. Data 2020, 7, 227. [CrossRef]

84. Moritz, S.; Rehbach, F.; Chandrasekaran, S.; Rebolledo, M.; Bartz–Beielstein, T. GECCO Industrial Challenge 2018 Dataset: A water
quality dataset for the ‘Internet of Things: Online Anomaly Detection for Drinking Water Quality’Competition. In Proceedings of
the Genetic and Evolutionary Computation Conference, Kyoto, Japan, 15–19 July 2018.

85. Poorebrahimi, A. CICIDS 2017. J. Adv. Signal Process. 2021, 5, 105–115.
86. KDD Cup. The Third International Knowledge Discovery and Data Mining Tools Competition Dataset KDD Cup 1999 Data. 1999.

Available online: https://kdd.ics.uci.edu/databases/kddcup99/kddcup99.html (accessed on 24 December 2024).

87. Ahmad, S.; Lavin, A.; Purdy, S.; Agha, Z. Unsupervised real–time anomaly detection for streaming data. Neurocomputing 2017,

262, 134–147. [CrossRef]

88. Dal Pozzolo, A.; Caelen, O.; Johnson, R.A.; Bontempi, G. Calibrating probability with undersampling for unbalanced classification.
In Proceedings of the IEEE Symposium Series on Computational Intelligence, Cape Town, South Africa, 7–10 December 2015;
pp. 159–166.
von Birgelen, A.; Niggemann, O. Anomaly detection and localization for cyber–physical production systems with self–organizing
maps. Improve 2018, 8, 55–71.
Filonov, P.; Lavrentyev, A.; Vorontsov, A. Multivariate industrial time series with cyber–attack simulation: Fault detection using
an lstm–based predictive data model. arXiv 2016, arXiv:1612.06676.

90.

89.

91. Aditya, P.M.; Nils, O.T. SWaT: A water treatment testbed for research and training on ICS security. In Proceedings of the 2016
International Workshop on Cyber–Physical Systems for Smart Water Networks (CySWater), Vienna, Austria, 11 April 2016;
pp. 31–36.

92. Goh, J.; Adepu, S.; Junejo, K.N.; Mathur, A. A dataset to support research in the design of secure water treatment systems. Crit.

Inf. Infrastruct. Secur. 2017, 10242, 88–99.

93. Ahmed, C.M.; Palleti, V.R.; Mathur, A.P. WADI: A water distribution testbed for research in the design of secure cyber physical
systems. In Proceedings of the 3rd International Workshop on Cyber–Physical Systems for Smart Water Networks, Pittsburgh,
PA, USA, 21 April 2017; pp. 25–28.

94. Nedelkoski, S.; Bogatinovski, J.; Mandapati, A.K.; Becker, S.; Cardoso, J.; Kao, O. Multi–source distributed system data for
ai–powered analytics. In Proceedings of the Service–Oriented and Cloud Computing: 8th IFIP WG 2.14 European Conference,
ESOCC 2020, Heraklion, Greece, 28–30 September 2020; pp. 161–176.

95. Moody, G.B.; Mark, R.G. The impact of the MIT–BIH arrhythmia database. IEEE Eng. Med. Biol. Mag. 2001, 20, 45–50. [CrossRef]
96. Goldberger, A.L.; Amaral, L.A.N.; Glass, L.; Hausdorff, J.M.; Ivanov, P.C.; Mark, R.G.; PhysioBank, P. PhysioNet: Components of

a New Research Resource for Complex Physiologic Signals. Circulation 2000, 101, 215–220. [CrossRef]

97. Vanderpump, M.P. The epidemiology of thyroid disease. Br. Med. Bull. 2011, 99, 39–51. [CrossRef]
98. Greenwald, S.D.; Patil, R.S.; Mark, R.G. Improved detection and classification of arrhythmias in noise–corrupted electrocardiograms
using contextual information. In Proceedings of the Computers in Cardiology, Chicago, IL, USA, 23–26 September 1990; pp. 461–464.
99. Bachlin, M.; Plotnik, M.; Roggen, D.; Maidan, I.; Hausdorff, J.M.; Giladi, N.; Troster, G. Wearable assistant for Parkinson’s disease

patients with the freezing of gait symptom. IEEE Trans. Inf. Technol. Biomed. 2009, 14, 436–446. [CrossRef]

100. Ihler, A.; Hutchins, J.; Smyth, P. Adaptive event detection with time–varying poisson processes. In Proceedings of the 12th ACM
SIGKDD International Conference on Knowledge Discovery and Data Mining, Philadelphia, PA, USA, 20–23 August 2006; pp. 207–216.

---

<!-- PAGE 26 -->

Sensors 2025, 25, 190

26 of 27

101. Daus, M.W. Taxis. In The Routledge Handbook of Public Transport; Routledge: London, UK, 2021; pp. 252–269.
102. Jacob, V.; Song, F.; Stiegler, A.; Rad, B.; Diao, Y.; Tatbul, N. Exathlon: A benchmark for explainable anomaly detection over time

series. arXiv 2020, arXiv:2010.05073. [CrossRef]

103. He, Z.; Chen, P.; Li, X.; Wang, Y.; Yu, G.; Chen, C.; Zheng, Z. A spatiotemporal deep learning approach for unsupervised anomaly

detection in cloud systems. IEEE Trans. Neural Netw. Learn. Syst. 2020, 34, 1705–1719. [CrossRef]

104. Abdulaal, A.; Liu, Z.; Lancewicki, T. Practical approach to asynchronous multivariate time series anomaly detection and
localization. In Proceedings of the 27th ACM SIGKDD Conference on Knowledge Discovery and Data Mining, Virtual Event,
Singapore, 14–18 August 2021; pp. 2485–2494.

105. Li, Z.; Chen, W.; Pei, D. Robust and unsupervised KPI anomaly detection based on conditional variational autoencoder. In
Proceedings of the 2018 IEEE 37th International Performance Computing and Communications Conference (IPCCC), Orlando,
FL, USA, 17–19 November 2018; pp. 1–9.

106. Muthukrishna, D.; Gupta, R. A Classifier–Based Approach to Multi–Class Anomaly Detection Applied to Astronomical Time–

Series. arXiv 2024, arXiv:2408.08888.

107. Scargle, J.D. Studies in astronomical time series analysis. Astrophys. J. 1982, 263, 835–853. [CrossRef]
108. Baireddy, S.; Desai, S.R.; Mathieson, J.L.; Foster, R.H.; Chan, M.W.; Comer, M.L.; Delp, E.J. Spacecraft time–series anomaly
detection using transfer learning. In Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition
(CVPR), Nashville, TN, USA, 20–25 June 2021; pp. 1951–1960.

109. El–Shafeiy, E.; Alsabaan, M.; Ibrahem, M.I.; Elwahsh, H. Real–time anomaly detection for water quality sensor monitoring based

on multivariate deep learning technique. Sensors 2023, 23, 8613. [CrossRef] [PubMed]

110. Chevrot, A.; Vernotte, A.; Legeard, B. CAE: Contextual auto–encoder for multivariate time–series anomaly detection in air

transportation. Comput. Secur. 2022, 116, 102652. [CrossRef]

111. Rollo, F.; Bachechi, C.; Po, L. Anomaly detection and repairing for improving air quality monitoring. Sensors 2023, 23, 640.

[CrossRef]

112. Sgueglia, A.; Di Sorbo, A.; Visaggio, C.A.; Canfora, G. A systematic literature review of IoT time series anomaly detection

solutions. Future Gener. Comput. Syst. 2022, 134, 170–186. [CrossRef]

113. Liu, Y.; Garg, S.; Nie, J.; Zhang, Y.; Xiong, Z.; Kang, J.; Hossain, M.S. Deep anomaly detection for time–series data in industrial IoT:
A communication–efficient on–device federated learning approach. IEEE Internet Things J. 2020, 8, 6348–6358. [CrossRef]
114. Nizam, H.; Zafar, S.; Lv, Z.; Wang, F.; Hu, X. Real–time deep anomaly detection framework for multivariate time–series data in

industrial iot. IEEE Sens. J. 2022, 22, 22836–22849. [CrossRef]

115. Crépey, S.; Lehdili, N.; Madhar, N.; Thomas, M. Anomaly detection in financial time series by principal component analysis and

neural networks. Algorithms 2022, 15, 385. [CrossRef]

116. Nam, Y.; Trirat, P.; Kim, T.; Lee, Y.; Lee, J.G. Context–aware deep time–series decomposition for anomaly detection in businesses.
In Proceedings of the Joint European Conference on Machine Learning and Knowledge Discovery in Databases, Turin, Italy,
18–22 September 2023; pp. 330–345.

117. Zelichenok, I.; Kotenko, I. Kitsune Dataset Analysis via BigData and Deep Learning Techniques. In Proceedings of the 2024 IEEE
Ural–Siberian Conference on Biomedical Engineering, Radioelectronics and Information Technology (USBEREIT), Yekaterinburg,
Russia, 13–15 May 2024; pp. 152–155.

118. Kravchik, M.; Shabtai, A. Efficient cyber attack detection in industrial control systems using lightweight neural networks and pca.

IEEE Trans. Dependable Secur. Comput. 2021, 19, 2179–2197. [CrossRef]

119. Hoang, N.X.; Hoang, N.V.; Du, N.H.; Huong, T.T.; Tran, K.P. Explainable anomaly detection for industrial control system

cybersecurity. IFAC–PapersOnLine 2022, 55, 1183–1188.

120. Sivapalan, G.; Nundy, K.K.; Dev, S.; Cardiff, B.; John, D. ANNet: A lightweight neural network for ECG anomaly detection in IoT

edge sensors. IEEE Trans. Biomed. Circuits Syst. 2022, 16, 24–35. [CrossRef]

121. Alamr, A.; Artoli, A. Unsupervised transformer–based anomaly detection in ECG signals. Algorithms 2023, 16, 152. [CrossRef]
122. Ren, H.; Xu, B.; Wang, Y.; Yi, C.; Huang, C.; Kou, X.; Zhang, Q. Time–series anomaly detection service at microsoft.

In
Proceedings of the 25th ACM SIGKDD International Conference on Knowledge Discovery and Data Mining, Anchorage, AK,
USA, 4–8 August 2019; pp. 3009–3017.

123. Netzer, M.; Palenga, Y.; Fleischer, J. Machine tool process monitoring by segmented timeseries anomaly detection using

subprocess–specific thresholds. Prod. Eng. 2022, 16, 597–606. [CrossRef]

124. Wu, B.; Zhang, F.; Wang, Y.; Hu, M.; Bai, X. Anomaly Detection Algorithm for Urban Infrastructure Construction Equipment

Based on Multidimensional Time Series. Sustainability 2024, 16, 3335. [CrossRef]

125. Liu, H.; Li, L. Anomaly detection of high–frequency sensing data in transportation infrastructure monitoring system based on

fine–tuned model. IEEE Sens. J. 2023, 23, 8630–8638. [CrossRef]

---

<!-- PAGE 27 -->

Sensors 2025, 25, 190

27 of 27

126. Wang, Z.; Pei, C.; Ma, M.; Wang, X.; Li, Z.; Pei, D.; Xie, G. Revisiting VAE for Unsupervised Time Series Anomaly Detection: A
Frequency Perspective. In Proceedings of the ACM on Web Conference 2024, Singapore, 13–17 May 2024; pp. 3096–3105.
127. Gao, S.; Koker, T.; Queen, O.; Hartvigsen, T.; Tsiligkaridis, T.; Zitnik, M. Units: Building a unified time series model. arXiv 2024,

arXiv:2403.00131.

Disclaimer/Publisher’s Note: The statements, opinions and data contained in all publications are solely those of the individual
author(s) and contributor(s) and not of MDPI and/or the editor(s). MDPI and/or the editor(s) disclaim responsibility for any injury to
people or property resulting from any ideas, methods, instructions or products referred to in the content.

<!-- MARKITDOWN CONVERSION -->

<!-- Full MarkItDown conversion for formatting fidelity. -->

Review
A Survey of Deep Anomaly Detection in Multivariate Time
Series: Taxonomy, Applications, and Directions
FenglingWang1,YiyueJiang1,RongjieZhang2,AiminWei3,JingmingXie4,*andXiongwenPang2,*
1 SchoolofArtificialIntelligence,SouthChinaNormalUniversity,Foshan528000,China;
wfl314159@163.com(F.W.);jiangyy@m.scnu.edu.cn(Y.J.)
2 SchoolofComputerScience,SouthChinaNormalUniversity,Guangzhou510555,China;zrj22127@gmail.com
3 SchoolofArchitecturalEngineering,GuangzhouPanyuPolytechnicCollege,Guangzhou511483,China;
weiam@gzpyp.edu.cn
4 DoctoralWorkstation,GuangdongSongshanPolytechnic,Shaoguan512126,China
* Correspondence:xiejm@gdsspt.edu.cn(J.X.);augepang@scnu.edu.cn(X.P.)
Abstract: Multivariate time series anomaly detection (MTSAD) can effectively identify
andanalyzeanomalousbehaviorincomplexsystems,whichisparticularlyimportantin
fieldssuchasfinancialmonitoring,industrialequipmentfaultdetection,andcybersecu-
rity. MTSADrequiressimultaneouslyanalyzetemporaldependenciesandinter-variable
relationshipshavepromptedresearcherstodevelopspecializeddeeplearningmodelsto
detectanomalouspatterns. Inthispaper,weconductedastructuredandcomprehensive
overviewofthelatesttechniquesindeeplearningformultivariatetimeseriesanomaly
detectionmethods. Firstly,weproposedataxonomyfortheanomalydetectionstrategies
fromtheperspectivesoflearningparadigmsanddeeplearningmodels,andthenprovidea
systematicreviewthatemphasizestheiradvantagesanddrawbacks. Wealsoorganizedthe
publicdatasetsfortimeseriesanomalydetectionalongwiththeirrespectiveapplication
domains. Finally,openissuesforfutureresearchonMTSADwereidentified.
Keywords: anomalydetection;deeplearningnetwork;multivariatetimeseries
AcademicEditors:JongmyonKim
1. Introduction
andGeorgeD.Magoulas
Time series anomaly detection is crucial in data analysis, focusing on identifying
Received:19November2024
unusualpatternsintimeseriesdatathatsignificantlydifferfromexpectedbehavior[1,2].
Revised:25December2024
Accepted:30December2024 ThistaskbecomesmoreintricateinMTSAD,whichitinvolvesmultiplechannelsorvariates
Published:1January2025 of data. The evolution of sensing technologies and enhancements in data storage have
Citation: Wang,F.;Jiang,Y.;Zhang, propelledtheadoptionofanomalydetectionacrossaspectrumofsectors. Forexample,In
R.;Wei,A.;Xie,J.;Pang,X.ASurvey thefinancialservicessector,itisusedinfinancialservicestoidentifyfraudulenttransactions
ofDeepAnomalyDetectionin andmarketfluctuations,protectingcustomerfunds[3]. Intheindustrialsector,itmonitors
MultivariateTimeSeries:Taxonomy,
equipmentstatustodetectfaultsearly,reducingdowntimeandmaintenancecosts[4].
Applications,andDirections.Sensors
Multivariatetimeseriesanomalydetectionhasbeenstudiedinavarietyofapplication
2025,25,190. https://doi.org/
domainsandhasexperiencedsignificantprogress. Thereexistvariousmethodsproposed
10.3390/s25010190
forMTSAD,includingstatisticalmethods,classicalmethods,distance-basedmethods[5],
Copyright:©2025bytheauthors.
distributional-basedmethods[6],anddensity-basedmethods[7],arestillaviablechoice
LicenseeMDPI,Basel,Switzerland.
ofalgorithm. Statisticaltechniquestypicallyinvolvemovingaverages(MA)andtheau-
Thisarticleisanopenaccessarticle
distributedunderthetermsand toregressiveintegratedmovingaverage(ARIMA)[8]. MAreducetheimpactofrandom
conditionsoftheCreativeCommons fluctuationsbycalculatingtheaveragevaluewithinaspecifictimewindow,therebyreveal-
Attribution(CCBY)license ingtrendsandpatternsinthedata. TheARIMAmodelisapopulartimeseriesforecasting
(https://creativecommons.org/
methodthatcombinesthreecomponents: AutoRegressive(AR),Integrated(I),andMA,
licenses/by/4.0/).
Sensors2025,25,190 https://doi.org/10.3390/s25010190

Sensors2025,25,190 2of27
whichareusedtomodelandpredicttimeseriesdata. Classicalmachinelearningmethods
includeOne-ClassSupportVectorMachine(OCSVM)[9]andSupportVectorDataDescrip-
tion(SVDD)[10]. SVDDissimilartoOCSVM,butinsteadoffindingjustaboundary,itcre-
atesahyperspherethatcontainsthenormaldata. Anydatapointsoutsidethishypersphere
areconsideredanomalies. Distance-basedtechniquesassessthedeviationofobservations
fromrepresentativedatapointsusingdistancemetrics,whiledistributionalmethodsfocus
onidentifyinganomaliesthroughpointswithlowlikelihood. Density-basedmethodsare
basedonthelocaldensityofdatapoints. Ifadatapointhassignificantlylowerlocaldensity
comparedtoitsneighboringarea,itmaybeflaggedasananomaly. However,astarget
systemsgrowinsizeandcomplexity, thesemethodsencounterchallenges, particularly
theirlimitationsinhandlingmultidimensionaldataandthelackoflabeledanomalies[11].
The challenge of MTSAD lies in the need to consider both the dynamic changes along
thetemporaldimensionandtheinterrelationshipsbetweenobservationssimultaneously.
Recently,deeplearning-basedtechniqueshaveadvancedthefieldofanomalydetection
withinmulti-dimensionaldatasets. Thesemethodsexploitpowerfuldeeplearningmodels
likeTransformers[12–14],GNN[15],VAEs[16],GANs[17],Diffusion[18]etc.,areadeptat
representingintricate,non-linearrelationshipsamongvarioussensorsandareproficientin
capturingtemporalcorrelationsandependencieseffectively[19]. Theseadvancedmodels
leverage the capabilities of deep learning to identify and learn subtle patterns in data,
enablingaccurateidentificationandearlywarningofanomalousbehaviorsacrossvarious
fieldssuchasfinancialtransactionmonitoring,cybersecuritythreatdetection,industrial
equipment maintenance forecasting, and healthcare monitoring. The progress of these
technologiesallowsustobetterunderstandandanalyzethecomplexdynamicswithin
multi-dimensionaldatasets,providingpowerfultoolsforreal-timeanomalydetectionand
decisionsupportsystems.
Inthispaper,weaimtoaddressthecurrentknowledgegapbyexploringfeaturesof
timeseries,typesofanomalies,andofferingathoroughoverviewofrecentadvancements
indeeplearningtechniquesforMTSAD.Itreviewsthelatestdeeplearningmethodsfor
this purpose from three perspectives and offers a comprehensive discussion about the
classification of deep learning models. Additionally, it compiles and organizes public
datasetsfortimeseriesanomalydetection,alongwiththeirrespectiveapplicationdomains.
Finally,thepaperwrapsupbyhighlightingpossibledirectionsforfutureresearchtofurther
developthefield.
Insummary,thecontributionsofthispaperinclude:
(1) The investigation and review of anomaly categories in multivariate time series
haveproposedanewclassification;
(2)Focusingonlearningparadigmsandneuralnetworkarchitectures,weconducted
a comprehensive review of the latest deep learning methods from three strategies and
proposedanewtaxonomyforMTSAD;
(3)AnexplorationoffutureresearchopportunitiesforMTSAD.
2. BackgroundandPreliminary
2.1. ProblemDefinition
MTSADreferstotheprocessofidentifyinganomalousbehaviororpatternsthatdevi-
atesignificantlyfromhistoricalpatternswithinthecontextofmultiplerelatedtimeseries.
Comparedtounivariatetimeseriesanomalydetection,multivariateanomalydetectionis
morecomplexasitrequiresconsiderationoftherelationshipsandtemporaldependencies
betweenmultiplevariablessimultaneously[20]. Anomalyscoreisanindicatorusedto
measurethedegreeofanomalyofatimepointortimewindows. Thehighertheanomaly
score,themorelikelythedatapointistobeanomalous.

Sensors2025,25,190
3of27
WeconsideracollectionofMTSdenotedasX. Hence,thedefinitioncanbeexpressed
asfollows:
|         |                                                | X = (x1,x2,...,xC) |             |                 | (1) |
| ------- | ---------------------------------------------- | ------------------ | ----------- | --------------- | --- |
|         |                                                | xc = (x            | ,x ,...,x ) |                 | (2) |
|         |                                                |                    | 1 2 T       |                 |     |
| wherexc | ∈ RT                                           |                    |             | ∈               |     |
|         | representsanT-dimensionalvector,eachdatapointx |                    |             | t Risacquiredat |     |
acertaintimestamptfromasensor. TrepresentsthelengthoflookbackwindowsandC
| representsthenumberofdimensionsorvariables(C |     |     | >1). |     |     |
| -------------------------------------------- | --- | --- | ---- | --- | --- |
GivenamultidimensionaltimeseriesdatasetX ∈ RTXC,thegoalistofindamethod
tocomputeanomalyscores:
|     |     | = (s | )               |     |     |
| --- | --- | ---- | --------------- | --- | --- |
|     |     | S    | 1 ,s 2 ,...,s T |     | (3) |
wheres t ∈ Rdenotestheanomalyscoreattimepointt.Thisallowsustoidentifyanomalous
datapointsthatdeviatefromnormalbehavior.
2.2. AnomalyTypesinMTS
MTSconsistsofasetofunivariatetimeseries(metric),eachofwhichdescribesdifferent
partsorattributesofacomplexentity. Therefore,itnotonlyhastemporaldependencies
within the metrics, manifested as periodic, trend, and other inherent patterns of each
metric, butalsointer-metricsdependencieswithintheentity, representingthelinearor
nonlinearrelationshipsbetweenallmetricsoftheentityateachtimepoint[2,21]. Thus,
anomaliesinMTScanbedividedintointra-metricanomalies(temporalanomalies)and
inter-metricanomalies. Theoverallclassificationframeworkforanomalytypesisshownin
Figure1. Temporalanomaliesoccurinmultivariate,affectingmultipleoralldimensions.
Temporalanomaliesprimarilyfocusonindividualdatapointsandsubsequences. Point-
wiseanomaliesrefertounexpectedeventsatasingletimepoint, wheretheanomalous
behaviorofatimepointcanbeaspikeorglitch. Pattern-wiseanomaliesareanomalous
subsequences, usually discordant or disharmonious. Here are the definitions of types
ofanomalies:
Figure1.Theoverallclassificationframeworkdiagramformultivariatetimeseriesanomalytypes.
2.2.1. Point-WiseAnomalies
Globalpointanomaly: Globalpointanomalyisananomalyinwhichasingledata
point is significantly different from other data. They are typically spikes in the entire
| sequence. | Consideringathresholdδ,itcanbedescribedas: |          |         |     |     |
| --------- | ------------------------------------------ | -------- | ------- | --- | --- |
|           |                                            | |x t −xˆ | t | > δ |     | (4) |

Sensors2025,25,190 4of27
wherex isexpectedvalueandxˆ istheoutputofthemodel,δ = λ∗G(x ),Grepresents
t t t
thevarianceofthecontextoverx ,andλisthethresholdadjustmentcoefficient.
t
LocalpointAnomaly: Localpointanomalyreferstoabnormalsituationsthatoccur
withinspecificenvironmentsorcontexts. Detectinglocalpointanomalytypicallyinvolves
analyzingboththepointanditsassociatedcontextualinformationtoidentifybehavior
thatdeviatesfromtheexpectednormswithinagivencontext. Thistypeofanomalycanbe
definedas:
δ ≈ λ∗L(x t−k : x t+k ) (5)
where x t−k : x t+k = (x t−k ,x t−k+1 ,...,x t+k ) referstothecontextofthedatapoint x t with
a window size k, L represents the variance of this local context. An example of point
anomaliesareshownonFigure2a,globalpointanomaliestypicallystandoutagainstthe
backdropoftheentiretimeseries,whilelocalpointanomaliescontrastmorewiththedata
pointsimmediatelyadjacenttothem.
Figure2.(a)Point-wiseanomalies,thereddotsindicateanomalies,and(b)Patten-wiseanomalies,
theredareasrepresentanomalies.
2.2.2. Pattern-WiseAnomalies
Shapeletanomaly: Shapeletanomaliesarecircumstancethatoccursinaparticular
environmentorcontext. Unlikeindividualdatapointanomalies,shapeletanomaliyindi-
catesthatthecollectivebehaviorofagroupofrelateddatasignificantlydeviatesfromthe
expectedornormalpattern,asshowninFigure2b.
diss (p,pˆ) > δ (6)
p
where pˆspecifiestheexpectedshapeofthesubsequence. dissisafunctionthatmeasures
thedifferencebetweentwosubsequences.
Trend anomaly: Trend anomalies focus on sudden changes or deviations from the
long-termtrendinthedata. Theseanomaliesmayresultfromsuddenevents,systemic
changes, or other factors leading to abrupt shifts or abnormal growth or decline in the
trenddirection.
diss (τ,τˆ) > δ (7)
τ
whereτˆ isthetrendofnormalsubsequences.
Cycle Anomaly: Cycle anomalies occur when there are abnormal changes in the
periodicpatternsoftimeseriesdata. Forexample,thereisanomalyinthefrequencyor
intensityofaseasonalevent.
diss (s,sˆ) > δ (8)
s

Sensors2025,25,190 5of27
wheresˆisthecyclicityofexpectedsubsequences.
2.2.3. Inter-MetricAnomalies
Globalintermetricanomaly: CertainmetricsinMTSexperiencesignificantchanges,
withalengthmatchingtheentiresequence. Thistypeofanomalytypicallyoccurswhen
initialparametersorsystemstatesdeviatefromthenormalrange. Whenthechangeina
keymetrictriggersaseriesofabnormalfluctuationsinrelatedmetrics,theentiresequence
reflectsthisanomaly. AnexampleofanentiresequenceanomalyisshowninFigure3a,as
itsbehaviorsignificantlydeviatesfromthatofothermetrics.
diss (corr(xi,xj)) > δ (9)
corr
where xi, and xj are different metrics, and corr represents the degree of correlation be-
tweenthem.
Figure3. (a)Globalintermetricanomalies. (b)Thered-highlightedareaontheleftindicateslocal
intermetricanomalies,whilethered-highlightedareaontherightindicatestemporal-localintermet-
ricanomalies.
Local intermetric anomaly: There is correlation between metrics within the entity,
whichcanbelinearornonlinear,suchastherelationshipbetweentemperatureandelectric-
ityconsumption. Ifthesecorrelationsaredisrupted,MTSwillexhibitanomalousbehavior.
Duringacertaintimeperiod,therelationshipsbetweenmetricssignificantlydeviatefrom
historicalpatterns,suggestingachangeintheinterdependenciesamongthemetrics. For
example,inFigure3b,thereisinitiallyapositivecorrelationbetweentwometrics,butthe
highlightedredareaontheleftclearlybreaksthisrelationship,leadingtoanomalies.
diss (corr(xi,xj),corr(xi ,x j ) > δ (10)
corr t:t+k t:t+k
wherekisthetimewindow. Ifthecorrelationisdisruptedfromttot+k,itindicatesthat
thecorrelationcoefficienthasexceededthethresholdcomparedtothenormalvalue.
Temporal-localintermetricanomaly: Theanomaliesviolatethedependenciesbetween
metricsandtemporalrelationships,focusingonhowaspecificmetricbreaksitscorrelation
and deviates from its historical trend within a certain time period, as indicated by the
highlightedredareaontherightsideofFigure3b.
2.3. Time/FrequencyDomainAnalysis
Timeseriesfrequencydomainanalysisinvolvestransformingatimedomainsignal,
which is a signal that varies over time, into a frequency-domain representation. This
conversionallowsforabetterunderstandingofthesignal’sfrequencycomponentsand
periodicity. Frequencydomainanalysisrevealsthedifferentfrequencycomponentswithin

Sensors2025,25,190 6of27
atimeseries,whichhelpsinidentifyingcyclicpatterns,trends,andanomalies. Themost
commonlyusedformulaistheDiscreteFourierTransform(DFT):
T−1
X = ∑ x e −i2πkt/T, k =0,...,T−1 (11)
k t
t=0
whereX isthediscretecomplexamplitudeatfrequencyk,x isthetimeseriessignal,and
k t
iistheimaginaryunit.
The Fast Fourier Transform (FFT) typically uses Formula (11) to convert the time
domainintothefrequencydomain. FFTisanefficientcomputationalalgorithmfortheDFT,
itcanconverttheoriginaltimeseriesintoaspectrumandsortitbycoefficients,obtaining
theseasonalcyclebyreversingthehighestfrequency. Mostprogramminglanguagesand
mathematicallibrariesprovidebuilt-inFFTfunctionsthatcanbedirectlyusedtocompute
theDFT.
3. TaxonomyofMTSADMethods
Tosummarizetheexistingdeepmultivariatetimeseriesanomalydetectionmethods,
weproposedataxonomyfortheanomalydetectionstrategiesfromtheperspectivesof
learning paradigms and deep learning models. We present a general pipeline as illus-
tratedinFigure4. Wecategorizeanomalydetectionmethodsintoforecasting,reconstruc-
tionandcontrastivetypes. Aforecasting-basedmodelusesnexttimestamppredictions,
whereasareconstruction-basedmodeluseslatentrepresentationsofthewholetimeseries.
Contrastive-basedmethodsrelyoncalculatingthesimilarityordissimilaritybetweendata
points to conduct analysis and prediction. Table 1 offers a more detailed overview of
thesemethods.
3.1. Temporal/Spatial
Temporalanalysisfocusesonhowvariableschangeovertime,whilespatialanalysis
examineshowthesevariablesvaryacrossdifferentlocationsorspatialunits. Temporaland
spatialperspectivesofferamorethoroughunderstandingoftheunderlyingrelationships
andpatternsinMTS.
Figure4. ThegeneralpipelineforMTSADusingdeeplearningmodels. Givenasourcedata,we
firstprocessthesourcedatausingadataprocessingmodulethatperformsbasicdatacleaningand
normalizationtasks.Subsequently,weutilizetheanomalydetectionstrategiesfromtheperspectives
oflearningparadigmsanddeeplearningmodelstoobtainrepresentationsforexecutinganomaly
detectiontasksacrossdifferentapplicationdomains.

Sensors2025,25,190
7of27
Table1.MultivariateDeepAnomalyDetectionModelsinTimeSeries.T/S:Temporal/Spatial|Values:
[S: Spatial, T: Temporal, ST: Spatio-Temporal], T/F: Time/Frequency domain|Values: [T: Time,
F: Frequency], LP: Learn Paradigms|Values: [Su: Supervised, Un: Unsupervised, Semi: Semi-
supervised,Self:Self-supervised],Input:ModelInput|Values:[P:Point,W:Window].
| Model | Venue | Bonkbone | LP S/T | T/F Input | Code Language |
| ----- | ----- | -------- | ------ | --------- | ------------- |
Forecasting
✓
| DeepAnt[22] | IEEE’2018 | CNN | Un T   | T W | Pytorch |
| ----------- | --------- | --- | ------ | --- | ------- |
| TCN-ms[23]  | IOP’2019  | CNN | Semi T | T W | – –     |
✓
| TimesNet[24] | ICLR’2023     | CNN | Un T   | F W | Pytorch      |
| ------------ | ------------- | --- | ------ | --- | ------------ |
| LSTM-NDT[25] | KDD’2018      | RNN | Un T   | T W | ✓ Tensorflow |
| LGMAD[26]    | Elsevier’2019 | RNN | Semi T | T P | – –          |
| THOC[27]     | NeurIPS’2020  | RNN | Self T | T W | – –          |
| AD-LTI[28]   | TKDE’2020     | RNN | Un T   | F P | – –          |
✓
| MTAD-GAT[29]    | ICDM’2020  | GNN         | Self ST | T W | Tensorflow |
| --------------- | ---------- | ----------- | ------- | --- | ---------- |
| GDN[30]         | AAAI’2021  | GNN         | Un S    | T W | ✓ Pytorch  |
| FuSAGNet[31]    | KDD’2022   | GNN         | Un ST   | T W | – –        |
| DVGCRN[32]      | ICML’2022  | GNN         | Un ST   | T W | – –        |
| DyGraphAD[33]   | ACM’2024   | GNN         | Un ST   | T W | – –        |
| MAD[34]         | IJCNN’2022 | Transformer | Self T  | T W | – –        |
| CLFormer[35]    | EAAI’2023  | Transformer | Un ST   | T W | – –        |
| AnomalyBERT[36] | ICLR’2023  | Transformer | Self T  | T W | ✓ Pytorch  |
Reconstruction
✓
| DAGMM[37] | ICLR’2018 | AE  | Un T | T P | Pytorch |
| --------- | --------- | --- | ---- | --- | ------- |
✓
| MSCRED[38]   | AAAI’2019    | AE      | Semi T | T W | Tensorflow   |
| ------------ | ------------ | ------- | ------ | --- | ------------ |
| USAD[39]     | KDD’2020     | AE,GAN  | Un T   | T W | ✓ Pytorch    |
| NPSR[40]     | NeurIPS’2024 | AE      | Un T   | T W | ✓ Pytorch    |
| LSTM-VAE[41] | IEEE’2018    | VAE,RNN | Semi T | T P | ✓ Tensorflow |
✓
| OmniAnomaly[42] | KDD’2019 | VAE,GRU | Semi T | T W | Tensorflow |
| --------------- | -------- | ------- | ------ | --- | ---------- |
✓
| InterFusion[43] | KDD’2021 | VAE | Un T | T W | Tensorflow |
| --------------- | -------- | --- | ---- | --- | ---------- |
✓
| SLA-VAE[44] | WWW’2022   | VAE | Semi T | T W | Pytorch      |
| ----------- | ---------- | --- | ------ | --- | ------------ |
| LARA[16]    | WWW’2024   | VAE | Un T   | T W | ✓ Pytorch    |
| MAD-GAN[45] | ICANN’2019 | GAN | Un ST  | T W | ✓ Tensorflow |
✓
| TadGAN[46] | IEEE’2020 | GAN,LSTM | Un T | T W | Pytorch |
| ---------- | --------- | -------- | ---- | --- | ------- |
✓
| MIM-GAN[47] | IEEE’2023 | GAN,LSTM | Un T | T W | Tensorflow |
| ----------- | --------- | -------- | ---- | --- | ---------- |
✓
| DAEMON[48]      | WSDM’2023    | GAN,AE       | Un T  | T W | Pytorch   |
| --------------- | ------------ | ------------ | ----- | --- | --------- |
| DCGAN[17]       | AAAI’2024    | GAN,CNN      | Un T  | T W | ✓ Pytorch |
| DiffusionAE[49] | ICDMW’2023   | Diffusion,AE | Un T  | T W | ✓ Pytorch |
| D3R[18]         |              |              |       |     | ✓         |
|                 | NeurIPS’2024 | Diffusion    | Un ST | F W | Pytorch   |
✓
| TransAnomaly[50] | CCDC’2021 | Transformer,VAE | Un T | T W | Pytorch |
| ---------------- | --------- | --------------- | ---- | --- | ------- |
✓
AnomalyTransformer[51] ICLR’2022 Transformer Un T T W Pytorch
| TranAD[52] | VLDB’2022    | Transformer | Un T | T W | ✓ Pytorch |
| ---------- | ------------ | ----------- | ---- | --- | --------- |
| MEMTO[53]  | NeurIPS’2023 | Transformer | Un T | T W | ✓ Pytorch |
✓
| Dual-TF[54] | WWW’2024 | Transformer | Un T | TF W | Pytorch |
| ----------- | -------- | ----------- | ---- | ---- | ------- |
✓
| CATCH[55] | arXiv’2024 | Transformer | Un T | TF W | Pytorch |
| --------- | ---------- | ----------- | ---- | ---- | ------- |
Contrastive
| AnomalyLLM[56] | arXiv’2024 | LLMs | Un ST  | T W | ✓ Pytorch |
| -------------- | ---------- | ---- | ------ | --- | --------- |
| aLLM4TS[57]    | ICML’2024  | LLMs | Self T | T W | ✓ Pytorch |
| AnomalyLLM[58] | IJCAI’2024 | LLMs | Self T | T W | – –       |
✓
| PatchAD[59]    | arXiv’2024    | MLP-Mixer   | Un T   | T W | Pytorch   |
| -------------- | ------------- | ----------- | ------ | --- | --------- |
| TRL-CPC[60]    | Elsevier’2022 | Transformer | Un T   | T W | – –       |
| RESIST[61]     | Springer’2022 | Transformer | Un T   | T W | – –       |
| Dcdetector[13] | KDD’2023      | Transformer | Self T | T W | ✓ Pytorch |
✓
| SimAD[62] | arXiv’2024 | Transformer | Un T | T W | Pytorch |
| --------- | ---------- | ----------- | ---- | --- | ------- |
✓
| RESTAD[63] | arXiv’2024 | Transformer | Un T | T W | Pytorch |
| ---------- | ---------- | ----------- | ---- | --- | ------- |
3.2. RelatedLearningParadigms
Unsupervised,semi-supervisedandself-supervisedmethodsarecommonlearning
paradigmsinMTSAD,andtheycanbedistinguishedaccordingtothelabelinformationof
thedataandthedegreeofsupervision:

Sensors2025,25,190 8of27
UnsupervisedLearning:Unsupervisedanomalydetectiondoesnotrelyonanylabeled
anomalous data for training. It attempts to discover anomalous patterns by analyzing
thefeaturesofthetimeseries,whichmeansitneedstouseonlynormaldataduringthe
trainingphase.
Semi-unsupervisedLearning: Insemi-supervisedlearning,onlypartofthetraining
datahaslabelinformation,whiletheotherpartofthesamplehasnolabelinformation,
the model uses the sample with label information to learn during the training process,
andtriestoimprovetheperformancethroughtheunlabeledsample. Inthemultivariate
timeseriesanomalydetection,thesemi-supervisedlearningmethodcanusethelabeled
anomaly sample the original and unlabeled normal samples are trained to distinguish
betweennormalandabnormaltimeseriespatterns.
Self-supervised Learning: Self-supervised methods utilize unlabeled data to train
models by creating supervisory signals from the data itself. These methods typically
involvepredictingmissingpartsorpropertiesoftheinputbasedontheobserveddata,
allowingthemodeltolearnusefulrepresentationswithoutrequiringexplicitlabels,which
canthenbeappliedtovariousdownstreamtasks.
3.3. ModelInput
Themodelinputofmultivariatetimeseriesanomalydetectioncanbetimestepsor
windows(slidingwindows).Timestepsrefertoindividualpointsintimewhereobserva-
tionsarerecordedforeachvariableinthemultivariatetimeseries. Eachtimestepincludes
measurementsforallvariablesatthatspecificmoment. Windowissubsetsofconsecutive
timestepswithafixedsize.Thesewindowsareusedtoaggregatedataovertime,capturing
temporalpatternsandrelationshipsamongvariableswithineachwindow. Inrealworld,
thereareoftencomplexstructuressuchasnoise,seasonality,trends,etc.,andanomalies
usuallydonotappearatasinglepointintime,butpersistorpresentapatternoveraperiod
oftime. Therefore,themostrecentMTSADmodeltakesawindowinsteadofasinglepoint
asthemodelinput.
4. ForecastingMethods
Forecasting-based methods use historical data of time series to train a predictive
model that can forecast future data points. This method assesses the anomaly level by
comparing predicted values with actual values, considering anomalies as a significant
increaseinpredictionerror,asillustratedinFigure5a. Thissectionwillexplorepredictive
anomalydetectionmethods,focusingprimarilyonfourtypes: CNN-based,RNN-based,
GNN-based,andTransformer-basedmodels.
Figure5.Theexamplesofeachtypeofanomalycriteria:(a)aforecastingloss;(b)areconstruction
loss;and(c)acontrastiveloss.

Sensors2025,25,190 9of27
4.1. CNN-BasedModels
DeepAnt[22]proposesanunsupervisedanomalydetectionmethodbasedonCNN,
whichdoesnotrequirelabeledtrainingdata. ThismethodusesCNNtoautomaticallylearn
therepresentationoftimeseriesdataandidentifiesanomaliesusingreconstructionerror.
ComparedtotraditionalCNNs,TemporalConvolutionalNetworks(TCN)canbetterhandle
thetemporalcharacteristicsoftimeseries,TCN-ms[23]usesTCNforanomalydetection,
emphasizingtheimportanceoftemporalinformation. Byintroducingcausalconvolution
anddilatedconvolutionintheconvolutionoperationtoprocesstimeseriesdata,ithelpsto
capturelongdistancedependencies. However,theaforementionedmethodsonlyconsider
theone-dimensionalchangesofthetimeseries. Toenhancethemodel’sunderstandingof
thestructureoftimeseries,TimesNet[24]extendstheanalysisoftemporalchangesto2D
spacebyinnovativelyincorporatesFastFourierTransform,makingiteasytomodel2D
changeswith2Dkernels,andprovidinganewperspectiveformorecomplextimeseries
analysis. Itnotonlyimprovestheaccuracyofanomalydetectionbutalsoenhancesthe
model’sgeneralizationabilityofthemodelfortimeseriesdata.
4.2. RNN-BasedModels
LSTM-NAT[25]representsaninnovativeapplicationofRNNsforspacecrafttelemetry
analysis, emphasizingtheuseofLSTM[64]toidentifyanomalieswithincomplexdata.
Unliketraditionalmethods,LSTM-NATemploysanon-parametricdynamicthresholding
method,utilizinganunsupervisedapproachtoassessresidualsanddeterminewhether
predictionerrorsindicatespacecraftanomalies. However,itsrelianceonone-dimensional
outputslimitsitsabilitytohandlehigh-dimensionaldatainmultivariatescenarios. Build-
inguponthisfoundation,LGMAD[26]integratesLSTMwiththeGaussianMixtureModel
(GMM)[65],providingacomprehensivesolutionforlow-dimensionalsystemcharacteris-
tics. Thismethodnotonlyenhancestheefficiencyofanomalydetectionthroughthehealth
factorbutalsoexpandsitsapplicationtotheprocessingofMTSbyleveragingthestrengths
ofbothLSTMandGMMincapturingtemporaldynamicsandanalyzingfeaturecorrela-
tions. AnothernotableadvancementincapturingtemporaldynamicsistheTHOC[27].
ByintroducingtheTemporalHierarchicalOne-Classnetwork,whichusesadilatedRNN
with skip connections [66], the limitations of LSTM in capturing multi-scale temporal
dynamicsareaddressed. ThehierarchicalclusteringprocessofTHOCandtheintroduction
ofaself-supervisiontaskinthetemporaldomainsignificantlyenhancethemodel’sability
todetectanomaliesinreal-worldtimeseriesdata. However,theseschemesmayrequire
adjustmentsforspecifictypesofmulti-seasonaltimeseriesdatatoensuretheiraccuracy
andefficiency. Wuetal. [28]proposedanunsupervisedschemewithmulti-seasonality.
AD-LTIintroducedanewmetric—LocalTrendInconsistency(LTI),whichcanbecomputed
efficientlyandrobustlyscorestheprobabilityofanomaliesforeachdatapoint.Itovercomes
thechallengesofrequiringlabeleddataandthecomputationalintensityofprocessinglarge
volumesofdata,makingitsuitableforavarietyofevent-sensitivescenarios.
4.3. GNN-BasedModels
InthefieldofMTSAD,capturingthecomplexrelationshipsanddynamicchanges
inMTSiscrucial. TheMTAD-GAT[29]modellearnscomplexdependenciesonboththe
featureandtemporaldimensionsviaagraphattentionnetwork[67]andachieveshigh
performanceinMTSADthroughajointoptimizationstrategy. However,itmayencounter
issueswithefficiencyandscalabilitywhendealingwithlarge-scaledatasets. GDN[30]
leveragesgraphneuralnetworkstolearnadependencygraphamongsensorsandenhances
theinterpretabilityofanomalydetectionthroughattentionweights. However,itfailsto
fullycapturethespatialandtemporalcorrelationsbetweensensorswhenprocessingsensor

Sensors2025,25,190 10of27
data. To address these issues, Chen et al. [31] proposed DVGCRN, effectively models
thespatialandtemporalcorrelationsoftimeseriesbycombininganEmbedding-Guided
ProbabilisticGenerativeNetwork(DEPN)withanadaptivevariationalgraphconvolutional
recurrent network(GCRN), demonstrating superior performance in anomaly detection.
FuSAGNet[32]integratesfeatureselectionwithGNNstoeffectivelyidentifyandmodel
the relationships between different time series features. The model constructs an inter-
seriesadjacencymatrixbasedonthelatentfeaturerepresentationsgeneratedbyasparse
auto-encoder,enhancingitsabilitytodetectanomalies. TheDyGraphAD[33]framework
strengthens the capture of short-term and long-term dependency relationships in time
seriesthroughdynamicgraphforecasting,therebyimprovingdetectionaccuracy.
4.4. Transformer-BasedModels
Transformer-based models, with their self-attention mechanisms, have become a
cornerstoneinavarietyofsequencemodelingtasks[12],includingtimeseriesanalysis.
These models are particularly adept at capturing the inherent temporal dynamics and
complexpatternsintimeseriesdata.
AnomalyBERT[36]utilizesaself-supervisedmethod,whichdoesnotrequirelabeled
data,acommonscenarioinreal-worldsituations. Itsinnovativedatadegradationscheme
introduces synthetic outliers, enhancing the model’s ability to detect various types of
anomalieswhileeffectivelycapturingtemporaldependenciesandcontextualinformation
usingtheTransformerarchitecture. However,themodelmayfacechallengesintraining
duetothecomplexityoftheTransformerarchitectureandtheneedtobalancethedata
degradationscheme. MAD[34]alsoadoptsaself-supervisedlearningapproach,eliminat-
ingtheneedforlabeleddata. However,MADfocusesonmaskedmodeling,simplifying
thetrainingprocessbylearningrepresentationsofnormality,whichreducesthecomplexity
introducedbytheintegrationofsyntheticoutliers. MADimprovesuponthetraditional
NextStepPrediction(NSP)taskbyusingmaskedinputs,allowingthemodeltolearnfrom
bidirectionalcontexts. Nevertheless,comparedtoNSPmodels,MADisslowerduringthe
inferenceprocess,especiallywhenmaskingallstepssequentially. Toenhanceinference
speed while maintaining accuracy, CLformer [35] proposes a lightweight Transformer,
enhancinglocalfeatureextractionthroughmulti-scalecausalconvolutionandreducing
erroraccumulation. Additionally,theblockrecurrentpredictionstrategydecreasestime
andspacecomplexity,leadingtofasterinference.
4.5. ProsandCons
Thissectionexplorestheadvantagesanddisadvantagesofprediction-basedtimeseries
anomalydetectionmethods.CNNsexcelasfeatureextractorsforcapturinglocalfeaturesin
timeseriesdata;however,theirkernelsizeandoperationalmechanismslimittheirability
tocaptureglobaldependencies,whichrestrictstheirperformanceasabackbonefortime
seriesdata. RNN-basedmodelsperformwellincapturinglong-termdependencies,but
facescalabilitychallengeswhenprocessinglongsequencesduetotheirsequentialnature
andmemorylimitations. GNN-basedmodelsprovidedeepinsightsintospatio-temporal
dynamics,buttheirincreasedcomputationalcomplexityposesadditionalchallengeswhen
handlinglarge-scaleorhigh-dimensionaldata,andtheymaynotbesuitablefornon-graph
orfuzzygraphstructures. Incontrast,Transformer-basedModelstypicallyoutperform
othersinanomalydetectiontasks,astheyarebetterathandlinglong-rangedependencies
andachievingparallelprocessing. However,thesemodelsmayrequirefurtheradjustments
toensurethatimportantcontextualinformationisnotoverlooked.

Sensors2025,25,190 11of27
5. ReconstructionMethods
Reconstruction-basedmethodsuseanormaldatasettotrainamodelthatattempts
to encode the data into a latent space and then reconstruct the original data from this
representation. Reconstructionlossiscalculatedbycomparingthedifferencesbetweenthe
reconstructeddataandtheoriginaldata,asillustratedinFigure5b. Thissectiondelvesinto
reconstructionanomalydetectionmethods,focusingonfourtypes: AE-based,VAE-based,
GAN-based,Transformer-based,andDiffusion-basedmodels.
5.1. AE-BasedModels
Asaninnovativeapplicationinthefieldofunsupervisedlearning,modelsbasedon
autoencoders(AE)[68]havemadesignificantprogressintheareaofAD.DAGMM[37]
isthepioneeringmodelthatintegratesdeepAEwithGMM[65]forunsupervisedanomaly
detection. Unlike traditional techniques that perform density estimation after dimen-
sionality reduction, DAGMM optimizes both processes simultaneously, ensuring that
keyinformationforanomalydetectionispreserved. However,DAGMMreliesondeep
autoencoders,whichfacechallengesinescapinglocaloptimaandrequiresubstantialcom-
putationalresources. Toaddressthisissue,USAD[39]wasproposed,utilizingadversarial
trainingtoenhancethestabilityandspeedofautoencoder-basedanomalydetection. The
architecture of USAD enables it to train quickly and isolate anomalies effectively, mak-
ingitsuitableforlarge-scaleapplications. However,USADmaystrugglewithdetecting
subtleanomaliesbecauseitfocusesonreconstructionerror. Inresponsetothischallenge,
Zhang et al. [38] introduced MSCRED, which incorporates a multi-scale convolutional
recurrentencoder-decoderframeworktocapturetemporaldependenciesandinter-sensor
correlationswithinmultivariatetimeseriesdata. Itsapproachusingsignaturematrices
andanattentionmechanismallowsthemodeltorobustlydiagnoseanomaliesofvarying
severitylevels. However,thecomplexityofthemodelmayposechallengeswhendeal-
ing with extremely high-dimensional data or real-time applications. The next method
NPSR,proposedbyLaietal. [40],alsofacesthechallengeofhandlingthecomplexityof
high-dimensionaldata. NPSRmodulatestheanomalydetectionprocessbyintroducinga
NominalityScore,balancingthedetectionofpointandcontextualanomalies. TheNPSR
framework includes both point-based and sequence-based reconstruction models, and
itsperformancesurpassesexistingtechniques,offeringatheoreticallygroundedmethod
for anomaly detection. Further optimization is still needed for its application in high-
dimensionalsettingstoensurecomputationalefficiency.
5.2. VAE-BasedModels
VariationalAutoencoders(VAEs)[69]useanencodertomapinputdataintoaspace
oflatentrandomvariables,andthenreconstructthedatafromthisspacewithadecoder.
LSTM-VAE[41],theformernetworkisreplacedbyLSTMinVAE.However,LSTM-VAE
ignoresthetemporaldependencebetweenstochasticvariates. Hence,OmniAnomaly[42]
wasproposed,themodelisthefirstMTSADalgorithmcapableofhandlingexplicittem-
poraldependenciesamongrandomvariables. Itprovidesanovelmethodforentity-level
anomaly explanation through stochastic recurrent neural networks, the objective is to
learnthenormalpatternsofdataandutilizereconstructionprobabilityforanomalyde-
tection. Additionally,InterFusion[43]isanunsupervisedmethodthatmodelsboththe
inter-dependencyandtemporaldependencyofMTSsimultaneously. Itscoreideainvolves
modeling the normal patterns within data using a hierarchical VAE with two stochas-
ticlatentvariables,eachlearninglow-dimensionalembeddingsofeitherinter-metricor
temporalaspects. UnsupervisedVAEisvulnerabletotheinfluenceofanomalousinputs.
SLA-VAE[44]addressesthechallengeofobtaininglabeleddatainInterFusionthrough

Sensors2025,25,190 12of27
semi-supervisedlearning,utilizingactivelearningtoleverageasmallnumberofhighly
uncertain samples for learning and updating online system anomaly detection models.
LARA[16]solvestheneedforonlinesystemstoquicklyadapttonewdistributionswitha
lightweightretrainingapproach. LARAdesignstheretrainingprocessasaconvexproblem
topreventoverfittingandensurerapidconvergence. Italsohasthecapabilitytoutilize
historicaldatawithouttheneedforstorage.
5.3. GAN-BasedModels
TheprincipleofGAN[70]isbasedonaframeworkknownasadversarialtraining,
whichconsistsoftwocomponents: ageneratordesignedtomimicthedistributionofreal
data,andadiscriminatortaskedwithdistinguishingbetweengeneratedandauthenticdata.
MAD-GAN[45]employsLSTM-RNNsasboththegeneratoranddiscriminatorwithin
aGANframeworktoseizethetemporalrelationshipsbetweentimeseriesdistributions,
whilealsotakingintoaccountthecompletedatasettouncovertheunderlyinginteractions
amongthem. MAD-GANusingstandardadversariallosssuffersfromgradientexplosion
andmodecollapse. Hence,TadGAN[46]combineswassersteinloss[71]andcycleconsis-
tencyloss[72]toformthefinalminmaxobjective,theformeraimstomatchthedistribution
ofgeneratedtimeserieswiththedatadistributionofthetargetdomain,whilethelatter
preventsconflictingoutputsbetweenthetwogenerators. Additionally,MIM-GAN[47]
introducesanexponentialinformationmetricintothelossfunctionofGANstoavoidlocal
optimalsolutionandmodelcollapse. Itconsidersadiscriminativereconstructionscore
composedofdiscriminativeandreconstructionloss. MIM-GANemploysLSTM-basedgen-
eratorsanddiscriminatorstocapturetemporalrelationshipswithinthedata.Soft-DTW[73]
isusedasadifferentiablealternativeforthereconstructionloss,andthecombinationof
reconstructionlossandthepriorprobabilitydistributionofthelatentspaceservesasthe
anomalyscore. DCGANs[17]canadjustthegeneratortoproducesamplesclosertoreal
databyminimizingtheSoft-DTWloss. DCGANsutilizeCNNsinboththegeneratorand
discriminatornetworks,whileperformingparallelcomputationforthereconstructionof
multiplepoints,effectivelyalleviatingperformancebottlenecks(i.e.,ModeCollapse). In
complexsystems,thedatageneratedbydevicesexhibitcomplexpatternsandascarcityof
labeleddata,makinganomalydetectionasignificantchallenge. DAEMON[48]employs
twodiscriminatorstoadversariallytrainanautoencodertolearnthenormalpatternsof
timeseries, usingreconstructionerrorstoidentifyanomalies. Itsrobustnessisensured
throughregularizationofhiddenvariablesandreconstructeddata.
5.4. Transformer-BasedModels
Duetothecomplextemporalcharacteristics(i.e.,temporaldependency,inter-variable
correlations,andnoise)inmultivariatetimeseries,manydifferenthybridschemeshave
beenproposed. TransAnomaly[50]isthefirstmodelcombiningTransformerandVAEfor
timeseriesdata. TransAnomalyenablesmoreparallelizationandreduceslearningcosts.
TranAD[52]proposestheuseofattention-basedsequenceencodersforrapidinference,
combinedwithadaptiveconditioningandadversarialtrainingtoenhancethestabilityof
themodel. However,theproblemofover-generalizationpersists. MEMTO[53]introduces
a novel memory module that can learn how each memory item should be updated in
responsetoinputdata,adaptingtodiversenormalpatterns. Duetotherarityofanomalies
intimeseriesdataandthedifficultyofestablishingnon-trivialassociationsfromanomalies
totheentireseries,AnomalyTransformer[51]calculatesassociationdiscrepancythrougha
newAnomaly-Attentionmechanismandenhancesthedistinguishabilitybetweennormal
andabnormalpointswithaminimaxstrategy,demonstratingthepotentialofTransformers
incapturingassociationsofanomalypointsintimeseries.

Sensors2025,25,190 13of27
Theaforementionedmethodsareallinthetimedomainanddonotutilizefrequency
domaininformation. Recentstudieshaveattemptedtoimprovetheaccuracyofanomaly
detection by combining information from both the time and frequency domains. Dual-
TF [54] proposes a Nested-Sliding Windows (NS-window) technique, where anomaly
scoresinthetimedomainarecalculatedwithintheouterwindow, andanomalyscores
inthefrequencydomainarecalculatedwithintheinnerwindow,achievingalignmentof
anomalyscoresatthegranularityofindividualdatapoints. CATCH[55]performspatching
operationsinthefrequencydomaintocapturefine-grainedfrequencycharacteristicsand
usesaChannelFusionModule(CFM)toperceivecorrelationsbetweenchannels. Ituses
Frequency-EnhancedPoint-GranularityScoringtechnology[54]tocalculatetheanomaly
scoreforeachtimepoint, whichinvolvespatchscanningandfrequencyreconstruction
withintheinputwindow.
5.5. Diffusion-BasedModels
DiffusionmodelsperturbtheobserveddatabygraduallyaddingGaussiannoise[74]
andthenutilizealearnabletransformationtorecovertheoriginaldata.
DiffusionAE [49] conditions the diffusion process on autoencoder reconstructions
ratherthantheoriginaldata. DiffusionAEachievesgreaterrobustnesstovaryingtraining
anomaly ratios and better handling of multiple anomaly types (i.e., point anomaly) in
the dataset. The diffusion process smooths out abnormal fragment, resulting in higher
reconstructionerrors,whichinturnimprovesperformance. However,thetrainingcostto
adjusttheinformationbottleneckinthereconstructionprocessishigh. D3R[18]introduces
amethodcallednoisediffusiontoexternallymanagetheinformationbottleneck. Diffu-
sionreframesthebottleneckbytreatingnoiseasthelimitingfactoranduncontaminated
informationasacondition. Asthebottleneckisnolongerinherenttothemodel,itcanbe
adjustedinsizewithoutrequiringretraining.
5.6. ProsandCons
Thissectiondescribestheadvantagesandlimitationsoftheaforementionedanomaly
detectionmodelsfortimeseriesdata.AE-basedmethodsautomaticallyextractdatafeatures
but cannot capture all the complexities of the data and have difficulty interpreting the
meaningofreconstructionerrors. VAEisadeptatexplicitlymodelingprobabilitiesand
provideatheoreticalfoundationforunderstandingdatadistributions.However,themodels
relyontheassumptionofGaussiandistributions,whichmaylimittheexpressivepowerof
thesemodels. GAN-basedmodelslearncomplexdatadistributionsthroughadversarial
training,maintaininganimpressivefidelitytotheoriginaldatadistributions. Nevertheless,
theyareverychallengingtotrainduetoissueslikevanishinggradients[75],whichcan
hindermodelstabilityandconvergence. Diffusionmodelsperformwellwhenfacingnoise
andmissingdata,astheycaninfermissingpartsduringthegenerationprocess,allowing
them to better understand the distribution of normal data when detecting anomalies.
However,whenhandlingtheboundarybetweenmissingandobservedparts,themodel
mayexhibitinconsistencies[49]. Additionally,capturingthedynamiccharacteristicsof
timeseriesmayrequirefurtheradjustmentsandimprovements.
6. ContrastiveMethods
Contrastivemethodsoperatewithintheframeworkofcontrastivelearning, which
typicallyinvolvesadual-towermodel. Timeseriesdataisinputintotwodistinctrepresen-
tationlearningnetworkstogeneratetworepresentationvectors. Duringtherepresentation
learningphase,representationsofthetimeseriesareextractedfromdifferentperspectives,
itisnecessarytouseacontrastivefusionmodule(suchasupsampling)toaligntherep-

Sensors2025,25,190 14of27
resentationstoeachtimestep. Subsequently, acontrastivelossisemployedtocalculate
thesimilaritybetweendifferentrepresentations. AsillustratedinFigure5c. Themethod
iscommonlyusedinunsupervisedorself-supervisedlearningtasks. Thissectiondelves
intocontrastiveanomalydetectionmethods,focusingonthreetypes: Transformer-based,
MLP-basedmodels,LLMs-bsed.
6.1. LLMs-BasedModels
Recently,LLMshavegainedpopularityintimeseriesAnalysis[76,77]. Refs. [56,58]
paperssharethesamemodelname,AnomalyLLM,buttheyadoptdifferentstrategiesto
addressanomalydetectionissuesintheirrespectivefields. TheformerAnomalyLLM[56]
involvespre-trainingadynamic-awareencodertogeneraterepresentationsofedgesin
dynamicgraphs. Thisincludesconstructingstructural-temporalsubgraphsandoptimizing
with contrastive loss to capture the structural and temporal information of the edges.
Byselectingwordembeddingsrelatedtodynamicgraphsandclusteringthemintotext
prototypes,thesetextprototypesarethenusedtoreprogramedgeembeddingstoalignthe
semanticsbetweendynamicgraphsandLLMs. Aprompttemplateisdesignedtoencode
theinformationofafewlabeledsamplesintotheLLM,enablingthemodeltoadaptto
varioustypesofanomalieswithoutupdatingmodelparameters. Thelatter,proposedby
Liuetal. [58],introducesaknowledgedistillation-basedmethodwhereastudentnetwork
is trained to mimic the output of a teacher network that is pre-trained on a large-scale
dataset. During the testing phase, anomalies are detected when there is a significant
discrepancy between the outputs of the student and teacher networks. To consolidate
normalfeatureextraction,prototypicalsignalsareincorporatedintothestudentnetwork,
makingitmorefocusedonhistoricalnormalpatterns. Syntheticanomaliesaregenerated
throughdataaugmentationtechniquestoexpandtherepresentationgapbetweenthetwo
networks. Additionally,acontrastivelossisusedtobringtherepresentationsoforiginal
andaugmentedsamplesintheteachernetworkclosertogether,servingasaregularization
termtoencouragetheteachernetworktocapturemoregeneralpatterns.
aLLM4TS[57]adaptsLLMsfortimeseriesthroughatwo-stagetrainingstrategy. Ini-
tially,itundergoescausalcontinuouspre-trainingonvarioustimeseriesdatasets,followed
by fine-tuning for multi-patch prediction in specific time series contexts. A distinctive
featureofthisframeworkisthepatch-wisedecodinglayer,whichconvertsindividualdata
patches(segments)directlyintotimeseries,therebysignificantlyenhancingthemodel’s
abilitytomastertimeseriesrepresentationsbasedontemporalpatches.
6.2. MLPMixer-BasedModels
Recently,analysesoftimeseriespredictionhaveshownthattheMLP-Mixercaneffec-
tivelyhandlesequentialdata[78–80]. PatchAD[59]representsadeparturefromtraditional
reconstruction-basedapproaches. ThemodelconsistsoffourdistinctMLPMixers,specifi-
callydesignedtoachieveefficiencyandlight-weightusingtheMLParchitecture. PatchAD
innovativelyintroducesadual-projectionconstraintmoduletoalleviatepotentialmodel
degradation. For practitioners and researchers seeking the latest and potentially more
effectivemethodsforMTSAD,thispapermaybevaluablereadingmaterial.
6.3. Transformer-BasedModels
Existingreconstruction-methodsfrequentlyfailtohandlesufficienttemporalcontext
andinadequaterepresentationofnormalpatterns,hinderingtheireffectivenessinidentify-
ingabnormalbehaviors. TheTRL-CPC[60]explorestheintegrationofcontrastivelearning
intotimeseriesanalysis. InTRL-CPC,thecontextvectorsrepresentobservationwindows
inMTS.Thelatentrepresentationsofsubsequenttimestepsareobtainedthroughnonlinear
transformationsofthesecontextvectorsarecontrastedwiththelatentrepresentationsof

Sensors2025,25,190 15of27
theencoderformultivariatetimeseriestomaximizepositivedensity. RESIST[61]relies
onarobustlossfunctionbasedoncontrastivelearningtotrainaTransformerthatmodels
theexpectedbehaviorofnetworkactivity,withouttheneedforananomaly-freetraining
subset. Itautomaticallymitigatestheimpactofatypicalcorruptedtrainingdatatoreduce
theirinfluenceontrainingoptimization. DCdetector[13]employsacontrastivelearning
frameworktolearnrepresentationsoftimeseriesdata. Byutilizingadual-attentionmecha-
nism,itobtainsrepresentationsoftheinputtimeseriesfromtwobranches(thein-patch
branchandthepatch-wisebranch). Thecontrastivelossfunctionisdefinedbymeasuring
the similarity of representations from these two different perspectives, thus acquiring
permutation-invariantrepresentationswithsuperiordiscriminativecapabilities.
Recentresearchhasbeguntocombinereconstructionandcontrastivelearningtocreate
a comprehensive integrated anomaly score that can capture deviations from expected
patternsandeffectivelyidentifysubtleanomalies. SimAD[62]combinesasophisticated
featureextractoradeptathandlingextendedtimewindows,integratesnormalbehavior
patternscomprehensivelyusingtheEmbedPatchencoder,andintroducesaninnovative
ContrastFusion module aimed at highlighting distribution differences between normal
andabnormaldatatoenhancetherobustnessofAD.RESTAD[63]implementsaRadial
BasisFunction(RBF)neuronlayerintheTransformermodeltorepresentanon-parametric
densityinthelatentspace. AhighoutputfromtheRBFindicatessimilaritywithnormal
training data. Additionally, RESTAD merges RBF similarity scores with reconstruction
errorstoenhanceanomalydetectionsensitivity.
6.4. ProsandCons
Thissectiondescribestheadvantagesandlimitationsoftheaforementionedanomaly
detectionmodelsfortimeseriesdata. MLPMixer-basedmethodsfeatureasimplestructure
thatiseasytoimplementandcanbeadaptedtovariousdatacomplexitiesbyadjusting
thenumberoflayersandneurons[78]. AlthoughMLPcancapturenonlinearrelationships,
theymaynoteffectivelyhandleextremelycomplexdatadistributions. LLMs-basedmodels
havelearnedawealthofsemanticknowledgethroughpre-trainingonlargetextdatasets,
possessingstrongrepresentationalcapabilities. Theyareadaptabletoavarietyofdown-
streamtasksandcanalsoperformwellinfew-shotlearningscenarios,butdirectlyapplying
LLMsforTSADisnoteffective. Itrequiresthedesignofpromptingstrategiesandproper
fine-tuningtoenhancetheirabilitytodetectandinterpretanomalies[76]. Moreover,LLMs
maystrugglewithmorecomplex,context-relatedanomaliesandmayhallucinatewhen
indexingandexplaininganomalypoints.
7. Datasets
Thissectioncompilesandsummarizesavarietyofdatasetsandevaluationbenchmarks
forMTSAD,aimingtoprovidecomprehensiveresearchresourcesforresearchersinthis
field. Thesedatasetsincludebothgeneralandspecializedtimeseriesdatasetsthatcanbe
usedfortheevaluationofanomalydetectiontasks,withthelatterbeingapplicableunder
certainassumptionsorspecificcustomizations. Eachdatasetorbenchmarkisdescribed
indetailthroughmultipledimensionsandtheirinherentcharacteristics. InTable2,we
havecollectedandanalyzeddatasetsthatarewellknownorfrequentlycitedinthefieldof
MTSAD,whichhavebeentestedbyaseriesofdeeplearningmodels.
Applicationstypicallyproducedataviaasequenceofdatagenerationprocessesthat
mirrorsystemoperationsorofferinsightsintothebehaviorofvariousentities. Anomalies
frequentlyemergeasaconsequenceofirregularitiesinthesedatagenerationprocesses,
highlightingunusualaspectsofthesystemsandentitiesinvolved. Identifyingsuchatypical

Sensors2025,25,190
16of27
traitscanyieldvaluableinsightsacrossdiverseapplications. Thedeeplearningmodels
outlinedbelowarecategorizedbasedontheirrespectiveapplicationdomains.
Table2.Publicdataset/benchmarkusedmostlyforMTSAD.R/S:Thesourceofthedata,whether
itisrealworlddataorsyntheticdata. Samples: Individualdatapointsorobservationswithina
dataset. Entities: Independentobservationunitorobject,suchassensors,machines,devices,etc.
Dims:Thenumberoffeaturesorvariablesinthedata.Rate:Theproportionofanomaloussamples
withinthedataset.
| Datasets/Benchmark       | R/S Samples    | Entities Dims | Rate Domain                    |
| ------------------------ | -------------- | ------------- | ------------------------------ |
| MSL[25]                  | Real 132,046   | 27 55         | 10.48 Aerospace                |
| NASAShuttleValveData[81] | Real 49,097    | 1 9           | 7.0 Aerospace                  |
| IOnsphere[82]            | Real 351       | 33            | 36.0 Astronomy                 |
| SWAN-SF[83]              | Real 355,330   | 5 51          | 23.8 Astronomy                 |
| SMAP[25]                 | Real 562,800   | 55 25         | 12.83 Environmentalscience     |
| OPPORTUNITY[82]          | Real 36,224    | 24 133        | 3.4 Environmentalscience       |
| GECCO[84]                | Real 138,521   | 1 9           | 1.25 Internetofthings(IoT)     |
| CICIDS[85]               | Real 170,231   | 72            | 1.28 Internetofthings(IoT)     |
| Kitsune[82]              | Real 3,018,973 | 9 115         | 17.0 Cybersecurity             |
| Http(KDDCUP99)[86]       | Real 567,479   | 3             | 0.4 Cybersecurity              |
| Smtp(KDDCUP99)[86]       | Real 95,156    | 3             | 0.03 Cybersecurity             |
| NAB-realAdExchange[87]   | Real 9616      | 3 2           | Businessandfinance             |
| Creditcard[88]           | Real 284,807   | 1 29          | 0.17 Businessandfinance        |
| Genesis[89]              | Real 16,220    | 1 18          | 0.3 Industrialcontrolsystems   |
| GHL[90]                  | Synth 200,001  | 48 22         | 0.4 Industrialcontrolsystems   |
| SWaT[91,92]              | Real 946,719   | 1 51          | 11.98 Industrialcontrolsystems |
| WADI[93]                 | Real 957,372   | 1 123         | 5.99 Industrialcontrolsystems  |
| trimSyn[38]              | Synth 17,680   | 1 35          | 2.34 Industrialcontrolsystems  |
| MSDS[94]                 | Real 292,860   | 1 10          | 5.37 Industrialcontrolsystems  |
| Arrhythmia[95]           | Real 452       | 1 274         | 15.0 Healthcare                |
| MBA[96]                  | Real 200,000   | 8 2           | 0.14 Healthcare                |
| Thyroid[97]              | Real 3772      | 6             | 2.5 Healthcare                 |
| SVDB[98]                 | Real 230,400   | 78 2          | 13.6 Healthcare                |
| Daphnet[82,99]           | Real 32,594    | 35 3          | 13.2 Healthcare                |
| Callt2[82,100]           | Real 10,080    | 2 2           | 4.1 Infrastructure             |
| Metro[82]                | Real 48,204    | 1 5           | 0.1 Infrastructure             |
| NYC[101]                 | Real 17,520    | 3             | 0.57 Infrastructure            |
| Occupancy[82]            | Real 6208      | 2 8           | 28.7 Infrastructure            |
| Exathlon[102]            | Real 47,530    | 39 45         | 18.3 Servermonitoring          |
| MBD[103]                 | Real 8640      | 5 26          | Servermonitoring               |
| MMS[103]                 | Real 4370      | 50 7          | Servermonitoring               |
| PSM[104]                 | Real 132,480   | 1 25          | 27.76 Servermonitoring         |
| SMD[105]                 | Real 1,416,825 | 28 38         | 4.16 Servermonitoring          |
7.1. Astronomy
Inthefieldofastronomy,datasetstypicallyincludevariousobservationalandsim-
ulationdata,mainlyusedtostudyphenomenasuchastheuniverse,galaxies,stars,and
planets [106,107]. The Ionosphere dataset [82] comes from the UCI Machine Learning
Repositoryandisusedforabinaryclassificationtask,withthegoalofdeterminingwhether
thereareelectronspresentintheionospherebasedonreceivedsignals.Thedatasetincludes
individualfeatureinformationaswellasionospherethresholds.Itcontains351samplesand
33features,whereeachsamplerepresentsameasurementofaradarechosignal. Various
classificationalgorithmscanbeusedformodeltrainingandvalidationwhenworkingwith
theIonospheredataset. Thedatasethasahighfeaturedimension,whichmayleadtothe
“curseofdimensionality”duringmodeltraining. Additionally,handlingnoiseandoutliers
inthedatasetisanotherimportantchallenge. TheAERO[14]modelcandistinguishnormal
temporalpatternsfrompotentialanomaliesinastronomicalobservations,effectivelydiffer-
entiateconcurrentnoise,andreducethenumberoffalsealarms. SWAN-SF(SpaceWeather

Sensors2025,25,190 17of27
AnalyticsforSolarFlares)[83]isamultivariatetimeseriesbenchmarkdatasetdesigned
forthefieldofsolarphysics. Thedatasetcontains4075solaractiveregions,spanningthe
9-yearoperationalperiodoftheSolarDynamicsObservatory(SDO).Accuratepredictionof
solarflaresiscrucialforastronauts,spaceequipment,andsatellitecommunicationsystems.
7.2. Aerospace
Intheaerospacefield,MTSADdatasetsaretypicallyusedtomonitortheperformance
parametersandtelemetrydataofaircraft,satellites,spacecraft,andotherrelatedequipment.
Aerospace datasets are crucial for predicting equipment failures and ensuring mission
success. By conducting in-depth analysis of this time series data, anomaly detection
algorithms can be developed and tested to enhance the reliability and performance of
aerospace systems [108,109]. For instance, the NASA Shuttle Valve Data [81] includes
telemetrydatafromshuttlevalves,whichisusedtoanalyzethehealthconditionofthe
valvesandpredictpotentialmalfunctions. TheMSL(MarsScienceLaboratory)dataset[25],
collectedbyNASA,containstime-seriesdatafrom27channels,eachwith55dimensions.
Thedataisanonymized,standardizedtoarangeof0–1,andrecordedeveryminute. Except
for the telemetry values, which are continuous, most variables are binary (indicating
whethercommandsweresent). AnLSTM-basedmodelcanbeusedforanomalydetection
inthisdataset. Hundmanetal. [25]proposedtheLSTM-NDT,anunsupervisedmethod
forunivariatetimeseriesanomalydetection,whichservesasanon-parametricanomaly
thresholdmethodforNASAdatasets.
7.3. EnvironmentalScience
Datasetsinthefieldofenvironmentalscienceareprimarilyusedformonitoringand
managingnaturalresources,environmentalquality,andthehealthofecosystems[110,111].
For instance, the SMAP [25] provides measurements of soil moisture and temperature,
which are crucial for understanding the water cycle, crop health, and climate change.
By conducting in-depth analysis of this time series data, we can better understand the
dynamicsofenvironmentalsystemsandprovidedatasupportforsustainabledevelopment.
The OPPORTUNITY dataset [82] contains data from 23 body-worn sensors, 12 object-
placementsensors,and21environmentalsensors,usedtomeasurethedailyactivitiesof
foursubjects. TheOPPORTUNITYdatasetiswidelyusedinresearchinthefieldsofdeep
learningandartificialintelligence,particularlyinactivityrecognition,andhasbecomean
importantbenchmarkdataset. ItisoftenutilizedwithCNNsandLSTMscombinedwith
spatio-temporalfeatureextractiontocapturecomplexactivitypatterns.
7.4. InternetofThings(IoT)
In the field of IoT, time series anomaly detection datasets are primarily used for
monitoringandanalyzingdatastreamsgeneratedbyavastarrayofinterconnecteddevices
andsensors. Thisallowsforthetimelydetectionofequipmentfailures,networkanomalies,
orunexpectedbehaviors[112]. TheGECCOIoT[84]dataset,forinstance,containssensor
data from smart home or industrial IoT devices, which is utilized for detecting device
anomaliesandsystemmalfunctions. TheCICIDSdataset[85]containssamplesofvarious
networkattacksandnormaltraffic. Itincludesdatafromnormalactivitiesandsimulated
maliciousattackscollectedoverfivedays.ThedatawasgeneratedusingtheCICFlowMeter
toolandprovidesrichlabeleddata. DeeplearningbasedmodelsontheCICIDSdataset
havesignificantlyimprovedtheaccuracyofintrusiondetection. Researchershaveexplored
deeplearningmethods,suchasmultilayerperceptronsandconvolutionalneuralnetworks,
toenhancedetectionaccuracyandefficiency.
IntheIoT,millionsofconnecteddevicesandsmartsensorsgeneratehighlydynamic,
large-scale,heterogeneous,andtimestampeddata. Thistimestampeddataisatthecoreof

Sensors2025,25,190 18of27
IoTautomationandhasthepotentialtosignificantlyimpactindustrialprocesses. Effec-
tivelydetectinganomaliesintime-seriesdataandprovidingreal-timeactionableinsightsto
driveimprovementsinindustrialprocessespresentssignificantchallenges. Liuetal.[113]
proposedtheAMCNN-LSTMmodel,whichemphasizescommunicationefficiencyand
federatedlearning(FL)methodsondevices,enablingdistributededgedevicestocollabora-
tivelytrainananomalydetectionmodel. Toachievereal-timeanomalydetection,Nizam
etal.[114]proposedahybridend-to-enddeepanomalydetectionframeworkthatleverages
CNNandLSTMnetworkstodevelopanadvancedanomalydetectionsystem. Thesystem
architectureconsistsofthreelayers: sensorsandmachinesintheindustrialsetting,anedge
layerforreal-timedataprocessing,andacloudlayerforoffloadingprocessingtasks. The
frameworkisdesignedtoaccuratelydetectanomaliesandextremelyrareeventsinIoT
streamingdata.
7.5. BusinessandFinance
Inthebusinessandfinancesector,timeseriesdatasetsarecrucialforidentifyingand
preventingfraud,marketanomalies,creditrisks,andotherfinancialissues[3]. TheNAB-
realAdExchange dataset [87] is part of the Numenta Anomaly Benchmark (NAB). This
datasetrecordsonlineadvertisementclick-throughrates,withthemetricbeingcostper
click(CPC).Itcontainsonefilewithnoanomaliesandanotherfilewithanomalies,designed
toevaluatetheperformanceofanomalydetectionalgorithmsonreal-timestreamingdata.
TheCreditCarddataset[88]containsrecordsofcreditcardtransactions,primarilyusedfor
identifyinganddetectinganomaloustransactions,thatis,potentialfraudulentactivities.
Whendealingwithfinancialtimeseriesinvolvingvariousmarketriskfactors,amajor
issueisthepresenceofanomalies. Theseanomaliescanleadtocalibrationerrorsinmod-
elsusedforquantifyingandmanagingrisk,resultinginpotentialmisestimationsofrisk.
Crépeyetal. [115]proposedananomalydetectionmethodforfinancialtimeseriesthat
combinesPrincipalComponentAnalysis(PCA)andneuralnetworks. Byreducingdimen-
sionalitywithPCA,thisapproacheffectivelyextractskeyfeaturesfromhigh-dimensional
financialtimeseriesdata,simplifyingthesubsequentanomalydetectionprocess. Neural
networksarethenappliedtoidentifynonlinearrelationshipsandcomplexpatterns. To
detectanomaliesinmorepracticalbusinessscenariosintherealworld,contextualinfor-
mationisneededforaccurateprediction. Time-CAD[116]isacontext-awaredeeptime
seriesdecompositionframeworkthatusesdeeplearningtechniquestodecomposetime
seriesdataandincorporatescontextualinformationtoimprovetheaccuracyofanomaly
detection. Thismethodiscapableofeffectivelydetectinganomaliesinbusinessprocesses.
7.6. Cybersecurity
Inthefieldofcybersecurity,timeseriesanomalydetectiondatasetsareprimarilyused
formonitoringandanalyzingnetworktraffic,userbehavior,andsystemlogstopromptly
identifysecuritythreats,intrusionattempts,andabnormalactivities. TheKDDCUP99[86]
isaclassiccybersecuritydatasetwidelyusedforresearchinnetworkanomalydetection. It
containsvarioustypesofcyberattacks,suchasDoS(DenialofService),Probe,R2L(Remote
toLocal),U2R(UsertoRoot),aswellastrafficdatafromnormalbehavior. TheKitsune
dataset [82] is a dataset used for network intrusion detection, containing both normal
andanomalousnetworktrafficdata. Thisdatasetisusedtotrainandtestdeeplearning
models to differentiate between normal and malicious traffic. KitNET [117] is a deep
learningmodelthatusesasetofautoencodersforonlinenetworkintrusiondetection. This
unsupervisedmethodcanlearntodistinguishthecharacteristicsofnormalandanomalous
networktrafficwithouttheneedforexpert-labeledtrafficdata.

Sensors2025,25,190 19of27
7.7. IndustrialControlSystems
InthefieldofIndustrialControlSystems(ICS),timeseriesdatasetsarecommonlyused
formonitoringandanalyzingtheoperationalstatusofindustrialequipment.Thisfacilitates
thetimelydetectionofequipmentfailures,predictionofmaintenanceneeds,optimization
ofproductionprocesses,andensuringproductionsafety. TheWADI(WaterDistribution)
dataset[93],collectedandopen-sourcedbytheiTrustinstituteoftheSingaporeUniversity
ofTechnologyandDesign(SUTD),isusedtosimulatewatertreatmentanddistribution
networks.Thisdatasetincludessensordataandnetworkdata,coveringmultiplestages
ofthewatertreatmentprocess,suchasrawwaterintake,chemicaltreatment,filtration,
dechlorination, and reverse osmosis. The SWaT (Secure Water Treatment) [91] is also
providedbytheiTrustinstituteofSUTDandservesasatestplatformforresearchinthe
fieldofISCforwatertreatmentprocesses. TheSWaTdatasetcontainssensordatafrom
variousstagesofthewatertreatmentprocess.
IndustrialControlSystems(ICS)arewidelyusedandarecrucialtobothindustryand
society. Failuresinthesesystemscanhavesevereimpactsontheeconomyandhumanlife.
Asaresult,thesesystemshavebecomeattractivetargetsforbothphysicalandcyberattacks.
Kravchiketal. [118]proposedanefficientmethodfordetectingnetworkattacksinICS,
whichcombineslightweightneuralnetworkswithPrincipalComponentAnalysis(PCA).
This approach aims to reduce computational resource consumption while maintaining
highdetectionaccuracy,whichisparticularlyimportantinresource-constrainedICSen-
vironments. Anomaly detection is critical for preventing cybersecurity intrusions and
system attacks. Many AI-based anomaly detection methods have been proposed with
high detection performance, but they remain a “black box” that is difficult to interpret.
Hoangetal. [119]usedexplainableartificialintelligence(XAI)toenhancetheperspective
andreliabilityofanLSTM-basedAutoencoder-OCSVMlearningmodelforanomalyde-
tection in ICS. This model is capable of providing detailed information about detected
anomalies,helpingsecurityteamsmakeinformeddecisions.
7.8. Healthcare
Inthehealthcaredomain,timeseriesanomalydetectiondatasetsareprimarilyuti-
lizedformonitoringandanalyzinganindividual’sphysiologicalparameters. Thisallows
for the timely detection of health issues, abnormalities in diseases, or malfunctions in
medicalequipment. Forinstance,theMIT-BIHArrhythmiaDatabase(ECG)[95]contains
avastcollectionofelectrocardiogram(ECG)recordsthatareusedforthedetectionand
analysis of cardiac arrhythmias. The SVDB [98] offers a range of standard and variant
electrocardiogramrecordings,whichareemployedinresearchoncardiachealthandthe
detectionofarrhythmias. Thesedatasetsareinstrumentalinadvancingourunderstanding
ofheartconditionsandindevelopingmoreeffectivediagnosticandmonitoringtoolsfor
healthcareprofessionals.
Electrocardiogram (ECG) signals are commonly used to assess heart health. The
heart,beingacomplexorgan,canexhibitmanydifferenttypesofarrhythmias. Therefore,
applying anomaly detection methods to analyze ECG signals can be highly beneficial.
ANNet [120] utilizes LSTM networks and MLP to process ECG signals, and improves
theaccuracyofanomalydetectionbycombiningfeaturevectors. Thestudyalsoincludes
preprocessingstepsforECGsignals,suchasdenoisingwithDiscreteWaveletTransform
(DWT)andusinga60Hznotchfiltertoremovepowerlineinterference(PLI).Similarly,
Alamretal. [121]proposedanunsupervisedtransformer-basedanomalydetectionmethod.
Themodelarchitectureconsistsoftwoparts: atransformermodelforfeatureextraction
andaclassifierforanomalyscoring, whichisusedtoevaluateanddetectanomaliesin
ECGsignals.

Sensors2025,25,190 20of27
7.9. ServerMonitoring
Timeseriesanomalydetectiondatasetswithinthedomainofservermonitoringare
primarilyusedtomonitortheperformancemetricsofserversystemstopromptlyidentify
performancebottlenecks,systemfailures,orsecurityissues.Forinstance,SMDdataset[105]
gathersavarietyofserverperformanceindicators,suchasCPUusage,memoryconsump-
tion,diskI/O,etc.,foranomalydetectionandperformanceanalysis. Exathlondataset[102]
may collect performance data of servers under high load conditions to detect perfor-
manceanomalies.
Largecompaniesneedtomonitorvariousmetrics(suchaspageviewsandrevenue)of
theirapplicationsandservicesinrealtime. AtMicrosoft,atime-seriesanomalydetection
servicehasbeendevelopedtohelpcustomerscontinuouslymonitortime-seriesdataand
promptlyalertpotentialincidents. Denetal. [122]proposedanovelalgorithmbasedon
SpectralResidualandCNN,whichisthefirstattempttoapplytheSRmodel,originally
fromthevisualsaliencydetectiondomain,totime-seriesanomalydetection. Theapproach
aimstoprovideanaccurate,efficient,andgeneralsolution. Netzeretal. [123]proposeda
segment-basedtimeseriesanomalydetectionmethodformonitoringmachiningprocesses.
Thisapproachdetectsanomaliesbyusingsubprocess-specificthresholds,enablingmore
preciseidentificationandlocalizationofabnormalbehaviorsinthemachiningprocess.
7.10. Infrastructure
Securityisthefoundationofsustainableurbandevelopment.Theprocessofurbancon-
structionandoperationinvolvesalargeamountofmultidimensionaltime-seriesdata. By
detectinganomaliesinMTS,decisionsupportforurbanconstructionandoperationalrisk
warningcanbeprovided. Giventhecomplexityofurbaninfrastructure,thereisanurgent
needforfastandaccurateanomalydetection. Wuetal. [124]proposedareal-timeanomaly
detection algorithm based on an improved distance measure, called RADIM. RADIM
preservestherelationshipsbetweendimensionsinthemultidimensionalsubsequences
andusesanextendedFrobeniusnormwithlocalweightsandEuclideandistancebasedon
multidimensionaldatatomeasurethesimilarityofMTS.Inaddition,athresholdupdate
mechanismbasedonthefirst-ordermeandifference(TMFD)isdesignedtodetectreal-time
anomaliesbyassessingdeviations. Thismethodhasbeenappliedintunnelconstruction.
Atthesametime,mostcurrentmodelsstillfacechallengesinperceivinghigh-frequency
data,andthemostchallengingtaskisprocessinglargevolumesofdatainanextremely
short time. Liu et al. [125] proposed an anomaly detection method for high-frequency
sensordataintrafficinfrastructuremonitoringsystemsbasedonafine-tunedmodel. The
researchersdemonstratedthatconvertingdataintoimagescanimproveanomalydetection
speed,buttrainingdeeplearningmodelsisstilltime-consuming. Therefore,theydesigned
afour-stagemodelandcomparedtheproposedCNNwithfourwidelyusedfine-tuned
CNNsusingconfusionmatricestorapidlydetectanomaliesinhigh-frequencydata.
8. ConclusionsandFutureDirection
Thisarticleprovidesacomprehensivesurveyandreviewofmultivariatetimeseries
anomalydetection,exploringtypesofanomaliesanddeeparchitecturesforanomalydetec-
tion. Itanalyzesandorganizesdeeplearningmodelarchitecturesforanomalydetection
fromthreeperspectives,proposesanewclassificationofanomalydetectionstrategies,and
discusses46deeplearningmodelsindepth. Inaddition,itcompilespublicdatasetsfor
multivariatetimeseriesanomalydetection,alongwiththeirrespectiveapplicationdomains.
Toadvancethefield,thearticleconcludeswithadiscussionofpotentialdirectionsforfuture
researchexploration.

Sensors2025,25,190 21of27
Discrepancy: The contrastive learning has attracted considerable attention across
various domains, as it is capable of training models by contrasting positive pairs with
negativepairs. Recentresearchhasbeenfocusingonhighlightingdiscrepancies[59,62],
andfurtherexplorationinthisdirectionisexpected.
Integrationofdomainknowledge: Integratingexistingknowledgefromthestatistical
domain with deep learning can further enhance the model’s capability for time series
anomalydetection. FCVAE[126]selectsthemostusefulinformationfromthefrequency
domain to achieve better short-term trend construction. Future work could leverage
insightsfromthefrequencydomain,combinedwithdomainknowledge,tostrengthenthe
analysisoftimeseriesdata.
Benchmarking and evaluation metrics: The development and use of diverse pub-
lic datasets that simulate real-world anomaly situations, with clear subset divisions
for training and testing. At the same time, the design of intuitive, interpretable, and
parameter-adjustment-free evaluation metrics to adapt to different types of time series
anomalydetection.
LeveragingtechniquesfromLLMs: Recently,LLMshavegainedpopularityintime
seriesanalysis[127]. LLMsexhibitexceptionalgeneralizationcapabilities,demonstrating
robustpredictiveperformanceevenwithscarcedatasets. Thischaracteristicisparticularly
valuableinthecontextofMTSAD.Byleveragingmultimodalknowledge,suchasincorpo-
ratingadditionaltextualinformationtogeneratemultimodalembeddings,LLMseffectively
bridgethegapbetweennormalandanomalousdatainanomalydetection. Thismodeling
approach enriches the anomaly detection process by providing a more comprehensive
data representation, enabling the inclusion of diverse data sources and fostering more
detailedandcontext-awareanomalydetection. ExploringLLMsinMTSADisapromising
avenuethatcouldsignificantlyenhancetheaccuracyandefficiencyofdetectinganomalies
inmultivariatetimeseriesdata.
AuthorContributions: Writing—–originaldraftpreparation,F.W.;writing–—reviewandediting,
F.W.,Y.J.,R.Z.,A.W.andJ.X.;supervision,X.P.;ProjectAdministration,A.W.;FundingAcquisition,
J.X.Allauthorshavereadandagreedtothepublishedversionofthemanuscript.
Funding: Thisresearchwasfundedbythe2021KeyResearchPlatformsandProjectsofCollegesand
UniversitiesbytheDepartmentofEducationofGuangdongProvince:ResearchontheConstruction
ofKnowledgeGraphModelsforVocationalCollegeArchitecturalEducationSupportedbyArtificial
Intelligence(ProjectNo.:2021ZDZX1112).
InstitutionalReviewBoardStatement:Notapplicable.
InformedConsentStatement:Notapplicable.
DataAvailabilityStatement:Thedatapresentedinthisstudyareavailableonthesourcementioned
inthetext.
ConflictsofInterest:Theauthorsdeclarenoconflictsofinterest.
References
1. Belay,M.A.;Blakseth,S.S.;Rasheed,A.;SalvoRossi,P.UnsupervisedAnomalyDetectionforIoT–BasedMultivariateTimeSeries:
ExistingSolutions,PerformanceAnalysisandFutureDirections.Sensors2023,23,2844.[CrossRef]
2. Correia,L.;Goos,J.C.;Klein,P.;Bäck,T.;Kononova,A.V.Onlinemodel–basedanomalydetectioninmultivariatetimeseries:
Taxonomy,survey,researchchallengesandfuturedirections.Eng.Appl.Artif.Intell.2024,138,109323.[CrossRef]
3. Hilal,W.;Gadsden,S.A.;Yawney,J.Financialfraud:Areviewofanomalydetectiontechniquesandrecentadvances.ExpertSyst.
Appl. 2022,193,116429.[CrossRef]
4. Cook,A.A.;Misirli,G.;Fan,Z.AnomalyDetectionforIoTTime–SeriesData:ASurvey.IEEEInternetThingsJ.2020,7,6481–6494.
[CrossRef]

Sensors2025,25,190 22of27
5. Angiulli,F.;Pizzuti,C.Fastoutlierdetectioninhighdimensionalspaces. InProceedingsofthe6thEuropeanConferenceon
PrinciplesofDataMiningandKnowledgeDiscovery,Berlin/Heidelberg,Germany,19–23August2002;pp.15–27.
6. Schölkopf,B.;Platt,J.C.;Shawe–Taylor,J.Estimatingthesupportofahigh–dimensionaldistribution.NeuralComput.2001,13,
1443–1471.[CrossRef][PubMed]
7. Breunig,M.M.;Kriegel,H.P.;Ng,R.T.;Sander,J.LOF:Identifyingdensity–basedlocaloutliers.InProceedingsofthe2000ACM
SIGMODInternationalConferenceonManagementofData,Dallas,TX,USA,15–18May2000;pp.93–104.
8. Nelson,B.K.Timeseriesanalysisusingautoregressiveintegratedmovingaverage(ARIMA)models.Acad.Emerg.Med.1998,5,
739–744.[CrossRef][PubMed]
9. Ma,J.;Perkins,S.Time–seriesnoveltydetectionusingone–classsupportvectormachines.InProceedingsoftheInternational
JointConferenceonNeuralNetworks,Portland,OR,USA,20–24July2003;Volume3,pp.1741–1745.
10. Tax,D.M.J.;Duin,R.P.W.Supportvectordatadescription.Mach.Learn.2004,54,45–66.[CrossRef]
11. Munir, M.; Chattha, M.A.; Dengel, A.; Ahmed, S.Acomparativeanalysisoftraditionalanddeeplearning–basedanomaly
detectionmethodsforstreamingdata. InProceedingsofthe18thIEEEInternationalConferenceonMachineLearningand
Applications(ICMLA),BocaRaton,FL,USA,16–19December2019;pp.561–566.
12. Vaswani,A.Attentionisallyouneed.InProceedingsofthe31stInternationalConferenceonNeuralInformationProcessing
Systems,LongBeach,CA,USA,4–9December2017.
13. Yang,Y.;Zhang,C.;Zhou,T.;Wen,Q.;Sun,L.Dcdetector: Dualattentioncontrastiverepresentationlearningfortimeseries
anomalydetection.InProceedingsofthe29thACMSIGKDDConferenceonKnowledgeDiscoveryandDataMining,LongBeach,
CA,USA,6–10August2023;pp.3033–3045.
14. Hao, X.; Chen, Y.; Yang, C.; Du, Z.; Ma, C.; Wu, C.; Meng, X. From Chaos to Clarity: Time Series Anomaly Detection in
AstronomicalObservations.arXiv2024,arXiv:2403.10220.
15. Huang,X.;Chen,N.;Deng,Z.;Huang,S.Multivariatetimeseriesanomalydetectionviadynamicgraphattentionnetworkand
Informer.Appl.Intell.2024,54,7636–7658.[CrossRef]
16. Chen,F.;Qin,Z.;Zhou,M.;Zhang,Y.;Deng,S.;Fan,L.;Wen,Q.LARA:ALightandAnti–overfittingRetrainingApproachfor
UnsupervisedTimeSeriesAnomalyDetection.InProceedingsoftheACMonWebConference2024,Singapore,13–17May2024;
pp.4138–4149.
17. Prabhu,H.;Valadi,J.;Arjunan,P.GenerativeAdversarialNetworkwithSoft–DynamicTimeWarpingandParallelReconstruction
forEnergyTimeSeriesAnomalyDetection.arXiv2024,arXiv:2402.14384.
18. Wang,C.;Zhuang,Z.;Qi,Q.;Wang,J.;Wang,X.;Sun,H.;Liao,J.Driftdoesn’tmatter:Dynamicdecompositionwithdiffusion
reconstructionforunstablemultivariatetimeseriesanomalydetection.InProceedingsofthe37thInternationalConferenceon
NeuralInformationProcessingSystems,NewOrleans,LA,USA,10–16December2023;pp.10758–10774.
19. Pang,G.;Shen,C.;Cao,L.;Hengel,A.V.D.Deeplearningforanomalydetection:Areview.ACMComput.Surv. 2021,54,1–38.
[CrossRef]
20. Ma, S.; Guan, S.; He, Z.; Nie, J.; Gao, M. TPAD: Temporal pattern based neural network model for anomaly detection in
multivariatetimeseries.IEEESens.J.2023,23,30668–30682.[CrossRef]
21. ZamanzadehDarban,Z.;Webb,G.I.;Pan,S.;Aggarwal,C.;Salehi,M.Deeplearningfortimeseriesanomalydetection:Asurvey.
ACMComput.Surv. 2024,57,1–42.[CrossRef]
22. Munir,M.;Siddiqui,S.A.;Dengel,A.;Ahmed,S.DeepAnT:Adeeplearningapproachforunsupervisedanomalydetectionin
timeseries.IEEEAccess2018,7,1991–2005.[CrossRef]
23. He,Y.;Zhao,J.Temporalconvolutionalnetworksforanomalydetectionintimeseries. J.Phys. Conf. Ser. 2019,1213,042050.
[CrossRef]
24. Wu,H.;Hu,T.;Liu,Y.;Zhou,H.;Wang,J.;Long,M.Timesnet:Temporal2d–variationmodelingforgeneraltimeseriesanalysis.
InProceedingsoftheEleventhInternationalConferenceonLearningRepresentations,Kigali,Rwanda,1–5May2023.
25. Hundman, K.; Constantinou, V.; Laporte, C.; Colwell, I.; Soderstrom, T. Detecting spacecraft anomalies using lstms and
nonparametric dynamic thresholding. In Proceedings of the 24th ACM SIGKDD International Conference on Knowledge
DiscoveryandDataMining,KDD’18,London,UK,19–23August2018;pp.387–395.
26. Ding,N.;Ma,H.;Gao,H.;Ma,Y.;Tan,G.Real–timeanomalydetectionbasedonlongshort–TermmemoryandGaussianMixture
Model.Comput.Electr.Eng.2019,79,106458.[CrossRef]
27. Shen,L.;Li,Z.;Kwok,J.Timeseriesanomalydetectionusingtemporalhierarchicalone–classnetwork.InProceedingsofthe34th
InternationalConferenceonNeuralInformationProcessingSystems,Vancouver,BC,Canada,6–12December2020;Volume33,
pp.13016–13026.
28. Wu,W.;He,L.;Lin,W.;Su,Y.;Cui,Y.;Maple,C.;Jarvis,S.Developinganunsupervisedreal–timeanomalydetectionschemefor
timeserieswithmulti–seasonality.IEEETrans.Knowl.DataEng.2020,34,4147–4160.[CrossRef]

Sensors2025,25,190 23of27
29. Zhao,H.;Wang,Y.;Duan,J.;Huang,C.;Cao,D.;Tong,Y.;Xu,B.;Bai,J.;Tong,J.;Zhang,Q.Multivariatetime–seriesanomaly
detectionviagraphattentionnetwork.InProceedingsoftheIEEEInternationalConferenceonDataMining,ICDM,Sorrento,
Italy,17–20November2020;pp.841–850.
30. Deng,A.;Hooi,B.GraphNeuralNetwork–BasedAnomalyDetectioninMultivariateTimeSeries.Proc.AAAIConf.Artif.Intell.
2021,35,4027–4035.[CrossRef]
31. Chen,W.;Tian,L.;Chen,B.;Dai,L.;Duan,Z.;Zhou,M.Deepvariationalgraphconvolutionalrecurrentnetworkformultivariate
timeseriesanomalydetection.InProceedingsofthe39thInternationalConferenceonMachineLearning,Baltimore,MD,USA,
17–23July2022;pp.3621–3633.
32. Han,S.;Woo,S.S.Learningsparselatentgraphrepresentationsforanomalydetectioninmultivariatetimeseries.InProceedings
ofthe28thACMSIGKDDConferenceonKnowledgeDiscoveryandDataMining,Washington,DC,USA,14–18August2022;
pp.2977–2986.
33. Chen, K.; Feng, M.; Wirjanto, T.S. Multivariate time series anomaly detection via dynamic graph forecasting. arXiv 2023,
arXiv:2302.02051.
34. Fu, Y.; Xue, F. Mad: Self–supervised masked anomaly detection task for multivariate time series. In Proceedings of the
InternationalJointConferenceonNeuralNetworks,IJCNN,Padua,Italy,18–23July2022;pp.1–8.
35. Wu,Y.;Dong,Y.;Zhu,W.;Zhang,J.;Liu,S.;Lu,D.;Li,Y.CLformer:Constraint–basedLocalityenhancedTransformerforanomaly
detectionofancientbuildingstructures.Eng.Appl.Artif.Intell.2023,126,107072.[CrossRef]
36. Jeong,Y.;Yang,E.;Ryu,J.H.;Park,I.;Kang,M.Anomalybert: Self–supervisedtransformerfortimeseriesanomalydetection
usingdatadegradationscheme.arXiv2023,arXiv:2305.04468.
37. Zong,B.;Song,Q.;RenqiangMin,M.;Cheng,W.;Lumezanu,C.;Cho,D.;Chen,H.Deepautoencodinggaussianmixturemodel
forunsupervisedanomalydetection.InProceedingsoftheInternationalConferenceonLearningRepresentations,Vancouver,
BC,Canada,30April–3May2018.
38. Zhang,C.;Song,D.;Chen,Y.;Feng,X.;Lumezanu,C.;Cheng,W.;Chawla,N.V.Adeepneuralnetworkforunsupervisedanomaly
detectionanddiagnosisinmultivariatetimeseriesdata. InProceedingsoftheAAAIConferenceonArtificialIntelligence,
Honolulu,HI,USA,27January–1February2019;Volume33,pp.1409–1416.
39. Audibert,J.;Michiardi,P.;Guyard,F.;Marti,S.;Zuluaga,M.A.Usad: Unsupervisedanomalydetectiononmultivariatetime
series.InProceedingsofthe26thACMSIGKDDInternationalConferenceonKnowledgeDiscoveryandDataMining,Virtual
Event,CA,USA,23–27August2020;pp.3395–3404.
40. Lai, C.Y.A.; Sun, F.K.; Gao, Z.; Lang, J.H.; Boning, D. Nominality score conditioned time series anomaly detection by
point/sequentialreconstruction.InProceedingsofthe37thConferenceonNeuralInformationProcessingSystems,NewOrleans,
LA,USA,10–16December2023;pp.76637–76655.
41. Park,D.;Hoshi,Y.;Kemp,C.C.Amultimodalanomalydetectorforrobot–assistedfeedingusinganlstm–basedvariational
autoencoder.IEEERobot.Autom.Lett.2018,3,1544–1551.[CrossRef]
42. Su, Y.; Zhao, Y.; Niu, C.; Liu, R.; Sun, W.; Pei, D.Robustanomalydetectionformultivariatetimeseriesthroughstochastic
recurrentneuralnetwork.InProceedingsofthe25thACMSIGKDDInternationalConferenceonKnowledgeDiscoveryandData
Mining,Anchorage,AK,USA,4–8August2019;pp.2828–2837.
43. Li,Z.;Zhao,Y.;Han,J.;Su,Y.;Jiao,R.;Wen,X.;Pei,D.Multivariatetimeseriesanomalydetectionandinterpretationusing
hierarchicalinter–metricandtemporalembedding.InProceedingsoftheACMSIGKDDInternationalConferenceonKnowledge
DiscoveryandDataMining,VirtualEvent,Singapore,14–18August2021;pp.3220–3230.
44. Huang,T.;Chen,P.;Li,R.Asemi–supervisedvaebasedactiveanomalydetectionframeworkinmultivariatetimeseriesforonline
systems.InProceedingsoftheACMWebConference,WWW’22,VirtualEvent,Lyon,France,25–29April2022;pp.1797–1806.
45. Li,D.;Chen,D.;Jin,B.;Shi,L.;Goh,J.;Ng,S.K.MAD–GAN:Multivariateanomalydetectionfortimeseriesdatawithgenerative
adversarialnetworks.Int.Conf.Artif.NeuralNetw.2019,11730,703–716.
46. Geiger,A.;Liu,D.;Alnegheimish,S.;Cuesta–Infante,A.;Veeramachaneni,K.Tadgan: Timeseriesanomalydetectionusing
generativeadversarialnetworks. InProceedingsoftheIEEEInternationalConferenceonDataMining, Atlanta, GA,USA,
10–13December2020;pp.33–43.
47. Lu, S.; Dong, Z.; Cai, D.; Fang, F.; Zhao, D. MIM–GAN–based Anomaly Detection for Multivariate Time Series Data. In
ProceedingsoftheIEEEVehicularTechnologyConference(VTC2023–Fall),HongKong,China,10–13October2023;pp.1–7.
48. Chen,X.;Deng,L.;Zhao,Y.;Zheng,K.Adversarialautoencoderforunsupervisedtimeseriesanomalydetectionandinterpretation.
InProceedingsofthe16thACMInternationalConferenceonWebSearchandDataMining,Singapore,27February–3March2023;
pp.267–275.
49. Pintilie,I.;Manolache,A.;Brad,F.Timeseriesanomalydetectionusingdiffusion–basedmodels. InProceedingsoftheIEEE
InternationalConferenceonDataMining,Shanghai,China,1–4December2023;pp.570–578.

Sensors2025,25,190 24of27
50. Zhang,H.; Xia,Y.; Yan,T.; Liu,G.Unsupervisedanomalydetectioninmultivariatetimeseriesthroughtransformer–based
variational autoencoder. In Proceedings of the 33rd Chinese Control and Decision Conference (CCDC), Kunming, China,
22–24May2021;pp.281–286.
51. Xu,J.Anomalytransformer:Timeseriesanomalydetectionwithassociationdiscrepancy.InProceedingsoftheInternational
ConferenceonLearningRepresentations,VirtualEvent,25–29April2022.
52. Tuli,S.;Casale,G.;Jennings,N.R.Tranad:Deeptransformernetworksforanomalydetectioninmultivariatetimeseriesdata.
Proc.VLDBEndow.2022,15,1201–1214.[CrossRef]
53. Song, J.; Kim, K.; Oh, J.; Cho, S. Memto: Memory–guided transformer for multivariate time series anomaly detection.
In Proceedings of the 37th International Conference on Neural Information Processing Systems, New Orleans, LA, USA,
10–16December2023;Volume36,pp.57947–57963.
54. Nam,Y.; Yoon,S.; Shin,Y.; Bae,M.; Song,H.; Lee,J.G.; Lee,B.S.BreakingtheTime–FrequencyGranularityDiscrepancyin
Time–SeriesAnomalyDetection.InProceedingsoftheACMonWebConference2024,WWW’24,Singapore,13–17May2024;
pp.4204–4215.
55. Wu,X.;Qiu,X.;Li,Z.;Wang,Y.;Hu,J.;Guo,C.;Yang,B.CATCH:Channel–AwareMultivariateTimeSeriesAnomalyDetection
viaFrequencyPatching.arXiv2024,arXiv:2410.12261.
56. Liu,S.;Yao,D.;Fang,L.;Li,Z.;Li,W.;Feng,K.;Bi,J.AnomalyLLM:Few–ShotAnomalyEdgeDetectionforDynamicGraphs
usingLargeLanguageModels.arXiv2024,arXiv:2405.07626.
57. Bian,Y.;Ju,X.;Li,J.;Xu,Z.;Cheng,D.;Xu,Q.Multi–patchprediction: Adaptingllmsfortimeseriesrepresentationlearning.
In Proceedings of the 41st International Conference on Machine Learning, Vienna, Austria, 21–27 July 2024; Volume 235,
pp.3889–3912.
58. Liu,C.;He,S.;Zhou,Q.;Li,S.;Meng,W.Largelanguagemodelguidedknowledgedistillationfortimeseriesanomalydetection.
InProceedingsoftheThirty–ThirdInternationalJointConferenceonArtificialIntelligence(IJCAI–24),Jeju,RepublicofKorea,
3–9August2024;pp.2162–2170.
59. Zhong,Z.;Yu,Z.;Yang,Y.;Wang,W.;Yang,K.PatchAD:Patch–BasedMLP–MixerforTimeSeriesAnomalyDetection.arXiv
2024,arXiv:2401.09793.
60. Pranavan,T.;Sim,T.;Ambikapathi,A.;Ramasamy,S.Contrastivepredictivecodingforanomalydetectioninmulti–variatetime
seriesdata.arXiv2022,arXiv:2202.03639.
61. Najari,N.;Berlemont,S.;Lefebvre,G.;Duffner,S.;Garcia,C.RESIST:Robusttransformerforunsupervisedtimeseriesanomaly
detection.InProceedingsoftheAdvancedAnalyticsandLearningonTemporalData:7thECMLPKDDWorkshop,Grenoble,
France,19–23September2022;pp.66–82.
62. Zhong,Z.;Yu,Z.;Xi,X.;Xu,Y.;Chen,J.;Yang,K.SimAD:ASimpleDissimilarity–BasedApproachforTimeSeriesAnomaly
Detection.arXiv2024,arXiv:2405.11238.
63. Ghorbani,R.;Reinders,M.J.;Tax,D.M.RESTAD:REconstructionandSimilaritybasedTransformerfortimeseriesAnomaly
Detection.arXiv2024,arXiv:2405.07509.
64. Hochreiter,S.;Schmidhuber,J.LongShort–TermMemory.NeuralComput.1997,9,1735–1780.[CrossRef][PubMed]
65. Reynolds,D.A.Gaussianmixturemodels.Encycl.Biom. 2009,741,659–663.
66. Orhan,A.E.;Pitkow,X.Skipconnectionseliminatesingularities.arXiv2017,arXiv:1701.09175.
67. Velickovic,P.;Cucurull,G.;Casanova,A.;Romero,A.;Lio,P.;Bengio,Y.Graphattentionnetworks.arXiv2017, arXiv:1710.10903.
68. Bank,D.;Koenigstein,N.;Giryes,R.Autoencoders.InMachineLearningforDataScienceHandbook:DataMiningandKnowledge
DiscoveryHandbook;Springer:Cham,Switzerland,2023;pp.353–374.
69. Doersch,C.Tutorialonvariationalautoencoders.arXiv2016,arXiv:1606.05908.
70. Goodfellow,I.;Pouget–Abadie,J.;Mirza,M.;Xu,B.;Warde–Farley,D.;Ozair,S.;Bengio,Y.Generativeadversarialnetworks.
Commun.ACM2020,63,139–144.[CrossRef]
71. Frogner, C.; Zhang, C.; Mobahi, H.; Araya, M.; Poggio, T.A. Learning with a Wasserstein loss. In Proceedings of the 28th
InternationalConferenceonNeuralInformationProcessingSystems,Montreal,QC,Canada,7–12December2015;Volume2,
pp.2053–2061.
72. Dwibedi,D.;Aytar,Y.;Tompson,J.;Sermanet,P.;Zisserman,A.Temporalcycle–consistencylearning. InProceedingsofthe
IEEE/CVFConferenceonConferenceonComputerVisionandPatternRecognition(CVPR),LongBeach,CA,USA,15–20June
2019;pp.1801–1810.
73. Cuturi, M.; Blondel, M. Soft–dtw: A differentiable loss function for time–series. In Proceedings of the 34th International
ConferenceonMachineLearning,Sydney,Australia,6–11August2017;pp.894–903.
74. MacKay,D.J.IntroductiontoGaussianprocesses.NATOASISer.FComput.Syst.Sci. 1998,168,133–166.

Sensors2025,25,190 25of27
75. Yoon,J.;Zame,W.R.;vanderSchaar,M.Estimatingmissingdataintemporaldatastreamsusingmulti–directionalrecurrent
neuralnetworks.IEEETrans.Biomed.Eng.2018,66,1477–1490.[CrossRef]
76. Dong,M.;Huang,H.;Cao,L.CanLLMsServeAsTimeSeriesAnomalyDetectors?arXiv2024,arXiv:2408.03475.
77. Alnegheimish,S.;Nguyen,L.;Berti–Equille,L.;Veeramachaneni,K.Largelanguagemodelscanbezero–shotanomalydetectors
fortimeseries?arXiv2024,arXiv:2405.14755.
78. Zhong,S.;Song,S.;Zhuo,W.;Li,G.;Liu,Y.;Chan,S.H.G.Amulti–scaledecompositionmlp–mixerfortimeseriesanalysis.arXiv
2023,arXiv:2310.11959.[CrossRef]
79. Gong, Z.; Tang, Y.; Liang, J. Patchmixer: A patch–mixing architecture for long–term time series forecasting. arXiv 2023,
arXiv:2310.00655.
80. Ekambaram,V.;Jati,A.;Nguyen,N.;Sinthong,P.;Kalagnanam,J.Tsmixer:Lightweightmlp–mixermodelformultivariatetime
seriesforecasting.InProceedingsofthe29thACMSIGKDDConferenceonKnowledgeDiscoveryandDataMining,LongBeach,
CA,USA,6–10August2023;pp.459–469.
81. Ferrell,B.;Santuro,S.NASAShuttleValveData;FloridaTech:Melbourne,FL,USA,2005.
82. Asuncion,A.;Newman,D.UCIMachineLearningRepository.2007.Availableonline:https://ergodicity.net/2013/07/(accessed
on8November2024).
83. Angryk,R.A.;Martens,P.C.;Aydin,B.;Kempton,D.;Mahajan,S.S.;Basodi,S.;Georgoulis,M.K.Multivariatetimeseriesdataset
forspaceweatherdataanalytics.Sci.Data2020,7,227.[CrossRef]
84. Moritz,S.;Rehbach,F.;Chandrasekaran,S.;Rebolledo,M.;Bartz–Beielstein,T.GECCOIndustrialChallenge2018Dataset:Awater
qualitydatasetforthe‘InternetofThings:OnlineAnomalyDetectionforDrinkingWaterQuality’Competition.InProceedingsof
theGeneticandEvolutionaryComputationConference,Kyoto,Japan,15–19July2018.
85. Poorebrahimi,A.CICIDS2017.J.Adv.SignalProcess.2021,5,105–115.
86. KDDCup.TheThirdInternationalKnowledgeDiscoveryandDataMiningToolsCompetitionDatasetKDDCup1999Data.1999.
Availableonline:https://kdd.ics.uci.edu/databases/kddcup99/kddcup99.html(accessedon24December2024).
87. Ahmad,S.;Lavin,A.;Purdy,S.;Agha,Z.Unsupervisedreal–timeanomalydetectionforstreamingdata.Neurocomputing2017,
262,134–147.[CrossRef]
88. DalPozzolo,A.;Caelen,O.;Johnson,R.A.;Bontempi,G.Calibratingprobabilitywithundersamplingforunbalancedclassification.
InProceedingsoftheIEEESymposiumSeriesonComputationalIntelligence,CapeTown,SouthAfrica,7–10December2015;
pp.159–166.
89. vonBirgelen,A.;Niggemann,O.Anomalydetectionandlocalizationforcyber–physicalproductionsystemswithself–organizing
maps.Improve2018,8,55–71.
90. Filonov,P.;Lavrentyev,A.;Vorontsov,A.Multivariateindustrialtimeserieswithcyber–attacksimulation:Faultdetectionusing
anlstm–basedpredictivedatamodel.arXiv2016, arXiv:1612.06676.
91. Aditya,P.M.;Nils,O.T.SWaT:AwatertreatmenttestbedforresearchandtrainingonICSsecurity.InProceedingsofthe2016
InternationalWorkshoponCyber–PhysicalSystemsforSmartWaterNetworks(CySWater),Vienna,Austria,11April2016;
pp.31–36.
92. Goh,J.;Adepu,S.;Junejo,K.N.;Mathur,A.Adatasettosupportresearchinthedesignofsecurewatertreatmentsystems.Crit.
Inf.Infrastruct.Secur.2017,10242,88–99.
93. Ahmed,C.M.;Palleti,V.R.;Mathur,A.P.WADI:Awaterdistributiontestbedforresearchinthedesignofsecurecyberphysical
systems.InProceedingsofthe3rdInternationalWorkshoponCyber–PhysicalSystemsforSmartWaterNetworks,Pittsburgh,
PA,USA,21April2017;pp.25–28.
94. Nedelkoski, S.; Bogatinovski, J.; Mandapati, A.K.; Becker, S.; Cardoso, J.; Kao, O.Multi–sourcedistributedsystemdatafor
ai–poweredanalytics.InProceedingsoftheService–OrientedandCloudComputing:8thIFIPWG2.14EuropeanConference,
ESOCC2020,Heraklion,Greece,28–30September2020;pp.161–176.
95. Moody,G.B.;Mark,R.G.TheimpactoftheMIT–BIHarrhythmiadatabase.IEEEEng.Med.Biol.Mag.2001,20,45–50.[CrossRef]
96. Goldberger,A.L.;Amaral,L.A.N.;Glass,L.;Hausdorff,J.M.;Ivanov,P.C.;Mark,R.G.;PhysioBank,P.PhysioNet:Componentsof
aNewResearchResourceforComplexPhysiologicSignals.Circulation2000,101,215–220.[CrossRef]
97. Vanderpump,M.P.Theepidemiologyofthyroiddisease.Br.Med.Bull.2011,99,39–51.[CrossRef]
98. Greenwald,S.D.;Patil,R.S.;Mark,R.G.Improveddetectionandclassificationofarrhythmiasinnoise–corruptedelectrocardiograms
usingcontextualinformation.InProceedingsoftheComputersinCardiology,Chicago,IL,USA,23–26September1990;pp.461–464.
99. Bachlin,M.;Plotnik,M.;Roggen,D.;Maidan,I.;Hausdorff,J.M.;Giladi,N.;Troster,G.WearableassistantforParkinson’sdisease
patientswiththefreezingofgaitsymptom.IEEETrans.Inf.Technol.Biomed.2009,14,436–446.[CrossRef]
100. Ihler,A.;Hutchins,J.;Smyth,P.Adaptiveeventdetectionwithtime–varyingpoissonprocesses. InProceedingsofthe12thACM
SIGKDDInternationalConferenceonKnowledgeDiscoveryandDataMining,Philadelphia,PA,USA,20–23August2006;pp.207–216.

Sensors2025,25,190 26of27
101. Daus,M.W.Taxis.InTheRoutledgeHandbookofPublicTransport;Routledge:London,UK,2021;pp.252–269.
102. Jacob,V.;Song,F.;Stiegler,A.;Rad,B.;Diao,Y.;Tatbul,N.Exathlon:Abenchmarkforexplainableanomalydetectionovertime
series.arXiv2020,arXiv:2010.05073.[CrossRef]
103. He,Z.;Chen,P.;Li,X.;Wang,Y.;Yu,G.;Chen,C.;Zheng,Z.Aspatiotemporaldeeplearningapproachforunsupervisedanomaly
detectionincloudsystems.IEEETrans.NeuralNetw.Learn.Syst.2020,34,1705–1719.[CrossRef]
104. Abdulaal, A.; Liu, Z.; Lancewicki, T. Practical approach to asynchronous multivariate time series anomaly detection and
localization.InProceedingsofthe27thACMSIGKDDConferenceonKnowledgeDiscoveryandDataMining,VirtualEvent,
Singapore,14–18August2021;pp.2485–2494.
105. Li,Z.;Chen,W.;Pei,D.RobustandunsupervisedKPIanomalydetectionbasedonconditionalvariationalautoencoder. In
Proceedingsofthe2018IEEE37thInternationalPerformanceComputingandCommunicationsConference(IPCCC),Orlando,
FL,USA,17–19November2018;pp.1–9.
106. Muthukrishna,D.;Gupta,R.AClassifier–BasedApproachtoMulti–ClassAnomalyDetectionAppliedtoAstronomicalTime–
Series.arXiv2024,arXiv:2408.08888.
107. Scargle,J.D.Studiesinastronomicaltimeseriesanalysis.Astrophys.J.1982,263,835–853.[CrossRef]
108. Baireddy, S.; Desai, S.R.; Mathieson, J.L.; Foster, R.H.; Chan, M.W.; Comer, M.L.; Delp, E.J.Spacecrafttime–seriesanomaly
detectionusingtransferlearning. InProceedingsoftheIEEE/CVFConferenceonComputerVisionandPatternRecognition
(CVPR),Nashville,TN,USA,20–25June2021;pp.1951–1960.
109. El–Shafeiy,E.;Alsabaan,M.;Ibrahem,M.I.;Elwahsh,H.Real–timeanomalydetectionforwaterqualitysensormonitoringbased
onmultivariatedeeplearningtechnique.Sensors2023,23,8613.[CrossRef][PubMed]
110. Chevrot, A.; Vernotte, A.; Legeard, B.CAE:Contextualauto–encoderformultivariatetime–seriesanomalydetectioninair
transportation.Comput.Secur. 2022,116,102652.[CrossRef]
111. Rollo, F.; Bachechi, C.; Po, L.Anomalydetectionandrepairingforimprovingairqualitymonitoring. Sensors2023, 23, 640.
[CrossRef]
112. Sgueglia, A.; DiSorbo, A.; Visaggio, C.A.; Canfora, G.AsystematicliteraturereviewofIoTtimeseriesanomalydetection
solutions.FutureGener.Comput.Syst.2022,134,170–186.[CrossRef]
113. Liu,Y.;Garg,S.;Nie,J.;Zhang,Y.;Xiong,Z.;Kang,J.;Hossain,M.S.Deepanomalydetectionfortime–seriesdatainindustrialIoT:
Acommunication–efficienton–devicefederatedlearningapproach.IEEEInternetThingsJ.2020,8,6348–6358.[CrossRef]
114. Nizam,H.;Zafar,S.;Lv,Z.;Wang,F.;Hu,X.Real–timedeepanomalydetectionframeworkformultivariatetime–seriesdatain
industrialiot.IEEESens.J.2022,22,22836–22849.[CrossRef]
115. Crépey,S.;Lehdili,N.;Madhar,N.;Thomas,M.Anomalydetectioninfinancialtimeseriesbyprincipalcomponentanalysisand
neuralnetworks.Algorithms2022,15,385.[CrossRef]
116. Nam,Y.;Trirat,P.;Kim,T.;Lee,Y.;Lee,J.G.Context–awaredeeptime–seriesdecompositionforanomalydetectioninbusinesses.
InProceedingsoftheJointEuropeanConferenceonMachineLearningandKnowledgeDiscoveryinDatabases,Turin,Italy,
18–22September2023;pp.330–345.
117. Zelichenok,I.;Kotenko,I.KitsuneDatasetAnalysisviaBigDataandDeepLearningTechniques.InProceedingsofthe2024IEEE
Ural–SiberianConferenceonBiomedicalEngineering,RadioelectronicsandInformationTechnology(USBEREIT),Yekaterinburg,
Russia,13–15May2024;pp.152–155.
118. Kravchik,M.;Shabtai,A.Efficientcyberattackdetectioninindustrialcontrolsystemsusinglightweightneuralnetworksandpca.
IEEETrans.DependableSecur.Comput.2021,19,2179–2197.[CrossRef]
119. Hoang, N.X.; Hoang, N.V.; Du, N.H.; Huong, T.T.; Tran, K.P. Explainable anomaly detection for industrial control system
cybersecurity.IFAC–PapersOnLine2022,55,1183–1188.
120. Sivapalan,G.;Nundy,K.K.;Dev,S.;Cardiff,B.;John,D.ANNet:AlightweightneuralnetworkforECGanomalydetectioninIoT
edgesensors.IEEETrans.Biomed.CircuitsSyst.2022,16,24–35.[CrossRef]
121. Alamr,A.;Artoli,A.Unsupervisedtransformer–basedanomalydetectioninECGsignals.Algorithms2023,16,152.[CrossRef]
122. Ren, H.; Xu, B.; Wang, Y.; Yi, C.; Huang, C.; Kou, X.; Zhang, Q. Time–series anomaly detection service at microsoft. In
Proceedingsofthe25thACMSIGKDDInternationalConferenceonKnowledgeDiscoveryandDataMining,Anchorage,AK,
USA,4–8August2019;pp.3009–3017.
123. Netzer, M.; Palenga, Y.; Fleischer, J. Machine tool process monitoring by segmented timeseries anomaly detection using
subprocess–specificthresholds.Prod.Eng. 2022,16,597–606.[CrossRef]
124. Wu,B.;Zhang,F.;Wang,Y.;Hu,M.;Bai,X.AnomalyDetectionAlgorithmforUrbanInfrastructureConstructionEquipment
BasedonMultidimensionalTimeSeries.Sustainability2024,16,3335.[CrossRef]
125. Liu,H.;Li,L.Anomalydetectionofhigh–frequencysensingdataintransportationinfrastructuremonitoringsystembasedon
fine–tunedmodel.IEEESens.J.2023,23,8630–8638.[CrossRef]

Sensors2025,25,190 27of27
126. Wang,Z.;Pei,C.;Ma,M.;Wang,X.;Li,Z.;Pei,D.;Xie,G.RevisitingVAEforUnsupervisedTimeSeriesAnomalyDetection:A
FrequencyPerspective.InProceedingsoftheACMonWebConference2024,Singapore,13–17May2024;pp.3096–3105.
127. Gao,S.;Koker,T.;Queen,O.;Hartvigsen,T.;Tsiligkaridis,T.;Zitnik,M.Units:Buildingaunifiedtimeseriesmodel.arXiv2024,
arXiv:2403.00131.
Disclaimer/Publisher’sNote: Thestatements, opinionsanddatacontainedinallpublicationsaresolelythoseoftheindividual
author(s)andcontributor(s)andnotofMDPIand/ortheeditor(s).MDPIand/ortheeditor(s)disclaimresponsibilityforanyinjuryto
peopleorpropertyresultingfromanyideas,methods,instructionsorproductsreferredtointhecontent.