---
conversion_metadata:
  converted_at: "2026-07-22T13:32:03Z"
  converter_tool: "markitdown"
  converter_version: "0.1.6"
  source_pdf: "Hassan et al.pdf"
  source_pdf_sha256: "fcf0a89c7565feb44050a89a1ff1d0b5d3191a327f00bcf81d1d3ec3160f2d2c"
  page_count: 11
  markdown_char_count: 124588
---

<!-- PAGE-AWARE EXTRACTION (via pdfminer.six) -->

<!-- PAGE 1 -->

Received 13 December 2023, accepted 21 January 2024, date of publication 26 January 2024, date of current version 5 February 2024.

Digital Object Identifier 10.1109/ACCESS.2024.3359053

GCZRec: Generative Collaborative
Zero-Shot Framework for Cold
Start News Recommendation

SYED ZAIN UL HASSAN 1, MUHAMMAD RAFI 1,
AND JAROSLAV FRNDA 2,3, (Senior Member, IEEE)
1Department of Computer Science, School of Computing, National University of Computer and Emerging Sciences, Islamabad 44000, Pakistan
2Department of Quantitative Methods and Economic Informatics, Faculty of Operation and Economics of Transport and Communications, University of ˘Zilina,
01026 ˘Zilina, Slovakia
3Department of Telecommunications, Faculty of Electrical Engineering and Computer Science, VSB—Technical University of Ostrava, 70800 Ostrava, Czech
Republic

Corresponding author: Jaroslav Frnda (jaroslav.frnda@uniza.sk)

This work was supported by the European Union within the REFRESH Project—Research Excellence for Region Sustainability and
High-Tech Industries of the European Just Transition Fund under Grant CZ.10.03.01/00/22 003/0000048.

ABSTRACT The aim of personalized news recommendation is to suggest news stories to the users that
are most interesting for them. To improve the user experience, it is important that these news items are not
only relevant to the user but also get recommended to them as soon as they are available. The inability of
traditional collaborative filtering approach to recommend such cold start items has led to techniques that
incorporate latent features of items in order to make cold start recommendations such as content based
filtering and deep neural network-based approaches. However, these existing techniques do not make use
of any collaborative information between users and items as well as latent features at the same time and
thus fail to provide any serendipity which is an important aspect of any recommender system. Moreover,
these underlying collaborative signals between users and items are crucial to improving the overall quality of
recommender systems and can also be utilized to make cold start recommendations. In this paper, we propose
the Generative Collaborative Zero-Shot Recommender System framework (GCZRec) which makes use of
both the latent user and item features as well as the underlying collaborative information to generate both
warm start and cold start recommendations. We evaluate our framework for news recommendation task given
cold start and warm start cases for both users and news items. We also discuss that our model can be plugged
in and used as preprocessing to improve the performance of an existing recommender system.

INDEX TERMS News recommendation, cold start problem, zero-shot learning, recommender system.

I. INTRODUCTION
The improvement in media technology and online services
have resulted in an overload of information especially with
online news articles as the people realize the need to be
well-informed at all times [1], [2]. Recommender systems
can therefore improve the user experience by suggesting news
articles that are most recent, relevant and contain value for
her. These systems can help the users find information that is

The associate editor coordinating the review of this manuscript and

approving it for publication was Chao Tong

.

interesting and personalized. But compared to recommending
movies and products, news article recommendations often
entail some additional challenges such as the latest news
articles being posted frequently and lacking any historical
interactions that can be used for recommending these news
items [3]. This severe case of cold start problem is a challenge
in news recommendations. Moreover, from the user point
of view, these news stories need to be recent but highly
personalized, while from the item perspective, it should be
recommended to the users based strictly on its relevance to
those particular users.

16610

2024 The Authors. This work is licensed under a Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 License.
For more information, see https://creativecommons.org/licenses/by-nc-nd/4.0/

VOLUME 12, 2024

---

<!-- PAGE 2 -->

S. Z. U. Hassan et al.: GCZRec: Generative Collaborative Zero-Shot Framework for Cold Start News Recommendation

The conventional collaborative recommendation algo-
rithms rely on historical interaction data of users and items
to find hidden patterns based on similarity [4], [5]. The
performance of these algorithms decreases when the data
contains missing user interaction entries for the items. This
lack of data is mostly seen in the case of news articles which
are often posted without any prior interaction information.
This leads to a severe case of cold start problem.

Other techniques such as Matrix Factorization [6] and
content-based filtering [7] also suffer from cold start user
problem [8], [9], [10]. In case of Matrix Factorization, it can
additionally suffer from both over-fitting and under-fitting
given the available historical data. Another problem that both
of these techniques face is the assumption that features are
always independent. This condition is difficult to hold true
in most real-world scenarios where not only the features
but items also have relative dependence on features and
themselves.

The cold start problem in recommender systems can be
remodeled as a classical zero-shot learning task which comes
from the computer vision domain [11], [12]. In zero-shot
classification, the set of classes in the training data and set
of classes in the samples to be classified can be disjoint.
Similarly, in cold start item recommendations, the aim is to
predict whether an item should be recommended to a partic-
ular user without any available historical interactions for that
item. In cold start user case, items are to be recommended
to a particular user for which there are no existing historical
information [13]. Following this intuition, the features of
news items and users can be used to deduce the behavioral
context of cold start items and users in recommendation
scheme just like a class label can be predicted for an unseen
data sample using the generalization from known samples in
zero-shot classification. Some existing studies [14], [15] have
used this relation to propose recommendation models for cold
start items.

But these techniques do not take into account serendipity,
which is an important aspect of a recommender system [16],
[17], [18], [19]. This lack of diversity stems from the inability
of these models to make use of the latent collaborative
information between users as well as items. These neigh-
borhood signals are therefore important to make fine-grained
recommendations that are not only relevant to the active users
but also provide diversity in choices for them.

We observe that by directly synthesizing the interactions
based on feature representations can eliminate the need
for any external click predictor model and can also pro-
vide an effective method to not only allow item-to-user
interactions prediction but also projection of user-to-item
interactions. This synthesis of interactions can also allow
us an efficient method to rank the predicted interactions.
This can be achieved by incorporating a generative network
with conditional information to learn the latent collaborative
information between users and items. This allows us to
use these hidden patterns in the available historical data
to directly synthesize the interactions for cold start users

FIGURE 1. Illustration of the cold start news recommendation problem.

and items. In the same way that an unseen class label is
used for prediction by leveraging the features of the novel
sample, the conditional input of the generator network can
also be learned from the available item and user feature
representations.

Based on the previous discussion, we propose a novel
recommender system framework, GCZRec, to synthesize
both cold start and warm start interactions for users and news
items. Our technique utilizes the hidden feature information
of users and items to perform cold start recommendations
as zero-shot predictions. The proposed model is capable
of learning collaborative signals between users and among
items to generate interactions thus allowing diverse rec-
ommendations. The framework also allows the ranking of
these recommendations. At its core, GCZRec framework
consists of two separate classifiers for zero-shot labelling
of cold start news and cold start user. These predicted
classes are used as input to conditional Wasserstein GAN
(cWGAN) for generating interactions. During training, two
separate generator networks are independently trained such
that each training sample of the first network represent a
news item with interaction. This generator network is trained
on samples each one of which is an interaction vector
containing both interactions of users for news items. The
experiments were conducted on two publicly available news
recommendation datasets Microsoft News Dataset (MIND)
[20] and Addressa [21] in order to provide the proof of
concept for our research. Furthermore, our framework allows
this problem to be formulated as an extreme multi-label
classification task where the class labels are news items to
be recommended.

The main contributions of this research are as follows:

• We propose a novel GCZRec framework capable of
using latent collaborative information to make both cold
start and warm start recommendations of news items in
generative manner and allowing the recommended items
to be ranked.

• We present a formulation of cold start recommenda-
tion as zero-shot learning problem and utilize hidden
features of both users and items in order to make
recommendations.

• Our framework can also be used for typical extreme
multi-label classification task and provides an efficient

VOLUME 12, 2024

16611

---

<!-- PAGE 3 -->

S. Z. U. Hassan et al.: GCZRec: Generative Collaborative Zero-Shot Framework for Cold Start News Recommendation

approach for predicting the subset of labels from a large
space given a new instance.

II. PRELIMINARIES
The goal of a recommender system is to present the users
with an ordered set of items which are ranked based on the
preference and relevance of these items for each particular
user. This section defines the relevant concepts pertaining
to the overall recommendation problem and provides the
necessary basis for further discussion on these topics in the
subsequent sections.

Definition 1: Given set of users U and items I, the U x I
interaction matrix ℜ represents the historical choices of users
and items r(u ∈ U, i ∈ I). A cold start user problem occur when
r(unew, i) is undefined for a novel user unew and all values of
items i in I. Whereas, a cold start item problem occurs when
r(u, inew) is undefined for a novel item inew and all values of
u in U.

The cold start problem in recommender systems is
comparable to zero-shot classification problem in computer
vision.

learning,

Definition 2: In zero-shot

the classification
model generalizes feature information from seen classes to
an unseen class in order to predict it. Mathematically, given
a set of instances X and set of labels Y where Y contains both
seen and unseen classes, and feature space Z, the objective of
zero-shot learning is to learn the mapping f from input state
X to semantic space Z:

f : X → Z

(1)

And also learn the mapping g from semantic space Z to label
space Y:

g : Z → Y

(2)

Since, in a recommendation problem, there are typically a
large number of users and items involved. The selection of a
small subset of relevant items for the user from a large space
of available items is analogous to predicting class labels in an
extreme multi-label classification problem.

Definition 3: In extreme multi-label classification,
the
objective is to predict a subset of most relevant labels from
a high-dimensional label space containing a vast number
of potential labels, given an input instance. Mathematically,
given an input space χ and a high-dimensional label space
|L|. The objective in extreme multi-label classification is to
train a model that can find a set l containing relevant labels
for a novel instance x given l ⊆ |L|.

We now introduce serendipity which can generally be seen
as the measure of diversity in recommendations produced by
an algorithm and is an important characteristic for improving
the overall user experience.

Definition 4: In the context of recommender systems,
serendipity refers to the ability of an algorithm to recommend
unexpected and diverse items to the users to expand their taste
into neighboring interest areas.

III. RELATED WORK
Over the years, numerous techniques have been proposed
to deal with recommendation problem with Collaborative
Filtering [4], Content-based Filtering [6], [22] and Matrix
Factorization [7] among the prominent approaches. However,
the problem of news recommendation presents an additional
challenge that the item must be linked to a target set of readers
soon upon entry into the system.

In this section, we first review the news recommendation
problem and the techniques that were employed for this
specific task and then we shift our attention to generative
adversarial approaches for recommendations that are present
in literature.

A. NEWS RECOMMENDATION
The earliest news recommendations were focused on similar-
ity and classical machine learning algorithms. In [22], simi-
larity between user model and news articles are exploited to
generate personalized recommendations. For finding relevant
news items, [23] proposed the idea of using semantics of the
news articles. SF-IDF in combination with different semantic
similarity measures were used to find relevant news items
where the only semantic context they incorporated was based
on synonyms. The approach of using SF-IDF was further
extended by [24] in their work which used an updated SF-IDF
measure for finding semantic similarity while taking into
account the relationship between synonym sets. In a graph-
based approach, [25] discussed the use of knowledge graphs
by connecting named entities, events and places present in the
news articles.

The idea of employing collaborative filtering along with
content-based approach to make news recommendation
was also explored in research. One such example was
NewsDude [26] which recommended news by sequentially
employing three modules. A content-based recommender,
followed by classical collaborative component and a Naïve
Bayes classifier. In [27], a hybrid algorithm was presented
that combined content-based recommender system with
collaborative filtering to recommend sports news articles.
The inability of collaborative version to handle cold start
items was dissimulated by the content-based component.
In another such work [28] proposed the technique for fusion
of collaborative filtering and content-based modelling to
generate news recommendations. The content-based module
was used to construct user profile while user groups similar
to the active user were found in much the same way as in
a collaborative approach. Then a fusion model with user’s
current and potential interests was developed to recommend
news by finding similarity between the fusion model and
content of the news articles.

In a different approach for finding personalized news
articles, [29], [30], [31] used deep neural networks as
their recommendation model. In [29], a news encoder and
user encoder were trained such that
the news encoder
used attention mechanism to find topic information from
news articles through classification. The user encoder was

16612

VOLUME 12, 2024

---

<!-- PAGE 4 -->

S. Z. U. Hassan et al.: GCZRec: Generative Collaborative Zero-Shot Framework for Cold Start News Recommendation

constructed with the help of users click behavior on news
articles. The news encoder was constructed in much the
same way by [30]. However, they argued that capturing both
long-term and short-term interests of the users is necessary
for recommending highly personalized news items. The
long-term representations were captured by the embeddings
of user IDs while the short-term representation of the users
was guided by their browsed articles using a GRU network.
The idea of different users who click on the same article
with attention on different aspects was discussed by [31] in
their paper. They used convolutional neural network (CNN)
to learn news item representation from its title. The attention
mechanism was used at news-level and word-level in the news
model since a particular news may have different importance
or relevance for different users.

B. GENERATIVE METHODS
Among the first to use GAN for recommendation problem
were IRGAN [32] and GraphGAN [33]. These methods
explored the potential of GAN for recommender systems but
suffered from the well-known ‘‘label confusion’’ problem;
that is the model learning to label an item with positive and
negative labels at the same time resulting in performance
degradation of the model. As an application of minimax
optimization inherently present in GANs, [32] proposed
item recommendation as a generalized information retrieval
task with an objective function of matching top-k relevant
documents to the user.

In their paper, [33] proposed a model that set an objective
of generating the connectivity distribution for a given
vertex. In the recommendation application, the connectivity
distribution between a given vertex and all relevant items
was discussed. It was discussed by [34] in their paper that
treating missing user-item as negative rating can deteriorate
the recommendation performance since the negative ratings
could just be due to the user unaware of the item. They
used GANs to generate pairwise recommendation for each
user and item with positive-unlabeled sampling. The idea
of using conditional variant of GAN for recommendation
was presented by [35] in their research. Their GAN was
conditioned on fashion item as a class, given which another
complementary item was generated as a recommendation.

A GAN-based approach to handle the problem of data
imbalance in recommender systems was proposed by [36].
They made use of conditional Wasserstein GAN to generate
missing data for minority class to perform recommendations.
Their work used PacGAN in the discriminator architecture
with an aim to alleviate the performance of missing data
and improve the performance of recommendation models.
In another Wasserstein GAN based framework, [37] proposed
GAZRec model to generate synthetic feature representations
for both cold start news and user. To find the probability
of click behavior, their framework adopted a separate click
predictor module given a single user and news item. The
model did not use the behavioral representations to train
the generator for learning distribution of interactions directly

for items across different users. Due to the click prediction
objective of their work, the recommendation task is reduced
to binary classification and could not be extended to allow for
multi-label formulation of the problem.

In an earlier work on generative recommendations, [38]
proposed autoencoders are generators for collaborative rec-
ommendations in CAAE model and to extract latent factors
from user-item interactions, however, their framework did not
utilize the separate feature space of users and items to make
recommendation in case there was a cold start user or product.

IV. GCZREC FRAMEWORK
The architecture of our proposed GCZRec framework con-
sists of dual generator networks, implemented as conditional
Wasserstein GAN. The generator for news-to-user interaction
is trained on mapping a given news item to a distribution
representing users’ interest score for the item. Whereas the
companion generator for user-to-news interaction is trained
to generate a distribution of interaction scores of all news
items for a given user. Another important component of the
GCZRec model are two independent classifiers for news
and users. These pre-trained classifiers are used to perform
zero shot prediction of a cold start news or user in order
to provide the generator networks their conditional input for
synthesizing the interactions.

The proposed framework utilizes generative capabilities
of the traditional GAN architecture to synthesize interactions.
The individual classifiers are trained to use semantic space
and classify both seen and unseen news item and user in
order to provide our generators a conditional input. This
design of our model also opens the door for a novel way
of performing zero-shot extreme multi-label classification
efficiently. In the subsequent subsections, each component
of our model is discussed in detail. In Fig. 2, the overall
architecture of GCZRec is illustrated.

A. NOTATIONAL CONVENTIONS
In the remainder of this paper, the general notation used for a
news is N and for active user it is U. We also denote warm
news, cold news, warm user and cold user by wn, cn, wu,
cu respectively. The four possible cases to be considered are
thus represented as wnwu, wncu, cnwu, cncu. These cases are
represented in the model with the help of a 2-bit vector which
serves as the item-user state gate gs and can determine the
synthesizer to be used for generating interest vector. We refer
to the generator responsible for synthesizing interactions
for each user given a particular news item as genN and its
companion generator which is responsible for generating
interactions for each news given a user as genU. Apart from
these generators, the zero-shot classifiers for novel news item
and user will be called news label predictor PN and user label
predictor PU. These classifiers are jointly referred to as zero-
shot predictors. For encoding the identifiers of warm start
news item and warm start users and map them to a unique
numeric identifier, the encoders employed are referred to as
EN and EU respectively.

VOLUME 12, 2024

16613

---

<!-- PAGE 5 -->

S. Z. U. Hassan et al.: GCZRec: Generative Collaborative Zero-Shot Framework for Cold Start News Recommendation

FIGURE 2. Architecture of proposed GCZRec framework.

B. NEWS INTEREST SCORE GENERATOR GENN
The generator genN in GCZRec framework is responsible
for handling the states wnwu, cnwu and cncu. These input
states are determined prior to it by state gate gs. This network
synthesizes interaction score for each of the users given the
news item label yN as its conditional input. The relevancy
of an active news item for a user can be determined from
the corresponding value generated by the network where this
value is essentially an interest score. The overall output of
genN is a vector of interest scores predicted to be given
by each user in the system to the active news item. Each
position in this vector represents a unique user and the value
is a score that shows preference of that particular user for
the active item. With the value closer to +1 meaning that
the user would like this news article whereas any score
closer to -1 implying the user’s dislike for the item. In state
wnwu, the genN takes encoded news label as conditional
input from news encoder EN to generate the interaction
scores as its output distribution. For both states cnwu and
cncu the generator genN uses label provided by PN for
synthesizing interaction scores. Due to its stability and the
inherent sparsity in the historical interactions present in
our data, we used a conditional gan that uses Wasserstein
loss called conditional Wasserstein GAN (cWGAN) with
the critic network during training to implement the genN
model.

The general objective function of cWGAN is given as:

minGmaxDV (D, G) = Ec,x∼true[D(xtrue, c)]
− Ec,z[D(G(z, c)), c]

(3)

In the context of news recommendation, the generator genN
aims to minimize this combined objective function, while
the critic aims to maximize it. This leads to a minimax
game where the generator tries to produce realistic synthetic
samples, and the critic tries to effectively distinguish between
real and synthetic samples. Where Ec,x true[D(xtrue,c)] repre-
sents expectation over real data whereas Ec,z[D(G(z,c)),c] is
the expectation over values generated by synthesis. In terms
of generating interest scores of users given news item as
conditional input.

The objective function of genN can therefore be stated as:

minLgenN

= −EyN ,Z ∼Pg(x)

[D(G(z, yN )), yN ]

(4)

Formally, this generator takes random noise z from a guassian
distribution g(x) as latent input and given a news class label
yN, it generates a vector of synthetic interest scores G(·)
for all users and aims to minimize the distance between
fake and ground truth interactions between user-news pairs.
The critic evaluates how well the generated scores match
real user interest scores given the corresponding news item
and produces D(·) which is the output when it evaluates

16614

VOLUME 12, 2024

---

<!-- PAGE 6 -->

S. Z. U. Hassan et al.: GCZRec: Generative Collaborative Zero-Shot Framework for Cold Start News Recommendation

FIGURE 3. Flow diagram of news recommendation in GCZRec framework.

the sample G(·) generated by genN. As part of adversarial
training, the critic network aims to discern the synthetic
interaction distribution from the real one that is produced by
the generator. The activation used in the dense and output
layers of this network are LeakyReLU and tanh respectively.
The critic network uses linear activations instead of sigmoid
in the output layer and its output is the approximation of
Wasserstein distance hence assigning lower values to fake
interactions. In the dense layers of this model, LeakyReLU
activations are used. During training, the weights of the critic
are clamped to a small range and this network is updated five
times compared to a single update of the generator in order to
improve the generation quality.

C. USER INTEREST SCORE GENERATOR GENU
The input states determine the use of genU for synthesizing
interest scores for active news. These states are handled by
gs. The genU takes the user class label yU of the active user
as its conditional input and generates fake interest scores for
each news item in the system. The possible states managed
by the genU are wnwu, wncu and cncu. The output of genU
is a vector of interest scores showing preferences given by
this user to each one of the news items. Each position of this
interaction vector representing a unique news and the value
at that index indicating a score in range -1 to +1 to show
if that particular item can be interesting for the active user.
For state wnwu, the conditional variable for this model is
provided by the user encoder EU as yU. For cases wncu and
cncu the predicted class label ˆyU from the zero-shot predictor
PU is used. Similar to genU the training of this network
is done in an adversarial manner by employing a cWGAN
and a critic that uses Wasserstein loss. The activation in the
dense layers of both generator and critic are LeakyReLU
while the output layer of the critic uses linear activation
and tanh activation is used for the output
layer of the
synthesizer.

The objective function of genU can be stated as:

minLgenU

= −EyU ,Z ∼Pg(x)

[D(G(z, yU )), yU ]

(5)

The model genU takes latent vector z from the gaussian
distribution as input along with user class label yU to generate
the distribution G(·) of synthetic interest scores for all news
items with respect to the active user. The critic outputs its
evaluation D(·) of the generated interaction scores produced
and genU tries to minimize the loss between real and fake
distribution of interaction scores.

D. WARM START ENCODERS
For warm start news, the class label yN to be served to the
interest score generator genN is encoded by mapping the raw
identifier of the active news item to a unique numeric id. This
encoded id is then used by EN to collect the corresponding
label of the news from historical data. In the same way, warm
start user id is encoded by EU to a unique numeric id in order
to extract the available class yU of this active warm start user
in order to provide conditional input to genU network.

E. LATENT FEATURE REPRESENTATION
In the GCZRec approach, we represent each news item N
as a latent feature vector, denoted by δ. This representation
is obtained by feature extraction process θ using pre-trained
embedding to extract informative features from the textual
content of the news item. The feature representation yielded
is δ = θ(N).

Since the MIND and Addressa datasets do not contain
any explicit user entity features, we transformed each user
U into latent feature representation λ with the help of her
historical interactions with the news categories. All the news
the user interacted with previously are treated as positive
samples and use to extract the hidden features. These features
are constructed as a process ρ which converts the list of
categories and subcategories of each interacted news into
one-hot encoding. Hence λ = ρ(U) becomes the user profile
of active user.

F. ZERO-SHOT CLASSIFIERS
The cold start problem for both news items and users is treated
as zero-shot classification task in the GCZRec approach. For

VOLUME 12, 2024

16615

---

<!-- PAGE 7 -->

S. Z. U. Hassan et al.: GCZRec: Generative Collaborative Zero-Shot Framework for Cold Start News Recommendation

TABLE 1. Statistics of adressa and MIND datasets.

these zero-shot predictions, we employ two classifiers that
use the latent feature representation to predict a class label
for item and user. As a result, this allows the predictors to
leverage hidden collaborative signals between items and also
users for predicting labels in terms of similarity in the latent
feature space.

1) NEWS LABEL PREDICTOR PN
Given the latent news feature representation δ, we classify
a novel item into one of K predefined categories, denoted
by yN1, yN2 , yN3,. . ., yNK where K is the total number of
news categories in the domain. We implement the news label
predictor as a 1D convolutional neural network with softmax
activation in the output layer for prediction. The classifier
|δ) for the given news item
calculates the probability P(yNi
belonging to class yNi as stated in equation 6.

P(yNi

|δ) =

ewi · δ
j=1 ewj · δ

Pk

The assigned news category ˆyN is expressed as:

ˆyN = arg max

i

P(yNi

|δ)

(6)

(7)

2) USER LABEL PREDICTOR PU
This classifier is used to predict the label for a user based on
its feature representation λ. Similar to news label predictor,
the architecture of this model is a 1D convolutional network
|λ)
with softmax function for finding the probability P(yUi
of the user falling into one of the yU1 , yU2, yU3,. . ., yUM
categories. The posterior probability for finding the user label
and label assignment is shown as follows:

P(yUi

|λ) =

Pk

ewi · λ
j=1 ewj · λ
P(yUi

i

ˆyU = arg max

(8)

(9)

|λ)

V. EXPERIMENTS
A. DATASET DETAILS
the experiments, we used the publicly available
For
MIND [20] and Adressa [21] news recommendation datasets.
The key statistics for both of these datasets are provided in
Table 1. The datasets contains click behavior of users for news
items. The data include information like impressions, news
categories, subcategories, abstract and textual content.

B. DATASET PREPROCESSING
From the users’ behavioral data provided including their
impressions log and news click history, we first sampled 70%
data for training our model and left the 30% for post-training
evaluation. For each user, the news item for which they have
positive interactions were found by extracting the news id
among their news click history and also from the impressions
where the user had a ‘‘1’’ as a click behavior for a particular
news. We encoded all the positive interactions between user
and news as the value ‘‘1’’ during training data construction.
The negative interactions between users and news were found
when the user did not click the news and hence has a 0 for that
particular news id in the impressions log. We encoded this
negative interaction as ‘‘-1’’ in the training data. For all the
news not present in either a user’s historical interactions or
impressions log, it was assumed that the user was never show
the news item and did not interact with it. These interactions
are encoded as ‘‘0’’ for training. Moreover, for indexing
purpose, each news id and user id is mapped to a unique
numeric news id and numeric user id respectively. Based on
their numeric indices, the final training set for genN was
constructed by using the numeric id as index for a unique
instance (row) and each numeric user id as a feature value
(column). In a similar manner, the final training data for genU
was constructed by using numeric user id as index for the
instance (row) and each numeric news id as index for feature
value (column).

C. IMPLEMENTATION
For constructing latent feature representations, we used
hierarchical clustering to assign contextual labels to each
news item based on its rich textual features. The number of
clusters selected based on silhouette score and discernment
was 32. For user labels,
the hyperparameter value for
number of classes was set to 18 classes. The embedding
size for news and user is set to 300 to allow for baseline
comparison. For news, pre-trained Word2Vec embedding
are used whereas for users we used count vectorization to
perform the behavior encoding. The same architecture for
genN and genU is used with a dropout rate of 0.5, learning
rate of 0.0002, LeakyReLU as activation in the dense layers,
tanh as non-linearity for the generator output layer. Adam
is used as optimizer with hyperparameters β1 =0.9 and
β2 =0.999. As part of the cWGAN, the critic is trained with
clipped weights. Both the zero-shot predictors are trained as
multi-class classifiers with conv1d hidden layers, batch norm
regularization, dropout rate of 0.5, learning rate of 0.0005 and
softmax activation.

D. BASELINE MODELS
In terms of the recommendation objective, the GCZRec
framework is compared with the existing recommender
models to validate the performance of the proposed approach.
The models are listed as:

• GAZRec-NPA [37]: A three-tower generative zero-
framework to generate generalized behavior

shot

16616

VOLUME 12, 2024

---

<!-- PAGE 8 -->

S. Z. U. Hassan et al.: GCZRec: Generative Collaborative Zero-Shot Framework for Cold Start News Recommendation

TABLE 2. Comparative results of GCZRec on MIND and adressa datasets in exclusively cold start case.

TABLE 3. Comparative results of GCZRec on MIND and adressa datasets in mixed cold start and warm start case.

representations of users and items for recommendation
and then use these representation for cold start and warm
start predictions using a neural click predictor.

• GNUD [39]: The user and news interactions are treated
as high-order graph in order to exploit latent preference
factors of the user to perform recommendation.

• NAML [40]: A neural news recommendation approach
with attentive multi-view learning in which user repre-
sentation is learned using their browsed history and other
information as well as news attributes such as title and
category are used for item representation.

E. EVALUATION METRICS
To evaluate the performance of the proposed GCZRec
four evaluation mea-
framework against
sures are used as performance indicators. These metrics
are Area Under Curve (AUC), normalized Discounted
Cumulative Gain (nDCG@k) and Mean Average Precision
(MAP).

the baseline,

The AUC can be measured in terms of true positive rate

(TPR) and false positive rate (FPR) as:

AUC ≈

n
X

i=1

1
2

(TPRi + TPRi−1)(FPRi − FPRi−1)

(10)

The nDCG@k is a measure of ranking quality in the list
of recommended items with IDCG as the ideal DCG and

position k:

nDCG@k =

DCG@k
IDCG@k

(11)

To measure the performance of recommender system using
average precision given top-k recommendations over multiple
values of k we use MAP which is defined as:

MAP =

PK

k=1 Average Precision@k
K

(12)

F. TEST ENVIRONMENT
For model training and performance evaluation we divided
the test data into two distinct sets. From the total test data
we selected 50% cold start items for evaluating the model
in an exclusively cold start setting. The remaining cold start
items along with the warm start data was used to generate
recommendations for mixed cold-warm news items.

The threshold value for recommendation of a given item is
fixed to 0.5 and the values used for hyperparameter k are 1,
5 and 10.

VI. RESULTS AND DISCUSSION
In this section, the effectiveness of the proposed approach
is evaluated and the results indicating the performance
on benchmark datasets are reported. These results are
summarized in Table 2 for cold start case and in Table 3 for
mixed case of both cold start and warm start items.

VOLUME 12, 2024

16617

---

<!-- PAGE 9 -->

S. Z. U. Hassan et al.: GCZRec: Generative Collaborative Zero-Shot Framework for Cold Start News Recommendation

A break down of model performance into different aspects
is needed in order to effectively discuss the outcomes
of GCZRec framework. These performance aspects are
presented in the following subsections.

A. CLASSIFICATION PERFORMANCE
The performance of generator networks in the GCZRec
for scores generation is done in the context of number of
correct interest score generation for a given news item. With
the help of threshold value, each individual interest score
produced in the interest vector can itself be treated as a
binary class prediction. The combined performance of these
positive and negative scores generation are represented by
the AUC values as presented in Table 2 and Table 3. The
results show significant improvement in cold start case for
MIND but slightly under-performed on Adressa against the
baseline for mixed cold-warm start case. This may be due to
the label encoding scheme used for the Adressa categories.
It can be further investigated whether category condensation
in the dataset affected the prediction accuracy.

B. PRECISION-RECALL TRADE-OFF
The GCZRec model offers significant improvement over
the existing approaches and the positional relevance of
recommended news items are taken into account by the
synthetic interaction generators. For both MIND and Adressa
dataset, the MAP score given by the proposed model shows
an improvement in both cold start and mixed warm-cold
start cases. But compared to purely cold start items, the
improvements in mixed case recommendations were much
more significant. The precision-recall curve for k=1, 5 and
10 for MIND and Adressa datasets in both cases is illustrated
in Fig. 4 and Fig. 5.

C. RANKING QUALITY
In terms of the ranking quality of news items in both cold
start and warm start cases, the proposed GCZRec framework
clearly outperforms baseline models with the highest average
improvement of +0.1113 is observed when top-5 items are
considered as shown by ndcg@k values for k=1, 5 and
10. The overall value of relative ranking in the proposed
approach can be attributed to the genN and genN learning
the underlying interest distribution from the data to produce
synthetic interest scores. These scores in their raw form are
used as is to provide the ranking of relevant items that are
recommended.

D. SERENDIPITY
For the inherently challenging and subjective aspect of
evaluating the proposed system in terms of expanding the
interest of users into neighbouring news categories, we model
the results of GCZRec as a collaborative recommendation
outcome. This is done in an implicit manner as the
output generated by genN and genU use the interaction
between similar user and news. We measure the diversity
of recommendations produced using GCZRec framework by

TABLE 4. Percentage of novel news.

FIGURE 4. Precision-recall curve for cold start case.

FIGURE 5. Precision-recall curve for mixed cold-warm start case.

finding the percentage of new high interest news item found
over 5, 10, 25 and 50 generations given the same user as input
to genU. A summary of this is presented in Table 4. It can
also be argued that the diversity is measurable for generations
produced by the genN in the same manner.

Based on the comparative results, it can be stated that the
proposed GCZRec framework provides more accurate and
relevant ranked recommendation of cold start and warm start
news items to users also incorporates diversity by leveraging
latent collaborative information present in feature space of
users and items.

VII. CONCLUSION
In this paper, we presented the GCZRec framework for cold
start news recommendation. We formulated the problem of
cold start recommendation as zero-shot classification task
and proposed that these recommendations can be diverse
and have serendipity if user and item information are
implicitly used during training. Unlike existing models,
the GCZRec approach allows the interest scores to be
generated directly for a given news or user in both warm
start and cold start cases. Two separate wCGAN networks
are trained on interaction between users and news items in
order to allow collaborative signals to be implicitly used
for producing synthetic interactions at testing time. For any
unseen user or news item, the model makes use of zero-shot
predictors implemented as 1D-CNN classifiers. Results on

16618

VOLUME 12, 2024

---

<!-- PAGE 10 -->

S. Z. U. Hassan et al.: GCZRec: Generative Collaborative Zero-Shot Framework for Cold Start News Recommendation

two benchmark datasets indicate that our proposed approach
offers significant improvement in the accuracy and ranking
of news items for cold start recommendation and also sets
a standard for incorporating serendipity by implicitly using
collaborative information with a generative recommender
system in zero-shot manner.

A. LIMITATIONS AND FUTURE WORK
The current limitation of our model include its inability
to consider the correlation between news items and tem-
poral relation between news clicks. Both of these aspects,
if incorporated, can be important in further improving the
recommendation quality of the GCZRec model.

In future work, we also aim to improve our framework to
allow cross-domain recommendation problems to be handled.
For this, existing knowledge distillation models can be used
to allow learned knowledge from source domain to be
transferred to a model set to recommend items that are present
in target domain.

REFERENCES
[1] A. Bermes, ‘‘Information overload and fake news sharing: A transactional
stress perspective exploring the mitigating role of consumers’ resilience
during COVID-19,’’ J. Retailing Consum. Services, vol. 61, Jul. 2021,
Art. no. 102555.

[2] S. Feng, J. Meng, and J. Zhang, ‘‘News recommendation systems in the
era of information overload,’’ J. Web Eng., vol. 20, no. 2, pp. 459–470,
Mar. 2021.

[3] M. Zihayat, A. Ayanso, and X. Zhao, ‘‘A utility-based news recommenda-

tion system,’’ Decis. Support Syst., vol. 117, pp. 14–27, Feb. 2019.

[4] D. Goldberg, D. Nichols, B. M. Oki, and D. Terry, ‘‘Using collaborative
filtering to weave an information tapestry,’’ Commun. ACM, vol. 35, no. 12,
pp. 61–70, Dec. 1992.

[5] Y. Koren, S. Rendle, and R. Bell, ‘‘Advances in collaborative filtering,’’
in Recommender Systems Handbook. Boston, MA, USA: Springer, 2021,
pp. 91–142.

[6] P. De Handschutter, N. Gillis, and X. Siebert, ‘‘A survey on deep matrix
factorizations,’’ Comput. Sci. Rev., vol. 42, Nov. 2021, Art. no. 100423.
[7] M. J. Pazzani and D. Billsus, ‘‘Content-based recommendation systems,’’
in The Adaptive Web: Methods and Strategies of Web Personalization.
Berlin, Germany: Springer, 2007, pp. 325–341.

[8] C. N. Sunilkumar, ‘‘A review of movie recommendation system: Limita-
tions, survey and challenges,’’ ELCVIA Electron. Lett. Comput. Vis. Image
Anal., vol. 19, no. 3, pp. 18–37, Sep. 2020.

[9] P. Lops, D. Jannach, C. Musto, T. Bogers, and M. Koolen, ‘‘Trends
in content-based recommendation: Preface to the special
issue on
recommender systems based on rich item descriptions,’’ User Model. User-
Adapted Interact., vol. 29, no. 2, pp. 239–249, Apr. 2019.

[10] M. H. Mohamed, M. H. Khafagy, and M. H. Ibrahim, ‘‘Recommender
systems challenges and solutions survey,’’ in Proc. Int. Conf. Innov. Trends
Comput. Eng. (ITCE), Feb. 2019, pp. 149–155.

[11] J. Li, M. Jing, K. Lu, L. Zhu, Y. Yang, and Z. Huang, ‘‘From zero-shot
learning to cold-start recommendation,’’ in Proc. AAAI Conf. Artif. Intell.,
vol. 33, 2019, pp. 4189–4196.

[12] W. Wang, V. W. Zheng, H. Yu, and C. Miao, ‘‘A survey of zero-shot
learning: Settings, methods, and applications,’’ ACM Trans. Intell. Syst.
Technol., vol. 10, no. 2, pp. 1–37, Mar. 2019.

[13] S. Yin and X. Luo, ‘‘A survey of learning-based methods for cold-start,
social recommendation, and data sparsity in e-commerce recommendation
systems,’’ in Proc. 16th Int. Conf. Intell. Syst. Knowl. Eng. (ISKE),
Nov. 2021, pp. 276–283.

[14] T. Wu, E. K.-I. Chio, H.-T. Cheng, Y. Du, S. Rendle, D. Kuzmin,
R. Agarwal, L. Zhang, J. Anderson, S. Singh, T. Chandra, E. H. Chi,
W. Li, A. Kumar, X. Ma, A. Soares, N. Jindal, and P. Cao, ‘‘Zero-shot
heterogeneous transfer learning from recommender systems to cold-start
search retrieval,’’ in Proc. 29th ACM Int. Conf. Inf. Knowl. Manage.,
Oct. 2020, pp. 2821–2828.

[15] H. Ding, Y. Ma, A. Deoras, Y. Wang, and H. Wang, ‘‘Zero-shot

recommender systems,’’ 2021, arXiv:2105.08318.

[16] R. J. Ziarani and R. Ravanmehr, ‘‘Serendipity in recommender systems:
A systematic literature review,’’ J. Comput. Sci. Technol., vol. 36, no. 2,
pp. 375–396, Apr. 2021.

[17] D. Kotkov, J. Veijalainen, and S. Wang, ‘‘How does serendipity affect
diversity in recommender systems? A serendipity-oriented greedy algo-
rithm,’’ Computing, vol. 102, no. 2, pp. 393–411, Feb. 2020.

[18] S. Inoue and M. Tokumaru, ‘‘Serendipity recommender system for
academic disciplines,’’ in Proc. Joint 11th Int. Conf. Soft Comput. Intell.
Syst. 21st Int. Symp. Adv. Intell. Syst. (SCIS-ISIS), Dec. 2020, pp. 1–4.
[19] T. Dorjmaa and T. Shin, ‘‘Evaluating the quality of recommendation

system by using serendipity measure,’’ vol. 25, no. 4, pp. 89–103, 2019.

[20] F. Wu, Y. Qiao, J.-H. Chen, C. Wu, T. Qi, J. Lian, D. Liu, X. Xie, J. Gao, and
W. Wu, ‘‘MIND: A large-scale dataset for news recommendation,’’ in Proc.
58th Annu. Meeting Assoc. Comput. Linguistics, 2020, pp. 3597–3606.

[21] J. A. Gulla, L. Zhang, P. Liu, Ö. Özgöbek, and X. Su, ‘‘The adressa dataset
for news recommendation,’’ in Proc. Int. Conf. Web Intell., Aug. 2017,
pp. 1042–1048.

[22] M. Kompan and M. Bieliková, ‘‘Content-based news recommendation,’’ in
Proc. 11th Int. Conf. e-commerce Web Technol. (EC-Web) (Lecture Notes
in Business Information Processing). Berlin, Germany: Springer, 2010,
pp. 61–72.

[23] M. Capelle, F. Frasincar, M. Moerland, and F. Hogenboom, ‘‘Semantics-
based news recommendation,’’ in Proc. 2nd Int. Conf. Web Intell., Mining
Semantics, Jun. 2012, pp. 1–9.

[24] M. Moerland, F. Hogenboom, M. Capelle, and F. Frasincar, ‘‘Semantics-
based news recommendation with SF-IDF+,’’ in Proc. 3rd Int. Conf. Web
Intell., Mining Semantics, Jun. 2013, pp. 1–8.

[25] K. Joseph and H. Jiang, ‘‘Content based news recommendation via shortest
entity distance over knowledge graphs,’’ in Proc. Companion World Wide
Web Conf., May 2019, pp. 690–699.

[26] D. Billsus and M. J. Pazzani, ‘‘User modeling for adaptive news access,’’
User Model. User-Adapted Interact., vol. 10, pp. 147–180, Jun. 2000.
[27] P. Lenhart and D. Herzog, ‘‘Combining content-based and collaborative
in Proc.

filtering for personalized sports news recommendations,’’
CBRecSys@ RecSys, 2016, pp. 3–10.

[28] W. Yang, R. Tang, and L. Lu, ‘‘News recommendation method by fusion
of content-based recommendation and collaborative filtering,’’ J. Comput.
Appl., vol. 36, no. 2, p. 414, 2016.

[29] C. Wu, F. Wu, M. An, Y. Huang, and X. Xie, ‘‘Neural news recommenda-
tion with topic-aware news representation,’’ in Proc. 57th Annu. Meeting
Assoc. Comput. Linguistics, 2019, pp. 1154–1159.

[30] M. An, F. Wu, C. Wu, K. Zhang, Z. Liu, and X. Xie, ‘‘Neural news
recommendation with long- and short-term user representations,’’ in Proc.
57th Annu. Meeting Assoc. Comput. Linguistics, 2019, pp. 336–345.
[31] C. Wu, F. Wu, M. An, J. Huang, Y. Huang, and X. Xie, ‘‘NPA:
Neural news recommendation with personalized attention,’’ in Proc. 25th
ACM SIGKDD Int. Conf. Knowl. Discovery Data Mining, Jul. 2019,
pp. 2576–2584.

[32] J. Wang, L. Yu, W. Zhang, Y. Gong, Y. Xu, B. Wang, P. Zhang, and
D. Zhang, ‘‘IRGAN: A minimax game for unifying generative and
discriminative information retrieval models,’’ in Proc. 40th Int. ACM
SIGIR Conf. Res. Develop. Inf. Retr., Aug. 2017, pp. 515–524.

[33] H. Wang, J. Wang, J. Wang, M. Zhao, W. Zhang, F. Zhang, X. Xie,
and M. Guo, ‘‘GraphGAN: Graph representation learning with generative
adversarial nets,’’ in Proc. AAAI Conf. Artif. Intell., vol. 32, 2018, pp. 1–8.
[34] Y. Zhou, J. Xu, J. Wu, Z. T. Nasrabadi, E. Korpeoglu, K. Achan, and J. He,
‘‘GAN-based recommendation with positive-unlabeled sampling,’’ 2020,
arXiv:2012.06901.

[35] S. Kumar and M. D. Gupta, ‘‘c+GAN: Complementary fashion item

recommendation,’’ 2019, arXiv:1906.05596.

[36] W. Shafqat and Y.-C. Byun, ‘‘A hybrid GAN-based approach to solve
imbalanced data problem in recommendation systems,’’ IEEE Access,
vol. 10, pp. 11036–11047, 2022.

[37] M. A. Alshehri and X. Zhang, ‘‘Generative adversarial zero-shot learning
for cold-start news recommendation,’’ in Proc. 31st ACM Int. Conf. Inf.
Knowl. Manage., Oct. 2022, pp. 26–36.

[38] D.-K. Chae, J. A. Shin, and S.-W. Kim, ‘‘Collaborative adversarial
autoencoders: An effective collaborative filtering model under the GAN
framework,’’ IEEE Access, vol. 7, pp. 37650–37663, 2019.

[39] L. Hu, S. Xu, C. Li, C. Yang, C. Shi, N. Duan, X. Xie, and M. Zhou,
‘‘Graph neural news recommendation with unsupervised preference dis-
entanglement,’’ in Proc. 58th Annu. Meeting Assoc. Comput. Linguistics,
2020, pp. 4255–4264.

VOLUME 12, 2024

16619

---

<!-- PAGE 11 -->

S. Z. U. Hassan et al.: GCZRec: Generative Collaborative Zero-Shot Framework for Cold Start News Recommendation

[40] C. Wu, F. Wu, M. An, J. Huang, Y. Huang, and X. Xie, ‘‘Neu-
ral news recommendation with attentive multi-view learning,’’ 2019,
arXiv:1907.05576.

SYED ZAIN UL HASSAN was born in Karachi,
Pakistan. He received the M.C.S. degree from
the University of Karachi, in 2014, and the M.S.
degree in computer science from the National
University of Computer and Emerging Sciences,
in 2018, where he is currently pursuing the Ph.D.
degree in computer science. He has more than
eight years of teaching experience and was a
Developer at a software service provider for almost
two years. His research interests include machine
learning, generative AI, recommendation systems, and large language model.

MUHAMMAD RAFI was born in Karachi,
Pakistan. He received the B.S. and M.S. degrees
in computer science from the FAST-Institute
of Computer Science, University of Karachi,
Pakistan, in 1996 and 2000, respectively, and the
Ph.D. degree in computer science in 2017. He has
more than ten years of experience in software
development and also a Consultant for the local
software industry. His current research interests
include algorithm development, machine learning,
information retrieval, text/data mining, time series analysis, and natural
travel grant awards for
language processing. He has received several
presenting his work at the top conferences. He has served as a Judge
and a Technical Quality Review Team at many versions for IEEEXtreme
Programming Competitions. He has served as a reviewer for various
international journals of high impact.

JAROSLAV FRNDA (Senior Member,
IEEE)
was born in Slovakia, in 1989. He received the
M.Sc. and Ph.D. degrees from the Department of
Telecommunications, VSB—Technical University
of Ostrava, Czech Republic, in 2013 and 2018,
respectively. He is currently an Assistant Professor
with the University of ˘Zilina, Slovakia. He has
authored or coauthored more than 85 journal
articles in Web of Science. His research interests
include the quality of multimedia services in IP
networks, data analysis, and machine learning algorithms. In 2022, he was
the Finalist of the Category Outstanding Scientist in Slovakia under the age
of 35-ESET Science Award, in 2022.

16620

VOLUME 12, 2024

<!-- MARKITDOWN CONVERSION -->

<!-- Full MarkItDown conversion for formatting fidelity. -->

Received13December2023,accepted21January2024,dateofpublication26January2024,dateofcurrentversion5February2024.
DigitalObjectIdentifier10.1109/ACCESS.2024.3359053
GCZRec: Generative Collaborative
Zero-Shot Framework for Cold
Start News Recommendation
SYEDZAINULHASSAN 1,MUHAMMADRAFI 1,
ANDJAROSLAVFRNDA 2,3,(SeniorMember,IEEE)
1DepartmentofComputerScience,SchoolofComputing,NationalUniversityofComputerandEmergingSciences,Islamabad44000,Pakistan
2DepartmentofQuantitativeMethodsandEconomicInformatics,FacultyofOperationandEconomicsofTransportandCommunications,UniversityofZ˘ilina,
01026Z˘ilina,Slovakia
3DepartmentofTelecommunications,FacultyofElectricalEngineeringandComputerScience,VSB—TechnicalUniversityofOstrava,70800Ostrava,Czech
Republic
Correspondingauthor:JaroslavFrnda(jaroslav.frnda@uniza.sk)
ThisworkwassupportedbytheEuropeanUnionwithintheREFRESHProject—ResearchExcellenceforRegionSustainabilityand
High-TechIndustriesoftheEuropeanJustTransitionFundunderGrantCZ.10.03.01/00/22003/0000048.
ABSTRACT The aim of personalized news recommendation is to suggest news stories to the users that
aremostinterestingforthem.Toimprovetheuserexperience,itisimportantthatthesenewsitemsarenot
onlyrelevanttotheuserbutalsogetrecommendedtothemassoonastheyareavailable.Theinabilityof
traditional collaborative filtering approach to recommend such cold start items has led to techniques that
incorporate latent features of items in order to make cold start recommendations such as content based
filtering and deep neural network-based approaches. However, these existing techniques do not make use
of any collaborative information between users and items as well as latent features at the same time and
thus fail to provide any serendipity which is an important aspect of any recommender system. Moreover,
theseunderlyingcollaborativesignalsbetweenusersanditemsarecrucialtoimprovingtheoverallqualityof
recommendersystemsandcanalsobeutilizedtomakecoldstartrecommendations.Inthispaper,wepropose
theGenerativeCollaborativeZero-ShotRecommenderSystemframework(GCZRec)whichmakesuseof
boththelatentuseranditemfeaturesaswellastheunderlyingcollaborativeinformationtogenerateboth
warmstartandcoldstartrecommendations.Weevaluateourframeworkfornewsrecommendationtaskgiven
coldstartandwarmstartcasesforbothusersandnewsitems.Wealsodiscussthatourmodelcanbeplugged
inandusedaspreprocessingtoimprovetheperformanceofanexistingrecommendersystem.
INDEXTERMS Newsrecommendation,coldstartproblem,zero-shotlearning,recommendersystem.
I. INTRODUCTION interestingandpersonalized.Butcomparedtorecommending
The improvement in media technology and online services movies and products, news article recommendations often
have resulted in an overload of information especially with entail some additional challenges such as the latest news
online news articles as the people realize the need to be articles being posted frequently and lacking any historical
well-informed at all times [1], [2]. Recommender systems interactions that can be used for recommending these news
canthereforeimprovetheuserexperiencebysuggestingnews items[3].Thisseverecaseofcoldstartproblemisachallenge
articles that are most recent, relevant and contain value for in news recommendations. Moreover, from the user point
her.Thesesystemscanhelptheusersfindinformationthatis of view, these news stories need to be recent but highly
personalized, while from the item perspective, it should be
The associate editor coordinating the review of this manuscript and recommended to the users based strictly on its relevance to
approvingitforpublicationwasChaoTong . thoseparticularusers.
2024TheAuthors.ThisworkislicensedunderaCreativeCommonsAttribution-NonCommercial-NoDerivatives4.0License.
16610 Formoreinformation,seehttps://creativecommons.org/licenses/by-nc-nd/4.0/ VOLUME12,2024

S.Z.U.Hassanetal.:GCZRec:GenerativeCollaborativeZero-ShotFrameworkforColdStartNewsRecommendation
The conventional collaborative recommendation algo-
rithms rely on historical interaction data of users and items
to find hidden patterns based on similarity [4], [5]. The
performance of these algorithms decreases when the data
contains missing user interaction entries for the items. This
lackofdataismostlyseeninthecaseofnewsarticleswhich
are often posted without any prior interaction information.
Thisleadstoaseverecaseofcoldstartproblem.
Other techniques such as Matrix Factorization [6] and
content-based filtering [7] also suffer from cold start user
problem[8],[9],[10].IncaseofMatrixFactorization,itcan FIGURE1. Illustrationofthecoldstartnewsrecommendationproblem.
additionally suffer from both over-fitting and under-fitting
giventheavailablehistoricaldata.Anotherproblemthatboth
and items. In the same way that an unseen class label is
of these techniques face is the assumption that features are
used for prediction by leveraging the features of the novel
always independent. This condition is difficult to hold true
sample, the conditional input of the generator network can
in most real-world scenarios where not only the features
also be learned from the available item and user feature
but items also have relative dependence on features and
representations.
themselves.
Based on the previous discussion, we propose a novel
The cold start problem in recommender systems can be
recommender system framework, GCZRec, to synthesize
remodeledasaclassicalzero-shotlearningtaskwhichcomes
bothcoldstartandwarmstartinteractionsforusersandnews
from the computer vision domain [11], [12]. In zero-shot
items.Ourtechniqueutilizesthehiddenfeatureinformation
classification, the set of classes in the training data and set
of users and items to perform cold start recommendations
of classes in the samples to be classified can be disjoint.
as zero-shot predictions. The proposed model is capable
Similarly, in cold start item recommendations, the aim is to
of learning collaborative signals between users and among
predictwhetheranitemshouldberecommendedtoapartic-
items to generate interactions thus allowing diverse rec-
ularuserwithoutanyavailablehistoricalinteractionsforthat
ommendations. The framework also allows the ranking of
item. In cold start user case, items are to be recommended
these recommendations. At its core, GCZRec framework
toaparticularuserforwhichtherearenoexistinghistorical
consists of two separate classifiers for zero-shot labelling
information [13]. Following this intuition, the features of
of cold start news and cold start user. These predicted
news items and users can be used to deduce the behavioral
classes are used as input to conditional Wasserstein GAN
context of cold start items and users in recommendation
(cWGAN) for generating interactions. During training, two
schemejustlikeaclasslabelcanbepredictedforanunseen
separate generator networks are independently trained such
datasampleusingthegeneralizationfromknownsamplesin
that each training sample of the first network represent a
zero-shotclassification.Someexistingstudies[14],[15]have
newsitemwithinteraction.Thisgeneratornetworkistrained
usedthisrelationtoproposerecommendationmodelsforcold
on samples each one of which is an interaction vector
startitems.
containing both interactions of users for news items. The
Butthesetechniquesdonottakeintoaccountserendipity,
experimentswereconductedontwopubliclyavailablenews
whichisanimportantaspectofarecommendersystem[16],
recommendation datasets Microsoft News Dataset (MIND)
[17],[18],[19].Thislackofdiversitystemsfromtheinability
[20] and Addressa [21] in order to provide the proof of
of these models to make use of the latent collaborative
conceptforourresearch.Furthermore,ourframeworkallows
information between users as well as items. These neigh-
this problem to be formulated as an extreme multi-label
borhoodsignalsarethereforeimportanttomakefine-grained
classification task where the class labels are news items to
recommendationsthatarenotonlyrelevanttotheactiveusers
berecommended.
butalsoprovidediversityinchoicesforthem.
Themaincontributionsofthisresearchareasfollows:
We observe that by directly synthesizing the interactions
based on feature representations can eliminate the need • We propose a novel GCZRec framework capable of
for any external click predictor model and can also pro- usinglatentcollaborativeinformationtomakebothcold
vide an effective method to not only allow item-to-user startandwarmstartrecommendationsofnewsitemsin
interactions prediction but also projection of user-to-item generativemannerandallowingtherecommendeditems
interactions. This synthesis of interactions can also allow toberanked.
us an efficient method to rank the predicted interactions. • We present a formulation of cold start recommenda-
Thiscanbeachievedbyincorporatingagenerativenetwork tion as zero-shot learning problem and utilize hidden
withconditionalinformationtolearnthelatentcollaborative features of both users and items in order to make
information between users and items. This allows us to recommendations.
use these hidden patterns in the available historical data • Our framework can also be used for typical extreme
to directly synthesize the interactions for cold start users multi-label classification task and provides an efficient
VOLUME12,2024 16611

S.Z.U.Hassanetal.:GCZRec:GenerativeCollaborativeZero-ShotFrameworkforColdStartNewsRecommendation
approachforpredictingthesubsetoflabelsfromalarge III. RELATEDWORK
spacegivenanewinstance. Over the years, numerous techniques have been proposed
|     |     |     |     |     | to deal with | recommendation     | problem   | with | Collaborative   |
| --- | --- | --- | --- | --- | ------------ | ------------------ | --------- | ---- | --------------- |
|     |     |     |     |     | Filtering    | [4], Content-based | Filtering | [6], | [22] and Matrix |
II. PRELIMINARIES
The goal of a recommender system is to present the users Factorization[7]amongtheprominentapproaches.However,
with an ordered set of items which are ranked based on the theproblemofnewsrecommendationpresentsanadditional
preference and relevance of these items for each particular challengethattheitemmustbelinkedtoatargetsetofreaders
user. This section defines the relevant concepts pertaining soonuponentryintothesystem.
to the overall recommendation problem and provides the In this section, we first review the news recommendation
necessary basis for further discussion on these topics in the problem and the techniques that were employed for this
subsequentsections. specific task and then we shift our attention to generative
Definition1: Given set of users U and items I, the U x I adversarialapproachesforrecommendationsthatarepresent
| interactionmatrixℜrepresentsthehistoricalchoicesofusers |     |     |     |     | inliterature. |     |     |     |     |
| ------------------------------------------------------- | --- | --- | --- | --- | ------------- | --- | --- | --- | --- |
anditemsr(u∈U,i∈I).Acoldstartuserproblemoccurwhen
|                                      |     |                    |     |     | A. NEWSRECOMMENDATION |     |     |     |     |
| ------------------------------------ | --- | ------------------ | --- | --- | --------------------- | --- | --- | --- | --- |
| r(u new ,i)isundefinedforanoveluseru |     | new andallvaluesof |     |     |                       |     |     |     |     |
Theearliestnewsrecommendationswerefocusedonsimilar-
itemsiinI.Whereas,acoldstartitemproblemoccurswhen
r(u,i )isundefinedforanovelitemi andallvaluesof ityandclassicalmachinelearningalgorithms.In[22],simi-
| new |     | new |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
laritybetweenusermodelandnewsarticlesareexploitedto
uinU.
generatepersonalizedrecommendations.Forfindingrelevant
| The cold | start problem | in recommender | systems | is  |     |     |     |     |     |
| -------- | ------------- | -------------- | ------- | --- | --- | --- | --- | --- | --- |
newsitems,[23]proposedtheideaofusingsemanticsofthe
| comparable | to zero-shot classification | problem | in computer |     |     |     |     |     |     |
| ---------- | --------------------------- | ------- | ----------- | --- | --- | --- | --- | --- | --- |
newsarticles.SF-IDFincombinationwithdifferentsemantic
vision.
Definition2: In zero-shot learning, the classification similarity measures were used to find relevant news items
wheretheonlysemanticcontexttheyincorporatedwasbased
| model generalizes | feature information | from | seen classes | to  |              |              |          |        |             |
| ----------------- | ------------------- | ---- | ------------ | --- | ------------ | ------------ | -------- | ------ | ----------- |
|                   |                     |      |              |     | on synonyms. | The approach | of using | SF-IDF | was further |
anunseenclassinordertopredictit.Mathematically,given
asetofinstancesXandsetoflabelsYwhereYcontainsboth extendedby[24]intheirworkwhichusedanupdatedSF-IDF
|     |     |     |     |     | measure | for finding semantic | similarity | while | taking into |
| --- | --- | --- | --- | --- | ------- | -------------------- | ---------- | ----- | ----------- |
seenandunseenclasses,andfeaturespaceZ,theobjectiveof
zero-shotlearningistolearnthemappingffrominputstate account the relationship between synonym sets. In a graph-
basedapproach,[25]discussedtheuseofknowledgegraphs
XtosemanticspaceZ:
byconnectingnamedentities,eventsandplacespresentinthe
:X →Z
|     | f   |     |     | (1) | newsarticles. |              |               |           |            |
| --- | --- | --- | --- | --- | ------------- | ------------ | ------------- | --------- | ---------- |
|     |     |     |     |     | The idea      | of employing | collaborative | filtering | along with |
AndalsolearnthemappinggfromsemanticspaceZtolabel
|     |     |     |     |     | content-based | approach | to make | news recommendation |     |
| --- | --- | --- | --- | --- | ------------- | -------- | ------- | ------------------- | --- |
spaceY:
|     |     |     |     |     | was also  | explored in research.  |                 | One such | example was     |
| --- | --- | --- | --- | --- | --------- | ---------------------- | --------------- | -------- | --------------- |
|     |     |     |     |     | NewsDude  | [26] which recommended |                 | news     | by sequentially |
|     | g:Z | →Y  |     | (2) |           |                        |                 |          |                 |
|     |     |     |     |     | employing | three modules.         | A content-based |          | recommender,    |
Since, in a recommendation problem, there are typically a followed by classical collaborative component and a Naïve
largenumberofusersanditemsinvolved.Theselectionofa Bayes classifier. In [27], a hybrid algorithm was presented
smallsubsetofrelevantitemsfortheuserfromalargespace that combined content-based recommender system with
ofavailableitemsisanalogoustopredictingclasslabelsinan collaborative filtering to recommend sports news articles.
extrememulti-labelclassificationproblem. The inability of collaborative version to handle cold start
Definition3: In extreme multi-label classification, the items was dissimulated by the content-based component.
objective is to predict a subset of most relevant labels from Inanothersuchwork[28]proposedthetechniqueforfusion
a high-dimensional label space containing a vast number of collaborative filtering and content-based modelling to
of potential labels, given an input instance. Mathematically, generatenewsrecommendations.Thecontent-basedmodule
χ
given an input space and a high-dimensional label space wasusedtoconstructuserprofilewhileusergroupssimilar
|L|. The objective in extreme multi-label classification is to to the active user were found in much the same way as in
trainamodel thatcanfindasetl containingrelevantlabels a collaborative approach. Then a fusion model with user’s
foranovelinstancex given l ⊆|L|. currentandpotentialinterestswasdevelopedtorecommend
Wenowintroduceserendipitywhichcangenerallybeseen news by finding similarity between the fusion model and
asthemeasureofdiversityinrecommendationsproducedby contentofthenewsarticles.
analgorithmandisanimportantcharacteristicforimproving In a different approach for finding personalized news
theoveralluserexperience. articles, [29], [30], [31] used deep neural networks as
Definition4: In the context of recommender systems, their recommendation model. In [29], a news encoder and
serendipityreferstotheabilityofanalgorithmtorecommend user encoder were trained such that the news encoder
unexpectedanddiverseitemstotheuserstoexpandtheirtaste used attention mechanism to find topic information from
intoneighboringinterestareas. news articles through classification. The user encoder was
| 16612 |     |     |     |     |     |     |     |     | VOLUME12,2024 |
| ----- | --- | --- | --- | --- | --- | --- | --- | --- | ------------- |

S.Z.U.Hassanetal.:GCZRec:GenerativeCollaborativeZero-ShotFrameworkforColdStartNewsRecommendation
constructed with the help of users click behavior on news for items across different users. Due to the click prediction
articles. The news encoder was constructed in much the objectiveoftheirwork,therecommendationtaskisreduced
samewayby[30].However,theyarguedthatcapturingboth tobinaryclassificationandcouldnotbeextendedtoallowfor
long-term and short-term interests of the users is necessary multi-labelformulationoftheproblem.
for recommending highly personalized news items. The In an earlier work on generative recommendations, [38]
long-termrepresentationswerecapturedbytheembeddings proposed autoencoders are generators for collaborative rec-
of user IDs while the short-term representation of the users ommendations in CAAE model and to extract latent factors
wasguidedbytheirbrowsedarticlesusingaGRUnetwork. fromuser-iteminteractions,however,theirframeworkdidnot
The idea of different users who click on the same article utilizetheseparatefeaturespaceofusersanditemstomake
with attention on different aspects was discussed by [31] in recommendationincasetherewasacoldstartuserorproduct.
theirpaper.Theyusedconvolutionalneuralnetwork(CNN)
tolearnnewsitemrepresentationfromitstitle.Theattention IV. GCZRECFRAMEWORK
mechanismwasusedatnews-levelandword-levelinthenews The architecture of our proposed GCZRec framework con-
modelsinceaparticularnewsmayhavedifferentimportance sistsofdualgeneratornetworks,implementedasconditional
orrelevancefordifferentusers. WassersteinGAN.Thegeneratorfornews-to-userinteraction
is trained on mapping a given news item to a distribution
B. GENERATIVEMETHODS representing users’ interest score for the item. Whereas the
Among the first to use GAN for recommendation problem companion generator for user-to-news interaction is trained
were IRGAN [32] and GraphGAN [33]. These methods to generate a distribution of interaction scores of all news
exploredthepotentialofGANforrecommendersystemsbut items for a given user. Another important component of the
suffered from the well-known ‘‘label confusion’’ problem; GCZRec model are two independent classifiers for news
thatisthemodellearningtolabelanitemwithpositiveand and users. These pre-trained classifiers are used to perform
negative labels at the same time resulting in performance zero shot prediction of a cold start news or user in order
degradation of the model. As an application of minimax toprovidethegeneratornetworkstheirconditionalinputfor
optimization inherently present in GANs, [32] proposed synthesizingtheinteractions.
item recommendation as a generalized information retrieval The proposed framework utilizes generative capabilities
task with an objective function of matching top-k relevant ofthetraditionalGANarchitecturetosynthesizeinteractions.
documentstotheuser. The individual classifiers are trained to use semantic space
Intheirpaper,[33]proposedamodelthatsetanobjective and classify both seen and unseen news item and user in
of generating the connectivity distribution for a given order to provide our generators a conditional input. This
vertex. In the recommendation application, the connectivity design of our model also opens the door for a novel way
distribution between a given vertex and all relevant items of performing zero-shot extreme multi-label classification
was discussed. It was discussed by [34] in their paper that efficiently. In the subsequent subsections, each component
treating missing user-item as negative rating can deteriorate of our model is discussed in detail. In Fig. 2, the overall
the recommendation performance since the negative ratings architectureofGCZRecisillustrated.
could just be due to the user unaware of the item. They
used GANs to generate pairwise recommendation for each A. NOTATIONALCONVENTIONS
user and item with positive-unlabeled sampling. The idea Intheremainderofthispaper,thegeneralnotationusedfora
of using conditional variant of GAN for recommendation news is N and for active user it is U. We also denote warm
was presented by [35] in their research. Their GAN was news, cold news, warm user and cold user by w , c , w ,
n n u
conditionedonfashionitemasaclass,givenwhichanother c respectively.Thefourpossiblecasestobeconsideredare
u
complementaryitemwasgeneratedasarecommendation. thusrepresentedasw w ,w c ,c w ,c c .Thesecasesare
n u n u n u n u
A GAN-based approach to handle the problem of data representedinthemodelwiththehelpofa2-bitvectorwhich
imbalance in recommender systems was proposed by [36]. serves as the item-user state gate g and can determine the
s
TheymadeuseofconditionalWassersteinGANtogenerate synthesizertobeusedforgeneratinginterestvector.Werefer
missingdataforminorityclasstoperformrecommendations. to the generator responsible for synthesizing interactions
Their work used PacGAN in the discriminator architecture for each user given a particular news item as gen and its
N
with an aim to alleviate the performance of missing data companion generator which is responsible for generating
and improve the performance of recommendation models. interactionsforeachnewsgivenauserasgen .Apartfrom
U
InanotherWassersteinGANbasedframework,[37]proposed thesegenerators,thezero-shotclassifiersfornovelnewsitem
GAZRecmodeltogeneratesyntheticfeaturerepresentations anduserwillbecallednewslabelpredictorP anduserlabel
N
for both cold start news and user. To find the probability predictorP .Theseclassifiersarejointlyreferredtoaszero-
U
of click behavior, their framework adopted a separate click shot predictors. For encoding the identifiers of warm start
predictor module given a single user and news item. The news item and warm start users and map them to a unique
model did not use the behavioral representations to train numericidentifier,theencodersemployedarereferredtoas
thegeneratorforlearningdistributionofinteractionsdirectly E andE respectively.
N U
VOLUME12,2024 16613

S.Z.U.Hassanetal.:GCZRec:GenerativeCollaborativeZero-ShotFrameworkforColdStartNewsRecommendation
FIGURE2. ArchitectureofproposedGCZRecframework.
B. NEWSINTERESTSCOREGENERATORGEN ThegeneralobjectivefunctionofcWGANisgivenas:
N
| The generator |     | gen N in | GCZRec | framework |     | is responsible |     |              |     |           |     |
| ------------- | --- | -------- | ------ | --------- | --- | -------------- | --- | ------------ | --- | --------- | --- |
|               |     |          |        |           |     |                | min | max V(D,G)=E |     | [D(x ,c)] |     |
for handling the st ates w w , c w and c c . These input G D c,x∼true true
|     |     |     | n u | n u | n   | u   |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
statesaredeterminedpriortoitbystategateg .Thisnetwork −E [D(G(z,c)),c] (3)
|             |             |     |       |          | s            |           |     |     | c,z |     |     |
| ----------- | ----------- | --- | ----- | -------- | ------------ | --------- | --- | --- | --- | --- | --- |
| synthesizes | interaction |     | score | for each | of the users | given the |     |     |     |     |     |
Inthecontextofnewsrecommendation,thegeneratorgen
| news item | label | y as | its conditional |     | input. | The relevancy |     |     |     |     | N   |
| --------- | ----- | ---- | --------------- | --- | ------ | ------------- | --- | --- | --- | --- | --- |
N
|              |      |      |       |          |               |      | aims to minimize | this combined    | objective | function,  | while   |
| ------------ | ---- | ---- | ----- | -------- | ------------- | ---- | ---------------- | ---------------- | --------- | ---------- | ------- |
| of an active | news | item | for a | user can | be determined | from |                  |                  |           |            |         |
|              |      |      |       |          |               |      | the critic       | aims to maximize | it. This  | leads to a | minimax |
thecorrespondingvaluegeneratedbythenetworkwherethis
gamewherethegeneratortriestoproducerealisticsynthetic
| value is | essentially | an  | interest | score. | The overall | output of |     |     |     |     |     |
| -------- | ----------- | --- | -------- | ------ | ----------- | --------- | --- | --- | --- | --- | --- |
samples,andthecritictriestoeffectivelydistinguishbetween
| gen is | a vector | of interest |     | scores predicted |     | to be given |                                |     |     |      |            |
| ------ | -------- | ----------- | --- | ---------------- | --- | ----------- | ------------------------------ | --- | --- | ---- | ---------- |
| N      |          |             |     |                  |     |             | realandsyntheticsamples.WhereE |     |     | [D(x | ,c)]repre- |
by each user in the system to the active news item. Each c,xtrue true
sentsexpectationoverrealdatawhereasE
c,z [D(G(z,c)),c]is
positioninthisvectorrepresentsauniqueuserandthevalue
theexpectationovervaluesgeneratedbysynthesis.Interms
| is a score | that  | shows preference |       | of that | particular | user for     |               |                 |          |            |         |
| ---------- | ----- | ---------------- | ----- | ------- | ---------- | ------------ | ------------- | --------------- | -------- | ---------- | ------- |
|            |       |                  |       |         |            |              | of generating | interest scores | of users | given news | item as |
| the active | item. | With the         | value | closer  | to +1      | meaning that |               |                 |          |            |         |
conditionalinput.
| the user                                             | would | like this | news | article | whereas | any score |                           |     |                         |     |     |
| ---------------------------------------------------- | ----- | --------- | ---- | ------- | ------- | --------- | ------------------------- | --- | ----------------------- | --- | --- |
|                                                      |       |           |      |         |         |           | Theobjectivefunctionofgen |     | canthereforebestatedas: |     |     |
| closerto-1implyingtheuser’sdislikefortheitem.Instate |       |           |      |         |         |           |                           |     | N                       |     |     |
w n w u , the gen N takes encoded news label as conditional minL =−E [D(G(z,y )),y ] (4)
|            |      |         |     |             |     |                 |     | genN yN,Z∼Pg(x) |     | N N |     |
| ---------- | ---- | ------- | --- | ----------- | --- | --------------- | --- | --------------- | --- | --- | --- |
| input from | news | encoder | E   | to generate |     | the interaction |     |                 |     |     |     |
N
scores as its output distribution. For both states c w and Formally,thisgeneratortakesrandomnoisezfromaguassian
|     |     |     |     |     |     | n u |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
c n c u the generator gen N uses label provided by P N for distributiong(x)aslatentinputandgivenanewsclasslabel
synthesizing interaction scores. Due to its stability and the y , it generates a vector of synthetic interest scores G(·)
N
inherent sparsity in the historical interactions present in for all users and aims to minimize the distance between
our data, we used a conditional gan that uses Wasserstein fake and ground truth interactions between user-news pairs.
loss called conditional Wasserstein GAN (cWGAN) with The critic evaluates how well the generated scores match
the critic network during training to implement the gen N real user interest scores given the corresponding news item
model. and produces D(·) which is the output when it evaluates
| 16614 |     |     |     |     |     |     |     |     |     | VOLUME12,2024 |     |
| ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------- | --- |

S.Z.U.Hassanetal.:GCZRec:GenerativeCollaborativeZero-ShotFrameworkforColdStartNewsRecommendation
FIGURE3. FlowdiagramofnewsrecommendationinGCZRecframework.
the sample G(·) generated by gen . As part of adversarial The model gen takes latent vector z from the gaussian
N U
training, the critic network aims to discern the synthetic distributionasinputalongwithuserclasslabely togenerate
U
interactiondistributionfromtherealonethatisproducedby thedistributionG(·)ofsyntheticinterestscoresforallnews
the generator. The activation used in the dense and output items with respect to the active user. The critic outputs its
layersofthisnetworkareLeakyReLUandtanhrespectively. evaluationD(·)ofthegeneratedinteractionscoresproduced
Thecriticnetworkuseslinearactivationsinsteadofsigmoid and gen tries to minimize the loss between real and fake
U
in the output layer and its output is the approximation of distributionofinteractionscores.
Wasserstein distance hence assigning lower values to fake
interactions. In the dense layers of this model, LeakyReLU D. WARMSTARTENCODERS
activationsareused.Duringtraining,theweightsofthecritic For warm start news, the class label y to be served to the
N
areclampedtoasmallrangeandthisnetworkisupdatedfive interestscoregeneratorgen isencodedbymappingtheraw
N
timescomparedtoasingleupdateofthegeneratorinorderto identifieroftheactivenewsitemtoauniquenumericid.This
improvethegenerationquality. encoded id is then used by E to collect the corresponding
N
labelofthenewsfromhistoricaldata.Inthesameway,warm
C. USERINTERESTSCOREGENERATORGEN U startuseridisencodedbyE U toauniquenumericidinorder
The input states determine the use of gen U for synthesizing toextracttheavailableclassy U ofthisactivewarmstartuser
interest scores for active news. These states are handled by inordertoprovideconditionalinputtogen U network.
g .Thegen takestheuserclasslabely oftheactiveuser
s U U
asitsconditionalinputandgeneratesfakeinterestscoresfor E. LATENTFEATUREREPRESENTATION
each news item in the system. The possible states managed In the GCZRec approach, we represent each news item N
by the gen are w w , w c and c c . The output of gen as a latent feature vector, denoted by δ. This representation
U n u n u n u U
is a vector of interest scores showing preferences given by isobtainedbyfeatureextractionprocessθ usingpre-trained
thisusertoeachoneofthenewsitems.Eachpositionofthis embedding to extract informative features from the textual
interaction vector representing a unique news and the value contentofthenewsitem.Thefeaturerepresentationyielded
at that index indicating a score in range -1 to +1 to show isδ=θ(N).
if that particular item can be interesting for the active user. Since the MIND and Addressa datasets do not contain
For state w w , the conditional variable for this model is any explicit user entity features, we transformed each user
n u
providedbytheuserencoderE asy .Forcasesw c and U into latent feature representation λ with the help of her
U U n u
c c thepredictedclasslabelyˆ fromthezero-shotpredictor historicalinteractionswiththenewscategories.Allthenews
n u U
P is used. Similar to gen the training of this network the user interacted with previously are treated as positive
U U
is done in an adversarial manner by employing a cWGAN samplesandusetoextractthehiddenfeatures.Thesefeatures
and a critic that uses Wasserstein loss. The activation in the are constructed as a process ρ which converts the list of
dense layers of both generator and critic are LeakyReLU categories and subcategories of each interacted news into
while the output layer of the critic uses linear activation one-hotencoding.Henceλ=ρ(U)becomestheuserprofile
and tanh activation is used for the output layer of the ofactiveuser.
synthesizer.
Theobjectivefunctionofgen canbestatedas: F. ZERO-SHOTCLASSIFIERS
U
Thecoldstartproblemforbothnewsitemsandusersistreated
minL genU =−E yU,Z∼Pg(x) [D(G(z,y U )),y U ] (5) aszero-shotclassificationtaskintheGCZRecapproach.For
VOLUME12,2024 16615

S.Z.U.Hassanetal.:GCZRec:GenerativeCollaborativeZero-ShotFrameworkforColdStartNewsRecommendation
TABLE1. StatisticsofadressaandMINDdatasets. B. DATASETPREPROCESSING
|     |     |     |     |     |     |     | From the | users’ | behavioral |     | data provided | including |     | their |
| --- | --- | --- | --- | --- | --- | --- | -------- | ------ | ---------- | --- | ------------- | --------- | --- | ----- |
impressionslogandnewsclickhistory,wefirstsampled70%
datafortrainingourmodelandleftthe30%forpost-training
evaluation.Foreachuser,thenewsitemforwhichtheyhave
|     |     |     |     |     |     |     | positive | interactions | were | found | by extracting |     | the news | id  |
| --- | --- | --- | --- | --- | --- | --- | -------- | ------------ | ---- | ----- | ------------- | --- | -------- | --- |
amongtheirnewsclickhistoryandalsofromtheimpressions
wheretheuserhada‘‘1’’asaclickbehaviorforaparticular
news.Weencodedallthepositiveinteractionsbetweenuser
andnewsasthevalue‘‘1’’duringtrainingdataconstruction.
| these zero-shot | predictions, |     | we  | employ | two classifiers | that |     |     |     |     |     |     |     |     |
| --------------- | ------------ | --- | --- | ------ | --------------- | ---- | --- | --- | --- | --- | --- | --- | --- | --- |
Thenegativeinteractionsbetweenusersandnewswerefound
| use the | latent feature | representation |     | to predict | a class | label |     |     |     |     |     |     |     |     |
| ------- | -------------- | -------------- | --- | ---------- | ------- | ----- | --- | --- | --- | --- | --- | --- | --- | --- |
whentheuserdidnotclickthenewsandhencehasa0forthat
| for item | and user. | As a | result, | this allows | the predictors | to  |            |      |       |                 |      |     |         |      |
| -------- | --------- | ---- | ------- | ----------- | -------------- | --- | ---------- | ---- | ----- | --------------- | ---- | --- | ------- | ---- |
|          |           |      |         |             |                |     | particular | news | id in | the impressions | log. | We  | encoded | this |
leveragehiddencollaborativesignalsbetweenitemsandalso
|     |     |     |     |     |     |     | negative | interaction | as  | ‘‘-1’’ | in the training | data. | For | all the |
| --- | --- | --- | --- | --- | --- | --- | -------- | ----------- | --- | ------ | --------------- | ----- | --- | ------- |
usersforpredictinglabelsintermsofsimilarityinthelatent
|     |     |     |     |     |     |     | news not | present | in either | a   | user’s historical | interactions |     | or  |
| --- | --- | --- | --- | --- | --- | --- | -------- | ------- | --------- | --- | ----------------- | ------------ | --- | --- |
featurespace.
impressionslog,itwasassumedthattheuserwasnevershow
thenewsitemanddidnotinteractwithit.Theseinteractions
1) NEWSLABELPREDICTORP
|     |     |     | N   |     |     |     | are encoded | as  | ‘‘0’’ | for training. | Moreover, |     | for indexing |     |
| --- | --- | --- | --- | --- | --- | --- | ----------- | --- | ----- | ------------- | --------- | --- | ------------ | --- |
δ,
Given the latent news feature representation we classify purpose, each news id and user id is mapped to a unique
| a novel | item into | one of | K predefined |     | categories, | denoted |     |     |     |     |     |     |     |     |
| ------- | --------- | ------ | ------------ | --- | ----------- | ------- | --- | --- | --- | --- | --- | --- | --- | --- |
numericnewsidandnumericuseridrespectively.Basedon
,...,
by y N1 , y N2 , y N3 y NK where K is the total number of their numeric indices, the final training set for gen was
N
newscategoriesinthedomain.Weimplementthenewslabel constructed by using the numeric id as index for a unique
predictorasa1Dconvolutionalneuralnetworkwithsoftmax
|     |     |     |     |     |     |     | instance | (row) | and each | numeric | user id | as a | feature | value |
| --- | --- | --- | --- | --- | --- | --- | -------- | ----- | -------- | ------- | ------- | ---- | ------- | ----- |
activation in the output layer for prediction. The classifier (column).Inasimilarmanner,thefinaltrainingdataforgen
U
| calculates | the probability |     | P(y | |δ) for the | given news | item |                 |     |          |         |      |       |       |         |
| ---------- | --------------- | --- | --- | ----------- | ---------- | ---- | --------------- | --- | -------- | ------- | ---- | ----- | ----- | ------- |
|            |                 |     | Ni  |             |            |      | was constructed |     | by using | numeric | user | id as | index | for the |
belongingtoclassy Ni asstatedinequation6. instance(row)andeachnumericnewsidasindexforfeature
value(column).
ewi ·δ
|     |     | P(y |δ)= |     |     |     | (6) |                   |     |     |     |     |     |     |     |
| --- | --- | -------- | --- | --- | --- | --- | ----------------- | --- | --- | --- | --- | --- | --- | --- |
|     |     | Ni       | Pk  | ·δ  |     |     |                   |     |     |     |     |     |     |     |
|     |     |          |     | ewj |     |     | C. IMPLEMENTATION |     |     |     |     |     |     |     |
j=1
|                           |     |     |     |                |     |     | For constructing |     | latent | feature | representations, |     | we  | used |
| ------------------------- | --- | --- | --- | -------------- | --- | --- | ---------------- | --- | ------ | ------- | ---------------- | --- | --- | ---- |
| Theassignednewscategoryyˆ |     |     |     | isexpressedas: |     |     |                  |     |        |         |                  |     |     |      |
N hierarchical clustering to assign contextual labels to each
|     |     |     |     |     |     |     | news item | based | on its | rich textual | features. | The | number | of  |
| --- | --- | --- | --- | --- | --- | --- | --------- | ----- | ------ | ------------ | --------- | --- | ------ | --- |
yˆ =argma x P(y |δ) (7) clusters selected based on silhouette score and discernment
|     |     | N   |     | Ni  |     |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
i
|     |     |     |     |     |     |     | was 32. | For        | user labels, | the    | hyperparameter |     | value     | for |
| --- | --- | --- | --- | --- | --- | --- | ------- | ---------- | ------------ | ------ | -------------- | --- | --------- | --- |
|     |     |     |     |     |     |     | number  | of classes | was          | set to | 18 classes.    | The | embedding |     |
2) USERLABELPREDICTORP
U
Thisclassifierisusedtopredictthelabelforauserbasedon size for news and user is set to 300 to allow for baseline
|             |                |     | λ.      |         |                  |     | comparison. | For     | news, | pre-trained | Word2Vec   |               | embedding |     |
| ----------- | -------------- | --- | ------- | ------- | ---------------- | --- | ----------- | ------- | ----- | ----------- | ---------- | ------------- | --------- | --- |
| its feature | representation |     | Similar | to news | label predictor, |     |             |         |       |             |            |               |           |     |
|             |                |     |         |         |                  |     | are used    | whereas | for   | users we    | used count | vectorization |           | to  |
thearchitectureofthismodelisa1Dconvolutionalnetwork
with softmax function for finding the probability P(y |λ) perform the behavior encoding. The same architecture for
U
|             |         |      |        |       | ,...,   | i   | gen and | gen | is used | with | a dropout | rate of | 0.5, learning |     |
| ----------- | ------- | ---- | ------ | ----- | ------- | --- | ------- | --- | ------- | ---- | --------- | ------- | ------------- | --- |
| of the user | falling | into | one of | the y | , y , y | y   | N       | U   |         |      |           |         |               |     |
U1 U2 U3 UM rateof0.0002,LeakyReLUasactivationinthedenselayers,
categories.Theposteriorprobabilityforfindingtheuserlabel
andlabelassignmentisshownasfollows: tanh as non-linearity for the generator output layer. Adam
|     |     |      |     |     |     |     | is used as                                       | optimizer |     | with hyperparameters |     | β1  | =0.9 | and |
| --- | --- | ---- | --- | --- | --- | --- | ------------------------------------------------ | --------- | --- | -------------------- | --- | --- | ---- | --- |
|     |     |      | ewi | ·λ  |     |     | β2=0.999.AspartofthecWGAN,thecriticistrainedwith |           |     |                      |     |     |      |     |
|     | P(y | |λ)= |     |     |     | (8) |                                                  |           |     |                      |     |     |      |     |
Ui Pk ·λ clippedweights.Boththezero-shotpredictorsaretrainedas
ewj
|     |     |     | j=1     |     |     |     | multi-classclassifierswithconv1dhiddenlayers,batchnorm  |     |     |     |     |     |     |     |
| --- | --- | --- | ------- | --- | --- | --- | ------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
|     |     | yˆ  | =argmax | P(y | |λ) | (9) |                                                         |     |     |     |     |     |     |     |
|     |     | U   |         | Ui  |     |     | regularization,dropoutrateof0.5,learningrateof0.0005and |     |     |     |     |     |     |     |
i
softmaxactivation.
V. EXPERIMENTS
| A. DATASETDETAILS |              |     |         |     |                    |     | D. BASELINEMODELS |        |                |      |              |     |             |     |
| ----------------- | ------------ | --- | ------- | --- | ------------------ | --- | ----------------- | ------ | -------------- | ---- | ------------ | --- | ----------- | --- |
|                   |              |     |         |     |                    |     | In terms          | of the | recommendation |      | objective,   |     | the GCZRec  |     |
| For the           | experiments, |     | we used | the | publicly available |     |                   |        |                |      |              |     |             |     |
|                   |              |     |         |     |                    |     | framework         | is     | compared       | with | the existing |     | recommender |     |
MIND[20]andAdressa[21]newsrecommendationdatasets.
The key statistics for both of these datasets are provided in modelstovalidatetheperformanceoftheproposedapproach.
Themodelsarelistedas:
Table1.Thedatasetscontainsclickbehaviorofusersfornews
items. The data include information like impressions, news • GAZRec-NPA [37]: A three-tower generative zero-
categories,subcategories,abstractandtextualcontent. shot framework to generate generalized behavior
| 16616 |     |     |     |     |     |     |     |     |     |     |     |     | VOLUME12,2024 |     |
| ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------- | --- |

S.Z.U.Hassanetal.:GCZRec:GenerativeCollaborativeZero-ShotFrameworkforColdStartNewsRecommendation
TABLE2. ComparativeresultsofGCZReconMINDandadressadatasetsinexclusivelycoldstartcase.
TABLE3. ComparativeresultsofGCZReconMINDandadressadatasetsinmixedcoldstartandwarmstartcase.
| representationsofusersanditemsforrecommendation |     |     |     |     |     |     | positionk: |     |     |     |     |     |     |
| ----------------------------------------------- | --- | --- | --- | --- | --- | --- | ---------- | --- | --- | --- | --- | --- | --- |
andthenusetheserepresentationforcoldstartandwarm
DCG@k
| startpredictionsusinganeuralclickpredictor. |     |     |     |     |     |     |     |     | nDCG@k | =   |     |     |     |
| ------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | ------ | --- | --- | --- | --- |
(11)
| GNUD[39]:Theuserandnewsinteractionsaretreated |     |     |     |     |     |     |     |     |     | IDCG@k |     |     |     |
| --------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------ | --- | --- | --- |
•
ashigh-ordergraphinordertoexploitlatentpreference Tomeasuretheperformanceofrecommendersystemusing
factorsoftheusertoperformrecommendation.
averageprecisiongiventop-krecommendationsovermultiple
• NAML[40]:Aneuralnewsrecommendationapproach valuesofkweuseMAPwhichisdefinedas:
| with | attentive | multi-view |     | learning | in which | user repre- |     |     |     |     |     |     |     |
| ---- | --------- | ---------- | --- | -------- | -------- | ----------- | --- | --- | --- | --- | --- | --- | --- |
PK
sentationislearnedusingtheirbrowsedhistoryandother AveragePrecision@k
|     |     |     |     |     |     |     |     | MAP= | k=1 |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ---- | --- | --- | --- | --- | --- |
(12)
| information |     | as well | as news | attributes | such | as title and |     |     |     |     | K   |     |     |
| ----------- | --- | ------- | ------- | ---------- | ---- | ------------ | --- | --- | --- | --- | --- | --- | --- |
categoryareusedforitemrepresentation.
F. TESTENVIRONMENT
|     |     |     |     |     |     |     | For model | training | and | performance | evaluation |     | we divided |
| --- | --- | --- | --- | --- | --- | --- | --------- | -------- | --- | ----------- | ---------- | --- | ---------- |
E. EVALUATIONMETRICS
|             |         |             |               |        |            |        | the test    | data into | two distinct | sets. | From           | the total | test data |
| ----------- | ------- | ----------- | ------------- | ------ | ---------- | ------ | ----------- | --------- | ------------ | ----- | -------------- | --------- | --------- |
| To evaluate | the     | performance |               | of the | proposed   | GCZRec |             |           |              |       |                |           |           |
|             |         |             |               |        |            |        | we selected | 50%       | cold start   | items | for evaluating |           | the model |
| framework   | against |             | the baseline, | four   | evaluation | mea-   |             |           |              |       |                |           |           |
inanexclusivelycoldstartsetting.Theremainingcoldstart
| sures are | used  | as performance |        | indicators. | These | metrics    |             |      |          |       |          |      |             |
| --------- | ----- | -------------- | ------ | ----------- | ----- | ---------- | ----------- | ---- | -------- | ----- | -------- | ---- | ----------- |
|           |       |                |        |             |       |            | items along | with | the warm | start | data was | used | to generate |
| are Area  | Under | Curve          | (AUC), | normalized  |       | Discounted |             |      |          |       |          |      |             |
recommendationsformixedcold-warmnewsitems.
| Cumulative | Gain | (nDCG@k) |     | and Mean | Average | Precision |     |     |     |     |     |     |     |
| ---------- | ---- | -------- | --- | -------- | ------- | --------- | --- | --- | --- | --- | --- | --- | --- |
Thethresholdvalueforrecommendationofagivenitemis
(MAP).
fixedto0.5andthevaluesusedforhyperparameterkare1,
| The AUC                           | can | be measured |     | in terms | of true | positive rate |                          |     |     |     |     |     |     |
| --------------------------------- | --- | ----------- | --- | -------- | ------- | ------------- | ------------------------ | --- | --- | --- | --- | --- | --- |
| (TPR)andfalsepositiverate(FPR)as: |     |             |     |          |         |               | 5and10.                  |     |     |     |     |     |     |
|                                   | n   |             |     |          |         |               | VI. RESULTSANDDISCUSSION |     |     |     |     |     |     |
X1
AUC ≈ (TPR +TPR )(FPR −FPR ) (10) In this section, the effectiveness of the proposed approach
|     |     |     | i   | i−1 | i   | i−1 |              |     |     |                    |     |                 |     |
| --- | --- | --- | --- | --- | --- | --- | ------------ | --- | --- | ------------------ | --- | --------------- | --- |
|     |     | 2   |     |     |     |     | is evaluated | and | the | results indicating |     | the performance |     |
i=1
|     |     |     |     |     |     |     | on benchmark |     | datasets | are reported. |     | These | results are |
| --- | --- | --- | --- | --- | --- | --- | ------------ | --- | -------- | ------------- | --- | ----- | ----------- |
The nDCG@k is a measure of ranking quality in the list summarizedinTable2forcoldstartcaseandinTable3for
of recommended items with IDCG as the ideal DCG and mixedcaseofbothcoldstartandwarmstartitems.
| VOLUME12,2024 |     |     |     |     |     |     |     |     |     |     |     |     | 16617 |
| ------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----- |

S.Z.U.Hassanetal.:GCZRec:GenerativeCollaborativeZero-ShotFrameworkforColdStartNewsRecommendation
Abreakdownofmodelperformanceintodifferentaspects TABLE4. Percentageofnovelnews.
| is needed | in         | order | to effectively | discuss     |     | the outcomes |     |     |     |     |     |
| --------- | ---------- | ----- | -------------- | ----------- | --- | ------------ | --- | --- | --- | --- | --- |
| of GCZRec | framework. |       | These          | performance |     | aspects      | are |     |     |     |     |
presentedinthefollowingsubsections.
A. CLASSIFICATIONPERFORMANCE
| The performance |            | of  | generator | networks       | in  | the GCZRec |     |     |     |     |     |
| --------------- | ---------- | --- | --------- | -------------- | --- | ---------- | --- | --- | --- | --- | --- |
| for scores      | generation |     | is done   | in the context |     | of number  | of  |     |     |     |     |
correctinterestscoregenerationforagivennewsitem.With
| the help | of threshold |          | value, | each individual |     | interest | score |     |     |     |     |
| -------- | ------------ | -------- | ------ | --------------- | --- | -------- | ----- | --- | --- | --- | --- |
| produced | in the       | interest | vector | can itself      | be  | treated  | as a  |     |     |     |     |
binaryclassprediction.Thecombinedperformanceofthese
| positive     | and negative |                 | scores      | generation | are represented |            | by     |                                                 |     |     |     |
| ------------ | ------------ | --------------- | ----------- | ---------- | --------------- | ---------- | ------ | ----------------------------------------------- | --- | --- | --- |
| the AUC      | values       | as presented    |             | in Table   | 2 and           | Table      | 3. The |                                                 |     |     |     |
| results show | significant  |                 | improvement | in         | cold            | start case | for    |                                                 |     |     |     |
|              |              |                 |             |            |                 |            |        | FIGURE4. Precision-recallcurveforcoldstartcase. |     |     |     |
| MIND but     | slightly     | under-performed |             | on         | Adressa         | against    | the    |                                                 |     |     |     |
baselineformixedcold-warmstartcase.Thismaybedueto
| the label | encoding | scheme | used | for the | Adressa | categories. |     |     |     |     |     |
| --------- | -------- | ------ | ---- | ------- | ------- | ----------- | --- | --- | --- | --- | --- |
Itcanbefurtherinvestigatedwhethercategorycondensation
inthedatasetaffectedthepredictionaccuracy.
B. PRECISION-RECALLTRADE-OFF
| The GCZRec   |            | model | offers | significant    | improvement |           | over   |     |     |     |     |
| ------------ | ---------- | ----- | ------ | -------------- | ----------- | --------- | ------ | --- | --- | --- | --- |
| the existing | approaches |       | and    | the positional |             | relevance | of     |     |     |     |     |
| recommended  |            | news  | items  | are taken into | account     |           | by the |     |     |     |     |
syntheticinteractiongenerators.ForbothMINDandAdressa
dataset,theMAPscoregivenbytheproposedmodelshows
|                |     |          |      |                |       |           |     | FIGURE5. Precision-recallcurveformixedcold-warmstartcase. |     |     |     |
| -------------- | --- | -------- | ---- | -------------- | ----- | --------- | --- | --------------------------------------------------------- | --- | --- | --- |
| an improvement |     | in both  | cold | start and      | mixed | warm-cold |     |                                                           |     |     |     |
| start cases.   | But | compared |      | to purely cold | start | items,    | the |                                                           |     |     |     |
improvements in mixed case recommendations were much findingthepercentageofnewhighinterestnewsitemfound
more significant. The precision-recall curve for k=1, 5 and over5,10,25and50generationsgiventhesameuserasinput
10forMINDandAdressadatasetsinbothcasesisillustrated to gen . A summary of this is presented in Table 4. It can
U
alsobearguedthatthediversityismeasurableforgenerations
inFig.4andFig.5.
|     |     |     |     |     |     |     |     | producedbythegen | N inthesamemanner. |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------------- | ------------------ | --- | --- |
C. RANKINGQUALITY Basedonthecomparativeresults,itcanbestatedthatthe
In terms of the ranking quality of news items in both cold proposed GCZRec framework provides more accurate and
startandwarmstartcases,theproposedGCZRecframework relevantrankedrecommendationofcoldstartandwarmstart
newsitemstousersalsoincorporatesdiversitybyleveraging
clearlyoutperformsbaselinemodelswiththehighestaverage
improvement of +0.1113 is observed when top-5 items are latent collaborative information present in feature space of
considered as shown by ndcg@k values for k=1, 5 and usersanditems.
| 10. The | overall | value | of relative | ranking | in  | the proposed |     |     |     |     |     |
| ------- | ------- | ----- | ----------- | ------- | --- | ------------ | --- | --- | --- | --- | --- |
approach can be attributed to the gen and gen learning VII. CONCLUSION
|     |     |     |     | N   |     | N   |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
theunderlyinginterestdistributionfromthedatatoproduce Inthispaper,wepresentedtheGCZRecframeworkforcold
synthetic interest scores. These scores in their raw form are start news recommendation. We formulated the problem of
used as is to provide the ranking of relevant items that are cold start recommendation as zero-shot classification task
recommended. and proposed that these recommendations can be diverse
|     |     |     |     |     |     |     |     | and have serendipity | if user and | item information | are |
| --- | --- | --- | --- | --- | --- | --- | --- | -------------------- | ----------- | ---------------- | --- |
D. SERENDIPITY implicitly used during training. Unlike existing models,
For the inherently challenging and subjective aspect of the GCZRec approach allows the interest scores to be
evaluating the proposed system in terms of expanding the generated directly for a given news or user in both warm
interestofusersintoneighbouringnewscategories,wemodel start and cold start cases. Two separate wCGAN networks
the results of GCZRec as a collaborative recommendation are trained on interaction between users and news items in
outcome. This is done in an implicit manner as the order to allow collaborative signals to be implicitly used
output generated by gen N and gen U use the interaction for producing synthetic interactions at testing time. For any
between similar user and news. We measure the diversity unseenuserornewsitem,themodelmakesuseofzero-shot
ofrecommendationsproducedusingGCZRecframeworkby predictors implemented as 1D-CNN classifiers. Results on
| 16618 |     |     |     |     |     |     |     |     |     | VOLUME12,2024 |     |
| ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------- | --- |

S.Z.U.Hassanetal.:GCZRec:GenerativeCollaborativeZero-ShotFrameworkforColdStartNewsRecommendation
twobenchmarkdatasetsindicatethatourproposedapproach [15] H. Ding, Y. Ma, A. Deoras, Y. Wang, and H. Wang, ‘‘Zero-shot
offers significant improvement in the accuracy and ranking recommendersystems,’’2021,arXiv:2105.08318.
[16] R.J.ZiaraniandR.Ravanmehr,‘‘Serendipityinrecommendersystems:
| of news | items for cold | start | recommendation |     | and also sets |     |     |     |     |     |     |     |
| ------- | -------------- | ----- | -------------- | --- | ------------- | --- | --- | --- | --- | --- | --- | --- |
Asystematicliteraturereview,’’J.Comput.Sci.Technol.,vol.36,no.2,
| a standard | for incorporating |     | serendipity | by  | implicitly using |     |     |     |     |     |     |     |
| ---------- | ----------------- | --- | ----------- | --- | ---------------- | --- | --- | --- | --- | --- | --- | --- |
pp.375–396,Apr.2021.
|               |             |      |              |     |             | [17] D. Kotkov, | J. Veijalainen, |     | and S. | Wang, ‘‘How | does | serendipity affect |
| ------------- | ----------- | ---- | ------------ | --- | ----------- | --------------- | --------------- | --- | ------ | ----------- | ---- | ------------------ |
| collaborative | information | with | a generative |     | recommender |                 |                 |     |        |             |      |                    |
diversityinrecommendersystems?Aserendipity-orientedgreedyalgo-
systeminzero-shotmanner.
rithm,’’Computing,vol.102,no.2,pp.393–411,Feb.2020.
|     |     |     |     |     |     | [18] S. Inoue | and M. | Tokumaru, | ‘‘Serendipity |     | recommender | system for |
| --- | --- | --- | --- | --- | --- | ------------- | ------ | --------- | ------------- | --- | ----------- | ---------- |
academicdisciplines,’’inProc.Joint11thInt.Conf.SoftComput.Intell.
A. LIMITATIONSANDFUTUREWORK
Syst.21stInt.Symp.Adv.Intell.Syst.(SCIS-ISIS),Dec.2020,pp.1–4.
| The current | limitation | of our | model | include | its inability |                 |     |          |              |     |            |                |
| ----------- | ---------- | ------ | ----- | ------- | ------------- | --------------- | --- | -------- | ------------ | --- | ---------- | -------------- |
|             |            |        |       |         |               | [19] T. Dorjmaa | and | T. Shin, | ‘‘Evaluating | the | quality of | recommendation |
to consider the correlation between news items and tem- systembyusingserendipitymeasure,’’vol.25,no.4,pp.89–103,2019.
[20] F.Wu,Y.Qiao,J.-H.Chen,C.Wu,T.Qi,J.Lian,D.Liu,X.Xie,J.Gao,and
| poral relation | between | news | clicks. | Both of | these aspects, |     |     |     |     |     |     |     |
| -------------- | ------- | ---- | ------- | ------- | -------------- | --- | --- | --- | --- | --- | --- | --- |
W.Wu,‘‘MIND:Alarge-scaledatasetfornewsrecommendation,’’inProc.
if incorporated, can be important in further improving the 58thAnnu.MeetingAssoc.Comput.Linguistics,2020,pp.3597–3606.
recommendationqualityoftheGCZRecmodel. [21] J.A.Gulla,L.Zhang,P.Liu,Ö.Özgöbek,andX.Su,‘‘Theadressadataset
Infuturework,wealsoaimtoimproveourframeworkto fornewsrecommendation,’’inProc.Int.Conf.WebIntell.,Aug.2017,
pp.1042–1048.
allowcross-domainrecommendationproblemstobehandled. [22] M.KompanandM.Bieliková,‘‘Content-basednewsrecommendation,’’in
Forthis,existingknowledgedistillationmodelscanbeused Proc.11thInt.Conf.e-commerceWebTechnol.(EC-Web)(LectureNotes
to allow learned knowledge from source domain to be in Business Information Processing). Berlin, Germany: Springer, 2010,
pp.61–72.
transferredtoamodelsettorecommenditemsthatarepresent [23] M.Capelle,F.Frasincar,M.Moerland,andF.Hogenboom,‘‘Semantics-
intargetdomain. basednewsrecommendation,’’inProc.2ndInt.Conf.WebIntell.,Mining
Semantics,Jun.2012,pp.1–9.
[24] M.Moerland,F.Hogenboom,M.Capelle,andF.Frasincar,‘‘Semantics-
REFERENCES basednewsrecommendationwithSF-IDF+,’’inProc.3rdInt.Conf.Web
Intell.,MiningSemantics,Jun.2013,pp.1–8.
[1] A.Bermes,‘‘Informationoverloadandfakenewssharing:Atransactional
stressperspectiveexploringthemitigatingroleofconsumers’resilience [25] K.JosephandH.Jiang,‘‘Contentbasednewsrecommendationviashortest
during COVID-19,’’ J. Retailing Consum. Services, vol. 61, Jul. 2021, entitydistanceoverknowledgegraphs,’’inProc.CompanionWorldWide
| Art.no.102555. |     |     |     |     |     | WebConf.,May2019,pp.690–699. |     |     |     |     |     |     |
| -------------- | --- | --- | --- | --- | --- | ---------------------------- | --- | --- | --- | --- | --- | --- |
[26] D.BillsusandM.J.Pazzani,‘‘Usermodelingforadaptivenewsaccess,’’
[2] S.Feng,J.Meng,andJ.Zhang,‘‘Newsrecommendationsystemsinthe
UserModel.User-AdaptedInteract.,vol.10,pp.147–180,Jun.2000.
eraofinformationoverload,’’J.WebEng.,vol.20,no.2,pp.459–470,
Mar.2021. [27] P.LenhartandD.Herzog,‘‘Combiningcontent-basedandcollaborative
[3] M.Zihayat,A.Ayanso,andX.Zhao,‘‘Autility-basednewsrecommenda- filtering for personalized sports news recommendations,’’ in Proc.
CBRecSys@RecSys,2016,pp.3–10.
tionsystem,’’Decis.SupportSyst.,vol.117,pp.14–27,Feb.2019.
[28] W.Yang,R.Tang,andL.Lu,‘‘Newsrecommendationmethodbyfusion
[4] D.Goldberg,D.Nichols,B.M.Oki,andD.Terry,‘‘Usingcollaborative
ofcontent-basedrecommendationandcollaborativefiltering,’’J.Comput.
filteringtoweaveaninformationtapestry,’’Commun.ACM,vol.35,no.12,
| pp.61–70,Dec.1992. |     |     |     |     |     | Appl.,vol.36,no.2,p.414,2016. |     |     |     |     |     |     |
| ------------------ | --- | --- | --- | --- | --- | ----------------------------- | --- | --- | --- | --- | --- | --- |
[29] C.Wu,F.Wu,M.An,Y.Huang,andX.Xie,‘‘Neuralnewsrecommenda-
[5] Y.Koren,S.Rendle,andR.Bell,‘‘Advancesincollaborativefiltering,’’
tionwithtopic-awarenewsrepresentation,’’inProc.57thAnnu.Meeting
inRecommenderSystemsHandbook.Boston,MA,USA:Springer,2021,
Assoc.Comput.Linguistics,2019,pp.1154–1159.
pp.91–142.
|     |     |     |     |     |     | [30] M. An, | F. Wu, C. | Wu, K. | Zhang, | Z. Liu, | and X. Xie, | ‘‘Neural news |
| --- | --- | --- | --- | --- | --- | ----------- | --------- | ------ | ------ | ------- | ----------- | ------------- |
[6] P.DeHandschutter,N.Gillis,andX.Siebert,‘‘Asurveyondeepmatrix
recommendationwithlong-andshort-termuserrepresentations,’’inProc.
factorizations,’’Comput.Sci.Rev.,vol.42,Nov.2021,Art.no.100423. 57thAnnu.MeetingAssoc.Comput.Linguistics,2019,pp.336–345.
[7] M.J.PazzaniandD.Billsus,‘‘Content-basedrecommendationsystems,’’
|        |               |         |                |     |                      | [31] C. Wu, | F. Wu, | M. An, | J. Huang, | Y. Huang, | and | X. Xie, ‘‘NPA: |
| ------ | ------------- | ------- | -------------- | --- | -------------------- | ----------- | ------ | ------ | --------- | --------- | --- | -------------- |
| in The | Adaptive Web: | Methods | and Strategies | of  | Web Personalization. |             |        |        |           |           |     |                |
Neuralnewsrecommendationwithpersonalizedattention,’’inProc.25th
Berlin,Germany:Springer,2007,pp.325–341.
|     |     |     |     |     |     | ACM | SIGKDD Int. | Conf. | Knowl. | Discovery | Data Mining, | Jul. 2019, |
| --- | --- | --- | --- | --- | --- | --- | ----------- | ----- | ------ | --------- | ------------ | ---------- |
[8] C.N.Sunilkumar,‘‘Areviewofmovierecommendationsystem:Limita-
pp.2576–2584.
tions,surveyandchallenges,’’ELCVIAElectron.Lett.Comput.Vis.Image [32] J. Wang, L. Yu, W. Zhang, Y. Gong, Y. Xu, B. Wang, P. Zhang, and
Anal.,vol.19,no.3,pp.18–37,Sep.2020.
|                  |                 |           |            |        |                     | D. Zhang,      | ‘‘IRGAN:    | A   | minimax   | game      | for unifying | generative and |
| ---------------- | --------------- | --------- | ---------- | ------ | ------------------- | -------------- | ----------- | --- | --------- | --------- | ------------ | -------------- |
| [9] P. Lops,     | D. Jannach,     | C. Musto, | T. Bogers, | and    | M. Koolen, ‘‘Trends |                |             |     |           |           |              |                |
|                  |                 |           |            |        |                     | discriminative | information |     | retrieval | models,’’ | in Proc.     | 40th Int. ACM  |
| in content-based | recommendation: |           | Preface    | to the | special issue on    |                |             |     |           |           |              |                |
SIGIRConf.Res.Develop.Inf.Retr.,Aug.2017,pp.515–524.
recommendersystemsbasedonrichitemdescriptions,’’UserModel.User- [33] H. Wang, J. Wang, J. Wang, M. Zhao, W. Zhang, F. Zhang, X. Xie,
AdaptedInteract.,vol.29,no.2,pp.239–249,Apr.2019. andM.Guo,‘‘GraphGAN:Graphrepresentationlearningwithgenerative
| [10] M.H.Mohamed, | M.H.Khafagy,andM. |     |     | H.Ibrahim,‘‘Recommender |     |     |     |     |     |     |     |     |
| ----------------- | ----------------- | --- | --- | ----------------------- | --- | --- | --- | --- | --- | --- | --- | --- |
adversarialnets,’’inProc.AAAIConf.Artif.Intell.,vol.32,2018,pp.1–8.
systemschallengesandsolutionssurvey,’’inProc.Int.Conf.Innov.Trends
[34] Y.Zhou,J.Xu,J.Wu,Z.T.Nasrabadi,E.Korpeoglu,K.Achan,andJ.He,
Comput.Eng.(ITCE),Feb.2019,pp.149–155.
‘‘GAN-basedrecommendationwithpositive-unlabeledsampling,’’2020,
[11] J.Li,M.Jing,K.Lu,L.Zhu,Y.Yang,andZ.Huang,‘‘Fromzero-shot arXiv:2012.06901.
learningtocold-startrecommendation,’’inProc.AAAIConf.Artif.Intell., [35] S. Kumar and M. D. Gupta, ‘‘c+GAN: Complementary fashion item
vol.33,2019,pp.4189–4196.
recommendation,’’2019,arXiv:1906.05596.
| [12] W. Wang, | V. W. Zheng, | H. Yu, | and C. Miao, | ‘‘A | survey of zero-shot |                 |           |       |     |                  |          |          |
| ------------- | ------------ | ------ | ------------ | --- | ------------------- | --------------- | --------- | ----- | --- | ---------------- | -------- | -------- |
|               |              |        |              |     |                     | [36] W. Shafqat | and Y.-C. | Byun, | ‘‘A | hybrid GAN-based | approach | to solve |
learning:Settings,methods,andapplications,’’ACMTrans.Intell.Syst. imbalanced data problem in recommendation systems,’’ IEEE Access,
Technol.,vol.10,no.2,pp.1–37,Mar.2019. vol.10,pp.11036–11047,2022.
[13] S.YinandX.Luo,‘‘Asurveyoflearning-basedmethodsforcold-start, [37] M.A.AlshehriandX.Zhang,‘‘Generativeadversarialzero-shotlearning
socialrecommendation,anddatasparsityine-commercerecommendation forcold-startnewsrecommendation,’’inProc.31stACMInt.Conf.Inf.
systems,’’ in Proc. 16th Int. Conf. Intell. Syst. Knowl. Eng. (ISKE), Knowl.Manage.,Oct.2022,pp.26–36.
Nov.2021,pp.276–283. [38] D.-K. Chae, J. A. Shin, and S.-W. Kim, ‘‘Collaborative adversarial
[14] T. Wu, E. K.-I. Chio, H.-T. Cheng, Y. Du, S. Rendle, D. Kuzmin, autoencoders:AneffectivecollaborativefilteringmodelundertheGAN
R. Agarwal, L. Zhang, J. Anderson, S. Singh, T. Chandra, E. H. Chi, framework,’’IEEEAccess,vol.7,pp.37650–37663,2019.
W.Li,A.Kumar,X.Ma,A.Soares,N.Jindal,andP.Cao,‘‘Zero-shot [39] L.Hu,S.Xu,C.Li,C.Yang,C.Shi,N.Duan,X.Xie,andM.Zhou,
heterogeneoustransferlearningfromrecommendersystemstocold-start ‘‘Graphneuralnewsrecommendationwithunsupervisedpreferencedis-
search retrieval,’’ in Proc. 29th ACM Int. Conf. Inf. Knowl. Manage., entanglement,’’inProc.58thAnnu.MeetingAssoc.Comput.Linguistics,
| Oct.2020,pp.2821–2828. |     |     |     |     |     | 2020,pp.4255–4264. |     |     |     |     |     |       |
| ---------------------- | --- | --- | --- | --- | --- | ------------------ | --- | --- | --- | --- | --- | ----- |
| VOLUME12,2024          |     |     |     |     |     |                    |     |     |     |     |     | 16619 |

S.Z.U.Hassanetal.:GCZRec:GenerativeCollaborativeZero-ShotFrameworkforColdStartNewsRecommendation
[40] C. Wu, F. Wu, M. An, J. Huang, Y. Huang, and X. Xie, ‘‘Neu- MUHAMMAD RAFI was born in Karachi,
ral news recommendation with attentive multi-view learning,’’ 2019, Pakistan.HereceivedtheB.S.andM.S.degrees
arXiv:1907.05576. in computer science from the FAST-Institute
of Computer Science, University of Karachi,
Pakistan,in1996and2000,respectively,andthe
Ph.D.degreeincomputersciencein2017.Hehas
more than ten years of experience in software
development and also a Consultant for the local
software industry. His current research interests
includealgorithmdevelopment,machinelearning,
information retrieval, text/data mining, time series analysis, and natural
language processing. He has received several travel grant awards for
presenting his work at the top conferences. He has served as a Judge
andaTechnicalQualityReviewTeamatmanyversionsforIEEEXtreme
Programming Competitions. He has served as a reviewer for various
internationaljournalsofhighimpact.
JAROSLAV FRNDA (Senior Member, IEEE)
was born in Slovakia, in 1989. He received the
M.Sc.andPh.D.degreesfromtheDepartmentof
SYED ZAIN UL HASSAN wasborninKarachi, Telecommunications,VSB—TechnicalUniversity
Pakistan. He received the M.C.S. degree from of Ostrava, Czech Republic, in 2013 and 2018,
theUniversityofKarachi,in2014,andtheM.S. respectively.HeiscurrentlyanAssistantProfessor
degree in computer science from the National with the University of Z˘ilina, Slovakia. He has
UniversityofComputerandEmergingSciences, authored or coauthored more than 85 journal
in2018,whereheiscurrentlypursuingthePh.D. articlesinWebofScience.Hisresearchinterests
degree in computer science. He has more than include the quality of multimedia services in IP
eight years of teaching experience and was a networks,dataanalysis,andmachinelearningalgorithms.In2022,hewas
Developeratasoftwareserviceproviderforalmost theFinalistoftheCategoryOutstandingScientistinSlovakiaundertheage
twoyears.Hisresearchinterestsincludemachine of35-ESETScienceAward,in2022.
learning,generativeAI,recommendationsystems,andlargelanguagemodel.
16620 VOLUME12,2024