---
conversion_metadata:
  converted_at: "2026-07-22T12:41:49Z"
  converter_tool: "markitdown"
  converter_version: "0.1.6"
  source_pdf: "Casolaro et al.pdf"
  source_pdf_sha256: "478c46de437da32d653b0c79b827bd1fb09cab9bf6139e23c761f3fc1a3f40c5"
  page_count: 35
  markdown_char_count: 269466
---

<!-- PAGE-AWARE EXTRACTION (via pdfminer.six) -->

<!-- PAGE 1 -->

Review
Deep Learning for Time Series Forecasting: Advances
and Open Problems

Angelo Casolaro †

, Vincenzo Capone †

, Gennaro Iannuzzo †

and Francesco Camastra *,†

Department of Science and Technology, Parthenope University of Naples, Centro Direzionale Isola C4,
80143 Naples, Italy; angelo.casolaro001@studenti.uniparthenope.it (A.C.);
vincenzo.capone002@studenti.uniparthenope.it (V.C.); gennaro.iannuzzo001@studenti.uniparthenope.it (G.I.)
* Correspondence: francesco.camastra@uniparthenope.it
† These authors contributed equally to this work.

Abstract: A time series is a sequence of time-ordered data, and it is generally used to describe how
a phenomenon evolves over time. Time series forecasting, estimating future values of time series,
allows the implementation of decision-making strategies. Deep learning, the currently leading ﬁeld
of machine learning, applied to time series forecasting can cope with complex and high-dimensional
time series that cannot be usually handled by other machine learning techniques. The aim of the
work is to provide a review of state-of-the-art deep learning architectures for time series forecasting,
underline recent advances and open problems, and also pay attention to benchmark data sets.
Moreover, the work presents a clear distinction between deep learning architectures that are suitable
for short-term and long-term forecasting. With respect to existing literature, the major advantage
of the work consists in describing the most recent architectures for time series forecasting, such as
Graph Neural Networks, Deep Gaussian Processes, Generative Adversarial Networks, Diffusion
Models, and Transformers.

Keywords: short-term forecasting; long-term forecasting; recurrent neural networks; temporal
convolutional neural networks; graph neural networks; deep gaussian processes; transformers; time
series benchmarking; generative adversarial networks; diffusion models

Citation: Casolaro, A.; Capone, V.;

Iannuzzo, G.; Camastra, F. Deep

Learning for Time Series Forecasting:

Advances and Open Problems.

Information 2023, 14, 598. https://

doi.org/10.3390/info14110598

Academic Editor: Nikos E.

Mastorakis

Received: 26 September 2023

Revised: 18 October 2023

Accepted: 2 November 2023

Published: 4 November 2023

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

A time series is a sequence of data enumerated in time order. Time series are used
to study how certain measures, e.g., air pollution data [1], ozone concentration [2], plant
growth [3], sunspots [4], Dow Jones and Nasdaq indices [5], and electricity consumption [6],
evolve over time. Time series forecasting estimates values that a time series takes in the
future, allowing the implementation of decision-making strategies, e.g., abandonment of
fossil fuels to reduce the surface temperature of the Earth. Speciﬁcally, time series fore-
casting is very relevant for the energy domain (e.g., electricity load demand [7,8], solar and
wind power estimation [9,10]), meteorology (e.g., prediction of wind speed [11], tempera-
ture [12,13], humidity [12], precipitation [13,14]), air pollution monitoring (e.g., prediction
of PM2.5, PM10, NO2, O3, SO2, and CO2 concentrations [12,15,16]), the ﬁnance domain
(e.g., stock market index and shares prediction [17,18], the stock price [19,20], exchange
rate [21,22]), health (e.g., prediction of infective diseases diffusion [23], diabetes mellitus [24],
blood glucose concentration [25], and cancer growth [26]), trafﬁc (e.g., trafﬁc speed and ﬂow
prediction [27–30]), and industrial production (e.g., petroleum production [31], remaining life
prediction [23,32,33], industrial processes [34], fuel cells durability [35], engine faults [36]).
Deep learning algorithms are currently the leading methods in machine learning due to
their successful application to many computer science domains (e.g., computer vision, natural
language processing, speech recognition). In recent years, there has been a growth of interest in
the application of deep learning to time series forecasting, due to deep learning’s capability
to grasp the nonlinear relations among input data (i.e., time series samples). To the best

Information 2023, 14, 598. https://doi.org/10.3390/info14110598

https://www.mdpi.com/journal/information

---

<!-- PAGE 2 -->

Information 2023, 14, 598

2 of 35

of our knowledge, there are several reviews on deep learning for time series forecasting
(e.g., [37–43]), but they have the following major shortcomings: they lack a description of
Transformer and its variants; they do not provide a clear distinction between models for
short-term and long-term forecasting, there are no sections on short-term and long-term
forecasting benchmarks; they do not cover the most recent deep learning strategies for
short-term forecasting (e.g., Graph Neural Networks, Deep Gaussian Processes, Generative
Adversarial Networks, and Diffusion Models). The aim of this work is to provide a comprehen-
sive survey of recent deep learning approaches for time series forecasting, underlining the
advances and the open problems for each reviewed deep learning architecture. Speciﬁcally,
the survey focuses on works about machine learning applied to time series forecasting that
are not older than 2016, for the sake of length. The paper is organised in the following
sections: in Section 2, the foundations of deterministic time series are introduced; Section 3
describes deep learning architectures for short-term forecasting, i.e., Convolutional Neural
Networks, Temporal Convolutional Networks, Recurrent Neural Networks (RNNs), Graph Neural
Networks, Deep Gaussian Processes, Generative Adversarial Networks, and Diffusion Models;
Section 4 discusses long-term forecasting architectures, i.e., the Transformer architecture
and its time series-based variants; Section 5 reviews other heterogeneous architectures for
both short-term and long-term forecasting; benchmarking for short-term and long-term
time series forecasting is presented in Section 6; in Section 7, some conclusions are drawn
and future possible developments are discussed; ﬁnally, in the appendix are reported the
main mathematical notation used in the work and a description of the main diffusion
model foundations.

2. Deterministic Time Series

A time series is called a univariate time series if all its samples are scalar; otherwise, if all
samples are vectors, it is called a multivariate time series. A time series is deﬁned as stationary
when the dynamical process that generated it does not change over time, otherwise, it is
non-stationary. A deterministic stationary time series xt, with t = 1, . . . , L, can be described by
an autoregressive model as follows:

xt+p = f (xt−1, . . . , xt−q) + (cid:101)t+p

∀p ∈ [0, P]

(1)

where f (·) and q are called skeleton and model order of time series, i.e., how many past
samples are required to model the time series adequately, respectively, and (cid:101)t+p represents
an indeterminable part originated either from unmodeled dynamics of the process or from
real noise. P deﬁnes the prediction length, i.e., how many future samples should be predicted.
Figure 1 gives a graphical representation of an autoregressive model.

Figure 1. An example of an autoregressive model for forecasting based on deterministic stationary
time series. In the ﬁgure, the model order is q = 2 and the prediction length is P = 0 (i.e., it is a
one-step ahead forecasting problem).

---

<!-- PAGE 3 -->

Information 2023, 14, 598

3 of 35

If P = 0, the autoregressive model deﬁnes the so-called one-step ahead forecasting, other-
wise, a prediction length P > 0 speciﬁes a multi-step ahead forecasting problem. Moreover,
multi-step ahead forecasting can be further divided into short-term and long-term forecasting.
In the literature, the typical threshold value of prediction length P between short-term and
long-term forecasting ranges between 2 and 48 [44]. Finally, for the sake of clarity, in this
work, one-step ahead forecasting is included in short-term forecasting.

3. Deep Learning Models for Short-Term Forecasting

In short-term forecasting, the skeleton of time series can be approximated by the
following deep learning models, which are described below. The section is organised as
follows. Firstly, Convolutional Neural Networks (Section 3.1), and Temporal Convolutional
Networks (Section 3.1.2) are introduced. Furthermore, Recurrent Neural Networks (Section 3.2)
are described, including Elman RNNs (Section 3.2.1), Echo State Networks (Section 3.2.3), Long
Short-Term Memory (Section 3.2.4), and Gated Recurrent Units (Section 3.2.5). Successively,
hybrids and variants (Section 3.3) of the aforementioned architectures are brieﬂy reviewed.
Moreover, Graph Neural Networks (Section 3.4), Deep Gaussian Processes (Section 3.5), and
generative models (Section 3.6), i.e., Generative Adversarial Networks (Section 3.6.1) and
Diffusion Models (Section 3.6.3), are discussed. Finally, for each reviewed model, drawbacks
and limitations are discussed in proper sections.

3.1. Convolutional Neural Networks

Convolutional Neural Networks (CNNs) [45], as shown in Figure 2, have a deep archi-
tecture generally formed by convolution, pooling, and fully connected layers. CNNs have
three main peculiarities: local connectivity, shared weights and translation equivariance. Local
connectivity resides in each CNN neuron being connected only to its exclusive input region,
the so-called receptive ﬁeld. Besides, the neurons of a given layer share the same weight
matrix. Translation equivariance is the ability of CNNs to detect certain patterns, regardless
of the position they have in the input image. 1D convolution (see Figure 3) of an input
sequence X = [x1, . . . , xL] with a given kernel w with size q is deﬁned as:

y(t) = (w ∗ X )(t) =

q/2
∑
a=−q/2

w(a)X (t − a)

∀t ∈ [1, . . . , L]

(2)

It is worthwhile to remark that in the autoregressive approach, the kernel size q corresponds
to the model order, generally ﬁxed using model selection techniques (e.g., cross-validation) [46].
Moreover, CNN can stack different convolutional layers in order to transform the input
data (i.e., the past time series values) into a more suitable higher-level representation for
the forecasting task. CNN time series forecasting applications are described in Table 1.

Figure 2. An example of Convolutional Neural Network applied to time series forecasting. The red,
the blue and the green boxes represent CNN’s convolutional layers.

---

<!-- PAGE 4 -->

Information 2023, 14, 598

4 of 35

Figure 3. Example of 1D convolution using a kernel with size k = 3. The scalar product is denoted by
•. The yellow boxes denote the learned kernel.

Table 1. Recent applications on time series forecasting using Convolutional Neural Networks.

Ref.

[47]
[48]
[10]
[6]
[7]
[49]
[50]
[12]

Year

2017
2018
2018
2018
2018
2019
2019
2023

Application

ETFs prices
Electricity consumption
Solar power and electricity load
Electricity consumption
Electricity price
Electricity price and load forecasting
Building-level load
CO2/Temperature/Humidity

3.1.1. Shortcomings of Convolutional Neural Networks

The major drawback of CNNs for time series forecasting is the use of Euclidean ker-
nels [51], since only a continuous and commonly short time series subsequence is considered
at a time by an Euclidean kernel. However, in time series forecasting tasks it may be use-
ful to extract representative features by analysing non-contiguous and farther time series
samples in the past. This limitation is overcome by Temporal Convolutional Networks (see
Section 3.1.2), with the use of causal and dilated convolutions, and by Graph Neural Networks
(see Section 3.4), with a properly designed adjacency matrix.

3.1.2. Temporal Convolutional Networks

Temporal Convolutional Networks (TCNs) were proposed for action segmentation and
detection by Lea et al. [52]. In a nutshell, a TCN is composed of cascaded 1D convolutional
layers that allow mapping arbitrarily long inputs onto output sequences of the same length.
In contrast to traditional CNNs, TCNs perform causal and dilated convolutions. Unlike 1D
convolution (see Equation (2)), in causal 1D convolution (see Figure 4) the output element
at time t is yielded by the convolution between the kernel and past input elements only,
namely [xt−1, xt−2, . . . , xt−q], where q is the kernel size that corresponds to the model order
in an autoregressive approach (see Section 3.1). In detail, causal 1D convolution is deﬁned
as follows:

y(t) = (w ∗ X )(t) =

q
∑
a=1

w(a)X (t − a)

∀t ∈ [1, . . . , L]

(3)

A dilated 1D convolution (see Figure 5) differs from a 1D convolution due to the in-
troduction of a dilation factor d. The dilation, applied to convolution, is equivalent to
considering a ﬁxed step between two adjacent kernel elements. In particular, dilated causal
1D convolution can be deﬁned as:

y(t) = (w ∗ X )(t) =

q
∑
a=1

w(a)X (t − d · a)

∀t ∈ [1, . . . , L]

(4)

---

<!-- PAGE 5 -->

Information 2023, 14, 598

5 of 35

When d = 1, a dilated 1D convolution is reduced to a 1D convolution. Dilated convolutions
allow the networks to have a large receptive ﬁeld, i.e., to capture information into the far
past, by a logarithmic growth of the number g of convolutional layers, as stated in:

g =

(cid:24)

logb

(cid:18) (n − 1)(b − 1)
(q − 1)

(cid:19)(cid:25)

+ 1

(5)

where b is the logarithmic base of the dilation factor di for the i-th convolutional layer (namely,
di = bi). TCN time series forecasting applications are reported in Table 2.

Figure 4. Causal 1D convolution with a kernel of size q = 3. Zero padding elements are added at the
beginning of the input sequence in order to have an output sequence with the same length as the
input sequence.

Figure 5. Example of a dilated causal 1D convolution with three layers using a dilation base b = 2
and a kernel size q = 3. Zero padding is used to preserve the input sequence length.

Table 2. Time series forecasting applications using Temporal Convolutional Networks.

Ref.

[53]
[15]
[30]
[54]
[9]
[55]
[11]

Year

2018
2019
2019
2020
2020
2020
2022

Application

Stock market
Beijing PM2.5
Trafﬁc
National electric demand and power demand
Wind power generation
Weather
Wind speed

TCNs share with CNNs most shortcomings (see Section 3.1.1), with the only exception

of the Euclidean kernel.

---

<!-- PAGE 6 -->

Information 2023, 14, 598

6 of 35

3.2. Recurrent Neural Networks

Recurrent Neural Networks (RNNs) [45] aim to explore the relations between the current
time series samples and the past ones. An RNN processes one time series sample at a time
to approximate the skeleton f (·) and determine the model order q implicitly. While in
Equation (1) the model order q is assumed to be constant, RNNs exhibit a dynamic temporal
behaviour, as they do not require a ﬁxed model order q and they auto-determine how far
back to look in the past. An RNN is composed of recurrent layers, which process one
input sample at a time. The earliest RNN applications for time series forecasting [56,57] are
replaced by more speciﬁc and sophisticated recurrent architectures, that is, Elman Recurrent
Neural Networks [58], Echo State Networks [59], Long Short-Term Memory Networks [60], and
Gated Recurrent Units [61].

3.2.1. Elman Recurrent Neural Networks

Elman [58], Williams-Zipser [62], and Jordan [63] RNNs are the earliest Recurrent Neural
Networks properly designed to handle temporal patterns in time series. In particular, Elman
RNN (ERNN) uses a recurrent layer, which yields an output(cid:126)ht that depends on the current
sample (cid:126)xt and the previous output(cid:126)ht−1 by a function g(·) and a generic set of time-shared
parameters ω, as described:

where(cid:126)ht−1 is produced by the same recurrent layer, i.e.,:

(cid:126)ht = gω((cid:126)xt,(cid:126)ht−1)

(cid:126)ht−1 = gω((cid:126)xt−1,(cid:126)ht−2)

(6)

(7)

and so on. The basic recurrent layer, often called a vanilla cell, works like a fully connected
layer with a ﬁxed number of units, jointly applied to the current input (cid:126)xt and the last
output(cid:126)ht−1:

(cid:16)

(cid:126)ht = g

V(cid:126)xt + W(cid:126)ht−1 +(cid:126)b

(cid:17)

(8)

In this case, the set of parameters of a recurrent layer is ω = {V, W,(cid:126)b}, where V is the
input-recurrent weight matrix, W is the recurrent-recurrent weight matrix, and(cid:126)b is the bias
vector. In Equation (8), g(·) is a nonlinear activation function, usually a hyperbolic tangent.
ERNN time series forecasting applications are summarised in Table 3.

Table 3. Elman RNN applications for time series forecasting.

Ref.

[64]
[65]
[66]
[14]
[16]

Year

2017
2018
2018
2019
2021

Application

Electricity load
Electricity load
Energy consumption
Monthly precipitation
Air Quality Index

3.2.2. Shortcomings of Recurrent Neural Networks

Recurrent neural networks based on the vanilla cell suffer from unstable training,
which prevents the network from grasping long-term dependencies. Recurrent networks,
like most neural networks, are trained by gradient descent [67], and backpropagation [67]
(Backpropagation is denoted Backpropagation Through Time (BPTT), when applied to re-
current neural networks) is used to compute the gradient of the loss function w.r.t. the
network’s weights. When back-propagation is applied to deep networks, the problems of
vanishing or exploding gradients [45] may arise. As the error gradient is back-propagated,
some of its components might either get very small, giving a negligible contribution to
the corresponding weight update, or very large, leading, in this way, to unstable training.
Over the years, several approaches have been proposed to cope with unstable gradients.

---

<!-- PAGE 7 -->

Information 2023, 14, 598

7 of 35

Among the most successful approaches are reservoir computing methods, e.g., Echo State Net-
works [59] (see Section 3.2.3), and gated cells, e.g., Long Short-Term Memory (LSTM) cells [60]
and Gated Recurrent Units (GRU) [61]. A gated cell controls how much input information
ﬂows through the layer and prevents derivatives from vanishing or getting large.

3.2.3. Echo State Networks

Echo State Networks (ESNs) were suggested by H. Jaeger [59] in 2001 as a variant of
ERNNs. ESNs are really effective in dealing with chaotic multivariate time series [68]. In addi-
tion, these networks mitigate the unstable gradient problem and are more computationally
efﬁcient due to the use of ﬁxed, random weight matrices for the recurrent layers. Based on
the vanilla cell of ERNNs (see Equation (8)), ESNs avoid backpropagation on the recurrent
layer by setting V and W as ﬁxed (i.e., non-trainable) random matrices. Furthermore, a
given sparsity level is considered in matrix W. Although random matrices are an advantage
of ENSs to mitigate the unstable gradient problem, they, at the same time, represent a major
ESNs shortcoming since they make particularly difﬁcult the application of common inter-
pretability approaches, e.g., gradient-based approaches [69,70]. ESN time series forecasting
applications are described in Table 4.

Table 4. ESN applications on time series forecasting.

Ref.

[71]
[32]
[72]
[13]
[73]
[34]
[35]
[74]
[75]
[76]
[77]
[78]
[36]
[79]
[25]
[80]
[81]
[16]
[82]

Year

2017
2017
2017
2017
2018
2019
2019
2019
2020
2020
2020
2020
2020
2020
2020
2021
2021
2021
2022

Application

Fuel cell voltage ageing
Health of automotive batteries
Slugging ﬂow phenomenon
Temperature/Rainfall
Lorenz/Rossler/Sunspot-Runoff
Industrial processes
Fuel cell durability
Photovoltaic voltage
Electricity load
Electricity load
Energy consumption/Wind power generation
Temperature of exhaust gas
Faults in airplane engines
Multiple time series
Blood glucose concentration
Multiple time series
Electrical load
Air Quality Index
Chaotic time series

3.2.4. Long Short-Term Memory

Long Short-Term Memory (LSTM) Networks [60] were originally proposed for natural
language modelling. The LSTM cell (see Figure 6) uses three gating mechanisms: input, forget
and output gates. Firstly, the input of LSTM layers, which is composed of the current input
(cid:126)xt and the output(cid:126)ht−1 from the last time step are is combined into the current input vector
(cid:126)it as follows:

(cid:126)it = γ(Wi(cid:126)xt + Ui

(cid:126)ht−1 +(cid:126)bi)

(9)

where γ(·) can be any sigmoidal function (e.g., logistic or hyperbolic tangent ones) and
{Wi, Ui,(cid:126)bi} is a set of parameters. Furthermore, the three gates are computed as:

(cid:126)gt = σ(Wg(cid:126)xt + Ug

(cid:126)ht−1 +(cid:126)bg)

(cid:126)ft = σ(Wf(cid:126)xt + U f

(cid:126)ht−1 +(cid:126)b f )

(10)

(11)

---

<!-- PAGE 8 -->

Information 2023, 14, 598

8 of 35

(cid:126)ht−1 +(cid:126)bo)

(cid:126)ot = σ(Wo(cid:126)xt + Uo

(12)
where σ(·) is the logistic function, (cid:126)gt, (cid:126)ft, (cid:126)ot are the input, forget, and output gates, respec-
tively, and {Wg, Ug,(cid:126)bg}, {Wf , U f ,(cid:126)b f }, {Wo, Uo,(cid:126)bo} are the respective sets of parameters.
Furthermore, the LSTM’s inner state (cid:126)ct is updated by a linear combination of (cid:126)it and the
previous inner state (cid:126)ct−1:

(cid:126)ct = (cid:126)gt (cid:12) (cid:126)it + (cid:126)ft (cid:12)(cid:126)ct−1
where (cid:12) is the element-wise product. Finally, the output(cid:126)ht of a LSTM layer is deﬁned as:

(13)

(cid:126)ht = (cid:126)ot (cid:12) tanh((cid:126)ct)

(14)

Figure 6. Long-Short Term Memory cell architecture.

LSTM time series forecasting applications are described in Table 5.

Table 5. LSTM applications on time series forecasting.

Ref.

[17]
[83]
[84]
[19]
[85,86]
[87]
[88]
[26]
[89,90]
[20]
[7]
[24]
[91]
[92]
[93,94]
[33]
[10]
[95]
[96]
[97]
[98]
[31]
[14]
[99]

Year

2016
2016
2016
2017
2017
2017
2017
2018
2018
2018
2018
2018
2018
2018
2018
2018
2018
2018
2018
2019
2019
2019
2019
2019

Application

Stock market
Electricity load
Trafﬁc ﬂow
Stock prices
Stock market
Electricity load
Air quality
Forecasting Cancer Growth
Stock market
Stock prices
Electricity price
Diabetes mellitus
Rainfall-runoff modelling
Predicting water table depth
Electricity load
Life prediction of batteries
Solar power and electricity load
Solar intensity
Air quality
UCI data sets
Building load
Petroleum production
Monthly precipitation
Weather forecasting

---

<!-- PAGE 9 -->

Information 2023, 14, 598

9 of 35

Table 5. Cont.

Ref.

[18]
[100]
[79]
[101]
[16]
[102]
[12]

Year

2020
2020
2020
2021
2021
2022
2023

Application

Stock market
COVID-19
Multiple time series
Weather/Air Quality/Clinical data
Air Quality Index
Financial markets
CO2/Temperature/Humidity

3.2.5. Gated Recurrent Units

RNNs based on Gated Recurrent Units (GRUs) [61] were introduced for Statistical
Machine Translation. A GRU layer, as shown in Figure 7, uses two gating mechanisms:
an update and a reset gate. Both the reset and the update gate depend on (cid:126)xt and (cid:126)ht−1.
Analogously to LSTM, the reset gate(cid:126)rt and the update gate (cid:126)ut are computed as:

(cid:16)

(cid:126)rt = σ

Wr(cid:126)xt + Ur

(cid:126)ht−1 +(cid:126)br

(cid:17)

(cid:16)

(cid:126)ut = σ

Wu(cid:126)xt + Uu

(cid:126)ht−1 +(cid:126)bu

(cid:17)

(15)

(16)

where σ(·) is the logistic function and the rest of the parameters have the same meaning as
the LSTM (see Section 3.2.4). Furthermore, an intermediate output(cid:126)h(cid:48)

t is given by:

(cid:126)h(cid:48)

t = tanh

(cid:16)

W(cid:126)xt + U((cid:126)rt (cid:12)(cid:126)ht−1) +(cid:126)b

(cid:17)

(17)

where {W, V,(cid:126)b} is an additional set of parameters and (cid:12) is the element-wise product.
Finally, the output (cid:126)ht of the GRU layer is given by the sum of (cid:126)h(cid:48)
t and (cid:126)ht−1, weighted
element-wise by the update gate:

(cid:126)ht = (cid:126)ut (cid:12)(cid:126)ht−1 + ((cid:126)e − (cid:126)ut) (cid:12)(cid:126)h(cid:48)
t

(18)

where (cid:126)e is a column vector whose elements are all equal to 1. GRU time series forecasting
applications are described in Table 6.

Figure 7. Architecture of a GRU cell. The column vector(cid:126)e is composed of elements that are all equal to 1.

---

<!-- PAGE 10 -->

Information 2023, 14, 598

10 of 35

Table 6. Applications on time series forecasting using GRU-based Recurrent Neural Networks.

Ref.

[84]
[8]
[103]
[7]
[24]
[97]
[79]
[104]

Year

2016
2017
2018
2018
2018
2019
2020
2021

Application

Trafﬁc ﬂow
Electricity load
Photovoltaic forecasting
Electricity price
Diabetes mellitus
UCI data sets
Multiple time series
Air quality/Stock prices/Household electric power

3.2.6. Shortcomings of LSTMs and GRUs

It has to be remarked that, even if training is stable, it can be hard for recurrent
networks to learn dependencies between distant sequence samples. For instance, a recurrent
network that generates an output sequence starting from an input sequence is shown in
Figure 8.

Figure 8. The red path in the recurrent model denotes the ﬂow that information about an input
sample (x20) must follow before reaching an output layer (y60) that might require it.

Supposing that the output element at position t = 60 has a strong dependency on the
input at position t = 20, information about the input sample x20 is useful to predict the
output sample y60. The output sample yt is predicted starting from ht, a lossy summary
of the past inputs yielded by the recurrent layer; hence, the only way for the output layer
to know about x20 is through h60. The recurrent layer ﬁrst captures information about
x20 through h20, which has to pass by many steps and then aggregate information about
many other input elements, before achieving h60. There is no guarantee that after so many
recurrent steps, adequate information about x20 is preserved into h60. In fact, h60 may just
contain information about the most recent samples and have no information about x20 at all.
The short-term memory of recurrent networks is one of their major drawbacks and one of
the main reasons why attention mechanisms and Transformers were originally introduced
in deep learning (see Section 4.1).

3.3. Hybrids and Variants of Deep Neural Networks

In recent years, speciﬁc deep neural networks have been proposed as hybrids or variants
of the aforementioned architectures. Hybrid models combine multiple statistical or machine
learning methods to improve the robustness and accuracy of forecasting. Towards the same
goal are the works that propose variants of deep neural architectures properly adapted
for time series forecasting tasks. Hybrids and variants of deep neural networks share the
same limitations as the models they are based on. The most successful approaches are
summarised in Table 7.

---

<!-- PAGE 11 -->

Information 2023, 14, 598

11 of 35

Table 7. Applications in time series forecasting using variants and hybrids of common deep neural
networks. The symbol ‘+’ denotes a combination of multiple models or methodologies. GARCH and
ANN acronym stand for Generalized AutoRegressive Conditional Heteroskedasticity [105] and Artiﬁcial
Neural Networks, respectively.

Ref.

[106]
[107]
[108]
[109]
[110]
[111]

Year

2016
2017
2017
2018
2018
2018

[112]

2018

[113]
[114]
[115]
[116]
[117]

2018
2018
2018
2018
2018

[118]

2019

[119]

2019

[120]

2019

[27]

[121]
[122]
[23]
[123]

2019

2020
2020
2020
2023

Architecture

Autoencoder + LSTM
Autoencoder + LSTM
CNN + LSTM
CNN + LSTM
CNN + LSTM
CNN + LSTM
LSTM + Attention mechanism
(see Section 4.1.1)
LSTM + GRU
GARCH + LSTM
GRU variant
CNN + LSTM
ANN + LSTM + CNN
LSTM + Attention mechanism
(see Section 4.1.1)
LSTM + Attention mechanism
(see Section 4.1.1)
LSTM + Attention mechanism
(see Section 4.1.1)
CNN + Attention mechanism
(see Section 4.1.1)
CNN + LSTM
LSTM + Fuzzy Logic
TCN + Attention
TCN + LSTM/GRU

Application

Solar power
Stock prices
Stock prices
Electricity prices
Electricity load
Wind speed

Stock market

Stock prices
Stock prices
Trafﬁc forecasting
PM2.5 concentration
PM2.5 concentration

Online Sales/Electricity prices

Solar generation

Electricity load

Trafﬁc/Stock market

Stock market/Temperature
COVID-19
Remaining Useful Life
Chaotic Time Series/ECG

3.4. Graph Neural Networks

A recent promising research direction in multivariate time series forecasting is the
application of Graph Neural Networks (GNNs) [124,125]. The original domain of GNNs is
the handling of spatial dependencies among entities in a graph-modelled problem. In detail,
GNNs can be used to generate representations of such entities that depend on the structure
of the graph and on any additional information. A graph G (cid:48) is formally deﬁned as a tuple
G (cid:48) = [V, E ], where V denotes the set of nodes and E is the set of edges, the connections
between the nodes of the graph, represented, in this case, with an adjacency matrix. The
deﬁnition of this matrix is based on a metric function that can be either a priori ﬁxed or
learned during the training process [125]. The basic idea of a GNN can be summarised
by the use of three main operators: aggregate, combine, and readout. The k-th GNN layer
performs the aggregate and combines operators. The former consists of agglomerating,
for each graph node v ∈ V, information from its neighbourhood N(v) as deﬁned by the
adjacency matrix:

N(v) = aggregate((cid:126)hk−1
(cid:126)hk

u

: u ∈ N(v))

∀k > 1

(19)

u

where(cid:126)hk−1
ous GNN layer k − 1, and (cid:126)hk
aggregated information(cid:126)hk

is the feature vector of the u-th neighbouring node of v, yielded by the previ-
N(v) is the aggregated information. The latter combines the

N(v) with the feature vector(cid:126)hk−1

v

of the current node v:

v = combine((cid:126)hk−1
(cid:126)hk

v

,(cid:126)hk

N(v))

∀k > 1.

(20)

---

<!-- PAGE 12 -->

Information 2023, 14, 598

12 of 35

When k = 1 the aggregate operator is not deﬁned, whereas the combine operator reduces to:

v = (cid:126)xv,
where (cid:126)xv represents the input feature vector associated to the v-th node. Furthermore, the
readout operator is applied on the output of the last GNN layer K in order to obtain a ﬁnal
vector(cid:126)hG representing the whole graph G (cid:48) = [V, E ]:

(21)

(cid:126)h1

(cid:126)hG = readout((cid:126)hK

v : v ∈ V )

(22)

In the case of multivariate time series forecasting, GNNs have been successfully applied as
feature selection mechanisms. It is important to remark that GNNs could also be applied to
spatio-temporal time series forecasting which is not the object of the survey. GNN time series
forecasting applications are described in Table 8.

Table 8. GNN applications on time series forecasting.

Ref.

[28]
[29]
[126]
[127]
[128]
[129]
[21]
[130]
[22]

Year

2020
2021
2022
2022
2022
2022
2022
2022
2023

Application

Trafﬁc/Electricity load/Exchange rate
Solar energy/Trafﬁc/Electricity load/Exchange rate
Stock market
PM2.5/Trafﬁc/Wind speed
Stock market
Electricity load/Solar energy/Trafﬁc
Solar energy/Wind power generation/Electricity load/Exchange rate
Solar energy/Trafﬁc/Electricity load/Exchange rate
Solar energy/Trafﬁc/Electricity load/Exchange rate

3.5. Deep Gaussian Processes

Let D = ((cid:126)x1, (cid:126)x2, . . . , (cid:126)xn) be a data set and Y = ((cid:126)y1, (cid:126)y2, . . . , (cid:126)yn) the target output, a
Gaussian Process [131] is a Bayesian model composed of a collection of random variables,
any ﬁnite number of which have a joint Gaussian distribution, and it is fully deﬁned
by a mean function m((cid:126)xi) and covariance function k((cid:126)xi, (cid:126)xj), which is usually a Mercer
kernel [131,132]. The analytical solution of a Gaussian Process entails computing the inverse
of the covariance matrix of observations, which has a computational complexity of O(n3).
A common approach for coping with this computational drawback is the use of Sparse
Gaussian Process [133]. This method consists of considering a reduced set of m (m (cid:28) n)
training samples, the so-called inducing variables, reducing, in this way, the complexity to
O(nm2). A sequence of Gaussian Processes deﬁnes a Bayesian model called Deep Gaussian
Process (DGP) [134]. As shown in Figure 9, in DGPs the output of the single Gaussian
Process located at the previous layer is fed as an input to the Gaussian Process located at
the next layer. Unlike the rest of the deep learning techniques, Deep Gaussian Processes
can estimate not only the value of future time series samples but also provide a conﬁdence
interval of the predictive time series value representing, in this way, the uncertainty of the
model. DGP time series forecasting applications are described in detail in Table 9.

Table 9. DGP applications on time series forecasting.

Ref.

[135]
[136]
[137]
[138]
[139]

Year

2017
2020
2022
2023
2023

Application

Crop Yield forecasting
Crop Yield forecasting
Electricity load
Car-hailing demand
Ozone concentration forecasting

---

<!-- PAGE 13 -->

Information 2023, 14, 598

13 of 35

Figure 9. Deep Gaussian Processes. In the ﬁgure X , Y represent the data set and the desired output,
respectively, f (i) is the latent function to be estimated and mi, ki represent the mean and covariance
function of i-th layer.

3.6. Generative Models

Among the latest trends in deep learning research, there are the so-called generative
models, speciﬁcally Generative Adversarial Networks (GANs) and Diffusion Models (DMs).
Both families are popular for their groundbreaking capabilities in generating synthetic
images. These successes encouraged researchers to apply GANs and DMs to sequential
data as well, including time series. As generative models, both methodologies have been
used for time series generation tasks. However, it can adapt them for other time series-related
tasks as well, speciﬁcally time series forecasting. Sections 3.6.1 and 3.6.2 provide an overview
of GANs and their usage for time series forecasting, respectively; Sections 3.6.3 and 3.6.4
discuss diffusion models and their applications to time series forecasting, respectively.

3.6.1. Generative Adversarial Networks

A GAN [140] is composed of two separate artiﬁcial neural networks: a generator
network G that generates synthetic data, with the same distribution of the input ones, and
a discriminator network D that classiﬁes input data as either real or synthetic. G and D are
trained with an adversarial training approach. G takes random noise as input and it has
to transform the noise into a synthetic data sample following the same distribution of the
real data. D receives both real and generated samples and it estimates the probability that
any given data sample comes from the real data rather than from the generator. The two
networks are trained jointly with a minimax two-player game [140], i.e., the discriminator
is trained to maximise the correct classiﬁcation ratio for both real and generated samples.
Whereas, the generator has the goal to trick the discriminator into misclassifying generated
samples by minimising the correct classiﬁcation ratio. This training procedure is expressed
by the objective function:

min
G

max
D

V(D, G) = E

(cid:126)x∼px((cid:126)x)[log D((cid:126)x)] + E

(cid:126)z∼pz((cid:126)z)[log(1 − D(G((cid:126)z)))].

(23)

where, (cid:126)x is a real data point, sampled from the real data distribution px((cid:126)x); (cid:126)z is a noise
vector, sampled from a distribution pz((cid:126)z), a priori ﬁxed; D((cid:126)x) is the probability distribution
estimated by the discriminator; G((cid:126)z) is the sample produced by the generator, starting from
the noise (cid:126)z. GANs can be implemented by any neural architecture for the generator and
the discriminator. For instance, G and D can be implemented by MLPs [67], as originally
proposed in [140], CNNs (see Section 3.1), with some architectural constraints to stabilise
the training procedure [141], or LSTM (see Section 3.2.4) networks [142].

---

<!-- PAGE 14 -->

Information 2023, 14, 598

14 of 35

3.6.2. Generative Adversarial Networks in Time Series Forecasting

In literature, there are two main approaches for using GANs in time series forecast-
ing: as data augmentation or as an end-to-end forecasting model. In the former case, GANs
generate synthetic time series in a given domain (e.g., ﬁnancial or health-related time
series) in order to augment the original small data set. The augmented data set, with
both real and generated time series, is then used to train a traditional forecasting model,
e.g., a model based on an LSTM network. In the latter case, the forecasting model is a
GAN itself, and it generates future samples starting from previous ones and, eventually,
other exogenous inputs (In time series forecasting, a variable is said to be exogenous if it
is not a time series sample, but it can still affect the time series samples. For instance,
temperature may be an exogenous variable in rainfall time series forecasting) [143]. For
example, in [144] a GAN is ﬁrstly used to augment a building energy consumption data set
and then, an ensemble of ﬁve traditional predictive models is trained on such augmented
data set. In particular, to augment the data set, Conditional GANs (CGANs) [145] and
Information Maximising GANs (InfoGANs) [146] are compared with each other. Similarly,
in [147] COVID-19 epidemic data is generated by a custom GAN with an LSTM generator
and an MLP discriminator. Furthermore, a Transformer is used to make a forecasting model
trained on the GAN-augmented data set. Moreover, some GAN-based models have been
speciﬁcally developed for time series generation, e.g., QuantGAN [148], for ﬁnancial time
series with long-term time dependencies, SynSigGAN [149], for continuous biomedical
signals, Recurrent Conditional GANs (RCGANs) [150], for medical data, TimeGAN [151], a
framework for domain-agnostic time series generation, Conditional Sig-Wasserstein GAN
(Sig-WCGAN) [152], and TTS-GAN [153], entirely based on Transformers. Some of the
aforementioned GANs, e.g., RCGAN, TimeGAN, Sig-WCGAN, are conditional GANs [145],
i.e, time series are not generated from only random noise but also conditioned on the real
time series and/or related information, e.g., exogenous inputs, for improving generated
time series quality. The use of conditional GANs is popular for end-to-end forecasting,
where the generated time series window, typically in the short-term future, is often con-
ditioned on previous samples and on other exogenous inputs (see [154–158]). Table 10
collects some works on GAN applications for time series forecasting.

Table 10. GAN applications on time series forecasting.

Ref.

[159]
[160]
[154]
[161]
[162]
[163]
[164]
[165]
[166]
[156]
[167]
[168]
[144]
[169]
[170]
[147,155]
[157,158]
[171]
[172]

Year

2018
2019
2019
2019
2019
2020
2020
2020
2021
2021
2021
2021
2021
2021
2022
2022
2022
2022
2023

Application

Stock market
Trafﬁc forecasting
Lorenz/Mackey-Glass/Internet Trafﬁc data
Medicine expenditure
Electricity load
Stock price
Long-term benchmark data sets (see Section 6.2)
Soil temperature
Stock market/Energy production/EEG/Air quality
Internet Trafﬁc data
Store Item Demand/Internet Trafﬁc/Meteorological data
Wind power/Solar power
Energy consumption
Electricity load
Trajectories forecasting
COVID-19
Photovoltaic power
Building power demand
Financial time series

---

<!-- PAGE 15 -->

Information 2023, 14, 598

15 of 35

3.6.3. Diffusion Models

A new family of generative architectures are the diffusion models. They have been
showing cutting-edge performance in generating samples that reﬂect the observed data
in different domains, e.g., image generation, video generation, and text synthesis. Three
key formulations are used to develop diffusion-based approaches for short-term time
series applications: denoising diffusion probabilistic models (DDPMs) [173,174], score-
based generative models (SGMs) [175], and stochastic differential equations (SDEs) [176].
Diffusion models aim to approximate a generative process G that generates new samples
drawn from an underlying distribution q(x), given some observed data x from the same
distribution. To approximate G, in the forward process, a progressive injection of Gaussian
noises on the observed data is performed by the majority of diffusion models. Furthermore,
a reverse process is applied, by a learnable transition kernel, to reconstruct the original
data. Most diffusion models assume that, after a ﬁnite number of noise injection steps, q(x)
distribution of the observed data will become a Gaussian distribution. Therefore, the goal
of diffusion models is to ﬁnd the probabilistic process P that approximates q(x) distribution
of original data from the Gaussian distribution. In this manner, any sample of Gaussian
distribution can be transformed by P into a new sample of q(x) distribution of observed
data x. The principle of diffusion models is to progressively perturb the observed data x
with a random noise by a forward diffusion process F before recovering the original data
using a backward reverse diffusion process B. A deep neural network is used in the B process
to approximate the amount of noise that must be removed in the denoising steps to recover
the original data. For the sake of readability, the theoretical foundations of diffusion models
and their main architectures are omitted in the section and moved in Appendix B, whereas
the diffusion models for short-term time series forecasting are described in the following
subsection.

3.6.4. Diffusion Models in Short-Term Time Series Forecasting

In recent years, several diffusion-based approaches for time series forecasting have
been proposed. They are based on the three predominant methods of diffusion model
described in Appendix B. The ﬁrst prominent diffusion model architecture for time series
forecasting is TimeGrad [177], which is a DDPM variant. The forward process of TimeGrad
injects noises into data at each predictive sample, and then denoises gradually through the
backward process conditioned on previous time series samples. For encoding the previous
time series samples, TimeGrad uses an RNN architecture, e.g., LSTM (see Section 3.2.4) or
GRU (see Section 3.2.5), The objective function of TimeGrad is represented by a negative
log-likelihood, denoted as:

T
∑
t=t0

− log pθ(x0

t |ht−1),

(24)

where [t0, T] is the prediction length. The Equation (24) can be reformulated considering the
lower bound:

E

t ,(cid:101)[δ(k)||(cid:101) − (cid:101)θ((cid:112)

k,x0

˜akx0

t + (cid:112)

1 − ˜ak(cid:101), ht−1, k)||2].

(25)

The parameters θ are estimated during the training, minimising the negative log-likelihood
objective function with a stochastic sampling. Furthermore, future time series samples are
generated with a step-by-step procedure. The observation for the next samples at time
T + 1 is predicted in a similar way as DDPM (see Appendix B). Similarly, the ScoreGrad
model [178], based on the same target distribution of TimeGrad, deﬁnes a continuous
diffusion process using SDEs (see Appendix B). ScoreGrad consists of two modules: the
former is a feature extraction module (e.g., an RNN) almost identical to TimeGrad, or an
attention-based network, e.g., Transformer (see Section 4.1), for computing the hidden state

---

<!-- PAGE 16 -->

Information 2023, 14, 598

16 of 35

ht of previous time samples, the latter is a conditional SDE-based score-matching module.
The objective function of ScoreGrad is computed as follows:

T
∑
t=t0

Lt(θ),

with Lt(θ) being:

E

k,x0

t ,xk
t

[δ(k)||sθ(xk

t , ht, k) − ∇xk

t

(26)

(27)

log qok(xt|x0

t )||2].

It is worthwhile to remark that, in Equation (27), the general formulation of SDEs has been
used for the sake of simplicity. Recently, time series research has paid attention to avoiding
model overﬁtting phenomena in the forecasting of short time series. D3VAE [179], tries to
address the problem of short time series, applying a coupled diffusion process for time series
data augmentation, and then it performs a bidirectional autoencoder (BVAE), as a score model.
Moreover, D3VAE takes into account the decoupling of latent variables by reducing total
correlation to improve prediction interpretability and stability. Furthermore, the objective
function of D3VAE includes the mean square error (MSE), which highlights the requirement
of supervision, among the forecast and current samples in the prediction window. Unlike
TimeGrad, D3VAE injects noises separately into the previous samples (context) x0
1:t0−1 and
the prediction window x0
t0:T by the coupled diffusion process:

1:t0−1 = (cid:112)
xk

˜akx0

1:t0−1 + (cid:112)

1 − ˜ak(cid:101),

(28)

(cid:113)

(cid:113)

˜a(cid:48)

kx0

xk
t0:T =

t0:T +
where (cid:101) indicates the standard Gaussian noise. Short time series forecasting beneﬁts the
simultaneous improvement of the context and prediction window provided by the diffusion
process. The B process is made up of two steps. The former forecasts xk
t0:T with a BVAE
model, considering the context xk
t0:T of BVAE with a
denoising score matching module, as follows:

1:t0−1. The latter denoises the output ˜xk

(29)

k(cid:101),

1 − ˜a(cid:48)

t0:T ← ˜xk
xk

t0:T − σ2

0 ∇ ˜xk

t0:T

E( ˜xk

t0:T; e),

(30)

where E( ˜xk
four losses, that can be written as follows:

t0:T; e) is the energy function. The objective function of D3VAE is composed of

λ1DKL(q(xk

t0:T||pθ( ˜xk

t0:T)) + λ2LDSM + λ3LTC + LMSE,

(31)

where λ1, λ2, λ3 are the regularisation parameters of divergence between target distribution and
distribution of prediction window, denoising score matching objective, and total correlation among
latent variables, respectively. Diffusion models for time series forecasting are summarised in
Table 11.

Table 11. Recent diffusion models for time series forecasting.

Ref.

[177]
[178]
[180]
[179]

Year

2021
2021
2022
2022

Model

TimeGrad
ScoreGrad
DSPD
D3VAE

4. Deep Learning Models for Long-Term Forecasting

In long-term forecasting, the skeleton of a time series can be approximated by using
the Transfomer architecture. Firstly, the original Transformer architecture (Section 4.1) is

---

<!-- PAGE 17 -->

Information 2023, 14, 598

17 of 35

described and attention mechanisms are presented (Sections 4.1.1 and 4.1.2). Furthermore,
the main limitations of Transformers are discussed (Section 4.1.3) and variants of Transformer,
properly designed to cope with long-term time series forecasting tasks, e.g., Informer,
Autoformer, FEDFormer and Crossformer, are presented (Section 4.1.4).

4.1. Transformers

The Transformer [181] is a deep-learning architecture borrowed from Natural Lan-
guage Processing. It can be described as: “a model architecture eschewing recurrence and relying
entirely on attention mechanisms to draw global dependencies between input and output” [181].
The Transformer architecture was proposed to overcome the main drawbacks of recurrent
models (see Sections 3.2.2 and 3.2.6) with sequence modelling tasks:

1.

2.

The output state ht of a recurrent layer at time t depends on the state ht−1, produced
at the previous time step. This inherent sequential nature prohibits the intra-sequence
parallelism of recurrent networks.
Recurrent networks cannot generally learn relationships between sequences of distant
samples, since information must ﬁrst pass through all data samples in between (see
Figure 8).

The standard Transformer follows a general encoder-decoder architecture for sequence-

to-sequence transduction, as shown in Figure 10.

In time series forecasting, the Transformer’s input is a time-ordered sequence of past
samples X = [(cid:126)x1,(cid:126)x2, . . . ,(cid:126)xL] where L is the sequence length and (cid:126)xi ∈ Rd is the i-th sample of a
d-dimensional multivariate time series. Due to the use of attention mechanisms, Transformers
make no assumption on any intrinsic temporal or spatial ordering of input elements, namely
inputs are seen as a set of samples rather than ordered sequences of samples. If there is a
relevant input ordering for the modelling task, e.g., time series forecasting, the ordering
should be encoded in the input embedding. In Transformers, this is commonly achieved by
summing a positional embedding Epos to the main sample embedding F(X ) [181]:

input = F(X ) + Epos

(32)

where the matrix (Differently from what appears in some machine learning papers, the
more precise tensor product notation is used in the whole work for representing matrices)
F(X ) ∈ RL ⊗ RD represents a projection of the input sequence in a higher D-dimensional
space (D > d).
In time series forecasting, a 1D convolutional layer is commonly used
with D learned kernels, as described in Section 3.1, in order to extract a D-dimensional
representation for each sample in X [181–184]. Epos can either be a learned embedding or
a ﬁxed embedding. A naive solution, yet effective, consists of using a sinusoidal position
encoding [181]. However, in time series forecasting, other positional embeddings can be
used as well, e.g., temporal-based embeddings [182–184]. The encoder and the decoder can
have two different separated embeddings, or they can share the same embedding if input
and output samples belong to the same set. In time series forecasting, the encoder input is
the complete sequence of past samples X , while the decoder input is commonly composed
of the most recent part of X (e.g., the second half of X , i.e., [(cid:126)xL/2,(cid:126)xL/2+1, . . . ,(cid:126)xL]) and a
zero-vector whose length is equal to prediction length P, see Equation (1). The encoder
and decoder are composed of Ne and Nd stacked layers, respectively (see Figure 10). The
output of a layer is the input for the next layer. Each encoder layer has two sublayers: a
self-attention layer, that relates each input sample with the rest of the samples, and a shallow
feed-forward dense layer, shared along the sequence axis, that works as a nonlinear projection
layer. To foster gradient propagation and training, each sublayer’s input is added to its own
output with a residual connection [185], and layer normalization [186] is used to normalise
the samples of the resulting sequence into a normal distribution with a learned mean and
standard deviation. Each decoder layer follows the same overall structure of a generic
encoder layer, but it has one additional sublayer. The ﬁrst sublayer implements a particular
kind of self-attention mechanism, the so-called causal (or masked) self-attention [181]. It works

---

<!-- PAGE 18 -->

Information 2023, 14, 598

18 of 35

similarly to the encoder layer’s self-attention, as each input sample is related to the others
in the decoder’s input sequence, but it also uses masking to prevent future samples from
being considered when the processing of the current sample occurs. Furthermore, the
output of the causal self-attention sublayer is related to the encoder’s hidden representation
(that is, the output of the ﬁnal encoder layer) by a cross-attention layer. As in encoder layers,
a Multi-Layer Perceptron [67] with one hidden layer is used for projecting nonlinearly the
output of cross-attention. Moreover, each sublayer is wrapped by a residual connection
followed by layer normalization. Finally, the output of the last decoder layer is fed to a ﬁnal
prediction layer.

Figure 10. Transformer architecture. On the left side, the encoder processes an input sequence,
producing a hidden representation. On the right side, the decoder uses the encoder’s output to generate
the output sequence. The decoder works in an autoregressive way, consuming past generated samples
as additional inputs to generate the next output sample.

4.1.1. Attention Mechanisms

The most important computational blocks of a Transformer are attention mechanisms,
that allow the model to focus its attention on speciﬁc parts of the input, depending on
the information being processed. Among various deﬁnitions of attention, Transformers
adopt the so-called scaled dot-product attention, which is very similar to multiplicative at-
tention [187]. Attention mechanisms operate on the following elements: a set of queries
Q ∈ RM ⊗ RDk that represents the information being processed by the model, and sets of
keys K ∈ RN ⊗ RDk and values V ∈ RN ⊗ RDv , where Dk and Dv denote the dimension of
space where queries, keys and values are projected. Moreover, N denotes the cardinality of
both keys and values, while M is the cardinality of the input queries. The output Y for all
queries is computed as follows:

Y = Attention(K, V, Q) = softmax

(cid:32)

(cid:33)

V

QK(cid:62)
√
Dk

(33)

The attention output Y ∈ RM ⊗ RDv is a matrix whose i-th row contains the output vector
for the i-th query. Note that the softmax in Equation (33) is applied row-wise to its input
matrix. Where do these queries, keys and values come from? First of all, keys and values are often
the same vectors, i.e., a value vector coincides with its key. Furthermore, as described in
Section 4.1, the Transformer performs attention in two ways, self-attention and cross-attention.

---

<!-- PAGE 19 -->

Information 2023, 14, 598

19 of 35

In self-attention, queries and values are the same vectors; in cross-attention queries come
from the previous decoder sublayer, while key and value vectors are given by the encoder’s
hidden representation.

4.1.2. Multi-Head Attention

Multi-Head Attention (MHA) is a more advanced version of the aforementioned scaled
dot-product attention. As discussed in [181], the scaled dot-product attention permits a
network to attend over a sequence. However, often there are multiple different aspects a
sequence element wants to attend to, and a single weighted average is not an adequate
option for it. This motivates the extension of the scaled dot-product attention to MHA,
which allows the model to jointly attend to information from diverse representation sub-
spaces, as shown in Figure 11.

(a) Scaled dot-product attention.
Figure 11. Comparison of a single scaled dot-product attention (a) and multi-head attention with H
attention heads (b).

(b) Multi-Head Attention with H heads.

In MHA, keys, values and queries are linearly projected H separate times, by three
learned projection matrices, onto spaces of dimensions Dk, Dv and Dk respectively. Fur-
thermore, a scaled dot-product attention is applied to each of these projections and the
results are concatenated together and re-projected onto the previous layer space. Each
projection-attention pair deﬁnes a so-called attention head hi. For the sake of simplicity,
keys, values and queries are assumed to have the same dimension D. Each attention head
i ∈ RD ⊗ RDk , WV
i ∈ RD ⊗ RDk ,
hi has three learned matrices: WK
used to project keys, values and queries, respectively. Each attention head applies a scaled
dot-product attention (see Equation (33)) to the projected keys, values and queries (see
Section 4.1.1):

i ∈ RD ⊗ RDv and WQ

hi = Attention(KWK

i , VWV
i

Finally, the attention output Y is given by:

, QWQ

i ) ∀i ∈ [1, H]

Y = MHA(K, V, Q) = Concatenate(h1, h2, . . . , hH)Wo

where the outputs hi from all attention heads are concatenated into a single RM ⊗ RHDv
matrix and then re-projected linearly to the original D-dimensional space via an additional
projection matrix Wo ∈ RHDv ⊗ RD.

4.1.3. Shortcomings of Transformers

There are three main shortcomings of Transformers. Firstly, Transformers are locally-
agnostic, that is, the scaled dot-product of the attention mechanism (see Equation (33)) is
insensitive to the local context, which can make the model prone to anomalies in time

(34)

(35)

---

<!-- PAGE 20 -->

Information 2023, 14, 598

20 of 35

series forecasting [188]. Furthermore, Transformers suffer of memory bottleneck, i.e., Trans-
formers’ space complexity is O(L2) with sequence length L [188]. Similarly, Transformers
also have the same time complexity, limiting their application to the long-term forecast-
ing. These shortcomings are faced by some of the Transformer variants described in the
following section.

4.1.4. Transformer Variants for Time Series Forecasting

In recent years, many variants of the naive Transformer [181], speciﬁc for time series
forecasting, have been proposed. Key innovations that these variants suggest concern the
embedding layer, attention mechanisms and even the encoder-decoder structure. Most
of the literature focused on the design of alternative attention mechanisms that are more
suitable for time series forecasting tasks. One of the ﬁrst such works is the LogTrans [188],
which handles two limitations of the traditional Transformer: locally-agnostic and memory
bottleneck (see Section 4.1.3). The former limitation is tackled using causal convolutions
(see Section 3.1.2) to generate keys and queries in the self-attention module. For the
latter, a log-sparse mask is considered in order to reduce the computational complexity (see
Section 4.1.3) of multi-head attention. Inspired by the idea of LogTrans, another variant, the
Informer [182], deﬁnes a new sparse measure to characterise a subset of the most informative
queries before applying attention. In addition, this strategy also allows for the reduction of
the computational complexity of attention mechanisms. Unlike LogTrans and Informer, the
Autoformer [183] replaces the standard scaled dot-product attention with an autocorrelation
mechanism. Additionally, a decomposition module is employed to break down the time series
into trend and seasonal components, assuming implicitly that they exist and are additive.
The autocorrelation mechanism measures the time-delay similarity between input signals
and aggregates the top-k similar sub-series to produce the output. The FEDformer [184],
based on the work of Linformer [189], applies attention to a low-rank approximation of the
input based on the Restricted Isometry Property (RIP) matrix theory [190]. First, it represents
the input signal into a frequency domain (either Fourier or Wavelet). Furthermore, it
achieves a linear complexity by applying simpliﬁed attention mechanisms on a randomly
selected subset of frequencies with a ﬁxed size m. Recently, research efforts have moved
from attention mechanisms to input representation, speciﬁcally concerning how to relate
the dimensions of a multivariate time series and how to project the input sequence into a
latent representation. The patchTST [191] assumes channel independence, i.e., independence
among the dimension of the input multivariate time series, processing each dimension
as a univariate time series. PatchTST segments each input sequence into shorter, local
sub-sequences that are fed as input samples to a naive Transformer encoder [181]. All
time series dimensions are implicitly related via the sharing of the encoder weights. A
similar consideration is adopted by the Crossformer [192], which segments each dimension
of the input time series into non-overlapping shorter sub-sequences. Unlike patchTST,
however, the Crossformer explicitly deﬁnes the relations among all dimensions using a
Two-Stage Attention (TSA) mechanism. Furthermore, Crossformer follows a Hierarchical
Encoder-Decoder architecture, in which multiple layers of TSA are used to capture relations
at multiple time scales. Another relevant work is the Pyraformer [193], which proposes a
Pyramidal Attention Module (PAM) to capture long-term dependencies while achieving a
complexity that is linear in the sequence length. Essentially, PAM consists of applying the
classic scaled dot-product attention in a sparse fashion according to a pyramidal graph,
built using a cascade of strided convolutions, that deﬁnes a multi-scale representation
of the input sequence. According to PAM, each node of the graph is a query and it
can attend only those nodes (keys) that are its direct neighbours in the graph. In this
way, Pyraformer is able to capture both short-term and long-term dependencies while
still achieving a linear complexity. Similarly to Pyraformer, Scaleformer [194] addresses
the importance of multi-scale dependencies in time series forecasting. The approach is
orthogonal to many time series Transformers and, as such, it has been empirically evaluated
with some of the aforementioned models like the Autoformer [183] and the FEDformer [184].

---

<!-- PAGE 21 -->

Information 2023, 14, 598

21 of 35

Given an input past sequence and the corresponding target sequence, the main idea is to
apply one of the above-mentioned Transformer models, multiple times at multiple time
scales. At a given scale si, the input to the encoder is the original look-back window but
downsampled by a factor si using average pooling; the input to the decoder is given by the
model forecast at the previous scale si−1, but upsampled by a ﬁxed factor s through linear
interpolation. To mitigate error propagation and distribution shifts that are due to repeated
upsampling operations, the encoder and decoder’s inputs are ﬁrst normalised using Cross-
Scale Normalization. Finally, a loss function, based on an adaptive loss, is applied at each
time scale between the model forecast and the target sequence, which is also downsampled
by a factor si via average pooling. The Triformer [195] proposes a particular architecture that
integrates attention mechanisms and recurrent units to ensure high efﬁciency and accuracy.
The former is achieved by a patch attention mechanism with linear complexity; the latter is
obtained by using variable-speciﬁc parameters. The patch attention mechanism splits the input
sequence in P patches of length S and assigns a learnable pseudo-timestamp Tp to each patch.
When patch attention is applied, each pseudo-timestamp Tp is considered as a query Q for its
patch only. Moreover, variable-speciﬁc parameters are introduced by factorising the projection
matrices (i.e, WK and WV) into three matrices: left variable-agnostic matrix L ∈ RD ⊗ Ra,
middle variable-speciﬁc matrix B ∈ Ra ⊗ Ra and right variable-agnostic matrix R ∈ Ra ⊗ RD,
where a (cid:28) D. Finally, to cope with the limited temporal receptive ﬁeld that is due to
the patch mechanism, recurrent units are used to aggregate and control the information
for all pseudo-timestamps of each layer before the ﬁnal prediction. All above-mentioned
variants of Transformer share the over-stationarization problem that consists in the inability
to generate distinguishable attention scores when trained on stationarized series [196]. The
Non-stationary Transformer [196] proposes a generic framework to overcome the problem of
over-stationarization. This framework is composed of two interdependent modules: Series
Stationarization and De-stationary Attention. The former attenuates the non-stationarity of
the time series considered, using two sequential operations: Normalization module, which
computes the mean and the variance for each input time series in order to transform it
into a stationary time series, and a De-normalization module, which transforms the model
outputs back into a non-stationary time series, using the mean and variance computed in
the previous module. The latter is a novel attention mechanism, which can approximate
the attention scores that are obtained without stationarization and discover the particular
temporal dependencies from original non-stationary data. Transformer variants for time
series forecasting are described in detail in Table 12. Further details on each Transformer
variant, can be found in the original paper that presents the architecture.

Table 12. Recent variants of Transformer architecture for time series forecasting.

Ref.

[188]
[182]
[183]
[184]
[193]
[195]
[196]
[191]
[192]
[194]

Year

2019
2021
2021
2022
2022
2022
2022
2023
2023
2023

Model

LogTrans
Informer
Autoformer
FEDFormer
Pyraformer
Triformer
Non-stationary Transfomers
PatchTST
Crossformer
Scaleformer

Table 13 reports an extensive comparison among all aforementioned Transformer
variants. It has to be noted that, the reported results were collected from the original papers
that tested a given model on a given data set (the reader can refer to the GitHub pages
linked in the original papers of each architecture for reproducing the experiments, using
the original experimental setups).

---

<!-- PAGE 22 -->

Information 2023, 14, 598

22 of 35

Table 13. Multivariate long-term forecasting benchmarks among variant of Transformer architectures with different prediction lengths P ∈ [96, 192, 336, 720]. The
input length considered for ILI data set is 36 and 96 for the others. A lower MSE or MAE indicates a better prediction. The best results, for each data sets, are
highlighted in bold.

Crossformer

PatchTST

Non-Stationary

Pyraformer

FEDFormer

Autoformer

Informer

LogTrans

LSTM

TCN

MSE MAE MSE MAE MSE MAE MSE MAE MSE MAE MSE MAE MSE MAE MSE MAE MSE MAE MSE MAE
0.589
0.600
0.608
0.610
0.784
0.794
0.799
0.804
0.813
0.821
0.824
0.784
1.830
1.879
1.892
1.918
1.330
1.339
1.348
1.354

0.266
0.307
0.359
0.419
0.613
0.616
0.622
0.660
0.201
0.222
0.231
0.254
3.483
3.103
2.669
2.770
0.255
0.281
0.339
0.422

0.369
0.416
0.455
0.535
0.843
0.847
0.853
0.500
0.375
0.442
0.439
0.980
5.914
6.631
6.736
6.870
2.041
2.249
2.568
2.720

0.296
0.336
0.380
0.482
0.349
0.346
0.323
0.368
0.297
0.308
0.313
0.343
0.963
0.976
0.981
1.061
0.287
0.328
0.366
0.415

0.490
0.589
0.652
0.675
0.384
0.390
0.408
0.396
0.357
0.368
0.380
0.376
1.444
1.467
1.468
1.560
0.642
0.757
0.872
1.328

0.300
0.598
0.578
1.059
0.719
0.696
0.777
0.864
0.274
0.296
0.300
0.373
5.764
4.755
4.763
5.264
0.365
0.533
1.363
3.379

0.406
0.435
0.454
0.520
0.453
0.453
0.455
0.805
0.437
0.473
0.473
0.814
1.734
1.845
1.857
1.879
1.073
1.112
1.238
1.287

0.615
0.629
0.639
0.639
1.438
1.463
1.479
1.499
0.985
0.996
1.000
1.438
6.624
6.858
6.968
7.127
3.041
3.072
3.105
3.153

0.392
0.597
0.592
0.723
0.393
0.394
0.396
0.404
0.299
0.312
0.326
0.372
1.693
1.733
1.763
1.814
0.488
0.641
0.846
1.526

0.217
0.276
0.339
0.403
0.562
0.562
0.570
0.596
0.183
0.195
0.212
0.231
2.203
2.272
2.209
2.545
0.203
0.269
0.325
0.421

0.384
0.544
0.523
0.741
0.391
0.379
0.420
0.472
0.368
0.386
0.394
0.439
1.677
1.467
1.469
1.564
0.453
0.563
0.887
1.388

0.458
0.658
0.797
0.869
0.684
0.685
0.733
0.717
0.258
0.266
0.280
0.283
4.480
4.799
4.800
5.278
0.768
0.989
1.334
3.048

0.354
0.673
0.634
0.942
0.684
0.692
0.699
0.712
0.498
0.828
1.476
4.090
5.800
6.043
6.213
6.531
0.409
0.673
1.210
4.044

0.336
0.367
0.395
0.428
0.388
0.382
0.337
0.408
0.317
0.334
0.338
0.361
1.287
1.148
1.085
1.125
0.339
0.340
0.372
0.419

0.198
0.241
0.282
0.334
0.249
0.256
0.264
0.286
0.222
0.240
0.159
0.290
0.754
0.870
0.815
0.788
0.256
0.296
0.329
0.385

0.173
0.245
0.321
0.414
0.612
0.613
0.618
0.653
0.169
0.182
0.200
0.222
2.294
1.825
2.010
2.178
0.192
0.280
0.334
0.417

0.223
0.285
0.338
0.410
0.338
0.340
0.328
0.355
0.273
0.286
0.304
0.321
0.945
0.848
0.900
0.963
0.274
0.339
0.361
0.413

-
-
0.515
0.542
-
-
0.300
0.313
-
-
0.369
0.423
1.186
1.232
1.221
1.305
-
-
-
-

0.149
0.194
0.245
0.314
0.360
0.379
0.392
0.432
0.129
0.147
0.163
0.197
1.319
1.579
1.553
1.470
0.166
0.223
0.274
0.362

-
-
0.495
0.526
-
-
0.530
0.573
-
-
0.323
0.404
3.041
3.406
3.459
3.640
-
-
-
-

Models

Metric

r
e
h
t
a
e
W

c
ﬁ
f
a
r
T

y
t
i
c
i
r
t
c
e
l
E

I
L
I

2
m
T
T
E

96
192
336
720
96
192
336
720
96
192
336
720
24
36
48
60
96
192
336
720

---

<!-- PAGE 23 -->

Information 2023, 14, 598

23 of 35

5. Other Relevant Deep Learning Models

This section is reserved for those works that propose interesting architectures for
short-term and long-term time series forecasting which do not ﬁt the previously deﬁned
categories. Even though these models might share the same building blocks of well-known
architectures (e.g., CNN, TCN, RNN, Transformer), due to their peculiarity and hetero-
geneity it has been decided to collect them under a proper section. In [197] a Continuous
Recurrent Unit (CRU) based on stochastic differential equations (SDEs) and Kalman ﬁlters,
that can handle irregularly sampled time series, is proposed. The FiLM (Frequency-improved
Legendre Memory) model [198] generates a representation of past time series samples by
Legendre projections. It uses a noise reduction module based on Fourier analysis to preserve
only relevant information from previous time samples, reducing the effect that noisy signals
can have on time series forecasting. In [199], it shows how a time series forecasting model
fully based on MLP can compare competitively with state-of-the-art Transformer models
(e.g., PatchTST [191]), reducing, in this way, the forecasting computational cost. In detail, it
proposes an adaption (TSMixer) of MLP-Mixer, originally proposed for the vision domain,
for time series forecasting. A convolution-based architecture, MICN (Multi-scale Isometric
Convolution Network) [200], can discover local patterns and global correlations in time series
by using a multi-branch structure and relying on downsampled 1D convolutions to extract local
features and isometric convolutions, a particular case of causal convolution (see Section 3.1.2),
to discover global correlations. Table 14 summarises the aforementioned models.

Table 14. Recent applications on time series forecasting using other deep learning architectures.

Ref.

[197]
[198]
[199,200]

Year

2022
2022
2023

Application

Climate data/Electronic Health Records
Long-term benchmark data sets (see Section 6.2)
Long-term benchmark data sets (see Section 6.2)

6. Benchmarks for Time Series Forecasting

Recently, a group of time series have emerged as benchmarks for assessing the perfor-
mance of machine learning models in time series forecasting tasks. This section describes
the most relevant benchmarks for both short and long-term forecasting.

6.1. Benchmarks for Short-Term Forecasting

Among several different data sets used for short-term forecasting, the most popular
ones are described in Table 15. It is worth quoting the M4 data set [44], proposed in 2020 for
the homonymous M4 competition as a common benchmark for evaluating the performance
of short-term forecasting models. The M4 data set contains 100.000 time series subdivided
according to their data frequency into six groups: M4-Yearly, M4-Quarterly, M4-Monthly,
M4-Weekly, M4-Daily and M4-Hourly. Furthermore, time series are also categorised into six
domains, namely, Demographic, Finance, Industry, Macro, Micro and Other. Some insights on
how time series are distributed into these categories are given in Figure 12.

Table 15. Short-term forecasting data sets. The column Dim refers to the dimensionality of time series.

Dataset

M4-Yearly [44]
M4-Quarterly [44]
M4-Monthly [44]
M4-Weekly [44]
M4-Daily [44]
M4-Hourly [44]
Mackey-Glass [201]
DatasetA [202]
DSVC1 [203]
Paris-14E [204]
DatasetD [205]

Dim

Data Type (Real/Synthetic)

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

Real
Real
Real
Real
Real
Real
Synthetic
Real
Real
Real
Synthetic

---

<!-- PAGE 24 -->

Information 2023, 14, 598

24 of 35

(a) M4-Monthly data set composition.

(b) M4-Yearly data set composition.

(c) M4-Competition data set composition.
Figure 12. Composition of the M4 data set. (a,b) show, respectively, the distribution of M4-Monthly
and M4-Yearly time series into the six M4 categories. (c) shows the number of time series in each of
the M4 data sets.

6.2. Benchmarks for Long-Term Forecasting

Nowadays, a group of speciﬁc data sets has become the de-facto benchmark [183] to
assess long-term forecasting accuracy of all Transformer variants presented in Section 4.1.4.
In detail, this benchmark is composed of nine multivariate time series data sets concerning
the following domains: electricity, transportation, weather, exchange rate and illness (see
Table 16). Time resolution can vary from 10 min up to 7 days.

Table 16. Long-term forecasting benchmark data sets. The data set size (·, ·, ·) refers to the car-
dinality of training, validation and test set, respectively. The columns dim, pred len and time res
refer to the dimensionality of time series, the number of predicted future samples and the time
resolution, respectively.

Dataset

Dim

Pred Len

Dataset Size

Time Res

Domain

ETTm1
ETTm2
ETTh1
ETTh2
Electricity
Trafﬁc
Weather
Exchange
ILI

7
7
7
7
321
862
21
8
7

[96,192,336,720]
[96,192,336,720]
[96,192,336,720]
[96,192,336,720]
[96,192,336,720]
[96,192,336,720]
[96,192,336,720]
[96,192,336,720]
[24,36,48,60]

(34,465, 11,521, 11,521)
(34,465, 11,521, 11,521)
(8545, 2881, 2881)
(8545, 2881, 2881)
(18,317, 2633, 5261)
(12,185, 1757, 3509)
(36,792, 5271, 10,540)
(5120, 665, 1422)
(617, 74, 170)

15 mins
15 mins
15 mins
15 mins
1 h
1 h
10 mins
1 day
1 week

Electricity
Electricity
Electricity
Electricity
Electricity
Transport
Weather
Finance
Illness

7. Conclusions

The paper has reviewed deep learning architectures for time series forecasting, un-
derlining their advances. Nevertheless, four major problems remain open. The ﬁrst one
resides in the inability of most deep learning methods, with the exception of Deep Gaussian
Processes, to estimate a conﬁdence interval for the time series prediction. In principle, all
deep learning architectures quoted in the survey can be properly modiﬁed using Bayesian
training strategies [206] in order to provide the uncertainty of the model prediction, but, to
the best of our knowledge, it has not been performed yet. The second problem resides in

---

<!-- PAGE 25 -->

Information 2023, 14, 598

25 of 35

the development of more and more complex deep learning architectures. This makes them
subject to overﬁtting, a problem that can hardly be faced by deep learning architectures.
Therefore, the development of deep learning architectures for time series forecasting that
are robust w.r.t. overﬁtting is becoming more and more relevant. The third problem consists
in the need for adequately long time series. In particular, some deep learning architectures,
e.g., Transformers, require the estimation of millions of parameters, implying, in this way,
the necessity of adequately long time series for estimating them. The problem seems to
be partially addressed by data augmentation but the proposed solutions are not fully
adequate, yet. Finally, the last problem emerges in most of the reviewed deep learning
models. They assume the dynamical stationarity of time series, implying that the dynamic
system generating time series is stationary over time. When the aforementioned assump-
tion is violated, a concept drift phenomenon [207] in time series is observed, consequently
leading to a dramatic decrease in the prediction accuracy of deep learning models for time
series forecasting.

Author Contributions: Conceptualization, A.C., V.C. and F.C.; methodology, A.C. and V.C.; valida-
tion, A.C., V.C. and F.C.; formal analysis, F.C.; investigation, A.C., V.C. and G.I.; resources, A.C., V.C.,
G.I. and F.C.; writing—original draft preparation, A.C., V.C. and F.C.; writing—review and editing,
A.C., V.C. and F.C.; visualization, A.C., V.C. and F.C.; supervision, F.C.; project administration, F.C.
All authors have read and agreed to the published version of the manuscript.

Funding: This research received no external funding.

Data Availability Statement: No new data were created or analyzed in this study. Data sharing is
not applicable to this article.

Acknowledgments: We would like to thank the anonymous reviewers for the useful comments.

Conﬂicts of Interest: The authors declare no conﬂict of interest.

Appendix A. Table of Mathematical Expressions

In Appendix A, the table of the most frequent mathematical expressions and operations

is provided. Table A1 provides a description for each mathematical operation.

Table A1. Table of the most commonly used mathematical operations with their respective description.

Symbol

Deﬁnition

Y = w ∗ X

Convolution between a kernel w and a sequence X . The result is a new sequence Y.

(cid:126)y = (cid:126)u (cid:12) (cid:126)v

V ⊗ W
I

Element-wise product between two vectors (cid:126)u and (cid:126)v. The result is a vector (cid:126)y such
that yi = uivi.

Tensor product between two vectors V and W, the result is a matrix.

The Identity matrix.

Appendix B. Diffusion Models

In this section, the most relevant diffusion models, i.e., DDPMs (Appendix B.1), SGMs

(Appendix B.2) and SDEs (Appendix B.3), and foundations, are described.

Appendix B.1. Denoising Diffusion Probabilistic Models

Denoising Diffusion Probabilistic Models, originally proposed in [173] and later extended
in [174], consider two Markov chains for forward and backward process, respectively, to
approximate the generative process of observed data. In detail, let the original noiseless data
be x0. The forward Markov chain projects x0 into a sequence of noised data x1, x2, . . . , xK
with a diffusion transition kernel:

q(xk|xk−1) = N (

√

akxk−1, (1 − ak)I),

(A1)

---

<!-- PAGE 26 -->

Information 2023, 14, 598

26 of 35

where K is the ﬁnite number of noise level of forward process, ak ∈ (0, 1) for k = 1, 2, . . . , K
are hyperparameters indicating the variance of the noise level at each step, N (·, ·) is the
Gaussian distribution, and I is the identity matrix. The Gaussian transition kernel q(·|·)
has a fundamental property that allows obtaining xk directly from original sample x0:

q(xk|x0) = N ((cid:112)

˜akx0, (1 − ˜ak)I),

(A2)

where ˜ak = ∏k
neural network:

i=1 ai. In DDPM, the reverse transition kernel pθ(·|·) is designed by a deep

pθ(xk−1|xk) = N (µθ(xk, k), Σ

θ(xk, k)),

(A3)

where θ indicates learnable parameters of deep neural networks. In order to compute the
parameters θ such that samples estimated by pθ(x0) are almost identical to observed data
x0, a maximum likelihood estimation method is performed, minimising the variational lower
bound of the estimated negative log-likelihood E[− log pθ(x0)]:

E[− log pθ(x0)] = E

q(x0:K)

− log p(xK) −

(cid:34)

K
∑
k=1

log

pθ(xk−1|xk)
q(xk|xk−1)

(cid:35)

,

(A4)

where x0:K indicates the sequence x0, . . . , xK. A simpler objective function [174] can be
provided, as follows:

E

k,x0,(cid:101)[δ(k)||(cid:101) − (cid:101)θ((cid:112)

˜akx0 + (cid:112)

1 − ˜ak(cid:101), k)||2],

(A5)

assuming the covariance matrix equal to Σ
and may vary at different reverse steps, and δ(k) = (1−ak)2

θ(xk, k) = σ2
k

I, where σ2
k ak(1− ˜ak) .
2σ2

k controls the noise level

Appendix B.2. Score-Based Generative Models

Score-based generative models (SGMs) [175], are made up of two modules. The former is
the score matching module [208], for estimating the unknown target distribution q(x) with the
Stein score approximation, ∇x log q(x), by means of a score-matching network (e.g., denoising
score matching [209], slided score matching [210]). The latter is the annealed Langevin dynamics
(ALD), that is a sampling algorithm generating samples with an iterative Langevin Monte
Carlo process at each update step. The fundamental idea behind denoising score matching is
I), and
to process the observed data x0 with the forward transition kernel q(xk|x0) = N (x0, σ2
k
to estimate jointly the Stein scores for the noise density distributions qσ1 (x), qσ2 (x), . . . , qσk (x).
In this case, the Stein score for noise density function qσk (x) is ∇x log qσk (x). Hence, a neural
network sθ(x, σx), with learnable parameters θ, can approximate the Stein score. The initial
objective function is therefore given by:

E

k,x0,xk [δ(k)||sθ(xk, k) − ∇k

x log qσk (xk)||2].

(A6)

Subsequently, the ALD algorithm is used for the sampling phase. The algorithm is
initialised with a sequence of increasing noise levels σ1, . . . , σK and a starting sample
xK,0 ∼ N (0, I). For k = K, K − 1, . . . , 0, xk is updated with N iterations that compute:

z ← N (0, I)

xk,n ← xk,n−1 +

ψksθ(xk,n−1, σk) + (cid:112)

ψkz,

1
2

where n = 1, . . . , N and ψk represent the step of update.

(A7)

(A8)

---

<!-- PAGE 27 -->

Information 2023, 14, 598

27 of 35

Appendix B.3. Stochastic Differential Equations

As described in Appendices B.1 and B.2, both DDPMs and SGMs models deﬁne a
discrete forward process, considering N iterations of diffusion steps. In order to deﬁne a
continuous diffusion process, a solution based on stochastic differential equations (SDEs) [176]
has been proposed. Since both DDPMs and SGMs are discrete forms of SDEs, the SDEs
formulation can be considered as an extension of the aforementioned two deﬁnitions.
Therefore, the backward process is modelled as a time-reverse SDE (see Equation (A10)), and
the samples can be generated by solving time-reverse SDE. A general expression of SDE is
deﬁned as follows:

and the time-reverse SDE [211] is:

dx = f (x, k)dk + g(k)dw,

dx = [ f (x, k) − g(k)2∇x log qk(x)]dk + g(k)d ˜w,

(A9)

(A10)

where w and ˜w are standard Wiener processes [212]. It can be proved [176] that the sampling
from the probability ﬂow ordinary differential equations (ODE) yields the same distribution of
the time-reverse SDE:

dx = [ f (x, k) −

1
2

g(x)∇x log qk(x)]dk,

(A11)

where f (x, k) and g(k) are the drift and diffusion coefﬁcients for the diffusion process, re-
spectively, and ∇x log qk(x) is the Stein score that can be learned with similar methods as
in SGMs (see Appendix B.2). At this point, it can observed that the DDPMs can be refor-
mulated in terms of SDEs, that generally known as variance preserving (VP) SDE [176]. The
same reformulation can be done for the forward process of SGMs, where the corresponding
SDE is known as variance exploding (VE) SDE [176]. After having learned the score model
sθ(x, k), the samples are generated by solving the time-reverse SDE or the probability ﬂow
ODE with ALD techniques.

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

Chianese, E.; Camastra, F.; Ciaramella, A.; Landi, T.C.; Staiano, A.; Riccio, A. Spatio-temporal learning in predicting ambient
particulate matter concentration by multi-layer perceptron. Ecol. Inform. 2019, 49, 54–61. [CrossRef]
Feng, Y.; Zhang, W.; Sun, D.; Zhang, L. Ozone concentration forecast method based on genetic algorithm optimized back
propagation neural networks and support vector machine data classiﬁcation. Atmos. Environ. 2011, 45, 1979–1985. [CrossRef]
Paine, C.T.; Marthews, T.R.; Vogt, D.R.; Purves, D.; Rees, M.; Hector, A.; Turnbull, L.A. How to ﬁt nonlinear plant growth models
and calculate growth rates: An update for ecologists. Methods Ecol. Evol. 2012, 3, 245–256. [CrossRef]
Pala, Z.; Atici, R. Forecasting sunspot time series using deep learning methods. Sol. Phys. 2019, 294, 50. [CrossRef]
Duarte, F.B.; Tenreiro Machado, J.; Monteiro Duarte, G. Dynamics of the Dow Jones and the NASDAQ stock indexes. Nonlinear
Dyn. 2010, 61, 691–705. [CrossRef]
Binkowski, M.; Marti, G.; Donnat, P. Autoregressive convolutional neural networks for asynchronous time series. In Proceedings
of the International Conference on Machine Learning, Stockholm, Sweden, 10–15 July 2018; pp. 580–589.
Ugurlu, U.; Oksuz, I.; Tas, O. Electricity price forecasting using recurrent neural networks. Energies 2018, 11, 1255. [CrossRef]
Kuan, L.; Yan, Z.; Xin, W.; Yan, C.; Xiangkun, P.; Wenxue, S.; Zhe, J.; Yong, Z.; Nan, X.; Xin, Z. Short-term electricity load
forecasting method based on multilayered self-normalising GRU network. In Proceedings of the 2017 IEEE Conference on Energy
Internet and Energy System Integration (EI2), Beijing, China, 26–28 November 2017; pp. 1–5.
Zhu, R.; Liao, W.; Wang, Y. Short-term prediction for wind power based on temporal convolutional network. Energy Rep. 2020,
6, 424–429. [CrossRef]

10. Koprinska, I.; Wu, D.; Wang, Z. Convolutional neural networks for energy time series forecasting. In Proceedings of the 2018

International Joint Conference on Neural Networks (IJCNN), Rio de Janeiro, Brazil, 8–13 July 2018; pp. 1–8.

11. Li, D.; Jiang, F.; Chen, M.; Qian, T. Multi-step-ahead wind speed forecasting based on a hybrid decomposition method and

temporal convolutional networks. Energy 2022, 238, 121981. [CrossRef]

12. Narigina, M.; Kempleis, A.; Romanovs, A. Machine Learning-based Forecasting of Sensor Data for Enhanced Environmental

Sensing. Wseas Trans. Syst. 2013, 22, 543–555. [CrossRef]

13. Han, M.; Xu, M. Laplacian echo state network for multivariate time series prediction. IEEE Trans. Neural Netw. Learn. Syst. 2017,

29, 238–244. [CrossRef]

---

<!-- PAGE 28 -->

Information 2023, 14, 598

28 of 35

14. Kumar, D.; Singh, A.; Samui, P.; Jha, R.K. Forecasting monthly precipitation using sequential modelling. Hydrol. Sci. J. 2019,

64, 690–700. [CrossRef]

15. Wan, R.; Mei, S.; Wang, J.; Liu, M.; Yang, F. Multivariate temporal convolutional network: A deep neural networks approach for

multivariate time series forecasting. Electronics 2019, 8, 876. [CrossRef]

16. Liu, H.; Zhang, X. AQI time series prediction based on a hybrid data decomposition and echo state networks. Environ. Sci. Pollut.

Res. 2021, 28, 51160–51182. [CrossRef] [PubMed]

17. Akita, R.; Yoshihara, A.; Matsubara, T.; Uehara, K. Deep learning for stock prediction using numerical and textual information.
In Proceedings of the 2016 IEEE/ACIS 15th International Conference on Computer and Information Science (ICIS), Okayama,
Japan, 26–29 June 2016; pp. 1–6.

18. Pang, X.; Zhou, Y.; Wang, P.; Lin, W.; Chang, V. An innovative neural network approach for stock market prediction.

J.

Supercomput. 2020, 76, 2098–2118. [CrossRef]

19. Zhang, L.; Aggarwal, C.; Qi, G.J. Stock price prediction via discovering multi-frequency trading patterns. In Proceedings of the
23rd ACM SIGKDD International Conference on Knowledge Discovery and Data Mining, Halifax, NS, Canada, 13–17 August
2017; pp. 2141–2149.

20. McNally, S.; Roche, J.; Caton, S. Predicting the price of bitcoin using machine learning. In Proceedings of the 2018 26th Euromicro
International Conference on Parallel, Distributed and Network-Based Processing (PDP), Cambridge, UK, 21–23 March 2018;
pp. 339–343.

21. Ye, J.; Liu, Z.; Du, B.; Sun, L.; Li, W.; Fu, Y.; Xiong, H. Learning the evolutionary and multi-scale graph structure for multivariate
In Proceedings of the 28th ACM SIGKDD Conference on Knowledge Discovery and Data Mining,

time series forecasting.
Washington, DC, USA, 14–18 August 2022; pp. 2296–2306.

22. Chen, L.; Chen, D.; Shang, Z.; Wu, B.; Zheng, C.; Wen, B.; Zhang, W. Multi-Scale Adaptive Graph Neural Network for Multivariate

23.

Time Series Forecasting. IEEE Trans. Knowl. Data Eng. 2023, 35, 10748–10761. [CrossRef]
Song, Y.; Gao, S.; Li, Y.; Jia, L.; Li, Q.; Pang, F. Distributed attention-based temporal convolutional network for remaining useful
life prediction. IEEE Internet Things J. 2020, 8, 9594–9602. [CrossRef]

24. Alhassan, Z.; McGough, A.S.; Alshammari, R.; Daghstani, T.; Budgen, D.; Al Moubayed, N. Type-2 diabetes mellitus diagnosis
from time series clinical data using deep learning models. In Proceedings of the Artiﬁcial Neural Networks and Machine Learning–
ICANN 2018: 27th International Conference on Artiﬁcial Neural Networks, Rhodes, Greece, 4–7 October 2018; Proceedings, Part
III 27; Springer: Berlin/Heidelberg, Germany, 2018; pp. 468–478.

25. Kim, T.; King, B.R. Time series prediction using deep echo state networks. Neural Comput. Appl. 2020, 32, 17769–17787. [CrossRef]
26. Lim, B. Forecasting treatment responses over time using recurrent marginal structural networks. Adv. Neural Inf. Process. Syst.

2018, 31.

27. Huang, S.; Wang, D.; Wu, X.; Tang, A. Dsanet: Dual self-attention network for multivariate time series forecasting. In Proceedings
of the 28th ACM International Conference on Information and Knowledge Management, Beijing, China, 3–7 November 2019;
pp. 2129–2132.

28. Wu, Z.; Pan, S.; Long, G.; Jiang, J.; Chang, X.; Zhang, C. Connecting the dots: Multivariate time series forecasting with graph
neural networks. In Proceedings of the 26th ACM SIGKDD International Conference on Knowledge Discovery & Data Mining,
Virtual, 6–10 July 2020; pp. 753–763.

29. Cui, Y.; Zheng, K.; Cui, D.; Xie, J.; Deng, L.; Huang, F.; Zhou, X. METRO: A generic graph neural network framework for

multivariate time series forecasting. Proc. Vldb Endow. 2021, 15, 224–236. [CrossRef]

30. Zhao, W.; Gao, Y.; Ji, T.; Wan, X.; Ye, F.; Bai, G. Deep temporal convolutional networks for short-term trafﬁc ﬂow forecasting.

31.

32.

IEEE Access 2019, 7, 114496–114507. [CrossRef]
Sagheer, A.; Kotb, M. Time series forecasting of petroleum production using deep LSTM recurrent networks. Neurocomputing
2019, 323, 203–213. [CrossRef]
Sánchez, L.; Anseán, D.; Otero, J.; Couso, I. Assessing the health of LiFePO4 traction batteries through monotonic echo state
networks. Sensors 2017, 18, 9. [CrossRef] [PubMed]

33. Zhang, Y.; Xiong, R.; He, H.; Pecht, M.G. Long short-term memory recurrent neural network for remaining useful life prediction

of lithium-ion batteries. IEEE Trans. Veh. Technol. 2018, 67, 5695–5705. [CrossRef]

34. Colla, V.; Matino, I.; Dettori, S.; Cateni, S.; Matino, R. Reservoir computing approaches applied to energy management in industry.
In Proceedings of the Engineering Applications of Neural Networks: 20th International Conference, EANN 2019, Xersonisos,
Crete, Greece, 24–26 May 2019; Proceedings 20; Springer: Berlin/Heidelberg, Germany, 2019; pp. 66–79.

35. Li, Z.; Zheng, Z.; Outbib, R. Adaptive prognostic of fuel cells by implementing ensemble echo state networks in time-varying

model space. IEEE Trans. Ind. Electron. 2019, 67, 379–389. [CrossRef]

36. Bala, A.; Ismail, I.; Ibrahim, R.; Sait, S.M.; Oliva, D. An improved grasshopper optimization algorithm based echo state network

for predicting faults in airplane engines. IEEE Access 2020, 8, 159773–159789. [CrossRef]

37. Mahmoud, A.; Mohammed, A. A survey on deep learning for time series forecasting. In Machine Learning and Big Data Analytics

Paradigms: Analysis, Applications and Challenges; Springer: Cham, Switzerland, 2021; pp. 365–392.

38. Lim, B.; Zohren, S. Time-series forecasting with deep learning: A survey. Philos. Trans. R. Soc. 2021, 379, 20200209. [CrossRef]

[PubMed]

---

<!-- PAGE 29 -->

Information 2023, 14, 598

29 of 35

39.

Sezer, O.B.; Gudelek, M.U.; Ozbayoglu, A.M. Financial time series forecasting with deep learning: A systematic literature review:
2005–2019. Appl. Soft Comput. 2020, 90, 106181. [CrossRef]

40. Zeroual, A.; Harrou, F.; Dairi, A.; Sun, Y. Deep learning methods for forecasting COVID-19 time-Series data: A Comparative

study. Chaos Solitons Fractals 2020, 140, 110121. [CrossRef]

41. Lara-Benítez, P.; Carranza-García, M.; Riquelme, J.C. An experimental review on deep learning architectures for time series

forecasting. Int. J. Neural Syst. 2021, 31, 2130001. [CrossRef]

42. Barrera-Animas, A.Y.; Oyedele, L.O.; Bilal, M.; Akinosho, T.D.; Delgado, J.M.D.; Akanbi, L.A. Rainfall prediction: A comparative
analysis of modern machine learning algorithms for time series forecasting. Mach. Learn. Appl. 2022, 7, 100204. [CrossRef]
43. Lakshmanna, K.; Kaluri, R.; Gundluru, N.; Alzamil, Z.S.; Rajput, D.S.; Khan, A.A.; Haq, M.A.; Alhussen, A. A review on deep

learning techniques for IoT data. Electronics 2022, 11, 1604. [CrossRef]

44. Makridakis, S.; Spiliotis, E.; Assimakopoulos, V. The M4 Competition: 100,000 time series and 61 forecasting methods. Int. J.

Forecast. 2020, 36, 54–74. [CrossRef]

45. Goodfellow, I.; Bengio, Y.; Courville, A. Deep Learning; MIT Press: Cambridge, MA, USA, 2016.
46. Hastie, T.; Tibshirani, R.; Friedman, J.H.; Friedman, J.H. The Elements of Statistical Learning: Data Mining, Inference, and Prediction;

Springer: Berlin/Heidelberg, Germany, 2009; Volume 2.

47. Gudelek, M.U.; Boluk, S.A.; Ozbayoglu, A.M. A deep learning based stock trading model with 2-D CNN trend detection. In
Proceedings of the 2017 IEEE Symposium Series on Computational Intelligence (SSCI), Honolulu, HI, USA, 27 November–1
December 2017; pp. 1–8.

48. Kuo, P.H.; Huang, C.J. A high precision artiﬁcial neural networks model for short-term energy load forecasting. Energies 2018,

11, 213. [CrossRef]

49. Zahid, M.; Ahmed, F.; Javaid, N.; Abbasi, R.A.; Zainab Kazmi, H.S.; Javaid, A.; Bilal, M.; Akbar, M.; Ilahi, M. Electricity price and
load forecasting using enhanced convolutional neural network and enhanced support vector regression in smart grids. Electronics
2019, 8, 122. [CrossRef]

50. Cai, M.; Pipattanasomporn, M.; Rahman, S. Day-ahead building-level load forecasts using deep learning vs. traditional time

series techniques. Appl. Energy 2019, 236, 1078–1088. [CrossRef]

51. Bronstein, M.M.; Bruna, J.; LeCun, Y.; Szlam, A.; Vandergheynst, P. Geometric deep learning: Going beyond euclidean data. IEEE

Signal Process. Mag. 2017, 34, 18–42. [CrossRef]

52. Lea, C.; Flynn, M.D.; Vidal, R.; Reiter, A.; Hager, G.D. Temporal convolutional networks for action segmentation and detection.
In Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition, Virtual, 6–10 July 2017; pp. 156–165.
53. Borovykh, A.; Bohte, S.; Oosterlee, C.W. Dilated convolutional neural networks for time series forecasting. J. Comput. Financ.

Forthcom. 2018. [CrossRef]

54. Lara-Benítez, P.; Carranza-García, M.; Luna-Romera, J.M.; Riquelme, J.C. Temporal convolutional networks applied to energy-

related time series forecasting. Appl. Sci. 2020, 10, 2322. [CrossRef]

55. Hewage, P.; Behera, A.; Trovati, M.; Pereira, E.; Ghahremani, M.; Palmieri, F.; Liu, Y. Temporal convolutional neural (TCN) network
for an effective weather forecasting using time series data from the local weather station. Soft Comput. 2020, 24, 16453–16482.
[CrossRef]
Sfetsos, A.; Coonick, A. Univariate and multivariate forecasting of hourly solar radiation with artiﬁcial intelligence techniques.
Sol. Energy 2000, 68, 169–178. [CrossRef]

56.

57. Hsieh, T.J.; Hsiao, H.F.; Yeh, W.C. Forecasting stock markets using wavelet transforms and recurrent neural networks: An

integrated system based on artiﬁcial bee colony algorithm. Appl. Soft Comput. 2011, 11, 2510–2525. [CrossRef]

58. Elman, J.L. Finding structure in time. Cogn. Sci. 1990, 14, 179–211. [CrossRef]
59.

Jaeger, H. The “echo state” approach to analysing and training recurrent neural networks-with an erratum note. Bonn Ger. Ger.
Natl. Res. Cent. Inf. Technol. Gmd Tech. Rep. 2001, 148, 13.

60. Hochreiter, S.; Schmidhuber, J. Long short-term memory. Neural Comput. 1997, 9, 1735–1780. [CrossRef]
61. Cho, K.; van Merrienboer, B.; Gulcehre, C.; Bahdanau, D.; Bougares, F.; Schwenk, H.; Bengio, Y. Learning Phrase Representations
using RNN Encoder–Decoder for Statistical Machine Translation. In Proceedings of the 2014 Conference on Empirical Methods in
Natural Language Processing (EMNLP), Doha, Qatar, 25–29 October 2014; Association for Computational Linguistics: Cedarville,
OH, USA, 2014; p. 1724.

62. Williams, R.J.; Zipser, D. A learning algorithm for continually running fully recurrent neural networks. Neural Comput. 1989,

63.

64.

1, 270–280. [CrossRef]
Jordan, M.I. Serial order: A parallel distributed processing approach. In Advances in Psychology; Elsevier: Amsterdam, The
Netherlands, 1997; Volume 121, pp. 471–495.
Shi, H.; Xu, M.; Ma, Q.; Zhang, C.; Li, R.; Li, F. A whole system assessment of novel deep learning approach on short-term load
forecasting. Energy Procedia 2017, 142, 2791–2796. [CrossRef]

65. Mohammadi, M.; Talebpour, F.; Safaee, E.; Ghadimi, N.; Abedinia, O. Small-scale building load forecast based on hybrid forecast

engine. Neural Process. Lett. 2018, 48, 329–351. [CrossRef]

66. Ruiz, L.G.B.; Rueda, R.; Cuéllar, M.P.; Pegalajar, M. Energy consumption forecasting based on Elman neural networks with

evolutive optimization. Expert Syst. Appl. 2018, 92, 380–389. [CrossRef]

67. Bishop, C.M. Neural Networks for Pattern Recognition; Oxford University Press: Oxford, UK, 1995.

---

<!-- PAGE 30 -->

Information 2023, 14, 598

30 of 35

68. Kantz, H.; Schreiber, T. Nonlinear Time Series Analysis; Cambridge University Press: Cambridge, UK, 2004; Volume 7.
69.

Simonyan, K.; Vedaldi, A.; Zisserman, A. Deep inside convolutional networks: Visualising image classiﬁcation models and
saliency maps. arXiv 2013, arXiv:1312.6034.
Selvaraju, R.R.; Cogswell, M.; Das, A.; Vedantam, R.; Parikh, D.; Batra, D. Grad-cam: Visual explanations from deep networks
via gradient-based localization. In Proceedings of the IEEE International Conference on Computer Vision, Venice, Italy, 22–29
October 2017; pp. 618–626.

70.

71. Morando, S.; Jemei, S.; Hissel, D.; Gouriveau, R.; Zerhouni, N. ANOVA method applied to proton exchange membrane fuel cell

ageing forecasting using an echo state network. Math. Comput. Simul. 2017, 131, 283–294. [CrossRef]

72. Antonelo, E.A.; Camponogara, E.; Foss, B. Echo state networks for data-driven downhole pressure estimation in gas-lift oil wells.

73.

74.

Neural Netw. 2017, 85, 106–117. [CrossRef] [PubMed]
Shen, L.; Chen, J.; Zeng, Z.; Yang, J.; Jin, J. A novel echo state network for multivariate and nonlinear time series prediction. Appl.
Soft Comput. 2018, 62, 524–535. [CrossRef]
Jing, Z.; Yuxi, L.; Yan, C.; Bao, Y.; Jiakui, Z.; Di, L. Photovoltaic Output Prediction Model Based on Echo State Networks with
Weather Type Index. In Proceedings of the 2019 3rd International Conference on Innovation in Artiﬁcial Intelligence, Suzhou,
China, 15–18 March 2019; pp. 91–95.

75. Hu, H.; Wang, L.; Peng, L.; Zeng, Y.R. Effective energy consumption forecasting using enhanced bagged echo state network.

Energy 2020, 193, 116778. [CrossRef]

76. Mansoor, M.; Grimaccia, F.; Mussetta, M. Echo State Network Performance in Electrical and Industrial Applications.

In

Proceedings of the 2020 International Joint Conference on Neural Networks (IJCNN), Glasgow, UK, 19–24 July 2020; pp. 1–7.

77. Hu, H.; Wang, L.; Lv, S.X. Forecasting energy consumption and wind power generation using deep echo state network. Renew.

Energy 2020, 154, 598–613. [CrossRef]

78. Yang, Y.; Zhao, X.; Liu, X. A novel echo state network and its application in temperature prediction of exhaust gas from hot blast

stove. IEEE Trans. Instrum. Meas. 2020, 69, 9465–9476. [CrossRef]

79. Li, N.; Tuo, J.; Wang, Y.; Wang, M. Prediction of blood glucose concentration for type 1 diabetes based on echo state networks

embedded with incremental learning. Neurocomputing 2020, 378, 248–259. [CrossRef]

80. Gao, R.; Du, L.; Duru, O.; Yuen, K.F. Time series forecasting based on echo state network and empirical wavelet transformation.

Appl. Soft Comput. 2021, 102, 107111. [CrossRef]

81. Mansoor, M.; Grimaccia, F.; Leva, S.; Mussetta, M. Comparison of echo state network and feed-forward neural networks in

82.

electrical load forecasting for demand response programs. Math. Comput. Simul. 2021, 184, 282–293. [CrossRef]
Sui, Y.; Gao, H. Modiﬁed echo state network for prediction of nonlinear chaotic time series. Nonlinear Dyn. 2022, 110, 3581–3603.
[CrossRef]

83. Marino, D.L.; Amarasinghe, K.; Manic, M. Building energy load forecasting using deep neural networks.

In Proceed-
ings of the IECON 2016—42nd Annual Conference of the IEEE Industrial Electronics Society, Florence, Italy, 23-26 October
2016; pp. 7046–7051.
Fu, R.; Zhang, Z.; Li, L. Using LSTM and GRU neural network methods for trafﬁc ﬂow prediction. In Proceedings of the 2016
31st Youth Academic Annual Conference of Chinese Association of Automation (YAC), Wuhan, China, 11–13 November 2016;
pp. 324–328.

84.

85. Li, Z.; Tam, V. Combining the real-time wavelet denoising and long-short-term-memory neural network for predicting stock
In Proceedings of the 2017 IEEE Symposium Series on Computational Intelligence (SSCI), Honolulu, HI, USA, 27

indexes.
November–1 December 2017; pp. 1–8.

86. dos Santos Pinheiro, L.; Dras, M. Stock market prediction with deep learning: A character-based neural language model for
event-based trading. In Proceedings of the Australasian Language Technology Association Workshop 2017, Brisbane, Australia,
6–8 December 2017; pp. 6–15.
Shi, H.; Xu, M.; Li, R. Deep learning for household load forecasting—A novel pooling deep RNN. IEEE Trans. Smart Grid 2017,
9, 5271–5280. [CrossRef]

87.

88. Li, X.; Peng, L.; Yao, X.; Cui, S.; Hu, Y.; You, C.; Chi, T. Long short-term memory neural network for air pollutant concentration

predictions: Method development and evaluation. Environ. Pollut. 2017, 231, 997–1004. [CrossRef] [PubMed]

89. Baek, Y.; Kim, H.Y. ModAugNet: A new forecasting framework for stock market index value with an overﬁtting prevention

90.

LSTM module and a prediction LSTM module. Expert Syst. Appl. 2018, 113, 457–480. [CrossRef]
Fischer, T.; Krauss, C. Deep learning with long short-term memory networks for ﬁnancial market predictions. Eur. J. Oper. Res.
2018, 270, 654–669. [CrossRef]

91. Kratzert, F.; Klotz, D.; Brenner, C.; Schulz, K.; Herrnegger, M. Rainfall–runoff modelling using Long Short-Term Memory (LSTM)

networks. Hydrol. Earth Syst. Sci. 2018, 22, 6005–6022. [CrossRef]

92. Zhang, J.; Zhu, Y.; Zhang, X.; Ye, M.; Yang, J. Developing a Long Short-Term Memory (LSTM) based model for predicting water

table depth in agricultural areas. J. Hydrol. 2018, 561, 918–929. [CrossRef]

93. Bouktif, S.; Fiaz, A.; Ouni, A.; Serhani, M.A. Optimal deep learning lstm model for electric load forecasting using feature selection

and genetic algorithm: Comparison with machine learning approaches. Energies 2018, 11, 1636. [CrossRef]

94. Xu, L.; Li, C.; Xie, X.; Zhang, G. Long-short-term memory network based hybrid model for short-term electrical load forecasting.

Information 2018, 9, 165. [CrossRef]

---

<!-- PAGE 31 -->

Information 2023, 14, 598

31 of 35

95. Wang, Y.; Shen, Y.; Mao, S.; Chen, X.; Zou, H. LASSO and LSTM integrated temporal model for short-term solar intensity

96.

forecasting. IEEE Internet Things J. 2018, 6, 2933–2944. [CrossRef]
Freeman, B.S.; Taylor, G.; Gharabaghi, B.; Thé, J. Forecasting air quality time series using deep learning. J. Air Waste Manag. Assoc.
(1995) 2018, 68, 866–886. [CrossRef]

97. Wang, Y.; Smola, A.; Maddix, D.; Gasthaus, J.; Foster, D.; Januschowski, T. Deep factors for forecasting. In Proceedings of the

International Conference on Machine Learning, Long Beach, CA, USA, 9–15 June 2019; pp. 6607–6617.

98. Nichiforov, C.; Stamatescu, G.; Stamatescu, I.; F˘ag˘ar˘a¸san, I. Evaluation of sequence-learning models for large-commercial-building

load forecasting. Information 2019, 10, 189. [CrossRef]

99. Zou, M.; Fang, D.; Harrison, G.; Djokic, S. Weather based day-ahead and week-ahead load forecasting using deep recurrent
neural network. In Proceedings of the 2019 IEEE 5th International forum on Research and Technology for Society and Industry
(RTSI), Florence, Italy, 9–12 September 2019; pp. 341–346.

100. Chimmula, V.K.R.; Zhang, L. Time series forecasting of COVID-19 transmission in Canada using LSTM networks. Chaos Solitons

Fractals 2020, 135, 109864. [CrossRef] [PubMed]

101. Wu, Y.; Ni, J.; Cheng, W.; Zong, B.; Song, D.; Chen, Z.; Liu, Y.; Zhang, X.; Chen, H.; Davidson, S.B. Dynamic gaussian mixture
based deep generative model for robust forecasting on sparse multivariate time series. In Proceedings of the AAAI Conference
on Artiﬁcial Intelligence, Virtual, 2–9 February 2021; Volume 35, pp. 651–659.

102. Dastgerdi, A.K.; Mercorelli, P. Investigating the effect of noise elimination on LSTM models for ﬁnancial markets prediction

using Kalman Filter and Wavelet Transform. WSEAS Trans. Bus. Econ. 2022, 19, 432–441. [CrossRef]

103. Wang, Y.; Liao, W.; Chang, Y. Gated recurrent unit network-based short-term photovoltaic forecasting. Energies 2018, 11, 2163.

[CrossRef]

104. Du, Y.; Wang, J.; Feng, W.; Pan, S.; Qin, T.; Xu, R.; Wang, C. Adarnn: Adaptive learning and forecasting of time series.

In
Proceedings of the 30th ACM International Conference on Information & Knowledge Management, Gold Coast, QLD, Australia,
1–5 November 2021; pp. 402–411.

105. Bollerslev, T. Generalized autoregressive conditional heteroskedasticity. J. Econom. 1986, 31, 307–327. [CrossRef]
106. Gensler, A.; Henze, J.; Sick, B.; Raabe, N. Deep Learning for solar power forecasting—An approach using AutoEncoder and
LSTM Neural Networks. In Proceedings of the 2016 IEEE International Conference on Systems, Man, and Cybernetics (SMC),
Budapest, Hungary, 9–12 October 2016; pp. 2858–2865.

107. Bao, W.; Yue, J.; Rao, Y. A deep learning framework for ﬁnancial time series using stacked autoencoders and long-short term

memory. PLoS ONE 2017, 12, e0180944. [CrossRef] [PubMed]

108. Lee, C.Y.; Soo, V.W. Predict stock price with ﬁnancial news based on recurrent convolutional neural networks. In Proceedings
of the 2017 Conference on Technologies and Applications of Artiﬁcial Intelligence (TAAI), Taipei, Taiwan, 1–3 December 2017;
pp. 160–165.

109. Kuo, P.H.; Huang, C.J. An electricity price forecasting model by hybrid structured deep neural networks. Sustainability 2018,

10, 1280. [CrossRef]

110. Tian, C.; Ma, J.; Zhang, C.; Zhan, P. A deep neural network model for short-term load forecast based on long short-term memory

network and convolutional neural network. Energies 2018, 11, 3493. [CrossRef]

111. Liu, H.; Mi, X.; Li, Y. Smart deep learning based wind speed prediction model using wavelet packet decomposition, convolutional
neural network and convolutional long short term memory network. Energy Convers. Manag. 2018, 166, 120–131. [CrossRef]
112. Chen, Y.; Wu, J.; Bu, H. Stock market embedding and prediction: A deep learning method. In Proceedings of the 2018 15th

International Conference on Service Systems and Service Management (ICSSSM), Hangzhou, China, 21–22 July 2018; pp. 1–6.

113. Hossain, M.A.; Karim, R.; Thulasiram, R.; Bruce, N.D.; Wang, Y. Hybrid deep learning model for stock price prediction. In
Proceedings of the 2018 IEEE Symposium Series on Computational Intelligence (SSCI), Bangalore, India, 18–21 November 2018;
pp. 1837–1844.

114. Kim, H.Y.; Won, C.H. Forecasting the volatility of stock price index: A hybrid model integrating LSTM with multiple GARCH-type

models. Expert Syst. Appl. 2018, 103, 25–37. [CrossRef]

115. Li, Y.; Yu, R.; Shahabi, C.; Liu, Y. Diffusion Convolutional Recurrent Neural Network: Data-Driven Trafﬁc Forecasting.

In

Proceedings of the International Conference on Learning Representations, Vancouver, BC, Canada, 30 April–3 May 2018.
116. Huang, C.J.; Kuo, P.H. A deep CNN-LSTM model for particulate matter (PM2. 5) forecasting in smart cities. Sensors 2018, 18, 2220.

[CrossRef]

117. Soh, P.W.; Chang, J.W.; Huang, J.W. Adaptive deep learning-based air quality prediction model using the most relevant

spatial-temporal relations. IEEE Access 2018, 6, 38186–38199. [CrossRef]

118. Fan, C.; Zhang, Y.; Pan, Y.; Li, X.; Zhang, C.; Yuan, R.; Wu, D.; Wang, W.; Pei, J.; Huang, H. Multi-horizon time series forecasting
with temporal attention learning. In Proceedings of the 25th ACM SIGKDD International Conference on Knowledge Discovery &
Data Mining, Anchorage, AK, USA, 4–8 August 2019; pp. 2527–2535.

119. Pan, C.; Tan, J.; Feng, D.; Li, Y. Very short-term solar generation forecasting based on LSTM with temporal attention mechanism.
In Proceedings of the 2019 IEEE 5th International Conference on Computer and Communications (ICCC), Chengdu, China, 6–9
December 2019; pp. 267–271.

120. Wang, S.; Wang, X.; Wang, S.; Wang, D. Bi-directional long short-term memory method based on attention mechanism and rolling

update for short-term load forecasting. Int. J. Electr. Power Energy Syst. 2019, 109, 470–479. [CrossRef]

---

<!-- PAGE 32 -->

Information 2023, 14, 598

32 of 35

121. Shen, Z.; Zhang, Y.; Lu, J.; Xu, J.; Xiao, G. A novel time series forecasting model with deep learning. Neurocomputing 2020,

396, 302–313. [CrossRef]

122. Pal, R.; Sekh, A.A.; Kar, S.; Prasad, D.K. Neural network based country wise risk prediction of COVID-19. Appl. Sci. 2020,

10, 6448. [CrossRef]

123. Dudukcu, H.V.; Taskiran, M.; Taskiran, Z.G.C.; Yildirim, T. Temporal Convolutional Networks with RNN approach for chaotic

time series prediction. Appl. Soft Comput. 2023, 133, 109945. [CrossRef]

124. Scarselli, F.; Gori, M.; Tsoi, A.C.; Hagenbuchner, M.; Monfardini, G. The graph neural network model. IEEE Trans. Neural Netw.

2008, 20, 61–80. [CrossRef]

125. Hamilton, W.L. Graph Representation Learning; Morgan & Claypool Publishers: San Rafael, CA, USA, 2020.
126. Cheng, D.; Yang, F.; Xiang, S.; Liu, J. Financial time series forecasting with multi-modality graph neural network. Pattern Recognit.

2022, 121, 108218. [CrossRef]

127. Geng, X.; He, X.; Xu, L.; Yu, J. Graph correlated attention recurrent neural network for multivariate time series forecasting. Inf.

Sci. 2022, 606, 126–142. [CrossRef]

128. Xiang, S.; Cheng, D.; Shang, C.; Zhang, Y.; Liang, Y. Temporal and Heterogeneous Graph Neural Network for Financial Time
Series Prediction. In Proceedings of the 31st ACM International Conference on Information & Knowledge Management, Atlanta,
GA, USA, 17–21 October 2022; pp. 3584–3593.

129. Jin, M.; Zheng, Y.; Li, Y.F.; Chen, S.; Yang, B.; Pan, S. Multivariate time series forecasting with dynamic graph neural odes. IEEE

Trans. Knowl. Data Eng. 2022, 35, 9168–9180. [CrossRef]

130. Liu, Y.; Liu, Q.; Zhang, J.W.; Feng, H.; Wang, Z.; Zhou, Z.; Chen, W. Multivariate time series forecasting with temporal polynomial

graph neural networks. Adv. Neural Inf. Process. Syst. 2022, 35, 19414–19426.

131. Williams, C.K.; Rasmussen, C.E. Gaussian Processes for Machine Learning; MIT Press: Cambridge, MA, USA, 2006; Volume 2.
132. Berg, C.; Christensen, J.P.R.; Ressel, P. Harmonic Analysis on Semigroups: Theory of Positive Deﬁnite and Related Functions; Springer:

Berlin/Heidelberg, Germany, 1984; Volume 100.

133. Hensman, J.; Fusi, N.; Lawrence, N.D. Gaussian processes for big data. arXiv 2013, arXiv:1309.6835.
134. Damianou, A.; Lawrence, N.D. Deep gaussian processes. In Proceedings of the Artiﬁcial Intelligence and Statistics, Scottsdale,

AZ, USA, 29 April–1 May 2013; pp. 207–215.

135. You, J.; Li, X.; Low, M.; Lobell, D.; Ermon, S. Deep gaussian process for crop yield prediction based on remote sensing data. In

Proceedings of the AAAI Conference on Artiﬁcial Intelligence, San Francisco, CA, USA, 4–9 February 2017; Volume 31.

136. Mahdi, M.D.; Mrittika, N.J.; Shams, M.; Chowdhury, L.; Siddique, S. A Deep Gaussian Process for Forecasting Crop Yield
and Time Series Analysis of Precipitation Based in Munshiganj, Bangladesh. In Proceedings of the IGARSS 2020—2020 IEEE
International Geoscience and Remote Sensing Symposium, Waikoloa, HI, USA, 26 September–2 October 2020; pp. 1331–1334.

137. Jiang, Y.; Fan, J.; Liu, Y.; Zhang, X. Deep graph Gaussian processes for short-term trafﬁc ﬂow forecasting from spatiotemporal

data. IEEE Trans. Intell. Transp. Syst. 2022, 23, 20177–20186. [CrossRef]

138. Chang, W.; Li, R.; Fu, Y.; Xiao, Y.; Zhou, S. A multistep forecasting method for online car-hailing demand based on wavelet

decomposition and deep Gaussian process regression. J. Supercomput. 2023, 79, 3412–3436. [CrossRef]

139. Camastra, F.; Casolaro, A.; Iannuzzo, G. Time Series prediction with missing data by an Iterated Deep Gaussian Process. In

Proceedings of the 31st Edition of WIRN 2023, Vietri sul Mare, Salerno, Italy, 22–26 May 2023.

140. Goodfellow, I.; Pouget-Abadie, J.; Mirza, M.; Xu, B.; Warde-Farley, D.; Ozair, S.; Courville, A.; Bengio, Y. Generative Adversarial
Nets. In Proceedings of the Advances in Neural Information Processing Systems, Montreal, QC, Canada, 8–13 December 2014;
Volume 27.

141. Radford, A.; Metz, L.; Chintala, S. Unsupervised representation learning with deep convolutional generative adversarial networks.

arXiv 2015, arXiv:1511.06434.

142. Mogren, O. C-RNN-GAN: Continuous recurrent neural networks with adversarial training. arXiv 2016, arXiv:1611.09904.
143. Box, G.E.; Jenkins, G.M.; Reinsel, G.C.; Ljung, G.M. Time Series Analysis: Forecasting and Control; John Wiley & Sons: Hoboken, NJ,

USA, 2015.

144. Wu, D.; Hur, K.; Xiao, Z. A GAN-Enhanced Ensemble Model for Energy Consumption Forecasting in Large Commercial Buildings.

IEEE Access 2021, 9, 158820–158830. [CrossRef]

145. Mirza, M.; Osindero, S. Conditional generative adversarial nets. arXiv 2014, arXiv:1411.1784.
146. Chen, X.; Duan, Y.; Houthooft, R.; Schulman, J.; Sutskever, I.; Abbeel, P. InfoGAN: Interpretable Representation Learning by

Information Maximising Generative Adversarial Nets. Adv. Neural Inf. Process. Syst. 2016, 29.

147. Wang, H.; Tao, G.; Ma, J.; Jia, S.; Chi, L.; Yang, H.; Zhao, Z.; Tao, J. Predicting the epidemics trend of COVID-19 using

epidemiological-based generative adversarial networks. IEEE J. Sel. Top. Signal Process. 2022, 16, 276–288. [CrossRef]

148. Wiese, M.; Knobloch, R.; Korn, R.; Kretschmer, P. Quant GANs: Deep generation of ﬁnancial time series. Quant. Financ. 2020,

20, 1419–1440. [CrossRef]

149. Hazra, D.; Byun, Y.C. SynSigGAN: Generative adversarial networks for synthetic biomedical signal generation. Biology 2020,

9, 441. [CrossRef] [PubMed]

150. Esteban, C.; Hyland, S.L.; Rätsch, G. Real-valued (medical) time series generation with recurrent conditional gans. arXiv 2017,

arXiv:1706.02633.

151. Yoon, J.; Jarrett, D.; Van der Schaar, M. Time-series generative adversarial networks. Adv. Neural Inf. Process. Syst. 2019, 32.

---

<!-- PAGE 33 -->

Information 2023, 14, 598

33 of 35

152. Ni, H.; Szpruch, L.; Wiese, M.; Liao, S.; Xiao, B. Conditional sig-wasserstein gans for time series generation.

arXiv 2020,

arXiv:2006.05421.

153. Li, X.; Metsis, V.; Wang, H.; Ngu, A.H.H. Tts-gan: A transformer-based time series generative adversarial network.

In
Proceedings of the International Conference on Artiﬁcial Intelligence in Medicine, Halifax, NS, Canada, 14–17 June 2022; Springer:
Berlin/Heidelberg, Germany, 2022; pp. 133–143.

154. Koochali, A.; Schichtel, P.; Dengel, A.; Ahmed, S. Probabilistic forecasting of sensory data with generative adversarial networks–

ForGAN. IEEE Access 2019, 7, 63868–63880. [CrossRef]

155. Bej, A.; Maulik, U.; Sarkar, A. Time-Series prediction for the epidemic trends of COVID-19 using Conditional Generative

adversarial Networks Regression on country-wise case studies. SN Comput. Sci. 2022, 3, 352. [CrossRef]

156. Zúñiga, G.; Acuña, G. Probabilistic multistep time series forecasting using conditional generative adversarial networks. In
Proceedings of the 2021 IEEE Latin American Conference on Computational Intelligence (LA-CCI), Temuco, Chile, 2–4 November
2021; pp. 1–6.

157. Huang, X.; Li, Q.; Tai, Y.; Chen, Z.; Liu, J.; Shi, J.; Liu, W. Time series forecasting for hourly photovoltaic power using conditional

generative adversarial network and Bi-LSTM. Energy 2022, 246, 123403. [CrossRef]

158. Li, F.; Zheng, H.; Li, X. A novel hybrid model for multi-step ahead photovoltaic power prediction based on conditional time

series generative adversarial networks. Renew. Energy 2022, 199, 560–586. [CrossRef]

159. Zhou, X.; Pan, Z.; Hu, G.; Tang, S.; Zhao, C. Stock market prediction on high-frequency data using generative adversarial nets.

Math. Probl. Eng. 2018, 2018, 4907423. [CrossRef]

160. Zhang, Y.; Wang, S.; Chen, B.; Cao, J.; Huang, Z. Trafﬁcgan: Network-scale deep trafﬁc prediction with generative adversarial

nets. IEEE Trans. Intell. Transp. Syst. 2019, 22, 219–230. [CrossRef]

161. Kaushik, S.; Choudhury, A.; Natarajan, S.; Pickett, L.A.; Dutt, V. Medicine expenditure prediction via a variance-based generative

adversarial network. IEEE Access 2020, 8, 110947–110958. [CrossRef]

162. Gu, Y.; Chen, Q.; Liu, K.; Xie, L.; Kang, C. GAN-based Model for Residential Load Generation Considering Typical Consumption
Patterns. In Proceedings of the 2019 IEEE Power & Energy Society Innovative Smart Grid Technologies Conference (ISGT),
Washington, DC, USA, 18–21 February 2019; pp. 1–5.

163. He, B.; Kita, E. Stock price prediction by using hybrid sequential generative adversarial networks. In Proceedings of the 2020

International Conference on Data Mining Workshops (ICDMW), Sorrento, Italy, 17–20 November 2020; pp. 341–347.

164. Wu, S.; Xiao, X.; Ding, Q.; Zhao, P.; Wei, Y.; Huang, J. Adversarial sparse transformer for time series forecasting. Adv. Neural Inf.

Process. Syst. 2020, 33, 17105–17115.

165. Li, Q.; Hao, H.; Zhao, Y.; Geng, Q.; Liu, G.; Zhang, Y.; Yu, F. GANs-LSTM model for soil temperature estimation from

meteorological: A new approach. IEEE Access 2020, 8, 59427–59443. [CrossRef]

166. Yin, X.; Han, Y.; Sun, H.; Xu, Z.; Yu, H.; Duan, X. Multi-attention generative adversarial network for multivariate time series

prediction. IEEE Access 2021, 9, 57351–57363. [CrossRef]

167. Wu, W.; Huang, F.; Kao, Y.; Chen, Z.; Wu, Q. Prediction method of multiple related time series based on generative adversarial

networks. Information 2021, 12, 55. [CrossRef]

168. Jiang, C.; Mao, Y.; Chai, Y.; Yu, M. Day-ahead renewable scenario forecasts based on generative adversarial networks. Int. J.

Energy Res. 2021, 45, 7572–7587. [CrossRef]

169. Bendaoud, N.M.M.; Farah, N.; Ben Ahmed, S. Comparing Generative Adversarial Networks architectures for electricity demand

forecasting. Energy Build. 2021, 247, 111152. [CrossRef]

170. Wu, X.; Yang, H.; Chen, H.; Hu, Q.; Hu, H. Long-term 4D trajectory prediction using generative adversarial networks. Transp.

Res. Part Emerg. Technol. 2022, 136, 103554. [CrossRef]

171. Ye, Y.; Strong, M.; Lou, Y.; Faulkner, C.A.; Zuo, W.; Upadhyaya, S. Evaluating performance of different generative adversarial

networks for large-scale building power demand prediction. Energy Build. 2022, 269, 112247. [CrossRef]

172. Vuleti´c, M.; Prenzel, F.; Cucuringu, M. Fin-Gan: Forecasting and Classifying Financial Time Series via Generative Adversarial

Networks. 2023. Available online: https://ssrn.com/abstract=4328302 (accessed on 25 September 2023).

173. Sohl-Dickstein, J.; Weiss, E.; Maheswaranathan, N.; Ganguli, S. Deep unsupervised learning using nonequilibrium thermodynam-

ics. In Proceedings of the International Conference on Machine Learning, Lille, France, 7–9 July 2015; pp. 2256–2265.
174. Ho, J.; Jain, A.; Abbeel, P. Denoising diffusion probabilistic models. Adv. Neural Inf. Process. Syst. 2020, 33, 6840–6851.
175. Song, Y.; Ermon, S. Generative modeling by estimating gradients of the data distribution. Adv. Neural Inf. Process. Syst. 2019, 32.
176. Song, Y.; Sohl-Dickstein, J.; Kingma, D.P.; Kumar, A.; Ermon, S.; Poole, B. Score-Based Generative Modeling through Stochastic
Differential Equations. In Proceedings of the International Conference on Learning Representations, Addis Ababa, Ethiopia,
26–32 April 2020.

177. Rasul, K.; Seward, C.; Schuster, I.; Vollgraf, R. Autoregressive denoising diffusion models for multivariate probabilistic time
series forecasting. In Proceedings of the International Conference on Machine Learning, Virtual, 18–24 July 2021; pp. 8857–8868.
178. Yan, T.; Zhang, H.; Zhou, T.; Zhan, Y.; Xia, Y. ScoreGrad: Multivariate probabilistic time series forecasting with continuous

energy-based generative models. arXiv 2021, arXiv:2106.10121.

179. Li, Y.; Lu, X.; Wang, Y.; Dou, D. Generative time series forecasting with diffusion, denoise, and disentanglement. Adv. Neural Inf.

Process. Syst. 2022, 35, 23009–23022.

---

<!-- PAGE 34 -->

Information 2023, 14, 598

34 of 35

180. Biloš, M.; Rasul, K.; Schneider, A.; Nevmyvaka, Y.; Günnemann, S. Modeling temporal data as continuous functions with process

diffusion. arXiv 2022, arXiv:2211.02590.

181. Vaswani, A.; Shazeer, N.; Parmar, N.; Uszkoreit, J.; Jones, L.; Gomez, A.N.; Kaiser, Ł.; Polosukhin, I. Attention is all you need.

Adv. Neural Inf. Process. Syst. 2017, 30.

182. Zhou, H.; Zhang, S.; Peng, J.; Zhang, S.; Li, J.; Xiong, H.; Zhang, W. Informer: Beyond efﬁcient transformer for long sequence
time series forecasting. In Proceedings of the AAAI Conference on Artiﬁcial Intelligence, Virtual, 2–9 February 2021; Volume 35,
pp. 11106–11115.

183. Wu, H.; Xu, J.; Wang, J.; Long, M. Autoformer: Decomposition transformers with auto-correlation for long-term series forecasting.

Adv. Neural Inf. Process. Syst. 2021, 34, 22419–22430.

184. Zhou, T.; Ma, Z.; Wen, Q.; Wang, X.; Sun, L.; Jin, R. Fedformer: Frequency enhanced decomposed transformer for long-term
series forecasting. In Proceedings of the International Conference on Machine Learning, Baltimore, MD, USA, 17–23 July 2022;
pp. 27268–27286.

185. He, K.; Zhang, X.; Ren, S.; Sun, J. Deep residual learning for image recognition. In Proceedings of the IEEE Conference on

Computer Vision and Pattern Recognition, Las Vegas, NV, USA, 26 June–1 July 2016; pp. 770–778.

186. Ba, J.L.; Kiros, J.R.; Hinton, G.E. Layer normalization. arXiv 2016, arXiv:1607.06450.
187. Luong, T.; Pham, H.; Manning, C.D. Effective Approaches to Attention-based Neural Machine Translation. In Proceedings of the
2015 Conference on Empirical Methods in Natural Language Processing, Lisbon, Portugal, 17–21 September 2015; Association for
Computational Linguistics: Cedarville, OH, USA, 2015; pp. 1412–1421.

188. Li, S.; Jin, X.; Xuan, Y.; Zhou, X.; Chen, W.; Wang, Y.X.; Yan, X. Enhancing the locality and breaking the memory bottleneck of

transformer on time series forecasting. Adv. Neural Inf. Process. Syst. 2019, 32.

189. Wang, S.; Li, B.Z.; Khabsa, M.; Fang, H.; Ma, H. Linformer: Self-attention with linear complexity. arXiv 2020, arXiv:2006.04768.
190. Donoho, D.L. Compressed sensing. IEEE Trans. Inf. Theory 2006, 52, 1289–1306. [CrossRef]
191. Nie, Y.; Nguyen, N.H.; Sinthong, P.; Kalagnanam, J. A Time Series is Worth 64 Words: Long-term Forecasting with Transformers.

In Proceedings of the International Conference on Learning Representations, Kigali, Rwanda, 1–5 May 2023.

192. Zhang, Y.; Yan, J. Crossformer: Transformer utilising cross-dimension dependency for multivariate time series forecasting. In

Proceedings of the Eleventh International Conference on Learning Representations, Kigali, Rwanda, 1–5 May 2022.

193. Liu, S.; Yu, H.; Liao, C.; Li, J.; Lin, W.; Liu, A.X.; Dustdar, S. Pyraformer: Low-Complexity Pyramidal Attention for Long-Range
Time Series Modeling and Forecasting. In Proceedings of the International Conference on Learning Representations, Virtual,
25–29 April 2022.

194. Shabani, M.A.; Abdi, A.H.; Meng, L.; Sylvain, T. Scaleformer: Iterative Multi-scale Reﬁning Transformers for Time Series
Forecasting. In Proceedings of the The Eleventh International Conference on Learning Representations, Kigali, Rwanda, 1–5
May 2023.

195. Cirstea, R.G.; Guo, C.; Yang, B.; Kieu, T.; Dong, X.; Pan, S. Triformer: Triangular, Variable-Speciﬁc Attentions for Long Sequence

Multivariate Time Series Forecasting–Full Version. arXiv 2022, arXiv:2204.13767.

196. Liu, Y.; Wu, H.; Wang, J.; Long, M. Non-stationary transformers: Exploring the stationarity in time series forecasting. Adv. Neural

Inf. Process. Syst. 2022, 35, 9881–9893.

197. Schirmer, M.; Eltayeb, M.; Lessmann, S.; Rudolph, M. Modeling irregular time series with continuous recurrent units.
Proceedings of the International Conference on Machine Learning, Baltimore, MD, USA, 17–23 July 2022; pp. 19388–19405.
198. Zhou, T.; Ma, Z.; Wen, Q.; Sun, L.; Yao, T.; Yin, W.; Jin, R. Film: Frequency improved legendre memory model for long-term time

In

series forecasting. Adv. Neural Inf. Process. Syst. 2022, 35, 12677–12690.

199. Ekambaram, V.; Jati, A.; Nguyen, N.; Sinthong, P.; Kalagnanam, J. TSMixer: Lightweight MLP-Mixer Model for Multivariate Time
Series Forecasting. In Proceedings of the 29th ACM SIGKDD Conference on Knowledge Discovery and Data Mining, Long Beach,
CA, USA, 6–10 August 2023; pp. 459–469.

200. Wang, H.; Peng, J.; Huang, F.; Wang, J.; Chen, J.; Xiao, Y. MICN: Multi-scale Local and Global Context Modeling for Long-term
Series Forecasting. In Proceedings of the Eleventh International Conference on Learning Representations, Kigali, Rwanda, 1–5
May 2023.

201. Mackey, M.C.; Glass, L. Oscillation and chaos in physiological control systems. Science 1977, 197, 287–289. [CrossRef] [PubMed]
202. Weiss, C.O.; Hübner, U.; Abraham, N.B.; Tang, D. Lorenz-like chaos in NH3-FIR lasers. Infrared Phys. Technol. 1995, 36, 489–512.

[CrossRef]

203. Aguirre, L.A.; Rodrigues, G.G.; Mendes, E.M. Nonlinear identiﬁcation and cluster analysis of chaotic attractors from a real

implementation of Chua’s circuit. Int. J. Bifurc. Chaos 1997, 7, 1411–1423. [CrossRef]

204. Wijngaard, J.; Klein Tank, A.; Können, G. Homogeneity of 20th century European daily temperature and precipitation series. Int.

J. Climatol. J. R. Meteorol. Soc. 2003, 23, 679–692. [CrossRef]

205. Weigend, A.S.; Gershenfeld, N.A. Time Series Prediction: Forecasting the Future and Understanding the Past; Santa Fe Institute Studies

in the Sciences of Complexity: Santa Fe, NM, USA, 1994.

206. Jospin, L.V.; Laga, H.; Boussaid, F.; Buntine, W.; Bennamoun, M. Hands-on Bayesian neural networks—A tutorial for deep

learning users. IEEE Comput. Intell. Mag. 2022, 17, 29–48. [CrossRef]

207. Lu, J.; Liu, A.; Dong, F.; Gu, F.; Gama, J.; Zhang, G. Learning under concept drift: A review. IEEE Trans. Knowl. Data Eng. 2018,

31, 2346–2363. [CrossRef]

---

<!-- PAGE 35 -->

Information 2023, 14, 598

35 of 35

208. Hyvärinen, A.; Dayan, P. Estimation of non-normalized statistical models by score matching. J. Mach. Learn. Res. 2005, 6.
209. Vincent, P. A connection between score matching and denoising autoencoders. Neural Comput. 2011, 23, 1661–1674. [CrossRef]

[PubMed]

210. Song, Y.; Garg, S.; Shi, J.; Ermon, S. Sliced score matching: A scalable approach to density and score estimation. In Proceedings of

the Uncertainty in Artiﬁcial Intelligence, Virtual, 3–6 August 2020; pp. 574–584.

211. Anderson, B.D. Reverse-time diffusion equation models. Stoch. Process. Their Appl. 1982, 12, 313–326. [CrossRef]
212. Papoulis, A.; Unnikrishna Pillai, S. Probability, Random Variables and Stochastic Processes; McGraw-Hill: New York, NY, USA, 2002.

Disclaimer/Publisher’s Note: The statements, opinions and data contained in all publications are solely those of the individual
author(s) and contributor(s) and not of MDPI and/or the editor(s). MDPI and/or the editor(s) disclaim responsibility for any injury to
people or property resulting from any ideas, methods, instructions or products referred to in the content.

<!-- MARKITDOWN CONVERSION -->

<!-- Full MarkItDown conversion for formatting fidelity. -->

informatio n
Review
Deep Learning for Time Series Forecasting: Advances
and Open Problems
AngeloCasolaro† ,VincenzoCapone† ,GennaroIannuzzo† andFrancescoCamastra*,†
DepartmentofScienceandTechnology,ParthenopeUniversityofNaples,CentroDirezionaleIsolaC4,
80143Naples,Italy;angelo.casolaro001@studenti.uniparthenope.it(A.C.);
vincenzo.capone002@studenti.uniparthenope.it(V.C.);gennaro.iannuzzo001@studenti.uniparthenope.it(G.I.)
* Correspondence:francesco.camastra@uniparthenope.it
† Theseauthorscontributedequallytothiswork.
Abstract:Atimeseriesisasequenceoftime-ordereddata,anditisgenerallyusedtodescribehow
aphenomenonevolvesovertime. Timeseriesforecasting,estimatingfuturevaluesoftimeseries,
allowstheimplementationofdecision-makingstrategies.Deeplearning,thecurrentlyleadingfield
ofmachinelearning,appliedtotimeseriesforecastingcancopewithcomplexandhigh-dimensional
timeseriesthatcannotbeusuallyhandledbyothermachinelearningtechniques. Theaimofthe
workistoprovideareviewofstate-of-the-artdeeplearningarchitecturesfortimeseriesforecasting,
underline recent advances and open problems, and also pay attention to benchmark data sets.
Moreover,theworkpresentsacleardistinctionbetweendeeplearningarchitecturesthataresuitable
forshort-termandlong-termforecasting. Withrespecttoexistingliterature,themajoradvantage
oftheworkconsistsindescribingthemostrecentarchitecturesfortimeseriesforecasting,suchas
GraphNeuralNetworks,DeepGaussianProcesses,GenerativeAdversarialNetworks,Diffusion
Models,andTransformers.
Keywords: short-term forecasting; long-term forecasting; recurrent neural networks; temporal
convolutionalneuralnetworks;graphneuralnetworks;deepgaussianprocesses;transformers;time
seriesbenchmarking;generativeadversarialnetworks;diffusionmodels
Citation:Casolaro,A.;Capone,V.;
Iannuzzo,G.;Camastra,F.Deep
1. Introduction
LearningforTimeSeriesForecasting:
Atimeseriesisasequenceofdataenumeratedintimeorder. Timeseriesareused
AdvancesandOpenProblems.
Information2023,14,598. https:// tostudyhowcertainmeasures,e.g.,airpollutiondata[1],ozoneconcentration[2],plant
doi.org/10.3390/info14110598 growth[3],sunspots[4],DowJonesandNasdaqindices[5],andelectricityconsumption[6],
evolveovertime. Timeseriesforecastingestimatesvaluesthatatimeseriestakesinthe
AcademicEditor:NikosE.
future,allowingtheimplementationofdecision-makingstrategies,e.g.,abandonmentof
Mastorakis
fossilfuelstoreducethesurfacetemperatureoftheEarth. Specifically, timeseriesfore-
Received:26September2023 castingisveryrelevantfortheenergydomain(e.g.,electricityloaddemand[7,8],solarand
Revised:18October2023 windpowerestimation[9,10]),meteorology(e.g.,predictionofwindspeed[11],tempera-
Accepted:2November2023 ture[12,13],humidity[12],precipitation[13,14]),airpollutionmonitoring(e.g.,prediction
Published:4November2023 of PM , PM , NO , O , SO , and CO concentrations [12,15,16]), the finance domain
2.5 10 2 3 2 2
(e.g.,stockmarketindexandsharesprediction[17,18],thestockprice[19,20],exchange
rate[21,22]),health(e.g.,predictionofinfectivediseasesdiffusion[23],diabetesmellitus[24],
bloodglucoseconcentration[25],andcancergrowth[26]),traffic(e.g.,trafficspeedandflow
Copyright: © 2023 by the authors.
prediction[27–30]),andindustrialproduction(e.g.,petroleumproduction[31],remaininglife
Licensee MDPI, Basel, Switzerland.
prediction[23,32,33],industrialprocesses[34],fuelcellsdurability[35],enginefaults[36]).
This article is an open access article
Deeplearningalgorithmsarecurrentlytheleadingmethodsinmachinelearningdueto
distributed under the terms and
theirsuccessfulapplicationtomanycomputersciencedomains(e.g.,computervision,natural
conditionsoftheCreativeCommons
Attribution(CCBY)license(https:// languageprocessing,speechrecognition). Inrecentyears,therehasbeenagrowthofinterestin
creativecommons.org/licenses/by/ theapplicationofdeeplearningtotimeseriesforecasting,duetodeeplearning’scapability
4.0/). tograspthenonlinearrelationsamonginputdata(i.e.,timeseriessamples). Tothebest
Information2023,14,598.https://doi.org/10.3390/info14110598 https://www.mdpi.com/journal/information

Information2023,14,598 2of35
ofourknowledge,thereareseveralreviewsondeeplearningfortimeseriesforecasting
(e.g.,[37–43]),buttheyhavethefollowingmajorshortcomings: theylackadescriptionof
Transformeranditsvariants; theydonotprovideacleardistinctionbetweenmodelsfor
short-termandlong-termforecasting,therearenosectionsonshort-termandlong-term
forecasting benchmarks; they do not cover the most recent deep learning strategies for
short-term forecasting (e.g., Graph Neural Networks, Deep Gaussian Processes, Generative
AdversarialNetworks,andDiffusionModels). Theaimofthisworkistoprovideacomprehen-
sivesurveyofrecentdeeplearningapproachesfortimeseriesforecasting,underliningthe
advancesandtheopenproblemsforeachrevieweddeeplearningarchitecture. Specifically,
thesurveyfocusesonworksaboutmachinelearningappliedtotimeseriesforecastingthat
arenotolderthan2016, forthesakeoflength. Thepaperisorganisedinthefollowing
sections: inSection2,thefoundationsofdeterministictimeseriesareintroduced;Section3
describesdeeplearningarchitecturesforshort-termforecasting,i.e.,ConvolutionalNeural
Networks,TemporalConvolutionalNetworks,RecurrentNeuralNetworks(RNNs),GraphNeural
Networks, Deep Gaussian Processes, Generative Adversarial Networks, and Diffusion Models;
Section4discusseslong-termforecastingarchitectures, i.e., theTransformerarchitecture
anditstimeseries-basedvariants;Section5reviewsotherheterogeneousarchitecturesfor
bothshort-termandlong-termforecasting;benchmarkingforshort-termandlong-term
timeseriesforecastingispresentedinSection6;inSection7,someconclusionsaredrawn
andfuturepossibledevelopmentsarediscussed;finally,intheappendixarereportedthe
main mathematical notation used in the work and a description of the main diffusion
modelfoundations.
2. DeterministicTimeSeries
Atimeseriesiscalledaunivariatetimeseriesifallitssamplesarescalar;otherwise,ifall
samplesarevectors,itiscalledamultivariatetimeseries. Atimeseriesisdefinedasstationary
whenthedynamicalprocessthatgenerateditdoesnotchangeovertime,otherwise,itis
non-stationary. Adeterministicstationarytimeseriesx ,witht =1,...,L,canbedescribedby
t
anautoregressivemodelasfollows:
x t+p = f(x t−1 ,...,x t−q )+(cid:101) t+p ∀p ∈ [0,P] (1)
where f(·) and q are called skeleton and model order of time series, i.e., how many past
samplesarerequiredtomodelthetimeseriesadequately,respectively,and(cid:101) t+p represents
anindeterminablepartoriginatedeitherfromunmodeleddynamicsoftheprocessorfrom
realnoise. Pdefinesthepredictionlength,i.e.,howmanyfuturesamplesshouldbepredicted.
Figure1givesagraphicalrepresentationofanautoregressivemodel.
X ... X X X
0 t-2 t-1 t
+ ε
f
X ... X X X X
0 t-2 t-1 t t+1
Figure1.Anexampleofanautoregressivemodelforforecastingbasedondeterministicstationary
timeseries. Inthefigure,themodelorderisq = 2andthepredictionlengthisP = 0(i.e.,itisa
one-stepaheadforecastingproblem).

Information2023,14,598 3of35
IfP =0,theautoregressivemodeldefinestheso-calledone-stepaheadforecasting,other-
wise,apredictionlengthP >0specifiesamulti-stepaheadforecastingproblem. Moreover,
multi-stepaheadforecastingcanbefurtherdividedintoshort-termandlong-termforecasting.
Intheliterature,thetypicalthresholdvalueofpredictionlengthPbetweenshort-termand
long-termforecastingrangesbetween2and48[44]. Finally,forthesakeofclarity,inthis
work,one-stepaheadforecastingisincludedinshort-termforecasting.
3. DeepLearningModelsforShort-TermForecasting
In short-term forecasting, the skeleton of time series can be approximated by the
followingdeeplearningmodels,whicharedescribedbelow. Thesectionisorganisedas
follows. Firstly, Convolutional Neural Networks (Section 3.1), and Temporal Convolutional
Networks(Section3.1.2)areintroduced. Furthermore,RecurrentNeuralNetworks(Section3.2)
aredescribed,includingElmanRNNs(Section3.2.1),EchoStateNetworks(Section3.2.3),Long
Short-TermMemory(Section3.2.4),andGatedRecurrentUnits(Section3.2.5). Successively,
hybridsandvariants(Section3.3)oftheaforementionedarchitecturesarebrieflyreviewed.
Moreover,GraphNeuralNetworks(Section3.4),DeepGaussianProcesses(Section3.5),and
generative models (Section 3.6), i.e., Generative Adversarial Networks (Section 3.6.1) and
DiffusionModels(Section3.6.3),arediscussed. Finally,foreachreviewedmodel,drawbacks
andlimitationsarediscussedinpropersections.
3.1. ConvolutionalNeuralNetworks
ConvolutionalNeuralNetworks(CNNs)[45],asshowninFigure2,haveadeeparchi-
tecture generally formed by convolution, pooling, and fully connected layers. CNNs have
threemainpeculiarities: localconnectivity,sharedweightsandtranslationequivariance. Local
connectivityresidesineachCNNneuronbeingconnectedonlytoitsexclusiveinputregion,
theso-calledreceptivefield. Besides,theneuronsofagivenlayersharethesameweight
matrix. TranslationequivarianceistheabilityofCNNstodetectcertainpatterns,regardless
of the position they have in the input image. 1D convolution (see Figure 3) of an input
sequenceX = [x ,...,x ]withagivenkernelwwithsizeqisdefinedas:
1 L
q/2
∑
y(t) = (w∗X)(t) = w(a)X(t−a) ∀t ∈ [1,...,L] (2)
a=−q/2
Itisworthwhiletoremarkthatintheautoregressiveapproach,thekernelsizeqcorresponds
tothemodelorder,generallyfixedusingmodelselectiontechniques(e.g.,cross-validation)[46].
Moreover,CNNcanstackdifferentconvolutionallayersinordertotransformtheinput
data(i.e.,thepasttimeseriesvalues)intoamoresuitablehigher-levelrepresentationfor
theforecastingtask. CNNtimeseriesforecastingapplicationsaredescribedinTable1.
Figure2.AnexampleofConvolutionalNeuralNetworkappliedtotimeseriesforecasting.Thered,
theblueandthegreenboxesrepresentCNN’sconvolutionallayers.

Information2023,14,598 4of35
Output Length
|     | . . . yt yt+1 | . . . |     | Output Sequence |     |     |     |
| --- | ------------- | ----- | --- | --------------- | --- | --- | --- |
Kernel (size=3)
| . . . | xt-1 xt xt+1xt+2 | . . . |     |     |     |     |     |
| ----- | ---------------- | ----- | --- | --- | --- | --- | --- |
Input Sequence
Input Length
Figure3.Exampleof1Dconvolutionusingakernelwithsizek=3.Thescalarproductisdenotedby
•.Theyellowboxesdenotethelearnedkernel.
Table1.RecentapplicationsontimeseriesforecastingusingConvolutionalNeuralNetworks.
| Ref. |     |     | Year |     |                                    | Application                  |     |
| ---- | --- | --- | ---- | --- | ---------------------------------- | ---------------------------- | --- |
| [47] |     |     | 2017 |     |                                    | ETFsprices                   |     |
| [48] |     |     | 2018 |     |                                    | Electricityconsumption       |     |
| [10] |     |     | 2018 |     |                                    | Solarpowerandelectricityload |     |
| [6]  |     |     | 2018 |     |                                    | Electricityconsumption       |     |
| [7]  |     |     | 2018 |     |                                    | Electricityprice             |     |
| [49] |     |     | 2019 |     | Electricitypriceandloadforecasting |                              |     |
| [50] |     |     | 2019 |     |                                    | Building-levelload           |     |
| [12] |     |     | 2023 |     |                                    | CO 2 /Temperature/Humidity   |     |
3.1.1. ShortcomingsofConvolutionalNeuralNetworks
ThemajordrawbackofCNNsfortimeseriesforecastingistheuseofEuclideanker-
nels[51],sinceonlyacontinuousandcommonlyshorttimeseriessubsequenceisconsidered
atatimebyanEuclideankernel. However,intimeseriesforecastingtasksitmaybeuse-
fultoextractrepresentativefeaturesbyanalysingnon-contiguousandfarthertimeseries
samplesinthepast. ThislimitationisovercomebyTemporalConvolutionalNetworks(see
Section3.1.2),withtheuseofcausalanddilatedconvolutions,andbyGraphNeuralNetworks
(seeSection3.4),withaproperlydesignedadjacencymatrix.
3.1.2. TemporalConvolutionalNetworks
Temporal Convolutional Networks (TCNs) were proposed for action segmentation and
detectionbyLeaetal.[52]. Inanutshell,aTCNiscomposedofcascaded1Dconvolutional
layersthatallowmappingarbitrarilylonginputsontooutputsequencesofthesamelength.
IncontrasttotraditionalCNNs,TCNsperformcausalanddilatedconvolutions. Unlike1D
convolution(seeEquation(2)),incausal1Dconvolution(seeFigure4)theoutputelement
at time t is yielded by the convolution between the kernel and past input elements only,
namely[x ,x ,...,x ],whereqisthekernelsizethatcorrespondstothemodelorder
| t−1 | t−2 t−q |     |     |     |     |     |     |
| --- | ------- | --- | --- | --- | --- | --- | --- |
inanautoregressiveapproach(seeSection3.1). Indetail,causal1Dconvolutionisdefined
asfollows:
q
∑
|     | y(t) = (w∗X)(t) |     | =   | w(a)X(t−a) |     | ∀t ∈ [1,...,L] | (3) |
| --- | --------------- | --- | --- | ---------- | --- | -------------- | --- |
a=1
A dilated 1D convolution (see Figure 5) differs from a 1D convolution due to the in-
troduction of a dilation factor d. The dilation, applied to convolution, is equivalent to
consideringafixedstepbetweentwoadjacentkernelelements. Inparticular,dilatedcausal
1Dconvolutioncanbedefinedas:
q
∑
|     | y(t) = (w∗X)(t) |     | =   | w(a)X(t−d·a) |     | ∀t ∈ [1,...,L] | (4) |
| --- | --------------- | --- | --- | ------------ | --- | -------------- | --- |
a=1

Information2023,14,598 5of35
Whend =1,adilated1Dconvolutionisreducedtoa1Dconvolution.
Dilatedconvolutions
allowthenetworkstohavealargereceptivefield,i.e.,tocaptureinformationintothefar
past,byalogarithmicgrowthofthenumbergofconvolutionallayers,asstatedin:
|     |     |     | (cid:24) | (cid:18)(n−1)(b−1) |       |     | (cid:19)(cid:25) |     |
| --- | --- | --- | -------- | ------------------ | ----- | --- | ---------------- | --- |
|     |     |     | g = log  |                    |       | +1  |                  | (5) |
|     |     |     |          | b                  | (q−1) |     |                  |     |
wherebisthelogarithmicbaseofthedilationfactord forthei-thconvolutionallayer(namely,
i
d = bi). TCNtimeseriesforecastingapplicationsarereportedinTable2.
i
|              |     | y y          | . . .         | y       | Output Sequence |     |     |     |
| ------------ | --- | ------------ | ------------- | ------- | --------------- | --- | --- | --- |
|              |     | 1 2          |               | L       |                 |     |     |     |
| 0            | 0   | x 1 x 2      | . . . x L-2 x | L-1 x L | Input Sequence  |     |     |     |
| Zero Padding |     | Input Length |               |         |                 |     |     |     |
Figure4.Causal1Dconvolutionwithakernelofsizeq=3.Zeropaddingelementsareaddedatthe
beginningoftheinputsequenceinordertohaveanoutputsequencewiththesamelengthasthe
inputsequence.
Output Sequence
ConvLayer2
(d2=22=4)
0
| Zero |     |     |     |     | ConvLayer1 |     |     |     |
| ---- | --- | --- | --- | --- | ---------- | --- | --- | --- |
Padding
(d1=21=2)
ConvLayer0
(d0=20=1)
Input Sequence
Figure5.Exampleofadilatedcausal1Dconvolutionwiththreelayersusingadilationbaseb=2
andakernelsizeq=3.Zeropaddingisusedtopreservetheinputsequencelength.
Table2.TimeseriesforecastingapplicationsusingTemporalConvolutionalNetworks.
|     | Ref. |     | Year |     |     |     | Application |     |
| --- | ---- | --- | ---- | --- | --- | --- | ----------- | --- |
|     | [53] |     | 2018 |     |     |     | Stockmarket |     |
|     | [15] |     | 2019 |     |     |     | BeijingPM   |     |
2.5
|     | [30] |     | 2019 |     |                                      |                     | Traffic   |     |
| --- | ---- | --- | ---- | --- | ------------------------------------ | ------------------- | --------- | --- |
|     | [54] |     | 2020 |     | Nationalelectricdemandandpowerdemand |                     |           |     |
|     | [9]  |     | 2020 |     |                                      | Windpowergeneration |           |     |
|     | [55] |     | 2020 |     |                                      |                     | Weather   |     |
|     | [11] |     | 2022 |     |                                      |                     | Windspeed |     |
TCNssharewithCNNsmostshortcomings(seeSection3.1.1),withtheonlyexception
oftheEuclideankernel.

Information2023,14,598 6of35
3.2. RecurrentNeuralNetworks
RecurrentNeuralNetworks(RNNs)[45]aimtoexploretherelationsbetweenthecurrent
timeseriessamplesandthepastones. AnRNNprocessesonetimeseriessampleatatime
f(·)
to approximate the skeleton and determine the model order q implicitly. While in
Equation(1)themodelorderqisassumedtobeconstant,RNNsexhibitadynamictemporal
behaviour,astheydonotrequireafixedmodelorderqandtheyauto-determinehowfar
back to look in the past. An RNN is composed of recurrent layers, which process one
inputsampleatatime. TheearliestRNNapplicationsfortimeseriesforecasting[56,57]are
replacedbymorespecificandsophisticatedrecurrentarchitectures,thatis,ElmanRecurrent
NeuralNetworks[58],EchoStateNetworks[59],LongShort-TermMemoryNetworks[60],and
GatedRecurrentUnits[61].
3.2.1. ElmanRecurrentNeuralNetworks
Elman[58],Williams-Zipser[62],andJordan[63]RNNsaretheearliestRecurrentNeural
Networksproperlydesignedtohandletemporalpatternsintimeseries.Inparticular,Elman
(cid:126)
RNN(ERNN)usesarecurrentlayer,whichyieldsanoutputh thatdependsonthecurrent
t
(cid:126)
sample(cid:126)x t andthepreviousoutput h t−1 byafunctiong(·)andagenericsetoftime-shared
parametersω,asdescribed:
|     |     | (cid:126) | (cid:126)         |     |     |
| --- | --- | --------- | ----------------- | --- | --- |
|     |     | h =       | g ((cid:126)x , h | )   | (6) |
|     |     | t         | ω t t−1           |     |     |
(cid:126)
whereh isproducedbythesamerecurrentlayer,i.e.,:
t−1
|     |     | (cid:126) |                     | (cid:126) |     |
| --- | --- | --------- | ------------------- | --------- | --- |
|     |     | h t−1 =   | g ω ((cid:126)x t−1 | , h t−2 ) | (7) |
andsoon. Thebasicrecurrentlayer,oftencalledavanillacell,workslikeafullyconnected
layer with a fixed number of units, jointly applied to the current input(cid:126)x and the last
t
(cid:126)
outputh t−1 :
|     |     | (cid:16)  |                    | (cid:17)   |     |
| --- | --- | --------- | ------------------ | ---------- | --- |
|     |     | (cid:126) | (cid:126)          | +(cid:126) |     |
|     |     | h t = g   | V(cid:126)x t +W h | t−1 b      | (8) |
In this case, the set of parameters of a recurrent layer is ω = {V,W, (cid:126) b}, where V is the
(cid:126)
input-recurrentweightmatrix,W istherecurrent-recurrentweightmatrix,andbisthebias
InEquation(8),g(·)isanonlinearactivationfunction,usuallyahyperbolictangent.
vector.
ERNNtimeseriesforecastingapplicationsaresummarisedinTable3.
Table3.ElmanRNNapplicationsfortimeseriesforecasting.
| Ref. | Year |     |     | Application          |     |
| ---- | ---- | --- | --- | -------------------- | --- |
| [64] | 2017 |     |     | Electricityload      |     |
| [65] | 2018 |     |     | Electricityload      |     |
| [66] | 2018 |     |     | Energyconsumption    |     |
| [14] | 2019 |     |     | Monthlyprecipitation |     |
| [16] | 2021 |     |     | AirQualityIndex      |     |
3.2.2. ShortcomingsofRecurrentNeuralNetworks
Recurrent neural networks based on the vanilla cell suffer from unstable training,
which prevents the network from grasping long-term dependencies. Recurrent networks,
like most neural networks, are trained by gradient descent [67], and backpropagation [67]
(Backpropagation is denoted Backpropagation Through Time (BPTT), when applied to re-
currentneuralnetworks)isusedtocomputethegradientofthelossfunctionw.r.t. the
network’sweights. Whenback-propagationisappliedtodeepnetworks,theproblemsof
vanishingorexplodinggradients[45]mayarise. Astheerrorgradientisback-propagated,
someofitscomponentsmighteithergetverysmall, givinganegligiblecontributionto
thecorrespondingweightupdate,orverylarge,leading,inthisway,tounstabletraining.
Overtheyears,severalapproacheshavebeenproposedtocopewithunstablegradients.

Information2023,14,598 7of35
Amongthemostsuccessfulapproachesarereservoircomputingmethods,e.g.,EchoStateNet-
works[59](seeSection3.2.3),andgatedcells,e.g.,LongShort-TermMemory(LSTM)cells[60]
andGatedRecurrentUnits(GRU)[61]. Agatedcellcontrolshowmuchinputinformation
flowsthroughthelayerandpreventsderivativesfromvanishingorgettinglarge.
3.2.3. EchoStateNetworks
EchoStateNetworks(ESNs)weresuggestedbyH.Jaeger[59]in2001asavariantof
ERNNs. ESNsarereallyeffectiveindealingwithchaoticmultivariatetimeseries[68]. Inaddi-
tion,thesenetworksmitigatetheunstablegradientproblemandaremorecomputationally
efficientduetotheuseoffixed,randomweightmatricesfortherecurrentlayers. Basedon
thevanillacellofERNNs(seeEquation(8)),ESNsavoidbackpropagationontherecurrent
layerbysettingV andW asfixed(i.e.,non-trainable)randommatrices. Furthermore,a
givensparsitylevelisconsideredinmatrixW. Althoughrandommatricesareanadvantage
ofENSstomitigatetheunstablegradientproblem,they,atthesametime,representamajor
ESNsshortcomingsincetheymakeparticularlydifficulttheapplicationofcommoninter-
pretabilityapproaches,e.g.,gradient-basedapproaches[69,70]. ESNtimeseriesforecasting
applicationsaredescribedinTable4.
Table4.ESNapplicationsontimeseriesforecasting.
| Ref. | Year |                                       | Application                   |     |
| ---- | ---- | ------------------------------------- | ----------------------------- | --- |
| [71] | 2017 |                                       | Fuelcellvoltageageing         |     |
| [32] | 2017 |                                       | Healthofautomotivebatteries   |     |
| [72] | 2017 |                                       | Sluggingflowphenomenon        |     |
| [13] | 2017 |                                       | Temperature/Rainfall          |     |
| [73] | 2018 |                                       | Lorenz/Rossler/Sunspot-Runoff |     |
| [34] | 2019 |                                       | Industrialprocesses           |     |
| [35] | 2019 |                                       | Fuelcelldurability            |     |
| [74] | 2019 |                                       | Photovoltaicvoltage           |     |
| [75] | 2020 |                                       | Electricityload               |     |
| [76] | 2020 |                                       | Electricityload               |     |
| [77] | 2020 | Energyconsumption/Windpowergeneration |                               |     |
| [78] | 2020 |                                       | Temperatureofexhaustgas       |     |
| [36] | 2020 |                                       | Faultsinairplaneengines       |     |
| [79] | 2020 |                                       | Multipletimeseries            |     |
| [25] | 2020 |                                       | Bloodglucoseconcentration     |     |
| [80] | 2021 |                                       | Multipletimeseries            |     |
| [81] | 2021 |                                       | Electricalload                |     |
| [16] | 2021 |                                       | AirQualityIndex               |     |
| [82] | 2022 |                                       | Chaotictimeseries             |     |
3.2.4. LongShort-TermMemory
LongShort-TermMemory(LSTM)Networks[60]wereoriginallyproposedfornatural
languagemodelling. TheLSTMcell(seeFigure6)usesthreegatingmechanisms: input,forget
andoutputgates. Firstly,theinputofLSTMlayers,whichiscomposedofthecurrentinput
| (cid:126)x (cid:126) |     |     |     |     |
| -------------------- | --- | --- | --- | --- |
t andtheoutput h t−1 fromthelasttimestepareiscombinedintothecurrentinputvector
(cid:126)
i asfollows:
t
|     | (cid:126) = | γ(W (cid:126)x +U | (cid:126) +(cid:126) ) |     |
| --- | ----------- | ----------------- | ---------------------- | --- |
|     | i t         | i t               | i h t−1 b i            | (9) |
where γ(·) can be any sigmoidal function (e.g., logistic or hyperbolic tangent ones) and
(cid:126)
{W,U, b}isasetofparameters. Furthermore,thethreegatesarecomputedas:
i i i
|     |              |                   | (cid:126) +(cid:126) |      |
| --- | ------------ | ----------------- | -------------------- | ---- |
|     | (cid:126)g = | σ(W (cid:126)x +U | h b )                | (10) |
|     | t            | g t               | g t−1 g              |      |
|     | (cid:126)    |                   | (cid:126) +(cid:126) |      |
|     | f =          | σ(W (cid:126)x +U | h b )                | (11) |
|     | t            | f t               | f t−1 f              |      |

Information2023,14,598 8of35
(cid:126) +(cid:126)
|     |     | (cid:126)o = | σ(W (cid:126)x +U | h     | b ) | (12) |
| --- | --- | ------------ | ----------------- | ----- | --- | ---- |
|     |     | t            | o t               | o t−1 | o   |      |
(cid:126)
whereσ(·)isthelogisticfunction,(cid:126)g t , f t ,(cid:126)o t aretheinput,forget,andoutputgates,respec-
| {W (cid:126) | }, {W | (cid:126) | }, {W (cid:126) | }   |     |     |
| ------------ | ----- | --------- | --------------- | --- | --- | --- |
tively, and g ,U g , b g f ,U f , b f o ,U o , b o are the respective sets of parameters.
|     | inner | state(cid:126)c |     |     | (cid:126) i |     |
| --- | ----- | --------------- | --- | --- | ----------- | --- |
Furthermore, the LSTM’s t is updated by a linear combination of t and the
| previousinnerstate(cid:126)c | :   |     |     |     |     |     |
| ---------------------------- | --- | --- | --- | --- | --- | --- |
t−1
|                                        |     |              | (cid:12)(cid:126)                              | (cid:126)                  |                              |      |
| -------------------------------------- | --- | ------------ | ---------------------------------------------- | -------------------------- | ---------------------------- | ---- |
|                                        |     | (cid:126)c t | =(cid:126)g t i t +                            | f t (cid:12)(cid:126)c t−1 |                              | (13) |
| where(cid:12)istheelement-wiseproduct. |     |              |                                                |                            | (cid:126)                    |      |
|                                        |     |              | Finally,theoutput                              |                            | h t ofaLSTMlayerisdefinedas: |      |
|                                        |     |              | (cid:126) =(cid:126)o (cid:12) tanh((cid:126)c | )                          |                              |      |
|                                        |     |              | h t t                                          | t                          |                              | (14) |
| x t                                    | i t |              |                                                |                            |                              |      |
Input
| h t-1 |     |     | c t |     |     |     |
| ----- | --- | --- | --- | --- | --- | --- |
tanh
| x          | g   |     |       |     |     |     |
| ---------- | --- | --- | ----- | --- | --- | --- |
| t          | t   |     |       |     |     |     |
| Input Gate |     |     | c t-1 |     |     |     |
h
t-1
h t
| x   | f   |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- |
| t   | t   |     |     |     |     |     |
Forget Gate
h
t-1
| x   | o   |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- |
| t   | t   |     |     |     |     |     |
Output Gate
h
t-1
Figure6.Long-ShortTermMemorycellarchitecture.
LSTMtimeseriesforecastingapplicationsaredescribedinTable5.
Table5.LSTMapplicationsontimeseriesforecasting.
| Ref.    |     | Year |     |                              | Application               |     |
| ------- | --- | ---- | --- | ---------------------------- | ------------------------- | --- |
| [17]    |     | 2016 |     |                              | Stockmarket               |     |
| [83]    |     | 2016 |     |                              | Electricityload           |     |
| [84]    |     | 2016 |     |                              | Trafficflow               |     |
| [19]    |     | 2017 |     |                              | Stockprices               |     |
| [85,86] |     | 2017 |     |                              | Stockmarket               |     |
| [87]    |     | 2017 |     |                              | Electricityload           |     |
| [88]    |     | 2017 |     |                              | Airquality                |     |
| [26]    |     | 2018 |     |                              | ForecastingCancerGrowth   |     |
| [89,90] |     | 2018 |     |                              | Stockmarket               |     |
| [20]    |     | 2018 |     |                              | Stockprices               |     |
| [7]     |     | 2018 |     |                              | Electricityprice          |     |
| [24]    |     | 2018 |     |                              | Diabetesmellitus          |     |
| [91]    |     | 2018 |     |                              | Rainfall-runoffmodelling  |     |
| [92]    |     | 2018 |     |                              | Predictingwatertabledepth |     |
| [93,94] |     | 2018 |     |                              | Electricityload           |     |
| [33]    |     | 2018 |     |                              | Lifepredictionofbatteries |     |
| [10]    |     | 2018 |     | Solarpowerandelectricityload |                           |     |
| [95]    |     | 2018 |     |                              | Solarintensity            |     |
| [96]    |     | 2018 |     |                              | Airquality                |     |
| [97]    |     | 2019 |     |                              | UCIdatasets               |     |
| [98]    |     | 2019 |     |                              | Buildingload              |     |
| [31]    |     | 2019 |     |                              | Petroleumproduction       |     |
| [14]    |     | 2019 |     |                              | Monthlyprecipitation      |     |
| [99]    |     | 2019 |     |                              | Weatherforecasting        |     |

Information2023,14,598 9of35
Table5.Cont.
|     | Ref.  |     | Year |     |                                 | Application           |     |     |
| --- | ----- | --- | ---- | --- | ------------------------------- | --------------------- | --- | --- |
|     | [18]  |     | 2020 |     |                                 | Stockmarket           |     |     |
|     | [100] |     | 2020 |     |                                 | COVID-19              |     |     |
|     | [79]  |     | 2020 |     |                                 | Multipletimeseries    |     |     |
|     | [101] |     | 2021 |     | Weather/AirQuality/Clinicaldata |                       |     |     |
|     | [16]  |     | 2021 |     |                                 | AirQualityIndex       |     |     |
|     | [102] |     | 2022 |     |                                 | Financialmarkets      |     |     |
|     | [12]  |     | 2023 |     | CO                              | /Temperature/Humidity |     |     |
2
3.2.5. GatedRecurrentUnits
RNNs based on Gated Recurrent Units (GRUs) [61] were introduced for Statistical
Machine Translation. A GRU layer, as shown in Figure 7, uses two gating mechanisms:
an update and a reset gate. Both the reset and the update gate depend on(cid:126)x and (cid:126) h .
t t−1
AnalogouslytoLSTM,theresetgate(cid:126)r andtheupdategate(cid:126)u arecomputedas:
|     |     |     |                | t               |                        | t        |     |      |
| --- | --- | --- | -------------- | --------------- | ---------------------- | -------- | --- | ---- |
|     |     |     |                | (cid:16)        | (cid:126) +(cid:126)   | (cid:17) |     |      |
|     |     |     | (cid:126)r = σ | W (cid:126)x +U | h                      | b        |     | (15) |
|     |     |     | t              | r t             | r t−1                  | r        |     |      |
|     |     |     | (cid:16)       |                 |                        | (cid:17) |     |      |
|     |     |     | (cid:126)u = σ | W (cid:126)x +U | (cid:126) h +(cid:126) | b        |     | (16) |
|     |     |     | t              | u t             | u t−1                  | u        |     |      |
whereσ(·)isthelogisticfunctionandtherestoftheparametershavethesamemeaningas
theLSTM(seeSection3.2.4). Furthermore,anintermediateoutput (cid:126) h(cid:48) isgivenby:
t
|     |     |     | (cid:16)                   |                           |                     | (cid:17)      |     |      |
| --- | --- | --- | -------------------------- | ------------------------- | ------------------- | ------------- | --- | ---- |
|     |     |     | (cid:126) h (cid:48) =tanh | W(cid:126)x +U((cid:126)r | (cid:12)(cid:126) h | )+(cid:126) b |     | (17) |
|     |     |     | t                          | t                         | t t−1               |               |     |      |
(cid:126)
where {W,V, b} is an additional set of parameters and (cid:12) is the element-wise product.
|     |     | (cid:126) |     |     |     |     | (cid:126) h(cid:48) (cid:126) |     |
| --- | --- | --------- | --- | --- | --- | --- | ----------------------------- | --- |
Finally, the output h t of the GRU layer is given by the sum of and h t−1 , weighted
t
element-wisebytheupdategate:
|     |     |     | (cid:126)     | (cid:12)(cid:126)         | )(cid:12)(cid:126) | (cid:48) |     |      |
| --- | --- | --- | ------------- | ------------------------- | ------------------ | -------- | --- | ---- |
|     |     |     | h =(cid:126)u | h +((cid:126)e−(cid:126)u |                    | h        |     | (18) |
|     |     |     | t t           | t−1                       | t                  | t        |     |      |
where(cid:126)eisacolumnvectorwhoseelementsareallequalto1.
GRUtimeseriesforecasting
applicationsaredescribedinTable6.
h
t-1
u
t
Update Gate
| x   |     | u   |     |     |     |     | h   |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| t   |     | t   |     |     |     |     | t   |     |
e-u
|       | e   |     | t   |     |      |     |     |     |
| ----- | --- | --- | --- | --- | ---- | --- | --- | --- |
| h t-1 |     |     |     |     | h' t |     |     |     |
r
t
|     |     | Reset Gate |     | tanh |     |     |     |     |
| --- | --- | ---------- | --- | ---- | --- | --- | --- | --- |
h
t-1
x
t
Figure7.ArchitectureofaGRUcell.Thecolumnvector(cid:126)eiscomposedofelementsthatareallequalto1.

Information2023,14,598 10of35
Table6.ApplicationsontimeseriesforecastingusingGRU-basedRecurrentNeuralNetworks.
Ref. Year Application
[84] 2016 Trafficflow
[8] 2017 Electricityload
[103] 2018 Photovoltaicforecasting
[7] 2018 Electricityprice
[24] 2018 Diabetesmellitus
[97] 2019 UCIdatasets
[79] 2020 Multipletimeseries
[104] 2021 Airquality/Stockprices/Householdelectricpower
3.2.6. ShortcomingsofLSTMsandGRUs
It has to be remarked that, even if training is stable, it can be hard for recurrent
networkstolearndependenciesbetweendistantsequencesamples.Forinstance,arecurrent
networkthatgeneratesanoutputsequencestartingfromaninputsequenceisshownin
Figure8.
y19 y20 y21 y59 y60 y61
OUT Layer OUT Layer OUT Layer OUT Layer OUT Layer OUT Layer
h19 h20 h21 h59 h60 h61
Recurrent Recurrent Recurrent Recurrent Recurrent Recurrent
Layer Layer Layer Layer Layer Layer
. . . . . . . . .
x19 x20 x21 x59 x60 x61
Figure8. Theredpathintherecurrentmodeldenotestheflowthatinformationaboutaninput
sample(x )mustfollowbeforereachinganoutputlayer(y )thatmightrequireit.
20 60
Supposingthattheoutputelementatpositiont =60hasastrongdependencyonthe
inputatpositiont = 20,informationabouttheinputsample x isusefultopredictthe
20
outputsampley . Theoutputsampley ispredictedstartingfromh ,alossysummary
60 t t
ofthepastinputsyieldedbytherecurrentlayer;hence,theonlywayfortheoutputlayer
to know about x is through h . The recurrent layer first captures information about
20 60
x throughh ,whichhastopassbymanystepsandthenaggregateinformationabout
20 20
manyotherinputelements,beforeachievingh . Thereisnoguaranteethataftersomany
60
recurrentsteps,adequateinformationaboutx ispreservedintoh . Infact,h mayjust
20 60 60
containinformationaboutthemostrecentsamplesandhavenoinformationaboutx atall.
20
Theshort-termmemoryofrecurrentnetworksisoneoftheirmajordrawbacksandoneof
themainreasonswhyattentionmechanismsandTransformerswereoriginallyintroduced
indeeplearning(seeSection4.1).
3.3. HybridsandVariantsofDeepNeuralNetworks
Inrecentyears,specificdeepneuralnetworkshavebeenproposedashybridsorvariants
oftheaforementionedarchitectures.Hybridmodelscombinemultiplestatisticalormachine
learningmethodstoimprovetherobustnessandaccuracyofforecasting. Towardsthesame
goalaretheworksthatproposevariantsofdeepneuralarchitecturesproperlyadapted
fortimeseriesforecastingtasks. Hybridsandvariantsofdeepneuralnetworkssharethe
same limitations as the models they are based on. The most successful approaches are
summarisedinTable7.

Information2023,14,598 11of35
Table7.Applicationsintimeseriesforecastingusingvariantsandhybridsofcommondeepneural
networks.Thesymbol‘+’denotesacombinationofmultiplemodelsormethodologies.GARCHand
ANNacronymstandforGeneralizedAutoRegressiveConditionalHeteroskedasticity[105]andArtificial
NeuralNetworks,respectively.
| Ref. Year  |     | Architecture     |     |     |     | Application       |     |
| ---------- | --- | ---------------- | --- | --- | --- | ----------------- | --- |
| [106] 2016 |     | Autoencoder+LSTM |     |     |     | Solarpower        |     |
| [107] 2017 |     | Autoencoder+LSTM |     |     |     | Stockprices       |     |
| [108] 2017 |     | CNN+LSTM         |     |     |     | Stockprices       |     |
| [109] 2018 |     | CNN+LSTM         |     |     |     | Electricityprices |     |
| [110] 2018 |     | CNN+LSTM         |     |     |     | Electricityload   |     |
| [111] 2018 |     | CNN+LSTM         |     |     |     | Windspeed         |     |
LSTM+Attentionmechanism
| [112] 2018 |     |     |     |     |     | Stockmarket |     |
| ---------- | --- | --- | --- | --- | --- | ----------- | --- |
(seeSection4.1.1)
| [113] 2018 |     | LSTM+GRU     |     |     |     | Stockprices          |     |
| ---------- | --- | ------------ | --- | --- | --- | -------------------- | --- |
| [114] 2018 |     | GARCH+LSTM   |     |     |     | Stockprices          |     |
| [115] 2018 |     | GRUvariant   |     |     |     | Trafficforecasting   |     |
| [116] 2018 |     | CNN+LSTM     |     |     |     | PM 2.5 concentration |     |
| [117] 2018 |     | ANN+LSTM+CNN |     |     |     | PM concentration     |     |
2.5
LSTM+Attentionmechanism
| [118] 2019 |     |     |     |     | OnlineSales/Electricityprices |     |     |
| ---------- | --- | --- | --- | --- | ----------------------------- | --- | --- |
(seeSection4.1.1)
LSTM+Attentionmechanism
| [119] 2019 |     |     |     |     |     | Solargeneration |     |
| ---------- | --- | --- | --- | --- | --- | --------------- | --- |
(seeSection4.1.1)
LSTM+Attentionmechanism
| [120] 2019 |     |     |     |     |     | Electricityload |     |
| ---------- | --- | --- | --- | --- | --- | --------------- | --- |
(seeSection4.1.1)
CNN+Attentionmechanism
| [27] 2019 |     |     |     |     |     | Traffic/Stockmarket |     |
| --------- | --- | --- | --- | --- | --- | ------------------- | --- |
(seeSection4.1.1)
| [121] 2020 |     | CNN+LSTM        |     |     |     | Stockmarket/Temperature |     |
| ---------- | --- | --------------- | --- | --- | --- | ----------------------- | --- |
| [122] 2020 |     | LSTM+FuzzyLogic |     |     |     | COVID-19                |     |
| [23] 2020  |     | TCN+Attention   |     |     |     | RemainingUsefulLife     |     |
| [123] 2023 |     | TCN+LSTM/GRU    |     |     |     | ChaoticTimeSeries/ECG   |     |
3.4. GraphNeuralNetworks
Arecentpromisingresearchdirectioninmultivariatetimeseriesforecastingisthe
applicationofGraphNeuralNetworks(GNNs)[124,125]. TheoriginaldomainofGNNsis
thehandlingofspatialdependenciesamongentitiesinagraph-modelledproblem. Indetail,
GNNscanbeusedtogeneraterepresentationsofsuchentitiesthatdependonthestructure
ofthegraphandonanyadditionalinformation. AgraphG(cid:48) isformallydefinedasatuple
| G(cid:48) = [V,E], | V   |     |     | E   |     |     |     |
| ------------------ | --- | --- | --- | --- | --- | --- | --- |
where denotes the set of nodes and is the set of edges, the connections
betweenthenodesofthegraph,represented,inthiscase,withanadjacencymatrix. The
definition of this matrix is based on a metric function that can be either a priori fixed or
learned during the training process [125]. The basic idea of a GNN can be summarised
bytheuseofthreemainoperators: aggregate,combine,andreadout. Thek-thGNNlayer
performstheaggregateandcombinesoperators. Theformerconsistsofagglomerating,
foreachgraphnodev ∈ V,informationfromitsneighbourhood N(v)asdefinedbythe
adjacencymatrix:
|     | (cid:126) | aggregate((cid:126) hk−1 |     |         |     |     |      |
| --- | --------- | ------------------------ | --- | ------- | --- | --- | ---- |
|     |           | hk =                     | : u | ∈ N(v)) | ∀k  | >1  | (19) |
|     |           | N(v)                     | u   |         |     |     |      |
where (cid:126) hk−1isthefeaturevectoroftheu-thneighbouringnodeofv,yieldedbytheprevi-
u
(cid:126)
ousGNNlayer k−1, and hk istheaggregatedinformation. Thelattercombinesthe
N(v)
|                       |     | (cid:126) hk         |     | (cid:126) hk−1ofthecurrentnodev: |     |     |     |
| --------------------- | --- | -------------------- | --- | -------------------------------- | --- | --- | --- |
| aggregatedinformation |     | withthefeaturevector |     |                                  | v   |     |     |
N(v)
|     |     | (cid:126) combine((cid:126) hk−1, | (cid:126) |     |        |     |      |
| --- | --- | --------------------------------- | --------- | --- | ------ | --- | ---- |
|     |     | hk =                              | hk        | )   | ∀k >1. |     | (20) |
|     |     | v                                 | v N(v)    |     |        |     |      |

Information2023,14,598 12of35
Whenk =1theaggregateoperatorisnotdefined,whereasthecombineoperatorreducesto:
|     | (cid:126) h1 | =(cid:126)x |     |      |
| --- | ------------ | ----------- | --- | ---- |
|     |              | v v ,       |     | (21) |
where(cid:126)x representstheinputfeaturevectorassociatedtothev-thnode. Furthermore,the
v
readoutoperatorisappliedontheoutputofthelastGNNlayerKinordertoobtainafinal
| (cid:126) representingthewholegraphG(cid:48) |     | = [V,E]: |     |     |
| -------------------------------------------- | --- | -------- | --- | --- |
vector h G
|     | (cid:126) h =readout((cid:126) | h K : v ∈ | V)  | (22) |
| --- | ------------------------------ | --------- | --- | ---- |
|     | G                              | v         |     |      |
Inthecaseofmultivariatetimeseriesforecasting,GNNshavebeensuccessfullyappliedas
featureselectionmechanisms. ItisimportanttoremarkthatGNNscouldalsobeappliedto
spatio-temporaltimeseriesforecastingwhichisnottheobjectofthesurvey. GNNtimeseries
forecastingapplicationsaredescribedinTable8.
Table8.GNNapplicationsontimeseriesforecasting.
| Ref. Year  |                                                  | Application            |     |     |
| ---------- | ------------------------------------------------ | ---------------------- | --- | --- |
| [28] 2020  | Traffic/Electricityload/Exchangerate             |                        |     |     |
| [29] 2021  | Solarenergy/Traffic/Electricityload/Exchangerate |                        |     |     |
| [126] 2022 |                                                  | Stockmarket            |     |     |
| [127] 2022 | PM                                               | 2.5 /Traffic/Windspeed |     |     |
| [128] 2022 |                                                  | Stockmarket            |     |     |
| [129] 2022 | Electricityload/Solarenergy/Traffic              |                        |     |     |
[21] 2022 Solarenergy/Windpowergeneration/Electricityload/Exchangerate
| [130] 2022 | Solarenergy/Traffic/Electricityload/Exchangerate |     |     |     |
| ---------- | ------------------------------------------------ | --- | --- | --- |
| [22] 2023  | Solarenergy/Traffic/Electricityload/Exchangerate |     |     |     |
3.5. DeepGaussianProcesses
Let D = (x(cid:126) ,x(cid:126) ,...,x(cid:126) ) be a data set and Y = (y(cid:126) ,y(cid:126) ,...,y(cid:126) ) the target output, a
| 1 2 | n   |     | 1 2 n |     |
| --- | --- | --- | ----- | --- |
GaussianProcess[131]isaBayesianmodelcomposedofacollectionofrandomvariables,
any finite number of which have a joint Gaussian distribution, and it is fully defined
by a mean function m((cid:126)x ) and covariance function k((cid:126)x,(cid:126)x ), which is usually a Mercer
| i   |     |     | i j |     |
| --- | --- | --- | --- | --- |
kernel[131,132]. TheanalyticalsolutionofaGaussianProcessentailscomputingtheinverse
ofthecovariancematrixofobservations,whichhasacomputationalcomplexityofO(n3).
A common approach for coping with this computational drawback is the use of Sparse
GaussianProcess[133]. Thismethodconsistsofconsideringareducedsetof m (m (cid:28) n)
trainingsamples,theso-calledinducingvariables,reducing,inthisway,thecomplexityto
O(nm2). AsequenceofGaussianProcessesdefinesaBayesianmodelcalledDeepGaussian
Process (DGP) [134]. As shown in Figure 9, in DGPs the output of the single Gaussian
ProcesslocatedatthepreviouslayerisfedasaninputtotheGaussianProcesslocatedat
thenextlayer. Unliketherestofthedeeplearningtechniques,DeepGaussianProcesses
canestimatenotonlythevalueoffuturetimeseriessamplesbutalsoprovideaconfidence
intervalofthepredictivetimeseriesvaluerepresenting,inthisway,theuncertaintyofthe
model. DGPtimeseriesforecastingapplicationsaredescribedindetailinTable9.
Table9.DGPapplicationsontimeseriesforecasting.
| Ref.  | Year |     | Application                   |     |
| ----- | ---- | --- | ----------------------------- | --- |
| [135] | 2017 |     | CropYieldforecasting          |     |
| [136] | 2020 |     | CropYieldforecasting          |     |
| [137] | 2022 |     | Electricityload               |     |
| [138] | 2023 |     | Car-hailingdemand             |     |
| [139] | 2023 |     | Ozoneconcentrationforecasting |     |

Information2023,14,598 13of35
Figure9.DeepGaussianProcesses.InthefigureX,Y representthedatasetandthedesiredoutput,
respectively, f(i)isthelatentfunctiontobeestimatedandm,k representthemeanandcovariance
i i
functionofi-thlayer.
3.6. GenerativeModels
Amongthelatesttrendsindeeplearningresearch,therearetheso-calledgenerative
models, specifically Generative Adversarial Networks (GANs) and Diffusion Models (DMs).
Both families are popular for their groundbreaking capabilities in generating synthetic
images. ThesesuccessesencouragedresearcherstoapplyGANsandDMstosequential
dataaswell,includingtimeseries. Asgenerativemodels,bothmethodologieshavebeen
usedfortimeseriesgenerationtasks. However,itcanadaptthemforothertimeseries-related
tasksaswell,specificallytimeseriesforecasting. Sections3.6.1and3.6.2provideanoverview
ofGANsandtheirusagefortimeseriesforecasting,respectively;Sections3.6.3and3.6.4
discussdiffusionmodelsandtheirapplicationstotimeseriesforecasting,respectively.
3.6.1. GenerativeAdversarialNetworks
A GAN [140] is composed of two separate artificial neural networks: a generator
networkGthatgeneratessyntheticdata,withthesamedistributionoftheinputones,and
adiscriminatornetworkDthatclassifiesinputdataaseitherrealorsynthetic. GandDare
trainedwithanadversarialtrainingapproach. G takesrandomnoiseasinputandithas
totransformthenoiseintoasyntheticdatasamplefollowingthesamedistributionofthe
realdata. Dreceivesbothrealandgeneratedsamplesanditestimatestheprobabilitythat
anygivendatasamplecomesfromtherealdataratherthanfromthegenerator. Thetwo
networksaretrainedjointlywithaminimaxtwo-playergame[140],i.e.,thediscriminator
istrainedtomaximisethecorrectclassificationratioforbothrealandgeneratedsamples.
Whereas,thegeneratorhasthegoaltotrickthediscriminatorintomisclassifyinggenerated
samplesbyminimisingthecorrectclassificationratio. Thistrainingprocedureisexpressed
bytheobjectivefunction:
minmaxV(D,G) =E [logD((cid:126)x)]+E [log(1−D(G((cid:126)z)))]. (23)
G D
(cid:126)x∼px ((cid:126)x) (cid:126)z∼pz ((cid:126)z)
where,(cid:126)x isarealdatapoint, sampledfromtherealdatadistribution p ((cid:126)x);(cid:126)z isanoise
x
vector,sampledfromadistribution p ((cid:126)z),apriorifixed;D((cid:126)x)istheprobabilitydistribution
z
estimatedbythediscriminator;G((cid:126)z)isthesampleproducedbythegenerator,startingfrom
thenoise(cid:126)z. GANscanbeimplementedbyanyneuralarchitectureforthegeneratorand
thediscriminator. Forinstance,GandDcanbeimplementedbyMLPs[67],asoriginally
proposedin[140],CNNs(seeSection3.1),withsomearchitecturalconstraintstostabilise
thetrainingprocedure[141],orLSTM(seeSection3.2.4)networks[142].

Information2023,14,598 14of35
3.6.2. GenerativeAdversarialNetworksinTimeSeriesForecasting
Inliterature,therearetwomainapproachesforusingGANsintimeseriesforecast-
ing: asdataaugmentationorasanend-to-endforecastingmodel. Intheformercase,GANs
generate synthetic time series in a given domain (e.g., financial or health-related time
series) in order to augment the original small data set. The augmented data set, with
bothrealandgeneratedtimeseries,isthenusedtotrainatraditionalforecastingmodel,
e.g., a model based on an LSTM network. In the latter case, the forecasting model is a
GANitself,anditgeneratesfuturesamplesstartingfrompreviousonesand,eventually,
otherexogenousinputs(Intimeseriesforecasting,avariableissaidtobeexogenousifit
is not a time series sample, but it can still affect the time series samples. For instance,
temperature may be an exogenous variable in rainfall time series forecasting) [143]. For
example,in[144]aGANisfirstlyusedtoaugmentabuildingenergyconsumptiondataset
andthen,anensembleoffivetraditionalpredictivemodelsistrainedonsuchaugmented
data set. In particular, to augment the data set, Conditional GANs (CGANs) [145] and
InformationMaximisingGANs(InfoGANs)[146]arecomparedwitheachother. Similarly,
in[147]COVID-19epidemicdataisgeneratedbyacustomGANwithanLSTMgenerator
andanMLPdiscriminator.Furthermore,aTransformerisusedtomakeaforecastingmodel
trainedontheGAN-augmenteddataset. Moreover,someGAN-basedmodelshavebeen
specificallydevelopedfortimeseriesgeneration,e.g.,QuantGAN[148],forfinancialtime
series with long-term time dependencies, SynSigGAN [149], for continuous biomedical
signals,RecurrentConditionalGANs(RCGANs)[150],formedicaldata,TimeGAN[151],a
frameworkfordomain-agnostictimeseriesgeneration,ConditionalSig-WassersteinGAN
(Sig-WCGAN) [152], and TTS-GAN [153], entirely based on Transformers. Some of the
aforementionedGANs,e.g.,RCGAN,TimeGAN,Sig-WCGAN,areconditionalGANs[145],
i.e,timeseriesarenotgeneratedfromonlyrandomnoisebutalsoconditionedonthereal
timeseriesand/orrelatedinformation,e.g.,exogenousinputs,forimprovinggenerated
timeseriesquality. TheuseofconditionalGANsispopularforend-to-endforecasting,
wherethegeneratedtimeserieswindow,typicallyintheshort-termfuture,isoftencon-
ditioned on previous samples and on other exogenous inputs (see [154–158]). Table 10
collectssomeworksonGANapplicationsfortimeseriesforecasting.
Table10.GANapplicationsontimeseriesforecasting.
| Ref.  | Year |                                             | Application         |
| ----- | ---- | ------------------------------------------- | ------------------- |
| [159] | 2018 |                                             | Stockmarket         |
| [160] | 2019 |                                             | Trafficforecasting  |
| [154] | 2019 | Lorenz/Mackey-Glass/InternetTrafficdata     |                     |
| [161] | 2019 |                                             | Medicineexpenditure |
| [162] | 2019 |                                             | Electricityload     |
| [163] | 2020 |                                             | Stockprice          |
| [164] | 2020 | Long-termbenchmarkdatasets(seeSection6.2)   |                     |
| [165] | 2020 |                                             | Soiltemperature     |
| [166] | 2021 | Stockmarket/Energyproduction/EEG/Airquality |                     |
| [156] | 2021 |                                             | InternetTrafficdata |
[167] 2021 StoreItemDemand/InternetTraffic/Meteorologicaldata
| [168]     | 2021 |     | Windpower/Solarpower    |
| --------- | ---- | --- | ----------------------- |
| [144]     | 2021 |     | Energyconsumption       |
| [169]     | 2021 |     | Electricityload         |
| [170]     | 2022 |     | Trajectoriesforecasting |
| [147,155] | 2022 |     | COVID-19                |
| [157,158] | 2022 |     | Photovoltaicpower       |
| [171]     | 2022 |     | Buildingpowerdemand     |
| [172]     | 2023 |     | Financialtimeseries     |

Information2023,14,598 15of35
3.6.3. DiffusionModels
A new family of generative architectures are the diffusion models. They have been
showingcutting-edgeperformanceingeneratingsamplesthatreflecttheobserveddata
indifferentdomains,e.g.,imagegeneration,videogeneration,andtextsynthesis. Three
key formulations are used to develop diffusion-based approaches for short-term time
series applications: denoising diffusion probabilistic models (DDPMs) [173,174], score-
basedgenerativemodels(SGMs)[175],andstochasticdifferentialequations(SDEs)[176].
DiffusionmodelsaimtoapproximateagenerativeprocessG thatgeneratesnewsamples
drawn from an underlying distribution q(x), given some observed data x from the same
distribution. ToapproximateG,intheforwardprocess,aprogressiveinjectionofGaussian
noisesontheobserveddataisperformedbythemajorityofdiffusionmodels. Furthermore,
areverseprocessisapplied,byalearnabletransitionkernel,toreconstructtheoriginal
data. Mostdiffusionmodelsassumethat,afterafinitenumberofnoiseinjectionsteps,q(x)
distributionoftheobserveddatawillbecomeaGaussiandistribution. Therefore,thegoal
ofdiffusionmodelsistofindtheprobabilisticprocessP thatapproximatesq(x)distribution
oforiginaldatafromtheGaussiandistribution. Inthismanner,anysampleofGaussian
distributioncanbetransformedbyP intoanewsampleofq(x)distributionofobserved
datax. Theprincipleofdiffusionmodelsistoprogressivelyperturbtheobserveddatax
witharandomnoisebyaforwarddiffusionprocess F beforerecoveringtheoriginaldata
usingabackwardreversediffusionprocessB. AdeepneuralnetworkisusedintheBprocess
toapproximatetheamountofnoisethatmustberemovedinthedenoisingstepstorecover
theoriginaldata. Forthesakeofreadability,thetheoreticalfoundationsofdiffusionmodels
andtheirmainarchitecturesareomittedinthesectionandmovedinAppendixB,whereas
thediffusionmodelsforshort-termtimeseriesforecastingaredescribedinthefollowing
subsection.
3.6.4. DiffusionModelsinShort-TermTimeSeriesForecasting
Inrecentyears,severaldiffusion-basedapproachesfortimeseriesforecastinghave
been proposed. They are based on the three predominant methods of diffusion model
describedinAppendixB.Thefirstprominentdiffusionmodelarchitecturefortimeseries
forecastingisTimeGrad[177],whichisaDDPMvariant. TheforwardprocessofTimeGrad
injectsnoisesintodataateachpredictivesample,andthendenoisesgraduallythroughthe
backwardprocessconditionedonprevioustimeseriessamples. Forencodingtheprevious
timeseriessamples,TimeGradusesanRNNarchitecture,e.g.,LSTM(seeSection3.2.4)or
GRU(seeSection3.2.5),TheobjectivefunctionofTimeGradisrepresentedbyanegative
log-likelihood,denotedas:
T
∑ −logp θ (x t 0|h t−1 ), (24)
t=t0
where[t ,T]isthepredictionlength. TheEquation(24)canbereformulatedconsideringthe
0
lowerbound:
E k,x0,(cid:101) [δ(k)||(cid:101) − (cid:101) θ ( (cid:112) a˜ k x t 0 + (cid:112) 1−a˜ k (cid:101),h t−1 ,k)||2]. (25)
t
Theparametersθareestimatedduringthetraining,minimisingthenegativelog-likelihood
objectivefunctionwithastochasticsampling. Furthermore,futuretimeseriessamplesare
generatedwithastep-by-stepprocedure. Theobservationforthenextsamplesattime
T+1ispredictedinasimilarwayasDDPM(seeAppendixB).Similarly,theScoreGrad
model [178], based on the same target distribution of TimeGrad, defines a continuous
diffusionprocessusingSDEs(seeAppendixB).ScoreGradconsistsoftwomodules: the
former is a feature extraction module (e.g., an RNN) almost identical to TimeGrad, or an
attention-basednetwork,e.g.,Transformer(seeSection4.1),forcomputingthehiddenstate

Information2023,14,598 16of35
h
t ofprevioustimesamples,thelatterisaconditionalSDE-basedscore-matchingmodule.
TheobjectivefunctionofScoreGradiscomputedasfollows:
T
∑
|     |     |     |     |     | L (θ), |     |     |     | (26) |
| --- | --- | --- | --- | --- | ------ | --- | --- | --- | ---- |
t
t=t0
withL t (θ)being:
|     | E       | [δ(k)||s | (xk,h | ,k) | − ∇ | logq  | (x |x0)||2]. |     | (27) |
| --- | ------- | -------- | ----- | --- | --- | ----- | ------------ | --- | ---- |
|     | k,x0,xk |          | θ     | t t |     | xk ok | t t          |     |      |
|     |         | t t      |       |     |     | t     |              |     |      |
Itisworthwhiletoremarkthat,inEquation(27),thegeneralformulationofSDEshasbeen
usedforthesakeofsimplicity. Recently,timeseriesresearchhaspaidattentiontoavoiding
model overfitting phenomena in the forecasting of short time series. D3VAE [179], tries to
addresstheproblemofshorttimeseries,applyingacoupleddiffusionprocessfortimeseries
dataaugmentation,andthenitperformsabidirectionalautoencoder(BVAE),asascoremodel.
Moreover,D3VAEtakesintoaccountthedecouplingoflatentvariablesbyreducingtotal
correlationtoimprovepredictioninterpretabilityandstability. Furthermore,theobjective
functionofD3VAEincludesthemeansquareerror(MSE),whichhighlightstherequirement
ofsupervision,amongtheforecastandcurrentsamplesinthepredictionwindow. Unlike
TimeGrad,D3VAEinjectsnoisesseparatelyintotheprevioussamples(context)x0 and
1:t0 −1
thepredictionwindowx0
bythecoupleddiffusionprocess:
t0:T
|     |     |      |      | (cid:112)     |         | (cid:112)    |              |     |      |
| --- | --- | ---- | ---- | ------------- | ------- | ------------ | ------------ | --- | ---- |
|     |     | xk   | =    | a˜ x0         | +       | 1−a˜         | (cid:101),   |     | (28) |
|     |     | 1:t0 | −1   | k             | 1:t0 −1 |              | k            |     |      |
|     |     |      |      | (cid:113)     |         | (cid:113)    |              |     |      |
|     |     | xk   | =    | a˜(cid:48) x0 | +       | 1−a˜(cid:48) |              |     |      |
|     |     |      | t0:T | k             | t0:T    |              | k (cid:101), |     | (29) |
where(cid:101)indicatesthestandardGaussiannoise. Shorttimeseriesforecastingbenefitsthe
simultaneousimprovementofthecontextandpredictionwindowprovidedbythediffusion
process. TheB processismadeupoftwosteps. Theformerforecastsxk withaBVAE
t0:T
model,consideringthecontextxk . Thelatterdenoisestheoutputx˜k ofBVAEwitha
|     |     |     | 1:t0 −1 |     |     |     |     | t0:T |     |
| --- | --- | --- | ------- | --- | --- | --- | --- | ---- | --- |
denoisingscorematchingmodule,asfollows:
|     |     | xk   | ← x˜k | −σ2∇ |     | E(x˜k | ;e), |     | (30) |
| --- | --- | ---- | ----- | ---- | --- | ----- | ---- | --- | ---- |
|     |     | t0:T |       | t0:T | 0 k | t0:T  |      |     |      |
x˜ t 0:T
whereE(x˜k ;e)istheenergyfunction. TheobjectivefunctionofD3VAEiscomposedof
t0:T
fourlosses,thatcanbewrittenasfollows:
|     | λ D (q(xk |      | ||p (x˜k | ))   | + λ L | +   | λ L + | L , | (31) |
| --- | --------- | ---- | -------- | ---- | ----- | --- | ----- | --- | ---- |
|     | 1 KL      | t0:T | θ        | t0:T | 2 DSM |     | 3 TC  | MSE |      |
whereλ ,λ ,λ aretheregularisationparametersofdivergencebetweentargetdistributionand
1 2 3
distributionofpredictionwindow,denoisingscorematchingobjective,andtotalcorrelationamong
latentvariables,respectively. Diffusionmodelsfortimeseriesforecastingaresummarisedin
Table11.
Table11.Recentdiffusionmodelsfortimeseriesforecasting.
| Ref.  |     |     |     |     | Year |     |     | Model     |     |
| ----- | --- | --- | --- | --- | ---- | --- | --- | --------- | --- |
| [177] |     |     |     |     | 2021 |     |     | TimeGrad  |     |
| [178] |     |     |     |     | 2021 |     |     | ScoreGrad |     |
| [180] |     |     |     |     | 2022 |     |     | DSPD      |     |
D3VAE
| [179] |     |     |     |     | 2022 |     |     |     |     |
| ----- | --- | --- | --- | --- | ---- | --- | --- | --- | --- |
4. DeepLearningModelsforLong-TermForecasting
Inlong-termforecasting,theskeletonofatimeseriescanbeapproximatedbyusing
theTransfomerarchitecture. Firstly,theoriginalTransformerarchitecture(Section4.1)is

Information2023,14,598 17of35
describedandattentionmechanismsarepresented(Sections4.1.1and4.1.2). Furthermore,
themainlimitationsofTransformersarediscussed(Section4.1.3)andvariantsofTransformer,
properly designed to cope with long-term time series forecasting tasks, e.g., Informer,
Autoformer,FEDFormerandCrossformer,arepresented(Section4.1.4).
4.1. Transformers
TheTransformer[181]isadeep-learningarchitectureborrowedfromNaturalLan-
guageProcessing.Itcanbedescribedas:“amodelarchitectureeschewingrecurrenceandrelying
entirelyonattentionmechanismstodrawglobaldependenciesbetweeninputandoutput”[181].
TheTransformerarchitecturewasproposedtoovercomethemaindrawbacksofrecurrent
models(seeSections3.2.2and3.2.6)withsequencemodellingtasks:
1. Theoutputstateh t ofarecurrentlayerattimetdependsonthestateh t−1 ,produced
attheprevioustimestep. Thisinherentsequentialnatureprohibitstheintra-sequence
parallelismofrecurrentnetworks.
2. Recurrentnetworkscannotgenerallylearnrelationshipsbetweensequencesofdistant
samples,sinceinformationmustfirstpassthroughalldatasamplesinbetween(see
Figure8).
ThestandardTransformerfollowsageneralencoder-decoderarchitectureforsequence-
to-sequencetransduction,asshowninFigure10.
Intimeseriesforecasting,theTransformer’sinputisatime-orderedsequenceofpast
samplesX = [(cid:126)x ,(cid:126)x ,...,(cid:126)x ]whereListhesequencelengthand(cid:126)x ∈Rdisthei-thsampleofa
1 2 L i
d-dimensionalmultivariatetimeseries.Duetotheuseofattentionmechanisms,Transformers
makenoassumptiononanyintrinsictemporalorspatialorderingofinputelements,namely
inputsareseenasasetofsamplesratherthanorderedsequencesofsamples. Ifthereisa
relevantinputorderingforthemodellingtask,e.g.,timeseriesforecasting,theordering
shouldbeencodedintheinputembedding. InTransformers,thisiscommonlyachievedby
summingapositionalembeddingE tothemainsampleembeddingF(X)[181]:
pos
input = F(X)+E (32)
pos
wherethematrix(Differentlyfromwhatappearsinsomemachinelearningpapers,the
moreprecisetensorproductnotationisusedinthewholeworkforrepresentingmatrices)
F(X) ∈RL⊗RD representsaprojectionoftheinputsequenceinahigherD-dimensional
space (D > d). In time series forecasting, a 1D convolutional layer is commonly used
with D learnedkernels, asdescribedinSection3.1, inordertoextracta D-dimensional
representationforeachsampleinX [181–184]. E caneitherbealearnedembeddingor
pos
afixedembedding. Anaivesolution,yeteffective,consistsofusingasinusoidalposition
encoding[181]. However,intimeseriesforecasting,otherpositionalembeddingscanbe
usedaswell,e.g.,temporal-basedembeddings[182–184]. Theencoderandthedecodercan
havetwodifferentseparatedembeddings,ortheycansharethesameembeddingifinput
andoutputsamplesbelongtothesameset. Intimeseriesforecasting,theencoderinputis
thecompletesequenceofpastsamplesX,whilethedecoderinputiscommonlycomposed
ofthemostrecentpartof X (e.g., thesecondhalfof X, i.e., [(cid:126)x L/2 ,(cid:126)x L/2+1 ,...,(cid:126)x L ])anda
zero-vector whose length is equal to prediction length P, see Equation (1). The encoder
anddecoderarecomposedofN andN stackedlayers,respectively(seeFigure10). The
e d
outputofalayeristheinputforthenextlayer. Eachencoderlayerhastwosublayers: a
self-attentionlayer,thatrelateseachinputsamplewiththerestofthesamples,andashallow
feed-forwarddenselayer,sharedalongthesequenceaxis,thatworksasanonlinearprojection
layer.Tofostergradientpropagationandtraining,eachsublayer’sinputisaddedtoitsown
outputwitharesidualconnection[185],andlayernormalization[186]isusedtonormalise
thesamplesoftheresultingsequenceintoanormaldistributionwithalearnedmeanand
standard deviation. Each decoder layer follows the same overall structure of a generic
encoderlayer,butithasoneadditionalsublayer. Thefirstsublayerimplementsaparticular
kindofself-attentionmechanism,theso-calledcausal(ormasked)self-attention[181]. Itworks

Information2023,14,598 18of35
similarlytotheencoderlayer’sself-attention,aseachinputsampleisrelatedtotheothers
inthedecoder’sinputsequence,butitalsousesmaskingtopreventfuturesamplesfrom
being considered when the processing of the current sample occurs. Furthermore, the
outputofthecausalself-attentionsublayerisrelatedtotheencoder’shiddenrepresentation
(thatis,theoutputofthefinalencoderlayer)byacross-attentionlayer. Asinencoderlayers,
aMulti-LayerPerceptron[67]withonehiddenlayerisusedforprojectingnonlinearlythe
outputofcross-attention. Moreover,eachsublayeriswrappedbyaresidualconnection
followedbylayernormalization. Finally,theoutputofthelastdecoderlayerisfedtoafinal
predictionlayer.
Output Probabilities
softmax
Dense Layer
Add & Norm
Feed-Forward
|     | Add & Norm |     | Add & Norm |     |     |     |
| --- | ---------- | --- | ---------- | --- | --- | --- |
N d
Decoder
|     | Feed-Forward |     | Cross-Attention | Layers |     |     |
| --- | ------------ | --- | --------------- | ------ | --- | --- |
N e
K V Q
Encoder
Layers
|     | Add & Norm     |     | Add & Norm |     |     |     |
| --- | -------------- | --- | ---------- | --- | --- | --- |
|     | Self-Attention |     | Causal     |     |     |     |
Self-Attention
|                      | K V              | Q            | K V              | Q                |     |     |
| -------------------- | ---------------- | ------------ | ---------------- | ---------------- | --- | --- |
| Positional           |                  | + Positional | +                |                  |     |     |
| Encoding             |                  | Encoding     |                  |                  |     |     |
|                      | D-dimensional    |              | D-dimensional    |                  |     |     |
|                      | Embedding Module |              | Embedding Module |                  |     |     |
| En c o d e r  In put |                  |              |                  | De c o d e r  In | put |     |
|                      | xi,1 xi,2        | xi,3 xi,L1   | xi,1 xi,2 xi,3   | xi,L2            |     |     |
| S e q u e n ce       |                  |              |                  | S e q u e n      | ce  |     |
Figure 10. Transformer architecture. On the left side, the encoder processes an input sequence,
producingahiddenrepresentation.Ontherightside,thedecoderusestheencoder’soutputtogenerate
theoutputsequence.Thedecoderworksinanautoregressiveway,consumingpastgeneratedsamples
asadditionalinputstogeneratethenextoutputsample.
4.1.1. AttentionMechanisms
ThemostimportantcomputationalblocksofaTransformerareattentionmechanisms,
that allow the model to focus its attention on specific parts of the input, depending on
theinformationbeingprocessed. Amongvariousdefinitionsofattention,Transformers
adopt the so-called scaled dot-product attention, which is very similar to multiplicative at-
tention [187]. Attention mechanisms operate on the following elements: a set of queries
∈RM⊗RDk
Q thatrepresentstheinformationbeingprocessedbythemodel,andsetsof
keysK ∈RN⊗RDk andvaluesV ∈RN⊗RDv,whereDk andDv denotethedimensionof
spacewherequeries,keysandvaluesareprojected. Moreover,Ndenotesthecardinalityof
bothkeysandvalues,while Misthecardinalityoftheinputqueries. TheoutputYforall
queriesiscomputedasfollows:
(cid:32) (cid:33)
QK(cid:62)
|     |     | Y =Attention(K,V,Q) |     | =softmax | √ V | (33) |
| --- | --- | ------------------- | --- | -------- | --- | ---- |
D k
∈RM⊗RDv
TheattentionoutputY isamatrixwhosei-throwcontainstheoutputvector
forthei-thquery. NotethatthesoftmaxinEquation(33)isappliedrow-wisetoitsinput
matrix.Wheredothesequeries,keysandvaluescomefrom?Firstofall,keysandvaluesareoften
thesamevectors,i.e.,avaluevectorcoincideswithitskey. Furthermore,asdescribedin
Section4.1,theTransformerperformsattentionintwoways,self-attentionandcross-attention.

Information2023,14,598 19of35
Inself-attention,queriesandvaluesarethesamevectors;incross-attentionqueriescome
fromthepreviousdecodersublayer,whilekeyandvaluevectorsaregivenbytheencoder’s
hiddenrepresentation.
4.1.2. Multi-HeadAttention
Multi-HeadAttention(MHA)isamoreadvancedversionoftheaforementionedscaled
dot-productattention. Asdiscussedin[181],thescaleddot-productattentionpermitsa
networktoattendoverasequence. However,oftentherearemultipledifferentaspectsa
sequenceelementwantstoattendto,andasingleweightedaverageisnotanadequate
optionforit. Thismotivatestheextensionofthescaleddot-productattentiontoMHA,
whichallowsthemodeltojointlyattendtoinformationfromdiverserepresentationsub-
spaces,asshowninFigure11.
|     |                                  | Y      |     |     |               | Y       |           |     |
| --- | -------------------------------- | ------ | --- | --- | ------------- | ------- | --------- | --- |
|     |                                  | MatMul |     |     |               | Project |           |     |
|     | Softmax                          |        |     |     | Concatenation |         |           |     |
|     | Masking                          |        |     |     |               |         | H         |     |
|     | (only for causal self-attention) |        |     |     |               |         | Attention |     |
Scaled Dot-Product Attention
Heads
Scaling
|     |     |     |     |     | Project | Project Project |     |     |
| --- | --- | --- | --- | --- | ------- | --------------- | --- | --- |
MatMul
|     | Q   | K   | V   |     | Q   | K   | V   |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
(a)Scaleddot-productattention. (b)Multi-HeadAttentionwithHheads.
Figure11.Comparisonofasinglescaleddot-productattention(a)andmulti-headattentionwithH
attentionheads(b).
InMHA,keys,valuesandqueriesarelinearlyprojected H separatetimes,bythree
learnedprojectionmatrices,ontospacesofdimensions D k , D v and D k respectively. Fur-
thermore, ascaleddot-productattentionisappliedtoeachoftheseprojectionsandthe
results are concatenated together and re-projected onto the previous layer space. Each
projection-attention pair defines a so-called attention head h. For the sake of simplicity,
i
keys,valuesandqueriesareassumedtohavethesamedimensionD. Eachattentionhead
|         |               |           | K   | ∈ RD⊗RDk, | V   | ∈ RD⊗RDv | Q ∈ RD⊗RDk, |     |
| ------- | ------------- | --------- | --- | --------- | --- | -------- | ----------- | --- |
| h i has | three learned | matrices: | W   |           | W   |          | andW        |     |
|         |               |           | i   |           | i   |          | i           |     |
usedtoprojectkeys,valuesandqueries,respectively. Eachattentionheadappliesascaled
dot-productattention(seeEquation(33))totheprojectedkeys, valuesandqueries(see
Section4.1.1):
|     |     |     | =Attention(KWK,VWV,QW |     |     | Q) ∀i ∈ [1,H] |     |      |
| --- | --- | --- | --------------------- | --- | --- | ------------- | --- | ---- |
|     |     | h   | i                     |     |     |               |     | (34) |
|     |     |     |                       | i   | i   | i             |     |      |
Finally,theattentionoutputYisgivenby:
)Wo
|     |     | Y =MHA(K,V,Q) |     | =Concatenate(h |     | ,h ,...,h |     | (35) |
| --- | --- | ------------- | --- | -------------- | --- | --------- | --- | ---- |
|     |     |               |     |                |     | 1 2       | H   |      |
RM⊗RHDv
wheretheoutputsh i fromallattentionheadsareconcatenatedintoasingle
matrixandthenre-projectedlinearlytotheoriginalD-dimensionalspaceviaanadditional
| projectionmatrixWo |     | ∈RHDv | ⊗RD. |     |     |     |     |     |
| ------------------ | --- | ----- | ---- | --- | --- | --- | --- | --- |
4.1.3. ShortcomingsofTransformers
TherearethreemainshortcomingsofTransformers. Firstly,Transformersarelocally-
agnostic,thatis,thescaleddot-productoftheattentionmechanism(seeEquation(33))is
insensitive to the local context, which can make the model prone to anomalies in time

Information2023,14,598 20of35
seriesforecasting[188]. Furthermore,Transformerssufferofmemorybottleneck,i.e.,Trans-
formers’spacecomplexityisO(L2)withsequencelengthL[188]. Similarly,Transformers
alsohavethesametimecomplexity,limitingtheirapplicationtothelong-termforecast-
ing. TheseshortcomingsarefacedbysomeoftheTransformervariantsdescribedinthe
followingsection.
4.1.4. TransformerVariantsforTimeSeriesForecasting
Inrecentyears,manyvariantsofthenaiveTransformer[181],specificfortimeseries
forecasting,havebeenproposed. Keyinnovationsthatthesevariantssuggestconcernthe
embeddinglayer,attentionmechanismsandeventheencoder-decoderstructure. Most
oftheliteraturefocusedonthedesignofalternativeattentionmechanismsthataremore
suitablefortimeseriesforecastingtasks. OneofthefirstsuchworksistheLogTrans[188],
whichhandlestwolimitationsofthetraditionalTransformer: locally-agnosticandmemory
bottleneck(seeSection4.1.3). Theformerlimitationistackledusingcausalconvolutions
(see Section 3.1.2) to generate keys and queries in the self-attention module. For the
latter,alog-sparsemaskisconsideredinordertoreducethecomputationalcomplexity(see
Section4.1.3)ofmulti-headattention. InspiredbytheideaofLogTrans,anothervariant,the
Informer[182],definesanewsparsemeasuretocharacteriseasubsetofthemostinformative
queriesbeforeapplyingattention. Inaddition,thisstrategyalsoallowsforthereductionof
thecomputationalcomplexityofattentionmechanisms. UnlikeLogTransandInformer,the
Autoformer[183]replacesthestandardscaleddot-productattentionwithanautocorrelation
mechanism. Additionally,adecompositionmoduleisemployedtobreakdownthetimeseries
intotrendandseasonalcomponents,assumingimplicitlythattheyexistandareadditive.
Theautocorrelationmechanismmeasuresthetime-delaysimilaritybetweeninputsignals
andaggregatesthetop-ksimilarsub-seriestoproducetheoutput. TheFEDformer[184],
basedontheworkofLinformer[189],appliesattentiontoalow-rankapproximationofthe
inputbasedontheRestrictedIsometryProperty(RIP)matrixtheory[190]. First,itrepresents
the input signal into a frequency domain (either Fourier or Wavelet). Furthermore, it
achievesalinearcomplexitybyapplyingsimplifiedattentionmechanismsonarandomly
selectedsubsetoffrequencieswithafixedsizem. Recently,researcheffortshavemoved
fromattentionmechanismstoinputrepresentation, specificallyconcerninghowtorelate
thedimensionsofamultivariatetimeseriesandhowtoprojecttheinputsequenceintoa
latentrepresentation. ThepatchTST[191]assumeschannelindependence,i.e.,independence
amongthe dimensionofthe inputmultivariatetime series, processingeachdimension
as a univariate time series. PatchTST segments each input sequence into shorter, local
sub-sequences that are fed as input samples to a naive Transformer encoder [181]. All
time series dimensions are implicitly related via the sharing of the encoder weights. A
similarconsiderationisadoptedbytheCrossformer[192],whichsegmentseachdimension
of the input time series into non-overlapping shorter sub-sequences. Unlike patchTST,
however,theCrossformerexplicitlydefinestherelationsamongalldimensionsusinga
Two-StageAttention(TSA)mechanism. Furthermore, CrossformerfollowsaHierarchical
Encoder-Decoderarchitecture,inwhichmultiplelayersofTSAareusedtocapturerelations
atmultipletimescales. AnotherrelevantworkisthePyraformer[193],whichproposesa
PyramidalAttentionModule(PAM)tocapturelong-termdependencieswhileachievinga
complexitythatislinearinthesequencelength. Essentially,PAMconsistsofapplyingthe
classicscaleddot-productattentioninasparsefashionaccordingtoapyramidalgraph,
built using a cascade of strided convolutions, that defines a multi-scale representation
of the input sequence. According to PAM, each node of the graph is a query and it
can attend only those nodes (keys) that are its direct neighbours in the graph. In this
way, Pyraformer is able to capture both short-term and long-term dependencies while
still achieving a linear complexity. Similarly to Pyraformer, Scaleformer [194] addresses
the importance of multi-scale dependencies in time series forecasting. The approach is
orthogonaltomanytimeseriesTransformersand,assuch,ithasbeenempiricallyevaluated
withsomeoftheaforementionedmodelsliketheAutoformer[183]andtheFEDformer[184].

Information2023,14,598 21of35
Givenaninputpastsequenceandthecorrespondingtargetsequence,themainideaisto
applyoneoftheabove-mentionedTransformermodels,multipletimesatmultipletime
scales. Atagivenscales,theinputtotheencoderistheoriginallook-backwindowbut i
downsampledbyafactors usingaveragepooling;theinputtothedecoderisgivenbythe
i
modelforecastatthepreviousscales i−1 ,butupsampledbyafixedfactorsthroughlinear
interpolation. Tomitigateerrorpropagationanddistributionshiftsthatareduetorepeated
upsamplingoperations,theencoderanddecoder’sinputsarefirstnormalisedusingCross-
ScaleNormalization. Finally,alossfunction,basedonanadaptiveloss,isappliedateach
timescalebetweenthemodelforecastandthetargetsequence,whichisalsodownsampled
byafactors viaaveragepooling. TheTriformer[195]proposesaparticulararchitecturethat
i
integratesattentionmechanismsandrecurrentunitstoensurehighefficiencyandaccuracy.
Theformerisachievedbyapatchattentionmechanismwithlinearcomplexity;thelatteris
obtainedbyusingvariable-specificparameters.Thepatchattentionmechanismsplitstheinput
sequenceinPpatchesoflengthSandassignsalearnablepseudo-timestampT toeachpatch.
p
Whenpatchattentionisapplied,eachpseudo-timestampT p isconsideredasaqueryQforits
patchonly. Moreover,variable-specificparametersareintroducedbyfactorisingtheprojection
| matrices(i.e,WK | andWV)intothreematrices: |                             |     | ∈ RD⊗Ra, |
| --------------- | ------------------------ | --------------------------- | --- | -------- |
|                 |                          | leftvariable-agnosticmatrix |     | L        |
middlevariable-specificmatrixB ∈Ra⊗Ra andrightvariable-agnosticmatrixR ∈Ra⊗RD,
(cid:28)
where a D. Finally, to cope with the limited temporal receptive field that is due to
thepatchmechanism,recurrentunitsareusedtoaggregateandcontroltheinformation
forallpseudo-timestampsofeachlayerbeforethefinalprediction. Allabove-mentioned
variantsofTransformersharetheover-stationarizationproblemthatconsistsintheinability
togeneratedistinguishableattentionscoreswhentrainedonstationarizedseries[196]. The
Non-stationaryTransformer[196]proposesagenericframeworktoovercometheproblemof
over-stationarization. Thisframeworkiscomposedoftwointerdependentmodules: Series
StationarizationandDe-stationaryAttention. Theformerattenuatesthenon-stationarityof
thetimeseriesconsidered,usingtwosequentialoperations: Normalizationmodule,which
computesthemeanandthevarianceforeachinputtimeseriesinordertotransformit
into a stationary time series, and a De-normalization module, which transforms the model
outputsbackintoanon-stationarytimeseries,usingthemeanandvariancecomputedin
thepreviousmodule. Thelatterisanovelattentionmechanism,whichcanapproximate
theattentionscoresthatareobtainedwithoutstationarizationanddiscovertheparticular
temporaldependenciesfromoriginalnon-stationarydata. Transformervariantsfortime
seriesforecastingaredescribedindetailinTable12. FurtherdetailsoneachTransformer
variant,canbefoundintheoriginalpaperthatpresentsthearchitecture.
Table12.RecentvariantsofTransformerarchitecturefortimeseriesforecasting.
|     | Ref.  | Year | Model                     |     |
| --- | ----- | ---- | ------------------------- | --- |
|     | [188] | 2019 | LogTrans                  |     |
|     | [182] | 2021 | Informer                  |     |
|     | [183] | 2021 | Autoformer                |     |
|     | [184] | 2022 | FEDFormer                 |     |
|     | [193] | 2022 | Pyraformer                |     |
|     | [195] | 2022 | Triformer                 |     |
|     | [196] | 2022 | Non-stationaryTransfomers |     |
|     | [191] | 2023 | PatchTST                  |     |
|     | [192] | 2023 | Crossformer               |     |
|     | [194] | 2023 | Scaleformer               |     |
Table 13 reports an extensive comparison among all aforementioned Transformer
variants. Ithastobenotedthat,thereportedresultswerecollectedfromtheoriginalpapers
thattestedagivenmodelonagivendataset(thereadercanrefertotheGitHubpages
linkedintheoriginalpapersofeacharchitectureforreproducingtheexperiments,using
theoriginalexperimentalsetups).

Information2023,14,598 22of35
Table13.Multivariatelong-termforecastingbenchmarksamongvariantofTransformerarchitectureswithdifferentpredictionlengthsP∈[96,192,336,720].The
inputlengthconsideredforILIdatasetis36and96fortheothers. AlowerMSEorMAEindicatesabetterprediction. Thebestresults,foreachdatasets,are
highlightedinbold.
Models Crossformer PatchTST Non-Stationary Pyraformer FEDFormer Autoformer Informer LogTrans LSTM TCN
Metric MSE MAE MSE MAE MSE MAE MSE MAE MSE MAE MSE MAE MSE MAE MSE MAE MSE MAE MSE MAE
rehtaeW
96 - - 0.149 0.198 0.173 0.223 0.354 0.392 0.217 0.296 0.266 0.336 0.300 0.384 0.458 0.490 0.369 0.406 0.615 0.589
192 - - 0.194 0.241 0.245 0.285 0.673 0.597 0.276 0.336 0.307 0.367 0.598 0.544 0.658 0.589 0.416 0.435 0.629 0.600
336 0.495 0.515 0.245 0.282 0.321 0.338 0.634 0.592 0.339 0.380 0.359 0.395 0.578 0.523 0.797 0.652 0.455 0.454 0.639 0.608
720 0.526 0.542 0.314 0.334 0.414 0.410 0.942 0.723 0.403 0.482 0.419 0.428 1.059 0.741 0.869 0.675 0.535 0.520 0.639 0.610
cfifarT
96 - - 0.360 0.249 0.612 0.338 0.684 0.393 0.562 0.349 0.613 0.388 0.719 0.391 0.684 0.384 0.843 0.453 1.438 0.784
192 - - 0.379 0.256 0.613 0.340 0.692 0.394 0.562 0.346 0.616 0.382 0.696 0.379 0.685 0.390 0.847 0.453 1.463 0.794
336 0.530 0.300 0.392 0.264 0.618 0.328 0.699 0.396 0.570 0.323 0.622 0.337 0.777 0.420 0.733 0.408 0.853 0.455 1.479 0.799
720 0.573 0.313 0.432 0.286 0.653 0.355 0.712 0.404 0.596 0.368 0.660 0.408 0.864 0.472 0.717 0.396 0.500 0.805 1.499 0.804
yticirtcelE 96 - - 0.129 0.222 0.169 0.273 0.498 0.299 0.183 0.297 0.201 0.317 0.274 0.368 0.258 0.357 0.375 0.437 0.985 0.813
192 - - 0.147 0.240 0.182 0.286 0.828 0.312 0.195 0.308 0.222 0.334 0.296 0.386 0.266 0.368 0.442 0.473 0.996 0.821
336 0.323 0.369 0.163 0.159 0.200 0.304 1.476 0.326 0.212 0.313 0.231 0.338 0.300 0.394 0.280 0.380 0.439 0.473 1.000 0.824
720 0.404 0.423 0.197 0.290 0.222 0.321 4.090 0.372 0.231 0.343 0.254 0.361 0.373 0.439 0.283 0.376 0.980 0.814 1.438 0.784
ILI
24 3.041 1.186 1.319 0.754 2.294 0.945 5.800 1.693 2.203 0.963 3.483 1.287 5.764 1.677 4.480 1.444 5.914 1.734 6.624 1.830
36 3.406 1.232 1.579 0.870 1.825 0.848 6.043 1.733 2.272 0.976 3.103 1.148 4.755 1.467 4.799 1.467 6.631 1.845 6.858 1.879
48 3.459 1.221 1.553 0.815 2.010 0.900 6.213 1.763 2.209 0.981 2.669 1.085 4.763 1.469 4.800 1.468 6.736 1.857 6.968 1.892
60 3.640 1.305 1.470 0.788 2.178 0.963 6.531 1.814 2.545 1.061 2.770 1.125 5.264 1.564 5.278 1.560 6.870 1.879 7.127 1.918
2mTTE
96 - - 0.166 0.256 0.192 0.274 0.409 0.488 0.203 0.287 0.255 0.339 0.365 0.453 0.768 0.642 2.041 1.073 3.041 1.330
192 - - 0.223 0.296 0.280 0.339 0.673 0.641 0.269 0.328 0.281 0.340 0.533 0.563 0.989 0.757 2.249 1.112 3.072 1.339
336 - - 0.274 0.329 0.334 0.361 1.210 0.846 0.325 0.366 0.339 0.372 1.363 0.887 1.334 0.872 2.568 1.238 3.105 1.348
720 - - 0.362 0.385 0.417 0.413 4.044 1.526 0.421 0.415 0.422 0.419 3.379 1.388 3.048 1.328 2.720 1.287 3.153 1.354

Information2023,14,598 23of35
5. OtherRelevantDeepLearningModels
This section is reserved for those works that propose interesting architectures for
short-termandlong-termtimeseriesforecastingwhichdonotfitthepreviouslydefined
categories. Eventhoughthesemodelsmightsharethesamebuildingblocksofwell-known
architectures(e.g., CNN,TCN,RNN,Transformer), duetotheirpeculiarityandhetero-
geneityithasbeendecidedtocollectthemunderapropersection. In[197]aContinuous
RecurrentUnit(CRU)basedonstochasticdifferentialequations(SDEs)andKalmanfilters,
thatcanhandleirregularlysampledtimeseries,isproposed. TheFiLM(Frequency-improved
LegendreMemory)model[198]generatesarepresentationofpasttimeseriessamplesby
Legendreprojections. ItusesanoisereductionmodulebasedonFourieranalysistopreserve
onlyrelevantinformationfromprevioustimesamples,reducingtheeffectthatnoisysignals
canhaveontimeseriesforecasting. In[199],itshowshowatimeseriesforecastingmodel
fullybasedonMLPcancomparecompetitivelywithstate-of-the-artTransformermodels
(e.g.,PatchTST[191]),reducing,inthisway,theforecastingcomputationalcost. Indetail,it
proposesanadaption(TSMixer)ofMLP-Mixer,originallyproposedforthevisiondomain,
fortimeseriesforecasting. Aconvolution-basedarchitecture,MICN(Multi-scaleIsometric
ConvolutionNetwork)[200],candiscoverlocalpatternsandglobalcorrelationsintimeseries
byusingamulti-branchstructureandrelyingondownsampled1Dconvolutionstoextractlocal
featuresandisometricconvolutions,aparticularcaseofcausalconvolution(seeSection3.1.2),
todiscoverglobalcorrelations. Table14summarisestheaforementionedmodels.
Table14.Recentapplicationsontimeseriesforecastingusingotherdeeplearningarchitectures.
| Ref.      | Year |                                           | Application |     |
| --------- | ---- | ----------------------------------------- | ----------- | --- |
| [197]     | 2022 | Climatedata/ElectronicHealthRecords       |             |     |
| [198]     | 2022 | Long-termbenchmarkdatasets(seeSection6.2) |             |     |
| [199,200] | 2023 | Long-termbenchmarkdatasets(seeSection6.2) |             |     |
6. BenchmarksforTimeSeriesForecasting
Recently,agroupoftimeserieshaveemergedasbenchmarksforassessingtheperfor-
manceofmachinelearningmodelsintimeseriesforecastingtasks. Thissectiondescribes
themostrelevantbenchmarksforbothshortandlong-termforecasting.
6.1. BenchmarksforShort-TermForecasting
Amongseveraldifferentdatasetsusedforshort-termforecasting,themostpopular
onesaredescribedinTable15. ItisworthquotingtheM4dataset[44],proposedin2020for
thehomonymousM4competitionasacommonbenchmarkforevaluatingtheperformance
ofshort-termforecastingmodels. TheM4datasetcontains100.000timeseriessubdivided
accordingtotheirdatafrequencyintosixgroups: M4-Yearly,M4-Quarterly,M4-Monthly,
M4-Weekly,M4-DailyandM4-Hourly. Furthermore,timeseriesarealsocategorisedintosix
domains,namely,Demographic,Finance,Industry,Macro,MicroandOther. Someinsightson
howtimeseriesaredistributedintothesecategoriesaregiveninFigure12.
Table15.Short-termforecastingdatasets.ThecolumnDimreferstothedimensionalityoftimeseries.
| Dataset          |     | Dim | DataType(Real/Synthetic) |      |
| ---------------- | --- | --- | ------------------------ | ---- |
| M4-Yearly[44]    |     | 1   |                          | Real |
| M4-Quarterly[44] |     | 1   |                          | Real |
| M4-Monthly[44]   |     | 1   |                          | Real |
1
| M4-Weekly[44]     |     |     |     | Real      |
| ----------------- | --- | --- | --- | --------- |
| M4-Daily[44]      |     | 1   |     | Real      |
| M4-Hourly[44]     |     | 1   |     | Real      |
| Mackey-Glass[201] |     | 1   |     | Synthetic |
| DatasetA[202]     |     | 1   |     | Real      |
| DSVC1[203]        |     | 1   |     | Real      |
| Paris-14E[204]    |     | 1   |     | Real      |
| DatasetD[205]     |     | 1   |     | Synthetic |

Information2023,14,598 24of35
|     | M4-Monthly	data	set                         |     |     |     | M4-Yearly	data	set |                          |
| --- | ------------------------------------------- | --- | --- | --- | ------------------ | ------------------------ |
|     | Other:	277	-	0.6% Demographic:	5728	-	11.9% |     |     |     | Other:	1236	-	5.4% | Demographic:	1088	-	4.7% |
Micro:	10975	-	22.9%
Finance:	6519	-	28.3%
Micro:	6538	-	28.4%
Finance:	10987	-	22.9%
Macro:	10016	-	20.9%
|     | Industry:	10017	-	20.9% |     |     | Macro:	3903	-	17.0% |     | Industry:	3716	-	16.2% |
| --- | ----------------------- | --- | --- | ------------------- | --- | ---------------------- |
Demographic Finance Industry Macro Micro Other Demographic Finance Industry Macro Micro Other
|     |     | meta-chart.com |     |     |     | meta-chart.com |
| --- | --- | -------------- | --- | --- | --- | -------------- |
(a)M4-Monthlydatasetcomposition. (b)M4-Yearlydatasetcomposition.
Total	M4	competition	data	sets
M4-Hourly:	414	-	0.4%
M4-Daily:	4227	-	4.2%
|     |     | M4-Weekly:	359	-	0.4% | M4-Yearly:	23000	-	23.0% |     |     |     |
| --- | --- | --------------------- | ------------------------ | --- | --- | --- |
M4-Monthly:	48000	-	48.0%
M4-Quarterly:	24000	-	24.0%
|     |     | M4-Yearly | M4-Quarterly M4-Monthly M4-Weekly | M4-Daily |     |     |
| --- | --- | --------- | --------------------------------- | -------- | --- | --- |
M4-Hourly
meta-chart.com
(c)M4-Competitiondatasetcomposition.
Figure12.CompositionoftheM4dataset.(a,b)show,respectively,thedistributionofM4-Monthly
andM4-YearlytimeseriesintothesixM4categories.(c)showsthenumberoftimeseriesineachof
theM4datasets.
6.2. BenchmarksforLong-TermForecasting
Nowadays,agroupofspecificdatasetshasbecomethede-factobenchmark[183]to
assesslong-termforecastingaccuracyofallTransformervariantspresentedinSection4.1.4.
Indetail,thisbenchmarkiscomposedofninemultivariatetimeseriesdatasetsconcerning
the following domains: electricity, transportation, weather, exchange rate and illness (see
Table16). Timeresolutioncanvaryfrom10minupto7days.
Table 16. Long-term forecasting benchmark data sets. The data set size (·,·,·) refers to the car-
dinality of training, validation and test set, respectively. The columns dim, pred len and time res
refer to the dimensionality of time series, the number of predicted future samples and the time
resolution,respectively.
| Dataset | Dim PredLen |     | DatasetSize |     | TimeRes | Domain |
| ------- | ----------- | --- | ----------- | --- | ------- | ------ |
ETTm1 7 [96,192,336,720] (34,465,11,521,11,521) 15mins Electricity
ETTm2 7 [96,192,336,720] (34,465,11,521,11,521) 15mins Electricity
| ETTh1 | 7 [96,192,336,720] |     | (8545,2881,2881) |     | 15mins | Electricity |
| ----- | ------------------ | --- | ---------------- | --- | ------ | ----------- |
| ETTh2 | 7 [96,192,336,720] |     | (8545,2881,2881) |     | 15mins | Electricity |
Electricity 321 [96,192,336,720] (18,317,2633,5261) 1h Electricity
| Traffic | 862 [96,192,336,720] |     | (12,185,1757,3509) |     | 1h  | Transport |
| ------- | -------------------- | --- | ------------------ | --- | --- | --------- |
Weather 21 [96,192,336,720] (36,792,5271,10,540) 10mins Weather
| Exchange | 8 [96,192,336,720] |     | (5120,665,1422) |     | 1day  | Finance |
| -------- | ------------------ | --- | --------------- | --- | ----- | ------- |
| ILI      | 7 [24,36,48,60]    |     | (617,74,170)    |     | 1week | Illness |
7. Conclusions
Thepaperhasrevieweddeeplearningarchitecturesfortimeseriesforecasting,un-
derliningtheiradvances. Nevertheless,fourmajorproblemsremainopen. Thefirstone
residesintheinabilityofmostdeeplearningmethods,withtheexceptionofDeepGaussian
Processes,toestimateaconfidenceintervalforthetimeseriesprediction. Inprinciple,all
deeplearningarchitecturesquotedinthesurveycanbeproperlymodifiedusingBayesian
trainingstrategies[206]inordertoprovidetheuncertaintyofthemodelprediction,but,to
thebestofourknowledge,ithasnotbeenperformedyet. Thesecondproblemresidesin

Information2023,14,598 25of35
thedevelopmentofmoreandmorecomplexdeeplearningarchitectures. Thismakesthem
subjecttooverfitting,aproblemthatcanhardlybefacedbydeeplearningarchitectures.
Therefore,thedevelopmentofdeeplearningarchitecturesfortimeseriesforecastingthat
arerobustw.r.t.overfittingisbecomingmoreandmorerelevant.Thethirdproblemconsists
intheneedforadequatelylongtimeseries. Inparticular,somedeeplearningarchitectures,
e.g.,Transformers,requiretheestimationofmillionsofparameters,implying,inthisway,
thenecessityofadequatelylongtimeseriesforestimatingthem. Theproblemseemsto
be partially addressed by data augmentation but the proposed solutions are not fully
adequate, yet. Finally, thelastproblememergesinmostoftherevieweddeeplearning
models. Theyassumethedynamicalstationarityoftimeseries,implyingthatthedynamic
systemgeneratingtimeseriesisstationaryovertime. Whentheaforementionedassump-
tionisviolated,aconceptdriftphenomenon[207]intimeseriesisobserved,consequently
leadingtoadramaticdecreaseinthepredictionaccuracyofdeeplearningmodelsfortime
seriesforecasting.
AuthorContributions:Conceptualization,A.C.,V.C.andF.C.;methodology,A.C.andV.C.;valida-
tion,A.C.,V.C.andF.C.;formalanalysis,F.C.;investigation,A.C.,V.C.andG.I.;resources,A.C.,V.C.,
G.I.andF.C.;writing—originaldraftpreparation,A.C.,V.C.andF.C.;writing—reviewandediting,
A.C.,V.C.andF.C.;visualization,A.C.,V.C.andF.C.;supervision,F.C.;projectadministration,F.C.
Allauthorshavereadandagreedtothepublishedversionofthemanuscript.
Funding:Thisresearchreceivednoexternalfunding.
DataAvailabilityStatement:Nonewdatawerecreatedoranalyzedinthisstudy.Datasharingis
notapplicabletothisarticle.
Acknowledgments:Wewouldliketothanktheanonymousreviewersfortheusefulcomments.
ConflictsofInterest:Theauthorsdeclarenoconflictofinterest.
AppendixA.TableofMathematicalExpressions
InAppendixA,thetableofthemostfrequentmathematicalexpressionsandoperations
isprovided. TableA1providesadescriptionforeachmathematicaloperation.
TableA1.Tableofthemostcommonlyusedmathematicaloperationswiththeirrespectivedescription.
Symbol Definition
Y =w∗X ConvolutionbetweenakernelwandasequenceX.TheresultisanewsequenceY.
Element-wiseproductbetweentwovectors(cid:126)uand(cid:126)v.Theresultisavector(cid:126)ysuch
(cid:126)y=(cid:126)u(cid:12)(cid:126)v
thaty =uv.
i i i
V⊗W TensorproductbetweentwovectorsVandW,theresultisamatrix.
I TheIdentitymatrix.
AppendixB.DiffusionModels
Inthissection,themostrelevantdiffusionmodels,i.e.,DDPMs(AppendixB.1),SGMs
(AppendixB.2)andSDEs(AppendixB.3),andfoundations,aredescribed.
AppendixB.1. DenoisingDiffusionProbabilisticModels
DenoisingDiffusionProbabilisticModels,originallyproposedin[173]andlaterextended
in[174],considertwoMarkovchainsforforwardandbackwardprocess,respectively,to
approximatethegenerativeprocessofobserveddata.Indetail,lettheoriginalnoiselessdata
bex0. TheforwardMarkovchainprojectsx0intoasequenceofnoiseddatax1,x2,...,xK
withadiffusiontransitionkernel:
√
q(xk|xk−1) = N( a xk−1,(1−a )I), (A1)
k k

Information2023,14,598 26of35
whereKisthefinitenumberofnoiselevelofforwardprocess,a ∈ (0,1)fork =1,2,...,K
k
arehyperparametersindicatingthevarianceofthenoiselevelateachstep,N(·,·)isthe
Gaussiandistribution,and I istheidentitymatrix. TheGaussiantransitionkernelq(·|·)
hasafundamentalpropertythatallowsobtainingxk directlyfromoriginalsamplex0:
(cid:112)
|     |     |     | q(xk|x0) |     | = N( | a˜ x0,(1−a˜)I), |     |     |     |     | (A2) |
| --- | --- | --- | -------- | --- | ---- | --------------- | --- | --- | --- | --- | ---- |
|     |     |     |          |     |      | k               | k   |     |     |     |      |
∏k
where a˜ = a. In DDPM, the reverse transition kernel p (·|·) is designed by a deep
|     | k i=1 | i   |     |     |     |     |     | θ   |     |     |     |
| --- | ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
neuralnetwork:
|     |     |     | (xk−1|xk) |     |       | (xk,k),Σ | (xk,k)), |     |     |     |      |
| --- | --- | --- | --------- | --- | ----- | -------- | -------- | --- | --- | --- | ---- |
|     |     |     | p         |     | = N(µ |          |          |     |     |     | (A3) |
|     |     |     | θ         |     |       | θ        | θ        |     |     |     |      |
whereθindicateslearnableparametersofdeepneuralnetworks. Inordertocomputethe
parametersθsuchthatsamplesestimatedby p (x0)arealmostidenticaltoobserveddata
θ
x0,amaximumlikelihoodestimationmethodisperformed,minimisingthevariationallower
| boundoftheestimatednegativelog-likelihood |     |     |     |     |     | E[−logp |     | (x0)]: |     |     |     |
| ----------------------------------------- | --- | --- | --- | --- | --- | ------- | --- | ------ | --- | --- | --- |
θ
|     |         |     |          |         | (cid:34)  |     |     |             |     | (cid:35) |      |
| --- | ------- | --- | -------- | ------- | --------- | --- | --- | ----------- | --- | -------- | ---- |
|     |         |     |          |         |           |     | K   | p (xk−1|xk) |     |          |      |
|     | E[−logp |     | (x0)] =E |         | −logp(xK) |     | − ∑ | θ           |     |          |      |
|     |         | θ   |          | q(x0:K) |           |     |     | log         |     | ,        | (A4) |
q(xk|xk−1)
k=1
where x0:K indicates the sequence x0,...,xK. A simpler objective function [174] can be
provided,asfollows:
|     |     |     |                  |     | (cid:112)      |      | (cid:112) |                   |     |     |      |
| --- | --- | --- | ---------------- | --- | -------------- | ---- | --------- | ----------------- | --- | --- | ---- |
|     |     | E   | [δ(k)||(cid:101) | −   | (cid:101) ( a˜ | x0 + | 1−a˜      | (cid:101),k)||2], |     |     | (A5) |
|     |     |     | k,x0,(cid:101)   |     | θ              | k    |           | k                 |     |     |      |
σ2I
assumingthecovariancematrixequaltoΣ (xk,k) = ,whereσ2controlsthenoiselevel
|     |     |     |     |     | θ   |     | k   | k   |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
)2
| andmayvaryatdifferentreversesteps,andδ(k) |     |     |     |     |     | =   | (1−ak | .   |     |     |     |
| ----------------------------------------- | --- | --- | --- | --- | --- | --- | ----- | --- | --- | --- | --- |
2ak
|     |     |     |     |     |     |     | 2σ (1−a˜k | )   |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --------- | --- | --- | --- | --- |
k
| AppendixB.2. | Score-BasedGenerativeModels |     |     |     |     |     |     |     |     |     |     |
| ------------ | --------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Score-basedgenerativemodels(SGMs)[175],aremadeupoftwomodules. Theformeris
thescorematchingmodule[208],forestimatingtheunknowntargetdistributionq(x)withthe
Steinscoreapproximation,∇ logq(x),bymeansofascore-matchingnetwork(e.g.,denoising
x
scorematching[209],slidedscorematching[210]). ThelatteristheannealedLangevindynamics
(ALD),thatisasamplingalgorithmgeneratingsampleswithaniterativeLangevinMonte
Carloprocessateachupdatestep. Thefundamentalideabehinddenoisingscorematchingis
toprocesstheobserveddatax0withtheforwardtransitionkernelq(xk|x0) = N(x0,σ2I),and
k
toestimatejointlytheSteinscoresforthenoisedensitydistributionsq (x),q (x),...,q (x).
|                                                  |     |     |     |     |     |     |        |      | σ1   | σ2            | σk  |
| ------------------------------------------------ | --- | --- | --- | --- | --- | --- | ------ | ---- | ---- | ------------- | --- |
| Inthiscase,theSteinscorefornoisedensityfunctionq |     |     |     |     |     |     | (x)is∇ | logq | (x). |               |     |
|                                                  |     |     |     |     |     |     | σk     | x    | σk   | Hence,aneural |     |
networks (x,σ ),withlearnableparametersθ,canapproximatetheSteinscore. Theinitial
θ x
objectivefunctionisthereforegivenby:
|     |     |     | E [δ(k)||s |     | (xk,k) | − ∇klogq |     | (xk)||2]. |     |     | (A6) |
| --- | --- | --- | ---------- | --- | ------ | -------- | --- | --------- | --- | --- | ---- |
|     |     |     | k,x0,xk    |     | θ      | x        | σk  |           |     |     |      |
Subsequently, the ALD algorithm is used for the sampling phase. The algorithm is
initialised with a sequence of increasing noise levels σ ,...,σ and a starting sample
|        |              |     |                           |     |                                      |           | 1   | K         |     |     |      |
| ------ | ------------ | --- | ------------------------- | --- | ------------------------------------ | --------- | --- | --------- | --- | --- | ---- |
| xK,0   | I).          |     | K,K−1,...,0,xk            |     |                                      |           |     |           |     |     |      |
| ∼ N(0, | Fork         | =   |                           |     | isupdatedwithNiterationsthatcompute: |           |     |           |     |     |      |
|        |              |     |                           |     | z ← N(0,                             | I)        |     |           |     |     | (A7) |
|        |              |     | xk,n xk,n−1               |     | 1                                    | (xk,n−1,σ |     | (cid:112) |     |     |      |
|        |              |     | ←                         | +   | ψ s                                  |           | )   | + ψ z,    |     |     | (A8) |
|        |              |     |                           |     | 2 k                                  | θ         | k   | k         |     |     |      |
| wheren | =1,...,Nandψ |     | representthestepofupdate. |     |                                      |           |     |           |     |     |      |
k

Information2023,14,598 27of35
AppendixB.3. StochasticDifferentialEquations
As described in Appendices B.1 and B.2, both DDPMs and SGMs models define a
discrete forward process, considering N iterations of diffusion steps. In order to define a
continuousdiffusionprocess,asolutionbasedonstochasticdifferentialequations(SDEs)[176]
hasbeenproposed. SincebothDDPMsandSGMsarediscreteformsofSDEs,theSDEs
formulation can be considered as an extension of the aforementioned two definitions.
Therefore,thebackwardprocessismodelledasatime-reverseSDE(seeEquation(A10)),and
thesamplescanbegeneratedbysolvingtime-reverseSDE.AgeneralexpressionofSDEis
definedasfollows:
dx = f(x,k)dk + g(k)dw, (A9)
andthetime-reverseSDE[211]is:
dx = [f(x,k) − g(k)2∇ logq (x)]dk + g(k)dw˜, (A10)
x k
wherewandw˜ arestandardWienerprocesses[212]. Itcanbeproved[176]thatthesampling
fromtheprobabilityflowordinarydifferentialequations(ODE)yieldsthesamedistributionof
thetime-reverseSDE:
1
dx = [f(x,k) − g(x)∇ logq (x)]dk, (A11)
x k
2
where f(x,k)and g(k)arethedriftanddiffusioncoefficientsforthediffusionprocess,re-
spectively,and∇ logq (x)istheSteinscorethatcanbelearnedwithsimilarmethodsas
x k
inSGMs(seeAppendixB.2). Atthispoint,itcanobservedthattheDDPMscanberefor-
mulatedintermsofSDEs,thatgenerallyknownasvariancepreserving(VP)SDE[176]. The
samereformulationcanbedonefortheforwardprocessofSGMs,wherethecorresponding
SDEisknownasvarianceexploding(VE)SDE[176]. Afterhavinglearnedthescoremodel
s (x,k),thesamplesaregeneratedbysolvingthetime-reverseSDEortheprobabilityflow
θ
ODEwithALDtechniques.
References
1. Chianese,E.;Camastra,F.;Ciaramella,A.;Landi,T.C.;Staiano,A.;Riccio,A. Spatio-temporallearninginpredictingambient
particulatematterconcentrationbymulti-layerperceptron. Ecol.Inform.2019,49,54–61.[CrossRef]
2. Feng, Y.; Zhang, W.; Sun, D.; Zhang, L. Ozoneconcentrationforecastmethodbasedongeneticalgorithmoptimizedback
propagationneuralnetworksandsupportvectormachinedataclassification. Atmos.Environ.2011,45,1979–1985.[CrossRef]
3. Paine,C.T.;Marthews,T.R.;Vogt,D.R.;Purves,D.;Rees,M.;Hector,A.;Turnbull,L.A. Howtofitnonlinearplantgrowthmodels
andcalculategrowthrates:Anupdateforecologists. MethodsEcol.Evol.2012,3,245–256.[CrossRef]
4. Pala,Z.;Atici,R. Forecastingsunspottimeseriesusingdeeplearningmethods. Sol.Phys.2019,294,50.[CrossRef]
5. Duarte,F.B.;TenreiroMachado,J.;MonteiroDuarte,G. DynamicsoftheDowJonesandtheNASDAQstockindexes. Nonlinear
Dyn.2010,61,691–705.[CrossRef]
6. Binkowski,M.;Marti,G.;Donnat,P. Autoregressiveconvolutionalneuralnetworksforasynchronoustimeseries. InProceedings
oftheInternationalConferenceonMachineLearning,Stockholm,Sweden,10–15July2018;pp.580–589.
7. Ugurlu,U.;Oksuz,I.;Tas,O. Electricitypriceforecastingusingrecurrentneuralnetworks. Energies2018,11,1255.[CrossRef]
8. Kuan, L.; Yan, Z.; Xin, W.; Yan, C.; Xiangkun, P.; Wenxue, S.; Zhe, J.; Yong, Z.; Nan, X.; Xin, Z. Short-termelectricityload
forecastingmethodbasedonmultilayeredself-normalisingGRUnetwork. InProceedingsofthe2017IEEEConferenceonEnergy
InternetandEnergySystemIntegration(EI2),Beijing,China,26–28November2017;pp.1–5.
9. Zhu,R.;Liao,W.;Wang,Y. Short-termpredictionforwindpowerbasedontemporalconvolutionalnetwork. EnergyRep.2020,
6,424–429.[CrossRef]
10. Koprinska,I.;Wu,D.;Wang,Z. Convolutionalneuralnetworksforenergytimeseriesforecasting. InProceedingsofthe2018
InternationalJointConferenceonNeuralNetworks(IJCNN),RiodeJaneiro,Brazil,8–13July2018;pp.1–8.
11. Li,D.;Jiang,F.;Chen,M.;Qian,T. Multi-step-aheadwindspeedforecastingbasedonahybriddecompositionmethodand
temporalconvolutionalnetworks. Energy2022,238,121981.[CrossRef]
12. Narigina,M.;Kempleis,A.;Romanovs,A. MachineLearning-basedForecastingofSensorDataforEnhancedEnvironmental
Sensing. WseasTrans.Syst.2013,22,543–555.[CrossRef]
13. Han,M.;Xu,M. Laplacianechostatenetworkformultivariatetimeseriesprediction. IEEETrans.NeuralNetw.Learn.Syst.2017,
29,238–244.[CrossRef]

Information2023,14,598 28of35
14. Kumar,D.;Singh,A.;Samui,P.;Jha,R.K. Forecastingmonthlyprecipitationusingsequentialmodelling. Hydrol. Sci. J.2019,
64,690–700.[CrossRef]
15. Wan,R.;Mei,S.;Wang,J.;Liu,M.;Yang,F. Multivariatetemporalconvolutionalnetwork:Adeepneuralnetworksapproachfor
multivariatetimeseriesforecasting. Electronics2019,8,876.[CrossRef]
16. Liu,H.;Zhang,X. AQItimeseriespredictionbasedonahybriddatadecompositionandechostatenetworks. Environ.Sci.Pollut.
Res.2021,28,51160–51182.[CrossRef][PubMed]
17. Akita,R.;Yoshihara,A.;Matsubara,T.;Uehara,K. Deeplearningforstockpredictionusingnumericalandtextualinformation.
InProceedingsofthe2016IEEE/ACIS15thInternationalConferenceonComputerandInformationScience(ICIS),Okayama,
Japan,26–29June2016;pp.1–6.
18. Pang, X.; Zhou, Y.; Wang, P.; Lin, W.; Chang, V. An innovative neural network approach for stock market prediction. J.
Supercomput.2020,76,2098–2118.[CrossRef]
19. Zhang,L.;Aggarwal,C.;Qi,G.J. Stockpricepredictionviadiscoveringmulti-frequencytradingpatterns. InProceedingsofthe
23rdACMSIGKDDInternationalConferenceonKnowledgeDiscoveryandDataMining,Halifax,NS,Canada,13–17August
2017;pp.2141–2149.
20. McNally,S.;Roche,J.;Caton,S. Predictingthepriceofbitcoinusingmachinelearning. InProceedingsofthe201826thEuromicro
InternationalConferenceonParallel,DistributedandNetwork-BasedProcessing(PDP),Cambridge,UK,21–23March2018;
pp.339–343.
21. Ye,J.;Liu,Z.;Du,B.;Sun,L.;Li,W.;Fu,Y.;Xiong,H. Learningtheevolutionaryandmulti-scalegraphstructureformultivariate
timeseriesforecasting. InProceedingsofthe28thACMSIGKDDConferenceonKnowledgeDiscoveryandDataMining,
Washington,DC,USA,14–18August2022;pp.2296–2306.
22. Chen,L.;Chen,D.;Shang,Z.;Wu,B.;Zheng,C.;Wen,B.;Zhang,W.Multi-ScaleAdaptiveGraphNeuralNetworkforMultivariate
TimeSeriesForecasting. IEEETrans.Knowl.DataEng.2023,35,10748–10761.[CrossRef]
23. Song,Y.;Gao,S.;Li,Y.;Jia,L.;Li,Q.;Pang,F. Distributedattention-basedtemporalconvolutionalnetworkforremaininguseful
lifeprediction. IEEEInternetThingsJ.2020,8,9594–9602.[CrossRef]
24. Alhassan,Z.;McGough,A.S.;Alshammari,R.;Daghstani,T.;Budgen,D.;AlMoubayed,N. Type-2diabetesmellitusdiagnosis
fromtimeseriesclinicaldatausingdeeplearningmodels. InProceedingsoftheArtificialNeuralNetworksandMachineLearning–
ICANN2018:27thInternationalConferenceonArtificialNeuralNetworks,Rhodes,Greece,4–7October2018;Proceedings,Part
III27;Springer:Berlin/Heidelberg,Germany,2018;pp.468–478.
25. Kim,T.;King,B.R.Timeseriespredictionusingdeepechostatenetworks. NeuralComput.Appl.2020,32,17769–17787.[CrossRef]
26. Lim,B. Forecastingtreatmentresponsesovertimeusingrecurrentmarginalstructuralnetworks. Adv.NeuralInf.Process.Syst.
2018,31.
27. Huang,S.;Wang,D.;Wu,X.;Tang,A.Dsanet:Dualself-attentionnetworkformultivariatetimeseriesforecasting. InProceedings
ofthe28thACMInternationalConferenceonInformationandKnowledgeManagement,Beijing,China,3–7November2019;
pp.2129–2132.
28. Wu,Z.;Pan,S.;Long,G.;Jiang,J.;Chang,X.;Zhang,C. Connectingthedots:Multivariatetimeseriesforecastingwithgraph
neuralnetworks. InProceedingsofthe26thACMSIGKDDInternationalConferenceonKnowledgeDiscovery&DataMining,
Virtual,6–10July2020;pp.753–763.
29. Cui, Y.; Zheng, K.; Cui, D.; Xie, J.; Deng, L.; Huang, F.; Zhou, X. METRO:Agenericgraphneuralnetworkframeworkfor
multivariatetimeseriesforecasting. Proc.VldbEndow.2021,15,224–236.[CrossRef]
30. Zhao,W.;Gao,Y.;Ji,T.;Wan,X.;Ye,F.;Bai,G. Deeptemporalconvolutionalnetworksforshort-termtrafficflowforecasting.
IEEEAccess2019,7,114496–114507.[CrossRef]
31. Sagheer,A.;Kotb,M. TimeseriesforecastingofpetroleumproductionusingdeepLSTMrecurrentnetworks. Neurocomputing
2019,323,203–213.[CrossRef]
32. Sánchez,L.;Anseán,D.;Otero,J.;Couso,I. AssessingthehealthofLiFePO4tractionbatteriesthroughmonotonicechostate
networks. Sensors2017,18,9.[CrossRef][PubMed]
33. Zhang,Y.;Xiong,R.;He,H.;Pecht,M.G. Longshort-termmemoryrecurrentneuralnetworkforremainingusefullifeprediction
oflithium-ionbatteries. IEEETrans.Veh.Technol.2018,67,5695–5705.[CrossRef]
34. Colla,V.;Matino,I.;Dettori,S.;Cateni,S.;Matino,R.Reservoircomputingapproachesappliedtoenergymanagementinindustry.
InProceedingsoftheEngineeringApplicationsofNeuralNetworks:20thInternationalConference,EANN2019,Xersonisos,
Crete,Greece,24–26May2019;Proceedings20;Springer:Berlin/Heidelberg,Germany,2019;pp.66–79.
35. Li,Z.;Zheng,Z.;Outbib,R. Adaptiveprognosticoffuelcellsbyimplementingensembleechostatenetworksintime-varying
modelspace. IEEETrans.Ind.Electron.2019,67,379–389.[CrossRef]
36. Bala,A.;Ismail,I.;Ibrahim,R.;Sait,S.M.;Oliva,D. Animprovedgrasshopperoptimizationalgorithmbasedechostatenetwork
forpredictingfaultsinairplaneengines. IEEEAccess2020,8,159773–159789.[CrossRef]
37. Mahmoud,A.;Mohammed,A. Asurveyondeeplearningfortimeseriesforecasting. InMachineLearningandBigDataAnalytics
Paradigms:Analysis,ApplicationsandChallenges;Springer:Cham,Switzerland,2021;pp.365–392.
38. Lim,B.;Zohren,S. Time-seriesforecastingwithdeeplearning:Asurvey. Philos.Trans.R.Soc. 2021,379,20200209.[CrossRef]
[PubMed]

Information2023,14,598 29of35
39. Sezer,O.B.;Gudelek,M.U.;Ozbayoglu,A.M. Financialtimeseriesforecastingwithdeeplearning:Asystematicliteraturereview:
2005–2019. Appl.SoftComput.2020,90,106181.[CrossRef]
40. Zeroual,A.;Harrou,F.;Dairi,A.;Sun,Y. DeeplearningmethodsforforecastingCOVID-19time-Seriesdata:AComparative
study. ChaosSolitonsFractals2020,140,110121.[CrossRef]
41. Lara-Benítez,P.;Carranza-García,M.;Riquelme,J.C. Anexperimentalreviewondeeplearningarchitecturesfortimeseries
forecasting. Int.J.NeuralSyst.2021,31,2130001.[CrossRef]
42. Barrera-Animas,A.Y.;Oyedele,L.O.;Bilal,M.;Akinosho,T.D.;Delgado,J.M.D.;Akanbi,L.A. Rainfallprediction:Acomparative
analysisofmodernmachinelearningalgorithmsfortimeseriesforecasting. Mach.Learn.Appl.2022,7,100204.[CrossRef]
43. Lakshmanna,K.;Kaluri,R.;Gundluru,N.;Alzamil,Z.S.;Rajput,D.S.;Khan,A.A.;Haq,M.A.;Alhussen,A. Areviewondeep
learningtechniquesforIoTdata. Electronics2022,11,1604.[CrossRef]
44. Makridakis,S.;Spiliotis,E.;Assimakopoulos,V. TheM4Competition:100,000timeseriesand61forecastingmethods. Int. J.
Forecast.2020,36,54–74.[CrossRef]
45. Goodfellow,I.;Bengio,Y.;Courville,A. DeepLearning;MITPress:Cambridge,MA,USA,2016.
46. Hastie,T.;Tibshirani,R.;Friedman,J.H.;Friedman,J.H. TheElementsofStatisticalLearning:DataMining,Inference,andPrediction;
Springer:Berlin/Heidelberg,Germany,2009;Volume2.
47. Gudelek,M.U.;Boluk,S.A.;Ozbayoglu,A.M. Adeeplearningbasedstocktradingmodelwith2-DCNNtrenddetection. In
Proceedingsofthe2017IEEESymposiumSeriesonComputationalIntelligence(SSCI),Honolulu,HI,USA,27November–1
December2017;pp.1–8.
48. Kuo,P.H.;Huang,C.J. Ahighprecisionartificialneuralnetworksmodelforshort-termenergyloadforecasting. Energies2018,
11,213.[CrossRef]
49. Zahid,M.;Ahmed,F.;Javaid,N.;Abbasi,R.A.;ZainabKazmi,H.S.;Javaid,A.;Bilal,M.;Akbar,M.;Ilahi,M. Electricitypriceand
loadforecastingusingenhancedconvolutionalneuralnetworkandenhancedsupportvectorregressioninsmartgrids. Electronics
2019,8,122.[CrossRef]
50. Cai,M.;Pipattanasomporn,M.;Rahman,S. Day-aheadbuilding-levelloadforecastsusingdeeplearningvs. traditionaltime
seriestechniques. Appl.Energy2019,236,1078–1088.[CrossRef]
51. Bronstein,M.M.;Bruna,J.;LeCun,Y.;Szlam,A.;Vandergheynst,P. Geometricdeeplearning:Goingbeyondeuclideandata. IEEE
SignalProcess.Mag.2017,34,18–42.[CrossRef]
52. Lea,C.;Flynn,M.D.;Vidal,R.;Reiter,A.;Hager,G.D. Temporalconvolutionalnetworksforactionsegmentationanddetection.
InProceedingsoftheIEEEConferenceonComputerVisionandPatternRecognition,Virtual,6–10July2017;pp.156–165.
53. Borovykh,A.;Bohte,S.;Oosterlee,C.W. Dilatedconvolutionalneuralnetworksfortimeseriesforecasting. J.Comput.Financ.
Forthcom.2018.[CrossRef]
54. Lara-Benítez,P.;Carranza-García,M.;Luna-Romera,J.M.;Riquelme,J.C. Temporalconvolutionalnetworksappliedtoenergy-
relatedtimeseriesforecasting. Appl.Sci.2020,10,2322.[CrossRef]
55. Hewage,P.;Behera,A.;Trovati,M.;Pereira,E.;Ghahremani,M.;Palmieri,F.;Liu,Y.Temporalconvolutionalneural(TCN)network
foraneffectiveweatherforecastingusingtimeseriesdatafromthelocalweatherstation. SoftComput. 2020,24,16453–16482.
[CrossRef]
56. Sfetsos,A.;Coonick,A. Univariateandmultivariateforecastingofhourlysolarradiationwithartificialintelligencetechniques.
Sol.Energy2000,68,169–178.[CrossRef]
57. Hsieh,T.J.; Hsiao,H.F.; Yeh,W.C. Forecastingstockmarketsusingwavelettransformsandrecurrentneuralnetworks: An
integratedsystembasedonartificialbeecolonyalgorithm. Appl.SoftComput.2011,11,2510–2525.[CrossRef]
58. Elman,J.L. Findingstructureintime. Cogn.Sci.1990,14,179–211.[CrossRef]
59. Jaeger,H. The“echostate”approachtoanalysingandtrainingrecurrentneuralnetworks-withanerratumnote. BonnGer.Ger.
Natl.Res.Cent.Inf.Technol.GmdTech.Rep.2001,148,13.
60. Hochreiter,S.;Schmidhuber,J. Longshort-termmemory. NeuralComput.1997,9,1735–1780.[CrossRef]
61. Cho,K.;vanMerrienboer,B.;Gulcehre,C.;Bahdanau,D.;Bougares,F.;Schwenk,H.;Bengio,Y. LearningPhraseRepresentations
usingRNNEncoder–DecoderforStatisticalMachineTranslation. InProceedingsofthe2014ConferenceonEmpiricalMethodsin
NaturalLanguageProcessing(EMNLP),Doha,Qatar,25–29October2014;AssociationforComputationalLinguistics:Cedarville,
OH,USA,2014;p.1724.
62. Williams,R.J.;Zipser,D. Alearningalgorithmforcontinuallyrunningfullyrecurrentneuralnetworks. NeuralComput.1989,
1,270–280.[CrossRef]
63. Jordan,M.I. Serialorder: Aparalleldistributedprocessingapproach. InAdvancesinPsychology;Elsevier: Amsterdam,The
Netherlands,1997;Volume121,pp.471–495.
64. Shi,H.;Xu,M.;Ma,Q.;Zhang,C.;Li,R.;Li,F. Awholesystemassessmentofnoveldeeplearningapproachonshort-termload
forecasting. EnergyProcedia2017,142,2791–2796.[CrossRef]
65. Mohammadi,M.;Talebpour,F.;Safaee,E.;Ghadimi,N.;Abedinia,O. Small-scalebuildingloadforecastbasedonhybridforecast
engine. NeuralProcess.Lett.2018,48,329–351.[CrossRef]
66. Ruiz,L.G.B.;Rueda,R.;Cuéllar,M.P.;Pegalajar,M. EnergyconsumptionforecastingbasedonElmanneuralnetworkswith
evolutiveoptimization. ExpertSyst.Appl.2018,92,380–389.[CrossRef]
67. Bishop,C.M. NeuralNetworksforPatternRecognition;OxfordUniversityPress:Oxford,UK,1995.

Information2023,14,598 30of35
68. Kantz,H.;Schreiber,T. NonlinearTimeSeriesAnalysis;CambridgeUniversityPress:Cambridge,UK,2004;Volume7.
69. Simonyan,K.;Vedaldi,A.;Zisserman,A. Deepinsideconvolutionalnetworks: Visualisingimageclassificationmodelsand
saliencymaps. arXiv2013,arXiv:1312.6034.
70. Selvaraju,R.R.;Cogswell,M.;Das,A.;Vedantam,R.;Parikh,D.;Batra,D. Grad-cam:Visualexplanationsfromdeepnetworks
viagradient-basedlocalization. InProceedingsoftheIEEEInternationalConferenceonComputerVision,Venice,Italy,22–29
October2017;pp.618–626.
71. Morando,S.;Jemei,S.;Hissel,D.;Gouriveau,R.;Zerhouni,N. ANOVAmethodappliedtoprotonexchangemembranefuelcell
ageingforecastingusinganechostatenetwork. Math.Comput.Simul.2017,131,283–294.[CrossRef]
72. Antonelo,E.A.;Camponogara,E.;Foss,B. Echostatenetworksfordata-drivendownholepressureestimationingas-liftoilwells.
NeuralNetw.2017,85,106–117.[CrossRef][PubMed]
73. Shen,L.;Chen,J.;Zeng,Z.;Yang,J.;Jin,J. Anovelechostatenetworkformultivariateandnonlineartimeseriesprediction. Appl.
SoftComput.2018,62,524–535.[CrossRef]
74. Jing,Z.;Yuxi,L.;Yan,C.;Bao,Y.;Jiakui,Z.;Di,L. PhotovoltaicOutputPredictionModelBasedonEchoStateNetworkswith
WeatherTypeIndex. InProceedingsofthe20193rdInternationalConferenceonInnovationinArtificialIntelligence,Suzhou,
China,15–18March2019;pp.91–95.
75. Hu,H.;Wang,L.;Peng,L.;Zeng,Y.R. Effectiveenergyconsumptionforecastingusingenhancedbaggedechostatenetwork.
Energy2020,193,116778.[CrossRef]
76. Mansoor, M.; Grimaccia, F.; Mussetta, M. Echo State Network Performance in Electrical and Industrial Applications. In
Proceedingsofthe2020InternationalJointConferenceonNeuralNetworks(IJCNN),Glasgow,UK,19–24July2020;pp.1–7.
77. Hu,H.;Wang,L.;Lv,S.X. Forecastingenergyconsumptionandwindpowergenerationusingdeepechostatenetwork. Renew.
Energy2020,154,598–613.[CrossRef]
78. Yang,Y.;Zhao,X.;Liu,X. Anovelechostatenetworkanditsapplicationintemperaturepredictionofexhaustgasfromhotblast
stove. IEEETrans.Instrum.Meas.2020,69,9465–9476.[CrossRef]
79. Li,N.;Tuo,J.;Wang,Y.;Wang,M. Predictionofbloodglucoseconcentrationfortype1diabetesbasedonechostatenetworks
embeddedwithincrementallearning. Neurocomputing2020,378,248–259.[CrossRef]
80. Gao,R.;Du,L.;Duru,O.;Yuen,K.F. Timeseriesforecastingbasedonechostatenetworkandempiricalwavelettransformation.
Appl.SoftComput.2021,102,107111.[CrossRef]
81. Mansoor,M.;Grimaccia,F.;Leva,S.;Mussetta,M. Comparisonofechostatenetworkandfeed-forwardneuralnetworksin
electricalloadforecastingfordemandresponseprograms. Math.Comput.Simul.2021,184,282–293.[CrossRef]
82. Sui,Y.;Gao,H. Modifiedechostatenetworkforpredictionofnonlinearchaotictimeseries. NonlinearDyn.2022,110,3581–3603.
[CrossRef]
83. Marino, D.L.; Amarasinghe, K.; Manic, M. Building energy load forecasting using deep neural networks. In Proceed-
ingsoftheIECON2016—42ndAnnualConferenceoftheIEEEIndustrialElectronicsSociety, Florence, Italy, 23-26October
2016;pp.7046–7051.
84. Fu,R.;Zhang,Z.;Li,L. UsingLSTMandGRUneuralnetworkmethodsfortrafficflowprediction. InProceedingsofthe2016
31stYouthAcademicAnnualConferenceofChineseAssociationofAutomation(YAC),Wuhan,China,11–13November2016;
pp.324–328.
85. Li,Z.;Tam,V. Combiningthereal-timewaveletdenoisingandlong-short-term-memoryneuralnetworkforpredictingstock
indexes. InProceedingsofthe2017IEEESymposiumSeriesonComputationalIntelligence(SSCI),Honolulu,HI,USA,27
November–1December2017;pp.1–8.
86. dosSantosPinheiro,L.;Dras,M. Stockmarketpredictionwithdeeplearning: Acharacter-basedneurallanguagemodelfor
event-basedtrading. InProceedingsoftheAustralasianLanguageTechnologyAssociationWorkshop2017,Brisbane,Australia,
6–8December2017;pp.6–15.
87. Shi,H.;Xu,M.;Li,R. Deeplearningforhouseholdloadforecasting—AnovelpoolingdeepRNN. IEEETrans.SmartGrid2017,
9,5271–5280.[CrossRef]
88. Li,X.;Peng,L.;Yao,X.;Cui,S.;Hu,Y.;You,C.;Chi,T. Longshort-termmemoryneuralnetworkforairpollutantconcentration
predictions:Methoddevelopmentandevaluation. Environ.Pollut.2017,231,997–1004.[CrossRef][PubMed]
89. Baek,Y.;Kim,H.Y. ModAugNet: Anewforecastingframeworkforstockmarketindexvaluewithanoverfittingprevention
LSTMmoduleandapredictionLSTMmodule. ExpertSyst.Appl.2018,113,457–480.[CrossRef]
90. Fischer,T.;Krauss,C. Deeplearningwithlongshort-termmemorynetworksforfinancialmarketpredictions. Eur.J.Oper.Res.
2018,270,654–669.[CrossRef]
91. Kratzert,F.;Klotz,D.;Brenner,C.;Schulz,K.;Herrnegger,M. Rainfall–runoffmodellingusingLongShort-TermMemory(LSTM)
networks. Hydrol.EarthSyst.Sci.2018,22,6005–6022.[CrossRef]
92. Zhang,J.;Zhu,Y.;Zhang,X.;Ye,M.;Yang,J. DevelopingaLongShort-TermMemory(LSTM)basedmodelforpredictingwater
tabledepthinagriculturalareas. J.Hydrol.2018,561,918–929.[CrossRef]
93. Bouktif,S.;Fiaz,A.;Ouni,A.;Serhani,M.A.Optimaldeeplearninglstmmodelforelectricloadforecastingusingfeatureselection
andgeneticalgorithm:Comparisonwithmachinelearningapproaches. Energies2018,11,1636.[CrossRef]
94. Xu,L.;Li,C.;Xie,X.;Zhang,G. Long-short-termmemorynetworkbasedhybridmodelforshort-termelectricalloadforecasting.
Information2018,9,165.[CrossRef]

Information2023,14,598 31of35
95. Wang, Y.; Shen, Y.; Mao, S.; Chen, X.; Zou, H. LASSOandLSTMintegratedtemporalmodelforshort-termsolarintensity
forecasting. IEEEInternetThingsJ.2018,6,2933–2944.[CrossRef]
96. Freeman,B.S.;Taylor,G.;Gharabaghi,B.;Thé,J. Forecastingairqualitytimeseriesusingdeeplearning. J.AirWasteManag.Assoc.
(1995)2018,68,866–886.[CrossRef]
97. Wang,Y.;Smola,A.;Maddix,D.;Gasthaus,J.;Foster,D.;Januschowski,T. Deepfactorsforforecasting. InProceedingsofthe
InternationalConferenceonMachineLearning,LongBeach,CA,USA,9–15June2019;pp.6607–6617.
98. Nichiforov,C.;Stamatescu,G.;Stamatescu,I.;Fa˘ga˘ra˘s¸an,I.Evaluationofsequence-learningmodelsforlarge-commercial-building
loadforecasting. Information2019,10,189.[CrossRef]
99. Zou,M.;Fang,D.;Harrison,G.;Djokic,S. Weatherbasedday-aheadandweek-aheadloadforecastingusingdeeprecurrent
neuralnetwork. InProceedingsofthe2019IEEE5thInternationalforumonResearchandTechnologyforSocietyandIndustry
(RTSI),Florence,Italy,9–12September2019;pp.341–346.
100. Chimmula,V.K.R.;Zhang,L. TimeseriesforecastingofCOVID-19transmissioninCanadausingLSTMnetworks. ChaosSolitons
Fractals2020,135,109864.[CrossRef][PubMed]
101. Wu,Y.;Ni,J.;Cheng,W.;Zong,B.;Song,D.;Chen,Z.;Liu,Y.;Zhang,X.;Chen,H.;Davidson,S.B. Dynamicgaussianmixture
baseddeepgenerativemodelforrobustforecastingonsparsemultivariatetimeseries. InProceedingsoftheAAAIConference
onArtificialIntelligence,Virtual,2–9February2021;Volume35,pp.651–659.
102. Dastgerdi,A.K.;Mercorelli,P. InvestigatingtheeffectofnoiseeliminationonLSTMmodelsforfinancialmarketsprediction
usingKalmanFilterandWaveletTransform. WSEASTrans.Bus.Econ.2022,19,432–441.[CrossRef]
103. Wang,Y.;Liao,W.;Chang,Y. Gatedrecurrentunitnetwork-basedshort-termphotovoltaicforecasting. Energies2018,11,2163.
[CrossRef]
104. Du,Y.; Wang,J.; Feng,W.; Pan,S.; Qin,T.; Xu,R.; Wang,C. Adarnn: Adaptivelearningandforecastingoftimeseries. In
Proceedingsofthe30thACMInternationalConferenceonInformation&KnowledgeManagement,GoldCoast,QLD,Australia,
1–5November2021;pp.402–411.
105. Bollerslev,T. Generalizedautoregressiveconditionalheteroskedasticity. J.Econom.1986,31,307–327.[CrossRef]
106. Gensler,A.;Henze,J.;Sick,B.;Raabe,N. DeepLearningforsolarpowerforecasting—AnapproachusingAutoEncoderand
LSTMNeuralNetworks. InProceedingsofthe2016IEEEInternationalConferenceonSystems,Man,andCybernetics(SMC),
Budapest,Hungary,9–12October2016;pp.2858–2865.
107. Bao,W.;Yue,J.;Rao,Y. Adeeplearningframeworkforfinancialtimeseriesusingstackedautoencodersandlong-shortterm
memory. PLoSONE2017,12,e0180944.[CrossRef][PubMed]
108. Lee,C.Y.;Soo,V.W. Predictstockpricewithfinancialnewsbasedonrecurrentconvolutionalneuralnetworks. InProceedings
ofthe2017ConferenceonTechnologiesandApplicationsofArtificialIntelligence(TAAI),Taipei,Taiwan,1–3December2017;
pp.160–165.
109. Kuo,P.H.;Huang,C.J. Anelectricitypriceforecastingmodelbyhybridstructureddeepneuralnetworks. Sustainability2018,
10,1280.[CrossRef]
110. Tian,C.;Ma,J.;Zhang,C.;Zhan,P. Adeepneuralnetworkmodelforshort-termloadforecastbasedonlongshort-termmemory
networkandconvolutionalneuralnetwork. Energies2018,11,3493.[CrossRef]
111. Liu,H.;Mi,X.;Li,Y.Smartdeeplearningbasedwindspeedpredictionmodelusingwaveletpacketdecomposition,convolutional
neuralnetworkandconvolutionallongshorttermmemorynetwork. EnergyConvers.Manag.2018,166,120–131.[CrossRef]
112. Chen,Y.;Wu,J.;Bu,H. Stockmarketembeddingandprediction: Adeeplearningmethod. InProceedingsofthe201815th
InternationalConferenceonServiceSystemsandServiceManagement(ICSSSM),Hangzhou,China,21–22July2018;pp.1–6.
113. Hossain,M.A.;Karim,R.;Thulasiram,R.;Bruce,N.D.;Wang,Y. Hybriddeeplearningmodelforstockpriceprediction. In
Proceedingsofthe2018IEEESymposiumSeriesonComputationalIntelligence(SSCI),Bangalore,India,18–21November2018;
pp.1837–1844.
114. Kim,H.Y.;Won,C.H.Forecastingthevolatilityofstockpriceindex:AhybridmodelintegratingLSTMwithmultipleGARCH-type
models. ExpertSyst.Appl.2018,103,25–37.[CrossRef]
115. Li,Y.; Yu,R.; Shahabi,C.; Liu,Y. DiffusionConvolutionalRecurrentNeuralNetwork: Data-DrivenTrafficForecasting. In
ProceedingsoftheInternationalConferenceonLearningRepresentations,Vancouver,BC,Canada,30April–3May2018.
116. Huang,C.J.;Kuo,P.H.AdeepCNN-LSTMmodelforparticulatematter(PM2.5)forecastinginsmartcities. Sensors2018,18,2220.
[CrossRef]
117. Soh, P.W.; Chang, J.W.; Huang, J.W. Adaptive deep learning-based air quality prediction model using the most relevant
spatial-temporalrelations. IEEEAccess2018,6,38186–38199.[CrossRef]
118. Fan,C.;Zhang,Y.;Pan,Y.;Li,X.;Zhang,C.;Yuan,R.;Wu,D.;Wang,W.;Pei,J.;Huang,H. Multi-horizontimeseriesforecasting
withtemporalattentionlearning. InProceedingsofthe25thACMSIGKDDInternationalConferenceonKnowledgeDiscovery&
DataMining,Anchorage,AK,USA,4–8August2019;pp.2527–2535.
119. Pan,C.;Tan,J.;Feng,D.;Li,Y. Veryshort-termsolargenerationforecastingbasedonLSTMwithtemporalattentionmechanism.
InProceedingsofthe2019IEEE5thInternationalConferenceonComputerandCommunications(ICCC),Chengdu,China,6–9
December2019;pp.267–271.
120. Wang,S.;Wang,X.;Wang,S.;Wang,D. Bi-directionallongshort-termmemorymethodbasedonattentionmechanismandrolling
updateforshort-termloadforecasting. Int.J.Electr.PowerEnergySyst.2019,109,470–479.[CrossRef]

Information2023,14,598 32of35
121. Shen,Z.;Zhang,Y.;Lu,J.;Xu,J.;Xiao,G. Anoveltimeseriesforecastingmodelwithdeeplearning. Neurocomputing2020,
396,302–313.[CrossRef]
122. Pal,R.;Sekh,A.A.;Kar,S.;Prasad,D.K. NeuralnetworkbasedcountrywiseriskpredictionofCOVID-19. Appl. Sci. 2020,
10,6448.[CrossRef]
123. Dudukcu,H.V.;Taskiran,M.;Taskiran,Z.G.C.;Yildirim,T. TemporalConvolutionalNetworkswithRNNapproachforchaotic
timeseriesprediction. Appl.SoftComput.2023,133,109945.[CrossRef]
124. Scarselli,F.;Gori,M.;Tsoi,A.C.;Hagenbuchner,M.;Monfardini,G. Thegraphneuralnetworkmodel. IEEETrans.NeuralNetw.
2008,20,61–80.[CrossRef]
125. Hamilton,W.L. GraphRepresentationLearning;Morgan&ClaypoolPublishers:SanRafael,CA,USA,2020.
126. Cheng,D.;Yang,F.;Xiang,S.;Liu,J. Financialtimeseriesforecastingwithmulti-modalitygraphneuralnetwork. PatternRecognit.
2022,121,108218.[CrossRef]
127. Geng,X.;He,X.;Xu,L.;Yu,J. Graphcorrelatedattentionrecurrentneuralnetworkformultivariatetimeseriesforecasting. Inf.
Sci.2022,606,126–142.[CrossRef]
128. Xiang,S.;Cheng,D.;Shang,C.;Zhang,Y.;Liang,Y. TemporalandHeterogeneousGraphNeuralNetworkforFinancialTime
SeriesPrediction. InProceedingsofthe31stACMInternationalConferenceonInformation&KnowledgeManagement,Atlanta,
GA,USA,17–21October2022;pp.3584–3593.
129. Jin,M.;Zheng,Y.;Li,Y.F.;Chen,S.;Yang,B.;Pan,S. Multivariatetimeseriesforecastingwithdynamicgraphneuralodes. IEEE
Trans.Knowl.DataEng.2022,35,9168–9180.[CrossRef]
130. Liu,Y.;Liu,Q.;Zhang,J.W.;Feng,H.;Wang,Z.;Zhou,Z.;Chen,W.Multivariatetimeseriesforecastingwithtemporalpolynomial
graphneuralnetworks. Adv.NeuralInf.Process.Syst.2022,35,19414–19426.
131. Williams,C.K.;Rasmussen,C.E. GaussianProcessesforMachineLearning;MITPress:Cambridge,MA,USA,2006;Volume2.
132. Berg,C.;Christensen,J.P.R.;Ressel,P. HarmonicAnalysisonSemigroups:TheoryofPositiveDefiniteandRelatedFunctions;Springer:
Berlin/Heidelberg,Germany,1984;Volume100.
133. Hensman,J.;Fusi,N.;Lawrence,N.D. Gaussianprocessesforbigdata. arXiv2013,arXiv:1309.6835.
134. Damianou,A.;Lawrence,N.D. Deepgaussianprocesses. InProceedingsoftheArtificialIntelligenceandStatistics,Scottsdale,
AZ,USA,29April–1May2013;pp.207–215.
135. You,J.;Li,X.;Low,M.;Lobell,D.;Ermon,S. Deepgaussianprocessforcropyieldpredictionbasedonremotesensingdata. In
ProceedingsoftheAAAIConferenceonArtificialIntelligence,SanFrancisco,CA,USA,4–9February2017;Volume31.
136. Mahdi, M.D.; Mrittika, N.J.; Shams, M.; Chowdhury, L.; Siddique, S. ADeepGaussianProcessforForecastingCropYield
andTimeSeriesAnalysisofPrecipitationBasedinMunshiganj,Bangladesh. InProceedingsoftheIGARSS2020—2020IEEE
InternationalGeoscienceandRemoteSensingSymposium,Waikoloa,HI,USA,26September–2October2020;pp.1331–1334.
137. Jiang,Y.;Fan,J.;Liu,Y.;Zhang,X. DeepgraphGaussianprocessesforshort-termtrafficflowforecastingfromspatiotemporal
data. IEEETrans.Intell.Transp.Syst.2022,23,20177–20186.[CrossRef]
138. Chang,W.;Li,R.;Fu,Y.;Xiao,Y.;Zhou,S. Amultistepforecastingmethodforonlinecar-hailingdemandbasedonwavelet
decompositionanddeepGaussianprocessregression. J.Supercomput.2023,79,3412–3436.[CrossRef]
139. Camastra,F.;Casolaro,A.;Iannuzzo,G. TimeSeriespredictionwithmissingdatabyanIteratedDeepGaussianProcess. In
Proceedingsofthe31stEditionofWIRN2023,VietrisulMare,Salerno,Italy,22–26May2023.
140. Goodfellow,I.;Pouget-Abadie,J.;Mirza,M.;Xu,B.;Warde-Farley,D.;Ozair,S.;Courville,A.;Bengio,Y. GenerativeAdversarial
Nets. InProceedingsoftheAdvancesinNeuralInformationProcessingSystems,Montreal,QC,Canada,8–13December2014;
Volume27.
141. Radford,A.;Metz,L.;Chintala,S.Unsupervisedrepresentationlearningwithdeepconvolutionalgenerativeadversarialnetworks.
arXiv2015,arXiv:1511.06434.
142. Mogren,O. C-RNN-GAN:Continuousrecurrentneuralnetworkswithadversarialtraining. arXiv2016,arXiv:1611.09904.
143. Box,G.E.;Jenkins,G.M.;Reinsel,G.C.;Ljung,G.M. TimeSeriesAnalysis:ForecastingandControl;JohnWiley&Sons:Hoboken,NJ,
USA,2015.
144. Wu,D.;Hur,K.;Xiao,Z.AGAN-EnhancedEnsembleModelforEnergyConsumptionForecastinginLargeCommercialBuildings.
IEEEAccess2021,9,158820–158830.[CrossRef]
145. Mirza,M.;Osindero,S. Conditionalgenerativeadversarialnets. arXiv2014,arXiv:1411.1784.
146. Chen,X.;Duan,Y.;Houthooft,R.;Schulman,J.;Sutskever,I.;Abbeel,P. InfoGAN:InterpretableRepresentationLearningby
InformationMaximisingGenerativeAdversarialNets. Adv.NeuralInf.Process.Syst.2016,29.
147. Wang, H.; Tao, G.; Ma, J.; Jia, S.; Chi, L.; Yang, H.; Zhao, Z.; Tao, J. Predicting the epidemics trend of COVID-19 using
epidemiological-basedgenerativeadversarialnetworks. IEEEJ.Sel.Top.SignalProcess.2022,16,276–288.[CrossRef]
148. Wiese,M.;Knobloch,R.;Korn,R.;Kretschmer,P. QuantGANs:Deepgenerationoffinancialtimeseries. Quant.Financ.2020,
20,1419–1440.[CrossRef]
149. Hazra,D.;Byun,Y.C. SynSigGAN:Generativeadversarialnetworksforsyntheticbiomedicalsignalgeneration. Biology2020,
9,441.[CrossRef][PubMed]
150. Esteban,C.;Hyland,S.L.;Rätsch,G. Real-valued(medical)timeseriesgenerationwithrecurrentconditionalgans. arXiv2017,
arXiv:1706.02633.
151. Yoon,J.;Jarrett,D.;VanderSchaar,M. Time-seriesgenerativeadversarialnetworks. Adv.NeuralInf.Process.Syst.2019,32.

Information2023,14,598 33of35
152. Ni, H.; Szpruch, L.; Wiese, M.; Liao, S.; Xiao, B. Conditional sig-wasserstein gans for time series generation. arXiv 2020,
arXiv:2006.05421.
153. Li, X.; Metsis, V.; Wang, H.; Ngu, A.H.H. Tts-gan: A transformer-based time series generative adversarial network. In
ProceedingsoftheInternationalConferenceonArtificialIntelligenceinMedicine,Halifax,NS,Canada,14–17June2022;Springer:
Berlin/Heidelberg,Germany,2022;pp.133–143.
154. Koochali,A.;Schichtel,P.;Dengel,A.;Ahmed,S. Probabilisticforecastingofsensorydatawithgenerativeadversarialnetworks–
ForGAN. IEEEAccess2019,7,63868–63880.[CrossRef]
155. Bej, A.; Maulik, U.; Sarkar, A. Time-Series prediction for the epidemic trends of COVID-19 using Conditional Generative
adversarialNetworksRegressiononcountry-wisecasestudies. SNComput.Sci.2022,3,352.[CrossRef]
156. Zúñiga,G.;Acuña,G. Probabilisticmultisteptimeseriesforecastingusingconditionalgenerativeadversarialnetworks. In
Proceedingsofthe2021IEEELatinAmericanConferenceonComputationalIntelligence(LA-CCI),Temuco,Chile,2–4November
2021;pp.1–6.
157. Huang,X.;Li,Q.;Tai,Y.;Chen,Z.;Liu,J.;Shi,J.;Liu,W. Timeseriesforecastingforhourlyphotovoltaicpowerusingconditional
generativeadversarialnetworkandBi-LSTM. Energy2022,246,123403.[CrossRef]
158. Li,F.;Zheng,H.;Li,X. Anovelhybridmodelformulti-stepaheadphotovoltaicpowerpredictionbasedonconditionaltime
seriesgenerativeadversarialnetworks. Renew.Energy2022,199,560–586.[CrossRef]
159. Zhou,X.;Pan,Z.;Hu,G.;Tang,S.;Zhao,C. Stockmarketpredictiononhigh-frequencydatausinggenerativeadversarialnets.
Math.Probl.Eng.2018,2018,4907423.[CrossRef]
160. Zhang,Y.;Wang,S.;Chen,B.;Cao,J.;Huang,Z. Trafficgan:Network-scaledeeptrafficpredictionwithgenerativeadversarial
nets. IEEETrans.Intell.Transp.Syst.2019,22,219–230.[CrossRef]
161. Kaushik,S.;Choudhury,A.;Natarajan,S.;Pickett,L.A.;Dutt,V. Medicineexpenditurepredictionviaavariance-basedgenerative
adversarialnetwork. IEEEAccess2020,8,110947–110958.[CrossRef]
162. Gu,Y.;Chen,Q.;Liu,K.;Xie,L.;Kang,C. GAN-basedModelforResidentialLoadGenerationConsideringTypicalConsumption
Patterns. InProceedingsofthe2019IEEEPower&EnergySocietyInnovativeSmartGridTechnologiesConference(ISGT),
Washington,DC,USA,18–21February2019;pp.1–5.
163. He,B.;Kita,E. Stockpricepredictionbyusinghybridsequentialgenerativeadversarialnetworks. InProceedingsofthe2020
InternationalConferenceonDataMiningWorkshops(ICDMW),Sorrento,Italy,17–20November2020;pp.341–347.
164. Wu,S.;Xiao,X.;Ding,Q.;Zhao,P.;Wei,Y.;Huang,J. Adversarialsparsetransformerfortimeseriesforecasting. Adv.NeuralInf.
Process.Syst.2020,33,17105–17115.
165. Li, Q.; Hao, H.; Zhao, Y.; Geng, Q.; Liu, G.; Zhang, Y.; Yu, F. GANs-LSTM model for soil temperature estimation from
meteorological:Anewapproach. IEEEAccess2020,8,59427–59443.[CrossRef]
166. Yin,X.;Han,Y.;Sun,H.;Xu,Z.;Yu,H.;Duan,X. Multi-attentiongenerativeadversarialnetworkformultivariatetimeseries
prediction. IEEEAccess2021,9,57351–57363.[CrossRef]
167. Wu,W.;Huang,F.;Kao,Y.;Chen,Z.;Wu,Q. Predictionmethodofmultiplerelatedtimeseriesbasedongenerativeadversarial
networks. Information2021,12,55.[CrossRef]
168. Jiang,C.;Mao,Y.;Chai,Y.;Yu,M. Day-aheadrenewablescenarioforecastsbasedongenerativeadversarialnetworks. Int. J.
EnergyRes.2021,45,7572–7587.[CrossRef]
169. Bendaoud,N.M.M.;Farah,N.;BenAhmed,S. ComparingGenerativeAdversarialNetworksarchitecturesforelectricitydemand
forecasting. EnergyBuild.2021,247,111152.[CrossRef]
170. Wu,X.;Yang,H.;Chen,H.;Hu,Q.;Hu,H. Long-term4Dtrajectorypredictionusinggenerativeadversarialnetworks. Transp.
Res.PartEmerg.Technol.2022,136,103554.[CrossRef]
171. Ye,Y.;Strong,M.;Lou,Y.;Faulkner,C.A.;Zuo,W.;Upadhyaya,S. Evaluatingperformanceofdifferentgenerativeadversarial
networksforlarge-scalebuildingpowerdemandprediction. EnergyBuild.2022,269,112247.[CrossRef]
172. Vuletic´,M.;Prenzel,F.;Cucuringu,M. Fin-Gan:ForecastingandClassifyingFinancialTimeSeriesviaGenerativeAdversarial
Networks.2023. Availableonline:https://ssrn.com/abstract=4328302(accessedon25September2023).
173. Sohl-Dickstein,J.;Weiss,E.;Maheswaranathan,N.;Ganguli,S. Deepunsupervisedlearningusingnonequilibriumthermodynam-
ics. InProceedingsoftheInternationalConferenceonMachineLearning,Lille,France,7–9July2015;pp.2256–2265.
174. Ho,J.;Jain,A.;Abbeel,P. Denoisingdiffusionprobabilisticmodels. Adv.NeuralInf.Process.Syst.2020,33,6840–6851.
175. Song,Y.;Ermon,S. Generativemodelingbyestimatinggradientsofthedatadistribution. Adv.NeuralInf.Process.Syst.2019,32.
176. Song,Y.;Sohl-Dickstein,J.;Kingma,D.P.;Kumar,A.;Ermon,S.;Poole,B. Score-BasedGenerativeModelingthroughStochastic
DifferentialEquations. InProceedingsoftheInternationalConferenceonLearningRepresentations,AddisAbaba,Ethiopia,
26–32April2020.
177. Rasul,K.;Seward,C.;Schuster,I.;Vollgraf,R. Autoregressivedenoisingdiffusionmodelsformultivariateprobabilistictime
seriesforecasting. InProceedingsoftheInternationalConferenceonMachineLearning,Virtual,18–24July2021;pp.8857–8868.
178. Yan,T.;Zhang,H.;Zhou,T.;Zhan,Y.;Xia,Y. ScoreGrad: Multivariateprobabilistictimeseriesforecastingwithcontinuous
energy-basedgenerativemodels. arXiv2021,arXiv:2106.10121.
179. Li,Y.;Lu,X.;Wang,Y.;Dou,D. Generativetimeseriesforecastingwithdiffusion,denoise,anddisentanglement. Adv.NeuralInf.
Process.Syst.2022,35,23009–23022.

Information2023,14,598 34of35
180. Biloš,M.;Rasul,K.;Schneider,A.;Nevmyvaka,Y.;Günnemann,S. Modelingtemporaldataascontinuousfunctionswithprocess
diffusion. arXiv2022,arXiv:2211.02590.
181. Vaswani,A.;Shazeer,N.;Parmar,N.;Uszkoreit,J.;Jones,L.;Gomez,A.N.;Kaiser,Ł.;Polosukhin,I. Attentionisallyouneed.
Adv.NeuralInf.Process.Syst.2017,30.
182. Zhou,H.;Zhang,S.;Peng,J.;Zhang,S.;Li,J.;Xiong,H.;Zhang,W. Informer:Beyondefficienttransformerforlongsequence
timeseriesforecasting. InProceedingsoftheAAAIConferenceonArtificialIntelligence,Virtual,2–9February2021;Volume35,
pp.11106–11115.
183. Wu,H.;Xu,J.;Wang,J.;Long,M. Autoformer:Decompositiontransformerswithauto-correlationforlong-termseriesforecasting.
Adv.NeuralInf.Process.Syst.2021,34,22419–22430.
184. Zhou,T.;Ma,Z.;Wen,Q.;Wang,X.;Sun,L.;Jin,R. Fedformer: Frequencyenhanceddecomposedtransformerforlong-term
seriesforecasting. InProceedingsoftheInternationalConferenceonMachineLearning,Baltimore,MD,USA,17–23July2022;
pp.27268–27286.
185. He,K.;Zhang,X.;Ren,S.;Sun,J. Deepresiduallearningforimagerecognition. InProceedingsoftheIEEEConferenceon
ComputerVisionandPatternRecognition,LasVegas,NV,USA,26June–1July2016;pp.770–778.
186. Ba,J.L.;Kiros,J.R.;Hinton,G.E. Layernormalization. arXiv2016,arXiv:1607.06450.
187. Luong,T.;Pham,H.;Manning,C.D. EffectiveApproachestoAttention-basedNeuralMachineTranslation. InProceedingsofthe
2015ConferenceonEmpiricalMethodsinNaturalLanguageProcessing,Lisbon,Portugal,17–21September2015;Associationfor
ComputationalLinguistics:Cedarville,OH,USA,2015;pp.1412–1421.
188. Li,S.;Jin,X.;Xuan,Y.;Zhou,X.;Chen,W.;Wang,Y.X.;Yan,X. Enhancingthelocalityandbreakingthememorybottleneckof
transformerontimeseriesforecasting. Adv.NeuralInf.Process.Syst.2019,32.
189. Wang,S.;Li,B.Z.;Khabsa,M.;Fang,H.;Ma,H. Linformer:Self-attentionwithlinearcomplexity. arXiv2020,arXiv:2006.04768.
190. Donoho,D.L. Compressedsensing. IEEETrans.Inf.Theory2006,52,1289–1306.[CrossRef]
191. Nie,Y.; Nguyen,N.H.;Sinthong,P.;Kalagnanam,J. ATimeSeriesisWorth64Words:Long-termForecastingwithTransformers.
InProceedingsoftheInternationalConferenceonLearningRepresentations,Kigali,Rwanda,1–5May2023.
192. Zhang,Y.;Yan,J. Crossformer:Transformerutilisingcross-dimensiondependencyformultivariatetimeseriesforecasting. In
ProceedingsoftheEleventhInternationalConferenceonLearningRepresentations,Kigali,Rwanda,1–5May2022.
193. Liu,S.;Yu,H.;Liao,C.;Li,J.;Lin,W.;Liu,A.X.;Dustdar,S. Pyraformer:Low-ComplexityPyramidalAttentionforLong-Range
TimeSeriesModelingandForecasting. InProceedingsoftheInternationalConferenceonLearningRepresentations,Virtual,
25–29April2022.
194. Shabani, M.A.; Abdi, A.H.; Meng, L.; Sylvain, T. Scaleformer: Iterative Multi-scale Refining Transformers for Time Series
Forecasting. InProceedingsoftheTheEleventhInternationalConferenceonLearningRepresentations,Kigali,Rwanda,1–5
May2023.
195. Cirstea,R.G.;Guo,C.;Yang,B.;Kieu,T.;Dong,X.;Pan,S. Triformer:Triangular,Variable-SpecificAttentionsforLongSequence
MultivariateTimeSeriesForecasting–FullVersion. arXiv2022,arXiv:2204.13767.
196. Liu,Y.;Wu,H.;Wang,J.;Long,M. Non-stationarytransformers:Exploringthestationarityintimeseriesforecasting. Adv.Neural
Inf.Process.Syst.2022,35,9881–9893.
197. Schirmer, M.; Eltayeb, M.; Lessmann, S.; Rudolph, M. Modelingirregulartimeserieswithcontinuousrecurrentunits. In
ProceedingsoftheInternationalConferenceonMachineLearning,Baltimore,MD,USA,17–23July2022;pp.19388–19405.
198. Zhou,T.;Ma,Z.;Wen,Q.;Sun,L.;Yao,T.;Yin,W.;Jin,R. Film:Frequencyimprovedlegendrememorymodelforlong-termtime
seriesforecasting. Adv.NeuralInf.Process.Syst.2022,35,12677–12690.
199. Ekambaram,V.;Jati,A.;Nguyen,N.;Sinthong,P.;Kalagnanam,J. TSMixer:LightweightMLP-MixerModelforMultivariateTime
SeriesForecasting. InProceedingsofthe29thACMSIGKDDConferenceonKnowledgeDiscoveryandDataMining,LongBeach,
CA,USA,6–10August2023;pp.459–469.
200. Wang,H.;Peng,J.;Huang,F.;Wang,J.;Chen,J.;Xiao,Y. MICN:Multi-scaleLocalandGlobalContextModelingforLong-term
SeriesForecasting. InProceedingsoftheEleventhInternationalConferenceonLearningRepresentations,Kigali,Rwanda,1–5
May2023.
201. Mackey,M.C.;Glass,L. Oscillationandchaosinphysiologicalcontrolsystems. Science1977,197,287–289.[CrossRef][PubMed]
202. Weiss,C.O.;Hübner,U.;Abraham,N.B.;Tang,D. Lorenz-likechaosinNH3-FIRlasers. InfraredPhys.Technol.1995,36,489–512.
[CrossRef]
203. Aguirre,L.A.;Rodrigues,G.G.;Mendes,E.M. Nonlinearidentificationandclusteranalysisofchaoticattractorsfromareal
implementationofChua’scircuit. Int.J.Bifurc.Chaos1997,7,1411–1423.[CrossRef]
204. Wijngaard,J.;KleinTank,A.;Können,G. Homogeneityof20thcenturyEuropeandailytemperatureandprecipitationseries. Int.
J.Climatol.J.R.Meteorol.Soc.2003,23,679–692.[CrossRef]
205. Weigend,A.S.;Gershenfeld,N.A.TimeSeriesPrediction:ForecastingtheFutureandUnderstandingthePast;SantaFeInstituteStudies
intheSciencesofComplexity:SantaFe,NM,USA,1994.
206. Jospin,L.V.;Laga,H.;Boussaid,F.;Buntine,W.;Bennamoun,M. Hands-onBayesianneuralnetworks—Atutorialfordeep
learningusers. IEEEComput.Intell.Mag.2022,17,29–48.[CrossRef]
207. Lu,J.;Liu,A.;Dong,F.;Gu,F.;Gama,J.;Zhang,G. Learningunderconceptdrift:Areview. IEEETrans.Knowl.DataEng.2018,
31,2346–2363.[CrossRef]

Information2023,14,598 35of35
208. Hyvärinen,A.;Dayan,P. Estimationofnon-normalizedstatisticalmodelsbyscorematching. J.Mach.Learn.Res.2005,6.
209. Vincent,P. Aconnectionbetweenscorematchinganddenoisingautoencoders. NeuralComput.2011,23,1661–1674.[CrossRef]
[PubMed]
210. Song,Y.;Garg,S.;Shi,J.;Ermon,S. Slicedscorematching:Ascalableapproachtodensityandscoreestimation. InProceedingsof
theUncertaintyinArtificialIntelligence,Virtual,3–6August2020;pp.574–584.
211. Anderson,B.D. Reverse-timediffusionequationmodels. Stoch.Process.TheirAppl.1982,12,313–326.[CrossRef]
212. Papoulis,A.;UnnikrishnaPillai,S. Probability,RandomVariablesandStochasticProcesses;McGraw-Hill:NewYork,NY,USA,2002.
Disclaimer/Publisher’s Note: The statements, opinions and data contained in all publications are solely those of the individual
author(s)andcontributor(s)andnotofMDPIand/ortheeditor(s).MDPIand/ortheeditor(s)disclaimresponsibilityforanyinjuryto
peopleorpropertyresultingfromanyideas,methods,instructionsorproductsreferredtointhecontent.