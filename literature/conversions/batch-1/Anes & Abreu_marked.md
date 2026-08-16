---
conversion_metadata:
  converted_at: "2026-07-22T11:57:10Z"
  converter_tool: "markitdown"
  converter_version: "0.1.6"
  source_pdf: "Anes & Abreu.pdf"
  source_pdf_sha256: "6cf9d628d50ee439a48b651c0f39ccb07de0c2caa9854540434b2b8bca38fc50"
  page_count: 21
  markdown_char_count: 146589
---

<!-- PAGE-AWARE EXTRACTION (via pdfminer.six) -->

<!-- PAGE 1 -->

Article
Adaptive Cluster-Based Normalization for Robust TOPSIS in
Multicriteria Decision-Making

Vitor Anes 1,2,*

and António Abreu 2,3

1

IDMEC, Instituto Superior de Engenharia de Lisboa, Instituto Politécnico de Lisboa, 1959-007 Lisbon, Portugal
2 Unit for Innovation and Research in Engineering, Polytechnic University of Lisbon, 1959-007 Lisbon, Portugal;

antonio.abreu@isel.pt

3 Center of Technology and Systems (UNINOVA-CTS), Associated Lab of Intelligent Systems (LASI),

2829-516 Caparica, Portugal

* Correspondence: vitor.anes@isel.pt

Abstract: In multicriteria decision-making (MCDM), methods such as TOPSIS are essential
for evaluating and comparing alternatives across multiple criteria. However, traditional
normalization techniques often struggle with datasets containing outliers, large variances,
or heterogeneous measurement units, which can lead to skewed or biased rankings. To
address these challenges, this paper proposes an adaptive, cluster-based normalization
approach, demonstrated through a real-world logistics case study involving the selection
of a host city for an international event. The method groups alternatives into clusters
based on similarities in criterion values and applies logarithmic normalization within each
cluster. This localized strategy reduces the influence of outliers and ensures that scaling
adjustments reflect the specific characteristics of each group. In the case study—where cities
were evaluated based on cost, infrastructure, safety, and accessibility—the cluster-based
normalization method yielded more stable and balanced rankings, even in the presence
of significant data variability. By reducing the influence of outliers through logarithmic
normalization and allowing predefined cluster profiles to reflect expert judgment, the
method improves fairness and adaptability. These features strengthen TOPSIS’s ability to
deliver accurate, balanced, and context-aware decisions in complex, real-world scenarios.

Keywords: TOPSIS; logarithmic normalization; cluster-based normalization; multicriteria
decision-making; outlier mitigation

1. Introduction

Multi-criteria decision-making (MCDM) methods are essential for addressing complex
problems that involve multiple, often conflicting, factors. Among these, the Technique for
Order of Preference by Similarity to Ideal Solution (TOPSIS) is widely used due to its ability
to effectively rank alternatives based on their closeness to an ideal solution.

Clustering techniques are increasingly relevant in TOPSIS-based applications because
they enable decision-makers to group alternatives with similar characteristics before per-
forming the ranking procedure. This segmentation enhances the interpretability of results
and allows for more context-sensitive comparisons. Rather than applying a one-size-fits-all
ranking across a diverse set of alternatives, clustering allows each group to be evaluated
against a tailored ideal profile, reflecting specific priorities or constraints. In this way,
clustering not only increases adaptability to real-world scenarios but also improves the
fairness and clarity of the final rankings.

Academic Editor: Yiming Tang

Received: 12 February 2025

Revised: 26 March 2025

Accepted: 2 April 2025

Published: 7 April 2025

Citation: Anes, V.; Abreu, A.

Adaptive Cluster-Based

Normalization for Robust TOPSIS in

Multicriteria Decision-Making. Appl.

Sci. 2025, 15, 4044. https://doi.org/

10.3390/app15074044

Copyright: © 2025 by the authors.

Licensee MDPI, Basel, Switzerland.

This article is an open access article

distributed under the terms and

conditions of the Creative Commons

Attribution (CC BY) license

(https://creativecommons.org/

licenses/by/4.0/).

Appl. Sci. 2025, 15, 4044

https://doi.org/10.3390/app15074044

---

<!-- PAGE 2 -->

Appl. Sci. 2025, 15, 4044

2 of 21

However, despite its advantages, certain challenges remain—particularly related to
clustering and normalization. Traditional clustering methods tend to assign alternatives
to fixed categories, even when those alternatives share features with multiple groups.
This rigid classification can lead to misinterpretation and the loss of valuable information,
especially when the data involves uncertainty or overlapping characteristics. Likewise,
widely used normalization techniques—such as Min–Max and Z-score—often struggle to
manage large data variations, skewed distributions, and extreme values, which can distort
rankings and introduce bias into decision-making.

To overcome these limitations, this study proposes two innovative methods designed
to make the TOPSIS framework more flexible, reliable, and user-friendly. The first is Clus-
tering Using Fuzzy Numbers and Centroid-Based Distance Allocation, a novel clustering
approach that incorporates fuzzy numbers to represent uncertainty in the evaluation of
alternatives. Unlike traditional clustering methods such as K-Means—where cluster cen-
troids are determined based on the data of existing elements—our approach defines the
centroid of each cluster a priori, based on expert judgment and ideal conditions for each
criterion. Alternatives are then evaluated using fuzzy numbers to account for uncertainty,
and their distances to the predefined cluster centroids are computed using crisp values
derived from these fuzzy assessments. This process avoids arbitrary assignments and
provides a more structured, interpretable classification framework that reflects both expert
intent and the inherent imprecision of real-world data.

The second innovation is logarithmic normalization in TOPSIS, a transformation tech-
nique that smooths extreme variations, preserves proportional differences, and prevents
any single criterion from dominating the final rankings. A key benefit of this technique is
that, while it enhances stability and accuracy, it remains as straightforward to apply as tradi-
tional methods like Min–Max or Z-score normalization, making it a practical enhancement
for decision-makers.

By integrating these two methodological advancements, this study improves both
the clustering and normalization components of the TOPSIS framework, addressing key
limitations in traditional approaches while maintaining simplicity and efficiency.

Unlike traditional data-driven clustering algorithms, the proposed method allows
decision-makers to define ideal cluster profiles independently of the dataset. This design,
combined with the use of fuzzy numbers to capture evaluation uncertainty, enables a simple
yet robust classification process. The deterministic assignment of alternatives enhances
transparency and interpretability, making the approach both innovative and well-suited
for real-world decision-making.

Designed for both ease of implementation and adaptability, the method is applicable
across a wide range of domains, including finance, environmental assessment, and indus-
trial planning. By improving the grouping of alternatives and enabling fairer comparisons
between criteria, the proposed approach offers a more balanced, insightful, and scalable
solution for complex decision-making problems.

The following sections provide a detailed explanation of the proposed methods, their

theoretical underpinnings, and their practical implementation.

The rest of this paper is organized as follows: Section 2 reviews the existing literature
on clustering and normalization in TOPSIS, highlighting their strengths and limitations
and identifying the gaps that this study aims to address. Section 3 outlines the Materials
and Methods, providing a detailed explanation of the proposed Clustering Using Fuzzy
Numbers and Centroid-Based Distance Allocation approach, as well as the logarithmic
normalization for TOPSIS, along with their theoretical foundations and implementation
process. Section 4 presents a case study, demonstrating how these methods can be applied
in a real-world decision-making scenario. Section 5 analyzes the results, comparing the

---

<!-- PAGE 3 -->

Appl. Sci. 2025, 15, 4044

3 of 21

proposed techniques with traditional methods to evaluate improvements in accuracy,
robustness, and efficiency. Finally, Section 6 offers the conclusion, summarizing the key
findings, discussing their broader implications, and suggesting possible directions for
future research.

2. Literature Review

Multi-criteria decision-making (MCDM) encompasses a set of methodologies used to
evaluate and prioritize multiple—often conflicting—factors in the decision-making process.
These approaches are critical in fields such as environmental management, engineering,
and economics, where complex decisions are frequently encountered [1].

One of the most widely applied MCDM techniques is the Technique for Order of
Preference by Similarity to Ideal Solution (TOPSIS). Its core principle is straightforward: the
optimal alternative is the one closest to the ideal solution and farthest from the worst-case
scenario. TOPSIS is particularly valued for its simplicity and its ability to effectively handle
both qualitative and quantitative data [2].

Like any method, however, TOPSIS has its limitations. It can struggle with datasets
characterized by uncertainty, outliers, or high variance, which may affect the consistency
and reliability of its rankings. In response, researchers have explored methods to link
input uncertainty with output uncertainty within the TOPSIS framework, highlighting the
challenges of interpreting uncertain data in real-world decision-making contexts [3].

Refining these techniques can increase decision-makers’ confidence in the results,
thereby enhancing the overall value and applicability of MCDM methods across various
industries [4].

Comparative studies have examined TOPSIS alongside other MCDM methods such
as VIKOR, PROMETHEE, and AHP. For instance, one study evaluated four different
techniques—AHP, TOPSIS, ELECTRE III, and PROMETHEE II—in the context of group
decision-making for sewer network projects, offering valuable insights into their applicabil-
ity and effectiveness [5–7].

Traditional clustering methods—such as K-Means and Hierarchical Clustering—have
long served as fundamental tools for grouping similar data points in decision-making
models. Their efficiency and ease of implementation contribute to their widespread use.
However, these methods have notable limitations, especially when dealing with uncertainty,
complex data distributions, or overlapping classifications. Because they rely on crisp
boundaries, each data point is strictly assigned to a single cluster, which can result in
inaccurate or overly simplistic groupings in real-world scenarios where data are often
ambiguous and multidimensional [8].

To overcome these limitations, fuzzy clustering techniques—particularly Fuzzy C-
Means (FCM)—offer a more flexible alternative. Unlike traditional clustering methods,
FCM allows data points to belong to multiple clusters with varying degrees of membership,
enabling more nuanced and adaptable classifications. This approach is especially valuable
in domains such as medical diagnosis, image segmentation, and customer profiling, where
real-world data rarely conforms to clearly defined categories [9].

Although FCM enhances clustering accuracy and adaptability, it also introduces
considerable computational complexity. In contrast to K-Means, which follows a relatively
simple iterative process, FCM requires more intensive calculations due to the continuous
updating of membership probabilities and the optimization of an objective function. This
iterative minimization process can become computationally expensive, particularly when
working with large, high-dimensional datasets. As a result, FCM increases processing time
and demands greater computational resources [10].

---

<!-- PAGE 4 -->

Appl. Sci. 2025, 15, 4044

4 of 21

Another significant barrier to the adoption of fuzzy clustering methods is the need for
programming and algorithmic expertise. Implementing these methods—particularly in
large-scale applications—requires familiarity with programming languages such as Python
v3, R v4, or MATLAB R2024a, as well as with specialized libraries like scikit-fuzzy or the
Fuzzy Logic Toolbox. Unlike traditional clustering algorithms, which are often accessible
through built-in software tools with minimal coding, FCM and similar approaches demand
manual parameter tuning (e.g., selecting the optimal fuzziness coefficient m) and careful
data preprocessing to produce meaningful results [11].

Additionally, FCM is highly sensitive to initialization—poorly selected initial centroids
can lead to suboptimal clustering outcomes, often requiring advanced techniques such as
genetic algorithms or particle swarm optimization to enhance results. Consequently, while
fuzzy clustering offers improved accuracy and flexibility, its practical application demands
greater expertise, computational resources, and algorithmic fine-tuning [12].

Recent research has focused on reducing the computational overhead associated with
fuzzy clustering by exploring hybrid models that combine deep learning and optimization
algorithms. These models aim to automate parameter selection and improve overall
performance. Such advances seek to make fuzzy clustering more accessible and scalable,
bridging the gap between its theoretical strengths and practical usability in complex, real-
world decision-making scenarios [13].

Normalization is a critical step in multi-criteria decision-making (MCDM) processes,
as it ensures that criteria measured on different scales can be compared meaningfully [14].
Common normalization methods include Min–Max normalization: This method
rescales data to a fixed range, typically [0, 1], but is sensitive to outliers, which can distort
the normalized values. Z-Score normalization: This technique standardizes data based on
mean and standard deviation, assuming a normal distribution, which may not hold true
for all datasets. Vector normalization: Often used in TOPSIS, this method normalizes data
by dividing each criterion value by the Euclidean norm of the vector. While effective, it
may not always preserve proportional differences between criteria.

These conventional normalization techniques face challenges when applied to highly
skewed data, extreme values, or non-linear distributions, which can compromise the fair-
ness and accuracy of decision-making outcomes. For example, the choice of normalization
method can significantly influence the ranking of alternatives in MCDM processes, un-
derscoring the importance of selecting an appropriate technique for each specific decision
context [15,16].

Logarithmic transformation is a mathematical technique used to handle non-linear
data and compress large numerical ranges. By applying a logarithmic function, data
can be transformed to reduce skewness, manage outliers, and stabilize variance. This
transformation preserves relative differences while minimizing the influence of extreme
values, making it useful in fields such as statistics, finance, and machine learning. Despite
these advantages, logarithmic normalization remains underutilized in MCDM methods
like TOPSIS. Integrating it into the TOPSIS framework could improve ranking stability
and decision accuracy—especially in datasets characterized by high variance [17]. One
study introduced a novel logarithmic normalization method within the context of game
theory, demonstrating its effectiveness in separating normalized values more efficiently
than conventional approaches. These findings suggest promising applications for such a
method in MCDM frameworks as well [18].

The current literature reveals a lack of studies that combine fuzzy clustering with
centroid-based distance allocation within MCDM frameworks [19,20]. Furthermore, al-
though logarithmic normalization offers clear advantages for handling high-variance data,
its application within TOPSIS and other MCDM models remains limited [21].

---

<!-- PAGE 5 -->

Appl. Sci. 2025, 15, 4044

5 of 21

Addressing these gaps presents an opportunity to improve decision-making processes
by developing a unified framework that integrates both techniques, thereby enhancing
clustering precision and ranking accuracy within MCDM applications [22].

Recent studies have also explored the integration of MCDM methods with uncertainty
modeling in emerging technological contexts. For instance, Nabeeh et al. [23] proposed
a hybrid model combining the Ordered Weighted Averaging (OWA) operator with the
TOPSIS method to evaluate key factors influencing the production of digital twins based on
blockchain technology. Their approach leverages neutrosophic logic to manage uncertainty
in expert judgments, offering a structured yet flexible decision-making framework. While
the application domain differs from the present study, both approaches share a common
goal: enhancing the reliability of TOPSIS in uncertain, multi-criteria environments. In
contrast to neutrosophic sets, our method uses fuzzy numbers exclusively to express
uncertainty during the evaluation phase, followed by crisp classification based on distance
to predefined ideal centroids. This allows for improved interpretability and computational
simplicity while maintaining robustness in decision support.

Beyond the MCDM- and TOPSIS-focused research reviewed here, advanced studies
in optimization, machine learning, and statistical modeling may inspire novel extensions
to fuzzy clustering and logarithmic normalization approaches. Recent works on meta-
learning for nonconvex optimization [24], few-shot identification for stochastic dynamical
systems [25], robust kernel-based surrogate modeling [26], and Gaussian kernel similar-
ity for multisource information fusion [27] illustrate how sophisticated algorithms can
handle high-dimensional, uncertain data. Related efforts address robust statistical tests
for heavy-tailed time series [28], supervised learning for complex tracking [29], adaptive
opinion dynamics [30], and agent-based decision models leveraging deep reinforcement
learning [31].

Although these advanced methods offer impressive capabilities, they often come with
increased computational complexity and demand a high level of technical expertise for
effective implementation. In contrast, our goal is to propose a more straightforward and
practical approach, suitable for real-world scenarios, that balances the need to address data
variability and uncertainty with simplicity and usability. Nonetheless, these sophisticated
techniques highlight promising directions for future MCDM research, particularly in the
integration of meta-learning, robust modeling, and adaptive information fusion to further
improve clustering and normalization strategies in complex decision-making contexts.

3. Materials and Methods

In this section, we introduce a new methodological approach that enhances both
clustering and normalization within the TOPSIS framework while ensuring that the process
remains straightforward and easy to implement. The proposed methods, Clustering Using
Fuzzy Numbers and Centroid-Based Distance Allocation, and the integration of logarithmic
normalization in TOPSIS, address key limitations in traditional techniques. By introducing
a more flexible clustering process and an adaptive normalization approach, these methods
allow for a more accurate representation of real-world data variability, improving decision-
making outcomes.

One of the fundamental challenges in decision models is that traditional clustering
methods tend to assign alternatives to rigid categories, even when the data suggests a more
nuanced classification. This can lead to misinterpretations, particularly when dealing with
uncertainty or overlapping data points. To overcome this limitation, we propose Clustering
Using Fuzzy Numbers and Centroid-Based Distance Allocation, which introduces a degree
of membership for each alternative within a cluster instead of enforcing a strict assignment.

---

<!-- PAGE 6 -->

Appl. Sci. 2025, 15, 4044

6 of 21

This method acknowledges that alternatives may exhibit characteristics of multiple clusters,
leading to a more precise, meaningful, and interpretable grouping of data.

Similarly, conventional normalization techniques such as Min–Max and Z-score often
fail to handle datasets with large numerical variations, highly skewed distributions, or
extreme outliers. These issues can distort rankings in TOPSIS, as criteria with significantly
larger values may disproportionately influence the final results. To address this, we propose
the integration of logarithmic normalization in TOPSIS, which effectively smooths extreme
variations, preserves relative differences, and ensures a more balanced influence across
criteria. One of its most compelling advantages is that, despite its effectiveness in handling
complex data distributions, it remains as easy to apply as traditional normalization methods,
making it an accessible yet powerful enhancement for decision-makers.

The strength of our proposed methodology lies in its ability to enhance accuracy,
robustness, and adaptability while maintaining ease of implementation. Both the fuzzy
clustering approach and logarithmic normalization are designed to seamlessly integrate
into existing decision-making workflows without adding computational complexity. By
introducing greater flexibility in clustering and a more adaptive approach to normalization,
this study provides a scalable, practical, and efficient framework for improving multi-
criteria decision-making. The following sections provide an in-depth explanation of how
these methods work and their practical applications.

3.1. Clustering Using Fuzzy Numbers and Centroid-Based Distance Allocation

To group alternatives into meaningful clusters, we implement a fuzzy clustering

approach. This method involves the following steps:

Step 1: Representation of alternatives with fuzzy numbers—each alternative’s criteria’s
values are converted into fuzzy numbers (a, b, c) representing the lower bound, central
value, and upper bound, respectively. This allows for a more flexible representation of
uncertainty in the decision-making process.

Step 2: In this step, the cluster centroids are determined qualitatively by the user,
identifying the optimal ranking for each criterion within the cluster. This process employs
fuzzy numbers, represented as values (a, b, c) ranging between 0 and 1. These results will
allow us to measure the distance between the cluster centroids, which represent the ideal
position for each cluster based on the selected criteria—and the scores of each alternative.
Beyond this primary purpose, the resulting centroids are also used to determine the criterion
weights, which will later be applied in the TOPSIS method. Formula (1) calculates the
centroid representing the optimal position within a given cluster.

Ccwj =

(cid:18) aw + bw + cw
3

(cid:19)

,

j

(1)

where aw, bw, cw are the fuzzy number components representing the optimal position within
a given cluster j.

Step 3: Determination of alternative centroids—using a fuzzy clustering approach,
the centroids of each alternative are determined. The centroid CAij for each alternative i is
computed as follows:

CAij =

(cid:18) ai + bi + ci
3

(cid:19)

,

j

(2)

where ai, bi, ci are the fuzzy number components of alternative i in the criterion j.

This formula is applied to all alternatives across all considered criteria to establish the

ranking of the alternatives.

Equations (1) and (2) define two distinct types of centroids within the proposed
method: cluster centroids and alternative centroids. The cluster centroid represents the ideal

---

<!-- PAGE 7 -->

Appl. Sci. 2025, 15, 4044

7 of 21

position of a given cluster across all criteria and is computed based on predefined fuzzy
values that characterize the cluster’s optimal conditions. This centroid remains fixed for all
alternatives within the cluster, serving as a reference point for comparison. In contrast, the
alternative centroid is calculated based on the fuzzy scores assigned to a specific alternative,
meaning it varies from one alternative to another. While the cluster centroid reflects the
overall profile of a group, the alternative centroid captures the individual positioning of an
alternative within the decision space. This distinction is crucial for the clustering process,
as it enables a more flexible classification of alternatives while maintaining a structured
evaluation framework.

Step 4: The new decision matrix, obtained from Step 3, is normalized using the cost

(lower is better) and benefit (higher is better) formulas (Formulas (2) and (3)).

Ni =

max(X) − Xi
max(X) − min(X)

Ni =

Xi − max(X)
max(X) − min(X)

,

,

(3)

(4)

where Ni is the normalized value of the alternative i, Xi is the original value of the alterna-
tive i, max(X) is the maximum value in the criterion, and min(X) is the minimum value in
the criterion. These formulas scale the values between 0 and 1, ensuring a fair comparison
between alternatives while maintaining the meaning of cost and benefit criteria.

Step 5: Calculation of distance to cluster centroids—the distance between each alter-
native centroid (CAlternative) in each criterion j, and each cluster centroid (CCluster) in each
criterion j, is calculated using the Euclidean distance formula as follows:

Diw =

(cid:118)
(cid:117)
(cid:117)
(cid:116)

(cid:16)

m
∑
j=1

CAlternative

ij

− CCluster
wj

(cid:17)2

,

(5)

where Diw represents the distance between the centroid of alternative i and the centroid of
the optimal position within cluster w, and m denotes the number of criteria considered in
the MCDM problem under analysis.

Step 4: Assignment of alternatives to clusters—each alternative is assigned to the
cluster with the smallest distance to its centroid. This process involves calculating the
distance between each alternative and all cluster centroids. The alternative is then assigned
to the cluster with the nearest centroid, ensuring it is grouped with the most similar
alternatives as defined in Formula (6).

Ci = argmin
w

Diw,

(6)

where Ci is the cluster assigned to alternative i and argmin
minimizes the distance.

w

selects the cluster w that

3.2. Logarithmic Normalization: An Adaptive Approach for TOPSIS

Normalization is a fundamental step in multi-criteria decision-making (MCDM) meth-
ods such as TOPSIS (Technique for Order of Preference by Similarity to Ideal Solution). It
ensures that criteria with different units and scales can be meaningfully compared. Tra-
ditional normalization methods, such as Min–Max and Z-score, effectively rescale data
but may not be suitable for datasets with high variance, extreme outliers, or non-linear
distributions. In such cases, logarithmic normalization emerges as an alternative technique
that dynamically adjusts to data distributions, making it particularly effective for handling
data spanning multiple orders of magnitude. By compressing large numerical variations

---

<!-- PAGE 8 -->

Appl. Sci. 2025, 15, 4044

8 of 21

while amplifying smaller differences, this approach ensures a more balanced contribu-
tion of criteria to the final decision, preserving the relative ranking among alternatives.
Logarithmic normalization is mathematically expressed as shown in Equation (7),

X =

log(X) − log(Xmin)
log(Xmax) − log(Xmin)

,

(7)

where X represents the normalized value, X is the original value, and Xmin and Xmax
denote the minimum and maximum values within a given criterion. This transformation is
particularly beneficial in decision-making scenarios where some criteria exhibit exponential
growth patterns, such as financial metrics, environmental indicators, and energy consump-
tion data. By using a logarithmic scale, the influence of extreme values is harmonized,
ensuring that all criteria contribute meaningfully to the decision-making process in TOPSIS,
for instance. A key strength of logarithmic normalization is its adaptive nature. Unlike
fixed range methods, it automatically adjusts to varying data magnitudes, dynamically
scaling values to ensure fair comparisons across criteria. This makes it particularly effective
for datasets with highly skewed distributions or large numerical differences. Moreover,
it enhances decision stability, reducing the dominance of criteria with disproportionately
large values while ensuring that smaller values remain distinguishable. Another advantage
of logarithmic normalization is its ability to enhance differentiation among alternatives.
By redistributing values in a way that emphasizes proportional differences, it ensures that
the ranking process in TOPSIS remains representative and reliable, even when dealing
with highly dispersed datasets. This is particularly beneficial in cases where criteria ex-
hibit non-linear relationships, allowing for a more accurate reflection of each alternative’s
performance. The implications of logarithmic normalization in TOPSIS are significant. By
integrating this approach, rankings become more stable and reflective of real-world condi-
tions, ensuring that decision-making processes remain robust and interpretable. Given its
ability to balance differences across criteria without distorting rankings, logarithmic normal-
ization offers an advanced scaling technique that aligns well with diverse decision-making
scenarios. Despite its many advantages, logarithmic normalization has yet to be widely
integrated into the TOPSIS framework, presenting an exciting opportunity for innovation.
By introducing this approach, we can create a more adaptive way of handling criteria with
high variance, non-linear distributions, and sensitivity to outliers. This integration helps
improve ranking stability, ensures fairer comparisons between alternatives, and strengthens
the overall decision-making process. What makes logarithmic normalization even more
appealing is its ease of implementation. While it effectively balances data distribution and
minimizes the impact of extreme values, it remains just as simple to apply as Min–Max or
Z-score normalization. This means that decision-makers can benefit from its advantages
without facing additional computational complexity or implementation challenges.

To further clarify the proposed method, Figure 1 provides a step-by-step flowchart
illustrating the transformation of raw data into fuzzy values, the application of fuzzy
clustering, and the final logarithmic normalization.

The proposed method introduces several methodological innovations that enhance
the flexibility, interpretability, and robustness of the TOPSIS framework. First, instead
of relying on data-driven clustering techniques, the approach uses expert-defined ideal
cluster profiles (step 4), represented through fuzzy numbers, allowing for context-aware
classification of alternatives. Second, alternatives are assigned to clusters based on their
Euclidean distance to these ideal profiles, enabling a deterministic and transparent grouping
process (steps 7 and 8). Third, logarithmic normalization is applied within each cluster to
reduce the influence of outliers and large variances, improving the stability and fairness of
the rankings (step 9). Finally, the method derives the weights of criteria directly from the

---

<!-- PAGE 9 -->

Appl. Sci. 2025, 15, 4044

9 of 21

ideal cluster centroids, eliminating the need for subjective or complex weighting procedures
(step 10). Together, these innovations offer a practical and scalable solution for multi-criteria
decision-making in real-world scenarios involving uncertainty and heterogeneous data.

Figure 1. Overview of the proposed decision-making workflow, combining fuzzy evaluation, cluster
assignment, and logarithmic normalization within the TOPSIS framework. The dashed outline boxes
represent the contributions of the proposed methodology.

4. Case Study

This case study focuses on selecting the most suitable city to host an international event
scheduled to take place in two years. The decision is complex, involving the evaluation
of key factors such as costs, logistics, attendee experience, and overall event impact. To
facilitate the process, a dataset of potential host cities was analyzed and grouped into
clusters based on economic characteristics, infrastructure quality, safety, and accessibility.
Table 1 presents an overview of the cities, each identified by a letter for clarity. These
cities were thoroughly assessed, with descriptions highlighting their individual strengths
and challenges. This structured approach provides valuable insights, supporting decision-
makers in identifying the best location to ensure the event’s success. In total, 12 cities were
evaluated using four criteria: cost, infrastructure, safety, and accessibility. These alternatives
were selected to reflect a realistic shortlisting scenario, where decision-makers typically
narrow down options based on preliminary screening. While the dataset is moderate in
size, it captures a diverse range of urban profiles and geographic contexts. The structure of
the data—organized as fuzzy evaluations per criterion—allows for nuanced analysis and
robust comparison across alternatives.

The cities were evaluated based on the following four key criteria, each playing a

crucial role in determining their suitability to host the international event:

1.

Cost (C1): The estimated total expense of hosting the event, measured in millions of
dollars. This criterion reflects the financial feasibility of each city and its potential
impact on the event’s budget.

---

<!-- PAGE 10 -->

Appl. Sci. 2025, 15, 4044

10 of 21

2.

3.

Infrastructure (C2): A score from 1 to 10 that represents the quality of venues, trans-
portation systems, accommodations, and other facilities required to host a large-scale
international event.
Safety (C3): An index (1 to 10) measuring overall safety in the city, including crime
rates, political stability, and emergency preparedness. A higher score indicates a safer
environment for attendees.

4. Accessibility (C4): A score from 1 to 10 reflecting the city’s connectivity and ease of
access, including international/domestic flight availability, public transit, and road
infrastructure.

Table 1. Potential cities for selection as hosts of an international event.

City (Letter)

City

Description

City A

Hanoi, Vietnam

City B

Kathmandu, Nepal

City C

City D

City E

Tokyo, Japan

Singapore, Singapore
Kuala Lumpur,
Malaysia

City F

Bangkok, Thailand

City G

Colombo, Sri Lanka

City H

Manila, Philippines

City I

City J

City K

Seoul, South Korea

Hong Kong, China

Ho Chi Minh City,
Vietnam

City L

Jakarta, Indonesia

Low-cost city with functional infrastructure, ideal
for regional events.
Highly affordable but with limited infrastructure
and moderate safety.
Exceptional infrastructure, safety, and accessibility;
high-cost city.
Similar quality to Tokyo with slightly lower costs.
Balanced city with high safety, accessibility, and
moderate costs.
More affordable than Kuala Lumpur, with slightly
lower safety scores.
Affordable with growing infrastructure and
moderate accessibility.
Slightly higher cost with challenges in infrastructure
and safety.
High safety and good infrastructure, though slightly
less accessible.
Highly accessible and secure, with costs similar
to Tokyo.
Good safety and accessibility, with moderately
higher costs.
High accessibility and safety with balanced,
moderate costs.

To streamline the decision-making process, the cities under consideration were
grouped into three clusters based on shared characteristics, including cost, infrastruc-
ture, safety, and accessibility. Each cluster represents a distinct category of cities, enabling
decision-makers to narrow their focus and evaluate alternatives more effectively as follows:

1.

Cluster 1: Cost-Effective Cities with Moderate Infrastructure. This cluster consists
of budget-friendly cities, making them attractive options for events with tighter
financial constraints. Their lower costs allow organizers to allocate resources to other
areas, such as marketing or improving the attendee experience. These cities may also
attract higher attendance from local or regional participants due to their affordability.
However, they present certain challenges. Infrastructure may require temporary
enhancements to meet the needs of an international audience, and their safety and
accessibility scores are generally moderate—requiring careful planning to ensure a
successful event.

In the following, the values presented for each criterion are analyzed and discussed
using fuzzy numbers, which represent the optimal values for each criterion within this
cluster. These fuzzy values indicate the most desirable levels for cost, infrastructure,
safety, and accessibility, providing a degree of flexibility rather than rigid, fixed values.
By applying fuzzy logic, this approach acknowledges that real-world city classifications

---

<!-- PAGE 11 -->

Appl. Sci. 2025, 15, 4044

11 of 21

involve gradual transitions rather than strict categorizations, allowing for a more nuanced
and adaptable evaluation of urban characteristics as follows:

2.

1.

2.

3.

4.

Cost (C1): This criterion represents the financial affordability of the city. Since this
cluster focuses on cost-effective locations, the cost should be as high as possible
(fuzzy number (0.9, 1, 1)). A higher rating means the city is more budget-friendly
in terms of living expenses, business operations, and overall affordability.
Infrastructure (C2): This refers to the quality and availability of public services,
transportation, and essential facilities. Cities in this cluster should have a
moderate level of infrastructure (fuzzy number (0.5, 0.6, 0.7)). This means they
provide basic amenities but might require improvements in areas like roads,
public transportation, healthcare, and digital connectivity.
Safety (C3): This criterion evaluates how secure the city is for residents, busi-
nesses, and visitors. These cities should have moderate safety levels (fuzzy
number (0.4, 0.5, 0.6)). While they are generally safe, they may have certain
areas that require extra precautions, such as higher crime rates or specific
security concerns.
Accessibility (C4): This criterion assesses how well-connected the city is both
regionally and internationally. The cities in this cluster should have moderate
accessibility (fuzzy number (0.4, 0.5, 0.6)). They typically have good regional
connectivity through local transportation networks but might lack direct ac-
cess to global travel hubs, such as major international airports or high-speed
rail links.

Cluster 2: High-Investment Cities with World-Class Infrastructure. Cities in this clus-
ter are renowned for their exceptional infrastructure, including state-of-the-art venues,
premium accommodations, and robust transportation networks. These cities are ideal
for events that aim to project prestige or cater to high-profile attendees. High safety
and accessibility scores further ensure a smooth and secure experience for participants.
However, these advantages come with significant costs, which can impact profitability
or restrict participation. Careful budgeting and strong justifications to stakeholders
are essential to address these challenges. The following analyzes and discusses the
values for each criterion in Cluster 2 using fuzzy numbers, which define the optimal
range for cost, infrastructure, safety, and accessibility within this category as follows:

1.

2.

3.

Cost (C1): Should be as low as possible (fuzzy number (0.05, 0.1, 0.12)) be-
cause these are expensive cities, making budget management a challenge.
The lower the rating, the higher the cost of living, business operations, and
general expenses.
Infrastructure (C2): Should be as high as possible (fuzzy number (0.8, 0.95, 1))
to ensure world-class facilities. This includes cutting-edge public transporta-
tion, advanced healthcare systems, efficient digital connectivity, and modern
urban planning.
Safety (C3): Should be as high as possible (fuzzy number (0.95, 0.95, 1)) since
these cities are known for their stability and security. Low crime rates, strong
law enforcement, and a secure environment make them attractive for businesses
and residents alike.

4. Accessibility (C4): Should be as high as possible (fuzzy number (0.7, 0.95, 1))
to ensure global connectivity. These cities have major international airports,
excellent public transit systems, and strong infrastructure to host international
conferences and business events.

---

<!-- PAGE 12 -->

Appl. Sci. 2025, 15, 4044

12 of 21

3.

Cluster 3: Balanced Cities with a Mix of Features. This cluster includes cities that strike
a strong balance between affordability and quality, offering good infrastructure, high
safety ratings, and excellent accessibility at reasonable costs. Their versatility makes
them ideal for events that seek to combine cost-effectiveness with a high-quality
experience for attendees. While these cities may not be as affordable as those in
Cluster 1 or have infrastructure as advanced as those in Cluster 2, their overall balance
makes them strong contenders for hosting successful events. Choosing between
similarly balanced options in this cluster might require additional considerations, but
their high safety and accessibility scores enhance the experience for all participants.
The following analyzes and discusses the values for each criterion in Cluster 3 using
fuzzy numbers, which define the optimal range for cost, infrastructure, safety, and
accessibility within this category.

1.

2.

3.

Cost (C1): Should be moderate (fuzzy number (0.5, 0.6, 0.7)) because these cities
balance quality and affordability. They are neither excessively expensive nor
extremely cheap, making them attractive for middle-income professionals and
businesses looking for cost-effective but well-equipped locations.
Infrastructure (C2): Should be good but not premium (fuzzy number (0.5, 0.6,
0.7)). These cities provide high-quality public services, efficient transportation,
and modern urban planning, but they may lack the cutting-edge facilities of
world-class metropolises.
Safety (C3): Should be high but not extreme (fuzzy number (0.5, 0.6, 0.7)). These
cities offer a safe environment with low to moderate crime rates, ensuring a
comfortable living and working atmosphere without reaching the ultra-secure
standards of Cluster 2 cities.

4. Accessibility (C4): Should be high but not at the maximum level (fuzzy number
(0.5, 0.6, 0.7)). These cities have strong regional and international connectivity,
including well-developed airports and transport networks, but they do not
match the global reach of the top-tier business hubs in Cluster 2.

Table 2 provides a summary of the optimal scores for each cluster discussed in
this section, with the centroids of each cluster defined using fuzzy numbers for each
criterion considered.

Table 2. Summary of optimal scores for each cluster—cluster centroids.

Cost (C1)

Infrastructure (C2)

Safety (C3)

Accessibility (C4)

Cluster
1
2
3

a
0.9
0.05
0.5

b
1
0.1
0.6

c
1
0.12
0.7

a
0.5
0.8
0.5

b
0.6
0.95
0.6

c
0.7
1
0.7

a
0.4
0.95
0.5

b
0.5
0.95
0.6

c
0.6
1
0.7

a
0.4
0.7
0.5

b
0.5
0.95
0.6

c
0.6
1
0.7

The scores presented in Table 3 were developed through a collaborative process
involving a diverse panel of experts and analysts. This group combined professional
experience in event planning and logistics with insights drawn from tourist feedback
and reviews published in reputable travel and tourism journals. By integrating these
perspectives, the evaluation captured not only the logistical and operational dimensions of
hosting an international event but also traveler perceptions and experiences.

---

<!-- PAGE 13 -->

Appl. Sci. 2025, 15, 4044

13 of 21

Table 3. Clustered data of cities for event hosting analysis.

Cost (C1) ($K)

Infrastructure (C2)

Safety (C3)

Accessibility (C4)

City A
City B
City C
City D
City E
City F
City G
City H
City I
City J
City K
City L

a
11
9
34
32
18
16
14
20
29
32
14
18

b
14
11
39
37
20
18
16
23
35
37
16
20

c
16
14
45
43
23
20
18
25
41
43
18
23

a
4
2
8
8
6
5
4
3
7
8
5
4

b
5
3
9
9
7
6
5
4
8
9
6
5

c
6
4
10
10
8
7
6
5
9
10
7
6

a
6
3
8
8
6
5
4
3
7
7
5
4

b
7
4
9
9
7
6
5
4
8
8
6
5

c
8
5
10
10
8
7
6
5
9
9
7
6

a
5
3
8
8
7
7
5
6
7
8
6
6

b
6
4
9
9
8
8
6
7
8
9
7
7

c
7
5
10
10
9
9
7
8
9
10
8
8

This comprehensive approach ensured that the assessment reflected both the func-
tional feasibility and the broader appeal of each city as a vibrant and welcoming destination.
For each city and criterion, experts provided individual scores based on their knowledge,
experience, and trusted sources such as government reports, traveler feedback, and indus-
try analyses. As expected, these evaluations varied, reflecting differing viewpoints and
priorities across the panel.

To ensure fairness and consistency, final scores were calculated by averaging the
individual assessments for each criterion and city. The resulting values were then expressed
as fuzzy numbers. This method helps harmonize diverse opinions and minimizes potential
bias, yielding well-rounded and objective scores for a more balanced evaluation.

5. Results and Discussion

In this section, we apply the proposed models, including the new clustering approach
and the logarithmic normalization method—within the TOPSIS framework for the pre-
sented case study. The results are detailed step by step, then analyzed and compared with
those obtained using traditional methods.

Table 4 presents the processing of the data from Table 3. Using the fuzzy number of
each alternative for each criterion, the corresponding centroid is calculated (columns 2 to
5), using Equation (2). These centroids are then normalized using the Min–Max method
(columns 6 to 9), using Equations (3) and (4).

Table 4. Normalized centroids for the four considered criteria across selected cities.

(C1)
Centroid

(C2)
Centroid

(C3)
Centroid

(C4)
Centroid

(C1)
Centroid
Normalized

(C1)
Centroid
Normalized

(C1)
Centroid
Normalized

(C1)
Centroid
Normalized

City A
City B
City C
City D
City E
City F
City G
City H
City I
City J
City K
City L

14
11
39
37
20
18
16
23
35
37
16
20

5
3
9
9
7
6
5
4
8
9
6
5

7
4
9
9
7
6
5
4
8
8
6
5

6
4
9
9
8
8
6
7
8
9
7
7

0.92
1.00
0.00
0.08
0.68
0.76
0.84
0.60
0.16
0.08
0.84
0.68

0.33
0.00
1.00
1.00
0.67
0.50
0.33
0.17
0.83
1.00
0.50
0.33

0.6
0
1
1
0.6
0.4
0.2
0
0.8
0.8
0.4
0.2

0.4
0
1
1
0.8
0.8
0.4
0.6
0.8
1
0.6
0.6

---

<!-- PAGE 14 -->

Appl. Sci. 2025, 15, 4044

14 of 21

The centroids calculated for each alternative are then used to compute their distances

to the optimal scores defined for each cluster, as outlined in Table 2.

Table 5 presents these distances, calculated using the Euclidean norm, as specified
in Equation (5). As the table shows, the distance between each alternative and the ideal
cluster values varies. To assign each alternative to a cluster, we select the one with the
minimum distance, as described in Equation (6). The final column in Table 5 displays the
shortest distance for each alternative, with the assigned cluster highlighted in bold.

Table 5. Evaluation of distances to the centroids of each cluster.

(C1) Distance

(C2) Distance

(C3) Distance

City A
City B
City C
City D
City E
City F
City G
City H
City I
City J
City K
City L

0.31
0.93
1.26
1.20
0.43
0.39
0.43
0.76
0.94
1.13
0.21
0.50

1.18
1.84
0.17
0.15
0.74
0.98
1.31
1.36
0.22
0.22
1.07
1.16

0.46
1.11
0.92
0.87
0.23
0.34
0.57
0.74
0.57
0.79
0.33
0.49

min

0.31
0.93
0.17
0.15
0.23
0.34
0.43
0.74
0.22
0.22
0.21
0.49

Table 6 presents the results aggregated by cluster, revealing a distribution that aligns

well with the intended definitions of each group.

Table 6. Result of the distribution of alternatives using the proposed clustering method.

Cluster

(C1)
Centroid

(C2)
Centroid

(C3)
Centroid

(C4)
Centroid

City A
City B
City G
City K

City C
City D
City I
City J

City E
City F
City H
City L

1
1
1
1

2
2
2
2

3
3
3
3

14
11
16
16

39
37
35
37

20
18
23
20

5
3
5
6

9
9
8
9

7
6
4
5

7
4
5
6

9
9
8
8

7
6
4
5

6
4
6
7

9
9
8
9

8
8
7
7

Cluster 1—Cost-Effective Cities with Moderate Infrastructure—includes alternatives
with the lowest costs, while the other criteria generally exhibit moderate values, confirming
the coherence of the classification.

Cluster 2—High-Investment Cities with World-Class Infrastructure—comprises alter-
natives that match the profile of high-cost cities offering top-tier scores in infrastructure,
safety, and accessibility.

Cluster 3—Balanced Cities with a Mix of Features—includes alternatives with inter-
mediate cost levels and criteria ratings that fall between those of Clusters 1 and 2. This
consistency reinforces the validity of the proposed clustering method.

---

<!-- PAGE 15 -->

Appl. Sci. 2025, 15, 4044

15 of 21

Based on these results, we can conclude that the proposed model produces outcomes
consistent with expectations. This means that analyzing the distribution of alternatives
across the different clusters confirms that the results are logical and align with the expected
distribution of alternatives within each cluster.

Table 7 compares the proposed clustering method with the Fuzzy K-Means approach,
revealing that the results are nearly identical—with one notable exception: City K is
assigned to Cluster 1 by the proposed method, whereas Fuzzy K-Means places it in Cluster
3. Although this difference may appear minor, it highlights an important distinction in
how each method interprets distances and assigns alternatives to clusters. Overall, the
strong alignment between the two methods supports the effectiveness and reliability of the
proposed approach as a viable alternative to traditional fuzzy clustering techniques.

Table 7. Comparison between the proposed clustering method and the Fuzzy K-Means method, bold
numbers highlight discrepancies between the two methods.

Proposed Method

Fuzzy K-Means

City A
City B
City G
City K
City C
City D
City I
City J
City E
City F
City H
City L

1
1
1
1
2
2
2
2
3
3
3
3

1
1
1
3
2
2
2
2
3
3
3
3

More importantly, assigning City K to Cluster 1 appears to be a more appropriate
classification. The city shares a low-cost profile, which is a defining characteristic of Cluster
1. In fact, City K has the same cost value as City G, which was placed in Cluster 1 by
the Fuzzy K-Means method. The only differences between the two are minor, such as a
one-point variation in other criteria—making them highly comparable. Therefore, grouping
City K with City G in Cluster 1 is more consistent with the underlying logic of the clustering
process. This supports the conclusion that the proposed method offers a more accurate and
contextually sound classification.

Another key advantage of the proposed method lies in its simplicity and computa-
tional efficiency when compared to Fuzzy K-Means, which depends on multiple iterative
calculations and a more complex optimization process. In contrast, the proposed method
uses a direct and intuitive approach by assigning each alternative to the nearest centroid,
eliminating the need for repeated recalculations. Fuzzy K-Means, on the other hand,
involves continuous re-evaluation of centroids, which increases computational demands—
particularly for larger datasets. Additionally, Fuzzy K-Means applies a soft clustering
strategy, where alternatives can partially belong to multiple clusters, whereas the proposed
method deterministically assigns each alternative to a single cluster.

In contrast, the proposed method is deterministic, assigning each alternative to a
single cluster without ambiguity. It also significantly reduces computational overhead by
avoiding iterative adjustments. Its ease of implementation makes it especially practical in
contexts where speed and efficiency are essential. Considering that the overall clustering
results are nearly identical—and that the proposed method classifies City K in a way that

---

<!-- PAGE 16 -->

Appl. Sci. 2025, 15, 4044

16 of 21

aligns more logically with the data—it can be regarded as not only simpler but also more
accurate and reliable than the Fuzzy K-Means approach.

In the next step, the rankings of each alternative within their respective clusters
were normalized using two methods: logarithmic normalization (Table 8) and Min–Max
normalization (Table 9).

Table 8. Logarithmic normalization results.

City

City A
City B
City G
City K

City C
City D
City I
City J

City E
City F
City H
City L

Cluster

1
1
1
1

2
2
2
2

3
3
3
3

C1

0.96
0.88
1.00
1.00

1.00
0.99
0.97
0.99

0.96
0.93
1.00
0.96

Table 9. Min–Max normalization results.

City

City A
City B
City G
City K

City C
City D
City I
City J

City E
City F
City H
City L

Cluster

1
1
1
1

2
2
2
2

3
3
3
3

C1

0.60
0.00
1.00
1.00

1.00
0.50
0.00
0.50

0.40
0.00
1.00
0.40

C2

0.92
0.71
0.92
1.00

1.00
1.00
0.95
1.00

1.00
0.94
0.77
0.86

C2

0.67
0.00
0.67
1.00

1.00
1.00
0.00
1.00

1.00
0.67
0.00
0.33

C3

1.00
0.77
0.86
0.94

1.00
1.00
0.95
0.95

1.00
0.94
0.77
0.86

C3

1.00
0.00
0.33
0.67

1.00
1.00
0.00
0.00

1.00
0.67
0.00
0.33

C4

0.94
0.77
0.94
1.00

1.00
1.00
0.95
1.00

1.00
1.00
0.95
0.95

C4

0.67
0.00
0.67
1.00

1.00
1.00
0.00
1.00

1.00
1.00
0.00
0.00

An analysis of Tables 8 and 9 shows that logarithmic normalization offers clear ad-
vantages over Min–Max normalization, particularly in the way it distributes values across
clusters. In Cluster 2, where the cost criterion (C1) exhibits significantly higher values
than in other clusters, Min–Max normalization exaggerates these differences, making cost
variations between cities appear more pronounced. In contrast, logarithmic normaliza-
tion compresses the scale, reducing the gaps between alternatives while preserving their
relative rankings.

A similar effect is observed in Cluster 3, where differences in cost (C1) and infras-
tructure (C2) are more evenly balanced under logarithmic transformation. This prevents
extreme values from overshadowing smaller differences. As a result, logarithmic nor-
malization delivers a more balanced representation, ensuring that no single high value
disproportionately influences the outcome—thus producing a more stable and interpretable
ranking system.

The next step is the application of the TOPSIS method to the normalized tables
(Tables 8 and 9), considering the weights for each criterion and each cluster, as presented in

---

<!-- PAGE 17 -->

Appl. Sci. 2025, 15, 4044

17 of 21

Table 10. These weights are derived from the optimal values within each cluster and are
essentially obtained by normalizing these values using the Min–Max method.

Table 10. Criterion weights for each cluster.

Cluster

(C1) Cluster
Centroid

(C2) Cluster
Centroid

(C3) Cluster
Centroid

(C4) Cluster
Centroid

Weight C1

Weight C2

Weight C3

Weight C4

1
2
3

1.0
0.1
0.6

0.6
0.9
0.6

0.5
1.0
0.6

0.5
0.9
0.6

0.38
0.03
0.25

0.23
0.32
0.25

0.19
0.34
0.25

0.19
0.31
0.25

City

City A
City B
City G
City K

City C
City D
City I
City J

City E
City F
City H
City L

City

City A
City B
City G
City K

City C
City D
City I
City J

City E
City F
City H
City L

Cluster

1
1
1
1

2
2
2
2

3
3
3
3

Cluster

1
1
1
1

2
2
2
2

3
3
3
3

The TOPSIS method was then applied using the weights derived for each cluster (as
shown in Table 10) and the normalized data from both approaches. Table 11 presents the
results obtained using logarithmic normalization, ranking the alternatives within their
respective clusters. Table 12 shows the results using Min–Max normalization, allowing for
a direct comparison between the two normalization techniques.

Table 11. TOPSIS results using logarithmic normalization, bold numbers indicate the best alternative
within each cluster identified by the method.

C1

0.36
0.33
0.38
0.38

0.03
0.03
0.03
0.03

0.24
0.23
0.25
0.24

C2

0.21
0.16
0.21
0.23

0.32
0.32
0.31
0.32

0.25
0.23
0.19
0.22

C3

0.19
0.15
0.16
0.18

0.34
0.34
0.32
0.32

0.25
0.23
0.19
0.22

C4

0.18
0.15
0.18
0.19

0.31
0.31
0.30
0.31

0.25
0.25
0.24
0.24

D+

0.03
0.10
0.03
0.01

0.00
0.00
0.03
0.02

0.01
0.03
0.08
0.05

D-

0.08
0.00
0.08
0.10

0.03
0.03
0.00
0.02

0.08
0.06
0.02
0.03

TOPSIS Score

0.74
0.00
0.69
0.89

1.00
0.98
0.00
0.57

0.89
0.67
0.18
0.38

Table 12. TOPSIS results using Min–Max normalization, bold numbers indicate the best alternative
within each cluster identified by the method.

C1

0.23
0.00
0.38
0.38

0.03
0.02
0.00
0.02

0.10
0.00
0.25
0.10

C2

0.15
0.00
0.15
0.23

0.32
0.32
0.00
0.32

0.25
0.17
0.00
0.08

C3

0.19
0.00
0.06
0.13

0.34
0.34
0.00
0.00

0.25
0.17
0.00
0.08

C4

0.13
0.00
0.13
0.19

0.31
0.31
0.00
0.31

0.25
0.25
0.00
0.00

D+

0.18
0.52
0.16
0.06

0.00
0.02
0.56
0.34

0.15
0.28
0.43
0.37

D-

0.36
0.00
0.43
0.50

0.56
0.56
0.00
0.45

0.44
0.34
0.25
0.15

TOPSIS Score

0.66
0.00
0.73
0.89

1.00
0.97
0.00
0.57

0.75
0.55
0.37
0.29

The application of the TOPSIS method using both Min–Max and logarithmic normal-
ization identified the top-ranked cities within each cluster. The results show that City
K (Cluster 1) and City C (Cluster 2) consistently achieved the highest scores across both
normalization methods, while City E (Cluster 3) exhibited some variation depending on
the technique used.

---

<!-- PAGE 18 -->

Appl. Sci. 2025, 15, 4044

18 of 21

In Cluster 1, City K emerged as the best-performing alternative, with a TOPSIS score
of approximately 0.887 in both cases. This indicates that City K offers a well-balanced
combination of cost, infrastructure, safety, and accessibility, making it the most suitable
option within its group.
Its consistent ranking across both normalization techniques
demonstrates strong alignment with the cluster’s ideal conditions.

In Cluster 2, City C achieved a perfect TOPSIS score of 1.000 under both normalization
methods, confirming its status as the most suitable alternative for this category. The
unchanged result, regardless of the normalization applied, reinforces City C’s dominance
in terms of meeting all weighted criteria.

In contrast, City E led Cluster 3 but showed noticeable variation between methods:
0.747 using Min–Max and 0.886 with logarithmic normalization. This difference suggests
that the logarithmic approach was more effective in smoothing extreme values and reducing
the influence of outliers. As a result, City E appeared closer to the ideal solution under
logarithmic normalization.

Overall, the consistency of City K and City C as top-ranked alternatives reinforces the
robustness of the methodology and confirms that the chosen criteria effectively distinguish
the best-performing cities within each cluster. However, the variation in City E’s score
highlights how normalization can influence ranking intensity, particularly in datasets where
differences between values are more pronounced.

The results show that logarithmic and Min–Max normalizations produced nearly
identical outcomes in the TOPSIS analysis, indicating that when there are no significant
outliers, logarithmic normalization performs just as well as the Min–Max method. However,
in the presence of extreme values, logarithmic normalization proves to be more effective, as
it reduces the impact of outliers and prevents criteria with very high values from distorting
the distance calculations in TOPSIS.

Thus, it is observed that for datasets without outliers, logarithmic normalization
performs just as well as Min–Max normalization, with the added advantage that when
outliers are present, logarithmic normalization delivers better performance. If the goal is
to ensure that normalization has a meaningful effect only in cases where data variation is
large, logarithmic normalization is preferable due to its ability to smooth extreme values.
However, when the data are naturally well-distributed, Min–Max normalization remains a
valid option, as it preserves the original proportions without information loss.

6. Conclusions

This study introduced two methodological innovations to enhance the TOPSIS
decision-making framework: Clustering Using Fuzzy Numbers and Centroid-Based Dis-
tance Allocation and logarithmic normalization. Together, these methods address key
limitations in traditional MCDM approaches, particularly in the handling of uncertainty,
outliers, and rigid data-driven classifications.

The proposed clustering approach allows decision-makers to define ideal cluster
profiles independently of the dataset, enabling greater strategic control. Fuzzy numbers
are used exclusively to model uncertainty in the evaluation of alternatives, which are
then converted to crisp values to calculate Euclidean distances from predefined centroids.
This results in a robust yet transparent classification method, free from iterative opti-
mization or probabilistic membership functions. Unlike traditional clustering techniques
such as K-Means, which derive centroids from data, our approach decouples clustering
from data distribution and focuses on alignment with idealized profiles—offering greater
interpretability and consistency.

Logarithmic normalization further enhances the robustness of the TOPSIS method by
smoothing extreme values and preserving proportional differences across criteria. This is es-

---

<!-- PAGE 19 -->

Appl. Sci. 2025, 15, 4044

19 of 21

pecially useful in datasets with high variance or non-linear distributions, where traditional
normalization techniques may distort rankings.

The case study results demonstrate that the proposed methodologies significantly
enhance both the accuracy and stability of decision-making outcomes. The fuzzy clustering
approach enables more realistic classification of alternatives, while logarithmic normaliza-
tion improves the comparability of criteria—without adding unnecessary complexity. A key
advantage of both methods is their computational simplicity and ease of implementation,
making them accessible for a broad range of practical applications.

Beyond the context of city selection, the proposed methodology offers broader en-
hancements to decision-making by improving how alternatives are grouped and compared
in the presence of uncertainty and variability. Its modular design—combining fuzzy-based
evaluation, predefined cluster centroids, and adaptive normalization—makes it suitable
for various domains such as supply chain optimization, financial assessment, environ-
mental planning, and strategic project prioritization. The method supports more robust,
context-aware, and scalable decision processes across diverse real-world applications.

Although the results are promising, there remain several opportunities for further
exploration and validation. A logical next step is to test the performance of these techniques
within other MCDM models—such as VIKOR, PROMETHEE, and AHP—to assess their
adaptability across different decision-making frameworks. Each of these models has unique
characteristics, and applying the proposed methods within them could offer deeper insights
into their generalizability and effectiveness.

Despite its promising results, the proposed methodology presents some limitations.
The definition of ideal cluster centroids is currently based on expert judgment, which,
while offering flexibility and interpretability, may introduce a degree of subjectivity. Fu-
ture refinements could explore hybrid or data-assisted strategies to support or validate
these predefined profiles. Additionally, while the method is computationally simple and
effective in the case study, its performance in large-scale or high-dimensional problems
remains to be tested. Moreover, although the proposed approach was applied within the
TOPSIS framework, evaluating its integration with other MCDM models (e.g., VIKOR,
PROMETHEE, AHP) would help assess its generalizability.

Finally, future work could involve benchmarking the proposed methods against other
clustering and normalization techniques. Comparative analyses focused on classification
accuracy, ranking stability, and computational efficiency would further support method
refinement and foster broader adoption in complex decision-making contexts.

Author Contributions: Conceptualization, V.A. and A.A.; methodology, V.A.; software, V.A.; vali-
dation, V.A. and A.A.; formal analysis, V.A.; investigation, V.A.; resources, V.A.; data curation, V.A.;
writing—original draft preparation, V.A.; writing—review and editing, A.A.; visualization, A.A.;
supervision, V.A.; project administration, V.A.; funding acquisition, A.A. All authors have read and
agreed to the published version of the manuscript.

Funding: This research received no external funding.

Institutional Review Board Statement: Not applicable.

Informed Consent Statement: Not applicable.

Data Availability Statement: The original contributions presented in the study are included in the
article; further inquiries can be directed to the corresponding authors.

Acknowledgments: The authors gratefully acknowledge the support from FCT–Fundação para a
Ciência e Tecnologia (Portuguese Foundation for Science and Technology), through IDMEC, under
LAETA Base Funding (DOI: 10.54499/UIDB/50022/2020).

Conflicts of Interest: The authors declare no conflicts of interest.

---

<!-- PAGE 20 -->

Appl. Sci. 2025, 15, 4044

References

20 of 21

1.

2.

Štili´c, A.; Puška, A. Integrating Multi-Criteria Decision-Making Methods with Sustainable Engineering: A Comprehensive Review
of Current Practices. Eng 2023, 4, 1536–1549. [CrossRef]
Hajduk, S.; Jelonek, D. A Decision-Making Approach Based on TOPSIS Method for Ranking Smart Cities in the Context of Urban
Energy. Energies 2021, 14, 2691. [CrossRef]

3. Madi, E.N.; Zakaria, Z.A.; Sambas, A.; Sukono. Toward Effective Uncertainty Management in Decision-Making Models Based on

4.

5.

6.

7.

8.

9.

Type-2 Fuzzy TOPSIS. Mathematics 2023, 11, 3512. [CrossRef]
Cai, M.; Hong, Y. Improved TOPSIS Method Considering Fuzziness and Randomness in Multi-Attribute Group Decision Making.
Mathematics 2022, 10, 4200. [CrossRef]
Sałabun, W.; W ˛atróbski, J.; Shekhovtsov, A. Are MCDA Methods Benchmarkable? A Comparative Study of TOPSIS, VIKOR,
COPRAS, and PROMETHEE II Methods. Symmetry 2020, 12, 1549. [CrossRef]
Vakilipour, S.; Sadeghi-Niaraki, A.; Ghodousi, M.; Choi, S.-M. Comparison between Multi-Criteria Decision-Making Methods
and Evaluating the Quality of Life at Different Spatial Levels. Sustainability 2021, 13, 4067. [CrossRef]
Qureshi, A.M.; Rachid, A. Comparative Analysis of Multi-Criteria Decision-Making Techniques for Outdoor Heat Stress
Mitigation. Appl. Sci. 2022, 12, 12308. [CrossRef]
Lim, Z.-Y.; Ong, L.-Y.; Leow, M.-C. A Review on Clustering Techniques: Creating Better User Experience for Online Roadshow.
Future Internet 2021, 13, 233. [CrossRef]
Krasnov, D.; Davis, D.; Malott, K.; Chen, Y.; Shi, X.; Wong, A. Fuzzy C-Means Clustering: A Review of Applications in Breast
Cancer Detection. Entropy 2023, 25, 1021. [CrossRef]

10. Al-Augby, S.; Majewski, S.; Majewska, A.; Nermend, K. A Comparison Of K -Means And Fuzzy C -Means Clustering Methods

For A Sample Of Gulf Cooperation Council Stock Markets. Folia Oeconomica Stetin. 2014, 14, 19–36. [CrossRef]

11. Ghadiri, N.; Ghaffari, M.; Nikbakht, M.A. BigFCM: Fast, Precise and Scalable FCM on Hadoop. arXiv 2016, arXiv:1605.03047.

[CrossRef]

12. Chen, Y.; Zhou, S. Revisiting Possibilistic Fuzzy C-Means Clustering Using the Majorization-Minimization Method. Entropy 2024,

26, 670. [CrossRef] [PubMed]

13. Chan, K.Y.; Yiu, K.F.C.; Kim, D.; Abu-Siada, A. Fuzzy Clustering-Based Deep Learning for Short-Term Load Forecasting in Power

Grid Systems Using Time-Varying and Time-Invariant Features. Sensors 2024, 24, 1391. [CrossRef]

14. Vafaei, N.; Ribeiro, R.A.; Matos, L.M.C. Data Normalization Techniques in Decision Making: Case Study with TOPSIS Method.

IJIDS 2018, 10, 19. [CrossRef]

15. Aytekin, A. Comparative Analysis of the Normalization Techniques in the Context of MCDM Problems. Decis. Mak. Appl. Manag.

Eng. 2021, 4, 1–25. [CrossRef]

16. Vafaei, N.; Ribeiro, R.A.; Camarinha-Matos, L.M. Comparison of Normalization Techniques on Data Sets with Outliers. Int.

J. Decis. Support Syst. Technol. 2021, 14, 1–17. [CrossRef]

17. Vafaei, N.; Ribeiro, R.A.; Camarinha-Matos, L.M. Normalization Techniques for Multi-Criteria Decision Making: Analytical
Hierarchy Process Case Study. In Technological Innovation for Cyber-Physical Systems; Camarinha-Matos, L.M., Falcão, A.J., Vafaei,
N., Najdi, S., Eds.; Springer International Publishing: Cham, Switzerland, 2016; Volume 470, pp. 261–269; ISBN 978-3-319-31164-7.
18. Zavadskas, E.K.; Turskis, Z. A New Logarithmic Normalization Method in Games Theory. Informatica 2008, 19, 303–314. [CrossRef]
Sahu, S.K. A Study of K-Means and C-Means Clustering Algorithms for Intrusion Detection Product Development. Int. J. Innov.
19.
Manag. Technol. 2014, 5, 207–213. [CrossRef]
Ikotun, A.M.; Ezugwu, A.E.; Abualigah, L.; Abuhaija, B.; Heming, J. K-Means Clustering Algorithms: A Comprehensive Review,
Variants Analysis, and Advances in the Era of Big Data. Inf. Sci. 2023, 622, 178–210. [CrossRef]

20.

21. Zolfani, S.; Yazdani, M.; Pamucar, D.; Zaraté, P. A VIKOR and TOPSIS Focused Reanalysis of the MADM Methods Based on

Logarithmic Normalization. arXiv 2020, arXiv:2006.08150. [CrossRef]

22. Magableh, G.M.; Mistarihi, M.Z. An Integrated Fuzzy MCDM Method for Assessing Crisis Recovery Strategies in the Supply

Chain. Sustainability 2024, 16, 2383. [CrossRef]

23. Nabeeh, N.A.; Abdel-Basset, M.; Gamal, A.; Chang, V. Evaluation of Production of Digital Twins Based on Blockchain Technology.

Electronics 2022, 11, 1268. [CrossRef]

24. Xia, J.-Y.; Li, S.; Huang, J.-J.; Yang, Z.; Jaimoukha, I.M.; Gündüz, D. Metalearning-Based Alternating Minimization Algorithm for

Nonconvex Optimization. IEEE Trans. Neural Netw. Learn. Syst. 2023, 34, 5366–5380. [CrossRef]

25. An, X.-K.; Du, L.; Jiang, F.; Zhang, Y.-J.; Deng, Z.-C.; Kurths, J. A Few-Shot Identification Method for Stochastic Dynamical
Systems Based on Residual Multipeaks Adaptive Sampling. Chaos Interdiscip. J. Nonlinear Sci. 2024, 34, 073118. [CrossRef]
Fang, P.; Gao, Z.; Tsay, R.S. Supervised Kernel Principal Component Analysis for Forecasting. Financ. Res. Lett. 2023, 58, 104292.
[CrossRef]

26.

27. Yang, R.-S.; Li, H.-B.; Huang, H.-Z. Multisource Information Fusion Considering the Weight of Focal Element’s Beliefs: A Gaussian

Kernel Similarity Approach. Meas. Sci. Technol. 2024, 35, 025136. [CrossRef]

---

<!-- PAGE 21 -->

Appl. Sci. 2025, 15, 4044

21 of 21

28.

Jin, H.; Tian, S.; Hu, J.; Zhu, L.; Zhang, S. Robust Ratio-Typed Test for Location Change under Strong Mixing Heavy-Tailed Time
Series Model. Commun. Stat.-Theory Methods 2025, 1–24. [CrossRef]

29. Zhou, M.; Zhao, X.; Luo, F.; Luo, J.; Pu, H.; Xiang, T. Robust RGB-T Tracking via Adaptive Modality Weight Correlation Filters

and Cross-Modality Learning. ACM Trans. Multimed. Comput. Commun. Appl. 2024, 20, 1–20. [CrossRef]

30. Peng, Y.; Zhao, Y.; Dong, J.; Hu, J. Adaptive Opinion Dynamics over Community Networks When Agents Cannot Express

Opinions Freely. Neurocomputing 2025, 618, 129123. [CrossRef]

31. Zhu, C. An Adaptive Agent Decision Model Based on Deep Reinforcement Learning and Autonomous Learning. J. Logist. Inform.

Serv. Sci. 2023, 10, 107–118. [CrossRef]

Disclaimer/Publisher’s Note: The statements, opinions and data contained in all publications are solely those of the individual
author(s) and contributor(s) and not of MDPI and/or the editor(s). MDPI and/or the editor(s) disclaim responsibility for any injury to
people or property resulting from any ideas, methods, instructions or products referred to in the content.

<!-- MARKITDOWN CONVERSION -->

<!-- Full MarkItDown conversion for formatting fidelity. -->

Article
Adaptive Cluster-Based Normalization for Robust TOPSIS in
Multicriteria Decision-Making
VitorAnes1,2,* andAntónioAbreu2,3
1 IDMEC,InstitutoSuperiordeEngenhariadeLisboa,InstitutoPolitécnicodeLisboa,1959-007Lisbon,Portugal
2 UnitforInnovationandResearchinEngineering,PolytechnicUniversityofLisbon,1959-007Lisbon,Portugal;
antonio.abreu@isel.pt
3 CenterofTechnologyandSystems(UNINOVA-CTS),AssociatedLabofIntelligentSystems(LASI),
2829-516Caparica,Portugal
* Correspondence:vitor.anes@isel.pt
Abstract: Inmulticriteriadecision-making(MCDM),methodssuchasTOPSISareessential
forevaluatingandcomparingalternativesacrossmultiplecriteria. However,traditional
normalizationtechniquesoftenstrugglewithdatasetscontainingoutliers,largevariances,
orheterogeneousmeasurementunits,whichcanleadtoskewedorbiasedrankings. To
addressthesechallenges,thispaperproposesanadaptive, cluster-basednormalization
approach,demonstratedthroughareal-worldlogisticscasestudyinvolvingtheselection
of a host city for an international event. The method groups alternatives into clusters
basedonsimilaritiesincriterionvaluesandapplieslogarithmicnormalizationwithineach
cluster. Thislocalizedstrategyreducestheinfluenceofoutliersandensuresthatscaling
adjustmentsreflectthespecificcharacteristicsofeachgroup.Inthecasestudy—wherecities
wereevaluatedbasedoncost,infrastructure,safety,andaccessibility—thecluster-based
normalizationmethodyieldedmorestableandbalancedrankings,eveninthepresence
ofsignificantdatavariability. Byreducingtheinfluenceofoutliersthroughlogarithmic
normalization and allowing predefined cluster profiles to reflect expert judgment, the
methodimprovesfairnessandadaptability. ThesefeaturesstrengthenTOPSIS’sabilityto
deliveraccurate,balanced,andcontext-awaredecisionsincomplex,real-worldscenarios.
Keywords: TOPSIS;logarithmicnormalization;cluster-basednormalization;multicriteria
decision-making;outliermitigation
AcademicEditor:YimingTang
Received:12February2025
Revised:26March2025
Accepted:2April2025 1. Introduction
Published:7April2025
Multi-criteriadecision-making(MCDM)methodsareessentialforaddressingcomplex
Citation: Anes,V.;Abreu,A.
problemsthatinvolvemultiple,oftenconflicting,factors. Amongthese,theTechniquefor
AdaptiveCluster-Based
OrderofPreferencebySimilaritytoIdealSolution(TOPSIS)iswidelyusedduetoitsability
NormalizationforRobustTOPSISin
toeffectivelyrankalternativesbasedontheirclosenesstoanidealsolution.
MulticriteriaDecision-Making.Appl.
Sci.2025,15,4044. https://doi.org/ ClusteringtechniquesareincreasinglyrelevantinTOPSIS-basedapplicationsbecause
10.3390/app15074044 theyenabledecision-makerstogroupalternativeswithsimilarcharacteristicsbeforeper-
formingtherankingprocedure. Thissegmentationenhancestheinterpretabilityofresults
Copyright:©2025bytheauthors.
LicenseeMDPI,Basel,Switzerland. andallowsformorecontext-sensitivecomparisons. Ratherthanapplyingaone-size-fits-all
Thisarticleisanopenaccessarticle rankingacrossadiversesetofalternatives,clusteringallowseachgrouptobeevaluated
distributedunderthetermsand against a tailored ideal profile, reflecting specific priorities or constraints. In this way,
conditionsoftheCreativeCommons
clusteringnotonlyincreasesadaptabilitytoreal-worldscenariosbutalsoimprovesthe
Attribution(CCBY)license
fairnessandclarityofthefinalrankings.
(https://creativecommons.org/
licenses/by/4.0/).
Appl.Sci.2025,15,4044 https://doi.org/10.3390/app15074044

Appl.Sci.2025,15,4044 2of21
However,despiteitsadvantages,certainchallengesremain—particularlyrelatedto
clusteringandnormalization. Traditionalclusteringmethodstendtoassignalternatives
to fixed categories, even when those alternatives share features with multiple groups.
Thisrigidclassificationcanleadtomisinterpretationandthelossofvaluableinformation,
especiallywhenthedatainvolvesuncertaintyoroverlappingcharacteristics. Likewise,
widelyusednormalizationtechniques—suchasMin–MaxandZ-score—oftenstruggleto
managelargedatavariations,skeweddistributions,andextremevalues,whichcandistort
rankingsandintroducebiasintodecision-making.
Toovercometheselimitations,thisstudyproposestwoinnovativemethodsdesigned
tomaketheTOPSISframeworkmoreflexible,reliable,anduser-friendly. ThefirstisClus-
teringUsingFuzzyNumbersandCentroid-BasedDistanceAllocation,anovelclustering
approachthatincorporatesfuzzynumberstorepresentuncertaintyintheevaluationof
alternatives. UnliketraditionalclusteringmethodssuchasK-Means—whereclustercen-
troidsaredeterminedbasedonthedataofexistingelements—ourapproachdefinesthe
centroidofeachclusterapriori,basedonexpertjudgmentandidealconditionsforeach
criterion. Alternativesarethenevaluatedusingfuzzynumberstoaccountforuncertainty,
andtheirdistancestothepredefinedclustercentroidsarecomputedusingcrispvalues
derived from these fuzzy assessments. This process avoids arbitrary assignments and
providesamorestructured,interpretableclassificationframeworkthatreflectsbothexpert
intentandtheinherentimprecisionofreal-worlddata.
ThesecondinnovationislogarithmicnormalizationinTOPSIS,atransformationtech-
niquethatsmoothsextremevariations,preservesproportionaldifferences,andprevents
anysinglecriterionfromdominatingthefinalrankings. Akeybenefitofthistechniqueis
that,whileitenhancesstabilityandaccuracy,itremainsasstraightforwardtoapplyastradi-
tionalmethodslikeMin–MaxorZ-scorenormalization,makingitapracticalenhancement
fordecision-makers.
By integrating these two methodological advancements, this study improves both
theclusteringandnormalizationcomponentsoftheTOPSISframework,addressingkey
limitationsintraditionalapproacheswhilemaintainingsimplicityandefficiency.
Unlike traditional data-driven clustering algorithms, the proposed method allows
decision-makerstodefineidealclusterprofilesindependentlyofthedataset. Thisdesign,
combinedwiththeuseoffuzzynumberstocaptureevaluationuncertainty,enablesasimple
yetrobustclassificationprocess. Thedeterministicassignmentofalternativesenhances
transparencyandinterpretability,makingtheapproachbothinnovativeandwell-suited
forreal-worlddecision-making.
Designedforbotheaseofimplementationandadaptability,themethodisapplicable
acrossawiderangeofdomains,includingfinance,environmentalassessment,andindus-
trialplanning. Byimprovingthegroupingofalternativesandenablingfairercomparisons
betweencriteria,theproposedapproachoffersamorebalanced,insightful,andscalable
solutionforcomplexdecision-makingproblems.
Thefollowingsectionsprovideadetailedexplanationoftheproposedmethods,their
theoreticalunderpinnings,andtheirpracticalimplementation.
Therestofthispaperisorganizedasfollows: Section2reviewstheexistingliterature
onclusteringandnormalizationinTOPSIS,highlightingtheirstrengthsandlimitations
andidentifyingthegapsthatthisstudyaimstoaddress. Section3outlinestheMaterials
andMethods,providingadetailedexplanationoftheproposedClusteringUsingFuzzy
NumbersandCentroid-BasedDistanceAllocationapproach, aswellasthelogarithmic
normalizationforTOPSIS,alongwiththeirtheoreticalfoundationsandimplementation
process. Section4presentsacasestudy,demonstratinghowthesemethodscanbeapplied
inareal-worlddecision-makingscenario. Section5analyzestheresults,comparingthe

Appl.Sci.2025,15,4044 3of21
proposed techniques with traditional methods to evaluate improvements in accuracy,
robustness,andefficiency. Finally,Section6offerstheconclusion,summarizingthekey
findings, discussing their broader implications, and suggesting possible directions for
futureresearch.
2. LiteratureReview
Multi-criteriadecision-making(MCDM)encompassesasetofmethodologiesusedto
evaluateandprioritizemultiple—oftenconflicting—factorsinthedecision-makingprocess.
Theseapproachesarecriticalinfieldssuchasenvironmentalmanagement,engineering,
andeconomics,wherecomplexdecisionsarefrequentlyencountered[1].
One of the most widely applied MCDM techniques is the Technique for Order of
PreferencebySimilaritytoIdealSolution(TOPSIS).Itscoreprincipleisstraightforward:the
optimalalternativeistheoneclosesttotheidealsolutionandfarthestfromtheworst-case
scenario. TOPSISisparticularlyvaluedforitssimplicityanditsabilitytoeffectivelyhandle
bothqualitativeandquantitativedata[2].
Likeanymethod,however,TOPSIShasitslimitations. Itcanstrugglewithdatasets
characterizedbyuncertainty,outliers,orhighvariance,whichmayaffecttheconsistency
and reliability of its rankings. In response, researchers have explored methods to link
inputuncertaintywithoutputuncertaintywithintheTOPSISframework,highlightingthe
challengesofinterpretinguncertaindatainreal-worlddecision-makingcontexts[3].
Refining these techniques can increase decision-makers’ confidence in the results,
therebyenhancingtheoverallvalueandapplicabilityofMCDMmethodsacrossvarious
industries[4].
ComparativestudieshaveexaminedTOPSISalongsideotherMCDMmethodssuch
as VIKOR, PROMETHEE, and AHP. For instance, one study evaluated four different
techniques—AHP,TOPSIS,ELECTREIII,andPROMETHEEII—inthecontextofgroup
decision-makingforsewernetworkprojects,offeringvaluableinsightsintotheirapplicabil-
ityandeffectiveness[5–7].
Traditionalclusteringmethods—suchasK-MeansandHierarchicalClustering—have
long served as fundamental tools for grouping similar data points in decision-making
models. Theirefficiencyandeaseofimplementationcontributetotheirwidespreaduse.
However,thesemethodshavenotablelimitations,especiallywhendealingwithuncertainty,
complex data distributions, or overlapping classifications. Because they rely on crisp
boundaries, each data point is strictly assigned to a single cluster, which can result in
inaccurate or overly simplistic groupings in real-world scenarios where data are often
ambiguousandmultidimensional[8].
To overcome these limitations, fuzzy clustering techniques—particularly Fuzzy C-
Means(FCM)—offeramoreflexiblealternative. Unliketraditionalclusteringmethods,
FCMallowsdatapointstobelongtomultipleclusterswithvaryingdegreesofmembership,
enablingmorenuancedandadaptableclassifications. Thisapproachisespeciallyvaluable
indomainssuchasmedicaldiagnosis,imagesegmentation,andcustomerprofiling,where
real-worlddatararelyconformstoclearlydefinedcategories[9].
Although FCM enhances clustering accuracy and adaptability, it also introduces
considerablecomputationalcomplexity. IncontrasttoK-Means,whichfollowsarelatively
simpleiterativeprocess,FCMrequiresmoreintensivecalculationsduetothecontinuous
updatingofmembershipprobabilitiesandtheoptimizationofanobjectivefunction. This
iterativeminimizationprocesscanbecomecomputationallyexpensive,particularlywhen
workingwithlarge,high-dimensionaldatasets. Asaresult,FCMincreasesprocessingtime
anddemandsgreatercomputationalresources[10].

Appl.Sci.2025,15,4044 4of21
Anothersignificantbarriertotheadoptionoffuzzyclusteringmethodsistheneedfor
programmingandalgorithmicexpertise. Implementingthesemethods—particularlyin
large-scaleapplications—requiresfamiliaritywithprogramminglanguagessuchasPython
v3,Rv4,orMATLABR2024a,aswellaswithspecializedlibrarieslikescikit-fuzzyorthe
FuzzyLogicToolbox. Unliketraditionalclusteringalgorithms,whichareoftenaccessible
throughbuilt-insoftwaretoolswithminimalcoding,FCMandsimilarapproachesdemand
manualparametertuning(e.g.,selectingtheoptimalfuzzinesscoefficientm)andcareful
datapreprocessingtoproducemeaningfulresults[11].
Additionally,FCMishighlysensitivetoinitialization—poorlyselectedinitialcentroids
canleadtosuboptimalclusteringoutcomes,oftenrequiringadvancedtechniquessuchas
geneticalgorithmsorparticleswarmoptimizationtoenhanceresults. Consequently,while
fuzzyclusteringoffersimprovedaccuracyandflexibility,itspracticalapplicationdemands
greaterexpertise,computationalresources,andalgorithmicfine-tuning[12].
Recentresearchhasfocusedonreducingthecomputationaloverheadassociatedwith
fuzzyclusteringbyexploringhybridmodelsthatcombinedeeplearningandoptimization
algorithms. These models aim to automate parameter selection and improve overall
performance. Suchadvancesseektomakefuzzyclusteringmoreaccessibleandscalable,
bridgingthegapbetweenitstheoreticalstrengthsandpracticalusabilityincomplex,real-
worlddecision-makingscenarios[13].
Normalizationisacriticalstepinmulti-criteriadecision-making(MCDM)processes,
asitensuresthatcriteriameasuredondifferentscalescanbecomparedmeaningfully[14].
Common normalization methods include Min–Max normalization: This method
rescalesdatatoafixedrange,typically[0,1],butissensitivetooutliers,whichcandistort
thenormalizedvalues. Z-Scorenormalization: Thistechniquestandardizesdatabasedon
meanandstandarddeviation,assuminganormaldistribution,whichmaynotholdtrue
foralldatasets. Vectornormalization: OftenusedinTOPSIS,thismethodnormalizesdata
bydividingeachcriterionvaluebytheEuclideannormofthevector. Whileeffective,it
maynotalwayspreserveproportionaldifferencesbetweencriteria.
Theseconventionalnormalizationtechniquesfacechallengeswhenappliedtohighly
skeweddata,extremevalues,ornon-lineardistributions,whichcancompromisethefair-
nessandaccuracyofdecision-makingoutcomes. Forexample,thechoiceofnormalization
methodcansignificantlyinfluencetherankingofalternativesinMCDMprocesses, un-
derscoringtheimportanceofselectinganappropriatetechniqueforeachspecificdecision
context[15,16].
Logarithmictransformationisamathematicaltechniqueusedtohandlenon-linear
data and compress large numerical ranges. By applying a logarithmic function, data
can be transformed to reduce skewness, manage outliers, and stabilize variance. This
transformationpreservesrelativedifferenceswhileminimizingtheinfluenceofextreme
values,makingitusefulinfieldssuchasstatistics,finance,andmachinelearning. Despite
theseadvantages,logarithmicnormalizationremainsunderutilizedinMCDMmethods
likeTOPSIS.IntegratingitintotheTOPSISframeworkcouldimproverankingstability
anddecisionaccuracy—especiallyindatasetscharacterizedbyhighvariance[17]. One
studyintroducedanovellogarithmicnormalizationmethodwithinthecontextofgame
theory,demonstratingitseffectivenessinseparatingnormalizedvaluesmoreefficiently
thanconventionalapproaches. Thesefindingssuggestpromisingapplicationsforsucha
methodinMCDMframeworksaswell[18].
The current literature reveals a lack of studies that combine fuzzy clustering with
centroid-based distance allocation within MCDM frameworks [19,20]. Furthermore, al-
thoughlogarithmicnormalizationoffersclearadvantagesforhandlinghigh-variancedata,
itsapplicationwithinTOPSISandotherMCDMmodelsremainslimited[21].

Appl.Sci.2025,15,4044 5of21
Addressingthesegapspresentsanopportunitytoimprovedecision-makingprocesses
bydevelopingaunifiedframeworkthatintegratesbothtechniques, therebyenhancing
clusteringprecisionandrankingaccuracywithinMCDMapplications[22].
RecentstudieshavealsoexploredtheintegrationofMCDMmethodswithuncertainty
modelinginemergingtechnologicalcontexts. Forinstance,Nabeehetal.[23]proposed
a hybrid model combining the Ordered Weighted Averaging (OWA) operator with the
TOPSISmethodtoevaluatekeyfactorsinfluencingtheproductionofdigitaltwinsbasedon
blockchaintechnology. Theirapproachleveragesneutrosophiclogictomanageuncertainty
inexpertjudgments,offeringastructuredyetflexibledecision-makingframework. While
theapplicationdomaindiffersfromthepresentstudy,bothapproachesshareacommon
goal: enhancing the reliability of TOPSIS in uncertain, multi-criteria environments. In
contrast to neutrosophic sets, our method uses fuzzy numbers exclusively to express
uncertaintyduringtheevaluationphase,followedbycrispclassificationbasedondistance
topredefinedidealcentroids. Thisallowsforimprovedinterpretabilityandcomputational
simplicitywhilemaintainingrobustnessindecisionsupport.
BeyondtheMCDM-andTOPSIS-focusedresearchreviewedhere,advancedstudies
inoptimization,machinelearning,andstatisticalmodelingmayinspirenovelextensions
to fuzzy clustering and logarithmic normalization approaches. Recent works on meta-
learningfornonconvexoptimization[24],few-shotidentificationforstochasticdynamical
systems[25],robustkernel-basedsurrogatemodeling[26],andGaussiankernelsimilar-
ity for multisource information fusion [27] illustrate how sophisticated algorithms can
handlehigh-dimensional,uncertaindata. Relatedeffortsaddressrobuststatisticaltests
forheavy-tailedtimeseries[28],supervisedlearningforcomplextracking[29],adaptive
opiniondynamics[30],andagent-baseddecisionmodelsleveragingdeepreinforcement
learning[31].
Althoughtheseadvancedmethodsofferimpressivecapabilities,theyoftencomewith
increasedcomputationalcomplexityanddemandahighleveloftechnicalexpertisefor
effectiveimplementation. Incontrast,ourgoalistoproposeamorestraightforwardand
practicalapproach,suitableforreal-worldscenarios,thatbalancestheneedtoaddressdata
variabilityanduncertaintywithsimplicityandusability. Nonetheless,thesesophisticated
techniqueshighlightpromisingdirectionsforfutureMCDMresearch,particularlyinthe
integrationofmeta-learning,robustmodeling,andadaptiveinformationfusiontofurther
improveclusteringandnormalizationstrategiesincomplexdecision-makingcontexts.
3. MaterialsandMethods
In this section, we introduce a new methodological approach that enhances both
clusteringandnormalizationwithintheTOPSISframeworkwhileensuringthattheprocess
remainsstraightforwardandeasytoimplement. Theproposedmethods,ClusteringUsing
FuzzyNumbersandCentroid-BasedDistanceAllocation,andtheintegrationoflogarithmic
normalizationinTOPSIS,addresskeylimitationsintraditionaltechniques. Byintroducing
amoreflexibleclusteringprocessandanadaptivenormalizationapproach,thesemethods
allowforamoreaccuraterepresentationofreal-worlddatavariability,improvingdecision-
makingoutcomes.
Oneofthefundamentalchallengesindecisionmodelsisthattraditionalclustering
methodstendtoassignalternativestorigidcategories,evenwhenthedatasuggestsamore
nuancedclassification. Thiscanleadtomisinterpretations,particularlywhendealingwith
uncertaintyoroverlappingdatapoints. Toovercomethislimitation,weproposeClustering
UsingFuzzyNumbersandCentroid-BasedDistanceAllocation,whichintroducesadegree
ofmembershipforeachalternativewithinaclusterinsteadofenforcingastrictassignment.

Appl.Sci.2025,15,4044 6of21
Thismethodacknowledgesthatalternativesmayexhibitcharacteristicsofmultipleclusters,
leadingtoamoreprecise,meaningful,andinterpretablegroupingofdata.
Similarly,conventionalnormalizationtechniquessuchasMin–MaxandZ-scoreoften
fail to handle datasets with large numerical variations, highly skewed distributions, or
extremeoutliers. TheseissuescandistortrankingsinTOPSIS,ascriteriawithsignificantly
largervaluesmaydisproportionatelyinfluencethefinalresults.Toaddressthis,wepropose
theintegrationoflogarithmicnormalizationinTOPSIS,whicheffectivelysmoothsextreme
variations,preservesrelativedifferences,andensuresamorebalancedinfluenceacross
criteria. Oneofitsmostcompellingadvantagesisthat,despiteitseffectivenessinhandling
complexdatadistributions,itremainsaseasytoapplyastraditionalnormalizationmethods,
makingitanaccessibleyetpowerfulenhancementfordecision-makers.
The strength of our proposed methodology lies in its ability to enhance accuracy,
robustness,andadaptabilitywhilemaintainingeaseofimplementation. Boththefuzzy
clusteringapproachandlogarithmicnormalizationaredesignedtoseamlesslyintegrate
intoexistingdecision-makingworkflowswithoutaddingcomputationalcomplexity. By
introducinggreaterflexibilityinclusteringandamoreadaptiveapproachtonormalization,
this study provides a scalable, practical, and efficient framework for improving multi-
criteriadecision-making. Thefollowingsectionsprovideanin-depthexplanationofhow
thesemethodsworkandtheirpracticalapplications.
3.1. ClusteringUsingFuzzyNumbersandCentroid-BasedDistanceAllocation
To group alternatives into meaningful clusters, we implement a fuzzy clustering
approach. Thismethodinvolvesthefollowingsteps:
Step1:Representationofalternativeswithfuzzynumbers—eachalternative’scriteria’s
valuesareconvertedintofuzzynumbers(a, b, c)representingthelowerbound, central
value, andupperbound, respectively. Thisallowsforamoreflexiblerepresentationof
uncertaintyinthedecision-makingprocess.
Step 2: In this step, the cluster centroids are determined qualitatively by the user,
identifyingtheoptimalrankingforeachcriterionwithinthecluster. Thisprocessemploys
fuzzynumbers,representedasvalues(a,b,c)rangingbetween0and1. Theseresultswill
allowustomeasurethedistancebetweentheclustercentroids,whichrepresenttheideal
positionforeachclusterbasedontheselectedcriteria—andthescoresofeachalternative.
Beyondthisprimarypurpose,theresultingcentroidsarealsousedtodeterminethecriterion
weights, which will later be applied in the TOPSIS method. Formula (1) calculates the
centroidrepresentingtheoptimalpositionwithinagivencluster.
(cid:18) a +b +c (cid:19)
C = w w w , (1)
cwj
3
j
wherea ,b ,c arethefuzzynumbercomponentsrepresentingtheoptimalpositionwithin
w w w
agivenclusterj.
Step3: Determinationofalternativecentroids—usingafuzzyclusteringapproach,
thecentroidsofeachalternativearedetermined. ThecentroidC foreachalternativeiis
Aij
computedasfollows:
(cid:18) a +b +c (cid:19)
C = i i i , (2)
Aij
3
j
wherea,b,c arethefuzzynumbercomponentsofalternativeiinthecriterionj.
i i i
Thisformulaisappliedtoallalternativesacrossallconsideredcriteriatoestablishthe
rankingofthealternatives.
Equations (1) and (2) define two distinct types of centroids within the proposed
method:clustercentroidsandalternativecentroids.Theclustercentroidrepresentstheideal

Appl.Sci.2025,15,4044 7of21
positionofagivenclusteracrossallcriteriaandiscomputedbasedonpredefinedfuzzy
valuesthatcharacterizethecluster’soptimalconditions. Thiscentroidremainsfixedforall
alternativeswithinthecluster,servingasareferencepointforcomparison. Incontrast,the
alternativecentroidiscalculatedbasedonthefuzzyscoresassignedtoaspecificalternative,
meaningitvariesfromonealternativetoanother. Whiletheclustercentroidreflectsthe
overallprofileofagroup,thealternativecentroidcapturestheindividualpositioningofan
alternativewithinthedecisionspace. Thisdistinctioniscrucialfortheclusteringprocess,
asitenablesamoreflexibleclassificationofalternativeswhilemaintainingastructured
evaluationframework.
Step4: Thenewdecisionmatrix,obtainedfromStep3,isnormalizedusingthecost
(lowerisbetter)andbenefit(higherisbetter)formulas(Formulas(2)and(3)).
max(X)−X
N = i , (3)
i max(X)−min(X)
X −max(X)
N = i , (4)
i max(X)−min(X)
whereN isthenormalizedvalueofthealternativei,X istheoriginalvalueofthealterna-
i i
tivei,max(X)isthemaximumvalueinthecriterion,andmin(X)istheminimumvaluein
thecriterion. Theseformulasscalethevaluesbetween0and1,ensuringafaircomparison
betweenalternativeswhilemaintainingthemeaningofcostandbenefitcriteria.
Step5: Calculationofdistancetoclustercentroids—thedistancebetweeneachalter-
nativecentroid(CAlternative)ineachcriterionj,andeachclustercentroid(CCluster)ineach
criterionj,iscalculatedusingtheEuclideandistanceformulaasfollows:
(cid:118)
D iw =
(cid:117)
(cid:117) (cid:116) ∑
m (cid:16)
C i A j lternative−C w Cl j uster
(cid:17)2
, (5)
j=1
whereD representsthedistancebetweenthecentroidofalternativeiandthecentroidof
iw
theoptimalpositionwithinclusterw,andmdenotesthenumberofcriteriaconsideredin
theMCDMproblemunderanalysis.
Step 4: Assignment of alternatives to clusters—each alternative is assigned to the
cluster with the smallest distance to its centroid. This process involves calculating the
distancebetweeneachalternativeandallclustercentroids. Thealternativeisthenassigned
to the cluster with the nearest centroid, ensuring it is grouped with the most similar
alternativesasdefinedinFormula(6).
C =argminD , (6)
i iw
w
where C is the cluster assigned to alternative i and argmin selects the cluster w that
i
w
minimizesthedistance.
3.2. LogarithmicNormalization: AnAdaptiveApproachforTOPSIS
Normalizationisafundamentalstepinmulti-criteriadecision-making(MCDM)meth-
odssuchasTOPSIS(TechniqueforOrderofPreferencebySimilaritytoIdealSolution). It
ensuresthatcriteriawithdifferentunitsandscalescanbemeaningfullycompared. Tra-
ditionalnormalizationmethods, suchasMin–MaxandZ-score, effectivelyrescaledata
butmaynotbesuitablefordatasetswithhighvariance,extremeoutliers,ornon-linear
distributions. Insuchcases,logarithmicnormalizationemergesasanalternativetechnique
thatdynamicallyadjuststodatadistributions,makingitparticularlyeffectiveforhandling
dataspanningmultipleordersofmagnitude. Bycompressinglargenumericalvariations

Appl.Sci.2025,15,4044 8of21
while amplifying smaller differences, this approach ensures a more balanced contribu-
tionofcriteriatothefinaldecision, preservingtherelativerankingamongalternatives.
LogarithmicnormalizationismathematicallyexpressedasshowninEquation(7),
log(X)−log(X )
X = min , (7)
log(X )−log(X )
max min
where X represents the normalized value, X is the original value, and X and X
min max
denotetheminimumandmaximumvalueswithinagivencriterion. Thistransformationis
particularlybeneficialindecision-makingscenarioswheresomecriteriaexhibitexponential
growthpatterns,suchasfinancialmetrics,environmentalindicators,andenergyconsump-
tion data. By using a logarithmic scale, the influence of extreme values is harmonized,
ensuringthatallcriteriacontributemeaningfullytothedecision-makingprocessinTOPSIS,
forinstance. Akeystrengthoflogarithmicnormalizationisitsadaptivenature. Unlike
fixedrangemethods,itautomaticallyadjuststovaryingdatamagnitudes,dynamically
scalingvaluestoensurefaircomparisonsacrosscriteria. Thismakesitparticularlyeffective
fordatasetswithhighlyskeweddistributionsorlargenumericaldifferences. Moreover,
itenhancesdecisionstability,reducingthedominanceofcriteriawithdisproportionately
largevalueswhileensuringthatsmallervaluesremaindistinguishable. Anotheradvantage
oflogarithmicnormalizationisitsabilitytoenhancedifferentiationamongalternatives.
Byredistributingvaluesinawaythatemphasizesproportionaldifferences,itensuresthat
the ranking process in TOPSIS remains representative and reliable, even when dealing
withhighlydisperseddatasets. Thisisparticularlybeneficialincaseswherecriteriaex-
hibitnon-linearrelationships,allowingforamoreaccuratereflectionofeachalternative’s
performance. TheimplicationsoflogarithmicnormalizationinTOPSISaresignificant. By
integratingthisapproach,rankingsbecomemorestableandreflectiveofreal-worldcondi-
tions,ensuringthatdecision-makingprocessesremainrobustandinterpretable. Givenits
abilitytobalancedifferencesacrosscriteriawithoutdistortingrankings,logarithmicnormal-
izationoffersanadvancedscalingtechniquethatalignswellwithdiversedecision-making
scenarios. Despiteitsmanyadvantages,logarithmicnormalizationhasyettobewidely
integratedintotheTOPSISframework,presentinganexcitingopportunityforinnovation.
Byintroducingthisapproach,wecancreateamoreadaptivewayofhandlingcriteriawith
highvariance,non-lineardistributions,andsensitivitytooutliers. Thisintegrationhelps
improverankingstability,ensuresfairercomparisonsbetweenalternatives,andstrengthens
theoveralldecision-makingprocess. Whatmakeslogarithmicnormalizationevenmore
appealingisitseaseofimplementation. Whileiteffectivelybalancesdatadistributionand
minimizestheimpactofextremevalues,itremainsjustassimpletoapplyasMin–Maxor
Z-scorenormalization. Thismeansthatdecision-makerscanbenefitfromitsadvantages
withoutfacingadditionalcomputationalcomplexityorimplementationchallenges.
Tofurtherclarifytheproposedmethod,Figure1providesastep-by-stepflowchart
illustrating the transformation of raw data into fuzzy values, the application of fuzzy
clustering,andthefinallogarithmicnormalization.
Theproposedmethodintroducesseveralmethodologicalinnovationsthatenhance
the flexibility, interpretability, and robustness of the TOPSIS framework. First, instead
ofrelyingondata-drivenclusteringtechniques,theapproachusesexpert-definedideal
clusterprofiles(step4),representedthroughfuzzynumbers,allowingforcontext-aware
classificationofalternatives. Second,alternativesareassignedtoclustersbasedontheir
Euclideandistancetotheseidealprofiles,enablingadeterministicandtransparentgrouping
process(steps7and8). Third,logarithmicnormalizationisappliedwithineachclusterto
reducetheinfluenceofoutliersandlargevariances,improvingthestabilityandfairnessof
therankings(step9). Finally,themethodderivestheweightsofcriteriadirectlyfromthe

Appl.Sci.2025,15,4044 9of21
idealclustercentroids,eliminatingtheneedforsubjectiveorcomplexweightingprocedures
Appl. Sci. 2025, 15, x FOR PEER REVIEW 9 of 21
(step10).Together,theseinnovationsofferapracticalandscalablesolutionformulti-criteria
decision-makinginreal-worldscenariosinvolvinguncertaintyandheterogeneousdata.
Figure1.Overviewoftheproposeddecision-makingworkflow,combiningfuzzyevaluation,cluster
Figure 1. Overview of the proposed decision-making workflow, combining fuzzy evaluation, clus-
assignment,andlogarithmicnormalizationwithintheTOPSISframework.Thedashedoutlineboxes
ter assignment, and logarithmic normalization within the TOPSIS framework. The dashed outline
representthecontributionsoftheproposedmethodology.
boxes represent the contributions of the proposed methodology.
4. CaseStudy
The proposed method introduces several methodological innovations that enhance
Thiscasestudyfocusesonselectingthemostsuitablecitytohostaninternationalevent
stchhee dfluelxeidbitloittya,k ienptelarpcereintatbwiloityye, aarns.dT rhoebduesctniseiosns oisf ctohme pTlOexP,SinISv oflrvaimngewthoerekv.a Fluirastti,o innstead of
orfeklyeiynfga cotno rdsastuac-hdraisvceons tcsl,ulsotgeirsitnicgs ,teactthenndiqeueeesx,p therei eanpcpe,roanadcho uveserasl lexevpeenrtt-idmepfiancet.dT iodeal clus-
ftaecri lpitraotefitlhese (psrtoecpe 4ss),, raedparteasseenttoefdp tohtreonutigahl hfousztzcyi tnieusmwbaesrasn, aallylozwedinagn dfogr rcoounpteedxti-natwoare clas-
csliufiscteartsiobna soefd aolnteercnoantoivmeisc. cSheacroanctder, iastlitcesr,ninaftrivasetsr uacrteu raesqsiuganlietyd, staof ectlyu,satnedrsa bccaessesdib iolinty t.heir Eu-
Table 1 presents an overview of the cities, each identified by a letter for clarity. These
clidean distance to these ideal profiles, enabling a deterministic and transparent grouping
citieswerethoroughlyassessed,withdescriptionshighlightingtheirindividualstrengths
process (steps 7 and 8). Third, logarithmic normalization is applied within each cluster to
andchallenges. Thisstructuredapproachprovidesvaluableinsights,supportingdecision-
reduce the influence of outliers and large variances, improving the stability and fairness
makersinidentifyingthebestlocationtoensuretheevent’ssuccess. Intotal,12citieswere
of the rankings (step 9). Finally, the method derives the weights of criteria directly from
evaluatedusingfourcriteria:cost,infrastructure,safety,andaccessibility.Thesealternatives
the ideal cluster centroids, eliminating the need for subjective or complex weighting pro-
wereselectedtoreflectarealisticshortlistingscenario,wheredecision-makerstypically
ncaerdrouwreds o(wstnepo p1t0io).n Tsobgaseethdeorn, tphreesliem iinnnaroyvsactrieoennsi nogff.eWr hai lpertahcetidcaatla asentdis smcaoldaebrlaet esoinlution for
smizeu,litti-ccarpittuerreias adedciviseirosen-rmanagkeionfgu irnb arneaplr-owfiolersldan sdcegneoagriroaps hinicvcoolnvtienxgts .uTnhceersttrauincttuyr eanofd hetero-
tgheendeaotau—s doragtaan. izedasfuzzyevaluationspercriterion—allowsfornuancedanalysisand
robustcomparisonacrossalternatives.
4. CTahseec iStietsuwdeyr e evaluated based on the following four key criteria, each playing a
crucialroleindeterminingtheirsuitabilitytohosttheinternationalevent:
This case study focuses on selecting the most suitable city to host an international
1. Cost(C1): Theestimatedtotalexpenseofhostingtheevent,measuredinmillionsof
event scheduled to take place in two years. The decision is complex, involving the evalu-
dollars. Thiscriterionreflectsthefinancialfeasibilityofeachcityanditspotential
ation of key factors such as costs, logistics, attendee experience, and overall event impact.
impactontheevent’sbudget.
To facilitate the process, a dataset of potential host cities was analyzed and grouped into
clusters based on economic characteristics, infrastructure quality, safety, and accessibility.
Table 1 presents an overview of the cities, each identified by a letter for clarity. These cities
were thoroughly assessed, with descriptions highlighting their individual strengths and
challenges. This structured approach provides valuable insights, supporting decision-
makers in identifying the best location to ensure the event’s success. In total, 12 cities were
evaluated using four criteria: cost, infrastructure, safety, and accessibility. These alterna-
tives were selected to reflect a realistic shortlisting scenario, where decision-makers typi-
cally narrow down options based on preliminary screening. While the dataset is moderate
in size, it captures a diverse range of urban profiles and geographic contexts. The structure

Appl.Sci.2025,15,4044
10of21
2. Infrastructure(C2): Ascorefrom1to10thatrepresentsthequalityofvenues,trans-
portationsystems,accommodations,andotherfacilitiesrequiredtohostalarge-scale
internationalevent.
3. Safety(C3): Anindex(1to10)measuringoverallsafetyinthecity,includingcrime
rates,politicalstability,andemergencypreparedness. Ahigherscoreindicatesasafer
environmentforattendees.
4. Accessibility(C4): Ascorefrom1to10reflectingthecity’sconnectivityandeaseof
access,includinginternational/domesticflightavailability,publictransit,androad
infrastructure.
Table1.Potentialcitiesforselectionashostsofaninternationalevent.
| City(Letter) | City | Description |
| ------------ | ---- | ----------- |
Low-costcitywithfunctionalinfrastructure,ideal
| CityA | Hanoi,Vietnam |     |
| ----- | ------------- | --- |
forregionalevents.
Highlyaffordablebutwithlimitedinfrastructure
| CityB | Kathmandu,Nepal |     |
| ----- | --------------- | --- |
andmoderatesafety.
Exceptionalinfrastructure,safety,andaccessibility;
| CityC | Tokyo,Japan |     |
| ----- | ----------- | --- |
high-costcity.
CityD Singapore,Singapore SimilarqualitytoTokyowithslightlylowercosts.
|     | KualaLumpur, | Balancedcitywithhighsafety,accessibility,and |
| --- | ------------ | -------------------------------------------- |
CityE
|     | Malaysia | moderatecosts. |
| --- | -------- | -------------- |
MoreaffordablethanKualaLumpur,withslightly
| CityF | Bangkok,Thailand |     |
| ----- | ---------------- | --- |
lowersafetyscores.
Affordablewithgrowinginfrastructureand
| CityG | Colombo,SriLanka |     |
| ----- | ---------------- | --- |
moderateaccessibility.
Slightlyhighercostwithchallengesininfrastructure
| CityH | Manila,Philippines |     |
| ----- | ------------------ | --- |
andsafety.
Highsafetyandgoodinfrastructure,thoughslightly
| CityI | Seoul,SouthKorea |     |
| ----- | ---------------- | --- |
lessaccessible.
Highlyaccessibleandsecure,withcostssimilar
| CityJ | HongKong,China |     |
| ----- | -------------- | --- |
toTokyo.
|     | HoChiMinhCity, | Goodsafetyandaccessibility,withmoderately |
| --- | -------------- | ----------------------------------------- |
CityK
|     | Vietnam | highercosts. |
| --- | ------- | ------------ |
Highaccessibilityandsafetywithbalanced,
| CityL | Jakarta,Indonesia |     |
| ----- | ----------------- | --- |
moderatecosts.
To streamline the decision-making process, the cities under consideration were
grouped into three clusters based on shared characteristics, including cost, infrastruc-
ture,safety,andaccessibility. Eachclusterrepresentsadistinctcategoryofcities,enabling
decision-makerstonarrowtheirfocusandevaluatealternativesmoreeffectivelyasfollows:
1. Cluster1: Cost-EffectiveCitieswithModerateInfrastructure. Thisclusterconsists
of budget-friendly cities, making them attractive options for events with tighter
financialconstraints. Theirlowercostsalloworganizerstoallocateresourcestoother
areas,suchasmarketingorimprovingtheattendeeexperience. Thesecitiesmayalso
attracthigherattendancefromlocalorregionalparticipantsduetotheiraffordability.
However, they present certain challenges. Infrastructure may require temporary
enhancementstomeettheneedsofaninternationalaudience,andtheirsafetyand
accessibilityscoresaregenerallymoderate—requiringcarefulplanningtoensurea
successfulevent.
Inthefollowing,thevaluespresentedforeachcriterionareanalyzedanddiscussed
usingfuzzynumbers, whichrepresenttheoptimalvaluesforeachcriterionwithinthis
cluster. These fuzzy values indicate the most desirable levels for cost, infrastructure,
safety, andaccessibility, providingadegreeofflexibilityratherthanrigid, fixedvalues.
Byapplyingfuzzylogic,thisapproachacknowledgesthatreal-worldcityclassifications

Appl.Sci.2025,15,4044 11of21
involvegradualtransitionsratherthanstrictcategorizations,allowingforamorenuanced
andadaptableevaluationofurbancharacteristicsasfollows:
1. Cost(C1):Thiscriterionrepresentsthefinancialaffordabilityofthecity.Sincethis
clusterfocusesoncost-effectivelocations,thecostshouldbeashighaspossible
(fuzzynumber(0.9,1,1)).Ahigherratingmeansthecityismorebudget-friendly
intermsoflivingexpenses,businessoperations,andoverallaffordability.
2. Infrastructure(C2): Thisreferstothequalityandavailabilityofpublicservices,
transportation, and essential facilities. Cities in this cluster should have a
moderatelevelofinfrastructure(fuzzynumber(0.5,0.6,0.7)). Thismeansthey
providebasicamenitiesbutmightrequireimprovementsinareaslikeroads,
publictransportation,healthcare,anddigitalconnectivity.
3. Safety(C3): Thiscriterionevaluateshowsecurethecityisforresidents,busi-
nesses, and visitors. These cities should have moderate safety levels (fuzzy
number (0.4, 0.5, 0.6)). While they are generally safe, they may have certain
areas that require extra precautions, such as higher crime rates or specific
securityconcerns.
4. Accessibility(C4): Thiscriterionassesseshowwell-connectedthecityisboth
regionallyandinternationally. Thecitiesinthisclustershouldhavemoderate
accessibility(fuzzynumber(0.4,0.5,0.6)). Theytypicallyhavegoodregional
connectivity through local transportation networks but might lack direct ac-
cesstoglobaltravelhubs,suchasmajorinternationalairportsorhigh-speed
raillinks.
2. Cluster2: High-InvestmentCitieswithWorld-ClassInfrastructure. Citiesinthisclus-
terarerenownedfortheirexceptionalinfrastructure,includingstate-of-the-artvenues,
premiumaccommodations,androbusttransportationnetworks. Thesecitiesareideal
foreventsthataimtoprojectprestigeorcatertohigh-profileattendees. Highsafety
andaccessibilityscoresfurtherensureasmoothandsecureexperienceforparticipants.
However,theseadvantagescomewithsignificantcosts,whichcanimpactprofitability
orrestrictparticipation. Carefulbudgetingandstrongjustificationstostakeholders
areessentialtoaddressthesechallenges. Thefollowinganalyzesanddiscussesthe
valuesforeachcriterioninCluster2usingfuzzynumbers,whichdefinetheoptimal
rangeforcost,infrastructure,safety,andaccessibilitywithinthiscategoryasfollows:
1. Cost (C1): Should be as low as possible (fuzzy number (0.05, 0.1, 0.12)) be-
cause these are expensive cities, making budget management a challenge.
The lower the rating, the higher the cost of living, business operations, and
generalexpenses.
2. Infrastructure(C2): Shouldbeashighaspossible(fuzzynumber(0.8,0.95,1))
to ensure world-classfacilities. Thisincludes cutting-edge public transporta-
tion, advancedhealthcaresystems, efficientdigitalconnectivity, andmodern
urbanplanning.
3. Safety(C3): Shouldbeashighaspossible(fuzzynumber(0.95,0.95,1))since
thesecitiesareknownfortheirstabilityandsecurity. Lowcrimerates,strong
lawenforcement,andasecureenvironmentmakethemattractiveforbusinesses
andresidentsalike.
4. Accessibility(C4): Shouldbeashighaspossible(fuzzynumber(0.7, 0.95, 1))
to ensure global connectivity. These cities have major international airports,
excellentpublictransitsystems,andstronginfrastructuretohostinternational
conferencesandbusinessevents.

Appl.Sci.2025,15,4044 12of21
3. Cluster3:BalancedCitieswithaMixofFeatures.Thisclusterincludescitiesthatstrike
astrongbalancebetweenaffordabilityandquality,offeringgoodinfrastructure,high
safetyratings,andexcellentaccessibilityatreasonablecosts. Theirversatilitymakes
them ideal for events that seek to combine cost-effectiveness with a high-quality
experience for attendees. While these cities may not be as affordable as those in
Cluster1orhaveinfrastructureasadvancedasthoseinCluster2,theiroverallbalance
makes them strong contenders for hosting successful events. Choosing between
similarlybalancedoptionsinthisclustermightrequireadditionalconsiderations,but
theirhighsafetyandaccessibilityscoresenhancetheexperienceforallparticipants.
ThefollowinganalyzesanddiscussesthevaluesforeachcriterioninCluster3using
fuzzynumbers,whichdefinetheoptimalrangeforcost,infrastructure,safety,and
accessibilitywithinthiscategory.
1. Cost(C1): Shouldbemoderate(fuzzynumber(0.5,0.6,0.7))becausethesecities
balancequalityandaffordability. Theyareneitherexcessivelyexpensivenor
extremelycheap,makingthemattractiveformiddle-incomeprofessionalsand
businesseslookingforcost-effectivebutwell-equippedlocations.
2. Infrastructure(C2): Shouldbegoodbutnotpremium(fuzzynumber(0.5,0.6,
0.7)). Thesecitiesprovidehigh-qualitypublicservices,efficienttransportation,
and modern urban planning, but they may lack the cutting-edge facilities of
world-classmetropolises.
3. Safety(C3): Shouldbehighbutnotextreme(fuzzynumber(0.5,0.6,0.7)). These
cities offer a safe environment with low to moderate crime rates, ensuring a
comfortablelivingandworkingatmospherewithoutreachingtheultra-secure
standardsofCluster2cities.
4. Accessibility(C4): Shouldbehighbutnotatthemaximumlevel(fuzzynumber
(0.5,0.6,0.7)). Thesecitieshavestrongregionalandinternationalconnectivity,
including well-developed airports and transport networks, but they do not
matchtheglobalreachofthetop-tierbusinesshubsinCluster2.
Table 2 provides a summary of the optimal scores for each cluster discussed in
this section, with the centroids of each cluster defined using fuzzy numbers for each
criterionconsidered.
Table2.Summaryofoptimalscoresforeachcluster—clustercentroids.
Cost(C1) Infrastructure(C2) Safety(C3) Accessibility(C4)
Cluster a b c a b c a b c a b c
1 0.9 1 1 0.5 0.6 0.7 0.4 0.5 0.6 0.4 0.5 0.6
2 0.05 0.1 0.12 0.8 0.95 1 0.95 0.95 1 0.7 0.95 1
3 0.5 0.6 0.7 0.5 0.6 0.7 0.5 0.6 0.7 0.5 0.6 0.7
The scores presented in Table 3 were developed through a collaborative process
involving a diverse panel of experts and analysts. This group combined professional
experience in event planning and logistics with insights drawn from tourist feedback
and reviews published in reputable travel and tourism journals. By integrating these
perspectives,theevaluationcapturednotonlythelogisticalandoperationaldimensionsof
hostinganinternationaleventbutalsotravelerperceptionsandexperiences.

Appl.Sci.2025,15,4044
13of21
Table3.Clustereddataofcitiesforeventhostinganalysis.
|       | Cost(C1)($K) |     | Infrastructure(C2) |     |     |     | Safety(C3) |     |     | Accessibility(C4) |      |
| ----- | ------------ | --- | ------------------ | --- | --- | --- | ---------- | --- | --- | ----------------- | ---- |
|       | a b          | c   | a                  | b   | c   |     | a          | b   | c   | a                 | b c  |
| CityA | 11 14        | 16  | 4                  | 5   | 6   |     | 6          | 7   | 8   | 5                 | 6 7  |
| CityB | 9 11         | 14  | 2                  | 3   | 4   |     | 3          | 4   | 5   | 3                 | 4 5  |
| CityC | 34 39        | 45  | 8                  | 9   | 10  |     | 8          | 9   | 10  | 8                 | 9 10 |
| CityD | 32 37        | 43  | 8                  | 9   | 10  |     | 8          | 9   | 10  | 8                 | 9 10 |
| CityE | 18 20        | 23  | 6                  | 7   | 8   |     | 6          | 7   | 8   | 7                 | 8 9  |
| CityF | 16 18        | 20  | 5                  | 6   | 7   |     | 5          | 6   | 7   | 7                 | 8 9  |
| CityG | 14 16        | 18  | 4                  | 5   | 6   |     | 4          | 5   | 6   | 5                 | 6 7  |
| CityH | 20 23        | 25  | 3                  | 4   | 5   |     | 3          | 4   | 5   | 6                 | 7 8  |
| CityI | 29 35        | 41  | 7                  | 8   | 9   |     | 7          | 8   | 9   | 7                 | 8 9  |
| CityJ | 32 37        | 43  | 8                  | 9   | 10  |     | 7          | 8   | 9   | 8                 | 9 10 |
| CityK | 14 16        | 18  | 5                  | 6   | 7   |     | 5          | 6   | 7   | 6                 | 7 8  |
| CityL | 18 20        | 23  | 4                  | 5   | 6   |     | 4          | 5   | 6   | 6                 | 7 8  |
Thiscomprehensiveapproachensuredthattheassessmentreflectedboththefunc-
tionalfeasibilityandthebroaderappealofeachcityasavibrantandwelcomingdestination.
Foreachcityandcriterion,expertsprovidedindividualscoresbasedontheirknowledge,
experience,andtrustedsourcessuchasgovernmentreports,travelerfeedback,andindus-
tryanalyses. Asexpected,theseevaluationsvaried,reflectingdifferingviewpointsand
prioritiesacrossthepanel.
To ensure fairness and consistency, final scores were calculated by averaging the
individualassessmentsforeachcriterionandcity.Theresultingvalueswerethenexpressed
asfuzzynumbers. Thismethodhelpsharmonizediverseopinionsandminimizespotential
bias,yieldingwell-roundedandobjectivescoresforamorebalancedevaluation.
5. ResultsandDiscussion
Inthissection,weapplytheproposedmodels,includingthenewclusteringapproach
andthelogarithmicnormalizationmethod—withintheTOPSISframeworkforthepre-
sentedcasestudy. Theresultsaredetailedstepbystep,thenanalyzedandcomparedwith
thoseobtainedusingtraditionalmethods.
Table4presentstheprocessingofthedatafromTable3. Usingthefuzzynumberof
eachalternativeforeachcriterion,thecorrespondingcentroidiscalculated(columns2to
5),usingEquation(2). ThesecentroidsarethennormalizedusingtheMin–Maxmethod
(columns6to9),usingEquations(3)and(4).
Table4.Normalizedcentroidsforthefourconsideredcriteriaacrossselectedcities.
|       |          |          |          |     |          |            | (C1) |            | (C1) | (C1)       | (C1)       |
| ----- | -------- | -------- | -------- | --- | -------- | ---------- | ---- | ---------- | ---- | ---------- | ---------- |
|       | (C1)     | (C2)     | (C3)     |     | (C4)     |            |      |            |      |            |            |
|       |          |          |          |     |          | Centroid   |      | Centroid   |      | Centroid   | Centroid   |
|       | Centroid | Centroid | Centroid |     | Centroid |            |      |            |      |            |            |
|       |          |          |          |     |          | Normalized |      | Normalized |      | Normalized | Normalized |
| CityA | 14       | 5        | 7        |     | 6        |            | 0.92 |            | 0.33 | 0.6        | 0.4        |
| CityB | 11       | 3        | 4        |     | 4        |            | 1.00 |            | 0.00 | 0          | 0          |
| CityC | 39       | 9        | 9        |     | 9        |            | 0.00 |            | 1.00 | 1          | 1          |
| CityD | 37       | 9        | 9        |     | 9        |            | 0.08 |            | 1.00 | 1          | 1          |
| CityE | 20       | 7        | 7        |     | 8        |            | 0.68 |            | 0.67 | 0.6        | 0.8        |
| CityF | 18       | 6        | 6        |     | 8        |            | 0.76 |            | 0.50 | 0.4        | 0.8        |
| CityG | 16       | 5        | 5        |     | 6        |            | 0.84 |            | 0.33 | 0.2        | 0.4        |
| CityH | 23       | 4        | 4        |     | 7        |            | 0.60 |            | 0.17 | 0          | 0.6        |
| CityI | 35       | 8        | 8        |     | 8        |            | 0.16 |            | 0.83 | 0.8        | 0.8        |
| CityJ | 37       | 9        | 8        |     | 9        |            | 0.08 |            | 1.00 | 0.8        | 1          |
| CityK | 16       | 6        | 6        |     | 7        |            | 0.84 |            | 0.50 | 0.4        | 0.6        |
| CityL | 20       | 5        | 5        |     | 7        |            | 0.68 |            | 0.33 | 0.2        | 0.6        |

Appl.Sci.2025,15,4044
14of21
Thecentroidscalculatedforeachalternativearethenusedtocomputetheirdistances
totheoptimalscoresdefinedforeachcluster,asoutlinedinTable2.
Table5presentsthesedistances,calculatedusingtheEuclideannorm,asspecified
inEquation(5). Asthetableshows,thedistancebetweeneachalternativeandtheideal
cluster values varies. To assign each alternative to a cluster, we select the one with the
minimumdistance,asdescribedinEquation(6). ThefinalcolumninTable5displaysthe
shortestdistanceforeachalternative,withtheassignedclusterhighlightedinbold.
Table5.Evaluationofdistancestothecentroidsofeachcluster.
|       | (C1)Distance | (C2)Distance |      | (C3)Distance |      |     | min  |
| ----- | ------------ | ------------ | ---- | ------------ | ---- | --- | ---- |
| CityA | 0.31         |              | 1.18 |              | 0.46 |     | 0.31 |
| CityB | 0.93         |              | 1.84 |              | 1.11 |     | 0.93 |
| CityC | 1.26         |              | 0.17 |              | 0.92 |     | 0.17 |
| CityD | 1.20         |              | 0.15 |              | 0.87 |     | 0.15 |
| CityE | 0.43         |              | 0.74 |              | 0.23 |     | 0.23 |
| CityF | 0.39         |              | 0.98 |              | 0.34 |     | 0.34 |
| CityG | 0.43         |              | 1.31 |              | 0.57 |     | 0.43 |
| CityH | 0.76         |              | 1.36 |              | 0.74 |     | 0.74 |
| CityI | 0.94         |              | 0.22 |              | 0.57 |     | 0.22 |
| CityJ | 1.13         |              | 0.22 |              | 0.79 |     | 0.22 |
| CityK | 0.21         |              | 1.07 |              | 0.33 |     | 0.21 |
| CityL | 0.50         |              | 1.16 |              | 0.49 |     | 0.49 |
Table6presentstheresultsaggregatedbycluster,revealingadistributionthataligns
wellwiththeintendeddefinitionsofeachgroup.
Table6.Resultofthedistributionofalternativesusingtheproposedclusteringmethod.
|     |     | (C1) |     | (C2) |     | (C3) | (C4) |
| --- | --- | ---- | --- | ---- | --- | ---- | ---- |
Cluster
|       |     | Centroid |     | Centroid |     | Centroid | Centroid |
| ----- | --- | -------- | --- | -------- | --- | -------- | -------- |
| CityA | 1   | 14       |     | 5        |     | 7        | 6        |
| CityB | 1   | 11       |     | 3        |     | 4        | 4        |
| CityG | 1   | 16       |     | 5        |     | 5        | 6        |
| CityK | 1   | 16       |     | 6        |     | 6        | 7        |
| CityC | 2   | 39       |     | 9        |     | 9        | 9        |
| CityD | 2   | 37       |     | 9        |     | 9        | 9        |
| CityI | 2   | 35       |     | 8        |     | 8        | 8        |
| CityJ | 2   | 37       |     | 9        |     | 8        | 9        |
| CityE | 3   | 20       |     | 7        |     | 7        | 8        |
| CityF | 3   | 18       |     | 6        |     | 6        | 8        |
| CityH | 3   | 23       |     | 4        |     | 4        | 7        |
| CityL | 3   | 20       |     | 5        |     | 5        | 7        |
Cluster1—Cost-EffectiveCitieswithModerateInfrastructure—includesalternatives
withthelowestcosts,whiletheothercriteriagenerallyexhibitmoderatevalues,confirming
thecoherenceoftheclassification.
Cluster2—High-InvestmentCitieswithWorld-ClassInfrastructure—comprisesalter-
nativesthatmatchtheprofileofhigh-costcitiesofferingtop-tierscoresininfrastructure,
safety,andaccessibility.
Cluster3—BalancedCitieswithaMixofFeatures—includesalternativeswithinter-
mediatecostlevelsandcriteriaratingsthatfallbetweenthoseofClusters1and2. This
consistencyreinforcesthevalidityoftheproposedclusteringmethod.

Appl.Sci.2025,15,4044
15of21
Basedontheseresults,wecanconcludethattheproposedmodelproducesoutcomes
consistentwithexpectations. Thismeansthatanalyzingthedistributionofalternatives
acrossthedifferentclustersconfirmsthattheresultsarelogicalandalignwiththeexpected
distributionofalternativeswithineachcluster.
Table7comparestheproposedclusteringmethodwiththeFuzzyK-Meansapproach,
revealing that the results are nearly identical—with one notable exception: City K is
assignedtoCluster1bytheproposedmethod,whereasFuzzyK-MeansplacesitinCluster
3. Althoughthisdifferencemayappearminor,ithighlightsanimportantdistinctionin
howeachmethodinterpretsdistancesandassignsalternativestoclusters. Overall, the
strongalignmentbetweenthetwomethodssupportstheeffectivenessandreliabilityofthe
proposedapproachasaviablealternativetotraditionalfuzzyclusteringtechniques.
Table7.ComparisonbetweentheproposedclusteringmethodandtheFuzzyK-Meansmethod,bold
numbershighlightdiscrepanciesbetweenthetwomethods.
| ProposedMethod | FuzzyK-Means |     |
| -------------- | ------------ | --- |
| CityA          | 1            | 1   |
| CityB          | 1            | 1   |
| CityG          | 1            | 1   |
| CityK          | 1            | 3   |
| CityC          | 2            | 2   |
| CityD          | 2            | 2   |
| CityI          | 2            | 2   |
| CityJ          | 2            | 2   |
| CityE          | 3            | 3   |
| CityF          | 3            | 3   |
| CityH          | 3            | 3   |
| CityL          | 3            | 3   |
More importantly, assigning City K to Cluster 1 appears to be a more appropriate
classification. Thecitysharesalow-costprofile,whichisadefiningcharacteristicofCluster
1. In fact, City K has the same cost value as City G, which was placed in Cluster 1 by
theFuzzyK-Meansmethod. Theonlydifferencesbetweenthetwoareminor,suchasa
one-pointvariationinothercriteria—makingthemhighlycomparable.Therefore,grouping
CityKwithCityGinCluster1ismoreconsistentwiththeunderlyinglogicoftheclustering
process. Thissupportstheconclusionthattheproposedmethodoffersamoreaccurateand
contextuallysoundclassification.
Anotherkeyadvantageoftheproposedmethodliesinitssimplicityandcomputa-
tionalefficiencywhencomparedtoFuzzyK-Means,whichdependsonmultipleiterative
calculationsandamorecomplexoptimizationprocess. Incontrast,theproposedmethod
usesadirectandintuitiveapproachbyassigningeachalternativetothenearestcentroid,
eliminating the need for repeated recalculations. Fuzzy K-Means, on the other hand,
involvescontinuousre-evaluationofcentroids,whichincreasescomputationaldemands—
particularly for larger datasets. Additionally, Fuzzy K-Means applies a soft clustering
strategy,wherealternativescanpartiallybelongtomultipleclusters,whereastheproposed
methoddeterministicallyassignseachalternativetoasinglecluster.
In contrast, the proposed method is deterministic, assigning each alternative to a
singleclusterwithoutambiguity. Italsosignificantlyreducescomputationaloverheadby
avoidingiterativeadjustments. Itseaseofimplementationmakesitespeciallypracticalin
contextswherespeedandefficiencyareessential. Consideringthattheoverallclustering
resultsarenearlyidentical—andthattheproposedmethodclassifiesCityKinawaythat

Appl.Sci.2025,15,4044
16of21
alignsmorelogicallywiththedata—itcanberegardedasnotonlysimplerbutalsomore
accurateandreliablethantheFuzzyK-Meansapproach.
In the next step, the rankings of each alternative within their respective clusters
werenormalizedusingtwomethods: logarithmicnormalization(Table8)andMin–Max
normalization(Table9).
Table8.Logarithmicnormalizationresults.
| City  | Cluster | C1   | C2   | C3   | C4   |
| ----- | ------- | ---- | ---- | ---- | ---- |
| CityA | 1       | 0.96 | 0.92 | 1.00 | 0.94 |
| CityB | 1       | 0.88 | 0.71 | 0.77 | 0.77 |
| CityG | 1       | 1.00 | 0.92 | 0.86 | 0.94 |
| CityK | 1       | 1.00 | 1.00 | 0.94 | 1.00 |
| CityC | 2       | 1.00 | 1.00 | 1.00 | 1.00 |
| CityD | 2       | 0.99 | 1.00 | 1.00 | 1.00 |
| CityI | 2       | 0.97 | 0.95 | 0.95 | 0.95 |
| CityJ | 2       | 0.99 | 1.00 | 0.95 | 1.00 |
| CityE | 3       | 0.96 | 1.00 | 1.00 | 1.00 |
| CityF | 3       | 0.93 | 0.94 | 0.94 | 1.00 |
| CityH | 3       | 1.00 | 0.77 | 0.77 | 0.95 |
| CityL | 3       | 0.96 | 0.86 | 0.86 | 0.95 |
Table9.Min–Maxnormalizationresults.
| City  | Cluster | C1   | C2   | C3   | C4   |
| ----- | ------- | ---- | ---- | ---- | ---- |
| CityA | 1       | 0.60 | 0.67 | 1.00 | 0.67 |
| CityB | 1       | 0.00 | 0.00 | 0.00 | 0.00 |
| CityG | 1       | 1.00 | 0.67 | 0.33 | 0.67 |
| CityK | 1       | 1.00 | 1.00 | 0.67 | 1.00 |
| CityC | 2       | 1.00 | 1.00 | 1.00 | 1.00 |
| CityD | 2       | 0.50 | 1.00 | 1.00 | 1.00 |
| CityI | 2       | 0.00 | 0.00 | 0.00 | 0.00 |
| CityJ | 2       | 0.50 | 1.00 | 0.00 | 1.00 |
| CityE | 3       | 0.40 | 1.00 | 1.00 | 1.00 |
| CityF | 3       | 0.00 | 0.67 | 0.67 | 1.00 |
| CityH | 3       | 1.00 | 0.00 | 0.00 | 0.00 |
| CityL | 3       | 0.40 | 0.33 | 0.33 | 0.00 |
AnanalysisofTables8and9showsthatlogarithmicnormalizationoffersclearad-
vantagesoverMin–Maxnormalization,particularlyinthewayitdistributesvaluesacross
clusters. In Cluster 2, where the cost criterion (C1) exhibits significantly higher values
thaninotherclusters,Min–Maxnormalizationexaggeratesthesedifferences,makingcost
variationsbetweencitiesappearmorepronounced. Incontrast, logarithmicnormaliza-
tioncompressesthescale,reducingthegapsbetweenalternativeswhilepreservingtheir
relativerankings.
A similar effect is observed in Cluster 3, where differences in cost (C1) and infras-
tructure(C2)aremoreevenlybalancedunderlogarithmictransformation. Thisprevents
extreme values from overshadowing smaller differences. As a result, logarithmic nor-
malizationdeliversamorebalancedrepresentation, ensuringthatnosinglehighvalue
disproportionatelyinfluencestheoutcome—thusproducingamorestableandinterpretable
rankingsystem.
The next step is the application of the TOPSIS method to the normalized tables
(Tables8and9),consideringtheweightsforeachcriterionandeachcluster,aspresentedin

Appl.Sci.2025,15,4044
17of21
Table10. Theseweightsarederivedfromtheoptimalvalueswithineachclusterandare
essentiallyobtainedbynormalizingthesevaluesusingtheMin–Maxmethod.
Table10.Criterionweightsforeachcluster.
|         | (C1)Cluster | (C2)Cluster | (C3)Cluster | (C4)Cluster |          |          |          |          |
| ------- | ----------- | ----------- | ----------- | ----------- | -------- | -------- | -------- | -------- |
| Cluster |             |             |             |             | WeightC1 | WeightC2 | WeightC3 | WeightC4 |
|         | Centroid    | Centroid    | Centroid    | Centroid    |          |          |          |          |
| 1       | 1.0         | 0.6         | 0.5         | 0.5         | 0.38     | 0.23     | 0.19     | 0.19     |
| 2       | 0.1         | 0.9         | 1.0         | 0.9         | 0.03     | 0.32     | 0.34     | 0.31     |
| 3       | 0.6         | 0.6         | 0.6         | 0.6         | 0.25     | 0.25     | 0.25     | 0.25     |
TheTOPSISmethodwasthenappliedusingtheweightsderivedforeachcluster(as
showninTable10)andthenormalizeddatafrombothapproaches. Table11presentsthe
results obtained using logarithmic normalization, ranking the alternatives within their
respectiveclusters. Table12showstheresultsusingMin–Maxnormalization,allowingfor
adirectcomparisonbetweenthetwonormalizationtechniques.
Table11.TOPSISresultsusinglogarithmicnormalization,boldnumbersindicatethebestalternative
withineachclusteridentifiedbythemethod.
| City  | Cluster | C1   | C2   | C3   | C4   | D+   | D-   | TOPSISScore |
| ----- | ------- | ---- | ---- | ---- | ---- | ---- | ---- | ----------- |
| CityA | 1       | 0.36 | 0.21 | 0.19 | 0.18 | 0.03 | 0.08 | 0.74        |
| CityB | 1       | 0.33 | 0.16 | 0.15 | 0.15 | 0.10 | 0.00 | 0.00        |
| CityG | 1       | 0.38 | 0.21 | 0.16 | 0.18 | 0.03 | 0.08 | 0.69        |
| CityK | 1       | 0.38 | 0.23 | 0.18 | 0.19 | 0.01 | 0.10 | 0.89        |
| CityC | 2       | 0.03 | 0.32 | 0.34 | 0.31 | 0.00 | 0.03 | 1.00        |
| CityD | 2       | 0.03 | 0.32 | 0.34 | 0.31 | 0.00 | 0.03 | 0.98        |
| CityI | 2       | 0.03 | 0.31 | 0.32 | 0.30 | 0.03 | 0.00 | 0.00        |
| CityJ | 2       | 0.03 | 0.32 | 0.32 | 0.31 | 0.02 | 0.02 | 0.57        |
| CityE | 3       | 0.24 | 0.25 | 0.25 | 0.25 | 0.01 | 0.08 | 0.89        |
| CityF | 3       | 0.23 | 0.23 | 0.23 | 0.25 | 0.03 | 0.06 | 0.67        |
| CityH | 3       | 0.25 | 0.19 | 0.19 | 0.24 | 0.08 | 0.02 | 0.18        |
| CityL | 3       | 0.24 | 0.22 | 0.22 | 0.24 | 0.05 | 0.03 | 0.38        |
Table12.TOPSISresultsusingMin–Maxnormalization,boldnumbersindicatethebestalternative
withineachclusteridentifiedbythemethod.
| City  | Cluster | C1   | C2   | C3   | C4   | D+   | D-   | TOPSISScore |
| ----- | ------- | ---- | ---- | ---- | ---- | ---- | ---- | ----------- |
| CityA | 1       | 0.23 | 0.15 | 0.19 | 0.13 | 0.18 | 0.36 | 0.66        |
| CityB | 1       | 0.00 | 0.00 | 0.00 | 0.00 | 0.52 | 0.00 | 0.00        |
| CityG | 1       | 0.38 | 0.15 | 0.06 | 0.13 | 0.16 | 0.43 | 0.73        |
| CityK | 1       | 0.38 | 0.23 | 0.13 | 0.19 | 0.06 | 0.50 | 0.89        |
| CityC | 2       | 0.03 | 0.32 | 0.34 | 0.31 | 0.00 | 0.56 | 1.00        |
| CityD | 2       | 0.02 | 0.32 | 0.34 | 0.31 | 0.02 | 0.56 | 0.97        |
| CityI | 2       | 0.00 | 0.00 | 0.00 | 0.00 | 0.56 | 0.00 | 0.00        |
| CityJ | 2       | 0.02 | 0.32 | 0.00 | 0.31 | 0.34 | 0.45 | 0.57        |
| CityE | 3       | 0.10 | 0.25 | 0.25 | 0.25 | 0.15 | 0.44 | 0.75        |
| CityF | 3       | 0.00 | 0.17 | 0.17 | 0.25 | 0.28 | 0.34 | 0.55        |
| CityH | 3       | 0.25 | 0.00 | 0.00 | 0.00 | 0.43 | 0.25 | 0.37        |
| CityL | 3       | 0.10 | 0.08 | 0.08 | 0.00 | 0.37 | 0.15 | 0.29        |
TheapplicationoftheTOPSISmethodusingbothMin–Maxandlogarithmicnormal-
ization identified the top-ranked cities within each cluster. The results show that City
K(Cluster1)andCityC(Cluster2)consistentlyachievedthehighestscoresacrossboth
normalizationmethods,whileCityE(Cluster3)exhibitedsomevariationdependingon
thetechniqueused.

Appl.Sci.2025,15,4044 18of21
InCluster1,CityKemergedasthebest-performingalternative,withaTOPSISscore
of approximately 0.887 in both cases. This indicates that City K offers a well-balanced
combinationofcost,infrastructure,safety,andaccessibility,makingitthemostsuitable
option within its group. Its consistent ranking across both normalization techniques
demonstratesstrongalignmentwiththecluster’sidealconditions.
InCluster2,CityCachievedaperfectTOPSISscoreof1.000underbothnormalization
methods, confirming its status as the most suitable alternative for this category. The
unchangedresult,regardlessofthenormalizationapplied,reinforcesCityC’sdominance
intermsofmeetingallweightedcriteria.
Incontrast,CityEledCluster3butshowednoticeablevariationbetweenmethods:
0.747usingMin–Maxand0.886withlogarithmicnormalization. Thisdifferencesuggests
thatthelogarithmicapproachwasmoreeffectiveinsmoothingextremevaluesandreducing
theinfluenceofoutliers. Asaresult,CityEappearedclosertotheidealsolutionunder
logarithmicnormalization.
Overall,theconsistencyofCityKandCityCastop-rankedalternativesreinforcesthe
robustnessofthemethodologyandconfirmsthatthechosencriteriaeffectivelydistinguish
the best-performing cities within each cluster. However, the variation in City E’s score
highlightshownormalizationcaninfluencerankingintensity,particularlyindatasetswhere
differencesbetweenvaluesaremorepronounced.
The results show that logarithmic and Min–Max normalizations produced nearly
identicaloutcomesintheTOPSISanalysis,indicatingthatwhentherearenosignificant
outliers,logarithmicnormalizationperformsjustaswellastheMin–Maxmethod.However,
inthepresenceofextremevalues,logarithmicnormalizationprovestobemoreeffective,as
itreducestheimpactofoutliersandpreventscriteriawithveryhighvaluesfromdistorting
thedistancecalculationsinTOPSIS.
Thus, it is observed that for datasets without outliers, logarithmic normalization
performsjustaswellasMin–Maxnormalization, withtheaddedadvantagethatwhen
outliersarepresent,logarithmicnormalizationdeliversbetterperformance. Ifthegoalis
toensurethatnormalizationhasameaningfuleffectonlyincaseswheredatavariationis
large,logarithmicnormalizationispreferableduetoitsabilitytosmoothextremevalues.
However,whenthedataarenaturallywell-distributed,Min–Maxnormalizationremainsa
validoption,asitpreservestheoriginalproportionswithoutinformationloss.
6. Conclusions
This study introduced two methodological innovations to enhance the TOPSIS
decision-makingframework: ClusteringUsingFuzzyNumbersandCentroid-BasedDis-
tance Allocation and logarithmic normalization. Together, these methods address key
limitationsintraditionalMCDMapproaches,particularlyinthehandlingofuncertainty,
outliers,andrigiddata-drivenclassifications.
The proposed clustering approach allows decision-makers to define ideal cluster
profilesindependentlyofthedataset,enablinggreaterstrategiccontrol. Fuzzynumbers
are used exclusively to model uncertainty in the evaluation of alternatives, which are
thenconvertedtocrispvaluestocalculateEuclideandistancesfrompredefinedcentroids.
This results in a robust yet transparent classification method, free from iterative opti-
mizationorprobabilisticmembershipfunctions. Unliketraditionalclusteringtechniques
suchasK-Means,whichderivecentroidsfromdata,ourapproachdecouplesclustering
fromdatadistributionandfocusesonalignmentwithidealizedprofiles—offeringgreater
interpretabilityandconsistency.
LogarithmicnormalizationfurtherenhancestherobustnessoftheTOPSISmethodby
smoothingextremevaluesandpreservingproportionaldifferencesacrosscriteria.Thisises-

Appl.Sci.2025,15,4044 19of21
peciallyusefulindatasetswithhighvarianceornon-lineardistributions,wheretraditional
normalizationtechniquesmaydistortrankings.
The case study results demonstrate that the proposed methodologies significantly
enhanceboththeaccuracyandstabilityofdecision-makingoutcomes. Thefuzzyclustering
approachenablesmorerealisticclassificationofalternatives,whilelogarithmicnormaliza-
tionimprovesthecomparabilityofcriteria—withoutaddingunnecessarycomplexity.Akey
advantageofbothmethodsistheircomputationalsimplicityandeaseofimplementation,
makingthemaccessibleforabroadrangeofpracticalapplications.
Beyond the context of city selection, the proposed methodology offers broader en-
hancementstodecision-makingbyimprovinghowalternativesaregroupedandcompared
inthepresenceofuncertaintyandvariability. Itsmodulardesign—combiningfuzzy-based
evaluation,predefinedclustercentroids,andadaptivenormalization—makesitsuitable
for various domains such as supply chain optimization, financial assessment, environ-
mentalplanning,andstrategicprojectprioritization. Themethodsupportsmorerobust,
context-aware,andscalabledecisionprocessesacrossdiversereal-worldapplications.
Although the results are promising, there remain several opportunities for further
explorationandvalidation.Alogicalnextstepistotesttheperformanceofthesetechniques
withinotherMCDMmodels—suchasVIKOR,PROMETHEE,andAHP—toassesstheir
adaptabilityacrossdifferentdecision-makingframeworks.Eachofthesemodelshasunique
characteristics,andapplyingtheproposedmethodswithinthemcouldofferdeeperinsights
intotheirgeneralizabilityandeffectiveness.
Despiteitspromisingresults,theproposedmethodologypresentssomelimitations.
The definition of ideal cluster centroids is currently based on expert judgment, which,
whileofferingflexibilityandinterpretability,mayintroduceadegreeofsubjectivity. Fu-
turerefinementscouldexplorehybridordata-assistedstrategiestosupportorvalidate
thesepredefinedprofiles. Additionally,whilethemethodiscomputationallysimpleand
effectiveinthecasestudy,itsperformanceinlarge-scaleorhigh-dimensionalproblems
remainstobetested. Moreover,althoughtheproposedapproachwasappliedwithinthe
TOPSIS framework, evaluating its integration with other MCDM models (e.g., VIKOR,
PROMETHEE,AHP)wouldhelpassessitsgeneralizability.
Finally,futureworkcouldinvolvebenchmarkingtheproposedmethodsagainstother
clusteringandnormalizationtechniques. Comparativeanalysesfocusedonclassification
accuracy,rankingstability,andcomputationalefficiencywouldfurthersupportmethod
refinementandfosterbroaderadoptionincomplexdecision-makingcontexts.
AuthorContributions:Conceptualization,V.A.andA.A.;methodology,V.A.;software,V.A.;vali-
dation,V.A.andA.A.;formalanalysis,V.A.;investigation,V.A.;resources,V.A.;datacuration,V.A.;
writing—originaldraftpreparation,V.A.;writing—reviewandediting,A.A.;visualization,A.A.;
supervision,V.A.;projectadministration,V.A.;fundingacquisition,A.A.Allauthorshavereadand
agreedtothepublishedversionofthemanuscript.
Funding:Thisresearchreceivednoexternalfunding.
InstitutionalReviewBoardStatement:Notapplicable.
InformedConsentStatement:Notapplicable.
DataAvailabilityStatement:Theoriginalcontributionspresentedinthestudyareincludedinthe
article;furtherinquiriescanbedirectedtothecorrespondingauthors.
Acknowledgments: TheauthorsgratefullyacknowledgethesupportfromFCT–Fundaçãoparaa
CiênciaeTecnologia(PortugueseFoundationforScienceandTechnology),throughIDMEC,under
LAETABaseFunding(DOI:10.54499/UIDB/50022/2020).
ConflictsofInterest:Theauthorsdeclarenoconflictsofinterest.

Appl.Sci.2025,15,4044 20of21
References
1. Štilic´,A.;Puška,A.IntegratingMulti-CriteriaDecision-MakingMethodswithSustainableEngineering:AComprehensiveReview
ofCurrentPractices.Eng2023,4,1536–1549.[CrossRef]
2. Hajduk,S.;Jelonek,D.ADecision-MakingApproachBasedonTOPSISMethodforRankingSmartCitiesintheContextofUrban
Energy.Energies2021,14,2691.[CrossRef]
3. Madi,E.N.;Zakaria,Z.A.;Sambas,A.;Sukono.TowardEffectiveUncertaintyManagementinDecision-MakingModelsBasedon
Type-2FuzzyTOPSIS.Mathematics2023,11,3512.[CrossRef]
4. Cai,M.;Hong,Y.ImprovedTOPSISMethodConsideringFuzzinessandRandomnessinMulti-AttributeGroupDecisionMaking.
Mathematics2022,10,4200.[CrossRef]
5. Sałabun,W.;Wa˛tróbski,J.;Shekhovtsov,A.AreMCDAMethodsBenchmarkable? AComparativeStudyofTOPSIS,VIKOR,
COPRAS,andPROMETHEEIIMethods.Symmetry2020,12,1549.[CrossRef]
6. Vakilipour,S.;Sadeghi-Niaraki,A.;Ghodousi,M.;Choi,S.-M.ComparisonbetweenMulti-CriteriaDecision-MakingMethods
andEvaluatingtheQualityofLifeatDifferentSpatialLevels.Sustainability2021,13,4067.[CrossRef]
7. Qureshi, A.M.; Rachid, A. Comparative Analysis of Multi-Criteria Decision-Making Techniques for Outdoor Heat Stress
Mitigation.Appl.Sci.2022,12,12308.[CrossRef]
8. Lim,Z.-Y.;Ong,L.-Y.;Leow,M.-C.AReviewonClusteringTechniques:CreatingBetterUserExperienceforOnlineRoadshow.
FutureInternet2021,13,233.[CrossRef]
9. Krasnov,D.;Davis,D.;Malott,K.;Chen,Y.;Shi,X.;Wong,A.FuzzyC-MeansClustering:AReviewofApplicationsinBreast
CancerDetection.Entropy2023,25,1021.[CrossRef]
10. Al-Augby,S.;Majewski,S.;Majewska,A.;Nermend,K.AComparisonOfK-MeansAndFuzzyC-MeansClusteringMethods
ForASampleOfGulfCooperationCouncilStockMarkets.FoliaOeconomicaStetin.2014,14,19–36.[CrossRef]
11. Ghadiri,N.;Ghaffari,M.;Nikbakht,M.A.BigFCM:Fast,PreciseandScalableFCMonHadoop. arXiv2016,arXiv:1605.03047.
[CrossRef]
12. Chen,Y.;Zhou,S.RevisitingPossibilisticFuzzyC-MeansClusteringUsingtheMajorization-MinimizationMethod.Entropy2024,
26,670.[CrossRef][PubMed]
13. Chan,K.Y.;Yiu,K.F.C.;Kim,D.;Abu-Siada,A.FuzzyClustering-BasedDeepLearningforShort-TermLoadForecastinginPower
GridSystemsUsingTime-VaryingandTime-InvariantFeatures.Sensors2024,24,1391.[CrossRef]
14. Vafaei,N.;Ribeiro,R.A.;Matos,L.M.C.DataNormalizationTechniquesinDecisionMaking:CaseStudywithTOPSISMethod.
IJIDS2018,10,19.[CrossRef]
15. Aytekin,A.ComparativeAnalysisoftheNormalizationTechniquesintheContextofMCDMProblems.Decis.Mak.Appl.Manag.
Eng.2021,4,1–25.[CrossRef]
16. Vafaei,N.;Ribeiro,R.A.;Camarinha-Matos,L.M.ComparisonofNormalizationTechniquesonDataSetswithOutliers. Int.
J.Decis.SupportSyst.Technol.2021,14,1–17.[CrossRef]
17. Vafaei,N.;Ribeiro,R.A.;Camarinha-Matos,L.M.NormalizationTechniquesforMulti-CriteriaDecisionMaking: Analytical
HierarchyProcessCaseStudy.InTechnologicalInnovationforCyber-PhysicalSystems;Camarinha-Matos,L.M.,Falcão,A.J.,Vafaei,
N.,Najdi,S.,Eds.;SpringerInternationalPublishing:Cham,Switzerland,2016;Volume470,pp.261–269;ISBN978-3-319-31164-7.
18. Zavadskas,E.K.;Turskis,Z.ANewLogarithmicNormalizationMethodinGamesTheory.Informatica2008,19,303–314.[CrossRef]
19. Sahu,S.K.AStudyofK-MeansandC-MeansClusteringAlgorithmsforIntrusionDetectionProductDevelopment.Int.J.Innov.
Manag.Technol.2014,5,207–213.[CrossRef]
20. Ikotun,A.M.;Ezugwu,A.E.;Abualigah,L.;Abuhaija,B.;Heming,J.K-MeansClusteringAlgorithms:AComprehensiveReview,
VariantsAnalysis,andAdvancesintheEraofBigData.Inf.Sci.2023,622,178–210.[CrossRef]
21. Zolfani,S.;Yazdani,M.;Pamucar,D.;Zaraté,P.AVIKORandTOPSISFocusedReanalysisoftheMADMMethodsBasedon
LogarithmicNormalization.arXiv2020,arXiv:2006.08150.[CrossRef]
22. Magableh,G.M.;Mistarihi,M.Z.AnIntegratedFuzzyMCDMMethodforAssessingCrisisRecoveryStrategiesintheSupply
Chain.Sustainability2024,16,2383.[CrossRef]
23. Nabeeh,N.A.;Abdel-Basset,M.;Gamal,A.;Chang,V.EvaluationofProductionofDigitalTwinsBasedonBlockchainTechnology.
Electronics2022,11,1268.[CrossRef]
24. Xia,J.-Y.;Li,S.;Huang,J.-J.;Yang,Z.;Jaimoukha,I.M.;Gündüz,D.Metalearning-BasedAlternatingMinimizationAlgorithmfor
NonconvexOptimization.IEEETrans.NeuralNetw.Learn.Syst.2023,34,5366–5380.[CrossRef]
25. An,X.-K.;Du,L.;Jiang,F.;Zhang,Y.-J.;Deng,Z.-C.;Kurths,J.AFew-ShotIdentificationMethodforStochasticDynamical
SystemsBasedonResidualMultipeaksAdaptiveSampling.ChaosInterdiscip.J.NonlinearSci.2024,34,073118.[CrossRef]
26. Fang,P.;Gao,Z.;Tsay,R.S.SupervisedKernelPrincipalComponentAnalysisforForecasting.Financ.Res.Lett.2023,58,104292.
[CrossRef]
27. Yang,R.-S.;Li,H.-B.;Huang,H.-Z.MultisourceInformationFusionConsideringtheWeightofFocalElement’sBeliefs:AGaussian
KernelSimilarityApproach.Meas.Sci.Technol.2024,35,025136.[CrossRef]

Appl.Sci.2025,15,4044 21of21
28. Jin,H.;Tian,S.;Hu,J.;Zhu,L.;Zhang,S.RobustRatio-TypedTestforLocationChangeunderStrongMixingHeavy-TailedTime
SeriesModel.Commun.Stat.-TheoryMethods2025,1–24.[CrossRef]
29. Zhou,M.;Zhao,X.;Luo,F.;Luo,J.;Pu,H.;Xiang,T.RobustRGB-TTrackingviaAdaptiveModalityWeightCorrelationFilters
andCross-ModalityLearning.ACMTrans.Multimed.Comput.Commun.Appl.2024,20,1–20.[CrossRef]
30. Peng,Y.; Zhao,Y.; Dong,J.; Hu,J.AdaptiveOpinionDynamicsoverCommunityNetworksWhenAgentsCannotExpress
OpinionsFreely.Neurocomputing2025,618,129123.[CrossRef]
31. Zhu,C.AnAdaptiveAgentDecisionModelBasedonDeepReinforcementLearningandAutonomousLearning.J.Logist.Inform.
Serv.Sci.2023,10,107–118.[CrossRef]
Disclaimer/Publisher’sNote: Thestatements, opinionsanddatacontainedinallpublicationsaresolelythoseoftheindividual
author(s)andcontributor(s)andnotofMDPIand/ortheeditor(s).MDPIand/ortheeditor(s)disclaimresponsibilityforanyinjuryto
peopleorpropertyresultingfromanyideas,methods,instructionsorproductsreferredtointhecontent.