---
conversion_metadata:
  converted_at: "2026-07-21T08:50:17Z"
  converter_tool: "markitdown"
  converter_version: "0.1.6"
  source_pdf: "Sonkavde et al.pdf"
  source_pdf_sha256: "2f18f5621edef0660100ffecbfef797bb9f16d5b35182f3ea86a6a58a70f0c23"
  page_count: 22
  markdown_char_count: 155457
---

<!-- PAGE-AWARE EXTRACTION (via pdfminer.six) -->

<!-- PAGE 1 -->

Review
Forecasting Stock Market Prices Using Machine Learning and
Deep Learning Models: A Systematic Review, Performance
Analysis and Discussion of Implications

Gaurang Sonkavde 1, Deepak Sudhakar Dharrao 2,*
and Subraya Krishna Bhat 5
Deepak Doreswamy 4

, Anupkumar M. Bongale 1,*

, Sarika T. Deokate 3

,

1 Department of Artiﬁcial Intelligence and Machine Learning, Symbiosis Institute of Technology, Symbiosis
International Deemed University, Pune 412115, Maharashtra, India; gaurangsonkavade@gmail.com

2 Department of Computer Science & Engineering, Symbiosis Institute of Technology, Symbiosis International

Deemed University, Pune 412115, Maharashtra, India

3 Department of Computer Engineering, Pimpri Chinchwad College of Engineering,

Pune 411044, Maharashtra, India; sarika.deokate@pccoepune.org

4 Department of Mechatronics, Manipal Institute of Technology, Manipal Academy of Higher Education,

Manipal 576104, Karnataka, India; deepak.d@manipal.edu

5 Department of Mechanical and Industrial Engineering, Manipal Institute of Technology, Manipal Academy of

Higher Education, Manipal 576104, Karnataka, India; sk.bhat@manipal.edu

* Correspondence: deepak.dharrao@sitpune.edu.in (D.S.D.); anupkumar.bongale@sitpune.edu.in (A.M.B.)

Abstract: The ﬁnancial sector has greatly impacted the monetary well-being of consumers, traders,
and ﬁnancial institutions. In the current era, artiﬁcial intelligence is redeﬁning the limits of the
ﬁnancial markets based on state-of-the-art machine learning and deep learning algorithms. There
is extensive use of these techniques in ﬁnancial instrument price prediction, market trend analysis,
establishing investment opportunities, portfolio optimization, etc. Investors and traders are using
machine learning and deep learning models for forecasting ﬁnancial instrument movements. With
the widespread adoption of AI in ﬁnance, it is imperative to summarize the recent machine learning
and deep learning models, which motivated us to present this comprehensive review of the practical
applications of machine learning in the ﬁnancial industry. This article examines algorithms such
as supervised and unsupervised machine learning algorithms, ensemble algorithms, time series
analysis algorithms, and deep learning algorithms for stock price prediction and solving classiﬁcation
problems. The contributions of this review article are as follows: (a) it provides a description of
machine learning and deep learning models used in the ﬁnancial sector; (b) it provides a generic
framework for stock price prediction and classiﬁcation; and (c) it implements an ensemble model—
“Random Forest + XG-Boost + LSTM”—for forecasting TAINIWALCHM and AGROPHOS stock
prices and performs a comparative analysis with popular machine learning and deep learning models.

Keywords: stock market; ﬁnance; linear regression; random forest; XG-Boost; FB Prophet; LSTM;
ensemble learning; blending ensemble

Citation: Sonkavde, Gaurang,

Deepak Sudhakar Dharrao,

Anupkumar M. Bongale, Sarika T.

Deokate, Deepak Doreswamy, and

Subraya Krishna Bhat. 2023.

Forecasting Stock Market Prices

Using Machine Learning and Deep

Learning Models: A Systematic

Review, Performance Analysis and

Discussion of Implications.

International Journal of Financial

Studies 11: 94. https://doi.org/

10.3390/ijfs11030094

Academic Editor: Muneer

M. Alshater

Received: 22 April 2023

Revised: 13 July 2023

Accepted: 19 July 2023

Published: 26 July 2023

1. Introduction

Copyright: © 2023 by the authors.

Licensee MDPI, Basel, Switzerland.

This article is an open access article

distributed under

the terms and

conditions of the Creative Commons

Attribution (CC BY) license (https://

creativecommons.org/licenses/by/

4.0/).

The performance of a country’s ﬁnancial market is a crucial determinant of its overall
economic condition, enabling economists and ﬁnancial experts to gauge the country’s
current economic health. Among the various ﬁnancial markets, the stock market stands
out as a key driving force. A country’s economic situation directly or indirectly impacts
sectors such as ﬁnance, agriculture, metal, and investment banking, among others. The
growth of these sectors hinges on their volatility, which follows the fundamental principle
of supply and demand. The demand for a particular sector directly inﬂuences the stock
market, with increased supply prompting traders and ﬁnancial institutions to invest in that
sector or stock, driving up prices. Additionally, regular dividend payments contribute to

Int. J. Financial Stud. 2023, 11, 94. https://doi.org/10.3390/ijfs11030094

https://www.mdpi.com/journal/ijfs

---

<!-- PAGE 2 -->

Int. J. Financial Stud. 2023, 11, 94

2 of 22

the generation of proﬁts and returns on invested capital. It is imperative for investors to
identify the opportune moment to sell shares and achieve their desired returns. Financial
markets encompass various types of market, including stock markets, derivatives markets,
bond markets, and commodity markets (Obthong et al. 2020). The stock market serves as a
platform for investors to invest in and own a portion or fraction of a company. As companies
grow, they often require additional funding to support their future endeavors. Following
the approval of current shareholders, who face diluted ownership due to the issuance
of new shares, companies can sell these shares to investors to raise capital. Successful
outcomes result in increased stock market value for the shares.

Shares listed on the stock market can be bought for both short-term and long-term
investment strategies. Long-term investment involves holding shares over an extended
period, while short-term investments involve buying and selling shares within shorter
timeframes, with investors aiming for proﬁts within days or weeks. Traders employ a wide
range of trading strategies, including swing trading, day trading, position trading, and
scalping (Mann and Kutz 2016).

Due to the unpredictable nature of the stock market, it is highly difﬁcult for individu-
als to obtain returns on their investments. Primary, fundamental, and technical analysis
are popular approaches to understanding market trends (Manish and Thenmozhi 2014),
but they possess inherent limitations due to the involvement of lagging indicators and
prediction inaccuracy. This has motivated researchers to develop improved techniques for
real-time market scenarios based on machine learning and deep learning models. In the cur-
rent era, machine learning and deep learning algorithms offer substantial advantages over
traditional techniques such as technical and fundamental analysis. Leveraging the power
of machine learning and artiﬁcial intelligence, these algorithms facilitate the forecasting
of stock prices and indices. Machine learning serves as an additional approach alongside
technical and fundamental analysis, with the combination of these tools forming a powerful
trading platform. Machine learning models can provide solutions to problems such as
stock price forecasting and classiﬁcation, portfolio management, algorithmic trading, stock
market sentiment analysis, risk assessment, etc. Of these problems, this review article
is focused on exploring different approaches described for stock price forecasting and
classiﬁcation.

The typical steps of a machine learning model pipeline for predicting stock price
involve several phases: collecting historical data via an API, pre-processing the data, creat-
ing a forecasting model, and evaluating the model. Pre-processing entails removing zero
values, eliminating duplicates, and scaling features. Subsequently, important features are
shortlisted, and valid data are selected for stock price prediction or forecasting (Raghaven-
dra et al. 2021). In this article, numerous popular machine learning and deep learning
algorithms, such as linear regression, random forest, logistic regression, k-nearest neighbor,
support vector machine, naïve Bayes, ARIMA (autoregressive integrated moving average),
FB Prophet (Facebook Prophet), LSTM (long short-term memory), GRU (gated recurrent
network), as well as ensemble algorithms such as random forest and XG-Boost (extreme
gradient boosting), are described (Zhong and Enke 2019; Sidra and Sen 2020; Parray et al.
2020). For evaluating a classiﬁcation model’s accuracy, recall, precision, and F-score, are
commonly preferred metrics, and for regression or price forecasting models, root mean
square error (RMSE) and mean absolute percentage error (MAPE) are often employed (Jose
et al. 2019).

There are a signiﬁcant number of review articles on stock price prediction and fore-
casting (Polamuri et al. 2019; Kumar et al. 2021; Soni et al. 2022). But due to the boom in
artiﬁcial intelligence and machine learning, the frequency of publications has increased
considerably. Hence, this review article presents recent state-of-the-art machine learning
and deep learning techniques for stock price prediction. The salient contributions and
uniqueness of this review article are listed below:
• One of the unique contributions of this review article is that it is not just limited to
summarizing the research articles. Extra effort is put into implementing the well-

---

<!-- PAGE 3 -->

Int. J. Financial Stud. 2023, 11, 94

3 of 22

known machine learning and deep learning models to understand their nature and
performance. Along with our review, a comparative analysis of various algorithms is
presented in this article. The machine learning and deep learning ensemble algorithms
are tested on TAINIWALCHM and AGROPHOS stock data, which fall under the
umbrella of the chemical industry market sector.
In this review article, detailed future research directions are included. Future research
avenues for researchers are identiﬁed based on the conducted study stock trend
analysis and classiﬁcation, pattern identiﬁcation, and candlestick chart pattern analysis
using computer vision.

•

The rest of the article is organized as follows. Section 2 describes the complete theo-
retical background of machine learning and deep learning models. A generic structure of
the machine learning modeling pipeline is presented in Section 3. The importance of the
ensemble model “Random Forest + XG-Boost + LSTM” for forecasting TAINIWALCHM
and AGROPHOS stock prices and a comparative analysis with popular machine learning
and deep learning models are mentioned in Section 4. Section 5 discusses the implications
and limitations of the current review. Future research directions are given in Section 6.
Finally, the paper is concluded in Section 7.

2. Comprehensive Summary of Theoretical Basis

Forecasting stock prices and predicting market trends are challenging tasks. Over
the years, researchers have proposed several solutions to these challenges (Obthong et al.
2020; Hu et al. 2021; Polamuri et al. 2019), and these methods are brieﬂy explained below.
Machine learning, deep learning, time series forecasting, and ensemble algorithms are
some of the most popular approaches to solving the mentioned problems. Ensemble
algorithms can improve accuracy and reduce RMSE. Hadoop architectures can also handle
large volumes of stock data (Jose et al. 2019) and deep learning algorithms can predict
ﬁnancial markets (Hu et al. 2021). Stock forecasting using LSTM, a unique recurrent neural
network (RNN), overcomes long-term dependency (Qiu et al. 2020; Banik et al. 2022). But
the vanishing gradient and exploding gradient problems often need to be addressed in
RNN-based architectures (Li and Pan 2021; Zhu 2020). Khan et al., in (Khan et al. 2020),
used Pyspark, MLlib, linear regression, and random forest to achieve 80–98% accuracy.

Multiple algorithms have been used to forecast stock prices, including neural networks,
which train data on layers of connected neurons, and support vector machines, which
predict stock price movement using hyperplanes. Random forest, trained on multiple
decision trees and Naïve Bayes, predicts stock movement based on negative or positive
probability using Reliance and Infosys’ 10-year historical data (Patel et al. 2015). Random
forest is compared to other algorithms on 5767 European companies. These algorithms
include neural networks, which are multiple layers of neurons connected with each other;
logistic regression, which outputs a binary value to predict whether the stock will move up
or down based on probability; support vector machines; and K-Nearest neighbor, which
ﬁnds the k nearest data points using Euclidean similarity metrics. Random forest is the best
algorithm, followed by SVM (Ballings et al. 2015).

Stock market forecasting is a regression use case because stock prices are continuous
(Seethalakshmi 2018). (Di Persio and Honchar 2017), used RNN for forecasting Google stock
prices. RNN, LSTM, and GRU are the three most efﬁcient neural networks for sequential
data. RNN is used for historical data. LSTM and GRU can avoid the vanishing gradient
problem based on forget, reset, and update gates. GRU is found to be faster as it operates
on reset and update gates (Di Persio and Honchar 2017).

Another study involves the use of ARIMA, LSTM, and random forest for price fore-
casting, and XG-Boost, an ensemble learning algorithm like random forest. Based on the
evaluation parameters, XG-Boost outperformed ARIMA and LSTM (Zhu and He 2022).
Isaac et al. also used ensemble machine learning to improve stock market forecasting results.
Cooperative and competitive classiﬁer algorithms use stacking and blending. Bagging and
boosting techniques are used to reduce variance and bias. Most ensemble classiﬁers and

---

<!-- PAGE 4 -->

Int. J. Financial Stud. 2023, 11, 94

4 of 22

regressors are developed by combining decision trees, support vector machines, and neural
networks (Nti et al. 2020). Similarly, (Xu et al. 2020) also used bagging ensemble learning
techniques to predict Chinese stocks. This approach combines a two-stage prediction model
called “Ensemble Learning SVR and Random Forest (E-SVR&RF)” with KNN to cluster it
with ten technical indicators. Another proposed method uses Ensemble LSTM with CNN
on stock indexes for training adversarial networks, which can help forecast high-frequency
stock and has advantages like adversarial training and reducing direction prediction loss
and forecast error loss (Zhou et al. 2018). To enhance the effectiveness of ensemble model
of XG-Boost and LSTM, XG-Boost is used to select features applied to high-dimensional
time series data and LSTM is used for stock price forecasting (Vuong et al. 2022).

Not only have machine learning ensemble methods helped to improve forecasting
performance, but in some research work, it has also been observed that neural network
blending ensemble models also perform well. (Yang 2019) implemented a model consisting
of two layers of RNN. The ﬁrst one was an LSTM-based blending ensemble algorithm, and
the second one was GRU-based. The model showed the lowest RMSE value of 186.32, a
precision of 60%, and an F1-score of 66.47 (Li and Pan 2021).

Sometimes, price movement is primarily affected by sentiments. These sentiments can
be positive, leading to a bullish movement, or negative, leading to a bearish movement.
Hence, stock sentiment analysis is important to understand stock price forecasting and
trend classiﬁcation. Further, in this section, we explore some forecasting techniques based
on sentiment analysis. Social media data, company news, and trend analysis can classify
investors’ stock sentiments as positive, negative, or neutral (Yadav and Vishwakarma 2019).
Since stock prices respond to news and global events, price variation alone cannot be
used to train ML models. ANN- and LSTM-based deep learning techniques can also be
trained using price values and text data. Word2vec and NGram are used to convert text
data to numerical data and train the model together with price-sentiment data. Diversiﬁed
data can predominantly increase accuracy and lower inaccurate results. An algorithm like
a random forest approach is also a good choice for Twitter sentiment analysis (Kumar and
Ningombam 2018; Reddy et al. 2020).

Financial news and user-generated text, such as comments on social media platforms,
can trigger new trends in the stock market. For example, “Monday has the lowest average
return” shows a statement representing a weak or negative sentiment.

While creating the dataset for training the model, a rolling window approach on historical
data works well with news-based text data. Ren et al. showed an increase in accuracy of up to
18.6% to 89.93% points when multimodal data were considered (Ren et al. 2019).

When text data are collected, they can include correct and fake data. In one study, the
authors used feature selection to eliminate fake news and spam tweets collected from social
media data. This improved the data quality for training, and a classiﬁcation algorithm, the
random forest algorithm, was used to train the model. Sentiments can be positive, neutral,
or negative, which helps people decide whether to buy or sell stock (Baheti et al. 2021).
Negative sentiments affect market conditions. Lim et al. considered a use case in which
a comparison of two stocks, Tesla and Nio, based on sentiments, was carried out. It was
found that negative events, such as Tesla’s 2021 protest, affected its competitor, Nio, as well.
This research was based on historical data using time series forecasting with 10, 15, and 20
days of data (Lim and Tan 2021).

In (Sharaf et al. 2022), news headlines pertaining to TSLA, AMZ, and GOOG stock were
considered to obtain good-quality data to reduce spam tweets through feature selection methods.
Sentiment analysis was also used for polarity detection and historical data mining, for which
DL algorithms were used. Similar feature engineering- and deep learning-based approaches are
presented in (Shen and Shafiq 2020; Nabipour et al. 2020; Mohapatra et al. 2022).

(Khairi et al. 2019) showed that technical analysis with sentiment analysis can also
provide prominent investment opportunities. Technical indicators like stochastic oscillators,
moving average convergence divergence (MACD), Bollinger bands, and relative strength
indicators (RSI) are good for short-term analysis but not long-term. In cases of negative

---

<!-- PAGE 5 -->

Int. J. Financial Stud. 2023, 11, 94

5 of 22

news, generally, market trends will be bearish, and the stock price will fall. To address
this issue, initial sentiment analysis can be performed to ﬁnd the negative news using PoS
(part of speech) tags in the news statement. Programming libraries like SentiWordNet
can be used for PoS tagging. This approach has resulted in high proﬁtability and low
loss-making situations (Khairi et al. 2019). In another approach proposed by Li et al. (Li
and Bastos 2020), a technical analysis of historical data and a fundamental analysis using a
deep learning approach were conducted to generate better returns. Here, LSTM is chosen
for prediction as it can store memory and does not have a vanishing gradient issue (Li and
Bastos 2020). Similar work is presented in (Agrawal et al. 2022; Sathish Kumar et al. 2020;
Umer et al. 2019).

Based on the studies presented so far, the best stock market forecasting solution is
derived from fundamental analysis and technical analysis with sentiment analysis and deep
learning models. Ensemble techniques provide especially promising forecasting outcomes.
The algorithms that are used for stock market prediction by considering research papers
are given in Figure 1.

Figure 1. Stock forecasting algorithm.

2.1. Basic Machine Learning Algorithm
2.1.1. Linear Regression

Linear regression is used for stock or ﬁnancial market prediction to forecast the future
price of stock regression and uses a model based on one or more attributes, such as closed
price, open price, volume, etc., to forecast the stock price. Regression modeling aims to
simulate the linear relationship between the dependent and independent variables. The
linear regression model produces a best-ﬁt line that describes the connection between the
independent factors and the dependent variable.

In this technique, a straight line represented by Equation (1) is drawn, ensuring that
the line crosses the highest possible number of the dataset’s data points. When charting
the dataset’s values on a graph, a straight line is mathematically ﬁtted between the points
so that the square of the distance or difference between each point and the line is as small
as possible. For each given x, the hypothesis line is used to forecast the value of y. This
forecasting method is known as linear regression. For the evaluation of the results and
to check how well the model ﬁts the line, parameters such as RMSE, MAE, MSE, and
R-squared are used (Gururaj et al. 2019; Dospinescu and Dospinescu 2019).

O = Sx + K

(1)

---

<!-- PAGE 6 -->

Int. J. Financial Stud. 2023, 11, 94

6 of 22

where O is the output, Sx represents the slope, and K is a constant.

2.1.2. K-Nearest Neighbor (KNN)

KNN is a classiﬁcation and regression technique and has been termed as a lazy learner
because it does not need a huge time period for learning. One of KNN’s advantages is that
it is one of the easiest ML algorithms. The only action that needs to be taken for KNN is to
calculate the value of K and the Euclidean distance. This algorithm’s slow learning aspect
makes it quicker than other algorithms. It may not generalize well for big data since it
skips the learning step (Tanuwijaya and Hansun 2019). The euclidean distance calculation
is given in Equation (2),

D(hi, pr) =

(cid:113)∑n..

l=1

(Pr − hi)2

(2)

where Pr represents the predicted value and hi represents the data value.

2.1.3. Support Vector Machine (SVM)

Stock market prediction using an SVM can be the most useful technique for predicting
stock price, as it can be used as a classiﬁcation and regression algorithm. The comparison of
SVM and its variants, such as “Peeling + SVM” and “CC + SVM”, shows that its prediction
can be improved by advanced SVM methods (Grigoryan 2017). A support vector machine
involves supervised learning used to categorize aspects using a separator. The separator is
then discovered when the data are initially mapped to a high-dimensional feature space. It
ﬁnds the categorization of data points occurring in an n-dimensional space and ﬁnds the
optimal hyperplane. The data points are grouped according to their location in relation
to the hyperplanes. The performance of the SVM algorithm can be elevated by tuning
parameters such as regularization, gamma, and kernel parameters (Bustos et al. 2017).
SVM can also be used for sentiment analysis to assess investors’ sentiments, which would
indirectly affect market conditions. It is well suited to both high-dimensional datasets and
small-scale datasets.

2.1.4. Naïve Bayes Algorithm

Naïve Bayes is a supervised machine learning technique that can be used to forecast

prices of various stocks in research on banking stock.

Naïve Bayes is a classiﬁcation algorithm in which a combination of probability sum-
ming up the frequencies and value combinations is taken from a dataset. Depending on the
values of the class variables, the Bayes theorem makes an assumption regarding whether
the attributes of naïve Bayes are independent or interdependent. The basic concept of
naïve Bayes is that attribute values are independent in the presence of an output value
(Setiani et al. 2020). The set up GNB models were graded based on their performance using
Kendall’s test of concordance for several assessment parameters. The outcomes showed
that the GNB LDA predictive model (Kardani et al. 2020) performed better than all other
GNB models. The posterior probability was calculated as shown in Equation (3) (Ampomah
et al. 2021).

P(H|U) =

P(U|H) · P(H)
P(U)

(3)

where U is unknown class data, H is the hypothesis for data of certain class, P(H) is the
hypothesis probability, P(U|H) is the probability of U being dependent on the condition
in hypothesis H, and P(U) is the probability of U.

The formula for naïve Bayes used in stock prediction is given by Equation (4):

P(Ai = a1|B = bi) =

√

)2

(ai −µij
.
2€4
ij

−

e

1
2π€

(4)

where π represents pi (3.14), e is the exponential (2.7183), µ represents the mean, and € is
the standard deviation.

---

<!-- PAGE 7 -->

Int. J. Financial Stud. 2023, 11, 94

7 of 22

2.1.5. Logistic Regression

Logistic regression is a supervised method of machine learning. By utilizing variables
for logistic curves, logistic regression groups several independent factors into two or more
mutually exclusive groups and forecasts the likelihood of equities that perform well (Ali
et al. 2018). To classify stock performance using logistic regression, the maximum likelihood
is calculated as per Equation (5):

Zit = β1 + β2EPSit + β2PBit + β2ROEit + β2CRit + β2DEit + β2salesit + Vit

(5)

where z = loglog

and Pr = probability of outcome is positive.
There are variants, such as binary logistic regression, that can improve ﬁnance ratios

(cid:17)

(cid:16) Pr
1−Pr

and investors’ ability to anticipate stock price (Smita 2021).

2.2. Forecasting of Stock Market Using Time Series Forecasting

Stock price data are time series data. Some of the classical methods, such as autore-
gressive moving average (ARIMA) and FB Prophet, are discussed in this subsection. These
methods were very well adopted before the success of deep learning models.

2.2.1. ARIMA

ARIMA is an algorithm that uses time series forecasting to predict the future value of
stocks. In a study presented by Tamerlan et al., in (Mashadihasanli 2022), it is demonstrated
that the ARIMA model best ﬁts the stock market index. The ARIMA model comprises
three steps—identify, estimate, and diagnose. These steps can be used for forecasting
any ﬁnance market such as equity, derivative, etc. (Mashadihasanli 2022). ARIMA can
be combined with another algorithm, symmetric generalized autoregressive conditional
heteroskedasticity (SGARCH), to improve forecasting performance. This combination has
been modeled and tested on the S&P500 Index (Vo and ´Slepaczuk 2022). ARIMA has even
been extended for stock sentiment analysis (Kedar 2021).

The formula of ARIMA, which combines AR (autoregression) and MA (moving aver-

age), is shown in Equation (6),

y(cid:48)(t) = k + β p ∗ ωD y(cid:48)

t−1 + · · · + β p ∗ ωDy(cid:48)

t−p + θ1 ∗ εt−1 + · · · + θq ∗ ε(ti−q) + εti

(6)

where p represents the autoregressive model’s given degree, D is the degree of different
orders, and q is the moving average’s given degree.

2.2.2. FB Prophet Model

FB Prophet is a time series forecasting library developed by Facebook. FB Prophet
better suits data that have a null value and it relatively shows more accurate results in such
situations. The formula of FB Prophet is presented in Equation (7):

Yt = l(t) + sp(t) + v(t) + εt, y t = g(t) + s(t) + h(t) + εn

(7)

where l(t) represents the linear trend, sp(t) represents seasonal patterns, v(t) represents
holiday effects, and εn is the white noise error. The algorithm designed based on FB Prophet
is implemented using the PyStan library (Suresh et al. 2022). Researchers have extensively
used FB Prophet in stock price forecasting (Kaninde et al. 2022; Shahi et al. 2020).

2.3. Deep Learning Methods

Deep learning models have wide-ranging popularity in many areas of science and
engineering. They are especially widely adopted in stock price forecasting and trend
prediction due to their ability to capture complex patterns, handle large volumes of data,
and undertake feature learning and representation, and their adaptability to changing
market conditions. In this subsection, some of the popular deep learning models are
discussed in relation to the ﬁnance domain.

---

<!-- PAGE 8 -->

Int. J. Financial Stud. 2023, 11, 94

8 of 22

2.3.1. Long Short-Term Memory (LSTM)

LSTM is an advanced model of Recurrent Neural Networks (RNNs), a deep learning
algorithm. An LSTM model can handle lengthy sequences of data units as it can remember
the data sequence, which can be used for future inputs. Figure 2 shows a general LSTM
cell structure. It comprises three gates—the input gate, the forget gate, and the output gate.
All of the gates employ the sigmoid activation function. All of the gates used in the LSTM
are mathematically represented as per Equations (8)–(10).

Figure 2. LSTM structure.

Input gate (New information in cell state):

iga = σ (cid:0)Wip [ht−1, Xc] + bi(cid:1)

Forget gate (useless information is eliminated):

(cid:16)

fga = σ

Wf g [ht−1, Xc] + b f

(cid:17)

Output gate (activation to last block of ﬁnal output):

Opg = σ (cid:0)Wop [ht−1, Xc] + bo(cid:1)

(8)

(9)

(10)

where σ is sigmoid, Wx is the neuron gate (x) weight, ht−1 is the result of the preceding
LSTM block, Xt is the input, and bx is bias.

As shown in Figure 2, the top part of the memory line in every cell can be used to
connect with the transport line with the help of the model, which can be used to handle
the data from the prior memory to the current memory. Each LSTM node should have a
set of cells that is used for storage of the data stream (Pramod and Pm 2021). In order to
provide a recursive network with plenty of time to train and allow for the creation of a
long-distance causal link, LSTM maintains errors at a more constant level (Mukherjee et al.
2021). In several cases, neural networks and deep neural networks have shown superior
forecasting performance compared to other machine learning models. However, when it
comes to predicting ﬁnancial distress, the logistic regression model has exhibited better
results in comparison to neural networks (Zizi et al. 2021).

2.3.2. Gated Recurrent Neural Network (GRU)

A GRU is yet another RNN-based model with comparable differences to LSTM. It
is computationally efﬁcient and faster to train than LSTM, while capturing long-term
dependencies in sequential data. GRU utilizes gating mechanisms to control the ﬂow of
information between the current and previous time steps. However, it utilizes only two
gates, a reset gate and an update gate, whereas LSTM has three gates. Figure 3 shows the
general structure of a GRU.

---

<!-- PAGE 9 -->

Int. J. Financial Stud. 2023, 11, 94

9 of 22

Figure 3. GRU structure.

The two gates that GRU uses are:

(1) Update gate

(2) Reset gate

Z[t] = σ (W(z)xt + U(z)ht−1)

(11)

r[t] = σ (W(r)xt + U(r)ht−1)
(12)
where Z[t] is update gate, r[t] is reset gate, σ represents sigmoid function, W(x) is
neuron gate, U(x) is previous weight, ht−1 is the result of the preceding GRU block,
and xt is the current input.
For stock price data, GRU receives the input as a sequence of historical stock prices
and generates the output as a sequence of predicted stock prices. The input sequence is
fed through the GRU network, which updates its internal state at each time step, and the
network’s ﬁnal state is used to generate the output (Di Persio and Honchar 2017) Both
LSTM and GRU have their advantages due to their capability to eliminate the vanishing
gradient problem and blend deep ensemble algorithms (Li and Pan 2021).

2.4. Ensemble Learning Methods
2.4.1. Random Forest Algorithm

Random forest is a supervised learning method and employs a technique called
ensemble learning. It works well for both classiﬁcation and regression use cases. It is
derived from the concept of a decision tree as it creates several decision trees to provide
results (Kaczmarek and Perez 2021). The process of random forest is shown in Figure 4.
The generic steps of a random forest algorithm applied to stock market prediction (Yadav
and Vishwakarma 2019) are:

Figure 4. Random forest.

---

<!-- PAGE 10 -->

Int. J. Financial Stud. 2023, 11, 94

10 of 22

Step 1: N random records are picked.
Step 2: A decision tree is built based on N inputs.
Step 3: The number of trees to be considered is picked.
Step 4: Based on the steps performed before, the output is predicted for each tree.
Random forest can perform well on large datasets, but the possibility of the formation
of large number of trees can slow down the algorithm’s performance (Salles et al. 2018). The
random forest approach can also be used for various other use cases, such as predicting the
direction of stocks (Sadorsky 2021). This algorithm is used in the Zagreb Stock Exchange
(Manojlovi´c and Štajduhar 2015) and is compared with SVM, KNN, and logistic regression
based on the evaluation parameters accuracy, precession, recall, and F-Score (Pathak and
Pathak 2020).

2.4.2. XG-Boost Regression Algorithm

XG-Boost is an ensembled machine learning algorithm that is like random forest with
subtle differences. It is a combination of weak learners such as decision trees. It is a good
prediction model for stock forecasting as it works on a sequential model that considers the
gradient for each iteration so that the weights are updated for each iteration of the decision
tree (Zhu and He 2022). The process of XG-Boost is depicted in Figure 5.

Figure 5. XG-Boost algorithm.

2.4.3. E-SVR-RF (Ensemble Support Vector Machine–Random Forest)

Ensemble support vector regression with random forest is an ensemble technique that
follows the bagging method. An ensemble learning algorithm that consists of a support
vector regressor and random forest is used to handle the complex relationship for each
cluster and individual forecast. These are ﬁnally combined using the bagging method to
show the ﬁnal prediction using a weighted average model (Xu et al. 2020). The suggested
ensembling can leverage the advantages of both the support vector machine and random
forest, where the support vector machine can capture complex relationships by ﬁnding
the hyperplane that maximizes the margin between the forecasted and actual price, and
random forest decreases the overﬁtting problem by combining the decision trees.

XG-Boost + LSTM, blending ensemble (LSTM + GRU) (Li and Pan 2021), and ensemble
techniques for sentiment analysis (Gite et al. 2023) are proposed by the research community
for ﬁnancial instrument price forecasting. To summarize further, based on our review, it
can be understood that deep learning- and machine learning-based ensemble techniques
have gained popularity due to their performance.

3. General Machine Learning Pipeline

The general approach to training a machine learning model is given in Figure 6:

---

<!-- PAGE 11 -->

Int. J. Financial Stud. 2023, 11, 94

11 of 22

Figure 6. Workﬂow of basic ML model.

Training the ML model involves six steps, which are described in the following section:
Step 1: Load the data from a csv ﬁle or call the historical data with the help of an API.

(examples: Yahoo Finance, Quandl, IEXFinance, etc.).

Step 2: Preprocess the historical data to remove any redundancies, null values, etc.

and feature selection should be conducted.

Step 3: Before training the ML model, features such as open, close, adj close, volume,

etc., can be selected along with secondary data.

Step 4: Divide the preprocessed data into training and testing data, preferably, where
preferably 75% of the data should be used to train the model, while the remaining 25%
should be used to evaluate the model’s performance.

Step 5: After splitting the data, use the training data to train the model; then, per-
formance evaluation can be carried out based on the model’s output using the testing
data.

Step 6: Once the model is constructed, the model’s respective evaluation parameters
for regression or classiﬁcation can be used to evaluate the model. The evaluation parameters
are precision, recall, F1 Score, and accuracy. The mean absolute error, mean square error,
root mean squared error, R-squared, chi square, and mean absolute percent error (mean
absolute percentage error) can be used.

Step 7: Fine-tune the hyperparameters to improve the evaluation parameters of the
model. Following hyperparameter tuning, the model should be evaluated to check for
improved prediction parameters, after which the prediction can be plotted.

4. Signiﬁcance of Ensemble Modeling

This section of the article is about the comparative analysis of the most signiﬁcant
methods explored in Sections 2 and 3. Based on the study, it is observed that most common
algorithms, such as SVR, MLPR, KNN, random forest, XG-Boost, and LSTM, are used

---

<!-- PAGE 12 -->

Int. J. Financial Stud. 2023, 11, 94

12 of 22

by various researchers in their research work. In this review article, we attempted to use
these algorithms for forecasting the stock price of two stocks, namely, Tainwala Chemicals
and Plastics (Mumbai, India) Lt. (TAINIWALCHM) and Agro Phos (Indore, India) Ltd.
(AGROPHOS), and proposed an ensemble algorithm based on “Random Forest + XG-Boost
+ LSTM”. The idea behind including a comparison of the algorithms is to understand
the generic performance of the popular machine learning and deep learning algorithms
identiﬁed during the literature review.

After studying various algorithms, we developed an ensemble model of random
forest, XG-Boost, and LSTM. Random forest is simpler than the gradient boosting algorithm
but has the ability to handle high-dimensional datasets and capture non-linear patterns
common in stock market forecasting. Gradient boosting is a top choice algorithm for
classiﬁcation and regression predictive modeling projects because it often achieves the
best performance, but it takes lot of time to converge to the solution. The ensemble of
XG-Boost provides an efﬁcient implementation of gradient boosting that can be conﬁgured
to train random forest ensembles and address the speed problems of gradient boosting. In
order to achieve the best performance in stock price forecasting, the LSTM is combined in
this model due to its capability of storing past information. To make the most of the two
models, it is good practice to combine these two and apply a higher weight to the model,
which yields a lower loss function (mean absolute error). The parameter setting used for
implementing the proposed ensemble model is mentioned Table 1.

Table 1. Ensemble model parameter conﬁguration.

Parameter

Description

Model type

Libraries

Algorithms

Training/testing size

Loss function

Optimizer

Maximum epochs

Number of estimators

Maximum depth

Maximum features

Hyperparameter tuning method

Maximum depth

Learning rate

Number of estimators

Stacked ensemble model

Keras, TensorFlow, sklearn

Random Forest + XG-Boost + LSTM

80% for training and 20% for testing

MSE

Adam

50

Random Forest Conﬁguration

[50, 100, 200]

[3, 5, 7]

[‘sqrt’, ‘log2’]

Grid search

XG-Boost Conﬁguration

[3, 4, 5]

[0.1, 0.01, 0.001]

[50, 100, 150, 500, 1000]

Hyperparameter tuning method

Grid search

LSTM Conﬁguration

LSTM Layers

Dropout rate

Dense layer

Batch size

Hyperparameter tuning method

2

0.2

25 units

32

Grid search

The necessary comparison and evaluations are depicted in Figures 7 and 8. We
implemented all of these algorithms using Python programming language. Figure 7 shows
the stock forecasting results of Tainwala Chemicals and Plastics (India) (TAINIWALCHM).
The dataset for implementation was obtained from Yahoo Finance API, and we considered

---

<!-- PAGE 13 -->

Int. J. Financial Stud. 2023, 11, 94

13 of 22

the dataset for TAINIWALCHM from the year 2014 to the year 2023. The RMSE and R2
scores were used for evaluating the performance of the various models.

Figure 7. TANIWALCHM stock price forecasting: (a) SVR, (b) MLPR, (c) KNN, (d) random forest,
(e) XG-Boost, (f) LSTM, (g) Ensemble Random Forest + XG-Boost + LSTM.

---

<!-- PAGE 14 -->

Int. J. Financial Stud. 2023, 11, 94

14 of 22

Figure 8. AGROPHOS stock price forecasting: (a) SVR, (b) MLPR, (c) KNN, (d) random forest,
(e) XG-Boost, (f) LSTM, (g) Ensemble Random Forest + XG-Boost + LSTM.

---

<!-- PAGE 15 -->

Int. J. Financial Stud. 2023, 11, 94

15 of 22

Figure 8 shows the stock forecasting results of Agro Phos (India) Ltd. (AGROPHOS).
The dataset for implementation was obtained from Yahoo Finance API, and we have
considered the dataset for TAINIWALCHM from the year 2018 to the year 2023. The RMSE
and R2 scores were used for evaluating the performance of the various models.

The analysis results in Table 2 indicate that the ensemble algorithm demonstrated the

best performance compared to other distinct algorithms’.

Table 2. RMSE and R2 scores of algorithms.

TANIWALCHM

AGROPHOS

Algorithm

SVR

MLPR

KNN

LSTM

Random forest

XG-Boost

Random Forest +
XG-Boost + LSTM

RMSE

4.525

2.5893

4.4249

5.6241

87.8839

2.0686

2.0247

R2

0.9279

0.9611

0.9311

0.8867

0.9818

0.9842

0.9921

RMSE

1.5074

2.4764

4.7877

5.2494

98.5633

1.7618

1.2658

R2

0.9432

0.9472

0.7262

0.8809

0.9428

0.9379

0.9897

From this study and experimental analysis, we observed that the modiﬁcation of
hyperparameters is a crucial stage in the process of stock forecasting as it can maximize
the performance of machine learning models. Table 3 lists machine learning models that
are frequently used in stock price forecasting. Nevertheless, the efﬁcacy of these models
is highly dependent on the choice of hyperparameters, which are parameters that are not
learned from the data, but rather, deﬁned before the learning process.

Table 3. Summary of existing stock prediction and forecasting algorithms with performance analysis.

Sr No

Algorithm Name

Gap Analysis

Performance Evaluation

1

Linear regression

2

Support vector
machine

3

K-nearest neighbor

Linear regression assumes a linear
relationship between dependent and
independent variables and is not suitable
for most real-time applications, and is used
to perform observations on readily
accessible sample data (Gururaj et al. 2019).

SVM’s excellent memory efﬁciency and
effectiveness make it an ideal estimating
technique in high-dimensional space. The
shortcoming of SVM is that it might
experience overﬁtting, but it performs
exceptionally well on tiny datasets (Pathak
and Pathak 2020; Grigoryan 2017).

KNN is an algorithm that skips the
learning step, so it may not generalize
effectively. With a huge dataset, it takes
longer since it must sort all the distances
from the unknown item (Tanuwijaya and
Hansun 2019; Pathak and Pathak 2020).

This is a regression type of algorithm that
shows graphs in a linear way, where in
RMSE is 3.22, MAE is 2.53, MSE is 10.37,
and R-squared is 0.73 (Gururaj et al. 2019).

This is a classiﬁcation type of algorithm,
and when used for stock prediction, the
results are as follows: accuracy is 68.2,
recall is 65.2, precision is 64.2, and F1-Score
is 64.9% (0.65).
When used as a support vector regression
(SVR) algorithm, the evaluation parameters
are as follows: SMAPE = 5.59,
R-squared = 1.69, and RMSE = 43.36.

This is a classiﬁcation type of ML
algorithm in which the results of stock
prediction are as follows: accuracy is 65.2,
recall is 63.6, precision is 64.8, and F1 Score
is 64.1% (0.64).
For KNN regressor, the evaluation
parameters are as follows: SMAPE = 14.32,
R-squared = −2.42, and RMSE = 56.44
(Venkat 2022).

---

<!-- PAGE 16 -->

Int. J. Financial Stud. 2023, 11, 94

16 of 22

Table 3. Cont.

Sr No

Algorithm Name

Gap Analysis

Performance Evaluation

4

Gaussian naïve
Bayes

Models with an integrated GNB algorithm
will yield feature extraction and feature
scaling outcomes that are superior to those
already achieved using models that
incorporate either the GNB algorithm or
feature scaling (Setiani et al. 2020;
Ampomah et al. 2021).

Gaussian naïve Bayes used by authors in
their research. Kendall’s Test of
Concordance is used in this feature, which
is scaled and extracted. The results are as
follows: accuracy is 84, F1 Score is 62.44%
(0.62), speciﬁcity is 0.70, and AUC values is
0.90 (Bansal et al. 2022).

5

Logistic regression

6

7

ARIMA

FB Prophet

8

GRU

9

LSTM

Both binary and multiclass classiﬁcation
use this algorithm. The ﬁndings obtained
via logistic regression are the most accurate;
however, identifying the best-ﬁtting feature
is necessary (Pathak and Pathak 2020; Ali
et al. 2018).

ARIMA can be considered because it is a
unique model with signiﬁcant coefﬁcients
and passes all the diagnostic tests
(Mashadihasanli 2022).

Prophet can use regression models to
determine seasonality on a daily, monthly,
and annual basis, as well as effects related
to holidays (Suresh et al. 2022; Kaninde
et al. 2022).

GRU is a neural network approach that is
an improvement upon RNN but has fewer
parameters than LSTM, so it trains faster.
Also, the chances of overﬁtting are lower
compared to RNN, and it can handle
long-term dependency (Shahi et al. 2020).

In this algorithm, weights are adjusted for
each long short-term memory data point
via stochastic gradient descent.
LSTM can handle more very long-term
dependency compared to any other neural
network algorithm (Shahi et al. 2020;
Pramod and Pm 2021; Mukherjee et al.
2021).

In this algorithm, with the help of research
papers, various ﬁnancial factors are
considered through which factors are
grouped for prediction. The results of this
algorithm are as follows: accuracy is 78.6,
recall is 76.6, precision is 77.8, and F1 Score
is 77.1% (0.77) (Pathak and Pathak 2020; Ali
et al. 2018).

ARIMA is a time series forecasting
technique for predicting market or stock
prices. It is a combination or integration of
autoregressive moving averages; the
results are as follows: RMSE, 88.05; MAE,
65.88; and MAPE, 5.73, and if performed
with sentiment analysis, the RMSE score is
6.41 (Kedar 2021).

This algorithm was created by Facebook
for time series forecasting. One of its
advantages is that it does not consider
holidays or null values. The result of its
RMSE is achieved 93 (Suresh et al. 2022;
Kaninde et al. 2022).

GRU is a deep learning algorithm that has
fewer parameters and handles short-term
data properly. The evaluation parameters
of GRU are, without sentiment analysis,
MAE = 42.8, RMSE = 47.31, and R-squared
= 0.879, and with sentiment analysis based
on news evaluation parameters,
MAE = 24.472, RMSE = 29.153, and
R-squared = 0.967 (Shahi et al. 2020).

LSTM is a more developed type of RNN
and is a deep learning technique. This is
one of the most used ML algorithms for
stock forecasting, and when used along
with sentiment analysis, it shows better
results than without sentiment analysis.
The result without sentiment analysis are
MAE = 48.47, RMSE = 55.993, and
R-squared = 0.867, and with sentiment
analysis based on news evaluation
parameters, are MAE = 17.689,
RMSE = 23.070, and R-squared = 0.867
(Shahi et al. 2020).

---

<!-- PAGE 17 -->

Int. J. Financial Stud. 2023, 11, 94

17 of 22

Table 3. Cont.

Sr No

Algorithm Name

Gap Analysis

Performance Evaluation

10

Random forest

11

XG-Boost

12

E-SVR-RF

13

XG-Boost + LSTM

14

Blending ensemble
(LSTM + GRU)

The effectiveness of random forest on large
datasets is one of its advantages. It can be
applied to classiﬁcation and regression
issues. The model becomes more random
as a result, improving it. This model’s use
of a huge number of trees slows it down,
which is a drawback (Pathak and Pathak
2020; Polamuri et al. 2019).

XG-Boost is an ensembled learning
technique that uses decision trees but in a
sequential manner and uses gradient
boosting in an iterative manner to obtain
better results.
XG-Boost is sensitive to hyperparameters
and will not work as well on large datasets
as random forest (Zhu and He 2022).

Ensemble support vector regression and
random forest shows improved accuracy as
it leverages the advantages of both
algorithms, and its robustness is increased,
but due to the increased complexity of both
algorithms, overﬁtting is an issue
(Xu et al. 2020).

Ensembling XG-Boost and LSTM can
leverage the advantages of both algorithms.
XG-Boost can handle linear and non-linear
relationships and LSTM can handle
long-term dependence. Due to this
algorithm’s complexity, hyperparameter
tuning can be an issue (Vuong et al. 2022).

Blending ensemble (LSTM+GRU) is a
combination of two to of the most-used
improvements to RNN and solves the
vanishing gradient problem. Both of them
can handle long-term dependence well,
and combining them would improve
forecasting; also, overﬁtting can be reduced.
It may require high computational power
and time to train both LSTM and GRU (Li
and Pan 2021).

This is an ensemble type of algorithm that
is used for stock forecasting. The results for
random forest are as follows: accuracy is
80.7, recall is 78.3, precision is 75.2, and F1
Score is 76.7% (0.77) (Pathak and Pathak
2020; Polamuri et al. 2019).

XG-Boost has the following evaluation
parameter: MSE = 360.0 (Zhu and He 2022).

The E-SVR-RF ensembled algorithm shows
the following evaluation parameters:
MAPE = 1.335, MAE = 0.1537,
RMSE = 0.0188, and MAE = 0.0485
(Xu et al. 2020).

The ensemble algorithm of XG-Boost +
LSTM shows the following evaluation
parameter: MSE = 3.465 (Vuong et al. 2022).

The blending ensemble algorithm, which
consists of a modiﬁed version of RNN, i.e.,
LSTM and GRU, has the following
evaluation parameters:
MSE = 186.32, MPA = 99.65,
precision = 60%, Recall = 75%,
F1-Score = 66.67% (Li and Pan 2021).

The next part of this section illustrates the comparative analysis of work conducted by
multiple authors on various classiﬁcation, regression, and time series-based algorithms to
evaluate their performance in stock market forecasting, as shown in Table 3. The algorithms
were assessed using various evaluation parameters, including accuracy, recall, precision, F1
Score, MSE, MAE, RMSE, and R-squared error. The aim was to identify effective algorithms
that could beneﬁt a wider audience, including general applied researchers and intelligent
laypersons, enabling them to make informed investment decisions. These ﬁndings will also
provide valuable insights for researchers, investors, and general audiences, enabling them
to make well-informed decisions and navigate the complexities of the ﬁnancial market.

5. Implications and Limitations of the Study

This study focused on the application of machine learning and deep learning models
in stock forecasting. It can be noted that machine learning or deep learning models alone

---

<!-- PAGE 18 -->

Int. J. Financial Stud. 2023, 11, 94

18 of 22

are not sufﬁcient. Ensemble techniques are capable of providing superior performance.
But merely developing a model is not enough, and emphasis should also be placed on
hyperparameter tuning. The performance of the model can be improved using hyperpa-
rameters such as learning rates, regularization in cases of deep learning, the number of
hidden layers, max_depth, n_estimators, and learning rate. Choosing the proper settings
for these hyperparameters can considerably enhance the precision of stock forecasts. For
instance, a model with a greater learning rate may converge more quickly but may also
be susceptible to overﬁtting, whereas a model with a lower learning rate may converge
more slowly but generalize better to new data. Tuning hyperparameters entails choosing
the optimal combination of hyperparameters for a given dataset and model architecture.
This procedure often entails training many models with distinct hyperparameter values
and evaluating their performance on a validation dataset. Typically, the optimal combi-
nation of hyperparameters is determined by the model’s capacity to reduce the deviation
between predicted and actual stock prices. The study of machine learning models and deep
learning models and the comparative results presented in this article will guide researchers
in choosing ideal and preferred machine learning and deep learning algorithms for their
respective research work.

6. Future Research Directions

The presented review article is focused on the review of related and published articles
on stock price prediction, forecasting, and classiﬁcation. The analysis of ﬁnancial instru-
ments such as stocks and equities is a considerable challenge. It is said that the stock market
evolves over a period of time (Lim and Brooks 2011), and hence, the approaches developed
for handling speciﬁc problems will see low performance sooner or later even though their
performance is found to be appreciated initially. As the stock market evolves under the
inﬂuence of various factors such as geopolitical issues, equity trading, and investment,
the underlying challenges also change, and so do the methodologies for addressing the
new challenges (Sprenger and Welpe 2011; Shah et al. 2019). Sufﬁcient research has been
presented on stock price prediction and stock classiﬁcation, which is the primary focus of
this review article. Based on the study presented in this article, we have identiﬁed some of
the key areas where researchers should focus their attention and explore better solutions.
In this section, an attempt is made to open new research avenues for researchers in the ﬁeld
of stock market research.

6.1. Trend Analysis and Classiﬁcation

Most researchers are inclined towards solving the problem of price prediction or
forecasting stock value series. It is important to know the movement of stock prices, as well.
We believe that researchers can explore the possible usage of state-of-the-art deep learning
and machine learning algorithms in stock trend prediction and classiﬁcation (Jiang 2021;
Nikou et al. 2019).

6.2. Pattern Identiﬁcation Using Computer Vision

Most researchers see stock price as time series data, which is true. But time series
numerical data can be transformed into images, and patterns in the images can be identiﬁed
to understand new trends occurring in the price changes (Barra et al. 2020). Due to the
advancement of deep learning in the form of pre-trained models and transfer learning,
researchers can explore opportunities to apply these models to understanding the images
generated based on time series data.

6.3. Chart Pattern Analysis Using Computer Vision

Chart pattern analysis is one of the most-applied approaches among traders and
investors. Candlesticks often form fascinating patterns (Cagliero et al. 2023; Hu et al. 2019),
which helps traders in capturing price action well before it occurs. But the biggest drawback
of chart pattern analysis is the perception of the viewer. Generally, these chart patterns are

---

<!-- PAGE 19 -->

Int. J. Financial Stud. 2023, 11, 94

19 of 22

identiﬁed based on the perceptions of traders. Every trader will have a different perception
of the market, and the emotions of traders tend to project different patterns for the same
price action. For example, it is difﬁcult to differentiate between double-top and triple-top
candlestick patterns (Lambert 2009). Researchers can address the problem of candlestick
pattern identiﬁcation using suitable deep-learning techniques so that perception bias can
be avoided amongst traders.

7. Conclusions

In this review, several conventional, machine learning, and deep learning techniques
that are employed in stock market forecasting are investigated. This review describes
various machine learning techniques, deep learning techniques, and time series forecasting
techniques. This article presents recent applications of machine learning and deep learning
models, and an ensemble model is also tested on the TAINIWALCHM and AGROPHOS
stock datasets. Despite the existence of several popular methods for stock price forecasting,
even today, there is no universal solution to accurately predict the stock price or trend of the
market. There is still a possibility that AI-based models can also fail if they are not trained
efﬁciently with fresh data. To conclude this article, we assert that researchers should keep
exploring new avenues to solve price action problems using ensemble techniques. Stock
forecasting models should be enhanced with suitable hyperparameter tuning so that they
can serve as precise stock price prediction models. Traders and investment advisors can
use machine learning and deep learning models as additional conﬁrmation indicators to
support their decisions, and decisions should not rely only on AI-based price forecasting
methods. Along with stock forecasting techniques, researchers in the future can expand
their studies to portfolio management, trading strategy design, and investment decision
making.

Author Contributions: Conceptualization G.S., D.S.D. and A.M.B.; Visualization, G.S.; Writing—
original draft, G.S., D.S.D. and A.M.B.; Supervision, D.S.D. and A.M.B.; Writing—review & editing,
S.T.D., D.D., S.K.B. All authors have read and agreed to the published version of the manuscript.

Funding: This research received no external funding.

Informed Consent Statement: Not applicable.

Data Availability Statement: Not applicable.

Conﬂicts of Interest: The authors declare no conﬂict of interest.

References

Agrawal, Manish, Piyush Kumar Shukla, Rajit Nair, Anand Nayyar, and Mehedi Masud. 2022. Stock Prediction Based on Technical

Indicators Using Deep Learning Model. Computers, Materials & Continua 70: 287–304.

Ali, Syed Shahan, Muhammad Mubeen, and Adnan Hussain. 2018. Prediction of stock performance by using logistic regression model:

Evidence from Pakistan Stock Exchange (PSX). Asian Journal of Empirical Research 15: 212.

Ampomah, Ernest Kwame, Gabriel Nyame, Zhiguang Qin, Prince Clement Addo, Enoch Opanin Gyamﬁ, and Micheal Gyan. 2021.

Stock Market Prediction with Gaussian Naïve Bayes Machine Learning Algorithm. Informatica 45: 2. [CrossRef]

Baheti, Radhika, Gauri Shirkande, Sneha Bodake, Janhavi Deokar, and Archana K. 2021. Stock Market Analysis from Social Media and
News using Machine Learning Techniques. International Journal on Data Science and Machine Learning with Applications 1: 59–67.
Ballings, Michel, Dirk Van den Poel, Nathalie Hespeels, and Ruben Gryp. 2015. Evaluating multiple classiﬁers for stock price direction

prediction. Expert Systems with Applications 42: 7046–56. [CrossRef]

Banik, Shouvik, Nonita Sharma, Monika Mangla, Sachi Nandan Mohanty, and Selvarajan Shitharth. 2022. LSTM based decision

support system for swing trading in stock market. Knowledge-Based Systems 239: 107994. [CrossRef]

Bansal, Malti, Apoorva Goyal, and Apoorva Choudhary. 2022. Stock Market Prediction with High Accuracy using Machine Learning

Techniques. Procedia Computer Science 215: 247–65. [CrossRef]

Barra, Silvio, Salvatore Mario Carta, Andrea Corriga, Alessandro Sebastian Podda, and Diego Reforgiato Recupero. 2020. Deep
learning and time series-to-image encoding for ﬁnancial forecasting. IEEE/CAA Journal of Automatica Sinica 7: 683–92. [CrossRef]
Bustos, Oscar, Alexandra Pomares, and Enrique Gonzalez. 2017. A comparison between SVM and multilayer perceptron in predicting
an emerging ﬁnancial market: Colombian stock market. Paper presented at 2017 Congreso Internacional de Innovacion y
Tendencias en Ingenieria (CONIITI), Bogotá, Colombia, October 4–6; pp. 1–6.

---

<!-- PAGE 20 -->

Int. J. Financial Stud. 2023, 11, 94

20 of 22

Cagliero, Luca, Jacopo Fior, and Paolo Garza. 2023. Shortlisting machine learning-based stock trading recommendations using

candlestick pattern recognition. Expert Systems with Applications 216: 119493. [CrossRef]

Di Persio, Luca, and Oleksandr Honchar. 2017. Recurrent neural networks approach to the ﬁnancial forecast of Google assets.

International Journal of Mathematics and Computers in Simulation 11: 7–13.

Dospinescu, Nicoleta, and Octavian Dospinescu. 2019. A Proﬁtability Regression Model In Financial Communication Of Romanian

Stock Exchange’s Companies. Ecoforum Journal 8: 4.

Gite, Shilpa, Shruti Patil, Deepak Dharrao, Madhuri Yadav, Sneha Basak, Arundarasi Rajendran, and Ketan Kotecha. 2023. Textual
Feature Extraction Using Ant Colony Optimization for Hate Speech Classiﬁcation. Big Data and Cognitive Computing 7: 45.
[CrossRef]

Grigoryan, Hakob. 2017. Stock Market Trend Prediction Using Support Vector Machines and Variable Selection Methods. Advances in

Intelligent Systems Research (AISR) 2017: 210–13. [CrossRef]

Gururaj, Vaishnavi, V. R. Shriya, and K. Ashwini. 2019. Stock Market Prediction using Linear Regression and Support Vector Machines.

International Journal of Applied Engineering Research 14: 1931–34.

Hu, Weilong, Yain-Whar Si, Simon Fong, and Raymond Yiu Keung Lau. 2019. A formal approach to candlestick pattern classiﬁcation

in ﬁnancial time series. Applied Soft Computing 84: 105700. [CrossRef]

Hu, Zexin, Yiqi Zhao, and Matloob Khushi. 2021. A survey of forex and stock price prediction using deep learning. Applied System

Innovation 4: 9. [CrossRef]

Jiang, Weiwei. 2021. Applications of deep learning in stock market prediction: Recent progress. Expert Systems with Applications 184:

115537. [CrossRef]

Jose, Jithina, Suja Cherukullapurath Mana, and B. Keerthi Samhitha. 2019. An Efﬁcient System to Predict and Analyze Stock Data

using Hadoop Techniques. International Journal of Recent Technology and Engineering (IJRTE) 8: 1039–43. [CrossRef]

Kaczmarek, Tomasz, and Katarzyna Perez. 2021. Building portfolios based on machine learning predictions. Economic Research-

Ekonomska Istraživanja 35: 19–37. [CrossRef]

Kaninde, Sumedh, Manish Mahajan, Aditya Janghale, and Bharti Joshi. 2022. Stock Price Prediction Using Facebook Prophet.

International Journal of Research in Engineering and Science 44: 03060. [CrossRef]

Kardani, Navid, Annan Zhou, Majidreza Nazem, and Shui-Long Shen. 2020. Improved prediction of slope stability using a hybrid
stacking ensemble method based on ﬁnite element analysis and ﬁeld data. Journal of Rock Mechanics and Geotechnical Engineering
13: 188–201. [CrossRef]

Kedar, S. V. 2021. Stock Market Increase and Decrease using Twitter Sentiment Analysis and ARIMA Model. Turkish Journal of Computer

and Mathematics Education (TURCOMAT) 12: 146–61. [CrossRef]

Khairi, Teaba W. A., Rana M. Zaki, and Wisam A. Mahmood. 2019. Stock Price Prediction using Technical, Fundamental and News
based Approach. Paper presented at 2019 2nd Scientiﬁc Conference of Computer Sciences (SCCS), Baghdad, Iraq, March 27–28.
Khan, Wasiat, Mustansar Ali Ghazanfar, Muhammad Awais Azam, Amin Karami, Khaled H. Alyoubi, and Ahmed S. Alfakeeh. 2020.
Stock market prediction using machine learning classiﬁers and social media, news. Journal of Ambient Intelligence and Humanized
Computing 13: 3433–56. [CrossRef]

Kumar, Deepak, Pradeepta Kumar Sarangi, and Rajit Verma. 2021. A systematic review of stock market prediction using machine

learning and statistical techniques. Materials Today: Proceedings 49: 3187–91. [CrossRef]

Kumar, Saurav, and Dhruba Ningombam. 2018. Short-Term Forecasting of Stock Prices Using Long Short Term Memory. Paper

presented at 2018 International Conference on Information Technology (ICIT), Hong Kong, China, December 29–31.
Lambert, Clive. 2009. Candlestick Charts: An Introduction to Using Candlestick Charts. Petersﬁeld: Harriman House Limited.
Li, Audeliano Wolian, and Guilherme Sousa Bastos. 2020. Stock Market Forecasting Using Deep Learning and Technical Analysis: A

Systematic Review. IEEE Access 8: 185232–242. [CrossRef]

Li, Yang, and Yi Pan. 2021. A novel ensemble deep learning model for stock prediction based on stock prices and news. International

Journal of Data Science and Analytics 13: 139–49. [CrossRef] [PubMed]

Lim, Kian-Ping, and Robert Brooks. 2011. The evolution of stock market efﬁciency over time: A survey of the empirical literature.

Journal of Economic Surveys 25: 69–108. [CrossRef]

Lim, Yi Xuan, and Consilz Tan. 2021. Do negative events really have deteriorating effects on stock performance? A comparative study

on Tesla (US) and Nio (China). Journal of Asian Business and Economic Studies 29: 105–19. [CrossRef]

Manish, Kumar, and M. Thenmozhi. 2014. Forecasting stock index returns using ARIMA-SVM, ARIMA-ANN, and ARIMA-random

forest hybrid models. International Journal of Banking Accounting and Finance 5: 284–308.

Mann, Jordan, and J. Nathan Kutz. 2016. Dynamic mode decomposition for ﬁnancial trading strategies. Quantitative Finance 16:

1643–55. [CrossRef]

Manojlovi´c, Teo, and Ivan Štajduhar. 2015. Predicting stock market trends using random forests: A sample of the Zagreb stock exchange.
Paper presented at International Convention on Information and Communication Technology Electronics and Microelectronics,
Opatija, Croatia, May 25–29.

Mashadihasanli, Tamerlan. 2022. Stock Market Price Forecasting Using the Arima Model: An Application to Istanbul, Turkiye. Journal

of Economic Policy Researches 9: 439–54. [CrossRef]

---

<!-- PAGE 21 -->

Int. J. Financial Stud. 2023, 11, 94

21 of 22

Mohapatra, Sabyasachi, Rohan Mukherjee, Arindam Roy, Anirban Sengupta, and Amit Puniyani. 2022. Can Ensemble Machine
Learning Methods Predict Stock Returns for Indian Banks Using Technical Indicators? Journal of Risk and Financial Management 8:
350. [CrossRef]

Mukherjee, Somenath, Bikash Sadhukhan, Nairita Sarkar, Debajyoti Roy, and Soumil De. 2021. Stock market prediction using deep

learning algorithms. CAAI Transactions on Intelligence Technology 8: 82–94. [CrossRef]

Nabipour, Mojtaba, Pooyan Nayyeri, Hamed Jabani, S. Shahab, and Amir Mosavi. 2020. Predicting Stock Market Trends Using Machine
Learning and Deep Learning Algorithms Via Continuous and Binary Data; a Comparative Analysis. IEEE Access 8: 150199–212.
[CrossRef]

Nikou, Mahla, Gholamreza Mansourfar, and Jamshid Bagherzadeh. 2019. Stock price prediction using DEEP learning algorithm and its
comparison with machine learning algorithms. Intelligent Systems in Accounting, Finance and Management 26: 164–74. [CrossRef]
Nti, Isaac Koﬁ, Adebayo Felix Adekoya, and Benjamin Asubam Weyori. 2020. A comprehensive evaluation of ensemble learning for

stock-market prediction. Journal of Big Data 7: 1–40. [CrossRef]

Obthong, Mehtabhorn, Nongnuch Tantisantiwong, Watthanasak Jeamwatthanachai, and Gary Wills. 2020. A Survey on Machine
Learning for Stock Price Prediction: Algorithms and Techniques. Paper presented at 2nd International Conference on Finance,
Economics, Management and IT Business, Prague, Czech Republic, May 5–6.

Parray, Irfan Ramzan, Surinder Singh Khurana, Munish Kumar, and Ali A. Altalbe. 2020. Time series data analysis of stock price

movement using machine learning techniques. Soft Computing 24: 16509–17. [CrossRef]

Patel, Jigar, Sahil Shah, Priyank Thakkar, and Ketan Kotecha. 2015. Predicting stock and stock price index movement using Trend
Deterministic Data Preparation and machine learning techniques. Expert Systems with Applications 42: 259–68. [CrossRef]
Pathak, Ashwini, and Sakshi Pathak. 2020. Study of Machine learning Algorithms for Stock Market Prediction. International Journal of

Engineering Research & Technology (IJERT) 9: 6.

Polamuri, Subba Rao, Kudipudi Srinivas, and A. Krishna Mohan. 2019. Stock Market Prices Prediction using Random Forest and Extra

Tree Regression. International Journal of Recent Technology and Engineering 8: 1224–28. [CrossRef]

Pramod, B. S., and Mallikarjuna Shastry Pm. 2021. Stock Price Prediction Using LSTM. Test Engineering and Management 83: 5246–51.
Qiu, Jiayu, Bin Wang, and Changjun Zhou. 2020. Forecasting stock prices with long-short term memory neural network based on

attention mechanism. PLoS ONE 15: e0227222. [CrossRef] [PubMed]

Raghavendra, Kumar, Pardeep Kumar, and Yugal Kumar. 2021. Analysis of ﬁnancial time series forecasting using deep learning model.
Paper presented at 2021 11th International Conference on Cloud Computing, Data Science & Engineering (Conﬂuence), Uttar
Pradesh, India, January 28–29; pp. 877–81.

Reddy, Niveditha N., E. Naresh, and Vijaya Kumar B. P. 2020. Predicting Stock Price Using Sentimental Analysis Through Twitter
Data. Paper presented at 2020 IEEE International Conference on Electronics, Computing and Communication Technologies
(CONECCT), Bangalore, India, July 2–4.

Ren, Rui, Desheng Dash Wu, and Tianxiang Liu. 2019. Forecasting Stock Market Movement Direction Using Sentiment Analysis and

Support Vector Machine. IEEE Systems Journal 13: 760–70. [CrossRef]

Sadorsky, Perry. 2021. A Random Forests Approach to Predicting Clean Energy Stock Prices. Journal of Risk and Financial Management

14: 48. [CrossRef]

Salles, Thiago, Marcos Gonçalves, Victor Rodrigues, and Leonardo Rocha. 2018. Improving random forests by neighborhood projection

for effective text classiﬁcation. Information Systems 77: 1–21. [CrossRef]

Sathish Kumar, R., R. Girivarman, S. Parameshwaran, and V. Sriram. 2020. Stock Price Prediction Using Deep Learning and Sentimental

Analysis. JETIR 7: 346–54.

Seethalakshmi, Ramaswamy. 2018. Analayis of stock market predictor variables using linear regression. International Journal of Pure and

Applied Mathematics 119: 369–78.

Setiani, Ida, Meilany Nonsi Tentua, and Sunggito Oyama. 2020. Prediction of Banking Stock Prices Using Naïve Bayes Method. Journal

of Physics Conference Series 1823: 012059. [CrossRef]

Shah, Dev, Haruna Isah, and Farhana Zulkernine. 2019. Stock Market Analysis: A Review and Taxonomy of Prediction Techniques.

International Journal of Financial Studies 7: 26. [CrossRef]

Shahi, Tej Bahadur, Ashish Shrestha, Arjun Neupane, and William Guo. 2020. Stock Price Forecasting with Deep Learning: A

Comparative Study. Mathematics and Computer Science 8: 1441. [CrossRef]

Sharaf, Marwa, Ezz El-Din Hemdan, Ayman El-Sayed, and Nirmeen A. El-Bahnasawy. 2022. An efﬁcient hybrid stock trend prediction
system during COVID-19 pandemic based on stacked-LSTM and news sentiment analysis. Multimedia Tools and Applications 28:
1–33. [CrossRef]

Shen, Jingyi, and M. Omair Shaﬁq. 2020. Short-term stock market price trend prediction using a comprehensive deep learning system.

Journal of Big Data 7: 1–33. [CrossRef]

Sidra, Mehtab, and Jaydip Sen. 2020. A time series analysis-based stock price prediction using machine learning and deep learning

models. arXiv arXiv:2004.11697.

Smita, Mrinalini. 2021. Logistic Regression Model For Predicting Performance of S&P BSE30 Company Using IBM SPSS. International

Journal of Mathematics Trends and Technology 67: 118–34. [CrossRef]

Soni, Payal, Yogya Tewari, and Deepa Krishnan. 2022. Machine Learning approaches in stock price prediction: A systematic review.

Journal of Physics Conference Series 2161: 012065. [CrossRef]

---

<!-- PAGE 22 -->

Int. J. Financial Stud. 2023, 11, 94

22 of 22

Sprenger, Timm O., and Isabell M. Welpe. 2011. News or noise? The stock market reaction to different types of company-speciﬁc news

events. SSRN Electronic Journal. [CrossRef]

Suresh, N., B. Priya, and G. Lakshmi. 2022. Historical Analysis and Forecasting of Stock Market Using Fbprophet. South Asian Journal

of Engineering and Technology 12: 152–57. [CrossRef]

Tanuwijaya, Julius, and Seng Hansun. 2019. LQ45 Stock Index Prediction using k-Nearest Neighbors Regression. International Journal of

Recent Technology and Engineering 8: 2388–91. [CrossRef]

Umer, Muhammad, Muhammad Awais, and Muhammad Muzammul. 2019. Stock Market Prediction Using Machine Learning (ML)

Algorithms. ADCAIJ Advances in Distributed Computing and Artiﬁcial Intelligence Journal 8: 97–116. [CrossRef]

Venkat, Projects. 2022. Stock Market Trend Prediction Using K-Nearest Neighbor (KNN) Algorithm. Journal of Engineering Sciences

3: 32–44.

Vo, Nguyen, and Robert ´Slepaczuk. 2022. Applying Hybrid ARIMA-SGARCH in Algorithmic Investment Strategies on S&P500 Index.

Entropy 24: 158. [CrossRef] [PubMed]

Vuong, Pham Hoang, Trinh Tan Dat, Tieu Khoi Mai, and Pham Hoang Uyen. 2022. Stock-Price Forecasting Based on XGBoost and

LSTM. Computer Systems Science & Engineering 40: 237–46.

Xu, Ying, Cuijuan Yang, Shaoliang Peng, and Yusuke Nojima. 2020. A hybrid two-stage ﬁnancial stock forecasting algorithm based on

clustering and ensemble learning. Applied Intelligence 50: 3852–67. [CrossRef]

Yadav, Ashima, and Dinesh Kumar Vishwakarma. 2019. Sentiment analysis using deep learning architectures: A review. Artiﬁcial

Intelligence Review 53: 4335–85. [CrossRef]

Yang, Liu. 2019. Novel volatility forecasting using deep learning-long short term memory recurrent neural networks. Expert Systems

with Applications 132: 99–109.

Zhong, Xiao, and David Enke. 2019. Predicting the daily return direction of the stock market using hybrid machine learning algorithms.

Financial Innovation 5: 1–20. [CrossRef]

Zhou, Xingyu, Zhisong Pan, Guyu Hu, Siqi Tang, and Cheng Zhao. 2018. Stock Market Prediction on High-Frequency Data Using

Generative Adversarial Nets. Mathematical Problems in Engineering 2018: 4907423. [CrossRef]

Zhu, Yongqiong. 2020. Stock price prediction using the RNN model. Journal of Physics Conference Series 1650: 032103. [CrossRef]
Zhu, Zhe, and Kexin He. 2022. Prediction of Amazon’s Stock Price Based on ARIMA, XGBoost, and LSTM Models. Proceedings of

Business and Economic Studies 5: 127–36. [CrossRef]

Zizi, Youssef, Amine Jamali-Alaoui, Badreddine El Goumi, Mohamed Oudgou, and Abdeslam El Moudden. 2021. An Optimal Model
of Financial Distress Prediction: A Comparative Study between Neural Networks and Logistic Regression. Risks 9: 200. [CrossRef]

Disclaimer/Publisher’s Note: The statements, opinions and data contained in all publications are solely those of the individual
author(s) and contributor(s) and not of MDPI and/or the editor(s). MDPI and/or the editor(s) disclaim responsibility for any injury to
people or property resulting from any ideas, methods, instructions or products referred to in the content.

<!-- MARKITDOWN CONVERSION -->

<!-- Full MarkItDown conversion for formatting fidelity. -->

International Journal o f
Financial Studies
Review
Forecasting Stock Market Prices Using Machine Learning and
Deep Learning Models: A Systematic Review, Performance
Analysis and Discussion of Implications
GaurangSonkavde1,DeepakSudhakarDharrao2,* ,AnupkumarM.Bongale1,* ,SarikaT.Deokate3 ,
DeepakDoreswamy4 andSubrayaKrishnaBhat5
1 DepartmentofArtificialIntelligenceandMachineLearning,SymbiosisInstituteofTechnology,Symbiosis
InternationalDeemedUniversity,Pune412115,Maharashtra,India;gaurangsonkavade@gmail.com
2 DepartmentofComputerScience&Engineering,SymbiosisInstituteofTechnology,SymbiosisInternational
DeemedUniversity,Pune412115,Maharashtra,India
3 DepartmentofComputerEngineering,PimpriChinchwadCollegeofEngineering,
Pune411044,Maharashtra,India;sarika.deokate@pccoepune.org
4 DepartmentofMechatronics,ManipalInstituteofTechnology,ManipalAcademyofHigherEducation,
Manipal576104,Karnataka,India;deepak.d@manipal.edu
5 DepartmentofMechanicalandIndustrialEngineering,ManipalInstituteofTechnology,ManipalAcademyof
HigherEducation,Manipal576104,Karnataka,India;sk.bhat@manipal.edu
* Correspondence:deepak.dharrao@sitpune.edu.in(D.S.D.);anupkumar.bongale@sitpune.edu.in(A.M.B.)
Abstract:Thefinancialsectorhasgreatlyimpactedthemonetarywell-beingofconsumers,traders,
and financial institutions. In the current era, artificial intelligence is redefining the limits of the
financialmarketsbasedonstate-of-the-artmachinelearninganddeeplearningalgorithms.There
Citation:Sonkavde,Gaurang, isextensiveuseofthesetechniquesinfinancialinstrumentpriceprediction,markettrendanalysis,
DeepakSudhakarDharrao, establishinginvestmentopportunities,portfoliooptimization,etc.Investorsandtradersareusing
AnupkumarM.Bongale,SarikaT. machinelearninganddeeplearningmodelsforforecastingfinancialinstrumentmovements.With
Deokate,DeepakDoreswamy,and thewidespreadadoptionofAIinfinance,itisimperativetosummarizetherecentmachinelearning
SubrayaKrishnaBhat.2023. anddeeplearningmodels,whichmotivatedustopresentthiscomprehensivereviewofthepractical
ForecastingStockMarketPrices applicationsofmachinelearninginthefinancialindustry. Thisarticleexaminesalgorithmssuch
UsingMachineLearningandDeep
assupervisedandunsupervisedmachinelearningalgorithms, ensemblealgorithms, timeseries
LearningModels:ASystematic
analysisalgorithms,anddeeplearningalgorithmsforstockpricepredictionandsolvingclassification
Review,PerformanceAnalysisand
problems. Thecontributionsofthisreviewarticleareasfollows: (a)itprovidesadescriptionof
DiscussionofImplications.
machinelearninganddeeplearningmodelsusedinthefinancialsector;(b)itprovidesageneric
InternationalJournalofFinancial
frameworkforstockpricepredictionandclassification;and(c)itimplementsanensemblemodel—
Studies11: 94. https://doi.org/
“RandomForest+XG-Boost+LSTM”—forforecastingTAINIWALCHMandAGROPHOSstock
10.3390/ijfs11030094
pricesandperformsacomparativeanalysiswithpopularmachinelearninganddeeplearningmodels.
AcademicEditor:Muneer
M.Alshater
Keywords: stockmarket;finance;linearregression;randomforest;XG-Boost;FBProphet;LSTM;
Received:22April2023 ensemblelearning;blendingensemble
Revised:13July2023
Accepted:19July2023
Published:26July2023
1. Introduction
Theperformanceofacountry’sfinancialmarketisacrucialdeterminantofitsoverall
economic condition, enabling economists and financial experts to gauge the country’s
Copyright: © 2023 by the authors.
currenteconomichealth. Amongthevariousfinancialmarkets,thestockmarketstands
Licensee MDPI, Basel, Switzerland.
outasakeydrivingforce. Acountry’seconomicsituationdirectlyorindirectlyimpacts
This article is an open access article
sectorssuchasfinance,agriculture,metal,andinvestmentbanking,amongothers. The
distributed under the terms and
growthofthesesectorshingesontheirvolatility,whichfollowsthefundamentalprinciple
conditionsoftheCreativeCommons
Attribution(CCBY)license(https:// ofsupplyanddemand. Thedemandforaparticularsectordirectlyinfluencesthestock
creativecommons.org/licenses/by/ market,withincreasedsupplypromptingtradersandfinancialinstitutionstoinvestinthat
4.0/). sectororstock,drivingupprices. Additionally,regulardividendpaymentscontributeto
Int.J.FinancialStud.2023,11,94.https://doi.org/10.3390/ijfs11030094 https://www.mdpi.com/journal/ijfs

Int.J.FinancialStud.2023,11,94 2of22
thegenerationofprofitsandreturnsoninvestedcapital. Itisimperativeforinvestorsto
identifytheopportunemomenttosellsharesandachievetheirdesiredreturns. Financial
marketsencompassvarioustypesofmarket,includingstockmarkets,derivativesmarkets,
bondmarkets,andcommoditymarkets(Obthongetal.2020). Thestockmarketservesasa
platformforinvestorstoinvestinandownaportionorfractionofacompany.Ascompanies
grow,theyoftenrequireadditionalfundingtosupporttheirfutureendeavors. Following
the approval of current shareholders, who face diluted ownership due to the issuance
of new shares, companies can sell these shares to investors to raise capital. Successful
outcomesresultinincreasedstockmarketvaluefortheshares.
Shareslistedonthestockmarketcanbeboughtforbothshort-termandlong-term
investmentstrategies. Long-terminvestmentinvolvesholdingsharesoveranextended
period, while short-term investments involve buying and selling shares within shorter
timeframes,withinvestorsaimingforprofitswithindaysorweeks. Tradersemployawide
rangeoftradingstrategies,includingswingtrading,daytrading,positiontrading,and
scalping(MannandKutz2016).
Duetotheunpredictablenatureofthestockmarket,itishighlydifficultforindividu-
alstoobtainreturnsontheirinvestments. Primary,fundamental,andtechnicalanalysis
arepopularapproachestounderstandingmarkettrends(ManishandThenmozhi2014),
but they possess inherent limitations due to the involvement of lagging indicators and
predictioninaccuracy. Thishasmotivatedresearcherstodevelopimprovedtechniquesfor
real-timemarketscenariosbasedonmachinelearninganddeeplearningmodels.Inthecur-
rentera,machinelearninganddeeplearningalgorithmsoffersubstantialadvantagesover
traditionaltechniquessuchastechnicalandfundamentalanalysis. Leveragingthepower
ofmachinelearningandartificialintelligence,thesealgorithmsfacilitatetheforecasting
ofstockpricesandindices. Machinelearningservesasanadditionalapproachalongside
technicalandfundamentalanalysis,withthecombinationofthesetoolsformingapowerful
trading platform. Machine learning models can provide solutions to problems such as
stockpriceforecastingandclassification,portfoliomanagement,algorithmictrading,stock
market sentiment analysis, risk assessment, etc. Of these problems, this review article
is focused on exploring different approaches described for stock price forecasting and
classification.
The typical steps of a machine learning model pipeline for predicting stock price
involveseveralphases: collectinghistoricaldataviaanAPI,pre-processingthedata,creat-
ingaforecastingmodel,andevaluatingthemodel. Pre-processingentailsremovingzero
values,eliminatingduplicates,andscalingfeatures. Subsequently,importantfeaturesare
shortlisted,andvaliddataareselectedforstockpricepredictionorforecasting(Raghaven-
dra et al. 2021). In this article, numerous popular machine learning and deep learning
algorithms,suchaslinearregression,randomforest,logisticregression,k-nearestneighbor,
supportvectormachine,naïveBayes,ARIMA(autoregressiveintegratedmovingaverage),
FBProphet(FacebookProphet),LSTM(longshort-termmemory),GRU(gatedrecurrent
network),aswellasensemblealgorithmssuchasrandomforestandXG-Boost(extreme
gradientboosting),aredescribed(ZhongandEnke2019;SidraandSen2020;Parrayetal.
2020). Forevaluatingaclassificationmodel’saccuracy,recall,precision,andF-score,are
commonlypreferredmetrics,andforregressionorpriceforecastingmodels,rootmean
squareerror(RMSE)andmeanabsolutepercentageerror(MAPE)areoftenemployed(Jose
etal.2019).
Thereareasignificantnumberofreviewarticlesonstockpricepredictionandfore-
casting(Polamurietal.2019;Kumaretal.2021;Sonietal.2022). Butduetotheboomin
artificialintelligenceandmachinelearning,thefrequencyofpublicationshasincreased
considerably. Hence,thisreviewarticlepresentsrecentstate-of-the-artmachinelearning
and deep learning techniques for stock price prediction. The salient contributions and
uniquenessofthisreviewarticlearelistedbelow:
• Oneoftheuniquecontributionsofthisreviewarticleisthatitisnotjustlimitedto
summarizing the research articles. Extra effort is put into implementing the well-

Int.J.FinancialStud.2023,11,94 3of22
knownmachinelearninganddeeplearningmodelstounderstandtheirnatureand
performance. Alongwithourreview,acomparativeanalysisofvariousalgorithmsis
presentedinthisarticle. Themachinelearninganddeeplearningensemblealgorithms
are tested on TAINIWALCHM and AGROPHOS stock data, which fall under the
umbrellaofthechemicalindustrymarketsector.
• Inthisreviewarticle,detailedfutureresearchdirectionsareincluded. Futureresearch
avenues for researchers are identified based on the conducted study stock trend
analysisandclassification,patternidentification,andcandlestickchartpatternanalysis
usingcomputervision.
Therestofthearticleisorganizedasfollows. Section2describesthecompletetheo-
reticalbackgroundofmachinelearninganddeeplearningmodels. Agenericstructureof
themachinelearningmodelingpipelineispresentedinSection3. Theimportanceofthe
ensemblemodel“RandomForest+XG-Boost+LSTM”forforecastingTAINIWALCHM
andAGROPHOSstockpricesandacomparativeanalysiswithpopularmachinelearning
anddeeplearningmodelsarementionedinSection4. Section5discussestheimplications
and limitations of the current review. Future research directions are given in Section 6.
Finally,thepaperisconcludedinSection7.
2. ComprehensiveSummaryofTheoreticalBasis
Forecasting stock prices and predicting market trends are challenging tasks. Over
theyears,researchershaveproposedseveralsolutionstothesechallenges(Obthongetal.
2020;Huetal.2021;Polamurietal.2019),andthesemethodsarebrieflyexplainedbelow.
Machine learning, deep learning, time series forecasting, and ensemble algorithms are
some of the most popular approaches to solving the mentioned problems. Ensemble
algorithmscanimproveaccuracyandreduceRMSE.Hadooparchitecturescanalsohandle
large volumes of stock data (Jose et al. 2019) and deep learning algorithms can predict
financialmarkets(Huetal.2021). StockforecastingusingLSTM,auniquerecurrentneural
network(RNN),overcomeslong-termdependency(Qiuetal.2020;Baniketal.2022). But
thevanishinggradientandexplodinggradientproblemsoftenneedtobeaddressedin
RNN-basedarchitectures(LiandPan2021;Zhu2020). Khanetal.,in(Khanetal.2020),
usedPyspark,MLlib,linearregression,andrandomforesttoachieve80–98%accuracy.
Multiplealgorithmshavebeenusedtoforecaststockprices,includingneuralnetworks,
which train data on layers of connected neurons, and support vector machines, which
predict stock price movement using hyperplanes. Random forest, trained on multiple
decisiontreesandNaïveBayes,predictsstockmovementbasedonnegativeorpositive
probabilityusingRelianceandInfosys’10-yearhistoricaldata(Pateletal.2015). Random
forestiscomparedtootheralgorithmson5767Europeancompanies. Thesealgorithms
includeneuralnetworks,whicharemultiplelayersofneuronsconnectedwitheachother;
logisticregression,whichoutputsabinaryvaluetopredictwhetherthestockwillmoveup
ordownbasedonprobability;supportvectormachines;andK-Nearestneighbor,which
findstheknearestdatapointsusingEuclideansimilaritymetrics. Randomforestisthebest
algorithm,followedbySVM(Ballingsetal.2015).
Stockmarketforecastingisaregressionusecasebecausestockpricesarecontinuous
(Seethalakshmi2018).(DiPersioandHonchar2017),usedRNNforforecastingGooglestock
prices. RNN,LSTM,andGRUarethethreemostefficientneuralnetworksforsequential
data. RNNisusedforhistoricaldata. LSTMandGRUcanavoidthevanishinggradient
problembasedonforget,reset,andupdategates. GRUisfoundtobefasterasitoperates
onresetandupdategates(DiPersioandHonchar2017).
AnotherstudyinvolvestheuseofARIMA,LSTM,andrandomforestforpricefore-
casting,andXG-Boost,anensemblelearningalgorithmlikerandomforest. Basedonthe
evaluationparameters,XG-BoostoutperformedARIMAandLSTM(ZhuandHe2022).
Isaacetal.alsousedensemblemachinelearningtoimprovestockmarketforecastingresults.
Cooperativeandcompetitiveclassifieralgorithmsusestackingandblending. Baggingand
boostingtechniquesareusedtoreducevarianceandbias. Mostensembleclassifiersand

Int.J.FinancialStud.2023,11,94 4of22
regressorsaredevelopedbycombiningdecisiontrees,supportvectormachines,andneural
networks(Ntietal.2020). Similarly,(Xuetal.2020)alsousedbaggingensemblelearning
techniquestopredictChinesestocks.Thisapproachcombinesatwo-stagepredictionmodel
called“EnsembleLearningSVRandRandomForest(E-SVR&RF)”withKNNtoclusterit
withtentechnicalindicators. AnotherproposedmethodusesEnsembleLSTMwithCNN
onstockindexesfortrainingadversarialnetworks,whichcanhelpforecasthigh-frequency
stockandhasadvantageslikeadversarialtrainingandreducingdirectionpredictionloss
andforecasterrorloss(Zhouetal.2018). Toenhancetheeffectivenessofensemblemodel
ofXG-BoostandLSTM,XG-Boostisusedtoselectfeaturesappliedtohigh-dimensional
timeseriesdataandLSTMisusedforstockpriceforecasting(Vuongetal.2022).
Notonlyhavemachinelearningensemblemethodshelpedtoimproveforecasting
performance,butinsomeresearchwork,ithasalsobeenobservedthatneuralnetwork
blendingensemblemodelsalsoperformwell. (Yang2019)implementedamodelconsisting
oftwolayersofRNN.ThefirstonewasanLSTM-basedblendingensemblealgorithm,and
thesecondonewasGRU-based. ThemodelshowedthelowestRMSEvalueof186.32,a
precisionof60%,andanF1-scoreof66.47(LiandPan2021).
Sometimes,pricemovementisprimarilyaffectedbysentiments. Thesesentimentscan
bepositive,leadingtoabullishmovement,ornegative,leadingtoabearishmovement.
Hence, stocksentimentanalysisisimportanttounderstandstockpriceforecastingand
trendclassification. Further,inthissection,weexploresomeforecastingtechniquesbased
onsentimentanalysis. Socialmediadata,companynews,andtrendanalysiscanclassify
investors’stocksentimentsaspositive,negative,orneutral(YadavandVishwakarma2019).
Sincestockpricesrespondtonewsandglobalevents,pricevariationalonecannotbe
usedtotrainMLmodels. ANN-andLSTM-baseddeeplearningtechniquescanalsobe
trainedusingpricevaluesandtextdata. Word2vecandNGramareusedtoconverttext
datatonumericaldataandtrainthemodeltogetherwithprice-sentimentdata. Diversified
datacanpredominantlyincreaseaccuracyandlowerinaccurateresults. Analgorithmlike
arandomforestapproachisalsoagoodchoiceforTwittersentimentanalysis(Kumarand
Ningombam2018;Reddyetal.2020).
Financialnewsanduser-generatedtext,suchascommentsonsocialmediaplatforms,
cantriggernewtrendsinthestockmarket. Forexample,“Mondayhasthelowestaverage
return”showsastatementrepresentingaweakornegativesentiment.
Whilecreatingthedatasetfortrainingthemodel,arollingwindowapproachonhistorical
dataworkswellwithnews-basedtextdata.Renetal.showedanincreaseinaccuracyofupto
18.6%to89.93%pointswhenmultimodaldatawereconsidered(Renetal.2019).
Whentextdataarecollected,theycanincludecorrectandfakedata. Inonestudy,the
authorsusedfeatureselectiontoeliminatefakenewsandspamtweetscollectedfromsocial
mediadata. Thisimprovedthedataqualityfortraining,andaclassificationalgorithm,the
randomforestalgorithm,wasusedtotrainthemodel. Sentimentscanbepositive,neutral,
ornegative, whichhelpspeopledecidewhethertobuyorsellstock(Bahetietal.2021).
Negativesentimentsaffectmarketconditions. Limetal. consideredausecaseinwhich
acomparisonoftwostocks,TeslaandNio,basedonsentiments,wascarriedout. Itwas
foundthatnegativeevents,suchasTesla’s2021protest,affecteditscompetitor,Nio,aswell.
Thisresearchwasbasedonhistoricaldatausingtimeseriesforecastingwith10,15,and20
daysofdata(LimandTan2021).
In(Sharafetal.2022),newsheadlinespertainingtoTSLA,AMZ,andGOOGstockwere
consideredtoobtaingood-qualitydatatoreducespamtweetsthroughfeatureselectionmethods.
Sentimentanalysiswasalsousedforpolaritydetectionandhistoricaldatamining,forwhich
DLalgorithmswereused.Similarfeatureengineering-anddeeplearning-basedapproachesare
presentedin(ShenandShafiq2020;Nabipouretal.2020;Mohapatraetal.2022).
(Khairietal.2019)showedthattechnicalanalysiswithsentimentanalysiscanalso
provideprominentinvestmentopportunities.Technicalindicatorslikestochasticoscillators,
movingaverageconvergencedivergence(MACD),Bollingerbands,andrelativestrength
indicators(RSI)aregoodforshort-termanalysisbutnotlong-term. Incasesofnegative

Int. J. Financial Stud. 2023, 11, x FOR PEER REVIEW 5 of 23
mining, for which DL algorithms were used. Similar feature engineering- and deep learn-
ing-based approaches are presented in (Shen and Shafiq 2020; Nabipour et al. 2020; Mo-
hapatra et al. 2022).
(Khairi et al. 2019) showed that technical analysis with sentiment analysis can also
Int.J.FinancialStud.2023,11,94 provide prominent investment opportunities. Technical indicators like stochastic os5ciolfla22-
tors, moving average convergence divergence (MACD), Bollinger bands, and relative
strength indicators (RSI) are good for short-term analysis but not long-term. In cases of
nneegwast,ivgee nneerwasll,y g,emnaerrkaleltyt, rmenadrksewt itlrlebnedsb ewairlils bhe, abnedartihshe, satnodck thper iscteowcki lplrfiaclel. wTiolla fdadll.r eTsos
athdidsriesssus eth,iins iitsiasulsee, nintiimtiaeln steanntaimlyesnist caannablyespise crfaonr mbee dpetorfofirnmdetdh eton efignadti vtheen newegsautisvien gnePwoSs
(upsainrtg oPfosSp (epeacrht) otfa gspseienchth) etangesw ins sthtaet enmewens ts.taPtreomgreanmt. mPrionggralimbrmariinegs lliibkreaSrieenst liiWkeo rSdeNntei-t
WcanorbdeNuets ecdanf obreP uosSedta fgogri nPgo.S Ttahgisgianpgp. rTohaicsh ahpapsroreascuhl theads irneshuilgtehdp irno fihtiagbhi lpitryofiantadbilloitwy
alonsds -lmowak lionsgs-smitaukaitniogn ssit(uKahtiaoinris e(Ktahla.i2r0i 1e9t )a.l.I n20a1n9o).t hIne ranapotphreora acphpprrooapcohs pedrobpyosLeide btya lL.i( Leti
aaln. d(LBi aasntods B2a0s2t0o)s, a20t2ec0h),n ai ctaelcahnnaiclyasl iasnoaflyhsisisto orfi chailsdtoartiacaaln ddaataf uanndda am feunntdalaamneanlytasli saunsailnygsias
udseienpgl ae adreneinpg leaaprpnrinogac ahpwpreoraeccho wndeurec tceodntdougcetende rtaot egebneettrearter ebteuttrners .reHtuerren,sL. HSTeMre,i sLSchToMse ins
cfohropserned fiocrt ipornedasicittiocann asst iotr ceamn estmoroer ymaenmdodroye asnndo dtoheasv enoatv haanviesh ai nvgangirsahdiniegn gtrisasduieen(Lt iisasnude
(BLais atonsd2 B0a2s0t)o.sS i2m02il0a)r. Swimoriklairs wproerske nist epdreinse(nAtegdra iwn a(Alegtraalw.2a0l 2e2t ;aSla. t2h0i2s2h; KSautmhiasrh eKtualm.2a0r2 e0t;
aUl.m 2e0r20et; Ualm.2e0r1 e9t) .al. 2019).
BBaasseedd oonn tthhee ssttuuddiieess pprreesseenntteedd ssoo ffaarr,, tthhee bbeesstt ssttoocckk mmaarrkkeett ffoorreeccaassttiinngg ssoolluuttiioonn iiss
ddeerriivveedd ffrroommf ufunnddaammenentatlaal naanlaylsyissiasn adntde cthenchicnailcaanl aalynsailsywsisit hwsiethn tsimenetnimtaennatl yasnisalaynsdisd aenedp
dleeaerpn ilnegarmniondge mls.oEdnelsse.m Enbsleemtebchlen tieqcuhensipqruoevsi pdreoevsipdeec eiaslplyecpiarollmy pisrionmgfiosirnegca fsotriencgaostuintcgo omuets-.
cTohmeeaslg. oTrhiteh amlgsotrhitahtmarse tuhsaet darfeo russteodc kfomr satrokcekt mpraerdkiectt ipornedbiyctcioonns bidye croinngsirdeesreianrgc hrepseaaprecrhs
aregiveninFigure1.
papers are given in Figure 1.
Figure 1. Stock forecasting algorithm.
Figure1.Stockforecastingalgorithm.
22..11.. BBaassiicc MMaacchhiinnee LLeeaarrnniinngg AAllggoorriitthhmm
22..11..11.. LLiinneeaarr RReeggrreessssiioonn
Linearregressionisusedforstockorfinancialmarketpredictiontoforecastthefuture
Linear regression is used for stock or financial market prediction to forecast the future
priceofstockregressionandusesamodelbasedononeormoreattributes,suchasclosed
price of stock regression and uses a model based on one or more attributes, such as closed
price,openprice,volume,etc.,toforecastthestockprice. Regressionmodelingaimsto
price, open price, volume, etc., to forecast the stock price. Regression modeling aims to
simulatethelinearrelationshipbetweenthedependentandindependentvariables. The
simulate the linear relationship between the dependent and independent variables. The
linearregressionmodelproducesabest-fitlinethatdescribestheconnectionbetweenthe
linear regression model produces a best-fit line that describes the connection between the inde-
independentfactorsandthedependentvariable.
pendent factors and the dependent variable.
Inthistechnique,astraightlinerepresentedbyEquation(1)isdrawn,ensuringthat
In this technique, a straight line represented by Equation (1) is drawn, ensuring that
thelinecrossesthehighestpossiblenumberofthedataset’sdatapoints. Whencharting
the line crosses the highest possible number of the dataset’s data points. When charting the
thedataset’svaluesonagraph,astraightlineismathematicallyfittedbetweenthepoints
sothatthesquareofthedistanceordifferencebetweeneachpointandthelineisassmall
aspossible. Foreachgivenx,thehypothesislineisusedtoforecastthevalueofy. This
forecastingmethodisknownaslinearregression. Fortheevaluationoftheresultsand
to check how well the model fits the line, parameters such as RMSE, MAE, MSE, and
R-squaredareused(Gururajetal.2019;DospinescuandDospinescu2019).
O = S +K (1)
x

Int.J.FinancialStud.2023,11,94 6of22
whereOistheoutput,S representstheslope,andKisaconstant.
x
2.1.2. K-NearestNeighbor(KNN)
KNNisaclassificationandregressiontechniqueandhasbeentermedasalazylearner
becauseitdoesnotneedahugetimeperiodforlearning. OneofKNN’sadvantagesisthat
itisoneoftheeasiestMLalgorithms. TheonlyactionthatneedstobetakenforKNNisto
calculatethevalueofKandtheEuclideandistance. Thisalgorithm’sslowlearningaspect
makesitquickerthanotheralgorithms. Itmaynotgeneralizewellforbigdatasinceit
skipsthelearningstep(TanuwijayaandHansun2019). Theeuclideandistancecalculation
isgiveninEquation(2),
(cid:113)
D(h i ,p r ) = ∑ . n l . =1 (P r −h i )2 (2)
whereP representsthepredictedvalueandh representsthedatavalue.
r i
2.1.3. SupportVectorMachine(SVM)
StockmarketpredictionusinganSVMcanbethemostusefultechniqueforpredicting
stockprice,asitcanbeusedasaclassificationandregressionalgorithm. Thecomparisonof
SVManditsvariants,suchas“Peeling+SVM”and“CC+SVM”,showsthatitsprediction
canbeimprovedbyadvancedSVMmethods(Grigoryan2017). Asupportvectormachine
involvessupervisedlearningusedtocategorizeaspectsusingaseparator. Theseparatoris
thendiscoveredwhenthedataareinitiallymappedtoahigh-dimensionalfeaturespace. It
findsthecategorizationofdatapointsoccurringinann-dimensionalspaceandfindsthe
optimalhyperplane. Thedatapointsaregroupedaccordingtotheirlocationinrelation
to the hyperplanes. The performance of the SVM algorithm can be elevated by tuning
parameters such as regularization, gamma, and kernel parameters (Bustos et al. 2017).
SVMcanalsobeusedforsentimentanalysistoassessinvestors’sentiments,whichwould
indirectlyaffectmarketconditions. Itiswellsuitedtobothhigh-dimensionaldatasetsand
small-scaledatasets.
2.1.4. NaïveBayesAlgorithm
NaïveBayesisasupervisedmachinelearningtechniquethatcanbeusedtoforecast
pricesofvariousstocksinresearchonbankingstock.
NaïveBayesisaclassificationalgorithminwhichacombinationofprobabilitysum-
mingupthefrequenciesandvaluecombinationsistakenfromadataset. Dependingonthe
valuesoftheclassvariables,theBayestheoremmakesanassumptionregardingwhether
the attributes of naïve Bayes are independent or interdependent. The basic concept of
naïveBayesisthatattributevaluesareindependentinthepresenceofanoutputvalue
(Setianietal.2020). ThesetupGNBmodelsweregradedbasedontheirperformanceusing
Kendall’stestofconcordanceforseveralassessmentparameters. Theoutcomesshowed
thattheGNBLDApredictivemodel(Kardanietal.2020)performedbetterthanallother
GNBmodels.TheposteriorprobabilitywascalculatedasshowninEquation(3)(Ampomah
etal.2021).
P(U|H)·P(H)
P(H|U) = (3)
P(U)
whereUisunknownclassdata, Histhehypothesisfordataofcertainclass,P(H)isthe
hypothesisprobability, P(U|H) istheprobabilityofUbeingdependentonthecondition
inhypothesisH,andP(U)istheprobabilityofU.
TheformulafornaïveBayesusedinstockpredictionisgivenbyEquation(4):
1 −
(ai−µi
. j
)2
P(A = a |B = b) = √ e 2€4ij (4)
i 1 i 2π€
whereπrepresentspi(3.14),eistheexponential(2.7183),µrepresentsthemean,and€is
thestandarddeviation.

Int.J.FinancialStud.2023,11,94 7of22
2.1.5. LogisticRegression
Logisticregressionisasupervisedmethodofmachinelearning. Byutilizingvariables
forlogisticcurves,logisticregressiongroupsseveralindependentfactorsintotwoormore
mutuallyexclusivegroupsandforecaststhelikelihoodofequitiesthatperformwell(Ali
etal.2018).Toclassifystockperformanceusinglogisticregression,themaximumlikelihood
iscalculatedasperEquation(5):
Z = β +β EPS +β PB +β ROE +β CR +β DE +β sales +V (5)
it 1 2 it 2 it 2 it 2 it 2 it 2 it it
(cid:16) (cid:17)
wherez = loglog Pr andPr=probabilityofoutcomeispositive.
1−Pr
Therearevariants,suchasbinarylogisticregression,thatcanimprovefinanceratios
andinvestors’abilitytoanticipatestockprice(Smita2021).
2.2. ForecastingofStockMarketUsingTimeSeriesForecasting
Stockpricedataaretimeseriesdata. Someoftheclassicalmethods,suchasautore-
gressivemovingaverage(ARIMA)andFBProphet,arediscussedinthissubsection. These
methodswereverywelladoptedbeforethesuccessofdeeplearningmodels.
2.2.1. ARIMA
ARIMAisanalgorithmthatusestimeseriesforecastingtopredictthefuturevalueof
stocks. InastudypresentedbyTamerlanetal.,in(Mashadihasanli2022),itisdemonstrated
that the ARIMA model best fits the stock market index. The ARIMA model comprises
three steps—identify, estimate, and diagnose. These steps can be used for forecasting
anyfinancemarketsuchasequity, derivative, etc. (Mashadihasanli2022). ARIMAcan
becombinedwithanotheralgorithm,symmetricgeneralizedautoregressiveconditional
heteroskedasticity(SGARCH),toimproveforecastingperformance. Thiscombinationhas
beenmodeledandtestedontheS&P500Index(VoandS´lepaczuk2022). ARIMAhaseven
beenextendedforstocksentimentanalysis(Kedar2021).
TheformulaofARIMA,whichcombinesAR(autoregression)andMA(movingaver-
age),isshowninEquation(6),
y (cid:48)(t) = k+β p ∗ωDy (cid:48) t−1 +···+ β p ∗ωDy (cid:48) t−p +θ 1 ∗ε t−1 +···+θq∗ε (ti−q) +ε ti (6)
where prepresentstheautoregressivemodel’sgivendegree,Disthedegreeofdifferent
orders,andqisthemovingaverage’sgivendegree.
2.2.2. FBProphetModel
FBProphetisatimeseriesforecastinglibrarydevelopedbyFacebook. FBProphet
bettersuitsdatathathaveanullvalueanditrelativelyshowsmoreaccurateresultsinsuch
situations. TheformulaofFBProphetispresentedinEquation(7):
Yt = l(t)+sp(t)+v(t)+εt, yt = g(t)+s(t)+h(t)+εn (7)
wherel(t)representsthelineartrend,sp(t)representsseasonalpatterns,v(t)represents
holidayeffects,andεnisthewhitenoiseerror.ThealgorithmdesignedbasedonFBProphet
isimplementedusingthePyStanlibrary(Sureshetal.2022). Researchershaveextensively
usedFBProphetinstockpriceforecasting(Kanindeetal.2022;Shahietal.2020).
2.3. DeepLearningMethods
Deeplearningmodelshavewide-rangingpopularityinmanyareasofscienceand
engineering. They are especially widely adopted in stock price forecasting and trend
predictionduetotheirabilitytocapturecomplexpatterns,handlelargevolumesofdata,
and undertake feature learning and representation, and their adaptability to changing
market conditions. In this subsection, some of the popular deep learning models are
discussedinrelationtothefinancedomain.

Int. J. Financial Stud. 2023, 11, x FOR PEER REVIEW 8 of 23
𝑌𝑡 = 𝑙(𝑡)+𝑠𝑝(𝑡)+𝑣(𝑡)+𝜀𝑡,𝑦 𝑡 = 𝑔( 𝑡 ) + 𝑠( 𝑡 ) + ℎ( 𝑡 ) + 𝜀𝑛 (7)
where 𝑙(𝑡) represents the linear trend, 𝑠𝑝(𝑡) represents seasonal patterns, 𝑣(𝑡) repre-
sents holiday effects, and 𝜀𝑛 is the white noise error. The algorithm designed based on
FB Prophet is implemented using the PyStan library (Suresh et al. 2022). Researchers have
extensively used FB Prophet in stock price forecasting (Kaninde et al. 2022; Shahi et al.
2020).
2.3. Deep Learning Methods
Deep learning models have wide-ranging popularity in many areas of science and
engineering. They are especially widely adopted in stock price forecasting and trend pre-
diction due to their ability to capture complex patterns, handle large volumes of data, and
undertake feature learning and representation, and their adaptability to changing market
conditions. In this subsection, some of the popular deep learning models are discussed in
relation to the finance domain.
2.3.1. Long Short-Term Memory (LSTM)
LSTM is an advanced model of Recurrent Neural Networks (RNNs), a deep learning
algorithm. An LSTM model can handle lengthy sequences of data units as it can remember
the data sequence, which can be used for future inputs. Figure 2 shows a general LSTM
cell structure. It comprises three gates—the input gate, the forget gate, and the
output gate. All of the gates employ the sigmoid activation function. All of the
gates used in the LSTM are mathematically represented as per Equations (8)–(10).
Input gate (New information in cell state):
Int.J.FinancialStud.2023,11,94 8of22
𝑖𝑔𝑎 = 𝜎 (𝑊 (cid:4670)ℎ ,𝑋𝑐(cid:4671) + 𝑏𝑖) (8)
(cid:3036)(cid:3043) (cid:3047)(cid:2879)(cid:2869)
Forget gate (useless information is eliminated):
2.3.1. LongShort-TermMemory(LSTM)
𝑓 = 𝜎 (𝑊 (cid:4670)ℎ ,𝑋𝑐(cid:4671) + 𝑏𝑓) (9)
(cid:3034)(cid:3028) (cid:3033)(cid:3034) (cid:3047)(cid:2879)(cid:2869)
LSTMisanadvancedmodelofRecurrentNeuralNetworks(RNNs),adeeplearning
algoOrituhtmpu.tA gnatLeS (TaMctimvaotdioenl ctoan lahsat nbdloleckle onfg fithnyals eoquutpenuct)e:s ofdataunitsasitcanremember
thedatasequence,whichcan b𝑂eus=ed 𝜎f (o𝑊rfu t(cid:4670)uℎrei,n𝑋p𝑐u(cid:4671)t s+. F𝑏i𝑜g)u re2showsageneralLS
(1
T
0
M
)
(cid:3043)(cid:3034) (cid:3042)(cid:3043) (cid:3047)(cid:2879)(cid:2869)
cellstructure. Itcomprisesthreegates—theinputgate,theforgetgate,andtheoutputgate.
wAhlleoref t𝜎h eisg astiegsmeomidp,l 𝑊oy𝑥t hise tshieg mneouidroanc tgiavtaet i(o𝑥n) wfuenicgthiot,n .ℎA(cid:3047)(cid:2879)l(cid:2869)l oisf tthhee greastuesltu osfe tdhein ptrheeceLdSiTnMg
LaSrTeMm abtlhoecmk,a t𝑋ic𝑡a ilsly threep irnepsuent,t aednda s𝑏p𝑥e risE bqiuasa.t ions(8)–(10).
FFiigguurree 22. .LLSSTTMM sstrtruuccttuurree. .
AInsp suhtogwante i(nN Feiwguirnef o2r,m thaeti otonpi npcaerltl osfta tthee): memory line in every cell can be used to
connect with the transport line with the help of the model, which can be used to handle
(cid:0) (cid:1)
the data from the prior memor i y g a to = th σ e c W uripre [ n h tt− m1 , em Xc o ] r + y. b E i ach LSTM node should have ( 8 a )
set of cells that is used for storage of the data stream (Pramod and Pm 2021). In order to
Forgetgate(uselessinformationiseliminated):
provide a recursive network with plenty of time to train and allow for the creation of a
long-distance causal link, LSTM main(cid:16)tains errors at a more(cid:17) constant level (Mukherjee et
f ga = σ W fg [h t−1 , Xc]+bf (9)
Outputgate(activationtolastblockoffinaloutput):
(cid:0) (cid:1)
O pg = σ W op [h t−1 , Xc]+bo (10)
whereσissigmoid,Wxistheneurongate(x)weight,h t−1 istheresultofthepreceding
LSTMblock,Xtistheinput,andbxisbias.
AsshowninFigure2, thetoppartofthememorylineineverycellcanbeusedto
connectwiththetransportlinewiththehelpofthemodel,whichcanbeusedtohandle
thedatafromthepriormemorytothecurrentmemory. EachLSTMnodeshouldhavea
setofcellsthatisusedforstorageofthedatastream(PramodandPm2021). Inorderto
providearecursivenetworkwithplentyoftimetotrainandallowforthecreationofa
long-distancecausallink,LSTMmaintainserrorsatamoreconstantlevel(Mukherjeeetal.
2021). Inseveralcases,neuralnetworksanddeepneuralnetworkshaveshownsuperior
forecastingperformancecomparedtoothermachinelearningmodels. However,whenit
comestopredictingfinancialdistress,thelogisticregressionmodelhasexhibitedbetter
resultsincomparisontoneuralnetworks(Zizietal.2021).
2.3.2. GatedRecurrentNeuralNetwork(GRU)
AGRUisyetanotherRNN-basedmodelwithcomparabledifferencestoLSTM.It
is computationally efficient and faster to train than LSTM, while capturing long-term
dependenciesinsequentialdata. GRUutilizesgatingmechanismstocontroltheflowof
informationbetweenthecurrentandprevioustimesteps. However,itutilizesonlytwo
gates,aresetgateandanupdategate,whereasLSTMhasthreegates. Figure3showsthe
generalstructureofaGRU.

Int. J. Financial Stud. 2023, 11, x FOR PEER REVIEW 9 of 23
al. 2021). In several cases, neural networks and deep neural networks have shown supe-
rior forecasting performance compared to other machine learning models. However,
when it comes to predicting financial distress, the logistic regression model has exhibited
better results in comparison to neural networks (Zizi et al. 2021).
2.3.2. Gated Recurrent Neural Network (GRU)
A GRU is yet another RNN-based model with comparable differences to LSTM. It is
computationally efficient and faster to train than LSTM, while capturing long-term de-
pendencies in sequential data. GRU utilizes gating mechanisms to control the flow of in-
formation between the current and previous time steps. However, it utilizes only two
Int.J.FinancialStud.2023,11,94 gates, a reset gate and an update gate, whereas LSTM has three gates. Figure 3 show9so tfh22e
general structure of a GRU.
FFiigguurree 33.. GGRRUU ssttrruuccttuurree..
TThhee ttwwoo ggaatteess tthhaatt GGRRUU uusseess aarree::
((11)) UUppddaattee ggaattee
𝑍 Z (cid:4670) [ 𝑡 t (cid:4671) ] = = 𝜎 σ ( ( 𝑊 W( ( (cid:3053) z ) ) 𝑥 x t+ + U 𝑈 ( ((cid:3053) z) )ℎ h t−1 ) ( ( 1 1 1 1 ) )
(cid:3047) (cid:3047)(cid:2879)(cid:2869)
(2) Resetgate
(2) Reset gate
r[t] = σ(W (r) x t +U (r) h t−1 ) (12)
where Z[t] is update gate, 𝑟 r[ (cid:4670) t 𝑡 ] (cid:4671) i = s r 𝜎 es ( e 𝑊 t g ((cid:3045) a ) t 𝑥 e(cid:3047), + σ r 𝑈 e ( p (cid:3045) r ) e ℎ s(cid:3047)(cid:2879)e(cid:2869)n ts sigmoid function, W(x()1 i 2 s )
wherne e𝑍u(cid:4670)r𝑡o(cid:4671)n igs autpe,dUat ( e x ) giastep,r 𝑟e(cid:4670)v𝑡i(cid:4671)o uiss rweseeitg ghat,teh,t σ− 1reisptrheseernetssu slitgomfothide pfurneccetidoinn,g 𝑊G(R(cid:3051))U isb lnoecuk-,
ron gaanted, x𝑈t(i(cid:3051)s) thise pcruervrieonutsi nwpeuitg.ht, ht−1 is the result of the preceding GRU block, and 𝑥
(cid:3047)
is
the cFuorrresntto cinkppurti.c edata,GRUreceivestheinputasasequenceofhistoricalstockprices
andgFeonre srtaotceks tphreicoeu dtpatuat, aGsRaUs erqecueeinvcees othfep irnepduictt eads as tsoecqkuperniccee so.fT hhisetoinrpicuatl ssetoqcuke npcrieceiss
faenddt hgreonuegrahteths ethGeR oUutnpeutwt aosr ka, sweqhuicehncuep odfa tperseidtsicitnetde rsntoaclks tpatreicaets.e aTchhe tiinmpeust tseepq,uaenndcteh ies
nfeedtw thorroku’sgfih nthale sGtaRteUi nseutsweodrkto, wgehnicehra utepdthaeteos uittsp iuntte(DrniaPl estrastioe aatn edacHho tnimchea srte2p01, 7a)ndB oththe
LnSeTtwMorakn’ds fiGnRaUl shtaatvee itsh ueisredad tvoa gnetangeerastde uteheto otuhtepiurtc a(Dpai bPielirtsyioto aenldim Hinoantcehtahre 2v0a1n7i)s hBiontgh
gLrSaTdMie natnpdr oGbRleUm haanvde bthleenird addeveapnetangseesm dbulee atlog othreitihr mcasp(aLbiialintyd tPoa enli2m02in1a).te the vanishing
gradient problem and blend deep ensemble algorithms (Li and Pan 2021).
2.4. EnsembleLearningMethods
22..44..1 E.nRsaenmdbolem LeFaorrneisntgA Mlgeothroitdhsm
Int. J. Financial Stud. 2023, 11, x FOR PEER RREaVnIdEoWm forest is a supervised learning method and employs a technique1c0a lolfe d23
2.4.1. Random Forest Algorithm
ensemble learning. It works well for both classification and regression use cases. It is
Random forest is a supervised learning method and employs a technique called en-
derivedfromtheconceptofadecisiontreeasitcreatesseveraldecisiontreestoprovide
semble learning. It works well for both classification and regression use cases. It is derived
resultSste(Kp a2c:z Am daereckisiaonnd trPeeer eisz b2u0i2lt1 b).aTsehde opnr o𝑁ce sinspouftrsa. ndomforestisshowninFigure4.
from the concept of a decision tree as it creates several decision trees to provide results
ThegSetneepr i3c: sTtehpes noufmabrearn dofo mtrefeosr teos tbael gcoornisthidmeraepdp ilsi epdictkoesdt.o ckmarketprediction(Yadav
(Kaczmarek and Perez 2021). The process of random forest is shown in Figure 4. The ge-
andVSitsehpw 4a:k Baarsmead 2o0n1 9th)ea rsete:ps performed before, the output is predicted for each tree.
neric steps of a random forest algorithm applied to stock market prediction (Yadav and
Vishwakarma 2019) are:
Step 1: 𝑁 random records are picked.
FFiigguurree4 4.. RRaannddoomm ffoorreesstt..
Random forest can perform well on large datasets, but the possibility of the formation
of large number of trees can slow down the algorithm’s performance (Salles et al. 2018).
The random forest approach can also be used for various other use cases, such as predict-
ing the direction of stocks (Sadorsky 2021). This algorithm is used in the Zagreb Stock
Exchange (Manojlović and Štajduhar 2015) and is compared with SVM, KNN, and logistic
regression based on the evaluation parameters accuracy, precession, recall, and F-Score
(Pathak and Pathak 2020).
2.4.2. XG-Boost Regression Algorithm
XG-Boost is an ensembled machine learning algorithm that is like random forest with
subtle differences. It is a combination of weak learners such as decision trees. It is a good
prediction model for stock forecasting as it works on a sequential model that considers
the gradient for each iteration so that the weights are updated for each iteration of the
decision tree (Zhu and He 2022). The process of XG-Boost is depicted in Figure 5.
Figure 5. XG-Boost algorithm.
2.4.3. E-SVR-RF (Ensemble Support Vector Machine–Random Forest)
Ensemble support vector regression with random forest is an ensemble technique
that follows the bagging method. An ensemble learning algorithm that consists of a sup-
port vector regressor and random forest is used to handle the complex relationship for

Int. J. Financial Stud. 2023, 11, x FOR PEER REVIEW 10 of 23
Step 2: A decision tree is built based on 𝑁 inputs.
Step 3: The number of trees to be considered is picked.
Step 4: Based on the steps performed before, the output is predicted for each tree.
Int.J.FinancialStud.2023,11,94 10of22
Step1: Nrandomrecordsarepicked.
Step2: AdecisiontreeisbuiltbasedonNinputs.
FigurSet e4.p R3a:nTdhomen fourmesbt.e roftreestobeconsideredispicked.
Step4: Basedonthestepsperformedbefore,theoutputispredictedforeachtree.
RRaannddoomm ffoorreesstt ccaann ppeerrffoorrmm wweellll oonn llaarrggee ddaattaasseettss,, bbuutt tthhee ppoossssiibbiilliittyy ooff tthhee ffoorrmmaattiioonn
ooff llaarrggeen nuummbbeerro offtr tereesecsa cnasnl oswlowdo dwonwtnh ethaleg aolrgitohrmith’smp’esr fpoerrmfoarnmcean(Scael l(eSsaellteasl .e2t 0a1l8. )2.0T1h8e).
rTahned roamndfoormes ftoarpepstr oaapcphrocaancha lcsaonb aelsuos ebde fuosrevda froior uvsaroitohuesr outsheecra usesse, csauscehs,a ssupcrhe dasic ptirnegdtihcte-
dinirge ctthieo ndoirfescttoiocnk so(fS satdoocrkssk y(S2a0d2o1r)s.kTyh 2is02a1lg).o Trihthism aligsoursiethdmin itsh uesZedag irne bthSet oZcakgErxebch Satnogcek
(EMxachnaonjlogve i(c´MaanndoŠjltoavjdiću hanard2 Š0t1a5jd)uahndari 2s0c1o5m) panarde dis wcoimthpSaVreMd, wKiNthN S,VanMd, lKoNgiNsti, carnedg rloesgsiisotinc
breagseredsosinonth beaesveadl uoant itohne peavraalmuaettieorns apcacruarmaecyte,rpsr eaccecsusriaocny,, rpecraeclle,sasniodnF, -rSeccoarlel, (aPnadth Fa-kScaonrde
P(Paaththaakk2 a0n20d) .Pathak 2020).
22..44..22.. XXGG--BBoooosstt RReeggrreessssiioonn AAllggoorriitthhmm
XXGG--BBoooosstt iiss aann eennsseemmbblleedd mmaacchhiinnee lleeaarrnniinngg aallggoorriitthhmm tthhaatt iiss lliikkee rraannddoomm ffoorreesstt wwiitthh
ssuubbttllee ddiiffffeerreenncceess.. IItt iiss aa ccoommbbiinnaattiioonn ooff wweeaakk lleeaarrnneerrss ssuucchh aass ddeecciissiioonn ttrreeeess.. IItt iiss aa ggoooodd
pprreeddiiccttiioonn mmooddeellf oforrs tsotcokckf ofroerceacsatsintigngas aist wit owrkosrkosn oans eaq sueeqnuteianltmialo dmeoldtheal tthcoant sciodnesrisdtehres
gthraed giernadtfieonrte afochr eitaecrhat iiotenrastoiothna stot htehawt etihgeh twsaerigehutps daartee dupfodraeteadch foitre reaatciohn iotefrtahteiodne coifs itohne
tdreeeci(sZiohnu tarened (HZheu2 0a2n2d) .HTeh 2e0p2r2o)c. eTshseo pfrXoGce-Bsso oosf tXisGd-Beopoicstte ids idneFpiigctuerde i5n. Figure 5.
FFiigguurree 55.. XXGG--BBoooosstt aallggoorriitthhmm..
22..44..33.. EE--SSVVRR--RRFF ((EEnnsseemmbbllee SSuuppppoorrtt VVeeccttoorr MMaacchhiinnee––RRaannddoomm FFoorreesstt))
EEnnsseemmbbllee ssuuppppoorrttv vecetcotrorr ergergersessiosinonw iwthitrha nrdanomdofmor efostreissta nis eanns eemnbselemtbecleh nteiqcuhenitqhuaet
ftohlalot wfoslltohwesb tahgeg binagggminegth modet.hAond.e Annse emnbselemlbealer nleinargnainlggo arligthomritthhmat tchoant sciosntssiosftsa osfu ap psuoprt-
vpeocrtto vrercetgorre sresogrreasnsodrr aanndd ormandfoormes tfoisreusst eids utosehda ntod lheatnhdelec otmhep cleoxmrpelleaxti ornelsahtiiopnfsohripea fcohr
clusterandindividualforecast. Thesearefinallycombinedusingthebaggingmethodto
showthefinalpredictionusingaweightedaveragemodel(Xuetal.2020). Thesuggested
ensemblingcanleveragetheadvantagesofboththesupportvectormachineandrandom
forest,wherethesupportvectormachinecancapturecomplexrelationshipsbyfinding
thehyperplanethatmaximizesthemarginbetweentheforecastedandactualprice,and
randomforestdecreasestheoverfittingproblembycombiningthedecisiontrees.
XG-Boost+LSTM,blendingensemble(LSTM+GRU)(LiandPan2021),andensemble
techniquesforsentimentanalysis(Giteetal.2023)areproposedbytheresearchcommunity
forfinancialinstrumentpriceforecasting. Tosummarizefurther,basedonourreview,it
canbeunderstoodthatdeeplearning-andmachinelearning-basedensembletechniques
havegainedpopularityduetotheirperformance.
3. GeneralMachineLearningPipeline
ThegeneralapproachtotrainingamachinelearningmodelisgiveninFigure6:

Int. J. Financial Stud. 2023, 11, x FOR PEER REVIEW 11 of 23
each cluster and individual forecast. These are finally combined using the bagging method
to show the final prediction using a weighted average model (Xu et al. 2020). The sug-
gested ensembling can leverage the advantages of both the support vector machine and
random forest, where the support vector machine can capture complex relationships by
finding the hyperplane that maximizes the margin between the forecasted and actual
price, and random forest decreases the overfitting problem by combining the decision
trees.
XG-Boost + LSTM, blending ensemble (LSTM + GRU) (Li and Pan 2021), and ensem-
ble techniques for sentiment analysis (Gite et al. 2023) are proposed by the research com-
munity for financial instrument price forecasting. To summarize further, based on our
review, it can be understood that deep learning- and machine learning-based ensemble
techniques have gained popularity due to their performance.
Int.J.FinancialStud.2023,11,94 3. General Machine Learning Pipeline 11of22
The general approach to training a machine learning model is given in Figure 6:
Figure 6. Workflow of basic ML model.
Figure6.WorkflowofbasicMLmodel.
TTrraaiinniinngg tthhee MMLLm mooddeelli ninvvoolvlvesess isxixs tsetpesp,sw, whihchichar aerdee dscersicbreidbeidn tinhe thfoel lfoowlloinwginsegc tsieocn-:
tion: S tep1: LoadthedatafromacsvfileorcallthehistoricaldatawiththehelpofanAPI.
(examStpelpe s1:: YLaohaodo tFhien daantcae ,frQouma na dcls,vI EfiXleF oinr acnaclle t,heetc h.)i.storical data with the help of an API.
(examSptelpes2: :YPahreopor Foicneasnscteh,e Qhuisatnodrilc, aIElXdFatinaatnocree, metocv.)e. anyredundancies,nullvalues,etc.
andfSetaetpu r2e: sPerleepctrioocnesssh othueld hbisetocroincadlu dctaetda .to remove any redundancies, null values, etc.
and fSetaetpur3e: sBeelefocrtieotnr asihnoinugldt hbee McoLndmuocdteedl,. fe aturessuchasopen,close,adjclose,volume,
etc.,cSatenpb 3e: sBeelefoctreed traalionninggw tihteh MseLco mndoadreyl, dfeaatatu.res such as open, close, adj close, volume,
etc., cSatnep be4 :sDelievcitdeed tahleonpgre wpriothc essesceodnddaatray idnatotat.r a iningandtestingdata,preferably,where
preferably75%ofthedatashouldbeusedtotrainthemodel, whiletheremaining25%
shouldbeusedtoevaluatethemodel’sperformance.
Step 5: After splitting the data, use the training data to train the model; then, per-
formance evaluation can be carried out based on the model’s output using the testing
data.
Step6: Oncethemodelisconstructed,themodel’srespectiveevaluationparameters
forregressionorclassificationcanbeusedtoevaluatethemodel.Theevaluationparameters
areprecision,recall,F1Score,andaccuracy. Themeanabsoluteerror,meansquareerror,
rootmeansquarederror,R-squared,chisquare,andmeanabsolutepercenterror(mean
absolutepercentageerror)canbeused.
Step7: Fine-tunethehyperparameterstoimprovetheevaluationparametersofthe
model. Following hyperparameter tuning, the model should be evaluated to check for
improvedpredictionparameters,afterwhichthepredictioncanbeplotted.
4. SignificanceofEnsembleModeling
Thissectionofthearticleisaboutthecomparativeanalysisofthemostsignificant
methodsexploredinSections2and3. Basedonthestudy,itisobservedthatmostcommon
algorithms, such as SVR, MLPR, KNN, random forest, XG-Boost, and LSTM, are used

Int.J.FinancialStud.2023,11,94 12of22
byvariousresearchersintheirresearchwork. Inthisreviewarticle,weattemptedtouse
thesealgorithmsforforecastingthestockpriceoftwostocks,namely,TainwalaChemicals
andPlastics(Mumbai,India)Lt. (TAINIWALCHM)andAgroPhos(Indore,India)Ltd.
(AGROPHOS),andproposedanensemblealgorithmbasedon“RandomForest+XG-Boost
+ LSTM”. The idea behind including a comparison of the algorithms is to understand
thegenericperformanceofthepopularmachinelearninganddeeplearningalgorithms
identifiedduringtheliteraturereview.
After studying various algorithms, we developed an ensemble model of random
forest,XG-Boost,andLSTM.Randomforestissimplerthanthegradientboostingalgorithm
buthastheabilitytohandlehigh-dimensionaldatasetsandcapturenon-linearpatterns
common in stock market forecasting. Gradient boosting is a top choice algorithm for
classification and regression predictive modeling projects because it often achieves the
best performance, but it takes lot of time to converge to the solution. The ensemble of
XG-Boostprovidesanefficientimplementationofgradientboostingthatcanbeconfigured
totrainrandomforestensemblesandaddressthespeedproblemsofgradientboosting. In
ordertoachievethebestperformanceinstockpriceforecasting,theLSTMiscombinedin
thismodelduetoitscapabilityofstoringpastinformation. Tomakethemostofthetwo
models,itisgoodpracticetocombinethesetwoandapplyahigherweighttothemodel,
whichyieldsalowerlossfunction(meanabsoluteerror). Theparametersettingusedfor
implementingtheproposedensemblemodelismentionedTable1.
Table1.Ensemblemodelparameterconfiguration.
Parameter Description
Modeltype Stackedensemblemodel
Libraries Keras,TensorFlow,sklearn
Algorithms RandomForest+XG-Boost+LSTM
Training/testingsize 80%fortrainingand20%fortesting
Lossfunction MSE
Optimizer Adam
Maximumepochs 50
RandomForestConfiguration
Numberofestimators [50,100,200]
Maximumdepth [3,5,7]
Maximumfeatures [‘sqrt’,‘log2’]
Hyperparametertuningmethod Gridsearch
XG-BoostConfiguration
Maximumdepth [3,4,5]
Learningrate [0.1,0.01,0.001]
Numberofestimators [50,100,150,500,1000]
Hyperparametertuningmethod Gridsearch
LSTMConfiguration
LSTMLayers 2
Dropoutrate 0.2
Denselayer 25units
Batchsize 32
Hyperparametertuningmethod Gridsearch
The necessary comparison and evaluations are depicted in Figures 7 and 8. We
implementedallofthesealgorithmsusingPythonprogramminglanguage. Figure7shows
thestockforecastingresultsofTainwalaChemicalsandPlastics(India)(TAINIWALCHM).
ThedatasetforimplementationwasobtainedfromYahooFinanceAPI,andweconsidered

Int. J. Financial Stud. 2023, 11, x FOR PEER REVIEW  13 of 23

| Hyperparameter tuning method  |     | Grid search  |     |     |
| ----------------------------- | --- | ------------ | --- | --- |
XG-Boost Configuration
| Maximum depth                 |     | [3, 4, 5]                  |     |     |
| ----------------------------- | --- | -------------------------- | --- | --- |
| Learning rate                 |     | [0.1, 0.01, 0.001]         |     |     |
| Number of estimators          |     | [50, 100, 150, 500, 1000]  |     |     |
| Hyperparameter tuning method  |     | Grid search                |     |     |
LSTM Configuration
| LSTM Layers                   |     | 2            |     |     |
| ----------------------------- | --- | ------------ | --- | --- |
| Dropout rate                  |     | 0.2          |     |     |
| Dense layer                   |     | 25 units     |     |     |
| Batch size                    |     | 32           |     |     |
| Hyperparameter tuning method  |     | Grid search  |     |     |
Int.J.FinancialStud.2023,11,94 13of22
The necessary comparison and evaluations are depicted in Figures 7 and 8. We im-
plemented all of these algorithms using Python programming language. Figure 7 shows
| the  stock  forecasting  | results  of  Tainwala  | Chemicals  | and  Plastics  (India)  | (TAINI- |
| ------------------------ | ---------------------- | ---------- | ----------------------- | ------- |
WALCHM). The dataset for implementation was obtained from Yahoo Finance API, and
thedatwase ectonfosirdeTrAedI NtheI WdaAtaLseCt fHorM TAfIrNoImWAtLhCeHyMea frro2m0 1th4e tyoeatrh 2e01y4e tao rth2e0 y2e3a.r T20h23e. RThMe SEandR2
scoreswRMerSeE uansde dR2f oscroerevsa wlueraet uinsegd tfhore epvaelrufaotrinmg athnec peeorffortmheanvcea roifo thues vmaroiodues lms.odels.
|      |     |      |     |     |
| ---- | --- | ---- | --- | --- |
| (a)  |     | (b)  |     |     |

Int. J. Financial Stud. 2023, 11, x FOR PEER REVIEW  14 of 23

| (c)  |     | (d)  |     |     |
| ---- | --- | ---- | --- | --- |

|      |     |      |     |     |
| ---- | --- | ---- | --- | --- |
| (e)  |     | (f)  |     |     |

(g)
Figure 7. TANIWALCHM stock price forecasting: (a) SVR, (b) MLPR, (c) KNN, (d) random forest,
Figure7.TANIWALCHMstockpriceforecasting:(a)SVR,(b)MLPR,(c)KNN,(d)randomforest,
(e) XG-Boost, (f) LSTM, (g) Ensemble Random Forest + XG-Boost + LSTM.
(e)XG-Boost,(f)LSTM,(g)EnsembleRandomForest+XG-Boost+LSTM.
Figure 8 shows the stock forecasting results of Agro Phos (India) Ltd. (AGROPHOS).
The dataset for implementation was obtained from Yahoo Finance API, and we have con-
sidered the dataset for TAINIWALCHM from the year 2018 to the year 2023. The RMSE
and R2 scores were used for evaluating the performance of the various models.

| (a)  |     | (b)  |     |     |
| ---- | --- | ---- | --- | --- |

Int. J. Financial Stud. 2023, 11, x FOR PEER REVIEW 14 of 23
(e) (f)
(g)
Figure 7. TANIWALCHM stock price forecasting: (a) SVR, (b) MLPR, (c) KNN, (d) random forest,
(e) XG-Boost, (f) LSTM, (g) Ensemble Random Forest + XG-Boost + LSTM.
Figure 8 shows the stock forecasting results of Agro Phos (India) Ltd. (AGROPHOS).
The dataset for implementation was obtained from Yahoo Finance API, and we have con-
Int.J.FinancialStud.2023,11,94 14of22
sidered the dataset for TAINIWALCHM from the year 2018 to the year 2023. The RMSE
and R2 scores were used for evaluating the performance of the various models.
Int. J. Financial Stud. 2023, 11, x FOR PEER REVIEW 15 of 23
(a) (b)
(c) (d)
(e) (f)
(g)
Figure 8. AGROPHOS stock price forecasting: (a) SVR, (b) MLPR, (c) KNN, (d) random forest, (e)
Figure 8. AGROPHOS stock price forecasting: (a) SVR, (b) MLPR, (c) KNN, (d) random forest,
XG-Boost, (f) LSTM, (g) Ensemble Random Forest + XG-Boost + LSTM.
(e)XG-Boost,(f)LSTM,(g)EnsembleRandomForest+XG-Boost+LSTM.
The analysis results in Table 2 indicate that the ensemble algorithm demonstrated the
best performance compared to other distinct algorithmsʹ.

| Int.J.FinancialStud.2023,11,94 |     |     |     |     |     | 15of22 |
| ------------------------------ | --- | --- | --- | --- | --- | ------ |
Figure8showsthestockforecastingresultsofAgroPhos(India)Ltd. (AGROPHOS).
The dataset for implementation was obtained from Yahoo Finance API, and we have
consideredthedatasetforTAINIWALCHMfromtheyear2018totheyear2023. TheRMSE
andR2scoreswereusedforevaluatingtheperformanceofthevariousmodels.
TheanalysisresultsinTable2indicatethattheensemblealgorithmdemonstratedthe
bestperformancecomparedtootherdistinctalgorithms’.
Table2.RMSEandR2scoresofalgorithms.
TANIWALCHM AGROPHOS
|     |     | Algorithm    | RMSE    | R2     | RMSE    | R2     |
| --- | --- | ------------ | ------- | ------ | ------- | ------ |
|     |     | SVR          | 4.525   | 0.9279 | 1.5074  | 0.9432 |
|     |     | MLPR         | 2.5893  | 0.9611 | 2.4764  | 0.9472 |
|     |     | KNN          | 4.4249  | 0.9311 | 4.7877  | 0.7262 |
|     |     | LSTM         | 5.6241  | 0.8867 | 5.2494  | 0.8809 |
|     |     | Randomforest | 87.8839 | 0.9818 | 98.5633 | 0.9428 |
|     |     | XG-Boost     | 2.0686  | 0.9842 | 1.7618  | 0.9379 |
RandomForest+
|     |     |     | 2.0247 | 0.9921 | 1.2658 | 0.9897 |
| --- | --- | --- | ------ | ------ | ------ | ------ |
XG-Boost+LSTM
From this study and experimental analysis, we observed that the modification of
hyperparametersisacrucialstageintheprocessofstockforecastingasitcanmaximize
theperformanceofmachinelearningmodels. Table3listsmachinelearningmodelsthat
arefrequentlyusedinstockpriceforecasting. Nevertheless,theefficacyofthesemodels
ishighlydependentonthechoiceofhyperparameters,whichareparametersthatarenot
learnedfromthedata,butrather,definedbeforethelearningprocess.
Table3.Summaryofexistingstockpredictionandforecastingalgorithmswithperformanceanalysis.
| SrNo | AlgorithmName |     | GapAnalysis |     | PerformanceEvaluation |     |
| ---- | ------------- | --- | ----------- | --- | --------------------- | --- |
Linearregressionassumesalinear
relationshipbetweendependentand Thisisaregressiontypeofalgorithmthat
independentvariablesandisnotsuitable showsgraphsinalinearway,wherein
| 1   | Linearregression |     |     |     |     |     |
| --- | ---------------- | --- | --- | --- | --- | --- |
formostreal-timeapplications,andisused RMSEis3.22,MAEis2.53,MSEis10.37,
toperformobservationsonreadily andR-squaredis0.73(Gururajetal.2019).
accessiblesampledata(Gururajetal.2019).
Thisisaclassificationtypeofalgorithm,
SVM’sexcellentmemoryefficiencyand andwhenusedforstockprediction,the
effectivenessmakeitanidealestimating resultsareasfollows:accuracyis68.2,
techniqueinhigh-dimensionalspace.The recallis65.2,precisionis64.2,andF1-Score
Supportvector
| 2   |     | shortcomingofSVMisthatitmight |     | is64.9%(0.65). |     |     |
| --- | --- | ----------------------------- | --- | -------------- | --- | --- |
machine
experienceoverfitting,butitperforms Whenusedasasupportvectorregression
exceptionallywellontinydatasets(Pathak (SVR)algorithm,theevaluationparameters
|     |     | andPathak2020;Grigoryan2017). |     | areasfollows:SMAPE=5.59, |     |     |
| --- | --- | ----------------------------- | --- | ------------------------ | --- | --- |
R-squared=1.69,andRMSE=43.36.
ThisisaclassificationtypeofML
algorithminwhichtheresultsofstock
KNNisanalgorithmthatskipsthe
predictionareasfollows:accuracyis65.2,
learningstep,soitmaynotgeneralize
recallis63.6,precisionis64.8,andF1Score
effectively.Withahugedataset,ittakes
| 3   | K-nearestneighbor |     |     | is64.1%(0.64). |     |     |
| --- | ----------------- | --- | --- | -------------- | --- | --- |
longersinceitmustsortallthedistances
ForKNNregressor,theevaluation
fromtheunknownitem(Tanuwijayaand
parametersareasfollows:SMAPE=14.32,
Hansun2019;PathakandPathak2020).
R-squared=−2.42,andRMSE=56.44
(Venkat2022).

Int.J.FinancialStud.2023,11,94 16of22
Table3.Cont.
SrNo AlgorithmName GapAnalysis PerformanceEvaluation
ModelswithanintegratedGNBalgorithm GaussiannaïveBayesusedbyauthorsin
willyieldfeatureextractionandfeature theirresearch.Kendall’sTestof
scalingoutcomesthataresuperiortothose Concordanceisusedinthisfeature,which
Gaussiannaïve
4 alreadyachievedusingmodelsthat isscaledandextracted.Theresultsareas
Bayes
incorporateeithertheGNBalgorithmor follows:accuracyis84,F1Scoreis62.44%
featurescaling(Setianietal.2020; (0.62),specificityis0.70,andAUCvaluesis
Ampomahetal.2021). 0.90(Bansaletal.2022).
Inthisalgorithm,withthehelpofresearch
Bothbinaryandmulticlassclassification papers,variousfinancialfactorsare
usethisalgorithm.Thefindingsobtained consideredthroughwhichfactorsare
vialogisticregressionarethemostaccurate; groupedforprediction.Theresultsofthis
5 Logisticregression
however,identifyingthebest-fittingfeature algorithmareasfollows:accuracyis78.6,
isnecessary(PathakandPathak2020;Ali recallis76.6,precisionis77.8,andF1Score
etal.2018). is77.1%(0.77)(PathakandPathak2020;Ali
etal.2018).
ARIMAisatimeseriesforecasting
techniqueforpredictingmarketorstock
ARIMAcanbeconsideredbecauseitisa prices.Itisacombinationorintegrationof
uniquemodelwithsignificantcoefficients autoregressivemovingaverages;the
6 ARIMA
andpassesallthediagnostictests resultsareasfollows:RMSE,88.05;MAE,
(Mashadihasanli2022). 65.88;andMAPE,5.73,andifperformed
withsentimentanalysis,theRMSEscoreis
6.41(Kedar2021).
ThisalgorithmwascreatedbyFacebook
Prophetcanuseregressionmodelsto
fortimeseriesforecasting.Oneofits
determineseasonalityonadaily,monthly,
advantagesisthatitdoesnotconsider
7 FBProphet andannualbasis,aswellaseffectsrelated
holidaysornullvalues.Theresultofits
toholidays(Sureshetal.2022;Kaninde
RMSEisachieved93(Sureshetal.2022;
etal.2022).
Kanindeetal.2022).
GRUisadeeplearningalgorithmthathas
fewerparametersandhandlesshort-term
GRUisaneuralnetworkapproachthatis
dataproperly.Theevaluationparameters
animprovementuponRNNbuthasfewer
ofGRUare,withoutsentimentanalysis,
parametersthanLSTM,soittrainsfaster.
8 GRU MAE=42.8,RMSE=47.31,andR-squared
Also,thechancesofoverfittingarelower
=0.879,andwithsentimentanalysisbased
comparedtoRNN,anditcanhandle
onnewsevaluationparameters,
long-termdependency(Shahietal.2020).
MAE=24.472,RMSE=29.153,and
R-squared=0.967(Shahietal.2020).
LSTMisamoredevelopedtypeofRNN
andisadeeplearningtechnique.Thisis
oneofthemostusedMLalgorithmsfor
Inthisalgorithm,weightsareadjustedfor
stockforecasting,andwhenusedalong
eachlongshort-termmemorydatapoint
withsentimentanalysis,itshowsbetter
viastochasticgradientdescent.
resultsthanwithoutsentimentanalysis.
LSTMcanhandlemoreverylong-term
9 LSTM Theresultwithoutsentimentanalysisare
dependencycomparedtoanyotherneural
MAE=48.47,RMSE=55.993,and
networkalgorithm(Shahietal.2020;
R-squared=0.867,andwithsentiment
PramodandPm2021;Mukherjeeetal.
analysisbasedonnewsevaluation
2021).
parameters,areMAE=17.689,
RMSE=23.070,andR-squared=0.867
(Shahietal.2020).

Int.J.FinancialStud.2023,11,94 17of22
Table3.Cont.
SrNo AlgorithmName GapAnalysis PerformanceEvaluation
Theeffectivenessofrandomforestonlarge
datasetsisoneofitsadvantages.Itcanbe Thisisanensembletypeofalgorithmthat
appliedtoclassificationandregression isusedforstockforecasting.Theresultsfor
issues.Themodelbecomesmorerandom randomforestareasfollows:accuracyis
10 Randomforest
asaresult,improvingit.Thismodel’suse 80.7,recallis78.3,precisionis75.2,andF1
ofahugenumberoftreesslowsitdown, Scoreis76.7%(0.77)(PathakandPathak
whichisadrawback(PathakandPathak 2020;Polamurietal.2019).
2020;Polamurietal.2019).
XG-Boostisanensembledlearning
techniquethatusesdecisiontreesbutina
sequentialmannerandusesgradient
boostinginaniterativemannertoobtain XG-Boosthasthefollowingevaluation
11 XG-Boost
betterresults. parameter:MSE=360.0(ZhuandHe2022).
XG-Boostissensitivetohyperparameters
andwillnotworkaswellonlargedatasets
asrandomforest(ZhuandHe2022).
Ensemblesupportvectorregressionand
randomforestshowsimprovedaccuracyas TheE-SVR-RFensembledalgorithmshows
itleveragestheadvantagesofboth thefollowingevaluationparameters:
12 E-SVR-RF algorithms,anditsrobustnessisincreased, MAPE=1.335,MAE=0.1537,
butduetotheincreasedcomplexityofboth RMSE=0.0188,andMAE=0.0485
algorithms,overfittingisanissue (Xuetal.2020).
(Xuetal.2020).
EnsemblingXG-BoostandLSTMcan
leveragetheadvantagesofbothalgorithms.
XG-Boostcanhandlelinearandnon-linear TheensemblealgorithmofXG-Boost+
13 XG-Boost+LSTM relationshipsandLSTMcanhandle LSTMshowsthefollowingevaluation
long-termdependence.Duetothis parameter:MSE=3.465(Vuongetal.2022).
algorithm’scomplexity,hyperparameter
tuningcanbeanissue(Vuongetal.2022).
Blendingensemble(LSTM+GRU)isa
combinationoftwotoofthemost-used
Theblendingensemblealgorithm,which
improvementstoRNNandsolvesthe
consistsofamodifiedversionofRNN,i.e.,
vanishinggradientproblem.Bothofthem
LSTMandGRU,hasthefollowing
Blendingensemble canhandlelong-termdependencewell,
14 evaluationparameters:
(LSTM+GRU) andcombiningthemwouldimprove
MSE=186.32,MPA=99.65,
forecasting;also,overfittingcanbereduced.
precision=60%,Recall=75%,
Itmayrequirehighcomputationalpower
F1-Score=66.67%(LiandPan2021).
andtimetotrainbothLSTMandGRU(Li
andPan2021).
Thenextpartofthissectionillustratesthecomparativeanalysisofworkconductedby
multipleauthorsonvariousclassification,regression,andtimeseries-basedalgorithmsto
evaluatetheirperformanceinstockmarketforecasting,asshowninTable3. Thealgorithms
wereassessedusingvariousevaluationparameters,includingaccuracy,recall,precision,F1
Score,MSE,MAE,RMSE,andR-squarederror. Theaimwastoidentifyeffectivealgorithms
thatcouldbenefitawideraudience,includinggeneralappliedresearchersandintelligent
laypersons,enablingthemtomakeinformedinvestmentdecisions. Thesefindingswillalso
providevaluableinsightsforresearchers,investors,andgeneralaudiences,enablingthem
tomakewell-informeddecisionsandnavigatethecomplexitiesofthefinancialmarket.
5. ImplicationsandLimitationsoftheStudy
Thisstudyfocusedontheapplicationofmachinelearninganddeeplearningmodels
instockforecasting. Itcanbenotedthatmachinelearningordeeplearningmodelsalone

Int.J.FinancialStud.2023,11,94 18of22
arenotsufficient. Ensembletechniquesarecapableofprovidingsuperiorperformance.
But merely developing a model is not enough, and emphasis should also be placed on
hyperparametertuning. Theperformanceofthemodelcanbeimprovedusinghyperpa-
rameterssuchaslearningrates,regularizationincasesofdeeplearning,thenumberof
hiddenlayers,max_depth,n_estimators,andlearningrate. Choosingthepropersettings
forthesehyperparameterscanconsiderablyenhancetheprecisionofstockforecasts. For
instance,amodelwithagreaterlearningratemayconvergemorequicklybutmayalso
besusceptibletooverfitting,whereasamodelwithalowerlearningratemayconverge
moreslowlybutgeneralizebettertonewdata. Tuninghyperparametersentailschoosing
theoptimalcombinationofhyperparametersforagivendatasetandmodelarchitecture.
Thisprocedureoftenentailstrainingmanymodelswithdistincthyperparametervalues
andevaluatingtheirperformanceonavalidationdataset. Typically,theoptimalcombi-
nationofhyperparametersisdeterminedbythemodel’scapacitytoreducethedeviation
betweenpredictedandactualstockprices. Thestudyofmachinelearningmodelsanddeep
learningmodelsandthecomparativeresultspresentedinthisarticlewillguideresearchers
inchoosingidealandpreferredmachinelearninganddeeplearningalgorithmsfortheir
respectiveresearchwork.
6. FutureResearchDirections
Thepresentedreviewarticleisfocusedonthereviewofrelatedandpublishedarticles
onstockpriceprediction,forecasting,andclassification. Theanalysisoffinancialinstru-
mentssuchasstocksandequitiesisaconsiderablechallenge.Itissaidthatthestockmarket
evolvesoveraperiodoftime(LimandBrooks2011),andhence,theapproachesdeveloped
forhandlingspecificproblemswillseelowperformancesoonerorlatereventhoughtheir
performanceisfoundtobeappreciatedinitially. Asthestockmarketevolvesunderthe
influence of various factors such as geopolitical issues, equity trading, and investment,
theunderlyingchallengesalsochange,andsodothemethodologiesforaddressingthe
newchallenges(SprengerandWelpe2011;Shahetal.2019). Sufficientresearchhasbeen
presentedonstockpricepredictionandstockclassification,whichistheprimaryfocusof
thisreviewarticle. Basedonthestudypresentedinthisarticle,wehaveidentifiedsomeof
thekeyareaswhereresearchersshouldfocustheirattentionandexplorebettersolutions.
Inthissection,anattemptismadetoopennewresearchavenuesforresearchersinthefield
ofstockmarketresearch.
6.1. TrendAnalysisandClassification
Most researchers are inclined towards solving the problem of price prediction or
forecastingstockvalueseries. Itisimportanttoknowthemovementofstockprices,aswell.
Webelievethatresearcherscanexplorethepossibleusageofstate-of-the-artdeeplearning
andmachinelearningalgorithmsinstocktrendpredictionandclassification(Jiang2021;
Nikouetal.2019).
6.2. PatternIdentificationUsingComputerVision
Most researchers see stock price as time series data, which is true. But time series
numericaldatacanbetransformedintoimages,andpatternsintheimagescanbeidentified
tounderstandnewtrendsoccurringinthepricechanges(Barraetal.2020). Duetothe
advancement of deep learning in the form of pre-trained models and transfer learning,
researcherscanexploreopportunitiestoapplythesemodelstounderstandingtheimages
generatedbasedontimeseriesdata.
6.3. ChartPatternAnalysisUsingComputerVision
Chart pattern analysis is one of the most-applied approaches among traders and
investors. Candlesticksoftenformfascinatingpatterns(Caglieroetal.2023;Huetal.2019),
whichhelpstradersincapturingpriceactionwellbeforeitoccurs.Butthebiggestdrawback
ofchartpatternanalysisistheperceptionoftheviewer. Generally,thesechartpatternsare

Int.J.FinancialStud.2023,11,94 19of22
identifiedbasedontheperceptionsoftraders. Everytraderwillhaveadifferentperception
ofthemarket,andtheemotionsoftraderstendtoprojectdifferentpatternsforthesame
priceaction. Forexample,itisdifficulttodifferentiatebetweendouble-topandtriple-top
candlestickpatterns(Lambert2009). Researcherscanaddresstheproblemofcandlestick
patternidentificationusingsuitabledeep-learningtechniquessothatperceptionbiascan
beavoidedamongsttraders.
7. Conclusions
Inthisreview,severalconventional,machinelearning,anddeeplearningtechniques
that are employed in stock market forecasting are investigated. This review describes
variousmachinelearningtechniques,deeplearningtechniques,andtimeseriesforecasting
techniques. Thisarticlepresentsrecentapplicationsofmachinelearninganddeeplearning
models,andanensemblemodelisalsotestedontheTAINIWALCHMandAGROPHOS
stockdatasets. Despitetheexistenceofseveralpopularmethodsforstockpriceforecasting,
eventoday,thereisnouniversalsolutiontoaccuratelypredictthestockpriceortrendofthe
market. ThereisstillapossibilitythatAI-basedmodelscanalsofailiftheyarenottrained
efficientlywithfreshdata. Toconcludethisarticle,weassertthatresearchersshouldkeep
exploringnewavenuestosolvepriceactionproblemsusingensembletechniques. Stock
forecastingmodelsshouldbeenhancedwithsuitablehyperparametertuningsothatthey
canserveasprecisestockpricepredictionmodels. Tradersandinvestmentadvisorscan
usemachinelearninganddeeplearningmodelsasadditionalconfirmationindicatorsto
supporttheirdecisions,anddecisionsshouldnotrelyonlyonAI-basedpriceforecasting
methods. Alongwithstockforecastingtechniques,researchersinthefuturecanexpand
theirstudiestoportfoliomanagement,tradingstrategydesign,andinvestmentdecision
making.
AuthorContributions: ConceptualizationG.S.,D.S.D.andA.M.B.; Visualization,G.S.; Writing—
originaldraft,G.S.,D.S.D.andA.M.B.;Supervision,D.S.D.andA.M.B.;Writing—review&editing,
S.T.D.,D.D.,S.K.B.Allauthorshavereadandagreedtothepublishedversionofthemanuscript.
Funding:Thisresearchreceivednoexternalfunding.
InformedConsentStatement:Notapplicable.
DataAvailabilityStatement:Notapplicable.
ConflictsofInterest:Theauthorsdeclarenoconflictofinterest.
References
Agrawal,Manish,PiyushKumarShukla,RajitNair,AnandNayyar,andMehediMasud.2022.StockPredictionBasedonTechnical
IndicatorsUsingDeepLearningModel.Computers,Materials&Continua70:287–304.
Ali,SyedShahan,MuhammadMubeen,andAdnanHussain.2018.Predictionofstockperformancebyusinglogisticregressionmodel:
EvidencefromPakistanStockExchange(PSX).AsianJournalofEmpiricalResearch15:212.
Ampomah,ErnestKwame,GabrielNyame,ZhiguangQin,PrinceClementAddo,EnochOpaninGyamfi,andMichealGyan.2021.
StockMarketPredictionwithGaussianNaïveBayesMachineLearningAlgorithm.Informatica45:2.[CrossRef]
Baheti,Radhika,GauriShirkande,SnehaBodake,JanhaviDeokar,andArchanaK.2021.StockMarketAnalysisfromSocialMediaand
NewsusingMachineLearningTechniques.InternationalJournalonDataScienceandMachineLearningwithApplications1:59–67.
Ballings,Michel,DirkVandenPoel,NathalieHespeels,andRubenGryp.2015.Evaluatingmultipleclassifiersforstockpricedirection
prediction.ExpertSystemswithApplications42:7046–56.[CrossRef]
Banik,Shouvik,NonitaSharma,MonikaMangla,SachiNandanMohanty,andSelvarajanShitharth. 2022. LSTMbaseddecision
supportsystemforswingtradinginstockmarket.Knowledge-BasedSystems239:107994.[CrossRef]
Bansal,Malti,ApoorvaGoyal,andApoorvaChoudhary.2022.StockMarketPredictionwithHighAccuracyusingMachineLearning
Techniques.ProcediaComputerScience215:247–65.[CrossRef]
Barra, Silvio, SalvatoreMarioCarta, AndreaCorriga, AlessandroSebastianPodda, andDiegoReforgiatoRecupero. 2020. Deep
learningandtimeseries-to-imageencodingforfinancialforecasting.IEEE/CAAJournalofAutomaticaSinica7:683–92.[CrossRef]
Bustos,Oscar,AlexandraPomares,andEnriqueGonzalez.2017.AcomparisonbetweenSVMandmultilayerperceptroninpredicting
an emerging financial market: Colombian stock market. Paper presented at 2017 Congreso Internacional de Innovacion y
TendenciasenIngenieria(CONIITI),Bogotá,Colombia,October4–6;pp.1–6.

Int.J.FinancialStud.2023,11,94 20of22
Cagliero, Luca, Jacopo Fior, and Paolo Garza. 2023. Shortlisting machine learning-based stock trading recommendations using
candlestickpatternrecognition.ExpertSystemswithApplications216:119493.[CrossRef]
Di Persio, Luca, and Oleksandr Honchar. 2017. Recurrent neural networks approach to the financial forecast of Google assets.
InternationalJournalofMathematicsandComputersinSimulation11:7–13.
Dospinescu,Nicoleta,andOctavianDospinescu.2019.AProfitabilityRegressionModelInFinancialCommunicationOfRomanian
StockExchange’sCompanies.EcoforumJournal8:4.
Gite,Shilpa,ShrutiPatil,DeepakDharrao,MadhuriYadav,SnehaBasak,ArundarasiRajendran,andKetanKotecha.2023.Textual
FeatureExtractionUsingAntColonyOptimizationforHateSpeechClassification. BigDataandCognitiveComputing7: 45.
[CrossRef]
Grigoryan,Hakob.2017.StockMarketTrendPredictionUsingSupportVectorMachinesandVariableSelectionMethods.Advancesin
IntelligentSystemsResearch(AISR)2017:210–13.[CrossRef]
Gururaj,Vaishnavi,V.R.Shriya,andK.Ashwini.2019.StockMarketPredictionusingLinearRegressionandSupportVectorMachines.
InternationalJournalofAppliedEngineeringResearch14:1931–34.
Hu,Weilong,Yain-WharSi,SimonFong,andRaymondYiuKeungLau.2019.Aformalapproachtocandlestickpatternclassification
infinancialtimeseries.AppliedSoftComputing84:105700.[CrossRef]
Hu,Zexin,YiqiZhao,andMatloobKhushi.2021.Asurveyofforexandstockpricepredictionusingdeeplearning.AppliedSystem
Innovation4:9.[CrossRef]
Jiang,Weiwei.2021.Applicationsofdeeplearninginstockmarketprediction:Recentprogress.ExpertSystemswithApplications184:
115537.[CrossRef]
Jose,Jithina,SujaCherukullapurathMana,andB.KeerthiSamhitha. 2019. AnEfficientSystemtoPredictandAnalyzeStockData
usingHadoopTechniques.InternationalJournalofRecentTechnologyandEngineering(IJRTE)8:1039–43.[CrossRef]
Kaczmarek, Tomasz, andKatarzynaPerez. 2021. Buildingportfoliosbasedonmachinelearningpredictions. EconomicResearch-
EkonomskaIstraživanja35:19–37.[CrossRef]
Kaninde, Sumedh, Manish Mahajan, Aditya Janghale, and Bharti Joshi. 2022. Stock Price Prediction Using Facebook Prophet.
InternationalJournalofResearchinEngineeringandScience44:03060.[CrossRef]
Kardani,Navid,AnnanZhou,MajidrezaNazem,andShui-LongShen.2020.Improvedpredictionofslopestabilityusingahybrid
stackingensemblemethodbasedonfiniteelementanalysisandfielddata.JournalofRockMechanicsandGeotechnicalEngineering
13:188–201.[CrossRef]
Kedar,S.V.2021.StockMarketIncreaseandDecreaseusingTwitterSentimentAnalysisandARIMAModel.TurkishJournalofComputer
andMathematicsEducation(TURCOMAT)12:146–61.[CrossRef]
Khairi,TeabaW.A.,RanaM.Zaki,andWisamA.Mahmood.2019.StockPricePredictionusingTechnical,FundamentalandNews
basedApproach.Paperpresentedat20192ndScientificConferenceofComputerSciences(SCCS),Baghdad,Iraq,March27–28.
Khan,Wasiat,MustansarAliGhazanfar,MuhammadAwaisAzam,AminKarami,KhaledH.Alyoubi,andAhmedS.Alfakeeh.2020.
Stockmarketpredictionusingmachinelearningclassifiersandsocialmedia,news.JournalofAmbientIntelligenceandHumanized
Computing13:3433–56.[CrossRef]
Kumar,Deepak,PradeeptaKumarSarangi,andRajitVerma. 2021. Asystematicreviewofstockmarketpredictionusingmachine
learningandstatisticaltechniques.MaterialsToday:Proceedings49:3187–91.[CrossRef]
Kumar,Saurav,andDhrubaNingombam. 2018. Short-TermForecastingofStockPricesUsingLongShortTermMemory. Paper
presentedat2018InternationalConferenceonInformationTechnology(ICIT),HongKong,China,December29–31.
Lambert,Clive.2009.CandlestickCharts:AnIntroductiontoUsingCandlestickCharts.Petersfield:HarrimanHouseLimited.
Li,AudelianoWolian,andGuilhermeSousaBastos.2020.StockMarketForecastingUsingDeepLearningandTechnicalAnalysis:A
SystematicReview.IEEEAccess8:185232–242.[CrossRef]
Li,Yang,andYiPan.2021.Anovelensembledeeplearningmodelforstockpredictionbasedonstockpricesandnews.International
JournalofDataScienceandAnalytics13:139–49.[CrossRef][PubMed]
Lim,Kian-Ping,andRobertBrooks. 2011. Theevolutionofstockmarketefficiencyovertime: Asurveyoftheempiricalliterature.
JournalofEconomicSurveys25:69–108.[CrossRef]
Lim,YiXuan,andConsilzTan.2021.Donegativeeventsreallyhavedeterioratingeffectsonstockperformance?Acomparativestudy
onTesla(US)andNio(China).JournalofAsianBusinessandEconomicStudies29:105–19.[CrossRef]
Manish,Kumar,andM.Thenmozhi.2014.ForecastingstockindexreturnsusingARIMA-SVM,ARIMA-ANN,andARIMA-random
foresthybridmodels.InternationalJournalofBankingAccountingandFinance5:284–308.
Mann,Jordan,andJ.NathanKutz. 2016. Dynamicmodedecompositionforfinancialtradingstrategies. QuantitativeFinance16:
1643–55.[CrossRef]
Manojlovic´,Teo,andIvanŠtajduhar.2015.Predictingstockmarkettrendsusingrandomforests:AsampleoftheZagrebstockexchange.
PaperpresentedatInternationalConventiononInformationandCommunicationTechnologyElectronicsandMicroelectronics,
Opatija,Croatia,May25–29.
Mashadihasanli,Tamerlan.2022.StockMarketPriceForecastingUsingtheArimaModel:AnApplicationtoIstanbul,Turkiye.Journal
ofEconomicPolicyResearches9:439–54.[CrossRef]

Int.J.FinancialStud.2023,11,94 21of22
Mohapatra,Sabyasachi,RohanMukherjee,ArindamRoy,AnirbanSengupta,andAmitPuniyani. 2022. CanEnsembleMachine
LearningMethodsPredictStockReturnsforIndianBanksUsingTechnicalIndicators?JournalofRiskandFinancialManagement8:
350.[CrossRef]
Mukherjee,Somenath,BikashSadhukhan,NairitaSarkar,DebajyotiRoy,andSoumilDe.2021.Stockmarketpredictionusingdeep
learningalgorithms.CAAITransactionsonIntelligenceTechnology8:82–94.[CrossRef]
Nabipour,Mojtaba,PooyanNayyeri,HamedJabani,S.Shahab,andAmirMosavi.2020.PredictingStockMarketTrendsUsingMachine
LearningandDeepLearningAlgorithmsViaContinuousandBinaryData;aComparativeAnalysis.IEEEAccess8:150199–212.
[CrossRef]
Nikou,Mahla,GholamrezaMansourfar,andJamshidBagherzadeh.2019.StockpricepredictionusingDEEPlearningalgorithmandits
comparisonwithmachinelearningalgorithms.IntelligentSystemsinAccounting,FinanceandManagement26:164–74.[CrossRef]
Nti,IsaacKofi,AdebayoFelixAdekoya,andBenjaminAsubamWeyori.2020.Acomprehensiveevaluationofensemblelearningfor
stock-marketprediction.JournalofBigData7:1–40.[CrossRef]
Obthong,Mehtabhorn,NongnuchTantisantiwong,WatthanasakJeamwatthanachai,andGaryWills. 2020. ASurveyonMachine
LearningforStockPricePrediction:AlgorithmsandTechniques.Paperpresentedat2ndInternationalConferenceonFinance,
Economics,ManagementandITBusiness,Prague,CzechRepublic,May5–6.
Parray,IrfanRamzan,SurinderSinghKhurana,MunishKumar,andAliA.Altalbe. 2020. Timeseriesdataanalysisofstockprice
movementusingmachinelearningtechniques.SoftComputing24:16509–17.[CrossRef]
Patel,Jigar,SahilShah,PriyankThakkar,andKetanKotecha. 2015. PredictingstockandstockpriceindexmovementusingTrend
DeterministicDataPreparationandmachinelearningtechniques.ExpertSystemswithApplications42:259–68.[CrossRef]
Pathak,Ashwini,andSakshiPathak.2020.StudyofMachinelearningAlgorithmsforStockMarketPrediction.InternationalJournalof
EngineeringResearch&Technology(IJERT)9:6.
Polamuri,SubbaRao,KudipudiSrinivas,andA.KrishnaMohan.2019.StockMarketPricesPredictionusingRandomForestandExtra
TreeRegression.InternationalJournalofRecentTechnologyandEngineering8:1224–28.[CrossRef]
Pramod,B.S.,andMallikarjunaShastryPm.2021.StockPricePredictionUsingLSTM.TestEngineeringandManagement83:5246–51.
Qiu,Jiayu,BinWang,andChangjunZhou. 2020. Forecastingstockpriceswithlong-shorttermmemoryneuralnetworkbasedon
attentionmechanism.PLoSONE15:e0227222.[CrossRef][PubMed]
Raghavendra,Kumar,PardeepKumar,andYugalKumar.2021.Analysisoffinancialtimeseriesforecastingusingdeeplearningmodel.
Paperpresentedat202111thInternationalConferenceonCloudComputing,DataScience&Engineering(Confluence),Uttar
Pradesh,India,January28–29;pp.877–81.
Reddy,NivedithaN.,E.Naresh,andVijayaKumarB.P.2020. PredictingStockPriceUsingSentimentalAnalysisThroughTwitter
Data. Paperpresentedat2020IEEEInternationalConferenceonElectronics,ComputingandCommunicationTechnologies
(CONECCT),Bangalore,India,July2–4.
Ren,Rui,DeshengDashWu,andTianxiangLiu.2019.ForecastingStockMarketMovementDirectionUsingSentimentAnalysisand
SupportVectorMachine.IEEESystemsJournal13:760–70.[CrossRef]
Sadorsky,Perry.2021.ARandomForestsApproachtoPredictingCleanEnergyStockPrices.JournalofRiskandFinancialManagement
14:48.[CrossRef]
Salles,Thiago,MarcosGonçalves,VictorRodrigues,andLeonardoRocha.2018.Improvingrandomforestsbyneighborhoodprojection
foreffectivetextclassification.InformationSystems77:1–21.[CrossRef]
SathishKumar,R.,R.Girivarman,S.Parameshwaran,andV.Sriram.2020.StockPricePredictionUsingDeepLearningandSentimental
Analysis.JETIR7:346–54.
Seethalakshmi,Ramaswamy.2018.Analayisofstockmarketpredictorvariablesusinglinearregression.InternationalJournalofPureand
AppliedMathematics119:369–78.
Setiani,Ida,MeilanyNonsiTentua,andSunggitoOyama.2020.PredictionofBankingStockPricesUsingNaïveBayesMethod.Journal
ofPhysicsConferenceSeries1823:012059.[CrossRef]
Shah,Dev,HarunaIsah,andFarhanaZulkernine.2019.StockMarketAnalysis:AReviewandTaxonomyofPredictionTechniques.
InternationalJournalofFinancialStudies7:26.[CrossRef]
Shahi, Tej Bahadur, Ashish Shrestha, Arjun Neupane, and William Guo. 2020. Stock Price Forecasting with Deep Learning: A
ComparativeStudy.MathematicsandComputerScience8:1441.[CrossRef]
Sharaf,Marwa,EzzEl-DinHemdan,AymanEl-Sayed,andNirmeenA.El-Bahnasawy.2022.Anefficienthybridstocktrendprediction
systemduringCOVID-19pandemicbasedonstacked-LSTMandnewssentimentanalysis.MultimediaToolsandApplications28:
1–33.[CrossRef]
Shen,Jingyi,andM.OmairShafiq.2020.Short-termstockmarketpricetrendpredictionusingacomprehensivedeeplearningsystem.
JournalofBigData7:1–33.[CrossRef]
Sidra,Mehtab,andJaydipSen.2020.Atimeseriesanalysis-basedstockpricepredictionusingmachinelearninganddeeplearning
models.arXivarXiv:2004.11697.
Smita,Mrinalini.2021.LogisticRegressionModelForPredictingPerformanceofS&PBSE30CompanyUsingIBMSPSS.International
JournalofMathematicsTrendsandTechnology67:118–34.[CrossRef]
Soni,Payal,YogyaTewari,andDeepaKrishnan.2022.MachineLearningapproachesinstockpriceprediction:Asystematicreview.
JournalofPhysicsConferenceSeries2161:012065.[CrossRef]

Int.J.FinancialStud.2023,11,94 22of22
Sprenger,TimmO.,andIsabellM.Welpe.2011.Newsornoise?Thestockmarketreactiontodifferenttypesofcompany-specificnews
events.SSRNElectronicJournal.[CrossRef]
Suresh,N.,B.Priya,andG.Lakshmi.2022.HistoricalAnalysisandForecastingofStockMarketUsingFbprophet.SouthAsianJournal
ofEngineeringandTechnology12:152–57.[CrossRef]
Tanuwijaya,Julius,andSengHansun.2019.LQ45StockIndexPredictionusingk-NearestNeighborsRegression.InternationalJournalof
RecentTechnologyandEngineering8:2388–91.[CrossRef]
Umer,Muhammad,MuhammadAwais,andMuhammadMuzammul.2019.StockMarketPredictionUsingMachineLearning(ML)
Algorithms.ADCAIJAdvancesinDistributedComputingandArtificialIntelligenceJournal8:97–116.[CrossRef]
Venkat,Projects.2022.StockMarketTrendPredictionUsingK-NearestNeighbor(KNN)Algorithm.JournalofEngineeringSciences
3:32–44.
Vo,Nguyen,andRobertS´lepaczuk.2022.ApplyingHybridARIMA-SGARCHinAlgorithmicInvestmentStrategiesonS&P500Index.
Entropy24:158.[CrossRef][PubMed]
Vuong,PhamHoang,TrinhTanDat,TieuKhoiMai,andPhamHoangUyen.2022.Stock-PriceForecastingBasedonXGBoostand
LSTM.ComputerSystemsScience&Engineering40:237–46.
Xu,Ying,CuijuanYang,ShaoliangPeng,andYusukeNojima.2020.Ahybridtwo-stagefinancialstockforecastingalgorithmbasedon
clusteringandensemblelearning.AppliedIntelligence50:3852–67.[CrossRef]
Yadav,Ashima,andDineshKumarVishwakarma. 2019. Sentimentanalysisusingdeeplearningarchitectures: Areview. Artificial
IntelligenceReview53:4335–85.[CrossRef]
Yang,Liu.2019.Novelvolatilityforecastingusingdeeplearning-longshorttermmemoryrecurrentneuralnetworks.ExpertSystems
withApplications132:99–109.
Zhong,Xiao,andDavidEnke.2019.Predictingthedailyreturndirectionofthestockmarketusinghybridmachinelearningalgorithms.
FinancialInnovation5:1–20.[CrossRef]
Zhou,Xingyu,ZhisongPan,GuyuHu,SiqiTang,andChengZhao.2018.StockMarketPredictiononHigh-FrequencyDataUsing
GenerativeAdversarialNets.MathematicalProblemsinEngineering2018:4907423.[CrossRef]
Zhu,Yongqiong.2020.StockpricepredictionusingtheRNNmodel.JournalofPhysicsConferenceSeries1650:032103.[CrossRef]
Zhu,Zhe,andKexinHe. 2022. PredictionofAmazon’sStockPriceBasedonARIMA,XGBoost,andLSTMModels. Proceedingsof
BusinessandEconomicStudies5:127–36.[CrossRef]
Zizi,Youssef,AmineJamali-Alaoui,BadreddineElGoumi,MohamedOudgou,andAbdeslamElMoudden.2021.AnOptimalModel
ofFinancialDistressPrediction:AComparativeStudybetweenNeuralNetworksandLogisticRegression.Risks9:200.[CrossRef]
Disclaimer/Publisher’s Note: The statements, opinions and data contained in all publications are solely those of the individual
author(s)andcontributor(s)andnotofMDPIand/ortheeditor(s).MDPIand/ortheeditor(s)disclaimresponsibilityforanyinjuryto
peopleorpropertyresultingfromanyideas,methods,instructionsorproductsreferredtointhecontent.