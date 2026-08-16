---
conversion_metadata:
  converted_at: "2026-07-21T14:08:47Z"
  converter_tool: "markitdown"
  converter_version: "0.1.6"
  source_pdf: "Ma P. et al.pdf"
  source_pdf_sha256: "34c4f511ee6ea632c604913f62d2683fe877668d862316b647ae51e58dd90fce"
  page_count: 17
  markdown_char_count: 127878
---

<!-- PAGE-AWARE EXTRACTION (via pdfminer.six) -->

<!-- PAGE 1 -->

Review
Review of Family-Level Short-Term Load Forecasting and Its
Application in Household Energy Management System

Ping Ma 1,†, Shuhui Cui 1,†, Mingshuai Chen 2, Shengzhe Zhou 3 and Kai Wang 1,*

1

School of Electrical Engineering, Weihai Innovation Research Institute, Qingdao University,
Qingdao 266000, China; qdumaping@163.com (P.M.); cuishuhui321@163.com (S.C.)

2 Rizhao Power Supply Company, State Grid Shandong Electric Power Company, Rizhao 276826, China;

chenmingshuaizsz@163.com

3 Department of Information Engineering, Shandong Water Conservancy Vocational College,

Rizhao 276826, China; zhoushengzheyx@126.com

* Correspondence: wangkai@qdu.edu.cn or wkwj888@163.com; Tel.: +86-15863060145; Fax: +86-532-85951980
†

These authors contributed equally to this work.

Abstract: With the rapid development of smart grids and distributed energy sources, the home
energy management system (HEMS) is becoming a hot topic of research as a hub for connecting
customers and utilities for energy visualization. Accurate forecasting of future short-term residential
electricity demand for each major appliance is a key part of the energy management system. This
paper aims to explore the current research status of household-level short-term load forecasting,
summarize the advantages and disadvantages of various forecasting methods, and provide research
ideas for short-term household load forecasting and household energy management. Firstly, the paper
analyzes the latest research results and research trends in deep learning load forecasting methods
in terms of network models, feature extraction, and adaptive learning; secondly, it points out the
importance of combining probabilistic forecasting methods that take into account load uncertainty
with deep learning techniques; and further explores the implications and methods for device-level
as well as ultra-short-term load forecasting. In addition, the paper also analyzes the importance of
short-term household load forecasting for the scheduling of electricity consumption in household
energy management systems. Finally, the paper points out the problems in the current research and
proposes suggestions for future development of short-term household load forecasting.

Keywords: home energy management systems; household-level load forecasting; short-term load;
deep learning neural networks; probabilistic forecasting

1. Introduction

With the development of the economy and living standards, household-based electri-
cal energy consumption accounts for an increasing proportion of total energy consumption,
and how to use electrical energy more efﬁciently is the key to reducing residential energy
consumption. In addition, with the development of energy saving and emission reduction
policies and distributed energy sources, energy management with the home energy man-
agement system (HEMS) as the main energy saving countermeasure has gradually become
the focus of residential energy optimization research [1]. Accurate forecasting of future
residential electricity demand in the short term is an intelligent decision-making tool for
energy management systems. It is therefore important to study methods for predicting
household-level and even device-level loads with high forecasting accuracy.

Load forecasting methods can generally be classiﬁed according to the forecasting
time scale: long-term load forecasting (LTLF), medium-term load forecasting (MTLF),
short-term load forecasting (STLF), and very short-term load forecasting (VSTLF). Among
them, short-term load forecasting can provide effective energy system planning, which is
important for energy management [2,3]. Traditional short-term load forecasting has focused

Citation: Ma, P.; Cui, S.; Chen, M.;

Zhou, S.; Wang, K. Review of

Family-Level Short-Term Load

Forecasting and Its Application in

Household Energy Management

System. Energies 2023, 16, 5809.

https://doi.org/10.3390/en16155809

Academic Editor: Paulo Santos

Received: 20 June 2023

Revised: 23 July 2023

Accepted: 2 August 2023

Published: 4 August 2023

Copyright: © 2023 by the authors.

Licensee MDPI, Basel, Switzerland.

This article is an open access article

distributed under

the terms and

conditions of the Creative Commons

Attribution (CC BY) license (https://

creativecommons.org/licenses/by/

4.0/).

Energies 2023, 16, 5809. https://doi.org/10.3390/en16155809

https://www.mdpi.com/journal/energies

---

<!-- PAGE 2 -->

Energies 2023, 16, 5809

2 of 17

on the system level, substation level, busbar level, feeder level, and building level. Unlike
system-level electrical loads, individual household loads lack a clear consistent pattern
conducive to forecast accuracy. In general, the diversity of aggregation levels smooths
out the daily load distribution, which makes substation loads relatively more predictable,
while individual household electricity consumption is more dependent on underlying
human behavior. Within individual households, the daily habits and lifestyles of residents
may have a more direct impact on the short-term load distribution. The randomness and
uncertainty caused by human behavior or weather changes make it difﬁcult to accurately
implement more established system-level load forecasting methods at the household level.
With the widespread installation of smart meters, household electricity consumption
data are available and household-level load forecasting is possible. Accurate short-term
load forecasting (STLF) can properly complement the HEMS and support utilities to imple-
ment more rational demand response strategies to reduce operational costs [4]. In recent
years, in order to further improve the accuracy of short-term household load forecasting,
there have been many related studies at home and abroad, proposing various forecasting
methods including probabilistic load forecasting and various deep learning algorithms.
The aim of this paper is to review the research papers in this ﬁeld, compare the accuracy
and advantages and disadvantages of various forecasting methods, and give effective
suggestions for the research of household-level load forecasting methods.

The rest of the paper is organized as follows:

1.

2.

3.

4.

Section 2 introduces the application of deep learning algorithms such as RNN, LSTM,
and CNN in household load forecasting, and analyzes the improvement of the algo-
rithms in terms of fusion of models, feature analysis and extraction, and adaptive
learning of networks.
Section 3 explores the advantages of probabilistic forecasting methods and proposes
a research direction to improve traditional probabilistic forecasting methods with
advanced deep learning algorithms.
Section 4 analyzes the development trends and challenges of ultra-short-term device-
level load forecasting.
Section 5 presents the principles of the HEMS and the key role played by home-level
load forecasting in the HEMS.

2. Deep Learning-Based Load Prediction Methods

There are many research methods on load forecasting, from classical time series
analysis to more recent machine learning methods, including the Autoregressive Integrated
Moving Average Model (ARIMA) [5], Support Vector Regression (SVR) [6], Random Forest
(RF) [7], and Gradient Boosting Regression (GBR) [8]. Another important branch of load
forecasting is the use of artiﬁcial neural network (ANN) models [9] for forecasting. In recent
years, with the increase in relevant load data and massively parallel computing capabilities,
load prediction using big data has become a hot research topic. Against the backdrop of
massive data and signiﬁcant growth in parallel computing performance, deep learning
(DL) is approaching or even surpassing humans in areas such as speech recognition and
image classiﬁcation and is gradually becoming the model of choice for many researchers to
improve load prediction methods.

2.1. Neural Network Prediction Models

In recent years, deep learning has become one of the most active techniques in many
areas of research. In contrast to shallow learning, deep learning typically refers to stacking
multiple layers of neural networks and relying on stochastic optimization to perform ma-
chine learning tasks. Different numbers of layers can provide different levels of abstraction
to improve learning ability and task performance. In particular, long short-term memory
(LSTM) recurrent neural networks (RNNs), proposed by Hochreiter and Schmidhuber [10],
have received a great deal of attention in the ﬁeld of sequence learning.

---

<!-- PAGE 3 -->

Energies 2023, 16, 5809

3 of 17

2.1.1. LSTM Model

Often, deep learning models encounter the problem of gradient explosion (i.e., learning
scattering) or gradient disappearance (i.e., learning stopping). This problem is solved by
LSTM networks that introduce memory cells and computational gates. LSTM is a type of
RNN that has been used in the past for time series analysis and load prediction problems.
A load proﬁle can be thought of as a time series in which there is a high degree
of correlation and dependence between successive samples. Long short-term memory
(LSTM) has the structure of a recurrent neural network with the characteristics of sequence
learning [2]. The LSTM structure has a memory unit that allows it to remember the
signiﬁcant states of the previous steps. In addition, LSTM has an oblivion gate to remove
unimportant features and reset the memory unit, as shown in Figure 1. LSTM can also
track customer consumption behavior by learning long-term dependencies and correlations
between successive samples of sequential data.

Figure 1. The structure of an LSTM: (a) The structure of an LSTM block. (b) The unrolled LSTM
sequential architecture.

It is generally assumed that the lifestyles of the inhabitants, however inconsistent, will
be reﬂected in repeated patterns of energy consumption. Kong et al. [11] proposed a load
prediction framework based on an LSTM cyclic neural network (Figure 2). The results show
that the prediction accuracy of LSTM is better than several other advanced machine learning
algorithms. In the later work, people try to improve the LSTM algorithm in order to obtain
higher prediction accuracy. In view of the uncertainty and non-linear characteristics of
household load data, the EMD method can transform non-stationary non-linear data into
stationary linear data. Liu et al. [12] proposed a combination algorithm of empirical mode
decomposition (EMD) and stack long short-term memory (SLSTM) that has been applied to

---

<!-- PAGE 4 -->

Energies 2023, 16, 5809

4 of 17

household short-term load prediction. This SLSTM can train better parameters and improve
the accuracy of prediction. SVR has the characteristic of linearly reﬂecting input–output
relationships. Combined with this characteristic, Moradzadeh et al. [13] proposed an
improved hybrid method of support vector regression—long-term and short-term memory
(SCR–LSTM) for short-term load prediction of a microgrid. The SVR–LSTM model with
the highest correlation coefﬁcient (R = 0.9901) and the lowest error value can provide
better results than the traditional SVR and LSTM. However, the data set used to verify
the method is not load data for single households and does not account for weather and
human uncertainties. Nevertheless, hybrid approaches such as these are widely proposed.

Figure 2. The LSTM-based forecasting framework.

---

<!-- PAGE 5 -->

Energies 2023, 16, 5809

5 of 17

2.1.2. CNN Model

CNN is a type of deep neural network which is most commonly used to analyze visual
images. CNN uses the method of local connection and weight sharing to process the original
data at a higher level and more abstract, which can effectively and automatically extract
the internal features in the data. The internal neural network layer is mainly composed of a
convolutional layer, pooling layer, and full connection layer, which reduces the number of
weights and network complexity. CNN automatically extracts feature vectors from data,
effectively reducing the complexity of feature extraction and data reconstruction, improving
the quality of data features, and obtaining effective information through a convolution
layer and pooling, greatly reducing the training time of the model.

Since LSTM utilizes the time locality of load time series by analogy with the spatial
locality in image processing, CNN seems to be able to obtain better accuracy when we
lack historical data, the size of the energy entity is small, and the prediction range is short
(forecast one day in advance). Based on the combination of convolutional neural networks
(CNNs) and data enhancement technology, Acharya et al. [14] converted the time series of
single household load data into multiple time series of residual load, which could artiﬁcially
enlarge the training data. This method can solve the problem caused by the lack of historical
data and improve the accuracy of residential load forecasting. In order to give full play to
the advantages of CNN, Andriopoulos et al. [15] proposed a method based on statistical
analysis to preprocess the time series data before solving the problem of short-term load
prediction. The main feature of this method is to optimize the superparameters of a neural
network by using the statistical attributes of each time series data set and transform the
given data set into a form that allows maximum advantage of the CNN algorithm. In
addition, the literature [16] designed a CNNGRU short-term load prediction model based
on the attention mechanism, and effectively classiﬁed the household load data according to
the household behavior. The accuracy of this method reaches 92.06% in small-range load
prediction. Compared with the general deep learning time series prediction model, the
prediction time of this method is reduced by 75%.

2.1.3. Hybrid Model

A comparison of several prediction models is shown in Table 1. Although CNNs
have their unique advantages in load prediction, the efﬁciency of LSTMs for long-term
dependencies is unquestionable. Therefore, the hybrid LSTM–CNN model becomes a
reliable deep learning load prediction method worthy of further study, especially when
multi-step methods are considered.

Table 1. Comparison of several forecasting models.

Model

Advantage

Shortcomings

Application Situation

Classical time series
model

LSTM

CNN

Simple to understand,
modeling time is short
Able to learn long-term
dependencies
Features can be learned
automatically

Poor performance on complex
time series prediction problems

Risk of overﬁtting the model

Not good for non-linear time
series data

Simple time series data prediction

Process non-linear and
non-stationary time series data
Lack of historical data, short
forecast time

Jiang et al. [17] proposed a multi-task, multi-information fusion deep learning frame-
work (MFDL) that combines long and short-term memory (LSTM) and a convolutional
neural network (CNN) to learn both near-term and long-term regular behavior, learning
near-term electricity consumption behavior by LSTM and long-term regular electricity
consumption behavior features by CNN. Experimental results show that this method
can signiﬁcantly improve the accuracy of single household short-term load prediction.
Guo et al. [18] also used convolutional neural network (CNN) and long and short-term
memory (LSTM) to capture temporal short-term local information and long-term corre-

---

<!-- PAGE 6 -->

Energies 2023, 16, 5809

6 of 17

lation information, respectively, and used an autoregressive (AR) model as the linear
component; experimental results show that this LST Net network model can better adapt
to time series and complex non-linear load data relationships. It has higher prediction
and generalization performance compared with ARIMA and CNN–LSTM models. And
based on an improved LSTM, Syed et al. [19] proposed a hybrid model (HSBUFC) based on
bidirectional and unidirectional LSTM superposition coupled with fully connected dense
layers, which ampliﬁes the advantages of unidirectional LSTMs, bidirectional LSTMs, and
RNN superposition for energy consumption prediction accuracy. The model outperforms
other hybrid models such as the widely used convolutional (Conv) neural network–LSTM
and ConvLSTM in terms of accuracy.

In summary, there have been many studies proving the usefulness of neural network
prediction models in household load forecasting, and hybrid models based on the fusion of
multiple neural networks are being developed more frequently. Future research should
explore better deep learning models, such as deeper, wider, and more complex neural
networks, or use new models such as self-attentive mechanisms to improve prediction
accuracy and stability. Due to the volatility of loads, single forecasting models sometimes
fail to achieve high accuracy. Combining forecasts using multiple deep learning methods
can effectively improve model generalization. Meanwhile, in household load forecasting,
multiple tasks such as power forecasting, electricity consumption forecasting, and power
forecasting may be involved. Therefore, researchers can explore how to use multi-task
learning methods to solve multi-task prediction to improve the prediction performance of
the model while ensuring the prediction accuracy of the model.

2.2. Feature Extraction

When applying deep learning algorithms for load prediction, the input training set
X-train can be fed directly into the LSTM network as if no feature extraction was performed,
or it can be ﬁrst transformed into a new feature space and then the transformed X-train
matrix is applied to the LSTM network [20]. It is worth noting that the original load curve
consists of many points, which may contain a large amount of redundant information. All
lagged load values cannot be used for load prediction at subsequent points. In addition,
the time series may contain useful information about the relationship between loading
points that is not apparent in the original feature space [21,22]. Therefore, the application
of appropriate feature extraction to the variable vector of the load curve can show the
dependence, correlation, and inherent characteristics of the load curve, which is very
important to improve the accuracy of load prediction.

Figure 3 shows the electricity consumption of a washing machine in a family for a week.
It is not difﬁcult to see that not only different electrical appliances have different load curves,
but also the load curves of a single electrical appliance differ on different days of a week.
How to extract the highly correlated features from the load curve is very important. As
shown in Figure 4, the literature [3] uses the advantages of wavelet decomposition (DWT)
and cooperative representation (CRT) to extract the features of hysteresis load variables.
DWT can effectively separate useless details from the approximate components of variable
vectors, while CRT can extract local information of load value dependence in adjacent time
instances and adopt a regularization method to control major load ﬂuctuations adaptively
to avoid unwanted changes in signals. Kiprijanovska et al. [23] extracted features from
the context data (weather, calendar) and the historical load of all families in the data
set to integrate multiple information sources, and calculated novel domain-speciﬁc time
series features so that the system could better simulate the energy consumption pattern of
families. The proposed method does not depend on the current number of households in
the system and has great commercial potential for predicting electrical energy consumption
at the individual household level. In the literature [24], mutual information (MI) and
principal component analysis (PCA) were used to select features and reduce dimensions of
multi-dimensional weather inﬂuencing factors to avoid interference from unrelated factors.
Finally, three-dimensional weather variables (cumulative contribution rate of 93.93%) were

---

<!-- PAGE 7 -->

Energies 2023, 16, 5809

7 of 17

obtained from the 12-D weather inﬂuence factors, which greatly improved the prediction
speed of the Co-LSTM network.

Figure 3. Consumption load of clothes washer on different days of a week.

Figure 4. Proposed load forecasting framework containing preprocessing, feature extraction, and
forecasting.

---

<!-- PAGE 8 -->

Energies 2023, 16, 5809

8 of 17

2.3. Adaptive Learning of Networks

The traditional static load forecasting technology obtains the single value load forecast
by using the off-line training forecasting model of the consumption pattern of the historical
load. However, this technology cannot capture the dynamic changes of the real load
consumption pattern during the forecast period. If the real load consumption pattern
changes during the forecast period, the prediction accuracy will be greatly reduced. In
order to improve the shortcomings of the traditional forecasting technology, the online
adaptive learning ability of the network is developed, which can effectively capture the
dynamic change of load consumption, so as to improve the forecasting accuracy [25,26].
At the same time, the large-scale deployment of smart meters provides an opportunity for
ﬁne-grained load forecasting using real-time residential data.

Load forecasting for residential users is challenging because users with similar charac-
teristics may have different consumption patterns. With the improvement of computing
power, artiﬁcial neural network technology for time series prediction has become more
and more widely developed. In most cases, training DNNS focuses on developing a model
to predict the load consumption of a single house. To predict multiple loads on multiple
houses, the standard procedure is to create a new model for each house, which results
in high consumption of training time and computing power. Gomez-Rosero et al. [27]
proposed a method to develop DNNs for multiple time series prediction by evolving
only one architecture and adjusting the weights of each time series, a process similar to
migration learning. Fujimoto et al. [28] introduced a deep ESN architecture with high
afﬁnity to edge computing, proposed an effective online learning scheme to keep prediction
models up-to-date, and used real annual data from over 500 households to evaluate its
effectiveness. The proposed framework will make a signiﬁcant contribution in enabling pre-
dictive models otherwise suited to edge computing to exploit the beneﬁts of deep learning
architectures. Fekri et al. [29] proposed an online adaptive RNN load prediction method
capable of continuously learning from newly arrived data and adapting to new patterns.
The RNN is used to capture temporal dependencies, while the online aspect is continuous
by adding preprocessing, buffering, and tuning modules for learning. The preprocessing
module prepares the data for online learning, the tuning module adapts the neural network
hyperparameters to the newly arrived patterns, and the buffering module helps to learn
from particularly difﬁcult patterns and assists with conceptual drift.

Household load forecasting is a dynamic problem and has become a topical issue
to enable forecasting models to automatically update parameters according to changes
In future
in data in order to provide better accuracy and real-time load forecasting.
work, experimenting with different adaptive algorithms (e.g., online learning, recursive
learning, and incremental learning) to improve prediction models and validating their
adaptive performance and prediction accuracy in real data can help us ﬁnd the most
suitable algorithm for the task of household load forecasting.

3. Probabilistic Load Forecasting Methods

Traditional single-value forecasts are unable to assess the uncertainty in load demand
forecasts, and an accurate assessment of uncertainty is essential for applications such
as optimal stochastic decision-making. Probabilistic load forecasting (PLF) methods can
model the uncertainty in future electricity consumption [30,31]. Its load forecasting for
individual households can be fed into robust optimization algorithms for home energy
management, and probabilistic forecasting captures the probability of occurrence of each
predicted value within the forecast interval, providing more comprehensive probabilistic
information about future loads (Figure 5). Wang et al. [32] combined quantile regression
neural networks (QRNN), quantile regression random forests (QRRF), and quantile re-
gression gradient augmentation (QRGA) methods to select the weight-optimal process.
Feng et al. [33] introduced STLF–QMS, a q-learning dynamic model selection (QMS) with a
mixture of deterministic and probabilistic load prediction models. By simulating consump-
tion scenarios, Xia et al. [34] proposed a probabilistic load forecasting method based on

---

<!-- PAGE 9 -->

Energies 2023, 16, 5809

9 of 17

consumption scenarios, where the extracted scenarios can effectively characterize house-
hold electricity consumption habits and are used to calculate the probability of occurrence
of each consumption scenario for a single household in any future time horizon. In contrast,
combined with deep learning, Brusaferri et al. [35] proposed a new approach to probabilis-
tic load prediction based on Bayesian deep learning techniques to achieve a comprehensive
uncertainty characterization by capturing general patterns of stochastic uncertainty and
cognitive uncertainty counterparts. A ﬁrst step towards a comprehensive exploration of
Bayesian hybrid density networks for probabilistic load prediction was initiated.

Figure 5. (a) Framework of probabilistic load forecasting. (b) Framework of conditional probabilistic
load forecasting.

In conclusion, probabilistic load forecasting methods have the advantages of relia-
bility, ﬂexibility, scalability, and real-time in household load forecasting, but traditional
probabilistic load forecasting methods based on statistical modeling are not well adapted
to a wide range of complex load forecasting problems. The authors argue that combining
probabilistic forecasting methods with deep learning time series models (e.g., probabilistic
forecasting methods based on empirical modal decomposition), which consider both fore-
casting accuracy and deeply reﬂect electricity consumption habits, has very broad research
prospects.

4. Exploration of Ultra-Short-Term and Facility-Level Load Forecasting

Much of the work in household load forecasting has previously focused on forecasting
the load of the entire household. While total load forecasting is important, the distribution
of household loads is often affected when customers take individual actions to save energy
or shift loads, for example, by delaying the operation of dishwashers to nighttime and
thus avoiding peak electricity consumption. Therefore, the development of short-term load
forecasting models at the residential appliance level is also important.

4.1. Bottom-Up Approach to Household Load Forecasting

In recent years, advanced metering infrastructure (AMI) [36] has been widely de-
ployed, while the development of artiﬁcial intelligence has greatly improved the accuracy
of non-intrusive load monitoring (NILM) [37]. With the collaboration of AMI and NILM, a
wealth of accurate device-level energy consumption information is available, and a bottom-
up load forecasting framework based on this underlying data from domestic appliances is

---

<!-- PAGE 10 -->

Energies 2023, 16, 5809

10 of 17

a new way of thinking about forecasting. The bottom-up approach can signiﬁcantly reduce
forecasting errors, but also requires room and appliance-level electricity consumption data.
For individual households, energy consumption is often determined by the habits
of the residents, but their behavior is accompanied by a degree of randomness due to
a variety of factors. In general, however, similar factors will have a similar effect on
the consumption of household appliances. Therefore, it is feasible to model household
consumption behavior using statistical characteristics of appliance consumption in similar
historical periods. Gao et al. [38] proposed a bottom-up forecasting framework based
on the underlying data of the electricity consumption of household appliances. In the
proposed framework, load distributions for group households are obtained using a similar
day’s extraction module (considering external environmental and internal household
factors affecting energy consumption), a household behavior analysis module (developing
probabilities of appliance consumption behavior), and a household behavior prediction
module.

However, unfortunately, this framework has only been veriﬁed in the group data of
multiple groups of families, which has a better prediction effect on the load distribution
of group families. For a single family, Zheng et al. [39] et al. veriﬁed that the bottom-up
method equipped with the long- and short-term memory cyclic neural network (LSTM)
model could obtain better results than the direct prediction at the family level. However,
for practical applications of the bottom-up approach, the LSTM model is inefﬁcient and
expensive. In order to effectively model a variety of different device usage patterns, a more
realistic lightweight algorithm is applied—the Kalman ﬁlter model adaptively predicts
device usage with less historical data and shorter computational time, outperforming large
algorithms such as the LSTM model. The literature [40] proposed a bottom-up method
considering the load characteristics of the equipment level. Considering the working
principle and load characteristics of home appliances, home appliances were divided into
continuous load and intermittent load. Through the accumulation of home appliance
loads, more reﬁned load prediction could be achieved. At the same time, considering the
ﬂuctuation of load curve, the loess-based seasonal trend decomposition program (STL) was
applied to continuous load appliances to obtain ﬁner grain and more regular load data.
The model can predict multiple equipment simultaneously and improve the computational
efﬁciency.

In the HEMS, predictions of short-term future electricity consumption are used to
support HEMS decision-making. Although there have been many studies on the predic-
tion of building electricity consumption, there is a lack of spatial analysis of predictive
performance, especially at the household level, the appliance level, or the submeter level.
Zheng et al. [4] adopted a LSTM neural network to establish a multi-step load prediction
model, as shown in Figure 6. The inﬂuence of spatial factors on the forecasting accuracy
of household electricity consumption was analyzed. The results showed that the predic-
tion accuracy can be improved by predicting the electricity consumption of household
appliances ﬁrst and then by aggregating, compared with predicting the electricity consump-
tion of households directly. Using deep learning technology to train the network based
on historical data of energy use of residential appliances, it is also possible to estimate
the energy use of a given appliance in the short term. Razghandi et al. [41] proposed a
residential electricity load forecasting model. This model used an LSTM cyclic neural
network to learn the energy consumption pattern of individual appliances in smart homes.
After preprocessing the data collected by smart meters, we inputted it into the deep neural
network to generate the predicted load consumption of devices and predicted the potential
load consumption of a given appliance at different time intervals.

---

<!-- PAGE 11 -->

Energies 2023, 16, 5809

11 of 17

Figure 6. Framework for the proposed appliance-level load forecasting deep learning-based model.

A bottom-up load prediction method requires accurate load prediction for each house-
hold appliance. This kind of device-level load prediction is a very challenging task. Pre-
vious studies have provided several forecasting frameworks, although they all have had
good simulation effects [42,43]. However, their feasibility still needs to be studied. The
deep learning algorithms used by the framework are relatively simple, and most of them
cannot give consideration to both accuracy and efﬁciency. According to the author, from
the power performance of equipment, the living habits of household users, the structural
characteristics of intelligent prediction algorithm, and so on, the probabilistic prediction
method considering load uncertainty is integrated, and the improved LSTM neural network
which has proved to be the most advanced load prediction algorithm is used. It is a worthy
research direction to develop a set of equipment-level load forecasting models which take
into account both prediction accuracy and practical feasibility.

4.2. The Challenge of Hourly Load Forecasting

On the other hand, with the deployment of IOT devices in buildings, electricity load
usage can be collected in real time, and the real-time data collection and processing makes
ultra-short-term load prediction at the hour level possible [44]. The literature [45] uses BN
to simulate the relationship between variables and proposes a multi-family ultra-short-term
load forecasting method that does not use a single generalist model and multivariate data
for load aggregation. Ageng et al. [46] proposed an hourly load prediction framework
combining data preparation and LSTM. Firstly, interpolation and Savitzky–Golay ﬁltering
were carried out on the collected data so as to extract the appropriate load consumption
mode for the next hour’s load prediction. In addition, in order to better determine the
relationship between the time series information, a two-layer LSTM was used.

It has been found from a large number of studies that in the ultra-short-term household
appliance load prediction, data-driven models such as artiﬁcial neural networks can predict
the trend of electric energy consumption of electrical equipment but often ignore the
consumption peak [47], that is, the switch state prediction of electrical equipment is more
accurate, while the peak prediction still has defects, as shown in Figure 7.

---

<!-- PAGE 12 -->

Energies 2023, 16, 5809

12 of 17

Figure 7. Load prediction results of different electrical equipment based on data-driven model.

It is helpful to predict the load consumption in the next hour of the household to
correctly manage household energy [48]. However, ultra-short-term load prediction is not
easy to achieve, mainly for the following reasons: (1) The dynamic behavior of each user
will affect the load usage pattern, which plays a major role in the hourly load prediction.
(2) Transmission and technical errors will also affect load usage patterns, thus reducing
the accuracy of ultra-short-term load prediction. (3) Inevitably, data loss or overﬂow may
occur due to hardware or system errors. Noise can also be added to the collected data. In
this case, the accuracy of the load forecast for the next hour will be reduced.

In future research, the method of hyperparameter adjustment can be developed to
improve the prediction accuracy. Secondary inﬂuences on load consumption, including the
number of people, season, and holiday period, can also be further studied.

---

<!-- PAGE 13 -->

Energies 2023, 16, 5809

13 of 17

5. Load Forecasting Is Used for Electricity Scheduling in the HEMS

Recently, the home energy management system (HEMS) as the main energy saving
countermeasure has gradually become the focus of residential energy optimization research.
In the context of the smart grid, the HEMS, as a hub connecting users with the power grid,
aims to optimize the utilization of electric energy by household users [49,50]. Table 2 shows
part of the data collected by smart meters. The main function of the HEMS is to optimize
household energy use, improve energy efﬁciency and user comfort through optimization
algorithms and scheduling strategies, and achieve energy saving and consumption reduc-
tion by relying on the scheduling of distributed energy and energy storage devices through
detection facilities such as smart meters and sensors [51]. The HEMS structure is shown
in Figure 8. According to the information of users’ electricity demand, environmental
conditions, and price incentives, the built-in residential electricity optimization strategy is
applied to adjust the operation of various electrical appliances, optimize the user load curve,
and participate in peak regulation. Household load forecasting can predict household elec-
tricity demand in advance, help households better plan energy use, and reduce electricity
costs and unnecessary energy waste. Schmidt et al. [4] proposed a probabilistic model for
predicting the electrical consumption of household appliances based on historical data,
taking into account three main factors: (1) the time elapsed after the last use of household
appliances; (2) the time of day during which the appliance may be used; (3) behavioral
patterns of occupants (for example, people are likely to use the washing machine two to
three times more on weekends than weekdays). The authors aim to provide advice to
occupants and improve home automation systems for load shifting or scheduling without
affecting the comfort of occupants.

Table 2. A segment of the data collected by smart meters.

Time

Active Power
(kW)

Reactive Power
(kW)

Average Voltage
(V)

Average Current
Intensity (A)

Total Load
(W·h)

16 December 2016 17:24:00
16 December 2016 17:25:00
16 December 2016 17:26:00
16 December 2016 17:27:00

4.216
5.360
5.374
5.388

0.418
0.436
0.498
0.502

234.840
233.630
233.290
233.740

18.400
23.000
23.000
23.000

18
17
19
18

Figure 8. Schematic diagram of the home energy management system.

---

<!-- PAGE 14 -->

Energies 2023, 16, 5809

14 of 17

The HEMS can dispatch energy consumption in households through real-time electric-
ity prices. It should be noted that although power companies release price information to
customers through smart meters or the network [52], the price data are usually released
several hours in advance for the next time period. Therefore, when scheduling using the
HEMS, the electricity price data for the scheduling period may be partially unknown. In
this case, only with the short-term forecasting function, the HEMS can better adjust the
working state of power equipment according to the energy consumption data and future
electricity price, so as to meet the needs of users and reduce the system operation cost.
Load prediction error will increase the uncertainty of the HEMS and affect the dispatching
performance of the household energy management system [53–58]. Therefore, a mature
household energy management system must be equipped with a set of efﬁcient household
load forecasting models.

According to the different consumption modes and user demand, household electric-
ity load can be divided into dispatchable load and undispatchable load. These include
high-voltage AC transmission systems, washing machines, clothes dryers, water heaters,
dishwashers, electric vehicles, pumps for home swimming pools, etc. Under certain condi-
tions, when the operation of this equipment scheduling will not affect the comfort of users,
they are schedulable loads. The unschedulable loads mainly include computers, refrigera-
tors, lighting systems, security systems, etc. The scheduling of these loads will seriously
affect the satisfaction of users. Therefore, optimizing the scheduling of the schedulable
load is one of the important ways to realize the demand response of residents. However,
predicting the power consumption of a schedulable load such as a washing machine is a
challenging task.

In the future, with the popularity of the smart home and the development of the
HEMS, household appliance load prediction will play a more important role. Future
research directions include improving prediction accuracy, improving real-time perfor-
mance and stability of algorithms, and developing more intelligent and sustainable energy
management systems.

6. Summary and Prospect

At present, the energy consumption of the household as a unit is increasing. In order
to make rational use of energy and optimize user cost, energy management with the HEMS
as the main energy-saving countermeasure has gradually become the focus of residential
energy optimization research. Accurate short-term household load prediction can effec-
tively improve the energy management efﬁciency and reliability of the HEMS, so as to
achieve the goal of efﬁcient utilization of energy and energy saving and emission reduction.
In this paper, we reviewed the latest research results of the deep neural network load
prediction method and probabilistic load prediction method in household load prediction,
and summarized and analyzed the network prediction model, feature extraction method,
adaptive learning ability of the network, equipment-level load prediction method, and
other aspects. The key role of short-term household appliance load forecasting in HEMS
dispatching was also pointed out.

Although many models and methods have achieved certain results in short-term

household load prediction, there are still many problems to be solved in future research:

1.

2.

Data quality: Short-term household load forecasting requires a large amount of histor-
ical load data and other relevant data, such as temperature and humidity. However,
the existing data often have quality problems, such as missing values, noise, etc.,
which will affect the prediction results.
Prediction accuracy of the model: Although the deep learning model has achieved a
certain accuracy in household load prediction, there is still a lot of room for improve-
ment. Researchers need to explore new model structures or optimization algorithms
to improve the prediction accuracy.

---

<!-- PAGE 15 -->

Energies 2023, 16, 5809

15 of 17

Generalization ability of the model: The deep learning model is prone to overﬁtting,
especially when the data set is small. Therefore, how to enhance the generalization ability
of the model is an important research direction.

3.

Real-time performance and uncertainty: Household load forecasting involves many
uncertain factors, such as weather and user behavior. Therefore, how to consider
these uncertainties and integrate them into the deep learning model is also a problem
that needs to be studied.

4. Model interpretability: Deep learning models are generally regarded as black box
models. In practical applications, the interpretability of models can facilitate users
to better understand the prediction results of models and make corresponding deci-
sions. However, in past studies, the explanatory forecasting framework of short-term
household load is rarely involved.

To solve these problems, in the future, the research direction of short-term household

appliance load prediction will include the following aspects:

1.

Explore more data sources: The continuous progress of data mining and preprocess-
ing technology can improve the quality of data and reduce the workload of data
processing. The construction of data sharing and open platform will help promote
the research progress of short-term household load forecasting and promote its ap-
plication in practical production. In addition to electricity consumption data, other
data can be used, such as meteorological data, calendar data, social media data, etc.,
to help forecast household load. Therefore, it is possible to consider how to combine
different data sources to improve the accuracy of the prediction.

2. Model innovation: Model fusion and integrated learning technology can combine the
advantages of various models to improve the prediction accuracy and robustness, such
as the hybrid model of different deep learning neural networks, the model combining
the probabilistic prediction method with deep learning time series model, etc. The
development of intelligent technologies, such as deep learning and natural language
processing (NLP), is expected to bring new breakthroughs for short-term household
load forecasting and improve the forecasting effect. In addition, exploring the use of
multi-task learning methods to realize synchronous prediction of multiple tasks such
as power consumption and power can also improve the prediction performance of
the model.

Author Contributions: Conceptualization, P.M.; Formal analysis, S.C.; Data curation, M.C.; Writing—
original draft preparation, P.M.; Methodology, P.M.; Investigation, S.Z.; Writing—review and editing,
S.C.; Project administration, K.W. All authors have read and agreed to the published version of the
manuscript.

Funding: This research was funded by the Youth Fund of Shandong Province Natural Science
Foundation grant number ZR2020QE212, Key Projects of Shandong Province Natural Science Foun-
dation grant number ZR2020KF020, the Guangdong Provincial Key Lab of Green Chemical Product
Technology grant number GC202111, Zhejiang Province Natural Science Foundation grant number
LY22E070007, and National Natural Science Foundation of China grant number 52007170.

Data Availability Statement: Data are contained within the article.

Conﬂicts of Interest: The authors declare that they have no known competing ﬁnancial interests or
personal relationships that could have appeared to inﬂuence the work reported in this paper.

References

1.

2.

3.

Lusis, P.; Khalilpour, K.R.; Andrew, L.; Liebman, A. Short-term residential load forecasting: Impact of calendar effects and forecast
granularity. Appl. Energy 2017, 205, 654–669. [CrossRef]
Sun, X.; Zhang, Y.; Zhang, Y.C.; Wang, L.; Wang, K. Summary of Health-State Estimation of Lithium-Ion Batteries Based on
Electrochemical Impedance Spectroscopy. Energies 2023, 16, 5682. [CrossRef]
Imani, M.; Ghassemian, H. Residential load forecasting using wavelet and collaborative representation transforms. Appl. Energy
2019, 253, 113505. [CrossRef]

---

<!-- PAGE 16 -->

Energies 2023, 16, 5809

16 of 17

4.

5.

6.

7.
8.

9.

Zheng, Z.; Chen, H.; Luo, X. Spatial granularity analysis on electricity consumption prediction using LSTM recurrent neural
network. Energy Procedia 2018, 158, 2713–2718. [CrossRef]
Kim, T.; Jang, M.; Jeong, H.C.; Joo, S.-K. Short-Term Residential Load Forecasting Using 2-Step SARIMAX. J. Electr. Eng. Technol.
2021, 17, 751–758. [CrossRef]
Ceperic, E.; Ceperic, V.; Baric, A. A Strategy for Short-Term Load Forecasting by Support Vector Regression Machines. IEEE Trans.
Power Syst. 2013, 28, 4356–4364. [CrossRef]
Dudek, G. A Comprehensive Study of Random Forest for Short-Term Load Forecasting. Energies 2022, 15, 7547. [CrossRef]
Candanedo, L.M.; Feldheim, V.; Deramaix, D. Data driven prediction models of energy use of appliances in a low-energy house.
Energy Build. 2017, 140, 81–97. [CrossRef]
Lu, C.N.; Wu, H.T.; Vemuri, S. Neural Network Based Short-Term Load Forecasting. IEEE Trans. Power Syst. 1993, 8, 336–342.
[CrossRef]

10. Hochreiter, S.; Schmidhuber, J. Long short-term memory. Neural Comput. 1997, 9, 1735–1780. [CrossRef]
11. Ma, N.; Yin, H.; Wang, K. Prediction of the Remaining Useful Life of Supercapacitors at Different Temperatures Based on

Improved Long Short-Term Memory. Energies 2023, 14, 5240. [CrossRef]

12. Liu, J.; Li, J.; Yang, L.; Yan, Y.; Liu, Y.; Zhang, Y. Short-term household load forecasting based on EMD-SLSTM. Power Syst. Prot.

Control 2019, 47, 40–47.

13. Moradzadeh, A.; Zakeri, S.; Shoaran, M.; Mohammadi-Ivatloo, B.; Mohammadi, F. Short-Term Load Forecasting of Microgrid via

Hybrid Support Vector Regression and Long Short-Term Memory Algorithms. Sustainability 2020, 12, 7076. [CrossRef]

14. Acharya, S.K.; Wi, Y.M.; Lee, J. Short-Term Load Forecasting for a Single Household Based on Convolution Neural Networks

Using Data Augmentation. Energies 2019, 12, 3560. [CrossRef]

15. Andriopoulos, N.; Magklaras, A.; Birbas, A.; Papalexopoulos, A.; Valouxis, C.; Daskalaki, S.; Birbas, M.; Housos, E.; Papaioannou,
G.P. Short Term Electric Load Forecasting Based on Data Transformation and Statistical Machine Learning. Appl. Sci. 2020, 11,
158. [CrossRef]

16. Cheng, X.; Wang, L.; Zhang, P.; Wang, X.; Yan, Q. Short-term fast forecasting based on family behavior pattern recognition for

17.

small-scale users load. Clust. Comput. 2021, 25, 2107–2123. [CrossRef]
Jiang, L.; Wang, X.; Li, W.; Wang, L.; Yin, X.; Jia, L. Hybrid Multitask Multi-Information Fusion Deep Learning for Household
Short-Term Load Forecasting. IEEE Trans. Smart Grid 2021, 12, 5362–5372. [CrossRef]

18. Guo, X.; Gao, Y.; Li, Y.; Zheng, D.; Shan, D. Short-term household load forecasting based on Long- and Short-term Time-series

19.

network. Energy Rep. 2021, 7, 58–64. [CrossRef]
Syed, D.; Abu-Rub, H.; Ghrayeb, A.; Refaat, S.S. Household-Level Energy Forecasting in Smart Buildings Using a Novel Hybrid
Deep Learning Model. IEEE Access 2021, 9, 33498–33511. [CrossRef]

20. Li, L.; Meinrenken, C.J.; Modi, V.; Culligan, P.J. Short-term apartment-level load forecasting using a modiﬁed neural network

with selected auto-regressive features. Appl. Energy 2021, 287, 116509. [CrossRef]

21. Bouktif, S.; Fiaz, A.; Ouni, A.; Serhani, M.A. Single and Multi-Sequence Deep Learning Models for Short and Medium Term

Electric Load Forecasting. Energies 2019, 12, 149. [CrossRef]

22. Tian, C.J.; Ma, J.; Zhang, C.H.; Zhan, P.P. A Deep Neural Network Model for Short-Term Load Forecast Based on Long Short-Term

Memory Network and Convolutional Neural Network. Energies 2018, 11, 3493. [CrossRef]

23. Kiprijanovska, I.; Stankoski, S.; Ilievski, I.; Jovanovski, S.; Gams, M.; Gjoreski, H. HousEEC: Day-Ahead Household Electrical

Energy Consumption Forecasting Using Deep Learning. Energies 2020, 13, 2672. [CrossRef]

24. Yang, W.; Shi, J.; Li, S.; Song, Z.; Zhang, Z.; Chen, Z. A combined deep learning load forecasting model of single household

resident user considering multi-time scale electricity consumption behavior. Appl. Energy 2022, 307, 118197. [CrossRef]

25. Hou, T.; Fang, R.; Tang, J.; Ge, G.; Yang, D.; Liu, J.; Zhang, W. A Novel Short-Term Residential Electric Load Forecasting Method

Based on Adaptive Load Aggregation and Deep Learning Algorithms. Energies 2021, 14, 7820. [CrossRef]

26. He, Y.; Luo, F.; Ranzi, G. Transferrable Model-Agnostic Meta-learning for Short-Term Household Load Forecasting with Limited

Training Data. IEEE Trans. Power Syst. 2022, 37, 3177–3180. [CrossRef]

27. Gomez-Rosero, S.; Capretz, M.A.M.; Mir, S. Transfer Learning by Similarity Centred Architecture Evolution for Multiple

28.

29.

Residential Load Forecasting. Smart Cities 2021, 4, 217–240. [CrossRef]
Fujimoto, Y.; Fujita, M.; Hayashi, Y. Deep reservoir architecture for short-term residential load forecasting: An online learning
scheme for edge computing. Appl. Energy 2021, 298, 117176.
Fekri, M.N.; Patel, H.; Grolinger, K.; Sharma, V. Deep learning for load forecasting with smart meter data: Online Adaptive
Recurrent Neural Network. Appl. Energy 2021, 282, 116177.

30. Hong, T.; Fan, S. Probabilistic electric load forecasting: A tutorial review. Int. J. Forecast. 2016, 32, 914–938. [CrossRef]
31. Liu, B.D.; Nowotarski, J.; Hong, T.; Weron, R. Probabilistic Load Forecasting via Quantile Regression Averaging on Sister Forecasts.

IEEE Trans. Smart Grid 2017, 8, 730–737. [CrossRef]

32. Wang, Y.; Zhang, N.; Tan, Y.; Hong, T.; Kirschen, D.; Kang, C. Combining Probabilistic Load Forecasts. IEEE Trans. Smart Grid

33.

2018, 10, 3664–3674. [CrossRef]
Feng, C.; Sun, M.C.; Zhang, J. Reinforced Deterministic and Probabilistic Load Forecasting via Q-Learning Dynamic Model
Selection. IEEE Trans. Smart Grid 2020, 11, 1377–1386. [CrossRef]

---

<!-- PAGE 17 -->

Energies 2023, 16, 5809

17 of 17

34. Xia, Z.; Ma, H.; Saha, T.K.; Zhang, R. Consumption Scenario-Based Probabilistic Load Forecasting of Single Household. IEEE

Trans. Smart Grid 2022, 13, 1075–1087. [CrossRef]

35. Brusaferri, A.; Matteucci, M.; Spinelli, S.; Vitali, A. Probabilistic electric load forecasting through Bayesian Mixture Density

Networks. Appl. Energy 2022, 309, 118341. [CrossRef]

36. Avancini, D.B.; Rodrigues, J.; Martins, S.G.B.; Rabelo, R.A.L.; Al-Muhtadi, J.; Solic, P. Energy meters evolution in smart grids: A

review. J. Clean. Prod. 2019, 217, 702–715. [CrossRef]

37. Tabatabaei, S.M.; Dick, S.; Xu, W.S. Toward Non-Intrusive Load Monitoring via Multi-Label Classiﬁcation. IEEE Trans. Smart Grid

2017, 8, 26–40. [CrossRef]

38. Gao, B.; Liu, X.; Zhu, Z. A Bottom-Up Model for Household Load Proﬁle Based on the Consumption Behavior of Residents.

Energies 2018, 11, 2112. [CrossRef]

39. Zheng, Z.; Chen, H.; Luo, X. A Kalman ﬁlter-based bottom-up approach for household short-term load forecast. Appl. Energy

2019, 250, 882–894. [CrossRef]

40. Wang, S.; Deng, X.; Chen, H.; Shi, Q.; Xu, D. A bottom-up short-term residential load forecasting approach based on appliance

characteristic analysis and multi-task learning. Electr. Power Syst. Res. 2021, 196, 107233. [CrossRef]

41. Razghandi, M.; Turgut, D. Residential Appliance-Level Load Forecasting with Deep Learning. In Proceedings of the GLOBECOM

42.

43.

2020—2020 IEEE Global Communications Conference, Taipei, Taiwan, 7–11 December 2020; pp. 1–6.
Sirojan, T.; Phung, B.T.; Ambikairajah, E. In Deep Neural Network Based Energy Disaggregation. In Proceedings of the 6th IEEE
International Conference on Smart Energy Grid Engineering (IEEE SEGE), Oshawa, ON, Canada, 12–15 August 2018; pp. 73–77.
Ji, Y.T.; Buechler, E.; Rajagopal, R. Data-Driven Load Modeling and Forecasting of Residential Appliances. IEEE Trans. Smart Grid
2020, 11, 2652–2661. [CrossRef]

44. Cheng, L.M.; Bao, Y.Q.; Tang, L.; Di, H.F. Very-short-term load forecasting based on empirical mode decomposition and deep

neural network. IEEE Trans. Electr. Electron. Eng. 2020, 15, 252–258. [CrossRef]

45. Bessani, M.; Massignan, J.A.D.; Santos, T.M.O.; London, J.B.A.; Maciel, C.D. Multiple households very short-term load forecasting

using bayesian networks. Electr. Power Syst. Res. 2020, 189, 106733. [CrossRef]

46. Ageng, D.; Huang, C.Y.; Cheng, R.G. A Short-Term Household Load Forecasting Framework Using LSTM and Data Preparation.

IEEE Access 2021, 9, 167911–167919. [CrossRef]

47. Tarmanini, C.; Sarma, N.; Gezegin, C.; Ozgonenel, O. Short term load forecasting based on ARIMA and ANN approaches. Energy

Rep. 2023, 9, 550–557. [CrossRef]

48. Hsiao, Y.H. Household Electricity Demand Forecast Based on Context Information and User Daily Schedule Analysis from Meter

Data. IEEE Trans. Ind. Inform. 2015, 11, 33–43. [CrossRef]

49. Zhou, B.; Li, W.T.; Chan, K.W.; Cao, Y.J.; Kuang, Y.H.; Liu, X.; Wang, X. Smart home energy management systems: Concept,

conﬁgurations, and scheduling strategies. Renew. Sustain. Energy Rev. 2016, 61, 30–40. [CrossRef]

50. Wang, F.; Xiang, B.; Li, K.P.; Ge, X.X.; Lu, H.; Lai, J.G.; Dehghanian, P. Smart Households’ Aggregated Capacity Forecasting for

Load Aggregators Under Incentive-Based Demand Response Programs. IEEE Trans. Ind. Appl. 2020, 56, 1086–1097. [CrossRef]

51. Al-Sumaiti, A.S.; Ahmed, M.H.; Salama, M.M.A. Smart Home Activities: A Literature Review. Electr. Power Compon. Syst. 2014,

42, 294–305. [CrossRef]

52. Zhao, X.; Gao, W.; Qian, F.; Ge, J. Electricity cost comparison of dynamic pricing model based on load forecasting in home energy

management system. Energy 2021, 229, 120538. [CrossRef]

53. Tiwari, P.; Mahanta, P.; Trivedi, G. A Dual-Stage Attention based RNN-Model for Short Term Load Forecasting of Individual
Household. In Proceedings of the 2021 International Conference on Electrical, Computer and Energy Technologies (ICECET),
Cape Town, South Africa, 9–10 December 2021; pp. 1–6.

54. Atef, S.; Ismail, N.; Eltawil, A.B. A new fuzzy logic based approach for optimal household appliance scheduling based on

electricity price and load consumption prediction. Adv. Build. Energy Res. 2022, 16, 262–280. [CrossRef]

55. Yi, Z.; Chen, Z.; Yin, K.; Wang, L.; Wang, K. Sensing as the key to the safety and sustainability of new energy storage devices. Prot.

Control. Mod. Power Syst. 2003, 8, 27. [CrossRef]

56. Wang, L.; Xie, L.; Yang, Y.; Zhang, Y.; Wang, K.; Cheng, S.-J. Distributed Online Voltage Control with Fast PV Power Fluctuations

and Imperfect Communication. IEEE Trans. Smart Grid 2023. [CrossRef]

57. Cui, Z.; Dai, J.; Sun, J.; Li, D.; Wang, L.; Wang, K. Hybrid methods using neural network and Kalman ﬁlter for the state of charge

estimation of lithium-ion battery. Math. Probl. Eng. 2022, 2022, 9616124. [CrossRef]

58. Zhang, M.; Yang, D.; Du, J.; Sun, H.; Li, L.; Wang, L.; Wang, K. A Review of SOH Prediction of Li-Ion Batteries Based on

Data-Driven Algorithms. Energies 2023, 16, 3167. [CrossRef]

Disclaimer/Publisher’s Note: The statements, opinions and data contained in all publications are solely those of the individual
author(s) and contributor(s) and not of MDPI and/or the editor(s). MDPI and/or the editor(s) disclaim responsibility for any injury to
people or property resulting from any ideas, methods, instructions or products referred to in the content.

<!-- MARKITDOWN CONVERSION -->

<!-- Full MarkItDown conversion for formatting fidelity. -->

Review
Review of Family-Level Short-Term Load Forecasting and Its
Application in Household Energy Management System

Ping Ma 1,†, Shuhui Cui 1,†, Mingshuai Chen 2, Shengzhe Zhou 3 and Kai Wang 1,*

1

School of Electrical Engineering, Weihai Innovation Research Institute, Qingdao University,
Qingdao 266000, China; qdumaping@163.com (P.M.); cuishuhui321@163.com (S.C.)

2 Rizhao Power Supply Company, State Grid Shandong Electric Power Company, Rizhao 276826, China;

chenmingshuaizsz@163.com

3 Department of Information Engineering, Shandong Water Conservancy Vocational College,

Rizhao 276826, China; zhoushengzheyx@126.com

* Correspondence: wangkai@qdu.edu.cn or wkwj888@163.com; Tel.: +86-15863060145; Fax: +86-532-85951980
†

These authors contributed equally to this work.

Abstract: With the rapid development of smart grids and distributed energy sources, the home
energy management system (HEMS) is becoming a hot topic of research as a hub for connecting
customers and utilities for energy visualization. Accurate forecasting of future short-term residential
electricity demand for each major appliance is a key part of the energy management system. This
paper aims to explore the current research status of household-level short-term load forecasting,
summarize the advantages and disadvantages of various forecasting methods, and provide research
ideas for short-term household load forecasting and household energy management. Firstly, the paper
analyzes the latest research results and research trends in deep learning load forecasting methods
in terms of network models, feature extraction, and adaptive learning; secondly, it points out the
importance of combining probabilistic forecasting methods that take into account load uncertainty
with deep learning techniques; and further explores the implications and methods for device-level
as well as ultra-short-term load forecasting. In addition, the paper also analyzes the importance of
short-term household load forecasting for the scheduling of electricity consumption in household
energy management systems. Finally, the paper points out the problems in the current research and
proposes suggestions for future development of short-term household load forecasting.

Keywords: home energy management systems; household-level load forecasting; short-term load;
deep learning neural networks; probabilistic forecasting

1. Introduction

With the development of the economy and living standards, household-based electri-
cal energy consumption accounts for an increasing proportion of total energy consumption,
and how to use electrical energy more efﬁciently is the key to reducing residential energy
consumption. In addition, with the development of energy saving and emission reduction
policies and distributed energy sources, energy management with the home energy man-
agement system (HEMS) as the main energy saving countermeasure has gradually become
the focus of residential energy optimization research [1]. Accurate forecasting of future
residential electricity demand in the short term is an intelligent decision-making tool for
energy management systems. It is therefore important to study methods for predicting
household-level and even device-level loads with high forecasting accuracy.

Load forecasting methods can generally be classiﬁed according to the forecasting
time scale: long-term load forecasting (LTLF), medium-term load forecasting (MTLF),
short-term load forecasting (STLF), and very short-term load forecasting (VSTLF). Among
them, short-term load forecasting can provide effective energy system planning, which is
important for energy management [2,3]. Traditional short-term load forecasting has focused

Citation: Ma, P.; Cui, S.; Chen, M.;

Zhou, S.; Wang, K. Review of

Family-Level Short-Term Load

Forecasting and Its Application in

Household Energy Management

System. Energies 2023, 16, 5809.

https://doi.org/10.3390/en16155809

Academic Editor: Paulo Santos

Received: 20 June 2023

Revised: 23 July 2023

Accepted: 2 August 2023

Published: 4 August 2023

Copyright: © 2023 by the authors.

Licensee MDPI, Basel, Switzerland.

This article is an open access article

distributed under

the terms and

conditions of the Creative Commons

Attribution (CC BY) license (https://

creativecommons.org/licenses/by/

4.0/).

Energies 2023, 16, 5809. https://doi.org/10.3390/en16155809

https://www.mdpi.com/journal/energies

energiesEnergies 2023, 16, 5809

2 of 17

on the system level, substation level, busbar level, feeder level, and building level. Unlike
system-level electrical loads, individual household loads lack a clear consistent pattern
conducive to forecast accuracy. In general, the diversity of aggregation levels smooths
out the daily load distribution, which makes substation loads relatively more predictable,
while individual household electricity consumption is more dependent on underlying
human behavior. Within individual households, the daily habits and lifestyles of residents
may have a more direct impact on the short-term load distribution. The randomness and
uncertainty caused by human behavior or weather changes make it difﬁcult to accurately
implement more established system-level load forecasting methods at the household level.
With the widespread installation of smart meters, household electricity consumption
data are available and household-level load forecasting is possible. Accurate short-term
load forecasting (STLF) can properly complement the HEMS and support utilities to imple-
ment more rational demand response strategies to reduce operational costs [4]. In recent
years, in order to further improve the accuracy of short-term household load forecasting,
there have been many related studies at home and abroad, proposing various forecasting
methods including probabilistic load forecasting and various deep learning algorithms.
The aim of this paper is to review the research papers in this ﬁeld, compare the accuracy
and advantages and disadvantages of various forecasting methods, and give effective
suggestions for the research of household-level load forecasting methods.

The rest of the paper is organized as follows:

1.

2.

3.

4.

Section 2 introduces the application of deep learning algorithms such as RNN, LSTM,
and CNN in household load forecasting, and analyzes the improvement of the algo-
rithms in terms of fusion of models, feature analysis and extraction, and adaptive
learning of networks.
Section 3 explores the advantages of probabilistic forecasting methods and proposes
a research direction to improve traditional probabilistic forecasting methods with
advanced deep learning algorithms.
Section 4 analyzes the development trends and challenges of ultra-short-term device-
level load forecasting.
Section 5 presents the principles of the HEMS and the key role played by home-level
load forecasting in the HEMS.

2. Deep Learning-Based Load Prediction Methods

There are many research methods on load forecasting, from classical time series
analysis to more recent machine learning methods, including the Autoregressive Integrated
Moving Average Model (ARIMA) [5], Support Vector Regression (SVR) [6], Random Forest
(RF) [7], and Gradient Boosting Regression (GBR) [8]. Another important branch of load
forecasting is the use of artiﬁcial neural network (ANN) models [9] for forecasting. In recent
years, with the increase in relevant load data and massively parallel computing capabilities,
load prediction using big data has become a hot research topic. Against the backdrop of
massive data and signiﬁcant growth in parallel computing performance, deep learning
(DL) is approaching or even surpassing humans in areas such as speech recognition and
image classiﬁcation and is gradually becoming the model of choice for many researchers to
improve load prediction methods.

2.1. Neural Network Prediction Models

In recent years, deep learning has become one of the most active techniques in many
areas of research. In contrast to shallow learning, deep learning typically refers to stacking
multiple layers of neural networks and relying on stochastic optimization to perform ma-
chine learning tasks. Different numbers of layers can provide different levels of abstraction
to improve learning ability and task performance. In particular, long short-term memory
(LSTM) recurrent neural networks (RNNs), proposed by Hochreiter and Schmidhuber [10],
have received a great deal of attention in the ﬁeld of sequence learning.

Energies 2023, 16, 5809

3 of 17

2.1.1. LSTM Model

Often, deep learning models encounter the problem of gradient explosion (i.e., learning
scattering) or gradient disappearance (i.e., learning stopping). This problem is solved by
LSTM networks that introduce memory cells and computational gates. LSTM is a type of
RNN that has been used in the past for time series analysis and load prediction problems.
A load proﬁle can be thought of as a time series in which there is a high degree
of correlation and dependence between successive samples. Long short-term memory
(LSTM) has the structure of a recurrent neural network with the characteristics of sequence
learning [2]. The LSTM structure has a memory unit that allows it to remember the
signiﬁcant states of the previous steps. In addition, LSTM has an oblivion gate to remove
unimportant features and reset the memory unit, as shown in Figure 1. LSTM can also
track customer consumption behavior by learning long-term dependencies and correlations
between successive samples of sequential data.

Figure 1. The structure of an LSTM: (a) The structure of an LSTM block. (b) The unrolled LSTM
sequential architecture.

It is generally assumed that the lifestyles of the inhabitants, however inconsistent, will
be reﬂected in repeated patterns of energy consumption. Kong et al. [11] proposed a load
prediction framework based on an LSTM cyclic neural network (Figure 2). The results show
that the prediction accuracy of LSTM is better than several other advanced machine learning
algorithms. In the later work, people try to improve the LSTM algorithm in order to obtain
higher prediction accuracy. In view of the uncertainty and non-linear characteristics of
household load data, the EMD method can transform non-stationary non-linear data into
stationary linear data. Liu et al. [12] proposed a combination algorithm of empirical mode
decomposition (EMD) and stack long short-term memory (SLSTM) that has been applied to

Energies 2023, 16, x FOR PEER REVIEW 3 of 17   2.1. Neural Network Prediction Models In recent years, deep learning has become one of the most active techniques in many areas of research. In contrast to shallow learning, deep learning typically refers to stacking multiple layers of neural networks and relying on stochastic optimization to perform ma-chine learning tasks. Diﬀerent numbers of layers can provide diﬀerent levels of abstrac-tion to improve learning ability and task performance. In particular, long short-term memory (LSTM) recurrent neural networks (RNNs), proposed by Hochreiter and Schmid-huber [10], have received a great deal of attention in the ﬁeld of sequence learning. 2.1.1. LSTM Model Often, deep learning models encounter the problem of gradient explosion (i.e., learn-ing scattering) or gradient disappearance (i.e., learning stopping). This problem is solved by LSTM networks that introduce memory cells and computational gates. LSTM is a type of RNN that has been used in the past for time series analysis and load prediction prob-lems. A load proﬁle can be thought of as a time series in which there is a high degree of correlation and dependence between successive samples. Long short-term memory (LSTM) has the structure of a recurrent neural network with the characteristics of se-quence learning [2]. The LSTM structure has a memory unit that allows it to remember the signiﬁcant states of the previous steps. In addition, LSTM has an oblivion gate to re-move unimportant features and reset the memory unit, as shown in Figure 1. LSTM can also track customer consumption behavior by learning long-term dependencies and cor-relations between successive samples of sequential data.  (a)  (b) Figure 1. The structure of an LSTM: (a) The structure of an LSTM block. (b) The unrolled LSTM sequential architecture. Energies 2023, 16, 5809

4 of 17

household short-term load prediction. This SLSTM can train better parameters and improve
the accuracy of prediction. SVR has the characteristic of linearly reﬂecting input–output
relationships. Combined with this characteristic, Moradzadeh et al. [13] proposed an
improved hybrid method of support vector regression—long-term and short-term memory
(SCR–LSTM) for short-term load prediction of a microgrid. The SVR–LSTM model with
the highest correlation coefﬁcient (R = 0.9901) and the lowest error value can provide
better results than the traditional SVR and LSTM. However, the data set used to verify
the method is not load data for single households and does not account for weather and
human uncertainties. Nevertheless, hybrid approaches such as these are widely proposed.

Figure 2. The LSTM-based forecasting framework.

Energies 2023, 16, x FOR PEER REVIEW 4 of 17   It is generally assumed that the lifestyles of the inhabitants, however inconsistent, will be reﬂected in repeated patterns of energy consumption. Kong et al. [11] proposed a load prediction framework based on an LSTM cyclic neural network (Figure 2). The re-sults show that the prediction accuracy of LSTM is better than several other advanced machine learning algorithms. In the later work, people try to improve the LSTM algorithm in order to obtain higher prediction accuracy. In view of the uncertainty and non-linear characteristics of household load data, the EMD method can transform non-stationary non-linear data into stationary linear data. Liu et al. [12] proposed a combination algo-rithm of empirical mode decomposition (EMD) and stack long short-term memory (SLSTM) that has been applied to household short-term load prediction. This SLSTM can train better parameters and improve the accuracy of prediction. SVR has the characteristic of linearly reﬂecting input–output relationships. Combined with this characteristic, Mo-radzadeh et al. [13] proposed an improved hybrid method of support vector regression—long-term and short-term memory (SCR–LSTM) for short-term load prediction of a mi-crogrid. The SVR–LSTM model with the highest correlation coeﬃcient (R = 0.9901) and the lowest error value can provide better results than the traditional SVR and LSTM. How-ever, the data set used to verify the method is not load data for single households and does not account for weather and human uncertainties. Nevertheless, hybrid approaches such as these are widely proposed.  Figure 2. The LSTM-based forecasting framework. Energies 2023, 16, 5809

5 of 17

2.1.2. CNN Model

CNN is a type of deep neural network which is most commonly used to analyze visual
images. CNN uses the method of local connection and weight sharing to process the original
data at a higher level and more abstract, which can effectively and automatically extract
the internal features in the data. The internal neural network layer is mainly composed of a
convolutional layer, pooling layer, and full connection layer, which reduces the number of
weights and network complexity. CNN automatically extracts feature vectors from data,
effectively reducing the complexity of feature extraction and data reconstruction, improving
the quality of data features, and obtaining effective information through a convolution
layer and pooling, greatly reducing the training time of the model.

Since LSTM utilizes the time locality of load time series by analogy with the spatial
locality in image processing, CNN seems to be able to obtain better accuracy when we
lack historical data, the size of the energy entity is small, and the prediction range is short
(forecast one day in advance). Based on the combination of convolutional neural networks
(CNNs) and data enhancement technology, Acharya et al. [14] converted the time series of
single household load data into multiple time series of residual load, which could artiﬁcially
enlarge the training data. This method can solve the problem caused by the lack of historical
data and improve the accuracy of residential load forecasting. In order to give full play to
the advantages of CNN, Andriopoulos et al. [15] proposed a method based on statistical
analysis to preprocess the time series data before solving the problem of short-term load
prediction. The main feature of this method is to optimize the superparameters of a neural
network by using the statistical attributes of each time series data set and transform the
given data set into a form that allows maximum advantage of the CNN algorithm. In
addition, the literature [16] designed a CNNGRU short-term load prediction model based
on the attention mechanism, and effectively classiﬁed the household load data according to
the household behavior. The accuracy of this method reaches 92.06% in small-range load
prediction. Compared with the general deep learning time series prediction model, the
prediction time of this method is reduced by 75%.

2.1.3. Hybrid Model

A comparison of several prediction models is shown in Table 1. Although CNNs
have their unique advantages in load prediction, the efﬁciency of LSTMs for long-term
dependencies is unquestionable. Therefore, the hybrid LSTM–CNN model becomes a
reliable deep learning load prediction method worthy of further study, especially when
multi-step methods are considered.

Table 1. Comparison of several forecasting models.

Model

Advantage

Shortcomings

Application Situation

Classical time series
model

LSTM

CNN

Simple to understand,
modeling time is short
Able to learn long-term
dependencies
Features can be learned
automatically

Poor performance on complex
time series prediction problems

Risk of overﬁtting the model

Not good for non-linear time
series data

Simple time series data prediction

Process non-linear and
non-stationary time series data
Lack of historical data, short
forecast time

Jiang et al. [17] proposed a multi-task, multi-information fusion deep learning frame-
work (MFDL) that combines long and short-term memory (LSTM) and a convolutional
neural network (CNN) to learn both near-term and long-term regular behavior, learning
near-term electricity consumption behavior by LSTM and long-term regular electricity
consumption behavior features by CNN. Experimental results show that this method
can signiﬁcantly improve the accuracy of single household short-term load prediction.
Guo et al. [18] also used convolutional neural network (CNN) and long and short-term
memory (LSTM) to capture temporal short-term local information and long-term corre-

Energies 2023, 16, 5809

6 of 17

lation information, respectively, and used an autoregressive (AR) model as the linear
component; experimental results show that this LST Net network model can better adapt
to time series and complex non-linear load data relationships. It has higher prediction
and generalization performance compared with ARIMA and CNN–LSTM models. And
based on an improved LSTM, Syed et al. [19] proposed a hybrid model (HSBUFC) based on
bidirectional and unidirectional LSTM superposition coupled with fully connected dense
layers, which ampliﬁes the advantages of unidirectional LSTMs, bidirectional LSTMs, and
RNN superposition for energy consumption prediction accuracy. The model outperforms
other hybrid models such as the widely used convolutional (Conv) neural network–LSTM
and ConvLSTM in terms of accuracy.

In summary, there have been many studies proving the usefulness of neural network
prediction models in household load forecasting, and hybrid models based on the fusion of
multiple neural networks are being developed more frequently. Future research should
explore better deep learning models, such as deeper, wider, and more complex neural
networks, or use new models such as self-attentive mechanisms to improve prediction
accuracy and stability. Due to the volatility of loads, single forecasting models sometimes
fail to achieve high accuracy. Combining forecasts using multiple deep learning methods
can effectively improve model generalization. Meanwhile, in household load forecasting,
multiple tasks such as power forecasting, electricity consumption forecasting, and power
forecasting may be involved. Therefore, researchers can explore how to use multi-task
learning methods to solve multi-task prediction to improve the prediction performance of
the model while ensuring the prediction accuracy of the model.

2.2. Feature Extraction

When applying deep learning algorithms for load prediction, the input training set
X-train can be fed directly into the LSTM network as if no feature extraction was performed,
or it can be ﬁrst transformed into a new feature space and then the transformed X-train
matrix is applied to the LSTM network [20]. It is worth noting that the original load curve
consists of many points, which may contain a large amount of redundant information. All
lagged load values cannot be used for load prediction at subsequent points. In addition,
the time series may contain useful information about the relationship between loading
points that is not apparent in the original feature space [21,22]. Therefore, the application
of appropriate feature extraction to the variable vector of the load curve can show the
dependence, correlation, and inherent characteristics of the load curve, which is very
important to improve the accuracy of load prediction.

Figure 3 shows the electricity consumption of a washing machine in a family for a week.
It is not difﬁcult to see that not only different electrical appliances have different load curves,
but also the load curves of a single electrical appliance differ on different days of a week.
How to extract the highly correlated features from the load curve is very important. As
shown in Figure 4, the literature [3] uses the advantages of wavelet decomposition (DWT)
and cooperative representation (CRT) to extract the features of hysteresis load variables.
DWT can effectively separate useless details from the approximate components of variable
vectors, while CRT can extract local information of load value dependence in adjacent time
instances and adopt a regularization method to control major load ﬂuctuations adaptively
to avoid unwanted changes in signals. Kiprijanovska et al. [23] extracted features from
the context data (weather, calendar) and the historical load of all families in the data
set to integrate multiple information sources, and calculated novel domain-speciﬁc time
series features so that the system could better simulate the energy consumption pattern of
families. The proposed method does not depend on the current number of households in
the system and has great commercial potential for predicting electrical energy consumption
at the individual household level. In the literature [24], mutual information (MI) and
principal component analysis (PCA) were used to select features and reduce dimensions of
multi-dimensional weather inﬂuencing factors to avoid interference from unrelated factors.
Finally, three-dimensional weather variables (cumulative contribution rate of 93.93%) were

Energies 2023, 16, 5809

7 of 17

obtained from the 12-D weather inﬂuence factors, which greatly improved the prediction
speed of the Co-LSTM network.

Figure 3. Consumption load of clothes washer on different days of a week.

Figure 4. Proposed load forecasting framework containing preprocessing, feature extraction, and
forecasting.

Energies 2023, 16, x FOR PEER REVIEW 7 of 17   and reduce dimensions of multi-dimensional weather inﬂuencing factors to avoid inter-ference from unrelated factors. Finally, three-dimensional weather variables (cumulative contribution rate of 93.93%) were obtained from the 12-D weather inﬂuence factors, which greatly improved the prediction speed of the Co-LSTM network.  Figure 3. Consumption load of clothes washer on diﬀerent days of a week.  Figure 4. Proposed load forecasting framework containing preprocessing, feature extraction, and forecasting. Energies 2023, 16, x FOR PEER REVIEW 7 of 17   and reduce dimensions of multi-dimensional weather inﬂuencing factors to avoid inter-ference from unrelated factors. Finally, three-dimensional weather variables (cumulative contribution rate of 93.93%) were obtained from the 12-D weather inﬂuence factors, which greatly improved the prediction speed of the Co-LSTM network.  Figure 3. Consumption load of clothes washer on diﬀerent days of a week.  Figure 4. Proposed load forecasting framework containing preprocessing, feature extraction, and forecasting. Energies 2023, 16, 5809

8 of 17

2.3. Adaptive Learning of Networks

The traditional static load forecasting technology obtains the single value load forecast
by using the off-line training forecasting model of the consumption pattern of the historical
load. However, this technology cannot capture the dynamic changes of the real load
consumption pattern during the forecast period. If the real load consumption pattern
changes during the forecast period, the prediction accuracy will be greatly reduced. In
order to improve the shortcomings of the traditional forecasting technology, the online
adaptive learning ability of the network is developed, which can effectively capture the
dynamic change of load consumption, so as to improve the forecasting accuracy [25,26].
At the same time, the large-scale deployment of smart meters provides an opportunity for
ﬁne-grained load forecasting using real-time residential data.

Load forecasting for residential users is challenging because users with similar charac-
teristics may have different consumption patterns. With the improvement of computing
power, artiﬁcial neural network technology for time series prediction has become more
and more widely developed. In most cases, training DNNS focuses on developing a model
to predict the load consumption of a single house. To predict multiple loads on multiple
houses, the standard procedure is to create a new model for each house, which results
in high consumption of training time and computing power. Gomez-Rosero et al. [27]
proposed a method to develop DNNs for multiple time series prediction by evolving
only one architecture and adjusting the weights of each time series, a process similar to
migration learning. Fujimoto et al. [28] introduced a deep ESN architecture with high
afﬁnity to edge computing, proposed an effective online learning scheme to keep prediction
models up-to-date, and used real annual data from over 500 households to evaluate its
effectiveness. The proposed framework will make a signiﬁcant contribution in enabling pre-
dictive models otherwise suited to edge computing to exploit the beneﬁts of deep learning
architectures. Fekri et al. [29] proposed an online adaptive RNN load prediction method
capable of continuously learning from newly arrived data and adapting to new patterns.
The RNN is used to capture temporal dependencies, while the online aspect is continuous
by adding preprocessing, buffering, and tuning modules for learning. The preprocessing
module prepares the data for online learning, the tuning module adapts the neural network
hyperparameters to the newly arrived patterns, and the buffering module helps to learn
from particularly difﬁcult patterns and assists with conceptual drift.

Household load forecasting is a dynamic problem and has become a topical issue
to enable forecasting models to automatically update parameters according to changes
In future
in data in order to provide better accuracy and real-time load forecasting.
work, experimenting with different adaptive algorithms (e.g., online learning, recursive
learning, and incremental learning) to improve prediction models and validating their
adaptive performance and prediction accuracy in real data can help us ﬁnd the most
suitable algorithm for the task of household load forecasting.

3. Probabilistic Load Forecasting Methods

Traditional single-value forecasts are unable to assess the uncertainty in load demand
forecasts, and an accurate assessment of uncertainty is essential for applications such
as optimal stochastic decision-making. Probabilistic load forecasting (PLF) methods can
model the uncertainty in future electricity consumption [30,31]. Its load forecasting for
individual households can be fed into robust optimization algorithms for home energy
management, and probabilistic forecasting captures the probability of occurrence of each
predicted value within the forecast interval, providing more comprehensive probabilistic
information about future loads (Figure 5). Wang et al. [32] combined quantile regression
neural networks (QRNN), quantile regression random forests (QRRF), and quantile re-
gression gradient augmentation (QRGA) methods to select the weight-optimal process.
Feng et al. [33] introduced STLF–QMS, a q-learning dynamic model selection (QMS) with a
mixture of deterministic and probabilistic load prediction models. By simulating consump-
tion scenarios, Xia et al. [34] proposed a probabilistic load forecasting method based on

Energies 2023, 16, 5809

9 of 17

consumption scenarios, where the extracted scenarios can effectively characterize house-
hold electricity consumption habits and are used to calculate the probability of occurrence
of each consumption scenario for a single household in any future time horizon. In contrast,
combined with deep learning, Brusaferri et al. [35] proposed a new approach to probabilis-
tic load prediction based on Bayesian deep learning techniques to achieve a comprehensive
uncertainty characterization by capturing general patterns of stochastic uncertainty and
cognitive uncertainty counterparts. A ﬁrst step towards a comprehensive exploration of
Bayesian hybrid density networks for probabilistic load prediction was initiated.

Figure 5. (a) Framework of probabilistic load forecasting. (b) Framework of conditional probabilistic
load forecasting.

In conclusion, probabilistic load forecasting methods have the advantages of relia-
bility, ﬂexibility, scalability, and real-time in household load forecasting, but traditional
probabilistic load forecasting methods based on statistical modeling are not well adapted
to a wide range of complex load forecasting problems. The authors argue that combining
probabilistic forecasting methods with deep learning time series models (e.g., probabilistic
forecasting methods based on empirical modal decomposition), which consider both fore-
casting accuracy and deeply reﬂect electricity consumption habits, has very broad research
prospects.

4. Exploration of Ultra-Short-Term and Facility-Level Load Forecasting

Much of the work in household load forecasting has previously focused on forecasting
the load of the entire household. While total load forecasting is important, the distribution
of household loads is often affected when customers take individual actions to save energy
or shift loads, for example, by delaying the operation of dishwashers to nighttime and
thus avoiding peak electricity consumption. Therefore, the development of short-term load
forecasting models at the residential appliance level is also important.

4.1. Bottom-Up Approach to Household Load Forecasting

In recent years, advanced metering infrastructure (AMI) [36] has been widely de-
ployed, while the development of artiﬁcial intelligence has greatly improved the accuracy
of non-intrusive load monitoring (NILM) [37]. With the collaboration of AMI and NILM, a
wealth of accurate device-level energy consumption information is available, and a bottom-
up load forecasting framework based on this underlying data from domestic appliances is

Energies 2023, 16, x FOR PEER REVIEW 9 of 17   a mixture of deterministic and probabilistic load prediction models. By simulating con-sumption scenarios, Xia et al. [34] proposed a probabilistic load forecasting method based on consumption scenarios, where the extracted scenarios can eﬀectively characterize household electricity consumption habits and are used to calculate the probability of oc-currence of each consumption scenario for a single household in any future time horizon. In contrast, combined with deep learning, Brusaferri et al. [35] proposed a new approach to probabilistic load prediction based on Bayesian deep learning techniques to achieve a comprehensive uncertainty characterization by capturing general patterns of stochastic uncertainty and cognitive uncertainty counterparts. A ﬁrst step towards a comprehensive exploration of Bayesian hybrid density networks for probabilistic load prediction was in-itiated.  (a) (b) Figure 5. (a) Framework of probabilistic load forecasting. (b) Framework of conditional probabilistic load forecasting. In conclusion, probabilistic load forecasting methods have the advantages of reliabil-ity, ﬂexibility, scalability, and real-time in household load forecasting, but traditional probabilistic load forecasting methods based on statistical modeling are not well adapted to a wide range of complex load forecasting problems. The authors argue that combining probabilistic forecasting methods with deep learning time series models (e.g., probabilis-tic forecasting methods based on empirical modal decomposition), which consider both forecasting accuracy and deeply reﬂect electricity consumption habits, has very broad re-search prospects. 4. Exploration of Ultra-Short-Term and Facility-Level Load Forecasting Much of the work in household load forecasting has previously focused on forecast-ing the load of the entire household. While total load forecasting is important, the distri-bution of household loads is often aﬀected when customers take individual actions to save energy or shift loads, for example, by delaying the operation of dishwashers to nighttime and thus avoiding peak electricity consumption. Therefore, the development of short-term load forecasting models at the residential appliance level is also important. 4.1. Bottom-Up Approach to Household Load Forecasting In recent years, advanced metering infrastructure (AMI) [36] has been widely de-ployed, while the development of artiﬁcial intelligence has greatly improved the accuracy of non-intrusive load monitoring (NILM) [37]. With the collaboration of AMI and NILM, a wealth of accurate device-level energy consumption information is available, and a bot-tom-up load forecasting framework based on this underlying data from domestic appli-Energies 2023, 16, 5809

10 of 17

a new way of thinking about forecasting. The bottom-up approach can signiﬁcantly reduce
forecasting errors, but also requires room and appliance-level electricity consumption data.
For individual households, energy consumption is often determined by the habits
of the residents, but their behavior is accompanied by a degree of randomness due to
a variety of factors. In general, however, similar factors will have a similar effect on
the consumption of household appliances. Therefore, it is feasible to model household
consumption behavior using statistical characteristics of appliance consumption in similar
historical periods. Gao et al. [38] proposed a bottom-up forecasting framework based
on the underlying data of the electricity consumption of household appliances. In the
proposed framework, load distributions for group households are obtained using a similar
day’s extraction module (considering external environmental and internal household
factors affecting energy consumption), a household behavior analysis module (developing
probabilities of appliance consumption behavior), and a household behavior prediction
module.

However, unfortunately, this framework has only been veriﬁed in the group data of
multiple groups of families, which has a better prediction effect on the load distribution
of group families. For a single family, Zheng et al. [39] et al. veriﬁed that the bottom-up
method equipped with the long- and short-term memory cyclic neural network (LSTM)
model could obtain better results than the direct prediction at the family level. However,
for practical applications of the bottom-up approach, the LSTM model is inefﬁcient and
expensive. In order to effectively model a variety of different device usage patterns, a more
realistic lightweight algorithm is applied—the Kalman ﬁlter model adaptively predicts
device usage with less historical data and shorter computational time, outperforming large
algorithms such as the LSTM model. The literature [40] proposed a bottom-up method
considering the load characteristics of the equipment level. Considering the working
principle and load characteristics of home appliances, home appliances were divided into
continuous load and intermittent load. Through the accumulation of home appliance
loads, more reﬁned load prediction could be achieved. At the same time, considering the
ﬂuctuation of load curve, the loess-based seasonal trend decomposition program (STL) was
applied to continuous load appliances to obtain ﬁner grain and more regular load data.
The model can predict multiple equipment simultaneously and improve the computational
efﬁciency.

In the HEMS, predictions of short-term future electricity consumption are used to
support HEMS decision-making. Although there have been many studies on the predic-
tion of building electricity consumption, there is a lack of spatial analysis of predictive
performance, especially at the household level, the appliance level, or the submeter level.
Zheng et al. [4] adopted a LSTM neural network to establish a multi-step load prediction
model, as shown in Figure 6. The inﬂuence of spatial factors on the forecasting accuracy
of household electricity consumption was analyzed. The results showed that the predic-
tion accuracy can be improved by predicting the electricity consumption of household
appliances ﬁrst and then by aggregating, compared with predicting the electricity consump-
tion of households directly. Using deep learning technology to train the network based
on historical data of energy use of residential appliances, it is also possible to estimate
the energy use of a given appliance in the short term. Razghandi et al. [41] proposed a
residential electricity load forecasting model. This model used an LSTM cyclic neural
network to learn the energy consumption pattern of individual appliances in smart homes.
After preprocessing the data collected by smart meters, we inputted it into the deep neural
network to generate the predicted load consumption of devices and predicted the potential
load consumption of a given appliance at different time intervals.

Energies 2023, 16, 5809

11 of 17

Figure 6. Framework for the proposed appliance-level load forecasting deep learning-based model.

A bottom-up load prediction method requires accurate load prediction for each house-
hold appliance. This kind of device-level load prediction is a very challenging task. Pre-
vious studies have provided several forecasting frameworks, although they all have had
good simulation effects [42,43]. However, their feasibility still needs to be studied. The
deep learning algorithms used by the framework are relatively simple, and most of them
cannot give consideration to both accuracy and efﬁciency. According to the author, from
the power performance of equipment, the living habits of household users, the structural
characteristics of intelligent prediction algorithm, and so on, the probabilistic prediction
method considering load uncertainty is integrated, and the improved LSTM neural network
which has proved to be the most advanced load prediction algorithm is used. It is a worthy
research direction to develop a set of equipment-level load forecasting models which take
into account both prediction accuracy and practical feasibility.

4.2. The Challenge of Hourly Load Forecasting

On the other hand, with the deployment of IOT devices in buildings, electricity load
usage can be collected in real time, and the real-time data collection and processing makes
ultra-short-term load prediction at the hour level possible [44]. The literature [45] uses BN
to simulate the relationship between variables and proposes a multi-family ultra-short-term
load forecasting method that does not use a single generalist model and multivariate data
for load aggregation. Ageng et al. [46] proposed an hourly load prediction framework
combining data preparation and LSTM. Firstly, interpolation and Savitzky–Golay ﬁltering
were carried out on the collected data so as to extract the appropriate load consumption
mode for the next hour’s load prediction. In addition, in order to better determine the
relationship between the time series information, a two-layer LSTM was used.

It has been found from a large number of studies that in the ultra-short-term household
appliance load prediction, data-driven models such as artiﬁcial neural networks can predict
the trend of electric energy consumption of electrical equipment but often ignore the
consumption peak [47], that is, the switch state prediction of electrical equipment is more
accurate, while the peak prediction still has defects, as shown in Figure 7.

Energies 2023, 16, x FOR PEER REVIEW 11 of 17    Figure 6. Framework for the proposed appliance-level load forecasting deep learning-based model. A bottom-up load prediction method requires accurate load prediction for each household appliance. This kind of device-level load prediction is a very challenging task. Previous studies have provided several forecasting frameworks, although they all have had good simulation eﬀects [42,43]. However, their feasibility still needs to be studied. The deep learning algorithms used by the framework are relatively simple, and most of them cannot give consideration to both accuracy and eﬃciency. According to the author, from the power performance of equipment, the living habits of household users, the struc-tural characteristics of intelligent prediction algorithm, and so on, the probabilistic pre-diction method considering load uncertainty is integrated, and the improved LSTM neu-ral network which has proved to be the most advanced load prediction algorithm is used. It is a worthy research direction to develop a set of equipment-level load forecasting mod-els which take into account both prediction accuracy and practical feasibility. 4.2. The Challenge of Hourly Load Forecasting On the other hand, with the deployment of IOT devices in buildings, electricity load usage can be collected in real time, and the real-time data collection and processing makes ultra-short-term load prediction at the hour level possible [44]. The literature [45] uses BN to simulate the relationship between variables and proposes a multi-family ultra-short-term load forecasting method that does not use a single generalist model and multivariate data for load aggregation. Ageng et al. [46] proposed an hourly load prediction framework combining data preparation and LSTM. Firstly, interpolation and Savitzky–Golay ﬁltering were carried out on the collected data so as to extract the appropriate load consumption mode for the next hour’s load prediction. In addition, in order to better determine the relationship between the time series information, a two-layer LSTM was used. It has been found from a large number of studies that in the ultra-short-term house-hold appliance load prediction, data-driven models such as artiﬁcial neural networks can predict the trend of electric energy consumption of electrical equipment but often ignore the consumption peak [47], that is, the switch state prediction of electrical equipment is more accurate, while the peak prediction still has defects, as shown in Figure 7. It is helpful to predict the load consumption in the next hour of the household to correctly manage household energy [48]. However, ultra-short-term load prediction is not easy to achieve, mainly for the following reasons: (1) The dynamic behavior of each user will aﬀect the load usage pattern, which plays a major role in the hourly load prediction. (2) Transmission and technical errors will also aﬀect load usage patterns, thus reducing the accuracy of ultra-short-term load prediction. (3) Inevitably, data loss or overﬂow may Energies 2023, 16, 5809

12 of 17

Figure 7. Load prediction results of different electrical equipment based on data-driven model.

It is helpful to predict the load consumption in the next hour of the household to
correctly manage household energy [48]. However, ultra-short-term load prediction is not
easy to achieve, mainly for the following reasons: (1) The dynamic behavior of each user
will affect the load usage pattern, which plays a major role in the hourly load prediction.
(2) Transmission and technical errors will also affect load usage patterns, thus reducing
the accuracy of ultra-short-term load prediction. (3) Inevitably, data loss or overﬂow may
occur due to hardware or system errors. Noise can also be added to the collected data. In
this case, the accuracy of the load forecast for the next hour will be reduced.

In future research, the method of hyperparameter adjustment can be developed to
improve the prediction accuracy. Secondary inﬂuences on load consumption, including the
number of people, season, and holiday period, can also be further studied.

Energies 2023, 16, x FOR PEER REVIEW 12 of 17   occur due to hardware or system errors. Noise can also be added to the collected data. In this case, the accuracy of the load forecast for the next hour will be reduced. In future research, the method of hyperparameter adjustment can be developed to improve the prediction accuracy. Secondary inﬂuences on load consumption, including the number of people, season, and holiday period, can also be further studied.  Figure 7. Load prediction results of diﬀerent electrical equipment based on data-driven model.   Energies 2023, 16, 5809

13 of 17

5. Load Forecasting Is Used for Electricity Scheduling in the HEMS

Recently, the home energy management system (HEMS) as the main energy saving
countermeasure has gradually become the focus of residential energy optimization research.
In the context of the smart grid, the HEMS, as a hub connecting users with the power grid,
aims to optimize the utilization of electric energy by household users [49,50]. Table 2 shows
part of the data collected by smart meters. The main function of the HEMS is to optimize
household energy use, improve energy efﬁciency and user comfort through optimization
algorithms and scheduling strategies, and achieve energy saving and consumption reduc-
tion by relying on the scheduling of distributed energy and energy storage devices through
detection facilities such as smart meters and sensors [51]. The HEMS structure is shown
in Figure 8. According to the information of users’ electricity demand, environmental
conditions, and price incentives, the built-in residential electricity optimization strategy is
applied to adjust the operation of various electrical appliances, optimize the user load curve,
and participate in peak regulation. Household load forecasting can predict household elec-
tricity demand in advance, help households better plan energy use, and reduce electricity
costs and unnecessary energy waste. Schmidt et al. [4] proposed a probabilistic model for
predicting the electrical consumption of household appliances based on historical data,
taking into account three main factors: (1) the time elapsed after the last use of household
appliances; (2) the time of day during which the appliance may be used; (3) behavioral
patterns of occupants (for example, people are likely to use the washing machine two to
three times more on weekends than weekdays). The authors aim to provide advice to
occupants and improve home automation systems for load shifting or scheduling without
affecting the comfort of occupants.

Table 2. A segment of the data collected by smart meters.

Time

Active Power
(kW)

Reactive Power
(kW)

Average Voltage
(V)

Average Current
Intensity (A)

Total Load
(W·h)

16 December 2016 17:24:00
16 December 2016 17:25:00
16 December 2016 17:26:00
16 December 2016 17:27:00

4.216
5.360
5.374
5.388

0.418
0.436
0.498
0.502

234.840
233.630
233.290
233.740

18.400
23.000
23.000
23.000

18
17
19
18

Figure 8. Schematic diagram of the home energy management system.

Energies 2023, 16, x FOR PEER REVIEW 13 of 17   5. Load Forecasting Is Used for Electricity Scheduling in the HEMS Recently, the home energy management system (HEMS) as the main energy saving countermeasure has gradually become the focus of residential energy optimization re-search. In the context of the smart grid, the HEMS, as a hub connecting users with the power grid, aims to optimize the utilization of electric energy by household users [49,50]. Table 2 shows part of the data collected by smart meters. The main function of the HEMS is to optimize household energy use, improve energy eﬃciency and user comfort through optimization algorithms and scheduling strategies, and achieve energy saving and con-sumption reduction by relying on the scheduling of distributed energy and energy storage devices through detection facilities such as smart meters and sensors [51]. The HEMS structure is shown in Figure 8. According to the information of users’ electricity demand, environmental conditions, and price incentives, the built-in residential electricity optimi-zation strategy is applied to adjust the operation of various electrical appliances, optimize the user load curve, and participate in peak regulation. Household load forecasting can predict household electricity demand in advance, help households better plan energy use, and reduce electricity costs and unnecessary energy waste. Schmidt et al. [4] proposed a probabilistic model for predicting the electrical consumption of household appliances based on historical data, taking into account three main factors: (1) the time elapsed after the last use of household appliances; (2) the time of day during which the appliance may be used; (3) behavioral patterns of occupants (for example, people are likely to use the washing machine two to three times more on weekends than weekdays). The authors aim to provide advice to occupants and improve home automation systems for load shifting or scheduling without aﬀecting the comfort of occupants. Table 2. A segment of the data collected by smart meters. Time Active Power (kW) Reactive Power (kW) Average Voltage (V) Average Current  Intensity (A) Total Load (W·h) 16 December 2016 17:24:00 4.216 0.418 234.840 18.400 18 16 December 2016 17:25:00 5.360 0.436 233.630 23.000 17 16 December 2016 17:26:00 5.374 0.498 233.290 23.000 19 16 December 2016 17:27:00 5.388 0.502 233.740 23.000 18  Figure 8. Schematic diagram of the home energy management system.   Energies 2023, 16, 5809

14 of 17

The HEMS can dispatch energy consumption in households through real-time electric-
ity prices. It should be noted that although power companies release price information to
customers through smart meters or the network [52], the price data are usually released
several hours in advance for the next time period. Therefore, when scheduling using the
HEMS, the electricity price data for the scheduling period may be partially unknown. In
this case, only with the short-term forecasting function, the HEMS can better adjust the
working state of power equipment according to the energy consumption data and future
electricity price, so as to meet the needs of users and reduce the system operation cost.
Load prediction error will increase the uncertainty of the HEMS and affect the dispatching
performance of the household energy management system [53–58]. Therefore, a mature
household energy management system must be equipped with a set of efﬁcient household
load forecasting models.

According to the different consumption modes and user demand, household electric-
ity load can be divided into dispatchable load and undispatchable load. These include
high-voltage AC transmission systems, washing machines, clothes dryers, water heaters,
dishwashers, electric vehicles, pumps for home swimming pools, etc. Under certain condi-
tions, when the operation of this equipment scheduling will not affect the comfort of users,
they are schedulable loads. The unschedulable loads mainly include computers, refrigera-
tors, lighting systems, security systems, etc. The scheduling of these loads will seriously
affect the satisfaction of users. Therefore, optimizing the scheduling of the schedulable
load is one of the important ways to realize the demand response of residents. However,
predicting the power consumption of a schedulable load such as a washing machine is a
challenging task.

In the future, with the popularity of the smart home and the development of the
HEMS, household appliance load prediction will play a more important role. Future
research directions include improving prediction accuracy, improving real-time perfor-
mance and stability of algorithms, and developing more intelligent and sustainable energy
management systems.

6. Summary and Prospect

At present, the energy consumption of the household as a unit is increasing. In order
to make rational use of energy and optimize user cost, energy management with the HEMS
as the main energy-saving countermeasure has gradually become the focus of residential
energy optimization research. Accurate short-term household load prediction can effec-
tively improve the energy management efﬁciency and reliability of the HEMS, so as to
achieve the goal of efﬁcient utilization of energy and energy saving and emission reduction.
In this paper, we reviewed the latest research results of the deep neural network load
prediction method and probabilistic load prediction method in household load prediction,
and summarized and analyzed the network prediction model, feature extraction method,
adaptive learning ability of the network, equipment-level load prediction method, and
other aspects. The key role of short-term household appliance load forecasting in HEMS
dispatching was also pointed out.

Although many models and methods have achieved certain results in short-term

household load prediction, there are still many problems to be solved in future research:

1.

2.

Data quality: Short-term household load forecasting requires a large amount of histor-
ical load data and other relevant data, such as temperature and humidity. However,
the existing data often have quality problems, such as missing values, noise, etc.,
which will affect the prediction results.
Prediction accuracy of the model: Although the deep learning model has achieved a
certain accuracy in household load prediction, there is still a lot of room for improve-
ment. Researchers need to explore new model structures or optimization algorithms
to improve the prediction accuracy.

Energies 2023, 16, 5809

15 of 17

Generalization ability of the model: The deep learning model is prone to overﬁtting,
especially when the data set is small. Therefore, how to enhance the generalization ability
of the model is an important research direction.

3.

Real-time performance and uncertainty: Household load forecasting involves many
uncertain factors, such as weather and user behavior. Therefore, how to consider
these uncertainties and integrate them into the deep learning model is also a problem
that needs to be studied.

4. Model interpretability: Deep learning models are generally regarded as black box
models. In practical applications, the interpretability of models can facilitate users
to better understand the prediction results of models and make corresponding deci-
sions. However, in past studies, the explanatory forecasting framework of short-term
household load is rarely involved.

To solve these problems, in the future, the research direction of short-term household

appliance load prediction will include the following aspects:

1.

Explore more data sources: The continuous progress of data mining and preprocess-
ing technology can improve the quality of data and reduce the workload of data
processing. The construction of data sharing and open platform will help promote
the research progress of short-term household load forecasting and promote its ap-
plication in practical production. In addition to electricity consumption data, other
data can be used, such as meteorological data, calendar data, social media data, etc.,
to help forecast household load. Therefore, it is possible to consider how to combine
different data sources to improve the accuracy of the prediction.

2. Model innovation: Model fusion and integrated learning technology can combine the
advantages of various models to improve the prediction accuracy and robustness, such
as the hybrid model of different deep learning neural networks, the model combining
the probabilistic prediction method with deep learning time series model, etc. The
development of intelligent technologies, such as deep learning and natural language
processing (NLP), is expected to bring new breakthroughs for short-term household
load forecasting and improve the forecasting effect. In addition, exploring the use of
multi-task learning methods to realize synchronous prediction of multiple tasks such
as power consumption and power can also improve the prediction performance of
the model.

Author Contributions: Conceptualization, P.M.; Formal analysis, S.C.; Data curation, M.C.; Writing—
original draft preparation, P.M.; Methodology, P.M.; Investigation, S.Z.; Writing—review and editing,
S.C.; Project administration, K.W. All authors have read and agreed to the published version of the
manuscript.

Funding: This research was funded by the Youth Fund of Shandong Province Natural Science
Foundation grant number ZR2020QE212, Key Projects of Shandong Province Natural Science Foun-
dation grant number ZR2020KF020, the Guangdong Provincial Key Lab of Green Chemical Product
Technology grant number GC202111, Zhejiang Province Natural Science Foundation grant number
LY22E070007, and National Natural Science Foundation of China grant number 52007170.

Data Availability Statement: Data are contained within the article.

Conﬂicts of Interest: The authors declare that they have no known competing ﬁnancial interests or
personal relationships that could have appeared to inﬂuence the work reported in this paper.

References

1.

2.

3.

Lusis, P.; Khalilpour, K.R.; Andrew, L.; Liebman, A. Short-term residential load forecasting: Impact of calendar effects and forecast
granularity. Appl. Energy 2017, 205, 654–669. [CrossRef]
Sun, X.; Zhang, Y.; Zhang, Y.C.; Wang, L.; Wang, K. Summary of Health-State Estimation of Lithium-Ion Batteries Based on
Electrochemical Impedance Spectroscopy. Energies 2023, 16, 5682. [CrossRef]
Imani, M.; Ghassemian, H. Residential load forecasting using wavelet and collaborative representation transforms. Appl. Energy
2019, 253, 113505. [CrossRef]

Energies 2023, 16, 5809

16 of 17

4.

5.

6.

7.
8.

9.

Zheng, Z.; Chen, H.; Luo, X. Spatial granularity analysis on electricity consumption prediction using LSTM recurrent neural
network. Energy Procedia 2018, 158, 2713–2718. [CrossRef]
Kim, T.; Jang, M.; Jeong, H.C.; Joo, S.-K. Short-Term Residential Load Forecasting Using 2-Step SARIMAX. J. Electr. Eng. Technol.
2021, 17, 751–758. [CrossRef]
Ceperic, E.; Ceperic, V.; Baric, A. A Strategy for Short-Term Load Forecasting by Support Vector Regression Machines. IEEE Trans.
Power Syst. 2013, 28, 4356–4364. [CrossRef]
Dudek, G. A Comprehensive Study of Random Forest for Short-Term Load Forecasting. Energies 2022, 15, 7547. [CrossRef]
Candanedo, L.M.; Feldheim, V.; Deramaix, D. Data driven prediction models of energy use of appliances in a low-energy house.
Energy Build. 2017, 140, 81–97. [CrossRef]
Lu, C.N.; Wu, H.T.; Vemuri, S. Neural Network Based Short-Term Load Forecasting. IEEE Trans. Power Syst. 1993, 8, 336–342.
[CrossRef]

10. Hochreiter, S.; Schmidhuber, J. Long short-term memory. Neural Comput. 1997, 9, 1735–1780. [CrossRef]
11. Ma, N.; Yin, H.; Wang, K. Prediction of the Remaining Useful Life of Supercapacitors at Different Temperatures Based on

Improved Long Short-Term Memory. Energies 2023, 14, 5240. [CrossRef]

12. Liu, J.; Li, J.; Yang, L.; Yan, Y.; Liu, Y.; Zhang, Y. Short-term household load forecasting based on EMD-SLSTM. Power Syst. Prot.

Control 2019, 47, 40–47.

13. Moradzadeh, A.; Zakeri, S.; Shoaran, M.; Mohammadi-Ivatloo, B.; Mohammadi, F. Short-Term Load Forecasting of Microgrid via

Hybrid Support Vector Regression and Long Short-Term Memory Algorithms. Sustainability 2020, 12, 7076. [CrossRef]

14. Acharya, S.K.; Wi, Y.M.; Lee, J. Short-Term Load Forecasting for a Single Household Based on Convolution Neural Networks

Using Data Augmentation. Energies 2019, 12, 3560. [CrossRef]

15. Andriopoulos, N.; Magklaras, A.; Birbas, A.; Papalexopoulos, A.; Valouxis, C.; Daskalaki, S.; Birbas, M.; Housos, E.; Papaioannou,
G.P. Short Term Electric Load Forecasting Based on Data Transformation and Statistical Machine Learning. Appl. Sci. 2020, 11,
158. [CrossRef]

16. Cheng, X.; Wang, L.; Zhang, P.; Wang, X.; Yan, Q. Short-term fast forecasting based on family behavior pattern recognition for

17.

small-scale users load. Clust. Comput. 2021, 25, 2107–2123. [CrossRef]
Jiang, L.; Wang, X.; Li, W.; Wang, L.; Yin, X.; Jia, L. Hybrid Multitask Multi-Information Fusion Deep Learning for Household
Short-Term Load Forecasting. IEEE Trans. Smart Grid 2021, 12, 5362–5372. [CrossRef]

18. Guo, X.; Gao, Y.; Li, Y.; Zheng, D.; Shan, D. Short-term household load forecasting based on Long- and Short-term Time-series

19.

network. Energy Rep. 2021, 7, 58–64. [CrossRef]
Syed, D.; Abu-Rub, H.; Ghrayeb, A.; Refaat, S.S. Household-Level Energy Forecasting in Smart Buildings Using a Novel Hybrid
Deep Learning Model. IEEE Access 2021, 9, 33498–33511. [CrossRef]

20. Li, L.; Meinrenken, C.J.; Modi, V.; Culligan, P.J. Short-term apartment-level load forecasting using a modiﬁed neural network

with selected auto-regressive features. Appl. Energy 2021, 287, 116509. [CrossRef]

21. Bouktif, S.; Fiaz, A.; Ouni, A.; Serhani, M.A. Single and Multi-Sequence Deep Learning Models for Short and Medium Term

Electric Load Forecasting. Energies 2019, 12, 149. [CrossRef]

22. Tian, C.J.; Ma, J.; Zhang, C.H.; Zhan, P.P. A Deep Neural Network Model for Short-Term Load Forecast Based on Long Short-Term

Memory Network and Convolutional Neural Network. Energies 2018, 11, 3493. [CrossRef]

23. Kiprijanovska, I.; Stankoski, S.; Ilievski, I.; Jovanovski, S.; Gams, M.; Gjoreski, H. HousEEC: Day-Ahead Household Electrical

Energy Consumption Forecasting Using Deep Learning. Energies 2020, 13, 2672. [CrossRef]

24. Yang, W.; Shi, J.; Li, S.; Song, Z.; Zhang, Z.; Chen, Z. A combined deep learning load forecasting model of single household

resident user considering multi-time scale electricity consumption behavior. Appl. Energy 2022, 307, 118197. [CrossRef]

25. Hou, T.; Fang, R.; Tang, J.; Ge, G.; Yang, D.; Liu, J.; Zhang, W. A Novel Short-Term Residential Electric Load Forecasting Method

Based on Adaptive Load Aggregation and Deep Learning Algorithms. Energies 2021, 14, 7820. [CrossRef]

26. He, Y.; Luo, F.; Ranzi, G. Transferrable Model-Agnostic Meta-learning for Short-Term Household Load Forecasting with Limited

Training Data. IEEE Trans. Power Syst. 2022, 37, 3177–3180. [CrossRef]

27. Gomez-Rosero, S.; Capretz, M.A.M.; Mir, S. Transfer Learning by Similarity Centred Architecture Evolution for Multiple

28.

29.

Residential Load Forecasting. Smart Cities 2021, 4, 217–240. [CrossRef]
Fujimoto, Y.; Fujita, M.; Hayashi, Y. Deep reservoir architecture for short-term residential load forecasting: An online learning
scheme for edge computing. Appl. Energy 2021, 298, 117176.
Fekri, M.N.; Patel, H.; Grolinger, K.; Sharma, V. Deep learning for load forecasting with smart meter data: Online Adaptive
Recurrent Neural Network. Appl. Energy 2021, 282, 116177.

30. Hong, T.; Fan, S. Probabilistic electric load forecasting: A tutorial review. Int. J. Forecast. 2016, 32, 914–938. [CrossRef]
31. Liu, B.D.; Nowotarski, J.; Hong, T.; Weron, R. Probabilistic Load Forecasting via Quantile Regression Averaging on Sister Forecasts.

IEEE Trans. Smart Grid 2017, 8, 730–737. [CrossRef]

32. Wang, Y.; Zhang, N.; Tan, Y.; Hong, T.; Kirschen, D.; Kang, C. Combining Probabilistic Load Forecasts. IEEE Trans. Smart Grid

33.

2018, 10, 3664–3674. [CrossRef]
Feng, C.; Sun, M.C.; Zhang, J. Reinforced Deterministic and Probabilistic Load Forecasting via Q-Learning Dynamic Model
Selection. IEEE Trans. Smart Grid 2020, 11, 1377–1386. [CrossRef]

Energies 2023, 16, 5809

17 of 17

34. Xia, Z.; Ma, H.; Saha, T.K.; Zhang, R. Consumption Scenario-Based Probabilistic Load Forecasting of Single Household. IEEE

Trans. Smart Grid 2022, 13, 1075–1087. [CrossRef]

35. Brusaferri, A.; Matteucci, M.; Spinelli, S.; Vitali, A. Probabilistic electric load forecasting through Bayesian Mixture Density

Networks. Appl. Energy 2022, 309, 118341. [CrossRef]

36. Avancini, D.B.; Rodrigues, J.; Martins, S.G.B.; Rabelo, R.A.L.; Al-Muhtadi, J.; Solic, P. Energy meters evolution in smart grids: A

review. J. Clean. Prod. 2019, 217, 702–715. [CrossRef]

37. Tabatabaei, S.M.; Dick, S.; Xu, W.S. Toward Non-Intrusive Load Monitoring via Multi-Label Classiﬁcation. IEEE Trans. Smart Grid

2017, 8, 26–40. [CrossRef]

38. Gao, B.; Liu, X.; Zhu, Z. A Bottom-Up Model for Household Load Proﬁle Based on the Consumption Behavior of Residents.

Energies 2018, 11, 2112. [CrossRef]

39. Zheng, Z.; Chen, H.; Luo, X. A Kalman ﬁlter-based bottom-up approach for household short-term load forecast. Appl. Energy

2019, 250, 882–894. [CrossRef]

40. Wang, S.; Deng, X.; Chen, H.; Shi, Q.; Xu, D. A bottom-up short-term residential load forecasting approach based on appliance

characteristic analysis and multi-task learning. Electr. Power Syst. Res. 2021, 196, 107233. [CrossRef]

41. Razghandi, M.; Turgut, D. Residential Appliance-Level Load Forecasting with Deep Learning. In Proceedings of the GLOBECOM

42.

43.

2020—2020 IEEE Global Communications Conference, Taipei, Taiwan, 7–11 December 2020; pp. 1–6.
Sirojan, T.; Phung, B.T.; Ambikairajah, E. In Deep Neural Network Based Energy Disaggregation. In Proceedings of the 6th IEEE
International Conference on Smart Energy Grid Engineering (IEEE SEGE), Oshawa, ON, Canada, 12–15 August 2018; pp. 73–77.
Ji, Y.T.; Buechler, E.; Rajagopal, R. Data-Driven Load Modeling and Forecasting of Residential Appliances. IEEE Trans. Smart Grid
2020, 11, 2652–2661. [CrossRef]

44. Cheng, L.M.; Bao, Y.Q.; Tang, L.; Di, H.F. Very-short-term load forecasting based on empirical mode decomposition and deep

neural network. IEEE Trans. Electr. Electron. Eng. 2020, 15, 252–258. [CrossRef]

45. Bessani, M.; Massignan, J.A.D.; Santos, T.M.O.; London, J.B.A.; Maciel, C.D. Multiple households very short-term load forecasting

using bayesian networks. Electr. Power Syst. Res. 2020, 189, 106733. [CrossRef]

46. Ageng, D.; Huang, C.Y.; Cheng, R.G. A Short-Term Household Load Forecasting Framework Using LSTM and Data Preparation.

IEEE Access 2021, 9, 167911–167919. [CrossRef]

47. Tarmanini, C.; Sarma, N.; Gezegin, C.; Ozgonenel, O. Short term load forecasting based on ARIMA and ANN approaches. Energy

Rep. 2023, 9, 550–557. [CrossRef]

48. Hsiao, Y.H. Household Electricity Demand Forecast Based on Context Information and User Daily Schedule Analysis from Meter

Data. IEEE Trans. Ind. Inform. 2015, 11, 33–43. [CrossRef]

49. Zhou, B.; Li, W.T.; Chan, K.W.; Cao, Y.J.; Kuang, Y.H.; Liu, X.; Wang, X. Smart home energy management systems: Concept,

conﬁgurations, and scheduling strategies. Renew. Sustain. Energy Rev. 2016, 61, 30–40. [CrossRef]

50. Wang, F.; Xiang, B.; Li, K.P.; Ge, X.X.; Lu, H.; Lai, J.G.; Dehghanian, P. Smart Households’ Aggregated Capacity Forecasting for

Load Aggregators Under Incentive-Based Demand Response Programs. IEEE Trans. Ind. Appl. 2020, 56, 1086–1097. [CrossRef]

51. Al-Sumaiti, A.S.; Ahmed, M.H.; Salama, M.M.A. Smart Home Activities: A Literature Review. Electr. Power Compon. Syst. 2014,

42, 294–305. [CrossRef]

52. Zhao, X.; Gao, W.; Qian, F.; Ge, J. Electricity cost comparison of dynamic pricing model based on load forecasting in home energy

management system. Energy 2021, 229, 120538. [CrossRef]

53. Tiwari, P.; Mahanta, P.; Trivedi, G. A Dual-Stage Attention based RNN-Model for Short Term Load Forecasting of Individual
Household. In Proceedings of the 2021 International Conference on Electrical, Computer and Energy Technologies (ICECET),
Cape Town, South Africa, 9–10 December 2021; pp. 1–6.

54. Atef, S.; Ismail, N.; Eltawil, A.B. A new fuzzy logic based approach for optimal household appliance scheduling based on

electricity price and load consumption prediction. Adv. Build. Energy Res. 2022, 16, 262–280. [CrossRef]

55. Yi, Z.; Chen, Z.; Yin, K.; Wang, L.; Wang, K. Sensing as the key to the safety and sustainability of new energy storage devices. Prot.

Control. Mod. Power Syst. 2003, 8, 27. [CrossRef]

56. Wang, L.; Xie, L.; Yang, Y.; Zhang, Y.; Wang, K.; Cheng, S.-J. Distributed Online Voltage Control with Fast PV Power Fluctuations

and Imperfect Communication. IEEE Trans. Smart Grid 2023. [CrossRef]

57. Cui, Z.; Dai, J.; Sun, J.; Li, D.; Wang, L.; Wang, K. Hybrid methods using neural network and Kalman ﬁlter for the state of charge

estimation of lithium-ion battery. Math. Probl. Eng. 2022, 2022, 9616124. [CrossRef]

58. Zhang, M.; Yang, D.; Du, J.; Sun, H.; Li, L.; Wang, L.; Wang, K. A Review of SOH Prediction of Li-Ion Batteries Based on

Data-Driven Algorithms. Energies 2023, 16, 3167. [CrossRef]

Disclaimer/Publisher’s Note: The statements, opinions and data contained in all publications are solely those of the individual
author(s) and contributor(s) and not of MDPI and/or the editor(s). MDPI and/or the editor(s) disclaim responsibility for any injury to
people or property resulting from any ideas, methods, instructions or products referred to in the content.

