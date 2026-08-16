---
conversion_metadata:
  converted_at: "2026-07-21T08:13:24Z"
  converter_tool: "markitdown"
  converter_version: "0.1.6"
  source_pdf: "Qu et al.pdf"
  source_pdf_sha256: "21e23218ecfbf7c56c80e8192c0b33a147a6ee7bebfd8cbcbfa7163c4141a8fe"
  page_count: 10
  markdown_char_count: 124421
---

<!-- PAGE-AWARE EXTRACTION (via pdfminer.six) -->

<!-- PAGE 1 -->

Budgeted Embedding Table For Recommender Systems

Yunke Qu
The University of Queensland
Brisbane, Australia
yunke.qu@uq.net.au

Quoc Viet Hung Nguyen
Griffith University
Gold Coast, Australia
henry.nguyen@griffith.edu.au

Tong Chen
The University of Queensland
Brisbane, Australia
tong.chen@uq.edu.au

Hongzhi Yin∗
The University of Queensland
Brisbane, Australia
h.yin1@uq.edu.au

ABSTRACT
At the heart of contemporary recommender systems (RSs) are latent
factor models that provide quality recommendation experience to
users. These models use embedding vectors, which are typically of a
uniform and fixed size, to represent users and items. As the number
of users and items continues to grow, this design becomes ineffi-
cient and hard to scale. Recent lightweight embedding methods
have enabled different users and items to have diverse embedding
sizes, but are commonly subject to two major drawbacks. Firstly,
they limit the embedding size search to optimizing a heuristic bal-
ancing the recommendation quality and the memory complexity,
where the trade-off coefficient needs to be manually tuned for ev-
ery memory budget requested. The implicitly enforced memory
complexity term can even fail to cap the parameter usage, mak-
ing the resultant embedding table fail to meet the memory budget
strictly. Secondly, most solutions, especially reinforcement learn-
ing based ones derive and optimize the embedding size for each
each user/item on an instance-by-instance basis, which impedes the
search efficiency. In this paper, we propose Budgeted Embedding
Table (BET), a novel method that generates table-level actions (i.e.,
embedding sizes for all users and items) that is guaranteed to meet
pre-specified memory budgets. Furthermore, by leveraging a set-
based action formulation and engaging set representation learning,
we present an innovative action search strategy powered by an
action fitness predictor that efficiently evaluates each table-level
action. Experiments have shown state-of-the-art performance on
two real-world datasets when BET is paired with three popular
recommender models under different memory budgets.

CCS CONCEPTS
• Information systems → Recommender systems.

∗Corresponding author

Permission to make digital or hard copies of all or part of this work for personal or
classroom use is granted without fee provided that copies are not made or distributed
for profit or commercial advantage and that copies bear this notice and the full citation
on the first page. Copyrights for components of this work owned by others than the
author(s) must be honored. Abstracting with credit is permitted. To copy otherwise, or
republish, to post on servers or to redistribute to lists, requires prior specific permission
and/or a fee. Request permissions from permissions@acm.org.
WSDM ’24, March 4–8, 2024, Merida, Mexico
© 2024 Copyright held by the owner/author(s). Publication rights licensed to ACM.
ACM ISBN 979-8-4007-0371-3/24/03. . . $15.00
https://doi.org/10.1145/3616855.3635778

KEYWORDS
recommender systems, neural architecture search

ACM Reference Format:
Yunke Qu, Tong Chen, Quoc Viet Hung Nguyen, and Hongzhi Yin. 2024.
Budgeted Embedding Table For Recommender Systems. In Proceedings of the
17th ACM International Conference on Web Search and Data Mining (WSDM
’24), March 4–8, 2024, Merida, Mexico. ACM, New York, NY, USA, 10 pages.
https://doi.org/10.1145/3616855.3635778

1 INTRODUCTION
Recommender systems (RSs) predict a user’s preference for an
item according to observed user-item interactions [51, 61] and
have been indispensable across numerous modern platforms such
as e-commerce and social media [23, 27, 64]. In contexts where
computations on local devices are essential, such as federated rec-
ommendation [39] and Internet of Things (IoT) services [16], the
need for RSs with small memory footprints becomes critical due to
highly constrained computational resources. The main bottleneck
for downsizing RSs is often the embedding table, which represents
users and items with distinct embedding vectors to facilitate pair-
wise similarity computation. As such, the size of the embedding
table can quickly exhaust the available memory, posing a significant
challenge to achieving scalable and resource-friendly RSs.

Such memory bottleneck is attributed to conventional embed-
ding tables, which typically allocate fixed and uniform embedding
sizes to each user and item [8, 18]. Such a design may require an
excessive number of parameters in industry-scale applications, e.g.,
the benchmark recommender in [11] has more than 25 billion pa-
rameters in its embedding table and requires 100 GB memory. In this
regard, researchers have developed methods to achieve lightweight
embeddings while maintaining its expressiveness. One stream of
methods aim to prune redundant parameters of the embedding table.
For example, [37] proposed OptEmbed, a novel embedding sparsifi-
cation framework that prunes redundant embeddings by learning an
importance score for each feature. These methods mostly optimize
a loss function combining a recommendation term and a sparsity
regularizer. Apart from sparsification/pruning methods, another
line of works featuring reinforcement learning (RL) techniques
have also emerged. Those methods adopt an RL-based policy net-
work to search for the optimal embedding sizes for each user/item,
where the embedding sizes (i.e., actions) can be selected from an
action space consisting of either a predefined set of values [? ]
or a continuous range [41]. Similar to sparsification methods, the
reward functions in RL-based lightweight embedding approaches

---

<!-- PAGE 2 -->

WSDM ’24, March 4–8, 2024, Merida, Mexico

Yunke Qu, Tong Chen, Quoc Viet Hung Nguyen, & Hongzhi Yin

also bind the recommendation quality term with a memory com-
plexity penalty. By tuning a trade-off coefficient among the two
terms, they can adjust the regularization strength on the parameter
consumption, thus achieving the desired memory efficiency.

Despite the possibility of balancing performance and embed-
ding parameter size, these two types of methods are still away
from practical use for two reasons. Firstly, such a desired balance
is achieved by jointly optimizing an additional space complexity
constraint on top of the recommendation objective. For example,
in [18], this is formulated as the difference between the budgeted
embedding parameter size and the actual parameter consumption
of the compressed embedding table. However, such an implicit loss
term means that the resultant embedding table may not necessarily
meet the desired parameter budget every time [8]. Moreover, the
optimization quality is highly sensitive to the trade-off coefficient,
which needs to be heuristically tuned for each memory budget.

The second reason is that, to achieve optimal recommendation
performance under each memory budget, the embedding size is
decided on an instance-by-instance basis w.r.t. each user/item. Tak-
ing a recent RL-based method CIESS [41] as an example, a policy
network predicts the optimal action for every single user and item,
based on which the backbone RS is trained and evaluated to cal-
culate the reward, enabling training the policy network. On the
one hand, ideally, the policy network is expected to be iteratively
updated w.r.t. each instance (i.e., user/item), but this can be prohib-
itively inefficient given the large number of users and items. On
the other hand, performing only one update per batch/epoch leads
to slower convergence due to the aggregated nature of the reward
function, and may potentially result in inferior generalization [20].
In response to both challenges, we propose Budgeted Embedding
Table (BET) for RSs, an automated input embedding size search
paradigm that can efficiently generate size decisions and perform
optimization at the embedding table level. An overview of BET is
provided in Figure 1. To address the first challenge, we innovatively
propose a bounded sampler that draws embedding sizes for all
users/items from a collection of probabilistic distributions, with the
guarantee that the total parameter usage is capped. As the embed-
ding sizes for all instances in the embedding table are produced all
at once, we term this a table-level action. This strategy frees us from
the need for manually designing and tuning the implicit parameter
constraint in the reward/loss function, and allows us to enforce the
memory budget with a negligible cost.

To tackle the second challenge, we further pair the generated
table-level actions with a fitness prediction network to evaluate the
quality of those actions. Essentially, in each search iteration, after
sampling several table-level actions, we need to identify the ones
that promise high recommendation accuracy. A straightforward
solution is to greedily evaluate each candidate action by training
and evaluating a backbone RS from scratch with the suggested
embedding sizes [18, 41, 62? ], which apparently impedes efficiency.
One may think of a surrogate function [3, 8] that “predicts” the
fitness of each action, instead of explicitly evaluating it. Accurately
predicting the performance of the table-level actions is crucial yet
another major challenge in this regard, as either overestimating or
underestimating an action’s performance will eventually cause sub-
optimal embedding size decisions. To align with the evaluation of
table-level actions in BET, our fitness predictor innovatively utilizes

Figure 1: Overview of BET.

a set-based formulation of actions, and embeds each action with
DeepSets [59], where the learned high-quality action embeddings
can efficiently provide reliable performance feedback on each table-
level action. Furthermore, the set-based action representations can
be inductively learned, which is essential for our iterative search
algorithm that constantly generates unseen actions that need to be
evaluated.

To summarize, our work presents the contributions below:

• We identify the practicality bottlenecks of existing embed-
ding size search methods for lightweight RSs, namely the
implicit and non-scalable parameter size constraints for meet-
ing different memory budgets, and the inefficient embedding
size generation and evaluation for every instance.

• We propose BET, a novel table-level embedding size search
approach featuring an efficient action sampling strategy that
generates table-level actions for all users and items and a
DeepSets-based fitness prediction network that accurately
predicts their performance to reduce action evaluation costs.
• Extensive empirical comparisons have been carried out on
two real-world datasets by pairing state-of-the-art embed-
ding size search algorithms with various backbone RSs, which
confirm the advantageous efficacy of BET.

2 PRELIMINARIES
To provide a detailed research background, we hereby discuss rele-
vant research topics.

2.1 Deep Recommender Systems
Researchers have proposed numerous deep recommender mod-
els to capture the user-item relationships. The first line of deep
recommender systems are based on MLPs. For instance, Neural
Collaborative Filtering (NCF) [15] integrates a MLP with a matrix
factorization component to learn the two-way interactions between
users and items. AutoRec [45] uses an autoencoder to model the
user-item interactions in a low-dimensional hidden space and per-
form collaborative filtering. Lin et al. proposed a novel sequential
recommender system, Dual Contrastive Network [31] that gen-
erates self-supervised signals by considering both user and item
perspectives and refining representation learning through dual rep-
resentation contrastive learning. In addition to MLP-based meth-
ods, graph-based architectures [14, 53, 58] have also been studied.
For example, Neural Graph Collaborative Filtering (NGCF) [53]
extends traditional neural collaborative filtering by modeling user-
item interactions with graph convolution networks. LightGCN [14]

---

<!-- PAGE 3 -->

Budgeted Embedding Table For Recommender Systems

WSDM ’24, March 4–8, 2024, Merida, Mexico

takes inspiration from NGCF and simplifies it by removing its self-
connection, feature transformation and linear activation operations.
Another line of recommender systems are based on factorization
machines. Factorization Machines (FM) combine linear regression
with matrix factorization techniques to handle high-order interac-
tions [42]. [2] was also created to mine higher-order interactions.
Its deep variants - QNFM [7], DeepFM [13] and xLightFM [17]
have been proposed too. Moreover, numerous methods have been
proposed to leverage heterogeneous data for recommendation. For
instance, [6, 12, 25] have been devised to extract information from
user reviews or hashtags. [24, 52] have been proposed to exploit
videos and images for recommendation. Location information has
also been utilized to assist location-aware recommendations [4].

2.2 Lightweight Embeddings For

Recommenders

Various classes of works have investigated learning compressed
embeddings to provide a low-memory alternative to traditional
embedding tables in recommender systems [63]. For examples,
feature selection search methods [32, 36, 54] are trained to learn
importance scores, based on which they filter out the unimportant
feature fields. Embedding dimension search approaches [22, 34, 35,
40, 41, 62] improve traditional recommender systems with fixed and
uniform sizes by introducing mixed dimensions for each feature.
Quantization-based methods [5, 9, 10, 19, 21, 26] reduces the preci-
sion of numerical values and store the parameters with lower bits.
Feature hashing approaches [1, 11, 28, 30, 33, 46, 47, 57, 60] utilize
various hash tricks to transform input values to a smaller range,
thus compression the embedding table. Knowledge distillation tech-
niques train a smaller student model from a larger teacher model
and have been used to learn an embedding table of smaller sizes
from larger ones [55, 56]. BET achieves dynamic embedding sizes
and aims to find the optimal embedding size for each feature, so it
should be classified as a embedding dimension search approach.

3 PROPOSED APPROACH
In a nutshell, BET has three components: (1) a pre-trained backbone
recommender with a full-size embedding table 𝐺Θ (·) parameterized
by Θ; (2) an action fitness prediction network 𝐹Φ (·) parameterized
by Φ; and (3) a non-parametric action sampler 𝐻 (·). Figure 1 pro-
vides an overview of the workflow of BET. Under pre-specified
memory budgets, 𝐻 (·) samples actions from a set of probabilistic
distributions in each iteration. Each action specifies the embedding
sizes for all users and items. Afterwards, 𝐹Φ (·) estimates the fitness
of each action and selects the best action predicted. 𝐺Θ (·) is further
finetuned by adopting the embedding sizes in the chosen action,
and is then is evaluated on a hold-out dataset to obtain the actual
fitness score (i.e., recommendation quality) of the action. This facil-
itates the optimization of 𝐹Φ (·) by minimizing its prediction error,
thus leading us to optimal actions under each given memory budget
after 𝑇 iterations. In the remainder of this section, we unfold the
design of each component.

3.1 Recommender with Embedding Masking
Let U and V denote a set of users 𝑢 and items 𝑣, respectively. The
embedding table in the recommender maps each integer-valued user

or item IDs to a real-valued embedding vector e𝑛, where 𝑛 ∈ U ∪V
indexes either a user or an item. Note that we only separately use 𝑢
and 𝑣 to index users and items when they need to be distinguished,
e.g., when performing pairwise ranking. The vertical concatena-
tion of all embedding vectors forms the embedding table E of size
(|U| + |V |) × 𝑑𝑚𝑎𝑥 , where 𝑑𝑚𝑎𝑥 is the maximum/full embedding
size supported by 𝐺Θ (·). The embedding sizes are adjusted via a bi-
nary mask M ∈ {0, 1} ( | U |+| V | ) ×𝑑𝑚𝑎𝑥 , which is commonly adopted
for embedding sparsification in lightweight recommender systems
[35, 37, 41]. Each row m𝑛 in M is a mask vector corresponding to
user/item 𝑛. Given a searched embedding size 𝑑𝑛, we set the first
𝑑𝑛 elements of m𝑛 to ones the remaining 𝑑𝑚𝑎𝑥 − 𝑑𝑛 dimensions to
zeros. Then, we perform element-wise multiplication of the embed-
ding table E and the binary mask matrix M to adjust the embedding
sizes during embedding look-up, i.e., e𝑛 = (E ⊙ M) [𝑛] where [𝑛]
retrieves the 𝑛-th row of a matrix. M is adaptively updated based
on the sampled actions in every iteration. It is worth noting that,
in the deployment stage, only the heavily sparsified embedding
table E𝑠𝑝𝑎𝑟𝑠𝑒 = E ⊙ M will be stored, where the cost of storing
zero-valued entries can be negligible with sparse matrix storage
techniques [44, 49]. Once we obtain the sparse embedding vectors,
the recommender model 𝐺Φ (·) computes a preference score ˆ𝑦𝑢𝑣
representing pairwise user-item similarity:

ˆ𝑦𝑢𝑣 = 𝐺Θ (e𝑢, e𝑣),

(1)
where 𝐺Θ (·) can be any latent factor-based recommender model
that supports pairwise scoring.

𝑢 ∈ U, 𝑣 ∈ V,

For optimizing the recommender, we adopt Bayesian Personal-

ized Ranking (BPR) loss [43]:

L𝐵𝑃𝑅 =

∑︁

(𝑢,𝑣,𝑣′ ) ∈ D𝑡𝑟𝑎𝑖𝑛

− ln 𝜎 ( ˆ𝑦𝑢𝑣 − ˆ𝑦𝑢𝑣′ ) + 𝜂 ∥Θ∥2
2

,

(2)

where (𝑢, 𝑣, 𝑣 ′) ∈ D𝑡𝑟𝑎𝑖𝑛 represents the training samples where
user 𝑢 chooses item 𝑣 over item 𝑣 ′, while ˆ𝑦𝑢𝑣 and ˆ𝑦𝑢𝑣′ respectively
represent the predicted preferences that user 𝑢 has on items 𝑣 and
𝑣 ′. 𝜂 ∥Θ∥2
2 provides regularization to prevent overfitting, with a
scaling factor 𝜂. Our goal is to search for the optimal embedding
sizes for all users and items under strict memory budgets, hence
the overall objective is defined as follows:

min
Θ,Φ

L𝐵𝑃𝑅 s.t. 1 −

∥M∥1,1
(|U| + |V |) × 𝑑𝑚𝑎𝑥

≤ 𝑐,

(3)

where ∥M∥1,1 counts the number of ones, or equivalently retained
parameters in the binary mask, 𝑐 (0 < 𝑐 < 1) is the target sparsity
rate, i.e., the ratio between the numbers of active parameters in
sparsified and full embedding tables.

3.2 Budget-Aware Action Sampling
Hereby we introduce a novel table-level action sampling strategy. In
each search iteration, we randomly sample a set of candidate actions
Q = {𝑎1, ..., 𝑎𝑚 }. Each action assigns a continuous embedding size
𝑑𝑛 ∈ N+

to every user or item 𝑛 ∈ U ∪ V.

≤𝑑𝑚𝑎𝑥

As we aim to avoid optimizing the selected action towards an
implicit, manually tuned memory cost term, we propose to directly
draw a table-level action that: (1) makes all generated embedding
sizes conditioned on a certain distribution; and (2) ensures the
total parameter size of all embeddings is capped at the budgeted

---

<!-- PAGE 4 -->

WSDM ’24, March 4–8, 2024, Merida, Mexico

Yunke Qu, Tong Chen, Quoc Viet Hung Nguyen, & Hongzhi Yin

parameter consumption. In short, (1) essentially narrows the action
space to mitigate the difficulty of searching from a huge collection
of completely random actions, while (2) guarantees that the table-
level action strictly meets the memory budget in the first place.

To generate an action 𝑎, we first determine two probability distri-
butions 𝑃U and 𝑃V respectively for users and items. Meanwhile, to
introduce inductive bias to the action sampler, instead of resorting
to a fixed distribution throughout the search process, 𝑃U and 𝑃V
are both randomly chosen from a set of candidate distributions
with on-the-fly parameterization. Specifically, we utilize a power
law distribution, a truncated exponential distribution, a truncated
normal distribution and a log normal distribution. For simplicity,
we let the two selected distributions respectively be parameterized
by 𝛽 U and 𝛽 V . In each iteration, the parameters are all determined
uniformly at random:

𝛽 U, 𝛽 V ∼ Uniform(0, 𝛽𝑚𝑎𝑥 ),
where 𝛽𝑚𝑎𝑥 is the maximal value allowed. Notably, the embedding
sizes of each field (i.e., users and items) are derived by independently
sampling from two distributions 𝑃U and 𝑃V . This is because each
field may have distinct properties [37] and different distributions
are needed to model the embedding sizes of users and items.

(4)

After the distributions are determined, we sample |U| and |V |
probabilities respectively from 𝑃U and 𝑃V . The set of probabilities
are respectively denoted as {𝑝𝑖 } | U |
∼ 𝑃V . We
𝑖=1
then normalize all 𝑝𝑖 and 𝑝 𝑗 as the following:
𝑝 𝑗
(cid:205)| V |
𝑗

∼ 𝑃U and {𝑝 𝑗 } | V |
𝑗=1

𝑝𝑖
(cid:205)| U |
𝑖

˜𝑝 𝑗 =

˜𝑝𝑖 =

𝑝 𝑗

𝑝𝑖

(5)

,

,

where ˜𝑝𝑖 / ˜𝑝 𝑗 indicates the fraction of parameters each user/item re-
ceives among all users/items. Next, we obtain the actual embedding
sizes by applying the fraction on the memory budget:
𝑑𝑖 = ⌊ ˜𝑝𝑖 · 𝑤 · 𝑑𝑚𝑎𝑥 · (|U| + |V |)⌋,
𝑑 𝑗 = ⌊ ˜𝑝 𝑗 · (1 − 𝑤) · 𝑑𝑚𝑎𝑥 · (|U| + |V |)⌋,

𝑖 = 1, 2, · · · , |U|,
𝑗 = 1, 2, · · · , |V |,

(6)

where 𝑤 controls the proportion of parameters allocated to the
users. In practice, 𝑤 can be empirically defined, such as an even
split (i.e., 0.5). In BET, 𝑤 is sampled from a uniform distribution
each time a table-level action is generated, i.e., 𝑤 ∼ Uniform(0, 1),
so as to probe more embedding size allocation strategies in the
iterative search process.

With |U| + |V | embedding sizes derived, we now allocate them
to each user and item. Previous studies [37, 48, 62] have shown that
more frequent users and items tend to be more informative than
long-tail ones, hence generally benefit from a larger embedding
dimension which allows more information to be encoded. Therefore,
we rank the users by their frequency and allocate the 𝑛-th largest
user embedding size to the 𝑛-th frequent user. Similarly, we assign
embedding sizes to items based on their frequency. As such, we are
capable of sampling 𝑚 random table-level actions in each search
iteration to facilitate the subsequent steps.

3.3 Fitness Prediction Network
In each iteration 𝑡 we sample a set of 𝑚 actions, denoted as Q𝑡 . To
select the optimal action from Q𝑡 , a straightforward approach is to
pair each sampled action with a fresh recommender, train it until

Figure 2: Example of our set-based action formulation. Sup-
pose we have three legitimate embedding sizes {16, 32, 64},
four users (red) and two items (green). Then, size 16 is a
set containing user 1, user 2 and item 4, which means their
embedding sizes are 16. Similarly, the action specifies the
embedding sizes of user 3 and item 5 to be 32. Size 64 is not
used by any users/items.

Figure 3: Overview of the DeepSets-based fitness predictor.

convergence and select the action that yields the best final recom-
mendation quality on the validation set. However, this approach
faces inevitable computational burdens given the 𝑚 training and
evaluation processes needed per search iteration.

In BET, we utilize an action fitness predictor, which inductively
learns distinct embeddings of actions and predicts its fitness score
(i.e., recommendation quality) based on the action embeddings. As
discussed earlier, learning expressive representations of different
actions is a crucial yet non-trivial task for effective fitness predic-
tion, especially considering the need for inductively composing
embeddings for unseen actions in every new search iteration.

Thus, we propose a novel action fitness prediction network based
on the notion of set representation learning [50, 59]. Before delving
into the fitness prediction network, we first detail the set-based
formulation of each action. Each action is regarded as a collection
𝑑𝑚𝑎𝑥
of sets 𝑎 = {S𝑑 }
𝑑=1 , where each set S𝑑 = {𝑛|∀𝑛 ∈ U ∪V, 𝑑𝑛 = 𝑑 }
stores the users and items that use the embedding size 𝑑 ∈ [1, 𝑑𝑚𝑎𝑥 ].
S𝑑 = ∅ if there is no user or item assigned to embedding size 𝑑.
A toy example with is given in figure 2. As such, this allows us to
build our fitness predictor upon DeepSets [59] owing to its ability
to learn permutation-variant representations of sets.

The fitness prediction network consists of four components: a
user encoder 𝜌 U (·), an item encoder 𝜌 V (·), an embedding size
encoder 𝜇 (·), and a decoder 𝜋 (·), all of which bear a distinct MLP.
Encoders 𝜌 U (·)/𝜌 V (·) take some contextual information about a

---

<!-- PAGE 5 -->

Budgeted Embedding Table For Recommender Systems

WSDM ’24, March 4–8, 2024, Merida, Mexico

user/item, and produce their corresponding representations. Previ-
ous studies [41, 62] have demonstrated the suitability of users’/items’
popularity and current embedding sizes as the context information
for embedding size search. We inherit this design by establishing a
hierarchical, set-compatible action representation learning scheme.
Specifically, 𝜌 U (·) and 𝜌 V (·) respectively takes the user and item
frequencies to generate frequency-weighted embeddings:

), 𝑢 ∈ U,

𝒒𝑢 = 𝜌 U (

𝑓𝑢
max𝑢′ ∈ U 𝑓𝑢′
𝑓𝑣
max𝑣′ ∈ V 𝑓𝑣′
where each 𝑓𝑢 /𝑓𝑣 is normalized by the maximum user/item fre-
quency observed.

𝒒𝑣 = 𝜌 V (

𝑣 ∈ V,

(7)

),

As mentioned above, within an action 𝑎, each set S𝑑 contains
all users and items with embedding size 𝑑. To obtain embedding 𝒔𝑑
of set S𝑑 , we firstly fuse the representations of all involved users
and items using mean aggregation, and then append the explicit
embedding size information:

𝒔𝑑 = 𝜇

(cid:16) (cid:104) 1

∑︁

|S𝑑 |

𝑛∈ S𝑑

𝒒𝑛;

𝑑
𝑑𝑚𝑎𝑥

(cid:105) (cid:17)

,

(8)

where [; ] represents concatenation. With the representations gen-
erated for all 𝑑𝑚𝑎𝑥 sets, we derive the embedding for the entire
action 𝑎 by further merging all set representations:

𝒉𝑎 =

1
𝑑𝑚𝑎𝑥

𝑑𝑚𝑎𝑥
∑︁

𝑑=1

𝒔𝑑,

(9)

where we use 𝒉𝑎 to denote an action embedding. An additional
benefit from the set-based action embeddings is that, whenever the
action sampler draws any action that is new to the fitness predictor
(which is commonly the case in embedding size search), it allows
for generating the action embedding in an inductive fashion with
the available context information and the updated set formulation.
With each action embedding 𝒉𝑎, the decoder 𝜋 (·) takes 𝒉𝑎 and

outputs ˆ𝑟𝑎, which is the predicted fitness score of action 𝑎:

Algorithm 1 Embedding Size Search with BET

1: Initialize Θ and Φ, set A ← ∅;
2: Train 𝐺Θ (·) till convergence w.r.t. Eq. 2;
3: for 𝑡 = 1, · · · ,𝑇 do
4:

Draw distributions and their parameters w.r.t. Eq. 4;
Draw 𝑚 actions Q𝑡 = {𝑎1, ..., 𝑎𝑚 } with Eq. 5 and Eq. 6;
if 0 ≤ 𝑡 mod 5 ≤ 2 then
𝑎𝑡 ← Strategy I;
else if 𝑡 mod 5 = 3 then
𝑎𝑡 ← Strategy II;
else if 𝑡 mod 5 = 4 then
𝑎𝑡 ← Strategy III;

end if
Finetune Θ w.r.t. E ⊙ M𝑎𝑡 and Eq. 2
𝑟𝑎𝑡 ← Eq. 13
A ← A ∪ (𝑎𝑡 , 𝑟𝑎𝑡 );
for 𝑗 = 1, · · · , 𝑁 do

Randomly sample (𝑎 𝑗 , 𝑟𝑎 𝑗 ) from A;
ˆ𝑟𝑎 𝑗 ← Eq. 10;
Update Φ w.r.t. Eq. 11;

5:

6:

7:

8:

9:

10:

11:

12:

13:

14:

15:

16:

17:

18:

19:

end for

20:
21: end for
22: Perform selective retraining and obtain 𝑎∗ ← Eq. 14.

where eval(·) evaluates the recommendation quality, D𝑣𝑎𝑙 is the
validation set, M𝑎 is the binary mask corresponding to action 𝑎,
and the denominator is the recommendation quality of the pre-
trained backbone recommender 𝐺Θ (·) with the full embedding
table. Hence, 𝑟𝑎 can be interpreted as the ratio between the two
recommendation accuracy obtained by the sparsified embeddings
and the full embeddings. The implementation of eval(·) can follow
most commonly used recommendation metrics like Recall@𝑘 and
NDCG@𝑘 [14, 43], where we adopt an ensemble of both metrics
under different values of 𝑘:
∑︁

(cid:205)𝑘 ∈ K Recall@𝑘𝑢 + NDCG@𝑘𝑢
2|K ||U|

,

eval(E ⊙ M|D𝑣𝑎𝑙 ) =

(13)

𝑢 ∈ U

ˆ𝑟𝑎 = 𝜋 (𝒉𝑎).

(10)

where we the choices of 𝑘 cover K = {5, 10, 20} in our paper.

We will detail how the entire fitness prediction network 𝐹Φ (·) is
optimized along with the search process in the next section.

3.4 Fitness Predictor Training
Though bearing a relatively simple structure, the fitness predictor
still needs to be trained with some ground truth samples. The
fitness prediction network 𝐹Φ (·) is optimized by minimizing the
mean squared error between the predicted fitness score ˆ𝑟𝑎 and the
actual one 𝑟𝑎 with gradient descent:
∑︁

∑︁

(𝑟𝑎 − 𝐹Φ′ (𝑎))2 = argmin

(𝑟𝑎 − ˆ𝑟𝑎)2.

Φ = argmin

(11)

Φ′

∀𝑎

Φ′

∀𝑎

The actual fitness score 𝑟𝑎, i.e., recommendation quality of the
action, can be evaluated on the backbone recommender 𝐺Θ (·) after
being finetuned with an action 𝑎 w.r.t. Eq. 2:

𝑟𝑎 =

eval(E ⊙ M𝑎 |D𝑣𝑎𝑙 )
eval(E|D𝑣𝑎𝑙 )

,

(12)

The ground truth samples can be thus generated by gathering
different action-fitness pairs. Instead of constructing a pool of such
training samples and train 𝐹Φ (·) upfront, we incrementally add one
training sample in every search iteration 𝑡 to optimize 𝐹Φ (·) on
the go. The training sample is constructed by firstly identifying
a promising action from Q𝑡 , denoted by 𝑎𝑡 , and then obtaining
𝑟𝑎𝑡 by evaluating 𝑎𝑡 on the finetuned 𝐺Θ (·). Compared with most
RL-based embedding size search methods, the required number of
fitness evaluation with the recommendation model will be reduced
from 𝑚 × 𝑇 to merely 𝑇 , where 𝑇 is the total number of iterations
as well as the ground truth samples for optimizing 𝐹Φ (·).

3.5 Action Selection and Embedding Retraining
The pseudocode for BET is presented in Algorithm 1. Among its 𝑇
search iterations, we utilize three different strategies to pick one
action 𝑎𝑡 from the candidate action set Q𝑡 (lines 4-12). Then, the
recommender 𝐺Θ (·) is finetuned by adopting 𝑎𝑡 and evaluated on
the validation set (lines 13-14), where the produced (𝑎𝑡 , 𝑟𝑎𝑡 ) sample

---

<!-- PAGE 6 -->

WSDM ’24, March 4–8, 2024, Merida, Mexico

Yunke Qu, Tong Chen, Quoc Viet Hung Nguyen, & Hongzhi Yin

is popped into the population set A to facilitate training the fitness
prediction network 𝐹Φ (·) (lines 16-20). Finally, a selective retraining
process is conducted with the top-ranked actions in the population
in order to identify the best embedding size decision for all users and
items. We provide further details about action selection strategies
and retraining the sparsified embeddings below.

3.5.1 Diversifying the Action Space. The iterative input embedding
size search contains 𝑇 iterations. In each iteration 𝑡, the selected
action 𝑎𝑡 is added to the population set A with its associated fitness
score. For efficiency consideration, in each iteration 𝑡, we only
compute the actual fitness score for action 𝑎𝑡 , which is selected
from candidate actions Q𝑡 with one of the three following strategies:
I: We use our fitness prediction network 𝐹Φ (·) to predict the
fitness score of each candidate actions, and greedily selects
the action predicted to have the highest fitness score, i.e., 𝑎𝑡 =
𝐹Φ (𝑎). In essence, 𝐹Φ (·) is a surrogate function
argmax𝑎∈ Q𝑡
that is trained to approximate Eq. 12 and is substantially more
cost-effective than evaluating all 𝑚 actions via recommender
finetuning.

II: We randomly select one action from the Q𝑡 to diversify the
training samples for 𝐹Φ (·) by preventing it from overfitting
some specific action distributions in the population A.
III: We identify currently the best action (with the highest 𝑟𝑎)
in A. All actions in Q𝑡 and the best action are inductively
embedded into vector representations using Eq. 9. Then, by
calculating the pairwise Euclidean distance, we select action
𝑎𝑡 ∈ Q𝑡 by locating the best action’s nearest neighbor in the
embedding space.

Selective Retraining for Sparsified Embeddings. After 𝑇 search
3.5.2
iterations, from the population we identify the top five actions with
the highest 𝑟𝑎 on the validation set, denoted as A′. Each action
𝑎 ∈ A′ is paired with a fresh backbone recommender model, which
is trained from scratch on the training set until convergence. Next,
we evaluate the trained recommenders and select the final action
𝑎∗ that yields the best validation performance:

𝑎∗ = argmax
𝑎∈ A′
with which the sparsified embedding E𝑠𝑝𝑎𝑟𝑠𝑒 is obtained and stored
for inference.

𝑟𝑎,

(14)

4 EXPERIMENTS
This section details the experimental results of BET’s performance.

4.1 Base Recommenders and Comparative

Methods

One can combine BET with different embedding-based representa-
tion learning backbone recommender models. We tested the effec-
tiveness of our approach with three commonly used recommender
models as the backbone recommender 𝐹Φ: NCF [15], NGCF [53]
and LightGCN [14]. We used the same settings as reported in their
original works and replaced the embedding table with one with
adjustable embedding sizes to demonstrate the versatility and gen-
eralizability of our method across various backbone recommenders.
We compare BET with the following model-agnostic embedding
size search algorithms:

• PEP [35]: It adaptively prunes the embedding parameters
based on a learned pruning threshold learned along with the
model’s other parameters during the training process.

• ESAPN [? ]: It uses an RL agent which performs hard selec-
tion on embedding sizes for users and items based on the
memory complexity and recommendation performance.
• OptEmbed [37]: It prunes redundant embeddings based on
learnable pruning thresholds indicative of features’ impor-
tance and derives the optimal embedding size for each field
using evolutionary search.

• CIESS [41]: It is an RL-based method that chooses embedding
sizes for the users and items from a continuous domain.
• Single and Uniform (SU): All users and items share equal

and fixed embedding sizes.

• Single and Random (SR): The embedding sizes of the users

and items are sampled from a uniform distribution.

4.2 Evaluation Protocols
All the aforementioned methods are evaluated on two real-world
datasets: Gowalla [29] and Yelp2018 [53]. The first has 1,027,370
interactions between 29,858 users and 40,981 items while the latter
has 1,561,147 interactions between 31,668 users and 38,048 items.
We take 50%, 25% and 25% of the two datasets for training, vali-
dation, and test. To measure the recommendation performance of
the backbone recommender, Recall@𝑘 and NDCG@𝑘 are used as
evaluation metrics, where 𝑘 is set to either 5 or 20. To test the recom-
mendation performance of CIESS, PEP, SU and SR, three different
sparsity ratios (𝑐) of 80%, 90% and 95% are used. For each method,
the compressed embedding table is ensured to have no more than
𝑐 · 𝑑𝑚𝑎𝑥 · (|U| + |V |) usable parameter and the maximal embed-
ding size is 𝑑𝑚𝑎𝑥 = 128. However, since ESAPN and OptEmbed are
not designed to precisely control the embedding sparsity and focus
more on the performance, this section only reports the performance
associated with their final embedding tables after pruning.

4.3 Implementation Notes for BET
Hereby we detail the implementation of BET. The number of search
iterations 𝑇 is 10. The maximal values of the distribution parameters
𝛽𝑚𝑎𝑥 are set to 20 for power law distribution, 20 for truncated
normal distribution, 5 for truncated exponential distribution and
0.5 for log normal distribution. The maximal embedding size 𝑑𝑚𝑎𝑥
is 128 and the minimal embedding size 𝑑𝑚𝑖𝑛 is 1. In each iteration,
the pre-trained backbone recommender is finetuned for 10 epochs
(i.e., ℎ = 10) when the backbone recommender is LightGCN or NCF.
When NGCF is used, the backbone recommender is finetuned for
15 epochs (i.e., ℎ = 15). For finetuning, the initial learning rate is
0.03 and decays every 200 steps with a decay ratio of 0.98. The
number of fitness prediction updates in each iteration, or 𝑁 , is set
to 2. The user and item encoders have input size 1, output size 16,
and hidden size 16. The size encoder has input size 17, output size
64, and hidden size 64. The decoder has input size 64, output size 1,
and hidden size 64. All the MLP-based encoders and decoders have
two layers with the Leaky RelU [38] activation function.

---

<!-- PAGE 7 -->

Budgeted Embedding Table For Recommender Systems

WSDM ’24, March 4–8, 2024, Merida, Mexico

Sparsity
75%
74%

80%

Method
ESAPN
OptEmb
PEP
SU
SR
CIESS
BET

PEP
SU
SR
CIESS
BET

PEP
SU
SR
CIESS
BET

𝑝-value

90%

95%

𝑝-value

𝑝-value

LightGCN
N@5
0.1173
0.0983
0.1189
0.1219
0.1150
0.1263
0.1303
0.0001
0.0992
0.1041
0.1013
0.1193
0.1212
0.0481
0.0666
0.0727
0.0834
0.0853
0.1037
0.0002

R@5
0.0741
0.0591
0.0715
0.0756
0.0708
0.0777
0.0797
0.0024
0.0594
0.0646
0.0617
0.0721
0.0736
0.0165
0.0372
0.0446
0.0500
0.0513
0.0627
0.0001

R@20
0.1579
0.1314
0.1588
0.1674
0.1583
0.1750
0.1753
0.0391
0.1274
0.1477
0.1403
0.1589
0.1620
0.0091
0.0803
0.1085
0.1178
0.1214
0.1374
0.0001

N@20
0.1329
0.1115
0.1347
0.1400
0.1323
0.1461
0.1483
0.0012
0.1102
0.1217
0.1171
0.1353
0.1376
0.0226
0.0712
0.0872
0.0975
0.0997
0.1171
0.0001

Sparsity
83%
75%

80%

90%

95%

R@5
0.0627
0.0510
0.0656
0.0619
0.0512
0.0676
0.0643
0.7815
0.0552
0.0589
0.0466
0.0601
0.0623
0.0005
0.0247
0.0527
0.0438
0.0505
0.0528
0.1896

NGCF
N@5
0.1060
0.0860
0.1049
0.0961
0.0815
0.1084
0.1039
0.2179
0.0914
0.0935
0.0764
0.0980
0.1012
0.0205
0.0471
0.0870
0.0739
0.0856
0.0883
0.0638

R@20
0.1396
0.1227
0.1524
0.1466
0.1223
0.1504
0.1454
0.0514
0.1327
0.1380
0.1123
0.1380
0.1426
0.0601
0.0674
0.1213
0.1040
0.1129
0.1172
0.7269

N@20
0.1193
0.1005
0.1245
0.1170
0.0982
0.1251
0.1204
0.0924
0.1081
0.1115
0.0911
0.1140
0.1177
0.0232
0.0554
0.1007
0.0859
0.0964
0.9980
0.3608

(a) Results on Gowalla

Sparsity
74%
82%

80%

90%

95%

R@5
0.0498
0.0330
0.0498
0.0481
0.0478
0.0550
0.0511
0.1962
0.0414
0.0413
0.0399
0.0448
0.0434
0.1454
0.0351
0.0336
0.0329
0.0361
0.0388
0.0321

NCF
N@5
0.0718
0.0492
0.0704
0.0662
0.0656
0.0744
0.0723
0.1337
0.0631
0.0548
0.0536
0.0613
0.0648
0.0554
0.0591
0.0478
0.0489
0.0567
0.0616
0.1107

R@20
0.1280
0.0877
0.1282
0.1235
0.1243
0.1307
0.1294
0.2578
0.1121
0.1112
0.1069
0.1131
0.1122
0.6608
0.0897
0.0952
0.0918
0.0933
0.0963
0.1104

N@20
0.0959
0.0653
0.0957
0.0916
0.0910
0.0997
0.0973
0.0414
0.0839
0.0796
0.0769
0.0841
0.0845
0.0655
0.0712
0.0682
0.0674
0.0717
0.0756
0.0010

90%

80%

80%

80%

𝑝-value

Sparsity
76%
77%

Sparsity
71%
67%

Sparsity
73%
80%

PEP
SU
SR
CIESS
BET

Method
ESAPN
OptEmb
PEP
SU
SR
CIESS
BET

R@5
0.0294
0.0183
0.0253
0.0289
0.0253
0.0292
0.0310
0.0008
0.0224
0.0230
0.0210
0.0263
0.0284
0.0045
0.0199
0.0217
0.0195
0.0230
0.0255
0.0403

LightGCN
N@5
0.0696
0.0424
0.0605
0.0665
0.0588
0.0692
0.0726
0.0309
0.0531
0.0544
0.0476
0.0649
0.0674
0.0060
0.0496
0.0494
0.0465
0.0534
0.0596
0.0200

NGCF
N@5
0.0538
0.0301
0.0167
0.0517
0.0499
0.0566
0.0601
0.0418
0.0153
0.0528
0.0449
0.0551
0.0586
0.0007
0.0143
0.0496
0.0415
0.0540
0.0505
0.0451
(b) Results on Yelp
Table 1: Performance of all methods on (a) Gowalla, and (b) Yelp2018 with the sparsity ratio set to 80%, 90%, and 95%. The best
results are highlighted. Recall@𝑘 and NDCG@𝑘 are denoted by R@𝑘 and N@𝑘 for simplicity. Each 𝑝-value is calculated via the
paired 𝑡-test between BET and the best baseline.

NCF
N@5
0.0342
0.0161
0.0236
0.0226
0.0183
0.0377
0.0451
0.0122
0.0242
0.0201
0.0170
0.0350
0.0400
0.0067
0.0244
0.0174
0.0145
0.0383
0.0404
0.0246

R@5
0.0153
0.0076
0.0130
0.0131
0.0101
0.0175
0.0194
0.0387
0.0139
0.0119
0.0089
0.0153
0.0173
0.0234
0.0125
0.0091
0.0078
0.0157
0.0170
0.0399

N@20
0.0603
0.0369
0.0223
0.0603
0.0573
0.0652
0.0685
0.0024
0.0215
0.0592
0.0524
0.0619
0.0676
0.0069
0.0206
0.0545
0.0486
0.0613
0.0588
0.0193

R@20
0.0812
0.0534
0.0723
0.0822
0.0783
0.0839
0.0873
0.0004
0.0657
0.0722
0.0642
0.0730
0.0816
0.0051
0.0600
0.0624
0.0583
0.6570
0.0727
0.0305

R@5
0.0214
0.0133
0.0086
0.0223
0.0212
0.0233
0.0254
0.0412
0.0080
0.0205
0.0195
0.0232
0.0246
0.0012
0.0075
0.0196
0.0175
0.0222
0.0216
0.0327

N@20
0.0430
0.0203
0.0327
0.0351
0.0268
0.0474
0.0554
0.0341
0.0335
0.0309
0.0242
0.0442
0.0499
0.0118
0.0330
0.0238
0.0216
0.0446
0.0491
0.0044

N@20
0.0773
0.0489
0.0682
0.0758
0.0698
0.0783
0.0816
0.0109
0.0610
0.0648
0.0573
0.0705
0.0762
0.0006
0.0561
0.0571
0.0540
0.0640
0.0676
0.0204

R@20
0.0490
0.0238
0.0406
0.0465
0.0342
0.0533
0.0620
0.0483
0.0427
0.0416
0.0309
0.0500
0.0565
0.0426
0.0399
0.0303
0.0275
0.0483
0.0545
0.0094

R@20
0.0632
0.0412
0.0275
0.0665
0.0618
0.0701
0.0741
0.0082
0.0276
0.0622
0.0573
0.0669
0.0736
0.0102
0.0259
0.0573
0.0528
0.0662
0.0639
0.0064

PEP
SU
SR
CIESS
BET

𝑝-value

𝑝-value

95%

90%

95%

90%

95%

Sparsity

Selection Method

80%

90%

95%

Random Selection
Simple fitness prediction
DeepSets fitness prediction
Random Selection
Simple fitness prediction
DeepSets fitness prediction
Random Selection
Simple fitness prediction
DeepSets fitness prediction

Yelp2018

Gowalla

R@20
0.0846
0.0835
0.0873
0.0767
0.0768
0.0816
0.0637
0.0673
0.0727

N@20
0.0788
0.0779
0.0816
0.0717
0.0717
0.0762
0.0583
0.0629
0.0676

R@20
0.1749
0.1739
0.1753
0.1594
0.1590
0.1620
0.1335
0.1349
0.1374

N@20
0.1473
0.1469
0.1483
0.1357
0.1355
0.1376
0.1143
0.1152
0.1171

Table 2: Performance of BET when different selection meth-
ods are used.
4.4 Overall Performance Comparison
Table 1 shows the Recall@𝑘 and NDCG@𝑘 scores of various light-
weight embedding methods when they are paired with different
backbone recommender models. We also perform paired student’s
𝑡-test between BET and the best baseline method. Compared with
the baselines with adjustable sparsity ratios (i.e., PEP, SU, SR, and
CIESS), BET achieves better performance across all three backbone

recommenders and at nearly all specified sparsity levels (80%, 90%,
and 95%). The associated 𝑝-values are below 5% most of the time
so we can reject the null hypothesis that the observed performance
changes occurred by chance in most scenarios.

Meanwhile, the sparsity ratios achieved by ESAPN and OptEm-
bed range from 67% and 83%, often failing to meet the minimum
target of 80%. Despite keeping a relatively higher number of param-
eters compared to other methods, their recommendation perfor-
mance is consistently inferior to BET. For instance, when used with
LightGCN on the Gowalla dataset, ESAPN requires more memory
complexity (75% sparsity ratio) to achieve a comparable perfor-
mance compared to BET under an 90% sparsity condition.

In summary, BET demonstrates superior performance while
maintaining the same memory usage. Similarly, when comparing
performance levels, BET proves to be more efficient in memory
utilization. Consequently, these findings highlight the benefits of
the ongoing embedding size exploration in BET.

---

<!-- PAGE 8 -->

WSDM ’24, March 4–8, 2024, Merida, Mexico

Yunke Qu, Tong Chen, Quoc Viet Hung Nguyen, & Hongzhi Yin

(a) Effect of 𝑚 on Yelp

(a) Effect of 𝑇 on Yelp

(b) Effect of 𝑚 on Gowalla
Figure 4: Sensitivity analysis of 𝑚 on Recall@20 and
NDCG@20 with LightGCN as the backbone recommender.

4.5 Model Component Analysis
Selecting from the set of candidate actions in each iteration is a vital
step in BET, where we proposed a hybrid selection method that
alternately uses three selection strategies. To study the effectiveness
of the proposed selection method and the DeepSets-based fitness
prediction network, we conduct a quantitative study on BET and
its two variants. The first variant uses random selection only. The
second variant incorporates a simplistic fitness prediction network
that only accepts the embedding sizes of each user and item. Table
2 illustrates the performance of the original version of BET along
with its two variants in terms of their Recall@20 and NDCG@20
scores. Only the performance of the best-performing backbone
recommender LightGCN is reported due to space limit. The results
show that BET with a DeepSets-based fitness prediction network
has better performance than the two variants, implying that our
proposed selection method is effective and the DeepSets-based
architecture is able to learn the latent representation of actions.

4.6 Analysis of Hyperparameter
In this section, we inspect the influence of the core hyperparameters
in BET in terms of Recall@20 and NDCG@20. LightGCN shows
the best performance so it is chosen as the backbone recommender
for demonstration.

4.6.1 Number of Sampled Actions 𝑚. In each iteration, we sam-
ple 𝑚 candidate actions to choose from. We tune BET with 𝑚 ∈
{20, 40, 60, 80, 100} for both Yelp2018 and Gowalla. Then we show
how the performance changes with different values of 𝑚 w.r.t. Re-
call@20 and NDCG@20 scores. As shown in Figure 4, although
BET is relatively insensitive to the value of 𝑚, better performance
is achieved with 𝑚 = 100 on both datasets.

4.6.2 Number of Iterations 𝑇 . BET iteratively samples, selects and
evaluates actions in search of the optimal one. One natural question
that arises is how many iterations it needs to find the action that
leads to peak recommendation performance. This question is crucial
for understanding the effectiveness of BET. Therefore, we perform
selective retraining as described in Section 3.5.2 on the resulting

(b) Effect of 𝑇 on Gowalla
Figure 5: Sensitivity analysis of 𝑇 on Recall@20 and
NDCG@20 with LightGCN as the backbone recommender.

Figure 6: Sensitivity analysis of 𝑇 on the fitness predic-
tion loss with LightGCN as the backbone recommender on
Yelp2018 (left) and Gowalla (right).
population A𝑡 for each training iteration 𝑡 ∈ [0,𝑇 ] and report
the best recommendation performance in terms of Recall@20 and
NDCG@20. We also report the average fitness prediction loss in
each iteration. Figure 6 shows that fitness predictor converges
within the first 15 iterations. While the training loss of the fitness
predictor is diminishing, BET witnesses a substantial improvement
in its performance in the first 10-15 iterations, as shown in Figure 5.
Then performance continues to climb slowly after the 15th iteration
until it reaches its peak around the 40th iteration and remains
unchanged after that. In conclusion, setting 𝑇 = 50 should suffice
for BET to find the optimal action for all sparsity ratios.

5 CONCLUSION AND FUTURE WORKS
Latent factor recommenders typically employ vectorized embed-
dings with a uniform and fixed size, resulting in suboptimal perfor-
mance and excessive memory complexity. To address this challenge,
we have introduced BET, a model-agnostic algorithm to enable the
selection of customized embedding sizes at the level of the em-
bedding table for each user/item. This approach enhances the the
embeddings while minimizing memory costs. Next, we will develop
embedding size search algorithms for streaming recommendation.

ACKNOWLEDGMENT
This work is supported by the Australian Research Council under
the streams of Future Fellowship (No. FT210100624), Discovery
Project (No. DP190101985), and Discovery Early Career Research
Award (No. DE200101465 and No. DE230101033).

---

<!-- PAGE 9 -->

Budgeted Embedding Table For Recommender Systems

WSDM ’24, March 4–8, 2024, Merida, Mexico

REFERENCES
[1] Anshumali Shrivastava Aditya Desai, Li Chou. 2022. Random Offset Block Embed-
ding (ROBE) for compressed embedding tables in deep learning recommendation
systems. In Proceedings of Machine Learning and Systems. 762–778.

[2] Mathieu Blondel, Akinori Fujino, Naonori Ueda, and Masakazu Ishihata. 2016.
Higher-Order Factorization Machines. In Proceedings of the 30th International
Conference on Neural Information Processing Systems. 3359–3367.

[3] Han Cai, Chuang Gan, Tianzhe Wang, Zhekai Zhang, and Song Han. 2020. Once-
for-all: Train one network and specialize it for efficient deployment. ICLR (2020).
[4] Cheng Chen, Xiangwu Meng, Zhenghua Xu, and Thomas Lukasiewicz. 2017.
Location-Aware Personalized News Recommendation With Deep Semantic Anal-
ysis. IEEE Access 5 (2017), 1624–1638.

[5] Ting Chen, Lala Li, and Yizhou Sun. 2020. Differentiable Product Quantization
for End-to-End Embedding Compression. In Proceedings of the 37th International
Conference on Machine Learning. 1617–1626.

[6] Tong Chen, Hongzhi Yin, Guanhua Ye, Zi Huang, Yang Wang, and Meng Wang.
2020. Try This Instead: Personalized and Interpretable Substitute Recommenda-
tion. In SIGIR. 891–900.

[7] Tong Chen, Hongzhi Yin, Xiangliang Zhang, Zi Huang, Yang Wang, and Meng
Wang. 2021. Quaternion Factorization Machines: A Lightweight Solution to
Intricate Feature Interaction Modeling. IEEE Transactions on Neural Networks
and Learning Systems 34, 8 (2021), 1–14.

[8] Tong Chen, Hongzhi Yin, Yujia Zheng, Zi Huang, Yang Wang, and Meng Wang.
2021. Learning Elastic Embeddings for Customizing On-Device Recommenders.
In SIGKDD. 138–147.

[9] Yankai Chen, Huifeng Guo, Yingxue Zhang, Chen Ma, Ruiming Tang, Jingjie Li,
and Irwin King. 2022. Learning Binarized Graph Representations with Multi-
Faceted Quantization Reinforcement for Top-K Recommendation. In SIGKDD.
168–178.

[10] Yankai Chen, Huifeng Guo, Yingxue Zhang, Chen Ma, Ruiming Tang, Jingjie
Li, and Irwin King. 2022. Learning Binarized Graph Representations with
Multi-Faceted Quantization Reinforcement for Top-K Recommendation. In KDD.
168–178.

[11] Aditya Desai and Anshumali Shrivastava. 2022. The trade-offs of model size
in large recommendation models : 100GB to 10MB Criteo-tb DLRM model. In
NeurIPS. 33961–33972.

[12] Yuyun Gong and Qi Zhang. 2016. Hashtag recommendation using attention-based

convolutional neural network.. In IJCAI. 2782–2788.

[13] Huifeng Guo, Ruiming Tang, Yunming Ye, Zhenguo Li, and Xiuqiang He. 2017.
DeepFM: a factorization-machine based neural network for CTR prediction. IJCAI
(2017).

[14] Xiangnan He, Kuan Deng, Xiang Wang, Yan Li, Yongdong Zhang, and Meng
Wang. 2020. Lightgcn: Simplifying and powering graph convolution network for
recommendation. In SIGIR. 639–648.

[15] Xiangnan He, Lizi Liao, Hanwang Zhang, Liqiang Nie, Xia Hu, and Tat-Seng

Chua. 2017. Neural collaborative filtering. In WWW. 173–182.

[16] Zhenhua Huang, Xin Xu, Juan Ni, Honghao Zhu, and Cheng Wang. 2019. Multi-
modal representation learning for recommendation in Internet of Things. IEEE
Internet of Things Journal 6, 6 (2019), 10675–10685.

[17] Gangwei Jiang, Hao Wang, Jin Chen, Haoyu Wang, Defu Lian, and Enhong Chen.
2021. XLightFM: Extremely Memory-Efficient Factorization Machine. In SIGIR.
337–346.

[18] Manas R Joglekar, Cong Li, Mei Chen, Taibai Xu, Xiaoming Wang, Jay K Adams,
Pranav Khaitan, Jiahui Liu, and Quoc V Le. 2020. Neural input search for large
scale recommendation models. In SIGKDD. 2387–2397.

[19] Wang-Cheng Kang, Derek Zhiyuan Cheng, Ting Chen, Xinyang Yi, Dong Lin,
Lichan Hong, and Ed H. Chi. 2020. Learning Multi-Granular Quantized Embed-
dings for Large-Vocab Categorical Features in Recommender Systems. In WWW.
562–566.

[20] Nitish Shirish Keskar, Dheevatsa Mudigere, Jorge Nocedal, Mikhail Smelyanskiy,
and Ping Tak Peter Tang. 2016. On Large-Batch Training for Deep Learning:
Generalization Gap and Sharp Minima. In ICLR.

[21] Yunyong Ko, Jae-Seo Yu, Hong-Kyun Bae, Yongjun Park, Dongwon Lee, and
Sang-Wook Kim. 2021. MASCOT: A Quantization Framework for Efficient Matrix
Factorization in Recommender Systems. In 2021 IEEE International Conference on
Data Mining (ICDM). 290–299.

[22] Shuming Kong, Weiyu Cheng, Yanyan Shen, and Linpeng Huang. 2023. AutoSrh:
An Embedding Dimensionality Search Framework for Tabular Data Prediction.
TKDE 35, 7 (2023), 6673–6686.

[23] Su Mon Kywe, Ee-Peng Lim, and Feida Zhu. 2012. A survey of recommender

systems in twitter. In International Conference on Social Informatics. 420–433.

[24] Joonseok Lee, Sami Abu-El-Haija, Balakrishnan Varadarajan, and Apostol Natsev.
2018. Collaborative deep metric learning for video understanding. In Proceedings
of the 24th ACM SIGKDD International conference on knowledge discovery & data
mining. 481–490.

[25] Piji Li, Zihao Wang, Zhaochun Ren, Lidong Bing, and Wai Lam. 2017. Neural
rating regression with abstractive tips generation for recommendation. In Proceed-
ings of the 40th International ACM SIGIR conference on Research and Development
in Information Retrieval. 345–354.

[26] Shiwei Li, Huifeng Guo, Lu Hou, Wei Zhang, Xing Tang, Ruiming Tang, Rui
Zhang, and Ruixuan Li. 2023. Adaptive Low-Precision Training for Embeddings
in Click-Through Rate Prediction. Proceedings of the AAAI Conference on Artificial
Intelligence 37, 4 (2023), 4435–4443.

[27] Siyuan Li and Elena Karahanna. 2015. Online Recommendation Systems in a B2C
E-Commerce Context: A Review and Future Directions. Journal of the Association
for Information Systems 16 (2015), 72–107.

[28] Yang Li, Tong Chen, Peng-Fei Zhang, and Hongzhi Yin. 2021. Lightweight self-

attentive sequential recommendation. In CIKM. 967–977.

[29] Dawen Liang, Laurent Charlin, James McInerney, and David M. Blei. 2016. Mod-

eling User Exposure in Recommendation. In WWW. 951–961.

[30] Xurong Liang, Tong Chen, Quoc Viet Hung Nguyen, Jianxin Li, and Hongzhi Yin.
2023. Learning Compact Compositional Embeddings via Regularized Pruning
for Recommendation. In ICDM.

[31] Guanyu Lin, Chen Gao, Yinfeng Li, Y. Zheng, Zhiheng Li, Depeng Jin, and Yong
Li. 2022. Dual Contrastive Network for Sequential Recommendation with User
and Item-Centric Perspectives. ACM Transactions on Information Systems 1, 1
(2022).

[32] Weilin Lin, Xiangyu Zhao, Yejing Wang, Tong Xu, and Xian Wu. 2022. AdaFS:
Adaptive Feature Selection in Deep Recommender System. In Proceedings of
the 28th ACM SIGKDD Conference on Knowledge Discovery and Data Mining.
3309–3317.

[33] Han Liu, Yinwei Wei, Jianhua Yin, and Liqiang Nie. 2023. HS-GCN: Hamming
Spatial Graph Convolutional Networks for Recommendation. TKDE 35, 6 (2023),
5977–5990.

[34] Haochen Liu, Xiangyu Zhao, Chong Wang, Xiaobing Liu, and Jiliang Tang. 2020.
Automated embedding size search in deep recommender systems. In SIGIR. 2307–
2316.

[35] Siyi Liu, Chen Gao, Yihong Chen, Depeng Jin, and Yong Li. 2021. Learnable

Embedding sizes for Recommender Systems. In ICLR.

[36] Yuanfei Luo, Mengshuo Wang, Hao Zhou, Quanming Yao, Wei-Wei Tu, Yuqiang
Chen, Wenyuan Dai, and Qiang Yang. 2019. Autocross: Automatic feature crossing
for tabular data in real-world applications. In SIGKDD. 1936–1945.

[37] Fuyuan Lyu, Xing Tang, Hong Zhu, Huifeng Guo, Yingxue Zhang, Ruiming
Tang, and Xue Liu. 2022. OptEmbed: Learning Optimal Embedding Table for
Click-through Rate Prediction. In CIKM. 1399–1409.

[38] Andrew L Maas, Awni Y Hannun, Andrew Y Ng, et al. 2013. Rectifier nonlineari-

ties improve neural network acoustic models. In ICML.

[39] Khalil Muhammad, Qinqin Wang, Diarmuid O’Reilly-Morgan, Elias Tragos, Barry
Smyth, Neil Hurley, James Geraci, and Aonghus Lawlor. 2020. Fedfast: Going
beyond average for faster training of federated recommender systems. In SIGKDD.
1234–1242.

[40] Liang Qu, Yonghong Ye, Ningzhi Tang, Lixin Zhang, Yuhui Shi, and Hongzhi Yin.
2022. Single-Shot Embedding Dimension Search in Recommender System. In
SIGIR. 513–522.

[41] Yunke Qu, Tong Chen, Xiangyu Zhao, Lizhen Cui, Kai Zheng, and Hongzhi Yin.
2023. Continuous Input Embedding Size Search For Recommender Systems. In
SIGIR. 708–717.

[42] Steffen Rendle. 2010. Factorization machines. In 2010 IEEE International conference

on data mining. 995–1000.

[43] Steffen Rendle, Christoph Freudenthaler, Zeno Gantner, and Lars Schmidt-Thieme.
2009. BPR: Bayesian Personalized Ranking from Implicit Feedback. In Proceedings
of the Twenty-Fifth Conference on Uncertainty in Artificial Intelligence. 452–461.
[44] Naser Sedaghati, Te Mu, Louis-Noel Pouchet, Srinivasan Parthasarathy, and P
Sadayappan. 2015. Automatic selection of sparse matrix representation on GPUs.
In ACM International Conference on Supercomputing. 99–108.

[45] Suvash Sedhain, Aditya Krishna Menon, Scott Sanner, and Lexing Xie. 2015.
AutoRec: Autoencoders Meet Collaborative Filtering. In WWW. 111–112.
[46] Geet Sethi, Bilge Acun, Niket Agarwal, Christos Kozyrakis, Caroline Trippel, and
Carole-Jean Wu. 2022. RecShard: Statistical Feature-Based Memory Optimization
for Industry-Scale Neural Recommendation. In Proceedings of the 27th ACM
International Conference on Architectural Support for Programming Languages and
Operating Systems. 344–358.

[47] Hao-Jun Michael Shi, Dheevatsa Mudigere, Maxim Naumov, and Jiyan Yang. 2020.
Compositional embeddings using complementary partitions for memory-efficient
recommendation systems. In SIGKDD. 165–175.

[48] Yang Sun, Fajie Yuan, Min Yang, Guoao Wei, Zhou Zhao, and Duo Liu. 2020. A
Generic Network Compression Framework for Sequential Recommender Systems.
In SIGIR ’20. 1299–1308.

[49] Pauli Virtanen et al. 2020. SciPy 1.0: fundamental algorithms for scientific com-

puting in Python. Nature Methods 17, 3 (2020), 261–272.

[50] Edward Wagstaff, Fabian B Fuchs, Martin Engelcke, Michael A Osborne, and
Ingmar Posner. 2022. Universal approximation of functions on sets. JMLR 23, 1
(2022), 6762–6817.

---

<!-- PAGE 10 -->

WSDM ’24, March 4–8, 2024, Merida, Mexico

Yunke Qu, Tong Chen, Quoc Viet Hung Nguyen, & Hongzhi Yin

[51] Shoujin Wang, Longbing Cao, Yan Wang, Quan Z Sheng, Mehmet A Orgun,
and Defu Lian. 2021. A survey on session-based recommender systems. ACM
Computing Surveys (CSUR) 54, 7 (2021), 1–38.

[52] Suhang Wang, Yilin Wang, Jiliang Tang, Kai Shu, Suhas Ranganath, and Huan Liu.
2017. What Your Images Reveal: Exploiting Visual Contents for Point-of-Interest
Recommendation. In Proceedings of the 26th International Conference on World
Wide Web. 391–400.

[53] Xiang Wang, Xiangnan He, Meng Wang, Fuli Feng, and Tat-Seng Chua. 2019.

Neural graph collaborative filtering. In SIGIR. 165–174.

[54] Yejing Wang, Xiangyu Zhao, Tong Xu, and Xian Wu. 2022. Autofield: Automating

feature selection in deep recommender systems. In WWW. 1977–1986.

[55] Xin Xia, Hongzhi Yin, Junliang Yu, Qinyong Wang, Guandong Xu, and Quoc
Viet Hung Nguyen. 2022. On-Device Next-Item Recommendation with Self-
Supervised Knowledge Distillation. In SIGIR. 546–555.

[56] Xin Xia, Junliang Yu, Qinyong Wang, Chaoqun Yang, Nguyen Quoc Viet Hung,
and Hongzhi Yin. 2023. Efficient On-Device Session-Based Recommendation.
ACM Transactions Information Systems 41, 4 (2023).

[57] Bencheng Yan, Pengjie Wang, Jinquan Liu, Wei Lin, Kuang-Chih Lee, Jian Xu, and
Bo Zheng. 2021. Binary Code Based Hash Embedding for Web-Scale Applications.
In CIKM. 3563–3567.

[58] Junliang Yu, Hongzhi Yin, Xin Xia, Tong Chen, Lizhen Cui, and Quoc Viet Hung
Nguyen. 2022. Are Graph Augmentations Necessary? Simple Graph Contrastive

Learning for Recommendation. In SIGIR. 1294–1303.

[59] Manzil Zaheer, Satwik Kottur, Siamak Ravanbhakhsh, Barnabás Póczos, Ruslan
Salakhutdinov, and Alexander J Smola. 2017. Deep Sets. In NeurIPS. 3394–3404.
[60] Caojin Zhang, Yicun Liu, Yuanpu Xie, Sofia Ira Ktena, Alykhan Tejani, Akshay
Gupta, Pranay Kumar Myana, Deepak Dilipkumar, Suvadip Paul, Ikuhiro Ihara,
et al. 2020. Model size reduction using frequency based double hashing for
recommender systems. In Fourteenth ACM Conference on Recommender Systems.
521–526.

[61] Shuai Zhang, Lina Yao, Aixin Sun, and Yi Tay. 2019. Deep learning based rec-
ommender system: A survey and new perspectives. ACM Computing Surveys
(CSUR) 52, 1 (2019), 1–38.

[62] Xiangyu Zhao, Haochen Liu, Wenqi Fan, Hui Liu, Jiliang Tang, Chong Wang,
Ming Chen, Xudong Zheng, Xiaobing Liu, and Xiwang Yang. 2021. Autoemb:
Automated embedding dimensionality search in streaming recommendations. In
2021 IEEE International Conference on Data Mining (ICDM). 896–905.

[63] Ruiqi Zheng, Liang Qu, Bin Cui, Yuhui Shi, and Hongzhi Yin. 2022. AutoML
for Deep Recommender Systems: A Survey. ACM Transactions on Information
Systems 101 (2022), 1–38.

[64] Meizi Zhou, Zhuoye Ding, Jiliang Tang, and Dawei Yin. 2018. Micro Behaviors:
A New Perspective in E-Commerce Recommender Systems. In Proceedings of the
Eleventh ACM International Conference on Web Search and Data Mining. 727–735.

<!-- MARKITDOWN CONVERSION -->

<!-- Full MarkItDown conversion for formatting fidelity. -->

Budgeted Embedding Table For Recommender Systems
YunkeQu TongChen
TheUniversityofQueensland TheUniversityofQueensland
Brisbane,Australia Brisbane,Australia
yunke.qu@uq.net.au tong.chen@uq.edu.au
QuocVietHungNguyen HongzhiYin∗
GriffithUniversity TheUniversityofQueensland
GoldCoast,Australia Brisbane,Australia
henry.nguyen@griffith.edu.au h.yin1@uq.edu.au
ABSTRACT KEYWORDS
Attheheartofcontemporaryrecommendersystems(RSs)arelatent recommendersystems,neuralarchitecturesearch
factormodelsthatprovidequalityrecommendationexperienceto
ACMReferenceFormat:
users.Thesemodelsuseembeddingvectors,whicharetypicallyofa
YunkeQu,TongChen,QuocVietHungNguyen,andHongzhiYin.2024.
uniformandfixedsize,torepresentusersanditems.Asthenumber
BudgetedEmbeddingTableForRecommenderSystems.InProceedingsofthe
ofusersanditemscontinuestogrow,thisdesignbecomesineffi- 17thACMInternationalConferenceonWebSearchandDataMining(WSDM
cientandhardtoscale.Recentlightweightembeddingmethods ’24),March4–8,2024,Merida,Mexico.ACM,NewYork,NY,USA,10pages.
haveenableddifferentusersanditemstohavediverseembedding https://doi.org/10.1145/3616855.3635778
sizes,butarecommonlysubjecttotwomajordrawbacks.Firstly,
1 INTRODUCTION
theylimittheembeddingsizesearchtooptimizingaheuristicbal-
ancingtherecommendationqualityandthememorycomplexity, Recommender systems (RSs) predict a user’s preference for an
wherethetrade-offcoefficientneedstobemanuallytunedforev- item according to observed user-item interactions [51, 61] and
erymemorybudgetrequested.Theimplicitlyenforcedmemory havebeenindispensableacrossnumerousmodernplatformssuch
complexitytermcanevenfailtocaptheparameterusage,mak- ase-commerceandsocialmedia[23,27,64].Incontextswhere
ingtheresultantembeddingtablefailtomeetthememorybudget computationsonlocaldevicesareessential,suchasfederatedrec-
strictly.Secondly,mostsolutions,especiallyreinforcementlearn- ommendation[39]andInternetofThings(IoT)services[16],the
ingbasedonesderiveandoptimizetheembeddingsizeforeach needforRSswithsmallmemoryfootprintsbecomescriticaldueto
eachuser/itemonaninstance-by-instancebasis,whichimpedesthe highlyconstrainedcomputationalresources.Themainbottleneck
searchefficiency.Inthispaper,weproposeBudgetedEmbedding fordownsizingRSsisoftentheembeddingtable,whichrepresents
Table(BET),anovelmethodthatgeneratestable-levelactions(i.e., usersanditemswithdistinctembeddingvectorstofacilitatepair-
embeddingsizesforallusersanditems)thatisguaranteedtomeet wisesimilaritycomputation.Assuch,thesizeoftheembedding
pre-specifiedmemorybudgets.Furthermore,byleveragingaset- tablecanquicklyexhausttheavailablememory,posingasignificant
basedactionformulationandengagingsetrepresentationlearning, challengetoachievingscalableandresource-friendlyRSs.
wepresentaninnovativeactionsearchstrategypoweredbyan Suchmemorybottleneckisattributedtoconventionalembed-
actionfitnesspredictorthatefficientlyevaluateseachtable-level dingtables,whichtypicallyallocatefixedanduniformembedding
action.Experimentshaveshownstate-of-the-artperformanceon sizestoeachuseranditem[8,18].Suchadesignmayrequirean
tworeal-worlddatasetswhenBETispairedwiththreepopular excessivenumberofparametersinindustry-scaleapplications,e.g.,
recommendermodelsunderdifferentmemorybudgets. thebenchmarkrecommenderin[11]hasmorethan25billionpa-
rametersinitsembeddingtableandrequires100GBmemory.Inthis
CCSCONCEPTS regard,researchershavedevelopedmethodstoachievelightweight
embeddingswhilemaintainingitsexpressiveness.Onestreamof
•Informationsystems→Recommendersystems.
methodsaimtopruneredundantparametersoftheembeddingtable.
Forexample,[37]proposedOptEmbed,anovelembeddingsparsifi-
∗Correspondingauthor cationframeworkthatprunesredundantembeddingsbylearningan
importancescoreforeachfeature.Thesemethodsmostlyoptimize
alossfunctioncombiningarecommendationtermandasparsity
Permissiontomakedigitalorhardcopiesofallorpartofthisworkforpersonalor
regularizer.Apartfromsparsification/pruningmethods,another
classroomuseisgrantedwithoutfeeprovidedthatcopiesarenotmadeordistributed
forprofitorcommercialadvantageandthatcopiesbearthisnoticeandthefullcitation line of works featuring reinforcement learning (RL) techniques
onthefirstpage.Copyrightsforcomponentsofthisworkownedbyothersthanthe havealsoemerged.ThosemethodsadoptanRL-basedpolicynet-
author(s)mustbehonored.Abstractingwithcreditispermitted.Tocopyotherwise,or
worktosearchfortheoptimalembeddingsizesforeachuser/item,
republish,topostonserversortoredistributetolists,requirespriorspecificpermission
and/orafee.Requestpermissionsfrompermissions@acm.org. wheretheembeddingsizes(i.e.,actions)canbeselectedfroman
WSDM’24,March4–8,2024,Merida,Mexico action space consisting of either a predefined set of values [? ]
©2024Copyrightheldbytheowner/author(s).PublicationrightslicensedtoACM.
oracontinuousrange[41].Similartosparsificationmethods,the
ACMISBN979-8-4007-0371-3/24/03...$15.00
https://doi.org/10.1145/3616855.3635778 rewardfunctionsinRL-basedlightweightembeddingapproaches
557

WSDM’24,March4–8,2024,Merida,Mexico YunkeQu,TongChen,QuocVietHungNguyen,&HongzhiYin
alsobindtherecommendationqualitytermwithamemorycom-
plexitypenalty.Bytuningatrade-offcoefficientamongthetwo
terms,theycanadjusttheregularizationstrengthontheparameter
consumption,thusachievingthedesiredmemoryefficiency.
Despitethepossibilityofbalancingperformanceandembed-
ding parameter size, these two types of methods are still away
frompracticalusefortworeasons.Firstly,suchadesiredbalance
isachievedbyjointlyoptimizinganadditionalspacecomplexity
constraintontopoftherecommendationobjective.Forexample,
in[18],thisisformulatedasthedifferencebetweenthebudgeted
embeddingparametersizeandtheactualparameterconsumption
Figure1:OverviewofBET.
ofthecompressedembeddingtable.However,suchanimplicitloss
termmeansthattheresultantembeddingtablemaynotnecessarily aset-basedformulationofactions,andembedseachactionwith
meetthedesiredparameterbudgeteverytime[8].Moreover,the DeepSets[59],wherethelearnedhigh-qualityactionembeddings
optimizationqualityishighlysensitivetothetrade-offcoefficient, canefficientlyprovidereliableperformancefeedbackoneachtable-
whichneedstobeheuristicallytunedforeachmemorybudget. levelaction.Furthermore,theset-basedactionrepresentationscan
Thesecondreasonisthat,toachieveoptimalrecommendation beinductivelylearned,whichisessentialforouriterativesearch
performanceundereachmemorybudget,theembeddingsizeis algorithmthatconstantlygeneratesunseenactionsthatneedtobe
decidedonaninstance-by-instancebasisw.r.t.eachuser/item.Tak- evaluated.
ingarecentRL-basedmethodCIESS[41]asanexample,apolicy Tosummarize,ourworkpresentsthecontributionsbelow:
networkpredictstheoptimalactionforeverysingleuseranditem, • Weidentifythepracticalitybottlenecksofexistingembed-
basedonwhichthebackboneRSistrainedandevaluatedtocal-
dingsizesearchmethodsforlightweightRSs,namelythe
culatethereward,enablingtrainingthepolicynetwork.Onthe
implicitandnon-scalableparametersizeconstraintsformeet-
onehand,ideally,thepolicynetworkisexpectedtobeiteratively
ingdifferentmemorybudgets,andtheinefficientembedding
updatedw.r.t.eachinstance(i.e.,user/item),butthiscanbeprohib-
sizegenerationandevaluationforeveryinstance.
itivelyinefficientgiventhelargenumberofusersanditems.On • WeproposeBET,anoveltable-levelembeddingsizesearch
theotherhand,performingonlyoneupdateperbatch/epochleads
approachfeaturinganefficientactionsamplingstrategythat
toslowerconvergenceduetotheaggregatednatureofthereward
generatestable-levelactionsforallusersanditemsanda
function,andmaypotentiallyresultininferiorgeneralization[20].
DeepSets-basedfitnesspredictionnetworkthataccurately
Inresponsetobothchallenges,weproposeBudgetedEmbedding
predictstheirperformancetoreduceactionevaluationcosts.
Table(BET)forRSs,anautomatedinputembeddingsizesearch • Extensiveempiricalcomparisonshavebeencarriedouton
paradigmthatcanefficientlygeneratesizedecisionsandperform
tworeal-worlddatasetsbypairingstate-of-the-artembed-
optimizationattheembeddingtablelevel.AnoverviewofBETis
dingsizesearchalgorithmswithvariousbackboneRSs,which
providedinFigure1.Toaddressthefirstchallenge,weinnovatively
confirmtheadvantageousefficacyofBET.
propose a bounded sampler that draws embedding sizes for all
users/itemsfromacollectionofprobabilisticdistributions,withthe
2 PRELIMINARIES
guaranteethatthetotalparameterusageiscapped.Astheembed-
dingsizesforallinstancesintheembeddingtableareproducedall Toprovideadetailedresearchbackground,weherebydiscussrele-
atonce,wetermthisatable-levelaction.Thisstrategyfreesusfrom vantresearchtopics.
theneedformanuallydesigningandtuningtheimplicitparameter
2.1 DeepRecommenderSystems
constraintinthereward/lossfunction,andallowsustoenforcethe
memorybudgetwithanegligiblecost. Researchers have proposed numerous deep recommender mod-
Totacklethesecondchallenge,wefurtherpairthegenerated elstocapturetheuser-itemrelationships.Thefirstlineofdeep
table-levelactionswithafitnesspredictionnetworktoevaluatethe recommendersystemsarebasedonMLPs.Forinstance,Neural
qualityofthoseactions.Essentially,ineachsearchiteration,after CollaborativeFiltering(NCF)[15]integratesaMLPwithamatrix
samplingseveraltable-levelactions,weneedtoidentifytheones factorizationcomponenttolearnthetwo-wayinteractionsbetween
thatpromisehighrecommendationaccuracy.Astraightforward usersanditems.AutoRec[45]usesanautoencodertomodelthe
solutionistogreedilyevaluateeachcandidateactionbytraining user-iteminteractionsinalow-dimensionalhiddenspaceandper-
and evaluating a backbone RS from scratch with the suggested formcollaborativefiltering.Linetal.proposedanovelsequential
embeddingsizes[18,41,62?],whichapparentlyimpedesefficiency. recommender system, Dual Contrastive Network [31] that gen-
Onemaythinkofasurrogatefunction[3,8]that“predicts”the eratesself-supervisedsignalsbyconsideringbothuseranditem
fitnessofeachaction,insteadofexplicitlyevaluatingit.Accurately perspectivesandrefiningrepresentationlearningthroughdualrep-
predictingtheperformanceofthetable-levelactionsiscrucialyet resentationcontrastivelearning.InadditiontoMLP-basedmeth-
anothermajorchallengeinthisregard,aseitheroverestimatingor ods,graph-basedarchitectures[14,53,58]havealsobeenstudied.
underestimatinganaction’sperformancewilleventuallycausesub- Forexample,NeuralGraphCollaborativeFiltering(NGCF)[53]
optimalembeddingsizedecisions.Toalignwiththeevaluationof extendstraditionalneuralcollaborativefilteringbymodelinguser-
table-levelactionsinBET,ourfitnesspredictorinnovativelyutilizes iteminteractionswithgraphconvolutionnetworks.LightGCN[14]
558

BudgetedEmbeddingTableForRecommenderSystems WSDM’24,March4–8,2024,Merida,Mexico
takesinspirationfromNGCFandsimplifiesitbyremovingitsself- oritemIDstoareal-valuedembeddingvectore𝑛,where𝑛∈U∪V
indexeseitherauseroranitem.Notethatweonlyseparatelyuse𝑢
connection,featuretransformationandlinearactivationoperations.
and𝑣toindexusersanditemswhentheyneedtobedistinguished,
Anotherlineofrecommendersystemsarebasedonfactorization
machines.FactorizationMachines(FM)combinelinearregression e.g.,whenperformingpairwiseranking.Theverticalconcatena-
withmatrixfactorizationtechniquestohandlehigh-orderinterac- tionofallembeddingvectorsformstheembeddingtableEofsize
tions[42].[2]wasalsocreatedtominehigher-orderinteractions. (|U|+|V|)×𝑑 𝑚𝑎𝑥,where𝑑 isthemaximum/fullembedding
𝑚𝑎𝑥
|                   |        |             |                   | sizesupportedby𝐺 | Θ(·).Theembeddingsizesareadjustedviaabi- |     |     |     |
| ----------------- | ------ | ----------- | ----------------- | ---------------- | ---------------------------------------- | --- | --- | --- |
| Its deep variants | - QNFM | [7], DeepFM | [13] and xLightFM | [17]             |                                          |     |     |     |
narymaskM∈{0,1}(|U|+|V|)×𝑑𝑚𝑎𝑥,whichiscommonlyadopted
havebeenproposedtoo.Moreover,numerousmethodshavebeen
proposedtoleverageheterogeneousdataforrecommendation.For forembeddingsparsificationinlightweightrecommendersystems
instance,[6,12,25]havebeendevisedtoextractinformationfrom [35,37,41].Eachrowm𝑛inMisamaskvectorcorrespondingto
userreviewsorhashtags.[24,52]havebeenproposedtoexploit user/item𝑛.Givenasearchedembeddingsize𝑑 𝑛,wesetthefirst
videosandimagesforrecommendation.Locationinformationhas 𝑑 𝑛elementsofm𝑛toonestheremaining𝑑 −𝑑
𝑚𝑎𝑥 𝑛dimensionsto
alsobeenutilizedtoassistlocation-awarerecommendations[4]. zeros.Then,weperformelement-wisemultiplicationoftheembed-
dingtableEandthebinarymaskmatrixMtoadjusttheembedding
2.2 LightweightEmbeddingsFor sizesduringembeddinglook-up,i.e.,e𝑛 = (E⊙M)[𝑛]where[𝑛]
Recommenders retrievesthe𝑛-throwofamatrix.Misadaptivelyupdatedbased
Variousclassesofworkshaveinvestigatedlearningcompressed onthesampledactionsineveryiteration.Itisworthnotingthat,
inthedeploymentstage,onlytheheavilysparsifiedembedding
embeddingstoprovidealow-memoryalternativetotraditional
|                  |                |         |                     | tableE𝑠𝑝𝑎𝑟𝑠𝑒 | = E⊙Mwillbestored,wherethecostofstoring |     |     |     |
| ---------------- | -------------- | ------- | ------------------- | ------------ | --------------------------------------- | --- | --- | --- |
| embedding tables | in recommender | systems | [63]. For examples, |              |                                         |     |     |     |
zero-valuedentriescanbenegligiblewithsparsematrixstorage
featureselectionsearchmethods[32,36,54]aretrainedtolearn
techniques[44,49].Onceweobtainthesparseembeddingvectors,
importancescores,basedonwhichtheyfilterouttheunimportant
|     |     |     |     | therecommendermodel𝐺 |     | Φ(·) computesapreferencescore𝑦ˆ𝑢𝑣 |     |     |
| --- | --- | --- | --- | -------------------- | --- | --------------------------------- | --- | --- |
featurefields.Embeddingdimensionsearchapproaches[22,34,35,
representingpairwiseuser-itemsimilarity:
40,41,62]improvetraditionalrecommendersystemswithfixedand
|     |     |     |     |     | 𝑦ˆ𝑢𝑣 =𝐺 | ,e𝑣), 𝑢 | ∈U,𝑣 ∈V, |     |
| --- | --- | --- | --- | --- | ------- | ------- | -------- | --- |
uniformsizesbyintroducingmixeddimensionsforeachfeature. Θ(e𝑢 (1)
Quantization-basedmethods[5,9,10,19,21,26]reducesthepreci-
|     |     |     |     | where𝐺 | Θ(·)canbeanylatentfactor-basedrecommendermodel |     |     |     |
| --- | --- | --- | --- | ------ | ---------------------------------------------- | --- | --- | --- |
sionofnumericalvaluesandstoretheparameterswithlowerbits.
thatsupportspairwisescoring.
Featurehashingapproaches[1,11,28,30,33,46,47,57,60]utilize
Foroptimizingtherecommender,weadoptBayesianPersonal-
varioushashtrickstotransforminputvaluestoasmallerrange,
izedRanking(BPR)loss[43]:
thuscompressiontheembeddingtable.Knowledgedistillationtech-
∑︁
niquestrainasmallerstudentmodelfromalargerteachermodel L𝐵𝑃𝑅 = −ln𝜎(𝑦ˆ𝑢𝑣−𝑦ˆ𝑢𝑣′)+𝜂∥Θ∥2 , (2)
2
andhavebeenusedtolearnanembeddingtableofsmallersizes (𝑢,𝑣,𝑣′)∈D𝑡𝑟𝑎𝑖𝑛
fromlargerones[55,56].BETachievesdynamicembeddingsizes
|     |     |     |     | where | (𝑢,𝑣,𝑣′) ∈ D𝑡𝑟𝑎𝑖𝑛 | representsthetrainingsampleswhere |     |     |
| --- | --- | --- | --- | ----- | ----------------- | --------------------------------- | --- | --- |
andaimstofindtheoptimalembeddingsizeforeachfeature,soit
|     |     |     |     | user𝑢choosesitem𝑣overitem𝑣′,while𝑦ˆ𝑢𝑣 |     |     | and𝑦ˆ𝑢𝑣′ | respectively |
| --- | --- | --- | --- | ------------------------------------- | --- | --- | -------- | ------------ |
shouldbeclassifiedasaembeddingdimensionsearchapproach. representthepredictedpreferencesthatuser𝑢hasonitems𝑣and
𝑣′.𝜂∥Θ∥2
|                    |     |     |     |     | provides regularization | to  | prevent overfitting, | with a |
| ------------------ | --- | --- | --- | --- | ----------------------- | --- | -------------------- | ------ |
| 3 PROPOSEDAPPROACH |     |     |     |     | 2                       |     |                      |        |
scalingfactor𝜂.Ourgoalistosearchfortheoptimalembedding
Inanutshell,BEThasthreecomponents:(1)apre-trainedbackbone sizesforallusersanditemsunderstrictmemorybudgets,hence
recommenderwithafull-sizeembeddingtable𝐺 Θ(·)parameterized theoverallobjectiveisdefinedasfollows:
| byΘ;(2)anactionfitnesspredictionnetwork𝐹 |     |     | Φ(·)parameterized |     |     |     |        |     |
| ---------------------------------------- | --- | --- | ----------------- | --- | --- | --- | ------ | --- |
|                                          |     |     |                   |     |     | ∥   | M ∥ ,1 |     |
byΦ;and(3)anon-parametricactionsampler𝐻(·).Figure1pro- nL𝐵𝑃𝑅 s.t.1− 1 ≤𝑐,
|     |     |     |     |     | m i  |       | ×𝑑          | (3) |
| --- | --- | --- | --- | --- | ---- | ----- | ----------- | --- |
|     |     |     |     |     | Θ, Φ | (|U|+ | | V | ) 𝑚𝑎𝑥 |     |
videsanoverviewoftheworkflowofBET.Underpre-specified
memorybudgets,𝐻(·)samplesactionsfromasetofprobabilistic
|     |     |     |     | where∥M∥                        | 1,1countsthenumberofones,orequivalentlyretained |     |                        |     |
| --- | --- | --- | --- | ------------------------------- | ----------------------------------------------- | --- | ---------------------- | --- |
|     |     |     |     | parametersinthebinarymask,𝑐(0<𝑐 |                                                 |     | <1)isthetargetsparsity |     |
distributionsineachiteration.Eachactionspecifiestheembedding
sizesforallusersanditems.Afterwards,𝐹 Φ(·)estimatesthefitness rate,i.e.,theratiobetweenthenumbersofactiveparametersin
ofeachactionandselectsthebestactionpredicted.𝐺 Θ(·)isfurther sparsifiedandfullembeddingtables.
finetunedbyadoptingtheembeddingsizesinthechosenaction,
|     |     |     |     | 3.2 | Budget-AwareActionSampling |     |     |     |
| --- | --- | --- | --- | --- | -------------------------- | --- | --- | --- |
andisthenisevaluatedonahold-outdatasettoobtaintheactual
fitnessscore(i.e.,recommendationquality)oftheaction.Thisfacil- Herebyweintroduceanoveltable-levelactionsamplingstrategy.In
| itatestheoptimizationof𝐹 |     | Φ(·)byminimizingitspredictionerror, |     |     |     |     |     |     |
| ------------------------ | --- | ----------------------------------- | --- | --- | --- | --- | --- | --- |
eachsearchiteration,werandomlysampleasetofcandidateactions
| thusleadingustooptimalactionsundereachgivenmemorybudget |     |     |     | Q={𝑎 | ,...,𝑎 |     |     |     |
| ------------------------------------------------------- | --- | --- | --- | ---- | ------ | --- | --- | --- |
1 𝑚}.Eachactionassignsacontinuousembeddingsize
| 𝑇   |     |     |     | 𝑑   | N + | 𝑛   |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
a f t e r it e r a ti on s. In t h e r e mainderofthissection,weunfoldthe 𝑛 ∈ t o e v e r y u s e r or i t em ∈ U ∪ V .
≤ 𝑑𝑚 𝑎 𝑥
d e s i g no f e a c h co m po n e n t . A s w e ai m t o a v o i d o p t im iz i n gt he s ele cte d actiontowardsan
implicit,manuallytunedmemorycostterm,weproposetodirectly
3.1 RecommenderwithEmbeddingMasking
drawatable-levelactionthat:(1)makesallgeneratedembedding
LetUandVdenoteasetofusers𝑢anditems𝑣,respectively.The sizes conditioned on a certain distribution; and (2) ensures the
embeddingtableintherecommendermapseachinteger-valueduser totalparametersizeofallembeddingsiscappedatthebudgeted
559

WSDM’24,March4–8,2024,Merida,Mexico YunkeQu,TongChen,QuocVietHungNguyen,&HongzhiYin
parameterconsumption.Inshort,(1)essentiallynarrowstheaction
spacetomitigatethedifficultyofsearchingfromahugecollection
ofcompletelyrandomactions,while(2)guaranteesthatthetable-
levelactionstrictlymeetsthememorybudgetinthefirstplace.
Togenerateanaction𝑎,wefirstdeterminetwoprobabilitydistri-
| butions𝑃 | Uand𝑃 | Vrespectivelyforusersanditems.Meanwhile,to |     |     |     |     |     |     |
| -------- | ----- | ------------------------------------------ | --- | --- | --- | --- | --- | --- |
introduceinductivebiastotheactionsampler,insteadofresorting Figure2:Exampleofourset-basedactionformulation.Sup-
| toafixeddistributionthroughoutthesearchprocess,𝑃 |     |     |     |     |     | and𝑃 |                                         |             |
| ------------------------------------------------ | --- | --- | --- | --- | --- | ---- | --------------------------------------- | ----------- |
|                                                  |     |     |     |     | U   | V    | posewehavethreelegitimateembeddingsizes | {16,32,64}, |
arebothrandomlychosenfromasetofcandidatedistributions four users (red) and two items (green). Then, size 16 is a
withon-the-flyparameterization.Specifically,weutilizeapower setcontaininguser1,user2anditem4,whichmeanstheir
lawdistribution,atruncatedexponentialdistribution,atruncated
embeddingsizesare16.Similarly,theactionspecifiesthe
normaldistributionandalognormaldistribution.Forsimplicity,
embeddingsizesofuser3anditem5tobe32.Size64isnot
weletthetwoselecteddistributionsrespectivelybeparameterized usedbyanyusers/items.
by𝛽 Uand𝛽
V.Ineachiteration,theparametersarealldetermined
uniformlyatrandom:
|     |     | 𝛽 ,𝛽 | ∼Uniform(0,𝛽 | 𝑚𝑎𝑥), |     | (4) |     |     |
| --- | --- | ---- | ------------ | ----- | --- | --- | --- | --- |
U V
| where𝛽 | 𝑚𝑎𝑥 | isthemaximalvalueallowed.Notably,theembedding |     |     |     |     |     |     |
| ------ | --- | --------------------------------------------- | --- | --- | --- | --- | --- | --- |
sizesofeachfield(i.e.,usersanditems)arederivedbyindependently
| samplingfromtwodistributions𝑃 |     |     |     | and𝑃 V.Thisisbecauseeach |     |     |     |     |
| ----------------------------- | --- | --- | --- | ------------------------ | --- | --- | --- | --- |
U
fieldmayhavedistinctproperties[37]anddifferentdistributions
areneededtomodeltheembeddingsizesofusersanditems.
Afterthedistributionsaredetermined,wesample|U|and|V|
| probabilitiesrespectivelyfrom𝑃 |     |     | and𝑃 | V.Thesetofprobabilities |     |     |     |     |
| ------------------------------ | --- | --- | ---- | ----------------------- | --- | --- | --- | --- |
U
| arerespectivelydenotedas{𝑝 |     |        | | U |             | ∼𝑃 and{𝑝      | | V | ∼𝑃 |      |     |     |
| -------------------------- | --- | ------ | ----------------- | ------------- | -------- | ---- | --- | --- |
|                            |     |        | 𝑖} 𝑖              | U             | 𝑗} 𝑗     | V.We |     |     |
|                            |     |        | = 1               |               | =1       |      |     |     |
| thennormalizeall𝑝          |     | 𝑖 and𝑝 | 𝑗 asthefollowing: |               |          |      |     |     |
|                            |     |        | 𝑝 𝑖               | 𝑝 𝑗           |          |      |     |     |
|                            |     | 𝑝˜𝑖 =  | , 𝑝˜𝑗             | =             | ,        | (5)  |     |     |
|                            |     |        | (cid:205)|U|𝑝     | (cid:205)|V|𝑝 |          |      |     |     |
|                            |     |        | 𝑖                 |               | 𝑗        |      |     |     |
|                            |     |        | 𝑖                 | 𝑗             |          |      |     |     |
where𝑝˜𝑖/𝑝˜𝑗 Figure3:OverviewoftheDeepSets-basedfitnesspredictor.
indicatesthefractionofparameterseachuser/itemre-
ceivesamongallusers/items.Next,weobtaintheactualembedding
sizesbyapplyingthefractiononthememorybudget: convergenceandselecttheactionthatyieldsthebestfinalrecom-
mendationqualityonthevalidationset.However,thisapproach
|     | 𝑑 = | ⌊𝑝˜𝑖 ·𝑤·𝑑 | ·(|U|+|V|)⌋, | 𝑖   | =1,2,···,|U|, |     |     |     |
| --- | --- | --------- | ------------ | --- | ------------- | --- | --- | --- |
𝑖 𝑚𝑎𝑥 facesinevitablecomputationalburdensgiventhe𝑚trainingand
(6)
| 𝑑   | 𝑗 = ⌊𝑝˜𝑗 ·(1−𝑤)·𝑑 |     | 𝑚𝑎𝑥 ·(|U|+|V|)⌋, | 𝑗   | =1,2,···,|V|, |     |     |     |
| --- | ----------------- | --- | ---------------- | --- | ------------- | --- | --- | --- |
evaluationprocessesneededpersearchiteration.
where𝑤 InBET,weutilizeanactionfitnesspredictor,whichinductively
controlstheproportionofparametersallocatedtothe
learnsdistinctembeddingsofactionsandpredictsitsfitnessscore
| users.Inpractice,𝑤 |     | canbeempiricallydefined,suchasaneven |     |     |     |     |     |     |
| ------------------ | --- | ------------------------------------ | --- | --- | --- | --- | --- | --- |
(i.e.,recommendationquality)basedontheactionembeddings.As
| split(i.e.,0.5).InBET,𝑤 |     |     | issampledfromauniformdistribution |     |     |     |     |     |
| ----------------------- | --- | --- | --------------------------------- | --- | --- | --- | --- | --- |
discussedearlier,learningexpressiverepresentationsofdifferent
| eachtimeatable-levelactionisgenerated,i.e.,𝑤 |     |     |     |     | ∼Uniform(0,1), |     |     |     |
| -------------------------------------------- | --- | --- | --- | --- | -------------- | --- | --- | --- |
actionsisacrucialyetnon-trivialtaskforeffectivefitnesspredic-
soastoprobemoreembeddingsizeallocationstrategiesinthe
tion,especiallyconsideringtheneedforinductivelycomposing
iterativesearchprocess.
embeddingsforunseenactionsineverynewsearchiteration.
With|U|+|V|embeddingsizesderived,wenowallocatethem
Thus,weproposeanovelactionfitnesspredictionnetworkbased
toeachuseranditem.Previousstudies[37,48,62]haveshownthat
onthenotionofsetrepresentationlearning[50,59].Beforedelving
morefrequentusersanditemstendtobemoreinformativethan
long-tailones,hencegenerallybenefitfromalargerembedding intothefitnesspredictionnetwork,wefirstdetailtheset-based
formulationofeachaction.Eachactionisregardedasacollection
dimensionwhichallowsmoreinformationtobeencoded.Therefore, 𝑑
weranktheusersbytheirfrequencyandallocatethe𝑛-thlargest ofsets𝑎={S𝑑} 𝑚 𝑎𝑥,whereeachsetS𝑑 ={𝑛|∀𝑛∈U∪V,𝑑 𝑛 =𝑑}
𝑑 =1
|     |     |     |     |     |     |     | storestheusersanditemsthatusetheembeddingsize𝑑 | ∈ [1,𝑑 𝑚𝑎𝑥]. |
| --- | --- | --- | --- | --- | --- | --- | ---------------------------------------------- | ------------ |
userembeddingsizetothe𝑛-thfrequentuser.Similarly,weassign
∅ifthereisnouseroritemassignedtoembeddingsize𝑑.
| embeddingsizestoitemsbasedontheirfrequency.Assuch,weare |     |     |     |     |     |     | S𝑑 = |     |
| ------------------------------------------------------- | --- | --- | --- | --- | --- | --- | ---- | --- |
capableofsampling𝑚randomtable-levelactionsineachsearch Atoyexamplewithisgiveninfigure2.Assuch,thisallowsusto
buildourfitnesspredictoruponDeepSets[59]owingtoitsability
iterationtofacilitatethesubsequentsteps.
tolearnpermutation-variantrepresentationsofsets.
3.3 FitnessPredictionNetwork
Thefitnesspredictionnetworkconsistsoffourcomponents:a
Ineachiteration𝑡 wesampleasetof𝑚actions,denotedasQ𝑡.To userencoder𝜌 (·),anitemencoder𝜌
U V (·),anembeddingsize
selecttheoptimalactionfromQ𝑡,astraightforwardapproachisto encoder𝜇(·),andadecoder𝜋(·),allofwhichbearadistinctMLP.
paireachsampledactionwithafreshrecommender,trainituntil Encoders𝜌 (·)/𝜌 (·)takesomecontextualinformationabouta
U V
560

BudgetedEmbeddingTableForRecommenderSystems WSDM’24,March4–8,2024,Merida,Mexico
user/item,andproducetheircorrespondingrepresentations.Previ- Algorithm1EmbeddingSizeSearchwithBET
ousstudies[41,62]havedemonstratedthesuitabilityofusers’/items’ 1: InitializeΘandΦ,setA←∅;
popularityandcurrentembeddingsizesasthecontextinformation Train𝐺 Θ(·)tillconvergencew.r.t.Eq.2;
2:
forembeddingsizesearch.Weinheritthisdesignbyestablishinga for𝑡 =1,···,𝑇 do
3:
hierarchical,set-compatibleactionrepresentationlearningscheme.
4: Drawdistributionsandtheirparametersw.r.t.Eq.4;
Specifically,𝜌 (·)and𝜌 (·)respectivelytakestheuseranditem Draw𝑚actionsQ𝑡 ={𝑎 ,...,𝑎
|     | U   | V   |     |     |     |     | 5:  |     |     | 1 𝑚}withEq.5andEq.6; |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | -------------------- | --- | --- | --- |
frequenciestogeneratefrequency-weightedembeddings: 6: if0≤𝑡 mod5≤2then
|            |         |               | 𝑓      |          |           |      |     |         | 𝑎 𝑡 ←StrategyI;       |        |     |     |     |
| ---------- | ------- | ------------- | ------ | -------- | --------- | ---- | --- | ------- | --------------------- | ------ | --- | --- | --- |
|            |         | =𝜌            | 𝑢      | ), 𝑢 ∈U, |           |      | 7:  |         |                       |        |     |     |     |
|            | 𝒒𝑢      | U (           |        |          |           |      |     | elseif𝑡 | mod5=3then            |        |     |     |     |
|            |         | max𝑢′∈U       | 𝑓      | 𝑢′       |           |      | 8:  |         |                       |        |     |     |     |
|            |         |               |        |          |           | (7)  |     |         | 𝑎 ←StrategyII;        |        |     |     |     |
|            |         |               | 𝑓      |          |           |      | 9:  |         | 𝑡                     |        |     |     |     |
|            |         | =𝜌            | 𝑣      | ), 𝑣 ∈V, |           |      |     |         | 𝑡                     |        |     |     |     |
|            | 𝒒𝑣      | V (           |        |          |           |      | 1 0 | : else  | if m o d 5 = 4        | t h en |     |     |     |
|            |         | max𝑣′∈V       | 𝑓      | 𝑣′       |           |      |     |         |                       |        |     |     |     |
|            |         |               |        |          |           |      | 1 1 | :       | 𝑎 𝑡 ← S tr at eg y II | I ;    |     |     |     |
| where each | 𝑓 𝑢/𝑓 𝑣 | is normalized | by the | maximum  | user/item | fre- |     | endif   |                       |        |     |     |     |
12:
| quencyobserved. |     |     |     |     |     |     |     | FinetuneΘw.r.t.E⊙M𝑎𝑡 |     | andEq.2 |     |     |     |
| --------------- | --- | --- | --- | --- | --- | --- | --- | -------------------- | --- | ------- | --- | --- | --- |
13:
| Asmentionedabove,withinanaction𝑎,eachsetS𝑑 |     |     |     |     |     | contains |     | 𝑟   | ←Eq.13 |     |     |     |     |
| ------------------------------------------ | --- | --- | --- | --- | --- | -------- | --- | --- | ------ | --- | --- | --- | --- |
|                                            |     |     |     |     |     |          | 14: | 𝑎𝑡  |        |     |     |     |     |
allusersanditemswithembeddingsize𝑑.Toobtainembedding𝒔𝑑 A←A∪(𝑎 ,𝑟
|     |     |     |     |     |     |     | 15: |     | 𝑡 𝑎𝑡 ); |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ------- | --- | --- | --- | --- |
ofsetS𝑑,wefirstlyfusetherepresentationsofallinvolvedusers 16: for𝑗 =1,···,𝑁 do
anditemsusingmeanaggregation,andthenappendtheexplicit 17: Randomlysample(𝑎 𝑗 ,𝑟 𝑎𝑗 )fromA;
| embeddingsizeinformation: |     |     |     |     |     |     |     |     | 𝑟ˆ𝑎𝑗 ←Eq.10; |     |     |     |     |
| ------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | ------------ | --- | --- | --- | --- |
18:
UpdateΦw.r.t.Eq.11;
|     |     | (cid:16)(cid:104) 1 | ∑︁   | 𝑑 (cid:105)(cid:17) |     |     | 19: |                                              |     |     |     |     |     |
| --- | --- | ------------------- | ---- | ------------------- | --- | --- | --- | -------------------------------------------- | --- | --- | --- | --- | --- |
|     |     | =𝜇                  |      |                     | ,   |     |     |                                              |     |     |     |     |     |
|     | 𝒔𝑑  |                     | 𝒒𝑛;  | 𝑑                   |     | (8) | 20: | endfor                                       |     |     |     |     |     |
|     |     | |S𝑑|                |      | 𝑚𝑎𝑥                 |     |     |     |                                              |     |     |     |     |     |
|     |     |                     | 𝑛∈S𝑑 |                     |     |     | 21: | endfor                                       |     |     |     |     |     |
|     |     |                     |      |                     |     |     | 22: | Performselectiveretrainingandobtain𝑎∗←Eq.14. |     |     |     |     |     |
where[;]representsconcatenation.Withtherepresentationsgen-
| eratedforall𝑑 | 𝑚𝑎𝑥 | sets,wederivetheembeddingfortheentire |     |     |     |     |     |     |     |     |     |     |     |
| ------------- | --- | ------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
action𝑎byfurthermergingallsetrepresentations:
|     |     |     |         |     |     |     | whereeval(·)evaluatestherecommendationquality,D𝑣𝑎𝑙 |     |                                        |     |     |     | isthe |
| --- | --- | --- | ------- | --- | --- | --- | -------------------------------------------------- | --- | -------------------------------------- | --- | --- | --- | ----- |
|     |     |     | 𝑑       |     |     |     |                                                    |     | isthebinarymaskcorrespondingtoaction𝑎, |     |     |     |       |
|     |     |     | 1 ∑︁𝑚𝑎𝑥 |     |     |     | validationset,M𝑎                                   |     |                                        |     |     |     |       |
|     |     | =   |         | ,   |     |     |                                                    |     |                                        |     |     |     |       |
𝒉𝑎 𝑑 𝒔𝑑 (9) andthedenominatoristherecommendationqualityofthepre-
𝑚𝑎𝑥
𝑑=1 trained backbone recommender𝐺 Θ(·) with the full embedding
|              |                                        |     |     |     |     |     | table.Hence,𝑟 |     | 𝑎 canbeinterpretedastheratiobetweenthetwo |     |     |     |     |
| ------------ | -------------------------------------- | --- | --- | --- | --- | --- | ------------- | --- | ----------------------------------------- | --- | --- | --- | --- |
| whereweuse𝒉𝑎 | todenoteanactionembedding.Anadditional |     |     |     |     |     |               |     |                                           |     |     |     |     |
recommendationaccuracyobtainedbythesparsifiedembeddings
benefitfromtheset-basedactionembeddingsisthat,wheneverthe
andthefullembeddings.Theimplementationofeval(·)canfollow
actionsamplerdrawsanyactionthatisnewtothefitnesspredictor
mostcommonlyusedrecommendationmetricslikeRecall@𝑘and
(whichiscommonlythecaseinembeddingsizesearch),itallows
NDCG@𝑘
forgeneratingtheactionembeddinginaninductivefashionwith [14,43],whereweadoptanensembleofbothmetrics
underdifferentvaluesof𝑘:
theavailablecontextinformationandtheupdatedsetformulation.
Witheachactionembedding𝒉𝑎,thedecoder𝜋(·)takes𝒉𝑎and ∑︁ (cid:205) 𝑘∈KRecall@𝑘 𝑢+NDCG@𝑘
|     |     |     |     |     |     |     | eval(E⊙M|D𝑣𝑎𝑙)= |     |     |     |     |     | 𝑢 , |
| --- | --- | --- | --- | --- | --- | --- | --------------- | --- | --- | --- | --- | --- | --- |
(13)
| outputs𝑟ˆ𝑎,whichisthepredictedfitnessscoreofaction𝑎: |     |     |     |     |     |     |     |     |     |     | 2|K||U| |     |     |
| ---------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------- | --- | --- |
𝑢∈U
𝑟ˆ𝑎 =𝜋(𝒉𝑎). (10) wherewethechoicesof𝑘coverK ={5,10,20}inourpaper.
Thegroundtruthsamplescanbethusgeneratedbygathering
Wewilldetailhowtheentirefitnesspredictionnetwork𝐹
Φ(·)is
differentaction-fitnesspairs.Insteadofconstructingapoolofsuch
optimizedalongwiththesearchprocessinthenextsection. trainingsamplesandtrain𝐹
Φ(·)upfront,weincrementallyaddone
|     |     |     |     |     |     |     | trainingsampleineverysearchiteration𝑡 |     |     |     | tooptimize𝐹 |     | Φ(·) on |
| --- | --- | --- | --- | --- | --- | --- | ------------------------------------- | --- | --- | --- | ----------- | --- | ------- |
3.4 FitnessPredictorTraining
thego.Thetrainingsampleisconstructedbyfirstlyidentifying
Thoughbearingarelativelysimplestructure,thefitnesspredictor apromisingactionfrom Q𝑡,denotedby𝑎 𝑡,andthenobtaining
still needs to be trained with some ground truth samples. The 𝑟 byevaluating𝑎 onthefinetuned𝐺 Θ(·).Comparedwithmost
|                           |     |     |                                |     |     |     | 𝑎𝑡  |     | 𝑡   |     |     |     |     |
| ------------------------- | --- | --- | ------------------------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| fitnesspredictionnetwork𝐹 |     |     | Φ(·)isoptimizedbyminimizingthe |     |     |     |     |     |     |     |     |     |     |
RL-basedembeddingsizesearchmethods,therequirednumberof
meansquarederrorbetweenthepredictedfitnessscore𝑟ˆ𝑎andthe
fitnessevaluationwiththerecommendationmodelwillbereduced
actualone𝑟
𝑎withgradientdescent: from𝑚×𝑇 tomerely𝑇,where𝑇 isthetotalnumberofiterations
|          | ∑︁  |                       |     | ∑︁  |             |     | aswellasthegroundtruthsamplesforoptimizing𝐹 |     |     |     |     | Φ(·). |     |
| -------- | --- | --------------------- | --- | --- | ----------- | --- | ------------------------------------------- | --- | --- | --- | --- | ----- | --- |
| Φ=argmin |     | (𝑟 𝑎−𝐹 Φ′(𝑎))2=argmin |     |     | (𝑟 𝑎−𝑟ˆ𝑎)2. |     |                                             |     |     |     |     |       |     |
(11)
|     | Φ′  |     |     | Φ′  |     |     |     |                                       |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------------------------------- | --- | --- | --- | --- | --- |
|     | ∀𝑎  |     |     | ∀𝑎  |     |     | 3.5 | ActionSelectionandEmbeddingRetraining |     |     |     |     |     |
Theactualfitnessscore𝑟
𝑎,i.e.,recommendationqualityofthe ThepseudocodeforBETispresentedinAlgorithm1.Amongits𝑇
action,canbeevaluatedonthebackbonerecommender𝐺
Θ(·)after
searchiterations,weutilizethreedifferentstrategiestopickone
| beingfinetunedwithanaction𝑎w.r.t.Eq.2: |     |     |     |     |     |     | action𝑎 |     |                             |     |                      |     |     |
| -------------------------------------- | --- | --- | --- | --- | --- | --- | ------- | --- | --------------------------- | --- | -------------------- | --- | --- |
|                                        |     |     |     |     |     |     |         | 𝑡   | fromthecandidateactionsetQ𝑡 |     | (lines4-12).Then,the |     |     |
eva l (E ⊙ M 𝑎 | D 𝑣𝑎𝑙) r ec o m m e n d e r 𝐺 Θ ( · ) is fi n e t u n ed b y a d o p t in g 𝑎 𝑡 an d e v a lu a t e d o n
|     |     | 𝑟 𝑎 = |     | ,   |     | (12) |     |     |     |     |     |     |     |
| --- | --- | ----- | --- | --- | --- | ---- | --- | --- | --- | --- | --- | --- | --- |
e v al (E |D 𝑙) th e v al id a ti o n s et ( l i ne s 13 - 1 4 ) ,w h er e t h e p r od u c ed ( 𝑎 𝑡 , 𝑟 𝑎𝑡 ) s a m p l e
𝑣 𝑎
561

WSDM’24,March4–8,2024,Merida,Mexico YunkeQu,TongChen,QuocVietHungNguyen,&HongzhiYin
ispoppedintothepopulationsetAtofacilitatetrainingthefitness • PEP[35]:Itadaptivelyprunestheembeddingparameters
predictionnetwork𝐹 Φ(·)(lines16-20).Finally,aselectiveretraining basedonalearnedpruningthresholdlearnedalongwiththe
processisconductedwiththetop-rankedactionsinthepopulation model’sotherparametersduringthetrainingprocess.
inordertoidentifythebestembeddingsizedecisionforallusersand • ESAPN[?]:ItusesanRLagentwhichperformshardselec-
items.Weprovidefurtherdetailsaboutactionselectionstrategies tiononembeddingsizesforusersanditemsbasedonthe
andretrainingthesparsifiedembeddingsbelow. memorycomplexityandrecommendationperformance.
• OptEmbed[37]:Itprunesredundantembeddingsbasedon
3.5.1 DiversifyingtheActionSpace. Theiterativeinputembedding
learnablepruningthresholdsindicativeoffeatures’impor-
sizesearchcontains𝑇 iterations.Ineachiteration𝑡,theselected
tanceandderivestheoptimalembeddingsizeforeachfield
action𝑎 𝑡 isaddedtothepopulationsetAwithitsassociatedfitness
usingevolutionarysearch.
score. For efficiency consideration, in each iteration𝑡, we only
• CIESS[41]:ItisanRL-basedmethodthatchoosesembedding
computetheactualfitnessscoreforaction𝑎 𝑡,whichisselected
sizesfortheusersanditemsfromacontinuousdomain.
fromcandidateactionsQ𝑡withoneofthethreefollowingstrategies:
• SingleandUniform(SU):Allusersanditemsshareequal
I: Weuseourfitnesspredictionnetwork𝐹 Φ(·)topredictthe
andfixedembeddingsizes.
fitnessscoreofeachcandidateactions,andgreedilyselects • SingleandRandom(SR):Theembeddingsizesoftheusers
theactionpredictedtohavethehighestfitnessscore,i.e.,𝑎 𝑡 = anditemsaresampledfromauniformdistribution.
argmax𝑎∈Q𝑡 𝐹 Φ(𝑎).Inessence,𝐹 Φ(·)isasurrogatefunction
thatistrainedtoapproximateEq.12andissubstantiallymore
cost-effectivethanevaluatingall𝑚actionsviarecommender
finetuning. 4.2 EvaluationProtocols
II: WerandomlyselectoneactionfromtheQ𝑡 todiversifythe
Alltheaforementionedmethodsareevaluatedontworeal-world
trainingsamplesfor𝐹 Φ(·)bypreventingitfromoverfitting
datasets:Gowalla[29]andYelp2018[53].Thefirsthas1,027,370
somespecificactiondistributionsinthepopulationA.
interactionsbetween29,858usersand40,981itemswhilethelatter
III: Weidentifycurrentlythebestaction(withthehighest𝑟 𝑎)
has1,561,147interactionsbetween31,668usersand38,048items.
inA.AllactionsinQ𝑡 andthebestactionareinductively
Wetake50%,25%and25%ofthetwodatasetsfortraining,vali-
embeddedintovectorrepresentationsusingEq.9.Then,by
dation,andtest.Tomeasuretherecommendationperformanceof
calculatingthepairwiseEuclideandistance,weselectaction thebackbonerecommender,Recall@𝑘andNDCG@𝑘areusedas
𝑎 𝑡 ∈Q𝑡 bylocatingthebestaction’snearestneighborinthe evaluationmetrics,where𝑘issettoeither5or20.Totesttherecom-
embeddingspace.
mendationperformanceofCIESS,PEP,SUandSR,threedifferent
3.5.2 SelectiveRetrainingforSparsifiedEmbeddings. After𝑇search sparsityratios(𝑐)of80%,90%and95%areused.Foreachmethod,
iterations,fromthepopulationweidentifythetopfiveactionswith thecompressedembeddingtableisensuredtohavenomorethan
thehighest𝑟 𝑎 onthevalidationset,denotedasA′.Eachaction 𝑐·𝑑 𝑚𝑎𝑥 ·(|U|+|V|)usableparameterandthemaximalembed-
𝑎∈A′ispairedwithafreshbackbonerecommendermodel,which dingsizeis𝑑 𝑚𝑎𝑥 =128.However,sinceESAPNandOptEmbedare
istrainedfromscratchonthetrainingsetuntilconvergence.Next, notdesignedtopreciselycontroltheembeddingsparsityandfocus
weevaluatethetrainedrecommendersandselectthefinalaction moreontheperformance,thissectiononlyreportstheperformance
𝑎∗thatyieldsthebestvalidationperformance: associatedwiththeirfinalembeddingtablesafterpruning.
𝑎∗=argmax𝑟 𝑎 , (14)
𝑎∈A′
withwhichthesparsifiedembeddingE𝑠𝑝𝑎𝑟𝑠𝑒isobtainedandstored 4.3 ImplementationNotesforBET
forinference.
HerebywedetailtheimplementationofBET.Thenumberofsearch
4 EXPERIMENTS
iterations𝑇is10.Themaximalvaluesofthedistributionparameters
𝛽 𝑚𝑎𝑥 are set to 20 for power law distribution, 20 for truncated
ThissectiondetailstheexperimentalresultsofBET’sperformance.
normaldistribution,5fortruncatedexponentialdistributionand
0.5forlognormaldistribution.Themaximalembeddingsize𝑑
𝑚𝑎𝑥
4.1 BaseRecommendersandComparative
is128andtheminimalembeddingsize𝑑 𝑚𝑖𝑛is1.Ineachiteration,
Methods
thepre-trainedbackbonerecommenderisfinetunedfor10epochs
OnecancombineBETwithdifferentembedding-basedrepresenta- (i.e.,ℎ=10)whenthebackbonerecommenderisLightGCNorNCF.
tionlearningbackbonerecommendermodels.Wetestedtheeffec- WhenNGCFisused,thebackbonerecommenderisfinetunedfor
tivenessofourapproachwiththreecommonlyusedrecommender 15epochs(i.e.,ℎ =15).Forfinetuning,theinitiallearningrateis
modelsasthebackbonerecommender𝐹 Φ:NCF[15],NGCF[53] 0.03anddecaysevery200stepswithadecayratioof0.98.The
andLightGCN[14].Weusedthesamesettingsasreportedintheir numberoffitnesspredictionupdatesineachiteration,or𝑁,isset
originalworksandreplacedtheembeddingtablewithonewith to2.Theuseranditemencodershaveinputsize1,outputsize16,
adjustableembeddingsizestodemonstratetheversatilityandgen- andhiddensize16.Thesizeencoderhasinputsize17,outputsize
eralizabilityofourmethodacrossvariousbackbonerecommenders. 64,andhiddensize64.Thedecoderhasinputsize64,outputsize1,
WecompareBETwiththefollowingmodel-agnosticembedding andhiddensize64.AlltheMLP-basedencodersanddecodershave
sizesearchalgorithms: twolayerswiththeLeakyRelU[38]activationfunction.
562

BudgetedEmbeddingTableForRecommenderSystems WSDM’24,March4–8,2024,Merida,Mexico
LightGCN NGCF NCF
Method Sparsity R@5 N@5 R@20 N@20 Sparsity R@5 N@5 R@20 N@20 Sparsity R@5 N@5 R@20 N@20
ESAPN 75% 0.0741 0.1173 0.1579 0.1329 83% 0.0627 0.1060 0.1396 0.1193 74% 0.0498 0.0718 0.1280 0.0959
OptEmb 74% 0.0591 0.0983 0.1314 0.1115 75% 0.0510 0.0860 0.1227 0.1005 82% 0.0330 0.0492 0.0877 0.0653
PEP 0.0715 0.1189 0.1588 0.1347 0.0656 0.1049 0.1524 0.1245 0.0498 0.0704 0.1282 0.0957
SU 0.0756 0.1219 0.1674 0.1400 0.0619 0.0961 0.1466 0.1170 0.0481 0.0662 0.1235 0.0916
SR 80% 0.0708 0.1150 0.1583 0.1323 80% 0.0512 0.0815 0.1223 0.0982 80% 0.0478 0.0656 0.1243 0.0910
CIESS 0.0777 0.1263 0.1750 0.1461 0.0676 0.1084 0.1504 0.1251 0.0550 0.0744 0.1307 0.0997
BET 0.0797 0.1303 0.1753 0.1483 0.0643 0.1039 0.1454 0.1204 0.0511 0.0723 0.1294 0.0973
𝑝-value 0.0024 0.0001 0.0391 0.0012 0.7815 0.2179 0.0514 0.0924 0.1962 0.1337 0.2578 0.0414
PEP 0.0594 0.0992 0.1274 0.1102 0.0552 0.0914 0.1327 0.1081 0.0414 0.0631 0.1121 0.0839
SU 0.0646 0.1041 0.1477 0.1217 0.0589 0.0935 0.1380 0.1115 0.0413 0.0548 0.1112 0.0796
SR 90% 0.0617 0.1013 0.1403 0.1171 90% 0.0466 0.0764 0.1123 0.0911 90% 0.0399 0.0536 0.1069 0.0769
CIESS 0.0721 0.1193 0.1589 0.1353 0.0601 0.0980 0.1380 0.1140 0.0448 0.0613 0.1131 0.0841
BET 0.0736 0.1212 0.1620 0.1376 0.0623 0.1012 0.1426 0.1177 0.0434 0.0648 0.1122 0.0845
𝑝-value 0.0165 0.0481 0.0091 0.0226 0.0005 0.0205 0.0601 0.0232 0.1454 0.0554 0.6608 0.0655
PEP 0.0372 0.0666 0.0803 0.0712 0.0247 0.0471 0.0674 0.0554 0.0351 0.0591 0.0897 0.0712
SU 0.0446 0.0727 0.1085 0.0872 0.0527 0.0870 0.1213 0.1007 0.0336 0.0478 0.0952 0.0682
SR 95% 0.0500 0.0834 0.1178 0.0975 95% 0.0438 0.0739 0.1040 0.0859 95% 0.0329 0.0489 0.0918 0.0674
CIESS 0.0513 0.0853 0.1214 0.0997 0.0505 0.0856 0.1129 0.0964 0.0361 0.0567 0.0933 0.0717
BET 0.0627 0.1037 0.1374 0.1171 0.0528 0.0883 0.1172 0.9980 0.0388 0.0616 0.0963 0.0756
𝑝-value 0.0001 0.0002 0.0001 0.0001 0.1896 0.0638 0.7269 0.3608 0.0321 0.1107 0.1104 0.0010
(a)ResultsonGowalla
LightGCN NGCF NCF
Method Sparsity R@5 N@5 R@20 N@20 Sparsity R@5 N@5 R@20 N@20 Sparsity R@5 N@5 R@20 N@20
ESAPN 73% 0.0294 0.0696 0.0812 0.0773 71% 0.0214 0.0538 0.0632 0.0603 76% 0.0153 0.0342 0.0490 0.0430
OptEmb 80% 0.0183 0.0424 0.0534 0.0489 67% 0.0133 0.0301 0.0412 0.0369 77% 0.0076 0.0161 0.0238 0.0203
PEP 0.0253 0.0605 0.0723 0.0682 0.0086 0.0167 0.0275 0.0223 0.0130 0.0236 0.0406 0.0327
SU 0.0289 0.0665 0.0822 0.0758 0.0223 0.0517 0.0665 0.0603 0.0131 0.0226 0.0465 0.0351
80% 80% 80%
SR 0.0253 0.0588 0.0783 0.0698 0.0212 0.0499 0.0618 0.0573 0.0101 0.0183 0.0342 0.0268
CIESS 0.0292 0.0692 0.0839 0.0783 0.0233 0.0566 0.0701 0.0652 0.0175 0.0377 0.0533 0.0474
BET 0.0310 0.0726 0.0873 0.0816 0.0254 0.0601 0.0741 0.0685 0.0194 0.0451 0.0620 0.0554
𝑝-value 0.0008 0.0309 0.0004 0.0109 0.0412 0.0418 0.0082 0.0024 0.0387 0.0122 0.0483 0.0341
PEP 0.0224 0.0531 0.0657 0.0610 0.0080 0.0153 0.0276 0.0215 0.0139 0.0242 0.0427 0.0335
SU 0.0230 0.0544 0.0722 0.0648 0.0205 0.0528 0.0622 0.0592 0.0119 0.0201 0.0416 0.0309
SR 90% 0.0210 0.0476 0.0642 0.0573 90% 0.0195 0.0449 0.0573 0.0524 90% 0.0089 0.0170 0.0309 0.0242
CIESS 0.0263 0.0649 0.0730 0.0705 0.0232 0.0551 0.0669 0.0619 0.0153 0.0350 0.0500 0.0442
BET 0.0284 0.0674 0.0816 0.0762 0.0246 0.0586 0.0736 0.0676 0.0173 0.0400 0.0565 0.0499
𝑝-value 0.0045 0.0060 0.0051 0.0006 0.0012 0.0007 0.0102 0.0069 0.0234 0.0067 0.0426 0.0118
PEP 0.0199 0.0496 0.0600 0.0561 0.0075 0.0143 0.0259 0.0206 0.0125 0.0244 0.0399 0.0330
SU 0.0217 0.0494 0.0624 0.0571 0.0196 0.0496 0.0573 0.0545 0.0091 0.0174 0.0303 0.0238
SR 95% 0.0195 0.0465 0.0583 0.0540 95% 0.0175 0.0415 0.0528 0.0486 95% 0.0078 0.0145 0.0275 0.0216
CIESS 0.0230 0.0534 0.6570 0.0640 0.0222 0.0540 0.0662 0.0613 0.0157 0.0383 0.0483 0.0446
BET 0.0255 0.0596 0.0727 0.0676 0.0216 0.0505 0.0639 0.0588 0.0170 0.0404 0.0545 0.0491
𝑝-value 0.0403 0.0200 0.0305 0.0204 0.0327 0.0451 0.0064 0.0193 0.0399 0.0246 0.0094 0.0044
(b)ResultsonYelp
Table1:Performanceofallmethodson(a)Gowalla,and(b)Yelp2018withthesparsityratiosetto80%,90%,and95%.Thebest
resultsarehighlighted.Recall@𝑘andNDCG@𝑘aredenotedbyR@𝑘andN@𝑘forsimplicity.Each𝑝-valueiscalculatedviathe
paired𝑡-testbetweenBETandthebestbaseline.
Sparsity SelectionMethod Yelp2018 Gowalla recommendersandatnearlyallspecifiedsparsitylevels(80%,90%,
R@20 N@20 R@20 N@20
RandomSelection 0.0846 0.0788 0.1749 0.1473
and95%).Theassociated𝑝-valuesarebelow5%mostofthetime
80% Simplefitnessprediction 0.0835 0.0779 0.1739 0.1469 sowecanrejectthenullhypothesisthattheobservedperformance
DeepSetsfitnessprediction 0.0873 0.0816 0.1753 0.1483 changesoccurredbychanceinmostscenarios.
RandomSelection 0.0767 0.0717 0.1594 0.1357
Meanwhile,thesparsityratiosachievedbyESAPNandOptEm-
90% Simplefitnessprediction 0.0768 0.0717 0.1590 0.1355
DeepSetsfitnessprediction 0.0816 0.0762 0.1620 0.1376 bedrangefrom67%and83%,oftenfailingtomeettheminimum
RandomSelection 0.0637 0.0583 0.1335 0.1143 targetof80%.Despitekeepingarelativelyhighernumberofparam-
95% Simplefitnessprediction 0.0673 0.0629 0.1349 0.1152
eterscomparedtoothermethods,theirrecommendationperfor-
DeepSetsfitnessprediction 0.0727 0.0676 0.1374 0.1171
Table2:PerformanceofBETwhendifferentselectionmeth- manceisconsistentlyinferiortoBET.Forinstance,whenusedwith
odsareused. LightGCNontheGowalladataset,ESAPNrequiresmorememory
complexity (75% sparsity ratio) to achieve a comparable perfor-
4.4 OverallPerformanceComparison
mancecomparedtoBETunderan90%sparsitycondition.
Table1showstheRecall@𝑘andNDCG@𝑘scoresofvariouslight-
In summary, BET demonstrates superior performance while
weightembeddingmethodswhentheyarepairedwithdifferent
maintainingthesamememoryusage.Similarly,whencomparing
backbonerecommendermodels.Wealsoperformpairedstudent’s
performancelevels,BETprovestobemoreefficientinmemory
𝑡-testbetweenBETandthebestbaselinemethod.Comparedwith
utilization.Consequently,thesefindingshighlightthebenefitsof
thebaselineswithadjustablesparsityratios(i.e.,PEP,SU,SR,and
theongoingembeddingsizeexplorationinBET.
CIESS),BETachievesbetterperformanceacrossallthreebackbone
563

WSDM’24,March4–8,2024,Merida,Mexico YunkeQu,TongChen,QuocVietHungNguyen,&HongzhiYin
(a)Effectof𝑚onYelp (a)Effectof𝑇 onYelp
(b)Effectof𝑚onGowalla (b)Effectof𝑇 onGowalla
Figure 4: Sensitivity analysis of 𝑚 on Recall@20 and Figure 5: Sensitivity analysis of 𝑇 on Recall@20 and
NDCG@20withLightGCNasthebackbonerecommender. NDCG@20withLightGCNasthebackbonerecommender.
4.5 ModelComponentAnalysis
Selectingfromthesetofcandidateactionsineachiterationisavital
stepinBET,whereweproposedahybridselectionmethodthat
alternatelyusesthreeselectionstrategies.Tostudytheeffectiveness
oftheproposedselectionmethodandtheDeepSets-basedfitness
predictionnetwork,weconductaquantitativestudyonBETand
itstwovariants.Thefirstvariantusesrandomselectiononly.The
Figure 6: Sensitivity analysis of 𝑇 on the fitness predic-
secondvariantincorporatesasimplisticfitnesspredictionnetwork
tionlosswithLightGCNasthebackbonerecommenderon
thatonlyacceptstheembeddingsizesofeachuseranditem.Table
Yelp2018(left)andGowalla(right).
2illustratestheperformanceoftheoriginalversionofBETalong
withitstwovariantsintermsoftheirRecall@20andNDCG@20 population A𝑡 for each training iteration𝑡 ∈ [0,𝑇] and report
scores. Only the performance of the best-performing backbone thebestrecommendationperformanceintermsofRecall@20and
recommenderLightGCNisreportedduetospacelimit.Theresults NDCG@20.Wealsoreporttheaveragefitnesspredictionlossin
showthatBETwithaDeepSets-basedfitnesspredictionnetwork each iteration. Figure 6 shows that fitness predictor converges
hasbetterperformancethanthetwovariants,implyingthatour withinthefirst15iterations.Whilethetraininglossofthefitness
proposed selection method is effective and the DeepSets-based predictorisdiminishing,BETwitnessesasubstantialimprovement
architectureisabletolearnthelatentrepresentationofactions. initsperformanceinthefirst10-15iterations,asshowninFigure5.
Thenperformancecontinuestoclimbslowlyafterthe15thiteration
4.6 AnalysisofHyperparameter until it reaches its peak around the 40th iteration and remains
unchangedafterthat.Inconclusion,setting𝑇 =50shouldsuffice
Inthissection,weinspecttheinfluenceofthecorehyperparameters
forBETtofindtheoptimalactionforallsparsityratios.
inBETintermsofRecall@20andNDCG@20.LightGCNshows
thebestperformancesoitischosenasthebackbonerecommender
5 CONCLUSIONANDFUTUREWORKS
fordemonstration.
Latentfactorrecommenderstypicallyemployvectorizedembed-
4.6.1 NumberofSampledActions𝑚. Ineachiteration,wesam-
dingswithauniformandfixedsize,resultinginsuboptimalperfor-
ple𝑚candidateactionstochoosefrom.WetuneBETwith𝑚 ∈
manceandexcessivememorycomplexity.Toaddressthischallenge,
{20,40,60,80,100}forbothYelp2018andGowalla.Thenweshow
wehaveintroducedBET,amodel-agnosticalgorithmtoenablethe
howtheperformancechangeswithdifferentvaluesof𝑚w.r.t.Re-
selectionofcustomizedembeddingsizesatthe leveloftheem-
call@20andNDCG@20scores.AsshowninFigure4,although
beddingtableforeachuser/item.Thisapproachenhancesthethe
BETisrelativelyinsensitivetothevalueof𝑚,betterperformance
embeddingswhileminimizingmemorycosts.Next,wewilldevelop
isachievedwith𝑚=100onbothdatasets.
embeddingsizesearchalgorithmsforstreamingrecommendation.
4.6.2 NumberofIterations𝑇. BETiterativelysamples,selectsand
ACKNOWLEDGMENT
evaluatesactionsinsearchoftheoptimalone.Onenaturalquestion
thatarisesishowmanyiterationsitneedstofindtheactionthat ThisworkissupportedbytheAustralianResearchCouncilunder
leadstopeakrecommendationperformance.Thisquestioniscrucial the streams of Future Fellowship (No. FT210100624), Discovery
forunderstandingtheeffectivenessofBET.Therefore,weperform Project(No.DP190101985),andDiscoveryEarlyCareerResearch
selectiveretrainingasdescribedinSection3.5.2ontheresulting Award(No.DE200101465andNo.DE230101033).
564

BudgetedEmbeddingTableForRecommenderSystems WSDM’24,March4–8,2024,Merida,Mexico
REFERENCES
[25] PijiLi,ZihaoWang,ZhaochunRen,LidongBing,andWaiLam.2017. Neural
[1] AnshumaliShrivastavaAdityaDesai,LiChou.2022.RandomOffsetBlockEmbed- ratingregressionwithabstractivetipsgenerationforrecommendation.InProceed-
ding(ROBE)forcompressedembeddingtablesindeeplearningrecommendation ingsofthe40thInternationalACMSIGIRconferenceonResearchandDevelopment
systems.InProceedingsofMachineLearningandSystems.762–778. inInformationRetrieval.345–354.
[2] MathieuBlondel,AkinoriFujino,NaonoriUeda,andMasakazuIshihata.2016. [26] ShiweiLi,HuifengGuo,LuHou,WeiZhang,XingTang,RuimingTang,Rui
Higher-OrderFactorizationMachines.InProceedingsofthe30thInternational Zhang,andRuixuanLi.2023.AdaptiveLow-PrecisionTrainingforEmbeddings
ConferenceonNeuralInformationProcessingSystems.3359–3367. inClick-ThroughRatePrediction.ProceedingsoftheAAAIConferenceonArtificial
[3] HanCai,ChuangGan,TianzheWang,ZhekaiZhang,andSongHan.2020.Once- Intelligence37,4(2023),4435–4443.
for-all:Trainonenetworkandspecializeitforefficientdeployment.ICLR(2020). [27] SiyuanLiandElenaKarahanna.2015.OnlineRecommendationSystemsinaB2C
[4] ChengChen,XiangwuMeng,ZhenghuaXu,andThomasLukasiewicz.2017. E-CommerceContext:AReviewandFutureDirections.JournaloftheAssociation
Location-AwarePersonalizedNewsRecommendationWithDeepSemanticAnal- forInformationSystems16(2015),72–107.
ysis.IEEEAccess5(2017),1624–1638. [28] YangLi,TongChen,Peng-FeiZhang,andHongzhiYin.2021.Lightweightself-
[5] TingChen,LalaLi,andYizhouSun.2020.DifferentiableProductQuantization attentivesequentialrecommendation.InCIKM.967–977.
forEnd-to-EndEmbeddingCompression.InProceedingsofthe37thInternational [29] DawenLiang,LaurentCharlin,JamesMcInerney,andDavidM.Blei.2016.Mod-
ConferenceonMachineLearning.1617–1626. elingUserExposureinRecommendation.InWWW.951–961.
[6] TongChen,HongzhiYin,GuanhuaYe,ZiHuang,YangWang,andMengWang. [30] XurongLiang,TongChen,QuocVietHungNguyen,JianxinLi,andHongzhiYin.
2020.TryThisInstead:PersonalizedandInterpretableSubstituteRecommenda- 2023.LearningCompactCompositionalEmbeddingsviaRegularizedPruning
tion.InSIGIR.891–900. forRecommendation.InICDM.
[7] TongChen,HongzhiYin,XiangliangZhang,ZiHuang,YangWang,andMeng [31] GuanyuLin,ChenGao,YinfengLi,Y.Zheng,ZhihengLi,DepengJin,andYong
Wang.2021. QuaternionFactorizationMachines:ALightweightSolutionto Li.2022.DualContrastiveNetworkforSequentialRecommendationwithUser
IntricateFeatureInteractionModeling. IEEETransactionsonNeuralNetworks andItem-CentricPerspectives.ACMTransactionsonInformationSystems1,1
andLearningSystems34,8(2021),1–14. (2022).
[8] TongChen,HongzhiYin,YujiaZheng,ZiHuang,YangWang,andMengWang. [32] WeilinLin,XiangyuZhao,YejingWang,TongXu,andXianWu.2022.AdaFS:
2021.LearningElasticEmbeddingsforCustomizingOn-DeviceRecommenders. AdaptiveFeatureSelectioninDeepRecommenderSystem.InProceedingsof
InSIGKDD.138–147. the28thACMSIGKDDConferenceonKnowledgeDiscoveryandDataMining.
[9] YankaiChen,HuifengGuo,YingxueZhang,ChenMa,RuimingTang,JingjieLi, 3309–3317.
andIrwinKing.2022. LearningBinarizedGraphRepresentationswithMulti- [33] HanLiu,YinweiWei,JianhuaYin,andLiqiangNie.2023.HS-GCN:Hamming
FacetedQuantizationReinforcementforTop-KRecommendation.InSIGKDD. SpatialGraphConvolutionalNetworksforRecommendation.TKDE35,6(2023),
168–178. 5977–5990.
[10] YankaiChen,HuifengGuo,YingxueZhang,ChenMa,RuimingTang,Jingjie [34] HaochenLiu,XiangyuZhao,ChongWang,XiaobingLiu,andJiliangTang.2020.
Li,andIrwinKing.2022. LearningBinarizedGraphRepresentationswith Automatedembeddingsizesearchindeeprecommendersystems.InSIGIR.2307–
Multi-FacetedQuantizationReinforcementforTop-KRecommendation.InKDD. 2316.
168–178. [35] SiyiLiu,ChenGao,YihongChen,DepengJin,andYongLi.2021. Learnable
[11] AdityaDesaiandAnshumaliShrivastava.2022. Thetrade-offsofmodelsize EmbeddingsizesforRecommenderSystems.InICLR.
inlargerecommendationmodels:100GBto10MBCriteo-tbDLRMmodel.In [36] YuanfeiLuo,MengshuoWang,HaoZhou,QuanmingYao,Wei-WeiTu,Yuqiang
NeurIPS.33961–33972. Chen,WenyuanDai,andQiangYang.2019.Autocross:Automaticfeaturecrossing
[12] YuyunGongandQiZhang.2016.Hashtagrecommendationusingattention-based fortabulardatainreal-worldapplications.InSIGKDD.1936–1945.
convolutionalneuralnetwork..InIJCAI.2782–2788. [37] FuyuanLyu,XingTang,HongZhu,HuifengGuo,YingxueZhang,Ruiming
[13] HuifengGuo,RuimingTang,YunmingYe,ZhenguoLi,andXiuqiangHe.2017. Tang,andXueLiu.2022. OptEmbed:LearningOptimalEmbeddingTablefor
DeepFM:afactorization-machinebasedneuralnetworkforCTRprediction.IJCAI Click-throughRatePrediction.InCIKM.1399–1409.
(2017). [38] AndrewLMaas,AwniYHannun,AndrewYNg,etal.2013.Rectifiernonlineari-
[14] XiangnanHe,KuanDeng,XiangWang,YanLi,YongdongZhang,andMeng tiesimproveneuralnetworkacousticmodels.InICML.
Wang.2020.Lightgcn:Simplifyingandpoweringgraphconvolutionnetworkfor [39] KhalilMuhammad,QinqinWang,DiarmuidO’Reilly-Morgan,EliasTragos,Barry
recommendation.InSIGIR.639–648. Smyth,NeilHurley,JamesGeraci,andAonghusLawlor.2020. Fedfast:Going
[15] XiangnanHe,LiziLiao,HanwangZhang,LiqiangNie,XiaHu,andTat-Seng beyondaverageforfastertrainingoffederatedrecommendersystems.InSIGKDD.
Chua.2017.Neuralcollaborativefiltering.InWWW.173–182. 1234–1242.
[16] ZhenhuaHuang,XinXu,JuanNi,HonghaoZhu,andChengWang.2019.Multi- [40] LiangQu,YonghongYe,NingzhiTang,LixinZhang,YuhuiShi,andHongzhiYin.
modalrepresentationlearningforrecommendationinInternetofThings.IEEE 2022. Single-ShotEmbeddingDimensionSearchinRecommenderSystem.In
InternetofThingsJournal6,6(2019),10675–10685. SIGIR.513–522.
[17] GangweiJiang,HaoWang,JinChen,HaoyuWang,DefuLian,andEnhongChen. [41] YunkeQu,TongChen,XiangyuZhao,LizhenCui,KaiZheng,andHongzhiYin.
2021.XLightFM:ExtremelyMemory-EfficientFactorizationMachine.InSIGIR. 2023.ContinuousInputEmbeddingSizeSearchForRecommenderSystems.In
337–346. SIGIR.708–717.
[18] ManasRJoglekar,CongLi,MeiChen,TaibaiXu,XiaomingWang,JayKAdams, [42] SteffenRendle.2010.Factorizationmachines.In2010IEEEInternationalconference
PranavKhaitan,JiahuiLiu,andQuocVLe.2020.Neuralinputsearchforlarge ondatamining.995–1000.
scalerecommendationmodels.InSIGKDD.2387–2397. [43] SteffenRendle,ChristophFreudenthaler,ZenoGantner,andLarsSchmidt-Thieme.
[19] Wang-ChengKang,DerekZhiyuanCheng,TingChen,XinyangYi,DongLin, 2009.BPR:BayesianPersonalizedRankingfromImplicitFeedback.InProceedings
LichanHong,andEdH.Chi.2020.LearningMulti-GranularQuantizedEmbed- oftheTwenty-FifthConferenceonUncertaintyinArtificialIntelligence.452–461.
dingsforLarge-VocabCategoricalFeaturesinRecommenderSystems.InWWW. [44] NaserSedaghati,TeMu,Louis-NoelPouchet,SrinivasanParthasarathy,andP
562–566. Sadayappan.2015.AutomaticselectionofsparsematrixrepresentationonGPUs.
[20] NitishShirishKeskar,DheevatsaMudigere,JorgeNocedal,MikhailSmelyanskiy, InACMInternationalConferenceonSupercomputing.99–108.
andPingTakPeterTang.2016. OnLarge-BatchTrainingforDeepLearning: [45] SuvashSedhain,AdityaKrishnaMenon,ScottSanner,andLexingXie.2015.
GeneralizationGapandSharpMinima.InICLR. AutoRec:AutoencodersMeetCollaborativeFiltering.InWWW.111–112.
[21] YunyongKo,Jae-SeoYu,Hong-KyunBae,YongjunPark,DongwonLee,and [46] GeetSethi,BilgeAcun,NiketAgarwal,ChristosKozyrakis,CarolineTrippel,and
Sang-WookKim.2021.MASCOT:AQuantizationFrameworkforEfficientMatrix Carole-JeanWu.2022.RecShard:StatisticalFeature-BasedMemoryOptimization
FactorizationinRecommenderSystems.In2021IEEEInternationalConferenceon forIndustry-ScaleNeuralRecommendation.InProceedingsofthe27thACM
DataMining(ICDM).290–299. InternationalConferenceonArchitecturalSupportforProgrammingLanguagesand
[22] ShumingKong,WeiyuCheng,YanyanShen,andLinpengHuang.2023.AutoSrh: OperatingSystems.344–358.
AnEmbeddingDimensionalitySearchFrameworkforTabularDataPrediction. [47] Hao-JunMichaelShi,DheevatsaMudigere,MaximNaumov,andJiyanYang.2020.
TKDE35,7(2023),6673–6686. Compositionalembeddingsusingcomplementarypartitionsformemory-efficient
[23] SuMonKywe,Ee-PengLim,andFeidaZhu.2012. Asurveyofrecommender recommendationsystems.InSIGKDD.165–175.
systemsintwitter.InInternationalConferenceonSocialInformatics.420–433. [48] YangSun,FajieYuan,MinYang,GuoaoWei,ZhouZhao,andDuoLiu.2020.A
[24] JoonseokLee,SamiAbu-El-Haija,BalakrishnanVaradarajan,andApostolNatsev. GenericNetworkCompressionFrameworkforSequentialRecommenderSystems.
2018.Collaborativedeepmetriclearningforvideounderstanding.InProceedings InSIGIR’20.1299–1308.
ofthe24thACMSIGKDDInternationalconferenceonknowledgediscovery&data [49] PauliVirtanenetal.2020.SciPy1.0:fundamentalalgorithmsforscientificcom-
mining.481–490. putinginPython.NatureMethods17,3(2020),261–272.
[50] EdwardWagstaff,FabianBFuchs,MartinEngelcke,MichaelAOsborne,and
IngmarPosner.2022.Universalapproximationoffunctionsonsets.JMLR23,1
(2022),6762–6817.
565

WSDM’24,March4–8,2024,Merida,Mexico YunkeQu,TongChen,QuocVietHungNguyen,&HongzhiYin
[51] ShoujinWang,LongbingCao,YanWang,QuanZSheng,MehmetAOrgun, LearningforRecommendation.InSIGIR.1294–1303.
andDefuLian.2021.Asurveyonsession-basedrecommendersystems.ACM [59] ManzilZaheer,SatwikKottur,SiamakRavanbhakhsh,BarnabásPóczos,Ruslan
ComputingSurveys(CSUR)54,7(2021),1–38. Salakhutdinov,andAlexanderJSmola.2017.DeepSets.InNeurIPS.3394–3404.
[52] SuhangWang,YilinWang,JiliangTang,KaiShu,SuhasRanganath,andHuanLiu. [60] CaojinZhang,YicunLiu,YuanpuXie,SofiaIraKtena,AlykhanTejani,Akshay
2017.WhatYourImagesReveal:ExploitingVisualContentsforPoint-of-Interest Gupta,PranayKumarMyana,DeepakDilipkumar,SuvadipPaul,IkuhiroIhara,
Recommendation.InProceedingsofthe26thInternationalConferenceonWorld etal.2020. Modelsizereductionusingfrequencybaseddoublehashingfor
WideWeb.391–400. recommendersystems.InFourteenthACMConferenceonRecommenderSystems.
[53] XiangWang,XiangnanHe,MengWang,FuliFeng,andTat-SengChua.2019. 521–526.
Neuralgraphcollaborativefiltering.InSIGIR.165–174. [61] ShuaiZhang,LinaYao,AixinSun,andYiTay.2019.Deeplearningbasedrec-
[54] YejingWang,XiangyuZhao,TongXu,andXianWu.2022.Autofield:Automating ommendersystem:Asurveyandnewperspectives. ACMComputingSurveys
featureselectionindeeprecommendersystems.InWWW.1977–1986. (CSUR)52,1(2019),1–38.
[55] XinXia,HongzhiYin,JunliangYu,QinyongWang,GuandongXu,andQuoc [62] XiangyuZhao,HaochenLiu,WenqiFan,HuiLiu,JiliangTang,ChongWang,
VietHungNguyen.2022. On-DeviceNext-ItemRecommendationwithSelf- MingChen,XudongZheng,XiaobingLiu,andXiwangYang.2021. Autoemb:
SupervisedKnowledgeDistillation.InSIGIR.546–555. Automatedembeddingdimensionalitysearchinstreamingrecommendations.In
[56] XinXia,JunliangYu,QinyongWang,ChaoqunYang,NguyenQuocVietHung, 2021IEEEInternationalConferenceonDataMining(ICDM).896–905.
andHongzhiYin.2023. EfficientOn-DeviceSession-BasedRecommendation. [63] RuiqiZheng,LiangQu,BinCui,YuhuiShi,andHongzhiYin.2022. AutoML
ACMTransactionsInformationSystems41,4(2023). forDeepRecommenderSystems:ASurvey.ACMTransactionsonInformation
[57] BenchengYan,PengjieWang,JinquanLiu,WeiLin,Kuang-ChihLee,JianXu,and Systems101(2022),1–38.
BoZheng.2021.BinaryCodeBasedHashEmbeddingforWeb-ScaleApplications. [64] MeiziZhou,ZhuoyeDing,JiliangTang,andDaweiYin.2018.MicroBehaviors:
InCIKM.3563–3567. ANewPerspectiveinE-CommerceRecommenderSystems.InProceedingsofthe
[58] JunliangYu,HongzhiYin,XinXia,TongChen,LizhenCui,andQuocVietHung EleventhACMInternationalConferenceonWebSearchandDataMining.727–735.
Nguyen.2022.AreGraphAugmentationsNecessary?SimpleGraphContrastive
566