---
conversion_metadata:
  converted_at: "2026-07-21T13:56:45Z"
  converter_tool: "markitdown"
  converter_version: "0.1.6"
  source_pdf: "Leibiker & Talmon.pdf"
  source_pdf_sha256: "d0e2c7a727c81f07373a0b91a9f5a82d48ec0535191c3f75facf4dba981a0f18"
  page_count: 11
  markdown_char_count: 104390
---

<!-- PAGE-AWARE EXTRACTION (via pdfminer.six) -->

<!-- PAGE 1 -->

A Recommendation System for Participatory Budgeting

Gil Leibiker

Nimrod Talmon

Ben-Gurion University, Israel

ABSTRACT
In participatory budgeting, voters specify their preferences over a
set of projects of different costs and the goal is to select a subset
of these projects that satisfy some total cost upper bound while
taking into account the preferences of the voters. To lower the
cognitive burden on voters, and to increase voter participation in
PB processes, we propose an approach based on a machine learning
techniques as recommendation system and binary classification
that queries voters for partial ballots and estimates their completion.
We develop several concrete algorithms and evaluate them – based
on real-world instances – wrt. their ability to correctly approximate
voter ballots as well as the overall outcome of the process.

KEYWORDS
Computational Social Choice, Attention-Aware Social Choice, Par-
ticipatory Budgeting, Machine Learning, Recommendation System

ACM Reference Format:
Gil Leibiker
Nimrod Talmon, Ben-Gurion University, Israel. 2023. A
Recommendation System for Participatory Budgeting. In Proc. of the 22nd
International Conference on Autonomous Agents and Multiagent Systems
(AAMAS 2023), London, United Kingdom, May 29 – June 2, 2023, IFAAMAS,
11 pages.

1 INTRODUCTION
Social Choice Theory is a branch of economics that studies collec-
tive decision-making processes and the preferences of individual
agents. It aims to determine how a majority can make decisions
based on the preferences of a group, while still respecting each
individual involved. The theory explores various voting systems
and ways to structure voting procedures in order to more accurately
represent the will of the majority. Social Choice Theory is an im-
portant research area as it seeks to understand collective behavior,
and can be applied to numerous fields such as political decision-
making, economic welfare, and game theory. In essence, Social
Choice Theory provides a framework to better understanding how
our decisions impact others, and how we can make decisions that
are both equitable and efficient [5, 13, 17]

Computational social choice is a field of research that combines
computer science, game theory and social choice theory to develop
algorithms for collective decision making. It examines how groups
of people can use computers to make decisions that are fair, effi-
cient and based on inputs from all involved parties. Computational
social choice can be used in a variety of real-world scenarios such
as voting systems, resource allocation, market design and even
communications networks [5].

Proc. of the 22nd International Conference on Autonomous Agents and Multiagent Sys-
tems (AAMAS 2023), A. Ricci, W. Yeoh, N. Agmon, B. An (eds.), May 29 – June 2, 2023,
London, United Kingdom. © 2023 International Foundation for Autonomous Agents
and Multiagent Systems (www.ifaamas.org). All rights reserved.

A sub-field of Computational social choice is Participatory Bud-
geting (PB). PB is a democratic process in which community mem-
bers decide how to spend a portion of a public or private budget.
PB allows members of a community to make their voices heard
regarding funding decisions affecting a range of fields such as edu-
cation, health and environment. It gives them the power to compose
project proposals and to express their preferences over the budget
allocation [1–3, 7]. In our study we concentrate on the most popular
variant of PB, namely approval-based combinatorial PB. That is,
given a set of projects – each with its cost – each voter expresses its
preferences over the projects by selecting a subset of the projects
that she “approves of”, and the result of the process of aggregating
such voter preferences is a subset of the projects whose total cost
does not go over some given budget upper bound [2, 3].

In this research we consider processes of PB and concentrate
on the information overload problem, i.e., the cognitive burden of
voters participating in such processes. Essentially, the information
overload problem appears when too much information interferes
with decision making [11, 20]. To mitigate the information overload
problem we propose several solutions based on techniques from
machine learning and recommendation systems.

Recommendation systems(RS) are a powerful tool in machine
learning, utilizing algorithms to process large datasets and make
personalized predictions for users [14, 20]. By learning user prefer-
ences and usage patterns, RS can provide users with tailored and
relevant recommendations for products, services, or content [11, 20].
For example, a movie RS could suggest films based on past user
ratings, genre preferences, and even social connections. Similarly,
a restaurant RS could suggest eateries based on location, cuisine
type, and price range. Moreover, RS are being applied in many other
areas such as music, books, and shopping, making them an impor-
tant part of machine learning. The information overload problem
is deeply related to the research on RS [4, 20, 24]. It may effect
the decision making of participants in such systems in various
aspects, in particular as users may find it challenging to choose
the most appropriate choices out of the huge amount and variety
of content that the internet offers. The goal of a RS is to support
users in various domains of decision making processes, such as
what items to purchase, which movies to watch, or which books
to read [14, 20, 22]. In particular, the research on RS, being well-
established by now, offers valuable tools for online users to cope
with information overload and help them in making better choices.
In this paper we discuss the problem of information overload in
PB where voters have to consider a large number of projects, leading
to a time-consuming and attention-demanding task [8, 27]. We
propose a solution that involves an application that uses machine
learning and RS to estimate a voter’s preferences for the remaining
projects based on their opinions about a few projects. This approach
could save voters time and allow them to express better preferences
for the proposals they do consider. The paper highlights the benefits

---

<!-- PAGE 2 -->

of this system, which could lead to a more efficient and effective
PB process.

1.1 Paper Structure
After providing an introduction, in Section 1, we go on to discuss
some preliminaries (in Section 2) regarding participatory budgeting
processes, machine learning methods and our algorithmic tasks.
Then, we continue – in Section 3.1 – by describing the different
problem variants we consider and its corresponding algorithms. In
sections 4, 5 and 6 we describe the data sets that we examined our
experiments on, discuss about the evaluation methods and describe
the various experiments we conducted. In Section 7 we present
and discuss our experimental results. We conclude in Section 8, in
which we discuss possible avenues for future research.

2 PRELIMINARIES
We discuss on the binary classification technique and recommen-
dation systems (Section 2.1), the standard model of combinatorial
participatory budgeting (PB; Section 2.2), the model of PB with
partial ballots that we use here (Section 2.3) and the algorithmic
task we dealt with (Section 2.4).

2.1 Binary Classification and Recommendation

Systems

We divide this section to two parts: Binary Classification and Rec-
ommendation systems.

2.1.1 Binary classification. Binary classification is a supervised
machine learning technique in which a model is trained to predict
one of two possible outcomes, often represented as "0" or "1" [18].
This type of classification is commonly used in a wide range of
applications. The primary goal of binary classification is to identify
which of the two classes an input sample belongs to, based on a set
of features or attributes [18]. The process of training a binary clas-
sifier involves providing the model with labeled examples of each
class, and then adjusting the model’s parameters to minimize the
classification error on the training set. Once the model is trained, it
can then be used to make predictions on new, unseen samples. One
popular algorithm for binary classification is XGBoost (eXtreme
Gradient Boosting). This algorithm is an ensemble learning tech-
nique that has been widely used in binary classification tasks [9, 26].
It is an implementation of gradient boosting, a powerful ensemble
method that combines the predictions of multiple weak learners to
produce a more accurate prediction [9, 26]. XGBoost is specifically
designed for decision tree-based models, and it has been observed to
outperform other popular machine learning algorithms [9]. Overall,
XGBoost is a powerful and widely-used tool for binary classification
tasks, and it is well-suited for datasets with complex, non-linear
relationships [9, 26]

2.1.2 Recommendation Systems. RS are tools that are based on ma-
chine learning techniques. Their purpose is to gather and analyze
information regarding the preferences of users wrt. a set of items
in order to deliver for each user a set of recommended items that
the user hopefully will find interesting to interact with [14, 20, 24].
RS are information filtering systems that process user’s and item’s
information to provide personalized prediction on the interaction

Figure 1: Rating matrix example. Each cell represents the
rating that a user gives to a particular item.

between an user and an item, meaning the prediction of the rat-
ing of the item that may be given by the user (such a rating can
be represented in various ranges [14, 20, 24]). RS techniques are
extensively used in the e-commerce industry [4, 20], where there
is a business aspect for how good the recommendations are.

The information based on which such RS operate can be ac-
quired explicitly by collecting users’ ratings. Since the rising of the
popularity of social networks and other platforms, there is a huge
corpus of available data that RS tools can use for their analysis and
operation [14, 20, 22]. Another way for gathering user information
is by a more implicit way, i.e., by analyzing user behavior on aspects
such as web searches and other forms of usage history [4, 14]. In
our research we focused on Collaborative filtering (CF) and Hybrid
RS.

Collaborative Filtering. The collaborative filtering (CF) approach
plays an important role in RS tools. It operates by analyzing relation-
ships between users and items in order to identify new user-item
interactions [15, 20, 21]. CF relies on an old, automatic act of people
sharing opinion between them in order to make better decisions.
For instance, a person may decide to go to a certain restaurant after
hearing good things about it from several friends. Corresponding,
hearing very bad reviews regarding a new movie from colleagues
may result in deciding to watch another movie instead. Essentially,
the CF technique operates in a similar fashion, however it allows
to consider such opinions on a much larger scale [20, 21].

In a CF scenario, a user-item matrix is constructed, where each
cell in the matrix represents the rating that a user gives to a particu-
lar item. Formally, a rating consists of the association of two things
– user and item, one way to visualize ratings is as a matrix where
each row represents a user, each column represents an item, and
the number at the intersection of a row and a column represents
the user’s rating value as shown in Figure 1. The absence of a rating
score at this intersection indicates that user has not yet rated the
item [20, 21].

One primary field of CF is latent factor models [15, 20, 21]. Latent
factor models are a popular technique in RS for capturing the un-
derlying preferences and attributes of users and items [15, 21]. The
idea behind latent factor models is that the observed ratings are gen-
erated by a low-dimensional latent space, where each user and item
is represented by a set of latent factors [15, 21]. The learned latent
factors can then be used to make personalized recommendations
to users. Latent factor models can handle the sparsity problem that
arises in large user-item matrices and can make recommendations
even for users with limited ratings. One latent factor model is the
Matrix Factorization (MF), MF can then be used to factorize this
large user-item matrix into two smaller matrices: a user matrix and
an item matrix [15]. The user matrix captures the latent preferences

2

---

<!-- PAGE 3 -->

of the users, while the item matrix captures the latent attributes of
the items [15, 16]. These factorized matrices can then be used to
make personalized recommendations to users by finding the items
that are most similar to the items they have rated highly in the
past. By using MF, CF can handle the sparsity problem that arises
in large user-item matrices, where many cells are empty, and make
recommendations even for users with limited ratings [15, 16, 20].

Hybrid approach - Factorization Machines. Hybrid RS combine
two or more recommendation techniques to that allow a RS to make
accurate and reliable recommendations with fewer of the drawbacks
of any individual one [6]. The hybrid approach combines the best
of both methods to provide a more holistic approach that can better
identify user preference and personalize the recommendations to
each individual user [6, 20]. It helps to overcome the limitations of
each method such as cold start, scalability and sparsity by combin-
ing the strengths of both and producing better recommendations
than any individual method could provide [16, 20].

Factorization Machines (FM) is a hybrid approach that increas-
ingly gaining traction due to their ability to generate high qual-
ity and personalized recommendations [19]. FM are learning al-
gorithms which combine the strengths of linear models and MF
methods to learn from sparse datasets [19]. This enables them to
capture intricate user-item interactions and the associated latent
factors, resulting in improved accuracy and personalization for
recommending products, movies, and other items to individual
users.

FM models possess several advantages over existing recommen-
dation algorithms, mainly due to their unique structure [19]. Unlike
other models, which rely on fixed feature representations that are
often tailored to one type of dataset, FM models are capable of
automatically learning complex feature representations derived
from interactions between users and items [19, 20]. This essentially
allows them to capture the underlying features that influence users’
preferences in an effective manner [19]. In addition, FM models
are highly efficient in terms of computational cost, as they require
minimal pre-processing and require only a small dataset to produce
accurate results [19, 20].

2.2 Participatory Budgeting
In our research we focus on combinatorial PB, as it is the most stud-
ied and applied model of PB [2]. Below we describe the ingredients
of an instance of combinatorial PB. Note that combinatorial PB is a
formal generalization of multiwinner elections [1].

2.2.1 Projects. The set of projects is denoted by 𝑃 = {𝑝1, . . . , 𝑝𝑚 }.
Each project 𝑝 ∈ 𝑃 has its cost 𝐶𝑝 (usually, the resource taking into
account for cost is money [2]). Note that model is indivisible, and,
in particular, each project can be either fully implemented (at its
given cost) or not implemented at all. In combinatorial PB projects
are either fully implemented or not implemented at all.

2.2.2 Voters. The set of voters is denoted by 𝑉 = {𝑣1, . . . , 𝑣𝑛 },
where each voter submits her preferences on the potential projects.
We consider approval-based processes, in which the ballot of a voter
corresponds to a subset of the set of projects (i.e., voter 𝑣𝑖 submits
an approval ballot, also denoted by 𝑣𝑖 , such that 𝑣𝑖 ⊆ 𝑃).

3

2.2.3 Popularity and Consensus. Given a set 𝑉 of voters with their
approval ballots over a set 𝑃 of projects, it is useful to consider the
approval score of each project as well as the consensus degree of each
project.

Definition 2.1 (Approval scores). 𝑠𝑐𝑜𝑟𝑒 (𝑝) = |{𝑣𝑖 ∈ 𝑉 : 𝑝 ∈ 𝑣𝑖 }|.

The approval score of a project 𝑝, denoted by 𝑠𝑐𝑜𝑟𝑒 (𝑝), is the
number of voters that approve it. We furthermore define 𝜎 to be
the set 𝑃 of projects, sorted in decreasing order of their scores; in
particular, 𝜎1 is the project that has the most votes while 𝜎𝑚 is the
least popular project.

While 𝜎 orders the projects according to their popularity, 𝛾,
defined next, orders the projects according to how much the voters
are in consensus regarding them.

The consensus level of a project 𝑝, denoted by 𝑐𝑜𝑛𝑠𝑒𝑛𝑠𝑢𝑠 (𝑝), is
the absolute difference between the number of voters approving 𝑝
and the number of voters disapproving 𝑝;

Definition 2.2 (Consensus levels). 𝑐𝑜𝑛𝑠𝑒𝑛𝑠𝑢𝑠 (𝑝) = 𝑎𝑏𝑠 (|{𝑣𝑖 ∈ 𝑉 :

𝑝 ∈ 𝑣𝑖 |, |{𝑣𝑖 ∈ 𝑉 : 𝑝 ∉ 𝑣𝑖 }|).

Note that, in particular, both a project that is approved by all
voters as well as a project that is disapproved by all voters have
consensus level 𝑛. Correspondingly, we define 𝛾 to be the set 𝑃 of
projects, sorted in decreasing order of their consensus levels; in
particular, 𝛾𝑚 is the “most controversial” project.

2.2.4 Budget upper limit and outcome. The budget limit is denoted
by 𝐵. The outcome (also referred to as the winning bundle) of a PB
process is a set of projects 𝑝★ ⊆ 𝑃 where (cid:205)𝑝 ∈𝑝★ 𝐶𝑝 ≤ 𝐵 (i.e., that
respects the budget limit).

2.2.5 Voting rules and greedy approval. A voting rule is a function
taking an instance of PB and returning a winning bundle. The most
popular voting rule for PB can be described as a greedy approval [25];
intuitively, it considers the projects according to their approval
scores, decreasingly, and keeps funding projects until the budget is
exhausted.

Formally, greedy approval proceeds in iterations and maintains
a temporary budget 𝐵′ and a temporary winning bundle 𝑆 ′. Initially,
𝐵′ := 𝐵 and 𝑆 ′ = ∅. In the 𝑖th iteration, 𝑖 ∈ [𝑛], the project 𝜎𝑖 is
considered. If 𝐶𝜎𝑖 ≤ 𝐵′, then the amount 𝐶𝜎𝑖 is decreased from
𝐵′ and 𝜎𝑖 is added to 𝑆 ′. After the 𝑛th iteration, 𝑆 ′ contains the
winning bundle.

Example 2.3. Consider a toy example with 𝑃 = {𝑝1, 𝑝2, 𝑝3},
where 𝐶𝑝1 = 𝐶𝑝2 = 1, 𝐶𝑝3 = 2, and 𝐵 = 3; and with 𝑉 = {𝑣1, 𝑣2, 𝑣3}
such that 𝑣1 = {𝑝1, 𝑝2}, 𝑣2 = {𝑝1, 𝑝3}, and 𝑣3 = {𝑝2}.

Note that 𝑠𝑐𝑜𝑟𝑒 (𝑝1) = 𝑠𝑐𝑜𝑟𝑒 (𝑝2) = 2 and 𝑠𝑐𝑜𝑟𝑒 (𝑝3) = 1. Thus, in
the first and second iterations of greedy approval, 𝑝1 and 𝑝2 will
be already selected to be included in the winning bundle; and, so,
in the third iteration of greedy approval, in which 𝑝3 is considered,
there is not enough budget left to fund it, so it will be skipped. The
winning bundle is thus {𝑝1, 𝑝2}.

2.3 Participatory Budgeting with Partial Ballots
Recall that we are interested in situations in which not all voters
provide complete ballots. In a ballot with 𝑚 candidates a partial
vote is case where voter gives preferences only over 𝑗 candidates,

---

<!-- PAGE 4 -->

where 1 ≤ 𝑗 < 𝑚 [12]. Our goal is to create and study algorithms
that, when given a partial ballot as an input, will produce output
as all voters having completely filled out their ballots. Specifically,
we assume that each voter is associated with a set of approved
candidates, a set of disapproved candidates, and a set of candidates
where the voter’s stand is unknown. Formally, voter 𝑣 ∈ {𝑣1, . . . , 𝑣𝑛 }
has an approval set 𝐴𝑣 ⊂ 𝑃, a disapproval set 𝐷𝑣 ⊂ 𝑃 and a hidden
set denoted by 𝐻𝑣 ⊂ 𝑃. Note that 𝐴𝑣 + 𝐷𝑣 + 𝐻𝑣 = 𝑃. We denote
that the merge of approved and disapproved candidates sets is an
exposed set 𝐴𝑣 ∪ 𝐷𝑣 = 𝐸𝑣, 𝐸𝑣 ∈ 𝑃.

Example 2.4. Consider an instance of PB with partial ballots with
3 projects: 𝑝1, 𝑝2, and 𝑝3; and with 2 voters: 𝑣1 and 𝑣2. Let it be that
𝑣1 provides a full ballot in which she approves all projects, while 𝑣2
provides a partial ballot in which she approves 𝑝1, disapproved 𝑝2
and does not provide her preference regarding 𝑝3. We denote such
a setting as follows: 𝑃 = {𝑝1, 𝑝2, 𝑝3}, 𝑉 = {𝑣1, 𝑣2}, 𝐸1 = {𝑝1, 𝑝2, 𝑝3},
𝐴1 = {𝑝1, 𝑝2, 𝑝3}, 𝐷1 = ∅, 𝐻1 = ∅, 𝐸2 = {𝑝1, 𝑝2}, 𝐴2 = {𝑝1},
𝐷2 = {𝑝2}, 𝐻2 = {𝑝3}.

2.4 Algorithmic Tasks
We consider three slightly different algorithmic tasks, correspond-
ing to different ways in which voters may interact with our envi-
sioned application, or to different assumptions regarding the partial
ballots. In all three variants, we assume some ideal instance of PB
containing 𝑛 voters, all of which provide full ballots; denote this
instance by 𝑖𝑑𝑒𝑎𝑙. Intuitively, in the algorithmic tasks we consider,
our goal is to estimate 𝑖𝑑𝑒𝑎𝑙, however the algorithms we design
do not have access to 𝑖𝑑𝑒𝑎𝑙 but only to a PB instance with partial
ballots that agrees with 𝑖𝑑𝑒𝑎𝑙 (a PB instance with partial ballots
is said to agree with some PB instance with full ballots if all the
provided preferences agree; intuitively, if it is possible to complete
the partial instance to be equal to the ideal instance).

Example 2.5. Consider an ideal instance 𝐼 with projects 𝑃 =
{𝑝1, 𝑝2, 𝑝3, 𝑝4} and one voter 𝑣1 where her exposed set 𝐸1 = {𝑝2, 𝑝4}.
Consider a PB instance with partial ballots, denoted by 𝐼 1, with
one voter 𝑣 ′
1 that provides a partial ballot, and let 𝐴1 = {𝑝2} and
𝐷1 = 𝑝1. Then, 𝐼 1 agrees with 𝐼 .

To describe our algorithmic tasks, consider some ideal instance
𝐼 with a set 𝑉 of 𝑛 voters. Then, consider an instance of PB with
partial ballots 𝐼 1 that is constructed by first partitioning two groups
of voters Learning Voters - 𝐿𝑉 and Target Voters - 𝑇𝑉 . Intuitively, 𝐿𝑉
are voters that already provided their full ballots and 𝑇𝑉 are voters
that provides partial ballots. Consider the voters in 𝑇𝑉 and set
them initially so that 𝐸 = ∅; i.e., such that they do not provide any
preference. The overarching goal of our algorithms is to estimate 𝐼
from 𝐼 1. Each of the three algorithmic tasks we consider differentiate
by the allowed operations that the algorithm can perform on 𝐼 1 to
reach this goal, as described next:

Random setup - An algorithm for the random setup operates
as follows: first, for each voter 𝑣 ∈ 𝑇𝑉 , the algorithm chooses 𝑘
projects uniformly at random and moves them into 𝐸, in a way that
𝐼 1 agrees with 𝐼 (possibly different 𝐸 for each voter 𝑣 ∈ 𝑇𝑉 ). Then,
the algorithm has to predict the rest the ballot - 𝐻 for each voter
𝑣 ∈ 𝑇𝑉 .

Offline setup - An algorithm for the offline setup operates as fol-
lows: first, for each voter 𝑣 ∈ 𝑇𝑉 , the algorithm chooses 𝑘 projects
of its choice (possibly by taking into consideration the ballots of
𝐿𝑉 , intuitively assuming some similarity between voters in 𝐿𝑉 and
𝑇𝑉 in 𝐼 ) and moves them into 𝐸, in a way that 𝐼 1 agrees with 𝐼 .
Then, the algorithm has to predict the rest of the ballots - 𝐻 for
each voter 𝑣 ∈ 𝑇𝑉 .

Online setup - An algorithm for the online setup operates as
follows: first, for each voter 𝑣 ∈ 𝑇𝑉 , the algorithm proceeds in 𝑘 it-
erations, where in each iteration the algorithm can choose 1 project
of its choice (possibly by taking into consideration the ballots of 𝐿𝑉
as well as the results of the previous iterations, intuitively assum-
ing some similarity between voters in 𝑇𝑉 and 𝐿𝑉 in 𝐼 and using
the revealed preferences of the previous iterations) and moves it
into 𝐸, in a way that 𝐼 1 agrees with 𝐼 . Then, the algorithm has
to predict the rest of the ballots - 𝐻 for each voter 𝑣 ∈ 𝑇𝑉 . A
more intuitive exposition of these algorithms tasks could be the
following: imagine 𝑛 voters providing their approval ballots where,
pictorially, each voter has 𝑚 cards, one card for each project, on
which the voter writes their approval/disapproval preference. Then,
some voters (those in 𝐿𝑉 ) show all their cards; while others (those
in 𝑇𝑉 ) initially do not show their cards at all. In the random setting,
each such voter shows 𝑘 cards at random to the algorithm; in the
offline setting, the algorithm can choose, for each such voter, a set
of 𝑘 cards that the algorithm wants to see; and in the online setting,
the algorithm can iteratively asks for a first card, a second card,
until a 𝑘th card, to see from each such voter. Finally, the algorithm
shall predict all of the hidden cards. Illustrations of the different
settings can be seen in Figure 2.

3 SOLUTION ARCHITECTURE
In this section we discuss the architecture of our solution, which
consists of three modules: sampling module, prediction module
and voting rule implementation. A graphical representation of our
solution architecture is given in Figure 3.

As mentioned, we propose a computational solution for PB with
partial ballots, where some voters do not complete ballots. As we
want to control the amount of information to gather from voters,
we define a level of partiality as how sparse is our PB and how we
divide the level of partiality to 𝐿𝑉 and 𝑇𝑉 .

3.0.1 Partiality level, Sampling Degree and LV Degree. The Partial-
ity level of a PB denoted by sample degree as the percentage of data
collecting from the voters participate in PB. We denote LV Degree
as the level of collected data that associated with 𝐿𝑉 . As the level
of sampling Degree increases, voters are requested to provide more
data and as the level of LV Degree increases the |𝐿𝑉 | is increases.

Example 3.1. Where Sampling Degree is 1 it means that the PB
is complete, all voters filled their ballots. When Sampling Degree is
0.5 and LV Degree is 1 it means that 50% of votes are known and all
of them are part of full individual ballots. When Sampling Degree is
0.5 and LV Degree is 0.1 it means that 50% of votes are known and
10% of them are part of full individual ballots and 90% are equally
divided between 𝑇𝑉 .

4

---

<!-- PAGE 5 -->

(a) The random setting - the algorithm
chooses randomly 𝑘 projects from each
voter to exposed.

(b) Offline Setting - the algorithm chooses a set of 𝑘 projects that
it asks for each voter to expose.

(c) Online Setting - the algorithm chooses iteratively 𝑘 projects
that it asks for each voter to expose.

Figure 2: Algorithmic Tasks.

3.1 Algorithmic Solutions
We describe several algorithmic solutions for each of the setups we
consider, namely for the random setup, the offline setup, and the
online setup.

5

Figure 3: Architecture: starting with sampling algorithm -
as the way we collect preferences from voters- gain partial
ballot; then filling the missing votes by applying prediction
module; implying voting rule to output the predicted win-
ning bundle.

3.1.1 Algorithms for the Random Setup. Recall that an algorithm
for this setup cannot choose the 𝑘 projects for which the voters in
𝑇𝑉 provide preferences for; thus, the only operation that such an
algorithm does is to predict the remaining preferences of the voters
in 𝑇𝑉 , based on the preferences of voters in 𝐿𝑉 and the preferences
in 𝐸𝑇𝑉 = (𝐸1, . . . , 𝐸𝑛) by prediction methods discussed in Section
2.1.

3.1.2 Algorithms for the Offline Setup. Recall that an algorithm for
this setup first has to choose, for each 𝑣 ∈ 𝑇𝑉 , a set 𝑘 of projects
to “reveal” (to set as 𝐸); and, only then, to predict the remaining
preferences of the voters in 𝑇𝑉 , based on the preferences of voters
in 𝐿𝑉 and the preferences in 𝐸𝑇𝑉 = (𝐸1, . . . , 𝐸𝑛) by prediction
methods discussed in Section 2.1.

• Revealing by popularity

Here the algorithm chooses the top 𝑘 popular projects of the
voters in 𝐿𝑉 and set the 𝐸 of each voter 𝑣 ∈ 𝑇𝑉 to include
exactly those. (I.e., it sets 𝐸 = {𝜎1, . . . , 𝜎𝑘 } for each 𝑣 ∈ 𝑇𝑉 .)

• Revealing by consensus

---

<!-- PAGE 6 -->

Here the algorithm chooses the 𝑘 projects most in consensus
among the voters in 𝐿𝑉 and set the 𝐸 of each voter 𝑣 ∈ 𝑇𝑉
to include exactly those. (I.e., it sets 𝐸 = {𝛾1, . . . , 𝛾𝑘 } for each
𝑣 ∈ 𝑇𝑉 .)

• Revealing by controversiality

Here the algorithm chooses the 𝑘 projects least in consensus
among the voters in 𝐿𝑉 and set the 𝐸 of each voter 𝑣 ∈ 𝑇𝑉
to include exactly those. (I.e., it sets 𝐸 = {𝛾𝑚−𝑘, . . . , 𝛾𝑚 } for
each 𝑣 ∈ 𝑇𝑉 .)
The intuition for this procedure is that the projects least in
consensus correspond to those projects that are the hardest
to predict.

3.1.3 Algorithms for the Online Setup. Recall that an algorithm for
this setup first has to choose, for each 𝑣 ∈ 𝑇𝑉 , a set 𝑘 of projects
to “reveal” (to set as 𝐸); and, only then, to predict the remaining
preferences of the voters in 𝑇𝑉 , based on the preferences of vot-
ers in 𝐿𝑉 and the preferences in 𝐸. But, in contrast to the offline
setting, the algorithm can choose these 𝑘 projects adaptively. We
consider one way of choosing the 𝑘 projects to reveal, adaptively,
namely: adaptive controversial. The algorithm proceeds in 𝑘 itera-
tions, where in each iteration it computes the most controversial
project. (Note that, indeed, this procedure is similar to the revealing
by controversiality procedure of the offline setting, however here
it is done iteratively and adaptively.) After using the adaptive con-
troversial procedure, we predict the remaining hidden preferences,
using prediction methods discussed in Section 2.1.

3.1.4 Voting Rule. After we perform the predicting module we
hold a full ballot, we now chose greedy approval as a voting rule.
As described in Section 2.2.5 for this voting system, each voter is
able to vote for as many candidates as they choose, but cannot
vote for the same candidate twice. The algorithm then begins with
the candidate who has the most number of votes and selects them.
Each subsequent candidate is chosen until the total number of votes
reaches the desired threshold. The aim of this system is to maximize
the amount of “approval” given to the chosen candidates by the
voters [25]. Hence, we output the predicted winning bundle with
respect to a given budget.

4 DATA SETS
We have used a real-world data sets coming for a public repository,
namely Pabulib [10], a public repository for data regarding real-
world instances of participatory budgeting, mainly from several
European cities. In particular, we have used the data concerning
the PB process in different districts from Warsaw, Poland. Out of
this open library we collected ten PB that took place from 2020 to
2023. Table 1 details the amount of voters, amount of projects and
budget for each PB. Table 2 details the attributes of PB’s voters and
projects. Each PB instance consist voters and projects (the projects
correspond to different proposals to improve the development of
Warsaw in several domains such as, e.g., education, environment
protection, public transportation, etc.). The proposals are also aimed
for different segments of the city population, e.g. children, adults,
seniors, and people with disabilities. Note that a certain proposal
can consist multiple topics and population segments. In all PBs the
percentage of voter’s approved project proposals is naturally small,

around 10% of project proposals were approved in every PB, the
exact percentage is detailed in Table 1.

Table 1: Description of used real-world datasets.

PB

Voters

Projects

Budget Approved proposals[%]

Wola 2022
Ursynow 2022
Wola 2021
Praga-Polnoc 2022
Praga-Poludnie 2022
Wawer 2021
Bielany 2020
Wawer 2022
Wola 2023
Targowe 2022

9256
6672
8647
2614
10424
4662
8003
5045
6760
4940

94
107
107
90
96
100
108
111
67
87

524020
5614506
465432
2432952
6643832
2493341
4321791
2807253
5663326
4585180

9.5
10.7
9.8
12.5
10.6
9.1
7.7
7.8
15.3
10.7

Table 2: Voter’s and project’s attributes space.

Voter’s Attributes

Project’s Attributes

Age
Gender
Voting Method

Cost
Category
Population segments

5 EVALUATION
In order to evaluate our predictions methods we divided our dataset
into 3 sets: Train-set, Validation-set and Test set.

In our research context, the train-set is the data that we collected
from voters regarding their votes. The validation set is predefined
set of votes from closed set of voters, these votes are used to tune
the hyperparameters of a model. We denoted that the validation
set size is 15% of each data set. The test-set is the collection of
votes that we use to evaluate our model, these votes are the votes
that we did not collected from the voters. As mentioned in Table 4,
the PB datasets are imbalanced, this can lead to biased results and
sub optimal performance of our predicting models, as the model is
more likely to predict the majority class. We address this issue by
modifying the model loss function to give more weight to minority
class samples.

We divide our evaluation methods into two sections: the classifi-
cation accuracy metrics in which analyze the full predicted ballots
and Bundle evaluation metrics that analyze the final predicted bun-
dle.

5.1 Classification Accuracy Metrics
To analyze our algorithms, we considered a variety of classification
accuracy metrics, namely: precision, recall and f1 [20, 23]. They
measure the amount of correct and incorrect classification and are
derived from confusion matrix. The confusion matrix holds the fol-
lowing measures: The acronym TP, FN, FP, and TN of the confusion
matrix cells refers to the following: TP = true positive, the num-
ber of positive cases that are correctly identified as positive, FN
= false negative, the number of positive cases that are misclassi-
fied as negative cases, FP = false positive, the number of negative
cases that are incorrectly identified as positive cases, TN = true

6

---

<!-- PAGE 7 -->

negative, the number of negative cases that are correctly identified
as negative cases [20, 23]. Precision, defined as 𝑇 𝑃/(𝑇 𝑃 + 𝐹 𝑃), in
RS context is the ratio of the number of relevant recommended
items to the total number of recommended items [20, 23]. Recall,
defined as 𝑇 𝑃/(𝑇 𝑃 + 𝐹 𝑁 ), is the ratio of relevant recommended
items to the number of relevant items.These two metrics, share an
inverse relationship between them. Precision and recall are not sen-
sitive to changes in data distributions. A perfect model will capture
all positive examples (Recall = 1), and score as only the examples
that are in fact (Precision = 1), from an analytical point of view
it is desirable to increase recall without sacrificing accuracy. 𝐹1
measure combines recall and precision as harmonic mean of them,
𝐹1 = (2 ∗ 𝑝𝑟𝑒𝑐𝑖𝑠𝑖𝑜𝑛 ∗ 𝑟𝑒𝑐𝑎𝑙𝑙)/(𝑝𝑟𝑒𝑐𝑖𝑠𝑖𝑜𝑛 + 𝑟𝑒𝑐𝑎𝑙𝑙) and is suitable
measure for an imbalanced data [23].

5.2 Bundle evaluation metrics
Eventually, we have interest in computing the bundle of winning
projects that was decided by the voters, i.e, the list of projects that
’won’ and would be implemented. As an evaluation method we
compared the bundle from the ’real’ votes to the bundle of the
’predicted’ votes. This comparison has done by computing the Sym-
metric Distance between the the real bundle (rb) and the predicted
bundle (pb).

Symmetric Distance. Symmetric distance(SD) is a distance
5.2.1
measure that satisfies the property of symmetry, which states that
the distance between two points is the same in both directions.
Formally, given two points x and y, a SD function f satisfies the
equation f(x,y) = f(y,x). Consider several toy examples: The SD
between 𝑟𝑏 = {1, 2, 3} and 𝑝𝑏 = {2, 1, 3} is 0. The SD between
𝑟𝑏 = {1, 2, 3} and 𝑝𝑏 = {1, 3, 4} is 1. The SD between 𝑟𝑏 = {1, 2, 3}
and 𝑝𝑏 = {1, 4, 5} is 4.

Fractional Allocation score. Another metric we use to eval-
5.2.2
uate the bundle is ’Fractional Allocation’ (FA) Score ; We denote
FA score as the sum costs of projects that were predicted properly
divided by the cost limit - budget.

Definition 5.1 (Fractional Allocation (FA) Score). We define the

fractional allocation score to be: 𝐹𝐴 = 𝜆

𝐵 , 𝜆 = (cid:205)𝑝 ∈𝑝𝑏∩𝑟𝑏 𝑐𝑜𝑠𝑡 (𝑝)

6 EXPERIMENTS
In this section we describe the experiments we conducted on the
real-world data-sets presented in Table 1. We began with defining
the partiality levels of the experiment, we defined multiple levels in
order to conduct several experiments with different Sample degree
and LV degree as mentioned in Section 3.0.1. The range of sample
degrees is 0.1, 0.15, 0.3, 0.5, 0.7 and 0.9 and the range of LV degrees
is 0.1, 0.2, 0.3, 0.5, 0.7, 0.9 and 1. When LV degree is equal to 1 it rep-
resent the case of sample size of the specific Sample Degree. After
we established the frame of the amounts of information we would
collect from the voters, we used each of our sample modules (Ran-
dom, Offline-popularity, Offline-controversial, Offline-consensus
and Online) to gather the preferences from voters. We performed
each sample module on all sample degree-LV degree combination
for 20 times. This procedure was executed on all PB datasets.

Then we performed each prediction module on the each of family
of sample degree and LV degree. We did this procedure on every

7

Figure 4: Treatment Matrix - please see Section 6.

dataset as detailed in Figure 4 for 50 times. We assume that the more
data we collected, higher sample degree in our context, the closer
we will be to the true real ballot results. In particular, we assume
that the FA score would increase as the sample degree increase
and the SD would decrease the sample degree increase for each
setup for every PB. Hence, we conducted a sanity test to check this
assumption.

Every algorithmic setup holds different level of intervention in
selecting the project proposals to collect; in the ’Random’ setup the
algorithm has no power at all in choosing which project proposals
preferences to collect, in the offline setups it has the power to
choose 𝐾 project proposals based on group of voters that provided
full ballots (LV group) and for the online setup it has the power to
choose project proposals based on all voters preferences itteratively.
We assume that the more ’power’ the algorithmic solution hold the
better it would perform better (higher FA score and lower SD).

Hence, for every PB we compared all setups and algorithmic
solutions per sample degree. Additionally, we implemented a per-
formance test in which we compared our solutions with a naive
sampling procedure. This sampling procedure is the case where
LV degree is equal to 1 for a certain sample degree. Note that in
sampling procedure only part of community (sample degree to be
exact) share their preferences, in contrast to our proposed solutions
where every voter has at least 𝐾 project proposals to share her
opinion on. In order to generate it we randomly sampled voters for
each PB for each sample degree for 50 times and calculate its FA
and SD.

7 RESULTS
In this section we describe and discuss our results for the prediction
module, for the sampling module, and for the architecture as a
whole.

First we performed a sanity check to test how the sample and LV
degrees effect on FA scores and SD. We calculated the average FA
scores and SD for all PB’s for each combination of sample degree
and LV degree as described in Figure 4. The sanity test results,
shown in Figures 5 and 6, showed that in most LV degrees, as the
sample degree increases the FA score increases as well and the SD
is decreases, as assumed.

Furthermore, it can be observed that as the LV degree increases
the FA score/SD increases/decreases as well, by means the predic-
tion modules perform better when a larger group of voters provide
their full ballots.

In Figures 7 - 12 we can see the FA scores performance of every
setup as function of LV degree and sample degree including a com-
parison to sampling method (LV degree equals to 1). It seems that in
some settings some of our solutions succeed better than a sampling

---

<!-- PAGE 8 -->

scores, Classification-online and Classification-offline-popularity
setups perform best for all sample degrees.

8 CONCLUSIONS AND OUTLOOK
We have proposed the use of techniques from machine learning
and recommendation systems to tackle the information overload
problem in participatory budgeting. Technically, we have developed
a more of PB with partial ballots that is useful for our context, de-
signed several algorithmic solutions for different specific prediction
settings, and reported on the results of computer-based simula-
tions showing the high quality of prediction with respect to voter
ballots and the winning bundles that the algorithms achieve for a
real-world data. We conducted our experiments on 10 real-world
PB and eliminated some preferences to simulate PB with partial
ballots. This elimination of preferences were conducted under con-
trolled and structured manner, defined as sampling module. After
we created these partial ballots we implemented prediction module
to predict the missing preferences. Then we calculated the winning
bundle using greedy approval voting rule. We evaluate our sampling
and prediction modules by comparing the winning bundles to the
real ones. The comparison were defined by symmetric distance and
Fractional Allocation score, as a measure of how good the budget
was allocated in the predicted winning ballot. Except from com-
paring our own solutions between themselves, we compared them
to a naive sampling method. We found that some of our solutions
perform better from sampling method. Hence, although taking a
sample of PB community and extract winning bundle out of it’s
preferences is quite easy and performs relatively good, we propose
solution that take into account all of PB’s voters and performs bet-
ter than sampling methods. So, our solutions permit all potential
voters in a PB to express their opinions regarding project proposals
and provide a solution to the information overload problem.

Some avenues for future research are the following:

• A different, somewhat stronger setting may correspond to
algorithms that initially get an instance of PB with partial
ballots where all voter preferences are hidden (i.e., where
𝑇𝑉 = 𝑉 and 𝐸 = ∅ for all 𝑣 ∈ 𝑇𝑉 ). Designing and analyzing
algorithms for this setting is of practical importance, as,
inherently, a PB process starts with only completely empty
ballots. From a technical point of view, this would naturally
allow the algorithm consider more complex correlations
across the electorate.

• A more interactive setting that is worth considering may
be the following: first, the voter reveals some of her pref-
erence, after which the algorithm estimates the rest of the
ballot (or, alternatively, only the preferences of the voter
regarding some further projects not yet revealed). Then, the
voter has the possibility to examine the predictions done
by the algorithm and to “correct” some of them, in which
case the algorithm can further update its estimates regarding
the remaining projects. Such an interactive communication
between a voter and the envision application may lead to
results of higher quality.

• While here we have considered the quite standard PB setting
of approval-based combinatorial PB, analyzing a similar RS-
oriented approach for different settings of PB (in particular,

Figure 5: Sanity test - heatmap of FA scores as function of
Sample degree and LV degree.

Figure 6: Sanity test - heatmap of SD as function of Sample
degree and LV degree.

method. Specifically, for sample degree equals to 0.1 (Figure 7) all
solutions except MF-online, MF-offline-popularity and FM-online
produce higher FA scores than sampling method. Specifically the
Classification-online and Classification-off-popularity setups for
sample deg equals to 0.1 perform better than sampling method
for sample degree equals to 0.3. In Figure 8 it seems that our so-
lutions perform not as good as the sampling method, except from
Classification-online and Classification-off-popularity. In Figure 9
we can see that more of our solutions perform better or good as
good as the sampling method, except from Classification-online and
Classification-off-popularity. In Figure 10 we see that the random
setups, for all prediction modules, outperforms and achieved rela-
tively high FA scores. Additionally, the Classification-off-popularity
gained the maximal FA score, we achieved it for collecting half of
the votes. As for sample degree equals to 0.7 and 0.9 it is not surpris-
ing that our solutions gained high FA scores. Through all sample
degrees the setups that perform best, produce the higher FA scores,
are the Classification-online and Classification-offline-popularity
setups, especially in the 0.1, 0.15 and 0.3 sample degrees. For higher
sampling degrees all of our solutions perform better or good as
sampling methods. As we assumed, the random sampling module
perform worse than the offline and online sampling modules. As for
the prediction modules, it is shown that the classification technique
performs better than the RS techniques.

In Figures 13 - 18 represent the SD of every setup as function of
LV degree and sample degree including a comparison to sampling
method. We see quite the same trend as we saw for for the FA

8

---

<!-- PAGE 9 -->

APPENDIX
We provide some further plots in the appendix. Figures 7 - 12 de-
scribe the FA scores that were produced for every combination
of the algorithmic solutions, prediction module, LV degree and
sample degree as describe in Figure 4. These heatmaps enable us
to compare the FA scores between the algorithmic solutions (ran-
dom, offline-popularity, offline-consensus, offline controversy and
online) and between the prediction module (MF, FM and binary
classification). Furthermore, we compare between our solutions
across all LV degree levels to sampling solution, where only part of
the voters taken into account, it is the case where LV degree equals
to 1, where each figure refers to different sample degree.

Figures 13 - 18 describe the same comparisons shown above but

for Symmetric distances (SD).

those in the survey of Aziz and Shah [2]) is a natural avenue
for future research.

• While we proposed certain approaches to address the predic-
tion module, it would be interesting to imply other machine
learning techniques to predict voter’s ballot.

REFERENCES
[1] Haris Aziz, Barton Lee, and Nimrod Talmon. 2017. Proportionally representative
participatory budgeting: Axioms and algorithms. arXiv preprint arXiv:1711.08226
(2017).

[2] Haris Aziz and Nisarg Shah. 2021. Participatory budgeting: Models and ap-
proaches. In Pathways Between Social Science and Computational Social Science.
Springer, 215–236.

[3] Gerdus Benade, Swaprava Nath, Ariel D Procaccia, and Nisarg Shah. 2021. Pref-
erence elicitation for participatory budgeting. Management Science 67, 5 (2021),
2813–2827.

[4] Jesús Bobadilla, Fernando Ortega, Antonio Hernando, and Abraham Gutiérrez.
2013. Recommender systems survey. Knowledge-based systems 46 (2013), 109–
132.

[5] Felix Brandt, Vincent Conitzer, and Ulle Endriss. 2012. Computational social

choice. Multiagent systems 2 (2012), 213–284.

[6] Robin Burke. 2002. Hybrid recommender systems: Survey and experiments. User

modeling and user-adapted interaction 12, 4 (2002), 331–370.

[7] Yves Cabannes. 2004. Participatory budgeting: a significant contribution to
participatory democracy. Environment and urbanization 16, 1 (2004), 27–46.
[8] Iván Cantador, María E Cortés-Cediel, Miriam Fernández, and Harith Alani. 2018.
What’s going on in my city? recommender systems and electronic participatory
budgeting. In Proceedings of the 12th ACM Conference on Recommender Systems.
219–223.

[9] Tianqi Chen and Carlos Guestrin. 2016. Xgboost: A scalable tree boosting system.
In Proceedings of the 22nd acm sigkdd international conference on knowledge
discovery and data mining. 785–794.

[10] Nimrod Talmon Dariusz Stolicki, Stanisław Szufa. 2020. pabulib an open PArtici-

patory BUdgeting LIBrary. http://http://pabulib.org.

[11] Angela Edmunds and Anne Morris. 2000. The problem of information overload
International journal of

in business organisations: a review of the literature.
information management 20, 1 (2000), 17–28.

[12] Peter Emerson. 2013. The original Borda count and partial voting. Social Choice

and Welfare 40, 2 (2013), 353–358.

[13] Wulf Gaertner. 2009. A primer in social choice theory: Revised edition. Oxford

University Press.

[14] Dietmar Jannach, Markus Zanker, Alexander Felfernig, and Gerhard Friedrich.
2010. Recommender systems: an introduction. Cambridge University Press.
[15] Yehuda Koren, Robert Bell, and Chris Volinsky. 2009. Matrix factorization tech-

niques for recommender systems. Computer 42, 8 (2009), 30–37.

[16] Blerina Lika, Kostas Kolomvatsos, and Stathes Hadjiefthymiades. 2014. Facing
the cold start problem in recommender systems. Expert Systems with Applications
41, 4 (2014), 2065–2073.

[17] Ian MD Little. 1952. Social choice and individual values. Journal of Political

Economy 60, 5 (1952), 422–432.

[18] Tom M Mitchell and Tom M Mitchell. 1997. Machine learning. Vol. 1. McGraw-hill

New York.

[19] Steffen Rendle. 2010. Factorization machines. In 2010 IEEE International conference

on data mining. IEEE, 995–1000.

[20] Francesco Ricci, Lior Rokach, and Bracha Shapira. 2011. Introduction to rec-
In Recommender systems handbook. Springer,

ommender systems handbook.
1–35.

[21] J Ben Schafer, Dan Frankowski, Jon Herlocker, and Shilad Sen. 2007. Collaborative
filtering recommender systems. In The adaptive web. Springer, 291–324.
[22] J Ben Schafer, Joseph Konstan, and John Riedl. 1999. Recommender systems in
e-commerce. In Proceedings of the 1st ACM conference on Electronic commerce.
158–166.

[23] Gunnar Schröder, Maik Thiele, and Wolfgang Lehner. 2011. Setting goals and
choosing metrics for recommender system evaluations. In UCERSTI2 workshop at
the 5th ACM conference on recommender systems, Chicago, USA, Vol. 23. 53.
[24] Guy Shani and Asela Gunawardana. 2011. Evaluating recommendation systems.

In Recommender systems handbook. Springer, 257–297.

[25] Nimrod Talmon and Piotr Faliszewski. 2019. A framework for approval-based

budgeting methods. In Proceedings of AAAI ’19, Vol. 33. 2181–2188.

[26] Chen Wang, Chengyuan Deng, and Suzhen Wang. 2020. Imbalance-XGBoost:
leveraging weighted and focal losses for binary label-imbalanced classification
with XGBoost. Pattern Recognition Letters 136 (2020), 190–197.

[27] Yueping Zheng and Hindy Lauer Schachter. 2017. Explaining citizens’ E-
participation use: The role of perceived advantages. Public Organization Review
17, 3 (2017), 409–428.

9

---

<!-- PAGE 10 -->

Figure 11: Heatmap of FA for Sample degree = 0.7.

Figure 7: Heatmap of FA for Sample degree = 0.1.

Figure 12: Heatmap of FA for Sample degree = 0.9.

Figure 8: Heatmap of FA for Sample degree = 0.15.

Figure 13: Heatmap of SD for Sample degree = 0.1.

Figure 9: Heatmap of FA for Sample degree = 0.3.

Figure 14: Heatmap of SD for Sample degree = 0.15.

Figure 10: Heatmap of FA for Sample degree = 0.5.

10

---

<!-- PAGE 11 -->

Figure 15: Heatmap of SD for Sample degree = 0.3.

Figure 17: Heatmap of SD for Sample degree = 0.7.

Figure 16: Heatmap of SD for Sample degree = 0.5.

Figure 18: Heatmap of SD for Sample degree = 0.9.

11

<!-- MARKITDOWN CONVERSION -->

<!-- Full MarkItDown conversion for formatting fidelity. -->

A Recommendation System for Participatory Budgeting
GilLeibiker NimrodTalmon
Ben-GurionUniversity,Israel
ABSTRACT Asub-fieldofComputationalsocialchoiceisParticipatoryBud-
Inparticipatorybudgeting,votersspecifytheirpreferencesovera geting(PB).PBisademocraticprocessinwhichcommunitymem-
setofprojectsofdifferentcostsandthegoalistoselectasubset bersdecidehowtospendaportionofapublicorprivatebudget.
oftheseprojectsthatsatisfysometotalcostupperboundwhile PBallowsmembersofacommunitytomaketheirvoicesheard
taking into account the preferences of the voters. To lower the regardingfundingdecisionsaffectingarangeoffieldssuchasedu-
cognitiveburdenonvoters,andtoincreasevoterparticipationin cation,healthandenvironment.Itgivesthemthepowertocompose
PBprocesses,weproposeanapproachbasedonamachinelearning projectproposalsandtoexpresstheirpreferencesoverthebudget
techniquesasrecommendationsystemandbinaryclassification allocation[1–3,7].Inourstudyweconcentrateonthemostpopular
thatqueriesvotersforpartialballotsandestimatestheircompletion. variantofPB,namelyapproval-basedcombinatorialPB.Thatis,
Wedevelopseveralconcretealgorithmsandevaluatethem–based givenasetofprojects–eachwithitscost–eachvoterexpressesits
onreal-worldinstances–wrt.theirabilitytocorrectlyapproximate preferencesovertheprojectsbyselectingasubsetoftheprojects
voterballotsaswellastheoveralloutcomeoftheprocess. thatshe“approvesof”,andtheresultoftheprocessofaggregating
suchvoterpreferencesisasubsetoftheprojectswhosetotalcost
KEYWORDS doesnotgooversomegivenbudgetupperbound[2,3].
InthisresearchweconsiderprocessesofPBandconcentrate
ComputationalSocialChoice,Attention-AwareSocialChoice,Par-
ontheinformationoverloadproblem,i.e.,thecognitiveburdenof
ticipatoryBudgeting,MachineLearning,RecommendationSystem
votersparticipatinginsuchprocesses.Essentially,theinformation
overloadproblemappearswhentoomuchinformationinterferes
ACMReferenceFormat:
withdecisionmaking[11,20].Tomitigatetheinformationoverload
GilLeibiker NimrodTalmon,Ben-GurionUniversity,Israel.2023.A
RecommendationSystemforParticipatoryBudgeting.InProc.ofthe22nd problemweproposeseveralsolutionsbasedontechniquesfrom
InternationalConferenceonAutonomousAgentsandMultiagentSystems machinelearningandrecommendationsystems.
(AAMAS2023),London,UnitedKingdom,May29–June2,2023,IFAAMAS, Recommendationsystems(RS)areapowerfultoolinmachine
11pages. learning,utilizingalgorithmstoprocesslargedatasetsandmake
personalizedpredictionsforusers[14,20].Bylearninguserprefer-
encesandusagepatterns,RScanprovideuserswithtailoredand
1 INTRODUCTION
relevantrecommendationsforproducts,services,orcontent[11,20].
SocialChoiceTheoryisabranchofeconomicsthatstudiescollec- Forexample,amovieRScouldsuggestfilmsbasedonpastuser
tivedecision-makingprocessesandthepreferencesofindividual ratings,genrepreferences,andevensocialconnections.Similarly,
agents.Itaimstodeterminehowamajoritycanmakedecisions arestaurantRScouldsuggesteateriesbasedonlocation,cuisine
basedonthepreferencesofagroup,whilestillrespectingeach type,andpricerange.Moreover,RSarebeingappliedinmanyother
individualinvolved.Thetheoryexploresvariousvotingsystems areassuchasmusic,books,andshopping,makingthemanimpor-
andwaystostructurevotingproceduresinordertomoreaccurately tantpartofmachinelearning.Theinformationoverloadproblem
representthewillofthemajority.SocialChoiceTheoryisanim- isdeeplyrelatedtotheresearchonRS[4,20,24].Itmayeffect
portantresearchareaasitseekstounderstandcollectivebehavior, the decision making of participants in such systems in various
andcanbeappliedtonumerousfieldssuchaspoliticaldecision- aspects,inparticularasusersmayfinditchallengingtochoose
making, economic welfare, and game theory. In essence, Social themostappropriatechoicesoutofthehugeamountandvariety
ChoiceTheoryprovidesaframeworktobetterunderstandinghow ofcontentthattheinternetoffers.ThegoalofaRSistosupport
ourdecisionsimpactothers,andhowwecanmakedecisionsthat usersinvariousdomainsofdecisionmakingprocesses,suchas
arebothequitableandefficient[5,13,17] whatitemstopurchase,whichmoviestowatch,orwhichbooks
Computationalsocialchoiceisafieldofresearchthatcombines toread[14,20,22].Inparticular,theresearchonRS,beingwell-
computerscience,gametheoryandsocialchoicetheorytodevelop establishedbynow,offersvaluabletoolsforonlineuserstocope
algorithmsforcollectivedecisionmaking.Itexamineshowgroups withinformationoverloadandhelptheminmakingbetterchoices.
ofpeoplecanusecomputerstomakedecisionsthatarefair,effi- Inthispaperwediscusstheproblemofinformationoverloadin
cientandbasedoninputsfromallinvolvedparties.Computational PBwherevotershavetoconsideralargenumberofprojects,leading
socialchoicecanbeusedinavarietyofreal-worldscenariossuch to a time-consuming and attention-demanding task [8, 27]. We
as voting systems, resource allocation, market design and even proposeasolutionthatinvolvesanapplicationthatusesmachine
communicationsnetworks[5]. learningandRStoestimateavoter’spreferencesfortheremaining
projectsbasedontheiropinionsaboutafewprojects.Thisapproach
couldsavevoterstimeandallowthemtoexpressbetterpreferences
Proc.ofthe22ndInternationalConferenceonAutonomousAgentsandMultiagentSys-
tems(AAMAS2023),A.Ricci,W.Yeoh,N.Agmon,B.An(eds.),May29–June2,2023, fortheproposalstheydoconsider.Thepaperhighlightsthebenefits
London,UnitedKingdom.©2023InternationalFoundationforAutonomousAgents
andMultiagentSystems(www.ifaamas.org).Allrightsreserved.

ofthissystem,whichcouldleadtoamoreefficientandeffective
PBprocess.
1.1 PaperStructure
Afterprovidinganintroduction,inSection1,wegoontodiscuss
somepreliminaries(inSection2)regardingparticipatorybudgeting
Figure1:Ratingmatrixexample.Eachcellrepresentsthe
processes,machinelearningmethodsandouralgorithmictasks.
ratingthatausergivestoaparticularitem.
Then,wecontinue–inSection3.1–bydescribingthedifferent
problemvariantsweconsideranditscorrespondingalgorithms.In
sections4,5and6wedescribethedatasetsthatweexaminedour betweenanuserandanitem,meaningthepredictionoftherat-
experimentson,discussabouttheevaluationmethodsanddescribe ingoftheitemthatmaybegivenbytheuser(sucharatingcan
thevariousexperimentsweconducted.InSection7wepresent berepresentedinvariousranges[14,20,24]).RStechniquesare
anddiscussourexperimentalresults.WeconcludeinSection8,in extensivelyusedinthee-commerceindustry[4,20],wherethere
whichwediscusspossibleavenuesforfutureresearch. isabusinessaspectforhowgoodtherecommendationsare.
The information based on which such RS operate can be ac-
2 PRELIMINARIES
quiredexplicitlybycollectingusers’ratings.Sincetherisingofthe
Wediscussonthebinaryclassificationtechniqueandrecommen- popularityofsocialnetworksandotherplatforms,thereisahuge
dationsystems(Section2.1),thestandardmodelofcombinatorial corpusofavailabledatathatRStoolscanusefortheiranalysisand
participatorybudgeting(PB;Section2.2),themodelofPBwith operation[14,20,22].Anotherwayforgatheringuserinformation
partialballotsthatweusehere(Section2.3)andthealgorithmic isbyamoreimplicitway,i.e.,byanalyzinguserbehavioronaspects
taskwedealtwith(Section2.4). suchaswebsearchesandotherformsofusagehistory[4,14].In
ourresearchwefocusedonCollaborativefiltering(CF)andHybrid
2.1 BinaryClassificationandRecommendation RS.
Systems
CollaborativeFiltering. Thecollaborativefiltering(CF)approach
Wedividethissectiontotwoparts:BinaryClassificationandRec- playsanimportantroleinRStools.Itoperatesbyanalyzingrelation-
ommendationsystems. shipsbetweenusersanditemsinordertoidentifynewuser-item
interactions[15,20,21].CFreliesonanold,automaticactofpeople
2.1.1 Binaryclassification. Binaryclassificationisasupervised
sharingopinionbetweentheminordertomakebetterdecisions.
machinelearningtechniqueinwhichamodelistrainedtopredict
Forinstance,apersonmaydecidetogotoacertainrestaurantafter
oneoftwopossibleoutcomes,oftenrepresentedas"0"or"1"[18].
hearinggoodthingsaboutitfromseveralfriends.Corresponding,
Thistypeofclassificationiscommonlyusedinawiderangeof
hearingverybadreviewsregardinganewmoviefromcolleagues
applications.Theprimarygoalofbinaryclassificationistoidentify
mayresultindecidingtowatchanothermovieinstead.Essentially,
whichofthetwoclassesaninputsamplebelongsto,basedonaset
theCFtechniqueoperatesinasimilarfashion,howeveritallows
offeaturesorattributes[18].Theprocessoftrainingabinaryclas-
toconsidersuchopinionsonamuchlargerscale[20,21].
sifierinvolvesprovidingthemodelwithlabeledexamplesofeach
InaCFscenario,auser-itemmatrixisconstructed,whereeach
class,andthenadjustingthemodel’sparameterstominimizethe
cellinthematrixrepresentstheratingthatausergivestoaparticu-
classificationerroronthetrainingset.Oncethemodelistrained,it
laritem.Formally,aratingconsistsoftheassociationoftwothings
canthenbeusedtomakepredictionsonnew,unseensamples.One
–useranditem,onewaytovisualizeratingsisasamatrixwhere
popularalgorithmforbinaryclassificationisXGBoost(eXtreme
eachrowrepresentsauser,eachcolumnrepresentsanitem,and
GradientBoosting).Thisalgorithmisanensemblelearningtech-
thenumberattheintersectionofarowandacolumnrepresents
niquethathasbeenwidelyusedinbinaryclassificationtasks[9,26].
theuser’sratingvalueasshowninFigure1.Theabsenceofarating
Itisanimplementationofgradientboosting,apowerfulensemble
scoreatthisintersectionindicatesthatuserhasnotyetratedthe
methodthatcombinesthepredictionsofmultipleweaklearnersto
item[20,21].
produceamoreaccurateprediction[9,26].XGBoostisspecifically
OneprimaryfieldofCFislatentfactormodels[15,20,21].Latent
designedfordecisiontree-basedmodels,andithasbeenobservedto
factormodelsareapopulartechniqueinRSforcapturingtheun-
outperformotherpopularmachinelearningalgorithms[9].Overall,
derlyingpreferencesandattributesofusersanditems[15,21].The
XGBoostisapowerfulandwidely-usedtoolforbinaryclassification
ideabehindlatentfactormodelsisthattheobservedratingsaregen-
tasks,anditiswell-suitedfordatasetswithcomplex,non-linear
eratedbyalow-dimensionallatentspace,whereeachuseranditem
relationships[9,26]
isrepresentedbyasetoflatentfactors[15,21].Thelearnedlatent
2.1.2 RecommendationSystems. RSaretoolsthatarebasedonma- factorscanthenbeusedtomakepersonalizedrecommendations
chinelearningtechniques.Theirpurposeistogatherandanalyze tousers.Latentfactormodelscanhandlethesparsityproblemthat
informationregardingthepreferencesofuserswrt.asetofitems arisesinlargeuser-itemmatricesandcanmakerecommendations
inordertodeliverforeachuserasetofrecommendeditemsthat evenforuserswithlimitedratings.Onelatentfactormodelisthe
theuserhopefullywillfindinterestingtointeractwith[14,20,24]. MatrixFactorization(MF),MFcanthenbeusedtofactorizethis
RSareinformationfilteringsystemsthatprocessuser’sanditem’s largeuser-itemmatrixintotwosmallermatrices:ausermatrixand
informationtoprovidepersonalizedpredictionontheinteraction anitemmatrix[15].Theusermatrixcapturesthelatentpreferences
2

oftheusers,whiletheitemmatrixcapturesthelatentattributesof 2.2.3 PopularityandConsensus. Givenaset𝑉 ofvoterswiththeir
approvalballotsoveraset𝑃
theitems[15,16].Thesefactorizedmatricescanthenbeusedto ofprojects,itisusefultoconsiderthe
makepersonalizedrecommendationstousersbyfindingtheitems approvalscoreofeachprojectaswellastheconsensusdegreeofeach
| thataremostsimilartotheitemstheyhaveratedhighlyinthe |     |     |     | project. |     |     |     |     |     |     |     |
| ---------------------------------------------------- | --- | --- | --- | -------- | --- | --- | --- | --- | --- | --- | --- |
past.ByusingMF,CFcanhandlethesparsityproblemthatarises
|                                                         |     |     |     | Definition2.1(Approvalscores). |     |     |     | 𝑠𝑐𝑜𝑟𝑒(𝑝)=|{𝑣 |     | ∈𝑉  | :𝑝 ∈𝑣 𝑖}|. |
| ------------------------------------------------------- | --- | --- | --- | ------------------------------ | --- | --- | --- | ------------ | --- | --- | ---------- |
| inlargeuser-itemmatrices,wheremanycellsareempty,andmake |     |     |     |                                |     |     |     |              |     | 𝑖   |            |
ofaproject𝑝,denotedby𝑠𝑐𝑜𝑟𝑒(𝑝),isthe
recommendationsevenforuserswithlimitedratings[15,16,20]. Theapprovalscore
numberofvotersthatapproveit.Wefurthermoredefine𝜎
tobe
Hybridapproach-FactorizationMachines. HybridRScombine theset𝑃 ofprojects,sortedindecreasingorderoftheirscores;in
twoormorerecommendationtechniquestothatallowaRStomake particular,𝜎 1istheprojectthathasthemostvoteswhile𝜎 𝑚 isthe
accurateandreliablerecommendationswithfewerofthedrawbacks leastpopularproject.
ofanyindividualone[6].Thehybridapproachcombinesthebest 𝜎 popularity,𝛾,
|     |     |     |     | While |     | orders | the projects | according |     | to their |     |
| --- | --- | --- | --- | ----- | --- | ------ | ------------ | --------- | --- | -------- | --- |
ofbothmethodstoprovideamoreholisticapproachthatcanbetter
definednext,orderstheprojectsaccordingtohowmuchthevoters
identifyuserpreferenceandpersonalizetherecommendationsto
areinconsensusregardingthem.
eachindividualuser[6,20].Ithelpstoovercomethelimitationsof Theconsensuslevelofaproject𝑝,denotedby𝑐𝑜𝑛𝑠𝑒𝑛𝑠𝑢𝑠(𝑝),is
eachmethodsuchascoldstart,scalabilityandsparsitybycombin- theabsolutedifferencebetweenthenumberofvotersapproving𝑝
ingthestrengthsofbothandproducingbetterrecommendations andthenumberofvotersdisapproving𝑝;
thananyindividualmethodcouldprovide[16,20].
FactorizationMachines(FM)isahybridapproachthatincreas- Definition2.2(Consensuslevels). 𝑐𝑜𝑛𝑠𝑒𝑛𝑠𝑢𝑠(𝑝) =𝑎𝑏𝑠(|{𝑣 𝑖 ∈𝑉 :
|     |     |     |     | 𝑝 ∈𝑣 | 𝑖|,|{𝑣 | 𝑖 ∈𝑉 :𝑝 | ∉𝑣 𝑖}|). |     |     |     |     |
| --- | --- | --- | --- | ---- | ------ | ------- | -------- | --- | --- | --- | --- |
inglygainingtractionduetotheirabilitytogeneratehighqual-
ityandpersonalizedrecommendations[19].FMarelearningal-
Notethat,inparticular,bothaprojectthatisapprovedbyall
gorithmswhichcombinethestrengthsoflinearmodelsandMF
votersaswellasaprojectthatisdisapprovedbyallvotershave
methodstolearnfromsparsedatasets[19].Thisenablesthemto
|     |     |     |     | consensuslevel𝑛.Correspondingly,wedefine𝛾 |     |     |     |     |     | tobetheset𝑃 | of  |
| --- | --- | --- | --- | ----------------------------------------- | --- | --- | --- | --- | --- | ----------- | --- |
captureintricateuser-iteminteractionsandtheassociatedlatent
projects,sortedindecreasingorderoftheirconsensuslevels;in
factors, resulting in improved accuracy and personalization for particular,𝛾 isthe“mostcontroversial”project.
𝑚
| recommending | products, | movies, and other | items to individual |     |     |     |     |     |     |     |     |
| ------------ | --------- | ----------------- | ------------------- | --- | --- | --- | --- | --- | --- | --- | --- |
users. 2.2.4 Budgetupperlimitandoutcome. Thebudgetlimitisdenoted
by𝐵.Theoutcome(alsoreferredtoasthewinningbundle)ofaPB
FMmodelspossessseveraladvantagesoverexistingrecommen-
|     |     |     |     | processisasetofprojects𝑝★⊆𝑃 |     |     |     | where(cid:205) |     |     |     |
| --- | --- | --- | --- | --------------------------- | --- | --- | --- | -------------- | --- | --- | --- |
dationalgorithms,mainlyduetotheiruniquestructure[19].Unlike 𝑝∈𝑝★ 𝐶 𝑝 ≤𝐵(i.e.,that
respectsthebudgetlimit).
othermodels,whichrelyonfixedfeaturerepresentationsthatare
oftentailoredtoonetypeofdataset,FMmodelsarecapableof
|     |     |     |     | 2.2.5 | Votingrulesandgreedyapproval. |     |     |     | Avotingruleisafunction |     |     |
| --- | --- | --- | --- | ----- | ----------------------------- | --- | --- | --- | ---------------------- | --- | --- |
automaticallylearningcomplexfeaturerepresentationsderived
takinganinstanceofPBandreturningawinningbundle.Themost
frominteractionsbetweenusersanditems[19,20].Thisessentially
popularvotingruleforPBcanbedescribedasagreedyapproval[25];
allowsthemtocapturetheunderlyingfeaturesthatinfluenceusers’
intuitively,itconsiderstheprojectsaccordingtotheirapproval
preferencesinaneffectivemanner[19].Inaddition,FMmodels scores,decreasingly,andkeepsfundingprojectsuntilthebudgetis
arehighlyefficientintermsofcomputationalcost,astheyrequire
exhausted.
minimalpre-processingandrequireonlyasmalldatasettoproduce
Formally,greedyapprovalproceedsiniterationsandmaintains
accurateresults[19,20]. atemporarybudget𝐵′andatemporarywinningbundle𝑆′.Initially,
|     |     |     |     | 𝐵′  | := 𝐵and𝑆′ | =   | ∅.Inthe𝑖thiteration,𝑖 |     | ∈   | [𝑛],theproject𝜎 | 𝑖 is |
| --- | --- | --- | --- | --- | --------- | --- | --------------------- | --- | --- | --------------- | ---- |
2.2 ParticipatoryBudgeting considered.If𝐶 ≤ 𝐵′,thentheamount𝐶 isdecreasedfrom
|     |     |     |     |     |     | 𝜎𝑖  |     |     |     | 𝜎𝑖  |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
𝐵′ and𝜎 isaddedto𝑆′.Afterthe𝑛thiteration,𝑆′
InourresearchwefocusoncombinatorialPB,asitisthemoststud- 𝑖 containsthe
| iedandappliedmodelofPB[2].Belowwedescribetheingredients |     |     |     | winningbundle. |     |     |     |     |     |     |     |
| ------------------------------------------------------- | --- | --- | --- | -------------- | --- | --- | --- | --- | --- | --- | --- |
ofaninstanceofcombinatorialPB.NotethatcombinatorialPBisa
|                                                |     |     |     | Example |     | 2.3. Consider |                    | a toy example | with | 𝑃 =     | {𝑝 ,𝑝 ,𝑝 }, |
| ---------------------------------------------- | --- | --- | --- | ------- | --- | ------------- | ------------------ | ------------- | ---- | ------- | ----------- |
| formalgeneralizationofmultiwinnerelections[1]. |     |     |     |         |     |               |                    |               |      |         | 1 2 3       |
|                                                |     |     |     | where𝐶  |     | =𝐶 =1,𝐶       | =2,and𝐵=3;andwith𝑉 |               |      |         | ={𝑣 ,𝑣 ,𝑣 } |
|                                                |     |     |     |         | 𝑝 1 | 𝑝 2           | 𝑝 3                |               |      |         | 1 2 3       |
|                                                |     |     |     |         | 𝑣   | = { 𝑝         | , 𝑝 }, 𝑣 =         | { 𝑝 , 𝑝 },    | 𝑣    | = { 𝑝 } |             |
2 . 2 .1 P r o j e c ts. T he s et o f p r o j ec ts i s d e n o t e d b y 𝑃 = { 𝑝 , . . . ,𝑝 } . suc h t h a t 1 1 2 2 1 3 an d 3 2 .
|     |       |     | 1 𝑚 |     |             | t𝑠 𝑐𝑜 𝑟 𝑒 | 𝑝 𝑠𝑐 𝑜𝑟 | 𝑒 𝑝     | 𝑠𝑐     | 𝑜𝑟 𝑒 𝑝          |     |
| --- | ----- | --- | --- | --- | ----------- | --------- | ------- | ------- | ------ | --------------- | --- |
|     | 𝑝 ∈ 𝑃 | 𝐶   |     | N   | o t e t h a |           | ( 1 ) = | ( 2 ) = | 2 a nd | ( 3 )=1.Thus,in |     |
E a c hpr o j e c t ha s it s c o s t 𝑝 (u s u a l ly , t h e re s ou rc e t a k i n g in t o thefirstandseconditerationsofgreedyapproval,𝑝 1and𝑝
2will
accountforcostismoney[2]).Notethatmodelisindivisible,and,
bealreadyselectedtobeincludedinthewinningbundle;and,so,
inparticular,eachprojectcanbeeitherfullyimplemented(atits
|     |     |     |     | inthethirditerationofgreedyapproval,inwhich𝑝 |     |     |     |     |     | 3isconsidered, |     |
| --- | --- | --- | --- | -------------------------------------------- | --- | --- | --- | --- | --- | -------------- | --- |
givencost)ornotimplementedatall.IncombinatorialPBprojects
thereisnotenoughbudgetlefttofundit,soitwillbeskipped.The
areeitherfullyimplementedornotimplementedatall.
|               |            |                       |                 | winningbundleisthus{𝑝 |     |     | ,𝑝  |      |     |     |     |
| ------------- | ---------- | --------------------- | --------------- | --------------------- | --- | --- | --- | ---- | --- | --- | --- |
|               |            |                       |                 |                       |     |     | 1   | 2 }. |     |     |     |
| 2.2.2 Voters. | The set of | voters is denoted by𝑉 | = {𝑣 ,...,𝑣 𝑛}, |                       |     |     |     |      |     |     |     |
1
2.3 ParticipatoryBudgetingwithPartialBallots
whereeachvotersubmitsherpreferencesonthepotentialprojects.
Weconsiderapproval-basedprocesses,inwhichtheballotofavoter Recallthatweareinterestedinsituationsinwhichnotallvoters
correspondstoasubsetofthesetofprojects(i.e.,voter𝑣 𝑖 submits providecompleteballots.Inaballotwith𝑚candidatesapartial
anapprovalballot,alsodenotedby𝑣 𝑖,suchthat𝑣 𝑖 ⊆𝑃). voteiscasewherevotergivespreferencesonlyover𝑗 candidates,
3

where1≤ 𝑗 <𝑚[12].Ourgoalistocreateandstudyalgorithms Offlinesetup-Analgorithmfortheofflinesetupoperatesasfol-
|     |     |     |     |     |     | lows:first,foreachvoter𝑣 | ∈𝑇𝑉,thealgorithmchooses𝑘projects |     |     |
| --- | --- | --- | --- | --- | --- | ------------------------ | -------------------------------- | --- | --- |
that,whengivenapartialballotasaninput,willproduceoutput
asallvotershavingcompletelyfilledouttheirballots.Specifically, ofitschoice(possiblybytakingintoconsiderationtheballotsof
weassumethateachvoterisassociatedwithasetofapproved 𝐿𝑉,intuitivelyassumingsomesimilaritybetweenvotersin𝐿𝑉 and
candidates,asetofdisapprovedcandidates,andasetofcandidates 𝑇𝑉 in𝐼)andmovestheminto𝐸,inawaythat𝐼1agreeswith𝐼.
wherethevoter’sstandisunknown.Formally,voter𝑣 ∈{𝑣 ,...,𝑣 𝑛} Then,thealgorithmhastopredicttherestoftheballots-𝐻 for
1
| hasanapprovalset𝐴 |     | ⊂𝑃,adisapprovalset𝐷 |     | ⊂𝑃            |            | eachvoter𝑣 | ∈𝑇𝑉. |     |     |
| ----------------- | --- | ------------------- | --- | ------------- | ---------- | ---------- | ---- | --- | --- |
|                   |     | 𝑣                   |     | 𝑣             | andahidden |            |      |     |     |
| setdenotedby𝐻     |     | 𝑃.Notethat𝐴         | +𝐷  | +𝐻 𝑃.Wedenote |            |            |      |     |     |
𝑣 ⊂ 𝑣 𝑣 𝑣 = Onlinesetup-Analgorithmfortheonlinesetupoperatesas
|     |     |     |     |     |     | follows:first,foreachvoter𝑣 |     | ∈𝑇𝑉,thealgorithmproceedsin𝑘it- |     |
| --- | --- | --- | --- | --- | --- | --------------------------- | --- | ------------------------------ | --- |
thatthemergeofapprovedanddisapprovedcandidatessetsisan
exposedset𝐴 𝑣∪𝐷 𝑣 =𝐸 𝑣 ,𝐸 𝑣 ∈𝑃. erations,whereineachiterationthealgorithmcanchoose1project
ofitschoice(possiblybytakingintoconsiderationtheballotsof𝐿𝑉
Example2.4. ConsideraninstanceofPBwithpartialballotswith aswellastheresultsofthepreviousiterations,intuitivelyassum-
3projects:𝑝 1,𝑝 2,and𝑝 3;andwith2voters:𝑣 1and𝑣 2.Letitbethat ingsomesimilaritybetweenvotersin𝑇𝑉 and𝐿𝑉 in𝐼
andusing
𝑣 1providesafullballotinwhichsheapprovesallprojects,while𝑣
|                                           |     |     |     |                | 2   | therevealedpreferencesofthepreviousiterations)andmovesit |     |     |     |
| ----------------------------------------- | --- | --- | --- | -------------- | --- | -------------------------------------------------------- | --- | --- | --- |
| providesapartialballotinwhichsheapproves𝑝 |     |     |     | 1,disapproved𝑝 |     |                                                          |     |     |     |
|                                           |     |     |     |                | 2   | into𝐸,inawaythat𝐼1agreeswith𝐼.Then,thealgorithmhas       |     |     |     |
anddoesnotprovideherpreferenceregarding𝑝
|     |     |     |     | 3.Wedenotesuch |     | to predict | the rest of the ballots | -𝐻 for each voter𝑣 | ∈ 𝑇𝑉. A |
| --- | --- | --- | --- | -------------- | --- | ---------- | ----------------------- | ------------------ | ------- |
asettingasfollows:𝑃 ={𝑝 ,𝑝 ,𝑝 },𝑉 ={𝑣 ,𝑣 },𝐸 ={𝑝 ,𝑝 ,𝑝 }, moreintuitiveexpositionofthesealgorithmstaskscouldbethe
|     |     | 1 2 3 |     | 1 2 1 | 1 2 3 |     |     |     |     |
| --- | --- | ----- | --- | ----- | ----- | --- | --- | --- | --- |
𝐴 = {𝑝 ,𝑝 ,𝑝 }, 𝐷 = ∅, 𝐻 = ∅, 𝐸 = {𝑝 ,𝑝 }, 𝐴 = {𝑝 }, following:imagine𝑛votersprovidingtheirapprovalballotswhere,
| 1   | 1 2 3 1 | 1   | 2   | 1 2 | 2 1 |     |     |     |     |
| --- | ------- | --- | --- | --- | --- | --- | --- | --- | --- |
𝐷 ={𝑝 },𝐻 ={𝑝 }. pictorially,eachvoterhas𝑚cards,onecardforeachproject,on
| 2 2 | 2 3 |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
whichthevoterwritestheirapproval/disapprovalpreference.Then,
2.4 AlgorithmicTasks somevoters(thosein𝐿𝑉)showalltheircards;whileothers(those
in𝑇𝑉)initiallydonotshowtheircardsatall.Intherandomsetting,
Weconsiderthreeslightlydifferentalgorithmictasks,correspond-
eachsuchvotershows𝑘cardsatrandomtothealgorithm;inthe
ingtodifferentwaysinwhichvotersmayinteractwithourenvi-
sionedapplication,ortodifferentassumptionsregardingthepartial offlinesetting,thealgorithmcanchoose,foreachsuchvoter,aset
of𝑘cardsthatthealgorithmwantstosee;andintheonlinesetting,
ballots.Inallthreevariants,weassumesomeidealinstanceofPB
containing𝑛voters,allofwhichprovidefullballots;denotethis thealgorithmcaniterativelyasksforafirstcard,asecondcard,
untila𝑘thcard,toseefromeachsuchvoter.Finally,thealgorithm
instanceby𝑖𝑑𝑒𝑎𝑙.Intuitively,inthealgorithmictasksweconsider,
ourgoalistoestimate𝑖𝑑𝑒𝑎𝑙,howeverthealgorithmswedesign shallpredictallofthehiddencards.Illustrationsofthedifferent
donothaveaccessto𝑖𝑑𝑒𝑎𝑙 butonlytoaPBinstancewithpartial settingscanbeseeninFigure2.
with𝑖𝑑𝑒𝑎𝑙
| ballotsthatagrees |     | (aPBinstancewithpartialballots |     |     |     |     |     |     |     |
| ----------------- | --- | ------------------------------ | --- | --- | --- | --- | --- | --- | --- |
issaidtoagreewithsomePBinstancewithfullballotsifallthe
3 SOLUTIONARCHITECTURE
providedpreferencesagree;intuitively,ifitispossibletocomplete
thepartialinstancetobeequaltotheidealinstance). Inthissectionwediscussthearchitectureofoursolution,which
consistsofthreemodules:samplingmodule,predictionmodule
Example 2.5. Consider an ideal instance 𝐼 with projects 𝑃 = andvotingruleimplementation.Agraphicalrepresentationofour
{𝑝 ,𝑝 ,𝑝 ,𝑝 }andonevoter𝑣 1whereherexposedset𝐸 ={𝑝 ,𝑝 }. solutionarchitectureisgiveninFigure3.
| 1 2 3 | 4   |     |     |     | 1 2 4 |     |     |     |     |
| ----- | --- | --- | --- | --- | ----- | --- | --- | --- | --- |
ConsideraPBinstancewithpartialballots,denotedby𝐼1,with Asmentioned,weproposeacomputationalsolutionforPBwith
| onevoter𝑣 | ′ thatprovidesapartialballot,andlet𝐴 |     |     |     | {𝑝       |                                                         |     |     |     |
| --------- | ------------------------------------ | --- | --- | --- | -------- | ------------------------------------------------------- | --- | --- | --- |
|           |                                      |     |     | 1   | = 2 }and | partialballots,wheresomevotersdonotcompleteballots.Aswe |     |     |     |
1
𝐷 =𝑝 1.Then,𝐼1agreeswith𝐼. wanttocontroltheamountofinformationtogatherfromvoters,
1
wedefinealevelofpartialityashowsparseisourPBandhowwe
Todescribeouralgorithmictasks,considersomeidealinstance dividethelevelofpartialityto𝐿𝑉 and𝑇𝑉.
| 𝐼 withaset𝑉 | of𝑛voters.Then,consideraninstanceofPBwith |     |     |     |     |     |     |     |     |
| ----------- | ----------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- |
partialballots𝐼1thatisconstructedbyfirstpartitioningtwogroups
ofvotersLearningVoters-𝐿𝑉 andTargetVoters-𝑇𝑉.Intuitively,𝐿𝑉 3.0.1 Partialitylevel,SamplingDegreeandLVDegree. ThePartial-
arevotersthatalreadyprovidedtheirfullballotsand𝑇𝑉 itylevelofaPBdenotedbysampledegreeasthepercentageofdata
arevoters
collectingfromthevotersparticipateinPB.WedenoteLVDegree
| that provides | partial | ballots. Consider | the | voters in𝑇𝑉 | and set |     |     |     |     |
| ------------- | ------- | ----------------- | --- | ----------- | ------- | --- | --- | --- | --- |
asthelevelofcollecteddatathatassociatedwith𝐿𝑉.Asthelevel
theminitiallysothat𝐸=∅;i.e.,suchthattheydonotprovideany
ofsamplingDegreeincreases,votersarerequestedtoprovidemore
preference.Theoverarchinggoalofouralgorithmsistoestimate𝐼
dataandasthelevelofLVDegreeincreasesthe|𝐿𝑉|isincreases.
from𝐼1.Eachofthethreealgorithmictasksweconsiderdifferentiate
bytheallowedoperationsthatthealgorithmcanperformon𝐼1to
reachthisgoal,asdescribednext: Example3.1. WhereSamplingDegreeis1itmeansthatthePB
Randomsetup-Analgorithmfortherandomsetupoperates iscomplete,allvotersfilledtheirballots.WhenSamplingDegreeis
asfollows:first,foreachvoter𝑣 ∈𝑇𝑉,thealgorithmchooses𝑘 0.5andLVDegreeis1itmeansthat50%ofvotesareknownandall
projectsuniformlyatrandomandmovestheminto𝐸,inawaythat
ofthemarepartoffullindividualballots.WhenSamplingDegreeis
| 𝐼1agreeswith𝐼 | (possiblydifferent𝐸foreachvoter𝑣 |     |     |     | ∈𝑇𝑉).Then, |     |     |     |     |
| ------------- | -------------------------------- | --- | --- | --- | ---------- | --- | --- | --- | --- |
0.5andLVDegreeis0.1itmeansthat50%ofvotesareknownand
thealgorithmhastopredicttheresttheballot-𝐻 foreachvoter 10%ofthemarepartoffullindividualballotsand90%areequally
| 𝑣 ∈𝑇𝑉. |     |     |     |     |     | dividedbetween𝑇𝑉. |     |     |     |
| ------ | --- | --- | --- | --- | --- | ----------------- | --- | --- | --- |
4

| (a) The random   | setting -  | the algorithm |     |     |     |     |
| ---------------- | ---------- | ------------- | --- | --- | --- | --- |
| chooses randomly | 𝑘 projects | from each     |     |     |     |     |
votertoexposed.
(b)OfflineSetting-thealgorithmchoosesasetof𝑘projectsthat
itasksforeachvotertoexpose.
Figure3:Architecture:startingwithsamplingalgorithm-
asthewaywecollectpreferencesfromvoters-gainpartial
ballot;thenfillingthemissingvotesbyapplyingprediction
module;implyingvotingruletooutputthepredictedwin-
ningbundle.
|     |     |     | 3.1.1 AlgorithmsfortheRandomSetup. |     | Recallthatanalgorithm |     |
| --- | --- | --- | ---------------------------------- | --- | --------------------- | --- |
forthissetupcannotchoosethe𝑘projectsforwhichthevotersin
𝑇𝑉 providepreferencesfor;thus,theonlyoperationthatsuchan
algorithmdoesistopredicttheremainingpreferencesofthevoters
|     |     |     | in𝑇𝑉,basedonthepreferencesofvotersin𝐿𝑉 |                                                |     | andthepreferences |
| --- | --- | --- | -------------------------------------- | ---------------------------------------------- | --- | ----------------- |
|     |     |     | in𝐸 =(𝐸                                | ,...,𝐸 𝑛)bypredictionmethodsdiscussedinSection |     |                   |
|     |     |     | 𝑇𝑉                                     | 1                                              |     |                   |
2.1.
|     |     |     | 3.1.2 AlgorithmsfortheOfflineSetup. |     | Recallthatanalgorithmfor |     |
| --- | --- | --- | ----------------------------------- | --- | ------------------------ | --- |
(c)OnlineSetting-thealgorithmchoosesiteratively𝑘projects
|                                 |     |     | thissetupfirsthastochoose,foreach𝑣 |     | ∈𝑇𝑉,aset𝑘 |            |
| ------------------------------- | --- | --- | ---------------------------------- | --- | --------- | ---------- |
| thatitasksforeachvotertoexpose. |     |     |                                    |     |           | ofprojects |
to“reveal”(tosetas𝐸);and,onlythen,topredicttheremaining
preferencesofthevotersin𝑇𝑉,basedonthepreferencesofvoters
Figure2:AlgorithmicTasks.
|     |     |     | in𝐿𝑉 and | the preferences | in 𝐸 𝑇𝑉 = (𝐸 ,...,𝐸 | 𝑛) by prediction |
| --- | --- | --- | -------- | --------------- | ------------------- | ---------------- |
1
methodsdiscussedinSection2.1.
• Revealingbypopularity
3.1 AlgorithmicSolutions Herethealgorithmchoosesthetop𝑘popularprojectsofthe
|     |     |     | votersin𝐿𝑉 | andsetthe𝐸ofeachvoter𝑣 |     | ∈𝑇𝑉 |
| --- | --- | --- | ---------- | ---------------------- | --- | --- |
Wedescribeseveralalgorithmicsolutionsforeachofthesetupswe toinclude
consider,namelyfortherandomsetup,theofflinesetup,andthe exactlythose.(I.e.,itsets𝐸={𝜎 1 ,...,𝜎 𝑘}foreach𝑣 ∈𝑇𝑉.)
onlinesetup. • Revealingbyconsensus
5

Herethealgorithmchoosesthe𝑘projectsmostinconsensus around10%ofprojectproposalswereapprovedineveryPB,the
| amongthevotersin𝐿𝑉 | andsetthe𝐸ofeachvoter𝑣 | ∈𝑇𝑉 |     |     |     |     |
| ------------------ | ---------------------- | --- | --- | --- | --- | --- |
exactpercentageisdetailedinTable1.
| toincludeexactlythose.(I.e.,itsets𝐸={𝛾 |     | ,...,𝛾 |     |     |     |     |
| -------------------------------------- | --- | ------ | --- | --- | --- | --- |
1 𝑘}foreach
| 𝑣 ∈𝑇𝑉.) |     |     | Table1:Descriptionofusedreal-worlddatasets. |     |     |     |
| ------- | --- | --- | ------------------------------------------- | --- | --- | --- |
• Revealingbycontroversiality
Herethealgorithmchoosesthe𝑘projectsleastinconsensus
|                                        |                        |           | PB          | Voters Projects | Budget Approvedproposals[%] |      |
| -------------------------------------- | ---------------------- | --------- | ----------- | --------------- | --------------------------- | ---- |
| amongthevotersin𝐿𝑉                     | andsetthe𝐸ofeachvoter𝑣 | ∈𝑇𝑉       |             |                 |                             |      |
|                                        |                        |           | Wola2022    | 9256 94         | 524020                      | 9.5  |
| toincludeexactlythose.(I.e.,itsets𝐸={𝛾 |                        | ,...,𝛾    |             |                 |                             |      |
|                                        |                        | 𝑚−𝑘 𝑚}for | Ursynow2022 | 6672 107        | 5614506                     | 10.7 |
each𝑣 ∈𝑇𝑉.)
|     |     |     | Wola2021         | 8647 107 | 465432  | 9.8  |
| --- | --- | --- | ---------------- | -------- | ------- | ---- |
|     |     |     | Praga-Polnoc2022 | 2614 90  | 2432952 | 12.5 |
Theintuitionforthisprocedureisthattheprojectsleastin
|     |     |     | Praga-Poludnie2022 | 10424 96 | 6643832 | 10.6 |
| --- | --- | --- | ------------------ | -------- | ------- | ---- |
consensuscorrespondtothoseprojectsthatarethehardest
|     |     |     | Wawer2021 | 4662 100 | 2493341 | 9.1 |
| --- | --- | --- | --------- | -------- | ------- | --- |
topredict.
|     |     |     | Bielany2020 | 8003 108 | 4321791 | 7.7 |
| --- | --- | --- | ----------- | -------- | ------- | --- |
|     |     |     | Wawer2022   | 5045 111 | 2807253 | 7.8 |
3.1.3 AlgorithmsfortheOnlineSetup. Recallthatanalgorithmfor Wola2023 6760 67 5663326 15.3
thissetupfirsthastochoose,foreach𝑣 ∈𝑇𝑉,aset𝑘 Targowe2022 4940 87 4585180 10.7
ofprojects
to“reveal”(tosetas𝐸);and,onlythen,topredicttheremaining
preferencesofthevotersin𝑇𝑉,basedonthepreferencesofvot-
Table2:Voter’sandproject’sattributesspace.
ersin𝐿𝑉 andthepreferencesin𝐸.But,incontrasttotheoffline
setting,thealgorithmcanchoosethese𝑘projectsadaptively.We
consideronewayofchoosingthe𝑘projectstoreveal,adaptively,
|     |     |     | Voter’sAttributes |     | Project’sAttributes |     |
| --- | --- | --- | ----------------- | --- | ------------------- | --- |
namely:adaptivecontroversial.Thealgorithmproceedsin𝑘itera-
|     |     |     |     | Age | Cost |     |
| --- | --- | --- | --- | --- | ---- | --- |
tions,whereineachiterationitcomputesthemostcontroversial
|     |     |     |     | Gender | Category |     |
| --- | --- | --- | --- | ------ | -------- | --- |
project.(Notethat,indeed,thisprocedureissimilartotherevealing
|     |     |     | VotingMethod |     | Populationsegments |     |
| --- | --- | --- | ------------ | --- | ------------------ | --- |
bycontroversialityprocedureoftheofflinesetting,howeverhere
itisdoneiterativelyandadaptively.)Afterusingtheadaptivecon-
troversialprocedure,wepredicttheremaininghiddenpreferences,
5 EVALUATION
usingpredictionmethodsdiscussedinSection2.1.
Inordertoevaluateourpredictionsmethodswedividedourdataset
3.1.4 VotingRule. Afterweperformthepredictingmodulewe into3sets:Train-set,Validation-setandTestset.
holdafullballot,wenowchosegreedyapprovalasavotingrule.
Inourresearchcontext,thetrain-setisthedatathatwecollected
AsdescribedinSection2.2.5forthisvotingsystem,eachvoteris
fromvotersregardingtheirvotes.Thevalidationsetispredefined
abletovoteforasmanycandidatesastheychoose,butcannot
setofvotesfromclosedsetofvoters,thesevotesareusedtotune
voteforthesamecandidatetwice.Thealgorithmthenbeginswith
thehyperparametersofamodel.Wedenotedthatthevalidation
thecandidatewhohasthemostnumberofvotesandselectsthem. setsize is15% ofeach data set. Thetest-set isthecollection of
Eachsubsequentcandidateischosenuntilthetotalnumberofvotes votesthatweusetoevaluateourmodel,thesevotesarethevotes
reachesthedesiredthreshold.Theaimofthissystemistomaximize
thatwedidnotcollectedfromthevoters.AsmentionedinTable4,
theamountof“approval”giventothechosencandidatesbythe
thePBdatasetsareimbalanced,thiscanleadtobiasedresultsand
voters[25].Hence,weoutputthepredictedwinningbundlewith
suboptimalperformanceofourpredictingmodels,asthemodelis
respecttoagivenbudget. morelikelytopredictthemajorityclass.Weaddressthisissueby
modifyingthemodellossfunctiontogivemoreweighttominority
4 DATASETS
classsamples.
Wehaveusedareal-worlddatasetscomingforapublicrepository, Wedivideourevaluationmethodsintotwosections:theclassifi-
namelyPabulib[10],apublicrepositoryfordataregardingreal- cationaccuracymetricsinwhichanalyzethefullpredictedballots
andBundleevaluationmetricsthatanalyzethefinalpredictedbun-
worldinstancesofparticipatorybudgeting,mainlyfromseveral
dle.
Europeancities.Inparticular,wehaveusedthedataconcerning
thePBprocessindifferentdistrictsfromWarsaw,Poland.Outof
5.1 ClassificationAccuracyMetrics
thisopenlibrarywecollectedtenPBthattookplacefrom2020to
2023.Table1detailstheamountofvoters,amountofprojectsand Toanalyzeouralgorithms,weconsideredavarietyofclassification
budgetforeachPB.Table2detailstheattributesofPB’svotersand accuracymetrics,namely:precision,recallandf1[20,23].They
projects.EachPBinstanceconsistvotersandprojects(theprojects measuretheamountofcorrectandincorrectclassificationandare
correspondtodifferentproposalstoimprovethedevelopmentof derivedfromconfusionmatrix.Theconfusionmatrixholdsthefol-
Warsawinseveraldomainssuchas,e.g.,education,environment lowingmeasures:TheacronymTP,FN,FP,andTNoftheconfusion
protection,publictransportation,etc.).Theproposalsarealsoaimed matrix cellsreferstothefollowing:TP=truepositive,thenum-
fordifferentsegmentsofthecitypopulation,e.g.children,adults, berofpositivecasesthatarecorrectlyidentifiedaspositive,FN
seniors,andpeoplewithdisabilities.Notethatacertainproposal =falsenegative,thenumberofpositivecasesthataremisclassi-
canconsistmultipletopicsandpopulationsegments.InallPBsthe fiedasnegativecases,FP=falsepositive,thenumberofnegative
percentageofvoter’sapprovedprojectproposalsisnaturallysmall, casesthatareincorrectlyidentifiedaspositivecases,TN=true
6

negative,thenumberofnegativecasesthatarecorrectlyidentified
asnegativecases[20,23].Precision,definedas𝑇𝑃/(𝑇𝑃 +𝐹𝑃),in
RScontextistheratioofthenumberofrelevantrecommended
itemstothetotalnumberofrecommendeditems[20,23].Recall,
definedas𝑇𝑃/(𝑇𝑃 +𝐹𝑁),istheratioofrelevantrecommended
itemstothenumberofrelevantitems.Thesetwometrics,sharean
inverserelationshipbetweenthem.Precisionandrecallarenotsen-
Figure4:TreatmentMatrix-pleaseseeSection6.
sitivetochangesindatadistributions.Aperfectmodelwillcapture
allpositiveexamples(Recall=1),andscoreasonlytheexamples
thatareinfact(Precision=1),fromananalyticalpointofview
itisdesirabletoincreaserecallwithoutsacrificingaccuracy.𝐹
1
datasetasdetailedinFigure4for50times.Weassumethatthemore
datawecollected,highersampledegreeinourcontext,thecloser
measurecombinesrecallandprecisionasharmonicmeanofthem,
𝐹 1 = (2∗𝑝𝑟𝑒𝑐𝑖𝑠𝑖𝑜𝑛∗𝑟𝑒𝑐𝑎𝑙𝑙)/(𝑝𝑟𝑒𝑐𝑖𝑠𝑖𝑜𝑛+𝑟𝑒𝑐𝑎𝑙𝑙) andissuitable wewillbetothetruerealballotresults.Inparticular,weassume
thattheFAscorewouldincreaseasthesampledegreeincrease
measureforanimbalanceddata[23].
andtheSDwoulddecreasethesampledegreeincreaseforeach
5.2 Bundleevaluationmetrics setupforeveryPB.Hence,weconductedasanitytesttocheckthis
assumption.
Eventually,wehaveinterestincomputingthebundleofwinning
Everyalgorithmicsetupholdsdifferentlevelofinterventionin
projectsthatwasdecidedbythevoters,i.e,thelistofprojectsthat
selectingtheprojectproposalstocollect;inthe’Random’setupthe
’won’andwouldbeimplemented.Asanevaluationmethodwe
algorithmhasnopoweratallinchoosingwhichprojectproposals
compared the bundle from the ’real’ votes to the bundle of the
preferences to collect, in the offline setups it has the power to
’predicted’votes.ThiscomparisonhasdonebycomputingtheSym-
choose𝐾 projectproposalsbasedongroupofvotersthatprovided
metricDistancebetweenthetherealbundle(rb)andthepredicted
fullballots(LVgroup)andfortheonlinesetupithasthepowerto
bundle(pb).
chooseprojectproposalsbasedonallvoterspreferencesitteratively.
5.2.1 SymmetricDistance. Symmetricdistance(SD)isadistance Weassumethatthemore’power’thealgorithmicsolutionholdthe
measurethatsatisfiesthepropertyofsymmetry,whichstatesthat betteritwouldperformbetter(higherFAscoreandlowerSD).
thedistancebetweentwopointsisthesameinbothdirections. Hence,foreveryPBwecomparedallsetupsandalgorithmic
Formally,giventwopointsxandy,aSDfunctionfsatisfiesthe solutionspersampledegree.Additionally,weimplementedaper-
equation f(x,y) = f(y,x). Consider several toy examples: The SD formancetestinwhichwecomparedoursolutionswithanaive
between𝑟𝑏 = {1,2,3} and𝑝𝑏 = {2,1,3} is 0. The SD between samplingprocedure.Thissamplingprocedureisthecasewhere
𝑟𝑏 ={1,2,3}and𝑝𝑏 ={1,3,4}is1.TheSDbetween𝑟𝑏 ={1,2,3} LVdegreeisequalto1foracertainsampledegree.Notethatin
and𝑝𝑏 ={1,4,5}is4. samplingprocedureonlypartofcommunity(sampledegreetobe
exact)sharetheirpreferences,incontrasttoourproposedsolutions
5.2.2 FractionalAllocationscore. Anothermetricweusetoeval-
whereeveryvoterhasatleast𝐾 projectproposalstoshareher
uatethebundleis’FractionalAllocation’(FA)Score;Wedenote
opinionon.Inordertogenerateitwerandomlysampledvotersfor
FAscoreasthesumcostsofprojectsthatwerepredictedproperly
eachPBforeachsampledegreefor50timesandcalculateitsFA
dividedbythecostlimit-budget.
andSD.
Definition5.1(FractionalAllocation(FA)Score). Wedefinethe
fractionalallocationscoretobe:𝐹𝐴=
𝐵
𝜆,𝜆=(cid:205)
𝑝∈𝑝𝑏∩𝑟𝑏
𝑐𝑜𝑠𝑡(𝑝) 7 RESULTS
Inthissectionwedescribeanddiscussourresultsfortheprediction
6 EXPERIMENTS
module, for the sampling module, and for the architecture as a
Inthissectionwedescribetheexperimentsweconductedonthe whole.
real-worlddata-setspresentedinTable1.Webeganwithdefining FirstweperformedasanitychecktotesthowthesampleandLV
thepartialitylevelsoftheexperiment,wedefinedmultiplelevelsin degreeseffectonFAscoresandSD.WecalculatedtheaverageFA
ordertoconductseveralexperimentswithdifferentSampledegree scoresandSDforallPB’sforeachcombinationofsampledegree
andLVdegreeasmentionedinSection3.0.1.Therangeofsample and LV degree as described in Figure 4. The sanity test results,
degreesis0.1,0.15,0.3,0.5,0.7and0.9andtherangeofLVdegrees showninFigures5and6,showedthatinmostLVdegrees,asthe
is0.1,0.2,0.3,0.5,0.7,0.9and1.WhenLVdegreeisequalto1itrep- sampledegreeincreasestheFAscoreincreasesaswellandtheSD
resentthecaseofsamplesizeofthespecificSampleDegree.After isdecreases,asassumed.
weestablishedtheframeoftheamountsofinformationwewould Furthermore,itcanbeobservedthatastheLVdegreeincreases
collectfromthevoters,weusedeachofoursamplemodules(Ran- theFAscore/SDincreases/decreasesaswell,bymeansthepredic-
dom,Offline-popularity,Offline-controversial,Offline-consensus tionmodulesperformbetterwhenalargergroupofvotersprovide
andOnline)togatherthepreferencesfromvoters.Weperformed theirfullballots.
eachsamplemoduleonallsampledegree-LVdegreecombination InFigures7-12wecanseetheFAscoresperformanceofevery
for20times.ThisprocedurewasexecutedonallPBdatasets. setupasfunctionofLVdegreeandsampledegreeincludingacom-
Thenweperformedeachpredictionmoduleontheeachoffamily parisontosamplingmethod(LVdegreeequalsto1).Itseemsthatin
ofsampledegreeandLVdegree.Wedidthisprocedureonevery somesettingssomeofoursolutionssucceedbetterthanasampling
7

scores,Classification-onlineandClassification-offline-popularity
setupsperformbestforallsampledegrees.
8 CONCLUSIONSANDOUTLOOK
Wehaveproposedtheuseoftechniquesfrommachinelearning
andrecommendationsystemstotackletheinformationoverload
probleminparticipatorybudgeting.Technically,wehavedeveloped
amoreofPBwithpartialballotsthatisusefulforourcontext,de-
signedseveralalgorithmicsolutionsfordifferentspecificprediction
settings,andreportedontheresultsofcomputer-basedsimula-
tionsshowingthehighqualityofpredictionwithrespecttovoter
Figure5:Sanitytest-heatmapofFAscoresasfunctionof ballotsandthewinningbundlesthatthealgorithmsachievefora
SampledegreeandLVdegree. real-worlddata.Weconductedourexperimentson10real-world
PBandeliminatedsomepreferencestosimulatePBwithpartial
ballots.Thiseliminationofpreferenceswereconductedundercon-
trolledandstructuredmanner,definedassamplingmodule.After
wecreatedthesepartialballotsweimplementedpredictionmodule
topredictthemissingpreferences.Thenwecalculatedthewinning
bundleusinggreedyapprovalvotingrule.Weevaluateoursampling
andpredictionmodulesbycomparingthewinningbundlestothe
realones.Thecomparisonweredefinedbysymmetricdistanceand
FractionalAllocationscore,asameasureofhowgoodthebudget
wasallocatedinthepredictedwinningballot.Exceptfromcom-
paringourownsolutionsbetweenthemselves,wecomparedthem
toanaivesamplingmethod.Wefoundthatsomeofoursolutions
performbetterfromsamplingmethod.Hence,althoughtakinga
Figure6:Sanitytest-heatmapofSDasfunctionofSample sampleofPBcommunityandextractwinningbundleoutofit’s
degreeandLVdegree. preferencesisquiteeasyandperformsrelativelygood,wepropose
solutionthattakeintoaccountallofPB’svotersandperformsbet-
terthansamplingmethods.So,oursolutionspermitallpotential
method.Specifically,forsampledegreeequalsto0.1(Figure7)all
votersinaPBtoexpresstheiropinionsregardingprojectproposals
solutionsexceptMF-online,MF-offline-popularityandFM-online
andprovideasolutiontotheinformationoverloadproblem.
producehigherFAscoresthansamplingmethod.Specificallythe
Someavenuesforfutureresearcharethefollowing:
Classification-onlineandClassification-off-popularitysetupsfor
sample deg equals to 0.1 perform better than sampling method • Adifferent,somewhatstrongersettingmaycorrespondto
forsampledegreeequalsto0.3.InFigure8itseemsthatourso- algorithmsthatinitiallygetaninstanceofPBwithpartial
lutionsperformnotasgoodasthesamplingmethod,exceptfrom ballotswhereallvoterpreferencesarehidden(i.e.,where
Classification-onlineandClassification-off-popularity.InFigure9 𝑇𝑉 =𝑉 and𝐸=∅forall𝑣 ∈𝑇𝑉).Designingandanalyzing
wecanseethatmoreofoursolutionsperformbetterorgoodas algorithms for this setting is of practical importance, as,
goodasthesamplingmethod,exceptfromClassification-onlineand inherently,aPBprocessstartswithonlycompletelyempty
Classification-off-popularity.InFigure10weseethattherandom ballots.Fromatechnicalpointofview,thiswouldnaturally
setups,forallpredictionmodules,outperformsandachievedrela- allow the algorithm consider more complex correlations
tivelyhighFAscores.Additionally,theClassification-off-popularity acrosstheelectorate.
gainedthemaximalFAscore,weachieveditforcollectinghalfof • Amoreinteractivesettingthatisworthconsideringmay
thevotes.Asforsampledegreeequalsto0.7and0.9itisnotsurpris- bethefollowing:first,thevoterrevealssomeofherpref-
ingthatoursolutionsgainedhighFAscores.Throughallsample erence,afterwhichthealgorithmestimatestherestofthe
degreesthesetupsthatperformbest,producethehigherFAscores, ballot(or,alternatively,onlythepreferencesofthevoter
aretheClassification-onlineandClassification-offline-popularity regardingsomefurtherprojectsnotyetrevealed).Then,the
setups,especiallyinthe0.1,0.15and0.3sampledegrees.Forhigher voterhasthepossibilitytoexaminethepredictionsdone
samplingdegreesallofoursolutionsperformbetterorgoodas bythealgorithmandto“correct”someofthem,inwhich
samplingmethods.Asweassumed,therandomsamplingmodule casethealgorithmcanfurtherupdateitsestimatesregarding
performworsethantheofflineandonlinesamplingmodules.Asfor theremainingprojects.Suchaninteractivecommunication
thepredictionmodules,itisshownthattheclassificationtechnique betweenavoterandtheenvisionapplicationmayleadto
performsbetterthantheRStechniques. resultsofhigherquality.
InFigures13-18representtheSDofeverysetupasfunctionof • WhileherewehaveconsideredthequitestandardPBsetting
LVdegreeandsampledegreeincludingacomparisontosampling ofapproval-basedcombinatorialPB,analyzingasimilarRS-
method. We see quite the same trend as we saw for for the FA orientedapproachfordifferentsettingsofPB(inparticular,
8

thoseinthesurveyofAzizandShah[2])isanaturalavenue APPENDIX
forfutureresearch. Weprovidesomefurtherplotsintheappendix.Figures7-12de-
• Whileweproposedcertainapproachestoaddressthepredic- scribetheFAscoresthatwereproducedforeverycombination
tionmodule,itwouldbeinterestingtoimplyothermachine of the algorithmic solutions, prediction module, LV degree and
learningtechniquestopredictvoter’sballot. sampledegreeasdescribeinFigure4.Theseheatmapsenableus
tocomparetheFAscoresbetweenthealgorithmicsolutions(ran-
REFERENCES
dom,offline-popularity,offline-consensus,offlinecontroversyand
[1] HarisAziz,BartonLee,andNimrodTalmon.2017.Proportionallyrepresentative online)andbetweenthepredictionmodule(MF,FMandbinary
participatorybudgeting:Axiomsandalgorithms.arXivpreprintarXiv:1711.08226
(2017). classification).Furthermore,wecomparebetweenoursolutions
[2] HarisAzizandNisargShah.2021. Participatorybudgeting:Modelsandap- acrossallLVdegreelevelstosamplingsolution,whereonlypartof
proaches.InPathwaysBetweenSocialScienceandComputationalSocialScience.
thevoterstakenintoaccount,itisthecasewhereLVdegreeequals
Springer,215–236.
[3] GerdusBenade,SwapravaNath,ArielDProcaccia,andNisargShah.2021.Pref- to1,whereeachfigurereferstodifferentsampledegree.
erenceelicitationforparticipatorybudgeting.ManagementScience67,5(2021), Figures13-18describethesamecomparisonsshownabovebut
2813–2827.
forSymmetricdistances(SD).
[4] JesúsBobadilla,FernandoOrtega,AntonioHernando,andAbrahamGutiérrez.
2013.Recommendersystemssurvey.Knowledge-basedsystems46(2013),109–
132.
[5] FelixBrandt,VincentConitzer,andUlleEndriss.2012. Computationalsocial
choice.Multiagentsystems2(2012),213–284.
[6] RobinBurke.2002.Hybridrecommendersystems:Surveyandexperiments.User
modelinganduser-adaptedinteraction12,4(2002),331–370.
[7] YvesCabannes.2004. Participatorybudgeting:asignificantcontributionto
participatorydemocracy.Environmentandurbanization16,1(2004),27–46.
[8] IvánCantador,MaríaECortés-Cediel,MiriamFernández,andHarithAlani.2018.
What’sgoingoninmycity?recommendersystemsandelectronicparticipatory
budgeting.InProceedingsofthe12thACMConferenceonRecommenderSystems.
219–223.
[9] TianqiChenandCarlosGuestrin.2016.Xgboost:Ascalabletreeboostingsystem.
InProceedingsofthe22ndacmsigkddinternationalconferenceonknowledge
discoveryanddatamining.785–794.
[10] NimrodTalmonDariuszStolicki,StanisławSzufa.2020.pabulibanopenPArtici-
patoryBUdgetingLIBrary.http://http://pabulib.org.
[11] AngelaEdmundsandAnneMorris.2000.Theproblemofinformationoverload
inbusinessorganisations:areviewoftheliterature. Internationaljournalof
informationmanagement20,1(2000),17–28.
[12] PeterEmerson.2013.TheoriginalBordacountandpartialvoting.SocialChoice
andWelfare40,2(2013),353–358.
[13] WulfGaertner.2009. Aprimerinsocialchoicetheory:Revisededition. Oxford
UniversityPress.
[14] DietmarJannach,MarkusZanker,AlexanderFelfernig,andGerhardFriedrich.
2010.Recommendersystems:anintroduction.CambridgeUniversityPress.
[15] YehudaKoren,RobertBell,andChrisVolinsky.2009.Matrixfactorizationtech-
niquesforrecommendersystems.Computer42,8(2009),30–37.
[16] BlerinaLika,KostasKolomvatsos,andStathesHadjiefthymiades.2014.Facing
thecoldstartprobleminrecommendersystems.ExpertSystemswithApplications
41,4(2014),2065–2073.
[17] IanMDLittle.1952. Socialchoiceandindividualvalues. JournalofPolitical
Economy60,5(1952),422–432.
[18] TomMMitchellandTomMMitchell.1997.Machinelearning.Vol.1.McGraw-hill
NewYork.
[19] SteffenRendle.2010.Factorizationmachines.In2010IEEEInternationalconference
ondatamining.IEEE,995–1000.
[20] FrancescoRicci,LiorRokach,andBrachaShapira.2011. Introductiontorec-
ommendersystemshandbook. InRecommendersystemshandbook.Springer,
1–35.
[21] JBenSchafer,DanFrankowski,JonHerlocker,andShiladSen.2007.Collaborative
filteringrecommendersystems.InTheadaptiveweb.Springer,291–324.
[22] JBenSchafer,JosephKonstan,andJohnRiedl.1999.Recommendersystemsin
e-commerce.InProceedingsofthe1stACMconferenceonElectroniccommerce.
158–166.
[23] GunnarSchröder,MaikThiele,andWolfgangLehner.2011.Settinggoalsand
choosingmetricsforrecommendersystemevaluations.InUCERSTI2workshopat
the5thACMconferenceonrecommendersystems,Chicago,USA,Vol.23.53.
[24] GuyShaniandAselaGunawardana.2011.Evaluatingrecommendationsystems.
InRecommendersystemshandbook.Springer,257–297.
[25] NimrodTalmonandPiotrFaliszewski.2019.Aframeworkforapproval-based
budgetingmethods.InProceedingsofAAAI’19,Vol.33.2181–2188.
[26] ChenWang,ChengyuanDeng,andSuzhenWang.2020.Imbalance-XGBoost:
leveragingweightedandfocallossesforbinarylabel-imbalancedclassification
withXGBoost.PatternRecognitionLetters136(2020),190–197.
[27] Yueping Zheng and Hindy Lauer Schachter. 2017. Explaining citizens’ E-
participationuse:Theroleofperceivedadvantages.PublicOrganizationReview
17,3(2017),409–428.
9

Figure11:HeatmapofFAforSampledegree=0.7. Figure7:HeatmapofFAforSampledegree=0.1.
Figure12:HeatmapofFAforSampledegree=0.9. Figure8:HeatmapofFAforSampledegree=0.15.
Figure13:HeatmapofSDforSampledegree=0.1.
Figure9:HeatmapofFAforSampledegree=0.3.
Figure14:HeatmapofSDforSampledegree=0.15.
Figure10:HeatmapofFAforSampledegree=0.5.
10

Figure15:HeatmapofSDforSampledegree=0.3. Figure17:HeatmapofSDforSampledegree=0.7.
Figure16:HeatmapofSDforSampledegree=0.5. Figure18:HeatmapofSDforSampledegree=0.9.
11