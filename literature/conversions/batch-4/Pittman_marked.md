---
conversion_metadata:
  converted_at: "2026-07-21T08:10:05Z"
  converter_tool: "markitdown"
  converter_version: "0.1.6"
  source_pdf: "Pittman.pdf"
  source_pdf_sha256: "313c51d55829fb17790b318870d9a7b99ab1eb6daa74d0e2a69def199ad43fa5"
  page_count: 9
  markdown_char_count: 117833
---

<!-- PAGE-AWARE EXTRACTION (via pdfminer.six) -->

<!-- PAGE 1 -->

Latenrgy: Model Agnostic Latency and Energy Consumption Prediction
for Binary Classiﬁers

Jason M. Pittman
University of Maryland Global Campus
https://orcid.org/0000-0002-5198-8157

4
2
0
2

c
e
D
6
2

]

G
L
.
s
c
[

1
v
1
4
2
9
1
.
2
1
4
2
:
v
i
X
r
a

Abstract - Machine learning systems increasingly
drive innovation across scientiﬁc ﬁelds and industry,
yet challenges in compute overhead—speciﬁcally dur-
ing inference—limit their scalability and sustainabil-
ity. Responsible AI guardrails, essential for ensur-
ing fairness, transparency, and privacy, further ex-
acerbate these computational demands. This study
addresses critical gaps in the literature, chieﬂy the
lack of generalized predictive techniques for latency
and energy consumption, limited cross-comparisons
of classiﬁers, and unquantiﬁed impacts of RAI
guardrails on inference performance. Using Theory
Construction Methodology, this work constructed a
model-agnostic theoretical framework for predicting
latency and energy consumption in binary classiﬁca-
tion models during inference. The framework synthe-
sizes classiﬁer characteristics, dataset properties, and
RAI guardrails into a uniﬁed analytical instrument.
Two predictive equations are derived that capture the
interplay between these factors while offering gener-
alizability across diverse classiﬁers. The proposed
framework provides foundational insights for design-
ing efﬁcient, responsible ML systems. It enables re-
searchers to benchmark and optimize inference per-
formance and assists practitioners in deploying scal-
able solutions. Finally, this work establishes a theoret-
ical foundation for balancing computational efﬁciency
with ethical AI principles, paving the way for future
empirical validation and broader applications.

Keywords: Responsible AI, Latency, Energy Consump-
tion, Machine Learning, Artiﬁcial Intelligence

1 Introduction

Machine learning (ML) has become integral to diverse
scientiﬁc ﬁelds and business applications. In genomics,
ML helps to decode complex genetic patterns, while in
climatology, it improves the predictive accuracy of ex-

1

treme weather events. Across industries, ML is revolu-
tionizing healthcare through diagnostic support and ad-
vancing ﬁnance via fraud detection systems.

Despite its widespread success, the ﬁeld of ML faces
persistent challenges. One such challenge is compute
overhead or the computational resources consumed dur-
ing the training and inference phases of ML models.
Training involves the extensive energy and processing
power required to optimize model parameters across
large datasets. Inference, on the other hand, focuses on
generating predictions from trained models, where com-
pute overhead is characterized by the interplay between
latency (the time required to produce a prediction) and
energy consumption (the power expended during infer-
ence tasks). High latency or energy consumption can
limit the scalability, accessibility, and sustainability of
ML systems, especially in resource-constrained environ-
ments such as mobile and edge devices (Henderson et al.,
2020).

Adding to these challenges is the growing emphasis
on Responsible AI (RAI). RAI is a framework of prin-
ciples aimed at ensuring AI technologies are ethical,
fair, and trustworthy. RAI principles include trans-
parency, accountability, fairness, privacy, and robust-
ness (Li, Liu, Yang, & Ren, 2024). To operationalize
technical controls and guardrails are
these principles,
employed. While essential for trustworthy AI deploy-
ment, these principles impose additional computational
burdens during training and inference. Doing so exacer-
bates existing issues of latency and energy consumption.

Surprisingly given the importance of RAI,
the liter-
ature offers limited insights into how guardrails in
particular impact compute overhead during inference
(Elesedy, Esperança, Oprea, & Ozay, 2024). While this
gap may seem abstract at a broad level, it becomes highly
relevant in speciﬁc scenarios, such as binary classiﬁca-
tion models deployed in resource-sensitive environments.
Understanding these impacts is critical for guiding the
design and scaling of ML systems in both scientiﬁc and

---

<!-- PAGE 2 -->

industrial contexts.

First,

limited

speciﬁc

study is motivated by three

chal-
This
there is a
lenges within the broader gap.
for esti-
lack of generalized predictive techniques
latency and energy consumption
mating classiﬁer
Sec-
(Mallik, Wang, Xie, Chen, & Han,
classiﬁcation
ond,
cross-comparison
how
of
algorithms
overheads
different models
(Cassales, Gomes, Bifet, Pfahringer, & Senger,
2022).
Finally, the potential impacts of RAI guardrails, such
as explainability and interpretability mechanisms, on
inference latency and energy consumption remain
underexplored (Li et al., 2024).

understanding
these

2023).
of

contribute

hindered

has

to

In response to these challenges, this work sought to con-
struct a model-agnostic equation for predicting latency
and energy consumption in binary classiﬁcation models
during inference with RAI guardrails. By addressing
these issues, this study contributes a theoretical founda-
tion for optimizing compute overhead while balancing
the computational efﬁciency and ethical robustness of
ML systems.

The remainder of this paper is organized as follows: Sec-
tion 2 reviews related work, providing a foundation of
background research. Section 3 details the theoretical
methodology used to derive the predictive equation. Sec-
tion 4 presents the derived equation and its components.
Finally, Section 5 concludes with a discussion of the
study’s implications and directions for future research.

2 Related work

A comprehensive understanding of this study’s contribu-
tion requires familiarity with three key topics: bench-
marking ML compute overhead, the trade-off between
latency and energy consumption, as well as the founda-
tion for RAI. The following sections summarize seminal
and highly inﬂuential works in each topic. Such exist-
ing literature provides necessary context and grounding
for this study’s theoretical framework and its focus on
model-agnostic predictions of compute overhead.

2.1 Benchmarking ML Compute Overhead

Benchmarking compute overhead in machine learning
(ML) is essential for understanding and optimizing the
performance and efﬁciency of ML systems across diverse
tasks and deployment scenarios. Compute overhead en-
compasses the computational resources consumed during

2

both training and inference phases, with signiﬁcant im-
plications for scalability, sustainability, and accessibility
(Strubell, Ganesh, & McCallum, 2020; Henderson et al.,
2020). While training requires substantial resources to
optimize model parameters, inference focuses on gen-
erating predictions in real-time. With inference, met-
rics such as latency (prediction time) and energy con-
sumption (power usage) are critical (Mattson et al., 2020;
Reddi et al., 2020) to total cost of ownership and user
experience. Thus, effective benchmarking provides a
foundation for evaluating and improving ML systems
where achieving low latency and high energy efﬁciency
is paramount (Cassales et al., 2022; Mallik et al., 2023).
Additionally, benchmarks such as MLPerf and related
studies have emphasized the growing importance of quan-
tifying compute overhead to address operational efﬁ-
ciency and environmental impact (Tschand et al., 2024).

A critical distinction exists between compute overhead
during training and inference. Training involves iterative
optimization over large datasets, requiring substantial
computational resources and prolonged processing times
(Strubell et al., 2020).
Inference, by contrast, focuses
on real-time applications, where latency (the time re-
quired to produce a prediction) and energy consumption
(the power required to perform inference) are paramount
(Henderson et al., 2020)). Although the literature has tra-
ditionally emphasized the training phase, inference has
received comparatively less attention.

To address some of these challenges, benchmarking
frameworks such as MLPerf have been developed.
MLPerf provides comprehensive benchmarks for both
training and inference, enabling standardized perfor-
mance evaluations across hardware and software plat-
forms (Mattson et al., 2020). The MLPerf Inference
Benchmark evaluates system performance on tasks such
as image classiﬁcation and object detection, offering in-
sights into latency and energy efﬁciency across different
implementations (Reddi et al., 2020). Further, MLPerf
Power introduces methodologies for assessing energy ef-
ﬁciency, reﬂecting the growing concern over the environ-
mental impact of AI workloads (Tschand et al., 2024).
While these benchmarks are instrumental in understand-
ing empirical performance, they focus on speciﬁc tasks
and lack predictive models that generalize across classi-
ﬁers or operational contexts.

Despite advancements in benchmarking, signiﬁcant gaps
remain. First, current benchmarks such as MLPerf pro-
vide empirical performance data but do not offer general-
ized predictive techniques for estimating latency and en-
ergy consumption across classiﬁers. This limitation hin-
ders the ability to anticipate performance bottlenecks or

---

<!-- PAGE 3 -->

energy demands in novel deployment scenarios, partic-
ularly those involving Responsible AI (RAI) guardrails
(Mallik et al., 2023). Second, no universally accepted
metrics exist for comparing latency and energy con-
sumption across ML frameworks and hardware conﬁg-
urations, making cross-platform evaluations inconsistent
(Mattson et al., 2020).

Additionally,
the literature on benchmarking compute
overhead demonstrates a limited cross-comparison of
classiﬁcation algorithms (e.g., SVM, k-Nearest Neigh-
bors, Random Forest, and Neural Networks) concerning
their effects on latency and energy consumption. Most
studies focus on single-model architectures or narrowly
compare a few model types (Cassales et al., 2022). This
narrow scope restricts generalizability, leaving gaps in
understanding how diverse classiﬁers perform in terms
of computational efﬁciency across real-world scenarios.
Addressing these limitations requires a theoretical frame-
work capable of predicting latency and energy consump-
tion in a model-agnostic manner. Doing so also requires
an understanding of the inherent tradeoff between latency
and energy consumption during inference on ML models.

2.2 The Latency and Energy Consumption

Tradeoff

The relationship between latency and energy consump-
tion during machine learning inference is complex, of-
ten involving trade-offs inﬂuenced by model architec-
ture, hardware, and optimization strategies. Generally,
reducing latency requires increased computational re-
sources, which can lead to higher energy consumption.
Conversely, minimizing energy usage may involve tech-
niques that introduce additional processing time, thereby
increasing latency. This inverse relationship is particu-
larly evident in resource-constrained environments, such
as edge devices, where balancing performance and efﬁ-
ciency is critical.

Recent studies have explored the trade-off between
latency and energy consumption during machine
learning inference, with varying levels of generaliz-
ability across classiﬁcation algorithms. For instance,
researchers examining multilayer perceptrons (MLPs)
demonstrated that hyperparameter optimization could
signiﬁcantly reduce energy consumption during infer-
ence with minimal impact on classiﬁcation accuracy
(Desislavov, Martínez-Plumed, & Hernández-Orallo,
2021). By tuning model complexity, such as reducing
hidden layers or using lower-precision arithmetic, the
study highlights strategies that, while tested on MLPs,
may generalize to other model architectures. However,

the reliance on speciﬁc algorithmic properties limits the
immediate applicability of these ﬁndings to non-neural
network classiﬁers.

2022)

Hauschild

and
analyzed

Hellbrück
In
contrast,
(Hauschild & Hellbrück,
convolu-
tional neural networks (CNNs) deployed on Internet of
Things (IoT) edge devices, emphasizing the dependency
of latency and energy consumption on model complexity
and wireless data rates. The results show that simplifying
CNN architectures can yield substantial efﬁciency gains
in resource-constrained environments, underscoring the
importance of tailoring models to deployment scenarios.
However, this approach is tightly coupled to CNNs and
does not address broader classiﬁcation paradigms, such
as decision trees or support vector machines.

While these studies offer valuable insights into optimiz-
ing latency and energy efﬁciency, the work reﬂects a
broader trend in the literature of focusing on speciﬁc
models or hardware conﬁgurations (Cassales et al., 2022;
Tschand et al., 2024). This limitation underscores the
need for generalized predictive techniques that span di-
verse classiﬁcation algorithms, bridging the gap between
theoretical models and empirical benchmarks. Address-
ing this challenge is critical for advancing the scalability
and efﬁciency of ML systems, particularly as the integra-
tion of Responsible AI (RAI) guardrails introduces addi-
tional computational overhead.

2.3 RAI Controls and Guardrails

Put simply, RAI ensures AI systems are developed and
deployed in ways that are ethical (Floridi et al., 2018;
2016).
Mittelstadt, Allo, Taddeo, Wachter, & Floridi,
Ethical, in this context, includes fairness, transparency,
privacy, security, and trustworthiness as core principles.
The idea is an AI system can be considered responsible
when the set of relevant principles are present. Here,
one should consider present as technical continuous
monitoring.

To that end, ethical principles have experienced rapid
theoretical and practical expansion. In a short time, re-
searchers have developed robust technical frameworks to
measure and evaluate these principles. Two prominent
examples are the Microsoft Responsible Toolbox and the
IBM AI 360 Toolkit. Yet, as much as AI practitioners
can use these frameworks to evaluate models, researchers
(Radclyffe, Ribeiro, & Wortham, 2023; Lu et al., 2024)
suggest RAI is one of the most critical challenges present
in AI and ML.

Culturally,

the rapid expansion has been motivated

3

---

<!-- PAGE 4 -->

include

examples

discriminatory

by demonstrable harm arising from a lack of RAI.
sentenc-
Such
ing and parole decisions in the US justice system
(Angwin, Larson, Mattu, & Kirchner, 2022) as well as
Amazon’s recruitment tool (Dastin, 2022).
Increasing
legal and regulatory requirements such as the US Presi-
dent’s Executive Order and the EU’s AI Act (Wörsdörfer,
2023) are also driving RAI research.

the

literature

(Khan et al.,

2022;
Meanwhile,
Alzubaidi et al.,
2023) has coalesced around ﬁve
speciﬁc RAI principles: explainability, bias or fairness,
robustness or safety,
transparency or interpretability,
and privacy. Additional principles, such as explicability
(Prem, 2023) and accountability (Liu et al., 2022), have
been studied but ultimately fall within the scope of one
or more of the ﬁve speciﬁc principles. Consequently,
industry (IBM, Microsoft, US Department of Defense)
has settled on explainability, bias,
inter-
pretability, and privacy for practical
implementation
of RAI. Trustworthiness tends to be discussed as an
emergent principle only present when the complete set
of RAI principles have sound implementations.

robustness,

On that note, the RAI principles can be implemented
either as a control or guardrail. On the one hand,
controls are techniques applied during the training
phase of a model
the AI system be-
to ensure that
haves ethically and responsibly (Mitchell et al., 2019;
Mehrabi, Morstatter, Saxena, Lerman, & Galstyan,
2021). On the other hand, guardrails are measures
implemented in deployed models to assess the run-
time behavior of models (Raji & Buolamwini, 2019;
Varshney & Alemzadeh, 2017). The aim is to ensure
that the AI system continues to operate responsibly and
ethically throughout the life of the system deployment
(Holstein, Wortman Vaughan, Daumé III, Dudik, & Wallach,
2019).

For example,

Despite the stated need for RAI and the availability of
broad technical frameworks, the computational costs of
implementing these guardrails are often excluded from
benchmarking studies.
the additional
overhead introduced by explainability mechanisms dur-
ing inference remains an under explored area (Li et al.,
2024). Without incorporating RAI considerations, exist-
ing benchmarks risk becoming outdated or incomplete as
the adoption of RAI increases. Moreover, and perhaps
most importantly, the ﬁeld is bereft of operationally vali-
dated knowledge of how runtime RAI may be more of a
poison than a cure.

3 Method

This work was motivated by a single research question:
What variables, coefﬁcients, and propositional operations
are necessary for a model-agnostic equation to be ca-
pable of predicting latency and energy consumption in
binary classiﬁcation models during inference with RAI
guardrails? To answer this question, the study employed
Theory Construction Methodology (TCM) to derive the
model-agnostic equation.

TCM is a structured approach to developing theoretical
frameworks by deﬁning key variables, establishing rela-
tionships, and formalizing them into mathematical mod-
els (Dubin, 1978). While TCM has been widely applied
in theoretical modeling, its application to derive predic-
tive equations for latency and energy consumption in the
context of RAI guardrails represents a novel adaptation
of this methodology. This approach is particularly well-
suited to the research problem because the abstraction
and generalization required for a predictive equation ap-
plicable across diverse classiﬁers necessitates a theoreti-
cal framework (Kaplan & Haenlein, 2019).

The TCM process began with identifying core variables
inﬂuencing latency and energy consumption during in-
ference. These variables were selected based on prior
empirical ﬁndings and theoretical reasoning, ensuring
relevance to diverse classiﬁcation contexts and com-
putational scenarios. For example, the computational
overhead introduced by explainability and interpretabil-
ity guardrails, such as those implemented using SHAP
(Lundberg, 2017) or LIME (Ribeiro, Singh, & Guestrin,
2016), was identiﬁed as a critical variable. This as-
sumption is supported by computational complexity the-
ory, which posits that even linear increases in input size
(O(n)) result in proportional growth in computational de-
mand.
In the context of RAI guardrails, the overhead
arises from explainability mechanisms that augment in-
ference operations with additional interpretive computa-
tions.

Relationships among these variables—such as the in-
verse correlation between latency and energy con-
sumption—are then proposed based on prior research
(Henderson et al., 2020; Mallik et al., 2023). For in-
stance, studies such as those by Hauschild and Hellbrück
(Hauschild & Hellbrück, 2022) demonstrate how compu-
tational trade-offs between latency and energy efﬁciency
are particularly evident in edge computing environments.
Coefﬁcients are incorporated to represent adjustable fac-
tors, including the type of classiﬁer and speciﬁc deploy-
ment conditions. These variables and coefﬁcients are
connected through mathematical operations, such as ad-

4

---

<!-- PAGE 5 -->

ditive and multiplicative terms, to capture their interac-
tions (Cassales et al., 2022).

Data type is represented as a categorical variable with
tabular data encoded as 0, text as 1, and image data as 2.

Finally, the equation is formalized to ensure generaliz-
ability, interpretability, and scalability across classiﬁers
such as SVM, k-Nearest Neighbors, Random Forest, and
Neural Networks. This theoretical framework establishes
a foundation for subsequent empirical validation, where
its predictive accuracy will be tested against experimen-
tal data in diverse operational settings.

RAI guardrails (G) encompass ﬁve principles: explain-
ability, fairness, interpretability, safety, and privacy. Each
principle is modeled as a binary state ([0, 1]), which,
when active, can include a continuous intensity score.
For example, explainability (expl) could take a value of
0.7, representing partial feature-level explanations cover-
ing the top 70% of features.

4 Discussion

4.3 Prediction Equations

The development of a model-agnostic equation for pre-
dicting latency and energy consumption began with iden-
tifying foundational variables (Table 1). These variables
are organized into three sets—classiﬁcation algorithm,
RAI guardrail, and dataset characteristics—all of which
serve as inputs to a prediction function f . The outputs
of the function, latency (L) and energy consumption (E),
are represented collectively as O.

The general equation was expanded into two prediction
equations, capturing latency (L) and energy consumption
(E). These equations model inference performance as a
function of algorithm type, dataset characteristics, and
the computational cost of RAI guardrails.

The latency equation (2) incorporates logarithmic scal-
ing for dataset size, capturing the diminishing impact of
larger datasets on prediction time:

4.1 General Equation

A general equation (1) was constructed to unify the di-
mensions of latency and energy consumption into a cohe-
sive analytical framework:

O = f (A, D, G)

(1)

This equation serves two purposes. First, it provides
a uniﬁed framework to compare inference performance
across binary classiﬁers. Second, it establishes a foun-
dation for synthesizing disparate dimensions of model
performance into a predictive tool, enabling cross-model
comparisons, performance prediction, and the integration
of RAI guardrails into system design.

4.2 Expanded Variables

Each variable set in the general equation is expanded into
measurable elements. Algorithm type (A) contains four
discrete elements: support vector machines (SVM), k-
nearest neighbors (k-NN), random forests (RF), and neu-
ral networks (NN). Categorical encoding is used to rep-
resent binary classiﬁers as a ∈ SV M, k-NN, RF, NN, with
A encoded as 1, 0, 0, 0 to predict L or E for SVM, for in-
stance.

Dataset characteristics (D) include the number of sam-
ples (n), feature dimensionality (p), and data type (t).

L = α+βAA +βD log(n)+γD p+δDt +∑
i

φG,igi +ε (2)

The energy consumption equation (3) applies linear scal-
ing for dataset size to account for cumulative resource
demands during inference:

E = α′ + βAA + β′

Dn + γD p + δDt + ∑
i

G,igi + ε′
φ′

(3)

Both equations use coefﬁcients to model the contribution
of each variable, as summarized in Table 2.

4.4 Novelty and Practical Implications

These equations provide a novel approach to predicting
inference performance across diverse binary classiﬁers.
Unlike prior studies, which focus on empirical bench-
marking or speciﬁc algorithms (Cassales et al., 2022;
Mallik et al., 2023), this framework offers generalizabil-
ity and scalability. Furthermore, it uniquely integrates
the computational cost of RAI guardrails, addressing a
critical gap in the literature (Li et al., 2024; Ribeiro et al.,
2016).

Future empirical validation will use benchmarks such as
MLPerf (Mattson et al., 2020) to evaluate the predictive
accuracy of these models. Practical applications include

5

---

<!-- PAGE 6 -->

Table 1: Foundational variables in a model-agnostic equa-
tion

Variable Set

Classiﬁcation algorithm
RAI guardrail
Dataset characteristics
Output metric

Symbol
A
G
D
O

Note: The prediction function f is undeﬁned in the gen-
eral equation. The formalized prediction equations for L
and E are outlined in Table 2.

Table 2: Coefﬁcients for model-agnostic prediction equations

Coefﬁcient Set

Baseline inference
Error terms for variability1
Algorithm type
Dataset size
Feature dimensionality
Dataset type
Guardrails

Symbol Variable
α,α′
ε,ε′
βA,β′
A
βD,β′
D
γD,γ′
D
δD,δ′
D
φG,i,φ′
G,i

O
-
A
Dn
Dp
Dt
G

Note: 1 Error terms handle unmodeled variability during inference.

overhead of RAI guardrails into a cohesive analytical
tool. Unlike previous studies that focus on speciﬁc clas-
siﬁers or empirical benchmarks, this work offers gener-
alizability and scalability, bridging theoretical modeling
with practical performance evaluation.

The broader signiﬁcance of this research lies in its impli-
cations for designing and deploying efﬁcient, responsible
ML systems. For researchers, the predictive equations
provide a foundational tool for benchmarking and opti-
mizing inference performance across diverse classiﬁers.
For practitioners, they enable informed decisions about
deploying models in resource-constrained environments,
such as edge or mobile devices, while maintaining ethi-
cal robustness. This work also aligns with the growing
need for sustainable AI, offering a pathway to balance
computational efﬁciency with ethical considerations.

In conclusion, this study provides a theoretical founda-
tion for understanding and predicting inference perfor-
mance in ML systems. By addressing critical gaps in the
literature, it lays the groundwork for future advancements
in model-agnostic performance prediction, enabling the
next generation of scalable and responsible AI systems.

optimizing ML systems for edge devices, estimating re-
source demands for RAI-integrated classiﬁers, and en-
abling informed trade-offs between latency, energy con-
sumption, and ethical robustness.

5 Conclusion

AI broadly, and ML in speciﬁc, continues to transform
science and industry. Yet, AI and ML scalability and
accessibility are often constrained by compute overhead.
The literature suggests such issues are particularly no-
table during inference. Challenges such as the lack of
generalized predictive techniques for latency and energy
consumption, limited cross-comparison of classiﬁcation
algorithms, and the unquantiﬁed computational impact
of RAI guardrails have left critical gaps in the literature.
This study aimed to address these gaps by developing
a model-agnostic equation capable of predicting latency
and energy consumption in binary classiﬁcation models
during inference with RAI guardrails.

The key contributions of this work include a model-
agnostic theoretical framework for analyzing inference
performance and two predictive equations for latency and
energy consumption. These models synthesize algorithm
characteristics, dataset properties, and the computational

6

---

<!-- PAGE 7 -->

5.1 Limitations

While this study provides a foundational framework for
predicting inference latency and energy consumption in
binary classiﬁcation models, ﬁve limitations should be
acknowledged.

First, the prediction equations rely on assumptions about
variable relationships, such as logarithmic scaling for
dataset size in latency prediction and linear scaling
for energy consumption. While these assumptions are
grounded in prior research and theoretical reasoning, they
may not fully capture real-world complexities in all sce-
narios. Additional research, more especially practical ex-
perimentation may reveal to what extent such a limitation
is addressable.

Second, the focus on binary classiﬁcation tasks excludes
multi-class classiﬁcation and other ML tasks, such as
regression or clustering, which may involve different
computational trade-offs. Along similar thinking, this
work does not account for potential innovations becom-
ing available in the future.

Third, the representation of RAI guardrails, while prac-
tical, simpliﬁes potential computational impact. Com-
plex guardrails, such as differential privacy or trustwor-
thiness mechanisms, may require more nuanced model-
ing to fully capture resource demands.

Fourth, the framework abstracts dataset characteristics to
size, feature dimensionality, and data type. Other impor-
tant factors, such as data quality or sparsity, are not in-
cluded and could affect predictions in speciﬁc contexts.

Finally, this study presents theoretical equations without
empirical validation. While the models are rigorous, their
accuracy and generalizability remain untested. Future
work will involve validating these equations with exper-
imental data across diverse classiﬁers, datasets, and de-
ployment environments to ensure their practical applica-
bility.

5.2 Future work

There are several areas for future work based on the the-
oretical framework demonstrated in this research.

Foremost, experimentation is necessary to validate and
quantify the coefﬁcients in the latency (L) and energy
consumption (E) prediction equations. Empirical studies
using benchmark datasets and platforms such as MLPerf
will help calibrate these coefﬁcients, ensuring their accu-
racy across diverse classiﬁers and deployment environ-
ments. Validation efforts should also explore the sensitiv-

ity of the equations to different input variables, such as
dataset characteristics and RAI guardrails, to reﬁne the
models further.

Furthermore, the generalizability of the L and E predic-
tive equations may be investigated by varying the set A
across a variety of AI subﬁelds. Of particular interest,
given the mainstream perception of AI, might be the ap-
plication of the framework to Large Language Models
(LLMs), where inference latency and energy efﬁciency
are critical due to their size and complexity. Additionally,
frontier research areas such as neuro-symbolic AI repre-
sent a compelling opportunity for extending the frame-
work to hybrid models that combine symbolic reasoning
with deep learning. These extensions could provide valu-
able insights into the computational trade-offs in emerg-
ing AI paradigms.

Another avenue for future work involves reﬁning the
representation of RAI guardrails. Current binary and
intensity-scale representations may oversimplify the
computational demands of advanced guardrails, such as
differential privacy, adversarial robustness, or nuanced in-
terpretability mechanisms. Developing more granular or
context-aware models for guardrail contributions could
enhance the framework’s precision and applicability.

Finally, while this study focused on binary classiﬁca-
tion tasks, future research could extend the framework
to multi-class classiﬁcation and other ML tasks, such as
regression or clustering. These extensions would test
the framework’s scalability and adaptability, addressing
broader applications in AI.

References

Alzubaidi, L., Al-Sabaawi, A., Bai, J., Dukhan, A., Alke-
nani, A. H., Al-Asadi, A., . . . others (2023). To-
wards risk-free trustworthy artiﬁcial intelligence:
Signiﬁcance and requirements. International Jour-
nal of Intelligent Systems, 2023(1), 4459198.
Angwin, J., Larson, J., Mattu, S., & Kirchner, L. (2022).
Machine bias. In Ethics of data and analytics (pp.
254–264). Auerbach Publications.

Cassales, G., Gomes, H. M., Bifet, A., Pfahringer, B., &
(2022). Balancing performance and
Senger, H.
energy consumption of bagging ensembles for the
classiﬁcation of data streams in edge computing.
IEEE Transactions on Network and Service Man-
agement, 20(3), 3038–3054.

Dastin, J.

(2022). Amazon scraps secret ai recruiting
tool that showed bias against women. In Ethics of

7

---

<!-- PAGE 8 -->

data and analytics (pp. 296–299). Auerbach Publi-
cations.

Desislavov, R., Martínez-Plumed, F., & Hernández-
Orallo, J.
(2021). Compute and energy con-
sumption trends in deep learning inference. arXiv
preprint arXiv:2109.05472.

Dubin, R. (1978). Theory building. The Free Press.
Elesedy, H., Esperança, P. M., Oprea, S. V., & Ozay, M.
(2024). Lora-guard: Parameter-efﬁcient guardrail
adaptation for content moderation of large lan-
guage models. arXiv preprint arXiv:2407.02987.

Floridi, L., Cowls, J., Beltrametti, M., Chatila, R.,
(2018).
Chazerand, P., Dignum, V.,
Ai4people—an ethical framework for a good ai so-
ciety: opportunities, risks, principles, and recom-
mendations. Minds and machines, 28, 689–707.

. . . others

Hauschild, S., & Hellbrück, H. (2022). Latency and en-
ergy consumption of convolutional neural network
In Global iot
models from iot edge perspective.
summit (pp. 385–396). Springer.

Henderson, P., Hu, J., Romoff, J., Brunskill, E., Juraf-
sky, D., & Pineau, J. (2020). Towards the system-
atic reporting of the energy and carbon footprints
of machine learning. Journal of Machine Learning
Research, 21(248), 1–43.

Holstein, K., Wortman Vaughan, J., Daumé III, H.,
Dudik, M., & Wallach, H. (2019). Improving fair-
ness in machine learning systems: What do indus-
try practitioners need? In Proceedings of the 2019
chi conference on human factors in computing sys-
tems (pp. 1–16).
Kaplan, A., & Haenlein, M.

(2019). Siri, siri, in my
hand: Who’s the fairest in the land? on the inter-
pretations, illustrations, and implications of artiﬁ-
cial intelligence. Business horizons, 62(1), 15–25.
Khan, A. A., Badshah, S., Liang, P., Waseem, M., Khan,
B., Ahmad, A., . . . Akbar, M. A. (2022). Ethics
of ai: A systematic literature review of principles
and challenges. In Proceedings of the 26th interna-
tional conference on evaluation and assessment in
software engineering (pp. 383–392).

Li, P., Liu, Y., Yang, J., & Ren, S.

(2024). Towards
socially and environmentally responsible ai. arXiv
preprint arXiv:2407.05176.

Liu, H., Wang, Y., Fan, W., Liu, X., Li, Y., Jain, S., . . .
Tang, J. (2022). Trustworthy ai: A computational
perspective. ACM Transactions on Intelligent Sys-
tems and Technology, 14(1), 1–59.

Lu, Q., Zhu, L., Xu, X., Whittle, J., Zowghi, D., &
(2024). Responsible ai pattern cata-
Jacquet, A.
logue: A collection of best practices for ai gover-
nance and engineering. ACM Computing Surveys,
56(7), 1–35.

Lundberg, S.

(2017).
terpreting model predictions.
arXiv:1705.07874.

A uniﬁed approach to in-
arXiv preprint

Mallik, A., Wang, H., Xie, J., Chen, D., & Han, K.
(2023). Epam: A predictive energy model for mo-
bile ai. In Icc 2023-ieee international conference
on communications (pp. 954–959).

Mattson, P., Reddi, V. J., Cheng, C., Coleman, C., Di-
amos, G., Kanter, D., . . . others (2020). Mlperf:
An industry standard benchmark suite for machine
learning performance. IEEE Micro, 40(2), 8–16.

Mehrabi, N., Morstatter, F., Saxena, N., Lerman, K., &
(2021). A survey on bias and fair-
Galstyan, A.
ness in machine learning. ACM computing surveys
(CSUR), 54(6), 1–35.

Mitchell, M., Wu, S., Zaldivar, A., Barnes, P., Vasserman,
L., Hutchinson, B., . . . Gebru, T. (2019). Model
In Proceedings of the
cards for model reporting.
conference on fairness, accountability, and trans-
parency (pp. 220–229).

Mittelstadt, B. D., Allo, P., Taddeo, M., Wachter, S.,
& Floridi, L.
(2016). The ethics of algorithms:
Mapping the debate. Big Data & Society, 3(2),
2053951716679679.

Prem, E. (2023). From ethical ai frameworks to tools:
a review of approaches. AI and Ethics, 3(3), 699–
716.

Radclyffe, C., Ribeiro, M., & Wortham, R. H.

(2023).
The assessment list for trustworthy artiﬁcial intelli-
gence: A review and recommendations. Frontiers
in artiﬁcial intelligence, 6, 1020592.

Raji, I. D., & Buolamwini, J. (2019). Actionable audit-
ing: Investigating the impact of publicly naming
biased performance results of commercial ai prod-
ucts. In Proceedings of the 2019 aaai/acm confer-
ence on ai, ethics, and society (pp. 429–435).
Reddi, V. J., Cheng, C., Kanter, D., Mattson, P.,
(2020).
Schmuelling, G., Wu, C.-J.,
In 2020 acm/ieee
Mlperf inference benchmark.
47th annual international symposium on computer
architecture (isca) (pp. 446–459).
Ribeiro, M. T., Singh, S., & Guestrin, C.

"
why should i trust you?" explaining the predictions
of any classiﬁer. In Proceedings of the 22nd acm
sigkdd international conference on knowledge dis-
covery and data mining (pp. 1135–1144).

. . . others

(2016).

Strubell, E., Ganesh, A., & McCallum, A. (2020). En-
ergy and policy considerations for modern deep
In Proceedings of the aaai
learning research.
conference on artiﬁcial intelligence (Vol. 34, pp.
13693–13696).

Tschand, A., Rajan, A. T. R., Idgunji, S., Ghosh, A.,
Holleman, J., Kiraly, C., . . . others (2024). Mlperf

8

---

<!-- PAGE 9 -->

power: Benchmarking the energy efﬁciency of
machine learning systems from microwatts to
arXiv preprint
megawatts for sustainable ai.
arXiv:2410.12032.

Varshney, K. R., & Alemzadeh, H. (2017). On the safety
of machine learning: Cyber-physical systems, de-
cision sciences, and data products. Big data, 5(3),
246–255.

Wörsdörfer, M. (2023). The eu’s artiﬁcial intelligence
act: an ordoliberal assessment. AI and Ethics, 1–
16.

9

<!-- MARKITDOWN CONVERSION -->

<!-- Full MarkItDown conversion for formatting fidelity. -->

Latenrgy: Model Agnostic Latency and Energy Consumption Prediction
|     |     |     |     |     |     | for Binary |         | Classifiers |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | ---------- | ------- | ----------- | --- | --- | --- | --- | --- | --- | --- |
|     |     |     |     |     |     |            | JasonM. | Pittman     |     |     |     |     |     |     |     |
UniversityofMarylandGlobalCampus
https://orcid.org/0000-0002-5198-8157
Abstract - Machine learning systems increasingly treme weather events. Across industries, ML is revolu-
4202 ceD 62  ]GL.sc[  1v14291.2142:viXra drive innovation across scientific fields and industry, tionizing healthcare through diagnostic support and ad-
yetchallengesincomputeoverhead—specifically dur- vancingfinanceviafrauddetection systems.
| ing inference—limit             |             |               | their scalability |                       | and               | sustainabil-   |         |                                           |                |                  |                |                      |                    |                |          |
| ------------------------------- | ----------- | ------------- | ----------------- | --------------------- | ----------------- | -------------- | ------- | ----------------------------------------- | -------------- | ---------------- | -------------- | -------------------- | ------------------ | -------------- | -------- |
|                                 |             |               |                   |                       |                   |                |         | Despite                                   | its widespread |                  | success,       |                      | the field          | of ML          | faces    |
| ity. Responsible                |             | AI            | guardrails,       |                       | essential         | for            | ensur-  |                                           |                |                  |                |                      |                    |                |          |
|                                 |             |               |                   |                       |                   |                |         | persistent                                | challenges.    |                  | One            | such                 | challenge          | is             | compute  |
| ing fairness,                   |             | transparency, |                   | and                   | privacy,          | further        | ex-     |                                           |                |                  |                |                      |                    |                |          |
|                                 |             |               |                   |                       |                   |                |         | overhead                                  | or the         | computational    |                | resources            |                    | consumed       | dur-     |
| acerbate                        | these       | computational |                   | demands.              |                   | This           | study   |                                           |                |                  |                |                      |                    |                |          |
|                                 |             |               |                   |                       |                   |                |         | ing the                                   | training       | and              | inference      | phases               |                    | of ML          | models.  |
| addresses                       | critical    | gaps          | in                | the literature,       |                   | chiefly        | the     |                                           |                |                  |                |                      |                    |                |          |
|                                 |             |               |                   |                       |                   |                |         | Training                                  | involves       | the              | extensive      |                      | energy             | and processing |          |
| lack of                         | generalized |               | predictive        | techniques            |                   | for            | latency |                                           |                |                  |                |                      |                    |                |          |
|                                 |             |               |                   |                       |                   |                |         | power                                     | required       | to optimize      |                | model                | parameters         |                | across   |
| and energy                      |             | consumption,  |                   | limited               | cross-comparisons |                |         |                                           |                |                  |                |                      |                    |                |          |
|                                 |             |               |                   |                       |                   |                |         | large datasets.                           |                | Inference,       | on             | the                  | other hand,        | focuses        | on       |
| of classifiers,                 |             | and           | unquantified      |                       | impacts           |                | of RAI  |                                           |                |                  |                |                      |                    |                |          |
|                                 |             |               |                   |                       |                   |                |         | generating                                | predictions    |                  | from           | trained              | models,            | where          | com-     |
| guardrails                      | on          | inference     | performance.      |                       |                   | Using          | Theory  |                                           |                |                  |                |                      |                    |                |          |
|                                 |             |               |                   |                       |                   |                |         | pute overhead                             |                | is characterized |                | by                   | the interplay      |                | between  |
| Construction                    |             | Methodology,  |                   | this                  | work              | constructed    |         | a                                         |                |                  |                |                      |                    |                |          |
|                                 |             |               |                   |                       |                   |                |         | latency                                   | (the time      | required         |                | to produce           | a                  | prediction)    | and      |
| model-agnostic                  |             | theoretical   |                   | framework             |                   | for predicting |         |                                           |                |                  |                |                      |                    |                |          |
|                                 |             |               |                   |                       |                   |                |         | energy                                    | consumption    |                  | (the power     |                      | expended           | during         | infer-   |
| latency                         | and         | energy        | consumption       |                       | in binary         | classifica-    |         |                                           |                |                  |                |                      |                    |                |          |
|                                 |             |               |                   |                       |                   |                |         | ence tasks).                              | High           | latency          |                | or energy            | consumption        |                | can      |
| tionmodelsduringinference.      |             |               |                   | Theframeworksynthe-   |                   |                |         |                                           |                |                  |                |                      |                    |                |          |
|                                 |             |               |                   |                       |                   |                |         | limit the                                 | scalability,   |                  | accessibility, |                      | and sustainability |                | of       |
| sizesclassifiercharacteristics, |             |               |                   | datasetproperties,and |                   |                |         |                                           |                |                  |                |                      |                    |                |          |
|                                 |             |               |                   |                       |                   |                |         | ML systems,                               | especially     |                  | in             | resource-constrained |                    |                | environ- |
| RAI guardrails                  |             | into          | a unified         | analytical            |                   | instrument.    |         |                                           |                |                  |                |                      |                    |                |          |
|                                 |             |               |                   |                       |                   |                |         | mentssuchasmobileandedgedevices(Henderson |                |                  |                |                      |                    |                | etal.,   |
Twopredictiveequationsarederivedthatcapturethe
2020).
| interplay   | between | these   | factors      |     | while | offering     | gener- |        |          |            |     |     |             |     |          |
| ----------- | ------- | ------- | ------------ | --- | ----- | ------------ | ------ | ------ | -------- | ---------- | --- | --- | ----------- | --- | -------- |
|             |         |         |              |     |       |              |        | Adding | to these | challenges |     | is  | the growing |     | emphasis |
| alizability | across  | diverse | classifiers. |     |       | The proposed |        |        |          |            |     |     |             |     |          |
framework provides foundational insights for design- on Responsible AI (RAI). RAI is a framework of prin-
ing efficient, responsible ML systems. It enables re- ciples aimed at ensuring AI technologies are ethical,
|           |     |           |     |          |     |           |      | fair, and | trustworthy. |     | RAI | principles |     | include | trans- |
| --------- | --- | --------- | --- | -------- | --- | --------- | ---- | --------- | ------------ | --- | --- | ---------- | --- | ------- | ------ |
| searchers | to  | benchmark | and | optimize |     | inference | per- |           |              |     |     |            |     |         |        |
formance and assists practitioners in deploying scal- parency, accountability, fairness, privacy, and robust-
ablesolutions. Finally,thisworkestablishesatheoret- ness (Li,Liu,Yang,&Ren, 2024). To operationalize
icalfoundationforbalancingcomputationalefficiency these principles, technical controls and guardrails are
|              |     |                |     |        |     |         |        | employed. | While | essential |     | for trustworthy |     | AI  | deploy- |
| ------------ | --- | -------------- | --- | ------ | --- | ------- | ------ | --------- | ----- | --------- | --- | --------------- | --- | --- | ------- |
| with ethical |     | AI principles, |     | paving | the | way for | future |           |       |           |     |                 |     |     |         |
empiricalvalidation andbroaderapplications. ment, these principles impose additional computational
|           |             |     |     |          |        |          |     | burdens       | during                               | training | and | inference. | Doing | so  | exacer- |
| --------- | ----------- | --- | --- | -------- | ------ | -------- | --- | ------------- | ------------------------------------ | -------- | --- | ---------- | ----- | --- | ------- |
| Keywords: | Responsible |     | AI, | Latency, | Energy | Consump- |     |               |                                      |          |     |            |       |     |         |
|           |             |     |     |          |        |          |     | batesexisting | issuesoflatencyandenergyconsumption. |          |     |            |       |     |         |
tion,MachineLearning,ArtificialIntelligence
|     |     |     |     |     |     |     |     | Surprisingly | given   | the     | importance |          | of     | RAI,       | the liter- |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------ | ------- | ------- | ---------- | -------- | ------ | ---------- | ---------- |
|     |     |     |     |     |     |     |     | ature offers | limited |         | insights   | into     | how    | guardrails | in         |
|     |     |     |     |     |     |     |     | particular   | impact  | compute |            | overhead | during |            | inference  |
1 Introduction
|     |     |     |     |     |     |     |     | (Elesedy,Esperança, |     |     | Oprea,&Ozay, |     | 2024). | While | this |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------------- | --- | --- | ------------ | --- | ------ | ----- | ---- |
gapmayseemabstractatabroadlevel,itbecomeshighly
Machine learning (ML) has become integral to diverse relevant in specific scenarios, such as binary classifica-
scientific fields and business applications. In genomics, tionmodelsdeployedinresource-sensitive environments.
|          |     |        |         |         |           |     |       | Understanding |     | these | impacts | is critical |     | for guiding | the |
| -------- | --- | ------ | ------- | ------- | --------- | --- | ----- | ------------- | --- | ----- | ------- | ----------- | --- | ----------- | --- |
| ML helps | to  | decode | complex | genetic | patterns, |     | while | in            |     |       |         |             |     |             |     |
climatology, it improves the predictive accuracy of ex- design and scaling of ML systems in both scientific and
1

industrial contexts. both training and inference phases, with significant im-
|                             |             |                  |            |      |            |          |                | plications        | for scalability, |             | sustainability, |             | and       | accessibility |         |
| --------------------------- | ----------- | ---------------- | ---------- | ---- | ---------- | -------- | -------------- | ----------------- | ---------------- | ----------- | --------------- | ----------- | --------- | ------------- | ------- |
| This study                  |             | is motivated     |            | by   | three      | specific |                | chal-             |                  |             |                 |             |           |               |         |
|                             |             |                  |            |      |            |          |                | (Strubell,Ganesh, |                  | &McCallum,  |                 | 2020;       | Henderson |               | etal.,  |
| lenges                      | within      | the              | broader    | gap. |            | First,   | there          | is a              |                  |             |                 |             |           |               |         |
|                             |             |                  |            |      |            |          |                | 2020).            | While            | training    | requires        | substantial |           | resources     | to      |
| lack of                     | generalized |                  | predictive |      | techniques |          | for            | esti-             |                  |             |                 |             |           |               |         |
|                             |             |                  |            |      |            |          |                | optimize          | model            | parameters, |                 | inference   | focuses   |               | on gen- |
| mating                      | classifier  |                  | latency    | and  | energy     |          | consumption    |                   |                  |             |                 |             |           |               |         |
|                             |             |                  |            |      |            |          |                | erating           | predictions      | in          | real-time.      | With        |           | inference,    | met-    |
| (Mallik,Wang,Xie,Chen,&Han, |             |                  |            |      |            | 2023).   |                | Sec-              |                  |             |                 |             |           |               |         |
|                             |             |                  |            |      |            |          |                | rics such         | as latency       |             | (prediction     | time)       | and       | energy        | con-    |
| ond,                        | limited     | cross-comparison |            |      |            | of       | classification |                   |                  |             |                 |             |           |               |         |
sumption(powerusage)arecritical(Mattsonetal.,2020;
| algorithms        | has                     | hindered        |                  | understanding |             |             | of        | how             |                 |            |         |              |              |            |          |
| ----------------- | ----------------------- | --------------- | ---------------- | ------------- | ----------- | ----------- | --------- | --------------- | --------------- | ---------- | ------- | ------------ | ------------ | ---------- | -------- |
|                   |                         |                 |                  |               |             |             |           | Reddietal.,     | 2020)           | to         | total   | cost of      | ownership    |            | and user |
| different         | models                  |                 | contribute       |               | to          | these       | overheads |                 |                 |            |         |              |              |            |          |
|                   |                         |                 |                  |               |             |             |           | experience.     | Thus,           | effective  |         | benchmarking |              | provides   | a        |
| (Cassales,        | Gomes,Bifet,Pfahringer, |                 |                  |               | &Senger,    |             |           | 2022).          |                 |            |         |              |              |            |          |
|                   |                         |                 |                  |               |             |             |           | foundation      | for             | evaluating | and     | improving    |              | ML         | systems  |
| Finally,          | the potential           |                 | impacts          |               | of RAI      | guardrails, |           | such            |                 |            |         |              |              |            |          |
|                   |                         |                 |                  |               |             |             |           | where achieving |                 | low        | latency | and high     | energy       | efficiency |          |
| as explainability |                         | and             | interpretability |               |             | mechanisms, |           | on              |                 |            |         |              |              |            |          |
|                   |                         |                 |                  |               |             |             |           | is paramount    | (Cassalesetal., |            |         | 2022;        | Malliketal., |            | 2023).   |
| inference         | latency                 |                 | and              | energy        | consumption |             |           | remain          |                 |            |         |              |              |            |          |
|                   |                         |                 |                  |               |             |             |           | Additionally,   |                 | benchmarks | such    | as           | MLPerf       | and        | related  |
| underexplored     |                         | (Lietal.,2024). |                  |               |             |             |           |                 |                 |            |         |              |              |            |          |
studieshaveemphasizedthegrowingimportanceofquan-
In response to these challenges, this work sought tocon- tifying compute overhead to address operational effi-
| struct a          | model-agnostic |            | equation    |             | for            | predicting  |            | latency                |             |               |                            |                  |              |             |           |
| ----------------- | -------------- | ---------- | ----------- | ----------- | -------------- | ----------- | ---------- | ---------------------- | ----------- | ------------- | -------------------------- | ---------------- | ------------ | ----------- | --------- |
|                   |                |            |             |             |                |             |            | ciencyandenvironmental |             |               | impact(Tschandetal.,2024). |                  |              |             |           |
| and energy        | consumption    |            |             | in binary   | classification |             |            | models                 |             |               |                            |                  |              |             |           |
|                   |                |            |             |             |                |             |            | A critical             | distinction |               | exists                     | between          | compute      | overhead    |           |
| during            | inference      | with       | RAI         | guardrails. |                | By          | addressing |                        |             |               |                            |                  |              |             |           |
|                   |                |            |             |             |                |             |            | duringtraining         |             | andinference. |                            | Traininginvolves |              |             | iterative |
| these issues,     |                | this study | contributes |             | a              | theoretical |            | founda-                |             |               |                            |                  |              |             |           |
|                   |                |            |             |             |                |             |            | optimization           | over        | large         | datasets,                  |                  | requiring    | substantial |           |
| tion for          | optimizing     |            | compute     | overhead    |                | while       | balancing  |                        |             |               |                            |                  |              |             |           |
|                   |                |            |             |             |                |             |            | computational          |             | resources     | andprolongedprocessing     |                  |              |             | times     |
| the computational |                | efficiency |             | and         | ethical        | robustness  |            | of                     |             |               |                            |                  |              |             |           |
|                   |                |            |             |             |                |             |            | (Strubelletal.,        |             | 2020).        | Inference,                 |                  | by contrast, |             | focuses   |
MLsystems.
|     |     |     |     |     |     |     |     | on real-time | applications, |     | where | latency |     | (the | time re- |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------ | ------------- | --- | ----- | ------- | --- | ---- | -------- |
Theremainder ofthispaperisorganized asfollows: Sec- quired to produce a prediction) and energy consumption
| tion 2 reviews |     | related | work, | providing |     | a foundation |     | of                |     |           |     |            |     |              |     |
| -------------- | --- | ------- | ----- | --------- | --- | ------------ | --- | ----------------- | --- | --------- | --- | ---------- | --- | ------------ | --- |
|                |     |         |       |           |     |              |     | (thepowerrequired |     | toperform |     | inference) |     | areparamount |     |
background research. Section 3 details the theoretical (Henderson etal.,2020)). Althoughtheliteraturehastra-
methodology usedtoderivethepredictive equation. Sec- ditionally emphasized the training phase, inference has
| tion 4 presents     |         | the derived |               | equation | and                | its        | components. |                       |             |               |                |             |              |              |          |
| ------------------- | ------- | ----------- | ------------- | -------- | ------------------ | ---------- | ----------- | --------------------- | ----------- | ------------- | -------------- | ----------- | ------------ | ------------ | -------- |
|                     |         |             |               |          |                    |            |             | receivedcomparatively |             |               | lessattention. |             |              |              |          |
| Finally,            | Section | 5           | concludes     | with     | a                  | discussion |             | of the                |             |               |                |             |              |              |          |
|                     |         |             |               |          |                    |            |             | To address            | some        | of            | these          | challenges, |              | benchmarking |          |
| study’simplications |         |             | anddirections |          | forfutureresearch. |            |             |                       |             |               |                |             |              |              |          |
|                     |         |             |               |          |                    |            |             | frameworks            | such        | as            | MLPerf         | have        | been         | developed.   |          |
|                     |         |             |               |          |                    |            |             | MLPerf                | provides    | comprehensive |                | benchmarks  |              |              | for both |
|                     |         |             |               |          |                    |            |             | training              | and         | inference,    | enabling       |             | standardized |              | perfor-  |
| 2 Related           |         | work        |               |          |                    |            |             |                       |             |               |                |             |              |              |          |
|                     |         |             |               |          |                    |            |             | mance                 | evaluations | across        | hardware       |             | and          | software     | plat-    |
|                     |         |             |               |          |                    |            |             | forms (Mattsonetal.,  |             |               | 2020).         | The         | MLPerf       | Inference    |          |
A comprehensive understanding of this study’s contribu- Benchmark evaluates system performance on tasks such
tion requires familiarity with three key topics: bench- as image classification and object detection, offering in-
|         |     |         |           |     |     |           |         | sights into | latency | and | energy | efficiency | across |     | different |
| ------- | --- | ------- | --------- | --- | --- | --------- | ------- | ----------- | ------- | --- | ------ | ---------- | ------ | --- | --------- |
| marking | ML  | compute | overhead, |     | the | trade-off | between |             |         |     |        |            |        |     |           |
latency and energy consumption, as well as the founda- implementations (Reddietal., 2020). Further, MLPerf
tionforRAI.Thefollowing sections summarize seminal Powerintroduces methodologies forassessing energy ef-
ficiency,reflectingthegrowingconcernovertheenviron-
| and highly | influential |     | works | in  | each | topic. | Such | exist- |     |     |     |     |     |     |     |
| ---------- | ----------- | --- | ----- | --- | ---- | ------ | ---- | ------ | --- | --- | --- | --- | --- | --- | --- |
ing literature provides necessary context and grounding mental impact of AI workloads (Tschandetal., 2024).
for this study’s theoretical framework and its focus on While these benchmarks are instrumental in understand-
model-agnostic predictions ofcomputeoverhead. ing empirical performance, they focus on specific tasks
|                  |     |         |           |          |     |          |          | and lack            | predictive | models    |                 | that generalize |                 | across | classi- |
| ---------------- | --- | ------- | --------- | -------- | --- | -------- | -------- | ------------------- | ---------- | --------- | --------------- | --------------- | --------------- | ------ | ------- |
|                  |     |         |           |          |     |          |          | fiersoroperational  |            | contexts. |                 |                 |                 |        |         |
| 2.1 Benchmarking |     |         | MLCompute |          |     | Overhead |          |                     |            |           |                 |                 |                 |        |         |
|                  |     |         |           |          |     |          |          | Despiteadvancements |            |           | inbenchmarking, |                 | significantgaps |        |         |
|                  |     |         |           |          |     |          |          | remain.             | First,     | current   | benchmarks      |                 | such as         | MLPerf | pro-    |
| Benchmarking     |     | compute |           | overhead | in  | machine  | learning |                     |            |           |                 |                 |                 |        |         |
videempiricalperformancedatabutdonotoffergeneral-
| (ML) is | essential | for | understanding |     | and | optimizing |     | the             |     |            |     |            |     |         |         |
| ------- | --------- | --- | ------------- | --- | --- | ---------- | --- | --------------- | --- | ---------- | --- | ---------- | --- | ------- | ------- |
|         |           |     |               |     |     |            |     | ized predictive |     | techniques | for | estimating |     | latency | and en- |
performanceandefficiencyofMLsystemsacrossdiverse
|     |     |     |     |     |     |     |     | ergy consumption |     | across | classifiers. |     | This | limitation | hin- |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------------- | --- | ------ | ------------ | --- | ---- | ---------- | ---- |
tasks and deployment scenarios. Compute overhead en- ders the ability to anticipate performance bottlenecks or
compassesthecomputationalresourcesconsumedduring
2

energy demands in novel deployment scenarios, partic- the reliance on specific algorithmic properties limits the
ularly those involving Responsible AI (RAI) guardrails immediate applicability of these findings to non-neural
(Malliketal., 2023). Second, no universally accepted networkclassifiers.
metrics exist for comparing latency and energy con-
In contrast, Hauschild and Hellbrück
sumption across ML frameworks and hardware config-
(Hauschild&Hellbrück, 2022) analyzed convolu-
urations, making cross-platform evaluations inconsistent
tional neural networks (CNNs) deployed on Internet of
(Mattsonetal.,2020).
Things (IoT) edge devices, emphasizing the dependency
Additionally, the literature on benchmarking compute oflatencyandenergyconsumption onmodelcomplexity
overhead demonstrates a limited cross-comparison of andwirelessdatarates. Theresultsshowthatsimplifying
classification algorithms (e.g., SVM, k-Nearest Neigh- CNN architectures can yield substantial efficiency gains
bors, Random Forest, and Neural Networks) concerning in resource-constrained environments, underscoring the
their effects on latency and energy consumption. Most importance of tailoring models to deployment scenarios.
studies focus on single-model architectures or narrowly However, this approach is tightly coupled to CNNs and
compare a few model types (Cassalesetal., 2022). This does not address broader classification paradigms, such
narrow scope restricts generalizability, leaving gaps in asdecision treesorsupportvectormachines.
understanding how diverse classifiers perform in terms
While these studies offer valuable insights into optimiz-
of computational efficiency across real-world scenarios.
ing latency and energy efficiency, the work reflects a
Addressingtheselimitationsrequiresatheoretical frame-
broader trend in the literature of focusing on specific
work capable of predicting latency and energy consump-
modelsorhardwareconfigurations(Cassalesetal.,2022;
tion in a model-agnostic manner. Doing so also requires
Tschandetal., 2024). This limitation underscores the
anunderstandingoftheinherenttradeoffbetweenlatency
need for generalized predictive techniques that span di-
andenergyconsumptionduringinferenceonMLmodels.
verseclassification algorithms, bridgingthegapbetween
theoretical models and empirical benchmarks. Address-
ingthis challenge iscritical foradvancing thescalability
2.2 The Latency and Energy Consumption
andefficiencyofMLsystems,particularly astheintegra-
Tradeoff
tion ofResponsible AI(RAI)guardrails introduces addi-
tionalcomputational overhead.
The relationship between latency and energy consump-
tion during machine learning inference is complex, of-
ten involving trade-offs influenced by model architec-
2.3 RAI Controlsand Guardrails
ture, hardware, and optimization strategies. Generally,
reducing latency requires increased computational re-
Put simply, RAI ensures AI systems are developed and
sources, which can lead to higher energy consumption.
deployed in ways that are ethical (Floridietal., 2018;
Conversely, minimizing energy usage may involve tech-
Mittelstadt, Allo,Taddeo,Wachter, &Floridi, 2016).
niquesthatintroduce additional processing time,thereby
Ethical, in this context, includes fairness, transparency,
increasing latency. This inverse relationship is particu-
privacy, security, and trustworthiness as core principles.
larly evident inresource-constrained environments, such
The idea is an AI system can be considered responsible
as edge devices, where balancing performance and effi-
when the set of relevant principles are present. Here,
ciencyiscritical.
one should consider present as technical continuous
Recent studies have explored the trade-off between monitoring.
latency and energy consumption during machine
To that end, ethical principles have experienced rapid
learning inference, with varying levels of generaliz-
theoretical and practical expansion. In a short time, re-
ability across classification algorithms. For instance,
searchershavedevelopedrobusttechnicalframeworksto
researchers examining multilayer perceptrons (MLPs)
measure and evaluate these principles. Two prominent
demonstrated that hyperparameter optimization could
examplesaretheMicrosoftResponsibleToolboxandthe
significantly reduce energy consumption during infer-
IBM AI 360 Toolkit. Yet, as much as AI practitioners
ence with minimal impact on classification accuracy
canusetheseframeworkstoevaluatemodels,researchers
(Desislavov, Martínez-Plumed, &Hernández-Orallo,
(Radclyffe, Ribeiro,&Wortham, 2023; Luetal., 2024)
2021). By tuning model complexity, such as reducing
suggestRAIisoneofthemostcriticalchallengespresent
hidden layers or using lower-precision arithmetic, the
inAIandML.
study highlights strategies that, while tested on MLPs,
may generalize to other model architectures. However, Culturally, the rapid expansion has been motivated
3

by demonstrable harm arising from a lack of RAI. 3 Method
Such examples include discriminatory sentenc-
ing and parole decisions in the US justice system
This work was motivated by a single research question:
(Angwin,Larson,Mattu,&Kirchner, 2022) as well as
Whatvariables,coefficients,andpropositionaloperations
Amazon’s recruitment tool (Dastin, 2022). Increasing
are necessary for a model-agnostic equation to be ca-
legal and regulatory requirements such as the US Presi-
pable of predicting latency and energy consumption in
dent’sExecutiveOrderandtheEU’sAIAct(Wörsdörfer,
binary classification models during inference with RAI
2023)arealsodrivingRAIresearch.
guardrails? Toanswer thisquestion, thestudy employed
Meanwhile, the literature (Khanetal., 2022;
Theory Construction Methodology (TCM) to derive the
Alzubaidietal., 2023) has coalesced around five
model-agnostic equation.
specific RAI principles: explainability, bias or fairness,
TCM is a structured approach to developing theoretical
robustness or safety, transparency or interpretability,
frameworks by defining key variables, establishing rela-
and privacy. Additional principles, such as explicability
tionships, and formalizing them into mathematical mod-
(Prem, 2023) and accountability (Liuetal., 2022), have
els (Dubin, 1978). While TCM has been widely applied
been studied but ultimately fall within the scope of one
in theoretical modeling, its application to derive predic-
or more of the five specific principles. Consequently,
tiveequations forlatencyandenergy consumption inthe
industry (IBM, Microsoft, US Department of Defense)
context of RAI guardrails represents a novel adaptation
has settled on explainability, bias, robustness, inter-
of this methodology. This approach is particularly well-
pretability, and privacy for practical implementation
suited to the research problem because the abstraction
of RAI. Trustworthiness tends to be discussed as an
and generalization required for a predictive equation ap-
emergent principle only present when the complete set
plicable across diverse classifiers necessitates a theoreti-
ofRAIprinciples havesoundimplementations.
calframework(Kaplan&Haenlein,2019).
On that note, the RAI principles can be implemented
The TCM process began with identifying core variables
either as a control or guardrail. On the one hand,
influencing latency and energy consumption during in-
controls are techniques applied during the training
ference. These variables were selected based on prior
phase of a model to ensure that the AI system be-
empirical findings and theoretical reasoning, ensuring
haves ethically and responsibly (Mitchelletal., 2019;
relevance to diverse classification contexts and com-
Mehrabi,Morstatter, Saxena,Lerman,&Galstyan,
putational scenarios. For example, the computational
2021). On the other hand, guardrails are measures
overhead introduced by explainability and interpretabil-
implemented in deployed models to assess the run-
ity guardrails, such as those implemented using SHAP
time behavior of models (Raji&Buolamwini, 2019;
(Lundberg, 2017) or LIME (Ribeiro,Singh,&Guestrin,
Varshney&Alemzadeh, 2017). The aim is to ensure
2016), was identified as a critical variable. This as-
that the AI system continues to operate responsibly and
sumption is supported by computational complexity the-
ethically throughout the life of the system deployment
ory, which posits that even linear increases in input size
(Holstein, WortmanVaughan,DauméIII,Dudik,&Wallach,
(O(n))resultinproportional growthincomputational de-
2019).
mand. In the context of RAI guardrails, the overhead
Despite the stated need for RAI and the availability of
arises from explainability mechanisms that augment in-
broad technical frameworks, the computational costs of
ference operations with additional interpretive computa-
implementing these guardrails are often excluded from
tions.
benchmarking studies. For example, the additional
Relationships among these variables—such as the in-
overhead introduced by explainability mechanisms dur-
verse correlation between latency and energy con-
ing inference remains an under explored area (Lietal.,
sumption—are then proposed based on prior research
2024). Without incorporating RAI considerations, exist-
(Henderson etal., 2020; Malliketal., 2023). For in-
ingbenchmarksriskbecomingoutdatedorincompleteas
stance,studiessuchasthosebyHauschildandHellbrück
the adoption of RAI increases. Moreover, and perhaps
(Hauschild&Hellbrück,2022)demonstratehowcompu-
mostimportantly, the fieldisbereft ofoperationally vali-
tational trade-offs between latency andenergy efficiency
dated knowledge of how runtime RAImay be more of a
areparticularly evidentinedgecomputing environments.
poisonthanacure.
Coefficients are incorporated to represent adjustable fac-
tors, including the type of classifier and specific deploy-
ment conditions. These variables and coefficients are
connected through mathematical operations, such as ad-
4

ditive and multiplicative terms, to capture their interac- Data type is represented as a categorical variable with
tions(Cassalesetal.,2022). tabulardataencoded as0,textas1,andimagedataas2.
Finally, the equation is formalized to ensure generaliz- RAI guardrails (G) encompass five principles: explain-
ability, interpretability, and scalability across classifiers ability,fairness,interpretability,safety,andprivacy. Each
suchasSVM,k-NearestNeighbors, RandomForest,and principle is modeled as a binary state ([0,1]), which,
NeuralNetworks. Thistheoreticalframeworkestablishes when active, can include a continuous intensity score.
a foundation for subsequent empirical validation, where For example, explainability (expl) could take a value of
its predictive accuracy will be tested against experimen- 0.7,representing partialfeature-level explanations cover-
taldataindiverseoperational settings. ingthetop70%offeatures.
4 Discussion 4.3 Prediction Equations
The general equation was expanded into two prediction
The development of a model-agnostic equation for pre-
equations,capturinglatency(L)andenergyconsumption
dictinglatencyandenergyconsumption beganwithiden-
(E). These equations model inference performance as a
tifying foundational variables (Table 1). These variables
function of algorithm type, dataset characteristics, and
are organized into three sets—classification algorithm,
thecomputational costofRAIguardrails.
RAI guardrail, and dataset characteristics—all of which
serve as inputs to a prediction function f. The outputs The latency equation (2) incorporates logarithmic scal-
ofthefunction, latency (L)and energy consumption (E), ing for dataset size, capturing the diminishing impact of
arerepresented collectively asO. largerdatasetsonprediction time:
4.1 General Equation
L=α+β A+β log(n)+γ p+δ t+∑φ g +ε (2)
A D D D G,i i
i
A general equation (1) was constructed to unify the di-
mensionsoflatencyandenergyconsumptionintoacohe-
Theenergy consumption equation (3)applies linear scal-
siveanalytical framework:
ing for dataset size to account for cumulative resource
demandsduringinference:
O= f(A,D,G) (1)
This equation serves two purposes. First, it provides E =α ′ +β A+β ′ n+γ p+δ t+∑φ ′ g +ε ′ (3)
A D D D G,i i
a unified framework to compare inference performance i
across binary classifiers. Second, it establishes a foun-
dation for synthesizing disparate dimensions of model Bothequationsusecoefficientstomodelthecontribution
performance intoapredictive tool,enabling cross-model ofeachvariable, assummarizedinTable2.
comparisons,performanceprediction,andtheintegration
ofRAIguardrails intosystemdesign.
4.4 Noveltyand Practical Implications
4.2 Expanded Variables These equations provide a novel approach to predicting
inference performance across diverse binary classifiers.
Eachvariablesetinthegeneralequationisexpandedinto Unlike prior studies, which focus on empirical bench-
measurable elements. Algorithm type (A) contains four marking or specific algorithms (Cassalesetal., 2022;
discrete elements: support vector machines (SVM), k- Malliketal., 2023), this framework offers generalizabil-
nearest neighbors (k-NN),random forests(RF),andneu- ity and scalability. Furthermore, it uniquely integrates
ral networks (NN). Categorical encoding is used to rep- the computational cost of RAI guardrails, addressing a
resentbinaryclassifiersasa∈SVM,k-NN,RF,NN,with criticalgapintheliterature(Lietal.,2024;Ribeiroetal.,
A encoded as 1,0,0,0 to predict L or E for SVM,for in- 2016).
stance.
Future empirical validation willuse benchmarks such as
Dataset characteristics (D) include the number of sam- MLPerf (Mattsonetal., 2020) to evaluate the predictive
ples (n), feature dimensionality (p), and data type (t). accuracy of these models. Practical applications include
5

|     |     |     |     | Table1: | Foundational |     | variablesinamodel-agnostic |     |     |     | equa- |     |     |     |     |
| --- | --- | --- | --- | ------- | ------------ | --- | -------------------------- | --- | --- | --- | ----- | --- | --- | --- | --- |
tion
|     |     |     |                   | VariableSet                   |                |                |          |                |           | Symbol    |          |     |     |     |     |
| --- | --- | --- | ----------------- | ----------------------------- | -------------- | -------------- | -------- | -------------- | --------- | --------- | -------- | --- | --- | --- | --- |
|     |     |     |                   | Classification                |                | algorithm      |          |                |           | A         |          |     |     |     |     |
|     |     |     |                   | RAIguardrail                  |                |                |          |                |           | G         |          |     |     |     |     |
|     |     |     |                   | Datasetcharacteristics        |                |                |          |                |           | D         |          |     |     |     |     |
|     |     |     |                   | Outputmetric                  |                |                |          |                |           | O         |          |     |     |     |     |
|     |     |     |                   | Note:                         | The prediction |                | function | f is undefined |           | in        | the gen- |     |     |     |     |
|     |     |     |                   | eral equation.                |                | The formalized |          | prediction     | equations |           | for L    |     |     |     |     |
|     |     |     |                   | andE                          | areoutlined    | inTable2.      |          |                |           |           |          |     |     |     |     |
|     |     |     | Table2:           | Coefficientsformodel-agnostic |                |                |          | prediction     |           | equations |          |     |     |     |     |
|     |     |     | CoefficientSet    |                               |                |                |          |                | Symbol    |           | Variable |     |     |     |     |
|     |     |     | Baselineinference |                               |                |                |          |                | α,α       | ′         |          | O   |     |     |     |
′
|     |     |     | Errortermsforvariability1 |     |     |     |     |     | ε,ε |     |     | -   |     |     |     |
| --- | --- | --- | ------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
′
|     |     |     | Algorithm | type |     |     |     |     | β   | A ,β |     | A   |     |     |     |
| --- | --- | --- | --------- | ---- | --- | --- | --- | --- | --- | ---- | --- | --- | --- | --- | --- |
A
|     |     |     | Datasetsize |     |     |     |     |     | β   | ,β ′ |     | D   |     |     |     |
| --- | --- | --- | ----------- | --- | --- | --- | --- | --- | --- | ---- | --- | --- | --- | --- | --- |
|     |     |     |             |     |     |     |     |     |     | D D  |     | n   |     |     |     |
′
|     |     |     | Featuredimensionality |     |     |     |     |     | γ   | ,γ  |     | D   |     |     |     |
| --- | --- | --- | --------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|     |     |     |                       |     |     |     |     |     | D   | D   |     | p   |     |     |     |
′
|     |     |     | Datasettype |     |     |     |     |     | δ D | ,δ  |     | D t |     |     |     |
| --- | --- | --- | ----------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
D
|     |     |     | Guardrails |     |     |     |     |     | φ   | ,φ ′ |     | G   |     |     |     |
| --- | --- | --- | ---------- | --- | --- | --- | --- | --- | --- | ---- | --- | --- | --- | --- | --- |
G,i G,i
1
|     |     |     | Note: | Errortermshandleunmodeled |     |     |     | variability |     | duringinference. |     |     |     |     |     |
| --- | --- | --- | ----- | ------------------------- | --- | --- | --- | ----------- | --- | ---------------- | --- | --- | --- | --- | --- |
optimizing ML systems for edge devices, estimating re- overhead of RAI guardrails into a cohesive analytical
source demands for RAI-integrated classifiers, and en- tool. Unlike previous studies that focus on specific clas-
abling informed trade-offs between latency, energy con- sifiers or empirical benchmarks, this work offers gener-
sumption, andethicalrobustness. alizability and scalability, bridging theoretical modeling
|     |     |     |     |     |     |     |     | withpractical |              | performance |                | evaluation. |     |                 |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------- | ------------ | ----------- | -------------- | ----------- | --- | --------------- | --- |
|     |     |     |     |     |     |     |     | Thebroader    | significance |             | ofthisresearch |             |     | liesinitsimpli- |     |
5 Conclusion cationsfordesigninganddeployingefficient,responsible
|                |               |          |              |           |                  |              |         | ML systems.        |                | For researchers, |                      | the              | predictive |               | equations    |
| -------------- | ------------- | -------- | ------------ | --------- | ---------------- | ------------ | ------- | ------------------ | -------------- | ---------------- | -------------------- | ---------------- | ---------- | ------------- | ------------ |
|                |               |          |              |           |                  |              |         | provide            | a foundational |                  | tool                 | for benchmarking |            |               | and opti-    |
| AI broadly,    | and           | ML       | in specific, | continues |                  | to transform |         |                    |                |                  |                      |                  |            |               |              |
|                |               |          |              |           |                  |              |         | mizing             | inference      | performance      |                      | across           | diverse    |               | classifiers. |
| science        | and industry. |          | Yet,         | AI and    | ML scalability   |              | and     |                    |                |                  |                      |                  |            |               |              |
|                |               |          |              |           |                  |              |         | For practitioners, |                | they             | enable               | informed         |            | decisions     | about        |
| accessibility  | are           | often    | constrained  |           | by compute       | overhead.    |         |                    |                |                  |                      |                  |            |               |              |
|                |               |          |              |           |                  |              |         | deploying          | models         | in               | resource-constrained |                  |            | environments, |              |
| The literature |               | suggests | such         | issues    | are particularly |              | no-     |                    |                |                  |                      |                  |            |               |              |
|                |               |          |              |           |                  |              |         | such as            | edge           | or mobile        | devices,             | while            |            | maintaining   | ethi-        |
| table during   | inference.    |          | Challenges   |           | such as          | the          | lack of |                    |                |                  |                      |                  |            |               |              |
|                |               |          |              |           |                  |              |         | cal robustness.    |                | This             | work                 | also aligns      | with       | the           | growing      |
generalized predictive techniques for latency and energy need for sustainable AI, offering a pathway to balance
| consumption, |            | limited | cross-comparison |     | of            | classification  |        |                |     |                                      |                |     |               |     |         |
| ------------ | ---------- | ------- | ---------------- | --- | ------------- | --------------- | ------ | -------------- | --- | ------------------------------------ | -------------- | --- | ------------- | --- | ------- |
|              |            |         |                  |     |               |                 |        | computational  |     | efficiencywithethicalconsiderations. |                |     |               |     |         |
| algorithms,  | and        | the     | unquantified     |     | computational |                 | impact |                |     |                                      |                |     |               |     |         |
|              |            |         |                  |     |               |                 |        | In conclusion, |     | this                                 | study provides |     | a theoretical |     | founda- |
| of RAI       | guardrails | have    | left critical    |     | gaps in       | the literature. |        |                |     |                                      |                |     |               |     |         |
This study aimed to address these gaps by developing tion for understanding and predicting inference perfor-
|                  |     |          |         |     |               |     |         | manceinMLsystems. |     |     | Byaddressing |     | criticalgapsinthe |     |     |
| ---------------- | --- | -------- | ------- | --- | ------------- | --- | ------- | ----------------- | --- | --- | ------------ | --- | ----------------- | --- | --- |
| a model-agnostic |     | equation | capable |     | of predicting |     | latency |                   |     |     |              |     |                   |     |     |
literature,itlaysthegroundworkforfutureadvancements
| and energy      | consumption   |                    | in        | binary | classification |           | models |                   |     |                          |     |             |     |            |     |
| --------------- | ------------- | ------------------ | --------- | ------ | -------------- | --------- | ------ | ----------------- | --- | ------------------------ | --- | ----------- | --- | ---------- | --- |
|                 |               |                    |           |        |                |           |        | in model-agnostic |     | performance              |     | prediction, |     | enabling   | the |
| duringinference |               | withRAIguardrails. |           |        |                |           |        |                   |     |                          |     |             |     |            |     |
|                 |               |                    |           |        |                |           |        | nextgeneration    |     | ofscalableandresponsible |     |             |     | AIsystems. |     |
| The key         | contributions |                    | of this   | work   | include        | a         | model- |                   |     |                          |     |             |     |            |     |
| agnostic        | theoretical   |                    | framework | for    | analyzing      | inference |        |                   |     |                          |     |             |     |            |     |
performanceandtwopredictiveequationsforlatencyand
| energyconsumption. |     |         | Thesemodelssynthesizealgorithm |     |                     |     |     |     |     |     |     |     |     |     |     |
| ------------------ | --- | ------- | ------------------------------ | --- | ------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| characteristics,   |     | dataset | properties,                    |     | andthecomputational |     |     |     |     |     |     |     |     |     |     |
6

5.1 Limitations ity of the equations to different input variables, such as
|                       |           |          |         |                  |     |             | dataset            | characteristics |     |                  | and RAI      | guardrails, |            | to refine | the       |
| --------------------- | --------- | -------- | ------- | ---------------- | --- | ----------- | ------------------ | --------------- | --- | ---------------- | ------------ | ----------- | ---------- | --------- | --------- |
| While this            | study     | provides |         | a foundational   |     | framework   | for modelsfurther. |                 |     |                  |              |             |            |           |           |
| predicting            | inference |          | latency | and energy       |     | consumption | in                 |                 |     |                  |              |             |            |           |           |
|                       |           |          |         |                  |     |             | Furthermore,       |                 | the | generalizability |              | of          | the L      | and       | E predic- |
| binary classification |           |          | models, | five limitations |     | should      | be                 |                 |     |                  |              |             |            |           |           |
|                       |           |          |         |                  |     |             | tive               | equations       |     | may be           | investigated |             | by varying |           | the set A |
acknowledged.
|     |     |     |     |     |     |     | across | a   | variety | of AI | subfields. | Of  | particular |     | interest, |
| --- | --- | --- | --- | --- | --- | --- | ------ | --- | ------- | ----- | ---------- | --- | ---------- | --- | --------- |
First,theprediction equations relyonassumptions about given the mainstream perception of AI, might be the ap-
|          |                |     |      |                |     |         | plication |     | of the | framework |     | to Large | Language |     | Models |
| -------- | -------------- | --- | ---- | -------------- | --- | ------- | --------- | --- | ------ | --------- | --- | -------- | -------- | --- | ------ |
| variable | relationships, |     | such | as logarithmic |     | scaling | for       |     |        |           |     |          |          |     |        |
dataset size in latency prediction and linear scaling (LLMs), where inference latency and energy efficiency
for energy consumption. While these assumptions are arecriticalduetotheirsizeandcomplexity. Additionally,
groundedinpriorresearchandtheoreticalreasoning,they frontier research areas such as neuro-symbolic AI repre-
|         |       |         |            |              |     |     | sent     | a compelling |     | opportunity |     | for | extending | the | frame- |
| ------- | ----- | ------- | ---------- | ------------ | --- | --- | -------- | ------------ | --- | ----------- | --- | --- | --------- | --- | ------ |
| may not | fully | capture | real-world | complexities |     | in  | all sce- |              |     |             |     |     |           |     |        |
narios. Additionalresearch, moreespecially practicalex- worktohybrid models that combine symbolic reasoning
perimentationmayrevealtowhatextentsuchalimitation withdeeplearning. Theseextensions couldprovidevalu-
|     |     |     |     |     |     |     | able | insights | into | the computational |     |     | trade-offs |     | in emerg- |
| --- | --- | --- | --- | --- | --- | --- | ---- | -------- | ---- | ----------------- | --- | --- | ---------- | --- | --------- |
isaddressable.
ingAIparadigms.
| Second, | thefocus | onbinary |     | classification |     | tasksexcludes |     |     |     |     |     |     |     |     |     |
| ------- | -------- | -------- | --- | -------------- | --- | ------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
multi-class classification and other ML tasks, such as Another avenue for future work involves refining the
regression or clustering, which may involve different representation of RAI guardrails. Current binary and
|               |     |             |     |               |     |           | intensity-scale |     |     | representations |     | may | oversimplify |     | the |
| ------------- | --- | ----------- | --- | ------------- | --- | --------- | --------------- | --- | --- | --------------- | --- | --- | ------------ | --- | --- |
| computational |     | trade-offs. |     | Along similar |     | thinking, | this            |     |     |                 |     |     |              |     |     |
work does not account for potential innovations becom- computational demands of advanced guardrails, such as
ingavailable inthefuture. differentialprivacy,adversarialrobustness,ornuancedin-
|                   |                |           |                 |                 |         |              | terpretability                 |     | mechanisms. |        | Developing    |     | more              | granular | or    |
| ----------------- | -------------- | --------- | --------------- | --------------- | ------- | ------------ | ------------------------------ | --- | ----------- | ------ | ------------- | --- | ----------------- | -------- | ----- |
| Third, the        | representation |           | of              | RAI guardrails, |         | while        | prac-                          |     |             |        |               |     |                   |          |       |
|                   |                |           |                 |                 |         |              | context-aware                  |     |             | models | for guardrail |     | contributions     |          | could |
| tical, simplifies |                | potential |                 | computational   |         | impact.      | Com-                           |     |             |        |               |     |                   |          |       |
|                   |                |           |                 |                 |         |              | enhancetheframework’sprecision |     |             |        |               |     | andapplicability. |          |       |
| plex guardrails,  |                | such      | as differential |                 | privacy | or trustwor- |                                |     |             |        |               |     |                   |          |       |
thiness mechanisms, may require more nuanced model- Finally, while this study focused on binary classifica-
ingtofullycaptureresource demands. tion tasks, future research could extend the framework
|                                                    |                 |                  |                                 |              |                     |         | to                  | multi-class | classification |             | and   | other             | ML  | tasks,     | such as |
| -------------------------------------------------- | --------------- | ---------------- | ------------------------------- | ------------ | ------------------- | ------- | ------------------- | ----------- | -------------- | ----------- | ----- | ----------------- | --- | ---------- | ------- |
| Fourth,theframeworkabstractsdatasetcharacteristics |                 |                  |                                 |              |                     |         | to                  |             |                |             |       |                   |     |            |         |
|                                                    |                 |                  |                                 |              |                     |         | regression          |             | or             | clustering. | These | extensions        |     | would      | test    |
| size, feature                                      | dimensionality, |                  |                                 | and data     | type.               | Other   | impor-              |             |                |             |       |                   |     |            |         |
|                                                    |                 |                  |                                 |              |                     |         | the                 | framework’s |                | scalability |       | and adaptability, |     | addressing |         |
| tant factors,                                      | such            | as               | data quality                    | or           | sparsity,           | are     | not in-             |             |                |             |       |                   |     |            |         |
|                                                    |                 |                  |                                 |              |                     |         | broaderapplications |             |                | inAI.       |       |                   |     |            |         |
| cludedandcouldaffectpredictions                    |                 |                  |                                 |              | inspecificcontexts. |         |                     |             |                |             |       |                   |     |            |         |
| Finally,                                           | this study      | presents         |                                 | theoretical  | equations           | without |                     |             |                |             |       |                   |     |            |         |
| empiricalvalidation.                               |                 |                  | Whilethemodelsarerigorous,their |              |                     |         |                     |             |                |             |       |                   |     |            |         |
| accuracy                                           | and             | generalizability |                                 | remain       | untested.           |         | Future References   |             |                |             |       |                   |     |            |         |
| work will                                          | involve         | validating       |                                 | these        | equations           | with    | exper-              |             |                |             |       |                   |     |            |         |
| imental                                            | data across     |                  | diverse                         | classifiers, | datasets,           |         | and de-             |             |                |             |       |                   |     |            |         |
Alzubaidi,L.,Al-Sabaawi,A.,Bai,J.,Dukhan,A.,Alke-
| ployment | environments |     | to  | ensure their | practical | applica- |     |       |     |               |     |         |        |         |     |
| -------- | ------------ | --- | --- | ------------ | --------- | -------- | --- | ----- | --- | ------------- | --- | ------- | ------ | ------- | --- |
|          |              |     |     |              |           |          |     | nani, | A.  | H., Al-Asadi, |     | A., ... | others | (2023). | To- |
bility.
|                               |         |       |     |                 |       |     |           | wards                        | risk-free  |                       | trustworthy      |               | artificial      | intelligence: |         |
| ----------------------------- | ------- | ----- | --- | --------------- | ----- | --- | --------- | ---------------------------- | ---------- | --------------------- | ---------------- | ------------- | --------------- | ------------- | ------- |
|                               |         |       |     |                 |       |     |           | Significanceandrequirements. |            |                       |                  |               | International   |               | Jour-   |
|                               |         |       |     |                 |       |     |           | nalofIntelligent             |            |                       | Systems,2023(1), |               |                 | 4459198.      |         |
| 5.2 Future                    |         | work  |     |                 |       |     |           |                              |            |                       |                  |               |                 |               |         |
|                               |         |       |     |                 |       |     | Angwin,   |                              | J.,Larson, | J.,Mattu,             |                  | S.,&Kirchner, |                 | L.            | (2022). |
|                               |         |       |     |                 |       |     |           | Machine                      |            | bias. In              | Ethics           | of data       | and             | analytics     | (pp.    |
| There are                     | several | areas | for | future work     | based | on  | the the-  |                              |            |                       |                  |               |                 |               |         |
|                               |         |       |     |                 |       |     |           | 254–264).                    |            | AuerbachPublications. |                  |               |                 |               |         |
| oreticalframeworkdemonstrated |         |       |     | inthisresearch. |       |     |           |                              |            |                       |                  |               |                 |               |         |
|                               |         |       |     |                 |       |     | Cassales, |                              | G., Gomes, | H.M.,                 |                  | Bifet,        | A., Pfahringer, |               | B.,&    |
Foremost, experimentation is necessary to validate and Senger, H. (2022). Balancing performance and
quantify the coefficients in the latency (L) and energy energy consumption of bagging ensembles for the
consumption (E)prediction equations. Empiricalstudies classification of data streams in edge computing.
usingbenchmark datasets andplatformssuchasMLPerf IEEE Transactions on Network and Service Man-
willhelpcalibrate these coefficients, ensuring theiraccu- agement,20(3),3038–3054.
racy across diverse classifiers and deployment environ- Dastin, J. (2022). Amazon scraps secret ai recruiting
ments. Validationeffortsshouldalsoexplorethesensitiv- tool that showed bias against women. In Ethics of
7

dataandanalytics(pp.296–299). AuerbachPubli- Lundberg, S. (2017). A unified approach to in-
cations. terpreting model predictions. arXiv preprint
Desislavov, R., Martínez-Plumed, F., & Hernández- arXiv:1705.07874.
Orallo, J. (2021). Compute and energy con- Mallik, A., Wang, H., Xie, J., Chen, D., & Han, K.
sumption trends in deep learning inference. arXiv (2023). Epam: A predictive energy model for mo-
preprintarXiv:2109.05472. bile ai. In Icc 2023-ieee international conference
Dubin,R. (1978). Theorybuilding. TheFreePress. oncommunications (pp.954–959).
Elesedy, H., Esperança, P. M., Oprea, S. V., & Ozay, M. Mattson, P., Reddi, V. J., Cheng, C., Coleman, C., Di-
(2024). Lora-guard: Parameter-efficient guardrail amos, G., Kanter, D., ... others (2020). Mlperf:
adaptation for content moderation of large lan- Anindustrystandardbenchmarksuiteformachine
guagemodels. arXivpreprintarXiv:2407.02987. learningperformance. IEEEMicro,40(2), 8–16.
Floridi, L., Cowls, J., Beltrametti, M., Chatila, R., Mehrabi, N., Morstatter, F., Saxena, N., Lerman, K., &
Chazerand, P., Dignum, V., ... others (2018). Galstyan, A. (2021). A survey on bias and fair-
Ai4people—anethicalframeworkforagoodaiso- nessinmachinelearning. ACMcomputingsurveys
ciety: opportunities, risks, principles, and recom- (CSUR),54(6),1–35.
mendations. Mindsandmachines,28,689–707. Mitchell,M.,Wu,S.,Zaldivar,A.,Barnes,P.,Vasserman,
Hauschild, S.,& Hellbrück, H. (2022). Latency and en- L., Hutchinson, B., ... Gebru, T. (2019). Model
ergyconsumption ofconvolutional neuralnetwork cards for model reporting. In Proceedings of the
models from iot edge perspective. In Global iot conference on fairness, accountability, and trans-
summit(pp.385–396). Springer. parency(pp.220–229).
Henderson, P., Hu, J., Romoff, J., Brunskill, E., Juraf- Mittelstadt, B. D., Allo, P., Taddeo, M., Wachter, S.,
sky, D.,& Pineau, J. (2020). Towards the system- & Floridi, L. (2016). The ethics of algorithms:
atic reporting of the energy and carbon footprints Mapping the debate. Big Data & Society, 3(2),
ofmachinelearning. JournalofMachineLearning 2053951716679679.
Research,21(248), 1–43. Prem, E. (2023). From ethical ai frameworks to tools:
Holstein, K., Wortman Vaughan, J., Daumé III, H., a review of approaches. AI and Ethics, 3(3), 699–
Dudik, M.,&Wallach, H. (2019). Improving fair- 716.
ness in machine learning systems: What do indus- Radclyffe, C., Ribeiro, M., & Wortham, R. H. (2023).
trypractitioners need? InProceedings ofthe2019 Theassessmentlistfortrustworthyartificialintelli-
chiconference onhumanfactors incomputing sys- gence: A review and recommendations. Frontiers
tems(pp.1–16). inartificial intelligence, 6,1020592.
Kaplan, A., & Haenlein, M. (2019). Siri, siri, in my Raji, I. D., & Buolamwini, J. (2019). Actionable audit-
hand: Who’s the fairest in the land? on the inter- ing: Investigating the impact of publicly naming
pretations, illustrations, and implications of artifi- biased performance results of commercial ai prod-
cialintelligence. Businesshorizons,62(1),15–25. ucts. In Proceedings of the 2019 aaai/acm confer-
Khan, A.A.,Badshah, S.,Liang, P.,Waseem, M., Khan, enceonai,ethics,andsociety(pp.429–435).
B., Ahmad, A., ... Akbar, M. A. (2022). Ethics Reddi, V. J., Cheng, C., Kanter, D., Mattson, P.,
of ai: A systematic literature review of principles Schmuelling, G., Wu, C.-J., ... others (2020).
andchallenges. InProceedingsofthe26thinterna- Mlperf inference benchmark. In 2020 acm/ieee
tional conference onevaluation andassessment in 47thannualinternational symposiumoncomputer
softwareengineering (pp.383–392). architecture (isca)(pp.446–459).
Li, P., Liu, Y., Yang, J., & Ren, S. (2024). Towards Ribeiro, M. T., Singh, S., & Guestrin, C. (2016). "
socially andenvironmentally responsible ai. arXiv whyshoulditrustyou?"explainingthepredictions
preprintarXiv:2407.05176. of any classifier. In Proceedings of the 22nd acm
Liu, H., Wang, Y., Fan, W., Liu, X., Li, Y., Jain, S., ... sigkdd international conference on knowledge dis-
Tang, J. (2022). Trustworthy ai: A computational coveryanddatamining(pp.1135–1144).
perspective. ACM Transactions on Intelligent Sys- Strubell, E., Ganesh, A., & McCallum, A. (2020). En-
temsandTechnology, 14(1), 1–59. ergy and policy considerations for modern deep
Lu, Q., Zhu, L., Xu, X., Whittle, J., Zowghi, D., & learning research. In Proceedings of the aaai
Jacquet, A. (2024). Responsible ai pattern cata- conference on artificial intelligence (Vol. 34, pp.
logue: A collection of best practices for ai gover- 13693–13696).
nance and engineering. ACM Computing Surveys, Tschand, A., Rajan, A. T. R., Idgunji, S., Ghosh, A.,
56(7),1–35. Holleman,J.,Kiraly,C.,... others (2024). Mlperf
8

power: Benchmarking the energy efficiency of
machine learning systems from microwatts to
megawatts for sustainable ai. arXiv preprint
arXiv:2410.12032.
Varshney,K.R.,&Alemzadeh,H. (2017). Onthesafety
of machine learning: Cyber-physical systems, de-
cision sciences, and data products. Big data, 5(3),
246–255.
Wörsdörfer, M. (2023). The eu’s artificial intelligence
act: an ordoliberal assessment. AI and Ethics, 1–
16.
9