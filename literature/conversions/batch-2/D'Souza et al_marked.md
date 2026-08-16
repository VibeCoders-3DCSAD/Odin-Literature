---
conversion_metadata:
  converted_at: "2026-07-22T13:03:22Z"
  converter_tool: "markitdown"
  converter_version: "0.1.6"
  source_pdf: "D'Souza et al.pdf"
  source_pdf_sha256: "9027cba26f098b2f73e202f0c93054a5ae44f6dd16e5872938b28839f1dff3d5"
  page_count: 18
  markdown_char_count: 104762
---

<!-- PAGE-AWARE EXTRACTION (via pdfminer.six) -->

<!-- PAGE 1 -->

A Comprehensive Review of Machine Learning
Techniques for Intelligent Personal Finance
Management Systems

Marilyn D’Souza
marilyndsza@gmail.com
Department of Artificial Intelligence and Machine Learning
P.E.S Modern College of Engineering
Pune, Maharashtra, India.

Parth Bhegade
parthbhegade48@gmail.com
Department of Artificial Intelligence and Machine Learning
P.E.S Modern College of Engineering
Pune, Maharashtra, India.

Pooja Bhalekar
poojadorey@gmail.com
Department of Artificial Intelligence and Machine Learning
P.E.S Modern College of Engineering
Pune, Maharashtra, India.

Yash Bhavsar
yashbhavsar520@gmail.com
Department of Artificial Intelligence and Machine Learning
P.E.S Modern College of Engineering
Pune, Maharashtra, India.

Abstract

The swift rise of fintech platforms and smart Personal Finance Management Systems
(PFMS) has significantly changed the way individuals and groups handle their income,
expenses, and financial choices. Although there has been notable advancement, current
research is still scattered across various segments, such as budgeting, expense forecasting,
anomaly detection, explainable financial analytics, and group expense management. This
fragmentation limits the creation of cohesive and intelligent PFMS solutions. This review
delves into the essential elements of contemporary PFMS, which encompass expense track-
ing, bill splitting, predictive budgeting, financial anomaly detection, recommendation sys-
tems, and explainable AI methods. The analysis covers a wide range of approaches, including
statistical methods, machine learning, deep learning, and hybrid techniques, all tailored for
personal and collaborative financial scenarios. By employing a qualitative literature survey
and comparative analysis, this review evaluates the trends, strengths, and weaknesses of
the existing systems. It offers a well-organized taxonomy of PFMS components and pro-
vides comparative insights across various learning methods. Additionally, it pinpoints gaps
in current research to steer future efforts toward developing integrated, explainable, and
user-friendly intelligent finance systems.

Keywords: Personal Finance Management Systems, Machine Learning, Expense Tracking,
Budgeting and Forecasting, Group Expense Management, Anomaly Detection, Explainable Ar-
tificial Intelligence

1

---

<!-- PAGE 2 -->

1

Introduction

In today’s digital age, managing personal and group finances has become a more intricate task.
With online payments, mobile wallets, subscription services, and the shift towards cashless
transactions, individuals find themselves navigating beyond basic income and expense tracking.
They now face the challenge of managing fluctuating spending habits, shared costs, budgeting
limitations, and planning for future financial needs.

This shift has led to an increased reliance on Personal Finance Management Systems (PFMS)
and applications designed for group expense management. These tools are critical in helping
users keep tabs on, analyze, and control their financial activities. However, research indicates
that many existing systems lack the necessary intelligence and adaptability. Most traditional
PFMS serve primarily as digital ledgers, depending on rigid rules, manual sorting, and basic
summaries.

While these tools can assist with fundamental budgeting and expense tracking, they often
fall short in personalization and predictive insights. Likewise, group expense management apps,
like those for splitting bills, tend to concentrate on calculating balances and settlements without
providing deeper analytical insights, spotting anomalies, or offering smart recommendations.

These shortcomings have spurred researchers to look into machine learning techniques to
improve budgeting, forecasting, anomaly detection, and collaborative finance management. Re-
cent studies highlight the use of various machine learning and statistical models across different
elements of PFMS. For instance, budgeting and expense analysis often utilize methods such as
Exponentially Weighted Moving Averages (EWMA), clustering techniques, Random Forests,
ARIMA, and Long Short-Term Memory (LSTM) models to reveal spending patterns and man-
age budget constraints.

Research focused on forecasting applies similar models to scrutinize past financial data and
project future expenses. When it comes to detecting financial anomalies and providing AI-driven
advice, unsupervised and semi-supervised methods like Isolation Forest are explored to spot un-
usual or risky spending behaviors. In the realm of group expense management and bill splitting,
regression-based models—including linear regression and other predictive approaches—are ex-
amined to understand shared spending trends and settlement patterns.

Despite these advancements, the existing literature tends to be scattered. Most studies
address individual components in isolation, with budgeting, forecasting, anomaly detection,
AI recommendations, and group finance rarely examined together within a cohesive PFMS
framework. Furthermore, there’s a lack of comparative analysis across models in these areas,
which makes it challenging to grasp their respective strengths, weaknesses, and suitability for
intelligent personal finance systems.

This review seeks to bridge that gap by systematically exploring and contrasting machine
learning models across various PFMS components, including budgeting, forecasting, anomaly
detection, AI-driven recommendations, and group expense management. By bringing together
insights from available research, this review aspires to offer a clearer understanding of how
different models are implemented, compared, and assessed within intelligent PFMS, thereby
shedding light on current practices and ongoing research challenges.

2 Overview of Personal Finance Management Systems

2.1 Existing System

The existing personal finance management system, also known as PFMS, as discussed in the
literature above, operates on the basis of using deterministic and rule-based driven mechanisms.
All the financial transactions provided by the users are first processed through the predefined
logic for expense based categorisation, aggregation, prediction and budget based validation. An
important factor when it comes to Budgeting in general, are the thresholds that are established

2

---

<!-- PAGE 3 -->

where alerts are generated once the limit exceeds. Detailed summaries are also provided over
the duration of fixed time windows such as daily or monthly periods.

With respect to group expense management systems, overall balances are calculated using
static rules like equal splits or user spending based splitting, followed by manual or semi-
automated settlement tracking. These systems combined, provide a basic monitoring and data
transparency feature, while assuming that the user’s spending behaviour and inputs are always
accurate. This results in the PFMS system becoming reactive in nature, rather than concluding
deterministic outcomes itself- which makes it’s adaptability very limited and contributes to
the inability of recognising patterns in data that are crucial for personalisation and predicitive
insights.

2.2 Proposed Intelligent PFMS

To overcome issues like adaptability, incompliance and inability to work around non-linear
data, recent research introduces the “intelligent PFMS paradigms” that extends beyond the
capabilities of traditional PFMS pipelines, with adaptive and data-driven components. Instead
of relying on rule-based systems, proposed system has integrated learning based mechanisms
for features like budgeting, forecasting, anomaly detection, AI-driven suggestions and group
expense analysis pipelines.

These systems focus on analysing historical financial data to identify behavioural patterns,
support adaptive budget management, and estimate future expenses while also detecting any
irregular or unexpected spending activities. In collaborative finance scenarios, intelligent PFMS
enhances balance analysis and settlement reasoning by incorporating behavioural trends instead
of simply using static splits alone.

The key differentiator for the proposed system lies within its ability to evolve along with
the user data, this allows PFMS to shift from descriptive reporting to decision support. While
these systems improve automation and contextual awareness, the literature also highlights un-
resolved challenges relative to explainability, data quality, privacy and user trust issues. This
indicates that intelligence must be introduced incrementally rather than a complete replacement
of existing structures.

2.3 Mathematical Model

At the system level, PFMS trends can be represented using a common mathematical abstraction
which is suitable for both existing and intelligent paradigms. Let the financial transaction
sequence be defined as:

X = {x1, x2, . . . , xn}

(1)

where each xi represents an individual financial transaction.
In existing PFMS, system outputs such as expense summaries, budget alerts, or group

balances are generated using deterministic mappings:

where g(·) denotes fixed aggregation rules and threshold-based constraints.
In contrast, proposed intelligent PFMS model the financial system as an adaptive mapping:

Y = g(X)

(2)

ˆY = f (X | Θ)

(3)

where Θ represents learned financial behavior patterns used to support budgeting decisions,
forecasting, anomaly identification, and group expense analysis. Despite this difference, both
paradigms follow the same high-level flow:

3

---

<!-- PAGE 4 -->

Input Data → Financial Processing → Decision-Support Output

This abstraction enables a clear comparison between static and intelligent PFMS and pro-

vides a consistent foundation for system-level analysis and diagrammatic representation.

3 Budgeting Techniques in Personal Finance

Budgeting within Personal Finance Management Systems (PFMS) is fundamentally a time-
dependent activity, as individual and group spending behavior changes continuously across
different time horizons. Unlike static financial summaries, effective budgeting requires under-
standing how expenses evolve over time in response to income variations, lifestyle changes,
and external factors. Prior research emphasizes that budgeting mechanisms must account for
historical trends, short-term fluctuations, and long-term behavioral patterns.

Consequently, PFMS budgeting approaches have progressed from static rule enforcement to

statistically driven, behavior-aware, and temporally modeled techniques.

3.1 Rule-based budgeting

Rule-based budgeting constitutes the most basic form of budget control adopted in PFMS. In
this approach, expenses accumulated within a predefined time period are summed and evaluated
against a fixed budget threshold. Let the sequence of expenses within a budgeting interval be
denoted as

The total expenditure is calculated as

X = {x1, x2, . . . , xn}

E =

n
(cid:88)

i=1

xi

and budget compliance is assessed using a deterministic condition:

Alert =

(cid:40)

1,
0,

if E > B
otherwise

(4)

(5)

(6)

Such mechanisms are widely adopted due to their clarity and ease of interpretation. However,
since budget limits remain constant over time, this approach implicitly assumes consistent
spending behavior and offers limited adaptability when financial patterns change.

3.2 Exponentially Weighted Moving Averages (EWMA)

To introduce temporal responsiveness, statistical budgeting techniques have been explored in
PFMS literature. Approaches based on Exponentially Weighted Moving Averages (EWMA)
incorporate past expenditure while assigning greater influence to recent spending activity. The
smoothed expenditure estimate is expressed as

St = αxt + (1 − α)St−1

(7)

where xt represents current expenditure and α controls the weight assigned to recent ob-
servations. EWMA-based budgeting enables gradual adjustment of budget baselines, making
it suitable for monitoring short-term spending trends. Nonetheless, these methods presume
relatively smooth behavioral transitions and may be affected by sudden or irregular expense
patterns.

4

---

<!-- PAGE 5 -->

3.3 Behavior-oriented budgeting

Behavior-oriented budgeting approaches further extend temporal analysis through clustering
techniques that group expenses or users according to similarity in spending behavior over time.
Given a set of financial observations X, clustering partitions the data into multiple behavioral
groups:

X =

K
(cid:91)

k=1

Ck

(8)

Budget estimates are derived from cluster-level characteristics rather than uniform thresh-
olds. This enables PFMS to reflect heterogeneous spending habits across users. However, the
effectiveness of such approaches is closely tied to data quality and historical availability, and
the resulting behavioral groupings may not always be easily interpretable.

3.4 Long Short-Term Memory (LSTM)

Deep learning-based budgeting approaches further generalize time-series modeling by capturing
long-term dependencies in expenditure sequences using Long Short-Term Memory (LSTM) net-
works. LSTM-based formulations regulate information flow through input, forget, and output
mechanisms to retain relevant financial context over extended time horizons.
Future expenditure is estimated as a function of historical observations:

and the corresponding budget is computed using a buffered prediction:

xt+1 = f (Xt)

Bt+1 = xt+1 + δ

(9)

(10)

These approaches support adaptive budgeting aligned with evolving financial behavior, while

introducing challenges related to data dependency and interpretability.

Overall, the reviewed literature indicates a transition from static budget enforcement toward
adaptive and predictive budgeting formulations, reflecting the increasing temporal complexity
of personal financial data.

The figure depicts a comparison between the actual time-series values and the corresponding
predicted values generated during the training phase. The observed series exhibits high short-
term volatility with frequent local fluctuations, reflecting the irregular nature of financial data.
In contrast, the predicted curve follows a smoother trajectory, capturing the underlying trend
while suppressing noise. This behavior indicates that the model emphasizes long-term temporal
patterns rather than reacting to transient variations. Such smoothing is desirable in personal
finance forecasting, where trend awareness is more critical than exact point-wise replication of
short-term fluctuations.

3.4.1 Internal Structure and Functional Mechanism of Long Short-Term Memory

(LSTM)

Long Short-Term Memory (LSTM) networks are described in the literature as advanced re-
current architectures developed to address the challenge of retaining information across long
temporal sequences. Conventional recurrent models often struggle to preserve contextual infor-
mation over extended intervals, particularly when modeling sequential data such as financial
transactions. LSTM overcomes this limitation by incorporating a dedicated memory component
that enables selective storage and controlled modification of information over time.

The internal functioning of an LSTM unit is regulated by three interconnected gating mech-
anisms—namely the forget gate, input gate, and output gate—which interact with a shared

5

---

<!-- PAGE 6 -->

Figure 1: Actual vs Predicted Values using LSTM

internal memory cell. These gates collectively manage the flow of information through the
network and determine how historical and current data are represented.

The forget gate evaluates the relevance of previously stored information and determines
which portions of the historical context should be retained or discarded. In financial modeling
scenarios, this mechanism allows the network to remove outdated spending behaviors while
maintaining persistent patterns that remain significant over time.

ft = σ (Wf · [ht−1, xt] + bf )

(11)

The input gate governs the integration of new information into the internal memory.
It
assesses the importance of recent financial activity and controls how much of this information is
added to the memory state. This selective updating process ensures that new spending trends
are incorporated without disrupting meaningful long-term financial representations.

it = σ (Wi · [ht−1, xt] + bi)

(12)

The internal memory cell serves as a continuous state that accumulates and preserves rel-
evant information across time steps. By combining retained historical patterns with newly
admitted data, the memory cell enables the network to maintain temporal continuity in sequen-
tial representations.

Ct = ft · Ct−1 + it · tanh (WC · [ht−1, xt] + bC)

(13)

The output gate regulates the extent to which the internal memory influences the current
output. It ensures that only contextually relevant information is propagated forward, thereby
shaping subsequent estimates or analytical outcomes.

6

---

<!-- PAGE 7 -->

LSTM architecture is highlighted for its capacity to capture evolving spending behavior
while preserving long-term financial habits. At the same time, the literature acknowledges
challenges related to transparency, interpretability, and computational demands, underscoring
the importance of integrating LSTM-based approaches thoughtfully within broader Personal
Finance Management System frameworks.

Figure 2: LSTM architecture

Building on the system-level workflow, the discussion now focuses on the budgeting pipeline
within Personal Finance Management Systems. This pipeline is examined in terms of how
expenditure data is processed over time to support budget formulation and monitoring. The
subsequent sections review the techniques commonly employed at different stages of the bud-
geting process, highlighting their role in handling temporal spending behavior and uncertainty.

Figure 3: Conceptual Architecture of the Budgeting Pipeline

This Figure illustrates a generalized budgeting pipeline in Personal Finance Management

7

---

<!-- PAGE 8 -->

Systems. Financial transaction data first enters the input stage and undergoes preprocessing
operations, including cleaning, aggregation, and temporal ordering, to ensure data consistency.
The processed data is then transformed through feature engineering, where expenditure values,
categorical information, and time indices are represented for analysis. A temporal modeling layer
applies statistical and learning-based techniques to capture expenditure dynamics and generate
predicted expenditure estimates. These predictions are forwarded to the budgeting stage, where
a safety margin is incorporated during budget formulation to account for uncertainty. The final
output is an adaptive budget representation that evolves with observed spending behavior. The
architecture represents a conceptual workflow synthesized from existing literature rather than
a specific system implementation.

Figure 4: Visualization of budgeting techniques in personal finance management

The diagram illustrates how multiple budgeting techniques analyze the same expenditure
data across time. Actual spending is represented using a histogram, highlighting natural vari-
ability in financial behavior. The EWMA curve demonstrates short-term smoothing by em-
phasizing recent expenditures, while the ARIMA trend reflects linear temporal dependencies
observed in historical data. The LSTM-based curve captures longer-term and non-linear spend-
ing patterns, representing behavioral dynamics that evolve over extended periods. The bud-
get threshold serves as a reference boundary for evaluating budget compliance. Overall, the
diagram conveys how different budgeting approaches provide complementary perspectives on
time-dependent financial behavior rather than competing solutions. Having examined budget-
ing techniques and their temporal behavior, the discussion now shifts to forecasting mechanisms
employed in Personal Finance Management Systems.

4 Forecasting Techniques in Personal Finance

Forecasting represents a fundamental analytical function in Personal Finance Management Sys-
tems (PFMS), enabling a shift from retrospective financial reporting to proactive financial

8

---

<!-- PAGE 9 -->

decision support. By estimating future expenditure trajectories, forecasting mechanisms assist
users in identifying potential budgetary constraints, assessing savings progression, and adapting
spending behavior before financial instability occurs. Beyond aggregate predictions, category-
level forecasting—covering domains such as food, transportation, utilities, and discretionary
expenses—supports structured resource allocation and informed long-term planning. Conse-
quently, forecasting plays a central role in enhancing the intelligence and practical utility of
modern PFMS.

4.1 Statistical Time-Series Models (ARIMA and SARIMA)

Statistical time-series models have traditionally served as the foundation of financial forecasting
due to their mathematical transparency and computational efficiency. Among these, the Au-
toRegressive Integrated Moving Average (ARIMA) model is widely employed to capture linear
temporal dependencies in expenditure data. ARIMA estimates future values as a function of
historical observations and past forecast errors by combining autoregressive, differencing, and
moving average components. The general formulation of an ARIMA model is expressed as

Yt = ϕ1Yt−1 + ϕ2Yt−2 + · · · + ϕpYt−p + θ1ϵt−1 + θ2ϵt−2 + · · · + θqϵt−q + ϵt

(14)

where Yt denotes the stationary time-series value at time t, ϕ represents autoregressive coef-
ficients, and θ denotes moving average parameters. To account for periodic spending behavior
commonly observed in consumer finance, Seasonal ARIMA (SARIMA) extends this formula-
tion by incorporating seasonal components. These statistical models are typically applied in
short-term forecasting scenarios where expenditure trends are relatively stable and stationarity
assumptions are satisfied.

Figure 5: Comparison of ARMA, ARIMA, and SARIMA time-series models

9

---

<!-- PAGE 10 -->

4.2 Machine Learning Regression Approaches

Machine learning regression methods provide an alternative to classical statistical models by
enabling the capture of non-linear relationships within high-dimensional financial data.
In
PFMS literature, ensemble-based regression techniques are frequently examined due to their
robustness and ability to model heterogeneous spending patterns. The effectiveness of these
approaches depends substantially on feature engineering processes that transform raw transac-
tion logs into structured inputs. Common representations include rolling expenditure averages
over fixed temporal windows, trend indicators that reflect spending increases or declines, and
category-specific frequency measures. Such features allow regression models to learn complex
financial interactions that are difficult to represent using linear time-series formulations.

4.3 Deep Learning Methods (LSTM and GRU)

Deep learning architectures are increasingly explored for forecasting tasks involving complex
and long-term temporal dependencies. Recurrent neural models, particularly Long Short-Term
Memory (LSTM) networks, are designed to preserve relevant historical information while adapt-
ing to recent expenditure variations through gated memory mechanisms. This architectural
design enables the modeling of recurring expenses, seasonal patterns, and evolving financial
behavior across extended time horizons.

Gated Recurrent Units (GRU) are also discussed as a computationally efficient alternative,
employing a simplified gating structure while retaining the capacity to model sequential depen-
dencies. Such architectures are often considered in scenarios where computational constraints
or real-time processing requirements limit the applicability of more complex recurrent models.

4.4 Hybrid and Ensemble Forecasting Approaches

To address the limitations associated with standalone forecasting models, recent research inves-
tigates hybrid and ensemble forecasting frameworks that integrate multiple modeling paradigms.
A commonly reported approach combines ARIMA and LSTM outputs, leveraging the strength
of ARIMA in capturing linear temporal trends and the capability of LSTM to model non-linear
residual behavior. In these ensemble formulations, individual model predictions are aggregated
using weighted combinations:

Yt,ensemble = w1 · Yt,ARIMA + w2 · ht,LSTM

(15)

where w1 and w2 represent weighting coefficients optimized through validation procedures.
Such hybrid strategies aim to enhance forecast robustness across varying financial conditions
without relying exclusively on a single modeling assumption.

4.5 Cross-Cutting Discussion

Across forecasting methodologies, several cross-cutting considerations consistently emerge in the
literature. Forecast horizon significantly influences model suitability, with statistical approaches
commonly applied to short-term prediction tasks, while deep learning models are examined for
longer-term forecasting where seasonal and behavioral patterns extend over months or years.
Data availability and quality also play a critical role, as deep learning techniques typically
require substantial historical data and are sensitive to noise, whereas statistical models are
more resilient in data-sparse settings but require stationarity through preprocessing techniques.
Interpretability remains a central concern in PFMS applications. Statistical models are
often regarded as transparent systems, while deep learning approaches introduce opacity that
motivates the integration of explainable artificial intelligence mechanisms to support user trust
and regulatory compliance. Additionally, scalability and deployment constraints are highlighted,

10

---

<!-- PAGE 11 -->

particularly for mobile and web-based PFMS, where computationally intensive models must
be managed through layered system architectures and API-driven services to ensure efficient
operation.

5 AI-Powered Spending Insights and Anomaly Detection

5.1 Distinction Between Anomaly Detection and Fraud Detection

In Personal Finance Management Systems (PFMS), anomaly detection and fraud detection
represent distinct analytical objectives, despite being frequently conflated in financial litera-
ture. Fraud detection is conventionally formulated as a supervised learning problem, relying
on historical datasets annotated with explicit fraud labels to train classification models. Such
formulations are well suited to institutional banking environments where large, labeled datasets
are available.

In contrast, spending anomaly detection within PFMS is inherently an unsupervised task.
Its primary objective is to identify atypical, inefficient, or irregular spending behavior relative
to an individual user’s historical patterns, without requiring predefined labels of undesirable
activity. This distinction arises from the highly personalized nature of spending behavior and
the practical difficulty of generating labeled datasets that define overspending or abnormal
consumption for individual users. As a result, anomaly detection in PFMS focuses on deviation
analysis rather than categorical identification of fraudulent events.

5.2 Rule-Based and Statistical Detection Methods

Early PFMS implementations employ rule-based logic and statistical thresholds as baseline
mechanisms for identifying anomalous spending behavior. These methods typically assume a
stable distribution of expenditure data and flag transactions that exceed expected variability
limits. A common statistical formulation defines an anomaly when current expenditure exceeds
a rolling historical average by a multiple of the observed dispersion:

Anomaly = True if xcurrent > µwindow + k · σwindow

(16)

where µwindow and σwindow denote the mean and standard deviation computed over a recent
temporal window, and k is a predefined scaling factor. While such approaches are computation-
ally efficient and easily interpretable, their effectiveness is limited in PFMS contexts. They are
unable to account for multi-feature spending behavior or adapt to seasonal and lifestyle-driven
expenditure shifts, often resulting in elevated false-positive rates during events such as holidays
or one-time purchases.

5.3 Unsupervised Machine Learning Approaches

Given the absence of labeled data and the inherently imbalanced nature of personal finan-
cial records, unsupervised learning techniques dominate anomaly detection research in PFMS.
Among these, Isolation Forest is frequently discussed due to its deviation-centric design. Rather
than modeling normal behavior, this approach isolates anomalous observations through recursive
partitioning, operating on the premise that anomalies are both rare and structurally distinct.

An anomaly score is computed based on the average path length required to isolate an

observation across an ensemble of isolation trees, expressed as:

where E(h(x)) represents the expected path length and c(ψ) denotes the normalization fac-
tor derived from random binary tree properties. Higher scores indicate a greater likelihood

s(x, ψ) = 2− E(h(x))

c(ψ)

(17)

11

---

<!-- PAGE 12 -->

of anomalous behavior. Comparative studies reported in the literature consistently demon-
strate that Isolation Forest achieves superior detection capability relative to density-based and
boundary-based alternatives, which often suffer from scalability limitations or sensitivity to
parameter selection in PFMS environments.

5.4 Deep Learning-Based Anomaly Detection

Deep learning architectures are explored for anomaly detection in PFMS when spending behav-
ior exhibits complex, non-linear patterns across high-dimensional feature spaces. Autoencoder-
based models are commonly examined in this context, where the network learns a compressed
representation of typical spending behavior and identifies anomalies based on elevated recon-
struction error.

Despite their expressive power, deep learning approaches introduce practical challenges in
PFMS deployment. These models typically require large volumes of high-quality training data
and impose substantial computational overhead, which can limit real-time responsiveness in
mobile or resource-constrained environments. Consequently, their adoption in mid-scale PFMS
applications is often restricted to offline analysis or exploratory use rather than continuous
monitoring.

5.5 Explainable Artificial Intelligence (XAI) Considerations

As PFMS transition from rule-based detection to learning-driven anomaly identification, issues
of transparency and user trust become increasingly significant. Complex machine learning
models often function as opaque systems, generating alerts without clear justification, which
can reduce user confidence and adoption. In financial decision-support applications, the ability
to explain detected anomalies is as critical as the detection itself.

To address this challenge, explainable artificial intelligence techniques are increasingly in-
corporated into PFMS pipelines. Post-hoc interpretability methods are applied to attribute
anomaly decisions to specific spending features, enabling the generation of human-readable ex-
planations. Additionally, attention-based mechanisms integrated within learning models high-
light historical transactions that most strongly influenced anomaly detection outcomes.

The literature frequently advocates hybrid system designs in which unsupervised learning
models perform anomaly detection, while rule-based or statistical logic is employed to generate
interpretable explanations. Such hybrid implementations aim to balance analytical rigor with
usability, ensuring that PFMS remain both technically robust and user-centric.

6 Group Expense Management and Collaborative Finance

6.1 Traditional Bill-Splitting Systems

Group expense management has traditionally been handled through manual and semi-digital
methods, including spreadsheets, handwritten records, and basic ledger-based applications. In
social and domestic contexts—such as shared travel, dining, or household utilities—tracking
individual contributions accurately often becomes cumbersome. Early mobile applications for
group finance typically function as electronic ledgers, requiring users to manually record trans-
actions and assign participants for each expense. These systems commonly rely on static,
rule-based logic, such as equal splitting, which fails to capture real-world variations where par-
ticipants contribute unevenly. As a result, such approaches are prone to data entry errors,
inconsistencies, and limited transparency, frequently leading to confusion and interpersonal
friction within groups.

12

---

<!-- PAGE 13 -->

Figure 6: Anomaly detection using One-Class SVM

6.2 Graph-Based Settlement Optimization

To address the complexity inherent in multi-party debt resolution, contemporary group expense
management systems incorporate graph-based settlement optimization techniques. In this for-
mulation, group members are represented as nodes, while financial obligations are modeled as
directed edges within a graph structure. Individual expenses are aggregated to compute net
balances for each participant, and optimization algorithms are applied to minimize the total
number of transactions required to settle group debts. Rather than executing numerous pair-
wise payments, the system recommends a reduced set of settlement transactions that efficiently
balance obligations across the group. This approach improves clarity, reduces administrative
overhead, and ensures consistency in large or frequently interacting groups.

6.3 Behavioral Analysis in Group Finance

Recent developments in collaborative finance emphasize behavioral and event-centric perspec-
tives on shared expenses. Instead of treating expenses as isolated transactions, intelligent sys-
tems organize group spending around contextual events, such as trips, social gatherings, or
recurring activities. This event-based organization enhances transparency by associating ex-
penses, discussions, and settlements within a unified context. Dashboards summarizing group-
level spending trends over monthly or annual periods enable participants to assess collective
financial behavior and identify recurring patterns.

To further reduce manual effort, optical character recognition (OCR) technologies are in-
creasingly integrated into group finance workflows. By automatically extracting item descrip-
tions, prices, and totals from receipts, OCR-enabled systems streamline expense entry and
reduce errors associated with manual transcription. This automation supports real-time collab-
oration while lowering the cognitive burden on users managing shared financial records.

6.4 Machine Learning–Based Payer Prediction and Expense Allocation

Advances in predictive analytics have enabled group expense management systems to evolve
from passive tracking tools into proactive collaborative assistants. Machine learning techniques
are applied to identify recurring behavioral patterns within groups and estimate the most likely
payer for a newly recorded expense. In parallel, regression-based models are explored to recom-

13

---

<!-- PAGE 14 -->

mend expense allocation ratios that reflect historical contribution behavior rather than uniform
splits.

At a conceptual level, allocation logic can be expressed as a functional mapping between

historical behavior and contextual attributes:

Member Share = f (Historical Contribution, Group Persona, Event Type)

(18)

By analyzing prior transactions and group dynamics, such systems can suggest personalized
allocation strategies and notify users when projected spending approaches predefined group
thresholds. The integration of classification for payer prediction and regression for allocation
enhances coordination, reduces disputes, and supports more equitable financial collaboration
within groups.

7 Comparative Analysis of Techniques

This section provides a qualitative synthesis of the methodological characteristics, data de-
pendencies, and operational trade-offs associated with the techniques surveyed in this review.
Rather than establishing hierarchical rankings, the analysis focuses on how architectural as-
sumptions and modeling constraints align with distinct objectives in personal finance manage-
ment. The discussion highlights interpretability, scalability, adaptability, and data requirements
as central dimensions influencing methodological suitability.

7.1 Comparative Analysis of Budgeting Techniques

Budgeting mechanisms in Personal Finance Management Systems (PFMS) span a spectrum
ranging from lightweight statistical heuristics to memory-driven deep learning architectures.
The choice of budgeting technique is largely influenced by the balance between decision trans-
parency and the capacity to capture complex behavioral patterns.

Table 1: Qualitative Comparison of Budgeting Techniques

Interpretability Scalability

Adaptability

Data Require-
ments
Low (minimal his-
tory)
Medium (feature
vectors)

/

Technique

EWMA

Clustering
(K-Means
GMM)
ARIMA

High (transparent
logic)
Medium (cluster
centroids)

(recur-

High
sive updates)
High
beled data)

(unla-

Medium (station-
ary series)

High (statistical
formulation)

Low (category-
wise modeling)

LSTM

(long

High
quences)

se-

Low (opaque rep-
resentations)

Medium
(resource
tensive)

in-

(stable

Low
habits only)
Medium
(pattern-
based)
Medium
(trend
ture)
Very
(temporal
shifts)

cap-

High

From a conceptual standpoint, budgeting approaches reflect a trade-off between temporal
awareness and behavioral expressiveness. Statistical methods such as EWMA and ARIMA
provide clear and interpretable mechanisms with low computational overhead, making them
suitable for users whose spending behavior remains relatively stable over time. However, these
approaches struggle to accommodate non-linear changes and seasonal variations. Clustering-
based methods introduce a behavioral abstraction by grouping users or transactions into spend-
In contrast,
ing profiles, though they disregard transaction order and temporal evolution.

14

---

<!-- PAGE 15 -->

LSTM-based models excel at capturing long-range dependencies across multiple spending cat-
egories but require substantial historical data and computational resources, which may limit
applicability for users with sparse financial records.

7.2 Comparative Analysis of Forecasting Techniques

Expenditure forecasting in PFMS involves balancing the stability of linear trend modeling with
the flexibility required to represent non-linear and evolving financial dynamics.

Table 2: Qualitative Comparison of Forecasting Techniques

Technique

ARIMA
SARIMA

/

Data Require-
ments
Low to Medium

High (linear for-
mulation)

Low (parame-
ter tuning)

Interpretability Scalability

Adaptability

LSTM / GRU High

(large

datasets)

Low
states)

(hidden

Hybrid
(ARIMA–
LSTM)

High (dual-stage
modeling)

Medium (partial
transparency)

Medium (com-
putational
overhead)
Medium (in-
tegration
complexity)

(sta-

Low
tionarity
constraints)
(non-
High
linear dynam-
ics)
High
Very
(linear + non-
linear)

The primary distinction among forecasting approaches lies in linear robustness versus non-
linear flexibility. ARIMA-based models effectively capture autocorrelations and linear temporal
dependencies, as expressed by:

Yt = ϕ1Yt−1 + · · · + θ1ϵt−1 + ϵt

(19)

This formulation supports reliable short-term forecasting under stationary conditions but
fails to represent complex behavioral shifts. Deep learning models, such as LSTM and GRU,
address this limitation by modeling non-linear temporal relationships through memory mecha-
nisms, albeit at the cost of increased computational demands and sensitivity to noise. Hybrid
ARIMA–LSTM frameworks aim to reconcile these paradigms by extracting linear trends via
ARIMA and modeling residual non-linear components using LSTM:

Yt,ensemble = w1 · Yt,ARIMA + w2 · ht,LSTM

(20)

While such integration enhances forecasting robustness across heterogeneous financial con-

texts, it introduces additional architectural complexity and resource overhead.

7.3 Comparative Analysis of Anomaly Detection Techniques

Anomaly detection within PFMS is primarily formulated as an unsupervised learning problem,
given the absence of labeled data defining undesirable or inefficient spending behavior.

The selection of an anomaly detection strategy reflects a balance between simplicity and
expressive power. Rule-based systems provide transparent and verifiable baselines but lack the
capacity to model multi-dimensional spending behavior or adapt to seasonal variation. Isolation
Forest represents a paradigm shift by isolating anomalies directly through random partitioning
rather than modeling normal behavior. Its anomaly scoring mechanism is defined as:

s(x, ψ) = 2− E(h(x))

c(ψ)

(21)

15

---

<!-- PAGE 16 -->

Table 3: Qualitative Comparison of Anomaly Detection Techniques

Technique

Rule-Based

Isolation For-
est
One-Class
SVM

Data Require-
ments
Low
rules)
Low to Medium

(manual

Medium

Interpretability Scalability

Adaptability

Very High

Medium (requires
XAI)
Low

(low

High
cost)
Very
(O(n log n))
Low (memory
intensive)

High

Low

Very
(rigid logic)
High (feature-
agnostic)
Medium

This formulation enables efficient and scalable detection in large, unlabeled datasets, though
it does not inherently provide explanatory context. More complex methods, such as One-
Class SVM and Autoencoders, offer enhanced detection capabilities for intricate anomalies
but suffer from poor scalability and high computational cost, particularly in mobile or real-
time PFMS environments. As a result, contemporary systems often adopt hybrid designs,
combining unsupervised detection mechanisms with rule-based or explainable AI layers to ensure
interpretability and user trust.

8 Conclusion

The evolution of Personal Finance Management Systems (PFMS) reflects a broader shift from
static, rule-based record-keeping tools toward intelligent, data-driven decision-support plat-
forms. This transition is characterized by the convergence of four core analytical dimensions:
adaptive budgeting, expenditure forecasting, anomaly detection, and collaborative group fi-
nance. Across the literature, budgeting mechanisms have progressed from fixed heuristics to
behavior-aware approaches that incorporate temporal context and spending patterns to support
personalized financial limits. Forecasting studies similarly demonstrate a movement toward hy-
brid modeling strategies, where statistical time-series methods are combined with learning-based
approaches to improve robustness across diverse financial conditions.

Anomaly detection research within PFMS has increasingly favored unsupervised methodolo-
gies, motivated by the absence of labeled personal spending data and the highly individualized
nature of financial behavior. Techniques designed to isolate deviations rather than classify pre-
defined outcomes have enabled scalable identification of unusual spending patterns. In parallel,
group expense management systems have advanced beyond manual tracking by incorporating
automated settlement optimization, event-centric organization, and receipt digitization, thereby
reducing administrative overhead and improving transparency in shared financial contexts.

Machine learning functions as a central enabler across these developments, facilitating the
identification of complex patterns and long-term dependencies that are difficult to capture using
traditional analytical methods. However, the growing reliance on complex models has also
emphasized the importance of explainability, with explainable artificial intelligence emerging as
a critical requirement for user trust and accountability in financial decision-support systems.

Despite substantial progress at the component level, existing research remains fragmented,
with limited emphasis on unified system-level integration. The literature consistently indi-
cates the need for cohesive intelligent PFMS frameworks that integrate budgeting, forecasting,
anomaly detection, and collaborative finance within a single platform. Advancing toward such
unified ecosystems represents a key direction for future research, with the potential to provide
users with comprehensive financial insights, enhance financial literacy, and support long-term
financial stability in an increasingly dynamic digital economy.

16

---

<!-- PAGE 17 -->

Acknowledgments

This work was carried out under the supervision of Professor Rupali Panpaliya. The author(s)
gratefully acknowledge her guidance, academic oversight, and constructive feedback, which con-
tributed significantly to the development and completion of this study.

References

[1] S. Hochreiter and J. Schmidhuber, “Long Short-Term Memory,” Neural Computation, vol.

9, no. 8, pp. 1735–1780, 1997.

[2] G. E. P. Box and G. M. Jenkins, Time Series Analysis: Forecasting and Control, Holden

Day, 1970.

[3] F. T. Liu, K. M. Ting, and Z. H. Zhou, “Isolation Forest,” Proceedings of the IEEE Inter-

national Conference on Data Mining (ICDM), pp. 413–422, 2008.

[4] G. P. Zhang, “Time Series Forecasting Using a Hybrid ARIMA and Neural Network

Model,” Neurocomputing, vol. 50, pp. 159–175, 2003.

[5] M. Khashei and M. Bijari, “A Novel Hybridization of Artificial Neural Networks and
ARIMA Models for Time Series Forecasting,” Applied Soft Computing, vol. 11, no. 2,
pp. 2664–2675, 2011.

[6] O. B. Sezer, M. U. Gudelek, and A. M. Ozbayoglu, “Financial Time Series Forecasting with
Deep Learning: A Systematic Literature Review (2005–2019),” Applied Soft Computing,
vol. 90, 2020.

[7] S. Makridakis, E. Spiliotis, and V. Assimakopoulos, “The M4 Competition: Results, Find-
ings, Conclusion and Way Forward,” International Journal of Forecasting, vol. 36, no. 1,
pp. 54–74, 2020.

[8] Y. Qin, D. Song, H. Chen, W. Cheng, G. Jiang, and G. Cottrell, “A Dual-Stage Attention-
Based Recurrent Neural Network for Time Series Prediction,” Proceedings of IJCAI, 2017.

[9] B. Lim, S. O. Arik, N. Loeff, and T. Pfister, “Temporal Fusion Transformers for Inter-
pretable Multi-Horizon Time Series Forecasting,” International Journal of Forecasting, vol.
37, no. 4, pp. 1748–1764, 2021.

[10] V. Chandola, A. Banerjee, and V. Kumar, “Anomaly Detection: A Survey,” ACM Com-

puting Surveys, vol. 41, no. 3, 2009.

[11] L. Ruff et al., “Deep One-Class Classification,” Proceedings of the 35th International Con-

ference on Machine Learning (ICML), 2018.

[12] M. T. Ribeiro, S. Singh, and C. Guestrin, “Why Should I Trust You? Explaining the Predic-
tions of Any Classifier,” Proceedings of the 22nd ACM SIGKDD Conference on Knowledge
Discovery and Data Mining, 2016.

[13] S. M. Lundberg and S. I. Lee, “A Unified Approach to Interpreting Model Predictions,”

Advances in Neural Information Processing Systems (NeurIPS), 2017.

[14] M. E. Celebi, H. A. Kingravi, and P. A. Vela, “A Comparative Study of Efficient Initializa-
tion Methods for the K-Means Clustering Algorithm,” Expert Systems with Applications,
vol. 40, no. 1, pp. 200–210, 2013.

17

---

<!-- PAGE 18 -->

[15] Z. Chen, C. Li, and W. Sun, “Bitcoin Price Prediction using Machine Learning: An Ap-
proach to Sample Dimension Engineering,” Journal of Computational and Applied Mathe-
matics, vol. 365, 2020.

18

<!-- MARKITDOWN CONVERSION -->

<!-- Full MarkItDown conversion for formatting fidelity. -->

| A Comprehensive |     |            |             | Review  | of Machine | Learning |
| --------------- | --- | ---------- | ----------- | ------- | ---------- | -------- |
| Techniques      |     | for        | Intelligent |         | Personal   | Finance  |
|                 |     | Management |             |         | Systems    |          |
|                 |     |            | Marilyn     | D’Souza |            |          |
marilyndsza@gmail.com
|     | Department | of    | Artificial | Intelligence  | and Machine    | Learning |
| --- | ---------- | ----- | ---------- | ------------- | -------------- | -------- |
|     |            | P.E.S | Modern     | College       | of Engineering |          |
|     |            |       | Pune,      | Maharashtra,  | India.         |          |
|     |            |       |            | Parth Bhegade |                |          |
parthbhegade48@gmail.com
|     | Department | of    | Artificial | Intelligence | and Machine    | Learning |
| --- | ---------- | ----- | ---------- | ------------ | -------------- | -------- |
|     |            | P.E.S | Modern     | College      | of Engineering |          |
|     |            |       | Pune,      | Maharashtra, | India.         |          |
|     |            |       | Pooja      | Bhalekar     |                |          |
poojadorey@gmail.com
|     | Department | of    | Artificial | Intelligence | and Machine    | Learning |
| --- | ---------- | ----- | ---------- | ------------ | -------------- | -------- |
|     |            | P.E.S | Modern     | College      | of Engineering |          |
|     |            |       | Pune,      | Maharashtra, | India.         |          |
|     |            |       |            | Yash Bhavsar |                |          |
yashbhavsar520@gmail.com
|     | Department | of    | Artificial | Intelligence | and Machine    | Learning |
| --- | ---------- | ----- | ---------- | ------------ | -------------- | -------- |
|     |            | P.E.S | Modern     | College      | of Engineering |          |
|     |            |       | Pune,      | Maharashtra, | India.         |          |
Abstract
The swift rise of fintech platforms and smart Personal Finance Management Systems
(PFMS) has significantly changed the way individuals and groups handle their income,
expenses, and financial choices. Although there has been notable advancement, current
research is still scattered across various segments, such as budgeting, expense forecasting,
anomaly detection, explainable financial analytics, and group expense management. This
fragmentation limits the creation of cohesive and intelligent PFMS solutions. This review
delves into the essential elements of contemporary PFMS, which encompass expense track-
ing, bill splitting, predictive budgeting, financial anomaly detection, recommendation sys-
tems,andexplainableAImethods. Theanalysiscoversawiderangeofapproaches,including
statistical methods, machine learning, deep learning, and hybrid techniques, all tailored for
personal and collaborative financial scenarios. By employing a qualitative literature survey
and comparative analysis, this review evaluates the trends, strengths, and weaknesses of
the existing systems. It offers a well-organized taxonomy of PFMS components and pro-
vides comparative insights across various learning methods. Additionally, it pinpoints gaps
in current research to steer future efforts toward developing integrated, explainable, and
| user-friendly | intelligent | finance | systems. |     |     |     |
| ------------- | ----------- | ------- | -------- | --- | --- | --- |
Keywords: Personal Finance Management Systems, Machine Learning, Expense Tracking,
Budgeting and Forecasting, Group Expense Management, Anomaly Detection, Explainable Ar-
tificial Intelligence
1

1 Introduction
In today’s digital age, managing personal and group finances has become a more intricate task.
With online payments, mobile wallets, subscription services, and the shift towards cashless
transactions, individuals find themselves navigating beyond basic income and expense tracking.
They now face the challenge of managing fluctuating spending habits, shared costs, budgeting
limitations, and planning for future financial needs.
ThisshifthasledtoanincreasedrelianceonPersonalFinanceManagementSystems(PFMS)
and applications designed for group expense management. These tools are critical in helping
users keep tabs on, analyze, and control their financial activities. However, research indicates
that many existing systems lack the necessary intelligence and adaptability. Most traditional
PFMS serve primarily as digital ledgers, depending on rigid rules, manual sorting, and basic
summaries.
While these tools can assist with fundamental budgeting and expense tracking, they often
fall short in personalization and predictive insights. Likewise, group expense management apps,
likethoseforsplittingbills, tendtoconcentrateoncalculatingbalancesandsettlementswithout
providing deeper analytical insights, spotting anomalies, or offering smart recommendations.
These shortcomings have spurred researchers to look into machine learning techniques to
improve budgeting, forecasting, anomaly detection, and collaborative finance management. Re-
cent studies highlight the use of various machine learning and statistical models across different
elements of PFMS. For instance, budgeting and expense analysis often utilize methods such as
Exponentially Weighted Moving Averages (EWMA), clustering techniques, Random Forests,
ARIMA, and Long Short-Term Memory (LSTM) models to reveal spending patterns and man-
age budget constraints.
Research focused on forecasting applies similar models to scrutinize past financial data and
projectfutureexpenses. WhenitcomestodetectingfinancialanomaliesandprovidingAI-driven
advice, unsupervised and semi-supervised methods like Isolation Forest are explored to spot un-
usualorriskyspendingbehaviors. Intherealmofgroupexpensemanagementandbillsplitting,
regression-based models—including linear regression and other predictive approaches—are ex-
amined to understand shared spending trends and settlement patterns.
Despite these advancements, the existing literature tends to be scattered. Most studies
address individual components in isolation, with budgeting, forecasting, anomaly detection,
AI recommendations, and group finance rarely examined together within a cohesive PFMS
framework. Furthermore, there’s a lack of comparative analysis across models in these areas,
which makes it challenging to grasp their respective strengths, weaknesses, and suitability for
intelligent personal finance systems.
This review seeks to bridge that gap by systematically exploring and contrasting machine
learning models across various PFMS components, including budgeting, forecasting, anomaly
detection, AI-driven recommendations, and group expense management. By bringing together
insights from available research, this review aspires to offer a clearer understanding of how
different models are implemented, compared, and assessed within intelligent PFMS, thereby
shedding light on current practices and ongoing research challenges.
2 Overview of Personal Finance Management Systems
2.1 Existing System
The existing personal finance management system, also known as PFMS, as discussed in the
literatureabove, operatesonthebasisofusingdeterministicandrule-baseddrivenmechanisms.
All the financial transactions provided by the users are first processed through the predefined
logic for expense based categorisation, aggregation, prediction and budget based validation. An
important factor when it comes to Budgeting in general, are the thresholds that are established
2

where alerts are generated once the limit exceeds. Detailed summaries are also provided over
the duration of fixed time windows such as daily or monthly periods.
With respect to group expense management systems, overall balances are calculated using
static rules like equal splits or user spending based splitting, followed by manual or semi-
automated settlement tracking. These systems combined, provide a basic monitoring and data
transparency feature, while assuming that the user’s spending behaviour and inputs are always
accurate. This results in the PFMS system becoming reactive in nature, rather than concluding
deterministic outcomes itself- which makes it’s adaptability very limited and contributes to
the inability of recognising patterns in data that are crucial for personalisation and predicitive
insights.
| 2.2 Proposed |     | Intelligent | PFMS |     |     |     |     |
| ------------ | --- | ----------- | ---- | --- | --- | --- | --- |
To overcome issues like adaptability, incompliance and inability to work around non-linear
data, recent research introduces the “intelligent PFMS paradigms” that extends beyond the
capabilities of traditional PFMS pipelines, with adaptive and data-driven components. Instead
of relying on rule-based systems, proposed system has integrated learning based mechanisms
for features like budgeting, forecasting, anomaly detection, AI-driven suggestions and group
| expense | analysis | pipelines. |     |     |     |     |     |
| ------- | -------- | ---------- | --- | --- | --- | --- | --- |
These systems focus on analysing historical financial data to identify behavioural patterns,
support adaptive budget management, and estimate future expenses while also detecting any
irregularorunexpectedspendingactivities. Incollaborativefinancescenarios, intelligentPFMS
enhancesbalanceanalysisandsettlementreasoningbyincorporatingbehaviouraltrendsinstead
| of simply | using | static splits | alone. |     |     |     |     |
| --------- | ----- | ------------- | ------ | --- | --- | --- | --- |
The key differentiator for the proposed system lies within its ability to evolve along with
the user data, this allows PFMS to shift from descriptive reporting to decision support. While
these systems improve automation and contextual awareness, the literature also highlights un-
resolved challenges relative to explainability, data quality, privacy and user trust issues. This
indicatesthatintelligencemustbeintroducedincrementallyratherthanacompletereplacement
| of existing      | structures. |     |       |     |     |     |     |
| ---------------- | ----------- | --- | ----- | --- | --- | --- | --- |
| 2.3 Mathematical |             |     | Model |     |     |     |     |
Atthesystemlevel,PFMStrendscanberepresentedusingacommonmathematicalabstraction
which is suitable for both existing and intelligent paradigms. Let the financial transaction
| sequence | be defined | as:          |               |     |           |              |     |
| -------- | ---------- | ------------ | ------------- | --- | --------- | ------------ | --- |
|          |            |              |               | X   | = {x      | ,x ,...,x }  | (1) |
|          |            |              |               |     | 1         | 2 n          |     |
| where    | each       | x represents | an individual |     | financial | transaction. |     |
i
In existing PFMS, system outputs such as expense summaries, budget alerts, or group
| balances | are generated | using | deterministic |     | mappings: |        |     |
| -------- | ------------- | ----- | ------------- | --- | --------- | ------ | --- |
|          |               |       |               |     | Y         | = g(X) | (2) |
where g(·) denotes fixed aggregation rules and threshold-based constraints.
In contrast, proposed intelligent PFMS model the financial system as an adaptive mapping:
|     |     |     |     |     | Yˆ = | f(X | Θ) | (3) |
| --- | --- | --- | --- | --- | ---- | -------- | --- |
where Θ represents learned financial behavior patterns used to support budgeting decisions,
forecasting, anomaly identification, and group expense analysis. Despite this difference, both
| paradigms | follow | the same | high-level | flow: |     |     |     |
| --------- | ------ | -------- | ---------- | ----- | --- | --- | --- |
3

|     | Input | Data | → Financial | Processing |     | → Decision-Support | Output |     |
| --- | ----- | ---- | ----------- | ---------- | --- | ------------------ | ------ | --- |
This abstraction enables a clear comparison between static and intelligent PFMS and pro-
vides a consistent foundation for system-level analysis and diagrammatic representation.
| 3 Budgeting |     | Techniques |     | in Personal |     | Finance |     |     |
| ----------- | --- | ---------- | --- | ----------- | --- | ------- | --- | --- |
Budgeting within Personal Finance Management Systems (PFMS) is fundamentally a time-
dependent activity, as individual and group spending behavior changes continuously across
different time horizons. Unlike static financial summaries, effective budgeting requires under-
standing how expenses evolve over time in response to income variations, lifestyle changes,
and external factors. Prior research emphasizes that budgeting mechanisms must account for
historical trends, short-term fluctuations, and long-term behavioral patterns.
Consequently, PFMS budgeting approaches have progressed from static rule enforcement to
statistically driven, behavior-aware, and temporally modeled techniques.
| 3.1 | Rule-based | budgeting |     |     |     |     |     |     |
| --- | ---------- | --------- | --- | --- | --- | --- | --- | --- |
Rule-based budgeting constitutes the most basic form of budget control adopted in PFMS. In
thisapproach,expensesaccumulatedwithinapredefinedtimeperiodaresummedandevaluated
against a fixed budget threshold. Let the sequence of expenses within a budgeting interval be
| denoted | as  |     |     |        |           |     |     |     |
| ------- | --- | --- | --- | ------ | --------- | --- | --- | --- |
|         |     |     |     | X = {x | ,x ,...,x | }   |     | (4) |
1 2 n
| The | total expenditure |     | is calculated | as  |     |     |     |     |
| --- | ----------------- | --- | ------------- | --- | --- | --- | --- | --- |
n
(cid:88)
|     |     |     |     | E = | x   |     |     | (5) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
i
i=1
| and | budget compliance |     | is assessed | using a | deterministic | condition: |     |     |
| --- | ----------------- | --- | ----------- | ------- | ------------- | ---------- | --- | --- |
(cid:40)
1, if E > B
|     |     |     |     | Alert = |     |     |     | (6) |
| --- | --- | --- | --- | ------- | --- | --- | --- | --- |
0, otherwise
Suchmechanismsarewidelyadoptedduetotheirclarityandeaseofinterpretation. However,
since budget limits remain constant over time, this approach implicitly assumes consistent
spending behavior and offers limited adaptability when financial patterns change.
| 3.2 | Exponentially |     | Weighted | Moving | Averages | (EWMA) |     |     |
| --- | ------------- | --- | -------- | ------ | -------- | ------ | --- | --- |
To introduce temporal responsiveness, statistical budgeting techniques have been explored in
PFMS literature. Approaches based on Exponentially Weighted Moving Averages (EWMA)
incorporate past expenditure while assigning greater influence to recent spending activity. The
| smoothed | expenditure | estimate |     | is expressed as |         |     |     |     |
| -------- | ----------- | -------- | --- | --------------- | ------- | --- | --- | --- |
|          |             |          |     | S t = αx t      | +(1−α)S | t−1 |     | (7) |
where x t represents current expenditure and α controls the weight assigned to recent ob-
servations. EWMA-based budgeting enables gradual adjustment of budget baselines, making
it suitable for monitoring short-term spending trends. Nonetheless, these methods presume
relatively smooth behavioral transitions and may be affected by sudden or irregular expense
patterns.
4

3.3 Behavior-oriented budgeting
Behavior-oriented budgeting approaches further extend temporal analysis through clustering
techniques that group expenses or users according to similarity in spending behavior over time.
Given a set of financial observations X, clustering partitions the data into multiple behavioral
groups:
K
(cid:91)
X = C (8)
k
k=1
Budget estimates are derived from cluster-level characteristics rather than uniform thresh-
olds. This enables PFMS to reflect heterogeneous spending habits across users. However, the
effectiveness of such approaches is closely tied to data quality and historical availability, and
the resulting behavioral groupings may not always be easily interpretable.
3.4 Long Short-Term Memory (LSTM)
Deep learning-based budgeting approaches further generalize time-series modeling by capturing
long-term dependencies in expenditure sequences using Long Short-Term Memory (LSTM) net-
works. LSTM-based formulations regulate information flow through input, forget, and output
mechanisms to retain relevant financial context over extended time horizons.
Future expenditure is estimated as a function of historical observations:
x = f(X ) (9)
t+1 t
and the corresponding budget is computed using a buffered prediction:
B = x +δ (10)
t+1 t+1
Theseapproachessupportadaptivebudgetingalignedwithevolvingfinancialbehavior,while
introducing challenges related to data dependency and interpretability.
Overall,thereviewedliteratureindicatesatransitionfromstaticbudgetenforcementtoward
adaptive and predictive budgeting formulations, reflecting the increasing temporal complexity
of personal financial data.
Thefiguredepictsacomparisonbetweentheactualtime-seriesvaluesandthecorresponding
predicted values generated during the training phase. The observed series exhibits high short-
term volatility with frequent local fluctuations, reflecting the irregular nature of financial data.
In contrast, the predicted curve follows a smoother trajectory, capturing the underlying trend
while suppressing noise. This behavior indicates that the model emphasizes long-term temporal
patterns rather than reacting to transient variations. Such smoothing is desirable in personal
finance forecasting, where trend awareness is more critical than exact point-wise replication of
short-term fluctuations.
3.4.1 Internal Structure and Functional Mechanism of Long Short-Term Memory
(LSTM)
Long Short-Term Memory (LSTM) networks are described in the literature as advanced re-
current architectures developed to address the challenge of retaining information across long
temporal sequences. Conventional recurrent models often struggle to preserve contextual infor-
mation over extended intervals, particularly when modeling sequential data such as financial
transactions. LSTMovercomesthislimitationbyincorporatingadedicatedmemorycomponent
that enables selective storage and controlled modification of information over time.
The internal functioning of an LSTM unit is regulated by three interconnected gating mech-
anisms—namely the forget gate, input gate, and output gate—which interact with a shared
5

|     |     |     | Figure | 1: Actual | vs  | Predicted | Values | using | LSTM |     |
| --- | --- | --- | ------ | --------- | --- | --------- | ------ | ----- | ---- | --- |
internal memory cell. These gates collectively manage the flow of information through the
network and determine how historical and current data are represented.
The forget gate evaluates the relevance of previously stored information and determines
which portions of the historical context should be retained or discarded. In financial modeling
scenarios, this mechanism allows the network to remove outdated spending behaviors while
| maintaining | persistent |     | patterns | that | remain | significant |        | over time. |     |      |
| ----------- | ---------- | --- | -------- | ---- | ------ | ----------- | ------ | ---------- | --- | ---- |
|             |            |     |          | f    | = σ(W  | ·[h         | ,x ]+b | )          |     | (11) |
|             |            |     |          |      | t      | f t−1       | t      | f          |     |      |
The input gate governs the integration of new information into the internal memory. It
assesses the importance of recent financial activity and controls how much of this information is
added to the memory state. This selective updating process ensures that new spending trends
are incorporated without disrupting meaningful long-term financial representations.
|     |     |     |     | i   | = σ(W | ·[h   | ,x ]+b | )   |     | (12) |
| --- | --- | --- | --- | --- | ----- | ----- | ------ | --- | --- | ---- |
|     |     |     |     |     | t     | i t−1 | t      | i   |     |      |
The internal memory cell serves as a continuous state that accumulates and preserves rel-
evant information across time steps. By combining retained historical patterns with newly
admitted data, the memory cell enables the network to maintain temporal continuity in sequen-
tial representations.
|     |     |     | C = | f ·C | +i  | ·tanh(W | ·[h | ,x  | ]+b ) | (13) |
| --- | --- | --- | --- | ---- | --- | ------- | --- | --- | ----- | ---- |
|     |     |     | t   | t    | t−1 | t       | C   | t−1 | t C   |      |
The output gate regulates the extent to which the internal memory influences the current
output. It ensures that only contextually relevant information is propagated forward, thereby
| shaping subsequent |     | estimates |     | or analytical |     | outcomes. |     |     |     |     |
| ------------------ | --- | --------- | --- | ------------- | --- | --------- | --- | --- | --- | --- |
6

LSTM architecture is highlighted for its capacity to capture evolving spending behavior
while preserving long-term financial habits. At the same time, the literature acknowledges
challenges related to transparency, interpretability, and computational demands, underscoring
the importance of integrating LSTM-based approaches thoughtfully within broader Personal
Finance Management System frameworks.
Figure 2: LSTM architecture
Building on the system-level workflow, the discussion now focuses on the budgeting pipeline
within Personal Finance Management Systems. This pipeline is examined in terms of how
expenditure data is processed over time to support budget formulation and monitoring. The
subsequent sections review the techniques commonly employed at different stages of the bud-
geting process, highlighting their role in handling temporal spending behavior and uncertainty.
Figure 3: Conceptual Architecture of the Budgeting Pipeline
This Figure illustrates a generalized budgeting pipeline in Personal Finance Management
7

Systems. Financial transaction data first enters the input stage and undergoes preprocessing
operations, including cleaning, aggregation, and temporal ordering, to ensure data consistency.
The processed data is then transformed through feature engineering, where expenditure values,
categoricalinformation,andtimeindicesarerepresentedforanalysis. Atemporalmodelinglayer
applies statistical and learning-based techniques to capture expenditure dynamics and generate
predictedexpenditureestimates. Thesepredictionsareforwardedtothebudgetingstage, where
a safety margin is incorporated during budget formulation to account for uncertainty. The final
output is an adaptive budget representation that evolves with observed spending behavior. The
architecture represents a conceptual workflow synthesized from existing literature rather than
a specific system implementation.
Figure 4: Visualization of budgeting techniques in personal finance management
The diagram illustrates how multiple budgeting techniques analyze the same expenditure
data across time. Actual spending is represented using a histogram, highlighting natural vari-
ability in financial behavior. The EWMA curve demonstrates short-term smoothing by em-
phasizing recent expenditures, while the ARIMA trend reflects linear temporal dependencies
observed in historical data. The LSTM-based curve captures longer-term and non-linear spend-
ing patterns, representing behavioral dynamics that evolve over extended periods. The bud-
get threshold serves as a reference boundary for evaluating budget compliance. Overall, the
diagram conveys how different budgeting approaches provide complementary perspectives on
time-dependent financial behavior rather than competing solutions. Having examined budget-
ingtechniquesandtheirtemporalbehavior, thediscussionnowshiftstoforecastingmechanisms
employed in Personal Finance Management Systems.
4 Forecasting Techniques in Personal Finance
Forecasting represents a fundamental analytical function in Personal Finance Management Sys-
tems (PFMS), enabling a shift from retrospective financial reporting to proactive financial
8

decision support. By estimating future expenditure trajectories, forecasting mechanisms assist
usersinidentifyingpotentialbudgetaryconstraints, assessingsavingsprogression, andadapting
spending behavior before financial instability occurs. Beyond aggregate predictions, category-
level forecasting—covering domains such as food, transportation, utilities, and discretionary
expenses—supports structured resource allocation and informed long-term planning. Conse-
quently, forecasting plays a central role in enhancing the intelligence and practical utility of
modern PFMS.
4.1 Statistical Time-Series Models (ARIMA and SARIMA)
Statistical time-series models have traditionally served as the foundation of financial forecasting
due to their mathematical transparency and computational efficiency. Among these, the Au-
toRegressive Integrated Moving Average (ARIMA) model is widely employed to capture linear
temporal dependencies in expenditure data. ARIMA estimates future values as a function of
historical observations and past forecast errors by combining autoregressive, differencing, and
moving average components. The general formulation of an ARIMA model is expressed as
Y = ϕ Y +ϕ Y +···+ϕ Y +θ ϵ +θ ϵ +···+θ ϵ +ϵ (14)
t 1 t−1 2 t−2 p t−p 1 t−1 2 t−2 q t−q t
where Y denotes the stationary time-series value at time t, ϕ represents autoregressive coef-
t
ficients, and θ denotes moving average parameters. To account for periodic spending behavior
commonly observed in consumer finance, Seasonal ARIMA (SARIMA) extends this formula-
tion by incorporating seasonal components. These statistical models are typically applied in
short-term forecasting scenarios where expenditure trends are relatively stable and stationarity
assumptions are satisfied.
Figure 5: Comparison of ARMA, ARIMA, and SARIMA time-series models
9

4.2 Machine Learning Regression Approaches
Machine learning regression methods provide an alternative to classical statistical models by
enabling the capture of non-linear relationships within high-dimensional financial data. In
PFMS literature, ensemble-based regression techniques are frequently examined due to their
robustness and ability to model heterogeneous spending patterns. The effectiveness of these
approaches depends substantially on feature engineering processes that transform raw transac-
tion logs into structured inputs. Common representations include rolling expenditure averages
over fixed temporal windows, trend indicators that reflect spending increases or declines, and
category-specific frequency measures. Such features allow regression models to learn complex
financial interactions that are difficult to represent using linear time-series formulations.
4.3 Deep Learning Methods (LSTM and GRU)
Deep learning architectures are increasingly explored for forecasting tasks involving complex
and long-term temporal dependencies. Recurrent neural models, particularly Long Short-Term
Memory(LSTM)networks,aredesignedtopreserverelevanthistoricalinformationwhileadapt-
ing to recent expenditure variations through gated memory mechanisms. This architectural
design enables the modeling of recurring expenses, seasonal patterns, and evolving financial
behavior across extended time horizons.
Gated Recurrent Units (GRU) are also discussed as a computationally efficient alternative,
employing a simplified gating structure while retaining the capacity to model sequential depen-
dencies. Such architectures are often considered in scenarios where computational constraints
or real-time processing requirements limit the applicability of more complex recurrent models.
4.4 Hybrid and Ensemble Forecasting Approaches
To address the limitations associated with standalone forecasting models, recent research inves-
tigateshybridandensembleforecastingframeworksthatintegratemultiplemodelingparadigms.
A commonly reported approach combines ARIMA and LSTM outputs, leveraging the strength
of ARIMA in capturing linear temporal trends and the capability of LSTM to model non-linear
residual behavior. In these ensemble formulations, individual model predictions are aggregated
using weighted combinations:
Y = w ·Y +w ·h (15)
t,ensemble 1 t,ARIMA 2 t,LSTM
where w and w represent weighting coefficients optimized through validation procedures.
1 2
Such hybrid strategies aim to enhance forecast robustness across varying financial conditions
without relying exclusively on a single modeling assumption.
4.5 Cross-Cutting Discussion
Acrossforecastingmethodologies,severalcross-cuttingconsiderationsconsistentlyemergeinthe
literature. Forecasthorizonsignificantlyinfluencesmodelsuitability,withstatisticalapproaches
commonly applied to short-term prediction tasks, while deep learning models are examined for
longer-term forecasting where seasonal and behavioral patterns extend over months or years.
Data availability and quality also play a critical role, as deep learning techniques typically
require substantial historical data and are sensitive to noise, whereas statistical models are
more resilient in data-sparse settings but require stationarity through preprocessing techniques.
Interpretability remains a central concern in PFMS applications. Statistical models are
often regarded as transparent systems, while deep learning approaches introduce opacity that
motivates the integration of explainable artificial intelligence mechanisms to support user trust
andregulatorycompliance. Additionally,scalabilityanddeploymentconstraintsarehighlighted,
10

particularly for mobile and web-based PFMS, where computationally intensive models must
be managed through layered system architectures and API-driven services to ensure efficient
operation.
| 5 AI-Powered |     | Spending |     | Insights |     | and | Anomaly | Detection |     |
| ------------ | --- | -------- | --- | -------- | --- | --- | ------- | --------- | --- |
5.1 Distinction Between Anomaly Detection and Fraud Detection
In Personal Finance Management Systems (PFMS), anomaly detection and fraud detection
represent distinct analytical objectives, despite being frequently conflated in financial litera-
ture. Fraud detection is conventionally formulated as a supervised learning problem, relying
on historical datasets annotated with explicit fraud labels to train classification models. Such
formulations are well suited to institutional banking environments where large, labeled datasets
are available.
In contrast, spending anomaly detection within PFMS is inherently an unsupervised task.
Its primary objective is to identify atypical, inefficient, or irregular spending behavior relative
to an individual user’s historical patterns, without requiring predefined labels of undesirable
activity. This distinction arises from the highly personalized nature of spending behavior and
the practical difficulty of generating labeled datasets that define overspending or abnormal
consumption for individual users. As a result, anomaly detection in PFMS focuses on deviation
| analysis       | rather | than categorical | identification |           | of fraudulent |         | events. |     |     |
| -------------- | ------ | ---------------- | -------------- | --------- | ------------- | ------- | ------- | --- | --- |
| 5.2 Rule-Based |        | and              | Statistical    | Detection |               | Methods |         |     |     |
Early PFMS implementations employ rule-based logic and statistical thresholds as baseline
mechanisms for identifying anomalous spending behavior. These methods typically assume a
stable distribution of expenditure data and flag transactions that exceed expected variability
limits. A common statistical formulation defines an anomaly when current expenditure exceeds
| a rolling | historical | average | by a multiple | of      | the observed |        | dispersion: |     |      |
| --------- | ---------- | ------- | ------------- | ------- | ------------ | ------ | ----------- | --- | ---- |
|           |            | Anomaly | =             | True if | x            | > µ    | +k·σ        |     | (16) |
|           |            |         |               |         | current      | window | window      |     |      |
where µ and σ denote the mean and standard deviation computed over a recent
|     | window | window |     |     |     |     |     |     |     |
| --- | ------ | ------ | --- | --- | --- | --- | --- | --- | --- |
temporal window, and k is a predefined scaling factor. While such approaches are computation-
ally efficient and easily interpretable, their effectiveness is limited in PFMS contexts. They are
unable to account for multi-feature spending behavior or adapt to seasonal and lifestyle-driven
expenditure shifts, often resulting in elevated false-positive rates during events such as holidays
| or one-time      | purchases. |         |     |          |            |     |     |     |     |
| ---------------- | ---------- | ------- | --- | -------- | ---------- | --- | --- | --- | --- |
| 5.3 Unsupervised |            | Machine |     | Learning | Approaches |     |     |     |     |
Given the absence of labeled data and the inherently imbalanced nature of personal finan-
cial records, unsupervised learning techniques dominate anomaly detection research in PFMS.
Amongthese, IsolationForestisfrequentlydiscussedduetoitsdeviation-centricdesign. Rather
thanmodelingnormalbehavior,thisapproachisolatesanomalousobservationsthroughrecursive
partitioning, operating on the premise that anomalies are both rare and structurally distinct.
An anomaly score is computed based on the average path length required to isolate an
| observation | across | an ensemble | of  | isolation | trees, | expressed | as: |     |     |
| ----------- | ------ | ----------- | --- | --------- | ------ | --------- | --- | --- | --- |
−E(h(x))
|     |     |     |     | s(x,ψ) | = 2 |     |     |     | (17) |
| --- | --- | --- | --- | ------ | --- | --- | --- | --- | ---- |
c(ψ)
where E(h(x)) represents the expected path length and c(ψ) denotes the normalization fac-
tor derived from random binary tree properties. Higher scores indicate a greater likelihood
11

of anomalous behavior. Comparative studies reported in the literature consistently demon-
strate that Isolation Forest achieves superior detection capability relative to density-based and
boundary-based alternatives, which often suffer from scalability limitations or sensitivity to
parameter selection in PFMS environments.
5.4 Deep Learning-Based Anomaly Detection
Deep learning architectures are explored for anomaly detection in PFMS when spending behav-
ior exhibits complex, non-linear patterns across high-dimensional feature spaces. Autoencoder-
based models are commonly examined in this context, where the network learns a compressed
representation of typical spending behavior and identifies anomalies based on elevated recon-
struction error.
Despite their expressive power, deep learning approaches introduce practical challenges in
PFMS deployment. These models typically require large volumes of high-quality training data
and impose substantial computational overhead, which can limit real-time responsiveness in
mobile or resource-constrained environments. Consequently, their adoption in mid-scale PFMS
applications is often restricted to offline analysis or exploratory use rather than continuous
monitoring.
5.5 Explainable Artificial Intelligence (XAI) Considerations
As PFMS transition from rule-based detection to learning-driven anomaly identification, issues
of transparency and user trust become increasingly significant. Complex machine learning
models often function as opaque systems, generating alerts without clear justification, which
can reduce user confidence and adoption. In financial decision-support applications, the ability
to explain detected anomalies is as critical as the detection itself.
To address this challenge, explainable artificial intelligence techniques are increasingly in-
corporated into PFMS pipelines. Post-hoc interpretability methods are applied to attribute
anomaly decisions to specific spending features, enabling the generation of human-readable ex-
planations. Additionally, attention-based mechanisms integrated within learning models high-
light historical transactions that most strongly influenced anomaly detection outcomes.
The literature frequently advocates hybrid system designs in which unsupervised learning
models perform anomaly detection, while rule-based or statistical logic is employed to generate
interpretable explanations. Such hybrid implementations aim to balance analytical rigor with
usability, ensuring that PFMS remain both technically robust and user-centric.
6 Group Expense Management and Collaborative Finance
6.1 Traditional Bill-Splitting Systems
Group expense management has traditionally been handled through manual and semi-digital
methods, including spreadsheets, handwritten records, and basic ledger-based applications. In
social and domestic contexts—such as shared travel, dining, or household utilities—tracking
individual contributions accurately often becomes cumbersome. Early mobile applications for
group finance typically function as electronic ledgers, requiring users to manually record trans-
actions and assign participants for each expense. These systems commonly rely on static,
rule-based logic, such as equal splitting, which fails to capture real-world variations where par-
ticipants contribute unevenly. As a result, such approaches are prone to data entry errors,
inconsistencies, and limited transparency, frequently leading to confusion and interpersonal
friction within groups.
12

Figure 6: Anomaly detection using One-Class SVM
6.2 Graph-Based Settlement Optimization
Toaddressthecomplexityinherentinmulti-partydebtresolution, contemporarygroupexpense
management systems incorporate graph-based settlement optimization techniques. In this for-
mulation, group members are represented as nodes, while financial obligations are modeled as
directed edges within a graph structure. Individual expenses are aggregated to compute net
balances for each participant, and optimization algorithms are applied to minimize the total
number of transactions required to settle group debts. Rather than executing numerous pair-
wise payments, the system recommends a reduced set of settlement transactions that efficiently
balance obligations across the group. This approach improves clarity, reduces administrative
overhead, and ensures consistency in large or frequently interacting groups.
6.3 Behavioral Analysis in Group Finance
Recent developments in collaborative finance emphasize behavioral and event-centric perspec-
tives on shared expenses. Instead of treating expenses as isolated transactions, intelligent sys-
tems organize group spending around contextual events, such as trips, social gatherings, or
recurring activities. This event-based organization enhances transparency by associating ex-
penses, discussions, and settlements within a unified context. Dashboards summarizing group-
level spending trends over monthly or annual periods enable participants to assess collective
financial behavior and identify recurring patterns.
To further reduce manual effort, optical character recognition (OCR) technologies are in-
creasingly integrated into group finance workflows. By automatically extracting item descrip-
tions, prices, and totals from receipts, OCR-enabled systems streamline expense entry and
reduce errors associated with manual transcription. This automation supports real-time collab-
oration while lowering the cognitive burden on users managing shared financial records.
6.4 Machine Learning–Based Payer Prediction and Expense Allocation
Advances in predictive analytics have enabled group expense management systems to evolve
from passive tracking tools into proactive collaborative assistants. Machine learning techniques
are applied to identify recurring behavioral patterns within groups and estimate the most likely
payer for a newly recorded expense. In parallel, regression-based models are explored to recom-
13

mend expense allocation ratios that reflect historical contribution behavior rather than uniform
splits.
At a conceptual level, allocation logic can be expressed as a functional mapping between
| historical | behavior | and | contextual | attributes: |     |     |     |     |     |     |
| ---------- | -------- | --- | ---------- | ----------- | --- | --- | --- | --- | --- | --- |
Member Share = f(Historical Contribution,Group Persona,Event Type) (18)
By analyzing prior transactions and group dynamics, such systems can suggest personalized
allocation strategies and notify users when projected spending approaches predefined group
thresholds. The integration of classification for payer prediction and regression for allocation
enhances coordination, reduces disputes, and supports more equitable financial collaboration
within groups.
| 7 Comparative |     |     | Analysis |     | of Techniques |     |     |     |     |     |
| ------------- | --- | --- | -------- | --- | ------------- | --- | --- | --- | --- | --- |
This section provides a qualitative synthesis of the methodological characteristics, data de-
pendencies, and operational trade-offs associated with the techniques surveyed in this review.
Rather than establishing hierarchical rankings, the analysis focuses on how architectural as-
sumptions and modeling constraints align with distinct objectives in personal finance manage-
ment. Thediscussionhighlightsinterpretability, scalability, adaptability, anddatarequirements
| as central      | dimensions |     | influencing | methodological |           | suitability. |     |     |     |     |
| --------------- | ---------- | --- | ----------- | -------------- | --------- | ------------ | --- | --- | --- | --- |
| 7.1 Comparative |            |     | Analysis    | of             | Budgeting | Techniques   |     |     |     |     |
Budgeting mechanisms in Personal Finance Management Systems (PFMS) span a spectrum
ranging from lightweight statistical heuristics to memory-driven deep learning architectures.
The choice of budgeting technique is largely influenced by the balance between decision trans-
| parency and | the | capacity | to capture     |     | complex    | behavioral | patterns. |            |     |     |
| ----------- | --- | -------- | -------------- | --- | ---------- | ---------- | --------- | ---------- | --- | --- |
|             |     | Table    | 1: Qualitative |     | Comparison | of         | Budgeting | Techniques |     |     |
Technique Data Require- Interpretability Scalability Adaptability
ments
EWMA Low(minimalhis- High (transparent High (recur- Low (stable
|     |     | tory) |     |     | logic) |     | sive | updates) | habits | only) |
| --- | --- | ----- | --- | --- | ------ | --- | ---- | -------- | ------ | ----- |
Clustering Medium (feature Medium (cluster High (unla- Medium
| (K-Means |     | / vectors) |     |     | centroids) |     | beled | data) | (pattern- |     |
| -------- | --- | ---------- | --- | --- | ---------- | --- | ----- | ----- | --------- | --- |
| GMM)     |     |            |     |     |            |     |       |       | based)    |     |
ARIMA Medium (station- High (statistical Low(category- Medium
|     |     | ary | series) |     | formulation) |     | wise | modeling) | (trend | cap- |
| --- | --- | --- | ------- | --- | ------------ | --- | ---- | --------- | ------ | ---- |
ture)
| LSTM |     | High     | (long | se- | Low (opaque   |     | rep- Medium |     | Very          | High |
| ---- | --- | -------- | ----- | --- | ------------- | --- | ----------- | --- | ------------- | ---- |
|      |     | quences) |       |     | resentations) |     | (resource   |     | in- (temporal |      |
|      |     |          |       |     |               |     | tensive)    |     | shifts)       |      |
From a conceptual standpoint, budgeting approaches reflect a trade-off between temporal
awareness and behavioral expressiveness. Statistical methods such as EWMA and ARIMA
provide clear and interpretable mechanisms with low computational overhead, making them
suitable for users whose spending behavior remains relatively stable over time. However, these
approaches struggle to accommodate non-linear changes and seasonal variations. Clustering-
based methods introduce a behavioral abstraction by grouping users or transactions into spend-
ing profiles, though they disregard transaction order and temporal evolution. In contrast,
14

LSTM-based models excel at capturing long-range dependencies across multiple spending cat-
egories but require substantial historical data and computational resources, which may limit
| applicability   | for | users with | sparse   | financial | records.    |     |            |     |     |     |     |
| --------------- | --- | ---------- | -------- | --------- | ----------- | --- | ---------- | --- | --- | --- | --- |
| 7.2 Comparative |     |            | Analysis | of        | Forecasting |     | Techniques |     |     |     |     |
Expenditure forecasting in PFMS involves balancing the stability of linear trend modeling with
the flexibility required to represent non-linear and evolving financial dynamics.
|     |     | Table | 2: Qualitative |     | Comparison |     | of Forecasting |     | Techniques |     |     |
| --- | --- | ----- | -------------- | --- | ---------- | --- | -------------- | --- | ---------- | --- | --- |
Technique Data Require- Interpretability Scalability Adaptability
ments
ARIMA / Low to Medium High (linear for- Low (parame- Low (sta-
| SARIMA |     |     |     |     | mulation) |     |     | ter tuning) |     | tionarity |     |
| ------ | --- | --- | --- | --- | --------- | --- | --- | ----------- | --- | --------- | --- |
constraints)
| LSTM | / GRU | High      |     | (large | Low     | (hidden |     | Medium     | (com- | High   | (non-  |
| ---- | ----- | --------- | --- | ------ | ------- | ------- | --- | ---------- | ----- | ------ | ------ |
|      |       | datasets) |     |        | states) |         |     | putational |       | linear | dynam- |
|      |       |           |     |        |         |         |     | overhead)  |       | ics)   |        |
Hybrid High (dual-stage Medium (partial Medium (in- Very High
| (ARIMA– |     | modeling) |     |     | transparency) |     |     | tegration   |     | (linear | + non- |
| ------- | --- | --------- | --- | --- | ------------- | --- | --- | ----------- | --- | ------- | ------ |
| LSTM)   |     |           |     |     |               |     |     | complexity) |     | linear) |        |
The primary distinction among forecasting approaches lies in linear robustness versus non-
linear flexibility. ARIMA-based models effectively capture autocorrelations and linear temporal
| dependencies, | as  | expressed | by: |     |            |     |       |     |     |     |      |
| ------------- | --- | --------- | --- | --- | ---------- | --- | ----- | --- | --- | --- | ---- |
|               |     |           |     | Y = | ϕ Y +···+θ |     | ϵ     | +ϵ  |     |     | (19) |
|               |     |           |     | t   | 1 t−1      |     | 1 t−1 | t   |     |     |      |
This formulation supports reliable short-term forecasting under stationary conditions but
fails to represent complex behavioral shifts. Deep learning models, such as LSTM and GRU,
address this limitation by modeling non-linear temporal relationships through memory mecha-
nisms, albeit at the cost of increased computational demands and sensitivity to noise. Hybrid
ARIMA–LSTM frameworks aim to reconcile these paradigms by extracting linear trends via
| ARIMA and | modeling |     | residual   | non-linear | components |     | using | LSTM:  |     |     |      |
| --------- | -------- | --- | ---------- | ---------- | ---------- | --- | ----- | ------ | --- | --- | ---- |
|           |          |     | Y          |            | = w ·Y     |     | +w    | ·h     |     |     | (20) |
|           |          |     | t,ensemble |            | 1 t,ARIMA  |     | 2     | t,LSTM |     |     |      |
While such integration enhances forecasting robustness across heterogeneous financial con-
texts, it introduces additional architectural complexity and resource overhead.
| 7.3 Comparative |     |     | Analysis | of  | Anomaly | Detection |     | Techniques |     |     |     |
| --------------- | --- | --- | -------- | --- | ------- | --------- | --- | ---------- | --- | --- | --- |
Anomaly detection within PFMS is primarily formulated as an unsupervised learning problem,
given the absence of labeled data defining undesirable or inefficient spending behavior.
The selection of an anomaly detection strategy reflects a balance between simplicity and
expressive power. Rule-based systems provide transparent and verifiable baselines but lack the
capacitytomodelmulti-dimensionalspendingbehaviororadapttoseasonalvariation. Isolation
Forest represents a paradigm shift by isolating anomalies directly through random partitioning
rather than modeling normal behavior. Its anomaly scoring mechanism is defined as:
−E(h(x))
|     |     |     |     |     | s(x,ψ) = | 2   | c(ψ) |     |     |     | (21) |
| --- | --- | --- | --- | --- | -------- | --- | ---- | --- | --- | --- | ---- |
15

Table 3: Qualitative Comparison of Anomaly Detection Techniques
Technique Data Require- Interpretability Scalability Adaptability
ments
Rule-Based Low (manual Very High High (low Very Low
rules) cost) (rigid logic)
Isolation For- Low to Medium Medium (requires Very High High (feature-
est XAI) (O(nlogn)) agnostic)
One-Class Medium Low Low (memory Medium
SVM intensive)
Thisformulationenablesefficientandscalabledetectioninlarge, unlabeleddatasets, though
it does not inherently provide explanatory context. More complex methods, such as One-
Class SVM and Autoencoders, offer enhanced detection capabilities for intricate anomalies
but suffer from poor scalability and high computational cost, particularly in mobile or real-
time PFMS environments. As a result, contemporary systems often adopt hybrid designs,
combiningunsuperviseddetectionmechanismswithrule-basedorexplainableAIlayerstoensure
interpretability and user trust.
8 Conclusion
The evolution of Personal Finance Management Systems (PFMS) reflects a broader shift from
static, rule-based record-keeping tools toward intelligent, data-driven decision-support plat-
forms. This transition is characterized by the convergence of four core analytical dimensions:
adaptive budgeting, expenditure forecasting, anomaly detection, and collaborative group fi-
nance. Across the literature, budgeting mechanisms have progressed from fixed heuristics to
behavior-awareapproachesthatincorporatetemporalcontextandspendingpatternstosupport
personalized financial limits. Forecasting studies similarly demonstrate a movement toward hy-
bridmodelingstrategies,wherestatisticaltime-seriesmethodsarecombinedwithlearning-based
approaches to improve robustness across diverse financial conditions.
AnomalydetectionresearchwithinPFMShasincreasinglyfavoredunsupervisedmethodolo-
gies, motivated by the absence of labeled personal spending data and the highly individualized
nature of financial behavior. Techniques designed to isolate deviations rather than classify pre-
defined outcomes have enabled scalable identification of unusual spending patterns. In parallel,
group expense management systems have advanced beyond manual tracking by incorporating
automatedsettlementoptimization,event-centricorganization,andreceiptdigitization,thereby
reducing administrative overhead and improving transparency in shared financial contexts.
Machine learning functions as a central enabler across these developments, facilitating the
identificationofcomplexpatternsandlong-termdependenciesthataredifficulttocaptureusing
traditional analytical methods. However, the growing reliance on complex models has also
emphasized the importance of explainability, with explainable artificial intelligence emerging as
a critical requirement for user trust and accountability in financial decision-support systems.
Despite substantial progress at the component level, existing research remains fragmented,
with limited emphasis on unified system-level integration. The literature consistently indi-
cates the need for cohesive intelligent PFMS frameworks that integrate budgeting, forecasting,
anomaly detection, and collaborative finance within a single platform. Advancing toward such
unified ecosystems represents a key direction for future research, with the potential to provide
users with comprehensive financial insights, enhance financial literacy, and support long-term
financial stability in an increasingly dynamic digital economy.
16

Acknowledgments
This work was carried out under the supervision of Professor Rupali Panpaliya. The author(s)
gratefully acknowledge her guidance, academic oversight, and constructive feedback, which con-
tributed significantly to the development and completion of this study.
References
[1] S. Hochreiter and J. Schmidhuber, “Long Short-Term Memory,” Neural Computation, vol.
| 9, no. 8, | pp. 1735–1780, | 1997. |     |     |     |
| --------- | -------------- | ----- | --- | --- | --- |
[2] G. E. P. Box and G. M. Jenkins, Time Series Analysis: Forecasting and Control, Holden
Day, 1970.
[3] F. T. Liu, K. M. Ting, and Z. H. Zhou, “Isolation Forest,” Proceedings of the IEEE Inter-
| national | Conference | on Data | Mining | (ICDM), | pp. 413–422, 2008. |
| -------- | ---------- | ------- | ------ | ------- | ------------------ |
[4] G. P. Zhang, “Time Series Forecasting Using a Hybrid ARIMA and Neural Network
| Model,” | Neurocomputing, |     | vol. 50, | pp. 159–175, | 2003. |
| ------- | --------------- | --- | -------- | ------------ | ----- |
[5] M. Khashei and M. Bijari, “A Novel Hybridization of Artificial Neural Networks and
ARIMA Models for Time Series Forecasting,” Applied Soft Computing, vol. 11, no. 2,
| pp. 2664–2675, | 2011. |     |     |     |     |
| -------------- | ----- | --- | --- | --- | --- |
[6] O.B.Sezer,M.U.Gudelek, andA.M.Ozbayoglu, “FinancialTimeSeriesForecastingwith
Deep Learning: A Systematic Literature Review (2005–2019),” Applied Soft Computing,
vol. 90, 2020.
[7] S. Makridakis, E. Spiliotis, and V. Assimakopoulos, “The M4 Competition: Results, Find-
ings, Conclusion and Way Forward,” International Journal of Forecasting, vol. 36, no. 1,
| pp. 54–74, | 2020. |     |     |     |     |
| ---------- | ----- | --- | --- | --- | --- |
[8] Y. Qin, D. Song, H. Chen, W. Cheng, G. Jiang, and G. Cottrell, “A Dual-Stage Attention-
Based Recurrent Neural Network for Time Series Prediction,” Proceedings of IJCAI, 2017.
[9] B. Lim, S. O. Arik, N. Loeff, and T. Pfister, “Temporal Fusion Transformers for Inter-
pretableMulti-HorizonTimeSeriesForecasting,” International Journal of Forecasting, vol.
| 37, no. | 4, pp. 1748–1764, |     | 2021. |     |     |
| ------- | ----------------- | --- | ----- | --- | --- |
[10] V. Chandola, A. Banerjee, and V. Kumar, “Anomaly Detection: A Survey,” ACM Com-
| puting | Surveys, vol. | 41, no. | 3, 2009. |     |     |
| ------ | ------------- | ------- | -------- | --- | --- |
[11] L. Ruff et al., “Deep One-Class Classification,” Proceedings of the 35th International Con-
| ference | on Machine | Learning | (ICML), | 2018. |     |
| ------- | ---------- | -------- | ------- | ----- | --- |
[12] M.T.Ribeiro,S.Singh,andC.Guestrin,“WhyShouldITrustYou? ExplainingthePredic-
tions of Any Classifier,” Proceedings of the 22nd ACM SIGKDD Conference on Knowledge
| Discovery | and Data | Mining, | 2016. |     |     |
| --------- | -------- | ------- | ----- | --- | --- |
[13] S. M. Lundberg and S. I. Lee, “A Unified Approach to Interpreting Model Predictions,”
Advances in Neural Information Processing Systems (NeurIPS), 2017.
[14] M. E. Celebi, H. A. Kingravi, and P. A. Vela, “A Comparative Study of Efficient Initializa-
tion Methods for the K-Means Clustering Algorithm,” Expert Systems with Applications,
| vol. 40, | no. 1, pp. | 200–210, | 2013. |     |     |
| -------- | ---------- | -------- | ----- | --- | --- |
17

[15] Z. Chen, C. Li, and W. Sun, “Bitcoin Price Prediction using Machine Learning: An Ap-
proach to Sample Dimension Engineering,” Journal of Computational and Applied Mathe-
matics, vol. 365, 2020.
18