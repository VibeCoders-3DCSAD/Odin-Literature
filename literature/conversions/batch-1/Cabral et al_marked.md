---
conversion_metadata:
  converted_at: "2026-07-22T12:32:43Z"
  converter_tool: "markitdown"
  converter_version: "0.1.6"
  source_pdf: "Cabral et al.pdf"
  source_pdf_sha256: "c371849fd977be2e9b6301bbad41ca5d4ff3513c364882a845244b0fe3eec0cb"
  page_count: 43
  markdown_char_count: 567588
---

<!-- PAGE-AWARE EXTRACTION (via pdfminer.six) -->

<!-- PAGE 1 -->

Abstract

In deployment, those assumptions fail:

Davi M. Cabrala,∗, Adriano M. A. Limaa, Gustavo H. F. M. Oliveirab, Adriano L. I. Oliveiraa

aCentro de Informática (CIn), Universidade Federal de Pernambuco, Recife, PE, Brasil
bSistemas de Informação, Universidade Federal de Alagoas, Penedo, AL, Brasil

Non-Stationarity in Financial Time Series: A Unifying Survey on Drift
Detection, Adaptive Learning, and Evaluation

Predictive and decision models in finance are typically validated under assumptions of distributional stability over
the evaluation window.
the data-generating process undergoes structural
change—breaks, regime transitions, and drift—that can invalidate conditional relationships, degrade calibration, and
amplify tail risk precisely when decisions are most consequential. Despite a large literature, results remain hard to
reconcile across econometrics, statistical monitoring, and machine learning due to divergent terminology and incom-
patible evaluation protocols. This survey aims to overcome the fragmentation and provides three concrete tools for
research and deployment under non-stationarity in financial time series: (1) a unified taxonomy of drift and regime
change, (2) a pipeline that connects representation, detection, and adaptation choices, and (3) an evaluation play-
book that supports apples-to-apples comparison. We align terms such as structural breaks, regimes, concept drift,
and dataset shift, and propose a taxonomy along temporal, statistical, spatial, and ontological axes to describe real
drift scenarios consistently. Using this lens, we review drift-aware representations, change detection methods, and
continuous adaptation strategies—from classical sequential monitoring and segmentation to Bayesian, multivariate,
and embedding-based out-of-distribution approaches. We then consolidate evaluation guidance spanning detection
delay, false-alarm control, computational cost, and finance-specific utility. Finally, we highlight emerging directions
(foundation models, multimodal context, parameter-efficient adaptation) and open challenges in benchmark design
and reliable online calibration.

Preprint not peer reviewed

Financial markets are dynamic and inherently non-
stationary systems, in which the data generation pro-
cess alternates between distinct statistical regimes due
to macroeconomic shocks, liquidity crises, regulatory
changes, and shifts in agent behavior [? ? ? ? ].
This phenomenon appears in the literature under various
terms—including concept drift, regime change, struc-
tural breaks, and heteroscedasticity—and directly af-
fects core financial tasks [? ? ? ? ? ] such as price fore-
casting, risk management, order execution, and portfo-
lio allocation [? ? ], creating persistent challenges for

In practice, non-stationarity progressively degrades
the predictive performance and calibration of forecast-
ing models [? ? ? ? ]. Under prequential evalua-
tion, this degradation manifests as systematic increases
in forecast error, unstable decision thresholds, and de-
layed reactions to new regimes—often precisely when
errors are most costly in terms of risk exposure and eco-
nomic decision-making [? ? ? ]. These effects ex-
pose the limitations of stationarity-based assumptions
and motivate approaches capable of anticipating and re-
sponding to distribution shifts as they occur.

Addressing these challenges requires coupling drift-
aware representations with timely change detection and
continuous adaptation [? ? ? ? ? ], while evalua-
tion must explicitly account not only for predictive ac-
curacy but also for detection delay and computational

Keywords:
financial time series, non-stationarity, concept drift, change-point detection, adaptive learning, evaluation protocols

amal@cin.ufpe.br (Adriano M. A. Lima),
gustavo.oliveira@penedo.ufal.br (Gustavo H. F. M.
Oliveira), alio@cin.ufpe.br (Adriano L. I. Oliveira)

predictive modeling in real-world, high-stakes deploy-
ments.

∗Corresponding author. Email: dmc6@cin.ufpe.br
Email addresses: dmc6@cin.ufpe.br (Davi M. Cabral),

Preprint submitted to Neurocomputing

1. Introduction

February 2, 2026

This preprint research paper has not been peer reviewed. Electronic copy available at: https://ssrn.com/abstract=6170273

---

<!-- PAGE 2 -->

constraints [? ? ]. In practice, the effectiveness of this
coupling depends critically on how data are represented,
since informative representations are necessary to make
distribution shifts observable rather than masking them
[? ? ]. This dependency naturally shifts attention to the
role and design of financial data representations under
non-stationarity.

verging across communities. As a result, machine learn-
ing, econometrics, and quantitative finance have largely
evolved in parallel, with limited cross-fertilization and
incompatible frameworks. The absence of a shared tax-
onomy and standardized evaluation hinders cumulative
evidence and slows the adoption of drift-aware methods
in practice, particularly in real-time and high-stakes fi-
nancial settings [? ? ].

With the aim of addressing these gaps, we formu-
late the following research questions: (RQ1) How does
the literature define and categorize the different forms
of non-stationarity in financial time series?
(RQ2)
How can financial series be represented by integrat-
ing endogenous and exogenous information to sup-
port the detection and interpretation of regime changes?
(RQ3) How can distribution shifts be automatically de-
tected over time? (RQ4) How can model learning be
adapted to distribution shifts continuously and effec-
tively? (RQ5) How can detection and adaptation sys-
tems be evaluated under non-stationarity using appro-
priate metrics and protocols? (RQ6) How can detection
and adaptation methods be benchmarked under non-
stationarity? (RQ7) What are the current limitations and
future research directions?

In non-stationary financial environments, data repre-
sentations must capture both endogenous market dy-
namics and exogenous drivers. Embeddings learned
from price and volume series summarize endogenous
behavior, enabling comparisons across historical peri-
ods and the identification of latent regimes beyond clas-
sical indicators [? ? ]. However, market behavior is also
shaped by external forces—such as macroeconomic an-
nouncements, geopolitical events, and firm-level disclo-
sures—which are not observable in price data alone. In-
corporating exogenous information through multimodal
inputs (e.g., news, textual reports, and economic indica-
tors) adds economic context to detected shifts [? ? ? ],
yielding representations that are more expressive under
concept drift and better suited to distinguishing transient
fluctuations from structurally meaningful regime transi-
tions.

Preprint not peer reviewed

In addressing these questions, this work makes four
contributions.
(i) We introduce a unified taxonomy
of drift and regime change phenomena in financial
time series, aligning terminology across machine learn-
ing, econometrics, and quantitative finance (RQ1, Sec-
tion 2).
(ii) We structure the literature around a five-
pillar pipeline—non-stationarity characterization, drift-
aware representations, change detection, continuous
adaptation, and evaluation—and review representative
approaches for representation learning, change detec-
tion, and adaptation (RQ2–RQ4, Sections 3, 4, and
5). (iii) We summarize evaluation metrics, experimental
protocols, and benchmarking practices used in financial
time series (RQ5–RQ6, Sections 6 and 7). (iv) Finally,
we synthesize current limitations and outline open re-
search directions (RQ7, Sections 8 and 9).

With such enriched representations, continuous adap-
tation becomes feasible. Model behavior can be up-
dated through classical mechanisms—including forget-
ting factors and regime-switching structures [? ? ? ? ?
]—as well as through modern architectures that support
lightweight domain adaptation, such as specialized fi-
nancial foundation models [? ? ]. In both cases, contex-
tualized representations enable models to respond more
selectively and interpretably to evolving conditions, bal-
ancing stability and responsiveness to improve robust-
ness in online forecasting and decision-making. How-
ever, the practical relevance of these adaptive gains is
inseparable from how model performance is defined and
measured over time.

Evaluation therefore emerges as a third essential di-
mension, complementing representation and adaptation.
To ensure practical effectiveness, evaluation protocols
must jointly account for predictive performance, detec-
tion speed, false-alarm control, computational budgets,
and economic impact, reinforcing the need for realis-
tic and comparable benchmarks [? ? ? ? ? ? ].
Despite advances along these axes, progress remains
uneven and often confined to specific methodological
traditions, limiting comparability and cumulative evi-
dence.

This survey was developed through an iterative strat-
reading, and synthesis,
egy for literature retrieval,
guided by keyword searches and by the temporal chain-
ing of contributions. Initial searches were carried out
in broad-coverage digital libraries and academic aggre-
gators (e.g., ScienceDirect, IEEE Xplore, ACM Digital
Library, SpringerLink, and Google Scholar), with a pri-
mary focus on publications from 2000 to 2025. When-
ever needed to contextualize modern formulations of
drift and regime changes, we also included a small set of

At a broader level, the theoretical landscape remains
fragmented [? ? ? ? ], with modeling assumptions,
methodological choices, and evaluation practices di-

1.1. Research methodology and related work

2

This preprint research paper has not been peer reviewed. Electronic copy available at: https://ssrn.com/abstract=6170273

---

<!-- PAGE 3 -->

sequential

2. Drifts and Regimes Foundations and Taxonomy

earlier foundational references (e.g., in sequential anal-
ysis, econometrics, and change-point detection).

tional changes and regimes; (4) adaptation mechanisms;
and (5) evaluation and benchmarking. We emphasize
that the goal is not to exhaustively cover all publications
in this rapidly growing area, but to highlight seminal
and representative contributions that clarify concepts,
design trade-offs, and practical implications for finan-
cial deployment.

The corpus was progressively refined based on topi-
cal relevance and usefulness for the proposed synthesis,
complemented by snowballing (backward and forward)
from seminal works, recent surveys, and recurring refer-
ences. This process resulted in a superset of 289 unique
candidate references (deduplicated across sources and
rounds).

This section seeks to answer the question: how does
the literature define and categorize the different forms
of non-stationarity in financial time series? Different
fields — statistics, econometrics, machine learning, fi-
nance, and the natural sciences — propose complemen-
tary taxonomies to address non-stationarity. In this con-
text, there is a broad consensus that non-stationarity
refers to variation, over time, in the statistical or struc-
tural properties of a data-generating process [? ? ? ?
? ]. However, beyond this high-level definition, these
fields differ in the way such changes in the data distri-
bution are formalized, categorized, and analyzed.

Search strings combined three intersecting fronts: (i)
non-stationarity terminology (e.g., concept drift, dis-
tribution shift, regime change/shift, structural break,
change point); (ii) operational mechanisms (e.g., drift
detection, change-point detection,
tests,
adaptive/continual learning, test-time adaptation, re-
training, ensembles); and (iii) financial contexts and re-
alistic protocols (e.g., algorithmic trading, risk manage-
ment, portfolio, volatility, market microstructure, back-
testing, transaction costs). Beyond surveys and reviews,
we also considered experimental and methodological
studies whenever they contributed directly to answering
the RQs and to structuring the survey’s pipeline (foun-
dations, detection, adaptation, and evaluation).

Preprint not peer reviewed

Motivated by these differences in conceptualization
and emphasis, we present an ontology, illustrated in
Figure 1, that describes the non-stationarity problem
in financial time series [? ? ? ? ? ] along four
(i) a temporal axis, which
main classification axes:
characterizes when and how changes unfold over time;
(ii) a statistical axis, which specifies which proper-
ties of the data-generating process are affected; (iii) a
spatial axis, which describes where changes manifest
within the data structure; and (iv) an ontological axis,
which distinguishes the nature and formal status of the
change. Finally, we discuss the causal axis, which iden-
tifies the underlying drivers of non-stationarity, includ-
ing exogenous shocks, endogenous feedback mecha-
nisms, and adversarial or institutional effects, linking
observed drifts and regime transitions to their sources.

A central element of this refinement was examin-
ing the future-work sections of the retrieved papers
and, whenever possible, checking whether the proposed
directions were later investigated or addressed. This
“from-future-to-present” tracking served as a structured
scan of gaps and adjacent research lines: by relating
explicit recommendations to subsequent evidence, we
were able to make persistent gaps explicit and map
emerging themes correlated with regime changes and
concept drift (e.g., GNNs, foundation models, multi-
modality, deep reinforcement learning, and knowledge
representation). After an initial relevance screening
and consolidation to remove near-duplicates and out-
of-scope items, this process yielded a shortlist of 220
references.

In the specific case of time series, non-stationarity
may affect the mean and variance of the very relation-
ship between variables or the mechanism that produces
them. One way to characterize these effects is by focus-
ing on how the changes unfold in relation to the timing
and temporal shape of the change in the process, that is,
how and when the change occurs, for example, as illus-
trated in Figure 2. Common types include abrupt drift,
gradual drift, incremental (or continuous) drift, and re-
current (or seasonal) drift [? ? ? ? ? ? ], but some
surveys also highlight blips (transient deviations / out-
liers) to differentiate short-lived noise from structural

For scope reasons and to preserve coherence with
the RQs and the proposed conceptual pipeline, part
of these adjacent themes was deliberately deprioritized
and not discussed in depth (e.g., topics centered on
MLOps/operational monitoring, temporal fairness, pri-
vacy/federated learning, and vintage data/real-time data
revisions, among others), remaining as opportunities for
future work. The final manuscript therefore cites 174
references.

Finally, the selected studies were organized accord-
ing to their predominant role in an end-to-end pipeline
for financial systems under non-stationarity: (1) foun-
dations and terminology harmonization; (2) represen-
tation and context modeling; (3) detection of distribu-

2.1. Temporal axis

3

This preprint research paper has not been peer reviewed. Electronic copy available at: https://ssrn.com/abstract=6170273

---

<!-- PAGE 4 -->

θ

θ

Local

Global

Abrupt

Regime

∆P(Y)

∆P(X)

Gradual

C2

Recurrent

∆P(Y|X)

Exogenous

Adversarial

Mechanism

Incremental

Endogenous

Causal
why

Spatial
where

Temporal
how/when

Statistical
what

Ontological
structure

Non-stationarity

Abrupt

(A) DGS10

Gradual

changes [? ? ? ? ], which we define below to clar-
ify their temporal dynamics.

Figure 1: Extended taxonomy of non-stationarity along five axes:
temporal (how/when), statistical (what changes), spatial (where), on-
tological (structure/state), with causal drivers (why) as the founda-
tional layer.

transition from an upward-trending regime to a
downward-trending regime, as market conditions
progressively weaken (from a bull market—a pe-
riod of broadly rising prices and optimistic senti-
ment—to a bear market—a period of broadly de-
clining prices and pessimistic sentiment1).

• Incremental / continuous drift: continuous drift
of parameters without a clear breakpoint or sta-
ble plateaus, i.e., without discrete states. Exam-
ples include long-run structural (secular) trends,
such as the multi-decade decline in long-term in-
terest rates [? ? ](Fig. 3A), driven by slow-moving
forces in saving and investment rather than a single
abrupt shock.

Preprint not peer reviewed

• Abrupt drift: sudden change that establishes a
new level almost instantaneously. For instance, the
revelation of a major accounting fraud at a large
corporation may trigger an immediate market-wide
sell-off, abruptly shifting volatility regimes, risk
premia, and correlation structures across related
sectors, with the new price dynamics and investor
sentiment establishing themselves within hours or
a single trading session.

Figure 3: U.S. interest-rate series at macro monthly time scales (sam-
ple: 1962-01 to 2025-12).
(A) 10-year Treasury constant-maturity
yield (DGS10; end-of-period at this frequency). (B) Effective federal
funds rate (FEDFUNDS), summarizing the stance of U.S. monetary
policy. Over this period, the 10-year yield declines from around 14%
in the early 1980s to about 8% in the early 1990s, around 5–6% in
the late 1990s, near 2% in the mid-2010s, and below 1% in 2020.
Policy-rate movements in (B) shape short-term financing conditions
and can transmit to longer maturities in (A) through expectations and
term premia, although the 10-year yield also reflects inflation expec-
tations and broader risk compensation. Source: FRED [? ? ].

Figure 2: Temporal morphology of drifts: Abrupt—sudden change
at changepoint τ; Gradual—transition interval where old and new
concepts coexist and switch with each other gradually; Incremen-
tal—continuous parameter drift without stable plateaus; Recurrent—
alternation between previously observed states.

transition interval in which ob-
servations from the old and new concepts coex-
ist, with a fuzzy boundary (a mixture of states for
some period). A canonical example is the slow

1In equity markets, a common rule of thumb defines a bull (bear)
market as a rise (fall) of about 20% or more in a broad market index
over at least a two-month period [? ? ].

• Recurrent / seasonal drifts: unlike gradual drift,
which describes a one-way transition where old

• Gradual drift:

Incremental

(B) FEDFUNDS

Recurrent

mixture

4

C1

S 2

S 1

τ

θ

θ

t

t

t

t

This preprint research paper has not been peer reviewed. Electronic copy available at: https://ssrn.com/abstract=6170273

---

<!-- PAGE 5 -->

2.2. Statistical axis

• Prior / label / target shift:

The statistical axis specifies which component of the
data-generating distribution changes over time. To un-
derstand, let Pt(X, Y) denote the joint probability distri-
bution governing the generation of input–output pairs at
time t, with the factorization Pt(X, Y) = Pt(Y | X) Pt(X).
Here, Pt(X) defines the probability distribution from
which inputs are drawn, while Pt(Y | X) defines the con-
ditional probability governing the generation of outputs
given the inputs.

change in Pt(Y)
(class/event proportions, or the marginal distribu-
tion of the target). This captures situations where
the frequency of outcomes changes over time, even
if conditional relations are relatively stable. An ex-
ample is a trading signal classifier where the pro-
portion of buy/sell/hold signals changes over time
due to changing market conditions, while the fea-
tures that characterize each signal type remain sim-
ilar.

and new concepts coexist for some time, recur-
rent drift refers to settings in which previously
observed concepts reappear after a period. Sea-
sonal drift is a special case of recurrent drift where
these recurrences follow a deterministic periodic
pattern. For example, trading volume and volatil-
ity patterns may exhibit recurrent behavior tied to
monthly options expiration cycles, quarterly earn-
ings announcements, or annual tax-loss harvesting
periods, with similar statistical properties recurring
at regular intervals.

• Class-conditional shift: change in Pt(X | Y)
with Pt(Y) approximately constant. Again, ap-
proximately" indicates a working approximation:
the marginal prevalence of classes/events is treated
as stable (or controlled for) over the comparison
window, while the feature distribution within each
class moves (e.g., due to measurement, microstruc-
ture, or representation effects). For instance, in
a model predicting order book price movements,
the proportion of upward, downward, and stable
price movements may remain constant, but the or-
der flow patterns characterizing each movement
class evolve as the composition of market partic-
ipants shifts from predominantly retail to institu-
tional traders, or as the prevalence of spoofing and
fake orders changes over time. If Pt(Y) also varies
materially, the setting is better described as a mix-
ture with prior/label shift.

Preprint not peer reviewed

• Covariate / virtual drift: change in Pt(X) while
the predictive mechanism Pt(Y | X) is assumed ap-
proximately invariant. Here, "approximately" re-
flects an idealized assumption: empirically, one
expects Pt(Y | X) ≈ Pt′ (Y | X) on the overlap-
ping support of X (i.e., regions where both periods
assign non-negligible probability mass), up to es-
timation noise and minor residual effects. In prac-
tice, the drift is interpreted as being driven mainly
by context/environment or sampling changes that
move the distribution of inputs. For instance, a re-
turn forecasting model trained on a market index
may face covariate drift when the composition of
the index shifts toward technology companies and
away from traditional manufacturing firms, even
though the relationship between company-level
features (valuation ratios, momentum, volatility)
and expected returns remains stable.

In this taxonomy, categories are defined by the dom-
inant changing term in this decomposition (or, equiv-
alently, in Pt(X | Y) Pt(Y)), i.e., whether the drift pri-
marily affects Pt(X), Pt(Y), Pt(X | Y), or Pt(Y | X).
In practice, however, multiple components may evolve
simultaneously. Accordingly, and consistent with the
dominance-based definition above, the categories below
should be interpreted as idealized descriptors that em-
phasize the primary source of change rather than as mu-
tually exclusive cases.

• Concept (strict sense) / real drift: change in
Pt(Y | X), i.e., a change in the relationship be-
tween inputs and targets (often corresponding to
"structural breaks" or "regime shifts" in econo-
metrics/finance). For example, a price prediction
model may observe that the same technical indica-
tors (moving averages, volume patterns) that previ-
ously signaled upward price movements now pre-
dict downward movements, reflecting a fundamen-
tal change in market dynamics.

Many authors use the term concept drift in a broad
sense, to denote any change in the data-generating pro-
cess ∆P(X, Y), and not only real drift ∆P(Y | X) [? ?
]. In this survey, we adopt the restricted convention: we
reserve “concept drift” for ∆P(Y | X) (real drift) and use
“distribution shift” or “non-stationarity” for the general
case.

To avoid ambiguity, when cited authors use “concept
drift” in the broad sense, we explicitly flag this and map
it to our taxonomy by identifying which term in the stan-
dard factorizations of Pt(X, Y) is drifting. Table 1 sum-
marizes the main terminological equivalences across

5

This preprint research paper has not been peer reviewed. Electronic copy available at: https://ssrn.com/abstract=6170273

---

<!-- PAGE 6 -->

Time

volatility spike

External shock

Shock / stress

)
c
i
t
a
m
e
h
c
s
(

Risky asset (e.g., equities)

Safe asset (e.g., Treasuries)

Reallocation: risk → safety

l
e
v
e
l
d
e
z
i
l
a
m
r
o
N

In the dataset-shift

univariate location statistics;

• First order: change in E[Xt] (mean, trend) or in

• Second order: change in Var(Xt) (volatility) or in

Figure 4: Schematic illustration of flight-to-quality: during stress, in-
vestors shift from risky assets to safer ones, depressing risky prices
and supporting safe-asset prices.

But, in addition to these terminologies, other classic
dimensions of non-stationarity can quantify how much
and which statistical moments have changed[? ? ? ? ?
]:

machine learning, econometrics, statistics, and quanti-
tative finance for broad-sense “concept drift,” mapping
changes in ∆Pt(X), ∆Pt(Y), ∆Pt(Y | X), ∆Pt(X | Y), and
∆Pt(X, Y) to their commonly used names in each com-
munity.

Throughout this survey, we use “distribution/dataset
shift” (or “non-stationarity”) as an umbrella term that
covers both offline (train–test) and online (time-varying)
settings, while reserving “concept drift” for changes in
Pt(Y | X) under our restricted convention. [? ? ]

literature, “dataset/distribution
shift” typically refers to a mismatch between training
and test distributions (i.e., the joint distribution differs
across stages). In contrast, the concept-drift literature
emphasizes online/streaming settings in which the dis-
tribution evolves over time, often affecting the input–
target relationship.

Preprint not peer reviewed

In multivariate settings, drifts may affect variances,
covariance, correlation, and tail dependence across as-
sets. Financial crises are typically marked by an abrupt
increase in tail dependence, with losses converging
across assets that were previously weakly correlated,
leading to the collapse of diversification strategies (see
Fig. 6). Conceptually, such changes can be described
as breaks in covariance matrices, transitions in depen-
dence graphs (financial networks), or changes in dy-
namic copulas that capture asymmetric dependence and
heavy tails [? ? ? ? ? ]. In these episodes, changes
of different orders often coexist: mean shifts associ-
ated with flight-to-quality dynamics (Fig. 4), volatil-

Figure 7 illustrates the typical inverse co-movement
between equity prices and implied volatility: equity
drawdowns often coincide with increases in VIX [? ],
which is computed from S&P 500 index option prices
and is widely used as a market “fear gauge” [? ]. As
an example of a news-driven repricing episode, late-
Jan. 2025 coverage reported a sharp tech-led selloff fol-
lowing DeepSeek-related developments, accompanied
by a spike in volatility expectations [? ? ? ].

ity explosions characterized by abrupt spikes in im-
plied volatility (Fig. 5), and increases in correlations and
tail dependence reflecting crisis contagion mechanisms
(Fig. 6). These phenomena occur in parallel, combining
first-order, second-order, and multivariate effects.

In terms of the statistical axis, first/second-order
tends to manifest as ∆P(X) changes in the features;
∆P(Y) affects marginal statistics of the target; and real
drift ∆P(Y | X) manifests as instability of parame-

2For a univariate series {Xt}, the mean is µt = E[Xt] and the au-
tocovariance at lag h is γ(h) = Cov(Xt+h, Xt); the autocorrelation is
the normalized quantity ρ(h) = γ(h)/γ(0).
In weak (second-order)
stationarity, µt is constant and γ(h) depends only on the lag h (not on
t).

• Multivariate: change in cross-dependence (e.g.,
covariance/correlation across variables or assets)
and tail dependence 3 [? ? ? ? ? ].

3Tail dependence captures extremal co-movement and is often
quantified by coefficients defined as limits of conditional quantile ex-
ceedance probabilities.

Figure 5: Schematic example of a VIX spike: an abrupt jump in im-
plied volatility around a shock, followed by gradual normalization.

Cov(Xt, Xt−k) (autocorrelation)2 [? ? ]; and

4https://github.com/davimcabral/NonStationarityIn

FinancialTS/blob/main/graphic_sp500_vix.ipynb

mean reversion

low-vol regime

Time

l
e
v
e
l

X
V

6

I

This preprint research paper has not been peer reviewed. Electronic copy available at: https://ssrn.com/abstract=6170273

---

<!-- PAGE 7 -->

Normal conditions

lower cross-dependence

Crisis / contagion

(A) S&P 500 and its 125-day moving average

higher correlation and
tail dependence

Tail dependence: co-
movement in extremes
(joint losses become
more likely)

Figure 6: Schematic illustration of crisis contagion in a cross-asset
network. Nodes represent assets (or variables) and edges denote statis-
tical dependence, with thicker edges indicating stronger dependence.
Under normal conditions (left), dependence is weaker and diversifi-
cation is effective. During crises (right), dependence and tail depen-
dence increase, making joint extreme losses more likely and reducing
diversification benefits.

• Global drift, when the change broadly affects the
entire domain, impacting most regions of the fea-
ture space or the majority of subpopulations simul-
taneously. For instance, a central bank interest rate
change typically affects pricing dynamics across
all asset classes and market segments, inducing a
system-wide shift in expected returns and risk pre-
mia.

• Local drift, when the change is confined to spe-
cific regions of the input space, such as a single
economic sector, asset class, geographic market, or
customer group. For example, regulatory changes
affecting only the pharmaceutical sector may alter
the predictive relationships for healthcare stocks
while leaving technology or energy sectors unaf-
fected. These changes are spatially heterogeneous,
often subtle, and more difficult to detect, requir-
ing region-aware or subdomain-sensitive monitor-
ing methods.

Preprint not peer reviewed

Beyond the distinction between global and local ef-
fects, spatial drifts may differ in their structural foot-
print across the feature space. Changes can propagate
smoothly across neighboring regions, remain isolated
within well-defined clusters, or emerge along specific
dimensions while leaving others unaffected. Such pat-
terns reflect the geometry of the input space and the in-
teraction structure among variables, rather than tempo-
ral ordering, and are naturally described through par-
titions of the feature domain, network representations,
or conditional submodels tailored to specific subpopu-
lations.

The spatial axis concerns the reach of a change within
the feature space or across subpopulations, as illustrated
in Fig. 8. It characterizes where in the input domain a
change occurs and how broadly it spreads across vari-
ables, assets, or groups. From this perspective, spatial
changes can be distinguished according to their extent,
ranging from drifts that affect the entire domain to those
confined to specific regions of the feature space, as for-
malized in [? ? ? ], and described below:

Figure 8: Spatial drift in financial time series. (A) Global drift: Dur-
ing the March 2020 COVID-19 market crash, all sectors experienced
synchronized volatility increase and drawdown—drift affects the en-
tire market. (B) Local drift: During the 2014 oil price collapse, only
the energy sector (bold orange) experienced significant drift while
other sectors remained stable. Local drift requires sector-specific de-
tection and adaptation rather than market-wide retraining.

Why do scales matter for the taxonomy? Drifts man-
ifest at different frequencies, and the scale often de-
termines which morphological pattern dominates. At
macro scales (years/decades), drifts tend to be abrupt

Figure 7: Co-movement between equity prices and implied volatility
(daily data). Authors’ own plot. The plotting notebook is available
online.4. Data accessed via FRED (series SP500 and VIXCLS [? ?
]; underlying index data are not redistributed).

ters/coefficients and of conditional dependencies, going
beyond marginal moments [? ? ? ? ? ? ].

(B) VIX and its 50-day moving average

2.3. Spatial axis

— Tech
— Fin
— Energy
— Health

(A) Global Drift: Market Crash

(B) Local Drift: Sector-Specific

— Tech
— Fin
— Energy

All sectors
drop together

Other sectors
stable

7

Mar 2020

— Health

t
f
i
r
d
l
a
c
o
l

Recovery

Recovery

Pre-crash

Oil crash

Returns

Returns

n
o
i
g
e
r

Stable

t
f
i
r
d

drift

t

t

This preprint research paper has not been peer reviewed. Electronic copy available at: https://ssrn.com/abstract=6170273

---

<!-- PAGE 8 -->

t
f
i
r
D

∆P(Y)

∆P(X)

t
p
e
c
n
o
C

Statistics

Joint shift

∆P(X, Y)

∆P(Y | X)

Phenomenon

)
e
s
n
e
s
d
a
o
r
b
(

Non-stationarity

Quant
finance

Market dislocation

Table 1: Terminological equivalences across traditions (broad-sense “concept drift”).

Covariate
shift
Conditional
shift
Target/ marginal
shift

Regime shift
Behavioural
shift
Market regime shift/
non-stationarity

Econometrics
Exogenous shift /
exogenous shock
Structural
break
Endogenous
change

Machine
learning
Covariateshift /
covariate drift
Concept drift
(strict sense)
Label shift /prior-
probability shift
Dataset shift /
distribution shift

through piecewise models with approximate stationar-
ity, where time series alternate between a finite number
of discrete and persistent states separated by change-
points (see Fig. 9). Transitions between regimes may
be abrupt, as during financial crises, or gradual, reflect-
ing slow structural adjustments in the economy.

(policy shocks, interest-rate regime changes; Fig. 3B)
or incremental (secular trends linked to business and
monetary-policy cycles;Fig. 3A) [? ? ? ? ]. At
daily/weekly scales, recurrent drifts prevail, associated
with risk-on/risk-off switches, news cycles and repric-
ing of risk around announcement windows [? ? ? ? ].
At high frequency, intraday seasonality and microstruc-
ture effects (open/close patterns, auctions, lunch breaks)
generate deterministic patterns that overlay structural
drifts observed at longer horizons [? ? ? ]. In crypto as-
sets, boom–bust cycles tend to overlap with these scales,
while deterministic events (such as halvings) act as nat-
ural triggers for regime changes [? ]. Multiscale ap-
proaches [? ? ? ] allow time series to be decomposed
into different frequencies, reveal regimes that remain
hidden at single resolutions, and thus classify drifts ac-
cording to their dominant scale [? ? ? ? ].

Preprint not peer reviewed

A useful way to understand such structural changes
is through the notion of a regime. Intuitively, a regime
corresponds to a persistent mode of operation of the data
generation system. While a regime is in place, data fol-
low relatively stable patterns; when the regime changes,
these patterns are altered in a systematic and lasting
way. In financial markets, common examples include
bull and bear phases, sustained transitions between low-
and high-volatility states, and crisis periods character-
ized by persistently high cross-asset correlations.

This framework helps clarify the relationship be-
tween drift and regime change. Every regime transition
necessarily involves a statistical change. But the con-
verse does not hold, because many drifts arise from con-
tinuous or incremental adjustments that do not introduce
a new regime. For instance, a brief spike in volatility
represents a short-lived deviation, whereas a sustained
period of elevated volatility over several months reflects
a genuine regime change. The distinction between these
cases is illustrated in Fig. 9.

In practice, a change is typically interpreted as a new
regime when it satisfies three broad criteria [? ? ]. First,
the change must be persistent, lasting long enough to
rule out transient noise. Second, it must be distinctive,
meaning that its statistical properties differ meaning-
fully from those observed previously. Finally, regimes
may be recurrent, in the sense that the same state can
reappear over time, although recurrence is not a strict
requirement.

Beyond regime changes, the ontological axis encom-
passes other forms of qualitative transformation in the
data-generating process, capturing changes in what the
system is, rather than only in how its statistical prop-
erties evolve.
In financial applications, such transfor-
mations include shifts between persistent market states,
the emergence of new market categories or instruments,
and structural changes in how data are generated, as il-
lustrated by examples summarized in Table 2.

Not all changes in data correspond to the same type of
structural transformation. Some variations reflect tran-
sient fluctuations around a stable system configuration,
while others signal a deeper change in how the data gen-
eration system operates. The ontological axis focuses
on these qualitative differences between distinct system
states.

These ontological changes intersect with the tempo-
ral, statistical, and spatial axes, but are distinguished by
reflecting modifications in the underlying structure or
semantics of the problem, rather than purely quantita-
tive variation [? ? ? ? ? ? ]. Common empirical drivers

from a modeling perspective,
regimes are often treated as latent states that govern
the data-generating process. This idea is formalized

2.4. Ontological axis

In econometrics,

8

This preprint research paper has not been peer reviewed. Electronic copy available at: https://ssrn.com/abstract=6170273

---

<!-- PAGE 9 -->

0

-1

+1

ρ(t)

t

t

ρ > 0

ρ < 0

State 2

State 1

State 1

Returns

Returns

S 1 → S 2

S 2 → S 1

t
f
i
r
d
m
s
i
n
a
h
c
e
m

structural change

— Stocks — Bonds

Negative
correlation

Positive
correlation

Bull Regime
µ > 0, σ low

Bull Regime
µ > 0, σ low

Bear Regime
µ < 0, σ high

(A) Regime Drift: Discrete States

(B) Mechanism Drift: Relationship Change

2.5. Causes of Non-Stationary

of these changes—such as policy interventions, techno-
logical innovations, or market disruptions—are further
mapped to the corresponding axes in Table 3. Within
this framework, ontological changes can be organized
into the following categories:

Figure 9: Ontological drift in financial time series. (A) Regime drift:
Discrete state transitions between bull and bear markets. Each regime
has distinct statistical properties (µ, σ), but the underlying data gener-
ation mechanism remains consistent within states. Modeled by Hid-
den Markov Models (HMMs), regime-switching models. (B) Mech-
anism drift: Fundamental relationship changes—stock-bond corre-
lation shifts from negative to positive (as observed 2020-2022). The
correlation structure ρ(t) evolves continuously, representing a change
in the causal/structural relationships rather than just state switching.

Table 3 summarizes how these causal drivers map
onto the temporal, statistical, and spatial axes of the
proposed taxonomy, illustrating how different sources
of non-stationarity induce characteristic patterns of drift
across dimensions. In addition, adversarial or manipu-
lative behaviors—such as pump-and-dump schemes or
spoofing practices in less liquid markets—may distort
local signals. These actions often produce short-term
drifts that do not correspond to long-term structural
changes.

From a causal standpoint, drifts and regime changes
can be triggered by exogenous, endogenous, or adver-
sarial factors. Among exogenous drivers, monetary pol-
icy and interest-rate cycles, supply and demand shocks,
financial crises, and geopolitical events stand out. These
forces alter expectations, risk pricing, and risk premia
across different time horizons [? ? ? ? ]. Endogenous
mechanisms arise from within the financial system it-
self. Leverage, liquidity constraints, margin calls, and
feedback dynamics between investor strategies can am-
plify shocks and generate regime transitions even in the
absence of new external events [? ? ? ].

Preprint not peer reviewed

• Mechanism change — modifications to the un-
derlying generative process, such as the introduc-
tion of new variables, rules, or dependencies, even
when observable classes remain unchanged. An
example is the implementation of circuit breakers
or new trading halts that alter market microstruc-
ture, changing how order flow translates into price
movements without necessarily changing the clas-
sification targets (e.g., up/down/neutral price direc-
tion).

At the first level, we consider internal signals derived
from the time series itself, corresponding to endogenous
information. At the second level, we incorporate ex-
ogenous context, representing external information that
influences the observed dynamics. A third layer explic-
itly models the latent structure of underlying states or
regimes as part of the representation, enabling a connec-
tion between observed data and unobserved market con-
ditions. Fourth, we consider representations oriented

• Concept evolution / new classes — the emer-
gence or disappearance of previously nonexistent
target classes, effectively expanding or redefining
the problem’s ontology. For instance, the introduc-
tion of a new asset class (such as exchange-traded
funds or cryptocurrency futures) creates novel pre-
diction targets that did not exist in the training pe-
riod, requiring models to recognize and adapt to
entirely new categories;

At high frequency, market microstructure effects play
a central role. Latency, order flow, tick size, and mar-
ket rules can create specific regimes, such as shallow or
deep order books, narrow or wide spreads, and windows
of elevated microstructural noise. These microstructure-
driven regimes overlay macroeconomic regimes and
contribute to the overall complexity of observed finan-
cial dynamics [? ? ? ].

The purpose of this section is to provide the foun-
dations for addressing the following question: how can
financial time series be represented, and how can inter-
nal and external information be integrated, to support
the detection and interpretation of regime changes? For
this, we adopt a layered approach to representation, il-
lustrated in Fig 10.

• Regime change — transitions between persis-
tent latent states with distinct statistical signatures,
while preserving the same set of target classes
(e.g., bull versus bear markets, low versus high
volatility);

3. Representation and Context

9

This preprint research paper has not been peer reviewed. Electronic copy available at: https://ssrn.com/abstract=6170273

---

<!-- PAGE 10 -->

Local

Local

Local

Cause

Global

Global

Global

Global

Abrupt

Abrupt

Abrupt

Abrupt

Abrupt

∆P(Y)

∆P(X)

∆P(X)

Gradual

Gradual

∆P(Y | X)

∆P(Y | X)

Temporal axis

1st/2nd order in P(X)

Spatial axis
(where)

Typical financial example

Recurrent seasonal regimes

P(X) / P(Y) and 2nd order

Global or
local
Local

Market crash; jump in risk premium

Ontological axis
(structure/state)

Temporal axis (how
and when)

Statistical axis (what
changes)

Table 3: Mapping drift causes to taxonomic axes

January effect; intraday open/close patterns

Table 2: Summary of drift taxonomic axes with financial examples

Incremental /
continuous
Recurrent / seasonal

2nd order (dependence /
tails)
∆P(X | Y)

Sudden downgrade of sovereign or
large-bank credit rating
Regulatory shock in a specific sector

Slow sector rotation (out of one sector into
another)
Secular downward trend in interest rates

Mechanism adjustment
within the same regime
Contagion regime (normal
→ high dependence)
Change in selection
mechanism

Market learning to price a new asset or
technology
Correlation collapse in crises; loss of
diversification
New credit-scoring criterion changing the
profile of approved clients

Regime change (normal →
crisis)
Same set of classes (no new
ontology)
Mechanism change
(regulation / rules)
Same set of classes (flows
within the regime)
Macro regime in slow drift

Preprint not peer reviewed

Classical studies in time-series statistics and econo-
metrics show that a large share of financial drifts mani-
fests as changes in first- and second-order properties of
the series (level, trend, volatility, autocorrelation), or in
more complex forms of temporal dependence [? ? ? ?
? ]. Thus, a natural starting point is to construct diag-
nostic features computed in moving time windows (or
multiple time scales) that capture these statistics. Ex-
amples include:

The goal of these representations is to transform
raw data into a feature space in which regime-relevant
changes become explicit, whether as drifts in embed-
dings, reorganizations of network structures, or varia-
tions in latent indicators. Figure 10 provides a com-
pact roadmap of how we organize drift-aware represen-
tations in this survey.

3.1. Internal Signals and Series Embeddings
Internal Signals. The most basic layer of representa-
tion consists of the internal signals contained in the time
series itself — prices, returns, volumes, spreads, among
others — analyzed through the lens of non-stationarity.
Beyond classical handcrafted statistics, internal signals

can also be summarized through learned representa-
tions. Fig. 11 illustrates this idea: each time window
wt is encoded into a latent vector zt, so that drift can be
monitored as a change in the trajectory {zt} in the em-
bedding space.

Monetary-policy shock
(exogenous)
Liquidity contagion
(endogenous)
Demographic trend
(exogenous)
Pump-and-dump
(adversarial)
Bitcoin halving (exogenous) Recurrent

toward robustness, emphasizing invariance and transfer-
ability across assets, time periods, and market environ-
ments.

• Location and dispersion statistics: moving
means, medians, or quantiles; realized volatility in

Global
(country/region)
Local

∆P(X), 2nd order,
multivariate

Incremental (long-run) ∆P(Y)

Global (crypto
assets)

Manipulation in crypto markets

Surprise interest-rate hike

Supply-reduction events

∆P(Y | X) + ∆P(X)

∆P(X) + ∆P(Y | X)

Cascading margin calls

∆P(X), 1st order

Population ageing

Global (systemic)

Statistical axis

Blip (transient)

(deterministic)

Spatial axis

Example

Gradual

Abrupt

Global

10

This preprint research paper has not been peer reviewed. Electronic copy available at: https://ssrn.com/abstract=6170273

---

<!-- PAGE 11 -->

external

,
l
a
r
o
p
m
e
t

,
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

information

stable features

:
s
e
x
a
y
m
o
n
o
x
a
T

l
a
c
i
g
o
l
o
t
n
o
,
l
a
i
t
a
p
s

Exogenous Context

Robustness & Invariance

Internal Signals
endogenous features

Raw Data: prices, volumes, spreads, news

Latent Structure
states & relationships

Drift-aware representation → Detection (Section 4) / Adaptation (Section 5)

• Regime probabilities P(S t)
• Dynamic graphs (correlations)
• Changepoint posteriors

• Causal/invariant features
• Foundation model embeddings
• Cross-regime stability

• Macro variables (rates, VIX)
• Microstructure (spread, depth)
• News & sentiment (multimodal)

• Moving statistics (mean, var, ACF)
• Multi-scale decomposition
• Learned embeddings zt

• Temporal dependence measures:

rolling windows; measures of skewness and kurto-
sis of returns.

Figure 10: Representation layers for drift-aware financial modeling.
Raw data is progressively transformed through internal signal extrac-
tion, exogenous context integration, latent structure modeling, and
robustness-oriented features, producing representations that feed de-
tection and adaptation systems.

autocorre-
lation and partial autocorrelation coefficients
(ACF/PACF [? ? ]) at several lags; assessment
of long memory via statistics such as long-run vari-
ance or unit-root tests (to identify changes between
stationary and non-stationary trends).

• Multi-scale indicators: features obtained through
wavelet decompositions or low-/high-pass filters at
different horizons, to separate short-, medium-, and
long-term movements [? ? ? ? ]. For example, dif-
ferences in means across scales (detection of trend
changes) or energy metrics in specific frequencies
(detection of emerging/vanishing cycles).

Preprint not peer reviewed

Series Embeddings. In this context, the concept-drift
(broad sense) literature for data streams, together with
advances in deep learning, suggests the need to learn
representations automatically,
rather than manually
specifying all relevant statistics. The objective is to train
a parametric function fθ that maps sequences or time
windows to dense vectors zt ∈ Rd (i.e., temporal em-
beddings), such that periods exhibiting similar behav-
ior are mapped to nearby regions in latent space [? ?
? ? ]. This idea—learning embeddings that represent
the latent state of the series—has become particularly
prominent in non-stationary settings, as learned repre-
sentations are often more effective at capturing com-
plex drift patterns than hand-crafted indicators [? ?
]. Table 4 summarizes the main drift-aware representa-
tion options discussed in this section, providing a struc-
tured overview before we examine specific approaches
in more detail.

These features provide an aggregated view of how
the statistical axis evolves when computed continu-
ously in sliding windows. For example, one can mon-
itor whether the mean or variance of returns exhibits
a significant drift indicating a transition in the volatil-
ity regime [? ? ? ]; track changes in the correla-
tion between an asset and an important risk factor [?
? ? ]; or detect instabilities in the estimated param-
eters of a local model (such as changes in the coeffi-
cients of a CAPM calibrated in rolling windows) [? ?
]. Indeed, many change-detection approaches in finan-
cial time series rely on monitoring such statistics in real
time. However, as the number of series and variables
increases—such as when considering multiple assets si-
multaneously or multiple frequencies (e.g., daily and in-
traday)—relying solely on pre-defined, manually engi-
neered features quickly becomes infeasible.

Figure 11: Learned embeddings for drift detection. Time windows
wt are encoded into latent vectors zt ∈ Rd. Similar market condi-
tions cluster together (bull vs. bear regimes), while drift manifests as
trajectory movement across the embedding space. Changepoint de-
tection can be applied directly to the sequence {zt}.

Embedding Space

Time Series

fθ : wt (cid:55)→ zt

11

encode

z(1)

z(2)

Bear

Bull

drift

w5

w1

w4

w3

w2

z5

z1

z4

z2

z3

xt

t

This preprint research paper has not been peer reviewed. Electronic copy available at: https://ssrn.com/abstract=6170273

---

<!-- PAGE 12 -->

Structure

3.2. Exogenous Context, Multimodality, and Market

In the context of drift detection, operating in the latent
space zt has an advantage: classical changepoint meth-
ods can be applied directly to the embedding series[?
? ]. Techniques such as CUSUM [? ? ], PELT [? ],
or non-parametric (kernel) tests [? ? ? ] can be run
on sequences of vectors zt instead of on the raw data.
Since these embeddings are trained to condense high-
dimensional relevant information (including nonlinear
dynamics) into a few components, a significant change
in series behavior tends to manifest as a detectable shift
in the embeddings. In short, the learned representation
“pre-processes” the data so that relevant changes are al-
ready highlighted, facilitating the detection stage.

As an example, the TS2Vec approach proposed by
Yue et al. [? ] uses hierarchical contrastive learning
to produce embeddings that are robust across multiple
temporal resolutions. Essentially, the model is trained
to generate consistent representations zt for similar sub-
sequences, while separating sequences with distinct pat-
terns. Thus, locally similar windows remain close in la-
tent space, whereas windows corresponding to different
behavior patterns (e.g., bull vs. bear markets, low vs.
high volatility periods) are mapped to distant regions of
the embedding space. Studies report that such learned
embeddings are useful not only for change detection but
also for predictive tasks and anomaly detection in time
series.

tiple horizons, wavelet decompositions, or specialized
layers for capturing distinct frequencies increase sensi-
tivity to drifts at various scales [? ? ? ? ? ? ? ?
]. Rather than deciding in advance on a single “cor-
rect” scale, these architectures internalize multiple fre-
quencies in the representation. This connects directly to
the temporal/morphological axis of the taxonomy (Sec-
tion 2): by simultaneously considering long- and short-
term components, we can detect both gradual long-term
changes and seasonal or abrupt short-term shifts. Stud-
ies in high-frequency markets show that ignoring simul-
taneous scales — for example, analyzing only the macro
trend and ignoring daily/intraday cycles — can lead to
distorted assessments of volatility and regime identifica-
tion [? ? ? ]. Multi-scale embeddings therefore tend to
provide robustness in the detection of complex changes.

Preprint not peer reviewed

A recent line of research goes further and explores
training objectives oriented specifically toward anoma-
lies and drifts. For example, contrastive learning meth-
ods that inject synthetic anomalies or perturbations dur-
ing training, following a philosophy similar to expos-
ing deep networks to outliers [? ]. Here, embeddings
are trained to maximize separation between “normal”
and “altered” patterns. Such approaches include new-
class detection methods in data streams [? ? ] and
self-supervised techniques like the CARLA model for
time series, which uses contrastive objectives calibrated
to highlight temporal anomalies [? ]. The result is to
bring the representation stage closer to the final detec-
tion task: one constructs a latent space designed to make
breaks, novelty events, and out-of-distribution observa-
tions more evident [? ? ? ? ]. In other words, instead
of generic embeddings, one trains embeddings that are
explicitly sensitive to drift.

Macroeconomic and Exogenous Context. The second
representation layer concerns the exogenous context
that influences financial regimes. As discussed in Sec-
tion 2.5, many drifts originate in macroeconomic shocks
and cycles, monetary-policy decisions, liquidity crises,
or geopolitical events [? ? ? ? ? ]. Ignoring these
contextual dimensions can lead to myopic representa-
tions that treat the series as an isolated system when, in
reality, it responds to external factors.

A fundamental strategy is to incorporate macroeco-
nomic and aggregate financial variables as covariates in
the representation model. For example, one might in-
clude series such as short- and long-term interest rates,
inflation indices, activity indicators, credit spreads, risk-
aversion metrics (VIX, etc.), as well as established risk
[? ? ? ? ?
factors (value, momentum, size, etc.)
]. These contextual variables can be integrated into the
representation system in different ways:

Another important consideration is to embed the in-
trinsic multi-scale temporal structure of the data into the
representation [? ? ]. Different changes manifest at dif-
ferent time scales — for example, a secular trend ver-
sus intraday cycles — and choosing a single analysis
scale a priori can lead to blind spots for certain types
of change [? ? ]. Models that integrate filters at mul-

1. Direct feature fusion: includes contextual vari-
ables as additional attributes concatenated to the
internal features of the series in each time window.
That is, the input to the representation model in-
cludes not only attributes derived from the target
series, but also the corresponding values of macro
indicators in that interval.

5A Hidden Markov Model (HMM) assumes a latent regime/state
process S t that evolves as a Markov chain, while observations Yt are
generated conditionally on the current state (via emission distribu-
tions). Inference typically relies on forward–backward recursions and
EM/Baum–Welch-type estimation [? ? ? ].

2. State models with exogenous drivers: in latent-
regime models (such as HMMs5 or MS-VAR 6),

6A Markov-Switching Vector Autoregression (MS-VAR) is a VAR

12

This preprint research paper has not been peer reviewed. Electronic copy available at: https://ssrn.com/abstract=6170273

---

<!-- PAGE 13 -->

to

Yes

aug-

(after

(after

overfit

(hand-

Method

(discrete

Real-time

Limitations

Advantages

TS2Vec [? ]

Low–Medium

Learning Type

pre-
limited

Interpretability

Low (black-box)

None
crafted)

Yes
training)

Yes
training)

High
regimes)

Yes (online
filtering)

Unsupervised
(EM)

Self-supervised
(contrastive)

careful
design;
to
patterns;

High (domain statis-
tics)

Drift-Oriented
Embeddings
(CARLA) [? ]

Self-supervised
(anomaly
con-
trastive)

Requires
anomaly
may
injected
black-box

Regime-Switching
(HMM/MS-VAR)
[? ? ? ? ]

Manual Statistical
Features [? ? ? ?
? ]

Table 4: Comparison of embedding methods for drift-aware financial time-series representation.

com-
Transparent;
putationally
light;
domain knowledge
integration

Requires
training;
interpretability;
sensitive
mentation design

Multi-resolution
robust embeddings;
no labels needed;
captures
complex
patterns

Explicitly sensitive
to drifts; synthetic
anomaly injection;
tailored for detec-
tion

feature
Requires
engineering; limited
to linear/simple pat-
terns; doesn’t scale
to high dimensions

Preprint not peer reviewed

Robustness to dis-
shifts;
tribution
focuses
sta-
relationships;
ble
reduces
spurious
correlations

Generalization; data
efficiency;
lever-
ages
cross-domain
patterns; minimal
training

discrete
Assumes
states;
parametric
assumptions; model
misspecification
risk

Systemic
view;
captures cross-asset
dependencies; net-
work reorganization
detection

Graph construction
scalability
choice;
to large networks;
dynamic edge com-
putation

Real-time
change-
point probabilities;
uncertainty quantifi-
cation;
principled
inference

Computational
para-
complexity;
metric
likelihood
assumptions; tuning
priors

Bayesian
On-
line Changepoint
(BOCPD) [? ? ? ?
? ? ]

Probabilistic regime
interpretable
states;
inte-
transitions;
grates macro drivers

Early signals from
news; rich context;
captures
narrative
drivers

com-
Alignment
plexity;
requires
textual data; modal-
ity fusion design

Domain gap; adap-
tation
needed;
update mechanisms;
interpretability loss

Requires
ment
assumptions
causal
optimization
plexity

Invariant/Causal
Features [? ? ? ? ?
? ]

environ-
annotations;
on
graph;
com-

Graph Neural Net-
works (GNN) [? ?
? ]

Foundation Mod-
els (Pre-trained) [?
? ]

Multimodal (Series
+ Text) [? ? ? ]

Medium (attention
maps)

High (causal struc-
ture)

Supervised
Self-supervised

Supervised
Self-supervised

Self-supervised
(transfer)

Unsupervised
(Bayesian)

Yes (infer-
ence)

Supervised
(IRM)

High
posterior)

Medium
structure)

Yes
training)

Yes
training)

Yes
training)

Low (black-box)

(run-length

Yes
line)

(graph

(after

(after

(after

(on-

13

on

/

/

This preprint research paper has not been peer reviewed. Electronic copy available at: https://ssrn.com/abstract=6170273

---

<!-- PAGE 14 -->

• Impact and resilience metrics: how much the
price moves after a large order (price impact)
and how quickly the market recovers (liquidity re-
silience);

macro variables can act as drivers that modulate
transition dynamics between regimes. For exam-
ple, interest-rate or inflation dynamics can be used
as explanatory variables in the transition probabil-
ities of a Markovian model [? ? ? ? ]. This ap-
proach embeds context into the very state-change
process, increasing interpretability (regimes can be
associated with certain macro levels) and poten-
tially improving the detection of transitions.

Studies with regime-switching and MS-VAR models
in finance suggest that using macro factors as part of
the latent state improves regime separation and the eco-
nomic interpretation of transitions. For example, a two-
regime model can be much more interpretable if one
regime is associated with “high inflation, rising rates”
and the other with “low inflation, stable rates”. Repre-
senting this context in the model state helps avoid spu-
rious or practically meaningless regime detections.

3. Joint multimodal embeddings: in deep architec-
tures, one can train a network to learn joint rep-
resentations that combine prices with macro indi-
cators and other factors. In this case, rather than
simply concatenating series, it is common to em-
ploy sub-networks or cross-attention mechanisms
that integrate the modalities. The network then
produces a unified embedding that simultaneously
encodes the behavior of the financial series and its
associated macroeconomic context [? ? ].

Together, these indicators make it possible to iden-
tify early signs of liquidity stress or structural changes
in market functioning. Empirical studies show that such
microstructure indicators can anticipate very short-term
drifts related to phenomena such as flight-to-liquidity,
liquidity crunches, or localized stress phases in specific
markets [? ? ? ]. That is, before a broader risk
regime is established, we often observe deterioration
in microstructure indicators (e.g., widening spreads, re-
duced depth) that signal a loss of liquidity. Incorporat-
ing these signals into the representation makes it reflect
the current state of microstructure, which often precedes
broader changes in price/risk regimes. In contrast, a rep-
resentation based solely on aggregated prices may fail to
capture these subtle structural changes.

Preprint not peer reviewed

Multimodal Context and Textual Information. In ad-
dition, an important aspect is the multimodality of infor-
mation. Financial series rarely exist “alone”: markets
are constantly influenced and contextualized by tex-
tual information — newspaper articles, analyst reports,
social-media posts, corporate and regulatory announce-
ments, among others. Many disruptive events appear
first as news or narratives before being fully reflected
in prices. This motivates a class of multimodal repre-
sentations that combine numerical time-series data with
textual sources (and possibly other modalities, such as
chart images, sentiment data, etc.).

Market Microstructure Context. The same principle
applies at finer temporal resolutions, where the rele-
vant context is no longer macroeconomic but structural.
At high-frequency time scales, market dynamics are
strongly shaped by market microstructure effects.
In-
traday behavior exhibits systematic patterns (opening,
midday, closing, and auction periods) as well as dis-
tinct liquidity regimes throughout the trading day. As
a result, representations designed for drift and regime
detection at these horizons benefit from incorporating
microstructure-related information, such as:

Figure 12 provides an overview of the main mul-
timodal fusion strategies, organized according to the
stage at which information from different sources is in-
tegrated within the modeling pipeline. Depending on
how modalities are combined, integration can occur at
different processing stages:

• Early fusion: combine numerical and textual rep-
resentations at the outset, for example, by con-
catenating series embeddings with news embed-
dings corresponding to the same time window.
Each time window is then represented by a joint
[series + text] vector.

• Intermediate fusion (cross-attention): use cross-
attention mechanisms between time sequences and
text sequences. For example, a transformer model
in which relevant news influence — via attention
— the learned representation of market data at that
time. This allows the final series representation to

model whose parameters (e.g., intercept, autoregressive matrices, and
often shock covariance) depend on a latent regime S t governed by a
Markov chain, allowing the multivariate dynamics to switch across
regimes (e.g., low vs. high volatility) [? ? ? ].

• Order flow: metrics of aggressiveness vs. passiv-
ity of orders; buy/sell imbalance in the order book;

• Order-book indicators: bid–ask spreads, depth
(volume) available on each side, book changes;

14

This preprint research paper has not been peer reviewed. Electronic copy available at: https://ssrn.com/abstract=6170273

---

<!-- PAGE 15 -->

zt

zt

Alert

Tech

Merge

Concat

Detector

Detector

Finance

Text
dt

Text
dt

Text
dt

Series
xt

Series
xt

Series
xt

Cross-Attention

Text
Encoder

Text
Encoder

Series
Encoder

Series
Encoder

Joint
Encoder

High correlation

Late Fusion

Early Fusion

Crisis Market

Normal Market

Intermediate
(cross-attention)

be modulated by textual content, amplifying or at-
tenuating movements according to the presence of
explanatory news.

Figure 12: Multimodal fusion strategies for integrating time series and
textual data. Early fusion: inputs concatenated before joint encod-
ing. Intermediate fusion: separate encoders with cross-attention to
exchange information. Late fusion: independent processing pipelines
merged at the decision level.

• Late fusion: combine only at the end the out-
puts or alerts originating from detectors special-
ized in each modality. In this case, one could have
a change detector operating on series and another
analyzing news, and then merge detections (e.g.,
flag a change only if both agree, or use text as con-
firmation that a quantitative signal corresponds to
a real event).

important to account for the structure of interrelation-
ships in the market as a dynamic graph. In multivari-
ate settings, drifts rarely affect a single asset in isola-
tion — typically, there is a reorganization of dependen-
cies among assets. For example, in a given regime,
economic sectors form clusters with high intra-cluster
correlations and lower inter-cluster correlations; dur-
ing crisis periods, correlations across most asset pairs
tend to rise simultaneously and may approach unity,
signaling a collapse of diversification and strong sys-
temic contagion. Likewise, measures of tail depen-
dence can change, revealing new channels of extreme
co-movement [? ? ? ? ? ]. Representing each series in-
dividually ignores this cross-information, whereas rep-
resenting the system as an evolving graph allows us to
capture co-movement regimes.

Preprint not peer reviewed

This intuition is illustrated in Figure 13, contrasting a
sector-clustered correlation structure in normal periods
with the dense, near-uniform dependence typically ob-
served during crisis episodes. In such a graph, we typi-
cally define nodes representing financial entities (assets,
indices, sectors, or countries) and weighted edges en-
coding some statistical or economic relationship among
them. Edges may reflect, for example, estimated corre-
lations or co-movements, measures of nonlinear depen-
dence (tail copulas), exposure–credit relationships be-
tween institutions, or capital flows across markets. Edge
weights vary over time, and regime changes appear as
abrupt or gradual reconfigurations in network topol-
ogy/weights. Examples include: during a financial-
contagion event, sector clusters may dissolve and all
nodes become highly interconnected; in subtler tran-
sitions, a new systemic hub may emerge (an asset or
sector that starts to lead dynamics), or some links may
weaken while others strengthen, reshaping the correla-

These fusion strategies are not merely conceptual;
they are increasingly adopted in recent research on mul-
timodal time-series analysis and Large Language Mod-
els (LLMs). In particular, studies on applying LLMs to
time series highlight architectures that perform tempo-
ral alignment and information fusion across numerical
series, text, and other sources [? ? ? ]. From the per-
spective of regime detection, the key advantage is that
events described primarily in text (e.g., political or regu-
latory news that anticipates a market shift) can influence
the joint representation before the corresponding move-
ment is fully reflected in prices [? ? ? ].

As a result, distances in multimodal space thus cap-
ture the combined effects of numerical and narrative sig-
nals: two periods will only be considered similar if both
the quantitative patterns and the news context are simi-
lar. This enrichment can reduce false negatives (missing
a change because the model did not “understand” that
the news implied a new regime) and also false positives
(distinguishing price drops caused by concrete events
from those due to noise, via the presence or absence of
textual explanations)[? ? ? ? ].

Figure 13: Dynamic correlation networks. Normal market: stocks
cluster by sector with sparse inter-sector connections. Crisis market:
correlations increase dramatically across all sectors (correlation col-
lapse), with dense interconnection replacing the community structure.
This regime change is captured by time-varying graph representations.

Market Structure and Inter-Asset Dependencies. Be-
yond individual series and external signals, it is also

15

Dense, correlated

Sparse, clustered

Consumer

Energy

crisis

This preprint research paper has not been peer reviewed. Electronic copy available at: https://ssrn.com/abstract=6170273

---

<!-- PAGE 16 -->

t

t

τ

τ

τ

0

1

1

2

3

xt

Bull

Bear

Crisis

P(S t )

P(Bull)

Recovery

Observed
Series

Regime
Probabilities

tion network.
The recent

such as the predicted probability of remaining in the cur-
rent regime or the expected regime duration.

In this sense, latent regime probabilities provide a
compact and interpretable summary of the system state,
integrating information from multiple variables into a
small set of indicators. Figure 14 illustrates this idea:
regime transitions appear as crossovers in the filtered
probability paths, yielding drift-aware signals that are
suitable for both detection and adaptation.

Recent financial models combine this graph-based
approach with multimodality (prices + indicators +
news), producing unified representations that account
for relationships among assets together with economic
context [? ]. In practice, node and graph embeddings
can serve directly as inputs to change detectors (Sec-
tion 4) — for example, by monitoring the time series of
the graph embedding to detect breaks in the correlation
network — or as additional context for regime-based
adaptation mechanisms (Section 5), guiding models to
treat groups of affected assets jointly [? ? ? ? ? ? ? ? ].

literature on Graph Neural Networks
(GNNs) for time series provides a framework for
learning embeddings that encode such complex spatio-
temporal dependencies [? ? ]. Essentially, dynamic-
graph models can learn both a representation for each
node (asset) and a representation for the graph as a
whole at each time interval. These network embeddings
capture the current state of the financial structure — for
example, they may encode that there are currently two
weakly correlated clusters, or that a given asset is ab-
normally connected to others, indicating stress. Regime
changes then manifest as changes in these embeddings:
a shift indicating that the graph topology has changed
significantly.

Preprint not peer reviewed

such as
Bayesian Online Changepoint Detection (BOCPD) and
its non-parametric extensions provide an alternative yet
they estimate, at each time t,
related representation:
the posterior distribution of the run-length (time elapsed
since the last change) and of current model parameters
[? ? ? ? ? ? ].
In practice, BOCPD computes,
at each new datum, a probability pt(changepoint) in-
dicating how likely it is that a change occurred at that
point, and maintains parameter distributions under the
no-change hypothesis.

Latent-State and Regime-Based Representations..
One prominent class of approaches within this perspec-
tive relies on latent-state models with explicit regimes.
Classical regime-switching models—such as HMMs,
MS-VAR, or regime GARCH—represent the system as
a finite set of discrete states, each associated with dis-
tinct statistical properties, and define transition proba-
bilities among these states [? ? ? ? ].

The time series of these change probabilities and state
statistics (for example, the posterior distribution of the
currently active level or variance) become, themselves,
rich representations of the degree of change perceived
by the model.
It is like a continuously updated “evi-
dence panel”: if pt(changepoint) rises abruptly, we have
a strong indication of drift; if uncertainty about param-
eters increases, this points to structural instability.

This subsection introduces representation strategies
oriented toward robustness and interpretability. The
goal is to construct representations that remain stable
under distribution shifts while providing economically
meaningful signals of regime changes. A natural way to
achieve this is to make regimes explicit in the represen-
tation itself, so that changes correspond to transitions
between interpretable system states.

In summary, latent-state models (whether classical
HMMs or online Bayesian methods) provide regime-
oriented representations — mapping data into probabil-
ities of scenarios — that both robustly capture relevant
changes and enhance interpretability (since they make
explicit “I am X% in regime A and Y% in regime B

From a representation standpoint, fitting such a
model amounts to mapping each time point to a vec-
tor of regime-membership probabilities, obtained either
in real time (filtered) or a posteriori (smoothed). These
vectors may be complemented by derived quantities,

Figure 14: Regime probabilities from a latent-state model (e.g.,
HMM). Top: observed series with regime-colored background. Bot-
| x1:t) for each regime. Transitions
tom: filtered probabilities P(S t
manifest as probability crossovers at changepoints τ1, τ2, τ3. These
probabilities serve as drift-aware features for detection and adapta-
tion.

3.3. Representations Oriented Toward Robustness and

From a Bayesian standpoint, models

Interpretation

16

P(Crisis)

P(Bear)

This preprint research paper has not been peer reviewed. Electronic copy available at: https://ssrn.com/abstract=6170273

---

<!-- PAGE 17 -->

]

now”).

cent studies show that causality-inspired models can
yield more robust forecasts precisely in turbulent peri-
ods, when spurious relationships change and only struc-
tural links remain[? ? ? ? ? ]. This suggests that
invariant representations not only help detection (reduc-
ing noisy false alarms due to superficial variations) but
also serve as a basis for adaptive models that maintain
performance under drift.

In response, a class of methods has emerged that aims
to learn features invariant to environmental changes,
drawing on ideas from Invariant Risk Minimization
(IRM) [?
and related frameworks. Rather than
optimizing only average predictive performance on
historical data,
these approaches impose constraints
or
regularizers that penalize excessive dependence
on environment-specific components, encouraging the
model to rely on more stable and transferable relation-
ships [? ? ? ? ].

Foundation Models and Universal Embeddings..
Along the same line of pursuing robust and transferable
embeddings, recent work explores time-series founda-
tion models as providers of universal embeddings. In-
spired by the success of large pre-trained models in lan-
guage and vision, researchers have examined whether
large-scale time-series models, pre-trained on heteroge-
neous collections of series, can serve as backbones for
diverse financial tasks [? ? ]. The idea is that a neural
model trained on a wide range of domains and frequen-
cies learns embeddings of windows or entire series that
carry temporal knowledge in a general way—capturing
seasonal patterns, typical reactions to shocks, etc.—and
that these embeddings can later be specialized to fi-
nance.

Causal and Invariant Representations.. While this
approach achieves robustness by explicitly modeling
regime transitions, a complementary line of work seeks
robustness at a deeper level: by identifying representa-
tions that remain valid across changing environments.
This motivates a group of techniques focused on causal
and invariant representations. The dataset-shift litera-
ture in classification emphasizes that many drifts arise
from changes in confounders or in the surrounding envi-
ronment—altering P(X) or jointly P(X, Y)—while cer-
tain underlying causal relationships remain stable over
time [? ? ? ? ? ]. For example, an investment strategy
may fail in a new regime because it relied on a spurious
correlation that held historically but later vanished, even
though the fundamental causal drivers of returns per-
sisted (e.g., a macroeconomic factor whose effect was
previously masked).

Preprint not peer reviewed

Instead of training a representation model from
scratch on often limited market- or asset-specific data,
(1) using the pre-
one can adopt strategies such as:
trained foundation model as a fixed feature extractor
and applying change detectors to the embeddings it gen-
erates; or (2) performing light adaptation (fine-tuning),
adjusting only the final layers to specialize the repre-
sentation to the financial domain [? ? ? ]. Both ap-
proaches aim to leverage the inductive bias contained
in large-scale pretraining—for example, a foundation
model may already “know” how to represent macro cy-
cles or common shocks; even if the asset in question has
never experienced a given regime in the available his-
tory, the model may recognize analogous patterns from
other contexts and thus generalize better under moder-
ate shifts.

In financial contexts, this amounts to seeking repre-
sentations that privilege structural drivers (e.g., risk pre-
mia genuinely linked to economic fundamentals) and
downweight correlations that, although effective in a
given regime, are peculiar to that environment and do
not persist outside it. As an example, imagine a repre-
sentation of equities that emphasizes fundamental fac-
tors (valuation metrics, earnings growth, etc.) and is
less sensitive to short-term technical factors whose sign
may flip when the regime changes — such a represen-
tation tends to be more robust to market shifts, because
fundamentals persist while transient technical patterns
may disappear.

From a pipeline perspective, embeddings provided
by foundation models enter as enriched internal signals,
representing the series through vectors of advanced fea-
tures. This is a rapidly evolving area; although promis-
ing, it requires careful assessment of whether patterns
learned from other domains apply to specific financial
contexts, as well as mechanisms for updating the foun-
dation model when the very “universe” of series evolves
(for example, new data types or post-2020 dynamics).
Well-designed representations not only increase sensi-
tivity and timeliness in identifying changes, but also
facilitate the economic interpretation of the resulting

In practice, building invariant representations may in-
(i) selecting features whose relationship with
volve:
returns remains stable across subperiods or regimes
(identifying “resilient” variables whose estimated coef-
ficients vary little between regimes); (ii) training em-
beddings with objectives that enforce predictive consis-
tency across multiple environments (e.g., different mar-
ket windows); (iii) integrating with latent-state models
that make environments/regimes explicit and penalize
excessive variation in causal effects across states. Re-

17

This preprint research paper has not been peer reviewed. Electronic copy available at: https://ssrn.com/abstract=6170273

---

<!-- PAGE 18 -->

tions

4. Change Detection

3.4. Design Guidelines for Drift-Aware Representa-

regimes—since they connect each drift alarm to under-
standable internal signals and potential structural mech-
anisms.

• Gradual or long-term changes (e.g., persistent
volatility increases): use longer rolling windows
or multi-scale embeddings to track slow drifts, ac-
cepting later detection in exchange for stability.

Table 5 summarizes practical choices for representa-
tion and monitoring under different drift scenarios, link-
ing observable drift patterns to concrete signal families
In practice, representation design
and failure modes.
can be guided by a small number of recurring situations:

• Abrupt shocks (e.g., crashes, policy announce-
ments): monitor short-window statistics (mean,
variance) or regime probabilities from HMMs.
These signals react quickly and are suitable for
early warning, but may trigger false alarms under
temporary noise.

To synthesize these perspectives, 4.6 provides a com-
pact overview that links the types of change defined by
the taxonomic axes to suitable detection strategies. This
overview serves as a practical guide for method selec-
tion, while also emphasizing how the choice of the ob-
served signal and the representation space shapes detec-
tor behavior and interpretability [? ? ? ]. Together,
these elements connect methodological decisions to the
effective detection of different forms of drift in real-
world data.

This Section addresses the research question: How
can drifts in data be automatically detected over time?
To answer it, we organize the discussion around the
main methodological paradigms used in practice. We
first cover retrospective segmentation methods, which
identify changes after observing a full data window
(4.1). We then move to sequential (online) monitor-
ing techniques, designed to trigger alarms as data ar-
rive (4.2), followed by Bayesian approaches that model
regime changes probabilistically (4.3). The section fur-
ther examines detectors operating in learned representa-
tion spaces and out-of-distribution settings (4.4), as well
as methods that target changes in multivariate depen-
dence structures (4.5).

Preprint not peer reviewed

Segmentation methods seek to partition the historical
time series X1:T = X1, . . . , XT , where T denotes the total
number of observations and Xt the observation at time t,
into approximately stationary segments, retrospectively
optimizing the changepoint locations that best explain
the data.
In this setting, it is assumed that the series
is generated by a sequence of distinct regimes indexed
by r, each associated with a probability distribution (or
model) P(X | θr), where θr denotes the set of parameters
characterizing regime r. Each regime is approximately
stationary within its corresponding segment, and regime
changes correspond to breaks in the underlying distribu-
tion or, equivalently, in the parameters θr.

In some cases, segmentation is applied not directly
to X, but to representations Z = f (X) or Z = f (X, Y)
(for example latent factors or features extracted from re-
turns and covariates), so that one searches for breaks in
P(Z) over time. Segmentation algorithms then apply op-
timization routines (exhaustive or approximate) to find
the optimal partition in terms of a global cost criterion
[? ? ? ].

Taken together, the checklist and table emphasize a
the representation should match the
simple principle:
dominant form of drift one expects to face. Fast sig-
nals favor sensitivity, stable embeddings favor robust-
ness, and interpretable regimes favor control and diag-
nosis.

• Externally driven changes (e.g., news, narratives):
combine prices with textual data through multi-
modal embeddings to capture signals before they
appear in returns, while accounting for alignment
and scaling issues.

• Asset- or sector-specific drift: use dependency-
based representations (graphs, tail dependence) to
detect changes in correlations and contagion pat-
terns, noting that estimates may become unstable
in small samples.

• Frequent regime switching: adopt latent-state mod-
els (HMM, MS-VAR) and track regime probabil-
ities or expected durations; performance depends
on correctly specifying the number of regimes.

• Need for robustness across market conditions: fa-
vor invariant or causal representations to reduce re-
liance on regime-specific correlations, at the cost
of discarding some short-term predictive signals.

A classical approach is the minimization of an ad-
ditive cost criterion. One defines an intra-segment cost

4.1. Segmentation (retrospective optimization)

18

This preprint research paper has not been peer reviewed. Electronic copy available at: https://ssrn.com/abstract=6170273

---

<!-- PAGE 19 -->

or

or

(cid:1),

secular

statistics,

correlation

Abrupt drift

(price +

Delayed detection

Spurious
drift

Drift characteristic

Estimation instability

Principal failure mode

Regime misspecification

Signal / feature family

Table 5: Design checklist linking drift taxonomy axes to representation choices.

Early-warning indica-
tor

False alarms due to tran-
sient noise

Gradual
drift
Regime switching

text) embeddings
Invariant / causal repre-
sentations

Algorithm 1: PELT: Pruned Exact Linear Time
Input: Time series x1:n = (x1, . . . , xn); cost function

Alignment and modality
noise
Loss of short-term pre-
dictability

that usually coincides with a negative log-likelihood, for
example

Sharp changes in mean,
regime
variance,
probability
Slow but persistent fea-
ture drift
Probability crossovers,
duration shifts
Rewiring of dependency
clusters
Text-led divergence be-
fore price moves
Stability across environ-
ments

Short-window statistics,
BOCPD, HMM proba-
bilities
Multi-scale
embeddings
HMM / MS-VAR latent
states
Graph embeddings, tail
Localized or sectoral
drift
dependence
Narrative-driven drift Multimodal

Preprint not peer reviewed

Once the segmentation framework and optimization
algorithms are defined, a key modeling choice con-
cerns which aspect of the data-generating distribution
is targeted by the cost function. Segmentation methods
therefore require specifying whether changes are sought
in the mean (location parameters), variance or covari-
ance structure, or in the full distribution of P(X) or P(Z).
The choice of contrast statistic directly determines
the type of changepoint that can be detected. Mean-
based contrasts primarily identify level shifts, while
variance-based contrasts are sensitive to changes in
volatility. More general distributional contrasts, such
as density-based measures, divergences, or energy

C(a, b) ≈ − log p(cid:0)Xa:b | ˆθa:b
where Xa:b is the data block in the segment and ˆθa:b are
parameters estimated under the hypothesis that, in that
interval, the distribution P(X) (or P(Z)) is stationary. A
cost is then added for each break introduced (a penalty
as a function of the number of segments). Algorithms
such as Bai & Perron [? ] implement exhaustive search
for multiple structural breaks by minimizing the total
penalized cost.

Another more efficient method such as PELT (Pruned
Exact Linear Time) [? ], summarized in Algorithm 1,
use a dynamic-programming recursion with pruning
rules that exploit the additive structure of the cost func-
tion C to discard suboptimal candidates, achieving lin-
ear computational cost in many practical settings, with
the penalty β controlling the number of detected change-
points.

// Find optimal previous changepoint
(F(t), τ∗) ← minτ∈Rt−1
cp(t) ← cp(τ∗) ∪ {τ∗} ;
configuration

Output: Set of changepoint locations
T = {τ1, . . . , τK}

// Optimal cost up to time 0
// Candidate set of last

13 Penalty: β = c · log n (BIC-type); higher β ⇒ fewer

14 Typical use: Offline segmentation; multiple breaks;

12 Cost functions: CL2 (mean shift), CGauss (variance),

11 Complexity: O(n) average case with pruning, O(n2)

Rt ← {τ ∈ Rt−1 ∪ {t} | F(τ) + C(xτ+1:t) ≤ F(t)}

3 cp(0) ← ∅ ;
4 for t = 1 to n do

long series
15 References: [? ? ]

9 T ← cp(n) \ {0} ;
(exclude 0)

// Prune: remove candidates that

// Changepoints up to time 0

1 F(0) ← −β ;
2 R0 ← {0} ;

(cid:2)F(τ) + C(xτ+1:t) + β(cid:3)

// Extract changepoints

CRBF (nonparametric)

cannot be optimal

// Store best

changepoints

C(·); penalty β

changepoints

10 return T

7
8 end

worst case

19

6

5

This preprint research paper has not been peer reviewed. Electronic copy available at: https://ssrn.com/abstract=6170273

---

<!-- PAGE 20 -->

time series.

4.2. Sequential Methods (online monitoring)

distances, allow the detection of broader structural
changes. In practice, segmentation often relies on sim-
ple within-segment models, including constant means,
regressions, or AR/ARMA processes, with
linear
changepoints corresponding to shifts in the regime-
specific parameters θr.

Beyond these canonical algorithms, there is a broad
family of techniques that build upon segmentation as
a basic block. Non-parametric extensions, such as
E-Divisive, energy-distance segmentation, and kernel
change point methods (kernel CPD), allow the detection
of breaks in complex distributions P(X) or P(Z) without
specifying an explicit parametric model, and are par-
ticularly useful for financial series with heavy tails and
asymmetries.

Sequential methods perform detection in real time,
examining the series continuously as new data arrive.
In probabilistic terms, one typically assumes a “pre-
change” distribution P0(X) and a “post-change” distri-
bution P1(X) (or, more agnostically, one seeks to detect
when Precent(X) starts to differ from Pbaseline(X)). The
goal is to trigger an alarm as quickly as possible af-
ter a change in P(X) occurs, while controlling the false
alarm rate. These methods typically maintain a window
or adaptive model and apply recurrent statistical tests.

A classic example is the CUSUM (Cumulative Sum)
test and its variants, detailed in the Algorithm 2, which
monitor the accumulated deviation of a statistic (for ex-
ample the mean of Xt or of a residual) relative to a refer-
ence value associated with P0(X), signaling a change
when this deviation exceeds a threshold. The choice
of the decision threshold and reference value (and the
implied false-alarm/delay trade-off). In its likelihood-
ratio formulation, CUSUM accumulates contrasts of
the form log p1(Xt)
p0(Xt) , approximating optimal detection be-
tween P0(X) and P1(X) under certain assumptions. An-
other example is the approach of Page–Hinkley, which
states that derivatives follow a similar logic [? ].

An important characteristic is that segmentation
methods provide a set of estimated changepoints for
the entire series (off-line mode), being suitable for ex-
ploratory analysis or historical validation of regimes.
They do not operate in real time, but often offer high
precision in ex post localization of significant changes
in P(X) or its parameters, especially when combined
with robust stopping criteria (penalties) that avoid over-
segmentation (inserting breaks where there is only
noise) [? ? ]. For example, techniques such as the Barry
& Hartigan method [? ] use partition models and priors
for optimal segmentation with uncertainty, obtaining a
posterior distribution over partitions of the series into
approximately stationary blocks in terms of P(X).

Preprint not peer reviewed

Another common formulation compares two win-
dows: a recent sliding window, associated with an em-
pirical distribution Precent(X), versus a past window or
long-term estimate Pbaseline(X). Online two-sample test
techniques, such as ADWIN and other drift detectors in
data streams, continuously compute the statistical dif-
ference between these empirical distributions (e.g., in
terms of mean, variance, or non-parametric measures
of divergence) and perform sequential hypothesis tests,
shrinking or expanding windows as needed to confirm
a change in P(X). Algorithms such as DDM, EDDM,
etc., are used in the data-stream literature to monitor er-
ror metrics of a classifier over time – that is, an aggre-
gated loss function Lt = ℓ(Yt, ˆYt) when pairs (Xt, Yt) are
available – and trigger alarms when there is a significant
increase in these metrics –indicating concept drift (strict
sense) in P(Y | X) [? ? ? ].

Narrowest-Over-Threshold (NOT), in turn, priori-
tizes the smallest interval whose contrast exceeds a
threshold, producing well-localized estimates of fea-
tures such as jumps in the mean or changes in slope and
generalizing to different types of structural change [? ].
In summary, segmentation methods frame change-
point detection as an offline optimization problem, in
which a time series is retrospectively partitioned into ap-
proximately stationary regimes by minimizing a penal-
ized global cost. Their effectiveness depends jointly on
the choice of representation (X or Z), the intra-segment
cost function, and the penalty controlling model com-
plexity. As a result, segmentation provides a flexible
and principled way to identify structural breaks and
regime boundaries in historical data, serving as a foun-
dational tool for exploratory analysis, regime charac-
terization, and downstream modeling in non-stationary

A central challenge in these methods is controlling
the trade-off between rapid detection and false alarms.
Thresholds that are too sensitive lead to frequent alarms
due to random fluctuations in P(X); high thresholds are
slow to react to real changes. For this reason, several
techniques use results from sequential stopping theory:
for example, defining thresholds that guarantee a certain
level of ARL0 (Average Run Length) for false detec-
tions – that is, on average, how long a change-free pe-

Multi-scale methods based on random sub-intervals,
such as Wild Binary Segmentation (WBS) and its exten-
sion WBS2, explore a large number of candidate seg-
ments to locate multiple changepoints, including sce-
narios with frequent breaks and very short spacing be-
tween drifts [? ? ].

20

This preprint research paper has not been peer reviewed. Electronic copy available at: https://ssrn.com/abstract=6170273

---

<!-- PAGE 21 -->

5

// Standardize

// Cumulative sum for upward

// Cumulative sum for downward

3 for t = 1 to n do
4

Output: Detection time τ or ∅ (no detection)

1 S + ← 0 ;
shifts
2 S − ← 0 ;
shifts

riod under P0(X) lasts until a false alarm occurs. Well-
known sequential methods such as Shiryaev–Roberts or
multivariate CUSUM calibrate thresholds via the de-
sired ARL0 [? ? ].

Algorithm 2: CUSUM for Mean Shift Detec-
tion
Input: Data stream x1, x2, . . . , xn; in-control mean µ0;
standard deviation σ; threshold h; slack
parameter k (typically 0.5)

Both approaches are necessary in financial applica-
tions, because online monitoring is used to detect struc-
tural changes in production: for example, warning that
a risk model has started to fail because P(X) or P(X, Y)
has changed. So that portfolio correlations, the distribu-
tion of P&L, or the rate of VaR violations are no longer
compatible with the historical regime.

Some efficient implementations (for example, using
low-complexity non-parametric tests) allow detectors to
run in streaming on market data. It is worth noting that
many sequential methods assume some knowledge of
P0(X); in contrast, works on drift in data streams aim
to be more agnostic, using sliding-window approaches
and empirically comparing Precent(X) versus Pbaseline(X)
or directly monitoring Precent(Y | X) through predictive
performance.

Preprint not peer reviewed

In practice, sequential methods are the backbone of
many operational tools in finance and machine learn-
In risk monitoring, variants of
ing for data streams.
CUSUM, EWMA, and GLR (generalized likelihood ra-
tio tests) are applied to P&L series, counts of VaR vi-
olations, or volatility-model residuals to build early-
warning dashboards that trigger limit reviews or stress
tests whenever the statistic crosses pre-defined control
bands, indicating that P(X) or P(Z = f (X)) has changed.
In terms of algorithmic standpoint, sequential pro-
cedures based on GLR and SPRT, as well as control
schemes on spread and liquidity indicators, act as “kill-
switches” that halt strategies when recent behavior be-
comes incompatible with the historical regime. GLR
compares online the likelihood of the data under no
change against the best-fitting post-change alternative,
while SPRT (Sequential Probability Ratio Test) accu-
mulates evidence between two specified hypotheses un-
til a decision threshold is reached. Control schemes
based on spread and liquidity indicators follow the same
logic.

libraries
such as MOA, River, and Scikit-Multiflow provide
DDM/EDDM/ECDD, ADWIN, KSWIN, and CUSUM
variants as plug-and-play components within incremen-
tal classifiers, which in practice has consolidated these
sequential detectors as de facto standards for monitor-
ing covariate drift in P(X), concept drift (strict sense) in
P(Y | X), and changes in time series in quasi-real time
[? ? ? ? ? ? ? ].

zt ← (xt − µ0)/σ ;
observation
S + ← max(0, S + + zt − k) ; // Update upward
CUSUM
S − ← max(0, S − − zt − k) ;
downward CUSUM
if S + > h or S − > h then
return τ = t ;
detected

Finally, sequential detectors are often combined with
segmentation methods: the online component provides

12 Complexity: O(n) time, O(1) space
13 Parameters: h controls ARL0 (false alarm rate); k is

In the supervised data-stream settings,

14 Typical use: Abrupt shifts in mean; online

9
10 end
11 return ∅ ;

// No change detected

15 References: [? ? ? ]

monitoring; low latency

the allowance for noise

// Alarm: change

// Update

end

21

7

8

6

This preprint research paper has not been peer reviewed. Electronic copy available at: https://ssrn.com/abstract=6170273

---

<!-- PAGE 22 -->

4.3. Bayesian Methods

| θrt ) (or more generally p(xt

At each step, the algorithm weighs two hypotheses:
“continue in the current regime” (increasing rt) versus
“start a new regime now” (resetting rt = 0). If the pos-
terior probability of rt = 0, p(rt = 0 | x1:t), increases
sharply, this indicates a changepoint in near real time.

Bayesian methods model changepoint detection by
specifying a probabilistic structure both for the occur-
rence of changes and for the data-generating process
within each regime. Change times and regime states
are treated as latent variables, jointly inferred with the
model parameters.

fast, near-real-time alarms, while off-line segmentation
refines the dating and statistical significance of struc-
tural breaks in subsequent analyses [? ? ]. Together,
these approaches balance responsiveness and statistical
robustness, making sequential change detection a cen-
tral building block in non-stationary time-series analy-
sis.

In finance, one often adjusts the hazard function to
reflect beliefs about the frequency of regime breaks
(for example, volatility shocks being rarer than smooth
changes in the mean) and chooses likelihoods compati-
ble with asymmetric or heteroscedastic returns, or even
with distributions over representations Z = f (X). Exact
BOCPD has cost O(T 2) in the length of the series, but
run-length truncations or sliding windows allow O(T )
approximations.

as summarized in Algorithm 3, via a message-passing
(i) the likelihood under the
scheme that combines:
|
current regime, p(xt
rt, xt−rt:t−1) for dependent models); and (ii) a prior on
regime duration, encoded by a hazard function h(rt)
specifying the probability of change as a function of rt.
In terms of data distributions, each segment corre-
sponds to a time interval in which P(X) (or P(Z =
f (X))) is assumed constant, and regime changes occur
when the model deems it more likely that the recent data
come from a new distribution.

It is assumed that the observations X1:T —or pairs
(Xt, Yt) when responses are available—are generated
from regime-dependent distributions P(X | θr) or P(Y |
X, θr), where r indexes the latent regime and θr de-
notes its associated parameters. The temporal evolu-
tion of regimes is itself probabilistic, commonly mod-
eled through hazard functions or Markovian dynamics.
Inference can be performed either sequentially (on-
line) or retrospectively (off-line). As new observations
arrive, or given the full data history, the model up-
dates posterior distributions over the parameters θr and
over latent quantities such as the run-length rt (the time
elapsed since the most recent change) and the probabil-
ity of a changepoint at time t.

Preprint not peer reviewed

(Barry–
Retrospective
Hartigan, Fearnhead–Liu). A second line of ap-
proaches works in off-line mode, seeking the most
probable segmentation (or samples from the segmen-
tation distribution) given the entire history X1:T [? ? ].
The change times τ1, . . . , τK are explicitly modeled as
latent variables, with prior distributions specifying both
the number of segments K and the typical duration of
regimes. In terms of data distribution, it is assumed that,
within each segment k, an approximately stationary
distribution generates the data, and that the task is to
infer P(τ1:K, K, θ1:K | X1:T ).

This framework naturally supports uncertainty quan-
tification, allowing one to assess both whether a change
occurred and when it occurred.
It enables the prin-
cipled incorporation of prior knowledge about regime
persistence—such as preferences for rare changes or
long-lasting regimes—through prior distributions on
P(change at t | rt) and on the regime parameters P(θr).
Schematically, we can group these methods into three
(a) online detection via BOCPD
main subfamilies:
(b) retrospective Bayesian segmen-
and extensions;
tation; and (c) regime-switching models (HMM/MS-
VAR) with Bayesian filtering and smoothing.

BOCPD and online detection via run-length. In
Bayesian Online Changepoint Detection (BOCPD) [?
], the time series is modeled as a sequence of approxi-
mately stationary segments separated by latent change-
points, with the run-length rt—the number of observa-
tions since the last changepoint—serving as the hidden
state. At each new observation xt, the algorithm recur-
sively updates the posterior distribution

Given this probabilistic formulation, inference can
be performed either by maximum a posteriori (MAP)
estimation, yielding a single “optimal” partition τk, or
by MCMC-based sampling, which produces a distribu-
tion over possible segmentations and credibility inter-
vals for each transition date. In both cases, the result
is a Bayesian characterization of the regime structure of
P(X) over time, with uncertainty explicitly quantified.

This explicit treatment of uncertainty makes these
models particularly appealing in financial applications,
where the goal is often to reconstruct historical regimes
ex post—such as bull and bear markets, high- and
low-volatility periods, or episodes of policy interven-
tion—while accounting for ambiguity in the precise

segmentation

p(rt | x1:t)

Bayesian

22

This preprint research paper has not been peer reviewed. Electronic copy available at: https://ssrn.com/abstract=6170273

---

<!-- PAGE 23 -->

t

4

3

8

6

7

5

0

no

end

end

// Likelihood

each run-length

· p(rt−1 = r − 1 |

2 for t = 1, 2, . . . do

t; changepoint probabilities

// Growth probabilities:

// Compute predictive probability for

Output: Run-length posterior p(rt | x1:t) at each time

1 p(r0 = 0) ← 1 ; // Initialize: run-length is

for r = 0 to min(t − 1, Rmax) do
π(r)
t ← p(xt | r, x1:t−1) ;
under run r

changepoint at t
for r = 1 to min(t, Rmax) do
p(rt = r | x1:t) ∝ π(r−1)
x1:t−1) · (1 − H(r − 1))

timing of regime boundaries for the relevant distribution
P(X) (e.g., returns, volatilities, or spreads).

Algorithm 3: BOCPD: Bayesian Online
Changepoint Detection
Input: Data stream x1, x2, . . .; predictive likelihood
p(xt | rt−1, x1:t−1); hazard function H(r); max
run-length Rmax (optional)

Regime-switching models (HMM, MS-VAR). Finally,
regime-switching models—most
notably Hidden
Markov Models (HMMs) and Markov-switching VARs
(MS-VARs)—model regime changes through an unob-
T
served discrete-state process S t
t=1. At each time t, the
latent state S t ∈ 1, . . . , R represents the active regime
and evolves according to a first-order Markov chain,
governing the model parameters in each period [? ? ].

Concrete instances of this class include the partition
models of Barry–Hartigan [? ], which place priors di-
rectly over partitions of the time series into approxi-
mately stationary blocks and derive the corresponding
posterior distribution. Related algorithms developed
by Fearnhead and collaborators [? ] exploit dynamic
programming or forward-type recursions to compute
the joint distribution over the number and locations of
changepoints, P(τ1:K | X1:T ). While exact inference typ-
ically incurs a computational cost of O(T 2), resampling-
based variants, such as particle filters, provide approxi-
mate solutions with near-O(T ) complexity.

Preprint not peer reviewed

regime-
switching models can be employed online, by moni-
toring changes in state probabilities or transition like-
lihoods, and off-line, to reconstruct historical regimes
and infer the most likely change dates. Their ability
to jointly model multiple variables and complex de-
pendence structures makes MS-VARs particularly well
suited for multivariate financial series, where regime
changes often involve simultaneous shifts in means,
volatilities, and correlations—i.e., structural changes in
P(X).

A classical example is Hamilton’s model [? ], which
| S t = r ∼ P(Xt
assumes that Xt
In this set-
ting, the series follows an autoregressive process whose
coefficients and/or intercepts depend on the latent state,
and each state r corresponds to a regime characterized
by specific mean, volatility, and correlation patterns.
| S t = r)
In multivariate extensions (MS-VAR), P(Xt
jointly captures regime-dependent autoregressive dy-
namics and covariance structures.

Inference in these models is typically Bayesian and
combines filtering and smoothing procedures—such as
|
the forward–backward algorithm—to estimate p(S t
x1:T ) and p(S t, S t+1 | x1:T ), together with parameter
estimation via MCMC or variational methods. This
yields posterior distributions for both the transition ma-
trix P(S t+1 | S t) and the regime-specific parameters θr
defining P(X | S t = r).

19 Likelihood: Conjugate pairs (Normal-Normal,
Poisson-Gamma) enable closed-form updates
20 Typical use: Online detection with uncertainty
quantification; gradual drifts; regime models

each run-length (model-dependent)
Update posterior parameters for p(θr | x1:t) for
each r

16 end
17 Complexity: O(n2) without truncation; O(nRmax) with

// Normalize posterior
Zt ← (cid:80)min(t,Rmax)
p(rt = r | x1:t)
r=0
p(rt | x1:t) ← p(rt | x1:t)/Zt

// Changepoint alarm (optional)
if p(rt = 0 | x1:t) > θalarm then

p(rt = 0 | x1:t) ∝ (cid:80)min(t−1,Rmax)
x1:t−1) · H(r)

18 Hazard function: H(r) = 1/λ (constant, geometric

In summary, Bayesian regime-switching methods

From a change detection perspective,

// Update sufficient statistics for

gaps); H(r) = 1/(r + 1) (increasing)

Signal: Changepoint detected at time t

// Changepoint probability:

21 References: [? ? ? ]

truncation at Rmax

· p(rt−1 = r |

reset to

| θr).

r = 0

π(r)
t

end

23

r=0

15

12

10

11

13

14

9

This preprint research paper has not been peer reviewed. Electronic copy available at: https://ssrn.com/abstract=6170273

---

<!-- PAGE 24 -->

4.4. Detection in Embeddings and OOD

4.5. Multivariate Structural Dependence Methods

? ? ? ? ]. In multivariate financial applications, embed-
dings learned by transformers or graph neural networks
are often combined with classical detectors—such as
kNN, kernel density estimation, MMD tests, or standard
CPD methods applied in latent space—to handle com-
plex temporal and cross-sectional dependencies [? ? ?
? ? ? ].

This family of approaches detects changes by moni-
toring how data points evolve in a representation, or la-
tent feature, space. Instead of operating directly on the
raw observations, the idea is to first transform the series
into a sequence of latent vectors and then track changes
in their distribution over time. In practice, this is often
framed as anomaly or out-of-distribution (OOD) detec-
tion in streaming settings.

Formally, a representation mapping Z = f (X) or
Z = f (X, Y) is learned from the observed series X and,
when available, from covariates Y. At each time t, a
latent vector zt = f (xt−k:t) or zt = f (xt−k:t, yt−k:t) sum-
marizes recent observations through a sliding window.
A regime change is then interpreted as a shift in the
induced distribution P(Z), which reflects an underlying
change in P(X) or P(X, Y) [? ? ? ? ? ].

provide a unified framework for regime detection and
modeling, with explicit uncertainty quantification and
the ability to incorporate prior information, such as as-
sumptions about regime persistence or plausible param-
eter values. At the same time, their computational cost
and sensitivity to modeling choices—such as the num-
ber of regimes, transition priors, and likelihood spec-
ification—require careful consideration, especially in
high-dimensional financial settings.

In finance, embedding- and OOD-based detectors
are especially useful for identifying genuinely unprece-
dented situations, where patterns of co-movement, liq-
uidity, or volatility deviate from all previously observed
regimes. Their effectiveness, however, depends criti-
cally on the quality of the learned representation. When
the embedding captures economically meaningful struc-
ture, changes in P(Z) reliably signal changes in P(X) or
P(X, Y). When it does not, these methods may confuse
minor fluctuations with true novelty.

Preprint not peer reviewed

One example involves algorithms for detecting
changes in the covariance matrix or in the graph of
a graphical model. Typically, we compare Pbaseline
and Precent(X) via statistics that summarize their depen-
dence: for example, tests for equality of covariance ma-
trices Σbaseline vs. Σrecent, or statistics of maximal differ-
ence in correlation coefficients ρi j over time. In this di-
rection, methods such as ICSS [? ], MOSUM [? ], and
PELT extensions for the covariance matrix (PELT–Σ) [?
] monitor breaks in univariate variance and, in multi-
variate versions, in joint variance/covariance, being use-
ful for identifying volatility and co-movement regime
changes [? ? ].

, . . . , X(d)
) denotes the multivariate
observation at time t, with each component X(i)
repre-
t
senting a distinct variable of interest, such as the return
of an asset, a risk factor, or a liquidity measure. Regime
changes are then modeled as alterations in the depen-
dence structure of the joint distribution, which may be
reflected, for instance, in changes in the covariance ma-
trix Σt = Cov(Xt), the correlation matrix Rt, a copula Ct
linking the marginal distributions, or in the topology of
a dependence graph (graphical model) associated with
P(X).

Beyond reconstruction-based signals, changes can
also be detected directly in the latent space. One ap-
proach is to define reference regions P(Z) associated
with known regimes, for instance, through contrastive
learning or clustering. A regime transition is then
detected when latent states drift away from these re-
gions or move closer to others. Related methods com-
pare distributions in representation space across time
windows, using tools such as density-ratio or density-
difference estimation, to explicitly test whether P(Z) it
has changed [? ? ? ? ? ? ].

A simple and intuitive example is provided by au-
toencoders or other unsupervised models trained on his-
torical data. These models learn a notion of “normal”
dynamics for the series. As new observations arrive,
reconstruction errors or anomaly scores are computed.
When these scores increase persistently, the current data
no longer resemble the training distribution, indicating
that the process generating X—and therefore Z—has
changed.

This general idea naturally extends to a wide range of
deep OOD techniques. These include energy-based de-
tectors, one-class and Deep-SVDD methods, generative
models that estimate latent densities, and uncertainty
monitoring in Bayesian or ensemble networks [? ? ?

Finally, we highlight methods aimed at detecting
regime changes that arise from shifts in the joint behav-
Instead of focusing on uni-
ior of multiple variables.
variate marginals P(X(i)) in isolation, these approaches
operate directly on the multivariate distribution

P(X) = P(cid:0)X(1), . . . , X(d)(cid:1),

Here Xt = (X(1)

24

t

t

This preprint research paper has not been peer reviewed. Electronic copy available at: https://ssrn.com/abstract=6170273

---

<!-- PAGE 25 -->

4.6. Change Detection Overview

Table 6 serves as the primary entry point.

joint extreme events. Similarly, historically stable hedge
relationships may deteriorate or invert sign, translating
into localized changes in Σt and Rt and into increased
residual volatility of long–short strategies.

This overview is anchored by three complementary
summaries. Together, Table 6, Figure 15, and Table 7
map the type of change of interest to suitable detection
methods, practical selection criteria, and their computa-
tional feasibility.

Some parametric methods assume Gaussian graphi-
cal models or related structures. An example is the use
of (possibly adaptive) Graphical Lasso to estimate, in
each window, a precision matrix Θt = Σ−1
associated
t
with a conditional independence graph Gt [? ]. In this
context, monitoring changes in dependence amounts to
monitoring changes in Gt or Θt.

It maps
different change axes—temporal, statistical, structural,
and ontological—to indicative method families and con-
crete financial examples. For instance, abrupt tem-
poral changes suggest segmentation or CUSUM-type
methods, while shifts in dependence structures point
toward covariance-, copula-, or graph-based detectors.
This compact view allows the practitioner to start from
the phenomenon of interest (e.g., contagion, regime
changes, beta instability) and narrow the methodolog-
ical space accordingly.

Building on this idea, several methodological lines
have been developed. On the sequential side, multivari-
ate versions of the CUSUM of squares [? ? ] monitor
sums of squares (or aggregated portfolio statistics) over
time to detect changes in joint volatility [? ? ]. An-
other line focuses on techniques for detecting changes in
copulas Ct, which describe exclusively the dependence
structure between variables, decoupled from marginals
Fi.
In this case, the idea is to compare an old” cop-
ula Cbaseline with a new” copula Crecent and test whether
there has been a change, including in tail regions [? ? ?
? ? ? ].

Preprint not peer reviewed

A complementary decision concerns the representa-
tion space in which change is monitored. As summa-
rized in Table 6 and operationalized in Figure 15, de-
tectors may act on raw series, on hand-crafted finan-
cial features, or on learned embeddings, depending on
dimensionality and interpretability requirements. This
choice determines whether changes are detected directly
in observable quantities (e.g., returns or correlations) or
indirectly through shifts in latent multivariate patterns.
Finally, Table 7 constrains these choices from a com-
putational perspective. It highlights how method fam-
ilies differ in time and memory complexity as a func-
tion of series length, dimensionality, and model struc-
ture. This comparison is essential in high-frequency or
high-dimensional settings, where theoretically appeal-
ing methods may be impractical without dimensionality
reduction or truncation strategies.

Other methods avoid strong parametric assumptions
and compare multivariate dependence measures con-
structed directly from the data, such as distance matrices
D(X) or kernel matrices K(X) [? ], using multivariate
Friedman–Rafsky-type tests [? ] or graph-based vari-
ants (MST, k-NN graph) [? ? ] to assess whether two
samples originate from the same joint distribution P(X).
On the Bayesian side, BOCPD extensions tailored to
detecting changes in structural dependence have also
been proposed [? ? ? ? ? ].
In these models, the
dependence structure (for example, a graph G or a pa-
rameter set Θ encoding the edges) is treated as latent and
evolving by regimes, and inference focuses on detecting
abrupt switches in this structure over time.

From a structural standpoint, methods based on cor-
relation matrices, copulas, or graphical models interpret
these events as rearrangements in the dependence net-
work [? ? ? ? ]. This perspective is particularly rele-
vant in financial applications, where structural changes
tend to manifest more strongly in the relationships be-
tween variables than in each series taken individually.
In distributional terms, this means that changes in P(X)
are often driven primarily by shifts in its dependence
component, while the marginals P(X(i)) may remain rel-
atively stable.

Figure 15 operationalizes this mapping as a deci-
sion tree. Starting from label availability, it guides
method selection through a sequence of practical ques-
tions about dimensionality, operational objective, usage
context (online vs. offline), and scale of concern. In this
way, the figure connects conceptual choices to imple-
mentable detector families, highlighting trade-offs be-
tween supervision, sensitivity, and interpretability.

Importantly, such changes can often be detected be-
fore any univariate model signals instability, since indi-
vidual series may remain within typical variation ranges
while the joint dependence structure becomes unprece-
dented [? ? ? ? ? ]. For instance, a contagion regime
may not be evident when inspecting individual asset re-
turns, but it becomes clear when correlations rise collec-
tively or when the tail copula concentrates more mass on

these complements transform the
broad taxonomy of change detection into a practical se-
lection framework: from identifying the relevant change
axis, to choosing an appropriate method family, repre-

Taken together,

25

This preprint research paper has not been peer reviewed. Electronic copy available at: https://ssrn.com/abstract=6170273

---

<!-- PAGE 26 -->

yt = β⊤

t xt + εt,

5. Adaptation and Continual Learning

5.1.1. Time-varying parameters (TVP / state-space)

sentation space, and control mechanism, all while re-
specting computational constraints.

in which βt follows an evolution equation βt = βt−1 + ut
(a random walk, possibly with some structure). In fi-
nance, this is applied to dynamic market betas (betas
that change over time) and other adaptive regression co-
efficients.

This section addresses the research question: How
can we adapt model learning to data distribution shifts
continuously and effectively? The focus is on strate-
gies that enable learning systems to react to evolving
data distributions in order to sustain or improve perfor-
mance in non-stationary environments, with particular
relevance to financial applications [? ? ].

Time-varying-parameter (TVP) models address non-
stationarity by allowing model coefficients themselves
to change over time.
Instead of estimating a single
fixed parameter vector, the model treats coefficients as
evolving quantities that are updated as new data arrive,
typically through a state-space formulation [? ? ? ].
This perspective naturally leads to regression models in
which parameters follow an explicit evolution equation.

The discussion is organized around the main
paradigms for continuous adaptation. We begin
with parametric adaptation methods that incorporate
change mechanisms directly into statistical models
(5.1). We then examine dynamic ensembles and regime-
specialized models that adaptively activate or reweight
learners across regimes (5.2). Next, we cover hybrid
adaptation flows that combine explicit change handling
with model updating (5.3). Finally, we discuss recent
approaches based on continual learning, test-time adap-
tation, and meta-learning, which aim to enable rapid and
data-efficient adaptation (5.4) [? ? ].

Preprint not peer reviewed

Estimation is typically carried out using the Kalman
filter or its extensions (for linear-Gaussian cases) or
through online optimization methods for more general
cases [? ? ? ]. The Kalman filter directly provides
recursive coefficient updates as new data arrive, using
a transition model that penalizes overly abrupt changes
(through the variance matrix Q of the term ut). This
yields an optimized adaptive forgetting: if the data indi-
cate that β is changing, the filter adjusts; if not, it keeps
it stable. In many cases, this “smooth” layer of adapt-
ability responds adequately to incremental or gradual
drifts, reserving more radical interventions (such as re-
sets or model switches) for moments of clear structural
break.

To synthesize these perspectives, Table 8 provides a
structured comparison of adaptation methods across key
operational dimensions, serving as a practical guide for
method selection under different application constraints.
This synthesis highlights the central trade-off between
stability and plasticity that characterizes adaptive learn-
ing in finance: overly aggressive adaptation may am-
plify noise and transaction costs, whereas conservative
updates risk sustained performance degradation after
regime changes [? ? ]. Together, these elements con-
nect adaptation strategies to their practical implications
in real-world non-stationary systems.

For example, suppose a stock’s sensitivity to a market
factor slowly increases over several months — a TVP
model with Kalman filtering will gradually raise the
estimated beta, tracking the change without ever hav-
ing to explicitly declare a one-shot “regime change”.
This avoids losing accumulated information and ensures
smoothness. However, if an abrupt shock drastically
changes β, the TVP model will take a few steps to fully
adjust (unless one temporarily increases the transition
variance Q at that instant, which is equivalent to detect-
ing and nearly resetting — hence the interaction with
detectors).

Within this family, we distinguish three main para-
metric strategies according to how change is repre-
sented in the model. The first relies on continuously
evolving parameters, typically formulated in state-space
form (5.1.1). The second introduces regime dependence
through observable drivers via threshold or smooth-
transition mechanisms (5.1.2). The third assumes a fi-
nite set of discrete latent regimes, with probabilistic
switching dynamics captured by regime-switching and
Hidden Markov models (5.1.3).

In summary, TVP and state-space models provide a
form of “built-in continuous adaptation,” especially use-
ful when we expect parameters to move slowly. In finan-
cial time series, there is broad application: stochastic-
volatility models with time-varying parameters, macro
VAR models with varying coefficients, dynamic CAPM
models, and so on [? ? ]. They tend to preserve eco-
nomic interpretability (e.g., one can track how a given
coefficient evolves and relate it to market conditions).

5.1. Parametric adaptation approaches

26

This preprint research paper has not been peer reviewed. Electronic copy available at: https://ssrn.com/abstract=6170273

---

<!-- PAGE 27 -->

No

Yes

Start

Usage context?

Goal: Fast alarm

Scale of concern?

Goal: Regime dating

Are labels Y available?

No(focus on ∆P(X))

Low dimension
(p < 10)

Online
(quasi real-time)

High dimension
(p ≥ 10)

Yes(focus on ∆P(Y), ∆P(Y|X))

⇒ Segmentation
(Sec. 4.1 )

Ex post
(backtesting, historical study)

⇒ Segmentation / CUSUM
(Secs. 4.1- 4.2)

Color coding: Start | Decision | Branch | Method | Context

⇒ Sequential (Sec. 4.2)
+ occasional refinement
via segmentation (Sec. 4.1)

⇒ DDM / EDDM / ECDD,
Loss-based CUSUM
(Sec. 4.2)

⇒ Segmentation (Sec. 4.1)
+ BOCPD / HMM
Regime models
(Sec. 4.3)

⇒ Embeddings
+ MMD / Energy or other
+ OOD/novelty in latent space
(Sec. 4.4 )

Global / Systemic
⇒ Aggregate series / systemic factors
(broad market, systemic risk;
see also structural dependence
methods, Sec. 4.5)

Figure 15: Decision tree for choosing change-detection method families. The flowchart guides method selection based on label availability,
dimensionality, operational goal, usage context, and scale of concern. Colors distinguish decision nodes (yellow), branching points (orange),
recommended methods (green), and contextual considerations (purple).

Preprint not peer reviewed

STAR (Smooth Transition Autoregressive) models, in
turn, implement the transition in a continuous way: pa-
rameters are weighted combinations of two (or more)
base regimes via a smooth function (typically logistic)
of the driver zt [? ? ? ? ]. Thus, if zt is in extreme
values, the model approximates a pure regime; in mid-
range values, it is a mixture of the two. This is useful
for capturing gradual changes or situations in which the
regime does not switch abruptly but as some indicator
deteriorates or improves. For example, a STAR model
for inflation: as expected inflation gradually moves
from X% to Y%, the monetary-policy regime (central
bank reaction parameters) transitions smoothly.

These models allow us to incorporate, ex ante, knowl-
edge about which variable signals a behavioral change.
In finance, there are clear cases: for instance, a volatility
model whose regime depends on an implied-volatility
indicator (VIX [? ]) — when VIX is high, differ-
ent parameters apply. Or a consumer-credit model that
changes when the unemployment rate exceeds a given
threshold. By specifying this, adaptation becomes auto-
mated: the model instantly adjusts its parameters when

In TAR models, one defines one or more thresholds
on a state variable (which may be the series itself at a
lag, or another variable) that determine discrete changes
in the parameters. For example, a bilinear TAR for re-
turns: if the variable zt−d (which may be a lagged return
or a macro indicator) is below a threshold γ, we use one
set of parameters (µ1, ϕ1, etc.); if it is above, we use
another set (µ2, ϕ2).

In some applications, changes in behavior are asso-
ciated with observable variables that indicate when the
system is operating under different conditions. Thresh-
old and smooth-transition models build on this idea by
allowing model parameters to change as a function of
such variables, rather than evolving autonomously over
time. This results in adaptation mechanisms in which
regime changes are triggered by explicit drivers.

This results in deterministic regime switching: not
stochastic as in an HMM, but governed by the driver
z. A financial example is a price-momentum model in
which, if a short-term return exceeds a given threshold,
the system enters a high-volatility regime or a regime

5.1.2. Smooth-transition
(TAR/STAR)

with different mean-reversion dynamics.

threshold models

Local / Sectoral
⇒ Run by cluster/sector;
Aggregate alarms
afterwards (Sec. 4.5)

and

27

This preprint research paper has not been peer reviewed. Electronic copy available at: https://ssrn.com/abstract=6170273

---

<!-- PAGE 28 -->

Axis / feature

Typical methods

Temporal – abrupt

Illustrative financial example

Sudden crash in a market index

Table 6: Change axes and indicative methods (compact view).

Temporal – gradual
Statistical – ∆P(X)
Statistical – ∆P(Y | X)

Sector rotation in stock returns
Instability of betas in a factor model

Structure – Σ / dependence
Ontological – new classes/regimes

Increase in correlations during crises (contagion)
New market regimes; unprecedented events

observation models, this transition structure defines the
joint evolution of latent states and observations.

the driver crosses the threshold (TAR), or adjusts grad-
ually (STAR), without needing to be re-estimated from
scratch.

Model parameters and latent-state probabilities are
typically inferred using the Expectation–Maximization
(EM) algorithm or Bayesian methods such as MCMC [?
? ? ]. In finance, these models are widely applied, for
example in Markov-switching GARCH and VAR for-
mulations [? ? ? ? ], where volatility or mean levels
can shift abruptly across regimes.

The limitation is obvious: one must choose the driver
and calibrate the threshold/transition function.
If the
cause of regime change is not clear, these models may
not be applicable. However, when the driver is well cho-
sen, they offer rapid adaptation (virtually without delay
if the driver is observed in real time) and usually sta-
bility within each regime, since each submodel can be
calibrated for that context.

Segmentation (PELT, Bai–Perron);
CUSUM
EWMA/GLR; BOCPD with smooth hazard Slow transition from bull to bear regime
E-Divisive, kernel CPD; ADWIN/KSWIN
Regression segmentation; supervised
CUSUM
PELT–Σ; CUSUM of squares; copula tests
BOCPD/HMM (recurrent regimes); OOD
in embeddings

Preprint not peer reviewed

5.1.3. Discrete latent states (HMM / regime-switching)
Another classical way of modeling structural change
is to assume that the data-generating process switches
between a small number of distinct regimes over time.
In this approach, regime membership is not directly ob-
served but inferred from the data, and each regime is
associated with its own set of parameters. This assump-
tion underlies regime-switching and Hidden Markov
models [? ? ? ? ]. Regime-switching models with
discrete latent states are arguably the classical paramet-
ric approach to structural breaks.

Even so, within the set of modeled regimes, HMM
adaptation is fast — as soon as the filtered probabil-
ity of a new state exceeds, say, 0.5, the model essen-
tially uses that state’s parameters, which is much faster
than recalibrating a model from scratch. Moreover, the
Markov structure imposes some inertia (e.g., if Πii is
high, states are persistent, and the model does not im-
mediately switch back), which prevents reacting to each
fluctuation.

However, a classical HMM with a fixed number of
regimes K has adaptive limitations: it can only alternate
among those K pre-estimated patterns. If a qualitatively
new regime emerges, the model does not explicitly rep-
resent it (unless K was chosen larger and that regime
occupies one of the slots). In other words, it handles
recurrences of known regimes well but not truly novel
regimes.

In the adaptation context, latent-regime models act
proactively:
they incorporate regime change in the
model structure itself. When a new regime occurs,
the model recognizes it (via filtered probabilities) and
switches to the corresponding parameter set, which may
differ radically from the previous one. Thus, we avoid
“forcing” a single parameter set across the entire his-
tory.

In this framework, a latent discrete-valued process
S t ∈ {1, . . . , K} indicates the regime active at time t.
Conditional on S t, the observed variable is generated by
a regime-specific distribution, with each regime charac-
terized by its own parameters (e.g., means, variances, or
coefficients). This allows the data-generating process to
switch abruptly between distinct parameterizations.

A Hidden Markov Model (HMM) specifies the
regime dynamics by assuming that {S t} follows a first-
order Markov chain with transition probabilities

where Π encodes regime persistence and switching be-
havior [? ? ]. Together with the regime-conditional

No single model performs well across all regimes,
particularly in non-stationary environments where

5.2. Dynamic ensembles and regime specialization

P(S t = j | S t−1 = i) = Πi j,

28

This preprint research paper has not been peer reviewed. Electronic copy available at: https://ssrn.com/abstract=6170273

---

<!-- PAGE 29 -->

Low

Yes*

Time

Notes

Space

No
No

Method

BOCPD

No
No*

O(n)
O(n)

Scalability

Real-time?

O(K)
O(n)

Yes
No
No

Yes
No
No
Yes

High
Medium

Medium
Low

Yes
Yes
Yes
Yes
Yes

WBS
Bai-Perron

Binary Seg.
PELT

O(nRmax) with truncation

Medium
Medium
Low

O(np)
O(nm)
O(nm)
O(p2)

Bayesian Methods (Section 4.3)

Sequential Methods (Section 4.2)

Embedding Methods (Section 4.4)

Segmentation Methods (Section 4.1)

Medium
Low
Medium
Medium

O(1)
O(1)
O(1)
O(w)
O(log n)

High
High
High
High
Medium

O(n)
O(Rmax)
O(S )
O(nS )
O(nS )

Online filtering
MAP sequence
T EM iterations

Wild binary segmentation
Regression breaks

O(n)
O(n)
O(n)
O(n)
O(n log n)

Greedy approximation
O(n2) worst; pruning critical

O(np + p3)
O(n2m2)
O(nm log nm)
O(np + p2)

O(n log n)
O(n) avg
O(n2) worst
O(n log2 n)
O(Kn2)

ICSS (Σ)
CUSUM of squares
Copula tests

HMM (Forward)
HMM (Viterbi)
HMM (Baum-Welch)

CUSUM
Page-Hinkley
EWMA
DDM/EDDM
ADWIN

Embed + CUSUM
MMD (kernel)
Energy Distance
OOD (density)

O(n2)
O(nRmax) trunc
O(nS 2)
O(nS 2)
O(T nS 2)

Single pass, constant memory
Variant of CUSUM
Exponential smoothing
Window size w
Dynamic window

Table 7: Computational complexity of change-detection methods. n = series length, p = dimension, S = number of states (HMM), Rmax = run-
length truncation (BOCPD), K = number of changepoints.

Preprint not peer reviewed

Scalability (rule-of-thumb): ratings indicate the typical maximum series length n that can be handled on a standard workstation with an efficient
implementation, assuming small-to-moderate dimension (p ≲ 20). High: n ≳ 106; Medium: 105 ≲ n ≲ 106; Low: n ≲ 105. In practice, large p
and expensive operations (e.g., kernel matrices) reduce these limits substantially.
* Real-time note: PELT is offline, but can be used in a quasi-online way via sliding/rolling windows. BOCPD is online, but the naive
implementation is O(n2); real-time operation typically uses run-length truncation to a maximum Rmax (e.g., 100–500), yielding O(nRmax) time and
O(Rmax) memory.
Practical considerations: for high-dimensional streams (p > 100), dimensionality reduction (e.g., PCA or learned embeddings) is usually
required before applying most detectors. Sequential methods (CUSUM/EWMA) are preferred for low-latency monitoring; segmentation methods
(PELT/Binary Segmentation) are preferred for retrospective analysis.

The core motivation behind ensembles is to provide
both robustness and continuity. By maintaining multi-
ple specialized models, the system becomes resilient to
unexpected regimes, while preserving knowledge from
past conditions that may recur. This property is particu-
larly valuable in finance, where market regimes tend to
repeat, and discarding models learned during previous
crises can result in the loss of useful information.

changes may be abrupt, recurrent, or difficult to param-
eterize [? ? ]. When multiple behaviors coexist or
regime changes are heterogeneous, even adaptive mod-
els can fail. A natural response is therefore to maintain
an ensemble of complementary models and adapt at the
model level as conditions evolve [? ? ].

Active-model selection (gating). A first strategy is to
explicitly choose, at each time step, which model should
be active. Several specialized models are maintained
(for example, one trained for a stable market and an-
other for a crisis), and a gating mechanism (which may
be a regime detector or a learned function) chooses

for range-bound markets. An ensemble can monitor
a trend indicator and dynamically adjust model usage,
either by gradually shifting weights toward the trend
model when momentum increases or by switching en-
tirely to the range-bound model during consolidation
phases.

In this context, we therefore distinguish three dy-
namic ensemble mechanisms: (i) gated model selection,
(ii) adaptive prediction weighting, and (iii) the incre-
mental introduction and retirement of experts.

As an illustration, consider a trading algorithm with
one model optimized for trending markets and another

p3 from embedding training
Windows n, m; kernel matrix
Sorting-based
After embedding trained

Covariance breaks
Multivariate variance
Tail dependence

Structural Dependence (Section 4.5)

O(np2)
O(np2)
O(n2 p2)

Medium
Medium
Low

O(p2)
O(p2)
O(np)

Quasi
Yes
No

29

This preprint research paper has not been peer reviewed. Electronic copy available at: https://ssrn.com/abstract=6170273

---

<!-- PAGE 30 -->

vs

Fast

Fast

Low

Low

Low

High

High

Slow

Slow

range

Batch

O(np)

Varies

classi-

Speed

Instant

Family

discrete

periodic

Method

Medium

Medium

Medium

Medium

Medium

Medium

O(M · t)

Very fast

Very low

Memory

O(M · c)

O(M · c)

O(KS 2)

Example

Ensemble

Ensemble

Ensemble

Parametric

Parametric

Parametric

Incremental

O(1) switch

Complexity

O(p) per step

When to Use

Gating (MoE)

HMM / MS

Online experts

Periodic retrain

TAR / STAR

against uncer-

SGD + forget

O(p2) per step

TVP / Kalman

Weighted combine

Continuous mild drift

Continual + EWC

Hyperparameter adapt Meta

Modern Approaches (Section 5.4)

Dynamic Ensembles (Section 5.2)

Incremental Learning (Section 5.3)

Parametric Approaches (Section 5.1)

Trend
models
DWM,
Learn++.NSE
Streaming
fiers

Dynamic market
betas
VIX-based volatil-
ity regimes
Bull/bear market
switching

Distinct regime special-
ists
Hedge
tainty
Evolving regimes, suffi-
cient data

Gradual parameter drift,
linear models
Known regime driver
available
Recurrent
regimes

Table 8: Comparison of adaptation methods for non-stationary financial time series. Methods are categorized by family and compared across key
operational dimensions.

Preprint not peer reviewed

Online training of new experts. A more proactive strat-
egy is to expand the ensemble over time by introducing
new models as data evolves. In continuous streams, one
can continuously train new models on recent windows
and add them to the ensemble, possibly removing or “re-
tiring” old models that have become obsolete — a form
of continuous learning in which the ensemble grows and
is pruned. For example, in the Learn++.NSE [? ? ]
method and variants, for each new batch of data, a new
classifier is trained, and the final prediction is a combi-

Notation: p = parameters, S = HMM states, K = iterations, M = ensemble size, c = expert cost, t = training cost, n = samples, p f = fine-tuned
parameters (typically p f ≪ p), k = TTA gradient steps.
Speed ratings: Very fast (<1ms), Fast (1–10ms), Medium (10–100ms), Slow (>100ms), Instant (0ms - rule-based).
Memory ratings: Very low (O(1) or O(p)), Low (O(p2) or O(S )), Medium (O(M) or O(np)), High (O(nM) or full history).
* Foundation model fine-tuning is slow initially but enables fast subsequent adaptation.

Prediction combination (ensemble weighting). A softer
alternative is to avoid hard switching and instead blend
the predictions of multiple models. Instead of choos-
ing a single model, combine the outputs of all of them
with time-varying adaptive weights. A simple method is
to weight models inversely proportional to their recent
error — thus, models that are performing poorly (per-
haps due to drift) receive lower weight, and if the regime

which model to use at each moment [? ? ? ? ? ]. This
is essentially the mixture-of-experts (MoE) idea with a
gating network, applied over time [? ? ]. For instance, a
forecasting system may have one expert for low volatil-
ity and another for high volatility; a volatility detector
(or even the HMM) determines in real time which expert
should make the prediction [? ? ? ? ].

changes and an alternative model starts performing bet-
ter, the weighting scheme automatically adjusts. This is
used in tracking and concept drift meta-learning: algo-
rithms such as Dynamic Weighted Majority (DWM) in
the concept-drift literature follow this strategy [? ? ? ].

Online linear mod-
els
Monthly model re-
fresh
Learning
scheduling

Stable with
shifts
Regime-dependent
ing

Distribution shift, unla-
beled test
Limited labeled data

Multi-task
detection
Domain adaptation

Pre-trained
formers

Preserve old knowledge

Test-time adapt

Foundation FT

O(np + p2)

Continual

Medium

Medium

Transfer

O(k · p)

O(np f )

Online

Slow*

trans-

fraud

High

Low

Fast

tun-

30

rate

This preprint research paper has not been peer reviewed. Electronic copy available at: https://ssrn.com/abstract=6170273

---

<!-- PAGE 31 -->

5.3. Hybrid continuous-adaptation flows

Continuity and memory. Adaptation does not imply
forgetting. To preserve useful past knowledge, continu-
ity mechanisms from continual learning are often em-
ployed. Replay-based strategies, such as maintaining a
memory buffer of historical samples and mixing them
into retraining, mitigate catastrophic forgetting and en-
able faster readaptation if previously observed regimes
re-emerge.

Hybrid adaptation flows are inherently multi-layered.
They combine low-cost, incremental updates operating
continuously with explicit responses triggered by de-
tected structural changes. This design seeks to rec-
oncile two competing goals: smooth tracking of mi-
nor fluctuations and decisive intervention when regime
changes are abrupt or persistent. Figure 16 summarizes
a generic hybrid adaptation architecture for learning in
non-stationary environments.

Actions upon detecting clear structural changes. When
a detector confirms a substantial change, more disrup-
tive actions are initiated, as incremental updates may
no longer suffice. Possible responses include partial or
total model resets, where prior knowledge is discarded
or strongly downweighted; on-the-fly hyperparameter
or architecture adjustments tailored to the new regime;
or specialization and branching, where a new model is
added to an ensemble rather than replacing the existing
one. These mechanisms allow flexible responses to het-
erogeneous or recurring regimes.

nation of all classifiers with weights that decay for older
ones if they misclassify recent data. This gradually “for-
gets” old hypotheses without discarding them abruptly.
Despite the advantages of ensemble-based ap-
proaches, they are not universally appropriate. Their
use may be impractical when computational resources
are severely constrained, as in ultra–low-latency trad-
ing systems, or when strong model interpretability is re-
quired for regulatory or operational reasons. Ensembles
may also be unnecessary in stable environments where
a single well-calibrated model suffices, or undesirable
when the operational burden of maintaining and mon-
itoring multiple models becomes prohibitive.
In such
cases, simpler adaptive approaches—such as incremen-
tal learning or time-varying-parameter models—can of-
fer a more suitable balance between adaptability and
complexity.

Preprint not peer reviewed

Local continuous adaptation. Between alarms,
the
is kept up to date through lightweight
model
incremental-learning schemes. Typical approaches in-
clude exponential forgetting in gradient updates or regu-
lar online retraining with newly arriving data. This layer
handles small, gradual shifts without destabilizing the
model and is supported by many standard learners, such
as linear models trained via stochastic gradient descent
and neural networks updated through progressive fine-
tuning.

Supervision and supervised reinitialization. In many
high-stakes applications, adaptation is not fully auto-
matic. Drift signals may prompt human review or of-
fline analysis, particularly in regulated domains such as
finance. In these cases, experts may recalibrate mod-
els, incorporate new explanatory variables, or validate
changes under regulatory constraints before redeploy-
ment, forming a hybrid manual–automatic loop.

Adaptation should not be automatic in all situations.
It may be suppressed when drift is transient, when data
after change are insufficient, when transaction or oper-
ational costs dominate, or when regulatory or stability
constraints require fixed models. In such cases, delayed
or conservative adaptation can be preferable to rapid but
unreliable updates.

These approaches are constrained by practical trade-
offs. Strong adaptation actions increase computational
cost and latency, whereas purely incremental updates
may respond too slowly to abrupt changes. The appro-
priate balance depends on the cost of model error rela-
tive to the cost and delay of adaptation, as summarized
in Table 9.

In summary, hybrid adaptation architectures provide
a principled way to manage non-stationarity by coordi-
nating continuous learning with selective intervention.
Their effectiveness lies not only in how they adapt, but
also in deciding when adaptation should be limited or
deferred, ensuring robustness without unnecessary in-
stability

Online monitoring and drift alarms. At the base of the
pipeline, change detectors operate continuously, track-
ing model performance, residuals, or properties of the
input data distribution. When these detectors signal a
potential structural drift, they act as triggers that acti-
vate higher-level adaptation mechanisms.

The Figure 16 highlights how continuous monitoring,
lightweight online updates, and event-driven interven-
tions interact in a single processing flow. The discussion
below follows this structure, detailing the main compo-
nents of such systems and how they jointly balance re-
sponsiveness to change with stability over time.

31

This preprint research paper has not been peer reviewed. Electronic copy available at: https://ssrn.com/abstract=6170273

---

<!-- PAGE 32 -->

Low

0 ms

High

N/A

None

latency-

Medium

1–10 ms

Latency

Strategy

Very low

1–10 min

+5–10%

10–100 ms

Perf. Gain

+10–20%

+10–15%

10 min–1 hr

Full retrain

When to Use

Baseline (0%)

No adaptation

Compute Cost

Streaming only

Ensemble reweight

Incremental update

Recent window
(100–1000)

Recent window
(50–500)

Data Require-
ments

Hyperparameter
tuning

Gradual drift; HFT;
critical

Add ensemble mem-
ber

Moderate regime change; peri-
odic maintenance

Stable regimes only; bench-
mark

Table 9: Cost-benefit trade-offs for adaptation strategies in financial applications. Performance gains are approximate and context-dependent;
values shown are typical for financial time series forecasting and classification tasks.

Preprint not peer reviewed

Latency: Time to apply adaptation and resume normal operation. Excludes initial training.
Compute cost: Relative CPU/GPU requirements. "Very low" = single-core CPU sufficient; "Very high" = multi-GPU or distributed cluster.
Data requirements: Approximate number of observations needed for reliable adaptation. Varies by problem dimensionality.
Performance gain: Typical improvement over no-adaptation baseline, measured by accuracy, RMSE reduction, or risk-adjusted returns. Highly
problem-dependent.
* Foundation model fine-tuning is expensive initially but enables rapid subsequent adaptation (<1 hr) to new sub-regimes.
HFT = High-frequency trading (microsecond-level latency requirements).

Decision guidance: In practice, hybrid policies are optimal: incremental updates as default (<10ms overhead), triggered actions (ensemble
reweight, hyperparameter tuning) for moderate drift, and scheduled full retraining (nightly/weekly) for major regime changes. The cost of error
relative to adaptation cost determines aggressiveness: risk management (high error cost) justifies expensive adaptation; informational forecasts
(low error cost) favor cheap incremental approaches.

Abrupt structural break; offline
batch

Novel regime emerges; suffi-
cient data

Complete regime change; his-
tory irrelevant

Domain shift; batch inference
mode

Uncertain regimes; multiple
hypotheses

New regime only
(1000+)

New regime data
(500–5000)

New domain;
training

Limited
(100–1000)

Unlabeled
batch

Foundation fine-tune

Full
(5000+)

Test-time adapt

leverage pre-

Low–medium

Model reset

10 min–1 hr

+15–25%

+15–25%

+20–30%

+15–30%

10–100 ms

+5–15%

1–12 hrs*

Very high

Very high

1–24 hrs

history

labels

High

32

test

This preprint research paper has not been peer reviewed. Electronic copy available at: https://ssrn.com/abstract=6170273

---

<!-- PAGE 33 -->

R

N

A

No

Yes

Type?

Light Drift
Gradual

Drift Detected?

Severe Drift
Structural

Classify Severity

Incremental Update

Online Monitoring

Prevents
catastrophic
forgetting

Drift Detector (Sec. 4)

Return to Monitoring

Moderate
Regime change

Continuous:
Always active,
low overhead

Event-driven:
Triggered by
detection

Memory
Buffer
Replay

Incremental SGD
with forgetting
(Sec. 5.4.1)

Novel:
Add ensemble
member
(Sec. 5.2)

Adjust hyperparams
+ reweight ensemble
(Sec. 5.2)

Abrupt:
Reset/retrain
with replay
(Sec. 5.4.1)

Recurrent:
Activate dormant
expert
(Sec. 5.2)

Figure 16: Hybrid continuous-adaptation pipeline. The system combines low-overhead incremental updates (continuous monitoring) with
event-driven adaptation actions triggered by drift detection. Severity classification routes to appropriate strategies: light drifts receive incremental
adjustments, moderate drifts trigger hyperparameter tuning and ensemble reweighting, severe drifts invoke more drastic measures (reset, expert
activation, or ensemble expansion). Memory buffers enable replay to mitigate catastrophic forgetting (Sec. 5.4.1). This multi-layer architecture
balances adaptation speed, stability, and performance (Sec. 5.3).

Preprint not peer reviewed

A representative example of this philosophy is Elas-
tic Weight Consolidation (EWC) [? ]. EWC augments
the training loss with a penalty that discourages devia-
tions in parameters deemed critical for previous tasks,
as measured by Fisher information. In a drift context,
once a regime change is identified, the model can be
updated using recent data while preserving parameters
that encode information from the earlier regime. This
allows the model, at least partially, to function across
multiple regimes without full retraining.

Replay-based memory further supports this process,
especially when historical data are limited or expensive
to collect. Maintaining even a small buffer of past obser-
vations can substantially reduce forgetting when adapt-
ing to new conditions. In practice, this often connects
continual learning with ensemble methods: rather than
forcing a single model to remember everything, multi-
ple specialized models can be maintained, with the en-
semble as a whole preserving broader historical knowl-
edge.

In continual learning, the objective is to enable mod-
els to incorporate new information sequentially while
avoiding catastrophic forgetting of previously acquired
knowledge [? ]. This property is particularly impor-
tant under distribution shift, where adaptation to a new
regime should not eliminate the model’s ability to oper-
ate if earlier regimes reappear or continue to coexist in
part of the data.

To achieve this, continual-learning methods rely on
mechanisms that constrain how new knowledge is ab-
sorbed. Common strategies include parameter reg-
ularization, which penalizes changes to parameters
that were important for past tasks; replay-based ap-
proaches[?
], which store or generate samples
from previous data distributions and mix them into

This subsection is organized around three learning
strategies for non-stationary environments. We first
present continuous learning methods (5.4.1), followed
by test-time adaptation techniques (5.4.2). Then, we
then discuss light adaptation of foundation models and
meta-learning approaches (5.4.3), which aim to enable
rapid specialization under distribution shift.

new training; and dynamic architectures, which allo-
cate additional capacity—such as new neurons or mod-
ules—to represent emerging regimes while preserving
existing ones. In financial settings, for instance, a fraud-
detection system that learns a new fraud pattern should
not become blind to older, still-relevant fraud behaviors.

5.4. Continuous learning,
foundation models

5.4.1. Continuous learning and memory preservation

test-time adaptation, and

33

?

This preprint research paper has not been peer reviewed. Electronic copy available at: https://ssrn.com/abstract=6170273

---

<!-- PAGE 34 -->

5.4.2. Test-time adaptation

This idea is explicit in data-stream algorithms such as
Learn++.NSE and its variants, which continually intro-
duce new models while retaining older ones and adjust-
ing their weights based on current performance. Older
hypotheses are not discarded outright, allowing them to
remain effective if earlier contexts recur.

regime may, when deployed in a new regime, ob-
serve incoming inputs and adjust selected parameters
or statistics to preserve internal consistency or invari-
ants. While this can provide fast correction without ex-
ternal retraining, it is inherently risky:
incorrect self-
supervised signals or poorly constrained updates may
introduce bias or amplify model drift.

Overall, the effectiveness of TTA approaches is lim-
ited when shifts are severe or conceptual in nature:
if the relationship between inputs and targets changes
abruptly, unlabeled test data provide little reliable guid-
ance for adjustment, unless robust self-supervised ob-
jectives correlate with the task loss or reliable pseudo-
labels can be generated.

A particularly practical use case arises in anomaly de-
tection, where test data are often assumed to be mostly
In such scenarios, thresholds, activity levels,
normal.
or internal reference statistics can be recalibrated using
only current observations. In finance, this is analogous
to daily recalibration of risk models using recent intra-
day prices to maintain alignment with current volatility
levels.

Overall, despite these advantages, continual learning
has clear limitations.
It can underperform when suc-
cessive regimes are too heterogeneous to be captured
by a shared representation, when memory buffers are
too small to adequately represent past distributions, or
when the model architecture lacks sufficient capacity to
express new regime complexity. In addition, if drift oc-
curs faster than the model can adapt—such as during
abrupt market shocks—gradual continual-learning up-
dates may lag behind reality. In such cases, ensemble
specialization or explicit regime-switching approaches
may be more effective than attempting to preserve a sin-
gle continuously adapting model.

Preprint not peer reviewed

This approach is effective under drift for two main
reasons. First, pre-training on diverse datasets produces
representations that often remain useful when market
conditions change, even if the target distribution shifts.
Second, adaptation can be limited to a small subset of
parameters—such as a task head or parameter-efficient
modules like LoRA or adapters—allowing fast updates
with bounded computational cost and reduced risk of
overfitting or instability [? ? ? ? ? ]. As a result, mod-
els can respond to regime changes without continuously
modifying the full parameter space.

At a basic level, TTA often operates by updating in-
ternal statistics rather than model parameters. A com-
mon example is adaptive normalization: neural net-
works with normalization layers (e.g., BatchNorm [? ]
or LayerNorm [? ]) rely on estimates of input mean and
variance, which may become misaligned under distri-
bution shift. Recomputing or gradually updating these
statistics at test time, without modifying the network
weights, can already improve robustness to covariate
shift.

More advanced TTA methods extend this idea by al-
lowing constrained parameter updates guided by self-
supervised objectives defined on test data [? ]. Typ-
ical choices include entropy minimization or self-
consistency criteria, which can be evaluated without la-
bels. The model performs a small number of gradient
steps to minimize such objectives before producing pre-
dictions. These techniques have shown promise in cor-
recting moderate domain shifts in vision and language
models.

Foundation models and meta-learning address non-
stationarity by reducing the need for frequent full re-
training.
Instead of rebuilding models whenever the
data distribution changes, they rely on pre-trained rep-
resentations that can be quickly re-specialized with lim-
ited data and computation. This shift is significant in
domains such as finance, where full retraining is expen-
sive, slow to deploy, and difficult to govern in produc-
tion.

loop follows
three steps. Incoming data are first encoded into em-
beddings using a frozen pre-trained backbone. These
embeddings are then monitored over time to detect dis-
tributional shifts by comparing recent representations
against a reference window that characterizes the base-
line regime. When a drift detector signals a significant

Test-time adaptation (TTA) encompasses methods
that allow a model to adjust parts of its behavior dur-
ing inference itself, using only unlabeled data from the
current environment [? ]. Rather than accumulating
new labeled data and retraining offline, the model per-
forms limited self-adjustment on the fly, aiming to re-
main aligned with the prevailing data distribution.

In time-series and financial settings, TTA can be in-
terpreted as rapid internal recalibration. For instance,
a return-forecasting model trained under one market

5.4.3. Light adaptation of foundation models and meta-

Operationally, a simple deployment

learning

34

This preprint research paper has not been peer reviewed. Electronic copy available at: https://ssrn.com/abstract=6170273

---

<!-- PAGE 35 -->

6.1. Temporal validation protocols

and false alarms (6.2). Finally, we discuss adaptive-
performance and cost-aware metrics that capture recov-
ery, stability, and adaptation costs (6.3).

change, a lightweight adaptation step is triggered us-
ing a small buffer of recent data. Only the selected pa-
rameters—typically the task head or parameter-efficient
components—are updated, while the backbone remains
fixed. Adaptation is usually constrained by explicit bud-
gets on data, optimization steps, and validation crite-
ria, ensuring that updates improve short-horizon perfor-
mance and can be safely rolled back if necessary.

In time-series problems, proper evaluation requires
validation protocols that respect temporal order, ensur-
ing that no future information is used during training or
calibration [? ? ]. While this principle is conceptually
simple, it demands careful implementation in practice:
training, validation, and test splits must be defined by
contiguous time blocks rather than random partitions,
as commonly done under i.i.d. assumptions [? ? ].
Moreover, when evaluating adaptive models, validation
should replicate production conditions; for instance, if
a model is updated monthly in deployment, the backtest
should explicitly simulate this update cycle [? ? ? ].

This paradigm is already reflected in recent time-
series foundation models such as TimesFM, Chronos,
and Moirai, which report strong zero-shot and trans-
fer performance across heterogeneous benchmarks. In
financial and macroeconomic forecasting, pre-trained
forecasters like TimeGPT-1, as well as compact trans-
ferable models such as Lag-LLaMA and Tiny Time
Mixers, provide practical starting points under common
production constraints on latency and compute. In these
settings, light adaptation through heads or adapters is
often sufficient to maintain performance across chang-
ing market conditions, avoiding repeated full retraining
cycles.

Preprint not peer reviewed

Similarly, adaptation methods should be evaluated
using protocols that emphasize performance across time
and regimes rather than relying on static train–test
splits [? ? ]. Common practices include organizing
evaluation by temporal windows or regimes and analyz-
ing system behavior before, during, and after distribu-
tion shifts, ensuring that adaptation is assessed under
conditions that reflect its intended operational use [? ].
In summary, robust evaluation under non-stationarity
relies on temporally consistent validation protocols, re-
alistic simulation of deployment conditions, and end-to-
end assessment of detection and adaptation mechanisms
within evolving data streams [? ? ? ].

Beyond general forecasting evaluation, specialized
protocols are required for systems that include change
detection and adaptation components.
For change
detection, when real or approximate annotations of
changepoint times are available, evaluation is com-
monly performed by running detectors on series with
known changes and observing their behavior relative
to these events [?
In real-world scenarios
].
where ground truth is unavailable, detectors are often
assessed indirectly through their interaction with down-
stream adaptation mechanisms, for example by embed-
ding them in a full adaptive pipeline and evaluating the
resulting system behavior [? ? ? ].

In summary, foundation models and meta-learning
support a controlled and scalable response to non-
stationarity. By combining reusable pre-trained repre-
sentations, continuous monitoring of embedding behav-
ior, and parameter-efficient adaptation, forecasting sys-
tems can handle drift more quickly and with lower op-
erational risk. While these methods do not eliminate
the need for full retraining in cases of large or persis-
tent shifts, they offer a practical middle ground between
static models and costly retraining pipelines, making
them well-suited for deployment in evolving financial
environments.

A widely used temporal validation protocol is the pre-
quential (sequential predictive test) scheme [? ? ? ]. In
this setting, the model is trained up to a given time and
then used to generate predictions sequentially as new
observations arrive, with the training set being updated
accordingly. This protocol closely mirrors online oper-
ation and allows evaluation under realistic data arrival
and adaptation conditions [? ? ].

This section addresses the research question: How
can we evaluate the performance of models and de-
tection/adaptation systems under non-stationarity, us-
ing appropriate metrics and protocols? Proper evalu-
ation is essential, as inappropriate protocols or metrics
can lead to misleading conclusions about the effective-
ness of methods in evolving environments.

The discussion is organized around three evalua-
tion components that together define a concise frame-
work for fair and meaningful evaluation under non-
stationarity. We first present temporal validation proto-
cols that respect data chronology and avoid information
leakage (6.1). We then review metrics specific to change
and drift detectors, including detection accuracy, delay,

6. Evaluation: Protocols and Metrics

35

?

This preprint research paper has not been peer reviewed. Electronic copy available at: https://ssrn.com/abstract=6170273

---

<!-- PAGE 36 -->

for

In contrast,

6.2. Metrics specific to detectors

• MDR (Missed Detection Rate): defined as the
proportion of true changes that are not detected,
this criterion complements recall by explicitly
quantifying failures to signal changepoints [? ? ].

• ARL0 (Average Run Length to false alarm): this
measure focuses on detector behavior under stable
conditions. It corresponds to the expected time un-
til a false alarm occurs and is inversely related to
the sequential false-positive rate. In practice, de-
tectors are often calibrated by specifying a target
ARL0 [? ? ].

The evaluation of change detectors depends funda-
mentally on the availability and nature of change-point
annotations, which in turn are closely tied to the type of
data used. In practice, detectors are evaluated on a spec-
trum ranging from synthetic and semi-synthetic series
to fully real-world data, each offering different levels of
control and realism [? ? ].

• Mean Time To Detection (MTTD): beyond
whether a change is detected, this criterion cap-
tures how quickly the detector reacts. It measures
the average delay between the true changepoint
and the alarm time [? ? ]. What constitutes an
acceptable delay is application-dependent—for in-
stance, seconds may matter in high-frequency trad-
ing, whereas delays of months may be acceptable
in macroeconomic analysis.

A common intermediate setting relies on semi-
synthetic datasets, where artificial changes are injected
into real time series. This approach provides approxi-
mate ground truth while preserving realistic noise char-
acteristics and temporal dependencies, allowing con-
trolled evaluation under conditions that resemble real
data [? ? ]. Fully synthetic series, on the other hand,
offer complete control over change locations and mech-
anisms, but may oversimplify real-world dynamics [?
].

Preprint not peer reviewed

real-world series without exact
changepoint labels, evaluation becomes more challeng-
ing. One pragmatic strategy is indirect assessment
within an adaptive modeling pipeline: different detec-
tors are combined with the same adaptation policy, and
their effectiveness is inferred from downstream behav-
ior [? ? ? ]. If detector A consistently leads to better-
adapted model performance than detector B under iden-
tical conditions, it is reasonable to conclude that A is
more effective at identifying relevant changes. Finally,
in fully unlabeled real data, qualitative inspection or ex-
pert judgment is sometimes used, comparing detected
changepoints against known historical events—such as
the 2008–09 financial crisis or the March 2020 COVID-
related market crash—to assess plausibility [? ? ].
While subjective, this approach can provide contextual
validation.

• Precision, recall, and F1 for change detection:
these metrics quantify how many true changes are
detected (recall) and, among all detected changes,
how many correspond to actual changepoints (pre-
cision) [? ? ]. They are particularly useful in
scenarios with imbalanced outcomes, where either
false alarms or missed detections dominate. In the
drift literature, these quantities are sometimes re-
ferred to as “drift detection rate” and “false alarm
rate” [? ? ].

• Testing across multiple scenarios and datasets:
adaptation should be evaluated on diverse series or
assets, covering different temporal structures and
drift types, rather than on a single benchmark [?
? ? ]. Reliance on a small number of canonical
benchmarks (e.g., the Electricity dataset[? ? ] or
a few market indices7), especially when combined
with simplified protocols, may limit the extent to
which conclusions generalize [? ? ].

Before analyzing adaptation costs and benefits
through specific metrics, it is necessary to define how
adaptive models are evaluated in practice. Metrics are
only meaningful when computed under evaluation se-
tups that reflect how models are trained, updated, and
deployed in a real-world environment over time [? ? ?
].

So, when change-point annotations are available, de-
tectors can be evaluated in a supervised manner, sim-
ilarly to classifiers, by contrasting correct detections
with false alarms [? ? ]. In this setting, several com-
plementary criteria are commonly used to characterize
detector behavior [? ? ].

Accordingly, the evaluation design must be made
explicit. The recommendations below specify how
scenarios and protocols may be defined to determine
where and under which conditions adaptive models are
tested [? ? ].

7Examples of widely used market-index data sources include the
S&P 500 level series distributed via FRED [? ]; volatility bench-
marks such as the VIX from Cboe (also mirrored in FRED) [? ? ];
research-grade equity and index returns via CRSP through WRDS [?
]; and provider methodology/governance documents for major global
benchmarks (e.g., MSCI and FTSE Russell) [? ? ].

6.3. Adaptive-performance and cost metrics

36

This preprint research paper has not been peer reviewed. Electronic copy available at: https://ssrn.com/abstract=6170273

---

<!-- PAGE 37 -->

7. Benchmark and Reproducibility

• External validity and replicability: consistent
evaluation pipelines and shared datasets enable
verification that reported results persist across
studies [? ].

• Robust evaluation protocols: all methods should
be compared under identical backtesting and up-
date procedures, with statistical testing applied
where appropriate [? ].

• Sensitivity analysis: critical parameters control-
ling adaptation (e.g., forgetting factors, detection
thresholds, update frequencies) should be varied
to verify that results are not driven by narrow tun-
ing [? ].

This section addresses the research question: How
can detection and adaptation methods be benchmarked
under non-stationarity in financial time series? Proper
benchmarking is essential, as inappropriate protocols,
scenario choices, or reporting conventions can lead to
misleading conclusions about what works in evolving
environments [? ].

Once these evaluation setups are fixed, the criteria fo-
cus on what should be measured to quantify the practi-
cal consequences of adaptation. In addition to standard
predictive metrics computed sequentially over time—
for example, forecasting error tracked across windows
or regimes—adaptive models must be assessed with re-
spect to the computational, behavioral, and economic
effects introduced by model updates, as summarized be-
low [? ? ? ].

The discussion is organized around four components.
We first define benchmark criteria and a scenario spec-
ification that makes assumptions explicit and compara-
ble across studies (Section 7.1). We then review datasets
and tasks for regime and anomaly detection from both
the financial and data-stream literature (Section 7.2).
Next, we propose a minimal scenario-coverage baseline
that enables comparable benchmark suites without re-
quiring a single canonical dataset (Section 7.3). Finally,
we provide a compact recipe for constructing bench-
marks and reporting reproducible evaluations under re-
alistic deployment constraints (Section 7.4).

Preprint not peer reviewed

Benchmarks for non-stationarity should support con-
trolled, reproducible comparison across methods and
research traditions. In finance, this is challenging be-
cause studies often rely on proprietary datasets, ad hoc
asset selections, and heterogeneous experimental proto-
cols, which limits reproducibility and undermines cross-
paper comparability.

Here, Πs fixes the online setting (e.g., prequential
latency
vs. rolling updates,
and compute budgets, and model-access assumptions),
while Es defines what is reported (detection quality,
predictive performance and calibration, computational
cost, and finance-specific utility).

• Computational overhead and latency: the fre-
quency and duration of model updates determine
whether adaptation is feasible under time con-
straints. Streaming frameworks (e.g., MOA, River)
typically report throughput to characterize this as-
pect [? ? ].

in financial applica-
tions, adaptation should be evaluated through risk-
adjusted utility measures. When multiple strate-
gies are compared, statistical controls such as
White’s Reality Check [? ] are required to miti-
gate data-snooping effects [? ? ].

• Stability and volatility of predictions: aggressive
adaptation can induce erratic behavior. Evaluation
should verify that model updates do not introduce
excessive oscillations in predictions or decisions
over time [? ? ].

• Memory footprint: adaptive architectures differ
in resource usage; large ensembles require substan-
tially more memory than single-model approaches,
which may be prohibitive in constrained environ-
ments.

(1)
using the four axes introduced in Section 2, together
with a data instantiation Ds, an online protocol Πs, and
an evaluation mapping Es (Fig. 17):

Under this specification, desirable benchmark prop-
erties become requirements on (i) coverage of drift sig-
natures {ϕ(s)} and (ii) comparability of protocols and
outcomes:

To make benchmark design explicit and comparable,
we specify each benchmark scenario s by a taxonomy-
conditioned descriptor:

ϕ(s) = (Temporal, Statistical, Spatial, Ontological),

7.1. Criteria and scenario specification

• Direct economic impact:

B = {(Ds, ϕ(s), Πs, Es)}S

label delay/availability,

s=1.

(2)

37

This preprint research paper has not been peer reviewed. Electronic copy available at: https://ssrn.com/abstract=6170273

---

<!-- PAGE 38 -->

Spatial: global / local

7.2.1. Financial

Online
protocol
Πs

Drift sig-
nature
ϕ(s)

Evaluation
mapping
Es

Data in-
stantiation
Ds

Ontological: regime /
mechanism

marks under changing regimes

time series and forecasting bench-

Scenario Specification
Bs = (Ds, ϕ(s), Πs, Es)

Temporal: abrupt /
gradual / recurrent
Statistical: ∆P(X) /
∆P(Y | X) / dep. shift

Detection: delay, false-alarm control; Predic-
tion: loss, calibration
Compute: wall-clock/memory; Utility: costs,
drawdown, risk-adj. return

Assets/markets; sampling frequency; horizon;
calendar rules and preprocessing
(optional) aligned context channels:
macro/microstructure/text

Update protocol: prequential / rolling; label
delay and availability
Latency/compute budgets; model access: white-
box / black-box

Figure 17: Scenario specification schema for benchmark design under
non-stationarity. A scenario is defined by data Ds, drift signature ϕ(s)
(four-axis taxonomy), online protocol Πs, and evaluation mapping Es.

casting and regime change. We then cover anomaly and
out-of-distribution benchmarks often used as proxies for
rare or extreme regimes. We close with practical consid-
erations on tooling and reproducible pipelines.

In finance, there are still no consolidated benchmark
repositories comparable to those used in the data-stream
literature. Instead, evaluation typically relies on isolated
time series and task-specific experimental setups cho-
sen by individual studies. As a consequence, there is no
single “standard dataset” for problems such as regime
change or adaptive forecasting: different works select
different assets, markets, and time periods. For exam-
ple, one study may focus on Bitcoin prices [? ], another
on individual stocks [? ? ? ? ], and another on sector in-
dices, making direct comparison difficult, since results
can vary substantially across assets and historical win-
dows.

Preprint not peer reviewed

Several efforts attempt to partially mitigate this lim-
itation by defining approximate regimes using known
economic or market events. Common strategies include
splitting series into pre- and post-crisis windows (e.g.,
the 2008 global financial crisis or the 2020 COVID
shock) and treating them as distinct regimes to assess
robustness under distribution shifts. While useful, these
constructions remain ad hoc and lack standardization
across studies.

• High-frequency financial data (tick or transaction-
level series) used to detect micro-regimes, such as
intraday changes in liquidity and volatility; recent
examples include microstructure data from B3 [?
? ? ].

• Detection of regime changes in macroeconomic
series (GDP, inflation) or market indicators such
as implied volatility and trading volume, includ-
ing interest-rate series affected by monetary policy
shifts.

• Coverage. Suites should span diverse morpholo-
gies and mechanisms across the four axes (e.g.,
abrupt vs. gradual, global vs. local, regime vs.
mechanism).

• Return or volatility forecasting for equity indices
(S&P 500, Dow Jones, and international indices)
over long horizons, where economic cycles and
crises provide implicit regime variation.

• Identifiability. Scenarios should include anno-
tated or controlled changes (event-based, statisti-
cal, or semi-synthetic) to enable objective assess-
ment.

• Realism–control balance. Combine real-market
episodes with controlled synthetic/semi-synthetic
settings to separate methodological effects from id-
iosyncratic artifacts.

pro-
vide aligned macro/microstructure/textual context
to evaluate context-aware and multimodal ap-
proaches [? ? ? ].

• Specialized tasks such as financial contagion de-
tection, based on time series of correlations or tail-
risk measures across markets [? ? ? ? ? ].

• Sufficient duration. Scenarios should be long
enough to evaluate long-run stability, repeated up-
dates, and cumulative adaptation effects.

We organize this discussion into two categories. We
first discuss financial time series benchmarks for fore-

7.2. Datasets and tasks for regime and anomaly detec-

In this fragmented scenario, other types of datasets

and tasks are more commonly used, such as:

• Context metadata.

When relevant,

tion

38

This preprint research paper has not been peer reviewed. Electronic copy available at: https://ssrn.com/abstract=6170273

---

<!-- PAGE 39 -->

for

and

out-of-

anomalies

mark suites

7.3. Scenario coverage:

towards comparable bench-

7.2.2. Benchmarks
distribution

economic feedback, including trading frictions and sta-
tistical controls against backtest overfitting [? ? ? ].

These tools facilitate implementation, but fair com-
parisons require explicit scenario and protocol specifi-
cations, which we formalize in Sections 7.3 and 7.4 [?
].

The distinction between concept drift, regimes, and
anomalies is often blurred: rare regimes may appear
anomalous when viewed from dominant market con-
ditions, while persistent anomalies can effectively de-
fine short-lived regimes. As a result, benchmarks
originally designed for anomaly or out-of-distribution
(OOD) detection are frequently reused to evaluate drift
and regime-detection methods, and the methodological
boundaries between these tasks are not always clear.

Section 7.2 highlights that, in finance, evaluation is
often driven by idiosyncratic choices of assets, time pe-
riods, and protocols, which makes results difficult to
compare across studies. To address this limitation with-
out requiring a single “standard dataset”, we propose
to standardize coverage: a benchmark suite should in-
clude a small set of scenarios whose drift signatures
span the main regions of the four-axis taxonomy (tem-
poral, statistical, spatial, ontological), while keeping the
suite compact enough for reproducible evaluation.

Several general-purpose benchmarks illustrate this
overlap. The Numenta Anomaly Benchmark (NAB) [?
], for example, includes multiple time series—some
with financial relevance, such as stock-related Twitter
activity—with annotated anomalies. Although its pri-
mary focus is on point anomalies, extended anoma-
lous segments can be interpreted as short regimes, and
some studies evaluate drift detectors on NAB by treat-
ing each annotated anomaly as a change point to detect.
Similarly, recently compiled shift benchmarks such as
the Shifts Dataset [? ] provide real distribution shifts
across multiple modalities, even though their emphasis
lies mainly outside finance.

Preprint not peer reviewed

In financial applications, however, there is no stan-
dardized anomaly or OOD benchmark. Most studies
rely on ad hoc, event-based constructions, such as com-
paring returns during “normal” periods with those ob-
served around major shocks (e.g., September 11 or the
Lehman Brothers collapse). While intuitive, these prac-
tices lack consistency and comparability across works.
As noted by Žliobait˙e [?
in her critique of the
long-standing use of the Electricity data set for con-
cept drift, the widespread adoption of a convenient but
limited benchmark can obscure important methodolog-
ical weaknesses. By analogy, commonly used finan-
cial anomaly series—especially those with artificially
injected outliers—should be critically examined before
being used to evaluate regime-change or drift-detection
methods.

To complement the dataset-and-task survey above,
we note that reproducible benchmarking pipelines are
often built on:
(i) data-stream frameworks (MOA,
Scikit-Multiflow, River) for incremental learning, drift
detectors, and prequential evaluation [? ? ? ]; (ii) fore-
casting toolkits and archives (Monash, GluonTS, Darts)
for standardized baselines and dataset access [? ? ?
]; and (iii) finance-oriented backtesting/simulation envi-
ronments (Gym-like setups) to evaluate adaptation with

Minimal reference suite. We recommend the follow-
ing minimal suite as a coverage baseline. Each sce-
nario is defined by a characteristic drift signature ϕ(s)
(Section 2) and can be instantiated using multiple
datasets/tasks from Section 7.2:

• S2: Local mechanism shift. Gradual change pri-
marily affecting ∆P(Y | X) (often coupled with
∆P(X)), local to a subset of assets/segments, in-
terpreted as a mechanism change (e.g., sector rota-
tion; microstructure/regulatory change).

• S3: Secular macro drift. Incremental drift dom-
inated by ∆P(X) and slow parameter drift with
interpreted as regime drift (e.g.,
global scope,
long-horizon evolution in rates/inflation/volatility
regimes).

• S5: True concept drift (signal efficacy). Abrupt
or gradual shifts in ∆P(Y | X) that change the use-
fulness or sign of predictive relationships; local
or global; interpreted as mechanism or regime de-
pending on domain assumptions.

• S1: Crisis dependence regime. Abrupt changes
in multivariate dependence/tails with global im-
pact, interpreted as a regime shift (e.g., contagion;
correlation/tail-risk breakdown across markets).

• S4: Recurrent seasonal regimes. Recurrent pat-
terns (calendar/intraday seasonality) primarily ex-
pressed through ∆P(X) and higher-order structure;
global or local; typically a regime phenomenon.

7.2.3. Practical considerations:
ducible pipelines

tooling and repro-

39

]

This preprint research paper has not been peer reviewed. Electronic copy available at: https://ssrn.com/abstract=6170273

---

<!-- PAGE 40 -->

6. Reproducibility checklist (minimal).

5. Establish baselines and tuning budgets. Include
non-adaptive baselines and simple adaptive base-
lines (e.g., rolling retrain) to contextualize gains.
Specify hyperparameter tuning budgets and cali-
bration targets (e.g., fixed false-alarm rate/ARL0
for detectors) to prevent unfair comparisons.

Provide
enough detail to reproduce end-to-end results: data
provenance and time span; asset identifiers; ex-
act feature computation windows (and leakage
checks); protocol definition (warm-up length, up-
date cadence); detector calibration and thresholds;
random seeds; compute environment; and code to
run the full pipeline from data to metrics.

model access such as white-box vs. black-box).
Avoid tuning Πs post hoc to favor a method.
4. Define the evaluation mapping Es. Report at
minimum: (i) detection quality (delay and false-
alarm control), (ii) predictive performance and
calibration under drift, (iii) computational cost
(wall-clock/memory,
including retraining), and
(iv) finance-specific utility (e.g., transaction costs,
turnover, drawdown, risk-adjusted return). Use
consistent protocols and metrics across methods
(Section 6).

How this complements existing datasets. This suite
is intentionally data-agnostic:
it does not prescribe
a single dataset, but specifies what a benchmark
suite should cover. For example,
index forecasting
and macro/indicator monitoring naturally instantiate
S3/S4; contagion and correlation-network tasks instan-
tiate S1; microstructure datasets support S2/S4; and
strategy/feature instability across regimes targets S5.
Anomaly/OOD benchmarks can be used as proxies for
specific cases (most often S4–S5), but should not be
treated as full substitutes for S1–S3 unless they preserve
multivariate dependence structure and realistic temporal
context.

Minimum reporting for coverage studies. For any suite
instantiation B = {(Ds, ϕ(s), Πs, Es)}S
s=1, authors should
report the scenario specification from Section 7.1 ex-
plicitly. At minimum, this includes (i) the intended
drift signature(s) ϕ(s) (temporal, statistical, spatial, on-
tological), (ii) the online protocol Πs (update mode and
cadence, label availability/delay, latency/compute bud-
gets, model-access assumptions), and (iii) the evalua-
tion mapping Es (detection delay and false-alarm con-
trol, predictive loss and calibration, computational cost,
and finance-specific utility). To support attribution of
improvements, results should include controlled com-
parisons or ablations that separate representation, detec-
tion, and adaptation choices (cf. Section 6).

Preprint not peer reviewed

This Section complements the research question:
What are the limitations and future research directions?
The discussion is organized around four classes of
threats to validity in learning under non-stationarity. We
first examine data- and label-related issues that affect
construct validity (8.1). We then analyze evaluation-
protocol choices that introduce internal and statistical-
conclusion validity threats (8.2). Next, we discuss mod-
eling and adaptation assumptions that can bias conclu-
sions about robustness under drift (8.3). Finally, we
address finance-specific limitations—such as the “fac-
tor zoo,” replicability, and limited generalization—that
challenge external validity (8.4).

A first family of threats concerns the quality of eval-
uation data and the definition of “change labels”.
In
real-world financial time series, there is rarely a pre-
cise ground truth for when drifts occur. As a result,
researchers often rely on proxies, such as associating
changes with known events (e.g., market crashes) or in-
jecting synthetic drifts into real data. While pragmatic,
these strategies may fail to capture the true nature of

2. Instantiate data Ds at the appropriate scale.
Choose markets/assets, sampling frequency, pre-
diction horizon, and any context channels (macro,
microstructure, text). Make preprocessing rules
explicit (calendar, missing data, corporate actions,
normalization).

1. Choose the target drift signature. Select a sce-
nario from the coverage suite (Section 7.3) or
define a new one by specifying ϕ(s) along the
This determines what
four axes (Section 2).
constitutes a “change” and what should be de-
tectable/adaptable.

To enable consistent benchmark construction across
datasets and research communities, we propose the fol-
lowing compact recipe. The goal is not to enforce a
single dataset, but to enforce comparable experimental
design.

3. Specify the online protocol Πs. Fix the eval-
uation mode (prequential vs. rolling), update ca-
dence (time-based or event-based), label availabil-
ity/delay, and constraints (latency/compute budget;

8.1. Data- and label-related threats (construct validity)

7.4. Recipe: constructing finance benchmarks under

8. Discussion and Future Directions

non-stationarity

40

This preprint research paper has not been peer reviewed. Electronic copy available at: https://ssrn.com/abstract=6170273

---

<!-- PAGE 41 -->

non-stationarity, which can directly affect construct va-
lidity: the experimental setup may not accurately mea-
sure the phenomenon it is intended to assess.

method is carefully tuned or evaluated without temporal
leakage, while others are not. In such cases, observed
performance gaps reflect experimental bias rather than
methodological superiority.

Closely related to this issue is the frequent ab-
sence—or low reliability—of validation labels. This is
particularly problematic in unsupervised detection set-
tings, where evaluation is often indirect or qualitative.
Without objective criteria, performance claims may rely
on visual inspection or on the proximity of detected
changes to well-known events, leaving room for sub-
jective interpretation and making systematic compari-
son across methods difficult.

Overall, internal and statistical-validity failures imply
that reported gains may disappear under stricter controls
or alternative samples, inflating the perceived effective-
ness of current methods. In financial applications, these
problems can become more serious. Multiple models
or variants are often tested on the same historical sam-
ple, and only the best result is reported. Apparent im-
provements are likely driven by chance and overfitting,
without correction for multiple testing, for example via
White’s Reality Check [? ],

Statistical-conclusion validity is compromised when
performance differences are reported without sig-
nificance analysis. Many studies claim improve-
ments based on small error reductions or detection
gains, without testing whether these differences are
In sequential settings, proper tests—such
robust.
as Diebold–Mariano or paired tests over
repeated
runs—are required to separate systematic gains from
noise. Without them, non-replicable results may be mis-
taken for progress.

This limitation becomes evident when coarse labels
are used to summarize complex dynamics. For exam-
ple, assigning the entire financial crisis period to a sin-
gle regime X” and the post-crisis to regime Y” ignores
the presence of multiple microdrifts within each phase.
In such cases, methods that merely react to large, well-
defined shocks may appear overly effective. Similarly,
validation on synthetic data with simple linear or abrupt
drifts can lead to overly optimistic conclusions, as de-
tectors tuned to these idealized settings often struggle
when faced with the nonlinear, overlapping, and grad-
ual changes observed in real markets.

Preprint not peer reviewed

Addressing these challenges opens several directions
for future research. One avenue is the development of
better-annotated benchmark data sets, possibly combin-
ing expert knowledge with data-driven labeling and un-
certainty quantification. More generally, evaluation pro-
tocols should constrain adaptation rules, computational
budgets, and retraining strategies to ensure comparabil-
ity. Detection frequency, false-alarm cost, and adapta-
tion latency should be reported explicitly. In financial
settings, downstream metrics may include risk-adjusted
returns, drawdowns, or turnover. This framing shifts
evaluation from proxy-based drift detection to robust-
ness and decision-relevant utility under realistic non-
stationary conditions.

Future research should prioritize controlled and stan-
dardized evaluation protocols,
in which all methods
should share the same data access, tuning budget, and
temporal constraints. Performance comparisons must
include significance testing and repeated runs.
In fi-
nance, multiple-testing corrections should be manda-
tory. Such practices would reduce spurious results and
enable more reliable assessment of progress under non-
stationarity.

A central limitation concerns the assumption of in-
dependence within regimes. Much of the concept-drift
literature models data as i.i.d. until an abrupt change,
after which a new i.i.d.
In con-
trast, financial time series exhibit strong temporal de-
pendence, including autocorrelation and heteroskedas-
ticity, even within stable regimes.

A second family of threats stems from inadequate
evaluation protocols, which can bias conclusions about
drift detectors and adaptation methods. These threats
fall into two categories: internal validity, related to ex-
perimental control, and statistical-conclusion validity,
related to the strength of the empirical evidence.

Another family of threats arises from modeling as-
sumptions and from the design of adaptation mecha-
nisms. To make analysis tractable, many studies adopt
simplifying assumptions that rarely hold in operational
settings, which weakens both construct and external va-
lidity.

Internal-validity problems arise when methods are
not compared under the same conditions. Common is-
sues include unequal access to data or computation, un-
even hyperparameter tuning, and inconsistent tempo-
In drift studies, it is frequent that one
ral protocols.

Beyond temporal dependence, many approaches also
assume a fixed feature space. Most methods focus on
distribution shifts in the target or in observed covariates,

threats
statistical-conclusion validity)

8.3. Modeling- and adaptation-related threats

8.2. Evaluation-protocol

regime is assumed.

(internal

and

41

This preprint research paper has not been peer reviewed. Electronic copy available at: https://ssrn.com/abstract=6170273

---

<!-- PAGE 42 -->

9. Conclusion

while ignoring feature evolution. In real systems, how-
ever, variables may appear, disappear, or change rele-
vance over time.

By confronting these limitations honestly and build-
ing robust evidence, the field can progress toward pro-
viding finance practitioners with reliable tools to navi-
gate a world of ever-changing data.

As a consequence, detectors that ignore temporal
structure may respond to volatility clustering or tran-
sient dynamics rather than to genuine regime changes,
producing misleading signals. When this occurs, a de-
tector may correctly identify a distribution shift but fail
to adapt because the informative features themselves are
not updated.

These modeling assumptions also propagate directly
to adaptation mechanisms. Evaluation setups often
presume that retraining or model updates can be per-
formed at negligible cost and without operational side
effects. In practice, adaptation introduces latency, com-
putational overhead, and potential instability, especially
when labels are delayed or noisy. When such costs are
ignored, explains why methods that perform well under
controlled benchmarks may fail when exposed to real
financial data.

Future research should therefore move toward more
realistic modeling and evaluation. Methods should be
tested on temporally dependent data with overlapping
sources of change, such as concurrent shifts in mean
and volatility. Feature evolution should be explicitly
modeled rather than assumed away. Finally, adaptation
costs, delays, and stability effects should be incorpo-
rated into evaluation protocols. Addressing these points
is essential for bridging the gap between laboratory per-
formance and real-world robustness.

tightly calibrated to past patterns often struggle to main-
tain their predictive performance under new conditions.
Future research should prioritize broader and more
systematic evaluations across multiple assets and time
spans, with explicit attention to replicability. Claims
about specific regimes should be tested in analogous set-
tings, and greater emphasis should be placed on struc-
turally grounded approaches that reduce overfitting and
enhance generalization, thereby increasing the likeli-
hood that methods maintain their effectiveness outside
of the original test conditions.

Preprint not peer reviewed

In the financial domain, several challenges threaten
external validity, that is, the ability of results to gen-
eralize across markets and time periods. A key issue
is the factor zoo, in which many reported factors or
strategies show positive historical performance but fail
to replicate out of sample. An analogous risk arises for
learning-based methods, which may become overfitted
to the characteristics of specific markets and time win-
dows rather than capturing broadly stable relationships.
This risk becomes more pronounced in studies that
rely on narrow evaluation settings, where a method may
perform well on a specific market or historical period
but fail to generalize to other assets or time spans. For
example, a regime detector could capture bull–bear al-
ternations in US equities between 2000 and 2020 with
high accuracy, yet its effectiveness might not carry over
to emerging markets or to earlier historical intervals. As
financial structures evolve over time, methods that are

The study shows that the literature adequately defines
the various forms of drift, provides approaches to repre-
sent financial series and integrate internal and external
information, proposes methods to automatically detect
changes, and explores adaptive mechanisms to maintain
predictive performance over time. Nevertheless, eval-
uation and benchmarking practices remain underdevel-
oped, with limited standardization, weak replicability,
and insufficient consideration of operational constraints.
A key insight is that there is no universally opti-
mal detector or adaptation strategy. Method selection
must align with the expected type, scale, and dynamics
of drift, while deployment decisions must account for
computational and operational constraints. Evaluation
practices should extend beyond predictive accuracy to
include detection delay, false-alarm control, economic
utility, and realistic backtesting that incorporates trans-
action costs and market frictions.

This research organized the literature on machine
learning, econometrics, and quantitative finance into a
coherent framework specifically focused on financial
time series. We proposed a four-axis taxonomy to char-
acterize non-stationarity, encompassing temporal, sta-
tistical, spatial, and ontological dimensions. Exter-
nal representations of non-stationarity were organized
around embeddings, multiscale features, and both en-
dogenous and exogenous context. In addition, we struc-
tured the literature as an end-to-end pipeline covering
drift detection, continuous adaptation, evaluation, and
benchmarking.

Addressing these gaps requires future research fo-
cused on standardized, multi-market benchmarks and
decision-centric evaluation protocols that incorporate

8.4. Finance-specific limitations: “factor zoo”, repli-
cability, and generalization (external validity)

42

This preprint research paper has not been peer reviewed. Electronic copy available at: https://ssrn.com/abstract=6170273

---

<!-- PAGE 43 -->

Disclaimer

ing – review.

Data availability

Methodology, Writing – review & editing.

CRediT authorship contribution statement

Adriano L. I. Oliveira: Supervision, Validation, Writ-

Gustavo H. F. M. Oliveira: Conceptualization,

Davi M. Cabral: Data Curation, Conceptualization,
Methodology, Writing – original draft, Writing – review
& editing, Visualization.

The views expressed in this article are those of the au-
thors and do not necessarily reflect the official positions
of their institutions.

economic outcomes, implementation costs, and real-
world deployment considerations. Taken together, these
points highlight that methodological performance can-
not be separated from practical feasibility.

No new datasets were created in this survey. The
bibliographic metadata of the reviewed corpus (Bib-
TeX) and machine-readable versions of the survey ta-
bles (CSV) are available from the corresponding author
upon reasonable request. Code used to generate illustra-
tive plots is publicly available in the authors’ repository
(see the caption of Fig. 7). Copyrighted full-text arti-
cles are not shared. Underlying third-party index data
accessed via FRED (e.g., SP500/VIXCLS) are not re-
distributed.

In conclusion, by offering a unified taxonomy and
structured pipeline, this survey provides a framework
to support more comparable evidence, facilitate reli-
able implementation, and strengthen the feedback loop
between methodological advances and practical appli-
cations in finance, emphasizing that addressing non-
stationarity in financial time series is inherently a sys-
tems problem spanning representation, detection, adap-
tation, and evaluation under practical and economic
constraints.

Preprint not peer reviewed

During the preparation of this work the authors used
ChatGPT to improve the clarity and quality of the writ-
ing. After using this tool/service, the authors reviewed
and edited the content as needed and take full responsi-
bility for the content of the published article.

The authors declare that they have no known com-
peting financial interests or personal relationships that
could have appeared to influence the work reported in
this paper.

This research did not receive any specific grant from
funding agencies in the public, commercial, or not-for-
profit sectors.

Declaration of generative AI and AI-assisted tech-
nologies in the manuscript preparation process

Adriano Lima: Visualization, Writing – review &

Declaration of Competing Interests

Funding

editing.

43

This preprint research paper has not been peer reviewed. Electronic copy available at: https://ssrn.com/abstract=6170273

<!-- MARKITDOWN CONVERSION -->

<!-- Full MarkItDown conversion for formatting fidelity. -->

d
e
Non-Stationarity in Financial Time Series: A Unifying Survey on Drift
w
|     |     |     | Detection, |     | Adaptive | Learning, |     | and | Evaluation |     |     |     |     |
| --- | --- | --- | ---------- | --- | -------- | --------- | --- | --- | ---------- | --- | --- | --- | --- |
DaviM.Cabrala,∗,AdrianoM.A.Limaa,GustavoH.F.M.Oliveirab,AdrieanoL.I.Oliveiraa
aCentrodeInformática(CIn),UniversidadeFederaldePernambuco,Recife,PE,Brasil
bSistemasdeInformação,UniversidadeFederaldeAlagoas,Penedo,ALi,Brasil
v
e
Abstract
Predictiveanddecisionmodelsinfinancearetypicallyvalidatedunrderassumptionsofdistributionalstabilityover
the evaluation window. In deployment, those assumptions fail: the data-generating process undergoes structural

change—breaks,regimetransitions,anddrift—thatcaninvalidateconditionalrelationships,degradecalibration,and
amplify tail risk precisely when decisions are most consequentrial. Despite a large literature, results remain hard to
reconcileacrosseconometrics,statisticalmonitoring,andmachinelearningduetodivergentterminologyandincom-
e
patible evaluation protocols. This survey aims to overcome the fragmentation and provides three concrete tools for
research and deployment under non-stationarity in financial time series: (1) a unified taxonomy of drift and regime
change, (2) a pipeline that connects representation,edetection, and adaptation choices, and (3) an evaluation play-
book that supports apples-to-apples comparison. We align terms such as structural breaks, regimes, concept drift,
and dataset shift, and propose a taxonomy along temporal, statistical, spatial, and ontological axes to describe real
wpe
drift scenarios consistently. Using this lens, review drift-aware representations, change detection methods, and
continuous adaptation strategies—from classical sequential monitoring and segmentation to Bayesian, multivariate,
and embedding-based out-of-distribution approaches. We then consolidate evaluation guidance spanning detection

delay,false-alarmcontrol,computationalcost,andfinance-specificutility. Finally,wehighlightemergingdirections
(foundation models, multimodal context t , parameter-efficient adaptation) and open challenges in benchmark design
| andreliableonlinecalibration. |     |     |     | o   |     |     |     |     |     |     |     |     |     |
| ----------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Keywords:
financialtimeseries,non-stationarity,conceptdrift,change-pointdetection,adaptivelearning,evaluationprotocols
n
1. Introduction predictive modeling in real-world, high-stakes deploy-

ments.
| Financial        | markets   | aretdynamic |           | and         | inherently | non-       |                                                    |            |                  |          |                 |             |              |
| ---------------- | --------- | ----------- | --------- | ----------- | ---------- | ---------- | -------------------------------------------------- | ---------- | ---------------- | -------- | --------------- | ----------- | ------------ |
|                  |           |             |           |             |            |            | In                                                 | practice,  | non-stationarity |          | progressively   |             | degrades     |
| stationary       | systemsn, | in          | which     | the data    | generation | pro-       |                                                    |            |                  |          |                 |             |              |
|                  |           |             |           |             |            |            | the                                                | predictive | performance      |          | and calibration |             | of forecast- |
| cess alternates  | between   |             | distinct  | statistical | regimes    | due        |                                                    |            |                  |          |                 |             |              |
|                  |           |             |           |             |            |            | ing                                                | models     | [? ?             | ? ? ].   | Under           | prequential | evalua-      |
| to macroeconomic |           | shocks,     | liquidity |             | crises,    | regulatory |                                                    |            |                  |          |                 |             |              |
|                  | shiifts   |             |           |             |            |            | tion,thisdegradationmanifestsassystematicincreases |            |                  |          |                 |             |              |
| changes,         | and       | in          | agent     | behavior    | [? ?       | ? ? ].     |                                                    |            |                  |          |                 |             |              |
|                  |           |             |           |             |            |            | in forecast                                        |            | error, unstable  | decision |                 | thresholds, | and de-      |
Thisphenomrenonappearsintheliteratureundervarious
|                             |     |                        |                 |                     |            |        | layed                                           | reactions       | to  | new regimes—often     |        | precisely | when        |
| --------------------------- | --- | ---------------------- | --------------- | ------------------- | ---------- | ------ | ----------------------------------------------- | --------------- | --- | --------------------- | ------ | --------- | ----------- |
| terms—including             |     | concept                | drift,          | regime              | change,    | struc- |                                                 |                 |     |                       |        |           |             |
| p                           |     |                        |                 |                     |            |        | errorsaremostcostlyintermsofriskexposureandeco- |                 |     |                       |        |           |             |
| tural breaks,               | and | heteroscedasticity—and |                 |                     | directly   | af-    |                                                 |                 |     |                       |        |           |             |
|                             |     |                        |                 |                     |            |        | nomic                                           | decision-making |     | [?                    | ? ? ]. | These     | effects ex- |
| fectscorefinancialtasks[??? |     |                        |                 | ??]suchaspricefore- |            |        |                                                 |                 |     |                       |        |           |             |
|                             |     |                        |                 |                     |            |        | pose                                            | the limitations |     | of stationarity-based |        |           | assumptions |
| caesting, riskmanagement,   |     |                        | orderexecution, |                     | andportfo- |        |                                                 |                 |     |                       |        |           |             |
andmotivateapproachescapableofanticipatingandre-
| lio allocation | [?  | ? ], creating |     | persistent | challenges | for |     |     |     |     |     |     |     |
| -------------- | --- | ------------- | --- | ---------- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- |
spondingtodistributionshiftsastheyoccur.
| r   |     |     |     |     |     |     | Addressing |     | these | challenges | requires | coupling | drift- |
| --- | --- | --- | --- | --- | --- | --- | ---------- | --- | ----- | ---------- | -------- | -------- | ------ |
∗Correspondingauthor.Email:dmc6@cin.ufpe.br awarerepresentationswithtimelychangedetectionand
PEmailaddresses:dmc6@cin.ufpe.br(DaviM.Cabral),
|     |     |     |     |     |     |     | continuous |     | adaptation | [? ? | ? ? | ? ], | while evalua- |
| --- | --- | --- | --- | --- | --- | --- | ---------- | --- | ---------- | ---- | --- | ---- | ------------- |
amal@cin.ufpe.br(AdrianoM.A.Lima),
|     |     |     |     |     |     |     | tion | must explicitly |     | account | not only | for | predictive ac- |
| --- | --- | --- | --- | --- | --- | --- | ---- | --------------- | --- | ------- | -------- | --- | -------------- |
gustavo.oliveira@penedo.ufal.br(GustavoH.F.M.
Oliveira),alio@cin.ufpe.br(AdrianoL.I.Oliveira) curacy but also for detection delay and computational
| PreprintsubmittedtoNeurocomputing |     |     |     |     |     |     |     |     |     |     |     | February2,2026 |     |
| --------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | -------------- | --- |
This preprint research paper has not been peer reviewed. Electronic copy available at: https://ssrn.com/abstract=6170273

d
e
constraints[? ? ]. Inpractice, theeffectivenessofthis vergingacrosscommunities.Asaresult,machinelearn-
couplingdependscriticallyonhowdataarerepresented, ing,econometrics,andquantitwativefinancehavelargely
sinceinformativerepresentationsarenecessarytomake evolved in parallel, with limited cross-fertilization and
distributionshiftsobservableratherthanmaskingthem incompatibleframeworks. Theabsenceofasharedtax-
[? ? ]. Thisdependencynaturallyshiftsattentiontothe onomyandstandardizedevaluationhinderscumulative
e
role and design of financial data representations under evidenceandslowstheadoptionofdrift-awaremethods
non-stationarity. in practice, particularly in real-time and high-stakes fi-
Innon-stationaryfinancialenvironments,datarepre- nancialsettings[? ? ].
i
sentations must capture both endogenous market dy- With the aim of addressing these gaps, we formu-
v
namics and exogenous drivers. Embeddings learned latethefollowingresearchquestions: (RQ1)Howdoes
from price and volume series summarize endogenous the literature define and categorize the different forms
e
behavior, enabling comparisons across historical peri- of non-stationarity in financial time series? (RQ2)
odsandtheidentificationoflatentregimesbeyondclas- How can financial series be represented by integrat-
sicalindicators[??].However,marketbehaviorisalso ing endogenous and exogenous information to sup-
r
shapedbyexternalforces—suchasmacroeconomican- portthedetectionandinterpretationofregimechanges?
nouncements,geopoliticalevents,andfirm-leveldisclo- (RQ3 )Howcandistributionshiftsbeautomaticallyde-
sures—whicharenotobservableinpricedataalone.In- tected over time? (RQ4) How can model learning be
r
corporatingexogenousinformationthroughmultimodal adapted to distribution shifts continuously and effec-
inputs(e.g.,news,textualreports,andeconomicindica- etively? (RQ5) How can detection and adaptation sys-
tors)addseconomiccontexttodetectedshifts[? ? ? ], tems be evaluated under non-stationarity using appro-
yieldingrepresentationsthataremoreexpressiveunder priatemetricsandprotocols? (RQ6)Howcandetection
e
conceptdriftandbettersuitedtodistinguishingtransient and adaptation methods be benchmarked under non-
fluctuationsfromstructurallymeaningfulregimetransi- stationarity?(RQ7)Whatarethecurrentlimitationsand
tions. pfutureresearchdirections?
Withsuchenrichedrepresentations,continuousadap- In addressing these questions, this work makes four
tation becomes feasible. Model behavior can be up- contributions. (i) We introduce a unified taxonomy
datedthroughclassicalmechanisms—includ ingforget- of drift and regime change phenomena in financial
tingfactorsandregime-switchingstructutres[? ? ? ? ? timeseries,aligningterminologyacrossmachinelearn-
]—aswellasthroughmodernarchitecturesthatsupport ing, econometrics, andquantitativefinance(RQ1, Sec-
o
lightweight domain adaptation, such as specialized fi- tion 2). (ii) We structure the literature around a five-
nancialfoundationmodels[??].Inbothcases,contex- pillarpipeline—non-stationaritycharacterization,drift-
tualizedrepresentationsenablnemodelstorespondmore aware representations, change detection, continuous
selectivelyandinterpretablytoevolvingconditions,bal- adaptation, and evaluation—and review representative
ancing stability and responsiveness to improve robust- approaches for representation learning, change detec-
ness in online forecasting and decision-making. How- tion, and adaptation (RQ2–RQ4, Sections 3, 4, and
ever, the practical relevtance of these adaptive gains is 5).(iii)Wesummarizeevaluationmetrics,experimental
inseparablefromhowmodelperformanceisdefinedand protocols,andbenchmarkingpracticesusedinfinancial
n
measuredovertime. timeseries(RQ5–RQ6,Sections6and7). (iv)Finally,
Evaluation therefore emerges as a third essential di- we synthesize current limitations and outline open re-
mension,compleimentingrepresentationandadaptation. searchdirections(RQ7,Sections8and9).
To ensure prractical effectiveness, evaluation protocols
mustjointlyaccountforpredictiveperformance,detec- 1.1. Researchmethodologyandrelatedwork
tionspeped, false-alarmcontrol, computationalbudgets, Thissurveywasdevelopedthroughaniterativestrat-
and economic impact, reinforcing the need for realis- egy for literature retrieval, reading, and synthesis,
tic and comparable benchmarks [? ? ? ? ? ? ]. guidedbykeywordsearchesandbythetemporalchain-
e
Despite advances along these axes, progress remains ing of contributions. Initial searches were carried out
uneven and often confined to specific methodological inbroad-coveragedigitallibrariesandacademicaggre-
rtraditions, limiting comparability and cumulative evi- gators(e.g.,ScienceDirect,IEEEXplore,ACMDigital
dence. Library,SpringerLink,andGoogleScholar),withapri-
P
Atabroaderlevel,thetheoreticallandscaperemains maryfocusonpublicationsfrom2000to2025. When-
fragmented [? ? ? ? ], with modeling assumptions, ever needed to contextualize modern formulations of
methodological choices, and evaluation practices di- driftandregimechanges,wealsoincludedasmallsetof
2
This preprint research paper has not been peer reviewed. Electronic copy available at: https://ssrn.com/abstract=6170273

d
e
earlierfoundationalreferences(e.g.,insequentialanal- tionalchangesandregimes;(4)adaptationmechanisms;
ysis,econometrics,andchange-pointdetection). and (5) evaluation and benchwmarking. We emphasize
Searchstringscombinedthreeintersectingfronts: (i) thatthegoalisnottoexhaustivelycoverallpublications
non-stationarity terminology (e.g., concept drift, dis- in this rapidly growing area, but to highlight seminal
tribution shift, regime change/shift, structural break, and representative contributions that clarify concepts,
change point); (ii) operational mechanisms (e.g., drift design trade-offs, and pr e actical implications for finan-
detection, change-point detection, sequential tests, cialdeployment.
adaptive/continual learning, test-time adaptation, re-
i
training,ensembles);and(iii)financialcontextsandre-
2. DriftsandRevgimesFoundationsandTaxonomy
alisticprotocols(e.g.,algorithmictrading,riskmanage-
ment,portfolio,volatility,marketmicrostructure,back- Thissectionseekstoanswerthequestion: howdoes
testing,transactioncosts).Beyondsurveysandreviews, the literaturee define and categorize the different forms
we also considered experimental and methodological of non-stationarity in financial time series? Different
studieswhenevertheycontributeddirectlytoanswering fields — statistics, econometrics, machine learning, fi-
r
theRQsandtostructuringthesurvey’spipeline(foun- nance,andthenaturalsciences—proposecomplemen-
dations,detection,adaptation,andevaluation). taryta xonomiestoaddressnon-stationarity. Inthiscon-
The corpus was progressively refined based on topi- text, there is a broad consensus that non-stationarity
r
calrelevanceandusefulnessfortheproposedsynthesis, referstovariation, overtime, inthestatisticalorstruc-
complementedbysnowballing(backwardandforward) etural properties of a data-generating process [? ? ? ?
fromseminalworks,recentsurveys,andrecurringrefer- ? ]. However, beyond this high-level definition, these
ences. Thisprocessresultedinasupersetof289unique fields differ in the way such changes in the data distri-
e
candidate references (deduplicated across sources and butionareformalized,categorized,andanalyzed.
rounds). Motivated by these differences in conceptualization
A central element of this refinement waspexamin- and emphasis, we present an ontology, illustrated in
ing the future-work sections of the retrieved papers Figure 1, that describes the non-stationarity problem
and,wheneverpossible,checkingwhethertheproposed in financial time series [? ? ? ? ? ] along four
directions were later investigated or addre ssed. This main classification axes: (i) a temporal axis, which
“from-future-to-present”trackingservedtasastructured characterizeswhenandhowchangesunfoldovertime;
scan of gaps and adjacent research lines: by relating (ii) a statistical axis, which specifies which proper-
o
explicit recommendations to subsequent evidence, we ties of the data-generating process are affected; (iii) a
were able to make persistent gaps explicit and map spatial axis, which describes where changes manifest
emerging themes correlated wnith regime changes and within the data structure; and (iv) an ontological axis,
concept drift (e.g., GNNs, foundation models, multi- whichdistinguishesthenatureandformalstatusofthe
modality, deep reinforcement learning, and knowledge change. Finally,wediscussthecausalaxis,whichiden-
representation). After an initial relevance screening tifiestheunderlyingdriversofnon-stationarity, includ-
and consolidation to retmove near-duplicates and out- ing exogenous shocks, endogenous feedback mecha-
of-scope items, this process yielded a shortlist of 220 nisms, and adversarial or institutional effects, linking
n
references. observeddriftsandregimetransitionstotheirsources.
For scope reasons and to preserve coherence with
the RQs and thie proposed conceptual pipeline, part 2.1. Temporalaxis
oftheseadjarcentthemeswasdeliberatelydeprioritized In the specific case of time series, non-stationarity
and not discussed in depth (e.g., topics centered on may affect the mean and variance of the very relation-
MLOpsp/operationalmonitoring, temporalfairness, pri- shipbetweenvariablesorthemechanismthatproduces
vacy/federatedlearning,andvintagedata/real-timedata them. Onewaytocharacterizetheseeffectsisbyfocus-
revisions,amongothers),remainingasopportunitiesfor ingonhowthechangesunfoldinrelationtothetiming
e
future work. The final manuscript therefore cites 174 andtemporalshapeofthechangeintheprocess,thatis,
references. howandwhenthechangeoccurs,forexample,asillus-
rFinally, the selected studies were organized accord- tratedinFigure2. Commontypesincludeabruptdrift,
ing to their predominant role in an end-to-end pipeline gradualdrift, incremental(orcontinuous)drift, andre-
P for financial systems under non-stationarity: (1) foun- current (or seasonal) drift [? ? ? ? ? ? ], but some
dations and terminology harmonization; (2) represen- surveys also highlight blips (transient deviations / out-
tation and context modeling; (3) detection of distribu- liers) to differentiate short-lived noise from structural
3
This preprint research paper has not been peer reviewed. Electronic copy available at: https://ssrn.com/abstract=6170273

d
e
Abrupt
Gradual Incremental Recurrent transition from an upward-trending regime to a
|     |     |     |     |     |     |     | downward-trending |     | regimwe, |     | as market | conditions |
| --- | --- | --- | --- | --- | --- | --- | ----------------- | --- | -------- | --- | --------- | ---------- |
how/when Temporal progressively weaken (from a bull market—a pe-
|     |     |     |     |     |     | ∆P(X) | riod | of broadly | rising | prices | and optimistic | senti- |
| --- | --- | --- | --- | --- | --- | ----- | ---- | ---------- | ------ | ------ | -------------- | ------ |
Regime
|     |     |                     |                  |     |     |                     | ment—to | a   | bear ma rket—a | period | of broadly | de- |
| --- | --- | ------------------- | ---------------- | --- | --- | ------------------- | ------- | --- | -------------- | ------ | ---------- | --- |
|     |     | O n to l o g i c al | Non-stationarity |     | Sta | ti s ti cal ∆P(Y|X) |         |     |                |        |            |     |
s tr u c t u r e w h a t cliningpricesandpessimisticsentiment1). e
Mechanism
∆P(Y)
S p a t ia l • Incremental / continuous drift: continuous drift
w h e r e
i
Global Local of parameters without a clear breakpoint or sta-
C au s al ble plateaus v , i.e., without discrete states. Exam-
w h y
|     |           |           |          |                     |             |                  | ples          | include | long-run                        | structural | (secular)    | trends, |
| --- | --------- | --------- | -------- | ------------------- | ----------- | ---------------- | ------------- | ------- | ------------------------------- | ---------- | ------------ | ------- |
|     |           | Exogenous |          | Endogenous          | Adversarial |                  |               |         |                                 |            |              |         |
|     |           |           |          |                     |             |                  | such          | aes the | multi-decade                    | decline    | in long-term | in-     |
|     |           |           |          |                     |             |                  | terestrates[? |         | ? ](Fig.3A),drivenbyslow-moving |            |              |         |
|     | Figure 1: | Extended  | taxonomy | of non-stationarity |             | along five axes: |               |         |                                 |            |              |         |
temporal(how/when),statistical(whatchanges),spatial(where),on-
forcesinsavingandinvestmentratherthanasingle
(structure/state),
tological with causal drivers (why) as the founda- abrruptshock.
tionallayer.

(A)DGS10
|     | changes                   | [? ? ? | ? ], which | we define | below   | to clar- | r   |     |     |     |     |     |
| --- | ------------------------- | ------ | ---------- | --------- | ------- | -------- | --- | --- | --- | --- | --- | --- |
|     | ifytheirtemporaldynamics. |        |            |           |         |          | e   |     |     |     |     |     |
|     | θ Abrupt                  |        |            | θ         | Gradual |          |     |     |     |     |     |     |
e
C2
|     |     |     |     | C1  |         | p   |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | ------- | --- | --- | --- | --- | --- | --- | --- |
|     |     |     | t   |     |         | t   |     |     |     |     |     |     |
|     |     | τ   |     |     | mixture |     |     |     |     |     |     |     |
(B)FEDFUNDS

|     | θ Incremental |     |     | θ   | Recurrent |     |     |     |     |     |     |     |
| --- | ------------- | --- | --- | --- | --------- | --- | --- | --- | --- | --- | --- | --- |
t
S2
o
S1
|     |                |                             | t           | n            |                     | t           |     |     |     |     |     |     |
| --- | -------------- | --------------------------- | ----------- | ------------ | ------------------- | ----------- | --- | --- | --- | --- | --- | --- |
|     | Figure2:       | Temporalmorphologyofdrifts: |             |              | Abrupt—suddenchange |             |     |     |     |     |     |     |
|     | at changepoint | τ; Gradual—transition       |             | interval     | where               | old and new |     |     |     |     |     |     |
|     | concepts       | coexist and                 | switch with |   each other | gradually;          | Incremen-   |     |     |     |     |     |     |
tal—continuousparameterdritftwithoutstableplateaus;Recurrent—
alternationbetweenpreviouslyobservedstates.
Figure3:U.S.interest-rateseriesatmacromonthlytimescales(sam-
n ple: 1962-01 to 2025-12). (A) 10-year Treasury constant-maturity
yield(DGS10;end-of-periodatthisfrequency).(B)Effectivefederal
• Abrupt drift: sudden change that establishes a fundsrate(FEDFUNDS),summarizingthestanceofU.S.monetary
newlevelailmostinstantaneously. policy.Overthisperiod,the10-yearyielddeclinesfromaround14%
Forinstance,the
intheearly1980stoabout8%intheearly1990s,around5–6%in
|     | revelatiorn | of  | a major | accounting | fraud | at a large |                 |      |                      |     |           |             |
| --- | ----------- | --- | ------- | ---------- | ----- | ---------- | --------------- | ---- | -------------------- | --- | --------- | ----------- |
|     |             |     |         |            |       |            | the late 1990s, | near | 2% in the mid-2010s, |     | and below | 1% in 2020. |
corporationmaytriggeranimmediatemarket-wide Policy-ratemovementsin(B)shapeshort-termfinancingconditions
p
sell-off, abruptly shifting volatility regimes, risk andcantransmittolongermaturitiesin(A)throughexpectationsand
premia, and correlation structures across related termpremia,althoughthe10-yearyieldalsoreflectsinflationexpec-
tationsandbroaderriskcompensation.Source:FRED[??].
|     | esectors, | withthenewpricedynamicsandinvestor |     |     |     |     |     |     |     |     |     |     |
| --- | --------- | ---------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
sentimentestablishingthemselveswithinhoursor
|     |     |     |     |     |     |     | •         |     | /        |         |                |        |
| --- | --- | --- | --- | --- | --- | --- | --------- | --- | -------- | ------- | -------------- | ------ |
|     |     |     |     |     |     |     | Recurrent |     | seasonal | drifts: | unlike gradual | drift, |
asingletradingsession.
| r   |           |        |            |          |     |              | which | describes | a one-way |     | transition | where old |
| --- | --------- | ------ | ---------- | -------- | --- | ------------ | ----- | --------- | --------- | --- | ---------- | --------- |
|     | • Gradual | drift: | transition | interval |     | in which ob- |       |           |           |     |            |           |
P
|     | servations | from | the | old and | new concepts | coex- |     |     |     |     |     |     |
| --- | ---------- | ---- | --- | ------- | ------------ | ----- | --- | --- | --- | --- | --- | --- |
1Inequitymarkets,acommonruleofthumbdefinesabull(bear)
|     | ist, | withafuzzyboundary(amixtureofstatesfor |     |     |     |     |     |     |     |     |     |     |
| --- | ---- | -------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
marketasarise(fall)ofabout20%ormoreinabroadmarketindex
some period). A canonical example is the slow overatleastatwo-monthperiod[??].
4
This preprint research paper has not been peer reviewed. Electronic copy available at: https://ssrn.com/abstract=6170273

d
e
|     |     |     |     |     |     |     |     | • / |     | /   |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
and new concepts coexist for some time, recur- Prior label target shift: change in P(Y) t
rent drift refers to settings in which previously (class/event proportions,wor the marginal distribu-
observed concepts reappear after a period. Sea- tion of the target). This captures situations where
sonaldriftisaspecialcaseofrecurrentdriftwhere thefrequencyofoutcomeschangesovertime,even
these recurrences follow a deterministic periodic ifconditionalrelationsarerelativelystable.Anex-
e
pattern. For example, trading volume and volatil- ample is a trading signal classifier where the pro-
ity patterns may exhibit recurrent behavior tied to portionofbuy/sell/holdsignalschangesovertime
monthlyoptionsexpirationcycles, quarterlyearn- due to changing market conditions, while the fea-
i
ingsannouncements,orannualtax-lossharvesting turesthatcharacterizeeachsignaltyperemainsim-
v
|     | periods,withsimilarstatisticalpropertiesrecurring |     |     |     |     |     |     | ilar. |     |     |     |     |     |
| --- | ------------------------------------------------- | --- | --- | --- | --- | --- | --- | ----- | --- | --- | --- | --- | --- |
atregularintervals.
|     |     |     |     |     |     |     |     | • Class-econditional |     | shift: | change | in P (X | | Y) |
| --- | --- | --- | --- | --- | --- | --- | --- | -------------------- | --- | ------ | ------ | ------- | ---- |
t
|     |     |     |     |     |     |     |     | with P(Y) | approximately |     | constant. | Again, | ap- |
| --- | --- | --- | --- | --- | --- | --- | --- | --------- | ------------- | --- | --------- | ------ | --- |
t
2.2. Statisticalaxis
|     |     |     |     |     |     |     |     | proximately" | indicates |     | a working | approximation: |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------ | --------- | --- | --------- | -------------- | --- |
thermarginalprevalenceofclasses/eventsistreated
Thestatisticalaxisspecifieswhichcomponentofthe
data-generating distribution changes over time. To un- as stable (or controlled for) over the comparison

window,whilethefeaturedistributionwithineach
| derstand,letP(X,Y)denotethejointprobabilitydistri- |     | t   |     |     |     |     |     |     |     |     |     |     |     |
| -------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
r classmoves(e.g.,duetomeasurement,microstruc-
butiongoverningthegenerationofinput–outputpairsat
effects).
timet,withthefactorizationP(X,Y)= P(Y | X)P(X). e ture, or representation For instance, in
|       |      |         |     | t           |              | t   | t    |         |            |       |      |                  |     |
| ----- | ---- | ------- | --- | ----------- | ------------ | --- | ---- | ------- | ---------- | ----- | ---- | ---------------- | --- |
|       |      |         |     |             |              |     |      | a model | predicting | order | book | price movements, |     |
| Here, | P(X) | defines | the | probability | distribution |     | from |         |            |       |      |                  |     |
t
whichinputsaredrawn,whileP(Y | X)definesthecon- the proportion of upward, downward, and stable
t
epricemovementsmayremainconstant,buttheor-
ditionalprobabilitygoverningthegenerationofoutputs
|     |     |     |     |     |     |     |     | der flow | patterns | characterizing |     | each movement |     |
| --- | --- | --- | --- | --- | --- | --- | --- | -------- | -------- | -------------- | --- | ------------- | --- |
giventheinputs.
|       |                                              |      |     |                    |     |      |        | class evolve  | as   | the composition |     | of market | partic-  |
| ----- | -------------------------------------------- | ---- | --- | ------------------ | --- | ---- | ------ | ------------- | ---- | --------------- | --- | --------- | -------- |
|       | Inthistaxonomy,categoriesaredefinedbythedom- |      |     |                    |     | p    |        |               |      |                 |     |           |          |
|       |                                              |      |     |                    |     |      |        | ipants shifts | from | predominantly   |     | retail to | institu- |
| inant | changing                                     | term | in  | this decomposition |     | (or, | equiv- |               |      |                 |     |           |          |
alently, in P(X | Y)P(Y)), i.e., whether the drift pri- tionaltraders,orastheprevalenceofspoofingand
|        |           | t        | t        |             |       |        |        |                                               |     |     |     |                   |     |
| ------ | --------- | -------- | -------- | ----------- | ----- | ------ | ------ | --------------------------------------------- | --- | --- | --- | ----------------- | --- |
|        | affects   |          |          |             |       |        |        | fakeorderschangesovertime.                    |     |     |     | IfP (Y)alsovaries |     |
| marily |           | P(X),    | P(Y),    | P(X         | | Y), | or P(Y | | X).  |                                               |     |     |     | t                 |     |
|        |           | t        | t        | t           |       | t      |        | materially,thesettingisbetterdescribedasamix- |     |     |     |                   |     |
| In     | practice, | however, | multiple | componentts |       | may    | evolve |                                               |     |     |     |                   |     |
turewithprior/labelshift.
| simultaneously. |     |     | Accordingly, | and | consistent |     | with the |     |     |     |     |     |     |
| --------------- | --- | --- | ------------ | --- | ---------- | --- | -------- | --- | --- | --- | --- | --- | --- |
o
| dominance-baseddefinitionabove,thecategoriesbelow |     |             |     |           |             |     |          | •       |           |          | /    |                  |     |
| ------------------------------------------------- | --- | ----------- | --- | --------- | ----------- | --- | -------- | ------- | --------- | -------- | ---- | ---------------- | --- |
|                                                   |     |             |     |           |             |     |          | Concept | (strict   | sense)   | real | drift: change    | in  |
| should                                            | be  | interpreted | as  | idealized | descriptors |     | that em- |         |           |          |      |                  |     |
|                                                   |     |             |     |           |             |     |          | P(Y |   | X), i.e., | a change | in   | the relationship | be- |
t
phasizetheprimarysourceofnchangeratherthanasmu- tween inputs and targets (often corresponding to
tuallyexclusivecases.
|     |                          |     |         |                |                     |         |       | "structural                                   | breaks" | or           | "regime | shifts" in         | econo- |
| --- | ------------------------ | --- | ------- | -------------- | ------------------- | ------- | ----- | --------------------------------------------- | ------- | ------------ | ------- | ------------------ | ------ |
|     |                          |     |         |                |                     |         |       | metrics/finance).                             |         | For example, |         | a price prediction |        |
|     | • Covariate              | /   | virtual | d rift: change |                     | in P(X) | while |                                               |         |              |         |                    |        |
|     |                          |     |         |                |                     | t       |       | modelmayobservethatthesametechnicalindica-    |         |              |         |                    |        |
|     | thepredictivemechtanismP |     |         |                | (Y | X)isassumedap- |         |       |                                               |         |              |         |                    |        |
|     |                          |     |         | t              |                     |         |       | tors(movingaverages,volumepatterns)thatprevi- |         |              |         |                    |        |
proximately invariant. Here, "approximately" re- ously signaled upward price movements now pre-
n
|     | flects | an idealized |     | assumption: | empirically, |     | one |     |     |     |     |     |     |
| --- | ------ | ------------ | --- | ----------- | ------------ | --- | --- | --- | --- | --- | --- | --- | --- |
dictdownwardmovements,reflectingafundamen-
|     |         | P(Y | | X) | ≈ P (Y | | X) on | the | overlap- |                            |     |     |     |     |     |
| --- | ------- | --- | ---- | ------ | ------- | --- | -------- | -------------------------- | --- | --- | --- | --- | --- |
|     | expects | t   |      | t′     |         |     |          | talchangeinmarketdynamics. |     |     |     |     |     |
pingsupporitofX(i.e.,regionswherebothperiods
assign nron-negligible probability mass), up to es- Many authors use the term concept drift in a broad
timationnoiseandminorresidualeffects.
|     |     |     |     |     |     |     | Inprac- | sense,todenoteanychangeinthedata-generatingpro- |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ------- | ----------------------------------------------- | --- | --- | --- | --- | --- |
ticpe,thedriftisinterpretedasbeingdrivenmainly cess ∆P(X,Y), and not only real drift ∆P(Y | X) [? ?
by context/environment or sampling changes that ]. Inthissurvey,weadopttherestrictedconvention: we
reserve“conceptdrift”for∆P(Y
movethedistributionofinputs. Forinstance,are- | X)(realdrift)anduse
e
turn forecasting model trained on a market index “distributionshift”or“non-stationarity”forthegeneral
|     | may | face covariate |     | drift when | the | composition | of  | case. |     |     |     |     |     |
| --- | --- | -------------- | --- | ---------- | --- | ----------- | --- | ----- | --- | --- | --- | --- | --- |
rtheindexshiftstowardtechnologycompaniesand Toavoidambiguity,whencitedauthorsuse“concept
away from traditional manufacturing firms, even drift”inthebroadsense,weexplicitlyflagthisandmap
P
though the relationship between company-level ittoourtaxonomybyidentifyingwhichterminthestan-
features (valuation ratios, momentum, volatility) dardfactorizationsofP(X,Y)isdrifting. Table1sum-
t
andexpectedreturnsremainsstable. marizes the main terminological equivalences across
5
This preprint research paper has not been peer reviewed. Electronic copy available at: https://ssrn.com/abstract=6170273

d
e
Shock/stress
| machine                                    | learning, | econometrics, |     | statistics, | and | quanti- |                 |     |     |     |     |     |
| ------------------------------------------ | --------- | ------------- | --- | ----------- | --- | ------- | --------------- | --- | --- | --- | --- | --- |
| tativefinanceforbroad-sense“conceptdrift,” |           |               |     |             |     | mapping |                 |     |     |     | w   |     |
| changesin∆P(X),∆P(Y),∆P(Y                  |           |               |     | | X),∆P(X   |     | |Y),and |                 |     |     |     |     |     |
|                                            | t         |               | t   | t           | t   |         | leveldezilamroN |     |     |     |     |     |
∆P(X,Y)totheircommonlyusednamesineachcom-
t
munity.
Reallocation:risk→safety
|                        |               |        |               | “dataset/distribution |         |          |     |     |     | e   |     |     |
| ---------------------- | ------------- | ------ | ------------- | --------------------- | ------- | -------- | --- | --- | --- | --- | --- | --- |
| In the                 | dataset-shift |        | literature,   |                       |         |          |     |     |     |     |     |     |
| shift” typically       |               | refers | to a mismatch |                       | between | training |     |     |     |     |     |     |
| and test distributions |               | (i.e., | the           | joint distribution    |         | differs  |     |     |     |     |     |     |
i
| across stages). |     | In contrast, | the | concept-drift |     | literature |     |     |     |     |     |     |
| --------------- | --- | ------------ | --- | ------------- | --- | ---------- | --- | --- | --- | --- | --- | --- |
v
| emphasizes | online/streaming |      | settings    |           | in which | the dis- |     |     |     |      |     |     |
| ---------- | ---------------- | ---- | ----------- | --------- | -------- | -------- | --- | --- | --- | ---- | --- | --- |
|            |                  |      |             | affecting |          |          |     |     |     | Time |     |     |
| tribution  | evolves          | over | time, often |           | the      | input–   |     |     |     |      |     |     |
e
targetrelationship.
|            |      |         |     |                           |     |     | Riskyasset(e.g.,equities) |     |     |     | Safeasset(e.g.,Treasuries) |     |
| ---------- | ---- | ------- | --- | ------------------------- | --- | --- | ------------------------- | --- | --- | --- | -------------------------- | --- |
| Throughout | this | survey, | we  | use “distribution/dataset |     |     |                           |     |     |     |                            |     |
shift” (or “non-stationarity”) as an umbrella term that Figure4:Schematicillustrationofflight-to-quality:duringstress,in-
r
coversbothoffline(train–test)andonline(time-varying) vestorsshiftfromriskyassetstosaferones,depressingriskyprices
andsupportingsafe-assetprices.
| settings, whilereserving“conceptdrift”forchangesin |                     |          |                |              |       |         |                     |     |               |     |                 |     |
| -------------------------------------------------- | ------------------- | -------- | -------------- | ------------ | ----- | ------- | ------------------- | --- | ------------- | --- | --------------- | --- |
| P(Y | X)underourrestrictedconvention.              |                     |          |                |              | [?    | ? ]     |                     |     | Externalshock |     |                 |     |
| t                                                  |                     |          |                |              |       |         | r                   |     |               |     |                 |     |
| But, in                                            | addition            | to these | terminologies, |              | other | classic | )citamehcs(levelXIV |     |               |     |                 |     |
|                                                    |                     |          |                |              |       |         | e                   |     |               |     | volatilityspike |     |
| dimensions                                         | of non-stationarity |          |                | can quantify | how   | much    |                     |     |               |     |                 |     |
| andwhichstatisticalmomentshavechanged[?            |                     |          |                |              |       | ? ? ? ? |                     |     |               |     |                 |     |
]:
e
| • First | order: | change | in E[X] | (mean, | trend) | or in |     |     |     |     |     |     |
| ------- | ------ | ------ | ------- | ------ | ------ | ----- | --- | --- | --- | --- | --- | --- |
t
| univariatelocationstatistics; |     |     |     |     |     |     |     |     |     |     |     | meanreversion |
| ----------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------- |
p
low-volregime
•
| Secondorder: |     | changeinVar(X)(volatility)orin |     |     |     |     |     |     |     |     |     |     |
| ------------ | --- | ------------------------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
t
| Cov(X,X |     | )(autocorrelation)2[? |     |     | ? ];and |     |     |     |     | Time |     |     |
| ------- | --- | --------------------- | --- | --- | ------- | --- | --- | --- | --- | ---- | --- | --- |
t t−k

| • Multivariate: |     | change | in  | cross-dependence |     | (e.g., |          |                              |     |     |     |                   |
| --------------- | --- | ------ | --- | ---------------- | --- | ------ | -------- | ---------------------------- | --- | --- | --- | ----------------- |
|                 |     |        |     |                  | t   |        | Figure5: | SchematicexampleofaVIXspike: |     |     |     | anabruptjumpinim- |
covariance/correlation
across variables or assets) pliedvolatilityaroundashock,followedbygradualnormalization.
o
| andtaildependence3[? |     |     | ?   | ? ? ? | ].  |     |     |     |     |     |     |     |
| -------------------- | --- | --- | --- | ----- | --- | --- | --- | --- | --- | --- | --- | --- |
In multivariate settings, drifts may affect variances, ity explosions characterized by abrupt spikes in im-
n
covariance, correlation, and tail dependence across as- pliedvolatility(Fig.5),andincreasesincorrelationsand
sets. Financialcrisesaretypicallymarkedbyanabrupt taildependencereflectingcrisiscontagionmechanisms
increase in tail dependence, with losses converging (Fig.6). Thesephenomenaoccurinparallel,combining

first-order,second-order,andmultivariateeffects.
| across assets | that | were | previously | weakly | correlated, |     |     |     |     |     |     |     |
| ------------- | ---- | ---- | ---------- | ------ | ----------- | --- | --- | --- | --- | --- | --- | --- |
t
leadingtothecollapseofdiversificationstrategies(see Figure 7 illustrates the typical inverse co-movement
Fig. 6). Conceptually, n such changes can be described between equity prices and implied volatility: equity
[?
as breaks in covariance matrices, transitions in depen- drawdowns often coincide with increases in VIX ],
dence graphs (financial networks), or changes in dy- which is computed from S&P 500 index option prices
i
|     |     |     |     |     |     |     | and is widely |     | used as | a market | “fear | gauge” [? ]. As |
| --- | --- | --- | --- | --- | --- | --- | ------------- | --- | ------- | -------- | ----- | --------------- |
namiccopulasthatcaptureasymmetricdependenceand
r
heavy tails [? ? ? ? ? ]. In these episodes, changes an example of a news-driven repricing episode, late-
of different orders often coexist: mean shifts associ- Jan.2025coveragereportedasharptech-ledsellofffol-
p
|           |                   |     |          |     |           |          | lowing                             | DeepSeek-related |                 | developments, |       | accompanied        |
| --------- | ----------------- | --- | -------- | --- | --------- | -------- | ---------------------------------- | ---------------- | --------------- | ------------- | ----- | ------------------ |
| ated with | flight-to-quality |     | dynamics |     | (Fig. 4), | volatil- |                                    |                  |                 |               |       |                    |
|           |                   |     |          |     |           |          | byaspikeinvolatilityexpectations[? |                  |                 |               |       | ? ? ].             |
| e         |                   |     |          |     |           |          | In terms                           | of               | the statistical |               | axis, | first/second-order |
2Foraunivariateseries{Xt },themeanisµt = E[Xt]andtheau- ∆P(X)
|                             |     |     |                 |                      |                      |     | tends to      | manifest | as           |            | changes        | in the features; |
| --------------------------- | --- | --- | --------------- | -------------------- | -------------------- | --- | ------------- | -------- | ------------ | ---------- | -------------- | ---------------- |
| tocovarianceatlaghisγ(h)    |     |     | = Cov(Xt+h,Xt); |                      | theautocorrelationis |     |               |          |              |            |                |                  |
|                             |     |     |                 |                      |                      |     | ∆P(Y) affects |          | marginal     | statistics | of the         | target; and real |
| r thenormalizedquantityρ(h) |     |     | = γ(h)/γ(0).    | Inweak(second-order) |                      |     |               |          |              |            |                |                  |
|                             |     |     |                 |                      |                      |     | drift ∆P(Y    | |        | X) manifests |            | as instability | of parame-       |
stationarity,µtisconstantandγ(h)dependsonlyonthelagh(noton
P t).
| 3Tail dependence |     | captures | extremal | co-movement | and | is often |     |     |     |     |     |     |
| ---------------- | --- | -------- | -------- | ----------- | --- | -------- | --- | --- | --- | --- | --- | --- |
quantifiedbycoefficientsdefinedaslimitsofconditionalquantileex- 4https://github.com/davimcabral/NonStationarityIn
ceedanceprobabilities. FinancialTS/blob/main/graphic_sp500_vix.ipynb
6
This preprint research paper has not been peer reviewed. Electronic copy available at: https://ssrn.com/abstract=6170273

d
e
|     |     |     | Crisis/contagion |     |     | • Globaldrift,whenthechangebroadlyaffectsthe |     |     |     |     |     |     |
| --- | --- | --- | ---------------- | --- | --- | -------------------------------------------- | --- | --- | --- | --- | --- | --- |
Normalconditions
|     |     |     |     |     |     | entire | domain, | impacting | w most | regions | of  | the fea- |
| --- | --- | --- | --- | --- | --- | ------ | ------- | --------- | ------ | ------- | --- | -------- |
turespaceorthemajorityofsubpopulationssimul-
|     |                    |     |     |     |     | taneously. |           | Forinstance,acentralbankinterestrate |         |           |          |        |
| --- | ------------------ | --- | --- | --- | --- | ---------- | --------- | ------------------------------------ | ------- | --------- | -------- | ------ |
|     |                    |     |     |     |     | change     | typically | affects                              | pricing | dynamics  |          | across |
|     | Taildependence:    | co- |     |     |     |            |           |                                      |         |           |          |        |
|     | movementinextremes |     |     |     |     |            |           | e                                    |         |           |          |        |
|     |                    |     |     |     |     | all asset  | classes   | and                                  | market  | segments, | inducing | a      |
(jointlossesbecome
system-wideshiftinexpectedreturnsandriskpre-
morelikely)
mia.
i
| lowercross-dependence                                         |     |     | highercorrelationand |     |     |                                               |         |              |        |             |     |          |
| ------------------------------------------------------------- | --- | --- | -------------------- | --- | --- | --------------------------------------------- | ------- | ------------ | ------ | ----------- | --- | -------- |
|                                                               |     |     | taildependence       |     |     | •                                             |         | v            |        |             |     |          |
|                                                               |     |     |                      |     |     | Local                                         | drift,  | when the     | change | is confined |     | to spe-  |
|                                                               |     |     |                      |     |     | cific                                         | regions | of the input | space, | such        | as  | a single |
| Figure6: Schematicillustrationofcrisiscontagioninacross-asset |     |     |                      |     |     |                                               |         |              |        |             |     |          |
|                                                               |     |     |                      |     |     | economicsector,assetclass,geographicmarket,or | e       |              |        |             |     |          |
network.Nodesrepresentassets(orvariables)andedgesdenotestatis-
ticaldependence,withthickeredgesindicatingstrongerdependence. customergroup. Forexample, regulatorychanges
Undernormalconditions(left),dependenceisweakeranddiversifi- affectingonlythepharmaceuticalsectormayalter
| cationiseffective. | Duringcrises(right),dependenceandtaildepen- |     |     |     |     |     |     |     |     |     |     |     |
| ------------------ | ------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
r
denceincrease,makingjointextremelossesmorelikelyandreducing the predictive relationships for healthcare stocks
diversificationbenefits. while leaving technology or energy sectors unaf-

|     |     |     |     |     |     | fected. | Thesechangesarespatiallyheterogeneous, |          |           |     |         |         |
| --- | --- | --- | --- | --- | --- | ------- | -------------------------------------- | -------- | --------- | --- | ------- | ------- |
|     |     |     |     |     |     | r       |                                        |          | difficult |     |         |         |
|     |     |     |     |     |     | often   | subtle,                                | and more |           | to  | detect, | requir- |
(A)S&P500andits125-daymovingaverage
e ingregion-awareorsubdomain-sensitivemonitor-
ingmethods.
e
|     |     |     |     |     |         | (A)GlobalDrift:MarketCrash |     |              |         | (B)LocalDrift:Sector-Specific |            |                  |
| --- | --- | --- | --- | --- | ------- | -------------------------- | --- | ------------ | ------- | ----------------------------- | ---------- | ---------------- |
|     |     |     |     |     | Returns |                            |     |              | Returns |                               |            |                  |
|     |     |     |     | p   |         |                            |     | —Tech        |         |                               |            | — T e c h        |
|     |     |     |     |     |         |                            |     | —Energy —Fin |         |                               |            | —E —n F ie n rgy |
|     |     |     |     |     |         |                            |     | —Health      |         |                               |            | —Health          |
|     |     |     |     |     |         |                            |     | noigertfird  |         |                               | tfirdlacol |                  |
(B)VIXandits50-daymovingaverage
drift

|     |     |     |     |     |     |           | Allsectors   |                  |     | Othersectors |          |          |
| --- | --- | --- | --- | --- | --- | --------- | ------------ | ---------------- | --- | ------------ | -------- | -------- |
|     |     |     | t   |     |     |           | droptogether |                  |     | stable       |          |          |
|     |     |     |     |     |     |           |              | t                |     |              |          | t        |
|     |     |     |     |     |     | Pre-crash |              | Mar2020 Recovery |     | Stable       | Oilcrash | Recovery |
o
Figure8:Spatialdriftinfinancialtimeseries.(A)Globaldrift:Dur-
ingtheMarch2020COVID-19marketcrash,allsectorsexperienced
synchronizedvolatilityincreaseanddrawdown—driftaffectstheen-
n
tiremarket.(B)Localdrift:Duringthe2014oilpricecollapse,only
|     |     |     |     |     | the                         | energy | sector (bold | orange)                              | experienced | significant |     | drift while |
| --- | --- | --- | --- | --- | --------------------------- | ------ | ------------ | ------------------------------------ | ----------- | ----------- | --- | ----------- |
|     |     |     |     |     | othersectorsremainedstable. |        |              | Localdriftrequiressector-specificde- |             |             |     |             |
Figure7:Co-movementbetweenequitypricesandimpliedvolatility   tectionandadaptationratherthanmarket-wideretraining.
| (dailydata).                               | Authors’ownplot. | Theplottingnotebookisavailable |     |      |        |         |                 |                |         |        |               |           |
| ------------------------------------------ | ---------------- | ------------------------------ | --- | ---- | ------ | ------- | --------------- | -------------- | ------- | ------ | ------------- | --------- |
| online.4.                                  | t                |                                |     |      |        |         |                 |                |         |        |               |           |
| DataaccessedviaFRED(seriesSP500andVIXCLS   |                  |                                |     | [? ? |        |         |                 |                |         |        |               |           |
|                                            |                  |                                |     |      |        | Beyond  | the distinction |                | between | global | and           | local ef- |
| ];underlyingindexdataarenotredistributed). | n                |                                |     |      |        |         |                 |                |         |        |               |           |
|                                            |                  |                                |     |      | fects, | spatial | drifts          | may differ     | in      | their  | structural    | foot-     |
|                                            |                  |                                |     |      | print  | across  | the             | feature space. | Changes |        | can propagate |           |
ters/coefficientsandofconditionaldependencies,going
|     | i   |     |     |     | smoothly |     | across | neighboring | regions, |     | remain | isolated |
| --- | --- | --- | --- | --- | -------- | --- | ------ | ----------- | -------- | --- | ------ | -------- |
beyondmarginalmoments[? ? ? ? ? ? ]. within well-defined clusters, or emerge along specific
r
unaffected.
|     |     |     |     |     | dimensions |     | while | leaving | others |     | Such | pat- |
| --- | --- | --- | --- | --- | ---------- | --- | ----- | ------- | ------ | --- | ---- | ---- |
2.3. Spatialaxis p ternsreflectthegeometryoftheinputspaceandthein-
Thespatialaxisconcernsthereachofachangewithin teractionstructureamongvariables,ratherthantempo-
thefeaturespaceoracrosssubpopulations,asillustrated ral ordering, and are naturally described through par-
e
in Fig. 8. It characterizes where in the input domain a titions of the feature domain, network representations,
change occurs and how broadly it spreads across vari- or conditional submodels tailored to specific subpopu-
| r ables, assets, | or groups. From | this | perspective, | spatial | lations. |     |     |     |     |     |     |     |
| ---------------- | --------------- | ---- | ------------ | ------- | -------- | --- | --- | --- | --- | --- | --- | --- |
changescanbedistinguishedaccordingtotheirextent, Whydoscalesmatterforthetaxonomy? Driftsman-
P rangingfromdriftsthataffecttheentiredomaintothose different
|     |     |     |     |     | ifest | at  |     | frequencies, | and | the | scale | often de- |
| --- | --- | --- | --- | --- | ----- | --- | --- | ------------ | --- | --- | ----- | --------- |
confinedtospecificregionsofthefeaturespace,asfor- termines which morphological pattern dominates. At
(years/decades),
malizedin[? ? ? ],anddescribedbelow: macro scales drifts tend to be abrupt
7
This preprint research paper has not been peer reviewed. Electronic copy available at: https://ssrn.com/abstract=6170273

d
e
Table1:Terminologicalequivalencesacrosstraditions(broad-sense“conceptdrift”).
w
|     |     |            |     | Machine         |     |                 |     |     |            | Quant   |     |     |
| --- | --- | ---------- | --- | --------------- | --- | --------------- | --- | --- | ---------- | ------- | --- | --- |
|     |     | Phenomenon |     | learning        |     | Econometrics    |     |     | Statistics | finance |     |     |
|     |     |            |     | Covariateshift/ |     | Exogenousshift/ |     |     |            |         |     |     |
Covariate
∆P(X)
tfirDtpecnoC )esnesdaorb( covariatedrift exogenousshock shift eMarketdislocation
Conceptdrift
|     |     |      |     |                   |     | Structural |       | Conditional     |       |             |     |     |
| --- | --- | ---- | --- | ----------------- | --- | ---------- | ----- | --------------- | ----- | ----------- | --- | --- |
|     |     | ∆P(Y | |X) | (strictsense)     |     |            | break |                 | shift | Regimeshift |     |     |
|     |     |      |     | Labelshift/prior- |     | Endogenous |       | Target/marginal |       | Behavioural |     |     |
i
|     |     | ∆P(Y) |     | probabilityshift |     |     | change |     | shift               |     | shift |     |
| --- | --- | ----- | --- | ---------------- | --- | --- | ------ | --- | ------------------- | --- | ----- | --- |
|     |     |       |     | Datasetshift/    |     |     |        |     | vMarketregimeshift/ |     |       |     |
∆P(X,Y) distributionshift Non-stationarity Jointshift non-stationarity
e
(policy shocks, interest-rate regime changes; Fig. 3B) through piecewise models with approximate stationar-
or incremental (secular trends linked to business and ity,wheretimeseriesalternatebetweenafinitenumber
r
monetary-policy cycles;Fig. 3A) [? ? ? ? ]. At of discrete and persistent states separated by change-
daily/weekly
scales, recurrent drifts prevail, associated points (see Fig. 9). Transitions between regimes may
with risk-on/risk-off switches, news cycles and repric- berabrupt,asduringfinancialcrises,orgradual,reflect-
ingofriskaroundannouncementwindows[? ? ? ? ]. ingslowstructuraladjustmentsintheeconomy.
e
Athighfrequency,intradayseasonalityandmicrostruc-
|     |     |     |     |     |     |     | This | framework | helps | clarify | the relationship | be- |
| --- | --- | --- | --- | --- | --- | --- | ---- | --------- | ----- | ------- | ---------------- | --- |
tureeffects(open/closepatterns,auctions,lunchbreaks)
|     |     |     |     |     |     |     | tweendriftandregimechange. |     |     | Everyregimetransition |     |     |
| --- | --- | --- | --- | --- | --- | --- | -------------------------- | --- | --- | --------------------- | --- | --- |
generate deterministic patterns that overlay structu ral necessarily involves a statistical change. But the con-
e
| driftsobservedatlongerhorizons[? |     |     |     | ?   | ? ]. Incryptoas- |     |     |     |     |     |     |     |
| -------------------------------- | --- | --- | --- | --- | ---------------- | --- | --- | --- | --- | --- | --- | --- |
versedoesnothold,becausemanydriftsarisefromcon-
sets,boom–bustcyclestendtooverlapwiththesescales, tinuousorincrementaladjustmentsthatdonotintroduce
whiledeterministicevents(suchashalvings)apctasnat- a new regime. For instance, a brief spike in volatility
| ural triggers | for | regime | changes | [? ]. | Multiscale | ap- |            |     |                        |     |         |             |
| ------------- | --- | ------ | ------- | ----- | ---------- | --- | ---------- | --- | ---------------------- | --- | ------- | ----------- |
|               |     |        |         |       |            |     | represents | a   | short-lived deviation, |     | whereas | a sustained |
proaches[? ? ? ] allowtimeseriestobedecomposed periodofelevatedvolatilityoverseveralmonthsreflects
| into different | frequencies, |     | reveal | regimes |  that | remain |     |     |     |     |     |     |
| -------------- | ------------ | --- | ------ | ------- | ----- | ------ | --- | --- | --- | --- | --- | --- |
agenuineregimechange.Thedistinctionbetweenthese
hiddenatsingleresolutions,andthusclatssifydriftsac- casesisillustratedinFig.9.
| cordingtotheirdominantscale[? |     |     |     | ? ? ? | ].  |     |                                                |     |     |     |     |     |
| ----------------------------- | --- | --- | --- | ----- | --- | --- | ---------------------------------------------- | --- | --- | --- | --- | --- |
|                               |     |     |     | o     |     |     | Inpractice,achangeistypicallyinterpretedasanew |     |     |     |     |     |
regimewhenitsatisfiesthreebroadcriteria[??].First,
2.4. Ontologicalaxis
|     |     |     |     |     |     |     | the change | must | be persistent, | lasting | long | enough to |
| --- | --- | --- | --- | --- | --- | --- | ---------- | ---- | -------------- | ------- | ---- | --------- |
n
|     |     |     |     |     |     |     | ruleouttransientnoise. |     | Second, | itmustbedistinctive, |     |     |
| --- | --- | --- | --- | --- | --- | --- | ---------------------- | --- | ------- | -------------------- | --- | --- |
Notallchangesindatacorrespondtothesametypeof
differ
structural transformation. Some variations reflect tran- meaning that its statistical properties meaning-
|     |     |     |     |     |     |     | fully | from those | observed | previously. | Finally, | regimes |
| --- | --- | --- | --- | --- | --- | --- | ----- | ---------- | -------- | ----------- | -------- | ------- |
sientfluctuationsarounda stablesystemconfiguration,
|     |     |     |     |     |     |     | may | be recurrent, | in the | sense that | the same | state can |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------- | ------ | ---------- | -------- | --------- |
whileotherssignaladeeperchangeinhowthedatagen-
t
|                    |        |                                  |     |                 |      |         | reappear                                     | over  | time, although       | recurrence     |     | is not a strict |
| ------------------ | ------ | -------------------------------- | --- | --------------- | ---- | ------- | -------------------------------------------- | ----- | -------------------- | -------------- | --- | --------------- |
| eration system     |        | operates.                        | The | ontological     | axis | focuses |                                              |       |                      |                |     |                 |
|                    |        | n                                |     |                 |      |         | requirement.                                 |       |                      |                |     |                 |
| onthesequalitative |        | differencesbetweendistinctsystem |     |                 |      |         |                                              |       |                      |                |     |                 |
| states.            |        |                                  |     |                 |      |         | Beyondregimechanges,theontologicalaxisencom- |       |                      |                |     |                 |
|                    |        |                                  |     |                 |      |         | passes                                       | other | forms of qualitative | transformation |     | in the          |
| A useful           | wayito | understand                       |     | such structural |      | changes |                                              |       |                      |                |     |                 |
is through the notion of a regime. Intuitively, a regime data-generatingprocess, capturingchangesinwhatthe
r
|     |     |     |     |     |     |     | system | is, rather | than only | in how | its statistical | prop- |
| --- | --- | --- | --- | --- | --- | --- | ------ | ---------- | --------- | ------ | --------------- | ----- |
correspondstoapersistentmodeofoperationofthedata
generatpionsystem. Whilearegimeisinplace,datafol- erties evolve. In financial applications, such transfor-
lowrelativelystablepatterns;whentheregimechanges, mationsincludeshiftsbetweenpersistentmarketstates,
theemergenceofnewmarketcategoriesorinstruments,
| these patterns |     | are altered | in a | systematic | and | lasting |     |     |     |     |     |     |
| -------------- | --- | ----------- | ---- | ---------- | --- | ------- | --- | --- | --- | --- | --- | --- |
e
way. In financial markets, common examples include andstructuralchangesinhowdataaregenerated,asil-
lustratedbyexamplessummarizedinTable2.
bullandbearphases,sustainedtransitionsbetweenlow-
rand high-volatility states, and crisis periods character- These ontological changes intersect with the tempo-
izedbypersistentlyhighcross-assetcorrelations. ral,statistical,andspatialaxes,butaredistinguishedby
P
In econometrics, from a modeling perspective, reflecting modifications in the underlying structure or
regimes are often treated as latent states that govern semantics of the problem, rather than purely quantita-
the data-generating process. This idea is formalized tivevariation[? ? ? ? ? ? ]. Commonempiricaldrivers
8
This preprint research paper has not been peer reviewed. Electronic copy available at: https://ssrn.com/abstract=6170273

d
e
(A)RegimeDrift:DiscreteStates (B)MechanismDrift:RelationshipChange 2.5. CausesofNon-Stationary
| Returns |     |     | Returns |     |     |     |     |     |     |     | w   |     |     |     |
| ------- | --- | --- | ------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
—Stocks—Bonds From a causal standpoint, drifts and regime changes
ρ(t)
µ>0,σlow BullRegime µ<0,σhigh BearRegime µ>0,σlow BullRegime -10+1 can be triggered by exogenous, endogenous, or adver-
|     |     |     |     |     | tfirdmsinahcem |     | sarialfactors. |     | Amongexogenousdrivers,monetarypol- |     |     |     |     |     |
| --- | --- | --- | --- | --- | -------------- | --- | -------------- | --- | ---------------------------------- | --- | --- | --- | --- | --- |
ρ<0
ρ>0
icyandinterest-ratecyclees,supplyanddemandshocks,
financialcrises,andgeopoliticaleventsstandout.These
|        |        |        |     | correlation Negative |                  | correlation Positive |                      |       |               |           |               |       |               |        |
| ------ | ------ | ------ | --- | -------------------- | ---------------- | -------------------- | -------------------- | ----- | ------------- | --------- | ------------- | ----- | ------------- | ------ |
|        |        | t      |     |                      |                  | t                    |                      |       |               |           |               |       |               |        |
|        |        |        |     |                      |                  |                      | forces               | alter | expectations, |           | risk pricing, |       | and risk      | premia |
| State1 | State2 | State1 |     |                      | structuralchange |                      |                      |       |               | i         |               |       |               |        |
|        |        |        |     |                      |                  |                      | acrossdifferenttimeh |       |               | orizons[? |               | ? ? ? | ]. Endogenous |        |
S1→S2 S2→S1 mechanisms arise v from within the financial system it-
|     |     |     |     |     |     |     | self. | Leverage, | liquidity |     | constraints, | margin | calls, | and |
| --- | --- | --- | --- | --- | --- | --- | ----- | --------- | --------- | --- | ------------ | ------ | ------ | --- |
Figure9:Ontologicaldriftinfinancialtimeseries.(A)Regimedrift:
feedbackdyenamicsbetweeninvestorstrategiescanam-
Discretestatetransitionsbetweenbullandbearmarkets.Eachregime
hasdistinctstatisticalproperties(µ,σ),buttheunderlyingdatagener- plifyshocksandgenerateregimetransitionseveninthe
ationmechanismremainsconsistentwithinstates. ModeledbyHid- absenceofnewexternalevents[? ? ? ].
| denMarkovModels(HMMs),regime-switchingmodels. |                                                 |     |     |     | (B)Mech- |     |       | r   |            |     |       |        |         |     |
| --------------------------------------------- | ----------------------------------------------- | --- | --- | --- | -------- | --- | ----- | --- | ---------- | --- | ----- | ------ | ------- | --- |
|                                               |                                                 |     |     |     |          |     | Table | 3   | summarizes | how | these | causal | drivers | map |
| anismdrift:                                   | Fundamentalrelationshipchanges—stock-bondcorre- |     |     |     |          |     |       |     |            |     |       |        |         |     |
lationshiftsfromnegativetopositive(asobserved2020-2022). The onto  the temporal, statistical, and spatial axes of the
correlationstructureρ(t)evolvescontinuously,representingachange proposed taxonomy, illustrating how different sources
| inthecausal/structuralrelationshipsratherthanjuststateswitching. |     |     |     |     |     |     | r                                                      |                |     |              |               |             |         |         |
| ---------------------------------------------------------------- | --- | --- | --- | --- | --- | --- | ------------------------------------------------------ | -------------- | --- | ------------ | ------------- | ----------- | ------- | ------- |
|                                                                  |     |     |     |     |     |     | of non-stationarityinducecharacteristicpatternsofdrift |                |     |              |               |             |         |         |
|                                                                  |     |     |     |     |     |     | eacross                                                | dimensions.    |     | In addition, |               | adversarial | or      | manipu- |
|                                                                  |     |     |     |     |     |     | lative                                                 | behaviors—such |     | as           | pump-and-dump |             | schemes | or      |
ofthesechanges—suchaspolicyinterventions,techno-
|                      |                   |           |         |                 |                  |         | spoofing | practices |        | in less    | liquid | markets—may |            | distort |
| -------------------- | ----------------- | --------- | ------- | --------------- | ---------------- | ------- | -------- | --------- | ------ | ---------- | ------ | ----------- | ---------- | ------- |
| logical innovations, |                   | or market |         | disruptions—are |                  | further |          |           |        |            |        |             |            |         |
|                      |                   |           |         |                 |                  | elocal  |          | signals.  | These  | actions    | often  | produce     | short-term |         |
| mapped to            | the corresponding |           | axes    | in              | Table 3.         | Within  |          |           |        |            |        |             |            |         |
|                      |                   |           |         |                 |                  |         | drifts   | that      | do not | correspond | to     | long-term   | structural |         |
| this framework,      | ontological       |           | changes |                 | can be organized |         |          |           |        |            |        |             |            |         |
changes.
| intothefollowingcategories: |     |     |     |     | p   |     |     |     |     |     |     |     |     |     |
| --------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Athighfrequency,marketmicrostructureeffectsplay
|          |        |     |             |     |         |         | a central | role. | Latency, | order | flow, | tick | size, and | mar- |
| -------- | ------ | --- | ----------- | --- | ------- | ------- | --------- | ----- | -------- | ----- | ----- | ---- | --------- | ---- |
| • Regime | change | —   | transitions |     | between | persis- |           |       |          |       |       |      |           |      |
 ketrulescancreatespecificregimes,suchasshallowor
tentlatentstateswithdistinctstatisticalsignatures,
deeporderbooks,narroworwidespreads,andwindows
| while | preserving | the | same | set | ofttarget | classes |     |     |     |     |     |     |     |     |
| ----- | ---------- | --- | ---- | --- | --------- | ------- | --- | --- | --- | --- | --- | --- | --- | --- |
ofelevatedmicrostructuralnoise.Thesemicrostructure-
| (e.g., | bull versus | bear | markets, |     | low versus | high |     |     |     |     |     |     |     |     |
| ------ | ----------- | ---- | -------- | --- | ---------- | ---- | --- | --- | --- | --- | --- | --- | --- | --- |
o
|     |     |     |     |     |     |     | driven | regimes | overlay |     | macroeconomic |     | regimes | and |
| --- | --- | --- | --- | --- | --- | --- | ------ | ------- | ------- | --- | ------------- | --- | ------- | --- |
volatility);
|           |                  |     |        |            |             |       | contribute     |     | to the | overall | complexity | of  | observed | finan- |
| --------- | ---------------- | --- | ------ | ---------- | ----------- | ----- | -------------- | --- | ------ | ------- | ---------- | --- | -------- | ------ |
|           |                  |     |        |            |             |       | cialdynamics[? |     |        | ? ? ].  |            |     |          |        |
| • Concept | evolution        |     | / nenw | classes    | — the       | emer- |                |     |        |         |            |     |          |        |
| gence     | or disappearance |     | of     | previously | nonexistent |       |                |     |        |         |            |     |          |        |
effectively
| target                 | classes, |     |                          | expanding | or redefining |     |     |                          |     |     |     |     |     |     |
| ---------------------- | -------- | --- | ------------------------ | --------- | ------------- | --- | --- | ------------------------ | --- | --- | --- | --- | --- | --- |
|                        |          |     |                          |           |               |     | 3.  | RepresentationandContext |     |     |     |     |     |     |
| theproblem’sontolog y. |          |     | Forinstance,theintroduc- |           |               |     |     |                          |     |     |     |     |     |     |
tionofanewassettclass(suchasexchange-traded
fundsorcryptocurrencyfutures)createsnovelpre- The purpose of this section is to provide the foun-
n
dictiontargetsthatdidnotexistinthetrainingpe- dationsforaddressingthefollowingquestion: howcan
financialtimeseriesberepresented,andhowcaninter-
| riod, | requiring | models | to  | recognize | and | adapt to |     |     |     |     |     |     |     |     |
| ----- | --------- | ------ | --- | --------- | --- | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
entirelynewicategories; nal and external information be integrated, to support
|     |     |     |     |     |     |     | thedetectionandinterpretationofregimechanges? |     |     |     |     |     |     | For |
| --- | --- | --- | --- | --- | --- | --- | --------------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
r
| • Mechanism |            | change | — modifications |      | to               | the un- |                   |          |           |          |     |                    |     |     |
| ----------- | ---------- | ------ | --------------- | ---- | ---------------- | ------- | ----------------- | -------- | --------- | -------- | --- | ------------------ | --- | --- |
|             |            |        |                 |      |                  |         | this,             | we adopt | a layered | approach |     | to representation, |     | il- |
| deprlying   | generative |        | process,        | such | as the introduc- |         | lustratedinFig10. |          |           |          |     |                    |     |     |
tionofnewvariables,rules,ordependencies,even Atthefirstlevel,weconsiderinternalsignalsderived
when observable classes remain unchanged. An fromthetimeseriesitself,correspondingtoendogenous
e
example is the implementation of circuit breakers information. At the second level, we incorporate ex-
| or new | trading | halts | that alter | market | microstruc- |     |     |     |     |     |     |     |     |     |
| ------ | ------- | ----- | ---------- | ------ | ----------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
ogenouscontext,representingexternalinformationthat
r ture,changinghoworderflowtranslatesintoprice influencestheobserveddynamics. Athirdlayerexplic-
movementswithoutnecessarilychangingtheclas- itly models the latent structure of underlying states or
Psificationtargets(e.g.,up/down/neutralpricedirec-
regimesaspartoftherepresentation,enablingaconnec-
| tion). |     |     |     |     |     |     | tionbetweenobserveddataandunobservedmarketcon- |         |     |             |                 |     |     |          |
| ------ | --- | --- | --- | --- | --- | --- | ---------------------------------------------- | ------- | --- | ----------- | --------------- | --- | --- | -------- |
|        |     |     |     |     |     |     | ditions.                                       | Fourth, |     | we consider | representations |     |     | oriented |
9
This preprint research paper has not been peer reviewed. Electronic copy available at: https://ssrn.com/abstract=6170273

d
e
Table2:Summaryofdrifttaxonomicaxeswithfinancialexamples
w
Temporalaxis(how Statisticalaxis(what Spatialaxis Ontologicalaxis Typicalfinancialexample
| andwhen) | changes) |     | (where) | (structure/state) |     |     |     |
| -------- | -------- | --- | ------- | ----------------- | --- | --- | --- |
Abrupt ∆P(Y|X) Global Regimechange(normal→ Marketcrash;jumpinriskpremium
|     |     |     |     | crisis) |     | e   |     |
| --- | --- | --- | --- | ------- | --- | --- | --- |
Abrupt ∆P(Y) Global Samesetofclasses(nonew Suddendowngradeofsovereignor
|        |       |     |       | ontology)       | large-bankcreditrating            |     |     |
| ------ | ----- | --- | ----- | --------------- | --------------------------------- | --- | --- |
|        | ∆P(X) |     |       |                 | Riegulatoryshockinaspecificsector |     |     |
| Abrupt |       |     | Local | Mechanismchange |                                   |     |     |
(regulation/rules)
v
∆P(X)
Gradual Local Samesetofclasses(flows Slowsectorrotation(outofonesectorinto
|     |     |     |     | withintheregime) | another) |     |     |
| --- | --- | --- | --- | ---------------- | -------- | --- | --- |
e
Incremental/ 1st/2ndorderinP(X) Global Macroregimeinsl owdrift Seculardownwardtrendininterestrates
continuous
Recurrent/seasonal P(X)/P(Y)and2ndorder Globalor Recurrentseasonalregimes Januaryeffect;intradayopen/closepatterns
|     |     |     | local | r   |     |     |     |
| --- | --- | --- | ----- | --- | --- | --- | --- |
Gradual ∆P(Y|X) Local Mechanismadjustment Marketlearningtopriceanewassetor
|     |     |     |     | withinthesameregime   | technology |     |     |
| --- | --- | --- | --- | --------------------- | ---------- | --- | --- |
Abrupt 2ndorder(dependence/ Global Contagrionregime(normal Correlationcollapseincrises;lossof
|        | tails)  |     |       | →highdependence)   | diversification                       |     |     |
| ------ | ------- | --- | ----- | ------------------ | ------------------------------------- | --- | --- |
|        | ∆P(X|Y) |     |       | eChangeinselection |                                       |     |     |
| Abrupt |         |     | Local |                    | Newcredit-scoringcriterionchangingthe |     |     |
|        |         |     |       | mechanism          | profileofapprovedclients              |     |     |
Table3:Mappinegdriftcausestotaxonomicaxes
| Cause |     | Temporalaxis | Statisticalaxis | Spatialaxis | Example |     |     |
| ----- | --- | ------------ | --------------- | ----------- | ------- | --- | --- |
p
∆P(Y|X)+∆P(X)
| Monetary-policyshock |     | Abrupt |     | Global | Surpriseinterest-ratehike |     |     |
| -------------------- | --- | ------ | --- | ------ | ------------------------- | --- | --- |
(exogenous)
 ∆P(X),2ndorder,
Liquiditycontagion Gradual Global(systemic) Cascadingmargincalls
| (endogenous) |     |     | multivariate |     |     |     |     |
| ------------ | --- | --- | ------------ | --- | --- | --- | --- |
t
Demographictrend Incremental(long-run) ∆P(Y) Global Populationageing
(country/region)
| (exogenous) |     | o   |     |     |     |     |     |
| ----------- | --- | --- | --- | --- | --- | --- | --- |
Pump-and-dump Blip(transient) ∆P(X),1storder Local Manipulationincryptomarkets
(adversarial)
Bitcoinhalving(exogenous) Recunrrent ∆P(X)+∆P(Y|X) Global(crypto Supply-reductionevents
|     |     | (deterministic) |     | assets) |     |     |     |
| --- | --- | --------------- | --- | ------- | --- | --- | --- |

towardrobustness,emphasizinginvarianceandtransfer- can also be summarized through learned representa-
t
abilityacrossassets,timeperiods,andmarketenviron- tions. Fig. 11 illustrates this idea: each time window
n
| ments. |     |     |     | w isencodedintoalatentvectorz,sothatdriftcanbe |     |     |     |
| ------ | --- | --- | --- | ---------------------------------------------- | --- | --- | --- |
|        |     |     |     | t                                              |     | t   |     |
The goal of these representations is to transform monitored as a change in the trajectory {z} in the em-
t
| raw data | into a i feature space | in which | regime-relevant | beddingspace. |     |     |     |
| -------- | ---------------------- | -------- | --------------- | ------------- | --- | --- | --- |
changes become explicit, whether as drifts in embed- Classical studies in time-series statistics and econo-
r
dings, reorganizations of network structures, or varia- metricsshowthatalargeshareoffinancialdriftsmani-
tions inplatent indicators. Figure 10 provides a com- festsaschangesinfirst-andsecond-orderpropertiesof
pactroadmapofhowweorganizedrift-awarerepresen- theseries(level,trend,volatility,autocorrelation),orin
tationsinthissurvey.
|     |     |     |     | morecomplexformsoftemporaldependence[? |     |     | ? ? ? |
| --- | --- | --- | --- | -------------------------------------- | --- | --- | ----- |
e
|     |     |     |     | ? ]. Thus, | a natural starting | point is to construct | diag- |
| --- | --- | --- | --- | ---------- | ------------------ | --------------------- | ----- |
3.1. InternalSignalsandSeriesEmbeddings nostic features computed in moving time windows (or
rInternal Signals. The most basic layer of representa- multiple time scales) that capture these statistics. Ex-
| tionconsistsoftheinternalsignalscontainedinthetime |     |     |     | amplesinclude: |     |     |     |
| -------------------------------------------------- | --- | --- | --- | -------------- | --- | --- | --- |
P
seriesitself—prices,returns,volumes,spreads,among
others—analyzedthroughthelensofnon-stationarity. • Location and dispersion statistics: moving
Beyondclassicalhandcraftedstatistics, internalsignals means,medians,orquantiles;realizedvolatilityin
10
This preprint research paper has not been peer reviewed. Electronic copy available at: https://ssrn.com/abstract=6170273

d
e
rollingwindows;measuresofskewnessandkurto-
|     |     |     |     |     |     |     | sisofreturns. |     |     |     | w   |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ------------- | --- | --- | --- | --- | --- | --- | --- |
•
|     |     |     |     |     |     |     | Temporal  |     | dependence |                 | measures: |       | autocorre-   |     |
| --- | --- | --- | --- | --- | --- | --- | --------- | --- | ---------- | --------------- | --------- | ----- | ------------ | --- |
|     |     |     |     |     |     |     | lation    | and | partial    | autocorrelation |           |       | coefficients |     |
|     |     |     |     |     |     |     | (ACF/PACF |     | [? ?       | e]) at          | several   | lags; | assessment   |     |
RawData:prices,volumes,spreads,news
oflongmemoryviastatisticssuchaslong-runvari-
anceorunit-roottests(toidentifychangesbetween
InternalSignals •Movingstatistics(mean,var,ACF) stationaryandnoin-stationarytrends).
•Multi-scaledecomposition
|     |                                                       | endogenousfeatures |     |     | •Learnedembeddingszt |     |                          |     |     |     |                         |     |     |     |
| --- | ----------------------------------------------------- | ------------------ | --- | --- | -------------------- | --- | ------------------------ | --- | --- | --- | ----------------------- | --- | --- | --- |
|     | lacigolotno,laitaps,laropmet,lacitsitats:sexaymonoxaT |                    |     |     |                      |     |                          |     | v   |     |                         |     |     |     |
|     |                                                       |                    |     |     |                      |     | • Multi-scaleindicators: |     |     |     | featuresobtainedthrough |     |     |     |
ExogenousContext •Macrovariables(rates,VIX) waveletdecompositionsorlow-/high-passfiltersat
•Microstructure(spread,depth)
|     |     | externalinformation |     |     | •News&sentiment(multimodal) |     |         | e                                       |     |     |     |     |     |     |
| --- | --- | ------------------- | --- | --- | --------------------------- | --- | ------- | --------------------------------------- | --- | --- | --- | --- | --- | --- |
|     |     |                     |     |     |                             |     | differe | nthorizons,toseparateshort-,medium-,and |     |     |     |     |     |     |
long-termmovements[????].Forexample,dif-
•RegimeprobabilitiesP(St)
|     |     | LatentStructure |     |     | •Dynamicgraphs(correlations) |     |     |     |     |     |     |     |     |     |
| --- | --- | --------------- | --- | --- | ---------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
states&relationships ferencesinmeansacrossscales(detectionoftrend
|     |     |     |     |     | •Changepointposteriors |     |     | r   |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | ---------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
changes)orenergymetricsinspecificfrequencies
( detectionofemerging/vanishingcycles).
|     |     | Robustness&Invariance |     |     | •Causal/invariantfeatures |     |     |     |     |     |     |     |     |     |
| --- | --- | --------------------- | --- | --- | ------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
•Foundationmodelembeddings
|     |     | stablefeatures |     |     | •Cross-regimestability |     |                 |          |              |     |            |          |          |     |
| --- | --- | -------------- | --- | --- | ---------------------- | --- | --------------- | -------- | ------------ | --- | ---------- | -------- | -------- | --- |
|     |     |                |     |     |                        |     | rThese          | features | provide      | an  | aggregated |          | view of  | how |
|     |     |                |     |     |                        |     | the statistical |          | axis evolves |     | when       | computed | continu- |     |
e
Drift-awarerepresentation→Detection(Section4)/Adaptation(Section5)
|           |                                                      |     |     |     |     |     | ously in      | sliding | windows.         | For         | example,     | one        | can          | mon- |
| --------- | ---------------------------------------------------- | --- | --- | --- | --- | --- | ------------- | ------- | ---------------- | ----------- | ------------ | ---------- | ------------ | ---- |
|           |                                                      |     |     |     |     |     | itor whether  |         | the mean         | or variance |              | of returns | exhibits     |      |
| Figure10: | Representationlayersfordrift-awarefinancialmodeling. |     |     |     |     |     |               |         |                  |             |              |            |              |      |
|           |                                                      |     |     |     |     |     | a significant |         | drift indicating |             | a transition | in         | the volatil- |      |
Rawdataisprogressivelytransformedthroughinternalsignalexterac-
tion, exogenous context integration, latent structure modeling, and ity regime [? ? ? ]; track changes in the correla-
robustness-orientedfeatures,producingrepresentationsthatfeedde- tion between an asset and an important risk factor [?
| tectionandadaptationsystems. |     |     |     |     |     | p?  |          |           |               |       |            |           |                |      |
| ---------------------------- | --- | --- | --- | --- | --- | --- | -------- | --------- | ------------- | ----- | ---------- | --------- | -------------- | ---- |
|                              |     |     |     |     |     |     | ? ];     | or detect | instabilities |       | in the     | estimated | param-         |      |
|                              |     |     |     |     |     |     | eters of | a local   | model         | (such | as changes |           | in the coeffi- |      |
|                              |     |     |     |     |     |     | cients   | of a CAPM | calibrated    |       | in rolling | windows)  |                | [? ? |

|     |     |     |     |     |     |     | ]. Indeed,                                         | many     | change-detection |        | approaches |            | in        | finan- |
| --- | --- | --- | --- | --- | --- | --- | -------------------------------------------------- | -------- | ---------------- | ------ | ---------- | ---------- | --------- | ------ |
|     |     |     |     |     | t   |     | cialtimeseriesrelyonmonitoringsuchstatisticsinreal |          |                  |        |            |            |           |        |
|     |     |     |     | o   |     |     | time.                                              | However, | as the           | number | of         | series and | variables |        |
increases—suchaswhenconsideringmultipleassetssi-
multaneouslyormultiplefrequencies(e.g.,dailyandin-
n
|     |     |     |     |     |     |     | traday)—relying |     | solely | on pre-defined, |     | manually |     | engi- |
| --- | --- | --- | --- | --- | --- | --- | --------------- | --- | ------ | --------------- | --- | -------- | --- | ----- |
neeredfeaturesquicklybecomesinfeasible.
|     |     |     |     |     |     |     | Series | Embeddings. | In  | this | context, | the | concept-drift |     |
| --- | --- | --- | --- | --- | --- | --- | ------ | ----------- | --- | ---- | -------- | --- | ------------- | --- |
EmbeddingSpace
TimeSeries z(2) (broad sense) literature for data streams, together with
|     | xt  |     | t   |     |     |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Bull
|     |     |     |     | z2  |     |     | advances | in deep | learning, | suggests |     | the need | to  | learn |
| --- | --- | --- | --- | --- | --- | --- | -------- | ------- | --------- | -------- | --- | -------- | --- | ----- |
n
|     |     |     |     | z1  |     |     | representations |     | automatically, |     | rather | than | manually |     |
| --- | --- | --- | --- | --- | --- | --- | --------------- | --- | -------------- | --- | ------ | ---- | -------- | --- |
drift
|     |     |     | encode |     | z3  |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | ------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
specifyingallrelevantstatistics.Theobjectiveistotrain
|     |     | i   |     |     | z4  | z5  | a parametric |     | function | f that | maps | sequences | or  | time |
| --- | --- | --- | --- | --- | --- | --- | ------------ | --- | -------- | ------ | ---- | --------- | --- | ---- |
θ
|     |          | t      |     |     | Bear |      | windows | to dense | vectors | z   | ∈ Rd | (i.e., temporal |     | em- |
| --- | -------- | ------ | --- | --- | ---- | ---- | ------- | -------- | ------- | --- | ---- | --------------- | --- | --- |
|     | w1 w2 w3 | rw4 w5 |     |     |      | z(1) |         |          |         | t   |      |                 |     |     |
fθ:wt(cid:55)→zt beddings), such that periods exhibiting similar behav-
|     | p   |     |     |     |     |     | ior are | mapped | to nearby | regions | in  | latent | space | [? ? |
| --- | --- | --- | --- | --- | --- | --- | ------- | ------ | --------- | ------- | --- | ------ | ----- | ---- |
Figure11: Learnedembeddingsfordriftdetection. Timewindows ? ? ]. This idea—learning embeddings that represent
| wt  | areencodedintolatentvectorszt |     |     | ∈ Rd. Similarmarketcondi- |     |     |            |       |        |            |     |        |              |     |
| --- | ----------------------------- | --- | --- | ------------------------- | --- | --- | ---------- | ----- | ------ | ---------- | --- | ------ | ------------ | --- |
|     |                               |     |     |                           |     |     | the latent | state | of the | series—has |     | become | particularly |     |
tioensclustertogether(bullvs.bearregimes),whiledriftmanifestsas
|                                            |     |     |     |     |                |     | prominent | in  | non-stationary |     | settings, | as learned |     | repre- |
| ------------------------------------------ | --- | --- | --- | --- | -------------- | --- | --------- | --- | -------------- | --- | --------- | ---------- | --- | ------ |
| trajectorymovementacrosstheembeddingspace. |     |     |     |     | Changepointde- |     |           |     |                |     |           |            |     |        |
effective
tectioncanbeapplieddirectlytothesequence{zt }. sentations are often more at capturing com-
| r   |     |     |     |     |     |     | plex drift | patterns | than | hand-crafted |     | indicators |     | [? ? |
| --- | --- | --- | --- | --- | --- | --- | ---------- | -------- | ---- | ------------ | --- | ---------- | --- | ---- |
]. Table4summarizesthemaindrift-awarerepresenta-
P
tionoptionsdiscussedinthissection,providingastruc-
|     |     |     |     |     |     |     | tured overview |     | before | we examine |     | specific | approaches |     |
| --- | --- | --- | --- | --- | --- | --- | -------------- | --- | ------ | ---------- | --- | -------- | ---------- | --- |
inmoredetail.
11
This preprint research paper has not been peer reviewed. Electronic copy available at: https://ssrn.com/abstract=6170273

d
e
As an example, the TS2Vec approach proposed by tiple horizons, wavelet decompositions, or specialized
Yue et al. [? ] uses hierarchical contrastive learning layersforcapturingdistinctfrwequenciesincreasesensi-
to produce embeddings that are robust across multiple tivity to drifts at various scales [? ? ? ? ? ? ? ?
temporal resolutions. Essentially, the model is trained ]. Rather than deciding in advance on a single “cor-
togenerateconsistentrepresentationsz forsimilarsub- rect” scale, these architectures internalize multiple fre-
t
e
sequences,whileseparatingsequenceswithdistinctpat- quenciesintherepresentation. Thisconnectsdirectlyto
terns. Thus,locallysimilarwindowsremaincloseinla- thetemporal/morphologicalaxisofthetaxonomy(Sec-
tentspace,whereaswindowscorrespondingtodifferent tion2): bysimultaneouslyconsideringlong-andshort-
i
behavior patterns (e.g., bull vs. bear markets, low vs. termcomponents,wecandetectbothgraduallong-term
v
highvolatilityperiods)aremappedtodistantregionsof changesandseasonalorabruptshort-termshifts. Stud-
the embedding space. Studies report that such learned iesinhigh-frequencymarketsshowthatignoringsimul-
e
embeddingsareusefulnotonlyforchangedetectionbut taneousscales—forexample,analyzingonlythemacro
alsoforpredictivetasksandanomalydetectionintime trend and ignoring daily/intraday cycles — can lead to
series. distortedassessmentsofvolatilityandregimeidentifica-
r
Inthecontextofdriftdetection,operatinginthelatent tion[? ? ? ]. Multi-scaleembeddingsthereforetendto
spacez hasanadvantage: classicalchangepointmeth- provid erobustnessinthedetectionofcomplexchanges.
t
ods can be applied directly to the embedding series[?
r
? ]. Techniques such as CUSUM [? ? ], PELT [? ], 3.2. Exogenous Context, Multimodality, and Market
or non-parametric (kernel) tests [? ? ? ] can be run eStructure
on sequences of vectors z instead of on the raw data. MacroeconomicandExogenousContext. Thesecond
t
Since these embeddings are trained to condense high- representation layer concerns the exogenous context
e
dimensional relevant information (including nonlinear that influences financial regimes. As discussed in Sec-
dynamics)intoafewcomponents,asignificantchange tion2.5,manydriftsoriginateinmacroeconomicshocks
inseriesbehaviortendstomanifestasadetectapbleshift and cycles, monetary-policy decisions, liquidity crises,
intheembeddings. Inshort, thelearnedrepresentation or geopolitical events [? ? ? ? ? ]. Ignoring these
“pre-processes”thedatasothatrelevantchangesareal- contextual dimensions can lead to myopic representa-
readyhighlighted,facilitatingthedetection stage. tionsthattreattheseriesasanisolatedsystemwhen,in
A recent line of research goes furthertand explores reality,itrespondstoexternalfactors.
trainingobjectivesorientedspecificallytowardanoma- A fundamental strategy is to incorporate macroeco-
o
liesanddrifts. Forexample,contrastivelearningmeth- nomicandaggregatefinancialvariablesascovariatesin
odsthatinjectsyntheticanomaliesorperturbationsdur- the representation model. For example, one might in-
ing training, following a philnosophy similar to expos- cludeseriessuchasshort-andlong-terminterestrates,
ing deep networks to outliers [? ]. Here, embeddings inflationindices,activityindicators,creditspreads,risk-
are trained to maximize separation between “normal” aversionmetrics(VIX,etc.),aswellasestablishedrisk
and “altered” patterns. Su ch approaches include new- factors (value, momentum, size, etc.) [? ? ? ? ?
class detection methodstin data streams [? ? ] and ]. Thesecontextualvariablescanbeintegratedintothe
self-supervised techniques like the CARLA model for
representationsystemindifferentways:
n
timeseries,whichusescontrastiveobjectivescalibrated 1. Direct feature fusion: includes contextual vari-
to highlight temporal anomalies [? ]. The result is to ables as additional attributes concatenated to the
bring the represeintation stage closer to the final detec- internalfeaturesoftheseriesineachtimewindow.
tiontask:onerconstructsalatentspacedesignedtomake That is, the input to the representation model in-
breaks,noveltyevents,andout-of-distributionobserva- cludes not only attributes derived from the target
tionsmporeevident[? ? ? ? ]. Inotherwords, instead series,butalsothecorrespondingvaluesofmacro
ofgenericembeddings, one trainsembeddingsthatare indicatorsinthatinterval.
explicitlysensitivetodrift. 2. State models with exogenous drivers: in latent-
e
Another important consideration is to embed the in- regime models (such as HMMs5 or MS-VAR 6),
trinsicmulti-scaletemporalstructureofthedataintothe
rrepresentation[? ? ]. Differentchangesmanifestatdif- 5AHiddenMarkovModel(HMM)assumesalatentregime/state
ferent time scales — for example, a secular trend ver- processStthatevolvesasaMarkovchain,whileobservationsYtare
P generated conditionally on the current state (via emission distribu-
sus intraday cycles — and choosing a single analysis
tions).Inferencetypicallyreliesonforward–backwardrecursionsand
scale a priori can lead to blind spots for certain types EM/Baum–Welch-typeestimation[???].
of change [? ? ]. Models that integrate filters at mul- 6AMarkov-SwitchingVectorAutoregression(MS-VAR)isaVAR
12
This preprint research paper has not been peer reviewed. Electronic copy available at: https://ssrn.com/abstract=6170273

d
e
w
Table4:Comparisonofembeddingmethodsfordrift-awarefinancialtime-seriesrepresentation.
Method LearningType Real-time Interpretability Advantages Limitations
e
Manual Statistical None (hand- Yes High(domainstatis- Transparent; com- Requires feature
Features [? ? ? ? crafted) tics) putationally light; engineering;limited
|     | ?]  |     |     |     | domain | knowledge | tolinear/simplepat- |     |
| --- | --- | --- | --- | --- | ------ | --------- | ------------------- | --- |
i
|     |     |     |     |     | integration |     | terns;           | doesn’t scale |
| --- | --- | --- | --- | --- | ----------- | --- | ---------------- | ------------- |
|     |     |     |     |     | v           |     | tohighdimensions |               |
TS2Vec[?] Self-supervised Yes (after Low(black-box) Multi-resolution Requires pre-
erobust
|     |     | (contrastive) | training) |     |          | embeddings;    | training;         | limited |
| --- | --- | ------------- | --------- | --- | -------- | -------------- | ----------------- | ------- |
|     |     |               |           |     | no       | labels needed; | interpretability; |         |
|     |     |               |           |     | captures | complex        | sensitive         | to aug- |
|     |     |               |           | r   | patterns |                | mentationdesign   |         |
Drift-Oriented Self-supervised Yes (after Low–Medium Explicitly sensitive Requires careful
Embeddings (anomaly con- training) to drifts; synthetic anomaly design;
r
|     | (CARLA)[?] | trastive) |     |           | anomaly | injection; | may       | overfit to |
| --- | ---------- | --------- | --- | --------- | ------- | ---------- | --------- | ---------- |
|     |            |           |     | etailored |         | for detec- | injected  | patterns;  |
|     |            |           |     |           | tion    |            | black-box |            |
Regime-Switching Unsupervised Yes (online High (discrete Probabilisticregime Assumes discrete
|     | (HMM/MS-VAR) |     | e   |     |     |     |     |     |
| --- | ------------ | --- | --- | --- | --- | --- | --- | --- |
(EM) filtering) regimes) states; interpretable states; parametric
|     | [????] |     |     |     | transitions;       | inte- | assumptions;     | model |
| --- | ------ | --- | --- | --- | ------------------ | ----- | ---------------- | ----- |
|     |        |     |     |     | gratesmacrodrivers |       | misspecification |       |
p
risk
Bayesian On- Unsupervised Yes (on- High (run-length Real-time change- Computational
line Changepoint (Bayesian) line ) posterior) point probabilities; complexity; para-
|     | (BOCPD)[? | ? ? ? |     |     | uncertaintyquantifi- |     | metric | likelihood |
| --- | --------- | ----- | --- | --- | -------------------- | --- | ------ | ---------- |
t
|     | ??] |     |     |     | cation;   | principled | assumptions; | tuning |
| --- | --- | --- | --- | --- | --------- | ---------- | ------------ | ------ |
|     |     |     | o   |     | inference |            | priors       |        |
Multimodal(Series Supervised / Yes (after Medium (attention Early signals from Alignment com-
+Text)[???]
Self-supervised n training) maps) news; rich context; plexity; requires
|     |     |     |     |     | captures | narrative | textualdata;    | modal- |
| --- | --- | --- | --- | --- | -------- | --------- | --------------- | ------ |
|     |     |     |     |     | drivers  |           | ityfusiondesign |        |
GraphNeuralNet- Supe rvised / Yes (after Medium (graph Systemic view; Graph construction
works (GNN) [? ? Stelf-supervised training) structure) captures cross-asset choice; scalability
|     | ?]  |     |     |     | dependencies; | net- | to large | networks; |
| --- | --- | --- | --- | --- | ------------- | ---- | -------- | --------- |
n
|     |     |     |     |     | work      | reorganization | dynamic  | edge com- |
| --- | --- | --- | --- | --- | --------- | -------------- | -------- | --------- |
|     |     |     |     |     | detection |                | putation |           |
Foundation Miod- Self-supervised Yes (infer- Low(black-box) Generalization;data Domain gap; adap-
els (Pre-trairned) [? (transfer) ence) efficiency; lever- tation needed;
|     | ?]  |     |     |     | ages      | cross-domain | updatemechanisms;    |     |
| --- | --- | --- | --- | --- | --------- | ------------ | -------------------- | --- |
|     | p   |     |     |     | patterns; | minimal      | interpretabilityloss |     |
training
Invariant/Causal Supervised Yes (after High (causal struc- Robustness to dis- Requires environ-
e
Features[? ? ? ? ? (IRM) training) ture) tribution shifts; ment annotations;
|     | ?]  |     |     |     | focuses      | on sta-        | assumptions  | on     |
| --- | --- | --- | --- | --- | ------------ | -------------- | ------------ | ------ |
|     | r   |     |     |     | ble          | relationships; | causal       | graph; |
|     |     |     |     |     | reduces      | spurious       | optimization | com-   |
| P   |     |     |     |     | correlations |                | plexity      |        |
13
This preprint research paper has not been peer reviewed. Electronic copy available at: https://ssrn.com/abstract=6170273

d
e
•
macro variables can act as drivers that modulate Impact and resilience metrics: how much the
transition dynamics between regimes. For exam- price moves after a larwge order (price impact)
ple,interest-rateorinflationdynamicscanbeused andhowquicklythemarketrecovers(liquidityre-
| asexplanatoryvariablesinthetransitionprobabil- |        |           |       |          |                   |             | silience); |          |             |        |               |          |          |
| ---------------------------------------------- | ------ | --------- | ----- | -------- | ----------------- | ----------- | ---------- | -------- | ----------- | ------ | ------------- | -------- | -------- |
| ities                                          | of a   | Markovian | model | [?       | ? ? ?             | ]. This ap- |            |          |             |        |               |          |          |
|                                                |        |           |       |          |                   |             | Together,  | these    | indicaetors | make   | it            | possible | to iden- |
| proach                                         | embeds | context   |       | into the | very state-change |             |            |          |             |        |               |          |          |
|                                                |        |           |       |          |                   |             | tify early | signs of | liquidity   | stress | or structural |          | changes  |
process,increasinginterpretability(regimescanbe
associated with certain macro levels) and poten- inmarketfunctioning. Empiricalstudiesshowthatsuch
i
microstructureindicatorscananticipateveryshort-term
tiallyimprovingthedetectionoftransitions.
v
Jointmultimodalembeddings: drifts related to phenomena such as flight-to-liquidity,
| 3.  |     |     |     |     | indeeparchitec- |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --------------- | --- | --- | --- | --- | --- | --- | --- | --- |
liquiditycrunches,orlocalizedstressphasesinspecific
| tures,       | one | can train | a network |         | to learn | joint rep-  |           |              |         |       |         |               |      |
| ------------ | --- | --------- | --------- | ------- | -------- | ----------- | --------- | ------------ | ------- | ----- | ------- | ------------- | ---- |
|              |     |           |           |         |          |             | markets   | [?e? ?       | ]. That | is,   | before  | a broader     | risk |
| resentations |     | that      | combine   | prices  | with     | macro indi- |           |              |         |       |         |               |      |
|              |     |           |           |         |          |             | regime is | established, | we      | often | observe | deterioration |      |
| cators       | and | other     | factors.  | In this | case,    | rather than |           |              |         |       |         |               |      |
inmicrostructureindicators(e.g.,wideningspreads,re-
| simply | concatenating |     | series, | it  | is common | to em- |     |     |     |     |     |     |     |
| ------ | ------------- | --- | ------- | --- | --------- | ------ | --- | --- | --- | --- | --- | --- | --- |
r
ploy sub-networks or cross-attention mechanisms duceddepth)thatsignalalossofliquidity. Incorporat-
ingth esesignalsintotherepresentationmakesitreflect
| that | integrate | the | modalities. |     | The network | then |     |     |     |     |     |     |     |
| ---- | --------- | --- | ----------- | --- | ----------- | ---- | --- | --- | --- | --- | --- | --- | --- |
thecurrentstateofmicrostructure,whichoftenprecedes
producesaunifiedembeddingthatsimultaneously
broaderchangesinprice/riskregimes.Incontrast,arep- r
encodesthebehaviorofthefinancialseriesandits
eresentationbasedsolelyonaggregatedpricesmayfailto
| associatedmacroeconomiccontext[? |     |     |     |     | ?   | ].  |     |     |     |     |     |     |     |
| -------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
capturethesesubtlestructuralchanges.
Studieswithregime-switchingandMS-VARmodels
|            |         |      |       |       |         | eMultimodalContextandTextualInformation. |     |     |     |     |     |     | Inad- |
| ---------- | ------- | ---- | ----- | ----- | ------- | ---------------------------------------- | --- | --- | --- | --- | --- | --- | ----- |
| in finance | suggest | that | using | macro | factors | as part of                               |     |     |     |     |     |     |       |
dition,animportantaspectisthemultimodalityofinfor-
thelatentstateimprovesregimeseparationandtheeco-
|                                   |       |        |      |      |                  |        | mation.        | Financial  | series | rarely | exist          | “alone”: | markets |
| --------------------------------- | ----- | ------ | ---- | ---- | ---------------- | ------ | -------------- | ---------- | ------ | ------ | -------------- | -------- | ------- |
| nomicinterpretationoftransitions. |       |        |      |      | Forexample,atwo- | p      |                |            |        |        |                |          |         |
|                                   |       |        |      |      |                  |        | are constantly | influenced |        | and    | contextualized |          | by tex- |
| regime                            | model | can be | much | more | interpretable    | if one |                |            |        |        |                |          |         |
tualinformation—newspaperarticles,analystreports,
| regime is | associated |     | with “high | inflation, | rising | rates” |     |     |     |     |     |     |     |
| --------- | ---------- | --- | ---------- | ---------- | ------ | ------ | --- | --- | --- | --- | --- | --- | --- |
social-mediaposts,corporateandregulatoryannounce-
| andtheotherwith“lowinflation, |     |     |     | stablerat es”. |     | Repre- |              |         |      |            |     |        |        |
| ----------------------------- | --- | --- | --- | -------------- | --- | ------ | ------------ | ------- | ---- | ---------- | --- | ------ | ------ |
|                               |     |     |     |                |     |        | ments, among | others. | Many | disruptive |     | events | appear |
sentingthiscontextinthemodelstatehelpsavoidspu-
t
|     |     |     |     |     |     |     | first as news | or narratives |     | before | being | fully | reflected |
| --- | --- | --- | --- | --- | --- | --- | ------------- | ------------- | --- | ------ | ----- | ----- | --------- |
riousorpracticallymeaninglessregimedetections.
|     |     |     |     | o   |     |     | in prices. | This motivates |     | a class | of multimodal |     | repre- |
| --- | --- | --- | --- | --- | --- | --- | ---------- | -------------- | --- | ------- | ------------- | --- | ------ |
sentationsthatcombinenumericaltime-seriesdatawith
| Market  | Microstructure |          | Context.      |     | The same | principle |                 |      |          |       |             |     |         |
| ------- | -------------- | -------- | ------------- | --- | -------- | --------- | --------------- | ---- | -------- | ----- | ----------- | --- | ------- |
|         |                |          |               |     |          |           | textual sources | (and | possibly | other | modalities, |     | such as |
| applies | at finer       | temporal | resnolutions, |     | where    | the rele- |                 |      |          |       |             |     |         |
chartimages,sentimentdata,etc.).
vantcontextisnolongermacroeconomicbutstructural.
|                   |        |                          |         |        |          |              | Figure         | 12 provides | an  | overview  | of  | the       | main mul- |
| ----------------- | ------ | ------------------------ | ------- | ------ | -------- | ------------ | -------------- | ----------- | --- | --------- | --- | --------- | --------- |
| At high-frequency |        | time                     | scales, | market | dynamics | are          |                |             |     |           |     |           |           |
|                   |        |                          |         |        |          |              | timodal fusion | strategies, |     | organized |     | according | to the    |
| strongly          | shaped | by market microstructure |         |        |          | effects. In- |                |             |     |           |     |           |           |
stageatwhichinformationfromdifferentsourcesisin-
| traday behavior |          | exhibitstsystematic |            |          | patterns | (opening, |                |            |           |           |             |           |          |
| --------------- | -------- | ------------------- | ---------- | -------- | -------- | --------- | -------------- | ---------- | --------- | --------- | ----------- | --------- | -------- |
|                 |          |                     |            |          |          |           | tegrated       | within the | modeling  | pipeline. |             | Depending | on       |
| midday,         | closing, | and                 | auction    | periods) | as well  | as dis-   |                |            |           |           |             |           |          |
|                 |          | n                   |            |          |          |           | how modalities | are        | combined, |           | integration | can       | occur at |
| tinct liquidity |          | regimes             | throughout | the      | trading  | day. As   |                |            |           |           |             |           |          |
differentprocessingstages:
| a result, | representations |          | designed | for | drift              | and regime |              |     |                                |     |     |     |     |
| --------- | --------------- | -------- | -------- | --- | ------------------ | ---------- | ------------ | --- | ------------------------------ | --- | --- | --- | --- |
| detection | at thesie       | horizons | benefit  |     | from incorporating |            | •            |     |                                |     |     |     |     |
|           |                 |          |          |     |                    |            | Earlyfusion: |     | combinenumericalandtextualrep- |     |     |     |     |
microstructurre-relatedinformation,suchas:
|               |     |                                   |     |     |     |     | resentations | at            | the        | outset, | for example, |      | by con- |
| ------------- | --- | --------------------------------- | --- | --- | --- | --- | ------------ | ------------- | ---------- | ------- | ------------ | ---- | ------- |
|               |     |                                   |     |     |     |     | catenating   | series        | embeddings |         | with         | news | embed-  |
| • Orpderflow: |     | metricsofaggressivenessvs.passiv- |     |     |     |     |              |               |            |         |              |      |         |
|               |     |                                   |     |     |     |     | dings        | corresponding |            | to the  | same         | time | window. |
ityoforders;buy/sellimbalanceintheorderbook;
|     |     |     |     |     |     |     | Each | time window |     | is then | represented |     | by a joint |
| --- | --- | --- | --- | --- | --- | --- | ---- | ----------- | --- | ------- | ----------- | --- | ---------- |
[series+text]vector.
e•
| Order-book                               |     | indicators: |     | bid–ask | spreads, | depth |                                            |     |                              |     |     |     |           |
| ---------------------------------------- | --- | ----------- | --- | ------- | -------- | ----- | ------------------------------------------ | --- | ---------------------------- | --- | --- | --- | --------- |
| (volume)availableoneachside,bookchanges; |     |             |     |         |          |       | •                                          |     |                              |     |     |     |           |
|                                          |     |             |     |         |          |       | Intermediatefusion(cross-attention):       |     |                              |     |     |     | usecross- |
| r                                        |     |             |     |         |          |       | attentionmechanismsbetweentimesequencesand |     |                              |     |     |     |           |
|                                          |     |             |     |         |          |       | textsequences.                             |     | Forexample,atransformermodel |     |     |     |           |
Pmodelwhoseparameters(e.g.,intercept,autoregressivematrices,and
|                                              |     |     |     |     |     |             | in which | relevant | news | influence |     | — via | attention |
| -------------------------------------------- | --- | --- | --- | --- | --- | ----------- | -------- | -------- | ---- | --------- | --- | ----- | --------- |
| oftenshockcovariance)dependonalatentregimeSt |     |     |     |     |     | governedbya |          |          |      |           |     |       |           |
—thelearnedrepresentationofmarketdataatthat
| Markovchain, | allowingthemultivariatedynamicstoswitchacross |     |     |     |     |     |     |     |     |     |     |     |     |
| ------------ | --------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
regimes(e.g.,lowvs.highvolatility)[???]. time. Thisallowsthefinalseriesrepresentationto
14
This preprint research paper has not been peer reviewed. Electronic copy available at: https://ssrn.com/abstract=6170273

d
e
bemodulatedbytextualcontent,amplifyingorat- important to account for the structure of interrelation-
tenuatingmovementsaccordingtothepresenceof ships in the market as a dynawmic graph. In multivari-
explanatorynews. ate settings, drifts rarely affect a single asset in isola-
tion—typically,thereisareorganizationofdependen-
• Late fusion: combine only at the end the out-
cies among assets. For example, in a given regime,
puts or alerts originating from detectors special- e
economic sectors form clusters with high intra-cluster
izedineachmodality. Inthiscase,onecouldhave
correlations and lower inter-cluster correlations; dur-
a change detector operating on series and another
ing crisis periods, correlations across most asset pairs
i
analyzing news, and then merge detections (e.g.,
tend to rise simultaneously and may approach unity,
v
flagachangeonlyifbothagree,orusetextascon-
signaling a collapse of diversification and strong sys-
firmation that a quantitative signal corresponds to
temic contagion. Likewise, measures of tail depen-
arealevent). e
dence can change, revealing new channels of extreme
co-movement[? ? ? ? ? ]. Representingeachseriesin-
dividually ignores this cross-information, whereas rep-
EarlyFusion Intermediate LateFusion r
(cross-attention) resenting the system as an evolving graph allows us to
Series Text
xt dt Series Text Series Text captu reco-movementregimes.
xt dt xt dt
Concat Series Text Series Text r
Encoder Encoder Encoder Encoder NormalMarket CrisisMarket
Joint
Encoder Cross-Attention Detector Detector eTech Finance Highcorrelation
zt zt Merge
Alert e
crisis
Figure12:Multimodalfusionstrategiesforintegratingtimeseriesand
textualdata. Earlyfusion: inputsconcatenatedbeforejointencod-
p
ing. Intermediatefusion: separateencoderswithcross-attentionto
exchangeinformation.Latefusion:independentprocessingpipelines
mergedatthedecisionlevel.
Energy Consumer
Sparse,clustered Dense,correlated
These fusion strategies are not meretly conceptual;
Figure13: Dynamiccorrelationnetworks. Normalmarket: stocks
theyareincreasinglyadoptedinrecentresearchonmul-
o clusterbysectorwithsparseinter-sectorconnections.Crisismarket:
timodaltime-seriesanalysisandLargeLanguageMod-
correlationsincreasedramaticallyacrossallsectors(correlationcol-
els(LLMs). Inparticular,studiesonapplyingLLMsto lapse),withdenseinterconnectionreplacingthecommunitystructure.
time series highlight architectnures that perform tempo- Thisregimechangeiscapturedbytime-varyinggraphrepresentations.
ral alignment and information fusion across numerical
series, text, and other sources [? ? ? ]. From the per- ThisintuitionisillustratedinFigure13,contrastinga
spective of regime detectio n, the key advantage is that sector-clusteredcorrelationstructureinnormalperiods
eventsdescribedprimaritlyintext(e.g.,politicalorregu- with the dense, near-uniform dependence typically ob-
latorynewsthatanticipatesamarketshift)caninfluence servedduringcrisisepisodes. Insuchagraph,wetypi-
n
thejointrepresentationbeforethecorrespondingmove- callydefinenodesrepresentingfinancialentities(assets,
mentisfullyreflectedinprices[? ? ? ]. indices, sectors, or countries) and weighted edges en-
As a result, diistances in multimodal space thus cap- codingsomestatisticaloreconomicrelationshipamong
turethecombrinedeffectsofnumericalandnarrativesig- them. Edgesmayreflect,forexample,estimatedcorre-
nals:twoperiodswillonlybeconsideredsimilarifboth lationsorco-movements,measuresofnonlineardepen-
thequa p ntitativepatternsandthenewscontextaresimi- dence (tail copulas), exposure–credit relationships be-
lar.Thisenrichmentcanreducefalsenegatives(missing tweeninstitutions,orcapitalflowsacrossmarkets.Edge
a change because the model did not “understand” that weights vary over time, and regime changes appear as
e
thenewsimpliedanewregime)andalsofalsepositives abrupt or gradual reconfigurations in network topol-
(distinguishing price drops caused by concrete events ogy/weights. Examples include: during a financial-
rfromthoseduetonoise,viathepresenceorabsenceof contagion event, sector clusters may dissolve and all
textualexplanations)[? ? ? ? ]. nodes become highly interconnected; in subtler tran-
P
sitions, a new systemic hub may emerge (an asset or
Market Structure and Inter-Asset Dependencies. Be- sector that starts to leaddynamics), or some links may
yond individual series and external signals, it is also weaken while others strengthen, reshaping the correla-
15
This preprint research paper has not been peer reviewed. Electronic copy available at: https://ssrn.com/abstract=6170273

d
e
tionnetwork. suchasthepredictedprobabilityofremaininginthecur-
The recent literature on Graph Neural Networks rentregimeortheexpectedregimeduration. w
(GNNs) for time series provides a framework for In this sense, latent regime probabilities provide a
learningembeddingsthatencodesuchcomplexspatio- compactandinterpretablesummaryofthesystemstate,
temporal dependencies [? ? ]. Essentially, dynamic- integrating information from multiple variables into a
e
graph models can learn both a representation for each small set of indicators. Figure 14 illustrates this idea:
node (asset) and a representation for the graph as a regime transitions appear as crossovers in the filtered
| wholeateachtimeinterval. |     |     | Thesenetworkembeddings |     |     |     |             |        |          |               |         |      |     |
| ------------------------ | --- | --- | ---------------------- | --- | --- | --- | ----------- | ------ | -------- | ------------- | ------- | ---- | --- |
|                          |     |     |                        |     |     |     | probability | paths, | yielding | i drift-aware | signals | that | are |
capturethecurrentstateofthefinancialstructure—for suitableforbothdetectionandadaptation.
v
| example, they     | may | encode    | that there | are     | currently | two    |     |     |     |     |     |     |     |
| ----------------- | --- | --------- | ---------- | ------- | --------- | ------ | --- | --- | --- | --- | --- | --- | --- |
| weakly correlated |     | clusters, | or that    | a given | asset     | is ab- |     | xt  |     |     |     |     |     |
e
normallyconnectedtoothers,indicatingstress. Regime Bull Crisis Bear Recovery
changesthenmanifestaschangesintheseembeddings:
|     |     |     |     |     |     |     | Observed |     | 1τ  | 2τ  | 3τ  |     |     |
| --- | --- | --- | --- | --- | --- | --- | -------- | --- | --- | --- | --- | --- | --- |
Series
| a shift indicating |     | that the | graph topology |     | has changed |     |     |     |     |     |     |     |     |
| ------------------ | --- | -------- | -------------- | --- | ----------- | --- | --- | --- | --- | --- | --- | --- | --- |
r
significantly.
t
P(St)
| Recent   | financial          | models | combine | this | graph-based |     |     |   1    |     |     |     |     |     |
| -------- | ------------------ | ------ | ------- | ---- | ----------- | --- | --- | ------ | --- | --- | --- | --- | --- |
| approach | with multimodality |        | (prices | +    | indicators  | +   |     | Regime |     |     |     |     |     |
Probabilities r
| news), producing  |     | unified      | representations |      | that account |     |     |     |     |     |     |     |     |
| ----------------- | --- | ------------ | --------------- | ---- | ------------ | --- | --- | --- | --- | --- | --- | --- | --- |
|                   |     |              |                 |      |              |     | e   |     |     |     |     |     | t   |
| for relationships |     | among assets | together        | with | economic     |     |     | 0   |     |     |     |     |     |
P(Bull)
context [? ]. In practice, node and graph embeddings P(Crisis)
P(Bear)
| can serve | directly | as inputs | to change | detectors |     | (Sec- |     |     |     |     |     |     |     |
| --------- | -------- | --------- | --------- | --------- | --- | ----- | --- | --- | --- | --- | --- | --- | --- |
e
tion4)—forexample,bymonitoringthetimeseriesof Figure 14: Regime probabilities from a latent-state model (e.g.,
thegraphembeddingtodetectbreaksinthecorrelation HMM).Top: observedserieswithregime-coloredbackground. Bot-
|     |     |     |     |     |     |     | tom: | filteredprobabilitiesP(St |     | | x1:t)foreachregime. |     | Transitions |     |
| --- | --- | --- | --- | --- | --- | --- | ---- | ------------------------- | --- | --------------------- | --- | ----------- | --- |
network — or as additional context for regime-based pmanifestasprobabilitycrossoversatchangepointsτ1,τ2,τ3. These
adaptation mechanisms (Section 5), guiding models to probabilities serve as drift-aware features for detection and adapta-
| treatgroupsofaffectedassetsjointly[? |     |     |     |     |         |        | tion. |     |     |     |     |     |     |
| ------------------------------------ | --- | --- | --- | --- | ------- | ------ | ----- | --- | --- | --- | --- | --- | --- |
|                                      |     |     |     | ?   | ? ? ? ? | ? ? ]. |       |     |     |     |     |     |     |

|                      |     |          |        |            |     |     | From | a Bayesian |     | standpoint, | models | such | as  |
| -------------------- | --- | -------- | ------ | ---------- | --- | --- | ---- | ---------- | --- | ----------- | ------ | ---- | --- |
| 3.3. Representations |     | Oriented | Toward | Robustness | t   | and |      |            |     |             |        |      |     |
BayesianOnlineChangepointDetection(BOCPD)and
Interpretation
o
itsnon-parametricextensionsprovideanalternativeyet
This subsection introduces representation strategies related representation: they estimate, at each time t,
| oriented toward |     | robustness | and | interpretability. |     | The |                                                     |     |     |     |     |     |     |
| --------------- | --- | ---------- | --- | ----------------- | --- | --- | --------------------------------------------------- | --- | --- | --- | --- | --- | --- |
|                 |     |            | n   |                   |     |     | theposteriordistributionoftherun-length(timeelapsed |     |     |     |     |     |     |
goal is to construct representations that remain stable sincethelastchange)andofcurrentmodelparameters
under distribution shifts while providing economically [? ? ? ? ? ? ]. In practice, BOCPD computes,
meaningfulsignalsofregimechanges.   Anaturalwayto at each new datum, a probability p(changepoint) t in-
achievethisistomakeregimesexplicitintherepresen- dicating how likely it is that a change occurred at that
t
tation itself, so that changes correspond to transitions point, and maintains parameter distributions under the
n
| betweeninterpretablesystemstates. |     |     |     |     |     |     | no-changehypothesis. |     |     |     |     |     |     |
| --------------------------------- | --- | --- | --- | --- | --- | --- | -------------------- | --- | --- | --- | --- | --- | --- |
Thetimeseriesofthesechangeprobabilitiesandstate
Latent-State and i Regime-Based Representations.. statistics (for example, the posterior distribution of the
Oneprominentclassofapproacheswithinthisperspec- currentlyactivelevelorvariance)become, themselves,
r
tive relies on latent-state models with explicit regimes. rich representations of the degree of change perceived
Classical p regime-switching models—such as HMMs, by the model. It is like a continuously updated “evi-
MS-VAR,orregimeGARCH—representthesystemas dencepanel”:ifp(changepoint)risesabruptly,wehave
t
a finite set of discrete states, each associated with dis- astrongindicationofdrift;ifuncertaintyaboutparam-
e
tinct statistical properties, and define transition proba- etersincreases,thispointstostructuralinstability.
bilitiesamongthesestates[? ? ? ? ]. In summary, latent-state models (whether classical
r From a representation standpoint, fitting such a HMMs or online Bayesian methods) provide regime-
model amounts to mapping each time point to a vec- orientedrepresentations—mappingdataintoprobabil-
P
torofregime-membershipprobabilities,obtainedeither itiesofscenarios—thatbothrobustlycapturerelevant
inrealtime(filtered)oraposteriori(smoothed). These changes and enhance interpretability (since they make
vectors may be complemented by derived quantities, explicit “I am X% in regime A and Y% in regime B
16
This preprint research paper has not been peer reviewed. Electronic copy available at: https://ssrn.com/abstract=6170273

d
e
now”). cent studies show that causality-inspired models can
yield more robust forecasts prwecisely in turbulent peri-
Causal and Invariant Representations.. While this ods,whenspuriousrelationshipschangeandonlystruc-
approach achieves robustness by explicitly modeling tural links remain[? ? ? ? ? ]. This suggests that
regimetransitions,acomplementarylineofworkseeks invariantrepresentationsnotonlyhelpdetection(reduc-
e
robustnessatadeeperlevel: byidentifyingrepresenta- ingnoisyfalsealarmsduetosuperficialvariations)but
tions that remain valid across changing environments. also serve as a basis for adaptive models that maintain
Thismotivatesagroupoftechniquesfocusedoncausal performanceunderdrift.
i
and invariant representations. The dataset-shift litera-
v
ture in classification emphasizes that many drifts arise Foundation Models and Universal Embeddings..
fromchangesinconfoundersorinthesurroundingenvi- Alongthesamelineofpursuingrobustandtransferable
ronment—altering P(X) or jointly P(X,Y)—while cer- embeddingse, recent work explores time-series founda-
tain underlying causal relationships remain stable over tion models as providers of universal embeddings. In-
time[? ? ? ? ? ]. Forexample,aninvestmentstrategy spiredbythesuccessoflargepre-trainedmodelsinlan-
r
mayfailinanewregimebecauseitreliedonaspurious guage and vision, researchers have examined whether
correlationthatheldhistoricallybutlatervanished,even large- scaletime-seriesmodels,pre-trainedonheteroge-
though the fundamental causal drivers of returns per- neous collections of series, can serve as backbones for
r
sisted (e.g., a macroeconomic factor whose effect was diversefinancialtasks[? ? ]. Theideaisthataneural
previouslymasked). emodeltrainedonawiderangeofdomainsandfrequen-
Inresponse,aclassofmethodshasemergedthataims cieslearnsembeddingsofwindowsorentireseriesthat
to learn features invariant to environmental changes, carrytemporalknowledgeinageneralway—capturing
e
drawing on ideas from Invariant Risk Minimization seasonalpatterns,typicalreactionstoshocks,etc.—and
(IRM) [? ] and related frameworks. Rather than that these embeddings can later be specialized to fi-
optimizing only average predictive performance on nance.
p
historical data, these approaches impose constraints Instead of training a representation model from
or regularizers that penalize excessive dependence scratch on often limited market- or asset-specific data,
on environment-specific components, enco uraging the one can adopt strategies such as: (1) using the pre-
model to rely on more stable and transfe t rable relation- trained foundation model as a fixed feature extractor
ships[? ? ? ? ]. andapplyingchangedetectorstotheembeddingsitgen-
o
In financial contexts, this amounts to seeking repre- erates; or(2)performinglightadaptation(fine-tuning),
sentationsthatprivilegestructuraldrivers(e.g.,riskpre- adjusting only the final layers to specialize the repre-
mia genuinely linked to econnomic fundamentals) and sentation to the financial domain [? ? ? ]. Both ap-
downweight correlations that, although effective in a proaches aim to leverage the inductive bias contained
given regime, are peculiar to that environment and do in large-scale pretraining—for example, a foundation
notpersistoutsideit. Asa nexample, imaginearepre- modelmayalready“know”howtorepresentmacrocy-
sentation of equities thatt emphasizes fundamental fac- clesorcommonshocks;eveniftheassetinquestionhas
tors (valuation metrics, earnings growth, etc.) and is never experienced a given regime in the available his-
n
lesssensitivetoshort-termtechnicalfactorswhosesign tory,themodelmayrecognizeanalogouspatternsfrom
may flip when the regime changes — such a represen- other contexts and thus generalize better under moder-
tationtendstobiemorerobusttomarketshifts,because ateshifts.
fundamentals r persist while transient technical patterns From a pipeline perspective, embeddings provided
maydisappear. byfoundationmodelsenterasenrichedinternalsignals,
Inprpactice,buildinginvariantrepresentationsmayin- representingtheseriesthroughvectorsofadvancedfea-
volve: (i) selecting features whose relationship with tures. Thisisarapidlyevolvingarea;althoughpromis-
returns remains stable across subperiods or regimes ing, it requires careful assessment of whether patterns
e
(identifying“resilient”variableswhoseestimatedcoef- learned from other domains apply to specific financial
ficients vary little between regimes); (ii) training em- contexts,aswellasmechanismsforupdatingthefoun-
rbeddingswithobjectivesthatenforcepredictiveconsis- dationmodelwhenthevery“universe”ofseriesevolves
tencyacrossmultipleenvironments(e.g.,differentmar- (for example, new data types or post-2020 dynamics).
P
ket windows); (iii) integrating with latent-state models Well-designed representations not only increase sensi-
that make environments/regimes explicit and penalize tivity and timeliness in identifying changes, but also
excessive variation in causal effects across states. Re- facilitate the economic interpretation of the resulting
17
This preprint research paper has not been peer reviewed. Electronic copy available at: https://ssrn.com/abstract=6170273

d
e
regimes—sincetheyconnecteachdriftalarmtounder- 4. ChangeDetection
| standableinternalsignalsandpotentialstructuralmech- |     |     |     |     |     |     |     |     |     |     | w   |     |     |
| --------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
anisms.
|     |     |     |     |     |     |     | This | Section | addresses | the | research | question: | How |
| --- | --- | --- | --- | --- | --- | --- | ---- | ------- | --------- | --- | -------- | --------- | --- |
candriftsindatabeautomaticallydetectedovertime?
|             |            |     |     |             |             |     | To answer | it, | we organize |     | the discussion |     | around the |
| ----------- | ---------- | --- | --- | ----------- | ----------- | --- | --------- | --- | ----------- | --- | -------------- | --- | ---------- |
| 3.4. Design | Guidelines |     | for | Drift-Aware | Representa- |     |           |     |             |     |                |     |            |
e
| tions |     |     |     |     |     |     | main methodological |               |     | paradigms    | used | in practice. | We    |
| ----- | --- | --- | --- | --- | --- | --- | ------------------- | ------------- | --- | ------------ | ---- | ------------ | ----- |
|       |     |     |     |     |     |     | first cover         | retrospective |     | segmentation |      | methods,     | which |
Table5summarizespracticalchoicesforrepresenta- identify changes after observing a full data window
i
tionandmonitoringunderdifferentdriftscenarios,link-
|     |     |     |     |     |     |     | (4.1). We | then | move | to sequential |     | (online) | monitor- |
| --- | --- | --- | --- | --- | --- | --- | --------- | ---- | ---- | ------------- | --- | -------- | -------- |
v
ingobservabledriftpatternstoconcretesignalfamilies ing techniques, designed to trigger alarms as data ar-
| and failure | modes. | In  | practice, | representation |     | design |     |     |     |     |     |     |     |
| ----------- | ------ | --- | --------- | -------------- | --- | ------ | --- | --- | --- | --- | --- | --- | --- |
rive(4.2),followedbyBayesianapproachesthatmodel
e
canbeguidedbyasmallnumberofrecurringsituations: regimechan gesprobabilistically(4.3). Thesectionfur-
therexaminesdetectorsoperatinginlearnedrepresenta-
| • Abrupt | shocks | (e.g., | crashes, |     | policy | announce- |     |     |     |     |     |     |     |
| -------- | ------ | ------ | -------- | --- | ------ | --------- | --- | --- | --- | --- | --- | --- | --- |
tionspacesandout-of-distributionsettings(4.4),aswell
r
ments): monitor short-window statistics (mean, as methods that target changes in multivariate depen-
| variance) |     | or regime | probabilities |     | from | HMMs. |     |     |     |     |     |     |     |
| --------- | --- | --------- | ------------- | --- | ---- | ----- | --- | --- | --- | --- | --- | --- | --- |
dence structures(4.5).
These signals react quickly and are suitable for rTosynthesizetheseperspectives,4.6providesacom-
| early | warning, | but | may | trigger | false alarms | under |     |     |     |     |     |     |     |
| ----- | -------- | --- | --- | ------- | ------------ | ----- | --- | --- | --- | --- | --- | --- | --- |
pactoverviewthatlinksthetypesofchangedefinedby
temporarynoise. ethetaxonomicaxestosuitabledetectionstrategies.This
|     |     |     |     |     |     |     | overview | serves | as a | practical | guide | for method | selec- |
| --- | --- | --- | --- | --- | --- | --- | -------- | ------ | ---- | --------- | ----- | ---------- | ------ |
•
| Gradual | or  | long-term |     | changes | (e.g., | persistent |     |     |     |     |     |     |     |
| ------- | --- | --------- | --- | ------- | ------ | ---------- | --- | --- | --- | --- | --- | --- | --- |
tion,whilealsoemphasizinghowthechoiceoftheob-
| volatility | increases): |     | use | longer | rolling | windoews |     |     |     |     |     |     |     |
| ---------- | ----------- | --- | --- | ------ | ------- | -------- | --- | --- | --- | --- | --- | --- | --- |
servedsignalandtherepresentationspaceshapesdetec-
ormulti-scaleembeddingstotrackslowdrifts,ac-
|     |     |     |     |     |     |     | tor behavior | and | interpretability |     | [?  | ? ? | ]. Together, |
| --- | --- | --- | --- | --- | --- | --- | ------------ | --- | ---------------- | --- | --- | --- | ------------ |
ceptinglaterdetectioninexchangeforstability.
ptheseelementsconnectmethodologicaldecisionstothe
|     |     |     |     |     |     |     | effective | detection | of  | different | forms | of drift | in real- |
| --- | --- | --- | --- | --- | --- | --- | --------- | --------- | --- | --------- | ----- | -------- | -------- |
• Frequentregimeswitching:adoptlatent-statemod-
worlddata.
| els | (HMM, | MS-VAR) | and | track | regime | probabil- |     |     |     |     |     |     |     |
| --- | ----- | ------- | --- | ----- | ------ | --------- | --- | --- | --- | --- | --- | --- | --- |

| ities | or expected |     | durations; | performance |     | depends |     |     |     |     |     |     |     |
| ----- | ----------- | --- | ---------- | ----------- | --- | ------- | --- | --- | --- | --- | --- | --- | --- |
oncorrectlyspecifyingthenumbero t fregimes. 4.1. Segmentation(retrospectiveoptimization)
o
| •                            |     |                 |     |                   |                 |     | Segmentationmethodsseektopartitionthehistorical |     |            |     |         |                 |     |
| ---------------------------- | --- | --------------- | --- | ----------------- | --------------- | --- | ----------------------------------------------- | --- | ---------- | --- | ------- | --------------- | --- |
| Asset-                       | or  | sector-specific |     | drift:            | use dependency- |     |                                                 |     |            |     |         |                 |     |
|                              |     |                 |     |                   |                 |     | timeseriesX                                     |     | = X ,...,X |     | ,whereT | denotesthetotal |     |
| basedrepresentations(graphs, |     |                 |     | taildependence)to |                 |     |                                                 | 1:T | 1          | T   |         |                 |     |
correlantions numberofobservationsandX t theobservationattimet,
| detect | changes | in  |     | and | contagion | pat- |     |     |     |     |     |     |     |
| ------ | ------- | --- | --- | --- | --------- | ---- | --- | --- | --- | --- | --- | --- | --- |
intoapproximatelystationarysegments,retrospectively
| terns, | noting | that | estimates | may | become | unstable |            |     |             |     |           |      |              |
| ------ | ------ | ---- | --------- | --- | ------ | -------- | ---------- | --- | ----------- | --- | --------- | ---- | ------------ |
|        |        |      |           |     |        |          | optimizing | the | changepoint |     | locations | that | best explain |
insmallsamples.
|     |     |     |     |     |     |     | the data.    | In this | setting,   | it  | is assumed | that    | the series |
| --- | --- | --- | --- | --- | --- | --- | ------------ | ------- | ---------- | --- | ---------- | ------- | ---------- |
| •   |     |     |     |     |     |     | is generated | by      | a sequence | of  | distinct   | regimes | indexed    |
Externallydrivencthanges(e.g.,news,narratives):
combine prices with textual data through multi- byr,eachassociatedwithaprobabilitydistribution(or
n
|        |             |     |            |            |     |             | model)P(X              | |θ  | ),whereθ | denotesthesetofparameters |     |     |     |
| ------ | ----------- | --- | ---------- | ---------- | --- | ----------- | ---------------------- | --- | -------- | ------------------------- | --- | --- | --- |
| modal  | embeddings  |     | to capture | signals    |     | before they |                        | r   |          | r                         |     |     |     |
|        |             |     |            |            |     |             | characterizingregimer. |     |          | Eachregimeisapproximately |     |     |     |
| appear | in returns, |     | while      | accounting | for | alignment   |                        |     |          |                           |     |     |     |
andscalingiissues. stationarywithinitscorrespondingsegment,andregime
changescorrespondtobreaksintheunderlyingdistribu-
r
| •                                        |     |     |     |     |     |     | tionor,equivalently,intheparametersθ |     |     |     |     | .   |     |
| ---------------------------------------- | --- | --- | --- | --- | --- | --- | ------------------------------------ | --- | --- | --- | --- | --- | --- |
| Needforrobustnessacrossmarketconditions: |     |     |     |     |     | fa- |                                      |     |     |     |     | r   |     |
voprinvariantorcausalrepresentationstoreducere- In some cases, segmentation is applied not directly
liance on regime-specific correlations, at the cost to X, but to representations Z = f(X) or Z = f(X,Y)
ofdiscardingsomeshort-termpredictivesignals. (forexamplelatentfactorsorfeaturesextractedfromre-
e
turnsandcovariates),sothatonesearchesforbreaksin
Taken together, the checklist and table emphasize a P(Z)overtime.Segmentationalgorithmsthenapplyop-
rsimple principle: the representation should match the timization routines (exhaustive or approximate) to find
dominant form of drift one expects to face. Fast sig- the optimal partition in terms of a global cost criterion
P
| nals favor | sensitivity, |     | stable | embeddings | favor | robust- | [? ? ? ]. |     |     |     |     |     |     |
| ---------- | ------------ | --- | ------ | ---------- | ----- | ------- | --------- | --- | --- | --- | --- | --- | --- |
ness, and interpretable regimes favor control and diag- A classical approach is the minimization of an ad-
| nosis. |     |     |     |     |     |     | ditivecostcriterion. |     | Onedefinesanintra-segmentcost |     |     |     |     |
| ------ | --- | --- | --- | --- | --- | --- | -------------------- | --- | ----------------------------- | --- | --- | --- | --- |
18
This preprint research paper has not been peer reviewed. Electronic copy available at: https://ssrn.com/abstract=6170273

d
e
Table5:Designchecklistlinkingdrifttaxonomyaxestorepresentationchoices.
w
Driftcharacteristic Signal/featurefamily Early-warning indica- Principalfailuremode
tor
Abruptdrift Short-windowstatistics, Sharp changes in mean, False alarms due to tran-
e
|     |     |     |     | BOCPD,   | HMM | proba- | variance,   | or  | regime | sientnoise |     |     |     |
| --- | --- | --- | --- | -------- | --- | ------ | ----------- | --- | ------ | ---------- | --- | --- | --- |
|     |     |     |     | bilities |     |        | probability |     |        |            |     |     |     |
Gradual or secular Multi-scale statistics, Slow but persistent fea- iDelayeddetection
| drift |     |     |     | embeddings |     |     | turedrift |     |     |     |     |     |     |
| ----- | --- | --- | --- | ---------- | --- | --- | --------- | --- | --- | --- | --- | --- | --- |
v
/
Regimeswitching HMM MS-VAR latent Probability crossovers, Regimemisspecification
|     |     |     |     | states |     |     | durationshifts |     |     |     |     |     |     |
| --- | --- | --- | --- | ------ | --- | --- | -------------- | --- | --- | --- | --- | --- | --- |
e
Localized or sectoral Graph embeddings, tail Rewiringofdependency Estimationinstability
| drift |     |     |     | dependence |     |     | clusters |     |     |     |     |     |     |
| ----- | --- | --- | --- | ---------- | --- | --- | -------- | --- | --- | --- | --- | --- | --- |
Narrative-drivendrift Multimodal (price + Text-led dirvergence be- Alignment and modality
|     |     |     |     | text)embeddings |     |     | forepricemoves |     |     | noise |     |     |     |
| --- | --- | --- | --- | --------------- | --- | --- | -------------- | --- | --- | ----- | --- | --- | --- |
Spurious correlation Invariant / causal repre- Stability acrossenviron- Loss of short-term pre-
| drift |     |     |     | sentations |     |     | mentrs |     |     | dictability |     |     |     |
| ----- | --- | --- | --- | ---------- | --- | --- | ------ | --- | --- | ----------- | --- | --- | --- |
e
thatusuallycoincideswithanegativelog-likelihood,for
example
eAlgorithm1:PELT:PrunedExactLinearTime
|        | C(a,b)≈−logp                    |     |     | (cid:0) |θˆ | (cid:1) |      |     |                   |     |     |          |                  |     |
| ------ | ------------------------------- | --- | --- | ----------- | ------- | ---- | --- | ----------------- | --- | --- | -------- | ---------------- | --- |
|        |                                 |     |     | X a:b       | a:b ,   |      |     |                   |     | =(x |          |                  |     |
|        |                                 |     |     |             |         |      |     | Input:Timeseriesx |     | 1:n | 1 ,...,x | n );costfunction |     |
| whereX | isthedatablockinthesegmentandθˆ |     |     |             |         | are  |     | C(·);penaltyβ     |     |     |          |                  |     |
|        | a:b                             |     |     |             |         | pa:b |     |                   |     |     |          |                  |     |
Output:Setofchangepointlocations
| parameters                                        | estimated |            | under the | hypothesis | that,      | in that |     |          |            |         |           |            |      |
| ------------------------------------------------- | --------- | ---------- | --------- | ---------- | ---------- | ------- | --- | -------- | ---------- | ------- | --------- | ---------- | ---- |
|                                                   |           |            |           |            |            |         |     | T        | ={τ ,...,τ | }       |           |            |      |
| interval,thedistributionP(X)(orP(Z))isstationary. |           |            |           |            |            |         | A   |          | 1          | K       |           |            |      |
|                                                   |           |            |           |            |            |         |     | F(0)←−β; | //         | Optimal | cost      | up to time | 0    |
| costisthenaddedforeachbreakintroduced (apenalty   |           |            |           |            |            |         |     | 1        |            |         |           |            |      |
|                                                   |           |            |           |            |            |         |     | R ←{0};  |            | //      | Candidate | set of     | last |
| as a function                                     | of        | the number | of        | segments). | Algorithms |         |     | 2 0      |            |         |           |            |      |
t
| suchasBai&Perron[? |            |     | ] implementexhaustivesearch |               |     |           |     | changepoints |     |              |     |            |     |
| ------------------ | ---------- | --- | --------------------------- | ------------- | --- | --------- | --- | ------------ | --- | ------------ | --- | ---------- | --- |
|                    |            |     |                             | o             |     |           |     | 3 cp(0)←∅;   | //  | Changepoints |     | up to time | 0   |
| for multiple       | structural |     | breaks                      | by minimizing |     | the total |     |              |     |              |     |            |     |
fort=1tondo
| penalizedcost. |     |     |     |     |     |     |     | 4   |     |     |     |     |     |
| -------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
AnothermoreefficientmethodsuchasPELT(Pruned // Find optimal previous changepoint
|     |     |     | n   |     |     |     |     |               |     | (cid:2) |          | (cid:3) |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------- | --- | ------- | -------- | ------- | --- |
|     |     |     |     |     |     |     |     | (F(t),τ∗)←min |     |         | F(τ)+C(x | )+β     |     |
Exact Linear Time) [? ], sum marized in Algorithm 1, 5 τ∈Rt−1 τ+1:t
|                           |     |     |     |           |      |         |     | cp(t)←cp(τ∗)∪{τ∗}; |     |     |     | // Store | best |
| ------------------------- | --- | --- | --- | --------- | ---- | ------- | --- | ------------------ | --- | --- | --- | -------- | ---- |
| use a dynamic-programming |     |     |     | recursion | with | pruning |     | 6                  |     |     |     |          |      |
configuration
rulesthatexploittheadditi vestructureofthecostfunc-
tion C to discard suboptimal candidates, achieving lin- // Prune: remove candidates that
t
|                   |     |                                 |         |           |           |      |     | cannot    | be  | optimal       |     |               |     |
| ----------------- | --- | ------------------------------- | ------- | --------- | --------- | ---- | --- | --------- | --- | ------------- | --- | ------------- | --- |
| ear computational |     | cost                            | in many | practical | settings, | with |     |           |     |               |     |               |     |
|                   |     | n                               |         |           |           |      |     | 7 R ←{τ∈R |     | ∪{t}|F(τ)+C(x |     | τ+1:t )≤F(t)} |     |
| thepenaltyβcontro |     | llingthenumberofdetectedchange- |         |           |           |      |     | t         | t−1 |               |     |               |     |
end
| points.    |                   |          |           |          |                  |      |     | 8             |     |     |         |              |     |
| ---------- | ----------------- | -------- | --------- | -------- | ---------------- | ---- | --- | ------------- | --- | --- | ------- | ------------ | --- |
|            |                   |          |           |          |                  |      |     | T ←cp(n)\{0}; |     | //  | Extract | changepoints |     |
| Once       | the segmientation |          | framework |          | and optimization |      |     | 9             |     |     |         |              |     |
|            |                   |          |           |          |                  |      |     | (exclude      | 0)  |     |         |              |     |
| algorithms | are               | defined, | a key     | modeling | choice           | con- |     |               |     |     |         |              |     |
r
10 returnT
| cerns which | aspect | of  | the data-generating |     | distribution |     |     |     |     |     |     |     |     |
| ----------- | ------ | --- | ------------------- | --- | ------------ | --- | --- | --- | --- | --- | --- | --- | --- |
Complexity:O(n)averagecasewithpruning,O(n2)
| istargeptedbythecostfunction.                     |     |     |     | Segmentationmethods |     |     |     | 11                 |     |               |     |             |     |
| ------------------------------------------------- | --- | --- | --- | ------------------- | --- | --- | --- | ------------------ | --- | ------------- | --- | ----------- | --- |
| thereforerequirespecifyingwhetherchangesaresought |     |     |     |                     |     |     |     | worstcase          |     |               |     |             |     |
|                                                   |     |     |     |                     |     |     |     | 12 Costfunctions:C |     | (meanshift),C |     | (variance), |     |
in the mean (location parameters), variance or covari- L2 Gauss
| e                                                  |     |     |     |     |     |     |     | C (nonparametric) |     |     |     |     |     |
| -------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | ----------------- | --- | --- | --- | --- | --- |
| ancestructure,orinthefulldistributionofP(X)orP(Z). |     |     |     |     |     |     |     | RBF               |     |     |     |     |     |
Penalty:β=c·logn(BIC-type);higherβ⇒fewer
13
| The choice |     | of contrast | statistic | directly | determines |     |     |     |     |     |     |     |     |
| ---------- | --- | ----------- | --------- | -------- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- |
changepoints
rthe type of changepoint that can be detected. Mean- Typicaluse:Offlinesegmentation;multiplebreaks;
14
| based contrasts |     | primarily | identify | level | shifts, | while |     |     |     |     |     |     |     |
| --------------- | --- | --------- | -------- | ----- | ------- | ----- | --- | --- | --- | --- | --- | --- | --- |
longseries
P
| variance-based |     | contrasts | are | sensitive | to changes | in  |     | References:[??] |     |     |     |     |     |
| -------------- | --- | --------- | --- | --------- | ---------- | --- | --- | --------------- | --- | --- | --- | --- | --- |
15
| volatility.      | More | general   | distributional |              | contrasts, | such      |     |     |     |     |     |     |     |
| ---------------- | ---- | --------- | -------------- | ------------ | ---------- | --------- | --- | --- | --- | --- | --- | --- | --- |
| as density-based |      | measures, |                | divergences, |            | or energy |     |     |     |     |     |     |     |
19
This preprint research paper has not been peer reviewed. Electronic copy available at: https://ssrn.com/abstract=6170273

d
e
distances, allow the detection of broader structural timeseries.
changes. Inpractice,segmentationoftenreliesonsim- w
ple within-segment models, including constant means, 4.2. SequentialMethods(onlinemonitoring)
linear regressions, or AR/ARMA processes, with Sequential methods perform detection in real time,
changepoints corresponding to shifts in the regime- examining the series continuously as new data arrive.
e
specificparametersθ . In probabilistic terms, one typically assumes a “pre-
r
An important characteristic is that segmentation change” distribution P (X) and a “post-change” distri-
0
methods provide a set of estimated changepoints for butionP (X)(or,moreagnostically,oneseekstodetect
1 i
the entire series (off-line mode), being suitable for ex- when P (X) starts to differ from P (X)). The
recent v baseline
ploratory analysis or historical validation of regimes. goal is to trigger an alarm as quickly as possible af-
They do not operate in real time, but often offer high terachangein P(X)occurs,whilecontrollingthefalse
precision in ex post localization of significant changes alarmrate. T e hesemethodstypicallymaintainawindow
in P(X) or its parameters, especially when combined oradaptivemodelandapplyrecurrentstatisticaltests.
withrobuststoppingcriteria(penalties)thatavoidover- AclassicexampleistheCUSUM(CumulativeSum)
r
segmentation (inserting breaks where there is only testanditsvariants,detailedintheAlgorithm2,which
noise)[??].Forexample,techniquessuchastheBarry monit ortheaccumulateddeviationofastatistic(forex-
&Hartiganmethod[? ] usepartitionmodelsandpriors amplethemeanofX orofaresidual)relativetoarefer-
r t
for optimal segmentation with uncertainty, obtaining a ence value associated with P (X), signaling a change
0
posterior distribution over partitions of the series into ewhen this deviation exceeds a threshold. The choice
approximatelystationaryblocksintermsofP(X). of the decision threshold and reference value (and the
Beyond these canonical algorithms, there is a broad implied false-alarm/delay trade-off). In its likelihood-
e
family of techniques that build upon segmentation as ratio formulation, CUSUM accumulates contrasts of
a basic block. Non-parametric extensions, such as theformlog p1(Xt),approximatingoptimaldetectionbe-
p0(Xt)
E-Divisive, energy-distance segmentation, anpd kernel tweenP
0
(X)andP
1
(X)undercertainassumptions. An-
changepointmethods(kernelCPD),allowthedetection otherexampleistheapproachofPage–Hinkley, which
ofbreaksincomplexdistributionsP(X)orP(Z)without statesthatderivativesfollowasimilarlogic[? ].
specifying an explicit parametric model, a nd are par- Another common formulation compares two win-
ticularlyusefulforfinancialserieswithhteavytailsand dows: arecentslidingwindow, associatedwithanem-
asymmetries. pirical distribution P (X), versus a past window or
o recent
Multi-scale methods based on random sub-intervals, long-termestimate P (X). Onlinetwo-sampletest
baseline
suchasWildBinarySegmentation(WBS)anditsexten- techniques,suchasADWINandotherdriftdetectorsin
sion WBS2, explore a large nnumber of candidate seg- data streams, continuously compute the statistical dif-
ments to locate multiple changepoints, including sce- ference between these empirical distributions (e.g., in
narios with frequent breaks and very short spacing be- terms of mean, variance, or non-parametric measures
tweendrifts[? ? ]. ofdivergence)andperformsequentialhypothesistests,
Narrowest-Over-Thretshold (NOT), in turn, priori- shrinking or expanding windows as needed to confirm
tizes the smallest interval whose contrast exceeds a a change in P(X). Algorithms such as DDM, EDDM,
n
threshold, producing well-localized estimates of fea- etc.,areusedinthedata-streamliteraturetomonitorer-
turessuchasjumpsinthemeanorchangesinslopeand rormetricsofaclassifierovertime–thatis, anaggre-
generalizingtodiifferenttypesofstructuralchange[? ]. gatedlossfunctionL
t
=ℓ(Y
t
,Yˆ
t
)whenpairs(X
t
,Y
t
)are
In summarry, segmentation methods frame change- available–andtriggeralarmswhenthereisasignificant
point detection as an offline optimization problem, in increaseinthesemetrics–indicatingconceptdrift(strict
whichaptimeseriesisretrospectivelypartitionedintoap- sense)inP(Y | X)[? ? ? ].
proximatelystationaryregimesbyminimizingapenal- A central challenge in these methods is controlling
izedglobalcost. Theireffectivenessdependsjointlyon the trade-off between rapid detection and false alarms.
e
thechoiceofrepresentation(X orZ),theintra-segment Thresholdsthataretoosensitiveleadtofrequentalarms
cost function, and the penalty controlling model com- duetorandomfluctuationsinP(X);highthresholdsare
rplexity. As a result, segmentation provides a flexible slow to react to real changes. For this reason, several
and principled way to identify structural breaks and techniquesuseresultsfromsequentialstoppingtheory:
P
regimeboundariesinhistoricaldata,servingasafoun- forexample,definingthresholdsthatguaranteeacertain
dational tool for exploratory analysis, regime charac- level of ARL (Average Run Length) for false detec-
0
terization, and downstream modeling in non-stationary tions – that is, on average, how long a change-free pe-
20
This preprint research paper has not been peer reviewed. Electronic copy available at: https://ssrn.com/abstract=6170273

d
e
|     |     |     |     |     |     | riodunder | P 0 (X)lastsuntilafalsealarmoccurs. |     |     |     |     | Well- |
| --- | --- | --- | --- | --- | --- | --------- | ----------------------------------- | --- | --- | --- | --- | ----- |
knownsequentialmethodssucwhasShiryaev–Robertsor
|     |     |     |     |     |     | multivariate | CUSUM |      | calibrate | thresholds |     | via the de- |
| --- | --- | --- | --- | --- | --- | ------------ | ----- | ---- | --------- | ---------- | --- | ----------- |
|     |     |     |     |     |     | siredARL     | [?    | ? ]. |           |            |     |             |
0
|     |     |     |     |     |     | Both | approaches | are | necessary | in  | financial | applica- |
| --- | --- | --- | --- | --- | --- | ---- | ---------- | --- | --------- | --- | --------- | -------- |
e
tions,becauseonlinemonitoringisusedtodetectstruc-
|     |     |     |     |     |     | turalchangesinproduction: |     |     |     | forexample, | warningthat |     |
| --- | --- | --- | --- | --- | --- | ------------------------- | --- | --- | --- | ----------- | ----------- | --- |
ariskmodelhasstartedtofailbecauseP(X)orP(X,Y)
i
|     |     |     |     |     |     | haschanged. | Sothatportfoliocorrelations,thedistribu- |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | ----------- | ---------------------------------------- | --- | --- | --- | --- | --- |
v
tionofP&L,ortherateofVaRviolationsarenolonger
compatiblewiththehistoricalregime.
effie
|     |     |     |     |     |     | Some | cient | implementations |     | (for | example, | using |
| --- | --- | --- | --- | --- | --- | ---- | ----- | --------------- | --- | ---- | -------- | ----- |
Algorithm 2: CUSUM for Mean Shift Detec- low-complexitynon-parametrictests)allowdetectorsto
| tion |     |     |     |     |     | runinstreamingonmarketdata. |     |     |     | Itisworthnotingthat |     |     |
| ---- | --- | --- | --- | --- | --- | --------------------------- | --- | --- | --- | ------------------- | --- | --- |
r
Input:Datastreamx ,x ,...,x ;in-controlmeanµ ; many sequential methods assume some knowledge of
|     |                                     |     | 1 2 | n   | 0   |         |           |       |     |          |      |             |
| --- | ----------------------------------- | --- | --- | --- | --- | ------- | --------- | ----- | --- | -------- | ---- | ----------- |
|     | standarddeviationσ;thresholdh;slack |     |     |     |     | P (X) ; |           |       |     |          |      |             |
|     |                                     |     |     |     |     | 0 in    | contrast, | works | on  | drift in | data | streams aim |
parameterk(typically0.5)
|     |                                       |     |     |     |     | to be more               | agnostic, | using | sliding-window |            |     | approaches |
| --- | ------------------------------------- | --- | --- | --- | --- | ------------------------ | --------- | ----- | -------------- | ---------- | --- | ---------- |
|     | Output:Detectiontimeτor∅(nodetection) |     |     |     |     | r                        |           |       |                |            |     |            |
|     |                                       |     |     |     |     | andempiricallycomparingP |           |       |                | (X)versusP |     | (X)        |
|     |                                       |     |     |     |     |                          |           |       |                | recent     |     | baseline   |
|     | S+←0;                                 |     |     |     |     | eordirectlymonitoring    |           |       |                |            |     |            |
1 // Cumulative sum for upward P recent (Y | X)throughpredictive
|     | shifts |     |     |     |     | performance. |     |     |     |     |     |     |
| --- | ------ | --- | --- | --- | --- | ------------ | --- | --- | --- | --- | --- | --- |
2 S−←0; // Cumulative sum for downward In practice, sequential methods are the backbone of
|     | shifts |     |     |     | e   |                  |     |       |            |     |         |        |
| --- | ------ | --- | --- | --- | --- | ---------------- | --- | ----- | ---------- | --- | ------- | ------ |
|     |        |     |     |     |     | many operational |     | tools | in finance | and | machine | learn- |
fort=1tondo
| 3   |           |            |     |     |              | ing for                                    | data streams. |     | In risk | monitoring, |     | variants of |
| --- | --------- | ---------- | --- | --- | ------------ | ------------------------------------------ | ------------- | --- | ------- | ----------- | --- | ----------- |
|     | z ← (x    | − µ ) / σ; |     | //  | Standar dize |                                            |               |     |         |             |     |             |
| 4   | t t       | 0          |     |     |              |                                            |               |     |         |             |     |             |
|     |           |            |     |     | p            | CUSUM,EWMA,andGLR(generalizedlikelihoodra- |               |     |         |             |     |             |
|     | o bse r v | at i o n   |     |     |              |                                            |               |     |         |             |     |             |
S+←max(0,S++z tio tests) are applied to P&L series, counts of VaR vi-
| 5   |     |     | −k); | // Update | upward |           |                     |     |     |           |     |              |
| --- | --- | --- | ---- | --------- | ------ | --------- | ------------------- | --- | --- | --------- | --- | ------------ |
|     |     |     | t    |           |        | olations, | or volatility-model |     |     | residuals | to  | build early- |
CUSUM
S−←max(0,S−−z −k); //   Update warning dashboards that trigger limit reviews or stress
| 6   |     |     | t   |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
downward CUSUM tests whenever the statistic crosses pre-defined control
t
|     | ifS+>horS−>hthen |     |     |     |     |                               |     |     |     | =   |                  |     |
| --- | ---------------- | --- | --- | --- | --- | ----------------------------- | --- | --- | --- | --- | ---------------- | --- |
| 7   |                  |     |     |     |     | bands,indicatingthatP(X)orP(Z |     |     |     |     | f(X))haschanged. |     |
|     | returnτ=t;       |     |     | o   |     |                               |     |     |     |     |                  |     |
8 // Alarm: change In terms of algorithmic standpoint, sequential pro-
|     | detected |     |     |     |     | cedures | based | on GLR | and | SPRT, | as well | as control |
| --- | -------- | --- | --- | --- | --- | ------- | ----- | ------ | --- | ----- | ------- | ---------- |
end
| 9   |     |     | n   |     |     | schemesonspreadandliquidityindicators,actas“kill- |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | ------------------------------------------------- | --- | --- | --- | --- | --- | --- |
10 end switches” that halt strategies when recent behavior be-
| 11  | return∅; |     | //  | No change | detected |                    |     |      |     |            |         |     |
| --- | -------- | --- | --- | --------- | -------- | ------------------ | --- | ---- | --- | ---------- | ------- | --- |
|     |          |     |     |           |          | comes incompatible |     | with | the | historical | regime. | GLR |
12 Complexity:O(n)time,O( 1)space compares online the likelihood of the data under no
Parameters:hcontrols ARL (falsealarmrate);kis change against the best-fitting post-change alternative,
| 13  |     |     | t 0 |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
theallowancefornoise
|     |     |     |     |     |     | while SPRT | (Sequential |     | Probability |     | Ratio | Test) accu- |
| --- | --- | --- | --- | --- | --- | ---------- | ----------- | --- | ----------- | --- | ----- | ----------- |
Typicaluse:Abrunptshiftsinmean;online
| 14  |     |     |     |     |     | mulatesevidencebetweentwospecifiedhypothesesun- |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | ----------------------------------------------- | --- | --- | --- | --- | --- | --- |
monitoring;lowlatency
|     |               |     |     |     |     | til a decision                                   | threshold |     | is reached. |     | Control | schemes |
| --- | ------------- | --- | --- | --- | --- | ------------------------------------------------ | --------- | --- | ----------- | --- | ------- | ------- |
| 15  | References:[? | ??] |     |     |     |                                                  |           |     |             |     |         |         |
|     |               | i   |     |     |     | basedonspreadandliquidityindicatorsfollowthesame |           |     |             |     |         |         |
logic.
r
|     |     |     |     |     |     | In the         | supervised |        | data-stream |                  | settings, | libraries |
| --- | --- | --- | --- | --- | --- | -------------- | ---------- | ------ | ----------- | ---------------- | --------- | --------- |
|     | p   |     |     |     |     | such as        | MOA,       | River, | and         | Scikit-Multiflow |           | provide   |
|     |     |     |     |     |     | DDM/EDDM/ECDD, |            |        | ADWIN,      | KSWIN,           | and       | CUSUM     |
variantsasplug-and-playcomponentswithinincremen-
e
|     |     |     |     |     |     | tal classifiers,                                    | which                                  | in  | practice | has       | consolidated | these        |
| --- | --- | --- | --- | --- | --- | --------------------------------------------------- | -------------------------------------- | --- | -------- | --------- | ------------ | ------------ |
|     |     |     |     |     |     | sequential                                          | detectors                              | as  | de facto | standards |              | for monitor- |
| r   |     |     |     |     |     | ingcovariatedriftinP(X),conceptdrift(strictsense)in |                                        |     |          |           |              |              |
|     |     |     |     |     |     | P(Y | X),                                           | andchangesintimeseriesinquasi-realtime |     |          |           |              |              |
P
|     |     |     |     |     |     | [? ? ? ? | ? ? ? | ].  |     |     |     |     |
| --- | --- | --- | --- | --- | --- | -------- | ----- | --- | --- | --- | --- | --- |
Finally,sequentialdetectorsareoftencombinedwith
|     |     |     |     |     |     | segmentation | methods: |     | the onlinecomponent |     |     | provides |
| --- | --- | --- | --- | --- | --- | ------------ | -------- | --- | ------------------- | --- | --- | -------- |
21
This preprint research paper has not been peer reviewed. Electronic copy available at: https://ssrn.com/abstract=6170273

d
e
whileoff-linesegmentation
fast, near-real-timealarms, assummarizedinAlgorithm3,viaamessage-passing
refines the dating and statistical significance of struc- scheme that combines: (i) twhe likelihood under the
tural breaks in subsequent analyses [? ? ]. Together, current regime, p(x | θ ) (or more generally p(x |
|     |     |     |     |     |     |     |     |     |     | t   | rt  |     |     | t   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
theseapproachesbalanceresponsivenessandstatistical r,x ) for dependent models); and (ii) a prior on
t t−rt:t−1
robustness, making sequential change detection a cen- regime duration, encoded by a hazard function h(r)
t
e
tral building block in non-stationary time-series analy- specifyingtheprobabilityofchangeasafunctionofr. t
| sis. |     |     |     |     |     |     | In     | terms | of data | distributions, |          | each | segment | corre- |
| ---- | --- | --- | --- | --- | --- | --- | ------ | ----- | ------- | -------------- | -------- | ---- | ------- | ------ |
|      |     |     |     |     |     |     | sponds | to    | a time  | interval       | in which | P(X) | (or P(Z | =      |
i
4.3. BayesianMethods f(X))) is assumed constant, and regime changes occur
v
whenthemodeldeemsitmorelikelythattherecentdata
| Bayesian | methods | model | changepoint |     | detection | by  |     |     |     |     |     |     |     |     |
| -------- | ------- | ----- | ----------- | --- | --------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
specifying a probabilistic structure both for the occur- comefromanewdistribution.
e
|             |         |         |                     |     |        |         | At        | each | step, the | algorithm       | weighs | two         | hypotheses: |        |
| ----------- | ------- | ------- | ------------------- | --- | ------ | ------- | --------- | ---- | --------- | --------------- | ------ | ----------- | ----------- | ------ |
| rence of    | changes | and for | the data-generating |     |        | process |           |      |           |                 |        |             |             |        |
|             |         |         |                     |     |        |         | “continue |      | in the    | current regime” |        | (increasing | r)          | versus |
| within each | regime. | Change  | times               | and | regime | states  |           |      |           |                 |        |             | t           |        |
=
are treated as latent variables, jointly inferred with the “startanewregimenow”(resettingr 0). Ifthepos-
|                  |     |     |     |     |     |     |        | r           |     |        |        | t     |                |     |
| ---------------- | --- | --- | --- | --- | --- | --- | ------ | ----------- | --- | ------ | ------ | ----- | -------------- | --- |
|                  |     |     |     |     |     |     | terior | probability |     | of r = | 0, p(r | = 0 | | x ), increases |     |
| modelparameters. |     |     |     |     |     |     |        |             |     | t      |        | t     | 1:t            |     |
It is assumed that the observations X —or pairs sharp ly,thisindicatesachangepointinnearrealtime.
1:T
|                                   |      |           |                   |        |     |           | In                                                | finance, | one   | often adjusts |           | the hazard | function | to     |
| --------------------------------- | ---- | --------- | ----------------- | ------ | --- | --------- | ------------------------------------------------- | -------- | ----- | ------------- | --------- | ---------- | -------- | ------ |
| (X,Y) t t                         | when | responses | are available—are |        |     | generated | r                                                 |          |       |               |           |            |          |        |
|                                   |      |           |                   |        |     |           | reflect                                           | beliefs  | about | the           | frequency | of         | regime   | breaks |
| fromregime-dependentdistributions |      |           |                   | P(X    | | θ | )or P(Y | |                                                   |          |       |               |           |            |          |        |
|                                   |      |           |                   |        |     | r         | e(forexample,volatilityshocksbeingrarerthansmooth |          |       |               |           |            |          |        |
| X,θ ), where                      |      | r indexes | the latent        | regime |     | and θ de- |                                                   |          |       |               |           |            |          |        |
| r                                 |      |           |                   |        |     | r         |                                                   |          |       |               |           |            |          |        |
changesinthemean)andchooseslikelihoodscompati-
| notes its | associated | parameters. |     | The | temporal | evolu- |     |     |     |     |     |     |     |     |
| --------- | ---------- | ----------- | --- | --- | -------- | ------ | --- | --- | --- | --- | --- | --- | --- | --- |
tion of regimes is itself probabilistic, commonly mod- blewithasymmetricorheteroscedasticreturns,oreven
e
|     |     |     |     |     |     |     | withdistributionsoverrepresentationsZ |     |     |     |     |     | = f(X). | Exact |
| --- | --- | --- | --- | --- | --- | --- | ------------------------------------- | --- | --- | --- | --- | --- | ------- | ----- |
eledthroughhazardfunctionsorMarkoviandynamics.
|           |     |              |     |        |              |      | BOCPD | has | cost | O(T2) in | the length | of  | the series, | but |
| --------- | --- | ------------ | --- | ------ | ------------ | ---- | ----- | --- | ---- | -------- | ---------- | --- | ----------- | --- |
| Inference | can | be performed |     | either | sequentially | (on- |       |     |      |          |            |     |             |     |
line) or retrospectively (off-line). As new obseprvations run-length truncations or sliding windows allow O(T)
approximations.
| arrive, or                                    | given | the full | data | history, | the | model up- |     |     |     |     |     |     |     |     |
| --------------------------------------------- | ----- | -------- | ---- | -------- | --- | --------- | --- | --- | --- | --- | --- | --- | --- | --- |
| datesposteriordistributionsovertheparametersθ |       |          |      |          |     | and       |     |     |     |     |     |     |     |     |
r
|                                          |     |     |     |     |  Retrospective |            |           |     |                 | Bayesian | segmentation |        | (Barry– |        |
| ---------------------------------------- | --- | --- | --- | --- | -------------- | ---------- | --------- | --- | --------------- | -------- | ------------ | ------ | ------- | ------ |
| overlatentquantitiessuchastherun-lengthr |     |     |     |     |                | t (thetime |           |     |                 |          |              |        |         |        |
|                                          |     |     |     |     |                |            | Hartigan, |     | Fearnhead–Liu). |          | A            | second | line    | of ap- |
elapsedsincethemostrecentchange)andttheprobabil-
off-line
ityofachangepointattimet. proaches works in mode, seeking the most
o
|     |     |     |     |     |     |     | probable | segmentation |     | (or | samples | from | the segmen- |     |
| --- | --- | --- | --- | --- | --- | --- | -------- | ------------ | --- | --- | ------- | ---- | ----------- | --- |
Thisframeworknaturallysupportsuncertaintyquan-
|                                                  |     |     |     |     |     |     | tationdistribution)giventheentirehistory |     |     |     |     |     | X   | [? ? ]. |
| ------------------------------------------------ | --- | --- | --- | --- | --- | --- | ---------------------------------------- | --- | --- | --- | --- | --- | --- | ------- |
| tification,allowingonetoassessbothwhetherachange |     |     |     |     |     |     |                                          |     |     |     |     |     | 1:T |         |
occurrned. The change times τ 1 ,...,τ K are explicitly modeled as
| occurred | and | when it |     | It  | enables | the prin- |     |     |     |     |     |     |     |     |
| -------- | --- | ------- | --- | --- | ------- | --------- | --- | --- | --- | --- | --- | --- | --- | --- |
latentvariables,withpriordistributionsspecifyingboth
| cipled incorporation                       |                 | of prior       | knowledge |       | about         | regime     |                                                    |      |             |     |                  |             |            |     |
| ------------------------------------------ | --------------- | -------------- | --------- | ----- | ------------- | ---------- | -------------------------------------------------- | ---- | ----------- | --- | ---------------- | ----------- | ---------- | --- |
|                                            |                 |                |           |       |               |            | the number                                         |      | of segments |     | K and            | the typical | duration   | of  |
| persistence—such                           |                 | as preferences |           | for   | rare          | changes or |                                                    |      |             |     |                  |             |            |     |
|                                            |                 |                |           |       |               |            | regimes.Intermsofdatadistribution,itisassumedthat, |      |             |     |                  |             |            |     |
| long-lasting                               | regimes—through |                |           | prior | distributions | on         |                                                    |      |             |     |                  |             |            |     |
|                                            |                 |                |           |       |               |            | within                                             | each | segment     | k,  | an approximately |             | stationary |     |
| P(changeatt|r)andonttheregimeparametersP(θ |                 |                |           |       |               | ).         |                                                    |      |             |     |                  |             |            |     |
|                                            |                 | t              |           |       |               | r          |                                                    |      |             |     |                  |             |            |     |
Schematically,wnecangroupthesemethodsintothree distribution generates the data, and that the task is to
|                   |     |                   |        |           |     |         | inferP(τ |      | ,K,θ          | | X | ).           |     |           |     |
| ----------------- | --- | ----------------- | ------ | --------- | --- | ------- | -------- | ---- | ------------- | --- | ------------ | --- | --------- | --- |
| main subfamilies: |     | (a)               | online | detection | via | BOCPD   |          | 1:K  | 1:K           | 1:T |              |     |           |     |
|                   |     |                   |        |           |     |         | Given    | this | probabilistic |     | formulation, |     | inference | can |
| and extensions;   |     | (b) retrospective |        | Bayesian  |     | segmen- |          |      |               |     |              |     |           |     |
iregime-switching (HMM/MS- be performed either by maximum a posteriori (MAP)
| tation; and                             | (c) |     |     | models |     |     |             |     |          |          |           |     |           |        |
| --------------------------------------- | --- | --- | --- | ------ | --- | --- | ----------- | --- | -------- | -------- | --------- | --- | --------- | ------ |
|                                         |     |     |     |        |     |     | estimation, |     | yielding | a single | “optimal” |     | partition | τ , or |
| VAR)withBrayesianfilteringandsmoothing. |     |     |     |        |     |     |             |     |          |          |           |     |           | k      |
byMCMC-basedsampling,whichproducesadistribu-
BOCPD p and online detection via run-length. In tion over possible segmentations and credibility inter-
|          |        |             |     |           |         |     | vals | for each | transition | date. | In  | both cases, | the | result |
| -------- | ------ | ----------- | --- | --------- | ------- | --- | ---- | -------- | ---------- | ----- | --- | ----------- | --- | ------ |
| Bayesian | Online | Changepoint |     | Detection | (BOCPD) | [?  |      |          |            |       |     |             |     |        |
], the time series is modeled as a sequence of approxi- isaBayesiancharacterizationoftheregimestructureof
e
P(X)overtime,withuncertaintyexplicitlyquantified.
matelystationarysegmentsseparatedbylatentchange-
points, with the run-length r—the number of observa- This explicit treatment of uncertainty makes these
t
rtionssincethelastchangepoint—servingasthehidden models particularlyappealing infinancial applications,
wherethegoalisoftentoreconstructhistoricalregimes
| state. Ateachnewobservation |     |     |     | x, thealgorithmrecur- |     |     |     |     |     |     |     |     |     |     |
| --------------------------- | --- | --- | --- | --------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| P                           |     |     |     | t                     |     |     |     |     |     |     |     |     |     |     |
sivelyupdatestheposteriordistribution ex post—such as bull and bear markets, high- and
|     |     |     |     |     |     |     | low-volatility |     | periods, | or  | episodes | of  | policy interven- |     |
| --- | --- | --- | --- | --- | --- | --- | -------------- | --- | -------- | --- | -------- | --- | ---------------- | --- |
|
p(r t x 1:t ) tion—while accounting for ambiguity in the precise
22
This preprint research paper has not been peer reviewed. Electronic copy available at: https://ssrn.com/abstract=6170273

d
e
timingofregimeboundariesfortherelevantdistribution
P(X)(e.g.,returns,volatilities,worspreads).
Concrete instances of this class include the partition
Algorithm 3: BOCPD: Bayesian Online
models of Barry–Hartigan [? ], which place priors di-
ChangepointDetection
rectly over partitions of the time series into approxi-
Input:Datastreamx ,x ,...;predictivelikelihood e
1 2 mately stationary blocks and derive the corresponding
p(x |r ,x );hazardfunctionH(r);max
t t−1 1:t−1 posterior distribution. Related algorithms developed
run-lengthR (optional)
max by Fearnhead and collaborators [? ] exploit dynamic
Output:Run-lengthposteriorp(r |x )ateachtime i
t 1:t programming or forward-type recursions to compute
t;changepointprobabilities v
the joint distribution over the number and locations of
1 p(r 0 =0)←1; // Initialize: run-length is changepoints,P(τ | X ).Whileexactinferencetyp-
0 icallyincurs e acom 1 p :K utati 1 o : n T alcostofO(T2),resampling-
2
fort=1,2,...do
basedvariants,suchasparticlefilters,provideapproxi-
// Compute predictive probability for matesolutionswithnear-O(T)complexity.
each run-length r
3 forr=0tomin(t−1,R max )do Regim e-switchingmodels(HMM,MS-VAR). Finally,
4 π( t r)← p(x t |r,x 1:t−1 ); // Likelihood regime-switching models—most notably Hidden
under run r r
MarkovModels(HMMs)andMarkov-switchingVARs
5 end
e(MS-VARs)—model regime changes through an unob-
// Growth probabilities: no served discrete-state process S T . At each time t, the
changepoint at t
tt=1
latent state S ∈ 1,...,R represents the active regime
6 forr=1tomin(t,R max )do e and evolves a t ccording to a first-order Markov chain,
7 p(r t =r|x 1:t )∝π( t r−1)·p(r t−1 =r−1| governingthemodelparametersineachperiod[? ? ].
x )·(1−H(r−1))
1:t−1
AclassicalexampleisHamilton’smodel[? ],which
8 end p
assumes that X | S = r ∼ P(X | θ ). In this set-
t t t r
// Changepoint probability: reset to
ting,theseriesfollowsanautoregressiveprocesswhose
r=0
9 p(r t =0|x 1:t )∝ (cid:80)m r= i 0 n(t−1,Rmax)π( t r)·p(r t−1 = r| c a o n e d ffi ea c c ie h nt s s ta a t n e d r /o c r o i r n r t e e s r p c o e n p d ts s d to ep a en re d g o im n e th c e h l a a r t a e c n t t e s r t i a z t e e d ,
x )·H(r) t
1:t−1
by specific mean, volatility, and correlation patterns.
// Normalize posterior o In multivariate extensions (MS-VAR), P(X | S = r)
10 Z t ← (cid:80)m r= i 0 n(t,Rmax)p(r t =r|x 1:t ) jointly captures regime-dependent autoreg t ressiv t e dy-
11 p(r t |x 1:t )← p(r t |x 1:t )/Z t n namicsandcovariancestructures.
// Changepoint alarm (optional) Inference in these models is typically Bayesian and
12 if p(r t =0|x 1:t )>θ alarm then combinesfilteringandsmoothingprocedures—suchas
13 Signal:Changepo intdetectedattimet the forward–backward algorithm—to estimate p(S |
t
14 end t x 1:T ) and p(S t ,S t+1 | x 1:T ), together with parameter
// Update sufficient statistics for estimation via MCMC or variational methods. This
n
each run-length (model-dependent) yieldsposteriordistributionsforboththetransitionma-
15 Updateposteriorparametersfor p(θ r |x 1:t )for trix P(S t+1 | S t ) and the regime-specific parameters θ r
16 end eachr i definingP(X |S t =r).
From a change detection perspective, regime-
r
17 Complexity:O(n2)withouttruncation;O(nR max )with switching models can be employed online, by moni-
truncationatR
pmax toring changes in state probabilities or transition like-
18 H g a a z p a s r ) d ;H fu ( n r) ct = io 1 n / : (r H + (r 1 ) ) = (i 1 n / c λ re ( a c s o in n g s ) tant,geometric lihoods, and off-line, to reconstruct historical regimes
and infer the most likely change dates. Their ability
19eLikelihood:Conjugatepairs(Normal-Normal,
Poisson-Gamma)enableclosed-formupdates to jointly model multiple variables and complex de-
20 Typicaluse:Onlinedetectionwithuncertainty pendence structures makes MS-VARs particularly well
rquantification;gradualdrifts;regimemodels suited for multivariate financial series, where regime
21 References:[???] changes often involve simultaneous shifts in means,
P volatilities,andcorrelations—i.e.,structuralchangesin
P(X).
In summary, Bayesian regime-switching methods
23
This preprint research paper has not been peer reviewed. Electronic copy available at: https://ssrn.com/abstract=6170273

d
e
provide a unified framework for regime detection and ? ? ? ? ]. Inmultivariatefinancialapplications,embed-
modeling, with explicit uncertainty quantification and dingslearnedbytransformersworgraphneuralnetworks
theabilitytoincorporatepriorinformation, suchasas- are often combined with classical detectors—such as
sumptionsaboutregimepersistenceorplausibleparam- kNN,kerneldensityestimation,MMDtests,orstandard
etervalues. Atthesametime,theircomputationalcost CPD methods applied in latent space—to handle com-
e
and sensitivity to modeling choices—such as the num- plextemporalandcross-sectionaldependencies[? ? ?
| ber of regimes, |     | transition | priors, | and | likelihood | spec- | ? ? ? | ].  |     |     |     |     |     |
| --------------- | --- | ---------- | ------- | --- | ---------- | ----- | ----- | --- | --- | --- | --- | --- | --- |
ification—require careful consideration, especially in In finance, embeddiing- and OOD-based detectors
high-dimensionalfinancialsettings. areespeciallyusefulforidentifyinggenuinelyunprece-
v
|     |     |     |     |     |     |     | dented | situations, | where | patterns | of  | co-movement, | liq- |
| --- | --- | --- | --- | --- | --- | --- | ------ | ----------- | ----- | -------- | --- | ------------ | ---- |
4.4. DetectioninEmbeddingsandOOD
uidity,orvolatilitydeviatefromallpreviouslyobserved
e
Thisfamilyofapproachesdetectschangesbymoni- regimes. T heir effectiveness, however, depends criti-
toringhowdatapointsevolveinarepresentation,orla- callyonthequalityofthelearnedrepresentation. When
tentfeature,space. Insteadofoperatingdirectlyonthe theembeddingcaptureseconomicallymeaningfulstruc-
r
rawobservations,theideaistofirsttransformtheseries ture,changesinP(Z)reliablysignalchangesinP(X)or
intoasequenceoflatentvectorsandthentrackchanges P(X,Y ). Whenitdoesnot,thesemethodsmayconfuse
intheirdistributionovertime. Inpractice, thisisoften minorfluctuationswithtruenovelty.
r
framedasanomalyorout-of-distribution(OOD)detec-
e
tioninstreamingsettings. 4.5. MultivariateStructuralDependenceMethods
| Formally, | a   | representation |     | mapping | Z = | f(X) or |     |     |     |     |     |     |     |
| --------- | --- | -------------- | --- | ------- | --- | ------- | --- | --- | --- | --- | --- | --- | --- |
Z = f(X,Y)islearnedfromtheobservedseries X and, Finally, we highlight methods aimed at detecting
e
when available, from covariates Y. At each time t, a regimechangesthatarisefromshiftsinthejointbehav-
latent vector z = f(x ) or z = f(x ,y ) sum- ior of multiple variables. Instead of focusing on uni-
|         | t      | t−k:t        |         | t   | t−k:t           | t−k:t |         |           |         |               |     |                  |     |
| ------- | ------ | ------------ | ------- | --- | --------------- | ----- | ------- | --------- | ------- | ------------- | --- | ---------------- | --- |
|         |        |              |         |     |                 |       | variate | marginals | P(X(i)) | in isolation, |     | these approaches |     |
| marizes | recent | observations | through | a   | slidingpwindow. |       |         |           |         |               |     |                  |     |
A regime change is then interpreted as a shift in the operatedirectlyonthemultivariatedistribution
| induceddistribution |     | P(Z),whichreflectsanunderlying |     |     |     |     |     |     |     |     |     |     |     |
| ------------------- | --- | ------------------------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
(cid:0) X(1),...,X(d)(cid:1)
|                                                  |     |           |         |          |           |        |      |     | P(X)=          | P    |         | ,                |     |
| ------------------------------------------------ | --- | --------- | ------- | -------- | --------- | ------ | ---- | --- | -------------- | ---- | ------- | ---------------- | --- |
| changeinP(X)orP(X,Y)[?                           |     |           | ?       | ? ? ? ]. |           |        |      |     |                |      |         |                  |     |
| A simple                                         | and | intuitive | example | is       | prtovided | by au- |      |     |                |      |         |                  |     |
|                                                  |     |           |         |          |           |        | Here | X   | = (X (1),...,X | (d)) | denotes | the multivariate |     |
| toencodersorotherunsupervisedmodelstrainedonhis- |     |           |         |          |           |        |      | t   | t              | t    |         |                  |     |
|                                                  |     |           |         | o        |           |        |      |     |                |      |         | X(i)             |     |
torical data. These models learn a notion of “normal” observation at time t, with each component repre-
t
dynamics for the series. As new observations arrive, sentingadistinctvariableofinterest,suchasthereturn
reconstruction errors or anomnaly scores are computed. ofanasset,ariskfactor,oraliquiditymeasure. Regime
Whenthesescoresincreasepersistently,thecurrentdata changes are then modeled as alterations in the depen-
|           |          |     |          |               |     |            | dence | structure | of the | joint distribution, |     | which | may be |
| --------- | -------- | --- | -------- | ------------- | --- | ---------- | ----- | --------- | ------ | ------------------- | --- | ----- | ------ |
| no longer | resemble | the | training | distribution, |     | indicating |       |           |        |                     |     |       |        |
that the process generatin g X—and therefore Z—has reflected,forinstance,inchangesinthecovariancema-
| changed. |     |     |     |     |     |     | trixΣ | =Cov(X | ),thecorrelationmatrixR |     |     | ,acopulaC |     |
| -------- | --- | --- | --- | --- | --- | --- | ----- | ------ | ----------------------- | --- | --- | --------- | --- |
|          |     |     | t   |     |     |     |       | t      | t                       |     |     | t         | t   |
Beyond reconstruction-based signals, changes can linkingthemarginaldistributions,orinthetopologyof
n
also be detected directly in the latent space. One ap- a dependence graph (graphical model) associated with
|           |           |           |     |         | P(Z) |            | P(X). |     |     |     |     |     |     |
| --------- | --------- | --------- | --- | ------- | ---- | ---------- | ----- | --- | --- | --- | --- | --- | --- |
| proach is | to define | reference |     | regions |      | associated |       |     |     |     |     |     |     |
with known regiimes, for instance, through contrastive One example involves algorithms for detecting
learning or rclustering. A regime transition is then changes in the covariance matrix or in the graph of
detected when latent states drift away from these re- a graphical model. Typically, we compare P baseline
gions opr move closer to others. Related methods com- andP (X)viastatisticsthatsummarizetheirdepen-
recent
pare distributions in representation space across time dence: forexample,testsforequalityofcovariancema-
|          |       |            |     |               |     |          | tricesΣ |          | vs.Σ   | ,orstatisticsofmaximaldiffer- |     |     |     |
| -------- | ----- | ---------- | --- | ------------- | --- | -------- | ------- | -------- | ------ | ----------------------------- | --- | --- | --- |
| windows, | using | tools such | as  | density-ratio | or  | density- |         |          |        |                               |     |     |     |
| e        |       |            |     |               |     |          |         | baseline | recent |                               |     |     |     |
difference estimation, to explicitly test whether P(Z) it enceincorrelationcoefficientsρ overtime. Inthisdi-
ij
haschanged[? ? ? ? ? ? ]. rection,methodssuchasICSS[? ],MOSUM[? ],and
rThisgeneralideanaturallyextendstoawiderangeof PELTextensionsforthecovariancematrix(PELT–Σ)[?
deepOODtechniques. Theseincludeenergy-basedde- ] monitor breaks in univariate variance and, in multi-
| P   |     |     |     |     |     |     | variateversions,injointvariance/covariance,beinguse- |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ---------------------------------------------------- | --- | --- | --- | --- | --- | --- |
tectors,one-classandDeep-SVDDmethods,generative
models that estimate latent densities, and uncertainty ful for identifying volatility and co-movement regime
| monitoring | in Bayesian |     | or ensemble | networks |     | [? ? ? | changes[? |     | ? ]. |     |     |     |     |
| ---------- | ----------- | --- | ----------- | -------- | --- | ------ | --------- | --- | ---- | --- | --- | --- | --- |
24
This preprint research paper has not been peer reviewed. Electronic copy available at: https://ssrn.com/abstract=6170273

d
e
Building on this idea, several methodological lines jointextremeevents.Similarly,historicallystablehedge
havebeendeveloped. Onthesequentialside,multivari- relationships may deteriorate owr invert sign, translating
ateversionsoftheCUSUMofsquares[? ? ] monitor into localized changes in Σ and R and into increased
t t
sumsofsquares(oraggregatedportfoliostatistics)over residualvolatilityoflong–shortstrategies.
| time to detect | changes | in joint | volatility | [? ? | ]. An- |     |     |     |     |     |     |     |
| -------------- | ------- | -------- | ---------- | ---- | ------ | --- | --- | --- | --- | --- | --- | --- |
e
otherlinefocusesontechniquesfordetectingchangesin 4.6. ChangeDetectionOverview
copulasC,whichdescribeexclusivelythedependence
t
structure between variables, decoupled from marginals This overview is anchored by three complementary
i
|            |           |      |               |         |      | summaries. |     | Together, | Table 6, | Figure | 15, and | Table 7 |
| ---------- | --------- | ---- | ------------- | ------- | ---- | ---------- | --- | --------- | -------- | ------ | ------- | ------- |
| F. In this | case, the | idea | is to compare | an old” | cop- |            |     |           |          |        |         |         |
| i          |           |      |               |         |      |            |     | v         |          |        |         |         |
ulaC withanew”copulaC andtestwhether mapthetypeofchangeofinteresttosuitabledetection
| baseline |     |     | recent |     |     |     |     |     |     |     |     |     |
| -------- | --- | --- | ------ | --- | --- | --- | --- | --- | --- | --- | --- | --- |
methods,practicalselectioncriteria,andtheircomputa-
| therehasbeenachange,includingintailregions[? |     |     |     |     | ?   | ?   |     |     |     |     |     |     |
| -------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
tionalfeasibeility.
? ? ? ].
Some parametric methods assume Gaussian graphi- Table 6 serves as the primary entry point. It maps
|                               |     |     |                   |     |     | different | change | axes—temporal, |     | statistical, |     | structural, |
| ----------------------------- | --- | --- | ----------------- | --- | --- | --------- | ------ | -------------- | --- | ------------ | --- | ----------- |
| calmodelsorrelatedstructures. |     |     | Anexampleistheuse |     |     |           |        |                |     |              |     |             |
r
of (possibly adaptive) Graphical Lasso to estimate, in andontological—toindicativemethodfamiliesandcon-
|              |             |        | Θ   | = Σ−1        |     | crete financial |     | examples. | For | instance, | abrupt | tem- |
| ------------ | ----------- | ------ | --- | ------------ | --- | --------------- | --- | --------- | --- | --------- | ------ | ---- |
| each window, | a precision | matrix | t   | t associated |     |                 |     |           |     |           |        |      |
withaconditionalindependencegraphG [? ]. Inthis poral changes suggest segmentation or CUSUM-type
|     |     |     |     | t   |     | r   |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
context,monitoringchangesindependenceamountsto methods, while shifts in dependence structures point
|                      |     | orΘ. |     |     |     | etoward | covariance-, | copula-, |     | or graph-based |     | detectors. |
| -------------------- | --- | ---- | --- | --- | --- | ------- | ------------ | -------- | --- | -------------- | --- | ---------- |
| monitoringchangesinG |     | t    | t   |     |     |         |              |          |     |                |     |            |
Other methods avoid strong parametric assumptions Thiscompactviewallowsthepractitionertostartfrom
and compare multivariate dependence measures con- the phenomenon of interest (e.g., contagion, regime
|     |     |     |     |     | e   | changes, | beta | instability) | and | narrow | the methodolog- |     |
| --- | --- | --- | --- | --- | --- | -------- | ---- | ------------ | --- | ------ | --------------- | --- |
structeddirectlyfromthedata,suchasdistancematrices
D(X) or kernel matrices K(X) [? ], using multivariate icalspaceaccordingly.
|                      |     |       |         |              |       | Figure | 15  | operationalizes |     | this mapping |     | as a deci- |
| -------------------- | --- | ----- | ------- | ------------ | ----- | ------ | --- | --------------- | --- | ------------ | --- | ---------- |
| Friedman–Rafsky-type |     | tests | [? ] or | graph-bapsed | vari- |        |     |                 |     |              |     |            |
ants (MST, k-NN graph) [? ? ] to assess whether two sion tree. Starting from label availability, it guides
samplesoriginatefromthesamejointdistributionP(X). methodselectionthroughasequenceofpracticalques-
OntheBayesianside,BOCPDextensions tailoredto tionsaboutdimensionality,operationalobjective,usage
context(onlinevs.offline),andscaleofconcern.
| detecting     | changes | in structural | dependetnce | have          | also |      |            |          |            |     |            | Inthis    |
| ------------- | ------- | ------------- | ----------- | ------------- | ---- | ---- | ---------- | -------- | ---------- | --- | ---------- | --------- |
|               |         |               |             |               |      | way, | the figure | connects | conceptual |     | choices    | to imple- |
| been proposed | [?      | ? ? ?         | ? ]. In     | these models, | the  |      |            |          |            |     |            |           |
|               |         |               | o           |               |      |      |            |          |            |     | trade-offs |           |
dependence structure (for example, a graphG or a pa- mentable detector families, highlighting be-
rametersetΘencodingtheedges)istreatedaslatentand tweensupervision,sensitivity,andinterpretability.
evolvingbyregimes,andinfernencefocusesondetecting A complementary decision concerns the representa-
abruptswitchesinthisstructureovertime. tion space in which change is monitored. As summa-
|        |            |             |         |       |         | rized | in Table | 6 and | operationalized |     | in Figure | 15, de- |
| ------ | ---------- | ----------- | ------- | ----- | ------- | ----- | -------- | ----- | --------------- | --- | --------- | ------- |
| From a | structural | standpoint, | methods | based | on cor- |       |          |       |                 |     |           |         |
relationmatrices,copulas,o rgraphicalmodelsinterpret tectors may act on raw series, on hand-crafted finan-
these events as rearrangtements in the dependence net- cial features, or on learned embeddings, depending on
work [? ? ? ? ]. This perspectiveis particularly rele- dimensionality and interpretability requirements. This
n
vantinfinancialapplications, wherestructuralchanges choicedetermineswhetherchangesaredetecteddirectly
inobservablequantities(e.g.,returnsorcorrelations)or
| tend to manifest | more | strongly | in the | relationships | be- |     |     |     |     |     |     |     |
| ---------------- | ---- | -------- | ------ | ------------- | --- | --- | --- | --- | --- | --- | --- | --- |
tween variablesithan in each series taken individually. indirectlythroughshiftsinlatentmultivariatepatterns.
Indistributiornalterms,thismeansthatchangesinP(X) Finally,Table7constrainsthesechoicesfromacom-
are often driven primarily by shifts in its dependence putational perspective. It highlights how method fam-
componpent,whilethemarginalsP(X(i))mayremainrel- ilies differ in time and memory complexity as a func-
ativelystable. tion of series length, dimensionality, and model struc-
Importantly, such changes can often be detected be- ture. Thiscomparisonisessentialinhigh-frequencyor
e
foreanyunivariatemodelsignalsinstability,sinceindi- high-dimensional settings, where theoretically appeal-
vidualseriesmayremainwithintypicalvariationranges ingmethodsmaybeimpracticalwithoutdimensionality
rwhilethejointdependencestructurebecomesunprece- reductionortruncationstrategies.
dented[? ? ? ? ? ]. Forinstance,acontagionregime Taken together, these complements transform the
P
maynotbeevidentwheninspectingindividualassetre- broadtaxonomyofchangedetectionintoapracticalse-
turns,butitbecomesclearwhencorrelationsrisecollec- lectionframework:fromidentifyingtherelevantchange
tivelyorwhenthetailcopulaconcentratesmoremasson axis, to choosing an appropriate method family, repre-
25
This preprint research paper has not been peer reviewed. Electronic copy available at: https://ssrn.com/abstract=6170273

d
e
Time-varyingparameters(TVP/state-space)
| sentation | space, and | control | mechanism, |     | all while re- | 5.1.1. |     |     |     |     |     |
| --------- | ---------- | ------- | ---------- | --- | ------------- | ------ | --- | --- | --- | --- | --- |
spectingcomputationalconstraints. Time-varying-parameter(TVwP)modelsaddressnon-
coefficients
|     |     |     |     |     |     | stationarity    | by allowing | model     |               | themselves   |          |
| --- | --- | --- | --- | --- | --- | --------------- | ----------- | --------- | ------------- | ------------ | -------- |
|     |     |     |     |     |     | to change       | over time.  | Instead   | of estimating |              | a single |
|     |     |     |     |     |     | fixed parameter | vector,     | the model | treats        | coefficients | as       |
5. AdaptationandContinualLearning
e
evolvingquantitiesthatareupdatedasnewdataarrive,
|              |           |     |              |     |               | typically | through a state-space |     | formulation | [?  | ? ? ]. |
| ------------ | --------- | --- | ------------ | --- | ------------- | --------- | --------------------- | --- | ----------- | --- | ------ |
| This section | addresses |     | the research |     | question: How |           |                       |     |             |     |        |
Thisperspectivenaturaillyleadstoregressionmodelsin
canweadaptmodellearningtodatadistributionshifts
whichparametersvfollowanexplicitevolutionequation.
effectively?
| continuously | and |     | The | focus | is on strate- |     |     |     |     |     |     |
| ------------ | --- | --- | --- | ----- | ------------- | --- | --- | --- | --- | --- | --- |
gies that enable learning systems to react to evolving =β⊤x +ε,
|     |     |     |     |     |     |     | y t | t   | t   |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|     |     |     |     |     |     |     | e   | t   |     |     |     |
datadistributionsinordertosustainorimproveperfor-
mance in non-stationary environments, with particular inwhichβ followsanevolutionequationβ =β +u
|                                    |     |     |     |      |     |           | t              |      |                  | t   | t−1 t  |
| ---------------------------------- | --- | --- | --- | ---- | --- | --------- | -------------- | ---- | ---------------- | --- | ------ |
| relevancetofinancialapplications[? |     |     |     | ? ]. |     |           |                |      |                  |     |        |
|                                    |     |     |     |      |     | (a random | walk, possibly | with | some structure). |     | In fi- |
r
The discussion is organized around the main nance, this is applied to dynamic market betas (betas
thatc hangeovertime)andotheradaptiveregressionco-
| paradigms | for continuous |     | adaptation. |     | We begin |     |     |     |     |     |     |
| --------- | -------------- | --- | ----------- | --- | -------- | --- | --- | --- | --- | --- | --- |
efficients.
| with parametric | adaptation |     | methods | that | incorporate |     |     |     |     |     |     |
| --------------- | ---------- | --- | ------- | ---- | ----------- | --- | --- | --- | --- | --- | --- |
r
change mechanisms directly into statistical models EstimationistypicallycarriedoutusingtheKalman
efilter
(5.1).Wethenexaminedynamicensemblesandregime- or its extensions (for linear-Gaussian cases) or
specialized models that adaptively activate or reweight through online optimization methods for more general
learners across regimes (5.2). Next, we cover hybrid cases [? ? ? ]. The Kalman filter directly provides
|     |     |     |     |     | e   |     | coefficient |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ----------- | --- | --- | --- | --- |
adaptationflowsthatcombineexplicitchangehandl ing recursive updates as new data arrive, using
with model updating (5.3). Finally, we discuss recent atransitionmodelthatpenalizesoverlyabruptchanges
|     |     |     |     |     |     |     |     |     | Q   | u   |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
approachesbasedoncontinuallearning,test-timpeadap- (through the variance matrix of the term t ). This
tation,andmeta-learning,whichaimtoenablerapidand yieldsanoptimizedadaptiveforgetting:ifthedataindi-
data-efficientadaptation(5.4)[? ? ]. catethatβischanging,thefilteradjusts;ifnot,itkeeps
To synthesize these perspectives, Table 8 provides a it stable. In many cases, this “smooth” layer of adapt-
structuredcomparisonofadaptationmethtodsacrosskey ability responds adequately to incremental or gradual
drifts,reservingmoreradicalinterventions(suchasre-
operationaldimensions,servingasapracticalguidefor
o
methodselectionunderdifferentapplicationconstraints. setsormodelswitches)formomentsofclearstructural
|                |            |     |             | trade-off |         | break. |     |     |     |     |     |
| -------------- | ---------- | --- | ----------- | --------- | ------- | ------ | --- | --- | --- | --- | --- |
| This synthesis | highlights |     | the central |           | between |        |     |     |     |     |     |
stabilityandplasticitythatchanracterizesadaptivelearn- Forexample,supposeastock’ssensitivitytoamarket
ing in finance: overly aggressive adaptation may am- factor slowly increases over several months — a TVP
|             |                 |     |        |         |              | model with | Kalman filtering |     | will gradually |     | raise the |
| ----------- | --------------- | --- | ------ | ------- | ------------ | ---------- | ---------------- | --- | -------------- | --- | --------- |
| plify noise | and transaction |     | costs, | whereas | conservative |            |                  |     |                |     |           |
updates risk sustained per   formance degradation after estimated beta, tracking the change without ever hav-
|                |     |                |     |       |               | ing to explicitly | declare | a one-shot | “regime |     | change”. |
| -------------- | --- | -------------- | --- | ----- | ------------- | ----------------- | ------- | ---------- | ------- | --- | -------- |
| regime changes | [?  | ? ].tTogether, |     | these | elements con- |                   |         |            |         |     |          |
nectadaptationstrategiestotheirpracticalimplications Thisavoidslosingaccumulatedinformationandensures
n
inreal-worldnon-stationarysystems. smoothness. However, if an abrupt shock drastically
changesβ,theTVPmodelwilltakeafewstepstofully
|     | i   |     |     |     |     | adjust (unless | one temporarily |     | increases | the | transition |
| --- | --- | --- | --- | --- | --- | -------------- | --------------- | --- | --------- | --- | ---------- |
5.1. Parametricadaptationapproaches varianceQatthatinstant,whichisequivalenttodetect-
r
|         |              |     |             |       |            | ing and     | nearly resetting | — hence | the | interaction | with |
| ------- | ------------ | --- | ----------- | ----- | ---------- | ----------- | ---------------- | ------- | --- | ----------- | ---- |
| Withpin | this family, | we  | distinguish | three | main para- | detectors). |                  |         |     |             |      |
metric strategies according to how change is repre- In summary, TVP and state-space models provide a
sented in the model. The first relies on continuously formof“built-incontinuousadaptation,”especiallyuse-
e
evolvingparameters,typicallyformulatedinstate-space fulwhenweexpectparameterstomoveslowly.Infinan-
form(5.1.1).Thesecondintroducesregimedependence cial time series, there is broad application: stochastic-
rthrough observable drivers via threshold or smooth- volatility models with time-varying parameters, macro
transition mechanisms (5.1.2). The third assumes a fi- VARmodelswithvaryingcoefficients,dynamicCAPM
P
nite set of discrete latent regimes, with probabilistic models, and so on [? ? ]. They tend to preserve eco-
switching dynamics captured by regime-switching and nomic interpretability (e.g., one can track how a given
coefficientevolvesandrelateittomarketconditions).
HiddenMarkovmodels(5.1.3).
26
This preprint research paper has not been peer reviewed. Electronic copy available at: https://ssrn.com/abstract=6170273

d
e
Start
w
ArelabelsYavailable?
|     |     |     |     |     | No  |     | Yes |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
e
|     |     |     | No(focuson∆P(X)) |     |     |     |     | Yes(focuson∆P(Y),∆P(Y|X)) |     |     |     |
| --- | --- | --- | ---------------- | --- | --- | --- | --- | ------------------------- | --- | --- | --- |
i
H i g h d i m e n s i o n
|     |     |      | L o w d i m e n s i o n    |        | ( p ≥ 1 0 )                             |     | G o a l   | : F a s t a l a r m  | G o a l : R e g i m e d a t i n  | g     |     |
| --- | --- | ---- | -------------------------- | ------ | --------------------------------------- | --- | --------- | -------------------- | -------------------------------- | ----- | --- |
|     |     |      | ( p < 1 0 )                |        | ⇒ E m b e d d i n g s                   |     | ⇒D D M /  | E D D M / E C DD, v⇒ | S eg m e n t a t i o n ( S e c . | 4 .1) |     |
|     |     | ⇒Seg | m e n t a t io n / C U SUM | + M    | M D / E n e r g y o r o t h e r         |     | L os s -b | a s e d C U S U M    | + B O C P D / H M M              |       |     |
|     |     |      | (S e c s . 4 . 1 - 4 . 2 ) | +O O D | /n o v e l t y i n l a t e n t s p a ce |     | (         | S e c . 4 . 2 )      | R e g i m e m o d e ls           |       |     |
|     |     |      |                            |        | ( S e c . 4 . 4 )                       |     |           |                      | ( S e c . 4 . 3 )                |       |     |
e
Usagecontext?
r
|     |     |     |     | E x | p o s t |     |  (quas | O i n re l a in l- e time) |     |     |     |
| --- | --- | --- | --- | --- | ------- | --- | ------ | -------------------------- | --- | --- | --- |
(backtestin g, h is t o ricalstudy)
|     |     |     |     | ⇒S e g | m e n ta tion |     | + ⇒    | S e q u e n t i a l (S e c . 4 . 2 )                                        |     |     |     |
| --- | --- | --- | --- | ------ | ------------- | --- | ------ | --------------------------------------------------------------------------- | --- | --- | --- |
|     |     |     |     | (S e c | . 4 .1 )      |     | rvi as | o e c g c m as e i n o t n a a t l io r n e fi ( n S e e m c . e 4 n . t 1) |     |     |     |
e
Scaleofconcern?
Global/Systemic
eLocal/Sectoral
|     |     |     |     | ⇒A g g r e g a t e s e r i                     | e s / s y s t e m i c f a c tors                         |     | ⇒   | R u n b y c l u s t e r / s e c t or; |     |     |     |
| --- | --- | --- | --- | ---------------------------------------------- | -------------------------------------------------------- | --- | --- | ------------------------------------- | --- | --- | --- |
|     |     |     |     | s ( e b e ro a a l s d o m s t a r r u k c e t | t u , r s a y l s d t e e p m e i n c d r e is n k c ; e |     |     | A g g r e g a t e a la r m s          |     |     |     |
|     |     |     |     | m e t h o d s                                  | , S e c . 4 . 5 )                                        |     |     | a f t e r w a r d s ( S e c . 4 . 5 ) |     |     |     |
Colorcoding:Start|Decision|Branch|Method|Context
p
Figure15: Decisiontreeforchoosingchange-detectionmethodfamilies. Theflowchartguidesmethodselectionbasedonlabelavailability,
dimensionality, operationalgoal, usagecontext, andscaleofconcern. Colorsdistinguishdecisionnodes(yellow), branchingpoints(orange),
recommendedmethods(green),andcontextualconsiderations(purple).

t
withdifferentmean-reversiondynamics.
| 5.1.2. Smooth-transition |     |     | and threshold |     | models |     |     |     |     |     |     |
| ------------------------ | --- | --- | ------------- | --- | ------ | --- | --- | --- | --- | --- | --- |
o
(TAR/STAR)
STAR(SmoothTransitionAutoregressive)models,in
| In some | applications, |     | changes in | behavior | are asso- |                                              |     |     |     |     |     |
| ------- | ------------- | --- | ---------- | -------- | --------- | -------------------------------------------- | --- | --- | --- | --- | --- |
|         |               |     |            |          |           | turn,implementthetransitioninacontinuousway: |     |     |     |     | pa- |
ciatedwithobservablevariabnlesthatindicatewhenthe
|     |     |     |     |     |     | rameters |     | are weighted | combinations | of two | (or more) |
| --- | --- | --- | --- | --- | --- | -------- | --- | ------------ | ------------ | ------ | --------- |
systemisoperatingunderdifferentconditions. Thresh- base regimes via a smooth function (typically logistic)
oldandsmooth-transitionmodelsbuildonthisideaby of the driver z [? ? ? ? ]. Thus, if z is in extreme
|     |     |     |     |     |     |     |     | t   |     | t   |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
allowing model parameters to change as a function of values, themodelapproximatesapureregime; inmid-
suchvariables,ratherthtanevolvingautonomouslyover
|     |     |     |     |     |     | range | values, | it is a mixture | of the | two. This | is useful |
| --- | --- | --- | --- | --- | --- | ----- | ------- | --------------- | ------ | --------- | --------- |
time. This resultsnin adaptation mechanisms in which forcapturinggradualchangesorsituationsinwhichthe
regimechangesaretriggeredbyexplicitdrivers. regime does not switch abruptly but as some indicator
In TAR models, one defines one or more thresholds deteriorates or improves. For example, a STAR model
i
|            |          |        |            |        |             | for | inflation: | as expected | inflation | gradually | moves |
| ---------- | -------- | ------ | ---------- | ------ | ----------- | --- | ---------- | ----------- | --------- | --------- | ----- |
| on a state | variable | (which | may be the | series | itself at a |     |            |             |           |           |       |
r
lag,oranothervariable)thatdeterminediscretechanges from X% to Y%, the monetary-policy regime (central
inthepparameters. Forexample, abilinearTARforre- bankreactionparameters)transitionssmoothly.
turns: ifthevariablez t−d (whichmaybealaggedreturn Thesemodelsallowustoincorporate,exante,knowl-
oramacroindicator)isbelowathresholdγ,weuseone
edgeaboutwhichvariablesignalsabehavioralchange.
seet
of parameters (µ 1 , ϕ 1 , etc.); if it is above, we use Infinance,thereareclearcases:forinstance,avolatility
| anotherset(µ | ,ϕ  | ).  |     |     |     |       |       |        |            |                       |     |
| ------------ | --- | --- | --- | --- | --- | ----- | ----- | ------ | ---------- | --------------------- | --- |
|              | 2   | 2   |     |     |     | model | whose | regime | depends on | an implied-volatility |     |
rThis results in deterministic regime switching: not indicator (VIX [? ]) — when VIX is high, differ-
stochastic as in an HMM, but governed by the driver entparametersapply. Oraconsumer-creditmodelthat
Pz.
A financial example is a price-momentum model in changes when the unemployment rate exceeds a given
which,ifashort-termreturnexceedsagiventhreshold, threshold. Byspecifyingthis,adaptationbecomesauto-
the system enters a high-volatility regime or a regime mated: themodelinstantlyadjustsitsparameterswhen
27
This preprint research paper has not been peer reviewed. Electronic copy available at: https://ssrn.com/abstract=6170273

d
e
Table6:Changeaxesandindicativemethods(compactview).
w
| Axis/feature |     |     | Typicalmethods |     |     |     | Illustrativefinancialexample |     |     |     |     |     |     |
| ------------ | --- | --- | -------------- | --- | --- | --- | ---------------------------- | --- | --- | --- | --- | --- | --- |
Temporal–abrupt Segmentation(PELT,Bai–Perron); Suddencrashinamarketindex
CUSUM
|                  |     |     | EWMA/GLR;BOCPDwithsmoothhazard |     |     |     |                    |     | e                |     |     |     |     |
| ---------------- | --- | --- | ------------------------------ | --- | --- | --- | ------------------ | --- | ---------------- | --- | --- | --- | --- |
| Temporal–gradual |     |     |                                |     |     |     | Slowtransitionfrom |     | bulltobearregime |     |     |     |     |
Statistical–∆P(X) E-Divisive,kernelCPD;ADWIN/KSWIN Sectorrotationinstockreturns
Statistical–∆P(Y|X) Regressionsegmentation;supervised Instabilityofbetasinafactormodel
i
CUSUM
Structure–Σ/dependence PELT–Σ;CUSUMofsquares;copulatests Increasein v correlationsduringcrises(contagion)
| Ontological–newclasses/regimes |     |     | BOCPD/HMM(recurrentregimes);OOD |     |     |     |     |     |     |     |     |     |     |
| ------------------------------ | --- | --- | ------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Newmarketregimes;unprecedentedevents
inembeddings
e
thedrivercrossesthethreshold(TAR),oradjustsgrad- observatrionmodels,thistransitionstructuredefinesthe
ually(STAR),withoutneedingtobere-estimatedfrom jointevolutionoflatentstatesandobservations.
scratch. Mo   del parameters and latent-state probabilities are
Thelimitationisobvious:onemustchoosethedriver tyrpically inferred using the Expectation–Maximization
and calibrate the threshold/transition function. If the (EM)algorithmorBayesianmethodssuchasMCMC[?
e
cause of regime change is not clear, these models may ? ? ]. Infinance, thesemodelsarewidelyapplied, for
notbeapplicable.However,whenthedriveriswellcho- example in Markov-switching GARCH and VAR for-
sen,theyofferrapidadaptation(virtuallywithoutdelay mulations [? ? ? ? ], where volatility or mean levels
e
if the driver is observed in real time) and usually sta- canshiftabruptlyacrossregimes.
bility within each regime, since each submodel can be In the adaptation context, latent-regime models act
calibratedforthatcontext. pproactively: they incorporate regime change in the
|     |     |     |     |     |     | model     | structure  | itself. | When    | a        | new            | regime | occurs, |
| --- | --- | --- | --- | --- | --- | --------- | ---------- | ------- | ------- | -------- | -------------- | ------ | ------- |
|     |     |     |     |     |     | the model | recognizes |         | it (via | filtered | probabilities) |        | and     |
5.1.3. Discretelatentstates(HMM/regime -switching)
switchestothecorrespondingparameterset,whichmay
| Anotherclassicalwayofmodelingstru |      |                     |     | cturalchange |          | differ    |           |        |              |     |        |            |       |
| --------------------------------- | ---- | ------------------- | --- | ------------ | -------- | --------- | --------- | ------ | ------------ | --- | ------ | ---------- | ----- |
|                                   |      |                     |     | t            |          |           | radically | from   | the previous |     | one.   | Thus, we   | avoid |
| is to assume                      | that | the data-generating |     | process      | switches |           |           |        |              |     |        |            |       |
|                                   |      |                     |     |              |          | “forcing” | a         | single | parameter    | set | across | the entire | his-  |
o
| between | a small | number of | distinct | regimes | over time. |     |     |     |     |     |     |     |     |
| ------- | ------- | --------- | -------- | ------- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- |
tory.
Inthisapproach,regimemembershipisnotdirectlyob-
|            |          |          |         |          |           | However, |     | a classical | HMM | with | a fixed | number | of  |
| ---------- | -------- | -------- | ------- | -------- | --------- | -------- | --- | ----------- | --- | ---- | ------- | ------ | --- |
| served but | inferred | from the | n data, | and each | regime is |          |     |             |     |      |         |        |     |
regimesKhasadaptivelimitations:itcanonlyalternate
| associatedwithitsownsetofparameters. |     |                  |     | Thisassump- |        |                                   |     |     |     |     |                  |     |     |
| ------------------------------------ | --- | ---------------- | --- | ----------- | ------ | --------------------------------- | --- | --- | --- | --- | ---------------- | --- | --- |
|                                      |     |                  |     |             |        | amongthoseKpre-estimatedpatterns. |     |     |     |     | Ifaqualitatively |     |     |
| tion underlies                       |     | regime-switching |     | and Hidden  | Markov |                                   |     |     |     |     |                  |     |     |
newregimeemerges,themodeldoesnotexplicitlyrep-
| models [? | ? ? | ? ]. Reg ime-switching |     |     | models with |        |            |     |            |     |            |      |        |
| --------- | --- | ---------------------- | --- | --- | ----------- | ------ | ---------- | --- | ---------- | --- | ---------- | ---- | ------ |
|           |     |                        |     |     |             | resent | it (unless | K   | was chosen |     | larger and | that | regime |
discretelatentstatesarearguablytheclassicalparamet-
|     |     | t   |     |     |     | occupies | one | of the | slots). | In other | words, | it  | handles |
| --- | --- | --- | --- | --- | --- | -------- | --- | ------ | ------- | -------- | ------ | --- | ------- |
ricapproachtostructuralbreaks.
|         |            | n        |                 |     |         | recurrences |     | of known | regimes | well | but | not truly | novel |
| ------- | ---------- | -------- | --------------- | --- | ------- | ----------- | --- | -------- | ------- | ---- | --- | --------- | ----- |
| In this | framework, | a latent | discrete-valued |     | process |             |     |          |         |      |     |           |       |
regimes.
| S ∈ {1,...,K} |     |     |     |     | t.  |     |     |     |     |     |     |     |     |
| ------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
t indicates the regime active at time Even so, within the set of modeled regimes, HMM
| ConditionalonSit |     | ,theobservedvariableisgeneratedby |     |     |     |            |     |         |           |     |              |           |     |
| ---------------- | --- | --------------------------------- | --- | --- | --- | ---------- | --- | ------- | --------- | --- | ------------ | --------- | --- |
|                  |     |                                   |     |     |     | adaptation |     | is fast | — as soon | as  | the filtered | probabil- |     |
aregime-spercificdistribution,witheachregimecharac-
|     |     |     |     |     |     | ity of | a new | state | exceeds, | say, | 0.5, the | model | essen- |
| --- | --- | --- | --- | --- | --- | ------ | ----- | ----- | -------- | ---- | -------- | ----- | ------ |
terizedbyitsownparameters(e.g.,means,variances,or
tiallyusesthatstate’sparameters,whichismuchfaster
| coefficipents). | Thisallowsthedata-generatingprocessto |     |     |     |     |                                     |     |     |     |     |     |              |     |
| --------------- | ------------------------------------- | --- | --- | --- | --- | ----------------------------------- | --- | --- | --- | --- | --- | ------------ | --- |
|                 |                                       |     |     |     |     | thanrecalibratingamodelfromscratch. |     |     |     |     |     | Moreover,the |     |
switchabruptlybetweendistinctparameterizations.
|     |     |     |     |     |     | Markov | structure |     | imposes | some | inertia | (e.g., | if Π is |
| --- | --- | --- | --- | --- | --- | ------ | --------- | --- | ------- | ---- | ------- | ------ | ------- |
ii
| A Hidden                                    | Markov | Model       | (HMM) | specifies    | the      |                                                  |        |                 |     |         |       |      |         |
| ------------------------------------------- | ------ | ----------- | ----- | ------------ | -------- | ------------------------------------------------ | ------ | --------------- | --- | ------- | ----- | ---- | ------- |
| e                                           |        |             |       |              |          | high,                                            | states | are persistent, |     | and the | model | does | not im- |
| regime dynamics                             |        | by assuming | that  | {S } follows | a first- |                                                  |        |                 |     |         |       |      |         |
|                                             |        |             |       | t            |          | mediatelyswitchback),whichpreventsreactingtoeach |        |                 |     |         |       |      |         |
| orderMarkovchainwithtransitionprobabilities |        |             |       |              |          | fluctuation.                                     |        |                 |     |         |       |      |         |
r
|     | P(S | = j|S | =i)=Π | ,   |     |      |                                         |     |     |     |     |     |     |
| --- | --- | ----- | ----- | --- | --- | ---- | --------------------------------------- | --- | --- | --- | --- | --- | --- |
|     |     | t     | t−1   | ij  |     |      |                                         |     |     |     |     |     |     |
| P   |     |       |       |     |     | 5.2. | Dynamicensemblesandregimespecialization |     |     |     |     |     |     |
whereΠencodesregimepersistenceandswitchingbe- No single model performs well across all regimes,
havior [? ? ]. Together with the regime-conditional particularly in non-stationary environments where
28
This preprint research paper has not been peer reviewed. Electronic copy available at: https://ssrn.com/abstract=6170273

d
e
Table7: Computationalcomplexityofchange-detectionmethods. n=serieslength, p=dimension,S =numberofstates(HMM),Rmax =run-
lengthtruncation(BOCPD),K=numberofchangepoints.
w
|     | Method |     | Time |     | Space | Real-time? |     | Scalability | Notes |     |     |     |     |
| --- | ------ | --- | ---- | --- | ----- | ---------- | --- | ----------- | ----- | --- | --- | --- | --- |
SequentialMethods(Section4.2)
|     | CUSUM        |     | O(n) |     | O(1) |     | Yes | High | Singleepass,constantmemory |     |     |     |     |
| --- | ------------ | --- | ---- | --- | ---- | --- | --- | ---- | -------------------------- | --- | --- | --- | --- |
|     | Page-Hinkley |     | O(n) |     | O(1) |     | Yes | High | VariantofCUSUM             |     |     |     |     |
|     | EWMA         |     | O(n) |     | O(1) |     | Yes | High | Exponentialsmoothing       |     |     |     |     |
|     | DDM/EDDM     |     | O(n) |     | O(w) |     | Yes | High | Windowsizew                |     |     |     |     |
i
|     | ADWIN      |     | O(nlogn) |                                 | O(logn) |     | Yes | Medium | Dynamicwindow              |     |     |     |     |
| --- | ---------- | --- | -------- | ------------------------------- | ------- | --- | --- | ------ | -------------------------- | --- | --- | --- | --- |
|     |            |     |          | SegmentationMethods(Section4.1) |         |     |     |        | v                          |     |     |     |     |
|     | BinarySeg. |     | O(nlogn) |                                 | O(K)    |     | No  | High   | Greedyapproximation        |     |     |     |     |
|     | PELT       |     | O(n)avg  |                                 | O(n)    |     | No* | Medium | O(n2)worst;pruningcritical |     |     |     |     |
e
O(n2)worst
|     | WBS        |     | O(nlog2n) |     | O(n) |     | No  | Medium | Wildbinarysegmentation |     |     |     |     |
| --- | ---------- | --- | --------- | --- | ---- | --- | --- | ------ | ---------------------- | --- | --- | --- | --- |
|     | Bai-Perron |     | O(Kn2)    |     | O(n) |     | No  | Low    | Regressionbreaks       |     |     |     |     |
BayesianMethods(Section4.3r)
|     | BOCPD        |     | O(n2)         |     | O(n)    |     | Yes* | Low    | O(nRmax)withtruncation |     |     |     |     |
| --- | ------------ | --- | ------------- | --- | ------- | --- | ---- | ------ | ---------------------- | --- | --- | --- | --- |
|     |              |     | O(nRmax)trunc |     | O(Rmax) |     |      |        |                        |     |     |     |     |
|     | HMM(Forward) |     | O(nS2)        |     | O(S)    |     | Yes  | Medium | Onlinefiltering        |     |     |     |     |
r
|     | HMM(Viterbi)    |     | O(nS2)  |     | O(nS) |     | No  | Medium | MAPsequence   |     |     |     |     |
| --- | --------------- | --- | ------- | --- | ----- | --- | --- | ------ | ------------- | --- | --- | --- | --- |
|     | HMM(Baum-Welch) |     | O(TnS2) |     | O(nS) | e   | No  | Low    | TEMiterations |     |     |     |     |
EmbeddingMethods(Section4.4)
|     | Embed+CUSUM |     | O(np+p3) |     |       |     |     |        |                         |     |     |     |     |
| --- | ----------- | --- | -------- | --- | ----- | --- | --- | ------ | ----------------------- | --- | --- | --- | --- |
|     |             |     |          |     | O(np) |     | Yes | Medium | p3fromembeddingtraining |     |     |     |     |
O(n2m2)
|     | MMD(kernel) |     |     |     | O(nm) |     | No  | Low | Windowsn,m;kernelmatrix |     |     |     |     |
| --- | ----------- | --- | --- | --- | ----- | --- | --- | --- | ----------------------- | --- | --- | --- | --- |
e
|     | EnergyDistance |     | O(nmlognm) |     | O(nm) |     | No  | Medium | Sorting-based         |     |     |     |     |
| --- | -------------- | --- | ---------- | --- | ----- | --- | --- | ------ | --------------------- | --- | --- | --- | --- |
|     |                |     | O(np+p2)   |     | O(p2) |     |     |        |                       |     |     |     |     |
|     | OOD(density)   |     |            |     |       |     | Yes | Medium | Afterembeddingtrained |     |     |     |     |
StructuralDependence(Section4.5)
|     | ICSS(Σ)        |     | O(np2)  |     | pO(p2) |       |     |        |                      |     |     |     |     |
| --- | -------------- | --- | ------- | --- | ------ | ----- | --- | ------ | -------------------- | --- | --- | --- | --- |
|     |                |     |         |     |        | Quasi |     | Medium | Covariancebreaks     |     |     |     |     |
|     |                |     | O(np2)  |     | O(p2)  |       |     |        |                      |     |     |     |     |
|     | CUSUMofsquares |     |         |     |        |       | Yes | Medium | Multivariatevariance |     |     |     |     |
|     | Copulatests    |     | O(n2p2) |     | O(np)  |       | No  | Low    | Taildependence       |     |     |     |     |

Scalability(rule-of-thumb):ratingsindicatethetypicalmaximumserieslengthnthatcanbehandledonastandardworkstationwithanefficient
implementation,assumingsmall-to-moderatedimentsion(p≲20).High:n≳106;Medium:105≲n≲106;Low:n≲105.Inpractice,largep
andexpensiveoperations(e.g.,kernelmatrices)reducetheselimitssubstantially.
*Real-timenote:PELTisoffline,butcanb o eusedinaquasi-onlinewayviasliding/rollingwindows.BOCPDisonline,butthenaive
implementationisO(n2);real-timeoperationtypicallyusesrun-lengthtruncationtoamaximumRmax(e.g.,100–500),yieldingO(nRmax)timeand
O(Rmax)memory.
Practicalconsiderations:forhigh-dnimensionalstreams(p>100),dimensionalityreduction(e.g.,PCAorlearnedembeddings)isusually
requiredbeforeapplyingmostdetectors.Sequentialmethods(CUSUM/EWMA)arepreferredforlow-latencymonitoring;segmentationmethods
(PELT/BinarySegmentation)arepreferredforretrospectiveanalysis.

changesmaybeabrupt,trecurrent,ordifficulttoparam- for range-bound markets. An ensemble can monitor
eterize [? ? ]. nWhen multiple behaviors coexist or a trend indicator and dynamically adjust model usage,
regimechangesareheterogeneous,evenadaptivemod- either by gradually shifting weights toward the trend
elscanfail. Anaturalresponseisthereforetomaintain model when momentum increases or by switching en-
anensembleofciomplementarymodelsandadaptatthe
|                                 |            |        |           |     |            |     | tirely  | to the range-bound |     | model     | during      | consolidation |           |
| ------------------------------- | ---------- | ------ | --------- | --- | ---------- | --- | ------- | ------------------ | --- | --------- | ----------- | ------------- | --------- |
| modellevelarsconditionsevolve[? |            |        | ?         | ].  |            |     | phases. |                    |     |           |             |               |           |
|                                 |            |        |           |     |            |     | In      | this context,      | we  | therefore | distinguish |               | three dy- |
| Thepcore                        | motivation | behind | ensembles | is  | to provide |     |         |                    |     |           |             |               |           |
namicensemblemechanisms:(i)gatedmodelselection,
| both robustness | and | continuity. | By maintaining |     | multi- |     |               |            |     |            |     |       |            |
| --------------- | --- | ----------- | -------------- | --- | ------ | --- | ------------- | ---------- | --- | ---------- | --- | ----- | ---------- |
|                 |     |             |                |     |        |     | (ii) adaptive | prediction |     | weighting, | and | (iii) | the incre- |
plespecializedmodels,thesystembecomesresilientto
uneexpectedregimes, whilepreservingknowledgefrom mentalintroductionandretirementofexperts.
| pastconditionsthatmayrecur. |     |     | Thispropertyisparticu- |     |     |     |              |           |     |           |     |                |       |
| --------------------------- | --- | --- | ---------------------- | --- | --- | --- | ------------ | --------- | --- | --------- | --- | -------------- | ----- |
|                             |     |     |                        |     |     |     | Active-model | selection |     | (gating). | A   | first strategy | is to |
larlyvaluableinfinance,wheremarketregimestendto
| r   |     |     |     |     |     |     | explicitlychoose,ateachtimestep,whichmodelshould |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ------------------------------------------------ | --- | --- | --- | --- | --- | --- |
repeat, and discarding models learned during previous be active. Several specialized models are maintained
Pcrisescanresultinthelossofusefulinformation.
|     |     |     |     |     |     |     | (for example, |     | one trained | for | a stable | market | and an- |
| --- | --- | --- | --- | --- | --- | --- | ------------- | --- | ----------- | --- | -------- | ------ | ------- |
As an illustration, consider a trading algorithm with otherforacrisis),andagatingmechanism(whichmay
one model optimized for trending markets and another be a regime detector or a learned function) chooses
29
This preprint research paper has not been peer reviewed. Electronic copy available at: https://ssrn.com/abstract=6170273

d
e
Table8:Comparisonofadaptationmethodsfornon-stationaryfinancialtimeseries.Methodsarecategorizedbyfamilyandcomparedacrosskey
operationaldimensions.
w
Method Family Speed Memory Complexity WhentoUse Example
ParametricApproaches(Section5.1)
TVP/Kalman Parametric Fast Low O(p2)perstep Gradual pearameter drift, Dynamic market
linearmodels betas
TAR/STAR Parametric Instant Low O(1)switch Known regime driver VIX-based volatil-
availabile ityregimes
HMM/MS Parametric Medium Medium O(KS2) Recurrent discrete Bull/bear market
v
regimes switching
DynamicEnsembles(Section5.2)
e
Gating(MoE) Ensemble Medium Medium O(M·c) Distinct regime special- Trend vs range
ists models
Weightedcombine Ensemble Fast Medium O(M·c) Hedge against uncer- DWM,
r tainty Learn++.NSE
Onlineexperts Ensemble Slow High O(M·t) Evolving regimes, suffi- Streaming classi-
cientdata fiers
r
IncrementalLearning(Section5.3)
SGD+forget Incremental Veryfast Verylow eO(p)perstep Continuousmilddrift Onlinelinearmod-
els
Periodicretrain Batch Slow High O(np) Stable with periodic Monthly model re-
shifts fresh
e
Hyperparameteradapt Meta Medium Low Varies Regime-dependent tun- Learning rate
ing scheduling
ModernApproaches(Section5.4) p
Continual+EWC Continual Medium Medium O(np+p2) Preserveoldknowledge Multi-task fraud
detection
Test-timeadapt Online Fast Low O(k·p) Distribution shift, unla- Domainadaptation
beledtest
t
FoundationFT Transfer Slow* High O(npf) Limitedlabeleddata Pre-trained trans-
o formers
Notation: p=parameters,S =HMMstates,K=iterations,M=ensemblesize,c=expertcost,t=trainingcost,n=samples,pf =fine-tuned
parameters(typicallypf ≪p),k=TTAgradientsteps.
Speedratings:Veryfast(<1ms),Fasnt(1–10ms),Medium(10–100ms),Slow(>100ms),Instant(0ms-rule-based).
Memoryratings:Verylow(O(1)orO(p)),Low(O(p2)orO(S)),Medium(O(M)orO(np)),High(O(nM)orfullhistory).
*Foundationmodelfine-tuningisslowinitiallybutenablesfastsubsequentadaptation.
whichmodeltouseateatchmoment[? ? ? ? ? ]. This changesandanalternativemodelstartsperformingbet-
isessentiallythemnixture-of-experts(MoE)ideawitha ter,theweightingschemeautomaticallyadjusts. Thisis
gatingnetwork,appliedovertime[??].Forinstance,a usedintrackingandconceptdriftmeta-learning: algo-
forecastingsystemmayhaveoneexpertforlowvolatil- rithmssuchasDynamicWeightedMajority(DWM)in
ity and another i for high volatility; a volatility detector theconcept-driftliteraturefollowthisstrategy[? ? ? ].
(oreventheHrMM)determinesinrealtimewhichexpert
shouldmaketheprediction[? ? ? ? ].
p Onlinetrainingofnewexperts. Amoreproactivestrat-
egyistoexpandtheensembleovertimebyintroducing
Predictioncombination(ensembleweighting). Asofter newmodelsasdataevolves. Incontinuousstreams,one
e
alternativeistoavoidhardswitchingandinsteadblend can continuously train new models on recent windows
the predictions of multiple models. Instead of choos- andaddthemtotheensemble,possiblyremovingor“re-
ring a single model, combine the outputs of all of them tiring”oldmodelsthathavebecomeobsolete—aform
withtime-varyingadaptiveweights.Asimplemethodis ofcontinuouslearninginwhichtheensemblegrowsand
P to weight models inversely proportional to their recent is pruned. For example, in the Learn++.NSE [? ? ]
error — thus, models that are performing poorly (per- methodandvariants,foreachnewbatchofdata,anew
hapsduetodrift)receivelowerweight,andiftheregime classifieristrained,andthefinalpredictionisacombi-
30
This preprint research paper has not been peer reviewed. Electronic copy available at: https://ssrn.com/abstract=6170273

d
e
nationofallclassifierswithweightsthatdecayforolder Actionsupondetectingclearstructuralchanges. When
onesiftheymisclassifyrecentdata.Thisgradually“for- a detector confirms a substantwial change, more disrup-
gets”oldhypotheseswithoutdiscardingthemabruptly. tive actions are initiated, as incremental updates may
nolongersuffice.
Despite the advantages of ensemble-based ap- Possibleresponsesincludepartialor
proaches, they are not universally appropriate. Their total model resets, where prior knowledge is discarded
e
use may be impractical when computational resources or strongly downweighted; on-the-fly hyperparameter
are severely constrained, as in ultra–low-latency trad- or architecture adjustments tailored to the new regime;
ingsystems,orwhenstrongmodelinterpretabilityisre- or specialization and branching, where a new model is
i
quiredforregulatoryoroperationalreasons. Ensembles addedtoanensembleratherthanreplacingtheexisting
v
mayalsobeunnecessaryinstableenvironmentswhere one. Thesemechanismsallowflexibleresponsestohet-
suffices,
a single well-calibrated model or undesirable erogeneousorrecurringregimes.
e
| when the         | operational | burden |         | of maintaining |     | and | mon- |            |             |            |     |      |           |
| ---------------- | ----------- | ------ | ------- | -------------- | --- | --- | ---- | ---------- | ----------- | ---------- | --- | ---- | --------- |
| itoring multiple |             | models | becomes | prohibitive.   |     | In  | such |            |             |            |     |      |           |
|                  |             |        |         |                |     |     |      | Continuity | and memory. | Adaptation |     | does | not imply |
cases,simpleradaptiveapproaches—suchasincremen-
r
tallearningortime-varying-parametermodels—canof- forgetting. Topreserveusefulpastknowledge,continu-
|            |          |         |     |         |              |     |     | ity m echanisms | from                                      | continual | learning |     | are often em- |
| ---------- | -------- | ------- | --- | ------- | ------------ | --- | --- | --------------- | ----------------------------------------- | --------- | -------- | --- | ------------- |
| fer a more | suitable | balance |     | between | adaptability |     | and |                 |                                           |           |          |     |               |
|            |          |         |     |         |              |     |     | ployed.         | Replay-basedstrategies,suchasmaintaininga |           |          |     |               |
complexity.
|     |     |     |     |     |     |     |     | r      | buffer        |     |         |     |             |
| --- | --- | --- | --- | --- | --- | --- | --- | ------ | ------------- | --- | ------- | --- | ----------- |
|     |     |     |     |     |     |     |     | memory | of historical |     | samples | and | mixing them |
eintoretraining,mitigatecatastrophicforgettinganden-
5.3. Hybridcontinuous-adaptationflows
|     |     |     |     |     |     |     |     | able faster | readaptation | if previously |     | observed | regimes |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------- | ------------ | ------------- | --- | -------- | ------- |
Hybridadaptationflowsareinherentlymulti-layered.
re-emerge.
| Theycombinelow-cost, |     |     | incrementalupdatesoperating |     |     |     |     |     |     |     |     |     |     |
| -------------------- | --- | --- | --------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
e
| continuously      | with      | explicit | responses |        | triggered | by  | de-  |             |                |            |                   |        |             |
| ----------------- | --------- | -------- | --------- | ------ | --------- | --- | ---- | ----------- | -------------- | ---------- | ----------------- | ------ | ----------- |
| tected structural |           | changes. | This      | design | seeks     | to  | rec- |             |                |            |                   |        |             |
|                   |           |          |           |        |           |     |      | Supervision | and supervised |            | reinitialization. |        | In many     |
| oncile two        | competing |          | goals:    | smooth | trackinpg | of  | mi-  |             |                |            |                   |        |             |
|                   |           |          |           |        |           |     |      | high-stakes | applications,  | adaptation |                   | is not | fully auto- |
norfluctuationsanddecisiveinterventionwhenregime matic. Drift signals may prompt human review or of-
| changesareabruptorpersistent. |     |     |     | Figure16summarizes |     |     |     |     |     |     |     |     |     |
| ----------------------------- | --- | --- | --- | ------------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- |
flineanalysis,particularlyinregulateddomainssuchas

agenerichybridadaptationarchitectureforlearningin finance. In these cases, experts may recalibrate mod-
| non-stationaryenvironments. |     |     |     |     | t   |     |     |                  |     |             |            |     |             |
| --------------------------- | --- | --- | --- | --- | --- | --- | --- | ---------------- | --- | ----------- | ---------- | --- | ----------- |
|                             |     |     |     |     |     |     |     | els, incorporate | new | explanatory | variables, |     | or validate |
TheFigure16highlightshowcontinuousmonitoring,
|     |     |     |     | o   |     |     |     | changes | under regulatory | constraints |     | before | redeploy- |
| --- | --- | --- | --- | --- | --- | --- | --- | ------- | ---------------- | ----------- | --- | ------ | --------- |
lightweight online updates, and event-driven interven- ment,formingahybridmanual–automaticloop.
tionsinteractinasingleprocessingflow.Thediscussion
Theseapproachesareconstrainedbypracticaltrade-
belowfollowsthisstructure,dnetailingthemaincompo-
offs.
|     |     |     |     |     |     |     |     | Strong | adaptation | actions | increase |     | computational |
| --- | --- | --- | --- | --- | --- | --- | --- | ------ | ---------- | ------- | -------- | --- | ------------- |
nentsofsuchsystemsandhowtheyjointlybalancere-
|     |     |     |     |     |     |     |     | cost and | latency, whereas |     | purely | incremental | updates |
| --- | --- | --- | --- | --- | --- | --- | --- | -------- | ---------------- | --- | ------ | ----------- | ------- |
sponsivenesstochangewithstabilityovertime.
|     |     |     |     |     |     |     |     | mayrespondtooslowlytoabruptchanges. |     |     |     |     | Theappro- |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------------------------------- | --- | --- | --- | --- | --------- |

priatebalancedependsonthecostofmodelerrorrela-
| Onlinemonitoringanddtriftalarms. |     |     |     |     | Atthebaseofthe |     |     |     |     |     |     |     |     |
| -------------------------------- | --- | --- | --- | --- | -------------- | --- | --- | --- | --- | --- | --- | --- | --- |
tivetothecostanddelayofadaptation,assummarized
| pipeline, | change       | detectors | operate    | continuously, |               |     | track- |           |     |     |     |     |     |
| --------- | ------------ | --------- | ---------- | ------------- | ------------- | --- | ------ | --------- | --- | --- | --- | --- | --- |
|           |              | n         |            |               |               |     |        | inTable9. |     |     |     |     |     |
| ing model | performance, |           | residuals, |               | or properties |     | of the |           |     |     |     |     |     |
Adaptationshouldnotbeautomaticinallsituations.
| input data | distribution. |     | When | these | detectors | signal | a   |     |     |     |     |     |     |
| ---------- | ------------- | --- | ---- | ----- | --------- | ------ | --- | --- | --- | --- | --- | --- | --- |
potential structuiral drift, they act as triggers that acti- Itmaybesuppressedwhendriftistransient,whendata
|     |     |     |     |     |     |     |     | after change | are insufficient, |     | when | transaction | or oper- |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------ | ----------------- | --- | ---- | ----------- | -------- |
vatehigher-lerveladaptationmechanisms.
|     |     |     |     |     |     |     |     | ational costs | dominate, | or when | regulatory |     | or stability |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------- | --------- | ------- | ---------- | --- | ------------ |
Local pcontinuous adaptation. Between alarms, the constraintsrequirefixedmodels. Insuchcases,delayed
model is kept up to date through lightweight orconservativeadaptationcanbepreferabletorapidbut
| incremental-learning |     | schemes. |     | Typical | approaches |     | in- | unreliableupdates. |     |     |     |     |     |
| -------------------- | --- | -------- | --- | ------- | ---------- | --- | --- | ------------------ | --- | --- | --- | --- | --- |
e
cludeexponentialforgettingingradientupdatesorregu- In summary, hybrid adaptation architectures provide
laronlineretrainingwithnewlyarrivingdata.Thislayer aprincipledwaytomanagenon-stationaritybycoordi-
rhandles small, gradual shifts without destabilizing the nating continuous learning with selective intervention.
modelandissupportedbymanystandardlearners,such Theireffectivenessliesnotonlyinhowtheyadapt,but
P
aslinearmodelstrainedviastochasticgradientdescent also in deciding when adaptation should be limited or
and neural networks updated through progressive fine- deferred, ensuring robustness without unnecessary in-
| tuning. |     |     |     |     |     |     |     | stability |     |     |     |     |     |
| ------- | --- | --- | --- | --- | --- | --- | --- | --------- | --- | --- | --- | --- | --- |
31
This preprint research paper has not been peer reviewed. Electronic copy available at: https://ssrn.com/abstract=6170273

d
e
w
e
i
v
Table9: Cost-benefittrade-offsforadaptationstrategiesinfinancialapplications. Performancegainsareapproximateandcontext-dependent;
valuesshownaretypicalforfinancialtimeseriesforecastingandclassificationtasks.
e
Strategy Latency ComputeCost Data Require- Perf.Gain WhentoUse
ments
r
Noadaptation 0ms None N/A Baseline(0%) Stable regimes only; bench-
mark
Incrementalupdate 1–10ms Verylow Streamingornly +5–10% Gradual drift; HFT; latency-
critical
e
Hyperparameter 1–10min Medium Recent window +10–15% Moderateregimechange;peri-
tuning (100–1000) odicmaintenance
Ensemblereweight 10–100ms Low eRecent window +10–20% Uncertain regimes; multiple
(50–500) hypotheses
Addensemblemem- 10min–1hr High New regime data +15–25% Novel regime emerges; suffi-
ber p(500–5000) cientdata
Fullretrain 1–24hrs Veryhigh Full history +20–30% Abruptstructuralbreak;offline
(5000+) batch
Modelreset 10min–1hr High Newregimeonly +15–25% Completeregimechange; his-
t(1000+) toryirrelevant
Test-timeadapt 10–100ms oLow–medium Unlabeled test +5–15% Domain shift; batch inference
batch mode
Foundationfine-tune 1–12hrs* Veryhigh Limited labels +15–30% New domain; leverage pre-
n
(100–1000) training
Latency:Timetoapplyadaptationandresumenormaloperation.Excludesinitialtraining.
Computecost:RelativeCPU/GP Urequirements."Verylow"=single-coreCPUsufficient;"Veryhigh"=multi-GPUordistributedcluster.
Datarequirements:Approximatenumberofobservationsneededforreliableadaptation.Variesbyproblemdimensionality.
Performancegain:Typicalimtprovementoverno-adaptationbaseline,measuredbyaccuracy,RMSEreduction,orrisk-adjustedreturns.Highly
problem-dependent.
n
*Foundationmodelfine-tuningisexpensiveinitiallybutenablesrapidsubsequentadaptation(<1hr)tonewsub-regimes.
HFT=High-frequencytrading(microsecond-levellatencyrequirements).
Decisionguidance:iInpractice,hybridpoliciesareoptimal:incrementalupdatesasdefault(<10msoverhead),triggeredactions(ensemble
reweight,hyperparametertuning)formoderatedrift,andscheduledfullretraining(nightly/weekly)formajorregimechanges.Thecostoferror
r
relativetoadaptationcostdeterminesaggressiveness:riskmanagement(higherrorcost)justifiesexpensiveadaptation;informationalforecasts
(lowerrorcost)favorcheapincrementalapproaches.
p
e
r
P
32
This preprint research paper has not been peer reviewed. Electronic copy available at: https://ssrn.com/abstract=6170273

d
e
OnlineMonitoring
w
DriftDetector(Sec.4)
Continuous:
Alwaysactive,
lowoverhead
|     |     | IncrementalUpdate |     | No  |     |     |     |     |     | e   |     |     |
| --- | --- | ----------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
DriftDetected?
Yes
|     |     |     |     |     | ClassifySeverity |     |     |     |     | i   |     |     |
| --- | --- | --- | --- | --- | ---------------- | --- | --- | --- | --- | --- | --- | --- |
v
Memory
|     |                        | L G ig r h a t d D u r a if | l t |     | Regi | M m od e e c ra h te ange |     | S Se tr v u er c e t D u | r r i a ft l |     | B u ff e r |     |
| --- | ---------------------- | --------------------------- | --- | --- | ---- | ------------------------- | --- | ------------------------ | ------------ | --- | ---------- | --- |
|     | Ev T e r n ig t g -d e | r re iv d e b n y :         |     |     |      |                           |     |                          |              |     | R e p la y |     |
|     | detection              |                             |     |     |      |                           |     | e                        |              |     |            |     |
Prevents
|     |     | IncrementalSGD |     |     | Adjusthyperparams |             |                       |                 |     |                  | catastrophic |     |
| --- | --- | -------------- | --- | --- | ----------------- | ----------- | --------------------- | --------------- | --- | ---------------- | ------------ | --- |
|     |     | withforgetting |     |     | +reweightensemble |             |                       | Type?           |     |                  | forgetting   |     |
|     |     | (Sec.5.4.1)    |     |     | (Sec.5.2)         |             |                       |                 |     |                  |              |     |
|     |     |                |     |     |                   |             |                       | ArR             | N   |                  |              |     |
|     |     |                |     |     |                   |             | Abrupt:  Recurrent:   |                 |     | Novel:           |              |     |
|     |     |                |     |     |                   |             | Reset/retrain         | Activatedormant |     | Addensemble      |              |     |
|     |     |                |     |     |                   | (Sec.5.4.1) | withreplay r(Sec.5.2) | expert          |     | (Sec.5.2) member |              |     |
e
ReturntoMonitoring
Figure 16: Hybrid continuous-adaptation pipeline. The system combines low-overhead incremental updates (continuous monitoring) with
event-drivenadaptationactionstriggeredbydriftdetection.Seveerityclassificationroutestoappropriatestrategies:lightdriftsreceiveincremental
adjustments,moderatedriftstriggerhyperparametertuningandensemblereweighting,severedriftsinvokemoredrasticmeasures(reset,expert
activation,orensembleexpansion). Memorybuffersenablereplaytomitigatecatastrophicforgetting(Sec.5.4.1). Thismulti-layerarchitecture
balancesadaptationspeed,stability,andperformance(Sec.5.3).
p
5.4. Continuous learning, test-time adaptation, and new training; and dynamic architectures, which allo-

foundationmodels cateadditionalcapacity—suchasnewneuronsormod-
|                 |     |              |     |        | t              |     | ules—to | represent | emerging | regimes | while | preserving |
| --------------- | --- | ------------ | --- | ------ | -------------- | --- | ------- | --------- | -------- | ------- | ----- | ---------- |
| This subsection |     | is organized |     | around | three learning |     |         |           |          |         |       |            |
existingones.Infinancialsettings,forinstance,afraud-
| strategies | for | non-stationary | enviroonments. |     | We  | first |     |     |     |     |     |     |
| ---------- | --- | -------------- | -------------- | --- | --- | ----- | --- | --- | --- | --- | --- | --- |
detectionsystemthatlearnsanewfraudpatternshould
| present continuous |     | learning | methods | (5.4.1), | followed |     |     |     |     |     |     |     |
| ------------------ | --- | -------- | ------- | -------- | -------- | --- | --- | --- | --- | --- | --- | --- |
notbecomeblindtoolder,still-relevantfraudbehaviors.
| by test-time | adaptation | techniques |     | (5.4.2). | Then, | we  |     |     |     |     |     |     |
| ------------ | ---------- | ---------- | --- | -------- | ----- | --- | --- | --- | --- | --- | --- | --- |
n
ArepresentativeexampleofthisphilosophyisElas-
thendiscusslightadaptationoffoundationmodelsand
meta-learning approaches (5.4.3), which aim to enable ticWeightConsolidation(EWC)[? ]. EWCaugments
rapidspecializationunderd istributionshift. the training loss with a penalty that discourages devia-
|     |     |     |     |     |     |     | tions | in parameters | deemed | critical | for previous | tasks, |
| --- | --- | --- | --- | --- | --- | --- | ----- | ------------- | ------ | -------- | ------------ | ------ |
t
5.4.1. Continuouslearningandmemorypreservation as measured by Fisher information. In a drift context,
|     |     | n   |     |     |     |     | once | a regime | change | is identified, | the model | can be |
| --- | --- | --- | --- | --- | --- | --- | ---- | -------- | ------ | -------------- | --------- | ------ |
Incontinuallearning,theobjectiveistoenablemod-
els to incorporate new information sequentially while updated using recent data while preserving parameters
|          |               |              |     |            |          |     | that encode | information |     | from the | earlier regime. | This |
| -------- | ------------- | ------------ | --- | ---------- | -------- | --- | ----------- | ----------- | --- | -------- | --------------- | ---- |
| avoiding | catastroiphic | forgettingof |     | previously | acquired |     |             |             |     |          |                 |      |
knowledge [? ]. This property is particularly impor- allows the model, at least partially, to function across
r
multipleregimeswithoutfullretraining.
tantunderdistributionshift,whereadaptationtoanew
regimepshouldnoteliminatethemodel’sabilitytooper- Replay-based memory further supports this process,
ateifearlierregimesreappearorcontinuetocoexistin especiallywhenhistoricaldataarelimitedorexpensive
tocollect.Maintainingevenasmallbufferofpastobser-
partofthedata.
e
To achieve this, continual-learning methods rely on vationscansubstantiallyreduceforgettingwhenadapt-
mechanisms that constrain how new knowledge is ab- ing to new conditions. In practice, this often connects
rsorbed. Common strategies include parameter reg- continual learning with ensemble methods: rather than
ularization, which penalizes changes to parameters forcing a single model to remember everything, multi-
P
that were important for past tasks; replay-based ap- plespecializedmodelscanbemaintained, withtheen-
proaches[? ? ], which store or generate samples sembleasawholepreservingbroaderhistoricalknowl-
| from previous |     | data distributions |     | and mix | them | into | edge. |     |     |     |     |     |
| ------------- | --- | ------------------ | --- | ------- | ---- | ---- | ----- | --- | --- | --- | --- | --- |
33
This preprint research paper has not been peer reviewed. Electronic copy available at: https://ssrn.com/abstract=6170273

d
e
Thisideaisexplicitindata-streamalgorithmssuchas regime may, when deployed in a new regime, ob-
Learn++.NSEanditsvariants,whichcontinuallyintro- serve incoming inputs and adwjust selected parameters
ducenewmodelswhileretainingolderonesandadjust- or statistics to preserve internal consistency or invari-
ing their weights based on current performance. Older ants. Whilethiscanprovidefastcorrectionwithoutex-
hypothesesarenotdiscardedoutright,allowingthemto ternal retraining, it is inherently risky: incorrect self-
| remaineffectiveifearliercontextsrecur. |     |     |     |     |     |            |         |       | e                |     |         |     |
| -------------------------------------- | --- | --- | --- | --- | --- | ---------- | ------- | ----- | ---------------- | --- | ------- | --- |
|                                        |     |     |     |     |     | supervised | signals | or po | orly constrained |     | updates | may |
Overall,despitetheseadvantages,continuallearning introducebiasoramplifymodeldrift.
|           |              |     |                  |      |      | Aparticularlypracti |     | calusecasearisesinanomalyde- |     |     |     |     |
| --------- | ------------ | --- | ---------------- | ---- | ---- | ------------------- | --- | ---------------------------- | --- | --- | --- | --- |
| has clear | limitations. | It  | can underperform | when | suc- |                     |     | i                            |     |     |     |     |
cessive regimes are too heterogeneous to be captured tection,wheretestdataareoftenassumedtobemostly
v
by a shared representation, when memory buffers are normal. In such scenarios, thresholds, activity levels,
too small to adequately represent past distributions, or orinternalreferencestatisticscanberecalibratedusing
e
whenthemodelarchitecturelackssufficientcapacityto onlycurren tobservations. Infinance,thisisanalogous
todailyrecalibrationofriskmodelsusingrecentintra-
| expressnewregimecomplexity. |     |     | Inaddition,ifdriftoc- |     |     |     |     |     |     |     |     |     |
| --------------------------- | --- | --- | --------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
curs faster than the model can adapt—such as during daypricestomaintainalignmentwithcurrentvolatility
r
| abrupt market | shocks—gradual |     | continual-learning |     | up- | levels. |     |     |     |     |     |     |
| ------------- | -------------- | --- | ------------------ | --- | --- | ------- | --- | --- | --- | --- | --- | --- |
theeffectivenessofTTAapproachesislim-
dates may lag behind reality. In such cases, ensemble Ov erall,
specialization or explicit regime-switching approaches ite d when shifts are severe or conceptual in nature:
r
maybemoreeffectivethanattemptingtopreserveasin- if the relationship between inputs and targets changes
eabruptly,unlabeledtestdataprovidelittlereliableguid-
glecontinuouslyadaptingmodel.
|                            |     |     |     |     |     | ance for | adjustment, | unless   | robust | self-supervised |          | ob-     |
| -------------------------- | --- | --- | --- | --- | --- | -------- | ----------- | -------- | ------ | --------------- | -------- | ------- |
|                            |     |     |     |     |     | jectives | correlate   | with the | task   | loss or         | reliable | pseudo- |
| 5.4.2. Test-timeadaptation |     |     |     |     | e   |          |             |          |        |                 |          |         |
labelscanbegenerated.
| Test-time | adaptation | (TTA) | encompasses |     | methods |     |     |     |     |     |     |     |
| --------- | ---------- | ----- | ----------- | --- | ------- | --- | --- | --- | --- | --- | --- | --- |
that allow a model to adjust parts of its behavior dur- 5.4.3. Lightadaptationoffoundationmodelsandmeta-
p
inginferenceitself,usingonlyunlabeleddatafromthe
learning
current environment [? ]. Rather than accumulating Foundation models and meta-learning address non-
| new labeled | data and | retraining | offline, | the model | per- |              |     |          |          |     |          |          |
| ----------- | -------- | ---------- | -------- | --------- | ---- | ------------ | --- | -------- | -------- | --- | -------- | -------- |
|             |          |            |          |           |      | stationarity | by  | reducing | the need | for | frequent | full re- |
forms limited self-adjustment on the fly, aiming to re- training. Instead of rebuilding models whenever the
t
mainalignedwiththeprevailingdatadistribution.
|     |     |     |     |     |     | data distribution |     | changes, | they | rely on | pre-trained | rep- |
| --- | --- | --- | --- | --- | --- | ----------------- | --- | -------- | ---- | ------- | ----------- | ---- |
o
Atabasiclevel, TTAoftenoperatesbyupdatingin- resentationsthatcanbequicklyre-specializedwithlim-
ternal statistics rather than model parameters. A com- ited data and computation. This shift is significant in
| mon example | is adaptive |     | no rmalization: | neural | net- |                                                  |     |     |     |     |     |     |
| ----------- | ----------- | --- | --------------- | ------ | ---- | ------------------------------------------------ | --- | --- | --- | --- | --- | --- |
|             |             |     | n               |        |      | domainssuchasfinance,wherefullretrainingisexpen- |     |     |     |     |     |     |
workswithnormalizationlayers(e.g.,BatchNorm[? ] sive, slow to deploy, and difficult to govern in produc-
| orLayerNorm[? | ])  | relyonestimatesofinputmeanand |     |     |     |     |     |     |     |     |     |     |
| ------------- | --- | ----------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
tion.
variance, which may beco me misaligned under distri- This approach is effective under drift for two main
bution shift. Recomputi ng or gradually updating these reasons. First,pre-trainingondiversedatasetsproduces
t
| statistics | at test time, | without | modifying | the | network |                 |     |            |        |        |      |        |
| ---------- | ------------- | ------- | --------- | --- | ------- | --------------- | --- | ---------- | ------ | ------ | ---- | ------ |
|            |               |         |           |     |         | representations |     | that often | remain | useful | when | market |
n
weights, can already improve robustness to covariate conditionschange,evenifthetargetdistributionshifts.
shift.
|     |     |     |     |     |     | Second, | adaptation | can | be limited | to  | a small subset | of  |
| --- | --- | --- | --- | --- | --- | ------- | ---------- | --- | ---------- | --- | -------------- | --- |
parameter-efficient
Moreadvance i dTTAmethodsextendthisideabyal- parameters—such as a task head or
lowing const rained parameter updates guided by self- moduleslikeLoRAoradapters—allowingfastupdates
r
[?
supervised objectives defined on test data ]. Typ- with bounded computational cost and reduced risk of
ical chpoices include entropy minimization or self- overfittingorinstability[? ? ? ? ? ]. Asaresult,mod-
consistencycriteria,whichcanbeevaluatedwithoutla- elscanrespondtoregimechangeswithoutcontinuously
bels. The model performs a small number of gradient modifyingthefullparameterspace.
e
stepstominimizesuchobjectivesbeforeproducingpre- Operationally, a simple deployment loop follows
dictions. Thesetechniqueshaveshownpromiseincor-
|     |     |     |     |     |     | three steps. | Incoming | data | are | first encoded |     | into em- |
| --- | --- | --- | --- | --- | --- | ------------ | -------- | ---- | --- | ------------- | --- | -------- |
rrecting moderate domain shifts in vision and language beddings using a frozen pre-trained backbone. These
| models. |     |     |     |     |     | embeddingsarethenmonitoredovertimetodetectdis- |     |     |     |     |     |     |
| ------- | --- | --- | --- | --- | --- | ---------------------------------------------- | --- | --- | --- | --- | --- | --- |
P
In time-series and financial settings, TTA can be in- tributional shifts by comparing recent representations
terpreted as rapid internal recalibration. For instance, againstareferencewindowthatcharacterizesthebase-
a return-forecasting model trained under one market lineregime. Whenadriftdetectorsignalsasignificant
34
This preprint research paper has not been peer reviewed. Electronic copy available at: https://ssrn.com/abstract=6170273

d
e
change, a lightweight adaptation step is triggered us- and false alarms (6.2). Finally, we discuss adaptive-
ingasmallbufferofrecentdata. Onlytheselectedpa- performanceandcost-awaremwetricsthatcapturerecov-
rameters—typicallythetaskheadorparameter-efficient ery,stability,andadaptationcosts(6.3).
components—areupdated,whilethebackboneremains
fixed.Adaptationisusuallyconstrainedbyexplicitbud-
6.1. Temporalvalidationprotocols
e
| gets on | data, optimization |     | steps, | and validation |     | crite- |     |     |     |     |     |     |     |
| ------- | ------------------ | --- | ------ | -------------- | --- | ------ | --- | --- | --- | --- | --- | --- | --- |
ria,ensuringthatupdatesimproveshort-horizonperfor- In time-series problems, proper evaluation requires
manceandcanbesafelyrolledbackifnecessary. validationprotocolsthatrespecttemporalorder, ensur-
i
ingthatnofutureinformationisusedduringtrainingor
| This paradigm |     | is already | reflected |     | in recent | time- |     |     |     |     |     |     |     |
| ------------- | --- | ---------- | --------- | --- | --------- | ----- | --- | --- | --- | --- | --- | --- | --- |
v
series foundation models such as TimesFM, Chronos, calibration[? ? ]. Whilethisprincipleisconceptually
|             |       |        |        |           |     |        | simple, it | demands | careful | implementation |     | in  | practice: |
| ----------- | ----- | ------ | ------ | --------- | --- | ------ | ---------- | ------- | ------- | -------------- | --- | --- | --------- |
| and Moirai, | which | report | strong | zero-shot | and | trans- |            |         |         |                |     |     |           |
vaelidation,
fer performance across heterogeneous benchmarks. In training, and test splits must be defined by
|             |                   |     |              |         |             |        | contiguous  | time | blocks | rather | than random |     | partitions, |
| ----------- | ----------------- | --- | ------------ | ------- | ----------- | ------ | ----------- | ---- | ------ | ------ | ----------- | --- | ----------- |
| financial   | and macroeconomic |     | forecasting, |         | pre-trained |        |             |      |        |        |             |     |             |
|             |                   |     |              |         |             |        | as commonly | done | under  | i.i.d. | assumptions |     | [? ? ].     |
| forecasters | like TimeGPT-1,   |     | as           | well as | compact     | trans- |             |      |        |        |             |     |             |
r
ferable models such as Lag-LLaMA and Tiny Time Moreover,whenevaluatingadaptivemodels,validation
|     |     |     |     |     |     |     | shoul d replicate |     | production | conditions; |     | for instance, | if  |
| --- | --- | --- | --- | --- | --- | --- | ----------------- | --- | ---------- | ----------- | --- | ------------- | --- |
Mixers,providepracticalstartingpointsundercommon
productionconstraintsonlatencyandcompute.Inthese amodelisupdatedmonthlyindeployment,thebacktest
r
settings, light adaptation through heads or adapters is shouldexplicitlysimulatethisupdatecycle[? ? ? ].
| sufficient |     |          |             |     |        |        | eAwidelyusedtemporalvalidationprotocolisthepre- |     |     |     |     |     |     |
| ---------- | --- | -------- | ----------- | --- | ------ | ------ | ----------------------------------------------- | --- | --- | --- | --- | --- | --- |
| often      | to  | maintain | performance |     | across | chang- |                                                 |     |     |     |     |     |     |
ingmarketconditions,avoidingrepeatedfullretraining quential(sequentialpredictivetest)scheme[? ? ? ]. In
thissetting,themodelistraineduptoagiventimeand
cycles.
e
In summary, foundation models and meta-learning then used to generate predictions sequentially as new
observationsarrive,withthetrainingsetbeingupdated
| support       | a controlled | and | scalable | response     |     | to non- |              |                                       |     |     |     |     |     |
| ------------- | ------------ | --- | -------- | ------------ | --- | ------- | ------------ | ------------------------------------- | --- | --- | --- | --- | --- |
|               |              |     |          |              |     |         | accordingly. | Thisprotocolcloselymirrorsonlineoper- |     |     |     |     |     |
| stationarity. | By combining |     | reusable | pre-trainepd |     | repre-  |              |                                       |     |     |     |     |     |
sentations,continuousmonitoringofembeddingbehav- ation and allows evaluation under realistic data arrival
ior,andparameter-efficientadaptation,forecastingsys- andadaptationconditions[? ? ].
temscanhandledriftmorequicklyandwit hlowerop- Beyond general forecasting evaluation, specialized
|           |                     |       |          |        |          |           | protocols | are required |            | for systems | that | include | change |
| --------- | ------------------- | ----- | -------- | ------ | -------- | --------- | --------- | ------------ | ---------- | ----------- | ---- | ------- | ------ |
| erational | risk. While         | these | methods  | dotnot |          | eliminate |           |              |            |             |      |         |        |
|           |                     |       |          |        |          |           | detection | and          | adaptation | components. |      | For     | change |
| the need  | for full retraining |       | in cases | of     | large or | persis-   |           |              |            |             |      |         |        |
o
tentshifts,theyofferapracticalmiddlegroundbetween detection, when real or approximate annotations of
|               |     |        |            |            |     |        | changepoint | times | are | available, | evaluation |     | is com- |
| ------------- | --- | ------ | ---------- | ---------- | --- | ------ | ----------- | ----- | --- | ---------- | ---------- | --- | ------- |
| static models | and | costly | retraining | pipelines, |     | making |             |       |     |            |            |     |         |
them well-suited for deploymnent in evolving financial monly performed by running detectors on series with
environments. known changes and observing their behavior relative
|     |     |     |     |     |     |     | to these     | events | [?       | ? ].         | In real-world |     | scenarios |
| --- | --- | --- | --- | --- | --- | --- | ------------ | ------ | -------- | ------------ | ------------- | --- | --------- |
|     |     |     |     |     |     |     | where ground |        | truth is | unavailable, | detectors     |     | are often |
assessedindirectlythroughtheirinteractionwithdown-
t
| 6. Evaluation: | ProtocolsandMetrics |     |     |     |     |     |     |     |     |     |     |     |     |
| -------------- | ------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
streamadaptationmechanisms,forexamplebyembed-
n
dingtheminafulladaptivepipelineandevaluatingthe
This section addresses the research question: How resultingsystembehavior[? ? ? ].
can we evaluate i the performance of models and de- Similarly, adaptation methods should be evaluated
tection/adaptation systems under non-stationarity, us- usingprotocolsthatemphasizeperformanceacrosstime
r
ing appropriate metrics and protocols? Proper evalu- and regimes rather than relying on static train–test
ation ispessential, as inappropriate protocols or metrics splits [? ? ]. Common practices include organizing
canleadtomisleadingconclusionsabouttheeffective- evaluationbytemporalwindowsorregimesandanalyz-
nessofmethodsinevolvingenvironments. ing system behavior before, during, and after distribu-
e
The discussion is organized around three evalua- tion shifts, ensuring that adaptation is assessed under
tion components that together define a concise frame- conditionsthatreflectitsintendedoperationaluse[? ].
rwork for fair and meaningful evaluation under non- Insummary,robustevaluationundernon-stationarity
stationarity. Wefirstpresenttemporalvalidationproto- reliesontemporallyconsistentvalidationprotocols,re-
P
colsthatrespectdatachronologyandavoidinformation alisticsimulationofdeploymentconditions,andend-to-
leakage(6.1).Wethenreviewmetricsspecifictochange endassessmentofdetectionandadaptationmechanisms
anddriftdetectors,includingdetectionaccuracy,delay, withinevolvingdatastreams[? ? ? ].
35
This preprint research paper has not been peer reviewed. Electronic copy available at: https://ssrn.com/abstract=6170273

d
e
•
6.2. Metricsspecifictodetectors Mean Time To Detection (MTTD): beyond
|     |                |     |           |           |     |         |        |     | whether                           | a change | is  | detewcted, | this | criterion  | cap- |
| --- | -------------- | --- | --------- | --------- | --- | ------- | ------ | --- | --------------------------------- | -------- | --- | ---------- | ---- | ---------- | ---- |
|     | The evaluation |     | of change | detectors |     | depends | funda- |     |                                   |          |     |            |      |            |      |
|     |                |     |           |           |     |         |        |     | tureshowquicklythedetectorreacts. |          |     |            |      | Itmeasures |      |
mentallyontheavailabilityandnatureofchange-point
annotations,whichinturnarecloselytiedtothetypeof the average delay between the true changepoint
|     |     |     |     |     |     |     |     |     | and the | alarm | time [? | ? ]. | What | constitutes | an  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ------- | ----- | ------- | ---- | ---- | ----------- | --- |
dataused.Inpractice,detectorsareevaluatedonaspec-
e
trum ranging from synthetic and semi-synthetic series acceptabledelayisapplication-dependent—forin-
tofullyreal-worlddata,eachofferingdifferentlevelsof stance,secondsmaymatterinhigh-frequencytrad-
|     |                     |     |     |      |     |     |     |     | ing, whereas | dela | ys of | months | may | be acceptable |     |
| --- | ------------------- | --- | --- | ---- | --- | --- | --- | --- | ------------ | ---- | ----- | ------ | --- | ------------- | --- |
|     | controlandrealism[? |     |     | ? ]. |     |     |     |     |              |      | i     |        |     |               |     |
A common intermediate setting relies on semi- inmacroeco nomicanalysis.
v
|     | syntheticdatasets, |      | whereartificialchangesareinjected |          |     |          |          | •   |                                         |     |     |     |     |     |     |
| --- | ------------------ | ---- | --------------------------------- | -------- | --- | -------- | -------- | --- | --------------------------------------- | --- | --- | --- | --- | --- | --- |
|     |                    |      |                                   |          |     |          |          |     | ARL (AverageRunLengthtofalsealarm):this |     |     |     |     |     |     |
|     | into real          | time | series. This                      | approach |     | provides | approxi- |     | 0                                       |     |     |     |     |     |     |
measureefocusesondetectorbehaviorunderstable
mategroundtruthwhilepreservingrealisticnoisechar-
|     |                                                 |            |              |               |            |           |       |     | conditions.      | Itcorrespondstotheexpectedtimeun- |                |     |               |           |        |
| --- | ----------------------------------------------- | ---------- | ------------ | ------------- | ---------- | --------- | ----- | --- | ---------------- | --------------------------------- | -------------- | --- | ------------- | --------- | ------ |
|     | acteristics                                     | and        | temporal     | dependencies, |            | allowing  | con-  |     |                  |                                   |                |     |               |           |        |
|     |                                                 |            |              |               |            |           |       |     | til a false      | alarm                             | occurs         | and | is inversely  | related   | to     |
|     | trolled evaluation                              |            | under        | conditions    | that       | resemble  | real  |     |                  |                                   |                |     |               |           |        |
|     |                                                 |            |              |               |            |           |       |     | the r sequential |                                   | false-positive |     | rate. In      | practice, | de-    |
|     | data [?                                         | ? ]. Fully | synthetic    | series,       | on         | the other | hand, |     |                  |                                   |                |     |               |           |        |
|     |                                                 |            |              |               |            |           |       |     | tectors          | are often                         | calibrated     |     | by specifying | a         | target |
|     | offercompletecontroloverchangelocationsandmech- |            |              |               |            |           |       |     |                  |                                   |                |     |               |           |        |
|     |                                                 |            |              |               |            |           |       |     | ARL [?           | ? ].                              |                |     |               |           |        |
|     | anisms,                                         | but may    | oversimplify |               | real-world | dynamics  | [?    |     | 0                |                                   |                |     |               |           |        |
r
|     | ].  |     |     |     |     |     |     | •   | MDR | (Missed | Detection | Rate): | defined |     | as the |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------- | --------- | ------ | ------- | --- | ------ |
e
In contrast, for real-world series without exact proportion of true changes that are not detected,
changepointlabels,evaluationbecomesmorechalleng- this criterion complements recall by explicitly
ing. One pragmatic strategy is indirect assessment quantifyingfailurestosignalchangepoints[? ? ].
e
|     | within an | adaptive | modeling | pipeline: |     | different | detec- |     |     |     |     |     |     |     |     |
| --- | --------- | -------- | -------- | --------- | --- | --------- | ------ | --- | --- | --- | --- | --- | --- | --- | --- |
torsarecombinedwiththesameadaptationpolicy,and 6.3. Adaptive-performanceandcostmetrics
|     | their effectiveness |     | is inferred | from | downstreampbehav- |     |     |        |           |     |            |     |       |              |     |
| --- | ------------------- | --- | ----------- | ---- | ----------------- | --- | --- | ------ | --------- | --- | ---------- | --- | ----- | ------------ | --- |
|     |                     |     |             |      |                   |     |     | Before | analyzing |     | adaptation |     | costs | and benefits |     |
ior[? ? ? ]. IfdetectorAconsistentlyleadstobetter- through specific metrics, it is necessary to define how
adaptedmodelperformancethandetectorBunderiden-
|     |                   |     |                  |     |             |        |      | adaptive | models     | are  | evaluated | in  | practice.        | Metrics | are |
| --- | ----------------- | --- | ---------------- | --- | ----------- | ------ | ---- | -------- | ---------- | ---- | --------- | --- | ---------------- | ------- | --- |
|     | tical conditions, |     | it is reasonable |     | to conclude |   that | A is |          |            |      |           |     |                  |         |     |
|     |                   |     |                  |     |             |        |      | only     | meaningful | when | computed  |     | under evaluation |         | se- |
effective
more at identifying relevant chatnges. Finally, tups that reflect how models are trained, updated, and
infullyunlabeledrealdata,qualitativeinspectionorex-
|     |               |     |              |       | o         |     |          | deployedinareal-worldenvironmentovertime[? |     |     |     |     |     |     | ? ? |
| --- | ------------- | --- | ------------ | ----- | --------- | --- | -------- | ------------------------------------------ | --- | --- | --- | --- | --- | --- | --- |
|     | pert judgment |     | is sometimes | used, | comparing |     | detected | ].                                         |     |     |     |     |     |     |     |
changepointsagainstknownhistoricalevents—suchas
|     |     |     |     |     |     |     |     | Accordingly, |     | the | evaluation | design | must | be  | made |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------ | --- | --- | ---------- | ------ | ---- | --- | ---- |
the2008–09financialcrisisorntheMarch2020COVID-
|     |     |     |     |     |     |     |     | explicit. | The | recommendations |     |     | below | specify | how |
| --- | --- | --- | --- | --- | --- | --- | --- | --------- | --- | --------------- | --- | --- | ----- | ------- | --- |
related market crash—to assess plausibility [? ? ]. scenarios and protocols may be defined to determine
|     | Whilesubjective, |     | thisapproachcanprovidecontextual |     |     |     |     |     |     |     |     |     |     |     |     |
| --- | ---------------- | --- | -------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
whereandunderwhichconditionsadaptivemodelsare
|     | validation. |     |     |     |     |     |     |          |      |     |     |     |     |     |     |
| --- | ----------- | --- | --- | --- | --- | --- | --- | -------- | ---- | --- | --- | --- | --- | --- | --- |
|     |             |     |     |     |     |     |     | tested[? | ? ]. |     |     |     |     |     |     |
So,whenchange-pointtannotationsareavailable,de-
|     | tectors can | be  | eva luated | in a | supervised | manner, | sim- | •   |         |        |          |           |     |           |     |
| --- | ----------- | --- | ---------- | ---- | ---------- | ------- | ---- | --- | ------- | ------ | -------- | --------- | --- | --------- | --- |
|     |             |     | n          |      |            |         |      |     | Testing | across | multiple | scenarios | and | datasets: |     |
ilarly to classifiers, by contrasting correct detections adaptationshouldbeevaluatedondiverseseriesor
with false alarms [? ? ]. In this setting, several com- assets, covering different temporal structures and
|     | plementary | criteiria | are | commonly | used | to characterize |     |     |              |        |      |      |                  |     |     |
| --- | ---------- | --------- | --- | -------- | ---- | --------------- | --- | --- | ------------ | ------ | ---- | ---- | ---------------- | --- | --- |
|     |            |           |     |          |      |                 |     |     | drift types, | rather | than | on a | single benchmark |     | [?  |
detectorbeharvior[? ? ]. ? ? ]. Reliance on a small number of canonical
|     |               |     |         |        |            |            |     |     |            |        |     |             | dataset[? |     | ?    |
| --- | ------------- | --- | ------- | ------ | ---------- | ---------- | --- | --- | ---------- | ------ | --- | ----------- | --------- | --- | ---- |
|     |               |     |         |        |            |            |     |     | benchmarks | (e.g., | the | Electricity |           |     | ] or |
|     | • Prpecision, |     | recall, | and F1 | for change | detection: |     |     |            |        |     |             |           |     |      |
afewmarketindices7),especiallywhencombined
thesemetricsquantifyhowmanytruechangesare
|     |                      |     |     |                          |     |     |     |     | with simplified              |     | protocols, | may | limit | the extent | to  |
| --- | -------------------- | --- | --- | ------------------------ | --- | --- | --- | --- | ---------------------------- | --- | ---------- | --- | ----- | ---------- | --- |
|     | detected(recall)and, |     |     | amongalldetectedchanges, |     |     |     |     |                              |     |            |     |       |            |     |
|     | e                    |     |     |                          |     |     |     |     | whichconclusionsgeneralize[? |     |            |     | ? ].  |            |     |
howmanycorrespondtoactualchangepoints(pre-
|     | cision) | [?  | ? ]. | They are | particularly | useful | in  |     |     |     |     |     |     |     |     |
| --- | ------- | --- | ---- | -------- | ------------ | ------ | --- | --- | --- | --- | --- | --- | --- | --- | --- |
rscenarioswithimbalancedoutcomes,whereeither 7Examplesofwidelyusedmarket-indexdatasourcesincludethe
falsealarmsormisseddetectionsdominate. Inthe S&P 500 level series distributed via FRED [? ]; volatility bench-
| P   |       |             |       |            |     |               |     | markssuchastheVIXfromCboe(alsomirroredinFRED)[? |     |     |     |     |     |     | ? ]; |
| --- | ----- | ----------- | ----- | ---------- | --- | ------------- | --- | ----------------------------------------------- | --- | --- | --- | --- | --- | --- | ---- |
|     | drift | literature, | these | quantities |     | are sometimes | re- |                                                 |     |     |     |     |     |     |      |
research-gradeequityandindexreturnsviaCRSPthroughWRDS[?
ferredtoas“driftdetectionrate”and“falsealarm
];andprovidermethodology/governancedocumentsformajorglobal
|     | rate”[? | ?   | ].  |     |     |     |     | benchmarks(e.g.,MSCIandFTSERussell)[??]. |     |     |     |     |     |     |     |
| --- | ------- | --- | --- | --- | --- | --- | --- | ---------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
36
This preprint research paper has not been peer reviewed. Electronic copy available at: https://ssrn.com/abstract=6170273

d
e
•
Robustevaluationprotocols: allmethodsshould 7. BenchmarkandReproducibility
| be  | compared | under | identical |     | backtesting | and up- |     |     |     | w   |     |     |     |
| --- | -------- | ----- | --------- | --- | ----------- | ------- | --- | --- | --- | --- | --- | --- | --- |
date procedures, with statistical testing applied This section addresses the research question: How
candetectionandadaptationmethodsbebenchmarked
| whereappropriate[? |     |           | ].       |     |            |          |                                             |     |             |     |               |            |        |
| ------------------ | --- | --------- | -------- | --- | ---------- | -------- | ------------------------------------------- | --- | ----------- | --- | ------------- | ---------- | ------ |
|                    |     |           |          |     |            |          | undernon-stationarityinfinancialtimeseries? |     |             |     |               |            | Proper |
| •                  |     |           |          |     |            |          | benchmarking                                | is  | essentieal, | as  | inappropriate | protocols, |        |
| Sensitivity        |     | analysis: | critical |     | parameters | control- |                                             |     |             |     |               |            |        |
ling adaptation (e.g., forgetting factors, detection scenario choices, or reporting conventions can lead to
|             |     |        |              |     |        |           | misleading     | conclusion | s   | about | what works | in  | evolving |
| ----------- | --- | ------ | ------------ | --- | ------ | --------- | -------------- | ---------- | --- | ----- | ---------- | --- | -------- |
| thresholds, |     | update | frequencies) |     | should | be varied |                |            | i   |       |            |     |          |
|             |     |        |              |     |        |           | environments[? |            | ].  |       |            |     |          |
toverifythatresultsarenotdrivenbynarrowtun-
v
| ing[? | ].  |     |     |     |     |     | Thediscussionisorganizedaroundfourcomponents. |     |     |     |     |     |     |
| ----- | --- | --- | --- | --- | --- | --- | --------------------------------------------- | --- | --- | --- | --- | --- | --- |
Wefirstdefinebenchmarkcriteriaandascenariospec-
ificationthaetmakesassumptionsexplicitandcompara-
| • External |     | validity | and | replicability: |     | consistent |     |     |     |     |     |     |     |
| ---------- | --- | -------- | --- | -------------- | --- | ---------- | --- | --- | --- | --- | --- | --- | --- |
bleacrossstudies(Section7.1).Wethenreviewdatasets
| evaluation   |     | pipelines | and      | shared  | datasets | enable |           |            |     |         |           |      |      |
| ------------ | --- | --------- | -------- | ------- | -------- | ------ | --------- | ---------- | --- | ------- | --------- | ---- | ---- |
|              |     |           |          |         |          |        | and tasks | for regime | and | anomaly | detection | from | both |
| verification |     | that      | reported | results | persist  | across |           |            |     |         |           |      |      |
r
|           |     |     |     |     |     |     | the financial | and | data-stream |     | literature | (Section | 7.2). |
| --------- | --- | --- | --- | --- | --- | --- | ------------- | --- | ----------- | --- | ---------- | -------- | ----- |
| studies[? |     | ].  |     |     |     |     |               |     |             |     |            |          |       |
Next, weproposeaminimalscenario-coveragebaseline
|                                                  |     |     |     |     |     |     | that enables                                | comparable |     | benchmark | suites | without | re-      |
| ------------------------------------------------ | --- | --- | --- | --- | --- | --- | ------------------------------------------- | ---------- | --- | --------- | ------ | ------- | -------- |
| Oncetheseevaluationsetupsarefixed,thecriteriafo- |     |     |     |     |     |     | r                                           |            |     |           |        |         |          |
|                                                  |     |     |     |     |     |     | quiringasinglecanonicaldataset(Section7.3). |            |     |           |        |         | Finally, |
cusonwhatshouldbemeasuredtoquantifythepracti-
|                              |     |     |     |                      |     |     | ewe provide | a compact |     | recipe | for constructing |     | bench- |
| ---------------------------- | --- | --- | --- | -------------------- | --- | --- | ----------- | --------- | --- | ------ | ---------------- | --- | ------ |
| calconsequencesofadaptation. |     |     |     | Inadditiontostandard |     |     |             |           |     |        |                  |     |        |
marksandreportingreproducibleevaluationsunderre-
| predictive | metrics | computed |     | sequentially |     | over time— |     |     |     |     |     |     |     |
| ---------- | ------- | -------- | --- | ------------ | --- | ---------- | --- | --- | --- | --- | --- | --- | --- |
alisticdeploymentconstraints(Section7.4).
| for example, | forecasting |     | error | tracked | across | windoews |     |     |     |     |     |     |     |
| ------------ | ----------- | --- | ----- | ------- | ------ | -------- | --- | --- | --- | --- | --- | --- | --- |
orregimes—adaptivemodelsmustbeassessedwithre-
7.1. Criteriaandscenariospecification
| spect to | the computational, |     |     | behavioral, | and | economic |     |     |     |     |     |     |     |
| -------- | ------------------ | --- | --- | ----------- | --- | -------- | --- | --- | --- | --- | --- | --- | --- |
effectsintroducedbymodelupdates,assummaprizedbe-
Benchmarksfornon-stationarityshouldsupportcon-
low[? ? ? ]. trolled, reproducible comparison across methods and
|     |     |     |     |     |     |     | research | traditions. | In  | finance, | this is | challenging | be- |
| --- | --- | --- | --- | --- | --- | --- | -------- | ----------- | --- | -------- | ------- | ----------- | --- |

| •             |     |          |          |       |          |           | causestudiesoftenrelyonproprietarydatasets,        |     |     |     |     |     | adhoc |
| ------------- | --- | -------- | -------- | ----- | -------- | --------- | -------------------------------------------------- | --- | --- | --- | --- | --- | ----- |
| Computational |     |          | overhead | and   | latency: | the fre-  |                                                    |     |     |     |     |     |       |
|               |     |          |          |       | t        |           | assetselections,andheterogeneousexperimentalproto- |     |     |     |     |     |       |
| quency        | and | duration | of       | model | updates  | determine |                                                    |     |     |     |     |     |       |
cols,whichlimitsreproducibilityandunderminescross-
| whether |     | adaptation | is  | feasibloe | under | time con- |     |     |     |     |     |     |     |
| ------- | --- | ---------- | --- | --------- | ----- | --------- | --- | --- | --- | --- | --- | --- | --- |
papercomparability.
straints.Streamingframeworks(e.g.,MOA,River)
Tomakebenchmarkdesignexplicitandcomparable,
typicallyreportthroughputtocharacterizethisas-
n
pect[? ? ]. we specify each benchmark scenario s by a taxonomy-
conditioneddescriptor:
| • Memory |     | footprint: |  adaptive |     | architectures | differ |     |     |     |     |     |     |     |
| -------- | --- | ---------- | --------- | --- | ------------- | ------ | --- | --- | --- | --- | --- | --- | --- |
ϕ(s)=(Temporal,
|     |     |     |     |     |     |     |     |     | Statistical, |     | Spatial, | Ontological), |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------ | --- | -------- | ------------- | --- |
inresourceusage;largeensemblesrequiresubstan-
|     |     |     | t   |     |     |     |     |     |     |     |     |     | (1) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
tiallymorememorythansingle-modelapproaches,
|     |     |     |     |     |     |     | using the | four axes | introduced |     | in Section | 2,  | together |
| --- | --- | --- | --- | --- | --- | --- | --------- | --------- | ---------- | --- | ---------- | --- | -------- |
n
which may be prohibitive in constrained environ- ,anonlineprotocolΠ
|     |     |     |     |     |     |     | withadatainstantiationD |     |     | s   |     |     | s ,and |
| --- | --- | --- | --- | --- | --- | --- | ----------------------- | --- | --- | --- | --- | --- | ------ |
ments.
|     |     |     |     |     |     |     | anevaluationmappingE |     |     | (Fig.17): |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | -------------------- | --- | --- | --------- | --- | --- | --- |
s
i
• Stabilit yandvolatilityofpredictions:aggressive B={(D ,ϕ(s),Π ,E )}S
|                                     | r   |     |     |     |     |            |     |     | s   |     | s s s=1 | .   | (2) |
| ----------------------------------- | --- | --- | --- | --- | --- | ---------- | --- | --- | --- | --- | ------- | --- | --- |
| adaptationcaninduceerraticbehavior. |     |     |     |     |     | Evaluation |     |     |     |     |         |     |     |
shpouldverifythatmodelupdatesdonotintroduce Here, Π fixes the online setting (e.g., prequential
s
excessive oscillations in predictions or decisions vs. rolling updates, label delay/availability, latency
overtime[? ? ]. and compute budgets, and model-access assumptions),
e
|     |     |     |     |     |     |     | while E | defines | what | is reported | (detection |     | quality, |
| --- | --- | --- | --- | --- | --- | --- | ------- | ------- | ---- | ----------- | ---------- | --- | -------- |
s
•
Direct economic impact: in financial applica- predictive performance and calibration, computational
rtions,adaptationshouldbeevaluatedthroughrisk- cost,andfinance-specificutility).
adjusted utility measures. When multiple strate- Under this specification, desirable benchmark prop-
P
gies are compared, statistical controls such as ertiesbecomerequirementson(i)coverageofdriftsig-
White’s Reality Check [? ] are required to miti- natures {ϕ(s)} and (ii) comparability of protocols and
gatedata-snoopingeffects[?
|     |     |     |     | ?   | ].  |     | outcomes: |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --------- | --- | --- | --- | --- | --- | --- |
37
This preprint research paper has not been peer reviewed. Electronic copy available at: https://ssrn.com/abstract=6170273

d
e
castingandregimechange. Wethencoveranomalyand
ScenarioSpecification out-of-distributionbenchmarkswoftenusedasproxiesfor
B s =(D s ,ϕ(s),Π s ,E s ) rareorextremeregimes.Weclosewithpracticalconsid-
erationsontoolingandreproduciblepipelines.
Datain- Assets/markets;samplingfrequency;horizon; e
stantiation calendarrulesandpreprocessing 7.2.1. Financial time series and forecasting bench-
D (optional)alignedcontextchannels: marksunderchangingregimes
s macro/microstructure/text
Infinance,thereareistillnoconsolidatedbenchmark
repositoriescompvarabletothoseusedinthedata-stream
Driftsig- Temporal: abrupt/ Spatial: global/local
nature gradual/recurrent literature.Instead,evaluationtypicallyreliesonisolated
ϕ(s) Statistical: ∆P(X)/ Ontological: regime/ time series and task-specific experimental setups cho-
e
∆P(Y|X)/dep.shift mechanism
senbyindividualstudies. Asaconsequence,thereisno
single “standard dataset” for problems such as regime
Online Updateprotocol: prequential/rolling;label
protocol delayandavailability change orr adaptive forecasting: different works select
Π Latency/computebudgets;modelaccess: white- different assets, markets, and time periods. For exam-
s box/black-box
ple,onestudymayfocusonBitcoinprices[? ],another
onrindividualstocks[????],andanotheronsectorin-
Evaluation Detection: delay,false-alarmcontrol;Predic- dices, making direct comparison difficult, since results
mapping tion: loss,calibration e
E Compute: wall-clock/memory;Utility: costs, can vary substantially across assets and historical win-
s
drawdown,risk-adj.return
dows.
eSeveral efforts attempt to partially mitigate this lim-
Figure17:Scenariospecificationschemaforbenchmarkdesignunder itation by defining approximate regimes using known
non-stationarity.AscenarioisdefinedbydataDs,driftsignatureϕ(s) economicormarketevents. Commonstrategiesinclude
(four-axistaxonomy),onlineprotocolΠ s,andevaluationmpappingE s.
splitting series into pre- and post-crisis windows (e.g.,
the 2008 global financial crisis or the 2020 COVID
• Identifiability. Scenarios should include anno- shock) and treating them as distinct regimes to assess
tated or controlled changes (event-based, statisti- robustnessunderdistributionshifts. Whileuseful,these
t
cal, or semi-synthetic) to enable objective assess- constructions remain ad hoc and lack standardization
ment. o acrossstudies.
In this fragmented scenario, other types of datasets
• Coverage. Suites should span diverse morpholo-
andtasksaremorecommonlyused,suchas:
gies and mechanisms acnross the four axes (e.g.,
abrupt vs. gradual, global vs. local, regime vs. • Return or volatility forecasting for equity indices
mechanism).
(S&P 500, Dow Jones, and international indices)
• Realism–control balance. Combine real-market over long horizons, where economic cycles and
episodes with cont t rolled synthetic/semi-synthetic crisesprovideimplicitregimevariation.
settingstosepnaratemethodologicaleffectsfromid-
• Detection of regime changes in macroeconomic
iosyncraticartifacts.
series (GDP, inflation) or market indicators such
• Sufficient iduration. Scenarios should be long as implied volatility and trading volume, includ-
enoughrtoevaluatelong-runstability,repeatedup- inginterest-rateseriesaffectedbymonetarypolicy
dates,andcumulativeadaptationeffects.
shifts.
p
• Context metadata. When relevant, pro- • High-frequencyfinancialdata(tickortransaction-
vide aligned macro/microstructure/textual context
levelseries)usedtodetectmicro-regimes,suchas
eto evaluate context-aware and multimodal ap-
intradaychangesinliquidityandvolatility; recent
proaches[? ? ? ].
examples include microstructure data from B3 [?
r ? ? ].
7.2. Datasetsandtasksforregimeandanomalydetec-
Ption • Specialized tasks such as financial contagion de-
Weorganizethisdiscussionintotwocategories. We tection,basedontimeseriesofcorrelationsortail-
first discuss financial time series benchmarks for fore- riskmeasuresacrossmarkets[? ? ? ? ? ].
38
This preprint research paper has not been peer reviewed. Electronic copy available at: https://ssrn.com/abstract=6170273

d
e
7.2.2. Benchmarks for anomalies and out-of- economicfeedback,includingtradingfrictionsandsta-
distribution tisticalcontrolsagainstbacktewstoverfitting[? ? ? ].
|                 |     |         |     |         |                 |     | These | tools | facilitate | implementation, |     | but | fair com- |
| --------------- | --- | ------- | --- | ------- | --------------- | --- | ----- | ----- | ---------- | --------------- | --- | --- | --------- |
| The distinction |     | between |     | concept | drift, regimes, | and |       |       |            |                 |     |     |           |
anomalies is often blurred: rare regimes may appear parisons require explicit scenario and protocol specifi-
anomalous when viewed from dominant market con- cations, which we formalize in Sections 7.3 and 7.4 [?
|                  |       |            |           |              | effectively |            |     |     |     | e   |     |     |     |
| ---------------- | ----- | ---------- | --------- | ------------ | ----------- | ---------- | --- | --- | --- | --- | --- | --- | --- |
| ditions,         | while | persistent | anomalies |              | can         | de-        | ].  |     |     |     |     |     |     |
| fine short-lived |       | regimes.   |           | As a result, |             | benchmarks |     |     |     |     |     |     |     |
originally designed for anomaly or out-of-distribution 7.3. Scenario coveragie: towards comparable bench-
| (OOD)detectionarefrequentlyreusedtoevaluatedrift |     |     |     |                      |     |     |         | marksuitesv |            |       |             |     |               |
| ------------------------------------------------ | --- | --- | --- | -------------------- | --- | --- | ------- | ----------- | ---------- | ----- | ----------- | --- | ------------- |
| andregime-detectionmethods,                      |     |     |     | andthemethodological |     |     |         |             |            |       |             |     |               |
|                                                  |     |     |     |                      |     |     | Section | 7.2         | highlights | that, | in finance, |     | evaluation is |
boundariesbetweenthesetasksarenotalwaysclear.
|         |                 |     |     |            |            |      | oftendrivenbyidiosyncraticchoicesofassets,timepe- | e              |     |       |       |         |              |
| ------- | --------------- | --- | --- | ---------- | ---------- | ---- | ------------------------------------------------- | -------------- | --- | ----- | ----- | ------- | ------------ |
| Several | general-purpose |     |     | benchmarks | illustrate | this |                                                   |                |     |       |       |         |              |
|         |                 |     |     |            |            |      | riods,                                            | and protocols, |     | which | makes | results | difficult to |
overlap. TheNumentaAnomalyBenchmark(NAB)[? compareacrossstudies. Toaddressthislimitationwith-
| ], for example, |     | includes   | multiple   |                  | time series—some |          |                |         |           |              |           |       |            |
| --------------- | --- | ---------- | ---------- | ---------------- | ---------------- | -------- | -------------- | ------- | --------- | ------------ | --------- | ----- | ---------- |
|                 |     |            |            |                  |                  |          | out requriring |         | a single  | “standard    | dataset”, |       | we propose |
| with financial  |     | relevance, | such       | as stock-related |                  | Twitter  |                |         |           |              |           |       |            |
|                 |     |            |            |                  |                  |          | to standardize |         | coverage: | a            | benchmark | suite | should in- |
| activity—with   |     | annotated  | anomalies. |                  | Although         | its pri- |                |         |           |              |           |       |            |
|                 |     |            |            |                  |                  |          | clude          | a small | set       | of scenarios | whose     | drift | signatures |
| mary focus      | is  | on point   | anomalies, |                  | extended         | anoma-   |                |         |           |              |           |       |            |
spranthemainregionsofthefour-axistaxonomy(tem-
lous segments can be interpreted as short regimes, and poral,statistical,spatial,ontological),whilekeepingthe
e
| some studies | evaluate |     | drift | detectors | on NAB | by treat- |     |     |     |     |     |     |     |
| ------------ | -------- | --- | ----- | --------- | ------ | --------- | --- | --- | --- | --- | --- | --- | --- |
suitecompactenoughforreproducibleevaluation.
ingeachannotatedanomalyasachangepointtodetect.
Similarly, recently compiled shift benchmarks such eMinimal as reference suite. We recommend the follow-
| the Shifts                | Dataset | [?            | ] provide | real                    | distribution | shifts      |             |            |       |                  |              |                 |           |
| ------------------------- | ------- | ------------- | --------- | ----------------------- | ------------ | ----------- | ----------- | ---------- | ----- | ---------------- | ------------ | --------------- | --------- |
|                           |         |               |           |                         |              |             | ing minimal |            | suite | as a coverage    | baseline.    |                 | Each sce- |
| acrossmultiplemodalities, |         |               |           | eventhoughtheiremphasis |              |             |             |            |       |                  |              |                 |           |
|                           |         |               |           |                         |              |             | nario       | is defined | by    | a characteristic |              | drift signature | ϕ(s)      |
| liesmainlyoutsidefinance. |         |               |           |                         |              | p(Section   |             |            |       |                  |              |                 |           |
|                           |         |               |           |                         |              |             |             | 2)         | and   | can be           | instantiated | using           | multiple  |
| In financial              |         | applications, |           | however,                | there        | is no stan- |             |            |       |                  |              |                 |           |
datasets/tasksfromSection7.2:
| dardized | anomaly | or  | OOD | benchmark. | Most | studies |     |     |     |     |     |     |     |
| -------- | ------- | --- | --- | ---------- | ---- | ------- | --- | --- | --- | --- | --- | --- | --- |
relyonadhoc,event-basedconstructions,su chascom- • S1: Crisis dependence regime. Abrupt changes
paring returns during “normal” periods wtith those ob- in multivariate dependence/tails with global im-
servedaroundmajorshocks(e.g., September11orthe pact,interpretedasaregimeshift(e.g.,contagion;
o
LehmanBrotherscollapse). Whileintuitive,theseprac- correlation/tail-riskbreakdownacrossmarkets).
| tices lack | consistency |            | and comparability |          | across   | works. |     |                          |           |      |                   |     |     |
| ---------- | ----------- | ---------- | ----------------- | -------- | -------- | ------ | --- | ------------------------ | --------- | ---- | ----------------- | --- | --- |
|            |             |            |                   |          |          |        | •   | S2: Localmechanismshift. |           |      | Gradualchangepri- |     |     |
| As noted   | by          | Žliobaite˙ | [?                | ]nin her | critique | of the |     |                          |           |      |                   |     |     |
|            |             |            |                   |          |          |        |     |                          | affecting | ∆P(Y |                   |     |     |
long-standing use of the Electricity data set for con- marily | X) (often coupled with
|            |                                       |     |     |     |     |     |     | ∆P(X)), | local | to a subset | of  | assets/segments, | in- |
| ---------- | ------------------------------------- | --- | --- | --- | --- | --- | --- | ------- | ----- | ----------- | --- | ---------------- | --- |
| ceptdrift, | thewidespreadadoptionofaconvenientbut |     |     |     |     |     |     |         |       |             |     |                  |     |
limitedbenchmarkcanobs cureimportantmethodolog- terpretedasamechanismchange(e.g.,sectorrota-
tion;microstructure/regulatorychange).
| ical weaknesses. |     | By                | atnalogy, | commonly |      | used finan-  |     |                        |     |     |                      |     |     |
| ---------------- | --- | ----------------- | --------- | -------- | ---- | ------------ | --- | ---------------------- | --- | --- | -------------------- | --- | --- |
| cial anomaly     |     | series—especially |           | those    | with | artificially |     |                        |     |     |                      |     |     |
|                  |     | n                 |           |          |      |              | •   | S3: Secularmacrodrift. |     |     | Incrementaldriftdom- |     |     |
injectedoutliers—shouldbecriticallyexaminedbefore
|     |     |     |     |     |     |     |     | inated | by ∆P(X) | and | slow parameter |     | drift with |
| --- | --- | --- | --- | --- | --- | --- | --- | ------ | -------- | --- | -------------- | --- | ---------- |
beingusedtoevaluateregime-changeordrift-detection
|          |     |     |     |     |     |     |     | global       | scope, | interpreted | as                            | regime | drift (e.g., |
| -------- | --- | --- | --- | --- | --- | --- | --- | ------------ | ------ | ----------- | ----------------------------- | ------ | ------------ |
| methods. |     | i   |     |     |     |     |     |              |        |             |                               |        |              |
|          |     |     |     |     |     |     |     | long-horizon |        | evolution   | in rates/inflation/volatility |        |              |
r
| 7.2.3. Practical  |     | considerations: |                  | tooling |        | and repro- |     | regimes).                |     |          |              |           |      |
| ----------------- | --- | --------------- | ---------------- | ------- | ------ | ---------- | --- | ------------------------ | --- | -------- | ------------ | --------- | ---- |
| dpuciblepipelines |     |                 |                  |         |        |            | •   |                          |     |          |              |           |      |
|                   |     |                 |                  |         |        |            |     | S4: Recurrent            |     | seasonal | regimes.     | Recurrent | pat- |
| To complement     |     | the             | dataset-and-task |         | survey | above,     |     |                          |     |          |              |           |      |
|                   |     |                 |                  |         |        |            |     | terns (calendar/intraday |     |          | seasonality) | primarily | ex-  |
w e note that reproducible benchmarking pipelines are pressedthrough∆P(X)andhigher-orderstructure;
e
| often built | on: | (i) | data-stream | frameworks |     | (MOA, |     |     |     |     |     |     |     |
| ----------- | --- | --- | ----------- | ---------- | --- | ----- | --- | --- | --- | --- | --- | --- | --- |
globalorlocal;typicallyaregimephenomenon.
| Scikit-Multiflow, |     | River) | for | incremental | learning, | drift |     |     |     |     |     |     |     |
| ----------------- | --- | ------ | --- | ----------- | --------- | ----- | --- | --- | --- | --- | --- | --- | --- |
rdetectors,andprequentialevaluation[? ? ? ];(ii)fore- • S5: True concept drift (signal efficacy). Abrupt
castingtoolkitsandarchives(Monash,GluonTS,Darts) orgradualshiftsin∆P(Y|X)thatchangetheuse-
P
for standardized baselines and dataset access [? ? ? fulness or sign of predictive relationships; local
];and(iii)finance-orientedbacktesting/simulationenvi- orglobal; interpretedasmechanismorregimede-
ronments(Gym-likesetups)toevaluateadaptationwith pendingondomainassumptions.
39
This preprint research paper has not been peer reviewed. Electronic copy available at: https://ssrn.com/abstract=6170273

d
e
How this complements existing datasets. This suite model access such as white-box vs. black-box).
is intentionally data-agnostic: it does not prescribe AvoidtuningΠ posthocwtofavoramethod.
s
| a single | dataset, | but | specifies | what | a benchmark |     |           |                |     |         |       |           |
| -------- | -------- | --- | --------- | ---- | ----------- | --- | --------- | -------------- | --- | ------- | ----- | --------- |
|          |          |     |           |      |             |     | 4. Define | the evaluation |     | mapping | E s . | Report at |
suite should cover. For example, index forecasting minimum: (i) detection quality (delay and false-
and macro/indicator monitoring naturally instantiate alarm control), (ii) predictive performance and
| S3/S4; |     |     |     |     |     |     |     |     | e   |     |     |     |
| ------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
contagionandcorrelation-networktasksinstan- calibration under d rift, (iii) computational cost
tiate S1; microstructure datasets support S2/S4; and (wall-clock/memory, including retraining), and
| strategy/feature |     | instability | across | regimes | targets | S5. |     |     |     |     |     |     |
| ---------------- | --- | ----------- | ------ | ------- | ------- | --- | --- | --- | --- | --- | --- | --- |
(iv)finance-speciificutility(e.g.,transactioncosts,
Anomaly/OOD
benchmarks can be used as proxies for turnover, drvawdown, risk-adjusted return). Use
specific cases (most often S4–S5), but should not be consistent protocols and metrics across methods
| treatedasfullsubstitutesforS1–S3unlesstheypreserve |     |     |     |     |     |     | (Section6). |     |     |     |     |     |
| -------------------------------------------------- | --- | --- | --- | --- | --- | --- | ----------- | --- | --- | --- | --- | --- |
e
multivariatedependencestructureandrealistictemporal 5. Establishbaselinesandtuningbudgets. Include
context.
|                                     |     |     |     |     |             |     | non-adaptive  |         | baselines | and simple | adaptive      | base-  |
| ----------------------------------- | --- | --- | --- | --- | ----------- | --- | ------------- | ------- | --------- | ---------- | ------------- | ------ |
|                                     |     |     |     |     |             |     | liners (e.g., | rolling | retrain)  | to         | contextualize | gains. |
| Minimumreportingforcoveragestudies. |     |     |     |     | Foranysuite |     |               |         |           |            |               |        |
= ,ϕ(s),Π )}S Specify hyperparameter tuning budgets and cali-
| instantiationB |          | {(D           | s   | s ,E s | ,authorsshould |         |          |         |        |                   |     |           |
| -------------- | -------- | ------------- | --- | ------ | -------------- | ------- | -------- | ------- | ------ | ----------------- | --- | --------- |
|                |          |               |     | s=1    |                |         | b ration | targets | (e.g., | fixed false-alarm |     | rate/ARL0 |
| report the     | scenario | specification |     | from   | Section        | 7.1 ex- |          |         |        |                   |     |           |
rfordetectors)topreventunfaircomparisons.
| plicitly.                                              | At minimum, |     | this | includes | (i) the | intended |                    |     |           |            |     |         |
| ------------------------------------------------------ | ----------- | --- | ---- | -------- | ------- | -------- | ------------------ | --- | --------- | ---------- | --- | ------- |
|                                                        |             |     |      |          |         |          | 6. Reproducibility |     | checklist | (minimal). |     | Provide |
| driftsignature(s)ϕ(s)(temporal,statistical,spatial,on- |             |     |      |          |         |          | e                  |     |           |            |     |         |
enoughdetailtoreproduceend-to-endresults:data
| tological),(ii)theonlineprotocolΠ |     |     |     | (updatemodeand |     |     |     |     |     |     |     |     |
| --------------------------------- | --- | --- | --- | -------------- | --- | --- | --- | --- | --- | --- | --- | --- |
s
availability/delay, latency/compute provenance and time span; asset identifiers; ex-
| cadence,           | label |               |     |     |           | bud-     |             |             |     |         |      |         |
| ------------------ | ----- | ------------- | --- | --- | --------- | -------- | ----------- | ----------- | --- | ------- | ---- | ------- |
|                    |       |               |     |     |           |          | act feature | computation |     | windows | (and | leakage |
| gets, model-access |       | assumptions), |     | and | (iii) the | evaleua- |             |             |     |         |      |         |
tion mapping E (detection delay and false-alarm con- checks); protocol definition (warm-up length, up-
s
datecadence);detectorcalibrationandthresholds;
trol,predictivelossandcalibration,computationalcost,
|                      |     |           |     |            |             | prandomseeds; |     |     | computeenvironment; |     |     | andcodeto |
| -------------------- | --- | --------- | --- | ---------- | ----------- | ------------- | --- | --- | ------------------- | --- | --- | --------- |
| and finance-specific |     | utility). |     | To support | attribution | of            |     |     |                     |     |     |           |
runthefullpipelinefromdatatometrics.
| improvements, |     | results | should | include | controlled | com- |     |     |     |     |     |     |
| ------------- | --- | ------- | ------ | ------- | ---------- | ---- | --- | --- | --- | --- | --- | --- |
parisonsorablationsthatseparaterepresenta tion,detec-
tion,andadaptationchoices(cf.Section6).
8. DiscussionandFutureDirections
t
7.4. Recipe: constructing financeobenchmarks under This Section complements the research question:
non-stationarity
Whatarethelimitationsandfutureresearchdirections?
To enable consistent benchmark construction across The discussion is organized around four classes of
n
datasetsandresearchcommunities,weproposethefol- threatstovalidityinlearningundernon-stationarity.We
affect
lowing compact recipe. The goal is not to enforce a first examine data- and label-related issues that
singledataset, buttoenfor cecomparableexperimental construct validity (8.1). We then analyze evaluation-

design.
|     |     |     |     |     |     |     | protocol choices | that | introduce | internal | and | statistical- |
| --- | --- | --- | --- | --- | --- | --- | ---------------- | ---- | --------- | -------- | --- | ------------ |
t
|           |      |        |          |            |          |         | conclusionvaliditythreats(8.2). |     |             | Next,wediscussmod- |     |              |
| --------- | ---- | ------ | -------- | ---------- | -------- | ------- | ------------------------------- | --- | ----------- | ------------------ | --- | ------------ |
| 1. Choose | the  | target | drift    | signature. | Select   | a sce-  |                                 |     |             |                    |     |              |
|           |      | n      |          |            |          |         | eling and adaptation            |     | assumptions | that               | can | bias conclu- |
| nario     | from | the    | coverage | suite      | (Section | 7.3) or |                                 |     |             |                    |     |              |
define a new one by specifying ϕ(s) along the sions about robustness under drift (8.3). Finally, we
|             |      |            |     |          |            |        | address finance-specific |     | limitations—such |                             |     | as the “fac- |
| ----------- | ---- | ---------- | --- | -------- | ---------- | ------ | ------------------------ | --- | ---------------- | --------------------------- | --- | ------------ |
| four        | axes | i(Section  | 2). | This     | determines | what   |                          |     |                  |                             |     |              |
|             |      |            |     |          |            |        | tor zoo,” replicability, |     | and              | limited generalization—that |     |              |
| constitutes |      | a “change” |     | and what | should     | be de- |                          |     |                  |                             |     |              |
r
| tectable/adaptable. |     |      |      |                 |     |        | challengeexternalvalidity(8.4). |     |     |     |     |     |
| ------------------- | --- | ---- | ---- | --------------- | --- | ------ | ------------------------------- | --- | --- | --- | --- | --- |
| 2. Inpstantiate     |     | data | D at | the appropriate |     | scale. |                                 |     |     |     |     |     |
s
Choose markets/assets, sampling frequency, pre- 8.1. Data-andlabel-relatedthreats(constructvalidity)
dictionhorizon,andanycontextchannels(macro, Afirstfamilyofthreatsconcernsthequalityofeval-
e
microstructure, text). Make preprocessing rules uation data and the definition of “change labels”. In
explicit(calendar,missingdata,corporateactions, real-world financial time series, there is rarely a pre-
rnormalization). cise ground truth for when drifts occur. As a result,
3. Specify the online protocol Π . Fix the eval- researchers often rely on proxies, such as associating
s
P
uation mode (prequential vs. rolling), update ca- changeswithknownevents(e.g.,marketcrashes)orin-
dence(time-basedorevent-based),labelavailabil- jectingsyntheticdriftsintorealdata. Whilepragmatic,
ity/delay,andconstraints(latency/computebudget;
|     |     |     |     |     |     |     | these strategies | may | fail to | capture | the true | nature of |
| --- | --- | --- | --- | --- | --- | --- | ---------------- | --- | ------- | ------- | -------- | --------- |
40
This preprint research paper has not been peer reviewed. Electronic copy available at: https://ssrn.com/abstract=6170273

d
e
non-stationarity,whichcandirectlyaffectconstructva- methodiscarefullytunedorevaluatedwithouttemporal
lidity: theexperimentalsetupmaynotaccuratelymea- leakage, while others are not.wIn such cases, observed
surethephenomenonitisintendedtoassess. performance gaps reflect experimental bias rather than
This limitation becomes evident when coarse labels methodologicalsuperiority.
are used to summarize complex dynamics. For exam- Statistical-conclusion validity is compromised when
ple,assigningtheentirefinancialcrisisperiodtoasin- performance differences e are reported without sig-
gleregimeX”andthepost-crisistoregimeY”ignores nificance analysis. Many studies claim improve-
thepresenceofmultiplemicrodriftswithineachphase. ments based on small error reductions or detection
i
Insuchcases,methodsthatmerelyreacttolarge,well- gains, without testing whether these differences are
v
defined shocks may appear overly effective. Similarly, robust. In sequential settings, proper tests—such
validationonsyntheticdatawithsimplelinearorabrupt as Diebold–Mariano or paired tests over repeated
e
drifts can lead to overly optimistic conclusions, as de- runs—are required to separate systematic gains from
tectors tuned to these idealized settings often struggle noise.Withoutthem,non-replicableresultsmaybemis-
when faced with the nonlinear, overlapping, and grad- takenforprogress.
r
ualchangesobservedinrealmarkets. Overall,internalandstatistical-validityfailuresimply
Closely related to this issue is the frequent ab- thatre portedgainsmaydisappearunderstrictercontrols
sence—orlowreliability—ofvalidationlabels. Thisis orralternativesamples,inflatingtheperceivedeffective-
particularly problematic in unsupervised detection set- nessofcurrentmethods. Infinancialapplications,these
tings, where evaluation is often indirect or qualitative. eproblems can become more serious. Multiple models
Withoutobjectivecriteria,performanceclaimsmayrely orvariantsareoftentestedonthesamehistoricalsam-
on visual inspection or on the proximity of detected ple, and only the best result is reported. Apparent im-
e
changes to well-known events, leaving room for sub- provementsarelikelydrivenbychanceandoverfitting,
jective interpretation and making systematic compari- withoutcorrectionformultipletesting,forexamplevia
sonacrossmethodsdifficult. pWhite’sRealityCheck[? ],
Addressingthesechallengesopensseveraldirections Futureresearchshouldprioritizecontrolledandstan-
for future research. One avenue is the development of dardized evaluation protocols, in which all methods
better-annotatedbenchmarkdatasets,possib lycombin- should share the same data access, tuning budget, and
ingexpertknowledgewithdata-drivenlatbelingandun- temporal constraints. Performance comparisons must
certaintyquantification.Moregenerally,evaluationpro- include significance testing and repeated runs. In fi-
o
tocolsshouldconstrainadaptationrules,computational nance, multiple-testing corrections should be manda-
budgets,andretrainingstrategiestoensurecomparabil- tory. Suchpracticeswouldreducespuriousresultsand
ity. Detection frequency, falsne-alarm cost, and adapta- enablemorereliableassessmentofprogressundernon-
tion latency should be reported explicitly. In financial stationarity.
settings,downstreammetricsmayincluderisk-adjusted
returns, drawdowns, or tu rnover. This framing shifts
8.3. Modeling-andadaptation-relatedthreats
evaluation from proxy-btased drift detection to robust-
ness and decision-relevant utility under realistic non- Another family of threats arises from modeling as-
n
stationaryconditions. sumptions and from the design of adaptation mecha-
nisms. To make analysis tractable, many studies adopt
8.2. Evaluation-protocol threats (internal and simplifyingassumptionsthatrarelyholdinoperational
i
statistical-conclusionvalidity) settings,whichweakensbothconstructandexternalva-
r
A second family of threats stems from inadequate lidity.
evaluatpionprotocols,whichcanbiasconclusionsabout A central limitation concerns the assumption of in-
drift detectors and adaptation methods. These threats dependencewithin regimes. Much oftheconcept-drift
fallintotwocategories: internalvalidity, relatedtoex- literature models data as i.i.d. until an abrupt change,
e
perimental control, and statistical-conclusion validity, after which a new i.i.d. regime is assumed. In con-
relatedtothestrengthoftheempiricalevidence. trast, financial time series exhibit strong temporal de-
rInternal-validity problems arise when methods are pendence, including autocorrelation and heteroskedas-
not compared under the same conditions. Common is- ticity,evenwithinstableregimes.
P
suesincludeunequalaccesstodataorcomputation,un- Beyondtemporaldependence,manyapproachesalso
even hyperparameter tuning, and inconsistent tempo- assume a fixed feature space. Most methods focus on
ral protocols. In drift studies, it is frequent that one distributionshiftsinthetargetorinobservedcovariates,
41
This preprint research paper has not been peer reviewed. Electronic copy available at: https://ssrn.com/abstract=6170273

d
e
whileignoringfeatureevolution. Inrealsystems,how- tightlycalibratedtopastpatternsoftenstruggletomain-
ever, variables may appear, disappear, or change rele- taintheirpredictiveperformanwceundernewconditions.
vanceovertime.
|     |     |     |     | Future | research | should prioritize |     | broader | and more |
| --- | --- | --- | --- | ------ | -------- | ----------------- | --- | ------- | -------- |
As a consequence, detectors that ignore temporal systematic evaluations across multiple assets and time
structure may respond to volatility clustering or tran- spans, with explicit attention to replicability. Claims
e
sient dynamics rather than to genuine regime changes, aboutspecificregimesshouldbetestedinanalogousset-
producing misleading signals. When this occurs, a de- tings, and greater emphasis should be placed on struc-
tectormaycorrectlyidentifyadistributionshiftbutfail turallygroundedapproachesthatreduceoverfittingand
i
toadaptbecausetheinformativefeaturesthemselvesare enhance generalization, thereby increasing the likeli-
v
notupdated. hood that methods maintain their effectiveness outside
Thesemodelingassumptionsalsopropagatedirectly oftheoriginaltestconditions.
e
to adaptation mechanisms. Evaluation setups often By confronting these limitations honestly and build-
presume that retraining or model updates can be per- ing robust evidence, the field can progress toward pro-
formed at negligible cost and without operational side viding finance practitioners with reliable tools to navi-
r
effects. Inpractice,adaptationintroduceslatency,com- gateaworldofever-changingdata.
| putationaloverhead,andpotentialinstability,especially |     |                  |     |     |     |     |     |     |     |
| ----------------------------------------------------- | --- | ---------------- | --- | --- | --- | --- | --- | --- | --- |
| whenlabelsaredelayedornoisy.                          |     | Whensuchcostsare |     |     |     |     |     |     |     |
r
9. Conclusion
ignored,explainswhymethodsthatperformwellunder
e
| controlled benchmarks | may fail | when exposed | to real |     |     |     |     |     |     |
| --------------------- | -------- | ------------ | ------- | --- | --- | --- | --- | --- | --- |
financialdata. This research organized the literature on machine
|                 |                  |             |      | learning, | econometrics, | and quantitative |     | finance | into a |
| --------------- | ---------------- | ----------- | ---- | --------- | ------------- | ---------------- | --- | ------- | ------ |
| Future research | should therefore | move toward | more |           |               |                  |     |         |        |
e
realistic modeling and evaluation. Methods should be coherent framework specifically focused on financial
|                      |                    |                       |      | timeseries.                | Weproposedafour-axistaxonomytochar- |              |     |           |      |
| -------------------- | ------------------ | --------------------- | ---- | -------------------------- | ----------------------------------- | ------------ | --- | --------- | ---- |
| tested on temporally | dependent          | data with overlapping |      |                            |                                     |              |     |           |      |
|                      |                    |                       |      | acterize non-stationarity, |                                     | encompassing |     | temporal, | sta- |
| sources of change,   | such as concurrent | shiftspin             | mean |                            |                                     |              |     |           |      |
and volatility. Feature evolution should be explicitly tistical, spatial, and ontological dimensions. Exter-
|                               |     |                    |     | nal representations |     | of non-stationarity |     | were | organized |
| ----------------------------- | --- | ------------------ | --- | ------------------- | --- | ------------------- | --- | ---- | --------- |
| modeledratherthanassumedaway. |     | Finally,adaptation |     |                     |     |                     |     |      |           |
costs, delays, and stability effects should b e incorpo- around embeddings, multiscale features, and both en-
|                               |     |                        |     | dogenousandexogenouscontext. |            |                  | Inaddition,westruc- |          |          |
| ----------------------------- | --- | ---------------------- | --- | ---------------------------- | ---------- | ---------------- | ------------------- | -------- | -------- |
| ratedintoevaluationprotocols. |     | Addressintgthesepoints |     |                              |            |                  |                     |          |          |
|                               |     |                        |     | tured the                    | literature | as an end-to-end |                     | pipeline | covering |
isessentialforbridgingthegapbetweenlaboratoryper-
o
formanceandreal-worldrobustness. drift detection, continuous adaptation, evaluation, and
benchmarking.
limitationns: Thestudyshowsthattheliteratureadequatelydefines
| 8.4. Finance-specific |     | “factor zoo”, | repli- |     |     |     |     |     |     |
| --------------------- | --- | ------------- | ------ | --- | --- | --- | --- | --- | --- |
thevariousformsofdrift,providesapproachestorepre-
cability,andgeneralization(externalvalidity)
|     |     |     |     | sent financial | series | and integrate | internal | and | external |
| --- | --- | --- | --- | -------------- | ------ | ------------- | -------- | --- | -------- |
In the financial domain, several challenges threaten information, proposes methods to automatically detect
external validity, that ist, the ability of results to gen- changes,andexploresadaptivemechanismstomaintain
eralize across markets and time periods. A key issue predictive performance over time. Nevertheless, eval-
n
is the factor zoo, in which many reported factors or uationandbenchmarkingpracticesremainunderdevel-
strategies show positive historical performance but fail oped, with limited standardization, weak replicability,
andinsufficientconsiderationofoperationalconstraints.
| toreplicateoutoifsample. | Ananalogousriskarisesfor |     |     |     |     |     |     |     |     |
| ------------------------ | ------------------------ | --- | --- | --- | --- | --- | --- | --- | --- |
learning-based methods, which may become overfitted A key insight is that there is no universally opti-
r
tothecharacteristicsofspecificmarketsandtimewin- mal detector or adaptation strategy. Method selection
dowsraptherthancapturingbroadlystablerelationships. mustalignwiththeexpectedtype,scale,anddynamics
This risk becomes more pronounced in studies that of drift, while deployment decisions must account for
relyonnarrowevaluationsettings,whereamethodmay computational and operational constraints. Evaluation
e
perform well on a specific market or historical period practices should extend beyond predictive accuracy to
butfailtogeneralizetootherassetsortimespans. For include detection delay, false-alarm control, economic
rexample, a regime detector could capture bull–bear al- utility,andrealisticbacktestingthatincorporatestrans-
ternations in US equities between 2000 and 2020 with actioncostsandmarketfrictions.
P highaccuracy,yetitseffectivenessmightnotcarryover
|     |     |     |     | Addressing | these | gaps requires | future | research | fo- |
| --- | --- | --- | --- | ---------- | ----- | ------------- | ------ | -------- | --- |
toemergingmarketsortoearlierhistoricalintervals.As cused on standardized, multi-market benchmarks and
financial structures evolve over time, methods that are decision-centric evaluation protocols that incorporate
42
This preprint research paper has not been peer reviewed. Electronic copy available at: https://ssrn.com/abstract=6170273

d
e
| economic                                          | outcomes, | implementation |     | costs, | and | real- | Dataavailability |     |     |     |
| ------------------------------------------------- | --------- | -------------- | --- | ------ | --- | ----- | ---------------- | --- | --- | --- |
| worlddeploymentconsiderations.Takentogether,these |           |                |     |        |     |       |                  |     | w   |     |
points highlight that methodological performance can- No new datasets were created in this survey. The
|     |     |     |     |     |     |     | bibliographic | metadata | of the reviewed | corpus (Bib- |
| --- | --- | --- | --- | --- | --- | --- | ------------- | -------- | --------------- | ------------ |
notbeseparatedfrompracticalfeasibility.
In conclusion, by offering a unified taxonomy and TeX) and machine-readable versions of the survey ta-
bles(CSV)areavailableefromthecorrespondingauthor
| structured | pipeline, | this | survey | provides | a framework |     |     |     |     |     |
| ---------- | --------- | ---- | ------ | -------- | ----------- | --- | --- | --- | --- | --- |
uponreasonablerequest.Codeusedtogenerateillustra-
| to support | more | comparable | evidence, |     | facilitate | reli- |     |     |     |     |
| ---------- | ---- | ---------- | --------- | --- | ---------- | ----- | --- | --- | --- | --- |
tiveplotsispubliclyavailableintheauthors’repository
| ableimplementation, |                | andstrengthenthefeedbackloop |          |               |     |        |          |            | i                    |                 |
| ------------------- | -------------- | ---------------------------- | -------- | ------------- | --- | ------ | -------- | ---------- | -------------------- | --------------- |
|                     |                |                              |          |               |     |        | (see the | caption of | Fig. 7). Copyrighted | full-text arti- |
| between             | methodological |                              | advances | and practical |     | appli- |          |            |                      |                 |
v
cations in finance, emphasizing that addressing non- cles are not shared. Underlying third-party index data
|              |     |           |             |               |     |        | accessed | via FRED | (e.g., SP500/VIXCLS) | are not re- |
| ------------ | --- | --------- | ----------- | ------------- | --- | ------ | -------- | -------- | -------------------- | ----------- |
| stationarity | in  | financial | time series | is inherently |     | a sys- |          |          |                      |             |
distributed.e
temsproblemspanningrepresentation,detection,adap-
| tation,      | and evaluation |     | under practical |     | and economic |     |             |     |     |     |
| ------------ | -------------- | --- | --------------- | --- | ------------ | --- | ----------- | --- | --- | --- |
| constraints. |                |     |                 |     |              |     | Disclaimrer |     |     |     |
The viewsexpressedinthisarticlearethoseoftheau-
thorsanddonotnecessarilyreflecttheofficialpositions
CRediTauthorshipcontributionstatement
r
oftheirinstitutions.
e
| Davi | M. Cabral: | Data | Curation, | Conceptualization, |     |     |     |     |     |     |
| ---- | ---------- | ---- | --------- | ------------------ | --- | --- | --- | --- | --- | --- |
Methodology,Writing–originaldraft,Writing–review
&editing,Visualization.
e
AdrianoL.I.Oliveira:Supervision,Validation,Writ-
ing–review.
| Gustavo | H.  | F. M. | Oliveira: | Conceptuaplization, |     |     |     |     |     |     |
| ------- | --- | ----- | --------- | ------------------- | --- | --- | --- | --- | --- | --- |
Methodology,Writing–review&editing.
| Adriano  | Lima: | Visualization, |     | Writing | – review | &   |     |     |     |     |
| -------- | ----- | -------------- | --- | ------- | -------- | --- | --- | --- | --- | --- |
| editing. |       |                |     |         |          |     |     |     |     |     |
t
o
| Declaration | of  | generative | AI  | and AI-assisted |     | tech- |     |     |     |     |
| ----------- | --- | ---------- | --- | --------------- | --- | ----- | --- | --- | --- | --- |
nologiesinthemanuscriptpreparationprocess
n
Duringthepreparationofthisworktheauthorsused
ChatGPTtoimprovetheclarityandqualityofthewrit-
| ing. Afterusingthistool/s ervice, |     |     |     | theauthorsreviewed |     |     |     |     |     |     |
| --------------------------------- | --- | --- | --- | ------------------ | --- | --- | --- | --- | --- | --- |
andeditedthecontentastneededandtakefullresponsi-
bilityforthecontentofthepublishedarticle.
n
| Funding |     | i   |     |     |     |     |     |     |     |     |
| ------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
r
Thisresearchdidnotreceiveanyspecificgrantfrom
fundingpagenciesinthepublic,commercial,ornot-for-
profitsectors.
e
DeclarationofCompetingInterests
r
| The authors |     | declare | that they | have no | known | com- |     |     |     |     |
| ----------- | --- | ------- | --------- | ------- | ----- | ---- | --- | --- | --- | --- |
P
| peting financial |          | interests | or personal | relationships |          | that |     |     |     |     |
| ---------------- | -------- | --------- | ----------- | ------------- | -------- | ---- | --- | --- | --- | --- |
| could have       | appeared | to        | influence   | the work      | reported | in   |     |     |     |     |
thispaper.
43
This preprint research paper has not been peer reviewed. Electronic copy available at: https://ssrn.com/abstract=6170273