---
conversion_metadata:
  converted_at: "2026-07-21T13:38:42Z"
  converter_tool: "markitdown"
  converter_version: "0.1.6"
  source_pdf: "Jiang et al.pdf"
  source_pdf_sha256: "cd1e207e632e3858aa7c4968f828de059863f5b4cbb832fafe619ce70ae5091b"
  page_count: 25
  markdown_char_count: 239991
---

<!-- PAGE-AWARE EXTRACTION (via pdfminer.six) -->

<!-- PAGE 1 -->

Received 30 January 2026, accepted 1 March 2026, date of publication 5 March 2026, date of current version 17 March 2026.

Digital Object Identifier 10.1109/ACCESS.2026.3670857

A Dynamic Framework for Causal User Profiling
and Treatment Segmentation via Uplift Modeling
in Internet Lending

JIANQING JIANG 1, NOR ASILAH WATI ABDUL HAMID 1,2, (Senior Member, IEEE),
NG KENG YAP 1,2, (Senior Member, IEEE), AND CHOO WEI CHONG3
1Institute for Mathematical Research (INSPEM), Universiti Putra Malaysia (UPM), Serdang, Selangor 43400, Malaysia
2Faculty of Computer Science and Information Technology, Universiti Putra Malaysia (UPM), Serdang, Selangor 43400, Malaysia
3School of Business and Economics (SBE), Universiti Putra Malaysia (UPM), Serdang, Selangor 43400, Malaysia

Corresponding author: Choo Wei Chong (wcchoo@upm.edu.my)

ABSTRACT The growth of internet lending has created a need for decision frameworks based on
models that are both personalized and causally interpretable. Conventional uplift models detect treatment
responsiveness without recognizing user heterogeneity, the temporal consistency of user behavior, or the
upstream design choices that carry important causal implications. This paper proposes an integrated and
reproducible Causal User Profiling (CUP) framework that combines causal inference, uplift modeling,
and response-based segmentation within a single pipeline. CUP realizes treatment-effect heterogeneity
through a four-type response taxonomy (Persuadable, Sure Thing, Lost Cause, Do-Not-Disturb) and embeds
it in a multi-stage pipeline involving hybrid feature selection (Information Value (IV), Causal Forest
importance, Population Stability Index (PSI) stability, and Stepwise refinement), stratified clustering with
a ‘‘C2 replacement strategy,’’ and meta-learning via both the X-Learner and the Doubly Robust (DR)
Learner using Logistic Regression (LR). A component-wise ablation analysis finds that feature selection
increases AUUC by 25–30%, C2 clustering by 10–12%, and the DR-Learner + LR by another 5–8%.
Overall, the integrated CUP framework yields 45–50% higher AUUC than the baseline (‘‘all features +
no clustering + standard learner’’) while retaining behaviorally coherent and temporally stable insights.
Methodologically, we provide: 1) an end-to-end causal user profiling framework that interoperates profiling,
causal estimation, clustering, and uplift evaluation; 2) a behaviorally and causally consistent response
segmentation mechanism grounded in the potential-outcomes model; and 3) a reproducible experimental
design that quantifies pipeline-level uplift gains through systematic ablation. Applied to large-scale
internet-lending data, CUP reveals opportunities for treatment-aware personalization, enabling financial
institutions to target Persuadables, support Sure Things, and avoid disturbing Do-Not-Disturbs based on
causal evidence.

INDEX TERMS C2 clustering strategy, causal precision, causal user profiling, decision support systems,
DR-learner, feature selection, heterogeneous treatment effects, internet lending, meta-learners, response
segmentation, uplift modeling, X-learner.

I. INTRODUCTION
The rapid evolution of digital platforms has heightened
the importance of personalization and targeting, shifting
attention toward core aspects of data-driven decision-making.

The associate editor coordinating the review of this manuscript and

approving it for publication was Diego Bellan

.

In this tussle, user profiling [1], [2], [3]—the process
of acquiring, analyzing, and organizing multi-dimensional
user data to create static and/or dynamic user profiles or
models of the user’s behaviors,
tastes, preferences, and
other demographics—is foundational to data-driven systems.
Profiling helps design interpretable user representations
that drive downstream applications such as recommender

VOLUME 14, 2026

2026 The Authors. This work is licensed under a Creative Commons Attribution 4.0 License.
For more information, see https://creativecommons.org/licenses/by/4.0/

40147

---

<!-- PAGE 2 -->

J. Jiang et al.: Dynamic Framework for CUP and Treatment Segmentation via Uplift Modeling

systems, targeted marketing, and risk assessment [4], [5] but
conventional profiling pipelines are observational in nature,
concerned with who the user is instead of how the user
would react if acted upon [6], and almost entirely ignore
causation [7], relegating them to use-case-specific opaque
models components [8].

During the same period, a shift in the way the field thought
about the phrase ‘‘learning from data’’ influenced how data—
used for the targeted deployment of algorithms—came to
be conceptualized. A widely used formulation characterizes
learning from data as the process in which ‘‘a program is said
to learn from experience E with respect to some class of tasks
T and performance measure P if its performance at tasks in
T, as measured by P, improves with experience E.’’ While
predictive power in analytics is impressive, machine learning
(ML) algorithms are limited by the fact that making decisions
can change the very distribution of the outcomes one wishes
to predict [9]. In many situations, prediction is insufficient,
and one needs to understand the causal structure of the world
because interventions change the distribution of data [10].
It is this limitation that led to additional research on causal
inference, defined as ‘‘the study of the relationship between
cause and effect’’ [9], which also extensively informs
decision-making since ML necessarily restricts its power by
learning only patterns instead of, for instance, generating
causal relations for its predictions. Causal inference has two
paradigms which can inform solutions to these problems.
The first is the potential outcomes framework, where ‘‘the
causal effect of a treatment on a unit is the difference
between the outcome when the unit receives the treatment
and the outcome when the unit does not’’ [11]. The
second is ‘‘the process of using data together with causal
assumptions to answer questions about causal relations—
such as predicting the effect of interventions or explaining
observed dependencies’’ [9]. The first provides a coherent
underpinning for counterfactual reasoning [12], and the
second provides models for reasoning qualitatively about the
data-generating process and is critical for the transportability
of causal knowledge [9]. The synthesis of the two is clear: ‘‘by
leveraging causal inference, you go beyond description and
association,’’ being able to ask what alternative actions would
do under differing situations [10]. These advances form the
basis of heterogeneous treatment effect (HTE) estimation,
which directly focuses on individual-level responsiveness
to interventions [6],
In this line of work,
Causal Trees reveal treatment heterogeneity using recursive
partitioning [6], and Causal Forests extend this methodology,
resulting in consistent Conditional Average Treatment Effects
(CATEs) [13]. Meta-learners (e.g., S-, T-, X-, and R-
learners) [15] reformulate the causal estimation task into
modular supervised-learning settings that allow for flexibility
and scalability across data environments [15]. Beyond
estimation, policy learning integrates causal inference with
decision-making contexts, creating decision rules from
estimates of treatment effects [16].

[13],

[14].

In practical internet lending systems, interventions such
as interest coupons, fee reductions, credit line adjustments,
and targeted reminders are routinely deployed to influence
user borrowing behavior. When such actions are guided
solely by predictive models or raw treatment-effect estimates,
platforms may repeatedly allocate incentives to users who
would borrow regardless of intervention, while failing to
activate users who are truly responsive to targeted actions.
Moreover, these interventions are often applied repeatedly
under budget and risk constraints, making it difficult to
translate heterogeneous treatment effect estimates into stable,
interpretable, and decision-aligned user representations.

Concurrently with the emerging HTE literature, uplift
modeling first arose in applied domains such as marketing,
healthcare, and finance to directly estimate incremental
impact: the difference between the probability of response
from a group exposed to treatment and that of a comparable
group not exposed [17]. In practical terms, this quantity
answers how much more likely a user
is to respond
as a direct result of an intervention, rather than due to
baseline propensity. Uplift models [18], [19] that focus on
modeling the ‘‘treatment effect induced,’’ rather than overall
predictive accuracy, can employ tree-based approaches. The
‘‘four-type’’ consumer classes—Persuadables, Sure Things,
Lost Causes, and Do-Not-Disturbs—serve as the concep-
tual framework for studying individual causal response
[20], [21], [22]. This taxonomy is widely used to align
incremental-effect estimation with operational
targeting,
because it distinguishes true incremental responders (Per-
suadables) from always-responders (Sure Things), never-
responders (Lost Causes), and users for whom treatment
may be harmful (Do-Not-Disturbs). [20], [21], [22] Uplift
modeling evaluates targeting strategies against metrics such
as Area Under the Uplift Curve (AUUC) and Qini coefficient,
which capture the incremental gain produced [17], [19].
Recently conducted reviews warn that uplift performance is
very sensitive to upstream design choices—feature selection,
clustering, and labeling—and that the value of an integrated
and transparent pipeline is greater than isolated model and
algorithm comparisons [8], [22].

Yet, ‘‘traditional’’ user profiling continues to follow the
predictable, descriptive steps of data collection, normal-
ization and cleansing, feature extraction, clustering, and
performance evaluation. The primary goal remains predictive
segmentation and operational classification [4], [23], [24].
Current profiling systems, effective as they are for prediction,
are not designed to estimate how users would respond to
interventions, nor do they derive properties from causal
heterogeneity [7]. From the perspective of profiling, causal
reasoning has not yet been embedded into an end-to-end
analysis pipeline, and we ask three broad methodology
questions: (i) how to design new AAUC-driven response
segmentation, where labeling both informs and determines
evaluation; (ii) how to integrate feature selection, stratified
clustering, bias adjustment, and treatment-effect estimation

40148

VOLUME 14, 2026

---

<!-- PAGE 3 -->

J. Jiang et al.: Dynamic Framework for CUP and Treatment Segmentation via Uplift Modeling

into a new unified causal user profiling workflow; and (iii)
how to measure the marginal contribution of each pipeline
component through component-wise ablation analysis [22].
This work intends to close these gaps by introducing a
unified method called Causal User Profiling (CUP), inte-
grating user profiling, causal inference, and uplift modeling
into a single analysis process, building on the previous
descriptive roadmap but embedding causal estimation and
uplift-based evaluation into its core. Conceptually, it allows
causal reasoning to take form inside profiling methods,
stating not only who users are, but how they respond to
actions performed on them [25].

We summarize three contributions:
(1) Causal User Profiling Framework. We propose an
integrated methodological framework that connects feature
selection, clustering, confounding adjustment, and causal
effect estimation into a coherent causal user profiling
pipeline.

(2) AAUC-Driven Post-Evaluation Response Segmenta-
tion. We develop a performance-based segmentation mech-
anism that classifies users into the four causal response
types (Persuadables, Sure Things, Lost Causes, and Do-
Not-Disturbs) based on AAUC results, bridging model
evaluation with actionable user interpretation. For example,
separating Persuadables from Sure Things clarifies whether
a high-response segment reflects true incremental impact or
merely high baseline propensity.

(3) Component-Wise Ablation and Performance Analysis.
We quantify the marginal contribution of each pipeline
stage—feature selection, clustering, bias adjustment, and
causal estimation—to overall uplift performance, providing
reproducible methodological insights for practitioners.

Validating on an internet-lending dataset, results illustrate
how embedding causal reasoning within user profiling
provides a means to deliver additional value to customers and
businesses alike, ultimately leading to better personalization,
more precise targeting, and more effective data-driven
decision-making under real-world constraints [22], [23].

a: ORGANIZATION OF THE PAPER
The remainder of this paper is organized as follows. Section II
reviews related work on heterogeneous treatment effect
estimation, uplift modeling, causal inference in recommender
systems, and user profiling, and identifies the methodological
gaps addressed in this study. Section III introduces the Causal
User Profiling (CUP) framework, detailing its core modules
including feature selection, causal estimation, clustering, and
response-type segmentation. Section IV describes the data
source, preprocessing procedures, and experimental design.
Section V presents and discusses the empirical results,
focusing on model performance, stability, and interpretability
under repeated interventions. Section VI outlines the lim-
itations of the proposed framework. Finally, Section VII
concludes the paper and discusses directions for future
research.

II. RELATED WORK
A. UPLIFT MODELING AND EVALUATION
Uplift modeling—also referred to as incremental response
modeling—reconceptualizes prediction as the estimation
of differential treatment response, emphasizing the causal
effect of an intervention rather than its absolute outcome
level. In contrast to conventional predictive modeling, which
estimates the likelihood of an outcome, uplift modeling
explicitly focuses on the change in outcome probability
attributable to an action. As Radcliffe and Surry [17] state,
uplift defines the notion of ‘‘the difference in response
rates attributable to a treatment’’ that ‘‘shifts analytics from
descriptive prediction into the prescriptive space.’’ Early
approaches adopted a two-model strategy, in which separate
predictive models are trained for treated and untreated groups,
and the difference is interpreted as the incremental effect [20].
Although simple to conceptualize, two-model approaches can
be unstable and lead to biased estimates when treatment
allocation is imbalanced or when covariate distributions differ
substantially across groups.

A significant methodological advance arrived with
tree-based uplift models, which introduced recursive parti-
tioning to seek maximum treatment–control heterogeneity
within subgroups [18]. These Uplift Decision Trees offered
interpretable segmentation rules and provided groundwork
for subsequent ensemble extensions. Uplift random forests
and causal forests improved robustness and consistency
through aggregation, although at some cost to interpretability
[6], [13]. This line of work reflects a broader methodolog-
transition toward explicitly modeling heterogeneous
ical
treatment effects (HTE) to inform intervention decisions.
As summarized by Devriendt et al. [22], this evolution
represents a broader shift from purely predictive response
models to prescriptive analytics that conceptually situates
uplift modeling within modern causal inference.

Parallel advances occurred in meta-learning approaches
that reinterpret uplift estimation as superimposed supervised
learning tasks. Frameworks like the S-, T-, X-, R-, and
DR-learners unify heterogeneous treatment effect (HTE)
estimation and uplift prediction under flexible templates [14],
[15]. These approaches decouple the estimation of nuisance
components, such as outcome and treatment assignment
models, from the final treatment-effect estimator, enabling
flexible combinations with different base learners. In prac-
tice, meta-learners differ mainly in how they reuse outcome
models and propensity information under imbalance and lim-
ited overlap, and their stability is therefore strongly shaped
by base-learner choice and nuisance-model specification.
[14], [15], [19] These methods yield additional generalization
across settings but remain sensitive to base-learner selection,
sample size, and hyperparameter tuning. Until now, tabular
models and representation-learning–based causal networks,
such as TARNet, CFRNet, DragonNet, and GANITE, have
adopted deep architectures to mitigate covariate imbalance,
reduce the burden of counterfactuals, or model nonlinear

VOLUME 14, 2026

40149

---

<!-- PAGE 4 -->

J. Jiang et al.: Dynamic Framework for CUP and Treatment Segmentation via Uplift Modeling

treatment effects on the response [26], [27], [28]. While
such models improve expressive capacity, prior studies note
trade-offs in interpretability, stability, and reproducibility,
particularly in profiling-oriented applications.

As models improved, so did evaluation. Uplift modeling
concerns incremental gain; thus standard accuracy metrics
are not useful. Uplift-specific ranking measures such as
the ‘‘Qini coefficient(s)’’ and the ‘‘Area Under the Uplift
Curve (AUUC)’’ are now standard [17], [19]. Both met-
rics evaluate how effectively a model ranks individuals
by incremental response rather than by absolute outcome
likelihood. The Qini coefficient sums cumulative differences
across incremental uplift-ranked segments between treated
and control groups. AUUC measures the total incremental
effect via the area between the uplift curve and a diagonal
baseline. The latter can be sensitive to treatment imbalance
or sparse samples, and recent advances have introduced
multi-treatment AUUC and cross-treatment gain surfaces
to cover multi-arm and dose-response settings [29], [30].
Intuitively, gain-surface style evaluations summarize how
incremental ranking performance varies across intervention
arms, making cross-arm trade-offs and sensitivity to treat-
ment choice explicit. [29], [30] Reviews emphasize that
the ability to generate strong uplift curves is attributable
largely to upstream pipeline design choices, particularly
feature selection, user segmentation, and response-type/target
labeling [8], [22]. Other comparative studies consider uplift
algorithms to be ‘‘opaque models’’ and provide limited detail
on implementation or sensitivity analyses, which undermines
reproducibility and reduces practical interpretability [17],
[18]. In this study, reproducibility refers to reporting and
structuring the full pipeline—feature construction/selection,
clustering settings, propensity modeling, learner configu-
ration, and labeling rules—so that an independent team
can rerun the workflow and obtain consistent uplift curves
and response-type assignments under the same data and
protocol. These concerns motivate a methodological shift
from isolated model comparison toward workflow-level opti-
mization, focusing on transparent design choices, pipeline
configuration, and component-wise diagnostics—principles
that underpin the Causal User Profiling (CUP) framework
introduced in this study.

B. HETEROGENEOUS TREATMENT EFFECTS (HTE) AND
CATE ESTIMATION
Although uplift modeling is used mostly in marketing
and intervention targeting, the concept of Heterogeneous
Treatment Effects (HTE) provides the theoretical foundation
for uplift modeling. HTE methods aim to estimate the
Conditional Average Treatment Effect (CATE) for each
the
individual or subgroup in the population—that
expected causal effect conditional on observed features [6],
[13]. From this perspective, uplift modeling can be viewed
as an operationalization of HTE estimation that emphasizes
ranking and targeting decisions rather than pointwise effect
estimation alone.

is,

Tree-based methods such as Causal Trees start with the full
covariate space and recursively partition it to identify regions
with distinct treatment effects. Causal Forests, for several
well-founded reasons, instead employ ensemble aggregation,
yielding more consistent estimators and supporting valid
statistical inference across regions [6], [13]. Generalized
Random Forests (GRF) extend this local/posterior forest
framework, unifying a large class of forest-based estimators
into a general nonparametric framework [16]. Beyond tree
ensembles, Bayesian and nonparametric approaches intro-
duce uncertainty quantification through credible intervals and
yield more robust estimates in small-sample or high-variance
settings [31], [32] via methods such as Bayesian Additive
Regression Trees (BART), Bayesian Causal Forests (BCF),
and Gaussian Process models. These approaches are often
preferred in settings where variance control and uncertainty
assessment are critical to downstream decision-making.

While lighter-weight estimators relax assumptions required
for CATE estimation, meta-learning approaches—S-, T-,
X-, R-, and DR-learners—decompose the CATE estimation
task into modular supervised learning problems and offer
flexibility in base-learner choice and treatment-variable
specification [14], [15]. The combination of meta-learners
with different base learners is motivated by the need to
balance bias, variance, and robustness under heterogeneous
data-generating conditions, rather than by any universally
optimal configuration. Empirical analyses show no uni-
versally dominant learner, highlighting that pipeline-level
optimization is preferred over naive model substitution
[22]. Representation-learning–based causal models such
as TARNet, CFRNet, DragonNet, and GANITE build
deep latent representations to reduce covariate imbalance
and improve counterfactual estimation [26], [27], [28].
While these models increase expressive capacity, prior
studies note trade-offs in transparency, stability, and repro-
ducibility, particularly when interpretability is required for
profiling-oriented analysis [7].

Evaluation frameworks in the HTE literature closely
those used in uplift modeling. Metrics such as
parallel
Incremental AUUC and Qini measure incremental ranking
performance, while Precision in Estimation of Heterogeneous
Effects (PEHE) and Mean Squared Error of Individual
Treatment Effects (MSE(ITE)) are common in semi-synthetic
benchmarks [15]. For joint learning of treatment policies,
policy value and doubly robust off-policy evaluation (OPE)
assess expected reward of policies derived from estimated
treatment effects [33]. When multiple interventions are
available, multi-treatment AUUC and consistency-based
metrics further characterize the stability of ranking and policy
decisions across treatment arms [29], [30].

Recent reviews provide empirical insight into the adoption
and implementation of HTE methods across domains.
A forthcoming 2024 methodological review of Causal Forest
applications analyzes 133 peer-reviewed studies across areas
from health to marketing, documenting widespread reliance
on the grf package but limited reporting of identification

40150

VOLUME 14, 2026

---

<!-- PAGE 5 -->

J. Jiang et al.: Dynamic Framework for CUP and Treatment Segmentation via Uplift Modeling

TABLE 1. Representative methods and evaluation frameworks in HTE and uplift modeling.

assumptions and tuning parameters [34]. A PRISMA-
guided scoping review of HTE estimation in randomized
controlled trials (RCTs) using machine learning reports
predominance of forest-based (60%) and Bayesian (53%)
models in domains such as health and education, while
again noting incomplete documentation of generalizability
checks and identification strategies [35]. In RCT-emulation
pipelines that benchmark recent methodologies—including
Ding et al. ’s RIF—reviews report frequent failures in
confounding adjustment or validation, reinforcing the impor-
tance of reproducibility, variance control, and coherent
pipeline design [36].

C. CAUSAL INFERENCE IN RECOMMENDER SYSTEMS
AND THE USER-PROFILING PIPELINE
In recommender systems, causal inference has been applied
to address exposure bias, selection bias, and to conduct
policy evaluation [23]. Rather than focusing solely on
predictive accuracy, this stream of work explicitly treats
recommendation actions as interventions and evaluates their
causal effects on user behavior. Recent reviews identify core
causal objectives along three interrelated dimensions:

(1) causal objectives, such as de-biasing item exposure and
estimating the treatment effects of recommendation actions;
including inverse propen-
sity scoring (IPS), doubly robust estimation (DR), and
instrumental-variable (IV) approaches;

(2) identification strategies,

(3) evaluation paradigms, covering offline policy learning,

counterfactual simulation, and online contextual bandits.

Together, these components form an integrated end-to-
end causal pipeline spanning data collection, identification,
policy optimization, and evaluation. This pipeline perspec-
tive emphasizes decision-oriented evaluation under explicit
interventions rather than static prediction.

Conversely,

traditional user-profiling research remains
largely predictive. As summarized by Wu et al. [8], profiling
pipelines typically consist of five sequential components—
data collection, data preprocessing, feature extraction, model-
ing, and evaluation—each originally designed for descriptive
segmentation or predictive accuracy rather than interpretabil-
ity. Similarly, Maraj et al. [37] argue that most profiling

systems emphasize data enrichment, privacy protection, and
governance considerations rather than response-driven causal
mechanisms. Purificato et al. [7] observe that many existing
profiling approaches ‘‘focus on correlations rather than causal
mechanisms,’’ limiting their ability to support responsive
interventions or predict user-level treatment responsiveness.
Thus, although causal recommender modeling has seen
significant advances, operational techniques that integrate
causal inference into user-profiling pipelines remain compar-
atively scarce. In particular, conventional profiling workflows
typically lack explicit components for treatment-effect identi-
fication, response-type labeling, and uplift-based evaluation.
A conceptual gap therefore persists between profiling work-
flows and causal-inference pipelines. Addressing this gap is
essential for moving beyond static or purely predictive user
profiles toward representations that capture how users are
likely to respond under alternative interventions.

D. GAPS OUR WORK ADDRESSES
Across the surveyed literatures, two practice-oriented gaps
arise repeatedly.

First, applications of HTE estimation and Causal Forest
modeling often under-report critical design and tuning
decisions, making it difficult to reproduce results uniformly
or determine which components of the pipeline actually
contribute to uplift or CATE performance. Rehill [34],
Inoue et al. [35], and Ling et al. [36] show that studies
frequently rely on heavy default hyperparameters, rarely
justify identification assumptions, and often omit report-
ing clustering or feature-selection strategies. As a result,
it remains unclear whether observed performance differences
stem from causal estimators themselves or from upstream
design choices such as feature selection, clustering, or label-
ing. This leaves unclear whether feature selection, clustering,
labeling, or other design choices are responsible for observed
uplift or CATE performance differences [22].

Second, mainstream user-profiling frameworks are com-
prehensive in data preparation and feature engineering, but
remain largely descriptive and correlation-based [7], [8].
They generally lack components for causal estimation, uplift-
based evaluation, or assignment of causal response types.

VOLUME 14, 2026

40151

---

<!-- PAGE 6 -->

J. Jiang et al.: Dynamic Framework for CUP and Treatment Segmentation via Uplift Modeling

Consequently, existing profiling systems are not designed to
represent how users are expected to respond under alternative
interventions, limiting their suitability for decision-oriented
personalization. This disconnect between predictive profiling
and causal reasoning inhibits existing systems from explain-
ing how users will respond to user-level interventions. Yet
such capabilities are core to adaptive personalization, broad
targeting optimization, and prescriptive analytics.

To address these gaps, we offer two methodological

contributions.

First, we introduce a module called Four-Type Response
theory, which uses
Segmentation, aligned with uplift
high-confidence uplift
thresholds, model-assisted infer-
ence, and post-hoc label refinement to operationalize the
dependence between AAUC-based evaluation metrics and
response-type labeling [18], [20]. This design explicitly
links model evaluation outcomes to interpretable response
categories, addressing the ambiguity between ranking perfor-
mance and user-level interpretation noted in prior studies.

Second, we propose improved Causal User Profiling
(CUP) Roadmap, which embeds feature selection, clus-
tering, confounding adjustment, causal estimation, and
response-type labeling into a unified, reproducible, and
resource-aware workflow. By structuring these components
as an integrated pipeline rather than isolated modeling steps,
CUP directly responds to reproducibility and transparency
concerns highlighted in the HTE and uplift
literature.
By combining causal inference, uplift modeling, and user
profiling into a single analytic pipeline, CUP addresses the
reproducibility issues and methodological silos highlighted
in earlier work, providing a principled foundation for causal
user profiling—a next-generation framework for data-driven
personalization, targeting, and intervention design.

III. RESEARCH FRAMEWORK
This paper proposes an integrated methodological frame-
work, Causal User Profiling (CUP), that connects three
previously disparate domains—user profiling, causal infer-
ence, and uplift modeling—into a common analytic pipeline
for personalized treatment analysis. This comes from our
observation that user-profiling studies typically investigate
who the user is, identifying demographic and behavioral
segments [4], [8], while ‘‘for practical intervention it is
important to first understand how a user would react if
we act’’ [6]. ‘‘Current user-modeling methods . . . focus
on correlations rather than causal mechanisms,’’ as noted
by Purificato et al. [7], which limits their interpretability
for strategic targeted interventions. The CUP framework
addresses this issue by embedding causal estimation and
response-based labeling into the profiling pipeline, turning
the de-facto descriptive workflow into a causally interpretable
and response-aware analytic system [22].

The CUP pipeline (Figure 1) builds on the conventional
user-modeling workflow.
It starts with data collection:
behavioral and contextual data are captured from production
platforms, followed by data preprocessing to ensure quality,

consistency, and readiness for analysis [8]. Next comes fea-
ture extraction, converting behavioral logs and demographic
information into representations suitable for modeling.

Although not shown in Figure 1 as a red-arrow component
of its own, feature selection is an essential overhead to this
step, ensuring that only variables with both predictive and
causal relevance move down the causal analysis pipeline.
Eke et al. [4] emphasize that profiling based on user behaviors
requires appropriate choice of representative variables, while
is easy to accept
Wager and Athey [13] warn that
predictive but non-causal features with varying predictive
noise (which tends to dilute estimated treatment effects). CUP
therefore uses a two-pronged approach: information value for
predictive importance, and causal importance from a Causal
Forests approach [13] to stabilize the interventions.

it

The first

truly new component of CUP is clustering
for stratification, grouping users into behaviorally similar
and causally comparable groups. As Wu et al. [8] remark,
‘‘most prior clustering methods for user profiling are mainly
descriptive and static; causal analysis benefits from grouping
such that the treatment and control users in a group are
balanced in terms of their distributions.’’ This aligns with
findings from Devriendt et al. [22], who show that uplift
models are sensitive to sample imbalance and perform better
in reliable uplift segments. Thus, CUP’s clustering step trades
off descriptive interpretability for causal validity by pairing
comparability with segmentation.

Treatment (T) is defined as a binary indicator of whether a
user received the targeted intervention within a given month.
Outcome (Y) is defined as whether the user initiated a
loan application during the same evaluation window. Causal
effects are estimated—after treatment-control selection—in
the next submodule, confounding and bias adjustment. This
step helps ensure that treatment and control groups are
comparable to permit causal attribution in non-experimental
settings. Bias-adjustment methods include inverse probability
weighting (IPW) and stratified reweighting (see [6] and [14]).
Through these techniques, CUP mitigates selection bias
and strengthens internal validity. To ensure comparabil-
ity between treated and control groups in the empirical
analysis, treatment assignment probabilities are estimated
using observed covariates and incorporated through inverse
propensity weighting during uplift evaluation. This adjust-
ment mitigates treatment imbalance arising from non-random
intervention assignment and reduces bias when comparing
incremental outcomes between treatment arms.

Next, within the potential-outcomes framework [11],
is the causal-effect estimation module. Our causal estimation
follows the standard potential-outcomes framework, which
assumes (i) SUTVA, (ii) conditional
ignorability given
observed covariates, and (iii) overlap (0 < P(T =
1|X ) < 1). Under these identification conditions, IPW
and DR learners provide consistent estimates of treatment
effects. Causal Trees [6]
track treatment heterogeneity
using recursive partitioning, and this logic is extended in
Causal Forests [14]. CATEs (conditional average treatment

40152

VOLUME 14, 2026

---

<!-- PAGE 7 -->

J. Jiang et al.: Dynamic Framework for CUP and Treatment Segmentation via Uplift Modeling

FIGURE 1. Traditional versus newly designed Causal User Profiling (CUP) roadmap. Blue arrows represent the traditional user profiling
process—Data Collection, Data Preprocessing, Feature Extraction, Modeling, and Performance Evaluation—while red arrows represent CUP
extensions: Clustering for Stratification, Confounding and Bias Adjustment, Causal Effect Estimation, and Response-Type Labeling.

effects) are the resulting estimands from such hierarchical
estimators. Meta-learning algorithms such as T-, S-, X-, and
R-learners [15] restate causal estimation as modular (still
supervised-learning) tasks that may be adjusted for cross-
environment flexibility. These estimators output each user’s
uplift value (the effect an intervention has on user behavior).
Following causal estimation, the performance-evaluation
submodule measures the captured impact. The Area Under
the Uplift Curve (AUUC) is, according to Devriendt et al.
[22] and Gutiérrez and Gérardy [19], the preferred metric for
uplift performance—measuring not predictive accuracy, but
incremental impact captured (see [17]). We denote AUUC
as the monthly Area Under the Uplift Curve computed
within each evaluation window. AAUC refers to the average
AUUC across the six monthly evaluations used in our rolling
experimental design. To interpret user-response behavior
and to disentangle module contributions, CUP performs
component-wise ablation analysis, isolating the per-stage
effect of the four modules: feature selection, clustering, bias
adjustment, and causal estimation. This follows the principle
that ‘‘uplift performance depends strongly on upstream
design choices’’ [22]. The purpose of the ablation analysis
in this study is not to conduct formal hypothesis testing, but
to assess the relative contribution and stability of individual
pipeline components under repeated real-world deployments.
Each ablation experiment removes one component from
the CUP workflow while keeping all others fixed, and
performance differences are evaluated consistently across
six consecutive monthly datasets. By examining whether
performance changes persist across time periods rather
than relying on a single snapshot, the analysis provides
empirical evidence on whether observed gains are systematic
rather than incidental. Given the operational nature of
the study and the use of large-scale observational data,
we focus on temporal consistency and magnitude of perfor-
mance differences rather than formal statistical significance
testing.

Response-type labeling occurs after performance evalu-
ation. Using AUUC-based results, users are tagged to the
four classic causal-response categories—Persuadables, Sure
Things, Lost Causes, and Do-Not-Disturbs—as defined by
Radcliffe and Surry [17] and extended by Jaskowski and
Jaroszewicz [21]. The result of this post-evaluation process
is interpreting user-model outputs into actionable causal
profiles, completing the causal-profiling loop.

CUP brings descriptive profiling and causal inference
closer together in a single sequence. Preservation of inter-
pretability from user profiling [4], [8], combined with the
structure of causal-effect estimation formalism [6], [15],
is central to the method, as is adopting the evaluative rigor
of uplift modeling [17], [22]. With utility demonstrated on
an Internet-lending dataset, the CUP framework shows how
causal ‘‘laws’’ can be operationalized within profiling to
support personalized and data-driven decision-making under
real-world constraints.

A. FOUR-TYPE RESPONSE SEGMENTATION MODULE
1) CONCEPT AND TAXONOMY
Based on the potential outcomes framework [11],
the
Four-Type Response module assigns users to four canonical
causal-response types—Persuadable (A), Sure Thing (B),
Lost Cause (C), and Do-Not-Disturb (D). These types
describe how an individual’s outcome would change were the
intervention present or absent, capturing causal responsive-
ness rather than behavioral similarity [17], [20].

In contrast to typical segmentation methods that cluster
users based on demographic or behavioral factors, uplift-
based profiling emphasizes incremental impact estimation—
the assessment of how the probability that a user takes the
desired action changes when the treatment is applied. Framed
in this way, user profiling becomes not merely descriptive,
but a treatment-aware decision process, informing the design
and evaluation of personalized interventions in marketing,
healthcare, and credit-analytics domains [18], [19], [22].

VOLUME 14, 2026

40153

---

<!-- PAGE 8 -->

J. Jiang et al.: Dynamic Framework for CUP and Treatment Segmentation via Uplift Modeling

TABLE 2. Behavioral evidence partition linking theoretical response
categories with observed treatment–outcome patterns.

2) BEHAVIORAL EVIDENCE PARTITION
To provide empirically grounded baselines for the theoretical
response types above, users are partitioned by treatment
assignment T and outcome Y , resulting in four cells of
evidence based on observed behavioral congruency expected
across the categories (Table 2). This integrates causal
estimation and response-based labeling into the profiling
pipeline, converting the conventional descriptive workflow
into a causally interpretable and response-aware analytic
system [22].

‘‘A’’ but

This partition restricts theoretical labeling to behavioral
realizability: a user assigned label
found in
T = 1, Y = 0(Set 2) would exhibit an anchored
violation of behavioral consistency and would therefore be
de-provisioned of the ‘‘A’’ label (referencing ‘‘refinement’’
from the previous subsection). Such anchoring makes the
Four-Type taxonomy both causally interpretable and empiri-
cally grounded.

3) EVOLVING THE SEGMENTATION DESIGNS FOR
FOUR-TYPE RESPONSE (V1-3)
The Four-Type Response Segmentation module evolved
through three generations of increasing interpretability and
robustness as we addressed limitations in earlier designs. The
key methodological distinctions are summarized concisely in
Table 3.

a: V1
The initial version (V1) adopts a simple triage approach that
partitions users into High, Medium, or Low responsiveness
groups solely based on the uplift score:

ˆp1 = P(Y = 1 | T = 1, X ),
ˆp0 = P(Y = 1 | T = 0, X ),
u = ˆp1 − ˆp0.

ui ≥ δ,
High,

Low,
ui ≤ −δ,
Medium, otherwise.



labeli =

(1)

This design provides a lightweight way to register individ-
ual sensitivity to intervention and offers a computationally
identifying users likely to be
inexpensive method for
affected. However,
it does not provide structural causal
interpretability, nor can any purely uplift-based design; thus it
remains a descriptive rather than a fully causal segmentation
method.

Algorithm 1 Version 1 – Uplift-only Triage (High / Medium
/ Low)
Input: Dataset D with column uplift_score u (or u =
ˆp1 − ˆp0 if available)
Output: Triage label ∈ {High, Medium, Low} for each
sample
Protocol: Split D into outer train/valid/test; select δ on valid
to maximize AUUC; freeze δ for test (no leakage)
1: for each i ∈ D do
if ui > δ then
2:

3:

4:

5:

6:

7:

label ← High
else if |ui| < δ then
label ← Medium

else

label ← Low

end if
8:
9: end for

Optional mapping:

• if ui ≥ δ → candidate for A (Persuadable)
• if ui ≤ −δ → candidate for D (Do Not Disturb)
• if |ui| < δ → candidate region for B/C (resolved by

V2/V3)

b: V2
The second version (V2) extends the framework by introduc-
ing a counterfactual mapping between treatment and control
outcome probabilities, constructing a two-dimensional pre-
diction space:

ˆp1 = P(Y = 1 | T = 1, X ),
ˆp0 = P(Y = 1 | T = 0, X ),
u = ˆp1 − ˆp0.

(2)

, δ) users are

Based on calibrated thresholds (yth
1

, yth
0

assigned to the four canonical response types as follows:

This design corresponds closely to the uplift-modeling
literatures [6] and [18] and enables interpretability as it visu-
alizes causal responsiveness across probability quadrants.
In reality, however, only a fraction of users are cleanly
segmented into these quadrants; many lie close to decision
boundaries, resulting in ambiguous labels or oscillating
between them. V2 therefore has better interpretability than
V1, but at the cost of robustness, as demonstrated during
evaluation [22].

c: V3
V3 introduces a hybrid causal–behavioral architecture that
uses uplift estimation, behavioral validation, and model
re-assessment to produce a joint labeling framework. V3
begins with high-confidence lift-based labeling and recon-
ciles theoretical label assignments with empirical behavior,
followed by classifier-based refinement to re-label ambigu-
ous or conflicting cases.

The V3 hybrid causal–behavioral procedure consists of

four stages, illustrated below:

40154

VOLUME 14, 2026

---

<!-- PAGE 9 -->

J. Jiang et al.: Dynamic Framework for CUP and Treatment Segmentation via Uplift Modeling

TABLE 3. Comparison of the three segmentation designs (V1–V3) by input dependencies and methodological focus.

FIGURE 2. V3-Based Four-Stage Causal Labeling Framework.

TABLE 4. Counterfactual quadrant mapping for four-type labeling.

Using this multi-stage infusion of uplift prediction, coun-
terfactual reasoning, and behavioral correction, V3 produces
causally interpretable and empirically consistent response-
type segmentation, achieving significant AUUC stability and
behavioral-consistency improvements over prior versions.
By anchoring response-type assignments to both uplift
estimates and observed (T , Y ) behavioral evidence, the V3
design promotes label consistency across time windows while
allowing individual users to transition between response
states as their behavior evolves.

This segmentation logic of the V3 hybrid labeling frame-

work shows:

What is the uplift distribution?
It is partitioned into five pieces by adjustable thresholds,
which correspond to the four stages of the labeling pipeline:

(1) uplift-based extreme segmentation;
(2) behavioral expansion of A/D boundaries;
(3) model-assisted tagging of ambiguous cases; and
(4) final integration and auditing.
The net result: maximum coverage of A and D users while
keeping (T , Y ) behavior consistent across all four response
types.

4) SUMMARY AND DISCUSSION
The three versions of user segmentation represent a journey
from the very light-handed uplift-based stratification (V1),

VOLUME 14, 2026

40155

---

<!-- PAGE 10 -->

J. Jiang et al.: Dynamic Framework for CUP and Treatment Segmentation via Uplift Modeling

Algorithm 2 Version 2 – Counterfactual Four-Quadrant
Segmentation
Input: Dataset D with columns y1_prob(p1), y0_prob(p0)
(arm-wise calibrated);
Output: Response type ∈ {A, B, C, D} for each sample
Protocol: Outer
(h, ℓ, δ) on validation to maximize AUUC;
(h∗, ℓ∗, δ∗) on test; drop samples violating overlap.
1: for each sample i ∈ D do
2:

if p1,i ≥ h∗ and p0,i ≤ ℓ∗ and ui ≥ δ∗ then

split; grid-search
fix

uplift u = p1 − p0

train/validation/test

labeli ← A (Persuadable)

else if p1,i ≤ ℓ∗ and p0,i ≥ h∗ and ui ≤ −δ∗ then

labeli ← D (Do Not Disturb)

else if p1,i ≥ h∗ and p0,i ≥ h∗ and |ui| < δ∗ then

labeli ← B (Sure Thing)

else if p1,i ≤ ℓ∗ and p0,i ≤ ℓ∗ and |ui| < δ∗ then

labeli ← C (Lost Cause)

else

labeli ← NearestCorner(p1,i, p0,i; h∗, ℓ∗, sign(ui))

end if
12:
13: end for
14: return {labeli}
Note: Figure 2b presents the conceptual diagram of counter-
factual segmentation under V2.

TABLE 5. Stages and functional Roles in the V3 causal labeling
framework.

3:

4:

5:

6:

7:

8:

9:
10:

11:

Algorithm 3 Hybrid Labeling (Compact Layout)
Input: Dataset D, T ∈ {0, 1}, Y ∈ {0, 1}
Output: Type ∈ {A,B,C,D}, Flags
Protocol: Train/Valid/Test split; maximize AUUC on Valid;
freeze on Test.
(A) Arm-wise models & Calibration

Train p1(x) & p0(x); Calibrate per arm.
u(x) = p1 − p0; drop overlap violators.

(B) Behavioral evidence partition

S1 = {T1, Y1}, S2 = {T1, Y0},

S3 = {T0, Y1}, S4 = {T0, Y0}.

(C) High/Mid-confidence A/D rules

Tune (uhigh, umid) on Valid. For i ∈ D:

a) High-confidence rule.

• If |ui| ≥ uhigh: assign A if ui > 0, otherwise

assign D if ui < 0.

b) Mid-confidence behavioral expansion. Else,

check umid-behavior consistency:
• If ui ≥ umid & (S1 or S4) → A
• If ui ≤ −umid & (S2 or S3) → D
• Else conflict → AD_conflict

(D) Initial B/C with conflict flags

For remaining i:

• If Y = 1: (ui < −uconf?B_conflict:B)
• If Y = 0: (ui > uconf?C_conflict:C)

(E) Model-assisted A↔D refinement

Train Classifier on Step (C) labels (stratified).
Reassign if Prob ≥ τAD & consistent quadrant.

(F) Model-assisted B↔C refinement

Use clean B/C from (D) as supervision.
Train/Calibrate B vs C models.
Refine if consensus ≥ τBC .

(G) Output

Return final labels, conflict types & diagnostics.
Note: Figure 2c presents the conceptual diagram of the
hybrid labeling workflow (P3) combining confidence rules
and model refinement.

through the more complex counterfactual segmentation (V2),
to the causal–behavioral hybrid refinement (V3) with which
the final design aligns. The addition of counterfactual
estimation and user profiling into the approach of V2
makes the return to descriptive profiling reach toward a
causal user-description framework that is interpretable and
grounded in the data. This journey reflects how the principles
of causal inference can help operationalize user profiling,
bridging incremental-impact modeling with behavioral real-
ism to support decision-making within systems that rely on
interventions.

B. IMPROVED EXPERIMENTAL DESIGN
Re-approaching uplift modeling as an evaluation of user
profiling, the improved experimental design strengthens the
reasoning behind how components of uplift modeling work
together. Rather than iteratively optimizing a single predictive
model, we reframe the assessment of intervention approaches
and refine all methodological components (feature selection,
clustering, causal estimation, response labeling), each of
which shapes the overall Area Under the Uplift Curve
(AUUC). With a structured modular approach in place, the
pipeline evaluation allows us to identify how components

40156

VOLUME 14, 2026

---

<!-- PAGE 11 -->

J. Jiang et al.: Dynamic Framework for CUP and Treatment Segmentation via Uplift Modeling

work together transparently, ensuring that an uplift-based
user-profiling pipeline is reproducible and as interpretable as
possible.

1) PIPELINE OVERVIEW
The framework for user profiling is based on causal
principles. Following from causal user profiling, we add to
the pipeline (Figure 3) a user-profiling and ‘‘de-causalizing’’
methodology based on feature uniqueness and response.
In particular, clustering, causal estimation, user profiling,
and component-wise ablation are incorporated to quantify
contributions.

Operating on a monthly rolling basis—across both
cross-sectional and temporal vigilance—the pipeline allows
examination of how feature selection, clustering, response-
interaction information, and causal adjustment work together
as individual components of a Causal User Profiling (CUP)
pipeline. All experiments share a common time-based
train/validation/test protocol with shared random seeds and
fixed preprocessing across months, highlighting that these
choices drive stability and practical reliability in modeling
user profiling under the causal framework.

2) CORE MODULES: FROM FEATURE SELECTION TO CAUSAL
ESTIMATION
The pipeline begins by identifying features that are both
stable and causally relevant, allowing us to draw causal
insights generalizable to unseen treatment groups. A multi-
stage selection process combines statistical relevance (Infor-
mation Value, IV), temporal stability (Population Stability
Index, PSI), and causal importance (Causal Forest variable
importance and stepwise regression) [13]. This produces
multiple feature sets from the base DataFrame: IV-only/PSI
subsets, CF-only/PSI, and hybrid types (IV + CF, IV + CF
+ STEP). The aim is to obtain a parsimonious set of features
representative of the population, standardized and imputed on
the same folds to ensure fairness and causal interpretability.
Before uplift estimation, we must address any remaining
treatment-control imbalances, often done using Propensity
Score Matching (PSM) and Inverse Probability Weighting
(IPW) [10], [38]. These covariate-adjustment
techniques
reweight samples to render treated and control groups
comparable so that the uplift reflects the genuine treatment
effect rather than asymmetries in treatment allocation (i.e.,
selection bias). For randomized subsets, they also serve as
a sanity check for stability: estimated uplift effects should
confirm confounding control.

Uplift estimation is conducted using two families of
models: meta-learners and Causal Forests. Meta-learners
such as T-, S-, X-, R-, and DR-learners factor CATE
estimation into modular supervised-learning tasks [14], [15],
while Causal Forests provide nonparametric and asymptoti-
cally consistent estimates of heterogeneous treatment effects
[16]. To preserve causal integrity, all learners share the
same preprocessing, data, and evaluation strategy. Logistic

Regression often serves as the baseline learner for com-
putational efficiency, while Random Forests, GBDT, and
XGBoost are employed as sanity checks. Each learner’s out-
puts are then passed to the Four-Type Response Segmentation
Module (Section III-B) to yield CATE/uplift scores tagged
with behavioral names or interpretable types.

In a final step to facilitate causal interpretability, we cluster
users into causally homogeneous strata. Recognizing that
real-world behavioral heterogeneity drives treatment-effect
variation, CUP employs K-Means clustering on standardized
features to form stable subpopulations, each serving as a
contextual unit for uplift estimation [8], [22]. The optimal
number of clusters K is chosen via elbow and silhouette
criteria. Clusters below 2% of total samples or yielding
AUUC lower than the baseline are merged into others.
Notably, clustering enhances interpretability and reveals
behavioral regimes that would otherwise remain hidden.

3) EVALUATION AND ABLATION DESIGN
This evaluation procedure quantifies how each decision either
promoted or detracted from ultimate uplift performance.
We use area under the uplift curve (AUUC) as the core
performance measure, as well as the Qini coefficient and
uplift@k [17], [19], [22]. We separate marginal effects
through component-wise ablation (e.g., removing the clus-
tering, causal feature selection, or label refinement module).
Performance is evaluated both globally and by cluster, using
a weighted metric:

Weighted AUUC =

K
X

k=1

wk · AUUCk ,

(3)

where wk denotes the relative proportion of valid samples in
cluster k.

Other diagnostics include:
• Label adherence rates (band, quadrant, and behavioral-

cell consistency)

• Type-wise outcome balance between treatment and

control groups

• Temporal stability measured via Cohen’s κ across

months

• Computational efficiency (runtime and convergence)
We computed robustness via bootstrap confidence inter-
vals, out-of-time validation, and selective sweeps through
subsamples when the uplift they contained appeared erratic.
We performed all experiments with fixed random seeds,
version-controlled datasets, and standardized preprocessing
pipelines. We took comprehensive logs of AUUC, variable
importance, and cluster diagnostics from each run, and then
stitched together the pieces. This provided a transparent
‘‘causal audit trail’’ enabling independent replication of our
results.

To avoid ad-hoc decisions outside the evaluation frame-
work, we made reproducibility a foundation within our evalu-
ation rather than separate it out as its own stage. This trade-off
between methodological rigor and operational reliability

VOLUME 14, 2026

40157

---

<!-- PAGE 12 -->

J. Jiang et al.: Dynamic Framework for CUP and Treatment Segmentation via Uplift Modeling

FIGURE 3. Improved experimental pipeline of the Causal User Profiling (CUP) framework. The pipeline integrates feature selection,
clustering, confounding adjustment, causal effect estimation, and evaluation into a reproducible workflow executed in monthly rolling
loops.

was empirically observed: this evaluation strategy stabilized
the AUUC variance across monthly slices. It reduced the
damage from confounding-driven fluctuations while giving
us a reliable measure of true treatment heterogeneity.

C. SUMMARY
In this chapter we presented an enhanced experimental
design that integrates both causal inference and user profiling
into a single uplift-modeling approach. The Four-Type
Response Segmentation Module guarantees causal labeling
robustness, while component-wise ablation analysis gauges
the contribution of each methodological component—feature
selection, clustering, and causal estimation—to the uplift
score. All of this is implemented in one consolidated process
that weaves evaluation and reproducibility together, thereby
laying the groundwork for a transparent, interpretable, and
empirically validated basis for dynamic causal user profiling.

IV. DATA DESCRIPTION
In our empirical analysis we employ proprietary data
collected from users of a leading Chinese internet finance
platform’s mobile app. To enable causal
interpretability,
we consider only active borrowers, i.e., users with outstand-
ing loan balances in the observation window. Compared to
non-borrowers (who are not indebted or have satisfied prior
loan demands), active borrowers are more homogeneous:
they seek credit more consistently, reducing the number of
possible confounders arising from variation in borrowing
motives. By ensuring behavioral comparability between
treated and control users, this focus improves the power of
causal identification.

The dataset consists of an intermingled trove of infor-
mation covering demographic behavior as well as credit

status—including both static user attributes and dynamic
financial indicators—comprising: gender, age, and city tier;
borrowing frequency; repayment performance; credit-line
utilization limits; overdue history and repayment discipline;
and consumption-related activity. These variables capture
treatment heterogeneity and user-specific behavior in gen-
eral.

Prior to model fitting, several procedures were conducted
to improve comparability and robustness within and across
potential covariates. Following business conventions, missing
or invalid values were set according to domain logic;
numerous continuous features were scaled for numeric com-
parability; and feature selection was subsequently applied
through a diagnostic three-stage procedure consistent with
previously documented theory [22]. This screening stage is
performed before constructing the downstream feature-set
configurations (e.g.,
IV-only, Causal, and hybrid sets),
ensuring that all reported feature sets are derived from the
same filtered and stability-checked candidate pool:

1. Information Value (IV) was computed to quantify

predictive relevance for the target outcome.

2. Population Stability Index (PSI) was used to evaluate
temporal stability and detect distributional shifts across
months.

3. Pairwise correlation analysis identified redundant vari-

ables and mitigated multicollinearity.

Variables having IV < 0.05 or PSI > 0.25 were dropped,
and features were merged when their pairwise correlation
exceeded 0.8 in absolute terms. This process produced
a balanced set of features encompassing interpretability,
robustness, and predictive capability—in line with recent
methodological standards in heterogeneous treatment-effect
research for similar use cases [41].

40158

VOLUME 14, 2026

---

<!-- PAGE 13 -->

J. Jiang et al.: Dynamic Framework for CUP and Treatment Segmentation via Uplift Modeling

Algorithm 4 Core Experimental Loop (Baseline and
Clustering-Enabled)
Input: Dataset D; FeatureSets {F1, . . . , F6};
Metalearners {T , S, X , DR, CF}; Baselearners {LR, RF,
GBDT, XGB}; Months {M1, . . . , M6}
Output: AUUC scores; cluster statistics; variable importance
1: for each month m ⊆ {M1, . . . , M6} do
Dm ← subset(D, month = m)
2:
for each feature set F in FeatureSets do

3:

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

14:

15:

16:

17:

18:

19:

20:

21:

22:

23:

X ← select_features(Dm, F); T ← treatment;
Y ← outcome
for each ML ∈ Metalearners do

for each BL ∈ Baselearners do
if clustering_enabled then

clusters ← KMeans(X , K )
for each cluster c in clusters do

if valid_cluster(c) then

modelc ← train(ML, BL, Xc, Tc, Yc)
scorec
evaluate_AUUC(modelc, Xc, Tc, Yc)

←

else

skip
end if
end for
clusters ← merge_low_AUUC(clusters)

else

model ← train(ML, BL, X , T , Y )
score ← evaluate_AUUC(model, X , T , Y )

end if
end for

end for

end for

24:
25: end for

Descriptive statistics for our dataset are shown in
Table 4-1. The dataset contains approximately 720,000 user-
months generated from six calendar months. The six-month
window reflects a practical trade-off between behavioral
stability and sample coverage in a real-world lending
system, providing repeated exposure to interventions for
temporal robustness checks while limiting structural drift
in user composition and platform policy. All loans have a
mean utilization rate of 62.8% (SD = 24.5%), indicating
behavioral heterogeneity. An average repayment-timeliness
index of 0.91 reflects a disciplined borrower population.
Approximately 78% of users live in a tier-2 or lower-tier city.
Users in the treatment group appear to exhibit somewhat
higher utilization and higher-frequency engagement than
users in the control group, implying heterogeneous interven-
tion responses relevant for uplift analyses. Feature stability
and relevance diagnostics further affirm the robustness of this
variable set: the average IV across retained features is 0.23,
and the average PSI is 0.07, both within accepted stability
indicators have
bounds [42]. Behavioral and repayment

the strongest predictive power, mirroring previous research
showing that dynamic behavioral attributes are highly pre-
dictive of treatment responsiveness. Correlation diagnostics
confirm that we effectively controlled for multicollinearity.

These procedures ensure that the empirical model iden-
tifies true behavioral heterogeneity rather than confounding
arising from unstable or superfluous predictors. In summary,
the dataset underwent a systematic and judicious filtering and
refinement process consistent with best practices in causal
inference and comparable recent works in the literature.
The resulting analysis environment is stable, representative,
and amenable to estimating heterogeneous treatment effects,
as well as to implementing causal models of users in
subsequent sections.

A. SEGMENTATION AND DISTRIBUTION OF FOUR
RESPONSE TYPES
This section presents the empirical results of the Four-Type
Response Segmentation Module introduced in Chapter 3,
illustrating how uplift-based causal labeling emerges in the
dataset. Within the causal user-profiling framework, users are
segmented based on their Individual Treatment Effect (ITE)
under the potential-outcomes model. In particular, we define
four canonical response types as:

• Persuadables (Type A): perform the target action only

if treated

(y1 = 1, y0 = 0)

• Sure Things (Type B): perform the action regardless of

treatment

(y1 = 1, y0 = 1)

• Lost Causes (Type C): never perform the action

(y1 = 0, y0 = 0)

• Do Not Disturb (Type D): perform the action only if

not treated

(y1 = 0, y0 = 1)

This typology provides conceptual clarity to heterogeneous
behavioral patterns and enables causal modelling, tailored
intervention strategies, and marketing resource allocation to
begin conceptually. In practice, the frequency of types across
users is summarized in Figure 5a. There are significantly
more Persuadables and Lost Causes relative to Sure Things
in the user population, meaning that there are slightly more
people who will change behaviour under some treatment
than will remain the same across any treatment; but the
most observations are of users who are resistant to treatment.
Sure Things should have stable demand, although—as with
everything else—they should be given equal rates of exposure
in the broadest possible sense of the term. Do-Not-Disturb
users are a hindrance, and serve as an indicator of potential
adverse intervention effects, serving as a caution against

VOLUME 14, 2026

40159

---

<!-- PAGE 14 -->

J. Jiang et al.: Dynamic Framework for CUP and Treatment Segmentation via Uplift Modeling

FIGURE 4. Workflow of Data Preprocessing and Variable Selection. Note. The workflow depicts sequential data preparation steps: Raw
Data Collection → Data Cleaning and Missing Value Treatment → Normalization and Standardization → IV Computation → PSI Evaluation
→ Correlation Filtering → Feature Retention for Modeling.

TABLE 6. Descriptive statistics of the sample.

over-targeting and treatment fatigue, even if they constitute
only a small portion of the total cohort.

To make even clearer how this segmentation might
typically be done, Figure 5b plots the empirical
joint
distribution of (y0, y1) and notes the four decision regions as
dictated by the potential-outcomes formulation.

B. EMPIRICAL EVALUATION OF THE CUP FRAMEWORK
This section describes the empirical evaluation of the Causal
User Profiling (CUP) framework. We evaluated each of the
core components of CUP—feature selection, clustering, and
meta-learner configuration—individually and as a combined
system to assess their influence on uplift performance,
as measured by the Area Under the Uplift Curve (AUUC).

1) FEATURE SELECTION AND UPLIFT PERFORMANCE
To explore how variable screening affects heterogeneous
treatment-effect estimation, six feature sets were compared:

ALL — all variables;
IV — selected by information value;
Causal — chosen by causal-forest importance and PSI

stability;

Stepwise — retained through cross-fitted regression;
IV + Causal — intersection of the first two;
IV + Causal + Stepwise — the hybrid refinement.
Findings show that appropriate variable selection is critical
to uplift modeling. Using ALL resulted in the lowest
mean AUUC and the highest variance—it appears that
when the models must learn in the presence of substantial
noise, it severely weakens identification with respect to the
heterogeneous effects themselves.

Both IV and Causal selections produce meaningfully better

results than the baseline, but in different ways:

IV features push the AUUC higher on the simpler meta-

learners (T- and X-Learners),

whereas Causal features assist with overall model stability,

particularly for the larger DR-Learner.

Because benefits come from different sources, it is not
obvious a priori how the responses will sort themselves
out when combining them. The IV + Causal set produces
the overall highest mean AUUC—validating that ‘‘picking
dimensions gives you information gain, and picking good
dimensions gives you causal relevance.’’ Once this outer-join
set of dimensions is added, Stepwise refinement can then
be incorporated. These hybrid sets exhibit slightly lower
mean AUUC but are less volatile month-to-month, yielding
smaller uplift-consistency (UC) indices. Although their mean
AUUC is marginally lower, the ability to depend on the model
producing similar results across months is worth the trade-off
in mean values.
In summary:
IV + Causal accelerates accuracy at the cost of some

stability.

IV + Causal + Stepwise favours stability at the cost of

some accuracy.

The second approach is more deployment-ready and is
therefore used as ‘‘the features’’ moving forward. Across
the meta- and base-learners perform
learners as well,
relatively consistently. Logistic Regression (LR) stands out as
the strongest base learner under the hybrid feature sets, while
tree-based learners show weakness when noise remains in the
embeddings. Therefore, feature selection forms the skeletal
structure for CUP.

2) CLUSTERING STRATEGIES AND AUUC ENHANCEMENT
Clustering was introduced to investigate local
treatment
heterogeneity independent of an explicit association with
outcomes, consistent with the notion that subgroups with
different causal effects can be mapped out by recursive
partitioning [6]. The empirical results suggest that clustering

40160

VOLUME 14, 2026

---

<!-- PAGE 15 -->

J. Jiang et al.: Dynamic Framework for CUP and Treatment Segmentation via Uplift Modeling

FIGURE 5. Empirical distribution of four causal response types (left) and joint distribution of potential outcomes (y0
illustrating ABCD regions (right).

, y1)

is helpful but is conditional rather than absolute, and as a
consequence should be used cautiously.

The contrast between Direct, C1 (Merging), and C2
(Replacement) shows a clear trade-off. The Elbow Method
suggests optimal clusters around K=6, at which point
the silhouette score levels off (see Figure 7a). This is
parsimonious and easy to interpret, and we derive clusters
following this throughout our analysis.

Across the three methods, the C2 step is consistently the
strongest, yielding the highest uplift effect: mean AUUC
(≈ 0.09) with the lowest variance (± 0.01). By ‘‘replacing’’

weak clusters with global predictions, C2 has a regularizing
effect, balancing local adaptivity and global stability. This
variance-reducing characteristic maps onto the findings of
Devriendt et al. [22], who show that ‘‘ensemble-style’’
uplift models produce lower variance (and greater reliability)
than ‘‘isolated’’ two-model structures. In our case, Direct
identifies behavioral heterogeneity but does not produce
stable models. C1 reduces this variance somewhat, but part
of it remains. Empirically, the clustering order is C2 > C1
> Direct (see Figure 7b), placing clustering as a refinement
rather than a requisite.

VOLUME 14, 2026

40161

---

<!-- PAGE 16 -->

J. Jiang et al.: Dynamic Framework for CUP and Treatment Segmentation via Uplift Modeling

FIGURE 6. Evaluation of feature-selection strategies and meta-learner interactions in uplift modeling.
(a) Boxplots of AUUC values across six feature sets, illustrating performance variability across
configurations. (b) Temporal mean AUUC over six months comparing IV + Causal and Step_IV + Causal
feature sets, with the lower panel showing the population standard deviation of AUUC across months
to evaluate temporal stability. (c) Heatmap of Meta-Learner × Feature-Set interactions, showing
average AUUC values for different learner-feature combinations. The DR-Learner achieves the highest
uplift performance under IV + Causal and Step_IV + Causal feature configurations. (d) Standard
deviation of AUUC across paired feature configurations, illustrating the variance-reduction effect of
stepwise refinement.

40162

VOLUME 14, 2026

---

<!-- PAGE 17 -->

J. Jiang et al.: Dynamic Framework for CUP and Treatment Segmentation via Uplift Modeling

Clustering interacts differently with the various meta-
learners. As reflected in Figure 7c, the X-Learner shows
the most robust and consistent improvement, reflecting its
theoretical gain in segmented or unbalanced samples [15].
In contrast, the DR-Learner and T-Learner show AUUC drops
or inconsistencies after clustering, and the Causal Forest
(CF) even experiences extreme performance deterioration.
This is consistent with earlier findings that tree-based causal
estimators lose efficiency when subgroup sample sizes are
small or unbalanced [13], [35] —meta-learners capable of
‘‘cross-arm information sharing’’ (such as the X-Learner)
remain stable under segmentation, whereas others are sen-
sitive to fragmentation. Figure 7d illustrates cluster-level
performance under the X-Learner. As expected, clustering
amplifies both signal and noise: some cluster-level AUUC
values improve substantially, while others drop sharply.
This follows the familiar
‘‘variance-amplifying effect,’’
where smaller subsamples increase both estimation bias and
variance [13]. Thus, clustering uncovers latent heterogeneity
but can also amplify random noise, helping to explain why its
performance varies across datasets and time periods.

The effectiveness of clustering depends critically on the
feature space used. In Figure 7, clustering derived from
the Causal feature set yields the most consistent gains,
outperforming clustering based on IV-only or ALL-variable
feature sets. This indicates that clustering is effective only
when the feature space encodes causally relevant informa-
tion: causal features yield a more coherent and interpretable
map of the underlying terrain, enabling clustering to identify
more precise treatment heterogeneity [43], [44]. To recap:
causal features structure the space, and clustering amplifies
heterogeneity. Clustering based solely on predictive or
correlation-driven variables tends to amplify noise.

Clustering does not universally improve outcomes. It pro-
duces a wide spread in AUUC across clusters; improvement
in some clusters may be accompanied by deterioration in
others. This dual-edged nature makes clustering powerful
but dangerous. Clustering should be viewed as a ‘‘positive
calibration mechanism,’’ effective only when strongly rooted
in causal features and paired with robust learners (such as
the X-Learner) that remain stable under segmentation. Its
feedback on the Four-Type causal segmentation (Persuad-
able, Sure Thing, Lost Cause, Do-Not-Disturb) must also be
monitored, as behavioral balance can be distorted through
subgroup redistribution.

In summary, clustering improves uplift estimation only
‘‘under reasonably complete causal feature structures’’ and
with ‘‘meta-learners that remain stable under segmentation.’’
Clustering performs best with the C2 replacement strategy.
Given that clustering can amplify both gains and volatility,
it should be treated as a calibrated instrument, not as a
mandatory component of every causal user-profiling pipeline.

3) META-LEARNER AND BASE-LEARNER CONFIGURATIONS
A total of sixteen meta/base combinations (four meta-learners
× four base learners) were explored using the optimal feature

set. Among the meta-learners, the DR-Learner consistently
produced the highest mean AUUC, albeit with higher
variance across months, indicating robustness in point perfor-
mance but sensitivity to temporal fluctuations. The X-Learner
treatment-
offers strong competition, particularly under
imbalance situations, whereas the T- and S-Learners are
far more unreliable in complex, high-variance environments.
Among the base learners, Logistic Regression (LR) performs
best in terms of stability and interpretability, while tree-based
learners exhibit substantially more variability overall.

4) OPTIMAL PATHWAY AND OVERALL EFFECT
Putting all these pieces together, the final CUP workflow
uses a hybrid IV + (Causal ∩ Stepwise) feature-selection
design, employs the C2 ‘‘replacement strategy’’ with a
moderate number of clusters K , and adopts a DR-Learner
with Logistic Regression as the modeling configuration. This
integrated pathway yields a large and stable improvement
in AUUC relative to the baseline (‘‘all features + no
clustering + standard learner’’). The main performance
gains come from variables that are informative (high IV)
and causally relevant, and the C2 approach provides a
form of structural regularization that prevents overfitting
and stabilizes heterogeneous treatment estimation. Together,
these components lead to a balanced pipeline that improves
both accuracy and interpretability.

Quantitatively, each module of

the CUP framework
contributes a distinct and measurable improvement to uplift
performance. Feature selection alone increases AUUC by
approximately 25–30%, reflecting the value of filtering
out noisy predictors and emphasizing causally important
variables. Incorporating C2 clustering provides an additional
10–12% gain by stabilizing weak clusters and harmonizing
local heterogeneity with global patterns. Optimizing the
meta/base configuration (DR-Learner + Logistic Regression)
yields a further 5–8% improvement, enhancing robustness
while maintaining interpretability. Cumulatively, the inte-
grated CUP workflow achieves roughly 45–50% higher
AUUC than the standard uplift-modeling baseline, demon-
strating that each component contributes a clear and persistent
increment across the six monthly slices.

V. DISCUSSION
The empirical validation of the framework demonstrates
that causal inference and uplift modelling can be rigorously
brought to bear on user analytics, closing a classic gap in
the analytics space between prediction and intervention. This
section discusses the empirical findings in relation to existing
uplift modeling and user profiling approaches, with emphasis
on stability, interpretability, and operational relevance.

The Causal User Profiling (CUP) framework moves
beyond descriptive or purely predictive profiling by cen-
tering treatment responsiveness as its primary analytical
dimension. This reframing abstracts user modelling from the
question of who users are, to how users behave when acted
on [6] and [22]. This move from correlation to causation

VOLUME 14, 2026

40163

---

<!-- PAGE 18 -->

J. Jiang et al.: Dynamic Framework for CUP and Treatment Segmentation via Uplift Modeling

FIGURE 7. Evaluation of clustering strategies and meta-learner performance under clustered
uplift modeling. (a) Elbow curve based on silhouette scores for selecting the optimal number
of clusters. The silhouette score stabilizes near K = 48, indicating a suitable trade-off
between cluster cohesion and separation. (b) Comparison of clustering strategies (Direct, C1,
C2) using multiple AUUC indicators, including baseline AUUC, weighted AUUC, cluster AUUC,
and extreme cluster AUUC values. Results indicate the performance ranking C2 > C1 >
Direct, with C2 achieving the highest stability and lowest variance. (c) Meta-learner
performance comparison under clustering across months. Results show that the XLearner
demonstrates the most consistent improvement, whereas DR-, T-, and CF-Learners exhibit
greater fluctuations or performance decline.

40164

VOLUME 14, 2026

---

<!-- PAGE 19 -->

J. Jiang et al.: Dynamic Framework for CUP and Treatment Segmentation via Uplift Modeling

FIGURE 7. (Continued). Evaluation of clustering strategies and meta-learner performance under
clustered uplift modeling. (a) Elbow curve based on silhouette scores for selecting the optimal number
of clusters. The silhouette score stabilizes near K = 48, indicating a suitable trade-off between cluster
cohesion and separation. (b) Comparison of clustering strategies (Direct, C1, C2) using multiple AUUC
indicators, including baseline AUUC, weighted AUUC, cluster AUUC, and extreme cluster AUUC values.
Results indicate the performance ranking C2 > C1 > Direct, with C2 achieving the highest stability and
lowest variance. (c) Meta-learner performance comparison under clustering across months. Results
show that the XLearner demonstrates the most consistent improvement, whereas DR-, T-, and
CF-Learners exhibit greater fluctuations or performance decline.

VOLUME 14, 2026

40165

---

<!-- PAGE 20 -->

J. Jiang et al.: Dynamic Framework for CUP and Treatment Segmentation via Uplift Modeling

FIGURE 8. Heatmap showing the mean AAUC values for all Meta-Learner × Base-Learner configurations. Darker cells indicate
higher uplift performance. The DR-Learner combined with Logistic Regression (LR) achieves the highest mean AAUC and lowest
variance, demonstrating the most balanced trade-off between accuracy, stability, and interpretability.

represents a transformation in the conceptual underpinnings
of personalization science, toward a framework that predicts
behaviour while also explaining why effects transpire. The
empirical findings confirm that causal
interpretability is
distinctive in its potential to redefine user segmentation.
Rooted in the potential outcomes framework [11], later aug-
mented into the metalevel framework of meta-learning [15],
CUP quantifies heterogeneous treatment effects through the
four-type response taxonomy of Persuadables, Sure Things,
Lost Causes, and Do-Not-Disturbs [17].

This treatment-aware representation of user behaviour
indicates that the heterogeneity observed in behaviour is
not an artefact of random variation but rather a marker
of differential responsiveness to intervention. In the digital
lending case-study context, these distinctions illustrate how
interventions may activate engagement, reinforce inevitable
outcomes, protect users from unnecessary actions, or respect
non-responsiveness. Compared with conventional uplift
ranking accuracy
modeling pipelines
alone, CUP aligns estimation, evaluation, and response
interpretation within a unified analytical framework, yielding
more stable gains under repeated interventions.

emphasize

that

A first salient

insight from the results concerns the
interrelationship between feature quality, model stability,
and causal validity. The hybrid feature selection strategy—
combining Information Value (IV), Causal Forest impor-
tance, and Stepwise refinement—produced the most stable
uplift performance across monthly samples. This observation
confirms the argument that causal estimation depends as
much on data stability and regime design as on algorithmic
sophistication [6]. High-IV variables ensure that the model
learns from information-rich dimensions; causal importance
anchors relevance to treatment effects; and Stepwise selection
serves as a form of variance regularization. Together, these
components yield a ‘‘causal feature space’’ that balances
predictive strength with generalizable structural characteris-
tics. This finding reinforces the notion of ‘‘data refinement’’
[4], consistent with evidence in causal machine learning
that emphasizes disciplined feature design over increasing
algorithmic complexity.

A second insight relates to methodological integration,
which contributes directly to the robustness of CUP. Rather
than operating as isolated modules, feature selection, clus-
tering, and causal estimation work synergistically. The C2
replacement strategy compensates for unstable clusters by
substituting their predictions with those of the global model,
producing a hierarchical regularization effect that maintains
local sensitivity while ensuring global consistency [4]. Within
this structure, the Doubly Robust (DR) Learner combined
with Logistic Regression (LR) delivers a favourable balance
between robustness and interpretability. While alternative
configurations such as the X-Learner may perform well under
certain imbalance conditions,
the DR–LR configuration
demonstrated greater
temporal stability across repeated
deployments, which is essential in operational environments.
From a practical perspective, CUP grounds causal rea-
soning in consequences experienced by decision-makers.
By estimating conditional
treatment effects rather than
predictive probabilities, the framework enables intervention
design based on causal evidence rather than intuition or corre-
lation. Empirically, the sequential stacking of methodological
components yields meaningful and interpretable gains in
performance:

• Hybrid feature selection improves AUUC by approxi-

mately 25–30% over the baseline;

• Clustering contributes an additional 10–12% through the

C2 refinement strategy;

• The DR-Learner + LR configuration adds a further

5–8% uplift.

Cumulatively, the full CUP pipeline achieves an approxi-
mately 45–50% improvement in model performance relative
to conventional profiling approaches. More importantly,
these gains persist across multiple time windows, indicating
systematic rather than incidental
improvements. From a
computational standpoint, the runtime of CUP is dominated
by base learner training and clustering stages and introduces
no additional asymptotic complexity beyond standard uplift
modeling pipelines, making it tractable for large-scale tabular
datasets.

40166

VOLUME 14, 2026

---

<!-- PAGE 21 -->

J. Jiang et al.: Dynamic Framework for CUP and Treatment Segmentation via Uplift Modeling

FIGURE 9. Cumulative gain curves comparing the optimized CUP pathway with the baseline; the CUP
curve uniformly dominates.

VI. LIMITATIONS OF THE STUDY
this study has several
Despite its empirical strengths,
limitations. First,
the analysis is based on data from a
single digital lending platform. While this enables controlled
evaluation under realistic operational conditions, it limits

external generalizability. Future research should assess CUP
across additional domains such as e-commerce, insurance,
and public finance to evaluate cross-context robustness.

Second, the treatment variable aggregates heterogeneous
interventions (e.g., coupons, credit-line increases, outbound

VOLUME 14, 2026

40167

---

<!-- PAGE 22 -->

J. Jiang et al.: Dynamic Framework for CUP and Treatment Segmentation via Uplift Modeling

calls), which may obscure intervention-specific behavioural
mechanisms. Extending CUP to explicit multi-treatment or
dynamic intervention settings would enable finer-grained
analysis of intervention-specific causal effects.

Third, the evaluation emphasizes temporal consistency
across six monthly deployments rather than formal statistical
hypothesis testing. This design choice reflects an operational
focus on stability and reproducibility but may limit inference
in settings that require formal significance testing.

Finally, issues of fairness, transparency, and ethical deploy-
ment warrant further attention. Incorporating fairness-aware
learning and causal explainability into CUP represents an
important direction for future work, particularly in sensitive
financial applications [1], [4].

VII. CONCLUSION AND FUTURE WORK
This study contributes to the growing literature on causal
analytics by positioning causality as the organizing principle
of user profiling. We propose Causal User Profiling (CUP),
an integrated pipeline that combines feature selection,
clustering, and meta-learning into a reproducible and inter-
pretable workflow that connects causal estimation with
actionable decision-making.

it

Empirically, CUP captures heterogeneous treatment effects
reframes user
with temporal stability; conceptually,
the causal understanding of behavioural
profiling as
response; and practically, it provides a scalable foundation
for treatment-aware strategies in diverse digital ecosystems.
Rather than competing with predictive machine learning,
CUP complements it by explaining why interventions
work and for whom, advancing personalization from
outcome prediction toward causal understanding and decision
optimization.

ACKNOWLEDGMENT
This study benefited from the Haier Group Digital Finance
Innovation Initiative (which provided the access to data and
computer resources for empirical validation of our proposed
model), and the authors are especially grateful to them for the
implementation of the CUP.

DATA AVAILABILITY STATEMENT
The dataset used in this study is subject to institutional
and commercial restrictions and therefore cannot be publicly
released at
this time. Aggregated statistics and derived
experimental results are reported in the manuscript.

The authors plan to release a reproducibility package,
including synthetic data examples and representative code
implementations, subject to data-sharing approval in future
work.

APPENDIX A
RESPONSE-TYPE LABEL CONSTRUCTION AND
CONSISTENCY
Response-type labels in CUP are constructed to reflect
both estimated treatment effects and observed behavioral

outcomes, ensuring causal interpretability while maintaining
temporal stability.

For each deployment period, uplift scores are first
estimated using the selected meta-learner configuration.
High-confidence uplift thresholds are applied to identify
users with strong positive or negative estimated treatment
effects. These uplift-based signals are then cross-validated
against observed (T , Y ) realizations to refine response-type
assignments and to prevent logically inconsistent labels.

Specifically, Persuadables and Do-Not-Disturb users are
identified through a combination of uplift magnitude and
treatment-outcome alignment, while Sure Things and Lost
Causes are distinguished based on behavioral invariance
with respect to treatment exposure. This two-stage procedure
mitigates label noise arising from estimation uncertainty
and ensures that response categories remain behaviorally
meaningful.

To

across

promote

consistency

time windows,
response-type definitions are held fixed, while individual
users are allowed to transition between response states as their
behavior evolves. This design yields stable population-level
semantics while preserving individual-level dynamics under
repeated interventions.

APPENDIX B
C2 REPLACEMENT STRATEGY
In the CUP framework, clustering is treated as a flexible
and corrective component rather than a hard segmentation
step. Clustering is performed at the individual level, while
model evaluation and stability assessment are conducted
across monthly deployment windows to reflect system-level
performance under repeated interventions.

After initial clustering, uplift performance is evaluated
at the cluster level and compared against a non-clustered
(Direct) baseline using the same monthly evaluation protocol.
Cluster-based prediction paths that exhibit unstable or
inferior uplift performance relative to the Direct global model
are not propagated to downstream response-type assignment.

This comparison gives rise to three evaluation paths:

• Direct: uplift estimation without clustering;
• C1: uplift estimation within clusters;
• C2: cluster-level evaluation followed by fallback to
Direct predictions when clustering degrades stability or
performance.

Rather than enforcing cluster-specific predictions at the
individual level, the C2 strategy operates as a path-level
regularization mechanism. It preserves cluster-based hetero-
geneity when beneficial, while reverting to the global model
when clustering introduces noise or instability.

APPENDIX C
ABLATION ANALYSIS DESIGN
The purpose of the ablation analysis in this study is not to
conduct formal hypothesis testing, but to assess the relative

40168

VOLUME 14, 2026

---

<!-- PAGE 23 -->

J. Jiang et al.: Dynamic Framework for CUP and Treatment Segmentation via Uplift Modeling

contribution and stability of individual components within the
CUP pipeline under repeated real-world deployments.

selected data summaries or code components may be made
available.

Each ablation experiment removes or modifies one com-
ponent of the framework while keeping all others fixed.
Performance differences are evaluated consistently across
six consecutive monthly datasets, allowing assessment of
whether observed effects persist over time rather than arising
from a single snapshot.

Given the operational nature of the study and the use
of large-scale observational data, emphasis is placed on
temporal consistency and the magnitude of performance
differences rather than formal statistical significance testing.
This design provides empirical evidence on whether observed
gains are systematic and reproducible under repeated inter-
vention settings.

APPENDIX D
FEATURE SCREENING AND SCALING STRATEGY
Feature preprocessing in CUP is designed to enhance
numerical comparability, stability, and causal relevance prior
to model estimation, rather than to optimize predictive
accuracy through aggressive normalization or transformation.
Before model fitting, all candidate covariates undergo
a unified screening process to ensure consistency across
downstream feature configurations. Continuous variables are
rescaled to a common numerical range to improve compara-
bility across features with heterogeneous magnitudes and to
facilitate stable optimization in subsequent modeling stages.
This rescaling is applied uniformly and does not alter the rel-
ative ordering or distributional shape of individual features.

that

combines

complementary

Feature selection proceeds through a diagnostic multi-stage
procedure
criteria:
(i) information-based screening to retain variables with suffi-
cient outcome relevance, (ii) causal importance assessment
to identify features consistently associated with treatment
effects across time windows, and (iii) stepwise refinement
to control redundancy and variance inflation.

Importantly, this screening stage is performed prior to
constructing downstream feature-set configurations (e.g.,
information-based, causal-based, or hybrid sets), ensuring
that all reported models draw from a common pool of
filtered and stability-checked covariates. This design avoids
feature-induced confounding when comparing alternative
model specifications and promotes reproducibility under
repeated deployment.

APPENDIX E
COMPUTATIONAL CONSIDERATIONS
The empirical study was conducted using large-scale obser-
vational data from a real-world digital lending platform. Due
to the involvement of sensitive customer-level financial infor-
mation, the underlying dataset cannot be publicly released
at this stage. Data access was granted under institutional
collaboration and confidentiality agreements, and results are
reported in aggregated and anonymized form. Subject to
future approval and appropriate de-identification protocols,

From a computational perspective, the CUP framework
is designed to remain tractable for large tabular datasets.
The dominant computational costs arise from repeated
uplift model estimation, causal
feature screening, and
clustering-based analyses across multiple monthly deploy-
ments. While no additional asymptotic complexity is intro-
duced beyond standard uplift modeling pipelines, the cumu-
lative experimental workload is substantial due to the breadth
of model configurations and ablation settings evaluated.

In this study, extensive ablation experiments and stability
checks were prioritized to assess robustness under repeated
deployment. As a result, certain algorithmic choices—such as
the selection of clustering methods and base learners—reflect
a deliberate trade-off between methodological coverage
and feasible computational execution under single-machine
constraints.

Future work will extend the CUP framework to incorporate
additional feature selection strategies, uplift estimators, and
clustering algorithms as computational resources permit.
These extensions are expected to further enrich comparative
analysis without altering the core methodological principles
established in the present study.

REFERENCES

[1] E. Rich, ‘‘User modeling via stereotypes,’’ Cognit. Sci., vol. 3, no. 4,

pp. 329–354, 1979.

[2] G. Adomavicius and A. Tuzhilin, ‘‘Toward the next generation of
recommender systems: A survey of the state-of-the-art and possible
extensions,’’ IEEE Trans. Knowl. Data Eng., vol. 17, no. 6, pp. 734–749,
Jun. 2005, doi: 10.1109/TKDE.2005.99.

[3] P. Brusilovsky and E. Millán, ‘‘User models for adaptive hypermedia and
adaptive educational systems,’’ in The Adaptive Web. Cham, Switzerland:
Springer, 2007, pp. 3–53.

[4] C. I. Eke, A. A. Norman, and W. Ozuem, ‘‘User profiling in personalized
recommender systems: A systematic review,’’ IEEE Access, vol. 7,
pp. 146923–146940, 2019, doi: 10.1109/ACCESS.2018.2887321.

[5] D. Mirylenka, F. Ricci, and L. Rokach, ‘‘User modeling and personaliza-
tion,’’ in Recommender Systems Handbook. New York, NY, USA: Springer,
2019, doi: 10.1145/3357384.3357818.

[6] S. Athey and G. Imbens, ‘‘Recursive partitioning for heterogeneous causal
effects,’’ Proc. Nat. Acad. Sci. USA, vol. 113, no. 27, pp. 7353–7360,
Jul. 2016, doi: 10.1073/pnas.1510489113.

[7] F. Purificato, A. Rago, A. Belkhir, P. Lanzini, and P. Cirillo, ‘‘Deep
causal models: A survey,’’ Inf. Process. & Manag., vol. 61, no. 3, 2024,
Art. no. 103579, doi: 10.1016/j.ipm.2023.103579.

[8] W. Wu, F. Yuan, J. Huang, X. Yu, and M. Zhang, ‘‘Social-network-based
user profiling: A survey,’’ Inf. Sci., vol. 648, Oct. 2024, Art. no. 119021,
doi: 10.1016/j.ins.2024.119021.

[9] J. Pearl, Causality: Models, Reasoning, and Inference, 2nd ed., Cambridge,

U.K.: Cambridge Univ. Press, 2009, doi: 10.1017/CBO9780511803478.

[10] M. A. Hernán and J. M. Robins, Causal Inference: What If. London, U.K.:

Chapman & Hall, 2020, doi: 10.1201/9780429259654.

[11] D. B. Rubin, ‘‘Estimating causal effects of treatments in randomized and
nonrandomized studies,’’ J. Educ. Psychol., vol. 66, no. 5, pp. 688–701,
Oct. 1974, doi: 10.1037/h0037350.

[12] G. W. Imbens and D. B. Rubin, Causal Inference for Statistics, Social, and
Biomedical Sciences. Cambridge, U.K.: Cambridge Univ. Press, 2015, doi:
10.1017/CBO9781139025751.

[13] S. Wager and S. Athey, ‘‘Estimation and inference of heterogeneous
treatment effects using random forests,’’ Biometrika, vol. 105, no. 2,
pp. 287–301, 2018, doi: 10.1093/biomet/asx045.

VOLUME 14, 2026

40169

---

<!-- PAGE 24 -->

J. Jiang et al.: Dynamic Framework for CUP and Treatment Segmentation via Uplift Modeling

[14] X. Nie and S. Wager,

‘‘Quasi-oracle estimation of heterogeneous
treatment effects,’’ Ann. Statist., vol. 49, no. 6, pp. 3935–3963, 3935, doi:
10.1214/20-AOS1964.

[15] S. R. Künzel, J. S. Sekhon, P. J. Bickel, and B. Yu, ‘‘Metalearners for
estimating heterogeneous treatment effects using machine learning,’’ Proc.
Nat. Acad. Sci. USA, vol. 116, no. 10, pp. 4156–4165, Mar. 2019, doi:
10.1073/pnas.1804597116.

[16] S. Athey, J. Tibshirani, and S. Wager, ‘‘Generalized random forests,’’
Ann. Statist., vol. 47, no. 2, pp. 1148–1178, Jan. 2019, doi: 10.1214/18-
AOS1709.

[17] N. J. Radcliffe and P. D. Surry, ‘‘Uplift modelling with significance-based

trees,’’ Stochastic Solutions, London, U.K., Tech. Rep., 2011.

[18] P. Rzepakowski and S. Jaroszewicz, ‘‘Decision trees for uplift modeling
with single and multiple treatments,’’ Knowl. Inf. Syst., vol. 32, no. 2,
pp. 303–327, Aug. 2012, doi: 10.1007/s10115-011-0434-0.

[19] P. Gutierrez and J. Y. Gérardy, ‘‘Causal inference and uplift modelling: A
review of the literature,’’ Inf. Sci., vol. 420, pp. 590–598, Jun. 2017, doi:
10.1016/j.ins.2017.02.002.

[20] N. J. Radcliffe, ‘‘Using control groups to target on predicted lift,’’

Stochastic Solutions, London, U.K., Tech. Rep., 2007.

[40] N. Hu, ‘‘Heterogeneous treatment effects analysis for social scientists:
A review,’’ Social Sci. Res., vol. 109, Jan. 2023, Art. no. 102810, doi:
10.1016/j.ssresearch.2022.102810.

[41] Z. Zhang, P. Zhao, X. Li, and Y. Liu, ‘‘Causal representation learning,’’ in
Proc. KDD, 2021, pp. 2663–2673, doi: 10.1145/3447548.3467381.
[42] A. M. Alaa and M. V. D. Schaar, ‘‘Limits of estimating heterogeneous
treatment effects: Guidelines for practical algorithm design,’’ IEEE Trans.
Neural Netw. Learn. Syst., pp. 129–138, Jan. 2018.

[43] X. Guo, K. Yu, L. Liu, F. Cao, and J. Li, ‘‘Causal representation
learning: A survey,’’ Artif. Intell., vol. 320, Nov. 2024, Art. no. 104072,
doi: 10.1016/j.artint.2024.104072.

[44] Z. Zhang, P. Zhao, X. Li, and Y. Liu, ‘‘Deep causal models for ITE
estimation: A survey,’’ ACM Comput. Surv., vol. 55, no. 12, pp. 1–38, 2023,
doi: 10.1145/3527154.

[21] M. Jaskowski and S. Jaroszewicz,

‘‘Uplift modeling for clinical
ICDM Workshops, 2012, pp. 17–23, doi:

trial data,’’
10.1109/ICDMW.2012.103.

in Proc.

[22] F. Devriendt, D. Moldovan, and W. Verbeke, ‘‘A literature survey and
experimental evaluation of the state-of-the-art in uplift modeling: A
stepping stone toward the development of prescriptive analytics,’’ Big
Data, vol. 6, no. 1, pp. 13–41, Mar. 2018, doi: 10.1089/big.2017.0104.

[23] Z. Zhang, P. Zhao, X. Li, and Y. Liu, ‘‘Deep causal models: Taxonomy and

roadmap,’’ ACM Comput. Surveys, vol. 56, no. 3, pp. 1–36, 2024.

[24] J. Chen, Y. Wang, and X. Li, ‘‘A survey of user profiling: State-of-the-
art, challenges and solutions,’’ Inf. Process. Manage., vol. 61, no. 2, 2024,
Art. no. 103676, doi: 10.1016/j.ipm.2023.103676.

[25] F. Devriendt, D. Moldovan, and W. Verbeke, ‘‘Prescriptive analytics
through uplift modeling: A review,’’ Inf. Fusion, vol. 73, pp. 67–86,
Sep. 2021, doi: 10.1016/j.inffus.2021.02.003.

[26] U. Shalit, F. D. Johansson, and D. Sontag, ‘‘Estimating individual treatment
effect: Generalization bounds and algorithms,’’ in Proc. 34th Int. Conf.
Mach. Learn., 2017, pp. 3076–3085.

[27] C. Shi, D. M. Blei, and V. Veitch, ‘‘Adapting neural networks for causal

inference,’’ 2019, arXiv:1905.12776.

[28] J. Yoon, J. Jordon, and M. Van Der Schaar, ‘‘GANITE: Estimating

individualized treatment effects,’’ 2018, arXiv.1806.04968.

[29] D. Olaya, H. Ponce, M. A. Gutiérrez-Andrade, and O. Martínez-Velázquez,
‘‘Multi-treatment uplift modeling,’’ in Proc. KDD, 2020, p. 106533, doi:
10.1145/3394486.3403196.

[30] K. Lee and J. Berger,

‘‘Cross-treatment gain surface and multi-
treatment uplift,’’ Inf. Sci., vol. 694, Jan. 2024, Art. no. 119240, doi:
10.1016/j.ins.2024.119240.

[31] J. L. Hill, ‘‘Bayesian nonparametric modeling for causal inference,’’ Stat.

Sci., vol. 26, no. 1, pp. 1–27, 2011, doi: 10.1214/11-STS367.

[32] P. R. Hahn, J. S. Murray, and C. M. Carvalho, ‘‘Bayesian regression
tree models for causal
inference: Regularization, confounding, and
heterogeneous effects (with discussion),’’ Bayesian Anal., vol. 15, no. 3,
pp. 965–1056, Sep. 2020, doi: 10.1214/19-ba1195.

[33] M. Dudik, J. Langford, and L. Li, ‘‘Doubly robust policy evaluation and

learning,’’ 2011, arXiv:1103.4601.

[34] J. Rehill,

‘‘A gentle

introduction to uplift modelling,’’ 2024,

arXiv.2403.03822.

[35] T. Inoue, K. Yamamoto, and T. Okuno, ‘‘Machine-learning-based het-
erogeneous treatment effect estimation in randomized trials: A PRISMA
review,’’ Trials, vol. 25, no. 134, pp. 1–21, 2024, doi: 10.1186/s13063-
024-07943-0.

[36] C. Ling, D. Sutherland, F. Johansson, and J. Wiens, ‘‘Causal inference

pipelines for RCT emulation,’’ 2023, arXiv.2302.03070.

[37] A. Maraj, M. Vuković, and D. Hotovec, ‘‘A systematic review of uplift
modeling,’’ Inf. Process. Manag., vol. 61, no. 2, 2024, Art. no. 103692,
doi: 10.1016/j.ipm.2023.103692.

[38] P. R. Rosenbaum and D. B. Rubin,

the
propensity score,’’ Biometrika, vol. 70, no. 1, pp. 41–55, 1983, doi:
10.1093/biomet/70.1.41.

‘‘The central

role of

[39] A. Caron, G. Baio, and I. Manolopoulou, ‘‘Estimating individual treatment
effects using non-parametric regression models: A review,’’ J. Roy. Stat.
Soc. Ser. A, Statist. Soc., vol. 185, no. 3, pp. 1115–1149, Jul. 2022, doi:
10.1111/rssa.12824.

JIANQING JIANG is currently pursuing the
Ph.D. degree with the Institute for Mathematical
Research (INSPEM), Universiti Putra Malaysia.
His research lies at the intersection of user pro-
filing, causal machine learning, uplift modeling,
and heterogeneous treatment effect estimation,
with a particular focus on dynamic user profiling
and personalized intervention design. He has
more than seven years of industry experience in
data science and business intelligence, holding
professional roles in China and Singapore in credit analytics, customer
modeling, and enterprise data systems. Prior to his Ph.D. studies, he was
a Senior Data Scientist developing credit scoring models, customer
segmentation frameworks, and large-scale data governance platforms. His
inference with behavioral modeling
current research integrates causal
to improve decision-making in internet
lending and other high-stakes
operational environments.

NOR ASILAH WATI ABDUL HAMID (Senior
Member, IEEE) received the Ph.D. degree in com-
puter science from The University of Adelaide,
Australia, in 2008.

From 2013 to 2015, she was a Visiting Scholar
with the High Performance Computing Labora-
tory, The George Washington University, USA.
In 2015, she was awarded the CUDA Teaching
Centre recognition by NVIDIA and subsequently
established the CUDA Laboratory at her faculty.
She is currently the Deputy Director of the Institute for Mathematical
Research (INSPEM), Universiti Putra Malaysia. She is also an Associate
Professor with the Department of Communication Technology and Network,
Faculty of Computer Science and Information Technology. She has authored
or co-authored more than 80 journal articles and conference papers. Her
research has been supported by both government and industry funding, with
interests focused on parallel and distributed high-performance computing,
cloud computing, and data-intensive computing.

Dr. Abdul Hamid is the Editor-in-Chief of Malaysian Journal of
Mathematical Sciences and serves as a reviewer for several well-regarded
journals and international conference proceedings.

40170

VOLUME 14, 2026

---

<!-- PAGE 25 -->

J. Jiang et al.: Dynamic Framework for CUP and Treatment Segmentation via Uplift Modeling

NG KENG YAP (Senior Member, IEEE) received
the B.Sc. and M.Sc. degrees in computer science
from Universiti Putra Malaysia, in 2001 and 2005,
respectively, and the Ph.D. degree in computer
science from The University of Manchester, U.K.,
in 2015. He is currently a Senior Lecturer with
the Faculty of Computer Science and Information
Technology, Universiti Putra Malaysia. He has
authored articles in IEEE ACCESS and other indexed
journals. He has been involved in multiple research
projects, including studies on palm oil production analytics, traffic flow
analysis, and disruptive technology in construction project management.
His research interests include software components, business analytics, and
software engineering for artificial intelligence (SE4AI) systems.

CHOO WEI CHONG received the bachelor’s
degree in science (statistics) and the Master’s of
Science degree in business statistics from Univer-
siti Putra Malaysia (UPM), and the Ph.D. and Post-
doctoral degrees in management studies/decision
science from the University of Oxford, U.K. He is
currently an Associate Professor with the School
of Business and Economics, UPM. His research
focuses on volatility modeling, high-frequency
financial data, machine learning–econometrics
hybrid forecasting, text-based analytics, and AI applications in healthcare
and tourism.

VOLUME 14, 2026

40171

<!-- MARKITDOWN CONVERSION -->

<!-- Full MarkItDown conversion for formatting fidelity. -->

Received30January2026,accepted1March2026,dateofpublication5March2026,dateofcurrentversion17March2026.
DigitalObjectIdentifier10.1109/ACCESS.2026.3670857
A Dynamic Framework for Causal User Profiling
and Treatment Segmentation via Uplift Modeling
in Internet Lending
JIANQINGJIANG 1,NORASILAHWATIABDULHAMID 1,2,(SeniorMember,IEEE),
NGKENGYAP 1,2,(SeniorMember,IEEE),ANDCHOOWEICHONG3
1InstituteforMathematicalResearch(INSPEM),UniversitiPutraMalaysia(UPM),Serdang,Selangor43400,Malaysia
2FacultyofComputerScienceandInformationTechnology,UniversitiPutraMalaysia(UPM),Serdang,Selangor43400,Malaysia
3SchoolofBusinessandEconomics(SBE),UniversitiPutraMalaysia(UPM),Serdang,Selangor43400,Malaysia
Correspondingauthor:ChooWeiChong(wcchoo@upm.edu.my)
ABSTRACT The growth of internet lending has created a need for decision frameworks based on
models that are both personalized and causally interpretable. Conventional uplift models detect treatment
responsiveness without recognizing user heterogeneity, the temporal consistency of user behavior, or the
upstream design choices that carry important causal implications. This paper proposes an integrated and
reproducible Causal User Profiling (CUP) framework that combines causal inference, uplift modeling,
and response-based segmentation within a single pipeline. CUP realizes treatment-effect heterogeneity
throughafour-typeresponsetaxonomy(Persuadable,SureThing,LostCause,Do-Not-Disturb)andembeds
it in a multi-stage pipeline involving hybrid feature selection (Information Value (IV), Causal Forest
importance,PopulationStabilityIndex(PSI)stability,andStepwiserefinement),stratifiedclusteringwith
a ‘‘C2 replacement strategy,’’ and meta-learning via both the X-Learner and the Doubly Robust (DR)
Learner using Logistic Regression (LR). A component-wise ablation analysis finds that feature selection
increases AUUC by 25–30%, C2 clustering by 10–12%, and the DR-Learner + LR by another 5–8%.
Overall, the integrated CUP framework yields 45–50% higher AUUC than the baseline (‘‘all features +
no clustering + standard learner’’) while retaining behaviorally coherent and temporally stable insights.
Methodologically,weprovide:1)anend-to-endcausaluserprofilingframeworkthatinteroperatesprofiling,
causal estimation, clustering, and uplift evaluation; 2) a behaviorally and causally consistent response
segmentation mechanism grounded in the potential-outcomes model; and 3) a reproducible experimental
design that quantifies pipeline-level uplift gains through systematic ablation. Applied to large-scale
internet-lending data, CUP reveals opportunities for treatment-aware personalization, enabling financial
institutions to target Persuadables, support Sure Things, and avoid disturbing Do-Not-Disturbs based on
causalevidence.
INDEX TERMS C2 clustering strategy, causal precision, causal user profiling, decision support systems,
DR-learner, feature selection, heterogeneous treatment effects, internet lending, meta-learners, response
segmentation,upliftmodeling,X-learner.
I. INTRODUCTION In this tussle, user profiling [1], [2], [3]—the process
The rapid evolution of digital platforms has heightened of acquiring, analyzing, and organizing multi-dimensional
the importance of personalization and targeting, shifting user data to create static and/or dynamic user profiles or
attentiontowardcoreaspectsofdata-drivendecision-making. models of the user’s behaviors, tastes, preferences, and
otherdemographics—isfoundationaltodata-drivensystems.
The associate editor coordinating the review of this manuscript and Profiling helps design interpretable user representations
approvingitforpublicationwasDiegoBellan . that drive downstream applications such as recommender
2026TheAuthors.ThisworkislicensedunderaCreativeCommonsAttribution4.0License.
VOLUME14,2026 Formoreinformation,seehttps://creativecommons.org/licenses/by/4.0/ 40147

J.Jiangetal.:DynamicFrameworkforCUPandTreatmentSegmentationviaUpliftModeling
systems,targetedmarketing,andriskassessment[4],[5]but In practical internet lending systems, interventions such
conventional profiling pipelines are observational in nature, as interest coupons, fee reductions, credit line adjustments,
concerned with who the user is instead of how the user and targeted reminders are routinely deployed to influence
would react if acted upon [6], and almost entirely ignore user borrowing behavior. When such actions are guided
causation [7], relegating them to use-case-specific opaque solelybypredictivemodelsorrawtreatment-effectestimates,
modelscomponents[8]. platforms may repeatedly allocate incentives to users who
Duringthesameperiod,ashiftinthewaythefieldthought would borrow regardless of intervention, while failing to
aboutthephrase‘‘learningfromdata’’influencedhowdata— activate users who are truly responsive to targeted actions.
used for the targeted deployment of algorithms—came to Moreover, these interventions are often applied repeatedly
beconceptualized.Awidelyusedformulationcharacterizes under budget and risk constraints, making it difficult to
learningfromdataastheprocessinwhich‘‘aprogramissaid translateheterogeneoustreatmenteffectestimatesintostable,
tolearnfromexperienceEwithrespecttosomeclassoftasks interpretable,anddecision-aligneduserrepresentations.
T and performance measure P if its performance at tasks in Concurrently with the emerging HTE literature, uplift
T, as measured by P, improves with experience E.’’ While modeling first arose in applied domains such as marketing,
predictivepowerinanalyticsisimpressive,machinelearning healthcare, and finance to directly estimate incremental
(ML)algorithmsarelimitedbythefactthatmakingdecisions impact: the difference between the probability of response
canchangetheverydistributionoftheoutcomesonewishes fromagroupexposedtotreatmentandthatofacomparable
to predict [9]. In many situations, prediction is insufficient, group not exposed [17]. In practical terms, this quantity
andoneneedstounderstandthecausalstructureoftheworld answers how much more likely a user is to respond
because interventions change the distribution of data [10]. as a direct result of an intervention, rather than due to
It is this limitation that led to additional research on causal baseline propensity. Uplift models [18], [19] that focus on
inference,definedas‘‘thestudyoftherelationshipbetween modelingthe‘‘treatmenteffectinduced,’’ratherthanoverall
cause and effect’’ [9], which also extensively informs predictiveaccuracy,canemploytree-basedapproaches.The
decision-makingsinceMLnecessarilyrestrictsitspowerby ‘‘four-type’’ consumer classes—Persuadables, Sure Things,
learning only patterns instead of, for instance, generating Lost Causes, and Do-Not-Disturbs—serve as the concep-
causalrelationsforitspredictions.Causalinferencehastwo tual framework for studying individual causal response
paradigms which can inform solutions to these problems. [20], [21], [22]. This taxonomy is widely used to align
The first is the potential outcomes framework, where ‘‘the incremental-effect estimation with operational targeting,
causal effect of a treatment on a unit is the difference because it distinguishes true incremental responders (Per-
between the outcome when the unit receives the treatment suadables) from always-responders (Sure Things), never-
and the outcome when the unit does not’’ [11]. The responders (Lost Causes), and users for whom treatment
second is ‘‘the process of using data together with causal may be harmful (Do-Not-Disturbs). [20], [21], [22] Uplift
assumptions to answer questions about causal relations— modeling evaluates targeting strategies against metrics such
such as predicting the effect of interventions or explaining asAreaUndertheUpliftCurve(AUUC)andQinicoefficient,
observed dependencies’’ [9]. The first provides a coherent which capture the incremental gain produced [17], [19].
underpinning for counterfactual reasoning [12], and the Recentlyconducted reviewswarn thatuplift performanceis
secondprovidesmodelsforreasoningqualitativelyaboutthe verysensitivetoupstreamdesignchoices—featureselection,
data-generatingprocessandiscriticalforthetransportability clustering,andlabeling—andthatthevalueofanintegrated
ofcausalknowledge[9].Thesynthesisofthetwoisclear:‘‘by and transparent pipeline is greater than isolated model and
leveraging causal inference, you go beyond description and algorithmcomparisons[8],[22].
association,’’beingabletoaskwhatalternativeactionswould Yet, ‘‘traditional’’ user profiling continues to follow the
do under differing situations [10]. These advances form the predictable, descriptive steps of data collection, normal-
basis of heterogeneous treatment effect (HTE) estimation, ization and cleansing, feature extraction, clustering, and
which directly focuses on individual-level responsiveness performanceevaluation.Theprimarygoalremainspredictive
to interventions [6], [13], [14]. In this line of work, segmentation and operational classification [4], [23], [24].
Causal Trees reveal treatment heterogeneity using recursive Currentprofilingsystems,effectiveastheyareforprediction,
partitioning[6],andCausalForestsextendthismethodology, are not designed to estimate how users would respond to
resultinginconsistentConditionalAverageTreatmentEffects interventions, nor do they derive properties from causal
(CATEs) [13]. Meta-learners (e.g., S-, T-, X-, and R- heterogeneity [7]. From the perspective of profiling, causal
learners) [15] reformulate the causal estimation task into reasoning has not yet been embedded into an end-to-end
modularsupervised-learningsettingsthatallowforflexibility analysis pipeline, and we ask three broad methodology
and scalability across data environments [15]. Beyond questions: (i) how to design new AAUC-driven response
estimation, policy learning integrates causal inference with segmentation, where labeling both informs and determines
decision-making contexts, creating decision rules from evaluation; (ii) how to integrate feature selection, stratified
estimatesoftreatmenteffects[16]. clustering, bias adjustment, and treatment-effect estimation
40148 VOLUME14,2026

J.Jiangetal.:DynamicFrameworkforCUPandTreatmentSegmentationviaUpliftModeling
into a new unified causal user profiling workflow; and (iii) II. RELATEDWORK
how to measure the marginal contribution of each pipeline A. UPLIFTMODELINGANDEVALUATION
componentthroughcomponent-wiseablationanalysis[22]. Uplift modeling—also referred to as incremental response
This work intends to close these gaps by introducing a modeling—reconceptualizes prediction as the estimation
unified method called Causal User Profiling (CUP), inte- of differential treatment response, emphasizing the causal
gratinguserprofiling,causalinference,andupliftmodeling effect of an intervention rather than its absolute outcome
into a single analysis process, building on the previous level.Incontrasttoconventionalpredictivemodeling,which
descriptive roadmap but embedding causal estimation and estimates the likelihood of an outcome, uplift modeling
uplift-based evaluation into its core. Conceptually, it allows explicitly focuses on the change in outcome probability
causal reasoning to take form inside profiling methods, attributable to an action. As Radcliffe and Surry [17] state,
stating not only who users are, but how they respond to uplift defines the notion of ‘‘the difference in response
actionsperformedonthem[25]. rates attributable to a treatment’’ that ‘‘shifts analytics from
Wesummarizethreecontributions: descriptive prediction into the prescriptive space.’’ Early
(1) Causal User Profiling Framework. We propose an approachesadoptedatwo-modelstrategy,inwhichseparate
integrated methodological framework that connects feature predictivemodelsaretrainedfortreatedanduntreatedgroups,
selection, clustering, confounding adjustment, and causal andthedifferenceisinterpretedastheincrementaleffect[20].
effect estimation into a coherent causal user profiling Althoughsimpletoconceptualize,two-modelapproachescan
pipeline. be unstable and lead to biased estimates when treatment
(2) AAUC-Driven Post-Evaluation Response Segmenta- allocationisimbalancedorwhencovariatedistributionsdiffer
tion. We develop a performance-based segmentation mech- substantiallyacrossgroups.
anism that classifies users into the four causal response A significant methodological advance arrived with
types (Persuadables, Sure Things, Lost Causes, and Do- tree-based uplift models, which introduced recursive parti-
Not-Disturbs) based on AAUC results, bridging model tioning to seek maximum treatment–control heterogeneity
evaluation with actionable user interpretation. For example, within subgroups [18]. These Uplift Decision Trees offered
separating Persuadables from Sure Things clarifies whether interpretable segmentation rules and provided groundwork
ahigh-responsesegmentreflectstrueincrementalimpactor for subsequent ensemble extensions. Uplift random forests
merelyhighbaselinepropensity. and causal forests improved robustness and consistency
(3)Component-WiseAblationandPerformanceAnalysis. throughaggregation,althoughatsomecosttointerpretability
We quantify the marginal contribution of each pipeline [6], [13]. This line of work reflects a broader methodolog-
stage—feature selection, clustering, bias adjustment, and ical transition toward explicitly modeling heterogeneous
causal estimation—to overall uplift performance, providing treatment effects (HTE) to inform intervention decisions.
reproduciblemethodologicalinsightsforpractitioners. As summarized by Devriendt et al. [22], this evolution
Validatingonaninternet-lendingdataset,resultsillustrate represents a broader shift from purely predictive response
how embedding causal reasoning within user profiling models to prescriptive analytics that conceptually situates
providesameanstodeliveradditionalvaluetocustomersand upliftmodelingwithinmoderncausalinference.
businessesalike,ultimatelyleadingtobetterpersonalization, Parallel advances occurred in meta-learning approaches
more precise targeting, and more effective data-driven thatreinterpretupliftestimationassuperimposedsupervised
decision-makingunderreal-worldconstraints[22],[23]. learning tasks. Frameworks like the S-, T-, X-, R-, and
DR-learners unify heterogeneous treatment effect (HTE)
a: ORGANIZATIONOFTHEPAPER estimationandupliftpredictionunderflexibletemplates[14],
Theremainderofthispaperisorganizedasfollows.SectionII [15].Theseapproachesdecoupletheestimationofnuisance
reviews related work on heterogeneous treatment effect components, such as outcome and treatment assignment
estimation,upliftmodeling,causalinferenceinrecommender models, from the final treatment-effect estimator, enabling
systems,anduserprofiling,andidentifiesthemethodological flexible combinations with different base learners. In prac-
gapsaddressedinthisstudy.SectionIIIintroducestheCausal tice,meta-learnersdiffermainlyinhowtheyreuseoutcome
UserProfiling(CUP)framework,detailingitscoremodules modelsandpropensityinformationunderimbalanceandlim-
includingfeatureselection,causalestimation,clustering,and ited overlap, and their stability is therefore strongly shaped
response-type segmentation. Section IV describes the data by base-learner choice and nuisance-model specification.
source, preprocessing procedures, and experimental design. [14],[15],[19]Thesemethodsyieldadditionalgeneralization
Section V presents and discusses the empirical results, acrosssettingsbutremainsensitivetobase-learnerselection,
focusingonmodelperformance,stability,andinterpretability sample size, and hyperparameter tuning. Until now, tabular
under repeated interventions. Section VI outlines the lim- models and representation-learning–based causal networks,
itations of the proposed framework. Finally, Section VII such as TARNet, CFRNet, DragonNet, and GANITE, have
concludes the paper and discusses directions for future adopted deep architectures to mitigate covariate imbalance,
research. reduce the burden of counterfactuals, or model nonlinear
VOLUME14,2026 40149

J.Jiangetal.:DynamicFrameworkforCUPandTreatmentSegmentationviaUpliftModeling
treatment effects on the response [26], [27], [28]. While Tree-basedmethodssuchasCausalTreesstartwiththefull
suchmodelsimproveexpressivecapacity,priorstudiesnote covariatespaceandrecursivelypartitionittoidentifyregions
trade-offs in interpretability, stability, and reproducibility, with distinct treatment effects. Causal Forests, for several
particularlyinprofiling-orientedapplications. well-foundedreasons,insteademployensembleaggregation,
As models improved, so did evaluation. Uplift modeling yielding more consistent estimators and supporting valid
concerns incremental gain; thus standard accuracy metrics statistical inference across regions [6], [13]. Generalized
are not useful. Uplift-specific ranking measures such as Random Forests (GRF) extend this local/posterior forest
the ‘‘Qini coefficient(s)’’ and the ‘‘Area Under the Uplift framework,unifyingalargeclassofforest-basedestimators
Curve (AUUC)’’ are now standard [17], [19]. Both met- into a general nonparametric framework [16]. Beyond tree
rics evaluate how effectively a model ranks individuals ensembles, Bayesian and nonparametric approaches intro-
by incremental response rather than by absolute outcome duceuncertaintyquantificationthroughcredibleintervalsand
likelihood.TheQinicoefficientsumscumulativedifferences yieldmorerobustestimatesinsmall-sampleorhigh-variance
across incremental uplift-ranked segments between treated settings [31], [32] via methods such as Bayesian Additive
and control groups. AUUC measures the total incremental Regression Trees (BART), Bayesian Causal Forests (BCF),
effect via the area between the uplift curve and a diagonal and Gaussian Process models. These approaches are often
baseline. The latter can be sensitive to treatment imbalance preferred in settings where variance control and uncertainty
or sparse samples, and recent advances have introduced assessmentarecriticaltodownstreamdecision-making.
multi-treatment AUUC and cross-treatment gain surfaces Whilelighter-weightestimatorsrelaxassumptionsrequired
to cover multi-arm and dose-response settings [29], [30]. for CATE estimation, meta-learning approaches—S-, T-,
Intuitively, gain-surface style evaluations summarize how X-, R-, and DR-learners—decompose the CATE estimation
incremental ranking performance varies across intervention task into modular supervised learning problems and offer
arms, making cross-arm trade-offs and sensitivity to treat- flexibility in base-learner choice and treatment-variable
ment choice explicit. [29], [30] Reviews emphasize that specification [14], [15]. The combination of meta-learners
the ability to generate strong uplift curves is attributable with different base learners is motivated by the need to
largely to upstream pipeline design choices, particularly balance bias, variance, and robustness under heterogeneous
featureselection,usersegmentation,andresponse-type/target data-generating conditions, rather than by any universally
labeling [8], [22]. Other comparative studies consider uplift optimal configuration. Empirical analyses show no uni-
algorithmstobe‘‘opaquemodels’’andprovidelimiteddetail versally dominant learner, highlighting that pipeline-level
onimplementationorsensitivityanalyses,whichundermines optimization is preferred over naive model substitution
reproducibility and reduces practical interpretability [17], [22]. Representation-learning–based causal models such
[18]. In this study, reproducibility refers to reporting and as TARNet, CFRNet, DragonNet, and GANITE build
structuring the full pipeline—feature construction/selection, deep latent representations to reduce covariate imbalance
clustering settings, propensity modeling, learner configu- and improve counterfactual estimation [26], [27], [28].
ration, and labeling rules—so that an independent team While these models increase expressive capacity, prior
can rerun the workflow and obtain consistent uplift curves studies note trade-offs in transparency, stability, and repro-
and response-type assignments under the same data and ducibility, particularly when interpretability is required for
protocol. These concerns motivate a methodological shift profiling-orientedanalysis[7].
fromisolatedmodelcomparisontowardworkflow-levelopti- Evaluation frameworks in the HTE literature closely
mization, focusing on transparent design choices, pipeline parallel those used in uplift modeling. Metrics such as
configuration, and component-wise diagnostics—principles Incremental AUUC and Qini measure incremental ranking
that underpin the Causal User Profiling (CUP) framework performance,whilePrecisioninEstimationofHeterogeneous
introducedinthisstudy. Effects (PEHE) and Mean Squared Error of Individual
TreatmentEffects(MSE(ITE))arecommoninsemi-synthetic
B. HETEROGENEOUSTREATMENTEFFECTS(HTE)AND benchmarks [15]. For joint learning of treatment policies,
CATEESTIMATION policy value and doubly robust off-policy evaluation (OPE)
Although uplift modeling is used mostly in marketing assess expected reward of policies derived from estimated
and intervention targeting, the concept of Heterogeneous treatment effects [33]. When multiple interventions are
TreatmentEffects(HTE)providesthetheoreticalfoundation available, multi-treatment AUUC and consistency-based
for uplift modeling. HTE methods aim to estimate the metricsfurthercharacterizethestabilityofrankingandpolicy
Conditional Average Treatment Effect (CATE) for each decisionsacrosstreatmentarms[29],[30].
individual or subgroup in the population—that is, the Recentreviewsprovideempiricalinsightintotheadoption
expected causal effect conditional on observed features [6], and implementation of HTE methods across domains.
[13]. From this perspective, uplift modeling can be viewed Aforthcoming2024methodologicalreviewofCausalForest
as an operationalization of HTE estimation that emphasizes applicationsanalyzes133peer-reviewedstudiesacrossareas
ranking and targeting decisions rather than pointwise effect from healthto marketing,documenting widespreadreliance
estimationalone. on the grf package but limited reporting of identification
40150 VOLUME14,2026

J.Jiangetal.:DynamicFrameworkforCUPandTreatmentSegmentationviaUpliftModeling
TABLE1. RepresentativemethodsandevaluationframeworksinHTEandupliftmodeling.
assumptions and tuning parameters [34]. A PRISMA- systemsemphasizedataenrichment,privacyprotection,and
guided scoping review of HTE estimation in randomized governanceconsiderationsratherthanresponse-drivencausal
controlled trials (RCTs) using machine learning reports mechanisms.Purificatoetal.[7]observethatmanyexisting
predominance of forest-based (60%) and Bayesian (53%) profilingapproaches‘‘focusoncorrelationsratherthancausal
models in domains such as health and education, while mechanisms,’’ limiting their ability to support responsive
again noting incomplete documentation of generalizability interventionsorpredictuser-leveltreatmentresponsiveness.
checks and identification strategies [35]. In RCT-emulation Thus, although causal recommender modeling has seen
pipelines that benchmark recent methodologies—including significant advances, operational techniques that integrate
Ding et al. ’s RIF—reviews report frequent failures in causalinferenceintouser-profilingpipelinesremaincompar-
confoundingadjustmentorvalidation,reinforcingtheimpor- ativelyscarce.Inparticular,conventionalprofilingworkflows
tance of reproducibility, variance control, and coherent typicallylackexplicitcomponentsfortreatment-effectidenti-
pipelinedesign[36]. fication,response-typelabeling,anduplift-basedevaluation.
Aconceptualgapthereforepersistsbetweenprofilingwork-
flowsandcausal-inferencepipelines.Addressingthisgapis
C. CAUSALINFERENCEINRECOMMENDERSYSTEMS essential for moving beyond static or purely predictive user
ANDTHEUSER-PROFILINGPIPELINE profiles toward representations that capture how users are
Inrecommendersystems,causalinferencehasbeenapplied likelytorespondunderalternativeinterventions.
to address exposure bias, selection bias, and to conduct
policy evaluation [23]. Rather than focusing solely on
predictive accuracy, this stream of work explicitly treats D. GAPSOURWORKADDRESSES
recommendationactionsasinterventionsandevaluatestheir Across the surveyed literatures, two practice-oriented gaps
causaleffectsonuserbehavior.Recentreviewsidentifycore ariserepeatedly.
causalobjectivesalongthreeinterrelateddimensions: First, applications of HTE estimation and Causal Forest
(1)causalobjectives,suchasde-biasingitemexposureand modeling often under-report critical design and tuning
estimatingthetreatmenteffectsofrecommendationactions; decisions,makingitdifficulttoreproduceresultsuniformly
(2) identification strategies, including inverse propen- or determine which components of the pipeline actually
sity scoring (IPS), doubly robust estimation (DR), and contribute to uplift or CATE performance. Rehill [34],
instrumental-variable(IV)approaches; Inoue et al. [35], and Ling et al. [36] show that studies
(3)evaluationparadigms,coveringofflinepolicylearning, frequently rely on heavy default hyperparameters, rarely
counterfactualsimulation,andonlinecontextualbandits. justify identification assumptions, and often omit report-
Together, these components form an integrated end-to- ing clustering or feature-selection strategies. As a result,
end causal pipeline spanning data collection, identification, itremainsunclearwhetherobservedperformancedifferences
policy optimization, and evaluation. This pipeline perspec- stem from causal estimators themselves or from upstream
tive emphasizes decision-oriented evaluation under explicit designchoicessuchasfeatureselection,clustering,orlabel-
interventionsratherthanstaticprediction. ing.Thisleavesunclearwhetherfeatureselection,clustering,
Conversely, traditional user-profiling research remains labeling,orotherdesignchoicesareresponsibleforobserved
largelypredictive.AssummarizedbyWuetal.[8],profiling upliftorCATEperformancedifferences[22].
pipelines typically consist of five sequential components— Second, mainstream user-profiling frameworks are com-
datacollection,datapreprocessing,featureextraction,model- prehensive in data preparation and feature engineering, but
ing,andevaluation—eachoriginallydesignedfordescriptive remain largely descriptive and correlation-based [7], [8].
segmentationorpredictiveaccuracyratherthaninterpretabil- Theygenerallylackcomponentsforcausalestimation,uplift-
ity. Similarly, Maraj et al. [37] argue that most profiling based evaluation, or assignment of causal response types.
VOLUME14,2026 40151

J.Jiangetal.:DynamicFrameworkforCUPandTreatmentSegmentationviaUpliftModeling
Consequently,existingprofilingsystemsarenotdesignedto consistency,andreadinessforanalysis[8].Nextcomesfea-
representhowusersareexpectedtorespondunderalternative tureextraction,convertingbehaviorallogsanddemographic
interventions, limiting their suitability for decision-oriented informationintorepresentationssuitableformodeling.
personalization.Thisdisconnectbetweenpredictiveprofiling AlthoughnotshowninFigure1asared-arrowcomponent
andcausalreasoninginhibitsexistingsystemsfromexplain- of its own, feature selection is an essential overhead to this
ing how users will respond to user-level interventions. Yet step, ensuring that only variables with both predictive and
such capabilities are core to adaptive personalization, broad causal relevance move down the causal analysis pipeline.
targetingoptimization,andprescriptiveanalytics. Ekeetal.[4]emphasizethatprofilingbasedonuserbehaviors
To address these gaps, we offer two methodological requiresappropriatechoiceofrepresentativevariables,while
contributions. Wager and Athey [13] warn that it is easy to accept
First, we introduce a module called Four-Type Response predictive but non-causal features with varying predictive
Segmentation, aligned with uplift theory, which uses noise(whichtendstodiluteestimatedtreatmenteffects).CUP
high-confidence uplift thresholds, model-assisted infer- thereforeusesatwo-prongedapproach:informationvaluefor
ence, and post-hoc label refinement to operationalize the predictiveimportance,andcausalimportancefromaCausal
dependence between AAUC-based evaluation metrics and Forestsapproach[13]tostabilizetheinterventions.
response-type labeling [18], [20]. This design explicitly The first truly new component of CUP is clustering
links model evaluation outcomes to interpretable response for stratification, grouping users into behaviorally similar
categories,addressingtheambiguitybetweenrankingperfor- and causally comparable groups. As Wu et al. [8] remark,
manceanduser-levelinterpretationnotedinpriorstudies. ‘‘mostpriorclusteringmethodsforuserprofilingaremainly
Second, we propose improved Causal User Profiling descriptiveandstatic;causalanalysisbenefitsfromgrouping
(CUP) Roadmap, which embeds feature selection, clus- such that the treatment and control users in a group are
tering, confounding adjustment, causal estimation, and balanced in terms of their distributions.’’ This aligns with
response-type labeling into a unified, reproducible, and findings from Devriendt et al. [22], who show that uplift
resource-aware workflow. By structuring these components modelsaresensitivetosampleimbalanceandperformbetter
asanintegratedpipelineratherthanisolatedmodelingsteps, inreliableupliftsegments.Thus,CUP’sclusteringsteptrades
CUP directly responds to reproducibility and transparency off descriptive interpretability for causal validity by pairing
concerns highlighted in the HTE and uplift literature. comparabilitywithsegmentation.
By combining causal inference, uplift modeling, and user Treatment(T)isdefinedasabinaryindicatorofwhethera
profiling into a single analytic pipeline, CUP addresses the userreceivedthetargetedinterventionwithinagivenmonth.
reproducibility issues and methodological silos highlighted Outcome (Y) is defined as whether the user initiated a
inearlierwork,providingaprincipledfoundationforcausal loanapplicationduringthesameevaluationwindow.Causal
userprofiling—anext-generationframeworkfordata-driven effects are estimated—after treatment-control selection—in
personalization,targeting,andinterventiondesign. the next submodule, confounding and bias adjustment. This
step helps ensure that treatment and control groups are
III. RESEARCHFRAMEWORK comparabletopermitcausalattributioninnon-experimental
This paper proposes an integrated methodological frame- settings.Bias-adjustmentmethodsincludeinverseprobability
work, Causal User Profiling (CUP), that connects three weighting(IPW)andstratifiedreweighting(see[6]and[14]).
previously disparate domains—user profiling, causal infer- Through these techniques, CUP mitigates selection bias
ence,andupliftmodeling—intoacommonanalyticpipeline and strengthens internal validity. To ensure comparabil-
for personalized treatment analysis. This comes from our ity between treated and control groups in the empirical
observation that user-profiling studies typically investigate analysis, treatment assignment probabilities are estimated
who the user is, identifying demographic and behavioral using observed covariates and incorporated through inverse
segments [4], [8], while ‘‘for practical intervention it is propensity weighting during uplift evaluation. This adjust-
important to first understand how a user would react if mentmitigatestreatmentimbalancearisingfromnon-random
we act’’ [6]. ‘‘Current user-modeling methods ...focus intervention assignment and reduces bias when comparing
on correlations rather than causal mechanisms,’’ as noted incrementaloutcomesbetweentreatmentarms.
by Purificato et al. [7], which limits their interpretability Next, within the potential-outcomes framework [11],
for strategic targeted interventions. The CUP framework isthecausal-effectestimationmodule.Ourcausalestimation
addresses this issue by embedding causal estimation and follows the standard potential-outcomes framework, which
response-based labeling into the profiling pipeline, turning assumes (i) SUTVA, (ii) conditional ignorability given
thede-factodescriptiveworkflowintoacausallyinterpretable observed covariates, and (iii) overlap (0 < P(T =
andresponse-awareanalyticsystem[22]. 1|X) < 1). Under these identification conditions, IPW
The CUP pipeline (Figure 1) builds on the conventional and DR learners provide consistent estimates of treatment
user-modeling workflow. It starts with data collection: effects. Causal Trees [6] track treatment heterogeneity
behavioralandcontextualdataarecapturedfromproduction using recursive partitioning, and this logic is extended in
platforms,followedbydatapreprocessingtoensurequality, Causal Forests [14]. CATEs (conditional average treatment
40152 VOLUME14,2026

J.Jiangetal.:DynamicFrameworkforCUPandTreatmentSegmentationviaUpliftModeling
FIGURE1. TraditionalversusnewlydesignedCausalUserProfiling(CUP)roadmap.Bluearrowsrepresentthetraditionaluserprofiling
process—DataCollection,DataPreprocessing,FeatureExtraction,Modeling,andPerformanceEvaluation—whileredarrowsrepresentCUP
extensions:ClusteringforStratification,ConfoundingandBiasAdjustment,CausalEffectEstimation,andResponse-TypeLabeling.
effects) are the resulting estimands from such hierarchical Response-type labeling occurs after performance evalu-
estimators.Meta-learningalgorithmssuchasT-,S-,X-,and ation. Using AUUC-based results, users are tagged to the
R-learners [15] restate causal estimation as modular (still fourclassic causal-responsecategories—Persuadables,Sure
supervised-learning) tasks that may be adjusted for cross- Things, Lost Causes, and Do-Not-Disturbs—as defined by
environment flexibility. These estimators output each user’s Radcliffe and Surry [17] and extended by Jaskowski and
upliftvalue(theeffectaninterventionhasonuserbehavior). Jaroszewicz [21]. The result of this post-evaluation process
Following causal estimation, the performance-evaluation is interpreting user-model outputs into actionable causal
submodule measures the captured impact. The Area Under profiles,completingthecausal-profilingloop.
the Uplift Curve (AUUC) is, according to Devriendt et al. CUP brings descriptive profiling and causal inference
[22]andGutiérrezandGérardy[19],thepreferredmetricfor closer together in a single sequence. Preservation of inter-
uplift performance—measuring not predictive accuracy, but pretability from user profiling [4], [8], combined with the
incremental impact captured (see [17]). We denote AUUC structure of causal-effect estimation formalism [6], [15],
as the monthly Area Under the Uplift Curve computed is central to the method, as is adopting the evaluative rigor
withineachevaluationwindow.AAUCreferstotheaverage of uplift modeling [17], [22]. With utility demonstrated on
AUUCacrossthesixmonthlyevaluationsusedinourrolling anInternet-lendingdataset,theCUPframeworkshowshow
experimental design. To interpret user-response behavior causal ‘‘laws’’ can be operationalized within profiling to
and to disentangle module contributions, CUP performs supportpersonalizedanddata-drivendecision-makingunder
component-wise ablation analysis, isolating the per-stage real-worldconstraints.
effectofthefourmodules:featureselection,clustering,bias
adjustment,andcausalestimation.Thisfollowstheprinciple A. FOUR-TYPERESPONSESEGMENTATIONMODULE
that ‘‘uplift performance depends strongly on upstream 1) CONCEPTANDTAXONOMY
design choices’’ [22]. The purpose of the ablation analysis Based on the potential outcomes framework [11], the
inthisstudyisnottoconductformalhypothesistesting,but Four-TypeResponsemoduleassignsuserstofourcanonical
toassesstherelativecontributionandstabilityofindividual causal-response types—Persuadable (A), Sure Thing (B),
pipelinecomponentsunderrepeatedreal-worlddeployments. Lost Cause (C), and Do-Not-Disturb (D). These types
Each ablation experiment removes one component from describehowanindividual’soutcomewouldchangewerethe
the CUP workflow while keeping all others fixed, and intervention present or absent, capturing causal responsive-
performance differences are evaluated consistently across nessratherthanbehavioralsimilarity[17],[20].
six consecutive monthly datasets. By examining whether In contrast to typical segmentation methods that cluster
performance changes persist across time periods rather users based on demographic or behavioral factors, uplift-
than relying on a single snapshot, the analysis provides basedprofilingemphasizesincrementalimpactestimation—
empiricalevidenceonwhetherobservedgainsaresystematic the assessment of how the probability that a user takes the
rather than incidental. Given the operational nature of desiredactionchangeswhenthetreatmentisapplied.Framed
the study and the use of large-scale observational data, in this way, user profiling becomes not merely descriptive,
we focus on temporal consistency and magnitude of perfor- butatreatment-awaredecisionprocess,informingthedesign
mance differences rather than formal statistical significance and evaluation of personalized interventions in marketing,
testing. healthcare,andcredit-analyticsdomains[18],[19],[22].
VOLUME14,2026 40153

J.Jiangetal.:DynamicFrameworkforCUPandTreatmentSegmentationviaUpliftModeling
Algorithm1Version1–Uplift-onlyTriage(High/Medium
TABLE2. Behavioralevidencepartitionlinkingtheoreticalresponse
categorieswithobservedtreatment–outcomepatterns. /Low)
Input: Dataset D with column uplift_score u (or u =
pˆ −pˆ ifavailable)
1 0
Output: Triage label ∈ {High,Medium,Low} for each
sample
Protocol:SplitDintooutertrain/valid/test;selectδonvalid
tomaximizeAUUC;freezeδfortest(noleakage)
2) BEHAVIORALEVIDENCEPARTITION
1: foreachi∈Ddo
Toprovideempiricallygroundedbaselinesforthetheoretical 2: ifu i >δthen
response types above, users are partitioned by treatment
3: label ←High
assignment T and outcome Y, resulting in four cells of 4: elseif|u i |<δthen
evidencebasedonobservedbehavioralcongruencyexpected
5: label ←Medium
across the categories (Table 2). This integrates causal
6: else
estimation and response-based labeling into the profiling
7: label ←Low
pipeline, converting the conventional descriptive workflow
8: endif
into a causally interpretable and response-aware analytic
9: endfor
system[22].
Optionalmapping:
This partition restricts theoretical labeling to behavioral
realizability: a user assigned label ‘‘A’’ but found in • ifu i ≥δ →candidateforA(Persuadable)
T = 1,Y = 0(Set 2) would exhibit an anchored • ifu i ≤−δ →candidateforD(DoNotDisturb)
violation of behavioral consistency and would therefore be • if |u i | < δ → candidate region for B/C (resolved by
V2/V3)
de-provisioned of the ‘‘A’’ label (referencing ‘‘refinement’’
from the previous subsection). Such anchoring makes the
Four-Typetaxonomybothcausallyinterpretableandempiri-
callygrounded. b: V2
Thesecondversion(V2)extendstheframeworkbyintroduc-
ingacounterfactualmappingbetweentreatmentandcontrol
3) EVOLVINGTHESEGMENTATIONDESIGNSFOR
outcome probabilities, constructing a two-dimensional pre-
FOUR-TYPERESPONSE(V1-3)
dictionspace:
The Four-Type Response Segmentation module evolved
through three generations of increasing interpretability and pˆ 1 =P(Y =1|T =1,X),
robustnessasweaddressedlimitationsinearlierdesigns.The pˆ =P(Y =1|T =0,X),
0
keymethodologicaldistinctionsaresummarizedconciselyin u=pˆ −pˆ . (2)
1 0
Table3.
Based on calibrated thresholds (yth,yth,δ) users are
1 0
assignedtothefourcanonicalresponsetypesasfollows:
a: V1
This design corresponds closely to the uplift-modeling
Theinitialversion(V1)adoptsasimpletriageapproachthat
literatures[6]and[18]andenablesinterpretabilityasitvisu-
partitions users into High, Medium, or Low responsiveness
groupssolelybasedontheupliftscore: alizes causal responsiveness across probability quadrants.
In reality, however, only a fraction of users are cleanly
pˆ =P(Y =1|T =1,X), segmented into these quadrants; many lie close to decision
1
boundaries, resulting in ambiguous labels or oscillating
pˆ =P(Y =1|T =0,X),
0 between them. V2 therefore has better interpretability than
u=pˆ
1
−pˆ
0
.
V1, but at the cost of robustness, as demonstrated during
 High, u ≥δ, evaluation[22].
 i
label
i
= Low, u
i
≤−δ, (1)
c: V3
Medium, otherwise.
V3 introduces a hybrid causal–behavioral architecture that
uses uplift estimation, behavioral validation, and model
Thisdesignprovidesalightweightwaytoregisterindivid- re-assessment to produce a joint labeling framework. V3
ual sensitivity to intervention and offers a computationally begins with high-confidence lift-based labeling and recon-
inexpensive method for identifying users likely to be ciles theoretical label assignments with empirical behavior,
affected. However, it does not provide structural causal followed by classifier-based refinement to re-label ambigu-
interpretability,norcananypurelyuplift-baseddesign;thusit ousorconflictingcases.
remainsadescriptiveratherthanafullycausalsegmentation The V3 hybrid causal–behavioral procedure consists of
method. fourstages,illustratedbelow:
40154 VOLUME14,2026

J.Jiangetal.:DynamicFrameworkforCUPandTreatmentSegmentationviaUpliftModeling
TABLE3. Comparisonofthethreesegmentationdesigns(V1–V3)byinputdependenciesandmethodologicalfocus.
FIGURE2. V3-BasedFour-StageCausalLabelingFramework.
TABLE4. Counterfactualquadrantmappingforfour-typelabeling. Usingthismulti-stageinfusionofupliftprediction,coun-
terfactualreasoning,andbehavioralcorrection,V3produces
causally interpretable and empirically consistent response-
typesegmentation,achievingsignificantAUUCstabilityand
behavioral-consistency improvements over prior versions.
By anchoring response-type assignments to both uplift
estimates and observed (T,Y) behavioral evidence, the V3
designpromoteslabelconsistencyacrosstimewindowswhile
allowing individual users to transition between response
statesastheirbehaviorevolves.
ThissegmentationlogicoftheV3hybridlabelingframe-
workshows:
Whatistheupliftdistribution?
It is partitioned into five pieces by adjustable thresholds,
whichcorrespondtothefourstagesofthelabelingpipeline:
(1)uplift-basedextremesegmentation;
(2)behavioralexpansionofA/Dboundaries;
(3)model-assistedtaggingofambiguouscases;and
(4)finalintegrationandauditing.
Thenetresult:maximumcoverageofAandDuserswhile
keeping (T,Y) behavior consistent across all four response
types.
4) SUMMARYANDDISCUSSION
Thethreeversionsofusersegmentationrepresentajourney
from the very light-handed uplift-based stratification (V1),
VOLUME14,2026 40155

J.Jiangetal.:DynamicFrameworkforCUPandTreatmentSegmentationviaUpliftModeling
Algorithm 2 Version 2 – Counterfactual Four-Quadrant Algorithm3HybridLabeling(CompactLayout)
| Segmentation |         |        |         |     |             |     |     | Input:DatasetD,T            |     |     | ∈{0,1},Y | ∈{0,1} |     |     |
| ------------ | ------- | ------ | ------- | --- | ----------- | --- | --- | --------------------------- | --- | --- | -------- | ------ | --- | --- |
|              |         |        |         |     | ),y0_prob(p |     |     | Output:Type∈{A,B,C,D},Flags |     |     |          |        |     |     |
| Input:       | Dataset | D with | columns |     | y1_prob(p 1 |     | 0 ) |                             |     |     |          |        |     |     |
(arm-wisecalibrated); upliftu=p −p Protocol:Train/Valid/Testsplit;maximizeAUUConValid;
|                                            |     |     |     |     | 1 0 |     |     |               |     |     |     |     |     |     |
| ------------------------------------------ | --- | --- | --- | --- | --- | --- | --- | ------------- | --- | --- | --- | --- | --- | --- |
| Output:Responsetype∈{A,B,C,D}foreachsample |     |     |     |     |     |     |     | freezeonTest. |     |     |     |     |     |     |
Protocol: Outer train/validation/test split; grid-search (A) Arm-wisemodels&Calibration
| (h,ℓ,δ) |     | on validation | to  | maximize | AUUC; |     | fix |        |     |       |                        |     |     |     |
| ------- | --- | ------------- | --- | -------- | ----- | --- | --- | ------ | --- | ----- | ---------------------- | --- | --- | --- |
|         |     |               |     |          |       |     |     | Trainp | 1   | (x)&p | 0 (x);Calibrateperarm. |     |     |     |
(h∗,ℓ∗,δ∗)ontest;dropsamplesviolatingoverlap.
|     |     |     |     |     |     |     |     | u(x)=p |     | −p  | ;dropoverlapviolators. |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------ | --- | --- | ---------------------- | --- | --- | --- |
1 0
|     | foreachsamplei∈Ddo |     |     |     |     |     |     | (B) Behavioralevidencepartition |     |     |     |     |     |     |
| --- | ------------------ | --- | --- | --- | --- | --- | --- | ------------------------------- | --- | --- | --- | --- | --- | --- |
1:
|     |        | ≥h∗andp                |     | ≤ℓ∗andu | ≥δ∗    |      |     |     |     |     |     |            |       |     |
| --- | ------ | ---------------------- | --- | ------- | ------ | ---- | --- | --- | --- | --- | --- | ---------- | ----- | --- |
| 2:  | if     | p 1,i                  | 0,i |         | i then |      |     |     |     |     |     |            |       |     |
|     |        | label ←A(Persuadable)  |     |         |        |      |     |     |     | S   | ={T | ,Y },S ={T | ,Y }, |     |
| 3:  |        | i                      |     |         |        |      |     |     |     | 1   | 1   | 1 2        | 1 0   |     |
|     |        | ≤ℓ∗andp                |     | ≥h∗andu | ≤−δ∗   |      |     |     |     |     |     |            |       |     |
| 4:  | elseif | p 1,i                  |     | 0,i     | i      | then |     |     |     |     |     |            |       |     |
| 5:  |        | label ←D(DoNotDisturb) |     |         |        |      |     |     |     |     |     |            |       |     |
i
|     | elseif | p ≥h∗andp             |     | ≥h∗and|u | |<δ∗ | then |     |     |     |     |     |            |       |     |
| --- | ------ | --------------------- | --- | -------- | ---- | ---- | --- | --- | --- | --- | --- | ---------- | ----- | --- |
| 6:  |        | 1,i                   |     | 0,i      | i    |      |     |     |     |     | ={T | ,Y },S ={T | ,Y }. |     |
|     |        |                       |     |          |      |      |     |     |     | S 3 | 0   | 1 4        | 0 0   |     |
| 7:  |        | label i ←B(SureThing) |     |          |      |      |     |     |     |     |     |            |       |     |
8: elseif p 1,i ≤ℓ∗andp 0,i ≤ℓ∗and|u |<δ∗ then (C) High/Mid-confidenceA/Drules
i
|     |     | ←C      |             |     |     |     |     |        |     | ,u  |                  |     |     |     |
| --- | --- | ------- | ----------- | --- | --- | --- | --- | ------ | --- | --- | ---------------- | --- | --- | --- |
| 9:  |     | label i | (LostCause) |     |     |     |     | Tune(u |     |     | )onValid.Fori∈D: |     |     |     |
high mid
10: else
|     |     |                          |     |     |                  |     |     |     | a) High-confidencerule. |     |     |     |     |     |
| --- | --- | ------------------------ | --- | --- | ---------------- | --- | --- | --- | ----------------------- | --- | --- | --- | --- | --- |
|     |     | l ab el ←NearestCorner(p |     |     | ,p ;h∗,ℓ∗,sign(u |     | ))  |     |                         |     |     |     |     |     |
1 1 : i 1,i 0,i i I f | u | ≥ u : a s sign A if u > 0, otherwise
|     |      |      |     |     |     |     |     |     | •   | i          | h igh     |     | i   |     |
| --- | ---- | ---- | --- | --- | --- | --- | --- | --- | --- | ---------- | --------- | --- | --- | --- |
| 1 2 | : en | d if |     |     |     |     |     |     |     |            |           | <   |     |     |
|     |      |      |     |     |     |     |     |     |     | a ss i g n | D i f u i | 0 . |     |     |
13: endfor
return {label } b) Mid-confidence behavioral expansion. Else,
| 14:                                                 |     | i   |     |     |     |     |     |     |        |          |                       |             |     |     |
| --------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | ------ | -------- | --------------------- | ----------- | --- | --- |
|                                                     |     |     |     |     |     |     |     |     | checku |          | -behaviorconsistency: |             |     |     |
| Note:Figure2bpresentstheconceptualdiagramofcounter- |     |     |     |     |     |     |     |     |        | mid      |                       |             |     |     |
|                                                     |     |     |     |     |     |     |     |     | •      | Ifu i ≥u | mid &(S               | 1 orS 4 )→A |     |     |
factualsegmentationunderV2.
|     |     |     |     |     |     |     |     |     | •   | Ifu ≤−u |     | &(S orS | )→D |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------- | --- | ------- | --- | --- |
|     |     |     |     |     |     |     |     |     |     | i       | mid | 2       | 3   |     |
Elseconflict→AD_conflict
•
TABLE5. StagesandfunctionalRolesintheV3causallabeling (D) InitialB/Cwithconflictflags
framework.
Forremainingi:
|     |     |     |     |     |     |     |     |     |       | =1:(u | <−u | ?B_conflict:B) |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ----- | ----- | --- | -------------- | --- | --- |
|     |     |     |     |     |     |     |     |     | • IfY |       | i   | conf           |     |     |
>u
|     |     |     |     |     |     |     |     |     | • IfY | =0:(u |     | ?C_conflict:C) |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ----- | ----- | --- | -------------- | --- | --- |
i conf
Model-assistedA↔Drefinement
(E)
TrainClassifieronStep(C)labels(stratified).
|     |     |     |     |     |     |     |     | ReassignifProb≥τ |     |     |     | &consistentquadrant. |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------------- | --- | --- | --- | -------------------- | --- | --- |
AD
|     |     |     |     |     |     |     |     | (F) Model-assistedB↔Crefinement |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------------------------- | --- | --- | --- | --- | --- | --- |
UsecleanB/Cfrom(D)assupervision.
Train/CalibrateBvsCmodels.
|     |     |     |     |     |     |     |     | Refineifconsensus≥τ |     |     |     | .   |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------------- | --- | --- | --- | --- | --- | --- |
BC
|     |     |     |     |     |     |     |     | (G) Output |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------- | --- | --- | --- | --- | --- | --- |
Returnfinallabels,conflicttypes&diagnostics.
|     |     |     |     |     |     |     |     | Note:  | Figure   | 2c presents |      | the conceptual | diagram    | of the |
| --- | --- | --- | --- | --- | --- | --- | --- | ------ | -------- | ----------- | ---- | -------------- | ---------- | ------ |
|     |     |     |     |     |     |     |     | hybrid | labeling | workflow    | (P3) | combining      | confidence | rules  |
andmodelrefinement.
throughthemorecomplexcounterfactualsegmentation(V2), B. IMPROVEDEXPERIMENTALDESIGN
tothecausal–behavioralhybridrefinement(V3)withwhich Re-approaching uplift modeling as an evaluation of user
the final design aligns. The addition of counterfactual profiling, the improved experimental design strengthens the
estimation and user profiling into the approach of V2 reasoning behind how components of uplift modeling work
makes the return to descriptive profiling reach toward a together.Ratherthaniterativelyoptimizingasinglepredictive
causal user-description framework that is interpretable and model,wereframetheassessmentofinterventionapproaches
groundedinthedata.Thisjourneyreflectshowtheprinciples andrefineallmethodologicalcomponents(featureselection,
of causal inference can help operationalize user profiling, clustering, causal estimation, response labeling), each of
bridgingincremental-impactmodelingwithbehavioralreal- which shapes the overall Area Under the Uplift Curve
ism to support decision-making within systems that rely on (AUUC). With a structured modular approach in place, the
interventions. pipeline evaluation allows us to identify how components
| 40156 |     |     |     |     |     |     |     |     |     |     |     |     | VOLUME14,2026 |     |
| ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------- | --- |

J.Jiangetal.:DynamicFrameworkforCUPandTreatmentSegmentationviaUpliftModeling
work together transparently, ensuring that an uplift-based Regression often serves as the baseline learner for com-
user-profilingpipelineisreproducibleandasinterpretableas putational efficiency, while Random Forests, GBDT, and
| possible. |     |     |     |     |     |     | XGBoostareemployedassanitychecks.Eachlearner’sout- |     |     |     |     |     |     |     |
| --------- | --- | --- | --- | --- | --- | --- | -------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
putsarethenpassedtotheFour-TypeResponseSegmentation
|     |     |     |     |     |     |     | Module | (Section | III-B) | to yield | CATE/uplift |     | scores | tagged |
| --- | --- | --- | --- | --- | --- | --- | ------ | -------- | ------ | -------- | ----------- | --- | ------ | ------ |
1) PIPELINEOVERVIEW
withbehavioralnamesorinterpretabletypes.
| The framework |     | for | user | profiling | is based | on causal |     |     |     |     |     |     |     |     |
| ------------- | --- | --- | ---- | --------- | -------- | --------- | --- | --- | --- | --- | --- | --- | --- | --- |
Inafinalsteptofacilitatecausalinterpretability,wecluster
| principles. | Following |     | from causal | user | profiling, | we add to |            |          |             |     |         |             |     |      |
| ----------- | --------- | --- | ----------- | ---- | ---------- | --------- | ---------- | -------- | ----------- | --- | ------- | ----------- | --- | ---- |
|             |           |     |             |      |            |           | users into | causally | homogeneous |     | strata. | Recognizing |     | that |
thepipeline(Figure3)auser-profilingand‘‘de-causalizing’’
|             |       |     |            |            |     |               | real-world | behavioral |     | heterogeneity |     | drives | treatment-effect |     |
| ----------- | ----- | --- | ---------- | ---------- | --- | ------------- | ---------- | ---------- | --- | ------------- | --- | ------ | ---------------- | --- |
| methodology | based |     | on feature | uniqueness |     | and response. |            |            |     |               |     |        |                  |     |
variation,CUPemploysK-Meansclusteringonstandardized
| In particular,     | clustering, |     | causal   | estimation,      |     | user profiling, |            |         |            |                 |     |            |         |         |
| ------------------ | ----------- | --- | -------- | ---------------- | --- | --------------- | ---------- | ------- | ---------- | --------------- | --- | ---------- | ------- | ------- |
|                    |             |     |          |                  |     |                 | features   | to form | stable     | subpopulations, |     | each       | serving | as a    |
| and component-wise |             |     | ablation | are incorporated |     | to quantify     |            |         |            |                 |     |            |         |         |
|                    |             |     |          |                  |     |                 | contextual | unit    | for uplift | estimation      |     | [8], [22]. | The     | optimal |
contributions.
|                 |     |              |         |               |              |           | number    | of clusters | K        | is chosen | via              | elbow   | and  | silhouette |
| --------------- | --- | ------------ | ------- | ------------- | ------------ | --------- | --------- | ----------- | -------- | --------- | ---------------- | ------- | ---- | ---------- |
| Operating       | on  | a            | monthly | rolling       | basis—across | both      |           |             |          |           |                  |         |      |            |
|                 |     |              |         |               |              |           | criteria. | Clusters    | below    | 2%        | of total         | samples | or   | yielding   |
| cross-sectional |     | and temporal |         | vigilance—the | pipeline     | allows    |           |             |          |           |                  |         |      |            |
|                 |     |              |         |               |              |           | AUUC      | lower       | than the | baseline  | are              | merged  | into | others.    |
| examination     | of  | how feature  |         | selection,    | clustering,  | response- |           |             |          |           |                  |         |      |            |
|                 |     |              |         |               |              |           | Notably,  | clustering  |          | enhances  | interpretability |         | and  | reveals    |
interactioninformation,andcausaladjustmentworktogether
behavioralregimesthatwouldotherwiseremainhidden.
| as individual | components |             | of  | a Causal | User Profiling | (CUP)      |     |     |     |     |     |     |     |     |
| ------------- | ---------- | ----------- | --- | -------- | -------------- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- |
| pipeline.     | All        | experiments |     | share a  | common         | time-based |     |     |     |     |     |     |     |     |
3) EVALUATIONANDABLATIONDESIGN
| train/validation/test |     | protocol |     | with shared | random | seeds and |     |     |     |     |     |     |     |     |
| --------------------- | --- | -------- | --- | ----------- | ------ | --------- | --- | --- | --- | --- | --- | --- | --- | --- |
Thisevaluationprocedurequantifieshoweachdecisioneither
| fixed preprocessing |                 | across | months,       | highlighting |     | that these  |          |      |           |            |          |        |              |          |
| ------------------- | --------------- | ------ | ------------- | ------------ | --- | ----------- | -------- | ---- | --------- | ---------- | -------- | ------ | ------------ | -------- |
|                     |                 |        |               |              |     |             | promoted | or   | detracted | from       | ultimate | uplift | performance. |          |
| choices             | drive stability |        | and practical | reliability  |     | in modeling |          |      |           |            |          |        |              |          |
|                     |                 |        |               |              |     |             | We use   | area | under     | the uplift | curve    | (AUUC) | as           | the core |
userprofilingunderthecausalframework.
|     |     |     |     |     |     |     | performance |       | measure, | as well | as the      | Qini | coefficient | and     |
| --- | --- | --- | --- | --- | --- | --- | ----------- | ----- | -------- | ------- | ----------- | ---- | ----------- | ------- |
|     |     |     |     |     |     |     | uplift@k    | [17], | [19],    | [22].   | We separate |      | marginal    | effects |
2) COREMODULES:FROMFEATURESELECTIONTOCAUSAL
|     |     |     |     |     |     |     | through | component-wise |     | ablation | (e.g., | removing |     | the clus- |
| --- | --- | --- | --- | --- | --- | --- | ------- | -------------- | --- | -------- | ------ | -------- | --- | --------- |
ESTIMATION tering,causalfeatureselection,orlabelrefinementmodule).
The pipeline begins by identifying features that are both Performanceisevaluatedbothgloballyandbycluster,using
stable and causally relevant, allowing us to draw causal aweightedmetric:
| insights | generalizable |     | to unseen | treatment | groups. | A multi- |     |     |     |     |     |     |     |     |
| -------- | ------------- | --- | --------- | --------- | ------- | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
K
| stageselectionprocesscombinesstatisticalrelevance(Infor- |     |               |     |           |             |           |     |               |     |     | X   |       |     |     |
| -------------------------------------------------------- | --- | ------------- | --- | --------- | ----------- | --------- | --- | ------------- | --- | --- | --- | ----- | --- | --- |
|                                                          |     |               |     |           |             |           |     | WeightedAUUC= |     |     | w   | ·AUUC | ,   | (3) |
|                                                          |     |               |     |           |             |           |     |               |     |     |     | k     | k   |     |
| mation Value,                                            |     | IV), temporal |     | stability | (Population | Stability |     |               |     |     |     |       |     |     |
k=1
| Index, PSI), | and | causal   | importance  | (Causal |       | Forest variable |        |                                                |     |     |     |     |     |     |
| ------------ | --- | -------- | ----------- | ------- | ----- | --------------- | ------ | ---------------------------------------------- | --- | --- | --- | --- | --- | --- |
|              |     |          |             |         |       |                 | wherew | k denotestherelativeproportionofvalidsamplesin |     |     |     |     |     |     |
| importance   | and | stepwise | regression) |         | [13]. | This produces   |        |                                                |     |     |     |     |     |     |
clusterk.
| multiple | feature | sets from | the | base DataFrame: |     | IV-only/PSI |     |     |     |     |     |     |     |     |
| -------- | ------- | --------- | --- | --------------- | --- | ----------- | --- | --- | --- | --- | --- | --- | --- | --- |
subsets,CF-only/PSI,andhybridtypes(IV+CF,IV+CF Otherdiagnosticsinclude:
+STEP).Theaimistoobtainaparsimonioussetoffeatures Labeladherencerates(band,quadrant,andbehavioral-
•
representativeofthepopulation,standardizedandimputedon cellconsistency)
thesamefoldstoensurefairnessandcausalinterpretability. • Type-wise outcome balance between treatment and
Before uplift estimation, we must address any remaining controlgroups
κ
treatment-control imbalances, often done using Propensity • Temporal stability measured via Cohen’s across
months
| Score Matching |     | (PSM) | and | Inverse Probability |     | Weighting |     |     |     |     |     |     |     |     |
| -------------- | --- | ----- | --- | ------------------- | --- | --------- | --- | --- | --- | --- | --- | --- | --- | --- |
(IPW) [10], [38]. These covariate-adjustment techniques • Computationalefficiency(runtimeandconvergence)
reweight samples to render treated and control groups We computed robustness via bootstrap confidence inter-
comparable so that the uplift reflects the genuine treatment vals, out-of-time validation, and selective sweeps through
effect rather than asymmetries in treatment allocation (i.e., subsampleswhentheuplifttheycontainedappearederratic.
selection bias). For randomized subsets, they also serve as We performed all experiments with fixed random seeds,
a sanity check for stability: estimated uplift effects should version-controlled datasets, and standardized preprocessing
confirmconfoundingcontrol. pipelines. We took comprehensive logs of AUUC, variable
Uplift estimation is conducted using two families of importance,andclusterdiagnosticsfromeachrun,andthen
models: meta-learners and Causal Forests. Meta-learners stitched together the pieces. This provided a transparent
such as T-, S-, X-, R-, and DR-learners factor CATE ‘‘causal audit trail’’ enabling independent replication of our
| estimationintomodularsupervised-learningtasks[14],[15], |     |     |     |     |     |     | results. |     |     |     |     |     |     |     |
| ------------------------------------------------------- | --- | --- | --- | --- | --- | --- | -------- | --- | --- | --- | --- | --- | --- | --- |
while Causal Forests provide nonparametric and asymptoti- To avoid ad-hoc decisions outside the evaluation frame-
callyconsistentestimatesofheterogeneoustreatmenteffects work,wemadereproducibilityafoundationwithinourevalu-
[16]. To preserve causal integrity, all learners share the ationratherthanseparateitoutasitsownstage.Thistrade-off
same preprocessing, data, and evaluation strategy. Logistic between methodological rigor and operational reliability
| VOLUME14,2026 |     |     |     |     |     |     |     |     |     |     |     |     |     | 40157 |
| ------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----- |

J.Jiangetal.:DynamicFrameworkforCUPandTreatmentSegmentationviaUpliftModeling
FIGURE3. ImprovedexperimentalpipelineoftheCausalUserProfiling(CUP)framework.Thepipelineintegratesfeatureselection,
clustering,confoundingadjustment,causaleffectestimation,andevaluationintoareproducibleworkflowexecutedinmonthlyrolling
loops.
wasempiricallyobserved:thisevaluationstrategystabilized status—including both static user attributes and dynamic
the AUUC variance across monthly slices. It reduced the financial indicators—comprising: gender, age, and city tier;
damage from confounding-driven fluctuations while giving borrowing frequency; repayment performance; credit-line
usareliablemeasureoftruetreatmentheterogeneity. utilizationlimits;overduehistoryandrepaymentdiscipline;
|     |     |     |     |     |     | and consumption-related |     | activity. | These | variables |     | capture |
| --- | --- | --- | --- | --- | --- | ----------------------- | --- | --------- | ----- | --------- | --- | ------- |
C. SUMMARY treatment heterogeneity and user-specific behavior in gen-
| In this chapter | we  | presented | an enhanced | experimental |     | eral. |     |     |     |     |     |     |
| --------------- | --- | --------- | ----------- | ------------ | --- | ----- | --- | --- | --- | --- | --- | --- |
Priortomodelfitting,severalprocedureswereconducted
designthatintegratesbothcausalinferenceanduserprofiling
into a single uplift-modeling approach. The Four-Type to improve comparability and robustness within and across
Response Segmentation Module guarantees causal labeling potentialcovariates.Followingbusinessconventions,missing
robustness, while component-wise ablation analysis gauges or invalid values were set according to domain logic;
thecontributionofeachmethodologicalcomponent—feature numerouscontinuousfeatureswerescaledfornumericcom-
|                        |     |            |               |     |            | parability; | and feature | selection | was | subsequently |     | applied |
| ---------------------- | --- | ---------- | ------------- | --- | ---------- | ----------- | ----------- | --------- | --- | ------------ | --- | ------- |
| selection, clustering, |     | and causal | estimation—to |     | the uplift |             |             |           |     |              |     |         |
score.Allofthisisimplementedinoneconsolidatedprocess through a diagnostic three-stage procedure consistent with
thatweavesevaluationandreproducibilitytogether,thereby previously documented theory [22]. This screening stage is
laying the groundwork for a transparent, interpretable, and performed before constructing the downstream feature-set
empiricallyvalidatedbasisfordynamiccausaluserprofiling. configurations (e.g., IV-only, Causal, and hybrid sets),
|     |     |     |     |     |     | ensuring | that all reported | feature | sets | are derived | from | the |
| --- | --- | --- | --- | --- | --- | -------- | ----------------- | ------- | ---- | ----------- | ---- | --- |
IV. DATADESCRIPTION samefilteredandstability-checkedcandidatepool:
In our empirical analysis we employ proprietary data 1. Information Value (IV) was computed to quantify
predictiverelevanceforthetargetoutcome.
| collected from | users | of a leading | Chinese | internet | finance |     |     |     |     |     |     |     |
| -------------- | ----- | ------------ | ------- | -------- | ------- | --- | --- | --- | --- | --- | --- | --- |
platform’s mobile app. To enable causal interpretability, 2. Population Stability Index (PSI) was used to evaluate
|     |     |     |     |     |     | temporal | stability and | detect | distributional |     | shifts | across |
| --- | --- | --- | --- | --- | --- | -------- | ------------- | ------ | -------------- | --- | ------ | ------ |
weconsideronlyactiveborrowers,i.e.,userswithoutstand-
| ing loan balances |     | in the observation | window. | Compared | to  | months. |     |     |     |     |     |     |
| ----------------- | --- | ------------------ | ------- | -------- | --- | ------- | --- | --- | --- | --- | --- | --- |
non-borrowers(whoarenotindebtedorhavesatisfiedprior 3.Pairwisecorrelationanalysisidentifiedredundantvari-
ablesandmitigatedmulticollinearity.
| loan demands), | active | borrowers | are more | homogeneous: |     |     |     |     |     |     |     |     |
| -------------- | ------ | --------- | -------- | ------------ | --- | --- | --- | --- | --- | --- | --- | --- |
they seek credit more consistently, reducing the number of Variables having IV < 0.05 or PSI > 0.25 were dropped,
|                      |     |         |                |     |           | and features | were merged | when | their | pairwise | correlation |     |
| -------------------- | --- | ------- | -------------- | --- | --------- | ------------ | ----------- | ---- | ----- | -------- | ----------- | --- |
| possible confounders |     | arising | from variation | in  | borrowing |              |             |      |       |          |             |     |
motives. By ensuring behavioral comparability between exceeded 0.8 in absolute terms. This process produced
treated and control users, this focus improves the power of a balanced set of features encompassing interpretability,
|     |     |     |     |     |     | robustness, | and predictive | capability—in |     | line | with | recent |
| --- | --- | --- | --- | --- | --- | ----------- | -------------- | ------------- | --- | ---- | ---- | ------ |
causalidentification.
The dataset consists of an intermingled trove of infor- methodological standards in heterogeneous treatment-effect
researchforsimilarusecases[41].
| mation covering |     | demographic | behavior | as well | as credit |     |     |     |     |     |               |     |
| --------------- | --- | ----------- | -------- | ------- | --------- | --- | --- | --- | --- | --- | ------------- | --- |
| 40158           |     |             |          |         |           |     |     |     |     |     | VOLUME14,2026 |     |

J.Jiangetal.:DynamicFrameworkforCUPandTreatmentSegmentationviaUpliftModeling
Algorithm 4 Core Experimental Loop (Baseline and the strongest predictive power, mirroring previous research
Clustering-Enabled) showing that dynamic behavioral attributes are highly pre-
| Input:DatasetD;FeatureSets{F |     | ,...,F | };  |     |     |     |     |     |
| ---------------------------- | --- | ------ | --- | --- | --- | --- | --- | --- |
1 6 dictive of treatment responsiveness. Correlation diagnostics
Metalearners {T, S, X, DR, CF}; Baselearners {LR, RF, confirmthatweeffectivelycontrolledformulticollinearity.
| GBDT,XGB};Months{M |     | ,...,M | }   |     |                  |             |                     |       |
| ------------------ | --- | ------ | --- | --- | ---------------- | ----------- | ------------------- | ----- |
|                    |     | 1      | 6   |     | These procedures | ensure that | the empirical model | iden- |
Output:AUUCscores;clusterstatistics;variableimportance tifies true behavioral heterogeneity rather than confounding
foreachmonthm⊆{M ,...,M }do arisingfromunstableorsuperfluouspredictors.Insummary,
| 1:  |     | 1   | 6   |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
2: D ←subset(D,month=m) thedatasetunderwentasystematicandjudiciousfilteringand
m
foreachfeaturesetF inFeatureSetsdo refinement process consistent with best practices in causal
3:
,F);
4: X ← select_features(D m T ← treatment; inference and comparable recent works in the literature.
Y ←outcome The resulting analysis environment is stable, representative,
∈Metalearnersdo andamenabletoestimatingheterogeneoustreatmenteffects,
5: foreachML
6: foreachBL ∈Baselearnersdo as well as to implementing causal models of users in
|     | ifclustering_enabledthen |     |     |     | subsequentsections. |     |     |     |
| --- | ------------------------ | --- | --- | --- | ------------------- | --- | --- | --- |
7:
clusters←KMeans(X,K)
8:
9: foreachclustercinclustersdo A. SEGMENTATIONANDDISTRIBUTIONOFFOUR
| 10: | ifvalid_cluster(c)then |     |     |     | RESPONSETYPES |     |     |     |
| --- | ---------------------- | --- | --- | --- | ------------- | --- | --- | --- |
11: model ←train(ML,BL,X ,T ,Y ) This section presents the empirical results of the Four-Type
|     |     | c   |     | c c c |     |     |     |     |
| --- | --- | --- | --- | ----- | --- | --- | --- | --- |
score ← Response Segmentation Module introduced in Chapter 3,
| 12: |     | c   |     |       |     |     |     |     |
| --- | --- | --- | --- | ----- | --- | --- | --- | --- |
|     |     |     | ,X  | ,T ,Y |     |     |     |     |
evaluate_AUUC(model c c c c ) illustrating how uplift-based causal labeling emerges in the
13: else dataset.Withinthecausaluser-profilingframework,usersare
skip
| 14: |     |     |     |     | segmentedbasedontheirIndividualTreatmentEffect(ITE) |     |     |     |
| --- | --- | --- | --- | --- | --------------------------------------------------- | --- | --- | --- |
15: endif underthepotential-outcomesmodel.Inparticular,wedefine
|     | endfor |     |     |     | fourcanonicalresponsetypesas: |     |     |     |
| --- | ------ | --- | --- | --- | ----------------------------- | --- | --- | --- |
16:
clusters←merge_low_AUUC(clusters)
| 17: |      |     |     |     | • Persuadables(TypeA):performthetargetactiononly |     |     |     |
| --- | ---- | --- | --- | --- | ------------------------------------------------ | --- | --- | --- |
| 18: | else |     |     |     |                                                  |     |     |     |
iftreated
model ←train(ML,BL,X,T,Y)
19:
|     | score←evaluate_AUUC(model,X,T,Y) |     |     |     |     | =1,y | =0) |     |
| --- | -------------------------------- | --- | --- | --- | --- | ---- | --- | --- |
| 20: |                                  |     |     |     |     | (y 1 | 0   |     |
endif
21:
• SureThings(TypeB):performtheactionregardlessof
| 22: | endfor |     |     |     |     |     |     |     |
| --- | ------ | --- | --- | --- | --- | --- | --- | --- |
treatment
23: endfor
endfor
| 24: |     |     |     |     |     | (y =1,y | =1) |     |
| --- | --- | --- | --- | --- | --- | ------- | --- | --- |
|     |     |     |     |     |     | 1       | 0   |     |
25: endfor
LostCauses(TypeC):neverperformtheaction
•
|             |            |         |             |          |                | (y =0,y   | =0) |     |
| ----------- | ---------- | ------- | ----------- | -------- | -------------- | --------- | --- | --- |
|             |            |         |             |          |                | 1         | 0   |     |
| Descriptive | statistics | for our | dataset are | shown in |                |           |     |     |
|             |            |         |             |          | Do Not Disturb | (Type D): |     |     |
Table4-1.Thedatasetcontainsapproximately720,000user- • perform the action only if
nottreated
monthsgeneratedfromsixcalendarmonths.Thesix-month
| window reflects | a practical | trade-off   | between      | behavioral |     |         |     |     |
| --------------- | ----------- | ----------- | ------------ | ---------- | --- | ------- | --- | --- |
|                 |             |             |              |            |     | (y =0,y | =1) |     |
|                 |             |             |              |            |     | 1       | 0   |     |
| stability and   | sample      | coverage in | a real-world | lending    |     |         |     |     |
system, providing repeated exposure to interventions for Thistypologyprovidesconceptualclaritytoheterogeneous
temporal robustness checks while limiting structural drift behavioral patterns and enables causal modelling, tailored
in user composition and platform policy. All loans have a interventionstrategies,andmarketingresourceallocationto
mean utilization rate of 62.8% (SD = 24.5%), indicating beginconceptually.Inpractice,thefrequencyoftypesacross
behavioral heterogeneity. An average repayment-timeliness users is summarized in Figure 5a. There are significantly
index of 0.91 reflects a disciplined borrower population. more Persuadables and Lost Causes relative to Sure Things
Approximately78%ofusersliveinatier-2orlower-tiercity. in the user population, meaning that there are slightly more
Users in the treatment group appear to exhibit somewhat people who will change behaviour under some treatment
higher utilization and higher-frequency engagement than than will remain the same across any treatment; but the
usersinthecontrolgroup,implyingheterogeneousinterven- mostobservationsareofuserswhoareresistanttotreatment.
tion responses relevant for uplift analyses. Feature stability Sure Things should have stable demand, although—as with
andrelevancediagnosticsfurtheraffirmtherobustnessofthis everythingelse—theyshouldbegivenequalratesofexposure
variableset:theaverageIVacrossretainedfeaturesis0.23, in the broadest possible sense of the term. Do-Not-Disturb
and the average PSI is 0.07, both within accepted stability users are a hindrance, and serve as an indicator of potential
bounds [42]. Behavioral and repayment indicators have adverse intervention effects, serving as a caution against
| VOLUME14,2026 |     |     |     |     |     |     |     | 40159 |
| ------------- | --- | --- | --- | --- | --- | --- | --- | ----- |

J.Jiangetal.:DynamicFrameworkforCUPandTreatmentSegmentationviaUpliftModeling
FIGURE4. WorkflowofDataPreprocessingandVariableSelection.Note.Theworkflowdepictssequentialdatapreparationsteps:Raw
DataCollection→DataCleaningandMissingValueTreatment→NormalizationandStandardization→IVComputation→PSIEvaluation
→CorrelationFiltering→FeatureRetentionforModeling.
TABLE6. Descriptivestatisticsofthesample.
over-targeting and treatment fatigue, even if they constitute whereasCausalfeaturesassistwithoverallmodelstability,
onlyasmallportionofthetotalcohort. particularlyforthelargerDR-Learner.
To make even clearer how this segmentation might Because benefits come from different sources, it is not
typically be done, Figure 5b plots the empirical joint obvious a priori how the responses will sort themselves
|     |     | ,y  |     |     |     |     |     |     | +   |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
distributionof(y 0 1 )andnotesthefourdecisionregionsas out when combining them. The IV Causal set produces
dictatedbythepotential-outcomesformulation. the overall highest mean AUUC—validating that ‘‘picking
|     |     |     |     |     |     | dimensions | gives you information |     | gain, and picking | good |
| --- | --- | --- | --- | --- | --- | ---------- | --------------------- | --- | ----------------- | ---- |
dimensionsgivesyoucausalrelevance.’’Oncethisouter-join
B. EMPIRICALEVALUATIONOFTHECUPFRAMEWORK
|     |     |     |     |     |     | set of dimensions | is added, | Stepwise | refinement | can then |
| --- | --- | --- | --- | --- | --- | ----------------- | --------- | -------- | ---------- | -------- |
ThissectiondescribestheempiricalevaluationoftheCausal
|                |     |       |            |              |             | be incorporated. | These hybrid          | sets            | exhibit slightly | lower    |
| -------------- | --- | ----- | ---------- | ------------ | ----------- | ---------------- | --------------------- | --------------- | ---------------- | -------- |
| User Profiling |     | (CUP) | framework. | We evaluated | each of the |                  |                       |                 |                  |          |
|                |     |       |            |              |             | mean AUUC        | but are less volatile | month-to-month, |                  | yielding |
corecomponentsofCUP—featureselection,clustering,and
smalleruplift-consistency(UC)indices.Althoughtheirmean
meta-learnerconfiguration—individuallyandasacombined
AUUCismarginallylower,theabilitytodependonthemodel
| system | to assess | their | influence | on uplift | performance, |     |     |     |     |     |
| ------ | --------- | ----- | --------- | --------- | ------------ | --- | --- | --- | --- | --- |
producingsimilarresultsacrossmonthsisworththetrade-off
asmeasuredbytheAreaUndertheUpliftCurve(AUUC).
inmeanvalues.
Insummary:
1) FEATURESELECTIONANDUPLIFTPERFORMANCE IV + Causal accelerates accuracy at the cost of some
| To explore | how | variable | screening | affects | heterogeneous | stability. |     |     |     |     |
| ---------- | --- | -------- | --------- | ------- | ------------- | ---------- | --- | --- | --- | --- |
treatment-effectestimation,sixfeaturesetswerecompared: IV + Causal + Stepwise favours stability at the cost of
| ALL—allvariables; |     |     |     |     |     | someaccuracy. |     |     |     |     |
| ----------------- | --- | --- | --- | --- | --- | ------------- | --- | --- | --- | --- |
IV—selectedbyinformationvalue; The second approach is more deployment-ready and is
Causal — chosen by causal-forest importance and PSI therefore used as ‘‘the features’’ moving forward. Across
stability;
|     |     |     |     |     |     | learners | as well, the meta- | and | base-learners | perform |
| --- | --- | --- | --- | --- | --- | -------- | ------------------ | --- | ------------- | ------- |
Stepwise—retainedthroughcross-fittedregression; relativelyconsistently.LogisticRegression(LR)standsoutas
IV+Causal—intersectionofthefirsttwo; thestrongestbaselearnerunderthehybridfeaturesets,while
IV+Causal+Stepwise—thehybridrefinement.
tree-basedlearnersshowweaknesswhennoiseremainsinthe
Findingsshowthatappropriatevariableselectioniscritical embeddings. Therefore, feature selection forms the skeletal
| to uplift | modeling. | Using |     | ALL resulted | in the lowest |     |     |     |     |     |
| --------- | --------- | ----- | --- | ------------ | ------------- | --- | --- | --- | --- | --- |
structureforCUP.
| mean AUUC |        | and the | highest | variance—it     | appears that   |     |     |     |     |     |
| --------- | ------ | ------- | ------- | --------------- | -------------- | --- | --- | --- | --- | --- |
| when the  | models | must    | learn   | in the presence | of substantial |     |     |     |     |     |
noise, it severely weakens identification with respect to the 2) CLUSTERINGSTRATEGIESANDAUUCENHANCEMENT
heterogeneouseffectsthemselves. Clustering was introduced to investigate local treatment
BothIVandCausalselectionsproducemeaningfullybetter heterogeneity independent of an explicit association with
resultsthanthebaseline,butindifferentways: outcomes, consistent with the notion that subgroups with
IV features push the AUUC higher on the simpler meta- different causal effects can be mapped out by recursive
learners(T-andX-Learners), partitioning[6].Theempiricalresultssuggestthatclustering
| 40160 |     |     |     |     |     |     |     |     |     | VOLUME14,2026 |
| ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------- |

J.Jiangetal.:DynamicFrameworkforCUPandTreatmentSegmentationviaUpliftModeling
FIGURE5. Empiricaldistributionoffourcausalresponsetypes(left)andjointdistributionofpotentialoutcomes(y0 ,y1)
illustratingABCDregions(right).
is helpful but is conditional rather than absolute, and as a weakclusterswithglobalpredictions,C2hasaregularizing
consequenceshouldbeusedcautiously. effect, balancing local adaptivity and global stability. This
The contrast between Direct, C1 (Merging), and C2 variance-reducing characteristic maps onto the findings of
(Replacement) shows a clear trade-off. The Elbow Method Devriendt et al. [22], who show that ‘‘ensemble-style’’
suggests optimal clusters around K=6, at which point upliftmodelsproducelowervariance(andgreaterreliability)
the silhouette score levels off (see Figure 7a). This is than ‘‘isolated’’ two-model structures. In our case, Direct
parsimonious and easy to interpret, and we derive clusters identifies behavioral heterogeneity but does not produce
followingthisthroughoutouranalysis. stable models. C1 reduces this variance somewhat, but part
Across the three methods, the C2 step is consistently the of it remains. Empirically, the clustering order is C2 > C1
strongest, yielding the highest uplift effect: mean AUUC >Direct(seeFigure7b),placingclusteringasarefinement
(≈0.09)withthelowestvariance(±0.01).By‘‘replacing’’ ratherthanarequisite.
VOLUME14,2026 40161

J.Jiangetal.:DynamicFrameworkforCUPandTreatmentSegmentationviaUpliftModeling
FIGURE6. Evaluationoffeature-selectionstrategiesandmeta-learnerinteractionsinupliftmodeling.
(a)BoxplotsofAUUCvaluesacrosssixfeaturesets,illustratingperformancevariabilityacross
configurations.(b)TemporalmeanAUUCoversixmonthscomparingIV+CausalandStep_IV+Causal
featuresets,withthelowerpanelshowingthepopulationstandarddeviationofAUUCacrossmonths
toevaluatetemporalstability.(c)HeatmapofMeta-Learner×Feature-Setinteractions,showing
averageAUUCvaluesfordifferentlearner-featurecombinations.TheDR-Learnerachievesthehighest
upliftperformanceunderIV+CausalandStep_IV+Causalfeatureconfigurations.(d)Standard
deviationofAUUCacrosspairedfeatureconfigurations,illustratingthevariance-reductioneffectof
stepwiserefinement.
40162 VOLUME14,2026

J.Jiangetal.:DynamicFrameworkforCUPandTreatmentSegmentationviaUpliftModeling
Clustering interacts differently with the various meta- set. Among the meta-learners, the DR-Learner consistently
learners. As reflected in Figure 7c, the X-Learner shows produced the highest mean AUUC, albeit with higher
the most robust and consistent improvement, reflecting its varianceacrossmonths,indicatingrobustnessinpointperfor-
theoretical gain in segmented or unbalanced samples [15]. mancebutsensitivitytotemporalfluctuations.TheX-Learner
Incontrast,theDR-LearnerandT-LearnershowAUUCdrops offers strong competition, particularly under treatment-
or inconsistencies after clustering, and the Causal Forest imbalance situations, whereas the T- and S-Learners are
(CF) even experiences extreme performance deterioration. farmoreunreliableincomplex,high-varianceenvironments.
Thisisconsistentwithearlierfindingsthattree-basedcausal Amongthebaselearners,LogisticRegression(LR)performs
estimators lose efficiency when subgroup sample sizes are bestintermsofstabilityandinterpretability,whiletree-based
small or unbalanced [13], [35] —meta-learners capable of learnersexhibitsubstantiallymorevariabilityoverall.
‘‘cross-arm information sharing’’ (such as the X-Learner)
remain stable under segmentation, whereas others are sen- 4) OPTIMALPATHWAYANDOVERALLEFFECT
sitive to fragmentation. Figure 7d illustrates cluster-level Putting all these pieces together, the final CUP workflow
performance under the X-Learner. As expected, clustering uses a hybrid IV + (Causal ∩ Stepwise) feature-selection
amplifies both signal and noise: some cluster-level AUUC design, employs the C2 ‘‘replacement strategy’’ with a
values improve substantially, while others drop sharply. moderate number of clusters K, and adopts a DR-Learner
This follows the familiar ‘‘variance-amplifying effect,’’ withLogisticRegressionasthemodelingconfiguration.This
wheresmallersubsamplesincreasebothestimationbiasand integrated pathway yields a large and stable improvement
variance[13].Thus,clusteringuncoverslatentheterogeneity in AUUC relative to the baseline (‘‘all features + no
butcanalsoamplifyrandomnoise,helpingtoexplainwhyits clustering + standard learner’’). The main performance
performancevariesacrossdatasetsandtimeperiods. gains come from variables that are informative (high IV)
The effectiveness of clustering depends critically on the and causally relevant, and the C2 approach provides a
feature space used. In Figure 7, clustering derived from form of structural regularization that prevents overfitting
the Causal feature set yields the most consistent gains, andstabilizesheterogeneoustreatmentestimation.Together,
outperforming clustering based on IV-only or ALL-variable these components lead to a balanced pipeline that improves
feature sets. This indicates that clustering is effective only bothaccuracyandinterpretability.
when the feature space encodes causally relevant informa- Quantitatively, each module of the CUP framework
tion:causalfeaturesyieldamorecoherentandinterpretable contributes a distinct and measurable improvement to uplift
mapoftheunderlyingterrain,enablingclusteringtoidentify performance. Feature selection alone increases AUUC by
more precise treatment heterogeneity [43], [44]. To recap: approximately 25–30%, reflecting the value of filtering
causal features structure the space, and clustering amplifies out noisy predictors and emphasizing causally important
heterogeneity. Clustering based solely on predictive or variables.IncorporatingC2clusteringprovidesanadditional
correlation-drivenvariablestendstoamplifynoise. 10–12% gain by stabilizing weak clusters and harmonizing
Clusteringdoesnotuniversallyimproveoutcomes.Itpro- local heterogeneity with global patterns. Optimizing the
ducesawidespreadinAUUCacrossclusters;improvement meta/baseconfiguration(DR-Learner+LogisticRegression)
in some clusters may be accompanied by deterioration in yields a further 5–8% improvement, enhancing robustness
others. This dual-edged nature makes clustering powerful while maintaining interpretability. Cumulatively, the inte-
but dangerous. Clustering should be viewed as a ‘‘positive grated CUP workflow achieves roughly 45–50% higher
calibrationmechanism,’’effectiveonlywhenstronglyrooted AUUC than the standard uplift-modeling baseline, demon-
in causal features and paired with robust learners (such as stratingthateachcomponentcontributesaclearandpersistent
the X-Learner) that remain stable under segmentation. Its incrementacrossthesixmonthlyslices.
feedback on the Four-Type causal segmentation (Persuad-
able,SureThing,LostCause,Do-Not-Disturb)mustalsobe V. DISCUSSION
monitored, as behavioral balance can be distorted through The empirical validation of the framework demonstrates
subgroupredistribution. thatcausalinferenceandupliftmodellingcanberigorously
In summary, clustering improves uplift estimation only brought to bear on user analytics, closing a classic gap in
‘‘under reasonably complete causal feature structures’’ and theanalyticsspacebetweenpredictionandintervention.This
with‘‘meta-learnersthatremainstableundersegmentation.’’ sectiondiscussestheempiricalfindingsinrelationtoexisting
Clustering performs best with the C2 replacement strategy. upliftmodelinganduserprofilingapproaches,withemphasis
Given that clustering can amplify both gains and volatility, onstability,interpretability,andoperationalrelevance.
it should be treated as a calibrated instrument, not as a The Causal User Profiling (CUP) framework moves
mandatorycomponentofeverycausaluser-profilingpipeline. beyond descriptive or purely predictive profiling by cen-
tering treatment responsiveness as its primary analytical
3) META-LEARNERANDBASE-LEARNERCONFIGURATIONS dimension.Thisreframingabstractsusermodellingfromthe
Atotalofsixteenmeta/basecombinations(fourmeta-learners question of who users are, to how users behave when acted
×fourbaselearners)wereexploredusingtheoptimalfeature on [6] and [22]. This move from correlation to causation
VOLUME14,2026 40163

J.Jiangetal.:DynamicFrameworkforCUPandTreatmentSegmentationviaUpliftModeling
FIGURE7. Evaluationofclusteringstrategiesandmeta-learnerperformanceunderclustered
upliftmodeling.(a)Elbowcurvebasedonsilhouettescoresforselectingtheoptimalnumber
ofclusters.ThesilhouettescorestabilizesnearK=48,indicatingasuitabletrade-off
betweenclustercohesionandseparation.(b)Comparisonofclusteringstrategies(Direct,C1,
C2)usingmultipleAUUCindicators,includingbaselineAUUC,weightedAUUC,clusterAUUC,
andextremeclusterAUUCvalues.ResultsindicatetheperformancerankingC2>C1>
Direct,withC2achievingthehigheststabilityandlowestvariance.(c)Meta-learner
performancecomparisonunderclusteringacrossmonths.ResultsshowthattheXLearner
demonstratesthemostconsistentimprovement,whereasDR-,T-,andCF-Learnersexhibit
greaterfluctuationsorperformancedecline.
40164 VOLUME14,2026

J.Jiangetal.:DynamicFrameworkforCUPandTreatmentSegmentationviaUpliftModeling
FIGURE7. (Continued).Evaluationofclusteringstrategiesandmeta-learnerperformanceunder
clusteredupliftmodeling.(a)Elbowcurvebasedonsilhouettescoresforselectingtheoptimalnumber
ofclusters.ThesilhouettescorestabilizesnearK=48,indicatingasuitabletrade-offbetweencluster
cohesionandseparation.(b)Comparisonofclusteringstrategies(Direct,C1,C2)usingmultipleAUUC
indicators,includingbaselineAUUC,weightedAUUC,clusterAUUC,andextremeclusterAUUCvalues.
ResultsindicatetheperformancerankingC2>C1>Direct,withC2achievingthehigheststabilityand
lowestvariance.(c)Meta-learnerperformancecomparisonunderclusteringacrossmonths.Results
showthattheXLearnerdemonstratesthemostconsistentimprovement,whereasDR-,T-,and
CF-Learnersexhibitgreaterfluctuationsorperformancedecline.
VOLUME14,2026 40165

J.Jiangetal.:DynamicFrameworkforCUPandTreatmentSegmentationviaUpliftModeling
FIGURE8. HeatmapshowingthemeanAAUCvaluesforallMeta-Learner×Base-Learnerconfigurations.Darkercellsindicate
higherupliftperformance.TheDR-LearnercombinedwithLogisticRegression(LR)achievesthehighestmeanAAUCandlowest
variance,demonstratingthemostbalancedtrade-offbetweenaccuracy,stability,andinterpretability.
representsatransformationintheconceptualunderpinnings A second insight relates to methodological integration,
ofpersonalizationscience,towardaframeworkthatpredicts which contributes directly to the robustness of CUP. Rather
behaviour while also explaining why effects transpire. The than operating as isolated modules, feature selection, clus-
empirical findings confirm that causal interpretability is tering, and causal estimation work synergistically. The C2
distinctive in its potential to redefine user segmentation. replacement strategy compensates for unstable clusters by
Rootedinthepotentialoutcomesframework[11],lateraug- substitutingtheirpredictionswiththoseoftheglobalmodel,
mentedintothemetalevelframeworkofmeta-learning[15], producing a hierarchical regularization effect that maintains
CUPquantifiesheterogeneoustreatmenteffectsthroughthe localsensitivitywhileensuringglobalconsistency[4].Within
four-type response taxonomy of Persuadables, Sure Things, this structure, the Doubly Robust (DR) Learner combined
LostCauses,andDo-Not-Disturbs[17]. withLogisticRegression(LR)deliversafavourablebalance
This treatment-aware representation of user behaviour between robustness and interpretability. While alternative
indicates that the heterogeneity observed in behaviour is configurationssuchastheX-Learnermayperformwellunder
not an artefact of random variation but rather a marker certain imbalance conditions, the DR–LR configuration
of differential responsiveness to intervention. In the digital demonstrated greater temporal stability across repeated
lending case-study context, these distinctions illustrate how deployments,whichisessentialinoperationalenvironments.
interventions may activate engagement, reinforce inevitable From a practical perspective, CUP grounds causal rea-
outcomes,protectusersfromunnecessaryactions,orrespect soning in consequences experienced by decision-makers.
non-responsiveness. Compared with conventional uplift By estimating conditional treatment effects rather than
modeling pipelines that emphasize ranking accuracy predictive probabilities, the framework enables intervention
alone, CUP aligns estimation, evaluation, and response designbasedoncausalevidenceratherthanintuitionorcorre-
interpretationwithinaunifiedanalyticalframework,yielding lation.Empirically,thesequentialstackingofmethodological
morestablegainsunderrepeatedinterventions. components yields meaningful and interpretable gains in
| A first           | salient | insight | from    | the      | results | concerns the | performance:   |                    |     |      |             |
| ----------------- | ------- | ------- | ------- | -------- | ------- | ------------ | -------------- | ------------------ | --- | ---- | ----------- |
| interrelationship |         | between | feature | quality, | model   | stability,   |                |                    |     |      |             |
|                   |         |         |         |          |         |              | Hybrid feature | selection improves |     | AUUC | by approxi- |
•
| and causal | validity. | The | hybrid | feature | selection | strategy— |     |     |     |     |     |
| ---------- | --------- | --- | ------ | ------- | --------- | --------- | --- | --- | --- | --- | --- |
mately25–30%overthebaseline;
| combining | Information |     | Value | (IV), | Causal Forest | impor- |     |     |     |     |     |
| --------- | ----------- | --- | ----- | ----- | ------------- | ------ | --- | --- | --- | --- | --- |
• Clusteringcontributesanadditional10–12%throughthe
| tance, and | Stepwise | refinement—produced |     |     | the | most stable |     |     |     |     |     |
| ---------- | -------- | ------------------- | --- | --- | --- | ----------- | --- | --- | --- | --- | --- |
C2refinementstrategy;
upliftperformanceacrossmonthlysamples.Thisobservation
|          |              |     |      |                   |     |            | • The DR-Learner | + LR configuration |     | adds | a further |
| -------- | ------------ | --- | ---- | ----------------- | --- | ---------- | ---------------- | ------------------ | --- | ---- | --------- |
| confirms | the argument |     | that | causal estimation |     | depends as |                  |                    |     |      |           |
5–8%uplift.
| much on | data stability |     | and regime | design | as on | algorithmic |     |     |     |     |     |
| ------- | -------------- | --- | ---------- | ------ | ----- | ----------- | --- | --- | --- | --- | --- |
sophistication [6]. High-IV variables ensure that the model Cumulatively,thefull CUPpipelineachievesanapproxi-
mately45–50%improvementinmodelperformancerelative
learnsfrominformation-richdimensions;causalimportance
anchorsrelevancetotreatmenteffects;andStepwiseselection to conventional profiling approaches. More importantly,
serves as a form of variance regularization. Together, these thesegainspersistacrossmultipletimewindows,indicating
|            |       |            |     |         |              |          | systematic rather | than incidental | improvements. |     | From a |
| ---------- | ----- | ---------- | --- | ------- | ------------ | -------- | ----------------- | --------------- | ------------- | --- | ------ |
| components | yield | a ‘‘causal |     | feature | space’’ that | balances |                   |                 |               |     |        |
predictivestrengthwithgeneralizablestructuralcharacteris- computationalstandpoint,theruntimeofCUPisdominated
bybaselearnertrainingandclusteringstagesandintroduces
tics.Thisfindingreinforcesthenotionof‘‘datarefinement’’
[4], consistent with evidence in causal machine learning no additional asymptotic complexity beyond standard uplift
that emphasizes disciplined feature design over increasing modelingpipelines,makingittractableforlarge-scaletabular
datasets.
algorithmiccomplexity.
| 40166 |     |     |     |     |     |     |     |     |     |     | VOLUME14,2026 |
| ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------- |

J.Jiangetal.:DynamicFrameworkforCUPandTreatmentSegmentationviaUpliftModeling
FIGURE9. CumulativegaincurvescomparingtheoptimizedCUPpathwaywiththebaseline;theCUP
curveuniformlydominates.
VI. LIMITATIONSOFTHESTUDY externalgeneralizability.FutureresearchshouldassessCUP
Despite its empirical strengths, this study has several across additional domains such as e-commerce, insurance,
limitations. First, the analysis is based on data from a andpublicfinancetoevaluatecross-contextrobustness.
singledigitallendingplatform.Whilethisenablescontrolled Second, the treatment variable aggregates heterogeneous
evaluation under realistic operational conditions, it limits interventions (e.g., coupons, credit-line increases, outbound
VOLUME14,2026 40167

J.Jiangetal.:DynamicFrameworkforCUPandTreatmentSegmentationviaUpliftModeling
calls), which may obscure intervention-specific behavioural outcomes,ensuringcausalinterpretabilitywhilemaintaining
mechanisms. Extending CUP to explicit multi-treatment or temporalstability.
dynamic intervention settings would enable finer-grained For each deployment period, uplift scores are first
analysisofintervention-specificcausaleffects. estimated using the selected meta-learner configuration.
Third, the evaluation emphasizes temporal consistency High-confidence uplift thresholds are applied to identify
acrosssixmonthlydeploymentsratherthanformalstatistical users with strong positive or negative estimated treatment
hypothesistesting.Thisdesignchoicereflectsanoperational effects. These uplift-based signals are then cross-validated
(T,Y)
focusonstabilityandreproducibilitybutmaylimitinference against observed realizations to refine response-type
insettingsthatrequireformalsignificancetesting. assignmentsandtopreventlogicallyinconsistentlabels.
Finally,issuesoffairness,transparency,andethicaldeploy- Specifically, Persuadables and Do-Not-Disturb users are
mentwarrantfurtherattention.Incorporatingfairness-aware identified through a combination of uplift magnitude and
learning and causal explainability into CUP represents an treatment-outcome alignment, while Sure Things and Lost
importantdirectionforfuturework,particularlyinsensitive Causes are distinguished based on behavioral invariance
financialapplications[1],[4]. withrespecttotreatmentexposure.Thistwo-stageprocedure
|     |     |     |     |     |     |     |     | mitigates | label noise | arising | from | estimation | uncertainty |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --------- | ----------- | ------- | ---- | ---------- | ----------- | --- |
VII. CONCLUSIONANDFUTUREWORK and ensures that response categories remain behaviorally
| This study | contributes |     | to the | growing | literature | on  | causal | meaningful. |     |     |     |     |     |     |
| ---------- | ----------- | --- | ------ | ------- | ---------- | --- | ------ | ----------- | --- | --- | --- | --- | --- | --- |
analyticsbypositioningcausalityastheorganizingprinciple To promote consistency across time windows,
of user profiling. We propose Causal User Profiling (CUP), response-type definitions are held fixed, while individual
an integrated pipeline that combines feature selection, usersareallowedtotransitionbetweenresponsestatesastheir
clustering, and meta-learning into a reproducible and inter- behavior evolves. This design yields stable population-level
pretable workflow that connects causal estimation with semanticswhilepreservingindividual-leveldynamicsunder
| actionabledecision-making. |     |     |     |     |     |     |     | repeatedinterventions. |     |     |     |     |     |     |
| -------------------------- | --- | --- | --- | --- | --- | --- | --- | ---------------------- | --- | --- | --- | --- | --- | --- |
Empirically,CUPcapturesheterogeneoustreatmenteffects
| with temporal |     | stability; | conceptually, |     | it  | reframes | user |     |     |     |     |     |     |     |
| ------------- | --- | ---------- | ------------- | --- | --- | -------- | ---- | --- | --- | --- | --- | --- | --- | --- |
APPENDIXB
| profiling | as the | causal | understanding |     | of  | behavioural |     |     |     |     |     |     |     |     |
| --------- | ------ | ------ | ------------- | --- | --- | ----------- | --- | --- | --- | --- | --- | --- | --- | --- |
C2REPLACEMENTSTRATEGY
| response;                     | and practically, |       | it provides     |     | a scalable         | foundation    |           |                  |              |            |            |            |               |          |
| ----------------------------- | ---------------- | ----- | --------------- | --- | ------------------ | ------------- | --------- | ---------------- | ------------ | ---------- | ---------- | ---------- | ------------- | -------- |
|                               |                  |       |                 |     |                    |               |           | In the CUP       | framework,   | clustering | is         | treated    | as a          | flexible |
| for treatment-awarestrategies |                  |       | indiverse       |     | digitalecosystems. |               |           |                  |              |            |            |            |               |          |
|                               |                  |       |                 |     |                    |               |           | and corrective   | component    | rather     | than       | a hard     | segmentation  |          |
| Rather                        | than competing   |       | with predictive |     | machine            |               | learning, |                  |              |            |            |            |               |          |
|                               |                  |       |                 |     |                    |               |           | step. Clustering | is performed |            | at the     | individual | level,        | while    |
| CUP complements               |                  | it    | by explaining   |     | why                | interventions |           |                  |              |            |            |            |               |          |
|                               |                  |       |                 |     |                    |               |           | model evaluation | and          | stability  | assessment |            | are conducted |          |
| work and                      | for              | whom, | advancing       |     | personalization    |               | from      |                  |              |            |            |            |               |          |
acrossmonthlydeploymentwindowstoreflectsystem-level
outcomepredictiontowardcausalunderstandinganddecision
performanceunderrepeatedinterventions.
optimization.
|     |     |     |     |     |     |     |     | After          | initial clustering, | uplift   | performance |     | is evaluated    |     |
| --- | --- | --- | --- | --- | --- | --- | --- | -------------- | ------------------- | -------- | ----------- | --- | --------------- | --- |
|     |     |     |     |     |     |     |     | at the cluster | level and           | compared | against     |     | a non-clustered |     |
ACKNOWLEDGMENT (Direct)baselineusingthesamemonthlyevaluationprotocol.
| This study | benefited | from | the | Haier | Group | Digital | Finance |               |            |       |      |         |          |     |
| ---------- | --------- | ---- | --- | ----- | ----- | ------- | ------- | ------------- | ---------- | ----- | ---- | ------- | -------- | --- |
|            |           |      |     |       |       |         |         | Cluster-based | prediction | paths | that | exhibit | unstable | or  |
InnovationInitiative(whichprovidedtheaccesstodataand
inferiorupliftperformancerelativetotheDirectglobalmodel
computerresourcesforempiricalvalidationofourproposed
arenotpropagatedtodownstreamresponse-typeassignment.
model),andtheauthorsareespeciallygratefultothemforthe
Thiscomparisongivesrisetothreeevaluationpaths:
implementationoftheCUP.
• Direct:upliftestimationwithoutclustering;
DATAAVAILABILITYSTATEMENT • C1:upliftestimationwithinclusters;
The dataset used in this study is subject to institutional C2: cluster-level evaluation followed by fallback to
•
andcommercialrestrictionsandthereforecannotbepublicly Directpredictionswhenclusteringdegradesstabilityor
released at this time. Aggregated statistics and derived performance.
experimentalresultsarereportedinthemanuscript.
|           |           |         |          |                   |                |     |          | Rather     | than enforcing | cluster-specific |          | predictions |                 | at the |
| --------- | --------- | ------- | -------- | ----------------- | -------------- | --- | -------- | ---------- | -------------- | ---------------- | -------- | ----------- | --------------- | ------ |
| The       | authors   | plan to | release  | a reproducibility |                |     | package, |            |                |                  |          |             |                 |        |
|           |           |         |          |                   |                |     |          | individual | level, the     | C2 strategy      | operates |             | as a path-level |        |
| including | synthetic | data    | examples | and               | representative |     | code     |            |                |                  |          |             |                 |        |
regularizationmechanism.Itpreservescluster-basedhetero-
| implementations, |     | subject | to data-sharing |     | approval |     | in future |     |     |     |     |     |     |     |
| ---------------- | --- | ------- | --------------- | --- | -------- | --- | --------- | --- | --- | --- | --- | --- | --- | --- |
geneitywhenbeneficial,whilerevertingtotheglobalmodel
work.
whenclusteringintroducesnoiseorinstability.
APPENDIXA
| RESPONSE-TYPELABELCONSTRUCTIONAND |     |     |     |     |     |     |     | APPENDIXC              |     |     |     |     |     |     |
| --------------------------------- | --- | --- | --- | --- | --- | --- | --- | ---------------------- | --- | --- | --- | --- | --- | --- |
| CONSISTENCY                       |     |     |     |     |     |     |     | ABLATIONANALYSISDESIGN |     |     |     |     |     |     |
Response-type labels in CUP are constructed to reflect The purpose of the ablation analysis in this study is not to
both estimated treatment effects and observed behavioral conduct formal hypothesis testing, but to assess the relative
| 40168 |     |     |     |     |     |     |     |     |     |     |     |     | VOLUME14,2026 |     |
| ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------- | --- |

J.Jiangetal.:DynamicFrameworkforCUPandTreatmentSegmentationviaUpliftModeling
contributionandstabilityofindividualcomponentswithinthe selected data summaries or code components may be made
| CUPpipelineunderrepeatedreal-worlddeployments. |     |     |     |     |     |     |     | available. |     |     |     |     |     |     |
| ---------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | ---------- | --- | --- | --- | --- | --- | --- |
Each ablation experiment removes or modifies one com- From a computational perspective, the CUP framework
ponent of the framework while keeping all others fixed. is designed to remain tractable for large tabular datasets.
Performance differences are evaluated consistently across The dominant computational costs arise from repeated
six consecutive monthly datasets, allowing assessment of uplift model estimation, causal feature screening, and
whetherobservedeffectspersistovertimeratherthanarising clustering-based analyses across multiple monthly deploy-
fromasinglesnapshot. ments. While no additional asymptotic complexity is intro-
Given the operational nature of the study and the use ducedbeyondstandardupliftmodelingpipelines,thecumu-
of large-scale observational data, emphasis is placed on lativeexperimentalworkloadissubstantialduetothebreadth
temporal consistency and the magnitude of performance ofmodelconfigurationsandablationsettingsevaluated.
differencesratherthanformalstatisticalsignificancetesting. Inthisstudy,extensiveablationexperimentsandstability
Thisdesignprovidesempiricalevidenceonwhetherobserved checks were prioritized to assess robustness under repeated
gains are systematic and reproducible under repeated inter- deployment.Asaresult,certainalgorithmicchoices—suchas
ventionsettings. theselectionofclusteringmethodsandbaselearners—reflect
|     |     |     |     |     |     |     |     | a deliberate | trade-off     |     | between   | methodological |                | coverage |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------ | ------------- | --- | --------- | -------------- | -------------- | -------- |
|     |     |     |     |     |     |     |     | and feasible | computational |     | execution | under          | single-machine |          |
APPENDIXD
| FEATURESCREENINGANDSCALINGSTRATEGY |     |     |     |     |     |     |     | constraints. |     |     |     |     |     |     |
| ---------------------------------- | --- | --- | --- | --- | --- | --- | --- | ------------ | --- | --- | --- | --- | --- | --- |
Feature preprocessing in CUP is designed to enhance FutureworkwillextendtheCUPframeworktoincorporate
|     |     |     |     |     |     |     |     | additional | feature | selection | strategies, | uplift | estimators, | and |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------- | ------- | --------- | ----------- | ------ | ----------- | --- |
numericalcomparability,stability,andcausalrelevanceprior
to model estimation, rather than to optimize predictive clustering algorithms as computational resources permit.
accuracythroughaggressivenormalizationortransformation. Theseextensionsareexpectedtofurtherenrichcomparative
Before model fitting, all candidate covariates undergo analysiswithoutalteringthecoremethodologicalprinciples
a unified screening process to ensure consistency across establishedinthepresentstudy.
downstreamfeatureconfigurations.Continuousvariablesare
rescaledtoacommonnumericalrangetoimprovecompara-
REFERENCES
bilityacrossfeatureswithheterogeneousmagnitudesandto
|     |     |     |     |     |     |     |     | [1] E. Rich, | ‘‘User | modeling | via stereotypes,’’ | Cognit. | Sci., | vol. 3, no. 4, |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------ | ------ | -------- | ------------------ | ------- | ----- | -------------- |
facilitatestableoptimizationinsubsequentmodelingstages. pp.329–354,1979.
Thisrescalingisapplieduniformlyanddoesnotaltertherel-
|     |     |     |     |     |     |     |     | [2] G. Adomavicius |     | and A.   | Tuzhilin, | ‘‘Toward                | the next | generation of |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------------ | --- | -------- | --------- | ----------------------- | -------- | ------------- |
|     |     |     |     |     |     |     |     | recommender        |     | systems: | A survey  | of the state-of-the-art |          | and possible  |
ativeorderingordistributionalshapeofindividualfeatures.
extensions,’’IEEETrans.Knowl.DataEng.,vol.17,no.6,pp.734–749,
Featureselectionproceedsthroughadiagnosticmulti-stage
Jun.2005,doi:10.1109/TKDE.2005.99.
| procedure | that | combines |     | complementary |     | criteria: |     |                                                                   |     |     |     |     |     |     |
| --------- | ---- | -------- | --- | ------------- | --- | --------- | --- | ----------------------------------------------------------------- | --- | --- | --- | --- | --- | --- |
|           |      |          |     |               |     |           |     | [3] P.BrusilovskyandE.Millán,‘‘Usermodelsforadaptivehypermediaand |     |     |     |     |     |     |
(i)information-basedscreeningtoretainvariableswithsuffi- adaptiveeducationalsystems,’’inTheAdaptiveWeb.Cham,Switzerland:
cient outcome relevance, (ii) causal importance assessment Springer,2007,pp.3–53.
|     |     |     |     |     |     |     |     | [4] C.I.Eke,A.A.Norman,andW.Ozuem,‘‘Userprofilinginpersonalized |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --------------------------------------------------------------- | --- | --- | --- | --- | --- | --- |
to identify features consistently associated with treatment recommender systems: A systematic review,’’ IEEE Access, vol. 7,
effects across time windows, and (iii) stepwise refinement pp.146923–146940,2019,doi:10.1109/ACCESS.2018.2887321.
tocontrolredundancyandvarianceinflation. [5] D.Mirylenka,F.Ricci,andL.Rokach,‘‘Usermodelingandpersonaliza-
tion,’’inRecommenderSystemsHandbook.NewYork,NY,USA:Springer,
| Importantly, |     | this screening |     | stage is | performed | prior | to  |     |     |     |     |     |     |     |
| ------------ | --- | -------------- | --- | -------- | --------- | ----- | --- | --- | --- | --- | --- | --- | --- | --- |
2019,doi:10.1145/3357384.3357818.
| constructing       | downstream |               | feature-set |           | configurations |          | (e.g., |                                                                      |       |            |           |           |         |               |
| ------------------ | ---------- | ------------- | ----------- | --------- | -------------- | -------- | ------ | -------------------------------------------------------------------- | ----- | ---------- | --------- | --------- | ------- | ------------- |
|                    |            |               |             |           |                |          |        | [6] S.AtheyandG.Imbens,‘‘Recursivepartitioningforheterogeneouscausal |       |            |           |           |         |               |
| information-based, |            | causal-based, |             | or hybrid | sets),         | ensuring |        |                                                                      |       |            |           |           |         |               |
|                    |            |               |             |           |                |          |        | effects,’’                                                           | Proc. | Nat. Acad. | Sci. USA, | vol. 113, | no. 27, | pp.7353–7360, |
that all reported models draw from a common pool of Jul.2016,doi:10.1073/pnas.1510489113.
filtered and stability-checked covariates. This design avoids [7] F. Purificato, A. Rago, A. Belkhir, P. Lanzini, and P. Cirillo, ‘‘Deep
causalmodels:Asurvey,’’Inf.Process.&Manag.,vol.61,no.3,2024,
feature-induced confounding when comparing alternative Art.no.103579,doi:10.1016/j.ipm.2023.103579.
model specifications and promotes reproducibility under [8] W.Wu,F.Yuan,J.Huang,X.Yu,andM.Zhang,‘‘Social-network-based
repeateddeployment. userprofiling:Asurvey,’’Inf.Sci.,vol.648,Oct.2024,Art.no.119021,
doi:10.1016/j.ins.2024.119021.
|     |     |     |     |     |     |     |     | [9] J.Pearl,Causality:Models,Reasoning,andInference,2nded.,Cambridge, |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --------------------------------------------------------------------- | --- | --- | --- | --- | --- | --- |
APPENDIXE
U.K.:CambridgeUniv.Press,2009,doi:10.1017/CBO9780511803478.
COMPUTATIONALCONSIDERATIONS [10] M.A.HernánandJ.M.Robins,CausalInference:WhatIf.London,U.K.:
Theempiricalstudywasconductedusinglarge-scaleobser- Chapman&Hall,2020,doi:10.1201/9780429259654.
vationaldatafromareal-worlddigitallendingplatform.Due [11] D.B.Rubin,‘‘Estimatingcausaleffectsoftreatmentsinrandomizedand
nonrandomizedstudies,’’J.Educ.Psychol.,vol.66,no.5,pp.688–701,
totheinvolvementofsensitivecustomer-levelfinancialinfor-
Oct.1974,doi:10.1037/h0037350.
| mation, | the underlying |     | dataset | cannot | be publicly | released |     |                                                                     |     |     |     |     |     |     |
| ------- | -------------- | --- | ------- | ------ | ----------- | -------- | --- | ------------------------------------------------------------------- | --- | --- | --- | --- | --- | --- |
|         |                |     |         |        |             |          |     | [12] G.W.ImbensandD.B.Rubin,CausalInferenceforStatistics,Social,and |     |     |     |     |     |     |
at this stage. Data access was granted under institutional BiomedicalSciences.Cambridge,U.K.:CambridgeUniv.Press,2015,doi:
10.1017/CBO9781139025751.
collaborationandconfidentialityagreements,andresultsare
|          |               |     |     |            |       |         |     | [13] S. Wager | and     | S. Athey, | ‘‘Estimation | and inference          |     | of heterogeneous |
| -------- | ------------- | --- | --- | ---------- | ----- | ------- | --- | ------------- | ------- | --------- | ------------ | ---------------------- | --- | ---------------- |
| reported | in aggregated |     | and | anonymized | form. | Subject | to  |               |         |           |              |                        |     |                  |
|          |               |     |     |            |       |         |     | treatment     | effects | using     | random       | forests,’’ Biometrika, |     | vol. 105, no. 2, |
future approval and appropriate de-identification protocols, pp.287–301,2018,doi:10.1093/biomet/asx045.
| VOLUME14,2026 |     |     |     |     |     |     |     |     |     |     |     |     |     | 40169 |
| ------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----- |

J.Jiangetal.:DynamicFrameworkforCUPandTreatmentSegmentationviaUpliftModeling
[14] X. Nie and S. Wager, ‘‘Quasi-oracle estimation of heterogeneous [40] N. Hu, ‘‘Heterogeneous treatment effects analysis for social scientists:
treatmenteffects,’’Ann.Statist.,vol.49,no.6,pp.3935–3963,3935,doi: A review,’’ Social Sci. Res., vol. 109, Jan. 2023, Art.no.102810, doi:
| 10.1214/20-AOS1964. |     |     |     |     |     |     |     | 10.1016/j.ssresearch.2022.102810. |     |     |     |     |     |     |
| ------------------- | --- | --- | --- | --- | --- | --- | --- | --------------------------------- | --- | --- | --- | --- | --- | --- |
[15] S.R.Künzel,J.S.Sekhon,P.J.Bickel,andB.Yu,‘‘Metalearnersfor [41] Z.Zhang,P.Zhao,X.Li,andY.Liu,‘‘Causalrepresentationlearning,’’in
estimatingheterogeneoustreatmenteffectsusingmachinelearning,’’Proc. Proc.KDD,2021,pp.2663–2673,doi:10.1145/3447548.3467381.
Nat.Acad.Sci.USA,vol.116,no.10,pp.4156–4165,Mar.2019,doi: [42] A.M.AlaaandM.V.D.Schaar,‘‘Limitsofestimatingheterogeneous
10.1073/pnas.1804597116. treatmenteffects:Guidelinesforpracticalalgorithmdesign,’’IEEETrans.
[16] S. Athey, J. Tibshirani, and S. Wager, ‘‘Generalized random forests,’’ NeuralNetw.Learn.Syst.,pp.129–138,Jan.2018.
Ann.Statist.,vol.47,no.2,pp.1148–1178,Jan.2019,doi:10.1214/18- [43] X. Guo, K. Yu, L. Liu, F. Cao, and J. Li, ‘‘Causal representation
AOS1709. learning:Asurvey,’’Artif.Intell.,vol.320,Nov.2024,Art.no.104072,
[17] N.J.RadcliffeandP.D.Surry,‘‘Upliftmodellingwithsignificance-based doi:10.1016/j.artint.2024.104072.
trees,’’StochasticSolutions,London,U.K.,Tech.Rep.,2011. [44] Z. Zhang, P. Zhao, X. Li, and Y. Liu, ‘‘Deep causal models for ITE
[18] P.RzepakowskiandS.Jaroszewicz,‘‘Decisiontreesforupliftmodeling estimation:Asurvey,’’ACMComput.Surv.,vol.55,no.12,pp.1–38,2023,
with single and multiple treatments,’’ Knowl. Inf. Syst., vol. 32, no. 2, doi:10.1145/3527154.
pp.303–327,Aug.2012,doi:10.1007/s10115-011-0434-0.
[19] P.GutierrezandJ.Y.Gérardy,‘‘Causalinferenceandupliftmodelling:A
reviewoftheliterature,’’Inf.Sci.,vol.420,pp.590–598,Jun.2017,doi:
10.1016/j.ins.2017.02.002.
| [20] N. J. | Radcliffe, | ‘‘Using | control | groups | to target on | predicted | lift,’’ |     |     |     |     |     |     |     |
| ---------- | ---------- | ------- | ------- | ------ | ------------ | --------- | ------- | --- | --- | --- | --- | --- | --- | --- |
StochasticSolutions,London,U.K.,Tech.Rep.,2007.
| [21] M. Jaskowski |     | and S. | Jaroszewicz, | ‘‘Uplift   | modeling | for       | clinical |     |     |     |     |     |     |     |
| ----------------- | --- | ------ | ------------ | ---------- | -------- | --------- | -------- | --- | --- | --- | --- | --- | --- | --- |
| trial data,’’     | in  | Proc.  | ICDM         | Workshops, | 2012,    | pp.17–23, | doi:     |     |     |     |     |     |     |     |
10.1109/ICDMW.2012.103. JIANQING JIANG is currently pursuing the
[22] F. Devriendt, D. Moldovan, and W. Verbeke, ‘‘A literature survey and Ph.D.degreewiththeInstituteforMathematical
experimental evaluation of the state-of-the-art in uplift modeling: A Research (INSPEM), Universiti Putra Malaysia.
| stepping | stone | toward the | development | of  | prescriptive | analytics,’’ | Big |     |     |              |      |                     |     |              |
| -------- | ----- | ---------- | ----------- | --- | ------------ | ------------ | --- | --- | --- | ------------ | ---- | ------------------- | --- | ------------ |
|          |       |            |             |     |              |              |     |     |     | His research | lies | at the intersection |     | of user pro- |
Data,vol.6,no.1,pp.13–41,Mar.2018,doi:10.1089/big.2017.0104.
|     |     |     |     |     |     |     |     |     |     | filing, | causal machine | learning, | uplift | modeling, |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------- | -------------- | --------- | ------ | --------- |
[23] Z.Zhang,P.Zhao,X.Li,andY.Liu,‘‘Deepcausalmodels:Taxonomyand
|     |     |     |     |     |     |     |     |     |     | and heterogeneous |     | treatment | effect | estimation, |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----------------- | --- | --------- | ------ | ----------- |
roadmap,’’ACMComput.Surveys,vol.56,no.3,pp.1–36,2024.
withaparticularfocusondynamicuserprofiling
[24] J.Chen,Y.Wang,andX.Li,‘‘Asurveyofuserprofiling:State-of-the-
art,challengesandsolutions,’’Inf.Process.Manage.,vol.61,no.2,2024, and personalized intervention design. He has
Art.no.103676,doi:10.1016/j.ipm.2023.103676. more thanseven years ofindustry experience in
[25] F. Devriendt, D. Moldovan, and W. Verbeke, ‘‘Prescriptive analytics data science and business intelligence, holding
through uplift modeling: A review,’’ Inf. Fusion, vol. 73, pp.67–86, professional roles in China and Singapore in credit analytics, customer
modeling,andenterprisedatasystems.PriortohisPh.D.studies,hewas
Sep.2021,doi:10.1016/j.inffus.2021.02.003.
[26] U.Shalit,F.D.Johansson,andD.Sontag,‘‘Estimatingindividualtreatment a Senior Data Scientist developing credit scoring models, customer
effect:Generalizationboundsandalgorithms,’’inProc.34thInt.Conf. segmentationframeworks,andlarge-scaledatagovernanceplatforms.His
Mach.Learn.,2017,pp.3076–3085. current research integrates causal inference with behavioral modeling
[27] C.Shi,D.M.Blei,andV.Veitch,‘‘Adaptingneuralnetworksforcausal to improve decision-making in internet lending and other high-stakes
| inference,’’2019,arXiv:1905.12776. |            |     |        |             |           |            |     | operationalenvironments. |     |     |     |     |     |     |
| ---------------------------------- | ---------- | --- | ------ | ----------- | --------- | ---------- | --- | ------------------------ | --- | --- | --- | --- | --- | --- |
| [28] J. Yoon,                      | J. Jordon, | and | M. Van | Der Schaar, | ‘‘GANITE: | Estimating |     |                          |     |     |     |     |     |     |
individualizedtreatmenteffects,’’2018,arXiv.1806.04968.
[29] D.Olaya,H.Ponce,M.A.Gutiérrez-Andrade,andO.Martínez-Velázquez,
‘‘Multi-treatmentupliftmodeling,’’inProc.KDD,2020,p.106533,doi:
10.1145/3394486.3403196.
| [30] K. Lee | and       | J. Berger, | ‘‘Cross-treatment |           | gain surface         | and | multi- |     |     |     |     |     |     |     |
| ----------- | --------- | ---------- | ----------------- | --------- | -------------------- | --- | ------ | --- | --- | --- | --- | --- | --- | --- |
| treatment   | uplift,’’ | Inf. Sci., | vol.              | 694, Jan. | 2024, Art.no.119240, |     | doi:   |     |     |     |     |     |     |     |
10.1016/j.ins.2024.119240.
[31] J.L.Hill,‘‘Bayesiannonparametricmodelingforcausalinference,’’Stat.
Sci.,vol.26,no.1,pp.1–27,2011,doi:10.1214/11-STS367.
| [32] P. R. Hahn, | J.  | S. Murray, | and C.     | M. Carvalho,    | ‘‘Bayesian |              | regression |     |     |     |     |     |     |     |
| ---------------- | --- | ---------- | ---------- | --------------- | ---------- | ------------ | ---------- | --- | --- | --- | --- | --- | --- | --- |
| tree models      | for | causal     | inference: | Regularization, |            | confounding, | and        |     |     |     |     |     |     |     |
heterogeneouseffects(withdiscussion),’’BayesianAnal.,vol.15,no.3, NOR ASILAH WATI ABDUL HAMID (Senior
pp.965–1056,Sep.2020,doi:10.1214/19-ba1195. Member,IEEE)receivedthePh.D.degreeincom-
|     |     |     |     |     |     |     |     |     |     | puter science | from | The University |     | of Adelaide, |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------- | ---- | -------------- | --- | ------------ |
[33] M.Dudik,J.Langford,andL.Li,‘‘Doublyrobustpolicyevaluationand
| learning,’’2011,arXiv:1103.4601. |     |     |     |     |     |     |     |     |     | Australia,in2008. |     |     |     |     |
| -------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----------------- | --- | --- | --- | --- |
[34] J. Rehill, ‘‘A gentle introduction to uplift modelling,’’ 2024, From2013to2015,shewasaVisitingScholar
arXiv.2403.03822. with the High Performance Computing Labora-
[35] T. Inoue, K. Yamamoto, and T. Okuno, ‘‘Machine-learning-based het- tory, The George Washington University, USA.
erogeneoustreatmenteffectestimationinrandomizedtrials:APRISMA In 2015, she was awarded the CUDA Teaching
review,’’Trials,vol.25,no.134,pp.1–21,2024,doi:10.1186/s13063-
CentrerecognitionbyNVIDIAandsubsequently
024-07943-0.
establishedtheCUDALaboratoryatherfaculty.
[36] C.Ling,D.Sutherland,F.Johansson,andJ.Wiens,‘‘Causalinference
|     |     |     |     |     |     |     |     | She is currently | the | Deputy Director | of  | the Institute | for | Mathematical |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------------- | --- | --------------- | --- | ------------- | --- | ------------ |
pipelinesforRCTemulation,’’2023,arXiv.2302.03070.
|     |     |     |     |     |     |     |     | Research | (INSPEM), | Universiti | Putra Malaysia. | She | is also | an Associate |
| --- | --- | --- | --- | --- | --- | --- | --- | -------- | --------- | ---------- | --------------- | --- | ------- | ------------ |
[37] A.Maraj,M.Vuković,andD.Hotovec,‘‘Asystematicreviewofuplift
modeling,’’Inf.Process.Manag.,vol.61,no.2,2024,Art.no.103692, ProfessorwiththeDepartmentofCommunicationTechnologyandNetwork,
FacultyofComputerScienceandInformationTechnology.Shehasauthored
doi:10.1016/j.ipm.2023.103692.
|            |           |     |       |        |               |      |        | or co-authored | more | than 80 journal | articles | and | conference | papers. Her |
| ---------- | --------- | --- | ----- | ------ | ------------- | ---- | ------ | -------------- | ---- | --------------- | -------- | --- | ---------- | ----------- |
| [38] P. R. | Rosenbaum | and | D. B. | Rubin, | ‘‘The central | role | of the |                |      |                 |          |     |            |             |
researchhasbeensupportedbybothgovernmentandindustryfunding,with
| propensity | score,’’ | Biometrika, |     | vol. 70, | no. 1, pp.41–55, | 1983, | doi: |     |     |     |     |     |     |     |
| ---------- | -------- | ----------- | --- | -------- | ---------------- | ----- | ---- | --- | --- | --- | --- | --- | --- | --- |
interestsfocusedonparallelanddistributedhigh-performancecomputing,
10.1093/biomet/70.1.41.
[39] A.Caron,G.Baio,andI.Manolopoulou,‘‘Estimatingindividualtreatment cloudcomputing,anddata-intensivecomputing.
effectsusingnon-parametricregressionmodels:Areview,’’J.Roy.Stat. Dr. Abdul Hamid is the Editor-in-Chief of Malaysian Journal of
Soc.Ser.A,Statist.Soc.,vol.185,no.3,pp.1115–1149,Jul.2022,doi: MathematicalSciencesandservesasareviewerforseveralwell-regarded
10.1111/rssa.12824. journalsandinternationalconferenceproceedings.
| 40170 |     |     |     |     |     |     |     |     |     |     |     |     |     | VOLUME14,2026 |
| ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------- |

J.Jiangetal.:DynamicFrameworkforCUPandTreatmentSegmentationviaUpliftModeling
NGKENGYAP(SeniorMember,IEEE)received CHOO WEI CHONG received the bachelor’s
theB.Sc.andM.Sc.degreesincomputerscience degreeinscience(statistics)andtheMaster’sof
fromUniversitiPutraMalaysia,in2001and2005, SciencedegreeinbusinessstatisticsfromUniver-
respectively, and the Ph.D. degree in computer sitiPutraMalaysia(UPM),andthePh.D.andPost-
sciencefromTheUniversityofManchester,U.K., doctoraldegreesinmanagementstudies/decision
in 2015. He is currently a Senior Lecturer with sciencefromtheUniversityofOxford,U.K.Heis
theFacultyofComputerScienceandInformation currentlyanAssociateProfessorwiththeSchool
Technology, Universiti Putra Malaysia. He has of Business and Economics, UPM. His research
authoredarticlesinIEEEACCESSandotherindexed focuses on volatility modeling, high-frequency
journals.Hehasbeeninvolvedinmultipleresearch financial data, machine learning–econometrics
projects, including studies on palm oil production analytics, traffic flow hybridforecasting,text-basedanalytics,andAIapplicationsinhealthcare
analysis, and disruptive technology in construction project management. andtourism.
Hisresearchinterestsincludesoftwarecomponents,businessanalytics,and
softwareengineeringforartificialintelligence(SE4AI)systems.
VOLUME14,2026 40171