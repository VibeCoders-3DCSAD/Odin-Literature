---
conversion_metadata:
  converted_at: "2026-07-22T12:38:21Z"
  converter_tool: "markitdown"
  converter_version: "0.1.6"
  source_pdf: "Caroprese et al.pdf"
  source_pdf_sha256: "9350e518335b22121e3f1c49b5e67839103fe5cf721e8009696a59da3c11b206"
  page_count: 28
  markdown_char_count: 170441
---

<!-- PAGE-AWARE EXTRACTION (via pdfminer.six) -->

<!-- PAGE 1 -->

Modelling Concept Drift in Dynamic Data Streams for
Recommender Systems

LUCIANO CAROPRESE, University Gabriele d’Annunzio of Chieti and Pescara, Department of Engi-
neering and Geosciences, Pescara, Italy and ICAR-CNR, Rende, Italy
FRANCESCO SERGIO PISANI, ICAR-CNR, Rende, Italy
BRUNO MIGUEL VELOSO, Universidade Portucalense, Porto, Portugal and INESC TEC, Porto, Portu-
gal
MATTHIAS KONIG, Leiden University, Leiden, Netherlands
GIUSEPPE MANCO, ICAR-CNR, Rende, Italy
HOLGER HOOS, Leiden University, Leiden, Netherlands and The University of British Columbia, Van-
couver, Canada
JOAO GAMA, Universidade Portucalense, Porto, Portugal and INESC TEC, Porto, Portugal

Recommendation systems play a crucial role in modern e-commerce and streaming services. However, the
limited availability of public datasets hampers the rapid development of more efficient and accurate recom-
mendation algorithms within the research community. This work introduces a stream-based data generator
designed to generate user preferences for a set of items while accommodating progressive changes in user
preferences. The underlying principle involves using user/item embeddings to derive preferences by explor-
ing the proximity of these embeddings. Whether randomly generated or learned from a real finite data stream,
these embeddings serve as the basis for generating new preferences. We investigate how this fundamental
model can adapt to shifts in user behavior over time; in our framework, changes correspond to alterations
in the structure of the tripartite graph, reflecting modifications in the underlying embeddings. Through an
analysis of real-life data streams, we demonstrate that the proposed model is effective in capturing actual
preferences and the changes that they can exhibit over time. Thus, we characterize these changes and de-
velop a generalized method capable of simulating realistic data, thereby generating streams with similar yet
controllable drift dynamics.
CCS Concepts: • Information systems → Retrieval models and ranking;

This work was partially supported by Project “SERICS - SEcurity and RIghts In the CyberSpace” (PE00000014) and partially
by the EU H2020 ICT48 project “HumanE-AI-Net” under contract #952026.
Authors’ Contact Information: Luciano Caroprese, University Gabriele d’Annunzio of Chieti and Pescara, Department
of Engineering and Geosciences, Pescara, Italy and ICAR-CNR, Rende, Calabria, Italy; e-mail: luciano.caroprese@unich.it;
Francesco Sergio Pisani, ICAR-CNR, Rende, Calabria, Italy; e-mail: francescosergio.pisani@icar.cnr.it; Bruno Miguel Veloso,
Universidade Portucalense, Porto, Portugal and INESC TEC, Porto, Portugal; e-mail: bveloso@fep.up.pt; Matthias Konig,
Leiden University, Leiden, Netherlands; e-mail: h.m.t.konig@liacs.leidenuniv.nl; Giuseppe Manco, ICAR-CNR, Rende, Cal-
abria, Italy; e-mail: giuseppe.manco@icar.cnr.it; Holger Hoos, Leiden University, Leiden, Netherlands and The University
of British Columbia, Vancouver, British Columbia, Canada; e-mail: h.h.hoos@liacs.leidenuniv.nl; Joao Gama, Universidade
Portucalense, Porto, Portugal and INESC TEC, Porto, Portugal; e-mail: jgama@fep.up.pt.

This work is licensed under a Creative Commons Attribution International 4.0 License.

© 2025 Copyright held by the owner/author(s).
ACM 2770-6699/2025/03-ART24
https://doi.org/10.1145/3707693

ACM Trans. Recomm. Syst., Vol. 3, No. 2, Article 24. Publication date: March 2025.

---

<!-- PAGE 2 -->

24:2

L. Caroprese et al.

Additional Key Words and Phrases: Recommender systems, collaborative filtering, concept drift adaptation,
data generation

ACM Reference Format:
Luciano Caroprese, Francesco Sergio Pisani, Bruno Miguel Veloso, Matthias Konig, Giuseppe Manco, Holger
Hoos, and Joao Gama. 2025. Modelling Concept Drift in Dynamic Data Streams for Recommender Systems.
ACM Trans. Recomm. Syst. 3, 2, Article 24 (March 2025), 28 pages. https://doi.org/10.1145/3707693

1 Introduction
Modern machine learning applications and systems need to deal with large amounts of continuous
data in the form of data streams. Most real-life application scenarios require the analysis of large
volumes of data whose properties or distribution can change and evolve. Notable examples
are e-commerce and streaming platforms, which contain catalogs counting thousands or even
millions of products or items, where user preferences and purchasing/adoption behavior can
evolve over time according to changes in the catalog. Data Stream Mining [13, 17, 26] represents
the set of techniques and methods that enable data analysis fulfilling the following characteristics:
(a) High amounts of data coming in an infinite stream [26]; (b) Concept Drifting [15, 42, 47], i.e.,
data change or evolve over time; (c) High volatility, that prevents the possibility of storing the data
and calls for online methods where data is analyzed as soon as it received and it is discarded or
summarised.

Besides traditional supervised [16] or unsupervised [25] learning problems on data streams,
recommendation can be considered an extremely significant landscape for data stream mining.
The massive amount of information available to users in the form of digital catalogs and online
services requires the capability to appropriately select relevant content and filter out irrelevant
data. Understanding and predicting users’ choices and preferences is thus a challenging task
and Recommender Systems (RS) play a crucial role in modeling complex situations, where
prior beliefs, specific tendencies, and reciprocal influences jointly contribute to determining such
preferences [1, 5, 35].

Notably, although the field has been extensively studied and several techniques and methods
were proposed in the literature, there is a significant gap between research algorithms and models,
and real-life industrial deployment of RS. In fact, the former are often based on the unrealistic
assumption that preferences are static and do not tend to change over time. As a consequence,
the studies essentially focus on static datasets collected over relatively long periods, and build
preference models that tend to be periodically updated. This perspective has obviously several
limitations, as it ignores the streaming nature of preference data and consequently the continuous
evolution of the interactions, due either to catalog updates, user churn or new acquisitions, and
evolving tastes or preferences. This problem has been recently at the center of the attention of
current research [2] and some initial attempts were made to devise more sophisticated models
capable of capturing the dynamic nature of preferences [11, 29, 30, 43, 45].

In this article, we address the problem of the shortage of sufficiently large public datasets with
real properties, needed to train and evaluate modern recommendation systems. When evaluating
recommendation systems in a streaming scenario [44], a significant challenge arises: How can we
effectively assess the robustness of advanced machine learning systems and quantify their perfor-
mance in a controlled experimental benchmarking environment, where all the characteristics of
the data can be appropriately tuned and the algorithmic response can be evaluated accordingly?
This problem is challenging for a number of relevant reasons. The most important is that obtaining
large-scale public repositories that represent interaction datasets is difficult, due to inherent

ACM Trans. Recomm. Syst., Vol. 3, No. 2, Article 24. Publication date: March 2025.

---

<!-- PAGE 3 -->

Modelling Concept Drift in Dynamic Data Streams for Recommender Systems

24:3

privacy and technological concerns associated with their sharing. In fact, the available datasets
such as Amazon [32], Netflix [7], or MovieLens [19] are orders of magnitude smaller than propri-
etary data and typically contain data collected in a limited period where preferences have been
collected. Synthetic data generators can help us alleviate this problem by providing ad-hoc datasets
where the data characteristics (number of users/items, number of interactions, data distributions)
can be manipulated and the algorithmic robustness compared according to such manipulations.
However, existing data generation methods do not take into account the dynamic nature of the data
distribution, which is likely to occur in a streaming scenario and in the presence of evolving prefer-
ences along the time dimension. This situation is further exacerbated by the lack of general models
for distribution dynamics, which should instead be accurately studied and correlated to algorithmic
responses.

In practice, synthetic data generation that accounts for drifts in a continuous streaming scenario

needs to address the following challenges:

(1) First, we need to hypothesize a preference model that can realistically characterize item
adoption and user preferences. This model should serve as the basis for the data generation
process without introducing any bias that is not actually observable in real data.

(2) Second, we need to consider all possible changes that can cause a drift within the preferences.
Drifts can be abrupt or progressive, they can involve a percentage of users/items or the
whole population, and they can be caused by new emerging trends or by changes in the
characteristics of users/items. All these aspects need to be modeled, and the data generation
process needs to embed them.

In order to deal with the above issues, we propose a general preference model that can easily
adapt to cover preference dynamics. We focus mainly on implicit preferences: Given a user/item
pair, a preference is a binary response expressing the fact that the user adopted/did not adopt the
item. This simple representation scheme naturally induces a per-user ordering among items, which
can, hence, be ranked according to the adoption likelihood. Our basic assumption is that both users
and items map to an underlying latent low-dimensional manifold, and preferences essentially oc-
cur due to closeness within this latent space. Notably, this interaction can be made explicit by
uncovering the latent space and modeling the interactions as a tripartite graph connecting users,
latent space dimensions, and items. As a consequence, preference dynamics can be easily made ex-
plicit by suitable modifications of the latent embeddings, which in turn represent modifications of
the underlying graph, as addition/deletion of nodes or changes in the connectivity, thus producing
realistic evolving preference data streams with characteristics that change over time (concept drift).
A major challenge is quantifying how realistic a preference model is when drifts are represented
as changes in the underlying embeddings. We approach this by investigating the behavior of the
underlying model on realistic data streams and studying how it can effectively replicate real-data
distributions. In practice, in our evaluation, we adopt a scheme where (i) drifts can be identified in
real data by observing the model’s inability to capture realistic preferences, and (ii) the model auto-
matically adjusts by making minimal changes to the graph structure to align actual and generated
preferences. In our scenario, the optimal adjustments are those that can accurately predict actual
preferences with minimal error, even in the presence of concept drift. Notably, the analysis of real
data also allows us to devise and characterize the changes that typically can occur, thus devising
a fully generative model for synthetic yet realistic preference data that can also be characterized
by preference dynamics.

To summarize, the main contributions of the article are

— A preference model based on latent embeddings. According to such a model, concept
drifts can be modeled as major modifications of the embeddings, that can be deemed as

ACM Trans. Recomm. Syst., Vol. 3, No. 2, Article 24. Publication date: March 2025.

---

<!-- PAGE 4 -->

24:4

L. Caroprese et al.

rewiring changes in the underlying tripartite graph. We show that this model is capable of
characterizing real-data distributions and can hence be used as a basis for synthetic data
generation.

— A stream-based data generator that can produce preference data also characterized by
preference dynamics. We study a categorization of the possible drifts that can occur
within preferences. To the best of our knowledge, this is the first attempt to systematically
approach the problem and propose a solution.

The remaining sections of this article are organized as follows. Section 2 presents a systematic
literature review on synthetic data generators for RS. In Section 3, we formulate the problem of
generating synthetic data and propose an algorithm for detecting drifts in preference data. Sec-
tion 4 provides details on experiments conducted using real data and discusses the application of
learned models for emulating a data generation process. Section 5 introduces a general data gener-
ation scheme based on the insights obtained from the experiments. Finally, in Section 6, we draw
general conclusions and outline future research directions.

2 Related Work

Generating synthetic data streams is not entirely novel and has been proposed in the past for
general machine learning tasks, such as classification and regression [8, 38]. However, previous
research on synthetic data streams for recommendation systems is limited and highly fragmented,
tackling different data issues such as user privacy [37], scalability, shortage of benchmarks [6, 9,
31, 41], and, most closely related to this work, concept changes [21].

In the work by Slokom et al. [37], the authors present a method to hide certain preference-related
user information from a set of user-item interactions, which otherwise could be accessed. Their
approach employs the CART algorithm [10], and the output is a set of synthesized preference data,
which preserves crucial statistical properties of the original data in order to be helpful for the
testing of recommendation algorithms but hides specific user information, such as their favorite
actor in the case of movie recommendation. However, their method is unable to generate new
ratings for unseen items, and it is unclear to what extent their approach can generate incremental
data or produce data streams with dynamically changing characteristics.

The same limitation holds for the work by Belletti et al. [6]. The authors employ a data generator
to produce a realistic copy of the MovieLens dataset but with a heavily extended number of users,
items, and ratings. While this approach successfully scales up the MovieLens dataset by several
orders of magnitude, therefore overcoming scalability, it does not address the issue of dynamic
changes in user preferences. In other words, there are no parameters in the generation process
that control drift in the data. In their study, Tso and Schmidt-Thieme [41] propose a synthetic
data generation methodology to examine the performance of attribute-aware algorithms. They
manipulate the level of informativeness of attributes in their artificial datasets to study their im-
pact on algorithm behavior. In the domain of context-aware recommendation systems, del Carmen
Rodríguez-Hernández et al. [9] developed a system specifically designed for generating preference
data that incorporates contextual information. Their aim was to address the lack of suitable bench-
marks in this area of research. Interestingly, their generator can mix real and synthetic data and,
thus, mimic properties from existing datasets. However, a change in the data, e.g., user taste, is
not considered in the generation process. The same holds for the work of Monti et al. [31], who
present a cluster-based data generation method that learns the rating behavior of specific user
communities and uses this information to generate new ratings.

In the work of Koren [24], the authors proposed to capture the temporal dynamics of user pref-
erences. More specifically, they tried to model gradual and sudden drifts using linear and spline

ACM Trans. Recomm. Syst., Vol. 3, No. 2, Article 24. Publication date: March 2025.

---

<!-- PAGE 5 -->

Modelling Concept Drift in Dynamic Data Streams for Recommender Systems

24:5

modeling of user biases. They also explored the impact of day effects on the bias. The results show
that the splines are more flexible in capturing user effects on gradual drifts, and the single-day
effects are useful for capturing sudden drifts. Similarly, the work of Bakir [4] describes the adop-
tion of a matrix factorization (MF) model using SVD, and to map the temporal dynamics, the
authors proposed the application of a conversion function used for the calculation of the age of
the ratings, giving more weight to more recent ratings and slowly forget old preferences. The
authors assumed that a gradual transition exists in the users’ preferences. With the increase of in-
terest in deep learning models (embedding), researchers developed some solutions for a sequential
recommendation.

In particular, [28] used self-attention mechanisms to capture interactions between two watched
items in predefined time intervals. Another approach proposed by Kang and McAuley [22] assigns
weights to watched items to forget past interactions or give relevance to them. In both cases,
the authors are trying to model the changes in user preferences. Our work not only models the
users’ preferences but also is capable of generating artificial drifts or producing synthetic data with
similar data distributions.

A recent work proposed by Veloso et al. [43] models user preferences using incrementally up-
dated embeddings. The proposed model is equipped with a drift detector to capture changes in
users’ preferences and initiate a real-time optimization task. The main idea is that every time
during the learning process a drift is detected, the model needs to be adjusted by changing its
hyperparameters.

Regarding drift detectors, there are several solutions available in the literature. Drift Detec-
tion Method (DDM) proposed by Gama et al. [14] observes the learner error rate and assumes
that with the increase of observed examples, the error rate will decrease since the data distribu-
tion is stationary. If the error rate increases above a specific threshold calculated based on the error
rate and standard deviation at one specific instant, it will trigger one alarm. Another variant of
this method called the Early Drift Detection Method (EDDM), proposed by Baena-García et al.
[3], was developed to improve detection performance under gradual concept drifts. The authors
proposed adopting running average distance and running standard deviations instead of calculat-
ing the values at specific instants. The Hoeffding Drift Detection Method (HDDM) proposed
by Frías-Blanco et al. [12] works with a different principle. It uses the Hoeffdings inequality and a
moving average test to detect the concept drifts. The Page–Hinkley method proposed by Sebastião
and Fernandes [36] detects changes using the CUSUM control chart and computes the observed
values and their mean until the current instant. If there is a change (increasing or decreasing the
mean), it will signal an alarm based on a predefined threshold. Finally, the Adaptive Windowing
(ADWIN) method proposed by Bifet and Gavalda [8] uses a dynamic-sized window that keeps
recent examples with the same data distribution. The window can be split into two parts and
compared if the data distribution is the same on both sub-windows, signaling an alarm if this con-
dition is invalid. The focus of this work is not to develop new DDMs but to use them to identify
the changes in the data distributions and build a portfolio of models.

Lex et al. [27] propose the adoption of Base-Level Learning (BLL) equations from the
cognitive architecture ACT-R together with recency-based modeling of music genre preferences,
which indicates a tendency for individuals to listen to genres they have recently encountered. The
significance of temporal drift in music genre preferences appears in all user groups. Consequently,
incorporating recency information is expected to enhance prediction accuracy. Similarly, Oyewole
[33] introduced a model for user temporal preferences designed to ascertain the recency weight
of an item, thereby capturing shifts in user preferences over time. The core principle of this
time-weighted algorithm is the determination of appropriate weights for all items, ensuring that

ACM Trans. Recomm. Syst., Vol. 3, No. 2, Article 24. Publication date: March 2025.

---

<!-- PAGE 6 -->

24:6

L. Caroprese et al.

more recently purchased items have a more significant influence on subsequent recommendations.
Consequently, items purchased more recently are typically assigned higher weight values than
those purchased earlier.

Han et al. [18] propose a hypergraph wavelet learning methodology to capture the subtle drifts
in job preferences. To address the impact of noise in interactions, which is often a consequence
of frequent preference changes (drifts), they introduce an adaptive wavelet filtering technique
designed to eliminate these noisy interactions.

According to Sun et al. [39], the recommendation for each user is conceptualized as an individual
learning task that aims at capturing region-independent personal preferences by utilizing their
check-in data without considering specific regions. Understanding users’ immediate demands and
modeling short-term preferences are crucial for the subsequent recommendation. To achieve this,
they employ sequential models to represent users’ personal preferences, thereby exploring their
behavior patterns through their complete check-in sequences using LSTM models.

Thaipisutikul [40] integrates contextual information into the subspace decomposition of short-
term and long-term memory units within the Long Short-Term Memory (LSTM) framework.
Specifically, they introduce a mechanism to attenuate the influence of the memory cell such that
as time progresses or concept drift occurs, the impact of prior memory on the current output
diminishes.

Yang et al. [48] employ a recurrent neural network (RNN)-based model to generate short-
term user preferences, incorporating dual branches specifically designed for preference transfer
and drift. The transfer branch and the Point of Interest (POI) embedding vectors are shared
between tourists and residents within the current city. In contrast, the drift branch captures varia-
tions in preferences among different user roles, including a tourist in their home city, a tourist in
the current city, and a resident in the current city.

Wangwatcharakul and Wongthanavasu [46] propose a model that learns multi-transition
low-dimensional factors to effectively capture variations in user interests across different periods.
The model emphasizes the importance of temporal influences, noting that a well-designed
algorithm should progressively diminish the impact of older data while maintaining accuracy
in predicting future user preferences. Initially, the model calculates the rating shift rate using
a time decay function that accounts for the forgotten information. Subsequently, it captures
the latent drift in user factors between successive time points to monitor the multi-transition
factors.

To our knowledge, the work of Jakomin et al. [21] is the only one that addresses incremen-
tal changes in the data. In this study, the authors present a method to generate multiple inter-
dependent data streams to evaluate recommendation or data fusion algorithms. The main idea
behind their generator is to simulate scenarios where groups of similar users rate groups of sim-
ilar items in the same manner. In other words, different probabilities connect the resulting users
and item clusters. These probabilities determine the ratings that users of a given user cluster would
give an item of a given item cluster. The output is a rating matrix where each non-zero cell rep-
resents the relation between a particular user and an item. Using arithmetic operations such as
multiplication or division to the ratings at a given time allows them to simulate concept drift.
However, this represents a limitation, as it does not consider changes in the latent feature space;
i.e., the embedding remains at a similar size, and users and items remain connected to the same
features as the data evolves. Our work differs from the literature in the following aspects: (i) We
model the user/item preferences and their evolution over time as a dynamic tripartite graph; (ii)
We learn from a real data stream a sequence of latent matrices that models this graph, and, lastly,
(iii) We use this sequence to produce synthetic data streams whose properties are similar to those
of the original one.

ACM Trans. Recomm. Syst., Vol. 3, No. 2, Article 24. Publication date: March 2025.

---

<!-- PAGE 7 -->

Modelling Concept Drift in Dynamic Data Streams for Recommender Systems

24:7

3 Data Stream Modelling

The proposed data generator can produce synthetic streams of preference data based on a graph
learned from real data. The generation process and the drift operations will be explained in the
following sections.

3.1 Basic Framework

We start by introducing the notation to be used throughout the remainder of this article. In the
following, u ∈ U = {1, . . . , N } indexes a user, and i ∈ I = {1, . . . , M } indexes an item for which
a user can express a preference. Let ru,i ∈ {rmin, . . . , rmax} denotes the preference (rating) of user
u for item i. The range {rmin, . . . , rmax} represents a preference rank: When ru,i = rmin, user u
maximally dislikes item i, while ru,i = rmax denotes maximal preference for the item. Typical
ranges are {0, 1} (implicit preference) or {1, . . . , 5}. In the following, we shall focus on implicit
preferences.

The set of all preferences can be represented as a rating matrix R, or alternatively, as a set
of triplets R = {(u1, i1, r1), . . . , (un, in, rn)}, where each triplet (uj , ij , rj ) represents an inter-
action between any user uj and any item ij , with rj = ruj,i j being the corresponding rating.
When N and M are large, R only represents a partial and extremely small view of all possible
ratings.

We adopt an MF framework for predicting the score that a user u assigns to each item i. Each
user u and item i admit a representation in a K-dimensional space. We denote such representations
by embedding vectors pu , qi ∈ RK , which represent the rows of the embedding matrices P ∈ RN ×K
and Q ∈ RM ×K .

Given user u and item i, the corresponding score ru,i can be modeled as a random variable
with a fixed distribution whose parameters rely on the embeddings pu and qi . This model can be
represented with a weighted and undirected tripartite graph. It has three types of nodes: Nodes
representing users (user nodes), those representing items (item nodes), and those representing fea-
tures (feature nodes). Edges can only connect users to features or items to features. The weight of
a user/feature edge (resp. item/feature edge) is a measure of how strongly that feature is present
in the user (resp. item); see Figure 1.

The preference matrix R induces a natural ordering among items, where i (cid:4)u j means that u
prefers i to j, i.e., ru,i > ru, j . The additional assumption that we make in this work is that the
partial view R can be continuously updated. That is, either new unknown entries can be disclosed
(for example, some users can express preferences for previously unseen items) or former prefer-
ences change (for example, due to change of tastes by the user, or due to a more accurate evalu-
ation). Thus, we assume that the history of preferences produces a continuous stream of shards
R(1), R(2), . . . , R(t ), where R(t ) represents the view of R at time t.

As already mentioned, snapshots can overlap, i.e., it can happen that both r

(n)
u,i

m (cid:2) n, and r
(cid:2) r
preserves recency. That is, by denoting
max{t | (u, i, ru,i ) ∈ R(t )}. If no such t ∗ exists, then V

(m)
u,i . We then define
(cid:2)

(cid:2)

(m)
u,i exist for
n ≤t R(n) as a merge among R(1), R(2), . . . , R(t ) that
(t ∗)
u,i , where t ∗ =

(n)
u,i and r

= r

(t )
u,i

n ≤t R(n) as V (t ), we define V
(t )
u,i is undefined.

Over time, the distribution of data can change, more or less abruptly. When this occurs, we
are facing a concept drift. The situation is illustrated in Figure 2. Typically, we can consider a
stream as the cooperation of multiple regimes that interact to produce observable data. A regime
i is characterized by an underlying model, described by factorization matrices P(i) and Q(i). The
appearance of a new regime as a result of a shift in data distribution reflects changes in user
preferences or the entry of new features. As shown in the figure, the changes are essentially due
to changes in the underlying graph which reflect on different samples in the data sampling process.

ACM Trans. Recomm. Syst., Vol. 3, No. 2, Article 24. Publication date: March 2025.

---

<!-- PAGE 8 -->

24:8

L. Caroprese et al.

Fig. 1. User/Feature/Item graph.

Fig. 2. Regimes in a data stream.

The challenge of managing new users or items can be addressed by adding new nodes initialized
with a heuristic function that considers the characteristics of the graph in the ith regime. However,
this approach introduces an additional layer of complexity. A feasible simplification is to avoid im-
posing specific assumptions and instead initialize the nodes randomly, then evaluate the variation
in model performance across different regimes. That is the actual implementation.

In practice, the problem we want to face is how to devise a data generation process based on
factorization matrices P and Q, capable of reflecting such changes. An initial attempt in this direc-
tion was made in [43]. More importantly, the questions we want to answer here are: What are the
typical changes that characterize a real (or realistic) data stream, and how can we model them by
controllable (model-based) adaptations of the underlying sampling process?

We approach this problem in two different steps. In the first step, we study how a popular fac-
torization model [34] can be used to track and describe changes in a real-life data stream. For this,
we propose an inference algorithm that, given a data stream, is capable of tracking viable changes
and adaptations of the underlying model to reflect the actual stream. The study and characteriza-
tion of such changes will then allow us to devise a fully controllable procedure for generating data
streams exhibiting concept drifts.

3.2 Learning Concept Drifts
The formulation we consider is inspired by the Bayesian Personalized Ranking (BPR) model
introduced in [34]. The BPR model is a popular implementation for MF-based model, ensuring scal-
ability, trainable on implicit feedback (no ratings are required). The training phase is quite effective,
as it is performed by comparing pairs of items that a user has interacted with and optimizing the
ranking of these items. This model allows us to process datasets with thousands of items and users.
Being highly popular in literature, it represents the primary choice made by numerous authors in
the field of RS. Moreover, the BPR model is chosen because of its robustness and suitability for

ACM Trans. Recomm. Syst., Vol. 3, No. 2, Article 24. Publication date: March 2025.

---

<!-- PAGE 9 -->

Modelling Concept Drift in Dynamic Data Streams for Recommender Systems

24:9

handling implicit preferences. However, the key aspect of the approach is not just the model itself
but its ability to track changes over time through adjustments in the latent factor matrices. In prin-
ciple, any MF model that supports a probabilistic interpretation of user/item adoption in terms of
latent factors could be used.

The idea underlying this model is that a preference i (cid:4)u j can be directly explained as closeness
in a latent space where both items and users can be mapped. Mathematically, this can be devised
u qi for each pair (u, i), and modeling precedences by means
by computing a factorization rank pT
of a Bernoulli process:

(cid:3)

(cid:4)

i (cid:4)u j ∼ Bernoulli(p) ,

p = σ

pT
u

(qi − qj )

,

where σ (a) = (1 + e−a)−1 is the logistic function. The optimal embeddings M = (P, Q) can hence
be obtained by optimizing the loss:

(cid:5)

(cid:5)

(cid:3)

(cid:4)

(cid:2)bpr (M|V ) =

log σ

pT
u

(qi − qj )

,

(1)

u

i, j
i (cid:4)u j

where i (cid:4)u j means Vu,i > Vu, j .

We can exploit

the above learning scheme to devise a sequence of embeddings
M(t1), . . . , M(th ), . . . where each M(t ) =
n ≤t R(n)) as ex-
P(t ), Q(t )
plained below. In particular, each model of this sequence represents a different regime and
characterizes its data distribution.

is trained on V (t ) (i.e.,

(cid:2)

(cid:6)

(cid:7)

Typically, RS are optimized by exploiting historical interactions as training data, to produce
a model that can predict users’ future interactions in the testing data. This scheme inherently
assumes that the training and testing data are drawn from the same distribution. However, distribu-
tion shifts can occur when changes in the preferences (expressed as modifications in the underlying
graph discussed in the previous section) occur. In practice, a model trained on current data is likely
to deteriorate its performance on future data when a substantial drift in the preferences occurs.

These observations inspire a specific protocol for training the embeddings M(t1), . . . , M(th ), . . .
characterizing the drift. The timestamp ti here represents the drift: model M(ti −1) underperforms
on R(ti ) and, as a consequence, we need to retrain the model. The idea is to devise a continuous
learning framework through the shards: at each step t the model is optimized on V (t ). If the model
substantially underperforms on R(t ), then an adaptation is required. Formally, we define the loss

(cid:5)

Lc (M; R) =

(cid:2)bpr (M|R) + λ(||P||∞ + ||Q||∞)

u ∈S

that includes the regularization term.

By minimizing the infinity norm of P and Q, we enforce an upper bound on the matrix weights

during the training process. This ensures that the weights belong to a limited range.

Then, given a current model M, we check whether a drift has occurred by checking the loss

Lc (M; R(t )).

If no drift is detected, the process proceeds in two steps:
— First, a synthetic interaction dataset S is generated from M.
— Next, M is updated by optimizing the loss Lc (M; S (cid:9) R(t )).
The second step resembles a continual learning strategy [13]. In principle, the model should
be updated from the entire V (t ). However, in a streaming scenario, it is impractical to maintain
the whole set of past interactions. Exploiting the current model to generate a sample S, with the
same size of R(t ), has the advantage of compacting the representation of past interactions and

ACM Trans. Recomm. Syst., Vol. 3, No. 2, Article 24. Publication date: March 2025.

---

<!-- PAGE 10 -->

24:10

L. Caroprese et al.

additionally, it provides better control on past preference shifts since the model will disregard
obsolete interactions.

If a drift is detected, M is obsolete and requires a substantial update. In our framework, this
means that the graph topology can change, with new users/items and/or features. We adopt a
conservative approach to tackling this problem. For a given user/feature probability vector pu ∈
RK , it is possible to devise an infinite-dimensional extension p(cid:10)
=
u
pu,k if 1 ≤ k ≤ K, and p (cid:10)
= 0 for k > K, and the same property holds for item/feature vector
qi . Thus, given M, we denote by M(cid:10) its infinite-dimensional counterpart. The learning objective
on the new regime can hence be stated as computing a new version M(cid:10) with minimal differences
w.r.t. M. Formally, we devise the loss

∈ R∞ initialized such that p (cid:10)

u,k

u,k

Ld (M

(cid:10)

; M, R

(t )) = Lc (M

(cid:10)

; R

(t )) + δ

|p

(cid:10)
u,k

− pu,k | +

(cid:8)

(cid:5)

K(cid:5)

u

k=1

(cid:5)

K(cid:5)

− qi,k |

|q

(cid:10)
i,k
(cid:9)

(cid:5)

(cid:5)

+

|p

(cid:10)
u,k

| +

k=1

i
(cid:5)

(cid:5)

|q

(cid:10)
i,k

|

u

k >K

i

k >K

the second term in the loss represents the divergence between underlying feature vectors. The ra-
tionale here is that the updated model should penalize unnecessary discrepancies with the previous
model on the current features, while at the same time letting the model introduce new features in
order to adapt to the current changes. In practice, the training starts by adding ΔK new columns
(initially set to 0) to both P and Q and then optimizing the extended model through Ld on the
new shard R(t ). Algorithm 1 provides an overview of the learning procedure. In this procedure,
we utilize the driftDetection function to detect any drifts in the losses. The effectiveness of drift
detection heavily relies on the chosen signal, which in our case is primarily the loss values. By
monitoring the loss function’s value, we can identify significant deviations in the model’s perfor-
mance, indicating the presence of drifts. However, it is worth noting that the choice of the signal
for drift detection can vary depending on the specific application and problem domain, which can
lead to different performance for detection algorithms. We employ the HDDMW algorithm [12], a
well-known DDM based on Hoeffding’s bounds with a moving weighted average test. HDDMW uti-
lizes the Exponentially Weighted Moving Average (EWMA) statistic as an estimator. Given a
stream of values (in our case, loss values) as input, it determines the estimated status of the stream:
Stable, Warning, or Drift.1

Therefore, the model is updated using two training modalities:
— when a drift occurs, we train the model M(cid:10) with the data of the current shard and penalize

the distance between M(cid:10) and the model learned in the previous regime M;

— otherwise, the current model M is refined on data of the current regime and a sample of
historical data generated from the model M of the current regime. This guarantees that the
model is aware of both a summary of the previous data and the new data available.

Finally, the generateSamples function leverages the matrix M to generate nS new samples.
This procedure involves sampling items for each user based on their score, with the probability
of selection proportional to the score. The item frequency for each user (or user frequency
for each item) can be estimated using a Zipf distribution or provided as input to preserve the
original properties. These frequencies help determine the number of items to sample and bias the
probability of selecting low-popularity items.

1Notice that the adoption of HDDMW requires bounded signals, which can be guaranteed by bounding the difference in
Equation (1).

ACM Trans. Recomm. Syst., Vol. 3, No. 2, Article 24. Publication date: March 2025.

---

<!-- PAGE 11 -->

Modelling Concept Drift in Dynamic Data Streams for Recommender Systems

24:11

The sample is combined with the shard’s data to train the current model. This approach aims
at retaining historical information without requiring the storage of all data in the current regime,
in this way we balance the weight of new preferences and the past ones. However, when a drift
occurs, we switch to a different strategy aimed at minimizing the deviation from the previous
model; thereby reducing the impact of the limited current data, i.e., the preferences of the current
shard, on updating the new model and preserving a soft transition between regimes. The value of
parameter nS has been set equal to the size of the Bt r ain set of the current shard, weighting equal
to the number of preferences observed in the current shard and in the current regime.

4 Experiments
We conducted an empirical evaluation of Algorithm 1 with two main objectives. Firstly, we aimed
to monitor actual drift in realistic scenarios. Secondly, we aimed to devise a data generator that
captures the properties of realistic data streams and effectively models concept drift similar to
what is observed in real data.

We processed three real data streams using our proposed approach. During the training phase,
we identified a sequence of regimes for each dataset, each characterized by its data distribution. We
associated an MF model with each regime. Using this sequence of models, we generated a synthetic
data stream that closely resembled the original stream. This was achieved by imposing the same
regimes in the same order, with an equal number of samples for each regime. By comparing the
original and synthetic streams, we assessed the fidelity of the generator in sampling new data.

Our approach yielded satisfactory results when the number of item preferences was sufficiently
high to train a model capable of replicating a real stream. This was especially evident in datasets
where there were numerous items with few preferences and a core set of highly popular items.
The behavior can be explained by the model’s inability to accurately estimate the distribution of
underrepresented items. To achieve good generation performance, it was crucial to have a suffi-
cient number of preferences for each item. This condition was naturally met when the number of
users significantly exceeded the number of items. In fact, the first and third datasets satisfied this
condition, as the distribution of the synthetic data closely resembled that of the original data.

We also chose a second dataset that did not exhibit this behavioral pattern, where the number of
users was much smaller than the number of items. In this case, the distribution of the synthetic data
generated by the generator deviated significantly from the original data. To further support our
hypothesis, we reversed the roles of users and items and repeated the experiment, demonstrating
the importance of having an adequate number of preferences to derive an effective model. The
results were satisfactory in this case.

Additionally, we selected a third dataset to analyze changes in distributions during a drift. We
drew insights from a study by Yang et al. [49], where they tackled the challenge of developing a
recommender system that can adapt to the dynamic nature of user preferences and item popularity.
To foster reproducibility, we have publicly released all the data and code required to reproduce our
experiments.2

4.1 Datasets

Our analysis is conducted on the following popular benchmark datasets, each from a different
domain and having specific characteristics:

— Microsoft News (MIND): This dataset consists of news articles published on the Microsoft
News website and the feedback logs generated by 1 million users over a span of 6 days. We

2https://github.com/fsp22/mcd_dds4rs

ACM Trans. Recomm. Syst., Vol. 3, No. 2, Article 24. Publication date: March 2025.

---

<!-- PAGE 12 -->

24:12

L. Caroprese et al.

ALGORITHM 1: Learning Latent Matrices

Input: Stream R = R

(1), . . . , R

(n), . . . of preferences ordered in shards; number of samples nS to

generate for training the model within the i-th shard, in conjunction with the shard’s data.

Output: A list M

(0), . . . , M

(h), . . . of preference models

1 t = 0; (cid:2) = ∅
2 q = ∅; r = ∅
(t )
3 initialize M
(i)
4 for each R

5

6

7

8

9

10

11

12

13

14

15

16

17

18

in R do
Btrain, Btest = splitData
(cid:3)

(cid:4)

(cid:4)

(cid:3)

(i)

R

(t )

M

; Btest

(cid:2)drift = Lc
drift = driftDetection((cid:2)drift, (cid:2))
if drift then
M
optimize M
t+=1

:= extendModel(M
on Ld (M

(t +1)

(t +1)

(t ), ΔK )
(t +1)
; M

(t ), Btrain)

end
else

S, q, r = generateSamples(M

(cid:3)

(t ), nS , q, r )
(cid:4)

optimize M

(t )

on Lc

(t )

M

; S (cid:9) Bt r ain

(t )

end
(cid:2)eval = Lc (M
(cid:2) = (cid:2) ∪ {(cid:2)eval }
Update user and item popularities q, r based on R

; Bt est )

(i)

19
20 end
21 return
22 Function generateSamples(M, nS , q = ∅, r = ∅, α = 1.8, β = 1.9, c = 1, d = 5):

(cid:10)
t

(t )}

{M

23

24

25

26

27

28

29

30

31

32

33

34

35

36

37

38

39

40

Function normalize(μ):
˜p = σ (c · μ − d)
return ˜p/(
if q = ∅ then

i ˜pi )

(cid:11)

for each u ∈ U do qu = Zipf (α, 1, M/c)

end
if r = ∅ then

for each i ∈ I do ri = Zipf (β, 1, N /d)

(cid:11)

u qu )(cid:14)
(cid:11)

end
for each u ∈ U do
qu = (cid:13)nSqu /(
˜pu = normalize(pu · Q)
pu = ( ˜pu (cid:15) r )/(
i ˜pu,iri )
nu = min(qu , |{i |pu,i > 0}|)
Sample with replacement nu items Iu from I with probability proportional to pu
S = generateTriplets(u, Iu )

end
return S, q, r

ACM Trans. Recomm. Syst., Vol. 3, No. 2, Article 24. Publication date: March 2025.

---

<!-- PAGE 13 -->

Modelling Concept Drift in Dynamic Data Streams for Recommender Systems

24:13

utilize the click information of each news article by users to construct a dataset. The read
news articles serve as user preferences, and we consider only users who have at least one
preference (news read). The final dataset comprises 19,206 items and 3,958,500 preferences
from 750,434 users. The dataset can be accessed at https://msnews.github.io/.

— Amazon Video Games: This dataset contains ratings provided by users for video games.
The ratings range from 1 to 5. As our approach focuses on implicit feedback, we binarize
the data by assigning a value of 1 to user-item pairs where the rating is strictly greater than
3, and 0 otherwise. To address GPU memory limitations, we process a subset of the dataset,
considering the last 824,752 preferences from 26,038 users registered over a span of 10 years,
with respect to 567,865 items. The dataset can be accessed at http://snap.stanford.edu/data/
amazon/productGraph/categoryFiles/ratings_Video_Games.csv.

— Yoochoose: This dataset was published for the RecSys Challenge 2015. It comprises a col-
lection of sessions from a retailer, specifically focusing on the purchase events of users. To
streamline the dataset, we selected items that were interacted with more than 4 times and
removed users with fewer than 3 purchased items. After the cleaning process, the dataset
consists of 143,481 users, 9,975 items, and 642,237 interactions. The dataset can be accessed
at https://www.kaggle.com/datasets/chadgostopp/recsys-challenge-2015.

These datasets were chosen due to their popularity and diverse characteristics, enabling us to
conduct comprehensive analyses and draw meaningful conclusions.

4.2 Modeling Data Streams
Following the protocol presented in Section 3, we test our model on the datasets reported in Sec-
tion 4.1. For each user u and each item i which is positive for u (i.e., (u, i, 1) ∈ R(t )), four negative
items j are sampled (i.e., (u, j, 1) (cid:3) R(t )). In our framework, we consider as negative any item that is
not explicitly positive for a user. This includes both items that the user has never interacted with
and items that the user explicitly dislikes. Thus, in this case, (u, j, 1) must not belong to R(t ) which
is different from saying that u dislikes j, i.e., (u, j, 0) must belong to R(t ).

This approach is common in RS, particularly when dealing with large item catalogs. The ratio-
nale behind this method lies in the typical characteristics of recommendation scenarios. In most
cases, the number of items a user likes is significantly smaller than the total number of available
items. For instance, in a catalog of millions of products, a user might only be interested in a few
hundred. This creates a very sparse preference matrix. Given this sparsity, randomly sampling an
item has a high probability of selecting one that the user would not like or has not interacted with,
making it a reasonable proxy for negative feedback. This assumption simplifies the modeling pro-
cess and is especially useful when detailed interaction data (like viewed but not purchased items)
is not available.

The triplets (u, i, j) are processed in chronological order grouping them in batches of 2 000 tuples.

We split each batch B in two sets: (i) a training set Bt r ain (70%), and (ii) a test set Bt est (30%).

To train the model, we use 20 epochs; the optimizer is the ADAM algorithm with a learning
rate of 0.001, and the loss functions are presented in Section 3.2. After each batch, we evaluate the
model on the test set, and we report some performance metrics. We consider (cid:2)bpr (M|Bt est ) and
the Hit-Rate score. Let us recall the definition of this last metric: Given a user u occurring in Bt est ,
we consider the set Pu of its positive items (i.e., Pu = {i | (u, i, j) ∈ Bt est }) and sample a set Nu of
negative items (|Nu | = 100, in our case). Then for a given cutoff k (we use k = 10 and k = 5) we
consider the k − 1 negative items in Nu for which M returns the highest score. Among them, we
consider the item j with the lowest score. There is a hit with cutoff k, for the user u and the item
i ∈ Pu , if M(u, i) ≥ M(u, j). In the following, we report both HR@5 and HR@10.

ACM Trans. Recomm. Syst., Vol. 3, No. 2, Article 24. Publication date: March 2025.

---

<!-- PAGE 14 -->

24:14

L. Caroprese et al.

Fig. 3. Loss on test set part of each batch of the Microsoft News dataset.

Fig. 4. Results for the Microsoft News dataset.

4.3 Experiment on MIND
Figure 3 shows the loss computed on the test part of the current batch (i.e., Lbpr (M, Bt est )) aver-
aged on a moving window of 20 batches. The moving average highlights the increasing/decreasing
trend, disregarding a local minimum/maximum. The orange vertical lines indicate the batches
where the drift algorithm has detected a warning before a potential drift; meanwhile, the red lines
indicate a drift.

The loss is relatively stable with minimal increase/decrease due to the nature of the dataset. The
number of items is less than the number of users, while the news are equally scattered across the
dataset that covers only six days. For this reason, each batch contains a few new items, and the
preferences on hot news registered in a few hours should motivate the high number of warning
and drift alerts and the value differences between consecutive batches. We highlight that each
batch contains the news read in a few minutes.

The good performance in the loss chart can be also seen in the HitRate charts. Just after Batch
500, in Figure 4(a), we can see a low HR value (HR@5 ≈ 0.6). This behavior could be explained by
a drift following multiple warnings in the region close to the minimum. Probably, this indicates
a significant change. Comparing the HR@5 values with the HR@10 values, the second ones are
better for the same batches, indicating that the model worsens the predictions only on some items
while maintaining good overall performance. The number of warnings is due to the fluctuations
recorded in the loss.

The visual representation in Figure 5 provides insights into the distinctions between segments
of the real data corresponding to different regimes and their synthetic counterparts. The synthetic
data in each regime is generated by sampling from the model trained on the corresponding real

ACM Trans. Recomm. Syst., Vol. 3, No. 2, Article 24. Publication date: March 2025.

---

<!-- PAGE 15 -->

Modelling Concept Drift in Dynamic Data Streams for Recommender Systems

24:15

Fig. 5. Comparison of real and synthetic stream for the Microsoft News dataset: The chart shows the P(f >
k) where the ith frequency is denoted as k (log-scale on both axes).

data. To ensure a fair and meaningful comparison between the synthetic and original data streams,
we meticulously structured the synthetic data to mirror the original data. This involved maintain-
ing the same regimes in the same order and ensuring an equal number of samples for each regime.
In the charts, the horizontal axis represents the ith frequency denoted as k, while the vertical
axis indicates the cumulative count of items (i.e., P(f > k)), normalized by the sum of values. Upon
analyzing the distributions, we observe that the frequencies exhibit comparable patterns, thereby
confirming the effectiveness of training the different models. The similarity is also confirmed by a
positive outcome of the Kolmogorov–Smirnov test [20] on each regime.

The observed similarity between the distributions in the charts serves as strong validation for
the effectiveness and fidelity of our approach in generating synthetic data that accurately repro-
duces the characteristics of the original stream.

It’s crucial to note that our comparison focuses on frequency distributions rather than prefer-
ence distributions in the charts. This deliberate choice is motivated by the recognition that com-
paring preference distributions can be problematic due to the influence of popularity bias on pre-
dictive models for preference data [23]. Popularity bias tends to overlook contributions from cold
start users and low-popularity items, especially in preference data with vast item catalogs. Com-
paring distributions based on preferences would consequently fail, due to inaccurate associations
involving cold-start users and/or low-popularity items. By contrast, it is important to highlight

ACM Trans. Recomm. Syst., Vol. 3, No. 2, Article 24. Publication date: March 2025.

---

<!-- PAGE 16 -->

24:16

L. Caroprese et al.

Fig. 6. Loss on test set part of each batch of the Amazon Video Games dataset.

Fig. 7. Results for the Amazon Video Games dataset.

that such inaccuracies do not significantly impact the global modeling capabilities of the learned
embedding matrices, which is the main focus here.

4.4 Experiment on Amazon Video Games
We conducted similar experiments for the other two datasets. Firstly, for the Amazon Video Games
dataset, we analyzed the loss values (Figure 6) and HitRate (Figure 7) on the test set. In these charts,
we observe the presence of 7 regimes, indicating 6 detected drifts by the algorithm. We observe
similar patterns as seen in the MIND dataset, where the performance deteriorates when multiple
drifts occur in close proximity.

To compare the item distribution of the synthetic stream with the real stream, we examined the
distributions shown in Figure 8. In contrast to the MIND dataset, the distributions in this case are
significantly worse. This indicates that the number of preferences for each item is insufficient to
acquire the necessary knowledge required to accurately replicate the stream.

To further support this observation, we inverted the roles of users and items in the dataset. By
doing so, the number of items became smaller than the number of users, resembling the MIND
dataset. Analyzing the loss performance (Figure 9) computed on each batch (i.e., M, Bt est ) after
the training phase, we notice a rapid increase in loss value when a drift appears in the stream.
Subsequently, the loss value decreases as the model adjusts to the new data. Although the drift
detection algorithm triggers a false warning, it has minimal impact on the loss value. We do not
observe any significant changes in the HitRate values.

We computed HR@5 and HR@10 (Figure 10) and observed similar behavior in both settings.
The model performs poorly in the vicinity of a drift due to significant changes in the data

ACM Trans. Recomm. Syst., Vol. 3, No. 2, Article 24. Publication date: March 2025.

---

<!-- PAGE 17 -->

Modelling Concept Drift in Dynamic Data Streams for Recommender Systems

24:17

Fig. 8. Comparison of real and synthetic stream for the Amazon Video Games dataset: The chart shows the
P(f > k) where the ith frequency is denoted as k (log-scale on both axes).

Fig. 9. Loss on test set part of each batch of the Inverted Amazon Video Games dataset.

distribution, even with new user/item preferences or previously unseen items. However, after the
drift, the new model is trained on the updated data, and within a few batches, it regains optimal
performance.

In contrast to the previous case, the distributions of the generated data are noticeably improved
in this scenario. As depicted in Figure 8, the curves representing the distributions are very close
to each other. This observation aligns with our intuition regarding the significance of having an
adequate number of item preferences to train a generative model effectively. The close similarity
between the curves confirms the importance of having a sufficient number of preferences for each
item in order to accurately replicate the data.

4.5 Experiment on Yoochoose
The results from the Yoochoose dataset exhibit a behavior similar to the previous dataset. Figure 11
illustrates the loss on the test set, highlighting a single drift where there is a noticeable increase

ACM Trans. Recomm. Syst., Vol. 3, No. 2, Article 24. Publication date: March 2025.

---

<!-- PAGE 18 -->

24:18

L. Caroprese et al.

Fig. 10. Results for the Inverted Amazon Video Games dataset.

Fig. 11. Loss on test set part of each batch of the Yoochoose dataset.

in the loss value. However, the changes in the data distribution have only partially affected the
quality measures, as depicted in the HitRate charts in Figure 12.

This observation suggests that while the model’s performance is impacted by the drift, it is
able to adapt and adjust to the new data to some extent. The changes in the data distribution
have resulted in a decrease in the HitRate, indicating that the model’s recommendations are less
accurate during the drift period. However, it is worth noting that the model gradually recovers
and improves its performance after the drift.

Overall, the results from the Yoochoose dataset confirm the presence of drift and the model’s
ability to adapt, albeit with some impact on the quality of recommendations during the transition
period.

4.6 Comparison with a Baseline Algorithm

In this section, a comparison was made between the BPR algorithm and a model that could be more
easily adaptable to managing new users/items. We have chosen a variational autoencoder, in which
the number of items the system can handle is fixed a priori. The model receives as input the items
that a user has already seen and, based on this information, assigns a score to the entire catalog to
generate a ranking and thus build a recommendation list. Having the whole catalog available from
the outset gives the model a competitive advantage over the BPR model, which instead adapts by
updating the latent space when significant changes are detected in the system, both in terms of
new users/items and/or new preference patterns for existing users/items. Naturally, the impact on
performance will be more noticeable with many items distributed over a broad temporal range.

ACM Trans. Recomm. Syst., Vol. 3, No. 2, Article 24. Publication date: March 2025.

---

<!-- PAGE 19 -->

Modelling Concept Drift in Dynamic Data Streams for Recommender Systems

24:19

Fig. 12. Results for the Yoochoose dataset.

Fig. 13. Comparison of real and synthetic stream for the Inverted Amazon Video Games dataset: The chart
shows the P(f > k) where the ith frequency is denoted as k (log-scale on both axes).

Fig. 14. Comparison of real and synthetic stream for the Yoochoose dataset: The chart shows the P(f > k)
where the ith frequency is denoted as k (log-scale on both axes).

Conversely, in the presence of lower variability, i.e., when the model can learn patterns in the
initial moments that are valid for the entire observation period, a model like the VAE will have a
competitive advantage over an adaptive model.

Performance was measured for three datasets: MIND, Amazon Video Games with reversed
roles, and Yoochoose. The experiment could not be executed for the original Amazon Video
Games dataset because the model required excessive memory due to the high number of items
(567,865). Considering the Hitrate@5 values (the Hitrate@10 metric shows similar trends and is
not reported for brevity), for the MIND dataset (Figure 15), we can observe that the VAE model
reaches a peak value in the middle of the stream and maintains constant performance for the
rest of the observation period. Conversely, the BPR model exhibits more fluctuating performance
following the detection of drifts. The nature of the data can explain this: the dataset consists
of news produced over 6 days. In many cases, these are news items covering the same event,
resulting in reduced variability in identified user preference patterns. The system can learn highly
generalizable recommendation models. For instance, it is common to observe many users sharing

ACM Trans. Recomm. Syst., Vol. 3, No. 2, Article 24. Publication date: March 2025.

---

<!-- PAGE 20 -->

24:20

L. Caroprese et al.

Fig. 15. Comparing BPR and VAE on the MIND dataset (HitRate@5).

Fig. 16. Comparing BPR and VAE on the Inverted Amazon Video Games dataset (HitRate@5).

similar patterns because they read multiple news items on the same topic. In this case, the VAE
is more effective in detecting latent space similarities than the BPR.

For the Amazon Video Games dataset with reversed roles (Figure 16), i.e., where users and items
were swapped to have a catalog of 25k items, we observed worse performance for the VAE. As the
number of new items grows, the model’s performance degrades. Additionally, the recommendation
list contains items for which no preferences are observed. An adaptive system like BPR manages
these changes better, ensuring superior performance.

We can see a similar trend for the Yoochoose dataset in Figure 17. The main difference lies in the
oscillating pattern seen in the charts. The system adapts more quickly to changes in preferences,
but the limited temporal range prevents the model from converging to mid-high levels. In this
context, BPR adapts faster to changes, while the VAE system tends to be more stable around a
lower median value than BPR. Moreover, a descending trend is evident in the last shards of the
stream: a relatively high number of new items appears with a limited number of preferences, and
both systems struggle to identify new patterns effectively.

4.7 Ablation Study
Our approach aims at identifying a method that allows generating realistic data, replicating the
trends present in a real stream. To capture possible changes in preferences, regimes homogeneous
in expressed preferences are identified, and their corresponding models are stored to generate data
derived from those behavioral models. Two analyses were conducted to evaluate this protocol:

— try ignoring the regime identification, so we train the model only on the first regime and

then test the performance on data of the next regimes;

ACM Trans. Recomm. Syst., Vol. 3, No. 2, Article 24. Publication date: March 2025.

---

<!-- PAGE 21 -->

Modelling Concept Drift in Dynamic Data Streams for Recommender Systems

24:21

Fig. 17. Comparing BPR and VAE on the Yoochoose dataset (HitRate@5).

Fig. 18. Test performance of the first model, i.e., trained only on first regime, on the entire stream.

— compare the performance ignoring the stream nature of the data. We sample a ‘small’ train-

ing set with data of all regimes, then test on the full dataset w.r.t regimes.

In the first experiment, we trained a single model only on data belonging to the first regime. As
soon as a drift is detected, the model is frozen and tested on the rest of the stream. It is evident
that the model achieves good performance only on the data belonging to the regime it was trained
on and performs poorly on the remaining regimes (Figure 18). This result is not surprising but
confirms the need to implement a mechanism of continuous training that creates and trains a new
model when the characteristics of the stream data change, and their properties can no longer be
captured by the previous one.

In the second experiment, we created a training set by randomly extracting 30% of the samples
from the original dataset. We trained a single model using this training set and verified that its
performance is similar to that achieved by the system we are proposing (Figure 19), which creates
and trains a new model when a new drift occurs. However, this simple model is not realistic and
cannot be applied in real-world contexts because it has the advantage of immediately analyzing
data samples from the entire history of the stream. It is not realistic because no model can ‘look’
into the future. The objective is only to test whether the detected changes are present in the

ACM Trans. Recomm. Syst., Vol. 3, No. 2, Article 24. Publication date: March 2025.

---

<!-- PAGE 22 -->

24:22

L. Caroprese et al.

Fig. 19. Test performance on the dataset with a model trained on a sample of data.

original dataset or are only a side effect of the model training. Breaking the chronological order of
preferences could heavily impact dataset evaluation: For Yoochoose and Amazon Video Games, it
means changing the order when items ‘appear’ in the system. For the MIND dataset, the side effect
is breaking the correlation between news: a sequence of news on the same event loses meaning,
influencing the performance evaluation. However, this behavior can be accepted considering the
scope of this experiment. The architecture we propose, however, remains competitive with this
‘ideal’ model and matches its performance.

In a further set of experiments, we evaluate whether the approach effectively supports actual
shifts in data distribution. In our approach, we only increase dimensionality when a drift is de-
tected. This means that if no increase in loss is detected, we do not modify the structure of the
current model. Conversely, any increase in the loss is identified as a structural inability of the
model to properly capture user preferences, prompting us to train a new model with updated di-
mensionality.

Figure 20(b) illustrates the test loss trend for the Yoochoose dataset after shuffling the data. In
this case, the dataset no longer demonstrates features that degrade model performance. Essentially,
the model fails to adapt to new items or preferences. A similar trend is observed with the Amazon
dataset.

Figure 20(a), where the focus is on the MIND dataset, presents a contrasting behavior: the
model’s performance worsens upon encountering new items. In this dataset, items typically fol-
low an inherent periodicity due to evolving topics over time. Users tend to read news on the same
topic within a short timeframe before moving on to the next one. Shuffling exacerbates this sce-
nario, leading the framework to adjust by identifying a greater number of regimes.

5 Enabling Full Generation
The rationale of the above analysis is that, by tracking a realistic data stream, it is possible to
devise a sequence of models that can be used to generate a synthetic data stream similar to an
original one. The comparison between the original stream and the synthetic stream in the previous
section allowed us to evaluate the fidelity level of the generator in sampling new data. Clearly,
this framework allows to generate streams with an arbitrary number of regimes, in an arbitrary

ACM Trans. Recomm. Syst., Vol. 3, No. 2, Article 24. Publication date: March 2025.

---

<!-- PAGE 23 -->

Modelling Concept Drift in Dynamic Data Streams for Recommender Systems

24:23

Fig. 20. Test performance on the dataset with a model trained on a sample of data.

Fig. 21. Summary statistics on changes in the regimes detected. The first column refers to the Microsoft
News dataset. The other two columns refer to (original and inverted) Amazon Video Games. The last column
refers to the Yoochoose dataset.

order, and with an arbitrary number of samples. However, this generation can only rely on the
models extracted from the original data stream. This is clearly a limitation since we would like to
generate new regimes that can also deviate from the extracted models. Better, we would like to
devise a general scheme where we can synthesize the matrices associated with each regime, and
even enable changes of these matrices along the shards.

In Figure 21, we present statistical insights into the changes observed in the data from the previ-
ous experiments. The first row provides information about the appearance/disappearance of users
and items across different regimes. It illustrates the dynamic nature of the dataset, where users
and items can appear or vanish over time.

The second row focuses on the feature vectors associated with users and items and how they
evolve across the regimes. While a significant number of components remain stable, indicating
consistent user and item characteristics, certain users undergo substantial changes in their feature
vectors. This suggests shifts in their preferences or characteristics over time.

Additionally, Figures 5, 8, 13, and 14 display other noteworthy changes in the distributions.
These figures provide visual representations of the variations observed in the generated data, re-
flecting shifts in user preferences, trends, or other significant modifications. The number of users
is reported in log-scale on the X -axis, while the number of items is reported in log-scale on the
Y -axis.

In general, the following drift directions can be identified:

— Users can undergo changes in their tastes, leading to shifts in their preferences. This can be
visualized as a rewiring of certain user nodes in the feature graph discussed in Section 3.1.

ACM Trans. Recomm. Syst., Vol. 3, No. 2, Article 24. Publication date: March 2025.

---

<!-- PAGE 24 -->

24:24

L. Caroprese et al.

— New trends may emerge, influencing user preferences. This is directly linked to the structure
of the feature graph and how nodes (representing users and items) are connected within it.
— New users can join the system, expressing their preferences and impacting the underlying
preference distributions. Similarly, new items can be introduced, further altering the
distribution of available items.

— Conversely, some users may leave the system or become inactive, and certain items may
become obsolete. These changes result in modifications to the underlying item distribution.

By understanding and addressing these drift directions, we can effectively capture the dynamics
of user preferences, trends, and the evolution of the item space.

In Algorithm 1, we observed that the generation of new samples (using the generateSamples
procedure) depends on the P and Q matrices, as well as the user/item frequency distributions
q and r . Consequently, if we want to capture the described drifts in the generated preferences,
we need to modify these parameters accordingly. We can develop a versatile stream generator
inspired by the concept of geometric closeness in the BPR model, which can effortlessly integrate
the aforementioned drift models.

To begin, we define a set of nearly orthogonal generating vectors in K-dimensional space, de-
noted as g1, . . . , gh (i.e., designed such that gi · gj ≈ 0, for i (cid:2) j). Conceptually, these vectors
represent clusters of users and items. In practice, we can generate feature vectors pu for users
u (and qi for items i) aligned with a specific generating vector gs . These user and item feature
vectors are created by introducing random variations along the K dimensions based on gs . To gen-
erate preferences, we utilize the generateSamples function, which incorporates random user/item
frequencies q and r accordingly.

Consequently, the aforementioned drifts can be effectively modeled by making appropriate

adjustments to these feature vectors, as described below.

Drifting users: To capture changes in user preferences, we can model the shift in tastes for
a user u with a feature vector pu associated with the generating vector gs . This shift can be
represented as a movement towards a different generating vector gt . Consequently, a new ver-
sion of the user’s feature vector pu can be obtained by combining gs and gt through a linear
combination.

New trends: To incorporate new trends, we introduce changes in the latent dimension K.
Each generating vector gs is extended with additional dimensions, denoted as k (cid:10). User and
item feature vectors are extended accordingly, and this extension affects their geometric
proximity.

Distribution drifts: To account for changes in user and item distributions, we can introduce new
users and items by associating them with a generator vector and generating their respective feature
vectors. Theoretical frequencies in q can be assigned to these new users/items. Alternatively, new
generating vectors gs can be created, allowing for the association of new items/users and the
drift of existing items. User churns and item obsolescence can be modeled by annihilating their
respective frequencies in q and r .

In Algorithm 2, we present a sample generation scheme that summarizes the aforementioned
concepts using a set of policies for preference generation. We identify six main policies, and provide
example implementations for some of these policies. They essentially introduce adjustments to
generating vectors, feature matrices, or frequency distributions. By utilizing the modified feature
matrices and/or frequency distributions, we can generate preferences for the shard associated with
each policy.

ACM Trans. Recomm. Syst., Vol. 3, No. 2, Article 24. Publication date: March 2025.

---

<!-- PAGE 25 -->

Modelling Concept Drift in Dynamic Data Streams for Recommender Systems

24:25

ALGORITHM 2: Stream Generator

Input: Number h of cluster generating vectors; Cluster user size Ns and item size Ms , for 1 ≤ s ≤ h; Number n of initial
preferences to generate; A list of T − 1 policies specific to drifting regimes and preferences to genarate nt

Output: Preference models M(1), . . . , M(T )

and associated preferences R(1), . . . , R(T )

.

6

7

8

9

10

11

12

13

14

15

16

17

18

19

20

21

22

27

28

29

35

36

37

38

39

49

50

51

52

1 M(1), G = generateFeatureMatrices({N1, . . . , Nh }, {M1, . . . , Mh })
2 R(1), q, r = generateSamples(M, n)
3 for each t ∈ {2, . . . , T } do
M(t ) = M(t −1)
4
if the t -th regime contains ’user drift’ with percentage α then

5

M(t ), G = coalesceDrift(α, G, M(t ))

end
if the t -th regime contains ’new trends’ with dimension k then

M(t ), G = directionDrift(α, G, M(t ))

end
if the t -th regime contains ’new users’ with dimension k then

M(t ), q = updateP(a, G, M(t ))

end
if the t -th regime contains ’new items’ with dimension k then

M(t ), r = updateQ(a, G, M(t ))

end
if the t -th regime contains ’users churn’ with percentage α then

q = churnDrift(α, q)

end
if the t -th regime contains ’items expire’ with percentage α then

r = obsolescenceDrift(α, r )

end
R(t ), q, r = generateSamples(M, nt , q, r )

23
24 end
25 Function generateFeatureMatrices({N1, . . . , Nh },{M1, . . . , Mh }):
26

Sample K > h
Generate h orthogonal vectors g1, . . . , gh ∈ RK
for each s ∈ {1, . . . , h } do

for each u ∈ {1, . . . , Ns } and i ∈ {1, . . . , Ms } do Generate two random perturbations of gs as pu and qi

Let gs be the generating vector associated with u.
Randomly sample gt with t (cid:2) s from G and β ∈ [0, 1]
gh+1 = β gs + (1 − β )gt ; Add gh+1 to G
Generate a random perturbations of gt as p(cid:10)

u and update pu as β ps + (1 − β )p(cid:10)

u

43

44

extend gs with k new random dimensions
for each u ∈ {1, . . . , Ns } and i ∈ {1, . . . , Ms } do extend pu and qi by using the random perturbations from the

generating vectors

30

end
return M, {g1, . . . , gh }
31
32 Function coalesceDrift(α , G, M):
Sample α % users from U into U (cid:10)
33
for each u ∈ U (cid:10)

do

34

end
return M, G

40
41 Function directionDrift(k , G, M):
42

for each s ∈ {1, . . . , h } do

45

end
return M, G
46
47 Function updateP(k, G, M):
48

end
return M, q

53
54 Function obsolescenceDrift(α , r ):
Sample α % users from U into U (cid:10)
55
for each u ∈ U (cid:10)
return M, q

56

57

Sample k generating vectors with replacement from G into G(cid:10)
for each g ∈ G(cid:10)

do

Generate a random perturbation of g as pu where u is a new user associated with g
Sample a random Zipf frequency qu

do update ru by multiplying it with a random decay w

ACM Trans. Recomm. Syst., Vol. 3, No. 2, Article 24. Publication date: March 2025.

---

<!-- PAGE 26 -->

24:26

6 Conclusions

L. Caroprese et al.

In this study, we introduced a technique for modeling user/item preferences and their evolution
over time using a dynamic tripartite graph representation. This graph is constructed as a sequence
of MF models trained on the source data stream, with each model capturing the properties and data
distribution of a specific regime. The transition from one model to another occurs when a concept
drift is detected.

We explored this concept in two main directions. Firstly, we utilized the learned sequence of
models to generate synthetic data streams that exhibit similar properties to the original data. This
approach enables the generation of realistic synthetic data streams, facilitating the development of
more efficient and accurate recommendation systems. The experimental evaluation demonstrated
the effectiveness of our approach in generating data streams that accurately reflect the dynamics
of the underlying data distribution.

Building upon the insights from the preliminary study, we developed a more general approach
capable of mapping specific drifting operations to changes in the underlying tripartite graphs.
These changes can be parameterized, allowing for controlled data generation strategies where
various drifting strategies can be implemented by manipulating the tripartite graph.

It is worth noting that our proposed approach is based on a specific preference model that as-
sumes geometric closeness of users and items in the latent embedding space as a measure of inter-
action. As a direction for future research, it would be interesting to adapt the proposed scheme to
other preference modeling strategies that do not rely on geometric closeness. For instance, explor-
ing how the model can be tuned to work with Markovian models where preferences are correlated,
and previous interactions can influence a user’s future preferences.

Another fascinating topic is the study of strategies for managing new users and/or items. For
instance, a new type of node could be added to the graph (Figure 1) to account for new entries and
apply targeted strategies to model the behavior of new users effectively. Similarly, for items, one
could consider incorporating business logic, such as prioritizing new, more profitable items. Also,
these strategies could be considered a viable solution to the cold-start problem of the recommender
system.

References
[1] Charu C. Aggarwal. 2016. Recommender Systems. Springer.
[2] Marie Al-Ghossein, Talel Abdessalem, and Anthony Barré. 2021. A survey on stream-based recommender systems.

ACM Computing Surveys 54, 5, Article 104 (2021), 1–36.

[3] Manuel Baena-García, José del Campo-Ávila, Raul Fidalgo, Albert Bifet, Ricard Gavalda, and Rafael Morales-Bueno.
2006. Early drift detection method. In Proceedings of the 4th International Workshop on Knowledge Discovery from Data
Streams. Citeseer, 77–86.

[4] Cigdem Bakir. 2018. Collaborative filtering with temporal dynamics with using singular value decomposition. Tehnički

Vjesnik 25, 1 (2018), 130–135.

[5] Nicola Barbieri, Giuseppe Manco, and Ettore Ritacco. 2014. Probabilistic Approaches to Recommendations. Morgan and

Claypool Publishers.

[6] Francois Belletti, Karthik Lakshmanan, Walid Krichene, Yi-Fan Chen, and John Anderson. 2019. Scalable realistic rec-
ommendation datasets through fractal expansions. arXiv:1901.08910. Retrieved from https://arxiv.org/abs/1901.08910
[7] James Bennett, Charles Elkan, Bing Liu, Padhraic Smyth, and Domonkos Tikk. 2007. KDD cup and workshop 2007.

ACM SIGKDD Explorations Newsletter 9, 2 (2007), 51–52.

[8] Albert Bifet and Ricard Gavalda. 2007. Learning from time-changing data with adaptive windowing. In Proceedings of

the 2007 SIAM International Conference on Data Mining. SIAM, 443–448.

[9] María del Carmen Rodríguez-Hernández, Sergio Ilarri, Ramón Hermoso, and Raquel Trillo-Lado. 2017. DataGenCARS:
A generator of synthetic data for the evaluation of context-aware recommendation systems. Pervasive and Mobile
Computing 38 (2017), 516–541.

[10] Jörg Drechsler and Jerome P. Reiter. 2011. An empirical evaluation of easily implemented, nonparametric methods for

generating synthetic datasets. Computational Statistics and Data Analysis 55, 12 (2011), 3232–3243.

ACM Trans. Recomm. Syst., Vol. 3, No. 2, Article 24. Publication date: March 2025.

---

<!-- PAGE 27 -->

Modelling Concept Drift in Dynamic Data Streams for Recommender Systems

24:27

[11] Eduardo Ferreira José, Fabricio Enembreck, and Jean Paul Barddal. 2020. ADADRIFT: An adaptive learning technique
for long-history stream-based recommender systems. In Proceedings of the 2020 IEEE International Conference on Sys-
tems, Man, and Cybernetics (SMC’20). 2593–2600.

[12] Isvani Frías-Blanco, José del Campo-Ávila, Gonzalo Ramos-Jiménez, Rafael Morales-Bueno, Agustín Ortiz-Díaz, and
Yailé Caballero-Mota. 2015. Online and non-parametric drift detection methods based on hoeffding’s bounds. IEEE
Transactions on Knowledge and Data Engineering 27, 3 (2015), 810–823. DOI:
https://doi.org/10.1109/TKDE.2014.
2345382

[13] Joao Gama. 2010. Knowledge Discovery from Data Streams. Chapman and Hall/CRC.
[14] Joao Gama, Pedro Medas, Gladys Castillo, and Pedro Rodrigues. 2004. Learning with drift detection. In Proceedings of

the Brazilian Symposium on Artificial Intelligence. Springer, 286–295.

[15] João Gama, Indre Žliobaite, Albert Bifet, Mykola Pechenizkiy, and Abdelhamid Bouchachia. 2014. A survey on concept

drift adaptation. ACM Computing Surveys 46, 4 (2014), 1–37.

[16] Heitor M. Gomes, Albert Bifet, Jesse Read, Jean Paul Barddal, Fabrício Enembreck, Bernhard Pfharinger, Geoff Holmes,
and Talel Abdessalem. 2017. Adaptive random forests for evolving data stream classification. Machine Learning 106,
9 (2017), 1469–1495.

[17] Heitor Murilo Gomes, Jesse Read, Albert Bifet, Jean Paul Barddal, and João Gama. 2019. Machine learning for streaming
data: State-of-the-art, challenges, and opportunities. ACM SIGKDD Explorations Newsletter 21, 2 (2019), 6–22.
[18] X. Han, C. Zhu, X. Hu, C. Qin, X. Zhao, and H. Zhu. 2024. Adapting job recommendations to user preference drift
with behavioral-semantic fusion learning. In Proceedings of the 30th ACM SIGKDD Conference on Knowledge Discovery
and Data Mining. 1004–1015.

[19] F. Maxwell Harper and Joseph A. Konstan. 2015. The MovieLens datasets: History and context. ACM Transactions on

Interactive Intelligent Systems 5, 4 (2015), 1–19.

[20] Myles Hollander, Douglas A. Wolfe, and Eric Chicken. 2014. Nonparametric Statistical Methods. John Wiley and Sons.
[21] Martin Jakomin, Tomaž Curk, and Zoran Bosnić. 2018. Generating inter-dependent data streams for recommender

systems. Simulation Modelling Practice and Theory 88 (2018), 1–16.

[22] Wang-Cheng Kang and Julian McAuley. 2018. Self-attentive sequential recommendation. In Proceedings of the IEEE

International Conference on Data Mining. IEEE, 197–206.

[23] Anastasiia Klimashevskaia, Dietmar Jannach, Mehdi Elahi, and Christoph Trattner. 2024. A survey on popularity
bias in recommender systems. User Model User-Adap Inter 34 (2024), 1777–1834. https://doi.org/10.1007/s11257-024-
09406-0

[24] Yehuda Koren. 2009. Collaborative filtering with temporal dynamics. In Proceedings of the 15th ACM SIGKDD Interna-

tional Conference on Knowledge Discovery and Data Mining. 447–456.

[25] Lukasz Korycki and Bartosz Krawczyk. 2019. Unsupervised drift detector ensembles for data stream mining. In Pro-
ceedings of the 2019 IEEE International Conference on Data Science and Advanced Analytics (DSAA’19). 317–325.
[26] Jure Leskovec, Anand Rajaraman, and Jeffrey Ullman. 2020. Mining Massive Data. Cambridge University Press.
[27] Elisabeth Lex, Dominik Kowald, and Markus Schedl. 2020. Modeling popularity and temporal drift of music genre

preferences. Transactions of the International Society for Music Information Retrieval 3, 1 (2020), 17–30.

[28] Jiacheng Li, Yujie Wang, and Julian McAuley. 2020. Time interval aware self-attention for sequential recommendation.

In Proceedings of the 13th International Conference on Web Search and Data Mining. 322–330.

[29] Pawel Matuszyk and Myra Spiliopoulou. 2017. Stream-based semi-supervised learning for recommender systems.

Machine Learning 106, 6 (2017), 771–798.

[30] Pawel Matuszyk, João Vinagre, Myra Spiliopoulou, Alípio Mário Jorge, and João Gama. 2018. Forgetting techniques for
stream-based matrix factorization in recommender systems. Knowledge and Information Systems 55, 2 (2018), 275–304.
[31] Diego Monti, Giuseppe Rizzo, and Maurizio Morisio. 2019. All you need is ratings: A clustering approach to synthetic

rating datasets generation. In Proceedings of the REVEAL Workshop at ACM RecSys Conference.

[32] Jianmo Ni, Jiacheng Li, and Julian McAuley. 2019. Justifying recommendations using distantly-labeled reviews and
fine-grained aspects. In Proceedings of the 2019 Conference on Empirical Methods in Natural Language Processing and
the 9th International Joint Conference on Natural Language Processing (EMNLP-IJCNLP’19). 188–197.

[33] Stanley Ade Oyewole. 2021. Image Content-based User Preference Elicitation for Personalised Mobile Recommendation of
Shopping Items. Ph. D. Dissertation. Department of Information Technology, Faculty of Accounting and Informatics,
Durban University of Technology Durban, South Africa.

[34] S. Rendle, C. Freudenthaler, Z. Gantner, and L. Schmidt-Thieme. 2009. BPR: Bayesian personalized ranking from im-

plicit feedback. In Proceedings of the Conference on Uncertainty in Artificial Intelligence (UAI ’09). 452–461.

[35] Francesco Ricci, Lior Rokach, and Bracha Shapira (Eds.). 2015. Recommender Systems Handbook (2nd ed.). Springer

Publishing Company, Incorporated.

[36] Raquel Sebastião and José Maria Fernandes. 2017. Supporting the Page-Hinkley test with empirical mode decompo-
sition for change detection. In Proceedings of the International Symposium on Methodologies for Intelligent Systems.
Springer, 492–498.

ACM Trans. Recomm. Syst., Vol. 3, No. 2, Article 24. Publication date: March 2025.

---

<!-- PAGE 28 -->

24:28

L. Caroprese et al.

[37] Manel Slokom, Martha Larson, and Alan Hanjalic. 2020. Partially synthetic data for recommender systems: Prediction

performance and preference hiding. arXiv:2008.03797. Retrieved from https://arxiv.org/abs/2008.03797

[38] Ricardo Sousa and Joao Gama. 2016. First principle models based dataset generation for multi-target regression and

multi-label classification evaluation. In Proceedings of the STREAMEVOLV@ ECML-PKDD.

[39] Huimin Sun, Jiajie Xu, Kai Zheng, Pengpeng Zhao, Pingfu Chao, and Xiaofang Zhou. 2021. MFNP: A meta-optimized

model for few-shot next POI recommendation. In Proceedings of the IJCAI. 3017–3023.

[40] Tipajin Thaipisutikul. 2022. An adaptive temporal-concept drift model for sequential recommendation. ECTI Transac-

tions on Computer and Information Technology 16, 2 (2022), 222–236.

[41] Karen H. L. Tso and Lars Schmidt-Thieme. 2006. Empirical analysis of attribute-aware recommender system algo-

rithms using synthetic data. J. Comput. 1, 4 (2006), 18–29.

[42] Alexey Tsymbal. 2004. The problem of concept drift: Definitions and related work. Computer Science Department,

Trinity College Dublin 106, 2 (2004), 58.

[43] Bruno Veloso, Luciano Caroprese, Matthias König, Sónia Teixeira, Giuseppe Manco, Holger H. Hoos, and João Gama.
2021. Hyper-parameter optimization for latent spaces. In Proceedings of the ECML/PKDD 2021 European Conference on
Machine Learning and Knowledge Discovery in Databases (Lecture Notes in Computer Science, Vol. 12977). 249–264.
[44] João Vinagre, Alípio Mário Jorge, Conceição Rocha, and Joao Gama. 2021. Statistically robust evaluation of stream-

based recommender systems. IEEE Transactions on Knowledge and Data Engineering 33, 7 (2021), 2971–2982.

[45] João Vinagre, Alípio Mário Jorge, and João Gama. 2018. Online gradient boosting for incremental recommender sys-

tems. In Proceedings of the Discovery Science. 209–223.

[46] Charinya Wangwatcharakul and Sartra Wongthanavasu. 2021. A novel temporal recommender system based on multi-
ple transitions in user preference drift and topic review evolution. Expert Systems with Applications 185 (2021), 115626.
[47] Geoffrey I. Webb, Loong Kuan Lee, François Petitjean, and Bart Goethals. 2017. Understanding concept drift.

arXiv:1704.00362. Retrieved from https://arxiv.org/abs/1704.00362

[48] Taoru Yang, Yong Gao, Zhou Huang, and Yu Liu. 2023. UPTDNet: A user preference transfer and drift network for

cross-city next POI recommendation. International Journal of Intelligent Systems 2023, 1 (2023), 9091570.

[49] Zhengyi Yang, Xiangnan He, Jizhi Zhang, Jiancan Wu, Xin Xin, Jiawei Chen, and Xiang Wang. 2023. A generic learning
framework for sequential recommendation with distribution shifts. In Proceedings of the 46th International ACM SIGIR
Conference on Research and Development in Information Retrieval.

Received 15 December 2022; revised 30 July 2024; accepted 17 September 2024

ACM Trans. Recomm. Syst., Vol. 3, No. 2, Article 24. Publication date: March 2025.

<!-- MARKITDOWN CONVERSION -->

<!-- Full MarkItDown conversion for formatting fidelity. -->

Modelling Concept Drift in Dynamic Data Streams for
Recommender Systems
LUCIANO CAROPRESE,UniversityGabrieled’AnnunzioofChietiandPescara,DepartmentofEngi-
neeringandGeosciences,Pescara,ItalyandICAR-CNR,Rende,Italy
FRANCESCOSERGIOPISANI,ICAR-CNR,Rende,Italy
BRUNOMIGUELVELOSO,UniversidadePortucalense,Porto,PortugalandINESCTEC,Porto,Portu-
gal
MATTHIASKONIG,LeidenUniversity,Leiden,Netherlands
GIUSEPPEMANCO,ICAR-CNR,Rende,Italy
HOLGER HOOS,LeidenUniversity,Leiden,NetherlandsandTheUniversityofBritishColumbia,Van-
couver,Canada
JOAOGAMA,UniversidadePortucalense,Porto,PortugalandINESCTEC,Porto,Portugal
Recommendationsystemsplayacrucialroleinmoderne-commerceandstreamingservices.However,the
limitedavailabilityofpublicdatasetshamperstherapiddevelopmentofmoreefficientandaccuraterecom-
mendationalgorithmswithintheresearchcommunity.Thisworkintroducesastream-baseddatagenerator
designedtogenerateuserpreferencesforasetofitemswhileaccommodatingprogressivechangesinuser
preferences.Theunderlyingprincipleinvolvesusinguser/itemembeddingstoderivepreferencesbyexplor-
ingtheproximityoftheseembeddings.Whetherrandomlygeneratedorlearnedfromarealfinitedatastream,
theseembeddingsserveasthebasisforgeneratingnewpreferences.Weinvestigatehowthisfundamental
modelcanadapttoshiftsinuserbehaviorovertime;inourframework,changescorrespondtoalterations
inthestructureofthetripartitegraph,reflectingmodificationsintheunderlyingembeddings.Throughan
analysisofreal-lifedatastreams,wedemonstratethattheproposedmodeliseffectiveincapturingactual
preferencesandthechangesthattheycanexhibitovertime.Thus,wecharacterizethesechangesandde-
velopageneralizedmethodcapableofsimulatingrealisticdata,therebygeneratingstreamswithsimilaryet
controllabledriftdynamics.
CCSConcepts:•Informationsystems→Retrievalmodelsandranking;
ThisworkwaspartiallysupportedbyProject“SERICS-SEcurityandRIghtsIntheCyberSpace”(PE00000014)andpartially
bytheEUH2020ICT48project“HumanE-AI-Net”undercontract#952026.
Authors’ContactInformation:LucianoCaroprese,UniversityGabrieled’AnnunzioofChietiandPescara,Department
ofEngineeringandGeosciences,Pescara,ItalyandICAR-CNR,Rende,Calabria,Italy;e-mail:luciano.caroprese@unich.it;
FrancescoSergioPisani,ICAR-CNR,Rende,Calabria,Italy;e-mail:francescosergio.pisani@icar.cnr.it;BrunoMiguelVeloso,
UniversidadePortucalense,Porto,PortugalandINESCTEC,Porto,Portugal;e-mail:bveloso@fep.up.pt;MatthiasKonig,
LeidenUniversity,Leiden,Netherlands;e-mail:h.m.t.konig@liacs.leidenuniv.nl;GiuseppeManco,ICAR-CNR,Rende,Cal-
abria,Italy;e-mail:giuseppe.manco@icar.cnr.it;HolgerHoos,LeidenUniversity,Leiden,NetherlandsandTheUniversity
ofBritishColumbia,Vancouver,BritishColumbia,Canada;e-mail:h.h.hoos@liacs.leidenuniv.nl;JoaoGama,Universidade
Portucalense,Porto,PortugalandINESCTEC,Porto,Portugal;e-mail:jgama@fep.up.pt.
This work is licensed under a Creative Commons Attribution International 4.0 License.
©2025Copyrightheldbytheowner/author(s).
ACM2770-6699/2025/03-ART24
https://doi.org/10.1145/3707693
ACMTrans.Recomm.Syst.,Vol.3,No.2,Article24.Publicationdate:March2025.

24:2 L.Caropreseetal.
AdditionalKeyWordsandPhrases:Recommendersystems,collaborativefiltering,conceptdriftadaptation,
datageneration
ACMReferenceFormat:
LucianoCaroprese,FrancescoSergioPisani,BrunoMiguelVeloso,MatthiasKonig,GiuseppeManco,Holger
Hoos,andJoaoGama.2025.ModellingConceptDriftinDynamicDataStreamsforRecommenderSystems.
ACMTrans.Recomm.Syst.3,2,Article24(March2025),28pages.https://doi.org/10.1145/3707693
1 Introduction
Modernmachinelearningapplicationsandsystemsneedtodealwithlargeamountsofcontinuous
dataintheformofdatastreams.Mostreal-lifeapplicationscenariosrequiretheanalysisoflarge
volumes of data whose properties or distribution can change and evolve. Notable examples
are e-commerce and streaming platforms, which contain catalogs counting thousands or even
millions of products or items, where user preferences and purchasing/adoption behavior can
evolveovertimeaccordingtochangesinthecatalog.DataStreamMining[13,17,26]represents
thesetoftechniquesandmethodsthatenabledataanalysisfulfillingthefollowingcharacteristics:
(a)Highamountsofdatacominginaninfinitestream[26];(b)ConceptDrifting[15,42,47],i.e.,
datachangeorevolveovertime;(c)Highvolatility,thatpreventsthepossibilityofstoringthedata
andcallsforonlinemethodswheredataisanalyzedassoonasitreceivedanditisdiscardedor
summarised.
Besides traditional supervised [16] or unsupervised [25] learning problems on data streams,
recommendation can be considered an extremely significant landscape for data stream mining.
The massive amount of information available to users in the form of digital catalogs and online
services requires the capability to appropriately select relevant content and filter out irrelevant
data. Understanding and predicting users’ choices and preferences is thus a challenging task
and Recommender Systems (RS) play a crucial role in modeling complex situations, where
priorbeliefs,specifictendencies,andreciprocalinfluencesjointlycontributetodeterminingsuch
preferences[1,5,35].
Notably, although the field has been extensively studied and several techniques and methods
wereproposedintheliterature,thereisasignificantgapbetweenresearchalgorithmsandmodels,
and real-life industrial deployment of RS. In fact, the former are often based on the unrealistic
assumption that preferences are static and do not tend to change over time. As a consequence,
the studies essentially focus on static datasets collected over relatively long periods, and build
preference models that tend to be periodically updated. This perspective has obviously several
limitations,asitignoresthestreamingnatureofpreferencedataandconsequentlythecontinuous
evolutionoftheinteractions,dueeithertocatalogupdates,userchurnornewacquisitions,and
evolving tastes or preferences. This problem has been recently at the center of the attention of
current research [2] and some initial attempts were made to devise more sophisticated models
capableofcapturingthedynamicnatureofpreferences[11,29,30,43,45].
Inthisarticle,weaddresstheproblemoftheshortageofsufficientlylargepublicdatasetswith
realproperties,neededtotrainandevaluatemodernrecommendationsystems.Whenevaluating
recommendationsystemsinastreamingscenario[44],asignificantchallengearises:Howcanwe
effectivelyassesstherobustnessofadvancedmachinelearningsystemsandquantifytheirperfor-
manceinacontrolledexperimentalbenchmarkingenvironment,whereallthecharacteristicsof
thedatacanbeappropriatelytunedandthealgorithmicresponsecanbeevaluatedaccordingly?
Thisproblemischallengingforanumberofrelevantreasons.Themostimportantisthatobtaining
large-scale public repositories that represent interaction datasets is difficult, due to inherent
ACMTrans.Recomm.Syst.,Vol.3,No.2,Article24.Publicationdate:March2025.

ModellingConceptDriftinDynamicDataStreamsforRecommenderSystems 24:3
privacy and technological concerns associated with their sharing. In fact, the available datasets
suchasAmazon[32],Netflix[7],orMovieLens[19]areordersofmagnitudesmallerthanpropri-
etary data and typically contain data collected in a limited period where preferences have been
collected.Syntheticdatageneratorscanhelpusalleviatethisproblembyprovidingad-hocdatasets
wherethedatacharacteristics(numberofusers/items,numberofinteractions,datadistributions)
can be manipulated and the algorithmic robustness compared according to such manipulations.
However,existingdatagenerationmethodsdonottakeintoaccountthedynamicnatureofthedata
distribution,whichislikelytooccurinastreamingscenarioandinthepresenceofevolvingprefer-
encesalongthetimedimension.Thissituationisfurtherexacerbatedbythelackofgeneralmodels
fordistributiondynamics,whichshouldinsteadbeaccuratelystudiedandcorrelatedtoalgorithmic
responses.
Inpractice,syntheticdatagenerationthataccountsfordriftsinacontinuousstreamingscenario
needstoaddressthefollowingchallenges:
(1) First, we need to hypothesize a preference model that can realistically characterize item
adoptionanduserpreferences.Thismodelshouldserveasthebasisforthedatageneration
processwithoutintroducinganybiasthatisnotactuallyobservableinrealdata.
(2) Second,weneedtoconsiderallpossiblechangesthatcancauseadriftwithinthepreferences.
Drifts can be abrupt or progressive, they can involve a percentage of users/items or the
whole population, and they can be caused by new emerging trends or by changes in the
characteristicsofusers/items.Alltheseaspectsneedtobemodeled,andthedatageneration
processneedstoembedthem.
Inordertodealwiththeaboveissues,weproposeageneralpreferencemodelthatcaneasily
adapttocoverpreferencedynamics.Wefocusmainlyonimplicitpreferences:Givenauser/item
pair,apreferenceisabinaryresponseexpressingthefactthattheuseradopted/didnotadoptthe
item.Thissimplerepresentationschemenaturallyinducesaper-userorderingamongitems,which
can,hence,berankedaccordingtotheadoptionlikelihood.Ourbasicassumptionisthatbothusers
anditemsmaptoanunderlyinglatentlow-dimensionalmanifold,andpreferencesessentiallyoc-
cur due to closeness within this latent space. Notably, this interaction can be made explicit by
uncoveringthelatentspaceandmodelingtheinteractionsasatripartitegraphconnectingusers,
latentspacedimensions,anditems.Asaconsequence,preferencedynamicscanbeeasilymadeex-
plicitbysuitablemodificationsofthelatentembeddings,whichinturnrepresentmodificationsof
theunderlyinggraph,asaddition/deletionofnodesorchangesintheconnectivity,thusproducing
realisticevolvingpreferencedatastreamswithcharacteristicsthatchangeovertime(conceptdrift).
Amajorchallengeisquantifyinghowrealisticapreferencemodeliswhendriftsarerepresented
aschangesintheunderlyingembeddings.Weapproachthisbyinvestigatingthebehaviorofthe
underlyingmodelonrealisticdatastreamsandstudyinghowitcaneffectivelyreplicatereal-data
distributions.Inpractice,inourevaluation,weadoptaschemewhere(i)driftscanbeidentifiedin
realdatabyobservingthemodel’sinabilitytocapturerealisticpreferences,and(ii)themodelauto-
maticallyadjustsbymakingminimalchangestothegraphstructuretoalignactualandgenerated
preferences.Inourscenario,theoptimaladjustmentsarethosethatcanaccuratelypredictactual
preferenceswithminimalerror,eveninthepresenceofconceptdrift.Notably,theanalysisofreal
dataalsoallowsustodeviseandcharacterizethechangesthattypicallycanoccur,thusdevising
afullygenerativemodelforsyntheticyetrealisticpreferencedatathatcanalsobecharacterized
bypreferencedynamics.
Tosummarize,themaincontributionsofthearticleare
—A preference model based on latent embeddings. According to such a model, concept
drifts can be modeled as major modifications of the embeddings, that can be deemed as
ACMTrans.Recomm.Syst.,Vol.3,No.2,Article24.Publicationdate:March2025.

24:4 L.Caropreseetal.
rewiringchangesintheunderlyingtripartitegraph.Weshowthatthismodeliscapableof
characterizing real-data distributions and can hence be used as a basis for synthetic data
generation.
—A stream-based data generator that can produce preference data also characterized by
preference dynamics. We study a categorization of the possible drifts that can occur
withinpreferences.Tothebestofourknowledge,thisisthefirstattempttosystematically
approachtheproblemandproposeasolution.
The remaining sections of this article are organized as follows. Section 2 presents a systematic
literaturereviewonsyntheticdatageneratorsforRS.InSection3,weformulatetheproblemof
generating synthetic data and propose an algorithm for detecting drifts in preference data. Sec-
tion4providesdetailsonexperimentsconductedusingrealdataanddiscussestheapplicationof
learnedmodelsforemulatingadatagenerationprocess.Section5introducesageneraldatagener-
ationschemebasedontheinsightsobtainedfromtheexperiments.Finally,inSection6,wedraw
generalconclusionsandoutlinefutureresearchdirections.
2 RelatedWork
Generating synthetic data streams is not entirely novel and has been proposed in the past for
general machine learning tasks, such as classification and regression [8, 38]. However, previous
researchonsyntheticdatastreamsforrecommendationsystemsislimitedandhighlyfragmented,
tacklingdifferentdataissuessuchasuserprivacy[37],scalability,shortageofbenchmarks[6,9,
31,41],and,mostcloselyrelatedtothiswork,conceptchanges[21].
IntheworkbySlokometal.[37],theauthorspresentamethodtohidecertainpreference-related
user information from a set of user-item interactions, which otherwisecould be accessed. Their
approachemploystheCARTalgorithm[10],andtheoutputisasetofsynthesizedpreferencedata,
which preserves crucial statistical properties of the original data in order to be helpful for the
testingofrecommendationalgorithmsbuthidesspecificuserinformation,suchastheirfavorite
actor in the case of movie recommendation. However, their method is unable to generate new
ratingsforunseenitems,anditisuncleartowhatextenttheirapproachcangenerateincremental
dataorproducedatastreamswithdynamicallychangingcharacteristics.
ThesamelimitationholdsfortheworkbyBellettietal.[6].Theauthorsemployadatagenerator
toproducearealisticcopyoftheMovieLensdatasetbutwithaheavilyextendednumberofusers,
items, and ratings. While this approach successfully scales up the MovieLens dataset by several
orders of magnitude, therefore overcoming scalability, it does not address the issue of dynamic
changes in user preferences. In other words, there are no parameters in the generation process
that control drift in the data. In their study, Tso and Schmidt-Thieme [41] propose a synthetic
data generation methodology to examine the performance of attribute-aware algorithms. They
manipulatethelevelofinformativenessofattributesintheirartificialdatasetstostudytheirim-
pactonalgorithmbehavior.Inthedomainofcontext-awarerecommendationsystems,delCarmen
Rodríguez-Hernándezetal.[9]developedasystemspecificallydesignedforgeneratingpreference
datathatincorporatescontextualinformation.Theiraimwastoaddressthelackofsuitablebench-
marksinthisareaofresearch.Interestingly,theirgeneratorcanmixrealandsyntheticdataand,
thus, mimic properties from existing datasets. However, a change in the data, e.g., user taste, is
notconsideredinthegenerationprocess.ThesameholdsfortheworkofMontietal.[31],who
present a cluster-based data generation method that learns the rating behavior of specific user
communitiesandusesthisinformationtogeneratenewratings.
IntheworkofKoren[24],theauthorsproposedtocapturethetemporaldynamicsofuserpref-
erences.Morespecifically,theytriedtomodelgradualandsuddendriftsusinglinearandspline
ACMTrans.Recomm.Syst.,Vol.3,No.2,Article24.Publicationdate:March2025.

ModellingConceptDriftinDynamicDataStreamsforRecommenderSystems 24:5
modelingofuserbiases.Theyalsoexploredtheimpactofdayeffectsonthebias.Theresultsshow
that the splines are more flexible in capturing user effects on gradual drifts, and the single-day
effectsareusefulforcapturingsuddendrifts.Similarly,theworkofBakir[4]describestheadop-
tionofamatrixfactorization(MF)modelusingSVD,andtomapthetemporaldynamics,the
authorsproposedtheapplicationofaconversionfunctionusedforthecalculationoftheageof
the ratings, giving more weight to more recent ratings and slowly forget old preferences. The
authorsassumedthatagradualtransitionexistsintheusers’preferences.Withtheincreaseofin-
terestindeeplearningmodels(embedding),researchersdevelopedsomesolutionsforasequential
recommendation.
Inparticular,[28]usedself-attentionmechanismstocaptureinteractionsbetweentwowatched
itemsinpredefinedtimeintervals.AnotherapproachproposedbyKangandMcAuley[22]assigns
weights to watched items to forget past interactions or give relevance to them. In both cases,
the authorsare trying to model the changes in user preferences. Our work not only models the
users’preferencesbutalsoiscapableofgeneratingartificialdriftsorproducingsyntheticdatawith
similardatadistributions.
ArecentworkproposedbyVelosoetal.[43]modelsuserpreferencesusingincrementallyup-
dated embeddings. The proposed model is equipped with a drift detector to capture changes in
users’ preferences and initiate a real-time optimization task. The main idea is that every time
during the learning process a drift is detected, the model needs to be adjusted by changing its
hyperparameters.
Regarding drift detectors, there are several solutions available in the literature. Drift Detec-
tionMethod(DDM)proposedbyGamaetal.[14]observesthelearnererrorrateandassumes
thatwith theincreaseof observedexamples, theerror ratewill decreasesince thedata distribu-
tionisstationary.Iftheerrorrateincreasesaboveaspecificthresholdcalculatedbasedontheerror
rate and standard deviation at one specific instant, it will trigger one alarm. Another variant of
thismethodcalledtheEarlyDriftDetectionMethod(EDDM),proposedbyBaena-Garcíaetal.
[3],wasdevelopedtoimprovedetectionperformanceundergradualconceptdrifts.Theauthors
proposedadoptingrunningaveragedistanceandrunningstandarddeviationsinsteadofcalculat-
ingthevaluesatspecificinstants.TheHoeffdingDriftDetectionMethod(HDDM)proposed
byFrías-Blancoetal.[12]workswithadifferentprinciple.ItusestheHoeffdingsinequalityanda
movingaveragetesttodetecttheconceptdrifts.ThePage–HinkleymethodproposedbySebastião
andFernandes[36]detectschangesusingtheCUSUMcontrolchartandcomputestheobserved
valuesandtheirmeanuntilthecurrentinstant.Ifthereisachange(increasingordecreasingthe
mean),itwillsignalanalarmbasedonapredefinedthreshold.Finally,theAdaptiveWindowing
(ADWIN) method proposed by Bifet and Gavalda [8] uses a dynamic-sized window that keeps
recent examples with the same data distribution. The window can be split into two parts and
comparedifthedatadistributionisthesameonbothsub-windows,signalinganalarmifthiscon-
ditionisinvalid.ThefocusofthisworkisnottodevelopnewDDMsbuttousethemtoidentify
thechangesinthedatadistributionsandbuildaportfolioofmodels.
Lex et al. [27] propose the adoption of Base-Level Learning (BLL) equations from the
cognitivearchitectureACT-Rtogetherwithrecency-basedmodelingofmusicgenrepreferences,
whichindicatesatendencyforindividualstolistentogenrestheyhaverecentlyencountered.The
significanceoftemporaldriftinmusicgenrepreferencesappearsinallusergroups.Consequently,
incorporatingrecencyinformationisexpectedtoenhancepredictionaccuracy.Similarly,Oyewole
[33]introducedamodelforusertemporalpreferencesdesignedtoascertaintherecencyweight
of an item, thereby capturing shifts in user preferences over time. The core principle of this
time-weightedalgorithmisthedeterminationofappropriateweightsforallitems,ensuringthat
ACMTrans.Recomm.Syst.,Vol.3,No.2,Article24.Publicationdate:March2025.

24:6 L.Caropreseetal.
morerecentlypurchaseditemshaveamoresignificantinfluenceonsubsequentrecommendations.
Consequently, items purchased more recently are typically assigned higher weight values than
thosepurchasedearlier.
Hanetal.[18]proposeahypergraphwaveletlearningmethodologytocapturethesubtledrifts
in job preferences. To address the impact of noise in interactions, which is often a consequence
of frequent preference changes (drifts), they introduce an adaptive wavelet filtering technique
designedtoeliminatethesenoisyinteractions.
AccordingtoSunetal.[39],therecommendationforeachuserisconceptualizedasanindividual
learning task that aims at capturing region-independent personal preferences by utilizing their
check-indatawithoutconsideringspecificregions.Understandingusers’immediatedemandsand
modelingshort-termpreferencesarecrucialforthesubsequentrecommendation.Toachievethis,
theyemploysequentialmodelstorepresentusers’personalpreferences,therebyexploringtheir
behaviorpatternsthroughtheircompletecheck-insequencesusingLSTMmodels.
Thaipisutikul[40]integratescontextualinformationintothesubspacedecompositionofshort-
term and long-term memory units within the Long Short-Term Memory (LSTM) framework.
Specifically,theyintroduceamechanismtoattenuatetheinfluenceofthememorycellsuchthat
as time progresses or concept drift occurs, the impact of prior memory on the current output
diminishes.
Yang et al. [48] employ a recurrent neural network (RNN)-based model to generate short-
term user preferences, incorporating dual branches specifically designed for preference transfer
and drift. The transfer branch and the Point of Interest (POI) embedding vectors are shared
betweentouristsandresidentswithinthecurrentcity.Incontrast,thedriftbranchcapturesvaria-
tionsinpreferencesamongdifferentuserroles,includingatouristintheirhomecity,atouristin
thecurrentcity,andaresidentinthecurrentcity.
Wangwatcharakul and Wongthanavasu [46] propose a model that learns multi-transition
low-dimensionalfactorstoeffectivelycapturevariationsinuserinterestsacrossdifferentperiods.
The model emphasizes the importance of temporal influences, noting that a well-designed
algorithm should progressively diminish the impact of older data while maintaining accuracy
in predicting future user preferences. Initially, the model calculates the rating shift rate using
a time decay function that accounts for the forgotten information. Subsequently, it captures
the latent drift in user factors between successive time points to monitor the multi-transition
factors.
To our knowledge, the work of Jakomin et al. [21] is the only one that addresses incremen-
tal changes in the data. In this study, the authors present a method to generate multiple inter-
dependent data streams to evaluate recommendation or data fusion algorithms. The main idea
behindtheirgeneratoristosimulatescenarioswheregroupsofsimilarusersrategroupsofsim-
ilaritemsinthesamemanner.Inotherwords,differentprobabilitiesconnecttheresultingusers
anditemclusters.Theseprobabilitiesdeterminetheratingsthatusersofagivenuserclusterwould
giveanitemofagivenitemcluster.Theoutputisaratingmatrixwhereeachnon-zerocellrep-
resents the relation between a particular user and an item. Using arithmetic operations such as
multiplication or division to the ratings at a given time allows them to simulate concept drift.
However,thisrepresentsalimitation,asitdoesnotconsiderchangesinthelatentfeaturespace;
i.e.,theembeddingremainsatasimilarsize,andusersanditemsremainconnectedtothesame
featuresasthedataevolves.Ourworkdiffersfromtheliteratureinthefollowingaspects:(i)We
modeltheuser/itempreferencesandtheirevolutionovertimeasadynamictripartitegraph;(ii)
Welearnfromarealdatastreamasequenceoflatentmatricesthatmodelsthisgraph,and,lastly,
(iii)Weusethissequencetoproducesyntheticdatastreamswhosepropertiesaresimilartothose
oftheoriginalone.
ACMTrans.Recomm.Syst.,Vol.3,No.2,Article24.Publicationdate:March2025.

ModellingConceptDriftinDynamicDataStreamsforRecommenderSystems 24:7
3 DataStreamModelling
Theproposeddatageneratorcanproducesyntheticstreamsofpreferencedatabasedonagraph
learned from real data. The generation process and the drift operations will be explained in the
followingsections.
3.1 BasicFramework
We start by introducing the notation to be used throughout the remainder of this article. In the
following,u ∈U = {1,...,N} indexesauser,andi ∈ I = {1,...,M} indexesanitemforwhich
ausercanexpressapreference.Letr ∈ {r ,...,r }denotesthepreference(rating)ofuser
u,i min max
u for itemi. The range {r ,...,r } represents a preference rank: Whenr = r , useru
min max u,i min
maximally dislikes item i, while r = r denotes maximal preference for the item. Typical
u,i max
ranges are {0,1} (implicit preference) or {1,...,5}. In the following, we shall focus on implicit
preferences.
The set of all preferences can be represented as a rating matrix R, or alternatively, as a set
of triplets R = {(u ,i ,r ),...,(u ,i ,r )}, where each triplet (u ,i ,r ) represents an inter-
1 1 1 n n n j j j
action between any user u and any item i , with r = r being the corresponding rating.
j j j uj,ij
When N and M are large, R only represents a partial and extremely small view of all possible
ratings.
WeadoptanMFframeworkforpredictingthescorethatauseru assignstoeachitemi.Each
useruanditemiadmitarepresentationinaK-dimensionalspace.Wedenotesuchrepresentations
byembeddingvectorsp ,q
∈RK,whichrepresenttherowsoftheembeddingmatricesP∈RN×K
u i
andQ∈RM×K.
Given useru and item i, the corresponding score r can be modeled as a random variable
u,i
withafixeddistributionwhoseparametersrelyontheembeddingsp andq .Thismodelcanbe
u i
represented with a weighted and undirected tripartite graph. It has three types of nodes: Nodes
representingusers(usernodes),thoserepresentingitems(itemnodes),andthoserepresentingfea-
tures(featurenodes).Edgescanonlyconnectuserstofeaturesoritemstofeatures.Theweightof
auser/featureedge(resp.item/featureedge)isameasureofhowstronglythatfeatureispresent
intheuser(resp.item);seeFigure1.
The preference matrixR induces a natural ordering among items, wherei (cid:4) j means thatu
u
prefersi to j, i.e.,r > r . The additional assumption that we make in this work is that the
u,i u,j
partialviewRcanbecontinuouslyupdated.Thatis,eithernewunknownentriescanbedisclosed
(forexample,someuserscanexpresspreferencesforpreviouslyunseenitems)orformerprefer-
enceschange(forexample,duetochangeoftastesbytheuser,orduetoamoreaccurateevalu-
ation). Thus, weassume thatthehistoryofpreferencesproducesacontinuousstreamof shards
R
(1)
,R
(2)
,...,R
(t)
,whereR
(t)
representstheviewofRattimet.
Asalreadymentioned,snapshotscanoverlap,i.e.,itcanhappenthatbothr
(n)
andr
(m)
existfor
(cid:2) u,i u,i
m (cid:2) n, and r u (n ,i ) (cid:2) r u (m ,i ) . We then defin (cid:2) e n≤t R (n) as a merge among R (1) ,R (2) ,...,R (t) that
preserves recency. That is, by denoting n≤t R (n) as V (t) , we define V u ( , t i ) = r u (t , ∗ i ) , where t ∗ =
max{t |(u,i,r )∈R (t)}.Ifnosucht ∗ exists,thenV (t) isundefined.
u,i u,i
Over time, the distribution of data can change, more or less abruptly. When this occurs, we
are facing a concept drift. The situation is illustrated in Figure 2. Typically, we can consider a
streamasthecooperationofmultipleregimesthatinteracttoproduceobservabledata.Aregime
i ischaracterizedbyanunderlyingmodel,describedbyfactorizationmatrices P
(i)
andQ
(i)
.The
appearance of a new regime as a result of a shift in data distribution reflects changes in user
preferencesortheentryofnewfeatures.Asshowninthefigure,thechangesareessentiallydue
tochangesintheunderlyinggraphwhichreflectondifferentsamplesinthedatasamplingprocess.
ACMTrans.Recomm.Syst.,Vol.3,No.2,Article24.Publicationdate:March2025.

24:8 L.Caropreseetal.
Fig.1. User/Feature/Itemgraph.
Fig.2. Regimesinadatastream.
Thechallengeofmanagingnewusersoritemscanbeaddressedbyaddingnewnodesinitialized
withaheuristicfunctionthatconsidersthecharacteristicsofthegraphintheithregime.However,
thisapproachintroducesanadditionallayerofcomplexity.Afeasiblesimplificationistoavoidim-
posingspecificassumptionsandinsteadinitializethenodesrandomly,thenevaluatethevariation
inmodelperformanceacrossdifferentregimes.Thatistheactualimplementation.
Inpractice,theproblemwewanttofaceis howtodeviseadata generationprocessbasedon
factorizationmatricesPandQ,capableofreflectingsuchchanges.Aninitialattemptinthisdirec-
tionwasmadein[43].Moreimportantly,thequestionswewanttoanswerhereare:Whatarethe
typicalchangesthatcharacterizeareal(orrealistic)datastream,andhowcanwemodelthemby
controllable(model-based)adaptationsoftheunderlyingsamplingprocess?
Weapproachthisproblemintwodifferentsteps.Inthefirststep,westudyhowapopularfac-
torizationmodel[34]canbeusedtotrackanddescribechangesinareal-lifedatastream.Forthis,
weproposeaninferencealgorithmthat,givenadatastream,iscapableoftrackingviablechanges
andadaptationsoftheunderlyingmodeltoreflecttheactualstream.Thestudyandcharacteriza-
tionofsuchchangeswillthenallowustodeviseafullycontrollableprocedureforgeneratingdata
streamsexhibitingconceptdrifts.
3.2 LearningConceptDrifts
TheformulationweconsiderisinspiredbytheBayesianPersonalizedRanking(BPR)model
introducedin[34].TheBPRmodelisapopularimplementationforMF-basedmodel,ensuringscal-
ability,trainableonimplicitfeedback(noratingsarerequired).Thetrainingphaseisquiteeffective,
asitisperformedbycomparingpairsofitemsthatauserhasinteractedwithandoptimizingthe
rankingoftheseitems.Thismodelallowsustoprocessdatasetswiththousandsofitemsandusers.
Beinghighlypopularinliterature,itrepresentstheprimarychoicemadebynumerousauthorsin
the field of RS. Moreover, the BPR model is chosen because of its robustness and suitability for
ACMTrans.Recomm.Syst.,Vol.3,No.2,Article24.Publicationdate:March2025.

ModellingConceptDriftinDynamicDataStreamsforRecommenderSystems 24:9
handlingimplicitpreferences.However,thekeyaspectoftheapproachisnotjustthemodelitself
butitsabilitytotrackchangesovertimethroughadjustmentsinthelatentfactormatrices.Inprin-
ciple,anyMFmodelthatsupportsaprobabilisticinterpretationofuser/itemadoptionintermsof
latentfactorscouldbeused.
Theideaunderlyingthismodelisthatapreferencei (cid:4) jcanbedirectlyexplainedascloseness
u
inalatentspacewherebothitemsanduserscanbemapped.Mathematically,thiscanbedevised
bycomputingafactorizationrankpTq foreachpair(u,i),andmodelingprecedencesbymeans
u i
ofaBernoulliprocess:
(cid:3) (cid:4)
i (cid:4) j ∼Bernoulli(p), p =σ pT(q −q ) ,
u u i j
whereσ(a) = (1+e −a)−1 isthelogisticfunction.TheoptimalembeddingsM = (P,Q)canhence
beobtainedbyoptimizingtheloss:
(cid:5)(cid:5) (cid:3) (cid:4)
(cid:2)bpr(M|V)= logσ pT(q −q ) , (1)
u i j
u i,j
i(cid:4) uj
wherei (cid:4) j meansV >V .
u u,i u,j
We can exploit the above learning(cid:6) scheme(cid:7) to devise a sequence(cid:2)of embeddings
M (t1 ) ,...,M (th ) ,... where each M (t) = P (t) ,Q (t) is trained on V (t) (i.e., n≤t R (n) ) as ex-
plained below. In particular, each model of this sequence represents a different regime and
characterizesitsdatadistribution.
Typically, RS are optimized by exploiting historical interactions as training data, to produce
a model that can predict users’ future interactions in the testing data. This scheme inherently
assumesthatthetrainingandtestingdataaredrawnfromthesamedistribution.However,distribu-
tionshiftscanoccurwhenchangesinthepreferences(expressedasmodificationsintheunderlying
graphdiscussedintheprevioussection)occur.Inpractice,amodeltrainedoncurrentdataislikely
todeteriorateitsperformanceonfuturedatawhenasubstantialdriftinthepreferencesoccurs.
TheseobservationsinspireaspecificprotocolfortrainingtheembeddingsM
(t1 )
,...,M
(th )
,...
characterizingthedrift.Thetimestampt
i
hererepresentsthedrift:modelM
(ti−1 )
underperforms
onR
(ti )
and,asaconsequence,weneedtoretrainthemodel.Theideaistodeviseacontinuous
learningframeworkthroughtheshards:ateachstept themodelisoptimizedonV
(t)
.Ifthemodel
substantiallyunderperformsonR
(t)
,thenanadaptationisrequired.Formally,wedefinetheloss
(cid:5)
Lc(M;R)= (cid:2)bpr(M|R)+λ(||P||
∞
+||Q||
∞
)
u∈S
thatincludestheregularizationterm.
ByminimizingtheinfinitynormofPandQ,weenforceanupperboundonthematrixweights
duringthetrainingprocess.Thisensuresthattheweightsbelongtoalimitedrange.
Then, given a current model M, we check whether a drift has occurred by checking the loss
Lc(M;R (t)).
Ifnodriftisdetected,theprocessproceedsintwosteps:
—First,asyntheticinteractiondatasetS isgeneratedfromM.
—Next,MisupdatedbyoptimizingthelossLc(M;S (cid:9)R (t)).
The second step resembles a continual learning strategy [13]. In principle, the model should
be updated from the entireV
(t)
. However, in a streaming scenario, it is impractical to maintain
thewholesetofpastinteractions.ExploitingthecurrentmodeltogenerateasampleS,withthe
same size of R
(t)
, has the advantage of compacting the representation of past interactions and
ACMTrans.Recomm.Syst.,Vol.3,No.2,Article24.Publicationdate:March2025.

24:10 L.Caropreseetal.
additionally, it provides better control on past preference shifts since the model will disregard
obsoleteinteractions.
If a drift is detected, M is obsolete and requires a substantial update. In our framework, this
means that the graph topology can change, with new users/items and/or features. We adopt a
conservativeapproachtotacklingthisproblem.Foragivenuser/featureprobabilityvectorp ∈
u
RK,itispossibletodeviseaninfinite-dimensionalextensionp (cid:10) ∈ R∞ initializedsuchthatp (cid:10) =
u u,k
p if1 ≤ k ≤ K,andp (cid:10) = 0fork > K,andthesamepropertyholdsforitem/featurevector
u,k u,k
(cid:10)
q .Thus,givenM,wedenotebyM itsinfinite-dimensionalcounterpart.Thelearningobjective
i
(cid:10)
onthenewregimecanhencebestatedascomputinganewversionM withminimaldifferences
w.r.t.M.Formally,wedevisetheloss
(cid:8)
(cid:5)(cid:5)K (cid:5)(cid:5)K
Ld(M (cid:10) ;M,R (t))=Lc(M (cid:10) ;R (t))+δ |p (cid:10) −p |+ |q (cid:10) −q |
u,k u,k i,k i,k
u k=1 i k=1 (cid:9)
(cid:5)(cid:5) (cid:5)(cid:5)
+ |p (cid:10) |+ |q (cid:10) |
u,k i,k
u k>K i k>K
thesecondterminthelossrepresentsthedivergencebetweenunderlyingfeaturevectors.Thera-
tionalehereisthattheupdatedmodelshouldpenalizeunnecessarydiscrepancieswiththeprevious
modelonthecurrentfeatures,whileatthesametimelettingthemodelintroducenewfeaturesin
ordertoadapttothecurrentchanges.Inpractice,thetrainingstartsbyaddingΔ newcolumns
K
(initially set to 0) to both P and Q and then optimizing the extended model through Ld on the
new shard R
(t)
. Algorithm 1 provides an overview of the learning procedure. In this procedure,
weutilizethedriftDetectionfunctiontodetectanydriftsinthelosses.Theeffectivenessofdrift
detection heavily relies on the chosen signal, which in our case is primarily the loss values. By
monitoringthelossfunction’svalue,wecanidentifysignificantdeviationsinthemodel’sperfor-
mance,indicatingthepresenceofdrifts.However,itisworthnotingthatthechoiceofthesignal
fordriftdetectioncanvarydependingonthespecificapplicationandproblemdomain,whichcan
leadtodifferentperformancefordetectionalgorithms.WeemploytheHDDM algorithm[12],a
W
well-knownDDMbasedonHoeffding’sboundswithamovingweightedaveragetest.HDDM uti-
W
lizestheExponentiallyWeightedMovingAverage(EWMA)statisticasanestimator.Givena
streamofvalues(inourcase,lossvalues)asinput,itdeterminestheestimatedstatusofthestream:
Stable,Warning,orDrift.1
Therefore,themodelisupdatedusingtwotrainingmodalities:
(cid:10)
—whenadriftoccurs,wetrainthemodelM withthedataofthecurrentshardandpenalize
(cid:10)
thedistancebetweenM andthemodellearnedinthepreviousregimeM;
—otherwise, the current model M is refined on data of the current regime and a sample of
historicaldatageneratedfromthemodelMofthecurrentregime.Thisguaranteesthatthe
modelisawareofbothasummaryofthepreviousdataandthenewdataavailable.
Finally, the generateSamples function leverages the matrix M to generate n new samples.
S
This procedure involves sampling items for each user based on their score, with the probability
of selection proportional to the score. The item frequency for each user (or user frequency
for each item) can be estimated using a Zipf distribution or provided as input to preserve the
originalproperties.Thesefrequencieshelpdeterminethenumberofitemstosampleandbiasthe
probabilityofselectinglow-popularityitems.
1NoticethattheadoptionofHDDMW requiresboundedsignals,whichcanbeguaranteedbyboundingthedifferencein
Equation(1).
ACMTrans.Recomm.Syst.,Vol.3,No.2,Article24.Publicationdate:March2025.

ModellingConceptDriftinDynamicDataStreamsforRecommenderSystems 24:11
Thesampleiscombinedwiththeshard’sdatatotrainthecurrentmodel.Thisapproachaims
atretaininghistoricalinformationwithoutrequiringthestorageofalldatainthecurrentregime,
inthiswaywebalancetheweightofnewpreferencesandthepastones.However,whenadrift
occurs, we switch to a different strategy aimed at minimizing the deviation from the previous
model;therebyreducingtheimpactofthelimitedcurrentdata,i.e.,thepreferencesofthecurrent
shard,onupdatingthenewmodelandpreservingasofttransitionbetweenregimes.Thevalueof
parametern hasbeensetequaltothesizeoftheBtrain setofthecurrentshard,weightingequal
S
tothenumberofpreferencesobservedinthecurrentshardandinthecurrentregime.
4 Experiments
WeconductedanempiricalevaluationofAlgorithm1withtwomainobjectives.Firstly,weaimed
to monitor actual drift in realistic scenarios. Secondly, we aimed to devise a data generator that
captures the properties of realistic data streams and effectively models concept drift similar to
whatisobservedinrealdata.
Weprocessedthreerealdatastreamsusingourproposedapproach.Duringthetrainingphase,
weidentifiedasequenceofregimesforeachdataset,eachcharacterizedbyitsdatadistribution.We
associatedanMFmodelwitheachregime.Usingthissequenceofmodels,wegeneratedasynthetic
datastreamthatcloselyresembledtheoriginalstream.Thiswasachievedbyimposingthesame
regimesinthesameorder,withanequalnumberofsamplesforeachregime.Bycomparingthe
originalandsyntheticstreams,weassessedthefidelityofthegeneratorinsamplingnewdata.
Ourapproachyieldedsatisfactoryresultswhenthenumberofitempreferenceswassufficiently
hightotrainamodelcapableofreplicatingarealstream.Thiswasespeciallyevidentindatasets
where there were numerous items with few preferences and a core set of highly popular items.
Thebehaviorcanbeexplainedbythemodel’sinabilitytoaccuratelyestimatethedistributionof
underrepresented items. To achieve good generation performance, it was crucial to have a suffi-
cientnumberofpreferencesforeachitem.Thisconditionwasnaturallymetwhenthenumberof
userssignificantlyexceededthenumberofitems.Infact,thefirstandthirddatasetssatisfiedthis
condition,asthedistributionofthesyntheticdatacloselyresembledthatoftheoriginaldata.
Wealsochoseaseconddatasetthatdidnotexhibitthisbehavioralpattern,wherethenumberof
userswasmuchsmallerthanthenumberofitems.Inthiscase,thedistributionofthesyntheticdata
generatedbythegeneratordeviatedsignificantlyfromtheoriginaldata. Tofurthersupportour
hypothesis,wereversedtherolesofusersanditemsandrepeatedtheexperiment,demonstrating
the importance of having an adequate number of preferences to derive an effective model. The
resultsweresatisfactoryinthiscase.
Additionally,weselectedathirddatasettoanalyzechangesindistributionsduringadrift.We
drewinsightsfromastudybyYangetal.[49],wheretheytackledthechallengeofdevelopinga
recommendersystemthatcanadapttothedynamicnatureofuserpreferencesanditempopularity.
Tofosterreproducibility,wehavepubliclyreleasedallthedataandcoderequiredtoreproduceour
experiments.2
4.1 Datasets
Our analysis is conducted on the following popular benchmark datasets, each from a different
domainandhavingspecificcharacteristics:
—MicrosoftNews(MIND):ThisdatasetconsistsofnewsarticlespublishedontheMicrosoft
Newswebsiteandthefeedbacklogsgeneratedby1millionusersoveraspanof6days.We
2https://github.com/fsp22/mcd_dds4rs
ACMTrans.Recomm.Syst.,Vol.3,No.2,Article24.Publicationdate:March2025.

24:12 L.Caropreseetal.
ALGORITHM1:LearningLatentMatrices
|     | StreamR=R | (1) (n) |     |
| --- | --------- | ------- | --- |
Input: ,...,R ,...ofpreferencesorderedinshards;numberofsamplesnS to
generatefortrainingthemodelwithinthei-thshard,inconjunctionwiththeshard’sdata.
|         | (0)    | (h)                           |     |
| ------- | ------ | ----------------------------- | --- |
| Output: | AlistM | ,...,M ,...ofpreferencemodels |     |
t =0;(cid:2)=∅
1
| q=∅;r | =∅  |     |     |
| ----- | --- | --- | --- |
2
| initializeM | (t) |     |     |
| ----------- | --- | --- | --- |
3
(i) Rdo
| 4 foreachR | in                    | (cid:3) | (cid:4) |
| ---------- | --------------------- | ------- | ------- |
|            | Btrain,Btest =splitDa | ta (i)  |         |
| 5          |                       | R       |         |
|            | (cid:3)               | (cid:4) |         |
(t)
| 6   | (cid:2)drift =Lc M                          | ;Btest |     |
| --- | ------------------------------------------- | ------ | --- |
| 7   | drift =driftDetection((cid:2)drift,(cid:2)) |        |     |
ifdriftthen
8
|     | (t+1) :=extendModel(M |              | (t) )                 |
| --- | --------------------- | ------------ | --------------------- |
| 9   | M                     |              | ,ΔK                   |
|     | optimizeM             | (t+1) onLd(M | (t+1) ;M (t) ,Btrain) |
10
| 11  | t+=1 |     |     |
| --- | ---- | --- | --- |
end
12
else
13
|     | =generateSam | ples(M  | (t) ,q,(cid:4)r) |
| --- | ------------ | ------- | ---------------- |
| 14  | S,q,r        | (cid:3) | ,nS              |
(t) onLc (t) ;S(cid:9)Btrain
| 15  | optimizeM | M   |     |
| --- | --------- | --- | --- |
16 end
(t)
|     | (cid:2)eval =Lc(M | ;Btest) |     |
| --- | ----------------- | ------- | --- |
17
(cid:2)=(cid:2)∪{(cid:2)eval}
18
(i)
|     | Updateuseranditempopularitiesq,r |     | basedonR |
| --- | -------------------------------- | --- | -------- |
19
20 end (cid:10)
(t)}
| return | {M  |     |     |
| ------ | --- | --- | --- |
| 21     | t   |     |     |
FunctiongenerateSamples(M,nS,q=∅,r =∅,α =1.8,β =1.9,c =1,d =5):
22
23 Functionnormalize(μ):
|     | p˜=σ(c·μ −d) |     |     |
| --- | ------------ | --- | --- |
24
(cid:11)
|     | returnp˜/( | p˜ ) |     |
| --- | ---------- | ---- | --- |
| 25  |            | i i  |     |
ifq=∅then
26
∈U =Zipf(α,1,M/c)
| 27  | foreachu | do qu |     |
| --- | -------- | ----- | --- |
end
28
=∅then
29 ifr
|     | ∈I       | =Zipf(β,1,N/d) |     |
| --- | -------- | -------------- | --- |
| 30  | foreachi | do ri          |     |
end
31
∈U
| 32  | foreachu       | do(cid:11)   |     |
| --- | -------------- | ------------ | --- |
|     | = (cid:13)nSqu | /( )(cid:14) |     |
| 33  | qu             | qu           |     |
u
|     | p˜ =normalize       | (pu ·Q)    |     |
| --- | ------------------- | ---------- | --- |
| 34  | u                   | (cid:11)   |     |
|     | =(p˜ (cid:15)r)/(   | )          |     |
| 35  | pu u                | i p˜ u,iri |     |
| 36  | nu =min(qu,|{i|pu,i | >0}|)      |     |
Samplewithreplacementnu itemsIu fromI withprobabilityproportionaltopu
37
|     | =generateTriplets(u,Iu |     | )   |
| --- | ---------------------- | --- | --- |
| 38  | S                      |     |     |
end
39
40 returnS,q,r
ACMTrans.Recomm.Syst.,Vol.3,No.2,Article24.Publicationdate:March2025.

ModellingConceptDriftinDynamicDataStreamsforRecommenderSystems 24:13
utilizetheclickinformationofeachnewsarticlebyuserstoconstructadataset.Theread
newsarticlesserveasuserpreferences,andweconsideronlyuserswhohaveatleastone
preference(newsread).Thefinaldatasetcomprises19,206itemsand3,958,500preferences
from750,434users.Thedatasetcanbeaccessedathttps://msnews.github.io/.
—Amazon Video Games: This dataset contains ratings provided by users for video games.
The ratings range from 1 to 5. As our approach focuses on implicit feedback, we binarize
thedatabyassigningavalueof1touser-itempairswheretheratingisstrictlygreaterthan
3,and0otherwise.ToaddressGPUmemorylimitations,weprocessasubsetofthedataset,
consideringthelast824,752preferencesfrom26,038usersregisteredoveraspanof10years,
withrespectto567,865items.Thedatasetcanbeaccessedathttp://snap.stanford.edu/data/
amazon/productGraph/categoryFiles/ratings_Video_Games.csv.
—Yoochoose:ThisdatasetwaspublishedfortheRecSysChallenge2015.Itcomprisesacol-
lectionofsessionsfromaretailer,specificallyfocusingonthepurchaseeventsofusers.To
streamlinethedataset,weselecteditemsthatwereinteractedwithmorethan4timesand
removed users with fewer than 3 purchased items. After the cleaning process, the dataset
consistsof143,481users,9,975items,and642,237interactions.Thedatasetcanbeaccessed
athttps://www.kaggle.com/datasets/chadgostopp/recsys-challenge-2015.
These datasets were chosen due to their popularity and diverse characteristics, enabling us to
conductcomprehensiveanalysesanddrawmeaningfulconclusions.
4.2 ModelingDataStreams
FollowingtheprotocolpresentedinSection3,wetestourmodelonthedatasetsreportedinSec-
tion4.1.Foreachuseru andeachitemi whichispositiveforu (i.e.,(u,i,1) ∈ R (t) ),fournegative
itemsjaresampled(i.e.,(u,j,1)(cid:3)R (t) ).Inourframework,weconsiderasnegativeanyitemthatis
notexplicitlypositiveforauser.Thisincludesbothitemsthattheuserhasneverinteractedwith
anditemsthattheuserexplicitlydislikes.Thus,inthiscase,(u,j,1)mustnotbelongtoR (t) which
isdifferentfromsayingthatu dislikesj,i.e.,(u,j,0)mustbelongtoR (t) .
ThisapproachiscommoninRS,particularlywhendealingwithlargeitemcatalogs.Theratio-
nalebehindthismethodliesinthetypicalcharacteristicsofrecommendationscenarios.Inmost
cases,thenumberofitemsauserlikesissignificantlysmallerthanthetotalnumberofavailable
items.Forinstance,inacatalogofmillionsofproducts,ausermightonlybeinterestedinafew
hundred.Thiscreatesaverysparsepreferencematrix.Giventhissparsity,randomlysamplingan
itemhasahighprobabilityofselectingonethattheuserwouldnotlikeorhasnotinteractedwith,
makingitareasonableproxyfornegativefeedback.Thisassumptionsimplifiesthemodelingpro-
cessandisespeciallyusefulwhendetailedinteractiondata(likeviewedbutnotpurchaseditems)
isnotavailable.
Thetriplets(u,i,j)areprocessedinchronologicalordergroupingtheminbatchesof2000tuples.
WespliteachbatchBintwosets:(i)atrainingsetBtrain (70%),and(ii)atestsetBtest (30%).
To train the model, we use 20 epochs; the optimizer is the ADAM algorithm with a learning
rateof0.001,andthelossfunctionsarepresentedinSection3.2.Aftereachbatch,weevaluatethe
model on the test set, and we report some performance metrics. We consider(cid:2)bpr(M|Btest) and
theHit-Ratescore.Letusrecallthedefinitionofthislastmetric:GivenauseruoccurringinBtest,
weconsiderthesetP ofitspositiveitems(i.e.,P = {i | (u,i,j) ∈ Btest})andsampleasetN of
u u u
negativeitems(|N | = 100,inourcase).Thenforagivencutoffk (weusek = 10andk = 5)we
u
considerthek −1negativeitemsinN forwhichMreturnsthehighestscore.Amongthem,we
u
considertheitemj withthelowestscore.Thereisahitwithcutoffk,fortheuseru andtheitem
i ∈P ,ifM(u,i) ≥ M(u,j).Inthefollowing,wereportbothHR@5andHR@10.
u
ACMTrans.Recomm.Syst.,Vol.3,No.2,Article24.Publicationdate:March2025.

24:14 L.Caropreseetal.
Fig.3. LossontestsetpartofeachbatchoftheMicrosoftNewsdataset.
Fig.4. ResultsfortheMicrosoftNewsdataset.
4.3 ExperimentonMIND
Figure3showsthelosscomputedonthetestpartofthecurrentbatch(i.e.,Lbpr(M,Btest))aver-
agedonamovingwindowof20batches.Themovingaveragehighlightstheincreasing/decreasing
trend, disregarding a local minimum/maximum. The orange vertical lines indicate the batches
wherethedriftalgorithmhasdetectedawarningbeforeapotentialdrift;meanwhile,theredlines
indicateadrift.
Thelossisrelativelystablewithminimalincrease/decreaseduetothenatureofthedataset.The
numberofitemsislessthanthenumberofusers,whilethenewsareequallyscatteredacrossthe
dataset that covers only six days. For this reason, each batch contains a few new items, and the
preferencesonhotnewsregisteredinafewhoursshouldmotivatethehighnumberofwarning
and drift alerts and the value differences between consecutive batches. We highlight that each
batchcontainsthenewsreadinafewminutes.
ThegoodperformanceinthelosschartcanbealsoseenintheHitRatecharts.JustafterBatch
500,inFigure4(a),wecanseealowHRvalue(HR@5≈0.6).Thisbehaviorcouldbeexplainedby
adriftfollowing multiplewarningsintheregionclosetotheminimum. Probably,thisindicates
asignificantchange.ComparingtheHR@5valueswiththeHR@10values,thesecondonesare
betterforthesamebatches,indicatingthatthemodelworsensthepredictionsonlyonsomeitems
whilemaintaininggoodoverallperformance.Thenumberofwarningsisduetothefluctuations
recordedintheloss.
ThevisualrepresentationinFigure5providesinsightsintothedistinctionsbetweensegments
oftherealdatacorrespondingtodifferentregimesandtheirsyntheticcounterparts.Thesynthetic
dataineachregimeisgeneratedbysamplingfromthemodeltrainedonthecorrespondingreal
ACMTrans.Recomm.Syst.,Vol.3,No.2,Article24.Publicationdate:March2025.

ModellingConceptDriftinDynamicDataStreamsforRecommenderSystems 24:15
Fig.5. ComparisonofrealandsyntheticstreamfortheMicrosoftNewsdataset:ThechartshowstheP(f >
k)wheretheithfrequencyisdenotedask(log-scaleonbothaxes).
data.Toensureafairandmeaningfulcomparisonbetweenthesyntheticandoriginaldatastreams,
wemeticulouslystructuredthesyntheticdatatomirrortheoriginaldata.Thisinvolvedmaintain-
ingthesameregimesinthesameorderandensuringanequalnumberofsamplesforeachregime.
Inthecharts,thehorizontalaxisrepresentstheithfrequencydenotedask,whilethevertical
axisindicatesthecumulativecountofitems(i.e.,P(f >k)),normalizedbythesumofvalues.Upon
analyzingthedistributions,weobservethatthefrequenciesexhibitcomparablepatterns,thereby
confirmingtheeffectivenessoftrainingthedifferentmodels.Thesimilarityisalsoconfirmedbya
positiveoutcomeoftheKolmogorov–Smirnovtest[20]oneachregime.
Theobservedsimilaritybetweenthedistributionsinthechartsservesasstrongvalidationfor
theeffectivenessandfidelityofourapproachingeneratingsyntheticdatathataccuratelyrepro-
ducesthecharacteristicsoftheoriginalstream.
It’scrucialtonotethatourcomparisonfocusesonfrequencydistributionsratherthanprefer-
encedistributionsinthecharts.Thisdeliberatechoiceismotivatedbytherecognitionthatcom-
paringpreferencedistributionscanbeproblematicduetotheinfluenceofpopularitybiasonpre-
dictivemodelsforpreferencedata[23].Popularitybiastendstooverlookcontributionsfromcold
startusersandlow-popularityitems,especiallyinpreferencedatawithvastitemcatalogs.Com-
paringdistributionsbasedonpreferenceswouldconsequentlyfail,duetoinaccurateassociations
involving cold-start users and/or low-popularity items. By contrast, it is important to highlight
ACMTrans.Recomm.Syst.,Vol.3,No.2,Article24.Publicationdate:March2025.

24:16 L.Caropreseetal.
Fig.6. LossontestsetpartofeachbatchoftheAmazonVideoGamesdataset.
Fig.7. ResultsfortheAmazonVideoGamesdataset.
thatsuchinaccuraciesdonotsignificantlyimpacttheglobalmodelingcapabilitiesofthelearned
embeddingmatrices,whichisthemainfocushere.
4.4 ExperimentonAmazonVideoGames
Weconductedsimilarexperimentsfortheothertwodatasets.Firstly,fortheAmazonVideoGames
dataset,weanalyzedthelossvalues(Figure6)andHitRate(Figure7)onthetestset.Inthesecharts,
weobservethepresenceof 7 regimes, indicating 6 detecteddriftsby thealgorithm. We observe
similarpatternsasseenintheMINDdataset,wheretheperformancedeteriorateswhenmultiple
driftsoccurincloseproximity.
Tocomparetheitemdistributionofthesyntheticstreamwiththerealstream,weexaminedthe
distributionsshowninFigure8.IncontrasttotheMINDdataset,thedistributionsinthiscaseare
significantlyworse.Thisindicatesthatthenumberofpreferencesforeachitemisinsufficientto
acquirethenecessaryknowledgerequiredtoaccuratelyreplicatethestream.
Tofurthersupportthisobservation,weinvertedtherolesofusersanditemsinthedataset.By
doing so, the number of items became smaller than the number of users, resembling the MIND
dataset. Analyzing the loss performance (Figure 9) computed on each batch (i.e., M,Btest) after
the training phase, we notice a rapid increase in loss value when a drift appears in the stream.
Subsequently, the loss value decreases as the model adjusts to the new data. Although the drift
detectionalgorithmtriggersafalsewarning,ithasminimalimpactonthelossvalue.Wedonot
observeanysignificantchangesintheHitRatevalues.
We computed HR@5 and HR@10 (Figure 10) and observed similar behavior in both settings.
The model performs poorly in the vicinity of a drift due to significant changes in the data
ACMTrans.Recomm.Syst.,Vol.3,No.2,Article24.Publicationdate:March2025.

ModellingConceptDriftinDynamicDataStreamsforRecommenderSystems 24:17
Fig.8. ComparisonofrealandsyntheticstreamfortheAmazonVideoGamesdataset:Thechartshowsthe
P(f >k)wheretheithfrequencyisdenotedask(log-scaleonbothaxes).
Fig.9. LossontestsetpartofeachbatchoftheInvertedAmazonVideoGamesdataset.
distribution,evenwithnewuser/itempreferencesorpreviouslyunseenitems.However,afterthe
drift,thenewmodelistrainedontheupdateddata,andwithinafewbatches,itregainsoptimal
performance.
Incontrasttothepreviouscase,thedistributionsofthegenerateddataarenoticeablyimproved
inthisscenario.AsdepictedinFigure8,thecurvesrepresentingthedistributionsareveryclose
toeachother.Thisobservationalignswithourintuitionregardingthesignificanceofhavingan
adequatenumberofitempreferencestotrainagenerativemodeleffectively.Theclosesimilarity
betweenthecurvesconfirmstheimportanceofhavingasufficientnumberofpreferencesforeach
iteminordertoaccuratelyreplicatethedata.
4.5 ExperimentonYoochoose
TheresultsfromtheYoochoosedatasetexhibitabehaviorsimilartothepreviousdataset.Figure11
illustratesthelossonthetestset,highlightingasingledriftwherethereisanoticeableincrease
ACMTrans.Recomm.Syst.,Vol.3,No.2,Article24.Publicationdate:March2025.

24:18 L.Caropreseetal.
Fig.10. ResultsfortheInvertedAmazonVideoGamesdataset.
Fig.11. LossontestsetpartofeachbatchoftheYoochoosedataset.
in the loss value. However, the changes in the data distribution have only partially affected the
qualitymeasures,asdepictedintheHitRatechartsinFigure12.
This observation suggests that while the model’s performance is impacted by the drift, it is
able to adapt and adjust to the new data to some extent. The changes in the data distribution
haveresultedinadecreaseintheHitRate,indicatingthatthemodel’srecommendationsareless
accurate during the drift period. However, it is worth noting that the model gradually recovers
andimprovesitsperformanceafterthedrift.
Overall, theresultsfrom theYoochoosedatasetconfirmthepresenceof driftand themodel’s
abilitytoadapt,albeitwithsomeimpactonthequalityofrecommendationsduringthetransition
period.
4.6 ComparisonwithaBaselineAlgorithm
Inthissection,acomparisonwasmadebetweentheBPRalgorithmandamodelthatcouldbemore
easilyadaptabletomanagingnewusers/items.Wehavechosenavariationalautoencoder,inwhich
thenumberofitemsthesystemcanhandleisfixedapriori.Themodelreceivesasinputtheitems
thatauserhasalreadyseenand,basedonthisinformation,assignsascoretotheentirecatalogto
generatearankingandthusbuildarecommendationlist.Havingthewholecatalogavailablefrom
theoutsetgivesthemodelacompetitiveadvantageovertheBPRmodel,whichinsteadadaptsby
updating thelatent space whensignificant changesare detectedin the system, both in terms of
newusers/itemsand/ornewpreferencepatternsforexistingusers/items.Naturally,theimpacton
performance will be more noticeable with many items distributed over a broad temporal range.
ACMTrans.Recomm.Syst.,Vol.3,No.2,Article24.Publicationdate:March2025.

ModellingConceptDriftinDynamicDataStreamsforRecommenderSystems 24:19
Fig.12. ResultsfortheYoochoosedataset.
Fig.13. ComparisonofrealandsyntheticstreamfortheInvertedAmazonVideoGamesdataset:Thechart
showstheP(f >k)wheretheithfrequencyisdenotedask(log-scaleonbothaxes).
Fig.14. ComparisonofrealandsyntheticstreamfortheYoochoosedataset:ThechartshowstheP(f >k)
wheretheithfrequencyisdenotedask(log-scaleonbothaxes).
Conversely, in the presence of lower variability, i.e., when the model can learn patterns in the
initialmomentsthatarevalidfortheentireobservationperiod,amodelliketheVAEwillhavea
competitiveadvantageoveranadaptivemodel.
Performance was measured for three datasets: MIND, Amazon Video Games with reversed
roles, and Yoochoose. The experiment could not be executed for the original Amazon Video
Games dataset because the model required excessive memory due to the high number of items
(567,865).ConsideringtheHitrate@5values(theHitrate@10metricshowssimilartrendsandis
not reported for brevity), for the MIND dataset (Figure 15), we can observe that the VAE model
reaches a peak value in the middle of the stream and maintains constant performance for the
restoftheobservationperiod.Conversely,theBPRmodelexhibitsmorefluctuatingperformance
following the detection of drifts. The nature of the data can explain this: the dataset consists
of news produced over 6 days. In many cases, these are news items covering the same event,
resultinginreducedvariabilityinidentifieduserpreferencepatterns.Thesystemcanlearnhighly
generalizablerecommendationmodels.Forinstance,itiscommontoobservemanyuserssharing
ACMTrans.Recomm.Syst.,Vol.3,No.2,Article24.Publicationdate:March2025.

24:20 L.Caropreseetal.
Fig.15. ComparingBPRandVAEontheMINDdataset(HitRate@5).
Fig.16. ComparingBPRandVAEontheInvertedAmazonVideoGamesdataset(HitRate@5).
similar patternsbecausetheyread multiple news items on thesame topic. In thiscase, the VAE
ismoreeffectiveindetectinglatentspacesimilaritiesthantheBPR.
FortheAmazonVideoGamesdatasetwithreversedroles(Figure16),i.e.,whereusersanditems
wereswappedtohaveacatalogof25kitems,weobservedworseperformancefortheVAE.Asthe
numberofnewitemsgrows,themodel’sperformancedegrades.Additionally,therecommendation
listcontainsitemsforwhichnopreferencesareobserved.AnadaptivesystemlikeBPRmanages
thesechangesbetter,ensuringsuperiorperformance.
WecanseeasimilartrendfortheYoochoosedatasetinFigure17.Themaindifferenceliesinthe
oscillatingpatternseeninthecharts.Thesystemadaptsmorequicklytochangesinpreferences,
but the limited temporal range prevents the model from converging to mid-high levels. In this
context, BPR adapts faster to changes, while the VAE system tends to be more stable around a
lower median value than BPR. Moreover, a descending trend is evident in the last shards of the
stream:arelativelyhighnumberofnewitemsappearswithalimitednumberofpreferences,and
bothsystemsstruggletoidentifynewpatternseffectively.
4.7 AblationStudy
Our approach aims at identifying a method that allows generating realistic data, replicating the
trendspresentinarealstream.Tocapturepossiblechangesinpreferences,regimeshomogeneous
inexpressedpreferencesareidentified,andtheircorrespondingmodelsarestoredtogeneratedata
derivedfromthosebehavioralmodels.Twoanalyseswereconductedtoevaluatethisprotocol:
—try ignoring the regime identification, so we train the model only on the first regime and
thentesttheperformanceondataofthenextregimes;
ACMTrans.Recomm.Syst.,Vol.3,No.2,Article24.Publicationdate:March2025.

ModellingConceptDriftinDynamicDataStreamsforRecommenderSystems 24:21
Fig.17. ComparingBPRandVAEontheYoochoosedataset(HitRate@5).
Fig.18. Testperformanceofthefirstmodel,i.e.,trainedonlyonfirstregime,ontheentirestream.
—comparetheperformanceignoringthestreamnatureofthedata.Wesamplea‘small’train-
ingsetwithdataofallregimes,thentestonthefulldatasetw.r.tregimes.
Inthefirstexperiment,wetrainedasinglemodelonlyondatabelongingtothefirstregime.As
soonasadriftisdetected,themodelisfrozenandtestedontherestofthestream.Itisevident
thatthemodelachievesgoodperformanceonlyonthedatabelongingtotheregimeitwastrained
on and performs poorly on the remaining regimes (Figure 18). This result is not surprising but
confirmstheneedtoimplementamechanismofcontinuoustrainingthatcreatesandtrainsanew
modelwhenthecharacteristicsofthestreamdatachange,andtheirpropertiescannolongerbe
capturedbythepreviousone.
Inthesecondexperiment,wecreatedatrainingsetbyrandomlyextracting30%ofthesamples
from the original dataset. We trained a single model using this training set and verified that its
performanceissimilartothatachievedbythesystemweareproposing(Figure19),whichcreates
andtrainsanewmodelwhenanewdriftoccurs.However,thissimplemodelisnotrealisticand
cannotbeappliedinreal-worldcontextsbecauseithastheadvantageofimmediatelyanalyzing
datasamplesfromtheentirehistoryofthestream.Itisnotrealisticbecausenomodelcan‘look’
into the future. The objective is only to test whether the detected changes are present in the
ACMTrans.Recomm.Syst.,Vol.3,No.2,Article24.Publicationdate:March2025.

24:22 L.Caropreseetal.
Fig.19. Testperformanceonthedatasetwithamodeltrainedonasampleofdata.
originaldatasetorareonlyasideeffectofthemodeltraining.Breakingthechronologicalorderof
preferencescouldheavilyimpactdatasetevaluation:ForYoochooseandAmazonVideoGames,it
meanschangingtheorderwhenitems‘appear’inthesystem.FortheMINDdataset,thesideeffect
isbreakingthecorrelationbetweennews:asequenceofnewsonthesameeventlosesmeaning,
influencingtheperformanceevaluation.However,thisbehaviorcanbeacceptedconsideringthe
scope of this experiment. The architecture we propose, however, remains competitive with this
‘ideal’modelandmatchesitsperformance.
Inafurthersetofexperiments,weevaluatewhethertheapproacheffectivelysupportsactual
shifts in data distribution. In our approach, we only increase dimensionality when a drift is de-
tected. This means that if no increase in loss is detected, we do not modify the structure of the
current model. Conversely, any increase in the loss is identified as a structural inability of the
modeltoproperlycaptureuserpreferences,promptingustotrainanewmodelwithupdateddi-
mensionality.
Figure20(b)illustratesthetestlosstrendfortheYoochoosedatasetaftershufflingthedata.In
thiscase,thedatasetnolongerdemonstratesfeaturesthatdegrademodelperformance.Essentially,
themodelfailstoadapttonewitemsorpreferences.AsimilartrendisobservedwiththeAmazon
dataset.
Figure 20(a), where the focus is on the MIND dataset, presents a contrasting behavior: the
model’s performance worsens upon encountering new items. In this dataset, items typically fol-
lowaninherentperiodicityduetoevolvingtopicsovertime.Userstendtoreadnewsonthesame
topicwithinashorttimeframebeforemovingontothenextone.Shufflingexacerbatesthissce-
nario,leadingtheframeworktoadjustbyidentifyingagreaternumberofregimes.
5 EnablingFullGeneration
The rationale of the above analysis is that, by tracking a realistic data stream, it is possible to
devise a sequence of models that can be used to generate a synthetic data stream similar to an
originalone.Thecomparisonbetweentheoriginalstreamandthesyntheticstreamintheprevious
section allowed us to evaluate the fidelity level of the generator in sampling new data. Clearly,
thisframeworkallowstogeneratestreamswithanarbitrarynumberofregimes,inanarbitrary
ACMTrans.Recomm.Syst.,Vol.3,No.2,Article24.Publicationdate:March2025.

ModellingConceptDriftinDynamicDataStreamsforRecommenderSystems 24:23
Fig.20. Testperformanceonthedatasetwithamodeltrainedonasampleofdata.
Fig.21. Summarystatisticsonchangesintheregimesdetected.ThefirstcolumnreferstotheMicrosoft
Newsdataset.Theothertwocolumnsreferto(originalandinverted)AmazonVideoGames.Thelastcolumn
referstotheYoochoosedataset.
order, and with an arbitrary number of samples. However, this generation can only rely on the
modelsextractedfromtheoriginaldatastream.Thisisclearlyalimitationsincewewouldliketo
generate new regimes that can also deviate from the extracted models. Better, we would like to
deviseageneralschemewherewecansynthesizethematricesassociatedwitheachregime,and
evenenablechangesofthesematricesalongtheshards.
InFigure21,wepresentstatisticalinsightsintothechangesobservedinthedatafromtheprevi-
ousexperiments.Thefirstrowprovidesinformationabouttheappearance/disappearanceofusers
and items across different regimes. It illustrates the dynamic nature of the dataset, where users
anditemscanappearorvanishovertime.
Thesecondrowfocusesonthefeaturevectorsassociatedwithusersanditemsandhowthey
evolve across the regimes. While a significant number of components remain stable, indicating
consistentuseranditemcharacteristics,certainusersundergosubstantialchangesintheirfeature
vectors.Thissuggestsshiftsintheirpreferencesorcharacteristicsovertime.
Additionally, Figures 5, 8, 13, and 14 display other noteworthy changes in the distributions.
Thesefiguresprovidevisualrepresentationsofthevariationsobservedinthegenerateddata,re-
flectingshiftsinuserpreferences,trends,orothersignificantmodifications.Thenumberofusers
isreportedinlog-scaleontheX-axis, whilethenumberofitemsisreportedinlog-scale onthe
Y-axis.
Ingeneral,thefollowingdriftdirectionscanbeidentified:
—Userscanundergochangesintheirtastes,leadingtoshiftsintheirpreferences.Thiscanbe
visualizedasarewiringofcertainusernodesinthefeaturegraphdiscussedinSection3.1.
ACMTrans.Recomm.Syst.,Vol.3,No.2,Article24.Publicationdate:March2025.

24:24 L.Caropreseetal.
—Newtrendsmayemerge,influencinguserpreferences.Thisisdirectlylinkedtothestructure
ofthefeaturegraphandhownodes(representingusersanditems)areconnectedwithinit.
—Newuserscanjointhesystem,expressingtheirpreferencesandimpactingtheunderlying
preference distributions. Similarly, new items can be introduced, further altering the
distributionofavailableitems.
—Conversely, some users may leave the system or become inactive, and certain items may
becomeobsolete.Thesechangesresultinmodificationstotheunderlyingitemdistribution.
Byunderstandingandaddressingthesedriftdirections,wecaneffectivelycapturethedynamics
ofuserpreferences,trends,andtheevolutionoftheitemspace.
In Algorithm 1, we observed that the generation of new samples (using the generateSamples
procedure) depends on the P and Q matrices, as well as the user/item frequency distributions
q and r. Consequently, if we want to capture the described drifts in the generated preferences,
we need to modify these parameters accordingly. We can develop a versatile stream generator
inspiredbytheconceptofgeometricclosenessintheBPRmodel,whichcaneffortlesslyintegrate
theaforementioneddriftmodels.
Tobegin,wedefineasetofnearlyorthogonalgeneratingvectorsinK-dimensionalspace,de-
noted as g ,...,g (i.e., designed such that g · g ≈ 0, for i (cid:2) j). Conceptually, these vectors
1 h i j
represent clusters of users and items. In practice, we can generate feature vectors p for users
u
u (and q for itemsi) aligned with a specific generating vector g . These user and item feature
i s
vectorsarecreatedbyintroducingrandomvariationsalongtheK dimensionsbasedong .Togen-
s
eratepreferences,weutilizethegenerateSamplesfunction,whichincorporatesrandomuser/item
frequenciesqandr accordingly.
Consequently, the aforementioned drifts can be effectively modeled by making appropriate
adjustmentstothesefeaturevectors,asdescribedbelow.
Drifting users: To capture changes in user preferences, we can model the shift in tastes for
a user u with a feature vector p associated with the generating vector g . This shift can be
u s
represented as a movement towards a different generating vector g . Consequently, a new ver-
t
sion of the user’s feature vector p can be obtained by combining g and g through a linear
u s t
combination.
New trends: To incorporate new trends, we introduce changes in the latent dimension K.
(cid:10)
Each generating vector g is extended with additional dimensions, denoted as k . User and
s
item feature vectors are extended accordingly, and this extension affects their geometric
proximity.
Distributiondrifts: Toaccountforchangesinuseranditemdistributions,wecanintroducenew
usersanditemsbyassociatingthemwithageneratorvectorandgeneratingtheirrespectivefeature
vectors.Theoreticalfrequenciesinqcanbeassignedtothesenewusers/items.Alternatively,new
generating vectors g can be created, allowing for the association of new items/users and the
s
drift of existing items. User churns and item obsolescence can be modeled by annihilating their
respectivefrequenciesinqandr.
InAlgorithm 2,wepresentasamplegenerationschemethatsummarizestheaforementioned
conceptsusingasetofpoliciesforpreferencegeneration.Weidentifysixmainpolicies,andprovide
example implementations for some of these policies. They essentially introduce adjustments to
generatingvectors,featurematrices,orfrequencydistributions.Byutilizingthemodifiedfeature
matricesand/orfrequencydistributions,wecangeneratepreferencesfortheshardassociatedwith
eachpolicy.
ACMTrans.Recomm.Syst.,Vol.3,No.2,Article24.Publicationdate:March2025.

ModellingConceptDriftinDynamicDataStreamsforRecommenderSystems 24:25
ALGORITHM2:StreamGenerator
Input: Numberhofclustergeneratingvectors;ClusterusersizeNsanditemsizeMs,for1≤s ≤h;Numbernofinitial
preferencestogenerate;AlistofT−1policiesspecifictodriftingregimesandpreferencestogenaratent
Output: PreferencemodelsM(1),...,M(T)andassociatedpreferencesR(1),...,R(T).
1
M(1),G=generateFeatureMatrices({N1,...,Nh },{M1,...,Mh })
2
R(1),q,r =generateSamples(M,n)
3 foreacht ∈{2,...,T}do
4
M(t)=M(t−1)
5 ifthet-thregimecontains’userdrift’withpercentageαthen
6
M(t),G=coalesceDrift(α,G,M(t))
7 end
8 ifthet-thregimecontains’newtrends’withdimensionkthen
9
M(t),G=directionDrift(α,G,M(t))
10 end
11 ifthet-thregimecontains’newusers’withdimensionkthen
12
M(t),q=updateP(a,G,M(t))
13 end
14 ifthet-thregimecontains’newitems’withdimensionkthen
15
M(t),r =updateQ(a,G,M(t))
16 end
17 ifthet-thregimecontains’userschurn’withpercentageαthen
18
q=churnDrift(α,q)
19 end
20 ifthet-thregimecontains’itemsexpire’withpercentageαthen
21 r =obsolescenceDrift(α,r)
22 end
23
R(t),q,r =generateSamples(M,nt,q,r)
24 end
25
FunctiongenerateFeatureMatrices({N1,...,Nh },{M1,...,Mh }):
26 SampleK >h
27 Generatehorthogonalvectorsg1,...,gh ∈RK
28 foreachs ∈{1,...,h}do
29 foreachu ∈{1,...,Ns }andi ∈{1,...,Ms }do Generatetworandomperturbationsofgsaspuandqi
30 end
31
returnM,{g1,...,gh }
32 FunctioncoalesceDrift(α,G,M):
33 Sampleα%usersfromU intoU(cid:10)
34 foreachu ∈U(cid:10)do
35 Letgsbethegeneratingvectorassociatedwithu.
36
Randomlysamplegtwitht(cid:2)sfromGandβ ∈[0,1]
37 gh+1 =βgs +(1−β)gt;Addgh+1toG
38 Generatearandomperturbationsofgtasp u (cid:10) andupdatepuasβps +(1−β)p u (cid:10)
39 end
40 returnM,G
41 FunctiondirectionDrift(k,G,M):
42 foreachs ∈{1,...,h}do
43 extendgswithknewrandomdimensions
44 foreachu ∈{1,...,Ns }andi ∈{1,...,Ms }do extendpuandqibyusingtherandomperturbationsfromthe
generatingvectors
45 end
46 returnM,G
47 FunctionupdateP(k,G,M):
48
SamplekgeneratingvectorswithreplacementfromGintoG(cid:10)
49
foreachg∈G(cid:10)do
50 Generatearandomperturbationofgaspuwhereuisanewuserassociatedwithg
51 SamplearandomZipffrequencyqu
52 end
53 returnM,q
54 FunctionobsolescenceDrift(α,r):
55 Sampleα%usersfromU intoU(cid:10)
56 foreachu ∈U(cid:10)do updaterubymultiplyingitwitharandomdecayw
57 returnM,q
ACMTrans.Recomm.Syst.,Vol.3,No.2,Article24.Publicationdate:March2025.

24:26 L.Caropreseetal.
6 Conclusions
Inthisstudy,weintroducedatechniqueformodelinguser/itempreferencesandtheirevolution
overtimeusingadynamictripartitegraphrepresentation.Thisgraphisconstructedasasequence
ofMFmodelstrainedonthesourcedatastream,witheachmodelcapturingthepropertiesanddata
distributionofaspecificregime.Thetransitionfromonemodeltoanotheroccurswhenaconcept
driftisdetected.
We explored this concept in two main directions. Firstly, we utilized the learned sequence of
modelstogeneratesyntheticdatastreamsthatexhibitsimilarpropertiestotheoriginaldata.This
approachenablesthegenerationofrealisticsyntheticdatastreams,facilitatingthedevelopmentof
moreefficientandaccuraterecommendationsystems.Theexperimentalevaluationdemonstrated
theeffectivenessofourapproachingeneratingdatastreamsthataccuratelyreflectthedynamics
oftheunderlyingdatadistribution.
Buildingupontheinsightsfromthepreliminarystudy,wedevelopedamoregeneralapproach
capable of mapping specific drifting operations to changes in the underlying tripartite graphs.
These changes can be parameterized, allowing for controlled data generation strategies where
variousdriftingstrategiescanbeimplementedbymanipulatingthetripartitegraph.
Itisworthnotingthatourproposedapproachisbasedonaspecificpreferencemodelthatas-
sumesgeometricclosenessofusersanditemsinthelatentembeddingspaceasameasureofinter-
action.Asadirectionforfutureresearch,itwouldbeinterestingtoadapttheproposedschemeto
otherpreferencemodelingstrategiesthatdonotrelyongeometriccloseness.Forinstance,explor-
inghowthemodelcanbetunedtoworkwithMarkovianmodelswherepreferencesarecorrelated,
andpreviousinteractionscaninfluenceauser’sfuturepreferences.
Anotherfascinatingtopicisthestudyofstrategiesformanagingnewusersand/oritems.For
instance,anewtypeofnodecouldbeaddedtothegraph(Figure1)toaccountfornewentriesand
applytargetedstrategiestomodelthebehaviorofnewuserseffectively.Similarly,foritems,one
couldconsiderincorporatingbusinesslogic,suchasprioritizingnew,moreprofitableitems.Also,
thesestrategiescouldbeconsideredaviablesolutiontothecold-startproblemoftherecommender
system.
References
[1] CharuC.Aggarwal.2016.RecommenderSystems.Springer.
[2] MarieAl-Ghossein,TalelAbdessalem,andAnthonyBarré.2021.Asurveyonstream-basedrecommendersystems.
ACMComputingSurveys54,5,Article104(2021),1–36.
[3] ManuelBaena-García,JosédelCampo-Ávila,RaulFidalgo,AlbertBifet,RicardGavalda,andRafaelMorales-Bueno.
2006.Earlydriftdetectionmethod.InProceedingsofthe4thInternationalWorkshoponKnowledgeDiscoveryfromData
Streams.Citeseer,77–86.
[4] CigdemBakir.2018.Collaborativefilteringwithtemporaldynamicswithusingsingularvaluedecomposition.Tehnički
Vjesnik25,1(2018),130–135.
[5] NicolaBarbieri,GiuseppeManco,andEttoreRitacco.2014.ProbabilisticApproachestoRecommendations.Morganand
ClaypoolPublishers.
[6] FrancoisBelletti,KarthikLakshmanan,WalidKrichene,Yi-FanChen,andJohnAnderson.2019.Scalablerealisticrec-
ommendationdatasetsthroughfractalexpansions.arXiv:1901.08910.Retrievedfromhttps://arxiv.org/abs/1901.08910
[7] JamesBennett,CharlesElkan,BingLiu,PadhraicSmyth,andDomonkosTikk.2007.KDDcupandworkshop2007.
ACMSIGKDDExplorationsNewsletter9,2(2007),51–52.
[8] AlbertBifetandRicardGavalda.2007.Learningfromtime-changingdatawithadaptivewindowing.InProceedingsof
the2007SIAMInternationalConferenceonDataMining.SIAM,443–448.
[9] MaríadelCarmenRodríguez-Hernández,SergioIlarri,RamónHermoso,andRaquelTrillo-Lado.2017.DataGenCARS:
Ageneratorofsyntheticdatafortheevaluationofcontext-awarerecommendationsystems.PervasiveandMobile
Computing38(2017),516–541.
[10] JörgDrechslerandJeromeP.Reiter.2011.Anempiricalevaluationofeasilyimplemented,nonparametricmethodsfor
generatingsyntheticdatasets.ComputationalStatisticsandDataAnalysis55,12(2011),3232–3243.
ACMTrans.Recomm.Syst.,Vol.3,No.2,Article24.Publicationdate:March2025.

ModellingConceptDriftinDynamicDataStreamsforRecommenderSystems 24:27
[11] EduardoFerreiraJosé,FabricioEnembreck,andJeanPaulBarddal.2020.ADADRIFT:Anadaptivelearningtechnique
forlong-historystream-basedrecommendersystems.InProceedingsofthe2020IEEEInternationalConferenceonSys-
tems,Man,andCybernetics(SMC’20).2593–2600.
[12] IsvaniFrías-Blanco,JosédelCampo-Ávila,GonzaloRamos-Jiménez,RafaelMorales-Bueno,AgustínOrtiz-Díaz,and
YailéCaballero-Mota.2015.Onlineandnon-parametricdriftdetectionmethodsbasedonhoeffding’sbounds.IEEE
TransactionsonKnowledgeandDataEngineering 27,3(2015),810–823.DOI: https://doi.org/10.1109/TKDE.2014.
2345382
[13] JoaoGama.2010.KnowledgeDiscoveryfromDataStreams.ChapmanandHall/CRC.
[14] JoaoGama,PedroMedas,GladysCastillo,andPedroRodrigues.2004.Learningwithdriftdetection.InProceedingsof
theBrazilianSymposiumonArtificialIntelligence.Springer,286–295.
[15] JoãoGama,IndreŽliobaite,AlbertBifet,MykolaPechenizkiy,andAbdelhamidBouchachia.2014.Asurveyonconcept
driftadaptation. ACMComputingSurveys46,4(2014),1–37.
[16] HeitorM.Gomes,AlbertBifet,JesseRead,JeanPaulBarddal,FabrícioEnembreck,BernhardPfharinger,GeoffHolmes,
andTalelAbdessalem.2017.Adaptiverandomforestsforevolvingdatastreamclassification.MachineLearning106,
9(2017),1469–1495.
[17] HeitorMuriloGomes,JesseRead,AlbertBifet,JeanPaulBarddal,andJoãoGama.2019.Machinelearningforstreaming
data:State-of-the-art,challenges,andopportunities.ACMSIGKDDExplorationsNewsletter21,2(2019),6–22.
[18] X.Han,C.Zhu,X.Hu,C.Qin,X.Zhao,andH.Zhu.2024.Adaptingjobrecommendationstouserpreferencedrift
withbehavioral-semanticfusionlearning.InProceedingsofthe30thACMSIGKDDConferenceonKnowledgeDiscovery
andDataMining.1004–1015.
[19] F.MaxwellHarperandJosephA.Konstan.2015.TheMovieLensdatasets:Historyandcontext.ACMTransactionson
InteractiveIntelligentSystems5,4(2015),1–19.
[20] MylesHollander,DouglasA.Wolfe,andEricChicken.2014.NonparametricStatisticalMethods.JohnWileyandSons.
[21] MartinJakomin,TomažCurk,andZoranBosnić.2018.Generatinginter-dependentdatastreamsforrecommender
systems.SimulationModellingPracticeandTheory88(2018),1–16.
[22] Wang-ChengKangandJulianMcAuley.2018.Self-attentivesequentialrecommendation.InProceedingsoftheIEEE
InternationalConferenceonDataMining.IEEE,197–206.
[23] AnastasiiaKlimashevskaia,DietmarJannach,MehdiElahi,andChristophTrattner.2024.Asurveyonpopularity
biasinrecommendersystems.UserModelUser-AdapInter 34(2024),1777–1834.https://doi.org/10.1007/s11257-024-
09406-0
[24] YehudaKoren.2009.Collaborativefilteringwithtemporaldynamics.InProceedingsofthe15thACMSIGKDDInterna-
tionalConferenceonKnowledgeDiscoveryandDataMining.447–456.
[25] LukaszKoryckiandBartoszKrawczyk.2019.Unsuperviseddriftdetectorensemblesfordatastreammining.InPro-
ceedingsofthe2019IEEEInternationalConferenceonDataScienceandAdvancedAnalytics(DSAA’19).317–325.
[26] JureLeskovec,AnandRajaraman,andJeffreyUllman.2020.MiningMassiveData.CambridgeUniversityPress.
[27] ElisabethLex,DominikKowald,andMarkusSchedl.2020.Modelingpopularityandtemporaldriftofmusicgenre
preferences.TransactionsoftheInternationalSocietyforMusicInformationRetrieval3,1(2020),17–30.
[28] JiachengLi,YujieWang,andJulianMcAuley.2020.Timeintervalawareself-attentionforsequentialrecommendation.
InProceedingsofthe13thInternationalConferenceonWebSearchandDataMining.322–330.
[29] PawelMatuszykandMyraSpiliopoulou.2017.Stream-basedsemi-supervisedlearningforrecommendersystems.
MachineLearning106,6(2017),771–798.
[30] PawelMatuszyk,JoãoVinagre,MyraSpiliopoulou,AlípioMárioJorge,andJoãoGama.2018.Forgettingtechniquesfor
stream-basedmatrixfactorizationinrecommendersystems.KnowledgeandInformationSystems55,2(2018),275–304.
[31] DiegoMonti,GiuseppeRizzo,andMaurizioMorisio.2019.Allyouneedisratings:Aclusteringapproachtosynthetic
ratingdatasetsgeneration.InProceedingsoftheREVEALWorkshopatACMRecSysConference.
[32] JianmoNi,JiachengLi,andJulianMcAuley.2019.Justifyingrecommendationsusingdistantly-labeledreviewsand
fine-grainedaspects.InProceedingsofthe2019ConferenceonEmpiricalMethodsinNaturalLanguageProcessingand
the9thInternationalJointConferenceonNaturalLanguageProcessing(EMNLP-IJCNLP’19).188–197.
[33] StanleyAdeOyewole.2021.ImageContent-basedUserPreferenceElicitationforPersonalisedMobileRecommendationof
ShoppingItems.Ph.D.Dissertation.DepartmentofInformationTechnology,FacultyofAccountingandInformatics,
DurbanUniversityofTechnologyDurban,SouthAfrica.
[34] S.Rendle,C.Freudenthaler,Z.Gantner,andL.Schmidt-Thieme.2009.BPR:Bayesianpersonalizedrankingfromim-
plicitfeedback.InProceedingsoftheConferenceonUncertaintyinArtificialIntelligence(UAI’09).452–461.
[35] FrancescoRicci,LiorRokach,andBrachaShapira(Eds.).2015.RecommenderSystemsHandbook(2nded.).Springer
PublishingCompany,Incorporated.
[36] RaquelSebastiãoandJoséMariaFernandes.2017.SupportingthePage-Hinkleytestwithempiricalmodedecompo-
sitionforchangedetection.InProceedingsoftheInternationalSymposiumonMethodologiesforIntelligentSystems.
Springer,492–498.
ACMTrans.Recomm.Syst.,Vol.3,No.2,Article24.Publicationdate:March2025.

24:28 L.Caropreseetal.
[37] ManelSlokom,MarthaLarson,andAlanHanjalic.2020.Partiallysyntheticdataforrecommendersystems:Prediction
performanceandpreferencehiding.arXiv:2008.03797.Retrievedfromhttps://arxiv.org/abs/2008.03797
[38] RicardoSousaandJoaoGama.2016.Firstprinciplemodelsbaseddatasetgenerationformulti-targetregressionand
multi-labelclassificationevaluation.InProceedingsoftheSTREAMEVOLV@ECML-PKDD.
[39] HuiminSun,JiajieXu,KaiZheng,PengpengZhao,PingfuChao,andXiaofangZhou.2021.MFNP:Ameta-optimized
modelforfew-shotnextPOIrecommendation.InProceedingsoftheIJCAI.3017–3023.
[40] TipajinThaipisutikul.2022.Anadaptivetemporal-conceptdriftmodelforsequentialrecommendation.ECTITransac-
tionsonComputerandInformationTechnology16,2(2022),222–236.
[41] KarenH.L.TsoandLarsSchmidt-Thieme.2006.Empiricalanalysisofattribute-awarerecommendersystemalgo-
rithmsusingsyntheticdata.J.Comput.1,4(2006),18–29.
[42] AlexeyTsymbal.2004.Theproblemofconceptdrift:Definitionsandrelatedwork.ComputerScienceDepartment,
TrinityCollegeDublin106,2(2004),58.
[43] BrunoVeloso,LucianoCaroprese,MatthiasKönig,SóniaTeixeira,GiuseppeManco,HolgerH.Hoos,andJoãoGama.
2021.Hyper-parameteroptimizationforlatentspaces.InProceedingsoftheECML/PKDD2021EuropeanConferenceon
MachineLearningandKnowledgeDiscoveryinDatabases(LectureNotesinComputerScience,Vol.12977).249–264.
[44] JoãoVinagre,AlípioMárioJorge,ConceiçãoRocha,andJoaoGama.2021.Statisticallyrobustevaluationofstream-
basedrecommendersystems.IEEETransactionsonKnowledgeandDataEngineering33,7(2021),2971–2982.
[45] JoãoVinagre,AlípioMárioJorge,andJoãoGama.2018.Onlinegradientboostingforincrementalrecommendersys-
tems.InProceedingsoftheDiscoveryScience.209–223.
[46] CharinyaWangwatcharakulandSartraWongthanavasu.2021.Anoveltemporalrecommendersystembasedonmulti-
pletransitionsinuserpreferencedriftandtopicreviewevolution.ExpertSystemswithApplications185(2021),115626.
[47] Geoffrey I. Webb, Loong Kuan Lee, François Petitjean, and Bart Goethals. 2017. Understanding concept drift.
arXiv:1704.00362.Retrievedfromhttps://arxiv.org/abs/1704.00362
[48] TaoruYang,YongGao,ZhouHuang,andYuLiu.2023.UPTDNet:Auserpreferencetransferanddriftnetworkfor
cross-citynextPOIrecommendation.InternationalJournalofIntelligentSystems2023,1(2023),9091570.
[49] ZhengyiYang,XiangnanHe,JizhiZhang,JiancanWu,XinXin,JiaweiChen,andXiangWang.2023.Agenericlearning
frameworkforsequentialrecommendationwithdistributionshifts.InProceedingsofthe46thInternationalACMSIGIR
ConferenceonResearchandDevelopmentinInformationRetrieval.
Received15December2022;revised30July2024;accepted17September2024
ACMTrans.Recomm.Syst.,Vol.3,No.2,Article24.Publicationdate:March2025.