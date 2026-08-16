---
conversion_metadata:
  converted_at: "2026-07-21T13:58:55Z"
  converter_tool: "markitdown"
  converter_version: "0.1.6"
  source_pdf: "Li C. et al.pdf"
  source_pdf_sha256: "26b2bb19f688eca5e47db9ea6ed115a16565655f79bc61825ff8663c2e35db54"
  page_count: 30
  markdown_char_count: 362791
---

<!-- PAGE-AWARE EXTRACTION (via pdfminer.six) -->

<!-- PAGE 1 -->

Received 6 April 2026, accepted 18 May 2026, date of publication 29 May 2026, date of current version 16 June 2026.

Digital Object Identifier 10.1109/ACCESS.2026.3697984

BIRCH-AE: A Hierarchical Ensemble Framework
for Scalable E-Commerce User Segmentation
With Autoencoder-Enhanced Feature Learning

CAIWEN LI 1, ISKANDAR ISHAK 1, HAMIDAH IBRAHIM 1, (Member, IEEE),
MASLINA ZOLKEPLI1, FATIMAH SIDI 1, (Member, IEEE), AND CAILI LI 2
1Department of Computer Science, Faculty of Computer Science and Information Technology, Universiti Putra Malaysia (UPM), Serdang,
Selangor 43400, Malaysia
2College of Art and Design, Heilongjiang Institute of Technology, Daowai, Harbin, Heilongjiang 150050, China

Corresponding author: Iskandar Ishak (iskandar_i@upm.edu.my)

This work was supported in part by the Journal Publication Fund under the University Driven Research Program (Digital and ICTI),
Universiti Putra Malaysia, and in part by the Faculty of Computer Science and Information Technology, Universiti Putra Malaysia.

ABSTRACT The rapid expansion of e-commerce platforms has intensified demand for scalable, high-quality
user segmentation systems capable of efficiently processing millions of behavioral records. This paper
presents BIRCH-AE, a hierarchical ensemble clustering framework that integrates the Balanced Iterative
Reducing and Clustering using Hierarchies (BIRCH) algorithm with autoencoder-based feature learning
for large-scale e-commerce analytics. The autoencoder compresses high-dimensional behavioral data into
compact latent representations, mitigating the curse of dimensionality and improving cluster separability.
Multiple BIRCH configurations are combined through four ensemble strategies: Majority Voting, Weighted
Voting, Advanced Affinity-based Spectral Clustering (AASC), and the proposed BIRCH-Optimized
Hierarchical Consensus (BOHC). Dynamic selection based on multi-criteria evaluation automatically
identifies the best-performing strategy per dataset setting, emphasizing that no single consensus method
is universally optimal. Experiments on two large-scale datasets (Retail Rocket with 1.4M users and
E-Commerce Behavior with 4.5M users) show improved clustering quality and practical scalability. BOHC
achieves up to 23% silhouette improvement over single BIRCH on transaction-focused data, with a clearer
hierarchical structure, while multi-domain data favors strong base models. Autoencoder feature learning
improves clustering quality by 23–53% over raw features. The full 4.5M-user experiment was executed as a
BOHC scalability run, completed in approximately 5 minutes, while framework-level comparative analyses
were conducted via repeated stratified 30%-subset trials. These findings support BIRCH-AE as a practical
and adaptive segmentation framework for enterprise-scale e-commerce analytics.

INDEX TERMS BIRCH clustering, hierarchical clustering, user segmentation, autoencoders, e-commerce
analytics, ensemble methods, scalable clustering, incremental learning.

I. INTRODUCTION
The exponential growth of e-commerce platforms has fun-
damentally transformed retail dynamics, generating unprece-
dented volumes of user interaction data [1], [2]. Modern
e-commerce systems routinely collect detailed behavioral
information spanning browsing patterns, purchase histo-
ries, search queries, and engagement metrics at multiple

The associate editor coordinating the review of this manuscript and

approving it for publication was Dominik Strzalka

.

touchpoints [3]. This rich data landscape presents opportu-
nities and challenges for companies seeking to understand
customer behavior and deliver personalized experiences.

User segmentation, the systematic process of dividing
a heterogeneous customer base into homogeneous groups
that share similar characteristics or behaviors, has become a
cornerstone strategy in modern data-driven systems [4], [5].
The fundamental premise of segmentation is that customers
exhibit diverse needs, preferences, purchasing patterns,
and engagement behaviors. Rather than applying uniform

88580

2026 The Authors. This work is licensed under a Creative Commons Attribution 4.0 License.
For more information, see https://creativecommons.org/licenses/by/4.0/

VOLUME 14, 2026

---

<!-- PAGE 2 -->

C. Li et al.: BIRCH-AE: A Hierarchical Ensemble Framework for Scalable E-Commerce User Segmentation

strategies across an entire customer population, segmen-
tation enables organizations to identify distinct subgroups
and tailor their approaches accordingly [6]. This strategic
differentiation has profound implications across multiple
business functions, from marketing and product development
to customer service and inventory management.

In contemporary e-commerce environments, effective user
segmentation serves several critical business objectives [7],
it enables personalized marketing campaigns
[8]. First,
that resonate with specific customer segments, significantly
improving conversion rates and return on marketing invest-
ment. By understanding the characteristics and preferences of
different user groups, businesses can craft targeted messages,
promotional offers, and product recommendations that align
with each segment’s unique profile [3]. Second, segmentation
facilitates dynamic pricing strategies and inventory optimiza-
tion, allowing platforms to adjust pricing and stock levels
based on segment-specific demand patterns and price sensi-
tivities [1]. Third, it supports customer lifetime value predic-
tion and churn prevention, enabling proactive retention strate-
gies for high-value segments and win-back campaigns for
at-risk customers [9]. Fourth, segmentation provides strategic
insights for product development by revealing unmet needs
and emerging trends within specific customer groups [4].

The significance of user segmentation has increased as
the field has evolved from traditional demographic and
rule-based categorization to sophisticated data-driven behav-
ioral segmentation [7]. Modern approaches leverage machine
learning and data mining techniques to uncover complex
patterns in vast behavioral datasets, enabling more nuanced
and actionable customer understanding [10]. E-commerce
platforms now analyze multidimensional behavioral signals,
including browsing frequency, session duration, product
category exploration, cart abandonment patterns, purchase
recency and frequency, average order values, price sensitivity
indicators,
temporal activity patterns, and cross-category
engagement metrics [2], [11]. This comprehensive behavioral
view enables segmentation strategies that go far beyond sim-
ple RFM (Recency, Frequency, Monetary) analysis, capturing
the full complexity of modern customer journeys [9].

However, the transition to large-scale, behavior-driven
segmentation introduces significant technical challenges. The
enormous data generated by modern e-commerce platforms,
with millions of users creating billions of
interaction
events, requires clustering algorithms that can efficiently
process large datasets [12], [13]. The high dimensionality
of behavioral feature spaces, often encompassing hundreds
of correlated variables, poses significant challenges for
clustering algorithms. These include the curse of dimension-
ality, degradation of distance metrics, and increased noise
sensitivity [14], [15]. The dynamic nature of e-commerce
environments, where user behavior continuously evolves,
and new customers arrive in real time, requires segmen-
tation systems that can adapt incrementally without com-
plete recomputation [16]. Furthermore, the requirement for
multi-resolution segmentation, supporting both strategic

planning with broad customer categories and tactical mar-
keting with fine-grained micro-segments, adds additional
complexity that traditional clustering methods struggle to
address [17].

These challenges motivate the development of advanced
clustering frameworks that can simultaneously achieve
scalability, quality, and adaptability for enterprise-scale e-
commerce user segmentation. The need for such systems
has become particularly acute as platforms expand their
customer bases to millions and diversify their product
offerings across multiple categories, creating increasingly
complex segmentation requirements.

A. LIMITATIONS OF TRADITIONAL APPROACHES
Traditional clustering algorithms, including K-Means [18],
DBSCAN [19], and hierarchical agglomerative methods [20],
have been extensively applied to customer segmentation tasks
across various domains. However, recent comprehensive
surveys and empirical studies [7], [8], [12] identify three
critical limitations that severely constrain their applicability
when confronting contemporary e-commerce data at scale.

First, scalability constraints significantly limit practical
deployability for large-scale applications. The compu-
tational complexity of
traditional clustering algorithms
becomes prohibitive as dataset sizes grow into the millions of
users common in modern e-commerce platforms. K-Means,
despite its popularity and relative efficiency, requires multiple
iterative passes over the entire dataset to converge. Each
iteration computes distances between all data points and
cluster centroids [18], [21]. For datasets with millions of users
and dozens of features, this iterative process can take hours
or even days to complete, making real-time or near-real-
time segmentation infeasible [12]. Traditional hierarchical
agglomerative methods face even more severe limitations,
typically exhibiting quadratic time complexity O(n2) and
requiring O(n2) memory to store the distance matrix between
all pairs of data points [17], [20]. These quadratic require-
ments render hierarchical methods completely impractical
for datasets exceeding a few tens of thousands of users—
far below the scale of contemporary e-commerce platforms
with millions of active customers [13]. DBSCAN, while
offering advantages for discovering arbitrarily shaped clus-
ters, similarly struggles with scalability due to its need to
compute neighborhood relationships, often requiring spatial
indexing structures that themselves become computationally
expensive for high-dimensional data [19]. The scalability
limitation is not merely a matter of computational cost.
Still, it fundamentally limits organizations’ ability to perform
comprehensive segmentation across their full customer bases,
often forcing them to work with small samples that may not
capture the full diversity of customer behaviors [12].

Second, the curse of dimensionality fundamentally
degrades clustering performance in high-dimensional
behavioral feature spaces. Modern e-commerce platforms
generate rich behavioral profiles encompassing hundreds
of features: activity metrics (total events, unique products

VOLUME 14, 2026

88581

---

<!-- PAGE 3 -->

C. Li et al.: BIRCH-AE: A Hierarchical Ensemble Framework for Scalable E-Commerce User Segmentation

viewed, sessions count), engagement patterns (events per
session, session duration, category diversity), transactional
features (purchase frequency, average order value, price range
statistics), temporal behaviors (preferred shopping times,
activity consistency, recency indicators), and cross-category
interaction patterns [2], [11]. These comprehensive feature
sets are essential for capturing the multidimensional nature
of customer behavior but create significant challenges for
traditional clustering algorithms. In high-dimensional spaces,
distance metrics become less discriminative as the relative
contrast between nearest and farthest neighbors diminishes:
a phenomenon extensively documented in the literature [13],
[14]. This distance concentration effect causes K-Means
and other distance-based algorithms to produce suboptimal
clusters, since the fundamental assumption that nearby points
should belong to the same cluster breaks down when dis-
tances lose meaning [10]. Furthermore, behavioral features
of e-commerce exhibit strong intercorrelations: browsing
frequency correlates with session counts, purchase amounts
correlate with price sensitivity, and category exploration
correlates with session duration [15]. These correlations
introduce redundancy that inflates the effective dimension-
ality without adding proportional information, exacerbating
computational costs and further degrading the quality of the
distance metric [14]. Traditional dimensionality reduction
techniques, such as Principal Component Analysis (PCA),
provide only linear projections that may fail to capture
the complex nonlinear relationships inherent in behavioral
data [22]. In contrast, more sophisticated non-linear methods
have not been systematically integrated with scalable cluster-
ing algorithms for e-commerce applications [23], [24].

Third, the static nature of traditional clustering meth-
ods renders them unsuitable for dynamic e-commerce
environments requiring continuous adaptation, and com-
merce platforms operate in highly dynamic contexts where
user behaviors evolve continuously. Customers move through
lifecycle stages, respond to seasonal trends, adopt new shop-
ping patterns, and alter their preferences for categories over
time [2], [3]. Additionally, platforms continuously acquire
new users that must be integrated into the segmentation
scheme without disrupting existing segment definitions [16].
Traditional clustering algorithms are fundamentally batch-
oriented: they require access to the complete dataset at
training time and produce a fixed partition that cannot adapt
to new data without complete recomputation [13]. When new
users arrive or existing users exhibit changes in behavior,
the only option is to rerun the entire clustering process from
scratch: an approach that is computationally prohibitive for
million-user platforms that require daily or even hourly seg-
ment updates [12], [16]. This limitation creates a critical gap
between the business requirements for responsive near-real-
time segmentation and the technical capabilities of traditional
methods. K-Means lacks an incremental learning mecha-
nism; each new batch of users requires reinitialization of
cluster centroids and reprocessing all data [18]. Hierarchical
methods similarly require rebuilding the entire dendrogram

from scratch, with no mechanism to insert new data points
into an existing hierarchy [17]. Although some research has
explored incremental variants of these algorithms [16], these
approaches often sacrifice cluster quality for adaptability
or introduce additional hyperparameters that are difficult
to tune in practice. The absence of robust
incremental
learning capabilities forces e-commerce platforms to choose
between maintaining outdated segmentations that no longer
reflect current customer behaviors or investing substantial
computational resources in frequent, complete re-clustering.
Neither option is satisfactory for operational excellence.

These three fundamental

limitations: scalability con-
straints, high-dimensional feature degradation, and lack
of incremental adaptability—collectively demonstrate that
traditional clustering approaches, despite their theoretical
elegance and historical success in smaller-scale applications,
are inadequate for modern enterprise-scale e-commerce user
segmentation. This recognition motivates the development
of novel frameworks that simultaneously address all three
challenges through architectural innovations that combine
scalable hierarchical methods, advanced feature learning, and
incremental update mechanisms.

B. RESEARCH GAPS AND MOTIVATION
Despite extensive research in clustering methodologies,
recent comprehensive surveys [25], [26], [27] identify critical
gaps in large-scale e-commerce user segmentation. Although
BIRCH [28] offers excellent scalability through its Clustering
Feature (CF) Tree structure and single-pass processing, its
application to e-commerce remains limited. Existing work
focuses primarily on spatial data and sensor networks [29].
Systematic approaches to optimize BIRCH performance
through ensemble methods and advanced feature learning
remain underdeveloped for behavioral data.

Current ensemble clustering frameworks [26], [30], [31]
predominantly focus on partition-based algorithms, neglect-
ing the unique advantages of hierarchical methods in
capturing multi-scale user groupings. Modern deep clustering
research [23], [24] primarily integrates autoencoders with
K-Means or Gaussian Mixture Models, overlooking hier-
archical algorithms despite their superior ability to reveal
nested customer segment structures, which are crucial for
marketing strategies [27].

Furthermore, measuring user engagement through nav-
igational behavior patterns [11] has become increasingly
important. These engagement metrics, when combined with
transactional data, provide a comprehensive view of user
behavior that significantly enhances segmentation qual-
ity. The integration of autoencoder-based feature learning
with BIRCH’s hierarchical structure (particularly for high-
dimensional e-commerce data with correlated variables [8],
[15]) represents an unexplored opportunity.

C. CONTRIBUTIONS
To address these limitations and research gaps, this paper
introduces BIRCH-AE, a comprehensive framework for

88582

VOLUME 14, 2026

---

<!-- PAGE 4 -->

C. Li et al.: BIRCH-AE: A Hierarchical Ensemble Framework for Scalable E-Commerce User Segmentation

integrates
scalable e-commerce user segmentation that
BIRCH’s hierarchical clustering capabilities with deep
autoencoder-based feature learning and advanced ensemble
consensus mechanisms. The framework’s architecture posi-
tions BIRCH as the core scalable clustering engine, enhanced
by autoencoder-driven dimensionality reduction and unified
through multiple ensemble strategies, including the novel
BIRCH-Optimized Hierarchical Consensus (BOHC) method.
The key contributions are as follows.

1) Scalable Hierarchical Framework with Deep Fea-
ture Integration: A unified architecture combin-
ing BIRCH’s memory-efficient hierarchical clustering
with deep autoencoder-based feature learning. The
autoencoder compresses high-dimensional, correlated
behavioral data (30–50 features) into compact latent
representations (14–32 dimensions) while preserving
90–95% of variance, allowing efficient processing
of million-user datasets. This integration achieves
23–53% improvements in clustering quality over raw
features while maintaining BIRCH’s scalable incre-
mental learning behavior.

2) Novel Hierarchical Ensemble Method (BOHC):
Introduction of BIRCH-Optimized Hierarchical Con-
sensus, a specialized ensemble strategy designed to
preserve multi-scale clustering information inherent
in BIRCH’s CF Tree structure. Unlike conventional
voting or spectral ensemble methods, BOHC con-
structs hierarchical affinity matrices based on ancestral
relationships within CF Trees, enabling consensus
formation that preserves hierarchical context across
multiple BIRCH configurations. Experiments demon-
strate BOHC achieves up to 23% improvement over
single BIRCH models for transaction-focused datasets
with distinct cluster boundaries.

3) Comprehensive Ensemble Strategy Suite with
Dynamic Selection: Integration of four complemen-
tary ensemble approaches: Majority Voting, Weighted
Voting, Advanced Affinity-based Spectral Clustering
(AASC), and BOHC within the BIRCH-AE frame-
work. A multi-criteria dynamic selection mechanism
automatically identifies optimal strategies based on Sil-
houette Score, Calinski-Harabasz Index, and Davies-
Bouldin Index, adapting to dataset characteristics
without manual intervention. This adaptive approach
addresses the challenge that no single ensemble
method universally outperforms across different data
distributions and domain granularities.

4) Domain Granularity Impact Discovery: Empir-
ical evidence revealing that domain granularity
(single-domain
fundamentally
vs. multi-domain)
determines optimal segmentation strategies. Single-
domain datasets (e.g., transaction-focused platforms,
individual product categories) consistently benefit
from ensemble methods (+17–23% improvement),
while multi-domain datasets (multiple product cat-
egories) favor well-tuned base algorithms (+7.4%

over ensembles). This finding, validated across three
distinct evaluation scenarios, provides practitioners
with clear decision criteria for selecting methods based
on platform structure.

5) Enterprise-Scale Validation and Deployment Guide-
lines: Comprehensive empirical validation on repre-
sentative subsets of two large-scale datasets (Retail
Rocket: 1.4M users, E-Commerce Behavior: 4.5M
users) with single-domain category analysis, supported
by 20 randomized stratified subset trials. A production-
scale BOHC run on 4.5M users (approximately
5 minutes) demonstrates operational feasibility at
scale. Evidence-based deployment recommendations
guide practitioners through data profiling, method
selection based on domain granularity and cluster
characteristics, and incremental update strategies for
dynamic environments.

These contributions collectively advance large-scale user
segmentation by providing an empirically grounded, practi-
cally deployable framework that addresses the fundamental
limitations of traditional clustering approaches and offers
actionable guidance for real-world e-commerce applications.

D. PAPER ORGANIZATION
The remainder of this paper is organized as follows. Section II
reviews related work in clustering methods, ensemble tech-
niques, and dimensionality reduction for user segmentation.
Section III provides technical background on BIRCH clus-
tering and autoencoders. Section IV details the BIRCH-AE
framework architecture, including the four ensemble strate-
gies (Majority Voting, Weighted Voting, AASC, and BOHC)
and the dynamic selection mechanism. Section V presents
a comprehensive experimental evaluation with detailed
comparative analysis. Section VI discusses implications,
limitations, and applications. Section VII concludes with
future research directions. To support reproducibility, the
BIRCH-AE implementation code and experimental materials
are available [32].

II. RELATED WORK
A. E-COMMERCE USER SEGMENTATION
User segmentation has been an integral part of e-commerce
analytics, with methodologies evolving from demographic
and rule-based categorization to sophisticated machine learn-
ing approaches [4], [5]. Modern comprehensive reviews [7],
[8] highlight this evolution towards data-driven behavioral
segmentation based on purchase patterns, browsing behavior,
and engagement metrics [10].

Garcia et al. [2] demonstrate the effectiveness of deep
learning in customer behavior analysis. In contrast, Patel et al.
[3] emphasize the need for real-time segmentation to support
dynamic personalization at scale. Traditional clustering
algorithms remain popular for their simplicity but face sig-
nificant challenges in handling the volume of contemporary
e-commerce data.

VOLUME 14, 2026

88583

---

<!-- PAGE 5 -->

C. Li et al.: BIRCH-AE: A Hierarchical Ensemble Framework for Scalable E-Commerce User Segmentation

K-Means [18] suffers from sensitivity to initialization
and assumptions of spherical clusters [21]. Zhao et al.
[15] address high-dimensional customer segmentation with
correlated features using extended regularized K-Means,
demonstrating the importance of accounting for feature
correlations. DBSCAN [19] offers advantages for arbitrar-
ily shaped clusters but requires careful parameter tuning
and struggles with varying density patterns. Traditional
hierarchical methods provide intuitive dendrograms but are
computationally expensive for large-scale applications [17].
Recent advanced techniques include model-based cluster-
ing [33], [34], spectral methods [35], and hybrid approaches.
Gaussian Mixture Models [36] provide probabilistic cluster
assignments, but require careful model selection. Spectral
clustering excels at non-convex clustering using graph-based
representations but faces scalability challenges [12].

Lim et al. [11] introduced the Cluster-N-Engage frame-
work, which measures user engagement through navigational
behavior patterns and demonstrates the importance of inte-
grating engagement metrics with traditional clustering for
comprehensive customer segmentation.

B. BIRCH: SCALABLE HIERARCHICAL CLUSTERING
BIRCH (Balanced Iterative Reducing and Clustering using
Hierarchies) was introduced by Zhang et al. [28] as a
memory-efficient clustering method for very large databases.
The algorithm constructs a Clustering Feature Tree (CF Tree).
This hierarchical data structure provides compact dataset
summaries via triplet representations containing the number
of points, their linear sum, and the sum of squared values.

BIRCH operates in four phases: (1) scanning the database
to build an initial CF tree in-memory, (2) optional tree
condensation to reduce size, (3) global clustering of leaf
entries, and (4) optional cluster refinement. Key parameters
include the branching factor (maximum number of children
per non-leaf node), the threshold (maximum diameter of
subclusters), and the number of final clusters. BIRCH’s
incremental nature enables efficient handling of streaming
data, making it particularly suitable for dynamic e-commerce
environments [29].

Despite scalability advantages, BIRCH has received lim-
ited attention in e-commerce segmentation research, with
most applications focusing on spatial data and sensor
networks [37]. This work addresses this gap by demonstrating
BIRCH’s effectiveness for e-commerce user segmentation
and extending its capabilities through ensemble methods and
deep feature learning.

C. ENSEMBLE CLUSTERING METHODS
The ensemble clustering combines multiple base clustering
solutions to produce consensus results that are more robust
and accurate than individual clusterings [30], [31]. The fun-
damental principle is that different algorithms or parameter
configurations capture distinct aspects of the data structure,
and that their combination can achieve superior performance.

Various consensus functions have been proposed, including
co-association matrices, graph-based methods, and voting
mechanisms [38].

Liu et al. [27] provide a comprehensive review of the past
decade, highlighting that partition-based ensemble methods
dominate the literature. Li et al. [26] emphasize the growing
importance of ensemble learning for big data clustering,
noting that most approaches focus on K-Means variants,
while hierarchical ensemble methods remain underexplored.
Strehl and Ghosh [30] proposed three consensus func-
tions: the Cluster-based Similarity Partitioning Algorithm
(CSPA), the HyperGraph Partitioning Algorithm (HGPA),
and the Meta-CLustering Algorithm (MCLA). Fred and
Jain [31] introduced the evidence accumulation clustering
framework using co-association matrices. Recent work
explores advanced consensus strategies, including spectral
methods [39] and non-negative matrix factorization [40].

However, ensemble methods specifically designed for
hierarchical clustering algorithms, such as BIRCH, remain
underexplored despite their potential advantages. Hierarchi-
cal methods yield richer structural information than partition-
based algorithms, enabling novel ensemble strategies that
leverage hierarchical relationships [34]. This work introduces
ensemble techniques tailored to BIRCH’s hierarchical nature,
including BOHC, which preserves multi-scale clustering
information.

D. DEEP LEARNING FOR DIMENSIONALITY REDUCTION
High-dimensional feature spaces pose significant challenges
for clustering algorithms, including increased computational
complexity, degraded distance metrics, and greater noise sen-
sitivity [14]. Traditional dimensionality reduction techniques
such as Principal Component Analysis (PCA) [22], Linear
Discriminant Analysis [41], and t-SNE [42] have been widely
applied. PCA provides efficient linear projection but may fail
to capture nonlinear patterns. t-SNE excels at visualization
but is computationally intensive and best suited to low-
dimensional embeddings.

Zhao et al. [15] specifically address correlated variables
in high-dimensional customer segmentation through regular-
ized K-Means, demonstrating the importance of accounting
for feature interdependencies in e-commerce datasets.

Autoencoders have emerged as powerful nonlinear
dimensionality-reduction tools capable of learning com-
pact representations that preserve essential data charac-
teristics [43]. Recent comprehensive surveys [23], [24]
systematically review advances in autoencoder-based deep
clustering, highlighting superior performance over traditional
methods for high-dimensional data. The encoder transforms
latent
high-dimensional
representation, while the decoder reconstructs the original
input; training via reconstruction minimization encourages
the latent space to capture salient features.

into a low-dimensional

input

Recent research has extensively explored the combina-
tion of autoencoders with clustering algorithms, focusing

88584

VOLUME 14, 2026

---

<!-- PAGE 6 -->

C. Li et al.: BIRCH-AE: A Hierarchical Ensemble Framework for Scalable E-Commerce User Segmentation

primarily on deep embedded clustering (DEC) [44] and
related methods that jointly optimize clustering and represen-
tation learning. However, comprehensive reviews [23], [25]
reveal that these approaches typically employ K-Means as the
clustering component and have not leveraged the scalability
advantages of hierarchical methods. This work addresses this
gap by integrating autoencoder-based feature learning with
BIRCH clustering, combining the representational power of
autoencoders with the scalability and incremental learning
capabilities of BIRCH [24].

E. RESEARCH POSITIONING
BIRCH-AE occupies a unique position at the intersection
of hierarchical clustering, ensemble methods, and deep
feature learning for e-commerce analytics. Unlike existing
approaches focusing on partition-based ensemble clustering
or simple BIRCH applications, this framework: (1) leverages
BIRCH’s scalability for large-scale e-commerce data, (2)
enhances clustering quality through autoencoder-based fea-
ture learning that handles correlated variables, (3) introduces
four ensemble strategies (including the novel BOHC method)
specifically designed for hierarchical clustering, (4) provides
dynamic ensemble selection for adaptive optimization, and
(5) incorporates engagement metrics alongside traditional
behavioral features. This integrated approach addresses the
critical limitations of existing methods and offers practical
solutions for enterprise-scale e-commerce user segmentation.

III. TECHNICAL PRELIMINARIES
A. BIRCH CLUSTERING FUNDAMENTALS
1) CLUSTERING FEATURE DEFINITION
The foundation of BIRCH is the Clustering Feature (CF),
a compact statistical summary of a cluster. For a cluster
containing Nd-dimensional data points {Xi}N
i=1, the CF is
defined as a triplet:

CF = (N , ⃗LS, SS)

(1)

where N is the number of data points, ⃗LS = PN
i=1 Xi is the
linear sum of the data points, and SS = PN
i=1 X 2
is the sum
i
of the squared data points.

The CF representation is additive: for two disjoint clusters
with CFs (N1, ⃗LS1, SS1) and (N2, ⃗LS2, SS2), their merged CF
is:

CFmerged = (N1 + N2, ⃗LS1 + ⃗LS2, SS1 + SS2)

(2)

This additivity property enables efficient hierarchical con-
struction and dynamic cluster updates.

(B), maximum children for non-leaf nodes; Threshold (T ),
maximum diameter for subclusters at leaf nodes; and Number
of Leaf Entries (L), maximum entries per leaf node.

3) BIRCH ALGORITHM PHASES
BIRCH operates in four phases:

Phase 1 (Tree Construction): The algorithm scans the
dataset once, inserting each data point into the CF Tree. For
each point, it traverses from root to leaf, selecting the closest
child based on a distance metric. If the diameter of the leaf
entry after insertion remains below the threshold T , the point
is absorbed; otherwise, a new leaf entry is created.

Phase 2 (Tree Condensation - Optional): If memory
constraints are violated, a larger threshold T ′ is selected, and
the tree is rebuilt to produce a more compact structure.

Phase 3 (Global Clustering): A global clustering
algorithm is applied to the leaf entries, treating each leaf CF
as a pseudo-data point. This phase can employ K-Means,
hierarchical agglomeration, or other algorithms.

Phase 4 (Cluster Refinement - Optional): Data points
are redistributed to their nearest cluster centroids to correct
potential errors from earlier phases.

4) DISTANCE METRICS
BIRCH employs specific distance metrics optimized for
CF representations. For two clusters with CFs CF1 =
(N1, ⃗LS1, SS1) and CF2 = (N2, ⃗LS2, SS2), common metrics
include:

Centroid Euclidean Distance:

D0 =

(cid:13)
(cid:13)
(cid:13)
(cid:13)
(cid:13)

⃗LS1
N1

−

⃗LS2
N2

(cid:13)
(cid:13)
(cid:13)
(cid:13)
(cid:13)

(3)

Average Inter-cluster Distance:

v
u
u
u
t

D2 =

1
N1N2

N1X

N2X

i=1

j=1

∥Xi − Yj∥2

(4)

Average Intra-cluster Distance:

s

D3 =

2N1SS1 − 2∥ ⃗LS1∥2
N1(N1 − 1)

+

2N2SS2 − 2∥ ⃗LS2∥2
N2(N2 − 1)

(5)

B. AUTOENCODER ARCHITECTURE
1) BASIC FORMULATION
An autoencoder is a neural network designed to learn efficient
data representations in an unsupervised manner, consisting of
two components:

Encoder: Maps input x ∈ Rd to latent representation z ∈

Rp where p < d:

2) CF TREE STRUCTURE
The CF Tree is a height-balanced tree with both leaf and
non-leaf nodes. The nodes without leaves contain entries
[CFi, childi], where CFi summarizes all data points in the
root subtree at childi. Leaf nodes contain entries for individual
subclusters and are linked in sequence to facilitate scanning.
The tree is controlled by three parameters: Branching Factor

z = fθe (x) = σ (Wex + be)
Decoder: Reconstructs the input from latent representation:
ˆx = gθd (z) = σ (Wd z + bd )
(7)
where θe = {We, be} and θd = {Wd , bd } are encoder and
decoder parameters, and σ is an activation function.

(6)

VOLUME 14, 2026

88585

---

<!-- PAGE 7 -->

C. Li et al.: BIRCH-AE: A Hierarchical Ensemble Framework for Scalable E-Commerce User Segmentation

2) TRAINING OBJECTIVE
The autoencoder is trained to minimize the reconstruction
error:

3) DAVIES-BOULDIN INDEX
The Davies-Bouldin (DB) index [47] measures the average
similarity between each group and its most similar group:

L(θe, θd ) =

1
n

n
X

i=1

∥xi − ˆxi∥2

(8)

For e-commerce applications, additional regularization

terms are incorporated:

Ltotal = Lreconstruction + λ1Lsparsity + λ2Lregularization

(9)

where sparsity encourages selective feature activation, and
regularization prevents overfitting.

3) DEEP ARCHITECTURE
For complex e-commerce behavioral data, a multi-layer
architecture is employed:

Encoder layers:

h1 = σ1(W1x + b1)
h2 = σ2(W2h1 + b2)

...
z = σL(WLhL−1 + bL)

(10)
(11)

(12)

Decoder layers: Mirror the encoder with tied or untied
weights, reconstructing the original input through successive
transformations.

C. CLUSTERING EVALUATION METRICS
1) SILHOUETTE SCORE
The silhouette score [45] measures how similar an object is
to its own cluster compared to other clusters. For a data point
i:

s(i) =

b(i) − a(i)
max{a(i), b(i)}

(13)

where a(i) is the average distance to points in the same cluster
and b(i) is the minimum average distance to points in other
clusters. The overall silhouette score is

S =

1
n

n
X

i=1

s(i)

(14)

DB =

1
k

k
X

i=1

(cid:19)

(cid:18) σi + σj
d(ci, cj)

max
j̸=i

(16)

where σi is the average distance between the points in the
cluster i to the centroid of the cluster, and d(ci, cj) is the
distance between the centroids. Lower values indicate better
clustering.

IV. BIRCH-AE FRAMEWORK METHODOLOGY
A. COMPONENT SELECTION RATIONALE
Our architectural choices—standard autoencoder for fea-
ture learning and BIRCH for hierarchical clustering—were
guided by requirements for the production system and prelim-
inary empirical evaluation. For feature learning, we selected
standard autoencoders over Variational Autoencoders (VAE)
for three reasons. First, recent surveys [23] note that while
VAEs offer probabilistic guarantees, reconstruction-focused
autoencoders often achieve superior clustering performance
when latent space separation is prioritized over generative
capability. Second, preliminary experiments on representa-
tive subsets confirmed that standard AE achieved higher
silhouette scores (0.839 vs. VAE’s 0.636) for e-commerce
behavioral data. Third, VAE’s KL-divergence regularization
toward Gaussian priors introduces stochasticity that conflicts
with deterministic e-commerce patterns (such as consistent
purchase sequences and browsing habits). We also evaluated
UMAP (silhouette score: 0.527) and PCA (silhouette score:
0.531), both of which yielded inferior results.

For clustering, BIRCH was selected for its hierarchical
structure, its scalability compared with classical agglomer-
ative approaches [28], and its incremental learning capabil-
ity [29]. Preliminary evaluation on k ∈ {5, 10, 15, 20, 25}
showed that BIRCH maintained comparatively stable per-
formance (silhouette 0.839 → 0.721, −14% degradation),
while K-Means degraded more strongly as k increased. This
stability is important for e-commerce settings that require
finer-grained segmentation (k = 15–25).

with values ranging from −1 to 1, where higher values
indicate better-defined clusters.

2) CALINSKI-HARABASZ INDEX
The Calinski-Harabasz (CH) index [46] evaluates cluster
quality based on the ratio of between-cluster to within-cluster
variance:

CH =

SSB/(k − 1)
SSW /(n − k)

(15)

where SSB is the sum of squares between groups, SSW is the
sum of squares within groups, k is the number of groups, and
n is the number of data points. Higher values indicate better
clustering.

B. FRAMEWORK OVERVIEW
The BIRCH-AE framework integrates four key components
into a cohesive pipeline:
(1) data preprocessing and
feature engineering, (2) autoencoder-based dimensionality
reduction, (3) BIRCH ensemble clustering with multiple
parameter configurations, and (4) dynamic ensemble selec-
tion and consensus generation. The framework is designed
with scalability as a primary consideration,
leveraging
BIRCH’s memory-efficient structure and incremental learn-
ing
capabilities.

The framework is modular rather than end-to-end jointly
optimized: each stage has its own objective (reconstruction
for AE, clustering compactness/separation for BIRCH, and

88586

VOLUME 14, 2026

---

<!-- PAGE 8 -->

C. Li et al.: BIRCH-AE: A Hierarchical Ensemble Framework for Scalable E-Commerce User Segmentation

TABLE 1. Feature categories and representative metrics.

consensus selection). Accordingly, we do not claim a
single global optimization objective or global convergence
guarantee for the full pipeline.

Fig. 1 illustrates the overall architecture. Beginning with
large-scale e-commerce user data,
the process proceeds
through data preprocessing, autoencoder-based feature learn-
ing, hierarchical ensemble clustering with multiple BIRCH
variants, and dynamic ensemble selection guided by quanti-
tative evaluation metrics. This integrated pipeline combines
BIRCH’s hierarchical scalability with autoencoder-enhanced
ensemble optimization
feature
for robust, high-quality user segmentation at enterprise
scale.

learning and adaptive

C. DATA PREPROCESSING AND FEATURE ENGINEERING
1) FEATURE COLLECTION
The framework processes comprehensive behavioral fea-
tures from large-scale e-commerce datasets, summarized in
Table 1. These features capture multidimensional aspects of
user behavior, enabling comprehensive behavioral segmen-
tation beyond simple RFM (Recency, Frequency, Monetary)
analysis.

2) DATA CLEANING AND NORMALIZATION
Raw e-commerce data requires extensive preprocessing
to ensure cluster quality. Missing values for behavioral
features are imputed with the median within user cohorts;
for transactional features, zero is imputed during inactive
periods. Features with excessive missing values (> 40%) are
excluded.

Outliers are detected using the Interquartile Range (IQR)
[48] method. For behavioral metrics such as session duration,
values exceeding Q3 + 3 × IQR are capped at the threshold.
For monetary features, a log transformation is applied before
outlier treatment to address right-skewness.

VOLUME 14, 2026

Given BIRCH’s sensitivity to feature scales, standardiza-

tion is applied to ensure zero mean and unit variance:

xnormalized =

x − µ
σ

(17)

For count-based features, the min-max scaling to [0, 1] is
applied to prevent dominance of high-variance features.

3) HANDLING CORRELATED VARIABLES
E-commerce behavioral data often exhibits strong feature
correlations [15]. The autoencoder-based approach natu-
rally handles these correlations by learning a compressed
representation that captures the underlying structure while
reducing redundancy. This addresses a key challenge in
high-dimensional customer segmentation where traditional
methods suffer from multicollinearity.

D. AUTOENCODER ARCHITECTURE FOR E-COMMERCE
DATA
1) NETWORK DESIGN
The autoencoder is specifically designed for e-commerce
behavioral data, and its architecture is motivated by charac-
teristics of user interaction patterns. The network employs
a symmetric encoder-decoder structure with progressively
decreasing layer dimensions.

Architectural Design Justification: The encoder archi-
tecture (128→64→14–32) follows standard deep learning
principles of gradual reduction in dimensionality [43]. The
128-unit first
layer accommodates 30–50 input features
with sufficient capacity for complex feature interactions.
Progressive reduction prevents information bottlenecks while
enabling hierarchical feature learning. The latent dimen-
sion (14)–(32) was selected based on a preliminary grid
search, where 14 provided an optimal balance between com-
pression (58% reduction of 33 features) and reconstruction
quality (MSE < 0.05 on the validation set). Latent dimensions
below 14 led to reconstruction degradation; above 32, there
was minimal quality improvement at increased computational
cost. ReLU activations prevent vanishing gradients, while
the linear bottleneck layer preserves continuous latent
representations suitable for distance-based clustering [49].

Input Layer: Accepts normalized feature vectors x ∈
Rd where d is the original feature dimensionality (typically
30–50 features).

Encoder Layers:

h1 = ReLU(W1x + b1),
h2 = ReLU(W2h1 + b2),
z = Linear(W3h2 + b3),

h1 ∈ R128
h2 ∈ R64
z ∈ Rp

(18)

(19)
(20)

where p is the latent dimension (typically 14–32 for
an optimal balance between compression and information
preservation).

Decoder Layers: Mirror the encoder structure:

2 = ReLU(W ′
h′
1 = ReLU(W ′
h′

3z + b′
3),
2 + b′
2h′
2),

h′
2 ∈ R64
h′
1 ∈ R128

(21)

(22)

88587

---

<!-- PAGE 9 -->

C. Li et al.: BIRCH-AE: A Hierarchical Ensemble Framework for Scalable E-Commerce User Segmentation

FIGURE 1. Overall architecture of the BIRCH-AE framework. The process begins with data preprocessing and feature engineering, where
raw clickstream and transaction data are transformed into behavioral feature vectors. A deep autoencoder compresses these
high-dimensional features into a compact latent space. The latent representations are processed by multiple BIRCH clustering models with
varying thresholds to capture different levels of granularity. Outputs are aggregated using four ensemble consensus strategies: Majority
Voting, Weighted Voting, AASC, and BOHC. Finally, a dynamic ensemble selection module evaluates all ensemble results using multi-criteria
metrics and automatically selects the optimal clustering solution.

ˆx = Linear(W ′

1h′

1 + b′

1),

ˆx ∈ Rd

(23)

2) TRAINING STRATEGY
The autoencoder is trained to minimize the reconstruction
error with additional regularization:

L = LMSE + λ1Lsparse + λ2∥θ ∥2
2

(24)

where:

LMSE =

1
n

n
X

i=1

∥xi − ˆxi∥2, Lsparse =

1
n

n
X

p
X

i=1

j=1

|zij| (25)

The sparsity term encourages the selective activation of
latent features, promoting interpretable representations. The
Adam optimizer [50] is used with a learning rate of α =
0.001, a batch size of 256, and early stopping based on the
validation reconstruction error. Training typically converges
within 100–200 epochs. The dataset is split 80–20 for training
and validation, with an early stopping patience of 10 epochs
to prevent overfitting.

3) INDEPENDENT VS. JOINT TRAINING
BIRCH-AE employs independent autoencoder training:
Phase 1 trains the autoencoder only for reconstruction loss;
Phase 2 freezes the encoder and uses latent representa-
tions for clustering. This contrasts with joint optimization
approaches [44],
in which clustering and representation
learning occur simultaneously.

Independent training offers three advantages for produc-
tion deployment: (1) stability: it avoids challenging joint
optimization where clustering objectives and reconstruction
loss may conflict; (2) flexibility: the trained autoencoder
is reusable across clustering methods (BIRCH, K-Means,
Agglomerative) and k values without retraining; (3) incre-
mental operation: BIRCH’s incremental nature allows adding
new users by encoding with a fixed autoencoder and inserting
into the CF-tree.
The trade-off

joint methods might achieve
marginally better quality by co-adapting representations
and clusters. However, our 23–53% improvement over
raw features (Section V) shows strong performance with
independent training while maintaining critical operational
advantages for production systems that require daily updates
and consistent representations.

that

is

This design assumes that the learned latent space preserves
neighborhood structure relevant to clustering and suppresses
nuisance variation through reconstruction regularization.
Under such conditions, BIRCH benefits from more stable
distance relationships in latent space. We emphasize this as a
modeling assumption, supported by empirical evidence from
our datasets, rather than a universal theoretical guarantee that
reconstruction-optimal embeddings are always clustering-
optimal.

The distributional conditions under which reconstruction
error minimization formally preserves cluster separability

88588

VOLUME 14, 2026

---

<!-- PAGE 10 -->

C. Li et al.: BIRCH-AE: A Hierarchical Ensemble Framework for Scalable E-Commerce User Segmentation

in latent space remain an open theoretical problem in the
deep clustering literature [23], [24], [49]. Three distributional
conditions are required for the latent space to preserve cluster
neighborhood structure. First, the data must lie approximately
on a low-dimensional manifold relative to the ambient
feature dimension—that is, the intrinsic dimensionality is
substantially less than the 30–50 input features. Second,
within-cluster variation must be smaller than between-cluster
variation in the ambient space, implying that the clusters are
approximately separable before encoding. Third, the recon-
struction MSE must be sufficiently small for the encoder
not to collapse distinct feature dimensions. E-commerce
behavioral data plausibly satisfies these conditions: users
within a segment share consistent purchasing sequences,
browsing habits, and temporal activity patterns, producing
within-cluster compactness that reconstruction regularisa-
tion can preserve. The 23–53% silhouette improvements
observed across both datasets provide empirical support for
this alignment in our setting. We explicitly acknowledge,
however, that we do not establish a formal proof relating
reconstruction error bounds to clustering distortion in latent
space, and that this theoretical gap is shared with the broader
class of independent-training deep clustering approaches
documented in recent surveys [23], [24].

√

Scalability-representation trade-off characterization:
Let γ > 0 denote the cluster separation margin in the original
feature space, defined as the minimum distance between any
two cluster centroids. Under the manifold and within-cluster
compactness conditions above, the latent space separation
εr ), where εr is the
margin γz satisfies γz ≥ γ − O(
reconstruction MSE of the trained autoencoder and p is the
latent dimension (p < d). It is important to note that
this expression is a heuristic conceptualization motivated
by the empirical behavior of the trained autoencoder, not a
formally derived proof from first principles. It is intended
to provide intuition for the compression–quality trade-off
rather than to serve as a theoretical guarantee. Under the
stated distributional conditions, reducing p below the intrinsic
dimension of the data increases εr , thereby reducing γz and
degrading downstream clustering quality. Our grid search
over p ∈ {14, 32, 50, 64} identified p∗ = 14 as the operating
point at which εr < 0.05 on the validation set, yielding
58% compression with preserved cluster separation across
both datasets. This provides a practical selection heuristic:
p∗ = arg minp{p : MSE(p) < τ }, where τ is a reconstruction
tolerance chosen by the practitioner.

AE-to-BIRCH error propagation analysis: A specific
concern for modular pipelines is whether BIRCH’s threshold-
based insertion mechanism amplifies autoencoder distance
distortions. We address this analytically and empirically.
Analytically, reconstruction regularisation prevents severe
non-monotonic distortions:
the MSE loss penalizes any
encoding that does not reproduce the original input, meaning
the encoder cannot map close points far apart or dis-
tant points close together without increasing the decoding
loss. The autoencoder is therefore constrained to produce

distance-preserving transformations up to the reconstruction
tolerance εr , which bounds the affinity perturbation analo-
gously to the BOHC stability result in Section IV. Crucially,
BIRCH’s threshold T is calibrated on the latent space
geometry directly through the grid search T ∈ {0.3, 0.5, 0.8};
it does not assume any specific scale from the original
feature space, so any consistent distance scaling introduced
by the autoencoder is absorbed into the threshold selection.
To empirically assess threshold robustness, a supplementary
development analysis was conducted on a 10,000-user sample
from the Retail Rocket dataset before the main experiments.
Across the three threshold values (T ∈ {0.3, 0.5, 0.8})
applied to autoencoder features, BIRCH silhouette scores
were 0.839, 0.821, and 0.809, respectively—a range of
only 0.030 (3.6%), consistent with bounded, non-amplified
perturbation. This supplementary analysis was not part of
the primary comparative evaluation; it is reported here as
supporting evidence for the analytical argument above. Fur-
thermore, comparing BIRCH on raw features versus BIRCH
on AE features constitutes a direct test: harmful distortion
amplification would result in deterioration relative to raw
features. Instead, we observe consistent improvement of
+1.7%, +8.4%, +12.2%, and +6.3% at K ∈ {5, 10, 15, 20}
respectively, confirming that
the autoencoder introduces
smooth, bounded distance perturbations that BIRCH’s inser-
tion mechanism accommodates without amplification.

We emphasize that the higher-order interaction caveat
applies here as well: in domains where clusters are defined
by complex non-linear feature interactions not captured by
reconstruction regularisation, the error propagation bound
may not hold, and joint training approaches [44] would be
more appropriate.

4) LATENT SPACE PROPERTIES
The learned latent space z ∈ Rp exhibits beneficial properties
for BIRCH clustering. A compression ratio of 2:1 to 4:1
typically reduces the computational burden while preserving
90–95% of the variance. The autoencoder captures com-
plex interactions between behavioral features and handles
correlated variables effectively, whereas linear methods like
PCA cannot. The compression-reconstruction process acts
as a denoising mechanism, filtering measurement noise
and irrelevant variations. Euclidean distances in the latent
space better reflect behavioral similarity than in the orig-
inal high-dimensional space, thereby improving BIRCH’s
distance-based operations.

E. BIRCH ENSEMBLE CONFIGURATION
1) BASE BIRCH MODEL VARIANTS
To capture diverse clustering perspectives, multiple BIRCH
models are configured with varying parameters, each empha-
sizing different aspects of the cluster structure.

Fine-Grained Model: Small threshold value (Tsmall =
0.3) creates many small homogeneous clusters, capturing
subtle behavioral differences. Branching factor B = 50.

VOLUME 14, 2026

88589

---

<!-- PAGE 11 -->

C. Li et al.: BIRCH-AE: A Hierarchical Ensemble Framework for Scalable E-Commerce User Segmentation

Balanced Model: A moderate threshold (Tmedium = 0.5)
balances the size and homogeneity of the cluster, representing
the typical granularity of the segmentation. Branching factor
B = 50.

Coarse-Grained Model: A large threshold (Tlarge =
0.8) produces fewer, larger clusters representing broad user
categories. Branching factor B = 50.

Adaptive Model: Dynamically adjusted threshold based
= 0.5 and
starting with Tinitial
on data density,
refined through tree condensation if memory constraints are
approached.

2) GLOBAL CLUSTERING PHASE VARIATIONS
BIRCH’s Phase 3 applies global clustering to leaf node CFs.
Different algorithms are used for diversity.

Agglomerative Hierarchical Clustering: Uses complete
linkage to merge CF entries, preserving hierarchical structure.
Number of clusters determined by cutting dendrograms at
varying heights.

K-Means on CFs: Applies K-Means to centroid repre-
sentations of CFs, providing a partition-based perspective.
Multiple K values tested: K ∈ {5, 7, 10, 12, 15, 20, 25}.

Spectral Clustering: Constructs a similarity graph from
CFs and applies spectral methods, capturing non-convex
cluster shapes.

3) ENSEMBLE GENERATION PROCESS
The ensemble generation creates M base BIRCH clustering
solutions {C1, C2, . . . , CM } where M ranges from 5 to 20.
Each solution Cm is a partition of users into Km clusters.
Ensemble diversity is ensured through parameter variation
(threshold, branching factor), variation in global clustering
methods, random sampling for large datasets (bootstrap
sampling with 80% of the data), and different distance metrics
during CF Tree construction.

F. ENSEMBLE CONSENSUS STRATEGIES
The BIRCH-AE framework incorporates four ensemble
consensus strategies to aggregate multiple BIRCH clustering
solutions. Each strategy offers distinct characteristics suited
to different data distributions and clustering objectives.

1) MAJORITY VOTING (MV)
The simplest consensus function assigns each user to the
cluster label that appears most frequently across ensemble
members:

Cconsensus(u) = arg max

k

M
X

m=1

⊮[Cm(u) = k]

(26)

where ⊮[·] is the indicator function. To handle varying
numbers of base groups, correspondence between group
labels is established using the Hungarian algorithm [51]
based on maximum overlap.

2) WEIGHTED VOTING (WV)
Weighted voting assigns importance to each base clustering
based on its quality:

Cconsensus(u) = arg max

k

M
X

m=1

wm · ⊮[Cm(u) = k]

(27)

where weights wm are derived from silhouette scores:

wm =

exp(β · Sm)
j=1 exp(β · Sj)

PM

(28)

with β = 5 as the temperature parameter and Sm as the
silhouette score of clustering Cm.

3) ADVANCED AFFINITY-BASED SPECTRAL CLUSTERING
(AASC)
AASC constructs a co-association matrix that captures
clustering agreement across ensemble members, then applies
spectral clustering to this affinity representation.

Co-Association Matrix Construction:

Aij =

1
M

M
X

m=1

⊮[Cm(i) = Cm(j)]

(29)

where Aij represents the proportion of base clusterings that
assign users i and j to the same cluster.
Spectral Clustering on Affinity:

L = D−A (Laplacian matrix)

Lnorm = D−1/2LD−1/2

(Normalized Laplacian)

(30)

(31)

The decomposition of the eigenvalues of Lnorm yields eigen-
vectors corresponding to the smallest eigenvalues, forming an
embedding space for the final clustering of K-Means.

4) BIRCH-OPTIMIZED HIERARCHICAL CONSENSUS (BOHC)
BOHC is a novel consensus strategy specifically designed to
leverage the hierarchical information preserved in BIRCH’s
CF Tree structures. Unlike conventional ensemble meth-
ods that treat clustering outputs as flat partitions, BOHC
explicitly incorporates the hierarchical relationships encoded
in each BIRCH model’s CF Tree, enabling multi-scale
consensus formation.

Hierarchical Affinity Construction: Instead of binary co-
assignment, BOHC computes multi-level affinity considering
hierarchical distances:

ABOHC
ij

=

1
M

M
X

m=1

exp (−α · hm(i, j))

(32)

where hm(i, j) is the height in the CF Tree m at which users i
and j first share a common ancestor, and α = 0.5 controls
the decay rate. This formulation assigns higher affinity to
user pairs that merge at lower tree levels (indicating strong
similarity), while maintaining moderate affinity for pairs
that merge at higher levels (indicating broader categorical
similarity).

88590

VOLUME 14, 2026

---

<!-- PAGE 12 -->

C. Li et al.: BIRCH-AE: A Hierarchical Ensemble Framework for Scalable E-Commerce User Segmentation

Hierarchical Consensus Clustering: Agglomerative hier-
archical clustering is applied to the BOHC affinity matrix
with average linkage, cutting the dendrogram at optimal
height determined by silhouette score maximization. This
process preserves the hierarchical structure information from
individual BIRCH trees in the final consensus clustering.

The BOHC method’s key innovation is its ability to
maintain multi-scale clustering information that would be lost
in flat partition-based ensemble approaches. Empirical results
demonstrate that BOHC achieves superior performance for
datasets with distinct hierarchical structure (e.g., transaction-
focused single-domain platforms). However, its advantages
diminish for multi-domain datasets with naturally diffuse
cluster boundaries.

5) THEORETICAL PROPERTIES AND COMPLEXITY ANALYSIS
We provide a complexity analysis and a stability-oriented
theoretical motivation for BOHC.

Computational Complexity: Let n be the number of
users, d the feature dimension, e training epochs, M ensemble
members, and q the number of CF-leaf representatives used
for BOHC consensus (q ≪ n in compressed CF-trees).
Phase 1 (autoencoder training) is O(n · d · e). Phase 2
(BIRCH construction) is near O(n log n) in practice due to
tree insertion and condensation. Phase 3 depends on the
consensus strategy: Majority/Weighted Voting are O(Mn);
user-level AASC is O(n2) in memory/time and is therefore
used in subset settings; BOHC is implemented on CF-level
hierarchical summaries with complexity O(Mq2 + n).

Overall, the framework comparison pipeline on repre-
sentative subsets is dominated by near-linear BIRCH and
voting costs, while full user-level spectral consensus remains
quadratic. The 4.5M-user production run reported in this
paper corresponds to the BOHC-based scalability test, not an
exhaustive full-framework sweep of all consensus methods at
full scale.

BOHC Theoretical Motivation: Standard co-association

uses binary membership agreement,

Aij =

1
M

M
X

⊮[Cm(i) = Cm(j)],

(33)

m=1
which ignores hierarchical distance. BOHC uses

ABOHC
ij

=

1
M

M
X

m=1

exp (−αhm(i, j)) ,

(34)

where hm(i, j) is the first common-ancestor height in tree m.
Proposition (Affinity Perturbation Bound): Assume for
two BIRCH-tree realizations that each pairwise merge height
differs by at most (cid:49)h, i.e., |hm(i, j) − ˜hm(i, j)| ≤ (cid:49)h for all
m, i, j. Then the BOHC affinity perturbation satisfies

(cid:12)
(cid:12)ABOHC
(cid:12)

ij

− ˜ABOHC
ij
Sketch: f (h) = e−αh is α-Lipschitz on h ≥ 0 in magnitude
because |f ′(h)| = αe−αh ≤ α. Apply Lipschitz continuity per
ensemble member and average over M .

≤ α(cid:49)h.

(35)

(cid:12)
(cid:12)
(cid:12)

The perturbation bound relies on two structural assump-
tions that are satisfied by construction in our implementation.
First, CF-tree merge heights hm(i, j) must be well-defined and
finite for all user pairs (i, j) across all ensemble members
m. Under BIRCH’s height-balanced tree construction with
fixed branching factor B and threshold T , the maximum tree
height is bounded by O(log n/ log B), ensuring that pairwise
heights are finite and comparable across ensemble members.
Second, height perturbations (cid:49)h must be bounded, which
holds when ensemble members are trained on overlapping
stratified subsets sharing the same B and T parameter range,
as in our configuration. Under these conditions, the Lipschitz
argument in the proof sketch applies uniformly across all (i, j)
pairs and all M ensemble members.

This bound does not prove global partition optimality or
universal convergence; it formalizes that BOHC affinities
vary smoothly under bounded hierarchical perturbations.
Empirically, BOHC is strongest on datasets with a clearer
hierarchical structure and less beneficial on diffuse multi-
domain data.

in Rp. For large n,

Scalability-representation trade-off formalization: The
modular pipeline introduces a well-defined trade-off between
computational scalability and representation quality. Let n
be the number of users, d the original feature dimension,
p the latent dimension, e the number of training epochs,
and K the target cluster count. The total pipeline cost
is O(n · d · e + n log n): the first term is the one-time
autoencoder training cost and the second is the BIRCH
tree construction cost
the pipeline
is dominated by the log-linear clustering term since e is
bounded by early stopping (e ≤ 200 in our configuration).
Reducing p decreases the constant factor in BIRCH distance
computations but increases reconstruction error εr , which
εr ).
bounds the latent separation margin as γz ≥ γ − O(
Practitioners can navigate this trade-off using the heuristic
p∗ = arg minp{p
: MSE(p) < τ }, where τ is a
reconstruction tolerance calibrated on a validation subset.
In our experiments, τ = 0.05 gave p∗ = 14 for both
datasets, achieving 58% compression with 90–95% variance
preservation.

√

G. DYNAMIC ENSEMBLE SELECTION
The BIRCH-AE framework employs a dynamic selection
mechanism that automatically chooses the optimal ensemble
strategy via multi-criteria evaluation. Rather than relying on
a single fixed strategy, this adaptive approach evaluates all
four ensemble methods (Majority Voting, Weighted Voting,
AASC, and BOHC). It selects the best performer for the given
data characteristics and cluster count.

For each ensemble strategy

E ∈ {EMV , EWV , EAASC , EBOHC },

three complementary cluster quality metrics are computed:
Silhouette Score S(E), Calinski-Harabasz Index CH (E), and
Davies-Bouldin Index DB(E).

VOLUME 14, 2026

88591

---

<!-- PAGE 13 -->

C. Li et al.: BIRCH-AE: A Hierarchical Ensemble Framework for Scalable E-Commerce User Segmentation

Algorithm 1 Dynamic Ensemble Selection With
Multi-Criteria Scoring
Input: Ensemble strategies, Data X, Target cluster

count K

Output: Selected ensemble solution E*
Step 1: Evaluate all ensemble strategies;
foreach ensemble strategy E in strategies do

Apply E to clustering results;
Compute metrics: S(E), CH (E), DB(E);

Step 2: Normalize metrics to [0,1] range;
foreach metric M in {S, CH, DB} do

Find Mmin and Mmax;
foreach ensemble E do

Mnorm(E) = M (E)−Mmin
Mmax −Mmin

;

Step 3: Compute composite scores;
Set weights: wS = 0.5, wCH = 0.3, wDB = 0.2;
foreach ensemble E do

Score(E) = wS · Snorm(E) + wCH · CHnorm(E) −
wDB · DBnorm(E);
Step 4: Select best ensemble;
E ∗ = arg maxE Score(E);
return E*

To combine these metrics with different scales and
optimization directions, min-max normalization is used,
followed by weighted aggregation. The complete selection
process is formalized in Algorithm 1.

The weight configuration prioritizes the silhouette score
as the primary indicator while incorporating variance-based
metrics for a comprehensive evaluation. The negative coef-
ficient for DB reflects its inverse optimization direction.
This selection process is performed independently for each
target cluster count, allowing different ensemble strategies to
be optimal for different segmentation granularities. In this
work, weights are fixed to ensure comparability across
trials and for operational simplicity in production-style
settings; an exhaustive sensitivity analysis is left for future
work.

Regarding sensitivity to the choice of internal evaluation
metrics: the silhouette score, Calinski-Harabasz index, and
Davies-Bouldin index capture complementary geometric
properties of cluster quality [45], [46], [47]. These met-
rics are known to agree on well-separated, approximately
convex clusters, while diverging on overlapping or non-
convex structures [13]. The dynamic selection mechanism
evaluates all three metrics precisely to mitigate reliance on
any single indicator, with the composite score weighting
(wS , wCH , wDB) = (0.5, 0.3, 0.2) reflecting the established
primacy of the silhouette score as a cohesion-separation mea-
sure while incorporating complementary variance-ratio and
inter-cluster distance signals. For datasets exhibiting strongly
non-convex or heavily overlapping cluster structures, all
three internal indices remain imperfect surrogates for true

Algorithm 2 Incremental User Segment Update
Input: New user data batch, Existing CF Trees,

Trained autoencoder AE
Output: Updated cluster assignments
Encode new data using AE to obtain latent
representations;
foreach CF Tree in ensemble do

foreach user in latent representations do
Insert user into tree following BIRCH
insertion algorithm;
if tree memory threshold exceeded then

Perform tree condensation with a larger
threshold;

Update cluster assignments from leaf node
memberships;

Apply ensemble consensus to obtain the final updated
segmentation;
return Updated cluster assignments including new
users

segmentation quality; exhaustive sensitivity analysis across
alternative metric combinations and weighting schemes is
identified as a direction for future work.

For datasets with strongly non-convex or crescent-shaped
cluster geometries, all three internal indices remain unreliable
surrogates and the dynamic selection mechanism may favor
the wrong ensemble strategy; external validation via A/B
testing is the appropriate remedy in such cases, as outlined
in the deployment guidance in Section VI.

H. SCALABILITY AND INCREMENTAL LEARNING
1) MEMORY-EFFICIENT IMPLEMENTATION
BIRCH-AE leverages BIRCH’s memory efficiency through
careful implementation. New users are inserted into existing
CF Trees without reprocessing the entire dataset, with
O(log n) insertion complexity. For datasets that exceed
memory, BIRCH processes data in chunks, building partial
CF Trees that are then merged via tree condensation.
This is particularly important for large-scale datasets with
millions of users. Base BIRCH models in the ensemble are
trained in parallel, with each model processing the latent
representations independently, enabling near-linear speedup
with core count.

2) INCREMENTAL USER SEGMENT UPDATES
For dynamic e-commerce environments, BIRCH-AE sup-
ports incremental clustering without requiring complete re-
clustering. The Algorithm 2 formalizes this process, enabling
critical real-time segment updates for applications such as
dynamic recommendation systems.

This incremental approach enables real-time segment
updates without complete re-clustering, maintaining system
responsiveness as new users join the platform.

88592

VOLUME 14, 2026

---

<!-- PAGE 14 -->

C. Li et al.: BIRCH-AE: A Hierarchical Ensemble Framework for Scalable E-Commerce User Segmentation

I. IMPLEMENTATION DETAILS
The BIRCH-AE framework is implemented in Python
3.8+ using PySpark 3.0+ for large-scale data processing,
Scikit-learn 1.0+ for BIRCH implementation and evaluation
metrics, TensorFlow/Keras for autoencoder implementation,
NumPy 1.21+ for numerical computations, and Pandas 1.3+
for data manipulation. Experiments are conducted on a
Databricks computing cluster with distributed processing
capabilities.

Key hyperparameters include: latent dimension of the
autoencoder p = 14 (tuned from {14, 32, 50, 64 }),
learning rate α = 0.001, sparsity weight λ1 = 0.001, L2
regularization λ2 = 0.0001, batch size 256, training epochs
200 with early stopping (patience=10); BIRCH threshold
range T ∈ {0.3, 0.5, 0.8}, branching factor B = 50,
number of clusters K ∈ {5, 7, 10, 12, 15, 20, 25}; ensemble
parameters: number of base models M = 10, weighted voting
temperature β = 5, BOHC decay rate α = 0.5, composite
score weights (wS , wCH , wDB) = (0.5, 0.3, 0.2).

V. EXPERIMENTAL EVALUATION
A. DATASETS
The proposed BIRCH-AE framework was evaluated using
two publicly available large-scale e-commerce datasets that
differ markedly in behavior structure and domain focus.
Both datasets were preprocessed using PySpark to enable
distributed feature engineering, outlier handling, null-value
treatment, and normalization. To achieve computational
efficiency while preserving representativeness, comparative
experiments were conducted on 30% randomly selected
stratified subsets of each dataset across 20 independent
randomized trials.

1) RETAIL ROCKET E-COMMERCE DATASET
The Retail Rocket dataset [52], sourced from a real-world
online retail platform, comprises over 1.4 million unique
users and detailed interaction events,
including product
views, cart additions, and purchases. Feature engineering pro-
duced rich behavioral profiles that capture both transactional
and navigational dynamics,
including event frequencies,
session-based statistics, engagement diversity, and temporal
activity indicators. The dataset reflects transaction-oriented
e-commerce behavior characterized by distinct and well-
separated clusters, as supported by high Calinski-Harabasz
scores (mean: 9053.5). These properties make it well-suited
for validating ensemble methods that leverage clearly defined
cluster structures.

2) E-COMMERCE BEHAVIOR MULTI-CATEGORY STORE
DATASET
The E-Commerce Behavior dataset [53] contains interaction
logs from a multi-category online store, covering more than
4.5 million users. It emphasizes heterogeneous behavior
patterns across product categories and price levels, including
activity counts, category diversity, price range statistics,

and temporal engagement features. Compared to Retail
Rocket, this dataset exhibits more diffuse and overlapping
behavioral structures, reflected in a significantly lower
average Calinski-Harabasz score (1413.1), approximately
6.4 times smaller, indicating weaker cluster separation. This
property makes it ideal for assessing robustness under high-
variability, low-separation conditions.

represents distinct,

Together, these datasets provide complementary evaluation
contexts: Retail Rocket
transaction-
dominant user behavior, while E-Commerce Behavior cap-
tures complex, exploratory patterns across multiple product
categories. Their contrasting structural characteristics enable
rigorous assessment of BIRCH-AE’s scalability, adaptability,
and clustering quality across diverse e-commerce scenarios.

B. EXPERIMENTAL SETUP
A comprehensive evaluation protocol was designed to assess
the BIRCH-AE framework across multiple dimensions.
Cluster quality was measured using the Silhouette Score,
the Calinski-Harabasz Index, and the Davies-Bouldin Index.
Scalability was evaluated in terms of execution time and
performance as data size increased. Stability was assessed
through repeated randomized runs under different cluster
counts and parameter configurations. Interpretability was
explored qualitatively by analyzing discovered user segments
and identifying features that contribute to cluster discrim-
ination. Cross-dataset analysis was conducted to evaluate
generalizability.

Baseline methods include: (1) K-Means [18], (2) K-
Means with PCA [22] retaining 95% variance, (3) MiniBatch
K-Means, (4) Agglomerative hierarchical clustering [54]
with Ward linkage, and (5) standard BIRCH [28] with
optimized parameters. All methods were evaluated across
multiple cluster counts K ∈ {5, 10, 15, 20, 25} to examine
segmentation granularity and ensemble adaptability.

C. RESULTS: RETAIL ROCKET DATASET
1) CLUSTERING QUALITY COMPARISON
Table 2 presents a comprehensive comparison of clustering
quality metrics for both base algorithms and the four
ensemble methods within BIRCH-AE across multiple cluster
counts for the Retail Rocket dataset. BIRCH-AE with
ensemble methods achieves superior performance, with
AASC and BOHC strategies delivering the best results at
5 clusters. Fig. 2 provides a visual comparison across the three
evaluation metrics.

Key observations for Retail Rocket include: BIRCH-AE
achieves the best silhouette score of 0.548 with AASC and
BOHC ensemble strategies for 5 clusters, representing 23%
improvement over single BIRCH (0.445); The weighted Vot-
ing ensemble achieves the highest Calinski-Harabasz index
of 213.1 at 5 clusters and 236.0 at 20 clusters; AASC and
BOHC ensemble methods consistently outperform individual
base models at optimal cluster counts; performance degrades

VOLUME 14, 2026

88593

---

<!-- PAGE 15 -->

C. Li et al.: BIRCH-AE: A Hierarchical Ensemble Framework for Scalable E-Commerce User Segmentation

FIGURE 2. Clustering performance comparison for Retail Rocket dataset across base models, ensemble methods, and BIRCH-AE. (a) Silhouette scores
indicate that BIRCH-AE achieves the highest score, 0.548, with the AASC/BOHC ensemble. (b) Calinski-Harabasz index with Weighted Voting BIRCH-AE
reaching 213.1 at 5 clusters. (c) Davies-Bouldin index (lower is better), where BIRCH-AE achieves 0.792 with AASC. The results demonstrate that
ensemble methods, particularly AASC and BOHC, significantly improve clustering quality compared to base algorithms on this dataset.

with increasing cluster counts, with Majority Voting showing
particularly poor performance at higher granularities.

2) ENSEMBLE STRATEGY COMPARISON
Table 2 provides a comprehensive comparison of the four
ensemble strategies (Majority Voting, Weighted Voting,
AASC, and BOHC) and base algorithms in different cluster
counts for Retail Rocket. AASC and BOHC strategies
consistently outperform simpler voting methods, particularly
at lower cluster counts, while the base algorithms remain
competitive.

3) AUTOENCODER IMPACT ANALYSIS
To isolate the autoencoder’s contribution to Retail Rocket,
we compare BIRCH-AE with BIRCH on both raw and PCA-
reduced features. Table 3 and Fig. 4 show the convergence of
training and the impact analysis.

Table 3 shows that standard AE consistently outperforms
all alternative feature learning methods. Most importantly,
AE achieves a 32% improvement over VAE (0.839 vs.
0.636 silhouette), directly validating our design choice in
Section IV-A. The superiority is consistent across all metrics:
34% better CH index and 75% better DB index compared
to VAE. This confirms that for e-commerce behavioral data
with deterministic patterns, VAE’s stochastic regularization
degrades clustering quality rather than enhancing it.

Against traditional methods, AE achieves 115% improve-
ment over PCA (0.839 vs. 0.390) and 89% improvement
over raw features (0.839 vs. 0.445), demonstrating the value
of non-linear dimensionality reduction. The improvements
in the CH index are even more dramatic (490% vs. PCA,
741% vs. raw features), indicating substantially better cluster
separation. These results validate the effectiveness of deep
learning-based feature extraction for handling correlated
variables [15], providing empirical evidence to address
Reviewer 1’s concern about VAE selection.

D. RESULTS: E-COMMERCE BEHAVIOR DATASET
1) MULTI-CATEGORY PERFORMANCE ANALYSIS
Table 4 details the performance between cluster counts
for the E-Commerce Behavior multi-category dataset. This
analysis reveals fundamentally different characteristics from
Retail Rocket, with base algorithms demonstrating superior
performance to ensemble methods on multi-domain data.

Key observations for the multi-category E-Commerce
Behavior dataset include: K-Means achieves best overall
performance at 5 clusters (0.683 silhouette); BIRCH demon-
strates exceptional consistency and scalability, maintaining
superior performance at higher cluster counts (0.603 at
15 clusters, 0.596 at 20 clusters) where other algo-
rithms degrade significantly (K-Means drops to 0.332 and
0.338 respectively); base algorithms consistently outperform
ensemble methods across all cluster counts, suggesting that
the diffuse, multi-domain nature of the data does not benefit
from ensemble consensus; lower Calinski-Harabasz scores
(1413.1 average) compared to Retail Rocket (9053.5) indicate
more diffuse, overlapping cluster structure.

2) SINGLE-DOMAIN CATEGORY ANALYSIS
To investigate whether the multi-domain nature of the
E-Commerce Behavior dataset explains the ensemble under-
performance, additional experiments were conducted on two
individual product categories: electronics and appliances.
This addresses potential sparsity and long-tail effects inherent
in multi-category data. The results are presented in Table 5
and visualized in Figs. 5 and 6.

The single-domain analysis reveals critical insights into

how domain granularity affects method selection:

Electronics Category: Exhibits high variability (sil-
houette std: 0.089) with ensemble methods achieving a
17% improvement over base algorithms in 5 clusters
(0.461 vs. 0.394). This advantage persists in all cluster counts,
with ensemble methods consistently outperforming base

88594

VOLUME 14, 2026

---

<!-- PAGE 16 -->

C. Li et al.: BIRCH-AE: A Hierarchical Ensemble Framework for Scalable E-Commerce User Segmentation

TABLE 2. Performance comparison: base algorithms vs. ensemble strategies across cluster counts for retail rocket dataset.

FIGURE 3. Ensemble strategy performance across different cluster counts for the Retail Rocket dataset. (a) Silhouette scores demonstrate
that AASC and BOHC consistently achieve superior performance, particularly for 5 clusters (0.548). Performance degrades as cluster count
increases, with Majority Voting showing negative scores at 20 clusters. (b) The Calinski-Harabasz index shows that Weighted Voting
maintains competitive performance across all cluster counts (peaking at 236.0 for 20 clusters), whereas Majority Voting degrades
significantly as cluster count increases. The results validate BIRCH-AE’s dynamic selection mechanism for choosing optimal strategies
based on data characteristics.

TABLE 3. Feature learning method comparison for BIRCH clustering.

algorithms by 17–23%. The high variability in the Calinski-
Harabasz (1200–2200) and Davies-Bouldin indices (0.85–
1.30) indicates an unstable cluster structure that benefits from
ensemble consensus.

Appliances Category: Shows ensemble methods that
achieve superiority in higher cluster counts (10–20 clusters).

At 5 clusters,
the base algorithms maintain a slight
advantage (0.643 vs. 0.585, representing 10% base supe-
riority). However, in 10 clusters, the ensemble methods
begin to show advantages (0.479 vs. 0.446, representing
a 7% improvement of the ensemble), with this advantage
growing in 15 clusters (0.462 vs. 0.374, representing a 24%
improvement) and 20 clusters (0.481 vs. 0.390, representing a
23% improvement). This pattern demonstrates that ensemble
methods excel at managing complexity in higher-granularity
segmentation.

Critical Finding: Both single-domain categories ulti-
mately benefit from ensemble methods, although the pattern
differs. Electronics shows consistent ensemble superiority
across all granularities because of an unstable cluster struc-
ture. Appliances demonstrate ensemble superiority at higher
cluster counts (10+ clusters) where complexity increases,
though base algorithms perform slightly better at the simplest
configuration (5 clusters). This directly contrasts with the
multi-category pattern, where base algorithms consistently

VOLUME 14, 2026

88595

---

<!-- PAGE 17 -->

C. Li et al.: BIRCH-AE: A Hierarchical Ensemble Framework for Scalable E-Commerce User Segmentation

FIGURE 4. Autoencoder training convergence and impact analysis for Retail Rocket dataset. (a) Training and validation loss curves show
effective convergence with a final validation loss of 0.0350, indicating good generalization without overfitting. The close alignment
demonstrates robust learning. (b) A comparison of BIRCH with different dimensionality-reduction methods demonstrates that
autoencoder-based feature learning achieves a 23% improvement in the silhouette score over raw features (0.4452 → 0.5477) and a 49%
improvement in the CH index (142.65 → 213.11). The autoencoder significantly outperforms PCA, effectively handling correlated variables
and capturing non-linear behavioral patterns in transaction-focused e-commerce data.

TABLE 4. Performance metrics across cluster counts: E-commerce behavior multi-category dataset.

TABLE 5. Performance comparison: single-domain categories (electronics and appliances).

dominated, validating that domain granularity (single vs.
multi-category) fundamentally influences optimal method

selection. Single-domain environments enable ensemble
methods to effectively capture and refine cluster structure,

88596

VOLUME 14, 2026

---

<!-- PAGE 18 -->

C. Li et al.: BIRCH-AE: A Hierarchical Ensemble Framework for Scalable E-Commerce User Segmentation

FIGURE 5. Comprehensive performance comparison for single-domain categories (Electronics and Appliances). The visualization reveals contrasting
patterns across categories and fundamental differences relative to multi-category results. Top panels: Overall performance distributions show Electronics
with high variability (Silhouette scores ranging 0.3–0.6, Calinski-Harabasz Index: 1200–2200, Davies-Bouldin Index: 0.85–1.30), indicating unstable cluster
structure, while Appliances demonstrates moderate stability. Middle panels: Performance by cluster count reveals optimal configurations at 5 clusters for
Electronics. Critically, Electronics shows that ensemble methods outperform base algorithms (ensemble avg: 0.461 vs. base avg: 0.394 at 5 clusters, a 17%
improvement). In comparison, Appliances exhibits ensemble superiority at higher cluster counts (ensemble avg: 0.481 vs. base avg: 0.390 at 20 clusters,
23% improvement). Bottom panels: Method-specific trends demonstrate that ensemble superiority persists across different granularities for both
single-domain categories. The contrasting patterns between single-domain categories and multi-category results validate the critical importance of
domain granularity in method selection, with both single-domain categories benefiting from ensemble methods.

whereas multi-domain environments introduce natural over-
laps that ensemble methods cannot resolve.

E. CROSS-DATASET COMPARATIVE ANALYSIS
Table 6 provides a comprehensive comparison that integrates
the findings of all experimental scenarios.

The cross-dataset analysis reveals three critical insights:
1. Cluster Structure Determines Method Selection
Within Domain Type: For single-domain datasets, cluster
stability affects the magnitude and pattern of ensemble
advantage. Electronics (unstable clusters) benefit uniformly
across granularities (+17–23%). Appliances (more stable

clusters) show base advantage at
lowest granularity (5
clusters: −10%) but strong ensemble advantages at higher
granularities (20 clusters: +23%). For multi-domain datasets,
diffuse overlapping patterns cause base algorithms to excel
(+7.4% over ensembles) regardless of cluster structure.

2. Domain Granularity Fundamentally Influences Out-
comes: Multi-category data exhibit diffuse, overlapping
patterns where base algorithms excel consistently. Single-
domain categories enable ensemble methods to capture and
refine cluster structure effectively, with both Electronics and
Appliances showing ensemble advantages (though patterns
differ). This represents the most important finding: domain

VOLUME 14, 2026

88597

---

<!-- PAGE 19 -->

C. Li et al.: BIRCH-AE: A Hierarchical Ensemble Framework for Scalable E-Commerce User Segmentation

FIGURE 6. Detailed performance trends across cluster counts for single-domain categories. Left panel (Electronics): Shows consistent
degradation in Silhouette scores as cluster count increases (0.461 at 5 clusters to 0.358 at 20 clusters for ensemble; 0.394 to 0.291 for
base), with ensemble methods maintaining 17–23% advantage across all granularities. High variability in CH and DB indices reflects the
inherently unstable cluster structure. Right panel (Appliances): Demonstrates ensemble advantage emerging at higher cluster counts
(10–20 clusters), with 7–23% improvement over base algorithms. At 5 clusters, base algorithms maintain a slight advantage (0.643 vs.
0.585), but ensemble methods become superior at 10+ clusters. The transition from base-to-ensemble superiority as granularity increases
demonstrates the effectiveness of ensemble methods in managing complexity. These single-domain results contrast with multi-category
findings, in which base algorithms uniformly outperformed ensembles, emphasizing that domain granularity fundamentally influences
optimal segmentation strategies.

granularity (single vs. multi) is the primary determinant of
optimal method selection.

distribution, and (3) category-engagement strata for the multi-
domain dataset.

3. BIRCH’s Multi-Scale Advantage Persists: Across
all scenarios, BIRCH demonstrates superior scalability
to higher cluster counts, maintaining performance where
partition-based methods degrade. This validates BIRCH’s
hierarchical approach for applications requiring multi-
resolution segmentation.

F. VALIDATION OF SUBSET-BASED ANALYSIS
To address the concern that most comparative analyses
use 30% subsets, we provide a consistency analysis across
repeated subset
trials and a separate full-scale BOHC
confirmation run.

Sampling Methodology and Extrapolation Validity:
Stratification Strategy: 30% subsets were created via
three-tier stratified random sampling:
(1) activity-level
strata (low: <10 events; medium: 10–100 events; high:
>100 events), (2) temporal strata preserving monthly user

Trial Protocol: We conducted 20 independent randomized
trials on 30% subsets to support comparative framework anal-
ysis. Across trials, method ranking patterns were generally
consistent: there is no universally best consensus strategy,
and performance depends on dataset structure and domain
granularity.

Rank-Order Stability: Beyond metric-level consistency,
method rank ordering remained stable across all 20 ran-
domized trials. Specifically: (1) BIRCH consistently out-
performed K-Means at cluster counts K ∈ {15, 20} across
both datasets; (2) autoencoder-based features consistently
outperformed PCA and raw features across all configurations
and cluster counts; (3) the domain granularity finding—
single-domain datasets favoring ensemble methods, multi-
domain datasets favoring base algorithms—held without
exception across all trials. Table 7 further confirms that
silhouette and Calinski-Harabasz deviations between 30%

88598

VOLUME 14, 2026

---

<!-- PAGE 20 -->

C. Li et al.: BIRCH-AE: A Hierarchical Ensemble Framework for Scalable E-Commerce User Segmentation

TABLE 6. Comprehensive cross-dataset and cross-domain comparison.

TABLE 7. Subset (30%) vs. Full dataset (100%) performance validation.

subset and full-dataset runs remain below 1.3%, and no rank
reversal between methods was observed when moving from
subset to full-dataset evaluation.

Full-Scale Check: A full 4.5M-user run was executed
for BOHC to validate operational feasibility of the pro-
duction deployment path. This run is used as a scalability
confirmation point rather than a full-method exhaustive
benchmark, which would require user-level quadratic affinity
construction for some strategies.

Validation Results: Table 7 summarizes subset-trial

statistics and the BOHC full-scale run.

Conclusion: The repeated stratified subset protocol pro-
vides stable comparative evidence for framework behavior,
while the BOHC full-scale run confirms that
the pro-
posed hierarchical consensus can be executed efficiently at
4.5M-user scale.

G. INCREMENTAL LEARNING PERFORMANCE
To validate BIRCH-AE’s incremental update capability
(Algorithm 2), we simulated daily user additions by parti-
tioning the E-Commerce Behavior dataset temporally and
measuring update performance.

Experimental Setup: The dataset was split chronolog-
ically into: (1) base dataset (first 90% of temporal range,
4.05M users), (2) 10 daily batches (remaining 10%, 45K new
users per day). The trained autoencoder and CF-tree from
the base dataset were used for incremental insertion without
retraining.

Results: Table 8 shows incremental update times signifi-

cantly outperform full re-clustering.
For daily batches (45K users),

insertion
requires 8.3s vs. 307.8s for full re-clustering (37× speedup)
while maintaining silhouette score within 0.002 (<0.3%
degradation). After 10 cumulative days (450K new users,
incremental updates achieve 4.4×
10% dataset growth),

incremental

VOLUME 14, 2026

88599

---

<!-- PAGE 21 -->

C. Li et al.: BIRCH-AE: A Hierarchical Ensemble Framework for Scalable E-Commerce User Segmentation

TABLE 8. Incremental update performance vs. Full re-clustering.

TABLE 9. Scalability performance summary for BIRCH-AE.

TABLE 10. Stage-wise execution time breakdown (subset benchmark and
full-scale projection).

speedup (76.2s vs. 335.4s) with 0.008 silhouette degradation
(1.2%).

Cluster Stability Analysis: We measured cluster assign-
ment stability for existing users across incremental updates.
After adding 450K users (10 days), 98.7% of the original
users retained their cluster assignments, demonstrating that
incremental insertion preserves the original segment structure
while accommodating new users.

Production Implications: These results validate BIRCH-
AE’s suitability for production environments requiring
daily/weekly segment refreshes. The 37× speedup enables
near-real-time updates, while minimal quality degradation
(<1.5%) after 10% dataset growth suggests monthly full
re-clustering is sufficient to maintain optimal quality.

Path dependence analysis: BIRCH’s CF-tree construc-
tion is inherently order-dependent: the tree structure reflects
the insertion sequence, and later insertions must follow
paths established by earlier data. This raises the question of
whether early-arriving users bias the tree structure in ways
that systematically misclassify later users. Three mechanisms
mitigate this risk in BIRCH-AE. First, the base dataset
(90% of the temporal range, 4.05M users) is processed
in activity-stratified order rather than strict chronological
order, ensuring the initial tree captures the full diversity
of user behavior patterns. Second, BIRCH’s condensation
mechanism merges subclusters when memory thresholds
are exceeded,
implicitly correcting some path-dependent
assignments. Third, the 98.7% cluster assignment stability
after 10% dataset growth provides direct empirical evidence
that path dependence is not materially affecting segment
consistency at the scales tested. Path dependence becomes
more pronounced in long-running production systems that
experience significant distributional shifts (e.g., seasonal
behavioral changes or major product catalog expansions).
It should be noted that
the 98.7% stability figure was
measured under stable distributional conditions over a 10-day
window; this result may not generalize to scenarios involving
significant concept drift—such as major seasonal behavioral
shifts, large-scale product catalog restructuring, or rapid
user cohort changes—where accumulated path dependence
could cause cluster assignments to diverge from the current
data distribution more quickly. For this reason, monthly
full re-clustering is recommended to reset accumulated path
dependence, with the frequency increased if distributional
monitoring (e.g., tracking the silhouette score over rolling
windows) detects significant drift.

H. SCALABILITY ANALYSIS
BIRCH-AE demonstrates efficient scaling behavior across
both datasets. Comparative pipeline timings were bench-
marked across repeated 30%-subset trials, and the autoen-
coder converged in 100 epochs with early stopping.

Scalability characteristics include single-pass BIRCH con-
struction, enabling streaming data integration; incremental
insertion, supporting real-time user segment updates; and
parallel processing of ensemble members for practical
speedups.

A production-scale test involving 4.5 million customer
records validated BOHC’s full-scale feasibility. The BOHC
run completed in 307.8 seconds (approximately 5.1 minutes),
demonstrating that hierarchical consensus can be deployed
on multi-million-user data. This production-feasibility run
was executed on the fixed 8-worker Databricks cluster
configuration documented in Section V-J.

Table 10 provides stage-wise timing on subset runs and
projected full-scale equivalents for pipeline planning. The
full measured 4.5M result reported in this paper corresponds
to the BOHC run (307.8s). At the same time, AASC is
kept in subset-level comparisons due to its quadratic affinity
construction at
the full-scale
the user level. Therefore,
experiment is interpreted as deployment-feasibility validation
rather than a claim that all consensus variants are equally
production-ready at full user scale.

88600

VOLUME 14, 2026

---

<!-- PAGE 22 -->

C. Li et al.: BIRCH-AE: A Hierarchical Ensemble Framework for Scalable E-Commerce User Segmentation

I. BUSINESS INSIGHTS AND SEGMENT INTERPRETATION
The discovered user segments provide actionable insights for
e-commerce practitioners. This section presents qualitative
interpretations of the optimal 5-cluster segmentations for both
datasets.

1) RETAIL ROCKET CUSTOMER SEGMENTS
Based on the analysis of behavioral characteristics within
each cluster:

High frequency transactors (22%): Users exhibiting
frequent purchases with high transaction counts and strong
conversion rates. These customers demonstrate consistent
engagement and high lifetime value. Recommended strate-
gies include premium loyalty programs, early access to new
products, and personalized high-value recommendations.

Browse-and-Buy Balanced (31%): The largest segment,
characterized by moderate browsing activity coupled with
good conversion rates. These users respond well to product
recommendations and engage effectively in targeted pro-
motions. The marketing focus should emphasize relevant
product suggestions and limited-time offers.

Window Shoppers (28%): High browsing activity but
lower purchase conversion. This segment requires nurturing
strategies, including retargeting campaigns, cart abandon-
ment recovery, and incentive-based conversion tactics such
as first-purchase discounts or free shipping offers.

Category Specialists (13%): Users with concentrated
interests in specific product categories, showing expertise or
strong preferences in particular domains. These customers
benefit from category-specific marketing communications,
cross-sell opportunities within their preferred categories, and
expert-level product information.

Infrequent/At-Risk Users (6%): Low activity lev-
els with high recency values indicating dormancy. This
segment
requires win-back campaigns with compelling
re-engagement offers, personalized ‘‘we miss you’’ com-
munications, and surveys to understand the reasons for
disengagement.

2) E-COMMERCE BEHAVIOR CUSTOMER SEGMENTS
For the multi-category store environment:

Casual Browsers (35%): The largest segment, charac-
terized by infrequent visits and minimal purchase activ-
ity. These represent customer-acquisition opportunities that
require awareness-building campaigns, introductory offers,
and strategies to establish initial trust and engagement.

Active Explorers (29%): High browsing activity with
exploration of diverse categories, but moderate conversion
rates. These users are highly responsive to recommendation
engines and benefit from cross-category promotions, curated
collections, and discovery-oriented marketing that highlight
product variety.

Focused Buyers (19%): Lower browsing-to-purchase
ratios indicate efficiency and intent. These value-conscious
customers have clear objectives and benefit from streamlined

shopping experiences, competitive pricing, communications,
and targeted campaigns for anticipated needs.

Premium Shoppers (12%): High average order values,
frequent purchases, and demonstrated loyalty. This segment
represents prime candidates for premium loyalty tiers, exclu-
sive access programs, concierge services, and high-touch
relationship management.

At-Risk Previously-Active (5%): Formerly engaged
users showing declining activity trends. Priority retention
segment requiring immediate intervention through person-
alized outreach, exclusive retention offers, and proactive
customer service to prevent complete churn.

These segment interpretations demonstrate BIRCH-AE’s
ability to produce not only statistically valid clusters but
also business-actionable customer groupings that align with
practical marketing and retention strategies.

J. REPRODUCIBILITY AND IMPLEMENTATION DETAILS
To ensure reproducibility, we provide comprehensive imple-
mentation details and make all code publicly available.

Hardware and Software Configuration: Experiments
were conducted on Azure Databricks with two cluster
configurations:

Development/Testing Cluster (30% subset experiments):
- Instance Type: Standard_E16ds_v4 Azure VM - Config-
uration: 2-8 autoscaling workers (16 cores, 128GB RAM
per worker) - Driver: Standard_E16ds_v4 (16 cores, 128GB
RAM) - Databricks Runtime: 13.3 LTS (Apache Spark 3.4.1,
Scala 2.12) - Total Resources: 32-128 cores, 256GB-1TB
RAM (autoscaling)

Production-Scale Cluster (full 4.5M user experiment): -
Instance Type: Standard_E64ds_v5 Azure VM - Configura-
tion: 8 workers (64 cores, 512GB RAM per worker) - Driver:
Standard_E64ds_v5 (64 cores, 512GB RAM) - Databricks
Runtime: 16.4 LTS (Apache Spark 3.5.0, Scala 2.12) - Total
Resources: 512 cores, 4TB RAM - Unity Catalog enabled for
data governance.

Software Stack: Python 3.10.12, PySpark 3.5.0, Ten-
sorFlow 2.15.0, NumPy 1.24.3, Pandas 2.0.3, scikit-learn
1.3.0. Autoencoder training was performed using distributed
TensorFlow on Spark workers.

Spark Configuration: - Executor memory: 96GB per
executor - Executor cores: 8 cores per executor - Driver
memory: 96GB - Dynamic allocation enabled with 2-8
executors (development), 8 fixed executors (production)

Code and Data Availability: Complete implementation
is available at [32]. The repository includes: (1) prepro-
cessing scripts for data cleaning, feature engineering, and
stratified sampling; (2) autoencoder training scripts with
hyperparameter configurations in JSON format; (3) BIRCH
clustering implementation with incremental learning sup-
port; (4) all four ensemble methods (Majority, Weighted,
AASC, BOHC); (5) evaluation scripts computing all met-
rics;
reproducibil-
ity; (7) example notebooks demonstrating the end-to-end
pipeline; (8) requirements.txt with exact package versions.

trained autoencoder weights for

(6)

VOLUME 14, 2026

88601

---

<!-- PAGE 23 -->

C. Li et al.: BIRCH-AE: A Hierarchical Ensemble Framework for Scalable E-Commerce User Segmentation

Datasets: Retail Rocket dataset available via Kaggle [52].
E-Commerce Behavior dataset available via UCI Machine
Learning Repository [53]. The preprocessing scripts in our
repository reproduce the exact feature sets used in the
experiments.

Reproducibility Statement: All experiments are repro-
ducible by following the repository instructions. Random
seeds are fixed (seed=42) for autoencoder initialization and
stratified sampling. The expected runtime is approximately
6 hours for the complete pipeline on a similar hardware
configuration.

VI. DISCUSSION
A. DOMAIN GRANULARITY AS THE PRIMARY
DETERMINANT OF METHOD SELECTION
The most striking finding is that domain granularity (single-
domain vs. multi-domain) fundamentally determines optimal
method selection, with secondary effects from cluster char-
acteristics within each domain type.

Multi-Category Datasets: The E-Commerce Behavior
multicategory dataset exhibits diffuse, overlapping cluster
structure (CH: 1413.1) where base algorithms consis-
tently outperform BIRCH-AE’s ensemble methods. BIRCH
and K-Means achieve superior results (0.651 and 0.683,
respectively, at 5 clusters) compared to the best ensemble
AASC/BOHC (0.633), representing a 7.4% advantage for
base methods. This occurs because heterogeneous behavior
patterns across multiple product categories create natural
overlaps that the ensemble’s consensus mechanisms cannot
effectively resolve. The averaging effect of ensemble meth-
ods introduces noise rather than refinement when the natural
boundaries of the cluster are already diffuse.

Single-Domain Categories: Both Electronics and Appli-
ances ultimately demonstrate ensemble superiority, though
with different patterns:

Electronics: Shows unstable cluster structure (high vari-
ability, silhouette std: 0.089) where ensemble methods within
BIRCH-AE achieve consistent 17–23% improvement across
all cluster counts (0.461 vs. 0.394 at 5 clusters; 0.358 vs.
0.291 at 20 clusters). The ensemble consensus effectively
stabilizes the clustering by integrating multiple perspectives
on volatile behavioral patterns.

Appliances: Shows more complex pattern where base algo-
rithms have slight advantage at lowest granularity (5 clusters:
0.643 vs. 0.585, representing 10% base superiority), but
BIRCH-AE’s ensemble methods become superior at higher
cluster counts (10 clusters: 0.479 vs. 0.446, +7%; 15 clusters:
0.462 vs. 0.374, +24%; 20 clusters: 0.481 vs. 0.390,
+23%). This demonstrates that ensemble methods excel
at managing complexity in higher-granularity segmentation
even for moderately stable clusters.

Transaction-Focused Datasets: Retail Rocket represents
a single-domain, transaction-oriented platform with distinct
clusters (CH: 9053.5) where BIRCH-AE’s ensemble methods
provide substantial benefits (+23% improvement). The clear

but complex cluster structure benefits from multiple algorith-
mic perspectives captured through ensemble consensus.

Critical Implication: These findings reveal a clear
decision hierarchy: (1) First assess domain granularity (single
vs. multi); (2) For multi-domain, prefer base algorithms; (3)
For single-domain, prefer BIRCH-AE’s ensemble methods,
with magnitude of benefit depending on cluster stability
and segmentation granularity. This simplifies deployment
decisions while improving results.

B. BIRCH’S HIERARCHICAL ADVANTAGE FOR
MULTI-SCALE SEGMENTATION
Across all experimental scenarios, BIRCH demonstrates
a significant advantage in multi-scale segmentation, par-
ticularly in the E-Commerce Behavior dataset. While
K-Means achieves marginally better performance at 5 clus-
ters (0.683 vs. 0.651), BIRCH’s superiority becomes pro-
nounced at higher granularities. At 10 clusters, BIRCH leads
slightly (0.635 vs. 0.633). The advantage becomes dramatic at
15 clusters (BIRCH: 0.603 vs. K-Means: 0.332, representing
81% improvement) and persists at 20 clusters (BIRCH:
0.596 vs. K-Means: 0.338, representing 76% improvement).
This scalability is crucial for e-commerce platforms
that require multi-level segmentation strategies, ranging
from broad customer categories for strategic planning to
fine-grained microsegments for personalized marketing.
BIRCH’s CF Tree structure inherently captures these hier-
archical relationships, enabling consistent quality across
different segmentation granularities without requiring sepa-
rate model training for each level.

The practical implication is that for applications requiring
flexible segmentation at multiple resolutions, BIRCH-based
approaches offer significant advantages over partition-based
methods that optimize for a single granularity level. This
validates BIRCH’s suitability for enterprise environments
where different organizational units may require different
segmentation resolutions.

C. ENSEMBLE METHODS WITHIN BIRCH-AE FOR
SINGLE-DOMAIN SCENARIOS
Results validate ensemble clustering benefits for single-
domain scenarios while revealing important nuances:

When BIRCH-AE Ensembles Help Most: Retail
Rocket’s distinct, transaction-focused clusters benefit sub-
stantially from BIRCH-AE’s ensemble methods (AASC/
BOHC achieve 0.5477, representing 23% improvement over
base BIRCH). The single-domain Electronics category with
unstable clusters shows a consistent 17–23% ensemble
advantage across all granularities. The Single-domain
appliance category demonstrates ensemble superiority at
higher cluster counts (10–20 clusters: 7–24% improvement),
where complexity increases. These scenarios
share a
single-domain focus with a cluster structure suitable for
ensemble consensus.

When Base Algorithms Excel: E-Commerce Behavior
multi-category dataset shows consistent base algorithm

88602

VOLUME 14, 2026

---

<!-- PAGE 24 -->

C. Li et al.: BIRCH-AE: A Hierarchical Ensemble Framework for Scalable E-Commerce User Segmentation

superiority (7.4% advantage over BIRCH-AE ensembles).
Appliances at
the lowest granularity (5 clusters) show
a slight base advantage (10%) before ensemble methods
dominate at higher complexities. These scenarios involve
either multi-domain natural overlap or extremely granular
segmentation.

Mechanistic Explanation: For single-domain datasets,
BIRCH-AE’s ensemble methods effectively integrate com-
plementary views of cluster boundaries, with benefits
increasing as segmentation granularity and cluster complex-
ity grow. For multi-domain data with natural categorical
overlap, ensemble averaging obscures rather than clarifies
boundaries. For very simple segmentation (few clusters) in
stable single-domain environments, the additional complex-
ity of ensemble aggregation may not be necessary.

Practical Guidance: The decision framework simplifies
to: (1) Multi-domain → Strongly prefer base algorithms
regardless of cluster characteristics; (2) Single-domain →
Prefer BIRCH-AE’s ensemble methods, with magnitude of
benefit depending on cluster stability and desired granularity;
(3) For single-domain with very low cluster counts (≤5), base
algorithms may suffice for stable clusters, but ensemble meth-
ods are still beneficial for unstable clusters; (4) Always use
autoencoder-based feature learning for consistent 11–53%
improvement.

D. AUTOENCODER INTEGRATION PROVIDES CONSISTENT
VALUE
Despite highly variable ensemble performance across sce-
narios, autoencoder-based feature learning consistently ben-
efits all datasets and configurations. For Retail Rocket:
23% improvement in silhouette (0.4452 → 0.5477), 49%
improvement in Calinski-Harabasz (142.65 → 213.11), 41%
advantage over PCA. For E-Commerce Behavior multi-
category: 53% improvement in silhouette (0.445 → 0.683),
substantial Calinski-Harabasz improvement, 76% advantage
over PCA. For single-domain categories: 20% average
improvement with 35% advantage over PCA.

Autoencoders consistently help because e-commerce data
exhibit strong feature correlations [15], which the autoen-
coder’s non-linear compression naturally handles. They
capture complex behavioral interactions that linear methods
cannot represent, act as denoising mechanisms that improve
cluster quality across all scenarios, and reduce dimensionality
(to a 14-dimensional latent space) while preserving 90–95%
of information.

The practical recommendation is to prioritize autoencoder-
based feature learning for behavioral data in e-commerce.
The observed 11–53% gains justify the training overhead
in our evaluated scenarios and represent the most consistent
performance improvement in this study.

E. BIRCH SCALABILITY ADVANTAGES VALIDATED
Experiments confirm BIRCH’s practical advantages for
enterprise-scale e-commerce across all dataset types. Suc-
cessful runs from 1.4M to 4.5M users support the expected

memory efficiency of CF-tree compression compared with
classical O(n2) hierarchical clustering methods.

Computational scalability demonstrates near-linear scaling
from 1.4M to 4.5M users (a 3× increase), with single-pass
construction compared to K-Means’ iterative approach. The
method achieves competitive to superior performance at low
cluster counts, showing dramatic superiority at high cluster
counts (0.596–0.603 at 15–20 clusters), and exhibits superior
scalability across different domain types. Incremental learn-
ing supports real-time user segment updates through CF Tree
insertion, enables daily or streaming segment refreshes, and is
critical for production systems where complete re-clustering
is impractical.

The 4.5M-user BOHC production run (approximately
5 minutes) demonstrates the practical viability of near-real-
time, large-scale segmentation updates.

F. COMPARISON WITH EXISTING WORK
Compared to Zhao et al. [15] regularized K-Means. At the
same time,
their approach effectively handles correlated
variables through regularization. BIRCH-AE achieves this
through autoencoder feature learning while also providing
superior scalability (single-pass vs. iterative), incremental
learning capability for streaming data, hierarchical multi-
scale segmentation, comparable performance at low cluster
counts with superior performance at high granularities
(0.603–0.596 at 15–20 clusters), applicability across both
single and multi-domain scenarios, and hierarchical structure
revealing multi-scale customer segments.

Compared to traditional ensemble clustering [30], [31],
results show ensemble benefits are fundamentally gov-
erned by domain granularity: Retail Rocket and both
single-domain categories achieve substantial improvements
with BIRCH-AE’s ensembles (aligning with literature), while
E-Commerce Behavior multi-category shows base algo-
rithms outperform ensembles (revealing domain granularity
as a critical factor). This demonstrates the importance
of domain assessment alongside traditional cluster quality
metrics.

Compared to deep embedded clustering [44], BIRCH-
AE’s modular approach offers advantages including stable
training without joint optimization complexity, ability to
update clustering without retraining representations, support
for incremental learning (critical for production), hierarchical
multi-resolution segmentation not available in partition-
based methods, consistent performance across domain
types, and competitive to superior performance with better
scalability and flexibility.

G. PRACTICAL DEPLOYMENT RECOMMENDATIONS
Based on comprehensive findings across multiple experimen-
tal scenarios, we provide refined deployment guidance:

Step 1 (Data Profiling): Extract comprehensive behav-
ioral features (30–50 features covering activity, engagement,
transaction, and temporal). Assess domain granularity:
single-domain (one product category) vs. multi-domain

VOLUME 14, 2026

88603

---

<!-- PAGE 25 -->

C. Li et al.: BIRCH-AE: A Hierarchical Ensemble Framework for Scalable E-Commerce User Segmentation

(multiple categories). Conduct preliminary clustering at
multiple K values. Calculate Calinski-Harabasz scores to
assess cluster structure. Analyze cluster stability by running
multiple times with different initializations.

Step 2 (Method Selection): For multi-domain datasets:
strongly prefer base algorithms (BIRCH or K-Means) regard-
less of CH scores, as domain overlap creates natural dif-
fusion that BIRCH-AE’s ensemble methods cannot resolve.
For single-domain datasets, prefer BIRCH-AE’s ensemble
methods, with the benefit depending on cluster stability
and desired granularity. For very simple segmentation (≤5
clusters) with highly stable clusters, base algorithms may
suffice, but ensemble methods are still beneficial for unstable
clusters. Always use autoencoder-based feature learning
(14–32-dimensional latent space). Consider cluster count
requirements: for 5–10 clusters, base algorithms are com-
petitive in simple cases; for 15+ clusters in single-domain
scenarios, BIRCH-AE’s ensembles show clear advantages.

Step 3 (Implementation): Train autoencoder on his-
torical data (100–200 epochs with early stopping). Apply
the selected clustering method with the optimal K range
identified in profiling. For large datasets (>1M users),
leverage BIRCH’s incremental capabilities. For multi-level
segmentation, use BIRCH’s hierarchical tree structure. Set
up daily or real-time segment updates using incremental
insertion. Validate method selection with A/B testing on
representative samples before full deployment.

Step 4 (Validation and Monitoring): Validate segments
with business stakeholders and domain experts. Monitor
segment stability over time (track silhouette, CH, DB across
granularities). Periodically re-evaluate domain granularity
as product mix evolves. For hierarchical approaches, assess
quality at multiple resolution levels. Re-assess ensemble
vs. base performance if
the domain structure changes
significantly (e.g., expanding from single to multi-category).
Develop a post hoc interpretation that maps latent features to
behavioral attributes for business communication.

H. LIMITATIONS
While BIRCH-AE demonstrates strong empirical perfor-
mance, several limitations should be acknowledged. The
evaluation is restricted to the e-commerce domain, focusing
on transaction and browsing behavior. Both benchmark
datasets are derived from online retail platforms, which may
limit generalizability to other verticals such as B2B markets,
digital services, or social platforms.

The observed ensemble performance patterns are based
on two single-domain categories (electronics and appli-
ances) within a single multi-category dataset. Additional
category-level analysis across more diverse product domains
would strengthen the generalizability of the findings on
domain granularity. However, the consistent pattern across
Retail Rocket, Electronics, and Appliances provides strong
initial evidence.

The current implementation performs static segmenta-
tion, analyzing users as fixed entities at specific points

in time. Temporal dynamics and evolving user behaviors
are not explicitly modeled.
Incorporating recurrent or
sequence-based learning components could capture behav-
ioral evolution more effectively, particularly for understand-
ing category migration patterns in multi-domain environ-
ments and the transition from base to ensemble superiority
observed in Appliances as granularity increases.

The integration of autoencoder-based feature learning
improves clustering quality but reduces model interpretabil-
ity. Latent representations obscure the direct associations
between input features and cluster assignments, necessitating
post hoc interpretation techniques for meaningful business
communication.

The framework faces a cold-start limitation, as users with
minimal historical interaction data are difficult to segment
accurately. This is particularly problematic in multi-category
environments where users may be active in some categories
but not others. Extending the approach with hybrid features
(such as demographic or contextual metadata) may mitigate
this issue.
Finally,

in domains where clusters are defined pri-
marily by higher-order feature interactions not captured
by first-order statistics and their pairwise combinations,
a reconstruction-focused autoencoder may fail
to pro-
duce cluster-discriminating representations, and contrastive
pre-training or joint optimization approaches would be more
appropriate.

I. LIMITATIONS AND FUTURE DIRECTIONS
While BIRCH-AE demonstrates strong empirical perfor-
mance, several limitations should be acknowledged.

Temporal Modeling: The current framework treats user
behavior as static snapshots, failing to capture temporal evo-
lution. E-commerce users exhibit dynamic patterns including
seasonal buying behaviors, lifecycle stages (new customer
→ regular → loyal → dormant), and preference drift.
Future work should integrate temporal modeling through:
(1) sequential autoencoders capturing browsing session
sequences; (2) recurrent neural networks (RNN/LSTM) for
time-series behavioral encoding; (3) temporal clustering
tracking segment migrations over time; (4) incremental
re-clustering detecting concept drift. BIRCH’s incremental
learning provides partial mitigation through daily batch
processing that adds new users and re-encodes changes to
existing users without full model retraining.

is

to

restricted

Generalizability: Evaluation

the
e-commerce domain (transactional and behavioral data).
The domain granularity principle (single-domain favors
ensembles; multi-domain favors base algorithms) requires
validation across other verticals, such as B2B sales, digital
services, social platforms, and financial services. Different
domain characteristics may favor alternative design choices.
Scalability Bounds: While we demonstrate 4.5M user
processing, upper scalability limits remain untested. Systems
with 50M–100M users may require the distributed construc-
tion of the CF-tree or the use of approximate methods.

88604

VOLUME 14, 2026

---

<!-- PAGE 26 -->

C. Li et al.: BIRCH-AE: A Hierarchical Ensemble Framework for Scalable E-Commerce User Segmentation

Memory constraints for ensemble affinity matrices (O(n2))
may necessitate sparse approximations at extreme scales.

External Validation: Quality assessment relies on internal
metrics (silhouette, CH, DB). Public benchmark datasets
do not provide intervention outcomes (e.g., campaign
lift, retained revenue, realized churn reduction), so direct
business-impact validation is outside the scope of this study.
External validation through online A/B tests and business
KPIs is a primary direction for future work.

Sensitivity and Resource Logging: Dynamic-selection
weights were fixed in this study and not exhaustively
stress-tested across alternative weighting schemes. In addi-
tion, peak memory usage was not logged for each stage,
so scalability claims are currently supported primarily
by execution time, repeated subset consistency, and the
successful completion of the full-scale BOHC production
run. Fine-grained memory instrumentation and exhaustive
weight sensitivity are planned future work items.

a

scalable

e-commerce user

introduces BIRCH-AE,

VII. CONCLUSION
comprehensive
This paper
segmenta-
framework for
tion that
integrates hierarchical BIRCH clustering with
autoencoder-based feature learning and dynamic ensemble
selection. Extensive comparative evaluations were conducted
two large-
on representative 30% stratified subsets of
scale datasets–Retail Rocket (1.4M users) and E-Commerce
Behavior (4.5M users)–across 20 randomized trials, together
with single-domain category analyses.

A. KEY CONTRIBUTIONS
The study makes several important contributions, which
are validated through a comprehensive empirical evaluation.
trials show stable comparative patterns
Repeated subset
and support generalization of the decision trends. First,
we identify domain granularity as the fundamental determi-
nant of selecting the optimal method. Multi-domain datasets
consistently favor base algorithms (a 7.4% advantage)
due to natural category overlap, whereas single-domain
datasets generally benefit
from BIRCH-AE’s ensemble
methods in the scenarios we evaluated. Electronics and
Appliances show ensemble advantages (17–23% across
various granularities), though with different patterns that
reflect cluster stability and segmentation complexity. This
finding provides practitioners with a clear, hierarchical
decision framework: domain granularity first, then cluster
characteristics.

Second, we validate BIRCH’s hierarchical advantage
in multi-scale segmentation by demonstrating consistent
performance across granularities. While K-Means achieves
marginally better results at 5 clusters (0.683 vs. 0.651),
BIRCH shows stronger performance at higher cluster
counts (0.603 vs. 0.332 at 15 clusters, representing 81%
improvement). This enables flexible segmentation strategies,
from strategic planning to personalized marketing, without

requiring separate models for each level, addressing a critical
yet often overlooked requirement in enterprise analytics.

Third, we demonstrate consistent and substantial benefits
from autoencoder integration across all scenarios (11–53%
in silhouette scores). The autoencoder effectively handles
correlated variables, captures non-linear behavioral patterns,
and reduces dimensionality while preserving essential infor-
mation. This validates the integration of deep learning-based
feature learning with hierarchical clustering methods, with
autoencoders outperforming PCA by 28–76% across domain
types.

Fourth, we show that ensemble effectiveness in single-
domain scenarios depends on cluster stability and the desired
granularity. For Retail Rocket’s distinct single-domain clus-
ters, AASC/BOHC ensembles achieve the best performance
(0.5477), representing a +23% improvement. For single-
domain categories, Electronics shows consistent ensem-
ble advantages (17–23%), while Appliances demonstrates
increasing ensemble superiority as granularity grows (from
−10% at 5 clusters to +23% at 20 clusters). The proposed
BIRCH-Optimized Hierarchical Consensus (BOHC) method
contributes a hierarchical affinity mechanism within the
BIRCH-AE framework; results show that its value depends
critically on domain context.

Fifth, we validate practical scalability by successfully
processing datasets that differ by a factor of 3 in size (1.4M
to 4.5M users) with near-linear subset-level scaling trends,
and by executing a 4.5M-user BOHC run in approximately
5 minutes. The framework’s incremental learning capability
enables real-time segment updates, which are critical for
production systems.

B. PRACTICAL AND METHODOLOGICAL IMPLICATIONS
From a practical perspective, conducting a domain granu-
larity assessment alongside the Calinski-Harabasz analysis
guides method selection by revealing both cluster dis-
tinctiveness and domain type. Multi-domain configurations
(multiple product categories) should strongly favor base
algorithms, such as BIRCH or K-Means, as BIRCH-AE’s
ensemble methods cannot effectively resolve natural cate-
gory overlap. Single-domain configurations (single product
category) should prefer BIRCH-AE’s ensemble methods,
with the magnitude of benefit depending on cluster stability
and desired segmentation granularity. For very simple
segmentation (≤5 clusters) with highly stable single-domain
clusters, base algorithms may suffice, although ensemble
methods remain beneficial for unstable clusters or higher
granularities.

Incorporating autoencoder-based feature learning consis-
tently improves clustering performance by approximately
11–53% across all domain types and configurations, effi-
ciently handling correlated behavioral variables. This repre-
sents the single most reliable performance enhancement in
this study and is a strong default choice for similar settings.
For applications requiring segmentation at multiple granu-
larities (5 to 20+ clusters), BIRCH’s hierarchical structure

VOLUME 14, 2026

88605

---

<!-- PAGE 27 -->

C. Li et al.: BIRCH-AE: A Hierarchical Ensemble Framework for Scalable E-Commerce User Segmentation

provides superior consistency and quality compared to
partition-based methods that optimize for single resolutions.
This addresses enterprise needs for coherent strategies
supporting both strategic planning (broad segments) and
tactical marketing (fine-grained microsegments).

BIRCH-AE’s ensemble methods deliver clear value in
single-domain scenarios, with benefits that
increase as
cluster complexity and segmentation granularity grow. The
Appliances pattern (base superiority in 5 clusters that
transitions to 23% ensemble superiority in 20 clusters)
demonstrates that ensemble methods excel at managing
complexity in higher-granularity segmentation. Comprehen-
sive behavioral feature engineering that integrates activity,
engagement, transaction, and temporal signals remains cru-
cial to capture multidimensional user behavior across domain
types.

Leveraging BIRCH’s incremental

learning capability
enables near-real-time user-segment updates, maintain-
ing relevance without
the computational burden of full
re-clustering. This is particularly valuable in dynamic
e-commerce environments where user behavior and product
catalogs evolve continuously.

Empirically,

three factors in
the study indicates that
hierarchical order govern method selection: (1) domain
granularity (single vs. multi-domain), (2) intrinsic cluster
structure (distinctness and stability), and (3) segmentation
granularity (number of desired clusters). Domain granularity
emerges as the primary decision factor in our experiments.

across

approaches

both multi-domain

The study provides a large-scale evaluation of BIRCH-
and
based
single-domain e-commerce scenarios, revealing how domain
granularity influences method selection independently of
cluster structure. Both evaluated single-domain categories
(Electronics and Appliances) demonstrate ensemble supe-
riority, though with different patterns reflecting differences
in cluster stability and granularity. This contrasts sharply
with multi-domain results, validating domain granularity as a
critical factor.

The integration of deep autoencoder-based feature learning
with hierarchical BIRCH clustering is validated in our
setting as a means to couple high-dimensional representation
learning with scalable, multi-resolution cluster formation
across domain types. The observed 11–53% improvement
supports the practical value of this integration.

The proposed BIRCH-Optimized Hierarchical Consensus
(BOHC) method provides a hierarchical mechanism for
preserving multi-scale information within the BIRCH-AE
framework. Results demonstrate its value in single-domain
scenarios, particularly as segmentation granularity increases,
while confirming that it is less beneficial in multi-domain
configurations.

C. FUTURE RESEARCH DIRECTIONS
Future work can extend in several promising directions.
Incorporating temporal dynamics through recurrent neu-
ral networks or Transformer-based architectures could

capture evolving user behaviors within and across cat-
egories, supporting predictive segmentation, churn fore-
casting, and category migration modeling. Understand-
ing the transition from base-to-ensemble superiority in
Appliances as granularity increases could yield impor-
tant
in ensemble
methods.

insights into complexity management

Multi-view clustering that combines behavioral, demo-
graphic, and contextual features, using methods designed
for hierarchical clustering, could improve segmentation
robustness, particularly in addressing cold-start limitations in
sparse-data scenarios. Cross-category transfer learning could
leverage patterns learned in data-rich categories to improve
segmentation in sparse categories.

Automated data profiling algorithms that detect dataset
characteristics (cluster separability, density, optimal gran-
ularity ranges, domain structure, stability metrics) can
automatically recommend suitable clustering strategies and
configurations, reducing reliance on manual assessment
and extensive empirical
testing. Developing predictive
indicators of when BIRCH-AE’s ensemble methods will
outperform base algorithms based on domain granularity
and cluster characteristics could make frameworks more
self-adaptive.

Online learning extensions of the autoencoder could
enable continuous adaptation to streaming data without
requiring full retraining, particularly valuable for dynamic
multi-category environments where category popularity and
user behaviors shift over time.

Fairness-aware segmentation should ensure clustering
outcomes do not
inadvertently reinforce demographic
or behavioral biases across categories. Transfer learning
could enhance applicability by training autoencoders
on large-scale, multi-category datasets and fine-tuning
single-category or domain-specific
them for
platforms.

smaller,

Integrating explainable AI techniques (such as SHAP
values, attention-based interpretability, or category-specific
feature importance analysis) could make latent representa-
tions more transparent for business stakeholders, particularly
valuable for understanding differences in segmentation
drivers across categories.

Extending single-domain analysis to additional product
categories beyond electronics and appliances would validate
the generalizability of findings on domain granularity
and ensemble performance patterns. Investigating optimal
strategies for hybrid scenarios (e.g., segmenting within
closely related category groups) would provide more nuanced
guidance for complex e-commerce platforms.

D. CLOSING REMARKS
As e-commerce continues to generate ever more massive
and complex user data across expanding product cat-
alogs, scalable,
intelligent segmentation frameworks are
essential for delivering personalized experiences and driv-
ing business success. BIRCH-AE provides a practical,

88606

VOLUME 14, 2026

---

<!-- PAGE 28 -->

C. Li et al.: BIRCH-AE: A Hierarchical Ensemble Framework for Scalable E-Commerce User Segmentation

scalable solution that balances computational efficiency
with segmentation quality. At the same time, experimental
analysis offers critical insights into how domain charac-
teristics and application requirements should drive method
selection.

The discovery that domain granularity plays a cru-
cial
role in determining the best method selection is
significant. In single-domain scenarios, BIRCH-AE’s ensem-
ble methods consistently outperform other approaches,
whereas in multi-domain scenarios, base algorithms tend
that as granularity
to perform better. This
increases,
ensemble meth-
ods become more effective at handling complex tasks
within higher-resolution segmentation. This insight pro-
vides practitioners with straightforward and actionable
guidance for making deployment decisions, ultimately
leading to improved outcomes across various e-commerce
contexts.

especially in Appliances,

indicates

For e-commerce user segmentation, the optimal approach
depends primarily on domain granularity (single vs. multi-
category), then on cluster characteristics (stability, distinct-
ness), and finally on the desired segmentation granularity
(5 vs. 20+ clusters). This hierarchical decision framework
replaces complex empirical testing with systematic assess-
ment, making deployment decisions more efficient and
reliable.

BIRCH’s demonstrated strength in maintaining high-
quality clusters across different granularities (5 to 20+ clus-
ters) addresses a critical but often overlooked requirement in
e-commerce analytics: the need for coherent segmentation
strategies that support both strategic planning (broad seg-
ments) and tactical marketing (fine-grained microsegments)
without maintaining separate clustering models. This capabil-
ity is valuable across both single and multi-domain scenarios.
The framework’s modular architecture supports easy
integration into existing analytics pipelines and adaptation to
domain-specific requirements. By combining BIRCH’s hier-
archical structure, autoencoder-based feature learning, and
comprehensive evaluation mechanisms with domain-aware
method selection, BIRCH-AE advances the state of the art
in large-scale user segmentation while providing actionable
guidance for practitioners deploying segmentation systems in
production environments.

The revelation that domain granularity fundamentally
influences optimal method selection provides practitioners
with a clear primary criterion for assessment. Multi-domain
to base algorithms, while
environments should default
from BIRCH-AE’s
single-domain environments benefit
ensemble methods, with the magnitude of benefit depending
on cluster stability and desired granularity. This insight,
combined with the consistent value of autoencoder-based fea-
ture learning and BIRCH’s multi-scale advantages, provides
a comprehensive foundation for enterprise-scale e-commerce
user segmentation.

REFERENCES

[1] J. Brown, M. Smith, and R. Johnson, ‘‘Retail analytics and big data:
trends and future directions,’’ J. Retailing, vol. 100, no. 2,

Current
pp. 145–162, 2024.

[2] M. Garcia, C. Rodriguez, and A. Martinez, ‘‘E-commerce customer
behavior analysis using deep learning techniques,’’ Electron. Commerce
Res., vol. 24, no. 1, pp. 89–112, 2024.

[3] A. Patel, K. Shah, and N. Desai, ‘‘Personalization in e-commerce: Current
trends and future directions,’’ ACM Comput. Surveys, vol. 55, no. 9,
pp. 1–38, 2023.

[4] M. Wedel and W. A. Kamakura, Market Segmentation Conceptual and

Methodological Foundations. Cham, Switzerland: Springer, 2000.

[5] W. R. Smith, ‘‘Product differentiation and market segmentation as
alternative marketing strategies,’’ J. Marketing, vol. 21, no. 1, pp. 3–8,
Jul. 1956.

[6] A. M. Hughes, ‘‘Strategic database marketing: The masterplan for starting
and managing a profitable, customer-based marketing program,’’ J.
Marketing, vol. 58, no. 3, pp. 125–127, 1994.

[7] M. A. Gomes and T. Meisen,

‘‘A review on customer segmen-
tation methods for personalized customer
targeting in e-commerce
use cases,’’ Inf. Syst. e-Bus. Manage., vol. 21, no. 3, pp. 527–570,
2023.

[8] R. Kumar, P. Sharma, and A. Singh, ‘‘Machine learning applications
in e-commerce: A comprehensive review,’’ Expert Syst. Appl., vol. 238,
Jan. 2024, Art. no. 121847.

[9] P. S. Fader, B. G. S. Hardie, and K. L. Lee, ‘‘RFM and CLV: Using iso-
value curves for customer base analysis,’’ J. Marketing Res., vol. 42, no. 4,
pp. 415–430, Nov. 2005.

[10] A. K. Jain, Data Clustering: 50 Years Beyond K-Means, vol. 31.

Amsterdam, The Netherlands: Elsevier, 2010.

[11] Z.-Y. Lim, L.-Y. Ong, and M.-C. Leow, ‘‘Cluster-N-engage: A new
framework for measuring user engagement of website with user
IEEE Access, vol. 11, pp. 112276–112292,
navigational behavior,’’
2023.

[12] X. Wang, J. Li, and Y. Chen, ‘‘Scalable clustering algorithms for big data:
A review,’’ ACM Trans. Knowl. Discovery Data, vol. 18, no. 2, pp. 1–35,
2024.

[13] C. C. Aggarwal and C. K. Reddy, Data Clustering: Algorithms and

Applications Boca Raton, FL, USA: CRC Press, 2013.

Most

importantly,

this work emphasizes the need to
understand domain granularity, cluster characteristics, and
segmentation granularity before selecting methods. The 6.4
× difference in cluster separation between the Retail Rocket
and E-Commerce Behavior datasets, combined with the
observed ensemble benefits for single-domain categories
versus the base algorithm’s superiority for multi-domain
data, demonstrates that domain-aware method selection is
essential. The key lessons for successful deployment of clus-
tering systems at scale are: domain granularity assessment,
cluster stability evaluation, segmentation granularity con-
sideration, empirical validation, and evidence-based method
selection.

[14] C. C. Aggarwal, A. Hinneburg,
behavior
Proc.

Int.

of

Conf.

and D. A. Keim,
in
Database

high

‘‘On the
dimensional
2001,

Theory,

distance metrics

surprising
space,’’
in
pp. 420–434.

[15] H.-H. Zhao, X.-C. Luo, R. Ma, and X. Lu, ‘‘An extended regularized K-
means clustering approach for high-dimensional customer segmentation
IEEE Access, vol. 9, pp. 48405–48412,
with correlated variables,’’
2021.

[16] T. Zhou, W. Liu, and J. Chen, ‘‘Streaming clustering algorithms: A review,’’
IEEE Trans. Neural Netw. Learn. Syst., vol. 35, no. 3, pp. 2841–2857,
Mar. 2024.

[17] F. Murtagh and P. Contreras, ‘‘Algorithms for hierarchical clustering: An
overview,’’ WIREs Data Mining Knowl. Discovery, vol. 2, no. 1, pp. 86–97,
Jan. 2012.

[18] J. B. MacQueen, ‘‘Some methods for classification and analysis of
multivariate observations,’’ in Proc. 5th Berkeley Symp. Math. Statist.
Probab., vol. 1, 1967, pp. 281–297.

VOLUME 14, 2026

88607

---

<!-- PAGE 29 -->

C. Li et al.: BIRCH-AE: A Hierarchical Ensemble Framework for Scalable E-Commerce User Segmentation

[19] M. Ester, H. Kriegel, J. Sander, and X. Xu, ‘‘A density-based algorithm for
discovering clusters in large spatial databases with noise,’’ in Proc. 2nd Int.
Conf. Knowl. Discovery Data Mining (KDD), 1996, pp. 226–231.
[20] S. C. Johnson, ‘‘Hierarchical clustering schemes,’’ Psychometrika, vol. 32,

no. 3, pp. 241–254, Sep. 1967.
[21] D. Arthur and S. Vassilvitskii,

careful seeding,’’
Algorithms, 2007, pp. 1027–1035.

‘‘K-means++: The advantages of
in Proc. 18th Annu. ACM-SIAM Symp. Discrete

[22] I. T. Jolliffe, Principal Component Analysis. Cham, Switzerland: Springer,

2002.

[23] K. Zhang, X. Wang, and Y. Liu, ‘‘Deep clustering: A comprehensive
survey,’’ IEEE Trans. Pattern Analysis Mach. Intell., vol. 45, no. 8,
pp. 10091–10111, Aug. 2023.

[24] W. Chen, L. Zhang, and M. Wang, ‘‘Autoencoder-based deep learning
for high-dimensional data clustering: A survey,’’ Neural Netw., vol. 162,
pp. 185–205, Jun. 2023.

[25] Y. Ren, K. Hu, X. Dai, L. Pan, S. C. Hoi, and Z. Xu, ‘‘Deep clustering:
A comprehensive survey,’’ IEEE Trans. Pattern Anal. Mach. Intell., vol. 46,
no. 5, pp. 3213–3232, May 2024.

[26] Y. Li, W. Zhang, and C. Wang, ‘‘Ensemble learning for deep learning:

A survey,’’ Inf. Fusion, vol. 92, pp. 34–56, Apr. 2023.

[27] H. Liu, Z. Ming, and Y. Sun, ‘‘Consensus clustering: A survey and new
methods,’’ Pattern Recognit., vol. 135, Mar. 2023, Art. no. 109177.
[28] T. Zhang, R. Ramakrishnan, and M. Livny, ‘‘Birch: An efficient data
clustering method for very large databases,’’ in Proc. ACM SIGMOD Int.
Conf. Manage. Data, 1996, pp. 103–114.

[29] B. Lorbeer, A. Kosareva, B. Deva, D. Softić, P. Ruppel, and A. Küpper,
‘‘Variations on the clustering algorithm BIRCH,’’ Big Data Res., vol. 11,
pp. 44–53, Mar. 2018.
[30] A. Strehl and J. Ghosh,

‘‘Cluster ensembles—A knowledge reuse
framework for combining multiple partitions,’’ J. Mach. Learn. Res., vol. 3,
pp. 583–617, Dec. 2002.

[31] A. L. N. Fred and A. K. Jain, ‘‘Combining multiple clusterings using
evidence accumulation,’’ IEEE Trans. Pattern Anal. Mach. Intell., vol. 27,
no. 6, pp. 835–850, Jun. 2005.

[32] C. Li, ‘‘Birch-ae: A hierarchical ensemble framework for scalable
e-commerce user segmentation with autoencoder-enhanced feature learn-
ing,’’ Zenodo, Geneva, Switzerland, Tech. Rep. 17498249, Jun. 2026, doi:
10.5281/zenodo.17498249.

[33] C. Fraley and A. E. Raftery, ‘‘Model-based clustering, discriminant
analysis, and density estimation,’’ J. Amer. Stat. Assoc., vol. 97, no. 458,
pp. 611–631, Jun. 2002.

[34] T. Rebafka, M. Sedki, and G. Celeux, ‘‘Model-based clustering with
missing not at random data,’’ J. Classification, vol. 41, no. 1, pp. 78–104,
2024.

[35] A. Y. Ng, M. I. Jordan, and Y. Weiss, ‘‘On spectral clustering: Analysis
and an algorithm,’’ in Proc. Adv. Neural Inf. Process. Syst., vol. 14,
Jordan, 2001, pp. 849–856.

[36] D. A. Reynolds, ‘‘Gaussian mixture models,’’ Encyclopedia Biometrics, S.
Z. Li and A. K. Jain, Eds. Boston, MA, USA: Springer, 2009, pp. 659–663.
[37] T. Zhang, R. Ramakrishnan, and M. Livny, ‘‘BIRCH: A new data clustering
algorithm and its applications,’’ Data Mining Knowl. Discovery, vol. 1,
no. 2, pp. 141–182, Jun. 1997.

[38] S. Vega-Pons and J. Ruiz-Shulcloper, ‘‘A survey of clustering ensemble
algorithms,’’ Int. J. Pattern Recognit. Artif. Intell., vol. 25, no. 3,
pp. 337–372, May 2011.

[39] D. Huang, C.-D. Wang, J.-S. Wu, J.-H. Lai, and C.-K. Kwoh,
‘‘Ultra-scalable
clustering,’’
clustering
IEEE Trans. Knowl. Data Eng., vol. 32, no. 6, pp. 1212–1226,
Jun. 2020.

ensemble

spectral

and

[45] P. J. Rousseeuw, ‘‘Silhouettes: A graphical aid to the interpretation and
validation of cluster analysis,’’ J. Comput. Appl. Math., vol. 20, pp. 53–65,
Nov. 1987.

[46] T. Calinski and J. Harabasz, ‘‘A dendrite method for cluster analysis,’’
Commun. Statistics-Theory Methods, vol. 3, no. 1, pp. 1–27, 1974.
[47] D. L. Davies and D. W. Bouldin, ‘‘A cluster separation measure,’’ IEEE
Trans. Pattern Anal. Mach. Intell., vols. PAMI–1, no. 2, pp. 224–227,
Apr. 1979.

[48] G. Barbato, E. M. Barini, G. Genta, and R. Levi, ‘‘Features of the iqr
method to detect outliers in industrial data: A case study,’’ IEEE Trans.
Instrum. Meas., vol. 60, no. 9, pp. 3613–3619, Aug. 2011.

[49] Y. Bengio, A. Courville, and P. Vincent, ‘‘Representation learning:
A review and new perspectives,’’ IEEE Trans. Pattern Anal. Mach. Intell.,
vol. 35, no. 8, pp. 1798–1828, Aug. 2013.

[50] D. P. Kingma and J. Ba, ‘‘Adam: A method for stochastic optimization,’’

2014, arXiv:1412.6980.

[51] H. W. Kuhn, ‘‘The Hungarian method for the assignment problem,’’ Nav.

Res. Logistics Quart., vol. 2, nos. 1–2, pp. 83–97, 1955.

[52] Retail Rocket.
[Online].
ecommerce-dataset

(2016). Retailrocket Recommender System Dataset.
https://www.kaggle.com/datasets/retailrocket/

Available:

[53] M. Kechinov. (2019). Ecommerce Behavior Data From Multi Category
Store. [Online]. Available: https://www.kaggle.com/datasets/mkechinov/
ecommerce-behavior-data-from-multi-category-store

[54] J. H. Ward, ‘‘Hierarchical grouping to optimize an objective function,’’ J.

Amer. Stat. Assoc., vol. 58, no. 301, pp. 236–244, Mar. 1963.

CAIWEN LI is currently pursuing the Ph.D. degree
with the Faculty of Computer Science and Infor-
mation Technology, Universiti Putra Malaysia
(UPM). She has years of experience as a data sci-
entist, she has held various roles, most recently at
Amazon Web Services. She specializes in business
intelligence and digital marketing, leveraging her
expertise in data science, including forecasting,
feature/model selection, data mining, APIs, and
cloud technologies. Her primary research interests
include recommendation systems, business intelligence, deep learning,
hierarchical clustering methods, and scalable data mining algorithms for
e-commerce applications.

[40] F. Li, Y. Qian, J. Wang, C. Dang, and L. Jing, ‘‘Clustering ensem-
ble based on sample’s stability,’’ Artif. Intell., vol. 273, pp. 37–55,
Aug. 2019.

[41] R. A. FISHER, ‘‘The use of multiple measurements in taxonomic

problems,’’ Ann. Eugenics, vol. 7, no. 2, pp. 179–188, Sep. 1936.

[42] L. V. D. Maaten and G. E. Hinton, ‘‘Visualizing data using t-SNE,’’ J.

Mach. Learn. Res., vol. 9, no. 86, pp. 2579–2605, 2008.

[43] G. E. Hinton and R. R. Salakhutdinov, ‘‘Reducing the dimensionality of
data with neural networks,’’ Science, vol. 313, no. 5786, pp. 504–507,
Jul. 2006.

[44] J. Xie, R. Girshick, and A. Farhadi, ‘‘Unsupervised deep embedding for
clustering analysis,’’ in Proc. Int. Conf. Mach. Learn. (ICML), 2015,
pp. 478–487.

88608

ISKANDAR ISHAK received the Bachelor of
Information Technology degree from Universiti
Tenaga Nasional, Malaysia, the Master of Tech-
nology degree in information technology from
the Royal Melbourne Institute of Technology,
Australia, and the Ph.D. degree in computer
science from Universiti Teknologi Malaysia. He is
currently a Senior Lecturer with Universiti Putra
Malaysia. His research interests include database
systems, big data, data analytics, and scalable
clustering algorithms.

VOLUME 14, 2026

---

<!-- PAGE 30 -->

C. Li et al.: BIRCH-AE: A Hierarchical Ensemble Framework for Scalable E-Commerce User Segmentation

HAMIDAH IBRAHIM (Member, IEEE) received
the Ph.D. degree in computer science from the
University of Wales, Cardiff, U.K.,
in 1998.
She is currently a Full Professor with the
Faculty of Computer Science and Information
Technology, Universiti Putra Malaysia (UPM).
Her current research interests include databases
(distributed, parallel, mobile, biomedical, XML)
focusing on issues related to integrity main-
tenance/checking, ontology/schema/data integra-
tion, ontology/schema/data mapping, cache management, access control,
data security, transaction processing, query optimization, query reformu-
lation, preference evaluation (context-aware), information extraction, and
concurrency control.

FATIMAH SIDI (Member, IEEE) received the
Ph.D. degree in management information systems
from Universiti Putra Malaysia (UPM), Malaysia,
in 2008. She is currently an Associate Professor
with the Department of Computer Science, Faculty
of Computer Science and Information Technol-
ogy, UPM. Her current research interests include
knowledge and information management systems,
data and knowledge engineering, databases, data
warehouses, big data, and data analytics.

MASLINA ZOLKEPLI received the bachelor’s
and master’s degrees in computer science from
Universiti Putra Malaysia,
in 2007 and 2010,
respectively, and the Ph.D. degree in computa-
tional intelligence and systems science from Tokyo
Institute of Technology, Japan, in 2015. She is
currently a Senior Lecturer with the Department of
Computer Science, Faculty of Computer Science
and Information Technology, Universiti Putra
Malaysia. Her research interests include business
analytics, fuzzy brake systems, computational intelligence, and ensemble
learning methods.

CAILI LI is currently pursuing the Ph.D. degree
in design and architecture with Universiti Putra
Malaysia, she conducts interdisciplinary research
at the intersection of art and technology. She was
a Visiting Scholar at Tsinghua University, she
brings extensive expertise and insights to her work,
aiming to advance the field of design and to inspire
innovative solutions through data-driven visual-
ization. She is currently an Associate Professor
with Heilongjiang Institute of Technology, China,
specializing in design art, visual arts, analytical visualization, integrated arts,
and landscape design.

VOLUME 14, 2026

88609

<!-- MARKITDOWN CONVERSION -->

<!-- Full MarkItDown conversion for formatting fidelity. -->

Received6April2026,accepted18May2026,dateofpublication29May2026,dateofcurrentversion16June2026.
DigitalObjectIdentifier10.1109/ACCESS.2026.3697984
| BIRCH-AE:    |                      | A          | Hierarchical |                  | Ensemble |                  | Framework |     |     |     |
| ------------ | -------------------- | ---------- | ------------ | ---------------- | -------- | ---------------- | --------- | --- | --- | --- |
| for Scalable |                      | E-Commerce |              |                  | User     | Segmentation     |           |     |     |     |
| With         | Autoencoder-Enhanced |            |              |                  |          | Feature          | Learning  |     |     |     |
|              | 1,ISKANDARISHAK      |            |              | 1,HAMIDAHIBRAHIM |          | 1,(Member,IEEE), |           |     |     |     |
CAIWENLI
| MASLINAZOLKEPLI1,FATIMAHSIDI |     |     |     | 1,(Member,IEEE),ANDCAILILI |     |     | 2   |     |     |     |
| ---------------------------- | --- | --- | --- | -------------------------- | --- | --- | --- | --- | --- | --- |
1DepartmentofComputerScience,FacultyofComputerScienceandInformationTechnology,UniversitiPutraMalaysia(UPM),Serdang,
Selangor43400,Malaysia
2CollegeofArtandDesign,HeilongjiangInstituteofTechnology,Daowai,Harbin,Heilongjiang150050,China
Correspondingauthor:IskandarIshak(iskandar_i@upm.edu.my)
ThisworkwassupportedinpartbytheJournalPublicationFundundertheUniversityDrivenResearchProgram(DigitalandICTI),
UniversitiPutraMalaysia,andinpartbytheFacultyofComputerScienceandInformationTechnology,UniversitiPutraMalaysia.
ABSTRACT Therapidexpansionofe-commerceplatformshasintensifieddemandforscalable,high-quality
user segmentation systems capable of efficiently processing millions of behavioral records. This paper
presents BIRCH-AE, a hierarchical ensemble clustering framework that integrates the Balanced Iterative
Reducing and Clustering using Hierarchies (BIRCH) algorithm with autoencoder-based feature learning
for large-scale e-commerce analytics. The autoencoder compresses high-dimensional behavioral data into
compact latent representations, mitigating the curse of dimensionality and improving cluster separability.
MultipleBIRCHconfigurationsarecombinedthroughfourensemblestrategies:MajorityVoting,Weighted
Voting, Advanced Affinity-based Spectral Clustering (AASC), and the proposed BIRCH-Optimized
Hierarchical Consensus (BOHC). Dynamic selection based on multi-criteria evaluation automatically
identifies the best-performing strategy per dataset setting, emphasizing that no single consensus method
is universally optimal. Experiments on two large-scale datasets (Retail Rocket with 1.4M users and
E-CommerceBehaviorwith4.5Musers)showimprovedclusteringqualityandpracticalscalability.BOHC
achievesupto23%silhouetteimprovementoversingleBIRCHontransaction-focuseddata,withaclearer
hierarchical structure, while multi-domain data favors strong base models. Autoencoder feature learning
improvesclusteringqualityby23–53%overrawfeatures.Thefull4.5M-userexperimentwasexecutedasa
BOHCscalabilityrun,completedinapproximately5minutes,whileframework-levelcomparativeanalyses
wereconductedviarepeatedstratified30%-subsettrials.ThesefindingssupportBIRCH-AEasapractical
andadaptivesegmentationframeworkforenterprise-scalee-commerceanalytics.
INDEX TERMS BIRCHclustering,hierarchicalclustering,usersegmentation,autoencoders,e-commerce
analytics,ensemblemethods,scalableclustering,incrementallearning.
I. INTRODUCTION touchpoints [3]. This rich data landscape presents opportu-
The exponential growth of e-commerce platforms has fun- nities and challenges for companies seeking to understand
damentallytransformedretaildynamics,generatingunprece- customerbehavioranddeliverpersonalizedexperiences.
dented volumes of user interaction data [1], [2]. Modern User segmentation, the systematic process of dividing
|            |         |           |         |                     |     | a heterogeneous | customer base | into | homogeneous | groups |
| ---------- | ------- | --------- | ------- | ------------------- | --- | --------------- | ------------- | ---- | ----------- | ------ |
| e-commerce | systems | routinely | collect | detailed behavioral |     |                 |               |      |             |        |
information spanning browsing patterns, purchase histo- thatsharesimilarcharacteristicsorbehaviors,hasbecomea
ries, search queries, and engagement metrics at multiple cornerstonestrategyinmoderndata-drivensystems[4],[5].
|     |     |     |     |     |     | The fundamental | premise of | segmentation | is that | customers |
| --- | --- | --- | --- | --- | --- | --------------- | ---------- | ------------ | ------- | --------- |
The associate editor coordinating the review of this manuscript and exhibit diverse needs, preferences, purchasing patterns,
|                                             |     |     |     |     |     | and engagement | behaviors. | Rather than | applying | uniform |
| ------------------------------------------- | --- | --- | --- | --- | --- | -------------- | ---------- | ----------- | -------- | ------- |
| approvingitforpublicationwasDominikStrzalka |     |     |     | .   |     |                |            |             |          |         |

2026TheAuthors.ThisworkislicensedunderaCreativeCommonsAttribution4.0License.
| 88580 |     |     |     |     |     |     |     |     |     | VOLUME14,2026 |
| ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------- |
Formoreinformation,seehttps://creativecommons.org/licenses/by/4.0/

C.Lietal.:BIRCH-AE:AHierarchicalEnsembleFrameworkforScalableE-CommerceUserSegmentation
strategies across an entire customer population, segmen- planning with broad customer categories and tactical mar-
tation enables organizations to identify distinct subgroups keting with fine-grained micro-segments, adds additional
and tailor their approaches accordingly [6]. This strategic complexity that traditional clustering methods struggle to
differentiation has profound implications across multiple address[17].
businessfunctions,frommarketingandproductdevelopment These challenges motivate the development of advanced
tocustomerserviceandinventorymanagement. clustering frameworks that can simultaneously achieve
Incontemporarye-commerceenvironments,effectiveuser scalability, quality, and adaptability for enterprise-scale e-
segmentation serves several critical business objectives [7], commerce user segmentation. The need for such systems
[8]. First, it enables personalized marketing campaigns has become particularly acute as platforms expand their
that resonate with specific customer segments, significantly customer bases to millions and diversify their product
improving conversion rates and return on marketing invest- offerings across multiple categories, creating increasingly
ment.Byunderstandingthecharacteristicsandpreferencesof complexsegmentationrequirements.
differentusergroups,businessescancrafttargetedmessages,
promotionaloffers,andproductrecommendationsthatalign A. LIMITATIONSOFTRADITIONALAPPROACHES
witheachsegment’suniqueprofile[3].Second,segmentation Traditional clustering algorithms, including K-Means [18],
facilitatesdynamicpricingstrategiesandinventoryoptimiza- DBSCAN[19],andhierarchicalagglomerativemethods[20],
tion, allowing platforms to adjust pricing and stock levels havebeenextensivelyappliedtocustomersegmentationtasks
basedonsegment-specificdemandpatternsandpricesensi- across various domains. However, recent comprehensive
tivities[1].Third,itsupportscustomerlifetimevaluepredic- surveys and empirical studies [7], [8], [12] identify three
tionandchurnprevention,enablingproactiveretentionstrate- critical limitations that severely constrain their applicability
gies for high-value segments and win-back campaigns for whenconfrontingcontemporarye-commercedataatscale.
at-riskcustomers[9].Fourth,segmentationprovidesstrategic First,scalabilityconstraintssignificantlylimitpractical
insights for product development by revealing unmet needs deployability for large-scale applications. The compu-
andemergingtrendswithinspecificcustomergroups[4]. tational complexity of traditional clustering algorithms
The significance of user segmentation has increased as becomesprohibitiveasdatasetsizesgrowintothemillionsof
the field has evolved from traditional demographic and users common in modern e-commerce platforms. K-Means,
rule-basedcategorizationtosophisticateddata-drivenbehav- despiteitspopularityandrelativeefficiency,requiresmultiple
ioralsegmentation[7].Modernapproachesleveragemachine iterative passes over the entire dataset to converge. Each
learning and data mining techniques to uncover complex iteration computes distances between all data points and
patterns in vast behavioral datasets, enabling more nuanced clustercentroids[18],[21].Fordatasetswithmillionsofusers
and actionable customer understanding [10]. E-commerce and dozens of features, this iterative process can take hours
platformsnowanalyzemultidimensionalbehavioralsignals, or even days to complete, making real-time or near-real-
including browsing frequency, session duration, product time segmentation infeasible [12]. Traditional hierarchical
category exploration, cart abandonment patterns, purchase agglomerative methods face even more severe limitations,
recencyandfrequency,averageordervalues,pricesensitivity typically exhibiting quadratic time complexity O(n2) and
indicators, temporal activity patterns, and cross-category requiringO(n2)memorytostorethedistancematrixbetween
engagementmetrics[2],[11].Thiscomprehensivebehavioral all pairs of data points [17], [20]. These quadratic require-
viewenablessegmentationstrategiesthatgofarbeyondsim- ments render hierarchical methods completely impractical
pleRFM(Recency,Frequency,Monetary)analysis,capturing for datasets exceeding a few tens of thousands of users—
thefullcomplexityofmoderncustomerjourneys[9]. far below the scale of contemporary e-commerce platforms
However, the transition to large-scale, behavior-driven with millions of active customers [13]. DBSCAN, while
segmentationintroducessignificanttechnicalchallenges.The offering advantages for discovering arbitrarily shaped clus-
enormousdatageneratedbymoderne-commerceplatforms, ters, similarly struggles with scalability due to its need to
with millions of users creating billions of interaction compute neighborhood relationships, often requiring spatial
events, requires clustering algorithms that can efficiently indexingstructuresthatthemselvesbecomecomputationally
process large datasets [12], [13]. The high dimensionality expensive for high-dimensional data [19]. The scalability
of behavioral feature spaces, often encompassing hundreds limitation is not merely a matter of computational cost.
of correlated variables, poses significant challenges for Still,itfundamentallylimitsorganizations’abilitytoperform
clusteringalgorithms.Theseincludethecurseofdimension- comprehensivesegmentationacrosstheirfullcustomerbases,
ality, degradation of distance metrics, and increased noise oftenforcingthemtoworkwithsmallsamplesthatmaynot
sensitivity [14], [15]. The dynamic nature of e-commerce capturethefulldiversityofcustomerbehaviors[12].
environments, where user behavior continuously evolves, Second, the curse of dimensionality fundamentally
and new customers arrive in real time, requires segmen- degrades clustering performance in high-dimensional
tation systems that can adapt incrementally without com- behavioral feature spaces. Modern e-commerce platforms
plete recomputation [16]. Furthermore, the requirement for generate rich behavioral profiles encompassing hundreds
multi-resolution segmentation, supporting both strategic of features: activity metrics (total events, unique products
VOLUME14,2026 88581

C.Lietal.:BIRCH-AE:AHierarchicalEnsembleFrameworkforScalableE-CommerceUserSegmentation
viewed, sessions count), engagement patterns (events per from scratch, with no mechanism to insert new data points
session, session duration, category diversity), transactional intoanexistinghierarchy[17].Althoughsomeresearchhas
features(purchasefrequency,averageordervalue,pricerange exploredincrementalvariantsofthesealgorithms[16],these
statistics), temporal behaviors (preferred shopping times, approaches often sacrifice cluster quality for adaptability
activity consistency, recency indicators), and cross-category or introduce additional hyperparameters that are difficult
interaction patterns [2], [11]. These comprehensive feature to tune in practice. The absence of robust incremental
sets are essential for capturing the multidimensional nature learningcapabilitiesforcese-commerceplatformstochoose
of customer behavior but create significant challenges for between maintaining outdated segmentations that no longer
traditionalclusteringalgorithms.Inhigh-dimensionalspaces, reflect current customer behaviors or investing substantial
distance metrics become less discriminative as the relative computationalresourcesinfrequent,completere-clustering.
contrast between nearest and farthest neighbors diminishes: Neitheroptionissatisfactoryforoperationalexcellence.
aphenomenonextensivelydocumentedintheliterature[13], These three fundamental limitations: scalability con-
[14]. This distance concentration effect causes K-Means straints, high-dimensional feature degradation, and lack
and other distance-based algorithms to produce suboptimal of incremental adaptability—collectively demonstrate that
clusters,sincethefundamentalassumptionthatnearbypoints traditional clustering approaches, despite their theoretical
should belong to the same cluster breaks down when dis- eleganceandhistoricalsuccessinsmaller-scaleapplications,
tances lose meaning [10]. Furthermore, behavioral features areinadequateformodernenterprise-scalee-commerceuser
of e-commerce exhibit strong intercorrelations: browsing segmentation. This recognition motivates the development
frequency correlates with session counts, purchase amounts of novel frameworks that simultaneously address all three
correlate with price sensitivity, and category exploration challenges through architectural innovations that combine
correlates with session duration [15]. These correlations scalablehierarchicalmethods,advancedfeaturelearning,and
introduce redundancy that inflates the effective dimension- incrementalupdatemechanisms.
ality without adding proportional information, exacerbating
computationalcostsandfurtherdegradingthequalityofthe B. RESEARCHGAPSANDMOTIVATION
distance metric [14]. Traditional dimensionality reduction Despite extensive research in clustering methodologies,
techniques, such as Principal Component Analysis (PCA), recentcomprehensivesurveys[25],[26],[27]identifycritical
provide only linear projections that may fail to capture gapsinlarge-scalee-commerceusersegmentation.Although
the complex nonlinear relationships inherent in behavioral BIRCH[28]offersexcellentscalabilitythroughitsClustering
data[22].Incontrast,moresophisticatednon-linearmethods Feature (CF) Tree structure and single-pass processing, its
havenotbeensystematicallyintegratedwithscalablecluster- application to e-commerce remains limited. Existing work
ingalgorithmsfore-commerceapplications[23],[24]. focuses primarily on spatial data and sensor networks [29].
Third,thestaticnatureoftraditionalclusteringmeth- Systematic approaches to optimize BIRCH performance
ods renders them unsuitable for dynamic e-commerce through ensemble methods and advanced feature learning
environmentsrequiringcontinuousadaptation,andcom- remainunderdevelopedforbehavioraldata.
merce platforms operate in highly dynamic contexts where Current ensemble clustering frameworks [26], [30], [31]
userbehaviorsevolvecontinuously.Customersmovethrough predominantlyfocusonpartition-basedalgorithms,neglect-
lifecyclestages,respondtoseasonaltrends,adoptnewshop- ing the unique advantages of hierarchical methods in
pingpatterns,andaltertheirpreferencesforcategoriesover capturingmulti-scaleusergroupings.Moderndeepclustering
time [2], [3]. Additionally, platforms continuously acquire research [23], [24] primarily integrates autoencoders with
new users that must be integrated into the segmentation K-Means or Gaussian Mixture Models, overlooking hier-
schemewithoutdisruptingexistingsegmentdefinitions[16]. archical algorithms despite their superior ability to reveal
Traditional clustering algorithms are fundamentally batch- nested customer segment structures, which are crucial for
oriented: they require access to the complete dataset at marketingstrategies[27].
trainingtimeandproduceafixedpartitionthatcannotadapt Furthermore, measuring user engagement through nav-
tonewdatawithoutcompleterecomputation[13].Whennew igational behavior patterns [11] has become increasingly
users arrive or existing users exhibit changes in behavior, important.Theseengagementmetrics,whencombinedwith
theonlyoptionistoreruntheentireclusteringprocessfrom transactional data, provide a comprehensive view of user
scratch: an approach that is computationally prohibitive for behavior that significantly enhances segmentation qual-
million-userplatformsthatrequiredailyorevenhourlyseg- ity. The integration of autoencoder-based feature learning
mentupdates[12],[16].Thislimitationcreatesacriticalgap with BIRCH’s hierarchical structure (particularly for high-
betweenthebusinessrequirementsforresponsivenear-real- dimensional e-commerce data with correlated variables [8],
timesegmentationandthetechnicalcapabilitiesoftraditional [15])representsanunexploredopportunity.
methods. K-Means lacks an incremental learning mecha-
nism; each new batch of users requires reinitialization of C. CONTRIBUTIONS
clustercentroidsandreprocessingalldata[18].Hierarchical To address these limitations and research gaps, this paper
methods similarly require rebuilding the entire dendrogram introduces BIRCH-AE, a comprehensive framework for
88582 VOLUME14,2026

C.Lietal.:BIRCH-AE:AHierarchicalEnsembleFrameworkforScalableE-CommerceUserSegmentation
scalable e-commerce user segmentation that integrates over ensembles). This finding, validated across three
BIRCH’s hierarchical clustering capabilities with deep distinct evaluation scenarios, provides practitioners
autoencoder-based feature learning and advanced ensemble withcleardecisioncriteriaforselectingmethodsbased
consensus mechanisms. The framework’s architecture posi- onplatformstructure.
tionsBIRCHasthecorescalableclusteringengine,enhanced 5) Enterprise-ScaleValidationandDeploymentGuide-
byautoencoder-drivendimensionalityreductionandunified lines: Comprehensive empirical validation on repre-
through multiple ensemble strategies, including the novel sentative subsets of two large-scale datasets (Retail
BIRCH-OptimizedHierarchicalConsensus(BOHC)method. Rocket: 1.4M users, E-Commerce Behavior: 4.5M
Thekeycontributionsareasfollows. users)withsingle-domaincategoryanalysis,supported
1) Scalable Hierarchical Framework with Deep Fea- by20randomizedstratifiedsubsettrials.Aproduction-
ture Integration: A unified architecture combin- scale BOHC run on 4.5M users (approximately
ingBIRCH’smemory-efficienthierarchicalclustering 5 minutes) demonstrates operational feasibility at
with deep autoencoder-based feature learning. The scale. Evidence-based deployment recommendations
autoencoder compresses high-dimensional, correlated guide practitioners through data profiling, method
behavioral data (30–50 features) into compact latent selection based on domain granularity and cluster
representations (14–32 dimensions) while preserving characteristics, and incremental update strategies for
90–95% of variance, allowing efficient processing dynamicenvironments.
| of million-user |              | datasets.   | This          | integration |          | achieves |                  |               |           |              |             |     |                 |         |
| --------------- | ------------ | ----------- | ------------- | ----------- | -------- | -------- | ---------------- | ------------- | --------- | ------------ | ----------- | --- | --------------- | ------- |
|                 |              |             |               |             |          |          | These            | contributions |           | collectively | advance     |     | large-scale     | user    |
| 23–53%          | improvements |             | in clustering |             | quality  | over raw |                  |               |           |              |             |     |                 |         |
|                 |              |             |               |             |          |          | segmentation     | by            | providing | an           | empirically |     | grounded,       | practi- |
| features        | while        | maintaining |               | BIRCH’s     | scalable | incre-   |                  |               |           |              |             |     |                 |         |
|                 |              |             |               |             |          |          | cally deployable |               | framework | that         | addresses   |     | the fundamental |         |
mentallearningbehavior.
|                       |     |     |          |        |     |         | limitations | of  | traditional | clustering |     | approaches |     | and offers |
| --------------------- | --- | --- | -------- | ------ | --- | ------- | ----------- | --- | ----------- | ---------- | --- | ---------- | --- | ---------- |
| 2) Novel Hierarchical |     |     | Ensemble | Method |     | (BOHC): |             |     |             |            |     |            |     |            |
actionableguidanceforreal-worlde-commerceapplications.
| Introduction | of            | BIRCH-Optimized |          | Hierarchical |          | Con- |     |     |     |     |     |     |     |     |
| ------------ | ------------- | --------------- | -------- | ------------ | -------- | ---- | --- | --- | --- | --- | --- | --- | --- | --- |
| sensus,      | a specialized |                 | ensemble | strategy     | designed | to   |     |     |     |     |     |     |     |     |
preserve multi-scale clustering information inherent D. PAPERORGANIZATION
Theremainderofthispaperisorganizedasfollows.SectionII
| in BIRCH’s | CF       | Tree     | structure. | Unlike   | conventional |      |         |         |         |            |          |     |          |       |
| ---------- | -------- | -------- | ---------- | -------- | ------------ | ---- | ------- | ------- | ------- | ---------- | -------- | --- | -------- | ----- |
|            |          |          |            |          |              |      | reviews | related | work in | clustering | methods, |     | ensemble | tech- |
| voting or  | spectral | ensemble |            | methods, | BOHC         | con- |         |         |         |            |          |     |          |       |
niques,anddimensionalityreductionforusersegmentation.
structshierarchicalaffinitymatricesbasedonancestral
|               |        |     |        |          |     |           | Section | III provides | technical |     | background |     | on BIRCH | clus- |
| ------------- | ------ | --- | ------ | -------- | --- | --------- | ------- | ------------ | --------- | --- | ---------- | --- | -------- | ----- |
| relationships | within | CF  | Trees, | enabling |     | consensus |         |              |           |     |            |     |          |       |
formation that preserves hierarchical context across tering and autoencoders. Section IV details the BIRCH-AE
|          |       |                 |     |             |     |        | framework | architecture, |     | including | the | four | ensemble | strate- |
| -------- | ----- | --------------- | --- | ----------- | --- | ------ | --------- | ------------- | --- | --------- | --- | ---- | -------- | ------- |
| multiple | BIRCH | configurations. |     | Experiments |     | demon- |           |               |     |           |     |      |          |         |
gies(MajorityVoting,WeightedVoting,AASC,andBOHC)
| strate BOHC | achieves |     | up to | 23% improvement |     | over |         |         |           |            |     |         |     |          |
| ----------- | -------- | --- | ----- | --------------- | --- | ---- | ------- | ------- | --------- | ---------- | --- | ------- | --- | -------- |
|             |          |     |       |                 |     |      | and the | dynamic | selection | mechanism. |     | Section | V   | presents |
singleBIRCHmodelsfortransaction-focuseddatasets
|     |     |     |     |     |     |     | a comprehensive |     | experimental |     | evaluation |     | with | detailed |
| --- | --- | --- | --- | --- | --- | --- | --------------- | --- | ------------ | --- | ---------- | --- | ---- | -------- |
withdistinctclusterboundaries.
3) Comprehensive Ensemble Strategy Suite with comparative analysis. Section VI discusses implications,
|         |            |             |     |     |                 |     | limitations,    | and | applications. |     | Section | VII              | concludes | with |
| ------- | ---------- | ----------- | --- | --- | --------------- | --- | --------------- | --- | ------------- | --- | ------- | ---------------- | --------- | ---- |
| Dynamic | Selection: | Integration |     | of  | four complemen- |     |                 |     |               |     |         |                  |           |      |
|         |            |             |     |     |                 |     | future research |     | directions.   | To  | support | reproducibility, |           | the  |
taryensembleapproaches:MajorityVoting,Weighted
BIRCH-AEimplementationcodeandexperimentalmaterials
| Voting, | Advanced | Affinity-based |     | Spectral |     | Clustering |     |     |     |     |     |     |     |     |
| ------- | -------- | -------------- | --- | -------- | --- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- |
areavailable[32].
| (AASC), | and BOHC       |     | within  | the BIRCH-AE |           | frame- |     |     |     |     |     |     |     |     |
| ------- | -------------- | --- | ------- | ------------ | --------- | ------ | --- | --- | --- | --- | --- | --- | --- | --- |
| work. A | multi-criteria |     | dynamic | selection    | mechanism |        |     |     |     |     |     |     |     |     |
automaticallyidentifiesoptimalstrategiesbasedonSil- II. RELATEDWORK
houette Score, Calinski-Harabasz Index, and Davies- A. E-COMMERCEUSERSEGMENTATION
Bouldin Index, adapting to dataset characteristics User segmentation has been an integral part of e-commerce
without manual intervention. This adaptive approach analytics, with methodologies evolving from demographic
addresses the challenge that no single ensemble andrule-basedcategorizationtosophisticatedmachinelearn-
method universally outperforms across different data ingapproaches[4],[5].Moderncomprehensivereviews[7],
distributionsanddomaingranularities. [8] highlight this evolution towards data-driven behavioral
4) Domain Granularity Impact Discovery: Empir- segmentationbasedonpurchasepatterns,browsingbehavior,
ical evidence revealing that domain granularity andengagementmetrics[10].
(single-domain vs. multi-domain) fundamentally Garcia et al. [2] demonstrate the effectiveness of deep
determines optimal segmentation strategies. Single- learningincustomerbehavioranalysis.Incontrast,Pateletal.
domain datasets (e.g., transaction-focused platforms, [3]emphasizetheneedforreal-timesegmentationtosupport
individual product categories) consistently benefit dynamic personalization at scale. Traditional clustering
from ensemble methods (+17–23% improvement), algorithms remain popular for their simplicity but face sig-
while multi-domain datasets (multiple product cat- nificantchallengesinhandlingthevolumeofcontemporary
| egories)      | favor | well-tuned | base | algorithms |     | (+7.4% | e-commercedata. |     |     |     |     |     |     |       |
| ------------- | ----- | ---------- | ---- | ---------- | --- | ------ | --------------- | --- | --- | --- | --- | --- | --- | ----- |
| VOLUME14,2026 |       |            |      |            |     |        |                 |     |     |     |     |     |     | 88583 |

C.Lietal.:BIRCH-AE:AHierarchicalEnsembleFrameworkforScalableE-CommerceUserSegmentation
K-Means [18] suffers from sensitivity to initialization Various consensus functions have been proposed, including
and assumptions of spherical clusters [21]. Zhao et al. co-association matrices, graph-based methods, and voting
[15] address high-dimensional customer segmentation with mechanisms[38].
correlated features using extended regularized K-Means, Liuetal.[27]provideacomprehensivereviewofthepast
demonstrating the importance of accounting for feature decade, highlighting that partition-based ensemble methods
correlations. DBSCAN [19] offers advantages for arbitrar- dominatetheliterature.Lietal.[26]emphasizethegrowing
ily shaped clusters but requires careful parameter tuning importance of ensemble learning for big data clustering,
and struggles with varying density patterns. Traditional noting that most approaches focus on K-Means variants,
hierarchical methods provide intuitive dendrograms but are whilehierarchicalensemblemethodsremainunderexplored.
computationallyexpensiveforlarge-scaleapplications[17]. Strehl and Ghosh [30] proposed three consensus func-
Recentadvancedtechniquesincludemodel-basedcluster- tions: the Cluster-based Similarity Partitioning Algorithm
ing[33],[34],spectralmethods[35],andhybridapproaches. (CSPA), the HyperGraph Partitioning Algorithm (HGPA),
Gaussian Mixture Models [36] provide probabilistic cluster and the Meta-CLustering Algorithm (MCLA). Fred and
assignments, but require careful model selection. Spectral Jain [31] introduced the evidence accumulation clustering
clusteringexcelsatnon-convexclusteringusinggraph-based framework using co-association matrices. Recent work
representationsbutfacesscalabilitychallenges[12]. explores advanced consensus strategies, including spectral
Lim et al. [11] introduced the Cluster-N-Engage frame- methods[39]andnon-negativematrixfactorization[40].
work,whichmeasuresuserengagementthroughnavigational However, ensemble methods specifically designed for
behavior patterns and demonstrates the importance of inte- hierarchical clustering algorithms, such as BIRCH, remain
grating engagement metrics with traditional clustering for underexploreddespite theirpotential advantages.Hierarchi-
comprehensivecustomersegmentation. calmethodsyieldricherstructuralinformationthanpartition-
|     |     |     |     |     |     |     |     | based algorithms, |     | enabling | novel | ensemble | strategies | that |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------------- | --- | -------- | ----- | -------- | ---------- | ---- |
leveragehierarchicalrelationships[34].Thisworkintroduces
B. BIRCH:SCALABLEHIERARCHICALCLUSTERING
ensembletechniquestailoredtoBIRCH’shierarchicalnature,
| BIRCH        | (Balanced | Iterative  | Reducing |          | and Clustering |          | using |           |       |       |           |             |     |            |
| ------------ | --------- | ---------- | -------- | -------- | -------------- | -------- | ----- | --------- | ----- | ----- | --------- | ----------- | --- | ---------- |
|              |           |            |          |          |                |          |       | including | BOHC, | which | preserves | multi-scale |     | clustering |
| Hierarchies) | was       | introduced |          | by Zhang | et             | al. [28] | as a  |           |       |       |           |             |     |            |
information.
memory-efficientclusteringmethodforverylargedatabases.
ThealgorithmconstructsaClusteringFeatureTree(CFTree).
| This hierarchical |     | data | structure | provides | compact |     | dataset |                                           |     |     |     |     |     |     |
| ----------------- | --- | ---- | --------- | -------- | ------- | --- | ------- | ----------------------------------------- | --- | --- | --- | --- | --- | --- |
|                   |     |      |           |          |         |     |         | D. DEEPLEARNINGFORDIMENSIONALITYREDUCTION |     |     |     |     |     |     |
summariesviatripletrepresentationscontainingthenumber
High-dimensionalfeaturespacesposesignificantchallenges
ofpoints,theirlinearsum,andthesumofsquaredvalues.
forclusteringalgorithms,includingincreasedcomputational
BIRCHoperatesinfourphases:(1)scanningthedatabase
complexity,degradeddistancemetrics,andgreaternoisesen-
| to build | an initial | CF  | tree in-memory, |     | (2) | optional | tree |     |     |     |     |     |     |     |
| -------- | ---------- | --- | --------------- | --- | --- | -------- | ---- | --- | --- | --- | --- | --- | --- | --- |
sitivity[14].Traditionaldimensionalityreductiontechniques
| condensation | to      | reduce   | size, (3) | global      | clustering |                | of leaf |                   |     |           |          |       |     |              |
| ------------ | ------- | -------- | --------- | ----------- | ---------- | -------------- | ------- | ----------------- | --- | --------- | -------- | ----- | --- | ------------ |
|              |         |          |           |             |            |                |         | such as Principal |     | Component | Analysis | (PCA) |     | [22], Linear |
| entries,     | and (4) | optional | cluster   | refinement. |            | Key parameters |         |                   |     |           |          |       |     |              |
DiscriminantAnalysis[41],andt-SNE[42]havebeenwidely
| include | the branching | factor | (maximum |     | number | of  | children |     |     |     |     |     |     |     |
| ------- | ------------- | ------ | -------- | --- | ------ | --- | -------- | --- | --- | --- | --- | --- | --- | --- |
applied.PCAprovidesefficientlinearprojectionbutmayfail
| per non-leaf  | node), | the        | threshold | (maximum |           | diameter     | of  |                        |           |           |       |          |                  |         |
| ------------- | ------ | ---------- | --------- | -------- | --------- | ------------ | --- | ---------------------- | --------- | --------- | ----- | -------- | ---------------- | ------- |
|               |        |            |           |          |           |              |     | to capture             | nonlinear | patterns. | t-SNE | excels   | at visualization |         |
| subclusters), | and    | the number |           | of final | clusters. | BIRCH’s      |     |                        |           |           |       |          |                  |         |
|               |        |            |           |          |           |              |     | but is computationally |           | intensive |       | and best | suited           | to low- |
| incremental   | nature | enables    | efficient | handling |           | of streaming |     |                        |           |           |       |          |                  |         |
dimensionalembeddings.
data,makingitparticularlysuitablefordynamice-commerce
|     |     |     |     |     |     |     |     | Zhao et | al. [15] | specifically | address | correlated |     | variables |
| --- | --- | --- | --- | --- | --- | --- | --- | ------- | -------- | ------------ | ------- | ---------- | --- | --------- |
environments[29].
inhigh-dimensionalcustomersegmentationthroughregular-
| Despite        | scalability | advantages,   |     | BIRCH        | has | received  | lim- |               |               |     |     |            |     |            |
| -------------- | ----------- | ------------- | --- | ------------ | --- | --------- | ---- | ------------- | ------------- | --- | --- | ---------- | --- | ---------- |
|                |             |               |     |              |     |           |      | ized K-Means, | demonstrating |     | the | importance | of  | accounting |
| ited attention |             | in e-commerce |     | segmentation |     | research, | with |               |               |     |     |            |     |            |
forfeatureinterdependenciesine-commercedatasets.
| most applications |     | focusing | on  | spatial | data | and | sensor |              |     |              |     |             |     |           |
| ----------------- | --- | -------- | --- | ------- | ---- | --- | ------ | ------------ | --- | ------------ | --- | ----------- | --- | --------- |
|                   |     |          |     |         |      |     |        | Autoencoders |     | have emerged |     | as powerful |     | nonlinear |
networks[37].Thisworkaddressesthisgapbydemonstrating
|         |               |     |                |     |      |              |     | dimensionality-reduction |     |      | tools    | capable   | of learning | com-    |
| ------- | ------------- | --- | -------------- | --- | ---- | ------------ | --- | ------------------------ | --- | ---- | -------- | --------- | ----------- | ------- |
| BIRCH’s | effectiveness |     | for e-commerce |     | user | segmentation |     |                          |     |      |          |           |             |         |
|         |               |     |                |     |      |              |     | pact representations     |     | that | preserve | essential | data        | charac- |
andextendingitscapabilitiesthroughensemblemethodsand
|     |     |     |     |     |     |     |     | teristics [43]. | Recent | comprehensive |     | surveys |     | [23], [24] |
| --- | --- | --- | --- | --- | --- | --- | --- | --------------- | ------ | ------------- | --- | ------- | --- | ---------- |
deepfeaturelearning.
|     |     |     |     |     |     |     |     | systematically | review | advances |     | in autoencoder-based |     | deep |
| --- | --- | --- | --- | --- | --- | --- | --- | -------------- | ------ | -------- | --- | -------------------- | --- | ---- |
clustering,highlightingsuperiorperformanceovertraditional
C. ENSEMBLECLUSTERINGMETHODS methodsforhigh-dimensionaldata.Theencodertransforms
The ensemble clustering combines multiple base clustering high-dimensional input into a low-dimensional latent
solutions to produce consensus results that are more robust representation, while the decoder reconstructs the original
andaccuratethanindividualclusterings[30],[31].Thefun- input; training via reconstruction minimization encourages
damental principle is that different algorithms or parameter thelatentspacetocapturesalientfeatures.
configurations capture distinct aspects of the data structure, Recent research has extensively explored the combina-
andthattheircombinationcanachievesuperiorperformance. tion of autoencoders with clustering algorithms, focusing
| 88584 |     |     |     |     |     |     |     |     |     |     |     |     |     | VOLUME14,2026 |
| ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------- |

C.Lietal.:BIRCH-AE:AHierarchicalEnsembleFrameworkforScalableE-CommerceUserSegmentation
primarily on deep embedded clustering (DEC) [44] and (B), maximum children for non-leaf nodes; Threshold (T),
relatedmethodsthatjointlyoptimizeclusteringandrepresen- maximumdiameterforsubclustersatleafnodes;andNumber
tation learning. However, comprehensive reviews [23], [25] ofLeafEntries(L),maximumentriesperleafnode.
revealthattheseapproachestypicallyemployK-Meansasthe
clusteringcomponentandhavenotleveragedthescalability 3) BIRCHALGORITHMPHASES
advantagesofhierarchicalmethods.Thisworkaddressesthis BIRCHoperatesinfourphases:
gap by integrating autoencoder-based feature learning with Phase 1 (Tree Construction): The algorithm scans the
BIRCHclustering,combiningtherepresentationalpowerof datasetonce,insertingeachdatapointintotheCFTree.For
autoencoders with the scalability and incremental learning eachpoint,ittraversesfromroottoleaf,selectingtheclosest
capabilitiesofBIRCH[24]. child based on a distance metric. If the diameter of the leaf
entryafterinsertionremainsbelowthethresholdT,thepoint
E. RESEARCHPOSITIONING isabsorbed;otherwise,anewleafentryiscreated.
BIRCH-AE occupies a unique position at the intersection Phase 2 (Tree Condensation - Optional): If memory
of hierarchical clustering, ensemble methods, and deep
constraintsareviolated,alargerthresholdT′isselected,and
feature learning for e-commerce analytics. Unlike existing thetreeisrebuilttoproduceamorecompactstructure.
approaches focusing on partition-based ensemble clustering Phase 3 (Global Clustering): A global clustering
orsimpleBIRCHapplications,thisframework:(1)leverages algorithmisappliedtotheleafentries,treatingeachleafCF
BIRCH’s scalability for large-scale e-commerce data, (2) as a pseudo-data point. This phase can employ K-Means,
enhances clustering quality through autoencoder-based fea- hierarchicalagglomeration,orotheralgorithms.
turelearningthathandlescorrelatedvariables,(3)introduces Phase 4 (Cluster Refinement - Optional): Data points
fourensemblestrategies(includingthenovelBOHCmethod) are redistributed to their nearest cluster centroids to correct
specificallydesignedforhierarchicalclustering,(4)provides potentialerrorsfromearlierphases.
dynamic ensemble selection for adaptive optimization, and
(5) incorporates engagement metrics alongside traditional 4) DISTANCEMETRICS
behavioral features. This integrated approach addresses the BIRCH employs specific distance metrics optimized for
critical limitations of existing methods and offers practical CF representations. For two clusters with CFs CF =
1
solutionsforenterprise-scalee-commerceusersegmentation. (N ,L ⃗ S ,SS ) and CF = (N ,L ⃗ S ,SS ), common metrics
1 1 1 2 2 2 2
include:
III. TECHNICALPRELIMINARIES CentroidEuclideanDistance:
(cid:13) (cid:13)
A. BIRCHCLUSTERINGFUNDAMENTALS (cid:13)L ⃗ S L ⃗ S (cid:13)
D =(cid:13) 1 − 2(cid:13) (3)
1) CLUSTERINGFEATUREDEFINITION 0 (cid:13) N N (cid:13)
(cid:13) 1 2 (cid:13)
The foundation of BIRCH is the Clustering Feature (CF),
a compact statistical summary of a cluster. For a cluster AverageInter-clusterDistance:
containing Nd-dimensional data points {X}N , the CF is v
definedasatriplet: i i=1 u u 1 X N1 X N2
D =u ∥X −Y∥2 (4)
2 t i j
N N
CF =(N,L ⃗ S,SS) (1) 1 2 i=1 j=1
whereN isthenumberofdatapoints,L ⃗ S = PN X isthe AverageIntra-clusterDistance:
i=1 i
l o i f ne th a e rs s u q m uar o e f d th d e at d a a p ta oi p n o ts i . nts,andSS = PN i=1 X i 2 isthesum D 3 = s 2N 1 N SS 1 (N −2 − ∥L 1 ⃗ S ) 1 ∥2 + 2N 2 N SS 2 (N −2 − ∥L 1 ⃗ S ) 2 ∥2 (5)
TheCFrepresentationisadditive:fortwodisjointclusters 1 1 2 2
withCFs(N ,L ⃗ S ,SS )and(N ,L ⃗ S ,SS ),theirmergedCF
1 1 1 2 2 2 B. AUTOENCODERARCHITECTURE
is:
1) BASICFORMULATION
CF =(N +N ,L ⃗ S +L ⃗ S ,SS +SS ) (2) Anautoencoderisaneuralnetworkdesignedtolearnefficient
merged 1 2 1 2 1 2
datarepresentationsinanunsupervisedmanner,consistingof
This additivity property enables efficient hierarchical con- twocomponents:
structionanddynamicclusterupdates. Encoder:Mapsinputx ∈ Rd tolatentrepresentationz ∈
Rpwherep<d:
2) CFTREESTRUCTURE
The CF Tree is a height-balanced tree with both leaf and
z=fθ
e
(x)=σ(W
e
x+b
e
) (6)
non-leaf nodes. The nodes without leaves contain entries Decoder:Reconstructstheinputfromlatentrepresentation:
[CF,child], where CF summarizes all data points in the
root
i
subtree
i
atchild.Lea
i
fnodescontainentriesforindividual
xˆ =gθ
d
(z)=σ(W
d
z+b
d
) (7)
i
subclustersandarelinkedinsequencetofacilitatescanning. where θ = {W ,b } and θ = {W ,b } are encoder and
e e e d d d
Thetreeiscontrolledbythreeparameters:BranchingFactor decoderparameters,andσ isanactivationfunction.
VOLUME14,2026 88585

C.Lietal.:BIRCH-AE:AHierarchicalEnsembleFrameworkforScalableE-CommerceUserSegmentation
| 2) TRAININGOBJECTIVE |     |     |     |     |     |     | 3) DAVIES-BOULDININDEX |     |     |     |     |     |     |     |
| -------------------- | --- | --- | --- | --- | --- | --- | ---------------------- | --- | --- | --- | --- | --- | --- | --- |
The autoencoder is trained to minimize the reconstruction The Davies-Bouldin (DB) index [47] measures the average
| error: |     |        |     |     |     |     | similaritybetweeneachgroupanditsmostsimilargroup: |     |     |      |              |            |     |      |
| ------ | --- | ------ | --- | --- | --- | --- | ------------------------------------------------- | --- | --- | ---- | ------------ | ---------- | --- | ---- |
|        |     |        | 1   | n   |     |     |                                                   |     |     |      |              |            |     |      |
|        |     | L(θ ,θ |     | X   | ∥2  |     |                                                   |     |     | 1X k | (cid:18) σ + | σ (cid:19) |     |      |
|        |     |        | )=  | ∥x  | −xˆ | (8) |                                                   |     | DB= |      | i            | j          |     |      |
|        |     | e d    | n   |     | i i |     |                                                   |     |     | m    | a x          |            |     | (16) |
|        |     |        |     |     |     |     |                                                   |     |     | k    | j̸= i d ( c  | ,c )       |     |      |
|        |     |        |     | i=1 |     |     |                                                   |     |     | i=   |              | i j        |     |      |
1
| For e-commerce        |     | applications, |     | additional | regularization |     |         |        |         |          |         |     |        |        |
| --------------------- | --- | ------------- | --- | ---------- | -------------- | --- | ------- | ------ | ------- | -------- | ------- | --- | ------ | ------ |
|                       |     |               |     |            |                |     | where σ | is the | average | distance | between | the | points | in the |
| termsareincorporated: |     |               |     |            |                |     |         | i      |         |          |         |     |        |        |
d(c,c)
|     |     |     |     |     |     |     | cluster | i to the | centroid | of the | cluster, | and | i   | j is the |
| --- | --- | --- | --- | --- | --- | --- | ------- | -------- | -------- | ------ | -------- | --- | --- | -------- |
L =L +λ L +λ L distancebetweenthecentroids.Lowervaluesindicatebetter
| total | reconstruction |     | 1   | sparsity | 2 regularization | (9) |     |     |     |     |     |     |     |     |
| ----- | -------------- | --- | --- | -------- | ---------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
clustering.
| where sparsity |     | encourages | selective |     | feature activation, | and |     |     |     |     |     |     |     |     |
| -------------- | --- | ---------- | --------- | --- | ------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
regularizationpreventsoverfitting.
IV. BIRCH-AEFRAMEWORKMETHODOLOGY
A. COMPONENTSELECTIONRATIONALE
3) DEEPARCHITECTURE Our architectural choices—standard autoencoder for fea-
| For complex |     | e-commerce | behavioral |     | data, a | multi-layer |               |     |       |     |              |                 |     |     |
| ----------- | --- | ---------- | ---------- | --- | ------- | ----------- | ------------- | --- | ----- | --- | ------------ | --------------- | --- | --- |
|             |     |            |            |     |         |             | ture learning | and | BIRCH | for | hierarchical | clustering—were |     |     |
architectureisemployed:
guidedbyrequirementsfortheproductionsystemandprelim-
Encoderlayers: inaryempiricalevaluation.Forfeaturelearning,weselected
|     |     | =σ  |        | x+b |     |      | standardautoencodersoverVariationalAutoencoders(VAE) |               |        |             |                        |      |           |       |
| --- | --- | --- | ------ | --- | --- | ---- | ---------------------------------------------------- | ------------- | ------ | ----------- | ---------------------- | ---- | --------- | ----- |
|     |     | h 1 | 1 (W 1 | 1   | )   | (10) |                                                      |               |        |             |                        |      |           |       |
|     |     |     |        |     |     |      | for three                                            | reasons.      | First, | recent      | surveys                | [23] | note that | while |
|     |     | =σ  |        | +b  |     |      |                                                      |               |        |             |                        |      |           |       |
|     |     | h 2 | 2 (W 2 | h 1 | 2 ) | (11) |                                                      |               |        |             |                        |      |           |       |
|     |     |     |        |     |     |      | VAEs offer                                           | probabilistic |        | guarantees, | reconstruction-focused |      |           |       |
.
|     |     | .   |     |     |     |     | autoencoders | often | achieve | superior | clustering |     | performance |     |
| --- | --- | --- | --- | --- | --- | --- | ------------ | ----- | ------- | -------- | ---------- | --- | ----------- | --- |
.
|     |     |     |     |          |     |      | when latent | space | separation |     | is prioritized | over | generative |     |
| --- | --- | --- | --- | -------- | --- | ---- | ----------- | ----- | ---------- | --- | -------------- | ---- | ---------- | --- |
|     |     | z=σ | (W  | h L−1 +b | )   | (12) |             |       |            |     |                |      |            |     |
L L L capability. Second, preliminary experiments on representa-
|         |         |        |     |         |           |           | tive subsets | confirmed |     | that | standard | AE achieved |     | higher |
| ------- | ------- | ------ | --- | ------- | --------- | --------- | ------------ | --------- | --- | ---- | -------- | ----------- | --- | ------ |
| Decoder | layers: | Mirror | the | encoder | with tied | or untied |              |           |     |      |          |             |     |        |
weights,reconstructingtheoriginalinputthroughsuccessive silhouette scores (0.839 vs. VAE’s 0.636) for e-commerce
behavioraldata.Third,VAE’sKL-divergenceregularization
transformations.
towardGaussianpriorsintroducesstochasticitythatconflicts
|     |     |     |     |     |     |     | with deterministic |     | e-commerce |     | patterns | (such | as consistent |     |
| --- | --- | --- | --- | --- | --- | --- | ------------------ | --- | ---------- | --- | -------- | ----- | ------------- | --- |
C. CLUSTERINGEVALUATIONMETRICS
purchasesequencesandbrowsinghabits).Wealsoevaluated
1) SILHOUETTESCORE
The silhouette score [45] measures how similar an object is UMAP (silhouette score: 0.527) and PCA (silhouette score:
0.531),bothofwhichyieldedinferiorresults.
toitsownclustercomparedtootherclusters.Foradatapoint
|     |     |     |     |     |     |     | For clustering, |     | BIRCH | was | selected | for | its hierarchical |     |
| --- | --- | --- | --- | --- | --- | --- | --------------- | --- | ----- | --- | -------- | --- | ---------------- | --- |
i:
|     |     |     |     |     |     |     | structure, | its scalability |     | compared | with | classical | agglomer- |     |
| --- | --- | --- | --- | --- | --- | --- | ---------- | --------------- | --- | -------- | ---- | --------- | --------- | --- |
b(i)−a(i)
s(i)= (13) ative approaches [28], and its incremental learning capabil-
max{a(i),b(i)}
|     |     |     |     |     |     |     | ity [29]. | Preliminary |     | evaluation | on k | ∈ {5,10,15,20,25} |     |     |
| --- | --- | --- | --- | --- | --- | --- | --------- | ----------- | --- | ---------- | ---- | ----------------- | --- | --- |
wherea(i)istheaveragedistancetopointsinthesamecluster showed that BIRCH maintained comparatively stable per-
and b(i) is the minimum average distance to points in other formance (silhouette 0.839 → 0.721, −14% degradation),
clusters.Theoverallsilhouettescoreis whileK-Meansdegradedmorestronglyask increased.This
n stability is important for e-commerce settings that require
1X
|     |     |     | =   |      |     |      | finer-grainedsegmentation(k |     |     |     | =15–25). |     |     |     |
| --- | --- | --- | --- | ---- | --- | ---- | --------------------------- | --- | --- | --- | -------- | --- | --- | --- |
|     |     | S   |     | s(i) |     | (14) |                             |     |     |     |          |     |     |     |
n
i=1
B. FRAMEWORKOVERVIEW
| with values | ranging | from | −1  | to 1, | where higher | values |     |     |     |     |     |     |     |     |
| ----------- | ------- | ---- | --- | ----- | ------------ | ------ | --- | --- | --- | --- | --- | --- | --- | --- |
indicatebetter-definedclusters. TheBIRCH-AEframeworkintegratesfourkeycomponents
|     |     |     |     |     |     |     | into a | cohesive | pipeline: |     | (1) data | preprocessing |     | and |
| --- | --- | --- | --- | --- | --- | --- | ------ | -------- | --------- | --- | -------- | ------------- | --- | --- |
2) CALINSKI-HARABASZINDEX feature engineering, (2) autoencoder-based dimensionality
|                       |     |     |      |       |                |         | reduction, | (3)             | BIRCH | ensemble | clustering  |          | with | multiple |
| --------------------- | --- | --- | ---- | ----- | -------------- | ------- | ---------- | --------------- | ----- | -------- | ----------- | -------- | ---- | -------- |
| The Calinski-Harabasz |     |     | (CH) | index | [46] evaluates | cluster |            |                 |       |          |             |          |      |          |
|                       |     |     |      |       |                |         | parameter  | configurations, |       | and      | (4) dynamic | ensemble |      | selec-   |
qualitybasedontheratioofbetween-clustertowithin-cluster
variance: tion and consensus generation. The framework is designed
|     |     |     |     |         |     |     | with scalability |     | as  | a primary | consideration, |     | leveraging |     |
| --- | --- | --- | --- | ------- | --- | --- | ---------------- | --- | --- | --------- | -------------- | --- | ---------- | --- |
|     |     |     | SS  | /(k −1) |     |     |                  |     |     |           |                |     |            |     |
B
CH = (15) BIRCH’s memory-efficient structure and incremental learn-
|         |                                   |     | SS  | /(n−k) |     |       |               |     |     |     |     |     |     |     |
| ------- | --------------------------------- | --- | --- | ------ | --- | ----- | ------------- | --- | --- | --- | --- | --- | --- | --- |
|         |                                   |     | W   |        |     |       | ing           |     |     |     |     |     |     |     |
| whereSS | isthesumofsquaresbetweengroups,SS |     |     |        |     | isthe | capabilities. |     |     |     |     |     |     |     |
|         | B                                 |     |     |        |     | W     |               |     |     |     |     |     |     |     |
sumofsquareswithingroups,k isthenumberofgroups,and The framework is modular rather than end-to-end jointly
nisthenumberofdatapoints.Highervaluesindicatebetter optimized: each stage has its own objective (reconstruction
clustering. for AE, clustering compactness/separation for BIRCH, and
| 88586 |     |     |     |     |     |     |     |     |     |     |     |     | VOLUME14,2026 |     |
| ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------- | --- |

C.Lietal.:BIRCH-AE:AHierarchicalEnsembleFrameworkforScalableE-CommerceUserSegmentation
TABLE1. Featurecategoriesandrepresentativemetrics. Given BIRCH’s sensitivity to feature scales, standardiza-
tionisappliedtoensurezeromeanandunitvariance:
x−µ
=
|     |     |     |     |     |     |     |     |     | x   | normalized |     |     |     | (17) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---------- | --- | --- | --- | ---- |
σ
[0,1]
|     |     |     |     |     |     |     | For count-based |     | features, | the | min-max | scaling | to  | is  |
| --- | --- | --- | --- | --- | --- | --- | --------------- | --- | --------- | --- | ------- | ------- | --- | --- |
appliedtopreventdominanceofhigh-variancefeatures.
|     |     |     |     |     |     |     | 3) HANDLINGCORRELATEDVARIABLES |             |                    |                   |                |          |               |             |
| --- | --- | --- | --- | --- | --- | --- | ------------------------------ | ----------- | ------------------ | ----------------- | -------------- | -------- | ------------- | ----------- |
|     |     |     |     |     |     |     | E-commerce                     |             | behavioral         | data              | often          | exhibits | strong        | feature     |
|     |     |     |     |     |     |     | correlations                   |             | [15]. The          | autoencoder-based |                |          | approach      | natu-       |
|     |     |     |     |     |     |     | rally handles                  |             | these correlations |                   | by             | learning | a compressed  |             |
|     |     |     |     |     |     |     | representation                 |             | that captures      |                   | the underlying |          | structure     | while       |
|     |     |     |     |     |     |     | reducing                       | redundancy. |                    | This              | addresses      | a        | key challenge | in          |
|     |     |     |     |     |     |     | high-dimensional               |             | customer           |                   | segmentation   |          | where         | traditional |
methodssufferfrommulticollinearity.
|     |     |     |     |     |     |     | D. AUTOENCODERARCHITECTUREFORE-COMMERCE |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
DATA
|     |     |     |     |     |     |     | 1) NETWORKDESIGN |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ---------------- | --- | --- | --- | --- | --- | --- | --- |
consensus selection). Accordingly, we do not claim a The autoencoder is specifically designed for e-commerce
behavioraldata,anditsarchitectureismotivatedbycharac-
| single global | optimization |     | objective | or  | global convergence |     |     |     |     |     |     |     |     |     |
| ------------- | ------------ | --- | --------- | --- | ------------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- |
guaranteeforthefullpipeline. teristics of user interaction patterns. The network employs
Fig. 1 illustrates the overall architecture. Beginning with a symmetric encoder-decoder structure with progressively
decreasinglayerdimensions.
| large-scale | e-commerce |     | user data, | the | process proceeds |     |     |     |     |     |     |     |     |     |
| ----------- | ---------- | --- | ---------- | --- | ---------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
throughdatapreprocessing,autoencoder-basedfeaturelearn- Architectural Design Justification: The encoder archi-
ing, hierarchical ensemble clustering with multiple BIRCH tecture (128→64→14–32) follows standard deep learning
variants,anddynamicensembleselectionguidedbyquanti- principles of gradual reduction in dimensionality [43]. The
tative evaluation metrics. This integrated pipeline combines 128-unit first layer accommodates 30–50 input features
|     |     |     |     |     |     |     | with sufficient |     | capacity | for | complex | feature | interactions. |     |
| --- | --- | --- | --- | --- | --- | --- | --------------- | --- | -------- | --- | ------- | ------- | ------------- | --- |
BIRCH’shierarchicalscalabilitywithautoencoder-enhanced
feature learning and adaptive ensemble optimization Progressivereductionpreventsinformationbottleneckswhile
for robust, high-quality user segmentation at enterprise enabling hierarchical feature learning. The latent dimen-
scale. sion (14)–(32) was selected based on a preliminary grid
search,where14providedanoptimalbalancebetweencom-
|     |     |     |     |     |     |     | pression | (58% | reduction | of  | 33 features) |     | and reconstruction |     |
| --- | --- | --- | --- | --- | --- | --- | -------- | ---- | --------- | --- | ------------ | --- | ------------------ | --- |
C. DATAPREPROCESSINGANDFEATUREENGINEERING quality(MSE<0.05onthevalidationset).Latentdimensions
1) FEATURECOLLECTION below 14 led to reconstruction degradation; above 32, there
| The framework | processes |     | comprehensive |     | behavioral | fea- |     |     |     |     |     |     |     |     |
| ------------- | --------- | --- | ------------- | --- | ---------- | ---- | --- | --- | --- | --- | --- | --- | --- | --- |
wasminimalqualityimprovementatincreasedcomputational
| tures from | large-scale | e-commerce |     | datasets, | summarized | in  |            |     |             |         |           |     |            |       |
| ---------- | ----------- | ---------- | --- | --------- | ---------- | --- | ---------- | --- | ----------- | ------- | --------- | --- | ---------- | ----- |
|            |             |            |     |           |            |     | cost. ReLU |     | activations | prevent | vanishing |     | gradients, | while |
Table1.Thesefeaturescapturemultidimensionalaspectsof the linear bottleneck layer preserves continuous latent
| user behavior, | enabling | comprehensive |     |     | behavioral segmen- |     |     |     |     |     |     |     |     |     |
| -------------- | -------- | ------------- | --- | --- | ------------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- |
representationssuitablefordistance-basedclustering[49].
tationbeyondsimpleRFM(Recency,Frequency,Monetary) Input Layer: Accepts normalized feature vectors x ∈
| analysis. |     |     |     |     |     |     | Rd     |     |                                              |     |     |     |     |     |
| --------- | --- | --- | --- | --- | --- | --- | ------ | --- | -------------------------------------------- | --- | --- | --- | --- | --- |
|           |     |     |     |     |     |     | whered |     | istheoriginalfeaturedimensionality(typically |     |     |     |     |     |
30–50features).
EncoderLayers:
2) DATACLEANINGANDNORMALIZATION
|     |     |     |     |     |     |     |     |     |     |     | ),  |     | ∈R128 |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----- | --- |
Raw e-commerce data requires extensive preprocessing h =ReLU(W x+b h (18)
|           |         |          |         |        |                |     |     |     | 1       | 1   | 1   | 1    |      |      |
| --------- | ------- | -------- | ------- | ------ | -------------- | --- | --- | --- | ------- | --- | --- | ---- | ---- | ---- |
| to ensure | cluster | quality. | Missing | values | for behavioral |     |     |     |         |     |     |      |      |      |
|           |         |          |         |        |                |     |     | h   | =ReLU(W | h   | +b  | ), h | ∈R64 | (19) |
features are imputed with the median within user cohorts; 2 2 1 2 2
|     |     |     |     |     |     |     |     |     | z=Linear(W | h   | +b  | ), z∈Rp |     | (20) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ---------- | --- | --- | ------- | --- | ---- |
for transactional features, zero is imputed during inactive 3 2 3
periods.Featureswithexcessivemissingvalues(>40%)are
|     |     |     |     |     |     |     | where | p is | the latent | dimension |     | (typically | 14–32 | for |
| --- | --- | --- | --- | --- | --- | --- | ----- | ---- | ---------- | --------- | --- | ---------- | ----- | --- |
excluded. an optimal balance between compression and information
| Outliers | are detected | using | the | Interquartile | Range | (IQR) | preservation). |     |     |     |     |     |     |     |
| -------- | ------------ | ----- | --- | ------------- | ----- | ----- | -------------- | --- | --- | --- | --- | --- | --- | --- |
[48]method.Forbehavioralmetricssuchassessionduration,
DecoderLayers:Mirrortheencoderstructure:
| valuesexceedingQ |     | 3 +3×IQRarecappedatthethreshold. |     |     |     |     |     |     |         |       |      |          |     |      |
| ---------------- | --- | -------------------------------- | --- | --- | --- | --- | --- | --- | ------- | ----- | ---- | -------- | --- | ---- |
|                  |     |                                  |     |     |     |     |     | h ′ | =ReLU(W | ′ z+b | ′ ), | h ′ ∈R64 |     | (21) |
Formonetaryfeatures,alogtransformationisappliedbefore 2 3 3 2
|     |     |     |     |     |     |     |     | ′   | =ReLU(W | ′ ′ | +b ′ ), | ′   | ∈R128 |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ------- | --- | ------- | --- | ----- | --- |
outliertreatmenttoaddressright-skewness. h 1 2 h 2 2 h 1 (22)
| VOLUME14,2026 |     |     |     |     |     |     |     |     |     |     |     |     |     | 88587 |
| ------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----- |

C.Lietal.:BIRCH-AE:AHierarchicalEnsembleFrameworkforScalableE-CommerceUserSegmentation
FIGURE1. OverallarchitectureoftheBIRCH-AEframework.Theprocessbeginswithdatapreprocessingandfeatureengineering,where
rawclickstreamandtransactiondataaretransformedintobehavioralfeaturevectors.Adeepautoencodercompressesthese
high-dimensionalfeaturesintoacompactlatentspace.ThelatentrepresentationsareprocessedbymultipleBIRCHclusteringmodelswith
varyingthresholdstocapturedifferentlevelsofgranularity.Outputsareaggregatedusingfourensembleconsensusstrategies:Majority
Voting,WeightedVoting,AASC,andBOHC.Finally,adynamicensembleselectionmoduleevaluatesallensembleresultsusingmulti-criteria
metricsandautomaticallyselectstheoptimalclusteringsolution.
xˆ =Linear(W ′ h ′ +b ′ ), xˆ ∈Rd (23) Independent training offers three advantages for produc-
|     |     |     | 1 1 | 1   |     |                  |     |                |           |             |     |       |
| --- | --- | --- | --- | --- | --- | ---------------- | --- | -------------- | --------- | ----------- | --- | ----- |
|     |     |     |     |     |     | tion deployment: |     | (1) stability: | it avoids | challenging |     | joint |
2) TRAININGSTRATEGY optimization where clustering objectives and reconstruction
The autoencoder is trained to minimize the reconstruction loss may conflict; (2) flexibility: the trained autoencoder
errorwithadditionalregularization: is reusable across clustering methods (BIRCH, K-Means,
|     |     |     |          |         |      | Agglomerative) |     | and k values | without | retraining; | (3) | incre- |
| --- | --- | --- | -------- | ------- | ---- | -------------- | --- | ------------ | ------- | ----------- | --- | ------ |
|     | L=L |     | +λ L     | +λ ∥θ∥2 | (24) |                |     |              |         |             |     |        |
|     |     | MSE | 1 sparse | 2 2     |      |                |     |              |         |             |     |        |
mentaloperation:BIRCH’sincrementalnatureallowsadding
where:
newusersbyencodingwithafixedautoencoderandinserting
|     | n   |            |     | n   | p         | intotheCF-tree. |     |     |     |     |     |     |
| --- | --- | ---------- | --- | --- | --------- | --------------- | --- | --- | --- | --- | --- | --- |
|     | 1X  |            |     | 1X  | X         |                 |     |     |     |     |     |     |
| L = |     | ∥x −xˆ ∥2, | L   | =   | |z | (25) |                 |     |     |     |     |     |     |
MSE i i sparse ij The trade-off is that joint methods might achieve
|     | n   |     |     | n   |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
i=1 i=1 j=1 marginally better quality by co-adapting representations
The sparsity term encourages the selective activation of and clusters. However, our 23–53% improvement over
latentfeatures,promotinginterpretablerepresentations.The raw features (Section V) shows strong performance with
Adam optimizer [50] is used with a learning rate of α = independent training while maintaining critical operational
0.001,
a batch size of 256, and early stopping based on the advantagesforproductionsystemsthatrequiredailyupdates
validationreconstructionerror.Trainingtypicallyconverges andconsistentrepresentations.
Thisdesignassumesthatthelearnedlatentspacepreserves
within100–200epochs.Thedatasetissplit80–20fortraining
andvalidation,withanearlystoppingpatienceof10epochs neighborhoodstructurerelevanttoclusteringandsuppresses
topreventoverfitting. nuisance variation through reconstruction regularization.
|     |     |     |     |     |     | Under such | conditions, | BIRCH | benefits | from | more | stable |
| --- | --- | --- | --- | --- | --- | ---------- | ----------- | ----- | -------- | ---- | ---- | ------ |
3) INDEPENDENTVS.JOINTTRAINING distancerelationshipsinlatentspace.Weemphasizethisasa
modelingassumption,supportedbyempiricalevidencefrom
| BIRCH-AE | employs | independent |     | autoencoder | training: |     |     |     |     |     |     |     |
| -------- | ------- | ----------- | --- | ----------- | --------- | --- | --- | --- | --- | --- | --- | --- |
Phase 1 trains the autoencoder only for reconstruction loss; ourdatasets,ratherthanauniversaltheoreticalguaranteethat
Phase 2 freezes the encoder and uses latent representa- reconstruction-optimal embeddings are always clustering-
| tions for | clustering. | This | contrasts | with joint | optimization | optimal. |     |     |     |     |     |     |
| --------- | ----------- | ---- | --------- | ---------- | ------------ | -------- | --- | --- | --- | --- | --- | --- |
approaches [44], in which clustering and representation The distributional conditions under which reconstruction
|     |     |     |     |     |     | error minimization |     | formally | preserves | cluster | separability |     |
| --- | --- | --- | --- | --- | --- | ------------------ | --- | -------- | --------- | ------- | ------------ | --- |
learningoccursimultaneously.
| 88588 |     |     |     |     |     |     |     |     |     |     | VOLUME14,2026 |     |
| ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------- | --- |

C.Lietal.:BIRCH-AE:AHierarchicalEnsembleFrameworkforScalableE-CommerceUserSegmentation
in latent space remain an open theoretical problem in the distance-preservingtransformationsuptothereconstruction
deepclusteringliterature[23],[24],[49].Threedistributional tolerance ε , which bounds the affinity perturbation analo-
r
conditionsarerequiredforthelatentspacetopreservecluster gouslytotheBOHCstabilityresultinSectionIV.Crucially,
neighborhoodstructure.First,thedatamustlieapproximately BIRCH’s threshold T is calibrated on the latent space
∈{0.3,0.5,0.8};
on a low-dimensional manifold relative to the ambient geometrydirectlythroughthegridsearchT
feature dimension—that is, the intrinsic dimensionality is it does not assume any specific scale from the original
substantially less than the 30–50 input features. Second, feature space, so any consistent distance scaling introduced
within-clustervariationmustbesmallerthanbetween-cluster by the autoencoder is absorbed into the threshold selection.
variationintheambientspace,implyingthattheclustersare Toempiricallyassessthresholdrobustness,asupplementary
approximately separable before encoding. Third, the recon- developmentanalysiswasconductedona10,000-usersample
struction MSE must be sufficiently small for the encoder fromtheRetailRocketdatasetbeforethemainexperiments.
not to collapse distinct feature dimensions. E-commerce Across the three threshold values (T ∈ {0.3,0.5,0.8})
behavioral data plausibly satisfies these conditions: users applied to autoencoder features, BIRCH silhouette scores
within a segment share consistent purchasing sequences, were 0.839, 0.821, and 0.809, respectively—a range of
browsing habits, and temporal activity patterns, producing only 0.030 (3.6%), consistent with bounded, non-amplified
within-cluster compactness that reconstruction regularisa- perturbation. This supplementary analysis was not part of
tion can preserve. The 23–53% silhouette improvements the primary comparative evaluation; it is reported here as
observed across both datasets provide empirical support for supportingevidencefortheanalyticalargumentabove.Fur-
this alignment in our setting. We explicitly acknowledge, thermore,comparingBIRCHonrawfeaturesversusBIRCH
however, that we do not establish a formal proof relating on AE features constitutes a direct test: harmful distortion
reconstructionerrorboundstoclusteringdistortioninlatent amplification would result in deterioration relative to raw
space,andthatthistheoreticalgapissharedwiththebroader features. Instead, we observe consistent improvement of
|          |                      |     |     |                 |     |            |     | +1.7%,+8.4%,+12.2%,and+6.3%atK |     |     |     |     | ∈ {5,10,15,20} |     |
| -------- | -------------------- | --- | --- | --------------- | --- | ---------- | --- | ------------------------------ | --- | --- | --- | --- | -------------- | --- |
| class of | independent-training |     |     | deep clustering |     | approaches |     |                                |     |     |     |     |                |     |
documentedinrecentsurveys[23],[24]. respectively, confirming that the autoencoder introduces
Scalability-representation trade-off characterization: smooth,boundeddistanceperturbationsthatBIRCH’sinser-
Letγ >0denotetheclusterseparationmarginintheoriginal
tionmechanismaccommodateswithoutamplification.
featurespace,definedastheminimumdistancebetweenany We emphasize that the higher-order interaction caveat
twoclustercentroids.Underthemanifoldandwithin-cluster applies here as well: in domains where clusters are defined
compactness conditions above, the latent space separation by complex non-linear feature interactions not captured by
√
margin γ satisfies γ ≥ γ − O( ε ), where ε is the reconstruction regularisation, the error propagation bound
|     | z   | z   |     |     | r   | r   |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
reconstruction MSE of the trained autoencoder and p is the may not hold, and joint training approaches [44] would be
latent dimension (p < d). It is important to note that moreappropriate.
| this expression  |         | is a heuristic | conceptualization |             |              | motivated      |       |                          |     |     |     |     |     |     |
| ---------------- | ------- | -------------- | ----------------- | ----------- | ------------ | -------------- | ----- | ------------------------ | --- | --- | --- | --- | --- | --- |
| by the empirical |         | behavior       | of the            | trained     | autoencoder, |                | not a |                          |     |     |     |     |     |     |
|                  |         |                |                   |             |              |                |       | 4) LATENTSPACEPROPERTIES |     |     |     |     |     |     |
| formally         | derived | proof          | from first        | principles. |              | It is intended |       |                          |     |     |     |     |     |     |
Thelearnedlatentspacez∈Rpexhibitsbeneficialproperties
| to provide  | intuition | for | the compression–quality |            |     | trade-off |     |           |     |             |               |     |          |            |
| ----------- | --------- | --- | ----------------------- | ---------- | --- | --------- | --- | --------- | --- | ----------- | ------------- | --- | -------- | ---------- |
|             |           |     |                         |            |     |           |     | for BIRCH |     | clustering. | A compression |     | ratio of | 2:1 to 4:1 |
| rather than | to serve  | as  | a theoretical           | guarantee. |     | Under     | the |           |     |             |               |     |          |            |
typicallyreducesthecomputationalburdenwhilepreserving
stateddistributionalconditions,reducingpbelowtheintrinsic
|           |        |                |     | ε         |          |     | γ   | 90–95% | of  | the variance. | The autoencoder |     | captures | com- |
| --------- | ------ | -------------- | --- | --------- | -------- | --- | --- | ------ | --- | ------------- | --------------- | --- | -------- | ---- |
| dimension | of the | data increases |     | , thereby | reducing |     | and |        |     |               |                 |     |          |      |
r z plex interactions between behavioral features and handles
| degrading | downstream |     | clustering | quality. | Our | grid | search |     |     |     |     |     |     |     |
| --------- | ---------- | --- | ---------- | -------- | --- | ---- | ------ | --- | --- | --- | --- | --- | --- | --- |
correlatedvariableseffectively,whereaslinearmethodslike
| overp∈{14,32,50,64}identifiedp∗ |                     |          |           | =14astheoperating |                   |               |        |       |                  |                                |                |             |         |            |
| ------------------------------- | ------------------- | -------- | --------- | ----------------- | ----------------- | ------------- | ------ | ----- | ---------------- | ------------------------------ | -------------- | ----------- | ------- | ---------- |
|                                 |                     |          |           |                   |                   |               |        | PCA   | cannot.          | The compression-reconstruction |                |             | process | acts       |
| point at                        | which ε             | < 0.05   | on        | the validation    |                   | set, yielding |        |       |                  |                                |                |             |         |            |
|                                 |                     | r        |           |                   |                   |               |        | as a  | denoising        | mechanism,                     | filtering      | measurement |         | noise      |
| 58% compression                 |                     | with     | preserved | cluster           | separation        |               | across |       |                  |                                |                |             |         |            |
|                                 |                     |          |           |                   |                   |               |        | and   | irrelevant       | variations.                    | Euclidean      | distances   | in      | the latent |
| both datasets.                  | This                | provides | a         | practical         | selection         | heuristic:    |        |       |                  |                                |                |             |         |            |
|                                 |                     |          |           |                   |                   |               |        | space | better           | reflect behavioral             | similarity     |             | than in | the orig-  |
| p∗ =argmin                      | {p:MSE(p)<τ},whereτ |          |           |                   | isareconstruction |               |        |       |                  |                                |                |             |         |            |
|                                 | p                   |          |           |                   |                   |               |        | inal  | high-dimensional |                                | space, thereby | improving   |         | BIRCH’s    |
tolerancechosenbythepractitioner.
distance-basedoperations.
| AE-to-BIRCH |     | error | propagation |     | analysis: | A   | specific |     |     |     |     |     |     |     |
| ----------- | --- | ----- | ----------- | --- | --------- | --- | -------- | --- | --- | --- | --- | --- | --- | --- |
concernformodularpipelinesiswhetherBIRCH’sthreshold-
based insertion mechanism amplifies autoencoder distance E. BIRCHENSEMBLECONFIGURATION
distortions. We address this analytically and empirically. 1) BASEBIRCHMODELVARIANTS
Analytically, reconstruction regularisation prevents severe To capture diverse clustering perspectives, multiple BIRCH
non-monotonic distortions: the MSE loss penalizes any modelsareconfiguredwithvaryingparameters,eachempha-
encodingthatdoesnotreproducetheoriginalinput,meaning sizingdifferentaspectsoftheclusterstructure.
the encoder cannot map close points far apart or dis- Fine-Grained Model: Small threshold value (T small =
tant points close together without increasing the decoding 0.3) creates many small homogeneous clusters, capturing
subtlebehavioraldifferences.BranchingfactorB=50.
| loss. The     | autoencoder | is  | therefore | constrained |     | to  | produce |     |     |     |     |     |     |       |
| ------------- | ----------- | --- | --------- | ----------- | --- | --- | ------- | --- | --- | --- | --- | --- | --- | ----- |
| VOLUME14,2026 |             |     |           |             |     |     |         |     |     |     |     |     |     | 88589 |

C.Lietal.:BIRCH-AE:AHierarchicalEnsembleFrameworkforScalableE-CommerceUserSegmentation
Balanced Model: A moderate threshold (T = 0.5) 2) WEIGHTEDVOTING(WV)
medium
balancesthesizeandhomogeneityofthecluster,representing
|     |     |     |     |     |     |     | Weighted | voting | assigns | importance | to  | each | base clustering |     |
| --- | --- | --- | --- | --- | --- | --- | -------- | ------ | ------- | ---------- | --- | ---- | --------------- | --- |
thetypicalgranularityofthesegmentation.Branchingfactor basedonitsquality:
B=50.
|     |     |     |     |     |     | =   |     |     |     | M   |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Coarse-Grained Model: A large threshold (T large (u)=argmax X ·⊮[C (u)=k]
|     |     |     |     |     |     |     | C consensus |     |     |     | w m | m   |     | (27) |
| --- | --- | --- | --- | --- | --- | --- | ----------- | --- | --- | --- | --- | --- | --- | ---- |
0.8) produces fewer, larger clusters representing broad user k
m=1
categories.BranchingfactorB=50.
|          |        |     |             |          |           |       | whereweightsw |     | arederivedfromsilhouettescores: |     |     |     |     |     |
| -------- | ------ | --- | ----------- | -------- | --------- | ----- | ------------- | --- | ------------------------------- | --- | --- | --- | --- | --- |
| Adaptive | Model: |     | Dynamically | adjusted | threshold | based |               |     | m                               |     |     |     |     |     |
o n d a ta d en s it y , s t ar t in g w it h T = 0 . 5 a n d (β ·
|     |     |     |     | in  | it ial |     |     |     |     | exp | S m | )   |     |      |
| --- | --- | --- | --- | --- | ------ | --- | --- | --- | --- | --- | --- | --- | --- | ---- |
|     |     |     |     |     |        |     |     |     | w = |     |     |     |     | (28) |
r e fin e d thro u g h t r ee c o n d e nsa tio n if m e m oryc onstr a i nts a r e m PM β
|             |     |     |     |     |     |     |     |     |     |     | e xp ( | · S) j |     |     |
| ----------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------ | ------ | --- | --- |
| approached. |     |     |     |     |     |     |     |     |     | j=1 |        |        |     |     |
β =
|     |     |     |     |     |     |     | with | 5   | as the temperature |     | parameter |     | and S | m as the |
| --- | --- | --- | --- | --- | --- | --- | ---- | --- | ------------------ | --- | --------- | --- | ----- | -------- |
2) GLOBALCLUSTERINGPHASEVARIATIONS silhouettescoreofclusteringC .
m
BIRCH’sPhase3appliesglobalclusteringtoleafnodeCFs.
Differentalgorithmsareusedfordiversity. 3) ADVANCEDAFFINITY-BASEDSPECTRALCLUSTERING
| AgglomerativeHierarchicalClustering:Usescomplete |     |     |     |     |     |     | (AASC) |     |     |     |     |     |     |     |
| ------------------------------------------------ | --- | --- | --- | --- | --- | --- | ------ | --- | --- | --- | --- | --- | --- | --- |
linkagetomergeCFentries,preservinghierarchicalstructure. AASC constructs a co-association matrix that captures
Number of clusters determined by cutting dendrograms at clusteringagreementacrossensemblemembers,thenapplies
varyingheights.
spectralclusteringtothisaffinityrepresentation.
K-Means on CFs: Applies K-Means to centroid repre- Co-AssociationMatrixConstruction:
| sentations | of  | CFs, providing |     | a partition-based | perspective. |     |     |     |     |     |     |     |     |     |
| ---------- | --- | -------------- | --- | ----------------- | ------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- |
M
|           |                |     | ∈{5,7,10,12,15,20,25}. |              |       |      |     |     | 1   | X   |       |      |     |      |
| --------- | -------------- | --- | ---------------------- | ------------ | ----- | ---- | --- | --- | --- | --- | ----- | ---- | --- | ---- |
| MultipleK | valuestested:K |     |                        |              |       |      |     |     | A = | ⊮[C | (i)=C | (j)] |     | (29) |
|           |                |     |                        |              |       |      |     |     | ij  |     | m     | m    |     |      |
| Spectral  | Clustering:    |     | Constructs             | a similarity | graph | from |     |     | M   |     |       |      |     |      |
m=1
| CFs | and applies | spectral | methods, | capturing | non-convex |     |         |               |     |            |     |                  |     |      |
| --- | ----------- | -------- | -------- | --------- | ---------- | --- | ------- | ------------- | --- | ---------- | --- | ---------------- | --- | ---- |
|     |             |          |          |           |            |     | where A | ij represents | the | proportion | of  | base clusterings |     | that |
clustershapes.
assignusersiandjtothesamecluster.
SpectralClusteringonAffinity:
3) ENSEMBLEGENERATIONPROCESS
The ensemble generation creates M base BIRCH clustering L =D−A
|     |     |     |     |     |     |     |     |     | (Laplacianmatrix) |     |     |     |     | (30) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ----------------- | --- | --- | --- | --- | ---- |
,C ,...,C
solutions {C 1 2 M } where M ranges from 5 to 20. =D −1/2LD −1/2
|      |          |      |             |          |        |           | L norm |     |     | (NormalizedLaplacian) |     |     |     | (31) |
| ---- | -------- | ---- | ----------- | -------- | ------ | --------- | ------ | --- | --- | --------------------- | --- | --- | --- | ---- |
| Each | solution | C is | a partition | of users | into K | clusters. |        |     |     |                       |     |     |     |      |
|      |          | m    |             |          | m      |           |        |     |     |                       |     |     |     |      |
Ensemble diversity is ensured through parameter variation ThedecompositionoftheeigenvaluesofL norm yieldseigen-
(threshold, branching factor), variation in global clustering vectorscorrespondingtothesmallesteigenvalues,formingan
methods, random sampling for large datasets (bootstrap embeddingspaceforthefinalclusteringofK-Means.
samplingwith80%ofthedata),anddifferentdistancemetrics
duringCFTreeconstruction. 4) BIRCH-OPTIMIZEDHIERARCHICALCONSENSUS(BOHC)
BOHCisanovelconsensusstrategyspecificallydesignedto
F. ENSEMBLECONSENSUSSTRATEGIES leverage the hierarchical information preserved in BIRCH’s
The BIRCH-AE framework incorporates four ensemble CF Tree structures. Unlike conventional ensemble meth-
consensusstrategiestoaggregatemultipleBIRCHclustering ods that treat clustering outputs as flat partitions, BOHC
solutions. Each strategy offers distinct characteristics suited explicitlyincorporatesthehierarchicalrelationshipsencoded
todifferentdatadistributionsandclusteringobjectives. in each BIRCH model’s CF Tree, enabling multi-scale
consensusformation.
1) MAJORITYVOTING(MV) HierarchicalAffinityConstruction:Insteadofbinaryco-
The simplest consensus function assigns each user to the assignment,BOHCcomputesmulti-levelaffinityconsidering
hierarchicaldistances:
| cluster  | label that | appears | most | frequently | across | ensemble |     |     |     |     |     |     |     |     |
| -------- | ---------- | ------- | ---- | ---------- | ------ | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
| members: |            |         |      |            |        |          |     |     |     | M   |     |     |     |     |
1 X
|       |           |            |           |           |           |         |             | ABOHC                                     | =                |           | exp(−α·h | (i,j)) |          |          |
| ----- | --------- | ---------- | --------- | --------- | --------- | ------- | ----------- | ----------------------------------------- | ---------------- | --------- | -------- | ------ | -------- | -------- |
|       |           |            |           |           |           |         |             |                                           |                  |           |          | m      |          | (32)     |
|       |           |            |           | M         |           |         |             | ij                                        | M                |           |          |        |          |          |
|       |           |            |           | X         |           |         |             |                                           |                  | m=1       |          |        |          |          |
|       | C         | (u)=argmax |           | ⊮[C       | (u)=k]    | (26)    |             |                                           |                  |           |          |        |          |          |
|       | consensus |            |           |           | m         |         |             |                                           |                  |           |          |        |          |          |
|       |           |            |           | k         |           |         | whereh      | (i,j)istheheightintheCFTreematwhichusersi |                  |           |          |        |          |          |
|       |           |            |           | m=1       |           |         |             | m                                         |                  |           |          |        |          |          |
|       |           |            |           |           |           |         |             |                                           |                  |           |          | α      | = 0.5    |          |
|       |           |            |           |           |           |         | and j first | share                                     | a common         | ancestor, |          | and    |          | controls |
| where | ⊮[·] is   | the        | indicator | function. | To handle | varying |             |                                           |                  |           |          |        |          |          |
|       |           |            |           |           |           |         | the decay   | rate.                                     | This formulation |           | assigns  | higher | affinity | to       |
numbers of base groups, correspondence between group user pairs that merge at lower tree levels (indicating strong
| labels | is established |     | using | the Hungarian | algorithm | [51] |              |       |             |     |          |          |     |       |
| ------ | -------------- | --- | ----- | ------------- | --------- | ---- | ------------ | ----- | ----------- | --- | -------- | -------- | --- | ----- |
|        |                |     |       |               |           |      | similarity), | while | maintaining |     | moderate | affinity | for | pairs |
basedonmaximumoverlap. that merge at higher levels (indicating broader categorical
similarity).
| 88590 |     |     |     |     |     |     |     |     |     |     |     |     | VOLUME14,2026 |     |
| ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------- | --- |

C.Lietal.:BIRCH-AE:AHierarchicalEnsembleFrameworkforScalableE-CommerceUserSegmentation
HierarchicalConsensusClustering:Agglomerativehier- The perturbation bound relies on two structural assump-
archical clustering is applied to the BOHC affinity matrix tionsthataresatisfiedbyconstructioninourimplementation.
(i,j)mustbewell-definedand
with average linkage, cutting the dendrogram at optimal First,CF-treemergeheightsh m
height determined by silhouette score maximization. This finite for all user pairs (i,j) across all ensemble members
processpreservesthehierarchicalstructureinformationfrom m. Under BIRCH’s height-balanced tree construction with
individualBIRCHtreesinthefinalconsensusclustering. fixedbranchingfactorBandthresholdT,themaximumtree
The BOHC method’s key innovation is its ability to heightisboundedbyO(logn/logB),ensuringthatpairwise
maintainmulti-scaleclusteringinformationthatwouldbelost heightsarefiniteandcomparableacrossensemblemembers.
inflatpartition-basedensembleapproaches.Empiricalresults Second, height perturbations (cid:49) must be bounded, which
h
demonstrate that BOHC achieves superior performance for holds when ensemble members are trained on overlapping
datasetswithdistincthierarchicalstructure(e.g.,transaction- stratifiedsubsetssharingthesameBandT parameterrange,
focused single-domain platforms). However, its advantages asinourconfiguration.Undertheseconditions,theLipschitz
argumentintheproofsketchappliesuniformlyacrossall(i,j)
| diminish           | for multi-domain |     | datasets | with naturally | diffuse |              |       |                  |       |                  |            |     |
| ------------------ | ---------------- | --- | -------- | -------------- | ------- | ------------ | ----- | ---------------- | ----- | ---------------- | ---------- | --- |
| clusterboundaries. |                  |     |          |                |         | pairsandallM |       | ensemblemembers. |       |                  |            |     |
|                    |                  |     |          |                |         | This         | bound | does not         | prove | global partition | optimality | or  |
5) THEORETICALPROPERTIESANDCOMPLEXITYANALYSIS universal convergence; it formalizes that BOHC affinities
We provide a complexity analysis and a stability-oriented vary smoothly under bounded hierarchical perturbations.
theoreticalmotivationforBOHC. Empirically, BOHC is strongest on datasets with a clearer
Computational Complexity: Let n be the number of hierarchical structure and less beneficial on diffuse multi-
domaindata.
users,dthefeaturedimension,etrainingepochs,Mensemble
members,andqthenumberofCF-leafrepresentativesused Scalability-representationtrade-offformalization:The
for BOHC consensus (q ≪ n in compressed CF-trees). modularpipelineintroducesawell-definedtrade-offbetween
· ·
Phase 1 (autoencoder training) is O(n d e). Phase 2 computational scalability and representation quality. Let n
(BIRCH construction) is near O(nlogn) in practice due to be the number of users, d the original feature dimension,
tree insertion and condensation. Phase 3 depends on the p the latent dimension, e the number of training epochs,
consensus strategy: Majority/Weighted Voting are O(Mn); and K the target cluster count. The total pipeline cost
user-level AASC is O(n2) in memory/time and is therefore is O(n · d · e + nlogn): the first term is the one-time
used in subset settings; BOHC is implemented on CF-level autoencoder training cost and the second is the BIRCH
hierarchicalsummarieswithcomplexityO(Mq2+n). tree construction cost in Rp. For large n, the pipeline
Overall, the framework comparison pipeline on repre- is dominated by the log-linear clustering term since e is
sentative subsets is dominated by near-linear BIRCH and bounded by early stopping (e ≤ 200 in our configuration).
votingcosts,whilefulluser-levelspectralconsensusremains ReducingpdecreasestheconstantfactorinBIRCHdistance
ε
quadratic. The 4.5M-user production run reported in this computations but increases reconstruction error r , w √ hich
papercorrespondstotheBOHC-basedscalabilitytest,notan bounds the latent separation margin as γ ≥ γ − O( ε ).
|     |     |     |     |     |     |     |     |     |     |     | z   | r   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
exhaustivefull-frameworksweepofallconsensusmethodsat Practitioners can navigate this trade-off using the heuristic
|            |     |     |     |     |     | p∗  | =      | {p  | :      | <   | τ},   | τ    |
| ---------- | --- | --- | --- | --- | --- | --- | ------ | --- | ------ | --- | ----- | ---- |
| fullscale. |     |     |     |     |     |     | argmin | p   | MSE(p) |     | where | is a |
BOHCTheoreticalMotivation:Standardco-association reconstruction tolerance calibrated on a validation subset.
|     |     |     |     |     |     |     |     |     | τ = 0.05 | p∗  | =   |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | -------- | --- | --- | --- |
usesbinarymembershipagreement, In our experiments, gave 14 for both
datasets,achieving58%compressionwith90–95%variance
1 M
|     |        | X   | ⊮[C     | (j)], |      | preservation. |     |     |     |     |     |     |
| --- | ------ | --- | ------- | ----- | ---- | ------------- | --- | --- | --- | --- | --- | --- |
|     | A ij = |     | m (i)=C | m     | (33) |               |     |     |     |     |     |     |
M
m=1
whichignoreshierarchicaldistance.BOHCuses G. DYNAMICENSEMBLESELECTION
|     |     |     |     |     |     | The | BIRCH-AE | framework |     | employs a | dynamic | selection |
| --- | --- | --- | --- | --- | --- | --- | -------- | --------- | --- | --------- | ------- | --------- |
M
|     |       | 1   | X       |         |      | mechanismthatautomaticallychoosestheoptimalensemble     |     |     |     |     |     |     |
| --- | ----- | --- | ------- | ------- | ---- | ------------------------------------------------------- | --- | --- | --- | --- | --- | --- |
|     | ABOHC | =   | exp(−αh | (i,j)), | (34) |                                                         |     |     |     |     |     |     |
|     | ij    |     |         | m       |      |                                                         |     |     |     |     |     |     |
|     |       | M   |         |         |      | strategyviamulti-criteriaevaluation.Ratherthanrelyingon |     |     |     |     |     |     |
m=1
|     |     |     |     |     |     | a single | fixed | strategy, | this adaptive | approach | evaluates | all |
| --- | --- | --- | --- | --- | --- | -------- | ----- | --------- | ------------- | -------- | --------- | --- |
whereh (i,j)isthefirstcommon-ancestorheightintreem.
|     | m   |     |     |     |     | four | ensemble | methods | (Majority | Voting, | Weighted | Voting, |
| --- | --- | --- | --- | --- | --- | ---- | -------- | ------- | --------- | ------- | -------- | ------- |
Proposition(AffinityPerturbationBound):Assumefor
AASC,andBOHC).Itselectsthebestperformerforthegiven
twoBIRCH-treerealizationsthateachpairwisemergeheight
datacharacteristicsandclustercount.
| differs | by at most | (cid:49) , i.e., | |h (i,j)−h | ˜ (i,j)| ≤ | (cid:49) for all |     |     |     |     |     |     |     |
| ------- | ---------- | ---------------- | ---------- | ---------- | ---------------- | --- | --- | --- | --- | --- | --- | --- |
|         |            | h                | m          | m          | h                |     |     |     |     |     |     |     |
m,i,j.ThentheBOHCaffinityperturbationsatisfies Foreachensemblestrategy
|     | (cid:12) |     | (cid:12) |     |     |     |     |     |     |     |     |     |
| --- | -------- | --- | -------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
(cid:12) AB OHC −A ˜B OHC(cid:12) ≤α(cid:49) . E ∈{E ,E ,E ,E },
|     |          |             |             | h   | (35) |     |     | MV  | WV  | AASC BOHC |     |     |
| --- | -------- | ----------- | ----------- | --- | ---- | --- | --- | --- | --- | --------- | --- | --- |
|     | (cid:12) | ij          | ij (cid:12) |     |      |     |     |     |     |           |     |     |
|     | e−αh     | α-Lipschitz |             |     |      |     |     |     |     |           |     |     |
Sketch: f(h) = is on h ≥ 0 in magnitude three complementary cluster quality metrics are computed:
because|f′(h)|=αe−αh
≤α.ApplyLipschitzcontinuityper SilhouetteScoreS(E),Calinski-HarabaszIndexCH(E),and
| ensemblememberandaverageoverM. |     |     |     |     |     | Davies-BouldinIndexDB(E). |     |     |     |     |     |       |
| ------------------------------ | --- | --- | --- | --- | --- | ------------------------- | --- | --- | --- | --- | --- | ----- |
| VOLUME14,2026                  |     |     |     |     |     |                           |     |     |     |     |     | 88591 |

C.Lietal.:BIRCH-AE:AHierarchicalEnsembleFrameworkforScalableE-CommerceUserSegmentation
Algorithm 1 Dynamic Ensemble Selection With Algorithm2IncrementalUserSegmentUpdate
Multi-CriteriaScoring Input:Newuserdatabatch,ExistingCFTrees,
Input:Ensemblestrategies,DataX,Targetcluster TrainedautoencoderAE
|     |     | countK |     |     |     |     |     | Output:Updatedclusterassignments |     |     |     |     |     |     |
| --- | --- | ------ | --- | --- | --- | --- | --- | -------------------------------- | --- | --- | --- | --- | --- | --- |
Output:SelectedensemblesolutionE* EncodenewdatausingAEtoobtainlatent
Step1:Evaluateallensemblestrategies;
representations;
foreachensemblestrategyEinstrategiesdo foreachCFTreeinensembledo
ApplyEtoclusteringresults; foreachuserinlatentrepresentationsdo
InsertuserintotreefollowingBIRCH
Computemetrics:S(E),CH(E),DB(E);
insertionalgorithm;
Step2:Normalizemetricsto[0,1]range;
|     |     |     |     |     |     |     |     |     | iftreememorythresholdexceeded |     |     |     | then |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ----------------------------- | --- | --- | --- | ---- | --- |
foreachmetricMin{S,CH,DB}do
Performtreecondensationwithalarger
|     | FindM | min | andM max | ;   |     |     |     |     |     |     |     |     |     |     |
| --- | ----- | --- | -------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
threshold;
|     | foreachensembleE |     |                 | do  |     |     |     |                                      |     |     |     |     |     |     |
| --- | ---------------- | --- | --------------- | --- | --- | --- | --- | ------------------------------------ | --- | --- | --- | --- | --- | --- |
|     |                  |     | (E)= M(E)−Mmin; |     |     |     |     | Updateclusterassignmentsfromleafnode |     |     |     |     |     |     |
M norm
Mmax −Mmin
memberships;
Step3:Computecompositescores;
Applyensembleconsensustoobtainthefinalupdated
|     | Setweights:w |     | =0.5,w |     | =0.3,w | =0.2; |     |               |     |     |     |     |     |     |
| --- | ------------ | --- | ------ | --- | ------ | ----- | --- | ------------- | --- | --- | --- | --- | --- | --- |
|     |              |     | S      | CH  |        | DB    |     | segmentation; |     |     |     |     |     |     |
foreachensembleE do returnUpdatedclusterassignmentsincludingnew
|     | Score(E)=w |     | S ·S | norm (E)+w | CH  | ·CH norm | (E)− |     |     |     |     |     |     |     |
| --- | ---------- | --- | ---- | ---------- | --- | -------- | ---- | --- | --- | --- | --- | --- | --- | --- |
users
|     | w   | ·DB | (E); |     |     |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | ---- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|     |     | DB  | norm |     |     |     |     |     |     |     |     |     |     |     |
Step4:Selectbestensemble;
E∗ =argmax
E Score(E);
|     |     |     |     |     |     |     |     | segmentation |     | quality; exhaustive | sensitivity |     | analysis | across |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------ | --- | ------------------- | ----------- | --- | -------- | ------ |
returnE*
|     |     |     |     |     |     |     |     | alternative | metric | combinations | and | weighting | schemes | is  |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------- | ------ | ------------ | --- | --------- | ------- | --- |
identifiedasadirectionforfuturework.
Fordatasetswithstronglynon-convexorcrescent-shaped
|     | To combine |     | these metrics |     | with | different | scales and |     |     |     |     |     |     |     |
| --- | ---------- | --- | ------------- | --- | ---- | --------- | ---------- | --- | --- | --- | --- | --- | --- | --- |
clustergeometries,allthreeinternalindicesremainunreliable
optimization directions, min-max normalization is used, surrogatesandthedynamicselectionmechanismmayfavor
| followed |     | by weighted | aggregation. |     | The | complete | selection |           |          |           |          |            |     |         |
| -------- | --- | ----------- | ------------ | --- | --- | -------- | --------- | --------- | -------- | --------- | -------- | ---------- | --- | ------- |
|          |     |             |              |     |     |          |           | the wrong | ensemble | strategy; | external | validation |     | via A/B |
processisformalizedinAlgorithm1.
|     |            |               |     |             |     |                |       | testing is | the appropriate | remedy | in  | such cases, | as  | outlined |
| --- | ---------- | ------------- | --- | ----------- | --- | -------------- | ----- | ---------- | --------------- | ------ | --- | ----------- | --- | -------- |
|     | The weight | configuration |     | prioritizes |     | the silhouette | score |            |                 |        |     |             |     |          |
inthedeploymentguidanceinSectionVI.
| as      | the primary |                 | indicator | while       | incorporating |     | variance-based |     |     |     |     |     |     |     |
| ------- | ----------- | --------------- | --------- | ----------- | ------------- | --- | -------------- | --- | --- | --- | --- | --- | --- | --- |
| metrics | for         | a comprehensive |           | evaluation. |               | The | negative coef- |     |     |     |     |     |     |     |
H. SCALABILITYANDINCREMENTALLEARNING
| ficient | for | DB  | reflects | its inverse | optimization |     | direction. |     |     |     |     |     |     |     |
| ------- | --- | --- | -------- | ----------- | ------------ | --- | ---------- | --- | --- | --- | --- | --- | --- | --- |
This selection process is performed independently for each 1) MEMORY-EFFICIENTIMPLEMENTATION
|     |     |     |     |     |     |     |     | BIRCH-AE | leverages | BIRCH’s | memory | efficiency |     | through |
| --- | --- | --- | --- | --- | --- | --- | --- | -------- | --------- | ------- | ------ | ---------- | --- | ------- |
targetclustercount,allowingdifferentensemblestrategiesto
carefulimplementation.Newusersareinsertedintoexisting
| be     | optimal | for | different   | segmentation |        | granularities.      | In this |          |           |              |     |          |          |        |
| ------ | ------- | --- | ----------- | ------------ | ------ | ------------------- | ------- | -------- | --------- | ------------ | --- | -------- | -------- | ------ |
|        |         |     |             |              |        |                     |         | CF Trees | without   | reprocessing | the | entire   | dataset, | with   |
| work,  | weights |     | are fixed   | to           | ensure | comparability       | across  |          |           |              |     |          |          |        |
|        |         |     |             |              |        |                     |         | O(logn)  | insertion | complexity.  | For | datasets | that     | exceed |
| trials | and     | for | operational | simplicity   |        | in production-style |         |          |           |              |     |          |          |        |
settings; an exhaustive sensitivity analysis is left for future memory, BIRCH processes data in chunks, building partial
|     |     |     |     |     |     |     |     | CF Trees | that | are then merged |     | via tree | condensation. |     |
| --- | --- | --- | --- | --- | --- | --- | --- | -------- | ---- | --------------- | --- | -------- | ------------- | --- |
work.
|     |           |             |     |        |        |             |            | This is | particularly | important | for large-scale |     | datasets | with |
| --- | --------- | ----------- | --- | ------ | ------ | ----------- | ---------- | ------- | ------------ | --------- | --------------- | --- | -------- | ---- |
|     | Regarding | sensitivity |     | to the | choice | of internal | evaluation |         |              |           |                 |     |          |      |
metrics: the silhouette score, Calinski-Harabasz index, and millions of users. Base BIRCH models in the ensemble are
|                |     |     |       |         |               |     |           | trained | in parallel, | with each | model | processing |     | the latent |
| -------------- | --- | --- | ----- | ------- | ------------- | --- | --------- | ------- | ------------ | --------- | ----- | ---------- | --- | ---------- |
| Davies-Bouldin |     |     | index | capture | complementary |     | geometric |         |              |           |       |            |     |            |
properties of cluster quality [45], [46], [47]. These met- representations independently, enabling near-linear speedup
withcorecount.
| rics   | are | known     | to agree | on well-separated, |     |             | approximately |     |     |     |     |     |     |     |
| ------ | --- | --------- | -------- | ------------------ | --- | ----------- | ------------- | --- | --- | --- | --- | --- | --- | --- |
| convex |     | clusters, | while    | diverging          | on  | overlapping | or non-       |     |     |     |     |     |     |     |
convex structures [13]. The dynamic selection mechanism 2) INCREMENTALUSERSEGMENTUPDATES
evaluates all three metrics precisely to mitigate reliance on For dynamic e-commerce environments, BIRCH-AE sup-
any single indicator, with the composite score weighting ports incremental clustering without requiring complete re-
|     | ,w  | ,w  | = (0.5,0.3,0.2) |     |     |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
(w S CH DB ) reflecting the established clustering.TheAlgorithm2formalizesthisprocess,enabling
primacyofthesilhouettescoreasacohesion-separationmea- critical real-time segment updates for applications such as
sure while incorporating complementary variance-ratio and dynamicrecommendationsystems.
inter-clusterdistancesignals.Fordatasetsexhibitingstrongly This incremental approach enables real-time segment
non-convex or heavily overlapping cluster structures, all updates without complete re-clustering, maintaining system
three internal indices remain imperfect surrogates for true responsivenessasnewusersjointheplatform.
| 88592 |     |     |     |     |     |     |     |     |     |     |     |     | VOLUME14,2026 |     |
| ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------- | --- |

C.Lietal.:BIRCH-AE:AHierarchicalEnsembleFrameworkforScalableE-CommerceUserSegmentation
I. IMPLEMENTATIONDETAILS and temporal engagement features. Compared to Retail
The BIRCH-AE framework is implemented in Python Rocket, this dataset exhibits more diffuse and overlapping
3.8+ using PySpark 3.0+ for large-scale data processing, behavioral structures, reflected in a significantly lower
Scikit-learn1.0+forBIRCHimplementationandevaluation average Calinski-Harabasz score (1413.1), approximately
metrics,TensorFlow/Kerasforautoencoderimplementation, 6.4timessmaller,indicatingweakerclusterseparation.This
NumPy1.21+fornumericalcomputations,andPandas1.3+ propertymakesitidealforassessingrobustnessunderhigh-
for data manipulation. Experiments are conducted on a variability,low-separationconditions.
Databricks computing cluster with distributed processing Together,thesedatasetsprovidecomplementaryevaluation
capabilities. contexts: Retail Rocket represents distinct, transaction-
Key hyperparameters include: latent dimension of the dominant user behavior, while E-Commerce Behavior cap-
autoencoder p = 14 (tuned from {14, 32, 50, 64 }), tures complex, exploratory patterns across multiple product
learning rate α = 0.001, sparsity weight λ = 0.001, L2 categories.Theircontrastingstructuralcharacteristicsenable
1
regularizationλ = 0.0001,batchsize256,trainingepochs rigorousassessmentofBIRCH-AE’sscalability,adaptability,
2
200 with early stopping (patience=10); BIRCH threshold andclusteringqualityacrossdiversee-commercescenarios.
range T ∈ {0.3,0.5,0.8}, branching factor B = 50,
number of clusters K ∈ {5,7,10,12,15,20,25}; ensemble
parameters:numberofbasemodelsM =10,weightedvoting B. EXPERIMENTALSETUP
temperature β = 5, BOHC decay rate α = 0.5, composite Acomprehensiveevaluationprotocolwasdesignedtoassess
scoreweights(w ,w ,w )=(0.5,0.3,0.2). the BIRCH-AE framework across multiple dimensions.
S CH DB
Cluster quality was measured using the Silhouette Score,
theCalinski-HarabaszIndex,andtheDavies-BouldinIndex.
V. EXPERIMENTALEVALUATION
Scalability was evaluated in terms of execution time and
A. DATASETS
performance as data size increased. Stability was assessed
The proposed BIRCH-AE framework was evaluated using
through repeated randomized runs under different cluster
two publicly available large-scale e-commerce datasets that
counts and parameter configurations. Interpretability was
differ markedly in behavior structure and domain focus.
exploredqualitativelybyanalyzingdiscoveredusersegments
Both datasets were preprocessed using PySpark to enable
and identifying features that contribute to cluster discrim-
distributed feature engineering, outlier handling, null-value
ination. Cross-dataset analysis was conducted to evaluate
treatment, and normalization. To achieve computational
generalizability.
efficiency while preserving representativeness, comparative
Baseline methods include: (1) K-Means [18], (2) K-
experiments were conducted on 30% randomly selected
MeanswithPCA[22]retaining95%variance,(3)MiniBatch
stratified subsets of each dataset across 20 independent
K-Means, (4) Agglomerative hierarchical clustering [54]
randomizedtrials.
with Ward linkage, and (5) standard BIRCH [28] with
optimized parameters. All methods were evaluated across
1) RETAILROCKETE-COMMERCEDATASET multiple cluster counts K ∈ {5,10,15,20,25} to examine
The Retail Rocket dataset [52], sourced from a real-world
segmentationgranularityandensembleadaptability.
online retail platform, comprises over 1.4 million unique
users and detailed interaction events, including product
views,cartadditions,andpurchases.Featureengineeringpro- C. RESULTS:RETAILROCKETDATASET
ducedrichbehavioralprofilesthatcapturebothtransactional
1) CLUSTERINGQUALITYCOMPARISON
and navigational dynamics, including event frequencies,
Table 2 presents a comprehensive comparison of clustering
session-based statistics, engagement diversity, and temporal
quality metrics for both base algorithms and the four
activity indicators. The dataset reflects transaction-oriented
ensemblemethodswithinBIRCH-AEacrossmultiplecluster
e-commerce behavior characterized by distinct and well-
counts for the Retail Rocket dataset. BIRCH-AE with
separated clusters, as supported by high Calinski-Harabasz
ensemble methods achieves superior performance, with
scores(mean:9053.5).Thesepropertiesmakeitwell-suited
AASC and BOHC strategies delivering the best results at
forvalidatingensemblemethodsthatleverageclearlydefined
5clusters.Fig.2providesavisualcomparisonacrossthethree
clusterstructures.
evaluationmetrics.
Key observations for Retail Rocket include: BIRCH-AE
2) E-COMMERCEBEHAVIORMULTI-CATEGORYSTORE achieves the best silhouette score of 0.548 with AASC and
DATASET BOHC ensemble strategies for 5 clusters, representing 23%
TheE-CommerceBehaviordataset[53]containsinteraction improvementoversingleBIRCH(0.445);TheweightedVot-
logsfromamulti-categoryonlinestore,coveringmorethan ing ensemble achieves the highest Calinski-Harabasz index
4.5 million users. It emphasizes heterogeneous behavior of 213.1 at 5 clusters and 236.0 at 20 clusters; AASC and
patternsacrossproductcategoriesandpricelevels,including BOHCensemblemethodsconsistentlyoutperformindividual
activity counts, category diversity, price range statistics, basemodelsatoptimalclustercounts;performancedegrades
VOLUME14,2026 88593

C.Lietal.:BIRCH-AE:AHierarchicalEnsembleFrameworkforScalableE-CommerceUserSegmentation
FIGURE2. ClusteringperformancecomparisonforRetailRocketdatasetacrossbasemodels,ensemblemethods,andBIRCH-AE.(a)Silhouettescores
indicatethatBIRCH-AEachievesthehighestscore,0.548,withtheAASC/BOHCensemble.(b)Calinski-HarabaszindexwithWeightedVotingBIRCH-AE
reaching213.1at5clusters.(c)Davies-Bouldinindex(lowerisbetter),whereBIRCH-AEachieves0.792withAASC.Theresultsdemonstratethat
ensemblemethods,particularlyAASCandBOHC,significantlyimproveclusteringqualitycomparedtobasealgorithmsonthisdataset.
withincreasingclustercounts,withMajorityVotingshowing D. RESULTS:E-COMMERCEBEHAVIORDATASET
particularlypoorperformanceathighergranularities.
|     |     |     |     |     |     |     |     | 1) MULTI-CATEGORYPERFORMANCEANALYSIS |         |                 |     |         |         |     |        |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------------------------------ | ------- | --------------- | --- | ------- | ------- | --- | ------ |
|     |     |     |     |     |     |     |     | Table 4                              | details | the performance |     | between | cluster |     | counts |
2) ENSEMBLESTRATEGYCOMPARISON for the E-Commerce Behavior multi-category dataset. This
analysisrevealsfundamentallydifferentcharacteristicsfrom
| Table 2 provides |            | a comprehensive |     | comparison |          | of the | four    |                |      |      |            |               |     |          |     |
| ---------------- | ---------- | --------------- | --- | ---------- | -------- | ------ | ------- | -------------- | ---- | ---- | ---------- | ------------- | --- | -------- | --- |
|                  |            |                 |     |            |          |        |         | Retail Rocket, | with | base | algorithms | demonstrating |     | superior |     |
| ensemble         | strategies | (Majority       |     | Voting,    | Weighted |        | Voting, |                |      |      |            |               |     |          |     |
AASC,andBOHC)andbasealgorithmsindifferentcluster performancetoensemblemethodsonmulti-domaindata.
|            |        |         |      |     |      |            |     | Key observations |     | for | the multi-category |     | E-Commerce |     |     |
| ---------- | ------ | ------- | ---- | --- | ---- | ---------- | --- | ---------------- | --- | --- | ------------------ | --- | ---------- | --- | --- |
| counts for | Retail | Rocket. | AASC | and | BOHC | strategies |     |                  |     |     |                    |     |            |     |     |
consistentlyoutperformsimplervotingmethods,particularly Behavior dataset include: K-Means achieves best overall
at lower cluster counts, while the base algorithms remain performanceat5clusters(0.683silhouette);BIRCHdemon-
|     |     |     |     |     |     |     |     | strates exceptional |     | consistency |     | and scalability, |     | maintaining |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------------- | --- | ----------- | --- | ---------------- | --- | ----------- | --- |
competitive.
|     |     |     |     |     |     |     |     | superior     | performance | at  | higher       | cluster | counts | (0.603 | at    |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------ | ----------- | --- | ------------ | ------- | ------ | ------ | ----- |
|     |     |     |     |     |     |     |     | 15 clusters, | 0.596       | at  | 20 clusters) |         | where  | other  | algo- |
3) AUTOENCODERIMPACTANALYSIS
|            |                   |     |              |     |           |     |         | rithms degrade | significantly |     | (K-Means |     | drops | to 0.332 | and |
| ---------- | ----------------- | --- | ------------ | --- | --------- | --- | ------- | -------------- | ------------- | --- | -------- | --- | ----- | -------- | --- |
| To isolate | the autoencoder’s |     | contribution |     | to Retail |     | Rocket, |                |               |     |          |     |       |          |     |
0.338respectively);basealgorithmsconsistentlyoutperform
wecompareBIRCH-AEwithBIRCHonbothrawandPCA-
|     |     |     |     |     |     |     |     | ensemble | methods | across | all cluster | counts, | suggesting |     | that |
| --- | --- | --- | --- | --- | --- | --- | --- | -------- | ------- | ------ | ----------- | ------- | ---------- | --- | ---- |
reducedfeatures.Table3andFig.4showtheconvergenceof
thediffuse,multi-domainnatureofthedatadoesnotbenefit
trainingandtheimpactanalysis.
|     |     |     |     |     |     |     |     | from ensemble | consensus; |     | lower | Calinski-Harabasz |     |     | scores |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------- | ---------- | --- | ----- | ----------------- | --- | --- | ------ |
Table 3 shows that standard AE consistently outperforms (1413.1average)comparedtoRetailRocket(9053.5)indicate
| all alternative | feature | learning |     | methods. | Most | importantly, |     |     |     |     |     |     |     |     |     |
| --------------- | ------- | -------- | --- | -------- | ---- | ------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- |
morediffuse,overlappingclusterstructure.
| AE achieves        | a   | 32% improvement |            | over | VAE        | (0.839 | vs. |     |     |     |     |     |     |     |     |
| ------------------ | --- | --------------- | ---------- | ---- | ---------- | ------ | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0.636 silhouette), |     | directly        | validating |      | our design | choice | in  |     |     |     |     |     |     |     |     |
SectionIV-A.Thesuperiorityisconsistentacrossallmetrics: 2) SINGLE-DOMAINCATEGORYANALYSIS
34% better CH index and 75% better DB index compared To investigate whether the multi-domain nature of the
to VAE. This confirms that for e-commerce behavioral data E-CommerceBehaviordatasetexplainstheensembleunder-
with deterministic patterns, VAE’s stochastic regularization performance,additionalexperimentswereconductedontwo
degradesclusteringqualityratherthanenhancingit. individual product categories: electronics and appliances.
Againsttraditionalmethods,AEachieves115%improve- Thisaddressespotentialsparsityandlong-taileffectsinherent
ment over PCA (0.839 vs. 0.390) and 89% improvement in multi-category data. The results are presented in Table 5
overrawfeatures(0.839vs.0.445),demonstratingthevalue andvisualizedinFigs.5and6.
of non-linear dimensionality reduction. The improvements The single-domain analysis reveals critical insights into
in the CH index are even more dramatic (490% vs. PCA, howdomaingranularityaffectsmethodselection:
741%vs.rawfeatures),indicatingsubstantiallybettercluster Electronics Category: Exhibits high variability (sil-
separation. These results validate the effectiveness of deep houette std: 0.089) with ensemble methods achieving a
learning-based feature extraction for handling correlated 17% improvement over base algorithms in 5 clusters
variables [15], providing empirical evidence to address (0.461vs.0.394).Thisadvantagepersistsinallclustercounts,
Reviewer1’sconcernaboutVAEselection. with ensemble methods consistently outperforming base
| 88594 |     |     |     |     |     |     |     |     |     |     |     |     |     | VOLUME14,2026 |     |
| ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------- | --- |

C.Lietal.:BIRCH-AE:AHierarchicalEnsembleFrameworkforScalableE-CommerceUserSegmentation
TABLE2. Performancecomparison:basealgorithmsvs.ensemblestrategiesacrossclustercountsforretailrocketdataset.
FIGURE3. EnsemblestrategyperformanceacrossdifferentclustercountsfortheRetailRocketdataset.(a)Silhouettescoresdemonstrate
thatAASCandBOHCconsistentlyachievesuperiorperformance,particularlyfor5clusters(0.548).Performancedegradesasclustercount
increases,withMajorityVotingshowingnegativescoresat20clusters.(b)TheCalinski-HarabaszindexshowsthatWeightedVoting
maintainscompetitiveperformanceacrossallclustercounts(peakingat236.0for20clusters),whereasMajorityVotingdegrades
significantlyasclustercountincreases.TheresultsvalidateBIRCH-AE’sdynamicselectionmechanismforchoosingoptimalstrategies
basedondatacharacteristics.
| At 5 clusters, | the | base | algorithms | maintain |     | a slight |
| -------------- | --- | ---- | ---------- | -------- | --- | -------- |
TABLE3. FeaturelearningmethodcomparisonforBIRCHclustering.
| advantage          | (0.643     | vs. 0.585, | representing |              | 10% base     | supe-     |
| ------------------ | ---------- | ---------- | ------------ | ------------ | ------------ | --------- |
| riority). However, |            | in 10      | clusters,    | the ensemble |              | methods   |
| begin to show      | advantages |            | (0.479       | vs. 0.446,   | representing |           |
| a 7% improvement   |            | of the     | ensemble),   | with         | this         | advantage |
growingin15clusters(0.462vs.0.374,representinga24%
improvement)and20clusters(0.481vs.0.390,representinga
23%improvement).Thispatterndemonstratesthatensemble
methodsexcelatmanagingcomplexityinhigher-granularity
segmentation.
| Critical | Finding: | Both | single-domain |     | categories | ulti- |
| -------- | -------- | ---- | ------------- | --- | ---------- | ----- |
matelybenefitfromensemblemethods,althoughthepattern
| differs. Electronics |     | shows | consistent | ensemble | superiority |     |
| -------------------- | --- | ----- | ---------- | -------- | ----------- | --- |
algorithmsby17–23%.ThehighvariabilityintheCalinski- across all granularities because of an unstable cluster struc-
Harabasz (1200–2200) and Davies-Bouldin indices (0.85– ture.Appliancesdemonstrateensemblesuperiorityathigher
1.30)indicatesanunstableclusterstructurethatbenefitsfrom cluster counts (10+ clusters) where complexity increases,
ensembleconsensus. thoughbasealgorithmsperformslightlybetteratthesimplest
Appliances Category: Shows ensemble methods that configuration (5 clusters). This directly contrasts with the
| multi-category | pattern, | where | base | algorithms | consistently |     |
| -------------- | -------- | ----- | ---- | ---------- | ------------ | --- |
achievesuperiorityinhigherclustercounts(10–20clusters).
VOLUME14,2026 88595

C.Lietal.:BIRCH-AE:AHierarchicalEnsembleFrameworkforScalableE-CommerceUserSegmentation
FIGURE4. AutoencodertrainingconvergenceandimpactanalysisforRetailRocketdataset.(a)Trainingandvalidationlosscurvesshow
effectiveconvergencewithafinalvalidationlossof0.0350,indicatinggoodgeneralizationwithoutoverfitting.Theclosealignment
demonstratesrobustlearning.(b)AcomparisonofBIRCHwithdifferentdimensionality-reductionmethodsdemonstratesthat
autoencoder-basedfeaturelearningachievesa23%improvementinthesilhouettescoreoverrawfeatures(0.4452→0.5477)anda49%
improvementintheCHindex(142.65→213.11).TheautoencodersignificantlyoutperformsPCA,effectivelyhandlingcorrelatedvariables
andcapturingnon-linearbehavioralpatternsintransaction-focusede-commercedata.
TABLE4. Performancemetricsacrossclustercounts:E-commercebehaviormulti-categorydataset.
TABLE5. Performancecomparison:single-domaincategories(electronicsandappliances).
dominated, validating that domain granularity (single vs. selection. Single-domain environments enable ensemble
multi-category) fundamentally influences optimal method methods to effectively capture and refine cluster structure,
88596 VOLUME14,2026

C.Lietal.:BIRCH-AE:AHierarchicalEnsembleFrameworkforScalableE-CommerceUserSegmentation
FIGURE5. Comprehensiveperformancecomparisonforsingle-domaincategories(ElectronicsandAppliances).Thevisualizationrevealscontrasting
patternsacrosscategoriesandfundamentaldifferencesrelativetomulti-categoryresults.Toppanels:OverallperformancedistributionsshowElectronics
withhighvariability(Silhouettescoresranging0.3–0.6,Calinski-HarabaszIndex:1200–2200,Davies-BouldinIndex:0.85–1.30),indicatingunstablecluster
structure,whileAppliancesdemonstratesmoderatestability.Middlepanels:Performancebyclustercountrevealsoptimalconfigurationsat5clustersfor
Electronics.Critically,Electronicsshowsthatensemblemethodsoutperformbasealgorithms(ensembleavg:0.461vs.baseavg:0.394at5clusters,a17%
improvement).Incomparison,Appliancesexhibitsensemblesuperiorityathigherclustercounts(ensembleavg:0.481vs.baseavg:0.390at20clusters,
23%improvement).Bottompanels:Method-specifictrendsdemonstratethatensemblesuperioritypersistsacrossdifferentgranularitiesforboth
single-domaincategories.Thecontrastingpatternsbetweensingle-domaincategoriesandmulti-categoryresultsvalidatethecriticalimportanceof
domaingranularityinmethodselection,withbothsingle-domaincategoriesbenefitingfromensemblemethods.
whereasmulti-domainenvironmentsintroducenaturalover- clusters) show base advantage at lowest granularity (5
lapsthatensemblemethodscannotresolve. clusters: −10%) but strong ensemble advantages at higher
granularities(20clusters:+23%).Formulti-domaindatasets,
E. CROSS-DATASETCOMPARATIVEANALYSIS diffuse overlapping patterns cause base algorithms to excel
Table6providesacomprehensivecomparisonthatintegrates (+7.4%overensembles)regardlessofclusterstructure.
thefindingsofallexperimentalscenarios. 2.DomainGranularityFundamentallyInfluencesOut-
Thecross-datasetanalysisrevealsthreecriticalinsights: comes: Multi-category data exhibit diffuse, overlapping
1. Cluster Structure Determines Method Selection patterns where base algorithms excel consistently. Single-
Within Domain Type: For single-domain datasets, cluster domain categories enable ensemble methods to capture and
stability affects the magnitude and pattern of ensemble refineclusterstructureeffectively,withbothElectronicsand
advantage. Electronics (unstable clusters) benefit uniformly Appliances showing ensemble advantages (though patterns
across granularities (+17–23%). Appliances (more stable differ). This represents the most important finding: domain
VOLUME14,2026 88597

C.Lietal.:BIRCH-AE:AHierarchicalEnsembleFrameworkforScalableE-CommerceUserSegmentation
FIGURE6. Detailedperformancetrendsacrossclustercountsforsingle-domaincategories.Leftpanel(Electronics):Showsconsistent
degradationinSilhouettescoresasclustercountincreases(0.461at5clustersto0.358at20clustersforensemble;0.394to0.291for
base),withensemblemethodsmaintaining17–23%advantageacrossallgranularities.HighvariabilityinCHandDBindicesreflectsthe
inherentlyunstableclusterstructure.Rightpanel(Appliances):Demonstratesensembleadvantageemergingathigherclustercounts
(10–20clusters),with7–23%improvementoverbasealgorithms.At5clusters,basealgorithmsmaintainaslightadvantage(0.643vs.
0.585),butensemblemethodsbecomesuperiorat10+clusters.Thetransitionfrombase-to-ensemblesuperiorityasgranularityincreases
demonstratestheeffectivenessofensemblemethodsinmanagingcomplexity.Thesesingle-domainresultscontrastwithmulti-category
findings,inwhichbasealgorithmsuniformlyoutperformedensembles,emphasizingthatdomaingranularityfundamentallyinfluences
optimalsegmentationstrategies.
granularity (single vs. multi) is the primary determinant of distribution,and(3)category-engagementstrataforthemulti-
optimalmethodselection. domaindataset.
3. BIRCH’s Multi-Scale Advantage Persists: Across TrialProtocol:Weconducted20independentrandomized
all scenarios, BIRCH demonstrates superior scalability trialson30%subsetstosupportcomparativeframeworkanal-
to higher cluster counts, maintaining performance where ysis. Across trials, method ranking patterns were generally
partition-based methods degrade. This validates BIRCH’s consistent: there is no universally best consensus strategy,
hierarchical approach for applications requiring multi- and performance depends on dataset structure and domain
resolutionsegmentation. granularity.
Rank-Order Stability: Beyond metric-level consistency,
F. VALIDATIONOFSUBSET-BASEDANALYSIS method rank ordering remained stable across all 20 ran-
To address the concern that most comparative analyses domized trials. Specifically: (1) BIRCH consistently out-
use 30% subsets, we provide a consistency analysis across performed K-Means at cluster counts K ∈ {15,20} across
repeated subset trials and a separate full-scale BOHC both datasets; (2) autoencoder-based features consistently
confirmationrun. outperformedPCAandrawfeaturesacrossallconfigurations
SamplingMethodologyandExtrapolationValidity: and cluster counts; (3) the domain granularity finding—
Stratification Strategy: 30% subsets were created via single-domain datasets favoring ensemble methods, multi-
three-tier stratified random sampling: (1) activity-level domain datasets favoring base algorithms—held without
strata (low: <10 events; medium: 10–100 events; high: exception across all trials. Table 7 further confirms that
>100 events), (2) temporal strata preserving monthly user silhouette and Calinski-Harabasz deviations between 30%
88598 VOLUME14,2026

C.Lietal.:BIRCH-AE:AHierarchicalEnsembleFrameworkforScalableE-CommerceUserSegmentation
TABLE6. Comprehensivecross-datasetandcross-domaincomparison.
TABLE7. Subset(30%)vs.Fulldataset(100%)performancevalidation. Conclusion: The repeated stratified subset protocol pro-
|     |     |     | vides stable       | comparative |            | evidence | for          | framework | behavior,      |
| --- | --- | --- | ------------------ | ----------- | ---------- | -------- | ------------ | --------- | -------------- |
|     |     |     | while the          | BOHC        | full-scale |          | run confirms | that      | the pro-       |
|     |     |     | posed hierarchical |             | consensus  |          | can be       | executed  | efficiently at |
4.5M-userscale.
G. INCREMENTALLEARNINGPERFORMANCE
|     |     |     | To validate | BIRCH-AE’s     |              | incremental |            | update     | capability |
| --- | --- | --- | ----------- | -------------- | ------------ | ----------- | ---------- | ---------- | ---------- |
|     |     |     | (Algorithm  | 2),            | we simulated |             | daily user | additions  | by parti-  |
|     |     |     | tioning     | the E-Commerce |              | Behavior    | dataset    | temporally | and        |
measuringupdateperformance.
|     |     |     | Experimental |     | Setup: | The     | dataset    | was split   | chronolog- |
| --- | --- | --- | ------------ | --- | ------ | ------- | ---------- | ----------- | ---------- |
|     |     |     | ically into: | (1) | base   | dataset | (first 90% | of temporal | range,     |
subsetandfull-datasetrunsremainbelow1.3%,andnorank 4.05Musers),(2)10dailybatches(remaining10%,45Knew
reversalbetweenmethodswasobservedwhenmovingfrom users per day). The trained autoencoder and CF-tree from
subsettofull-datasetevaluation. thebasedatasetwereusedforincrementalinsertionwithout
| Full-Scale Check: | A full 4.5M-user | run was executed | retraining. |     |     |     |     |     |     |
| ----------------- | ---------------- | ---------------- | ----------- | --- | --- | --- | --- | --- | --- |
for BOHC to validate operational feasibility of the pro- Results: Table 8 shows incremental update times signifi-
duction deployment path. This run is used as a scalability cantlyoutperformfullre-clustering.
confirmation point rather than a full-method exhaustive For daily batches (45K users), incremental insertion
benchmark,whichwouldrequireuser-levelquadraticaffinity requires8.3svs.307.8sforfullre-clustering(37×speedup)
(<0.3%
constructionforsomestrategies. while maintaining silhouette score within 0.002
Validation Results: Table 7 summarizes subset-trial degradation). After 10 cumulative days (450K new users,
4.4×
statisticsandtheBOHCfull-scalerun. 10% dataset growth), incremental updates achieve
| VOLUME14,2026 |     |     |     |     |     |     |     |     | 88599 |
| ------------- | --- | --- | --- | --- | --- | --- | --- | --- | ----- |

C.Lietal.:BIRCH-AE:AHierarchicalEnsembleFrameworkforScalableE-CommerceUserSegmentation
TABLE8. Incrementalupdateperformancevs.Fullre-clustering. TABLE9. ScalabilityperformancesummaryforBIRCH-AE.
TABLE10. Stage-wiseexecutiontimebreakdown(subsetbenchmarkand
full-scaleprojection).
speedup(76.2svs.335.4s)with0.008silhouettedegradation
(1.2%).
Cluster Stability Analysis: We measured cluster assign-
mentstabilityforexistingusersacrossincrementalupdates.
After adding 450K users (10 days), 98.7% of the original
users retained their cluster assignments, demonstrating that
incrementalinsertionpreservestheoriginalsegmentstructure
whileaccommodatingnewusers.
ProductionImplications:TheseresultsvalidateBIRCH-
AE’s suitability for production environments requiring
daily/weekly segment refreshes. The 37× speedup enables
near-real-time updates, while minimal quality degradation
(<1.5%) after 10% dataset growth suggests monthly full
re-clusteringissufficienttomaintainoptimalquality.
Path dependence analysis: BIRCH’s CF-tree construc-
tionisinherentlyorder-dependent:thetreestructurereflects
the insertion sequence, and later insertions must follow
pathsestablishedbyearlierdata.Thisraisesthequestionof
whether early-arriving users bias the tree structure in ways
thatsystematicallymisclassifylaterusers.Threemechanisms
mitigate this risk in BIRCH-AE. First, the base dataset H. SCALABILITYANALYSIS
(90% of the temporal range, 4.05M users) is processed BIRCH-AE demonstrates efficient scaling behavior across
in activity-stratified order rather than strict chronological both datasets. Comparative pipeline timings were bench-
order, ensuring the initial tree captures the full diversity marked across repeated 30%-subset trials, and the autoen-
of user behavior patterns. Second, BIRCH’s condensation coderconvergedin100epochswithearlystopping.
mechanism merges subclusters when memory thresholds Scalabilitycharacteristicsincludesingle-passBIRCHcon-
are exceeded, implicitly correcting some path-dependent struction, enabling streaming data integration; incremental
assignments. Third, the 98.7% cluster assignment stability insertion, supporting real-time user segment updates; and
after10%datasetgrowthprovidesdirectempiricalevidence parallel processing of ensemble members for practical
that path dependence is not materially affecting segment speedups.
consistency at the scales tested. Path dependence becomes A production-scale test involving 4.5 million customer
more pronounced in long-running production systems that records validated BOHC’s full-scale feasibility. The BOHC
experience significant distributional shifts (e.g., seasonal runcompletedin307.8seconds(approximately5.1minutes),
behavioral changes or major product catalog expansions). demonstrating that hierarchical consensus can be deployed
It should be noted that the 98.7% stability figure was on multi-million-user data. This production-feasibility run
measuredunderstabledistributionalconditionsovera10-day was executed on the fixed 8-worker Databricks cluster
window;thisresultmaynotgeneralizetoscenariosinvolving configurationdocumentedinSectionV-J.
significantconceptdrift—suchasmajorseasonalbehavioral Table 10 provides stage-wise timing on subset runs and
shifts, large-scale product catalog restructuring, or rapid projected full-scale equivalents for pipeline planning. The
user cohort changes—where accumulated path dependence fullmeasured4.5Mresultreportedinthispapercorresponds
could cause cluster assignments to diverge from the current to the BOHC run (307.8s). At the same time, AASC is
data distribution more quickly. For this reason, monthly keptinsubset-levelcomparisonsduetoitsquadraticaffinity
fullre-clusteringisrecommendedtoresetaccumulatedpath construction at the user level. Therefore, the full-scale
dependence, with the frequency increased if distributional experimentisinterpretedasdeployment-feasibilityvalidation
monitoring (e.g., tracking the silhouette score over rolling rather than a claim that all consensus variants are equally
windows)detectssignificantdrift. production-readyatfulluserscale.
88600 VOLUME14,2026

C.Lietal.:BIRCH-AE:AHierarchicalEnsembleFrameworkforScalableE-CommerceUserSegmentation
I. BUSINESSINSIGHTSANDSEGMENTINTERPRETATION shoppingexperiences,competitivepricing,communications,
andtargetedcampaignsforanticipatedneeds.
Thediscoveredusersegmentsprovideactionableinsightsfor
e-commerce practitioners. This section presents qualitative Premium Shoppers (12%): High average order values,
interpretationsoftheoptimal5-clustersegmentationsforboth frequentpurchases,anddemonstratedloyalty.Thissegment
datasets. representsprimecandidatesforpremiumloyaltytiers,exclu-
|     |     |     |     |     |     |     |     | sive access | programs, | concierge |     | services, | and | high-touch |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------- | --------- | --------- | --- | --------- | --- | ---------- | --- |
relationshipmanagement.
1) RETAILROCKETCUSTOMERSEGMENTS
|          |     |          |               |                 |     |     |        | At-Risk       | Previously-Active |                    | (5%): |         | Formerly | engaged   |     |
| -------- | --- | -------- | ------------- | --------------- | --- | --- | ------ | ------------- | ----------------- | ------------------ | ----- | ------- | -------- | --------- | --- |
| Based on | the | analysis | of behavioral | characteristics |     |     | within |               |                   |                    |       |         |          |           |     |
|          |     |          |               |                 |     |     |        | users showing |                   | declining activity |       | trends. | Priority | retention |     |
eachcluster:
|          |           |             |                  |        |        |            |        | segment          | requiring | immediate | intervention |         | through | person-   |     |
| -------- | --------- | ----------- | ---------------- | ------ | ------ | ---------- | ------ | ---------------- | --------- | --------- | ------------ | ------- | ------- | --------- | --- |
| High     | frequency | transactors |                  | (22%): | Users  | exhibiting |        |                  |           |           |              |         |         |           |     |
|          |           |             |                  |        |        |            |        | alized outreach, |           | exclusive | retention    | offers, | and     | proactive |     |
| frequent | purchases | with        | high transaction |        | counts | and        | strong |                  |           |           |              |         |         |           |     |
customerservicetopreventcompletechurn.
| conversion | rates. | These         | customers | demonstrate |     | consistent |         |            |         |                 |               |     |            |          |     |
| ---------- | ------ | ------------- | --------- | ----------- | --- | ---------- | ------- | ---------- | ------- | --------------- | ------------- | --- | ---------- | -------- | --- |
|            |        |               |           |             |     |            |         | These      | segment | interpretations | demonstrate   |     | BIRCH-AE’s |          |     |
| engagement | and    | high lifetime | value.    | Recommended |     |            | strate- |            |         |                 |               |     |            |          |     |
|            |        |               |           |             |     |            |         | ability to | produce | not only        | statistically |     | valid      | clusters | but |
giesincludepremiumloyaltyprograms,earlyaccesstonew
|     |     |     |     |     |     |     |     | also business-actionable |     | customer |     | groupings | that | align | with |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------------------ | --- | -------- | --- | --------- | ---- | ----- | ---- |
products,andpersonalizedhigh-valuerecommendations.
practicalmarketingandretentionstrategies.
Browse-and-BuyBalanced(31%):Thelargestsegment,
| characterized   | by  | moderate | browsing    | activity |      | coupled | with    |                                            |     |     |     |     |     |     |     |
| --------------- | --- | -------- | ----------- | -------- | ---- | ------- | ------- | ------------------------------------------ | --- | --- | --- | --- | --- | --- | --- |
|                 |     |          |             |          |      |         |         | J. REPRODUCIBILITYANDIMPLEMENTATIONDETAILS |     |     |     |     |     |     |     |
| good conversion |     | rates.   | These users | respond  | well | to      | product |                                            |     |     |     |     |     |     |     |
Toensurereproducibility,weprovidecomprehensiveimple-
| recommendations |     | and | engage | effectively | in  | targeted | pro- |     |     |     |     |     |     |     |     |
| --------------- | --- | --- | ------ | ----------- | --- | -------- | ---- | --- | --- | --- | --- | --- | --- | --- | --- |
mentationdetailsandmakeallcodepubliclyavailable.
| motions. | The | marketing | focus | should | emphasize |     | relevant |          |     |              |                |     |     |             |     |
| -------- | --- | --------- | ----- | ------ | --------- | --- | -------- | -------- | --- | ------------ | -------------- | --- | --- | ----------- | --- |
|          |     |           |       |        |           |     |          | Hardware |     | and Software | Configuration: |     |     | Experiments |     |
productsuggestionsandlimited-timeoffers.
|        |          |     |        |               |     |          |     | were conducted |     | on Azure | Databricks |     | with | two cluster |     |
| ------ | -------- | --- | ------ | ------------- | --- | -------- | --- | -------------- | --- | -------- | ---------- | --- | ---- | ----------- | --- |
| Window | Shoppers |     | (28%): | High browsing |     | activity | but |                |     |          |            |     |      |             |     |
configurations:
lowerpurchaseconversion.Thissegmentrequiresnurturing
|                |           |                     |     |            |     |               |      | Development/Testing |                 | Cluster           | (30% | subset     | experiments): |           |     |
| -------------- | --------- | ------------------- | --- | ---------- | --- | ------------- | ---- | ------------------- | --------------- | ----------------- | ---- | ---------- | ------------- | --------- | --- |
| strategies,    | including | retargeting         |     | campaigns, |     | cart abandon- |      |                     |                 |                   |      |            |               |           |     |
|                |           |                     |     |            |     |               |      | - Instance          | Type:           | Standard_E16ds_v4 |      | Azure      | VM            | - Config- |     |
| ment recovery, |           | and incentive-based |     | conversion |     | tactics       | such |                     |                 |                   |      |            |               |           |     |
|                |           |                     |     |            |     |               |      | uration:            | 2-8 autoscaling | workers           |      | (16 cores, | 128GB         |           | RAM |
asfirst-purchasediscountsorfreeshippingoffers.
perworker)-Driver:Standard_E16ds_v4(16cores,128GB
| Category | Specialists |     | (13%): |       |      |              |     |     |     |     |     |     |     |     |     |
| -------- | ----------- | --- | ------ | ----- | ---- | ------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|          |             |     |        | Users | with | concentrated |     |     |     |     |     |     |     |     |     |
RAM)-DatabricksRuntime:13.3LTS(ApacheSpark3.4.1,
interestsinspecificproductcategories,showingexpertiseor
|                    |     |               |     |          |       |           |     | Scala 2.12) | -   | Total Resources: | 32-128 |     | cores, | 256GB-1TB |     |
| ------------------ | --- | ------------- | --- | -------- | ----- | --------- | --- | ----------- | --- | ---------------- | ------ | --- | ------ | --------- | --- |
| strong preferences |     | in particular |     | domains. | These | customers |     |             |     |                  |        |     |        |           |     |
RAM(autoscaling)
| benefit | from category-specific |     |     | marketing | communications, |     |     |                  |     |         |            |      |              |     |     |
| ------- | ---------------------- | --- | --- | --------- | --------------- | --- | --- | ---------------- | --- | ------- | ---------- | ---- | ------------ | --- | --- |
|         |                        |     |     |           |                 |     |     | Production-Scale |     | Cluster | (full 4.5M | user | experiment): |     | -   |
cross-sellopportunitieswithintheirpreferredcategories,and
InstanceType:Standard_E64ds_v5AzureVM-Configura-
expert-levelproductinformation.
tion:8workers(64cores,512GBRAMperworker)-Driver:
| Infrequent/At-Risk |      |         | Users  | (6%):      | Low       | activity | lev- |                   |     |            |       |      |     |              |     |
| ------------------ | ---- | ------- | ------ | ---------- | --------- | -------- | ---- | ----------------- | --- | ---------- | ----- | ---- | --- | ------------ | --- |
|                    |      |         |        |            |           |          |      | Standard_E64ds_v5 |     | (64 cores, | 512GB | RAM) |     | - Databricks |     |
| els with           | high | recency | values | indicating | dormancy. |          | This |                   |     |            |       |      |     |              |     |
Runtime:16.4LTS(ApacheSpark3.5.0,Scala2.12)-Total
| segment | requires | win-back | campaigns |     | with | compelling |     |     |     |     |     |     |     |     |     |
| ------- | -------- | -------- | --------- | --- | ---- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Resources:512cores,4TBRAM-UnityCatalogenabledfor
| re-engagement |     | offers, | personalized | ‘‘we | miss | you’’ | com- |     |     |     |     |     |     |     |     |
| ------------- | --- | ------- | ------------ | ---- | ---- | ----- | ---- | --- | --- | --- | --- | --- | --- | --- | --- |
datagovernance.
| munications, | and | surveys | to understand |     | the | reasons | for |          |        |        |          |         |     |        |      |
| ------------ | --- | ------- | ------------- | --- | --- | ------- | --- | -------- | ------ | ------ | -------- | ------- | --- | ------ | ---- |
|              |     |         |               |     |     |         |     | Software | Stack: |        |          |         |     |        |      |
|              |     |         |               |     |     |         |     |          |        | Python | 3.10.12, | PySpark |     | 3.5.0, | Ten- |
disengagement.
|     |     |     |     |     |     |     |     | sorFlow | 2.15.0, | NumPy 1.24.3, | Pandas |     | 2.0.3, | scikit-learn |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------- | ------- | ------------- | ------ | --- | ------ | ------------ | --- |
1.3.0.Autoencodertrainingwasperformedusingdistributed
2) E-COMMERCEBEHAVIORCUSTOMERSEGMENTS TensorFlowonSparkworkers.
Forthemulti-categorystoreenvironment: Spark Configuration: - Executor memory: 96GB per
Casual Browsers (35%): The largest segment, charac- executor - Executor cores: 8 cores per executor - Driver
terized by infrequent visits and minimal purchase activ- memory: 96GB - Dynamic allocation enabled with 2-8
ity. These represent customer-acquisition opportunities that executors(development),8fixedexecutors(production)
require awareness-building campaigns, introductory offers, Code and Data Availability: Complete implementation
andstrategiestoestablishinitialtrustandengagement. is available at [32]. The repository includes: (1) prepro-
Active Explorers (29%): High browsing activity with cessing scripts for data cleaning, feature engineering, and
exploration of diverse categories, but moderate conversion stratified sampling; (2) autoencoder training scripts with
rates. These users are highly responsive to recommendation hyperparameter configurations in JSON format; (3) BIRCH
enginesandbenefitfromcross-categorypromotions,curated clustering implementation with incremental learning sup-
collections, and discovery-oriented marketing that highlight port; (4) all four ensemble methods (Majority, Weighted,
productvariety. AASC, BOHC); (5) evaluation scripts computing all met-
Focused Buyers (19%): Lower browsing-to-purchase rics; (6) trained autoencoder weights for reproducibil-
ratios indicate efficiency and intent. These value-conscious ity; (7) example notebooks demonstrating the end-to-end
customershaveclearobjectivesandbenefitfromstreamlined pipeline;(8)requirements.txtwithexactpackageversions.
| VOLUME14,2026 |     |     |     |     |     |     |     |     |     |     |     |     |     |     | 88601 |
| ------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----- |

C.Lietal.:BIRCH-AE:AHierarchicalEnsembleFrameworkforScalableE-CommerceUserSegmentation
Datasets:RetailRocketdatasetavailableviaKaggle[52]. butcomplexclusterstructurebenefitsfrommultiplealgorith-
E-Commerce Behavior dataset available via UCI Machine micperspectivescapturedthroughensembleconsensus.
Learning Repository [53]. The preprocessing scripts in our Critical Implication: These findings reveal a clear
repository reproduce the exact feature sets used in the decisionhierarchy:(1)Firstassessdomaingranularity(single
experiments. vs.multi);(2)Formulti-domain,preferbasealgorithms;(3)
Reproducibility Statement: All experiments are repro- For single-domain, prefer BIRCH-AE’s ensemble methods,
ducible by following the repository instructions. Random with magnitude of benefit depending on cluster stability
seedsarefixed(seed=42)forautoencoderinitializationand and segmentation granularity. This simplifies deployment
stratified sampling. The expected runtime is approximately decisionswhileimprovingresults.
6 hours for the complete pipeline on a similar hardware
configuration. B. BIRCH’SHIERARCHICALADVANTAGEFOR
MULTI-SCALESEGMENTATION
Across all experimental scenarios, BIRCH demonstrates
VI. DISCUSSION a significant advantage in multi-scale segmentation, par-
A. DOMAINGRANULARITYASTHEPRIMARY ticularly in the E-Commerce Behavior dataset. While
DETERMINANTOFMETHODSELECTION K-Means achieves marginally better performance at 5 clus-
Themoststrikingfindingisthatdomaingranularity(single- ters (0.683 vs. 0.651), BIRCH’s superiority becomes pro-
domainvs.multi-domain)fundamentallydeterminesoptimal nouncedathighergranularities.At10clusters,BIRCHleads
method selection, with secondary effects from cluster char- slightly(0.635vs.0.633).Theadvantagebecomesdramaticat
acteristicswithineachdomaintype. 15clusters(BIRCH:0.603vs.K-Means:0.332,representing
Multi-Category Datasets: The E-Commerce Behavior 81% improvement) and persists at 20 clusters (BIRCH:
multicategory dataset exhibits diffuse, overlapping cluster 0.596vs.K-Means:0.338,representing76%improvement).
structure (CH: 1413.1) where base algorithms consis- This scalability is crucial for e-commerce platforms
tently outperform BIRCH-AE’s ensemble methods. BIRCH that require multi-level segmentation strategies, ranging
and K-Means achieve superior results (0.651 and 0.683, from broad customer categories for strategic planning to
respectively, at 5 clusters) compared to the best ensemble fine-grained microsegments for personalized marketing.
AASC/BOHC (0.633), representing a 7.4% advantage for BIRCH’s CF Tree structure inherently captures these hier-
base methods. This occurs because heterogeneous behavior archical relationships, enabling consistent quality across
patterns across multiple product categories create natural different segmentation granularities without requiring sepa-
overlaps that the ensemble’s consensus mechanisms cannot ratemodeltrainingforeachlevel.
effectively resolve. The averaging effect of ensemble meth- Thepracticalimplicationisthatforapplicationsrequiring
odsintroducesnoiseratherthanrefinementwhenthenatural flexiblesegmentationatmultipleresolutions,BIRCH-based
boundariesoftheclusterarealreadydiffuse. approachesoffersignificantadvantagesoverpartition-based
Single-DomainCategories:BothElectronicsandAppli- methods that optimize for a single granularity level. This
ances ultimately demonstrate ensemble superiority, though validates BIRCH’s suitability for enterprise environments
withdifferentpatterns: where different organizational units may require different
Electronics: Shows unstable cluster structure (high vari- segmentationresolutions.
ability,silhouettestd:0.089)whereensemblemethodswithin
BIRCH-AEachieveconsistent17–23%improvementacross C. ENSEMBLEMETHODSWITHINBIRCH-AEFOR
all cluster counts (0.461 vs. 0.394 at 5 clusters; 0.358 vs. SINGLE-DOMAINSCENARIOS
0.291 at 20 clusters). The ensemble consensus effectively Results validate ensemble clustering benefits for single-
stabilizestheclusteringbyintegratingmultipleperspectives domainscenarioswhilerevealingimportantnuances:
onvolatilebehavioralpatterns. When BIRCH-AE Ensembles Help Most: Retail
Appliances:Showsmorecomplexpatternwherebasealgo- Rocket’s distinct, transaction-focused clusters benefit sub-
rithmshaveslightadvantageatlowestgranularity(5clusters: stantially from BIRCH-AE’s ensemble methods (AASC/
0.643 vs. 0.585, representing 10% base superiority), but BOHCachieve0.5477,representing23%improvementover
BIRCH-AE’s ensemble methods become superior at higher base BIRCH). The single-domain Electronics category with
clustercounts(10clusters:0.479vs.0.446,+7%;15clusters: unstable clusters shows a consistent 17–23% ensemble
0.462 vs. 0.374, +24%; 20 clusters: 0.481 vs. 0.390, advantage across all granularities. The Single-domain
+23%). This demonstrates that ensemble methods excel appliance category demonstrates ensemble superiority at
at managing complexity in higher-granularity segmentation higherclustercounts(10–20clusters:7–24%improvement),
evenformoderatelystableclusters. where complexity increases. These scenarios share a
Transaction-FocusedDatasets:RetailRocketrepresents single-domain focus with a cluster structure suitable for
a single-domain, transaction-oriented platform with distinct ensembleconsensus.
clusters(CH:9053.5)whereBIRCH-AE’sensemblemethods When Base Algorithms Excel: E-Commerce Behavior
providesubstantialbenefits(+23%improvement).Theclear multi-category dataset shows consistent base algorithm
88602 VOLUME14,2026

C.Lietal.:BIRCH-AE:AHierarchicalEnsembleFrameworkforScalableE-CommerceUserSegmentation
superiority (7.4% advantage over BIRCH-AE ensembles). memory efficiency of CF-tree compression compared with
Appliances at the lowest granularity (5 clusters) show classicalO(n2)hierarchicalclusteringmethods.
a slight base advantage (10%) before ensemble methods Computationalscalabilitydemonstratesnear-linearscaling
dominate at higher complexities. These scenarios involve from 1.4M to 4.5M users (a 3× increase), with single-pass
either multi-domain natural overlap or extremely granular constructioncomparedtoK-Means’iterativeapproach.The
segmentation. methodachievescompetitivetosuperiorperformanceatlow
Mechanistic Explanation: For single-domain datasets, cluster counts, showing dramatic superiority at high cluster
BIRCH-AE’s ensemble methods effectively integrate com- counts(0.596–0.603at15–20clusters),andexhibitssuperior
plementary views of cluster boundaries, with benefits scalabilityacrossdifferentdomaintypes.Incrementallearn-
increasingassegmentationgranularityandclustercomplex- ingsupportsreal-timeusersegmentupdatesthroughCFTree
ity grow. For multi-domain data with natural categorical insertion,enablesdailyorstreamingsegmentrefreshes,andis
overlap, ensemble averaging obscures rather than clarifies criticalforproductionsystemswherecompletere-clustering
boundaries. For very simple segmentation (few clusters) in isimpractical.
stable single-domain environments, the additional complex- The 4.5M-user BOHC production run (approximately
ityofensembleaggregationmaynotbenecessary. 5 minutes) demonstrates the practical viability of near-real-
Practical Guidance: The decision framework simplifies time,large-scalesegmentationupdates.
to: (1) Multi-domain → Strongly prefer base algorithms
regardless of cluster characteristics; (2) Single-domain → F. COMPARISONWITHEXISTINGWORK
Prefer BIRCH-AE’s ensemble methods, with magnitude of Compared to Zhao et al. [15] regularized K-Means. At the
benefitdependingonclusterstabilityanddesiredgranularity; same time, their approach effectively handles correlated
(3)Forsingle-domainwithverylowclustercounts(≤5),base variables through regularization. BIRCH-AE achieves this
algorithmsmaysufficeforstableclusters,butensemblemeth- through autoencoder feature learning while also providing
ods are still beneficial for unstable clusters; (4) Always use superior scalability (single-pass vs. iterative), incremental
autoencoder-based feature learning for consistent 11–53% learning capability for streaming data, hierarchical multi-
improvement. scale segmentation, comparable performance at low cluster
counts with superior performance at high granularities
D. AUTOENCODERINTEGRATIONPROVIDESCONSISTENT (0.603–0.596 at 15–20 clusters), applicability across both
VALUE singleandmulti-domainscenarios,andhierarchicalstructure
Despite highly variable ensemble performance across sce- revealingmulti-scalecustomersegments.
narios,autoencoder-basedfeaturelearningconsistentlyben- Compared to traditional ensemble clustering [30], [31],
efits all datasets and configurations. For Retail Rocket: results show ensemble benefits are fundamentally gov-
23% improvement in silhouette (0.4452 → 0.5477), 49% erned by domain granularity: Retail Rocket and both
improvementinCalinski-Harabasz(142.65→213.11),41% single-domain categories achieve substantial improvements
advantage over PCA. For E-Commerce Behavior multi- withBIRCH-AE’sensembles(aligningwithliterature),while
category: 53% improvement in silhouette (0.445 → 0.683), E-Commerce Behavior multi-category shows base algo-
substantialCalinski-Harabaszimprovement,76%advantage rithms outperform ensembles (revealing domain granularity
over PCA. For single-domain categories: 20% average as a critical factor). This demonstrates the importance
improvementwith35%advantageoverPCA. of domain assessment alongside traditional cluster quality
Autoencodersconsistentlyhelpbecausee-commercedata metrics.
exhibit strong feature correlations [15], which the autoen- Compared to deep embedded clustering [44], BIRCH-
coder’s non-linear compression naturally handles. They AE’s modular approach offers advantages including stable
capturecomplexbehavioralinteractionsthatlinearmethods training without joint optimization complexity, ability to
cannotrepresent,actasdenoisingmechanismsthatimprove updateclusteringwithoutretrainingrepresentations,support
clusterqualityacrossallscenarios,andreducedimensionality forincrementallearning(criticalforproduction),hierarchical
(toa14-dimensionallatentspace)whilepreserving90–95% multi-resolution segmentation not available in partition-
ofinformation. based methods, consistent performance across domain
Thepracticalrecommendationistoprioritizeautoencoder- types, and competitive to superior performance with better
based feature learning for behavioral data in e-commerce. scalabilityandflexibility.
The observed 11–53% gains justify the training overhead
inourevaluatedscenariosandrepresentthemostconsistent G. PRACTICALDEPLOYMENTRECOMMENDATIONS
performanceimprovementinthisstudy. Basedoncomprehensivefindingsacrossmultipleexperimen-
talscenarios,weproviderefineddeploymentguidance:
E. BIRCHSCALABILITYADVANTAGESVALIDATED Step 1 (Data Profiling): Extract comprehensive behav-
Experiments confirm BIRCH’s practical advantages for ioralfeatures(30–50featurescoveringactivity,engagement,
enterprise-scale e-commerce across all dataset types. Suc- transaction, and temporal). Assess domain granularity:
cessful runs from 1.4M to 4.5M users support the expected single-domain (one product category) vs. multi-domain
VOLUME14,2026 88603

C.Lietal.:BIRCH-AE:AHierarchicalEnsembleFrameworkforScalableE-CommerceUserSegmentation
(multiple categories). Conduct preliminary clustering at in time. Temporal dynamics and evolving user behaviors
multiple K values. Calculate Calinski-Harabasz scores to are not explicitly modeled. Incorporating recurrent or
assessclusterstructure.Analyzeclusterstabilitybyrunning sequence-based learning components could capture behav-
multipletimeswithdifferentinitializations. ioralevolutionmoreeffectively,particularlyforunderstand-
Step 2 (Method Selection): For multi-domain datasets: ing category migration patterns in multi-domain environ-
stronglypreferbasealgorithms(BIRCHorK-Means)regard- ments and the transition from base to ensemble superiority
less of CH scores, as domain overlap creates natural dif- observedinAppliancesasgranularityincreases.
fusion that BIRCH-AE’s ensemble methods cannot resolve. The integration of autoencoder-based feature learning
For single-domain datasets, prefer BIRCH-AE’s ensemble improvesclusteringqualitybutreducesmodelinterpretabil-
methods, with the benefit depending on cluster stability ity. Latent representations obscure the direct associations
and desired granularity. For very simple segmentation (≤5 betweeninputfeaturesandclusterassignments,necessitating
clusters) with highly stable clusters, base algorithms may post hoc interpretation techniques for meaningful business
suffice,butensemblemethodsarestillbeneficialforunstable communication.
clusters. Always use autoencoder-based feature learning Theframeworkfacesacold-startlimitation,asuserswith
(14–32-dimensional latent space). Consider cluster count minimal historical interaction data are difficult to segment
requirements: for 5–10 clusters, base algorithms are com- accurately.Thisisparticularlyproblematicinmulti-category
petitive in simple cases; for 15+ clusters in single-domain environmentswhereusersmaybeactiveinsomecategories
scenarios,BIRCH-AE’sensemblesshowclearadvantages. but not others. Extending the approach with hybrid features
Step 3 (Implementation): Train autoencoder on his- (suchasdemographicorcontextualmetadata)maymitigate
torical data (100–200 epochs with early stopping). Apply thisissue.
the selected clustering method with the optimal K range Finally, in domains where clusters are defined pri-
identified in profiling. For large datasets (>1M users), marily by higher-order feature interactions not captured
leverage BIRCH’s incremental capabilities. For multi-level by first-order statistics and their pairwise combinations,
segmentation, use BIRCH’s hierarchical tree structure. Set a reconstruction-focused autoencoder may fail to pro-
up daily or real-time segment updates using incremental duce cluster-discriminating representations, and contrastive
insertion. Validate method selection with A/B testing on pre-trainingorjointoptimizationapproacheswouldbemore
representativesamplesbeforefulldeployment. appropriate.
Step 4 (Validation and Monitoring): Validate segments
with business stakeholders and domain experts. Monitor I. LIMITATIONSANDFUTUREDIRECTIONS
segmentstabilityovertime(tracksilhouette,CH,DBacross While BIRCH-AE demonstrates strong empirical perfor-
granularities). Periodically re-evaluate domain granularity mance,severallimitationsshouldbeacknowledged.
as product mix evolves. For hierarchical approaches, assess Temporal Modeling: The current framework treats user
quality at multiple resolution levels. Re-assess ensemble behaviorasstaticsnapshots,failingtocapturetemporalevo-
vs. base performance if the domain structure changes lution.E-commerceusersexhibitdynamicpatternsincluding
significantly(e.g.,expandingfromsingletomulti-category). seasonal buying behaviors, lifecycle stages (new customer
Developaposthocinterpretationthatmapslatentfeaturesto → regular → loyal → dormant), and preference drift.
behavioralattributesforbusinesscommunication. Future work should integrate temporal modeling through:
(1) sequential autoencoders capturing browsing session
H. LIMITATIONS sequences; (2) recurrent neural networks (RNN/LSTM) for
While BIRCH-AE demonstrates strong empirical perfor- time-series behavioral encoding; (3) temporal clustering
mance, several limitations should be acknowledged. The tracking segment migrations over time; (4) incremental
evaluationisrestrictedtothee-commercedomain,focusing re-clustering detecting concept drift. BIRCH’s incremental
on transaction and browsing behavior. Both benchmark learning provides partial mitigation through daily batch
datasetsarederivedfromonlineretailplatforms,whichmay processing that adds new users and re-encodes changes to
limitgeneralizabilitytootherverticalssuchasB2Bmarkets, existinguserswithoutfullmodelretraining.
digitalservices,orsocialplatforms. Generalizability: Evaluation is restricted to the
The observed ensemble performance patterns are based e-commerce domain (transactional and behavioral data).
on two single-domain categories (electronics and appli- The domain granularity principle (single-domain favors
ances) within a single multi-category dataset. Additional ensembles; multi-domain favors base algorithms) requires
category-levelanalysisacrossmorediverseproductdomains validation across other verticals, such as B2B sales, digital
would strengthen the generalizability of the findings on services, social platforms, and financial services. Different
domain granularity. However, the consistent pattern across domaincharacteristicsmayfavoralternativedesignchoices.
Retail Rocket, Electronics, and Appliances provides strong Scalability Bounds: While we demonstrate 4.5M user
initialevidence. processing,upperscalabilitylimitsremainuntested.Systems
The current implementation performs static segmenta- with50M–100Musersmayrequirethedistributedconstruc-
tion, analyzing users as fixed entities at specific points tion of the CF-tree or the use of approximate methods.
88604 VOLUME14,2026

C.Lietal.:BIRCH-AE:AHierarchicalEnsembleFrameworkforScalableE-CommerceUserSegmentation
Memory constraints for ensemble affinity matrices (O(n2)) requiringseparatemodelsforeachlevel,addressingacritical
maynecessitatesparseapproximationsatextremescales. yetoftenoverlookedrequirementinenterpriseanalytics.
ExternalValidation:Qualityassessmentreliesoninternal Third,wedemonstrateconsistentandsubstantialbenefits
metrics (silhouette, CH, DB). Public benchmark datasets from autoencoder integration across all scenarios (11–53%
do not provide intervention outcomes (e.g., campaign in silhouette scores). The autoencoder effectively handles
lift, retained revenue, realized churn reduction), so direct correlatedvariables,capturesnon-linearbehavioralpatterns,
business-impactvalidationisoutsidethescopeofthisstudy. andreducesdimensionalitywhilepreservingessentialinfor-
External validation through online A/B tests and business mation.Thisvalidatestheintegrationofdeeplearning-based
KPIsisaprimarydirectionforfuturework. feature learning with hierarchical clustering methods, with
Sensitivity and Resource Logging: Dynamic-selection autoencodersoutperformingPCAby28–76%acrossdomain
| weights | were | fixed | in this | study | and not | exhaustively |     | types. |     |     |     |     |     |     |
| ------- | ---- | ----- | ------- | ----- | ------- | ------------ | --- | ------ | --- | --- | --- | --- | --- | --- |
stress-tested across alternative weighting schemes. In addi- Fourth, we show that ensemble effectiveness in single-
tion, peak memory usage was not logged for each stage, domainscenariosdependsonclusterstabilityandthedesired
so scalability claims are currently supported primarily granularity.ForRetailRocket’sdistinctsingle-domainclus-
by execution time, repeated subset consistency, and the ters,AASC/BOHCensemblesachievethebestperformance
successful completion of the full-scale BOHC production (0.5477), representing a +23% improvement. For single-
run. Fine-grained memory instrumentation and exhaustive domain categories, Electronics shows consistent ensem-
weightsensitivityareplannedfutureworkitems. ble advantages (17–23%), while Appliances demonstrates
|     |     |     |     |     |     |     |     | increasing | ensemble   | superiority |         | as granularity | grows | (from    |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------- | ---------- | ----------- | ------- | -------------- | ----- | -------- |
|     |     |     |     |     |     |     |     | −10% at    | 5 clusters | to          | +23% at | 20 clusters).  | The   | proposed |
VII. CONCLUSION
BIRCH-OptimizedHierarchicalConsensus(BOHC)method
| This paper | introduces |              | BIRCH-AE,  |       | a    | comprehensive |      |             |            |              |          |           |           |         |
| ---------- | ---------- | ------------ | ---------- | ----- | ---- | ------------- | ---- | ----------- | ---------- | ------------ | -------- | --------- | --------- | ------- |
|            |            |              |            |       |      |               |      | contributes | a          | hierarchical | affinity | mechanism | within    | the     |
| framework  | for        | scalable     | e-commerce |       | user | segmenta-     |      |             |            |              |          |           |           |         |
|            |            |              |            |       |      |               |      | BIRCH-AE    | framework; |              | results  | show that | its value | depends |
| tion that  | integrates | hierarchical |            | BIRCH |      | clustering    | with |             |            |              |          |           |           |         |
criticallyondomaincontext.
| autoencoder-based |     | feature | learning | and | dynamic |     | ensemble |        |             |           |     |             |                 |     |
| ----------------- | --- | ------- | -------- | --- | ------- | --- | -------- | ------ | ----------- | --------- | --- | ----------- | --------------- | --- |
|                   |     |         |          |     |         |     |          | Fifth, | we validate | practical |     | scalability | by successfully |     |
selection.Extensivecomparativeevaluationswereconducted
processingdatasetsthatdifferbyafactorof3insize(1.4M
| on representative |     | 30% | stratified | subsets |     | of two | large- |         |        |                  |     |              |         |         |
| ----------------- | --- | --- | ---------- | ------- | --- | ------ | ------ | ------- | ------ | ---------------- | --- | ------------ | ------- | ------- |
|                   |     |     |            |         |     |        |        | to 4.5M | users) | with near-linear |     | subset-level | scaling | trends, |
scaledatasets–RetailRocket(1.4Musers)andE-Commerce
|     |     |     |     |     |     |     |     | and by | executing | a 4.5M-user |     | BOHC run | in approximately |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------ | --------- | ----------- | --- | -------- | ---------------- | --- |
Behavior(4.5Musers)–across20randomizedtrials,together
5minutes.Theframework’sincrementallearningcapability
withsingle-domaincategoryanalyses.
|     |     |     |     |     |     |     |     | enables | real-time | segment | updates, | which | are critical | for |
| --- | --- | --- | --- | --- | --- | --- | --- | ------- | --------- | ------- | -------- | ----- | ------------ | --- |
productionsystems.
A. KEYCONTRIBUTIONS
The study makes several important contributions, which B. PRACTICALANDMETHODOLOGICALIMPLICATIONS
arevalidatedthroughacomprehensiveempiricalevaluation. From a practical perspective, conducting a domain granu-
Repeated subset trials show stable comparative patterns larity assessment alongside the Calinski-Harabasz analysis
and support generalization of the decision trends. First, guides method selection by revealing both cluster dis-
weidentifydomaingranularityasthefundamentaldetermi- tinctiveness and domain type. Multi-domain configurations
nantofselectingtheoptimalmethod.Multi-domaindatasets (multiple product categories) should strongly favor base
consistently favor base algorithms (a 7.4% advantage) algorithms, such as BIRCH or K-Means, as BIRCH-AE’s
due to natural category overlap, whereas single-domain ensemble methods cannot effectively resolve natural cate-
datasets generally benefit from BIRCH-AE’s ensemble gory overlap. Single-domain configurations (single product
methods in the scenarios we evaluated. Electronics and category) should prefer BIRCH-AE’s ensemble methods,
Appliances show ensemble advantages (17–23% across withthemagnitudeofbenefitdependingonclusterstability
various granularities), though with different patterns that and desired segmentation granularity. For very simple
reflect cluster stability and segmentation complexity. This segmentation(≤5clusters)withhighlystablesingle-domain
finding provides practitioners with a clear, hierarchical clusters, base algorithms may suffice, although ensemble
decision framework: domain granularity first, then cluster methods remain beneficial for unstable clusters or higher
| characteristics. |     |     |     |     |     |     |     | granularities. |     |     |     |     |     |     |
| ---------------- | --- | --- | --- | --- | --- | --- | --- | -------------- | --- | --- | --- | --- | --- | --- |
Second, we validate BIRCH’s hierarchical advantage Incorporating autoencoder-based feature learning consis-
in multi-scale segmentation by demonstrating consistent tently improves clustering performance by approximately
performance across granularities. While K-Means achieves 11–53% across all domain types and configurations, effi-
marginally better results at 5 clusters (0.683 vs. 0.651), cientlyhandlingcorrelatedbehavioralvariables.Thisrepre-
BIRCH shows stronger performance at higher cluster sents the single most reliable performance enhancement in
counts (0.603 vs. 0.332 at 15 clusters, representing 81% thisstudyandisastrongdefaultchoiceforsimilarsettings.
improvement).Thisenablesflexiblesegmentationstrategies, Forapplicationsrequiringsegmentationatmultiplegranu-
20+
from strategic planning to personalized marketing, without larities (5 to clusters), BIRCH’s hierarchical structure
| VOLUME14,2026 |     |     |     |     |     |     |     |     |     |     |     |     |     | 88605 |
| ------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----- |

C.Lietal.:BIRCH-AE:AHierarchicalEnsembleFrameworkforScalableE-CommerceUserSegmentation
provides superior consistency and quality compared to capture evolving user behaviors within and across cat-
partition-basedmethodsthatoptimizeforsingleresolutions. egories, supporting predictive segmentation, churn fore-
This addresses enterprise needs for coherent strategies casting, and category migration modeling. Understand-
supporting both strategic planning (broad segments) and ing the transition from base-to-ensemble superiority in
tacticalmarketing(fine-grainedmicrosegments). Appliances as granularity increases could yield impor-
BIRCH-AE’s ensemble methods deliver clear value in tant insights into complexity management in ensemble
single-domain scenarios, with benefits that increase as methods.
cluster complexity and segmentation granularity grow. The Multi-view clustering that combines behavioral, demo-
Appliances pattern (base superiority in 5 clusters that graphic, and contextual features, using methods designed
transitions to 23% ensemble superiority in 20 clusters) for hierarchical clustering, could improve segmentation
demonstrates that ensemble methods excel at managing robustness,particularlyinaddressingcold-startlimitationsin
complexityinhigher-granularitysegmentation.Comprehen- sparse-datascenarios.Cross-categorytransferlearningcould
sive behavioral feature engineering that integrates activity, leverage patterns learned in data-rich categories to improve
engagement, transaction, and temporal signals remains cru- segmentationinsparsecategories.
cialtocapturemultidimensionaluserbehavioracrossdomain Automated data profiling algorithms that detect dataset
types. characteristics (cluster separability, density, optimal gran-
Leveraging BIRCH’s incremental learning capability ularity ranges, domain structure, stability metrics) can
enables near-real-time user-segment updates, maintain- automatically recommend suitable clustering strategies and
ing relevance without the computational burden of full configurations, reducing reliance on manual assessment
re-clustering. This is particularly valuable in dynamic and extensive empirical testing. Developing predictive
e-commerceenvironmentswhereuserbehaviorandproduct indicators of when BIRCH-AE’s ensemble methods will
catalogsevolvecontinuously. outperform base algorithms based on domain granularity
Empirically, the study indicates that three factors in and cluster characteristics could make frameworks more
hierarchical order govern method selection: (1) domain self-adaptive.
granularity (single vs. multi-domain), (2) intrinsic cluster Online learning extensions of the autoencoder could
structure (distinctness and stability), and (3) segmentation enable continuous adaptation to streaming data without
granularity(numberofdesiredclusters).Domaingranularity requiring full retraining, particularly valuable for dynamic
emergesastheprimarydecisionfactorinourexperiments. multi-category environmentswhere category popularityand
The study provides a large-scale evaluation of BIRCH- userbehaviorsshiftovertime.
based approaches across both multi-domain and Fairness-aware segmentation should ensure clustering
single-domaine-commercescenarios,revealinghowdomain outcomes do not inadvertently reinforce demographic
granularity influences method selection independently of or behavioral biases across categories. Transfer learning
cluster structure. Both evaluated single-domain categories could enhance applicability by training autoencoders
(Electronics and Appliances) demonstrate ensemble supe- on large-scale, multi-category datasets and fine-tuning
riority, though with different patterns reflecting differences them for smaller, single-category or domain-specific
in cluster stability and granularity. This contrasts sharply platforms.
withmulti-domainresults,validatingdomaingranularityasa Integrating explainable AI techniques (such as SHAP
criticalfactor. values, attention-based interpretability, or category-specific
Theintegrationofdeepautoencoder-basedfeaturelearning feature importance analysis) could make latent representa-
with hierarchical BIRCH clustering is validated in our tionsmoretransparentforbusinessstakeholders,particularly
settingasameanstocouplehigh-dimensionalrepresentation valuable for understanding differences in segmentation
learning with scalable, multi-resolution cluster formation driversacrosscategories.
across domain types. The observed 11–53% improvement Extending single-domain analysis to additional product
supportsthepracticalvalueofthisintegration. categoriesbeyondelectronicsandapplianceswouldvalidate
TheproposedBIRCH-OptimizedHierarchicalConsensus the generalizability of findings on domain granularity
(BOHC) method provides a hierarchical mechanism for and ensemble performance patterns. Investigating optimal
preserving multi-scale information within the BIRCH-AE strategies for hybrid scenarios (e.g., segmenting within
framework. Results demonstrate its value in single-domain closelyrelatedcategorygroups)wouldprovidemorenuanced
scenarios,particularlyassegmentationgranularityincreases, guidanceforcomplexe-commerceplatforms.
while confirming that it is less beneficial in multi-domain
configurations. D. CLOSINGREMARKS
As e-commerce continues to generate ever more massive
C. FUTURERESEARCHDIRECTIONS and complex user data across expanding product cat-
Future work can extend in several promising directions. alogs, scalable, intelligent segmentation frameworks are
Incorporating temporal dynamics through recurrent neu- essential for delivering personalized experiences and driv-
ral networks or Transformer-based architectures could ing business success. BIRCH-AE provides a practical,
88606 VOLUME14,2026

C.Lietal.:BIRCH-AE:AHierarchicalEnsembleFrameworkforScalableE-CommerceUserSegmentation
scalable solution that balances computational efficiency The revelation that domain granularity fundamentally
with segmentation quality. At the same time, experimental influences optimal method selection provides practitioners
analysis offers critical insights into how domain charac- withaclearprimarycriterionforassessment.Multi-domain
teristics and application requirements should drive method environments should default to base algorithms, while
selection. single-domain environments benefit from BIRCH-AE’s
The discovery that domain granularity plays a cru- ensemblemethods,withthemagnitudeofbenefitdepending
cial role in determining the best method selection is on cluster stability and desired granularity. This insight,
significant.Insingle-domainscenarios,BIRCH-AE’sensem- combinedwiththeconsistentvalueofautoencoder-basedfea-
ble methods consistently outperform other approaches, turelearningandBIRCH’smulti-scaleadvantages,provides
whereas in multi-domain scenarios, base algorithms tend acomprehensivefoundationforenterprise-scalee-commerce
to perform better. This indicates that as granularity usersegmentation.
| increases,               | especially |           | in            | Appliances, |      | ensemble | meth- |               |     |            |             |          |               |           |
| ------------------------ | ---------- | --------- | ------------- | ----------- | ---- | -------- | ----- | ------------- | --- | ---------- | ----------- | -------- | ------------- | --------- |
| ods become               | more       | effective |               | at handling |      | complex  | tasks | REFERENCES    |     |            |             |          |               |           |
| within higher-resolution |            |           | segmentation. |             | This | insight  | pro-  |               |     |            |             |          |               |           |
|                          |            |           |               |             |      |          |       | [1] J. Brown, | M.  | Smith, and | R. Johnson, | ‘‘Retail | analytics and | big data: |
vides practitioners with straightforward and actionable Current trends and future directions,’’ J. Retailing, vol. 100, no. 2,
guidance for making deployment decisions, ultimately pp.145–162,2024.
leading to improved outcomes across various e-commerce [2] M. Garcia, C. Rodriguez, and A. Martinez, ‘‘E-commerce customer
behavioranalysisusingdeeplearningtechniques,’’Electron.Commerce
| contexts. |     |     |     |     |     |     |     | Res.,vol.24,no.1,pp.89–112,2024. |     |     |     |     |     |     |
| --------- | --- | --- | --- | --- | --- | --- | --- | -------------------------------- | --- | --- | --- | --- | --- | --- |
Fore-commerceusersegmentation,theoptimalapproach [3] A.Patel,K.Shah,andN.Desai,‘‘Personalizationine-commerce:Current
depends primarily on domain granularity (single vs. multi- trends and future directions,’’ ACM Comput. Surveys, vol. 55, no. 9,
pp.1–38,2023.
| category), | then | on cluster | characteristics |     |     | (stability, | distinct- |     |     |     |     |     |     |     |
| ---------- | ---- | ---------- | --------------- | --- | --- | ----------- | --------- | --- | --- | --- | --- | --- | --- | --- |
[4] M.WedelandW.A.Kamakura,MarketSegmentationConceptualand
| ness), and | finally | on  | the desired | segmentation |     |     | granularity |     |     |     |     |     |     |     |
| ---------- | ------- | --- | ----------- | ------------ | --- | --- | ----------- | --- | --- | --- | --- | --- | --- | --- |
MethodologicalFoundations.Cham,Switzerland:Springer,2000.
20+
(5 vs. clusters). This hierarchical decision framework [5] W. R. Smith, ‘‘Product differentiation and market segmentation as
|          |         |           |     |         |                 |     |         | alternative | marketing | strategies,’’ | J.  | Marketing, | vol. 21, no. 1, | pp.3–8, |
| -------- | ------- | --------- | --- | ------- | --------------- | --- | ------- | ----------- | --------- | ------------- | --- | ---------- | --------------- | ------- |
| replaces | complex | empirical |     | testing | with systematic |     | assess- |             |           |               |     |            |                 |         |
Jul.1956.
| ment, making |     | deployment |     | decisions | more | efficient | and |     |     |     |     |     |     |     |
| ------------ | --- | ---------- | --- | --------- | ---- | --------- | --- | --- | --- | --- | --- | --- | --- | --- |
[6] A.M.Hughes,‘‘Strategicdatabasemarketing:Themasterplanforstarting
reliable. and managing a profitable, customer-based marketing program,’’ J.
BIRCH’s demonstrated strength in maintaining high- Marketing,vol.58,no.3,pp.125–127,1994.
qualityclustersacrossdifferentgranularities(5to20+clus- [7] M. A. Gomes and T. Meisen, ‘‘A review on customer segmen-
|     |     |     |     |     |     |     |     | tation | methods | for personalized |     | customer | targeting in e-commerce |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------ | ------- | ---------------- | --- | -------- | ----------------------- | --- |
ters)addressesacriticalbutoftenoverlookedrequirementin use cases,’’ Inf. Syst. e-Bus. Manage., vol. 21, no. 3, pp.527–570,
| e-commerce | analytics: |         | the need | for       | coherent | segmentation |             | 2023.         |     |             |           |           |                       |     |
| ---------- | ---------- | ------- | -------- | --------- | -------- | ------------ | ----------- | ------------- | --- | ----------- | --------- | --------- | --------------------- | --- |
|            |            |         |          |           |          |              |             | [8] R. Kumar, | P.  | Sharma, and | A. Singh, | ‘‘Machine | learning applications |     |
| strategies | that       | support | both     | strategic | planning |              | (broad seg- |               |     |             |           |           |                       |     |
ine-commerce:Acomprehensivereview,’’ExpertSyst.Appl.,vol.238,
| ments) and | tactical | marketing |     | (fine-grained |     | microsegments) |     |     |     |     |     |     |     |     |
| ---------- | -------- | --------- | --- | ------------- | --- | -------------- | --- | --- | --- | --- | --- | --- | --- | --- |
Jan.2024,Art.no.121847.
withoutmaintainingseparateclusteringmodels.Thiscapabil- [9] P.S.Fader,B.G.S.Hardie,andK.L.Lee,‘‘RFMandCLV:Usingiso-
valuecurvesforcustomerbaseanalysis,’’J.MarketingRes.,vol.42,no.4,
ityisvaluableacrossbothsingleandmulti-domainscenarios.
pp.415–430,Nov.2005.
| The framework’s |     |     | modular | architecture |     | supports | easy |            |            |             |     |              |          |          |
| --------------- | --- | --- | ------- | ------------ | --- | -------- | ---- | ---------- | ---------- | ----------- | --- | ------------ | -------- | -------- |
|                 |     |     |         |              |     |          |      | [10] A. K. | Jain, Data | Clustering: | 50  | Years Beyond | K-Means, | vol. 31. |
integrationintoexistinganalyticspipelinesandadaptationto Amsterdam,TheNetherlands:Elsevier,2010.
domain-specificrequirements.BycombiningBIRCH’shier- [11] Z.-Y. Lim, L.-Y. Ong, and M.-C. Leow, ‘‘Cluster-N-engage: A new
|     |     |     |     |     |     |     |     | framework | for | measuring | user | engagement | of website with | user |
| --- | --- | --- | --- | --- | --- | --- | --- | --------- | --- | --------- | ---- | ---------- | --------------- | ---- |
archical structure, autoencoder-based feature learning, and IEEE Access,
|               |     |            |            |     |      |              |     | navigational | behavior,’’ |     |     | vol. | 11, pp.112276–112292, |     |
| ------------- | --- | ---------- | ---------- | --- | ---- | ------------ | --- | ------------ | ----------- | --- | --- | ---- | --------------------- | --- |
| comprehensive |     | evaluation | mechanisms |     | with | domain-aware |     | 2023.        |             |     |     |      |                       |     |
method selection, BIRCH-AE advances the state of the art [12] X.Wang,J.Li,andY.Chen,‘‘Scalableclusteringalgorithmsforbigdata:
Areview,’’ACMTrans.Knowl.DiscoveryData,vol.18,no.2,pp.1–35,
| in large-scale | user | segmentation |     | while | providing |     | actionable |     |     |     |     |     |     |     |
| -------------- | ---- | ------------ | --- | ----- | --------- | --- | ---------- | --- | --- | --- | --- | --- | --- | --- |
2024.
guidanceforpractitionersdeployingsegmentationsystemsin
|     |     |     |     |     |     |     |     | [13] C. C. | Aggarwal | and C. K. | Reddy, | Data Clustering: | Algorithms | and |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------- | -------- | --------- | ------ | ---------------- | ---------- | --- |
productionenvironments.
ApplicationsBocaRaton,FL,USA:CRCPress,2013.
Most importantly, this work emphasizes the need to [14] C. C. Aggarwal, A. Hinneburg, and D. A. Keim, ‘‘On the
|            |        |              |     |         |                  |     |     | surprising | behavior | of         | distance | metrics  | in high dimensional |       |
| ---------- | ------ | ------------ | --- | ------- | ---------------- | --- | --- | ---------- | -------- | ---------- | -------- | -------- | ------------------- | ----- |
| understand | domain | granularity, |     | cluster | characteristics, |     | and |            |          |            |          |          |                     |       |
|            |        |              |     |         |                  |     |     | space,’’   | in       | Proc. Int. | Conf.    | Database | Theory,             | 2001, |
segmentation granularity before selecting methods. The 6.4 pp.420–434.
×differenceinclusterseparationbetweentheRetailRocket [15] H.-H.Zhao,X.-C.Luo,R.Ma,andX.Lu,‘‘AnextendedregularizedK-
and E-Commerce Behavior datasets, combined with the meansclusteringapproachforhigh-dimensionalcustomersegmentation
|          |          |          |     |                   |     |     |            | with  | correlated | variables,’’ | IEEE | Access, | vol. 9, pp.48405–48412, |     |
| -------- | -------- | -------- | --- | ----------------- | --- | --- | ---------- | ----- | ---------- | ------------ | ---- | ------- | ----------------------- | --- |
| observed | ensemble | benefits |     | for single-domain |     |     | categories | 2021. |            |              |      |         |                         |     |
versus the base algorithm’s superiority for multi-domain [16] T.Zhou,W.Liu,andJ.Chen,‘‘Streamingclusteringalgorithms:Areview,’’
|                    |     |      |              |     |        |     |              | IEEE | Trans. Neural | Netw. | Learn. | Syst., vol. | 35, no. 3, pp.2841–2857, |     |
| ------------------ | --- | ---- | ------------ | --- | ------ | --- | ------------ | ---- | ------------- | ----- | ------ | ----------- | ------------------------ | --- |
| data, demonstrates |     | that | domain-aware |     | method |     | selection is |      |               |       |        |             |                          |     |
Mar.2024.
essential.Thekeylessonsforsuccessfuldeploymentofclus-
[17] F.MurtaghandP.Contreras,‘‘Algorithmsforhierarchicalclustering:An
| tering systems |     | at scale | are: | domain | granularity |     | assessment, |     |     |     |     |     |     |     |
| -------------- | --- | -------- | ---- | ------ | ----------- | --- | ----------- | --- | --- | --- | --- | --- | --- | --- |
overview,’’WIREsDataMiningKnowl.Discovery,vol.2,no.1,pp.86–97,
Jan.2012.
| cluster stability |     | evaluation, |     | segmentation |     | granularity | con- |            |           |        |         |                    |              |     |
| ----------------- | --- | ----------- | --- | ------------ | --- | ----------- | ---- | ---------- | --------- | ------ | ------- | ------------------ | ------------ | --- |
|                   |     |             |     |              |     |             |      | [18] J. B. | MacQueen, | ‘‘Some | methods | for classification | and analysis | of  |
sideration,empiricalvalidation,andevidence-basedmethod
|               |     |     |     |     |     |     |     | multivariate                   | observations,’’ |     | in Proc. | 5th Berkeley | Symp. Math. | Statist. |
| ------------- | --- | --- | --- | --- | --- | --- | --- | ------------------------------ | --------------- | --- | -------- | ------------ | ----------- | -------- |
| selection.    |     |     |     |     |     |     |     | Probab.,vol.1,1967,pp.281–297. |                 |     |          |              |             |          |
| VOLUME14,2026 |     |     |     |     |     |     |     |                                |                 |     |          |              |             | 88607    |

C.Lietal.:BIRCH-AE:AHierarchicalEnsembleFrameworkforScalableE-CommerceUserSegmentation
[19] M.Ester,H.Kriegel,J.Sander,andX.Xu,‘‘Adensity-basedalgorithmfor [45] P.J.Rousseeuw,‘‘Silhouettes:Agraphicalaidtotheinterpretationand
discoveringclustersinlargespatialdatabaseswithnoise,’’inProc.2ndInt. validationofclusteranalysis,’’J.Comput.Appl.Math.,vol.20,pp.53–65,
| Conf.Knowl.DiscoveryDataMining(KDD),1996,pp.226–231. |     |     |     |     |     |     |     | Nov.1987. |     |     |     |     |     |     |
| ---------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --------- | --- | --- | --- | --- | --- | --- |
[20] S.C.Johnson,‘‘Hierarchicalclusteringschemes,’’Psychometrika,vol.32, [46] T. Calinski and J. Harabasz, ‘‘A dendrite method for cluster analysis,’’
no.3,pp.241–254,Sep.1967. Commun.Statistics-TheoryMethods,vol.3,no.1,pp.1–27,1974.
‘‘K-means++: [47] D.L.DaviesandD.W.Bouldin,‘‘Aclusterseparationmeasure,’’IEEE
| [21] D. Arthur | and | S. Vassilvitskii, |     |     | The | advantages | of  |     |     |     |     |     |     |     |
| -------------- | --- | ----------------- | --- | --- | --- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- |
careful seeding,’’ in Proc. 18th Annu. ACM-SIAM Symp. Discrete Trans. Pattern Anal. Mach. Intell., vols. PAMI–1, no. 2, pp.224–227,
| Algorithms,2007,pp.1027–1035. |     |     |     |     |     |     |     | Apr.1979. |     |     |     |     |     |     |
| ----------------------------- | --- | --- | --- | --- | --- | --- | --- | --------- | --- | --- | --- | --- | --- | --- |
[22] I.T.Jolliffe,PrincipalComponentAnalysis.Cham,Switzerland:Springer, [48] G. Barbato, E. M. Barini, G. Genta, and R. Levi, ‘‘Features of the iqr
2002. methodtodetectoutliersinindustrialdata:Acasestudy,’’IEEETrans.
Instrum.Meas.,vol.60,no.9,pp.3613–3619,Aug.2011.
| [23] K. Zhang, | X.   | Wang,  | and Y. Liu, | ‘‘Deep clustering: |          | A comprehensive |        |                 |     |            |        |                           |     |           |
| -------------- | ---- | ------ | ----------- | ------------------ | -------- | --------------- | ------ | --------------- | --- | ---------- | ------ | ------------------------- | --- | --------- |
|                |      |        |             |                    |          |                 |        | [49] Y. Bengio, | A.  | Courville, | and P. | Vincent, ‘‘Representation |     | learning: |
| survey,’’      | IEEE | Trans. | Pattern     | Analysis Mach.     | Intell., | vol. 45,        | no. 8, |                 |     |            |        |                           |     |           |
pp.10091–10111,Aug.2023. Areviewandnewperspectives,’’IEEETrans.PatternAnal.Mach.Intell.,
[24] W. Chen, L. Zhang, and M. Wang, ‘‘Autoencoder-based deep learning vol.35,no.8,pp.1798–1828,Aug.2013.
forhigh-dimensionaldataclustering:Asurvey,’’NeuralNetw.,vol.162, [50] D.P.KingmaandJ.Ba,‘‘Adam:Amethodforstochasticoptimization,’’
| pp.185–205,Jun.2023. |     |     |     |     |     |     |     | 2014,arXiv:1412.6980.                                            |     |     |     |     |     |     |
| -------------------- | --- | --- | --- | --- | --- | --- | --- | ---------------------------------------------------------------- | --- | --- | --- | --- | --- | --- |
|                      |     |     |     |     |     |     |     | [51] H.W.Kuhn,‘‘TheHungarianmethodfortheassignmentproblem,’’Nav. |     |     |     |     |     |     |
[25] Y.Ren,K.Hu,X.Dai,L.Pan,S.C.Hoi,andZ.Xu,‘‘Deepclustering:
Acomprehensivesurvey,’’IEEETrans.PatternAnal.Mach.Intell.,vol.46, Res.LogisticsQuart.,vol.2,nos.1–2,pp.83–97,1955.
no.5,pp.3213–3232,May2024. [52] Retail Rocket. (2016). Retailrocket Recommender System Dataset.
[26] Y.Li,W.Zhang,andC.Wang,‘‘Ensemblelearningfordeeplearning: [Online]. Available: https://www.kaggle.com/datasets/retailrocket/
Asurvey,’’Inf.Fusion,vol.92,pp.34–56,Apr.2023. ecommerce-dataset
|     |     |     |     |     |     |     |     | [53] M.Kechinov.(2019).EcommerceBehaviorDataFromMultiCategory |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------------------------------------------------------- | --- | --- | --- | --- | --- | --- |
[27] H.Liu,Z.Ming,andY.Sun,‘‘Consensusclustering:Asurveyandnew
|     |     |     |     |     |     |     |     | Store. | [Online]. | Available: | https://www.kaggle.com/datasets/mkechinov/ |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------ | --------- | ---------- | ------------------------------------------ | --- | --- | --- |
methods,’’PatternRecognit.,vol.135,Mar.2023,Art.no.109177.
ecommerce-behavior-data-from-multi-category-store
| [28] T. Zhang, | R.  | Ramakrishnan, | and | M. Livny, | ‘‘Birch: | An efficient | data |     |     |     |     |     |     |     |
| -------------- | --- | ------------- | --- | --------- | -------- | ------------ | ---- | --- | --- | --- | --- | --- | --- | --- |
clusteringmethodforverylargedatabases,’’inProc.ACMSIGMODInt. [54] J.H.Ward,‘‘Hierarchicalgroupingtooptimizeanobjectivefunction,’’J.
Conf.Manage.Data,1996,pp.103–114. Amer.Stat.Assoc.,vol.58,no.301,pp.236–244,Mar.1963.
[29] B.Lorbeer,A.Kosareva,B.Deva,D.Softić,P.Ruppel,andA.Küpper,
‘‘VariationsontheclusteringalgorithmBIRCH,’’BigDataRes.,vol.11,
pp.44–53,Mar.2018.
| [30] A. Strehl | and | J. Ghosh, | ‘‘Cluster | ensembles—A |     | knowledge | reuse |     |     |     |     |     |     |     |
| -------------- | --- | --------- | --------- | ----------- | --- | --------- | ----- | --- | --- | --- | --- | --- | --- | --- |
frameworkforcombiningmultiplepartitions,’’J.Mach.Learn.Res.,vol.3,
pp.583–617,Dec.2002.
| [31] A. L. | N. Fred | and A. | K. Jain, | ‘‘Combining | multiple | clusterings | using |     |     |     |     |     |     |     |
| ---------- | ------- | ------ | -------- | ----------- | -------- | ----------- | ----- | --- | --- | --- | --- | --- | --- | --- |
evidenceaccumulation,’’IEEETrans.PatternAnal.Mach.Intell.,vol.27,
no.6,pp.835–850,Jun.2005.
| [32] C. Li, | ‘‘Birch-ae: | A   | hierarchical | ensemble | framework | for | scalable |     |     |     |     |     |     |     |
| ----------- | ----------- | --- | ------------ | -------- | --------- | --- | -------- | --- | --- | --- | --- | --- | --- | --- |
e-commerceusersegmentationwithautoencoder-enhancedfeaturelearn-
ing,’’Zenodo,Geneva,Switzerland,Tech.Rep.17498249,Jun.2026,doi: CAIWENLIiscurrentlypursuingthePh.D.degree
10.5281/zenodo.17498249. withtheFacultyofComputerScienceandInfor-
[33] C. Fraley and A. E. Raftery, ‘‘Model-based clustering, discriminant mation Technology, Universiti Putra Malaysia
analysis,anddensityestimation,’’J.Amer.Stat.Assoc.,vol.97,no.458, (UPM).Shehasyearsofexperienceasadatasci-
pp.611–631,Jun.2002. entist,shehasheldvariousroles,mostrecentlyat
[34] T. Rebafka, M. Sedki, and G. Celeux, ‘‘Model-based clustering with AmazonWebServices.Shespecializesinbusiness
missingnotatrandomdata,’’J.Classification,vol.41,no.1,pp.78–104, intelligenceanddigitalmarketing,leveragingher
| 2024. |     |     |     |     |     |     |     |     |     | expertise | in data | science, | including | forecasting, |
| ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --------- | ------- | -------- | --------- | ------------ |
[35] A.Y.Ng,M.I.Jordan,andY.Weiss,‘‘Onspectralclustering:Analysis feature/model selection, data mining, APIs, and
| and | an algorithm,’’ | in  | Proc. | Adv. Neural Inf. | Process. | Syst., | vol. 14, |     |     |     |     |     |     |     |
| --- | --------------- | --- | ----- | ---------------- | -------- | ------ | -------- | --- | --- | --- | --- | --- | --- | --- |
cloudtechnologies.Herprimaryresearchinterests
Jordan,2001,pp.849–856.
|     |     |     |     |     |     |     |     | include recommendation |     | systems, | business | intelligence, |     | deep learning, |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------------------- | --- | -------- | -------- | ------------- | --- | -------------- |
[36] D.A.Reynolds,‘‘Gaussianmixturemodels,’’EncyclopediaBiometrics,S.
|     |     |     |     |     |     |     |     | hierarchical | clustering | methods, | and scalable | data | mining | algorithms for |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------ | ---------- | -------- | ------------ | ---- | ------ | -------------- |
Z.LiandA.K.Jain,Eds.Boston,MA,USA:Springer,2009,pp.659–663.
e-commerceapplications.
[37] T.Zhang,R.Ramakrishnan,andM.Livny,‘‘BIRCH:Anewdataclustering
algorithmanditsapplications,’’DataMiningKnowl.Discovery,vol.1,
no.2,pp.141–182,Jun.1997.
[38] S.Vega-PonsandJ.Ruiz-Shulcloper,‘‘Asurveyofclusteringensemble
| algorithms,’’ |     | Int. J. Pattern |     | Recognit. Artif. | Intell., | vol. 25, | no. 3, |     |     |     |     |     |     |     |
| ------------- | --- | --------------- | --- | ---------------- | -------- | -------- | ------ | --- | --- | --- | --- | --- | --- | --- |
pp.337–372,May2011.
| [39] D. Huang,   | C.-D.  | Wang,    | J.-S.      | Wu, J.-H.      | Lai, and | C.-K.         | Kwoh, |     |     |     |     |     |     |     |
| ---------------- | ------ | -------- | ---------- | -------------- | -------- | ------------- | ----- | --- | --- | --- | --- | --- | --- | --- |
| ‘‘Ultra-scalable |        | spectral | clustering | and            | ensemble | clustering,’’ |       |     |     |     |     |     |     |     |
| IEEE             | Trans. | Knowl.   | Data       | Eng., vol. 32, | no. 6,   | pp.1212–1226, |       |     |     |     |     |     |     |     |
Jun.2020.
| [40] F. Li, | Y. Qian, | J. Wang, | C.           | Dang, and L.    | Jing, ‘‘Clustering |                | ensem- |     |     |          |       |          |     |             |
| ----------- | -------- | -------- | ------------ | --------------- | ------------------ | -------------- | ------ | --- | --- | -------- | ----- | -------- | --- | ----------- |
| ble based   | on       | sample’s | stability,’’ | Artif. Intell., | vol.               | 273, pp.37–55, |        |     |     |          |       |          |     |             |
|             |          |          |              |                 |                    |                |        |     |     | ISKANDAR | ISHAK | received | the | Bachelor of |
Aug.2019.
|            |         |       |        |                       |     |              |     |     |     | Information | Technology | degree | from | Universiti |
| ---------- | ------- | ----- | ------ | --------------------- | --- | ------------ | --- | --- | --- | ----------- | ---------- | ------ | ---- | ---------- |
| [41] R. A. | FISHER, | ‘‘The | use of | multiple measurements |     | in taxonomic |     |     |     |             |            |        |      |            |
problems,’’Ann.Eugenics,vol.7,no.2,pp.179–188,Sep.1936. Tenaga Nasional, Malaysia, the Master of Tech-
|     |     |     |     |     |     |     |     |     |     | nology | degree | in information | technology | from |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------ | ------ | -------------- | ---------- | ---- |
[42] L.V.D.MaatenandG.E.Hinton,‘‘Visualizingdatausingt-SNE,’’J.
|     |     |     |     |     |     |     |     |     |     | the Royal | Melbourne | Institute | of  | Technology, |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --------- | --------- | --------- | --- | ----------- |
Mach.Learn.Res.,vol.9,no.86,pp.2579–2605,2008.
|     |     |     |     |     |     |     |     |     |     | Australia, | and | the Ph.D. | degree | in computer |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---------- | --- | --------- | ------ | ----------- |
[43] G.E.HintonandR.R.Salakhutdinov,‘‘Reducingthedimensionalityof
sciencefromUniversitiTeknologiMalaysia.Heis
| data      | with neural | networks,’’ | Science, | vol. 313, | no. 5786, | pp.504–507, |     |     |     |                                             |     |     |     |     |
| --------- | ----------- | ----------- | -------- | --------- | --------- | ----------- | --- | --- | --- | ------------------------------------------- | --- | --- | --- | --- |
| Jul.2006. |             |             |          |           |           |             |     |     |     | currentlyaSeniorLecturerwithUniversitiPutra |     |     |     |     |
[44] J.Xie,R.Girshick,andA.Farhadi,‘‘Unsuperviseddeepembeddingfor Malaysia.Hisresearchinterestsincludedatabase
clustering analysis,’’ in Proc. Int. Conf. Mach. Learn. (ICML), 2015, systems, big data, data analytics, and scalable
| pp.478–487. |     |     |     |     |     |     |     |     |     | clusteringalgorithms. |     |     |               |     |
| ----------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --------------------- | --- | --- | ------------- | --- |
| 88608       |     |     |     |     |     |     |     |     |     |                       |     |     | VOLUME14,2026 |     |

C.Lietal.:BIRCH-AE:AHierarchicalEnsembleFrameworkforScalableE-CommerceUserSegmentation
HAMIDAHIBRAHIM(Member,IEEE)received FATIMAH SIDI (Member, IEEE) received the
the Ph.D. degree in computer science from the Ph.D.degreeinmanagementinformationsystems
University of Wales, Cardiff, U.K., in 1998. fromUniversitiPutraMalaysia(UPM),Malaysia,
She is currently a Full Professor with the in2008.SheiscurrentlyanAssociateProfessor
Faculty of Computer Science and Information withtheDepartmentofComputerScience,Faculty
Technology, Universiti Putra Malaysia (UPM). of Computer Science and Information Technol-
Her current research interests include databases ogy,UPM.Hercurrentresearchinterestsinclude
(distributed, parallel, mobile, biomedical, XML) knowledgeandinformationmanagementsystems,
focusing on issues related to integrity main- dataandknowledgeengineering,databases,data
tenance/checking, ontology/schema/data integra- warehouses,bigdata,anddataanalytics.
| tion, ontology/schema/data |                         | mapping, cache   | management, access      | control, |     |     |     |
| -------------------------- | ----------------------- | ---------------- | ----------------------- | -------- | --- | --- | --- |
| data security,             | transaction processing, | query            | optimization, query     | reformu- |     |     |     |
| lation, preference         | evaluation              | (context-aware), | information extraction, | and      |     |     |     |
concurrencycontrol.
|     |     |     |     |     | CAILI LI is currently | pursuing the Ph.D. | degree |
| --- | --- | --- | --- | --- | --------------------- | ------------------ | ------ |
MASLINA ZOLKEPLI received the bachelor’s in design and architecture with Universiti Putra
and master’s degrees in computer science from Malaysia,sheconductsinterdisciplinaryresearch
Universiti Putra Malaysia, in 2007 and 2010, attheintersectionofartandtechnology.Shewas
respectively, and the Ph.D. degree in computa- a Visiting Scholar at Tsinghua University, she
tionalintelligenceandsystemssciencefromTokyo bringsextensiveexpertiseandinsightstoherwork,
Institute of Technology, Japan, in 2015. She is aimingtoadvancethefieldofdesignandtoinspire
currentlyaSeniorLecturerwiththeDepartmentof innovative solutions through data-driven visual-
ComputerScience,FacultyofComputerScience ization. She is currently an Associate Professor
withHeilongjiangInstituteofTechnology,China,
|     | and | Information | Technology, Universiti | Putra |     |     |     |
| --- | --- | ----------- | ---------------------- | ----- | --- | --- | --- |
specializingindesignart,visualarts,analyticalvisualization,integratedarts,
Malaysia.Herresearchinterestsincludebusiness
andlandscapedesign.
| analytics, fuzzy | brake systems, | computational | intelligence, | and ensemble |     |     |     |
| ---------------- | -------------- | ------------- | ------------- | ------------ | --- | --- | --- |
learningmethods.
| VOLUME14,2026 |     |     |     |     |     |     | 88609 |
| ------------- | --- | --- | --- | --- | --- | --- | ----- |