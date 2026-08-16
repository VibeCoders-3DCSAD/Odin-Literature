---
conversion_metadata:
  converted_at: "2026-07-21T09:25:47Z"
  converter_tool: "markitdown"
  converter_version: "0.1.6"
  source_pdf: "Xiang et al.pdf"
  source_pdf_sha256: "22934b538ffd695a24b36136b11c897ebb90c3601b90a91537502b163e8aa541"
  page_count: 27
  markdown_char_count: 220169
---

<!-- PAGE-AWARE EXTRACTION (via pdfminer.six) -->

<!-- PAGE 1 -->

Review
Concept Drift Adaptation Methods under the Deep Learning
Framework: A Literature Review

Qiuyan Xiang

, Lingling Zi *, Xin Cong and Yan Wang

College of Computer and Information Science, Chongqing Normal University, Chongqing 401331, China
* Correspondence: lingling19812004@126.com

Abstract: With the advent of the fourth industrial revolution, data-driven decision making has also
become an integral part of decision making. At the same time, deep learning is one of the core
technologies of the fourth industrial revolution that have become vital in decision making. However,
in the era of epidemics and big data, the volume of data has increased dramatically while the sources
have become progressively more complex, making data distribution highly susceptible to change.
These situations can easily lead to concept drift, which directly affects the effectiveness of prediction
models. How to cope with such complex situations and make timely and accurate decisions from
multiple perspectives is a challenging research issue. To address this challenge, we summarize
concept drift adaptation methods under the deep learning framework, which is beneﬁcial to help
decision makers make better decisions and analyze the causes of concept drift. First, we provide an
overall introduction to concept drift, including the deﬁnition, causes, types, and process of concept
drift adaptation methods under the deep learning framework. Second, we summarize concept drift
adaptation methods in terms of discriminative learning, generative learning, hybrid learning, and
others. For each aspect, we elaborate on the update modes, detection modes, and adaptation drift
types of concept drift adaptation methods. In addition, we brieﬂy describe the characteristics and
application ﬁelds of deep learning algorithms using concept drift adaptation methods. Finally, we
summarize common datasets and evaluation metrics and present future directions.

Keywords: deep learning;
time-series analysis; concept drift; data-driven decision making;
discriminative learning; generative learning; hybrid learning; deep reinforcement learning; deep
transfer learning

1. Introduction

The 2019 outbreak of coronavirus disease (COVID-19) has distinct effects on people’s
health and quality of life, and there is great uncertainty regarding the outbreak’s evolution,
duration, and scope in the future. So, in this era of the epidemic and big data, decision
makers face a series of problems, such as extensive databases, rapid growth, diversiﬁed
data sources, and rapid changes in data distribution. At present, deep learning technologies
can solve part of the problems and provide part of the guidance to decision makers [1].
However, it does not adapt well to the changing environment. Once the environment
changes, the new data does not match the distribution of the old data. With concept drift
occurring [2], the deep learning model will become obsolete and invalid. How to deal with
this complex situation and make timely and accurate decisions from multiple perspectives
is a challenging research problem. Concept drift adaptation methods offer the possibility of
solving the problem [3], helping decision makers to ﬁnd the optimal or most satisfactory
solution in this dynamic and complex situation. These methods can continuously capture
the potential danger of events by analyzing the data stream, deal with distribution changes
in the data stream on time, and help decision makers update existing decision results to
prevent losses due to decision making.

Citation: Xiang, Q.; Zi, L.; Cong, X.;

Wang, Y. Concept Drift Adaptation

Methods under the Deep Learning

Framework: A Literature Review.

Appl. Sci. 2023, 13, 6515. https://

doi.org/10.3390/app13116515

Academic Editors: Paolo Renna,

Asad Masood Khattak, Rahman Ali

and Farkhund Iqbal

Received: 23 February 2023

Revised: 29 April 2023

Accepted: 24 May 2023

Published: 26 May 2023

Copyright: © 2023 by the authors.

Licensee MDPI, Basel, Switzerland.

This article is an open access article

distributed under

the terms and

conditions of the Creative Commons

Attribution (CC BY) license (https://

creativecommons.org/licenses/by/

4.0/).

Appl. Sci. 2023, 13, 6515. https://doi.org/10.3390/app13116515

https://www.mdpi.com/journal/applsci

---

<!-- PAGE 2 -->

Appl. Sci. 2023, 13, 6515

2 of 27

Concept drift adaptation methods can be applied in various ﬁelds. By continuously
upgrading the learning model to ensure its correctness and timeliness, they can provide
accurate prediction information for decision makers. At the same time, they can perform
active detection in combination with detection algorithms, which provides decision makers
with knowledge of dynamic concepts [4], and analyze the concept drift that is occurring. For
example, in the information security ﬁeld, improved long short-term memory (I-LSTM) [5]
can effectively detect network anomalies, analyze the causes, and strengthen protection.
In the ﬁnancial investment ﬁeld, DeepBreath [6] can effectively minimize investment risk,
and it has been experimentally proven to obtain better investment returns than current
expert investment strategies. In addition, in the ﬁeld of customer behavior analysis and air
quality detection, ConceptExplorer [7], which combined concept drift with visualization,
can help decision makers to conduct intuitive exploration and provide a basis for experts
to make subsequent decisions. Therefore, concept drift adaptation methods can effectively
help decision makers determine the main inﬂuencing factors, update their understanding
of potential relationships, understand the nature of the data, ﬁnd potential dangers, and
make correct decisions.

Due to the important role of concept drift adaptation methods in applications, many
researchers have reviewed them from different perspectives. For example, within nearly
10 years, Hoens et al. [8] reviewed concept drift detection methods and summarized the
problem of class imbalance in the data stream. YM et al. [9] reviewed the classiﬁcation prob-
lem from the perspective of a single model and an ensemble model. Gama et al. [4] reviewed
concept drift adaption methods from four aspects: memory usage, concept drift detection,
model update method, and model evaluation index. Dtizler et al. [10] reviewed the ex-
isting concept drift detection methods from two aspects: active mode and passive mode.
Webb et al. [11] mainly involved various types, such as drift target, drift transition mode,
and drift amount, and explained their speciﬁc deﬁnitions. Krawczyk et al. [12] reviewed
ensemble learning in data stream classiﬁcation and regression tasks. Kamassi et al. [13]
summarized concept drift adaption methods from the aspects of data processing, adap-
tation mode, and the number of classiﬁers. Lu et al. [14] comprehensively summarized
when drift occurs, to what extent, and how long it lasts, as well as the category imbal-
ance in the classiﬁcation of concept drift data streams, big data mining, and data-driven
decision support systems. Ghani et al. [15] mainly introduced conceptual drift detection
methods for untagged data streams. Lima et al. [16] summarized and classiﬁed concept
drift adaptation methods based on different machine learning models under the regression
task. Bayram et al. [17] classiﬁed and reviewed the existing detection algorithms of concept
drift adaptation methods. However, to the best of our knowledge, there is no detailed
introduction and summary of concept drift adaptation methods under the deep learning
framework. Therefore, this paper explores the important role of concept drift adaptation
methods under the deep learning framework.

The main contributions of this paper can be summarized as follows:

(1) We review concept drift adaptation methods under the deep learning framework
from four aspects—discriminative learning, generative learning, hybrid learning, and
relevant others—so as to ﬁll the gap in this area of investigation in previous work.

(2) We reveal the general operation process of concept drift adaptive methods under deep
learning frameworks and explain concept drift detection modes and update modes
in detail.

(3) We summarize the representative algorithms of each subcategory, common datasets,

evaluation metrics, their application areas, and limitations.

(4) We analyze and discuss the current problems of concept drift adaption methods and

point out the future direction.

The rest of the paper is structured as follows. Section 2 provides the deﬁnition, causes,
and types of concept drift and introduces the process of concept drift adaptation methods
under the deep learning framework. Section 3 classiﬁes concept drift adaptation methods
based on deep learning and reviews the existing methods in the literature. Section 4

---

<!-- PAGE 3 -->

Appl. Sci. 2023, 13, 6515

3 of 27

summarizes the common datasets and evaluation metrics. Section 5 provides future
research, and Section 6 concludes this paper.

2. Overview of Concept Drift

In this section, we introduce the deﬁnition and causes of concept drift, different types
of concept drift, and the process of concept drift adaptation methods. Concept drift was ﬁrst
proposed by Schlemmer et al. [2] in 1986 and mainly refers to the fact that the underlying
data stream distribution changes over time [18,19].

2.1. The Deﬁnition of Concept Drift

Assuming that Pt0 represents the joint probability distribution between the input
variable x and the target variable y at time t0 and Pt1 represents the joint probability
distribution between the x and y at t1, then concept drift will occur if Equation (1) holds
when t0 turns to t1.

∃x : Pt0 (x, y) (cid:54)= Pt1 (x, y)

(1)

At this time, the underlying data distribution no longer conforms to concept C1, and a new
concept C2 is generated. Due to the characteristics of joint probability Pt(x, y) = Pt( x)Pt(y|x)
if Equation (2) is satisfied when t0 turns to t1, concept drift will also occur.

∃x : Pt0 (x)Pt0 (y|x) (cid:54)= Pt1 (x)Pt1 (y|x)

(2)

Changes in both Pt(x) and Pt(y|x) can lead to concept drift.

2.2. The Causes of Concept Drift

According to the deﬁnition of concept drift and the characteristics of joint probability,

it can have the following three causes:

(1) Virtual concept drift. When the probability of x changes, but the probability of y under
the condition of x does not change, i.e., Pt0 (x) (cid:54)= Pt1 (x) and Pt0(y|x) = Pt1 (y|x). This
case belongs to virtual concept drift, which does not affect its decision boundary and
only changes the feature space.

(2) Real concept drift. When the probability of y under the condition of x changes, the
probability of x remains the same, i.e., Pt0 (y|x) (cid:54)= Pt1 (y|x) and Pt0 (x) = Pt1 (x). This
case has a direct impact on the prediction model and is a real concept drift, which not
only changes the feature space but also changes its decision-making boundary.
(3) Hybrid concept drift. In an open environment, both real concept drift and virtual
concept drift can exist in the data stream at the same time, i.e., Pt0 (x) (cid:54)= Pt1 (x),
Pt0 (y|x) (cid:54)= Pt1 (y|x). This is a mixed concept drift, which is most common.
It is worth noting that according to the Bayesian decision theory [20], we obtain

Equation (3):

P(y|x) =

P(y) ∗ P(x|y)
P(x)

(3)

It can be seen that Pt(y) and Pt(x|y) also affect Pt(y|x), thus indirectly causing a real
concept drift. The speciﬁc manifestations of the concept drift due to different causes are
shown in Figure 1, in which (X1, X2) represents the two-digit feature space and y represents
its category label.

For example, in stock trading, users can be divided into proﬁtable and non-proﬁt
stocks according to proﬁtability. When a user considers purchasing stocks, a change in
the channel of purchase or a small change in the number of purchases does not affect the
trend of the stock. However, if affected by an outbreak, the trend of stocks may change,
thus directly affecting stock returns. This situation belongs to the real concept drift, so
users need to reconsider and make decisions. In real life, virtual drift tends to have less
impact on the outcome of a decision. There will be no loss to decision makers. However,
real concept drift tends to have a direct impact on decision outcomes due to changes in its

---

<!-- PAGE 4 -->

Appl. Sci. 2023, 13, 6515

4 of 27

data relationships. It requires decision makers to discover in time and re-make decisions to
avoid losses.

Figure 1. The causes of concept drift.

2.3. The Types of Concept Drift

The changes in concept may manifest in different forms over time. At present, the
most popular types of concept drift can be divided into abrupt drift, incremental drift,
gradual drift, and recurring drift [14,16,17].

Abrupt drift refers to the rapid change of concept C1 into concept C2 in a short period
of time, and if an earthquake suddenly occurs in a certain place, its economic model changes
instantaneously, as shown in Figure 2a. Incremental drift refers to the slow transformation
of concept C1 into concept C2 in a continuous manner, as the economy gradually recovers
after an earthquake, as shown in Figure 2b. Gradual drift refers to a short period of time: C1
and C2 repeatedly switch and eventually stabilize at C2, as the equipment ages, occasionally
fails, and ﬁnally stops working, as shown in Figure 2c. Recurring drift refers to the fact that
over time, the previous concept will reappear after a period of time; for example, the sales
of down jackets meet concept C1 in the winter, start to enter the off-season after the end
of the winter, their sales will meet concept C2, and then the next winter concept C1 will
reappear, as shown in Figure 2d. In addition, the speed of recurring drift can be abrupt,
gradual, or incremental. It can also be periodic or irregular.

Figure 2. The types of concept drift.

In the academic research of concept drift, the types are different according to the
classiﬁcation criteria. However, it is common to divide the types of concepts according to
their transformations, and this criteria manifestation is more intuitive. In related studies,
different methods adapt to solving different types of concept drift. For example, the drift
detection method (DDM) algorithm [21] is more suitable for abrupt drift. In addition
to adapting the four common types above, there are some methods for distinguishing
real drift and virtual drift, avoiding mixing with virtual concept drift or outliers and
noise. For example, the RRBM–DD [22] considers explicitly how to identify the drift of
the real concept. Although concept drift adaptation methods cannot solve all types of
concept drift at one time, they can still solve multiple concept drifts, which belongs to a
one-to-many relationship.

In recent years, there have also been many excellent concept drift detection algo-
rithms to detect multiple concept drifts, for example, based on sliding-window algorithms,
OCDD [23], CDT_MSW [24], and KSWIN [25]. OCDD mainly has two sliding windows

---

<!-- PAGE 5 -->

Appl. Sci. 2023, 13, 6515

5 of 27

to store new and old data, and the percentage of outliers detected by the classiﬁer in the
sliding window is used to send a drift signal, which is more suitable for detecting abrupt
and incremental drift, but hyperparameter settings are required. CDT_MSW also has two
windows, the difference being that it can identify the position and length of concept drift, so
as to accurately determine the type of concept drift. KSWIN detects concept drift by apply-
ing the “Kolmogorov–Smirnov test”. These algorithms are based on supervised learning.
Unsupervised concept drift algorithms include LD3 [26], STUDD [27], and CDCMS [28].
LD3 introduces the concept of label-dependent ordering for concept drift detection in multi-
label classiﬁcation, which is more suitable for mutation and incremental drift. STUDD
mainly creates an auxiliary model (students) to mimic the behavior of the main model
(teacher), uses the teacher to predict new instances, and monitors the student’s imitation
loss to detect concept drift. It is more suitable for abrupt, gradual, and incremental drift.
CDCMS mainly uses novel clustering and diversity-based memory management strate-
gies in model space strategies to deal with concept drift and has good effects in dealing
with abrupt and recurring drift. Finally, it is worth mentioning that most of the concept
drift detection algorithms either occupy more memory or have a slow detection speed.
DMDDM [29] is based on the Page–Hinkley test, which effectively improves the detection
speed of concept drift and overcomes the limitations of cost and execution time but is only
suitable for abrupt drift. How to achieve a cost-saving detection algorithm that covers
all drift types is also a major challenge. Therefore, we will also summarize the types of
conceptual drift for each method.

2.4. The Process of Concept Drift Adaptation Methods under Deep Learning Framework

The general adaptation process of concept drift under the deep learning framework
when dealing with unstable state data streams is shown in Figure 3. First, the data stream
input (single input or batch input) is generally trained and learned by the deep learning
model (single model or ensemble model) to obtain the basic prediction results. Next,
if concept drift occurs during this process, a concept drift adaptation method will be
triggered to update the deep learning model to accommodate concept drift and maintain
the model [16,19]. The concept drift adaptation method can be divided into two parts:
concept drift detection and model update. Among them, concept drift detection contains
both active and passive modes, and model updates can be divided into structure updates
and parameter updates.

Figure 3. The general process of concept drift adaptation methods under deep learning framework.

---

<!-- PAGE 6 -->

Appl. Sci. 2023, 13, 6515

6 of 27

Active modes mean that the learning process of a deep learning model contains a con-
cept drift detection algorithm. When concept drift is detected, the concept drift adaptation
method will be triggered to update the model. Passive mode means that the method contin-
uously adjusts its model as data are continuously input during the learning process. Instead
of using a drift detection algorithm, it uses a concept drift adaptation method to passively
update the model continuously. After triggering the concept drift application mechanism,
the deep learning model is generally updated to adapt to the concept drift through a model
parameter update or a structure update [30]. Model parameter updates can be divided into
full parameter updates and partial parameter updates. In particular, parameter updates
also include parameter updates between ensemble models. Here, parameter updates are
also weight updates. In addition, model structure updates can generally be performed by
adjusting the width and depth of the network.

3. Concept Drift Adaptation Methods under Deep Learning

In this section, we will summarize concept drift adaptation methods according to the
classiﬁcation of deep learning [31], including discriminative learning, generative learning,
hybrid learning, and others, as shown in Figure 4. For each part, we will explain the update
modes, types of drift adapted, and detection modes. In addition, we will also introduce
the characteristics and application ﬁelds of deep learning techniques using concept drift
adaptation methods.

Figure 4. A taxonomy of concept drift adaption under deep learning framework.

3.1. Concept Drift Adaptation Methods Based on Discriminant Learning

This type of deep learning technique is used in supervised or classiﬁcation applications
by describing the posterior distributions of conditioned visible data. A discriminative

---

<!-- PAGE 7 -->

Appl. Sci. 2023, 13, 6515

7 of 27

model is a model that learns the relationship between input data and output labels, and
it predicts output labels by learning the characteristics of the input data. In classiﬁcation
problems, the main purpose is to assign each input vector a to label b. Discriminant models
attempt to directly learn the function f (a) that maps input vectors to labels. The classiﬁer
ﬁrst learns the posterior class probability P(b = k|a) from the training data and assigns a
new sample a to the class with the highest posterior probability based on these probabilities,
where k stands for class. The general process of the discriminant concept drift adaption
method is shown in Figure 5, while the two methods of active detection and parameter
update mode account for a relatively large proportion. Discriminant learning mainly
includes multilayer perceptrons (MLPs), convolutional neural networks (CNNs), recurrent
neural networks (RNNs), and their variants.

Figure 5. The general process of concept drift adaptation methods based on discriminant learning.

• MLP-based concept drift adaptation methods

MLP is a discriminant learning model widely adopted in decision making [32], which
is often used in combination with concept drift adaptation methods to solve classiﬁcation
problems for unstable streaming data. However, concept drift adaptation methods are
computationally expensive and converge slowly each time the model is updated due to
the hyperparameter problem. Typical algorithms, such as selective ensemble-based online
adaptive deep neural networks (SEOAs), bilevel online deep learning (BODL), neural
networks with dynamically evolved capacity (NADINEs), and Adadelta optimizer-based
deep neural networks with concept drift detection (CIDD-ADODNNs), are elaborated
as follows.

SEOA [33] uses a deep learning model with L network layer MLPs to form L basic
classiﬁers. It then dynamically adjusts the parameters of each basic classiﬁer to handle
concept drift and regularly selects base classiﬁers with different convergence and ﬁtting
abilities.
It enhances the adaptability and generalization ability of the model to data
distribution, which is more suitable for gradual, incremental, and recurring drift, although
less suitable for dealing with high-dimensional non-linear problems. BODL [34] mainly
uses the MLP model for classiﬁcation prediction and detects concept drift based on the
classiﬁer’s error rate. When concept drift is detected, the model’s parameters are updated
through a bilevel optimization strategy and the exponential gradient descent method to
adapt to the abrupt concept drift, but its limitation is that the added classes cannot be
identiﬁed online. In contrast, the convergence speed of the algorithm for model structure
update can be slower. NADINE [35] uses a drift detection mechanism to detect concept
drift actively. The drift detection mechanism mainly adds an adaptive windowing strategy
to the prominent Hoeffding’s bound detection algorithm. When the drift signal is detected,
its network structure will be updated to adapt to concept drift, which mainly adjusts its
network structure through the hidden unit growing strategy and hidden unit pruning
strategy. The main advantage of NADINE over other algorithms is its elastic structure
and online learning trait, but the training time of the model is relatively slow. It can be
applied to classiﬁcation and regression problems. Additionally, scholars have researched
it for certain special data. CIDD-ADODNN [36] is adopted for the classiﬁcation model of
highly unbalanced data ﬂow, which mainly uses an adaptive sliding window (ADWIN)
drift detection algorithm to actively detect concept drift and then updates the network

---

<!-- PAGE 8 -->

Appl. Sci. 2023, 13, 6515

8 of 27

parameters through the Adadelta optimizer, so as to adapt to the abrupt and gradual drift.
This algorithm effectively improves the classiﬁcation performance of highly unbalanced
data streams, although its feature selection needs to be optimized.

•

RNN-based concept drift adaptation methods

Compared to other neural networks, RNN has certain advantages in processing
sequence data because it has at least one feedback connection [37]. To some extent, it can
alleviate the problem of concept drift. However, its capacity is also limited, especially when
it comes to processing long data. It is mainly used in the ﬁelds of electricity loading, weather
forecasting, and anomaly detection. Typical algorithms are the online adaptive recurrent
neural network (OARNN), ONU-SHO-based RNN (ONU-SHO-RNN), adaptive behavioral-
based incremental batch learning malware variant detection model (AIBL-MVD), and
multilayer self-evolving recurrent neural network (MUSE-RNN).

OARNN [38] mainly uses the RNN model to capture the temporal correlation and track
its performance. When the performance deteriorates, the tree-structured Parzen estimator
(TPE) will be used to optimize the hyperparameters of the model online. Then, the weights
of the RNN model are completely updated and relearned from new data to accommodate
concept drift over short periods of time. It is mainly used for energy and electricity load
forecasting, although it requires a large amount of data for training and learning. In
addition, Jagait et al. [39] proposed an online ARIMA-RNN integration based on OARNN,
which belongs to hybrid learning. It will be further introduced later. ONU-SHO-RNN [40]
determines whether to update the model by calculating its prediction accuracy and the
concept drift detection of the RNN model on the data stream. It mainly uses the ONU-SHO
algorithm to perform a complete parameter update and narrow the error between the
target output and the measurement output. It is capable of fast convergence, adapting
to incremental and gradual drift, although there are problems with update delays. In
addition, AIBL-MVD [41] also adapts to incremental and gradual drift. It mainly uses the
statistical process control (SPC) algorithm to actively detect the occurrence of concept drift
and update all model weights through incremental learning. It is mainly used in the ﬁeld
of malware detection. In this process, the catastrophic forgetting problem is solved by
mixing the new data with a subset of the old data. Its limitation is that labeled malware
samples must be available right before updating the model. All of the above methods are
based on parameter update mode. Subsequently, MUSE-RNN [42] mainly uses structural
updates to update the models, and it actively detects concept drift through Hoeffding’s
bound detection algorithm, which is also a common method in concept drift detection
algorithms. The model is updated by using growth and pruning hidden nodes and layers
for the real-time classiﬁcation of data streams, although it does not handle image streams.

•

LSTM-based concept drift adaptation methods

Long short-term memory (LSTM) is a variant of RNN that solves problems such as
vanishing gradients and is suitable for processing and forecasting important events with
relatively long intervals and delays in time series [43]. LSTM-based concept drift adaptation
methods are mainly used in the ﬁelds of anomaly detection, photovoltaic power generation
prediction, and industrial prediction, and their typical algorithms include DL-CIBuild,
I-LSTM, multi-objective metaheuristic optimization-based big data analytics with concept
drift detection (MOMBD-CDD), adaptive LSTM (AD-LSTM), DCA-DNN, etc.

DL-CIBuild [44] is an algorithm based on the LSTM model to construct prediction
models for continuous integration (CI) build outcome prediction.
It uses the genetic
algorithm (GA) to adjust the hyperparameters (including the number of hidden layers and
neurons) of the LSTM model. In particular, it does not require a very large dataset size and
has good robustness. However, the algorithm is relatively expensive in terms of labor and
requires the construction of annotated datasets. I-LSTM [5] combines the idea of time factor
with stratiﬁed sampling. Therefore, the newer the data, the higher the weight assigned to
accommodate concept drift, but there are also problems with balancing old and new data.
Overall, it improves multi-classiﬁcation performance for anomaly detection, mainly for

---

<!-- PAGE 9 -->

Appl. Sci. 2023, 13, 6515

9 of 27

IoT applications. MOMBD-CDD [45] mainly deals with high-dimensional streaming data.
It mainly uses the Statistical Test of Equal Proportions method (STEPD) to detect concept
drift and combines the glowworm swarm optimization (GSO) algorithm to update the
bidirectional long short-term memory (Bi-LSTM) model by adjusting weights. However, it
is more computationally intensive and takes up more resources. In this process, STEPD
deﬁnes two windows, a recent window r and an overall window o. This is also common
in deep-learning-based concept drift adaptation methods. It applies the statistical test
of equal proportions to compare the accuracies between the two windows as shown in
Equations (4) and (5):

T(vo, vr, no, nr) =

|vo/no − vr/nr|−0.5 × (1/no + 1/nr)
µ + (1 − µ) × (1/no + 1/nr)

(cid:112)

µ = (v0 + vr)/(no + nr)

(4)

(5)

Its value is compared to the percentile of the standard normal distribution to obtain
the observed signiﬁcance level (p-value). p-value is equivalent to the chi-square test
with Yates’s continuity correction, in which v is the value of accurate predictions, and
n is the number of samples for the window. The calculation formula for µ is shown in
Equation (5). If p-value < αd, STEPD predicts a concept drift. If p-value < αw, STEPD
predicts a warning that concept drift may occur. αd is the concept drift signiﬁcance level;
αw is the warning signiﬁcance level. Fog-DeepStream [46] uses wavelet transform to
reduce the dimensionality of the data and LSTM models to predict future behavior for
data stream analysis on fog computing. It uses a drift detection algorithm to determine
the occurrence of conceptual drift, and when a conceptual drift is detected, parameters
are updated to accommodate the conceptual drift. The method tries three drift detection
algorithms: cumulative sum (CUSUM), Page–Hinkley, and exponentially weighted moving
average (EWMA). However, this algorithm also takes up a lot of memory.

The above algorithms are used in the Internet ﬁeld. Next, we introduce algorithms
in other ﬁelds. For example, AD-LSTM [47] is used for predicting photovoltaic power
generation. It actively detects the occurrence of concept drift through the sliding window
(SDWIN) algorithm and adopts the second stage of the two-phase adaptive learning strategy
(TP-ALS) to ﬁne-tune the prediction model. DCA-DNN [48] is mainly used for industrial
prognosis and is based on the LSTM-FC model, which actively detects the occurrence
of concept drift through the dendritic cell algorithm. It generates synthetic data using a
kernel density estimator with drift-based bandwidth, which can be used to ﬁne-tune the
weights of the last layer to achieve faster adaptation and mitigate the problem of limited
new samples. Both of the above algorithms suffer from model update delays, and their
concept drift detection algorithms need to be optimized.

•

CNN-based concept drift adaptation methods

CNN is a feed-forward neural network in which the connections between neurons in
its convolutional layer are not fully connected, and the weights and biases of connections
between some neurons in the same layer are shared [49,50]. So, the computational cost
of this concept drift adaptation method is also relatively low. Typical algorithms, such
as the evaluative convolutional neural network (ECNN) [51], mainly use re-weighting
operation technology to dynamically update the model, so as to solve the concept drift
problem in high-throughput data. ECNN overcame the “over-ﬁtting” and “under-ﬁtting”
problems. ECNN is the ﬁrst online deep learning technique to be introduced into marine
data prediction research, although it is relatively computationally expensive. Online CNN-
based model selection using performance gradient-based saliency maps (OS-PGSM) [52] is
mainly applied to time-series prediction and uses Hoeffding’s bound detection algorithm
to actively detect the occurrence of concept drift. When concept drift occurs, the region of
competence (ROC) of the model will be recalculated to update the weights. It has a low
computational cost, using signiﬁcance plots to provide an explanation for model selection,

---

<!-- PAGE 10 -->

Appl. Sci. 2023, 13, 6515

10 of 27

but hyperparameter settings need to be optimized. Deep incremental hashing (DIH) [53]
focuses on semantic image retrieval using a CNN model. The parameters of the CNN are
updated using a point-by-point loss function guided by the similarity of the current data
block keeping the target code. DIH mainly adapts to gradual, incremental drift. It also has
certain limitations, such as not considering the semantic relationships between labels.

Table 1 summarizes the discriminant-learning-based concept drift adaptation methods.
From this table, it can be seen that the MLP-based concept drift adaptation method focuses
on the processing of streaming data samples to ensure the balance between old and new
data and imbalanced data, thus improving the accuracy of prediction and reducing errors.
However, it has certain limitations in dealing with high dimensionality, which is more
suitable for dealing with gradual and abrupt concept drift. The RNN-based algorithm
and its variants have good timeliness and can handle long-term serial data. However, it
is necessary to overcome the problem of catastrophic forgetting, which is more sensitive
to incremental and gradual concept drift. It is worth noting that the types of concept drift
adaptation are rarely clearly speciﬁed in related studies based on LSTM and CNN. Further,
most concept drift adaptation methods face the problem of slow convergence speed.

Table 1. Concept drift adaptation methods based on discriminant learning.

Types of Deep
Learning

Algorithms

Concept Drift Adaptation Methods

Detection
Modes

Update Modes

Adaptation
Drift Types

Limitation

MLP

SEOA [33]

BODL [34]

NADINE [35]

CIDD-ADODNN [36]

OARNN [38]

RNN

ONU-SHO-RNN [40]

AIBL-MVD [41]

MUSE-RNN [42]

DL-CIBuild [44]

I-LSTM [5]

LSTM

MOMBD-CDD [45]

Fog-DeepStream [46]

AD-LSTM [47]

DCA-DNN [48]

ECNN [51]

OS-PGSM [52]

DIH [53]

CNN

−

+

+

+

−

+

+

+

−

−

+

+

+

+

−

+

−

SNN

OeSNN [54]

+ || −

√

√

×
√

√

√

√

×

×

√

√

√

√

√

√

√

√

×

A I G

A

A G R

A G

N

I G

I G

Not suitable for high-dimensional
non-linear problems

New classes cannot be identiﬁed online

Slow training time

Feature selection to be optimized

Requires large amounts of data to update
the model

Model update delay

Must have a marked malware sample
before updating model

A G R

Cannot handle image data streams

N

G

N

N

N

N

N

I G

G R

High labor cost and need to build
annotated datasets

Balance of old and new data

High resource cost

High memory consumption

Model update latency exists

High computational cost

Hyperparameter settings need to
be optimized

No consideration of semantic
relationships between labels

No consideration of a priori information
such as speed and severity of drift

Note: + represents active mode, − represents passive mode,
represents parameter update, × represents
structural update, “A” represents abrupt drift, “I” represents incremental drift, “G” represents gradual drift,
“R” represents recurring drift, and “N” means not mentioned in the reference.

√

In addition to the above types of mainstream algorithms, there are some other methods
of discriminant learning. For example, the OeSNN-DRT algorithm based on a spike
network [54] introduces two methods: active and passive adaptation methods. It uses the
data reduction technique (DRT), a selective and generative data reduction technique, to

---

<!-- PAGE 11 -->

Appl. Sci. 2023, 13, 6515

11 of 27

optimize the contents of the neuronal repository and update its structure. However, it
does not take into account a priori information such as the speed and severity of the drift.
Currently, there are few studies related to other types of concept drift adaptation methods
compared to mainstream deep learning models, so they are not listed. However, it is a
worthy direction for research.

3.2. Concept Drift Adaptation Methods Based on Generative Learning

Generative learning technologies are often used to describe higher-order correlation
attributes or features for pattern analysis or synthesis, as well as joint statistical distribu-
tions of visible data and their related classes [55]. Most generative learning is unsupervised
learning, but sometimes it can also be used for preprocessing in supervised learning, di-
mensionality reduction processing, etc. [56]. A generative model learns the data generation
process, learns the probability distribution of input data, and generates new samples of
data. More speciﬁcally, the generative model ﬁrst estimates the conditional density of the
classes P(a|b = k) and the prior class probability P(b = k) from the training data. They
tried to understand how the data for each classiﬁcation was generated. Bayes’ theorem is
then used to estimate the posterior class probability. Generative models can also learn the
joint distribution of inputs and labels P(a, b) and then normalize them to obtain posterior
probabilities P(b = k|a). The general process of the conceptual drift adaptive method
based on generative learning is shown in Figure 6, while the general parameter update
mode accounts for a large proportion, and the proportion of active detection and passive
adaptation is comparable. Common deep neural network technologies for unsupervised
or generative learning are generative adversarial networks (GANs), autoencoders (AEs),
restricted Boltzmann machines (RBMs), self-organizing mapping (SOM), and deep belief
networks (DBNs) and their variants.

Figure 6. The general process of concept drift adaptation methods based on generative learning.

•

AE-based concept drift adaptation methods

AE mainly consists of an encoder, a code, and a decoder [57]. It is combined with a con-
cept drift adaptation method, which is mainly used for the anomaly detection of some high-
dimensional data, such as the detection of the anomalous behavior of elderly people. Typical
algorithms include the adaptive framework for online deep anomaly detection (ARCUS),
unsupervised statistical concept drift detection (USCDD-AE), deep evolving denoising
autoencoder (DEVDAN), and memory-based streaming anomaly detection (MemStream).
ARCUS [58] contains concept-driven inference and drift-aware model pool updates,
where concept-driven inference focuses on evaluating the reliability of its models and
giving evaluation scores when given a new data point. When a concept drift occurs, its
evaluation score will drop to trigger a model pool update. Some models will then be
removed and retrained to adapt to the occurrence of concept drift. In this process, the
algorithm mainly uses the same structure of the AE model to form a model pool to perform
anomaly detection of the data ﬂow, which mainly has a large resource cost and cannot store
the current batch of data where concept drift may occur. USCDD-AE [59] uses variational
autoencoders to identify the anomalies of elderly people, which detects concept drift based

---

<!-- PAGE 12 -->

Appl. Sci. 2023, 13, 6515

12 of 27

on data from families and the activity probability plot of the Kullback–Leibler divergence,
as deﬁned below.

DKL(G (cid:107) Q) = ∑
z∈Z

G(z) log(

G(z)
Q(z)

)

(6)

where Z is the probability space, and G and Q are probability distributions deﬁned
over Z. Here G and Q are activity probability maps. Then, when concept drift occurs, the
encoder will be updated to adapt to concept drift by backpropagating the reconstruction
error. In this process, there are often difﬁculties with data collection and the possibility of
false positives.

DEVDAN [60] is an incremental learning method that primarily uses the network
signiﬁcance formula to evaluate the predictive power of the model. Once the value in the
capture formula rises, its hidden nodes are adjusted. USCDD-AE and DEVDAN are mainly
based on the active concept drift adaptation method but ignore mutation oblivion when
adding new layers. MemStream [61] is used for anomaly detection in multidimensional
data and concept drift. It ﬁrst uses a small portion of the training set and extracts features
using the denoising autoencoder. Then, when a new sample arrives, the anomaly score is
recalculated, and the weighting factor of AE is updated. If the anomaly score exceeds a
user-set threshold, the memory is updated in a ﬁrst in, ﬁrst out (FIFO) manner, and the
model is retrained to accommodate concept drift. This method effectively avoids noise
disturbances and retrains quickly but with high resource overheads.

•

GAN-based concept drift adaptation methods

GAN mainly consists of a generator and a discriminator. The former is used to create
new data with similar characteristics to the original data, and the latter is used to determine
the authenticity of the given data [62]. There are few examples of GAN combined with
concept drift adaptation methods compared to other deep learning techniques, such as the
distributed class-incremental learning method based on generative adversarial networks
(DCIGAN). DCIGAN [63] uses a GAN generator to store information about past data
and constantly updates GAN parameters with new data. Meanwhile, a generative fusion
method (GF), which integrates multi-node local generators into a new global generator, is
adopted. Particularly, a method for monitoring and evaluating GAN during continuous
learning is presented, which explains the concept drift [64]. Its main purpose is to solve
the problem of classifying data streams, but different hyperparameters need to be set in
different environments.

•

RBM-based concept drift adaptation methods

RBM is usually made up of visible and hidden nodes, each connected to every other
node, which facilitates the understanding of some irregular datasets. Moreover, it is sensi-
tive to the occurrence of concept drift because it is able to learn the probability distribution
of the input [65]. RBM-I [66] and RRBM–DD [22] are two typical concept drift detection
algorithms proposed by Korycki and Krawczyk, for multi-class imbalance and the presence
of adversarial attack data streams, respectively. They both use gradient descent to update
the weights in order to maintain the sensitivity of concept drift detection. RBM-IM is not
suitable for small data streams and is prone to overﬁtting. RBM-DD has limitations in
identifying adversarial concept drift in dynamic classes of unbalanced data streams. In
addition, the Gaussian restricted Boltzmann machine (GRBM) algorithm [67] primarily
uses the Kullback–Leibler divergence distance to determine whether a concept drift has oc-
curred, thus enabling the adaptive adjustment of the sliding window and the division of the
data stream. It reduces energy consumption and saves memory but only makes judgments
on data from a single source and does not adaptively divide heterogeneous data.

•

SOM-based concept drift adaptation methods

SOM is often applied to create low-dimensional (usually two-dimensional) representa-
tions of high-dimensional datasets, while maintaining the topology of the data [68]. The
main beneﬁt of using SOM is that it makes high-dimensional data easier to visualize and

---

<!-- PAGE 13 -->

Appl. Sci. 2023, 13, 6515

13 of 27

analyze for understanding patterns. As in the case of GAN, there are few examples of SOM
combined with concept drift adaptation methods. An online unsupervised incremental
method based on self-organizing maps (OUIM-SOM) [69] is used for multi-label stream clas-
siﬁcation in inﬁnite delay labeling scenarios. It adopts the online update of neuronal weight
vectors and dataset label cardinality to accommodate abrupt and incremental concept drifts.
However, its adaptive effect on conceptual drift is limited.

Table 2 summarizes the typical algorithms based on generative learning. Among
them, AE-based algorithms are mainly used for anomaly detection, and depending on
the characteristics of autoencoders, these algorithms use generally unsupervised or semi-
supervised learning, which can enhance the ﬂexibility of data ﬂow methods in utilizing
unlabeled samples. The remaining methods of combining generative learning models with
concept drift algorithms, especially the concept drift adaptation methods involved in the
deep belief network, have not been found, so they are not presented in this paper. However,
there are some other generative learning models involved. A self-organizing incremental
neural network (SOINN+) for unsupervised learning from noisy data streams [70] adapts
to concept drift by adding or removing nodes, creating or deleting edges, or combining
both. SOINN+ is robust to noise and is able to ﬁnd topological representations that are
consistent with the distribution of real data. It is worth noting that the Euclidean distance
used in the node similarity metric is not suitable for high-dimensional data.

Table 2. Concept drift adaptation methods based on generative learning.

Types of Deep
Learning

Algorithms

Concept Drift Adaptation Methods

Detection
Modes

Update Modes

Adaptation
Drift Types

Limitation

AE

ARCUS [58]

DEVDAN [60]

MemStream [61]

USCDD-AE [59]

GAN

DCIGAN [63]

RBM

RRBM–DD [22]

RBM–IM [66]

GRBM [67]

SOM

OUIM-SOM [69]

SOINN

SOINN+ [70]

−

+

−

+

−

+

+

+

−

−

√

×

√

√

√

√

√

√

√

×

A I G R

A I G

N

A I G R

N

A G R

A I G

N

A I

A I

Cannot store data for the current batch
where concept drift may occur

Ignores mutation forgetting when adding
new layers

High resource overhead

Difﬁcult data collection and possible
false positives

Hyperparameter setting

Limitations in identifying adversarial
conceptual drift in dynamic class
imbalanced data streams

Not suitable for small data streams, prone
to overﬁtting

Does not adaptively partition
heterogeneous data

Limited adaptive effect on conceptual drift

Euclidean distance used in the node
similarity measure is not suitable for
high-dimensional data

Note: The symbol description is the same as in Table 1.

3.3. Concept Drift Adaptation Methods Based on Hybrid Learning

Hybrid deep learning models usually consist of multiple deep underlying learning
models, either a free combination of discriminative or generative learning or discrim-
inative/generative learning plus other models, such as CNN + LSTM, GAN + CNN,
CNN + SVM, and other algorithms, as shown in Table 3.

The generative model and discriminant model have their own advantages. The
generative learning model can learn from unlabeled data and can save labor costs. The
discriminant learning model is better than the generative model in supervised tasks. Hybrid
deep learning integrates discriminant or generative models according to the target task,
and the framework for training deep generative models and discriminant models can enjoy

---

<!-- PAGE 14 -->

Appl. Sci. 2023, 13, 6515

14 of 27

the advantages of both models to solve real-world problems. The general process of the
concept drift adaption method based on generative learning is shown in Figure 7, while
the general parameter update mode accounts for a large proportion, and the proportion of
active detection and passive adaptation is comparable.

Figure 7. The general process of concept drift adaptation methods based on hybrid learning.

Typical algorithms combined with LSTM include HSN-LSTM, online autoregression
with deep long short-term memory (OAR-DLSTM), CausalConvLSTM, and LSTMCNNcda.
HSN-LSTM [71] is mainly used for multivariate time-series forecasting. It mainly embeds a
novel adaptive and hybrid spiking (AHS) module into LSTM to keep the model capable of
long-term prediction and alleviate its catastrophic forgetting problem. At the same time, in
order to mitigate the impact of concept drift, it adopts the negative log-likelihood function
in the fusion attention module to dynamically adjust the attention score and avoid noise
interference. However, the resource costs are relatively high. OAR-DLSTM [72] combines a
denoising autoencoder, an autoregressive model, and the deep long short-term memory
(DLSTM) method, where the denoising encoder is mainly applied to feature extraction,
and ORA and DLSTM are applied to target prediction. In the ofﬂine state, it divides the
training data into data blocks and then pre-trains and retrains the DLSTM model with the
error rate predicted by ORA in each data block to obtain several independent sub-models.
In the online state, the results of the two models are weighted using a maximum likelihood
estimation to obtain the ﬁnal time-series prediction output. When the dataset is too large,
its performance degrades. B-Detection [73] is primarily used to detect runtime reliability
anomalies in MEC services. It uses LSTM and AE models to capture the normal reliability
data stream distribution characteristics. A weight-based reservoir sampling technique is
then used to sample representative normal reliability data. Finally, the sampled data are
used for detection model training, and the detection model is retrained to accommodate
conceptual drift based on detection performance. However, the run time is relatively long.
A typical algorithm for the combination of LSTM and CNN is CausalConvLSTM [74],
which utilizes CNN to extract spatial features efﬁciently and the LSTM model for prediction.
It determines whether the model needs to be retrained based on the false-positive rate
calculated from the rolling window and updates the network weights to accommodate
concept drift by the backpropagation through time (BPTT) algorithm. CausalConvLSTM
is primarily used for network intrusion detection but has a problem in that it is limited
in the types of logs. Another example is LSTMCNNcda [75] for time-series forecasting,
which focuses on actively detecting the occurrence of concept drift and updating the
LSTMCNNnet model by an online parameter update when a concept drift is detected but
with certain restrictions on the normalized time series and window size selection.

In addition, typical algorithms based on hybrid learning include the stacked
autoencoder-deep neural network (SAE-DNN), OARIMA-RNN, and recurrent adaptive
classiﬁer ensemble (RACE). SAE-DNN [76] actively detects the occurrence of concept drift
using the STEPD. If a concept drift occurs, the top level of SAE-DNN is extended by
means of random vector function linking (RVFL). The parameters in the extension layer
are dynamically assigned to new data through Lasso regularization and L2 regularization.

---

<!-- PAGE 15 -->

Appl. Sci. 2023, 13, 6515

15 of 27

However, there is a certain amount of noise interference. Adaptive online ensemble learn-
ing with RNN and ARIMA (OARIMA-RNN) [39] uses RNN models to capture temporal
dependencies and implement online learning modeling. Then, it dynamically adapts to
concept drift by adding ARIMA to the set and RNN hyperparameters being optimized
with each new batch. It has better accuracy than traditional ofﬂine models. However, there
was no quantiﬁcation of conceptual drift or performance during the drift. RACE [77] uses
the concept of processing recycling, which uses an MLP, J48 decision tree, and support
vector machine as basic learners to process training instances of time-series data. Then, the
training instances are processed by the incremental learning algorithm, and the concept
is used to detect the occurrence of concept drift. When concept drift occurs, it is updated
and retrained. The algorithm requires a large amount of memory to run and slows down
convergence as the size of the integration increases.

Table 3. Concept drift adaptation methods based on hybrid learning.

Concept Drift Adaptation Methods

Types of Deep Learning

Algorithms

Detection
Modes

LSTM + SNN

HSN-LSTM [71]

LSTM + AE + ORA

OAR-DLSTM [72]

LSTM + AE

B-Detection [73]

LSTM + CNN

CausalConvLSTM [74]

LSTMCNNcda [75]

AE + DNN

SAE-DNN [76]

RNN + ARIMA

OARIMA-RNN [39]

MLP + Decision tree + SVM

RACE [77]

−

−

−

−

+

+

−

+

Update
Modes
√

√

√

√

√

×

√

√

Adaptation
Drift Types

N

I R

Limitation

High resource overhead

The dataset is too large, and its
performance appears to degrade

A I G R

Long running time

N

A G

A G

N

A G R

Limited log types for
algorithm applications

Time-series data normalization issues,
window size selection

Noise interference

No quantiﬁcation of conceptual drift
or performance during drift

Requires large amounts of memory,
increased integration size,
slows convergence

Note: The symbol description is the same as in Table 1.

From the summary of

typical algorithms in Table 3,

it can be seen that
“LSTM” + “other models” is a common hybrid approach, which is mainly applicable
to long-term streaming data and can overcome the forgetting problem and improve the
accuracy to a certain extent. In summary, for hybrid learning methods, multi-model in-
tegration is mainly tuned using dynamic weighting between models. So, it is essentially
parameter updating, and there are also embedded model combinations that are mainly
applied in process industries, such as power forecasting.

3.4. Other Concept Drift Adaptation Methods

The deep learning framework classiﬁcation mentioned above is mainly divided based
on the perspective of single-class models or hybrid multiple models. It is worth noting that
there are cases where other deep learning technologies [31,78], such as deep reinforcement
learning and deep federated learning, are used. For example, deep reinforcement learning
was introduced as a combination of deep learning (DL) and reinforcement learning (RL) to
better cope with the dynamic changes of unstable environments, leveraging the primary
deep learning models to generate the target models we need [79,80]. The general process
of this concept drift adaption method is shown in Figure 8, while the structure update
mode is more common in deep transfer learning. Parameter updating is more common in
deep reinforcement learning. However, relatively few research studies involving concept
drift adaption methods are elaborated compared to other classes. The most popular are
deep transfer learning (DTL) and deep reinforcement learning (DRL). Therefore, we mainly

---

<!-- PAGE 16 -->

Appl. Sci. 2023, 13, 6515

16 of 27

introduce DTL and DRL. Table 4 summarizes concept drift adaptation methods based on
DTL and DRL.

Figure 8. The general process of concept drift adaptation methods based on other deep learning.

•

DTL-based concept drift adaptation methods

DTL mainly uses pre-training of deep learning models to obtain relevant knowl-
edge. Then, by transferring the acquired knowledge to a new model, it can be adapted
to a new task with minimal data and can save resources [81]. Currently, there are not
many algorithms that involve concept drift. Typical methods are neural network patching
(NN-Patching), adaptive mechanisms for learning CNNs (AM-CNNs), and autonomous
transfer learning (ATL).

NN-Patching [82] is passively handled concept drift by an error estimator. It mainly
constructs a discriminant classiﬁer to identify the misclassiﬁed regions. Then, it trains a
new classiﬁer (called a patch network) on the misclassiﬁed data. The patch network uses
the intermediate layer of the original neural network to extract features and representations
that are critical to classiﬁcation. This method keeps the original neural network quickly
adaptable to concept drift, but its ability to handle concept drift is limited, and the hy-
perparameters need to be adjusted for the scene. AM-CNNs [83] uses the nonparametric
CUSUM test to actively detect the occurrence of concept drift. It relies on a “transfer
learning” paradigm that transfers the knowledge of the CNN running before the concept
drift to the CNN running after the concept drift, but the resource overhead is relatively
high. ATL [84] uses the autonomous Gaussian mixture model (AGMM) to automatically
adjust the network width, which solves the concept drift problem. It is just a matter of
readapting to a concept that has been there before when it reappears. An adaptive anomaly
detection approach toward concept drift (ADTCD) [85] is an adaptive anomaly detection
model based on knowledge distillation and DTL. It transfers knowledge from the AE-based
teacher model to the student model and updates only the student model, which dynami-
cally adjusts model weights to accommodate concept drift primarily through local inference
on new samples. However, the algorithm also suffers from two limitations. Firstly, the
industrial scenarios used for the experiments are relatively homogeneous, and secondly,
little attention is paid to scarce anomaly data.

•

DRL-based concept drift adaptation methods

DRL combines the perception ability of deep learning with the decision-making
ability of reinforcement learning, which can be directly controlled based on the input
information. Reinforcement learning deﬁnes the goal of optimization, and deep learning
gives the mechanism by which it works (how to characterize problems and how to solve
them) [86]. The algorithms using this concept drift adapting method are mainly applied in
the ﬁelds of ﬁnancial investment and anomaly detection. Typical algorithms include Deep-
Pocket, RL4OASD, online ensemble aggregation using reinforcement learning (OEA-RL),
and DeepBreath.

DeepPocket [87] is used in the ﬁeld of ﬁnancial investment. This algorithm mainly uses
a restricted stacked autoencoder to extract features and uses two convolutional networks

---

<!-- PAGE 17 -->

Appl. Sci. 2023, 13, 6515

17 of 27

to ﬁnd the best portfolio through deep reinforcement learning. Then, it uses online training
to dynamically update weights to accommodate concept drift, but it does not lend itself
to a long-term investment strategy. RL4OASD [88] is mainly used for the detection of
abnormal trajectories of vehicles. It includes two networks: one is responsible for learning
the features of the road network and trajectory, and the other is responsible for detecting
anomalous sub-traces based on the learned features. The two networks can be trained
iteratively without labeled data, and they employ an online learning strategy; that is, they
are trained with newly recorded trajectory data and continuously update their strategies
based on current trafﬁc conditions, but they have a longer training time. OEA-RL [89]
mainly uses the deep reinforcement learning framework as a meta-learning method to learn
linear weighted ensembles and actively detects the occurrence of concept drift through the
Page–Hinkley (PH) test. Then, it adapts to concept drift by updating its parameters. Again,
there is a certain delay in updating due to its active detection algorithm. DeepBreath [6]
is mainly used for ﬁnancial investment, which uses a limited superimposed autoencoder
for dimensionality reduction and feature processing. Then, the SARSA algorithm and the
online batch processing method are used to train CNN learning investment strategies from
historical data, and after training the model, the weights are updated through the online
learning scheme to adapt to the concept drift. The algorithm lacks, to some extent, the
consideration of exogenous factors.

As can be seen in Table 4, for DRL and DTL, the update mode of DRL is mainly
a parameter update. It interacts well with the environment to learn the sequence of its
behavior. The update mode of DTL is mainly a structural update. DTL can effectively
use a small amount of data to train neural networks. This characteristic can use structure
updates to train better predictive models. In addition, they generally use a combination
of online and ofﬂine approaches to adapt concept drift and support more complex predic-
tions. In addition to DTL and DRL, two more popular deep learning methods, there are
also concept drift adaption methods based on other deep learning technologies. Such as
FedHAR [90], which is a smart human activity recognition (HAR) frame based on deep
federated learning. FedHAR designs an unsupervised gradient aggregation strategy that
can overcome the problem of concept drift and convergence instability in online learning,
which is mainly used to summarize the gradients of all labeled clients and unlabeled clients
in federated learning and then drive the parameter update of the server model by averaging
the aggregate gradient to adapt to the concept drift.

Table 4. Other concept drift adaptation methods.

Types of
Deep
Learning

DTL

DRL

Algorithms

NN-Patching [82]

AM-CNNs [83]

ATL [84]

ADTCD [85]

DeepPocket [87]

RL4OASD [88]

OEA-RL [89]

DeepBreath [6]

DFL

FedHAR [90]

Concept Drift Adaptation Methods

Detection
Modes

Update Modes

Adaptation
Drift Types

Limitation

−

+

−

−

−

−

+

−

−

×

×

×
√

√

√

√

√

√

N

N

A I G

A I G R

N

N

N

N

N

Need to adjust hyperparameters for the scene

High overhead

Forgetting problem

Little attention is paid to scarce anomaly data

Not suitable for long-term investment strategies

Long model training time

Updating delay

Lack of consideration for exogenous factors

Scarcity of labels, with privacy

Note: The symbol description is the same as in Table 1.

3.5. Discussion

According to the summary of concept drift adaptation methods, we can see that the
proportion of hybrid learning and discriminant learning is relatively large, and especially

---

<!-- PAGE 18 -->

Appl. Sci. 2023, 13, 6515

18 of 27

discriminative learning is widely used. This phenomenon reﬂects the fact that having
label information samples is beneﬁcial for detecting changes in the distribution of data.
In addition, parameter updates also account for a large part. Compared with structural
updates, parameter updates reduce the convergence time and adapt well to abrupt concept
drift. Secondly, in the algorithms of discriminant learning and generative learning, its active
detection also accounts for a considerable part, and it is mainly conducive to explaining
the occurrence of concept drift and reducing the computing resources of training, but to a
certain extent, it requires additional memory and CPU storage. From this paper, it can be
seen that dealing with concept drift, reducing the amount of computation, saving resources,
and speeding up convergence are our main challenges at present.

In addition, according to the above summary of drift adaptation types, we can ﬁnd
that there are usually more adaptation methods for abrupt, incremental, and gradual
drift types. Relatively speaking, abrupt drift occurs most frequently, and its drift speed
occurs the fastest, so most detection methods can be sensitive to detection, but there will
also be problems such as update delay and high computational complexity. In contrast,
recurring drift occurs the least often. In the case of recurring drift, previously learned
models may become relevant again in the future. Online deep learning algorithms may
have to relearn previous concepts. This process has a high computational burden because it
means tuning or training a new model from scratch. This is also one of the main challenges
at this time. Finally, it should be added that in addition to being based on deep learning
algorithms, extreme learning machines are also models based on neural networks. In recent
years, the use of the concept drift algorithm of ELM has also increased, and the main
algorithms include Meta-RKOS-ELM [91], SSOE-FP-ELM [92], ONLAD [93], etc., which is
also a worthy research direction.

4. Performance Evaluation of Concept Drift

In this section, we summarize the common datasets and evaluation metrics. The
datasets are divided into real datasets and synthetic datasets. For the former, we present
its sources, learning tasks, and properties. For the latter, we show the drift types and
characteristics it contains. After that, we describe the evaluation metrics and their meanings.

4.1. Datasets

Real datasets can effectively demonstrate the generality and applicability of the al-
gorithm in the real world, for which the commonly used datasets are KDD CUP 1999,
Electricity, Weather, Spam, and CoverType. The KDD CUP 1999 [94] is the dataset used
in the KDD (knowledge discovery and data mining) competition. It is mainly used for
network intrusion detection to distinguish between normal network connections and mali-
cious network connections, including various attack data simulated in the military network
environment. Electricity [95] is derived from the electricity market of New South Wales,
Australia (1996–1998). It is mainly used to predict changes in electricity prices in the past
24 h, including the weather, user demand, supply conditions, and seasons. Weather [96]
contains daily weather measurement data for a certain area from 2006 to 2016, including
temperature, humidity, wind direction, wind speed, visibility, atmospheric pressure, etc.,
for predicting rainfall. Spam [97] is mainly used to identify spam. CoverType [94] is derived
from the forest cover of a certain area in the U.S. Forest Service system.

Synthetic datasets can evaluate the performance of the algorithms under different
concept drift situations and contain various types of concept drift. For detecting abrupt
concept drift, R.MNIST [98], P.MNIST [60], and SEA [99] can be used. SEA contains three
features and two classes in each sample. R.MNIST and P.MNIST are generated from the
MNIST dataset containing 784 features and 10 classes. It is worth noting that P.MNIST also
detects recurring drift. For detecting gradual concept drift, Circles [100], Hyperplane [101],
and LED [94] can be used. Circles contains two features and two classes in each sample.
Then, Hyperplane also detects incremental drift, containing 10 features and 2 classes

---

<!-- PAGE 19 -->

Appl. Sci. 2023, 13, 6515

19 of 27

in each sample. LED also detects abrupt drift, containing 24 features and 10 classes in
each sample.

In addition to the above commonly used datasets, there are some special datasets
for deep learning frameworks, such as the Vxheaven dataset [102] commonly used in
previous malware analysis studies, consisting of Windows binaries belonging to malware
and benign portable executables, containing different types of malware families, such as
trojans, ransomware, and viruses. HAR-UCI [103] was made from recordings of 30 subjects
performing activities of daily living. The STL-10 dataset [104] is an image recognition
dataset for the development of unsupervised feature learning, deep learning, and self-
learning algorithms. The Cat-Dog dataset [105] contains two classes, cats and dogs, with
12,500 images. The CIFAR100 dataset [106] is utilized to simulate the distribution drifting
situation. It has 60,000 32 × 32 × 3 RGB images. Finally, some researchers have used
their own collected data, as well as datasets from the application domain. For example,
the I-LSTM and ECNN algorithms are collected data, and CausalLSTM uses the HDFS
dataset [107] and the Cybersecurity’s Intrusion Detection Evaluation dataset [108].

4.2. The Evaluation Metrics

For algorithms based on discriminative learning and hybrid learning, accuracy recall,
precision, F1-score, Matthews’ correlation coefﬁcient (MCC), and Cohen’s kappa k are
mainly used for classiﬁcation problems, and mean absolute error (MAE), mean squared
error (MSE), and root mean squared error (RMSE) are mainly used for regression problems.
For algorithms based on generative learning and others, the number of hidden nodes per
time step (HN), the number of hidden layers per time step (HL), parameter count (PC),
and execution time (ET) are mainly used. In particular, they are unique evaluation metrics
under the framework of deep learning. It is worth noting that the MCC and Cohen’s kappa
k evaluation metrics are mainly used for unbalanced data. The deﬁnition of MCC is shown
in Equation (7).

MCC =

TP × TN − FP × FN
(cid:112)(TP + FP)(TP + FN)(TN + FP)(TN + FN)

(7)

where TP represents true positives, TN represents true negatives, FP represents false
positives, and FN represents false negatives. The deﬁnition of Cohen’s kappa is shown
in Equation (8).

k =

P0 − Pe
1 − Pe

(8)

where P0 and Pe are the success rate of the actual and random predictors.

In addition to the above basic evaluation metrics, some researchers also use some
evaluation metrics for the application ﬁeld of algorithms. For example, the DeepPocket
algorithm, which is mainly used in the ﬁeld of ﬁnancial investment, mainly uses maximum
drawdown (MDD), Sharpe ratio (Sr), and conditional value at risk (CVaR) to evaluate
its performance.

5. Future Directions

Based on the analysis and discussion of the above algorithms, we summarize the prob-
lems that need to be solved, which require further research in the future, as described below.

5.1. Full Coverage of Concept Drift Types

According to the above-mentioned algorithms, such as ONU-SHO-RNN, DEVDAN,
etc., we can ﬁnd that it is not possible to adapt to all concept drifts at once, and among the
four types of concept drift, the best adaptability of the algorithm is to abrupt drift. There
are also some algorithms, such as ECNN and HSN-LSTM, for which the dataset used in
the experimental part does not indicate the type of drift included, and there are also no

---

<!-- PAGE 20 -->

Appl. Sci. 2023, 13, 6515

20 of 27

experiments on the effectiveness of different types of concept drift. Therefore, it is necessary
to improve the robustness and generalization of the methods to study concept drift.

5.2. Data Processing Problem

Data processing has been a big challenge in deep learning and concept drift adaptation
methods [4,21]. Firstly, when inputting samples, we may face problems such as class-
imbalance data, high-dimensional data, etc. For example, when performing online anomaly
detection, most of the datasets are very unbalanced, and the abnormal data account for
a very small part [109]. Secondly, when the model update is performed, we will face the
problem of how to balance between new data and old data and the problem that the new
data samples are not enough to support the update of the deep learning model after the
concept drift occurs. These will lead to poor prediction, slow model convergence, delayed
model update, and other consequences that are worthy of our consideration and research.

5.3. Multi-Model Integration Problem

Our review shows that online integration methods have been more popular in concept
drift adaptation methods, such as OARIMA-RNN. Ensemble algorithms can effectively pre-
vent overﬁtting and provide better prediction performance. However, their computational
complexity is high, and they take up more resources, so how to optimize their performance
is also a question worthy of deep consideration [110].

5.4. Visualization Problem of Concept Drift

At present, there is relatively little research on concept drift visualization. Classic
visualizers have DriftVis [111], which can help decision makers identify and correct concept
drift in data streams.
In fact, for many related ﬁelds such as air quality monitoring,
ﬁnancial market analysis, etc. [7,112], explaining concept drift is conducive to helping
decision makers comprehensively analyze problems and make correct decisions. Finally, it
is worth mentioning the application of conceptual drift type visualization.

6. Conclusions

In recent years, deep learning has become one of the core technologies of the fourth
industrial revolution. So, it has also become one of the indispensable tools to assist intelli-
gent decision making. However, in the era of the epidemic and big data, data distribution
in streaming data can change very easily, which is a phenomenon known as concept drift.
Once concept drift occurs, even the best-trained deep learning models become obsolete,
producing poor predictions. Therefore, this paper summarizes concept drift adaptation
methods under the deep learning framework. Firstly, we explain the deﬁnition and causes
of concept drift. Then, we introduce the types of concept drift and the general process of
a concept drift adapting method under the deep learning framework. Next, we divide
the deep learning model using the concept drift adaptation method from four aspects,
including discriminant learning, generative learning, hybrid learning, and others. For each
aspect, we introduce in detail the update modes, detection modes, and adaptation drift
types of concept drift adaptation methods. Finally, we summarize common datasets and
evaluation metrics for concept drift adaptation methods and point out future directions.
We hope that this paper can provide some academic help to researchers.

Author Contributions: Conceptualization, Q.X. and L.Z.; methodology, Q.X. and X.C.; formal analy-
sis, Q.X. and Y.W.; investigation, Q.X. and X.C.; writing—original draft preparation, Q.X.; writing—
review and editing, Q.X., L.Z., X.C., and Y.W.; supervision, L.Z.; project administration, L.Z.; funding
acquisition, L.Z. All authors have read and agreed to the published version of the manuscript.

Funding: This work was supported by the Key Program of Chongqing Education Science Planning
Project (No. K22YE205098) and the Doctoral Research Foundation of Chongqing Normal University
(No.21XLB030, No.21XLB029).

Institutional Review Board Statement: Not applicable.

---

<!-- PAGE 21 -->

Appl. Sci. 2023, 13, 6515

21 of 27

Informed Consent Statement: Not applicable.

Data Availability Statement: The data supporting this review are from previously reported studies
and datasets, which have been cited.

Acknowledgments: We acknowledge the financial support provided by the Key Program of Chongqing
Education Science Planning Project (No. K22YE205098) and the Doctoral Research Foundation of
Chongqing Normal University (No. 21XLB030, No. 21XLB029).

Conﬂicts of Interest: The authors declare that there are no conﬂict of interest regarding the publica-
tion of this paper.

Abbreviations

one-class drift detector
concept drift type identiﬁcation method based on multi-sliding windows
Kolmogorov–Smirnov test detector
label dependency drift detector
student–teacher approach for unsupervised drift detection
concept drift handling based on clustering in the model space
diversity measure drift detection method
improved long short-term memory
drift detection method
multilayer perceptron
convolutional neural network
recurrent neural network
deep neural network
selective ensemble-based online adaptive deep neural network
bilevel online deep learning framework
neural network with dynamically evolved capacity

The following abbreviations are used in this manuscript:
OCDD
CDT_MSW
KSWIN
LD3
STUDD
CDCMS
DMDDM
I-LSTM
DDM
MLP
CNN
RNN
DNN
SEOA
BODL
NADINE
CIDD-ADODNN Adadelta optimizer-based deep neural networks with concept drift detection
ADWIN
OARNN
TPE
ONU-SHO
ONU-SHO-RNN ONU-SHO-based RNN

adaptive sliding-window drift detection technology
online adaptive recurrent neural network
tree-structured Parzen estimator
opposition-based novel updating spotted hyena optimization

AIBL-MVD

SPC
MUSE-RNN
LSTM
CI
GA

MOMBD-CDD

STEPD
GSO
Bi-LSTM
CUSUM
EWMA
AD-LSTM
SDWIN
TP-ALS
ECNN

OS-PGSM

DIH
ROC

adaptive behavioral-based incremental batch learning malware variant
detection model
statistical process control
multilayer self-evolving recurrent neural network
long short-term memory
continuous integration
genetic algorithm
multi-objective metaheuristic optimization-based big data analytics with
concept drift detection
Statistical Test of Equal Proportions method
glowworm swarm optimization
bidirectional long short-term memory
cumulative sum
exponentially weighted moving average
adaptive LSTM framework
sliding-window algorithm
two-phase adaptive learning strategy
evolutive convolutional neural network
online CNN-based model selection using performance gradient-based
saliency maps
deep incremental hashing
region of competence

---

<!-- PAGE 22 -->

Appl. Sci. 2023, 13, 6515

22 of 27

DRT

ARCUS

USCDD-AE
DEVDAN
MemStream
FIFO
ADTCD
GAN
AE
RBM
SOM

DCIGAN

GF
GRBM
OUIM-SOM

SOINN+

AHS
OAR-DLSTM
HDL-OKW
BPTT
SAE-DNN
RVFL
SVM
OARIMA-RNN
RACE
DTL
NN-Patching
AM-CNNs
ATL
AGMM
DRL
OEA-RL
PH
KDD
MCC
MAE
MSE
RMSE
HN
HL
PC
ET
MDD
Sr
CVaR
FedHAR

data reduction technique
adaptive framework for online deep anomaly detection under a complex
evolving data stream
unsupervised statistical concept drift detection
deep evolving denoising autoencoder
memory-based streaming anomaly detection
ﬁrst in, ﬁrst out
adaptive anomaly detection approach toward concept drift
generative adversarial network
autoencoder
restricted Boltzmann machine
self-organizing mapping
distributed class-incremental learning method based on generative
adversarial networks
generative fusion
Gaussian restricted Boltzmann machine
online unsupervised incremental method based on self-organizing maps
self-organizing incremental neural network for unsupervised learning from
noisy data streams
novel adaptive and hybrid spiking module
online autoregression with deep long short-term memory
hybrid deep learning classiﬁer and optimized key windowing approach
backpropagation through time
stacked autoencoder-deep neural network
random vector function linking
support vector machines
adaptive online ensemble learning with recurrent neural network and ARIMA
recurrent adaptive classiﬁer ensemble
deep transfer learning
neural network patching
adaptive mechanism for learning CNNs
autonomous transfer learning
autonomous Gaussian mixture model
deep reinforcement learning
online ensemble aggregation using reinforcement learning
Page–Hinkley
knowledge discovery and data mining
Matthews’ correlation coefﬁcient
mean absolute error
mean squared error
root mean squared error
the number of hidden nodes per time step
the number of hidden layers per time step
parameter count
execution time
maximum drawdown
Sharpe ratio
conditional value at risk
federated learning human activity recognition frame

References

1.

2.
3.

4.

Shrestha, Y.R.; Krishna, V.; von Krogh, G. Augmenting organizational decision-making with deep learning algorithms: Principles,
promises, and challenges. J. Bus. Res. 2021, 123, 588–603. [CrossRef]
Schlimmer, J.C.; Granger, R.H. Incremental learning from noisy data. Mach. Learn. 1986, 1, 317–354. [CrossRef]
Lu, J.; Liu, A.; Song, Y.; Zhang, G. Data-driven decision support under concept drift in streamed big data. Complex Intell. Syst.
2020, 6, 157–163. [CrossRef]
Gama, J.; Žliobait ˙e, I.; Bifet, A.; Pechenizkiy, M.; Bouchachia, A. A survey on concept drift adaptation. ACM Comput. Surv. 2014,
46, 1–37. [CrossRef]

---

<!-- PAGE 23 -->

Appl. Sci. 2023, 13, 6515

23 of 27

5.

6.

Xu, R.; Cheng, Y.; Liu, Z.; Xie, Y.; Yang, Y. Improved Long Short-Term Memory based anomaly detection with concept drift
adaptive method for supporting IoT services. Futur. Gener. Comput. Syst. 2020, 112, 228–242. [CrossRef]
Soleymani, F.; Paquet, E. Financial portfolio optimization with online deep reinforcement learning and restricted stacked
autoencoder—DeepBreath. Expert Syst. Appl. 2020, 156, 113456. [CrossRef]

7. Wang, X.; Chen, W.; Xia, J.; Chen, Z.; Xu, D.; Wu, X.; Xu, M.; Schreck, T. ConceptExplorer: Visual Analysis of Concept Drifts in
Multi-source Time-series Data. In Proceedings of the IEEE Conference on Visual Analytics Science and Technology (VAST), Salt
Lake City, UT, USA, 25–30 October 2020; pp. 1–11. [CrossRef]

8. Hoens, T.R.; Polikar, R.; Chawla, N.V. Learning from streaming data with concept drift and imbalance: An overview. Prog. Artif.

Intell. 2012, 1, 89–101. [CrossRef]

9. Wen, Y.; Qiang, B.; Fan, Z. A survey of the classiﬁcation of data streams with concept drift. CAAI Trans. Intell. Syst. 2013, 8,

95–104.

10. Ditzler, G.; Roveri, M.; Alippi, C.; Polikar, R. Learning in Nonstationary Environments: A Survey. IEEE Comput. Intell. Mag. 2015,

10, 12–25. [CrossRef]

11. Webb, G.I.; Hyde, R.; Cao, H.; Nguyen, H.L.; Petitjean, F. Characterizing concept drift. Data Min. Knowl. Discov. 2016, 30, 964–994.

[CrossRef]

12. Krawczyk, B.; Minku, L.L.; Gama, J.; Stefanowski, J.; Wo´zniak, M. Ensemble learning for data stream analysis: A survey.

Inf. Fusion 2017, 37, 132–156. [CrossRef]

13. Khamassi, I.; Sayed-Mouchaweh, M.; Hammami, M.; Ghédira, K. Discussion and review on evolving data streams and concept

drift adapting. Evol. Syst. 2018, 9, 1–23. [CrossRef]

14. Lu, J.; Liu, A.; Dong, F.; Gu, F.; Gama, J.; Zhang, G. Learning under Concept Drift: A Review. IEEE Trans. Knowl. Data Eng. 2018,

31, 2346–2363. [CrossRef]

15. Ab Ghani, N.L.; Aziz, I.A.; Mehat, M. Concept Drift Detection on Unlabeled Data Streams: A Systematic Literature Review. In
Proceedings of the IEEE Conference on Big Data and Analytics (ICBDA), Xiamen, China, 8–11 May 2020; pp. 61–65. [CrossRef]
16. Lima, M.; Neto, M.; Filho, T.S.; Fagundes, R.A.D.A. Learning Under Concept Drift for Regression—A Systematic Literature

Review. IEEE Access 2022, 10, 45410–45429. [CrossRef]

17. Bayram, F.; Ahmed, B.S.; Kassler, A. From concept drift to model degradation: An overview on performance-aware drift detectors.

Knowl. Based Syst. 2022, 245, 108632. [CrossRef]

18. Desale, K.S.; Shinde, S.V. Addressing Concept Drifts Using Deep Learning for Heart Disease Prediction: A Review. In Proceedings
of Second Doctoral Symposium on Computational Intelligence; Gupta, D., Khanna, A., Kansal, V., Fortino, G., Hassanien, A.E., Eds.;
Springer: Singapore, 2022; Volume 1374, pp. 157–167. [CrossRef]
Iwashita, A.S.; Papa, J.P. An Overview on Concept Drift Learning. IEEE Access 2018, 7, 1532–1547. [CrossRef]

19.
20. R.O. Duda, P.E. Hart, and D.G. Stork, Pattern Classiﬁcation, New York: John Wiley & Sons, 2001, pp. xx + 654, ISBN: 0-471-05669-3.

J. Classif. 2007, 24, 305–307. [CrossRef]

21. Agrahari, S.; Singh, A.K. Concept Drift Detection in Data Stream Mining: A literature review. J. King Saud Univ.-Comput. Inf. Sci.

2021, 34, 9523–9540. [CrossRef]

22. Korycki, Ł.; Krawczyk, B. Adversarial concept drift detection under poisoning attacks for robust data stream mining. Mach. Learn.

2022, 1–36. [CrossRef]

23. Gözüaçık, Ö.; Can, F. Concept learning using one-class classiﬁers for implicit drift detection in evolving data streams. Artif. Intell.

Rev. 2021, 54, 3725–3747. [CrossRef]

24. Guo, H.; Li, H.; Ren, Q.; Wang, W. Concept drift type identiﬁcation based on multi-sliding windows. Inf. Sci. 2022, 585, 1–23.

[CrossRef]

25. Raab, C.; Heusinger, M.; Schleif, F.-M. Reactive Soft Prototype Computing for Concept Drift Streams. Neurocomputing 2020, 416,

340–351. [CrossRef]

26. Gözüaçık, Ö.; Büyükçakır, A.; Bonab, H.; Can, F. Unsupervised concept drift detection with a discriminative classiﬁer. In
Proceedings of the 28th ACM International Conference on Information and Knowledge Management, Beijing China, 3–7
November 2019; pp. 2365–2368.

27. Cerqueira, V.; Gomes, H.M.; Bifet, A.; Torgo, L. STUDD: A student–teacher method for unsupervised concept drift detection.

Mach. Learn. 2022, 1–28. [CrossRef]

28. Chiu, C.W.; Minku, L.L. A Diversity Framework for Dealing with Multiple Types of Concept Drift Based on Clustering in the

Model Space. IEEE Trans. Neural Netw. Learn. Syst. 2020, 33, 1299–1309. [CrossRef]

29. Mahdi, O.A.; Pardede, E.; Ali, N.; Cao, J. Diversity measure as a new drift detection method in data streaming. Knowl.-Based Syst.

2020, 191, 105227. [CrossRef]

30. Yuan, L.; Li, H.; Xia, B.; Gao, C.; Liu, M.; Yuan, W.; You, X. Recent Advances in Concept Drift Adaptation Methods for Deep
Learning. In Proceedings of the 31st International Joint Conference on Artiﬁcial Intelligence, Vienna, Austria, 23–29 July 2022;
International Joint Conferences on Artiﬁcial Intelligence Organization: Vienna, Austria, 2022; pp. 5654–5661.
Sarker, I.H. Deep Learning: A Comprehensive Overview on Techniques, Taxonomy, Applications and Research Directions. SN
Comput. Sci. 2021, 2, 420. [CrossRef]

31.

---

<!-- PAGE 24 -->

Appl. Sci. 2023, 13, 6515

24 of 27

32. Leväsluoto, J.; Kohl, J.; Sigfrids, A.; Pihlajamäki, J.; Martikainen, J. Digitalization as an Engine for Change? Building a Vision
Pathway towards a Sustainable Health Care System by Using the MLP and Health Economic Decision Modelling. Sustainability
2021, 13, 13007. [CrossRef]

33. Guo, H.; Zhang, S.; Wang, W. Selective ensemble-based online adaptive deep neural networks for streaming data with concept

drift. Neural Netw. 2021, 142, 437–456. [CrossRef]

34. Han, Y.-N.; Liu, J.-W.; Xiao, B.-B.; Wang, X.-T.; Luo, X.-L. Bilevel Online Deep Learning in Non-stationary Environment. In
Proceedings of the 30th International Conference on Artiﬁcial Neural Networks, Bratislava, Slovakia, 14–17 September 2021.
[CrossRef]

35. Pratama, M.; Za’In, C.; Ashfahani, A.; Ong, Y.S.; Ding, W. Automatic Construction of Multi-layer Perceptron Network from
Streaming Examples. In Proceedings of the 28th ACM International Conference on Information and Knowledge Management,
Beijing China, 3–7 November 2019. [CrossRef]

36. Priya, S.; Uthra, R.A. Deep learning framework for handling concept drift and class imbalanced complex decision-making on

streaming data. Complex Intell. Syst. 2021, 1–17. [CrossRef]

37. Dezfouli, A.; Grifﬁths, K.; Ramos, F.; Dayan, P.; Balleine, B.W. Models that learn how humans learn: The case of decision-making

38.

39.

40.

and its disorders. PLoS Comput. Biol. 2019, 15, e1006903. [CrossRef]
Fekri, M.N.; Patel, H.; Grolinger, K.; Sharma, V. Deep learning for load forecasting with smart meter data: Online Adaptive
Recurrent Neural Network. Appl. Energy 2021, 282, 116177. [CrossRef]
Jagait, R.K.; Fekri, M.N.; Grolinger, K.; Mir, S. Load Forecasting Under Concept Drift: Online Ensemble Learning with Recurrent
Neural Network and ARIMA. IEEE Access 2021, 9, 98992–99008. [CrossRef]
Singh, M.N.; Khaiyum, S. Enhanced Data Stream Classiﬁcation by Optimized Weight Updated Meta-learning: Continuous
learning-based on Concept-Drift. Int. J. Web Inf. Syst. 2021, 17, 645–668. [CrossRef]

41. Darem, A.A.; Ghaleb, F.A.; Al-Hashmi, A.A.; Abawajy, J.H.; Alanazi, S.M.; Al-Rezami, A.Y. An Adaptive Behavioral-Based
Incremental Batch Learning Malware Variants Detection Model Using Concept Drift Detection and Sequential Deep Learning.
IEEE Access 2021, 9, 97180–97196. [CrossRef]

42. Das, M.; Pratama, M.; Savitri, S.; Zhang, J. MUSE-RNN: A Multilayer Self-Evolving Recurrent Neural Network for Data Stream
Classiﬁcation. In Proceedings of the IEEE International Conference on Data Mining (ICDM), Beijing, China, 8–11 November 2019;
pp. 110–119. [CrossRef]

43. Badri, A.K.; Heikal, J.; Terah, Y.A.; Nurjaman, D.R. Decision-Making Techniques using LSTM on Antam Mining Shares before

44.

and during the COVID-19 Pandemic in Indonesia. Aptisi Trans. Manag. 2021, 6, 167–180. [CrossRef]
Saidani, I.; Ouni, A.; Mkaouer, M.W. Improving the prediction of continuous integration build failures using deep learning.
Autom. Softw. Eng. 2022, 29, 21. [CrossRef]

45. Mansour, R.F.; Al-Otaibi, S.; Al-Rasheed, A.; Aljuaid, H.; Pustokhina, I.V.; Pustokhin, D.A. An Optimal Big Data Analytics with

Concept Drift Detection on High-Dimensional Streaming Data. Comput. Mater. Contin. 2021, 68, 2843–2858. [CrossRef]

46. Alencar, B.M.; Canário, J.P.; Neto, R.L.; Prazeres, C.; Bifet, A.; Rios, R.A. Fog-DeepStream: A new approach combining LSTM and

Concept Drift for data stream analytics on Fog computing. Internet Things 2023, 22, 100731. [CrossRef]

47. Luo, X.; Zhang, D. An adaptive deep learning framework for day-ahead forecasting of photovoltaic power generation. Sustain.

Energy Technol. Assess. 2022, 52, 16. [CrossRef]

48. Diez-Olivan, A.; Ortego, P.; Del Ser, J.; Landa-Torres, I.; Galar, D.; Camacho, D.; Sierra, B. Adaptive Dendritic Cell-Deep Learning
Approach for Industrial Prognosis Under Changing Conditions. IEEE Trans. Ind. Inform. 2021, 17, 7760–7770. [CrossRef]
49. Cheng, M.-M.; Jiang, P.-T.; Han, L.-H.; Wang, L.; Torr, P. Deeply Explain CNN Via Hierarchical Decomposition. Int. J. Comput. Vis.

2023, 131, 1091–1105. [CrossRef]

50. Gu, J.; Wang, Z.; Kuen, J.; Ma, L.; Shahroudy, A.; Shuai, B.; Liu, T.; Wang, X.; Wang, G.; Cai, J.; et al. Recent advances in

convolutional neural networks. Pattern Recognit. 2018, 77, 354–377. [CrossRef]

51. Li, X.; Zhang, Z.; Zhao, Z.; Wu, L.; Huo, J.; Zhang, J.; Wang, Y. ECNN: One Online Deep Learning Model for Streaming Ocean
Data Prediction. In Proceedings of the ACM International Conference on Intelligent Computing and Its Emerging Applications,
Jinan, China, 28–29 December 2021; p. 6.
Saadallah, A.; Jakobs, M.; Morik, K. Explainable Online Deep Neural Network Selection Using Adaptive Saliency Maps for Time
Series Forecasting. In Machine Learning and Knowledge Discovery in Databases. Research Track; Oliver, N., Pérez-Cruz, F., Kramer, S.,
Read, J., Lozano, J.A., Eds.; Springer International Publishing: Cham, Switzerland, 2021; Volume 12975, pp. 404–420. [CrossRef]
53. Tian, X.; Ng, W.W.Y.; Xu, H. Deep Incremental Hashing for Semantic Image Retrieval with Concept Drift. IEEE Trans. Big Data

52.

2023, 1–13. [CrossRef]

54. Lobo, J.L.; Laña, I.; Del Ser, J.; Bilbao, M.N.; Kasabov, N. Evolving Spiking Neural Networks for online learning over drifting data

streams. Neural Netw. 2018, 108, 1–19. [CrossRef]

55. Da’u, A.; Salim, N. Recommendation system based on deep learning methods: A systematic review and new directions.

Artif. Intell. Rev. 2020, 53, 2709–2748. [CrossRef]

56. Deng, L. A tutorial survey of architectures, algorithms, and applications for deep learning. APSIPA Trans. Signal Inf. Process. 2014,

3, e2. [CrossRef]

57. Bank, D.; Koenigstein, N.; Giryes, R. Autoencoders. arXiv 2021, arXiv:2003.05991.

---

<!-- PAGE 25 -->

Appl. Sci. 2023, 13, 6515

25 of 27

58. Yoon, S.; Lee, Y.; Lee, J.-G.; Lee, B.S. Adaptive Model Pooling for Online Deep Anomaly Detection from a Complex Evolving Data
Stream. In Proceedings of the 28th ACM SIGKDD Conference on Knowledge Discovery and Data Mining, Washington, DC, USA,
14–18 August 2022; pp. 2347–2357. [CrossRef]
Friedrich, B.; Sawabe, T.; Hein, A. Unsupervised statistical concept drift detection for behaviour abnormality detection.
Appl. Intell. 2022, 53, 2527–2537. [CrossRef]

59.

60. Ashfahani, A.; Pratama, M.; Lughofer, E.; Ong, Y.-S. DEVDAN: Deep evolving denoising autoencoder. Neurocomputing 2020, 390,

297–314. [CrossRef]

61. Bhatia, S.; Jain, A.; Srivastava, S.; Kawaguchi, K.; Hooi, B. MemStream: Memory-Based Streaming Anomaly Detection. In

Proceedings of the ACM Web Conference 2022, Lyon, France, 25–29 April 2022; pp. 610–621. [CrossRef]

62. Goodfellow, I.; Pouget-Abadie, J.; Mirza, M.; Xu, B.; Warde-Farley, D.; Ozair, S.; Courville, A.; Bengio, Y. Generative adversarial

networks. Commun. ACM 2020, 63, 139–144. [CrossRef]

63. Guan, H.; Wang, Y.; Ma, X.; Li, Y. DCIGAN: A Distributed Class-Incremental Learning Method Based on Generative Adversarial
Networks. In Proceedings of the IEEE Intl Conf on Parallel & Distributed Processing with Applications, Big Data & Cloud Com-
puting, Sustainable Computing & Communications, Social Computing & Networking (ISPA/BDCloud/SocialCom/SustainCom),
Rio de Janeiro, Brazil, 20–24 May 2019; pp. 768–775. [CrossRef]

64. Guzy, F.; Wozniak, M.; Krawczyk, B. Evaluating and Explaining Generative Adversarial Networks for Continual Learning under
Concept Drift. In Proceedings of the International Conference on Data Mining Workshops (ICDMW), Auckland, New Zealand,
7–10 December 2021; pp. 295–303. [CrossRef]

65. Zhang, N.; Ding, S.; Zhang, J.; Xue, Y. An overview on Restricted Boltzmann Machines. Neurocomputing 2018, 275, 1186–1199.

[CrossRef]

66. Korycki, L.; Krawczyk, B. Concept Drift Detection from Multi-Class Imbalanced Data Streams. In Proceedings of the IEEE 37th

International Conference on Data Engineering (ICDE), Chania, Greece, 19–22 April 2021; pp. 1068–1079.

67. Wang, W.; Zhang, M. Data Stream Adaptive Partitioning of Sliding Window Based on Gaussian Restricted Boltzmann Machine.
In Artiﬁcial Intelligence in China; Liang, Q., Wang, W., Mu, J., Liu, X., Na, Z., Chen, B., Eds.; Springer: Singapore, 2020; Volume 572,
pp. 220–228. [CrossRef]

68. Miljkovic, D. Brief review of self-organizing maps. In Proceedings of the 40th International Convention on Information and
Communication Technology, Electronics and Microelectronics (MIPRO), Opatija, Croatia, 22–26 May 2017; pp. 1061–1066.
69. Cerri, R.; Junior, J.D.C.; Faria, E.R.; Gama, J. A new self-organizing map based algorithm for multi-label stream classiﬁcation. In
Proceedings of the 36th Annual ACM Symposium on Applied Computing, Virtual Event Republic of Korea, 22–26 March 2021.
[CrossRef]

70. Wiwatcharakoses, C.; Berrar, D. SOINN+, a Self-Organizing Incremental Neural Network for Unsupervised Learning from Noisy

Data Streams. Expert Syst. Appl. 2020, 143, 113069. [CrossRef]

71. Zheng, W.; Zhao, P.; Chen, G.; Zhou, H.; Tian, Y. A Hybrid Spiking Neurons Embedded LSTM Network for Multivariate Time

72.

Series Learning under Concept-drift Environment. IEEE Trans. Knowl. Data Eng. 2022, 1–14. [CrossRef]
Sun, L.; Ji, Y.; Zhu, M.; Gu, F.; Dai, F.; Li, K. A new predictive method supporting streaming data with hybrid recurring concept
drifts in process industry. Comput. Ind. Eng. 2021, 161, 107625. [CrossRef]

73. Wang, L.; Chen, S.; Chen, F.; He, Q.; Liu, J. B-Detection: Runtime Reliability Anomaly Detection for MEC Services with Boosting

LSTM Autoencoder. IEEE Trans. Mob. Comput. 2023, 1–14. [CrossRef]

74. Yen, S.; Moh, M.; Moh, T.-S. CausalConvLSTM: Semi-Supervised Log Anomaly Detection Through Sequence Modeling. In
Proceedings of the 18th IEEE International Conference on Machine Learning And Applications (ICMLA), Boca Raton, FL, USA,
16–19 December 2019; pp. 1334–1341.

75. Perera, P.P.B. Anomaly Detection on Single Variate Time Series with Concept drifts. Ph.D. Thesis, University of Colombo School

of Computing, Colombo, Sri Lanka, 2021.

76. Zhang, X.; Zou, Y.; Li, S. Enhancing incremental deep learning for FCCU end-point quality prediction. Inf. Sci. 2020, 530, 95–107.

[CrossRef]

77. Museba, T.; Nelwamondo, F.; Ouahada, K.; Akinola, A. Recurrent Adaptive Classiﬁer Ensemble for Handling Recurring Concept

Drifts. Appl. Comput. Intell. Soft Comput. 2021, 2021, 5533777. [CrossRef]

78. Massaoudi, M.; Chihi, I.; Abu-Rub, H.; Refaat, S.S.; Oueslati, F.S. Convergence of Photovoltaic Power Forecasting and Deep

Learning: State-of-Art Review. IEEE Access 2021, 9, 136593–136615. [CrossRef]

79. Mnih, V.; Kavukcuoglu, K.; Silver, D.; Rusu, A.A.; Veness, J.; Bellemare, M.G.; Graves, A.; Riedmiller, M.; Fidjeland, A.K.;

Ostrovski, G.; et al. Human-level control through deep reinforcement learning. Nature 2015, 518, 529–533. [CrossRef]

80. Zhang, D.; China Electric Power Research Institute; Han, X.; Deng, C. Taiyuan University of Technology. Review on the research
and practice of deep learning and reinforcement learning in smart grids. CSEE J. Power Energy Syst. 2018, 4, 362–370. [CrossRef]
81. Tan, C.; Sun, F.; Kong, T.; Zhang, W.; Yang, C.; Liu, C. A Survey on Deep Transfer Learning. In Proceedings of the 27th International

Conference on Artiﬁcial Neural Networks, Rhodes, Greece, 4–7 October 2018. [CrossRef]

82. Kauschke, S.; Lehmann, D.H.; Furnkranz, J. Patching Deep Neural Networks for Nonstationary Environments. In Proceedings of

the International Joint Conference on Neural Networks (IJCNN), Budapest, Hungary, 14–19 July 2019.

83. Disabato, S.; Roveri, M. Learning Convolutional Neural Networks in presence of Concept Drift. In Proceedings of the International

Joint Conference on Neural Networks (IJCNN), Budapest, Hungary, 14–19 July 2019; p. 8. [CrossRef]

---

<!-- PAGE 26 -->

Appl. Sci. 2023, 13, 6515

26 of 27

84. Pratama, M.; de Carvalho, M.; Xie, R.; Lughofer, E.; Lu, J. ATL: Autonomous Knowledge Transfer from Many Streaming
Processes. In Proceedings of the 28th ACM International Conference on Information and Knowledge Management, Beijing, China,
3–7 November 2019.

85. Xu, L.; Ding, X.; Peng, H.; Zhao, D.; Li, X. ADTCD: An Adaptive Anomaly Detection Approach Towards Concept-Drift in IoT.

IEEE Internet Things J. 2023, 1–13. [CrossRef]

86. Yang, T.; Tang, H.; Bai, C.; Liu, J.; Hao, J.; Meng, Z.; Liu, P.; Wang, Z. Exploration in Deep Reinforcement Learning: A

87.

Comprehensive Survey. arXiv 2022, arXiv:2109.06668.
Soleymani, F.; Paquet, E. Deep graph convolutional reinforcement learning for ﬁnancial portfolio management—DeepPocket.
Expert Syst. Appl. 2021, 182, 115127. [CrossRef]

88. Zhang, Q.; Wang, Z.; Long, C.; Huang, C.; Yiu, S.M.; Liu, Y.; Cong, G.; Shi, J. Online Anomalous Subtrajectory Detection on Road

89.

Networks with Deep Reinforcement Learning. arXiv 2022, arXiv:2211.08415. [CrossRef]
Saadallah, A.; Morik, K. Online Ensemble Aggregation using Deep Reinforcement Learning for Time Series Forecasting. In
Proceedings of the IEEE 8th International Conference on Data Science and Advanced Analytics (DSAA), Porto, Portugal,
6–9 October 2021; pp. 1–8. [CrossRef]

90. Yu, H.; Chen, Z.; Zhang, X.; Chen, X.; Zhuang, F.; Xiong, H.; Cheng, X. FedHAR: Semi-Supervised Online Learning for

Personalized Federated Human Activity Recognition. IEEE Trans. Mob. Comput. 2021, 22, 3318–3332. [CrossRef]

91. Liu, Z.; Loo, C.K.; Pasupa, K.; Seera, M. Meta-cognitive recurrent kernel online sequential extreme learning machine with kernel

adaptive ﬁlter for concept drift handling. Eng. Appl. Artif. Intell. 2020, 88, 103327. [CrossRef]

92. da Silva, C.A.S.; Krohling, R.A. Semi-Supervised Online Elastic Extreme Learning Machine with Forgetting Parameter to deal
with concept drift in data streams. In Proceedings of the International Joint Conference on Neural Networks (IJCNN), Budapest,
Hungary, 14–19 July 2019; pp. 1–8.

93. Tsukada, M.; Kondo, M.; Matsutani, H. A Neural Network-Based On-device Learning Anomaly Detector for Edge Devices.

IEEE Trans. Comput. 2020, 69, 1027–1044. [CrossRef]

94. Asuncion, A.; Newman, D. UCI Machine Learning Repository; University of California: Irvine, CA, USA, 2007.
95. Harries, M.; Wales, N.S. Splice-2 Comparative Evaluation: Electricity Pricing; Research Gate: Berlin, Germany, 1999.
96. Elwell, R.; Polikar, R. Incremental Learning of Concept Drift in Nonstationary Environments. IEEE Trans. Neural Netw. 2011, 22,

1517–1531. [CrossRef]

97. Katakis, I.; Tsoumakas, G.; Vlahavas, I. Tracking recurring contexts using ensemble classiﬁers: An application to email ﬁltering.

Knowl. Inf. Syst. 2010, 22, 371–391. [CrossRef]

98. Lopez-Paz, D.; Ranzato, M.A. Gradient Episodic Memory for Continual Learning. arXiv 2022, arXiv:1706.08840.
99.

Street, W.N.; Kim, Y. A streaming ensemble algorithm (SEA) for large-scale classiﬁcation. In Proceedings of the seventh ACM
SIGKDD international conference on Knowledge discovery and data mining, San Francisco, CA, USA, 26–29 August 2001; ACM
Press: New York, NY, USA, 2001; pp. 377–382.

100. Gama, J.; Medas, P.; Castillo, G.; Rodrigues, P. Learning with Drift Detection. In Advances in Artiﬁcial Intelligence—SBIA 2004;

Bazzan, A.L.C., Labidi, S., Eds.; Springer: Berlin/Heidelberg, Germany, 2004; Volume 3171, pp. 286–295. [CrossRef]

101. Fan, W.; Yu, P.; Han, J. Mining Concept-Drifting Data Streams using Ensemble Classiﬁers. In Proceedings of the 9th ACM SIGKDD

International Conference on Knowledge Discovery and Data Mining, Washington, DC, USA, 24–27 August 2003; p. 10.

102. Kakisim, A.G.; Nar, M.; Sogukpinar, I. Metamorphic malware identiﬁcation using engine-speciﬁc patterns based on co-opcode

graphs. Comput. Stand. Interfaces 2020, 71, 103443. [CrossRef]

103. Anguita, D.; Ghio, A.; Oneto, L.; Parra-Llanas, X.; Reyes-Ortiz, J. Proceedings of the International Conference on European Symposium

on Artiﬁcial Neural Networks (ESANN); ESAN: Bruges, Belgium, 2013; Volume 3, p. 3.

104. Coates, A.; Ng, A.; Lee, H. An analysis of single-layer networks in unsupervised feature learning. In Proceedings of the 14th
International Conference on Artiﬁcial Intelligence and Statistics, Fort Lauderdale, FL, USA, 11–13 April 2011; pp. 215–223.
105. Elson, J.; Douceur, J.R.; Howell, J.; Saul, J. Asirra: A CAPTCHA that exploits interest-aligned manual image categorization. CCS

2007, 7, 366–374.

106. Krizhevsky, A.; Hinton, G. Learning Multiple Layers of Features from Tiny Images; University of Toronto: Toronto, ON, Canada, 2009.
107. Xu, W.; Huang, L.; Fox, A.; Patterson, D.; Jordan, M.I. Detecting large-scale system problems by mining console logs. In
Proceedings of the ACM SIGOPS 22nd Symposium on Operating Systems Principles, Big Sky, MT, USA, 11–14 October 2009;
ACM Press: New York, NY, USA, 2009.

108. Sharafaldin, I.; Lashkari, A.H.; Ghorbani, A.A. Toward generating a new intrusion detection dataset and intrusion trafﬁc
characterization. In Proceedings of the International Conference on Information Systems Security and Privacy, Funchal, Portugal,
22–24 January 2018; pp. 108–116.

109. Pang, G.; Shen, C.; Cao, L.; Hengel, A.V.D. Deep learning for anomaly detection: A review. ACM Comput. Surv. 2021, 54, 1–38.

[CrossRef]

110. Ganaie, M.A.; Hu, M.; Malik, A.; Tanveer, M.; Suganthan, P. Ensemble deep learning: A review. Eng. Appl. Artif. Intell. 2022, 115,

105151. [CrossRef]

---

<!-- PAGE 27 -->

Appl. Sci. 2023, 13, 6515

27 of 27

111. Yang, W.; Li, Z.; Liu, M.; Lu, Y.; Cao, K.; Maciejewski, R.; Liu, S. Diagnosing concept drift with visual analytics. In Proceedings of
the IEEE Conference on Visual Analytics Science and Technology (VAST), Salt Lake City, UT, USA, 25–30 October 2020; pp. 12–23.
112. Stiglic, G.; Kokol, P. Interpretability of Sudden Concept Drift in Medical Informatics Domain. In Proceedings of the IEEE 11th

International Conference on Data Mining Workshops, Vancouver, BC, Canada, 11–14 December 2011; pp. 609–613. [CrossRef]

Disclaimer/Publisher’s Note: The statements, opinions and data contained in all publications are solely those of the individual
author(s) and contributor(s) and not of MDPI and/or the editor(s). MDPI and/or the editor(s) disclaim responsibility for any injury to
people or property resulting from any ideas, methods, instructions or products referred to in the content.

<!-- MARKITDOWN CONVERSION -->

<!-- Full MarkItDown conversion for formatting fidelity. -->

applied
sciences
Review
Concept Drift Adaptation Methods under the Deep Learning
Framework: A Literature Review
QiuyanXiang ,LinglingZi*,XinCongandYanWang
CollegeofComputerandInformationScience,ChongqingNormalUniversity,Chongqing401331,China
* Correspondence:lingling19812004@126.com
Abstract:Withtheadventofthefourthindustrialrevolution,data-drivendecisionmakinghasalso
becomeanintegralpartofdecisionmaking. Atthesametime, deeplearningisoneofthecore
technologiesofthefourthindustrialrevolutionthathavebecomevitalindecisionmaking.However,
intheeraofepidemicsandbigdata,thevolumeofdatahasincreaseddramaticallywhilethesources
havebecomeprogressivelymorecomplex,makingdatadistributionhighlysusceptibletochange.
Thesesituationscaneasilyleadtoconceptdrift,whichdirectlyaffectstheeffectivenessofprediction
models.Howtocopewithsuchcomplexsituationsandmaketimelyandaccuratedecisionsfrom
multiple perspectives is a challenging research issue. To address this challenge, we summarize
conceptdriftadaptationmethodsunderthedeeplearningframework,whichisbeneficialtohelp
decisionmakersmakebetterdecisionsandanalyzethecausesofconceptdrift.First,weprovidean
overallintroductiontoconceptdrift,includingthedefinition,causes,types,andprocessofconcept
driftadaptationmethodsunderthedeeplearningframework.Second,wesummarizeconceptdrift
adaptationmethodsintermsofdiscriminativelearning,generativelearning,hybridlearning,and
others.Foreachaspect,weelaborateontheupdatemodes,detectionmodes,andadaptationdrift
typesofconceptdriftadaptationmethods.Inaddition,webrieflydescribethecharacteristicsand
applicationfieldsofdeeplearningalgorithmsusingconceptdriftadaptationmethods.Finally,we
summarizecommondatasetsandevaluationmetricsandpresentfuturedirections.
Keywords: deep learning; time-series analysis; concept drift; data-driven decision making;
Citation:Xiang,Q.;Zi,L.;Cong,X.; discriminativelearning;generativelearning;hybridlearning;deepreinforcementlearning;deep
Wang,Y.ConceptDriftAdaptation
transferlearning
MethodsundertheDeepLearning
Framework:ALiteratureReview.
Appl.Sci.2023,13,6515. https://
doi.org/10.3390/app13116515
1. Introduction
AcademicEditors:PaoloRenna,
The2019outbreakofcoronavirusdisease(COVID-19)hasdistincteffectsonpeople’s
AsadMasoodKhattak,RahmanAli
healthandqualityoflife,andthereisgreatuncertaintyregardingtheoutbreak’sevolution,
andFarkhundIqbal
duration,andscopeinthefuture. So,inthiseraoftheepidemicandbigdata,decision
Received:23February2023 makersfaceaseriesofproblems,suchasextensivedatabases,rapidgrowth,diversified
Revised:29April2023 datasources,andrapidchangesindatadistribution.Atpresent,deeplearningtechnologies
Accepted:24May2023 cansolvepartoftheproblemsandprovidepartoftheguidancetodecisionmakers[1].
Published:26May2023 However, it does not adapt well to the changing environment. Once the environment
changes,thenewdatadoesnotmatchthedistributionoftheolddata. Withconceptdrift
occurring[2],thedeeplearningmodelwillbecomeobsoleteandinvalid. Howtodealwith
thiscomplexsituationandmaketimelyandaccuratedecisionsfrommultipleperspectives
Copyright: © 2023 by the authors.
isachallengingresearchproblem. Conceptdriftadaptationmethodsofferthepossibilityof
Licensee MDPI, Basel, Switzerland.
solvingtheproblem[3],helpingdecisionmakerstofindtheoptimalormostsatisfactory
This article is an open access article
solutioninthisdynamicandcomplexsituation. Thesemethodscancontinuouslycapture
distributed under the terms and
thepotentialdangerofeventsbyanalyzingthedatastream,dealwithdistributionchanges
conditionsoftheCreativeCommons
inthedatastreamontime,andhelpdecisionmakersupdateexistingdecisionresultsto
Attribution(CCBY)license(https://
preventlossesduetodecisionmaking.
creativecommons.org/licenses/by/
4.0/).
Appl.Sci.2023,13,6515.https://doi.org/10.3390/app13116515 https://www.mdpi.com/journal/applsci

Appl.Sci.2023,13,6515 2of27
Conceptdriftadaptationmethodscanbeappliedinvariousfields. Bycontinuously
upgradingthelearningmodeltoensureitscorrectnessandtimeliness,theycanprovide
accuratepredictioninformationfordecisionmakers. Atthesametime,theycanperform
activedetectionincombinationwithdetectionalgorithms,whichprovidesdecisionmakers
withknowledgeofdynamicconcepts[4],andanalyzetheconceptdriftthatisoccurring.For
example,intheinformationsecurityfield,improvedlongshort-termmemory(I-LSTM)[5]
caneffectivelydetectnetworkanomalies,analyzethecauses,andstrengthenprotection.
Inthefinancialinvestmentfield,DeepBreath[6]caneffectivelyminimizeinvestmentrisk,
andithasbeenexperimentallyproventoobtainbetterinvestmentreturnsthancurrent
expertinvestmentstrategies. Inaddition,inthefieldofcustomerbehavioranalysisandair
qualitydetection,ConceptExplorer[7],whichcombinedconceptdriftwithvisualization,
canhelpdecisionmakerstoconductintuitiveexplorationandprovideabasisforexperts
tomakesubsequentdecisions. Therefore,conceptdriftadaptationmethodscaneffectively
helpdecisionmakersdeterminethemaininfluencingfactors,updatetheirunderstanding
ofpotentialrelationships,understandthenatureofthedata,findpotentialdangers,and
makecorrectdecisions.
Duetotheimportantroleofconceptdriftadaptationmethodsinapplications,many
researchershavereviewedthemfromdifferentperspectives. Forexample,withinnearly
10years,Hoensetal.[8]reviewedconceptdriftdetectionmethodsandsummarizedthe
problemofclassimbalanceinthedatastream. YMetal.[9]reviewedtheclassificationprob-
lemfromtheperspectiveofasinglemodelandanensemblemodel.Gamaetal.[4]reviewed
conceptdriftadaptionmethodsfromfouraspects: memoryusage,conceptdriftdetection,
modelupdatemethod, andmodelevaluationindex. Dtizleretal.[10]reviewedtheex-
istingconceptdriftdetectionmethodsfromtwoaspects: activemodeandpassivemode.
Webbetal.[11]mainlyinvolvedvarioustypes,suchasdrifttarget,drifttransitionmode,
anddriftamount,andexplainedtheirspecificdefinitions. Krawczyketal.[12]reviewed
ensemblelearningindatastreamclassificationandregressiontasks. Kamassietal.[13]
summarizedconceptdriftadaptionmethodsfromtheaspectsofdataprocessing,adap-
tationmode,andthenumberofclassifiers. Luetal.[14]comprehensivelysummarized
when drift occurs, to what extent, and how long it lasts, as well as the category imbal-
anceintheclassificationofconceptdriftdatastreams,bigdatamining,anddata-driven
decisionsupportsystems. Ghanietal.[15]mainlyintroducedconceptualdriftdetection
methodsforuntaggeddatastreams. Limaetal.[16]summarizedandclassifiedconcept
driftadaptationmethodsbasedondifferentmachinelearningmodelsundertheregression
task. Bayrametal.[17]classifiedandreviewedtheexistingdetectionalgorithmsofconcept
drift adaptation methods. However, to the best of our knowledge, there is no detailed
introductionandsummaryofconceptdriftadaptationmethodsunderthedeeplearning
framework. Therefore,thispaperexplorestheimportantroleofconceptdriftadaptation
methodsunderthedeeplearningframework.
Themaincontributionsofthispapercanbesummarizedasfollows:
(1) We review concept drift adaptation methods under the deep learning framework
fromfouraspects—discriminativelearning,generativelearning,hybridlearning,and
relevantothers—soastofillthegapinthisareaofinvestigationinpreviouswork.
(2) Werevealthegeneraloperationprocessofconceptdriftadaptivemethodsunderdeep
learningframeworksandexplainconceptdriftdetectionmodesandupdatemodes
indetail.
(3) Wesummarizetherepresentativealgorithmsofeachsubcategory,commondatasets,
evaluationmetrics,theirapplicationareas,andlimitations.
(4) Weanalyzeanddiscussthecurrentproblemsofconceptdriftadaptionmethodsand
pointoutthefuturedirection.
Therestofthepaperisstructuredasfollows. Section2providesthedefinition,causes,
andtypesofconceptdriftandintroducestheprocessofconceptdriftadaptationmethods
underthedeeplearningframework. Section3classifiesconceptdriftadaptationmethods
based on deep learning and reviews the existing methods in the literature. Section 4

Appl.Sci.2023,13,6515 3of27
summarizes the common datasets and evaluation metrics. Section 5 provides future
research,andSection6concludesthispaper.
2. OverviewofConceptDrift
Inthissection,weintroducethedefinitionandcausesofconceptdrift,differenttypes
ofconceptdrift,andtheprocessofconceptdriftadaptationmethods.Conceptdriftwasfirst
proposedbySchlemmeretal.[2]in1986andmainlyreferstothefactthattheunderlying
datastreamdistributionchangesovertime[18,19].
2.1. TheDefinitionofConceptDrift
Assuming that P represents the joint probability distribution between the input
t0
variable x and the target variable y at time t and P represents the joint probability
0 t1
distributionbetweenthexandyatt ,thenconceptdriftwilloccurifEquation(1)holds
1
whent turnstot .
0 1
∃x: P (x,y) (cid:54)= P (x,y) (1)
t0 t1
Atthistime,theunderlyingdatadistributionnolongerconformstoconceptC ,andanew
1
conceptC isgenerated.DuetothecharacteristicsofjointprobabilityP(x,y)=P(x)P(y|x)
2 t t t
ifEquation(2)issatisfiedwhent turnstot ,conceptdriftwillalsooccur.
0 1
∃x: P (x)P (y|x) (cid:54)= P (x)P (y|x) (2)
t0 t0 t1 t1
ChangesinbothP (x)andP (y|x)canleadtoconceptdrift.
t t
2.2. TheCausesofConceptDrift
Accordingtothedefinitionofconceptdriftandthecharacteristicsofjointprobability,
itcanhavethefollowingthreecauses:
(1) Virtualconceptdrift. Whentheprobabilityofxchanges,buttheprobabilityofyunder
theconditionofxdoesnotchange,i.e.,P (x)(cid:54)=P (x)andP (y|x)=P (y|x). This
t0 t1 t0 t1
casebelongstovirtualconceptdrift,whichdoesnotaffectitsdecisionboundaryand
onlychangesthefeaturespace.
(2) Realconceptdrift. Whentheprobabilityofyundertheconditionofxchanges,the
probabilityofxremainsthesame,i.e.,P (y|x)(cid:54)=P (y|x)andP (x)=P (x). This
t0 t1 t0 t1
casehasadirectimpactonthepredictionmodelandisarealconceptdrift,whichnot
onlychangesthefeaturespacebutalsochangesitsdecision-makingboundary.
(3) Hybridconceptdrift. Inanopenenvironment, bothrealconceptdriftandvirtual
concept drift can exist in the data stream at the same time, i.e., P (x) (cid:54)= P (x),
t0 t1
P (y|x)(cid:54)=P (y|x).Thisisamixedconceptdrift,whichismostcommon.
t0 t1
It is worth noting that according to the Bayesian decision theory [20], we obtain
Equation(3):
P(y)∗P(x|y)
P(y|x) = (3)
P(x)
ItcanbeseenthatP (y)andP (x|y)alsoaffectP (y|x),thusindirectlycausingareal
t t t
conceptdrift. Thespecificmanifestationsoftheconceptdriftduetodifferentcausesare
showninFigure1,inwhich(X ,X )representsthetwo-digitfeaturespaceandyrepresents
1 2
itscategorylabel.
For example, in stock trading, users can be divided into profitable and non-profit
stocksaccordingtoprofitability. Whenauserconsiderspurchasingstocks, achangein
thechannelofpurchaseorasmallchangeinthenumberofpurchasesdoesnotaffectthe
trendofthestock. However,ifaffectedbyanoutbreak,thetrendofstocksmaychange,
thus directly affecting stock returns. This situation belongs to the real concept drift, so
usersneedtoreconsiderandmakedecisions. Inreallife,virtualdrifttendstohaveless
impactontheoutcomeofadecision. Therewillbenolosstodecisionmakers. However,
realconceptdrifttendstohaveadirectimpactondecisionoutcomesduetochangesinits

Appl. Sci. 2023, 13, x FOR PEER REVIEW 4 of 28
Appl.Sci.2023,13,6515 4of27
Appl. Sci. 2023, 13, x FOR PEER REVdIEaWta relationships. Itrequiresdecisionmakerstodiscoverintimeandre-makedecisio4n soft o28
avoidlosses.
Figure 1. The causes of concept drift.
For example, in stock trading, users can be divided into profitable and non-profit
stocks according to profitability. When a user considers purchasing stocks, a change in the
channel of purchase or a small change in the number of purchases does not affect the trend
of the stock. However, if affected by an outbreak, the trend of stocks may change, thus
directly affecting stock returns. This situation belongs to the real concept drift, so users
need to reconsider and make decisions. In real life, virtual drift tends to have less impact
on the outcome of a decision. There will be no loss to decision makers. However, real
concept drift tends to have a direct impact on decision outcomes due to changes in its data
relationships. It requires decision makers to discover in time and re-make decisions to
avoid losses.
FFigiguurere1 1..T Thheec caauusesesso offc oconnceceppttd drirfitf.t.
2.3. The Types of Concept Drift
2.3. TheTypesofConceptDrift
For example, in stock trading, users can be divided into profitable and non-profit
The changes in concept may manifest in different forms over time. At present, the
stocTksh eaccchoarndginegs tion pcroonficteapbtilmitya.y Wmhaenni fae ustseinr cdoinffseirdeenrts fpourmrchsaosvinerg tsitmocek.sA, at cphraensegnet i,nt hthee
most popular types of concept drift can be divided into abrupt drift, incremental drift,
mchosatnpneolp oufl parurtcyhpaesseo ofr cao snmceapllt cdhrainftgeca inn tbhee dniuvmidbeedr oinf tpouarbchruapsetsd droifets, ninoctr aeffmeecnt ttahle dtrreifntd,
gradual drift, and recurring drift [14,16,17].
goraf dthuea lsdtorcifkt,. aHnodwreevcuerr,r iinf gaffdericftte[d1 4b,1y6 a,1n7 ]o.utbreak, the trend of stocks may change, thus
A A b b r r u u p p t t d d r r i i f f t t r r e e f f e e r r s s t t o o t t h h e e r r a a p p i i d d c c h h a a n n g g e e o o f f c c o o n n c c e e p p t t C C1 i i n n t t o o c c o o n n c c e e p p t t C C2 i i n n a a s s h h o o r r t t p p e e r r i i o o d d
directly affecting stock returns. This situation belongs1 to the real conc2ept drift, so users
of time, and if an earthquake suddenly occurs in a certain place, its economic model
oftime,andifanearthquakesuddenlyoccursinacertainplace,itseconomicmodelchanges
need to reconsider and make decisions. In real life, virtual drift tends to have less impact
changes instantaneously, as shown in Figure 2a. Incremental drift refers to the slow trans-
instantaneously,asshowninFigure2a. Incrementaldriftreferstotheslowtransformation
on the outcome of a decision. There will be no loss to decision makers. However, real
foofrmcoantcioepn toCf coinntcoepcot nCc1 einpttoC coinncaepcto Cn2t iinnu ao cuosnmtinanunoeurs, masatnhneeerc, oans othmey ecgorandoumayll ygrraedcuovalelrys
concept drif1t tends to have a2 direct impact on decision outcomes due to changes in its data
raefctoervearnse aafrttehrq auna ekaer,tahsqsuhaokwen, aisn sFhiogwurne i2nb .FGigruardeu 2abl.d Grirfatdreufaelr sdtroifat rsehfoerrts ptoer aio sdhoorftt ipmeeri:oCd
relationships. It requires decision makers to discover in time and re-make decisions t1o
oafn tdimCe: rCep1 aeantde dCl2y rsewpeitacthedanlyd sewveitncthu aanlldy setvaebniltiuzaelalyt Csta,baislitzhee aetq Cu2i,p ams ethnet aegqeusi,pomcceanstio angaelsly,
avoid2 losses. 2
ofaccilass,iaonndalfilyn afalliylss, taonpds wfinoarklliyn sgt,oapsss whoowrknining,F aigs usrheo2wc.nR inec Fuirgruinrge 2dcr.i fRterecfuerrrsintog tdhreiffta rcetftehrast
toov tehret ifmacet, tthhaetp orveverio tuimsceo, nthceep ptrwevililoruesa pcpoenacrepaftt ewriall preearipopdeoafr taimfteer; fao rpeexriaomd polfe ,ttimhees; afloers
2.3. The Types of Concept Drift
eoxfadmopwlen, jtahcek esatslems eoeft dcoowncne pjatcCke
1
tisn mtheeetw cionntecer,pstt aCr1t itno tehnet ewritnhteero,f fs-tsaerat stoon eanftteerr tthhee oenffd-
The changes in concept may manifest in different forms over time. At present, the
soefatshoen wafitnerte trh,et heenidr osaf ltehse wwiilnltmere, ethteciorn scaelepst wCi
2
l,l amnedett hcoennctehpet nCe2,x atnwdi nthteenr cthoen cneepxtt Cw
1
inwteirll
most popular types of concept drift can be divided into abrupt drift, incremental drift,
croenacpeppeta Cr,1a wsislhl orewanppineaFri, gaus rseh2odw.nI nina dFidgiutiroen 2,dth. eIns padeedditioofnr,e tchuer rsipnegedd roifft rceacnurbreinagb druripftt ,
gradual drift, and recurring drift [14,16,17].
cgarna dbue aalb,rourpint,c greramdeunatla, lo.rI tincacnreamlseonbtael.p Iet rciaond iaclsoor ibrer epgeurliaord.ic or irregular.
Abrupt drift refers to the rapid change of concept C1 into concept C2 in a short period
of time, and if an earthquake suddenly occurs in a certain place, its economic model
changes instantaneously, as shown in Figure 2a. Incremental drift refers to the slow trans-
formation of concept C1 into concept C2 in a continuous manner, as the economy gradually
recovers after an earthquake, as shown in Figure 2b. Gradual drift refers to a short period
of time: C1 and C2 repeatedly switch and eventually stabilize at C2, as the equipment ages,
occasionally fails, and finally stops working, as shown in Figure 2c. Recurring drift refers
to the fact that over time, the previous concept will reappear after a period of time; for
Figure2.Thetypesofconceptdrift.
Fiegxuarme 2p. lTeh, et htyep seasl oefs coofn cdeopwt dnr ijfat.c kets meet concept C1 in the winter, start to enter the off-
seas I o n n t a h f e te a r c t a h d e e e m nd ic o r f e t s h e e a w rc i h nt o e f r, c t o h n e c ir e s p a t le d s r w ift i , ll t m he ee ty t c p o e n s c a e r p e t C di2f , f a e n re d n t t he a n cc t o h r e d n in e g xt t w o i t n h t e er
In the academic research of concept drift, the types are different according to the clas-
cclaosnscifiepcat tCio1n wcirlilt reeraiap.pHeaorw, eavs esrh,oitwisnc ionm Fmigounret o2dd.i vInid aedtdhietitoynp, etsheo fscpoenecde opft sreaccucorrridnign gdrtoift
sification criteria. However, it is common to divide the types of concepts according to their
thcaenir btrea anbsrfourpmt, agtrioadnus,aal,n odr tihnicsrcermiteenritaalm. Iat nciafnes atlastoio bnei psemrioordeicin otur iitrirveeg.uIlnarr.e latedstudies,
transformations, and this criteria manifestation is more intuitive. In related studies, dif-
differentmethodsadapttosolvingdifferenttypesofconceptdrift. Forexample,thedrift
ferent methods adapt to solving different types of concept drift. For example, the drift
detection method (DDM) algorithm [21] is more suitable for abrupt drift. In addition
detection method (DDM) algorithm [21] is more suitable for abrupt drift. In addition to
to adapting the four common types above, there are some methods for distinguishing
real drift and virtual drift, avoiding mixing with virtual concept drift or outliers and
noise. Forexample,theRRBM–DD[22]considersexplicitlyhowtoidentifythedriftof
the real concept. Although concept drift adaptation methods cannot solve all types of
conceptdriftatonetime,theycanstillsolvemultipleconceptdrifts,whichbelongstoa
one-to-manyrelationship.
Figure 2. The types of concept drift.
In recent years, there have also been many excellent concept drift detection algo-
rithmstodetectmultipleconceptdrifts,forexample,basedonsliding-windowalgorithms,
In the academic research of concept drift, the types are different according to the clas-
OCDD[23],CDT_MSW[24],andKSWIN[25]. OCDDmainlyhastwoslidingwindows
sification criteria. However, it is common to divide the types of concepts according to their
transformations, and this criteria manifestation is more intuitive. In related studies, dif-
ferent methods adapt to solving different types of concept drift. For example, the drift
detection method (DDM) algorithm [21] is more suitable for abrupt drift. In addition to

Appl.Sci.2023,13,6515 5of27
tostorenewandolddata,andthepercentageofoutliersdetectedbytheclassifierinthe
slidingwindowisusedtosendadriftsignal,whichismoresuitablefordetectingabrupt
andincrementaldrift,buthyperparametersettingsarerequired. CDT_MSWalsohastwo
windows,thedifferencebeingthatitcanidentifythepositionandlengthofconceptdrift,so
astoaccuratelydeterminethetypeofconceptdrift. KSWINdetectsconceptdriftbyapply-
ingthe“Kolmogorov–Smirnovtest”. Thesealgorithmsarebasedonsupervisedlearning.
UnsupervisedconceptdriftalgorithmsincludeLD3[26],STUDD[27],andCDCMS[28].
LD3introducestheconceptoflabel-dependentorderingforconceptdriftdetectioninmulti-
label classification, which is more suitable for mutation and incremental drift. STUDD
mainly creates an auxiliary model (students) to mimic the behavior of the main model
(teacher),usestheteachertopredictnewinstances,andmonitorsthestudent’simitation
losstodetectconceptdrift. Itismoresuitableforabrupt,gradual,andincrementaldrift.
CDCMSmainlyusesnovelclusteringanddiversity-basedmemorymanagementstrate-
giesinmodelspacestrategiestodealwithconceptdriftandhasgoodeffectsindealing
withabruptandrecurringdrift. Finally,itisworthmentioningthatmostoftheconcept
drift detection algorithms either occupy more memory or have a slow detection speed.
DMDDM[29]isbasedonthePage–Hinkleytest,whicheffectivelyimprovesthedetection
speedofconceptdriftandovercomesthelimitationsofcostandexecutiontimebutisonly
suitable for abrupt drift. How to achieve a cost-saving detection algorithm that covers
alldrifttypesisalsoamajorchallenge. Therefore,wewillalsosummarizethetypesof
conceptualdriftforeachmethod.
2.4. TheProcessofConceptDriftAdaptationMethodsunderDeepLearningFramework
Thegeneraladaptationprocessofconceptdriftunderthedeeplearningframework
whendealingwithunstablestatedatastreamsisshowninFigure3. First,thedatastream
input(singleinputorbatchinput)isgenerallytrainedandlearnedbythedeeplearning
model (single model or ensemble model) to obtain the basic prediction results. Next,
if concept drift occurs during this process, a concept drift adaptation method will be
triggeredtoupdatethedeeplearningmodeltoaccommodateconceptdriftandmaintain
the model [16,19]. The concept drift adaptation method can be divided into two parts:
conceptdriftdetectionandmodelupdate. Amongthem,conceptdriftdetectioncontains
Appl. Sci. 2023, 13, x FOR PEER REVIEW 6 of 28
bothactiveandpassivemodes,andmodelupdatescanbedividedintostructureupdates
andparameterupdates.
FigFuigruer3e. 3T. hTeheg geenneerraallp prroocceessss ooff ccoonncceepptt ddrrifitf taaddapatpattaiotino nmmetheothdos dusnudenrd deeredpe leeparlneianrgn firnagmferwamorekw. ork.
Active modes mean that the learning process of a deep learning model contains a
concept drift detection algorithm. When concept drift is detected, the concept drift adap-
tation method will be triggered to update the model. Passive mode means that the method
continuously adjusts its model as data are continuously input during the learning process.
Instead of using a drift detection algorithm, it uses a concept drift adaptation method to
passively update the model continuously. After triggering the concept drift application
mechanism, the deep learning model is generally updated to adapt to the concept drift
through a model parameter update or a structure update [30]. Model parameter updates
can be divided into full parameter updates and partial parameter updates. In particular,
parameter updates also include parameter updates between ensemble models. Here, pa-
rameter updates are also weight updates. In addition, model structure updates can gen-
erally be performed by adjusting the width and depth of the network.
3. Concept Drift Adaptation Methods under Deep Learning
In this section, we will summarize concept drift adaptation methods according to the
classification of deep learning [31], including discriminative learning, generative learning,
hybrid learning, and others, as shown in Figure 4. For each part, we will explain the up-
date modes, types of drift adapted, and detection modes. In addition, we will also intro-
duce the characteristics and application fields of deep learning techniques using concept
drift adaptation methods.

Appl.Sci.2023,13,6515 6of27
Activemodesmeanthatthelearningprocessofadeeplearningmodelcontainsacon-
ceptdriftdetectionalgorithm. Whenconceptdriftisdetected,theconceptdriftadaptation
methodwillbetriggeredtoupdatethemodel. Passivemodemeansthatthemethodcontin-
uouslyadjustsitsmodelasdataarecontinuouslyinputduringthelearningprocess.Instead
ofusingadriftdetectionalgorithm,itusesaconceptdriftadaptationmethodtopassively
updatethemodelcontinuously. Aftertriggeringtheconceptdriftapplicationmechanism,
thedeeplearningmodelisgenerallyupdatedtoadapttotheconceptdriftthroughamodel
parameterupdateorastructureupdate[30]. Modelparameterupdatescanbedividedinto
fullparameterupdatesandpartialparameterupdates. Inparticular,parameterupdates
alsoincludeparameterupdatesbetweenensemblemodels. Here,parameterupdatesare
alsoweightupdates. Inaddition,modelstructureupdatescangenerallybeperformedby
adjustingthewidthanddepthofthenetwork.
3. ConceptDriftAdaptationMethodsunderDeepLearning
Inthissection,wewillsummarizeconceptdriftadaptationmethodsaccordingtothe
classificationofdeeplearning[31],includingdiscriminativelearning,generativelearning,
hybridlearning,andothers,asshowninFigure4. Foreachpart,wewillexplaintheupdate
modes,typesofdriftadapted,anddetectionmodes. Inaddition,wewillalsointroduce
Appl. Sci. 2023, 13, x FOR PEER REVIEW 7 of 28
thecharacteristicsandapplicationfieldsofdeeplearningtechniquesusingconceptdrift
adaptationmethods.
Figure 4. A taxonomy of concept drift adaption under deep learning framework.
Figure4.Ataxonomyofconceptdriftadaptionunderdeeplearningframework.
33..11.. CCoonncceepptt DDrriifftt AAddaappttaattiioonn MMeetthhooddss BBaasseedd oonn DDiissccrriimmiinnaanntt LLeeaarrnniinngg
TThhiiss ttyyppee ooffd deeeeppl elaeranrnininggte tcehcnhinqiuqeuies iuss uedseidn sinu pseurpveisrvediseodr colar scsliafiscsaitfiiocantiaopnp laipcaptliiocnas-
tbiyondse bscyr idbeisncgritbhinegp tohsete prioosrtedriisotrr idbiusttrioibnustioofncso onfd ciotinodnietdionveisdi bvliesidbaleta d.aAta.d Ais cdriismcriinmaitnivae-
tive model is a model that learns the relationship between input data and output labels,
and it predicts output labels by learning the characteristics of the input data. In classifica-
tion problems, the main purpose is to assign each input vector a to label b. Discriminant
models attempt to directly learn the function f(a) that maps input vectors to labels. The
classifier first learns the posterior class probability P(b = k|a) from the training data and
assigns a new sample a to the class with the highest posterior probability based on these
probabilities, where k stands for class. The general process of the discriminant concept
drift adaption method is shown in Figure 5, while the two methods of active detection and
parameter update mode account for a relatively large proportion. Discriminant learning
mainly includes multilayer perceptrons (MLPs), convolutional neural networks (CNNs),
recurrent neural networks (RNNs), and their variants.

Appl.Sci.2023,13,6515 7of27
modelisamodelthatlearnstherelationshipbetweeninputdataandoutputlabels,and
itpredictsoutputlabelsbylearningthecharacteristicsoftheinputdata. Inclassification
problems,themainpurposeistoassigneachinputvectoratolabelb. Discriminantmodels
attempttodirectlylearnthefunctionf(a)thatmapsinputvectorstolabels. Theclassifier
firstlearnstheposteriorclassprobabilityP(b=k|a)fromthetrainingdataandassignsa
newsampleatotheclasswiththehighestposteriorprobabilitybasedontheseprobabilities,
wherekstandsforclass. Thegeneralprocessofthediscriminantconceptdriftadaption
methodisshowninFigure5,whilethetwomethodsofactivedetectionandparameter
Appl. Sci. 2023, 13, x FOR PEER REVIuEWpd ate mode account for a relatively large proportion. Discriminant learning m8 aoifn l2y8
includesmultilayerperceptrons(MLPs),convolutionalneuralnetworks(CNNs),recurrent
neuralnetworks(RNNs),andtheirvariants.
Figure 5. The general process of concept drift adaptation methods based on discriminant learning.
Figure5.Thegeneralprocessofconceptdriftadaptationmethodsbasedondiscriminantlearning.
• • MMLLPP--bbaasseedd ccoonncceepptt ddrriifftt aaddaappttaattiioonn mmeetthhooddss
MLP is a discriminant learning model widely adopted in decision making [32], which
MLPisadiscriminantlearningmodelwidelyadoptedindecisionmaking[32],which
is often used in combination with concept drift adaptation methods to solve classification
isoftenusedincombinationwithconceptdriftadaptationmethodstosolveclassification
problems for unstable streaming data. However, concept drift adaptation methods are
problems for unstable streaming data. However, concept drift adaptation methods are
computationally expensive and converge slowly each time the model is updated due to
computationallyexpensiveandconvergeslowlyeachtimethemodelisupdateddueto
the hyperparameter problem. Typical algorithms, such as selective ensemble-based online
thehyperparameterproblem. Typicalalgorithms,suchasselectiveensemble-basedonline
adaptive deep neural networks (SEOAs), bilevel online deep learning (BODL), neural net-
adaptive deep neural networks (SEOAs), bilevel online deep learning (BODL), neural
works with dynamically evolved capacity (NADINEs), and Adadelta optimizer-based
networkswithdynamicallyevolvedcapacity(NADINEs),andAdadeltaoptimizer-based
ddeeeepp nneeuurraall nneettwwoorrkkss wwitihth ccoonnceceppt tddrirfitf tdedteetcetciotino n(C(ICDIDD-DA-DAODDONDNNsN),s a),rea reelaebloabraotreadt eads
afoslfloolwlosw. s.
SSEEOOAA [[3333]] uusseess aa ddeeeepp lleeaarrnniinngg mmooddeell wwiitthh LL nneettwwoorrkk llaayyeerr MMLLPPss ttoo ffoorrmm LL bbaassiicc
ccllaassssiififieerrss.. IItt tthheenn ddyynnaammiiccaallllyy aaddjjuussttss tthhee ppaarraammeetteerrss ooff eeaacchh bbaassiicc ccllaassssiififieerr ttoo hhaannddllee
ccoonncceepptt ddrriifftt aanndd rreegguullaarrllyy sseelleeccttss bbaassee ccllaassssiififieerrss wwiitthh ddiiffffeerreenntt ccoonnvveerrggeennccee aanndd fifittttiinngg
aabbiilliittiieess.. ItI tenenhhanancecse sthteh eadaadpatpabtaibliitlyit aynadn gdengeernaelrizaalitzioatni oanbialibtyil iotyf tohfe tmheodmelo dtoe ldtaotad daitsa-
dtriisbturitbiounti,o wn,hwichhi cihs imsomroe rseusiutaitbalbe lfeofro grrgardaudaula, li,nincrceremmeenntatal,l ,aanndd rreeccuurrrriinngg ddrriifftt,, aalltthhoouugghh
lleessss ssuuiittaabbllee ffoorr ddeeaalliinngg wwiitthh hhiigghh--ddiimmeennssiioonnaall nnoonn--lliinneeaarr pprroobblleemmss.. BBOODDLL [[3344]] mmaaiinnllyy
uusseess tthhee MMLLPP mmooddeell ffoorr ccllaassssiifificcaattiioonn pprreeddiiccttiioonn aanndd ddeetteeccttss ccoonncceepptt ddrriifftt bbaasseedd oonn tthhee
ccllaassssiififieerr’’ss eerrrroorr rraattee.. WWhheenn ccoonncceepptt ddrriifftt iiss ddeetteecctteedd,, tthhee mmooddeell’’ss ppaarraammeetteerrss aarree uuppddaatteedd
tthhrroouugghh aa bbiilleevveell ooppttiimmiizzaattiioonn ssttrraatteeggyy aanndd tthhee eexxppoonneennttiiaall ggrraaddiieenntt ddeesscceenntt mmeetthhoodd ttoo
aaddaapptt ttoo tthhee aabbrruupptt ccoonncceepptt ddrriifftt,, bbuutt iittss lliimmiittaattiioonn iiss tthhaatt tthhee aaddddeedd ccllaasssseess ccaannnnoott bbee
iiddeennttiififieedd oonnlliinnee.. IInn ccoonnttrraasstt,, tthhee ccoonnvveerrggeennccee ssppeeeedd ooff tthhee aallggoorriitthhmm ffoorr mmooddeell ssttrruuccttuurree
uuppddaattee ccaann bbee sslloowweerr.. NNAADDIINNEE [[3355]] uusseess aa ddrriifftt ddeetteeccttiioonn mmeecchhaanniissmm ttoo ddeetteecctt ccoonncceepptt
ddrriifftt aaccttiivveellyy.. TThheed drrifitftd deetetectcitoionnm mecehcahnainsimsmm maianilnylyad addsdasn aand aadpatipvteivwe iwndinodwoinwginsgtr astteragty-
teogyth teop trhoem pirnoemntinHeonet fHfdoineffg’dsibnogu’sn bdoduentdec dtieotnecatligoonr aitlhgmor.itWhmhe. nWthheend rtihfte sdigrinfta lsiigsndaelt eisc tdeed-,
ittesctneedt,w itosr knesttwruocrtku rsetrwucitlulbree wupildl abtee duptodaatdedap ttot aodcaopntc teop tcodnrcifetp,wt dhriicfht, mwahiinchly madaijunlsyts aidts-
njuesttws oitrsk nsetrtwucotrukr esttrhurcotuugreh tthhreohuigdhd ethneu hniidtdgerno wuinnigt gsrtroawteingyg astnrdatehgidyd aenndu hniidtdpernu nuinnigt
sptrruanteignyg. sTtrhaetemgya.i nTahde vmanatiang aedovfaNntAagDeI NofE NoAveDrIoNtEh eorvaelrg oortihtherm aslgisoritisthemlass tiisc isttsr ueclatustriec
astnrducotunlrien aenldea ornnliinnge tlreaairtn,ibnugt ttrhaeit,t rbauint itnhge ttrimaineionfgt thimeme oofd tehlei smroedlaetli vise lryelsaltoivwe.lyIt scloawn.b Iet
acapnp lbieed atpopclileadss itfio ccaltaisosnifiacnadtioreng arensds iroengprersosbiolenm psr.oAbdledmitsi.o Anadldlyi,tisocnhaolllayr,s shchavoelarress heaarvceh reed-
istefaorrchceerdt aiti nfosrp ceecriatalidna stpa.ecCiaIDl dDa-tAa.D COIDDDN-NAD[3O6]DisNaNd o[3p6te] disf aodrothpetecdla fsosri fithcaet ciolanssmifiocdaetlioonf
highlyunbalanceddataflow,whichmainlyusesanadaptiveslidingwindow(ADWIN)
model of highly unbalanced data flow, which mainly uses an adaptive sliding window
drift detection algorithm to actively detect concept drift and then updates the network
(ADWIN) drift detection algorithm to actively detect concept drift and then updates the
network parameters through the Adadelta optimizer, so as to adapt to the abrupt and
gradual drift. This algorithm effectively improves the classification performance of highly
unbalanced data streams, although its feature selection needs to be optimized.
• RNN-based concept drift adaptation methods
Compared to other neural networks, RNN has certain advantages in processing se-
quence data because it has at least one feedback connection [37]. To some extent, it can
alleviate the problem of concept drift. However, its capacity is also limited, especially
when it comes to processing long data. It is mainly used in the fields of electricity loading,
weather forecasting, and anomaly detection. Typical algorithms are the online adaptive
recurrent neural network (OARNN), ONU-SHO-based RNN (ONU-SHO-RNN), adaptive

Appl.Sci.2023,13,6515 8of27
parametersthroughtheAdadeltaoptimizer,soastoadapttotheabruptandgradualdrift.
Thisalgorithmeffectivelyimprovestheclassificationperformanceofhighlyunbalanced
datastreams,althoughitsfeatureselectionneedstobeoptimized.
• RNN-basedconceptdriftadaptationmethods
Compared to other neural networks, RNN has certain advantages in processing
sequencedatabecauseithasatleastonefeedbackconnection[37]. Tosomeextent,itcan
alleviatetheproblemofconceptdrift. However,itscapacityisalsolimited,especiallywhen
itcomestoprocessinglongdata.Itismainlyusedinthefieldsofelectricityloading,weather
forecasting,andanomalydetection. Typicalalgorithmsaretheonlineadaptiverecurrent
neuralnetwork(OARNN),ONU-SHO-basedRNN(ONU-SHO-RNN),adaptivebehavioral-
based incremental batch learning malware variant detection model (AIBL-MVD), and
multilayerself-evolvingrecurrentneuralnetwork(MUSE-RNN).
OARNN[38]mainlyusestheRNNmodeltocapturethetemporalcorrelationandtrack
itsperformance. Whentheperformancedeteriorates,thetree-structuredParzenestimator
(TPE)willbeusedtooptimizethehyperparametersofthemodelonline. Then,theweights
oftheRNNmodelarecompletelyupdatedandrelearnedfromnewdatatoaccommodate
conceptdriftovershortperiodsoftime. Itismainlyusedforenergyandelectricityload
forecasting, although it requires a large amount of data for training and learning. In
addition,Jagaitetal.[39]proposedanonlineARIMA-RNNintegrationbasedonOARNN,
whichbelongstohybridlearning. Itwillbefurtherintroducedlater. ONU-SHO-RNN[40]
determineswhethertoupdatethemodelbycalculatingitspredictionaccuracyandthe
conceptdriftdetectionoftheRNNmodelonthedatastream. ItmainlyusestheONU-SHO
algorithm to perform a complete parameter update and narrow the error between the
target output and the measurement output. It is capable of fast convergence, adapting
to incremental and gradual drift, although there are problems with update delays. In
addition,AIBL-MVD[41]alsoadaptstoincrementalandgradualdrift. Itmainlyusesthe
statisticalprocesscontrol(SPC)algorithmtoactivelydetecttheoccurrenceofconceptdrift
andupdateallmodelweightsthroughincrementallearning. Itismainlyusedinthefield
of malware detection. In this process, the catastrophic forgetting problem is solved by
mixingthenewdatawithasubsetoftheolddata. Itslimitationisthatlabeledmalware
samplesmustbeavailablerightbeforeupdatingthemodel. Alloftheabovemethodsare
basedonparameterupdatemode. Subsequently,MUSE-RNN[42]mainlyusesstructural
updatestoupdatethemodels,anditactivelydetectsconceptdriftthroughHoeffding’s
bound detection algorithm, which is also a common method in concept drift detection
algorithms. Themodelisupdatedbyusinggrowthandpruninghiddennodesandlayers
forthereal-timeclassificationofdatastreams,althoughitdoesnothandleimagestreams.
• LSTM-basedconceptdriftadaptationmethods
Longshort-termmemory(LSTM)isavariantofRNNthatsolvesproblemssuchas
vanishinggradientsandissuitableforprocessingandforecastingimportanteventswith
relativelylongintervalsanddelaysintimeseries[43].LSTM-basedconceptdriftadaptation
methodsaremainlyusedinthefieldsofanomalydetection,photovoltaicpowergeneration
prediction, and industrial prediction, and their typical algorithms include DL-CIBuild,
I-LSTM,multi-objectivemetaheuristicoptimization-basedbigdataanalyticswithconcept
driftdetection(MOMBD-CDD),adaptiveLSTM(AD-LSTM),DCA-DNN,etc.
DL-CIBuild[44]isanalgorithmbasedontheLSTMmodeltoconstructprediction
models for continuous integration (CI) build outcome prediction. It uses the genetic
algorithm(GA)toadjustthehyperparameters(includingthenumberofhiddenlayersand
neurons)oftheLSTMmodel. Inparticular,itdoesnotrequireaverylargedatasetsizeand
hasgoodrobustness. However,thealgorithmisrelativelyexpensiveintermsoflaborand
requirestheconstructionofannotateddatasets. I-LSTM[5]combinestheideaoftimefactor
withstratifiedsampling. Therefore,thenewerthedata,thehighertheweightassignedto
accommodateconceptdrift,buttherearealsoproblemswithbalancingoldandnewdata.
Overall,itimprovesmulti-classificationperformanceforanomalydetection,mainlyfor

Appl.Sci.2023,13,6515 9of27
IoTapplications. MOMBD-CDD[45]mainlydealswithhigh-dimensionalstreamingdata.
ItmainlyusestheStatisticalTestofEqualProportionsmethod(STEPD)todetectconcept
drift and combines the glowworm swarm optimization (GSO) algorithm to update the
bidirectionallongshort-termmemory(Bi-LSTM)modelbyadjustingweights. However,it
ismorecomputationallyintensiveandtakesupmoreresources. Inthisprocess,STEPD
definestwowindows,arecentwindowrandanoverallwindowo. Thisisalsocommon
in deep-learning-based concept drift adaptation methods. It applies the statistical test
ofequalproportionstocomparetheaccuraciesbetweenthetwowindowsasshownin
Equations(4)and(5):
|v /n −v /n |−0.5×(1/n +1/n )
T(v o ,v r ,n o ,n r ) = o (cid:112) o r r o r (4)
µ+(1−µ)×(1/n +1/n )
o r
µ = (v +v )/(n +n ) (5)
0 r o r
Itsvalueiscomparedtothepercentileofthestandardnormaldistributiontoobtain
the observed significance level (p-value). p-value is equivalent to the chi-square test
with Yates’s continuity correction, in which v is the value of accurate predictions, and
n is the number of samples for the window. The calculation formula for µ is shown in
Equation(5). If p-value<αd, STEPD predicts a concept drift. If p-value < α , STEPD
w
predictsawarningthatconceptdriftmayoccur. α istheconceptdriftsignificancelevel;
d
α is the warning significance level. Fog-DeepStream [46] uses wavelet transform to
w
reduce the dimensionality of the data and LSTM models to predict future behavior for
datastreamanalysisonfogcomputing. Itusesadriftdetectionalgorithmtodetermine
theoccurrenceofconceptualdrift,andwhenaconceptualdriftisdetected,parameters
areupdatedtoaccommodatetheconceptualdrift. Themethodtriesthreedriftdetection
algorithms:cumulativesum(CUSUM),Page–Hinkley,andexponentiallyweightedmoving
average(EWMA).However,thisalgorithmalsotakesupalotofmemory.
TheabovealgorithmsareusedintheInternetfield. Next,weintroducealgorithms
in other fields. For example, AD-LSTM [47] is used for predicting photovoltaic power
generation. Itactivelydetectstheoccurrenceofconceptdriftthroughtheslidingwindow
(SDWIN)algorithmandadoptsthesecondstageofthetwo-phaseadaptivelearningstrategy
(TP-ALS)tofine-tunethepredictionmodel. DCA-DNN[48]ismainlyusedforindustrial
prognosis and is based on the LSTM-FC model, which actively detects the occurrence
ofconceptdriftthroughthedendriticcellalgorithm. Itgeneratessyntheticdatausinga
kerneldensityestimatorwithdrift-basedbandwidth,whichcanbeusedtofine-tunethe
weightsofthelastlayertoachievefasteradaptationandmitigatetheproblemoflimited
newsamples. Bothoftheabovealgorithmssufferfrommodelupdatedelays,andtheir
conceptdriftdetectionalgorithmsneedtobeoptimized.
• CNN-basedconceptdriftadaptationmethods
CNNisafeed-forwardneuralnetworkinwhichtheconnectionsbetweenneuronsin
itsconvolutionallayerarenotfullyconnected,andtheweightsandbiasesofconnections
betweensomeneuronsinthesamelayerareshared[49,50]. So, thecomputationalcost
of this concept drift adaptation method is also relatively low. Typical algorithms, such
as the evaluative convolutional neural network (ECNN) [51], mainly use re-weighting
operationtechnologytodynamicallyupdatethemodel,soastosolvetheconceptdrift
probleminhigh-throughputdata. ECNNovercamethe“over-fitting”and“under-fitting”
problems. ECNNisthefirstonlinedeeplearningtechniquetobeintroducedintomarine
datapredictionresearch,althoughitisrelativelycomputationallyexpensive. OnlineCNN-
basedmodelselectionusingperformancegradient-basedsaliencymaps(OS-PGSM)[52]is
mainlyappliedtotime-seriespredictionandusesHoeffding’sbounddetectionalgorithm
toactivelydetecttheoccurrenceofconceptdrift. Whenconceptdriftoccurs,theregionof
competence(ROC)ofthemodelwillberecalculatedtoupdatetheweights. Ithasalow
computationalcost,usingsignificanceplotstoprovideanexplanationformodelselection,

Appl.Sci.2023,13,6515 10of27
buthyperparametersettingsneedtobeoptimized. Deepincrementalhashing(DIH)[53]
focusesonsemanticimageretrievalusingaCNNmodel. TheparametersoftheCNNare
updatedusingapoint-by-pointlossfunctionguidedbythesimilarityofthecurrentdata
blockkeepingthetargetcode. DIHmainlyadaptstogradual,incrementaldrift. Italsohas
certainlimitations,suchasnotconsideringthesemanticrelationshipsbetweenlabels.
Table1summarizesthediscriminant-learning-basedconceptdriftadaptationmethods.
Fromthistable,itcanbeseenthattheMLP-basedconceptdriftadaptationmethodfocuses
ontheprocessingofstreamingdatasamplestoensurethebalancebetweenoldandnew
dataandimbalanceddata,thusimprovingtheaccuracyofpredictionandreducingerrors.
However, it has certain limitations in dealing with high dimensionality, which is more
suitable for dealing with gradual and abrupt concept drift. The RNN-based algorithm
anditsvariantshavegoodtimelinessandcanhandlelong-termserialdata. However,it
isnecessarytoovercometheproblemofcatastrophicforgetting,whichismoresensitive
toincrementalandgradualconceptdrift. Itisworthnotingthatthetypesofconceptdrift
adaptationarerarelyclearlyspecifiedinrelatedstudiesbasedonLSTMandCNN.Further,
mostconceptdriftadaptationmethodsfacetheproblemofslowconvergencespeed.
Table1.Conceptdriftadaptationmethodsbasedondiscriminantlearning.
ConceptDriftAdaptationMethods
TypesofDeep
|          | Algorithms | Detection   |     | Adaptation | Limitation                     |
| -------- | ---------- | ----------- | --- | ---------- | ------------------------------ |
| Learning |            | UpdateModes |     |            |                                |
|          |            | Modes       |     | DriftTypes |                                |
|          |            |             | √   |            | Notsuitableforhigh-dimensional |
|          | SEOA[33]   | −           |     | AIG        |                                |
non-linearproblems
√
| MLP | BODL[34] | +   |     | A   | Newclassescannotbeidentifiedonline |
| --- | -------- | --- | --- | --- | ---------------------------------- |
×
|     | NADINE[35] | +   |     | AGR | Slowtrainingtime |
| --- | ---------- | --- | --- | --- | ---------------- |
√
|     | CIDD-ADODNN[36] | +   |     | AG  | Featureselectiontobeoptimized      |
| --- | --------------- | --- | --- | --- | ---------------------------------- |
|     |                 |     | √   |     | Requireslargeamountsofdatatoupdate |
|     | OARNN[38]       | −   |     | N   |                                    |
themodel
√
|     | ONU-SHO-RNN[40] | +   |     | IG  | Modelupdatedelay |
| --- | --------------- | --- | --- | --- | ---------------- |
RNN
|     |              |     | √   |     | Musthaveamarkedmalwaresample |
| --- | ------------ | --- | --- | --- | ---------------------------- |
|     | AIBL-MVD[41] | +   |     | IG  |                              |
beforeupdatingmodel
|     | MUSE-RNN[42]   | +   | ×   | AGR | Cannothandleimagedatastreams |
| --- | -------------- | --- | --- | --- | ---------------------------- |
|     |                | −   | ×   |     | Highlaborcostandneedtobuild  |
|     | DL-CIBuild[44] |     |     | N   | annotateddatasets            |
√
|     | I-LSTM[5] | −   |     | G   | Balanceofoldandnewdata |
| --- | --------- | --- | --- | --- | ---------------------- |
√
| LSTM | MOMBD-CDD[45] | +   |     | N   | Highresourcecost |
| ---- | ------------- | --- | --- | --- | ---------------- |
√
|     | Fog-DeepStream[46] | +   |     |     | Highmemoryconsumption |
| --- | ------------------ | --- | --- | --- | --------------------- |
√
|     | AD-LSTM[47] | +   |     | N   |                          |
| --- | ----------- | --- | --- | --- | ------------------------ |
|     |             |     | √   |     | Modelupdatelatencyexists |
|     | DCA-DNN[48] | +   |     | N   |                          |
√
−
|     | ECNN[51]    |     |     | N   | Highcomputationalcost        |
| --- | ----------- | --- | --- | --- | ---------------------------- |
|     |             |     | √   |     | Hyperparametersettingsneedto |
|     | OS-PGSM[52] | +   |     | N   |                              |
| CNN |             |     |     |     | beoptimized                  |
|     |             |     | √   |     | Noconsiderationofsemantic    |
|     | DIH[53]     | −   |     | IG  |                              |
relationshipsbetweenlabels
Noconsiderationofaprioriinformation
| SNN | OeSNN[54] | +||− | ×   | GR  |     |
| --- | --------- | ---- | --- | --- | --- |
suchasspeedandseverityofdrift
√
Note: +representsactivemode, −representspassivemode, representsparameterupdate, ×represents
structuralupdate,“A”representsabruptdrift,“I”representsincrementaldrift,“G”representsgradualdrift,
“R”representsrecurringdrift,and“N”meansnotmentionedinthereference.
Inadditiontotheabovetypesofmainstreamalgorithms,therearesomeothermethods
of discriminant learning. For example, the OeSNN-DRT algorithm based on a spike
network[54]introducestwomethods: activeandpassiveadaptationmethods. Itusesthe
datareductiontechnique(DRT),aselectiveandgenerativedatareductiontechnique,to

AAppppll.. SSccii.. 22002233,, 1133,, x65 F1O5R PEER REVIEW 121 1ooff 2287
dopoetism niozte tathkee cinotnot eancctsouonftt ha epnrieourir oinnfaolrrmepatoiosinto sruycha nads tuhped sapteeedit sanstdru scetvuerreit.yH oof wtheev derri,fitt.
Cdouersrennottlyt,a tkheeirnet aorae cfceowu nsttuadpiersi orreilaintefdor tmo aottihoenr styupchesa osft choenscpeepetd darinftd asdeavpetraittyioonf mtheethdordifst.
cCoumrrpeanrtelyd, tthoe mreaairnestfreewamst uddeieeps rleelaartneidngto motohdeerlsty, psoes tohfeyco anrcee pntodt rliifstteadd.a Hptoawtioenvemr,e itth iosd as
wcoomrtphayr eddiretoctmionai fnosrt rreeasmeardcehe. plearningmodels, sotheyarenotlisted. However, itisa
worthydirectionforresearch.
3.2. Concept Drift Adaptation Methods Based on Generative Learning
3.2. ConceptDriftAdaptationMethodsBasedonGenerativeLearning
Generative learning technologies are often used to describe higher-order correlation
Generativelearningtechnologiesareoftenusedtodescribehigher-ordercorrelation
attributes or features for pattern analysis or synthesis, as well as joint statistical distribu-
attributesorfeaturesforpatternanalysisorsynthesis,aswellasjointstatisticaldistribu-
tions of visible data and their related classes [55]. Most generative learning is unsuper-
tionsofvisibledataandtheirrelatedclasses[55]. Mostgenerativelearningisunsupervised
vised learning, but sometimes it can also be used for preprocessing in supervised learning,
learning,butsometimesitcanalsobeusedforpreprocessinginsupervisedlearning,di-
dimensionality reduction processing, etc. [56]. A generative model learns the data gener-
mensionalityreductionprocessing,etc.[56]. Agenerativemodellearnsthedatageneration
ation process, learns the probability distribution of input data, and generates new samples
process,learnstheprobabilitydistributionofinputdata,andgeneratesnewsamplesof
of data. More specifically, the generative model first estimates the conditional density of
data. Morespecifically,thegenerativemodelfirstestimatestheconditionaldensityofthe
the classes P(a|b = k) and the prior class probability P(b = k) from the training data. They
classes P(a|b = k) and the prior class probability P(b = k) from the training data. They
tried to understand how the data for each classification was generated. Bayes’ theorem is
triedtounderstandhowthedataforeachclassificationwasgenerated. Bayes’theoremis
then used to estimate the posterior class probability. Generative models can also learn the
thenusedtoestimatetheposteriorclassprobability. Generativemodelscanalsolearnthe
joint distribution of inputs and labels P(a, b) and then normalize them to obtain posterior
jointdistributionofinputsandlabelsP(a,b)andthennormalizethemtoobtainposterior
probabilities P(b = k|a). The general process of the conceptual drift adaptive method based
probabilities P(b = k|a). The general process of the conceptual drift adaptive method
on generative learning is shown in Figure 6, while the general parameter update mode
basedongenerativelearningisshowninFigure6,whilethegeneralparameterupdate
accounts for a large proportion, and the proportion of active detection and passive adap-
modeaccountsforalargeproportion,andtheproportionofactivedetectionandpassive
tation is comparable. Common deep neural network technologies for unsupervised or
adaptationiscomparable. Commondeepneuralnetworktechnologiesforunsupervised
generative learning are generative adversarial networks (GANs), autoencoders (AEs), re-
orgenerativelearningaregenerativeadversarialnetworks(GANs),autoencoders(AEs),
stricted Boltzmann machines (RBMs), self-organizing mapping (SOM), and deep belief
restrictedBoltzmannmachines(RBMs),self-organizingmapping(SOM),anddeepbelief
networks (DBNs) and their variants.
networks(DBNs)andtheirvariants.
Figure 6. The general process of concept drift adaptation methods based on generative learning.
Figure6.Thegeneralprocessofconceptdriftadaptationmethodsbasedongenerativelearning.
• • AAEE--bbaasseedd ccoonncceepptt ddrriifftt aaddaappttaattiioonn mmeetthhooddss
AE mainly consists of an encoder, a code, and a decoder [57]. It is combined with a
AEmainlyconsistsofanencoder,acode,andadecoder[57].Itiscombinedwithacon-
concept drift adaptation method, which is mainly used for the anomaly detection of some
ceptdriftadaptationmethod,whichismainlyusedfortheanomalydetectionofsomehigh-
high-dimensional data, such as the detection of the anomalous behavior of elderly people.
dimensionaldata,suchasthedetectionoftheanomalousbehaviorofelderlypeople.Typical
Typical algorithms include the adaptive framework for online deep anomaly detection
algorithmsincludetheadaptiveframeworkforonlinedeepanomalydetection(ARCUS),
(ARCUS), unsupervised statistical concept drift detection (USCDD-AE), deep evolving
unsupervised statistical concept drift detection (USCDD-AE), deep evolving denoising
dauentooeinsicnogd earu(tDoeEnVcDodAeNr )(,DanEdVDmAemNo),r ya-nbda semdesmtroeraym-binasgeadn ostmreaalymdinegte catnioonm(aMlye mdeStterecatimon).
(MemASRtrCeUamS)[.5 8]containsconcept-driveninferenceanddrift-awaremodelpoolupdates,
wherAeRcConUcSe p[5t-8d] rciovnentaiinnsf ecroenncceepfto-dcurisveesno innfeevreanlucea tainngd dthreiftr-ealwiaabrieli tmyoodfeilt spomool duepldsaatnesd,
wgihveinreg ceovnacleupatt-idornivsecno riensfewrehnecne gfoivcuenseas onnew evdaalutaatpinogin tth.eW rehlieanbialitcyo nofc eitpst mdoridftelosc acnudrs g,iivts-
ienvga leuvaatliuoantisocno rsecowreisll wdhroepn gtoivternig ag enrewa mdaotda eplopinoto. lWuhpedna tae .coSnocmepet mdroifdt eolcscwurisll, itthse envable-
ureamtioonv esdcoarne dwrilelt drarionpe dto ttoriagdgearp at tmootdheel opcocoulr urepndcaeteo.f Scoomnec empotdderlisft w. Iilnl tthheisn pbreo rceemsso,vtehde
aanlgdo rriethtrmainmeadi ntloy audsaepstt hteo stahme eocstcruurcrteunrceeo offt hceonAcEepmt oddreifltt.o Info rthmisa pmroocdeeslsp, othoel taolgpoerriftohrmm
manaoimnlayl yusdeest ethctei osnamofet shterudcattuarfle oowf t,hweh AicEh mmoadinelly toh afosramla ar gmeordeseol uprocoelc toos ptearnfdorcman annootmstaolrye
dtheeteccutirorenn otfb tahtceh doaftad afltoaww, hwerheiccho nmceapintldyr hifatsm aa ylaorgcceu rre.sUouSCrcDe Dco-AstE a[n5d9 ]cuasnensovt asrtioarteio tnhael
cauurtoreenntc obdaetcrhs toofi ddeantati fwyhtheerea ncoomncaelpiets dorfifetl dmeralyy pocecouprle. ,UwShCicDhDd-eAteEc t[s59co] nucseepst vdarrifitatbiaosneadl
autoencoders to identify the anomalies of elderly people, which detects concept drift
based on data from families and the activity probability plot of the Kullback–Leibler di-
vergence, as defined below.

Appl.Sci.2023,13,6515 12of27
ondatafromfamiliesandtheactivityprobabilityplotoftheKullback–Leiblerdivergence,
asdefinedbelow.
∑
G(z)
D (G (cid:107) Q) = G(z)log( ) (6)
KL Q(z)
z∈Z
where Z is the probability space, and G and Q are probability distributions defined
overZ.HereGandQareactivityprobabilitymaps. Then,whenconceptdriftoccurs,the
encoderwillbeupdatedtoadapttoconceptdriftbybackpropagatingthereconstruction
error. Inthisprocess,thereareoftendifficultieswithdatacollectionandthepossibilityof
falsepositives.
DEVDAN [60] is an incremental learning method that primarily uses the network
significanceformulatoevaluatethepredictivepowerofthemodel. Oncethevalueinthe
captureformularises,itshiddennodesareadjusted. USCDD-AEandDEVDANaremainly
basedontheactiveconceptdriftadaptationmethodbutignoremutationoblivionwhen
addingnewlayers. MemStream[61]isusedforanomalydetectioninmultidimensional
dataandconceptdrift. Itfirstusesasmallportionofthetrainingsetandextractsfeatures
usingthedenoisingautoencoder. Then,whenanewsamplearrives,theanomalyscoreis
recalculated,andtheweightingfactorofAEisupdated. Iftheanomalyscoreexceedsa
user-setthreshold,thememoryisupdatedinafirstin,firstout(FIFO)manner,andthe
modelisretrainedtoaccommodateconceptdrift. Thismethodeffectivelyavoidsnoise
disturbancesandretrainsquicklybutwithhighresourceoverheads.
• GAN-basedconceptdriftadaptationmethods
GANmainlyconsistsofageneratorandadiscriminator. Theformerisusedtocreate
newdatawithsimilarcharacteristicstotheoriginaldata,andthelatterisusedtodetermine
theauthenticityofthegivendata[62]. TherearefewexamplesofGANcombinedwith
conceptdriftadaptationmethodscomparedtootherdeeplearningtechniques,suchasthe
distributedclass-incrementallearningmethodbasedongenerativeadversarialnetworks
(DCIGAN). DCIGAN [63] uses a GAN generator to store information about past data
andconstantlyupdatesGANparameterswithnewdata. Meanwhile,agenerativefusion
method(GF),whichintegratesmulti-nodelocalgeneratorsintoanewglobalgenerator,is
adopted. Particularly,amethodformonitoringandevaluatingGANduringcontinuous
learningispresented,whichexplainstheconceptdrift[64]. Itsmainpurposeistosolve
theproblemofclassifyingdatastreams,butdifferenthyperparametersneedtobesetin
differentenvironments.
• RBM-basedconceptdriftadaptationmethods
RBMisusuallymadeupofvisibleandhiddennodes,eachconnectedtoeveryother
node,whichfacilitatestheunderstandingofsomeirregulardatasets. Moreover,itissensi-
tivetotheoccurrenceofconceptdriftbecauseitisabletolearntheprobabilitydistribution
oftheinput[65]. RBM-I[66]andRRBM–DD[22]aretwotypicalconceptdriftdetection
algorithmsproposedbyKoryckiandKrawczyk,formulti-classimbalanceandthepresence
ofadversarialattackdatastreams,respectively. Theybothusegradientdescenttoupdate
theweightsinordertomaintainthesensitivityofconceptdriftdetection. RBM-IMisnot
suitable for small data streams and is prone to overfitting. RBM-DD has limitations in
identifyingadversarialconceptdriftindynamicclassesofunbalanceddatastreams. In
addition, theGaussianrestrictedBoltzmannmachine(GRBM)algorithm[67]primarily
usestheKullback–Leiblerdivergencedistancetodeterminewhetheraconceptdrifthasoc-
curred,thusenablingtheadaptiveadjustmentoftheslidingwindowandthedivisionofthe
datastream. Itreducesenergyconsumptionandsavesmemorybutonlymakesjudgments
ondatafromasinglesourceanddoesnotadaptivelydivideheterogeneousdata.
• SOM-basedconceptdriftadaptationmethods
SOMisoftenappliedtocreatelow-dimensional(usuallytwo-dimensional)representa-
tionsofhigh-dimensionaldatasets,whilemaintainingthetopologyofthedata[68]. The
mainbenefitofusingSOMisthatitmakeshigh-dimensionaldataeasiertovisualizeand

Appl.Sci.2023,13,6515 13of27
analyzeforunderstandingpatterns. AsinthecaseofGAN,therearefewexamplesofSOM
combinedwithconceptdriftadaptationmethods. Anonlineunsupervisedincremental
methodbasedonself-organizingmaps(OUIM-SOM)[69]isusedformulti-labelstreamclas-
sificationininfinitedelaylabelingscenarios.Itadoptstheonlineupdateofneuronalweight
vectorsanddatasetlabelcardinalitytoaccommodateabruptandincrementalconceptdrifts.
However,itsadaptiveeffectonconceptualdriftislimited.
Table 2 summarizes the typical algorithms based on generative learning. Among
them, AE-based algorithms are mainly used for anomaly detection, and depending on
thecharacteristicsofautoencoders,thesealgorithmsusegenerallyunsupervisedorsemi-
supervisedlearning,whichcanenhancetheflexibilityofdataflowmethodsinutilizing
unlabeledsamples. Theremainingmethodsofcombininggenerativelearningmodelswith
conceptdriftalgorithms,especiallytheconceptdriftadaptationmethodsinvolvedinthe
deepbeliefnetwork,havenotbeenfound,sotheyarenotpresentedinthispaper. However,
therearesomeothergenerativelearningmodelsinvolved. Aself-organizingincremental
neuralnetwork(SOINN+)forunsupervisedlearningfromnoisydatastreams[70]adapts
toconceptdriftbyaddingorremovingnodes,creatingordeletingedges,orcombining
both. SOINN+isrobusttonoiseandisabletofindtopologicalrepresentationsthatare
consistentwiththedistributionofrealdata. ItisworthnotingthattheEuclideandistance
usedinthenodesimilaritymetricisnotsuitableforhigh-dimensionaldata.
Table2.Conceptdriftadaptationmethodsbasedongenerativelearning.
ConceptDriftAdaptationMethods
TypesofDeep
Algorithms
| Learning |     | Detection |     | Adaptation |     | Limitation |
| -------- | --- | --------- | --- | ---------- | --- | ---------- |
UpdateModes
|     |     | Modes |     | DriftTypes |     |     |
| --- | --- | ----- | --- | ---------- | --- | --- |
√
|     |           | −   |     |      | Cannotstoredataforthecurrentbatch |     |
| --- | --------- | --- | --- | ---- | --------------------------------- | --- |
|     | ARCUS[58] |     |     | AIGR |                                   |     |
whereconceptdriftmayoccur
Ignoresmutationforgettingwhenadding
|     | DEVDAN[60] | +   | ×   | AIG |     |           |
| --- | ---------- | --- | --- | --- | --- | --------- |
| AE  |            |     |     |     |     | newlayers |
√
|     | MemStream[61] | −   |     | N    | Highresourceoverhead               |     |
| --- | ------------- | --- | --- | ---- | ---------------------------------- | --- |
|     |               |     | √   |      | Difficultdatacollectionandpossible |     |
|     | USCDD-AE[59]  | +   |     | AIGR |                                    |     |
falsepositives
√
| GAN | DCIGAN[63]  | −   |     | N   | Hyperparametersetting               |     |
| --- | ----------- | --- | --- | --- | ----------------------------------- | --- |
|     |             |     | √   |     | Limitationsinidentifyingadversarial |     |
|     | RRBM–DD[22] | +   |     | AGR | conceptualdriftindynamicclass       |     |
imbalanceddatastreams
| RBM |            |     | √   |     | Notsuitableforsmalldatastreams,prone |     |
| --- | ---------- | --- | --- | --- | ------------------------------------ | --- |
|     | RBM–IM[66] | +   |     | AIG |                                      |     |
tooverfitting
|     |          |     | √   |     | Doesnotadaptivelypartition |     |
| --- | -------- | --- | --- | --- | -------------------------- | --- |
|     | GRBM[67] | +   |     | N   |                            |     |
heterogeneousdata
√
| SOM | OUIM-SOM[69] | −   |     | AI  | Limitedadaptiveeffectonconceptualdrift |     |
| --- | ------------ | --- | --- | --- | -------------------------------------- | --- |
Euclideandistanceusedinthenode
| SOINN | SOINN+[70] | −   | ×   | AI  | similaritymeasureisnotsuitablefor |     |
| ----- | ---------- | --- | --- | --- | --------------------------------- | --- |
high-dimensionaldata
Note:ThesymboldescriptionisthesameasinTable1.
3.3. ConceptDriftAdaptationMethodsBasedonHybridLearning
Hybriddeeplearningmodelsusuallyconsistofmultipledeepunderlyinglearning
models, either a free combination of discriminative or generative learning or discrim-
inative/generative learning plus other models, such as CNN + LSTM, GAN + CNN,
CNN+SVM,andotheralgorithms,asshowninTable3.
The generative model and discriminant model have their own advantages. The
generativelearningmodelcanlearnfromunlabeleddataandcansavelaborcosts. The
discriminantlearningmodelisbetterthanthegenerativemodelinsupervisedtasks.Hybrid
deeplearningintegratesdiscriminantorgenerativemodelsaccordingtothetargettask,
andtheframeworkfortrainingdeepgenerativemodelsanddiscriminantmodelscanenjoy

Appl. Sci. 2023, 13, x FOR PEER REVIEW 15 of 28
Hybrid deep learning models usually consist of multiple deep underlying learning
models, either a free combination of discriminative or generative learning or discrimina-
tive/generative learning plus other models, such as CNN + LSTM, GAN + CNN, CNN +
SVM, and other algorithms, as shown in Table 3.
The generative model and discriminant model have their own advantages. The gen-
erative learning model can learn from unlabeled data and can save labor costs. The discri-
minant learning model is better than the generative model in supervised tasks. Hybrid
Appl.Sci.2023,13,6515 14of27
deep learning integrates discriminant or generative models according to the target task,
and the framework for training deep generative models and discriminant models can en-
joy the advantages of both models to solve real-world problems. The general process of
theadvantagesofbothmodelstosolvereal-worldproblems. Thegeneralprocessofthe
the concept drift adaption method based on generative learning is shown in Figure 7,
conceptdriftadaptionmethodbasedongenerativelearningisshowninFigure7,while
while the general parameter update mode accounts for a large proportion, and the pro-
thegeneralparameterupdatemodeaccountsforalargeproportion,andtheproportionof
portion of active detection and passive adaptation is comparable.
activedetectionandpassiveadaptationiscomparable.
Figure 7. The general process of concept drift adaptation methods based on hybrid learning.
Figure7.Thegeneralprocessofconceptdriftadaptationmethodsbasedonhybridlearning.
TTyyppiiccaall aallggoorriitthhmmss ccoommbbiinneedd wwiitthh LLSSTTMM iinncclluuddee HHSSNN--LLSSTTMM,, oonnlliinnee aauuttoorreeggrreessssiioonn
wwiitthh dedepeelpon glsohnogr t-tsehrmortm-teemrmo rym(OeAmRo-rDyL ST(OMA),RC-DauLsSaTlCMo)n, vLCSTauMs,aalCndonLvSLTSMTCMN, Nacdnad.
HLSSTNM-LCSNTMNc[d71a]. HisSmNa-iLnSlyTuMs e[d71f]o irsm mualitnivlya ruiasteedt ifmore m-seurliteivsaforiraetcea tsitmineg-.sIetrmiesa ifnolryeceamstbiendgs. Iat
nmoavienllyad eampbtievdesa an ndohvyebl raiddaspptiikvien agn(dA hHySb)rmido sdpuikleiningt (oALHSTS)M mtoodkueleep inthtoe LmSoTdMel tcoa kpeaebple thoef
lmonogd-etel rcmapparbeldei cotfi olonnagn-dtearmlle vpiraetdeiicttsiocant aasntdro aplhleicvifaotreg eittsti ncagtapsrtorbolpehmic. Afotrtgheettsianmg eprtiombele,min.
oArtd tehret osammitei gtiamteet,h ien iomrdpaerc ttoof mcoitnigceaptet dthreif ti,mitpaadcot potfs ctohnecneepgt adtirvifet,l oitg a-ldikoepliths otohde nfuengcattiiovne
ilnogth-leikfeulishioonoda tftuennctitoionnm ino dthuel efutosiodny naattmenictiaolnly madodjuusltet thoe dayttneanmtioicnalslcyo ardejaunstd thave oaittdennotiiosne
isnctoerrefe arnendc aev.oHidow neoviseer ,itnhteerrfeesroeunrccee. cHoostwseavreerr,e tlhaeti vreeslyouhricgeh .coOsAtsR a-rDe LrSelTaMtiv[e7l2y] hciogmhb. OinAesRa-
dDeLnSoTisMin g[7a2u] tcooemnbcoindeesr ,aa dneanuotiosrineggr easustioveenmcooddeerl, ,aann dautthoeredgereepssliovneg mshoodretl-,t aernmd tmhee mdoeeryp
(lDonLgS TshMo)rtm-teerthmo dm,ewmhoerrye (tDheLSdTeMno)i sminegtheondc,o wdehreirse mthaei ndleynaopispilniegd entocofedaetru irse mexatirnalcyt iaopn-,
apnlidedO tRoA feaantudreD eLxStTraMctiaorne, aapnpdl iOedRAto atanrdg eDtLpSrTedMic atiroen a.pIpnlitehde toof fltainrgeestt aptree,diticdtiiovnid. eIns tthhee
torfflaininine gstdaateta, iitn dtoivdidateas bthloec tkrsaiannidngth deantap rine-ttor adiantsaa bnldocrkestr aaninds tthheenD pLrSeT-tMraimnso adnedlw reitthratihnes
errorratepredictedbyORAineachdatablocktoobtainseveralindependentsub-models.
the DLSTM model with the error rate predicted by ORA in each data block to obtain sev-
Intheonlinestate,theresultsofthetwomodelsareweightedusingamaximumlikelihood
eral independent sub-models. In the online state, the results of the two models are
estimationtoobtainthefinaltime-seriespredictionoutput. Whenthedatasetistoolarge,
weighted using a maximum likelihood estimation to obtain the final time-series prediction
itsperformancedegrades. B-Detection[73]isprimarilyusedtodetectruntimereliability
output. When the dataset is too large, its performance degrades. B-Detection [73] is pri-
anomaliesinMECservices. ItusesLSTMandAEmodelstocapturethenormalreliability
marily used to detect runtime reliability anomalies in MEC services. It uses LSTM and AE
datastreamdistributioncharacteristics. Aweight-basedreservoirsamplingtechniqueis
models to capture the normal reliability data stream distribution characteristics. A weight-
thenusedtosamplerepresentativenormalreliabilitydata. Finally,thesampleddataare
based reservoir sampling technique is then used to sample representative normal reliabil-
usedfordetectionmodeltraining,andthedetectionmodelisretrainedtoaccommodate
ity data. Finally, the sampled data are used for detection model training, and the detection
conceptualdriftbasedondetectionperformance. However,theruntimeisrelativelylong.
model is retrained to accommodate conceptual drift based on detection performance.
AtypicalalgorithmforthecombinationofLSTMandCNNisCausalConvLSTM[74],
However, the run time is relatively long.
whichutilizesCNNtoextractspatialfeaturesefficientlyandtheLSTMmodelforprediction.
A typical algorithm for the combination of LSTM and CNN is CausalConvLSTM [74],
It determines whether the model needs to be retrained based on the false-positive rate
which utilizes CNN to extract spatial features efficiently and the LSTM model for predic-
calculatedfromtherollingwindowandupdatesthenetworkweightstoaccommodate
tion. It determines whether the model needs to be retrained based on the false-positive
conceptdriftbythebackpropagationthroughtime(BPTT)algorithm. CausalConvLSTM
rate calculated from the rolling window and updates the network weights to accommo-
isprimarilyusedfornetworkintrusiondetectionbuthasaprobleminthatitislimited
inthetypesoflogs. AnotherexampleisLSTMCNNcda[75]fortime-seriesforecasting,
which focuses on actively detecting the occurrence of concept drift and updating the
LSTMCNNnetmodelbyanonlineparameterupdatewhenaconceptdriftisdetectedbut
withcertainrestrictionsonthenormalizedtimeseriesandwindowsizeselection.
In addition, typical algorithms based on hybrid learning include the stacked
autoencoder-deepneuralnetwork(SAE-DNN),OARIMA-RNN,andrecurrentadaptive
classifierensemble(RACE).SAE-DNN[76]activelydetectstheoccurrenceofconceptdrift
using the STEPD. If a concept drift occurs, the top level of SAE-DNN is extended by
meansofrandomvectorfunctionlinking(RVFL).Theparametersintheextensionlayer
aredynamicallyassignedtonewdatathroughLassoregularizationandL2regularization.

Appl.Sci.2023,13,6515 15of27
However,thereisacertainamountofnoiseinterference. Adaptiveonlineensemblelearn-
ingwithRNNandARIMA(OARIMA-RNN)[39]usesRNNmodelstocapturetemporal
dependenciesandimplementonlinelearningmodeling. Then,itdynamicallyadaptsto
conceptdriftbyaddingARIMAtothesetandRNNhyperparametersbeingoptimized
witheachnewbatch. Ithasbetteraccuracythantraditionalofflinemodels. However,there
wasnoquantificationofconceptualdriftorperformanceduringthedrift. RACE[77]uses
theconceptofprocessingrecycling, whichusesanMLP,J48decisiontree, andsupport
vectormachineasbasiclearnerstoprocesstraininginstancesoftime-seriesdata. Then,the
traininginstancesareprocessedbytheincrementallearningalgorithm,andtheconcept
isusedtodetecttheoccurrenceofconceptdrift. Whenconceptdriftoccurs,itisupdated
andretrained. Thealgorithmrequiresalargeamountofmemorytorunandslowsdown
convergenceasthesizeoftheintegrationincreases.
Table3.Conceptdriftadaptationmethodsbasedonhybridlearning.
ConceptDriftAdaptationMethods
| TypesofDeepLearning | Algorithms |           |        |            | Limitation |
| ------------------- | ---------- | --------- | ------ | ---------- | ---------- |
|                     |            | Detection | Update | Adaptation |            |
|                     |            | Modes     | Modes  | DriftTypes |            |
√
| LSTM+SNN    | HSN-LSTM[71]  | −   |     | N   | Highresourceoverhead        |
| ----------- | ------------- | --- | --- | --- | --------------------------- |
|             |               |     | √   |     | Thedatasetistoolarge,andits |
| LSTM+AE+ORA | OAR-DLSTM[72] | −   |     | IR  |                             |
performanceappearstodegrade
√
| LSTM+AE | B-Detection[73] | −   |     | AIGR | Longrunningtime |
| ------- | --------------- | --- | --- | ---- | --------------- |
√
Limitedlogtypesfor
|     | CausalConvLSTM[74] | −   |     | N   |     |
| --- | ------------------ | --- | --- | --- | --- |
algorithmapplications
LSTM+CNN
√
Time-seriesdatanormalizationissues,
|           | LSTMCNNcda[75] | +   |     | AG                                | windowsizeselection |
| --------- | -------------- | --- | --- | --------------------------------- | ------------------- |
| AE+DNN    | SAE-DNN[76]    | +   | ×   | AG                                | Noiseinterference   |
|           |                |     | √   | Noquantificationofconceptualdrift |                     |
| RNN+ARIMA | OARIMA-RNN[39] | −   |     | N                                 |                     |
orperformanceduringdrift
|     |     |     | √   |     | Requireslargeamountsofmemory, |
| --- | --- | --- | --- | --- | ----------------------------- |
MLP+Decisiontree+SVM RACE[77] + AGR increasedintegrationsize,
slowsconvergence
Note:ThesymboldescriptionisthesameasinTable1.
From the summary of typical algorithms in Table 3, it can be seen that
“LSTM” + “other models” is a common hybrid approach, which is mainly applicable
tolong-termstreamingdataandcanovercometheforgettingproblemandimprovethe
accuracytoacertainextent. Insummary,forhybridlearningmethods,multi-modelin-
tegrationismainlytunedusingdynamicweightingbetweenmodels. So,itisessentially
parameterupdating,andtherearealsoembeddedmodelcombinationsthataremainly
appliedinprocessindustries,suchaspowerforecasting.
3.4. OtherConceptDriftAdaptationMethods
Thedeeplearningframeworkclassificationmentionedaboveismainlydividedbased
ontheperspectiveofsingle-classmodelsorhybridmultiplemodels. Itisworthnotingthat
therearecaseswhereotherdeeplearningtechnologies[31,78],suchasdeepreinforcement
learninganddeepfederatedlearning,areused. Forexample,deepreinforcementlearning
wasintroducedasacombinationofdeeplearning(DL)andreinforcementlearning(RL)to
bettercopewiththedynamicchangesofunstableenvironments,leveragingtheprimary
deeplearningmodelstogeneratethetargetmodelsweneed[79,80]. Thegeneralprocess
of this concept drift adaption method is shown in Figure 8, while the structure update
modeismorecommonindeeptransferlearning. Parameterupdatingismorecommonin
deepreinforcementlearning. However,relativelyfewresearchstudiesinvolvingconcept
driftadaptionmethodsareelaboratedcomparedtootherclasses. Themostpopularare
deeptransferlearning(DTL)anddeepreinforcementlearning(DRL).Therefore,wemainly

Appl. Sci. 2023, 13, x FOR PEER REVIEW 17 of 28
updating, and there are also embedded model combinations that are mainly applied in
process industries, such as power forecasting.
3.4. Other Concept Drift Adaptation Methods
The deep learning framework classification mentioned above is mainly divided
based on the perspective of single-class models or hybrid multiple models. It is worth
noting that there are cases where other deep learning technologies [31,78], such as deep
reinforcement learning and deep federated learning, are used. For example, deep rein-
forcement learning was introduced as a combination of deep learning (DL) and reinforce-
ment learning (RL) to better cope with the dynamic changes of unstable environments,
leveraging the primary deep learning models to generate the target models we need
[79,80]. The general process of this concept drift adaption method is shown in Figure 8,
while the structure update mode is more common in deep transfer learning. Parameter
Appl.Sci.2023,13,6515 16of27
updating is more common in deep reinforcement learning. However, relatively few re-
search studies involving concept drift adaption methods are elaborated compared to other
classes. The most popular are deep transfer learning (DTL) and deep reinforcement learn-
initnrgo d(DucReLD). TTLhearnedfoDreR, wL.eT mabalienl4y siunmtromdaurciez eDsTcLo nacnedp tDdRrLif.t Taadbalep t4a tsiuomnmmaertihzoeds scobnacseepdt on
DdTrLifat naddaDptRaLti.on methods based on DTL and DRL.
Figure 8. The general process of concept drift adaptation methods based on other deep learning.
Figure8.Thegeneralprocessofconceptdriftadaptationmethodsbasedonotherdeeplearning.
• • D D T T L L -b -b a a se se d d c c o o n n c c e e p p t t d d r r i i f f t t a a d d a a p p t t a at t i i o o n n m m e e t t h h o o d d s s
DTL mainly uses pre-training of deep learning models to obtain relevant knowledge.
DTL mainly uses pre-training of deep learning models to obtain relevant knowl-
Then, by transferring the acquired knowledge to a new model, it can be adapted to a new
edge. Then,bytransferringtheacquiredknowledgetoanewmodel,itcanbeadapted
task with minimal data and can save resources [81]. Currently, there are not many algo-
to a new task with minimal data and can save resources [81]. Currently, there are not
rithms that involve concept drift. Typical methods are neural network patching (NN-
manyalgorithmsthatinvolveconceptdrift. Typicalmethodsareneuralnetworkpatching
Patching), adaptive mechanisms for learning CNNs (AM-CNNs), and autonomous trans-
(NN-Patching),adaptivemechanismsforlearningCNNs(AM-CNNs),andautonomous
fer learning (ATL).
transferlearning(ATL).
NN-Patching [82] is passively handled concept drift by an error estimator. It mainly
NN-Patching[82]ispassivelyhandledconceptdriftbyanerrorestimator. Itmainly
constructs a discriminant classifier to identify the misclassified regions. Then, it trains a
conneswtr uclcatsssiafiedri s(ccrailmledin aa nptatcclha snseifitwerortko) iodne nthtief ymtihscelamssiisficelads sdiafitead. Trheeg ipoantcsh. Tnhetewno,ritk turaseins sa
nethwe cilnatsesrimfieedri(actael lleadyear poaf ttchhe noeritgwinoarlk n)eounrathl enemtwisocrlaks tsoifi eexdtrdacatt afe.aTtuhreeps aatncdh rneeptrwesoernktau-ses
thteioinnste trhmaet dairaet ecrlaityicearlo tfot hcelaossriigfiicnaatilonne. uTrhalisn metwethorokd tokeeexptsr atchtef eoartiugriensala nndeurreaplr enseetnwtoartiko ns
thqautiackrelyc aridtaicpatlabtolec tloa scsoinficceaptti odnri.ftT, hbiust mitse athboilidtyk teoe hpasntdhlee ocoringcienpatl dnreifut risa llinmeittwedo, rakndq uthicek ly
adhaypptearbplaeratomectoenrsc enpetedd rtiof tb,eb audtjuitssteadb ifloirt ythteo shceanned. lAeMco-CncNeNpts d[8r3if]t uissesli mthiet endo,napnardamtheet-hy-
perricp aCrUamSUeMte rtsesnte teod atcotibveelyad djuetsetcetd thfoe rotchceursrceenncee. oAf Mco-nCcNepNt sdr[i8f3t.] Iut sreeslieths eonn oan “ptararnamsfeert ric
ClUeaSrUnMingt”e pstartaodaigcmtiv tehlayt tdreatnescftertsh teheo ckcnuorwrelendcgeeo off ctohne cCeNptNd rruifntn.inItg rbeelfioesreo tnhea co“ntrcaenpst fer
ledarrinfitn tgo” thpea rCaNdiNg mrutnhnaitntgr aanftsefre rthset hceonkcneopwt dlerdifgt,e bouft tthhee CreNsoNurrcuen onvinerghbeaedfo irse rtehleatcivoenlcye pt
drhiifgthto. AthTLe C[8N4]N usreusn tnhien aguatoftneormthoeusc oGnacuespsitadnr mifti,xbtuurte tmheodreesl o(AurGcMeoMv)e troh eaaudtoimsaretilcaatlilvye ly
hiagdhju.sAt TthLe[ 8n4e]twusoersk twheidathu,t ownhoimcho suoslvGeas uthssei acnonmceixpttu drreifmt pordoebll(eAmG. IMt iMs )jutsot aau mtoamtteart iocaf lly
adrejuasdtatphtienng ettow ao croknwceipdtt thh,awt hhaisc hbeseonl vtheserteh beecfoornec wephtedn riitf rteparpopbelaerms. .AInt iasdjaupsttivae manaottmer- of
reaaldya dpettiencgtitoona acpopnrcoeapcht tthoawtahrads cboenecneptht edrreifbt e(AfoDreTwCDhe) n[8i5t]r eisa apnp eaadrasp.tAivne aadnaopmtaivlye danetoemc-aly
detitoenct mioondaepl bparoseadc honto kwnoawrdlecdognec depisttidllraitfito(nA aDndT CDDTL).[ 8It5 t]raisnasfnerasd kanpotwivleedagneo fmroamly tdhee tAecEt-ion
modelbasedonknowledgedistillationandDTL.IttransfersknowledgefromtheAE-based
teachermodeltothestudentmodelandupdatesonlythestudentmodel,whichdynami-
callyadjustsmodelweightstoaccommodateconceptdriftprimarilythroughlocalinference
onnewsamples. However, thealgorithmalsosuffersfromtwolimitations. Firstly, the
industrialscenariosusedfortheexperimentsarerelativelyhomogeneous,andsecondly,
littleattentionispaidtoscarceanomalydata.
• DRL-basedconceptdriftadaptationmethods
DRL combines the perception ability of deep learning with the decision-making
ability of reinforcement learning, which can be directly controlled based on the input
information. Reinforcementlearningdefinesthegoalofoptimization,anddeeplearning
givesthemechanismbywhichitworks(howtocharacterizeproblemsandhowtosolve
them)[86]. Thealgorithmsusingthisconceptdriftadaptingmethodaremainlyappliedin
thefieldsoffinancialinvestmentandanomalydetection. TypicalalgorithmsincludeDeep-
Pocket,RL4OASD,onlineensembleaggregationusingreinforcementlearning(OEA-RL),
andDeepBreath.
DeepPocket[87]isusedinthefieldoffinancialinvestment.Thisalgorithmmainlyuses
arestrictedstackedautoencodertoextractfeaturesandusestwoconvolutionalnetworks

Appl.Sci.2023,13,6515 17of27
tofindthebestportfoliothroughdeepreinforcementlearning. Then,itusesonlinetraining
todynamicallyupdateweightstoaccommodateconceptdrift,butitdoesnotlenditself
to a long-term investment strategy. RL4OASD [88] is mainly used for the detection of
abnormaltrajectoriesofvehicles. Itincludestwonetworks: oneisresponsibleforlearning
thefeaturesoftheroadnetworkandtrajectory,andtheotherisresponsiblefordetecting
anomalous sub-traces based on the learned features. The two networks can be trained
iterativelywithoutlabeleddata,andtheyemployanonlinelearningstrategy;thatis,they
aretrainedwithnewlyrecordedtrajectorydataandcontinuouslyupdatetheirstrategies
based on current traffic conditions, but they have a longer training time. OEA-RL [89]
mainlyusesthedeepreinforcementlearningframeworkasameta-learningmethodtolearn
linearweightedensemblesandactivelydetectstheoccurrenceofconceptdriftthroughthe
Page–Hinkley(PH)test. Then,itadaptstoconceptdriftbyupdatingitsparameters. Again,
thereisacertaindelayinupdatingduetoitsactivedetectionalgorithm. DeepBreath[6]
ismainlyusedforfinancialinvestment,whichusesalimitedsuperimposedautoencoder
fordimensionalityreductionandfeatureprocessing. Then,theSARSAalgorithmandthe
onlinebatchprocessingmethodareusedtotrainCNNlearninginvestmentstrategiesfrom
historicaldata,andaftertrainingthemodel,theweightsareupdatedthroughtheonline
learning scheme to adapt to the concept drift. The algorithm lacks, to some extent, the
considerationofexogenousfactors.
As can be seen in Table 4, for DRL and DTL, the update mode of DRL is mainly
a parameter update. It interacts well with the environment to learn the sequence of its
behavior. The update mode of DTL is mainly a structural update. DTL can effectively
useasmallamountofdatatotrainneuralnetworks. Thischaracteristiccanusestructure
updatestotrainbetterpredictivemodels. Inaddition,theygenerallyuseacombination
ofonlineandofflineapproachestoadaptconceptdriftandsupportmorecomplexpredic-
tions. InadditiontoDTLandDRL,twomorepopulardeeplearningmethods,thereare
alsoconceptdriftadaptionmethodsbasedonotherdeeplearningtechnologies. Suchas
FedHAR[90],whichisasmarthumanactivityrecognition(HAR)framebasedondeep
federatedlearning. FedHARdesignsanunsupervisedgradientaggregationstrategythat
canovercometheproblemofconceptdriftandconvergenceinstabilityinonlinelearning,
whichismainlyusedtosummarizethegradientsofalllabeledclientsandunlabeledclients
infederatedlearningandthendrivetheparameterupdateoftheservermodelbyaveraging
theaggregategradienttoadapttotheconceptdrift.
Table4.Otherconceptdriftadaptationmethods.
Typesof ConceptDriftAdaptationMethods
Deep Algorithms Detection Adaptation Limitation
Learning Modes UpdateModes DriftTypes
NN-Patching[82] − × N Needtoadjusthyperparametersforthescene
AM-CNNs[83] + × N Highoverhead
DTL
ATL[84] − × AIG Forgettingproblem
√
ADTCD[85] − AIGR Littleattentionispaidtoscarceanomalydata
√
DeepPocket[87] − N Notsuitableforlong-terminvestmentstrategies
√
RL4OASD[88] − N Longmodeltrainingtime
DRL √
OEA-RL[89] + N Updatingdelay
√
DeepBreath[6] − N Lackofconsiderationforexogenousfactors
√
DFL FedHAR[90] − N Scarcityoflabels,withprivacy
Note:ThesymboldescriptionisthesameasinTable1.
3.5. Discussion
Accordingtothesummaryofconceptdriftadaptationmethods,wecanseethatthe
proportionofhybridlearninganddiscriminantlearningisrelativelylarge,andespecially

Appl.Sci.2023,13,6515 18of27
discriminative learning is widely used. This phenomenon reflects the fact that having
labelinformationsamplesisbeneficialfordetectingchangesinthedistributionofdata.
Inaddition,parameterupdatesalsoaccountforalargepart. Comparedwithstructural
updates,parameterupdatesreducetheconvergencetimeandadaptwelltoabruptconcept
drift.Secondly,inthealgorithmsofdiscriminantlearningandgenerativelearning,itsactive
detectionalsoaccountsforaconsiderablepart,anditismainlyconducivetoexplaining
theoccurrenceofconceptdriftandreducingthecomputingresourcesoftraining,buttoa
certainextent,itrequiresadditionalmemoryandCPUstorage. Fromthispaper,itcanbe
seenthatdealingwithconceptdrift,reducingtheamountofcomputation,savingresources,
andspeedingupconvergenceareourmainchallengesatpresent.
Inaddition,accordingtotheabovesummaryofdriftadaptationtypes,wecanfind
that there are usually more adaptation methods for abrupt, incremental, and gradual
drifttypes. Relativelyspeaking,abruptdriftoccursmostfrequently,anditsdriftspeed
occursthefastest,somostdetectionmethodscanbesensitivetodetection,buttherewill
alsobeproblemssuchasupdatedelayandhighcomputationalcomplexity. Incontrast,
recurring drift occurs the least often. In the case of recurring drift, previously learned
modelsmaybecomerelevantagaininthefuture. Onlinedeeplearningalgorithmsmay
havetorelearnpreviousconcepts. Thisprocesshasahighcomputationalburdenbecauseit
meanstuningortraininganewmodelfromscratch. Thisisalsooneofthemainchallenges
atthistime. Finally,itshouldbeaddedthatinadditiontobeingbasedondeeplearning
algorithms,extremelearningmachinesarealsomodelsbasedonneuralnetworks. Inrecent
years, the use of the concept drift algorithm of ELM has also increased, and the main
algorithmsincludeMeta-RKOS-ELM[91],SSOE-FP-ELM[92],ONLAD[93],etc.,whichis
alsoaworthyresearchdirection.
4. PerformanceEvaluationofConceptDrift
In this section, we summarize the common datasets and evaluation metrics. The
datasetsaredividedintorealdatasetsandsyntheticdatasets. Fortheformer,wepresent
its sources, learning tasks, and properties. For the latter, we show the drift types and
characteristicsitcontains.Afterthat,wedescribetheevaluationmetricsandtheirmeanings.
4.1. Datasets
Realdatasetscaneffectivelydemonstratethegeneralityandapplicabilityoftheal-
gorithm in the real world, for which the commonly used datasets are KDD CUP 1999,
Electricity,Weather,Spam,andCoverType. TheKDDCUP1999[94]isthedatasetused
intheKDD(knowledgediscoveryanddatamining)competition. Itismainlyusedfor
networkintrusiondetectiontodistinguishbetweennormalnetworkconnectionsandmali-
ciousnetworkconnections,includingvariousattackdatasimulatedinthemilitarynetwork
environment. Electricity[95]isderivedfromtheelectricitymarketofNewSouthWales,
Australia(1996–1998). Itismainlyusedtopredictchangesinelectricitypricesinthepast
24h,includingtheweather,userdemand,supplyconditions,andseasons. Weather[96]
containsdailyweathermeasurementdataforacertainareafrom2006to2016,including
temperature,humidity,winddirection,windspeed,visibility,atmosphericpressure,etc.,
forpredictingrainfall.Spam[97]ismainlyusedtoidentifyspam.CoverType[94]isderived
fromtheforestcoverofacertainareaintheU.S.ForestServicesystem.
Synthetic datasets can evaluate the performance of the algorithms under different
conceptdriftsituationsandcontainvarioustypesofconceptdrift. Fordetectingabrupt
conceptdrift,R.MNIST[98],P.MNIST[60],andSEA[99]canbeused. SEAcontainsthree
featuresandtwoclassesineachsample. R.MNISTandP.MNISTaregeneratedfromthe
MNISTdatasetcontaining784featuresand10classes. ItisworthnotingthatP.MNISTalso
detectsrecurringdrift. Fordetectinggradualconceptdrift,Circles[100],Hyperplane[101],
andLED[94]canbeused. Circlescontainstwofeaturesandtwoclassesineachsample.
Then, Hyperplane also detects incremental drift, containing 10 features and 2 classes

Appl.Sci.2023,13,6515 19of27
in each sample. LED also detects abrupt drift, containing 24 features and 10 classes in
eachsample.
In addition to the above commonly used datasets, there are some special datasets
for deep learning frameworks, such as the Vxheaven dataset [102] commonly used in
previousmalwareanalysisstudies,consistingofWindowsbinariesbelongingtomalware
andbenignportableexecutables,containingdifferenttypesofmalwarefamilies,suchas
trojans,ransomware,andviruses. HAR-UCI[103]wasmadefromrecordingsof30subjects
performing activities of daily living. The STL-10 dataset [104] is an image recognition
dataset for the development of unsupervised feature learning, deep learning, and self-
learningalgorithms. TheCat-Dogdataset[105]containstwoclasses,catsanddogs,with
12,500images. TheCIFAR100dataset[106]isutilizedtosimulatethedistributiondrifting
situation. It has 60,000 32 × 32 × 3 RGB images. Finally, some researchers have used
theirowncollecteddata,aswellasdatasetsfromtheapplicationdomain. Forexample,
the I-LSTM and ECNN algorithms are collected data, and CausalLSTM uses the HDFS
dataset[107]andtheCybersecurity’sIntrusionDetectionEvaluationdataset[108].
4.2. TheEvaluationMetrics
Foralgorithmsbasedondiscriminativelearningandhybridlearning,accuracyrecall,
precision, F -score, Matthews’ correlation coefficient (MCC), and Cohen’s kappa k are
1
mainlyusedforclassificationproblems,andmeanabsoluteerror(MAE),meansquared
error(MSE),androotmeansquarederror(RMSE)aremainlyusedforregressionproblems.
Foralgorithmsbasedongenerativelearningandothers,thenumberofhiddennodesper
timestep(HN),thenumberofhiddenlayerspertimestep(HL),parametercount(PC),
andexecutiontime(ET)aremainlyused. Inparticular,theyareuniqueevaluationmetrics
undertheframeworkofdeeplearning. ItisworthnotingthattheMCCandCohen’skappa
kevaluationmetricsaremainlyusedforunbalanceddata. ThedefinitionofMCCisshown
inEquation(7).
TP×TN−FP×FN
MCC = (cid:112) (7)
(TP+FP)(TP+FN)(TN+FP)(TN+FN)
where TP represents true positives, TN represents true negatives, FP represents false
positives,andFN representsfalsenegatives. ThedefinitionofCohen’skappaisshown
inEquation(8).
P −P
k = 0 e (8)
1−P
e
whereP andPearethesuccessrateoftheactualandrandompredictors.
0
In addition to the above basic evaluation metrics, some researchers also use some
evaluationmetricsfortheapplicationfieldofalgorithms. Forexample,theDeepPocket
algorithm,whichismainlyusedinthefieldoffinancialinvestment,mainlyusesmaximum
drawdown (MDD), Sharpe ratio (Sr), and conditional value at risk (CVaR) to evaluate
itsperformance.
5. FutureDirections
Basedontheanalysisanddiscussionoftheabovealgorithms,wesummarizetheprob-
lemsthatneedtobesolved,whichrequirefurtherresearchinthefuture,asdescribedbelow.
5.1. FullCoverageofConceptDriftTypes
Accordingtotheabove-mentionedalgorithms,suchasONU-SHO-RNN,DEVDAN,
etc.,wecanfindthatitisnotpossibletoadapttoallconceptdriftsatonce,andamongthe
fourtypesofconceptdrift,thebestadaptabilityofthealgorithmistoabruptdrift. There
arealsosomealgorithms,suchasECNNandHSN-LSTM,forwhichthedatasetusedin
theexperimentalpartdoesnotindicatethetypeofdriftincluded,andtherearealsono

Appl.Sci.2023,13,6515 20of27
experimentsontheeffectivenessofdifferenttypesofconceptdrift.Therefore,itisnecessary
toimprovetherobustnessandgeneralizationofthemethodstostudyconceptdrift.
5.2. DataProcessingProblem
Dataprocessinghasbeenabigchallengeindeeplearningandconceptdriftadaptation
methods [4,21]. Firstly, when inputting samples, we may face problems such as class-
imbalancedata,high-dimensionaldata,etc. Forexample,whenperformingonlineanomaly
detection,mostofthedatasetsareveryunbalanced,andtheabnormaldataaccountfor
averysmallpart[109]. Secondly,whenthemodelupdateisperformed,wewillfacethe
problemofhowtobalancebetweennewdataandolddataandtheproblemthatthenew
datasamplesarenotenoughtosupporttheupdateofthedeeplearningmodelafterthe
conceptdriftoccurs. Thesewillleadtopoorprediction,slowmodelconvergence,delayed
modelupdate,andotherconsequencesthatareworthyofourconsiderationandresearch.
5.3. Multi-ModelIntegrationProblem
Ourreviewshowsthatonlineintegrationmethodshavebeenmorepopularinconcept
driftadaptationmethods,suchasOARIMA-RNN.Ensemblealgorithmscaneffectivelypre-
ventoverfittingandprovidebetterpredictionperformance. However,theircomputational
complexityishigh,andtheytakeupmoreresources,sohowtooptimizetheirperformance
isalsoaquestionworthyofdeepconsideration[110].
5.4. VisualizationProblemofConceptDrift
At present, there is relatively little research on concept drift visualization. Classic
visualizershaveDriftVis[111],whichcanhelpdecisionmakersidentifyandcorrectconcept
drift in data streams. In fact, for many related fields such as air quality monitoring,
financial market analysis, etc. [7,112], explaining concept drift is conducive to helping
decisionmakerscomprehensivelyanalyzeproblemsandmakecorrectdecisions. Finally,it
isworthmentioningtheapplicationofconceptualdrifttypevisualization.
6. Conclusions
Inrecentyears,deeplearninghasbecomeoneofthecoretechnologiesofthefourth
industrialrevolution. So,ithasalsobecomeoneoftheindispensabletoolstoassistintelli-
gentdecisionmaking. However,intheeraoftheepidemicandbigdata,datadistribution
instreamingdatacanchangeveryeasily,whichisaphenomenonknownasconceptdrift.
Onceconceptdriftoccurs,eventhebest-traineddeeplearningmodelsbecomeobsolete,
producingpoorpredictions. Therefore,thispapersummarizesconceptdriftadaptation
methodsunderthedeeplearningframework. Firstly,weexplainthedefinitionandcauses
ofconceptdrift. Then,weintroducethetypesofconceptdriftandthegeneralprocessof
a concept drift adapting method under the deep learning framework. Next, we divide
the deep learning model using the concept drift adaptation method from four aspects,
includingdiscriminantlearning,generativelearning,hybridlearning,andothers. Foreach
aspect,weintroduceindetailtheupdatemodes,detectionmodes,andadaptationdrift
typesofconceptdriftadaptationmethods. Finally,wesummarizecommondatasetsand
evaluationmetricsforconceptdriftadaptationmethodsandpointoutfuturedirections.
Wehopethatthispapercanprovidesomeacademichelptoresearchers.
AuthorContributions:Conceptualization,Q.X.andL.Z.;methodology,Q.X.andX.C.;formalanaly-
sis,Q.X.andY.W.;investigation,Q.X.andX.C.;writing—originaldraftpreparation,Q.X.;writing—
reviewandediting,Q.X.,L.Z.,X.C.,andY.W.;supervision,L.Z.;projectadministration,L.Z.;funding
acquisition,L.Z.Allauthorshavereadandagreedtothepublishedversionofthemanuscript.
Funding:ThisworkwassupportedbytheKeyProgramofChongqingEducationSciencePlanning
Project(No.K22YE205098)andtheDoctoralResearchFoundationofChongqingNormalUniversity
(No.21XLB030,No.21XLB029).
InstitutionalReviewBoardStatement:Notapplicable.

Appl.Sci.2023,13,6515 21of27
InformedConsentStatement:Notapplicable.
DataAvailabilityStatement:Thedatasupportingthisreviewarefrompreviouslyreportedstudies
anddatasets,whichhavebeencited.
Acknowledgments:WeacknowledgethefinancialsupportprovidedbytheKeyProgramofChongqing
EducationSciencePlanningProject(No. K22YE205098)andtheDoctoralResearchFoundationof
ChongqingNormalUniversity(No.21XLB030,No.21XLB029).
ConflictsofInterest:Theauthorsdeclarethattherearenoconflictofinterestregardingthepublica-
tionofthispaper.
Abbreviations
Thefollowingabbreviationsareusedinthismanuscript:
OCDD one-classdriftdetector
CDT_MSW conceptdrifttypeidentificationmethodbasedonmulti-slidingwindows
KSWIN Kolmogorov–Smirnovtestdetector
LD3 labeldependencydriftdetector
STUDD student–teacherapproachforunsuperviseddriftdetection
CDCMS conceptdrifthandlingbasedonclusteringinthemodelspace
DMDDM diversitymeasuredriftdetectionmethod
I-LSTM improvedlongshort-termmemory
DDM driftdetectionmethod
MLP multilayerperceptron
CNN convolutionalneuralnetwork
RNN recurrentneuralnetwork
DNN deepneuralnetwork
SEOA selectiveensemble-basedonlineadaptivedeepneuralnetwork
BODL bilevelonlinedeeplearningframework
NADINE neuralnetworkwithdynamicallyevolvedcapacity
CIDD-ADODNN Adadeltaoptimizer-baseddeepneuralnetworkswithconceptdriftdetection
ADWIN adaptivesliding-windowdriftdetectiontechnology
OARNN onlineadaptiverecurrentneuralnetwork
TPE tree-structuredParzenestimator
ONU-SHO opposition-basednovelupdatingspottedhyenaoptimization
ONU-SHO-RNN ONU-SHO-basedRNN
adaptivebehavioral-basedincrementalbatchlearningmalwarevariant
AIBL-MVD
detectionmodel
SPC statisticalprocesscontrol
MUSE-RNN multilayerself-evolvingrecurrentneuralnetwork
LSTM longshort-termmemory
CI continuousintegration
GA geneticalgorithm
multi-objectivemetaheuristicoptimization-basedbigdataanalyticswith
MOMBD-CDD
conceptdriftdetection
STEPD StatisticalTestofEqualProportionsmethod
GSO glowwormswarmoptimization
Bi-LSTM bidirectionallongshort-termmemory
CUSUM cumulativesum
EWMA exponentiallyweightedmovingaverage
AD-LSTM adaptiveLSTMframework
SDWIN sliding-windowalgorithm
TP-ALS two-phaseadaptivelearningstrategy
ECNN evolutiveconvolutionalneuralnetwork
onlineCNN-basedmodelselectionusingperformancegradient-based
OS-PGSM
saliencymaps
DIH deepincrementalhashing
ROC regionofcompetence

Appl.Sci.2023,13,6515 22of27
DRT datareductiontechnique
adaptiveframeworkforonlinedeepanomalydetectionunderacomplex
ARCUS
evolvingdatastream
USCDD-AE unsupervisedstatisticalconceptdriftdetection
DEVDAN deepevolvingdenoisingautoencoder
MemStream memory-basedstreaminganomalydetection
FIFO firstin,firstout
ADTCD adaptiveanomalydetectionapproachtowardconceptdrift
GAN generativeadversarialnetwork
AE autoencoder
RBM restrictedBoltzmannmachine
SOM self-organizingmapping
distributedclass-incrementallearningmethodbasedongenerative
DCIGAN
adversarialnetworks
GF generativefusion
GRBM GaussianrestrictedBoltzmannmachine
OUIM-SOM onlineunsupervisedincrementalmethodbasedonself-organizingmaps
self-organizingincrementalneuralnetworkforunsupervisedlearningfrom
SOINN+
noisydatastreams
AHS noveladaptiveandhybridspikingmodule
OAR-DLSTM onlineautoregressionwithdeeplongshort-termmemory
HDL-OKW hybriddeeplearningclassifierandoptimizedkeywindowingapproach
BPTT backpropagationthroughtime
SAE-DNN stackedautoencoder-deepneuralnetwork
RVFL randomvectorfunctionlinking
SVM supportvectormachines
OARIMA-RNN adaptiveonlineensemblelearningwithrecurrentneuralnetworkandARIMA
RACE recurrentadaptiveclassifierensemble
DTL deeptransferlearning
NN-Patching neuralnetworkpatching
AM-CNNs adaptivemechanismforlearningCNNs
ATL autonomoustransferlearning
AGMM autonomousGaussianmixturemodel
DRL deepreinforcementlearning
OEA-RL onlineensembleaggregationusingreinforcementlearning
PH Page–Hinkley
KDD knowledgediscoveryanddatamining
MCC Matthews’correlationcoefficient
MAE meanabsoluteerror
MSE meansquarederror
RMSE rootmeansquarederror
HN thenumberofhiddennodespertimestep
HL thenumberofhiddenlayerspertimestep
PC parametercount
ET executiontime
MDD maximumdrawdown
Sr Sharperatio
CVaR conditionalvalueatrisk
FedHAR federatedlearninghumanactivityrecognitionframe
References
1. Shrestha,Y.R.;Krishna,V.;vonKrogh,G.Augmentingorganizationaldecision-makingwithdeeplearningalgorithms:Principles,
promises,andchallenges.J.Bus.Res.2021,123,588–603.[CrossRef]
2. Schlimmer,J.C.;Granger,R.H.Incrementallearningfromnoisydata.Mach.Learn.1986,1,317–354.[CrossRef]
3. Lu,J.;Liu,A.;Song,Y.;Zhang,G.Data-drivendecisionsupportunderconceptdriftinstreamedbigdata.ComplexIntell.Syst.
2020,6,157–163.[CrossRef]
4. Gama,J.;Žliobaite˙,I.;Bifet,A.;Pechenizkiy,M.;Bouchachia,A.Asurveyonconceptdriftadaptation.ACMComput.Surv.2014,
46,1–37.[CrossRef]

Appl.Sci.2023,13,6515 23of27
5. Xu,R.;Cheng,Y.;Liu,Z.;Xie,Y.;Yang,Y.ImprovedLongShort-TermMemorybasedanomalydetectionwithconceptdrift
adaptivemethodforsupportingIoTservices.Futur.Gener.Comput.Syst.2020,112,228–242.[CrossRef]
6. Soleymani, F.; Paquet, E. Financial portfolio optimization with online deep reinforcement learning and restricted stacked
autoencoder—DeepBreath.ExpertSyst.Appl.2020,156,113456.[CrossRef]
7. Wang,X.;Chen,W.;Xia,J.;Chen,Z.;Xu,D.;Wu,X.;Xu,M.;Schreck,T.ConceptExplorer:VisualAnalysisofConceptDriftsin
Multi-sourceTime-seriesData.InProceedingsoftheIEEEConferenceonVisualAnalyticsScienceandTechnology(VAST),Salt
LakeCity,UT,USA,25–30October2020;pp.1–11.[CrossRef]
8. Hoens,T.R.;Polikar,R.;Chawla,N.V.Learningfromstreamingdatawithconceptdriftandimbalance:Anoverview.Prog.Artif.
Intell.2012,1,89–101.[CrossRef]
9. Wen,Y.;Qiang,B.;Fan,Z.Asurveyoftheclassificationofdatastreamswithconceptdrift. CAAITrans. Intell. Syst. 2013,8,
95–104.
10. Ditzler,G.;Roveri,M.;Alippi,C.;Polikar,R.LearninginNonstationaryEnvironments:ASurvey.IEEEComput.Intell.Mag.2015,
10,12–25.[CrossRef]
11. Webb,G.I.;Hyde,R.;Cao,H.;Nguyen,H.L.;Petitjean,F.Characterizingconceptdrift.DataMin.Knowl.Discov.2016,30,964–994.
[CrossRef]
12. Krawczyk, B.; Minku, L.L.; Gama, J.; Stefanowski, J.; Woz´niak, M. Ensemble learning for data stream analysis: A survey.
Inf.Fusion2017,37,132–156.[CrossRef]
13. Khamassi,I.;Sayed-Mouchaweh,M.;Hammami,M.;Ghédira,K.Discussionandreviewonevolvingdatastreamsandconcept
driftadapting.Evol.Syst.2018,9,1–23.[CrossRef]
14. Lu,J.;Liu,A.;Dong,F.;Gu,F.;Gama,J.;Zhang,G.LearningunderConceptDrift:AReview.IEEETrans.Knowl.DataEng.2018,
31,2346–2363.[CrossRef]
15. AbGhani,N.L.;Aziz,I.A.;Mehat,M.ConceptDriftDetectiononUnlabeledDataStreams:ASystematicLiteratureReview.In
ProceedingsoftheIEEEConferenceonBigDataandAnalytics(ICBDA),Xiamen,China,8–11May2020;pp.61–65.[CrossRef]
16. Lima,M.;Neto,M.;Filho,T.S.;Fagundes,R.A.D.A.LearningUnderConceptDriftforRegression—ASystematicLiterature
Review.IEEEAccess2022,10,45410–45429.[CrossRef]
17. Bayram,F.;Ahmed,B.S.;Kassler,A.Fromconceptdrifttomodeldegradation:Anoverviewonperformance-awaredriftdetectors.
Knowl.BasedSyst.2022,245,108632.[CrossRef]
18. Desale,K.S.;Shinde,S.V.AddressingConceptDriftsUsingDeepLearningforHeartDiseasePrediction:AReview.InProceedings
ofSecondDoctoralSymposiumonComputationalIntelligence;Gupta,D.,Khanna,A.,Kansal,V.,Fortino,G.,Hassanien,A.E.,Eds.;
Springer:Singapore,2022;Volume1374,pp.157–167.[CrossRef]
19. Iwashita,A.S.;Papa,J.P.AnOverviewonConceptDriftLearning.IEEEAccess2018,7,1532–1547.[CrossRef]
20. R.O.Duda,P.E.Hart,andD.G.Stork,PatternClassification,NewYork:JohnWiley&Sons,2001,pp.xx+654,ISBN:0-471-05669-3.
J.Classif.2007,24,305–307.[CrossRef]
21. Agrahari,S.;Singh,A.K.ConceptDriftDetectioninDataStreamMining:Aliteraturereview.J.KingSaudUniv.-Comput.Inf.Sci.
2021,34,9523–9540.[CrossRef]
22. Korycki,Ł.;Krawczyk,B.Adversarialconceptdriftdetectionunderpoisoningattacksforrobustdatastreammining.Mach.Learn.
2022,1–36.[CrossRef]
23. Gözüaçık,Ö.;Can,F.Conceptlearningusingone-classclassifiersforimplicitdriftdetectioninevolvingdatastreams.Artif.Intell.
Rev.2021,54,3725–3747.[CrossRef]
24. Guo,H.;Li,H.;Ren,Q.;Wang,W.Conceptdrifttypeidentificationbasedonmulti-slidingwindows. Inf. Sci. 2022,585,1–23.
[CrossRef]
25. Raab,C.;Heusinger,M.;Schleif,F.-M.ReactiveSoftPrototypeComputingforConceptDriftStreams.Neurocomputing2020,416,
340–351.[CrossRef]
26. Gözüaçık, Ö.; Büyükçakır, A.; Bonab, H.; Can, F. Unsupervised concept drift detection with a discriminative classifier. In
Proceedings of the 28th ACM International Conference on Information and Knowledge Management, Beijing China, 3–7
November2019;pp.2365–2368.
27. Cerqueira,V.;Gomes,H.M.;Bifet,A.;Torgo,L.STUDD:Astudent–teachermethodforunsupervisedconceptdriftdetection.
Mach.Learn.2022,1–28.[CrossRef]
28. Chiu,C.W.;Minku,L.L.ADiversityFrameworkforDealingwithMultipleTypesofConceptDriftBasedonClusteringinthe
ModelSpace.IEEETrans.NeuralNetw.Learn.Syst.2020,33,1299–1309.[CrossRef]
29. Mahdi,O.A.;Pardede,E.;Ali,N.;Cao,J.Diversitymeasureasanewdriftdetectionmethodindatastreaming.Knowl.-BasedSyst.
2020,191,105227.[CrossRef]
30. Yuan,L.;Li,H.;Xia,B.;Gao,C.;Liu,M.;Yuan,W.;You,X.RecentAdvancesinConceptDriftAdaptationMethodsforDeep
Learning.InProceedingsofthe31stInternationalJointConferenceonArtificialIntelligence,Vienna,Austria,23–29July2022;
InternationalJointConferencesonArtificialIntelligenceOrganization:Vienna,Austria,2022;pp.5654–5661.
31. Sarker,I.H.DeepLearning:AComprehensiveOverviewonTechniques,Taxonomy,ApplicationsandResearchDirections.SN
Comput.Sci.2021,2,420.[CrossRef]

Appl.Sci.2023,13,6515 24of27
32. Leväsluoto,J.;Kohl,J.;Sigfrids,A.;Pihlajamäki,J.;Martikainen,J.DigitalizationasanEngineforChange? BuildingaVision
PathwaytowardsaSustainableHealthCareSystembyUsingtheMLPandHealthEconomicDecisionModelling.Sustainability
2021,13,13007.[CrossRef]
33. Guo,H.;Zhang,S.;Wang,W.Selectiveensemble-basedonlineadaptivedeepneuralnetworksforstreamingdatawithconcept
drift.NeuralNetw.2021,142,437–456.[CrossRef]
34. Han,Y.-N.; Liu,J.-W.;Xiao,B.-B.;Wang,X.-T.;Luo,X.-L.BilevelOnlineDeepLearninginNon-stationaryEnvironment. In
Proceedingsofthe30thInternationalConferenceonArtificialNeuralNetworks,Bratislava,Slovakia,14–17September2021.
[CrossRef]
35. Pratama,M.;Za’In,C.;Ashfahani,A.;Ong,Y.S.;Ding,W.AutomaticConstructionofMulti-layerPerceptronNetworkfrom
StreamingExamples.InProceedingsofthe28thACMInternationalConferenceonInformationandKnowledgeManagement,
BeijingChina,3–7November2019.[CrossRef]
36. Priya,S.;Uthra,R.A.Deeplearningframeworkforhandlingconceptdriftandclassimbalancedcomplexdecision-makingon
streamingdata.ComplexIntell.Syst.2021,1–17.[CrossRef]
37. Dezfouli,A.;Griffiths,K.;Ramos,F.;Dayan,P.;Balleine,B.W.Modelsthatlearnhowhumanslearn:Thecaseofdecision-making
anditsdisorders.PLoSComput.Biol.2019,15,e1006903.[CrossRef]
38. Fekri,M.N.;Patel,H.;Grolinger,K.;Sharma,V.Deeplearningforloadforecastingwithsmartmeterdata: OnlineAdaptive
RecurrentNeuralNetwork.Appl.Energy2021,282,116177.[CrossRef]
39. Jagait,R.K.;Fekri,M.N.;Grolinger,K.;Mir,S.LoadForecastingUnderConceptDrift:OnlineEnsembleLearningwithRecurrent
NeuralNetworkandARIMA.IEEEAccess2021,9,98992–99008.[CrossRef]
40. Singh, M.N.; Khaiyum, S.EnhancedDataStreamClassificationbyOptimizedWeightUpdatedMeta-learning: Continuous
learning-basedonConcept-Drift.Int.J.WebInf.Syst.2021,17,645–668.[CrossRef]
41. Darem,A.A.; Ghaleb,F.A.; Al-Hashmi,A.A.; Abawajy,J.H.; Alanazi,S.M.; Al-Rezami,A.Y.AnAdaptiveBehavioral-Based
IncrementalBatchLearningMalwareVariantsDetectionModelUsingConceptDriftDetectionandSequentialDeepLearning.
IEEEAccess2021,9,97180–97196.[CrossRef]
42. Das,M.;Pratama,M.;Savitri,S.;Zhang,J.MUSE-RNN:AMultilayerSelf-EvolvingRecurrentNeuralNetworkforDataStream
Classification.InProceedingsoftheIEEEInternationalConferenceonDataMining(ICDM),Beijing,China,8–11November2019;
pp.110–119.[CrossRef]
43. Badri,A.K.;Heikal,J.;Terah,Y.A.;Nurjaman,D.R.Decision-MakingTechniquesusingLSTMonAntamMiningSharesbefore
andduringtheCOVID-19PandemicinIndonesia.AptisiTrans.Manag.2021,6,167–180.[CrossRef]
44. Saidani,I.;Ouni,A.;Mkaouer,M.W.Improvingthepredictionofcontinuousintegrationbuildfailuresusingdeeplearning.
Autom.Softw.Eng.2022,29,21.[CrossRef]
45. Mansour,R.F.;Al-Otaibi,S.;Al-Rasheed,A.;Aljuaid,H.;Pustokhina,I.V.;Pustokhin,D.A.AnOptimalBigDataAnalyticswith
ConceptDriftDetectiononHigh-DimensionalStreamingData.Comput.Mater.Contin.2021,68,2843–2858.[CrossRef]
46. Alencar,B.M.;Canário,J.P.;Neto,R.L.;Prazeres,C.;Bifet,A.;Rios,R.A.Fog-DeepStream:AnewapproachcombiningLSTMand
ConceptDriftfordatastreamanalyticsonFogcomputing.InternetThings2023,22,100731.[CrossRef]
47. Luo,X.;Zhang,D.Anadaptivedeeplearningframeworkforday-aheadforecastingofphotovoltaicpowergeneration.Sustain.
EnergyTechnol.Assess.2022,52,16.[CrossRef]
48. Diez-Olivan,A.;Ortego,P.;DelSer,J.;Landa-Torres,I.;Galar,D.;Camacho,D.;Sierra,B.AdaptiveDendriticCell-DeepLearning
ApproachforIndustrialPrognosisUnderChangingConditions.IEEETrans.Ind.Inform.2021,17,7760–7770.[CrossRef]
49. Cheng,M.-M.;Jiang,P.-T.;Han,L.-H.;Wang,L.;Torr,P.DeeplyExplainCNNViaHierarchicalDecomposition.Int.J.Comput.Vis.
2023,131,1091–1105.[CrossRef]
50. Gu, J.; Wang, Z.; Kuen, J.; Ma, L.; Shahroudy, A.; Shuai, B.; Liu, T.; Wang, X.; Wang, G.; Cai, J.; et al. Recent advances in
convolutionalneuralnetworks.PatternRecognit.2018,77,354–377.[CrossRef]
51. Li,X.;Zhang,Z.;Zhao,Z.;Wu,L.;Huo,J.;Zhang,J.;Wang,Y.ECNN:OneOnlineDeepLearningModelforStreamingOcean
DataPrediction.InProceedingsoftheACMInternationalConferenceonIntelligentComputingandItsEmergingApplications,
Jinan,China,28–29December2021;p.6.
52. Saadallah,A.;Jakobs,M.;Morik,K.ExplainableOnlineDeepNeuralNetworkSelectionUsingAdaptiveSaliencyMapsforTime
SeriesForecasting.InMachineLearningandKnowledgeDiscoveryinDatabases.ResearchTrack;Oliver,N.,Pérez-Cruz,F.,Kramer,S.,
Read,J.,Lozano,J.A.,Eds.;SpringerInternationalPublishing:Cham,Switzerland,2021;Volume12975,pp.404–420.[CrossRef]
53. Tian,X.;Ng,W.W.Y.;Xu,H.DeepIncrementalHashingforSemanticImageRetrievalwithConceptDrift.IEEETrans.BigData
2023,1–13.[CrossRef]
54. Lobo,J.L.;Laña,I.;DelSer,J.;Bilbao,M.N.;Kasabov,N.EvolvingSpikingNeuralNetworksforonlinelearningoverdriftingdata
streams.NeuralNetw.2018,108,1–19.[CrossRef]
55. Da’u, A.; Salim, N. Recommendation system based on deep learning methods: A systematic review and new directions.
Artif.Intell.Rev.2020,53,2709–2748.[CrossRef]
56. Deng,L.Atutorialsurveyofarchitectures,algorithms,andapplicationsfordeeplearning.APSIPATrans.SignalInf.Process.2014,
3,e2.[CrossRef]
57. Bank,D.;Koenigstein,N.;Giryes,R.Autoencoders.arXiv2021,arXiv:2003.05991.

Appl.Sci.2023,13,6515 25of27
58. Yoon,S.;Lee,Y.;Lee,J.-G.;Lee,B.S.AdaptiveModelPoolingforOnlineDeepAnomalyDetectionfromaComplexEvolvingData
Stream.InProceedingsofthe28thACMSIGKDDConferenceonKnowledgeDiscoveryandDataMining,Washington,DC,USA,
14–18August2022;pp.2347–2357.[CrossRef]
59. Friedrich, B.; Sawabe, T.; Hein, A. Unsupervised statistical concept drift detection for behaviour abnormality detection.
Appl.Intell.2022,53,2527–2537.[CrossRef]
60. Ashfahani,A.;Pratama,M.;Lughofer,E.;Ong,Y.-S.DEVDAN:Deepevolvingdenoisingautoencoder.Neurocomputing2020,390,
297–314.[CrossRef]
61. Bhatia, S.; Jain, A.; Srivastava, S.; Kawaguchi, K.; Hooi, B.MemStream: Memory-BasedStreamingAnomalyDetection. In
ProceedingsoftheACMWebConference2022,Lyon,France,25–29April2022;pp.610–621.[CrossRef]
62. Goodfellow,I.;Pouget-Abadie,J.;Mirza,M.;Xu,B.;Warde-Farley,D.;Ozair,S.;Courville,A.;Bengio,Y.Generativeadversarial
networks.Commun.ACM2020,63,139–144.[CrossRef]
63. Guan,H.;Wang,Y.;Ma,X.;Li,Y.DCIGAN:ADistributedClass-IncrementalLearningMethodBasedonGenerativeAdversarial
Networks.InProceedingsoftheIEEEIntlConfonParallel&DistributedProcessingwithApplications,BigData&CloudCom-
puting,SustainableComputing&Communications,SocialComputing&Networking(ISPA/BDCloud/SocialCom/SustainCom),
RiodeJaneiro,Brazil,20–24May2019;pp.768–775.[CrossRef]
64. Guzy,F.;Wozniak,M.;Krawczyk,B.EvaluatingandExplainingGenerativeAdversarialNetworksforContinualLearningunder
ConceptDrift.InProceedingsoftheInternationalConferenceonDataMiningWorkshops(ICDMW),Auckland,NewZealand,
7–10December2021;pp.295–303.[CrossRef]
65. Zhang,N.;Ding,S.;Zhang,J.;Xue,Y.AnoverviewonRestrictedBoltzmannMachines.Neurocomputing2018,275,1186–1199.
[CrossRef]
66. Korycki,L.;Krawczyk,B.ConceptDriftDetectionfromMulti-ClassImbalancedDataStreams.InProceedingsoftheIEEE37th
InternationalConferenceonDataEngineering(ICDE),Chania,Greece,19–22April2021;pp.1068–1079.
67. Wang,W.;Zhang,M.DataStreamAdaptivePartitioningofSlidingWindowBasedonGaussianRestrictedBoltzmannMachine.
InArtificialIntelligenceinChina;Liang,Q.,Wang,W.,Mu,J.,Liu,X.,Na,Z.,Chen,B.,Eds.;Springer:Singapore,2020;Volume572,
pp.220–228.[CrossRef]
68. Miljkovic,D.Briefreviewofself-organizingmaps. InProceedingsofthe40thInternationalConventiononInformationand
CommunicationTechnology,ElectronicsandMicroelectronics(MIPRO),Opatija,Croatia,22–26May2017;pp.1061–1066.
69. Cerri,R.;Junior,J.D.C.;Faria,E.R.;Gama,J.Anewself-organizingmapbasedalgorithmformulti-labelstreamclassification.In
Proceedingsofthe36thAnnualACMSymposiumonAppliedComputing,VirtualEventRepublicofKorea,22–26March2021.
[CrossRef]
70. Wiwatcharakoses,C.;Berrar,D.SOINN+,aSelf-OrganizingIncrementalNeuralNetworkforUnsupervisedLearningfromNoisy
DataStreams.ExpertSyst.Appl.2020,143,113069.[CrossRef]
71. Zheng,W.;Zhao,P.;Chen,G.;Zhou,H.;Tian,Y.AHybridSpikingNeuronsEmbeddedLSTMNetworkforMultivariateTime
SeriesLearningunderConcept-driftEnvironment.IEEETrans.Knowl.DataEng.2022,1–14.[CrossRef]
72. Sun,L.;Ji,Y.;Zhu,M.;Gu,F.;Dai,F.;Li,K.Anewpredictivemethodsupportingstreamingdatawithhybridrecurringconcept
driftsinprocessindustry.Comput.Ind.Eng.2021,161,107625.[CrossRef]
73. Wang,L.;Chen,S.;Chen,F.;He,Q.;Liu,J.B-Detection:RuntimeReliabilityAnomalyDetectionforMECServiceswithBoosting
LSTMAutoencoder.IEEETrans.Mob.Comput.2023,1–14.[CrossRef]
74. Yen,S.; Moh,M.; Moh,T.-S.CausalConvLSTM:Semi-SupervisedLogAnomalyDetectionThroughSequenceModeling. In
Proceedingsofthe18thIEEEInternationalConferenceonMachineLearningAndApplications(ICMLA),BocaRaton,FL,USA,
16–19December2019;pp.1334–1341.
75. Perera,P.P.B.AnomalyDetectiononSingleVariateTimeSerieswithConceptdrifts.Ph.D.Thesis,UniversityofColomboSchool
ofComputing,Colombo,SriLanka,2021.
76. Zhang,X.;Zou,Y.;Li,S.EnhancingincrementaldeeplearningforFCCUend-pointqualityprediction.Inf.Sci.2020,530,95–107.
[CrossRef]
77. Museba,T.;Nelwamondo,F.;Ouahada,K.;Akinola,A.RecurrentAdaptiveClassifierEnsembleforHandlingRecurringConcept
Drifts.Appl.Comput.Intell.SoftComput.2021,2021,5533777.[CrossRef]
78. Massaoudi,M.;Chihi,I.;Abu-Rub,H.;Refaat,S.S.;Oueslati,F.S.ConvergenceofPhotovoltaicPowerForecastingandDeep
Learning:State-of-ArtReview.IEEEAccess2021,9,136593–136615.[CrossRef]
79. Mnih, V.; Kavukcuoglu, K.; Silver, D.; Rusu, A.A.; Veness, J.; Bellemare, M.G.; Graves, A.; Riedmiller, M.; Fidjeland, A.K.;
Ostrovski,G.;etal.Human-levelcontrolthroughdeepreinforcementlearning.Nature2015,518,529–533.[CrossRef]
80. Zhang,D.;ChinaElectricPowerResearchInstitute;Han,X.;Deng,C.TaiyuanUniversityofTechnology.Reviewontheresearch
andpracticeofdeeplearningandreinforcementlearninginsmartgrids.CSEEJ.PowerEnergySyst.2018,4,362–370.[CrossRef]
81. Tan,C.;Sun,F.;Kong,T.;Zhang,W.;Yang,C.;Liu,C.ASurveyonDeepTransferLearning.InProceedingsofthe27thInternational
ConferenceonArtificialNeuralNetworks,Rhodes,Greece,4–7October2018.[CrossRef]
82. Kauschke,S.;Lehmann,D.H.;Furnkranz,J.PatchingDeepNeuralNetworksforNonstationaryEnvironments.InProceedingsof
theInternationalJointConferenceonNeuralNetworks(IJCNN),Budapest,Hungary,14–19July2019.
83. Disabato,S.;Roveri,M.LearningConvolutionalNeuralNetworksinpresenceofConceptDrift.InProceedingsoftheInternational
JointConferenceonNeuralNetworks(IJCNN),Budapest,Hungary,14–19July2019;p.8.[CrossRef]

Appl.Sci.2023,13,6515 26of27
84. Pratama, M.; de Carvalho, M.; Xie, R.; Lughofer, E.; Lu, J. ATL: Autonomous Knowledge Transfer from Many Streaming
Processes.InProceedingsofthe28thACMInternationalConferenceonInformationandKnowledgeManagement,Beijing,China,
3–7November2019.
85. Xu,L.;Ding,X.;Peng,H.;Zhao,D.;Li,X.ADTCD:AnAdaptiveAnomalyDetectionApproachTowardsConcept-DriftinIoT.
IEEEInternetThingsJ.2023,1–13.[CrossRef]
86. Yang, T.; Tang, H.; Bai, C.; Liu, J.; Hao, J.; Meng, Z.; Liu, P.; Wang, Z. Exploration in Deep Reinforcement Learning: A
ComprehensiveSurvey.arXiv2022,arXiv:2109.06668.
87. Soleymani,F.;Paquet,E.Deepgraphconvolutionalreinforcementlearningforfinancialportfoliomanagement—DeepPocket.
ExpertSyst.Appl.2021,182,115127.[CrossRef]
88. Zhang,Q.;Wang,Z.;Long,C.;Huang,C.;Yiu,S.M.;Liu,Y.;Cong,G.;Shi,J.OnlineAnomalousSubtrajectoryDetectiononRoad
NetworkswithDeepReinforcementLearning.arXiv2022,arXiv:2211.08415.[CrossRef]
89. Saadallah,A.;Morik,K.OnlineEnsembleAggregationusingDeepReinforcementLearningforTimeSeriesForecasting. In
Proceedings of the IEEE 8th International Conference on Data Science and Advanced Analytics (DSAA), Porto, Portugal,
6–9October2021;pp.1–8.[CrossRef]
90. Yu, H.; Chen, Z.; Zhang, X.; Chen, X.; Zhuang, F.; Xiong, H.; Cheng, X. FedHAR: Semi-Supervised Online Learning for
PersonalizedFederatedHumanActivityRecognition.IEEETrans.Mob.Comput.2021,22,3318–3332.[CrossRef]
91. Liu,Z.;Loo,C.K.;Pasupa,K.;Seera,M.Meta-cognitiverecurrentkernelonlinesequentialextremelearningmachinewithkernel
adaptivefilterforconceptdrifthandling.Eng.Appl.Artif.Intell.2020,88,103327.[CrossRef]
92. daSilva,C.A.S.;Krohling,R.A.Semi-SupervisedOnlineElasticExtremeLearningMachinewithForgettingParametertodeal
withconceptdriftindatastreams.InProceedingsoftheInternationalJointConferenceonNeuralNetworks(IJCNN),Budapest,
Hungary,14–19July2019;pp.1–8.
93. Tsukada,M.;Kondo,M.;Matsutani,H.ANeuralNetwork-BasedOn-deviceLearningAnomalyDetectorforEdgeDevices.
IEEETrans.Comput.2020,69,1027–1044.[CrossRef]
94. Asuncion,A.;Newman,D.UCIMachineLearningRepository;UniversityofCalifornia:Irvine,CA,USA,2007.
95. Harries,M.;Wales,N.S.Splice-2ComparativeEvaluation:ElectricityPricing;ResearchGate:Berlin,Germany,1999.
96. Elwell,R.;Polikar,R.IncrementalLearningofConceptDriftinNonstationaryEnvironments.IEEETrans.NeuralNetw.2011,22,
1517–1531.[CrossRef]
97. Katakis,I.;Tsoumakas,G.;Vlahavas,I.Trackingrecurringcontextsusingensembleclassifiers:Anapplicationtoemailfiltering.
Knowl.Inf.Syst.2010,22,371–391.[CrossRef]
98. Lopez-Paz,D.;Ranzato,M.A.GradientEpisodicMemoryforContinualLearning.arXiv2022,arXiv:1706.08840.
99. Street,W.N.;Kim,Y.Astreamingensemblealgorithm(SEA)forlarge-scaleclassification.InProceedingsoftheseventhACM
SIGKDDinternationalconferenceonKnowledgediscoveryanddatamining,SanFrancisco,CA,USA,26–29August2001;ACM
Press:NewYork,NY,USA,2001;pp.377–382.
100. Gama,J.;Medas,P.;Castillo,G.;Rodrigues,P.LearningwithDriftDetection. InAdvancesinArtificialIntelligence—SBIA2004;
Bazzan,A.L.C.,Labidi,S.,Eds.;Springer:Berlin/Heidelberg,Germany,2004;Volume3171,pp.286–295.[CrossRef]
101. Fan,W.;Yu,P.;Han,J.MiningConcept-DriftingDataStreamsusingEnsembleClassifiers.InProceedingsofthe9thACMSIGKDD
InternationalConferenceonKnowledgeDiscoveryandDataMining,Washington,DC,USA,24–27August2003;p.10.
102. Kakisim,A.G.;Nar,M.;Sogukpinar,I.Metamorphicmalwareidentificationusingengine-specificpatternsbasedonco-opcode
graphs.Comput.Stand.Interfaces2020,71,103443.[CrossRef]
103. Anguita,D.;Ghio,A.;Oneto,L.;Parra-Llanas,X.;Reyes-Ortiz,J.ProceedingsoftheInternationalConferenceonEuropeanSymposium
onArtificialNeuralNetworks(ESANN);ESAN:Bruges,Belgium,2013;Volume3,p.3.
104. Coates,A.;Ng,A.;Lee,H.Ananalysisofsingle-layernetworksinunsupervisedfeaturelearning. InProceedingsofthe14th
InternationalConferenceonArtificialIntelligenceandStatistics,FortLauderdale,FL,USA,11–13April2011;pp.215–223.
105. Elson,J.;Douceur,J.R.;Howell,J.;Saul,J.Asirra:ACAPTCHAthatexploitsinterest-alignedmanualimagecategorization.CCS
2007,7,366–374.
106. Krizhevsky,A.;Hinton,G.LearningMultipleLayersofFeaturesfromTinyImages;UniversityofToronto:Toronto,ON,Canada,2009.
107. Xu, W.; Huang, L.; Fox, A.; Patterson, D.; Jordan, M.I. Detecting large-scale system problems by mining console logs. In
ProceedingsoftheACMSIGOPS22ndSymposiumonOperatingSystemsPrinciples,BigSky,MT,USA,11–14October2009;
ACMPress:NewYork,NY,USA,2009.
108. Sharafaldin, I.; Lashkari, A.H.; Ghorbani, A.A. Toward generating a new intrusion detection dataset and intrusion traffic
characterization.InProceedingsoftheInternationalConferenceonInformationSystemsSecurityandPrivacy,Funchal,Portugal,
22–24January2018;pp.108–116.
109. Pang,G.;Shen,C.;Cao,L.;Hengel,A.V.D.Deeplearningforanomalydetection:Areview.ACMComput.Surv.2021,54,1–38.
[CrossRef]
110. Ganaie,M.A.;Hu,M.;Malik,A.;Tanveer,M.;Suganthan,P.Ensembledeeplearning:Areview.Eng.Appl.Artif.Intell.2022,115,
105151.[CrossRef]

Appl.Sci.2023,13,6515 27of27
111. Yang,W.;Li,Z.;Liu,M.;Lu,Y.;Cao,K.;Maciejewski,R.;Liu,S.Diagnosingconceptdriftwithvisualanalytics.InProceedingsof
theIEEEConferenceonVisualAnalyticsScienceandTechnology(VAST),SaltLakeCity,UT,USA,25–30October2020;pp.12–23.
112. Stiglic,G.;Kokol,P.InterpretabilityofSuddenConceptDriftinMedicalInformaticsDomain.InProceedingsoftheIEEE11th
InternationalConferenceonDataMiningWorkshops,Vancouver,BC,Canada,11–14December2011;pp.609–613.[CrossRef]
Disclaimer/Publisher’s Note: The statements, opinions and data contained in all publications are solely those of the individual
author(s)andcontributor(s)andnotofMDPIand/ortheeditor(s).MDPIand/ortheeditor(s)disclaimresponsibilityforanyinjuryto
peopleorpropertyresultingfromanyideas,methods,instructionsorproductsreferredtointhecontent.