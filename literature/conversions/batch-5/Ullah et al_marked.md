---
conversion_metadata:
  converted_at: "2026-07-21T09:04:57Z"
  converter_tool: "markitdown"
  converter_version: "0.1.6"
  source_pdf: "Ullah et al.pdf"
  source_pdf_sha256: "c01a3717c20d775a308b8a266b53cb3bd281c31d833364d731d65cba8cfb2956"
  page_count: 24
  markdown_char_count: 286731
---

<!-- PAGE-AWARE EXTRACTION (via pdfminer.six) -->

<!-- PAGE 1 -->

Received 26 July 2024, accepted 6 August 2024, date of publication 8 August 2024, date of current version 21 August 2024.

Digital Object Identifier 10.1109/ACCESS.2024.3440631

Short-Term Load Forecasting: A Comprehensive
Review and Simulation Study With CNN-LSTM
Hybrids Approach

KALEEM ULLAH 1, MUHAMMAD AHSAN 2, SYED MUHAMMAD HASANAT1,
MUHAMMAD HARIS 3, HAMZA YOUSAF 4, SYED FARAZ RAZA2, RITESH TANDON5,
SAMAIN ABID2, AND ZAHID ULLAH 6, (Graduate Student Member, IEEE)
1Centre for Advanced Studies in Energy, University of Engineering and Technology, Peshawar (UET Peshawar), Peshawar 25000, Pakistan
2Department of Computer Science, University of Alabama at Birmingham, Birmingham, AL 35294, USA
3Institute for Insight, J. Mack Robinson College of Business, Georgia State University, Atlanta, GA 30303, USA
4Stetson-Hatcher School of Business, Mercer University, Macon, GA 30341, USA
5School of Informatics, Computing, and Engineering, Indiana University, Bloomington, IN 47405, USA
6Dipartimento di Elettronica, Informazione e Bioingegneria, Politecnico di Milano, 20133 Milan, Italy

Corresponding author: Zahid Ullah (zahid.ullah@polimi.it)

This work was supported by the Politecnico di Milano for providing Open Access within the CRUI CARE Agreement.

ABSTRACT Short-term load forecasting (STLF) is vital in effectively managing the reserve requirement in
modern power grids. Subsequently, it supports the grid operator in making effective and economical decisions
during the power balancing operation. Therefore, this study comprehensively reviews STLF methods,
including time series analysis, regression-based frameworks, artificial neural networks (ANNs), and hybrid
models that employ different forecasting approaches. Detailed mathematical and graphical analyses and
a comparative evaluation of these methods are provided, highlighting their advantages and disadvantages.
Further, the study proposes a hybrid CNN-LSTM model comprised of Convolutional neural networks (CNN)
for feature extraction of high dimensional data and Long short-term memory (LSTM) networks to boost the
model’s efficiency for temporal sequence prediction. This study assessed the model using a comprehensive
dataset from Pakistan’s NTDC national grid. The analysis revealed superior performance in short-term load
prediction, achieving enhanced accuracy. For single-step forecasting, the model yielded an RMSE of 538.71,
MAE of 371.97, and MAPE of 2.72. In 24-hour forecasting, it achieved an RMSE of 951.94, MAE of
656.35, and MAPE of 4.72 on the NTDC dataset. Moreover, the model has outperformed previous models
in comparison using the AEP dataset, demonstrating its superiority in enhancing reserve management and
balancing supply and demand in modern electricity networks.

INDEX TERMS Short-term load forecasting, convolution neural network, hybrid LSTM-CNN network,
NTDC Pakistan, power balancing operation.

I. INTRODUCTION
Forecasting load demand is central to power system manage-
ment and planning; thus, the accuracy of available demand
forecasting models is crucial for effectively managing power
grids. From this perspective, short-term load forecasting
(STLF) enables the proper management of energy resources
and the accurate control of energy storage. The accurate and
timely predictions of possible future load variations by STLF

The associate editor coordinating the review of this manuscript and

approving it for publication was Akshay Kumar Saha

.

also enhance the work of utilizing the available resources,
hence improving the overall functionality of the systems [1].
STLF constitutes a fundamental element in energy man-
agement [2]. These models are made for forecasting power
requirements for the short-term timeframe ranging from an
hour ahead to days or weeks at most but typically up to a
maximum of one month only. These models are invaluable for
utility companies and grid operators as they help in planning
the resources using better foresight to manage the responses
to the ever-changing energy requirements that ensure the sta-
bility and availability of the power supply systems. However,

111858

2024 The Authors. This work is licensed under a Creative Commons Attribution 4.0 License.
For more information, see https://creativecommons.org/licenses/by/4.0/

VOLUME 12, 2024

---

<!-- PAGE 2 -->

K. Ullah et al.: STLF: A Comprehensive Review and Simulation Study

in the progress made before the big data era, various STLF
methodologies have appeared in the literature, each with
inherent features and limitations [3]. These frameworks cover
a spectrum of computation methods, including artificial neu-
ral networks (ANNs), time series analysis, regression-based
methods, and a combination of both (hybrid systems). The
time series methods utilize historical load information using
variant statistical tools, including ARIMA models and dif-
ferent types of exponential smoothing, to identify and then
temporally analyze load trends to improve load forecasts’
accuracy [4]. Contrarily, ANNs are a complex set of machine
learning structures capable of learning input-output mapping
that otherwise has a non-linear relationship. These mod-
els are trained across various data set assemblages using
backpropagation networks, enabling them to adapt to infor-
mation complex formation [5]. Regression-based models
utilize linear or non-linear regression techniques to map
causal associations with load and other features such as
humidity, temperature, and time of day [6].

Contrarily, integrated models blend the strengths of dif-
ferent modeling approaches, such as ANNs and time series
analysis, with the explicit intention of improving accuracy
and increasing resistance to interference [7]. Though, each
class of model has its unique difficulties and oddities. For
example, in time series models, challenges often arise in
explaining enduring trends and temporary fluctuations, load
data in particular, reacting more sharply to anomalies and
gaps in information. However, there are drawbacks associ-
ated with the computational complexity of ANNs, which
subsequently decreases their levels of interpretability; this
is coupled with their inherent tendency to fit over. Further,
ANNs suffer from noise and bias in training data and are
also sensitive to variations [8]. A major drawback of the
regression-based models is that they are generally restricted
to identifying linear and additive relations within input/output
data. In addition, the models are not accustomed to handling
categorical or non-numerical data. These challenges threaten
the model as it cannot effectively employ graph structures to
represent or analyze complex data [9].

Alternatively, some drawbacks of hybrid models include
the contingency of the Extended Model with increased model
complexity and an increased number of parameters, issues in
parameter tuning, and primary issues of overfitting and data
redundancy of the model. In this regard, the necessary steps
must be taken to tackle these issues by comparing and assess-
ing the different STLF models. This should be done regarding
some of the actual load data that has been evaluated and
verified using a wide range of measures and methods for val-
idation purposes to understand their efficiency and reliability
better. This way, considering one’s advantages and challenges
makes it possible to evaluate and compare various model
types and assess their applicability in sustainably addressing
the complexity of load forecasting in practical operational
environments. Given the current fast-paced development in
AI and data processing methods, there is an ongoing need
to engage the sources that present the most contemporary

syntheses of STLF models. These updates are important in
keeping up with the current technological advancements and
improving the prediction factors. To address this research
gap, this review manuscript discusses the preceding points
and explores advanced or relatively new STLF models that
the earlier reviews may not have captured well. It also pro-
poses a novel integration approach of LSTM for time series
analysis and CNN for features from high-dimension data to
enhance precision in prediction. By evaluating the result of
the model, the NTDC Pakistan National Grid offered a data
set for the study.

A. LITERATURE SURVEY
The construction of STLF models is a challenging and com-
plicated activity because it has to deal with various concerns
connected to the dynamic features of load data. These data
are time-dependent and affected by factors such as the cli-
mate state, economic characteristics, and buyers’ behaviour,
whether they are individuals or companies [10]. Conse-
quently, there is a need for STLF models to incorporate the
skills that allow them to learn these dynamic data generation
processes. Apart from controlling transient information, deal-
ing with uncertainties and risks poses major challenges [11].
Other conventional approaches offer some forecast, more
often, just a point estimation while failing to incorporate
corresponding variability or risk. Tremendous efforts need to
be made to bridge this divide and implement more advanced
models that provide probabilistic forecasts, as demonstrated
by the models that utilize the quantile regression approach.
These reports employ advanced methodologies as a way of
addressing issues of variability that are often associated with
the data.

Moreover, incorporating wind and solar power as a part
of renewable energy also adds fluctuations and randomness
to the power supply, negatively impacting the precision and
efficiency of STLF models [12]. Similar challenges relate
to data characteristics in studying current trends; the data
field is high-dimensional, and various input variables such
as weather conditions, vacation plans, and economic activity
indicators exist. This implies that identifying and selecting
relevant predictors for regression models is a significant step
toward avoiding overfitting and improving forecasting pre-
cision [13]. Moreover, it can be found that non-Gaussian
and highly salience distributions are usually present in load
data [14], and these characteristics are not suitable for most
of the traditional approaches for forecast-based models since
they violate the basic assumptions. This means that effec-
tive models need to incorporate such relation patterns, and
therefore, the structure includes load data and other aspects
such as climates and economic factors. The temporal and,
mainly, spatial structure of load data adds further challenge
because the load often exhibits different patterns depending
on the geographic location and time of day or year, and this
information must be incorporated into models by recognizing
and providing for spatial correlations and variations in load.

VOLUME 12, 2024

111859

---

<!-- PAGE 3 -->

Further, the clarity and interpretability of STLF models are
critical as these models play a crucial role in driving key deci-
sions in the energy sector, such as Load management [15].
Those undertaking decision-making roles in energy systems
must have comprehensible model results to act promptly and
efficiently. However, a need for data, which is both scarce
and of questionable quality, is the last but very important
matter that hinders the creation of accurate STLF models. The
high-quality data needed to train and validate the different
models points to the significant need to address data issues if
the accuracy of the climate forecasts is to be enhanced.

These challenges have, for instance, been elaborated in
detail to understand the best methodological approaches to
conduct research in the STLF and other solutions towards
creating innovative strategies to solve them within the field.
Similarly, for coping with the non-stationary data, new mod-
els that are time-varying, such as TVARMA, and for having
better learning algorithms, such as DNNs, have been devel-
oped [11], [14]. To enhance dealing with uncertainty and risk,
various statistical methodologies like quantile regression and
scenario-based forecasting have been employed [16], [17].
The integration of STLF with the forecasts of renewable
energy intends to enhance accuracy. It is further supported
by demand response and energy storage to cope with fluctua-
tions in the renewable source [12]. Methods used for feature
selection and dimensionality include feature selection and
dimensionality reduction, which is crucial in handling the
huge and complicated nature of STLF data. At the same
time, robust models and distribution approaches address
non-Gaussian distributions of data [18]. Nonparametric and
kernel-based models are preferred for nonlinearity relations
since they are more effective than parametric models [14].
Spatial and temporal models and clustering methods are
properly employed to account for and promote spatial prop-
erties dependency. Causal inference methods are used to
enhance the trust in models for energy management as trans-
parency and interpretability of the models are essential for
informed decision-making in the corresponding domain [14].
The aforementioned data availability and quality concerns are
also discussed, as well as other methods, including data aug-
mentation, transfer learning, and domain adaptation. These
methods enhance the reliability and versatility of the STLF
models and extend the horizons of forecasting trends to the
energy industry [19], [20].

B. PAPER CONTRIBUTION
The study comprehensively reviews STLF methods, includ-
ing time series analysis, regression-based frameworks, artifi-
cial neural networks (ANNs), and hybrid models that employ
different forecasting approaches. Detailed mathematical and
graphical analyses and a comparative evaluation of these
methods are provided, highlighting their advantages and dis-
advantages. Furthermore, the research suggests a combined
model of CNN and LSTM for deeper characteristics extrac-
tion and temporal sequence analysis, respectively, to enhance

K. Ullah et al.: STLF: A Comprehensive Review and Simulation Study

prediction precision. This work uses a possessive dataset of
the national network of NTDC Pakistan to test and validate
the model. The proposed model demonstrates exceptional
accuracy in single-step and 24-hour forecasting, achieving
significantly lower error metrics than the reference meth-
ods. For single-step forecasting, the NTDC dataset shows
an RMSE of 538.71, MAE of 371.97, and MAPE of 2.72,
while the AEP dataset achieves an RMSE of 126.35, MAE
of 94.27, and MAPE of 0.64. For 24-hour forecasting, the
NTDC dataset reports an RMSE of 951.94, MAE of 656.35,
and MAPE of 4.72, and the AEP dataset shows an RMSE of
702.97, MAE of 507.97, and MAPE of 3.39.

C. STRUCTURE OF THE PAPER
The paper is divided into two main sections, as shown
in Figure 1: a comprehensive review and development of
a practical hybrid model for STLF. The review examines
various STLF models, including statistical, intelligent, and
hybrid models, each subject to detailed analysis. The (2nd )
section of the paper presents an innovative hybrid approach
using LSTM and CNN for single-stage and multi-stage load
forecasting.

FIGURE 1. Organization of the paper.

II. LOAD FORECASTING LEVELS
Load forecasting operates at different levels, each serving
specific managerial goals and employing various methods.
Micro-level forecasting involves analyzing smaller segments
within a region to estimate load patterns, which is crucial for
managing energy plants and grids.

Macro-level forecasting looks at broader areas like cities or
countries without dividing them into smaller parts. Regarding
the time of the forecast for the load, they are divided into
three levels, including short, medium, and long forecasting
levels, as shown in Fig. 2 [21]. Short-term forecasting pre-
dicts hourly loads, important for energy plant scheduling and
grid stability. Mid-term forecasting covers monthly to yearly
projections for managing peak consumption and resource
planning. Long-term forecasting helps with major decisions
like investing in infrastructure and planning for future energy
needs. Despite using different methods, all forecasting levels

111860

VOLUME 12, 2024

---

<!-- PAGE 4 -->

K. Ullah et al.: STLF: A Comprehensive Review and Simulation Study

FIGURE 2. Time frames for the load forecasting levels.

consider factors like population growth and energy prices to
make accurate predictions. In this study, the STLF models are
emphasized.

III. STLF MODELS
Traditional methods for STLF rely on historical data related
to electricity consumption, weather conditions, and calen-
dar events. Conversely, the proliferation of emerging data
channels, such as social media analytics and granular teleme-
try from smart measurement infrastructures, represents an
excellent opportunity to improve the accuracy and robust-
ness of STLF paradigms. Using sophisticated computational
methods, including deep neural architectures and adaptive
reinforcement learning algorithms, is expected to signifi-
cantly optimize STLF systems’ precision. Deep learning
enables the automatic extraction of intricate data patterns
and relationships, while reinforcement learning facilitates
optimizing actions based on environmental feedback [22].
Further, converting the forecasts into point forecasts enables
power system operators to make the right decisions when the
actual uncertainty is experienced by including the probability
estimation of the point forecasts. STLF models cover statis-
tical, intelligent, and hybrid systems, all of which have their
merits and areas of application [23].

A. MODELS BASED ON STATISTICAL TECHNIQUES
Statistical tools grounded on analysis concepts of time series
load demand profiles are particularly useful in explaining the
temporal dynamics contained in load demand profiles. Based
on the bibliography found in the course of the research, the
primary types of statistical structures used in the field of
STLF are as follows: ARIMA models, their seasonal counter-
parts, SARIMA, generalized linear models, and exponential
smoothing models [24]. ARIMA models crucially assume
that current load requirements are formed from past load
sequences and a stochastic term. SARIMA models enhance
this structural plan by incorporating fluctuations of a seasonal
nature, which are almost always present in energy activity
systems where loading demand varies cyclically: diurnal or
menstrual. This integration helps improve the cyclical tem-
poral dependencies to recur at specific intervals to improve
precise prediction models where the load is dominated by

well-defined seasonal behaviour [25]. In turn, exponential
smoothing (ES) models forecast the future load demand
based on seasonal factors by providing certain weights to
the previous values. Despite being accurate, quick to com-
pute, and relatively easy to implement, statistical models
have several limitations stemming from their basic structure;
they may not delineate the nonlinear links and dependen-
cies in power systems and, consequently, could provide less
accurate predictions. EMS for power systems employs STLF
as a foundational component for advanced energy applica-
tions [26]. Hence, a model that can predict accurate STLF
is of utmost significance in optimizing the power system’s
energy supply and demand balance, leading to increased
efficiency in utilizing energy, reduced costs, and system reli-
ability. A detailed explanation of some of these models and a
literature review are presented in the following section.

1) AUTOREGRESSIVE INTEGRATED MOVING AVERAGE
(ARIMA) MODELS
ARIMA models find extensive application in STLF owing
to their straightforward nature and capacity to capture tem-
poral patterns within load data. These models consist of
three main components: the autoregressive (AR) component,
which quantifies the influence exerted by predecessor values;
the integrated (I) component, which incorporates differen-
tiation to achieve stationarity within the data set; and the
moving average (MA) component, which includes the influ-
ence of prior stochastic deviations [27]ARIMA frameworks
provide considerable adaptability through their parametric
customization options, allowing for meticulous calibration
of the AR and MA sequences, alongside the differentiation
magnitude in the I segment. Such configurability facilitates
the model’s alignment with the dataset’s peculiarities and the
precise forecasting prerequisites [28]. Nonetheless, ARIMA
models operate assuming that load data adheres to a station-
ary process, a condition that might not consistently hold in
power system contexts. Moreover, these models may fail to
capture the intricate nonlinear connections between load pat-
terns and various influential factors like weather conditions
and occupancy levels.

Figure 3 gives the algorithm for ARIMA models. The
notation represents the ARIMA model as ARIMA(p,d,q); p
refers to the number of the autoregressive term ‘AR,’ d refers
to the degree of differencing applied to make a time series
stationary, and q refers to the number of moving average
term ‘MA.’ These parameters are explained by comparing the
specific features of the investigated times series inherent char-
acteristics employing advanced stochastic analysis methods,
including the maximum likelihood estimation, to guarantee
the reliability of the fit between the suggested model and
observed data. After assessing these parameters, the ARIMA
model is ready to forecast new values in the time series. Its
mechanism uses past data to guess the next entry in the series
with the help of the AR and the MA parts. Subsequently,
the forecasted value is used to adjust the error term, using

VOLUME 12, 2024

111861

---

<!-- PAGE 5 -->

which an improved estimate of the temporal increment is
derived for the subsequent temporal segment. This process
repeats itself routinely and produces a final forecast covering
pre-designated future periods.

The AR facet requires that today’s observation in the time
series depends on past observations in the same time series.
An AR configuration of order ’p’ is designated as AR(p), with
its respective formulation explicated as follows:

Y (t) = ∁ + ϕ1Y ( − 1) + ϕ2 ( − 2) . . . . . . . . . . . . . . .

+ ϕp ( − p) E( )

(1)

In (1), Y (t) represents the value of the time series at time
t, reflecting the current state of the series. c is a constant
term representing any fixed, unchanging component within
the time series. ϕ1ϕ2 . . . . . . . . . ϕp denote the autoregressive
coefficients, each capturing the influence of past values of
the time series on the present value. These coefficients are
integral to understanding the temporal dependencies within
the series. p signifies the order of the AR model, indicating
the number of past observations considered in predicting the
current value.

FIGURE 3. Algorithm of the ARIMA model.

A higher p-value implies a more extensive consideration
of past values in the prediction process. (ε)(t) represents the
error term at time t, encapsulating the discrepancy between
the predicted value generated by the AR model and the
actual observed value at that time step. This term reflects
the unpredictability or randomness inherent in the time series
data. In the context of the ARIMA model, the parameter ‘d’
signifies the process of differencing. The time series for the
first-order difference is:

(cid:49)Y ( ) = Y ( ) −Y ( − 1)

(2)

Additional stratifications of differencing can be achieved
by iteratively executing the differencing maneuver on a
dataset previously modified by an initial differencing, thereby

K. Ullah et al.: STLF: A Comprehensive Review and Simulation Study

intensifying the transformation to ensure enhanced statisti-
cal constancy. For example, the mechanism of second-order
differencing materializes by applying differencing anew to a
series that has already been subjected to a first-order differ-
encing process.

(cid:49)2Y ( ) = Yt ( ) − Yt ( − 1)

(3)

The MA component embodies the influence of prior error
terms on the current value of the time series. An MA model,
characterized by an order ’ ,’ is denoted as MA( ), with its
equation expressed as follows:

Y(t) = r + ∈ ( ) − ψ1∈ ( − 1 ) − ψ2∈ ( − 2 ) − . . .
(4)

− ψ1∈ ( − ϱ )

In (4), Y(t) denotes the value of the time series at a time
t, reflecting the present conditionsof the series. The term
r represents a constant factor that remains invariant across
the temporal span. In the equation, ∈ (t) signifies the error
term at time t, encapsulating the discrepancy between the
observed value and the value predicted by the model at that
specific time. The coefficients ψ1ψ2ψ3 . . . . . . ψϱ represent
the moving average parameters, determining how much past
error terms influence the current series value. These coeffi-
cients delineate the temporal interdependencies in the series
attributed to antecedent errors. The variable ϱ specifies the
order of the MA model, representing the count of prior error
terms factored into the forecast of the current value. An ele-
vated ϱ value suggests an expansive inclusion of historical
error terms in the predictive framework.

By integrating the AR, I, and MA components, we can

represent an ARIMA(p,d,ϱ) model as:

(cid:49)d Y(t) = ∁ + ϕ1(cid:49)d Y (t − 1) . . . . . . ϕp(cid:49)d Y (t − p) + ∈(t)
− ψ1∈(t − 1) − . . . − ψq∈(t − q)(t)

= (cid:49)Y(t) = Y(t) − Y(t − 1)

(5)

2) SEASONAL AUTOREGRESSIVE INTEGRATED MOVING
AVERAGE (SARIMA) MODEL
SARIMA models, building upon the foundation laid by
ARIMA models, extend their capabilities to accommodate
seasonal variations inherent in various datasets. These models
introduce additional parameters explicitly designed to capture
and interpret the recurring seasonal patterns present within
the data. Within this array of parameters are considerations
on the seasonal interval, with the capability to proficiently
model and predict seasonal variances across various data
contexts [29]. While SARIMA models prove advantageous
for STLF endeavours within power systems characterized
by pronounced seasonal variations, such as load periods
with daily or weekly peaks, they are not without limitations.
Analogous to ARIMA constructs, SARIMA configurations
are predicated on a stationary sequence and demonstrate
deficiencies in comprehensively delineating the nonlinear
interdependencies between load dynamics and various con-
tributory elements [30]. Additionally, the model demands an

111862

VOLUME 12, 2024

---

<!-- PAGE 6 -->

K. Ullah et al.: STLF: A Comprehensive Review and Simulation Study

extensive corpus of historical data to accurately ascertain
seasonal parameters, which could pose difficulties for nascent
power system infrastructures. The schematic representation
of SARIMA models is illustrated in Figure 4.

These models are delineated by three core parame-
ters: ℘, ∂,
governing the non-seasonal facets, alongside
P, D, Q, which dictate the seasonal components. This
schema ℘ is allocated to represent the autoregressive order, ∂
is employed to specify the extent of differencing, and is uti-
lized to define the moving average order for the non-seasonal
segment. Similarly, within the SARIMA architecture, the
parameters P, D, and Q correspond to the order of autore-
gression, the degree of differencing, and the order of the
moving average, respectively, each tailored to address the sea-
sonal nuances of the model. The process of fitting a SARIMA
model encompasses a series of methodical steps. Initially,
model parameters undergo maximum likelihood estimation,
a sophisticated statistical method aimed at discerning the
most appropriate values for ℘, ∂, P, D, Q that optimize the
possibility of the perceived dataset [49]. After parameter esti-
mation, the model is fitted to the dataset utilizing advanced
forecasting techniques.

FIGURE 4. SARIMA Model approach.

This tactical methodology leverages the model to fore-
cast future time intervals utilizing historical datasets. The
following are the formulas delineating the facets of the
SARIMA model, which include the Integrated (I), Seasonal
Moving Average (SMA), MA, Seasonal Integrated (SI), AR,
and Seasonal Autoregressive (SAR), alongside the composite
equation.

• Component for the Autoregressive (AR):

ϑ (B) Xt = c + (cid:57)(B)∈t

(6)
In expression (6), ϑ (B) is delineated as the autoregressive
operator, with B signifying the backshift operator. Here, Xt

denotes the sequential data at time t, whereas c encapsulates
a fixed coefficient. Additionally, (cid:57) (B) is delineated as the
moving average operator, while εt embodies the stochastic
error constituent.

• Component for the Differencing (I):

(1 − B) Xt = Y(t)
In this formulation, the notation (1 − B) characterizes the
differencing operator, while Y(t) denotes the time series that
has been transmuted via differencing.

(7)

• Component for MA

Xt = U + 1ζ ( − 1) . . . . . . + ϱζ ( − ϱ)
Within this schema, U designates the arithmetic mean of
i encapsulates the coefficients correlated

the series while
with the moving average (MA) component.

(8)

• Component for SAR

(cid:50) (B )Yt = ψ (B )εt
Within this delineation, (cid:50) (B ) is identified as the seasonal
autoregressive operator, whereas ψ (B ) characterizes the
seasonal moving average operator.

(9)

• Component for Seasonal differencing

(1 − B )DYt = Zt
where Zt denotes the seasonally differenced time series, the
seasonal differencing operator is represented by (1 − B )D.

(10)

• Component SMA

Yt = (cid:56)sεt (t − ) + . . . + Zt (cid:56)sQε(t − (cid:56)s)

(11)

where (cid:56)si are the coefficients for the seasonal moving aver-
age component.

Combining these elements, the equation for the SARIMA-

based model can be articulated as follows:

ϑ (B) ϑs

(cid:0)Bs(cid:1) (1 − B)D(1 − Bs)DXt = c+(cid:57)(B)(cid:57)s(Bs)εt
(12)

• ARIMA VS SARIMA MODEL
While comparing both models, it may be noted that,
in short-term load forecasts, both ARIMA and SARIMA
models have their own merits and demerits [31]. ARIMA
proves superior because it is far more economical with fewer
parameters, particularly when the load data is non-seasonal
or has minimal seasonality. It captures the relative change
over a period, trends, cycles, and even random fluctuation,
helping to give a very good forecast in stable and non-periodic
environments. On the set of its drawbacks, the main disad-
vantage can be considered an inability of ARIMA to model
seasonality, which can become an important problem while
considering such load patterns that demonstrate clear cyclical
fluctuations in the loading and demand during a day or a
week.

SARIMA is a little specialized, with several extra param-
eters, particularly for seasonality. Due to its ability to model

VOLUME 12, 2024

111863

---

<!-- PAGE 7 -->

TABLE 1. Comparison analysis of ARIMA and SARIMA models [31].

and factor in seasonal variations, SARIMA is highly appli-
cable in short-term load forecasting scenarios where load
data contains strong seasonality characteristics, such as peak
loading during certain hours or certain days. Since these
recurring seasonal variations can be modeled, SARIMA mod-
els are generally more accurate than ARIMA models in
similar cases. However, due to the complexity of SARIMA,
the parameters need to be tuned, and sufficient data should be
obtained to avoid overfitting.

3) MODELS WITH EXPONENTIAL SMOOTHING
Exponential Smoothing (ES) models are predictive algo-
rithms within the time series domain, utilizing exponentially
weighted averages of antecedent observations to project
forthcoming values. Adjustability within these models is
achieved by manipulating the smoothing constant, which
governs the weight allocations to historical data points.
ES models encompass a multitude of sophisticated variants,
such as Holt’s Linear Exponential Smoothing (Holt), Simple
Exponential Smoothing (SES), and Holt-Winters Seasonal
Exponential Smoothing (HW) [32]. SES models apply just
one index of smoothing, which helps attain load data based
on observations. Holt models include another coefficient, g,
that deals with the series’s linear trends. Whereas HW models
define the trend and contain the parameters that account for
seasonality, the approach used in the model is superior when
analyzing periodic fluctuations in the load data. These HW
models are especially suitable for STLF in systems character-
ized by consistent trends and definite seasonal patterns [33].
It can be used in real-time prediction and is not as computa-
tionally demanding as the ARIMA and SARIMA models; ES
models use a relatively small amount of historical data. They
can also capture nonlinear associations with load data and
other effects like weather conditions and population density.
However, load data is assumed to remain stationary in the case
of ES models, implying that the accuracy of ES models when
it comes to non-stationary load in power system is affected.
The ES models’ operation process flow is depicted in
Fig. 5. The ES framework is characterized by two key param-
eters: alpha and beta. The first paper selected for the analysis
is the work of Fountain and colleagues, published in the
Journal of Midwifery & Women’s Health in 2018. The value
of the alpha parameter defines the primary importance of
the last value, while the beta parameter sets the importance
of the trend factor in the given model. The procedure for

K. Ullah et al.: STLF: A Comprehensive Review and Simulation Study

calibrating an ES model encompasses multiple stages. Ini-
tially, the baseline and trend estimates are derived from the
early observations in the time series. Subsequently, these esti-
mates are recurrently refined for each additional observation
by employing the equations outlined below:

L(t) = σ ×Y ( ) + (1 − σ ) × (L ( − 1) +I ( − 1))

(13)

T ( ) = β ( ) ×((L ( ) − L ( − 1)) + (1 − β) × I

(14)

Here, L ( ) captures the level of the data at a particular time
and translates the current status of the phenomenon under
study, whereas T( ) depicts the trend, describing the rate of
change of a certain occurrence.

FIGURE 5. ES model principal.

Therefore, once the level and trend estimates have stabi-
lized, it can forecast future periods with even more accurate
and precise ES models. The projection for the upcoming
period + 1 is derived by summing the current level and
trend components, as per the equation: The projection for the
upcoming period + 1 is derived by summing the current
level and trend components, as per the equation:

F ( + 1) = L ( ) + T ( )

(15)

4) MODELS FOR GENERALIZED LINEAR STRUCTURE
GLM is a large and systematic class of advanced statistical
techniques exploring the weak nonlinear relation between
load profile and influential factors. Various extensions of
GLMs exist, including the Poisson regression model, the
Negative Binomial regression model, the Gamma model,
and others [34]. GLMs extend the linear regression model
by providing the ability to manage the non-normal depen-
dency of the response. The benefits of GLMs are that they
can handle highly flexible load patterns due to the change
in load behaviour with meteorological parameters and/or
occupancy patterns based on the link function. This func-
tion provides an estimated value of the dependent variable
as E(y) = f (X1, X2, . . . . . . . . . . . . Xk from the predictor
variables X1, X2, . . . . . . . . . . . . Xk [35]. Likewise, in STLF,
the primary focus of most GM applications is the Poisson
regression model, the most common type of GLM, where the
load count is the dependent variable to the relevant control

111864

VOLUME 12, 2024

---

<!-- PAGE 8 -->

K. Ullah et al.: STLF: A Comprehensive Review and Simulation Study

variables. The Poisson regression model presupposes that the
described response variable is Poisson distributed and maps
the mean of this variable through a logarithmic link function
to the set of predictors. Indeed, the Poisson regression is
particularly adapted to power systems that involve counting
data, which means the number of working or existing appli-
ances or devices. In its own right, one must acknowledge the
function that PCA serves as a powerful tool for capturing
complex nonlinear relationships between loads’ variability
and a range of potential drivers [36]. The Poisson regression
model, employing a log-linear framework, formulates the
relationship between the predictor variables λ and the antic-
ipated count X. This relationship can be expressed as The
Poisson regression model, employing a log-linear framework,
formulates the relationship between the predictor variables
λ and the anticipated count X. This relationship can be
described as:

Logξ = α0 + α1X1
(16)
In this context, α0 refers to the intercept, whereas α_1
refers to the coefficient estimate for X1. Another advanced
GLM that is employed in STLF is the Negative Binomial
Regression model, which follows the formula: Derived from
Poisson regression models, it is most appropriate in working
with over-dispersed count data by including a prevalence
parameter by thus improving preciseness and reliability in
conditions of high data variability. This is because the vari-
ance of the response variable is generally more than its mean
and is quite common for load datasets considering power
systems due to high variability [37]. The logarithmic link
function used in the negative binomial regression model is an
advanced statistical method useful in accurately measuring
the complex relationship of the response variable with the
predictor variables in case the expected value of the response
cannot be assumed to be a linear function of the predictor
variables. This relationship is explained proficiently in linear
algebra by describing the association between the predictors
and the outcome in terms of a linear combination, thereby
providing a rich appreciation of how each predictor con-
tributes to the prediction. The difference in this model lies
in including one more dispersion parameter to reduce the
density of the response variables. This parameter contributes
additional robustness to the method because it is inherently
possible to have variability within the datasets used in real-
world applications. Indeed, incorporating the third variable,
which accounts for dispersion, enhances the model’s capa-
bilities by ensuring that the model can capture fine details
of the data sets. The articulation of the dispersion model is
as follows: The articulation of the dispersion model is as
follows:

Log (ϕ) = α0 + α1X1
(17)
In this context, ϕ belongs to the mathematical expectation
of the response variable, mean, which is a primary measure
of the central tendency of any set of data. On the other hand,
the symbol α0 represent the model intercept representing the

response variable’s baseline level, whereby all the predictor
variables have been set to zero. Moreover, α1 refers to the
coefficient that corresponds to the predictor variable, which
is X1 in this case, hence showing the degree of its impact
on the mean of the response variable. Novelty is deemed the
dispersion parameter κ, which brings variability to the model.
It can either be made fixed so it only offers a fixed measure
of dispersion or can be estimated depending on the predic-
tor variables, which provides the possibility of changing in
response to changes in the data used to create the model.
When κ is modeled as a function of the predictors, it follows
a logarithmic equation: When κ is modeled as a function of
the predictors, it follows a logarithmic equation:

Log (κ) = ρ0 + ρ1 1
(18)
Here, ρ0 term provides the intercept for the dispersion
component whereby the value of ρ signifies the general basal
level of dispersion. At this stage, ρ1 represents the estimator
of 1 which shows its effect on the variability of the response
variable. Gamma regression is identified in detail as one of the
significant tools in the Generalized Linear Models category
specifically utilized in Short-Term Load Forecasting during
power systems. Since the response variable is an instance
of the gamma distribution, this regression method brilliantly
transforms continuous load data and the dependent variable
in terms of the predictor variable.

G (U) = η

(19)

In (19), it also defines a complex interaction between the
mean of the response variable U and the linear predictor η
via an appropriate link function G. The integration of the link
function with the linear predictor results in a comprehensive
equation that encapsulates the complex interplay between the
response variable and the predictor variables: The integration
of the link function with the linear predictor results in a com-
prehensive equation that encapsulates the complex interplay
between the response variable and the predictor variables:
G (U) = ρ0 + ρ1X1 + ρ2X2 + . . . + ρPXP

(20)

GLMs boast computational efficiency and the flexibility to
accommodate diverse predictor variables, encompassing both
categorical and interaction terms. Furthermore, GLMs fur-
nish interpretable coefficients, facilitating the identification
of pivotal predictor variables and quantifying their impact on
the load [38]. However, a significant drawback of GLMs lies
in their assumption regarding the distribution of the response
variable, which may not universally apply to power system
contexts [39]. Additionally, the accurate estimation of model
parameters via GLMs often necessitates a substantial volume
of historical data, presenting challenges for newly established
power system installations with limited data availability [40].

B. MODELS WITH INTELLIGENT TECHNIQUES
Sophisticated methodologies in STLF encompass a range of
prognosticative techniques that employ cutting-edge compu-
tational strategies, including artificial intelligence, machine

VOLUME 12, 2024

111865

---

<!-- PAGE 9 -->

learning, and various optimization algorithms, to anticipate
near-future electrical demands. These advanced models are
intricately designed to discern and interpret complex patterns,
nonlinear interdependencies, and multifaceted relationships
within the load data, thereby enhancing the precision and
dependability of forecasts [41]. Figure 1 delineates several
prominent intelligent models employed in STLF, which have
been discussed in detail.

1) METHODS WITH SUPPORT VECTOR MACHINE
APPROACH
A critical machine learning archetype for STLF is the Support
Vector Machine (SVM), an advanced supervised learning
in addressing linear and nonlinear
framework proficient
associations between the electrical load and its influencing
determinants. SVMs are remarkably versatile in handling
an extensive spectrum of predictor variables, which include
categorical variables and interaction terms [42]. Furthermore,
these models are adept at mitigating issues related to noisy
data by applying a kernel function that transposes the data
into a higher-dimensional realm for enhanced analysis. SVMs
have been widely employed in predicting load dependent on
the/power system variables like temperature, humidity, and
time. In the context of the domain STLF, it is unobtrusively
incorporated to predict the future load or demand on elec-
tricity for up to one week. However, other intervals, such
as a few hours, can also be used. In general, an SVM aims
to find the best hyperplane that offers the maximum likely
separation of two classes of regression data sets. In the two-
dimensional case, it appears as a hyperplane, which in this
context represents a line that separates the data distinctly
into two separate categories. In ad-dimensional geometries,
a hyperplane is a sub-space born of the containment space
and is reduced by one dimension. A margin represents the dis-
tance between the hyperplane and the neighbours of distant
classes of points referred to as support vectors. These vectors
are essential in the structure and position of the hyperplane
as they provide its support. The fundamental objective of
an SVM revolves around optimizing this margin to ensure
the precise categorization of data elements. Within a dataset
containing labelled data pairs ( i,
i) where i represents a
vector in n-dimensional real space Rn and i designates the
binary class labels (−1, 1), the delineation of the hyperplane
is established mathematically [43].

. + = 0

(21)

In this context,

signifies the vector of coefficients,

encapsulates the vector of input features, and
as the intercept. The scalar product
of the projection of
is to determine the most advantageous values for
that effectively maximize the separation, or margin, between
the two categorically distinct classes. The discriminative cri-
terion for categorization is

is identified
. calculates the extent
. The task
and

in the direction oriented by

( ) = sign(

. + )

(22)

K. Ullah et al.: STLF: A Comprehensive Review and Simulation Study

where sign represents the signum function, which assigns the
class label according to the sign of its argument. The margin
for each data point is determined in the following manner:

Yi(

.

i + )

(23)

.

i about the vector

where, In the world of binary-defined classes Yi represents
the ith data point’s classification, often as −1 or +1. In turn,
denotes the weight vector that is orthogonal to the defining
i refers to features for the ith data sam-
hyperplane, whereas
ple. Moreover,
i the bias term is the important function that
shifts the delineating boundary from the origin. The notation
i represents the dot product between the network weight
i, which is a representation
vector w and the feature vector
. In the context
of the projection of
of the SVM paradigm, the fundamental aim, therefore, is to
understand how to obtain the biggest margin and, at the same
time, ensure all pattern vectors are classified correctly. This
optimization is made by controlling the size of the weight
vector, which is represented as |
|, where it is known that
the distance between the hyperplane and the data point is
inversely proportional to |
|. Building on this concept, the
SVM is meant to look for the perfect hyperplane that not only
partitions the data points according to their classes but also
does it with the largest margin, measured as the distance of
this hyperplane from the nearest data point of any of the class.
Thus, by minimizing |
|, the classifying hyperplane of the
SVM increases the said margin, and this, in turn, improves
the overall performance of the model in terms of its ability
to generalize. This process makes it possible for the SVM to
fulfil the optimal condition of maximizing the margin while
minimizing the classification errors and, hence, arriving at an
efficient and accurate classification system.

M =

1

|

|

(24)

The optimization conundrum for an SVM can be articu-

lated as a constrained optimization quandary.

× |

|2

(25)

1
2
Subject to the condition: Yi (

Min =

.

i + ) ≥1 for each i from
1 to . This situation leads to a convex quadratic programming
problem with linear constraints imposed on it. This task is
a challenge that is solved with the help of finding extrema
by using Lagrange multipliers, which thus leads to what is
called the dual problem. The dual formulation presents a more
practically applicable approach to deal with the problem of
optimization integrated in SVM, particularly in cases where
kernel functions are introduced in nonlinear situations [44].
The steps involved in STLF are as follows, and a flow diagram
is given in Figure 6.

• The first step is to collect past load demand data on
electricity, other systemic parameters, external environmental
conditions, and days of the week and time. It is then followed
by a cleanse and preprocess step to eliminate or minimize
any inconsistencies, noise, or missing values in the data. This

111866

VOLUME 12, 2024

---

<!-- PAGE 10 -->

K. Ullah et al.: STLF: A Comprehensive Review and Simulation Study

FIGURE 6. Machine system based on support vector mechanism.

is usually done through the normalization of standardization
methods to enhance the performance and quality of the SVM.
• In the next step, the attributes relevant to the forecasting
enterprise are identified for further assessment solely. This
stage is paramount, particularly if unnecessary functions neg-
atively affect the model’s performance. Also, there are RFE,
correlation reviews, or PCA to identify the features of the
problem that would be optimal to focus on.

• To elaborate further, the selected model of SVM is care-
fully trained on the refined data and the chosen variables only.
SVMs aim to obtain the best hyperplane that distinguishes
the studied data sets into distinct categories or classes. The
model is given for predicting continuous values to be the
electrical load, given that STLF is naturally a regression
problem. It should be understood that these kernel functions
are designed to map the input data to a space of higher dimen-
sionality. It helps when finding an appropriate hyperplane
in this expanded space of slowly growing dimensionality to
separate the points.

• The SVM model is initially trained using preprocessed
data, as discussed in Section III, and the most appropriate
attributes are selected. SVMs, as a technology, aim to classify
the data as aptly as possible into well-defined classes or
categories. For example, while STLF is a regression problem,
the model is set to forecast the continuous values for electrical
load. To achieve this, the SVM employs what is known as
kernels (which could be linear, polynomial, or the radial basis
kernel function,) which transforms the input data into the
higher dimensional space, making it easier to identify a plane
of best fit that separates the classes.

• To ensure everyone knows that the SVM model devel-
oped to solve different problems performs well, it is tested
using measures like cross-validation. Splitting the data into
the training and the validation set is performed in this process,
and the former Mode is trained while the latter mode is tested.
This helps to determine the model’s performance apart from
the test dataset and check for the model’s ability to perform
well across the other dataset.

• Moreover, the present enhancements include the cost
factor, the type of kernel function to be utilized, and the
parameters associated with the kernels that are incorporated
in the best estimation for solving the specific STLF challenge.
• Once a particular model, such as the SVM model, has
been trained and calibrated, its performance in terms of

prediction can then be evaluated on another data set that
was not used during the training. An examiner can assess
the model based on factors like standard error, R square,
coefficient of determination, and accuracy using MAE, MSE,
or MAPE.

• It is worth mentioning that, with new input data, the
proposed SVM model that is trained, validated, and tested can
provide a five-minute STLF. The developed model calculates
the required attributes for the forecast period and gives the
expected demand for electricity load.

2) DECISION TREE
Another suitable approach in business for the STLF is the
Decision Tree (DT), a statistical model specializing in seg-
menting predictor variables into categorical or continuous
categories, as shown in Fig. 7. DTs function by dividing the
predictor variables into subsets known as the leaf node. The
trees are connected based on load patterns within the load
prediction or mere hierarchy [45]. Decision trees have also
demonstrated favorable performance in power system-related
studies, especially in forecasting load variations from weather
characteristics, occupancy ratios, and time factors. Therefore,
divisions, lame, and splitting standards are at the heart of the
decision tree [46], [47].

Regarding classification tasks, data binning through met-
rics such as the Gini index or information gain is used, making
it easy to classify the different classes within the dataset.

• Gini Impurity: This metric assesses the heterogeneity of
a node (mix of classes), where lower figures indicate a higher
degree of uniformity. The Gini impurity for a node expressed
through class probabilities

, is formulated as:

G.I = 1 − X

(π )2

(26)

• Information Gain: Predicated on the concept of entropy,
which evaluates the degree of disorder or indeterminacy
within a group, Information Gain is computed for a node with
class probabilities π as

Ent = − X

( × log 2)(π)

(27)

Information gain (IG) is the entropy difference before and

after the data elements or nodes split.

IG = Entropy(parent)− weighted sum(Entropy(children))
(28)

To increase the information sought to facilitate the for-
mation of equally proportioned descendant nodes, the most
frequent technique used in regression efforts IX is using
Mean Squared Error (MSE) to split. MSE is expressed as the
mean of the squared difference between actual and estimated
targets; it serves as a key criterion underlying each partition’s
goal to minimize error. To train the decision tree model for
predictive analysis, it is crucial to correctly obtain previous
electricity load data and other independent variables like
weather parameters, day and month of the week, and time,
and address any anomalies or missing values. Pre-processing

VOLUME 12, 2024

111867

---

<!-- PAGE 11 -->

K. Ullah et al.: STLF: A Comprehensive Review and Simulation Study

for its capability to refine the precision of load forecasts.
The method systematically incorporates successive decision
trees, each tasked with rectifying the errors identified in its
predecessors, thereby constructing a comprehensive model
capable of capturing the intricate nonlinear dependencies
between the load and its influencing variables [49].

FIGURE 7. Block decision tree diagram.

techniques such as selection by using RFE, correlation anal-
ysis, or Information gain help remove attribute features that
may distort the classification result. The splitting is done
stepwise in the process of modeling, where the data is divided
into segments to minimize impurity, as measured by MSE,
until the model reaches the predetermined condition for ter-
minating the process of building a tree, such as the maximum
depth of the tree being achieved. Due to the nature of the
overfitting of decision trees, indicators for validation and
pruning, like cross-validation or cost complexity, are used
to enhance the stability and performance of the tree. After
extensive training and subsequent pruning, the final model
goes through specific performance evaluation metrics such
as MAE, MSE, or MAPE. Once the decision tree model is
validated, the process of short-term load forecasting begins
by transforming the input data into valid decision-making
criteria and passing it through the tree structure, moving from
the root of the tree to a node or leaf point at the end of a
decision path, which is the forecasted electricity load.

3) RANDOM FOREST AND GRADIENT BOOSTING (GB)
Random Forest (RF) is a refined version of DT developed
to reduce sensitivity to data noise and enhance accuracy in
load forecasting. RFs use the bootstrap aggregating method,
that is, many decision trees are built using bootstrap samples
of the training dataset for arriving at a final decision from
all these individual trees, and outputs from all the trees are
averaged to arrive at the final prediction. This technique is
used in certain power system paradigms to forecast load
changes due to specific factors like temperature, humidity,
and sunlight [48]. The simplified working model of an RF
algorithm is depicted below in Figure 8: In each tree node,
for a given dataset, ‘m’ number of features are randomly
selected from the total features. Many trees are then re-
grew, leading to different predictive classifications coming
from each of them. The last prediction is the overall con-
sensus, either a simple average or the decision from most
of the above-mentioned classification types [48]. GB is a
sophisticated ensemble machine learning paradigm known

FIGURE 8. Random forest algorithm.

Figure 9 illustrates the gradient boosting algorithm pro-
cess, which leverages training data to pinpoint weak learners,
enhancing the accuracy of subsequent predictions. The
sequential operation of the random forest and gradient boost-
ing algorithms is delineated as follows [50].

• The initial phase aggregates a load of power data along-
side variables such as meteorological data, the day of the
week, and the diurnal cycle. This collected data undergoes
cleansing and preprocessing to eliminate inconsistencies,
anomalies, or absent values. Notably, feature scaling is typi-
cally superfluous for random forests since the decision trees,
which serve as their foundational learners, exhibit a reduced
sensitivity to the magnitude of input features.

• The procedural execution of random forest and gradient
boosting algorithms proceeds as follows: The most perti-
nent attributes for the forecasting endeavor are meticulously
selected to preclude the detrimental effects of extrane-
ous or superfluous features on the model. While random
forests intrinsically possess the capacity to manage many
features and autonomously evaluate their significance, apply-
ing domain expertise or methodologies such as RFE and
correlation analysis can substantially enhance the model’s
performance.

• The model is trained after feature selection for the best
performing random forest model. This algorithm builds many
decision trees from a bootstrap sample in the presented data
set. Specifically, an independent random sample of features is
selected at the split stage of tree construction. It helps increase
the tree number intended to improve a model’s accuracy and
also helps avoid overfitting problems in the gradient-boosting
model.

• This confirms that the random forest model is reliable
in its performance with contemporary datasets due to the
application of the cross-validation technique. The dataset is
split into the train and validation sets, wherein the entire

111868

VOLUME 12, 2024

---

<!-- PAGE 12 -->

K. Ullah et al.: STLF: A Comprehensive Review and Simulation Study

FIGURE 9. Gradient boosting algorithmic diagram.

computation process is performed on the first subset, and the
results are tested on the second one. This methodology allows
evaluation of the model’s performance and generalization
ability on a different dataset.

• The random forest algorithm contains various tunable
hyper parameters. One can identify the number of trees within
the forest, the specified maximum depth of each tree, and
the minimum sample size of a node. These hyper parameters
can be tuned and fine-tuned through such techniques as grid
search, random search, [and] k-fold cross-validation to arrive
at the best setup relative to a given STLF task.

• Once the random forest model is thoroughly developed
and refined, it can accomplish STLF chap accordingly to the
newly supplied input data. For the particular given forecasting
time, the model takes the relevant characteristics and fore-
casts based on each tree in the decision tree. The last forecast
is then calculated as the average of all these results to produce
a more accurate and less volatile forecast.

4) MULTILAYER PERCEPTRON (MLP) MODEL
An MLP is an extended artificial neural network comprising
several linked stages, also known as layers of neurons or per-
ceptron layers. Figure 10 shows the architecture of an MLP;
the following are the main components of this nerve [51].

FIGURE 10. Multilayer perceptron model.

• Primary Interface: This MLP architecture’s first module
involves ingesting the first data received at the platform,

acceptability in various forms, including numeracy, imagery,
or text. Each node here stands for a specific attribute of the
input data.

• Intermediary Layers: Sitting between the input and
output parts, these layers incorporate neurons required for
translating the complexities into the acceptable format of the
system. The architecture of these layers determines the depth
of the model and the number of neurons within them, which
dictates the ability of the model to understand more complex
patterns.

• Terminal Section: This final component of the MLP
framework provides the last outcomes and or predictions of
the analysis. The use of nodes depends on the type of task to
be solved and whether to classify images into ten categories,
as it is assumed to have ten nodes.

• Neuronal Units: Every node in this computational archi-
tecture takes in input from the earlier layer of nodes, applies
a transform on this input, and then passes on the transformed
input to the next layer of nodes. Fortunately, containing a
non-linear activation function enables these networks to func-
tion and model complicated data configurations.

• Synaptic Weights and Biases: connectivity strength is
measured in weights, which control the inputs from one neu-
ron to another. These weights are fine-tuned iteratively in the
training phase to minimize the difference between predicted
outputs and actual input data.

• Model Calibration: These connected neural structures are
calibrated using a complicated procedure known as backprop-
agation. This method operates by systematically adjusting
weights and biases to reduce the gap between computed
results and reality. The basic idea with Calibration is that the
algorithm works continuously on a data set until it achieves
better and more accurate network prediction.

• Performance Metric: The network evaluation is based on
a loss metric, gauging the model’s efficiency. The general
structure of this kind of graphic is such that lower values
mean better accuracy and effectiveness. The principle during
calibration is to reduce this performance measure as much as
possible since it jeopardizes the network’s capabilities.

Mathematically, the output of a neuron can be represented

as [52]:

I = X

(W × + )

(29)

to the neuron

In the complex design of an MLP,

I is the quantity
we name the activation, which is the output of a neuron
I, is decided by an activation function . This function is
governed by the weighted sum of inputs, which is also a linear
summation of inputs, where W is a weight connecting the
input
.
Furthermore, the bias term
is introduced to each neuron,
enabling the model to be more flexible since the weights can
be adjusted with the additional input. To denote the above
relation in the MLP for each consequent stratum, the matrix
construct will make it possible to have computed right across
the network layer concurrently. This representation signif-
icantly improves activation calculations in many network

and is the value of the input

VOLUME 12, 2024

111869

---

<!-- PAGE 13 -->

K. Ullah et al.: STLF: A Comprehensive Review and Simulation Study

layers, thereby increasing the effectiveness of deeper learning
architectures.

A = X

(WX + B)

(30)

In this detailed description of an MLP, the matrix A rep-
resents the activation matrix in which a column contains the
activation information of a neuron to the input examples. The
matrix W represents the weight matrix and holds coefficients
that relate the inputs with the specific neurons to alter the
effect of every input feature in the neuron’s output. X can be
represented by the symbol, where each column of the matrix
comprises a specific input feature vector and contains the
input data that is directly supplied to the network. Finally,
B is the bias matrix integral to the network for adding a bias
term to each neuron’s weighted input, which assists in shifting
the activation function curve, thus offering another degree of
freedom for the learning algorithm. After the computation of
activations throughout all strata, the terminal stratum delivers
the ultimate forecast. In classification endeavours, a softmax
function is habitually deployed in the output stratum to trans-
figure the activations into probabilities:
ea
a
P e

Soft − Max(

(31)

) =

In this framework, s

denotes the activation for output
signifies the activation for output neuron , and
) is the probability associated with class.

neuron,
Soft − Max(

5) ENSEMBLE MODELS
Understanding the integration of machine learning archi-
tectures, the last category, ensemble models, integrates the
predictions of multiple models to create a single forecast. The
basic concept of ensemble modeling is to combine various
models, where each model has its unique characteristics and
strengths, and use their forecasted result together, which,
when developed, forms a clearer and more robust prediction.
These models have general applicability in most machine
learning processes, including classifications, regression, and
clustering [53]. Another benefit associated with the ensemble
models is the ability to minimize variance and reduce the
extent of overfitting. Variance, in ensemble models, refers to
the variation of the standard deviation of the outcomes of the
individual models within the ensemble. Overfitting is a model
learning problem that happens when excessive detail about
the training data is developed, and therefore, it is ineffective
in analyzing new data. This characteristic of ensemble models
provides a basis for ensuring their stability and increases their
applicability on various datasets. Ensemble models do a good
job of reducing variances and overfitting because they com-
bine the real estimations of the models, reducing the overall
variations that lead to a stronger prediction [54]. However,
there is one disadvantage regarding ensemble models: They
are highly complex. Each of these situated models is typically
less straightforward in their application and analysis than
isolated models and often requires higher computing power.

FIGURE 11. Types of the ensemble method.

However, the effectiveness of ensemble models cannot
be generalized and depends on the specific combination of
integrated models; identifying which configuration is most
effective may be difficult. The limitations present in ensemble
models include the fact that the accuracy of the models within
the ensemble directly impacts the ensemble models’ overall
accuracy and reliability of the forecast [55]. Substandard
models reduce the efficacy of ensemble models, whereby
a model may cross-spread problems such as overfitting or
under fitting the data. Selecting the models that would be
part of the ensemble should be done carefully; ensuring
they are all high-quality is important. The ensemble model
construction tactics include bagging, boosting, and stacking,
as shown in Figure 11. Both methods are suitable for handling
data and have specific strengths and weaknesses, and the
choice of a method depends on the features of the given
application and the dataset. Bagging, also known as bootstrap
aggregating, involves using many based models developed
on different samples of the base training set to create a final
forecast or solution, the weighted average of the individual
predictions/solutions. The fundamental idea of bagging lies
in constructing several replicas of the initial set, wherein each
replica will consist of a distinct yet somehow diverse part of
the set [56].

Further, models are trained on each of such executions,
and the outcomes are combined to generate the final fore-
cast. In this approach, bagging involves compiling the results
of all the models that have been developed to produce a
more accurate and reliable prediction. Boosting is the method
through which the training of models is set in a sequential
form such that each is responsible for correcting the mistakes
made by its predecessor. This technique increases prediction
accuracy – generally due to increased susceptibility to over-
fitting compared to the bagging method. According to the
principles of boosting, the process begins with a simple model
and continues with increasing levels of model complexity
added to solve the mistakes of the prior level [57]. These
models are then added with a weighted average, where the
weights have direct proportionality to accuracy, and errors are
gradually focused on previous models, enhancing attempts
towards higher accuracy and reliability of the forecast.

The process of hierarchical aggregation, frequently known
as stratified synthesis, implies that numerous models are

111870

VOLUME 12, 2024

---

<!-- PAGE 14 -->

K. Ullah et al.: STLF: A Comprehensive Review and Simulation Study

trained successively in the training dataset, and the calculated
outputs are used as inputs for the other, more complex mod-
els. The higher-level model further learns to accumulate the
outcome of the lower-level models to arrive at an outcome.
Despite these, the stacking model can enhance the accuracy
and reliability of the prediction compared to bagging or
boosting but may be harder to apply and analyze than the
two [58]. The higher-level model then learns to aggregate
the two lower-level predictions into one prediction. Stacking,
in general, is a way to obtain a more accurate and stable fore-
cast since, by using several models together, the result is an
ensemble that is usually more precise [59]. DL is an advanced
ML model classification that performs well when discovering
the intricate nonlinear relationship of load by other preceding
factors [60]. The DL frameworks have stacked layers of inter-
acting nodes that help convey information using weighted
connections [61]. As a significant point, it is possible to
emphasize that CNNs are one of the most used DL models for
STLF. These networks effectively capture load data based on
space and time characteristics. CNNs are very useful in power
systems, enabling the possibility of predicting changes in load
due to special factors such as weather, occupancy, and time
of day. The second key model for TLs specialized in STLF
is the RNN, as this type of network can quickly identify load
data’s temporal characteristics. Sequential Neural Networks
(SNNs) possess feedback connections and the ability to move
from one time point to the next, thus equipping the model to
quantify changes in the load over time. Altogether, compared
to all the correlated works on SNNs, the especially suitable
for this task is the LSTM network, as it is characterized by
a rather high ability to perceive short-time and long-time
temporal interdependences in the load data set [62].

C. HYBRID MODELS
As suggested by the title, they encompass both statistical
and machine learning methodologies that are integrated to
magnify the strengths of still. Among all the hybrids analyzed
in STLF studies, ARIMA–SVR and ES–ANN are the most
utilized models. The type of composite scheme employed
for this particular kind of investigation in this paper is the
ARIMA–SVR model, a conjunction of ARIMA and SVR
architecture for capturing temporal patterns in load demand
and non-linear associations with load demand [63], [64].
On the other hand, due to the integration of ES with ANN,
the ES – ANN design can note complexities like changes
in season and other non-linear demands in load. Accu-
rate and hardly interpretable models are achieved; hence,
the STLF models are improved for use in power systems
with the help of hybrid models. However,
they require
fewer statistical models and are more required than machine
learning algorithms, and they can have more problems imple-
menting than purely machine learning models [65]. These
biomechanical-fractured constructs, which support different
modeling methodologies for assimilation efficiently, have
been said to improve load forecast rates. Here are some

notable hybrid models: Some hybrids have a strong combi-
nation of the two types.

1) HYBRID MODEL WITH ARIMA–ANN APPROACH
Another conventional time series forecasting approach is
the ARIMA model, which serves as the basis for capturing
linearity in the data. On the other hand, ANNs can catego-
rize complex non-linear relationships. This compound model
fully integrates the linear skill of ARIMA for load data and
the nonlinear diagnosis capacity of ANNs by realizing lin-
ear forecasting of ARIMA & nonlinear diagnosis of ANNs.
Indeed, such a synthesis significantly improves the accuracy
of STLF [66].

2) HYBRID MODELS BASED ON WAVELET-TRANSFORM
One of the sophisticated analytical tools that allow for the
decomposition of a time series into several discrete frequency
bands is the wavelet coefficient. The resolution means that
the high-frequency section contains noise and other irregu-
larities, whereas the low-frequency section captures steady
variations. Since EMD can be combined with different pre-
dictive models like the ANN, SVM, or LSTM networks, this
technique can be effectively incorporated into developing
the hybrid forecasting model. What is more important is
that, through splitting the frequency components, this method
increases the accuracy of the forecasts by an average of sixty-
five percent [67].

3) HYBRID MODEL EEMD ANN APPROACH
The EEMD is a refined signal analysis that helps to recreate
a non-stationary time series through a set of IMFs. This
study further strengthens the proposed hybrid model by com-
bining ANEMD with ANN to handle non-stationary and
non-linear load data. In this process, EEMD filters the load
data to extract the IMFs. Finally, the ANN is trained with the
extracted IMFs identified in the previous section to build pre-
dictive forecasts. These individual forecasts are then summed
up to arrive at the STLF output [68].

4) HYBRID MODELS FUZZY LOGIC APPROACH
Fuzzy logic is a mathematical approach designed to han-
dle such uncertainties and impreciseness in data. It can be
easily extended with other predictive methods like ANN,
SVM, or regression functions. It can create a highly effective
combined model to solve the high uncertainty observed in
the load data. In this regard, fuzzy logic can filter the input
data, represent uncertainties in modeling the forecast unit,
or combine the outputs of distinct models to sharpen the
forecast accuracy [69].

5) HYBRID MODELS WITH DEEP-LEARNING APPROACH
Deep learning paradigms, including CNNs and long LSTMs,
have demonstrated high fitness in STLF due to their abil-
ity to uncover hierarchical and temporal informatics. These
enhanced learning frameworks can be incorporated with other

VOLUME 12, 2024

111871

---

<!-- PAGE 15 -->

predictive systems like statistical models, wavelet transform,
or fuzzy rules to form a blended model. Such integrative
models make the best out of the integrated methodologies
of STLF and significantly increase the accuracy level of the
models [63].

D. PERFORMANCE COMPARISON OF STLF MODELS
It is, therefore, safe to mention that several antecedent fac-
tors determine the effects of STLF models and the volume
and caliber of the variables involved. It is well established
that intelligent models often have superior predictive power
compared to models based solely on pure statistical con-
siderations, and models based on a blend of statistical and
intelligent framework components have been found to out-
perform both [70]. However, these models’ somewhat relative
performance depends on the specific application and the data
used. For instance, statistical models might produce good
outcome predictions of stationary and linear values if data is
limited in quantity.

On the other hand, intelligent models are known to perform
well under nonlinear and non-stationary datasets or environ-
ments, particularly if only a large number of datasets are
present. When these variables present linear and nonlinear
data patterns of relationship, and problems like noise or
missing data elements are there, hybrid models are more
beneficial. The following summarizes these observations,
as given in Table 2.

IV. CASE STUDY
A. PROPOSED MODEL
The proposed model architecture effectively integrates con-
volutional neural networks (CNNs) with long short-term
memory (LSTM) networks to process sequential data char-
acterized by 24-time steps and 17 features per time step. This
hybrid architecture leverages the strengths of both CNNs and
LSTMs, enabling the model to capture spatial and temporal
dependencies inherent in the data.

The model begins with an input layer that accommodates
sequences of the specified shape. The first processing block
consists of a 1D convolutional layer with 48 filters and a ker-
nel size 3. This convolutional layer is intended to extract local
features from the input sequences, capitalizing on the capa-
bility of convolutional operations to identify patterns such
as trends and periodicities. The output of this convolutional
layer is then passed through a ReLU activation function,
which introduces non-linearity into the model, enhancing its
capacity to capture complex relationships within the data.

Following the activation, the output is flattened, trans-
forming the multi-dimensional tensor into a 1D vector. This
flattened representation is subsequently processed by a dense
layer comprising 24 nodes. This dense layer aims to fur-
ther abstract and learn higher-level representations of the
features extracted by the convolutional layer. The second
convolutional block takes the output from the first activation
layer as input and applies another 1D convolutional layer

K. Ullah et al.: STLF: A Comprehensive Review and Simulation Study

TABLE 2. Different Model of STLF and their Pros and Cons.

with 32 filters and a kernel size 3. This layer continues the
process of feature extraction but at a finer granularity. The
activation, flattening, and dense layer operations are repeated
as in the first block, ensuring consistent transformation and
abstraction of features. The third convolutional block follows

111872

VOLUME 12, 2024

---

<!-- PAGE 16 -->

K. Ullah et al.: STLF: A Comprehensive Review and Simulation Study

a similar structure, utilizing a 1D convolutional layer with
16 filters and a kernel size 3. The progressively decreas-
ing number of filters in subsequent convolutional layers is
designed to reduce the dimensionality of the feature space
while retaining essential patterns. After the ReLU activation,
the output is flattened and passed through another dense layer
with 24 nodes.

ensure the net makes out the total series of hidden states.
Finally, the return sequence is false in the final LSTM layer:
It is worth noting that in the final LSTM layer, the network
gives only the hidden state (the last time step). Therefore,
another dropout layer was invoked before the output layer to
reduce cases of overlearning and high chances of overfitting.
The input or fully connected layer comprises 20 neurons
equivalent to 20 indexes of the irregular array used to cool
the neural network during the simulation. The neurons in the
output layers are from one to six to cover all the look-ahead
periods of 1 up to 3 h for load forecasting. The parameter
setting of the formulated deep learning framework in this
study is captured in Table 4.

TABLE 3. Various layer configuration of the proposed model.

FIGURE 12. Proposed Model of the Network.

Following the third activation layer, a dropout rate of
0.25 is applied to mitigate the risk of overfitting. This regu-
larization technique randomly sets a fraction of input units to
zero during training, promoting robustness and generalization
of the model. The model then transitions to a series of LSTM
layers, beginning with an LSTM layer containing 20 units
that return sequences. This layer is instrumental in capturing
the temporal dependencies within the data, leveraging the
LSTM’s ability to retain and utilize information from pre-
vious time steps. A second LSTM layer with 20 units and
returning sequences further processes the temporal informa-
tion. The third LSTM layer, with 20 units, returns only the last
output in the sequence, encapsulating the temporal dynamics
into a fixed-size vector. Following the LSTM layers, another
dropout layer with a dropout rate 0.25 is introduced to fur-
ther reduce overfitting. The output from this layer is then
concatenated with the outputs from the three dense layers
following each convolutional block. This concatenation oper-
ation effectively combines the spatial features extracted by
the CNN layers with the temporal features captured by the
LSTM layers, providing a comprehensive representation of
the input data. Finally, the concatenated features are passed
through a dense layer with 24 or 1 node and a tanh activation
function, producing the model’s final output for single-step
and multistep forecasting [79]. However, it has been modified
to enhance the performance. The parameter setting of the
formulated deep learning framework in this study is captured
in Table 3.

It also assists them in reducing the number of overfitting
and results in a smaller number of trainable parameters. Every
stack included a sequence learning block, where exactly three
LSTM layers were used, with 20 neurons per layer. The return
sequence is set as the true for the first two LSTM layers to

TABLE 4. Proposed model setting (Parameters).

To this end, the distinguished optimizer tagged ‘Adam’ was
deployed in this study due to its efficiency and supposedly
optimal responsiveness to fluctuating learning rate require-
ments. To evaluate the accuracy of the mean absolute error,
or MAE was utilized as the loss function by calculating the
absolute value of the difference between the target and pre-
dicted values for each data point, summing all these values,
and dividing the total by the overall number of values in a
dataset.

B. DATA PRE-PROCESSING
For optimal learning, data must be meticulously pre-processed
before model training. A well-prepared dataset enhances

VOLUME 12, 2024

111873

---

<!-- PAGE 17 -->

K. Ullah et al.: STLF: A Comprehensive Review and Simulation Study

FIGURE 13. Pre-processing diagram.

a model’s ability to identify trends and relationships. The
primary pre-processing steps include train-test splitting, data
cleaning, high-level feature extraction, and formatting the
data into a 3D structure (Samples, Time Steps, and Fea-
tures) suitable for model training. Figure 13 illustrates the
comprehensive pre-processing flowchart. Utilizing the afore-
mentioned model for pre-processing, the initial data was
acquired from the National Transmission and Dispatch Com-
pany (NTDC) in Islamabad. This data was initially scattered
across multiple files, which posed a challenge for effective
handling and analysis. These disparate files were meticu-
lously processed and merged to streamline the process into a
cohesive file, facilitating more efficient data management and
feature extraction. The comprehensive flowchart detailing the
entire pre-processing procedure is presented in Figure 13.

This dataset encompasses a time range from January 1,
2019, at 00:00 hours to May 31, 2023, at 23:00 hours, with
data recorded hourly by the National Power Control Center
(NPCC). Several manipulation techniques were applied to
ensure data privacy while preparing it for analysis. These
m anipulations were executed to preserve the overall con-
sumption patterns, introducing only minor adjustments to the

data. This approach was essential to maintain the integrity and
utility of the dataset for accurate feature extraction and sub-
sequent model training. A detailed description of the dataset,
including various attributes and corresponding values, is pro-
vided in Table 5.

TABLE 5. Dataset description.

This comprehensive description clearly explains the data’s
scope and characteristics, ensuring that all relevant infor-
mation is available for thorough analysis and model devel-
opment. Subsequently, the data was divided into training
and testing sets. The period from February 2023 to May
2023 was designated as the test data and extracted from the

111874

VOLUME 12, 2024

---

<!-- PAGE 18 -->

K. Ullah et al.: STLF: A Comprehensive Review and Simulation Study

FIGURE 14. Outliers before and after handling.

entire dataset. The remaining data, spanning from January
2019 to January 2023, was partitioned such that 70 percent
was utilized for training and 30 percent for validation.

During the analysis process, it was confirmed that there
was no missing data; however, outliers were detected within
the training dataset, as illustrated in Figure 14. These outliers
were identified and addressed to ensure the integrity of the
model training process. The analysis assumes no missing
data was in the dataset while outliers were identified, espe-
cially during off-peak hours. The figure presents the load
in megawatts (MW) by categories, including working days,
holidays, off-peak, and peak hours during the summer peak
period. The median load is slightly lower during holidays
than during working days, but a similar IQR follows this and
has no extreme points; therefore, the load is similar during
both working days and holidays. Contrarily, the load during
on-peak is much higher and more consolidated than off-peak,
with several low values and higher variability. This implies
a high and well-defined increase in energy demand during
the on-peak hours. Therefore, there is a need to establish a
better way of predicting the variations and stability during the
off-peak hours. They are important for energy management,
resource planning, and load forecast enhancement. Follow-
ing this, all potential features that could influence the load
consumption pattern were extracted, as depicted in the heat
map in Figure 15. Additionally, this study treated all national
holidays as weekend holidays to maintain consistency in the
data analysis.

The outliers were identified using the following equations:

Lower Outliers = Min × (Q1 − 1.5 × IQR)
Upper Outliers = Max× (Q3+1.5 × IQR)

(32)
(33)

The outliers were managed similarly to consecutive missing
values. Specifically, the data anomalies from 2021-01-02

22:00:00 to 2021-01-09 22:00:00 and from 2021-01-09
06:00:00 to 2021-01-16 06:00:00 were rectified by substi-
tuting them with the mean values computed over 24-hour
periods, grouped by each hour. Before and after this treat-
ment process, the comprehensive details of the outliers are
delineated in Table 6.

TABLE 6. Detail description of outliers.

Various factors influencing the load consumption pat-
tern were incorporated for feature extraction. These factors
included the hour of the day, the month, and the weekdays,
with their effects illustrated in Figures 16 and 17, respectively.
Additionally, Pakistani national holidays were encoded as
binary signals (0 for no holiday, 1 for a holiday), and week-
ends were included in the analysis.

The data was prepared for the deep learning network to
accommodate single-step and multistep inputs. Algorithms
for configuring single-step and multistep data sequences were
delineated in our previous work. Notably, 17 input features

VOLUME 12, 2024

111875

---

<!-- PAGE 19 -->

K. Ullah et al.: STLF: A Comprehensive Review and Simulation Study

FIGURE 15. Correlation of Feature with Load.

FIGURE 16. Categorical features.

were incorporated to train the CNN and LSTM models,
as illustrated in Table 7. Accordingly, the performance eval-
uation metrics are presented in Tables 8 and 9, respectively.

C. RESULTS AND DISCUSSION
Hourly load forecasting is an essential component of energy
management systems, ensuring the stability and efficiency of
power networks. Accurate forecasts enable utilities to allocate

resources and balance loads effectively, enhancing overall
system performance. Recently, there has been an increasing
interest in developing sophisticated forecasting models to
improve the precision of hour-ahead load predictions. The
actual power consumption and the predicted power from
the proposed model are illustrated in Figure 18 for hour-
ahead forecasting. This graph juxtaposes the actual load (in
megawatts) with the predicted load across various dates. The
x-axis denotes the dates from December 2020 to April 2021,

111876

VOLUME 12, 2024

---

<!-- PAGE 20 -->

K. Ullah et al.: STLF: A Comprehensive Review and Simulation Study

FIGURE 17. Cyclic features.

FIGURE 18. Actual and predicted load consumption.

while the y-axis measures the electrical load in megawatts
(MW). The black line represents the actual load, and the
predicted load is depicted in red. The graph indicates that
the predicted load closely mirrors the actual load, suggesting

that the prediction model has effectively captured the overall
trend and most fluctuations in the load data. Although the
prediction is conducted for the entire test dataset, only a
few days from the beginning are shown for better visibility.

VOLUME 12, 2024

111877

---

<!-- PAGE 21 -->

TABLE 7. Input features.

K. Ullah et al.: STLF: A Comprehensive Review and Simulation Study

The input features are presented in Table 7. In contrast, the
performance evaluation for the single step and 24 steps are
presented in Comparing the performance of the forecasting
models presented in [55] and [79], and the proposed model,
it is possible to note the increase in the performance indica-
tors of the proposed model for both single-step and 24-hour
forecasting. In the case of single-step forecasting, the dataset
of NTDC has demonstrated that the proposed model has a
value of RMSE equal to 538. 71, MAE of 371. 97, and MAPE
of 2. 72, outperforming [79]. Likewise, for the AEP dataset,
the RMSE of the proposed model is 126. 35, MAE of 94.
27, and MAPE of 0. 64 are substantially better than [79]
(RMSE: 372. 77, MAE: 295. 92, MAPE: 2. 05 and [55]
RMSE: 472. 13, MAE: 358. 6, MAPE: 2. 41. In 24-hour
forecasting, the proposed model also outperforms the other
models with NTDC values of RMSE 951. 94, MAE 656. 35,
and MAPE 4. 72, compared to [79] (RMSE: And in this case,
the proposed model has a lower RMSE (1038. 04) than [55]
(1166. 79), a lower MAE (773. 18) than [55] (843. 76), and
a lower MAPE (5. 35) than [55] (6. 16). In the case of the
AEP dataset, the RMSE of the proposed model is 702. 97,
MAE of 507. 97, and MAPE of 3. 39 also outperform [79].
In general, the proposed model outperforms the benchmark
models in terms of accuracy and reliability in one-step and
n-step ahead forecasting.

TABLE 8. Performance evaluation matrix for single-step.

TABLE 9. Performance evaluation matrix for 24 hours.

Likewise, how they compare is shown in Figure 19. It can
be confirmed that the values of the proposed model’s pre-
dictions (red line) are closer to the actual load values (black

FIGURE 19. Comparison with the reference model.

line) than the values of predictions defined by the reference
method (blue line). The data utilized in this case was NTDC,
which serves as the study’s baseline. This shows that the
adopted model has given a better, more accurate load forecast
in MWatt over the stipulated period. The reference method
has high variability to the actual values, as evidenced by
Fig. 19, which explains this method’s fairly poor predictive
power.

V. CONCLUSION
Short-term load forecasting (STLF) is crucial in large-scale
power grids, enabling grid operators to accurately fore-
cast load and efficiently utilize operating reserves. This
paper explains the latest STLF techniques, including sta-
tistical models such as autoregressive integrated moving
averages (ARIMA), seasonal ARIMA (SARIMA), expo-
nential smoothing, and generalized linear models. It also
includes smart techniques such as Support vector machine
(SVM), decision tree, random forest, gradient boosting, MLP,
ENSEMBLE, and hybrid models. These methods are then
assessed in the paper through mathematical and graphical
analysis, and their advantages and drawbacks are discussed
to assist with their proper implementation in present day
power systems. Further, the paper has proposed a hybrid
CNN-LSTM model for STLF, which combines Convolu-
tional Neural Networks (CNNs) for feature extraction and
Long Short-Term Memory networks (LSTMs) for sequence
forecasting and uses textual data from the NTDC Pakistan
national power grid. The results of the comparative analysis
with the previous models using the AEP dataset prove that
the proposed hybrid model has higher accuracy in single-step
and 24-hour forecasts, thus improving the forecast quality and
generalizing the model’s performance for various forecast
horizons.

In the future, this study can be extended to probabilistic
load forecasting to improve the stability and accuracy of
the forecast. Probabilistic forecasting measures the degree

111878

VOLUME 12, 2024

---

<!-- PAGE 22 -->

K. Ullah et al.: STLF: A Comprehensive Review and Simulation Study

of uncertainty by providing the range of possible and fore-
casted values, which is crucial in risk management and
decision-making in power systems. This includes incor-
porating techniques like quantile regression, Monte Carlo
simulation, and Bayesian analysis. These approaches would
give more context-aware information about expected devi-
ations or risks in load forecasts, enhancing the accuracy of
the forecasts and the decision-making process in power grid
management.

REFERENCES

[1] L. Cheng and T. Yu, ‘‘A new generation of AI: A review and perspective on
machine learning technologies applied to smart energy and electric power
systems,’’ Int. J. Energy Res., vol. 43, no. 6, pp. 1928–1973, May 2019.
[2] Y. Ding, Y. Zhu, J. Feng, P. Zhang, and Z. Cheng, ‘‘Interpretable spatio-
temporal attention LSTM model for flood forecasting,’’ Neurocomputing,
vol. 403, pp. 348–359, Aug. 2020.

[3] H. Fu, J.-C. Baltazar, and D. E. Claridge, ‘‘Review of developments
in whole-building statistical energy consumption models for commer-
cial buildings,’’ Renew. Sustain. Energy Rev., vol. 147, Sep. 2021,
Art. no. 111248.

[4] S. Lu, Q. Li, L. Bai, and R. Wang, ‘‘Performance predictions of ground
source heat pump system based on random forest and back propagation
neural network models,’’ Energy Convers. Manage., vol. 197, Oct. 2019,
Art. no. 111864.

[5] M. A. Ganaie, M. Hu, A. K. Malik, M. Tanveer, and P. N. Suganthan,
‘‘Ensemble deep learning: A review,’’ Eng. Appl. Artif. Intell., vol. 115,
Oct. 2022, Art. no. 105151.

[6] A. Altan, S. Karasu, and E. Zio, ‘‘A new hybrid model for wind speed
forecasting combining long short-term memory neural network, decom-
position methods and grey wolf optimizer,’’ Appl. Soft Comput., vol. 100,
Mar. 2021, Art. no. 106996.

[7] M. Alexander and H. Beushausen, ‘‘Durability, service life prediction,
and modelling for reinforced concrete structures—Review and critique,’’
Cement Concrete Res., vol. 122, pp. 17–29, Aug. 2019.

[8] A. Kurani, P. Doshi, A. Vakharia, and M. Shah, ‘‘A comprehensive compar-
ative study of artificial neural network (ANN) and support vector machines
(SVM) on stock forecasting,’’ Ann. Data Sci., vol. 10, no. 1, pp. 183–208,
Feb. 2023.

[9] A. S. Dagoumas and N. E. Koltsaklis, ‘‘Review of models for integrating
renewable energy in the generation expansion planning,’’ Appl. Energy,
vol. 242, pp. 1573–1587, May 2019.

[10] L.-L. Li, X. Zhao, M.-L. Tseng, and R. R. Tan, ‘‘Short-term wind power
forecasting based on support vector machine with improved dragonfly
algorithm,’’ J. Cleaner Prod., vol. 242, Jan. 2020, Art. no. 118447.
[11] J. Chen and X. Ran, ‘‘Deep learning with edge computing: A review,’’ Proc.

IEEE, vol. 107, no. 8, pp. 1655–1674, Aug. 2019.

[12] A. Ruano, A. Hernandez, J. Ureña, M. Ruano, and J. Garcia, ‘‘NILM
techniques for intelligent home energy management and ambient assisted
living: A review,’’ Energies, vol. 12, no. 11, p. 2203, Jun. 2019.

[13] S. M. Hasanat, R. Younis, S. Alahmari, M. T. Ejaz, M. Haris, H. Yousaf,
S. Watara, K. Ullah, and Z. Ullah, ‘‘Enhancing load forecasting accuracy
in smart grids: A novel parallel multichannel network approach using
1D CNN and Bi-LSTM models,’’ Int. J. Energy Res., vol. 2024, no. 1,
Jan. 2024, Art. no. 2403847.

[14] M. Sharifzadeh, A. Sikinioti-Lock, and N. Shah, ‘‘Machine-learning meth-
ods for integrated renewable power generation: A comparative study of
artificial neural networks, support vector regression, and Gaussian process
regression,’’ Renew. Sustain. Energy Rev., vol. 108, pp. 513–538, Jul. 2019.
[15] H. Liu, C. Chen, X. Lv, X. Wu, and M. Liu, ‘‘Deterministic wind energy
forecasting: A review of intelligent predictors and auxiliary methods,’’
Energy Convers. Manage., vol. 195, pp. 328–345, Sep. 2019.

[16] A. Nespoli, E. Ogliari, S. Leva, A. Massi Pavan, A. Mellit, V. Lughi, and
A. Dolara, ‘‘Day-ahead photovoltaic forecasting: A comparison of the most
effective techniques,’’ Energies, vol. 12, no. 9, p. 1621, Apr. 2019.
[17] M. Mahzarnia, M. P. Moghaddam, P. T. Baboli, and P. Siano, ‘‘A review of
the measures to enhance power systems resilience,’’ IEEE Syst. J., vol. 14,
no. 3, pp. 4059–4070, Sep. 2020.

[18] Z. Liu, P. Jiang, L. Zhang, and X. Niu, ‘‘A combined forecasting model
for time series: Application to short-term wind speed forecasting,’’ Appl.
Energy, vol. 259, Feb. 2020, Art. no. 114137.

[19] C. Fan, J. Wang, W. Gang, and S. Li, ‘‘Assessment of deep recurrent neu-
ral network-based strategies for short-term building energy predictions,’’
Appl. Energy, vol. 236, pp. 700–710, Feb. 2019.

[20] E. Hossain, I. Khan, F. Un-Noor, S. S. Sikander, and M. S. H. Sunny,
‘‘Application of big data and machine learning in smart grid, and
IEEE Access, vol. 7,
associated security concerns: A review,’’
pp. 13960–13988, 2019.

[21] Y. Eren and I. Küçükdemiral, ‘‘A comprehensive review on deep learning
approaches for short-term load forecasting,’’ Renew. Sustain. Energy Rev.,
vol. 189, Jan. 2024, Art. no. 114031.

[22] H. Hassani and E. S. Silva, ‘‘Predictions from generative artificial intel-
ligence models: Towards a new benchmark in forecasting practice,’’
Information, vol. 15, no. 6, p. 291, May 2024.

[23] M. H. Sulaiman and Z. Mustaffa, ‘‘Chiller energy prediction in commer-
cial building: A metaheuristic-enhanced deep learning approach,’’ Energy,
vol. 297, Jun. 2024, Art. no. 131159.

[24] D. Hou and R. Evins, ‘‘A protocol for developing and evaluating
neural network-based surrogate models and its application to building
energy prediction,’’ Renew. Sustain. Energy Rev., vol. 193, Apr. 2024,
Art. no. 114283.

[25] K. Wang, X. Qi, and H. Liu, ‘‘Photovoltaic power forecasting based LSTM-

convolutional network,’’ Energy, vol. 189, Dec. 2019, Art. no. 116225.

[26] S. Du, T. Li, Y. Yang, and S.-J. Horng, ‘‘Multivariate time series forecast-
ing via attention-based encoder–decoder framework,’’ Neurocomputing,
vol. 388, pp. 269–279, May 2020.

[27] A. Mosavi, M. Salimi, S. F. Ardabili, T. Rabczuk, S. Shamshirband, and
A. R. Varkonyi-Koczy, ‘‘State of the art of machine learning models in
energy systems, a systematic review,’’ Energies, vol. 12, no. 7, p. 1301,
Apr. 2019.

[28] M. Cai, M. Pipattanasomporn, and S. Rahman, ‘‘Day-ahead building-level
load forecasts using deep learning vs. traditional time-series techniques,’’
Appl. Energy, vol. 236, pp. 1078–1088, Feb. 2019.

[29] S. Sobri, S. Koohi-Kamali, and N. A. Rahim, ‘‘Solar photovoltaic genera-
tion forecasting methods: A review,’’ Energy Convers. Manage., vol. 156,
pp. 459–497, Jan. 2018.

[30] R. Ahmed, V. Sreeram, Y. Mishra, and M. D. Arif, ‘‘A review and eval-
uation of the state-of-the-art in PV solar power forecasting: Techniques
and optimization,’’ Renew. Sustain. Energy Rev., vol. 124, May 2020,
Art. no. 109792.

[31] C. Tarmanini, N. Sarma, C. Gezegin, and O. Ozgonenel, ‘‘Short term load
forecasting based on ARIMA and ANN approaches,’’ Energy Rep., vol. 9,
pp. 550–557, May 2023.

[32] N. Kalchbrenner, I. Danihelka, and A. Graves, ‘‘Grid long short-term

memory,’’ 2015, arXiv:1507.01526.

[33] K. T. Ponds, A. Arefi, A. Sayigh, and G. Ledwich, ‘‘Aggregator of demand
response for renewable integration and customer engagement: Strengths,
weaknesses, opportunities, and threats,’’ Energies, vol. 11, no. 9, p. 2391,
Sep. 2018.

[34] G. Fan, Y. Guo, J. Zheng, and W. Hong, ‘‘A generalized regression
model based on hybrid empirical mode decomposition and support vector
regression with back-propagation neural network for mid-short-term load
forecasting,’’ J. Forecasting, vol. 39, no. 5, pp. 737–756, Aug. 2020.
[35] A. S. Nair, P. Ranganathan, C. Finley, and N. Kaabouch, ‘‘Short-term
forecast analysis on wind power generation data,’’ in Proc. IEEE Kansas
Power Energy Conf. (KPEC), Apr. 2021, pp. 1–6.

[36] L. Shang, K. Chen, G. Wang, Y. Liu, R. Hu, and Y. Shang, ‘‘Short-term
distribution network peak load forecasting based on generalized linear
model,’’ in Proc. 4th Int. Conf. Power Energy Technol. (ICPET), Jul. 2022,
pp. 584–589.

[37] A. Pierrot and Y. Goude, ‘‘Short-term electricity load forecasting with

generalized additive models,’’ Proc. ISAP Power, 2011, pp. 1–6.

[38] Y. Liang, D. Niu, and W.-C. Hong, ‘‘Short term load forecasting based on
feature extraction and improved general regression neural network model,’’
Energy, vol. 166, pp. 653–663, Jan. 2019.

[39] G. Hafeez, K. S. Alimgeer, and I. Khan, ‘‘Electric load forecasting based
on deep learning and optimized by heuristic algorithm in smart grid,’’ Appl.
Energy, vol. 269, Jul. 2020, Art. no. 114915.

[40] Y. Wang, D. Gan, M. Sun, N. Zhang, Z. Lu, and C. Kang, ‘‘Probabilis-
tic individual load forecasting using pinball loss guided LSTM,’’ Appl.
Energy, vol. 235, pp. 10–20, Feb. 2019.

VOLUME 12, 2024

111879

---

<!-- PAGE 23 -->

[41] A. Ahmed and M. Khalid, ‘‘A review on the selected applications of
forecasting models in renewable power systems,’’ Renew. Sustain. Energy
Rev., vol. 100, pp. 9–21, Feb. 2019.

[42] W. Kong, Z. Y. Dong, Y. Jia, D. J. Hill, Y. Xu, and Y. Zhang, ‘‘Short-term
residential load forecasting based on LSTM recurrent neural network,’’
IEEE Trans. Smart Grid, vol. 10, no. 1, pp. 841–851, Jan. 2019.

[43] M. Barman and N. B. Dev Choudhury, ‘‘Season specific approach for
short-term load forecasting based on hybrid FA-SVM and similarity con-
cept,’’ Energy, vol. 174, pp. 886–896, May 2019.

[44] S. Aslam, H. Herodotou, S. M. Mohsin, N. Javaid, N. Ashraf, and S. Aslam,
‘‘A survey on deep learning methods for power load and renewable energy
forecasting in smart microgrids,’’ Renew. Sustain. Energy Rev., vol. 144,
Jul. 2021, Art. no. 110992.

[45] R. Wazirali, E. Yaghoubi, M. S. S. Abujazar, R. Ahmad, and A. H. Vakili,
‘‘State-of-the-art review on energy and load forecasting in microgrids
using artificial neural networks, machine learning, and deep learning tech-
niques,’’ Electric Power Syst. Res., vol. 225, Dec. 2023, Art. no. 109792.
[46] N. Ghadimi, A. Akbarimajd, H. Shayeghi, and O. Abedinia, ‘‘Two stage
forecast engine with feature selection technique and improved meta-
heuristic algorithm for electricity load forecasting,’’ Energy, vol. 161,
pp. 130–142, Oct. 2018.

[47] F. He, J. Zhou, Z.-K. Feng, G. Liu, and Y. Yang, ‘‘A hybrid short-term
load forecasting model based on variational mode decomposition and long
short-term memory networks considering relevant factors with Bayesian
optimization algorithm,’’ Appl. Energy, vol. 237, pp. 103–116, Mar. 2019.
[48] G. Dudek, ‘‘A comprehensive study of random forest for short-term load

forecasting,’’ Energies, vol. 15, no. 20, p. 7547, Oct. 2022.

[49] S. H. Rafi and M. M. Mahdi, ‘‘A short-term load forecasting technique
using extreme gradient boosting algorithm,’’ in Proc. IEEE PES Innov.
Smart Grid Technol., Dec. 2021, pp. 1–5.

[50] K. Zhu, J. Geng, and K. Wang, ‘‘A hybrid prediction model based on pat-
tern sequence-based matching method and extreme gradient boosting for
holiday load forecasting,’’ Electric Power Syst. Res., vol. 190, Jan. 2021,
Art. no. 106841.

[51] J. Kim, J. Moon, E. Hwang, and P. Kang, ‘‘Recurrent inception convolution
neural network for multi short-term load forecasting,’’ Energy Buildings,
vol. 194, pp. 328–341, Jul. 2019.

[52] A. Yang, W. Li, and X. Yang, ‘‘Short-term electricity load forecasting based
on feature selection and least squares support vector machines,’’ Knowl.-
Based Syst., vol. 163, pp. 159–173, Jan. 2019.

[53] P. Du, J. Wang, W. Yang, and T. Niu, ‘‘A novel hybrid model for short-
term wind power forecasting,’’ Appl. Soft Comput., vol. 80, pp. 93–106,
Jul. 2019.

[54] A.-D. Pham, N.-T. Ngo, T. T. Ha Truong, N.-T. Huynh, and N.-S. Truong,
‘‘Predicting energy consumption in multiple buildings using machine
learning for improving energy efficiency and sustainability,’’ J. Cleaner
Prod., vol. 260, Jul. 2020, Art. no. 121082.

[55] S. H. Rafi, S. R. Deeba, and E. Hossain, ‘‘A short-term load forecasting
method using integrated CNN and LSTM network,’’ IEEE Access, vol. 9,
pp. 32436–32448, 2021.

[56] L. Zhang, J. Wen, Y. Li, J. Chen, Y. Ye, Y. Fu, and W. Livingood, ‘‘A review
of machine learning in building load prediction,’’ Appl. Energy, vol. 285,
Mar. 2021, Art. no. 116452.

[57] M. Tan, S. Yuan, S. Li, Y. Su, H. Li, and F. He, ‘‘Ultra-short-term industrial
power demand forecasting using LSTM based hybrid ensemble learning,’’
IEEE Trans. Power Syst., vol. 35, no. 4, pp. 2937–2948, Jul. 2020.
[58] M. Bourdeau, X. Q. Zhai, E. Nefzaoui, X. Guo, and P. Chatellier, ‘‘Model-
ing and forecasting building energy consumption: A review of data-driven
techniques,’’ Sustain. Cities Soc., vol. 48, Jul. 2019, Art. no. 101533.
[59] K. Yan, W. Li, Z. Ji, M. Qi, and Y. Du, ‘‘A hybrid LSTM neural network for
energy consumption forecasting of individual households,’’ IEEE Access,
vol. 7, pp. 157633–157642, 2019.

[60] M. Massaoudi, S. S. Refaat, I. Chihi, M. Trabelsi, F. S. Oueslati, and
H. Abu-Rub, ‘‘A novel stacked generalization ensemble-based hybrid
LGBM-XGB-MLP model for short-term load forecasting,’’ Energy,
vol. 214, Jan. 2021, Art. no. 118874.

[61] J. F. Bermejo, J. F. G. Fernández, F. O. Polo, and A. C. Márquez, ‘‘A review
of the use of artificial neural network models for energy and reliability
prediction. A study of the solar PV, hydraulic and wind energy sources,’’
Appl. Sci., vol. 9, no. 9, p. 1844, May 2019.

[62] S. Akhtar, S. Shahzad, A. Zaheer, H. S. Ullah, H. Kilic, R. Gono,
M. Jasinski, and Z. Leonowicz, ‘‘Short-term load forecasting models: A
review of challenges, progress, and the road ahead,’’ Energies, vol. 16,
no. 10, p. 4060, May 2023.

K. Ullah et al.: STLF: A Comprehensive Review and Simulation Study

[63] P. Li, K. Zhou, X. Lu, and S. Yang, ‘‘A hybrid deep learning model for
short-term PV power forecasting,’’ Appl. Energy, vol. 259, Feb. 2020,
Art. no. 114216.

[64] S. O. Abter, S. M. Jameel, H. M. Majeed, and A. H. Sabry, ‘‘Intel-
ligent forecasting temperature measurements of solar PV cells using
modified recurrent neural network,’’ EUREKA, Phys. Eng., vol. 3, no. 3,
pp. 169–177, 2024, doi: 10.21303/2461-4262.2024.003354.

[65] J. F. Torres, D. Hadjout, A. Sebaa, F. Martínez-Álvarez, and A. Troncoso,
‘‘Deep learning for time series forecasting: A survey,’’ Big Data, vol. 9,
no. 1, pp. 3–21, Feb. 2021.

[66] X. Wang, Z. Yao, and M. Papaefthymiou, ‘‘A real-time electrical load fore-
casting and unsupervised anomaly detection framework,’’ Appl. Energy,
vol. 330, Jan. 2023, Art. no. 120279.

[67] N. Huang, S. Wang, R. Wang, G. Cai, Y. Liu, and Q. Dai, ‘‘Gated spatial–
temporal graph neural network based short-term load forecasting for wide-
area multiple buses,’’ Int. J. Electr. Power Energy Syst., vol. 145, Feb. 2023,
Art. no. 108651.

[68] Y. K. Semero, J. Zhang, and D. Zheng, ‘‘EMD–PSO–ANFIS-based hybrid
approach for short-term load forecasting in microgrids,’’ IET Gener.,
Transmiss. Distrib., vol. 14, no. 3, pp. 470–475, Feb. 2020.

[69] M. Luy, V. Ates, N. Barisci, H. Polat, and E. Cam, ‘‘Short-term fuzzy load
forecasting model using genetic–fuzzy and ant colony–fuzzy knowledge
base optimization,’’ Appl. Sci., vol. 8, no. 6, p. 864, May 2018.

[70] D. Yang, J.-E. Guo, Y. Li, S. Sun, and S. Wang, ‘‘Short-term load forecast-
ing with an improved dynamic decomposition-reconstruction-ensemble
approach,’’ Energy, vol. 263, Jan. 2023, Art. no. 125609.

[71] Z. Wang, T. Hong, and M. A. Piette, ‘‘Building thermal load prediction
through shallow machine learning and deep learning,’’ Appl. Energy,
vol. 263, Apr. 2020, Art. no. 114683.

[72] S. Bouktif, A. Fiaz, A. Ouni, and M. A. Serhani, ‘‘Multi-sequence LSTM-
RNN deep learning and metaheuristics for electric load forecasting,’’
Energies, vol. 13, no. 2, p. 391, Jan. 2020.

[73] L. Wen, K. Zhou, S. Yang, and X. Lu, ‘‘Optimal load dispatch of commu-
nity microgrid with deep learning based solar power and load forecasting,’’
Energy, vol. 171, pp. 1053–1065, Mar. 2019.

[74] M. Sun, T. Zhang, Y. Wang, G. Strbac, and C. Kang, ‘‘Using Bayesian deep
learning to capture uncertainty for residential net load forecasting,’’ IEEE
Trans. Power Syst., vol. 35, no. 1, pp. 188–201, Jan. 2020.

[75] B. Nepal, M. Yamaha, A. Yokoe, and T. Yamaji, ‘‘Electricity load fore-
casting using clustering and ARIMA model for energy management in
buildings,’’ Jpn. Architectural Rev., vol. 3, no. 1, pp. 62–76, Jan. 2020.

[76] T. Hong, J. Xie, and J. Black, ‘‘Global energy forecasting competition
2017: Hierarchical probabilistic load forecasting,’’ Int. J. Forecasting,
vol. 35, no. 4, pp. 1389–1399, Oct. 2019.

[77] Z. Zhang and W.-C. Hong, ‘‘Electric load forecasting by complete ensem-
ble empirical mode decomposition adaptive noise and support vector
regression with quantum-based dragonfly algorithm,’’ Nonlinear Dyn.,
vol. 98, no. 2, pp. 1107–1136, Oct. 2019.

[78] I. Shah, H. Iftikhar, S. Ali, and D. Wang, ‘‘Short-term electricity demand
forecasting using components estimation technique,’’ Energies, vol. 12,
no. 13, p. 2532, Jul. 2019.

[79] M. Alhussein, K. Aurangzeb, and S. I. Haider, ‘‘Hybrid CNN-LSTM model
for short-term individual household load forecasting,’’ IEEE Access, vol. 8,
pp. 180544–180557, 2020.

KALEEM ULLAH received the Ph.D. degree in
electrical engineering (power) from the Univer-
sity of Engineering and Technology, Peshawar.
He is currently an accomplished Electrical Engi-
neer specializing in power systems. During the
Ph.D. study, he conducted extensive research
on real-time dynamic dispatch strategies for
automatic generation control (AGC) and load
forecasting mechanisms focusing on integrating
large-scale RES power into the grid while main-
taining active power balance and enhancing system reliability. USAID
Pakistan funded his work through an applied research grant. He secured a
significant grant from Pakistan Science Foundation for his research project
on load dispatch control for Pakistan Power System.

111880

VOLUME 12, 2024

---

<!-- PAGE 24 -->

K. Ullah et al.: STLF: A Comprehensive Review and Simulation Study

MUHAMMAD AHSAN received the B.Eng.
degree in electrical engineering from the NED
University of Engineering and Technology and the
master’s degree in data science from the University
of Alabama at Birmingham. He is equipped with
a strong foundation in electrical engineering and
data science. His dedication to his field is evi-
dent through his commitment to staying updated
with the latest advancements in data science and
its applications. His research interests include the
intersection of data science and electrical engineering, where he aims to
develop innovative solutions to complex problems.

SYED MUHAMMAD HASANAT received the
B.Sc. degree in electrical engineering from
the University of Engineering and Technology,
Peshawar. He is currently pursuing the master’s
degree in electrical energy system engineering
with Center for Advanced Studies in Energy, UET
Peshawar. He is focusing his research efforts on
the critical area of short-term load forecasting.
He is dedicated to addressing the challenges and
complexities inherent in energy systems manage-
ment. His scholarly pursuits have garnered recognition, with his work being
published in numerous impactful journals in recent years.

MUHAMMAD HARIS received the B.Sc. degree
in mathematics and economics from Lahore Uni-
versity of Management Sciences, in 2021. He is
currently pursuing the M.S. degree in data science
and analytics with Georgia State University. He is
also a Graduate Research Assistant at Georgia
State University, collaborating with Truist Bank’s
ESG and Climate Data and Analytics Team. He has
significant experience in data science, having
worked at Afiniti Inc., where he optimized cus-
tomer retention and developed predictive models. In this role, he applies
advanced NLP techniques and generative AI to enhance climate-related
financial disclosures. His research interests include machine learning, LSTM
networks, and natural language processing (NLP).

SYED FARAZ RAZA received the B.Eng. degree
in electronic engineering from the NED Uni-
versity of Engineering and Technology, Karachi.
He is currently pursuing the master’s degree in
data science from the University of Alabama
at Birmingham. Demonstrating a commitment to
academic excellence and a passion for advancing
his knowledge, he is pursuing the master’s degree.
He is focusing his skill set on machine learning
and artificial intelligence to support the research

efforts in the critical area of short-term load forecasting.

RITESH TANDON received the master’s degree
in data science from Indiana University, Bloom-
ington, IN, USA. He is currently an accomplished
Lead Data Scientist. With a career spanning
over two decades in the information technology
industry, he has been at
the forefront of the
machine learning and artificial intelligence revolu-
tion. Since 2019, he has been with PLIC, where his
passion for AI has driven him to design and imple-
ment cutting-edge data software products tailored
for the insurance industry. His expertise in developing machine learning
models has been instrumental in optimizing costs and mitigating risks for
his company. His work in NLP has led to innovative solutions for document
classification and question-answering models. In addition, he has signifi-
cantly contributed to speech-to-text technology, extracting valuable insights
from spoken language. Dedicated to advancing AI, he is committed to
architecting and implementing intelligent solutions that push the boundaries
of technology.

SAMAIN ABID received the B.Sc. degree in com-
puter science from the Sir Syed University of
Engineering and Technology. He is currently pur-
suing the master’s degree in data science with
the University of Alabama at Birmingham. His
research primarily focuses on machine learning
predictive models, where he aims to solve complex
problems in data analytics. His dedication to his
field is evident through his innovative approach to
addressing the challenges in data science.

HAMZA YOUSAF received the B.B.A. degree
(Hons.)
from Lahore School of Economics,
Pakistan, in 2016, and the M.S. degree in busi-
ness analytics from the Stetson-Hatcher School of
Business, Mercer University, Macon, GA, USA,
in 2024. He was an Analyst in various multina-
tional corporations, leveraging his data science and
analytics expertise. His research interests include
machine learning, deep learning, predictive mod-
eling, sentiment analysis, and anomaly detection.

ZAHID ULLAH (Graduate Student Member,
IEEE)
received the B.S. degree in electrical
engineering from UET Peshawar, in 2014, and
the M.S. degree in electrical engineering from
COMSATS University Islamabad, Abbottabad
Campus, Abbottabad, Pakistan, in 2017. He is
currently pursuing the Ph.D. degree in electri-
cal engineering with Politecnico di Milano, Italy.
He was a Lecturer with UMT Lahore, Pakistan.
His research interests include smart grids, energy
management, renewable energy systems, AI for energy, and ICTs for power
systems.

Open Access funding provided by ‘Politecnico di Milano’ within the CRUI CARE Agreement

VOLUME 12, 2024

111881

<!-- MARKITDOWN CONVERSION -->

<!-- Full MarkItDown conversion for formatting fidelity. -->

Received26July2024,accepted6August2024,dateofpublication8August2024,dateofcurrentversion21August2024.
DigitalObjectIdentifier10.1109/ACCESS.2024.3440631
Short-Term Load Forecasting: A Comprehensive
Review and Simulation Study With CNN-LSTM
Hybrids Approach
KALEEMULLAH 1,MUHAMMADAHSAN 2,SYEDMUHAMMADHASANAT1,
MUHAMMADHARIS 3,HAMZAYOUSAF 4,SYEDFARAZRAZA2,RITESHTANDON5,
SAMAINABID2,ANDZAHIDULLAH 6,(GraduateStudentMember,IEEE)
1CentreforAdvancedStudiesinEnergy,UniversityofEngineeringandTechnology,Peshawar(UETPeshawar),Peshawar25000,Pakistan
2DepartmentofComputerScience,UniversityofAlabamaatBirmingham,Birmingham,AL35294,USA
3InstituteforInsight,J.MackRobinsonCollegeofBusiness,GeorgiaStateUniversity,Atlanta,GA30303,USA
4Stetson-HatcherSchoolofBusiness,MercerUniversity,Macon,GA30341,USA
5SchoolofInformatics,Computing,andEngineering,IndianaUniversity,Bloomington,IN47405,USA
6DipartimentodiElettronica,InformazioneeBioingegneria,PolitecnicodiMilano,20133Milan,Italy
Correspondingauthor:ZahidUllah(zahid.ullah@polimi.it)
ThisworkwassupportedbythePolitecnicodiMilanoforprovidingOpenAccesswithintheCRUICAREAgreement.
ABSTRACT Short-termloadforecasting(STLF)isvitalineffectivelymanagingthereserverequirementin
modernpowergrids.Subsequently,itsupportsthegridoperatorinmakingeffectiveandeconomicaldecisions
during the power balancing operation. Therefore, this study comprehensively reviews STLF methods,
includingtimeseriesanalysis,regression-basedframeworks,artificialneuralnetworks(ANNs),andhybrid
models that employ different forecasting approaches. Detailed mathematical and graphical analyses and
a comparative evaluation of these methods are provided, highlighting their advantages and disadvantages.
Further,thestudyproposesahybridCNN-LSTMmodelcomprisedofConvolutionalneuralnetworks(CNN)
forfeatureextractionofhighdimensionaldataandLongshort-termmemory(LSTM)networkstoboostthe
model’sefficiencyfortemporalsequenceprediction.Thisstudyassessedthemodelusingacomprehensive
datasetfromPakistan’sNTDCnationalgrid.Theanalysisrevealedsuperiorperformanceinshort-termload
prediction,achievingenhancedaccuracy.Forsingle-stepforecasting,themodelyieldedanRMSEof538.71,
MAE of 371.97, and MAPE of 2.72. In 24-hour forecasting, it achieved an RMSE of 951.94, MAE of
656.35,andMAPEof4.72ontheNTDCdataset.Moreover,themodelhasoutperformedpreviousmodels
incomparisonusingtheAEPdataset,demonstratingitssuperiorityinenhancingreservemanagementand
balancingsupplyanddemandinmodernelectricitynetworks.
INDEX TERMS Short-term load forecasting, convolution neural network, hybrid LSTM-CNN network,
NTDCPakistan,powerbalancingoperation.
I. INTRODUCTION also enhance the work of utilizing the available resources,
Forecastingloaddemandiscentraltopowersystemmanage- henceimprovingtheoverallfunctionalityofthesystems[1].
ment and planning; thus, the accuracy of available demand STLF constitutes a fundamental element in energy man-
forecastingmodelsiscrucialforeffectivelymanagingpower agement [2]. These models are made for forecasting power
grids. From this perspective, short-term load forecasting requirements for the short-term timeframe ranging from an
(STLF)enablesthepropermanagementofenergyresources hour ahead to days or weeks at most but typically up to a
andtheaccuratecontrolofenergystorage.Theaccurateand maximumofonemonthonly.Thesemodelsareinvaluablefor
timelypredictionsofpossiblefutureloadvariationsbySTLF utilitycompaniesandgridoperatorsastheyhelpinplanning
theresourcesusingbetterforesighttomanagetheresponses
The associate editor coordinating the review of this manuscript and totheever-changingenergyrequirementsthatensurethesta-
bilityandavailabilityofthepowersupplysystems.However,
approvingitforpublicationwasAkshayKumarSaha .
2024TheAuthors.ThisworkislicensedunderaCreativeCommonsAttribution4.0License.
111858 Formoreinformation,seehttps://creativecommons.org/licenses/by/4.0/ VOLUME12,2024

K.Ullahetal.:STLF:AComprehensiveReviewandSimulationStudy
in the progress made before the big data era, various STLF syntheses of STLF models. These updates are important in
methodologies have appeared in the literature, each with keepingupwiththecurrenttechnologicaladvancementsand
inherentfeaturesandlimitations[3].Theseframeworkscover improving the prediction factors. To address this research
aspectrumofcomputationmethods,includingartificialneu- gap, this review manuscript discusses the preceding points
ralnetworks(ANNs),timeseriesanalysis,regression-based and explores advanced or relatively new STLF models that
methods, and a combination of both (hybrid systems). The the earlier reviews may not have captured well. It also pro-
timeseriesmethodsutilizehistoricalloadinformationusing posesanovelintegrationapproachofLSTMfortimeseries
variant statistical tools, including ARIMA models and dif- analysis and CNN for features from high-dimension data to
ferent types of exponential smoothing, to identify and then enhance precision in prediction. By evaluating the result of
temporally analyze load trends to improve load forecasts’ themodel,theNTDCPakistanNationalGridofferedadata
accuracy[4].Contrarily,ANNsareacomplexsetofmachine setforthestudy.
learningstructurescapableoflearninginput-outputmapping
| that otherwise | has | a non-linear | relationship. |     | These mod- |     |     |     |     |     |     |     |
| -------------- | --- | ------------ | ------------- | --- | ---------- | --- | --- | --- | --- | --- | --- | --- |
els are trained across various data set assemblages using A. LITERATURESURVEY
TheconstructionofSTLFmodelsisachallengingandcom-
| backpropagation | networks, | enabling | them | to adapt | to infor- |     |     |     |     |     |     |     |
| --------------- | --------- | -------- | ---- | -------- | --------- | --- | --- | --- | --- | --- | --- | --- |
mation complex formation [5]. Regression-based models plicatedactivitybecauseithastodealwithvariousconcerns
utilize linear or non-linear regression techniques to map connected to the dynamic features of load data. These data
causal associations with load and other features such as are time-dependent and affected by factors such as the cli-
humidity,temperature,andtimeofday[6]. matestate,economiccharacteristics,andbuyers’behaviour,
|             |            |        |       |               |         | whether | they are | individuals | or  | companies |     | [10]. Conse- |
| ----------- | ---------- | ------ | ----- | ------------- | ------- | ------- | -------- | ----------- | --- | --------- | --- | ------------ |
| Contrarily, | integrated | models | blend | the strengths | of dif- |         |          |             |     |           |     |              |
ferent modeling approaches, such as ANNs and time series quently, there is a need for STLF models to incorporate the
analysis, with the explicit intention of improving accuracy skillsthatallowthemtolearnthesedynamicdatageneration
and increasing resistance to interference [7]. Though, each processes.Apartfromcontrollingtransientinformation,deal-
class of model has its unique difficulties and oddities. For ingwithuncertaintiesandrisksposesmajorchallenges[11].
|          |                |         |            |       |          | Other conventional |     | approaches |     | offer | some forecast, | more |
| -------- | -------------- | ------- | ---------- | ----- | -------- | ------------------ | --- | ---------- | --- | ----- | -------------- | ---- |
| example, | in time series | models, | challenges | often | arise in |                    |     |            |     |       |                |      |
explainingenduringtrendsandtemporaryfluctuations,load often, just a point estimation while failing to incorporate
data in particular, reacting more sharply to anomalies and correspondingvariabilityorrisk.Tremendouseffortsneedto
gaps in information. However, there are drawbacks associ- bemadetobridgethisdivideandimplementmoreadvanced
ated with the computational complexity of ANNs, which modelsthatprovideprobabilisticforecasts,asdemonstrated
|              |           |       |           |                   |      | by the models | that | utilize | the quantile |     | regression | approach. |
| ------------ | --------- | ----- | --------- | ----------------- | ---- | ------------- | ---- | ------- | ------------ | --- | ---------- | --------- |
| subsequently | decreases | their | levels of | interpretability; | this |               |      |         |              |     |            |           |
is coupled with their inherent tendency to fit over. Further, These reports employ advanced methodologies as a way of
ANNs suffer from noise and bias in training data and are addressingissuesofvariabilitythatareoftenassociatedwith
thedata.
| also sensitive | to variations | [8]. | A major | drawback | of the |     |     |     |     |     |     |     |
| -------------- | ------------- | ---- | ------- | -------- | ------ | --- | --- | --- | --- | --- | --- | --- |
regression-basedmodelsisthattheyaregenerallyrestricted Moreover, incorporating wind and solar power as a part
|     |     |     |     |     |     | of renewable | energy | also | adds fluctuations |     | and | randomness |
| --- | --- | --- | --- | --- | --- | ------------ | ------ | ---- | ----------------- | --- | --- | ---------- |
toidentifyinglinearandadditiverelationswithininput/output
data.Inaddition,themodelsarenotaccustomedtohandling to the power supply, negatively impacting the precision and
categoricalornon-numericaldata.Thesechallengesthreaten efficiency of STLF models [12]. Similar challenges relate
|     |     |     |     |     |     | to data | characteristics | in  | studying | current | trends; | the data |
| --- | --- | --- | --- | --- | --- | ------- | --------------- | --- | -------- | ------- | ------- | -------- |
themodelasitcannoteffectivelyemploygraphstructuresto
representoranalyzecomplexdata[9]. field is high-dimensional, and various input variables such
asweatherconditions,vacationplans,andeconomicactivity
| Alternatively, | some | drawbacks | of hybrid | models | include |     |     |     |     |     |     |     |
| -------------- | ---- | --------- | --------- | ------ | ------- | --- | --- | --- | --- | --- | --- | --- |
thecontingencyoftheExtendedModelwithincreasedmodel indicators exist. This implies that identifying and selecting
complexityandanincreasednumberofparameters,issuesin relevantpredictorsforregressionmodelsisasignificantstep
|     |     |     |     |     |     | toward avoiding |     | overfitting | and | improving | forecasting | pre- |
| --- | --- | --- | --- | --- | --- | --------------- | --- | ----------- | --- | --------- | ----------- | ---- |
parametertuning,andprimaryissuesofoverfittinganddata
redundancyofthemodel.Inthisregard,thenecessarysteps cision [13]. Moreover, it can be found that non-Gaussian
mustbetakentotackletheseissuesbycomparingandassess- and highly salience distributions are usually present in load
ingthedifferentSTLFmodels.Thisshouldbedoneregarding data[14],andthesecharacteristicsarenotsuitableformost
some of the actual load data that has been evaluated and ofthetraditionalapproachesforforecast-basedmodelssince
|     |     |     |     |     |     | they violate | the | basic assumptions. |     | This | means | that effec- |
| --- | --- | --- | --- | --- | --- | ------------ | --- | ------------------ | --- | ---- | ----- | ----------- |
verifiedusingawiderangeofmeasuresandmethodsforval-
idationpurposestounderstandtheirefficiencyandreliability tive models need to incorporate such relation patterns, and
better.Thisway,consideringone’sadvantagesandchallenges therefore, the structure includes load data and other aspects
makes it possible to evaluate and compare various model such as climates and economic factors. The temporal and,
typesandassesstheirapplicabilityinsustainablyaddressing mainly, spatial structure of load data adds further challenge
|                |         |             |     |           |             | because | the load | often exhibits | different |     | patterns | depending |
| -------------- | ------- | ----------- | --- | --------- | ----------- | ------- | -------- | -------------- | --------- | --- | -------- | --------- |
| the complexity | of load | forecasting | in  | practical | operational |         |          |                |           |     |          |           |
environments. Given the current fast-paced development in onthegeographiclocationandtimeofdayoryear,andthis
AI and data processing methods, there is an ongoing need informationmustbeincorporatedintomodelsbyrecognizing
to engage the sources that present the most contemporary andprovidingforspatialcorrelationsandvariationsinload.
| VOLUME12,2024 |     |     |     |     |     |     |     |     |     |     |     | 111859 |
| ------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------ |

K.Ullahetal.:STLF:AComprehensiveReviewandSimulationStudy
Further, the clarity and interpretability of STLF models are prediction precision. This work uses a possessive dataset of
criticalasthesemodelsplayacrucialroleindrivingkeydeci- the national network of NTDC Pakistan to test and validate
sions in the energy sector, such as Load management [15]. the model. The proposed model demonstrates exceptional
Thoseundertakingdecision-makingrolesinenergysystems accuracy in single-step and 24-hour forecasting, achieving
musthavecomprehensiblemodelresultstoactpromptlyand significantly lower error metrics than the reference meth-
efficiently. However, a need for data, which is both scarce ods. For single-step forecasting, the NTDC dataset shows
and of questionable quality, is the last but very important an RMSE of 538.71, MAE of 371.97, and MAPE of 2.72,
matterthathindersthecreationofaccurateSTLFmodels.The while the AEP dataset achieves an RMSE of 126.35, MAE
high-quality data needed to train and validate the different of 94.27, and MAPE of 0.64. For 24-hour forecasting, the
modelspointstothesignificantneedtoaddressdataissuesif NTDCdatasetreportsanRMSEof951.94,MAEof656.35,
theaccuracyoftheclimateforecastsistobeenhanced. andMAPEof4.72,andtheAEPdatasetshowsanRMSEof
These challenges have, for instance, been elaborated in 702.97,MAEof507.97,andMAPEof3.39.
detail to understand the best methodological approaches to
conduct research in the STLF and other solutions towards C. STRUCTUREOFTHEPAPER
creatinginnovativestrategiestosolvethemwithinthefield. The paper is divided into two main sections, as shown
Similarly,forcopingwiththenon-stationarydata,newmod- in Figure 1: a comprehensive review and development of
elsthataretime-varying,suchasTVARMA,andforhaving a practical hybrid model for STLF. The review examines
better learning algorithms, such as DNNs, have been devel- various STLF models, including statistical, intelligent, and
oped[11],[14].Toenhancedealingwithuncertaintyandrisk, hybrid models, each subject to detailed analysis. The (2nd)
variousstatisticalmethodologieslikequantileregressionand section of the paper presents an innovative hybrid approach
scenario-based forecasting have been employed [16], [17]. usingLSTMandCNNforsingle-stageandmulti-stageload
The integration of STLF with the forecasts of renewable forecasting.
energy intends to enhance accuracy. It is further supported
bydemandresponseandenergystoragetocopewithfluctua-
tionsintherenewablesource[12].Methodsusedforfeature
selection and dimensionality include feature selection and
dimensionality reduction, which is crucial in handling the
huge and complicated nature of STLF data. At the same
time, robust models and distribution approaches address
non-Gaussian distributions of data [18]. Nonparametric and
kernel-based models are preferred for nonlinearity relations
since they are more effective than parametric models [14].
Spatial and temporal models and clustering methods are
properlyemployedtoaccountforandpromotespatialprop-
erties dependency. Causal inference methods are used to
enhancethetrustinmodelsforenergymanagementastrans-
parency and interpretability of the models are essential for FIGURE1. Organizationofthepaper.
informeddecision-makinginthecorrespondingdomain[14].
Theaforementioneddataavailabilityandqualityconcernsare
alsodiscussed,aswellasothermethods,includingdataaug- II. LOADFORECASTINGLEVELS
mentation, transfer learning, and domain adaptation. These Load forecasting operates at different levels, each serving
methods enhance the reliability and versatility of the STLF specific managerial goals and employing various methods.
models and extend the horizons of forecasting trends to the Micro-levelforecastinginvolvesanalyzingsmallersegments
energyindustry[19],[20]. withinaregiontoestimateloadpatterns,whichiscrucialfor
managingenergyplantsandgrids.
Macro-levelforecastinglooksatbroaderareaslikecitiesor
B. PAPERCONTRIBUTION countrieswithoutdividingthemintosmallerparts.Regarding
The study comprehensively reviews STLF methods, includ- the time of the forecast for the load, they are divided into
ingtimeseriesanalysis,regression-basedframeworks,artifi- three levels, including short, medium, and long forecasting
cialneuralnetworks(ANNs),andhybridmodelsthatemploy levels, as shown in Fig. 2 [21]. Short-term forecasting pre-
differentforecastingapproaches.Detailedmathematicaland dictshourlyloads,importantforenergyplantschedulingand
graphical analyses and a comparative evaluation of these gridstability.Mid-termforecastingcoversmonthlytoyearly
methodsareprovided,highlightingtheiradvantagesanddis- projections for managing peak consumption and resource
advantages. Furthermore, the research suggests a combined planning.Long-termforecastinghelpswithmajordecisions
modelofCNNandLSTMfordeepercharacteristicsextrac- likeinvestingininfrastructureandplanningforfutureenergy
tionandtemporalsequenceanalysis,respectively,toenhance needs.Despiteusingdifferentmethods,allforecastinglevels
111860 VOLUME12,2024

K.Ullahetal.:STLF:AComprehensiveReviewandSimulationStudy
|     |     |     |     | well-defined | seasonal   |         | behaviour | [25].      | In          | turn, exponential |            |
| --- | --- | --- | --- | ------------ | ---------- | ------- | --------- | ---------- | ----------- | ----------------- | ---------- |
|     |     |     |     | smoothing    | (ES)       | models  | forecast  | the        | future      | load              | demand     |
|     |     |     |     | based on     | seasonal   | factors | by        | providing  | certain     |                   | weights to |
|     |     |     |     | the previous | values.    |         | Despite   | being      | accurate,   | quick             | to com-    |
|     |     |     |     | pute, and    | relatively |         | easy to   | implement, | statistical |                   | models     |
haveseverallimitationsstemmingfromtheirbasicstructure;
|     |     |     |     | they may | not | delineate | the | nonlinear | links | and | dependen- |
| --- | --- | --- | --- | -------- | --- | --------- | --- | --------- | ----- | --- | --------- |
ciesinpowersystemsand,consequently,couldprovideless
accuratepredictions.EMSforpowersystemsemploysSTLF
|     |     |     |     | as a foundational |              | component |       | for advanced |         | energy   | applica- |
| --- | --- | --- | --- | ----------------- | ------------ | --------- | ----- | ------------ | ------- | -------- | -------- |
|     |     |     |     | tions [26].       | Hence,       | a         | model | that can     | predict | accurate | STLF     |
|     |     |     |     | is of utmost      | significance |           | in    | optimizing   | the     | power    | system’s |
FIGURE2. Timeframesfortheloadforecastinglevels.
|     |     |     |     | energy supply |     | and demand |     | balance, | leading | to  | increased |
| --- | --- | --- | --- | ------------- | --- | ---------- | --- | -------- | ------- | --- | --------- |
efficiencyinutilizingenergy,reducedcosts,andsystemreli-
considerfactorslikepopulationgrowthandenergypricesto
ability.Adetailedexplanationofsomeofthesemodelsanda
makeaccuratepredictions.Inthisstudy,theSTLFmodelsare literaturereviewarepresentedinthefollowingsection.
emphasized.
| III. STLFMODELS |     |     |     | 1) AUTOREGRESSIVEINTEGRATEDMOVINGAVERAGE |     |     |     |     |     |     |     |
| --------------- | --- | --- | --- | ---------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
TraditionalmethodsforSTLFrelyonhistoricaldatarelated (ARIMA)MODELS
to electricity consumption, weather conditions, and calen- ARIMA models find extensive application in STLF owing
dar events. Conversely, the proliferation of emerging data to their straightforward nature and capacity to capture tem-
channels,suchassocialmediaanalyticsandgranularteleme-
|     |     |     |     | poral patterns |     | within | load | data. These | models |     | consist of |
| --- | --- | --- | --- | -------------- | --- | ------ | ---- | ----------- | ------ | --- | ---------- |
try from smart measurement infrastructures, represents an threemaincomponents:theautoregressive(AR)component,
excellent opportunity to improve the accuracy and robust- whichquantifiestheinfluenceexertedbypredecessorvalues;
nessofSTLFparadigms.Usingsophisticatedcomputational
|     |     |     |     | the integrated |     | (I) component, |     | which | incorporates |     | differen- |
| --- | --- | --- | --- | -------------- | --- | -------------- | --- | ----- | ------------ | --- | --------- |
methods, including deep neural architectures and adaptive tiation to achieve stationarity within the data set; and the
| reinforcement | learning algorithms, | is expected | to signifi- |     |     |     |     |     |     |     |     |
| ------------- | -------------------- | ----------- | ----------- | --- | --- | --- | --- | --- | --- | --- | --- |
movingaverage(MA)component,whichincludestheinflu-
cantly optimize STLF systems’ precision. Deep learning ence of prior stochastic deviations [27]ARIMA frameworks
enables the automatic extraction of intricate data patterns provide considerable adaptability through their parametric
| and relationships, | while reinforcement | learning | facilitates |               |     |          |          |     |            |     |             |
| ------------------ | ------------------- | -------- | ----------- | ------------- | --- | -------- | -------- | --- | ---------- | --- | ----------- |
|                    |                     |          |             | customization |     | options, | allowing | for | meticulous |     | calibration |
optimizing actions based on environmental feedback [22]. of the AR and MA sequences, alongside the differentiation
Further,convertingtheforecastsintopointforecastsenables
|     |     |     |     | magnitude | in the | I segment. |     | Such configurability |     |     | facilitates |
| --- | --- | --- | --- | --------- | ------ | ---------- | --- | -------------------- | --- | --- | ----------- |
powersystemoperatorstomaketherightdecisionswhenthe themodel’salignmentwiththedataset’speculiaritiesandthe
actualuncertaintyisexperiencedbyincludingtheprobability preciseforecastingprerequisites[28].Nonetheless,ARIMA
estimationofthepointforecasts.STLFmodelscoverstatis-
modelsoperateassumingthatloaddataadherestoastation-
tical,intelligent,andhybridsystems,allofwhichhavetheir ary process, a condition that might not consistently hold in
meritsandareasofapplication[23].
|     |     |     |     | power system | contexts. |     | Moreover, | these | models | may | fail to |
| --- | --- | --- | --- | ------------ | --------- | --- | --------- | ----- | ------ | --- | ------- |
capturetheintricatenonlinearconnectionsbetweenloadpat-
A. MODELSBASEDONSTATISTICALTECHNIQUES terns and various influential factors like weather conditions
Statisticaltoolsgroundedonanalysisconceptsoftimeseries andoccupancylevels.
loaddemandprofilesareparticularlyusefulinexplainingthe Figure 3 gives the algorithm for ARIMA models. The
temporaldynamicscontainedinloaddemandprofiles.Based notation represents the ARIMA model as ARIMA(p,d,q); p
on the bibliography found in the course of the research, the referstothenumberoftheautoregressiveterm‘AR,’drefers
primary types of statistical structures used in the field of to the degree of differencing applied to make a time series
STLFareasfollows:ARIMAmodels,theirseasonalcounter- stationary, and q refers to the number of moving average
parts,SARIMA,generalizedlinearmodels,andexponential term‘MA.’Theseparametersareexplainedbycomparingthe
smoothing models [24]. ARIMA models crucially assume specificfeaturesoftheinvestigatedtimesseriesinherentchar-
that current load requirements are formed from past load acteristicsemployingadvancedstochasticanalysismethods,
sequences and a stochastic term. SARIMA models enhance including the maximum likelihood estimation, to guarantee
thisstructuralplanbyincorporatingfluctuationsofaseasonal the reliability of the fit between the suggested model and
nature, which are almost always present in energy activity observeddata.Afterassessingtheseparameters,theARIMA
systems where loading demand varies cyclically: diurnal or model is ready to forecast new values in the time series. Its
menstrual. This integration helps improve the cyclical tem- mechanismusespastdatatoguessthenextentryintheseries
poral dependencies to recur at specific intervals to improve with the help of the AR and the MA parts. Subsequently,
precise prediction models where the load is dominated by the forecasted value is used to adjust the error term, using
| VOLUME12,2024 |     |     |     |     |     |     |     |     |     |     | 111861 |
| ------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------ |

K.Ullahetal.:STLF:AComprehensiveReviewandSimulationStudy
which an improved estimate of the temporal increment is intensifying the transformation to ensure enhanced statisti-
derived for the subsequent temporal segment. This process calconstancy.Forexample,themechanismofsecond-order
repeatsitselfroutinelyandproducesafinalforecastcovering differencingmaterializesbyapplyingdifferencinganewtoa
pre-designatedfutureperiods. seriesthathasalreadybeensubjectedtoafirst-orderdiffer-
| TheARfacetrequiresthattoday’sobservationinthetime |     |     |     |     |     | encingprocess. |     |     |     |     |     |     |     |
| ------------------------------------------------- | --- | --- | --- | --- | --- | -------------- | --- | --- | --- | --- | --- | --- | --- |
seriesdependsonpastobservationsinthesametimeseries.
|     |     |     |     |     |     |     |     | (cid:49)2Y( | )=  | Yt( )−Yt( |     | −1) | (3) |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------- | --- | --------- | --- | --- | --- |
AnARconfigurationoforder’p’isdesignatedasAR(p),with
itsrespectiveformulationexplicatedasfollows: TheMAcomponentembodiestheinfluenceofpriorerror
∁+ϕ ( −1)+ϕ ( −2)............... termsonthecurrentvalueofthetimeseries.AnMAmodel,
| Y(t)= |     | Y   |     |     |     |                         |     |     |     |                  |     |     |           |
| ----- | --- | --- | --- | --- | --- | ----------------------- | --- | --- | --- | ---------------- | --- | --- | --------- |
|       |     | 1   | 2   |     |     | characterizedbyanorder’ |     |     |     | ,’isdenotedasMA( |     |     | ),withits |
+ϕ ( −p)E(
|     |     |     | )   |     | (1) | equationexpressedasfollows: |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --------------------------- | --- | --- | --- | --- | --- | --- | --- |
p
In(1),Y(t)representsthevalueofthetimeseriesattime Y(t)= r + ∈( )− ψ ∈( −1)−ψ ∈( −2)−...
|               |     |               |        |           |               |     |     |      |     | 1   |     | 2   |     |
| ------------- | --- | ------------- | ------ | --------- | ------------- | --- | --- | ---- | --- | --- | --- | --- | --- |
| t, reflecting | the | current state | of the | series. c | is a constant |     |     |      |     |     |     |     |     |
|               |     |               |        |           |               |     | −   | ψ ∈( | −ϱ) |     |     |     | (4) |
1
| term representing |     | any fixed, | unchanging | component | within |     |     |     |     |     |     |     |     |
| ----------------- | --- | ---------- | ---------- | --------- | ------ | --- | --- | --- | --- | --- | --- | --- | --- |
the time series. ϕ ϕ .........ϕ denote the autoregressive In (4), Y(t) denotes the value of the time series at a time
|     |     | 1 2 | p   |     |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
coefficients, each capturing the influence of past values of t, reflecting the present conditionsof the series. The term
the time series on the present value. These coefficients are r represents a constant factor that remains invariant across
integral to understanding the temporal dependencies within the temporal span. In the equation, ∈ (t) signifies the error
the series. p signifies the order of the AR model, indicating term at time t, encapsulating the discrepancy between the
thenumberofpastobservationsconsideredinpredictingthe observedvalueandthevaluepredictedbythemodelatthat
| currentvalue. |     |     |     |     |     |          |       |     |              | ψ   | ψ ψ   | ......ψ |             |
| ------------- | --- | --- | --- | --- | --- | -------- | ----- | --- | ------------ | --- | ----- | ------- | ----------- |
|               |     |     |     |     |     | specific | time. | The | coefficients |     | 1 2 3 |         | ϱ represent |
themovingaverageparameters,determininghowmuchpast
|     |     |     |     |     |     | error | terms | influence | the | current | series value. | These | coeffi- |
| --- | --- | --- | --- | --- | --- | ----- | ----- | --------- | --- | ------- | ------------- | ----- | ------- |
cientsdelineatethetemporalinterdependenciesintheseries
|     |     |     |     |     |     | attributed | to  | antecedent | errors. | The | variable | ϱ specifies | the |
| --- | --- | --- | --- | --- | --- | ---------- | --- | ---------- | ------- | --- | -------- | ----------- | --- |
orderoftheMAmodel,representingthecountofpriorerror
termsfactoredintotheforecastofthecurrentvalue.Anele-
|     |     |     |     |     |     | vated | ϱ value | suggests | an  | expansive | inclusion |     | of historical |
| --- | --- | --- | --- | --- | --- | ----- | ------- | -------- | --- | --------- | --------- | --- | ------------- |
errortermsinthepredictiveframework.
|     |     |     |     |     |     | By  | integrating |     | the AR, | I, and | MA components, |     | we can |
| --- | --- | --- | --- | --- | --- | --- | ----------- | --- | ------- | ------ | -------------- | --- | ------ |
representanARIMA(p,d,ϱ)modelas:
|     |     |     |     |     |     | (cid:49)dY(t)=∁+ϕ |                |     | (cid:49)dY(t  | −1)...... | ϕ   | (cid:49)dY(t | −p)+∈(t) |
| --- | --- | --- | --- | --- | --- | ----------------- | -------------- | --- | ------------- | --------- | --- | ------------ | -------- |
|     |     |     |     |     |     |                   |                |     | 1             |           | p   |              |          |
|     |     |     |     |     |     |                   |                | − ψ | ∈(t −1)−...−ψ |           | ∈(t | −q)(t)       |          |
|     |     |     |     |     |     |                   |                | 1   |               |           | q   |              |          |
|     |     |     |     |     |     |                   | =(cid:49)Y(t)= |     | Y(t)−Y(t      |           | −1) |              | (5)      |
2) SEASONALAUTOREGRESSIVEINTEGRATEDMOVING
AVERAGE(SARIMA)MODEL
|     |     |     |     |     |     | SARIMA |     | models, | building | upon | the | foundation | laid by |
| --- | --- | --- | --- | --- | --- | ------ | --- | ------- | -------- | ---- | --- | ---------- | ------- |
FIGURE3. AlgorithmoftheARIMAmodel.
|     |     |     |     |     |     | ARIMA | models, |     | extend | their capabilities |     | to accommodate |     |
| --- | --- | --- | --- | --- | --- | ----- | ------- | --- | ------ | ------------------ | --- | -------------- | --- |
seasonalvariationsinherentinvariousdatasets.Thesemodels
| A higher | p-value | implies | a more extensive | consideration |     |     |     |     |     |     |     |     |     |
| -------- | ------- | ------- | ---------------- | ------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
introduceadditionalparametersexplicitlydesignedtocapture
ofpastvaluesinthepredictionprocess.(ε)(t)representsthe
|                 |         |                  |                 |             |               | and       | interpret | the       | recurring | seasonal      | patterns   | present            | within       |
| --------------- | ------- | ---------------- | --------------- | ----------- | ------------- | --------- | --------- | --------- | --------- | ------------- | ---------- | ------------------ | ------------ |
| error term      | at time | t, encapsulating | the             | discrepancy | between       |           |           |           |           |               |            |                    |              |
|                 |         |                  |                 |             |               | the data. | Within    | this      | array     | of parameters |            | are considerations |              |
| the predicted   | value   | generated        | by the          | AR model    | and the       |           |           |           |           |               |            |                    |              |
|                 |         |                  |                 |             |               | on the    | seasonal  | interval, |           | with the      | capability | to                 | proficiently |
| actual observed |         | value at         | that time step. | This        | term reflects |           |           |           |           |               |            |                    |              |
|                 |         |                  |                 |             |               | model     | and       | predict   | seasonal  | variances     | across     |                    | various data |
theunpredictabilityorrandomnessinherentinthetimeseries
|     |     |     |     |     |     | contexts | [29]. | While | SARIMA | models | prove | advantageous |     |
| --- | --- | --- | --- | --- | --- | -------- | ----- | ----- | ------ | ------ | ----- | ------------ | --- |
data.InthecontextoftheARIMAmodel,theparameter‘d’
|     |     |     |     |     |     | for STLF |     | endeavours | within | power | systems | characterized |     |
| --- | --- | --- | --- | --- | --- | -------- | --- | ---------- | ------ | ----- | ------- | ------------- | --- |
signifiestheprocessofdifferencing.Thetimeseriesforthe
|     |     |     |     |     |     | by pronounced |     | seasonal |     | variations, | such | as load | periods |
| --- | --- | --- | --- | --- | --- | ------------- | --- | -------- | --- | ----------- | ---- | ------- | ------- |
first-orderdifferenceis:
withdailyorweeklypeaks,theyarenotwithoutlimitations.
(cid:49)Y( )= Y( )−Y( −1) Analogous to ARIMA constructs, SARIMA configurations
(2)
|     |     |     |     |     |     | are predicated |     | on  | a stationary | sequence |     | and | demonstrate |
| --- | --- | --- | --- | --- | --- | -------------- | --- | --- | ------------ | -------- | --- | --- | ----------- |
Additional stratifications of differencing can be achieved deficiencies in comprehensively delineating the nonlinear
by iteratively executing the differencing maneuver on a interdependencies between load dynamics and various con-
datasetpreviouslymodifiedbyaninitialdifferencing,thereby tributoryelements[30].Additionally,themodeldemandsan
| 111862 |     |     |     |     |     |     |     |     |     |     |     |     | VOLUME12,2024 |
| ------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------- |

K.Ullahetal.:STLF:AComprehensiveReviewandSimulationStudy
extensive corpus of historical data to accurately ascertain denotesthesequentialdataattimet,whereascencapsulates
seasonalparameters,whichcouldposedifficultiesfornascent a fixed coefficient. Additionally, (cid:57)(B) is delineated as the
power system infrastructures. The schematic representation moving average operator, while εt embodies the stochastic
ofSARIMAmodelsisillustratedinFigure4. errorconstituent.
These models are delineated by three core parame- •ComponentfortheDifferencing(I):
ters: ℘,∂, governing the non-seasonal facets, alongside
P,D, Q, which dictate the seasonal components. This (1−B) X t = Y(t) (7)
schema℘isallocatedtorepresenttheautoregressiveorder,∂ Inthisformulation,thenotation(1−B) characterizesthe
isemployedtospecifytheextentofdifferencing,and isuti- differencingoperator,whileY(t)denotesthetimeseriesthat
lizedtodefinethemovingaverageorderforthenon-seasonal hasbeentransmutedviadifferencing.
segment. Similarly, within the SARIMA architecture, the •ComponentforMA
parameters P, D, and Q correspond to the order of autore-
gression, the degree of differencing, and the order of the X t = U+ 1 ζ( −1)......+ ϱ ζ( −ϱ) (8)
movingaverage,respectively,eachtailoredtoaddressthesea- Within this schema, U designates the arithmetic mean of
sonalnuancesofthemodel.TheprocessoffittingaSARIMA
the series while encapsulates the coefficients correlated
i
model encompasses a series of methodical steps. Initially,
withthemovingaverage(MA)component.
model parameters undergo maximum likelihood estimation, •ComponentforSAR
a sophisticated statistical method aimed at discerning the
mostappropriatevaluesfor℘,∂, P,D, Qthatoptimizethe (cid:50) (B )Y
t
= ψ (B )ε
t
(9)
possibilityoftheperceiveddataset[49].Afterparameteresti- Withinthisdelineation,(cid:50) (B )isidentifiedastheseasonal
mation, the model is fitted to the dataset utilizing advanced autoregressive operator, whereas ψ (B ) characterizes the
forecastingtechniques.
seasonalmovingaverageoperator.
•ComponentforSeasonaldifferencing
(1−B )DY =Z (10)
t t
whereZ denotestheseasonallydifferencedtimeseries,the
t
seasonaldifferencingoperatorisrepresentedby(1−B )D.
•ComponentSMA
Y =(cid:56) ε (t − )+...+Z (cid:56) Qε(t −(cid:56) )
t s t t s s
(11)
where(cid:56) arethecoefficientsfortheseasonalmovingaver-
si
agecomponent.
Combiningtheseelements,theequationfortheSARIMA-
basedmodelcanbearticulatedasfollows:
ϑ(B)ϑ (cid:0) Bs(cid:1) (1−B)D(1− Bs)DX =c+(cid:57)(B)(cid:57) (Bs)εt
s t s
(12)
•ARIMAVSSARIMAMODEL
While comparing both models, it may be noted that,
in short-term load forecasts, both ARIMA and SARIMA
models have their own merits and demerits [31]. ARIMA
FIGURE4. SARIMAModelapproach.
provessuperiorbecauseitisfarmoreeconomicalwithfewer
This tactical methodology leverages the model to fore- parameters, particularly when the load data is non-seasonal
cast future time intervals utilizing historical datasets. The or has minimal seasonality. It captures the relative change
following are the formulas delineating the facets of the over a period, trends, cycles, and even random fluctuation,
SARIMA model, which include the Integrated (I), Seasonal helpingtogiveaverygoodforecastinstableandnon-periodic
MovingAverage(SMA),MA,SeasonalIntegrated(SI),AR, environments. On the set of its drawbacks, the main disad-
andSeasonalAutoregressive(SAR),alongsidethecomposite vantage can be considered an inability of ARIMA to model
equation. seasonality, which can become an important problem while
•ComponentfortheAutoregressive(AR): consideringsuchloadpatternsthatdemonstrateclearcyclical
fluctuations in the loading and demand during a day or a
ϑ(B)X = c+ (cid:57)(B)∈ (6)
t t week.
Inexpression(6),ϑ(B)isdelineatedastheautoregressive SARIMAisalittlespecialized,withseveralextraparam-
operator,withBsignifyingthebackshiftoperator.Here,X eters,particularlyforseasonality.Duetoitsabilitytomodel
t
VOLUME12,2024 111863

K.Ullahetal.:STLF:AComprehensiveReviewandSimulationStudy
TABLE1. ComparisonanalysisofARIMAandSARIMAmodels[31]. calibrating an ES model encompasses multiple stages. Ini-
|     |     |     |     |     |     |     | tially, | the baseline | and trend | estimates |     | are derived | from the |
| --- | --- | --- | --- | --- | --- | --- | ------- | ------------ | --------- | --------- | --- | ----------- | -------- |
earlyobservationsinthetimeseries.Subsequently,theseesti-
matesarerecurrentlyrefinedforeachadditionalobservation
byemployingtheequationsoutlinedbelow:
|     |     |     |     |     |     |     | L(t)= | σ×Y( | )+(1−σ)×(L( |     |     | −1)+I( | −1)) |
| --- | --- | --- | --- | --- | --- | --- | ----- | ---- | ----------- | --- | --- | ------ | ---- |
(13)
|     |     |     |     |     |     |     |     | T(  | β( )×((L( | )−L( | −1))+(1−β)×I |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --------- | ---- | ------------ | --- | --- |
)=
(14)
|            |             |      |             |           |           |        | Here,L( |            | )capturesthelevelofthedataataparticulartime |        |        |            |       |
| ---------- | ----------- | ---- | ----------- | --------- | --------- | ------ | ------- | ---------- | ------------------------------------------- | ------ | ------ | ---------- | ----- |
| and factor | in seasonal |      | variations, | SARIMA    | is highly | appli- |         |            |                                             |        |        |            |       |
|            |             |      |             |           |           |        | and     | translates | the current                                 | status | of the | phenomenon | under |
| cable in   | short-term  | load | forecasting | scenarios | where     | load   |         |            |                                             |        |        |            |       |
study,whereasT(
)depictsthetrend,describingtherateof
datacontainsstrongseasonalitycharacteristics,suchaspeak
changeofacertainoccurrence.
| loading | during | certain | hours | or certain | days. Since | these |     |     |     |     |     |     |     |
| ------- | ------ | ------- | ----- | ---------- | ----------- | ----- | --- | --- | --- | --- | --- | --- | --- |
recurringseasonalvariationscanbemodeled,SARIMAmod-
| els are | generally | more | accurate | than | ARIMA models | in  |     |     |     |     |     |     |     |
| ------- | --------- | ---- | -------- | ---- | ------------ | --- | --- | --- | --- | --- | --- | --- | --- |
similarcases.However,duetothecomplexityofSARIMA,
theparametersneedtobetuned,andsufficientdatashouldbe
obtainedtoavoidoverfitting.
3) MODELSWITHEXPONENTIALSMOOTHING
| Exponential | Smoothing |     | (ES) | models | are predictive | algo- |     |     |     |     |     |     |     |
| ----------- | --------- | --- | ---- | ------ | -------------- | ----- | --- | --- | --- | --- | --- | --- | --- |
rithmswithinthetimeseriesdomain,utilizingexponentially
| weighted    | averages        | of            | antecedent | observations  | to           | project |          |                   |     |     |     |     |     |
| ----------- | --------------- | ------------- | ---------- | ------------- | ------------ | ------- | -------- | ----------------- | --- | --- | --- | --- | --- |
| forthcoming | values.         | Adjustability |            | within        | these models | is      |          |                   |     |     |     |     |     |
| achieved    | by manipulating |               | the        | smoothing     | constant,    | which   |          |                   |     |     |     |     |     |
|             |                 |               |            |               |              |         | FIGURE5. | ESmodelprincipal. |     |     |     |     |     |
| governs     | the weight      | allocations   |            | to historical | data         | points. |          |                   |     |     |     |     |     |
ESmodelsencompassamultitudeofsophisticatedvariants,
|     |     |     |     |     |     |     | Therefore, |     | once the level | and | trend | estimates have | stabi- |
| --- | --- | --- | --- | --- | --- | --- | ---------- | --- | -------------- | --- | ----- | -------------- | ------ |
suchasHolt’sLinearExponentialSmoothing(Holt),Simple
lized,itcanforecastfutureperiodswithevenmoreaccurate
Exponential Smoothing (SES), and Holt-Winters Seasonal and precise ES models. The projection for the upcoming
| Exponential | Smoothing |     | (HW) | [32]. SES | models apply | just |        | +   |            |            |     |             |           |
| ----------- | --------- | --- | ---- | --------- | ------------ | ---- | ------ | --- | ---------- | ---------- | --- | ----------- | --------- |
|             |           |     |      |           |              |      | period | 1   | is derived | by summing |     | the current | level and |
one index of smoothing, which helps attain load data based trendcomponents,aspertheequation:Theprojectionforthe
onobservations.Holtmodelsincludeanothercoefficient,g, upcoming period + 1 is derived by summing the current
thatdealswiththeseries’slineartrends.WhereasHWmodels
levelandtrendcomponents,aspertheequation:
definethetrendandcontaintheparametersthataccountfor
|                                                     |          |              |     |             |             |     |     |     | F( +1)= | L(  | )+T( | )   |      |
| --------------------------------------------------- | -------- | ------------ | --- | ----------- | ----------- | --- | --- | --- | ------- | --- | ---- | --- | ---- |
| seasonality,theapproachusedinthemodelissuperiorwhen |          |              |     |             |             |     |     |     |         |     |      |     | (15) |
| analyzing                                           | periodic | fluctuations |     | in the load | data. These | HW  |     |     |         |     |      |     |      |
modelsareespeciallysuitableforSTLFinsystemscharacter- 4) MODELSFORGENERALIZEDLINEARSTRUCTURE
izedbyconsistenttrendsanddefiniteseasonalpatterns[33]. GLM is a large and systematic class of advanced statistical
Itcanbeusedinreal-timepredictionandisnotascomputa- techniques exploring the weak nonlinear relation between
tionallydemandingastheARIMAandSARIMAmodels;ES load profile and influential factors. Various extensions of
modelsusearelativelysmallamountofhistoricaldata.They GLMs exist, including the Poisson regression model, the
can also capture nonlinear associations with load data and Negative Binomial regression model, the Gamma model,
othereffectslikeweatherconditionsandpopulationdensity. and others [34]. GLMs extend the linear regression model
However,loaddataisassumedtoremainstationaryinthecase by providing the ability to manage the non-normal depen-
ofESmodels,implyingthattheaccuracyofESmodelswhen dency of the response. The benefits of GLMs are that they
itcomestonon-stationaryloadinpowersystemisaffected. can handle highly flexible load patterns due to the change
The ES models’ operation process flow is depicted in in load behaviour with meteorological parameters and/or
Fig.5.TheESframeworkischaracterizedbytwokeyparam- occupancy patterns based on the link function. This func-
eters:alphaandbeta.Thefirstpaperselectedfortheanalysis tion provides an estimated value of the dependent variable
is the work of Fountain and colleagues, published in the as E(y) = f(X ,X ,............X from the predictor
|     |     |     |     |     |     |     |     |     | 1 2 |     |     | k   |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
JournalofMidwifery&Women’sHealthin2018.Thevalue variables X ,X ,............X [35]. Likewise, in STLF,
|     |     |     |     |     |     |     |     | 1   | 2   |     | k   |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
of the alpha parameter defines the primary importance of the primary focus of most GM applications is the Poisson
the last value, while the beta parameter sets the importance regressionmodel,themostcommontypeofGLM,wherethe
of the trend factor in the given model. The procedure for load count is the dependent variable to the relevant control
| 111864 |     |     |     |     |     |     |     |     |     |     |     | VOLUME12,2024 |     |
| ------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------- | --- |

K.Ullahetal.:STLF:AComprehensiveReviewandSimulationStudy
variables.ThePoissonregressionmodelpresupposesthatthe response variable’s baseline level, whereby all the predictor
describedresponsevariableisPoissondistributedandmaps variables have been set to zero. Moreover, α refers to the
1
themeanofthisvariablethroughalogarithmiclinkfunction coefficient that corresponds to the predictor variable, which
to the set of predictors. Indeed, the Poisson regression is is X in this case, hence showing the degree of its impact
1
particularly adapted to power systems that involve counting onthemeanoftheresponsevariable.Noveltyisdeemedthe
data,whichmeansthenumberofworkingorexistingappli- dispersionparameterκ,whichbringsvariabilitytothemodel.
ancesordevices.Initsownright,onemustacknowledgethe Itcaneitherbemadefixedsoitonlyoffersafixedmeasure
function that PCA serves as a powerful tool for capturing of dispersion or can be estimated depending on the predic-
complex nonlinear relationships between loads’ variability tor variables, which provides the possibility of changing in
andarangeofpotentialdrivers[36].ThePoissonregression response to changes in the data used to create the model.
model, employing a log-linear framework, formulates the Whenκ ismodeledasafunctionofthepredictors,itfollows
relationshipbetweenthepredictorvariablesλandtheantic- alogarithmicequation:Whenκ ismodeledasafunctionof
thepredictors,itfollowsalogarithmicequation:
| ipated count | X.  | This | relationship | can | be expressed |     | as The |     |     |     |     |     |
| ------------ | --- | ---- | ------------ | --- | ------------ | --- | ------ | --- | --- | --- | --- | --- |
Poissonregressionmodel,employingalog-linearframework,
|     |     |     |     |     |     |     |     |     | Log(κ)= | ρ +ρ |     | (18) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ------- | ---- | --- | ---- |
0 1 1
| formulates | the | relationship |     | between | the predictor | variables |     |     |     |     |     |     |
| ---------- | --- | ------------ | --- | ------- | ------------- | --------- | --- | --- | --- | --- | --- | --- |
ρ
λ and the anticipated count X. This relationship can be Here, term provides the intercept for the dispersion
0
describedas: componentwherebythevalueofρsignifiesthegeneralbasal
levelofdispersion.Atthisstage,ρ
|     |     | Logξ |     | α +α | X   |     |      |                                                     |     | 1 representstheestimator |     |     |
| --- | --- | ---- | --- | ---- | --- | --- | ---- | --------------------------------------------------- | --- | ------------------------ | --- | --- |
|     |     |      | =   |      |     |     | (16) |                                                     |     |                          |     |     |
|     |     |      |     | 0 1  | 1   |     |      | of whichshowsitseffectonthevariabilityoftheresponse |     |                          |     |     |
1
In this context, α refers to the intercept, whereas α_1 variable.Gammaregressionisidentifiedindetailasoneofthe
0
X
refers to the coefficient estimate for . Another advanced significant tools in the Generalized Linear Models category
1
GLM that is employed in STLF is the Negative Binomial specifically utilized in Short-Term Load Forecasting during
Regressionmodel,whichfollowstheformula:Derivedfrom power systems. Since the response variable is an instance
Poissonregressionmodels,itismostappropriateinworking ofthegammadistribution,thisregressionmethodbrilliantly
with over-dispersed count data by including a prevalence transforms continuous load data and the dependent variable
parameter by thus improving preciseness and reliability in intermsofthepredictorvariable.
| conditions | of high | data | variability. | This | is because | the | vari- |     |        |     |     |      |
| ---------- | ------- | ---- | ------------ | ---- | ---------- | --- | ----- | --- | ------ | --- | --- | ---- |
|            |         |      |              |      |            |     |       |     | G(U)=η |     |     | (19) |
anceoftheresponsevariableisgenerallymorethanitsmean
and is quite common for load datasets considering power In(19),italsodefinesacomplexinteractionbetweenthe
systems due to high variability [37]. The logarithmic link mean of the response variable U and the linear predictor η
viaanappropriatelinkfunctionG.Theintegrationofthelink
functionusedinthenegativebinomialregressionmodelisan
advanced statistical method useful in accurately measuring functionwiththelinearpredictorresultsinacomprehensive
equationthatencapsulatesthecomplexinterplaybetweenthe
| the complex | relationship |     | of  | the response | variable | with | the |     |     |     |     |     |
| ----------- | ------------ | --- | --- | ------------ | -------- | ---- | --- | --- | --- | --- | --- | --- |
predictorvariablesincasetheexpectedvalueoftheresponse responsevariableandthepredictorvariables:Theintegration
cannot be assumed to be a linear function of the predictor ofthelinkfunctionwiththelinearpredictorresultsinacom-
variables.Thisrelationshipisexplainedproficientlyinlinear prehensiveequationthatencapsulatesthecomplexinterplay
algebrabydescribingtheassociationbetweenthepredictors betweentheresponsevariableandthepredictorvariables:
and the outcome in terms of a linear combination, thereby G(U)= ρ +ρ X +ρ X +...+ρ X
|           |        |              |     |        |      |           |      |     | 0 1 1 | 2 2 | P P | (20) |
| --------- | ------ | ------------ | --- | ------ | ---- | --------- | ---- | --- | ----- | --- | --- | ---- |
| providing | a rich | appreciation |     | of how | each | predictor | con- |     |       |     |     |      |
tributes to the prediction. The difference in this model lies GLMsboastcomputationalefficiencyandtheflexibilityto
accommodatediversepredictorvariables,encompassingboth
| in including | one | more | dispersion | parameter |     | to reduce | the |     |     |     |     |     |
| ------------ | --- | ---- | ---------- | --------- | --- | --------- | --- | --- | --- | --- | --- | --- |
densityoftheresponsevariables.Thisparametercontributes categorical and interaction terms. Furthermore, GLMs fur-
|            |            |     |        |        |         |                  |     | nish interpretable | coefficients, | facilitating | the identification |     |
| ---------- | ---------- | --- | ------ | ------ | ------- | ---------------- | --- | ------------------ | ------------- | ------------ | ------------------ | --- |
| additional | robustness |     | to the | method | because | it is inherently |     |                    |               |              |                    |     |
possible to have variability within the datasets used in real- ofpivotalpredictorvariablesandquantifyingtheirimpacton
world applications. Indeed, incorporating the third variable, theload[38].However,asignificantdrawbackofGLMslies
intheirassumptionregardingthedistributionoftheresponse
| which accounts |     | for dispersion, |     | enhances | the | model’s | capa- |     |     |     |     |     |
| -------------- | --- | --------------- | --- | -------- | --- | ------- | ----- | --- | --- | --- | --- | --- |
bilities by ensuring that the model can capture fine details variable, which may not universally apply to power system
of the data sets. The articulation of the dispersion model is contexts[39].Additionally,theaccurateestimationofmodel
as follows: The articulation of the dispersion model is as parametersviaGLMsoftennecessitatesasubstantialvolume
follows: ofhistoricaldata,presentingchallengesfornewlyestablished
powersysteminstallationswithlimiteddataavailability[40].
|     |     | Log(ϕ)= |     | α +α | X   |     |      |     |     |     |     |     |
| --- | --- | ------- | --- | ---- | --- | --- | ---- | --- | --- | --- | --- | --- |
|     |     |         |     | 0    | 1 1 |     | (17) |     |     |     |     |     |
Inthiscontext,ϕ belongstothemathematicalexpectation B. MODELSWITHINTELLIGENTTECHNIQUES
of the response variable, mean, which is a primary measure SophisticatedmethodologiesinSTLFencompassarangeof
ofthecentraltendencyofanysetofdata.Ontheotherhand, prognosticativetechniquesthatemploycutting-edgecompu-
thesymbolα
0 representthemodelinterceptrepresentingthe tational strategies, including artificial intelligence, machine
| VOLUME12,2024 |     |     |     |     |     |     |     |     |     |     |     | 111865 |
| ------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------ |

K.Ullahetal.:STLF:AComprehensiveReviewandSimulationStudy
learning, and various optimization algorithms, to anticipate wheresignrepresentsthesignumfunction,whichassignsthe
near-future electrical demands. These advanced models are classlabelaccordingtothesignofitsargument.Themargin
intricatelydesignedtodiscernandinterpretcomplexpatterns, foreachdatapointisdeterminedinthefollowingmanner:
| nonlinear  | interdependencies, |               | and | multifaceted |     | relationships |     |     |     |     |     |     |      |
| ---------- | ------------------ | ------------- | --- | ------------ | --- | ------------- | --- | --- | --- | --- | --- | --- | ---- |
|            |                    |               |     |              |     |               |     |     | Y(  | .   | +   |     |      |
|            |                    |               |     |              |     |               |     |     |     | i   | i ) |     | (23) |
| within the | load               | data, thereby |     | enhancing    | the | precision and |     |     |     |     |     |     |      |
dependability of forecasts [41]. Figure 1 delineates several Y
|     |     |     |     |     |     |     | where, In | the world | of  | binary-defined |     | classes | i represents |
| --- | --- | --- | --- | --- | --- | --- | --------- | --------- | --- | -------------- | --- | ------- | ------------ |
prominentintelligentmodelsemployedinSTLF,whichhave
theithdatapoint’sclassification,oftenas−1or+1.Inturn,
beendiscussedindetail. denotestheweightvectorthatisorthogonaltothedefining
|     |     |     |     |     |     |     | hyperplane,whereas |     | i referstofeaturesfortheithdatasam- |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ------------------ | --- | ----------------------------------- | --- | --- | --- | --- |
1) METHODSWITHSUPPORTVECTORMACHINE ple.Moreover, thebiastermistheimportantfunctionthat
i
APPROACH
shiftsthedelineatingboundaryfromtheorigin.Thenotation
AcriticalmachinelearningarchetypeforSTLFistheSupport . representsthedotproductbetweenthenetworkweight
i
Vector Machine (SVM), an advanced supervised learning vectorwandthefeaturevector ,whichisarepresentation
i
| framework | proficient | in  | addressing |     | linear | and nonlinear |                   |     |      |       |            | .   |             |
| --------- | ---------- | --- | ---------- | --- | ------ | ------------- | ----------------- | --- | ---- | ----- | ---------- | --- | ----------- |
|           |            |     |            |     |        |               | of the projection |     | of i | about | the vector | In  | the context |
associations between the electrical load and its influencing oftheSVMparadigm,thefundamentalaim,therefore,isto
| determinants. | SVMs | are | remarkably |     | versatile | in handling |     |     |     |     |     |     |     |
| ------------- | ---- | --- | ---------- | --- | --------- | ----------- | --- | --- | --- | --- | --- | --- | --- |
understandhowtoobtainthebiggestmarginand,atthesame
an extensive spectrum of predictor variables, which include time,ensureallpatternvectorsareclassifiedcorrectly.This
categoricalvariablesandinteractionterms[42].Furthermore, optimization is made by controlling the size of the weight
these models are adept at mitigating issues related to noisy |
|     |     |     |     |     |     |     | vector, which | is  | represented | as  | |, where | it is | known that |
| --- | --- | --- | --- | --- | --- | --- | ------------- | --- | ----------- | --- | -------- | ----- | ---------- |
data by applying a kernel function that transposes the data the distance between the hyperplane and the data point is
| intoahigher-dimensionalrealmforenhancedanalysis.SVMs |     |     |     |     |     |     |           |              |     | |   |          |         |              |
| ---------------------------------------------------- | --- | --- | --- | --- | --- | --- | --------- | ------------ | --- | --- | -------- | ------- | ------------ |
|                                                      |     |     |     |     |     |     | inversely | proportional | to  | |.  | Building | on this | concept, the |
havebeenwidelyemployedinpredictingloaddependenton SVMismeanttolookfortheperfecthyperplanethatnotonly
the/power system variables like temperature, humidity, and partitions the data points according to their classes but also
time.InthecontextofthedomainSTLF,itisunobtrusively
|     |     |     |     |     |     |     | does it with | the | largest | margin, | measured | as the | distance of |
| --- | --- | --- | --- | --- | --- | --- | ------------ | --- | ------- | ------- | -------- | ------ | ----------- |
incorporated to predict the future load or demand on elec- thishyperplanefromthenearestdatapointofanyoftheclass.
tricity for up to one week. However, other intervals, such Thus, by minimizing | |, the classifying hyperplane of the
as a few hours, can also be used. In general, an SVM aims SVM increases the said margin, and this, in turn, improves
to find the best hyperplane that offers the maximum likely the overall performance of the model in terms of its ability
separationoftwoclassesofregressiondatasets.Inthetwo-
togeneralize.ThisprocessmakesitpossiblefortheSVMto
dimensional case, it appears as a hyperplane, which in this fulfiltheoptimalconditionofmaximizingthemarginwhile
context represents a line that separates the data distinctly minimizingtheclassificationerrorsand,hence,arrivingatan
| into two | separate | categories. | In  | ad-dimensional |     | geometries, |     |     |     |     |     |     |     |
| -------- | -------- | ----------- | --- | -------------- | --- | ----------- | --- | --- | --- | --- | --- | --- | --- |
efficientandaccurateclassificationsystem.
| a hyperplane | is  | a sub-space | born | of  | the containment | space |     |     |     |     |     |     |     |
| ------------ | --- | ----------- | ---- | --- | --------------- | ----- | --- | --- | --- | --- | --- | --- | --- |
1
| andisreducedbyonedimension.Amarginrepresentsthedis- |     |     |     |     |     |     |     |     |     | =   |     |     |      |
| --------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---- |
|                                                     |     |     |     |     |     |     |     |     |     | M   |     |     | (24) |
| |
| tance between |     | the hyperplane |     | and the | neighbours | of distant |     |     |     |     |     |     |     |
| ------------- | --- | -------------- | --- | ------- | ---------- | ---------- | --- | --- | --- | --- | --- | --- | --- |
classesofpointsreferredtoassupportvectors.Thesevectors The optimization conundrum for an SVM can be articu-
| are essential | in  | the structure | and | position | of the | hyperplane |     |     |     |     |     |     |     |
| ------------- | --- | ------------- | --- | -------- | ------ | ---------- | --- | --- | --- | --- | --- | --- | --- |
latedasaconstrainedoptimizationquandary.
| as they | provide | its support. | The | fundamental |     | objective of |     |     |     |     |     |     |     |
| ------- | ------- | ------------ | --- | ----------- | --- | ------------ | --- | --- | --- | --- | --- | --- | --- |
1
an SVM revolves around optimizing this margin to ensure Min= ×| |2 (25)
2
theprecisecategorizationofdataelements.Withinadataset
|            |          |      |         |     |       |              | Subjecttothecondition:Y |     |     | (   | . + | )≥1foreachifrom |     |
| ---------- | -------- | ---- | ------- | --- | ----- | ------------ | ----------------------- | --- | --- | --- | --- | --------------- | --- |
| containing | labelled | data | pairs ( | , ) | where | represents a |                         |     |     | i   | i   |                 |     |
|            |          |      |         | i i |       | i            |                         |     |     |     |     |                 |     |
vectorinn-dimensionalrealspaceR and designatesthe 1to .Thissituationleadstoaconvexquadraticprogramming
|     |     |     |     | n   | i   |     |         |             |             |     |         |        |              |
| --- | --- | --- | --- | --- | --- | --- | ------- | ----------- | ----------- | --- | ------- | ------ | ------------ |
|     |     |     |     |     |     |     | problem | with linear | constraints |     | imposed | on it. | This task is |
binaryclasslabels(−1,1),thedelineationofthehyperplane
isestablishedmathematically[43]. a challenge that is solved with the help of finding extrema
|     |     |     |     |     |     |      | by using | Lagrange | multipliers, |     | which thus | leads | to what is |
| --- | --- | --- | --- | --- | --- | ---- | -------- | -------- | ------------ | --- | ---------- | ----- | ---------- |
|     |     |     | . + | = 0 |     | (21) |          |          |              |     |            |       |            |
calledthedualproblem.Thedualformulationpresentsamore
|         |          |           |     |            |                  |     | practically | applicable | approach |     | to deal | with the | problem of |
| ------- | -------- | --------- | --- | ---------- | ---------------- | --- | ----------- | ---------- | -------- | --- | ------- | -------- | ---------- |
| In this | context, | signifies |     | the vector | of coefficients, |     |             |            |          |     |         |          |            |
optimizationintegratedinSVM,particularlyincaseswhere
| encapsulatesthevectorofinputfeatures,and |     |     |     |     |     | isidentified |     |     |     |     |     |     |     |
| ---------------------------------------- | --- | --- | --- | --- | --- | ------------ | --- | --- | --- | --- | --- | --- | --- |
. kernel functions are introduced in nonlinear situations [44].
| astheintercept.Thescalarproduct |     |     |     |     | calculatestheextent |     |     |     |     |     |     |     |     |
| ------------------------------- | --- | --- | --- | --- | ------------------- | --- | --- | --- | --- | --- | --- | --- | --- |
ThestepsinvolvedinSTLFareasfollows,andaflowdiagram
| oftheprojectionof |     | inthedirectionorientedby |     |     |     | .Thetask |     |     |     |     |     |     |     |
| ----------------- | --- | ------------------------ | --- | --- | --- | -------- | --- | --- | --- | --- | --- | --- | --- |
isgiveninFigure6.
| is to determine |     | the most | advantageous |     | values | for and |       |            |       |         |           |        |         |
| --------------- | --- | -------- | ------------ | --- | ------ | ------- | ----- | ---------- | ----- | ------- | --------- | ------ | ------- |
|                 |     |          |              |     |        |         | • The | first step | is to | collect | past load | demand | data on |
thateffectivelymaximizetheseparation,ormargin,between
electricity,othersystemicparameters,externalenvironmental
thetwocategoricallydistinctclasses.Thediscriminativecri-
conditions,anddaysoftheweekandtime.Itisthenfollowed
terionforcategorizationis
|     |     |           |     |     |     |     | by a cleanse | and | preprocess | step | to eliminate |     | or minimize |
| --- | --- | --------- | --- | --- | --- | --- | ------------ | --- | ---------- | ---- | ------------ | --- | ----------- |
|     |     | ( )=sign( |     | . + |     |     |              |     |            |      |              |     |             |
) (22) anyinconsistencies,noise,ormissingvaluesinthedata.This
| 111866 |     |     |     |     |     |     |     |     |     |     |     |     | VOLUME12,2024 |
| ------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------- |

K.Ullahetal.:STLF:AComprehensiveReviewandSimulationStudy
|     |     |     |     |     |     | prediction | can         | then be    | evaluated | on another    | data   | set that   |
| --- | --- | --- | --- | --- | --- | ---------- | ----------- | ---------- | --------- | ------------- | ------ | ---------- |
|     |     |     |     |     |     | was not    | used during | the        | training. | An examiner   |        | can assess |
|     |     |     |     |     |     | the model  | based       | on factors |           | like standard | error, | R square,  |
coefficientofdetermination,andaccuracyusingMAE,MSE,
orMAPE.
|     |     |     |     |     |     | • It is | worth | mentioning |     | that, with new | input | data, the |
| --- | --- | --- | --- | --- | --- | ------- | ----- | ---------- | --- | -------------- | ----- | --------- |
proposedSVMmodelthatistrained,validated,andtestedcan
provideafive-minuteSTLF.Thedevelopedmodelcalculates
|     |     |     |     |     |     | the required | attributes |     | for the | forecast period | and | gives the |
| --- | --- | --- | --- | --- | --- | ------------ | ---------- | --- | ------- | --------------- | --- | --------- |
FIGURE6. Machinesystembasedonsupportvectormechanism.
expecteddemandforelectricityload.
|     |     |     |     |     |     | 2) DECISIONTREE |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --------------- | --- | --- | --- | --- | --- | --- |
isusuallydonethroughthenormalizationofstandardization Another suitable approach in business for the STLF is the
methodstoenhancetheperformanceandqualityoftheSVM. Decision Tree (DT), a statistical model specializing in seg-
•Inthenextstep,theattributesrelevanttotheforecasting
|     |     |     |     |     |     | menting | predictor | variables |     | into categorical | or  | continuous |
| --- | --- | --- | --- | --- | --- | ------- | --------- | --------- | --- | ---------------- | --- | ---------- |
enterprise are identified for further assessment solely. This categories,asshowninFig.7.DTsfunctionbydividingthe
stageisparamount,particularlyifunnecessaryfunctionsneg-
predictorvariablesintosubsetsknownastheleafnode.The
ativelyaffectthemodel’sperformance.Also,thereareRFE, trees are connected based on load patterns within the load
correlation reviews, or PCA to identify the features of the prediction or mere hierarchy [45]. Decision trees have also
problemthatwouldbeoptimaltofocuson.
demonstratedfavorableperformanceinpowersystem-related
•Toelaboratefurther,theselectedmodelofSVMiscare- studies,especiallyinforecastingloadvariationsfromweather
fullytrainedontherefineddataandthechosenvariablesonly. characteristics,occupancyratios,andtimefactors.Therefore,
SVMs aim to obtain the best hyperplane that distinguishes divisions,lame,andsplittingstandardsareattheheartofthe
the studied data sets into distinct categories or classes. The decisiontree[46],[47].
| model is | given for predicting | continuous |     | values to | be the |           |                |     |        |              |         |      |
| -------- | -------------------- | ---------- | --- | --------- | ------ | --------- | -------------- | --- | ------ | ------------ | ------- | ---- |
|          |                      |            |     |           |        | Regarding | classification |     | tasks, | data binning | through | met- |
electrical load, given that STLF is naturally a regression ricssuchastheGiniindexorinformationgainisused,making
problem.Itshouldbeunderstoodthatthesekernelfunctions iteasytoclassifythedifferentclasseswithinthedataset.
aredesignedtomaptheinputdatatoaspaceofhigherdimen- •GiniImpurity:Thismetricassessestheheterogeneityof
sionality. It helps when finding an appropriate hyperplane anode(mixofclasses),wherelowerfiguresindicateahigher
| in this expanded | space of | slowly | growing | dimensionality | to  |     |     |     |     |     |     |     |
| ---------------- | -------- | ------ | ------- | -------------- | --- | --- | --- | --- | --- | --- | --- | --- |
degreeofuniformity.TheGiniimpurityforanodeexpressed
separatethepoints. throughclassprobabilities ,isformulatedas:
| • The | SVM model is initially |     | trained using | preprocessed |     |     |     |     |     |     |     |     |
| ----- | ---------------------- | --- | ------------- | ------------ | --- | --- | --- | --- | --- | --- | --- | --- |
X
|          |                      |      |         |                  |     |     |     | G.I= | 1−  | (π)2 |     | (26) |
| -------- | -------------------- | ---- | ------- | ---------------- | --- | --- | --- | ---- | --- | ---- | --- | ---- |
| data, as | discussed in Section | III, | and the | most appropriate |     |     |     |      |     |      |     |      |
attributesareselected.SVMs,asatechnology,aimtoclassify
•InformationGain:Predicatedontheconceptofentropy,
| the data | as aptly as possible | into | well-defined | classes | or  |                 |     |            |     |             |                  |     |
| -------- | -------------------- | ---- | ------------ | ------- | --- | --------------- | --- | ---------- | --- | ----------- | ---------------- | --- |
|          |                      |      |              |         |     | which evaluates |     | the degree |     | of disorder | or indeterminacy |     |
categories.Forexample,whileSTLFisaregressionproblem,
withinagroup,InformationGainiscomputedforanodewith
themodelissettoforecastthecontinuousvaluesforelectrical
|          |                   |             |     |               |     | classprobabilitiesπ |     | as  |     |     |     |     |
| -------- | ----------------- | ----------- | --- | ------------- | --- | ------------------- | --- | --- | --- | --- | --- | --- |
| load. To | achieve this, the | SVM employs |     | what is known | as  |                     |     |     |     |     |     |     |
X
kernels(whichcouldbelinear,polynomial,ortheradialbasis Ent = − ( ×log2)(π) (27)
| kernel function,) | which transforms |     | the input | data into | the |     |     |     |     |     |     |     |
| ----------------- | ---------------- | --- | --------- | --------- | --- | --- | --- | --- | --- | --- | --- | --- |
Informationgain(IG)istheentropydifferencebeforeand
higherdimensionalspace,makingiteasiertoidentifyaplane
afterthedataelementsornodessplit.
ofbestfitthatseparatestheclasses.
| • To    | ensure everyone knows    | that | the SVM  | model       | devel- |      |                                                |     |     |     |     |     |
| ------- | ------------------------ | ---- | -------- | ----------- | ------ | ---- | ---------------------------------------------- | --- | --- | --- | --- | --- |
|         |                          |      |          |             |        | IG = | Entropy(parent)−weightedsum(Entropy(children)) |     |     |     |     |     |
| oped to | solve different problems |      | performs | well, it is | tested |      |                                                |     |     |     |     |     |
(28)
| using measures | like cross-validation. |     | Splitting | the data | into |     |     |     |     |     |     |     |
| -------------- | ---------------------- | --- | --------- | -------- | ---- | --- | --- | --- | --- | --- | --- | --- |
thetrainingandthevalidationsetisperformedinthisprocess, To increase the information sought to facilitate the for-
andtheformerModeistrainedwhilethelattermodeistested. mation of equally proportioned descendant nodes, the most
Thishelpstodeterminethemodel’sperformanceapartfrom frequent technique used in regression efforts IX is using
thetestdatasetandcheckforthemodel’sabilitytoperform MeanSquaredError(MSE)tosplit.MSEisexpressedasthe
wellacrosstheotherdataset. meanofthesquareddifferencebetweenactualandestimated
•
Moreover, the present enhancements include the cost targets;itservesasakeycriterionunderlyingeachpartition’s
factor, the type of kernel function to be utilized, and the goal to minimize error. To train the decision tree model for
parametersassociatedwiththekernelsthatareincorporated predictive analysis, it is crucial to correctly obtain previous
inthebestestimationforsolvingthespecificSTLFchallenge. electricity load data and other independent variables like
• Once a particular model, such as the SVM model, has weather parameters, day and month of the week, and time,
been trained and calibrated, its performance in terms of andaddressanyanomaliesormissingvalues.Pre-processing
| VOLUME12,2024 |     |     |     |     |     |     |     |     |     |     |     | 111867 |
| ------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------ |

K.Ullahetal.:STLF:AComprehensiveReviewandSimulationStudy
|     |     |     |     |     |     |     | for its capability |     | to refine | the | precision | of load | forecasts. |
| --- | --- | --- | --- | --- | --- | --- | ------------------ | --- | --------- | --- | --------- | ------- | ---------- |
Themethodsystematicallyincorporatessuccessivedecision
|     |     |     |     |     |     |     | trees, each   | tasked       | with rectifying |           | the             | errors identified | in its |
| --- | --- | --- | --- | --- | --- | --- | ------------- | ------------ | --------------- | --------- | --------------- | ----------------- | ------ |
|     |     |     |     |     |     |     | predecessors, | thereby      | constructing    |           | a comprehensive |                   | model  |
|     |     |     |     |     |     |     | capable       | of capturing | the             | intricate | nonlinear       | dependencies      |        |
betweentheloadanditsinfluencingvariables[49].
FIGURE7. Blockdecisiontreediagram.
techniquessuchasselectionbyusingRFE,correlationanal-
| ysis,orInformation |     | gainhelpremoveattributefeaturesthat |         |     |           |         |     |     |     |     |     |     |     |
| ------------------ | --- | ----------------------------------- | ------- | --- | --------- | ------- | --- | --- | --- | --- | --- | --- | --- |
| may distort        | the | classification                      | result. | The | splitting | is done |     |     |     |     |     |     |     |
FIGURE8. Randomforestalgorithm.
stepwiseintheprocessofmodeling,wherethedataisdivided
into segments to minimize impurity, as measured by MSE, Figure 9 illustrates the gradient boosting algorithm pro-
untilthemodelreachesthepredeterminedconditionforter-
cess,whichleveragestrainingdatatopinpointweaklearners,
minatingtheprocessofbuildingatree,suchasthemaximum
|     |     |     |     |     |     |     | enhancing | the accuracy |     | of subsequent |     | predictions. | The |
| --- | --- | --- | --- | --- | --- | --- | --------- | ------------ | --- | ------------- | --- | ------------ | --- |
depth of the tree being achieved. Due to the nature of the sequentialoperationoftherandomforestandgradientboost-
| overfitting | of decision | trees, | indicators |     | for validation | and |     |     |     |     |     |     |     |
| ----------- | ----------- | ------ | ---------- | --- | -------------- | --- | --- | --- | --- | --- | --- | --- | --- |
ingalgorithmsisdelineatedasfollows[50].
| pruning, | like cross-validation |     | or  | cost complexity, |     | are used |     |     |     |     |     |     |     |
| -------- | --------------------- | --- | --- | ---------------- | --- | -------- | --- | --- | --- | --- | --- | --- | --- |
•Theinitialphaseaggregatesaloadofpowerdataalong-
| to enhance | the      | stability      | and performance |          | of the | tree. After |                |             |                   |      |           |           |            |
| ---------- | -------- | -------------- | --------------- | -------- | ------ | ----------- | -------------- | ----------- | ----------------- | ---- | --------- | --------- | ---------- |
|            |          |                |                 |          |        |             | side variables | such        | as meteorological |      |           | data, the | day of the |
| extensive  | training | and subsequent |                 | pruning, | the    | final model |                |             |                   |      |           |           |            |
|            |          |                |                 |          |        |             | week, and      | the diurnal | cycle.            | This | collected | data      | undergoes  |
goes through specific performance evaluation metrics such cleansing and preprocessing to eliminate inconsistencies,
| as MAE, | MSE, | or MAPE. | Once | the decision | tree | model is |     |     |     |     |     |     |     |
| ------- | ---- | -------- | ---- | ------------ | ---- | -------- | --- | --- | --- | --- | --- | --- | --- |
anomalies,orabsentvalues.Notably,featurescalingistypi-
| validated, | the process | of  | short-term | load | forecasting | begins |     |     |     |     |     |     |     |
| ---------- | ----------- | --- | ---------- | ---- | ----------- | ------ | --- | --- | --- | --- | --- | --- | --- |
callysuperfluousforrandomforestssincethedecisiontrees,
| by transforming |     | the input | data | into valid | decision-making |     |     |     |     |     |     |     |     |
| --------------- | --- | --------- | ---- | ---------- | --------------- | --- | --- | --- | --- | --- | --- | --- | --- |
whichserveastheirfoundationallearners,exhibitareduced
criteriaandpassingitthroughthetreestructure,movingfrom
sensitivitytothemagnitudeofinputfeatures.
the root of the tree to a node or leaf point at the end of a •Theproceduralexecutionofrandomforestandgradient
decisionpath,whichistheforecastedelectricityload.
|     |     |     |     |     |     |     | boosting | algorithms | proceeds |     | as follows: | The most | perti- |
| --- | --- | --- | --- | --- | --- | --- | -------- | ---------- | -------- | --- | ----------- | -------- | ------ |
nentattributesfortheforecastingendeavoraremeticulously
3) RANDOMFORESTANDGRADIENTBOOSTING(GB)
|     |     |     |     |     |     |     | selected | to preclude | the | detrimental |     | effects of | extrane- |
| --- | --- | --- | --- | --- | --- | --- | -------- | ----------- | --- | ----------- | --- | ---------- | -------- |
Random Forest (RF) is a refined version of DT developed ous or superfluous features on the model. While random
to reduce sensitivity to data noise and enhance accuracy in forests intrinsically possess the capacity to manage many
loadforecasting.RFsusethebootstrapaggregatingmethod, featuresandautonomouslyevaluatetheirsignificance,apply-
thatis,manydecisiontreesarebuiltusingbootstrapsamples ing domain expertise or methodologies such as RFE and
of the training dataset for arriving at a final decision from correlation analysis can substantially enhance the model’s
| all these | individual | trees, | and outputs | from | all | the trees are | performance. |     |     |     |     |     |     |
| --------- | ---------- | ------ | ----------- | ---- | --- | ------------- | ------------ | --- | --- | --- | --- | --- | --- |
averaged to arrive at the final prediction. This technique is • The model is trained after feature selection for the best
used in certain power system paradigms to forecast load performingrandomforestmodel.Thisalgorithmbuildsmany
changes due to specific factors like temperature, humidity, decisiontreesfromabootstrapsampleinthepresenteddata
and sunlight [48]. The simplified working model of an RF set.Specifically,anindependentrandomsampleoffeaturesis
algorithm is depicted below in Figure 8: In each tree node, selectedatthesplitstageoftreeconstruction.Ithelpsincrease
for a given dataset, ‘m’ number of features are randomly thetreenumberintendedtoimproveamodel’saccuracyand
selected from the total features. Many trees are then re- alsohelpsavoidoverfittingproblemsinthegradient-boosting
| grew, leading | to  | different | predictive | classifications |     | coming | model. |     |     |     |     |     |     |
| ------------- | --- | --------- | ---------- | --------------- | --- | ------ | ------ | --- | --- | --- | --- | --- | --- |
from each of them. The last prediction is the overall con- • This confirms that the random forest model is reliable
sensus, either a simple average or the decision from most in its performance with contemporary datasets due to the
of the above-mentioned classification types [48]. GB is a application of the cross-validation technique. The dataset is
sophisticated ensemble machine learning paradigm known split into the train and validation sets, wherein the entire
| 111868 |     |     |     |     |     |     |     |     |     |     |     | VOLUME12,2024 |     |
| ------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------- | --- |

K.Ullahetal.:STLF:AComprehensiveReviewandSimulationStudy
acceptabilityinvariousforms,includingnumeracy,imagery,
|     |     |     |     |     | or text. | Each node | here | stands | for | a specific | attribute | of the |
| --- | --- | --- | --- | --- | -------- | --------- | ---- | ------ | --- | ---------- | --------- | ------ |
inputdata.
|     |     |     |     |     | • Intermediary |       | Layers: |             | Sitting | between | the input | and |
| --- | --- | --- | --- | --- | -------------- | ----- | ------- | ----------- | ------- | ------- | --------- | --- |
|     |     |     |     |     | output parts,  | these | layers  | incorporate |         | neurons | required  | for |
translatingthecomplexitiesintotheacceptableformatofthe
system.Thearchitectureoftheselayersdeterminesthedepth
ofthemodelandthenumberofneuronswithinthem,which
dictatestheabilityofthemodeltounderstandmorecomplex
patterns.
|     |     |     |     |     | • Terminal |          | Section: | This | final    | component | of the         | MLP |
| --- | --- | --- | --- | --- | ---------- | -------- | -------- | ---- | -------- | --------- | -------------- | --- |
|     |     |     |     |     | framework  | provides | the      | last | outcomes | and       | or predictions | of  |
FIGURE9. Gradientboostingalgorithmicdiagram. theanalysis.Theuseofnodesdependsonthetypeoftaskto
besolvedandwhethertoclassifyimagesintotencategories,
asitisassumedtohavetennodes.
computationprocessisperformedonthefirstsubset,andthe
•NeuronalUnits:Everynodeinthiscomputationalarchi-
resultsaretestedonthesecondone.Thismethodologyallows
tecturetakesininputfromtheearlierlayerofnodes,applies
| evaluation | of the | model’s performance | and | generalization |     |     |     |     |     |     |     |     |
| ---------- | ------ | ------------------- | --- | -------------- | --- | --- | --- | --- | --- | --- | --- | --- |
atransformonthisinput,andthenpassesonthetransformed
abilityonadifferentdataset.
|     |     |     |     |     | input to | the next | layer | of  | nodes. | Fortunately, | containing | a   |
| --- | --- | --- | --- | --- | -------- | -------- | ----- | --- | ------ | ------------ | ---------- | --- |
•
The random forest algorithm contains various tunable non-linearactivationfunctionenablesthesenetworkstofunc-
hyperparameters.Onecanidentifythenumberoftreeswithin
tionandmodelcomplicateddataconfigurations.
| the forest, | the specified | maximum | depth of | each tree, and |            |     |         |     |         |              |          |     |
| ----------- | ------------- | ------- | -------- | -------------- | ---------- | --- | ------- | --- | ------- | ------------ | -------- | --- |
|             |               |         |          |                | • Synaptic |     | Weights | and | Biases: | connectivity | strength | is  |
theminimumsamplesizeofanode.Thesehyperparameters
measuredinweights,whichcontroltheinputsfromoneneu-
canbetunedandfine-tunedthroughsuchtechniquesasgrid
rontoanother.Theseweightsarefine-tunediterativelyinthe
search,randomsearch,[and]k-foldcross-validationtoarrive trainingphasetominimizethedifferencebetweenpredicted
atthebestsetuprelativetoagivenSTLFtask.
outputsandactualinputdata.
| • Once | the random | forest model | is thoroughly | developed |     |     |     |     |     |     |     |     |
| ------ | ---------- | ------------ | ------------- | --------- | --- | --- | --- | --- | --- | --- | --- | --- |
•ModelCalibration:Theseconnectedneuralstructuresare
andrefined,itcanaccomplishSTLFchapaccordinglytothe
calibratedusingacomplicatedprocedureknownasbackprop-
newlysuppliedinputdata.Fortheparticulargivenforecasting
|           |             |              |                 |           | agation. | This       | method | operates  | by  | systematically |          | adjusting |
| --------- | ----------- | ------------ | --------------- | --------- | -------- | ---------- | ------ | --------- | --- | -------------- | -------- | --------- |
| time, the | model takes | the relevant | characteristics | and fore- |          |            |        |           |     |                |          |           |
|           |             |              |                 |           | weights  | and biases |        | to reduce | the | gap between    | computed |           |
castsbasedoneachtreeinthedecisiontree.Thelastforecast
resultsandreality.ThebasicideawithCalibrationisthatthe
isthencalculatedastheaverageofalltheseresultstoproduce
algorithmworkscontinuouslyonadatasetuntilitachieves
amoreaccurateandlessvolatileforecast.
betterandmoreaccuratenetworkprediction.
•PerformanceMetric:Thenetworkevaluationisbasedon
4) MULTILAYERPERCEPTRON(MLP)MODEL a loss metric, gauging the model’s efficiency. The general
AnMLPisanextendedartificialneuralnetworkcomprising
|     |     |     |     |     | structure | of this | kind | of graphic |     | is such that | lower | values |
| --- | --- | --- | --- | --- | --------- | ------- | ---- | ---------- | --- | ------------ | ----- | ------ |
severallinkedstages,alsoknownaslayersofneuronsorper-
meanbetteraccuracyandeffectiveness.Theprincipleduring
ceptronlayers.Figure10showsthearchitectureofanMLP;
calibrationistoreducethisperformancemeasureasmuchas
thefollowingarethemaincomponentsofthisnerve[51].
possiblesinceitjeopardizesthenetwork’scapabilities.
Mathematically,theoutputofaneuroncanberepresented
as[52]:
X
|     |     |     |     |     |     |     | =   | (W  | ×   | +   | )   | (29) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---- |
I
|     |     |     |     |     | In the        | complex | design           |       | of an    | MLP, I     | is the        | quantity |
| --- | --- | --- | --- | --- | ------------- | ------- | ---------------- | ----- | -------- | ---------- | ------------- | -------- |
|     |     |     |     |     | we name       | the     | activation,      | which | is       | the output | of a          | neuron   |
|     |     |     |     |     | I, is decided |         | by an activation |       | function | .          | This function | is       |
governedbytheweightedsumofinputs,whichisalsoalinear
|     |     |     |     |     | summationofinputs,whereW |        |        |     | isaweightconnectingthe    |       |              |     |
| --- | --- | --- | --- | --- | ------------------------ | ------ | ------ | --- | ------------------------- | ----- | ------------ | --- |
|     |     |     |     |     | input                    | to the | neuron | and | is the                    | value | of the input | .   |
|     |     |     |     |     | Furthermore,thebiasterm  |        |        |     | isintroducedtoeachneuron, |       |              |     |
enablingthemodeltobemoreflexiblesincetheweightscan
|     |     |     |     |     | be adjusted | with | the | additional | input. | To  | denote the | above |
| --- | --- | --- | --- | --- | ----------- | ---- | --- | ---------- | ------ | --- | ---------- | ----- |
relationintheMLPforeachconsequentstratum,thematrix
| FIGURE10. | Multilayerperceptronmodel. |     |     |     |     |     |     |     |     |     |     |     |
| --------- | -------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
constructwillmakeitpossibletohavecomputedrightacross
•PrimaryInterface:ThisMLParchitecture’sfirstmodule the network layer concurrently. This representation signif-
involves ingesting the first data received at the platform, icantly improves activation calculations in many network
| VOLUME12,2024 |     |     |     |     |     |     |     |     |     |     |     | 111869 |
| ------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------ |

K.Ullahetal.:STLF:AComprehensiveReviewandSimulationStudy
layers,therebyincreasingtheeffectivenessofdeeperlearning
architectures.
X
|     |     | A=  | (WX+B) |     |     | (30) |     |     |     |     |     |     |     |     |
| --- | --- | --- | ------ | --- | --- | ---- | --- | --- | --- | --- | --- | --- | --- | --- |
A
| In this | detailed | description | of an | MLP, | the matrix | rep- |     |     |     |     |     |     |     |     |
| ------- | -------- | ----------- | ----- | ---- | ---------- | ---- | --- | --- | --- | --- | --- | --- | --- | --- |
resentstheactivationmatrixinwhichacolumncontainsthe
activationinformationofaneurontotheinputexamples.The
matrixWrepresentstheweightmatrixandholdscoefficients
| that relate | the inputs | with | the specific | neurons |     | to alter the |     |     |     |     |     |     |     |     |
| ----------- | ---------- | ---- | ------------ | ------- | --- | ------------ | --- | --- | --- | --- | --- | --- | --- | --- |
effectofeveryinputfeatureintheneuron’soutput.Xcanbe
|     |     |     |     |     |     |     | FIGURE11. | Typesoftheensemblemethod. |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --------- | ------------------------- | --- | --- | --- | --- | --- | --- |
representedbythesymbol,whereeachcolumnofthematrix
| comprises  | a specific | input    | feature  | vector | and      | contains the |          |     |               |     |             |        |     |        |
| ---------- | ---------- | -------- | -------- | ------ | -------- | ------------ | -------- | --- | ------------- | --- | ----------- | ------ | --- | ------ |
| input data | that is    | directly | supplied | to the | network. | Finally,     |          |     |               |     |             |        |     |        |
|            |            |          |          |        |          |              | However, | the | effectiveness |     | of ensemble | models |     | cannot |
Bisthebiasmatrixintegraltothenetworkforaddingabias
|     |     |     |     |     |     |     | be generalized |     | and depends | on  | the specific | combination |     | of  |
| --- | --- | --- | --- | --- | --- | --- | -------------- | --- | ----------- | --- | ------------ | ----------- | --- | --- |
termtoeachneuron’sweightedinput,whichassistsinshifting
|     |     |     |     |     |     |     | integrated | models; | identifying |     | which | configuration | is  | most |
| --- | --- | --- | --- | --- | --- | --- | ---------- | ------- | ----------- | --- | ----- | ------------- | --- | ---- |
theactivationfunctioncurve,thusofferinganotherdegreeof
effectivemaybedifficult.Thelimitationspresentinensemble
freedomforthelearningalgorithm.Afterthecomputationof
modelsincludethefactthattheaccuracyofthemodelswithin
activationsthroughoutallstrata,theterminalstratumdelivers
theensembledirectlyimpactstheensemblemodels’overall
theultimateforecast.Inclassificationendeavours,asoftmax
|     |     |     |     |     |     |     | accuracy | and | reliability | of the | forecast | [55]. | Substandard |     |
| --- | --- | --- | --- | --- | --- | --- | -------- | --- | ----------- | ------ | -------- | ----- | ----------- | --- |
functionishabituallydeployedintheoutputstratumtotrans-
|     |     |     |     |     |     |     | models | reduce | the efficacy | of  | ensemble | models, | whereby |     |
| --- | --- | --- | --- | --- | --- | --- | ------ | ------ | ------------ | --- | -------- | ------- | ------- | --- |
figuretheactivationsintoprobabilities:
|     |     |     |     |     |     |     | a model | may cross-spread |     | problems |     | such as | overfitting | or  |
| --- | --- | --- | --- | --- | --- | --- | ------- | ---------------- | --- | -------- | --- | ------- | ----------- | --- |
a
|     |      |       |     | e   |     |      | under fitting | the          | data. | Selecting | the     | models     | that would | be  |
| --- | ---- | ----- | --- | --- | --- | ---- | ------------- | ------------ | ----- | --------- | ------- | ---------- | ---------- | --- |
|     | Soft | −Max( | )=  |     |     | (31) |               |              |       |           |         |            |            |     |
|     |      |       |     | P a |     |      | part of       | the ensemble |       | should    | be done | carefully; | ensuring   |     |
e
|         |            |     |         |                |     |            | they are | all high-quality |     | is important. |     | The ensemble |     | model |
| ------- | ---------- | --- | ------- | -------------- | --- | ---------- | -------- | ---------------- | --- | ------------- | --- | ------------ | --- | ----- |
| In this | framework, | s   | denotes | the activation |     | for output |          |                  |     |               |     |              |     |       |
constructiontacticsincludebagging,boosting,andstacking,
neuron, signifiestheactivationforoutputneuron ,and asshowninFigure11.Bothmethodsaresuitableforhandling
| Soft −Max( | )istheprobabilityassociatedwithclass. |     |     |     |     |     |           |          |          |           |        |             |        |       |
| ---------- | ------------------------------------- | --- | --- | --- | --- | --- | --------- | -------- | -------- | --------- | ------ | ----------- | ------ | ----- |
|            |                                       |     |     |     |     |     | data and  | have     | specific | strengths | and    | weaknesses, | and    | the   |
|            |                                       |     |     |     |     |     | choice of | a method | depends  |           | on the | features    | of the | given |
5) ENSEMBLEMODELS applicationandthedataset.Bagging,alsoknownasbootstrap
Understanding the integration of machine learning archi- aggregating, involves using many based models developed
tectures, the last category, ensemble models, integrates the ondifferentsamplesofthebasetrainingsettocreateafinal
predictionsofmultiplemodelstocreateasingleforecast.The forecast or solution, the weighted average of the individual
basic concept of ensemble modeling is to combine various predictions/solutions. The fundamental idea of bagging lies
models,whereeachmodelhasitsuniquecharacteristicsand inconstructingseveralreplicasoftheinitialset,whereineach
strengths, and use their forecasted result together, which, replicawillconsistofadistinctyetsomehowdiversepartof
| whendeveloped,formsaclearerandmorerobustprediction. |     |     |     |     |     |     | theset[56]. |     |     |     |     |     |     |     |
| --------------------------------------------------- | --- | --- | --- | --- | --- | --- | ----------- | --- | --- | --- | --- | --- | --- | --- |
These models have general applicability in most machine Further, models are trained on each of such executions,
learningprocesses,includingclassifications,regression,and and the outcomes are combined to generate the final fore-
clustering[53].Anotherbenefitassociatedwiththeensemble cast.Inthisapproach,bagginginvolvescompilingtheresults
models is the ability to minimize variance and reduce the of all the models that have been developed to produce a
extentofoverfitting.Variance,inensemblemodels,refersto moreaccurateandreliableprediction.Boostingisthemethod
thevariationofthestandarddeviationoftheoutcomesofthe through which the training of models is set in a sequential
individualmodelswithintheensemble.Overfittingisamodel formsuchthateachisresponsibleforcorrectingthemistakes
learning problem that happens when excessive detail about madebyitspredecessor.Thistechniqueincreasesprediction
thetrainingdataisdeveloped,andtherefore,itisineffective accuracy–generallyduetoincreasedsusceptibilitytoover-
inanalyzingnewdata.Thischaracteristicofensemblemodels fitting compared to the bagging method. According to the
providesabasisforensuringtheirstabilityandincreasestheir principlesofboosting,theprocessbeginswithasimplemodel
applicabilityonvariousdatasets.Ensemblemodelsdoagood and continues with increasing levels of model complexity
jobofreducingvariancesandoverfittingbecausetheycom- added to solve the mistakes of the prior level [57]. These
binetherealestimationsofthemodels,reducingtheoverall models are then added with a weighted average, where the
variations that lead to a stronger prediction [54]. However, weightshavedirectproportionalitytoaccuracy,anderrorsare
thereis onedisadvantageregarding ensemblemodels:They gradually focused on previous models, enhancing attempts
arehighlycomplex.Eachofthesesituatedmodelsistypically towardshigheraccuracyandreliabilityoftheforecast.
less straightforward in their application and analysis than Theprocessofhierarchicalaggregation,frequentlyknown
isolatedmodelsandoftenrequireshighercomputingpower. as stratified synthesis, implies that numerous models are
| 111870 |     |     |     |     |     |     |     |     |     |     |     |     | VOLUME12,2024 |     |
| ------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------- | --- |

K.Ullahetal.:STLF:AComprehensiveReviewandSimulationStudy
trainedsuccessivelyinthetrainingdataset,andthecalculated notable hybrid models: Some hybrids have a strong combi-
outputsareusedasinputsfortheother,morecomplexmod- nationofthetwotypes.
els.Thehigher-levelmodelfurtherlearnstoaccumulatethe
| outcome | of the | lower-level |     | models | to arrive | at an | outcome. |     |     |     |     |     |     |     |
| ------- | ------ | ----------- | --- | ------ | --------- | ----- | -------- | --- | --- | --- | --- | --- | --- | --- |
1) HYBRIDMODELWITHARIMA–ANNAPPROACH
Despitethese,thestackingmodelcanenhancetheaccuracy Another conventional time series forecasting approach is
and reliability of the prediction compared to bagging or the ARIMA model, which serves as the basis for capturing
| boosting | but may | be  | harder | to apply | and | analyze | than the |           |        |          |           |       |      |             |
| -------- | ------- | --- | ------ | -------- | --- | ------- | -------- | --------- | ------ | -------- | --------- | ----- | ---- | ----------- |
|          |         |     |        |          |     |         |          | linearity | in the | data. On | the other | hand, | ANNs | can catego- |
two [58]. The higher-level model then learns to aggregate rizecomplexnon-linearrelationships.Thiscompoundmodel
thetwolower-levelpredictionsintooneprediction.Stacking,
|     |     |     |     |     |     |     |     | fully integrates |     | the linear | skill of | ARIMA | for load | data and |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------------- | --- | ---------- | -------- | ----- | -------- | -------- |
ingeneral,isawaytoobtainamoreaccurateandstablefore- the nonlinear diagnosis capacity of ANNs by realizing lin-
castsince,byusingseveralmodelstogether,theresultisan earforecasting ofARIMA&nonlinear diagnosisofANNs.
ensemblethatisusuallymoreprecise[59].DLisanadvanced
Indeed,suchasynthesissignificantlyimprovestheaccuracy
| MLmodelclassificationthatperformswellwhendiscovering |     |     |     |     |     |     |     | ofSTLF[66]. |     |     |     |     |     |     |
| ---------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | ----------- | --- | --- | --- | --- | --- | --- |
theintricatenonlinearrelationshipofloadbyotherpreceding
factors[60].TheDLframeworkshavestackedlayersofinter- 2) HYBRIDMODELSBASEDONWAVELET-TRANSFORM
| acting nodes | that  | help | convey        | information |        | using          | weighted |        |                   |     |            |       |            |         |
| ------------ | ----- | ---- | ------------- | ----------- | ------ | -------------- | -------- | ------ | ----------------- | --- | ---------- | ----- | ---------- | ------- |
|              |       |      |               |             |        |                |          | One of | the sophisticated |     | analytical | tools | that allow | for the |
| connections  | [61]. | As   | a significant |             | point, | it is possible | to       |        |                   |     |            |       |            |         |
decompositionofatimeseriesintoseveraldiscretefrequency
emphasizethatCNNsareoneofthemostusedDLmodelsfor
|     |     |     |     |     |     |     |     | bands is | the wavelet | coefficient. |     | The resolution |     | means that |
| --- | --- | --- | --- | --- | --- | --- | --- | -------- | ----------- | ------------ | --- | -------------- | --- | ---------- |
STLF.Thesenetworkseffectivelycaptureloaddatabasedon
|     |     |     |     |     |     |     |     | the high-frequency |     | section | contains | noise | and other | irregu- |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------------ | --- | ------- | -------- | ----- | --------- | ------- |
spaceandtimecharacteristics.CNNsareveryusefulinpower larities, whereas the low-frequency section captures steady
systems,enablingthepossibilityofpredictingchangesinload
|                |     |         |         |          |            |     |          | variations. | Since | EMD can | be combined |     | with different | pre- |
| -------------- | --- | ------- | ------- | -------- | ---------- | --- | -------- | ----------- | ----- | ------- | ----------- | --- | -------------- | ---- |
| due to special |     | factors | such as | weather, | occupancy, |     | and time |             |       |         |             |     |                |      |
dictivemodelsliketheANN,SVM,orLSTMnetworks,this
| of day. The | second | key | model | for TLs | specialized |     | in STLF |           |     |                |              |     |      |            |
| ----------- | ------ | --- | ----- | ------- | ----------- | --- | ------- | --------- | --- | -------------- | ------------ | --- | ---- | ---------- |
|             |        |     |       |         |             |     |         | technique | can | be effectively | incorporated |     | into | developing |
istheRNN,asthistypeofnetworkcanquicklyidentifyload
|     |     |     |     |     |     |     |     | the hybrid | forecasting |     | model. | What is | more important | is  |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------- | ----------- | --- | ------ | ------- | -------------- | --- |
data’s temporal characteristics. Sequential Neural Networks that,throughsplittingthefrequencycomponents,thismethod
(SNNs)possessfeedbackconnectionsandtheabilitytomove
increasestheaccuracyoftheforecastsbyanaverageofsixty-
fromonetimepointtothenext,thusequippingthemodelto
fivepercent[67].
quantifychangesintheloadovertime.Altogether,compared
| to all the | correlated | works | on  | SNNs, | the especially |     | suitable |     |     |     |     |     |     |     |
| ---------- | ---------- | ----- | --- | ----- | -------------- | --- | -------- | --- | --- | --- | --- | --- | --- | --- |
3) HYBRIDMODELEEMDANNAPPROACH
| for this | task is | the LSTM | network, |     | as it is | characterized | by  |     |     |     |     |     |     |     |
| -------- | ------- | -------- | -------- | --- | -------- | ------------- | --- | --- | --- | --- | --- | --- | --- | --- |
TheEEMDisarefinedsignalanalysisthathelpstorecreate
| a rather | high | ability | to perceive | short-time |     | and | long-time |                  |     |             |         |     |        |            |
| -------- | ---- | ------- | ----------- | ---------- | --- | --- | --------- | ---------------- | --- | ----------- | ------- | --- | ------ | ---------- |
|          |      |         |             |            |     |     |           | a non-stationary |     | time series | through | a   | set of | IMFs. This |
temporalinterdependencesintheloaddataset[62].
studyfurtherstrengthenstheproposedhybridmodelbycom-
|     |     |     |     |     |     |     |     | bining ANEMD |      | with ANN | to            | handle | non-stationary | and      |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------ | ---- | -------- | ------------- | ------ | -------------- | -------- |
|     |     |     |     |     |     |     |     | non-linear   | load | data. In | this process, | EEMD   | filters        | the load |
C. HYBRIDMODELS
datatoextracttheIMFs.Finally,theANNistrainedwiththe
| As suggested |     | by the | title, | they encompass |     | both | statistical |     |     |     |     |     |     |     |
| ------------ | --- | ------ | ------ | -------------- | --- | ---- | ----------- | --- | --- | --- | --- | --- | --- | --- |
extractedIMFsidentifiedintheprevioussectiontobuildpre-
| and machine | learning |     | methodologies |     | that | are integrated | to  |     |     |     |     |     |     |     |
| ----------- | -------- | --- | ------------- | --- | ---- | -------------- | --- | --- | --- | --- | --- | --- | --- | --- |
magnifythestrengthsofstill.Amongallthehybridsanalyzed dictiveforecasts.Theseindividualforecastsarethensummed
uptoarriveattheSTLFoutput[68].
| in STLF  | studies, | ARIMA–SVR |         | and       | ES–ANN | are | the most |     |     |     |     |     |     |     |
| -------- | -------- | --------- | ------- | --------- | ------ | --- | -------- | --- | --- | --- | --- | --- | --- | --- |
| utilized | models.  | The       | type of | composite | scheme |     | employed |     |     |     |     |     |     |     |
4) HYBRIDMODELSFUZZYLOGICAPPROACH
| for this | particular | kind | of investigation |     | in  | this paper | is the |     |     |     |     |     |     |     |
| -------- | ---------- | ---- | ---------------- | --- | --- | ---------- | ------ | --- | --- | --- | --- | --- | --- | --- |
ARIMA–SVR model, a conjunction of ARIMA and SVR Fuzzy logic is a mathematical approach designed to han-
architecture for capturing temporal patterns in load demand dle such uncertainties and impreciseness in data. It can be
|                |     |              |     |           |        |       |       | easily extended |     | with other | predictive |     | methods | like ANN, |
| -------------- | --- | ------------ | --- | --------- | ------ | ----- | ----- | --------------- | --- | ---------- | ---------- | --- | ------- | --------- |
| and non-linear |     | associations |     | with load | demand | [63], | [64]. |                 |     |            |            |     |         |           |
On the other hand, due to the integration of ES with ANN, SVM,orregressionfunctions.Itcancreateahighlyeffective
|        |       |        |     |                   |     |      |         | combined | model | to solve | the high | uncertainty | observed | in  |
| ------ | ----- | ------ | --- | ----------------- | --- | ---- | ------- | -------- | ----- | -------- | -------- | ----------- | -------- | --- |
| the ES | – ANN | design | can | note complexities |     | like | changes |          |       |          |          |             |          |     |
in season and other non-linear demands in load. Accu- the load data. In this regard, fuzzy logic can filter the input
rate and hardly interpretable models are achieved; hence, data, represent uncertainties in modeling the forecast unit,
|          |        |     |          |     |        |       |         | or combine | the | outputs | of distinct | models | to sharpen | the |
| -------- | ------ | --- | -------- | --- | ------ | ----- | ------- | ---------- | --- | ------- | ----------- | ------ | ---------- | --- |
| the STLF | models | are | improved | for | use in | power | systems |            |     |         |             |        |            |     |
with the help of hybrid models. However, they require forecastaccuracy[69].
fewerstatisticalmodelsandaremorerequiredthanmachine
learningalgorithms,andtheycanhavemoreproblemsimple- 5) HYBRIDMODELSWITHDEEP-LEARNINGAPPROACH
menting than purely machine learning models [65]. These Deeplearningparadigms,includingCNNsandlongLSTMs,
biomechanical-fractured constructs, which support different have demonstrated high fitness in STLF due to their abil-
modeling methodologies for assimilation efficiently, have ity to uncover hierarchical and temporal informatics. These
been said to improve load forecast rates. Here are some enhancedlearningframeworkscanbeincorporatedwithother
| VOLUME12,2024 |     |     |     |     |     |     |     |     |     |     |     |     |     | 111871 |
| ------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------ |

K.Ullahetal.:STLF:AComprehensiveReviewandSimulationStudy
predictivesystemslikestatisticalmodels,wavelettransform, TABLE2. DifferentModelofSTLFandtheirProsandCons.
or fuzzy rules to form a blended model. Such integrative
models make the best out of the integrated methodologies
ofSTLFandsignificantlyincreasetheaccuracylevelofthe
models[63].
D. PERFORMANCECOMPARISONOFSTLFMODELS
It is, therefore, safe to mention that several antecedent fac-
tors determine the effects of STLF models and the volume
and caliber of the variables involved. It is well established
that intelligent models often have superior predictive power
compared to models based solely on pure statistical con-
siderations, and models based on a blend of statistical and
intelligent framework components have been found to out-
performboth[70].However,thesemodels’somewhatrelative
performancedependsonthespecificapplicationandthedata
used. For instance, statistical models might produce good
outcomepredictionsofstationaryandlinearvaluesifdatais
limitedinquantity.
Ontheotherhand,intelligentmodelsareknowntoperform
wellundernonlinearandnon-stationarydatasetsorenviron-
ments, particularly if only a large number of datasets are
present. When these variables present linear and nonlinear
data patterns of relationship, and problems like noise or
missing data elements are there, hybrid models are more
beneficial. The following summarizes these observations,
asgiveninTable2.
IV. CASESTUDY
A. PROPOSEDMODEL
The proposed model architecture effectively integrates con-
volutional neural networks (CNNs) with long short-term
memory (LSTM) networks to process sequential data char-
acterizedby24-timestepsand17featurespertimestep.This
hybridarchitectureleveragesthestrengthsofbothCNNsand
LSTMs,enablingthemodeltocapturespatialandtemporal
dependenciesinherentinthedata.
Themodelbeginswithaninputlayerthataccommodates
sequencesofthespecifiedshape.Thefirstprocessingblock
consistsofa1Dconvolutionallayerwith48filtersandaker-
nelsize3.Thisconvolutionallayerisintendedtoextractlocal
features from the input sequences, capitalizing on the capa-
bility of convolutional operations to identify patterns such
as trends and periodicities. The output of this convolutional
layer is then passed through a ReLU activation function,
whichintroducesnon-linearityintothemodel,enhancingits
capacitytocapturecomplexrelationshipswithinthedata.
Following the activation, the output is flattened, trans-
formingthemulti-dimensionaltensorintoa1Dvector.This
flattenedrepresentationissubsequentlyprocessedbyadense
layer comprising 24 nodes. This dense layer aims to fur- with 32 filters and a kernel size 3. This layer continues the
ther abstract and learn higher-level representations of the process of feature extraction but at a finer granularity. The
features extracted by the convolutional layer. The second activation,flattening,anddenselayeroperationsarerepeated
convolutionalblocktakestheoutputfromthefirstactivation as in the first block, ensuring consistent transformation and
layer as input and applies another 1D convolutional layer abstractionoffeatures.Thethirdconvolutionalblockfollows
111872 VOLUME12,2024

K.Ullahetal.:STLF:AComprehensiveReviewandSimulationStudy
a similar structure, utilizing a 1D convolutional layer with ensure the net makes out the total series of hidden states.
16 filters and a kernel size 3. The progressively decreas- Finally,thereturnsequenceisfalseinthefinalLSTMlayer:
ing number of filters in subsequent convolutional layers is It is worth noting that in the final LSTM layer, the network
designed to reduce the dimensionality of the feature space gives only the hidden state (the last time step). Therefore,
whileretainingessentialpatterns.AftertheReLUactivation, anotherdropoutlayerwasinvokedbeforetheoutputlayerto
theoutputisflattenedandpassedthroughanotherdenselayer reducecasesofoverlearningandhighchancesofoverfitting.
with24nodes. The input or fully connected layer comprises 20 neurons
|     |     |     |     |     | equivalent | to 20 indexes | of the irregular | array used | to cool |
| --- | --- | --- | --- | --- | ---------- | ------------- | ---------------- | ---------- | ------- |
theneuralnetworkduringthesimulation.Theneuronsinthe
outputlayersarefromonetosixtocoverallthelook-ahead
|     |     |     |     |     | periods of | 1 up to 3 h    | for load forecasting. | The       | parameter |
| --- | --- | --- | --- | --- | ---------- | -------------- | --------------------- | --------- | --------- |
|     |     |     |     |     | setting of | the formulated | deep learning         | framework | in this   |
studyiscapturedinTable4.
TABLE3. Variouslayerconfigurationoftheproposedmodel.
| FIGURE12. | ProposedModeloftheNetwork. |                   |           |         |     |     |     |     |     |
| --------- | -------------------------- | ----------------- | --------- | ------- | --- | --- | --- | --- | --- |
| Following | the third                  | activation layer, | a dropout | rate of |     |     |     |     |     |
0.25isappliedtomitigatetheriskofoverfitting.Thisregu-
larizationtechniquerandomlysetsafractionofinputunitsto
zeroduringtraining,promotingrobustnessandgeneralization
ofthemodel.ThemodelthentransitionstoaseriesofLSTM
| layers, beginning | with | an LSTM layer | containing | 20 units |     |     |     |     |     |
| ----------------- | ---- | ------------- | ---------- | -------- | --- | --- | --- | --- | --- |
thatreturnsequences.Thislayerisinstrumentalincapturing
| the temporal | dependencies      | within the  | data, leveraging | the          |     |     |     |     |     |
| ------------ | ----------------- | ----------- | ---------------- | ------------ | --- | --- | --- | --- | --- |
| LSTM’s       | ability to retain | and utilize | information      | from pre-    |     |     |     |     |     |
| vious time   | steps. A second   | LSTM layer  | with             | 20 units and |     |     |     |     |     |
returningsequencesfurtherprocessesthetemporalinforma-
tion.ThethirdLSTMlayer,with20units,returnsonlythelast
TABLE4. Proposedmodelsetting(Parameters).
outputinthesequence,encapsulatingthetemporaldynamics
intoafixed-sizevector.FollowingtheLSTMlayers,another
| dropout      | layer with a dropout | rate 0.25        | is introduced | to fur-       |     |     |     |     |     |
| ------------ | -------------------- | ---------------- | ------------- | ------------- | --- | --- | --- | --- | --- |
| ther reduce  | overfitting.         | The output from  | this          | layer is then |     |     |     |     |     |
| concatenated | with the             | outputs from the | three         | dense layers  |     |     |     |     |     |
followingeachconvolutionalblock.Thisconcatenationoper-
| ation effectively | combines        | the spatial       | features | extracted by |     |     |     |     |     |
| ----------------- | --------------- | ----------------- | -------- | ------------ | --- | --- | --- | --- | --- |
| the CNN           | layers with the | temporal features | captured | by the       |     |     |     |     |     |
LSTM layers, providing a comprehensive representation of Tothisend,thedistinguishedoptimizertagged‘Adam’was
the input data. Finally, the concatenated features are passed deployed in this study due to its efficiency and supposedly
throughadenselayerwith24or1nodeandatanhactivation optimal responsiveness to fluctuating learning rate require-
function, producing the model’s final output for single-step ments. To evaluate the accuracy of the mean absolute error,
andmultistepforecasting[79].However,ithasbeenmodified or MAE was utilized as the loss function by calculating the
to enhance the performance. The parameter setting of the absolute value of the difference between the target and pre-
formulateddeeplearningframeworkinthisstudyiscaptured dictedvaluesforeachdatapoint,summingallthesevalues,
inTable3. and dividing the total by the overall number of values in a
| It also | assists them in | reducing the | number of | overfitting | dataset. |     |     |     |     |
| ------- | --------------- | ------------ | --------- | ----------- | -------- | --- | --- | --- | --- |
andresultsinasmallernumberoftrainableparameters.Every
stackincludedasequencelearningblock,whereexactlythree B. DATAPRE-PROCESSING
LSTMlayerswereused,with20neuronsperlayer.Thereturn Foroptimallearning,datamustbemeticulouslypre-processed
sequence is set as the true for the first two LSTM layers to before model training. A well-prepared dataset enhances
| VOLUME12,2024 |     |     |     |     |     |     |     |     | 111873 |
| ------------- | --- | --- | --- | --- | --- | --- | --- | --- | ------ |

K.Ullahetal.:STLF:AComprehensiveReviewandSimulationStudy
| FIGURE13. | Pre-processingdiagram. |     |     |     |     |     |     |
| --------- | ---------------------- | --- | --- | --- | --- | --- | --- |
a model’s ability to identify trends and relationships. The data.Thisapproachwasessentialtomaintaintheintegrityand
primarypre-processingstepsincludetrain-testsplitting,data utilityofthedatasetforaccuratefeatureextractionandsub-
cleaning, high-level feature extraction, and formatting the sequentmodeltraining.Adetaileddescriptionofthedataset,
data into a 3D structure (Samples, Time Steps, and Fea- includingvariousattributesandcorrespondingvalues,ispro-
tures) suitable for model training. Figure 13 illustrates the videdinTable5.
comprehensivepre-processingflowchart.Utilizingtheafore-
mentioned model for pre-processing, the initial data was TABLE5. Datasetdescription.
acquiredfromtheNationalTransmissionandDispatchCom-
pany(NTDC)inIslamabad.Thisdatawasinitiallyscattered
| across multiple | files, which  | posed a         | challenge for | effective |     |     |     |
| --------------- | ------------- | --------------- | ------------- | --------- | --- | --- | --- |
| handling        | and analysis. | These disparate | files were    | meticu-   |     |     |     |
louslyprocessedandmergedtostreamlinetheprocessintoa
cohesivefile,facilitatingmoreefficientdatamanagementand
featureextraction.Thecomprehensiveflowchartdetailingthe
entirepre-processingprocedureispresentedinFigure13.
| This dataset   | encompasses | a time range  | from January    | 1,   |     |     |     |
| -------------- | ----------- | ------------- | --------------- | ---- | --- | --- | --- |
| 2019, at 00:00 | hours to    | May 31, 2023, | at 23:00 hours, | with |     |     |     |
Thiscomprehensivedescriptionclearlyexplainsthedata’s
data recorded hourly by the National Power Control Center scope and characteristics, ensuring that all relevant infor-
(NPCC). Several manipulation techniques were applied to mation is available for thorough analysis and model devel-
ensure data privacy while preparing it for analysis. These opment. Subsequently, the data was divided into training
m anipulations were executed to preserve the overall con- and testing sets. The period from February 2023 to May
sumptionpatterns,introducingonlyminoradjustmentstothe
|        |     |     |     | 2023 was designated | as the test | data andextracted | from the      |
| ------ | --- | --- | --- | ------------------- | ----------- | ----------------- | ------------- |
| 111874 |     |     |     |                     |             |                   | VOLUME12,2024 |

K.Ullahetal.:STLF:AComprehensiveReviewandSimulationStudy
| FIGURE14. |     | Outliersbeforeandafterhandling. |     |     |     |     |     |     |     |     |     |
| --------- | --- | ------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
entire dataset. The remaining data, spanning from January 22:00:00 to 2021-01-09 22:00:00 and from 2021-01-09
2019 to January 2023, was partitioned such that 70 percent 06:00:00 to 2021-01-16 06:00:00 were rectified by substi-
wasutilizedfortrainingand30percentforvalidation. tuting them with the mean values computed over 24-hour
During the analysis process, it was confirmed that there periods, grouped by each hour. Before and after this treat-
wasnomissingdata;however,outliersweredetectedwithin ment process, the comprehensive details of the outliers are
thetrainingdataset,asillustratedinFigure14.Theseoutliers delineatedinTable6.
| were identified |     | and addressed |     | to ensure | the integrity | of the |     |     |     |     |     |
| --------------- | --- | ------------- | --- | --------- | ------------- | ------ | --- | --- | --- | --- | --- |
model training process. The analysis assumes no missing TABLE6. Detaildescriptionofoutliers.
| data was      | in the     | dataset | while       | outliers were | identified, | espe-    |     |     |     |     |     |
| ------------- | ---------- | ------- | ----------- | ------------- | ----------- | -------- | --- | --- | --- | --- | --- |
| cially during | off-peak   |         | hours.      | The figure    | presents    | the load |     |     |     |     |     |
| in megawatts  | (MW)       | by      | categories, | including     | working     | days,    |     |     |     |     |     |
| holidays,     | off-peak,  | and     | peak hours  | during        | the summer  | peak     |     |     |     |     |     |
| period.       | The median | load    | is slightly | lower         | during      | holidays |     |     |     |     |     |
thanduringworkingdays,butasimilarIQRfollowsthisand
| has no extreme |     | points; | therefore, | the load | is similar | during |     |     |     |     |     |
| -------------- | --- | ------- | ---------- | -------- | ---------- | ------ | --- | --- | --- | --- | --- |
bothworkingdaysandholidays.Contrarily,theloadduring
on-peakismuchhigherandmoreconsolidatedthanoff-peak,
| with several | low          | values     | and higher | variability. |           | This implies |     |     |     |     |     |
| ------------ | ------------ | ---------- | ---------- | ------------ | --------- | ------------ | --- | --- | --- | --- | --- |
| a high and   | well-defined |            | increase   | in energy    | demand    | during       |     |     |     |     |     |
| the on-peak  | hours.       | Therefore, |            | there is     | a need to | establish a  |     |     |     |     |     |
betterwayofpredictingthevariationsandstabilityduringthe
off-peakhours.Theyareimportantforenergymanagement,
| resource  | planning,     | and | load forecast | enhancement. |           | Follow-  |     |     |     |     |     |
| --------- | ------------- | --- | ------------- | ------------ | --------- | -------- | --- | --- | --- | --- | --- |
| ing this, | all potential |     | features      | that could   | influence | the load |     |     |     |     |     |
consumption pattern were extracted, as depicted in the heat Various factors influencing the load consumption pat-
|     |     |     |     |     |     |     | tern were | incorporated | for | feature extraction. | These factors |
| --- | --- | --- | --- | --- | --- | --- | --------- | ------------ | --- | ------------------- | ------------- |
mapinFigure15.Additionally,thisstudytreatedallnational
|     |     |     |     |     |     |     | included | the hour of | the day, | the month, | and the weekdays, |
| --- | --- | --- | --- | --- | --- | --- | -------- | ----------- | -------- | ---------- | ----------------- |
holidaysasweekendholidaystomaintainconsistencyinthe
dataanalysis. withtheireffectsillustratedinFigures16and17,respectively.
|     |     |     |     |     |     |     | Additionally, | Pakistani | national | holidays | were encoded as |
| --- | --- | --- | --- | --- | --- | --- | ------------- | --------- | -------- | -------- | --------------- |
Theoutlierswereidentifiedusingthefollowingequations:
binarysignals(0fornoholiday,1foraholiday),andweek-
LowerOutliers = Min×(Q −1.5×IQR) (32) endswereincludedintheanalysis.
1
|               |     |     |          |           |     |      | The data | was prepared |     | for the deep learning | network to |
| ------------- | --- | --- | -------- | --------- | --- | ---- | -------- | ------------ | --- | --------------------- | ---------- |
| UpperOutliers |     |     | = Max×(Q | +1.5×IQR) |     | (33) |          |              |     |                       |            |
3
|     |     |     |     |     |     |     | accommodate | single-step |     | and multistep | inputs. Algorithms |
| --- | --- | --- | --- | --- | --- | --- | ----------- | ----------- | --- | ------------- | ------------------ |
Theoutliersweremanagedsimilarlytoconsecutivemissing forconfiguringsingle-stepandmultistepdatasequenceswere
values. Specifically, the data anomalies from 2021-01-02 delineated in our previous work. Notably, 17 input features
| VOLUME12,2024 |     |     |     |     |     |     |     |     |     |     | 111875 |
| ------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------ |

K.Ullahetal.:STLF:AComprehensiveReviewandSimulationStudy
FIGURE15. CorrelationofFeaturewithLoad.
FIGURE16. Categoricalfeatures.
were incorporated to train the CNN and LSTM models, resources and balance loads effectively, enhancing overall
asillustratedinTable7.Accordingly,theperformanceeval- system performance. Recently, there has been an increasing
uationmetricsarepresentedinTables8and9,respectively. interest in developing sophisticated forecasting models to
improve the precision of hour-ahead load predictions. The
actual power consumption and the predicted power from
C. RESULTSANDDISCUSSION the proposed model are illustrated in Figure 18 for hour-
Hourlyloadforecastingisanessentialcomponentofenergy ahead forecasting. This graph juxtaposes the actual load (in
managementsystems,ensuringthestabilityandefficiencyof megawatts)withthepredictedloadacrossvariousdates.The
powernetworks.Accurateforecastsenableutilitiestoallocate x-axisdenotesthedatesfromDecember2020toApril2021,
111876 VOLUME12,2024

K.Ullahetal.:STLF:AComprehensiveReviewandSimulationStudy
FIGURE17. Cyclicfeatures.
FIGURE18. Actualandpredictedloadconsumption.
while the y-axis measures the electrical load in megawatts thatthepredictionmodelhaseffectivelycapturedtheoverall
(MW). The black line represents the actual load, and the trend and most fluctuations in the load data. Although the
predicted load is depicted in red. The graph indicates that prediction is conducted for the entire test dataset, only a
thepredictedloadcloselymirrorstheactualload,suggesting few days from the beginning are shown for better visibility.
VOLUME12,2024 111877

K.Ullahetal.:STLF:AComprehensiveReviewandSimulationStudy
TABLE7. Inputfeatures.
| The input   | features     | are | presented | in Table    | 7. In    | contrast, the |     |     |     |     |     |     |     |     |
| ----------- | ------------ | --- | --------- | ----------- | -------- | ------------- | --- | --- | --- | --- | --- | --- | --- | --- |
| performance | evaluation   |     | for the   | single      | step and | 24 steps are  |     |     |     |     |     |     |     |     |
| presented   | in Comparing |     | the       | performance | of the   | forecasting   |     |     |     |     |     |     |     |     |
modelspresentedin[55]and[79],andtheproposedmodel,
|     |     |     |     |     |     |     | FIGURE19. | Comparisonwiththereferencemodel. |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --------- | -------------------------------- | --- | --- | --- | --- | --- | --- |
itispossibletonotetheincreaseintheperformanceindica-
torsoftheproposedmodelforbothsingle-stepand24-hour
line)thanthevaluesofpredictionsdefinedbythereference
forecasting.Inthecaseofsingle-stepforecasting,thedataset
method(blueline).ThedatautilizedinthiscasewasNTDC,
| of NTDC | has | demonstrated |     | that the | proposed | model has a |              |     |             |           |     |      |       |          |
| ------- | --- | ------------ | --- | -------- | -------- | ----------- | ------------ | --- | ----------- | --------- | --- | ---- | ----- | -------- |
|         |     |              |     |          |          |             | which serves | as  | the study’s | baseline. |     | This | shows | that the |
valueofRMSEequalto538.71,MAEof371.97,andMAPE
adoptedmodelhasgivenabetter,moreaccurateloadforecast
of2.72,outperforming[79].Likewise,fortheAEPdataset,
|          |      |              |        |               |          |             | in MWatt | over        | the stipulated |               | period. | The reference |                 | method |
| -------- | ---- | ------------ | ------ | ------------- | -------- | ----------- | -------- | ----------- | -------------- | ------------- | ------- | ------------- | --------------- | ------ |
| the RMSE | of   | the proposed |        | model is      | 126. 35, | MAE of 94.  |          |             |                |               |         |               |                 |        |
|          |      |              |        |               |          |             | has high | variability | to             | the actual    | values, | as            | evidenced       | by     |
| 27, and  | MAPE | of 0.        | 64 are | substantially | better   | than [79]   |          |             |                |               |         |               |                 |        |
|          |      |              |        |               |          |             | Fig. 19, | which       | explains       | this method’s |         | fairly        | poor predictive |        |
| (RMSE:   | 372. | 77, MAE:     | 295.   | 92, MAPE:     | 2.       | 05 and [55] |          |             |                |               |         |               |                 |        |
power.
| RMSE:        | 472. 13, | MAE:     | 358.  | 6, MAPE: | 2. 41.      | In 24-hour |     |     |     |     |     |     |     |     |
| ------------ | -------- | -------- | ----- | -------- | ----------- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- |
| forecasting, | the      | proposed | model | also     | outperforms | the other  |     |     |     |     |     |     |     |     |
V. CONCLUSION
modelswithNTDCvaluesofRMSE951.94,MAE656.35,
|     |     |     |     |     |     |     | Short-term | load | forecasting | (STLF) |     | is crucial | in large-scale |     |
| --- | --- | --- | --- | --- | --- | --- | ---------- | ---- | ----------- | ------ | --- | ---------- | -------------- | --- |
andMAPE4.72,comparedto[79](RMSE:Andinthiscase,
|     |     |     |     |     |     |     | power grids, | enabling |     | grid operators |     | to accurately |     | fore- |
| --- | --- | --- | --- | --- | --- | --- | ------------ | -------- | --- | -------------- | --- | ------------- | --- | ----- |
theproposedmodelhasalowerRMSE(1038.04)than[55]
|     |     |     |     |     |     |     | cast load | and | efficiently | utilize | operating |     | reserves. | This |
| --- | --- | --- | --- | --- | --- | --- | --------- | --- | ----------- | ------- | --------- | --- | --------- | ---- |
(1166.79),alowerMAE(773.18)than[55](843.76),and
|              |          |             |       |                 |                      |              | paper explains     |          | the latest | STLF           | techniques, |            | including | sta-    |
| ------------ | -------- | ----------- | ----- | --------------- | -------------------- | ------------ | ------------------ | -------- | ---------- | -------------- | ----------- | ---------- | --------- | ------- |
| a lower      | MAPE     | (5. 35)     | than  | [55] (6.        | 16). In the          | case of the  |                    |          |            |                |             |            |           |         |
|              |          |             |       |                 |                      |              | tistical models    |          | such as    | autoregressive |             | integrated |           | moving  |
| AEP dataset, | the      | RMSE        | of    | the proposed    | model                | is 702. 97,  |                    |          |            |                |             |            |           |         |
|              |          |             |       |                 |                      |              | averages           | (ARIMA), | seasonal   |                | ARIMA       | (SARIMA),  |           | expo-   |
| MAE of       | 507. 97, | and         | MAPE  | of 3. 39        | also outperform[79]. |              |                    |          |            |                |             |            |           |         |
|              |          |             |       |                 |                      |              | nential smoothing, |          | and        | generalized    |             | linear     | models.   | It also |
| In general,  | the      | proposed    | model | outperforms     | the                  | benchmark    |                    |          |            |                |             |            |           |         |
|              |          |             |       |                 |                      |              | includes           | smart    | techniques | such           | as Support  |            | vector    | machine |
| models       | in terms | of accuracy |       | and reliability | in                   | one-step and |                    |          |            |                |             |            |           |         |
n-stepaheadforecasting. (SVM),decisiontree,randomforest,gradientboosting,MLP,
|     |     |     |     |     |     |     | ENSEMBLE, | and    | hybrid        | models. | These        | methods |     | are then  |
| --- | --- | --- | --- | --- | --- | --- | --------- | ------ | ------------- | ------- | ------------ | ------- | --- | --------- |
|     |     |     |     |     |     |     | assessed  | in the | paper through |         | mathematical |         | and | graphical |
TABLE8. Performanceevaluationmatrixforsingle-step.
|     |     |     |     |     |     |     | analysis,       | and their  | advantages   |                | and drawbacks |              | are discussed |          |
| --- | --- | --- | --- | --- | --- | --- | --------------- | ---------- | ------------ | -------------- | ------------- | ------------ | ------------- | -------- |
|     |     |     |     |     |     |     | to assist       | with their | proper       | implementation |               |              | in present    | day      |
|     |     |     |     |     |     |     | power systems.  |            | Further,     | the            | paper         | has proposed |               | a hybrid |
|     |     |     |     |     |     |     | CNN-LSTM        | model      | for          | STLF,          | which         | combines     |               | Convolu- |
|     |     |     |     |     |     |     | tional Neural   | Networks   |              | (CNNs)         | for           | feature      | extraction    | and      |
|     |     |     |     |     |     |     | Long Short-Term |            | Memory       | networks       |               | (LSTMs)      | for           | sequence |
|     |     |     |     |     |     |     | forecasting     | and        | uses textual | data           | from          | the NTDC     |               | Pakistan |
nationalpowergrid.Theresultsofthecomparativeanalysis
TABLE9. Performanceevaluationmatrixfor24hours.
|     |     |     |     |     |     |     | with the | previous | models | using | the | AEP dataset | prove | that |
| --- | --- | --- | --- | --- | --- | --- | -------- | -------- | ------ | ----- | --- | ----------- | ----- | ---- |
theproposedhybridmodelhashigheraccuracyinsingle-step
and24-hourforecasts,thusimprovingtheforecastqualityand
|     |     |     |     |     |     |     | generalizing | the | model’s | performance |     | for various |     | forecast |
| --- | --- | --- | --- | --- | --- | --- | ------------ | --- | ------- | ----------- | --- | ----------- | --- | -------- |
horizons.
Likewise,howtheycompareisshowninFigure19.Itcan In the future, this study can be extended to probabilistic
be confirmed that the values of the proposed model’s pre- load forecasting to improve the stability and accuracy of
dictions(redline)areclosertotheactualloadvalues(black the forecast. Probabilistic forecasting measures the degree
| 111878 |     |     |     |     |     |     |     |     |     |     |     |     | VOLUME12,2024 |     |
| ------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------- | --- |

K.Ullahetal.:STLF:AComprehensiveReviewandSimulationStudy
of uncertainty by providing the range of possible and fore- [18] Z.Liu,P.Jiang,L.Zhang,andX.Niu,‘‘Acombinedforecastingmodel
casted values, which is crucial in risk management and fortimeseries:Applicationtoshort-termwindspeedforecasting,’’Appl.
Energy,vol.259,Feb.2020,Art.no.114137.
| decision-making     | in   | power    | systems. | This        | includes | incor- |                                                                  |     |     |     |     |     |     |
| ------------------- | ---- | -------- | -------- | ----------- | -------- | ------ | ---------------------------------------------------------------- | --- | --- | --- | --- | --- | --- |
|                     |      |          |          |             |          |        | [19] C.Fan,J.Wang,W.Gang,andS.Li,‘‘Assessmentofdeeprecurrentneu- |     |     |     |     |     |     |
| porating techniques | like | quantile |          | regression, | Monte    | Carlo  |                                                                  |     |     |     |     |     |     |
ralnetwork-basedstrategiesforshort-termbuildingenergypredictions,’’
Appl.Energy,vol.236,pp.700–710,Feb.2019.
simulation,andBayesiananalysis.Theseapproacheswould
|                 |               |             |           |       |              |       | [20] E. Hossain, | I.       | Khan, F.    | Un-Noor,    | S. S. Sikander, | and               | M.S.H.Sunny, |
| --------------- | ------------- | ----------- | --------- | ----- | ------------ | ----- | ---------------- | -------- | ----------- | ----------- | --------------- | ----------------- | ------------ |
| give more       | context-aware | information |           | about | expected     | devi- |                  |          |             |             |                 |                   |              |
|                 |               |             |           |       |              |       | ‘‘Application    |          | of big data | and machine |                 | learning in smart | grid, and    |
| ations or risks | in load       | forecasts,  | enhancing |       | the accuracy | of    |                  |          |             |             |                 |                   |              |
|                 |               |             |           |       |              |       | associated       | security | concerns:   |             | A review,’’     | IEEE Access,      | vol. 7,      |
theforecastsandthedecision-makingprocessinpowergrid pp.13960–13988,2019.
management. [21] Y.ErenandI.Küçükdemiral,‘‘Acomprehensivereviewondeeplearning
approachesforshort-termloadforecasting,’’Renew.Sustain.EnergyRev.,
vol.189,Jan.2024,Art.no.114031.
|     |     |     |     |     |     |     | [22] H.HassaniandE.S.Silva,‘‘Predictionsfromgenerativeartificialintel- |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ---------------------------------------------------------------------- | --- | --- | --- | --- | --- | --- |
REFERENCES
|     |     |     |     |     |     |     | ligence | models: | Towards | a new | benchmark | in forecasting | practice,’’ |
| --- | --- | --- | --- | --- | --- | --- | ------- | ------- | ------- | ----- | --------- | -------------- | ----------- |
[1] L.ChengandT.Yu,‘‘AnewgenerationofAI:Areviewandperspectiveon
Information,vol.15,no.6,p.291,May2024.
machinelearningtechnologiesappliedtosmartenergyandelectricpower
|     |     |     |     |     |     |     | [23] M.H.SulaimanandZ.Mustaffa,‘‘Chillerenergypredictionincommer- |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ----------------------------------------------------------------- | --- | --- | --- | --- | --- | --- |
systems,’’Int.J.EnergyRes.,vol.43,no.6,pp.1928–1973,May2019. cialbuilding:Ametaheuristic-enhanceddeeplearningapproach,’’Energy,
[2] Y.Ding,Y.Zhu,J.Feng,P.Zhang,andZ.Cheng,‘‘Interpretablespatio- vol.297,Jun.2024,Art.no.131159.
temporalattentionLSTMmodelforfloodforecasting,’’Neurocomputing, [24] D. Hou and R. Evins, ‘‘A protocol for developing and evaluating
vol.403,pp.348–359,Aug.2020. neural network-based surrogate models and its application to building
[3] H. Fu, J.-C. Baltazar, and D. E. Claridge, ‘‘Review of developments energy prediction,’’ Renew. Sustain. Energy Rev., vol. 193, Apr. 2024,
Art.no.114283.
| in whole-building | statistical | energy | consumption |     | models | for commer- |     |     |     |     |     |     |     |
| ----------------- | ----------- | ------ | ----------- | --- | ------ | ----------- | --- | --- | --- | --- | --- | --- | --- |
cial buildings,’’ Renew. Sustain. Energy Rev., vol. 147, Sep. 2021, [25] K.Wang,X.Qi,andH.Liu,‘‘PhotovoltaicpowerforecastingbasedLSTM-
Art.no.111248. convolutionalnetwork,’’Energy,vol.189,Dec.2019,Art.no.116225.
[4] S.Lu,Q.Li,L.Bai,andR.Wang,‘‘Performancepredictionsofground [26] S.Du,T.Li,Y.Yang,andS.-J.Horng,‘‘Multivariatetimeseriesforecast-
sourceheatpumpsystembasedonrandomforestandbackpropagation ing via attention-based encoder–decoder framework,’’ Neurocomputing,
neuralnetworkmodels,’’EnergyConvers.Manage.,vol.197,Oct.2019, vol.388,pp.269–279,May2020.
Art.no.111864. [27] A.Mosavi,M.Salimi,S.F.Ardabili,T.Rabczuk,S.Shamshirband,and
A.R.Varkonyi-Koczy,‘‘Stateoftheartofmachinelearningmodelsin
[5] M.A.Ganaie,M.Hu,A.K.Malik,M.Tanveer,andP.N.Suganthan,
‘‘Ensembledeeplearning:Areview,’’Eng.Appl.Artif.Intell.,vol.115, energysystems,asystematicreview,’’Energies,vol.12,no.7,p.1301,
| Oct.2022,Art.no.105151. |     |     |     |     |     |     | Apr.2019. |     |     |     |     |     |     |
| ----------------------- | --- | --- | --- | --- | --- | --- | --------- | --- | --- | --- | --- | --- | --- |
[6] A.Altan,S.Karasu,andE.Zio,‘‘Anewhybridmodelforwindspeed [28] M.Cai,M.Pipattanasomporn,andS.Rahman,‘‘Day-aheadbuilding-level
forecastingcombininglongshort-termmemoryneuralnetwork,decom- loadforecastsusingdeeplearningvs.traditionaltime-seriestechniques,’’
Appl.Energy,vol.236,pp.1078–1088,Feb.2019.
positionmethodsandgreywolfoptimizer,’’Appl.SoftComput.,vol.100,
|     |     |     |     |     |     |     | [29] S.Sobri,S.Koohi-Kamali,andN.A.Rahim,‘‘Solarphotovoltaicgenera- |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ------------------------------------------------------------------- | --- | --- | --- | --- | --- | --- |
Mar.2021,Art.no.106996.
tionforecastingmethods:Areview,’’EnergyConvers.Manage.,vol.156,
| [7] M. Alexander | and H. | Beushausen, | ‘‘Durability, | service | life | prediction, |     |     |     |     |     |     |     |
| ---------------- | ------ | ----------- | ------------- | ------- | ---- | ----------- | --- | --- | --- | --- | --- | --- | --- |
andmodellingforreinforcedconcretestructures—Reviewandcritique,’’ pp.459–497,Jan.2018.
CementConcreteRes.,vol.122,pp.17–29,Aug.2019. [30] R.Ahmed,V.Sreeram,Y.Mishra,andM.D.Arif,‘‘Areviewandeval-
[8] A.Kurani,P.Doshi,A.Vakharia,andM.Shah,‘‘Acomprehensivecompar- uationofthestate-of-the-artinPVsolarpowerforecasting:Techniques
|     |     |     |     |     |     |     | and | optimization,’’ | Renew. | Sustain. | Energy | Rev., vol. 124, | May 2020, |
| --- | --- | --- | --- | --- | --- | --- | --- | --------------- | ------ | -------- | ------ | --------------- | --------- |
ativestudyofartificialneuralnetwork(ANN)andsupportvectormachines
Art.no.109792.
(SVM)onstockforecasting,’’Ann.DataSci.,vol.10,no.1,pp.183–208,
|     |     |     |     |     |     |     | [31] C.Tarmanini,N.Sarma,C.Gezegin,andO.Ozgonenel,‘‘Shorttermload |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ----------------------------------------------------------------- | --- | --- | --- | --- | --- | --- |
Feb.2023.
forecastingbasedonARIMAandANNapproaches,’’EnergyRep.,vol.9,
[9] A.S.DagoumasandN.E.Koltsaklis,‘‘Reviewofmodelsforintegrating
renewableenergyinthegenerationexpansionplanning,’’Appl.Energy, pp.550–557,May2023.
vol.242,pp.1573–1587,May2019. [32] N. Kalchbrenner, I. Danihelka, and A. Graves, ‘‘Grid long short-term
memory,’’2015,arXiv:1507.01526.
[10] L.-L.Li,X.Zhao,M.-L.Tseng,andR.R.Tan,‘‘Short-termwindpower
|             |          |         |                |      |          |           | [33] K.T.Ponds,A.Arefi,A.Sayigh,andG.Ledwich,‘‘Aggregatorofdemand |     |     |     |     |     |     |
| ----------- | -------- | ------- | -------------- | ---- | -------- | --------- | ----------------------------------------------------------------- | --- | --- | --- | --- | --- | --- |
| forecasting | based on | support | vector machine | with | improved | dragonfly |                                                                   |     |     |     |     |     |     |
responseforrenewableintegrationandcustomerengagement:Strengths,
algorithm,’’J.CleanerProd.,vol.242,Jan.2020,Art.no.118447.
weaknesses,opportunities,andthreats,’’Energies,vol.11,no.9,p.2391,
[11] J.ChenandX.Ran,‘‘Deeplearningwithedgecomputing:Areview,’’Proc.
Sep.2018.
IEEE,vol.107,no.8,pp.1655–1674,Aug.2019.
|     |     |     |     |     |     |     | [34] G. Fan, | Y. Guo, | J. Zheng, | and | W. Hong, | ‘‘A generalized | regression |
| --- | --- | --- | --- | --- | --- | --- | ------------ | ------- | --------- | --- | -------- | --------------- | ---------- |
[12] A. Ruano, A. Hernandez, J. Ureña, M. Ruano, and J. Garcia, ‘‘NILM modelbasedonhybridempiricalmodedecompositionandsupportvector
techniquesforintelligenthomeenergymanagementandambientassisted regressionwithback-propagationneuralnetworkformid-short-termload
living:Areview,’’Energies,vol.12,no.11,p.2203,Jun.2019.
forecasting,’’J.Forecasting,vol.39,no.5,pp.737–756,Aug.2020.
[13] S.M.Hasanat,R.Younis,S.Alahmari,M.T.Ejaz,M.Haris,H.Yousaf,
|     |     |     |     |     |     |     | [35] A. S. | Nair, P. | Ranganathan, | C. Finley, | and | N. Kaabouch, | ‘‘Short-term |
| --- | --- | --- | --- | --- | --- | --- | ---------- | -------- | ------------ | ---------- | --- | ------------ | ------------ |
S.Watara,K.Ullah,andZ.Ullah,‘‘Enhancingloadforecastingaccuracy
forecastanalysisonwindpowergenerationdata,’’inProc.IEEEKansas
in smart grids: A novel parallel multichannel network approach using PowerEnergyConf.(KPEC),Apr.2021,pp.1–6.
1DCNNandBi-LSTMmodels,’’Int.J.EnergyRes.,vol.2024,no.1, [36] L.Shang,K.Chen,G.Wang,Y.Liu,R.Hu,andY.Shang,‘‘Short-term
Jan.2024,Art.no.2403847. distribution network peak load forecasting based on generalized linear
[14] M.Sharifzadeh,A.Sikinioti-Lock,andN.Shah,‘‘Machine-learningmeth- model,’’inProc.4thInt.Conf.PowerEnergyTechnol.(ICPET),Jul.2022,
odsforintegratedrenewablepowergeneration:Acomparativestudyof
pp.584–589.
artificialneuralnetworks,supportvectorregression,andGaussianprocess
|     |     |     |     |     |     |     | [37] A. Pierrot | and | Y. Goude, | ‘‘Short-term | electricity | load forecasting | with |
| --- | --- | --- | --- | --- | --- | --- | --------------- | --- | --------- | ------------ | ----------- | ---------------- | ---- |
regression,’’Renew.Sustain.EnergyRev.,vol.108,pp.513–538,Jul.2019. generalizedadditivemodels,’’Proc.ISAPPower,2011,pp.1–6.
[15] H.Liu,C.Chen,X.Lv,X.Wu,andM.Liu,‘‘Deterministicwindenergy [38] Y.Liang,D.Niu,andW.-C.Hong,‘‘Shorttermloadforecastingbasedon
forecasting: A review of intelligent predictors and auxiliary methods,’’ featureextractionandimprovedgeneralregressionneuralnetworkmodel,’’
EnergyConvers.Manage.,vol.195,pp.328–345,Sep.2019. Energy,vol.166,pp.653–663,Jan.2019.
[16] A.Nespoli,E.Ogliari,S.Leva,A.MassiPavan,A.Mellit,V.Lughi,and [39] G.Hafeez,K.S.Alimgeer,andI.Khan,‘‘Electricloadforecastingbased
A.Dolara,‘‘Day-aheadphotovoltaicforecasting:Acomparisonofthemost
ondeeplearningandoptimizedbyheuristicalgorithminsmartgrid,’’Appl.
effectivetechniques,’’Energies,vol.12,no.9,p.1621,Apr.2019. Energy,vol.269,Jul.2020,Art.no.114915.
[17] M.Mahzarnia,M.P.Moghaddam,P.T.Baboli,andP.Siano,‘‘Areviewof [40] Y.Wang,D.Gan,M.Sun,N.Zhang,Z.Lu,andC.Kang,‘‘Probabilis-
themeasurestoenhancepowersystemsresilience,’’IEEESyst.J.,vol.14, ticindividualloadforecastingusingpinballlossguidedLSTM,’’Appl.
no.3,pp.4059–4070,Sep.2020. Energy,vol.235,pp.10–20,Feb.2019.
| VOLUME12,2024 |     |     |     |     |     |     |     |     |     |     |     |     | 111879 |
| ------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------ |

K.Ullahetal.:STLF:AComprehensiveReviewandSimulationStudy
[41] A. Ahmed and M. Khalid, ‘‘A review on the selected applications of [63] P.Li,K.Zhou,X.Lu,andS.Yang,‘‘Ahybriddeeplearningmodelfor
forecastingmodelsinrenewablepowersystems,’’Renew.Sustain.Energy short-term PV power forecasting,’’ Appl. Energy, vol. 259, Feb. 2020,
Rev.,vol.100,pp.9–21,Feb.2019. Art.no.114216.
[42] W.Kong,Z.Y.Dong,Y.Jia,D.J.Hill,Y.Xu,andY.Zhang,‘‘Short-term [64] S. O. Abter, S. M. Jameel, H. M. Majeed, and A. H. Sabry, ‘‘Intel-
residentialloadforecastingbasedonLSTMrecurrentneuralnetwork,’’ ligent forecasting temperature measurements of solar PV cells using
IEEETrans.SmartGrid,vol.10,no.1,pp.841–851,Jan.2019. modifiedrecurrentneuralnetwork,’’EUREKA,Phys.Eng.,vol.3,no.3,
[43] M. Barman and N. B. Dev Choudhury, ‘‘Season specific approach for pp.169–177,2024,doi:10.21303/2461-4262.2024.003354.
short-termloadforecastingbasedonhybridFA-SVMandsimilaritycon- [65] J.F.Torres,D.Hadjout,A.Sebaa,F.Martínez-Álvarez,andA.Troncoso,
cept,’’Energy,vol.174,pp.886–896,May2019. ‘‘Deeplearningfortimeseriesforecasting:Asurvey,’’BigData,vol.9,
[44] S.Aslam,H.Herodotou,S.M.Mohsin,N.Javaid,N.Ashraf,andS.Aslam, no.1,pp.3–21,Feb.2021.
‘‘Asurveyondeeplearningmethodsforpowerloadandrenewableenergy [66] X.Wang,Z.Yao,andM.Papaefthymiou,‘‘Areal-timeelectricalloadfore-
forecastinginsmartmicrogrids,’’Renew.Sustain.EnergyRev.,vol.144, castingandunsupervisedanomalydetectionframework,’’Appl.Energy,
Jul.2021,Art.no.110992. vol.330,Jan.2023,Art.no.120279.
[45] R.Wazirali,E.Yaghoubi,M.S.S.Abujazar,R.Ahmad,andA.H.Vakili, [67] N.Huang,S.Wang,R.Wang,G.Cai,Y.Liu,andQ.Dai,‘‘Gatedspatial–
‘‘State-of-the-art review on energy and load forecasting in microgrids temporalgraphneuralnetworkbasedshort-termloadforecastingforwide-
usingartificialneuralnetworks,machinelearning,anddeeplearningtech- areamultiplebuses,’’Int.J.Electr.PowerEnergySyst.,vol.145,Feb.2023,
niques,’’ElectricPowerSyst.Res.,vol.225,Dec.2023,Art.no.109792. Art.no.108651.
[46] N.Ghadimi,A.Akbarimajd,H.Shayeghi,andO.Abedinia,‘‘Twostage [68] Y.K.Semero,J.Zhang,andD.Zheng,‘‘EMD–PSO–ANFIS-basedhybrid
forecast engine with feature selection technique and improved meta- approach for short-term load forecasting in microgrids,’’ IET Gener.,
heuristic algorithm for electricity load forecasting,’’ Energy, vol. 161, Transmiss.Distrib.,vol.14,no.3,pp.470–475,Feb.2020.
pp.130–142,Oct.2018. [69] M.Luy,V.Ates,N.Barisci,H.Polat,andE.Cam,‘‘Short-termfuzzyload
[47] F.He,J.Zhou,Z.-K.Feng,G.Liu,andY.Yang,‘‘Ahybridshort-term forecastingmodelusinggenetic–fuzzyandantcolony–fuzzyknowledge
loadforecastingmodelbasedonvariationalmodedecompositionandlong baseoptimization,’’Appl.Sci.,vol.8,no.6,p.864,May2018.
short-termmemorynetworksconsideringrelevantfactorswithBayesian [70] D.Yang,J.-E.Guo,Y.Li,S.Sun,andS.Wang,‘‘Short-termloadforecast-
optimizationalgorithm,’’Appl.Energy,vol.237,pp.103–116,Mar.2019. ing with an improved dynamic decomposition-reconstruction-ensemble
[48] G.Dudek,‘‘Acomprehensivestudyofrandomforestforshort-termload approach,’’Energy,vol.263,Jan.2023,Art.no.125609.
forecasting,’’Energies,vol.15,no.20,p.7547,Oct.2022. [71] Z.Wang,T.Hong,andM.A.Piette,‘‘Buildingthermalloadprediction
[49] S.H.RafiandM.M.Mahdi,‘‘Ashort-termloadforecastingtechnique through shallow machine learning and deep learning,’’ Appl. Energy,
usingextremegradientboostingalgorithm,’’inProc.IEEEPESInnov. vol.263,Apr.2020,Art.no.114683.
SmartGridTechnol.,Dec.2021,pp.1–5. [72] S.Bouktif,A.Fiaz,A.Ouni,andM.A.Serhani,‘‘Multi-sequenceLSTM-
[50] K.Zhu,J.Geng,andK.Wang,‘‘Ahybridpredictionmodelbasedonpat- RNN deep learning and metaheuristics for electric load forecasting,’’
ternsequence-basedmatchingmethodandextremegradientboostingfor Energies,vol.13,no.2,p.391,Jan.2020.
holidayloadforecasting,’’ElectricPowerSyst.Res.,vol.190,Jan.2021, [73] L.Wen,K.Zhou,S.Yang,andX.Lu,‘‘Optimalloaddispatchofcommu-
Art.no.106841. nitymicrogridwithdeeplearningbasedsolarpowerandloadforecasting,’’
[51] J.Kim,J.Moon,E.Hwang,andP.Kang,‘‘Recurrentinceptionconvolution Energy,vol.171,pp.1053–1065,Mar.2019.
neuralnetworkformultishort-termloadforecasting,’’EnergyBuildings, [74] M.Sun,T.Zhang,Y.Wang,G.Strbac,andC.Kang,‘‘UsingBayesiandeep
vol.194,pp.328–341,Jul.2019. learningtocaptureuncertaintyforresidentialnetloadforecasting,’’IEEE
[52] A.Yang,W.Li,andX.Yang,‘‘Short-termelectricityloadforecastingbased Trans.PowerSyst.,vol.35,no.1,pp.188–201,Jan.2020.
onfeatureselectionandleastsquaressupportvectormachines,’’Knowl.- [75] B.Nepal,M.Yamaha,A.Yokoe,andT.Yamaji,‘‘Electricityloadfore-
BasedSyst.,vol.163,pp.159–173,Jan.2019. castingusingclusteringandARIMAmodelforenergymanagementin
[53] P.Du,J.Wang,W.Yang,andT.Niu,‘‘Anovelhybridmodelforshort- buildings,’’Jpn.ArchitecturalRev.,vol.3,no.1,pp.62–76,Jan.2020.
termwindpowerforecasting,’’Appl.SoftComput.,vol.80,pp.93–106, [76] T. Hong, J. Xie, and J. Black, ‘‘Global energy forecasting competition
Jul.2019. 2017: Hierarchical probabilistic load forecasting,’’ Int. J. Forecasting,
[54] A.-D.Pham,N.-T.Ngo,T.T.HaTruong,N.-T.Huynh,andN.-S.Truong, vol.35,no.4,pp.1389–1399,Oct.2019.
‘‘Predicting energy consumption in multiple buildings using machine [77] Z.ZhangandW.-C.Hong,‘‘Electricloadforecastingbycompleteensem-
learningforimprovingenergyefficiencyandsustainability,’’J.Cleaner ble empirical mode decomposition adaptive noise and support vector
Prod.,vol.260,Jul.2020,Art.no.121082. regression with quantum-based dragonfly algorithm,’’ Nonlinear Dyn.,
[55] S.H.Rafi,S.R.Deeba,andE.Hossain,‘‘Ashort-termloadforecasting vol.98,no.2,pp.1107–1136,Oct.2019.
methodusingintegratedCNNandLSTMnetwork,’’IEEEAccess,vol.9, [78] I.Shah,H.Iftikhar,S.Ali,andD.Wang,‘‘Short-termelectricitydemand
pp.32436–32448,2021. forecastingusingcomponentsestimationtechnique,’’Energies,vol.12,
[56] L.Zhang,J.Wen,Y.Li,J.Chen,Y.Ye,Y.Fu,andW.Livingood,‘‘Areview no.13,p.2532,Jul.2019.
ofmachinelearninginbuildingloadprediction,’’Appl.Energy,vol.285, [79] M.Alhussein,K.Aurangzeb,andS.I.Haider,‘‘HybridCNN-LSTMmodel
Mar.2021,Art.no.116452. forshort-termindividualhouseholdloadforecasting,’’IEEEAccess,vol.8,
[57] M.Tan,S.Yuan,S.Li,Y.Su,H.Li,andF.He,‘‘Ultra-short-termindustrial pp.180544–180557,2020.
powerdemandforecastingusingLSTMbasedhybridensemblelearning,’’
IEEETrans.PowerSyst.,vol.35,no.4,pp.2937–2948,Jul.2020.
[58] M.Bourdeau,X.Q.Zhai,E.Nefzaoui,X.Guo,andP.Chatellier,‘‘Model-
ingandforecastingbuildingenergyconsumption:Areviewofdata-driven
techniques,’’Sustain.CitiesSoc.,vol.48,Jul.2019,Art.no.101533.
[59] K.Yan,W.Li,Z.Ji,M.Qi,andY.Du,‘‘AhybridLSTMneuralnetworkfor KALEEM ULLAH received the Ph.D. degree in
energyconsumptionforecastingofindividualhouseholds,’’IEEEAccess, electrical engineering (power) from the Univer-
vol.7,pp.157633–157642,2019. sity of Engineering and Technology, Peshawar.
[60] M. Massaoudi, S. S. Refaat, I. Chihi, M. Trabelsi, F. S. Oueslati, and
HeiscurrentlyanaccomplishedElectricalEngi-
H.Abu-Rub, ‘‘A novel stacked generalization ensemble-based hybrid
neer specializing in power systems. During the
LGBM-XGB-MLP model for short-term load forecasting,’’ Energy,
Ph.D. study, he conducted extensive research
vol.214,Jan.2021,Art.no.118874.
on real-time dynamic dispatch strategies for
[61] J.F.Bermejo,J.F.G.Fernández,F.O.Polo,andA.C.Márquez,‘‘Areview
automatic generation control (AGC) and load
oftheuseofartificialneuralnetworkmodelsforenergyandreliability
prediction.AstudyofthesolarPV,hydraulicandwindenergysources,’’ forecasting mechanisms focusing on integrating
Appl.Sci.,vol.9,no.9,p.1844,May2019. large-scaleRESpowerintothegridwhilemain-
[62] S. Akhtar, S. Shahzad, A. Zaheer, H. S. Ullah, H. Kilic, R. Gono, taining active power balance and enhancing system reliability. USAID
M.Jasinski,andZ.Leonowicz,‘‘Short-termloadforecastingmodels:A Pakistanfundedhisworkthroughanappliedresearchgrant.Hesecureda
reviewofchallenges,progress,andtheroadahead,’’Energies,vol.16, significantgrantfromPakistanScienceFoundationforhisresearchproject
no.10,p.4060,May2023. onloaddispatchcontrolforPakistanPowerSystem.
111880 VOLUME12,2024

K.Ullahetal.:STLF:AComprehensiveReviewandSimulationStudy
MUHAMMAD AHSAN received the B.Eng. SYEDFARAZRAZAreceivedtheB.Eng.degree
degree in electrical engineering from the NED in electronic engineering from the NED Uni-
UniversityofEngineeringandTechnologyandthe versityofEngineeringandTechnology,Karachi.
master’sdegreeindatasciencefromtheUniversity He is currently pursuing the master’s degree in
ofAlabamaatBirmingham.Heisequippedwith data science from the University of Alabama
astrongfoundationinelectricalengineeringand atBirmingham.Demonstratingacommitmentto
data science. His dedication to his field is evi- academicexcellenceandapassionforadvancing
dentthroughhiscommitmenttostayingupdated hisknowledge,heispursuingthemaster’sdegree.
withthelatestadvancementsindatascienceand He is focusing his skill set on machine learning
itsapplications.Hisresearchinterestsincludethe andartificialintelligencetosupporttheresearch
intersection of data science and electrical engineering, where he aims to effortsinthecriticalareaofshort-termloadforecasting.
developinnovativesolutionstocomplexproblems.
|     |     |     |     |     |     |     |     | RITESH | TANDON | received | the master’s | degree |
| --- | --- | --- | --- | --- | --- | --- | --- | ------ | ------ | -------- | ------------ | ------ |
indatasciencefromIndianaUniversity,Bloom-
ington,IN,USA.Heiscurrentlyanaccomplished
|     |     | SYED MUHAMMAD |     | HASANAT    | received    | the  |     |           |            |      |                   |     |
| --- | --- | ------------- | --- | ---------- | ----------- | ---- | --- | --------- | ---------- | ---- | ----------------- | --- |
|     |     |               |     |            |             |      |     | Lead Data | Scientist. | With | a career spanning |     |
|     |     | B.Sc. degree  | in  | electrical | engineering | from |     |           |            |      |                   |     |
the University of Engineering and Technology, over two decades in the information technology
Peshawar. He is currently pursuing the master’s industry, he has been at the forefront of the
degree in electrical energy system engineering machinelearningandartificialintelligencerevolu-
withCenterforAdvancedStudiesinEnergy,UET tion.Since2019,hehasbeenwithPLIC,wherehis
Peshawar.Heisfocusinghisresearcheffortson passionforAIhasdrivenhimtodesignandimple-
mentcutting-edgedatasoftwareproductstailored
|     |     | the critical | area of | short-term | load forecasting. |     |                   |                         |     |            |         |          |
| --- | --- | ------------ | ------- | ---------- | ----------------- | --- | ----------------- | ----------------------- | --- | ---------- | ------- | -------- |
|     |     |              |         |            |                   |     | for the insurance | industry. His expertise | in  | developing | machine | learning |
Heisdedicatedtoaddressingthechallengesand
modelshasbeeninstrumentalinoptimizingcostsandmitigatingrisksfor
complexitiesinherentinenergysystemsmanage-
hiscompany.HisworkinNLPhasledtoinnovativesolutionsfordocument
ment.Hisscholarlypursuitshavegarneredrecognition,withhisworkbeing
|     |     |     |     |     |     |     | classification | and question-answering | models. | In addition, | he has | signifi- |
| --- | --- | --- | --- | --- | --- | --- | -------------- | ---------------------- | ------- | ------------ | ------ | -------- |
publishedinnumerousimpactfuljournalsinrecentyears.
cantlycontributedtospeech-to-texttechnology,extractingvaluableinsights
|     |     |     |     |     |     |     | from spoken | language. Dedicated | to advancing | AI, | he is committed | to  |
| --- | --- | --- | --- | --- | --- | --- | ----------- | ------------------- | ------------ | --- | --------------- | --- |
architectingandimplementingintelligentsolutionsthatpushtheboundaries
oftechnology.
MUHAMMADHARISreceivedtheB.Sc.degree
inmathematicsandeconomicsfromLahoreUni-
versityofManagementSciences,in2021.Heis
SAMAINABIDreceivedtheB.Sc.degreeincom-
currentlypursuingtheM.S.degreeindatascience puter science from the Sir Syed University of
andanalyticswithGeorgiaStateUniversity.Heis EngineeringandTechnology.Heiscurrentlypur-
also a Graduate Research Assistant at Georgia suing the master’s degree in data science with
StateUniversity,collaboratingwithTruistBank’s the University of Alabama at Birmingham. His
ESGandClimateDataandAnalyticsTeam.Hehas
|     |     |             |            |         |          |        |     | research | primarily | focuses on | machine | learning |
| --- | --- | ----------- | ---------- | ------- | -------- | ------ | --- | -------- | --------- | ---------- | ------- | -------- |
|     |     | significant | experience | in data | science, | having |     |          |           |            |         |          |
predictivemodels,whereheaimstosolvecomplex
|     |     | worked at | Afiniti Inc., | where | he optimized | cus- |     |     |     |     |     |     |
| --- | --- | --------- | ------------- | ----- | ------------ | ---- | --- | --- | --- | --- | --- | --- |
problemsindataanalytics.Hisdedicationtohis
| tomer retention | and | developed predictive | models. | In  | this role, | he applies |     |     |     |     |     |     |
| --------------- | --- | -------------------- | ------- | --- | ---------- | ---------- | --- | --- | --- | --- | --- | --- |
fieldisevidentthroughhisinnovativeapproachto
| advanced | NLP techniques | and generative | AI  | to enhance | climate-related |     |     |     |     |     |     |     |
| -------- | -------------- | -------------- | --- | ---------- | --------------- | --- | --- | --- | --- | --- | --- | --- |
addressingthechallengesindatascience.
financialdisclosures.Hisresearchinterestsincludemachinelearning,LSTM
networks,andnaturallanguageprocessing(NLP).
|     |     |     |     |     |     |     |     | ZAHID       | ULLAH    | (Graduate       | Student Member, |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------- | -------- | --------------- | --------------- | --- |
|     |     |     |     |     |     |     |     | IEEE)       | received | the B.S. degree | in electrical   |     |
|     |     |     |     |     |     |     |     | engineering | from     | UET Peshawar,   | in 2014,        | and |
HAMZA YOUSAF received the B.B.A. degree the M.S. degree in electrical engineering from
(Hons.) from Lahore School of Economics, COMSATS University Islamabad, Abbottabad
Pakistan, in 2016, and the M.S. degree in busi- Campus, Abbottabad, Pakistan, in 2017. He is
nessanalyticsfromtheStetson-HatcherSchoolof currently pursuing the Ph.D. degree in electri-
Business, Mercer University, Macon, GA, USA, calengineeringwithPolitecnicodiMilano,Italy.
in 2024. He was an Analyst in various multina- He was a Lecturer with UMT Lahore, Pakistan.
tionalcorporations,leveraginghisdatascienceand Hisresearchinterestsincludesmartgrids,energy
analyticsexpertise.Hisresearchinterestsinclude management,renewableenergysystems,AIforenergy,andICTsforpower
|     |     | machinelearning,deeplearning,predictivemod- |     |     |     |     | systems. |     |     |     |     |     |
| --- | --- | ------------------------------------------- | --- | --- | --- | --- | -------- | --- | --- | --- | --- | --- |
eling,sentimentanalysis,andanomalydetection.
OpenAccessfundingprovidedby‘PolitecnicodiMilano’withintheCRUICAREAgreement
| VOLUME12,2024 |     |     |     |     |     |     |     |     |     |     |     | 111881 |
| ------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------ |