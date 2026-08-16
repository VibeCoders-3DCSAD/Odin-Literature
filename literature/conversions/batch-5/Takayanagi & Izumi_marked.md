---
conversion_metadata:
  converted_at: "2026-07-21T08:54:50Z"
  converter_tool: "markitdown"
  converter_version: "0.1.6"
  source_pdf: "Takayanagi & Izumi.pdf"
  source_pdf_sha256: "d7fc7245591892da2db7fd0c6cd363ea1c27369d1c31c8d109b09b33f4ec290f"
  page_count: 15
  markdown_char_count: 74137
---

<!-- PAGE-AWARE EXTRACTION (via pdfminer.six) -->

<!-- PAGE 1 -->

New Generation Computing (2024) 42:635–649
https://doi.org/10.1007/s00354-024-00241-w

Incorporating Domain-Speciﬁc Traits into
Personality-Aware Recommendations for Financial
Applications

Takehiro Takayanagi1

· Kiyoshi Izumi1

Received: 18 August 2023 / Accepted: 14 November 2023 / Published online: 25 February 2024
© The Author(s) 2024

Abstract
The general personality traits, notably the Big-Five personality traits, have been
increasingly integrated into recommendation systems. The personality-aware recom-
mendations, which incorporate human personality into recommendation systems, have
shown promising results in general recommendation areas including music, movie,
and e-commerce recommendations. On the other hand, the number of research delving
into the applicability of personality-aware recommendations in specialized domains
such as ﬁnance and education remains limited. In addition, these domains have unique
challenges in incorporating personality-aware recommendations as domain-speciﬁc
psychological traits such as risk tolerance and behavioral biases play a crucial role
in explaining user behavior in these domains. Addressing these challenges, this study
addresses an in-depth exploration of personality-aware recommendations in the ﬁnan-
cial domain, speciﬁcally within the context of stock recommendations. First, this study
investigates the beneﬁts of deploying general personality traits in stock recommenda-
tions through the integration of personality-aware recommendations with user-based
collaborative ﬁltering approaches. Second, this study further veriﬁes whether incor-
porating domain-speciﬁc psychological traits along with general personality traits
enhances the performance of stock recommender systems. Thirdly, this paper intro-
duces a personalized stock recommendation model that incorporates both general
personality traits and domain-speciﬁc psychological traits as well as transaction data.
The experimental results show that the proposed model outperformed baseline models
in ﬁnancial stock recommendations.

B Takehiro Takayanagi

takayanagi-takehiro590@g.ecc.u-tokyo.ac.jp

Kiyoshi Izumi
izumi@sys.t.u-tokyo.ac.jp

1 Department of Engineering, The University of Tokyo, Hongo 7-3-1, Bunkyo-ku 1138656, Tokyo,

Japan

123

---

<!-- PAGE 2 -->

636

New Generation Computing (2024) 42:635–649

Keywords Stock recommendation · Financial data mining · Collaborative ﬁltering ·
Behavioral ﬁnance

1 Introduction

In the current digital era, users are presented with an overwhelming amount of online
information and multiple sources of knowledge, which can lead to a phenomenon
known as information overload. Recommender systems represent a promising
approach to assist users in managing this challenge by suggesting items that match
their preferences. Personality is a core human characteristic that remains relatively
stable across time and is suitable for modeling user behavior, in contrast to emotions
and mood, which tend to be more transient and context-dependent. Incorporating per-
sonality into recommender systems can improve the accuracy of recommendations and
enhance user satisfaction by tailoring suggestions to their individual characteristics.
Personality traits have gained signiﬁcant attention in recommender systems due
to their potential to mitigate the cold-start problem when we do not have access to a
user’s interaction data, enhance recommendation diversity, and capture users’ com-
plex nature [1, 2]. Accordingly, recent studies have demonstrated the effectiveness of
personality-aware recommendation [1–3], which employs personality traits to make
recommendations, in general domains with abundant open data such as ﬁlms, music,
and books.

While personality-aware recommendation systems have demonstrated success in
general domains where data is readily available, research on their applicability in
speciﬁc domains, such as ﬁnance, has been limited due to privacy concerns and the
requirement for domain expertise to produce precise recommendations [1, 4]. Con-
sequently, it is worthwhile to explore the potential usefulness of personality traits
in ﬁnance recommendation systems, as they may help address challenges such as
information overload in the ﬁnancial domain.

In addition, it is important to note that domain-speciﬁc variables can have a sig-
niﬁcant impact on decision-making processes, particularly in the domain of ﬁnance
while previous studies on personality-aware recommendation have mainly focused on
general personality traits, such as the Big-Five personality traits [5]. For instance, fac-
tors such as risk tolerance play a critical role in investment decision-making, but may
not be as relevant in movie or music recommendations. Thus, it is essential to con-
sider domain-speciﬁc variables when developing personality-aware recommendation
systems for ﬁnance to ensure that they accurately capture the unique characteristics
of this domain.

Finally, personality-aware recommendation systems have primarily been used to
address the cold-start problem in recommendation [1, 3], but their potential to enhance
existing recommendation models with transaction data remains underexplored [2].
Therefore, it is also intriguing to investigate whether incorporating general personality
traits and domain-speciﬁc psychological traits in non-cold start settings can lead to
improved performance in recommendation systems.

In summary, we formulated the following research questions.

123

---

<!-- PAGE 3 -->

New Generation Computing (2024) 42:635–649

637

1. RQ1: Can general personality traits be useful in stock recommendation tasks?
2. RQ2: Do domain-speciﬁc psychological traits contribute to the performance of

stock recommendations?

3. RQ3: How can we integrate investors’ general personality traits and domain-
speciﬁc psychological traits with their interaction history to enhance the stock
recommendation model?

The rest of this work broadly corresponds to the research questions.

2 Related Work

2.1 Personality-Aware Recommender System

Personality traits have been increasingly utilized in the research of recommendation
[1–3, 6]. Utilizing personality traits for a recommender system has three advantages.
First, using personality traits for the recommender system will mitigate the cold-start
problem, especially for new users rather than items. Second, personality traits can be
used to increase recommendation diversity [7]. Third, personality traits help model
the complex nature of user behaviors. For example, personality traits are known to
be signiﬁcantly correlated with users’ preferences in some areas such as music and
movie preference [3, 6].

Various theories in the literature of personality psychology have attempted to
describe human personality traits. Among other theories, the Five-factor model, also
known as the Big-Five personality traits theory is one of the most commonly used
models, where the human personality is characterized by ﬁve factors: Extraversion,
Openness to experience, Conscientiousness, Agreeableness, and Neuroticism [5].

While ﬁve-factor models are widely used to measure the users’ similarity across
various domains in personality-aware recommendations, most works only utilize per-
sonality traits to represent users’ psychological traits and ignore other psychological
effects which might be as important as personality traits [3, 6]. Thus, previous stud-
ies have not explored the beneﬁt of incorporating domain-speciﬁc psychological traits
such as behavioral biases in ﬁnance into the personality-aware recommendation model.

2.2 Stock Recommendation

There is a growing demand for stock recommendations as the number of retail investors
using online brokers has been rapidly increasing. Accordingly, many studies have
tackled stock recommendation tasks. Stock recommendations can be classiﬁed into
two approaches: non-personalized stock recommendations and personalized stock
recommendations. Most works in stock recommendation fall within the scope of non-
personalized recommendation, which focuses on identifying optimal strategies for
selecting stocks or portfolios that are likely to be more proﬁtable in the future [8]. On
the other hand, little research has been done on personalized stock recommendations
due to the lack of open data and difﬁculties in data collection due to privacy concerns
[4, 9–13]. Despite the limited literature on the subject, some studies have tackled the

123

---

<!-- PAGE 4 -->

638

New Generation Computing (2024) 42:635–649

problem of personalized stock recommendations. Collaborative ﬁltering has been used
for personalized stock recommendations, oftentimes combined with other recommen-
dation approaches such as order book analysis, and multiple criteria decision analysis
[4, 9, 10]. For instance, Robin et al. [4] estimate the investor’s risk tolerance from
users’ portfolios and recommends stock based on the relevance of the stock’s risk
return with the user’s risk tolerance combined with a collaborative ﬁltering method.
The method of personalizing stock recommendations based on investors’ risk tolerance
has two shortcomings. First, it suffers from the cold-start problem. Second, it is not
clear whether one variable, risk tolerance, can capture the complex nature of investors.
Therefore, the beneﬁt of personality-aware recommendations which can mitigate the
cold-start problem and help model users’ behaviors needs to be investigated for stock
recommendations.

2.3 Behavioral Finance

The theory of modern economics is built on the assumption that human beings are
rational agents. These agents aim to maximize their wealth and minimize risk, care-
fully assessing the risk and return of investment choices to obtain a portfolio that
matches their risk aversion. However, empirical studies suggest that the real individ-
ual investors’ behaviors are different from those of the assumption. The literature in
behavioral ﬁnance has shown that psychological traits such as behavioral biases, per-
sonality, and cognitive ability affect the ﬁnancial behaviors of individual investors and
suggested that these psychological traits and biases are useful in explaining individual
investors’ behavior. The relationships among investors’ traits—such as personality,
behavioral biases, cognitive ability, and investment goals—have been extensively
studied. This examination spans both empirical research in behavioral ﬁnance and
theoretical studies. While empirical studies highlight the value of domain-speciﬁc psy-
chological factors, including behavioral biases, in explaining and predicting investor
behavior, their beneﬁts remain unexplored in personality-aware recommendations
[14–17]. Therefore, the effectiveness of domain-speciﬁc psychological traits in stock
recommendations merits further investigation.

3 Method

The overview of our proposed model is presented in Fig. 1. The model comprises
four steps: (1) grouping individual investors based on speciﬁc criteria, which will be
discussed later; (2) measuring user similarity; (3) forming user neighborhoods based
on the similarity scores; and (4) predicting investors’ preferences and generating stock
recommendations. We also provide a notation list in Table 1 for clarity and consistency.
To group individual investors, we employed one of two methods: a clustering anal-
ysis based on psychological traits or an equal division based on the number of past
transactions. Speciﬁcally, we divided all investors I into ncluster groups using one of
these methods, which will be described in the fourth and ﬁfth experiments.

123

---

<!-- PAGE 5 -->

New Generation Computing (2024) 42:635–649

639

Table 1 Notation and symbols

Symbol

Meaning

I = {i1, i2, ...in}
(cid:2)
C j ⊂ I ,
SimT (u, v)

j C j = I

The set of all the investors
The set of investors in cluster C j
Similarity between investor u and investor v based on their

transaction data

Sim P(u, v)

Similarity between investor u and investor v based on their

Yuv = {a, b, ...}
rua
ru
Psy = {Psy1, Psy2, ...Psyl }

pi
u
pu
αu∈Ci
k

psychological traits

The set of stocks both stock u and stock v purchased
The preference of investor u to stock a

The mean of preference of investor u

The set of psychological traits including personality, behavioral

bias, cognitive ability, and purposes of investment

The value of u’s psychological variable i

The mean value of the psychological traits vector for investor u
The weight of SimT (u, v) of investor u in cluster Ci
The number of neighbors

n_cluster

The number of clusters

Fig. 1 Outline of our proposed recommendation model

{C1, C2, ...Cn_cluster} = DM(I )

(1)

where DM represents the method to divide investors such as the clustering algorithm.
Then, we computed the similarity between investors based on their transaction
data, general personality traits, and domain-speciﬁc psychological traits. First, we
measured the similarity based on transaction data (SimT ). SimT was computed using
the Pearson correlation coefﬁcient as in Eq. (2).

123

---

<!-- PAGE 6 -->

640

New Generation Computing (2024) 42:635–649

SimT (u, v) =

(cid:4)(cid:3)

(cid:3)

(rua − ru)(rva − rv)

a∈Yu,v
(rua − ru)2

(cid:4)(cid:3)

a∈Yuv

(rva − rv)2

a∈Yuv

(2)

where u and v are individual investors from set I , ru,a is the preference of u to a, ru
is the mean of preference of u, and Yu,v is the set of stocks both u and v purchased.
Likewise, we computed the similarity based on investors’ psychological traits

(Sim P). Sim P was computed using Pearson correlation coefﬁcient as in Eq. (3).

Sim P(u, v) =

(cid:4)(cid:3)

(cid:3)

( pi
u
− pu)2

i∈Psy
( pi
u

− pu)( pi
(cid:4)(cid:3)

i∈Psy

v − pv)

( pi

v − pv)2

i∈Psy

(3)

where Psy is the set of psychological traits, pi
u is the value of u’s psychological
variable i, and pu is the mean value of the psychological traits vector for investor
u. We computed similarity (Sim) based both on Sim P and SimT . Then, Sim was
computed using a weighted average of SimT and Sim P as in Eq. (4). αu∈Ci was
dependent on the cluster investor u belongs to, and computed as in Eq. (5).

Sim(u, v) = αu∈Ci SimT (u, v) + (1 − αu∈Ci

)Sim P(u, v)

αu∈Ci

= α∈[0,1] Scor eCi

(α)

(4)

(5)

where αu∈Ci is the weight of SimT for u, and Scor eCi shows the evaluation metrics
such as the F1 score of the performance of recommendation when the weight parameter
is α.

Third, the neighbors of target user x were set as in Eq. (6).

N (x, k) = {u ∈ I : |{v ∈ I : Sim(x, v) < Sim(x, u)}| < k}

(6)

where x is a target investor, k is the number of neighbors.

Finally, we predicted the preference score of each stock for the target investor
by aggregating the preference scores of their neighbors, weighted by the similarity
between the target investor and their neighbors. This was done using Eq. (7). Finally,
we recommended the top-n stocks with the highest preference scores to the target
investor.

(cid:3)

(cid:5)rxa = rx +

y∈Nx
(cid:3)

Sim(x, y)(ry,a − ry)
Sim(x, y)

y∈Nx

(7)

where (cid:5)rxa is the predicted preference score of x to a, rx is the average preference score
of x, and Nx represents the set of neighbors of x (Fig. 2).

123

---

<!-- PAGE 7 -->

New Generation Computing (2024) 42:635–649

641

Fig. 2 The details of the clustering analysis. Subﬁgure (a) shows the elbow method on personality traits.
Subﬁgure (b) shows the clustering analysis on personality traits using Kmeans and reduced the dimension
into 2d with t-SNE

4 Dataset

4.1 Data Acquisition

In our study, we collected data from a Japanese securities company, focusing on
individual investors who had made over 50 transactions in a year. We obtained
general personality traits and domain-speciﬁc psychological traits data along with
past transaction history from a total of 969 investors. The data range from July
2020 to September 2022. We collected various domain-speciﬁc psychological traits
from investors, including behavioral biases, cognitive ability, investment purposes,
and general personality traits. Personality traits were assessed using the ten-item
personality inventory (TIPI) [18, 19]. To ensure the validity of the questionnaire
domain-speciﬁc psychological traits, we referred to the Japan Household Panel Survey
(JHPS) questionnaire.1 We collected behavioral data including risk preference, time
discount, overconﬁdence, hyperbolic discounting, sign effect, and magnitude effect.
To measure cognitive ability, we assessed ﬁnancial literacy through a set of questions
regarding ﬁnancial knowledge and wealth management and administered a cognitive
reﬂection test to evaluate investors’ cognitive ability [20]. Furthermore, we inquired
about investors’ investment goals, including retirement, housing, education, medical
expenses, vacation, and other objectives.

We processed the transaction data into a user-item matrix given m users and n items.

Following the work in [4], we deﬁne m × n matrix U f with components

(U f )i j = f (i, j)

(8)

1 https://www.iser.osaka-u.ac.jp/survey_data/survey_eng.html.

123

---

<!-- PAGE 8 -->

642

New Generation Computing (2024) 42:635–649

Let qi, j,t be the portfolio of user i on stock j on the day t which is obtained from
transaction data.

(cid:6)

qi, j,t =

1 if user i holds stock j in time t
0 otherwise

We deﬁne implicit feedback collaborative ﬁltering user-item matrix R as U f R in
Eq. (10).

(cid:6)

f R(i, j) =

1 if there is t ∈ T s.t. qi, j,t (cid:4)= 0
0 otherwise

(9)

(10)

where T is an entire period. Simply speaking, rows of the R matrix represent, for user
i, whether they held stock j during any period.

4.2 Investor Behavior Analysis

Figure 3 presents the hierarchical clustering heatmap of investor behavioral traits. The
visualization reveals several noteworthy observations. For instance, in Fig. 3, neuroti-
cism exhibits lower correlations with openness and conscientiousness, while cognitive
ability demonstrates a higher correlation with ﬁnancial literacy. Furthermore, it high-
lights that investors with low risk aversion tend to exhibit high-risk tolerance, and that
annual income and investment experiences are strongly correlated. Additionally, Fig. 3
suggests that investors can be grouped into distinct clusters based on their behavioral
traits. The visual representations provide valuable insights into the interrelationships
among various investor characteristics.

5 Experiment

5.1 Tasks and Evaluation Metrics

We evaluate its ability to recommend relevant stocks to individual investors. Speciﬁ-
cally, we evaluated the model’s performance in two tasks: general stock recommen-
dation and new stock recommendation.

For the general stock recommendation task, we used test data that consisted of each
investor’s ﬁve most recent transactions to evaluate the model’s top 10 recommended
items. In the new stock recommendation task, we removed the transaction data of
stocks that each user had in the test data from the train data. The latter task is particularly
important in ﬁnancial stock recommendations, as investors tend to be biased towards
familiar stocks, rather than exploring new assets [21]. Therefore, it is crucial for stock
recommender systems to recommend new stocks to investors, which can help mitigate
familiarity bias and encourage exploration. We used precision@10, recall@10, and
F1 scores as evaluation metrics.

5.2 Experiments

We conducted ﬁve experiments to address the three research questions.

123

---

<!-- PAGE 9 -->

New Generation Computing (2024) 42:635–649

643

Fig. 3 Hierarchical clustering heatmap of investor traits: This heatmap illustrates the relationships among
investors based on their key traits. Each column represents a distinct investor, while each row corresponds
to a speciﬁc trait. The hierarchical clustering algorithm organizes investors with similar characteristics
together

To address RQ1, we conducted the ﬁrst experiment to investigate the impact of
investors’ personality traits on stock recommendations. We compared the perfor-
mance of a personality-based model, which uses the Big-Five personality traits, with a
transaction-based model and a random model. In the personality-based model, we set
ncluster to 1 and αu = 0 for all investors u ∈ I , while in the transaction-based model,
we set ncluster to 1 and αu = 1 for all investors u ∈ I .

To address RQ2, we conducted the second experiment to analyze the value of
domain-speciﬁc psychological traits in the personality-aware recommendation. We
conducted an ablation study for the combinations of general personality traits and
domain-speciﬁc psychological traits.

To address RQ3, we conducted three experiments to compare the performance
of existing methods with that of our proposed recommendation models. In the third

123

---

<!-- PAGE 10 -->

644

New Generation Computing (2024) 42:635–649

Table 2 Results for the ﬁrst, fourth, and ﬁfth experiment

Random model

General personality-based model

Transaction-based model

Cluster model

Division model

GSR
P@10

0.002

0.059

0.104

0.104
0.105

R@10

F1

0.007

0.176
0.329
0.324
0.329

0.003

0.088

0.158

0.157
0.159

NSR
P@10

0.001

0.040

0.050
0.058
0.058

R@10

F1

0.005

0.122
0.160
0.153

0.154

0.002

0.060

0.076

0.083
0.085

experiment, we implemented a weighted average model, which is a modiﬁcation of the
approach proposed by Ning et al. [22] that combines the two similarity metrics, Sim P
and SimT . Speciﬁcally, we varied the weight parameter αu from 0 to 1 to investigate
its impact on performance. In the fourth and ﬁfth experiments, we aimed to validate
the effectiveness of the proposed recommendation models. To determine the optimal
weight parameter αu∈Ci , we split the dataset into train, validation, and test sets. The
test and validation sets contained the most recent and next ﬁve transaction records for
each investor. We performed a grid search on the train and validation sets and used
the best parameter to evaluate performance on the test set. In the fourth experiment,
we clustered investors based on their psychological traits, hypothesizing that investors
with speciﬁc psychological traits would be better predicted by Sim P. We tuned the
weight parameter αu∈Ci for each cluster Ci and named this model the cluster model.
The number of clusters was determined to be nclusters = 8 using the elbow method
as shown in Fig. 2. In the ﬁfth experiment, we partitioned investors into equal groups
based on their number of past transactions, hypothesizing that investors with more
transaction data would be better predicted by SimT , while investors with limited
transaction data could be better predicted by Sim P. We tuned the weight parameter
αu∈Ci for each cluster Ci and named this model the division model.

5.3 Results

Table 2 presents the results of the ﬁrst, fourth, and ﬁfth experiments. The evalua-
tion metrics used are Precision@10 and Recall@10, denoted as P@10 and R@10,
respectively. GSR and NSR stand for general stock recommendations and new stock
recommendations, respectively. The results demonstrate that the general personality-
based model signiﬁcantly outperformed the random model in both settings.

The second experiment’s result is presented in Table 3. The table shows the per-
formance of the ablation study on the combinations of general personality traits and
domain-speciﬁc psychological traits. The results indicate that adding domain-speciﬁc
traits such as cognitive ability, behavioral bias, and purposes of investment improved
the performance in both general and new stock recommendation tasks. However,
adding more variables did not necessarily lead to higher performance, as the model
with all variables did not perform better than the models with a subset of variables.

123

---

<!-- PAGE 11 -->

New Generation Computing (2024) 42:635–649

645

Table 3 Results for the second experiment

Personality

Cognitive

Goal

Behavioral

Cognitive goal

Behavioral cognitive

Personality behavioral

Behavioral goal

Personality cognitive

Personality goal

Personality cognitive goal

Behavioral cognitive goal

Personality behavioral cognitive

Personality behavioral goal

Personality behavioral cognitive goal

GSR
P@10

0.059

0.055

0.056

0.059

0.057

0.054

0.058

0.059

0.059
0.061
0.058

0.059

0.057

0.058

0.059

R@10

F1

0.176

0.165

0.169

0.178

0.175

0.169

0.177

0.180

0.179
0.184
0.175

0.180

0.173

0.179

0.182

0.088

0.083

0.084

0.089

0.086

0.082

0.087

0.089

0.089
0.092
0.087

0.089

0.086

0.088

0.089

NSR
P@10

0.040

0.038

0.038

0.039

0.039

0.037

0.039

0.038

0.040

0.040

0.040

0.039

0.038
0.040
0.040

R@10

F1

0.122

0.117

0.118

0.124

0.120

0.118

0.122

0.122

0.126

0.124

0.123

0.124

0.120
0.130
0.129

0.060

0.057

0.057

0.059

0.059

0.056

0.059

0.058

0.061

0.060

0.060

0.059

0.058
0.061
0.061

Fig. 4 The results for the third experiment. a is the results with varying weight of SimT in General Stock
Recommendation and b is the result in New Stock Recommendation

The results of the third experiment, presented in Fig. 4, indicate that the performance
of the weighted average model mostly fell between the performance of the psychology-
based model and the transaction-based model. The results of the fourth experiment, as
shown in Table 2 suggest that the cluster model outperformed the transaction-based
model in the new stock recommendation task with regard to F1 score. Finally, the
results of the ﬁfth experiment, presented in Table 2 and Fig. 5, suggest that most of the
division models performed better than the transaction-based model in the new stock

123

---

<!-- PAGE 12 -->

646

New Generation Computing (2024) 42:635–649

Fig. 5 The comparison of the F1 score among the division model with the transaction-based model and the
cluster model. The x-axis shows ncluster

recommendation task, with the transaction-based model being outperformed only in
one setting when ncluster equaled 9 in the general stock recommendation task.

6 Discussion

For RQ1, we can conclude that the comparison between the random model and the
general personality-based model in Table 2 supports the value of general personal-
ity traits in stock recommendation tasks, which is consistent with previous ﬁndings
in other recommendation domains like music, book, and movie recommendation.
The personality-based model outperformed the random model by a signiﬁcant mar-
gin, demonstrating that personality traits can be leveraged for addressing cold start
problems in personalized stock recommendations. However, the performance of the
personality-based model was inferior to the transaction-based model, indicating that
personality traits should be used in conjunction with transaction data for optimal per-
formance in stock recommendation tasks where past transaction data is available for
each investor.

For RQ2, we can conclude that incorporating domain-speciﬁc psychological traits
in addition to general personality traits can improve recommendation performance,
as shown in Table 3. However, further investigation is required to identify the most
useful combinations of these variables for optimal recommendation performance. This
highlights the need for future research to carefully analyze and select the optimal
psychological variables for personalized recommendations.

To address RQ3, we carried out three experiments. The third experiment, presented
in Fig. 4, revealed that a simple weighted average of Sim P and SimT did not yield
better performance than the transaction-based model. This outcome suggested that it
is necessary to partition investors into groups with distinct characteristics to take full
advantage of general personality traits, domain-speciﬁc psychological traits, and trans-

123

---

<!-- PAGE 13 -->

New Generation Computing (2024) 42:635–649

647

action data. The fourth experiment, detailed in Table 2, demonstrated that our cluster
model outperformed the transaction-based model in the new stock recommendation
task, but not in the general stock recommendation. The usefulness of personality-aware
recommendation for enhancing the diversity of recommendations is well-documented
in literature [1, 2, 7]. Consequently, we consider that the diversity in the recommended
lists contributed to the improved performance of our new stock recommendation task,
which mandated the provision of diverse recommendations to enable investors to
explore new stocks. Moreover, we noted that speciﬁc clusters with characteristic psy-
chological traits were better predicted using Sim P than others, which needs further
investigation. Therefore, it is worthwhile to analyze the characteristics of clusters with
different performances. The superior performance of the transaction-based model in
general stock recommendation can be attributed to the repeat purchase behavior of
stocks, which is inﬂuenced by familiarity bias. This bias causes investors to repeatedly
purchase certain stocks, and as a result, the transaction-based model that learns directly
from past transactions performed better in providing general stock recommendations.
The results of the ﬁfth experiment show a similar pattern to that observed in the cluster
model. Speciﬁcally, the division model outperformed the transaction-based model in
most cases for the new stock recommendation task, while it only did so in one case for
the general stock recommendation is when the number of clusters was 9. In addition to
the diversity added to the recommendations, we argue that psychological traits play a
signiﬁcant role in enhancing the performance of the division model for investors with
limited transaction data. Figure 5 shows that the cluster model and the division model
outperformed the traditional transaction-based model in new stock recommendations.
Therefore, this result supports our hypothesis that dividing the investors into groups
with characteristics is essential in exploiting general personality traits, domain-speciﬁc
psychological traits, and transaction data.

To fully leverage the beneﬁts of dividing investors into groups with different char-
acteristics, it is essential to explore how investors in different groups are affected by
psychological traits. Future work should investigate the selection of psychological
traits and optimal weights at the cluster level to maximize the beneﬁts of personalized
recommendations.

7 Conclusion

In this paper, we examine personality-aware recommendations in the ﬁnancial domain.
Speciﬁcally, we conduct ﬁve experiments in ﬁnancial stock recommendation tasks with
Precision@10, Recall@10, and F1 scores as evaluation metrics. This paper reports
three ﬁndings. First, we show that general personality traits such as the Big-Five
personality traits are useful for domain-speciﬁc recommendations such as stock rec-
ommendations. Second, we show that utilizing domain-speciﬁc psychological traits
enhances the performance of the recommendation. Third, we show that our pro-
posed models that divide investors into groups with characteristics outperform the
transaction-based model, especially in the new stock recommendation task. While
this paper suggests the beneﬁts of incorporating domain-speciﬁc psychological traits
for recommendations and proposes a model to utilize all the data, careful analysis of

123

---

<!-- PAGE 14 -->

648

New Generation Computing (2024) 42:635–649

optimal selections of weights and psychological variables needs to be studied in future
work.

Acknowledgements This work was supported by the Japan Science and Technology-Future (JST-Mirai)
Program Grant Number JPMJMI20B1, Japan. Also, this work was supported by Daiwa Securities Group
Inc.

Funding Open Access funding provided by The University of Tokyo.

Declarations

Conﬂict of Interest The second author of this manuscript, Kiyoshi Izumi, is a lead guest editor for this
journal. This role is disclosed as per the journal’s policy.

Open Access This article is licensed under a Creative Commons Attribution 4.0 International License, which
permits use, sharing, adaptation, distribution and reproduction in any medium or format, as long as you give
appropriate credit to the original author(s) and the source, provide a link to the Creative Commons licence,
and indicate if changes were made. The images or other third party material in this article are included
in the article’s Creative Commons licence, unless indicated otherwise in a credit line to the material. If
material is not included in the article’s Creative Commons licence and your intended use is not permitted
by statutory regulation or exceeds the permitted use, you will need to obtain permission directly from the
copyright holder. To view a copy of this licence, visit http://creativecommons.org/licenses/by/4.0/.

References

1. Lex, E., Schedl, M.: Psychology-informed recommender systems tutorial. In: Proceedings of the 16th

ACM Conference on Recommender Systems, pp. 714–717 (2022)

2. Dhelim, S., Aung, N., Bouras, M.A., Ning, H., Cambria, E.: A survey on personality-aware recom-

mendation systems. Artif. Intell. Rev. 55(3), 2409–2454 (2022)

3. Ferwerda, B., Tkalcic, M., Schedl, M.: Personality traits and music genres: What do people prefer to

listen to? In: User Modeling, Adaptation and Personalization, pp. 285–288 (2017)

4. Swezey, R.M.E., Charron, B.: Large-scale recommendation for portfolio optimization. In: Proceedings

of the 12th ACM Conference on Recommender Systems, pp. 382–386 (2018)

5. McCrae, R.R., John, O.P.: An introduction to the ﬁve-factor model and its applications. J. Pers. 60(2),

175–215 (1992)

6. Wu, W., Chen, L.: Implicit acquisition of user personality for augmenting movie recommendations.

In: User Modeling, Adaptation and Personalization, pp. 302–314 (2015)

7. Wu, W., Chen, L., Zhao, Y.: Personalizing recommendation diversity based on user personality. User

Model. User-Adap. Inter. 28, 237–276 (2018)

8. Voditel, P., Deshpande, U.: A stock market portfolio recommender system based on association rule

mining. Appl. Soft Comput. 13, 1055–1063 (2013)

9. Yujun, Y., Jianping, L., Yimei, Y.: An efﬁcient stock recommendation model based on big order net

inﬂow. Math. Probl. Eng. 2016, 1–15 (2016)

10. Taghavi, M., Bakhtiyari, K., Scavino, E.: Agent-based computational investing recommender system.

In: Proceedings of the 7th ACM Conference on Recommender Systems, pp. 455–458 (2013)

11. Takayanagi, T., Chen, C.-C., Izumi, K.: Personalized dynamic recommender system for investors.
In: Proceedings of the 46th International ACM SIGIR Conference on Research and Development in
Information Retrieval, pp. 2246–2250 (2023)

12. Takayanagi, T., Izumi, K., Kato, A., Tsunedomi, N., Abe, Y.: Personalized stock recommendation with
investors’ attention and contextual information. In: Proceedings of the 46th International ACM SIGIR
Conference on Research and Development in Information Retrieval, pp. 3339–3343 (2023)

123

---

<!-- PAGE 15 -->

New Generation Computing (2024) 42:635–649

649

13. Takayanagi, T., Izumi, K.: Context-aware stock recommendations with stocks’ characteristics and
investors’ traits. IEICE Trans. Inf. Syst. E 106D, 1732–1741 (2023). https://doi.org/10.1587/transinf.
2023EDP7017

14. Oehler, A., Wendt, S., Wedlich, F., Horn, M.: Investors’ personality inﬂuences investment decisions:

experimental evidence on extraversion and neuroticism. J. Behav. Fin. 19(1), 30–48 (2018)

15. Tauni, M.Z., Fang, H.X., Rao, Z.-U.-R., Yousaf, S.: The inﬂuence of investor personality traits on
information acquisition and trading behavior: evidence from Chinese futures exchange. Pers. Individ.
Differ. 87, 248–255 (2015)

16. Grinbaltt, M., Keloharju, M., Linnainmaa, J.: Iq and stock market participation. J. Fin. 66(6), 2121–

2164 (2011)

17. Shefrin, H., Statman, M.: Behavioral portfolio theory. J. Fin. Quant. Anal. 35(2), 127–151 (2000)
18. Gosling, S.D., Rentfrow, P.J., Swann, W.B.: A very brief measure of the big-ﬁve personality domains.

J. Res. Pers. 37(6), 504–528 (2003)

19. Oshio, A., Abe, A., Cutrone, S., Samuel, P.G.: Big ﬁve content representation of the Japanese version

of the ten-item personality inventory. Psychology 4, 924–929 (2013)

20. Frederick, S.: Cognitive reﬂection and decision making. J. Econ. Perspect. 19(4), 25–42 (2005)
21. Huberman, G.: Familiarity breeds investment. Rev. Fin. Stud. 14(3), 659–680 (2015)
22. Ning, H., Dhelim, S., Aung, N.: Personet: friend recommendation system based on big-ﬁve personality

traits and hybrid ﬁltering. IEEE Trans. Comput. Soc. Syst. 6(3), 394–402 (2019)

Publisher’s Note Springer Nature remains neutral with regard to jurisdictional claims in published maps
and institutional afﬁliations.

123

<!-- MARKITDOWN CONVERSION -->

<!-- Full MarkItDown conversion for formatting fidelity. -->

NewGenerationComputing(2024)42:635–649
https://doi.org/10.1007/s00354-024-00241-w
IncorporatingDomain-SpecificTraitsinto
Personality-AwareRecommendationsforFinancial
Applications
Takehiro Takayanagi1 ·Kiyoshi Izumi1
Received:18August2023/Accepted:14November2023/Publishedonline:25February2024
©TheAuthor(s)2024
Abstract
The general personality traits, notably the Big-Five personality traits, have been
increasinglyintegratedintorecommendationsystems.Thepersonality-awarerecom-
mendations,whichincorporatehumanpersonalityintorecommendationsystems,have
shown promising results in general recommendation areas including music, movie,
ande-commercerecommendations.Ontheotherhand,thenumberofresearchdelving
intotheapplicabilityofpersonality-awarerecommendations inspecializeddomains
suchasfinanceandeducationremainslimited.Inaddition,thesedomainshaveunique
challenges in incorporating personality-aware recommendations as domain-specific
psychological traits such as risk tolerance and behavioral biases play a crucial role
inexplaininguserbehaviorinthesedomains.Addressingthesechallenges,thisstudy
addressesanin-depthexplorationofpersonality-awarerecommendationsinthefinan-
cialdomain,specificallywithinthecontextofstockrecommendations.First,thisstudy
investigatesthebenefitsofdeployinggeneralpersonalitytraitsinstockrecommenda-
tionsthroughtheintegrationofpersonality-awarerecommendationswithuser-based
collaborative filtering approaches. Second, this study further verifies whether incor-
porating domain-specific psychological traits along with general personality traits
enhances theperformanceofstockrecommender systems.Thirdly,thispaperintro-
duces a personalized stock recommendation model that incorporates both general
personalitytraitsanddomain-specificpsychologicaltraitsaswellastransactiondata.
Theexperimentalresultsshowthattheproposedmodeloutperformedbaselinemodels
infinancialstockrecommendations.
B
TakehiroTakayanagi
takayanagi-takehiro590@g.ecc.u-tokyo.ac.jp
KiyoshiIzumi
izumi@sys.t.u-tokyo.ac.jp
1 DepartmentofEngineering,TheUniversityofTokyo,Hongo7-3-1,Bunkyo-ku1138656,Tokyo,
Japan
123

636 NewGenerationComputing(2024)42:635–649
Keywords Stockrecommendation·Financialdatamining·Collaborativefiltering·
Behavioralfinance
1 Introduction
Inthecurrentdigitalera,usersarepresentedwithanoverwhelmingamountofonline
information and multiple sources of knowledge, which can lead to a phenomenon
known as information overload. Recommender systems represent a promising
approach to assist users in managing this challenge by suggesting items that match
their preferences. Personality is a core human characteristic that remains relatively
stableacrosstimeandissuitableformodelinguserbehavior,incontrasttoemotions
andmood,whichtendtobemoretransientandcontext-dependent.Incorporatingper-
sonalityintorecommendersystemscanimprovetheaccuracyofrecommendationsand
enhanceusersatisfactionbytailoringsuggestionstotheirindividualcharacteristics.
Personality traits have gained significant attention in recommender systems due
totheirpotentialtomitigatethecold-startproblemwhenwedonothaveaccesstoa
user’s interaction data, enhance recommendation diversity, and capture users’ com-
plexnature[1,2].Accordingly,recentstudieshavedemonstratedtheeffectivenessof
personality-awarerecommendation[1–3],whichemployspersonalitytraitstomake
recommendations,ingeneraldomainswithabundantopendatasuchasfilms,music,
andbooks.
While personality-aware recommendation systems have demonstrated success in
general domains where data is readily available, research on their applicability in
specific domains, such as finance, has been limited due to privacy concerns and the
requirement for domain expertise to produce precise recommendations [1, 4]. Con-
sequently, it is worthwhile to explore the potential usefulness of personality traits
in finance recommendation systems, as they may help address challenges such as
informationoverloadinthefinancialdomain.
In addition, it is important to note that domain-specific variables can have a sig-
nificant impact on decision-making processes, particularly in the domain of finance
whilepreviousstudiesonpersonality-awarerecommendationhavemainlyfocusedon
generalpersonalitytraits,suchastheBig-Fivepersonalitytraits[5].Forinstance,fac-
torssuchasrisktoleranceplayacriticalroleininvestmentdecision-making,butmay
not be as relevant in movie or music recommendations. Thus, it is essential to con-
siderdomain-specificvariableswhendevelopingpersonality-awarerecommendation
systems for finance to ensure that they accurately capture the unique characteristics
ofthisdomain.
Finally, personality-aware recommendation systems have primarily been used to
addressthecold-startprobleminrecommendation[1,3],buttheirpotentialtoenhance
existing recommendation models with transaction data remains underexplored [2].
Therefore,itisalsointriguingtoinvestigatewhetherincorporatinggeneralpersonality
traits and domain-specific psychological traits in non-cold start settings can lead to
improvedperformanceinrecommendationsystems.
Insummary,weformulatedthefollowingresearchquestions.
123

NewGenerationComputing(2024)42:635–649 637
1. RQ1:Cangeneralpersonalitytraitsbeusefulinstockrecommendationtasks?
2. RQ2: Do domain-specific psychological traits contribute to the performance of
stockrecommendations?
3. RQ3: How can we integrate investors’ general personality traits and domain-
specific psychological traits with their interaction history to enhance the stock
recommendationmodel?
Therestofthisworkbroadlycorrespondstotheresearchquestions.
2 RelatedWork
2.1 Personality-AwareRecommenderSystem
Personalitytraitshavebeenincreasinglyutilizedintheresearchofrecommendation
[1–3,6].Utilizingpersonalitytraitsforarecommendersystemhasthreeadvantages.
First,usingpersonalitytraitsfortherecommendersystemwillmitigatethecold-start
problem,especiallyfornewusersratherthanitems.Second,personalitytraitscanbe
used to increase recommendation diversity [7]. Third, personality traits help model
the complex nature of user behaviors. For example, personality traits are known to
be significantly correlated with users’ preferences in some areas such as music and
moviepreference[3,6].
Various theories in the literature of personality psychology have attempted to
describehumanpersonalitytraits.Amongothertheories,theFive-factormodel,also
known as the Big-Five personality traits theory is one of the most commonly used
models, where the human personality is characterized by five factors: Extraversion,
Opennesstoexperience,Conscientiousness,Agreeableness,andNeuroticism[5].
While five-factor models are widely used to measure the users’ similarity across
variousdomainsinpersonality-awarerecommendations,mostworksonlyutilizeper-
sonalitytraitstorepresentusers’psychologicaltraitsandignoreotherpsychological
effectswhichmightbeasimportantaspersonalitytraits[3,6].Thus,previousstud-
ieshavenotexploredthebenefitofincorporatingdomain-specificpsychologicaltraits
suchasbehavioralbiasesinfinanceintothepersonality-awarerecommendationmodel.
2.2 StockRecommendation
Thereisagrowingdemandforstockrecommendationsasthenumberofretailinvestors
using online brokers has been rapidly increasing. Accordingly, many studies have
tackled stock recommendation tasks. Stock recommendations can be classified into
two approaches: non-personalized stock recommendations and personalized stock
recommendations.Mostworksinstockrecommendationfallwithinthescopeofnon-
personalized recommendation, which focuses on identifying optimal strategies for
selectingstocksorportfoliosthatarelikelytobemoreprofitableinthefuture[8].On
theotherhand,littleresearchhasbeendoneonpersonalizedstockrecommendations
duetothelackofopendataanddifficultiesindatacollectionduetoprivacyconcerns
[4,9–13].Despitethelimitedliteratureonthesubject,somestudieshavetackledthe
123

638 NewGenerationComputing(2024)42:635–649
problemofpersonalizedstockrecommendations.Collaborativefilteringhasbeenused
forpersonalizedstockrecommendations,oftentimescombinedwithotherrecommen-
dationapproachessuchasorderbookanalysis,andmultiplecriteriadecisionanalysis
[4, 9, 10]. For instance, Robin et al. [4] estimate the investor’s risk tolerance from
users’ portfolios and recommends stock based on the relevance of the stock’s risk
returnwiththeuser’srisktolerancecombinedwithacollaborativefilteringmethod.
Themethodofpersonalizingstockrecommendationsbasedoninvestors’risktolerance
hastwoshortcomings.First,itsuffersfromthecold-startproblem.Second,itisnot
clearwhetheronevariable,risktolerance,cancapturethecomplexnatureofinvestors.
Therefore,thebenefitofpersonality-awarerecommendationswhichcanmitigatethe
cold-startproblemandhelpmodelusers’behaviorsneedstobeinvestigatedforstock
recommendations.
2.3 BehavioralFinance
The theory of modern economics is built on the assumption that human beings are
rationalagents.Theseagentsaimtomaximizetheirwealthandminimizerisk,care-
fully assessing the risk and return of investment choices to obtain a portfolio that
matchestheirriskaversion.However,empiricalstudiessuggestthattherealindivid-
ualinvestors’behaviorsaredifferentfromthoseoftheassumption.Theliteraturein
behavioralfinancehasshownthatpsychologicaltraitssuchasbehavioralbiases,per-
sonality,andcognitiveabilityaffectthefinancialbehaviorsofindividualinvestorsand
suggestedthatthesepsychologicaltraitsandbiasesareusefulinexplainingindividual
investors’ behavior. The relationships among investors’ traits—such as personality,
behavioral biases, cognitive ability, and investment goals—have been extensively
studied. This examination spans both empirical research in behavioral finance and
theoreticalstudies.Whileempiricalstudieshighlightthevalueofdomain-specificpsy-
chologicalfactors,includingbehavioralbiases,inexplainingandpredictinginvestor
behavior, their benefits remain unexplored in personality-aware recommendations
[14–17].Therefore,theeffectivenessofdomain-specificpsychologicaltraitsinstock
recommendationsmeritsfurtherinvestigation.
3 Method
TheoverviewofourproposedmodelispresentedinFig.1.Themodelcomprises
foursteps:(1)groupingindividualinvestorsbasedonspecificcriteria,whichwillbe
discussedlater;(2)measuringusersimilarity;(3)forminguserneighborhoodsbased
onthesimilarityscores;and(4)predictinginvestors’preferencesandgeneratingstock
recommendations.WealsoprovideanotationlistinTable1forclarityandconsistency.
Togroupindividualinvestors,weemployedoneoftwomethods:aclusteringanal-
ysis based on psychological traits or an equal division based on the number of past
transactions.Specifically,wedividedallinvestors I inton groupsusingoneof
cluster
thesemethods,whichwillbedescribedinthefourthandfifthexperiments.
123

NewGenerationComputing(2024)42:635–649 639
Table1 Notationandsymbols
| Symbol     |          | Meaning                      |
| ---------- | -------- | ---------------------------- |
| ={i1 ,i    | ,...in } |                              |
| I (cid:2)2 |          | Thesetofalltheinvestors      |
| Cj ⊂I,     | Cj =I    | ThesetofinvestorsinclusterCj |
j
| SimT(u,v) |     | Similaritybetweeninvestoruandinvestorvbasedontheir |
| --------- | --- | -------------------------------------------------- |
transactiondata
| SimP(u,v) |     | Similaritybetweeninvestoruandinvestorvbasedontheir |
| --------- | --- | -------------------------------------------------- |
psychologicaltraits
| Yuv={a,b,...} |     | Thesetofstocksbothstockuandstockvpurchased |
| ------------- | --- | ------------------------------------------ |
| rua           |     | Thepreferenceofinvestorutostocka           |
| ru            |     | Themeanofpreferenceofinvestoru             |
Psy={Psy1 ,Psy2 ,...Psyl } Thesetofpsychologicaltraitsincludingpersonality,behavioral
bias,cognitiveability,andpurposesofinvestment
i
| p u |     | Thevalueofu’spsychologicalvariablei                    |
| --- | --- | ------------------------------------------------------ |
| pu  |     | Themeanvalueofthepsychologicaltraitsvectorforinvestoru |
| α   |     | TheweightofSimT(u,v)ofinvestoruinclusterCi             |
u∈Ci
| k         |     | Thenumberofneighbors |
| --------- | --- | -------------------- |
| n_cluster |     | Thenumberofclusters  |
Fig.1 Outlineofourproposedrecommendationmodel
{C ,C ,...C }=DM(I)
1 2 n_cluster (1)
whereDMrepresentsthemethodtodivideinvestorssuchastheclusteringalgorithm.
Then, we computed the similarity between investors based on their transaction
data, general personality traits, and domain-specific psychological traits. First, we
measuredthesimilaritybasedontransactiondata(SimT).SimT wascomputedusing
thePearsoncorrelationcoefficientasinEq.(2).
123

| 640 |     |     |     | NewGenerationComputing(2024)42:635–649 |     |     |     |
| --- | --- | --- | --- | -------------------------------------- | --- | --- | --- |
(cid:3)
|     |            |     |                | (r −  | r )(rva   | −rv )       |     |
| --- | ---------- | --- | -------------- | ----- | --------- | ----------- | --- |
|     | SimT(u,v)= |     | (cid:4) a∈Yu,v | ua    | (cid:4) u |             |     |
|     |            |     | (cid:3)        |       | (cid:3)   |             | (2) |
|     |            |     | (r             | −r )2 |           | (rva −rv )2 |     |
|     |            |     | a∈Yuv ua       | u     | a∈Yuv     |             |     |
andv
whereu areindividualinvestorsfromset I,r u,a isthepreferenceofu toa,r u
isthemeanofpreferenceofu,andY u,v isthesetofstocksbothu andvpurchased.
Likewise, we computed the similarity based on investors’ psychological traits
(SimP).SimP wascomputedusingPearsoncorrelationcoefficientasinEq.(3).
(cid:3)
|     |            |     |               | (p i −   | p )(p i     | − pv )       |     |
| --- | ---------- | --- | ------------- | -------- | ----------- | ------------ | --- |
|     | SimP(u,v)= |     | (cid:4) i∈Psy | u        | (cid:4) u v |              |     |
|     |            |     | (cid:3)       |          | (cid:3)     |              | (3) |
|     |            |     | (p            | i − p )2 |             | (p i − pv )2 |     |
|     |            |     | i∈Psy         | u u      | i∈Psy       | v            |     |
where Psy is the set of psychological traits, pi is the value of u’s psychological
u
variable i, and p is the mean value of the psychological traits vector for investor
u
u. We computed similarity (Sim) based both on SimP and SimT. Then, Sim was
computed using a weighted average of SimT and SimP as in Eq.(4). α was
u∈Ci
dependentontheclusterinvestoru belongsto,andcomputedasinEq.(5).
|     | Sim(u,v)=α |      | SimT(u,v)+(1−α   |     |      | )SimP(u,v) |     |
| --- | ---------- | ---- | ---------------- | --- | ---- | ---------- | --- |
|     |            | u∈Ci |                  |     | u∈Ci |            | (4) |
|     |            |      | α = α∈[0,1]Score |     | (α)  |            | (5) |
|     |            |      | u∈Ci             |     | Ci   |            |     |
whereα istheweightof SimT foru,and Score showstheevaluationmetrics
|     | u∈Ci |     |     |     | Ci  |     |     |
| --- | ---- | --- | --- | --- | --- | --- | --- |
suchastheF1scoreoftheperformanceofrecommendationwhentheweightparameter
isα.
| Third,theneighborsoftargetuserx |                     |     | weresetasinEq.(6).      |           |               |     |     |
| ------------------------------- | ------------------- | --- | ----------------------- | --------- | ------------- | --- | --- |
|                                 | N(x,k)={u           | ∈   | :|{v ∈ :                | Sim(x,v)< | Sim(x,u)}|<k} |     |     |
|                                 |                     |     | I I                     |           |               |     | (6) |
| wherex                          | isatargetinvestor,k |     | isthenumberofneighbors. |           |               |     |     |
Finally, we predicted the preference score of each stock for the target investor
by aggregating the preference scores of their neighbors, weighted by the similarity
betweenthetargetinvestorandtheirneighbors.ThiswasdoneusingEq.(7).Finally,
we recommended the top-n stocks with the highest preference scores to the target
| investor. |     |             | (cid:3)     |            |     |     |     |
| --------- | --- | ----------- | ----------- | ---------- | --- | --- | --- |
|           |     |             |             | Sim(x,y)(r | −r  | )   |     |
|           |     |             | y∈N(cid:3)x |            | y,a | y   |     |
|           |     | r(cid:5) =r | +           |            |     |     | (7) |
|           |     | xa          | x           | Sim(x,y)   |     |     |     |
y∈Nx
wherer(cid:5)isthepredictedpreferencescoreofxtoa,r
|         | xa                               |     |     |          | x istheaveragepreferencescore |     |     |
| ------- | -------------------------------- | --- | --- | -------- | ----------------------------- | --- | --- |
| ofx,and | N representsthesetofneighborsofx |     |     | (Fig.2). |                               |     |     |
x
123

NewGenerationComputing(2024)42:635–649 641
Fig.2 Thedetailsoftheclusteringanalysis.Subfigure(a)showstheelbowmethodonpersonalitytraits.
Subfigure(b)showstheclusteringanalysisonpersonalitytraitsusingKmeansandreducedthedimension
into2dwitht-SNE
4 Dataset
4.1 DataAcquisition
In our study, we collected data from a Japanese securities company, focusing on
individual investors who had made over 50 transactions in a year. We obtained
general personality traits and domain-specific psychological traits data along with
past transaction history from a total of 969 investors. The data range from July
2020 to September 2022. We collected various domain-specific psychological traits
from investors, including behavioral biases, cognitive ability, investment purposes,
and general personality traits. Personality traits were assessed using the ten-item
personality inventory (TIPI) [18, 19]. To ensure the validity of the questionnaire
domain-specificpsychologicaltraits,wereferredtotheJapanHouseholdPanelSurvey
(JHPS)questionnaire.1 Wecollectedbehavioraldataincludingriskpreference,time
discount,overconfidence,hyperbolicdiscounting,signeffect,andmagnitudeeffect.
Tomeasurecognitiveability,weassessedfinancialliteracythroughasetofquestions
regardingfinancialknowledgeandwealthmanagementandadministeredacognitive
reflectiontesttoevaluateinvestors’cognitiveability[20].Furthermore,weinquired
aboutinvestors’investmentgoals,includingretirement,housing,education,medical
expenses,vacation,andotherobjectives.
Weprocessedthetransactiondataintoauser-itemmatrixgivenmusersandnitems.
Followingtheworkin[4],wedefinem×nmatrixU withcomponents
f
(U ) = f(i, j) (8)
f ij
1 https://www.iser.osaka-u.ac.jp/survey_data/survey_eng.html.
123

642 NewGenerationComputing(2024)42:635–649
Let q i,j,t be the portfolio of user i on stock j on the day t which is obtained from
transactiondata. (cid:6)
1 ifuseri holdsstock j intimet
q i,j,t =
0 otherwise
(9)
We define implicit feedback collaborative filtering user-item matrix R as U in
fR
Eq.(10). (cid:6)
f (i, j)= 1 ifthereist ∈Ts.t.q i,j,t (cid:4)=0 (10)
R 0 otherwise
whereT isanentireperiod.Simplyspeaking,rowsoftheRmatrixrepresent,foruser
i,whethertheyheldstock j duringanyperiod.
4.2 InvestorBehaviorAnalysis
Figure3presentsthehierarchicalclusteringheatmapofinvestorbehavioraltraits.The
visualizationrevealsseveralnoteworthyobservations.Forinstance,inFig.3,neuroti-
cismexhibitslowercorrelationswithopennessandconscientiousness,whilecognitive
abilitydemonstratesahighercorrelationwithfinancialliteracy.Furthermore,ithigh-
lightsthatinvestorswithlowriskaversiontendtoexhibithigh-risktolerance,andthat
annualincomeandinvestmentexperiencesarestronglycorrelated.Additionally,Fig.3
suggeststhatinvestorscanbegroupedintodistinctclustersbasedontheirbehavioral
traits.Thevisualrepresentationsprovidevaluableinsightsintotheinterrelationships
amongvariousinvestorcharacteristics.
5 Experiment
5.1 TasksandEvaluationMetrics
Weevaluateitsabilitytorecommendrelevantstockstoindividualinvestors.Specifi-
cally,weevaluatedthemodel’sperformanceintwotasks:generalstockrecommen-
dationandnewstockrecommendation.
Forthegeneralstockrecommendationtask,weusedtestdatathatconsistedofeach
investor’sfivemostrecenttransactionstoevaluatethemodel’stop10recommended
items. In the new stock recommendation task, we removed the transaction data of
stocksthateachuserhadinthetestdatafromthetraindata.Thelattertaskisparticularly
importantinfinancialstockrecommendations,asinvestorstendtobebiasedtowards
familiarstocks,ratherthanexploringnewassets[21].Therefore,itiscrucialforstock
recommendersystemstorecommendnewstockstoinvestors,whichcanhelpmitigate
familiarity bias and encourage exploration. We used precision@10, recall@10, and
F1scoresasevaluationmetrics.
5.2 Experiments
Weconductedfiveexperimentstoaddressthethreeresearchquestions.
123

NewGenerationComputing(2024)42:635–649 643
Fig.3 Hierarchicalclusteringheatmapofinvestortraits:Thisheatmapillustratestherelationshipsamong
investorsbasedontheirkeytraits.Eachcolumnrepresentsadistinctinvestor,whileeachrowcorresponds
toaspecifictrait.Thehierarchicalclusteringalgorithmorganizesinvestorswithsimilarcharacteristics
together
To address RQ1, we conducted the first experiment to investigate the impact of
investors’ personality traits on stock recommendations. We compared the perfor-
manceofapersonality-basedmodel,whichusestheBig-Fivepersonalitytraits,witha
transaction-basedmodelandarandommodel.Inthepersonality-basedmodel,weset
n to1andα =0forallinvestorsu ∈ I,whileinthetransaction-basedmodel,
cluster u
wesetn to1andα =1forallinvestorsu ∈ I.
cluster u
To address RQ2, we conducted the second experiment to analyze the value of
domain-specific psychological traits in the personality-aware recommendation. We
conducted an ablation study for the combinations of general personality traits and
domain-specificpsychologicaltraits.
To address RQ3, we conducted three experiments to compare the performance
ofexistingmethodswiththatofourproposedrecommendationmodels.Inthethird
123

| 644 |     | NewGenerationComputing(2024)42:635–649 |     |     |
| --- | --- | -------------------------------------- | --- | --- |
Table2 Resultsforthefirst,fourth,andfifthexperiment
|             | GSR         |       | NSR         |       |
| ----------- | ----------- | ----- | ----------- | ----- |
|             | P@10 R@10   | F1    | P@10 R@10   | F1    |
| Randommodel | 0.002 0.007 | 0.003 | 0.001 0.005 | 0.002 |
Generalpersonality-basedmodel 0.059 0.176 0.088 0.040 0.122 0.060
|                        | 0.329       |       | 0.160       |       |
| ---------------------- | ----------- | ----- | ----------- | ----- |
| Transaction-basedmodel | 0.104       | 0.158 | 0.050       | 0.076 |
| Clustermodel           | 0.104 0.324 | 0.157 | 0.058 0.153 | 0.083 |
|                        | 0.105 0.329 | 0.159 | 0.058       | 0.085 |
| Divisionmodel          |             |       | 0.154       |       |
experiment,weimplementedaweightedaveragemodel,whichisamodificationofthe
approachproposedbyNingetal.[22]thatcombinesthetwosimilaritymetrics,SimP
andSimT.Specifically,wevariedtheweightparameterα
|     |     |     | u from0to1toinvestigate |     |
| --- | --- | --- | ----------------------- | --- |
itsimpactonperformance.Inthefourthandfifthexperiments,weaimedtovalidate
theeffectivenessoftheproposedrecommendationmodels.Todeterminetheoptimal
weightparameterα
u∈Ci ,wesplitthedatasetintotrain,validation,andtestsets.The
testandvalidationsetscontainedthemostrecentandnextfivetransactionrecordsfor
each investor. We performed a grid search on the train and validation sets and used
thebestparametertoevaluateperformanceonthetestset.Inthefourthexperiment,
weclusteredinvestorsbasedontheirpsychologicaltraits,hypothesizingthatinvestors
withspecificpsychologicaltraitswouldbebetterpredictedby SimP.Wetunedthe
weightparameterα foreachclusterC andnamedthismodeltheclustermodel.
u∈Ci i
=
The number of clusters was determined to be n clusters 8 using the elbow method
asshowninFig.2.Inthefifthexperiment,wepartitionedinvestorsintoequalgroups
based on their number of past transactions, hypothesizing that investors with more
transaction data would be better predicted by SimT, while investors with limited
transactiondatacouldbebetterpredictedby SimP.Wetunedtheweightparameter
α
| u∈Ci foreachclusterC i | andnamedthismodelthedivisionmodel. |     |     |     |
| ---------------------- | ---------------------------------- | --- | --- | --- |
5.3 Results
Table 2 presents the results of the first, fourth, and fifth experiments. The evalua-
tion metrics used are Precision@10 and Recall@10, denoted as P@10 and R@10,
respectively.GSRandNSRstandforgeneralstockrecommendationsandnewstock
recommendations,respectively.Theresultsdemonstratethatthegeneralpersonality-
basedmodelsignificantlyoutperformedtherandommodelinbothsettings.
The second experiment’s result is presented in Table 3. The table shows the per-
formanceoftheablationstudyonthecombinationsofgeneralpersonalitytraitsand
domain-specificpsychologicaltraits.Theresultsindicatethataddingdomain-specific
traitssuchascognitiveability,behavioralbias,andpurposesofinvestmentimproved
the performance in both general and new stock recommendation tasks. However,
adding more variables did not necessarily lead to higher performance, as the model
withallvariablesdidnotperformbetterthanthemodelswithasubsetofvariables.
123

NewGenerationComputing(2024)42:635–649 645
Table3 Resultsforthesecondexperiment
|                          | GSR         | NSR         |             |
| ------------------------ | ----------- | ----------- | ----------- |
|                          | P@10 R@10   | F1 P@10     | R@10 F1     |
| Personality              | 0.059 0.176 | 0.088 0.040 | 0.122 0.060 |
| Cognitive                | 0.055 0.165 | 0.083 0.038 | 0.117 0.057 |
| Goal                     | 0.056 0.169 | 0.084 0.038 | 0.118 0.057 |
| Behavioral               | 0.059 0.178 | 0.089 0.039 | 0.124 0.059 |
| Cognitivegoal            | 0.057 0.175 | 0.086 0.039 | 0.120 0.059 |
| Behavioralcognitive      | 0.054 0.169 | 0.082 0.037 | 0.118 0.056 |
| Personalitybehavioral    | 0.058 0.177 | 0.087 0.039 | 0.122 0.059 |
| Behavioralgoal           | 0.059 0.180 | 0.089 0.038 | 0.122 0.058 |
| Personalitycognitive     | 0.059 0.179 | 0.089 0.040 | 0.126 0.061 |
| Personalitygoal          | 0.061 0.184 | 0.092 0.040 | 0.124 0.060 |
| Personalitycognitivegoal | 0.058 0.175 | 0.087 0.040 | 0.123 0.060 |
| Behavioralcognitivegoal  | 0.059 0.180 | 0.089 0.039 | 0.124 0.059 |
Personalitybehavioralcognitive 0.057 0.173 0.086 0.038 0.120 0.058
Personalitybehavioralgoal 0.058 0.179 0.088 0.040 0.130 0.061
Personalitybehavioralcognitivegoal 0.059 0.182 0.089 0.040 0.129 0.061
Fig.4 Theresultsforthethirdexperiment.aistheresultswithvaryingweightofSimTinGeneralStock
RecommendationandbistheresultinNewStockRecommendation
Theresultsofthethirdexperiment,presentedinFig.4,indicatethattheperformance
oftheweightedaveragemodelmostlyfellbetweentheperformanceofthepsychology-
basedmodelandthetransaction-basedmodel.Theresultsofthefourthexperiment,as
showninTable2suggestthattheclustermodeloutperformedthetransaction-based
model in the new stock recommendation task with regard to F1 score. Finally, the
resultsofthefifthexperiment,presentedinTable2andFig.5,suggestthatmostofthe
divisionmodelsperformedbetterthanthetransaction-basedmodelinthenewstock
123

646 NewGenerationComputing(2024)42:635–649
Fig.5 ThecomparisonoftheF1scoreamongthedivisionmodelwiththetransaction-basedmodelandthe
clustermodel.Thex-axisshowsncluster
recommendationtask,withthetransaction-basedmodelbeingoutperformedonlyin
onesettingwhenn equaled9inthegeneralstockrecommendationtask.
cluster
6 Discussion
For RQ1, we can conclude that the comparison between the random model and the
general personality-based model in Table 2 supports the value of general personal-
ity traits in stock recommendation tasks, which is consistent with previous findings
in other recommendation domains like music, book, and movie recommendation.
The personality-based model outperformed the random model by a significant mar-
gin, demonstrating that personality traits can be leveraged for addressing cold start
problemsinpersonalized stockrecommendations. However, theperformance ofthe
personality-basedmodelwasinferiortothetransaction-basedmodel,indicatingthat
personalitytraitsshouldbeusedinconjunctionwithtransactiondataforoptimalper-
formanceinstockrecommendationtaskswherepasttransactiondataisavailablefor
eachinvestor.
ForRQ2,wecanconcludethatincorporatingdomain-specificpsychologicaltraits
in addition to general personality traits can improve recommendation performance,
as shown in Table 3. However, further investigation is required to identify the most
usefulcombinationsofthesevariablesforoptimalrecommendationperformance.This
highlights the need for future research to carefully analyze and select the optimal
psychologicalvariablesforpersonalizedrecommendations.
ToaddressRQ3,wecarriedoutthreeexperiments.Thethirdexperiment,presented
inFig.4,revealedthatasimpleweightedaverageof SimP and SimT didnotyield
betterperformancethanthetransaction-basedmodel.Thisoutcomesuggestedthatit
isnecessarytopartitioninvestorsintogroupswithdistinctcharacteristicstotakefull
advantageofgeneralpersonalitytraits,domain-specificpsychologicaltraits,andtrans-
123

NewGenerationComputing(2024)42:635–649 647
actiondata.Thefourthexperiment,detailedinTable2,demonstratedthatourcluster
model outperformed the transaction-based model in the new stock recommendation
task,butnotinthegeneralstockrecommendation.Theusefulnessofpersonality-aware
recommendationforenhancingthediversityofrecommendationsiswell-documented
inliterature[1,2,7].Consequently,weconsiderthatthediversityintherecommended
listscontributedtotheimprovedperformanceofournewstockrecommendationtask,
which mandated the provision of diverse recommendations to enable investors to
explorenewstocks.Moreover,wenotedthatspecificclusterswithcharacteristicpsy-
chologicaltraitswerebetterpredictedusing SimP thanothers,whichneedsfurther
investigation.Therefore,itisworthwhiletoanalyzethecharacteristicsofclusterswith
differentperformances.Thesuperiorperformanceofthetransaction-basedmodelin
general stock recommendation can be attributed to the repeat purchase behavior of
stocks,whichisinfluencedbyfamiliaritybias.Thisbiascausesinvestorstorepeatedly
purchasecertainstocks,andasaresult,thetransaction-basedmodelthatlearnsdirectly
frompasttransactionsperformedbetterinprovidinggeneralstockrecommendations.
Theresultsofthefifthexperimentshowasimilarpatterntothatobservedinthecluster
model.Specifically,thedivisionmodeloutperformedthetransaction-basedmodelin
mostcasesforthenewstockrecommendationtask,whileitonlydidsoinonecasefor
thegeneralstockrecommendationiswhenthenumberofclusterswas9.Inadditionto
thediversityaddedtotherecommendations,wearguethatpsychologicaltraitsplaya
significantroleinenhancingtheperformanceofthedivisionmodelforinvestorswith
limitedtransactiondata.Figure5showsthattheclustermodelandthedivisionmodel
outperformedthetraditionaltransaction-basedmodelinnewstockrecommendations.
Therefore,thisresultsupportsourhypothesisthatdividingtheinvestorsintogroups
withcharacteristicsisessentialinexploitinggeneralpersonalitytraits,domain-specific
psychologicaltraits,andtransactiondata.
Tofullyleveragethebenefitsofdividinginvestorsintogroupswithdifferentchar-
acteristics,itisessentialtoexplorehowinvestorsindifferentgroupsareaffectedby
psychological traits. Future work should investigate the selection of psychological
traitsandoptimalweightsattheclusterleveltomaximizethebenefitsofpersonalized
recommendations.
7 Conclusion
Inthispaper,weexaminepersonality-awarerecommendationsinthefinancialdomain.
Specifically,weconductfiveexperimentsinfinancialstockrecommendationtaskswith
Precision@10, Recall@10, and F1 scores as evaluation metrics. This paper reports
three findings. First, we show that general personality traits such as the Big-Five
personalitytraitsareusefulfordomain-specificrecommendationssuchasstockrec-
ommendations. Second, we show that utilizing domain-specific psychological traits
enhances the performance of the recommendation. Third, we show that our pro-
posed models that divide investors into groups with characteristics outperform the
transaction-based model, especially in the new stock recommendation task. While
thispapersuggeststhebenefitsofincorporatingdomain-specificpsychologicaltraits
forrecommendationsandproposesamodeltoutilizeallthedata,carefulanalysisof
123

648 NewGenerationComputing(2024)42:635–649
optimalselectionsofweightsandpsychologicalvariablesneedstobestudiedinfuture
work.
Acknowledgements ThisworkwassupportedbytheJapanScienceandTechnology-Future(JST-Mirai)
ProgramGrantNumberJPMJMI20B1,Japan.Also,thisworkwassupportedbyDaiwaSecuritiesGroup
Inc.
Funding OpenAccessfundingprovidedbyTheUniversityofTokyo.
Declarations
ConflictofInterest Thesecondauthorofthismanuscript,KiyoshiIzumi,isaleadguesteditorforthis
journal.Thisroleisdisclosedasperthejournal’spolicy.
OpenAccess ThisarticleislicensedunderaCreativeCommonsAttribution4.0InternationalLicense,which
permitsuse,sharing,adaptation,distributionandreproductioninanymediumorformat,aslongasyougive
appropriatecredittotheoriginalauthor(s)andthesource,providealinktotheCreativeCommonslicence,
andindicateifchangesweremade.Theimagesorotherthirdpartymaterialinthisarticleareincluded
inthearticle’sCreativeCommonslicence,unlessindicatedotherwiseinacreditlinetothematerial.If
materialisnotincludedinthearticle’sCreativeCommonslicenceandyourintendeduseisnotpermitted
bystatutoryregulationorexceedsthepermitteduse,youwillneedtoobtainpermissiondirectlyfromthe
copyrightholder.Toviewacopyofthislicence,visithttp://creativecommons.org/licenses/by/4.0/.
References
1. Lex,E.,Schedl,M.:Psychology-informedrecommendersystemstutorial.In:Proceedingsofthe16th
ACMConferenceonRecommenderSystems,pp.714–717(2022)
2. Dhelim,S.,Aung,N.,Bouras,M.A.,Ning,H.,Cambria,E.:Asurveyonpersonality-awarerecom-
mendationsystems.Artif.Intell.Rev.55(3),2409–2454(2022)
3. Ferwerda,B.,Tkalcic,M.,Schedl,M.:Personalitytraitsandmusicgenres:Whatdopeoplepreferto
listento?In:UserModeling,AdaptationandPersonalization,pp.285–288(2017)
4. Swezey,R.M.E.,Charron,B.:Large-scalerecommendationforportfoliooptimization.In:Proceedings
ofthe12thACMConferenceonRecommenderSystems,pp.382–386(2018)
5. McCrae,R.R.,John,O.P.:Anintroductiontothefive-factormodelanditsapplications.J.Pers.60(2),
175–215(1992)
6. Wu,W.,Chen,L.:Implicitacquisitionofuserpersonalityforaugmentingmovierecommendations.
In:UserModeling,AdaptationandPersonalization,pp.302–314(2015)
7. Wu,W.,Chen,L.,Zhao,Y.:Personalizingrecommendationdiversitybasedonuserpersonality.User
Model.User-Adap.Inter.28,237–276(2018)
8. Voditel,P.,Deshpande,U.:Astockmarketportfoliorecommendersystembasedonassociationrule
mining.Appl.SoftComput.13,1055–1063(2013)
9. Yujun,Y.,Jianping,L.,Yimei,Y.:Anefficientstockrecommendationmodelbasedonbigordernet
inflow.Math.Probl.Eng.2016,1–15(2016)
10. Taghavi,M.,Bakhtiyari,K.,Scavino,E.:Agent-basedcomputationalinvestingrecommendersystem.
In:Proceedingsofthe7thACMConferenceonRecommenderSystems,pp.455–458(2013)
11. Takayanagi,T.,Chen,C.-C.,Izumi,K.:Personalizeddynamicrecommendersystemforinvestors.
In:Proceedingsofthe46thInternationalACMSIGIRConferenceonResearchandDevelopmentin
InformationRetrieval,pp.2246–2250(2023)
12. Takayanagi,T.,Izumi,K.,Kato,A.,Tsunedomi,N.,Abe,Y.:Personalizedstockrecommendationwith
investors’attentionandcontextualinformation.In:Proceedingsofthe46thInternationalACMSIGIR
ConferenceonResearchandDevelopmentinInformationRetrieval,pp.3339–3343(2023)
123

NewGenerationComputing(2024)42:635–649 649
13. Takayanagi, T., Izumi, K.: Context-aware stock recommendations with stocks’ characteristics and
investors’traits.IEICETrans.Inf.Syst.E106D,1732–1741(2023).https://doi.org/10.1587/transinf.
2023EDP7017
14. Oehler,A.,Wendt,S.,Wedlich,F.,Horn,M.:Investors’personalityinfluencesinvestmentdecisions:
experimentalevidenceonextraversionandneuroticism.J.Behav.Fin.19(1),30–48(2018)
15. Tauni,M.Z.,Fang,H.X.,Rao,Z.-U.-R.,Yousaf,S.:Theinfluenceofinvestorpersonalitytraitson
informationacquisitionandtradingbehavior:evidencefromChinesefuturesexchange.Pers.Individ.
Differ.87,248–255(2015)
16. Grinbaltt,M.,Keloharju,M.,Linnainmaa,J.:Iqandstockmarketparticipation.J.Fin.66(6),2121–
2164(2011)
17. Shefrin,H.,Statman,M.:Behavioralportfoliotheory.J.Fin.Quant.Anal.35(2),127–151(2000)
18. Gosling,S.D.,Rentfrow,P.J.,Swann,W.B.:Averybriefmeasureofthebig-fivepersonalitydomains.
J.Res.Pers.37(6),504–528(2003)
19. Oshio,A.,Abe,A.,Cutrone,S.,Samuel,P.G.:BigfivecontentrepresentationoftheJapaneseversion
oftheten-itempersonalityinventory.Psychology4,924–929(2013)
20. Frederick,S.:Cognitivereflectionanddecisionmaking.J.Econ.Perspect.19(4),25–42(2005)
21. Huberman,G.:Familiaritybreedsinvestment.Rev.Fin.Stud.14(3),659–680(2015)
22. Ning,H.,Dhelim,S.,Aung,N.:Personet:friendrecommendationsystembasedonbig-fivepersonality
traitsandhybridfiltering.IEEETrans.Comput.Soc.Syst.6(3),394–402(2019)
Publisher’sNote SpringerNatureremainsneutralwithregardtojurisdictionalclaimsinpublishedmaps
andinstitutionalaffiliations.
123