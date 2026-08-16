---
conversion_metadata:
  converted_at: "2026-07-21T08:13:56Z"
  converter_tool: "markitdown"
  converter_version: "0.1.6"
  source_pdf: "Rabinovich et al.pdf"
  source_pdf_sha256: "194096a3a32f2c41bf4357649f4283246210d9b6adbb55d342b22f12c83b46a4"
  page_count: 67
  markdown_char_count: 243587
---

<!-- PAGE-AWARE EXTRACTION (via pdfminer.six) -->

<!-- PAGE 1 -->

Mapping Financial Mindsets: A Two-Stage Unsupervised Framework for Behavioral

Proﬁling Using High-Dimensional Psychometric Data

Irina Rabinovich1, Rikki Rabinovich2, Nick Ashburn1,3, Moraya DeGeare1,4

Abstract

Financial well-being reﬂects a complex interplay of psychological traits, behaviors, and

knowledge, yet most segmentation approaches rely on limited indicators such as spending

patterns or socio-demographic data, overlooking behavioral and psychometric factors. This paper

proposes a novel methodological framework for psychometric segmentation that models complex

interactions across multiple psychometric domains, enabling the identiﬁcation of latent proﬁles

of ﬁnancial mindset and behavior. We demonstrate the utility of the framework by applying it to

two distinct datasets--a proprietary ﬁnancial assessment (N = 337) and the nationally

representative U.S. CFPB Financial Well-Being Survey (N = 5,897). In both applications, the

approach yields psychologically interpretable proﬁles, exhibits strong internal stability, and

shows consistent associations with life satisfaction, psychological well-being, and ﬁnancial

health. Rather than prescribing a single population taxonomy, our goal is to provide a replicable

and scalable procedure for identifying meaningful behavioral patterns within any ﬁnancial

population. This makes the approach well suited to behavioral ﬁnance applications including

ﬁnancial advising, wellness interventions, and the design of personalized tools and

communications aimed at improving ﬁnancial decision-making and well-being.

1. Introduction

Financial well-being is increasingly recognized as a multidimensional construct that includes not

only objective indicators, such as income, savings, and debt, but also subjective experiences,

1 Calibrate, Inc; 2 Department of Neurosurgery, University of Utah; 3 Drexel University, 4 BFF Therapy

---

<!-- PAGE 2 -->

including ﬁnancial stress, conﬁdence, and perceived control (Brüggen et al., 2017; CFPB, 2015a;

Netemeyer et al., 2018). It reﬂects both behavioral and psychological aspects, demanding

assessment tools that go beyond ﬁnancial conditions to account for beliefs, motivations, and

emotional responses. Traditional methods for classifying individuals in the ﬁnancial domain have

typically relied on spending patterns or demographic factors and have therefore often overlooked

the psychological patterns that inﬂuence how individuals perceive, relate to, and manage their

ﬁnances. Here, we deﬁne ﬁnancial mindset as a multidimensional construct where capability,

motivation, psychological resources, and enacted behavior intersect to shape decision-making.

This perspective aligns with our clustering framework, which seeks to identify patterns in how

these dimensions co-occur across individuals. The resulting clusters represent distinct proﬁles of

how individuals organize and regulate their ﬁnancial lives.

This paper makes three contributions. First, it addresses the challenge of modeling

multifaceted psychological constructs and their interdependencies in behavioral proﬁling. To this

end, it introduces a methodological framework that integrates domain-speciﬁc manifold learning

with spectral clustering to identify nonlinear patterns in psychometric and behavioral data.

Second, it tests the framework across two distinct datasets--one proprietary and psychometrically

rich, the other large-scale and nationally representative -- demonstrating how this framework

reveals psychologically coherent patterns of ﬁnancial mindsets that are not captured by

conventional linear or demographic segmentation approaches. Third, as the results of the

application to the two distinct datasets show, it provides preliminary evidence that the proposed

approach reveals  a reliable underlying structure – showing consistent separability and stability

across diﬀerent instruments, populations, and survey formats, even if the speciﬁc proﬁles diﬀer.

Applying this two-stage unsupervised learning framework, we identify emergent

1

---

<!-- PAGE 3 -->

behavioral proﬁles that capture complex nonlinear relationships missed by standard

factor-analytic or demographic approaches. We evaluate these proﬁles internally using structural

metrics of cluster coherence and externally by demonstrating robust associations with outcome

indicators, namely, life satisfaction, psychological well-being, and ﬁnancial health. We also show

that these external indicators are far more strongly associated with the learned proﬁles than with

socio-demographic variables such as age, education, or income, underscoring the distinctive

value of psychometric and behavioral dimensions for understanding heterogeneity in ﬁnancial

well-being. Finally, we show that demographic variables alone provide only limited predictive

power for cluster membership, indicating that the framework captures behavioral–psychological

structure that is not reducible to age, income, or education.

To demonstrate the utility of the proposed framework, we apply it to two very diﬀerent

datasets: a proprietary assessment with deep psychometric coverage and the U.S. CFPB

Financial Well-Being Survey, which uses a diﬀerent item structure and response format. Despite

these diﬀerences, the approach consistently identiﬁes interpretable, psychologically coherent

proﬁles that share a common structural organization and exhibit strong internal structure and

meaningful associations with external outcomes.

By decoupling the modeling methodology from any speciﬁc survey instrument, the

framework opens the door to scalable application for academic research, personalized ﬁntech

solutions, and even clinical applications where ﬁnancial behavior may inform intervention

strategies.

2. Background & Related Work

In this section we review core concepts from behavioral ﬁnance and psychometrics that underpin

our framework. We also highlight relevant applications of machine learning in the behavioral

2

---

<!-- PAGE 4 -->

sciences and examine prior attempts to assess ﬁnancial well-being through multidimensional

measurement.

2.1 Behavioral Finance and Psychometrics

Behavioral ﬁnance integrates psychological theories into economic models to better explain

real-world ﬁnancial decision-making, recognizing that individuals are often inﬂuenced by

cognitive biases, emotions, and heuristics rather than strict rationality (Kahneman & Tversky,

1979). Psychometric approaches complement this perspective by using validated instruments to

quantify individual diﬀerences in traits such as risk tolerance, ﬁnancial anxiety, and internalized

money beliefs or “scripts” (Grable & Joo, 2004; Klontz et al., 2011; Lown, 2011).

A growing body of evidence shows that psychological traits, like self-control, optimism,

and emotional regulation, are strongly associated with ﬁnancial behaviors (e.g., saving, spending,

and investing) and contribute to broader measures of well-being (Gathergood, 2012; Shim et al.,

2009; Xiao & O’Neill, 2016). Perceived psychological power has also been shown to promote

ﬁnancial behaviors like saving, highlighting the aﬀective and motivational dimensions of

ﬁnancial decision-making (Garbinsky et al., 2014). The integration of psychometrics into

ﬁnancial assessments improves the predictive accuracy of ﬁnancial health outcomes by capturing

psychological contributors beyond ﬁnancial variables alone (Serido et al., 2013). Building on this

foundation, our work fuses self-reported ﬁnancial behavior constructs with multidimensional

psychological traits into a uniﬁed representation, enabling more precise behavioral proﬁling than

isolated domain-speciﬁc approaches.

2.2 Clustering and Dimensionality Reduction in Behavioral Sciences

Unsupervised learning methods have become increasingly valuable in the behavioral sciences,

enabling researchers to uncover natural groupings within complex behavioral datasets (Kaufman

3

---

<!-- PAGE 5 -->

& Rousseeuw, 2009; Yarkoni & Westfall, 2017; Zhang, 2021). In ﬁnance, these techniques have

primarily been applied to behavioral segmentation based on observable ﬁnancial actions, credit

risk modeling, and product targeting (Nazareth, 2023). Dimensionality reduction methods such

as Principal Component Analysis (PCA) and Uniform Manifold Approximation and Projection

(UMAP1) aid in simplifying high-dimensional datasets while preserving structure relevant to

clustering (Jolliﬀe, 2002; McInnes et al., 2018). Combinations of nonlinear embedding and

graph-based clustering have been successfully applied in other domains, including genomics

(Becht et al., 2019), psychiatry (Marquand et al., 2016), and health informatics (Miotto et al.,

2016), where they have enabled the discovery of complex latent structure that is diﬃcult to

recover with linear or centroid-based methods. However, applications of these approaches to

ﬁnancial–psychometric segmentation remain limited.

Unsupervised learning is particularly appealing in contexts where ground-truth labels are

unavailable or poorly deﬁned, allowing researchers to detect latent patterns inherent in the data.

In the context of our study, these methods can reveal psychologically meaningful proﬁles,

especially when working with rich psychometric or behavioral data that is diﬃcult to analyze

directly.  However, critiques of unsupervised methods note their sensitivity to parameter choices,

potential instability across diﬀerent samples, and challenges in validating clusters against

external criteria (Şenbabaoğlu et al., 2014; von Luxburg, 2010). We address these concerns

through internal validation metrics, external outcome associations, and replication across

independent samples with diﬀerent survey structures.

Recent studies have successfully applied unsupervised methods to reveal latent structure in

1 A dimensionality reduction technique that transforms high-dimensional data (e.g., multiple questionnaire scores) into a lower-dimensional 
representation while preserving underlying structure. It facilitates pattern recognition and visualization.

4

---

<!-- PAGE 6 -->

other (not ﬁnancial) psychological domains. For example, Hofman et al. (2023) used hierarchical

clustering to identify stable subtypes of depression and anxiety symptoms in a large-scale

population study, while Mõttus et al. (2017) demonstrated the predictive utility of ﬁne-grained

personality trait clustering for life outcomes.  These studies highlight the potential of clustering

to uncover psychologically meaningful proﬁles that support both explanatory modeling and

tailored interventions. We go beyond these innovations and apply UMAP and Spectral Clustering

to integrated psychometric and self-reported ﬁnancial behavior data, generating psychologically

interpretable behavioral-ﬁnancial proﬁles grounded in latent structure.

2.3 Prior Approaches to Financial Well-Being Assessment

While traditional assessments of ﬁnancial well-being have evolved to include subjective

indicators such as ﬁnancial stress, perceived control, and self-eﬃcacy (CFPB, 2015b; Netemeyer

et al., 2018), they remain limited in psychological scope. Tools like the CFPB Financial

Well-Being Scale and the InCharge Distress Scale (Prawitz et al., 2006), though

psychometrically strong (α ≈ 0.87), primarily assess emotional strain and perceived hardship.

They omit motivational drivers, behavioral consistency, and self-regulatory capacity. Similarly,

ﬁnancial literacy assessments such as the OECD/INFE Toolkit (Atkinson & Messy, 2012)

emphasize knowledge but not emotional readiness to act. This is a critical omission, since traits

like impulsivity, perseverance, and low self-eﬃcacy often inhibit behavior change, regardless of

knowledge.

Psychological constructs such as locus of control, psychological capital, and ﬁnancial

self-eﬃcacy have been linked to ﬁnancial behaviors (Grable & Joo, 2004; Lown, 2011; Serido et

al., 2013), but they are typically modeled in isolation or examined using supervised methods.

This obscures how multiple traits co-occur in practice and limits the discovery of latent

5

---

<!-- PAGE 7 -->

psychological conﬁgurations. Machine learning in ﬁntech, while increasingly common (Das &

Nayak, 2022; Zhang, 2021), prioritizes what users do (observable output) over why they do it

(internal psychological structure), limiting the ability to predict how ﬁnancial stress will impact

decision-making.

The present study addresses these limitations by clustering a comprehensive set of

psychometric and behavioral measures to reveal interpretable ﬁnancial well-being proﬁles. By

modeling the co-occurrence structure across domains, the framework uncovers psychologically

meaningful patterns that are diﬃcult to detect using linear or domain-isolated approaches. These

proﬁles do not represent ﬁxed “types” but rather data-driven conﬁgurations that capture how

traits, behaviors, and motivations align within and across individuals. This structure enables

richer descriptive insight, supports hypothesis generation for future theory-building, and can

inform targeted interventions in ﬁnancial advising and wellness contexts.

3. Framework Overview

The framework begins by organizing questionnaire items into conceptually coherent domains,

each representing a distinct psychological or behavioral construct (e.g., motivation, planning,

ﬁnancial literacy). Domain partitioning is essential because psychometric surveys typically

contain a heterogeneous mix of measurement formats--binary indicators, multi-level Likert

items, and scales with diﬀerent response ranges. Even when items are rescaled to a common

numeric range, the combined item space remains geometrically inconsistent: binary items create

abrupt, discontinuous jumps in response patterns; Likert items introduce smooth graded

variation; and items from unrelated constructs add uncorrelated or orthogonal sources of

variance. When these heterogeneous items are analyzed or clustered directly at the item level, the

resulting structure is often dominated by measurement artifacts rather than underlying behavioral

6

---

<!-- PAGE 8 -->

organization, leading to clusters that change unpredictably across seeds or algorithms. Indeed, we

are unable to obtain interpretable item-level clusters in either dataset used in this study, even after

applying dimensionality reduction to raw responses. In contrast, partitioning the survey into

domains preserves construct-level coherence: items designed to measure the same latent trait are

modeled together, while variation across constructs is deferred to later stages. The domain

structure provides the foundation for Stage 1 of the framework, which produces continuous,

domain-level scores for each participant. These domain scores then serve as the standardized,

psychometrically meaningful inputs to Stage 2, which identiﬁes behavioral clusters based on the

joint distribution of domains. Figure 1a provides an overview of the full two-stage dataﬂow.

3.1. Considerations of Domain Depth and Response Variability

To produce a meaningful domain-level representation, the domain must have suﬃcient response

resolution, i.e., items within a domain must collectively span a suﬃciently rich set of response

patterns to capture meaningful distinctions among individuals. Domains with very few items or

coarse response scales yield a limited set of possible response patterns, making it diﬃcult to

diﬀerentiate individuals or summarize the construct along a continuum. In practice, domains

intended to reﬂect broad, multi-faceted constructs typically require enough item-level richness –

at least six to eight items with nontrivial variability – to behave like continuous dimensions. By

contrast, domains designed to measure narrow or tightly deﬁned attributes (e.g., ﬁnancial literacy,

numeracy, construal level, or short-form aﬀective or motivational mini-scales) naturally exhibit

lower variability and fewer response combinations; these domains are scored using simpler

approaches that reﬂect their focused scope. Domains with insuﬃcient response resolution for

continuous diﬀerentiation are excluded from the clustering stage but may be retained for

interpretive or validation analyses. These considerations determine how each domain is handled

7

---

<!-- PAGE 9 -->

within the framework’s scoring procedures introduced below.

3.2 Stage 1: Producing Unidimensional Domain Scores

There are multiple valid ways to construct a domain-level score once items have been grouped

into coherent constructs, and the appropriate approach depends on the statistical and

psychometric properties of the domain. In this paper, we explore three such strategies, chosen to

illustrate how the framework can adapt domain scoring to diﬀerent structural patterns. Other

scoring approaches--such as projections in the original item space or alternative aggregation

schemes--are also feasible, but evaluating all possible variants lies beyond the scope of the

present study.

3.2.1 Anchor Projection Score

For medium- to high-dimensional domains with nonlinear relationships between the items,

heterogeneous item formats, and high response resolution, we apply dimensionality reduction

followed by anchor-based projection.  By embedding high-dimensional response patterns into a

lower-dimensional space, dimensionality reduction can mitigate redundancy, noise, and uneven

scaling, thereby improving interpretability and support downstream clustering.  In principle, both

linear methods, such as principal component analysis (PCA), and nonlinear manifold learning

techniques, such as UMAP, can be used. Linear methods assume that domain structure is well

approximated by a global linear subspace and are eﬀective when item relationships are

predominantly linear. Nonlinear methods relax this assumption by allowing local neighborhoods

to be preserved even when the global structure is curved. Note that some nonlinear approaches,

such as t-SNE, are primarily optimized for visualization and do not preserve global geometry or

support stable one-dimensional parametrization, making them less suitable for domain scoring in

the present context.

8

---

<!-- PAGE 10 -->

To guide method selection, we assess the geometric structure of each domain using

several complementary diagnostics. One indicator is the variance explained by the ﬁrst principal

component, which reﬂects the dominance of a single linear dimension. We also quantify

nonlinearity using a tangent-alignment index, deﬁned as the mean absolute cosine similarity

between the global PC1 direction and local one-dimensional PCA tangents estimated from each

participant’s 20 nearest neighbors. Domains with high PC1 dominance and tangent alignment

near 1.0 behave approximately linearly, whereas lower values indicate curved latent structure. As

an additional check, we evaluate whether linear projections adequately preserve neighborhood

relationships using trustworthiness and continuity metrics.

Once a domain representation is obtained, we convert each participant’s

multidimensional coordinates into a unidimensional domain score using a deterministic

anchor-based projection. For each domain, we deﬁne two deterministic anchor proﬁles: one

representing the weakest possible response for the domain traits, vmin (e.g., all 1s), and one the

strongest, vmax (e.g., all 5s). These anchors are embedded into the same low-dimensional space as

the observed participants, yielding embedded anchor points ve

min  and ve

max , respectively. Because

UMAP embeddings typically organize observations along smooth latent gradients, projecting

participants onto the axis deﬁned by the embedded anchors provides a simple and interpretable

summary of the dominant pattern distinguishing individuals within a domain. When this latent

gradient is approximately linear, linear projection preserves both relative ordering and distances

along the principal axis of variation. In this case, the domain score for participant i is computed

as the orthogonal projection of the participant’s embedding pᵢ onto the anchor axis: sᵢ = [(pᵢ −

ve

min) ⋅ (ve

max  − ve

min  )] / ǁve

max  − ve

min  ǁ². This score represents the participant's relative position

along the axis spanning the theoretical response range.

9

---

<!-- PAGE 11 -->

However, when the gradient is substantially curved, for instance, due to saturation eﬀects,

linear projection can distort distances or relative ordering along the manifold. To assess whether

linear projection is adequate, we evaluate rank consistency between anchor-based linear scores

and manifold-respecting positions using Spearman’s rank correlation coeﬃcient (ρ) and

Kendall’s rank correlation coeﬃcient (τ). These metrics quantify the degree to which linear

projection preserves relative ordering along the underlying manifold. Linear projection is

retained when ρ≥0.90 and τ≥0.85. When both statistics fall below these thresholds, indicating

concurrent global and local rank distortion, we compute participants’ scores using geodesic

distances (e.g., via Isomap) measured along the embedded manifold from ve

min to each

participant, normalized by the total manifold path length connecting ve

min  and ve

max  (Figure 2).

Although geodesic scoring provides a manifold-respecting parametrization of domain

progression, it is not used by default: if the latent gradient is approximately linear, linear

anchor-based projection yields more stable and auditable scores. Geodesic scoring is therefore

applied only when diagnostics indicate that linear projection fails to preserve both global and

local rank structure.

Unlike sample-based scores derived from z-scoring, percentile ranking, or other

normalization schemes, where scores depend on a participant’s relative position within a given

sample, anchor-based projection retains absolute interpretive meaning by computing each score

relative to ﬁxed conceptual anchor proﬁles rather than to other respondents in the dataset.

Sample-based scores are aﬀected by the empirical distribution of the data, which can distort

interpretation and make respondents appear “low” or “high” simply because the sample is

skewed. In addition to making scores sample-independent, anchor-based projection oﬀers a

10

---

<!-- PAGE 12 -->

preferable alternative to simple and weighted averages in domains where appropriate item

weights are unknown or direct aggregation of item values is not appropriate. By placing each

respondent along a predeﬁned continuum between low-functioning and high-functioning anchor

proﬁles, this approach produces domain-level scores without requiring explicit weighting

assumptions or reliance on sample-dependent normalization.

3.2.2 Weighted Average Score

When anchor-based projection is not applicable, such as in domains composed of dichotomously

scored items (e.g., correct vs. incorrect) or domains with highly homogeneous items reﬂecting a

particularly narrow trait, a weighted average provides a suitable alternative. In these cases, the

construct is well deﬁned in advance, item directionality is clear, and either the relative

importance of items is known or can be reasonably derived. In these cases, a weighted composite

score oﬀers a stable and interpretable summary of each participant’s standing in the domain.

Below we describe two typical scenarios when weights can be derived.

If items function as indicators of a common latent construct (e.g., abstract vs. concrete

thinking), item weights may be derived from the dominant covariance pattern within the domain.

Indicators with stronger and more consistent contributions to shared variance receive higher

weights, while weaker indicators contribute proportionally less. This yields a weighted index that

retains the clarity of the composite score while incorporating information about the latent

structure implied by the data. Weighting indicators by their contribution to shared variance is

consistent with reﬂective measurement theory (e.g., Bollen, 1989; Fabrigar & Wegener, 2012;

Embretson & Reise, 2000), which deﬁnes constructs through systematic covariance among

indicators.

By contrast, in domains where responses indicate correctness rather than endorsement of

11

---

<!-- PAGE 13 -->

a psychological attribute, a diﬃculty-based weighting scheme can be applied, in which each

item’s weight is proportional to its empirical diﬃculty (based on the prevalence of correct

responses in the sample) after adjusting for chance performance (e.g., Lord, 1989; Embretson &

Reise, 2000). Harder items receive higher weights, whereas items answered correctly by nearly

all participants contribute less.

After computing item weights, we compute domain scores as diﬃculty- or

covariance-weighted proportions, with 0 corresponding to the lowest attainable (not necessarily

present in the sample) standing and 1 to the highest. The resulting scores–bounded by the

theoretical range of the corresponding trait rather than the range in the sample–places these

domains on the common scale with the anchor-based projections described above, ensuring

comparability across domains and compatibility with downstream analyses.

3.2.3 Simple (Normalized) Average Score

For domains that do not lend themselves to anchor projection or are composed of items for which

no principled basis exists for diﬀerential weighting, we summarize responses using simple

unweighted averages. This approach is appropriate when items share a common response scale,

ensuring comparability across indicators2. Under these conditions, equal weighting provides a

transparent summary of domain-level functioning without imposing additional assumptions

about item importance or latent structure.

3.3 Stage 2: Clustering

The second stage of the pipeline operates on the domain-level scores produced in Stage 1.

Because each domain is now represented by unidimensional scores and the number of domains is

2 For domains that don’t fall into any of the three categories we consider in this paper, alternative scoring mechanisms (such as anchor projection 
in the original space) will need to be considered. None of the domains we identified in the datasets used for the current study required that.

12

---

<!-- PAGE 14 -->

generally small, the input to stage 2 is therefore low-dimensional. Nonetheless, domains are

intentionally constructed to be conceptually distinct and hence, when considered jointly, can

exhibit nonlinear structure, heterogeneous variance, or uneven resolution. To accommodate these

cross-domain characteristics, we apply UMAP to the domain-level scores to construct a

second-stage embedding prior to clustering.

To show that nonlinear embedding is called for at this stage, we benchmark clustering

performance across raw domain scores, PCA projections, and UMAP embeddings. UMAP

produces markedly stronger separation and more coherent geometry than either PCA or

raw-space representations, as reﬂected in higher silhouette values across benchmarked

conﬁgurations (Appendix B). We expect this ﬁnding to hold generally if survey items are

grouped into domains properly, i.e., to represent largely unrelated psychometric constructs.

Spectral clustering is then performed to identify latent groupings within the embedded

space3.  The resulting clusters of the points in the embedded space correspond to distinct

psychometric proﬁles of the participants represented by those points.  Both UMAP

transformation and spectral clustering will produce diﬀerent clustering solutions depending on

hyperparameters used. We tune hyperparameters and evaluate resulting clustering solutions based

on internal validity and qualitative interpretability of the resulting proﬁles. Internal validity is

quantiﬁed using standard metrics--including the silhouette score, Calinski–Harabasz index, and

Davies–Bouldin index--computed in the embedded space, while qualitative interpretability is

assessed by the coherence and distinctiveness of domain score patterns across clusters. These

complementary considerations guide selection among candidate solutions in speciﬁc applications

3 We tested alternatives such as K-means, DBSCAN, and HDBSCAN, but these performed poorly in capturing the non-convex geometry of the 
UMAP-transformed space (see Appendix B for comparisons).

13

---

<!-- PAGE 15 -->

of the framework.

We note that domains with few distinct score values (i.e., each value is shared by a

signiﬁcant fraction of participants) can induce trivial clustering partitions, even when those

domains have high theoretical response resolution. Because UMAP prioritizes the strongest local

contrasts when constructing its neighborhood graph, these low-cardinality domains produce a

small number of discrete plateaus that dominate the remaining dimensions. Spectral clustering

then splits the data almost exclusively along these plateaus, yielding clusters that are technically

stable but largely uninformative: individuals with identical values on the low-cardinality domain

are grouped together even when they diﬀer substantially on the broader psychometric constructs.

To avoid this collapse of the multivariate structure onto a single coarse dimension, we exclude

these domains from Stage 2 clustering and retain them only for interpretive analyses.

To aid interpretability, clusters are indexed according to their average cross-domain

behavioral standing.  For each participant, we compute a scalar summary score deﬁned as the

mean of their standardized scores across the ﬁve behavioral-ﬁnancial domains. This

participant-level average provides a parsimonious measure of overall functioning that weights

each domain equally and remains independent of geometric properties of the low-dimensional

embedding. Cluster-level summaries are obtained by averaging these participant-level scores

scores across all members of each cluster and clusters are then ordered according to their mean

score, yielding an interpretable ordering along a continuous cross-domain gradient.

To aid interpretability, clusters are indexed according to their average cross-domain behavioral

standing rather than their position in the embedded space. For each participant, we compute a

scalar score deﬁned as a weighted average of their domain scores, where weights reﬂect

empirically derived domain importance from post hoc analyses of cluster separation.

14

---

<!-- PAGE 16 -->

Cluster-level summaries are obtained by averaging these participant-level scores across all

members of each cluster. Clusters are then ordered according to their mean participant score,

yielding an interpretable ranking along a continuous cross-domain gradient from lower to higher

overall behavioral and ﬁnancial functioning. This ordering is not intended to imply a normative

ranking; rather, it provides a stable indexing convention across pipeline runs with diﬀerent seeds

and parameters. Nonetheless, the resulting numbering often follows a broad gradient--from more

vulnerable or struggling proﬁles to more adaptive or ﬂourishing ones. Intermediate clusters,

however, do not fall cleanly along this continuum and instead reﬂect distinct, non-linear

conﬁgurations of behavioral and psychological traits.

4. Use Case 1: Development of Individualized Strategy for Financial Advice

This framework was developed to support professional practice settings in which individuals or

couples seek guidance around financial decision-making and money-related relationship

dynamics. In such contexts, practitioners often work with clients who struggle with

follow-through, self-regulation, emotional responses to money, or alignment between intentions

and behavior, particularly among couples. The framework is designed to reveal a client’s

behavioral and psychological profile and thus support structured conversations, targeted

coaching, and more tailored intervention strategies. This applied orientation motivates the use of

a broad psychometric assessment of financial functioning that is given to new clients as part of

onboarding. Responses to this assessment form a proprietary dataset which we describe next.

4.1 Dataset Description and Conceptual Coverage

The proprietary dataset consists of responses to a 122-item psychometric instrument, comprising

95 domain items that assess eight dimensions of ﬁnancial functioning (Table 1) and 21 outcome

items used exclusively for external validation analyses (described in Section 4.7). The instrument

15

---

<!-- PAGE 17 -->

draws on established frameworks including Family Financial Socialization Theory (Gudmunson

& Danes, 2011), Self-Determination Theory (Di Domenico et al., 2022), and the Transtheoretical

Model of Change (Prochaska & DiClemente, 1983).

The instrument includes eight domains, each containing between 5 and 21 items, selected

to reﬂect multiple aspects of psychological functioning relevant to ﬁnancial behavior, including

self-regulation, motivation, construal, emotional resources, and ﬁnancial knowledge. Domains

corresponding to Financial Behavior (Prochaska & DiClemente, 1983), Financial Literacy

(Lusardi & Mitchell, 2011), and Motivation (Ryan & Deci, 2017) are well-established predictors

of ﬁnancial well-being and provide familiar interpretability within behavioral ﬁnance. Attitudes

& Capabilities domain captures perceived control, emotional tendencies, and ﬁnancial

self-concept–constructs strongly linked to planning and follow-through (Gudmunson & Danes,

2011) but often underrepresented in ﬁnancial assessments. Psychological Capital (hope,

resilience, optimism, eﬃcacy; Luthans, et al, 2007) and Character Strengths (e.g., perseverance,

self-regulation, gratitude) draw on well-validated frameworks (Peterson & Seligman, 2004) and

have been empirically linked to ﬁnancial resilience, adaptive coping, and reduced ﬁnancial stress

(Strömbäck et al., 2017; Xiao & O’Neill, 2016). Financial Construal Level, grounded in

Construal Level Theory (Trope & Liberman, 2010), assesses how individuals construe and

interpret ﬁnancial choices, shaping risk perception, time horizons, and behavioral

follow-through. The breadth of the item pool allows broad behavioral–psychological proﬁles to

emerge during the unsupervised learning.

4.2 Participant Sample and Psychometric Properties

A total of 337 participants meet the predeﬁned inclusion criteria and are included in the analytic

sample. Participants are required to complete at least 80% of each survey module to ensure

16

---

<!-- PAGE 18 -->

suﬃcient item-level data for reliable domain score computation. Item-level missing responses

within included surveys are handled using the imputation procedures described in Supplemental

Table C3. Domain-level score distributions are examined for extreme values (|z| > 3), and no

outliers are detected within the analytic sample. Participants are drawn from several U.S.-based

sources—including ﬁnancial advisors and their clients, college students, and voluntary

users—resulting in a heterogeneous sample that spans a wide range of ﬁnancial experiences,

decision-making contexts, and behavioral tendencies. Table 3 summarizes the socio-demographic

composition of the dataset.

Although modest in size, the dataset exhibits substantial response variability and strong

internal reliability in all psychometric domains (Cronbach’s α = .50–.94; Supplemental Table

S1). Responses vary widely across the full response range in each domain, with no evidence of

ﬂoor or ceiling eﬀects. Inter-domain correlations ranged from .30 to .83 (median r = .56),

indicating related but non-redundant constructs. Prior methodological work in exploratory

psychometric settings suggests that when measurement quality is high, meaningful latent

structure can be recovered with modest sample sizes, even in non-probability samples (Kyriazos,

2018). Moreover, the sample composition reﬂects the kinds of mixed recruitment sources

commonly available in practical behavioral-ﬁnance applications, where segmentation models are

typically developed from convenience-based cohorts rather than nationally representative

surveys.

4.3 Producing Domain Scores

Across the psychometric domains examined in this dataset, diagnostic analysis indicates that

most domains exhibit suﬃcient response resolution and globally curved geometry (Table 2),

warranting the application of UMAP followed by anchor-based projection to derive

17

---

<!-- PAGE 19 -->

unidimensional domain scores. To obtain stable embeddings, UMAP hyperparameters are

selected via randomized search by jointly maximizing trustworthiness and continuity using a

weighted objective to prioritize trustworthiness (α = 0.6; see Appendix C for the resulting

hyperparameter values). The embedding quality is high across all domains, with trustworthiness

ranging from 0.936 to 0.958 and continuity ranging from 0.949 to 0.972. For all evaluated

domains, linear anchor-based scores and geodesic (Isomap-based) scores produced nearly

identical rank orderings, with Spearman correlations exceeding .99 and Kendall τ values above

.87. Anchor-based projection scoring is, therefore, used throughout.

Two domains require alternative scoring approaches. Financial Literacy is scored as a

diﬃculty-adjusted accuracy composite, reﬂecting the proportion of correct responses weighted

by item diﬃculty as described in Section 3.2.2. In the Financial Construal Level domain,

although items are binary, their response options diﬀer substantially in the degree to which they

reﬂect abstract versus concrete construal. Treating all responses as uniformly equivalent (e.g.,

assigning 0/1 values) would therefore obscure meaningful diﬀerences in abstraction across items.

Instead, we use covariance-weighted aggregation, allowing responses to given items to contribute

proportionally based on their empirical alignment with overall construal patterns in the sample.

For example, items for which the “abstract” response tends to co-occur with abstract responses

on other items receive greater weight.

4.4 Clustering and Internal Validation

Using the domain-level scores described above, we construct a second-stage UMAP embedding

and apply spectral clustering to identify latent behavioral proﬁles of the participants. We tune the

hyperparameters of both UMAP and spectral clustering (Appendix C) to optimize separation in

the resulting low-dimensional manifold. Grouping the participants into seven clusters produces

18

---

<!-- PAGE 20 -->

results with discernible spatial separation and coherent structure: Silhouette Score of 0.569,

Calinski–Harabasz Index of 1,543.50, and Davies–Bouldin Index of 0.579. Moreover, the

clusters have reasonably uniform distribution as shown in Table 4.

To assess stability, we rerun the (UMAP → spectral clustering) pipeline using 100

independent random seeds while holding all hyperparameters ﬁxed. Cluster consistency across

runs is high (mean ARI = 0.916, SD = 0.043). We further assess robustness of the clustering

stage to sampling variation: we generate a single UMAP embedding using the full dataset and

apply spectral clustering to 100 random 80% subsamples within this ﬁxed embedded space.

Subsample solutions show very high stability relative to the full-sample reference (ARI = 0.970,

SD = 0.018).

4.5 Cluster Interpretability

In addition to the internal validity as described above, the clusters also possess coherent and

interpretable psychological structure (Figure 3a). These clusters can be understood as distinct

proﬁles within the broader ﬁnancial mindset space deﬁned in the Introduction. They are deﬁned

not only by the overall level of functioning but by how distinct combinations of ﬁnancial

behavior, perceived capability, motivation, psychological resources, and indicators of positive

functioning (deﬁned by domain scores) combine to shape behavior. Although clusters are

broadly ordered along a dominant functioning gradient, interpretability arises from meaningful

deviations from this gradient, yielding distinct behavioral pathways rather than simple severity

tiers.

At lower levels of functioning, limited psychological resources and motivation constrain

the translation of ﬁnancial knowledge into consistent behavior, whereas mid-range clusters

diverge in whether ﬁnancial engagement is primarily cognitive (e.g., higher construal and literacy

19

---

<!-- PAGE 21 -->

without equivalent execution) or structural (e.g., stable routines and competence with modest

motivational drive). At higher levels of functioning, clusters further diﬀerentiate based on the

role of motivation relative to skills, distinguishing proﬁles characterized by steady,

competence-driven performance from those marked by heightened motivational activation and

behavioral intensity. These patterns indicate that clusters reﬂect qualitatively distinct

conﬁgurations of psychological and behavioral factors, rather than points along a single

continuum. Domain-level summaries for cluster proﬁles are reported in Table 5a.

4.6 Demographic Analysis

To evaluate whether the behavioral clusters are primarily attributable to socio-demographic

stratification, we model cluster membership as a function of age, education, and income using

multinomial logistic regression. These variables are widely used indicators of socioeconomic

status (SES) in behavioral and financial research. The overall model is statistically significant

(likelihood-ratio test, p < .001), indicating that demographic variables are associated with cluster

assignment. However, explanatory power is modest (McFadden pseudo-R² = .091), suggesting

that socio-demographic factors account for only a limited proportion of variance in cluster

membership. At the predictor level, income shows statistically significant associations with

membership in two clusters (ps = .002–.003), while its associations with other clusters are

non-significant (ps > .08). Age and education display isolated significant contrasts (ps ≈

.03–.05), but the majority of their coefficients are non-significant (ps ≥ .09), and no consistent

pattern emerges across clusters. Taken together, these findings indicate that although

demographic variables contribute some signal, they do not substantially account for the

clustering structure.

4.7 External Associations with Independent Outcomes

20

---

<!-- PAGE 22 -->

We have seen in Sections 4.4 and 4.6 that our clustering approach expresses meaningful internal

structure that cannot be revealed through purely demographic  data.  We now turn to another

important aspect in evaluating our framework, namely,  whether the latent proﬁles it reveals

correspond to meaningful diﬀerences in overall functioning across psychological and behavioral

domains.  To this end, we consider how cluster membership correlates with independent external

outcomes that were not utilized in cluster construction.

Speciﬁcally, we consider life satisfaction, psychological well-being, and perceived

ﬁnancial health –  conceptually related yet empirically distinct evaluative outcomes. Life

satisfaction reﬂects a global cognitive appraisal of one’s life circumstances, psychological

well-being captures eudaimonic functioning and internal psychological resources, and ﬁnancial

health reﬂects perceived or objective ﬁnancial capacity and security. Prior research consistently

shows that although these constructs are moderately correlated, none is reducible to the others,

and each retains substantial unique variance after controlling for socioeconomic status and

objective ﬁnancial conditions (Mentus, 2017; Kokun et al., 2024; Halandová, 2024). Moreover,

psychological well-being is not merely an outcome of ﬁnancial conditions but also a key

antecedent of ﬁnancial behavior: low psychological resources, maladaptive beliefs, and

emotional distress reliably inhibit planning, follow-through, and adaptive ﬁnancial

decision-making, contributing to poorer ﬁnancial health over time (Thompson, 2021; Thompson,

2023).  Life satisfaction is measured using the Satisfaction with Life Scale (Diener et al., 1985),

psychological well-being is assessed with the Flourishing Scale (Diener et al., 2010), and

perceived ﬁnancial health is evaluated using a 10-item version of the Financial Health Network

Score (Financial Health Network, 2018).

Cluster membership is strongly associated with all three outcomes. One-way ANOVAs

21

---

<!-- PAGE 23 -->

indicate signiﬁcant between-cluster diﬀerences for Life Satisfaction, F(6,330) = 12.98, p < .001

(ηp² = .19), Psychological Well-Being, F(6, 330) = 19.90, p < .001 (ηp² = .27), and Perceived

Financial Health, F(6, 330) = 84.73, p < .001 (ηp² = .61). Post-hoc Tukey tests reveal extensive

pairwise diﬀerences between clusters; after correction for multiple comparisons, approximately

52–90% of pairwise contrasts remain signiﬁcant (adjusted p < .05). Full ANOVA tables are

reported in Supplemental Table S2.

To further assess reducibility, we compare regression models including (a) cluster

membership only, (b) socio-demographic variables only, and (c) both predictors jointly. Across

outcomes, cluster membership accounts for substantially more variance than socio-demographic

variables alone (R² = .19–.61 vs. .09–.16). In combined models, clusters contribute large

additional explanatory power beyond SES (ΔR² = .14–.45; Figure 5), whereas SES adds

comparatively little unique variance once cluster membership is included.

The observed associations between cluster membership and the external outcomes

provide evidence that the learned proﬁles capture underlying behavioral–psychological

organization that generalizes across distinct but interconnected domains of functioning, rather

than reﬂecting redundancy among outcome measures.

4.8 Assigning New Individuals to Learned Profiles

In the applied settings that motivated the development of this framework--such as ﬁnancial

advising, behavioral coaching, and clinical contexts--new individuals must be assigned to

previously constructed behavioral proﬁles.  It is obviously infeasible to re-cluster from scratch

every time a new respondent is added to the population.  Accordingly, we evaluate whether the

new respondents can be assigned to existing clusters using a supervised classiﬁcation approach.

To this end, we train a supervised ensemble soft-voting classiﬁer (see Supplemental Table C4),

22

---

<!-- PAGE 24 -->

composed of a Support Vector Machine (SVM) and a Random Forest, with cluster indices as

target labels, and evaluate its performance using 5-fold stratiﬁed cross-validation. The ensemble

achieves an accuracy of 79.2%, which substantially exceeds chance-level performance given the

number of clusters.

4.9 Anecdotal Success Evidence of Tailored Interventions

In addition to quantitative validation, we collect qualitative feedback from a small number of

pilot advisors who used the behavioral proﬁles revealed by the proposed pipeline in live client

engagements. Advisors describe using the proﬁles to anticipate client behavioral tendencies and

inform advisor-mediated interventions, particularly in time-constrained or emotionally salient

contexts.

Across examples, advisors report that the proﬁles are perceived as useful for anticipating

patterns of ﬁnancial avoidance under high salience, asymmetric pacing needs within couples,

sensitivity to pressure or authority, and reluctance to request assistance. These anticipated

tendencies inform decisions about communication framing, pacing and staging of

recommendations, meeting structure, and the timing of information delivery (e.g., asynchronous

plan review prior to discussion). Advisors further note that the proﬁles support interpretation of

client behavior when unexpected disclosures or actions occurred, reducing surprise and enabling

calibrated responses.

5. Use Case 2: Behavioral Segmentation At Scale

Here we evaluate whether the same two-stage framework identiﬁes meaningful behavioral

patterns in a large, independent, population-based dataset with diﬀerent measurement properties.

We apply the framework to the 2017 U.S. CFPB National Financial Well-Being Survey, a

nationally representative dataset designed to assess ﬁnancial well-being, ﬁnancial behaviors, and

23

---

<!-- PAGE 25 -->

perceived ﬁnancial capability among U.S. adults. Speciﬁcally, we apply the proposed framework

to segment the dataset population into meaningful clusters reﬂecting distinct behavioral proﬁles.

5.1 Dataset Description and Construct Mapping

Although the CFPB survey contains a broad set of variables spanning demographics, family

context, ﬁnancial behaviors, and structural conditions, our analysis focuses on a targeted subset

of items reﬂecting psychometric, attitudinal, relational, or cognitive constructs relevant to

ﬁnancial decision-making. Variables capturing situational constraints, access-related factors, or

external resources are excluded because they do not represent psychological attributes and are

therefore not suitable inputs for trait-based behavioral proﬁling (see Appendix A for item

details).

We group the selected items into ﬁve domains--Capabilities, Financial Literacy, Planning,

Budgeting & Saving, and Social & Relational Support (as shown in Appendix A)--which serve

as functional analogues to broader conceptual categories represented in the proprietary dataset.

5.2 Characteristics and Measurement Properties of the Sample

After excluding incomplete cases (n = 497; <8% of respondents), the ﬁnal analytic sample

consists of 5,897 individuals. Incomplete cases were deﬁned as respondents with missing data on

one or more items required for domain construction and clustering. The large sample size and

broad demographic coverage provide a stringent test of the framework utility under reduced

construct resolution and heterogeneous item scales. Although the CFPB survey was not designed

as a uniﬁed psychometric battery, the selected domains exhibit suﬃcient variability and internal

coherence to support nonlinear embedding and clustering (Cronbach’s α = .78–.87; Supplemental

Table S1). The Financial Literacy domain contains items that have binary response values

corresponding to correct or incorrect answers. The remaining domains capture perceived

24

---

<!-- PAGE 26 -->

capability, planning tendencies, routine ﬁnancial management, and social support.

5.3 Producing Domain Scores

Domain-level scores are derived using the same general principles described in Section 3, with

adaptations reﬂecting the CFPB instrument’s structure. Financial Literacy is scored as a

diﬃculty-adjusted accuracy composite in the exact same way as the corresponding proprietary

domain. The Social & Relational Support domain, which consists of seven binary items, is

scored using a simple average4. For the remaining psychometric domains, diagnostic analyses

indicate the need for nonlinear embedding, yet linear anchor-based projection in the resulting

embedded space is suﬃcient. Across these domains, UMAP embeddings achieve high

trustworthiness (0.944–0.983) and continuity (0.979–0.993); selected hyperparameter values are

listed in Supplemental Table S1.

5.4 Clustering and Internal Validation

Following the framework methodology, we tune hyperparameters for the second-stage UMAP

and spectral clustering via randomized search, optimizing the same metrics used for the

proprietary dataset (Supplemental Table S1). As expected, the Social & Relational Support

domain is not suitable for clustering, as it has only eight unique score values across all

participants; this domain is therefore excluded from the clustering step and retained solely for

post hoc interpretation. More unexpectedly, the inclusion of the Financial Literacy domain

consistently collapses the learned manifold, resulting in poor cluster separation and reduced

interpretability. Careful inspection of the resulting score distribution reveals that, despite its high

nominal response resolution, empirically, Financial Literacy concentrates respondents on a

4 The items in this domain appear to be positively correlated in a fairly uniform way, so the covariance weights end up close to 
equal weighting. When that happens, the covariance-weighted score collapses to something very close to the simple average.

25

---

<!-- PAGE 27 -->

limited set of score values, with the four most frequent values alone comprising approximately

30% of the sample (Figure 4). These spikes impose a strong ordering structure that

disproportionately shapes the embedding geometry and obscures multidimensional behavioral

variation contributed by other domains. Accordingly, Financial Literacy is also excluded from

clustering and examined only post hoc for proﬁle interpretation.

After removing these two domains, we perform the clustering procedure to group the

participants into seven clusters (Figure 1c). Internal validation metrics indicate meaningful

clustering structure, with a Silhouette Score of 0.500, a Calinski–Harabasz Index of 10,639.98,

and a Davies–Bouldin Index of 0.622. Although cluster separation is less pronounced than in the

proprietary dataset, these values are consistent with coherent proﬁle diﬀerentiation given the

larger population base and reduced construct resolution.

As in the case of the proprietary dataset, we assess the seed stability by reruning the

clustering pipeline across 100 independent random seeds and subsample stability by clustering

100 random 80% subsamples within a ﬁxed second-stage embedding.  Both metrics indicate that

the recovered structure is not driven by stochastic variation or sampling idiosyncrasies: the seed

stability is high, with mean ARI = 0.814 (SD = 0.086) and subsample stability is very high, with

mean ARI = 0.994 (SD = 0.003)

5.5 Cluster Interpretability

The CFPB clusters exhibit coherent and interpretable structure, reﬂecting distinct conﬁgurations

of ﬁnancial capability, planning, budgeting and saving behavior, social and relational functioning,

and ﬁnancial literacy (Figure 3b). Although cluster means generally increase along an overall

gradient of ﬁnancial functioning, the proﬁles are not reducible to a single severity dimension.

Instead, clusters are distinguished by how knowledge, planning capacity, and enacted ﬁnancial

26

---

<!-- PAGE 28 -->

behaviors align—or fail to align—within individuals.

Lower-functioning clusters are characterized by comparatively weaker budgeting and

saving behavior and planning capacity, even when ﬁnancial literacy is moderate, suggesting

barriers in translating knowledge into sustained ﬁnancial routines. Intermediate clusters diverge

in the balance between structural behaviors and cognitive resources: some proﬁles emphasize

strong budgeting and saving practices with only moderate planning or capability, whereas others

show elevated planning and literacy without commensurate behavioral execution. At higher

levels of functioning, clusters diﬀerentiate based on the relative emphasis placed on planning

intensity, behavioral consistency, and social–relational support, distinguishing proﬁles marked by

comprehensive, integrated ﬁnancial engagement from those with more selectively developed

strengths (Table 5b).

5.6 Demographic Analysis

Given the central role of socio-demographic variables in population-based ﬁnancial surveys, we

examine whether cluster membership in the CFPB sample is primarily explained by

socio-demographic factors. We estimate a multinomial logistic regression predicting cluster

membership from age, education, and income. The overall model is statistically signiﬁcant

(likelihood-ratio test, p < .001), and age, education, and income are each statistically signiﬁcant

predictors across multinomial contrasts (all ps < .001). However, explanatory power is modest

(McFadden pseudo-R² = .061), indicating that socio-demographic variables account for only a

limited proportion of variance in cluster assignment. These results mirror the proprietary dataset

ﬁndings and indicate that the CFPB clusters are not reducible to demographic stratiﬁcation, but

instead capture behavioral and psychological variation beyond standard SES indicators.

5.7 External Associations With Independent Outcomes

27

---

<!-- PAGE 29 -->

We consider three outcome domains not included in the clustering process: Life Satisfaction and

Perceived Financial Health, which parallel the evaluative outcomes examined in the proprietary

dataset, and Material Hardship capturing acute ﬁnancial strain. Cluster membership is

signiﬁcantly associated with all three outcomes. One-way ANOVAs indicate between-cluster

diﬀerences for Life Satisfaction (ηp² = .14), Material Hardship (ηp² = .23), and Perceived

Financial Health (ηp² = .44), closely paralleling the pattern observed in the proprietary data (see

Supplemental Table S2). Post-hoc Tukey tests indicate that these eﬀects reﬂect systematic

diﬀerences across multiple clusters rather than being driven by a single extreme group.

Further, as shown in Figure 5, cluster membership explains substantial variance in Life

Satisfaction (R² = .14) and Perceived Financial Health (R² = .44), exceeding the variance

explained by demographics alone (R² = .04 and .25, respectively), and contributes meaningful

unique variance in the full models (ΔR² = .12 for Life Satisfaction; ΔR² = .25 for Perceived

Financial Health). As expected, socio-demographic variables account for a larger share of

variance in Material Hardship (R² = .27); nevertheless, cluster membership explains additional

unique variance (ΔR² = .09), indicating that behavioral–psychological proﬁles provide

explanatory power even for outcomes reﬂecting concrete economic strain.

6. Structural Alignment of Cluster Proﬁles Across Datasets

We have seen that the proposed framework can be applied to two datasets of very diﬀerent

nature, producing meaningful interpretable clusters in each case.  We next explore whether

proﬁles derived from the proprietary and CFPB samples exhibit functional similarities. The

challenge arises because the instruments in both datasets are not the same: they contain diﬀerent

questions, with markedly diﬀerent measurement properties. Still, both instruments assess several

core constructs related to ﬁnancial behavior, literacy, psychological resources, positive

28

---

<!-- PAGE 30 -->

functioning, and planning or organizational processes. Thus, we harmonize the two datasets into

a common ﬁve-domain conceptual space: Financial Behavior, Financial Literacy, Psychological

Resources, Positive Functioning, and Motivation & Planning.  Financial Construal Level domain

is excluded from the proprietary side because the CFPB dataset lacks an equivalent domain. See

Appendix D for details on constructing the harmonized space.

This uniﬁed space allows direct comparison of proﬁles derived from both datasets, with

alignment quantiﬁed using several complementary metrics described in Appendix D2. Cluster

centroids are closely aligned along a dominant global functioning axis deﬁned primarily by

Financial Behavior, Psychological Resources, and Motivation & Planning (PC1 loadings = .524,

.505, and .507, respectively), with weaker contributions from Financial Literacy and Positive

Functioning (loadings = .250 and .389). Cluster ordering along this axis is perfectly preserved

across datasets (Spearman ρ = 1.00), indicating preserved rank structure despite diﬀerences in

domain coverage. Geometric alignment of cluster proﬁles is moderate to strong (Procrustes

disparity = .158; mean CPSI = .739), with the greatest correspondence observed at higher levels

of functioning and increased compression in CFPB proﬁles relative to the proprietary dataset at

the lower end of the distribution. Figure 6 illustrates that, when clusters are ordered along the

global functioning axis, proprietary and CFPB centroids exhibit similar absolute functioning

levels, consistent with strong ordinal correspondence and relatively low Procrustes disparity.

These results indicate that the framework captures a shared latent structure that extends

beyond sample-speciﬁc clustering solutions. While the present analysis is limited to two datasets,

the observed structural alignment suggests that suﬃciently rich behavioral surveys may reveal

proﬁles reﬂecting inherent properties of ﬁnancial behavior. Further experimentation with

additional datasets–across diﬀerent instruments and populations–is required to conﬁrm this

29

---

<!-- PAGE 31 -->

conjecture.

7. Discussion

This study presents a novel behavioral segmentation framework that leverages unsupervised

learning to uncover latent behavioral structure. The primary contribution of this work is

methodological: the framework that introduces a staged approach to behavioral proﬁling, which

separates within-domain representation from cross-domain integration, enabling psychologically

interpretable segmentation across diverse psychometric instruments.  Rather than assuming a

predeﬁned structure or rigid scoring strategy, this approach accommodates domains with varying

measurement properties, including both approximately linear and nonlinear relationships among

items.

We provide evidence of wide applicability of the proposed framework by using it to

uncover latent proﬁles in two independent datasets of very diﬀerent nature.  The emergent

proﬁles in both cases demonstrate robust internal structure and meaningful diﬀerentiation with

respect to external outcomes–most strongly for ﬁnancial health and psychological well-being,

and to a lesser degree for life satisfaction. This pattern aligns with prior work showing that

proximal outcomes such as ﬁnancial health are more tightly linked to daily behaviors and

psychological capacities, whereas life satisfaction reﬂects broader and more diﬀuse life

evaluations (Diener et al., 1999; Netemeyer et al., 2018). Systematic diﬀerences on these broader

outcome measures suggest that the learned proﬁles reﬂect underlying psychological organization

rather than merely diﬀerences in observable ﬁnancial behaviors.

In addition to quantitative validation above, the framework is being evaluated in live

advisory contexts, where preliminary practitioner feedback indicates that the resulting proﬁles

predict behaviorally relevant tendencies that inform practitioners’ decision-making in tailoring

30

---

<!-- PAGE 32 -->

advisor–client interactions.

7.1 Methodological Advances

This work advances behavioral segmentation methodology in four key ways. First, rather than

clustering item-level responses directly, the framework adopts a two-stage representation strategy

that separates the inference of the within-domain structure from cross-domain integration. This

design preserves domain-speciﬁc psychological distinctions while preventing domains with

greater item counts from disproportionately inﬂuencing the clustering solution.

Second, the framework formalizes domain-level representations as continuous scores that

place individuals along a meaningful psychological axis within the domain. Speciﬁcally, we

introduce an anchor-based projection strategy that can be applied in either the original item space

or after dimensionality reduction, mapping responses onto interpretable continua deﬁned by ﬁxed

conceptual reference proﬁles.

Third, the framework is intentionally modular and algorithm-agnostic. Although UMAP

and spectral clustering provide strong empirical performance in the present study, the

architecture does not depend on a speciﬁc embedding or clustering method, enabling

applicability across instruments, populations, and survey formats.

Finally, by applying the same framework to datasets with markedly diﬀerent

psychometric depth, this work demonstrates how measurement richness inﬂuences the

granularity of recovered behavioral proﬁles without requiring fundamentally diﬀerent modeling

strategies.

Together, these advances provide a ﬂexible and interpretable approach to

behavioral-ﬁnance segmentation that extends beyond existing linear or single-pass clustering

methods. Domain construction, scoring methods, and inclusion in clustering are speciﬁed

31

---

<!-- PAGE 33 -->

conceptually a-priori, and then evaluated empirically using the diagnostics described in this

paper, leading to potential revision cycles. This enables the framework to adapt ﬂexibly across

instruments and datasets while preserving interpretability and methodological coherence.

7.2 Practical Applications

The  clustering framework developed in this study lends itself to a wide range of applications

across clinical, advisory, and digital ﬁnancial contexts.

In clinical psychology and ﬁnancial therapy, behavioral proﬁles may support more

targeted intervention planning than traditional demographic or symptom-based approaches by

aligning treatment strategies with clients’ emotional, cognitive, and motivational readiness for

ﬁnancial change (Archuleta et al., 2012). For example, proﬁles characterized by strong capability

and stable behavioral routines (e.g., Cluster 3) may beneﬁt less from motivational enhancement

strategies and more from structured goal-setting, cognitive restructuring around long-term

planning, and values clariﬁcation interventions. In such cases, therapeutic work may focus on

optimizing existing strengths rather than increasing behavioral activation. In contrast, individuals

in Cluster 0, who exhibit lower psychological resources or signs of emotional depletion, may

beneﬁt from approaches that prioritize therapeutic alliance, emotion-focused techniques, or

motivational interviewing (MI) to strengthen autonomy, hope, and readiness for change before

introducing structured ﬁnancial planning tasks. In this way, the proﬁles may assist practitioners

in determining whether cognitive-behavioral techniques, motivational enhancement, or

supportive-expressive approaches are most appropriate, thereby facilitating more precise

treatment matching within established clinical frameworks.

In ﬁnancial advising, the proﬁles support personalization of communication style,

planning horizons, and behavioral scaﬀolds based on clients’ cognitive and motivational

32

---

<!-- PAGE 34 -->

tendencies. For instance, clients with strong analytical capacity but weak follow-through may

beneﬁt from structured action plans and accountability mechanisms, whereas those with lower

conﬁdence or elevated anxiety may respond better to incremental goal-setting and simpliﬁed

messaging.

In consumer-facing ﬁntech platforms, behavioral proﬁles can drive adaptive

personalization features such as goal tracking, contextual nudges, and mindset-speciﬁc content

(Thaler & Sunstein, 2008). Integration with LLM-powered agents further enables real-time

adjustment of conversational tone and support strategies based on users’ behavioral tendencies.

This approach is currently being operationalized within the Calibrate platform, where a

reduced-item classiﬁer enables scalable psychometric segmentation to support adaptive

onboarding, behavioral coaching, and digital ﬁnancial planning.

At a population level, behavioral segmentation can inform public ﬁnancial-wellness

initiatives and workplace ﬁnancial education programs, enabling stratiﬁed content delivery, early

risk identiﬁcation, and targeted outreach to underserved or vulnerable groups.

7.3 Limitations and Future Work

This study has several limitations that primarily reﬂect data availability and the scope of

empirical evaluation rather than the proposed methodology itself.

First, both datasets are cross-sectional, which precludes assessing how individuals’

behavioral proﬁles evolve over time. It is important to distinguish this limitation from

methodological stability: while the clustering solutions are reproducible across random

initializations and analytic settings, the present data do not permit evaluating whether individuals

transition between proﬁles in response to interventions, life events, or changing ﬁnancial

circumstances. Longitudinal data would be required to study such dynamics and to examine how

33

---

<!-- PAGE 35 -->

the framework responds to temporal change.

Second, all measures are based on self-report. Self-reported data may be inﬂuenced by

response styles, social desirability, or diﬀerential self-awareness, which can introduce

measurement noise and aﬀect the geometry of the learned representations. Incorporating

behavioral, transactional, or passively collected data in future work would strengthen ecological

validity and improve the precision with which behavioral structure is inferred.

Third, the proprietary dataset is modest in size and drawn from a heterogeneous

convenience sample that skews younger than the broader U.S. population. While this reﬂects a

limitation in terms of population representativeness, it also mirrors the data constraints

commonly encountered in applied and advisory settings, where large probabilistic samples are

rarely available. Demonstrating that the framework yields coherent and interpretable structure in

such a small-sample context is therefore a practical feature of the approach. Nonetheless,

additional applications across diverse populations, institutional settings, and sample sizes would

help further characterize the robustness and boundary conditions of the method.

Fourth, as with most unsupervised learning frameworks, the proposed approach involves

analytic design choices--such as domain construction, embedding parameters, and clustering

resolution--that can inﬂuence the resulting structure. Rather than emphasizing uniqueness of any

single solution, we focus on reproducibility across reasonable speciﬁcations. Future work could

further formalize guidelines for parameter selection and sensitivity analysis to support broader

applied use.

Finally, although the present study focuses on ﬁnancial behavior, the analytic framework

itself is domain-agnostic. Applying the approach to other areas--such as mental health, education,

or wellness--would help assess the extent to which similar forms of latent

34

---

<!-- PAGE 36 -->

behavioral-psychological structure emerge across diﬀerent substantive domains and

data-generating contexts.

8. Conclusion

This paper introduces a two-stage unsupervised learning framework for identifying

psychologically interpretable patterns of ﬁnancial behavior. Applied to both a proprietary

psychometric instrument and the public CFPB dataset, the approach yields coherent and

externally meaningful clustering structure, demonstrating its utility for uncovering latent

behavioral organization in ﬁnancial data. Although additional validation across more diverse

populations will further clarify its generalizability, the present results show that integrating

behavioral science with manifold learning can support theoretically informed and practically

useful segmentation of ﬁnancial mindsets.

We validate the framework through internal measures of psychometric coherence and

external associations with independent well-being outcomes, indicating that the recovered

structure reﬂects psychologically relevant variation rather than statistical artifacts. The resulting

clusters extend traditional ﬁnancial personas by incorporating emotional, cognitive, and

motivational dimensions, yielding segments that are interpretable and informative in applied

settings.

Together, these contributions support a growing movement toward behaviorally

intelligent personalization in ﬁnancial services. The proposed framework oﬀers a scalable and

replicable foundation for modeling the human dimensions of ﬁnancial decision-making in a

manner that is data-driven, ﬂexible, and person-centered.

Acknowledgements

We are grateful to Dr. Joseph Beyer of Microsoft and Dr. Megan McCoy of Kansas State

35

---

<!-- PAGE 37 -->

University for their early guidance and encouragement in the development of the assessment that

produced our proprietary dataset. We also thank Dr. McCoy and Dr. Jack Bowler of the

University of Utah for their careful reading of the manuscript and valuable feedback.

36

---

<!-- PAGE 38 -->

Figure 1. Behavioral-ﬁnancial clusters derived from unsupervised learning.  (a) Schematic of the two-stage 
unsupervised learning framework. (b) Two-dimensional UMAP projection of the proprietary dataset colored by 
Spectral Clustering assignments. (c) Two-dimensional UMAP projection of the public CFPB dataset. In both 
projections, anchor references (black and green dots) are included to aid spatial interpretability of the embedded 
proﬁles. The anchors are generated by setting all domain scores to their observed minimum or maximum values 
across all participants and subsequently embedded into the ﬁnal space. Cluster structure exhibits clear separation in 
reduced-dimensional psychometric space, with curvature reﬂecting dataset-speciﬁc nonlinear organization.

37

---

<!-- PAGE 39 -->

max , green) anchors. For a representative participant (circled), the orthogonal projection onto the

Figure 2. Anchor-based linear versus geodesic scoring on low- and high-curvature manifolds. 
Panel A illustrates a domain embedding with low curvature, where participant embeddings (gray points) are 
organized along an approximately linear latent gradient between the embedded minimum (ve
min, black) and 
maximum (ve
anchor-deﬁned axis yields a scalar score corresponding to the participant’s progress along the domain continuum. 
The blue dashed segment along the anchor axis indicates the resulting linear score. 
Panel B illustrates a domain embedding with substantial curvature. Although a straight-line anchor axis can still be 
deﬁned, linear projection no longer faithfully represents progression along the latent gradient. Instead, the 
participant’s score is deﬁned by the length of the manifold path from ve
manifold (blue dashed path), normalized by the total path length between ve
In both cases, the score reﬂects progression along the anchor-deﬁned domain continuum rather than overall 
Euclidean proximity to the anchors.

min to the participant along the embedded

min  (black) and ve

max  (green).

38

---

<!-- PAGE 40 -->

Figure 3. Heatmaps of mean domain scores by cluster across eight psychological and behavioral domains for the 
proprietary dataset (a) and ﬁve domains for the CFPB dataset (b), revealing distinctive cluster-level proﬁles.

Figure 4. The spike chart of score value occurrences for the CFPB domains. The Social and Relational domain 
shows spikes corresponding to the eight possible score values. The Financial Literacy domain shows a small number 
of spikes dominating the score distribution. The rest of the domains show wider distribution of scores across 
participants, with less prominent spikes.

39

---

<!-- PAGE 41 -->

Figure 5. Variance explained by cluster membership and socio-economic status for subjective and ﬁnancial

outcomes in the proprietary (top) and CFPB (bottom) datasets.

Bar charts show the proportion of variance explained (R²) in Life Satisfaction, Psychological Well-Being, Financial

Health, and Financial Strain for three models: (1) Clusters only; (2) Demographics only (age, education, income);

and (3) Clusters + Demographics. In both datasets, cluster membership accounts for substantial variance in Life

Satisfaction and Financial Health, exceeding that explained by demographics alone. For Material Hardship--a

construct more tightly linked to resource constraints--demographics contribute more variance, yet clusters still

explain sizable unique variance beyond demographics. The combined models indicate that behavioral–psychological

proﬁles captured by the clustering framework provide explanatory power that is not reducible to demographic

factors.

40

---

<!-- PAGE 42 -->

Figure 6: Global functioning gradient across clusters. Clusters from the proprietary and CFPB datasets are ordered 
by their position along the global functioning axis (PC1), derived from principal component analysis of pooled 
cluster centroids expressed in the uniﬁed ﬁve-domain space. Lines connect order-preserving paired clusters to 
illustrate similarity in absolute functioning levels across datasets.

Table 1 
Summary of the eight psychometric domains used in the clustering analysis, including theoretical foundations, item 
counts, and response formats. Full descriptive statistics and reliability estimates are reported in Supplemental Table 
S1; sample items are provided in Appendix A.

Domain

Description

Format

Item Count  Core Constructs

Character 
Strengths

Attitudes & 
Capabilities

Psychological 
Capital

Motivation

Financial 
Behavior

Adapted from the VIA Classiﬁcation 
of Character Strengths (Peterson & 
Seligman, 2004) to reﬂect ﬁnancial 
decision-making contexts

Perceived behavioral control and 
ﬁnancial self-eﬃcacy; aligns with 
Family Financial Socialization 
Theory (Gudmunson & Danes, 
2011)

Positive psychological resources for 
coping and adaptive ﬁnancial 
behavior, drawn from the PsyCap 
framework (Luthans et al., 2007)

Internal and external motivational 
drivers of ﬁnancial behavior; based 
on Self-Determination Theory (Ryan 
& Deci, 2017)

Everyday ﬁnancial management 
behaviors; consistent with 
stages-of-change perspectives 
(Prochaska & DiClemente, 1983)

5-point Likert

21

Self-regulation, 
perseverance, ethical 
values

5-point Likert

17

Financial self-eﬃcacy, 
perceived control

5-point Likert

8

Hope, resilience, 
optimism, self-eﬃcacy

5-point Likert

14

Goal orientation, 
long-term motivation

5-point Likert

11

Behavioral 
consistency, habit 
strength

41

---

<!-- PAGE 43 -->

Positive 
Functioning

Psychological well-being and 
emotional balance relevant to 
ﬁnancial decision-making 
(Seligman, 2011)

5-point Likert

9

Subjective well-being, 
emotional regulation

Financial 
Construal 
Level

Financial 
Literacy

Tendency to interpret ﬁnancial 
situations at more concrete vs. more 
abstract levels of meaning (Trope & 
Liberman, 2010).

Forced choice 
(2-option)

10

Construal-level 
processing, abstraction 
orientation

Objective ﬁnancial knowledge 
assessed using validated items 
(Lusardi & Mitchell, 2011)

Multiple choice

5

Decision accuracy, 
factual ﬁnancial 
knowledge

Note: All domain items are derived from validated psychometric frameworks (e.g., VIA Character Strengths, PsyCap, 
Self-Determination Theory, Construal Level Theory) and are adapted where appropriate to reﬂect ﬁnancial decision-making 
contexts. The ﬁnal 95 items represent the empirically selected subset of a broader 224-item domain pool, retained based on 
distributional quality, non-redundancy, and their contribution to stable structure in preliminary UMAP manifold assessments.

Table 2 
Summary of Domain Structures, Dimensional Properties, and Scoring Methods for the Proprietary and CFPB 
Datasets 
Domain

Scoring Method

# 
Items

PC1 Variance 
Explained

Domain 
Resolution

Nonlinearity 
Indicator*

Spearman ρ 
/Kendal τ

Proprietary Dataset

Character 
Strengths

Attitudes & 
Capabilities

Psych. Capital

Motivation

Financial 
Behavior

Positive 
Functioning

Construal Level

Financial 
Literacy

CFPB Dataset

Capability

Budgeting & 
Saving

Planning

Financial

21

17

8

14

11

.434

.407

.537

.465

.430

4.77×1014

.614

.997/.952

UMAP + Anchor

7.63×1011

.588

.994/.932

UMAP + Anchor

3.91×105

6.10×109

4.88×107.

.597

.541

.573

.994/.932

UMAP + Anchor

.995/.941

UMAP + Anchor

.996/.951

UMAP + Anchor

9

.517

1.95×106

.574

.989/.916

UMAP + Anchor

10

5

13

9

9

12

.181

-

.424

.346

.362

.123

1,024

32

7.24×108

1.35×106

7.76×105

4,096

.381

-

.400

.377

.399

.319

Weighted average

Diﬃculty-weighted 
average, 
interpretation only

.999/.978

UMAP + Anchor

.979/.879

UMAP + Anchor

.994/.933

UMAP + Anchor

Diﬃculty-weighted

42

---

<!-- PAGE 44 -->

Literacy

Social & 
Relational

7

-

128

-

average

Simple average, 
interpretation only

Note: * Nonlinearity Indicator is deﬁned as the mean absolute cosine similarity between the global PC1 direction 
and the local 1-D PCA tangent estimated from each point’s 20 nearest neighbors. Lower values indicate greater 
deviation from global linearity and stronger support for a nonlinear embedding. Even when values suggest 
approximate linear structure, incomplete local tangent alignment motivates the use of manifold embedding to 
preserve curved latent organization. 
Domains with very limited response resolution, which yield only a small number of unique response patterns after 
deduplication, are excluded from PCA- and manifold-based linearity diagnostics because such metrics are not 
meaningful for discrete, low-variability constructs. 
Outcome domains (Life Satisfaction, Psychological Well-Being, Material Hardship, and Financial Health) are not 
included in these diagnostics because they are used solely as external validation measures rather than as inputs to the 
embedding or clustering procedures.

Table 3

Demographic characteristics of proprietary set participants

Variable

Gender

Age Group

Category

Female

Male

Non-binary/undisclosed

18–24

25–34

35–44

45–54

55–64

65+

Not reported/undisclosed

Income

Less than $50,000

$50,000 – $100,000

$100,000 – $200,000

$200,000 – $500,000

$500,000 or more

Not reported

Education

Graduate or professional degree

Bachelor’s degree

N

170

147

20

86

41

85

45

48

18

15

77

50

74

69

42

25

115

115

%

50.4%

43.7%

5.9%

25.5%

12.2%

25.2%

13.4%

13.9%

5.3%

4.5%

22.9%

14.8%

22.0%

20.5%

12.5%

7.4%

34.1%

34.1%

43

---

<!-- PAGE 45 -->

High school or equivalent

Some college / Associate degree

Not reported/Undisclosed

Race/Ethnicity

White

Black or African American

Asian

Hispanic or Latino

Other

Not reported

24

39

44

7.1%

11.6%

13.1%

202

59.9%

51

42

19

19

6

15.1%

12.5%

5.6%

5.6%

1.8%

Note: Participants could select multiple ethnicity categories; percentages sum to more than 100%.

Table 4  
Cluster distribution 
Both datasets exhibited similar cluster dispersion: cluster sizes ranged from 7%–21% in the proprietary sample and 
8%–22% in the CFPB sample.

Proprietary Dataset

CFPB dataset

Cluster

n  % of Sample

Cluster

n  % of Sample

0

1

2

3

4

5

6

26

71

47

65

62

25

41

7.72%

21.07%

13.95%

19.29%

18.40%

7.42%

12.17%

0

1

2

3

4

5

6

1,301

22.06%

745

12.63%

1,294

980

461

629

487

21.95

16.62

7.82

10.67

8.26

100

Total

337

100

Total

5,897

Table 5a 
Descriptive Cluster Proﬁles in the proprietary Dataset 
Cluster-level summary descriptions derived from domain score patterns (Character Strengths, Attitudes & 
Capabilities, Psychological Capital, Motivation, Financial Behavior, Positive Functioning, Financial Construal 
Level, and Financial Literacy). Labels are descriptive and reﬂect relative strengths across domains.

Cluster  Label

Interpretive Summary

44

---

<!-- PAGE 46 -->

0

1

2

3

4

5

6

Low capability, low psychological 
resources

Globally low strengths, capability, psychological capital, 
motivation, and behavior. Adequate literacy does not translate 
into action because conﬁdence and functioning are limited.

Emerging capability with inconsistent 
habits

Improving capability, literacy, and functioning, but motivation 
and routines are not yet stable. Behavior is inconsistent despite 
modest psychological resources.

Cognitively engaged, moderately 
supported

Capable and stable

Highly capable, steady performer

Organized and well-resourced

Highly resourced and consistently 
eﬀective

Moderate strengths, capability, and behavior, with relatively 
higher literacy and ﬁnancial construal. Thinks about ﬁnances and 
plans ahead, but only mid-level energy and execution.

Strong capability, literacy, functioning, and behavior, paired with 
moderate motivation. Operates eﬀectively through competence 
and routine rather than pronounced motivational drive.

High capability, psychological capital, functioning, and literacy, 
with solid behavior but only moderate motivational drive. 
Performs reliably through skills and structure rather than strong 
emotional push.

High strengths, capability, motivation, and behavior, with very 
strong literacy and functioning.

Exceptionally strong across all psychological, motivational, and 
behavioral domains. Demonstrates very high internal resources, 
strong motivation, excellent functioning, and reliable execution.

Table 5b  
Descriptive Cluster Proﬁles in the CFPB Dataset 
Cluster-level summary descriptions derived from domain score patterns (Capability, Budgeting & Saving, Planning, 
Social & Relational Support, and Financial Literacy). Labels are descriptive and reﬂect relative strengths across 
domains. 
Cluster  Label

Interpretive Summary

0

1

2

3

4

Low structure, low follow-through

Growing structure, limited action

Has diﬃculty getting started; weak systems, low motivation, and 
limited follow-through. Conﬁdence is modest, making ﬁnancial 
tasks feel eﬀortful or overwhelming.

Has some organizational footing and emerging conﬁdence, but 
actions are irregular. Motivation exists but isn’t strong enough to 
sustain habits.

Highly organized, cautious executor  Well-organized and deliberate, but often slow to execute. Strong

Strong everyday habits

systems, but prefers caution over speed.

Shows reliable real-world behavior even without elaborate 
planning. Conﬁdent and motivated enough to maintain consistent 
routines.

Structured and consistent

Combines strong systems with strong execution. Conﬁdent, 
organized, and steady in follow-through.

45

---

<!-- PAGE 47 -->

References

Archuleta, K. L., Burr, E. A., Dale, A. K., Canale, A., Danford, D., Rasure, E., Nelson, J.,

Williams, K., Schindler, K., Coﬀman, B., & Horwitz, E. (2012). What is ﬁnancial

therapy? Discovering mechanisms and aspects of an emerging ﬁeld. Journal of Financial

Therapy, 3(2), 57–77. https://doi.org/10.4148/jft.v3i2.1807

Atkinson, A., & Messy, F. A. (2012). Measuring ﬁnancial literacy: Results of the OECD /

International Network on Financial Education (INFE) pilot study. OECD Working Papers

on Finance, Insurance and Private Pensions, No. 15.

https://doi.org/10.1787/5k9csfs90fr4-en

Becht, E., McInnes, L., Healy, J., Dutertre, C. A., Kwok, I. W., Ng, L. G., Ginhoux, F., &

Newell, E. W. (2019). Dimensionality reduction for visualizing single-cell data using

UMAP. Nature Biotechnology, 37(1), 38–44. https://doi.org/10.1038/nbt.4314

Bergstra, J., & Bengio, Y. (2012). Random search for hyper-parameter optimization. Journal of

Machine Learning Research, 13, 281–305.

https://www.jmlr.org/papers/v13/bergstra12a.html

Bollen, K. A. (1989). Structural Equations with Latent Variables. New York, NY: Wiley.

Brüggen, E. C., Hogreve, J., Holmlund, M., Kabadayi, S., & Löfgren, M. (2017). Financial

well-being: A conceptualization and research agenda. Journal of Business Research, 79,

228–237. https://doi.org/10.1016/j.jbusres.2017.03.013

Carver, C. S., & Scheier, M. F. (1998). On the self-regulation of behavior. Cambridge University

Press.

CFPB. (2015a). Financial well-being: The goal of ﬁnancial education. Consumer Financial

Protection Bureau.

46

---

<!-- PAGE 48 -->

CFPB. (2015b). Financial well-being scale: Scale development technical report. Consumer

Financial Protection Bureau.

CFPB. (2017). National Financial Well-Being Survey Public Use File. Consumer Financial

Protection Bureau.

https://www.consumerﬁnance.gov/data-research/ﬁnancial-well-being-survey-data/

Di Domenico, S. I., Ryan, R. M., Bradshaw, E. L., & Duineveld, J. J. (2022). Motivations for

personal financial management: A self-determination theory perspective. Frontiers in

Psychology, 13(3). https://doi.org/10.3389/fpsyg.2022.977818

Das, S., & Nayak, J. (2022). Customer segmentation via data mining techniques: State-of-the-art

review. Computational Intelligence in Data Mining (pp. 489–507). Springer.

https://doi.org/10.1007/978-981-16-9447-9_38

Diener, E., Emmons, R. A., Larsen, R. J., & Griﬃn, S. (1985). The Satisfaction With Life Scale.

Journal of Personality Assessment, 49(1), 71–75.

https://doi.org/10.1207/s15327752jpa4901_13

Diener, E., Suh, E. M., Lucas, R. E., & Smith, H. L. (1999). Subjective well-being: Three

decades of progress. Psychological Bulletin, 125(2), 276–302.

https://doi.org/10.1037/0033-2909.125.2.276

Diener, E., Wirtz, D., Tov, W., Kim-Prieto, C., Choi, D., Oishi, S., & Biswas-Diener, R. (2010).

New well-being measures: Short scales to assess ﬂourishing and positive and negative

feelings. Social Indicators Research, 97(2), 143–156.

https://doi.org/10.1007/s11205-009-9493-y

Embretson, S. E., & Reise, S. P. (2000). Item Response Theory for Psychologists. Mahwah, NJ:

Lawrence Erlbaum Associates.

47

---

<!-- PAGE 49 -->

Fabrigar, L. R., & Wegener, D. T. (2012). Exploratory Factor Analysis. New York, NY: Oxford

University Press.

Financial Health Network. (2018). Eight Indicators of Financial Health. Retrieved from

https://ﬁnhealthnetwork.org/research/ﬁnancial-health-score/

Garbinsky, E. N., Klesse, A.-K., & Aaker, J. (2014). Money in the bank: Feeling powerful

increases saving. Journal of Consumer Research, 41(3), 610–623.

https://doi.org/10.1086/676965

Gathergood, J. (2012). Self-control, ﬁnancial literacy and consumer over-indebtedness. Journal

of Economic Psychology, 33(3), 590–602.  https://doi.org/10.1016/j.joep.2011.11.006

Ghojogh, B., Ghodsi, A., Karray, F., & Crowley, M. (2021). Uniform Manifold Approximation

and Projection (UMAP) and Its Variants: Tutorial and Survey. arXiv preprint

arXiv:2109.02508. https://doi.org/10.48550/arXiv.2109.02508

Gollwitzer, P. M. (1999). Implementation intentions: Strong eﬀects of simple plans. American

Psychologist, 54(7), 493–503. https://doi.org/10.1037/0003-066X.54.7.493

Grable, J. E., & Joo, S. H. (2004). Environmental and biopsychosocial predictors of ﬁnancial risk

tolerance. Journal of Financial Counseling and Planning, 15(1), 73–82.

Guan, N., Guariglia, A., Moore, P., Xu, F., & Al‑Janabi, H. (2022). Financial stress and

depression in adults: A systematic review. PLOS One, 17(2), e0264041.

https://doi.org/10.1371/journal.pone.0264041

Gudmunson, C. G., & Danes, S. M. (2011). Family ﬁnancial socialization: Theory and critical

review. Journal of Family and Economic Issues, 32(4), 644–667.

https://doi.org/10.1007/s10834-011-9275-y

48

---

<!-- PAGE 50 -->

Halkidi, M., Batistakis, Y., & Vazirgiannis, M. (2001). On clustering validation techniques.

Journal of Intelligent Information Systems, 17(2–3), 107–145.

https://doi.org/10.1023/A:1012801612483

Hobfoll, S. E. (1989). Conservation of resources: A new attempt at conceptualizing stress.

American Psychologist, 44(3), 513–524. https://doi.org/10.1037/0003-066X.44.3.513

Halandová, K. (2024). The inﬂuence of objective ﬁnancial well-being on life satisfaction.

Ekonomické rozhľady – Economic Review, 53(2), 131–149.

https://doi.org/10.53465/er.2644-7185.2024.2.131-149

Hofman, A., Lier, I., Ikram, M. A., van Wingerden, M., & Luik, A. I. (2023). Uncovering

psychiatric phenotypes using unsupervised machine learning: A data-driven symptoms

approach. European Psychiatry, 66(1), e27. https://doi.org/10.1192/j.eurpsy.2023.13

Jolliﬀe, I. T. (2002). Principal component analysis (2nd ed.). Springer.

https://doi.org/10.1007/b98835

Kahneman, D., & Tversky, A. (1979). Prospect theory: An analysis of decision under risk.

Econometrica, 47(2), 263–291.

Kaufman, L., & Rousseeuw, P. J. (2009). Finding groups in data: An introduction to cluster

analysis. John Wiley & Sons.

Klontz, B., Britt, S., & Archuleta, K. (2011). Financial therapy: A new approach to ﬁnancial

distress. Journal of Financial Therapy, 2(1), 1–8. https://doi.org/10.4148/jft.v2i1.451

Kokun, O., Serdiuk, L., & Lytvynenko, O. (2024). Psychological antecedents of life satisfaction.

Psychological Thought, 17(2). https://doi.org/10.37708/psyct.v17i2.975

49

---

<!-- PAGE 51 -->

Kyriazos, T. A. (2018). Applied psychometrics: Sample size and sample power considerations in

factor analysis (EFA, CFA) and SEM in general. Psychology, 9(8), 2207–2230.

https://doi.org/10.4236/psych.2018.98126

Lord, F. M. (1980). Applications of Item Response Theory to Practical Testing Problems.

Hillsdale, NJ: Erlbaum.

Lown, J. M. (2011). Development and validation of a ﬁnancial self-eﬃcacy scale. Journal of

Financial Counseling and Planning, 22(2), 54–63.

https://psycnet.apa.org/record/2013-19795-003

Luthans, F., Avolio, B. J., Avey, J. B., & Norman, S. M. (2007). Positive psychological capital:

Measurement and relationship with performance and satisfaction. Personnel Psychology,

60(3), 541–572. https://doi.org/10.1111/j.1744-6570.2007.00083.x.

Marquand, A. F., Rezek, I., Buitelaar, J., & Beckmann, C. F. (2016). Beyond lumping and

splitting: A review of computational approaches for stratifying psychiatric disorders.

Biological Psychiatry, 80(2), 137–150. https://doi.org/10.1016/j.bpsc.2016.04.002

McInnes, L., Healy, J., & Melville, J. (2018). UMAP: Uniform manifold approximation and

projection for dimension reduction. arXiv preprint arXiv:1802.03426.

https://doi.org/10.48550/arXiv.1802.03426

Mentus, V. (2017). Validity and reliability of subjective wellbeing indicators in sociological

research: The measurement of life satisfaction. Sociološki pregled, 51(1), 157–180.

https://doi.org/10.5937/socpreg1701157m

50

---

<!-- PAGE 52 -->

Miotto, R., Li, L., Kidd, B. A., & Dudley, J. T. (2016). Deep patient: An unsupervised

representation to predict the future of patients from the electronic health records.

Scientiﬁc Reports, 6, 26094. https://doi.org/10.1038/srep26094

Mõttus, R., Kandler, C., Bleidorn, W., Riemann, R., & McCrae, R. R. (2017). Personality traits

below facets: The consensual validity, longitudinal stability, heritability, and utility of

personality nuances. Journal of Personality and Social Psychology, 112(3), 474–490.

https://doi.org/10.1037/pspp0000100

Nazareth, N., & Reddy, Y. V. R. (2023). Financial applications of machine learning: A literature

review. Expert Systems with Applications, 213, 119640.

https://doi.org/10.1016/j.eswa.2023.119640

Netemeyer, R. G., Warmath, D., Fernandes, D., & Lynch Jr, J. G. (2018). How am I doing?

Perceived ﬁnancial well-being, its potential antecedents, and its relation to overall

well-being. Journal of Consumer Research, 45(1), 68–89.

https://doi.org/10.1093/jcr/ucx109

Ng, A.Y., Jordan, M.I., Weiss, Y., et al. (2002) On Spectral Clustering: Analysis and An

algorithm. Advances in Neural Information Processing Systems, 2, 849-856.

Pavot, W., & Diener, E. (2008). The Satisfaction With Life Scale and the emerging construct of

life satisfaction. The Journal of Positive Psychology, 3(2), 137–152.

https://doi.org/10.1080/17439760701756946

Peterson, C., & Seligman, M. E. P. (2004). Character strengths and virtues: A handbook and

classiﬁcation. Oxford University Press.

Prawitz, A. D., Garman, E. T., Sorhaindo, B., O'Neill, B., Kim, J., & Drentea, P. (2006).

InCharge ﬁnancial distress/ﬁnancial well-being scale: Development, administration, and

51

---

<!-- PAGE 53 -->

score interpretation. Journal of Financial Counseling and Planning, 17(1), 34–50.

https://doi.org/10.1037/t60365-000

Prochaska, J. O., & DiClemente, C. C. (1983). Stages and processes of self-change of smoking:

Toward an integrative model of change. Journal of Consulting and Clinical Psychology,

51(3), 390–395. https://doi.org/10.1037/0022-006X.51.3.390

Şenbabaoğlu, Y., Michailidis, G., & Li, J. Z. (2014). Critical limitations of consensus clustering

in class discovery.Scientiﬁc Reports, 4, 6207. https://doi.org/10.1038/srep06207

Seligman, M. E. P. (1975). Helplessness: On depression, development, and death. W.H. Freeman.

Seligman, M. E. P. (2011). Flourish: A visionary new understanding of happiness and

well-being. Free Press.

Serido, J., Shim, S., & Tang, C. (2013). A developmental model of ﬁnancial capability: A

framework for promoting a successful transition to adulthood. International Journal of

Behavioral Development, 37(4), 287–297. https://doi.org/10.1177/0165025413479476

Shim, S., Xiao, J. J., Barber, B. L., & Lyons, A. C. (2009). Pathways to life success: A

conceptual model of ﬁnancial well-being for young adults. Journal of Applied

Developmental Psychology, 30(6), 708–723.

https://doi.org/10.1016/j.appdev.2009.02.003

Strömbäck, C., Lind, T., Skagerlund, K., Västfjäll, D., & Tinghög, G. (2017). Does self-control

predict ﬁnancial behavior and ﬁnancial well-being? Journal of Behavioral and

Experimental Finance, 14, 30–38. https://doi.org/10.1016/j.jbef.2017.04.002

Thaler, R. H., & Sunstein, C. R. (2008). Nudge: Improving decisions about health, wealth, and

happiness. Yale University Press.

52

---

<!-- PAGE 54 -->

Thompson, P. (2021). A study of the ﬁnancial crisis and its eﬀect on psychological well-being,

health, satisfaction, and ﬁnancial incapability. Research Square.

https://doi.org/10.21203/rs.3.rs-393768/v1

Thompson, P. W. (2023). Financial crisis and its eﬀect on psychological well-being, health,

satisfaction, and ﬁnancial incapability: A systematic review. Pakistan Journal of Medical

and Health Sciences, 17(3), 511–517. https://doi.org/10.53350/pjmhs2023173511

Trope, Y., & Liberman, N. (2010). Construal-level theory of psychological distance.

Psychological Review, 117(2), 440–463. https://doi.org/10.1037/a0018963.

Vallacher, R. R., & Wegner, D. M. (1987). What do people think they're doing? Action

identiﬁcation and human behavior. Psychological Review, 94(1), 3–15.

https://doi.org/10.1037/0033-295X.94.1.3

von Luxburg, U. (2010). Clustering stability: An overview. Foundations and Trends in Machine

Learning, 2(3), 235–274. https://doi.org/10.1561/2200000008

Xiao, J. J., & O’Neill, B. (2016). Consumer ﬁnancial education and ﬁnancial capability.

International Journal of Consumer Studies, 40(6), 712–721.

https://doi.org/10.1111/ijcs.12285

Yarkoni, T., & Westfall, J. (2017). Choosing prediction over explanation in psychology: Lessons

from machine learning. Perspectives on Psychological Science, 12(6), 1100–1122.

https://doi.org/10.1177/1745691617693393

Zadhasan, Z. (2024). Predictors of life satisfaction: The role of mindfulness and locus of control.

Journal of Personality and Psychosomatic Research, 2(1), 4–9.

https://doi.org/10.61838/kman.jppr.2.1.2

53

---

<!-- PAGE 55 -->

Zhang, Z. (2021). Cluster analysis of consumer's behaviors based on unsupervised learning. In

Proceedings of the 2021 3rd International Conference on Artiﬁcial Intelligence and

Advanced Manufacture (pp. 1178–1184). ACM.

https://doi.org/10.1145/3495018.3495360

54

---

<!-- PAGE 56 -->

Appendix A: Domain Composition for Clustering and Validation

A1. Proprietary Dataset Sample Items

1.  “I am conﬁdent I can make wise ﬁnancial decisions even under pressure.”

2.  “I can conﬁdently navigate uncertain ﬁnancial waters.”

3.  “I believe I can reach my long-term ﬁnancial goals through persistent eﬀort.”

4.  “I do not give up on my ﬁnancial goals easily.”

5.  “Unexpected expenses totally stress me out.”

6.  “I lie awake in bed at night because I am worried about my ﬁnancial future.”

7.  “When I get a bill notiﬁcation, it feels like a threat or warning.”

8.  “I often avoid looking at my checking or credit card statement to avoid seeing how much

I’ve spent.”

9.  “Actually, I gave up trying to keep track of my income and expenses.”

10. “I enjoy learning about personal ﬁnancial management.”

11. “I actively seek new information about how I can manage my money eﬀectively.”

12. “I see the big picture when planning my ﬁnances.”

A2. CFPB Dataset

Capability:

FS1_1-FS1_6, FS2_1-FS2_3, GOALCONF, SELFCONTROL_1-SELFCONTROL_3

Measures perceived ﬁnancial skills, conﬁdence, sense of control, and self-regulatory

capacity.

Budgeting & Saving:

MANAGE1_1-MANAGE1_4, SAVEHABIT, FRUGALITY, ABSORBSHOCK,

ENDSMEET, SCFHORIZON

55

---

<!-- PAGE 57 -->

Captures day-to-day money management practices, saving habits, frugality, and

short-term ﬁnancial resilience.

Planning:

PROPPLAN_1-PROPPLAN_4, ACT1_1, ACT1_2, ASK1_1, ASK1_2, FINGOALS

Assesses planning behaviors, proactive ﬁnancial organization, and the extent to which

individuals set and act on ﬁnancial goals.

Social & Relational:

FINSOC2_1-FINSOC2_7

Measures access to social and interpersonal support, relational resources, and ﬁnancial

well-being derived from social networks.

Financial Literacy:

FK1correct - FK3correct, KH1correct -KH9correct

Measures ﬁnancial knowledge, understanding of compound interest, diversiﬁcation, risk.

LifeSatisfaction:

SWB_1 - SWB_3

Captures global cognitive evaluations of life quality.

Perceived Financial Health:

FWB1_1-FWB1_6, FWB2_1-FWB2_4

Uses standard 10-item Financial Well-Being Scale.

Material Hardship:

MATHARDSHIP_1 - MATHARDSHIP_6, DISTRESS, HOUSING

Captures experiences of material hardship and acute ﬁnancial stress.

56

---

<!-- PAGE 58 -->

The Social & Relational domain is excluded from the clustering inputs because it exhibits very

low structural variability (at most 128 possible combinations), providing broad global gradients

rather than ﬁne-grained psychological information. Including such low-variability domains in a

nonlinear manifold risks collapsing the embedding onto a single severity axis, overshadowing the

richer multi-dimensional variation captured by the core behavioral and psychological domains.

For this reason, this domain is retained only for post-hoc interpretation and validation of the ﬁnal

cluster solution.

See CFPB survey codebook for additional information

Appendix B: Benchmarking Data Representations and Clustering Methods

To develop a stable and psychologically interpretable clustering pipeline, we conducted three

complementary analyses. First, we examined the geometric properties of the psychometric

domains (Stage 1) to determine whether linear dimensionality reduction (e.g., PCA) could

adequately preserve global and local structure, or whether nonlinear embedding was required.

Second, we benchmarked alternative low-dimensional representations (raw domain scores, PCA

projections, UMAP embeddings) to evaluate their suitability for Stage 2 clustering. Third, within

the preferred representation, we compared several clustering approaches to assess their

qualitative stability and alignment with known behavioral structure. Together, these analyses

provide an empirical foundation for the dimensionality-reduction and clustering choices used in

the main framework.

B.1 Benchmarking Linear vs. Nonlinear Representations in Stage 1

To evaluate whether a linear method such as PCA could adequately serve as the Stage 1

dimensionality reduction step, we assessed domain-level geometry using three complementary

diagnostics:

57

---

<!-- PAGE 59 -->

1.  Global linearity: the proportion of variance explained by the ﬁrst principal component

(PC1).

2.  Local tangent alignment: the mean ∣cos θ∣ between the domain-level PC1 axis and

local one-dimensional PCA directions estimated from each participant’s 20-nearest

neighbors.

3.  Neighborhood preservation: trustworthiness and continuity comparisons between PCA

and UMAP.

Global Linearity (PC1 Variance): Across domains, PC1 captures only 35–59% of total

variance, indicating that no domain is dominated by a single global linear axis. This suggests that

Stage 1 representations must account for multi-dimensional or curved manifold structure rather

than relying on a single major linear direction.

Local Tangent Alignment: Local tangent–global axis alignment is modest, with mean ∣cos θ∣

values ranging from 0.38 to 0.67 (median values ≈ 0.37–0.74 across domains). These moderate

alignments indicate substantial curvature or heterogeneous local variance structures, further

suggesting that a strictly linear mapping such as PCA is unable to capture the local geometry that

Stage 1 must preserve.

Neighborhood Preservation: PCA with two components shows consistently weaker

neighborhood preservation compared with UMAP.

●  Trustworthiness: PCA ≈ 0.81–0.91, UMAP ≈ 0.94–0.98

●  Continuity: PCA ≈ 0.93–0.96, UMAP ≈ 0.96–0.99

Even when PCA is expanded to four components, UMAP matches or exceeds it across most

domains in both metrics, underscoring that the latent structures underlying these psychometric

58

---

<!-- PAGE 60 -->

domains are meaningfully nonlinear.

Across diagnostics--global variance structure, local tangent geometry, and neighborhood

preservation--PCA fails to capture the nonlinear manifold characteristics present in the

domain-level data. UMAP provides substantially better preservation of both local and global

structure, supporting its use as the Stage 1 embedding method.

B.2 Benchmarking Linear vs. Nonlinear Representations in Stage 2

We evaluated whether nonlinear embedding is necessary for identifying stable clusters by

comparing clustering performance across three representations: raw domain scores, linear PCA

projections, and UMAP embeddings. Although t-SNE is a popular nonlinear visualization tool, it

does not preserve global structure and is not suitable for graph-based clustering; therefore, it was

excluded from quantitative comparison. Because the proprietary and CFPB datasets diﬀer in size

and sampling density, results are reported separately.

Proprietary dataset: This dataset exhibits relatively strong inherent structure, reﬂected in higher

absolute silhouette values across all representations. Clustering on raw domain scores produced a

silhouette of approximately 0.17. PCA projections improved separation modestly (≈0.38 in 2D;

≈0.20 in 4D). UMAP yielded the clearest manifold structure and the strongest separation (≈0.56).

CFPB dataset: In this larger and denser dataset, clustering on raw domain scores again produced

weak separation (≈0.23), indicating that the cross-domain space is not linearly separable. PCA

oﬀered only modest improvement (≈0.32). UMAP achieved substantially stronger separation

(≈0.50) and outperformed linear methods on Calinski–Harabasz and Davies–Bouldin indices,

consistent with meaningful nonlinear structure in the data.

Across both datasets, linear representations--either raw space or PCA--are unable to

recover the nonlinear geometry required for stable, interpretable clustering. UMAP produced

59

---

<!-- PAGE 61 -->

markedly stronger separability and more coherent manifold structure, supporting its use as the

Stage 2 embedding in the proposed framework.

B.3 Algorithmic Evaluation of Clustering Methods

Several clustering algorithms are evaluated on the UMAP embeddings

K-means: Considered for its simplicity and widespread use, K-means consistently

underperformed. Its assumption of convex, spherical clusters conﬂicted with the observed

structure of the UMAP space. The resulting clusters lacked behavioral coherence, and internal

validation metrics (e.g., silhouette score) are poor.

DBSCAN and HDBSCAN: Density-based methods showed initial promise but proved unstable.

DBSCAN often merged distinct subgroups, while HDBSCAN labeled large portions of the data

as noise. Both are highly sensitive to parameter settings (e.g., min_samples, min_cluster_size),

and qualitative inspection revealed weak alignment with psychological or behavioral patterns.

Agglomerative Clustering: This method was more stable than density-based approaches and

delivered modest performance. However, the absence of a clear criterion for selecting the optimal

number of clusters, along with weaker separation metrics, limited its usefulness.

Spectral Clustering: Spectral Clustering demonstrated the strongest performance across both

quantitative and qualitative criteria. It is well-suited to capturing non-convex cluster shapes and

leverages the pairwise similarity structure preserved in the UMAP embedding.

Appendix C: Dimensionality Reduction, Clustering, and Classification Hyperparameters

Supplemental Table C1  
UMAP parameters for domain-level (Stage 1) and composite embeddings (Stage 2)

Dataset

Domain

n_neighbors  n_components  min_dist

spread

local_connectivity

Proprietary  Character Strengths

Attitudes & 
Capabilities

24

24

15

15

.8

.8

1.00

1.00

1

1

60

---

<!-- PAGE 62 -->

Psychological Capital

Motivation

Financial Behavior

Positive Functioning

Composite Embedding

CFPB

Capability

Budgeting & Saving

Planning

Composite Embedding

Supplemental Table C2  
Spectral Clustering parameters (Stage 2)

22

26

26

21

15

37

16

17

24

8

8

8

5

2

5

5

5

2

.6

.6

.6

.4

.0

.6

.6

.7

.02

1.00

1.00

1.00

1.00

.3

1.00

1.00

1.00

1.2

1

1

1

1

7

1

1

1

7

Dataset

n_clusters

aﬃnity

gamma

eigen_solver

Proprietary

CFPB

7

7

rbf

rbf

8.00

2.53

arpack

arpack

Supplemental Table C3  
Imputation details

Component

Parameter

Value

IterativeImputer

estimator

max_iter

RandomForestRegressor

10

initial_strategy

mean

imputation_order

ascending

skip_complete

True

min_value

0 for binary, 1 for Likert

max_value

1 for binary, 5 for Likert

RandomForestRegressor

n_estimators

max_depth

250

15

Supplemental Table C4 
Classiﬁcation details

Component

Feature Selection (ExtraTreesClassifier)

Parameter

n_estimators

Value

1000

61

---

<!-- PAGE 63 -->

Ensemble Classifier (VotingClassifier)

RandomForestClassifier (model_0)

SVC (model_1)

max_depth

voting

None

soft

base estimators

RandomForestClassifier, SVC

n_estimators

max_depth

max_features

min_samples_leaf

criterion

bootstrap

kernel

degree

C

gamma

probability

shrinking

150

10

log2

2

gini

False

poly

2

0.5

0.05

True

False

Appendix D: Harmonization of Domains Across Datasets

D1. Domain Harmonization

To explore cross-dataset alignment, we develop a uniﬁed ﬁve-domain conceptual space shared by

both instruments. The goal of this harmonization is to align instrument-speciﬁc domains

according to their underlying psychological functions rather than their exact item structure or

naming conventions. This approach emphasizes functional equivalence rather than item-level

correspondence: each conceptual domain aggregates the set of original domains that, within each

instrument, represent similar underlying processes (e.g., agency, planning, execution, or

motivation). Below we summarize the domain mappings used for the analysis.

Supplemental Table D1 
Domain Harmonization Mapping

Conceptual Domain

Proprietary Domains

CFPB Domains

Financial Behavior

Financial Behavior

Budgeting & Saving

62

---

<!-- PAGE 64 -->

Financial Literacy

Financial Literacy

Financial Literacy

Positive Functioning

Positive Functioning

Social & Relational Support

Psychological Resources

Attitudes & Capabilities; Psychological 
Capital; Character Strengths

Motivation & Planning

Motivation

Capability

Planning

Note. Mappings reﬂect correspondence at the level of higher-order psychological constructs rather than item-level equivalence. 
CFPB Social & Relational Support captures aspects of the broader Positive Functioning domain in the proprietary instrument, and 
CFPB Planning reﬂects the behavioral expression of the same organizational tendencies represented in the proprietary Motivation 
domain. These conceptual parallels allow the two datasets to be harmonized within a shared domain space, even though speciﬁc 
item content diﬀers. No direct CFPB analogue exists for proprietary Financial Construal constructs.

Because the instruments diﬀer in the number and granularity of available scales, some conceptual

domains are formed by averaging multiple source domains, while others correspond to a single

scale. For conceptual domain Dk composed of nk source domains si , the harmonized score for a

participant is the simple mean:

𝐷

𝑘

= 1
𝑛

𝑛
𝑘
∑ 𝑠

𝑘 𝑖−1

. This transformation preserves relative standing on 
𝑖

the underlying constructs even when item content diﬀers.

D2. Cross-Dataset Cluster Alignment

Since clusters are identiﬁed independently within each dataset using the full set of original

domain scores, to compare clusters across datasets, we represent each cluster by a harmonized

cluster proﬁle: a vector of mean scores on the ﬁve harmonized domains. For cluster c containing

Nc individuals and harmonized domain j:

𝐷

𝑐,𝑗

=   1
𝑁

∑ 𝐷

𝑐 𝑛ϵ𝑐

.  Each harmonized cluster is

𝑛,𝑗

therefore represented by a 5-dimensional proﬁle vector:

𝐷

𝑐

=  (𝐷

constitute the basis for cross-dataset comparison.

, … ,  𝐷

)
𝑐,5

𝑐,1

. These vectors

We evaluate similarity between clustering solutions using several complementary metrics

that capture local proximity, ordinal correspondence, and global geometric alignment. First,

63

---

<!-- PAGE 65 -->

pairwise cluster proximity is summarized using the Cluster-Pair Similarity Index (CPSI), a

normalized inverse-distance measure computed from Euclidean distances between five-domain

cluster profiles. CPSI rescales distances onto an interpretable similarity scale ranging from 0 to

1, with larger values indicating more similar profiles:

𝐶𝑃𝑆𝐼

𝑖,𝑗

=

1
1+𝑑(𝑖,𝑗)

, where d(i,j) denotes the

Euclidean distance between cluster i and cluster j in the unified five-domain space.  CPSI is used

descriptively and does not impose a one-to-one correspondence between clusters.

Second, we derive a shared global functioning axis by applying principal component

analysis (PCA) to the pooled set of proprietary and CFPB cluster centroids, each represented as a

five-dimensional domain profile. The first principal component (PC1) defines a one-dimensional

gradient summarizing dominant variation across clusters in the harmonized domain space. Each

cluster receives a score on this axis, and cross-dataset alignment in relative cluster ordering is

assessed using the Spearman rank correlation between PC1 scores, with higher correlation

values indicating stronger agreement in cluster ordering across datasets.

Finally, to assess configuration-level geometric similarity, we apply Procrustes analysis

to the proprietary and CFPB centroid matrices expressed in the unified domain space. Procrustes

analysis identifies the optimal rotation and scaling that best superimposes one configuration onto

the other. Geometric similarity is quantified using the Procrustes disparity, defined as the squared

Frobenius norm of the residual matrix after optimal alignment:

|
|
𝐷  = 𝑋 − 𝑌

*

|

|

2
, where X

denotes the matrix of proprietary cluster centroids (rows = clusters, columns = domains) and Y∗

denotes the optimally transformed CFPB centroid matrix. Lower disparity values indicate greater

similarity in the overall spatial organization of clusters across datasets.

D3. Interpretation Caveats

It is important to note several interpretation caveats. The harmonized domains represent

64

---

<!-- PAGE 66 -->

conceptual correspondences, not item-level equivalences, and thus should not be interpreted as

measuring the same constructs with identical psychometric content. Averaging across

contributing scales preserves relative diﬀerences, proﬁle shape, and cross-domain patterns, but

does not reproduce ﬁne-grained item structure or latent-factor detail. Comparisons therefore

reﬂect similarity in high-level psychological organization, not equality of measurement precision

or scale composition. Finally, magnitude diﬀerences across datasets (for example, compression

of variation in the CFPB domains) are expected given diﬀerences in survey breadth and scale

design. Alignment metrics are consequently interpreted in terms of pattern, ordering, and overall

conﬁguration, which provide more stable and meaningful indicators of structural correspondence

across instruments.

Supplemental Table S1 
Descriptive statistics for each psychometric domain 
Reports the number of items, scale ranges, descriptive statistics, and internal consistency (Cronbach’s α) for each 
domain. All domains exhibit adequate variability and reliability for unsupervised modeling.

Domain

# Items

Scale Range

Mean

SD  Min  Max

Cronbach's α

Proprietary Dataset

Character Strengths

Attitudes & Capabilities

Psychological Capital

Motivation

Financial Behavior

Positive Functioning

Financial Construal Level

Financial Literacy

Life Satisfaction

Perceived Financial Health

Psychological Well-Being

CFPB Dataset

Capabilities

21

17

8

14

11

9

10

5

5

10

6

13

1–5

1–5

1–5

1–5

1–5

1–5

0/1

0/1

1–5

1–5

1–5

3.76

2.74

3.78

2.99

3.25

3.19

0.65

0.84

3.33

2.94

3.07

1.18

1.00

5.00

1.40

1.00

5.00

1.02

1.00

5.00

1.47

1.00

5.00

1.46

1.00

5.00

1.46

1.00

5.00

0.47

0.00

1.00

0.21

0.00

1.00

1.14

1.00

5.00

1.41

1.00

5.00

1.37

1.00

5.00

0.930

0.897

0.894

0.823

0.875

0.856

0.651

0.461

0.865

0.922

0.570

1–4/1–5

3.35

0.93

1.00

5.00

0.878

65

---

<!-- PAGE 67 -->

Planning

Budgeting & Saving

Social & Relational

Financial Literacy

Life Satisfaction

Perceived Financial Health

Material Hardship

9

9

7

12

3

10

8

1–5, 0/1

1–5/1–6

3.25

3.97

1.35

1.00

5.00

1.31

1.00

6.00

0/1

0/1

1–7

1–5

1–3/1–5

0.51

0.50

0.00

1.00

0.74

5.44

3.35

2.81

0.44

0.00

1.00

1.44

1.00

7.00

1.20

1.00

5.00

0.59

1.00

5.00

0.803

0.796

0.779

0.688

0.793

0.917

0.754

Note: Financial Literacy items are scored 1 = correct, 0 = incorrect, and the domain score reﬂects the proportion 
answered correctly.

Supplemental Table S2. Outcome diﬀerentiation by cluster membership.   
This table reports the results of one-way ANOVA examining how cluster membership predicts three outcome 
variables: Life Satisfaction, Psychological Well-Being, Material Hardship, and Perceived Financial Health.  
Proprietary=df(6, 330), CFPB=df(6, 5890)

Outcome

SSB

SSW

F

Partial η²  Levene’s W  Levene’s p

Proprietary Dataset

Life Satisfaction

3.146

13.330

12.984

0.191

0.68

Psychological Well-Being

2.283

6.309

19.904

0.266

1.99

Perceived Financial Health

11.849

7.691

84.732

0.606

7.03

0.667

0.067

<.001

CFPB Dataset

Life Satisfaction

1247.742

7398.907  165.546

0.144

24.72

< .001

Material Hardship

174.600

568.844

301.310

0.234

112.63

< .001

Perceived Financial Health

1996.911

2558.232  766.271

0.438

18.84

< .001

Note. Partial η² is reported as eﬀect size. Levene’s test p-values assess homogeneity of variance. In the proprietary 
dataset (N = 337), cluster sizes are reasonably balanced (n = 25–71 per cluster), and observed eﬀect sizes are 
moderate to large (partial η² = .19–.61), supporting reliable estimation of between-cluster diﬀerences.

66

<!-- MARKITDOWN CONVERSION -->

<!-- Full MarkItDown conversion for formatting fidelity. -->

Mapping Financial Mindsets: A Two-Stage Unsupervised Framework for Behavioral
Profiling Using High-Dimensional Psychometric Data
Irina Rabinovich1, Rikki Rabinovich2, Nick Ashburn1,3, Moraya DeGeare1,4
Abstract
Financial well-being reflects a complex interplay of psychological traits, behaviors, and
knowledge, yet most segmentation approaches rely on limited indicators such as spending
patterns or socio-demographic data, overlooking behavioral and psychometric factors. This paper
proposes a novel methodological framework for psychometric segmentation that models complex
interactions across multiple psychometric domains, enabling the identification of latent profiles
of financial mindset and behavior. We demonstrate the utility of the framework by applying it to
two distinct datasets--a proprietary financial assessment (N = 337) and the nationally
representative U.S. CFPB Financial Well-Being Survey (N = 5,897). In both applications, the
approach yields psychologically interpretable profiles, exhibits strong internal stability, and
shows consistent associations with life satisfaction, psychological well-being, and financial
health. Rather than prescribing a single population taxonomy, our goal is to provide a replicable
and scalable procedure for identifying meaningful behavioral patterns within any financial
population. This makes the approach well suited to behavioral finance applications including
financial advising, wellness interventions, and the design of personalized tools and
communications aimed at improving financial decision-making and well-being.
1. Introduction
Financial well-being is increasingly recognized as a multidimensional construct that includes not
only objective indicators, such as income, savings, and debt, but also subjective experiences,
1 Calibrate, Inc; 2 Department of Neurosurgery, University of Utah; 3 Drexel University, 4 BFF Therapy

including financial stress, confidence, and perceived control (Brüggen et al., 2017; CFPB, 2015a;
Netemeyer et al., 2018). It reflects both behavioral and psychological aspects, demanding
assessment tools that go beyond financial conditions to account for beliefs, motivations, and
emotional responses. Traditional methods for classifying individuals in the financial domain have
typically relied on spending patterns or demographic factors and have therefore often overlooked
the psychological patterns that influence how individuals perceive, relate to, and manage their
finances. Here, we define financial mindset as a multidimensional construct where capability,
motivation, psychological resources, and enacted behavior intersect to shape decision-making.
This perspective aligns with our clustering framework, which seeks to identify patterns in how
these dimensions co-occur across individuals. The resulting clusters represent distinct profiles of
how individuals organize and regulate their financial lives.
This paper makes three contributions. First, it addresses the challenge of modeling
multifaceted psychological constructs and their interdependencies in behavioral profiling. To this
end, it introduces a methodological framework that integrates domain-specific manifold learning
with spectral clustering to identify nonlinear patterns in psychometric and behavioral data.
Second, it tests the framework across two distinct datasets--one proprietary and psychometrically
rich, the other large-scale and nationally representative -- demonstrating how this framework
reveals psychologically coherent patterns of financial mindsets that are not captured by
conventional linear or demographic segmentation approaches. Third, as the results of the
application to the two distinct datasets show, it provides preliminary evidence that the proposed
approach reveals a reliable underlying structure – showing consistent separability and stability
across different instruments, populations, and survey formats, even if the specific profiles differ.
Applying this two-stage unsupervised learning framework, we identify emergent
1

behavioral profiles that capture complex nonlinear relationships missed by standard
factor-analytic or demographic approaches. We evaluate these profiles internally using structural
metrics of cluster coherence and externally by demonstrating robust associations with outcome
indicators, namely, life satisfaction, psychological well-being, and financial health. We also show
that these external indicators are far more strongly associated with the learned profiles than with
socio-demographic variables such as age, education, or income, underscoring the distinctive
value of psychometric and behavioral dimensions for understanding heterogeneity in financial
well-being. Finally, we show that demographic variables alone provide only limited predictive
power for cluster membership, indicating that the framework captures behavioral–psychological
structure that is not reducible to age, income, or education.
To demonstrate the utility of the proposed framework, we apply it to two very different
datasets: a proprietary assessment with deep psychometric coverage and the U.S. CFPB
Financial Well-Being Survey, which uses a different item structure and response format. Despite
these differences, the approach consistently identifies interpretable, psychologically coherent
profiles that share a common structural organization and exhibit strong internal structure and
meaningful associations with external outcomes.
By decoupling the modeling methodology from any specific survey instrument, the
framework opens the door to scalable application for academic research, personalized fintech
solutions, and even clinical applications where financial behavior may inform intervention
strategies.
2. Background & Related Work
In this section we review core concepts from behavioral finance and psychometrics that underpin
our framework. We also highlight relevant applications of machine learning in the behavioral
2

sciences and examine prior attempts to assess financial well-being through multidimensional
measurement.
2.1 Behavioral Finance and Psychometrics
Behavioral finance integrates psychological theories into economic models to better explain
real-world financial decision-making, recognizing that individuals are often influenced by
cognitive biases, emotions, and heuristics rather than strict rationality (Kahneman & Tversky,
1979). Psychometric approaches complement this perspective by using validated instruments to
quantify individual differences in traits such as risk tolerance, financial anxiety, and internalized
money beliefs or “scripts” (Grable & Joo, 2004; Klontz et al., 2011; Lown, 2011).
A growing body of evidence shows that psychological traits, like self-control, optimism,
and emotional regulation, are strongly associated with financial behaviors (e.g., saving, spending,
and investing) and contribute to broader measures of well-being (Gathergood, 2012; Shim et al.,
2009; Xiao & O’Neill, 2016). Perceived psychological power has also been shown to promote
financial behaviors like saving, highlighting the affective and motivational dimensions of
financial decision-making (Garbinsky et al., 2014). The integration of psychometrics into
financial assessments improves the predictive accuracy of financial health outcomes by capturing
psychological contributors beyond financial variables alone (Serido et al., 2013). Building on this
foundation, our work fuses self-reported financial behavior constructs with multidimensional
psychological traits into a unified representation, enabling more precise behavioral profiling than
isolated domain-specific approaches.
2.2 Clustering and Dimensionality Reduction in Behavioral Sciences
Unsupervised learning methods have become increasingly valuable in the behavioral sciences,
enabling researchers to uncover natural groupings within complex behavioral datasets (Kaufman
3

& Rousseeuw, 2009; Yarkoni & Westfall, 2017; Zhang, 2021). In finance, these techniques have
primarily been applied to behavioral segmentation based on observable financial actions, credit
risk modeling, and product targeting (Nazareth, 2023). Dimensionality reduction methods such
as Principal Component Analysis (PCA) and Uniform Manifold Approximation and Projection
(UMAP1) aid in simplifying high-dimensional datasets while preserving structure relevant to
clustering (Jolliffe, 2002; McInnes et al., 2018). Combinations of nonlinear embedding and
graph-based clustering have been successfully applied in other domains, including genomics
(Becht et al., 2019), psychiatry (Marquand et al., 2016), and health informatics (Miotto et al.,
2016), where they have enabled the discovery of complex latent structure that is difficult to
recover with linear or centroid-based methods. However, applications of these approaches to
financial–psychometric segmentation remain limited.
Unsupervised learning is particularly appealing in contexts where ground-truth labels are
unavailable or poorly defined, allowing researchers to detect latent patterns inherent in the data.
In the context of our study, these methods can reveal psychologically meaningful profiles,
especially when working with rich psychometric or behavioral data that is difficult to analyze
directly. However, critiques of unsupervised methods note their sensitivity to parameter choices,
potential instability across different samples, and challenges in validating clusters against
external criteria (Şenbabaoğlu et al., 2014; von Luxburg, 2010). We address these concerns
through internal validation metrics, external outcome associations, and replication across
independent samples with different survey structures.
Recent studies have successfully applied unsupervised methods to reveal latent structure in
1 A dimensionality reduction technique that transforms high-dimensional data (e.g., multiple questionnaire scores) into a lower-dimensional
representation while preserving underlying structure. It facilitates pattern recognition and visualization.
4

other (not financial) psychological domains. For example, Hofman et al. (2023) used hierarchical
clustering to identify stable subtypes of depression and anxiety symptoms in a large-scale
population study, while Mõttus et al. (2017) demonstrated the predictive utility of fine-grained
personality trait clustering for life outcomes. These studies highlight the potential of clustering
to uncover psychologically meaningful profiles that support both explanatory modeling and
tailored interventions. We go beyond these innovations and apply UMAP and Spectral Clustering
to integrated psychometric and self-reported financial behavior data, generating psychologically
interpretable behavioral-financial profiles grounded in latent structure.
2.3 Prior Approaches to Financial Well-Being Assessment
While traditional assessments of financial well-being have evolved to include subjective
indicators such as financial stress, perceived control, and self-efficacy (CFPB, 2015b; Netemeyer
et al., 2018), they remain limited in psychological scope. Tools like the CFPB Financial
Well-Being Scale and the InCharge Distress Scale (Prawitz et al., 2006), though
psychometrically strong (α ≈ 0.87), primarily assess emotional strain and perceived hardship.
They omit motivational drivers, behavioral consistency, and self-regulatory capacity. Similarly,
financial literacy assessments such as the OECD/INFE Toolkit (Atkinson & Messy, 2012)
emphasize knowledge but not emotional readiness to act. This is a critical omission, since traits
like impulsivity, perseverance, and low self-efficacy often inhibit behavior change, regardless of
knowledge.
Psychological constructs such as locus of control, psychological capital, and financial
self-efficacy have been linked to financial behaviors (Grable & Joo, 2004; Lown, 2011; Serido et
al., 2013), but they are typically modeled in isolation or examined using supervised methods.
This obscures how multiple traits co-occur in practice and limits the discovery of latent
5

psychological configurations. Machine learning in fintech, while increasingly common (Das &
Nayak, 2022; Zhang, 2021), prioritizes what users do (observable output) over why they do it
(internal psychological structure), limiting the ability to predict how financial stress will impact
decision-making.
The present study addresses these limitations by clustering a comprehensive set of
psychometric and behavioral measures to reveal interpretable financial well-being profiles. By
modeling the co-occurrence structure across domains, the framework uncovers psychologically
meaningful patterns that are difficult to detect using linear or domain-isolated approaches. These
profiles do not represent fixed “types” but rather data-driven configurations that capture how
traits, behaviors, and motivations align within and across individuals. This structure enables
richer descriptive insight, supports hypothesis generation for future theory-building, and can
inform targeted interventions in financial advising and wellness contexts.
3. Framework Overview
The framework begins by organizing questionnaire items into conceptually coherent domains,
each representing a distinct psychological or behavioral construct (e.g., motivation, planning,
financial literacy). Domain partitioning is essential because psychometric surveys typically
contain a heterogeneous mix of measurement formats--binary indicators, multi-level Likert
items, and scales with different response ranges. Even when items are rescaled to a common
numeric range, the combined item space remains geometrically inconsistent: binary items create
abrupt, discontinuous jumps in response patterns; Likert items introduce smooth graded
variation; and items from unrelated constructs add uncorrelated or orthogonal sources of
variance. When these heterogeneous items are analyzed or clustered directly at the item level, the
resulting structure is often dominated by measurement artifacts rather than underlying behavioral
6

organization, leading to clusters that change unpredictably across seeds or algorithms. Indeed, we
are unable to obtain interpretable item-level clusters in either dataset used in this study, even after
applying dimensionality reduction to raw responses. In contrast, partitioning the survey into
domains preserves construct-level coherence: items designed to measure the same latent trait are
modeled together, while variation across constructs is deferred to later stages. The domain
structure provides the foundation for Stage 1 of the framework, which produces continuous,
domain-level scores for each participant. These domain scores then serve as the standardized,
psychometrically meaningful inputs to Stage 2, which identifies behavioral clusters based on the
joint distribution of domains. Figure 1a provides an overview of the full two-stage dataflow.
3.1. Considerations of Domain Depth and Response Variability
To produce a meaningful domain-level representation, the domain must have sufficient response
resolution, i.e., items within a domain must collectively span a sufficiently rich set of response
patterns to capture meaningful distinctions among individuals. Domains with very few items or
coarse response scales yield a limited set of possible response patterns, making it difficult to
differentiate individuals or summarize the construct along a continuum. In practice, domains
intended to reflect broad, multi-faceted constructs typically require enough item-level richness –
at least six to eight items with nontrivial variability – to behave like continuous dimensions. By
contrast, domains designed to measure narrow or tightly defined attributes (e.g., financial literacy,
numeracy, construal level, or short-form affective or motivational mini-scales) naturally exhibit
lower variability and fewer response combinations; these domains are scored using simpler
approaches that reflect their focused scope. Domains with insufficient response resolution for
continuous differentiation are excluded from the clustering stage but may be retained for
interpretive or validation analyses. These considerations determine how each domain is handled
7

within the framework’s scoring procedures introduced below.
3.2 Stage 1: Producing Unidimensional Domain Scores
There are multiple valid ways to construct a domain-level score once items have been grouped
into coherent constructs, and the appropriate approach depends on the statistical and
psychometric properties of the domain. In this paper, we explore three such strategies, chosen to
illustrate how the framework can adapt domain scoring to different structural patterns. Other
scoring approaches--such as projections in the original item space or alternative aggregation
schemes--are also feasible, but evaluating all possible variants lies beyond the scope of the
present study.
3.2.1 Anchor Projection Score
For medium- to high-dimensional domains with nonlinear relationships between the items,
heterogeneous item formats, and high response resolution, we apply dimensionality reduction
followed by anchor-based projection. By embedding high-dimensional response patterns into a
lower-dimensional space, dimensionality reduction can mitigate redundancy, noise, and uneven
scaling, thereby improving interpretability and support downstream clustering. In principle, both
linear methods, such as principal component analysis (PCA), and nonlinear manifold learning
techniques, such as UMAP, can be used. Linear methods assume that domain structure is well
approximated by a global linear subspace and are effective when item relationships are
predominantly linear. Nonlinear methods relax this assumption by allowing local neighborhoods
to be preserved even when the global structure is curved. Note that some nonlinear approaches,
such as t-SNE, are primarily optimized for visualization and do not preserve global geometry or
support stable one-dimensional parametrization, making them less suitable for domain scoring in
the present context.
8

To guide method selection, we assess the geometric structure of each domain using
several complementary diagnostics. One indicator is the variance explained by the first principal
component, which reflects the dominance of a single linear dimension. We also quantify
nonlinearity using a tangent-alignment index, defined as the mean absolute cosine similarity
between the global PC1 direction and local one-dimensional PCA tangents estimated from each
participant’s 20 nearest neighbors. Domains with high PC1 dominance and tangent alignment
near 1.0 behave approximately linearly, whereas lower values indicate curved latent structure. As
an additional check, we evaluate whether linear projections adequately preserve neighborhood
relationships using trustworthiness and continuity metrics.
Once a domain representation is obtained, we convert each participant’s
multidimensional coordinates into a unidimensional domain score using a deterministic
anchor-based projection. For each domain, we define two deterministic anchor profiles: one
representing the weakest possible response for the domain traits, v (e.g., all 1s), and one the
min
strongest, v (e.g., all 5s). These anchors are embedded into the same low-dimensional space as
max
the observed participants, yielding embedded anchor points ve and ve , respectively. Because
min max
UMAP embeddings typically organize observations along smooth latent gradients, projecting
participants onto the axis defined by the embedded anchors provides a simple and interpretable
summary of the dominant pattern distinguishing individuals within a domain. When this latent
gradient is approximately linear, linear projection preserves both relative ordering and distances
along the principal axis of variation. In this case, the domain score for participant i is computed
as the orthogonal projection of the participant’s embedding pᵢ onto the anchor axis: sᵢ = [(pᵢ −
ve ) ⋅ (ve − ve )] / ǁve − ve ǁ². This score represents the participant's relative position
min max min max min
along the axis spanning the theoretical response range.
9

However, when the gradient is substantially curved, for instance, due to saturation effects,
linear projection can distort distances or relative ordering along the manifold. To assess whether
linear projection is adequate, we evaluate rank consistency between anchor-based linear scores
and manifold-respecting positions using Spearman’s rank correlation coefficient (ρ) and
Kendall’s rank correlation coefficient (τ). These metrics quantify the degree to which linear
projection preserves relative ordering along the underlying manifold. Linear projection is
retained when ρ≥0.90 and τ≥0.85. When both statistics fall below these thresholds, indicating
concurrent global and local rank distortion, we compute participants’ scores using geodesic
distances (e.g., via Isomap) measured along the embedded manifold from ve to each
min
participant, normalized by the total manifold path length connecting ve and ve (Figure 2).
min max
Although geodesic scoring provides a manifold-respecting parametrization of domain
progression, it is not used by default: if the latent gradient is approximately linear, linear
anchor-based projection yields more stable and auditable scores. Geodesic scoring is therefore
applied only when diagnostics indicate that linear projection fails to preserve both global and
local rank structure.
Unlike sample-based scores derived from z-scoring, percentile ranking, or other
normalization schemes, where scores depend on a participant’s relative position within a given
sample, anchor-based projection retains absolute interpretive meaning by computing each score
relative to fixed conceptual anchor profiles rather than to other respondents in the dataset.
Sample-based scores are affected by the empirical distribution of the data, which can distort
interpretation and make respondents appear “low” or “high” simply because the sample is
skewed. In addition to making scores sample-independent, anchor-based projection offers a
10

preferable alternative to simple and weighted averages in domains where appropriate item
weights are unknown or direct aggregation of item values is not appropriate. By placing each
respondent along a predefined continuum between low-functioning and high-functioning anchor
profiles, this approach produces domain-level scores without requiring explicit weighting
assumptions or reliance on sample-dependent normalization.
3.2.2 Weighted Average Score
When anchor-based projection is not applicable, such as in domains composed of dichotomously
scored items (e.g., correct vs. incorrect) or domains with highly homogeneous items reflecting a
particularly narrow trait, a weighted average provides a suitable alternative. In these cases, the
construct is well defined in advance, item directionality is clear, and either the relative
importance of items is known or can be reasonably derived. In these cases, a weighted composite
score offers a stable and interpretable summary of each participant’s standing in the domain.
Below we describe two typical scenarios when weights can be derived.
If items function as indicators of a common latent construct (e.g., abstract vs. concrete
thinking), item weights may be derived from the dominant covariance pattern within the domain.
Indicators with stronger and more consistent contributions to shared variance receive higher
weights, while weaker indicators contribute proportionally less. This yields a weighted index that
retains the clarity of the composite score while incorporating information about the latent
structure implied by the data. Weighting indicators by their contribution to shared variance is
consistent with reflective measurement theory (e.g., Bollen, 1989; Fabrigar & Wegener, 2012;
Embretson & Reise, 2000), which defines constructs through systematic covariance among
indicators.
By contrast, in domains where responses indicate correctness rather than endorsement of
11

a psychological attribute, a difficulty-based weighting scheme can be applied, in which each
item’s weight is proportional to its empirical difficulty (based on the prevalence of correct
responses in the sample) after adjusting for chance performance (e.g., Lord, 1989; Embretson &
Reise, 2000). Harder items receive higher weights, whereas items answered correctly by nearly
all participants contribute less.
After computing item weights, we compute domain scores as difficulty- or
covariance-weighted proportions, with 0 corresponding to the lowest attainable (not necessarily
present in the sample) standing and 1 to the highest. The resulting scores–bounded by the
theoretical range of the corresponding trait rather than the range in the sample–places these
domains on the common scale with the anchor-based projections described above, ensuring
comparability across domains and compatibility with downstream analyses.
3.2.3 Simple (Normalized) Average Score
For domains that do not lend themselves to anchor projection or are composed of items for which
no principled basis exists for differential weighting, we summarize responses using simple
unweighted averages. This approach is appropriate when items share a common response scale,
ensuring comparability across indicators2. Under these conditions, equal weighting provides a
transparent summary of domain-level functioning without imposing additional assumptions
about item importance or latent structure.
3.3 Stage 2: Clustering
The second stage of the pipeline operates on the domain-level scores produced in Stage 1.
Because each domain is now represented by unidimensional scores and the number of domains is
2 For domains that don’t fall into any of the three categories we consider in this paper, alternative scoring mechanisms (such as anchor projection
in the original space) will need to be considered. None of the domains we identified in the datasets used for the current study required that.
12

generally small, the input to stage 2 is therefore low-dimensional. Nonetheless, domains are
intentionally constructed to be conceptually distinct and hence, when considered jointly, can
exhibit nonlinear structure, heterogeneous variance, or uneven resolution. To accommodate these
cross-domain characteristics, we apply UMAP to the domain-level scores to construct a
second-stage embedding prior to clustering.
To show that nonlinear embedding is called for at this stage, we benchmark clustering
performance across raw domain scores, PCA projections, and UMAP embeddings. UMAP
produces markedly stronger separation and more coherent geometry than either PCA or
raw-space representations, as reflected in higher silhouette values across benchmarked
configurations (Appendix B). We expect this finding to hold generally if survey items are
grouped into domains properly, i.e., to represent largely unrelated psychometric constructs.
Spectral clustering is then performed to identify latent groupings within the embedded
space3. The resulting clusters of the points in the embedded space correspond to distinct
psychometric profiles of the participants represented by those points. Both UMAP
transformation and spectral clustering will produce different clustering solutions depending on
hyperparameters used. We tune hyperparameters and evaluate resulting clustering solutions based
on internal validity and qualitative interpretability of the resulting profiles. Internal validity is
quantified using standard metrics--including the silhouette score, Calinski–Harabasz index, and
Davies–Bouldin index--computed in the embedded space, while qualitative interpretability is
assessed by the coherence and distinctiveness of domain score patterns across clusters. These
complementary considerations guide selection among candidate solutions in specific applications
3 We tested alternatives such as K-means, DBSCAN, and HDBSCAN, but these performed poorly in capturing the non-convex geometry of the
UMAP-transformed space (see Appendix B for comparisons).
13

of the framework.
We note that domains with few distinct score values (i.e., each value is shared by a
significant fraction of participants) can induce trivial clustering partitions, even when those
domains have high theoretical response resolution. Because UMAP prioritizes the strongest local
contrasts when constructing its neighborhood graph, these low-cardinality domains produce a
small number of discrete plateaus that dominate the remaining dimensions. Spectral clustering
then splits the data almost exclusively along these plateaus, yielding clusters that are technically
stable but largely uninformative: individuals with identical values on the low-cardinality domain
are grouped together even when they differ substantially on the broader psychometric constructs.
To avoid this collapse of the multivariate structure onto a single coarse dimension, we exclude
these domains from Stage 2 clustering and retain them only for interpretive analyses.
To aid interpretability, clusters are indexed according to their average cross-domain
behavioral standing. For each participant, we compute a scalar summary score defined as the
mean of their standardized scores across the five behavioral-financial domains. This
participant-level average provides a parsimonious measure of overall functioning that weights
each domain equally and remains independent of geometric properties of the low-dimensional
embedding. Cluster-level summaries are obtained by averaging these participant-level scores
scores across all members of each cluster and clusters are then ordered according to their mean
score, yielding an interpretable ordering along a continuous cross-domain gradient.
To aid interpretability, clusters are indexed according to their average cross-domain behavioral
standing rather than their position in the embedded space. For each participant, we compute a
scalar score defined as a weighted average of their domain scores, where weights reflect
empirically derived domain importance from post hoc analyses of cluster separation.
14

Cluster-level summaries are obtained by averaging these participant-level scores across all
members of each cluster. Clusters are then ordered according to their mean participant score,
yielding an interpretable ranking along a continuous cross-domain gradient from lower to higher
overall behavioral and financial functioning. This ordering is not intended to imply a normative
ranking; rather, it provides a stable indexing convention across pipeline runs with different seeds
and parameters. Nonetheless, the resulting numbering often follows a broad gradient--from more
vulnerable or struggling profiles to more adaptive or flourishing ones. Intermediate clusters,
however, do not fall cleanly along this continuum and instead reflect distinct, non-linear
configurations of behavioral and psychological traits.
4. Use Case 1: Development of Individualized Strategy for Financial Advice
This framework was developed to support professional practice settings in which individuals or
couples seek guidance around financial decision-making and money-related relationship
dynamics. In such contexts, practitioners often work with clients who struggle with
follow-through, self-regulation, emotional responses to money, or alignment between intentions
and behavior, particularly among couples. The framework is designed to reveal a client’s
behavioral and psychological profile and thus support structured conversations, targeted
coaching, and more tailored intervention strategies. This applied orientation motivates the use of
a broad psychometric assessment of financial functioning that is given to new clients as part of
onboarding. Responses to this assessment form a proprietary dataset which we describe next.
4.1 Dataset Description and Conceptual Coverage
The proprietary dataset consists of responses to a 122-item psychometric instrument, comprising
95 domain items that assess eight dimensions of financial functioning (Table 1) and 21 outcome
items used exclusively for external validation analyses (described in Section 4.7). The instrument
15

draws on established frameworks including Family Financial Socialization Theory (Gudmunson
& Danes, 2011), Self-Determination Theory (Di Domenico et al., 2022), and the Transtheoretical
Model of Change (Prochaska & DiClemente, 1983).
The instrument includes eight domains, each containing between 5 and 21 items, selected
to reflect multiple aspects of psychological functioning relevant to financial behavior, including
self-regulation, motivation, construal, emotional resources, and financial knowledge. Domains
corresponding to Financial Behavior (Prochaska & DiClemente, 1983), Financial Literacy
(Lusardi & Mitchell, 2011), and Motivation (Ryan & Deci, 2017) are well-established predictors
of financial well-being and provide familiar interpretability within behavioral finance. Attitudes
& Capabilities domain captures perceived control, emotional tendencies, and financial
self-concept–constructs strongly linked to planning and follow-through (Gudmunson & Danes,
2011) but often underrepresented in financial assessments. Psychological Capital (hope,
resilience, optimism, efficacy; Luthans, et al, 2007) and Character Strengths (e.g., perseverance,
self-regulation, gratitude) draw on well-validated frameworks (Peterson & Seligman, 2004) and
have been empirically linked to financial resilience, adaptive coping, and reduced financial stress
(Strömbäck et al., 2017; Xiao & O’Neill, 2016). Financial Construal Level, grounded in
Construal Level Theory (Trope & Liberman, 2010), assesses how individuals construe and
interpret financial choices, shaping risk perception, time horizons, and behavioral
follow-through. The breadth of the item pool allows broad behavioral–psychological profiles to
emerge during the unsupervised learning.
4.2 Participant Sample and Psychometric Properties
A total of 337 participants meet the predefined inclusion criteria and are included in the analytic
sample. Participants are required to complete at least 80% of each survey module to ensure
16

sufficient item-level data for reliable domain score computation. Item-level missing responses
within included surveys are handled using the imputation procedures described in Supplemental
Table C3. Domain-level score distributions are examined for extreme values (|z| > 3), and no
outliers are detected within the analytic sample. Participants are drawn from several U.S.-based
sources—including financial advisors and their clients, college students, and voluntary
users—resulting in a heterogeneous sample that spans a wide range of financial experiences,
decision-making contexts, and behavioral tendencies. Table 3 summarizes the socio-demographic
composition of the dataset.
Although modest in size, the dataset exhibits substantial response variability and strong
internal reliability in all psychometric domains (Cronbach’s α = .50–.94; Supplemental Table
S1). Responses vary widely across the full response range in each domain, with no evidence of
floor or ceiling effects. Inter-domain correlations ranged from .30 to .83 (median r = .56),
indicating related but non-redundant constructs. Prior methodological work in exploratory
psychometric settings suggests that when measurement quality is high, meaningful latent
structure can be recovered with modest sample sizes, even in non-probability samples (Kyriazos,
2018). Moreover, the sample composition reflects the kinds of mixed recruitment sources
commonly available in practical behavioral-finance applications, where segmentation models are
typically developed from convenience-based cohorts rather than nationally representative
surveys.
4.3 Producing Domain Scores
Across the psychometric domains examined in this dataset, diagnostic analysis indicates that
most domains exhibit sufficient response resolution and globally curved geometry (Table 2),
warranting the application of UMAP followed by anchor-based projection to derive
17

unidimensional domain scores. To obtain stable embeddings, UMAP hyperparameters are
selected via randomized search by jointly maximizing trustworthiness and continuity using a
weighted objective to prioritize trustworthiness (α = 0.6; see Appendix C for the resulting
hyperparameter values). The embedding quality is high across all domains, with trustworthiness
ranging from 0.936 to 0.958 and continuity ranging from 0.949 to 0.972. For all evaluated
domains, linear anchor-based scores and geodesic (Isomap-based) scores produced nearly
identical rank orderings, with Spearman correlations exceeding .99 and Kendall τ values above
.87. Anchor-based projection scoring is, therefore, used throughout.
Two domains require alternative scoring approaches. Financial Literacy is scored as a
difficulty-adjusted accuracy composite, reflecting the proportion of correct responses weighted
by item difficulty as described in Section 3.2.2. In the Financial Construal Level domain,
although items are binary, their response options differ substantially in the degree to which they
reflect abstract versus concrete construal. Treating all responses as uniformly equivalent (e.g.,
assigning 0/1 values) would therefore obscure meaningful differences in abstraction across items.
Instead, we use covariance-weighted aggregation, allowing responses to given items to contribute
proportionally based on their empirical alignment with overall construal patterns in the sample.
For example, items for which the “abstract” response tends to co-occur with abstract responses
on other items receive greater weight.
4.4 Clustering and Internal Validation
Using the domain-level scores described above, we construct a second-stage UMAP embedding
and apply spectral clustering to identify latent behavioral profiles of the participants. We tune the
hyperparameters of both UMAP and spectral clustering (Appendix C) to optimize separation in
the resulting low-dimensional manifold. Grouping the participants into seven clusters produces
18

results with discernible spatial separation and coherent structure: Silhouette Score of 0.569,
Calinski–Harabasz Index of 1,543.50, and Davies–Bouldin Index of 0.579. Moreover, the
clusters have reasonably uniform distribution as shown in Table 4.
To assess stability, we rerun the (UMAP → spectral clustering) pipeline using 100
independent random seeds while holding all hyperparameters fixed. Cluster consistency across
runs is high (mean ARI = 0.916, SD = 0.043). We further assess robustness of the clustering
stage to sampling variation: we generate a single UMAP embedding using the full dataset and
apply spectral clustering to 100 random 80% subsamples within this fixed embedded space.
Subsample solutions show very high stability relative to the full-sample reference (ARI = 0.970,
SD = 0.018).
4.5 Cluster Interpretability
In addition to the internal validity as described above, the clusters also possess coherent and
interpretable psychological structure (Figure 3a). These clusters can be understood as distinct
profiles within the broader financial mindset space defined in the Introduction. They are defined
not only by the overall level of functioning but by how distinct combinations of financial
behavior, perceived capability, motivation, psychological resources, and indicators of positive
functioning (defined by domain scores) combine to shape behavior. Although clusters are
broadly ordered along a dominant functioning gradient, interpretability arises from meaningful
deviations from this gradient, yielding distinct behavioral pathways rather than simple severity
tiers.
At lower levels of functioning, limited psychological resources and motivation constrain
the translation of financial knowledge into consistent behavior, whereas mid-range clusters
diverge in whether financial engagement is primarily cognitive (e.g., higher construal and literacy
19

without equivalent execution) or structural (e.g., stable routines and competence with modest
motivational drive). At higher levels of functioning, clusters further differentiate based on the
role of motivation relative to skills, distinguishing profiles characterized by steady,
competence-driven performance from those marked by heightened motivational activation and
behavioral intensity. These patterns indicate that clusters reflect qualitatively distinct
configurations of psychological and behavioral factors, rather than points along a single
continuum. Domain-level summaries for cluster profiles are reported in Table 5a.
4.6 Demographic Analysis
To evaluate whether the behavioral clusters are primarily attributable to socio-demographic
stratification, we model cluster membership as a function of age, education, and income using
multinomial logistic regression. These variables are widely used indicators of socioeconomic
status (SES) in behavioral and financial research. The overall model is statistically significant
(likelihood-ratio test, p < .001), indicating that demographic variables are associated with cluster
assignment. However, explanatory power is modest (McFadden pseudo-R² = .091), suggesting
that socio-demographic factors account for only a limited proportion of variance in cluster
membership. At the predictor level, income shows statistically significant associations with
membership in two clusters (ps = .002–.003), while its associations with other clusters are
non-significant (ps > .08). Age and education display isolated significant contrasts (ps ≈
.03–.05), but the majority of their coefficients are non-significant (ps ≥ .09), and no consistent
pattern emerges across clusters. Taken together, these findings indicate that although
demographic variables contribute some signal, they do not substantially account for the
clustering structure.
4.7 External Associations with Independent Outcomes
20

We have seen in Sections 4.4 and 4.6 that our clustering approach expresses meaningful internal
structure that cannot be revealed through purely demographic data. We now turn to another
important aspect in evaluating our framework, namely, whether the latent profiles it reveals
correspond to meaningful differences in overall functioning across psychological and behavioral
domains. To this end, we consider how cluster membership correlates with independent external
outcomes that were not utilized in cluster construction.
Specifically, we consider life satisfaction, psychological well-being, and perceived
financial health – conceptually related yet empirically distinct evaluative outcomes. Life
satisfaction reflects a global cognitive appraisal of one’s life circumstances, psychological
well-being captures eudaimonic functioning and internal psychological resources, and financial
health reflects perceived or objective financial capacity and security. Prior research consistently
shows that although these constructs are moderately correlated, none is reducible to the others,
and each retains substantial unique variance after controlling for socioeconomic status and
objective financial conditions (Mentus, 2017; Kokun et al., 2024; Halandová, 2024). Moreover,
psychological well-being is not merely an outcome of financial conditions but also a key
antecedent of financial behavior: low psychological resources, maladaptive beliefs, and
emotional distress reliably inhibit planning, follow-through, and adaptive financial
decision-making, contributing to poorer financial health over time (Thompson, 2021; Thompson,
2023). Life satisfaction is measured using the Satisfaction with Life Scale (Diener et al., 1985),
psychological well-being is assessed with the Flourishing Scale (Diener et al., 2010), and
perceived financial health is evaluated using a 10-item version of the Financial Health Network
Score (Financial Health Network, 2018).
Cluster membership is strongly associated with all three outcomes. One-way ANOVAs
21

indicate significant between-cluster differences for Life Satisfaction, F(6,330) = 12.98, p < .001
(ηp² = .19), Psychological Well-Being, F(6, 330) = 19.90, p < .001 (ηp² = .27), and Perceived
Financial Health, F(6, 330) = 84.73, p < .001 (ηp² = .61). Post-hoc Tukey tests reveal extensive
pairwise differences between clusters; after correction for multiple comparisons, approximately
52–90% of pairwise contrasts remain significant (adjusted p < .05). Full ANOVA tables are
reported in Supplemental Table S2.
To further assess reducibility, we compare regression models including (a) cluster
membership only, (b) socio-demographic variables only, and (c) both predictors jointly. Across
outcomes, cluster membership accounts for substantially more variance than socio-demographic
variables alone (R² = .19–.61 vs. .09–.16). In combined models, clusters contribute large
additional explanatory power beyond SES (ΔR² = .14–.45; Figure 5), whereas SES adds
comparatively little unique variance once cluster membership is included.
The observed associations between cluster membership and the external outcomes
provide evidence that the learned profiles capture underlying behavioral–psychological
organization that generalizes across distinct but interconnected domains of functioning, rather
than reflecting redundancy among outcome measures.
4.8 Assigning New Individuals to Learned Profiles
In the applied settings that motivated the development of this framework--such as financial
advising, behavioral coaching, and clinical contexts--new individuals must be assigned to
previously constructed behavioral profiles. It is obviously infeasible to re-cluster from scratch
every time a new respondent is added to the population. Accordingly, we evaluate whether the
new respondents can be assigned to existing clusters using a supervised classification approach.
To this end, we train a supervised ensemble soft-voting classifier (see Supplemental Table C4),
22

composed of a Support Vector Machine (SVM) and a Random Forest, with cluster indices as
target labels, and evaluate its performance using 5-fold stratified cross-validation. The ensemble
achieves an accuracy of 79.2%, which substantially exceeds chance-level performance given the
number of clusters.
4.9 Anecdotal Success Evidence of Tailored Interventions
In addition to quantitative validation, we collect qualitative feedback from a small number of
pilot advisors who used the behavioral profiles revealed by the proposed pipeline in live client
engagements. Advisors describe using the profiles to anticipate client behavioral tendencies and
inform advisor-mediated interventions, particularly in time-constrained or emotionally salient
contexts.
Across examples, advisors report that the profiles are perceived as useful for anticipating
patterns of financial avoidance under high salience, asymmetric pacing needs within couples,
sensitivity to pressure or authority, and reluctance to request assistance. These anticipated
tendencies inform decisions about communication framing, pacing and staging of
recommendations, meeting structure, and the timing of information delivery (e.g., asynchronous
plan review prior to discussion). Advisors further note that the profiles support interpretation of
client behavior when unexpected disclosures or actions occurred, reducing surprise and enabling
calibrated responses.
5. Use Case 2: Behavioral Segmentation At Scale
Here we evaluate whether the same two-stage framework identifies meaningful behavioral
patterns in a large, independent, population-based dataset with different measurement properties.
We apply the framework to the 2017 U.S. CFPB National Financial Well-Being Survey, a
nationally representative dataset designed to assess financial well-being, financial behaviors, and
23

perceived financial capability among U.S. adults. Specifically, we apply the proposed framework
to segment the dataset population into meaningful clusters reflecting distinct behavioral profiles.
5.1 Dataset Description and Construct Mapping
Although the CFPB survey contains a broad set of variables spanning demographics, family
context, financial behaviors, and structural conditions, our analysis focuses on a targeted subset
of items reflecting psychometric, attitudinal, relational, or cognitive constructs relevant to
financial decision-making. Variables capturing situational constraints, access-related factors, or
external resources are excluded because they do not represent psychological attributes and are
therefore not suitable inputs for trait-based behavioral profiling (see Appendix A for item
details).
We group the selected items into five domains--Capabilities, Financial Literacy, Planning,
Budgeting & Saving, and Social & Relational Support (as shown in Appendix A)--which serve
as functional analogues to broader conceptual categories represented in the proprietary dataset.
5.2 Characteristics and Measurement Properties of the Sample
After excluding incomplete cases (n = 497; <8% of respondents), the final analytic sample
consists of 5,897 individuals. Incomplete cases were defined as respondents with missing data on
one or more items required for domain construction and clustering. The large sample size and
broad demographic coverage provide a stringent test of the framework utility under reduced
construct resolution and heterogeneous item scales. Although the CFPB survey was not designed
as a unified psychometric battery, the selected domains exhibit sufficient variability and internal
coherence to support nonlinear embedding and clustering (Cronbach’s α = .78–.87; Supplemental
Table S1). The Financial Literacy domain contains items that have binary response values
corresponding to correct or incorrect answers. The remaining domains capture perceived
24

capability, planning tendencies, routine financial management, and social support.
5.3 Producing Domain Scores
Domain-level scores are derived using the same general principles described in Section 3, with
adaptations reflecting the CFPB instrument’s structure. Financial Literacy is scored as a
difficulty-adjusted accuracy composite in the exact same way as the corresponding proprietary
domain. The Social & Relational Support domain, which consists of seven binary items, is
scored using a simple average4. For the remaining psychometric domains, diagnostic analyses
indicate the need for nonlinear embedding, yet linear anchor-based projection in the resulting
embedded space is sufficient. Across these domains, UMAP embeddings achieve high
trustworthiness (0.944–0.983) and continuity (0.979–0.993); selected hyperparameter values are
listed in Supplemental Table S1.
5.4 Clustering and Internal Validation
Following the framework methodology, we tune hyperparameters for the second-stage UMAP
and spectral clustering via randomized search, optimizing the same metrics used for the
proprietary dataset (Supplemental Table S1). As expected, the Social & Relational Support
domain is not suitable for clustering, as it has only eight unique score values across all
participants; this domain is therefore excluded from the clustering step and retained solely for
post hoc interpretation. More unexpectedly, the inclusion of the Financial Literacy domain
consistently collapses the learned manifold, resulting in poor cluster separation and reduced
interpretability. Careful inspection of the resulting score distribution reveals that, despite its high
nominal response resolution, empirically, Financial Literacy concentrates respondents on a
4 The items in this domain appear to be positively correlated in a fairly uniform way, so the covariance weights end up close to
equal weighting. When that happens, the covariance-weighted score collapses to something very close to the simple average.
25

limited set of score values, with the four most frequent values alone comprising approximately
30% of the sample (Figure 4). These spikes impose a strong ordering structure that
disproportionately shapes the embedding geometry and obscures multidimensional behavioral
variation contributed by other domains. Accordingly, Financial Literacy is also excluded from
clustering and examined only post hoc for profile interpretation.
After removing these two domains, we perform the clustering procedure to group the
participants into seven clusters (Figure 1c). Internal validation metrics indicate meaningful
clustering structure, with a Silhouette Score of 0.500, a Calinski–Harabasz Index of 10,639.98,
and a Davies–Bouldin Index of 0.622. Although cluster separation is less pronounced than in the
proprietary dataset, these values are consistent with coherent profile differentiation given the
larger population base and reduced construct resolution.
As in the case of the proprietary dataset, we assess the seed stability by reruning the
clustering pipeline across 100 independent random seeds and subsample stability by clustering
100 random 80% subsamples within a fixed second-stage embedding. Both metrics indicate that
the recovered structure is not driven by stochastic variation or sampling idiosyncrasies: the seed
stability is high, with mean ARI = 0.814 (SD = 0.086) and subsample stability is very high, with
mean ARI = 0.994 (SD = 0.003)
5.5 Cluster Interpretability
The CFPB clusters exhibit coherent and interpretable structure, reflecting distinct configurations
of financial capability, planning, budgeting and saving behavior, social and relational functioning,
and financial literacy (Figure 3b). Although cluster means generally increase along an overall
gradient of financial functioning, the profiles are not reducible to a single severity dimension.
Instead, clusters are distinguished by how knowledge, planning capacity, and enacted financial
26

behaviors align—or fail to align—within individuals.
Lower-functioning clusters are characterized by comparatively weaker budgeting and
saving behavior and planning capacity, even when financial literacy is moderate, suggesting
barriers in translating knowledge into sustained financial routines. Intermediate clusters diverge
in the balance between structural behaviors and cognitive resources: some profiles emphasize
strong budgeting and saving practices with only moderate planning or capability, whereas others
show elevated planning and literacy without commensurate behavioral execution. At higher
levels of functioning, clusters differentiate based on the relative emphasis placed on planning
intensity, behavioral consistency, and social–relational support, distinguishing profiles marked by
comprehensive, integrated financial engagement from those with more selectively developed
strengths (Table 5b).
5.6 Demographic Analysis
Given the central role of socio-demographic variables in population-based financial surveys, we
examine whether cluster membership in the CFPB sample is primarily explained by
socio-demographic factors. We estimate a multinomial logistic regression predicting cluster
membership from age, education, and income. The overall model is statistically significant
(likelihood-ratio test, p < .001), and age, education, and income are each statistically significant
predictors across multinomial contrasts (all ps < .001). However, explanatory power is modest
(McFadden pseudo-R² = .061), indicating that socio-demographic variables account for only a
limited proportion of variance in cluster assignment. These results mirror the proprietary dataset
findings and indicate that the CFPB clusters are not reducible to demographic stratification, but
instead capture behavioral and psychological variation beyond standard SES indicators.
5.7 External Associations With Independent Outcomes
27

We consider three outcome domains not included in the clustering process: Life Satisfaction and
Perceived Financial Health, which parallel the evaluative outcomes examined in the proprietary
dataset, and Material Hardship capturing acute financial strain. Cluster membership is
significantly associated with all three outcomes. One-way ANOVAs indicate between-cluster
differences for Life Satisfaction (ηp² = .14), Material Hardship (ηp² = .23), and Perceived
Financial Health (ηp² = .44), closely paralleling the pattern observed in the proprietary data (see
Supplemental Table S2). Post-hoc Tukey tests indicate that these effects reflect systematic
differences across multiple clusters rather than being driven by a single extreme group.
Further, as shown in Figure 5, cluster membership explains substantial variance in Life
Satisfaction (R² = .14) and Perceived Financial Health (R² = .44), exceeding the variance
explained by demographics alone (R² = .04 and .25, respectively), and contributes meaningful
unique variance in the full models (ΔR² = .12 for Life Satisfaction; ΔR² = .25 for Perceived
Financial Health). As expected, socio-demographic variables account for a larger share of
variance in Material Hardship (R² = .27); nevertheless, cluster membership explains additional
unique variance (ΔR² = .09), indicating that behavioral–psychological profiles provide
explanatory power even for outcomes reflecting concrete economic strain.
6. Structural Alignment of Cluster Profiles Across Datasets
We have seen that the proposed framework can be applied to two datasets of very different
nature, producing meaningful interpretable clusters in each case. We next explore whether
profiles derived from the proprietary and CFPB samples exhibit functional similarities. The
challenge arises because the instruments in both datasets are not the same: they contain different
questions, with markedly different measurement properties. Still, both instruments assess several
core constructs related to financial behavior, literacy, psychological resources, positive
28

functioning, and planning or organizational processes. Thus, we harmonize the two datasets into
a common five-domain conceptual space: Financial Behavior, Financial Literacy, Psychological
Resources, Positive Functioning, and Motivation & Planning. Financial Construal Level domain
is excluded from the proprietary side because the CFPB dataset lacks an equivalent domain. See
Appendix D for details on constructing the harmonized space.
This unified space allows direct comparison of profiles derived from both datasets, with
alignment quantified using several complementary metrics described in Appendix D2. Cluster
centroids are closely aligned along a dominant global functioning axis defined primarily by
Financial Behavior, Psychological Resources, and Motivation & Planning (PC1 loadings = .524,
.505, and .507, respectively), with weaker contributions from Financial Literacy and Positive
Functioning (loadings = .250 and .389). Cluster ordering along this axis is perfectly preserved
across datasets (Spearman ρ = 1.00), indicating preserved rank structure despite differences in
domain coverage. Geometric alignment of cluster profiles is moderate to strong (Procrustes
disparity = .158; mean CPSI = .739), with the greatest correspondence observed at higher levels
of functioning and increased compression in CFPB profiles relative to the proprietary dataset at
the lower end of the distribution. Figure 6 illustrates that, when clusters are ordered along the
global functioning axis, proprietary and CFPB centroids exhibit similar absolute functioning
levels, consistent with strong ordinal correspondence and relatively low Procrustes disparity.
These results indicate that the framework captures a shared latent structure that extends
beyond sample-specific clustering solutions. While the present analysis is limited to two datasets,
the observed structural alignment suggests that sufficiently rich behavioral surveys may reveal
profiles reflecting inherent properties of financial behavior. Further experimentation with
additional datasets–across different instruments and populations–is required to confirm this
29

conjecture.
7. Discussion
This study presents a novel behavioral segmentation framework that leverages unsupervised
learning to uncover latent behavioral structure. The primary contribution of this work is
methodological: the framework that introduces a staged approach to behavioral profiling, which
separates within-domain representation from cross-domain integration, enabling psychologically
interpretable segmentation across diverse psychometric instruments. Rather than assuming a
predefined structure or rigid scoring strategy, this approach accommodates domains with varying
measurement properties, including both approximately linear and nonlinear relationships among
items.
We provide evidence of wide applicability of the proposed framework by using it to
uncover latent profiles in two independent datasets of very different nature. The emergent
profiles in both cases demonstrate robust internal structure and meaningful differentiation with
respect to external outcomes–most strongly for financial health and psychological well-being,
and to a lesser degree for life satisfaction. This pattern aligns with prior work showing that
proximal outcomes such as financial health are more tightly linked to daily behaviors and
psychological capacities, whereas life satisfaction reflects broader and more diffuse life
evaluations (Diener et al., 1999; Netemeyer et al., 2018). Systematic differences on these broader
outcome measures suggest that the learned profiles reflect underlying psychological organization
rather than merely differences in observable financial behaviors.
In addition to quantitative validation above, the framework is being evaluated in live
advisory contexts, where preliminary practitioner feedback indicates that the resulting profiles
predict behaviorally relevant tendencies that inform practitioners’ decision-making in tailoring
30

advisor–client interactions.
7.1 Methodological Advances
This work advances behavioral segmentation methodology in four key ways. First, rather than
clustering item-level responses directly, the framework adopts a two-stage representation strategy
that separates the inference of the within-domain structure from cross-domain integration. This
design preserves domain-specific psychological distinctions while preventing domains with
greater item counts from disproportionately influencing the clustering solution.
Second, the framework formalizes domain-level representations as continuous scores that
place individuals along a meaningful psychological axis within the domain. Specifically, we
introduce an anchor-based projection strategy that can be applied in either the original item space
or after dimensionality reduction, mapping responses onto interpretable continua defined by fixed
conceptual reference profiles.
Third, the framework is intentionally modular and algorithm-agnostic. Although UMAP
and spectral clustering provide strong empirical performance in the present study, the
architecture does not depend on a specific embedding or clustering method, enabling
applicability across instruments, populations, and survey formats.
Finally, by applying the same framework to datasets with markedly different
psychometric depth, this work demonstrates how measurement richness influences the
granularity of recovered behavioral profiles without requiring fundamentally different modeling
strategies.
Together, these advances provide a flexible and interpretable approach to
behavioral-finance segmentation that extends beyond existing linear or single-pass clustering
methods. Domain construction, scoring methods, and inclusion in clustering are specified
31

conceptually a-priori, and then evaluated empirically using the diagnostics described in this
paper, leading to potential revision cycles. This enables the framework to adapt flexibly across
instruments and datasets while preserving interpretability and methodological coherence.
7.2 Practical Applications
The clustering framework developed in this study lends itself to a wide range of applications
across clinical, advisory, and digital financial contexts.
In clinical psychology and financial therapy, behavioral profiles may support more
targeted intervention planning than traditional demographic or symptom-based approaches by
aligning treatment strategies with clients’ emotional, cognitive, and motivational readiness for
financial change (Archuleta et al., 2012). For example, profiles characterized by strong capability
and stable behavioral routines (e.g., Cluster 3) may benefit less from motivational enhancement
strategies and more from structured goal-setting, cognitive restructuring around long-term
planning, and values clarification interventions. In such cases, therapeutic work may focus on
optimizing existing strengths rather than increasing behavioral activation. In contrast, individuals
in Cluster 0, who exhibit lower psychological resources or signs of emotional depletion, may
benefit from approaches that prioritize therapeutic alliance, emotion-focused techniques, or
motivational interviewing (MI) to strengthen autonomy, hope, and readiness for change before
introducing structured financial planning tasks. In this way, the profiles may assist practitioners
in determining whether cognitive-behavioral techniques, motivational enhancement, or
supportive-expressive approaches are most appropriate, thereby facilitating more precise
treatment matching within established clinical frameworks.
In financial advising, the profiles support personalization of communication style,
planning horizons, and behavioral scaffolds based on clients’ cognitive and motivational
32

tendencies. For instance, clients with strong analytical capacity but weak follow-through may
benefit from structured action plans and accountability mechanisms, whereas those with lower
confidence or elevated anxiety may respond better to incremental goal-setting and simplified
messaging.
In consumer-facing fintech platforms, behavioral profiles can drive adaptive
personalization features such as goal tracking, contextual nudges, and mindset-specific content
(Thaler & Sunstein, 2008). Integration with LLM-powered agents further enables real-time
adjustment of conversational tone and support strategies based on users’ behavioral tendencies.
This approach is currently being operationalized within the Calibrate platform, where a
reduced-item classifier enables scalable psychometric segmentation to support adaptive
onboarding, behavioral coaching, and digital financial planning.
At a population level, behavioral segmentation can inform public financial-wellness
initiatives and workplace financial education programs, enabling stratified content delivery, early
risk identification, and targeted outreach to underserved or vulnerable groups.
7.3 Limitations and Future Work
This study has several limitations that primarily reflect data availability and the scope of
empirical evaluation rather than the proposed methodology itself.
First, both datasets are cross-sectional, which precludes assessing how individuals’
behavioral profiles evolve over time. It is important to distinguish this limitation from
methodological stability: while the clustering solutions are reproducible across random
initializations and analytic settings, the present data do not permit evaluating whether individuals
transition between profiles in response to interventions, life events, or changing financial
circumstances. Longitudinal data would be required to study such dynamics and to examine how
33

the framework responds to temporal change.
Second, all measures are based on self-report. Self-reported data may be influenced by
response styles, social desirability, or differential self-awareness, which can introduce
measurement noise and affect the geometry of the learned representations. Incorporating
behavioral, transactional, or passively collected data in future work would strengthen ecological
validity and improve the precision with which behavioral structure is inferred.
Third, the proprietary dataset is modest in size and drawn from a heterogeneous
convenience sample that skews younger than the broader U.S. population. While this reflects a
limitation in terms of population representativeness, it also mirrors the data constraints
commonly encountered in applied and advisory settings, where large probabilistic samples are
rarely available. Demonstrating that the framework yields coherent and interpretable structure in
such a small-sample context is therefore a practical feature of the approach. Nonetheless,
additional applications across diverse populations, institutional settings, and sample sizes would
help further characterize the robustness and boundary conditions of the method.
Fourth, as with most unsupervised learning frameworks, the proposed approach involves
analytic design choices--such as domain construction, embedding parameters, and clustering
resolution--that can influence the resulting structure. Rather than emphasizing uniqueness of any
single solution, we focus on reproducibility across reasonable specifications. Future work could
further formalize guidelines for parameter selection and sensitivity analysis to support broader
applied use.
Finally, although the present study focuses on financial behavior, the analytic framework
itself is domain-agnostic. Applying the approach to other areas--such as mental health, education,
or wellness--would help assess the extent to which similar forms of latent
34

behavioral-psychological structure emerge across different substantive domains and
data-generating contexts.
8. Conclusion
This paper introduces a two-stage unsupervised learning framework for identifying
psychologically interpretable patterns of financial behavior. Applied to both a proprietary
psychometric instrument and the public CFPB dataset, the approach yields coherent and
externally meaningful clustering structure, demonstrating its utility for uncovering latent
behavioral organization in financial data. Although additional validation across more diverse
populations will further clarify its generalizability, the present results show that integrating
behavioral science with manifold learning can support theoretically informed and practically
useful segmentation of financial mindsets.
We validate the framework through internal measures of psychometric coherence and
external associations with independent well-being outcomes, indicating that the recovered
structure reflects psychologically relevant variation rather than statistical artifacts. The resulting
clusters extend traditional financial personas by incorporating emotional, cognitive, and
motivational dimensions, yielding segments that are interpretable and informative in applied
settings.
Together, these contributions support a growing movement toward behaviorally
intelligent personalization in financial services. The proposed framework offers a scalable and
replicable foundation for modeling the human dimensions of financial decision-making in a
manner that is data-driven, flexible, and person-centered.
Acknowledgements
We are grateful to Dr. Joseph Beyer of Microsoft and Dr. Megan McCoy of Kansas State
35

University for their early guidance and encouragement in the development of the assessment that
produced our proprietary dataset. We also thank Dr. McCoy and Dr. Jack Bowler of the
University of Utah for their careful reading of the manuscript and valuable feedback.
36

Figure 1. Behavioral-financial clusters derived from unsupervised learning. (a) Schematic of the two-stage
unsupervised learning framework. (b) Two-dimensional UMAP projection of the proprietary dataset colored by
Spectral Clustering assignments. (c) Two-dimensional UMAP projection of the public CFPB dataset. In both
projections, anchor references (black and green dots) are included to aid spatial interpretability of the embedded
profiles. The anchors are generated by setting all domain scores to their observed minimum or maximum values
across all participants and subsequently embedded into the final space. Cluster structure exhibits clear separation in
reduced-dimensional psychometric space, with curvature reflecting dataset-specific nonlinear organization.
37

Figure 2. Anchor-based linear versus geodesic scoring on low- and high-curvature manifolds.
Panel A illustrates a domain embedding with low curvature, where participant embeddings (gray points) are
organized along an approximately linear latent gradient between the embedded minimum (ve , black) and
min
maximum (ve , green) anchors. For a representative participant (circled), the orthogonal projection onto the
max
anchor-defined axis yields a scalar score corresponding to the participant’s progress along the domain continuum.
The blue dashed segment along the anchor axis indicates the resulting linear score.
Panel B illustrates a domain embedding with substantial curvature. Although a straight-line anchor axis can still be
defined, linear projection no longer faithfully represents progression along the latent gradient. Instead, the
participant’s score is defined by the length of the manifold path from ve to the participant along the embedded
min
manifold (blue dashed path), normalized by the total path length between ve (black) and ve (green).
min max
In both cases, the score reflects progression along the anchor-defined domain continuum rather than overall
Euclidean proximity to the anchors.
38

Figure 3. Heatmaps of mean domain scores by cluster across eight psychological and behavioral domains for the
proprietary dataset (a) and five domains for the CFPB dataset (b), revealing distinctive cluster-level profiles.
Figure 4. The spike chart of score value occurrences for the CFPB domains. The Social and Relational domain
shows spikes corresponding to the eight possible score values. The Financial Literacy domain shows a small number
of spikes dominating the score distribution. The rest of the domains show wider distribution of scores across
participants, with less prominent spikes.
39

Figure 5. Variance explained by cluster membership and socio-economic status for subjective and financial
outcomes in the proprietary (top) and CFPB (bottom) datasets.
Bar charts show the proportion of variance explained (R²) in Life Satisfaction, Psychological Well-Being, Financial
Health, and Financial Strain for three models: (1) Clusters only; (2) Demographics only (age, education, income);
and (3) Clusters + Demographics. In both datasets, cluster membership accounts for substantial variance in Life
Satisfaction and Financial Health, exceeding that explained by demographics alone. For Material Hardship--a
construct more tightly linked to resource constraints--demographics contribute more variance, yet clusters still
explain sizable unique variance beyond demographics. The combined models indicate that behavioral–psychological
profiles captured by the clustering framework provide explanatory power that is not reducible to demographic
factors.
40

Figure 6: Global functioning gradient across clusters. Clusters from the proprietary and CFPB datasets are ordered
by their position along the global functioning axis (PC1), derived from principal component analysis of pooled
cluster centroids expressed in the unified five-domain space. Lines connect order-preserving paired clusters to
illustrate similarity in absolute functioning levels across datasets.
Table 1
Summary of the eight psychometric domains used in the clustering analysis, including theoretical foundations, item
counts, and response formats. Full descriptive statistics and reliability estimates are reported in Supplemental Table
S1; sample items are provided in Appendix A.
Domain Description Format Item Count Core Constructs
Character Adapted from the VIA Classification 5-point Likert 21 Self-regulation,
Strengths of Character Strengths (Peterson & perseverance, ethical
values
Seligman, 2004) to reflect financial
decision-making contexts
Attitudes & Perceived behavioral control and 5-point Likert 17 Financial self-efficacy,
Capabilities financial self-efficacy; aligns with perceived control
Family Financial Socialization
Theory (Gudmunson & Danes,
2011)
Psychological Positive psychological resources for 5-point Likert 8 Hope, resilience,
Capital coping and adaptive financial optimism, self-efficacy
behavior, drawn from the PsyCap
framework (Luthans et al., 2007)
Motivation Internal and external motivational 5-point Likert 14 Goal orientation,
drivers of financial behavior; based long-term motivation
on Self-Determination Theory (Ryan
& Deci, 2017)
Financial Everyday financial management 5-point Likert 11 Behavioral
Behavior behaviors; consistent with consistency, habit
stages-of-change perspectives strength
(Prochaska & DiClemente, 1983)
41

Positive  Psychological well-being and  5-point Likert  9  Subjective well-being,
Functioning  emotional balance relevant to  emotional regulation
financial decision-making
(Seligman, 2011)
Financial  Tendency to interpret financial  Forced choice  10  Construal-level
Construal  situations at more concrete vs. more  (2-option)  processing, abstraction
| Level  | abstract levels of meaning (Trope &  |     |     |     | orientation  |     |
| ------ | ------------------------------------ | --- | --- | --- | ------------ | --- |
Liberman, 2010).
Financial  Objective financial knowledge  Multiple choice  5  Decision accuracy,
| Literacy  | assessed using validated items  |     |     |     | factual financial  |     |
| --------- | ------------------------------- | --- | --- | --- | ------------------ | --- |
(Lusardi & Mitchell, 2011)
knowledge
Note: All domain items are derived from validated psychometric frameworks (e.g., VIA Character Strengths, PsyCap,
Self-Determination Theory, Construal Level Theory) and are adapted where appropriate to reflect financial decision-making
contexts. The final 95 items represent the empirically selected subset of a broader 224-item domain pool, retained based on
distributional quality, non-redundancy, and their contribution to stable structure in preliminary UMAP manifold assessments.

Table 2
Summary of Domain Structures, Dimensional Properties, and Scoring Methods for the Proprietary and CFPB
Datasets
Spearman ρ
Domain        #  PC1 Variance  Domain  Nonlinearity  Scoring Method
|                      | Items  Explained  | Resolution  | Indicator*  | /Kendal τ  |     |     |
| -------------------- | ----------------- | ----------- | ----------- | ---------- | --- | --- |
| Proprietary Dataset  |                   |             |             |            |     |     |
Character  21  .434  4.77×1014  .614  .997/.952  UMAP + Anchor
Strengths
Attitudes &  17  .407  7.63×1011  .588  .994/.932  UMAP + Anchor
Capabilities
Psych. Capital  8  .537  3.91×105  .597  .994/.932  UMAP + Anchor
6.10×109
| Motivation  | 14  .465  |     | .541  | .995/.941  | UMAP + Anchor  |     |
| ----------- | --------- | --- | ----- | ---------- | -------------- | --- |
Financial  11  .430  4.88×107.   .573   .996/.951  UMAP + Anchor
Behavior
1.95×106
| Positive  | 9  .517  |     | .574  | .989/.916  | UMAP + Anchor  |     |
| --------- | -------- | --- | ----- | ---------- | -------------- | --- |
Functioning
| Construal Level  | 10  .181  | 1,024  | .381  |     | Weighted average     |           |
| ---------------- | --------- | ------ | ----- | --- | -------------------- | --------- |
| Financial        | 5  -      | 32     | -     |     | Difficulty-weighted  |           |
| Literacy         |           |        |       |     |                      | average,  |
interpretation only
| CFPB Dataset  |     |     |     |     |     |     |
| ------------- | --- | --- | --- | --- | --- | --- |
7.24×108
| Capability  | 13  .424  |     | .400  | .999/.978  | UMAP + Anchor  |     |
| ----------- | --------- | --- | ----- | ---------- | -------------- | --- |
Budgeting &  9  .346  1.35×106  .377  .979/.879  UMAP + Anchor
Saving
| Planning   | 9  .362   | 7.76×105  | .399  | .994/.933  | UMAP + Anchor        |     |
| ---------- | --------- | --------- | ----- | ---------- | -------------------- | --- |
| Financial  | 12  .123  | 4,096     | .319  |            | Difficulty-weighted  |     |
42

Literacy  average
| Social &    | 7  -  | 128  | -   |   Simple average,    |
| ----------- | ----- | ---- | --- | -------------------- |
| Relational  |       |      |     | interpretation only  |

Note: * Nonlinearity Indicator is defined as the mean absolute cosine similarity between the global PC1 direction
and the local 1-D PCA tangent estimated from each point’s 20 nearest neighbors. Lower values indicate greater
deviation from global linearity and stronger support for a nonlinear embedding. Even when values suggest
approximate linear structure, incomplete local tangent alignment motivates the use of manifold embedding to
preserve curved latent organization.
Domains with very limited response resolution, which yield only a small number of unique response patterns after
deduplication, are excluded from PCA- and manifold-based linearity diagnostics because such metrics are not
meaningful for discrete, low-variability constructs.
Outcome domains (Life Satisfaction, Psychological Well-Being, Material Hardship, and Financial Health) are not
included in these diagnostics because they are used solely as external validation measures rather than as inputs to the
embedding or clustering procedures.

Table 3
Demographic characteristics of proprietary set participants
| Variable  | Category  | N    | %      |     |
| --------- | --------- | ---- | ------ | --- |
|           | Female    | 170  | 50.4%  |     |
Gender
|     | Male  | 147  | 43.7%  |     |
| --- | ----- | ---- | ------ | --- |

|     | Non-binary/undisclosed  | 20  | 5.9%  |     |
| --- | ----------------------- | --- | ----- | --- |

| Age Group  | 18–24                            | 86   | 25.5%  |     |
| ---------- | -------------------------------- | ---- | ------ | --- |
|            | 25–34                            | 41   | 12.2%  |     |
|            | 35–44                            | 85   | 25.2%  |     |
|            | 45–54                            | 45   | 13.4%  |     |
|            | 55–64                            | 48   | 13.9%  |     |
|            | 65+                              | 18   | 5.3%   |     |
|            | Not reported/undisclosed         | 15   | 4.5%   |     |
| Income     | Less than $50,000                | 77   | 22.9%  |     |
|            | $50,000 – $100,000               | 50   | 14.8%  |     |
|            | $100,000 – $200,000              | 74   | 22.0%  |     |
|            | $200,000 – $500,000              | 69   | 20.5%  |     |
|            | $500,000 or more                 | 42   | 12.5%  |     |
|            | Not reported                     | 25   | 7.4%   |     |
| Education  | Graduate or professional degree  | 115  | 34.1%  |     |
|            | Bachelor’s degree                | 115  | 34.1%  |     |
43

|                 | High school or equivalent        |     | 24   | 7.1%   |     |
| --------------- | -------------------------------- | --- | ---- | ------ | --- |
|                 | Some college / Associate degree  |     | 39   | 11.6%  |     |
|                 | Not reported/Undisclosed         |     | 44   | 13.1%  |     |
| Race/Ethnicity  | White                            |     | 202  | 59.9%  |     |
|                 | Black or African American        |     | 51   | 15.1%  |     |
|                 | Asian                            |     | 42   | 12.5%  |     |
|                 | Hispanic or Latino               |     | 19   | 5.6%   |     |
|                 | Other                            |     | 19   | 5.6%   |     |
|                 | Not reported                     |     | 6    | 1.8%   |     |
Note: Participants could select multiple ethnicity categories; percentages sum to more than 100%.

Table 4
Cluster distribution
Both datasets exhibited similar cluster dispersion: cluster sizes ranged from 7%–21% in the proprietary sample and
8%–22% in the CFPB sample.
| Proprietary Dataset  |                 |     | CFPB dataset  |        |              |
| -------------------- | --------------- | --- | ------------- | ------ | ------------ |
| Cluster              | n  % of Sample  |     | Cluster       | n      | % of Sample  |
| 0                    | 26  7.72%       |     | 0             | 1,301  | 22.06%       |
21.07%  12.63%
| 1      | 71          |     | 1      |   745  |        |
| ------ | ----------- | --- | ------ | ------ | ------ |
| 2      | 47  13.95%  |     | 2      | 1,294  | 21.95  |
| 3      | 65  19.29%  |     | 3      | 980    | 16.62  |
| 4      | 62  18.40%  |     | 4      | 461    | 7.82   |
| 5      | 25  7.42%   |     | 5      | 629    | 10.67  |
| 6      | 41  12.17%  |     | 6      | 487    | 8.26   |
| Total  | 337  100    |     | Total  | 5,897  | 100    |

Table 5a
Descriptive Cluster Profiles in the proprietary Dataset
Cluster-level summary descriptions derived from domain score patterns (Character Strengths, Attitudes &
Capabilities, Psychological Capital, Motivation, Financial Behavior, Positive Functioning, Financial Construal
Level, and Financial Literacy). Labels are descriptive and reflect relative strengths across domains.
| Cluster  Label   |     | Interpretive Summary  |     |     |     |
| ---------------- | --- | --------------------- | --- | --- | --- |
44

0 Low capability, low psychological Globally low strengths, capability, psychological capital,
resources motivation, and behavior. Adequate literacy does not translate
into action because confidence and functioning are limited.
1 Emerging capability with inconsistent Improving capability, literacy, and functioning, but motivation
habits and routines are not yet stable. Behavior is inconsistent despite
modest psychological resources.
2 Cognitively engaged, moderately Moderate strengths, capability, and behavior, with relatively
supported higher literacy and financial construal. Thinks about finances and
plans ahead, but only mid-level energy and execution.
3 Capable and stable Strong capability, literacy, functioning, and behavior, paired with
moderate motivation. Operates effectively through competence
and routine rather than pronounced motivational drive.
4 Highly capable, steady performer High capability, psychological capital, functioning, and literacy,
with solid behavior but only moderate motivational drive.
Performs reliably through skills and structure rather than strong
emotional push.
5 Organized and well-resourced High strengths, capability, motivation, and behavior, with very
strong literacy and functioning.
6 Highly resourced and consistently Exceptionally strong across all psychological, motivational, and
effective behavioral domains. Demonstrates very high internal resources,
strong motivation, excellent functioning, and reliable execution.
Table 5b
Descriptive Cluster Profiles in the CFPB Dataset
Cluster-level summary descriptions derived from domain score patterns (Capability, Budgeting & Saving, Planning,
Social & Relational Support, and Financial Literacy). Labels are descriptive and reflect relative strengths across
domains.
Cluster Label Interpretive Summary
0 Low structure, low follow-through Has difficulty getting started; weak systems, low motivation, and
limited follow-through. Confidence is modest, making financial
tasks feel effortful or overwhelming.
1 Growing structure, limited action Has some organizational footing and emerging confidence, but
actions are irregular. Motivation exists but isn’t strong enough to
sustain habits.
2 Highly organized, cautious executor Well-organized and deliberate, but often slow to execute. Strong
systems, but prefers caution over speed.
3 Strong everyday habits Shows reliable real-world behavior even without elaborate
planning. Confident and motivated enough to maintain consistent
routines.
4 Structured and consistent Combines strong systems with strong execution. Confident,
organized, and steady in follow-through.
45

References
Archuleta, K. L., Burr, E. A., Dale, A. K., Canale, A., Danford, D., Rasure, E., Nelson, J.,
Williams, K., Schindler, K., Coffman, B., & Horwitz, E. (2012). What is financial
therapy? Discovering mechanisms and aspects of an emerging field. Journal of Financial
Therapy, 3(2), 57–77. https://doi.org/10.4148/jft.v3i2.1807
Atkinson, A., & Messy, F. A. (2012). Measuring financial literacy: Results of the OECD /
International Network on Financial Education (INFE) pilot study. OECD Working Papers
on Finance, Insurance and Private Pensions, No. 15.
https://doi.org/10.1787/5k9csfs90fr4-en
Becht, E., McInnes, L., Healy, J., Dutertre, C. A., Kwok, I. W., Ng, L. G., Ginhoux, F., &
Newell, E. W. (2019). Dimensionality reduction for visualizing single-cell data using
UMAP. Nature Biotechnology, 37(1), 38–44. https://doi.org/10.1038/nbt.4314
Bergstra, J., & Bengio, Y. (2012). Random search for hyper-parameter optimization. Journal of
Machine Learning Research, 13, 281–305.
https://www.jmlr.org/papers/v13/bergstra12a.html
Bollen, K. A. (1989). Structural Equations with Latent Variables. New York, NY: Wiley.
Brüggen, E. C., Hogreve, J., Holmlund, M., Kabadayi, S., & Löfgren, M. (2017). Financial
well-being: A conceptualization and research agenda. Journal of Business Research, 79,
228–237. https://doi.org/10.1016/j.jbusres.2017.03.013
Carver, C. S., & Scheier, M. F. (1998). On the self-regulation of behavior. Cambridge University
Press.
CFPB. (2015a). Financial well-being: The goal of financial education. Consumer Financial
Protection Bureau.
46

CFPB. (2015b). Financial well-being scale: Scale development technical report. Consumer
Financial Protection Bureau.
CFPB. (2017). National Financial Well-Being Survey Public Use File. Consumer Financial
Protection Bureau.
https://www.consumerfinance.gov/data-research/financial-well-being-survey-data/
Di Domenico, S. I., Ryan, R. M., Bradshaw, E. L., & Duineveld, J. J. (2022). Motivations for
personal financial management: A self-determination theory perspective. Frontiers in
Psychology, 13(3). https://doi.org/10.3389/fpsyg.2022.977818
Das, S., & Nayak, J. (2022). Customer segmentation via data mining techniques: State-of-the-art
review. Computational Intelligence in Data Mining (pp. 489–507). Springer.
https://doi.org/10.1007/978-981-16-9447-9_38
Diener, E., Emmons, R. A., Larsen, R. J., & Griffin, S. (1985). The Satisfaction With Life Scale.
Journal of Personality Assessment, 49(1), 71–75.
https://doi.org/10.1207/s15327752jpa4901_13
Diener, E., Suh, E. M., Lucas, R. E., & Smith, H. L. (1999). Subjective well-being: Three
decades of progress. Psychological Bulletin, 125(2), 276–302.
https://doi.org/10.1037/0033-2909.125.2.276
Diener, E., Wirtz, D., Tov, W., Kim-Prieto, C., Choi, D., Oishi, S., & Biswas-Diener, R. (2010).
New well-being measures: Short scales to assess flourishing and positive and negative
feelings. Social Indicators Research, 97(2), 143–156.
https://doi.org/10.1007/s11205-009-9493-y
Embretson, S. E., & Reise, S. P. (2000). Item Response Theory for Psychologists. Mahwah, NJ:
Lawrence Erlbaum Associates.
47

Fabrigar, L. R., & Wegener, D. T. (2012). Exploratory Factor Analysis. New York, NY: Oxford
University Press.
Financial Health Network. (2018). Eight Indicators of Financial Health. Retrieved from
https://finhealthnetwork.org/research/financial-health-score/
Garbinsky, E. N., Klesse, A.-K., & Aaker, J. (2014). Money in the bank: Feeling powerful
increases saving. Journal of Consumer Research, 41(3), 610–623.
https://doi.org/10.1086/676965
Gathergood, J. (2012). Self-control, financial literacy and consumer over-indebtedness. Journal
of Economic Psychology, 33(3), 590–602. https://doi.org/10.1016/j.joep.2011.11.006
Ghojogh, B., Ghodsi, A., Karray, F., & Crowley, M. (2021). Uniform Manifold Approximation
and Projection (UMAP) and Its Variants: Tutorial and Survey. arXiv preprint
arXiv:2109.02508. https://doi.org/10.48550/arXiv.2109.02508
Gollwitzer, P. M. (1999). Implementation intentions: Strong effects of simple plans. American
Psychologist, 54(7), 493–503. https://doi.org/10.1037/0003-066X.54.7.493
Grable, J. E., & Joo, S. H. (2004). Environmental and biopsychosocial predictors of financial risk
tolerance. Journal of Financial Counseling and Planning, 15(1), 73–82.
Guan, N., Guariglia, A., Moore, P., Xu, F., & Al‑Janabi, H. (2022). Financial stress and
depression in adults: A systematic review. PLOS One, 17(2), e0264041.
https://doi.org/10.1371/journal.pone.0264041
Gudmunson, C. G., & Danes, S. M. (2011). Family financial socialization: Theory and critical
review. Journal of Family and Economic Issues, 32(4), 644–667.
https://doi.org/10.1007/s10834-011-9275-y
48

Halkidi, M., Batistakis, Y., & Vazirgiannis, M. (2001). On clustering validation techniques.
Journal of Intelligent Information Systems, 17(2–3), 107–145.
https://doi.org/10.1023/A:1012801612483
Hobfoll, S. E. (1989). Conservation of resources: A new attempt at conceptualizing stress.
American Psychologist, 44(3), 513–524. https://doi.org/10.1037/0003-066X.44.3.513
Halandová, K. (2024). The influence of objective financial well-being on life satisfaction.
Ekonomické rozhľady – Economic Review, 53(2), 131–149.
https://doi.org/10.53465/er.2644-7185.2024.2.131-149
Hofman, A., Lier, I., Ikram, M. A., van Wingerden, M., & Luik, A. I. (2023). Uncovering
psychiatric phenotypes using unsupervised machine learning: A data-driven symptoms
approach. European Psychiatry, 66(1), e27. https://doi.org/10.1192/j.eurpsy.2023.13
Jolliffe, I. T. (2002). Principal component analysis (2nd ed.). Springer.
https://doi.org/10.1007/b98835
Kahneman, D., & Tversky, A. (1979). Prospect theory: An analysis of decision under risk.
Econometrica, 47(2), 263–291.
Kaufman, L., & Rousseeuw, P. J. (2009). Finding groups in data: An introduction to cluster
analysis. John Wiley & Sons.
Klontz, B., Britt, S., & Archuleta, K. (2011). Financial therapy: A new approach to financial
distress. Journal of Financial Therapy, 2(1), 1–8. https://doi.org/10.4148/jft.v2i1.451
Kokun, O., Serdiuk, L., & Lytvynenko, O. (2024). Psychological antecedents of life satisfaction.
Psychological Thought, 17(2). https://doi.org/10.37708/psyct.v17i2.975
49

Kyriazos, T. A. (2018). Applied psychometrics: Sample size and sample power considerations in
factor analysis (EFA, CFA) and SEM in general. Psychology, 9(8), 2207–2230.
https://doi.org/10.4236/psych.2018.98126
Lord, F. M. (1980). Applications of Item Response Theory to Practical Testing Problems.
Hillsdale, NJ: Erlbaum.
Lown, J. M. (2011). Development and validation of a financial self-efficacy scale. Journal of
Financial Counseling and Planning, 22(2), 54–63.
https://psycnet.apa.org/record/2013-19795-003
Luthans, F., Avolio, B. J., Avey, J. B., & Norman, S. M. (2007). Positive psychological capital:
Measurement and relationship with performance and satisfaction. Personnel Psychology,
60(3), 541–572. https://doi.org/10.1111/j.1744-6570.2007.00083.x.
Marquand, A. F., Rezek, I., Buitelaar, J., & Beckmann, C. F. (2016). Beyond lumping and
splitting: A review of computational approaches for stratifying psychiatric disorders.
Biological Psychiatry, 80(2), 137–150. https://doi.org/10.1016/j.bpsc.2016.04.002
McInnes, L., Healy, J., & Melville, J. (2018). UMAP: Uniform manifold approximation and
projection for dimension reduction. arXiv preprint arXiv:1802.03426.
https://doi.org/10.48550/arXiv.1802.03426
Mentus, V. (2017). Validity and reliability of subjective wellbeing indicators in sociological
research: The measurement of life satisfaction. Sociološki pregled, 51(1), 157–180.
https://doi.org/10.5937/socpreg1701157m
50

Miotto, R., Li, L., Kidd, B. A., & Dudley, J. T. (2016). Deep patient: An unsupervised
representation to predict the future of patients from the electronic health records.
Scientific Reports, 6, 26094. https://doi.org/10.1038/srep26094
Mõttus, R., Kandler, C., Bleidorn, W., Riemann, R., & McCrae, R. R. (2017). Personality traits
below facets: The consensual validity, longitudinal stability, heritability, and utility of
personality nuances. Journal of Personality and Social Psychology, 112(3), 474–490.
https://doi.org/10.1037/pspp0000100
Nazareth, N., & Reddy, Y. V. R. (2023). Financial applications of machine learning: A literature
review. Expert Systems with Applications, 213, 119640.
https://doi.org/10.1016/j.eswa.2023.119640
Netemeyer, R. G., Warmath, D., Fernandes, D., & Lynch Jr, J. G. (2018). How am I doing?
Perceived financial well-being, its potential antecedents, and its relation to overall
well-being. Journal of Consumer Research, 45(1), 68–89.
https://doi.org/10.1093/jcr/ucx109
Ng, A.Y., Jordan, M.I., Weiss, Y., et al. (2002) On Spectral Clustering: Analysis and An
algorithm. Advances in Neural Information Processing Systems, 2, 849-856.
Pavot, W., & Diener, E. (2008). The Satisfaction With Life Scale and the emerging construct of
life satisfaction. The Journal of Positive Psychology, 3(2), 137–152.
https://doi.org/10.1080/17439760701756946
Peterson, C., & Seligman, M. E. P. (2004). Character strengths and virtues: A handbook and
classification. Oxford University Press.
Prawitz, A. D., Garman, E. T., Sorhaindo, B., O'Neill, B., Kim, J., & Drentea, P. (2006).
InCharge financial distress/financial well-being scale: Development, administration, and
51

score interpretation. Journal of Financial Counseling and Planning, 17(1), 34–50.
https://doi.org/10.1037/t60365-000
Prochaska, J. O., & DiClemente, C. C. (1983). Stages and processes of self-change of smoking:
Toward an integrative model of change. Journal of Consulting and Clinical Psychology,
51(3), 390–395. https://doi.org/10.1037/0022-006X.51.3.390
Şenbabaoğlu, Y., Michailidis, G., & Li, J. Z. (2014). Critical limitations of consensus clustering
in class discovery.Scientific Reports, 4, 6207. https://doi.org/10.1038/srep06207
Seligman, M. E. P. (1975). Helplessness: On depression, development, and death. W.H. Freeman.
Seligman, M. E. P. (2011). Flourish: A visionary new understanding of happiness and
well-being. Free Press.
Serido, J., Shim, S., & Tang, C. (2013). A developmental model of financial capability: A
framework for promoting a successful transition to adulthood. International Journal of
Behavioral Development, 37(4), 287–297. https://doi.org/10.1177/0165025413479476
Shim, S., Xiao, J. J., Barber, B. L., & Lyons, A. C. (2009). Pathways to life success: A
conceptual model of financial well-being for young adults. Journal of Applied
Developmental Psychology, 30(6), 708–723.
https://doi.org/10.1016/j.appdev.2009.02.003
Strömbäck, C., Lind, T., Skagerlund, K., Västfjäll, D., & Tinghög, G. (2017). Does self-control
predict financial behavior and financial well-being? Journal of Behavioral and
Experimental Finance, 14, 30–38. https://doi.org/10.1016/j.jbef.2017.04.002
Thaler, R. H., & Sunstein, C. R. (2008). Nudge: Improving decisions about health, wealth, and
happiness. Yale University Press.
52

Thompson, P. (2021). A study of the financial crisis and its effect on psychological well-being,
health, satisfaction, and financial incapability. Research Square.
https://doi.org/10.21203/rs.3.rs-393768/v1
Thompson, P. W. (2023). Financial crisis and its effect on psychological well-being, health,
satisfaction, and financial incapability: A systematic review. Pakistan Journal of Medical
and Health Sciences, 17(3), 511–517. https://doi.org/10.53350/pjmhs2023173511
Trope, Y., & Liberman, N. (2010). Construal-level theory of psychological distance.
Psychological Review, 117(2), 440–463. https://doi.org/10.1037/a0018963.
Vallacher, R. R., & Wegner, D. M. (1987). What do people think they're doing? Action
identification and human behavior. Psychological Review, 94(1), 3–15.
https://doi.org/10.1037/0033-295X.94.1.3
von Luxburg, U. (2010). Clustering stability: An overview. Foundations and Trends in Machine
Learning, 2(3), 235–274. https://doi.org/10.1561/2200000008
Xiao, J. J., & O’Neill, B. (2016). Consumer financial education and financial capability.
International Journal of Consumer Studies, 40(6), 712–721.
https://doi.org/10.1111/ijcs.12285
Yarkoni, T., & Westfall, J. (2017). Choosing prediction over explanation in psychology: Lessons
from machine learning. Perspectives on Psychological Science, 12(6), 1100–1122.
https://doi.org/10.1177/1745691617693393
Zadhasan, Z. (2024). Predictors of life satisfaction: The role of mindfulness and locus of control.
Journal of Personality and Psychosomatic Research, 2(1), 4–9.
https://doi.org/10.61838/kman.jppr.2.1.2
53

Zhang, Z. (2021). Cluster analysis of consumer's behaviors based on unsupervised learning. In
Proceedings of the 2021 3rd International Conference on Artificial Intelligence and
Advanced Manufacture (pp. 1178–1184). ACM.
https://doi.org/10.1145/3495018.3495360
54

Appendix A: Domain Composition for Clustering and Validation
A1. Proprietary Dataset Sample Items
1. “I am confident I can make wise financial decisions even under pressure.”
2. “I can confidently navigate uncertain financial waters.”
3. “I believe I can reach my long-term financial goals through persistent effort.”
4. “I do not give up on my financial goals easily.”
5. “Unexpected expenses totally stress me out.”
6. “I lie awake in bed at night because I am worried about my financial future.”
7. “When I get a bill notification, it feels like a threat or warning.”
8. “I often avoid looking at my checking or credit card statement to avoid seeing how much
I’ve spent.”
9. “Actually, I gave up trying to keep track of my income and expenses.”
10. “I enjoy learning about personal financial management.”
11. “I actively seek new information about how I can manage my money effectively.”
12. “I see the big picture when planning my finances.”
A2. CFPB Dataset
Capability:
FS1_1-FS1_6, FS2_1-FS2_3, GOALCONF, SELFCONTROL_1-SELFCONTROL_3
Measures perceived financial skills, confidence, sense of control, and self-regulatory
capacity.
Budgeting & Saving:
MANAGE1_1-MANAGE1_4, SAVEHABIT, FRUGALITY, ABSORBSHOCK,
ENDSMEET, SCFHORIZON
55

Captures day-to-day money management practices, saving habits, frugality, and
short-term financial resilience.
Planning:
PROPPLAN_1-PROPPLAN_4, ACT1_1, ACT1_2, ASK1_1, ASK1_2, FINGOALS
Assesses planning behaviors, proactive financial organization, and the extent to which
individuals set and act on financial goals.
Social & Relational:
FINSOC2_1-FINSOC2_7
Measures access to social and interpersonal support, relational resources, and financial
well-being derived from social networks.
Financial Literacy:
FK1correct - FK3correct, KH1correct -KH9correct
Measures financial knowledge, understanding of compound interest, diversification, risk.
LifeSatisfaction:
SWB_1 - SWB_3
Captures global cognitive evaluations of life quality.
Perceived Financial Health:
FWB1_1-FWB1_6, FWB2_1-FWB2_4
Uses standard 10-item Financial Well-Being Scale.
Material Hardship:
MATHARDSHIP_1 - MATHARDSHIP_6, DISTRESS, HOUSING
Captures experiences of material hardship and acute financial stress.
56

The Social & Relational domain is excluded from the clustering inputs because it exhibits very
low structural variability (at most 128 possible combinations), providing broad global gradients
rather than fine-grained psychological information. Including such low-variability domains in a
nonlinear manifold risks collapsing the embedding onto a single severity axis, overshadowing the
richer multi-dimensional variation captured by the core behavioral and psychological domains.
For this reason, this domain is retained only for post-hoc interpretation and validation of the final
cluster solution.
See CFPB survey codebook for additional information
Appendix B: Benchmarking Data Representations and Clustering Methods
To develop a stable and psychologically interpretable clustering pipeline, we conducted three
complementary analyses. First, we examined the geometric properties of the psychometric
domains (Stage 1) to determine whether linear dimensionality reduction (e.g., PCA) could
adequately preserve global and local structure, or whether nonlinear embedding was required.
Second, we benchmarked alternative low-dimensional representations (raw domain scores, PCA
projections, UMAP embeddings) to evaluate their suitability for Stage 2 clustering. Third, within
the preferred representation, we compared several clustering approaches to assess their
qualitative stability and alignment with known behavioral structure. Together, these analyses
provide an empirical foundation for the dimensionality-reduction and clustering choices used in
the main framework.
B.1 Benchmarking Linear vs. Nonlinear Representations in Stage 1
To evaluate whether a linear method such as PCA could adequately serve as the Stage 1
dimensionality reduction step, we assessed domain-level geometry using three complementary
diagnostics:
57

1. Global linearity: the proportion of variance explained by the first principal component
(PC1).
2. Local tangent alignment: the mean ∣cos θ∣ between the domain-level PC1 axis and
local one-dimensional PCA directions estimated from each participant’s 20-nearest
neighbors.
3. Neighborhood preservation: trustworthiness and continuity comparisons between PCA
and UMAP.
Global Linearity (PC1 Variance): Across domains, PC1 captures only 35–59% of total
variance, indicating that no domain is dominated by a single global linear axis. This suggests that
Stage 1 representations must account for multi-dimensional or curved manifold structure rather
than relying on a single major linear direction.
Local Tangent Alignment: Local tangent–global axis alignment is modest, with mean ∣cos θ∣
values ranging from 0.38 to 0.67 (median values ≈ 0.37–0.74 across domains). These moderate
alignments indicate substantial curvature or heterogeneous local variance structures, further
suggesting that a strictly linear mapping such as PCA is unable to capture the local geometry that
Stage 1 must preserve.
Neighborhood Preservation: PCA with two components shows consistently weaker
neighborhood preservation compared with UMAP.
● Trustworthiness: PCA ≈ 0.81–0.91, UMAP ≈ 0.94–0.98
● Continuity: PCA ≈ 0.93–0.96, UMAP ≈ 0.96–0.99
Even when PCA is expanded to four components, UMAP matches or exceeds it across most
domains in both metrics, underscoring that the latent structures underlying these psychometric
58

domains are meaningfully nonlinear.
Across diagnostics--global variance structure, local tangent geometry, and neighborhood
preservation--PCA fails to capture the nonlinear manifold characteristics present in the
domain-level data. UMAP provides substantially better preservation of both local and global
structure, supporting its use as the Stage 1 embedding method.
B.2 Benchmarking Linear vs. Nonlinear Representations in Stage 2
We evaluated whether nonlinear embedding is necessary for identifying stable clusters by
comparing clustering performance across three representations: raw domain scores, linear PCA
projections, and UMAP embeddings. Although t-SNE is a popular nonlinear visualization tool, it
does not preserve global structure and is not suitable for graph-based clustering; therefore, it was
excluded from quantitative comparison. Because the proprietary and CFPB datasets differ in size
and sampling density, results are reported separately.
Proprietary dataset: This dataset exhibits relatively strong inherent structure, reflected in higher
absolute silhouette values across all representations. Clustering on raw domain scores produced a
silhouette of approximately 0.17. PCA projections improved separation modestly (≈0.38 in 2D;
≈0.20 in 4D). UMAP yielded the clearest manifold structure and the strongest separation (≈0.56).
CFPB dataset: In this larger and denser dataset, clustering on raw domain scores again produced
weak separation (≈0.23), indicating that the cross-domain space is not linearly separable. PCA
offered only modest improvement (≈0.32). UMAP achieved substantially stronger separation
(≈0.50) and outperformed linear methods on Calinski–Harabasz and Davies–Bouldin indices,
consistent with meaningful nonlinear structure in the data.
Across both datasets, linear representations--either raw space or PCA--are unable to
recover the nonlinear geometry required for stable, interpretable clustering. UMAP produced
59

markedly stronger separability and more coherent manifold structure, supporting its use as the
Stage 2 embedding in the proposed framework.
B.3 Algorithmic Evaluation of Clustering Methods
Several clustering algorithms are evaluated on the UMAP embeddings
K-means: Considered for its simplicity and widespread use, K-means consistently
underperformed. Its assumption of convex, spherical clusters conflicted with the observed
structure of the UMAP space. The resulting clusters lacked behavioral coherence, and internal
validation metrics (e.g., silhouette score) are poor.
DBSCAN and HDBSCAN: Density-based methods showed initial promise but proved unstable.
DBSCAN often merged distinct subgroups, while HDBSCAN labeled large portions of the data
as noise. Both are highly sensitive to parameter settings (e.g., min_samples, min_cluster_size),
and qualitative inspection revealed weak alignment with psychological or behavioral patterns.
Agglomerative Clustering: This method was more stable than density-based approaches and
delivered modest performance. However, the absence of a clear criterion for selecting the optimal
number of clusters, along with weaker separation metrics, limited its usefulness.
Spectral Clustering: Spectral Clustering demonstrated the strongest performance across both
quantitative and qualitative criteria. It is well-suited to capturing non-convex cluster shapes and
leverages the pairwise similarity structure preserved in the UMAP embedding.
Appendix C: Dimensionality Reduction, Clustering, and Classification Hyperparameters
Supplemental Table C1
UMAP parameters for domain-level (Stage 1) and composite embeddings (Stage 2)
Dataset Domain n_neighbors n_components min_dist spread local_connectivity
Proprietary Character Strengths 24 15 .8 1.00 1
Attitudes & 24 15 .8 1.00 1
Capabilities
60

|       | Psychological Capital  | 22  | 8   | .6  1.00  | 1   |
| ----- | ---------------------- | --- | --- | --------- | --- |
|       | Motivation             | 26  | 8   | .6  1.00  | 1   |
|       | Financial Behavior     | 26  | 8   | .6  1.00  | 1   |
|       | Positive Functioning   | 21  | 5   | .4  1.00  | 1   |
|       | Composite Embedding    | 15  | 2   | .0  .3    | 7   |
| CFPB  | Capability             | 37  | 5   | .6  1.00  | 1   |
|       | Budgeting & Saving     | 16  | 5   | .6  1.00  | 1   |
|       | Planning               | 17  | 5   | .7  1.00  | 1   |
|       | Composite Embedding    | 24  | 2   | .02  1.2  | 7   |

Supplemental Table C2
Spectral Clustering parameters (Stage 2)
| Dataset      | n_clusters  | affinity  | gamma   | eigen_solver  |     |
| ------------ | ----------- | --------- | ------- | ------------- | --- |
| Proprietary  | 7           | rbf       | 8.00    | arpack        |     |
| CFPB         | 7           | rbf       | 2.53    | arpack        |     |

Supplemental Table C3
Imputation details
| Component              |     | Parameter         | Value                       |     |     |
| ---------------------- | --- | ----------------- | --------------------------- | --- | --- |
| IterativeImputer       |     | estimator         | RandomForestRegressor       |     |     |
|                        |     | max_iter          | 10                          |     |     |
|                        |     | initial_strategy  | mean                        |     |     |
|                        |     | imputation_order  | ascending                   |     |     |
|                        |     | skip_complete     | True                        |     |     |
|                        |     | min_value         | 0 for binary, 1 for Likert  |     |     |
|                        |     | max_value         | 1 for binary, 5 for Likert  |     |     |
| RandomForestRegressor  |     | n_estimators      | 250                         |     |     |
|                        |     | max_depth         | 15                          |     |     |

Supplemental Table C4
Classification details
| Component  |     |     | Parameter  | Value  |     |
| ---------- | --- | --- | ---------- | ------ | --- |
Feature Selection (ExtraTreesClassifier)  n_estimators  1000
61

|                                         |     | max_depth         | None                         |
| --------------------------------------- | --- | ----------------- | ---------------------------- |
| Ensemble Classifier (VotingClassifier)  |     | voting            | soft                         |
|                                         |     | base estimators   | RandomForestClassifier, SVC  |
| RandomForestClassifier (model_0)        |     | n_estimators      | 150                          |
|                                         |     | max_depth         | 10                           |
|                                         |     | max_features      | log2                         |
|                                         |     | min_samples_leaf  | 2                            |
|                                         |     | criterion         | gini                         |
|                                         |     | bootstrap         | False                        |
| SVC (model_1)                           |     | kernel            | poly                         |
|                                         |     | degree            | 2                            |
|                                         |     | C                 | 0.5                          |
|                                         |     | gamma             | 0.05                         |
|                                         |     | probability       | True                         |
|                                         |     | shrinking         | False                        |
|                                         |     |                   |                              |
Appendix D: Harmonization of Domains Across Datasets
D1. Domain Harmonization
To explore cross-dataset alignment, we develop a unified five-domain conceptual space shared by
both instruments. The goal of this harmonization is to align instrument-specific domains
according to their underlying psychological functions rather than their exact item structure or
naming conventions. This approach emphasizes functional equivalence rather than item-level
correspondence: each conceptual domain aggregates the set of original domains that, within each
instrument, represent similar underlying processes (e.g., agency, planning, execution, or
motivation). Below we summarize the domain mappings used for the analysis.
Supplemental Table D1
Domain Harmonization Mapping
| Conceptual Domain   | Proprietary Domains  |     | CFPB Domains        |
| ------------------- | -------------------- | --- | ------------------- |
| Financial Behavior  | Financial Behavior   |     | Budgeting & Saving  |
62

Financial Literacy Financial Literacy Financial Literacy
Positive Functioning Positive Functioning Social & Relational Support
Psychological Resources Attitudes & Capabilities; Psychological Capability
Capital; Character Strengths
Motivation & Planning Motivation Planning
Note. Mappings reflect correspondence at the level of higher-order psychological constructs rather than item-level equivalence.
CFPB Social & Relational Support captures aspects of the broader Positive Functioning domain in the proprietary instrument, and
CFPB Planning reflects the behavioral expression of the same organizational tendencies represented in the proprietary Motivation
domain. These conceptual parallels allow the two datasets to be harmonized within a shared domain space, even though specific
item content differs. No direct CFPB analogue exists for proprietary Financial Construal constructs.
Because the instruments differ in the number and granularity of available scales, some conceptual
domains are formed by averaging multiple source domains, while others correspond to a single
scale. For conceptual domain D composed of n source domains s , the harmonized score for a
k k i
𝑛
𝑘
1
participant is the simple mean: 𝐷 = ∑ 𝑠 . This transformation preserves relative standing on
𝑘 𝑛 𝑖
𝑘𝑖−1
the underlying constructs even when item content differs.
D2. Cross-Dataset Cluster Alignment
Since clusters are identified independently within each dataset using the full set of original
domain scores, to compare clusters across datasets, we represent each cluster by a harmonized
cluster profile: a vector of mean scores on the five harmonized domains. For cluster c containing
1
N individuals and harmonized domain j: 𝐷 = ∑ 𝐷 . Each harmonized cluster is
c
𝑐,𝑗 𝑁 𝑛,𝑗
𝑐 𝑛ϵ𝑐
therefore represented by a 5-dimensional profile vector: 𝐷 = (𝐷 ,… , 𝐷 ). These vectors
𝑐 𝑐,1 𝑐,5
constitute the basis for cross-dataset comparison.
We evaluate similarity between clustering solutions using several complementary metrics
that capture local proximity, ordinal correspondence, and global geometric alignment. First,
63

pairwise cluster proximity is summarized using the Cluster-Pair Similarity Index (CPSI), a
normalized inverse-distance measure computed from Euclidean distances between five-domain
cluster profiles. CPSI rescales distances onto an interpretable similarity scale ranging from 0 to
1
1, with larger values indicating more similar profiles: 𝐶𝑃𝑆𝐼 = , where d(i,j) denotes the
𝑖,𝑗 1+𝑑(𝑖,𝑗)
Euclidean distance between cluster i and cluster j in the unified five-domain space. CPSI is used
descriptively and does not impose a one-to-one correspondence between clusters.
Second, we derive a shared global functioning axis by applying principal component
analysis (PCA) to the pooled set of proprietary and CFPB cluster centroids, each represented as a
five-dimensional domain profile. The first principal component (PC1) defines a one-dimensional
gradient summarizing dominant variation across clusters in the harmonized domain space. Each
cluster receives a score on this axis, and cross-dataset alignment in relative cluster ordering is
assessed using the Spearman rank correlation between PC1 scores, with higher correlation
values indicating stronger agreement in cluster ordering across datasets.
Finally, to assess configuration-level geometric similarity, we apply Procrustes analysis
to the proprietary and CFPB centroid matrices expressed in the unified domain space. Procrustes
analysis identifies the optimal rotation and scaling that best superimposes one configuration onto
the other. Geometric similarity is quantified using the Procrustes disparity, defined as the squared
2
|| *||
Frobenius norm of the residual matrix after optimal alignment: 𝐷 = 𝑋 − 𝑌 , where X
denotes the matrix of proprietary cluster centroids (rows = clusters, columns = domains) and Y∗
denotes the optimally transformed CFPB centroid matrix. Lower disparity values indicate greater
similarity in the overall spatial organization of clusters across datasets.
D3. Interpretation Caveats
It is important to note several interpretation caveats. The harmonized domains represent
64

conceptual correspondences, not item-level equivalences, and thus should not be interpreted as
measuring the same constructs with identical psychometric content. Averaging across
contributing scales preserves relative differences, profile shape, and cross-domain patterns, but
does not reproduce fine-grained item structure or latent-factor detail. Comparisons therefore
reflect similarity in high-level psychological organization, not equality of measurement precision
or scale composition. Finally, magnitude differences across datasets (for example, compression
of variation in the CFPB domains) are expected given differences in survey breadth and scale
design. Alignment metrics are consequently interpreted in terms of pattern, ordering, and overall
configuration, which provide more stable and meaningful indicators of structural correspondence
across instruments.
Supplemental Table S1
Descriptive statistics for each psychometric domain
Reports the number of items, scale ranges, descriptive statistics, and internal consistency (Cronbach’s α) for each
domain. All domains exhibit adequate variability and reliability for unsupervised modeling.

Domain  # Items  Scale Range  Mean  SD  Min  Max  Cronbach's α
| Proprietary Dataset  |     |      |             |             |        |
| -------------------- | --- | ---- | ----------- | ----------- | ------ |
| Character Strengths  | 21  | 1–5  | 3.76  1.18  | 1.00  5.00  | 0.930  |
Attitudes & Capabilities  17  1–5  2.74  1.40  1.00  5.00  0.897
Psychological Capital  8  1–5  3.78  1.02  1.00  5.00  0.894
| Motivation            | 14  | 1–5  | 2.99  1.47  | 1.00  5.00  | 0.823  |
| --------------------- | --- | ---- | ----------- | ----------- | ------ |
| Financial Behavior    | 11  | 1–5  | 3.25  1.46  | 1.00  5.00  | 0.875  |
| Positive Functioning  | 9   | 1–5  | 3.19  1.46  | 1.00  5.00  | 0.856  |
Financial Construal Level  10  0/1  0.65  0.47  0.00  1.00  0.651
| Financial Literacy  | 5   | 0/1  | 0.84  0.21  | 0.00  1.00  | 0.461  |
| ------------------- | --- | ---- | ----------- | ----------- | ------ |
| Life Satisfaction   | 5   | 1–5  | 3.33  1.14  | 1.00  5.00  | 0.865  |
Perceived Financial Health  10  1–5  2.94  1.41  1.00  5.00  0.922
Psychological Well-Being  6  1–5  3.07  1.37  1.00  5.00  0.570
| CFPB Dataset   |     |          |             |             |        |
| -------------- | --- | -------- | ----------- | ----------- | ------ |
| Capabilities   | 13  | 1–4/1–5  | 3.35  0.93  | 1.00  5.00  | 0.878  |
65

| Planning  | 9   | 1–5, 0/1  | 3.25  1.35  | 1.00  5.00  | 0.803  |
| --------- | --- | --------- | ----------- | ----------- | ------ |
Budgeting & Saving  9  1–5/1–6  3.97  1.31  1.00  6.00  0.796
| Social & Relational  | 7   | 0/1  | 0.51   0.50  | 0.00  1.00  | 0.779  |
| -------------------- | --- | ---- | ------------ | ----------- | ------ |
| Financial Literacy   | 12  | 0/1  | 0.74  0.44   | 0.00  1.00  | 0.688  |
| Life Satisfaction    | 3   | 1–7  | 5.44  1.44   | 1.00  7.00  | 0.793  |
Perceived Financial Health  10  1–5  3.35  1.20  1.00  5.00  0.917
Material Hardship  8  1–3/1–5  2.81  0.59  1.00  5.00  0.754

Note: Financial Literacy items are scored 1 = correct, 0 = incorrect, and the domain score reflects the proportion
answered correctly.

Supplemental Table S2. Outcome differentiation by cluster membership.
This table reports the results of one-way ANOVA examining how cluster membership predicts three outcome
variables: Life Satisfaction, Psychological Well-Being, Material Hardship, and Perceived Financial Health.
Proprietary=df(6, 330), CFPB=df(6, 5890)
| Outcome              | SSB  | SSW  | F  Partial η²  | Levene’s W  | Levene’s p  |
| -------------------- | ---- | ---- | -------------- | ----------- | ----------- |
| Proprietary Dataset  |      |      |                |             |             |
Life Satisfaction  3.146  13.330  12.984  0.191  0.68  0.667
Psychological Well-Being  2.283  6.309  19.904  0.266  1.99  0.067
Perceived Financial Health  11.849  7.691  84.732  0.606  7.03  <.001
| CFPB Dataset  |     |     |     |     |     |
| ------------- | --- | --- | --- | --- | --- |
Life Satisfaction  1247.742  7398.907  165.546  0.144  24.72  < .001
Material Hardship  174.600  568.844  301.310  0.234  112.63  < .001
Perceived Financial Health  1996.911  2558.232  766.271  0.438  18.84  < .001
Note. Partial η² is reported as effect size. Levene’s test p-values assess homogeneity of variance. In the proprietary
dataset (N = 337), cluster sizes are reasonably balanced (n = 25–71 per cluster), and observed effect sizes are
moderate to large (partial η² = .19–.61), supporting reliable estimation of between-cluster differences.
66