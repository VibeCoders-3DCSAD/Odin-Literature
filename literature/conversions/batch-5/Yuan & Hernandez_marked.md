---
conversion_metadata:
  converted_at: "2026-07-21T09:30:51Z"
  converter_tool: "markitdown"
  converter_version: "0.1.6"
  source_pdf: "Yuan & Hernandez.pdf"
  source_pdf_sha256: "c854c50536a315a02c211cbaa7a43c8c06390ac7f18dd785c4516c54754c15ac"
  page_count: 20
  markdown_char_count: 167108
---

<!-- PAGE-AWARE EXTRACTION (via pdfminer.six) -->

<!-- PAGE 1 -->

Received 12 October 2023, accepted 27 November 2023, date of publication 1 December 2023,
date of current version 11 December 2023.

Digital Object Identifier 10.1109/ACCESS.2023.3338705

User Cold Start Problem in Recommendation
Systems: A Systematic Review

HONGLI YUAN 1,2 AND ALEXANDER A. HERNANDEZ 1, (Member, IEEE)
1College of Computing and Information Technologies, National University, Manila 1008, Philippines
2Big Data and Artificial Intelligence College, Anhui Xinhua University, Hefei 230088, China

Corresponding author: Hongli Yuan (yuanhongli@axhu.edu.cn)

This work was supported in part by the Natural Science Foundation of the Anhui Provincial Education Office under Grant 2022AH051868
and Grant KJ2021A1156; in part by the Natural Science Foundation of the Anhui Xinhua University under Grant 2020zr002 and Grant
kytd202203; and in part by the Quality Engineering Project 2022xxkc053, Project 2022jyxm651, and Project 2022kcszx04.

ABSTRACT The recommendation system makes recommendations based on the preferences of the users.
These user preferences usually come from the user’s basic information, item rating, historical data, and so
on. The ‘‘user cold start problem’’ happens when a new user cannot be appropriately suggested due to a
lack of more detailed preference information. In many instances, the user cold start problem hinders the
use of the recommendation system. Many researchers are currently trying to discover a solution to the user
cold start problem. Unfortunately, there are two drawbacks in the current systematic reviews of how to deal
with the user cold start problem. First, systematic reviews on how to deal with the user cold start problem
are scarce or outdated. Second, existing reviews lack the distinction between the user cold start problem
and the item cold start problem. Nevertheless, the solutions to the two problems differ. To address these
problems, our study thorough review of all literature published by researchers from January 2016 to April
2023 about 8 years. Firstly, this study analyzes the literatures on approaches that addressed the user cold
start problem during the past eight years and divides them into two categories: data-driven technology and
approach-driven technology, and then describes and classifies each type of technology in detail. Secondly,
this study also analyzes the main evaluation criteria currently used in these methods to provide a reference
for researchers in related fields. Finally, this paper also points out the future research direction of this field.

INDEX TERMS Recommendation systems, user cold start, systematic review.

I. INTRODUCTION
With the continuous development of the Internet, mobile
Internet, big data, and other technologies, people’s lives are
being saturated by an increasing amount of information.
Thus, users face the problem of information overload. How
to enable users to efficiently and quickly find the requested
items from a large amount of information has become the
current research hotspots and difficulties.

The recommender system can provide items that may be
of interest to users based on their previous interaction data
in the system. It also uses user feedback to optimize the
system’s recommendation capabilities [1]. Compared with
categorized queries and search engines, the emergence of

The associate editor coordinating the review of this manuscript and

approving it for publication was Fabrizio Messina

.

a recommendation system can help users find information
that meets their needs quickly and accurately [2]. This
improves user satisfaction and user experience [3]. Today,
recommendation systems are widely used in e-commerce [4],
[5], social networks [6], [7], news [8], [9], video [10], [11],
music [3], [12], education [13], [14], [15], and other fields.
It provides more intelligent and personalized services for
users. Recommender systems play an important role in the
current society.

However, the cold start problem of recommender systems
is a common problem in recommender systems [16], [17],
[18], [19]. It is mainly divided into user cold start [20] and
item cold start [21], [22]. To make the cold-start problem
easier to understand, a simple example of recommendation
using user ratings is exemplified in Table 1. In Table 1 rows
represent users. The columns represent n items. The rating

136958

2023 The Authors. This work is licensed under a Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 License.
For more information, see https://creativecommons.org/licenses/by-nc-nd/4.0/

VOLUME 11, 2023

---

<!-- PAGE 2 -->

H. Yuan, A. A. Hernandez: User Cold Start Problem in Recommendation Systems: A Systematic Review

matrix represents the user ratings of the items in the range
{ 1, 2, 3, 4, 5 }, and the ratings can only be integers. The score
represents the user’s rating for the item, and if the user has
not rated the item, it is denoted by ‘‘−’’.

TABLE 1. The cold start example.

the process followed in this paper to write the systematic
literature review. Section IV describes the literature statistics.
Section V presents the results of this thesis and the analysis of
the results. Section VI presents a discussion of the user cold
start issue in recommender systems and the main research
directions. Finally, Section VII is the conclusion.

A. ITEM COLD START
For new items, the lack of historical data makes it difficult to
understand the characteristics of items and user preferences,
which leads to inaccurate recommendation results. As in
Table 1, Item n is new and has no user ratings. Therefore, it is
not possible to recommend this item based on user ratings.

B. USER COLD START
For new users, it is difficult to accurately predict users’
interests and behaviors due to the lack of historical data,
which leads to inaccurate recommendation results or even
useless recommendation results. As show in Table 1, the new
user Cary has not used the items in the recommender system
and has not evaluated the items after using them. If the user’s
evaluation information is used to recommend items to the
user, it is difficult to accurately recommend the desired items
to Gary.

This affects the performance and accuracy of the recom-
mendation system and is more obvious when the number of
new users and new items is large. There are currently many
different approaches to solving cold starts to improve the
accuracy and performance of recommender systems [23]. The
methods used to solve different cold starts are different, and
this paper focuses on user cold start issues.This paper refers to
the user cold start issue as the new user issue in later the paper.
The mitigation of the user cold start problem is essential
for the large-scale utility of recommender systems. It can
no longer solely point out the accuracy of recommendation,
however additionally enhances the user experience. How to
resolve the user cold start issues? This problem has been a
hot spot in the research of a variety of recommender systems
in recent years.

Several systematic literature reviews exist for cold start
problems in recommender systems [24], [25], [26]. However,
in general, it is known that different approaches are used
to solve different cold start problems. Currently, there are
few systematic reviews of the literature that address the new
user problems. Son [27] provides a detailed discussion of the
new user problem in three categories. However, this research
was published earlier and does not cover the recent years of
research on solving user cold start problems.

The following sections of the paper are organized as
follows. Section II presents previous work related to the
issues. Section III specifically describes
user cold start

II. RELATED WORK
The research on cold start questions for new users is
summarized in the paragraphs that follow.

Panda and Ray [26] conducted a study and review of
91 articles on cold-start mitigation. The study was the first
to categorize the various approaches into data-driven and
method-driven strategies. It also categorized method-driven
strategies into five main approaches based on the methods
used by the researchers. The study also analyzed the bench-
mark algorithms used for comparison and the evaluation
metrics used to assess the cold start problem. However, the
study did not separate user cold starts from project cold starts.
In solving the cold start problem, these two problems are
solved differently.

Camacho and Alves-Souza [25] investigated the research
on the application of data from social networks between
2011 and 2017 to alleviate the cold start issue. In recommen-
dations without purchase history or preference selection, the
analysis discovered. Information from social networks can
be effectively utilized to make up for users’ data shortages.
delivering more persuasive suggestions. However, this paper
only study on using social networks to address the issues
facing new users. However, other good solutions like the
application of deep learning, machine learning, etc. are no
longer being taken into consideration.

Son [27] also a comprehensive study of the issue of cold
starts for new users. The researchers provide a comparative
analysis of three approaches for the new user cold-start
problem, including (i) using other sources of information,
(ii) choosing the most significant similar user categories, and
(iii) improving predictions with a hybrid technique. Several
including MIPFGWC-CS, NHSM,
important algorithms,
FARAMS, and HU-FCF, are also compared and examined in
the study. However, this systematic review was finished in
2014, and there are a lot of new techniques that this paper
hasn’t considered lately.

Abdullah et al. [28] provides a detailed classification and
introduction of methods to address the new user problem
through assisted information. It also includes a thorough
explanation of how to acquire and extract auxiliary data.
This systematic review focuses on data-driven strategies for
solving the new user cold start issue. Less consideration is
given to the method-driven strategy.

In conclusion, there are several issues with the existing
study of the literature on how to solve the user cold
start problem. (i) The user cold start problem is addressed
in outdated evaluations of the literature. The most recent
relevant literature is not taken into consideration. (ii) The
analysis for resolving the user cold-start problem solely

VOLUME 11, 2023

136959

---

<!-- PAGE 3 -->

H. Yuan, A. A. Hernandez: User Cold Start Problem in Recommendation Systems: A Systematic Review

concentrates on one specific kind of approach. They do
not take into account other method categories like machine
learning, deep learning, etc (iii) The review is based on all
cold-start problems, with no differentiation made between
user and project-specific problems. The resolutions to these
two problems, however, differ from one another.

The user cold start issue has a significant impact on how
recommender systems are used. Unlike other reviews of the
cold start problem, this review only looks at the user cold start
problem literature from the last eight years. The approaches
employed are categorized and thoroughly examined in this
study to be as comprehensive as possible. The study also
offers an in-depth review of the evaluation criteria and open
problems currently applied to these methods.

III. SYSTEMATIC LITERATURE REVIEW METHODOLOGY
A thorough evaluation of the literature is crucial for raising
the standard of knowledge-based research. To conduct a more
impartial literature review, a systematic literature review
entails choosing, analyzing, and synthesizing important
scientific papers. The systematic literature review’s strategy
is presented in this section. The methodology is primarily
based on the guidelines used by [29] and [30].

A. RESEARCH QUESTIONS
As noted above, with the growing research on user cold
start recommender systems. However, there are few overview
researches in this area. All existing studies are based only on
classical surveys and reviews of the current state of research.
Therefore, a systematic literature review is needed. This is
regarded as the best method to offer a thorough and objective
analysis of the published findings. Several of the research
questions (Qs) are asked by this literature review, as defined
in Table 2.

TABLE 2. Research issues for organized literature review.

To begin the systematic literature review study. It
is
first defined that the questions shown in Table 2 originate
from the following keywords: (1) recommendation system or
recommender system, (2) user cold start or cold start user, and
(3) cold start. Examples of such strings are given in Table 3.

B. SYSTEMATIC LITERATURE REVIEW FLOW
The process of completing this systematic literature review
includes seven steps, as shown in Fig. 1.

• Step1: Definition researching questions and keywords.
The study question (see Table 2) and the search keywords
for this paper are finally both identified.

TABLE 3. Search strings for systematic reviews of the literature.

• Step 2: Choose search keywords and browse the
literature database in step two. In this stage, the search
string is specified by the format of the selected search
database (as shown in Table 3). The databases used
for this study include IEEE, ACM, and Web of Science.
These three datasets pretty much cover everything a
cold-start recommender system user could need to know.
• Step 3: Define both exclusion and inclusion standards.
A series of criteria were used to choose which articles
to read in-depth. These specifications are shown in the
Table 4.

• Step 4: Search for papers. In this phase, we search
for articles utilizing the search keywords that were
developed using the research’s study questions and
keywords (Table 3).

• Step 5: Article pre-selection. The abstracts and titles of
all the publications that were retrieved in the previous
phase are the only things that are read in this step. These
publications were either selected for a careful reading
or excluded based on the standards for inclusion and
exclusion.

• Step 6: Thoroughly read the selected paper. This stage
aims to consolidate and analyze the literature. Literature
that met the criteria was screened by reviewing and
searching relevant literature using quality evaluation
criteria (shown in Table 5). Each piece of literature
was examined and thoroughly evaluated to verify that
it answered the formulated questions posed.

TABLE 4. Criteria for systematic literature review inclusion and exclusion.

• Step 7: Classification. These papers are then assessed.
Additionally, they are rated as being entirely irrelevant,
hardly relevant, or extremely relevant
to the study
issue.

136960

VOLUME 11, 2023

---

<!-- PAGE 4 -->

H. Yuan, A. A. Hernandez: User Cold Start Problem in Recommendation Systems: A Systematic Review

FIGURE 1. The systematic literature review flow diagram.

VOLUME 11, 2023

136961

---

<!-- PAGE 5 -->

H. Yuan, A. A. Hernandez: User Cold Start Problem in Recommendation Systems: A Systematic Review

TABLE 5. Quality assessment and selection.

C. PAPER SEARCH
After identifying the literature database. Searched online
databases based on search strings. 1480 relevant literatures
were searched. The number of literature returned varied as
each literature database used a different strategy in its search
engine.

The most relevant literature was selected. Firstly, by read-
ing the title, abstract, and conclusion irrelevant stud-
ies were removed.
In the end, 117 documents were
obtained. Then, 117 documents were screened by applying
inclusion/exclusion criteria. Ultimately, 74 literatures were
retained. As shown in Fig. 2.

IV. DESCRIPTIVE STATISTICS OF THE LITERATURE
Table 6 shows the results of paper retrieval and selection for
systematic literature review. The total quantity of publications
discovered in every database can be seen in this table.

TABLE 6. The quantity of articles found in Fig.1’s phases 4 through 7.

Fig. 3 shows the distribution of completed reading and
evaluation of 45 selected papers in each publication year
(2016-2023), respectively at step 6 and step 7 (in Fig. 1). The
quantity of relevant literature reached the maximum in 2020,
with 11 papers, and there may be an even sharper rise from
2023. This shows that there is an increase in interest in finding
solutions to the cold start issues related to recommendations.
Because the year has barely begun, the results of 2023 cannot
be considered final.

In this study, 45 research papers from 35 various meetings
and journals with peer review were selected (see Table 7).
These publications mostly focus on the field of computer
science, systems for information and related topics. The two
with the highest counts, both with a value of 4, are ‘‘IEEE
Access’’ and ‘‘ACM Transactions on Information Systems’’.
‘‘ACM SIGKDD International Conference on Knowledge
Discovery and Data Mining’’ and ‘‘43rd International ACM

SIGIR Conference on Research and Development in Infor-
mation Retrieval’’ are the next, with 3 total.

V. QUALITATIVE SYNTHESIS OF THE LITERATURE
A. WHAT RESEARCH TOPICS ARE BEING ADDRESSED
USER COLD START IN RECOMMENDATION SYSTEM?
This paper provides an in-depth study of 45 selected papers.
An overview of approaches to address the new user issue
is presented. In this research, we primarily categorize these
techniques into two primary groups: data-driven techniques
and method-driven techniques. As shown in Table 8.

• Data-driven techniques
These articles offer ideas for approaches inspired by
efficient data utilization and the connection between user and
project attributes. The new ways to resolve the issues of cold
start are proposed by using person region data, person social
community data, person belief information, and individual
cross-domain data.

• Approach-driven techniques
This category of approaches mitigates the cold start
problem by proposing new algorithms or improving old
ones. The study further classified them into five categories.
Deep learning-based approach, Matrix factorization-based
approach, hybrid approach, the improvement over collabora-
tive filtering-based approach, the improvement over content-
based approach.

1) DATA-DRIVEN TECHNIQUES

• Cross-domain data
Table 9 presents a line-by-line comparison of the main
ideas, Datasets, evaluation indicators, strengths, and weak-
nesses of the selected literatures.

Utilizing user preferences from several domains enables
the creation of more thorough user models and improved sug-
gestions. For instance, using cross-domain recommendations
to address the target domain’s cold start issue. Cross-domain
recommendation mechanisms make or enhance recommen-
dations for the target domain using information garnered
from the source domain [43], [44]. Numerous scenarios and
tasks can be employed for cross-domain recommendation.
Cross-domain recommendation systems are therefore more
organized and complex than one-domain recommendations.
Cremonesi et al. [43] first proposed the classification
of scenarios for cross-domain recommendation, and later
studies largely agreed with this categorization. As illustrated
they identified four distinct recommendation
in Fig. 4,
scenarios: no overlap, user overlap,
item overlap, and
complete overlap. The most common methods for solving
problems involve user and item overlap and user overlap.

Many methods for task classification in cross-domain
recommender systems. It can be combined according to
the cross-domain information. It is divided into two types:
Aggregating knowledge and Linking/transferring knowledge.
The Aggregate Knowledge task first aggregates knowledge
from different source domains into the target domain. Then

136962

VOLUME 11, 2023

---

<!-- PAGE 6 -->

H. Yuan, A. A. Hernandez: User Cold Start Problem in Recommendation Systems: A Systematic Review

FIGURE 2. The paper selection process.

FIGURE 3. The number of papers per year.

recommendations are made. As shown in Fig. 5. For example,
fusing user preferences from different source domains not
only allows cross-system research but also solves the user
cold-start problem.

The establishment or transference of information among
domains in support of recommendations is referred to as link-
ing and transferring knowledge (shown in Fig. 6). Because
they both fall under categories that can be semantically
mapped, such as comedies and humor, we can correlate a
certain comedy movie with a humor book, for instance.

The literature is displayed in Table 10 according to
the categories of Gathering information and Transferring
information.

Jin et al. [45] proposed a cross-domain recommendation
algorithm, called RACRec. RACRec solves the problem
of predicting full new users in recommendation. RACRec
is a cross-domain recommendation algorithm that uses a
review selection strategy to dynamically choose appropriate
cross-domain methods for each user.

Wang et al. [46] employ auxiliary data from the advertising
sector to address the issue of user cold start
in online
shopping. The procedure examines the user’s web browsing
history on the advertising platform and generates recommen-
dations from it.

Zhao et al. [47] proposed a method called CATN, a recom-
mendation method to address user cold start problems. The

VOLUME 11, 2023

136963

---

<!-- PAGE 7 -->

H. Yuan, A. A. Hernandez: User Cold Start Problem in Recommendation Systems: A Systematic Review

TABLE 7. Distribution of selected papers for journals and conferences.

FIGURE 4. The scenarios where user set and item set data overlap.

FIGURE 5. Aggregating knowledge.

CATN extracts features from review documents. It enhances
the user representation by using auxiliary comments from
similar users.

A cross-domain recommendation model entirely based on
the partial least squares regression technique was proposed
by Li et al. [48]. The latent properties of users in the source
domain and users in the target domain can be accurately
correlated using these models by researching a matrix of
regression coefficients. Even target domain users’ cold start
issues can be solved by the model.

• Social network data

136964

In Table 11, a line-by-line comparison of the main ideas,
Datasets, evaluation indicators, strengths, and weaknesses of
the selected literatures is presented.

The unprecedented growth of various social networking
platforms has greatly enriched the daily lives of users.
Social networks are a source of information. In addition
to determining the impact of a user on other users. It also
provides valuable data to determine user preferences for
items. All of this knowledge can be very helpful in making
more accurate and objective product recommendations to
users, which will significantly help to solve the user cold start
issue. Utilizing information from social networks, there are

VOLUME 11, 2023

---

<!-- PAGE 8 -->

H. Yuan, A. A. Hernandez: User Cold Start Problem in Recommendation Systems: A Systematic Review

TABLE 8. Classification of approaches for alleviating the user cold start problem in recommender systems.

TABLE 9. Reviewing and comparing Cross-domain data approach.

VOLUME 11, 2023

136965

---

<!-- PAGE 9 -->

H. Yuan, A. A. Hernandez: User Cold Start Problem in Recommendation Systems: A Systematic Review

steps, which are computed independently for each group of
neighbors.

Li et al. [52] gathered user information for the new user
issue by examining their social network information. Learn-
ing from side data (such as consumer social interactions,
human traits, etc.). Once it is done, teach new users the
information. This method helps to mitigate the issue with cold
starts.

A latent feature representation and social network data
frequently show up as attribute mapping in attribute mapping
methods.

Predict whether cold-start users will become important
users on the growing online social network (Medium)
by using user data from the most popular online social
network (Twitter) [53]. To transfer descriptive information
and knowledge of dynamic actions to the most influential
online social networks, they used a supervised-based machine
learning approach.

A unique model of LoCo is put out by Sedhain et al. [31].
Through stochastic SVD, it directly and effectively learns a
low-rank linear model. In comparison to state-of-the-art user
cold start advice, the results validated in this study on four real
datasets demonstrate considerable improvements in LoCo.

FIGURE 6. The linking and transferring knowledge.

TABLE 10. Classification of literatures on cross domain.

two groups of strategies for reducing the user cold start issue.
The first group includes feature mapping models [53] and the
second, similarity-based models [50], [51], [52].

It’s easy to use the similarity-based model. Their equation

can be written as

Ys = WYt .

(1)

2) APPROACH-DRIVEN TECHNIQUES

where W is the similarity matrix. In general, W is the
similarity between the relation source domain Ys and the
target domain Yt .

A cold-start recommender system based on linked open
data and social network elements has been proposed for new
users [50]. This technique uses the user profile generator
module to automatically create a user’s profile when they
first log in using their Facebook ID and, if applicable, their
DBpedia ID. After that, ‘‘user clusters’’ are created using
the user’s profile information and class labels to train a
classifier. A classifier is then fed the data from the new user
to make a prediction about which category the new user
belongs to. The system will only review the user ratings given
to each ‘‘program’’ by members of the ‘‘group’’ to which
the new user belongs once that group has been identified.
Finally, the average weight of the ratings given by the users
in the predicted cluster to each Item cluster was calculated,
and the Item cluster with the highest rating was recommended
to the new user.

Reshma et al. [51] alleviate the cold start problem by using
user social behavior. The customer rating matrix is used in
the suggested method to determine the nearest neighbors
first. The properties of social network data are analyzed in
the subsequent stage to determine the attribute comparability
between every other user and those who are active. In the third
stage, a group of neighbors are selected from the network of
friends, and the social similarity is determined as a weighted
sum of these values. The final planned rating of the item is
then calculated by adding the weighted total of the forecasted
ratings for each set of neighbors obtained in the first two

• Meta-learning

In Table 12, a line-by-line comparison of the main ideas,
Datasets, evaluation indicators, strengths, and weaknesses of
the selected literatures is presented.

A current

trend in machine learning is called meta-
learning. It enables quick adaptation to new tasks using
a limited set of examples. One might consider of the
new user suggestion challenge as a learning problem from
a limited number of samples. Because of this, the user
cold start problem can be solved extremely well using the
meta-learning approach. Plenty of researchers are currently
employing meta-learning to solve the new user issue. [54]

Three categories of meta-learning exist: metrics-based,
model-based, and optimisation-based. [55] The following
Table. 13 categorizes the meta-learning techniques addressed
to the new user issue.

The goal of metrics-based meta-learning is to identify
patterns among samples within a task. Jiang et al. [56]
suggest using user clustering to group individuals with
similar interests based on their shared knowledge. The
transformation network is built using the user’s clustering
data, and it transforms the global initialization parameters
gained by meta-learning into the cluster’s ideal starting
parameters. It can lessen the detrimental impacts of users
with various tastes and enhance the meta-learning model’s
functioning.

Model-based meta-learning updates parameters quickly
through several training steps. Using memory enhanced meta
optimization (MAMO), Dong et al. [58] suggested a cold
beginning strategy. A feature-specific memory is meant to

136966

VOLUME 11, 2023

---

<!-- PAGE 10 -->

H. Yuan, A. A. Hernandez: User Cold Start Problem in Recommendation Systems: A Systematic Review

TABLE 11. Reviewing and comparing Social network data approach.

provide individual deviation items while configuring the
model’s parameters. Comprehensive tests on two regularly
used data sets show that MAMO outperforms cutting-edge
solutions.

Optimization-based meta-learning aims to adjust
the
optimization algorithm so that the model can learn well
from a small number of examples. The novel user sequence
recommender framework known as metaCSR based on
meta-learning was proposed by Huang et al. [55]. When
learning effective initialization for new users, the framework
employs Model-Agnostic Meta-Learning (MAML) to extract
and spread transferable information from previous users.
MetaCSR has demonstrated high performance in learning
typical patterns from regular users through experiments.
Shen et al. [61] proposed the RESUS to resolve the cold
user CTR prediction problem through meta-learning. The
method may quickly learn from a narrow range of user-
specific interactions, and the learning can be applied to
deduce individual preferences. The method is experimentally
confirmed to improve the predictability of click-through rates
for chilly users.

• Deep Learning

Table 14 presents a line-by-line comparison of
the
main ideas, Datasets, evaluation indicators, strengths, and
weaknesses of the selected literatures.

The deep learning algorithm is a particular kind of neural
network-based machine learning algorithm. It learns and
classifies input data using a multi-layer neural network. Deep
learning techniques including Autoencoder, Graph Neural
Networks, Generative Adversarial Networks, and others have
been used in recommendation algorithms.

Briand et al. [32] use deep neural network architecture and
user clustering from heterogeneous information sources to
solve the new user issue. A brand-new service recommen-
dation technique for multiplex interaction, known as MISR,
was proposed by Ma et al. [16]. This strategy functions by
incorporating three different kinds of service and mashup
interactions within DNN. A deep neural network-based
DeCS framework is suggested by Mondal et al. [33]. The
collaborative filtering recommendation’s new user issue
is solved using this technique. The suggested framework,
DeCS, may be applied to various data sets and aids in
system performance improvement. Kumar et al. [34] provide
a video recommendation system that overcomes the cold
start problem and makes use of intrinsic information to
suggest films. The deep neural network of the architecture
is fed with the output of the C3D model, mainly video-level
characteristics.

Chen et al. [35] proposes an end-to-end recommendation
system ColdGAN based on the Generative Adversarial
Network, which can generate accurate data under imprecise
data. ColdGAN is simple and effective in restoring lost
functions of related items and effectively solves the problem
of new users.

Hao et al. [36] proposed a multi-policy approach for new
user recommendation (MPT). The model uses user and item
dependencies obtained by a GNN encoder and introduces
a Transformer encoder to obtain long-term dependencies.
A brand-new inductive heterogeneous graph neural network
(IHGNN) model is put out by Cai et al. [37]. To address
the sparsity of user features issue, the model makes use
of relational information from the new user recommenda-
tion system. Hao et al. [38] presented a recommendation

VOLUME 11, 2023

136967

---

<!-- PAGE 11 -->

H. Yuan, A. A. Hernandez: User Cold Start Problem in Recommendation Systems: A Systematic Review

TABLE 12. Reviewing and comparing Meta-learning approach.

136968

VOLUME 11, 2023

---

<!-- PAGE 12 -->

H. Yuan, A. A. Hernandez: User Cold Start Problem in Recommendation Systems: A Systematic Review

TABLE 13. The meta-learning methods used to solve the user-cold start
problem.

method based on the GNN model. The model enhances
the aggregation capability of graph convolution based on a
self-focused meta-aggregator. The method can after better
mitigate the new user problem. A new framed attribute graph
neural network (AGNN) is developed using attribute graphs.
Qian et al. [39] AGNN can generate strictly cold user/item
preference embeddings by learning attribute distributions
with an extended variational self-encoder (eVAE) structure.

• Matrix Factorization

the
Table 15 presents a line-by-line comparison of
main ideas, Datasets, evaluation indicators, strengths, and
weaknesses of the selected literatures.

Zhou et al. [68] proposed a matrix decomposition rec-
ommender system method based only on homomorphic
encryption and social networks. The method introduces the
preference information of users similar to new users as
features in the recommender system. The new user problem
is solved with this method. Natarajan et al. A Matrix
Factorization Model (CD-SemMF) based on cross-domain
semantic association is presented to solve the new user
issue in collaborative filtering recommendations employing
Linked Open Data (LOD). Lin et al. [70] A MetaMatrix
Factorization (MetaMF) model is proposed that is capable
of generating private item embedding and rating prediction
models using meta-networks. Chen et al. [71] find that
combining regularization differentiating functions with a
matrix factorization-based approach can better predict users’
preferences for items to address the new user issue.

• Improved New Approach Based on Collaborative

Filtering

the
Table 16 presents a line-by-line comparison of
main ideas, Datasets, evaluation indicators, strengths, and
weaknesses of the selected literatures.

When used directly, collaborative filtering algorithms
cannot effectively address the user cold start issue. Many
researchers are working to develop a collaborative filtering
algorithm to address the user’s cold start issue Collaborative
filtering algorithms cannot effectively solve the new user
issue when used directly. Many researchers are working
to develop collaborative filtering algorithms to solve the
new user issue [72]. To deal with the limited data of
user characteristics, Z. Zhang et al. [73] propose a novel
inductive heterogeneous graph neural network (IHGNN)
architecture that utilizes the relational data from the new user
recommendation system.

A new CF framework called Augmented Reality CF
was proposed by Chae et al. [74]. It effectively addresses
the new issue and raises the overall effectiveness of the

recommendation. The fundamental goal is to create fictitious
yet believable people and things. The rating matrix is then
expanded using them as extra rows (users) and columns
(things).

Duricic et al. [75] explore the use of Katz similarity (KS)
in a collaborative filtering (CF) algorithm for cold start users.
This is the rule-equivalent similarity measure in the network
for selecting the k nearest neighbors.

Chao et al. [76] proposes an innovative way to solve
challenges faced by new users by using leader recommenda-
tions. The Collaborative Filtering technique chooses potential
leaders based on previous user ratings. These potential
leaders have multiple ratings and have excellent historical
data fit. As a result, they may be relied upon to suggest
products to new consumers.

Al-Bakri Hassan [77] proposed a collaborative filtering
model for user authenticity information based on fuzzy
c-mean clustering. The method makes use of a new measure
formula. The formula uses combination coefficients to
combine user evaluation with fuzzy authenticity information.
Zahid et al. [78] presented standardization techniques
combined with systematic filtering methods and Matrix
factorization methods to solve the new user issue in recom-
mendation, considering variables that are not directly related
to user profiles but are meaningful enough to ultimately
recommend to users.

• New Improved Content-based Approach

the
Table 17 presents a line-by-line comparison of
main ideas, Datasets, evaluation indicators, strengths, and
weaknesses of the selected literatures.

it can deal with different

Content-based recommendation algorithm is an algorithm
that recommends similar items according to users’ histor-
ical behavior and item attributes. The core idea of this
algorithm is to use the characteristics of the object itself
to recommend, rather than relying on the user’s behavior.
The benefit of a content-based recommendation algorithm
types and fields of
is that
items, and does not need the user’s personal information
and behavioral data. The drawback is that it is unable to
account for users’ shifting interests and preferences, so the
recommendation may be inaccurate in some cases. Content-
based recommendation algorithms suffer from user cold-start
problems, and currently, many scholars have improved
content-based recommendation algorithms to alleviate new
user problems.

A frequently occurring pattern mining framework (FPRS)
for recommender systems is presented by Kannout et al. [40].
To alleviate the cold-start issue for new users and new
item sets
items, FPRS combines the created frequent
with a content-based strategy. The method’s efficacy is
confirmed by empirical study. The term frequency-inverse
document frequency (TF-IDF) text mining technique was
used by Chia et al. [41] for data filtering and information
retrieval.

VOLUME 11, 2023

136969

---

<!-- PAGE 13 -->

H. Yuan, A. A. Hernandez: User Cold Start Problem in Recommendation Systems: A Systematic Review

TABLE 14. Reviewing and comparing Deep Learning approach.

To solve these issues, a system called Cold-Transformer is
proposed by Li et al. [42]. Context-based adaptive embedding
is created by Cold-Transformer to account for variations in
feature distribution. To convey the related user preferences,
it changes the embed of a new user into a hot state that is
more similar to an existing user.

B. WHAT METRICS ARE EMPLOYED TO ASSESS THE
EFFECTIVENESS OF USER COLD START?
An overly performant recommender system is the ultimate
goal of
recommender system design. How should the
effectiveness of a particular recommender system be assessed
to address the user cold-start issue? Three commonly utilized
metrics - ranking measures, classification accuracy metrics,
and rating prediction metrics - are categorized. Table 18
displays the distribution of the studied studies regarding the
prediction metrics.

Mean Square Error (MSE), Root Mean Square Error
(RMSE), and Mean Absolute Error (MAE) are the three
main rating prediction metrics. As the value of the measure
falls, the precision rises. Area under the curve (AUC) and
recall, precision, f1 score, and recall are often used evaluation
measures for the classification accuracy metric.

Ranking Metrics is the value obtained in the recommen-
dation for a given user U and a test set S, after calculating
the ranking of all possible recommendation results for S by
that user U. If a recommendation system has a higher Top-K
accuracy, it means that it can better predict and rank the items
of interest to the user. top-K accuracy is mainly ndcg@K,
Hit@K, etc.

Multiple types of evaluation metrics are used in most of
the literature to evaluate models. Rating prediction metrics
(MSE and RMSE) and Ranking Metrics (ndcg@K) were
used in the paper [56]. The literature [49] used AUC and
NDCG@K. Huang et al. [55] used AUC, MAP, Hit@K and
NDCG@N. MAE, NDCG@K and DCG@K were used in the
literature [58] and [62]. NDCG@k, Recall@k, Prision@k,
and AUC were used in the literature [37].

Some literature uses only one type of evaluation metric in
the performance evaluation process. As in the literature [42]
the AUC was used to evaluate the model.
and [53]
In the literature [59] used NDCG@N for evaluation model.
In the literature [76] used RMSE for evaluation. Most of this
literature uses Ranking Metrics for model evaluation [39],
[59], [69], [71]. As in the literature [36] and [38], only
Recall@K and NDCG@K were used.

136970

VOLUME 11, 2023

---

<!-- PAGE 14 -->

H. Yuan, A. A. Hernandez: User Cold Start Problem in Recommendation Systems: A Systematic Review

TABLE 15. Reviewing and comparing Matrix Factorization approach.

TABLE 16. Reviewing and comparing improved new approach based on collaborative filtering.

VI. DISCUSSION AND DIRECTIONS FOR FUTURE
RESEARCH
A. DISCUSSION
The cold start issue is one key issue that affects the accuracy
and precision of recommendations. With the cold start issues,
there are new user issues and new item issues. The problem

with new users is that when they start to show up throughout
the recommendation process, better recommendations cannot
be produced due to a lack of user-specific data.

This literature review divides the approaches to solving
user cold starts into two groups. Data-driven and method-
driven. Show as Fig. 7.

VOLUME 11, 2023

136971

---

<!-- PAGE 15 -->

H. Yuan, A. A. Hernandez: User Cold Start Problem in Recommendation Systems: A Systematic Review

TABLE 17. Reviewing and comparing new improved content-based approach.

TABLE 18. Distribution of studies related to evaluation metrics for user
cold start problems.

Data-driven mainly utilizes different user information to
solve the new user issue. Such as user social network data,
user demographic data, etc. The advantage of these methods
can better solve the problems that new users have no historical
behavior data by using user-related data (such as social
network data). It can better alleviate the user cold start
problem. However, these methods have some problems such
as the difficulty of multi-domain user feature fusion, user data
privacy and user data acquisition.

Method-driven solves the problem by applying different
algorithms or models. In this paper, method-driven is subdi-
vided into five categories. They are meta-learning methods,
deep learning methods, matrix factorization methods, new
methods based on collaborative filtering, and new methods
for content-based recommender systems. The advantage of
these methods is that some rules are used to solve the
user cold start problem. For example, machine learning
related methods can be recommended to new users through
rapid learning, and multi-feature fusion can be better solved.
However, such methods have the defects of complex models
and poor results for pure cold start problems.

to
This study’s primary finding is very beneficial
cross-domain and social network data to address user cold
start difficulties. As part of the selection or filtering process,
researchers frequently analyze data or inferences using pre-
established standards. This is because it’s possible that the
additional data, which mainly consists of assumptions and
information from questionable sources, isn’t accurate and
trustworthy. Researchers have chosen and sorted these facts
in this order based on their dependability. The study found
that machine learning and deep learning techniques are being
used more often in a range of academic fields. DNN, GNN,
and other techniques are being used by more researchers to
alleviate the problem of new users, as can be observed in
Fig. 8.

In recommender systems,

the use of deep learning
or machine learning techniques can successfully capture
non-linear correlations between users and items. Deep
learning can handle intricate and sophisticated interactions
in knowledge gathered from a variety of sources (like
text embeddings, context embeddings, and visual embed-
dings), as well as the encoding of complex conceptions as
higher-level information presentations. To solve user cold
start difficulties, additional research using deep learning or
machine learning methods is required. The new user issue
is being addressed in research on deep learning algorithms.
Graph neural networks or the Attention mechanism are
being used by more and more researchers. View as in
Fig. 9.

The research in this paper found that recommendations
for films, music, and books are the most researched areas.
This is because there are more publicly available datasets in
these domains. Recommendation methods for shopping and
e-commerce are next in research. This is because shopping
and product review datasets are more readily available.
However, recommendation methods in the field of education
are less researched yet extremely important. This suggests
new research directions for recommender systems scholars.

136972

VOLUME 11, 2023

---

<!-- PAGE 16 -->

H. Yuan, A. A. Hernandez: User Cold Start Problem in Recommendation Systems: A Systematic Review

FIGURE 7. Classification of user cold start recommendation strategies.

FIGURE 8. Time to solve the new users’ problem. (Yellow indicates the nearest time, and purple indicates the farthest time.)

Both the cold start problem and the data sparsity problem
are related to situations where there is insufficient informa-
tion in a recommender system, but they occur at different
times, on different scales, and with different solutions.
Approaches to the cold-start problem typically focus more
on obtaining additional information (e.g., user registration
information or item metadata), while approaches to the

data sparsity problem focus more on filling in the missing
information by using data that already exists. However,
approaches such as machine learning, meta-learning, and
some hybrid approaches can address both the cold-start
problem and the data sparsity problem.

Three main types of evaluation metrics are used for
user cold start model evaluation: Rating prediction metrics,

VOLUME 11, 2023

136973

---

<!-- PAGE 17 -->

H. Yuan, A. A. Hernandez: User Cold Start Problem in Recommendation Systems: A Systematic Review

FIGURE 9. Deep learning algorithm overlay visualization. (Yellow indicates the closest to the current time, and purple
indicates the farthest from the current time.)

FIGURE 10. The evaluation metrics overlay diagram in the literature abstract. (Yellow indicates the closest to the current time,
and purple indicates the farthest from the current time.)

Classification accuracy metrics, and Ranking Metrics. Most
of the literature will choose different types of evaluation
metrics for a comprehensive evaluation. Some papers use
one type of evaluation metrics for evaluation. Most of the
literature will adopt the Ranking Metrics type of evaluation
metrics. Fig. 10 shows the evaluation metrics overlay diagram
in the literature abstract. As can be seen from the figure,
recently more and more scholars are using NDCG to analyze
the performance of user cold start recommendation systems.

B. DIRECTIONS FOR FUTURE RESEARCH
In this research review, we survey the state-of-the-art
literature addressing the user cold-start problem. Despite
these advances, there are still many challenges that need to
be addressed.

• Collecting and utilizing additional information
Researchers have found that using additional information
about users and items can go a long way toward allevi-
ating user cold-start problems. This additional information

includes user profile information, social relationships, user
behavior, and auxiliary information (e.g., knowledge base
and time signals). However, there are great challenges in
collecting implicit user data and processing real-time user
feedback data, and it is a challenge to collect and utilize
additional information effectively.

• Multi-task learning
Deep learning-based methods are more effective in solving
the user cold start problem compared to single-task learning.
Utilizing multi-task learning in deep neural networks can
reduce the problem of having little data at the beginning
of a new user through implicit data augmentation. Some
researchers are looking to apply deeper architectures to user
data to explore additional multitask learning.

• Attention Mechanisms
The attention mechanism enables neural networks to focus
on a subset of features by selecting specific inputs, helping
to alleviate the user cold-start problem in recommender
systems. This is a mechanism that can be intuitively applied

136974

VOLUME 11, 2023

---

<!-- PAGE 18 -->

H. Yuan, A. A. Hernandez: User Cold Start Problem in Recommendation Systems: A Systematic Review

to many deep learning architectures such as CNNs and RNNs.
For example, when applying attention techniques to CNN
models, it can be utilized to select the most representative
elements and filter out uninformative ones, while providing
better interpretability. Thus, attention modeling is a promis-
ing research direction.

• Harmonized indicators for evaluating user satisfaction
It was observed in this review that although recent rec-
ommender systems have shown good performance. However,
there is no single standardized criterion that can be used to
evaluate the performance of all recommender systems. User
satisfaction and personalization play a very important role in
the success of such recommender systems. There is a need
for some new standardized evaluation criteria to evaluate the
level of user satisfaction in real-time.

• Protecting users’ private information
Interaction information and incidental information (e.g.,
social networks) are commonly used for recommendations
in solving the user cold-start problem. However, one may be
reluctant to share it with the recommender system because his
privacy may be compromised or even violated by others. How
to better protect users’ private information is an open issue.

VII. CONCLUSION AND LIMITATIONS
The focus of this paper is to analyze how the user cold start
problem has been solved in literature during the last eight
years. This study’s primary contribution is a comprehensive
analysis of 45 related literature. A thorough categorization of
solutions for the user cold start issue is provided.

This study categorizes approaches to addressing the new
user issue into data-driven and method-driven strategies. This
study can provide a comprehensive guide for future research
on solving the new user issue. It helps to understand the
direction of research and studies on new user issues.

The investigation in this paper is based solely on a
systematic literature review of 45 articles published in
academic conferences and academic journals. Although this
study has made a great endeavor to strive and collate the
strategies proposed by quite a few researchers to alleviate
the issue with user cold starts. However, no experimental
validation has been carried out for comparative analysis.
In the later phase of the study, the authors will typically focus
on this issue.

REFERENCES
[1] F. O. Isinkaye, Y. O. Folajimi, and B. A. Ojokoh, ‘‘Recommendation
systems: Principles, methods and evaluation,’’ Egyptian Informat. J.,
vol. 16, no. 3, pp. 261–273, Nov. 2015.

[2] H. Ko, S. Lee, Y. Park, and A. Choi, ‘‘A survey of recommendation
systems: Recommendation models, techniques, and application fields,’’
Electronics, vol. 11, no. 1, p. 141, Jan. 2022.

[3] K. Patel and H. B. Patel, ‘‘A state-of-the-art survey on recommendation
system and prospective extensions,’’ Comput. Electron. Agricult., vol. 178,
Nov. 2020, Art. no. 105779.

[4] J.-P. Cabrera-Sánchez,

I. Ramos-de-Luna, E. Carvajal-Trujillo, and
Á. F. Villarejo-Ramos, ‘‘Online recommendation systems: Factors influ-
encing use in e-commerce,’’ Sustainability, vol. 12, no. 21, p. 8888,
Oct. 2020, doi: 10.3390/su12218888.

[5] Y. Guo, M. Wang, and X. Li, ‘‘Application of an improved Apriori
Ind.
algorithm in a mobile e-commerce recommendation system,’’
Manage. Data Syst., vol. 117, no. 2, pp. 287–303, Mar. 2017, doi:
10.1108/imds-03-2016-0094.

[6] D. Mumin, L.-L. Shi, L. Liu, and J. Panneerselvam, ‘‘Data-driven diffusion
recommendation in online social networks for the Internet of people,’’
IEEE Trans. Syst., Man, Cybern., Syst., vol. 52, no. 1, pp. 166–178,
Jan. 2022, doi: 10.1109/TSMC.2020.3015355.

[7] W. Zhang, F. Liu, D. Xu, and L. Jiang, ‘‘Recommendation system in social
networks with topical attention and probabilistic matrix factorization,’’
PLoS ONE, vol. 14, no. 10, Oct. 2019, Art. no. e0223967, doi:
10.1371/journal.pone.0223967.

[8] M. Zhang, G. Wang, L. Ren, J. Li, K. Deng, and B. Zhang,
‘‘METoNR: A meta explanation triplet oriented news recommendation
model,’’ Knowl.-Based Syst., vol. 238, Feb. 2022, Art. no. 107922, doi:
10.1016/j.knosys.2021.107922.

[9] D. Z. Ulian, J. L. Becker, C. B. Marcolin, and E. Scornavacca, ‘‘Exploring
the effects of different clustering methods on a news recommender
system,’’ Expert Syst. Appl., vol. 183, Nov. 2021, Art. no. 115341, doi:
10.1016/j.eswa.2021.115341.

[10] J. Davidson, B. Liebald, J. Liu, P. Nandy, and T. Van Vleet, ‘‘The YouTube
video recommendation system,’’ in Proc. 4th ACM Conf. Recommender
Syst., Sep. 2010, pp. 293–296, doi: 10.1145/1864708.1864770.

[11] Z. Chen, S. Ye, X. Chu, H. Xia, H. Zhang, H. Qu, and Y. Wu, ‘‘Augmenting
sports videos with VisCommentator,’’ IEEE Trans. Vis. Comput. Graphics,
vol. 28, no. 1, pp. 824–834, Jan. 2022, doi: 10.1109/TVCG.2021.3114806.
‘‘Deep learning in music recommendation systems,’’
Frontiers Appl. Math. Statist., vol. 5, p. 44, Aug. 2019, doi:
10.3389/fams.2019.00044.

[12] M. Schedl,

[13] S. S. Khanal, P. W. C. Prasad, A. Alsadoon, and A. Maag, ‘‘A systematic
review: Machine learning based recommendation systems for e-learning,’’
Educ. Inf. Technol., vol. 25, no. 4, pp. 2635–2664, Jul. 2020, doi:
10.1007/s10639-019-10063-9.

[14] M. C. Urdaneta-Ponte, A. Mendez-Zorrilla, and I. Oleagordia-Ruiz, ‘‘Rec-
ommendation systems for education: Systematic review,’’ Electronics,
vol. 10, no. 14, p. 1611, Jul. 2021, doi: 10.3390/electronics10141611.
[15] I. Uddin, A. S. Imran, K. Muhammad, N. Fayyaz, and M. Sajjad, ‘‘A sys-
tematic mapping review on MOOC recommender systems,’’ IEEE Access,
vol. 9, pp. 118379–118405, 2021, doi: 10.1109/ACCESS.2021.3101039.
[16] Y. Ma, X. Geng, and J. Wang, ‘‘A deep neural network with multiplex inter-
actions for cold-start service recommendation,’’ IEEE Trans. Eng. Manag.,
vol. 68, no. 1, pp. 105–119, Feb. 2021, doi: 10.1109/TEM.2019.2961376.
[17] F. Tahmasebi, M. Meghdadi, S. Ahmadian, and K. Valiallahi, ‘‘A hybrid
recommendation system based on profile expansion technique to alleviate
cold start problem,’’ Multimedia Tools Appl., vol. 80, no. 2, pp. 2339–2354,
Jan. 2021, doi: 10.1007/s11042-020-09768-8.

[18] L. Paleti, P. R. Krishna, and J. V. R. Murthy, ‘‘Approaching the cold-
start problem using community detection based alternating least square
factorization in recommendation systems,’’ Evol. Intell., vol. 14, no. 2,
pp. 835–849, Jun. 2021, doi: 10.1007/s12065-020-00464-y.

[19] N. T. Al Ghifari, B. Sitohang, and G. A. P. Saptawati, ‘‘Addressing cold
start new user in recommender system based on hybrid approach: A review
and bibliometric analysis,’’ IT J. Res. Dev., vol. 6, no. 1, pp. 1–16, 2021.

[20] R. Yu, Y. Gong, X. He, Y. Zhu, Q. Liu, W. Ou, and B. An, ‘‘Personalized
adaptive meta-learning for cold-start user preference prediction,’’ in Proc.
35th AAAI Conf. Artif. Intell., 2021, vol. 35, no. 12, pp. 10772–10780, doi:
10.1609/aaai.v35i12.17287.

[21] Y. Zhu, J. Lin, S. He, B. Wang, Z. Guan, H. Liu, and D. Cai, ‘‘Addressing
the item cold-start problem by attribute-driven active learning,’’ IEEE
Trans. Knowl. Data Eng., vol. 32, no. 4, pp. 631–644, Apr. 2020, doi:
10.1109/TKDE.2019.2891530.

[22] Y. Bi, L. Song, M. Yao, Z. Wu, J. Wang, and J. Xiao, ‘‘A heterogeneous
information network based cross domain insurance recommendation sys-
tem for cold start users,’’ in Proc. 43rd Int. ACM SIGIR Conf. Res. Develop.
Inf. Retr., Jul. 2020, pp. 2211–2220, doi: 10.1145/3397271.3401426.

[23] J. Wei, J. He, K. Chen, Y. Zhou, and Z. Tang,

‘‘Collaborative
filtering and deep learning based recommendation system for cold
start items,’’ Expert Syst. Appl., vol. 69, pp. 29–39, Mar. 2017, doi:
10.1016/j.eswa.2016.09.040.

[24] A. Da’u and N. Salim, ‘‘Recommendation system based on deep learning
methods: A systematic review and new directions,’’ Artif. Intell. Rev.,
vol. 53, no. 4, pp. 2709–2748, Apr. 2020, doi: 10.1007/s10462-019-
09744-1.

VOLUME 11, 2023

136975

---

<!-- PAGE 19 -->

H. Yuan, A. A. Hernandez: User Cold Start Problem in Recommendation Systems: A Systematic Review

[25] L. A. G. Camacho and S. N. Alves-Souza, ‘‘Social network data
to alleviate cold-start in recommender system: A systematic review,’’
Inf. Process. Manage., vol. 54, no. 4, pp. 529–544, Jul. 2018, doi:
10.1016/j.ipm.2018.03.004.

[26] D. K. Panda and S. Ray, ‘‘Approaches and algorithms to mitigate
cold start problems in recommender systems: A systematic literature
review,’’ J. Intell. Inf. Syst., vol. 59, no. 2, pp. 341–366, Oct. 2022, doi:
10.1007/s10844-022-00698-5.

[27] L. H. Son, ‘‘Dealing with the new user cold-start problem in recommender
systems: A comparative review,’’ Inf. Syst., vol. 58, pp. 87–104, Jun. 2016,
doi: 10.1016/j.is.2014.10.001.

[28] N. A. Abdullah, R. A. Rasheed, M. H. N. M. Nasir, and M. M. Rahman,
‘‘Eliciting auxiliary information for cold start user recommendation:
A survey,’’ Appl. Sci., vol. 11, no. 20, p. 9608, Oct. 2021, doi:
10.3390/app11209608.

[29] B. Kitchenham, ‘‘Guidelines for performing systematic literature reviews
in software engineering,’’ Univ. Durham, Durham, U.K., Tech. Rep. EBSE-
2007-01, Version 2.3, 2007.

[30] B. Kitchenham, O. P. Brereton, D. Budgen, M. Turner, J. Bailey, and
S. Linkman, ‘‘Systematic literature reviews in software engineering—
A systematic literature review,’’ Inf. Softw. Technol., vol. 51, no. 1,
pp. 7–15, Jan. 2009, doi: 10.1016/j.infsof.2008.09.009.

[31] S. Sedhain, A. Menon, S. Sanner, L. Xie, and D. Braziunas, ‘‘Low-
rank linear cold-start recommendation from social data,’’ in Proc. AAAI
Conf. Artif. Intell., Feb. 2017, vol. 31, no. 1, pp. 1502–1508, doi:
10.1609/aaai.v31i1.10758.

[32] L. Briand, G. Salha-Galvan, W. Bendada, M. Morlon, and V. A. Tran,
‘‘A semi-personalized system for user cold start recommendation on music
streaming apps,’’ in Proc. 27th ACM SIGKDD Conf. Knowl. Discovery
Data Mining, Aug. 2021, pp. 2601–2609, doi: 10.1145/3447548.3467110.
[33] R. Mondal and B. Bhowmik, ‘‘DeCS: A deep neural network framework
IEEE
for cold start problem in recommender systems,’’
Region 10 Symp. (TENSYMP), Jul. 2022, pp. 1–6, doi: 10.1109/TEN-
SYMP54529.2022.9864409.

in Proc.

[34] Y. Kumar, A. Sharma, A. Khaund, A. Kumar, P. Kumaraguru, and
R. R. Shah, ‘‘IceBreaker: Solving cold start problem for video recommen-
dation engines,’’ in Proc. IEEE Int. Symp. Multimedia (ISM), Dec. 2019,
pp. 217–222, doi: 10.1109/ISM.2018.000-3.

[35] C. C. Chen, P.-L. Lai, and C.-Y. Chen, ‘‘ColdGAN: An effective cold-
start recommendation system for new users based on generative adversarial
networks,’’ Int. J. Speech Technol., vol. 53, no. 7, pp. 8302–8317,
Apr. 2023, doi: 10.1007/s10489-022-04005-1.

[36] B. Hao, H. Yin, J. Zhang, C. Li, and H. Chen, ‘‘A multi-strategy-based pre-
training method for cold-start recommendation,’’ ACM Trans. Inf. Syst.,
vol. 41, no. 2, pp. 1–24, Apr. 2023, doi: 10.1145/3544107.

[37] D. Cai, S. Qian, Q. Fang, J. Hu, and C. Xu,

‘‘User cold-start
recommendation via inductive heterogeneous graph neural network,’’ ACM
Trans. Inf. Syst., vol. 41, no. 3, pp. 1–27, Jul. 2023, doi: 10.1145/3560487.
[38] B. Hao, J. Zhang, H. Yin, C. Li, and H. Chen, ‘‘Pre-training graph neural
networks for cold-start users and items representation,’’ in Proc. 14th
ACM Int. Conf. Web Search Data Mining, Mar. 2021, pp. 266–273, doi:
10.1145/3437963.3441738.

[39] T. Qian, Y. Liang, Q. Li, and H. Xiong,

‘‘Attribute graph neu-
IEEE Trans.
ral networks for strict cold start
Knowl. Data Eng., vol. 34, no. 8, pp. 3597–3610, Aug. 2022, doi:
10.1109/TKDE.2020.3038234.

recommendation,’’

[40] E. Kannout, M. Grodzki, and M. Grzegorowski, ‘‘Utilizing frequent
pattern mining for solving cold-start problem in recommender systems,’’
in Proc. 17th Conf. Comput. Sci. Intell. Syst., 2022, pp. 217–226, doi:
10.15439/2022F86.

[41] E. J. Chia and M. K. Najafabadi,

‘‘Solving cold start problem
for recommendation system using content-based filtering,’’ in Proc.
Int. Conf. Comput. Technol. (ICCTech), Feb. 2022, pp. 38–42, doi:
10.1109/ICCTech55650.2022.00015.

[42] P. Li, R. Chen, Q. Liu, J. Xu, and B. Zheng, ‘‘Transform cold-start users
into warm via fused behaviors in large-scale recommendation,’’ in Proc.
45th Int. ACM SIGIR Conf. Res. Develop. Inf. Retr., 2022, pp. 2013–2017,
doi: 10.1145/3477495.3531797.

[43] P. Cremonesi, A. Tripodi, and R. Turrin, ‘‘Cross-domain recommender
systems,’’ in Proc. IEEE 11th Int. Conf. Data Mining Workshops,
Dec. 2011, pp. 496–503, doi: 10.1109/ICDMW.2011.57.

[44] P. Cantador, I. Fernandez-Tobias, S. Berkovsky, and P. Cremonesi, ‘‘Cross-
domain recommender systems,’’ in Recommender Systems Handbook.
Boston, MA, USA: Springer, 2015, pp. 919–959.

[45] Y. Jin, S. Dong, Y. Cai, and J. Hu,

‘‘RACRec: Review aware
IEEE
cross-domain
for
Access, vol. 8, pp. 55032–55041, 2020, doi: 10.1109/ACCESS.2020.
2982037.

recommendation

fully-cold-start

user,’’

[46] H. Wang, D. Amagata, T. Makeawa, T. Hara, N. Hao, K. Yonekawa,
and M. Kurokawa, ‘‘A DNN-based cross-domain recommender system for
alleviating cold-start problem in e-commerce,’’ IEEE Open J. Ind. Elec-
tron. Soc., vol. 1, pp. 194–206, 2020, doi: 10.1109/ojies.2020.3012627.

[47] C. Zhao, C. Li, R. Xiao, H. Deng, and A. Sun, ‘‘CATN: Cross-domain
recommendation for cold-start users via aspect transfer network,’’ in Proc.
43rd Int. ACM SIGIR Conf. Res. Develop. Inf. Retr., 2020, pp. 229–238,
doi: 10.1145/3397271.3401169.

[48] C.-T. Li, C.-T. Hsu, and M.-K. Shan, ‘‘A cross-domain recommendation
mechanism for cold-start users based on partial least squares regression,’’
ACM Trans. Intell. Syst. Technol., vol. 9, no. 6, pp. 1–26, Nov. 2018, doi:
10.1145/3231601.

[49] Y. Zhu, K. Ge, F. Zhuang, R. Xie, D. Xi, X. Zhang, L. Lin, and Q. He,
‘‘Transfer-meta framework for cross-domain recommendation to cold-start
users,’’ in Proc. 44th Int. ACM SIGIR Conf. Res. Develop. Inf. Retr., 2021,
pp. 1813–1817, doi: 10.1145/3404835.3463010.

[50] U. Yadav, N. Duhan, and K. K. Bhatia, ‘‘Dealing with pure new user cold-
start problem in recommendation system based on linked open data and
social network features,’’ Mobile Inf. Syst., vol. 2020, pp. 1–20, Jun. 2020,
doi: 10.1155/2020/8912065.

[51] R. Reshma, G. Ambikesh, and P. S. Thilagam, ‘‘Alleviating data sparsity
and cold start
in recommender systems using social behavior,’’ in
Proc. Int. Conf. Recent Trends Inf. Technol., Apr. 2016, pp. 1–8, doi:
10.1109/ICRTIT.2016.7569532.

[52] J. Li, K. Lu, Z. Huang, and H. T. Shen, ‘‘On both cold-start and
long-tail recommendation with social data,’’ IEEE Trans. Knowl. Data
Eng., vol. 33, no. 1, pp. 194–208, Jan. 2021, doi: 10.1109/TKDE.2019.
2924656.

[53] Q. Gong, Y. Chen, X. He, Y. Xiao, P. Hui, X. Wang, and X. Fu, ‘‘Cross-
site prediction on social influence for cold-start users in online social
networks,’’ ACM Trans. Web, vol. 15, no. 2, pp. 1–23, May 2021, doi:
10.1145/3409108.

[54] Y. Lu, K. Nakamura, and R. Ichise, ‘‘HyperRS: Hypernetwork-based
recommender system for the user cold-start problem,’’ IEEE Access,
vol. 11, pp. 5453–5463, 2023, doi: 10.1109/ACCESS.2023.3236391.
[55] X. Huang, J. Sang, J. Yu, and C. Xu, ‘‘Learning to learn a cold-start
sequential recommender,’’ ACM Trans. Inf. Syst., vol. 40, no. 2, pp. 1–25,
Apr. 2022, doi: 10.1145/3466753.

[56] F. Jiang, Q. Xu, W. Li, B. Xiao, and Y. Luo, ‘‘They like comedy, don’t
you? A cluster-based meta-learning for cold-start recommendation,’’ in
Proc. IEEE Int. Conf. Multimedia Expo (ICME), Jul. 2022, pp. 1–6, doi:
10.1109/ICME52920.2022.9859863.

[57] G. Wang and X. Wang,

with collaborative boosted meta transitional
5th Int. Conf. Data Sci.
10.1109/DSIT55514.2022.9943897.

sequential

‘‘Cold-start

recommendation
in Proc.
Inf. Technol., Jul. 2022, pp. 1–5, doi:

learning,’’

[58] M. Dong, F. Yuan, L. Yao, X. Xu, and L. Zhu, ‘‘MAMO: Memory-
augmented meta-optimization for cold-start recommendation,’’ in Proc.
26th ACM SIGKDD Int. Conf. Knowl. Discovery Data Mining, 2020,
pp. 688–697, doi: 10.1145/3394486.3403113.

[59] S. Liu, Y. Liu, X. Zhang, C. Xu, J. He, and Y. Qi, ‘‘Improving the
performance of cold-start recommendation by fusion of attention network
and meta-learning,’’ Electronics, vol. 12, no. 2, p. 376, Jan. 2023, doi:
10.3390/electronics12020376.

[60] J. Misztal-Radecka, B. Indurkhya, and A. Smywišski-Pohl, ‘‘Meta-
User2Vec model for addressing the user and item cold-start problem in
recommender systems,’’ User Model. User-Adapted Interact., vol. 31,
no. 2, pp. 261–286, Apr. 2021, doi: 10.1007/s11257-020-09282-4.
[61] Y. Shen, L. Zhao, W. Cheng, Z. Zhang, W. Zhou, and L. Kangyi, ‘‘RESUS:
Warm-up cold users via meta-learning residual user preferences in CTR
prediction,’’ ACM Trans. Inf. Syst., vol. 41, no. 3, pp. 1–26, Jul. 2023, doi:
10.1145/3564283.

[62] H. Lee, J. Im, S. Jang, H. Cho, and S. Chung, ‘‘Melu: Meta-learned user
preference estimator for cold-start recommendation,’’ in Proc. 25th ACM
SIGKDD Int. Conf. Knowl. Discovery Data Mining, 2019, pp. 1073–1082,
doi: 10.1145/3292500.3330859.

[63] X. Lin, J. Wu, C. Zhou, S. Pan, Y. Cao, and B. Wang, ‘‘Task-adaptive neural
process for user cold-start recommendation,’’ in Proc. Web Conf., 2021,
pp. 1306–1316, doi: 10.1145/3442381.3449908.

136976

VOLUME 11, 2023

---

<!-- PAGE 20 -->

H. Yuan, A. A. Hernandez: User Cold Start Problem in Recommendation Systems: A Systematic Review

[64] T. Wei, Z. Wu, R. Li, Z. Hu, F. Feng, X. He, Y. Sun, and W. Wang,
‘‘Fast adaptation for cold-start collaborative filtering with meta-learning,’’
in Proc. IEEE Int. Conf. Data Mining (ICDM), Nov. 2020, pp. 661–670,
doi: 10.1109/ICDM50108.2020.00075.

[65] K. P. Neupane, E. Zheng, and Q. Yu, ‘‘MetaEDL: Meta evidential
learning for uncertainty-aware cold-start recommendations,’’ in Proc.
IEEE Int. Conf. Data Mining (ICDM), Dec. 2021, pp. 1258–1263, doi:
10.1109/ICDM51629.2021.00154.

[66] H. Bharadhwaj, ‘‘Meta-learning for user cold-start recommendation,’’ in
Proc. Int. Joint Conf. Neural Netw. (IJCNN), Jul. 2019, pp. 1–8, doi:
10.1109/IJCNN.2019.8852100.
and Y. Zhao,

‘‘ML2E: Meta-learning

[67] H. Wang

ensemble for cold-start
pp. 165757–165768, 2020, doi: 10.1109/ACCESS.2020.3022796.
[68] T. Zhou, Y. Zeng, Y. Li, Z. Jiang, Z. Liu, and T. Li,

recommendation,’’

‘‘Cold-
recommendation method based on homomorphic encryption,’’
Int. Conf. Netw. Netw. Appl., 2021, pp. 461–465, doi:

start
in Proc.
10.1109/NaNA53684.2021.00086.

embedding
IEEE Access, vol. 8,

[69] S. Natarajan, S. Vairavasundaram, K. Kotecha, V. Indragandhi, S. Palani,
J. R. Saini, and L. Ravi, ‘‘CD-SemMF: Cross-domain semantic relatedness
based matrix factorization model enabled with linked open data for user
cold start issue,’’ IEEE Access, vol. 10, pp. 52955–52970, 2022, doi:
10.1109/ACCESS.2022.3175566.

[70] Y. Lin, P. Ren, Z. Chen, Z. Ren, D. Yu, J. Ma, and X. Cheng, ‘‘Meta
matrix factorization for federated rating predictions,’’ in Proc. 43rd Int.
ACM SIGIR Conf. Res. Develop. Inf. Retr., Jul. 2020, pp. 981–990.
[71] H.-H. Chen and P. Chen, ‘‘Differentiating regularization weights—A
simple mechanism to alleviate cold start in recommender systems,’’ ACM
Trans. Knowl. Discovery Data, vol. 13, no. 1, pp. 1–22, Feb. 2019, doi:
10.1145/3285954.

[72] R. Kumar, P. K. Bala, and S. Mukherjee, ‘‘A new neighbourhood
formation approach for solving cold-start user problem in collaborative
filtering,’’ Int. J. Appl. Manage. Sci., vol. 12, no. 2, p. 118, 2020, doi:
10.1504/ijams.2020.106734.

[73] Z. Zhang, M. Dong, K. Ota, and Y. Kudo, ‘‘Alleviating new user cold-
start in user-based collaborative filtering via bipartite network,’’ IEEE
Trans. Computat. Social Syst., vol. 7, no. 3, pp. 672–685, Jun. 2020, doi:
10.1109/TCSS.2020.2971942.

[74] D.-K. Chae, J. Kim, D. H. Chau, and S.-W. Kim, ‘‘AR-CF: Augmenting
virtual users and items in collaborative filtering for addressing cold-start
problems,’’ in Proc. 43rd Int. ACM SIGIR Conf. Res. Develop. Inf. Retr.,
Jul. 2020, pp. 1251–1260, doi: 10.1145/3397271.3401038.

[75] T. Duricic, D. Kowald, E. Lacic, and E. Lex, ‘‘Trust-based collaborative
filtering: Tackling the cold start problem using regular equivalence,’’
in Proc. 12th ACM Conf. Recommender Syst., 2018, pp. 446–450, doi:
10.1145/3240323.3240404.

[76] X. Chao and C. Guangcai, ‘‘Collaborative filtering and leaders’ advice
based recommendation system for cold start users,’’ in Proc. 6th Int. Conf.
Comput. Artif. Intell., 2020, pp. 158–164, doi: 10.1145/3404555.3404644.
[77] N. F. Al-Bakri and S. Hassan, ‘‘A proposed model to solve cold start
problem using fuzzy user-based clustering,’’ in Proc. 2nd Sci. Conf.
Comput. Sci., Mar. 2019, pp. 121–125, doi: 10.1109/SCCS.2019.8852624.
[78] A. Zahid, N. Sharef, and A. Mustapha, ‘‘Normalization-based neigh-
borhood model for cold start problem in recommendation system,’’ Int.
Arab J. Inf. Technol., vol. 17, no. 3, pp. 422–431, May 2020, doi:
10.34028/iajit/17/3/1.

[79] L. Hu, L. Cao, J. Cao, Z. Gu, G. Xu, and D. Yang, ‘‘Learning informative
priors from heterogeneous domains to improve recommendation in cold-
start user domains,’’ ACM Trans. Inf. Syst., vol. 35, no. 2, pp. 1–37,
Apr. 2017, doi: 10.1145/2976737.

[80] Y. Shao and Y. H. Xie, ‘‘Research on cold-start problem of collaborative
filtering algorithm,’’ in Proc. 3rd Int. Conf. Big Data Res., 2019, pp. 67–71,
doi: 10.1145/3372454.3372470.

[81] B. Wang, C. Zhang, H. Zhang, X. Lyu, and Z. Tang, ‘‘Dual autoencoder
network with swap reconstruction for cold-start recommendation,’’ in
Proc. 29th ACM Int. Conf. Inf. Knowl. Manag., 2020, pp. 2249–2252, doi:
10.1145/3340531.3412069.

[82] Y. Bi, L. Song, M. Yao, Z. Wu, J. Wang, and J. Xiao, ‘‘DCDIR: A deep
cross-domain recommendation system for cold start users in insurance
domain,’’ in Proc. 43rd Int. ACM SIGIR Conf. Res. Develop. Inf. Retr.,
2020, pp. 1661–1664, doi: 10.1145/3397271.3401193.

[83] H. Wang, D. Amagata, T. Maekawa, T. Hara, H. Niu, K. Yonekawa,
and M. Kurokawa, ‘‘Preliminary investigation of alleviating user cold-
start problem in e-commerce with deep cross-domain recommender
system,’’ in Proc. World Wide Web Conf., 2019, pp. 398–403, doi:
10.1145/3308560.3316596.

[84] J. Wang, K. Ding, and J. Caverlee, ‘‘Sequential recommendation for
learning,’’ in Proc. 44th Int.
cold-start users with meta transitional
ACM SIGIR Conf. Res. Develop. Inf. Retr., 2021, pp. 1783–1787, doi:
10.1145/3404835.3463089.

[85] R. Togashi, M. Otani, and S. Satoh, ‘‘Alleviating cold-start problems
in recommendation through pseudo-labelling over knowledge graph,’’ in
Proc. 14th ACM Int. Conf. Web Search Data Mining, 2021, pp. 931–939,
doi: 10.1145/3437963.3441773.

HONGLI YUAN received the Bachelor of Science
degree in computer science and technology from
Northwest Normal University, Lanzhou, China,
in 2009, and the master’s degree in computer appli-
cations from Southwest University, Chongqing,
China, in 2013. She is currently pursuing the Ph.D.
degree in computer science with the National
University of the Philippines.

Since 2013, she has been an Associate Professor
with the School of Big Data and Artificial
Intelligence, Anhui Xinhua University. She is the author of more than
20 papers and one Chinese invention patent. Her research interests include
big data, data mining, and information security.

ALEXANDER A. HERNANDEZ (Member, IEEE)
received the bachelor’s and master’s degrees in
information technology from the Technological
Institute of the Philippines, in 2008 and 2011,
respectively, and the Ph.D. degree in information
technology from De La Salle University, Manila,
Philippines, in 2016.

He is currently a Professor with the Graduate
Programs, College of Computing and Informa-
tion Technologies, National University, Manila.
He received a Research Fellowship grant from the Singapore National
Academy of Science, in 2022, to work on developing a digital platform for
older adults that integrates artificial intelligence and games-based cognitive
function screening. He has been involved in externally funded projects and
consultancy work in some multinational firms. He has published papers
in reputable international journals and conferences. His research interests
include the intersections of applied machine learning, information systems,
and sustainability.

Prof. Hernandez is a member of the Association for Information
Systems (AIS) and the Philippines Society of Information Technology
Educators, National Capital Region (PSITE—NCR). He is actively serving
in professional communities on the editorial review board of journals in
computing and international conferences advisory and technical committees.

VOLUME 11, 2023

136977

<!-- MARKITDOWN CONVERSION -->

<!-- Full MarkItDown conversion for formatting fidelity. -->

Received12October2023,accepted27November2023,dateofpublication1December2023,
dateofcurrentversion11December2023.
DigitalObjectIdentifier10.1109/ACCESS.2023.3338705
User Cold Start Problem in Recommendation
Systems: A Systematic Review
HONGLIYUAN 1,2 ANDALEXANDERA.HERNANDEZ 1,(Member,IEEE)
1CollegeofComputingandInformationTechnologies,NationalUniversity,Manila1008,Philippines
2BigDataandArtificialIntelligenceCollege,AnhuiXinhuaUniversity,Hefei230088,China
Correspondingauthor:HongliYuan(yuanhongli@axhu.edu.cn)
ThisworkwassupportedinpartbytheNaturalScienceFoundationoftheAnhuiProvincialEducationOfficeunderGrant2022AH051868
andGrantKJ2021A1156;inpartbytheNaturalScienceFoundationoftheAnhuiXinhuaUniversityunderGrant2020zr002andGrant
kytd202203;andinpartbytheQualityEngineeringProject2022xxkc053,Project2022jyxm651,andProject2022kcszx04.
ABSTRACT Therecommendationsystemmakesrecommendationsbasedonthepreferencesoftheusers.
Theseuserpreferencesusuallycomefromtheuser’sbasicinformation,itemrating,historicaldata,andso
on. The ‘‘user cold start problem’’ happens when a new user cannot be appropriately suggested due to a
lack of more detailed preference information. In many instances, the user cold start problem hinders the
useoftherecommendationsystem.Manyresearchersarecurrentlytryingtodiscoverasolutiontotheuser
coldstartproblem.Unfortunately,therearetwodrawbacksinthecurrentsystematicreviewsofhowtodeal
withtheusercoldstartproblem.First,systematicreviewsonhowtodealwiththeusercoldstartproblem
are scarce or outdated. Second, existing reviews lack the distinction between the user cold start problem
and the item cold start problem. Nevertheless, the solutions to the two problems differ. To address these
problems,ourstudythoroughreviewofallliteraturepublishedbyresearchersfromJanuary2016toApril
2023 about 8 years. Firstly, this study analyzes the literatures on approaches that addressed the user cold
startproblemduringthepasteightyearsanddividesthemintotwocategories:data-driventechnologyand
approach-driventechnology,andthendescribesandclassifieseachtypeoftechnologyindetail.Secondly,
thisstudyalsoanalyzesthemainevaluationcriteriacurrentlyusedinthesemethodstoprovideareference
forresearchersinrelatedfields.Finally,thispaperalsopointsoutthefutureresearchdirectionofthisfield.
INDEXTERMS Recommendationsystems,usercoldstart,systematicreview.
I. INTRODUCTION a recommendation system can help users find information
With the continuous development of the Internet, mobile that meets their needs quickly and accurately [2]. This
Internet, big data, and other technologies, people’s lives are improves user satisfaction and user experience [3]. Today,
being saturated by an increasing amount of information. recommendationsystemsarewidelyusedine-commerce[4],
Thus, users face the problem of information overload. How [5], social networks [6], [7], news [8], [9], video [10], [11],
to enable users to efficiently and quickly find the requested music [3], [12], education [13], [14], [15], and other fields.
items from a large amount of information has become the It provides more intelligent and personalized services for
currentresearchhotspotsanddifficulties. users. Recommender systems play an important role in the
The recommender system can provide items that may be currentsociety.
of interest to users based on their previous interaction data However,thecoldstartproblemofrecommendersystems
in the system. It also uses user feedback to optimize the is a common problem in recommender systems [16], [17],
system’s recommendation capabilities [1]. Compared with [18], [19]. It is mainly divided into user cold start [20] and
categorized queries and search engines, the emergence of item cold start [21], [22]. To make the cold-start problem
easier to understand, a simple example of recommendation
The associate editor coordinating the review of this manuscript and usinguserratingsisexemplifiedinTable1.InTable1rows
approvingitforpublicationwasFabrizioMessina . represent users. The columns represent n items. The rating
2023TheAuthors.ThisworkislicensedunderaCreativeCommonsAttribution-NonCommercial-NoDerivatives4.0License.
136958 Formoreinformation,seehttps://creativecommons.org/licenses/by-nc-nd/4.0/ VOLUME11,2023

H.Yuan,A.A.Hernandez:UserColdStartProbleminRecommendationSystems:ASystematicReview
matrix represents the user ratings of the items in the range the process followed in this paper to write the systematic
{1,2,3,4,5},andtheratingscanonlybeintegers.Thescore literaturereview.SectionIVdescribestheliteraturestatistics.
represents the user’s rating for the item, and if the user has SectionVpresentstheresultsofthisthesisandtheanalysisof
notratedtheitem,itisdenotedby‘‘−’’. theresults.SectionVIpresentsadiscussionoftheusercold
start issue in recommender systems and the main research
TABLE1. Thecoldstartexample.
directions.Finally,SectionVIIistheconclusion.
II. RELATEDWORK
The research on cold start questions for new users is
summarizedintheparagraphsthatfollow.
Panda and Ray [26] conducted a study and review of
91 articles on cold-start mitigation. The study was the first
A. ITEMCOLDSTART to categorize the various approaches into data-driven and
Fornewitems,thelackofhistoricaldatamakesitdifficultto method-driven strategies. It also categorized method-driven
understandthecharacteristicsofitemsanduserpreferences, strategies into five main approaches based on the methods
which leads to inaccurate recommendation results. As in usedbytheresearchers.Thestudyalsoanalyzedthebench-
Table1,Itemnisnewandhasnouserratings.Therefore,itis mark algorithms used for comparison and the evaluation
notpossibletorecommendthisitembasedonuserratings. metrics used to assess the cold start problem. However, the
studydidnotseparateusercoldstartsfromprojectcoldstarts.
B. USERCOLDSTART In solving the cold start problem, these two problems are
For new users, it is difficult to accurately predict users’ solveddifferently.
interests and behaviors due to the lack of historical data, Camacho and Alves-Souza [25] investigated the research
which leads to inaccurate recommendation results or even on the application of data from social networks between
uselessrecommendationresults.AsshowinTable1,thenew 2011and2017toalleviatethecoldstartissue.Inrecommen-
userCaryhasnotusedtheitemsintherecommendersystem dationswithoutpurchasehistoryorpreferenceselection,the
andhasnotevaluatedtheitemsafterusingthem.Iftheuser’s analysis discovered. Information from social networks can
evaluation information is used to recommend items to the be effectively utilized to make up for users’ data shortages.
user,itisdifficulttoaccuratelyrecommendthedesireditems deliveringmorepersuasivesuggestions.However,thispaper
toGary. only study on using social networks to address the issues
This affects the performance and accuracy of the recom- facing new users. However, other good solutions like the
mendationsystemandismoreobviouswhenthenumberof application of deep learning, machine learning, etc. are no
newusersandnewitemsislarge.Therearecurrentlymany longerbeingtakenintoconsideration.
different approaches to solving cold starts to improve the Son [27] also a comprehensive study of the issue of cold
accuracyandperformanceofrecommendersystems[23].The starts for new users. The researchers provide a comparative
methodsusedtosolvedifferentcoldstartsaredifferent,and analysis of three approaches for the new user cold-start
thispaperfocusesonusercoldstartissues.Thispaperrefersto problem, including (i) using other sources of information,
theusercoldstartissueasthenewuserissueinlaterthepaper. (ii)choosingthemostsignificantsimilarusercategories,and
The mitigation of the user cold start problem is essential (iii) improving predictions with a hybrid technique. Several
for the large-scale utility of recommender systems. It can important algorithms, including MIPFGWC-CS, NHSM,
nolongersolelypointouttheaccuracyofrecommendation, FARAMS,andHU-FCF,arealsocomparedandexaminedin
however additionally enhances the user experience. How to the study. However, this systematic review was finished in
resolve the user cold start issues? This problem has been a 2014, and there are a lot of new techniques that this paper
hotspotintheresearchofavarietyofrecommendersystems hasn’tconsideredlately.
inrecentyears. Abdullahetal.[28]providesadetailedclassificationand
Several systematic literature reviews exist for cold start introduction of methods to address the new user problem
problemsinrecommendersystems[24],[25],[26].However, through assisted information. It also includes a thorough
in general, it is known that different approaches are used explanation of how to acquire and extract auxiliary data.
to solve different cold start problems. Currently, there are Thissystematicreviewfocusesondata-drivenstrategiesfor
fewsystematicreviewsoftheliteraturethataddressthenew solving the new user cold start issue. Less consideration is
userproblems.Son[27]providesadetaileddiscussionofthe giventothemethod-drivenstrategy.
newuserprobleminthreecategories.However,thisresearch In conclusion, there are several issues with the existing
waspublishedearlieranddoesnotcovertherecentyearsof study of the literature on how to solve the user cold
researchonsolvingusercoldstartproblems. start problem. (i) The user cold start problem is addressed
The following sections of the paper are organized as in outdated evaluations of the literature. The most recent
follows. Section II presents previous work related to the relevant literature is not taken into consideration. (ii) The
user cold start issues. Section III specifically describes analysis for resolving the user cold-start problem solely
VOLUME11,2023 136959

H.Yuan,A.A.Hernandez:UserColdStartProbleminRecommendationSystems:ASystematicReview
concentrates on one specific kind of approach. They do TABLE3. Searchstringsforsystematicreviewsoftheliterature.
| not take   | into account     | other     | method    | categories      |             | like machine |     |     |     |     |     |     |     |
| ---------- | ---------------- | --------- | --------- | --------------- | ----------- | ------------ | --- | --- | --- | --- | --- | --- | --- |
| learning,  | deep             | learning, | etc (iii) | The review      | is          | based on all |     |     |     |     |     |     |     |
| cold-start | problems,        | with      | no        | differentiation | made        | between      |     |     |     |     |     |     |     |
| user and   | project-specific |           | problems. | The             | resolutions | to these     |     |     |     |     |     |     |     |
twoproblems,however,differfromoneanother.
| The user | cold | start issue | has | a significant | impact | on how |     |     |     |     |     |     |     |
| -------- | ---- | ----------- | --- | ------------- | ------ | ------ | --- | --- | --- | --- | --- | --- | --- |
recommendersystemsareused.Unlikeotherreviewsofthe
coldstartproblem,thisreviewonlylooksattheusercoldstart
problemliteraturefromthelasteightyears.Theapproaches
| employed | are   | categorized   | and | thoroughly   | examined | in this    |           |        |        |          |     |     |            |
| -------- | ----- | ------------- | --- | ------------ | -------- | ---------- | --------- | ------ | ------ | -------- | --- | --- | ---------- |
| study to | be as | comprehensive |     | as possible. | The      | study also |           |        |        |          |     |     |            |
|          |       |               |     |              |          |            | • Step 2: | Choose | search | keywords |     | and | browse the |
offersanin-depthreviewoftheevaluationcriteriaandopen
problemscurrentlyappliedtothesemethods. literaturedatabaseinsteptwo.Inthisstage,thesearch
|     |     |     |     |     |     |     | string is | specified | by  | the format | of      | the selected | search |
| --- | --- | --- | --- | --- | --- | --- | --------- | --------- | --- | ---------- | ------- | ------------ | ------ |
|     |     |     |     |     |     |     | database  | (as shown | in  | Table      | 3). The | databases    | used   |
III. SYSTEMATICLITERATUREREVIEWMETHODOLOGY
A thorough evaluation of the literature is crucial for raising forthisstudyincludeIEEE,ACM,andWebofScience.
|     |     |     |     |     |     |     | These three | datasets |     | pretty | much | cover everything | a   |
| --- | --- | --- | --- | --- | --- | --- | ----------- | -------- | --- | ------ | ---- | ---------------- | --- |
thestandardofknowledge-basedresearch.Toconductamore
cold-startrecommendersystemusercouldneedtoknow.
| impartial | literature | review,    | a   | systematic       | literature | review    |         |        |                |     |               |     |            |
| --------- | ---------- | ---------- | --- | ---------------- | ---------- | --------- | ------- | ------ | -------------- | --- | ------------- | --- | ---------- |
|           |            |            |     |                  |            |           | Step 3: | Define | both exclusion |     | and inclusion |     | standards. |
| entails   | choosing,  | analyzing, |     | and synthesizing |            | important | •       |        |                |     |               |     |            |
scientific papers.The systematicliterature review’sstrategy A series of criteria were used to choose which articles
is presented in this section. The methodology is primarily toreadin-depth.Thesespecificationsareshowninthe
| basedontheguidelinesusedby[29]and[30]. |     |     |     |     |     |     | Table4.   |        |             |     |         |        |           |
| -------------------------------------- | --- | --- | --- | --- | --- | --- | --------- | ------ | ----------- | --- | ------- | ------ | --------- |
|                                        |     |     |     |     |     |     | • Step 4: | Search | for papers. |     | In this | phase, | we search |
A. RESEARCHQUESTIONS
|          |        |      |             |          |     |              | for articles | utilizing |     | the search | keywords |           | that were |
| -------- | ------ | ---- | ----------- | -------- | --- | ------------ | ------------ | --------- | --- | ---------- | -------- | --------- | --------- |
| As noted | above, | with | the growing | research |     | on user cold |              |           |     |            |          |           |           |
|          |        |      |             |          |     |              | developed    | using     | the | research’s | study    | questions | and       |
startrecommendersystems.However,therearefewoverview
keywords(Table3).
researchesinthisarea.Allexistingstudiesarebasedonlyon
• Step5:Articlepre-selection.Theabstractsandtitlesof
classicalsurveysandreviewsofthecurrentstateofresearch.
|            |              |     |            |        |            |         | all the publications |     | that | were | retrieved | in  | the previous |
| ---------- | ------------ | --- | ---------- | ------ | ---------- | ------- | -------------------- | --- | ---- | ---- | --------- | --- | ------------ |
| Therefore, | a systematic |     | literature | review | is needed. | This is |                      |     |      |      |           |     |              |
regardedasthebestmethodtoofferathoroughandobjective phasearetheonlythingsthatarereadinthisstep.These
|          |        |           |           |         |     |              | publications | were  | either | selected      | for | a careful     | reading |
| -------- | ------ | --------- | --------- | ------- | --- | ------------ | ------------ | ----- | ------ | ------------- | --- | ------------- | ------- |
| analysis | of the | published | findings. | Several | of  | the research |              |       |        |               |     |               |         |
|          |        |           |           |         |     |              | or excluded  | based | on     | the standards |     | for inclusion | and     |
questions(Qs)areaskedbythisliteraturereview,asdefined
| inTable2. |     |     |     |     |     |     | exclusion. |            |      |     |          |        |            |
| --------- | --- | --- | --- | --- | --- | --- | ---------- | ---------- | ---- | --- | -------- | ------ | ---------- |
|           |     |     |     |     |     |     | • Step 6:  | Thoroughly | read | the | selected | paper. | This stage |
aimstoconsolidateandanalyzetheliterature.Literature
TABLE2. Researchissuesfororganizedliteraturereview.
|     |     |     |     |     |     |     | that met     | the criteria |                | was screened |           | by reviewing | and           |
| --- | --- | --- | --- | --- | --- | --- | ------------ | ------------ | -------------- | ------------ | --------- | ------------ | ------------- |
|     |     |     |     |     |     |     | searching    | relevant     | literature     |              | using     | quality      | evaluation    |
|     |     |     |     |     |     |     | criteria     | (shown       | in Table       | 5).          | Each      | piece        | of literature |
|     |     |     |     |     |     |     | was examined |              | and thoroughly |              | evaluated | to           | verify that   |
itansweredtheformulatedquestionsposed.
TABLE4. Criteriaforsystematicliteraturereviewinclusionandexclusion.
| To begin      | the  | systematic    |     | literature | review   | study. It is |     |     |     |     |     |     |     |
| ------------- | ---- | ------------- | --- | ---------- | -------- | ------------ | --- | --- | --- | --- | --- | --- | --- |
| first defined | that | the questions |     | shown      | in Table | 2 originate  |     |     |     |     |     |     |     |
fromthefollowingkeywords:(1)recommendationsystemor
recommendersystem,(2)usercoldstartorcoldstartuser,and
(3)coldstart.ExamplesofsuchstringsaregiveninTable3.
B. SYSTEMATICLITERATUREREVIEWFLOW
| The process | of  | completing | this | systematic | literature | review |     |     |     |     |     |     |     |
| ----------- | --- | ---------- | ---- | ---------- | ---------- | ------ | --- | --- | --- | --- | --- | --- | --- |
includessevensteps,asshowninFig.1.
|     |     |     |     |     |     |     | • Step 7: Classification.These |     |     |     | papers | are thenassessed. |     |
| --- | --- | --- | --- | --- | --- | --- | ------------------------------ | --- | --- | --- | ------ | ----------------- | --- |
• Step1: Definition researching questions and keywords. Additionally,theyareratedasbeingentirelyirrelevant,
Thestudyquestion(seeTable2)andthesearchkeywords
|                                       |     |     |     |     |     |     | hardly relevant, |     | or extremely |     | relevant | to  | the study     |
| ------------------------------------- | --- | --- | --- | --- | --- | --- | ---------------- | --- | ------------ | --- | -------- | --- | ------------- |
| forthispaperarefinallybothidentified. |     |     |     |     |     |     | issue.           |     |              |     |          |     |               |
| 136960                                |     |     |     |     |     |     |                  |     |              |     |          |     | VOLUME11,2023 |

H.Yuan,A.A.Hernandez:UserColdStartProbleminRecommendationSystems:ASystematicReview
FIGURE1. Thesystematicliteraturereviewflowdiagram.
VOLUME11,2023 136961

H.Yuan,A.A.Hernandez:UserColdStartProbleminRecommendationSystems:ASystematicReview
TABLE5. Qualityassessmentandselection. SIGIR Conference on Research and Development in Infor-
mationRetrieval’’arethenext,with3total.
V. QUALITATIVESYNTHESISOFTHELITERATURE
A. WHATRESEARCHTOPICSAREBEINGADDRESSED
USERCOLDSTARTINRECOMMENDATIONSYSTEM?
Thispaperprovidesanin-depthstudyof45selectedpapers.
An overview of approaches to address the new user issue
is presented. In this research, we primarily categorize these
techniques into two primary groups: data-driven techniques
andmethod-driventechniques.AsshowninTable8.
C. PAPERSEARCH • Data-driventechniques
After identifying the literature database. Searched online These articles offer ideas for approaches inspired by
databases based on search strings. 1480 relevant literatures efficientdatautilizationandtheconnectionbetweenuserand
were searched. The number of literature returned varied as projectattributes.Thenewwaystoresolvetheissuesofcold
eachliteraturedatabaseusedadifferentstrategyinitssearch startareproposedbyusingpersonregiondata,personsocial
engine. community data, person belief information, and individual
Themostrelevantliteraturewasselected.Firstly,byread- cross-domaindata.
ing the title, abstract, and conclusion irrelevant stud- • Approach-driventechniques
ies were removed. In the end, 117 documents were This category of approaches mitigates the cold start
obtained. Then, 117 documents were screened by applying problem by proposing new algorithms or improving old
inclusion/exclusion criteria. Ultimately, 74 literatures were ones. The study further classified them into five categories.
retained.AsshowninFig.2. Deep learning-based approach, Matrix factorization-based
approach,hybridapproach,theimprovementovercollabora-
IV. DESCRIPTIVESTATISTICSOFTHELITERATURE tivefiltering-basedapproach,theimprovementovercontent-
Table6showstheresultsofpaperretrievalandselectionfor basedapproach.
systematicliteraturereview.Thetotalquantityofpublications
discoveredineverydatabasecanbeseeninthistable.
1) DATA-DRIVENTECHNIQUES
• Cross-domaindata
TABLE6. ThequantityofarticlesfoundinFig.1’sphases4through7. Table 9 presents a line-by-line comparison of the main
ideas, Datasets, evaluation indicators, strengths, and weak-
nessesoftheselectedliteratures.
Utilizing user preferences from several domains enables
thecreationofmorethoroughusermodelsandimprovedsug-
gestions.Forinstance,usingcross-domainrecommendations
toaddressthetargetdomain’scoldstartissue.Cross-domain
recommendation mechanisms make or enhance recommen-
dations for the target domain using information garnered
Fig. 3 shows the distribution of completed reading and fromthesourcedomain[43],[44].Numerousscenariosand
evaluation of 45 selected papers in each publication year tasks can be employed for cross-domain recommendation.
(2016-2023),respectivelyatstep6andstep7(inFig.1).The Cross-domain recommendation systems are therefore more
quantityofrelevantliteraturereachedthemaximumin2020, organizedandcomplexthanone-domainrecommendations.
with 11 papers, and there may be an even sharper rise from Cremonesi et al. [43] first proposed the classification
2023.Thisshowsthatthereisanincreaseininterestinfinding of scenarios for cross-domain recommendation, and later
solutionstothecoldstartissuesrelatedtorecommendations. studieslargelyagreedwiththiscategorization.Asillustrated
Becausetheyearhasbarelybegun,theresultsof2023cannot in Fig. 4, they identified four distinct recommendation
beconsideredfinal. scenarios: no overlap, user overlap, item overlap, and
Inthisstudy,45researchpapersfrom35variousmeetings complete overlap. The most common methods for solving
and journals with peer review were selected (see Table 7). problemsinvolveuseranditemoverlapanduseroverlap.
These publications mostly focus on the field of computer Many methods for task classification in cross-domain
science,systemsforinformationandrelatedtopics.Thetwo recommender systems. It can be combined according to
with the highest counts, both with a value of 4, are ‘‘IEEE the cross-domain information. It is divided into two types:
Access’’and‘‘ACMTransactionsonInformationSystems’’. AggregatingknowledgeandLinking/transferringknowledge.
‘‘ACM SIGKDD International Conference on Knowledge TheAggregateKnowledgetaskfirstaggregatesknowledge
DiscoveryandDataMining’’and‘‘43rdInternationalACM from different source domains into the target domain. Then
136962 VOLUME11,2023

H.Yuan,A.A.Hernandez:UserColdStartProbleminRecommendationSystems:ASystematicReview
FIGURE2. Thepaperselectionprocess.
FIGURE3. Thenumberofpapersperyear.
recommendationsaremade.AsshowninFig.5.Forexample, Jin et al. [45] proposed a cross-domain recommendation
fusing user preferences from different source domains not algorithm, called RACRec. RACRec solves the problem
only allows cross-system research but also solves the user of predicting full new users in recommendation. RACRec
cold-startproblem. is a cross-domain recommendation algorithm that uses a
The establishment or transference of information among reviewselectionstrategytodynamicallychooseappropriate
domainsinsupportofrecommendationsisreferredtoaslink- cross-domainmethodsforeachuser.
ing and transferring knowledge (shown in Fig. 6). Because Wangetal.[46]employauxiliarydatafromtheadvertising
they both fall under categories that can be semantically sector to address the issue of user cold start in online
mapped, such as comedies and humor, we can correlate a shopping.Theprocedureexaminestheuser’swebbrowsing
certaincomedymoviewithahumorbook,forinstance. historyontheadvertisingplatformandgeneratesrecommen-
The literature is displayed in Table 10 according to dationsfromit.
the categories of Gathering information and Transferring Zhaoetal.[47]proposedamethodcalledCATN,arecom-
information. mendation method to address user cold start problems. The
VOLUME11,2023 136963

H.Yuan,A.A.Hernandez:UserColdStartProbleminRecommendationSystems:ASystematicReview
TABLE7. Distributionofselectedpapersforjournalsandconferences.
FIGURE5. Aggregatingknowledge.
FIGURE4. Thescenarioswhereusersetanditemsetdataoverlap.
|     |     |     |     |     |     | In Table | 11, a line-by-line | comparison | of  | the main | ideas, |
| --- | --- | --- | --- | --- | --- | -------- | ------------------ | ---------- | --- | -------- | ------ |
CATNextractsfeaturesfromreviewdocuments.Itenhances
Datasets,evaluationindicators,strengths,andweaknessesof
| the user | representation | by  | using auxiliary |     | comments from |     |     |     |     |     |     |
| -------- | -------------- | --- | --------------- | --- | ------------- | --- | --- | --- | --- | --- | --- |
theselectedliteraturesispresented.
similarusers. The unprecedented growth of various social networking
Across-domainrecommendationmodelentirelybasedon
|             |               |            |           |     |              | platforms       | has greatly enriched | the | daily        | lives of    | users. |
| ----------- | ------------- | ---------- | --------- | --- | ------------ | --------------- | -------------------- | --- | ------------ | ----------- | ------ |
| the partial | least squares | regression | technique |     | was proposed |                 |                      |     |              |             |        |
|             |               |            |           |     |              | Social networks | are a source         | of  | information. | In addition |        |
byLietal.[48].Thelatentpropertiesofusersinthesource
|            |             |               |                |     |               | to determining | the impact        | of a user    | on other | users.      | It also |
| ---------- | ----------- | ------------- | -------------- | --- | ------------- | -------------- | ----------------- | ------------ | -------- | ----------- | ------- |
| domain     | and users   | in the target | domain         | can | be accurately |                |                   |              |          |             |         |
|            |             |               |                |     |               | provides       | valuable data     | to determine | user     | preferences | for     |
| correlated | using these | models        | by researching |     | a matrix of   |                |                   |              |          |             |         |
|            |             |               |                |     |               | items. All     | of this knowledge | can be       | very     | helpful in  | making  |
regressioncoefficients.Eventargetdomainusers’coldstart
|     |     |     |     |     |     | more accurate | and objective | product | recommendations |     | to  |
| --- | --- | --- | --- | --- | --- | ------------- | ------------- | ------- | --------------- | --- | --- |
issuescanbesolvedbythemodel.
users,whichwillsignificantlyhelptosolvetheusercoldstart
• Socialnetworkdata issue. Utilizing information from social networks, there are
| 136964 |     |     |     |     |     |     |     |     |     | VOLUME11,2023 |     |
| ------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------- | --- |

H.Yuan,A.A.Hernandez:UserColdStartProbleminRecommendationSystems:ASystematicReview
TABLE8. Classificationofapproachesforalleviatingtheusercoldstartprobleminrecommendersystems.
TABLE9. ReviewingandcomparingCross-domaindataapproach.
VOLUME11,2023 136965

H.Yuan,A.A.Hernandez:UserColdStartProbleminRecommendationSystems:ASystematicReview
|     |     |     |     | steps, which | are computed | independently |     | for | each group | of  |
| --- | --- | --- | --- | ------------ | ------------ | ------------- | --- | --- | ---------- | --- |
neighbors.
|     |     |     |     | Li et al. | [52] gathered | user | information | for | the new | user |
| --- | --- | --- | --- | --------- | ------------- | ---- | ----------- | --- | ------- | ---- |
issuebyexaminingtheirsocialnetworkinformation.Learn-
|     |     |     |     | ing from      | side data (such | as    | consumer | social | interactions, |     |
| --- | --- | --- | --- | ------------- | --------------- | ----- | -------- | ------ | ------------- | --- |
|     |     |     |     | human traits, | etc.). Once     | it is | done,    | teach  | new users     | the |
information.Thismethodhelpstomitigatetheissuewithcold
starts.
|     |     |     |     | A latent | feature representation |     | and | social | network | data |
| --- | --- | --- | --- | -------- | ---------------------- | --- | --- | ------ | ------- | ---- |
frequentlyshowupasattributemappinginattributemapping
methods.
|     |     |     |     | Predict | whether cold-start |     | users will | become | important |     |
| --- | --- | --- | --- | ------- | ------------------ | --- | ---------- | ------ | --------- | --- |
FIGURE6. Thelinkingandtransferringknowledge.
|     |     |     |     | users on | the growing    | online | social | network | (Medium) |        |
| --- | --- | --- | --- | -------- | -------------- | ------ | ------ | ------- | -------- | ------ |
|     |     |     |     | by using | user data from | the    | most   | popular | online   | social |
TABLE10. Classificationofliteraturesoncrossdomain.
|     |     |     |     | network       | (Twitter) [53]. | To transfer | descriptive |          | information |     |
| --- | --- | --- | --- | ------------- | --------------- | ----------- | ----------- | -------- | ----------- | --- |
|     |     |     |     | and knowledge | of dynamic      | actions     | to          | the most | influential |     |
onlinesocialnetworks,theyusedasupervised-basedmachine
learningapproach.
AuniquemodelofLoCoisputoutbySedhainetal.[31].
twogroupsofstrategiesforreducingtheusercoldstartissue. Through stochastic SVD, it directly and effectively learns a
Thefirstgroupincludesfeaturemappingmodels[53]andthe
low-ranklinearmodel.Incomparisontostate-of-the-artuser
second,similarity-basedmodels[50],[51],[52]. coldstartadvice,theresultsvalidatedinthisstudyonfourreal
It’seasytousethesimilarity-basedmodel.Theirequation
datasetsdemonstrateconsiderableimprovementsinLoCo.
canbewrittenas
|     |     | Y =WY . | (1) |                              |     |     |     |     |     |     |
| --- | --- | ------- | --- | ---------------------------- | --- | --- | --- | --- | --- | --- |
|     |     | s t     |     | 2) APPROACH-DRIVENTECHNIQUES |     |     |     |     |     |     |
• Meta-learning
| where W | is the similarity | matrix. In general, | W is the |     |     |     |     |     |     |     |
| ------- | ----------------- | ------------------- | -------- | --- | --- | --- | --- | --- | --- | --- |
similarity between the relation source domain Y s and the In Table 12, a line-by-line comparison of the main ideas,
targetdomainY . Datasets,evaluationindicators,strengths,andweaknessesof
t
A cold-start recommender system based on linked open theselectedliteraturesispresented.
dataandsocialnetworkelementshasbeenproposedfornew A current trend in machine learning is called meta-
users [50]. This technique uses the user profile generator learning. It enables quick adaptation to new tasks using
module to automatically create a user’s profile when they a limited set of examples. One might consider of the
first log in using their Facebook ID and, if applicable, their new user suggestion challenge as a learning problem from
DBpedia ID. After that, ‘‘user clusters’’ are created using a limited number of samples. Because of this, the user
the user’s profile information and class labels to train a cold start problem can be solved extremely well using the
classifier.Aclassifieristhenfedthedatafromthenewuser meta-learning approach. Plenty of researchers are currently
to make a prediction about which category the new user employingmeta-learningtosolvethenewuserissue.[54]
belongsto.Thesystemwillonlyreviewtheuserratingsgiven Three categories of meta-learning exist: metrics-based,
to each ‘‘program’’ by members of the ‘‘group’’ to which model-based, and optimisation-based. [55] The following
the new user belongs once that group has been identified. Table.13categorizesthemeta-learningtechniquesaddressed
Finally,theaverageweightoftheratingsgivenbytheusers tothenewuserissue.
in the predicted cluster to each Item cluster was calculated, The goal of metrics-based meta-learning is to identify
andtheItemclusterwiththehighestratingwasrecommended patterns among samples within a task. Jiang et al. [56]
tothenewuser. suggest using user clustering to group individuals with
Reshmaetal.[51]alleviatethecoldstartproblembyusing similar interests based on their shared knowledge. The
user social behavior. The customer rating matrix is used in transformation network is built using the user’s clustering
the suggested method to determine the nearest neighbors data, and it transforms the global initialization parameters
first. The properties of social network data are analyzed in gained by meta-learning into the cluster’s ideal starting
thesubsequentstagetodeterminetheattributecomparability parameters. It can lessen the detrimental impacts of users
betweeneveryotheruserandthosewhoareactive.Inthethird with various tastes and enhance the meta-learning model’s
| stage,agroupofneighborsareselectedfromthenetworkof |     |     |     | functioning. |     |     |     |     |     |     |
| -------------------------------------------------- | --- | --- | --- | ------------ | --- | --- | --- | --- | --- | --- |
friends,andthesocialsimilarityisdeterminedasaweighted Model-based meta-learning updates parameters quickly
sum of these values. The final planned rating of the item is throughseveraltrainingsteps.Usingmemoryenhancedmeta
thencalculatedbyaddingtheweightedtotaloftheforecasted optimization (MAMO), Dong et al. [58] suggested a cold
ratings for each set of neighbors obtained in the first two beginning strategy. A feature-specific memory is meant to
| 136966 |     |     |     |     |     |     |     |     | VOLUME11,2023 |     |
| ------ | --- | --- | --- | --- | --- | --- | --- | --- | ------------- | --- |

H.Yuan,A.A.Hernandez:UserColdStartProbleminRecommendationSystems:ASystematicReview
TABLE11. ReviewingandcomparingSocialnetworkdataapproach.
provide individual deviation items while configuring the Briandetal.[32]usedeepneuralnetworkarchitectureand
model’s parameters. Comprehensive tests on two regularly user clustering from heterogeneous information sources to
used data sets show that MAMO outperforms cutting-edge solve the new user issue. A brand-new service recommen-
solutions. dationtechniqueformultiplexinteraction,knownasMISR,
Optimization-based meta-learning aims to adjust the was proposed by Ma et al. [16]. This strategy functions by
optimization algorithm so that the model can learn well incorporating three different kinds of service and mashup
fromasmallnumberofexamples.Thenovelusersequence interactions within DNN. A deep neural network-based
recommender framework known as metaCSR based on DeCS framework is suggested by Mondal et al. [33]. The
meta-learning was proposed by Huang et al. [55]. When collaborative filtering recommendation’s new user issue
learningeffectiveinitializationfornewusers,theframework is solved using this technique. The suggested framework,
employsModel-AgnosticMeta-Learning(MAML)toextract DeCS, may be applied to various data sets and aids in
and spread transferable information from previous users. systemperformanceimprovement.Kumaretal.[34]provide
MetaCSR has demonstrated high performance in learning a video recommendation system that overcomes the cold
typical patterns from regular users through experiments. start problem and makes use of intrinsic information to
Shen et al. [61] proposed the RESUS to resolve the cold suggest films. The deep neural network of the architecture
user CTR prediction problem through meta-learning. The isfedwiththeoutputoftheC3Dmodel,mainlyvideo-level
method may quickly learn from a narrow range of user- characteristics.
specific interactions, and the learning can be applied to Chen et al. [35] proposes an end-to-end recommendation
deduceindividualpreferences.Themethodisexperimentally system ColdGAN based on the Generative Adversarial
confirmedtoimprovethepredictabilityofclick-throughrates Network,whichcangenerateaccuratedataunderimprecise
forchillyusers. data. ColdGAN is simple and effective in restoring lost
functionsofrelateditemsandeffectivelysolvestheproblem
• DeepLearning
ofnewusers.
Table 14 presents a line-by-line comparison of the Haoetal.[36]proposedamulti-policyapproachfornew
main ideas, Datasets, evaluation indicators, strengths, and userrecommendation(MPT).Themodelusesuseranditem
weaknessesoftheselectedliteratures. dependencies obtained by a GNN encoder and introduces
Thedeeplearningalgorithmisaparticularkindofneural a Transformer encoder to obtain long-term dependencies.
network-based machine learning algorithm. It learns and Abrand-newinductiveheterogeneousgraphneuralnetwork
classifiesinputdatausingamulti-layerneuralnetwork.Deep (IHGNN) model is put out by Cai et al. [37]. To address
learning techniques including Autoencoder, Graph Neural the sparsity of user features issue, the model makes use
Networks,GenerativeAdversarialNetworks,andothershave of relational information from the new user recommenda-
beenusedinrecommendationalgorithms. tion system. Hao et al. [38] presented a recommendation
VOLUME11,2023 136967

H.Yuan,A.A.Hernandez:UserColdStartProbleminRecommendationSystems:ASystematicReview
TABLE12. ReviewingandcomparingMeta-learningapproach.
136968 VOLUME11,2023

H.Yuan,A.A.Hernandez:UserColdStartProbleminRecommendationSystems:ASystematicReview
TABLE13. Themeta-learningmethodsusedtosolvetheuser-coldstart recommendation.Thefundamentalgoalistocreatefictitious
problem. yet believable people and things. The rating matrix is then
|     |     |     |     |     |     |     |     | expanded | using | them as | extra | rows | (users) | and columns |     |
| --- | --- | --- | --- | --- | --- | --- | --- | -------- | ----- | ------- | ----- | ---- | ------- | ----------- | --- |
(things).
Duricicetal.[75]exploretheuseofKatzsimilarity(KS)
inacollaborativefiltering(CF)algorithmforcoldstartusers.
Thisistherule-equivalentsimilaritymeasureinthenetwork
method based on the GNN model. The model enhances forselectingtheknearestneighbors.
the aggregation capability of graph convolution based on a Chao et al. [76] proposes an innovative way to solve
self-focused meta-aggregator. The method can after better challengesfacedbynewusersbyusingleaderrecommenda-
mitigatethenewuserproblem.Anewframedattributegraph tions.TheCollaborativeFilteringtechniquechoosespotential
neuralnetwork(AGNN)isdevelopedusingattributegraphs. leaders based on previous user ratings. These potential
Qian et al. [39] AGNN can generate strictly cold user/item leaders have multiple ratings and have excellent historical
preference embeddings by learning attribute distributions data fit. As a result, they may be relied upon to suggest
withanextendedvariationalself-encoder(eVAE)structure. productstonewconsumers.
|     |     |     |     |     |     |     |     | Al-Bakri | Hassan | [77] | proposed | a collaborative |     | filtering |     |
| --- | --- | --- | --- | --- | --- | --- | --- | -------- | ------ | ---- | -------- | --------------- | --- | --------- | --- |
• MatrixFactorization
|       |             |     |                |     |            |     |        | model for | user | authenticity | information |     | based | on  | fuzzy |
| ----- | ----------- | --- | -------------- | --- | ---------- | --- | ------ | --------- | ---- | ------------ | ----------- | --- | ----- | --- | ----- |
| Table | 15 presents |     | a line-by-line |     | comparison |     | of the |           |      |              |             |     |       |     |       |
c-meanclustering.Themethodmakesuseofanewmeasure
| main ideas, | Datasets, |     | evaluation | indicators, |     | strengths, | and |          |             |      |             |     |              |     |     |
| ----------- | --------- | --- | ---------- | ----------- | --- | ---------- | --- | -------- | ----------- | ---- | ----------- | --- | ------------ | --- | --- |
|             |           |     |            |             |     |            |     | formula. | The formula | uses | combination |     | coefficients |     | to  |
weaknessesoftheselectedliteratures.
combineuserevaluationwithfuzzyauthenticityinformation.
| Zhou       | et al. [68] | proposed |           | a matrix | decomposition |             | rec-     |               |         |                |           |                 |            |            |        |
| ---------- | ----------- | -------- | --------- | -------- | ------------- | ----------- | -------- | ------------- | ------- | -------------- | --------- | --------------- | ---------- | ---------- | ------ |
|            |             |          |           |          |               |             |          | Zahid         | et al.  | [78] presented |           | standardization |            | techniques |        |
| ommender   | system      | method   | based     | only     | on            | homomorphic |          |               |         |                |           |                 |            |            |        |
|            |             |          |           |          |               |             |          | combined      | with    | systematic     | filtering | methods         |            | and        | Matrix |
| encryption | and         | social   | networks. | The      | method        | introduces  | the      |               |         |                |           |                 |            |            |        |
|            |             |          |           |          |               |             |          | factorization | methods | to solve       | the       | new             | user issue | in recom-  |        |
| preference | information |          | of users  | similar  | to            | new         | users as |               |         |                |           |                 |            |            |        |
mendation,consideringvariablesthatarenotdirectlyrelated
featuresintherecommendersystem.Thenewuserproblem
|           |      |              |     |           |     |       |        | to user | profiles | but are | meaningful | enough |     | to ultimately |     |
| --------- | ---- | ------------ | --- | --------- | --- | ----- | ------ | ------- | -------- | ------- | ---------- | ------ | --- | ------------- | --- |
| is solved | with | this method. |     | Natarajan | et  | al. A | Matrix |         |          |         |            |        |     |               |     |
recommendtousers.
| Factorization | Model       | (CD-SemMF) |              | based | on    | cross-domain |      |     |     |     |     |     |     |     |     |
| ------------- | ----------- | ---------- | ------------ | ----- | ----- | ------------ | ---- | --- | --- | --- | --- | --- | --- | --- | --- |
| semantic      | association |            | is presented | to    | solve | the new      | user |     |     |     |     |     |     |     |     |
• NewImprovedContent-basedApproach
| issue in      | collaborative |        | filtering | recommendations |            | employing    |         |             |             |            |              |             |            |            |        |
| ------------- | ------------- | ------ | --------- | --------------- | ---------- | ------------ | ------- | ----------- | ----------- | ---------- | ------------ | ----------- | ---------- | ---------- | ------ |
| Linked        | Open Data     | (LOD). | Lin       | et al.          | [70]       | A MetaMatrix |         |             |             |            |              |             |            |            |        |
|               |               |        |           |                 |            |              |         | Table       | 17 presents | a          | line-by-line |             | comparison |            | of the |
| Factorization | (MetaMF)      |        | model     | is proposed     |            | that is      | capable |             |             |            |              |             |            |            |        |
|               |               |        |           |                 |            |              |         | main ideas, | Datasets,   | evaluation |              | indicators, |            | strengths, | and    |
| of generating | private       | item   | embedding |                 | and rating | prediction   |         |             |             |            |              |             |            |            |        |
weaknessesoftheselectedliteratures.
| models | using meta-networks. |     |     | Chen | et al. | [71] find | that |     |     |     |     |     |     |     |     |
| ------ | -------------------- | --- | --- | ---- | ------ | --------- | ---- | --- | --- | --- | --- | --- | --- | --- | --- |
Content-basedrecommendationalgorithmisanalgorithm
| combining | regularization |     | differentiating |     | functions |     | with a |                 |     |         |       |           |     |        |         |
| --------- | -------------- | --- | --------------- | --- | --------- | --- | ------ | --------------- | --- | ------- | ----- | --------- | --- | ------ | ------- |
|           |                |     |                 |     |           |     |        | that recommends |     | similar | items | according | to  | users’ | histor- |
matrixfactorization-basedapproachcanbetterpredictusers’
|     |     |     |     |     |     |     |     | ical behavior | and | item | attributes. | The | core | idea of | this |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------- | --- | ---- | ----------- | --- | ---- | ------- | ---- |
preferencesforitemstoaddressthenewuserissue.
|          |     |     |          |       |     |               |     | algorithm     | is to | use the characteristics |         |     | of the     | object    | itself |
| -------- | --- | --- | -------- | ----- | --- | ------------- | --- | ------------- | ----- | ----------------------- | ------- | --- | ---------- | --------- | ------ |
| Improved |     | New | Approach | Based | on  | Collaborative |     |               |       |                         |         |     |            |           |        |
| •        |     |     |          |       |     |               |     | to recommend, |       | rather than             | relying | on  | the user’s | behavior. |        |
Filtering
|     |     |     |     |     |     |     |     | The benefit | of  | a content-based |     | recommendation |     | algorithm |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------- | --- | --------------- | --- | -------------- | --- | --------- | --- |
Table 16 presents a line-by-line comparison of the is that it can deal with different types and fields of
main ideas, Datasets, evaluation indicators, strengths, and items, and does not need the user’s personal information
weaknessesoftheselectedliteratures. and behavioral data. The drawback is that it is unable to
When used directly, collaborative filtering algorithms account for users’ shifting interests and preferences, so the
cannot effectively address the user cold start issue. Many recommendationmaybeinaccurateinsomecases.Content-
researchers are working to develop a collaborative filtering basedrecommendationalgorithmssufferfromusercold-start
algorithmtoaddresstheuser’scoldstartissueCollaborative problems, and currently, many scholars have improved
filtering algorithms cannot effectively solve the new user content-based recommendation algorithms to alleviate new
issue when used directly. Many researchers are working userproblems.
to develop collaborative filtering algorithms to solve the Afrequentlyoccurringpatternminingframework(FPRS)
new user issue [72]. To deal with the limited data of forrecommendersystemsispresentedbyKannoutetal.[40].
user characteristics, Z. Zhang et al. [73] propose a novel To alleviate the cold-start issue for new users and new
inductive heterogeneous graph neural network (IHGNN) items, FPRS combines the created frequent item sets
architecturethatutilizestherelationaldatafromthenewuser with a content-based strategy. The method’s efficacy is
recommendationsystem. confirmed by empirical study. The term frequency-inverse
A new CF framework called Augmented Reality CF document frequency (TF-IDF) text mining technique was
was proposed by Chae et al. [74]. It effectively addresses used by Chia et al. [41] for data filtering and information
| the new       | issue | and raises | the | overall | effectiveness |     | of the | retrieval. |     |     |     |     |     |     |        |
| ------------- | ----- | ---------- | --- | ------- | ------------- | --- | ------ | ---------- | --- | --- | --- | --- | --- | --- | ------ |
| VOLUME11,2023 |       |            |     |         |               |     |        |            |     |     |     |     |     |     | 136969 |

H.Yuan,A.A.Hernandez:UserColdStartProbleminRecommendationSystems:ASystematicReview
TABLE14. ReviewingandcomparingDeepLearningapproach.
Tosolvetheseissues,asystemcalledCold-Transformeris Ranking Metrics is the value obtained in the recommen-
proposedbyLietal.[42].Context-basedadaptiveembedding dation for a given user U and a test set S, after calculating
is created by Cold-Transformer to account for variations in the ranking of all possible recommendation results for S by
feature distribution. To convey the related user preferences, thatuserU.IfarecommendationsystemhasahigherTop-K
it changes the embed of a new user into a hot state that is accuracy,itmeansthatitcanbetterpredictandranktheitems
moresimilartoanexistinguser. of interest to the user. top-K accuracy is mainly ndcg@K,
Hit@K,etc.
B. WHATMETRICSAREEMPLOYEDTOASSESSTHE Multiple types of evaluation metrics are used in most of
EFFECTIVENESSOFUSERCOLDSTART? the literature to evaluate models. Rating prediction metrics
An overly performant recommender system is the ultimate (MSE and RMSE) and Ranking Metrics (ndcg@K) were
goal of recommender system design. How should the used in the paper [56]. The literature [49] used AUC and
effectivenessofaparticularrecommendersystembeassessed NDCG@K.Huangetal.[55]usedAUC,MAP,Hit@Kand
toaddresstheusercold-startissue?Threecommonlyutilized NDCG@N.MAE,NDCG@KandDCG@Kwereusedinthe
metrics - ranking measures, classification accuracy metrics, literature [58] and [62]. NDCG@k, Recall@k, Prision@k,
and rating prediction metrics - are categorized. Table 18 andAUCwereusedintheliterature[37].
displaysthedistributionofthestudiedstudiesregardingthe Someliteratureusesonlyonetypeofevaluationmetricin
predictionmetrics. theperformanceevaluationprocess.Asintheliterature[42]
Mean Square Error (MSE), Root Mean Square Error and [53] the AUC was used to evaluate the model.
(RMSE), and Mean Absolute Error (MAE) are the three In the literature [59] used NDCG@N for evaluation model.
main rating prediction metrics. As the value of the measure Intheliterature[76]usedRMSEforevaluation.Mostofthis
falls, the precision rises. Area under the curve (AUC) and literature uses Ranking Metrics for model evaluation [39],
recall,precision,f1score,andrecallareoftenusedevaluation [59], [69], [71]. As in the literature [36] and [38], only
measuresfortheclassificationaccuracymetric. Recall@KandNDCG@Kwereused.
136970 VOLUME11,2023

H.Yuan,A.A.Hernandez:UserColdStartProbleminRecommendationSystems:ASystematicReview
TABLE15. ReviewingandcomparingMatrixFactorizationapproach.
TABLE16. Reviewingandcomparingimprovednewapproachbasedoncollaborativefiltering.
VI. DISCUSSIONANDDIRECTIONSFORFUTURE withnewusersisthatwhentheystarttoshowupthroughout
RESEARCH therecommendationprocess,betterrecommendationscannot
A. DISCUSSION beproducedduetoalackofuser-specificdata.
Thecoldstartissueisonekeyissuethataffectstheaccuracy This literature review divides the approaches to solving
andprecisionofrecommendations.Withthecoldstartissues, user cold starts into two groups. Data-driven and method-
therearenewuserissuesandnewitemissues.Theproblem driven.ShowasFig.7.
VOLUME11,2023 136971

H.Yuan,A.A.Hernandez:UserColdStartProbleminRecommendationSystems:ASystematicReview
TABLE17. Reviewingandcomparingnewimprovedcontent-basedapproach.
TABLE18. Distributionofstudiesrelatedtoevaluationmetricsforuser This study’s primary finding is very beneficial to
coldstartproblems.
|     |     |     |     |     | cross-domain | and | social | network | data | to address | user | cold |
| --- | --- | --- | --- | --- | ------------ | --- | ------ | ------- | ---- | ---------- | ---- | ---- |
startdifficulties.Aspartoftheselectionorfilteringprocess,
|     |     |     |     |     | researchers   | frequently  | analyze      |                | data or  | inferences     | using    | pre-     |
| --- | --- | --- | --- | --- | ------------- | ----------- | ------------ | -------------- | -------- | -------------- | -------- | -------- |
|     |     |     |     |     | established   | standards.  | This         | is because     |          | it’s possible  |          | that the |
|     |     |     |     |     | additional    | data,       | which        | mainly         | consists | of assumptions |          | and      |
|     |     |     |     |     | information   | from        | questionable |                | sources, | isn’t          | accurate | and      |
|     |     |     |     |     | trustworthy.  | Researchers |              | have chosen    |          | and sorted     | these    | facts    |
|     |     |     |     |     | in this order | based       | on their     | dependability. |          | The            | study    | found    |
thatmachinelearninganddeeplearningtechniquesarebeing
usedmoreofteninarangeofacademicfields.DNN,GNN,
|     |     |     |     |     | and other | techniques  | are | being      | used by | more   | researchers | to  |
| --- | --- | --- | --- | --- | --------- | ----------- | --- | ---------- | ------- | ------ | ----------- | --- |
|     |     |     |     |     | alleviate | the problem | of  | new users, | as      | can be | observed    | in  |
Fig.8.
|             |                 |                |             |     | In recommender |              | systems,   |         | the use | of           | deep   | learning |
| ----------- | --------------- | -------------- | ----------- | --- | -------------- | ------------ | ---------- | ------- | ------- | ------------ | ------ | -------- |
|             |                 |                |             |     | or machine     | learning     | techniques |         | can     | successfully |        | capture  |
| Data-driven | mainly utilizes | different user | information | to  |                |              |            |         |         |              |        |          |
|             |                 |                |             |     | non-linear     | correlations |            | between | users   | and          | items. | Deep     |
solve the new user issue. Such as user social network data, learning can handle intricate and sophisticated interactions
userdemographicdata,etc.Theadvantageofthesemethods in knowledge gathered from a variety of sources (like
canbettersolvetheproblemsthatnewusershavenohistorical
|     |     |     |     |     | text embeddings, |     | context | embeddings, |     | and | visual | embed- |
| --- | --- | --- | --- | --- | ---------------- | --- | ------- | ----------- | --- | --- | ------ | ------ |
behavior data by using user-related data (such as social dings), as well as the encoding of complex conceptions as
network data). It can better alleviate the user cold start higher-level information presentations. To solve user cold
problem.However,thesemethodshavesomeproblemssuch
|     |     |     |     |     | start difficulties, |     | additional | research | using | deep | learning | or  |
| --- | --- | --- | --- | --- | ------------------- | --- | ---------- | -------- | ----- | ---- | -------- | --- |
asthedifficultyofmulti-domainuserfeaturefusion,userdata machine learning methods is required. The new user issue
privacyanduserdataacquisition.
|     |     |     |     |     | is being | addressed | in research | on  | deep | learning | algorithms. |     |
| --- | --- | --- | --- | --- | -------- | --------- | ----------- | --- | ---- | -------- | ----------- | --- |
Method-driven solves the problem by applying different Graph neural networks or the Attention mechanism are
algorithmsormodels.Inthispaper,method-drivenissubdi- being used by more and more researchers. View as in
| vided into | five categories. | They are meta-learning |     | methods, |     |     |     |     |     |     |     |     |
| ---------- | ---------------- | ---------------------- | --- | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
Fig.9.
deep learning methods, matrix factorization methods, new The research in this paper found that recommendations
| methods based | on collaborative | filtering, | and new | methods |            |        |           |     |          |            |     |        |
| ------------- | ---------------- | ---------- | ------- | ------- | ---------- | ------ | --------- | --- | -------- | ---------- | --- | ------ |
|               |                  |            |         |         | for films, | music, | and books | are | the most | researched |     | areas. |
for content-based recommender systems. The advantage of Thisisbecausetherearemorepubliclyavailabledatasetsin
these methods is that some rules are used to solve the thesedomains.Recommendationmethodsforshoppingand
| user cold | start problem. | For example, | machine | learning |            |     |         |           |      |            |          |     |
| --------- | -------------- | ------------ | ------- | -------- | ---------- | --- | ------- | --------- | ---- | ---------- | -------- | --- |
|           |                |              |         |          | e-commerce | are | next in | research. | This | is because | shopping |     |
related methods can be recommended to new users through and product review datasets are more readily available.
rapidlearning,andmulti-featurefusioncanbebettersolved.
However,recommendationmethodsinthefieldofeducation
However,suchmethodshavethedefectsofcomplexmodels are less researched yet extremely important. This suggests
andpoorresultsforpurecoldstartproblems. newresearchdirectionsforrecommendersystemsscholars.
| 136972 |     |     |     |     |     |     |     |     |     |     | VOLUME11,2023 |     |
| ------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------- | --- |

H.Yuan,A.A.Hernandez:UserColdStartProbleminRecommendationSystems:ASystematicReview
FIGURE7. Classificationofusercoldstartrecommendationstrategies.
FIGURE8. Timetosolvethenewusers’problem.(Yellowindicatesthenearesttime,andpurpleindicatesthefarthesttime.)
Boththecoldstartproblemandthedatasparsityproblem data sparsity problem focus more on filling in the missing
are related to situations where there is insufficient informa- information by using data that already exists. However,
tion in a recommender system, but they occur at different approaches such as machine learning, meta-learning, and
times, on different scales, and with different solutions. some hybrid approaches can address both the cold-start
Approaches to the cold-start problem typically focus more problemandthedatasparsityproblem.
on obtaining additional information (e.g., user registration Three main types of evaluation metrics are used for
information or item metadata), while approaches to the user cold start model evaluation: Rating prediction metrics,
VOLUME11,2023 136973

H.Yuan,A.A.Hernandez:UserColdStartProbleminRecommendationSystems:ASystematicReview
FIGURE9. Deeplearningalgorithmoverlayvisualization.(Yellowindicatestheclosesttothecurrenttime,andpurple
indicatesthefarthestfromthecurrenttime.)
FIGURE10. Theevaluationmetricsoverlaydiagramintheliteratureabstract.(Yellowindicatestheclosesttothecurrenttime,
andpurpleindicatesthefarthestfromthecurrenttime.)
Classificationaccuracymetrics,andRankingMetrics.Most includes user profile information, social relationships, user
of the literature will choose different types of evaluation behavior, and auxiliary information (e.g., knowledge base
metrics for a comprehensive evaluation. Some papers use and time signals). However, there are great challenges in
one type of evaluation metrics for evaluation. Most of the collecting implicit user data and processing real-time user
literature will adopt the Ranking Metrics type of evaluation feedback data, and it is a challenge to collect and utilize
metrics.Fig.10showstheevaluationmetricsoverlaydiagram additionalinformationeffectively.
in the literature abstract. As can be seen from the figure, • Multi-tasklearning
recentlymoreandmorescholarsareusingNDCGtoanalyze
Deeplearning-basedmethodsaremoreeffectiveinsolving
theperformanceofusercoldstartrecommendationsystems.
theusercoldstartproblemcomparedtosingle-tasklearning.
Utilizing multi-task learning in deep neural networks can
B. DIRECTIONSFORFUTURERESEARCH reduce the problem of having little data at the beginning
In this research review, we survey the state-of-the-art of a new user through implicit data augmentation. Some
literature addressing the user cold-start problem. Despite researchersarelookingtoapplydeeperarchitecturestouser
these advances, there are still many challenges that need to datatoexploreadditionalmultitasklearning.
beaddressed.
• AttentionMechanisms
• Collectingandutilizingadditionalinformation Theattentionmechanismenablesneuralnetworkstofocus
Researchershavefoundthatusingadditionalinformation on a subset of features by selecting specific inputs, helping
about users and items can go a long way toward allevi- to alleviate the user cold-start problem in recommender
ating user cold-start problems. This additional information systems.Thisisamechanismthatcanbeintuitivelyapplied
136974 VOLUME11,2023

H.Yuan,A.A.Hernandez:UserColdStartProbleminRecommendationSystems:ASystematicReview
tomanydeeplearningarchitecturessuchasCNNsandRNNs. [5] Y. Guo, M. Wang, and X. Li, ‘‘Application of an improved Apriori
For example, when applying attention techniques to CNN algorithm in a mobile e-commerce recommendation system,’’ Ind.
|            |        |          |           |     |                     |     |     | Manage. | Data | Syst., vol. | 117, | no. 2, pp.287–303, |     | Mar. | 2017, doi: |
| ---------- | ------ | -------- | --------- | --- | ------------------- | --- | --- | ------- | ---- | ----------- | ---- | ------------------ | --- | ---- | ---------- |
| models, it | can be | utilized | to select | the | most representative |     |     |         |      |             |      |                    |     |      |            |
10.1108/imds-03-2016-0094.
| elements | and filter | out uninformative |     | ones, | while | providing |     |                                                                      |     |           |        |          |         |          |              |
| -------- | ---------- | ----------------- | --- | ----- | ----- | --------- | --- | -------------------------------------------------------------------- | --- | --------- | ------ | -------- | ------- | -------- | ------------ |
|          |            |                   |     |       |       |           |     | [6] D.Mumin,L.-L.Shi,L.Liu,andJ.Panneerselvam,‘‘Data-drivendiffusion |     |           |        |          |         |          |              |
|          |            |                   |     |       |       |           |     | recommendation                                                       |     | in online | social | networks | for the | Internet | of people,’’ |
betterinterpretability.Thus,attentionmodelingisapromis-
|     |     |     |     |     |     |     |     | IEEE Trans. | Syst., | Man, | Cybern., | Syst., | vol. 52, | no. 1, | pp.166–178, |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------- | ------ | ---- | -------- | ------ | -------- | ------ | ----------- |
ingresearchdirection.
Jan.2022,doi:10.1109/TSMC.2020.3015355.
• Harmonizedindicatorsforevaluatingusersatisfaction [7] W.Zhang,F.Liu,D.Xu,andL.Jiang,‘‘Recommendationsysteminsocial
|        |          |         |        |               |     |        |      | networks | with      | topical attention | and     | probabilistic |      | matrix factorization,’’ |      |
| ------ | -------- | ------- | ------ | ------------- | --- | ------ | ---- | -------- | --------- | ----------------- | ------- | ------------- | ---- | ----------------------- | ---- |
| It was | observed | in this | review | that although |     | recent | rec- |          |           |                   |         |               |      |                         |      |
|        |          |         |        |               |     |        |      | PLoS     | ONE, vol. | 14,               | no. 10, | Oct. 2019,    | Art. | no. e0223967,           | doi: |
ommendersystemshaveshowngoodperformance.However, 10.1371/journal.pone.0223967.
|             |        |              |           |     |          |         |     | [8] M. Zhang, | G.  | Wang,            | L. Ren, | J. Li,           | K. Deng, | and            | B. Zhang, |
| ----------- | ------ | ------------ | --------- | --- | -------- | ------- | --- | ------------- | --- | ---------------- | ------- | ---------------- | -------- | -------------- | --------- |
| there is no | single | standardized | criterion |     | that can | be used | to  |               |     |                  |         |                  |          |                |           |
|             |        |              |           |     |          |         |     | ‘‘METoNR:     | A   | meta explanation |         | triplet oriented | news     | recommendation |           |
evaluatetheperformanceofallrecommendersystems.User
model,’’Knowl.-BasedSyst.,vol.238,Feb.2022,Art.no.107922,doi:
satisfactionandpersonalizationplayaveryimportantrolein
10.1016/j.knosys.2021.107922.
the success of such recommender systems. There is a need [9] D.Z.Ulian,J.L.Becker,C.B.Marcolin,andE.Scornavacca,‘‘Exploring
|     |     |     |     |     |     |     |     | the effects | of  | different | clustering | methods | on a | news recommender |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------- | --- | --------- | ---------- | ------- | ---- | ---------------- | --- |
forsomenewstandardizedevaluationcriteriatoevaluatethe
system,’’ExpertSyst.Appl.,vol.183,Nov.2021,Art.no.115341,doi:
levelofusersatisfactioninreal-time.
10.1016/j.eswa.2021.115341.
Protectingusers’privateinformation [10] J.Davidson,B.Liebald,J.Liu,P.Nandy,andT.VanVleet,‘‘TheYouTube
•
videorecommendationsystem,’’inProc.4thACMConf.Recommender
Interaction information and incidental information (e.g., Syst.,Sep.2010,pp.293–296,doi:10.1145/1864708.1864770.
|                  |     |              |     |          |                 |     |     | [11] Z.Chen,S.Ye,X.Chu,H.Xia,H.Zhang,H.Qu,andY.Wu,‘‘Augmenting |     |     |     |     |     |     |     |
| ---------------- | --- | ------------ | --- | -------- | --------------- | --- | --- | -------------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
| social networks) |     | are commonly |     | used for | recommendations |     |     |                                                                |     |     |     |     |     |     |     |
sportsvideoswithVisCommentator,’’IEEETrans.Vis.Comput.Graphics,
insolvingtheusercold-startproblem.However,onemaybe
vol.28,no.1,pp.824–834,Jan.2022,doi:10.1109/TVCG.2021.3114806.
reluctanttoshareitwiththerecommendersystembecausehis
|     |     |     |     |     |     |     |     | [12] M. Schedl, | ‘‘Deep | learning | in  | music | recommendation |     | systems,’’ |
| --- | --- | --- | --- | --- | --- | --- | --- | --------------- | ------ | -------- | --- | ----- | -------------- | --- | ---------- |
privacymaybecompromisedorevenviolatedbyothers.How Frontiers Appl. Math. Statist., vol. 5, p.44, Aug. 2019, doi:
tobetterprotectusers’privateinformationisanopenissue. 10.3389/fams.2019.00044.
|     |     |     |     |     |     |     |     | [13] S.S.Khanal,P.W.C.Prasad,A.Alsadoon,andA.Maag,‘‘Asystematic |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --------------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
review:Machinelearningbasedrecommendationsystemsfore-learning,’’
VII. CONCLUSIONANDLIMITATIONS Educ. Inf. Technol., vol. 25, no. 4, pp.2635–2664, Jul. 2020, doi:
Thefocusofthispaperistoanalyzehowtheusercoldstart 10.1007/s10639-019-10063-9.
|     |     |     |     |     |     |     |     | [14] M.C.Urdaneta-Ponte,A.Mendez-Zorrilla,andI.Oleagordia-Ruiz,‘‘Rec- |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --------------------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
problem has been solved in literature during the last eight ommendation systems for education: Systematic review,’’ Electronics,
years.Thisstudy’sprimarycontributionisacomprehensive vol.10,no.14,p.1611,Jul.2021,doi:10.3390/electronics10141611.
|     |     |     |     |     |     |     |     | [15] I.Uddin,A.S.Imran,K.Muhammad,N.Fayyaz,andM.Sajjad,‘‘Asys- |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | -------------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
analysisof45relatedliterature.Athoroughcategorizationof
tematicmappingreviewonMOOCrecommendersystems,’’IEEEAccess,
solutionsfortheusercoldstartissueisprovided.
vol.9,pp.118379–118405,2021,doi:10.1109/ACCESS.2021.3101039.
| This study | categorizes |     | approaches | to  | addressing | the | new |                                                                    |     |     |     |     |     |     |     |
| ---------- | ----------- | --- | ---------- | --- | ---------- | --- | --- | ------------------------------------------------------------------ | --- | --- | --- | --- | --- | --- | --- |
|            |             |     |            |     |            |     |     | [16] Y.Ma,X.Geng,andJ.Wang,‘‘Adeepneuralnetworkwithmultiplexinter- |     |     |     |     |     |     |     |
userissueintodata-drivenandmethod-drivenstrategies.This actionsforcold-startservicerecommendation,’’IEEETrans.Eng.Manag.,
vol.68,no.1,pp.105–119,Feb.2021,doi:10.1109/TEM.2019.2961376.
studycanprovideacomprehensiveguideforfutureresearch
|     |     |     |     |     |     |     |     | [17] F.Tahmasebi,M.Meghdadi,S.Ahmadian,andK.Valiallahi,‘‘Ahybrid |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
on solving the new user issue. It helps to understand the recommendationsystembasedonprofileexpansiontechniquetoalleviate
directionofresearchandstudiesonnewuserissues. coldstartproblem,’’MultimediaToolsAppl.,vol.80,no.2,pp.2339–2354,
The investigation in this paper is based solely on a Jan.2021,doi:10.1007/s11042-020-09768-8.
|     |     |     |     |     |     |     |     | [18] L. Paleti, | P. R. | Krishna, | and J. | V. R. Murthy, | ‘‘Approaching |     | the cold- |
| --- | --- | --- | --- | --- | --- | --- | --- | --------------- | ----- | -------- | ------ | ------------- | ------------- | --- | --------- |
systematic literature review of 45 articles published in startproblemusingcommunitydetectionbasedalternatingleastsquare
academicconferencesandacademicjournals.Althoughthis factorizationin recommendationsystems,’’Evol.Intell.,vol. 14,no.2,
pp.835–849,Jun.2021,doi:10.1007/s12065-020-00464-y.
| study has  | made     | a great  | endeavor | to strive       | and | collate      | the |                                                                   |     |     |     |     |     |     |     |
| ---------- | -------- | -------- | -------- | --------------- | --- | ------------ | --- | ----------------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
|            |          |          |          |                 |     |              |     | [19] N.T.AlGhifari,B.Sitohang,andG.A.P.Saptawati,‘‘Addressingcold |     |     |     |     |     |     |     |
| strategies | proposed | by quite | a        | few researchers |     | to alleviate |     |                                                                   |     |     |     |     |     |     |     |
startnewuserinrecommendersystembasedonhybridapproach:Areview
the issue with user cold starts. However, no experimental andbibliometricanalysis,’’ITJ.Res.Dev.,vol.6,no.1,pp.1–16,2021.
|            |     |              |     |                 |     |           |     | [20] R.Yu,Y.Gong,X.He,Y.Zhu,Q.Liu,W.Ou,andB.An,‘‘Personalized |     |     |     |     |     |     |     |
| ---------- | --- | ------------ | --- | --------------- | --- | --------- | --- | ------------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
| validation | has | been carried | out | for comparative |     | analysis. |     |                                                               |     |     |     |     |     |     |     |
adaptivemeta-learningforcold-startuserpreferenceprediction,’’inProc.
Inthelaterphaseofthestudy,theauthorswilltypicallyfocus
35thAAAIConf.Artif.Intell.,2021,vol.35,no.12,pp.10772–10780,doi:
| onthisissue. |     |     |     |     |     |     |     | 10.1609/aaai.v35i12.17287.                                      |            |         |     |                  |        |             |      |
| ------------ | --- | --- | --- | --- | --- | --- | --- | --------------------------------------------------------------- | ---------- | ------- | --- | ---------------- | ------ | ----------- | ---- |
|              |     |     |     |     |     |     |     | [21] Y.Zhu,J.Lin,S.He,B.Wang,Z.Guan,H.Liu,andD.Cai,‘‘Addressing |            |         |     |                  |        |             |      |
|              |     |     |     |     |     |     |     | the item                                                        | cold-start | problem | by  | attribute-driven | active | learning,’’ | IEEE |
REFERENCES Trans. Knowl. Data Eng., vol. 32, no. 4, pp.631–644, Apr. 2020, doi:
[1] F. O. Isinkaye, Y. O. Folajimi, and B. A. Ojokoh, ‘‘Recommendation 10.1109/TKDE.2019.2891530.
systems: Principles, methods and evaluation,’’ Egyptian Informat. J., [22] Y.Bi,L.Song,M.Yao,Z.Wu,J.Wang,andJ.Xiao,‘‘Aheterogeneous
vol.16,no.3,pp.261–273,Nov.2015. informationnetworkbasedcrossdomaininsurancerecommendationsys-
temforcoldstartusers,’’inProc.43rdInt.ACMSIGIRConf.Res.Develop.
| [2] H. Ko, | S. Lee, | Y. Park, and | A. Choi, | ‘‘A survey | of  | recommendation |     |     |     |     |     |     |     |     |     |
| ---------- | ------- | ------------ | -------- | ---------- | --- | -------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
systems: Recommendation models, techniques, and application fields,’’ Inf.Retr.,Jul.2020,pp.2211–2220,doi:10.1145/3397271.3401426.
Electronics,vol.11,no.1,p.141,Jan.2022. [23] J. Wei, J. He, K. Chen, Y. Zhou, and Z. Tang, ‘‘Collaborative
[3] K.PatelandH.B.Patel,‘‘Astate-of-the-artsurveyonrecommendation filtering and deep learning based recommendation system for cold
systemandprospectiveextensions,’’Comput.Electron.Agricult.,vol.178, start items,’’ Expert Syst. Appl., vol. 69, pp.29–39, Mar. 2017, doi:
| Nov.2020,Art.no.105779. |     |     |     |     |     |     |     | 10.1016/j.eswa.2016.09.040. |     |     |     |     |     |     |     |
| ----------------------- | --- | --- | --- | --- | --- | --- | --- | --------------------------- | --- | --- | --- | --- | --- | --- | --- |
[4] J.-P. Cabrera-Sánchez, I. Ramos-de-Luna, E. Carvajal-Trujillo, and [24] A.Da’uandN.Salim,‘‘Recommendationsystembasedondeeplearning
Á.F.Villarejo-Ramos,‘‘Onlinerecommendationsystems:Factorsinflu- methods: A systematic review and new directions,’’ Artif. Intell. Rev.,
encing use in e-commerce,’’ Sustainability, vol. 12, no. 21, p.8888, vol. 53, no. 4, pp.2709–2748, Apr. 2020, doi: 10.1007/s10462-019-
| Oct.2020,doi:10.3390/su12218888. |     |     |     |     |     |     |     | 09744-1. |     |     |     |     |     |     |        |
| -------------------------------- | --- | --- | --- | --- | --- | --- | --- | -------- | --- | --- | --- | --- | --- | --- | ------ |
| VOLUME11,2023                    |     |     |     |     |     |     |     |          |     |     |     |     |     |     | 136975 |

H.Yuan,A.A.Hernandez:UserColdStartProbleminRecommendationSystems:ASystematicReview
[25] L. A. G. Camacho and S. N. Alves-Souza, ‘‘Social network data [45] Y. Jin, S. Dong, Y. Cai, and J. Hu, ‘‘RACRec: Review aware
to alleviate cold-start in recommender system: A systematic review,’’ cross-domain recommendation for fully-cold-start user,’’ IEEE
Inf. Process. Manage., vol. 54, no. 4, pp.529–544, Jul. 2018, doi: Access, vol. 8, pp.55032–55041, 2020, doi: 10.1109/ACCESS.2020.
10.1016/j.ipm.2018.03.004. 2982037.
[26] D. K. Panda and S. Ray, ‘‘Approaches and algorithms to mitigate [46] H. Wang, D. Amagata, T. Makeawa, T. Hara, N. Hao, K. Yonekawa,
cold start problems in recommender systems: A systematic literature andM.Kurokawa,‘‘ADNN-basedcross-domainrecommendersystemfor
review,’’J.Intell.Inf.Syst.,vol.59,no.2,pp.341–366,Oct.2022,doi: alleviatingcold-startproblemine-commerce,’’IEEEOpenJ.Ind.Elec-
10.1007/s10844-022-00698-5. tron.Soc.,vol.1,pp.194–206,2020,doi:10.1109/ojies.2020.3012627.
[27] L.H.Son,‘‘Dealingwiththenewusercold-startprobleminrecommender [47] C.Zhao,C.Li,R.Xiao,H.Deng,andA.Sun,‘‘CATN:Cross-domain
systems:Acomparativereview,’’Inf.Syst.,vol.58,pp.87–104,Jun.2016, recommendationforcold-startusersviaaspecttransfernetwork,’’inProc.
doi:10.1016/j.is.2014.10.001. 43rdInt.ACMSIGIRConf.Res.Develop.Inf.Retr.,2020,pp.229–238,
[28] N.A.Abdullah,R.A.Rasheed,M.H.N.M.Nasir,andM.M.Rahman, doi:10.1145/3397271.3401169.
‘‘Eliciting auxiliary information for cold start user recommendation: [48] C.-T.Li,C.-T.Hsu,andM.-K.Shan,‘‘Across-domainrecommendation
A survey,’’ Appl. Sci., vol. 11, no. 20, p.9608, Oct. 2021, doi: mechanismforcold-startusersbasedonpartialleastsquaresregression,’’
10.3390/app11209608. ACMTrans.Intell.Syst.Technol.,vol.9,no.6,pp.1–26,Nov.2018,doi:
[29] B.Kitchenham,‘‘Guidelinesforperformingsystematicliteraturereviews 10.1145/3231601.
insoftwareengineering,’’Univ.Durham,Durham,U.K.,Tech.Rep.EBSE- [49] Y.Zhu,K.Ge,F.Zhuang,R.Xie,D.Xi,X.Zhang,L.Lin,andQ.He,
2007-01,Version2.3,2007. ‘‘Transfer-metaframeworkforcross-domainrecommendationtocold-start
[30] B. Kitchenham, O. P. Brereton, D. Budgen, M. Turner, J. Bailey, and users,’’inProc.44thInt.ACMSIGIRConf.Res.Develop.Inf.Retr.,2021,
S.Linkman, ‘‘Systematic literature reviews in software engineering— pp.1813–1817,doi:10.1145/3404835.3463010.
A systematic literature review,’’ Inf. Softw. Technol., vol. 51, no. 1, [50] U.Yadav,N.Duhan,andK.K.Bhatia,‘‘Dealingwithpurenewusercold-
pp.7–15,Jan.2009,doi:10.1016/j.infsof.2008.09.009. startprobleminrecommendationsystembasedonlinkedopendataand
[31] S. Sedhain, A. Menon, S. Sanner, L. Xie, and D. Braziunas, ‘‘Low- socialnetworkfeatures,’’MobileInf.Syst.,vol.2020,pp.1–20,Jun.2020,
ranklinearcold-startrecommendationfromsocialdata,’’inProc.AAAI doi:10.1155/2020/8912065.
Conf. Artif. Intell., Feb. 2017, vol. 31, no. 1, pp.1502–1508, doi: [51] R.Reshma,G.Ambikesh,andP.S.Thilagam,‘‘Alleviatingdatasparsity
10.1609/aaai.v31i1.10758. and cold start in recommender systems using social behavior,’’ in
[32] L. Briand, G. Salha-Galvan, W. Bendada, M. Morlon, and V. A. Tran, Proc. Int. Conf. Recent Trends Inf. Technol., Apr. 2016, pp.1–8, doi:
‘‘Asemi-personalizedsystemforusercoldstartrecommendationonmusic 10.1109/ICRTIT.2016.7569532.
streamingapps,’’inProc.27thACMSIGKDDConf.Knowl.Discovery
[52] J. Li, K. Lu, Z. Huang, and H. T. Shen, ‘‘On both cold-start and
DataMining,Aug.2021,pp.2601–2609,doi:10.1145/3447548.3467110.
long-tail recommendation with social data,’’ IEEE Trans. Knowl. Data
[33] R.MondalandB.Bhowmik,‘‘DeCS:Adeepneuralnetworkframework
Eng.,vol.33,no.1,pp.194–208,Jan.2021,doi:10.1109/TKDE.2019.
for cold start problem in recommender systems,’’ in Proc. IEEE
2924656.
Region 10 Symp. (TENSYMP), Jul. 2022, pp.1–6, doi: 10.1109/TEN-
[53] Q.Gong,Y.Chen,X.He,Y.Xiao,P.Hui,X.Wang,andX.Fu,‘‘Cross-
SYMP54529.2022.9864409.
site prediction on social influence for cold-start users in online social
[34] Y. Kumar, A. Sharma, A. Khaund, A. Kumar, P. Kumaraguru, and
networks,’’ ACM Trans. Web, vol. 15, no. 2, pp.1–23, May 2021, doi:
R.R.Shah,‘‘IceBreaker:Solvingcoldstartproblemforvideorecommen-
10.1145/3409108.
dationengines,’’inProc.IEEEInt.Symp.Multimedia(ISM),Dec.2019,
[54] Y. Lu, K. Nakamura, and R. Ichise, ‘‘HyperRS: Hypernetwork-based
pp.217–222,doi:10.1109/ISM.2018.000-3.
recommender system for the user cold-start problem,’’ IEEE Access,
[35] C.C.Chen,P.-L.Lai,andC.-Y.Chen,‘‘ColdGAN:Aneffectivecold-
vol.11,pp.5453–5463,2023,doi:10.1109/ACCESS.2023.3236391.
startrecommendationsystemfornewusersbasedongenerativeadversarial
[55] X. Huang, J. Sang, J. Yu, and C. Xu, ‘‘Learning to learn a cold-start
networks,’’ Int. J. Speech Technol., vol. 53, no. 7, pp.8302–8317,
sequentialrecommender,’’ACMTrans.Inf.Syst.,vol.40,no.2,pp.1–25,
Apr.2023,doi:10.1007/s10489-022-04005-1.
Apr.2022,doi:10.1145/3466753.
[36] B.Hao,H.Yin,J.Zhang,C.Li,andH.Chen,‘‘Amulti-strategy-basedpre-
[56] F.Jiang,Q.Xu,W.Li,B.Xiao,andY.Luo,‘‘Theylikecomedy,don’t
trainingmethodforcold-startrecommendation,’’ACMTrans.Inf.Syst.,
you? A cluster-based meta-learning for cold-start recommendation,’’ in
vol.41,no.2,pp.1–24,Apr.2023,doi:10.1145/3544107.
Proc.IEEEInt.Conf.MultimediaExpo(ICME),Jul.2022,pp.1–6,doi:
[37] D. Cai, S. Qian, Q. Fang, J. Hu, and C. Xu, ‘‘User cold-start
10.1109/ICME52920.2022.9859863.
recommendationviainductiveheterogeneousgraphneuralnetwork,’’ACM
[57] G. Wang and X. Wang, ‘‘Cold-start sequential recommendation
Trans.Inf.Syst.,vol.41,no.3,pp.1–27,Jul.2023,doi:10.1145/3560487.
with collaborative boosted meta transitional learning,’’ in Proc.
[38] B.Hao,J.Zhang,H.Yin,C.Li,andH.Chen,‘‘Pre-traininggraphneural
5th Int. Conf. Data Sci. Inf. Technol., Jul. 2022, pp.1–5, doi:
networks for cold-start users and items representation,’’ in Proc. 14th
10.1109/DSIT55514.2022.9943897.
ACMInt.Conf.WebSearchDataMining,Mar.2021,pp.266–273,doi:
[58] M. Dong, F. Yuan, L. Yao, X. Xu, and L. Zhu, ‘‘MAMO: Memory-
10.1145/3437963.3441738.
augmented meta-optimization for cold-start recommendation,’’ in Proc.
[39] T. Qian, Y. Liang, Q. Li, and H. Xiong, ‘‘Attribute graph neu-
ral networks for strict cold start recommendation,’’ IEEE Trans. 26th ACM SIGKDD Int. Conf. Knowl. Discovery Data Mining, 2020,
Knowl. Data Eng., vol. 34, no. 8, pp.3597–3610, Aug. 2022, doi: pp.688–697,doi:10.1145/3394486.3403113.
10.1109/TKDE.2020.3038234. [59] S. Liu, Y. Liu, X. Zhang, C. Xu, J. He, and Y. Qi, ‘‘Improving the
[40] E. Kannout, M. Grodzki, and M. Grzegorowski, ‘‘Utilizing frequent performanceofcold-startrecommendationbyfusionofattentionnetwork
patternminingforsolvingcold-startprobleminrecommendersystems,’’ and meta-learning,’’ Electronics, vol. 12, no. 2, p.376, Jan. 2023, doi:
in Proc. 17th Conf. Comput. Sci. Intell. Syst., 2022, pp.217–226, doi: 10.3390/electronics12020376.
10.15439/2022F86. [60] J. Misztal-Radecka, B. Indurkhya, and A. Smywišski-Pohl, ‘‘Meta-
[41] E. J. Chia and M. K. Najafabadi, ‘‘Solving cold start problem User2Vecmodelforaddressingtheuseranditemcold-startproblemin
for recommendation system using content-based filtering,’’ in Proc. recommender systems,’’ User Model. User-Adapted Interact., vol. 31,
Int. Conf. Comput. Technol. (ICCTech), Feb. 2022, pp.38–42, doi: no.2,pp.261–286,Apr.2021,doi:10.1007/s11257-020-09282-4.
10.1109/ICCTech55650.2022.00015. [61] Y.Shen,L.Zhao,W.Cheng,Z.Zhang,W.Zhou,andL.Kangyi,‘‘RESUS:
[42] P.Li,R.Chen,Q.Liu,J.Xu,andB.Zheng,‘‘Transformcold-startusers Warm-upcoldusersviameta-learningresidualuserpreferencesinCTR
intowarmviafusedbehaviorsinlarge-scalerecommendation,’’inProc. prediction,’’ACMTrans.Inf.Syst.,vol.41,no.3,pp.1–26,Jul.2023,doi:
45thInt.ACMSIGIRConf.Res.Develop.Inf.Retr.,2022,pp.2013–2017, 10.1145/3564283.
doi:10.1145/3477495.3531797. [62] H.Lee,J.Im,S.Jang,H.Cho,andS.Chung,‘‘Melu:Meta-learneduser
[43] P. Cremonesi, A. Tripodi, and R. Turrin, ‘‘Cross-domain recommender preferenceestimatorforcold-startrecommendation,’’inProc.25thACM
systems,’’ in Proc. IEEE 11th Int. Conf. Data Mining Workshops, SIGKDDInt.Conf.Knowl.DiscoveryDataMining,2019,pp.1073–1082,
Dec.2011,pp.496–503,doi:10.1109/ICDMW.2011.57. doi:10.1145/3292500.3330859.
[44] P.Cantador,I.Fernandez-Tobias,S.Berkovsky,andP.Cremonesi,‘‘Cross- [63] X.Lin,J.Wu,C.Zhou,S.Pan,Y.Cao,andB.Wang,‘‘Task-adaptiveneural
domain recommender systems,’’ in Recommender Systems Handbook. processforusercold-startrecommendation,’’inProc.WebConf.,2021,
Boston,MA,USA:Springer,2015,pp.919–959. pp.1306–1316,doi:10.1145/3442381.3449908.
136976 VOLUME11,2023

H.Yuan,A.A.Hernandez:UserColdStartProbleminRecommendationSystems:ASystematicReview
[64] T. Wei, Z. Wu, R. Li, Z. Hu, F. Feng, X. He, Y. Sun, and W. Wang, [82] Y.Bi,L.Song,M.Yao,Z.Wu,J.Wang,andJ.Xiao,‘‘DCDIR:Adeep
‘‘Fastadaptationforcold-startcollaborativefilteringwithmeta-learning,’’ cross-domain recommendation system for cold start users in insurance
inProc.IEEEInt.Conf.DataMining(ICDM),Nov.2020,pp.661–670, domain,’’inProc.43rdInt.ACMSIGIRConf.Res.Develop.Inf.Retr.,
doi:10.1109/ICDM50108.2020.00075. 2020,pp.1661–1664,doi:10.1145/3397271.3401193.
[65] K. P. Neupane, E. Zheng, and Q. Yu, ‘‘MetaEDL: Meta evidential [83] H. Wang, D. Amagata, T. Maekawa, T. Hara, H. Niu, K. Yonekawa,
learning for uncertainty-aware cold-start recommendations,’’ in Proc. and M. Kurokawa, ‘‘Preliminary investigation of alleviating user cold-
IEEEInt.Conf.DataMining(ICDM),Dec.2021,pp.1258–1263,doi: start problem in e-commerce with deep cross-domain recommender
10.1109/ICDM51629.2021.00154. system,’’ in Proc. World Wide Web Conf., 2019, pp.398–403, doi:
[66] H.Bharadhwaj,‘‘Meta-learningforusercold-startrecommendation,’’in 10.1145/3308560.3316596.
Proc. Int. Joint Conf. Neural Netw. (IJCNN), Jul. 2019, pp.1–8, doi: [84] J. Wang, K. Ding, and J. Caverlee, ‘‘Sequential recommendation for
10.1109/IJCNN.2019.8852100. cold-start users with meta transitional learning,’’ in Proc. 44th Int.
[67] H. Wang and Y. Zhao, ‘‘ML2E: Meta-learning embedding ACM SIGIR Conf. Res. Develop. Inf. Retr., 2021, pp.1783–1787, doi:
ensemble for cold-start recommendation,’’ IEEE Access, vol. 8, 10.1145/3404835.3463089.
pp.165757–165768,2020,doi:10.1109/ACCESS.2020.3022796. [85] R. Togashi, M. Otani, and S. Satoh, ‘‘Alleviating cold-start problems
[68] T. Zhou, Y. Zeng, Y. Li, Z. Jiang, Z. Liu, and T. Li, ‘‘Cold- inrecommendationthroughpseudo-labellingoverknowledgegraph,’’in
start recommendation method based on homomorphic encryption,’’ Proc.14thACMInt.Conf.WebSearchDataMining,2021,pp.931–939,
in Proc. Int. Conf. Netw. Netw. Appl., 2021, pp.461–465, doi: doi:10.1145/3437963.3441773.
10.1109/NaNA53684.2021.00086.
[69] S.Natarajan,S.Vairavasundaram,K.Kotecha,V.Indragandhi,S.Palani,
J.R.Saini,andL.Ravi,‘‘CD-SemMF:Cross-domainsemanticrelatedness
basedmatrixfactorizationmodelenabledwithlinkedopendataforuser
cold start issue,’’ IEEE Access, vol. 10, pp.52955–52970, 2022, doi:
10.1109/ACCESS.2022.3175566.
HONGLIYUANreceivedtheBachelorofScience
[70] Y. Lin, P. Ren, Z. Chen, Z. Ren, D. Yu, J. Ma, and X. Cheng, ‘‘Meta
degreeincomputerscienceandtechnologyfrom
matrixfactorizationforfederatedratingpredictions,’’inProc.43rdInt.
Northwest Normal University, Lanzhou, China,
ACMSIGIRConf.Res.Develop.Inf.Retr.,Jul.2020,pp.981–990.
[71] H.-H. Chen and P. Chen, ‘‘Differentiating regularization weights—A in2009,andthemaster’sdegreeincomputerappli-
simplemechanismtoalleviatecoldstartinrecommendersystems,’’ACM cations from Southwest University, Chongqing,
Trans.Knowl.DiscoveryData,vol.13,no.1,pp.1–22,Feb.2019,doi: China,in2013.SheiscurrentlypursuingthePh.D.
10.1145/3285954. degree in computer science with the National
[72] R. Kumar, P. K. Bala, and S. Mukherjee, ‘‘A new neighbourhood UniversityofthePhilippines.
formationapproachforsolvingcold-startuserproblemincollaborative Since2013,shehasbeenanAssociateProfessor
filtering,’’ Int. J. Appl. Manage. Sci., vol. 12, no. 2, p.118, 2020, doi: with the School of Big Data and Artificial
10.1504/ijams.2020.106734. Intelligence, Anhui Xinhua University. She is the author of more than
[73] Z.Zhang,M.Dong,K.Ota,andY.Kudo,‘‘Alleviatingnewusercold- 20papersandoneChineseinventionpatent.Herresearchinterestsinclude
start in user-based collaborative filtering via bipartite network,’’ IEEE bigdata,datamining,andinformationsecurity.
Trans.Computat.SocialSyst.,vol.7,no.3,pp.672–685,Jun.2020,doi:
10.1109/TCSS.2020.2971942.
[74] D.-K.Chae,J.Kim,D.H.Chau,andS.-W.Kim,‘‘AR-CF:Augmenting
virtualusersanditemsincollaborativefilteringforaddressingcold-start
problems,’’inProc.43rdInt.ACMSIGIRConf.Res.Develop.Inf.Retr.,
Jul.2020,pp.1251–1260,doi:10.1145/3397271.3401038.
ALEXANDERA.HERNANDEZ(Member,IEEE)
[75] T.Duricic,D.Kowald,E.Lacic,andE.Lex,‘‘Trust-basedcollaborative
received the bachelor’s and master’s degrees in
filtering: Tackling the cold start problem using regular equivalence,’’
in Proc. 12th ACM Conf. Recommender Syst., 2018, pp.446–450, doi: information technology from the Technological
10.1145/3240323.3240404. Institute of the Philippines, in 2008 and 2011,
[76] X.ChaoandC.Guangcai,‘‘Collaborativefilteringandleaders’advice respectively,andthePh.D.degreeininformation
basedrecommendationsystemforcoldstartusers,’’inProc.6thInt.Conf. technologyfromDeLaSalleUniversity,Manila,
Comput.Artif.Intell.,2020,pp.158–164,doi:10.1145/3404555.3404644. Philippines,in2016.
[77] N. F. Al-Bakri and S. Hassan, ‘‘A proposed model to solve cold start He iscurrently a Professorwith the Graduate
problem using fuzzy user-based clustering,’’ in Proc. 2nd Sci. Conf. Programs, College of Computing and Informa-
Comput.Sci.,Mar.2019,pp.121–125,doi:10.1109/SCCS.2019.8852624. tion Technologies, National University, Manila.
[78] A. Zahid, N. Sharef, and A. Mustapha, ‘‘Normalization-based neigh- He received a Research Fellowship grant from the Singapore National
borhoodmodelforcoldstartprobleminrecommendationsystem,’’Int. AcademyofScience,in2022,toworkondevelopingadigitalplatformfor
Arab J. Inf. Technol., vol. 17, no. 3, pp.422–431, May 2020, doi: olderadultsthatintegratesartificialintelligenceandgames-basedcognitive
10.34028/iajit/17/3/1.
functionscreening.Hehasbeeninvolvedinexternallyfundedprojectsand
[79] L.Hu,L.Cao,J.Cao,Z.Gu,G.Xu,andD.Yang,‘‘Learninginformative
consultancy work in some multinational firms. He has published papers
priorsfromheterogeneousdomainstoimproverecommendationincold-
inreputableinternationaljournalsandconferences.Hisresearchinterests
start user domains,’’ ACM Trans. Inf. Syst., vol. 35, no. 2, pp.1–37,
includetheintersectionsofappliedmachinelearning,informationsystems,
Apr.2017,doi:10.1145/2976737.
andsustainability.
[80] Y.ShaoandY.H.Xie,‘‘Researchoncold-startproblemofcollaborative
Prof. Hernandez is a member of the Association for Information
filteringalgorithm,’’inProc.3rdInt.Conf.BigDataRes.,2019,pp.67–71,
doi:10.1145/3372454.3372470. Systems (AIS) and the Philippines Society of Information Technology
[81] B.Wang,C.Zhang,H.Zhang,X.Lyu,andZ.Tang,‘‘Dualautoencoder Educators,NationalCapitalRegion(PSITE—NCR).Heisactivelyserving
network with swap reconstruction for cold-start recommendation,’’ in in professional communities on the editorial review board of journals in
Proc.29thACMInt.Conf.Inf.Knowl.Manag.,2020,pp.2249–2252,doi: computingandinternationalconferencesadvisoryandtechnicalcommittees.
10.1145/3340531.3412069.
VOLUME11,2023 136977