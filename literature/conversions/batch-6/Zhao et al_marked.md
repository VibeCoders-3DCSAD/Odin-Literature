---
conversion_metadata:
  converted_at: "2026-07-21T10:06:51Z"
  converter_tool: "markitdown"
  converter_version: "0.1.6"
  source_pdf: "Zhao et al.pdf"
  source_pdf_sha256: "b10c5a130d0f166eeab198b0a991cbc3ee3c911fad97e25b1b0b9fbbe106ab32"
  page_count: 15
  markdown_char_count: 191446
---

<!-- PAGE-AWARE EXTRACTION (via pdfminer.six) -->

<!-- PAGE 1 -->

OPEN ACCESS

EDITED BY
Emad Maher Natsheh,
An-Najah National University, Palestine

REVIEWED BY
Bashar Tahayna,
An-Najah National University, Palestine
Jehad M. Hamamreh,
An-Najah National University Libraries,
Palestine

*CORRESPONDENCE
Yumin Yao

yaoyumin@csu.edu.cn

RECEIVED 13 March 2026
REVISED 02 May 2026
ACCEPTED 04 May 2026
PUBLISHED 25 May 2026

CITATION
Zhao L, Zhao H, Li M, Wang J, Ke X and
Yao Y (2026) DynEC: dynamic
evolutionary clustering for power user
load proﬁling using multi-view graph
neural networks.
Front. Artif. Intell. 9:1829649.
doi: 10.3389/frai.2026.1829649

COPYRIGHT
© 2026 Zhao, Zhao, Li, Wang, Ke and
Yao. This is an open-access article
distributed under the terms of the
Creative Commons Attribution License
(CC BY). The use, distribution or
reproduction in other forums is
permitted, provided the original author(s)
and the copyright owner(s) are credited
and that the original publication in this
journal is cited, in accordance with
accepted academic practice. No use,
distribution or reproduction is permitted
which does not comply with these terms.

TYPE Original Research
PUBLISHED 25 May 2026
DOI 10.3389/frai.2026.1829649

DynEC: dynamic evolutionary
clustering for power user load
proﬁling using multi-view graph
neural networks

Lei Zhao1, Hong Zhao1, Mengjie Li1, Jia Wang1, Xingsi Ke1 and
Yumin Yao2*

1State Grid Sichuan Electric Power Corporation, Chengdu, China, 2School of Computer Science and
Engineering, Central South University, Changsha, China

Introduction: With the deep integration of generation-transmission-load-
storage systems, the power demand side has become highly dynamic and
stochastic, challenging the traditional assumption that user behavior remains
stationary over time. Static clustering models therefore suffer from sensitivity to
daily noise and false user identity switching.
Methods: This study proposes Dynamic Evolutionary Clustering (DynEC), a
multi-view graph neural network framework for power user load proﬁling. DynEC
constructs a sparse multi-view dynamic graph that captures geometric proximity,
temporal alignment through constrained dynamic time warping, and statistical
dependencies. A gated spatiotemporal graph neural network then optimizes
a dual-objective loss to learn latent representations while balancing current
snapshot quality and historical temporal smoothness.
Results: Experiments on real-world datasets show that DynEC outperforms
existing baseline methods. The proposed framework identiﬁes genuine concept
drift more accurately while reducing erroneous cluster switching.
Discussion: DynEC provides a stable and reliable proﬁling tool for modern
power grid management by modeling load proﬁling as a continuous evolutionary
process rather than a set of independent static clustering tasks.

KEYWORDS

concept drift, dynamic evolutionary clustering, graph neural networks, load proﬁling,
multi-view learning, source-grid-load-storage

1 Introduction

With the development of Advanced Metering Infrastructure (AMI) and artiﬁcial
intelligence (Balamurugan et al., 2025; Belge et al., 2024), load forecasting in power grids
has shifted from a passive interface to an active, bidirectional engagement point. This
structural shift toward a “generation-grid-load-storage” paradigm necessitates a transition
from macroscopic demand management to precise, user-centric proﬁling. At the core of
this transformation lies load proﬁling, as precise load proﬁles serve as the foundation for
dynamic pricing design, demand response (DR) targeting (Zou et al., 2024; Tolas et al.,
2024; Zhang et al., 2025), and grid ﬂexibility planning under carbon neutrality constraints
(Badhe et al., 2025; Verma and Rao, 2025).

With the proliferation of distributed energy resources and electric vehicles, users
are increasingly becoming grid prosumers who both consume and generate electricity.

Frontiers in Artiﬁcial Intelligence

01

frontiersin.org

---

<!-- PAGE 2 -->

Zhao et al.

10.3389/frai.2026.1829649

by

pricing,

real-time

inﬂuenced

extreme
Consequently,
weather events, and evolving work-from-home practices, daily
consumption patterns have become highly stochastic. These factors
continuously reshape the load curve, triggering concept drift
(Gama et al., 2014; Lu et al., 2018). The traditional assumption that
user behavior remains strictly stationary over time is no longer
suitable for this pattern.

Current methods treat load proﬁling as a static snapshot
problem, aggregating data from several months to assign users a
single, permanent label. While useful for high-level infrastructure
planning, static clustering fails severely in grids with a high
proportion of renewable energy. When users fundamentally alter
their routines (e.g., by purchasing an electric vehicle), static models
exhibit delayed adaptation, leading to persistent misclassiﬁcation.
Conversely, if operators repeatedly apply static clustering to daily
or weekly data blocks, the model overreacts to normal daily
noise. Users may jump erratically between clusters without any
actual underlying behavioral change. This false “identity switching”
undermines the temporal smoothness required for reliable demand
response (DR) targeting. Dynamic evolutionary clustering oﬀers
a solution by modeling proﬁles not as isolated snapshots, but as
continuous videos that explicitly track how behavior evolves, while
penalizing unstable cluster hopping.

later,

It is well known that Euclidean metrics are highly vulnerable
to temporal phase shifts (Kim et al., 2025). Two users may
if one wakes up
have identical consumption patterns, but
an hour
the Euclidean distance will place them in
completely diﬀerent clusters. Dynamic Time Warping (DTW)
(Berndt and Cliﬀord, 1994; Keogh and Ratanamahatana, 2005)
addresses this alignment issue but suﬀers from poor scalability
on large-scale datasets. Meanwhile, while spatiotemporal graph
neural networks (ST-GNNs) have achieved some success in load
forecasting, they lack the speciﬁc loss functions required to balance
structural feature learning with temporal clustering consistency in
unsupervised settings.

In summary, to bridge the gap between structural graph
learning and dynamic pattern evolution, this study proposes
DynEC (Dynamic Evolutionary Clustering). Our approach makes
it constructs a multi-view
three main contributions: First,
dynamic graph to address the temporal evolution of user proﬁles.
By integrating geometric proximity,
temporal alignment (via
computationally eﬃcient cDTW), and statistical dependencies
(Pearson correlation) into a uniﬁed graph structure, it reliably
captures user relationships even under severe phase shifts. Second,
we design a self-supervised deep evolutionary graph learning
framework that combines a gated spatio-temporal graph encoder
with a dual-objective evolutionary optimization strategy. By
adopting a network-optimized dual loss function that balances
snapshot quality and temporal smoothness, the model adapts to
genuine concept drift while suppressing false identity switching.
Third, we evaluate the framework using real-world smart meter
it
data from three diﬀerent cities. The results conﬁrm that

Abbreviations: DynEC, Dynamic Evolutionary Clustering; GNN, Graph Neural
Network; GST-GNN, Gated Spatio-Temporal Graph Neural Network; cDTW,
Constrained Dynamic Time Warping; CSR, Cluster Switching Rate; ARI,
Adjusted Rand Index; V2G, Vehicle-to-Grid; DR, Demand Response.

TABLE 1 Comparison between static and dynamic clustering paradigms.

Dimension

Static clustering

Dynamic
clustering

Metaphor

Static photo

Continuous video

Temporal

perspective

Ignores time or ﬂattens it

Explicitly models evolution

(snapshot)

Feature

Global/static statistics

Time-varying embeddings

representation

Primary goal

Discover long-term

Capture pattern evolution

stable patterns

and drift

Drift sensitivity

Cannot detect concept

Adaptable to and detects

drift

drift

Computational

Low (one-time)

High (online/recursive)

cost

Application

Long-term planning

Real-time DR, anomaly

detection

achieves excellent internal clustering quality, as measured by
the silhouette coeﬃcient and ARI, while signiﬁcantly reducing
the cluster switching rate (CSR). By eﬀectively tracking genuine
behavioral shifts while ignoring daily noise, DynEC provides a
highly stable and actionable proﬁling engine for next-generation
smart grids.

The remainder of this article is structured as follows: Section
2 reviews the relevant literature. Section 3 provides a detailed
description of the DynEC methodology and complexity analysis.
Section 4 presents the experimental setup and results. Section 5
concludes the article.

2 Related work

2.1 Dynamic community detection and
evolutionary clustering

The eﬀective organization of dynamic data streams is a
focal point of academic research. This ﬁeld is typically divided
into two main areas: dynamic community detection in social
networks and evolutionary clustering in data mining. In particular,
(Chakrabarti et al., 2006) proposed a formalized “evolutionary
clustering” framework, noting that the optimal clustering solution
at time t requires balancing two competing objectives: maximizing
the current data ﬁt (Snapshot Quality) while minimizing the
deviation from previous clustering results (Temporal Cost).
However, in traditional methods, the trade-oﬀ parameters are
typically user-deﬁned. To overcome this limitation, deep graph
learning can automatically learn adaptive, dynamically evolving
parameters.

Building on the perspectives proposed by Wang et al. (2019)
and Tariq et al. (2022), this study adapts static clustering models
for dynamic environments; Table 1 summarizes the conceptual
diﬀerences between the static and dynamic paradigms.

Frontiers in Artiﬁcial Intelligence

02

frontiersin.org

---

<!-- PAGE 3 -->

Zhao et al.

10.3389/frai.2026.1829649

In the context of smart grids, user behavior often undergoes
concept drift, causing the statistical properties of target variables to
change over time (Gama et al., 2014; Jiang et al., 2021). Traditional
static methods, such as applying K-Means to daily snapshots,
typically overreact to noise. This can trigger “cluster hopping,”
where users oscillate between clusters without any actual change
in behavior (Jain et al., 2021). Conversely, incremental learning
methods that update only cluster centroids suﬀer from “lag,”
failing to adapt quickly to sudden shifts. Therefore, the framework
proposed in this study adopts explicit modeling of nodes,
incorporates temporal evolution, and updates cluster centroids,
enabling the model to adapt to dynamic changes in clustering.

Recent advances in graph-stream mining have introduced
methods that maintain temporal summaries of graph structures.
For example, Time2Graph (Cheng et al., 2020) treats temporal
evolution as a sequence of shapelets, but it still relies on static
K-Means in the ﬁnal clustering step. DynEC enhances existing
methods by directly integrating temporal consistency into deep
learning objectives.

2.2 Deep learning in load proﬁling

Current deep learning technologies signiﬁcantly advance
smart grid management by enabling robust load proﬁle clustering
and predictive pattern recognition. For instance, Long et al.
(2025) combined density-based clustering (DBSCAN) with a
graph attention network to predict air conditioning loads across
geographic grids. This approach demonstrates the value of
grouping spatially correlated units. In the context of data security,
Zhang et al. (2025) proposed a CK-Means clustering scheme based
on adaptive diﬀerential privacy for smart meter data analysis. This
ensures both privacy protection and computational eﬃciency.
Furthermore, Muyulema-Masaquiza and Ayala-Chauvin (2025)
showed that eﬀective consumption segmentation directly supports
dynamic pricing, anomaly detection, and demand forecasting.

2.2.1 Static deep clustering

Early

studies

typically

employed dimension reduction
techniques, such as principal component analysis (PCA) and hand-
engineered features, followed by K-Means clustering (Chicco et al.,
2006). Later, deep clustering methods based on autoencoders
enabled the concurrent optimization of feature learning and cluster
assignment. However, these methods are inherently static. They
treat data as a collection of independent and identically distributed
(i.i.d.) samples, ignoring the sequential dependencies inherent in
load proﬁles. While eﬀective for static snapshots, they fail to capture
the temporal sequence in dynamic grid data. Therefore, adaptive
modeling is crucial; Wang et al. (2020) speciﬁcally adopted deep
reinforcement learning for demand response management.

2.2.2 Spatio-temporal graph neural networks

To eﬀectively capture complex spatial structures and temporal
dependencies, advanced power grid analysis techniques typically

(ST-GNNs).
employ spatio-temporal graph neural networks
Typical model architectures, such as Graph WaveNet (Wu et al.,
2019) and DCRNN (Li et al., 2018), integrate graph convolutional
networks (GCNs) with spatiotemporal convolutional or recurrent
neural networks (RNNs). This integration simultaneously models
spatial dependencies (power grid topology) and temporal dynamics
(load trends). EvolveGCN (Pareja et al., 2020) uses RNNs to
evolve the parameters of the GCN itself to adapt to changes
in global distributions. However, for load proﬁling, preserving
individual user identities is crucial. Therefore, TGN (Rossi et al.,
2020) captures continuous temporal dynamics through a memory
module to extract
individual user proﬁling features. DySAT
(Sankar et al., 2020) constructs adaptive dynamic proﬁles by
introducing a self-attention mechanism to jointly model structural
and temporal evolution. Furthermore, deep graph clustering has
emerged as a highly promising direction. Works such as SDCN
(Bo et al., 2020) have successfully integrated structural information
into clustering tasks. Concurrently, contrastive learning methods
(e.g., temporal subgraph contrastive learning Wang et al., 2023)
have demonstrated potential in dynamic graph representations.
This study focuses on evolving node embeddings via GRU memory
modules to ensure the model retains stable historical context for
each speciﬁc user, thereby preventing identity loss during temporal
updates.

Despite signiﬁcant progress in the aforementioned areas, most
spatiotemporal graph neural network (ST-GNN) research has
primarily focused on supervised learning tasks, such as load
estimation (Fekri et al., 2021) or fault detection. Consequently,
the exploration of unsupervised clustering remains very limited.
Foundational work, such as DGI (Veliˇckovi´c et al., 2019) and
MVGRL (Hassani and Khasahmadi, 2020), has demonstrated the
feasibility of unsupervised graph representation learning. However,
applying these principles to power grid user proﬁling with
dynamically evolving features remains challenging.

2.3 Similarity measures: geometric,
shape-based, and statistical

In user proﬁling tasks based on Graph Neural Networks
(GNNs), constructing meaningful user graphs is critical to model
performance. Although the commonly used Euclidean distance
oﬀers an ideal computational complexity of O(D), it is highly
sensitive to temporal phase shifts when processing time-series data
like load curves. Even minor phase shifts can incorrectly separate
inherently similar curves, a behavior demonstrated in experimental
analyses by Kim et al. (2025).

To address this issue, we incorporate Dynamic Time Warping
(DTW). As emphasized by Berndt and Cliﬀord (1994), DTW
eﬀectively compensates for local deviations along the time axis
by ﬁnding an optimal non-linear alignment. However, standard
DTW has a time complexity of O(D2), making it computationally
expensive for large-scale applications. For load curves with
prominent periodicity, Constrained Dynamic Time Warping
(cDTW) oﬀers a more eﬃcient alternative. The pioneering work
of Sakoe and Chiba (1978) demonstrates that introducing Sakoe–
Chiba bands to apply local constraints on the alignment path

Frontiers in Artiﬁcial Intelligence

03

frontiersin.org

---

<!-- PAGE 4 -->

Zhao et al.

10.3389/frai.2026.1829649

maintains accuracy while controlling time complexity within a
polynomial range of the number of data points D and the signal-
to-noise ratio w. A more systematic review can be found in
Ratanamahatana and Keogh (2004).

Building on this, recent studies have also explored mapping
DTW similarity into Euclidean space via Shapelets to explicitly
enforce alignment constraints during synthesis (El Amouri et al.,
2023). However, the automatic Shapelet discovery process often
requires intensive computation, causing practical diﬃculties in
large-scale situations.

geometric

To combine the strengths of various similarity measures,
(2019) proposed integrating multiple metrics. This
Lin et al.
strategy
(e.g., Euclidean
incorporates
distance), shape similarity (cDTW), and statistical dependence
(speciﬁcally,
our
work)
thereby enabling the
construction of more robust graph structures in the presence
of noise.

correlation
into a multidimensional graph,

the Pearson

coeﬃcient

similarity

in

2.4 Clustering validation and stability
analysis

Traditional clustering validity metrics, such as the Rousseeuw
(Rousseeuw, 1987) or the Davies–Bouldin index,
coeﬃcient
primarily focus on snapshot quality, verifying the compactness and
separation of clusters. They ignore temporal instability and impose
no penalty when users jump erratically between clusters.

As noted by Jain et al. (2021), in industrial applications, stability
is just as important as accuracy. A clustering algorithm that
produces drastically diﬀerent partitions when the input data is
slightly perturbed is operationally useless. In dynamic settings,
this translates directly to temporal stability: unless the underlying
data distribution actually shifts, the cluster assignments should
not change signiﬁcantly between time steps (Lange et al., 2004;
Luxburg, 2007). We use the cluster switching rate (CSR) and
temporal smoothness (TS) metrics to formalize this requirement.
This dual-metric system provides a holistic evaluation framework
that balances internal cluster quality with operational robustness.

3 Methodology

3.1 Problem deﬁnition

This

their

energy

study formalizes

the dynamic user

segmentation
problem under concept drift as a dynamic graph clustering
task. Rather than treating electricity consumers as isolated
entities with static labels, we model the continuous evolution
through complex
of
consumption behaviors
spatio-temporal
consumers
representing
interactions.
as nodes and their multi-view similarities as
time-varying
edges,
tracking genuine behavioral shifts is
mathematically transformed into an evolutionary representation
learning and clustering optimization problem over a sequence of
dynamic graphs.

the challenge of

By

3.1.1 Prerequisites

Deﬁnition 1 (Dynamic load proﬁle stream (DLPS)). Let U =
{u1, u2, . . . , uN } be the set of electricity users, where N is the total
number of users. At each time step t ∈ {1, 2, . . . , T}, we observe a
load matrix X(t). Let x(t)
∈ RD denote the electricity consumption
i
proﬁle of user ui over a time interval of length D. The continuous
load proﬁle stream is thus deﬁned as Equation 1:

X = {X(1), X(2), . . . , X(T)}

(1)

Deﬁnition 2 (Concept drift). A data stream is considered to exhibit
concept drift when its underlying joint probability distribution
changes over time, as shown in Equation 2:

P(X(t)) (cid:3)= P(X(t+1))

(2)

In the context of power grids, such drift typically arises from
individual behavioral shifts, such as installing new appliances or
developing new electric vehicle charging patterns, or from system-
level macro changes, such as seasonal eﬀects or pricing adjustments.

Deﬁnition 3 (Dynamic graph ﬂow). We model the evolving
relationships among users as a sequence of dynamic graphs, as
shown in Equation 3:

G = {G(1), G(2), . . . , G(T)}

(3)

Here, the node set V = U remains ﬁxed, while the time-varying
adjacency matrix A(t) captures the instantaneous similarities
between users at time t.

3.1.2 Problem description

Given a sequence of dynamic graphs G, our objective is to learn
a mapping function fθ at each time step t, as shown in Equation 4:

fθ : G(t) → C(t)

(4)

where C(t) = {C1, . . . , CK } denotes the cluster partition of the N
users into K distinct groups. This partition must simultaneously
optimize two competing objectives:
Snapshot quality: Users within the same cluster Ck should exhibit
high intra-cluster similarity in terms of geometric characteristics
(e.g., load magnitude and shape), temporal synchronization, and
statistical dependencies.

Temporal consistency: The clustering structure should evolve
smoothly over time. Speciﬁcally, the current partition C(t) should
not deviate drastically from the previous partition C(t−1) unless
genuine concept drift occurs, thereby minimizing erroneous user
identity switching.

3.2 Framework architecture

As illustrated in Figure 1, the proposed Dynamic Evolutionary
Clustering framework consists of two core modules that operate
sequentially at each time step.

Frontiers in Artiﬁcial Intelligence

04

frontiersin.org

---

<!-- PAGE 5 -->

Zhao et al.

10.3389/frai.2026.1829649

First, the Multi-view dynamic graph construction module
(Section 3.3) takes the raw multi-dimensional load proﬁles as input
and constructs a comprehensive user relationship graph. Rather
than relying on a single similarity metric, it models inter-user
relationships from three complementary perspectives: geometric
proximity (Euclidean distance), temporal alignment (Constrained
Dynamic Time Warping, cDTW), and statistical dependency
(Pearson correlation). This multi-view fusion mechanism is
speciﬁcally designed to capture complex non-linear correlations
and robustly align user behaviors even in the presence of severe
temporal phase shifts.

Second,

the Deep evolutionary graph learning module
(Section 3.4) performs evolutionary representation learning and
clustering assignment. It integrates a Gated Spatio-Temporal Graph
Encoder (comprising a Multi-Head Graph Attention Network
and a Gated Recurrent Unit) to extract evolution-aware node
embeddings. These embeddings are then optimized through a
Dual-Objective Optimization mechanism that explicitly balances
the snapshot clustering quality (via KL divergence) with temporal
smoothness. By jointly optimizing these two objectives,
the
architecture eﬀectively solves the stability-plasticity dilemma,
enabling the reliable tracking of genuine concept drift while
aggressively suppressing erroneous identity switching caused by
daily noise.

3.3 Multi-view dynamic graph construction

This section elucidates the rationale behind the multi-view
framework, detailing the speciﬁc relationships characterized by
each view and the mechanism for fusing them into a uniﬁed
graph structure. We construct the user similarity structure from
three complementary perspectives—geometric proximity, temporal
alignment, and statistical dependency—to facilitate robust graph
representation learning.

3.3.1 Motivation: toward a comprehensive user
relationship graph

the objective is

At each time step t,

to construct a
dynamic graph G(t) = (V, E(t)) that authentically reﬂects the
multifaceted relationships among users. A single metric, such as
Euclidean distance, is often insuﬃcient as it primarily captures
similarity in numerical magnitude at synchronized sampling points.
Consequently, it fails to account for: load proﬁles that exhibit
to temporal
similar morphological patterns but are subject
phase shifts, as well as users who display signiﬁcant disparities
in magnitude or phase but still share underlying statistical
dependencies. To address these limitations, we adopt a multi-
view modeling approach, synthesizing three distinct adjacency
structures to derive a uniﬁed adjacency matrix A(t).

3.3.2 Geometric view (Ageo): characterizing
magnitude-based proximity

The geometric view captures the local proximity of user load
proﬁles within the Euclidean space at a given time grid. For any

pair of users (i, j), the Euclidean distance at time t is deﬁned as
Equation 5:

dgeo(i, j) = (cid:5)x(t)
i

− x(t)
j

(cid:5)2.

(5)

Based on this metric, a k-Nearest Neighbors (kNN) graph is
constructed: Ageo(i, j) = 1 if user j is among the k-nearest neighbors
of user i, and 0 otherwise. This view connects users exhibiting highly
synchronized consumption variations predominantly on the same
temporal scale, thereby reﬂecting local geometric similarities.

3.3.3 Temporal alignment view (Adtw):
characterizing shape similarity under temporal
shifts

A critical limitation of the geometric view is its sensitivity to
temporal phase shifts. For instance, two users with morphologically
similar load curves may be deemed dissimilar by Euclidean distance
due to a time lag (e.g., cooking activities occurring at diﬀerent
times). To mitigate this, the temporal alignment view incorporates
Constrained Dynamic Time Warping (cDTW). cDTW minimizes
the cumulative distance between matched points by identifying an
optimal warping path W = {w1, . . . , wK } between two sequences xi
and xj as shown in Equation 6:

cDTW(xi, xj) = min
W

K(cid:2)

k=1

wk,

(6)

subject to the constraint |ik
| < w, where wk denotes the
− jk
distance of the k-th matched pair and w is the Sakoe–Chiba
window width. Given the inherent periodicity of daily load proﬁles,
imposing a narrow window w reduces the time complexity to
O(D·w), ensuring approximately linear scalability while preserving
alignment precision.

Upon computing the cDTW distance, a Gaussian kernel is
employed to transform the distance into a similarity measure as
shown in Equation 7:

Sdtw(i, j) = exp(−d2(i, j)/σ 2).

(7)

The resulting similarity matrix is subsequently thresholded to
yield a sparse adjacency matrix Adtw. This view eﬀectively links
users whose load proﬁles are morphologically similar but temporally
shifted, serving as a crucial complement to the geometric view.

3.3.4 Correlation view (Acorr): characterizing
statistical dependency

Two load proﬁles may diﬀer signiﬁcantly in magnitude or phase
yet still exhibit strong co-movement patterns. The dependency
view, therefore, uses the absolute Pearson correlation coeﬃcient
to quantify statistical dependency between users while remaining
computationally eﬃcient for high-dimensional continuous load
proﬁles. For two load proﬁles xi and xj, the correlation score is
deﬁned as Equation 8:

ρ(i, j) =

(cid:3)
(cid:3)
(cid:3)
(cid:3)
(cid:3)

(cid:6)

(xi − ¯xi)
(xj − ¯xj)
(cid:5)xi − ¯xi(cid:5)2 (cid:5)xj − ¯xj(cid:5)2

(cid:3)
(cid:3)
(cid:3)
(cid:3)
(cid:3) .

(8)

Frontiers in Artiﬁcial Intelligence

05

frontiersin.org

---

<!-- PAGE 6 -->

Zhao et al.

10.3389/frai.2026.1829649

FIGURE 1
Overview of the architecture of DynEC. (A) Multi-view dynamic graph construction: fusing geometric, temporal, and statistical dependencies. (B)
Gated spatio-temporal graph encoder: updating node embeddings via Multi-Head GAT and GRU. (C) Dual-objective clustering: optimizing for both
cluster purity (KL divergence to target) and temporal consistency.

This metric facilitates

the identiﬁcation of users with
statistically similar behavior even in the presence of substantial
discrepancies in the raw time domain. The corresponding adjacency
matrix Acorr
therefore captures linear statistical dependency,
enriching the graph with information complementary to geometric
proximity and temporal alignment.

Require: Load profiles X(t), Neighbors k, Window w,

Kernel σ , Weights α, β, γ .

Ensure: Fused Adjacency Matrix A(t).

1: Geometric View Construction:

2: Compute pairwise Euclidean distances Dgeo;
3: Construct kNN graph A(t)

geo based on Dgeo with k

neighbors;

3.3.5 Graph fusion: integration of heterogeneous
views

4: Temporal Alignment View Construction:

5: Compute pairwise cDTW distances Ddtw with window w

The three views generate distinct adjacency matrices A(t)
geo,
dtw, and A(t)
A(t)
corr. To enable the Graph Neural Network to learn
from these heterogeneous sources, we employ a “weighted fusion
and normalization” strategy to synthesize a uniﬁed adjacency
matrix A(t).

First, the views are integrated via a weighted linear combination

as shown in Equation 9:

A(t)

fused

= αA(t)
geo

+ βA(t)
dtw

+ γ A(t)

corr,

(9)

where α, β, γ are hyperparameters satisfying α + β + γ =
1, regulating the relative contributions of geometric proximity,
temporal alignment, and statistical dependency.

Subsequently, symmetric normalization is applied to the fused
fused as shown in Equation 10:

adjacency matrix A(t)

A(t) = D

− 1

2 (A(t)

fused

+ I)D

− 1
2 ,

(10)

where I is the identity matrix representing self-loops, and D is
the degree matrix of A(t)
+ I. This normalization is essential
for mitigating the bias introduced by uneven degree distributions
during graph convolution.

fused

The resulting uniﬁed adjacency matrix A(t) simultaneously
encodes local Euclidean proximity (Geometric View), shape
similarity invariant
to temporal shifts (Temporal Alignment
View), and linear statistical dependency (Correlation View). This
multi-view dynamic graph provides a comprehensive and robust
structural foundation for subsequent spatio-temporal learning in
the GST-GNN.

The detailed procedure for multi-view dynamic graph

construction is summarized in Algorithm 1.

(Equation 5);

6: Convert to similarity Sdtw = exp(−D2
7: Sparsify Sdtw to obtain A(t)
dtw;
8: Dependency View Construction:

dtw

/σ 2);

9: Compute

Pearson-correlation

matrix

(Equation 6);

A(t)
corr

10: Fusion and Normalization:
+ γ A(t)
11: A(t)
2 (A(t)
12: Normalize A(t) ← D
13: return

+ βA(t)
dtw
− 1

← αA(t)
geo

A(t)

fused

fused

corr;

+ I)D

− 1

2 ;

Algorithm 1. Multi-view dynamic graph construction.

3.4 Deep evolutionary graph learning
framework

The core of DynEC is a uniﬁed self-supervised learning
framework that seamlessly integrates a Gated Spatio-Temporal
Graph Encoder with a Dual-Objective Optimization Mechanism.

3.4.1 Gated spatio-temporal graph encoder

The Gated Spatio-Temporal Graph Neural Network (GST-
GNN)
is designed to learn node embeddings that capture
both the structural patterns from the multi-view graph A(t)
and the temporal evolution of user behaviors from the feature
stream X(t). Unlike traditional ST-GNNs, which primarily focus
on supervised forecasting tasks (Wu et al., 2019), our encoder
is speciﬁcally tailored for unsupervised evolutionary clustering,

Frontiers in Artiﬁcial Intelligence

06

frontiersin.org

---

<!-- PAGE 7 -->

Zhao et al.

10.3389/frai.2026.1829649

learning with dynamic
eﬀectively connecting static structural
pattern evolution. The “Gated” nature of this architecture is
twofold: it employs an attention-based soft gating mechanism for
spatial aggregation and a gated recurrent unit for temporal updates.

3.4.1.1 Spatial aggregation (multi-head GAT)

To capture the manifold relationship patterns present in the
multi-view graph, a Multi-Head Graph Attention Network (GAT)
is employed. Let h(t)
i denote the feature vector of node i at time t
(where initially h(t)
= x(t)
i ). For each attention head k, the attention
i
coeﬃcient eij,k between node i and its neighbor j ∈ Ni (deﬁned by
A(t)) is calculated as follows Equation 11:

eij,k

= LeakyReLU((cid:8)aT

k [Wkh(t)

i

(cid:5)Wkh(t)

j ])

(11)

where Wk denotes the learnable weight matrix, (cid:8)ak is the attention
vector for the k-th head, and (cid:5) represents the concatenation
operation. The attention weights, denoted by α
ij,k, are obtained
through softmax normalization as shown in Equation 12:

α

ij,k

=

(cid:4)

exp(eij,k)
l∈Ni exp(eil,k)

(12)

These weights function as a “soft gating” mechanism, ﬁltering
out noisy connections by assigning lower importance to irrelevant
neighbors. The ﬁnal spatial embedding h(t)
is obtained by
concatenating the outputs of the K heads as shown in Equation 13:
⎛

i,spat

⎞

h(t)
i,spat

=

K(cid:5)
(cid:5)
(cid:5)

(cid:2)

⎝

σ

k=1

j∈Ni

ij,kWkh(t)
α
j

⎠

(13)

where σ is a non-linear activation function (e.g., ELU).

3.4.1.2 Temporal evolution (GRU update)

To capture user proﬁle dynamics and handle concept drift,
a Gated Recurrent Unit (GRU) is utilized to update the node
embeddings. The GRU eﬃciently tracks temporal embeddings,
providing a robust mechanism to update user representations
under concept drift. The GRU processes the current spatial feature
i,spat (output from GAT) and the previous user embedding z(t−1)
h(t)
as input to yield the ﬁnal temporal embedding z(t)
. The reset gate
i
within the GRU determines the extent to which past information
should be disregarded, a process essential for adapting to concept
drift. Meanwhile, the update gate controls the incorporation of new
spatial information. This mechanism enables the model to retain
a long-term memory of user identity while adapting to short-term
ﬂuctuations.

i

3.4.2 Dual-objective evolutionary optimization

The fundamental principle of our framework is unsupervised
clustering. We employ a self-training methodology utilizing a
Student’s t-distribution kernel.

the cluster centroid μ
k. In this study, we propose using the
Student’s t-distribution kernel instead of the conventional Gaussian
kernel used in Gaussian Mixture Models. This choice is motivated
by the heavy-tailed property of the t-distribution, which makes
the clustering more robust to outliers. This is a critical feature
when dealing with volatile electricity load data, where spikes and
anomalies are common. The soft assignment is computed as follows
Equation 14:

qik

= (1 + (cid:5)zi − μ
k
k(cid:9) (1 + (cid:5)zi − μ

(cid:4)

(cid:5)2/ν)
k(cid:9) (cid:5)2/ν)

− ν+1
2
− ν+1
2

(14)

where ν represents the degrees of freedom, which is set to 1
in this instance, reducing the equation to a Cauchy distribution.
This formulation enables a more ﬂexible cluster boundary,
accommodating the inherent noise in smart meter data without
excessively penalizing distant points.

3.4.2.2 Self-training target distribution

To overcome the lack of ground truth labels in unsupervised
settings, we employ a self-training strategy. The target distribution,
deﬁned herein as P, is used to “sharpen” the soft assignments, Q, to
encourage high-conﬁdence predictions. The target probability p is
derived from q by raising it to the second power and normalizing
by cluster frequency as shown in Equation 15:

=

pik

/fk(cid:4)
q2
ik
k(cid:9) q2

ik(cid:9) /fk(cid:9)

(cid:4)

(15)

=

where fk
i qik is the soft cluster frequency. The target
(1)
distribution is designed to satisfy three key properties:
Sharpening: By squaring the probabilities, the distribution is
pushed toward a one-hot encoding, reducing entropy and forcing
the model to make decisive cluster assignments. (2) Conﬁdence
Emphasis: Data points that initially demonstrate high conﬁdence
contribute more to the gradient, guiding the learning process.
(3) Normalization: Division by fk prevents large clusters from
dominating the loss function, ensuring that smaller but distinct user
groups (e.g., EV owners) are not ignored.

3.4.2.3 Dual-objective loss function

The learning objective is divided into two competing
components: clustering quality loss and temporal smoothness loss
as shown in Equation 16.

L = L

+ λLtemp

clus

(16)

1. Snapshot clustering loss (Lclus): This term minimizes the
Kullback-Leibler (KL) divergence between the soft assignment Q(t)
and the target distribution P(t) at the current time step as shown in
Equation 17.

L

clus

= KL(P(t)(cid:5)Q(t)) =

(cid:2)

(cid:2)

i

k

p(t)
ik log

p(t)
ik
q(t)
ik

(17)

3.4.2.1 Soft assignment (student’s t-distribution)

The probability of user i belonging to cluster k, denoted
qik, is measured by the similarity between its embedding zi and

By minimizing this divergence, the model is forced to iteratively
reﬁne its cluster assignments, moving the centroids toward the
high-density centers of the embeddings.

Frontiers in Artiﬁcial Intelligence

07

frontiersin.org

---

<!-- PAGE 8 -->

Zhao et al.

10.3389/frai.2026.1829649

2. Temporal consistency loss (Ltemp): To prevent erratic
“Identity Switching,” we introduce a temporal
smoothness
constraint. This term penalizes abrupt deviations of the current
cluster assignment Q(t) from the previous assignment Q(t−1) as
shown in Equation 18.

Require: Continuous

X =
{X(1), . . . , X(T)}, Number of clusters K, Hyperparameters
λ, α, β, γ .

profile

stream

load

Ensure: Cluster assignments C = {C(1), . . . , C(T)} for all

users.

Ltemp = KL(Q(t−1)(cid:5)Q(t)) =

(cid:2)

(cid:2)

i

k

q(t−1)
ik

log

q(t−1)
ik
q(t)
ik

1: Initialization: Pre-train the GST-GNN encoder using

(18)

reconstruction loss; Initialize cluster centroids
μ(0) via K-Means on the initial embeddings Z(0).

This regularization encourages the model to preserve a user’s
cluster membership unless strong evidence from new data dictates
a change. The hyperparameter λ controls the trade-oﬀ between
ﬁtting the current snapshot (Plasticity) and respecting historical
consistency (Stability).

3.4.3 Overall training process

To provide a clear roadmap of the proposed methodology,
the complete execution pipeline of the evolutionary clustering
framework is summarized in Algorithm 2. The procedure operates
in an online manner across continuous time steps. It begins with
a pre-training phase to establish robust initial representations
and cluster centroids. Subsequently, at each time step t, the
framework sequentially performs multi-view graph construction,
spatio-temporal embedding updates via the GST-GNN, and dual-
objective optimization. This iterative process ensures that the
model dynamically adapts to emerging concept drifts while
preserving the structural continuity of user proﬁles.

4 Experiments

4.1 Experimental setup

4.1.1 Datasets

To evaluate the performance of DynEC, we utilized three
real-world smart meter datasets collected from distinct cities in
Sichuan Province, China, covering the entire year of 2024. City
A (Mixed Residential/Commercial) comprises 800 users, including
a signiﬁcant proportion of early adopters of Distributed Energy
Resources (DERs) and Electric Vehicles (EVs). This dataset exhibits
high volatility and frequent pattern shifts. City B (Residential-
Dominant) consists of 500 users who display regular weekly
patterns, although these patterns are subject to signiﬁcant seasonal
ﬂuctuations. City C (Industrial Park Zone) contains 650 users
from a specialized industrial environment, serving as a proxy for
a fully integrated Source-Grid-Load-Storage system characterized
by diverse interaction patterns and distinct concept drifts.

3:

2: for t = 1 to T do
Multi-View
adjacency matrices A(t)
geo, A(t)
Fuse and normalize into a unified graph A(t)

Construction:
dtw, A(t)

Compute

Graph

corr.

4:

5:

6:

7:

8:

9:

10:

11:

12:

13:

(Equation 7).

Spatio-Temporal Embedding Update:
Extract spatial features: H(t) ← GAT(A(t), X(t)).

Update temporal states: Z(t) ← GRU(H(t), Z(t−1)).

Clustering & Dual-Objective Optimization:

Compute

soft

assignments

Q(t)

using

Eq. Equation 11.

Calculate the auxiliary target distribution
P(t) using Eq. Equation 12.
Calculate clustering loss Lclus and temporal
consistency loss Ltemp.
network
Update
centroids μ by minimizing L = Lclus + λLtemp.
Cluster Assignment: Assign each user i to
cluster c(t)
← arg maxk q(t)
ik .

parameters

cluster

and

θ

i

14: end for
15: return C.

Algorithm 2. Evolutionary clustering training process.

interpolation. To scale each user’s daily proﬁle to the interval [0, 1],
we applied min-max normalization. This ensures that the clustering
process focuses on shape patterns rather than absolute magnitudes.

4.1.1.2 Baseline information

To assess DynEC, we employed a comprehensive suite of
baselines, comprising both static and dynamic methods. Evol-
KMeans denotes our implementation of the evolutionary K-Means
approach proposed by Chakrabarti et al. (2006), instantiated via
centroid smoothing across consecutive monthly snapshots. The
speciﬁc descriptions of these baselines are shown in Table 2.

4.2 Implementation details

4.1.1.1 Pre-processing

4.2.1 Fusion weight strategy

The raw AMI data were sampled at 15-min intervals and
subsequently aggregated into hourly load proﬁles (D = 24). To
simulate a realistic dynamic environment, we employed a sliding
window approach with a sequence length of 24 h and a step size of
1 h. Missing values (approximately 0.5%) were imputed using linear

While the conceptual

framework allows for dynamically
updated fusion weights, our practical engineering implementation
utilizes ﬁxed, equal weights (α = β = γ = 1/3). This
choice prevents “view collapse” during training and ensures robust

Frontiers in Artiﬁcial Intelligence

08

frontiersin.org

---

<!-- PAGE 9 -->

Zhao et al.

10.3389/frai.2026.1829649

TABLE 2 Summary of baseline methods.

TABLE 3 Detailed implementation speciﬁcations and hyperparameter conﬁguration.

Category

Method

Description

Parameter

Value/speciﬁcation

Static baselines

K-Means

Standard baseline for load proﬁling;

Model architecture

acts as a reference for snapshot

quality but suﬀers from high

instability.

Spectral

Clusters via Laplacian

Clustering

eigendecomposition (Luxburg,

2007); it is computationally

expensive and lacks temporal

consistency.

Implementation framework

PyTorch geometric (PyG)

Graph encoder

2-layer Gated-GAT (Hidden dimensions:
64 → 32)

Temporal module

GRU (Hidden dimension: 32)

Attention mechanism

Multi-head Attention (K = 4 heads)

Clustering kernel

Student’s t-distribution (Degrees of freedom
ν = 1)

Dynamic/evolutionary

Time2Graph

Shapelet-based temporal

Hyperparameters

baselines

representation model adapted for

Temporal consistency (λ)

0.1 (Selected via grid search)

clustering using K-Means, following

the dynamic shapelet framework of

Cheng et al. (2020).

EvolveGCN-

Adaptation of EvolveGCN

Clus

(Pareja et al., 2020) evolving GCN

parameters via RNN, modiﬁed for

unsupervised clustering.

Fusion weights (α, β, γ )

Fixed at 1/3 (Equal Weighting)

cDTW bandwidth

2 (equivalent to ±2 hours temporal shift)

Optimization

Adam optimizer (learning rate η = 10−3, Weight
decay 10−4)

Training & hardware

Pre-training strategy

50 epochs (MSE reconstruction loss)

Evol-

Evolutionary K-Means baseline with

Clustering strategy

100 epochs (KL divergence loss)

KMeans

explicit centroid smoothing between

Batch size

256 users

consecutive monthly snapshots;

designed to reduce switching but

prone to under-adaptation when

heterogeneous drift occurs.

Computing resources

NVIDIA RTX 3090 GPU (24GB VRAM), 64GB

RAM

performance across diﬀerent datasets. Sensitivity to this design
choice is analyzed in Section 4.6.

The DynEC framework was

implemented in PyTorch

Geometric. The speciﬁc parameter settings are listed in Table 3.

4.2.1.1 Hyperparameters

The temporal consistency weight λ was set to 0.1, determined
through a grid search on the validation set. For the graph fusion
weights, ﬁxed equal values of 1/3 were used for α, β, and γ
throughout training. For the cDTW calculation, the Sakoe–Chiba
bandwidth was set to 2, allowing for a temporal shift of up to 2 h.
−3 and a
We utilized the Adam optimizer with a learning rate of 10
weight decay of 10

−4.

4.2.1.2 Training strategy

The GST-GNN encoder was pre-trained for 50 epochs using
Mean Squared Error (MSE) reconstruction loss to initialize the
node embeddings. Subsequent clustering training was conducted
in mini-batches of 256 users at each time step for 100 epochs. All
experiments were performed on a server equipped with an NVIDIA
RTX 3090 GPU and 64GB of RAM.

4.3 Evaluation metrics

To evaluate the trade-oﬀ between clustering quality and

temporal stability, we adopted a dual-metric evaluation system.

4.3.1 Snapshot quality metrics

These metrics evaluate the degree to which the clustering
structure corresponds to the data at a given time t. The Silhouette
Coeﬃcient (SC), developed by Rousseeuw (1987),
is used to
measure the contrast between intra-cluster cohesion and inter-
cluster separation. Additionally, the Davies-Bouldin Index (DBI)
is employed to evaluate the average similarity of each cluster with
its most similar neighbor. When groundtruth labels are available,
the Adjusted Rand Index (ARI) is also reported to quantify
the agreement between predicted partitions and the reference
clustering. In this study, ARI was computed against the pre-
deﬁned base_cluster labels in users.csv. These reference
labels were maintained in the utility’s operational system and
were cross-checked against customer-type records (e.g., residential
and commercial categories). To improve label reliability, domain
experts from the State Grid Sichuan Electric Power Corporation
randomly sampled 10% of users and veriﬁed the authenticity of
their assigned user types against ﬁeld-visit records before model
development. The de-identiﬁed dataset and reference labels are
publicly available in a GitHub repository.

4.3.2 Temporal stability metrics

In addition to static quality, assessing the temporal consistency
of cluster assignments is crucial for dynamic proﬁling. The Cluster
Switching Rate (CSR) is used to measure the stability of user
allocation over time. CSR is deﬁned as the average proportion of

Frontiers in Artiﬁcial Intelligence

09

frontiersin.org

---

<!-- PAGE 10 -->

Zhao et al.

10.3389/frai.2026.1829649

users who change their cluster aﬃliation between consecutive time
steps as shown in Equation 19:

CSR = 1

T − 1

T−1(cid:2)

t=1

(cid:10)

(cid:4)

N
i=1 1

c(t)
i

(cid:3)= c(t+1)
i

(cid:11)

N

(19)

where 1(·) is the indicator function, and c(t)
represents the cluster
i
label of user i at time t. A lower CSR indicates higher temporal
stability, meaning the model is robust to minor ﬂuctuations and
can capture consistent behavioral patterns.

4.4 Comparative analysis

As shown in Table 4, this study presents a comprehensive
performance comparison with ﬁve baseline models across three
the framework proposed in
cities. The results indicate that
this study achieves certain improvements in balancing clustering
quality and temporal stability.

4.4.1 Clustering quality (ARI & SC)

spectral

clustering

approaches,

identifying genuine behavioral

In City A (mixed type), which exhibits the highest volatility,
the ARI (0.56 ± 0.06) of our DynEC method outperforms
all other
(ARI
including
0.51 ± 0.01) and the explicit time-regularized baseline Evol-
KMeans (ARI 0.43 ± 0.00). This indicates that DynEC is
highly capable of
semantics
amid complex mixed patterns. However, static methods like
K-Means show stronger intra-cluster geometric compactness
(SC and DBI) on individual snapshots. This is an expected
trade-oﬀ, as our evolutionary learning framework sacriﬁces
minor instantaneous spatial cohesion to achieve a signiﬁcantly
lower Cluster Switching Rate (CSR), ensuring temporal semantic
consistency. In City B (residential), stability-oriented baseline
models
(such as Evol-KMeans) achieved exceptionally high
snapshot quality (ARI 0.92 ± 0.00, SC 0.65 ± 0.00), indicating
that residential patterns form distinct and geometrically well-
separated clusters on individual days. Although DynEC’s ARI
(0.85 ± 0.06) is slightly lower,
it remains highly competitive
while maintaining a consistent evolutionary representation.
In City C (industrial), DynEC remains competitive compared
(ARI 0.65 ± 0.06 vs. 0.65 ± 0.00) and
to Evol-KMeans
outperforms the state-of-the-art EvolveGCN (ARI 0.65 ± 0.06
vs. 0.62 ± 0.07), conﬁrming its robustness across diﬀerent
consumer types.

4.4.1.1 Temporal stability (CSR)

The proposed method achieves CSR values close to zero
(0.02–0.04) across all cities, signiﬁcantly lower than those of
static baseline methods (K-Means/Spectral: approximately 0.70–
approximately
0.79)
and dynamic methods
reduces CSR
0.29–0.61). However, Evol-KMeans
its
to 0.00–0.01 through explicit centroid smoothing; yet,
weaker ARI on the heterogeneous City A dataset
indicates
that temporal smoothing alone is insuﬃcient to model mixed

(EvolveGCN:
further

↓
R
S
C

↓

I

B
D

↑
C
S

↑

I

R
A

↓
R
S
C

↓

I

B
D

↑
C
S

↑

I

R
A

↓
R
S
C

↓

I

B
D

↑
C
S

↑

I

R
A

)
l
a
i
r
t
s
u
d
n
i
(

C
y
t
i

C

)
l
a
i
t
n
e
d
i
s
e
r
(

B
y
t
i

C

)
d
e
x
m

i

(

A
y
t
i

C

d
o
h
t
e
M

.
s
t
e
s
a
t
a
d
e
e
r
h
t
n
o
n
o
s
i
r
a
p
m
o
c
e
c
n
a
m
r
o
f
r
e
P

4
E
L
B
A
T

.

9
0
0
±
8
7
0

.

.

0
0
0
±
9
7
0

.

.

0
0
0
±
5
4
0

.

.

0
0
0
±
6
5
0

.

.

0
1
0
±
0
7
0

.

.

5
0
0
±
9
7
0

.

.

6
0
0
±
1
1
1

.

.

2
0
0
±
7
2
0

.

.

1
0
0
±
7
4
0

.

.

4
0
0
±
4
8
0

.

.

4
0
0
±
6
5
0

.

.

4
0
0
±
6
9
0

.

.

1
0
0
±
0
4
0

.

.

7
0
0
±
2
6
0

.

.

0
1
0
±
9
2
0

.

.

3
0
0
±
8
7
0

.

.

0
3
0
±
7
3
3

.

.

0
0
0
±
8
1
0

.

.

1
0
0
±
3
2
0

.

.

5
0
0
±
0
7
0

.

.

0
0
0
±
1
0
0

.

.

0
0
0
±
4
8
0

.

.

0
0
0
±
6
4
0

.

.

0
0
0
±
5
6
0

.

.

0
0
0
±
0
0
0

.

.

1
0
0
±
3
0
0

.

.

7
0
0
±
6
9
0

.

.

2
0
0
±
8
3
0

.

6
0
.
0
±
5
6
.
0

.

2
0
0
±
2
0
0

.

.

0
0
0
±
6
5
0

.

.

0
0
0
±
9
5
0

.

.

0
0
0
±
1
9
0

.

.

4
0
0
±
0
8
0

.

.

0
0
0
±
4
9
0

.

.

0
0
0
±
1
4
0

.

.

0
0
0
±
6
4
0

.

.

9
0
0
±
6
2
1

.

.

4
0
0
±
9
1
0

.

.

4
0
0
±
1
5
0

.

.

6
0
0
±
9
7
0

.

.

3
0
0
±
9
0
1

.

.

1
0
0
±
3
3
0

.

.

1
0
0
±
1
5
0

.

.

1
0
0
±
9
5
0

.

.

1
0
0
±
8
5
0

.

.

2
0
0
±
0
9
0

.

.

4
0
0
±
1
6
0

.

.

7
0
0
±
1
0
1

.

.

2
0
0
±
9
3
0

.

.

3
0
0
±
4
4
0

.

.

1
1
0
±
4
7
1

.

.

1
0
0
±
4
3
0

.

.

3
0
0
±
8
4
0

.

.

3
0
0
±
7
7
0

.

.

1
4
0
±
4
5
3

.

.

1
0
0
±
7
1
0

.

.

1
0
0
±
8
1
0

.

.

0
0
0
±
9
4
0

.

.

0
0
0
±
5
6
0

.

.

0
0
0
±
2
9
0

.

.

0
0
0
±
1
0
0

.

.

0
0
0
±
3
9
0

.

.

0
0
0
±
2
4
0

.

.

0
0
0
±
3
4
0

.

l

s
u
C
-
N
C
G
e
v
l
o
v
E

h
p
a
r
G
2
e
m
T

i

s
n
a
e

M
K
-
l
o
v
E

s
n
a
e

M
-
K

l
a
r
t
c
e
p
S

.

9
0
0
±
2
6
0

.

.

5
0
0
±
4
5
0

.

.

6
0
0
±
5
8
0

.

2
0
.
0
±
4
0
.
0

.

7
0
0
±
0
1
1

.

.

1
0
0
±
1
3
0

.

6
0
.
0
±
6
5
.
0

)
s
r
u
O

(
C
E
n
y
D

.

d
n
a
8
0
2
0
0
=
p
(
A
y
t
i

C
n

i

s
n
a
e

M
K
-
l
o
v
E
d
n
a

s
n
a
e

M
-
K
r
e
v
o
I
R
A
s
e
v
o
r
p
m

i

y
l
t
n
a
c
ﬁ
i
n
g
i
s
d
o
h
t
e
m
d
e
s
o
p
o
r
p
e
h
t

t
a
h
t

w
o
h
s

s
d
e
e
s

e
v
ﬁ
e
h
t

r
e
v
o
s
t
s
e
t
-
t
d
e
r
i
a
P

.

l

d
o
b
n

i
d
e
t
h
g
i
l
h
g
i
h
e
r
a

s
t
l
u
s
e
r

t
s
e
B

.
s
n
u
r

t
n
e
d
n
e
p
e
d
n

i
5
r
e
v
o
n
o
i
t
a
i
v
e
D
d
r
a
d
n
a
t
S
±
n
a
e

M

s
a
d
e
t
r
o
p
e
r

e
r
a

s
e
u
l
a
V

.

.
)
5
0
0
>
p
(

t
n
a
c
ﬁ
i
n
g
i
s
y
l
l
a
c
i
t
s
i
t
a
t
s

t
o
n
e
r
a
C
y
t
i

C
d
n
a
B
y
t
i

C
n

i

s
e
n

i
l
e
s
a
b
d
e
t
n
e
i
r
o
-
t
o
h
s
p
a
n
s

t
s
e
g
n
o
r
t
s

e
h
t

t
s
n
i
a
g
a

s
e
c
n
e
r
e
ﬀ
i
d
I
R
A
e
h
T

.
)

3
−

0
1
<
p
(

s
e
i
t
i
c

e
e
r
h
t

l
l
a
n

i

s
n
a
e

M
-
K
o
t

e
v
i
t
a
l
e
r
R
S
C
s
e
c
u
d
e
r
y
l
t
n
a
c
ﬁ
i
n
g
i
s
d
n
a

)
7
0
1
0
0
=
p

.

Frontiers in Artiﬁcial Intelligence

10

frontiersin.org

---

<!-- PAGE 11 -->

Zhao et al.

10.3389/frai.2026.1829649

their high CSR indicates

user drift. Although static methods such as K-Means may
achieve high snapshot quality in stable environments (City
B),
frequent “identity switching,”
where users are reassigned to diﬀerent clusters daily due to
framework
minor ﬂuctuations. Our
learning
transitions while maintaining
eﬀectively
semantic
real-world
utility applications.

smooths
consistency, which

evolutionary

crucial

these

for

is

4.4.1.2 Statistical signiﬁcance

Paired t-tests over the ﬁve random seeds conﬁrm that DynEC’s
ARI improvement in City A is statistically signiﬁcant relative to K-
Means (p = 0.0208) and Evol-KMeans (p = 0.0107). For temporal
stability, DynEC achieves signiﬁcantly lower CSR than K-Means in
−3). By contrast, the ARI
City A, City B, and City C (all p < 10
diﬀerences between DynEC and the strongest snapshot-oriented
baselines in City B and City C are not statistically signiﬁcant
(p > 0.05), which is consistent with the limitation discussed in
Section 4.8.

4.5 Ablation study

To rigorously verify the contribution of

the two core
innovations of
the proposed framework, a component-wise
ablation study was conducted on the City A dataset. The results
explicitly support the architectural design choices.

4.5.1 Validation of multi-view dynamic graph
construction

Regarding the removal of the time-aligned view (cDTW)
(i.e., “w/o DTW View”), this operation resulted in the most
signiﬁcant decline in clustering quality, with ARI dropping
sharply from 0.62 to 0.35. Therefore, geometric proximity alone
is insuﬃcient to characterize complex load patterns; the cDTW
view is crucial for capturing shape similarity and identifying
consistent user behavior in the presence of temporal misalignment.
Similarly, removing the correlation view (Pearson) resulted in

reduced stability (CSR increased from 0.02 to 0.05) and a slight
decrease in ARI, conﬁrming that statistical co-movement provides
supplementary information and enhances the robustness of the
clustering process.

4.5.2 Validation of deep evolutionary graph
learning framework

Setting the time-consistency weight

to λ = 0 (“no
time consistency”) resulted in a signiﬁcant deterioration of the
ARI (from 0.62 to 0.50), although the CSR remained at a
low level. This indicates that without time regularization, the
model cannot maintain a consistent semantic interpretation
over time, even when cluster assignments do not ﬂuctuate
rapidly. Furthermore, removing the gating mechanism (“no
gating”) resulted in a comprehensive decline in performance (ARI
dropped to 0.51, CSR rose to 0.07), validating its role as a
learnable ﬁlter that selectively aggregates information-rich spatial
neighbors while suppressing noise, thereby balancing plasticity
and stability.

4.6 Parameter sensitivity analysis

As shown in Figure 2, the adjusted Rand index (ARI) and
cluster switching rate (CSR) are plotted as λ varies from 0 to
1. In Mechanism I (λ <0.1), the model lacks suﬃcient time
constraints, resulting in poor cluster quality. Mechanism II (0.1 ≤
λ ≤ 0.3) represents the “optimal point,” where ARI peaks (at
λ = 0.2) while CSR decreases, indicating that appropriate temporal
regularization eﬀectively ﬁlters out noise and improves alignment
with the true values. In Mechanism III (λ >0.5), although CSR
decreases further (high stability), ARI ﬂuctuates, suggesting that
excessive regularization may hinder the model’s ability to adapt to
true conceptual drift, thereby leading to “lag.” In addition to λ, the
model demonstrates robustness to the number of neighbors k in
graph construction and the window size w in cDTW, as long as they
capture suﬃcient local context (e.g., k ∈ [5, 15]). Figure 3 further
shows that ﬁxed equal fusion weights (α = β = γ = 1/3) provide

FIGURE 2
Sensitivity analysis of temporal consistency weight λ on City A. An
optimal balance is observed around λ = 0.2, where cluster quality
(high ARI) is maximized while maintaining temporal stability (low
CSR).

FIGURE 3
Sensitivity analysis of fusion weights. The equal-weight conﬁguration
(α = β = γ = 1/3) achieves the best trade-off, maximizing ARI while
keeping CSR near zero.

Frontiers in Artiﬁcial Intelligence

11

frontiersin.org

---

<!-- PAGE 12 -->

Zhao et al.

10.3389/frai.2026.1829649

FIGURE 4
Illustration of robustness to phase shifts. Traditional Euclidean distance fails to match shape-similar but time-shifted load proﬁles, while the proposed
cDTW view correctly aligns these proﬁles, ensuring they are clustered together despite the temporal misalignment. (A) Euclidean distance: mismatch.
(B) cDTW: robust alignment.

4.7.2 Stability under concept drift

Figure 5 visualizes the evolution of User #42 from City A.
This case exempliﬁes a typical scenario in the context of Source-
Grid-Load-Storage: a residential user transforming into an active
prosumer by participating in a Vehicle-to-Grid (V2G) program
on Day 15. This structural change, characterized by the transition
from passive consumption to bi-directional power ﬂow, represents
a distinct incremental concept drift.

As observed, the static K-Means algorithm, treating each day
as an independent snapshot, reacted chaotically to the initial load
ﬂuctuations induced by V2G discharging events. On Days 14–
16, the user’s label ﬂickered violently between Cluster 1 (Standard
Residential) and Cluster 3 (V2G Prosumers). This phenomenon
illustrates the “Identity Switching” problem induced by the
stochasticity of source-load interactions, where static methods
fail to distinguish between transient ﬂuctuations and genuine
behavioral evolution. Such instability would trigger erroneous
billing adjustments in a real-world utility system.

In sharp contrast, DynEC maintained a coherent trajectory.
Facilitated by the temporal consistency loss and the GRU memory
mechanism, the model eﬀectively suppressed immediate responses
to transient noise. It reassigned the user to the V2G Prosumer
cluster only after the new interaction pattern persisted and
stabilized (post Day 16). This “smooth transition” capability
conﬁrms that our framework successfully balances plasticity
(adapting to the new V2G mode) with stability (ignoring temporary
volatility), validating its suitability for automated and noise-
tolerant load proﬁling.

4.8 Discussion and limitations

While our method demonstrates exceptional performance in
dynamic environments, we observe a slight performance trade-
oﬀ in extremely stable settings. Speciﬁcally, in City B, where the
load patterns are highly consistent, static K-Means marginally
outperforms DynEC in terms of ARI on a single snapshot. This
occurs because static models can greedily ﬁt the cross-sectional
temporal smoothing.
data without
This represents an inherent limitation of evolutionary clustering
algorithms, where maintaining low CSR introduces a slight

the “historical burden" of

FIGURE 5
Visualization of concept drift for User #42. Top: Daily load proﬁles
showing the emergence of V2G interaction patterns. Bottom:
Cluster assignment probabilities over time. DynEC exhibits a smooth
transition compared to the erratic switching of K-Means.

the best balance between snapshot quality and temporal stability,
supporting the engineering choice adopted in Section 4.2.

4.7 Case study: visualizing model
effectiveness

To intuitively demonstrate the superiority of the proposed
framework, qualitative visualizations corresponding to its two core
innovations are provided.

4.7.1 Robustness to phase shifts

The Multi-View Dynamic Graph Construction is designed to
handle temporal misalignments. In the analysis of the mixed-
type dataset, we identiﬁed numerous instances of “shape-similar
but
time-shifted” users (e.g., households with evening peaks
occurring at 18:00 vs. 20:00). Methods based on traditional
Euclidean distance (e.g., K-Means) often assign these users to
disparate clusters due to large point-wise distances. However,
by incorporating the cDTW view, the model successfully groups
these users into the same functional cluster, conﬁrming that the
multi-view fusion strategy eﬀectively captures inherent behavioral
similarity beyond simple geometric alignment. As shown in
Figure 4, cDTW correctly aligns shape-similar but time-shifted load
proﬁles, whereas Euclidean distance treats them as mismatched due
to point-wise temporal oﬀsets.

Frontiers in Artiﬁcial Intelligence

12

frontiersin.org

---

<!-- PAGE 13 -->

Zhao et al.

10.3389/frai.2026.1829649

FIGURE 6
Event-driven concept drift validation based on the real City-A event log. Top: number of veriﬁed monthly events in the evaluated 500-user subset.
Middle and bottom: mean ARI and CSR over ﬁve seeds. Month 5 contains the highest event concentration (32 users), where our approach retains
higher clustering quality while adapting more selectively than static K-Means and less conservatively than Evolutionary K-Means.

regularization penalty on snapshot-speciﬁc ﬁt in purely static
scenarios.

4.8.1 Event-driven concept drift validation

To verify that the exceptionally low CSR achieved by DynEC is
not merely the result of mathematical over-smoothing, we analyze
its behavior around real-world events. Using the veriﬁed City-A
event log for the same 500-user evaluation subset, we aggregate
recorded EV, PV, and SHOCK events into monthly snapshots
and compare them with the mean ARI/CSR trajectories over
ﬁve seeds. As shown in Figure 6, Month 5 contains the highest
concentration of veriﬁed events (32 aﬀected users). Around this
peak-drift snapshot, the proposed model preserves a clearly higher
ARI than Evolutionary K-Means while allowing a moderate CSR
increase, whereas Evolutionary K-Means keeps CSR near zero
by over-smoothing, and its ARI drops steadily after the event
accumulation period.

5 Conclusion

In this article, we presented the DynEC framework to
address the challenges in Source-Grid-Load-Storage integration
environments. By modeling load proﬁling as a continuous
evolutionary process rather than a set of static labels, it eﬀectively

mitigates the identity-switching behavior caused by bi-directional
source-load interactions. Our analysis indicates that traditional
static methods fail to capture the evolutionary characteristics of
energy consumption and exhibit operational instability. To solve
these problems, we utilized a Multi-View Dynamic Graph Neural
Network as the underlying architecture.

The core technical contributions of our framework are
summarized as follows: First, it integrates geometric, temporal
(cDTW), and statistical dependencies to capture complex non-
Euclidean correlations, thereby comprehensively addressing the
limitations of single-metric similarity in dynamic environments. In
addition, it introduces a uniﬁed paradigm that combines a Gated
Spatio-Temporal Graph Encoder with Dual-Objective Evolutionary
Optimization. This mechanism allows the model to learn evolution-
aware representations while explicitly balancing the trade-oﬀ
between snapshot clustering quality and temporal smoothness.

Extensive

experiments on three

real-world datasets—
comprising mixed residential/commercial, residential-dominant,
and industrial park zones—conﬁrm that DynEC signiﬁcantly
reduces the Cluster Switching Rate (CSR) compared to static
baselines, while maintaining state-of-the-art clustering quality
(Silhouette Coeﬃcient). By shifting from state-based analysis
to process-based evolution tracking,
the proposed approach
establishes a robust foundation for dynamic pricing and targeted
demand response. Ultimately, DynEC strikes a critical balance
between stability and adaptability, paving the way for the next
generation of reliable and automated smart grid management.

Frontiers in Artiﬁcial Intelligence

13

frontiersin.org

---

<!-- PAGE 14 -->

Zhao et al.

10.3389/frai.2026.1829649

Data availability statement

Conﬂict of interest

The Data availability statement is accurate. The datasets and

code are available at: https://github.com/jerryao/DynEC.

The author(s) declared that this work was conducted in the
absence of any commercial or ﬁnancial relationships that could be
construed as a potential conﬂict of interest.

Author contributions

LZ: Writing – original draft. HZ: Supervision, Writing –
review & editing. ML: Investigation, Writing – review & editing.
JW: Methodology, Validation, Writing – review & editing. XK:
Funding acquisition, Resources, Writing – review & editing. YY:
Conceptualization, Writing – review & editing.

Funding

The author(s) declared that ﬁnancial support was received
for this work and/or its publication. This research was funded
by the State Grid Sichuan Electric Power Corporation, grant
number 521999240001 (Research on Key Technologies for Fine
Management and Precise Control of Load Resources for Power
Supply Guarantee Demand-Side Management). The APC was
funded by the State Grid Sichuan Electric Power Corporation.

Acknowledgments

We thank the reviewers for their constructive feedback.

Generative AI statement

The author(s) declared that generative AI was not used in the

creation of this manuscript.

Any alternative text (alt

text) provided alongside ﬁgures
in this article has been generated by Frontiers with the
intelligence and reasonable eﬀorts have
support of artiﬁcial
been made to ensure accuracy,
including review by the
authors wherever possible. If you identify any issues, please
contact us.

Publisher’s note

All claims expressed in this article are solely those of the
authors and do not necessarily represent those of their aﬃliated
organizations, or those of the publisher, the editors and the
reviewers. Any product that may be evaluated in this article, or
claim that may be made by its manufacturer, is not guaranteed or
endorsed by the publisher.

References
Badhe, N. B., Neve, R. P., Yele, V. P., Abhang, S., Dhule, K. M., and Mali, D.
(2025). An optimized system for predicting energy usage in smart grids using
temporal fusion transformer and Aquila optimizer. Front. Artif. Intell. 8:1542320.
doi: 10.3389/frai.2025.1542320

Balamurugan, M., Narayanan, K., Raghu, N., Arjun Kumar, G. B., and Trupti, V. N.
(2025). Role of artiﬁcial intelligence in smart grid–a mini review. Front. Artif. Intell.
8:1551661. doi: 10.3389/frai.2025.1551661

Belge, A. T., Gupta, S., Alegavi, S., Singh, V., and Shukla, K. (2024). Advancements,
challenges, and future prospects of smart grid technology in India. Front. Artif. Intell.
7:1475604. doi: 10.3389/frai.2024.1475604

Berndt, D. J., and Cliﬀord, J. (1994). “Using dynamic time warping to ﬁnd patterns in
time series,” in Proceedings of the 3rd International Conference on Knowledge Discovery
and Data Mining (KDD-94), 359–370.

Bo, D., Wang, X., Cui, C., Wang, H., and Shi, C. (2020). “Structural deep
clustering network,” in Proceedings of
the Web Conference 2020, 1400–1410.
doi: 10.1145/3366423.3380214

Chakrabarti, D., Kumar, R., and Tomkins, A. (2006). “Evolutionary clustering,”
in Proceedings of the 12th ACM SIGKDD International Conference on Knowledge
Discovery and Data Mining, KDD ’06 (ACM), 554–560. doi: 10.1145/1150402.
1150467

Cheng, Z., Yang, Y., Wang, W., Hu, W., Zhuang, Y., and Song, G. (2020). “Time2graph:
revisiting time series modeling with dynamic shapelets,” in Proceedings of the AAAI
Conference on Artiﬁcial Intelligence, 3617–3624. doi: 10.1609/aaai.v34i04.5769

El Amouri, H., Lampert, T., Gançarski, P., and Mallet, C. (2023). Constrained
dtw preserving shapelets for explainable time-series clustering. Pattern Recognit.
143:109804. doi: 10.1016/j.patcog.2023.109804

Fekri, M. N., Patel, H., Grolinger, K., and Sharma, V. (2021). Deep learning for load
forecasting with smart meter data: online adaptive recurrent neural network. Appl.
Energy 282:116177. doi: 10.1016/j.apenergy.2020.116177

Gama, J., Žliobait˙e, I., Bifet, A., Pechenizkiy, M., and Bouchachia, A. (2014). A
survey on concept drift adaptation. ACM Comput. Surv. 46, 1–37. doi: 10.1145/25
23813

Hassani, K., and Khasahmadi, A. H. (2020). “Contrastive multi-view representation
learning on graphs,” in International Conference on Machine Learning (PMLR),
4116–4126.

Jain, M., AlSkaif, T., and Dev, S.
for electric load demand proﬁles.
doi: 10.1109/TII.2021.3061470

(2021). Validating clustering frameworks
Inform. 17, 8057–8065.

IEEE Trans.

Ind.

Jiang, Z., Lin, R., and Yang, F. (2021). An incremental clustering algorithm
with pattern drift detection for iot-enabled smart grid system. Sensors 21:6466.
doi: 10.3390/s21196466

Keogh, E., and Ratanamahatana, C. A. (2005). Exact indexing of dynamic time warping.
Knowl. Inf. Syst. 7, 358–386. doi: 10.1007/s10115-004-0154-9

Kim, M., Firoozjaei, M. D., Kim, H., and El-Hajj, M. (2025). Power proﬁling
of
14:2015.
doi: 10.3390/electronics14102015

grid users using dynamic

time warping. Electronics

smart

Chicco, G., Napoli, R., and Piglione, F. (2006). Comparisons among clustering
techniques for electricity customer classiﬁcation. IEEE Trans. Power Syst. 21, 933–940.
doi: 10.1109/TPWRS.2006.873122

Lange, T., Roth, V., Braun, M. L., and Buhmann,
based validation of
clustering
doi: 10.1162/089976604773717621

J. M.
solutions. Neural Comput.

(2004). Stability-
1299–1323.
16,

Frontiers in Artiﬁcial Intelligence

14

frontiersin.org

---

<!-- PAGE 15 -->

Zhao et al.

10.3389/frai.2026.1829649

Li, Y., Yu, R., Shahabi, C., and Liu, Y. (2018). Diﬀusion convolutional recurrent neural
network: data-driven traﬃc forecasting. arXiv preprint arXiv:1707.01926.

Lin, S., Li, F., Tian, E., Fu, Y., and Li, D. (2019). Clustering load proﬁles
for demand response applications.
IEEE Trans. Smart Grid 10, 1599–1607.
doi: 10.1109/TSG.2017.2773573

Long, C., Yang, X., Su, Y., Liu, F., Ma, R., Ma, T., et al. (2025). Air conditioning load
forecasting for geographical grids using deep reinforcement learning and density-based
spatial clustering of applications with noise and graph attention networks. Energies
18:2832. doi: 10.3390/en18112832

Lu, J., Liu, A., Dong, F., Gu, F., Gama, J., and Zhang, G. (2018). Learning
under concept drift: a review. IEEE Trans. Knowl. Data Eng. 31, 2346–2363.
doi: 10.1109/TKDE.2018.2876857

Luxburg, U. (2007). A tutorial on spectral clustering. Stat. Comput. 17, 395–416.
doi: 10.1007/s11222-007-9033-z

Muyulema-Masaquiza, D., and Ayala-Chauvin, M. (2025). Segmentation of energy
consumption using k-means: applications in tariﬃng, outlier detection, and demand
prediction in non-smart metering systems. Energies 18:3083. doi: 10.3390/en18123083

Pareja, A., Domeniconi, G., Chen,
J., Ma, T., Suzumura, T., Kanezashi, H.,
et al. (2020). “Evolvegcn: evolving graph convolutional networks for dynamic
graphs,” in Proceedings of the AAAI Conference on Artiﬁcial Intelligence, 5363–5370.
doi: 10.1609/aaai.v34i04.5984

Sankar, A., Wu, Y., Gou, L., Zhang, W., and Yang, H. (2020). “Dysat: deep neural
representation learning on dynamic graphs via self-attention networks,” in Proceedings
of the 13th International Conference on Web Search and Data Mining, 519–527.
doi: 10.1145/3336191.3371845

Tariq, M. A. U. R., Poorolajal, J., and Shah, S. A. A. (2022). Deterioration of
electrical load forecasting models in a smart grid environment. Sensors 22:4363.
doi: 10.3390/s22124363

Tolas, R., Portase, R., and Potolea, R. (2024). From individual device usage to household
energy consumption proﬁling. Electronics 13:2325. doi: 10.3390/electronics131
22325

Veliˇckovi´c, P., Fedus, W., Hamilton, W. L., Lió, P., Bengio, Y., and Hjelm, R. D. (2019).
“Deep graph infomax,” in International Conference on Learning Representations, 1–13.

Verma, S., and Rao, A.
for decentralized smart grid cybersecurity. Front. Artif.
doi: 10.3389/frai.2025.1557960

(2025). A short

report on deep learning synergy
Intell. 8:1557960.

Wang, B., Li, Y., Ming, W., and Wang, S. (2020). Deep reinforcement learning method
for demand response management of interruptible load. IEEE Trans. Smart Grid 11,
3146–3155. doi: 10.1109/TSG.2020.2967430

Wang, M., Li, H., and Wu, J. (2023). Self-supervised dynamic graph representation
learning via temporal subgraph contrast. ACM Trans. Knowl. Disc. Data 18, 1–20.
doi: 10.1145/3612931

Ratanamahatana, C. A., and Keogh, E. (2004). “Everything you know about dynamic
time warping is wrong,” in Proceedings of the Third Workshop on Mining Temporal and
Sequential Data, 1–11.

Wang, Y., Chen, Q., Hong, T., and Kang, C. (2019). Review of smart meter data
analytics: applications, methodologies, and challenges. IEEE Trans. Smart Grid 10,
3125–3148. doi: 10.1109/TSG.2018.2818167

Rossi, E., Chamberlain, B., Frasca, F., Eynard, D., Monti, F., and Bronstein, M.
(2020). Temporal graph networks for deep learning on dynamic graphs. arXiv preprint
arXiv:2006.10637.

Wu, Z., Pan, S., Long, G., Jiang, J., and Zhang, C. (2019). “Graph wavenet for deep
spatial-temporal graph modeling,” in Proceedings of the International Joint Conference
on Artiﬁcial Intelligence (IJCAI), 1907–1913. doi: 10.24963/ijcai.2019/264

Rousseeuw, P.
and validation of
doi: 10.1016/0377-0427(87)90125-7

cluster

J.

(1987). Silhouettes: a graphical aid to the interpretation
53–65.

J. Comput. Appl. Math.

analysis.

20,

and Chiba,

Sakoe, H.,
optimization for
doi: 10.1109/TASSP.1978.1163055

S.
spoken word recognition.

(1978). Dynamic

algorithm
IEEE Trans. Acoust. 26, 43–49.

programming

Zhang, S., Zhu, J., Luo, E., Zhu, X., and Yang, Q. (2025). Dpck: an adaptive diﬀerential
privacy-based ck-means clustering scheme for smart meter data analysis. Electronics
14:2074. doi: 10.3390/electronics14102074

J., Liu, S., Ouyang, L., Ruan,
for

Zou,
demand
response
doi: 10.3390/electronics13244941

residential

J., and Tang, S.
buildings.
smart

(2024). Carbon-aware
13:4941.

Electronics

Frontiers in Artiﬁcial Intelligence

15

frontiersin.org

<!-- MARKITDOWN CONVERSION -->

<!-- Full MarkItDown conversion for formatting fidelity. -->

TYPE OriginalResearch
PUBLISHED 25May2026
DOI 10.3389/frai.2026.1829649
DynEC: dynamic evolutionary
clustering for power user load
OPENACCESS
profiling using multi-view graph
EDITEDBY
EmadMaherNatsheh,
An-NajahNationalUniversity,Palestine neural networks
REVIEWEDBY
BasharTahayna,
An-NajahNationalUniversity,Palestine
JehadM.Hamamreh, LeiZhao1,HongZhao1,MengjieLi1,JiaWang1,XingsiKe1 and
An-NajahNationalUniversityLibraries, YuminYao2*
Palestine
*CORRESPONDENCE 1StateGridSichuanElectricPowerCorporation,Chengdu,China,2SchoolofComputerScienceand
YuminYao Engineering,CentralSouthUniversity,Changsha,China
yaoyumin@csu.edu.cn
RECEIVED13March2026
Introduction: With the deep integration of generation-transmission-load-
REVISED02May2026
ACCEPTED04May2026 storage systems, the power demand side has become highly dynamic and
PUBLISHED25May2026
stochastic, challenging the traditional assumption that user behavior remains
CITATION stationaryovertime.Staticclusteringmodelsthereforesufferfromsensitivityto
ZhaoL,ZhaoH,LiM,WangJ,KeXand
YaoY(2026)DynEC:dynamic dailynoiseandfalseuseridentityswitching.
evolutionaryclusteringforpoweruser Methods: This study proposes Dynamic Evolutionary Clustering (DynEC), a
loadprofilingusingmulti-viewgraph
multi-viewgraphneuralnetworkframeworkforpoweruserloadprofiling.DynEC
neuralnetworks.
Front.Artif.Intell.9:1829649. constructsasparsemulti-viewdynamicgraphthatcapturesgeometricproximity,
doi:10.3389/frai.2026.1829649 temporal alignment through constrained dynamic time warping, and statistical
dependencies. A gated spatiotemporal graph neural network then optimizes
COPYRIGHT
©2026 Zhao,Zhao,Li,Wang,Keand a dual-objective loss to learn latent representations while balancing current
Yao.Thisisanopen-accessarticle
snapshotqualityandhistoricaltemporalsmoothness.
distributedunderthetermsofthe
CreativeCommonsAttributionLicense Results: Experiments on real-world datasets show that DynEC outperforms
(CCBY).Theuse,distributionor existingbaselinemethods.Theproposedframeworkidentifiesgenuineconcept
reproductioninotherforumsis
driftmoreaccuratelywhilereducingerroneousclusterswitching.
permitted,providedtheoriginalauthor(s)
andthecopyrightowner(s)arecredited Discussion: DynEC provides a stable and reliable profiling tool for modern
andthattheoriginalpublicationinthis powergridmanagementbymodelingloadprofilingasacontinuousevolutionary
journaliscited,inaccordancewith
processratherthanasetofindependentstaticclusteringtasks.
acceptedacademicpractice.Nouse,
distributionorreproductionispermitted
whichdoesnotcomplywiththeseterms.
KEYWORDS
conceptdrift,dynamicevolutionaryclustering,graphneuralnetworks,loadprofiling,
multi-viewlearning,source-grid-load-storage
1 Introduction
With the development of Advanced Metering Infrastructure (AMI) and artificial
intelligence(Balamuruganetal.,2025;Belgeetal.,2024),loadforecastinginpowergrids
has shifted from a passive interface to an active, bidirectional engagement point. This
structuralshifttowarda“generation-grid-load-storage”paradigmnecessitatesatransition
frommacroscopicdemandmanagementtoprecise,user-centricprofiling.Atthecoreof
thistransformationliesloadprofiling,aspreciseloadprofilesserveasthefoundationfor
dynamic pricing design, demand response (DR) targeting (Zouetal., 2024; Tolasetal.,
2024;Zhangetal.,2025),andgridflexibilityplanningundercarbonneutralityconstraints
(Badheetal.,2025;VermaandRao,2025).
With the proliferation of distributed energy resources and electric vehicles, users
are increasingly becoming grid prosumers who both consume and generate electricity.
FrontiersinArtificialIntelligence 01 frontiersin.org

Zhaoetal. 10.3389/frai.2026.1829649
Consequently, influenced by real-time pricing, extreme TABLE1Comparisonbetweenstaticanddynamicclusteringparadigms.
weather events, and evolving work-from-home practices, daily
Dimension Staticclustering Dynamic
consumptionpatternshavebecomehighlystochastic.Thesefactors
clustering
continuously reshape the load curve, triggering concept drift
(Gamaetal.,2014;Luetal.,2018).Thetraditionalassumptionthat Metaphor Staticphoto Continuousvideo
user behavior remains strictly stationary over time is no longer
Temporal Ignorestimeorflattensit Explicitlymodelsevolution
suitableforthispattern.
perspective (snapshot)
Current methods treat load profiling as a static snapshot
Feature Global/staticstatistics Time-varyingembeddings
problem, aggregating data from several months to assign users a
representation
single,permanentlabel.Whileusefulforhigh-levelinfrastructure
planning, static clustering fails severely in grids with a high Primarygoal Discoverlong-term Capturepatternevolution
proportion of renewable energy. When users fundamentally alter stablepatterns anddrift
theirroutines(e.g.,bypurchasinganelectricvehicle),staticmodels Driftsensitivity Cannotdetectconcept Adaptabletoanddetects
exhibitdelayedadaptation,leadingtopersistentmisclassification. drift drift
Conversely,ifoperatorsrepeatedlyapplystaticclusteringtodaily
Computational Low(one-time) High(online/recursive)
or weekly data blocks, the model overreacts to normal daily
cost
noise. Users may jump erratically between clusters without any
Application Long-termplanning Real-timeDR,anomaly
actualunderlyingbehavioralchange.Thisfalse“identityswitching”
detection
underminesthetemporalsmoothnessrequiredforreliabledemand
response (DR) targeting. Dynamic evolutionary clustering offers
a solution by modeling profiles not as isolated snapshots, but as
continuousvideosthatexplicitlytrackhowbehaviorevolves,while
achieves excellent internal clustering quality, as measured by
penalizingunstableclusterhopping.
the silhouette coefficient and ARI, while significantly reducing
It is well known that Euclidean metrics are highly vulnerable
the cluster switching rate (CSR). By effectively tracking genuine
to temporal phase shifts (Kimetal., 2025). Two users may
behavioral shifts while ignoring daily noise, DynEC provides a
have identical consumption patterns, but if one wakes up
highly stable and actionable profiling engine for next-generation
an hour later, the Euclidean distance will place them in
smartgrids.
completely different clusters. Dynamic Time Warping (DTW)
The remainder of this article is structured as follows: Section
(BerndtandClifford, 1994; KeoghandRatanamahatana, 2005)
2 reviews the relevant literature. Section 3 provides a detailed
addresses this alignment issue but suffers from poor scalability
description of the DynEC methodology and complexity analysis.
on large-scale datasets. Meanwhile, while spatiotemporal graph
Section 4 presents the experimental setup and results. Section 5
neural networks (ST-GNNs) have achieved some success in load
concludesthearticle.
forecasting,theylackthespecificlossfunctionsrequiredtobalance
structuralfeaturelearningwithtemporalclusteringconsistencyin
unsupervisedsettings.
In summary, to bridge the gap between structural graph
2 Related work
learning and dynamic pattern evolution, this study proposes
DynEC(DynamicEvolutionaryClustering).Ourapproachmakes
2.1 Dynamic community detection and
three main contributions: First, it constructs a multi-view
evolutionary clustering
dynamicgraphtoaddressthetemporalevolutionofuserprofiles.
By integrating geometric proximity, temporal alignment (via
The effective organization of dynamic data streams is a
computationally efficient cDTW), and statistical dependencies
focal point of academic research. This field is typically divided
(Pearson correlation) into a unified graph structure, it reliably
into two main areas: dynamic community detection in social
capturesuserrelationshipsevenunderseverephaseshifts.Second,
networksandevolutionaryclusteringindatamining.Inparticular,
we design a self-supervised deep evolutionary graph learning
(Chakrabartietal., 2006) proposed a formalized “evolutionary
framework that combines a gated spatio-temporal graph encoder
clustering”framework,notingthattheoptimalclusteringsolution
with a dual-objective evolutionary optimization strategy. By
attimetrequiresbalancingtwocompetingobjectives:maximizing
adopting a network-optimized dual loss function that balances
the current data fit (Snapshot Quality) while minimizing the
snapshot quality and temporal smoothness, the model adapts to
deviation from previous clustering results (Temporal Cost).
genuine concept drift while suppressing false identity switching.
However, in traditional methods, the trade-off parameters are
Third, we evaluate the framework using real-world smart meter
typically user-defined. To overcome this limitation, deep graph
data from three different cities. The results confirm that it
learning can automatically learn adaptive, dynamically evolving
parameters.
Building on the perspectives proposed by Wangetal. (2019)
Abbreviations:DynEC,DynamicEvolutionaryClustering;GNN,GraphNeural
and Tariqetal. (2022), this study adapts static clustering models
Network;GST-GNN,GatedSpatio-TemporalGraphNeuralNetwork;cDTW,
for dynamic environments; Table1 summarizes the conceptual
Constrained Dynamic Time Warping; CSR, Cluster Switching Rate; ARI,
AdjustedRandIndex;V2G,Vehicle-to-Grid;DR,DemandResponse. differencesbetweenthestaticanddynamicparadigms.
FrontiersinArtificialIntelligence 02 frontiersin.org

Zhaoetal. 10.3389/frai.2026.1829649
In the context of smart grids, user behavior often undergoes employ spatio-temporal graph neural networks (ST-GNNs).
conceptdrift,causingthestatisticalpropertiesoftargetvariablesto Typical model architectures, such as Graph WaveNet (Wuetal.,
changeovertime(Gamaetal.,2014;Jiangetal.,2021).Traditional 2019)andDCRNN(Lietal.,2018),integrategraphconvolutional
static methods, such as applying K-Means to daily snapshots, networks(GCNs)withspatiotemporalconvolutionalorrecurrent
typically overreact to noise. This can trigger “cluster hopping,” neuralnetworks(RNNs).Thisintegrationsimultaneouslymodels
where users oscillate between clusters without any actual change spatialdependencies(powergridtopology)andtemporaldynamics
in behavior (Jainetal., 2021). Conversely, incremental learning (load trends). EvolveGCN (Parejaetal., 2020) uses RNNs to
methods that update only cluster centroids suffer from “lag,” evolve the parameters of the GCN itself to adapt to changes
failingtoadaptquicklytosuddenshifts.Therefore,theframework in global distributions. However, for load profiling, preserving
proposed in this study adopts explicit modeling of nodes, individual user identities is crucial. Therefore, TGN (Rossietal.,
incorporates temporal evolution, and updates cluster centroids, 2020)capturescontinuoustemporaldynamicsthroughamemory
enablingthemodeltoadapttodynamicchangesinclustering. module to extract individual user profiling features. DySAT
Recent advances in graph-stream mining have introduced (Sankaretal., 2020) constructs adaptive dynamic profiles by
methods that maintain temporal summaries of graph structures. introducingaself-attentionmechanismtojointlymodelstructural
For example, Time2Graph (Chengetal., 2020) treats temporal and temporal evolution. Furthermore, deep graph clustering has
evolution as a sequence of shapelets, but it still relies on static emerged as a highly promising direction. Works such as SDCN
K-Means in the final clustering step. DynEC enhances existing (Boetal.,2020)havesuccessfullyintegratedstructuralinformation
methods by directly integrating temporal consistency into deep into clustering tasks. Concurrently, contrastive learning methods
learningobjectives. (e.g., temporal subgraph contrastive learning Wangetal., 2023)
have demonstrated potential in dynamic graph representations.
ThisstudyfocusesonevolvingnodeembeddingsviaGRUmemory
2.2 Deep learning in load profiling modules to ensure the model retains stable historical context for
eachspecificuser,therebypreventingidentitylossduringtemporal
Current deep learning technologies significantly advance updates.
smartgridmanagementbyenablingrobustloadprofileclustering Despitesignificantprogressintheaforementionedareas,most
and predictive pattern recognition. For instance, Longetal. spatiotemporal graph neural network (ST-GNN) research has
(2025) combined density-based clustering (DBSCAN) with a primarily focused on supervised learning tasks, such as load
graph attention network to predict air conditioning loads across estimation (Fekrietal., 2021) or fault detection. Consequently,
geographic grids. This approach demonstrates the value of the exploration of unsupervised clustering remains very limited.
groupingspatiallycorrelatedunits.Inthecontextofdatasecurity, Foundational work, such as DGI (Velicˇkovic´etal., 2019) and
Zhangetal.(2025)proposedaCK-Meansclusteringschemebased MVGRL (HassaniandKhasahmadi, 2020), has demonstrated the
onadaptivedifferentialprivacyforsmartmeterdataanalysis.This feasibilityofunsupervisedgraphrepresentationlearning.However,
ensures both privacy protection and computational efficiency. applying these principles to power grid user profiling with
Furthermore, Muyulema-MasaquizaandAyala-Chauvin (2025) dynamicallyevolvingfeaturesremainschallenging.
showedthateffectiveconsumptionsegmentationdirectlysupports
dynamicpricing,anomalydetection,anddemandforecasting.
2.3 Similarity measures: geometric,
2.2.1 Staticdeepclustering shape-based, and statistical
Early studies typically employed dimension reduction In user profiling tasks based on Graph Neural Networks
techniques,suchasprincipalcomponentanalysis(PCA)andhand- (GNNs),constructingmeaningfulusergraphsiscriticaltomodel
engineeredfeatures,followedbyK-Meansclustering(Chiccoetal., performance. Although the commonly used Euclidean distance
2006). Later, deep clustering methods based on autoencoders offers an ideal computational complexity of O(D), it is highly
enabledtheconcurrentoptimizationoffeaturelearningandcluster sensitivetotemporalphaseshiftswhenprocessingtime-seriesdata
assignment. However, these methods are inherently static. They likeloadcurves.Evenminorphaseshiftscanincorrectlyseparate
treatdataasacollectionofindependentandidenticallydistributed inherentlysimilarcurves,abehaviordemonstratedinexperimental
(i.i.d.) samples, ignoring the sequential dependencies inherent in analysesbyKimetal.(2025).
loadprofiles.Whileeffectiveforstaticsnapshots,theyfailtocapture Toaddressthisissue,weincorporateDynamicTimeWarping
the temporal sequence in dynamic grid data. Therefore, adaptive (DTW). As emphasized by BerndtandClifford (1994), DTW
modeling is crucial; Wangetal. (2020) specifically adopted deep effectively compensates for local deviations along the time axis
reinforcementlearningfordemandresponsemanagement. by finding an optimal non-linear alignment. However, standard
DTWhasatimecomplexityofO(D2),makingitcomputationally
expensive for large-scale applications. For load curves with
2.2.2 Spatio-temporalgraphneuralnetworks prominent periodicity, Constrained Dynamic Time Warping
(cDTW) offers a more efficient alternative. The pioneering work
Toeffectivelycapturecomplexspatialstructuresandtemporal of SakoeandChiba (1978) demonstrates that introducing Sakoe–
dependencies, advanced power grid analysis techniques typically Chiba bands to apply local constraints on the alignment path
FrontiersinArtificialIntelligence 03 frontiersin.org

| Zhaoetal. |     |     |     |     |     |     |     |     |     |     | 10.3389/frai.2026.1829649 |     |     |
| --------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------------------- | --- | --- |
maintains accuracy while controlling time complexity within a 3.1.1 Prerequisites
polynomialrangeofthenumberofdatapointsDandthesignal-
=
to-noise ratio w. A more systematic review can be found in Definition 1 (Dynamic load profile stream (DLPS)). Let U
RatanamahatanaandKeogh(2004). {u1,u2,...,uN }bethesetofelectricityusers,whereN isthetotal
∈ {1,2,...,T},weobservea
Building on this, recent studies have also explored mapping numberofusers.Ateachtimestept
|                |     |                |     |           |           |               | loadmatrixX(t).Letx(t) |     | ∈ RDdenotetheelectricityconsumption |     |     |     |     |
| -------------- | --- | -------------- | --- | --------- | --------- | ------------- | ---------------------- | --- | ----------------------------------- | --- | --- | --- | --- |
| DTW similarity |     | into Euclidean |     | space via | Shapelets | to explicitly |                        |     |                                     |     |     |     |     |
i
enforce alignment constraints during synthesis (ElAmourietal., profileofuserui overatimeintervaloflengthD.Thecontinuous
2023). However, the automatic Shapelet discovery process often loadprofilestreamisthusdefinedasEquation1:
| requires | intensive | computation, |     | causing | practical | difficulties | in  |     |                         |     |     |     |     |
| -------- | --------- | ------------ | --- | ------- | --------- | ------------ | --- | --- | ----------------------- | --- | --- | --- | --- |
|          |           |              |     |         |           |              |     |     | X ={X(1),X(2),...,X(T)} |     |     |     | (1) |
large-scalesituations.
| To combine |     | the strengths |     | of various | similarity | measures, |     |     |     |     |     |     |     |
| ---------- | --- | ------------- | --- | ---------- | ---------- | --------- | --- | --- | --- | --- | --- | --- | --- |
Linetal. (2019) proposed integrating multiple metrics. This Definition2(Conceptdrift). Adatastreamisconsideredtoexhibit
|          |              |           |     |            |     |                  | concept | drift when | its underlying | joint | probability | distribution |     |
| -------- | ------------ | --------- | --- | ---------- | --- | ---------------- | ------- | ---------- | -------------- | ----- | ----------- | ------------ | --- |
| strategy | incorporates | geometric |     | similarity |     | (e.g., Euclidean |         |            |                |       |             |              |     |
distance), shape similarity (cDTW), and statistical dependence changesovertime,asshowninEquation2:
| (specifically, | the | Pearson          | correlation |            | coefficient | in              | our            |     |                          |      |                 |        |      |
| -------------- | --- | ---------------- | ----------- | ---------- | ----------- | --------------- | -------------- | --- | ------------------------ | ---- | --------------- | ------ | ---- |
|                |     |                  |             |            |             |                 |                |     | P(X(t))(cid:3)=P(X(t+1)) |      |                 |        | (2)  |
| work) into     | a   | multidimensional |             | graph,     | thereby     | enabling        | the            |     |                          |      |                 |        |      |
| construction   | of  | more robust      | graph       | structures |             | in the presence |                |     |                          |      |                 |        |      |
|                |     |                  |             |            |             |                 | In the context | of  | power grids,             | such | drift typically | arises | from |
ofnoise.
|     |     |     |     |     |     |     | individual | behavioral | shifts, | such as installing |     | new appliances | or  |
| --- | --- | --- | --- | --- | --- | --- | ---------- | ---------- | ------- | ------------------ | --- | -------------- | --- |
developingnewelectricvehiclechargingpatterns,orfromsystem-
levelmacrochanges,suchasseasonaleffectsorpricingadjustments.
| 2.4 Clustering |     | validation |     | and | stability |     |            |            |       |        |          |     |          |
| -------------- | --- | ---------- | --- | --- | --------- | --- | ---------- | ---------- | ----- | ------ | -------- | --- | -------- |
|                |     |            |     |     |           |     | Definition | 3 (Dynamic | graph | flow). | We model | the | evolving |
analysis
|     |     |     |     |     |     |     | relationships | among | users | as a sequence | of dynamic | graphs, | as  |
| --- | --- | --- | --- | --- | --- | --- | ------------- | ----- | ----- | ------------- | ---------- | ------- | --- |
showninEquation3:
Traditionalclusteringvaliditymetrics,suchastheRousseeuw
coefficient (Rousseeuw, 1987) or the Davies–Bouldin index, G ={G(1),G(2),...,G(T)} (3)
primarilyfocusonsnapshotquality,verifyingthecompactnessand
separationofclusters.Theyignoretemporalinstabilityandimpose
|     |     |     |     |     |     |     | Here,thenodesetV |     | = U | remainsfixed,whilethetime-varying |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ---------------- | --- | --- | --------------------------------- | --- | --- | --- |
nopenaltywhenusersjumperraticallybetweenclusters. adjacency matrix A(t) captures the instantaneous similarities
AsnotedbyJainetal.(2021),inindustrialapplications,stability
betweenusersattimet.
| is just as | important   | as        | accuracy.  | A clustering |      | algorithm | that    |     |     |     |     |     |     |
| ---------- | ----------- | --------- | ---------- | ------------ | ---- | --------- | ------- | --- | --- | --- | --- | --- | --- |
| produces   | drastically | different | partitions |              | when | the input | data is |     |     |     |     |     |     |
slightly perturbed is operationally useless. In dynamic settings, 3.1.2 Problemdescription
thistranslatesdirectlytotemporalstability:unlesstheunderlying
data distribution actually shifts, the cluster assignments should GivenasequenceofdynamicgraphsG,ourobjectiveistolearn
not change significantly between time steps (Langeetal., 2004; amappingfunctionfθ ateachtimestept,asshowninEquation4:
| Luxburg, | 2007). | We use | the cluster | switching |     | rate (CSR) | and |     |     |     |     |     |     |
| -------- | ------ | ------ | ----------- | --------- | --- | ---------- | --- | --- | --- | --- | --- | --- | --- |
temporalsmoothness(TS)metricstoformalizethisrequirement. fθ:G(t)→C(t) (4)
Thisdual-metricsystemprovidesaholisticevaluationframework
thatbalancesinternalclusterqualitywithoperationalrobustness. where C(t) = {C 1,...,C } denotes the cluster partition of the N
K
|     |     |     |     |     |     |     | users into | K distinct | groups. | This partition | must | simultaneously |     |
| --- | --- | --- | --- | --- | --- | --- | ---------- | ---------- | ------- | -------------- | ---- | -------------- | --- |
optimizetwocompetingobjectives:
|     |     |     |     |     |     |     | Snapshotquality:UserswithinthesameclusterC |     |     |     |     | shouldexhibit |     |
| --- | --- | --- | --- | --- | --- | --- | ------------------------------------------ | --- | --- | --- | --- | ------------- | --- |
k
3 Methodology high intra-cluster similarity in terms of geometric characteristics
|             |     |            |     |     |     |     | (e.g., load              | magnitude | and shape), | temporal | synchronization, |     | and |
| ----------- | --- | ---------- | --- | --- | --- | --- | ------------------------ | --------- | ----------- | -------- | ---------------- | --- | --- |
| 3.1 Problem |     | definition |     |     |     |     | statisticaldependencies. |           |             |          |                  |     |     |
Temporalconsistency:Theclusteringstructureshouldevolve
This study formalizes the dynamic user segmentation smoothlyovertime.Specifically,thecurrentpartitionC(t) should
C(t−1)
problem under concept drift as a dynamic graph clustering not deviate drastically from the previous partition unless
task. Rather than treating electricity consumers as isolated genuine concept drift occurs, thereby minimizing erroneous user
identityswitching.
| entities        | with static | labels,          | we model | the             | continuous | evolution       |               |     |              |     |     |     |     |
| --------------- | ----------- | ---------------- | -------- | --------------- | ---------- | --------------- | ------------- | --- | ------------ | --- | --- | --- | --- |
| of their        | energy      | consumption      |          | behaviors       |            | through complex |               |     |              |     |     |     |     |
| spatio-temporal |             | interactions.    |          | By representing |            | consumers       |               |     |              |     |     |     |     |
|                 |             |                  |          |                 |            |                 | 3.2 Framework |     | architecture |     |     |     |     |
| as nodes        | and         | their multi-view |          | similarities    |            | as time-varying |               |     |              |     |     |     |     |
| edges, the      | challenge   | of               | tracking | genuine         | behavioral | shifts          | is            |     |              |     |     |     |     |
mathematically transformed into an evolutionary representation AsillustratedinFigure1,theproposedDynamicEvolutionary
learning and clustering optimization problem over a sequence of Clustering framework consists of two core modules that operate
| dynamicgraphs.                    |     |     |     |     |     |     | sequentiallyateachtimestep. |     |     |     |     |                 |     |
| --------------------------------- | --- | --- | --- | --- | --- | --- | --------------------------- | --- | --- | --- | --- | --------------- | --- |
| FrontiersinArtificialIntelligence |     |     |     |     |     |     | 04                          |     |     |     |     | frontiersin.org |     |

| Zhaoetal. |     |     |     |     |     |     |     |     |     |     | 10.3389/frai.2026.1829649 |     |     |
| --------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------------------- | --- | --- |
First, the Multi-view dynamic graph construction module pair of users (i,j), the Euclidean distance at time t is defined as
| (Section3.3)takestherawmulti-dimensionalloadprofilesasinput |     |               |      |              |        |        | Equation5: |     |                    |       |               |     |     |
| ----------------------------------------------------------- | --- | ------------- | ---- | ------------ | ------ | ------ | ---------- | --- | ------------------ | ----- | ------------- | --- | --- |
| and constructs                                              | a   | comprehensive | user | relationship | graph. | Rather |            |     |                    |       |               |     |     |
|                                                             |     |               |      |              |        |        |            |     | dgeo(i,j)=(cid:5)x | (t)−x | (t)(cid:5) 2. |     | (5) |
than relying on a single similarity metric, it models inter-user i j
relationships from three complementary perspectives: geometric Based on this metric, a k-Nearest Neighbors (kNN) graph is
proximity(Euclideandistance),temporalalignment(Constrained constructed:Ageo(i,j)=1ifuserjisamongthek-nearestneighbors
| Dynamic | Time | Warping, | cDTW), | and statistical | dependency |     |     |     |     |     |     |     |     |
| ------- | ---- | -------- | ------ | --------------- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- |
ofuseri,and0otherwise.Thisviewconnectsusersexhibitinghighly
(Pearson correlation). This multi-view fusion mechanism is synchronized consumption variations predominantly on the same
| specifically | designed | to capture | complex | non-linear | correlations |     |     |     |     |     |     |     |     |
| ------------ | -------- | ---------- | ------- | ---------- | ------------ | --- | --- | --- | --- | --- | --- | --- | --- |
temporalscale,therebyreflectinglocalgeometricsimilarities.
| and robustly | align | user behaviors | even | in the | presence | of severe |     |     |     |     |     |     |     |
| ------------ | ----- | -------------- | ---- | ------ | -------- | --------- | --- | --- | --- | --- | --- | --- | --- |
temporalphaseshifts.
Second, the Deep evolutionary graph learning module 3.3.3 Temporalalignmentview(A ):
dtw
(Section 3.4) performs evolutionary representation learning and characterizingshapesimilarityundertemporal
| clusteringassignment.ItintegratesaGatedSpatio-TemporalGraph |             |              |     |       |           |         | shifts |     |     |     |     |     |     |
| ----------------------------------------------------------- | ----------- | ------------ | --- | ----- | --------- | ------- | ------ | --- | --- | --- | --- | --- | --- |
| Encoder                                                     | (comprising | a Multi-Head |     | Graph | Attention | Network |        |     |     |     |     |     |     |
and a Gated Recurrent Unit) to extract evolution-aware node A critical limitation of the geometric view is its sensitivity to
| embeddings. | These | embeddings | are | then optimized |     | through | a   |     |     |     |     |     |     |
| ----------- | ----- | ---------- | --- | -------------- | --- | ------- | --- | --- | --- | --- | --- | --- | --- |
temporalphaseshifts.Forinstance,twouserswithmorphologically
Dual-Objective Optimization mechanism that explicitly balances similarloadcurvesmaybedeemeddissimilarbyEuclideandistance
thesnapshotclusteringquality(viaKLdivergence)withtemporal due to a time lag (e.g., cooking activities occurring at different
smoothness. By jointly optimizing these two objectives, the times).Tomitigatethis,thetemporalalignmentviewincorporates
architecture effectively solves the stability-plasticity dilemma, Constrained Dynamic Time Warping (cDTW). cDTW minimizes
| enabling | the reliable | tracking | of genuine | concept |     | drift while |     |     |     |     |     |     |     |
| -------- | ------------ | -------- | ---------- | ------- | --- | ----------- | --- | --- | --- | --- | --- | --- | --- |
thecumulativedistancebetweenmatchedpointsbyidentifyingan
aggressively suppressing erroneous identity switching caused by optimalwarpingpathW ={w1,...,wK }betweentwosequencesxi
| dailynoise. |     |     |     |     |     |     | andxjasshowninEquation6: |     |     |     |     |     |     |
| ----------- | --- | --- | --- | --- | --- | --- | ------------------------ | --- | --- | --- | --- | --- | --- |
(cid:2)K
cDTW(xi,xj)=min
| 3.3 Multi-view |     | dynamic | graph |     | construction |     |     |     |     |     | w   | k , | (6) |
| -------------- | --- | ------- | ----- | --- | ------------ | --- | --- | --- | --- | --- | --- | --- | --- |
W
k=1
This section elucidates the rationale behind the multi-view |i − | <
|     |     |     |     |     |     |     | subject to | the constraint |     | k j k | w, where | w k denotes | the |
| --- | --- | --- | --- | --- | --- | --- | ---------- | -------------- | --- | ----- | -------- | ----------- | --- |
framework, detailing the specific relationships characterized by distance of the k-th matched pair and w is the Sakoe–Chiba
| each view | and | the mechanism | for | fusing them | into | a unified |     |     |     |     |     |     |     |
| --------- | --- | ------------- | --- | ----------- | ---- | --------- | --- | --- | --- | --- | --- | --- | --- |
windowwidth.Giventheinherentperiodicityofdailyloadprofiles,
graph structure. We construct the user similarity structure from imposing a narrow window w reduces the time complexity to
threecomplementaryperspectives—geometricproximity,temporal O(D·w),ensuringapproximatelylinearscalabilitywhilepreserving
| alignment, | and | statistical | dependency—to | facilitate | robust | graph |     |     |     |     |     |     |     |
| ---------- | --- | ----------- | ------------- | ---------- | ------ | ----- | --- | --- | --- | --- | --- | --- | --- |
alignmentprecision.
representationlearning. Upon computing the cDTW distance, a Gaussian kernel is
|     |     |     |     |     |     |     | employed | to transform | the | distance | into a | similarity measure | as  |
| --- | --- | --- | --- | --- | --- | --- | -------- | ------------ | --- | -------- | ------ | ------------------ | --- |
showninEquation7:
3.3.1 Motivation:towardacomprehensiveuser
| relationshipgraph |     |     |     |     |     |     |     | S   | (i,j)=exp(−d2(i,j)/σ2). |     |     |     | (7) |
| ----------------- | --- | --- | --- | --- | --- | --- | --- | --- | ----------------------- | --- | --- | --- | --- |
dtw
At each time step t, the objective is to construct a Theresultingsimilaritymatrixissubsequentlythresholdedto
dynamic graph G(t) = (V,E(t)) that authentically reflects the yield a sparse adjacency matrix A . This view effectively links
dtw
multifaceted relationships among users. A single metric, such as userswhoseloadprofilesaremorphologicallysimilarbuttemporally
Euclidean distance, is often insufficient as it primarily captures shifted,servingasacrucialcomplementtothegeometricview.
similarityinnumericalmagnitudeatsynchronizedsamplingpoints.
| Consequently, | it  | fails to | account for: | load profiles | that | exhibit |     |     |     |     |     |     |     |
| ------------- | --- | -------- | ------------ | ------------- | ---- | ------- | --- | --- | --- | --- | --- | --- | --- |
similar morphological patterns but are subject to temporal 3.3.4 Correlationview(A corr ):characterizing
statisticaldependency
| phase shifts, | as  | well as users | who display | significant      |     | disparities |     |     |     |     |     |     |     |
| ------------- | --- | ------------- | ----------- | ---------------- | --- | ----------- | --- | --- | --- | --- | --- | --- | --- |
| in magnitude  | or  | phase         | but still   | share underlying |     | statistical |     |     |     |     |     |     |     |
dependencies. To address these limitations, we adopt a multi- Twoloadprofilesmaydiffersignificantlyinmagnitudeorphase
view modeling approach, synthesizing three distinct adjacency yet still exhibit strong co-movement patterns. The dependency
structurestoderiveaunifiedadjacencymatrixA(t). view, therefore, uses the absolute Pearson correlation coefficient
|     |     |     |     |     |     |     | to quantify     | statistical | dependency | between          | users | while remaining |      |
| --- | --- | --- | --- | --- | --- | --- | --------------- | ----------- | ---------- | ---------------- | ----- | --------------- | ---- |
|     |     |     |     |     |     |     | computationally | efficient   | for        | high-dimensional |       | continuous      | load |
3.3.2 Geometricview(A ):characterizing profiles. For two load profiles xi and xj, the correlation score is
geo
magnitude-basedproximity
definedasEquation8:
|     |     |     |     |     |     |     |     |     | (cid:3) |     |         | (cid:3) |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ------- | --- | ------- | ------- | --- |
|     |     |     |     |     |     |     |     |     | (cid:3) |     | (cid:6) | (cid:3) |     |
The geometric view captures the local proximity of user load (cid:3) (xi −x¯ i) (xj −x¯ j) (cid:3)
|     |     |     |     |     |     |     |     | ρ(i,j)= | (cid:3)          |             |               | (cid:3).        | (8) |
| --- | --- | --- | --- | --- | --- | --- | --- | ------- | ---------------- | ----------- | ------------- | --------------- | --- |
|     |     |     |     |     |     |     |     |         | (cid:3)(cid:5)xi | −x¯ (cid:5) | (cid:5)xj −x¯ | (cid:5) (cid:3) |     |
profiles within the Euclidean space at a given time grid. For any i 2 j 2
| FrontiersinArtificialIntelligence |     |     |     |     |     |     | 05  |     |     |     |     | frontiersin.org |     |
| --------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --------------- | --- |

| Zhaoetal. |     |     |     |     |     |     |     |     |     |     |     | 10.3389/frai.2026.1829649 |     |     |
| --------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------------------- | --- | --- |
FIGURE1
OverviewofthearchitectureofDynEC.(A)Multi-viewdynamicgraphconstruction:fusinggeometric,temporal,andstatisticaldependencies.(B)
Gatedspatio-temporalgraphencoder:updatingnodeembeddingsviaMulti-HeadGATandGRU.(C)Dual-objectiveclustering:optimizingforboth
clusterpurity(KLdivergencetotarget)andtemporalconsistency.
|     | This | metric facilitates | the | identification |     | of users | with |     |     |     |     |     |     |     |
| --- | ---- | ------------------ | --- | -------------- | --- | -------- | ---- | --- | --- | --- | --- | --- | --- | --- |
X(t),
|               |     |                  |      |        |          |                |     | Require: | Load profiles |        | Neighbors |     | k, Window | w,  |
| ------------- | --- | ---------------- | ---- | ------ | -------- | -------------- | --- | -------- | ------------- | ------ | --------- | --- | --------- | --- |
| statistically |     | similar behavior | even | in the | presence | of substantial |     |          |               |        |           |     |           |     |
|               |     |                  |      |        |          |                |     | Kernel   | σ, Weights    | α,β,γ. |           |     |           |     |
discrepanciesintherawtimedomain.Thecorrespondingadjacency
A(t).
matrix Acorr therefore captures linear statistical dependency, Ensure: Fused Adjacency Matrix
|     |     |     |     |     |     |     |     | 1: Geometric | View | Construction: |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------ | ---- | ------------- | --- | --- | --- | --- |
enrichingthegraphwithinformationcomplementarytogeometric
|     |     |     |     |     |     |     |     | 2: Compute | pairwise | Euclidean | distances |     | Dgeo; |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------- | -------- | --------- | --------- | --- | ----- | --- |
proximityandtemporalalignment.
A( t )
|     |     |     |     |     |     |     |     | 3: Construct | kNN | graph | ge o based |     | on Dgeo with | k   |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------ | --- | ----- | ---------- | --- | ------------ | --- |
neighbors;
3.3.5 Graphfusion:integrationofheterogeneous 4: Temporal Alignment View Construction:
| views |     |     |     |     |     |     |     | 5: Compute | pairwise | cDTW | distances | Ddtw | with window | w   |
| ----- | --- | --- | --- | --- | --- | --- | --- | ---------- | -------- | ---- | --------- | ---- | ----------- | --- |
|       |     |     |     |     |     |     |     | (Equation  | 5);      |      |           |      |             |     |
|       |     |     |     |     |     |     |     |            |          |      | =exp(−D2  |      | /σ2);       |     |
The three views generate distinct adjacency matrices A( t ) , 6: Convert to similarity Sdtw
|     |     |     |     |     |     |     | g e o |     |     |     |     |     | dtw |     |
| --- | --- | --- | --- | --- | --- | --- | ----- | --- | --- | --- | --- | --- | --- | --- |
A( t ) A( t ) 7 : S p a r s i f y S t o o b t a i n A ( t ) ;
, and . To enable the Graph Neural Network to learn dt w d t w
| d   | t w | c o rr |     |     |     |     |     |     |     |     |     |     |     |     |
| --- | --- | ------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
fromtheseheterogeneoussources,weemploya“weightedfusion 8 : D e p e n d e nc y V ie w C o n s t r uc t i o n:
|     |     |     |     |     |     |     |     |            |                     |     |     |     |        | A( t ) |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------- | ------------------- | --- | --- | --- | ------ | ------ |
|     |     |     |     |     |     |     |     | 9: Compute | Pearson-correlation |     |     |     | matrix |        |
and normalization” strategy to synthesize a unified adjacency co r r
|     |     |     |     |     |     |     |     | (Equation | 6); |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --------- | --- | --- | --- | --- | --- | --- |
matrixA(t).
|     |     |     |     |     |     |     |     | 10: Fusion | and Normalization: |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------- | ------------------ | --- | --- | --- | --- | --- |
First,theviewsareintegratedviaaweightedlinearcombination
|                     |            |                     |               |            |              |            |     | 11: A( t )    | ←αA( t )+βA(                        | t )+γA( | t ) ;      |     |     |     |
| ------------------- | ---------- | ------------------- | ------------- | ---------- | ------------ | ---------- | --- | ------------- | ----------------------------------- | ------- | ---------- | --- | --- | --- |
| asshowninEquation9: |            |                     |               |            |              |            |     | fu s ed       | ge o                                | dt w    | co r r     |     |     |     |
|                     |            |                     |               |            |              |            |     |               | A(t)←D−1                            | 2(A(    | t ) +I)D−1 |     |     |     |
|                     |            |                     |               |            |              |            |     | 12: Normalize |                                     |         | fu s ed    | 2;  |     |     |
|                     |            | A( t) =αA(          | t ) +βA(      | t ) +γA(   | t )          |            |     |               |                                     |         |            |     |     |     |
|                     |            |                     |               |            | ,            |            | (9) | 13: return    | A(t)                                |         |            |     |     |     |
|                     |            | fu sed              | g e o         | d t w      | c o rr       |            |     |               |                                     |         |            |     |     |     |
|                     | α,β,γ      |                     |               |            | α            | + β +      | γ = |               |                                     |         |            |     |     |     |
| where               |            | are hyperparameters |               | satisfying |              |            |     |               |                                     |         |            |     |     |     |
|                     |            |                     |               |            |              |            |     | Algorithm1.   | Multi-viewdynamicgraphconstruction. |         |            |     |     |     |
| 1,                  | regulating | the relative        | contributions |            | of geometric | proximity, |     |               |                                     |         |            |     |     |     |
temporalalignment,andstatisticaldependency.
Subsequently,symmetricnormalizationisappliedtothefused 3.4 Deep evolutionary graph learning
| adjacencymatrixA(t) |     | asshowninEquation10: |           |      |     |     |      |           |     |     |     |     |     |     |
| ------------------- | --- | -------------------- | --------- | ---- | --- | --- | ---- | --------- | --- | --- | --- | --- | --- | --- |
|                     |     | fused                |           |      |     |     |      | framework |     |     |     |     |     |     |
|                     |     | A(t)=D               | −1 2(A(t) | +I)D | −1  |     |      |           |     |     |     |     |     |     |
|                     |     |                      |           |      | 2,  |     | (10) |           |     |     |     |     |     |     |
fused The core of DynEC is a unified self-supervised learning
where I is the identity matrix representing self-loops, and D is framework that seamlessly integrates a Gated Spatio-Temporal
|     |     | A(t) | +   |     |     |     |     |     |     |     |     |     |     |     |
| --- | --- | ---- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
the degree matrix of I. This normalization is essential GraphEncoderwithaDual-ObjectiveOptimizationMechanism.
fused
formitigatingthebiasintroducedbyunevendegreedistributions
duringgraphconvolution.
The resulting unified adjacency matrix A(t) simultaneously 3.4.1 Gatedspatio-temporalgraphencoder
| encodes | local | Euclidean | proximity | (Geometric |     | View), | shape |     |     |     |     |     |     |     |
| ------- | ----- | --------- | --------- | ---------- | --- | ------ | ----- | --- | --- | --- | --- | --- | --- | --- |
similarity invariant to temporal shifts (Temporal Alignment The Gated Spatio-Temporal Graph Neural Network (GST-
View), and linear statistical dependency (Correlation View). This GNN) is designed to learn node embeddings that capture
A(t)
multi-view dynamic graph provides a comprehensive and robust both the structural patterns from the multi-view graph
structural foundation for subsequent spatio-temporal learning in and the temporal evolution of user behaviors from the feature
X(t).
theGST-GNN. stream Unlike traditional ST-GNNs, which primarily focus
The detailed procedure for multi-view dynamic graph on supervised forecasting tasks (Wuetal., 2019), our encoder
constructionissummarizedinAlgorithm1. is specifically tailored for unsupervised evolutionary clustering,
| FrontiersinArtificialIntelligence |     |     |     |     |     |     |     | 06  |     |     |     |     | frontiersin.org |     |
| --------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --------------- | --- |

| Zhaoetal. |     |     |     |     |     |     |     |     |     |     |     | 10.3389/frai.2026.1829649 |     |     |
| --------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------------------- | --- | --- |
μ
effectively connecting static structural learning with dynamic the cluster centroid . In this study, we propose using the
k
pattern evolution. The “Gated” nature of this architecture is Student’st-distributionkernelinsteadoftheconventionalGaussian
twofold:itemploysanattention-basedsoftgatingmechanismfor kernelusedinGaussianMixtureModels.Thischoiceismotivated
spatialaggregationandagatedrecurrentunitfortemporalupdates. by the heavy-tailed property of the t-distribution, which makes
|     |     |     |     |     |     |     | the clustering |     | more robust | to  | outliers. | This | is a critical | feature |
| --- | --- | --- | --- | --- | --- | --- | -------------- | --- | ----------- | --- | --------- | ---- | ------------- | ------- |
3.4.1.1 Spatialaggregation(multi-headGAT) whendealingwithvolatileelectricityloaddata,wherespikesand
To capture the manifold relationship patterns present in the anomaliesarecommon.Thesoftassignmentiscomputedasfollows
| multi-viewgraph,aMulti-HeadGraphAttentionNetwork(GAT) |                                      |     |     |     |     |     | Equation14: |     |     |     |     |     |     |     |
| ----------------------------------------------------- | ------------------------------------ | --- | --- | --- | --- | --- | ----------- | --- | --- | --- | --- | --- | --- | --- |
| isemployed.Leth(t)                                    | denotethefeaturevectorofnodeiattimet |     |     |     |     |     |             |     |     |     |     |     |     |     |
i
(whereinitiallyh( t) =x (t)).Foreachattentionheadk,theattention (1+(cid:5)zi −μ (cid:5)2/ν) −ν+ 1
|     |     |     |     |     |     |     |     |     | =            |     | k   |     | 2   |      |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------ | --- | --- | --- | --- | ---- |
|     | i i |     |     |     |     |     |     |     | q ik (cid:4) |     |     |     |     | (14) |
coefficiente betweennodeianditsneighborj ∈ N i(definedby k(cid:9)(1+(cid:5)zi −μ (cid:5)2/ν) −ν+ 1
|     | ij,k |     |     |     |     |     |     |     |     |     |     | k(cid:9) | 2   |     |
| --- | ---- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | -------- | --- | --- |
A(t))iscalculatedasfollowsEquation11:
ν
|     |     |     |     |     |     |     | where | represents | the | degrees | of freedom, |     | which | is set to 1 |
| --- | --- | --- | --- | --- | --- | --- | ----- | ---------- | --- | ------- | ----------- | --- | ----- | ----------- |
e =LeakyReLU(a(cid:8)T [W h( t)(cid:5)W h( t)]) (11) in this instance, reducing the equation to a Cauchy distribution.
|     | ij,k |     | k k i | k j |     |     |      |             |         |     |      |          |         |           |
| --- | ---- | --- | ----- | --- | --- | --- | ---- | ----------- | ------- | --- | ---- | -------- | ------- | --------- |
|     |      |     |       |     |     |     | This | formulation | enables | a   | more | flexible | cluster | boundary, |
denotesthelearnableweightmatrix,a(cid:8)
whereW k k istheattention accommodating the inherent noise in smart meter data without
(cid:5)
vector for the k-th head, and represents the concatenation excessivelypenalizingdistantpoints.
| operation. | The attention | weights, | denoted | by α | , are obtained |     |     |     |     |     |     |     |     |     |
| ---------- | ------------- | -------- | ------- | ---- | -------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
ij,k
throughsoftmaxnormalizationasshowninEquation12: 3.4.2.2 Self-trainingtargetdistribution
|     |     |     |     |     |     |     | To  | overcome | the lack | of ground | truth | labels | in  | unsupervised |
| --- | --- | --- | --- | --- | --- | --- | --- | -------- | -------- | --------- | ----- | ------ | --- | ------------ |
exp(e ij,k )
α = (cid:4) (12) settings,weemployaself-trainingstrategy.Thetargetdistribution,
|     | ij,k |     | exp(e | )   |     |     |     |     |     |     |     |     |     |     |
| --- | ---- | --- | ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
l∈N il,k definedhereinasP,isusedto“sharpen”thesoftassignments,Q,to
i
encouragehigh-confidencepredictions.Thetargetprobabilitypis
Theseweightsfunctionasa“softgating”mechanism,filtering
derivedfromqbyraisingittothesecondpowerandnormalizing
outnoisyconnectionsbyassigninglowerimportancetoirrelevant
|            |                   |           |     | h(t)   |             |     | byclusterfrequencyasshowninEquation15: |     |     |     |     |     |     |     |
| ---------- | ----------------- | --------- | --- | ------ | ----------- | --- | -------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
| neighbors. | The final spatial | embedding |     | i,spat | is obtained | by  |                                        |     |     |     |     |     |     |     |
concatenatingtheoutputsoftheKheadsasshowninEquation13:
q2/f
|     |     | ⎛        |         | ⎞   |     |     |     |     |     | p = | (cid:4) ik k |          |     | (15) |
| --- | --- | -------- | ------- | --- | --- | --- | --- | --- | --- | --- | ------------ | -------- | --- | ---- |
|     |     |          |         |     |     |     |     |     |     | ik  | k(cid:9)q2   | /f       |     |      |
|     |     | K(cid:5) | (cid:2) |     |     |     |     |     |     |     | ik(cid:9)    | k(cid:9) |     |      |
(cid:5)
|     | h(t) = | (cid:5) σ⎝ | α W   | h(t)⎠ |     | (13) |              |     | (cid:4)  |        |              |            |                 |            |
| --- | ------ | ---------- | ----- | ----- | --- | ---- | ------------ | --- | -------- | ------ | ------------ | ---------- | --------------- | ---------- |
|     | i,spat |            | ij,k  | k j   |     |      |              |     |          |        |              |            |                 |            |
|     |        |            |       |       |     |      | where        | f = | q        | is the | soft cluster | frequency. |                 | The target |
|     | k=1    |            | j∈N i |       |     |      |              | k   | i ik     |        |              |            |                 |            |
|     |        |            |       |       |     |      | distribution | is  | designed | to     | satisfy      | three      | key properties: | (1)        |
whereσ
isanon-linearactivationfunction(e.g.,ELU). Sharpening: By squaring the probabilities, the distribution is
pushedtowardaone-hotencoding,reducingentropyandforcing
3.4.1.2 Temporalevolution(GRUupdate)
|     |     |     |     |     |     |     | the model | to  | make decisive | cluster | assignments. |     | (2) | Confidence |
| --- | --- | --- | --- | --- | --- | --- | --------- | --- | ------------- | ------- | ------------ | --- | --- | ---------- |
To capture user profile dynamics and handle concept drift, Emphasis: Data points that initially demonstrate high confidence
| a Gated | Recurrent Unit | (GRU) | is utilized | to update | the | node |            |      |        |           |         |     |          |          |
| ------- | -------------- | ----- | ----------- | --------- | --- | ---- | ---------- | ---- | ------ | --------- | ------- | --- | -------- | -------- |
|         |                |       |             |           |     |      | contribute | more | to the | gradient, | guiding | the | learning | process. |
embeddings. The GRU efficiently tracks temporal embeddings, (3) Normalization: Division by f prevents large clusters from
k
providing a robust mechanism to update user representations dominatingthelossfunction,ensuringthatsmallerbutdistinctuser
underconceptdrift.TheGRUprocessesthecurrentspatialfeature groups(e.g.,EVowners)arenotignored.
h(t) (outputfromGAT)andtheprevioususerembeddingz(t−1)
| i,spat |     |     |     |     |     | i   |     |     |     |     |     |     |     |     |
| ------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
asinputtoyieldthefinaltemporalembeddingz(t).Theresetgate
|     |     |     |     |     |     |     | 3.4.2.3 | Dual-objectivelossfunction |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ------- | -------------------------- | --- | --- | --- | --- | --- | --- |
i
withintheGRUdeterminestheextenttowhichpastinformation The learning objective is divided into two competing
components:clusteringqualitylossandtemporalsmoothnessloss
shouldbedisregarded,aprocessessentialforadaptingtoconcept
drift.Meanwhile,theupdategatecontrolstheincorporationofnew asshowninEquation16.
| spatial information. | This | mechanism | enables | the | model to | retain |     |     |     |     |     |     |     |      |
| -------------------- | ---- | --------- | ------- | --- | -------- | ------ | --- | --- | --- | --- | --- | --- | --- | ---- |
|                      |      |           |         |     |          |        |     |     |     | L=L | +λL |     |     | (16) |
along-termmemoryofuseridentitywhileadaptingtoshort-term clus temp
fluctuations.
|     |     |     |     |     |     |     | 1.  | Snapshot | clustering | loss | (L  | ): This | term minimizes | the |
| --- | --- | --- | --- | --- | --- | --- | --- | -------- | ---------- | ---- | --- | ------- | -------------- | --- |
clus
Kullback-Leibler(KL)divergencebetweenthesoftassignmentQ(t)
andthetargetdistributionP(t)atthecurrenttimestepasshownin
3.4.2 Dual-objectiveevolutionaryoptimization
Equation17.
Thefundamentalprincipleofourframeworkisunsupervised
|             |             |               |             |     |           |     |     |      |                       |     | (cid:2)(cid:2) |         | p(   | t)   |
| ----------- | ----------- | ------------- | ----------- | --- | --------- | --- | --- | ---- | --------------------- | --- | -------------- | ------- | ---- | ---- |
| clustering. | We employ a | self-training | methodology |     | utilizing | a   |     |      |                       |     |                |         |      |      |
|             |             |               |             |     |           |     |     | L    | =KL(P(t)(cid:5)Q(t))= |     |                | p(t)log | ik   | (17) |
|             |             |               |             |     |           |     |     | clus |                       |     |                | ik      | q(t) |      |
Student’st-distributionkernel.
|     |     |     |     |     |     |     |     |     |     |     | i   | k   | ik  |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
3.4.2.1 Softassignment(student’st-distribution)
Byminimizingthisdivergence,themodelisforcedtoiteratively
The probability of user i belonging to cluster k, denoted refine its cluster assignments, moving the centroids toward the
q , is measured by the similarity between its embedding zi and high-densitycentersoftheembeddings.
ik
| FrontiersinArtificialIntelligence |     |     |     |     |     | 07  |     |     |     |     |     |     |     | frontiersin.org |
| --------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --------------- |

Zhaoetal. 10.3389/frai.2026.1829649
2. Temporal consistency loss (L temp): To prevent erratic
Require: Continuous load profile stream X =
“Identity Switching,” we introduce a temporal smoothness
{X(1),...,X(T)}, Number of clusters K, Hyperparameters
constraint. This term penalizes abrupt deviations of the current
cluster assignment Q(t) from the previous assignment Q(t−1) as
λ,α,β,γ.
Ensure: Cluster assignments C = {C(1),...,C(T)} for all
showninEquation18.
users.
L temp =KL(Q(t−1)(cid:5)Q(t))= (cid:2) i (cid:2) k q( ik t−1)log q q ( ik t ( i − k t) 1) (18) 1: r μ I e n (0 c i ) o t n i v s a i t l a r i u z K c a - t t M i i e o o a n n n : s l P o o r s n e s - ; t t h r e I a n i i i n n t i i t t a h i l e a i G l z S e T e - m c G b l N e u N d s d t e i e n n r c g o s c d e e Z n r ( t 0) r u . o s i i d n s g
2: for t=1 to T do
This regularization encourages the model to preserve a user’s 3: Multi-View Graph Construction: Compute
clustermembershipunlessstrongevidencefromnewdatadictates adjacency matrices A(t),A(t),A(t) .
a change. The hyperparameter λ controls the trade-off between 4: Fuse and normalize g i e n o to dt a w un c i or f r ied graph A(t)
fitting the current snapshot (Plasticity) and respecting historical (Equation 7).
consistency(Stability). 5: Spatio-Temporal Embedding Update:
6: Extract spatial features: H(t)←GAT(A(t),X(t)).
3.4.3 Overalltrainingprocess 7: Update temporal states: Z(t)←GRU(H(t),Z(t−1)).
To provide a clear roadmap of the proposed methodology,
8: Clustering & Dual-Objective Optimization:
the complete execution pipeline of the evolutionary clustering 9: Compute soft assignments Q(t) using
frameworkissummarizedinAlgorithm2.Theprocedureoperates
Eq. Equation 11.
inanonlinemanneracrosscontinuoustimesteps.Itbeginswith
10: Calculate the auxiliary target distribution
a pre-training phase to establish robust initial representations P(t) using Eq. Equation 12.
and cluster centroids. Subsequently, at each time step t, the 11: Calculate clustering loss L clus and temporal
framework sequentially performs multi-view graph construction, consistency loss L temp.
spatio-temporalembeddingupdatesviatheGST-GNN,anddual- 12: Update network parameters θ and cluster
objective optimization. This iterative process ensures that the centroids μ by minimizing L=L clus +λL temp.
model dynamically adapts to emerging concept drifts while
13: Cluster Assignment: Assign each user i to
preservingthestructuralcontinuityofuserprofiles. cluster c(
i
t)←argmaxkq(
ik
t).
14: end for
15: return C.
4 Experiments
Algorithm2. Evolutionaryclusteringtrainingprocess.
4.1 Experimental setup
4.1.1 Datasets interpolation.Toscaleeachuser’sdailyprofiletotheinterval[0,1],
weappliedmin-maxnormalization.Thisensuresthattheclustering
To evaluate the performance of DynEC, we utilized three processfocusesonshapepatternsratherthanabsolutemagnitudes.
real-world smart meter datasets collected from distinct cities in
Sichuan Province, China, covering the entire year of 2024. City
4.1.1.2 Baselineinformation
A(MixedResidential/Commercial)comprises800users,including
To assess DynEC, we employed a comprehensive suite of
a significant proportion of early adopters of Distributed Energy
baselines, comprising both static and dynamic methods. Evol-
Resources(DERs)andElectricVehicles(EVs).Thisdatasetexhibits
KMeansdenotesourimplementationoftheevolutionaryK-Means
high volatility and frequent pattern shifts. City B (Residential-
approach proposed by Chakrabartietal. (2006), instantiated via
Dominant) consists of 500 users who display regular weekly
centroid smoothing across consecutive monthly snapshots. The
patterns,althoughthesepatternsaresubjecttosignificantseasonal
specificdescriptionsofthesebaselinesareshowninTable2.
fluctuations. City C (Industrial Park Zone) contains 650 users
fromaspecializedindustrialenvironment,servingasaproxyfor
a fully integrated Source-Grid-Load-Storage system characterized
bydiverseinteractionpatternsanddistinctconceptdrifts. 4.2 Implementation details
4.1.1.1 Pre-processing 4.2.1 Fusionweightstrategy
The raw AMI data were sampled at 15-min intervals and
subsequently aggregated into hourly load profiles (D = 24). To While the conceptual framework allows for dynamically
simulate a realistic dynamic environment, we employed a sliding updatedfusionweights,ourpracticalengineeringimplementation
windowapproachwithasequencelengthof24handastepsizeof utilizes fixed, equal weights (α = β = γ = 1/3). This
1h.Missingvalues(approximately0.5%)wereimputedusinglinear choiceprevents“viewcollapse”duringtrainingandensuresrobust
FrontiersinArtificialIntelligence 08 frontiersin.org

| Zhaoetal. |     |     |     |     |     |     |     |     |     |     | 10.3389/frai.2026.1829649 |     |
| --------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------------------- | --- |
TABLE2Summaryofbaselinemethods. TABLE3Detailedimplementationspecificationsandhyperparameterconfiguration.
| Category        |     | Method  | Description                       |     |     |     | Parameter         |     | Value/specification |     |     |     |
| --------------- | --- | ------- | --------------------------------- | --- | --- | --- | ----------------- | --- | ------------------- | --- | --- | --- |
| Staticbaselines |     | K-Means | Standardbaselineforloadprofiling; |     |     |     | Modelarchitecture |     |                     |     |     |     |
actsasareferenceforsnapshot
|     |     |     |     |     |     |     | Implementationframework |     | PyTorchgeometric(PyG) |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ----------------------- | --- | --------------------- | --- | --- | --- |
qualitybutsuffersfromhigh
|     |     |     |     |     |     |     | Graphencoder |     | 2-layerGated-GAT(Hiddendimensions: |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ------------ | --- | ---------------------------------- | --- | --- | --- |
instability.
64→32)
|     |     | Spectral   | ClustersviaLaplacian        |     |     |     |                |     |                         |     |     |     |
| --- | --- | ---------- | --------------------------- | --- | --- | --- | -------------- | --- | ----------------------- | --- | --- | --- |
|     |     |            |                             |     |     |     | Temporalmodule |     | GRU(Hiddendimension:32) |     |     |     |
|     |     | Clustering | eigendecomposition(Luxburg, |     |     |     |                |     |                         |     |     |     |
Multi-headAttention(K=4heads)
Attentionmechanism
2007);itiscomputationally
expensiveandlackstemporal Clusteringkernel Student’st-distribution(Degreesoffreedom
ν=1)
consistency.
Hyperparameters
| Dynamic/evolutionary |     | Time2Graph | Shapelet-basedtemporal |     |     |     |     |     |     |     |     |     |
| -------------------- | --- | ---------- | ---------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
baselines representationmodeladaptedfor Temporalconsistency(λ) 0.1(Selectedviagridsearch)
|     |     |     | clusteringusingK-Means,following |     |     |     | Fusionweights(α,β,γ) |     | Fixedat1/3(EqualWeighting) |     |     |     |
| --- | --- | --- | -------------------------------- | --- | --- | --- | -------------------- | --- | -------------------------- | --- | --- | --- |
thedynamicshapeletframeworkof
|     |     |     |     |     |     |     | cDTWbandwidth |     | 2(equivalentto±2hourstemporalshift) |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ------------- | --- | ----------------------------------- | --- | --- | --- |
Chengetal.(2020).
Adamoptimizer(learningrateη=10−3,Weight
Optimization
|     |     | EvolveGCN- | AdaptationofEvolveGCN |     |     |     |     |     |     |     |     |     |
| --- | --- | ---------- | --------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
decay10−4)
|     |     | Clus | (Parejaetal.,2020)evolvingGCN |     |     |     |     |     |     |     |     |     |
| --- | --- | ---- | ----------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Training&hardware
parametersviaRNN,modifiedfor
|     |     |     |     |     |     |     | Pre-trainingstrategy |     | 50epochs(MSEreconstructionloss) |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | -------------------- | --- | ------------------------------- | --- | --- | --- |
unsupervisedclustering.
|     |     |        |                                  |     |     |     | Clusteringstrategy |     | 100epochs(KLdivergenceloss) |     |     |     |
| --- | --- | ------ | -------------------------------- | --- | --- | --- | ------------------ | --- | --------------------------- | --- | --- | --- |
|     |     | Evol-  | EvolutionaryK-Meansbaselinewith  |     |     |     |                    |     |                             |     |     |     |
|     |     | KMeans | explicitcentroidsmoothingbetween |     |     |     | Batchsize          |     | 256users                    |     |     |     |
consecutivemonthlysnapshots; Computingresources NVIDIARTX3090GPU(24GBVRAM),64GB
designedtoreduceswitchingbut
RAM
pronetounder-adaptationwhen
heterogeneousdriftoccurs.
|             |        |           |           |             |     |             | 4.3.1 Snapshotqualitymetrics |     |     |     |     |     |
| ----------- | ------ | --------- | --------- | ----------- | --- | ----------- | ---------------------------- | --- | --- | --- | --- | --- |
| performance | across | different | datasets. | Sensitivity | to  | this design |                              |     |     |     |     |     |
choiceisanalyzedinSection4.6. These metrics evaluate the degree to which the clustering
The DynEC framework was implemented in PyTorch structurecorrespondstothedataatagiventimet.TheSilhouette
Geometric.ThespecificparametersettingsarelistedinTable3. Coefficient (SC), developed by Rousseeuw (1987), is used to
|     |     |     |     |     |     |     | measure | the contrast | between | intra-cluster | cohesion | and inter- |
| --- | --- | --- | --- | --- | --- | --- | ------- | ------------ | ------- | ------------- | -------- | ---------- |
4.2.1.1 Hyperparameters cluster separation. Additionally, the Davies-Bouldin Index (DBI)
Thetemporalconsistencyweightλwassetto0.1,determined isemployedtoevaluatetheaveragesimilarityofeachclusterwith
through a grid search on the validation set. For the graph fusion itsmostsimilarneighbor.Whengroundtruthlabelsareavailable,
1/3 α, β, γ the Adjusted Rand Index (ARI) is also reported to quantify
| weights, | fixed equal | values | of  | were used | for | and |               |         |           |            |     |               |
| -------- | ----------- | ------ | --- | --------- | --- | --- | ------------- | ------- | --------- | ---------- | --- | ------------- |
|          |             |        |     |           |     |     | the agreement | between | predicted | partitions | and | the reference |
throughouttraining.ForthecDTWcalculation,theSakoe–Chiba
|     |     |     |     |     |     |     | clustering. | In this study, | ARI | was computed |     | against the pre- |
| --- | --- | --- | --- | --- | --- | --- | ----------- | -------------- | --- | ------------ | --- | ---------------- |
bandwidthwassetto2,allowingforatemporalshiftofupto2h.
|     |     |     |     |     |     | −3anda | definedbase_clusterlabelsinusers.csv.Thesereference |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | ------ | --------------------------------------------------- | --- | --- | --- | --- | --- |
WeutilizedtheAdamoptimizerwithalearningrateof10
weightdecayof10 −4. labels were maintained in the utility’s operational system and
werecross-checkedagainstcustomer-typerecords(e.g.,residential
|     |     |     |     |     |     |     | and commercial | categories). | To  | improve | label reliability, | domain |
| --- | --- | --- | --- | --- | --- | --- | -------------- | ------------ | --- | ------- | ------------------ | ------ |
4.2.1.2 Trainingstrategy
|                  |         |            |                 |          |               |           | experts from   | the State         | Grid Sichuan | Electric     | Power         | Corporation     |
| ---------------- | ------- | ---------- | --------------- | -------- | ------------- | --------- | -------------- | ----------------- | ------------ | ------------ | ------------- | --------------- |
| The              | GST-GNN | encoder    | was pre-trained | for      | 50 epochs     | using     |                |                   |              |              |               |                 |
|                  |         |            |                 |          |               |           | randomly       | sampled 10%       | of users     | and verified | the           | authenticity of |
| Mean Squared     | Error   | (MSE)      | reconstruction  | loss     | to initialize |           | the            |                   |              |              |               |                 |
|                  |         |            |                 |          |               |           | their assigned | user types        | against      | field-visit  | records       | before model    |
| node embeddings. |         | Subsequent | clustering      | training | was           | conducted |                |                   |              |              |               |                 |
|                  |         |            |                 |          |               |           | development.   | The de-identified |              | dataset      | and reference | labels are      |
inmini-batchesof256usersateachtimestepfor100epochs.All
publiclyavailableinaGitHubrepository.
experimentswereperformedonaserverequippedwithanNVIDIA
RTX3090GPUand64GBofRAM.
|     |     |     |     |     |     |     | 4.3.2 Temporalstabilitymetrics |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ------------------------------ | --- | --- | --- | --- | --- |
4.3 Evaluation metrics Inadditiontostaticquality,assessingthetemporalconsistency
ofclusterassignmentsiscrucialfordynamicprofiling.TheCluster
To evaluate the trade-off between clustering quality and Switching Rate (CSR) is used to measure the stability of user
temporalstability,weadoptedadual-metricevaluationsystem. allocationovertime. CSRisdefinedastheaverage proportionof
| FrontiersinArtificialIntelligence |     |     |     |     |     |     | 09  |     |     |     |     | frontiersin.org |
| --------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --------------- |

| Zhaoetal. |     |     |     |     |     |     |     |     |     |     | 10.3389/frai.2026.1829649 |
| --------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------------------- |
userswhochangetheirclusteraffiliationbetweenconsecutivetime dna8020.0=p(AytiCnisnaeMK-lovEdnasnaeM-KrevoIRAsevorpmiyltnacfiingisdohtemdesoporpehttahtwohssdeesevfiehtrevostset-tderiaP.dlobnidethgilhgiherastlusertseB.snurtnednepedni5revonoitaiveDdradnatS±naeMsadetropereraseulaV
stepsasshowninEquation19:
|     |      |     |            |          |                |          |     |      |      | 90.0±87.0 50.0±97.0 40.0±65.0 30.0±87.0 | 00.0±10.0 10.0±30.0 |
| --- | ---- | --- | ---------- | -------- | -------------- | -------- | --- | ---- | ---- | --------------------------------------- | ------------------- |
|     |      |     |            | (cid:10) |                | (cid:11) |     |      | ↓RSC |                                         |                     |
|     |      |     | (cid:4)    |          |                | (t+1)    |     |      |      |                                         |                     |
|     |      |     | T(cid:2)−1 | N 1      | c (t)(cid:3)=c |          |     |      |      |                                         |                     |
|     |      | 1   |            | i=1      | i              | i        |     |      |      |                                         |                     |
|     | CSR= |     |            |          |                |          |     | (19) |      |                                         |                     |
T−1
|     |     |     | t=1 |     | N   |     |     |     |     |                                         |                     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --------------------------------------- | ------------------- |
|     |     |     |     |     |     |     |     |     |     | 00.0±97.0 60.0±11.1 40.0±69.0 03.0±73.3 | 00.0±48.0 70.0±69.0 |
)lairtsudni(CytiC ↓IBD
| where1(·)istheindicatorfunction,andc(t) |     |     |     |     | representsthecluster |     |     |     |     |     |     |
| --------------------------------------- | --- | --- | --- | --- | -------------------- | --- | --- | --- | --- | --- | --- |
i
| label of | user i at | time t. | A lower | CSR | indicates | higher | temporal |     |     |     |     |
| -------- | --------- | ------- | ------- | --- | --------- | ------ | -------- | --- | --- | --- | --- |
stability, meaning the model is robust to minor fluctuations and .)50.0>p(tnacfiingisyllacitsitatstoneraCytiCdnaBytiCnisenilesabdetneiro-tohspanstsegnortsehttsniagasecnereffidIRAehT.)3−01<p(seiticeerhtllanisnaeM-KotevitalerRSCsecuderyltnacfiingisdna)7010.0=p
cancaptureconsistentbehavioralpatterns.
|     |     |     |     |     |     |     |     |     |     | 00.0±54.0 20.0±72.0 10.0±04.0 00.0±81.0 | 00.0±64.0 20.0±83.0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --------------------------------------- | ------------------- |
↑CS
| 4.4 Comparative |     |     | analysis |     |     |     |     |     |     |                                         |                     |
| --------------- | --- | --- | -------- | --- | --- | --- | --- | --- | --- | --------------------------------------- | ------------------- |
|                 |     |     |          |     |     |     |     |     |     | 00.0±65.0 10.0±74.0 70.0±26.0 10.0±32.0 | 00.0±56.0 60.0±56.0 |
↑IRA
| As shown                     |            | in Table4, | this         | study         | presents     | a comprehensive |              |     |      |                                         |                     |
| ---------------------------- | ---------- | ---------- | ------------ | ------------- | ------------ | --------------- | ------------ | --- | ---- | --------------------------------------- | ------------------- |
| performance                  | comparison |            | with         | five baseline | models       |                 | across three |     |      |                                         |                     |
| cities. The                  | results    | indicate   | that         | the           | framework    |                 | proposed     | in  |      |                                         |                     |
| this study                   | achieves   | certain    | improvements |               | in balancing |                 | clustering   |     |      |                                         |                     |
|                              |            |            |              |               |              |                 |              |     |      | 01.0±07.0 40.0±48.0 01.0±92.0 50.0±07.0 | 00.0±00.0 20.0±20.0 |
| qualityandtemporalstability. |            |            |              |               |              |                 |              |     | ↓RSC |                                         |                     |
4.4.1 Clusteringquality(ARI&SC)
|     |     |     |     |     |     |     |     |     | )laitnediser(BytiC | 00.0±65.0 90.0±62.1 10.0±95.0 11.0±47.1 | 00.0±94.0 90.0±26.0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------------ | --------------------------------------- | ------------------- |
↓IBD
| In City        | A (mixed    | type),          | which         | exhibits         | the        | highest    | volatility, |      |     |                                         |                     |
| -------------- | ----------- | --------------- | ------------- | ---------------- | ---------- | ---------- | ----------- | ---- | --- | --------------------------------------- | ------------------- |
| the ARI        | (0.56       | ± 0.06)         | of our        | DynEC            | method     |            | outperforms |      |     |                                         |                     |
| all other      | approaches, |                 | including     | spectral         |            | clustering | (ARI        |      |     |                                         |                     |
| 0.51 ±         | 0.01) and   | the explicit    |               | time-regularized |            | baseline   | Evol-       |      |     |                                         |                     |
|                |             |                 |               |                  |            |            |             |      |     | 00.0±95.0 40.0±91.0 10.0±85.0 10.0±43.0 | 00.0±56.0 50.0±45.0 |
|                |             | ±               |               |                  |            |            |             |      | ↑CS |                                         |                     |
| KMeans         | (ARI        | 0.43            | 0.00).        | This             | indicates  | that       | DynEC       | is   |     |                                         |                     |
| highly capable |             | of identifying  |               | genuine          | behavioral |            | semantics   |      |     |                                         |                     |
| amid complex   |             | mixed patterns. |               | However,         | static     | methods    |             | like |     |                                         |                     |
| K-Means        | show        | stronger        | intra-cluster |                  | geometric  |            | compactness |      |     |                                         |                     |
|                |             |                 |               |                  |            |            |             |      |     | 00.0±19.0 40.0±15.0 20.0±09.0 30.0±84.0 | 00.0±29.0 60.0±58.0 |
(SC and DBI) on individual snapshots. This is an expected ↑IRA
| trade-off,          | as our    | evolutionary |             | learning | framework  |          | sacrifices    |     |     |                                         |                     |
| ------------------- | --------- | ------------ | ----------- | -------- | ---------- | -------- | ------------- | --- | --- | --------------------------------------- | ------------------- |
| minor instantaneous |           | spatial      | cohesion    |          | to achieve | a        | significantly |     |     |                                         |                     |
| lower Cluster       | Switching |              | Rate (CSR), | ensuring |            | temporal | semantic      |     |     |                                         |                     |
|                     |           |              |             |          |            |          |               |     |     | 40.0±08.0 60.0±97.0 40.0±16.0 30.0±77.0 | 00.0±10.0 20.0±40.0 |
consistency. In City B (residential), stability-oriented baseline ↓RSC
| models           | (such   | as Evol-KMeans) |       | achieved |      | exceptionally |            | high |     |     |     |
| ---------------- | ------- | --------------- | ----- | -------- | ---- | ------------- | ---------- | ---- | --- | --- | --- |
|                  |         |                 | ±     |          |      | ±             |            |      |     |     |     |
| snapshot         | quality | (ARI 0.92       | 0.00, | SC       | 0.65 | 0.00),        | indicating |      |     |     |     |
| that residential |         | patterns        | form  | distinct | and  | geometrically | well-      |      |     |     |     |
separated clusters on individual days. Although DynEC’s ARI 00.0±49.0 30.0±90.1 70.0±10.1 14.0±45.3 00.0±39.0 70.0±01.1
↓IBD
±
| (0.85             | 0.06)           | is slightly  | lower, | it remains   |             | highly          | competitive |     | )dexim(AytiC |     |     |
| ----------------- | --------------- | ------------ | ------ | ------------ | ----------- | --------------- | ----------- | --- | ------------ | --- | --- |
| while maintaining |                 | a consistent |        | evolutionary |             | representation. |             |     |              |     |     |
| In City           | C (industrial), |              | DynEC  | remains      | competitive |                 | compared    |     |              |     |     |
|                   |                 |              | ±      |              |             | ±               |             |     |              |     |     |
to Evol-KMeans (ARI 0.65 0.06 vs. 0.65 0.00) and 00.0±14.0 10.0±33.0 20.0±93.0 10.0±71.0 00.0±24.0 10.0±13.0
↑CS
| outperforms | the | state-of-the-art |     | EvolveGCN |     | (ARI | 0.65 ± | 0.06 |     |     |     |
| ----------- | --- | ---------------- | --- | --------- | --- | ---- | ------ | ---- | --- | --- | --- |
±
| vs. 0.62 | 0.07), | confirming |     | its robustness |     | across | different |     |     |     |     |
| -------- | ------ | ---------- | --- | -------------- | --- | ------ | --------- | --- | --- | --- | --- |
.stesatadeerhtnonosirapmocecnamrofreP4ELBAT
consumertypes.
|     |     |     |     |     |     |     |     |     |     | 00.0±64.0 10.0±15.0 30.0±44.0 10.0±81.0 | 00.0±34.0 60.0±65.0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --------------------------------------- | ------------------- |
↑IRA
4.4.1.1 Temporalstability(CSR)
| The             | proposed | method      | achieves           | CSR | values        | close | to    | zero |     |     |     |
| --------------- | -------- | ----------- | ------------------ | --- | ------------- | ----- | ----- | ---- | --- | --- | --- |
| (0.02–0.04)     | across   | all cities, | significantly      |     | lower         | than  | those | of   |     |     |     |
| static baseline |          | methods     | (K-Means/Spectral: |     | approximately |       | 0.70– |      |     |     |     |
sulC-NCGevlovE
0.79) and dynamic methods (EvolveGCN: approximately )sruO(CEnyD
|             |          |     |             |     |         |         |     |     |        | hparG2emiT | snaeMK-lovE |
| ----------- | -------- | --- | ----------- | --- | ------- | ------- | --- | --- | ------ | ---------- | ----------- |
| 0.29–0.61). | However, |     | Evol-KMeans |     | further | reduces |     | CSR | dohteM |            |             |
snaeM-K
lartcepS
| to 0.00–0.01                      |        | through           | explicit | centroid        | smoothing; |          | yet,      | its |     |     |                 |
| --------------------------------- | ------ | ----------------- | -------- | --------------- | ---------- | -------- | --------- | --- | --- | --- | --------------- |
| weaker                            | ARI on | the heterogeneous |          |                 | City A     | dataset  | indicates |     |     |     |                 |
| that temporal                     |        | smoothing         | alone    | is insufficient |            | to model | mixed     |     |     |     |                 |
| FrontiersinArtificialIntelligence |        |                   |          |                 |            |          |           | 10  |     |     | frontiersin.org |

| Zhaoetal. |     |     |     |     |     |     |     |     |     |     |     | 10.3389/frai.2026.1829649 |     |
| --------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------------------- | --- |
user drift. Although static methods such as K-Means may reduced stability (CSR increased from 0.02 to 0.05) and a slight
achieve high snapshot quality in stable environments (City decreaseinARI,confirmingthatstatisticalco-movementprovides
B), their high CSR indicates frequent “identity switching,” supplementary information and enhances the robustness of the
| where users | are           | reassigned | to different | clusters | daily due   | to  | clusteringprocess. |     |     |     |     |     |     |
| ----------- | ------------- | ---------- | ------------ | -------- | ----------- | --- | ------------------ | --- | --- | --- | --- | --- | --- |
| minor       | fluctuations. | Our        | evolutionary | learning | framework   |     |                    |     |     |     |     |     |     |
| effectively | smooths       | these      | transitions  | while    | maintaining |     |                    |     |     |     |     |     |     |
semantic consistency, which is crucial for real-world 4.5.2 Validationofdeepevolutionarygraph
| utilityapplications. |     |     |     |     |     |     | learningframework |     |     |     |     |     |     |
| -------------------- | --- | --- | --- | --- | --- | --- | ----------------- | --- | --- | --- | --- | --- | --- |
|                      |     |     |     |     |     |     |                   |     |     |     |     | λ   | =   |
4.4.1.2 Statisticalsignificance Setting the time-consistency weight to 0 (“no
Pairedt-testsoverthefiverandomseedsconfirmthatDynEC’s time consistency”) resulted in a significant deterioration of the
ARIimprovementinCityAisstatisticallysignificantrelativetoK-
|     |     |     |     |     |     |     | ARI (from | 0.62 | to 0.50), | although | the | CSR remained | at a |
| --- | --- | --- | --- | --- | --- | --- | --------- | ---- | --------- | -------- | --- | ------------ | ---- |
Means(p=0.0208)andEvol-KMeans(p=0.0107).Fortemporal
|     |     |     |     |     |     |     | low level. | This | indicates | that without | time | regularization, | the |
| --- | --- | --- | --- | --- | --- | --- | ---------- | ---- | --------- | ------------ | ---- | --------------- | --- |
stability,DynECachievessignificantlylowerCSRthanK-Meansin model cannot maintain a consistent semantic interpretation
< −3).
City A, City B, and City C (all p 10 By contrast, the ARI over time, even when cluster assignments do not fluctuate
differences between DynEC and the strongest snapshot-oriented rapidly. Furthermore, removing the gating mechanism (“no
| baselines | in City | B and | City C are not | statistically | significant |     |     |     |     |     |     |     |     |
| --------- | ------- | ----- | -------------- | ------------- | ----------- | --- | --- | --- | --- | --- | --- | --- | --- |
gating”)resultedinacomprehensivedeclineinperformance(ARI
>
(p 0.05), which is consistent with the limitation discussed in dropped to 0.51, CSR rose to 0.07), validating its role as a
Section4.8. learnable filter that selectively aggregates information-rich spatial
|     |     |     |     |     |     |     | neighbors | while | suppressing | noise, | thereby | balancing | plasticity |
| --- | --- | --- | --- | --- | --- | --- | --------- | ----- | ----------- | ------ | ------- | --------- | ---------- |
andstability.
| 4.5 Ablation |     | study |     |     |     |     |     |     |     |     |     |     |     |
| ------------ | --- | ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
To rigorously verify the contribution of the two core 4.6 Parameter sensitivity analysis
| innovations | of the    | proposed  | framework,  | a          | component-wise |     |          |     |          |              |     |            |           |
| ----------- | --------- | --------- | ----------- | ---------- | -------------- | --- | -------- | --- | -------- | ------------ | --- | ---------- | --------- |
| ablation    | study was | conducted | on the City | A dataset. | The results    |     |          |     |          |              |     |            |           |
|             |           |           |             |            |                |     | As shown | in  | Figure2, | the adjusted |     | Rand index | (ARI) and |
explicitlysupportthearchitecturaldesignchoices. cluster switching rate (CSR) are plotted as λ varies from 0 to
(λ <0.1),
|     |     |     |     |     |     |     | 1. In Mechanism |     | I   | the | model | lacks sufficient | time |
| --- | --- | --- | --- | --- | --- | --- | --------------- | --- | --- | --- | ----- | ---------------- | ---- |
≤
constraints,resultinginpoorclusterquality.MechanismII(0.1
4.5.1 Validationofmulti-viewdynamicgraph
|     |     |     |     |     |     |     | λ ≤ 0.3) | represents | the | “optimal | point,” | where ARI | peaks (at |
| --- | --- | --- | --- | --- | --- | --- | -------- | ---------- | --- | -------- | ------- | --------- | --------- |
construction λ=0.2)whileCSRdecreases,indicatingthatappropriatetemporal
regularizationeffectivelyfiltersoutnoiseandimprovesalignment
Regarding the removal of the time-aligned view (cDTW) (λ >0.5),
|             |     |         |                |          |             |     | with the  | true values. | In Mechanism      |     | III             | although   | CSR  |
| ----------- | --- | ------- | -------------- | -------- | ----------- | --- | --------- | ------------ | ----------------- | --- | --------------- | ---------- | ---- |
| (i.e., “w/o | DTW | View”), | this operation | resulted | in the most |     |           |              |                   |     |                 |            |      |
|             |     |         |                |          |             |     | decreases | further      | (high stability), |     | ARI fluctuates, | suggesting | that |
significant decline in clustering quality, with ARI dropping excessiveregularizationmayhinderthemodel’sabilitytoadaptto
sharply from 0.62 to 0.35. Therefore, geometric proximity alone trueconceptualdrift,therebyleadingto“lag.”Inadditiontoλ,the
| is insufficient | to characterize |           | complex | load patterns; | the cDTW        |     |                    |     |            |     |            |              |      |
| --------------- | --------------- | --------- | ------- | -------------- | --------------- | --- | ------------------ | --- | ---------- | --- | ---------- | ------------ | ---- |
|                 |                 |           |         |                |                 |     | model demonstrates |     | robustness | to  | the number | of neighbors | k in |
| view is         | crucial for     | capturing | shape   | similarity     | and identifying |     |                    |     |            |     |            |              |      |
graphconstructionandthewindowsizewincDTW,aslongasthey
| consistentuserbehaviorinthepresenceoftemporalmisalignment. |     |     |     |     |     |     |                                      |     |     |     | ∈   |                        |     |
| ---------------------------------------------------------- | --- | --- | --- | --- | --- | --- | ------------------------------------ | --- | --- | --- | --- | ---------------------- | --- |
|                                                            |     |     |     |     |     |     | capturesufficientlocalcontext(e.g.,k |     |     |     |     | [5,15]).Figure3further |     |
Similarly, removing the correlation view (Pearson) resulted in showsthatfixedequalfusionweights(α =β =γ =1/3)provide
FIGURE2
SensitivityanalysisoftemporalconsistencyweightλonCityA.An
FIGURE3
optimalbalanceisobservedaroundλ=0.2,whereclusterquality Sensitivityanalysisoffusionweights.Theequal-weightconfiguration
(highARI)ismaximizedwhilemaintainingtemporalstability(low (α=β=γ =1/3)achievesthebesttrade-off,maximizingARIwhile
| CSR).                             |     |     |     |     |     |     | keepingCSRnearzero. |     |     |     |     |     |                 |
| --------------------------------- | --- | --- | --- | --- | --- | --- | ------------------- | --- | --- | --- | --- | --- | --------------- |
| FrontiersinArtificialIntelligence |     |     |     |     |     | 11  |                     |     |     |     |     |     | frontiersin.org |

| Zhaoetal. |     |     |     |     |     |     |     |     |     | 10.3389/frai.2026.1829649 |     |     |
| --------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------------------- | --- | --- |
FIGURE4
Illustrationofrobustnesstophaseshifts.TraditionalEuclideandistancefailstomatchshape-similarbuttime-shiftedloadprofiles,whiletheproposed
cDTWviewcorrectlyalignstheseprofiles,ensuringtheyareclusteredtogetherdespitethetemporalmisalignment.(A)Euclideandistance:mismatch.
(B)cDTW:robustalignment.
4.7.2 Stabilityunderconceptdrift
|     |     |     |     |     |     | Figure5            | visualizes       | the           | evolution | of User           | #42     | from City A.   |
| --- | --- | --- | --- | --- | --- | ------------------ | ---------------- | ------------- | --------- | ----------------- | ------- | -------------- |
|     |     |     |     |     |     | This case          | exemplifies      | a typical     | scenario  | in the            | context | of Source-     |
|     |     |     |     |     |     | Grid-Load-Storage: |                  | a residential |           | user transforming |         | into an active |
|     |     |     |     |     |     | prosumer           | by participating |               | in a      | Vehicle-to-Grid   | (V2G)   | program        |
onDay15.Thisstructuralchange,characterizedbythetransition
frompassiveconsumptiontobi-directionalpowerflow,represents
| FIGURE5 |     |     |     |     |     | adistinctincrementalconceptdrift. |     |     |     |     |     |     |
| ------- | --- | --- | --- | --- | --- | --------------------------------- | --- | --- | --- | --- | --- | --- |
VisualizationofconceptdriftforUser#42.Top:Dailyloadprofiles
showingtheemergenceofV2Ginteractionpatterns.Bottom: As observed, the static K-Means algorithm, treating each day
Clusterassignmentprobabilitiesovertime.DynECexhibitsasmooth asanindependentsnapshot,reactedchaoticallytotheinitialload
transitioncomparedtotheerraticswitchingofK-Means. fluctuations induced by V2G discharging events. On Days 14–
16,theuser’slabelflickeredviolentlybetweenCluster1(Standard
|     |     |     |     |     |     | Residential) | and | Cluster | 3 (V2G | Prosumers). | This | phenomenon |
| --- | --- | --- | --- | --- | --- | ------------ | --- | ------- | ------ | ----------- | ---- | ---------- |
thebestbalancebetweensnapshotqualityandtemporalstability, illustrates the “Identity Switching” problem induced by the
|     |     |     |     |     |     | stochasticity | of  | source-load | interactions, | where | static | methods |
| --- | --- | --- | --- | --- | --- | ------------- | --- | ----------- | ------------- | ----- | ------ | ------- |
supportingtheengineeringchoiceadoptedinSection4.2.
|     |     |     |     |     |     | fail to distinguish |            | between | transient   | fluctuations |         | and genuine |
| --- | --- | --- | --- | --- | --- | ------------------- | ---------- | ------- | ----------- | ------------ | ------- | ----------- |
|     |     |     |     |     |     | behavioral          | evolution. | Such    | instability | would        | trigger | erroneous   |
billingadjustmentsinareal-worldutilitysystem.
| 4.7 Case | study: visualizing |     | model |     |     |          |           |       |            |     |          |             |
| -------- | ------------------ | --- | ----- | --- | --- | -------- | --------- | ----- | ---------- | --- | -------- | ----------- |
|          |                    |     |       |     |     | In sharp | contrast, | DynEC | maintained | a   | coherent | trajectory. |
effectiveness
FacilitatedbythetemporalconsistencylossandtheGRUmemory
mechanism,themodeleffectivelysuppressedimmediateresponses
| To intuitively | demonstrate | the | superiority | of the proposed |     |              |        |               |     |             |         |          |
| -------------- | ----------- | --- | ----------- | --------------- | --- | ------------ | ------ | ------------- | --- | ----------- | ------- | -------- |
|                |             |     |             |                 |     | to transient | noise. | It reassigned |     | the user to | the V2G | Prosumer |
framework,qualitativevisualizationscorrespondingtoitstwocore
|     |     |     |     |     |     | cluster only | after | the new | interaction | pattern |     | persisted and |
| --- | --- | --- | --- | --- | --- | ------------ | ----- | ------- | ----------- | ------- | --- | ------------- |
innovationsareprovided.
|     |     |     |     |     |     | stabilized | (post    | Day 16).  | This | “smooth transition” |          | capability |
| --- | --- | --- | --- | --- | --- | ---------- | -------- | --------- | ---- | ------------------- | -------- | ---------- |
|     |     |     |     |     |     | confirms   | that our | framework |      | successfully        | balances | plasticity |
(adaptingtothenewV2Gmode)withstability(ignoringtemporary
4.7.1 Robustnesstophaseshifts
|     |     |     |     |     |     | volatility), | validating | its | suitability | for automated |     | and noise- |
| --- | --- | --- | --- | --- | --- | ------------ | ---------- | --- | ----------- | ------------- | --- | ---------- |
tolerantloadprofiling.
| The Multi-View  | Dynamic                | Graph | Construction | is designed       | to  |     |     |     |     |     |     |     |
| --------------- | ---------------------- | ----- | ------------ | ----------------- | --- | --- | --- | --- | --- | --- | --- | --- |
| handle temporal | misalignments.         | In    | the analysis | of the mixed-     |     |     |     |     |     |     |     |     |
| type dataset,   | we identified numerous |       | instances    | of “shape-similar |     |     |     |     |     |     |     |     |
but time-shifted” users (e.g., households with evening peaks 4.8 Discussion and limitations
| occurring | at 18:00 vs. 20:00). | Methods | based | on traditional |     |     |     |     |     |     |     |     |
| --------- | -------------------- | ------- | ----- | -------------- | --- | --- | --- | --- | --- | --- | --- | --- |
Euclidean distance (e.g., K-Means) often assign these users to While our method demonstrates exceptional performance in
disparate clusters due to large point-wise distances. However, dynamic environments, we observe a slight performance trade-
by incorporating the cDTW view, the model successfully groups off in extremely stable settings. Specifically, in City B, where the
these users into the same functional cluster, confirming that the load patterns are highly consistent, static K-Means marginally
multi-viewfusionstrategyeffectivelycapturesinherentbehavioral outperforms DynEC in terms of ARI on a single snapshot. This
similarity beyond simple geometric alignment. As shown in occurs because static models can greedily fit the cross-sectional
Figure4,cDTWcorrectlyalignsshape-similarbuttime-shiftedload data without the “historical burden" of temporal smoothing.
profiles,whereasEuclideandistancetreatsthemasmismatcheddue This represents an inherent limitation of evolutionary clustering
topoint-wisetemporaloffsets. algorithms, where maintaining low CSR introduces a slight
| FrontiersinArtificialIntelligence |     |     |     |     | 12  |     |     |     |     |     |     | frontiersin.org |
| --------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --------------- |

| Zhaoetal. |     |     |     |     |     |     |     |     |     | 10.3389/frai.2026.1829649 |     |     |
| --------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------------------- | --- | --- |
FIGURE6
Event-drivenconceptdriftvalidationbasedontherealCity-Aeventlog.Top:numberofverifiedmonthlyeventsintheevaluated500-usersubset.
Middleandbottom:meanARIandCSRoverfiveseeds.Month5containsthehighesteventconcentration(32users),whereourapproachretains
higherclusteringqualitywhileadaptingmoreselectivelythanstaticK-MeansandlessconservativelythanEvolutionaryK-Means.
regularization penalty on snapshot-specific fit in purely static mitigatestheidentity-switchingbehaviorcausedbybi-directional
scenarios. source-load interactions. Our analysis indicates that traditional
|     |     |     |     |     |     | static methods     | fail to capture | the     | evolutionary |              | characteristics | of       |
| --- | --- | --- | --- | --- | --- | ------------------ | --------------- | ------- | ------------ | ------------ | --------------- | -------- |
|     |     |     |     |     |     | energy consumption | and             | exhibit | operational  | instability. |                 | To solve |
4.8.1 Event-drivenconceptdriftvalidation theseproblems,weutilizedaMulti-ViewDynamicGraphNeural
Networkastheunderlyingarchitecture.
ToverifythattheexceptionallylowCSRachievedbyDynECis The core technical contributions of our framework are
notmerelytheresultofmathematicalover-smoothing,weanalyze
|     |     |     |     |     |     | summarized | as follows: First, | it  | integrates | geometric, |     | temporal |
| --- | --- | --- | --- | --- | --- | ---------- | ------------------ | --- | ---------- | ---------- | --- | -------- |
its behavior around real-world events. Using the verified City-A (cDTW), and statistical dependencies to capture complex non-
event log for the same 500-user evaluation subset, we aggregate Euclidean correlations, thereby comprehensively addressing the
| recorded | EV, PV, | and SHOCK | events into | monthly | snapshots |     |     |     |     |     |     |     |
| -------- | ------- | --------- | ----------- | ------- | --------- | --- | --- | --- | --- | --- | --- | --- |
limitationsofsingle-metricsimilarityindynamicenvironments.In
and compare them with the mean ARI/CSR trajectories over addition,itintroducesaunifiedparadigmthatcombinesaGated
| five seeds. | As shown | in Figure6, | Month 5 | contains the | highest |     |     |     |     |     |     |     |
| ----------- | -------- | ----------- | ------- | ------------ | ------- | --- | --- | --- | --- | --- | --- | --- |
Spatio-TemporalGraphEncoderwithDual-ObjectiveEvolutionary
concentration of verified events (32 affected users). Around this Optimization.Thismechanismallowsthemodeltolearnevolution-
peak-driftsnapshot,theproposedmodelpreservesaclearlyhigher aware representations while explicitly balancing the trade-off
| ARI than | Evolutionary | K-Means | while allowing | a moderate | CSR |     |     |     |     |     |     |     |
| -------- | ------------ | ------- | -------------- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- |
betweensnapshotclusteringqualityandtemporalsmoothness.
increase, whereas Evolutionary K-Means keeps CSR near zero Extensive experiments on three real-world datasets—
| by over-smoothing, |     | and its | ARI drops steadily | after | the event |            |                               |     |     |                       |     |     |
| ------------------ | --- | ------- | ------------------ | ----- | --------- | ---------- | ----------------------------- | --- | --- | --------------------- | --- | --- |
|                    |     |         |                    |       |           | comprising | mixed residential/commercial, |     |     | residential-dominant, |     |     |
accumulationperiod. and industrial park zones—confirm that DynEC significantly
|     |     |     |     |     |     | reduces the | Cluster Switching | Rate             | (CSR) | compared |            | to static |
| --- | --- | --- | --- | --- | --- | ----------- | ----------------- | ---------------- | ----- | -------- | ---------- | --------- |
|     |     |     |     |     |     | baselines,  | while maintaining | state-of-the-art |       |          | clustering | quality   |
5 Conclusion (Silhouette Coefficient). By shifting from state-based analysis
|     |     |     |     |     |     | to process-based | evolution | tracking, |     | the proposed |     | approach |
| --- | --- | --- | --- | --- | --- | ---------------- | --------- | --------- | --- | ------------ | --- | -------- |
In this article, we presented the DynEC framework to establishes a robust foundation for dynamic pricing and targeted
|             |            |                             |     |             |     | demand response. | Ultimately, | DynEC | strikes |     | a critical | balance |
| ----------- | ---------- | --------------------------- | --- | ----------- | --- | ---------------- | ----------- | ----- | ------- | --- | ---------- | ------- |
| address the | challenges | in Source-Grid-Load-Storage |     | integration |     |                  |             |       |         |     |            |         |
environments. By modeling load profiling as a continuous between stability and adaptability, paving the way for the next
evolutionaryprocessratherthanasetofstaticlabels,iteffectively generationofreliableandautomatedsmartgridmanagement.
| FrontiersinArtificialIntelligence |     |     |     |     |     | 13  |     |     |     |     | frontiersin.org |     |
| --------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --------------- | --- |

Zhaoetal. 10.3389/frai.2026.1829649
Data availability statement Conflict of interest
The Data availability statement is accurate. The datasets and The author(s) declared that this work was conducted in the
codeareavailableat:https://github.com/jerryao/DynEC. absenceofanycommercialorfinancialrelationshipsthatcouldbe
construedasapotentialconflictofinterest.
Author contributions
Generative AI statement
LZ: Writing – original draft. HZ: Supervision, Writing –
review & editing. ML: Investigation, Writing – review & editing.
JW: Methodology, Validation, Writing – review & editing. XK: Theauthor(s)declaredthatgenerativeAIwasnotusedinthe
Funding acquisition, Resources, Writing – review & editing. YY: creationofthismanuscript.
Conceptualization,Writing–review&editing. Any alternative text (alt text) provided alongside figures
in this article has been generated by Frontiers with the
support of artificial intelligence and reasonable efforts have
Funding been made to ensure accuracy, including review by the
authors wherever possible. If you identify any issues, please
The author(s) declared that financial support was received contactus.
for this work and/or its publication. This research was funded
by the State Grid Sichuan Electric Power Corporation, grant
number 521999240001 (Research on Key Technologies for Fine
Management and Precise Control of Load Resources for Power Publisher’s note
Supply Guarantee Demand-Side Management). The APC was
fundedbytheStateGridSichuanElectricPowerCorporation.
All claims expressed in this article are solely those of the
authors and do not necessarily represent those of their affiliated
organizations, or those of the publisher, the editors and the
Acknowledgments
reviewers. Any product that may be evaluated in this article, or
claimthatmaybemadebyitsmanufacturer,isnotguaranteedor
Wethankthereviewersfortheirconstructivefeedback. endorsedbythepublisher.
References
Badhe, N. B., Neve, R. P., Yele, V. P., Abhang, S., Dhule, K. M., and Mali, D. El Amouri, H., Lampert, T., Gançarski, P., and Mallet, C. (2023). Constrained
(2025). An optimized system for predicting energy usage in smart grids using dtw preserving shapelets for explainable time-series clustering. Pattern Recognit.
temporal fusion transformer and Aquila optimizer. Front. Artif. Intell. 8:1542320. 143:109804.doi:10.1016/j.patcog.2023.109804
doi:10.3389/frai.2025.1542320
Fekri,M.N.,Patel,H.,Grolinger,K.,andSharma,V.(2021).Deeplearningforload
Balamurugan,M.,Narayanan,K.,Raghu,N.,ArjunKumar,G.B.,andTrupti,V.N. forecastingwithsmartmeterdata:onlineadaptiverecurrentneuralnetwork.Appl.
(2025).Roleofartificialintelligenceinsmartgrid–aminireview.Front.Artif.Intell. Energy282:116177.doi:10.1016/j.apenergy.2020.116177
8:1551661.doi:10.3389/frai.2025.1551661 Gama, J., Žliobaite˙, I., Bifet, A., Pechenizkiy, M., and Bouchachia, A. (2014). A
Belge,A.T.,Gupta,S.,Alegavi,S.,Singh,V.,andShukla,K.(2024).Advancements, surveyonconceptdriftadaptation.ACMComput.Surv.46,1–37.doi:10.1145/25
challenges,andfutureprospectsofsmartgridtechnologyinIndia.Front.Artif.Intell. 23813
7:1475604.doi:10.3389/frai.2024.1475604 Hassani,K.,andKhasahmadi,A.H.(2020).“Contrastivemulti-viewrepresentation
Berndt,D.J.,andClifford,J.(1994).“Usingdynamictimewarpingtofindpatternsin learning on graphs,” in International Conference on Machine Learning (PMLR),
timeseries,”inProceedingsofthe3rdInternationalConferenceonKnowledgeDiscovery 4116–4126.
andDataMining(KDD-94),359–370. Jain, M., AlSkaif, T., and Dev, S. (2021). Validating clustering frameworks
Bo, D., Wang, X., Cui, C., Wang, H., and Shi, C. (2020). “Structural deep for electric load demand profiles. IEEE Trans. Ind. Inform. 17, 8057–8065.
clustering network,” in Proceedings of the Web Conference 2020, 1400–1410. doi:10.1109/TII.2021.3061470
doi:10.1145/3366423.3380214 Jiang, Z., Lin, R., and Yang, F. (2021). An incremental clustering algorithm
with pattern drift detection for iot-enabled smart grid system. Sensors 21:6466.
Chakrabarti, D., Kumar, R., and Tomkins, A. (2006). “Evolutionary clustering,”
doi:10.3390/s21196466
in Proceedings of the 12th ACM SIGKDD International Conference on Knowledge
Discovery and Data Mining, KDD ’06 (ACM), 554–560. doi: 10.1145/1150402. Keogh,E.,andRatanamahatana,C.A.(2005).Exactindexingofdynamictimewarping.
1150467 Knowl.Inf.Syst.7,358–386.doi:10.1007/s10115-004-0154-9
Cheng,Z.,Yang,Y.,Wang,W.,Hu,W.,Zhuang,Y.,andSong,G.(2020).“Time2graph: Kim, M., Firoozjaei, M. D., Kim, H., and El-Hajj, M. (2025). Power profiling
revisitingtimeseriesmodelingwithdynamicshapelets,”inProceedingsoftheAAAI of smart grid users using dynamic time warping. Electronics 14:2015.
ConferenceonArtificialIntelligence,3617–3624.doi:10.1609/aaai.v34i04.5769 doi:10.3390/electronics14102015
Chicco, G., Napoli, R., and Piglione, F. (2006). Comparisons among clustering Lange, T., Roth, V., Braun, M. L., and Buhmann, J. M. (2004). Stability-
techniquesforelectricitycustomerclassification.IEEETrans.PowerSyst.21,933–940. based validation of clustering solutions. Neural Comput. 16, 1299–1323.
doi:10.1109/TPWRS.2006.873122 doi:10.1162/089976604773717621
FrontiersinArtificialIntelligence 14 frontiersin.org

| Zhaoetal. |     |     |     |     |     |     | 10.3389/frai.2026.1829649 |     |
| --------- | --- | --- | --- | --- | --- | --- | ------------------------- | --- |
Li,Y.,Yu,R.,Shahabi,C.,andLiu,Y.(2018).Diffusionconvolutionalrecurrentneural Sankar,A.,Wu,Y.,Gou,L.,Zhang,W.,andYang,H.(2020).“Dysat:deepneural
network:data-driventrafficforecasting.arXivpreprintarXiv:1707.01926. representationlearningondynamicgraphsviaself-attentionnetworks,”inProceedings
|              |                   |                        |            |               | of the 13th International | Conference on | Web Search and | Data Mining, 519–527. |
| ------------ | ----------------- | ---------------------- | ---------- | ------------- | ------------------------- | ------------- | -------------- | --------------------- |
| Lin, S., Li, | F., Tian, E., Fu, | Y., and Li, D. (2019). | Clustering | load profiles |                           |               |                |                       |
doi:10.1145/3336191.3371845
| for demand | response applications. | IEEE Trans. | Smart Grid 10, | 1599–1607. |     |     |     |     |
| ---------- | ---------------------- | ----------- | -------------- | ---------- | --- | --- | --- | --- |
doi:10.1109/TSG.2017.2773573 Tariq, M. A. U. R., Poorolajal, J., and Shah, S. A. A. (2022). Deterioration of
|     |     |     |     |     | electrical load forecasting | models in a | smart grid environment. | Sensors 22:4363. |
| --- | --- | --- | --- | --- | --------------------------- | ----------- | ----------------------- | ---------------- |
Long,C.,Yang,X.,Su,Y.,Liu,F.,Ma,R.,Ma,T.,etal.(2025).Airconditioningload
| forecastingforgeographicalgridsusingdeepreinforcementlearninganddensity-based |     |     |     |     | doi:10.3390/s22124363 |     |     |     |
| ----------------------------------------------------------------------------- | --- | --- | --- | --- | --------------------- | --- | --- | --- |
spatialclusteringofapplicationswithnoiseandgraphattentionnetworks.Energies Tolas,R.,Portase,R.,andPotolea,R.(2024).Fromindividualdeviceusagetohousehold
18:2832.doi:10.3390/en18112832 energy consumption profiling. Electronics 13:2325. doi: 10.3390/electronics131
22325
| Lu, J., Liu, | A., Dong, F., Gu, | F., Gama, J., and | Zhang, G. (2018). | Learning |     |     |     |     |
| ------------ | ----------------- | ----------------- | ----------------- | -------- | --- | --- | --- | --- |
under concept drift: a review. IEEE Trans. Knowl. Data Eng. 31, 2346–2363. Velicˇkovic´,P.,Fedus,W.,Hamilton,W.L.,Lió,P.,Bengio,Y.,andHjelm,R.D.(2019).
doi:10.1109/TKDE.2018.2876857 “Deepgraphinfomax,”inInternationalConferenceonLearningRepresentations,1–13.
Luxburg, U. (2007). A tutorial on spectral clustering. Stat. Comput. 17, 395–416. Verma, S., and Rao, A. (2025). A short report on deep learning synergy
doi:10.1007/s11222-007-9033-z for decentralized smart grid cybersecurity. Front. Artif. Intell. 8:1557960.
doi:10.3389/frai.2025.1557960
Muyulema-Masaquiza,D.,andAyala-Chauvin,M.(2025).Segmentationofenergy
consumptionusingk-means:applicationsintariffing,outlierdetection,anddemand Wang,B.,Li,Y.,Ming,W.,andWang,S.(2020).Deepreinforcementlearningmethod
predictioninnon-smartmeteringsystems.Energies18:3083.doi:10.3390/en18123083 fordemandresponsemanagementofinterruptibleload.IEEETrans.SmartGrid11,
3146–3155.doi:10.1109/TSG.2020.2967430
| Pareja, A., | Domeniconi, G., | Chen, J., Ma, T., | Suzumura, T., Kanezashi, | H., |     |     |     |     |
| ----------- | --------------- | ----------------- | ------------------------ | --- | --- | --- | --- | --- |
et al. (2020). “Evolvegcn: evolving graph convolutional networks for dynamic Wang,M.,Li,H.,andWu,J.(2023).Self-superviseddynamicgraphrepresentation
graphs,”inProceedingsoftheAAAIConferenceonArtificialIntelligence,5363–5370. learningviatemporalsubgraphcontrast.ACMTrans.Knowl.Disc.Data18,1–20.
| doi:10.1609/aaai.v34i04.5984 |     |     |     |     | doi:10.1145/3612931 |     |     |     |
| ---------------------------- | --- | --- | --- | --- | ------------------- | --- | --- | --- |
Ratanamahatana,C.A.,andKeogh,E.(2004).“Everythingyouknowaboutdynamic Wang,Y.,Chen,Q.,Hong,T.,andKang,C.(2019).Reviewofsmartmeterdata
timewarpingiswrong,”inProceedingsoftheThirdWorkshoponMiningTemporaland analytics:applications,methodologies,andchallenges.IEEETrans.SmartGrid10,
| SequentialData,1–11. |     |     |     |     | 3125–3148.doi:10.1109/TSG.2018.2818167 |     |     |     |
| -------------------- | --- | --- | --- | --- | -------------------------------------- | --- | --- | --- |
Rossi, E., Chamberlain, B., Frasca, F., Eynard, D., Monti, F., and Bronstein, M. Wu,Z.,Pan,S.,Long,G.,Jiang,J.,andZhang,C.(2019).“Graphwavenetfordeep
(2020).Temporalgraphnetworksfordeeplearningondynamicgraphs.arXivpreprint spatial-temporalgraphmodeling,”inProceedingsoftheInternationalJointConference
arXiv:2006.10637. onArtificialIntelligence(IJCAI),1907–1913.doi:10.24963/ijcai.2019/264
Rousseeuw, P. J. (1987). Silhouettes: a graphical aid to the interpretation Zhang,S.,Zhu,J.,Luo,E.,Zhu,X.,andYang,Q.(2025).Dpck:anadaptivedifferential
and validation of cluster analysis. J. Comput. Appl. Math. 20, 53–65. privacy-basedck-meansclusteringschemeforsmartmeterdataanalysis.Electronics
doi:10.1016/0377-0427(87)90125-7 14:2074.doi:10.3390/electronics14102074
Sakoe, H., and Chiba, S. (1978). Dynamic programming algorithm Zou, J., Liu, S., Ouyang, L., Ruan, J., and Tang, S. (2024). Carbon-aware
optimization for spoken word recognition. IEEE Trans. Acoust. 26, 43–49. demand response for residential smart buildings. Electronics 13:4941.
doi:10.1109/TASSP.1978.1163055 doi:10.3390/electronics13244941
| FrontiersinArtificialIntelligence |     |     |     |     | 15  |     |     | frontiersin.org |
| --------------------------------- | --- | --- | --- | --- | --- | --- | --- | --------------- |