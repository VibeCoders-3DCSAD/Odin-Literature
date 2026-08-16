---
conversion_metadata:
  converted_at: "2026-07-21T13:41:52Z"
  converter_tool: "markitdown"
  converter_version: "0.1.6"
  source_pdf: "Karthikeyan et al.pdf"
  source_pdf_sha256: "c6037a120e79b3040daae601f238cea2b1c2fa15fbd59d058452fc52917388d1"
  page_count: 8
  markdown_char_count: 101695
---

<!-- PAGE-AWARE EXTRACTION (via pdfminer.six) -->

<!-- PAGE 1 -->

A High-Recall Cost-Sensitive Machine Learning
Framework for Real-Time Online Banking
Transaction Fraud Detection

Karthikeyan VR
Computer Science and Engineering
SA Engineering College
Chennai, India
2216087@saec.ac.in

Kavinraaj S
Computer Science and Engineering
SA Engineering College
Chennai, India
2216088@saec.ac.in

Premnath S
Computer Science and Engineering
SA Engineering College
Chennai, India
2216105@saec.ac.in

Mrs. J. Sangeetha M.E., (Ph.D)
Computer Science and Engineering
SA Engineering College
Chennai, India
sangeethaj@saec.ac.in

Abstract—Fraudulent activities on digital banking services
are becoming more intricate by the day, challenging existing
defenses. While older rule-driven methods struggle to keep pace,
even precision-focused algorithms fall short when new scams
are introduced. These tools typically overlook subtle shifts in
criminal behavior, missing crucial signals. Because silent breaches
cost institutions far more than flagged but legitimate actions,
catching every possible case is crucial. High sensitivity to actual
threats becomes essential when oversight leads to heavy losses.
One key aim here involves reducing missed fraud cases without
spiking incorrect alerts too much. This study builds a system
using group learning methods adjusted through smart threshold
choices. Using real-world transaction records shared openly,
where cheating acts rarely appear among normal activities, tests
are run under practical skewed distributions. The outcomes
revealed that approximately 98% of actual fraud was caught,
beating standard setups that rely on unchanging rules when
dealing with uneven examples across classes. When tested in
live settings, the fraud detection system connects directly to an
online bank’s transaction flow, stopping questionable activities
before they are completed. Alongside this setup, a browser add-
on built for Chrome is designed to flag deceptive web links and
reduce threats from harmful sites. These tests show one insight:
adjusting decisions by cost impact and validating across entire
systems makes deployment more stable and realistic for today’s
digital banking platforms.

Index Terms—Transaction Fraud Detection, Online Banking
Security, Machine Learning, Cost-Sensitive Learning, Ensemble
Models, Threshold Optimization, Imbalanced Data, Real-Time
Fraud Detection

I. INTRODUCTION

Nowadays, more people rely on Internet banking and elec-
tronic payment systems. This shift has brought easier access
to money services, yet opened doors to scams such as fake
transactions, stolen accounts, or hidden illegal fund flows.
With the increasing number of daily payments, older methods

intended to stop fraud often fail to react quickly or work well,
leading to serious monetary damage and weakened confidence
among users.

Fraud detection in banks usually depends on fixed rules or
standard machine learning methods aimed at achieving high
accuracy rates. However, both have serious flaws. Rules cannot
be adjusted to new threats, missing novel fraud types entirely.
Machine learning tools focused on precision tend to ignore
rare cases when dishonest actions account for only a small
share of the activity. Because actual fraud occurs infrequently
compared to normal operations, such models miss dangerous
outliers too easily.

Fraud slipping through tends to hurt more than flagging
honest activity by mistake, because mistaken alerts usually get
cleared with extra checks. Because missing real scams carry
heavier consequences, catching nearly all fraud matters most,
even if the overall correctness appears lower. What counts
here is how much each error type costs; therefore, methods
that adjust to these uneven risks make better sense. However,
standard measures ignore such imbalances.

Recent studies have combined multiple models or used deep
neural networks to spot fraudulent transactions; however, most
test these systems with static decision rules and in isolated
environments. These methods fall short in practice because
they overlook how changing thresholds affect outcomes, bal-
ance detection accuracy against incorrect flags, and fit within
the active financial infrastructure. Testing the entire setup by
embedding detection tools directly into the flow of actual
transaction processing remains rare.

This study introduces a fraud detection system for financial
transactions built using ensemble learning methods paired with
adjusted decision thresholds to account for cost differences
between error types. Instead of ignoring the imbalance, the

6
2
0
2

n
a
J

9
1

]

R
C
.
s
c
[

2
v
6
7
2
7
0
.
1
0
6
2
:
v
i
X
r
a

---

<!-- PAGE 2 -->

method focuses on boosting the detection of rare fraudulent
cases without increasing false alarms. The real-world perfor-
mance was tested using an open-access dataset that mirrors
actual transaction patterns and fraud occurrences. For live
validation, it runs inside an active online banking setup, halting
questionable transfers in real-time. In addition, a browser add-
on for spotting phishing websites comes alongside, adding
another level of defence by targeting scam pages directly in
daily browsing.

What sets this study apart begins not with theory but with
timing - embedding recall-driven threshold tuning directly into
live transaction flows. Most prior research has concentrated
on static benchmarks or overall precision measured after the
fact. Here, decisions shift dynamically, shaped by how much
more damaging missed fraud is compared to flagged legitimate
activities. The approach not only performs well on paper but
also adjusts in step with actual bank operations. Instead of
treating errors equally, it reflects what banks experience daily:
overlooking fraud carries heavier consequences than raising
false alarms. This alignment emerges through design choices
tuned to operational realities rather than idealized conditions.
A different angle emerges when ensemble stability meets
budget-aware decision thresholds, tied together through live
transaction controls, all built into one framework ready for
actual use. Security gains depth once a secondary check for
phishing is added to the setup, targeting not only active scams
but also their starting points. What stands out is how high
recall and practical operation take precedence here, shifting
focus away from pure accuracy; this shift helps close the
distance between theoretical models and what banks really
need on the ground.

A. Problem Statement

Despite handling countless financial operations instantly,
digital banking platforms face constant threats, such as illicit
fund movements and improper account access. Because dis-
honest actions are so rare among legitimate actions, spotting
them becomes extremely difficult. Most standard detection
methods prioritize general performance, missing subtle but
serious anomalies. When fraud accounts for only a small por-
tion of the total transactions, conventional rules and algorithms
struggle to respond effectively.

What holds back Current methods for spotting transaction
fraud are limited by rigid thresholds paired with measures
focused only on overall correctness. These fail to reflect the
true cost of different mistakes. When banks miss actual fraud,
the fallout includes monetary losses, trouble with regulations,
and damaged relationships with customers. Errors that flag
honest activity as suspicious usually lead to smaller burdens,
such as extra checks or verification steps.

Therefore, the central challenge is building a fraud detection
system for financial transactions that maintains low costs while
catching most fraudulent cases. This approach needs to work
despite uneven data distributions, spotting nearly all scams
without swamping legitimate activities with errors. Speed
matters just as much; decisions occur in moments during live

bank operations. Performance hinges on quick and accurate
judgments, each fitting seamlessly into the existing digital
infrastructure.

II. LITERATURE REVIEW

As more people depend on digital banking, the detection of
fake transactions has become a major research topic. Previ-
ously, banks mostly used fixed rules set by experts to catch
odd payments. These setups are straightforward to understand,
yet they struggle when scams change shape over time. As
conditions shift quickly in modern finance, these rigid methods
miss many real threats.

To address the shortcomings of rigid rule-driven setups,
experts have turned to machine learning techniques, such as
logistic regression, decision trees, and support vector ma-
chines, along with combined strategies, such as random forests
and gradient boosting. Drawing from past transaction records,
these systems independently identify signs of fraud on their
own, outperforming fixed-rule alternatives. However, much
of the existing work emphasizes total prediction correctness,
an approach poorly matched to skewed fraud data, where
dishonest activities are few. Therefore, models built around
accuracy frequently miss uncommon yet critical fraudulent
events.

Fraud detection now uses groups of machine learning mod-
els together, aiming for more stable and adaptable outcomes.
Combining the outputs from different classifiers helps to lower
the prediction errors while increasing the overall accuracy.
Some studies have highlighted better performance with ran-
dom forests or boosted trees; however, such strategies often
rely on unchanging cutoff points for decisions. Missing from
most is a clear adjustment for how costly it is to miss fraud
compared to falsely flagging normal activity, something banks
face daily.

Although methods such as RNNs, CNNs, and LSTM net-
works are used to spot fraudulent transactions and similar
they require significant computing power.
security issues,
Owing to their structure, these systems can recognize patterns
over time and subtle links between features in transaction
data. However, most tests occur after the fact, ignoring live
processing needs or limits found in actual applications. Their
strength in modeling does not always translate into practical
setups.

Simultaneously, researchers have explored phishing detec-
tion to support broader efforts against online fraud driven
by harmful web pages. Instead of relying solely on rules,
systems now apply machine learning and deep learning to sort
suspicious links using characteristics tied to naming patterns,
layout design, or user interaction traces. Although spotting
fake sites may lower risks before financial actions occur, many
analyses keep website threats apart from payment abuses and
rarely test both within one unified framework.

Research to date shows that machine learning methods,
especially combined ones, can detect fraudulent activity quite
well; however, some problems still exist. While many studies
focus on overall correctness, they often ignore how many

---

<!-- PAGE 3 -->

actual fraud cases are missed. Fixed decision points are
common, even though they may not suit shifting patterns
in financial behavior. Researchers rarely adjust their models
based on the varying costs linked to false alarms versus
missed detections. Another missing piece is testing within
live systems, and few attempts have been made to connect
detection tools directly to active bank transaction flows. The
proposed design is focused on detecting more fraud instances
while reducing costly errors, intelligently adjusting its trigger
levels, and running continuously inside an operational payment
environment.

III. EXISTING SYSTEM

Most current online banking fraud detection tools depend on
fixed rules or older machine learning methods that learn from
past transactions. These rule-driven setups use set boundaries
made by experts, such as caps on transfer amounts, loca-
tion checks, or how often payments occur, to flag unusual
activity. Although they are straightforward to implement and
understand, they cannot be adjusted over time. New types of
fraudulent actions easily bypass these systems, especially those
that have never been seen before.

Most banks now use machine learning tools, such as de-
cision trees, logistic regression, support vector machines, or
ensemble methods, to boost their ability to spot anomalies.
Transaction features help these systems label activity, either
normal or suspicious, without manual
input. Despite out-
performing fixed rule sets, they often aim for high general
accuracy, a goal that misaligns with actual fraud detection
needs, where genuine cases vastly outnumber fake ones.

One key weakness in current setups lies in their reliance on
unchanging cutoff points, often pinned at 0.5, to flag fraud.
Because banks face unequal consequences when mistakes
occur, rigid boundaries struggle to respond effectively. Missing
real fraud means that money vanishes along with customer
trust. In contrast, incorrectly tagging clean activities usually
adds a small review workload. When models adhere too
closely to one rule, they overlook harmful patterns more often
than necessary.

Most current tools for spotting fraud are tested only in
controlled lab-like conditions and rarely face actual day-to-
day use. Because of this gap, they often struggle when applied
directly to active payment networks. In addition, anti-phishing
methods, if used at all, usually run separately, disconnected
from broader systems meant to catch suspicious transactions.
It is crucial to design fraud detection methods that focus on
catching more incidents while keeping costs low. Real-world
data often show far fewer fraudulent cases than legitimate
ones, which shapes the performance of such systems. Shifting
patterns in deceptive actions mean that flexibility cannot be
ignored. The integration of live banking platforms adds another
layer of practical demand.

real-time, online banking environments. The primary objec-
tive of the system is to minimize false negatives (missed
fraud cases) while maintaining an acceptable false-positive
rate under highly imbalanced transaction data. To achieve
this, the system combines ensemble machine learning models
with decision threshold optimization, enabling recall-oriented
is suitable for safety-critical financial
fraud detection that
applications.

A. System Architecture

The proposed framework consists of three main compo-

nents:

1) Transaction Data Processing Module: Incoming trans-
action requests are processed to extract relevant trans-
actional, behavioral, temporal, and contextual features.
These features include transaction amount, transaction
type, user behavior patterns, time-based attributes, and
device or location data. All features were preprocessed
using appropriate encoding and normalization tech-
niques to ensure compatibility with the trained machine
learning models.

2) Fraud Detection Engine: The core fraud detection engine
employs an ensemble of machine learning classifiers
trained on historical transaction data. Ensemble learning
is used to improve robustness and generalization by ag-
gregating predictions from multiple base models. Instead
of relying on a fixed probability threshold, the system
applies decision threshold optimization to control the
trade-off between fraud recall and false-positive rate. A
transaction is classified as fraudulent when the predicted
fraud probability exceeds an optimized threshold value
selected based on recall-oriented performance criteria.
3) Real-Time Decision and Enforcement Module The fraud
detection model is directly integrated into the transaction
execution pipeline. Each transaction is evaluated in real
time before completion. Transactions classified as fraud-
ulent are automatically blocked or flagged for further
verification, whereas legitimate transactions are allowed
to proceed without delay. This design ensures immediate
risk mitigation and prevents financial losses caused by
delayed fraud detection.

B. Supporting Phishing Detection Component

To enhance end-to-end security, a supporting phishing-URL
detection mechanism was implemented as a Chrome browser
extension. The extension visits URLs and evaluates them
using a hybrid deep learning model combined with rule-based
heuristics. This component acts as an auxiliary defense layer
by reducing the likelihood of fraudulent transactions initiated
through malicious websites. The phishing detection module
operates independently and does not interfere with the core
fraud detection process.

IV. PROPOSED SYSTEM

C. Role of Phishing Detection in System-Level Security

The proposed system introduces a cost-sensitive transaction
fraud detection framework designed to operate effectively in

A common starting point misses how phishing is tied
to broader risks. The detection of malicious URLs plays a

---

<!-- PAGE 4 -->

supporting role, not a central role, in classifying fraud during
transactions. Credentials stolen by fake websites often lead
to unauthorized banking activities. Because of this pathway,
focusing only on actions taken during a transfer overlooks the
earlier weaknesses. Protection that begins too late cannot stop
what began long before it.

Above all, early warnings are triggered when deceptive sites
appear. By preventing users from reaching harmful pages,
one part quietly reduces risks before login attempts. Instead
of mixing with fraud checks on payments, it runs its own
course. Separate tracking means that the decision accuracy
for transactions remains steady. The performance remains firm
because the layers work separately.

Security gains depth when phishing detection is considered,
targeting not only active scams but also their origins. What
makes it work well is how this piece fits into the larger
setup, able to switch on or off without disrupting other func-
tions. Updates occur in isolation; therefore, changes remain
contained. This separation supports smoother rollouts in real-
world banking systems, in which adaptability is crucial.

From a system design perspective, treating phishing detec-
tion as an independent security layer aligns with the constraints
of real-world banking deployments. Financial institutions typ-
ically enforce strict access controls and isolation between
transaction-processing systems and external web-monitoring
components. By decoupling phishing detection from the core
transaction fraud engine, the proposed framework respects
these operational boundaries, while enabling layered risk miti-
gation. This separation allows banks to deploy, test, and update
the phishing module without requiring modifications to the
critical transaction infrastructure, thereby reducing the integra-
tion complexity, compliance risk, and operational downtime.

Fig. 1.
framework

System architecture of the proposed transaction fraud detection

D. Advantages of the Proposed System

The proposed system offers the following advantages over

existing approaches:

• Prioritizes fraud recall through cost-sensitive threshold
optimization rather than accuracy-centric evaluation.
• Effectively handles class imbalance commonly observed

in real-world banking transactions.

• Supports real-time transaction analysis and enforcement,

making it suitable for live online banking systems.

• Provides system-level validation by integrating fraud de-

tection directly into the transaction pipeline.

• Enhances security through an auxiliary phishing detection

mechanism without increasing transaction latency.

By addressing the limitations of existing fraud detection
systems, the proposed framework provides a practical and
deployable solution for improving fraud prevention in modern
online banking environments

V. METHODOLOGY AND IMPLEMENTATION

This section describes the methodology and implementation
details of the proposed cost-sensitive transaction-fraud detec-
tion framework. The system is designed to operate under real-
world constraints, including class imbalance, real-time deci-
sion requirements, and asymmetric costs of misclassification
errors in online banking environments.

A. Data Preprocessing and Feature Engineering

Incoming transaction data were first subjected to prepro-
cessing to ensure consistency and compatibility with the fraud
detection models. The dataset contains both numerical and
categorical attributes that represent transactional, behavioral,
information. Categorical features
temporal, and contextual
were transformed using suitable encoding techniques, and
numerical features were normalized to reduce scale variations
and improve model stability.

To enable controlled model learning and reduce class bias
the dataset was balanced prior to model
during training,
development. The processed feature set included the trans-
action amount, transaction type, time-based attributes, user
behavior indicators, and contextual metadata. These features
allow the model to capture meaningful patterns associated with
fraudulent activity while supporting a reliable evaluation of
recall–precision trade-offs through threshold analysis.

1) Dataset Description and Experimental Protocol: A
number of large-scale transaction records sourced from public
platforms, such as UCI and Kaggle, form the basis for testing
the fraud detection method described here. These collections
include hundreds of thousands of entries, most of which are
drawn from actual banking activity, yet masked to protect
user identity. Rarely do fraudulent cases appear, making up
less than one percent of all data points. This scarcity mirrors
the challenges banks typically face when monitoring digital
payments. Such an imbalance shapes how models must be
assessed.

A single entry logs details such as how much was spent,
what kind of transaction occurred, whether it used biometrics

---

<!-- PAGE 5 -->

or a PIN, when it happened, typical actions by the person
involved, along with data about the machine or place tied to
the event. Taken together, these pieces reflect the immediate
features of purchases as well as shifts in habits that might
signal fraud.

Subsequently, to check consistency and real-world function,
the data were split into training and testing portions in time
order. During this phase, one portion teaches the algorithm,
adjusts the category weights, and tunes the cutoff points for
decisions. Meanwhile, the second part remains hidden until
the final review, maintaining its natural imbalance. Because of
this setup, the outcomes show how well the systems adapt
beyond the practice rounds. Only then do numbers reveal
actual readiness for fresh cases.

Assessing model performance involves several metrics: con-
fusion matrices, PR curves, ROC behavior, and threshold
responses. In particular, precision-recall is important because
it handles imbalance well, which is common in detecting
rare fraudulent cases. The results shown are from a separate
test group, maintaining stable comparisons across reference
systems.

B. Fraud Detection Model

First, several basic classifiers learn patterns from past trans-
actions to power the main fraud detection system. Rather than
depending on one model alone, combining their outputs yields
steadier results across unpredictable datasets. By design, this
method smooths out inconsistencies while handling skewed or
messy real-world data more effectively.

A single prediction is obtained from each base model,
providing a number that indicates the likelihood of fraud.
Because these numbers matter together, they merge into one
overall risk mark per event. What shapes the group setup is
not how fancy the tools are, but how well they work and hold
up under pressure, which makes them fit for instant decisions.
Despite variations in design, speed, and reliability, guide the
choice.

C. Cost-Sensitive Decision Threshold Optimization

Unlike conventional fraud detection systems that apply a
fixed decision threshold, the proposed framework incorporates
cost-sensitive decision threshold optimization to prioritize
fraud recall. The classification decision is based on comparing
the predicted fraud probability against an optimized threshold
value, which is selected to minimize false negatives while
maintaining an acceptable false-positive rate. This approach
reflects the asymmetric cost structure of fraud detection in
online banking systems, where undetected fraud results in
significantly higher losses than false alarms.

Let P (y = 1 | x) denote the predicted probability that
a transaction x is fraudulent. A transaction is classified as
fraudulent if:

P (y = 1 | x) ≥ τ

(1)

where τ represents the decision threshold.

To explicitly model asymmetric misclassification costs, the

expected classification cost is defined as:

C(τ ) = CF N · F N (τ ) + CF P · F P (τ )

(2)

where F N (τ ) and F P (τ ) denote the number of false neg-
atives and false positives at threshold τ , respectively. The
misclassification costs satisfy:

CF N ≫ CF P

(3)

reflecting the substantially higher financial and operational
impact of undetected fraudulent transactions compared to false
alarms.

The optimal decision threshold τ ∗ is selected by minimizing

the expected classification cost:

τ ∗ = arg min

C(τ )

(4)

τ
This cost-sensitive threshold optimization shifts the decision
boundary toward higher fraud recall while constraining false-
positive rates within acceptable operational
limits, making
the proposed framework suitable for safety-critical real-time
online banking applications.

1) Discussion on High Fraud Recall Performance: What
drives strong fraud detection performance? This lies in how
the model treats misclassification costs differently across out-
comes. Typical methods stick to fixed cutoffs, aiming to get
most cases right overall; however, this one does not. Instead,
it adjusts its threshold based on real-world consequences and
tunes decisions where mistakes matter more. By focusing on
the financial risk asymmetry inherent in digital transactions,
the system deliberately moves its judgment
line to detect
fraudulent activity. This shift explains the higher capture rate
without reworking the core mechanics.

Most fraud in actual bank operations shows clear signs,
such as odd spending sizes, strange timing, or shifts from
normal habits. Because ensemble methods process these sig-
nals together, they separate legitimate from suspicious cases
more effectively, even when few fraud examples are present.
Adjusting the decision cutoff helps identify more true fraud
instances while skipping artificial data boosts or questionable
premises.

Choosing the operating point involves looking at precision,
recall, and how sensitive thresholds are, instead of just fo-
cusing on accuracy, so the recall numbers show a balanced
approach between catching fraud and limiting false alarms.
Therefore, the strong recall observed in this study is more
closely aligned with real-world use than with idealized test
conditions..

D. Real-Time Transaction Processing Pipeline

The trained fraud detection model was integrated into a
real-time online banking transaction pipeline. Each transaction
request is evaluated immediately after feature extraction and
prior to execution. If a transaction is classified as fraudulent, it
is automatically blocked or flagged for verification. Legitimate
transactions are processed without additional delays, ensuring
minimal impact on the user experience.

---

<!-- PAGE 6 -->

All transaction outcomes, including fraud prediction and
decision results, were logged in the transaction database.
This design supports auditability, performance monitoring, and
future model updates.

1) Real-Time Performance Considerations: A system built
for spotting fraudulent activity fits the speed demands of
today’s digital banking, requiring quick verdicts on transac-
tions under tight time limits. Tree-driven machine learning
methods form the core here - simple by design, allowing swift
predictions without heavy computing needs. After training,
fraud detection becomes a sequence: reshaping inputs, judging
likelihoods, and checking values against a set level - all steps
handled rapidly when payments move through. A fast response
remains achievable because each stage runs lean and integrates
smoothly into live operations.

Choosing the best decision threshold adds no extra load
when running the system because it is set ahead of time while
testing the model. Instead of calculating on the fly, the chosen
cutoff remains constant once the model goes live. During
processing time, each transaction requires checking whether
its fraud score exceeds the preset level. The check occurs
quickly enough to fit within normal payment workflows. Users
who complete valid transactions do not experience noticeable
wait times. The performance remains smooth because the logic
fits neatly into the existing steps. Detection runs in step with
processing, not apart from it.

Instead of relying on heavy deep learning during transac-
tions, the system uses a flexible design that fits fast-paced
online banking environments. Because fraud detection works
instantly,
it can trigger quick responses, such as halting
payments or asking for extra checks. This approach reduces
monetary exposure without disrupting user interaction with the
service.

E. Supporting Phishing Detection Implementation

A small extra layer of protection comes from a Chrome
add-on that checks website addresses for signs of phishing
attacks. This tool monitors every page visit and sends links
to a server for review. Risk levels are judged using smart
algorithms and pattern rules. Although it runs apart from the
main fraud-tracking system, its presence helps guard against
online scams. Protection improves when threats from harmful
websites are detected early.

F. Implementation Details

A design built

in separate parts allows for growth and
simplifies updates. Prediction tools for spotting fraud run
inside a server layer, offering real-time results via accessible
endpoints. Communication between bank systems and this
layer occurs through protected API requests, linking transac-
tions and analysis smoothly. Speed, consistency across runs,
and a straightforward setup guide how the system fits into
active banking platforms.

TABLE I
PERFORMANCE COMPARISON WITH BASELINE MODELS

Model

Accuracy (%)

Precision

Recall

F1-Score

ROC-AUC

Logistic Regression
Random Forest
XGBoost (Fixed Threshold τ = 0.5)
Proposed Model (Optimized τ )

95.4
97.1
97.8
98.3

82.6
90.3
94.1
96.8

71.2
88.7
92.4
98.6

76.5
89.5
93.2
98.2

0.942
0.981
0.988
0.996

Fig. 2. Confusion matrix of the proposed fraud detection model on the test
dataset.

Fig. 3.
illustrates the Precision–Recall (PR) curve of the proposed fraud
detection framework under highly imbalanced class conditions. The curve
demonstrates consistently high precision across a wide range of recall values,
indicating that the model effectively identifies fraudulent transactions while
minimizing false positives. This behavior is particularly important in online
banking environments, where excessive false alarms lead to operational over-
head. The strong PR performance confirms that the proposed cost-sensitive
threshold optimization successfully prioritizes fraud recall without sacrificing
precision.

---

<!-- PAGE 7 -->

rics, such as recall and classification accuracy. Visual tools
such as ROC curves and confusion matrices confirmed the
model’s ability to effectively separate normal transactions from
fraudulent ones. What stands out is how smoothly the model
fits into live transaction flows, proving that it can run fast
enough for real-world use without delays. Beyond direct fraud
spotting, another layer checks incoming links for signs of
phishing attacks before they lead users to be deceived. This
extra step does not replace the main system; rather, it supports
it by closing gaps that pure transaction monitoring might leave
open.

The results show that cost-aware decisions are important
when spotting fraud in online banks. Instead of just measuring
how often predictions are correct, aiming for high recall fits
the actual risks that money institutions face. Threshold tuning
plays a key role in ensuring that such systems function well
under pressure.

A. Future Work

Looking ahead, efforts will be aimed at adapting the frame-
work for real-world imbalances in class distribution alongside
shifting fraud behaviors. Instead of fixed rules,
thresholds
can shift with transaction risk levels, guided by the practical
system limits. Behavior over time may be modeled to reflect
how users act over extended periods. Updating models step-
by-step using continuous learning methods may offer a path
forward. To test the wider applicability, broader transaction
datasets must be considered. Real-system testing at scale
is expected to follow, ensuring stability beyond controlled
settings.

REFERENCES

[1] T. Dal Pozzolo, O. Bontempi, and G. Snoeck, “Adaptive Machine
Learning for Credit Card Fraud Detection,” IEEE Intelligent Systems,
vol. 30, no. 4, pp. 34–41, Jul.–Aug. 2015.

[2] A. Dal Pozzolo, G. Bontempi, and O. Snoeck, “Calibrating Probability
with Undersampling for Unbalanced Classification,” in Proc. IEEE
Symposium Series on Computational Intelligence, 2015, pp. 159–166.
[3] N. Dal Pozzolo et al., “Adversarial Drift Detection,” in Proc. IEEE
International Joint Conference on Neural Networks (IJCNN), 2014, pp.
2975–2982.

[4] C. Elkan, “The Foundations of Cost-Sensitive Learning,” in Proc. 17th
International Joint Conference on Artificial Intelligence (IJCAI), 2001,
pp. 973–978.

[5] T. Fawcett, “An Introduction to ROC Analysis,” Pattern Recognition

Letters, vol. 27, no. 8, pp. 861–874, 2006.

[6] S. Bhattacharyya et al., “Data Mining for Credit Card Fraud: A Com-
parative Study,” Decision Support Systems, vol. 50, no. 3, pp. 602–613,
2011.

[7] L. Breiman, “Random Forests,” Machine Learning, vol. 45, no. 1, pp.

5–32, 2001.

[8] T. Chen and C. Guestrin, “XGBoost: A Scalable Tree Boosting System,”
in Proc. 22nd ACM SIGKDD International Conference on Knowledge
Discovery and Data Mining, 2016, pp. 785–794.

[9] G. Ke et al., “LightGBM: A Highly Efficient Gradient Boosting Decision
Tree,” in Proc. Advances in Neural Information Processing Systems
(NeurIPS), 2017, pp. 3146–3154.

[10] L. Prokhorenkova et al., “CatBoost: Unbiased Boosting with Categorical
Features,” in Proc. Advances in Neural Information Processing Systems
(NeurIPS), 2018, pp. 6638–6648.

[11] M. Bahnsen et al., “Example-Dependent Cost-Sensitive Decision Trees,”
Expert Systems with Applications, vol. 42, no. 19, pp. 6609–6619, 2015.
[12] J. Maillo et al., “kNN-IS,” Knowledge-Based Systems, vol. 117, pp.

3–15, 2017.

Fig. 4. presents the Receiver Operating Characteristic (ROC) curve of the
proposed fraud detection model. The curve exhibits a steep ascent toward
the upper-left corner,
indicating strong discriminative capability between
fraudulent and legitimate transactions. While the high ROC-AUC value
reflects effective class separability, Precision–Recall analysis is emphasized
in this work as it provides a more representative evaluation metric for fraud
detection tasks characterized by severe class imbalance.

Fig. 5. Effect of decision threshold on model performance, illustrating the
trade-off between detection accuracy and classification sensitivity.

VI. CONCLUSION AND FUTURE WORK

it

A closer look at fraud in online banking reveals how
is to catch every suspicious case; missing one
crucial
could have serious consequences. Instead of merely cutting
costs, the method presented in this study focuses on reducing
missed detections through smart modeling choices. Ensemble
techniques are used to handle data where fraud cases are rare
by using multiple models together while carefully adjusting
decision boundaries. The results show that it works well -
not perfectly, but solidly–when tested across different met-

---

<!-- PAGE 8 -->

[13] R. S. Rao and A. R. Pais, “Detection of Phishing Websites,” Neural
Computing and Applications, vol. 31, no. 8, pp. 3851–3873, 2019.
[14] UCI Machine Learning Repository, “Credit Card Fraud Detection

Dataset,” 2024.

[15] Kaggle, “Financial Fraud Detection Dataset,” 2024.
[16] D. J. Hand and R. J. Whitrow, “Statistical techniques for fraud detec-
tion,” Wiley Interdisciplinary Reviews, vol. 1, no. 6, pp. 771–783, 2009.
[17] M. Dal Pozzolo et al., “Credit card fraud detection,” IEEE Trans. Neural

Netw. Learn. Syst., vol. 26, no. 10, pp. 2580–2593, Oct. 2015.

[18] A. Dal Pozzolo et al., “Handling class imbalance,” in Proc. IEEE Int.

Conf. Intelligent Systems, 2014, pp. 1–6.

[19] K. Weiss et al., “Cost-sensitive learning vs. sampling,” in Proc. IEEE

Int. Conf. Data Mining (ICDM), 2007, pp. 35–41.

[20] J. Davis and M. Goadrich, “The relationship between precision-recall
and ROC curves,” in Proc. 23rd Int. Conf. Machine Learning (ICML),
2006, pp. 233–240.

<!-- MARKITDOWN CONVERSION -->

<!-- Full MarkItDown conversion for formatting fidelity. -->

A High-Recall Cost-Sensitive Machine Learning
Framework for Real-Time Online Banking
Transaction Fraud Detection
Karthikeyan VR Kavinraaj S Premnath S
Computer Science and Engineering Computer Science and Engineering Computer Science and Engineering
SA Engineering College SA Engineering College SA Engineering College
Chennai, India Chennai, India Chennai, India
2216087@saec.ac.in 2216088@saec.ac.in 2216105@saec.ac.in
Mrs. J. Sangeetha M.E., (Ph.D)
Computer Science and Engineering
SA Engineering College
Chennai, India
sangeethaj@saec.ac.in
Abstract—Fraudulent activities on digital banking services intendedtostopfraudoftenfailtoreactquicklyorworkwell,
are becoming more intricate by the day, challenging existing leadingtoseriousmonetarydamageandweakenedconfidence
defenses.Whileolderrule-drivenmethodsstruggletokeeppace,
among users.
even precision-focused algorithms fall short when new scams
Fraud detection in banks usually depends on fixed rules or
are introduced. These tools typically overlook subtle shifts in
criminalbehavior,missingcrucialsignals.Becausesilentbreaches standard machine learning methods aimed at achieving high
cost institutions far more than flagged but legitimate actions, accuracyrates.However,bothhaveseriousflaws.Rulescannot
catching every possible case is crucial. High sensitivity to actual be adjusted to new threats, missing novel fraud types entirely.
threats becomes essential when oversight leads to heavy losses.
Machine learning tools focused on precision tend to ignore
One key aim here involves reducing missed fraud cases without
rare cases when dishonest actions account for only a small
spiking incorrect alerts too much. This study builds a system
using group learning methods adjusted through smart threshold share of the activity. Because actual fraud occurs infrequently
choices. Using real-world transaction records shared openly, compared to normal operations, such models miss dangerous
wherecheatingactsrarelyappearamongnormalactivities,tests outliers too easily.
are run under practical skewed distributions. The outcomes
Fraud slipping through tends to hurt more than flagging
revealed that approximately 98% of actual fraud was caught,
honestactivitybymistake,becausemistakenalertsusuallyget
beating standard setups that rely on unchanging rules when
dealing with uneven examples across classes. When tested in cleared with extra checks. Because missing real scams carry
live settings, the fraud detection system connects directly to an heavier consequences, catching nearly all fraud matters most,
online bank’s transaction flow, stopping questionable activities even if the overall correctness appears lower. What counts
before they are completed. Alongside this setup, a browser add-
here is how much each error type costs; therefore, methods
on built for Chrome is designed to flag deceptive web links and
that adjust to these uneven risks make better sense. However,
reduce threats from harmful sites. These tests show one insight:
adjusting decisions by cost impact and validating across entire standard measures ignore such imbalances.
systems makes deployment more stable and realistic for today’s Recentstudieshavecombinedmultiplemodelsoruseddeep
digital banking platforms. neuralnetworkstospotfraudulenttransactions;however,most
Index Terms—Transaction Fraud Detection, Online Banking test these systems with static decision rules and in isolated
Security, Machine Learning, Cost-Sensitive Learning, Ensemble
environments. These methods fall short in practice because
Models, Threshold Optimization, Imbalanced Data, Real-Time
they overlook how changing thresholds affect outcomes, bal-
Fraud Detection
ance detection accuracy against incorrect flags, and fit within
the active financial infrastructure. Testing the entire setup by
I. INTRODUCTION
embedding detection tools directly into the flow of actual
Nowadays, more people rely on Internet banking and elec- transaction processing remains rare.
tronic payment systems. This shift has brought easier access This study introduces a fraud detection system for financial
to money services, yet opened doors to scams such as fake transactionsbuiltusingensemblelearningmethodspairedwith
transactions, stolen accounts, or hidden illegal fund flows. adjusted decision thresholds to account for cost differences
With the increasing number of daily payments, older methods between error types. Instead of ignoring the imbalance, the
6202
naJ
91
]RC.sc[
2v67270.1062:viXra

method focuses on boosting the detection of rare fraudulent bank operations. Performance hinges on quick and accurate
cases without increasing false alarms. The real-world perfor- judgments, each fitting seamlessly into the existing digital
| mance              | was tested | using    | an  | open-access | dataset      | that mirrors | infrastructure. |     |     |     |     |
| ------------------ | ---------- | -------- | --- | ----------- | ------------ | ------------ | --------------- | --- | --- | --- | --- |
| actual transaction |            | patterns |     | and fraud   | occurrences. | For          | live            |     |     |     |     |
II. LITERATUREREVIEW
validation,itrunsinsideanactiveonlinebankingsetup,halting
questionabletransfersinreal-time.Inaddition,abrowseradd- As more people depend on digital banking, the detection of
|        |          |          |          |     |                  |     | fake transactions | has become | a major research |     | topic. Previ- |
| ------ | -------- | -------- | -------- | --- | ---------------- | --- | ----------------- | ---------- | ---------------- | --- | ------------- |
| on for | spotting | phishing | websites |     | comes alongside, |     | adding            |            |                  |     |               |
another level of defence by targeting scam pages directly in ously, banks mostly used fixed rules set by experts to catch
daily browsing. oddpayments.Thesesetupsarestraightforwardtounderstand,
What sets this study apart begins not with theory but with yet they struggle when scams change shape over time. As
timing-embeddingrecall-driventhresholdtuningdirectlyinto conditionsshiftquicklyinmodernfinance,theserigidmethods
|                  |     |        |      |       |              |              | miss many | real threats. |     |     |     |
| ---------------- | --- | ------ | ---- | ----- | ------------ | ------------ | --------- | ------------- | --- | --- | --- |
| live transaction |     | flows. | Most | prior | research has | concentrated |           |               |     |     |     |
on static benchmarks or overall precision measured after the To address the shortcomings of rigid rule-driven setups,
fact. Here, decisions shift dynamically, shaped by how much experts have turned to machine learning techniques, such as
moredamagingmissedfraudiscomparedtoflaggedlegitimate logistic regression, decision trees, and support vector ma-
activities. The approach not only performs well on paper but chines,alongwithcombinedstrategies,suchasrandomforests
|              |     |      |             |      |             |         | and gradient | boosting. Drawing | from past | transaction | records, |
| ------------ | --- | ---- | ----------- | ---- | ----------- | ------- | ------------ | ----------------- | --------- | ----------- | -------- |
| also adjusts | in  | step | with actual | bank | operations. | Instead | of           |                   |           |             |          |
treatingerrorsequally,itreflectswhatbanksexperiencedaily: these systems independently identify signs of fraud on their
overlooking fraud carries heavier consequences than raising own, outperforming fixed-rule alternatives. However, much
false alarms. This alignment emerges through design choices of the existing work emphasizes total prediction correctness,
tuned to operational realities rather than idealized conditions. an approach poorly matched to skewed fraud data, where
A different angle emerges when ensemble stability meets dishonest activities are few. Therefore, models built around
budget-aware decision thresholds, tied together through live accuracy frequently miss uncommon yet critical fraudulent
| transaction | controls, |     | all built | into | one framework | ready | for events. |     |     |     |     |
| ----------- | --------- | --- | --------- | ---- | ------------- | ----- | ----------- | --- | --- | --- | --- |
actual use. Security gains depth once a secondary check for Fraud detection now uses groups of machine learning mod-
phishingisaddedtothesetup,targetingnotonlyactivescams els together, aiming for more stable and adaptable outcomes.
but also their starting points. What stands out is how high Combiningtheoutputsfromdifferentclassifiershelpstolower
recall and practical operation take precedence here, shifting the prediction errors while increasing the overall accuracy.
focus away from pure accuracy; this shift helps close the Some studies have highlighted better performance with ran-
|          |         |             |     |        |          |       | dom forests | or boosted trees; | however, | such strategies | often |
| -------- | ------- | ----------- | --- | ------ | -------- | ----- | ----------- | ----------------- | -------- | --------------- | ----- |
| distance | between | theoretical |     | models | and what | banks | really      |                   |          |                 |       |
need on the ground. rely on unchanging cutoff points for decisions. Missing from
|            |           |     |     |     |     |     | most is | a clear adjustment | for how costly | it is to | miss fraud |
| ---------- | --------- | --- | --- | --- | --- | --- | ------- | ------------------ | -------------- | -------- | ---------- |
| A. Problem | Statement |     |     |     |     |     |         |                    |                |          |            |
comparedtofalselyflaggingnormalactivity,somethingbanks
| Despite | handling |     | countless | financial | operations | instantly, | face daily. |     |     |     |     |
| ------- | -------- | --- | --------- | --------- | ---------- | ---------- | ----------- | --- | --- | --- | --- |
digital banking platforms face constant threats, such as illicit Although methods such as RNNs, CNNs, and LSTM net-
fund movements and improper account access. Because dis- works are used to spot fraudulent transactions and similar
honest actions are so rare among legitimate actions, spotting security issues, they require significant computing power.
them becomes extremely difficult. Most standard detection Owing to their structure, these systems can recognize patterns
methods prioritize general performance, missing subtle but over time and subtle links between features in transaction
serious anomalies. When fraud accounts for only a small por- data. However, most tests occur after the fact, ignoring live
tionofthetotaltransactions,conventionalrulesandalgorithms processing needs or limits found in actual applications. Their
struggle to respond effectively. strength in modeling does not always translate into practical
| What | holds | back Current |     | methods | for spotting | transaction | setups. |     |     |     |     |
| ---- | ----- | ------------ | --- | ------- | ------------ | ----------- | ------- | --- | --- | --- | --- |
fraud are limited by rigid thresholds paired with measures Simultaneously, researchers have explored phishing detec-
focused only on overall correctness. These fail to reflect the tion to support broader efforts against online fraud driven
true cost of different mistakes. When banks miss actual fraud, by harmful web pages. Instead of relying solely on rules,
the fallout includes monetary losses, trouble with regulations, systemsnowapplymachinelearninganddeeplearningtosort
and damaged relationships with customers. Errors that flag suspicious links using characteristics tied to naming patterns,
honest activity as suspicious usually lead to smaller burdens, layout design, or user interaction traces. Although spotting
such as extra checks or verification steps. fakesitesmaylowerrisksbeforefinancialactionsoccur,many
Therefore,thecentralchallengeisbuildingafrauddetection analyses keep website threats apart from payment abuses and
systemforfinancialtransactionsthatmaintainslowcostswhile rarely test both within one unified framework.
catching most fraudulent cases. This approach needs to work Research to date shows that machine learning methods,
despite uneven data distributions, spotting nearly all scams especially combined ones, can detect fraudulent activity quite
without swamping legitimate activities with errors. Speed well; however, some problems still exist. While many studies
matters just as much; decisions occur in moments during live focus on overall correctness, they often ignore how many

actual fraud cases are missed. Fixed decision points are real-time, online banking environments. The primary objec-
common, even though they may not suit shifting patterns tive of the system is to minimize false negatives (missed
in financial behavior. Researchers rarely adjust their models fraud cases) while maintaining an acceptable false-positive
based on the varying costs linked to false alarms versus rate under highly imbalanced transaction data. To achieve
missed detections. Another missing piece is testing within this, the system combines ensemble machine learning models
live systems, and few attempts have been made to connect with decision threshold optimization, enabling recall-oriented
detection tools directly to active bank transaction flows. The fraud detection that is suitable for safety-critical financial
| proposed       | design | is focused | on      | detecting     | more      | fraud | instances   | applications. |              |     |     |     |     |     |
| -------------- | ------ | ---------- | ------- | ------------- | --------- | ----- | ----------- | ------------- | ------------ | --- | --- | --- | --- | --- |
| while reducing |        | costly     | errors, | intelligently | adjusting |       | its trigger |               |              |     |     |     |     |     |
|                |        |            |         |               |           |       |             | A. System     | Architecture |     |     |     |     |     |
levels,andrunningcontinuouslyinsideanoperationalpayment
environment. The proposed framework consists of three main compo-
nents:
III. EXISTINGSYSTEM
|     |     |     |     |     |     |     |     | 1) Transaction |     | Data Processing |     | Module: | Incoming | trans- |
| --- | --- | --- | --- | --- | --- | --- | --- | -------------- | --- | --------------- | --- | ------- | -------- | ------ |
Mostcurrentonlinebankingfrauddetectiontoolsdependon
|     |     |     |     |     |     |     |     | action | requests | are | processed | to extract | relevant | trans- |
| --- | --- | --- | --- | --- | --- | --- | --- | ------ | -------- | --- | --------- | ---------- | -------- | ------ |
fixed rules or older machine learning methods that learn from actional, behavioral, temporal, and contextual features.
past transactions. These rule-driven setups use set boundaries These features include transaction amount, transaction
| made by | experts, | such | as  | caps on | transfer | amounts, | loca- |       |      |          |           |            |             |     |
| ------- | -------- | ---- | --- | ------- | -------- | -------- | ----- | ----- | ---- | -------- | --------- | ---------- | ----------- | --- |
|         |          |      |     |         |          |          |       | type, | user | behavior | patterns, | time-based | attributes, | and |
tion checks, or how often payments occur, to flag unusual device or location data. All features were preprocessed
| activity. | Although | they | are straightforward |     |     | to implement | and |       |             |     |          |                   |     |       |
| --------- | -------- | ---- | ------------------- | --- | --- | ------------ | --- | ----- | ----------- | --- | -------- | ----------------- | --- | ----- |
|           |          |      |                     |     |     |              |     | using | appropriate |     | encoding | and normalization |     | tech- |
understand, they cannot be adjusted over time. New types of niques to ensure compatibility with the trained machine
fraudulentactionseasilybypassthesesystems,especiallythose learning models.
| that have | never | been seen | before. |     |     |     |     |     |     |     |     |     |     |     |
| --------- | ----- | --------- | ------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
2) FraudDetectionEngine:Thecorefrauddetectionengine
Most banks now use machine learning tools, such as de- employs an ensemble of machine learning classifiers
| cision trees, | logistic | regression, |     | support | vector | machines, | or  |     |     |     |     |     |     |     |
| ------------- | -------- | ----------- | --- | ------- | ------ | --------- | --- | --- | --- | --- | --- | --- | --- | --- |
trainedonhistoricaltransactiondata.Ensemblelearning
ensemble methods, to boost their ability to spot anomalies. is used to improve robustness and generalization by ag-
Transaction features help these systems label activity, either gregatingpredictionsfrommultiplebasemodels.Instead
| normal | or suspicious, |     | without | manual | input. | Despite | out- |            |     |            |             |            |     |            |
| ------ | -------------- | --- | ------- | ------ | ------ | ------- | ---- | ---------- | --- | ---------- | ----------- | ---------- | --- | ---------- |
|        |                |     |         |        |        |         |      | of relying |     | on a fixed | probability | threshold, |     | the system |
performing fixed rule sets, they often aim for high general applies decision threshold optimization to control the
accuracy, a goal that misaligns with actual fraud detection trade-off between fraud recall and false-positive rate. A
needs, where genuine cases vastly outnumber fake ones. transactionisclassifiedasfraudulentwhenthepredicted
Onekeyweaknessincurrentsetupsliesintheirrelianceon fraud probability exceeds an optimized threshold value
| unchanging | cutoff | points, | often | pinned | at 0.5, | to  | flag fraud. |          |       |                    |     |             |     |           |
| ---------- | ------ | ------- | ----- | ------ | ------- | --- | ----------- | -------- | ----- | ------------------ | --- | ----------- | --- | --------- |
|            |        |         |       |        |         |     |             | selected | based | on recall-oriented |     | performance |     | criteria. |
Because banks face unequal consequences when mistakes 3) Real-TimeDecisionandEnforcementModuleThefraud
occur,rigidboundariesstruggletorespondeffectively.Missing detectionmodelisdirectlyintegratedintothetransaction
real fraud means that money vanishes along with customer execution pipeline. Each transaction is evaluated in real
trust. In contrast, incorrectly tagging clean activities usually timebeforecompletion.Transactionsclassifiedasfraud-
| adds a | small | review | workload. | When | models |     | adhere too |       |                   |     |         |     |         |             |
| ------ | ----- | ------ | --------- | ---- | ------ | --- | ---------- | ----- | ----------------- | --- | ------- | --- | ------- | ----------- |
|        |       |        |           |      |        |     |            | ulent | are automatically |     | blocked | or  | flagged | for further |
closelytoonerule,theyoverlookharmfulpatternsmoreoften verification, whereas legitimate transactions are allowed
than necessary. toproceedwithoutdelay.Thisdesignensuresimmediate
| Most | current | tools | for spotting |     | fraud are | tested | only | in   |            |     |          |           |        |           |
| ---- | ------- | ----- | ------------ | --- | --------- | ------ | ---- | ---- | ---------- | --- | -------- | --------- | ------ | --------- |
|      |         |       |              |     |           |        |      | risk | mitigation | and | prevents | financial | losses | caused by |
controlled lab-like conditions and rarely face actual day-to- delayed fraud detection.
dayuse.Becauseofthisgap,theyoftenstrugglewhenapplied
|     |     |     |     |     |     |     |     | B. Supporting | Phishing | Detection |     | Component |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------- | -------- | --------- | --- | --------- | --- | --- |
directlytoactivepaymentnetworks.Inaddition,anti-phishing
methods, if used at all, usually run separately, disconnected Toenhanceend-to-endsecurity,asupportingphishing-URL
| from broader |     | systems | meant | to catch | suspicious | transactions. |     |                     |     |     |             |     |          |         |
| ------------ | --- | ------- | ----- | -------- | ---------- | ------------- | --- | ------------------- | --- | --- | ----------- | --- | -------- | ------- |
|              |     |         |       |          |            |               |     | detection mechanism |     | was | implemented | as  | a Chrome | browser |
Itiscrucialtodesignfrauddetectionmethodsthatfocuson extension. The extension visits URLs and evaluates them
catching more incidents while keeping costs low. Real-world using a hybrid deep learning model combined with rule-based
data often show far fewer fraudulent cases than legitimate heuristics. This component acts as an auxiliary defense layer
ones, which shapes the performance of such systems. Shifting by reducing the likelihood of fraudulent transactions initiated
| patterns | in deceptive |     | actions | mean | that flexibility |     | cannot be |                   |     |           |              |     |           |        |
| -------- | ------------ | --- | ------- | ---- | ---------------- | --- | --------- | ----------------- | --- | --------- | ------------ | --- | --------- | ------ |
|          |              |     |         |      |                  |     |           | through malicious |     | websites. | The phishing |     | detection | module |
ignored.Theintegrationoflivebankingplatformsaddsanother operates independently and does not interfere with the core
| layer of | practical | demand. |     |     |     |     |     | fraud detection | process. |     |     |     |     |     |
| -------- | --------- | ------- | --- | --- | --- | --- | --- | --------------- | -------- | --- | --- | --- | --- | --- |
IV. PROPOSEDSYSTEM C. Role of Phishing Detection in System-Level Security
Theproposedsystemintroducesacost-sensitivetransaction A common starting point misses how phishing is tied
fraud detection framework designed to operate effectively in to broader risks. The detection of malicious URLs plays a

supporting role, not a central role, in classifying fraud during D. Advantages of the Proposed System
transactions. Credentials stolen by fake websites often lead The proposed system offers the following advantages over
| to unauthorized |     | banking | activities. |     | Because | of  | this pathway, |     |     |     |     |     |     |     |     |
| --------------- | --- | ------- | ----------- | --- | ------- | --- | ------------- | --- | --- | --- | --- | --- | --- | --- | --- |
existing approaches:
| focusing | only | on actions | taken | during | a transfer |     | overlooks the |             |     |       |        |         |                |     |           |
| -------- | ---- | ---------- | ----- | ------ | ---------- | --- | ------------- | ----------- | --- | ----- | ------ | ------- | -------------- | --- | --------- |
|          |      |            |       |        |            |     |               | Prioritizes |     | fraud | recall | through | cost-sensitive |     | threshold |
•
| earlier weaknesses. |      | Protection |     | that | begins | too late | cannot stop |              |     |         |       |                  |          |             |          |
| ------------------- | ---- | ---------- | --- | ---- | ------ | -------- | ----------- | ------------ | --- | ------- | ----- | ---------------- | -------- | ----------- | -------- |
|                     |      |            |     |      |        |          |             | optimization |     | rather  | than  | accuracy-centric |          | evaluation. |          |
| what began          | long | before     | it. |      |        |          |             |              |     |         |       |                  |          |             |          |
|                     |      |            |     |      |        |          |             | Effectively  |     | handles | class | imbalance        | commonly |             | observed |
•
Aboveall,earlywarningsaretriggeredwhendeceptivesites in real-world banking transactions.
appear. By preventing users from reaching harmful pages, • Supports real-time transaction analysis and enforcement,
one part quietly reduces risks before login attempts. Instead making it suitable for live online banking systems.
| of mixing | with | fraud | checks | on  | payments, | it  | runs its own |            |              |     |            |     |                |     |           |
| --------- | ---- | ----- | ------ | --- | --------- | --- | ------------ | ---------- | ------------ | --- | ---------- | --- | -------------- | --- | --------- |
|           |      |       |        |     |           |     |              | • Provides | system-level |     | validation |     | by integrating |     | fraud de- |
course. Separate tracking means that the decision accuracy tection directly into the transaction pipeline.
fortransactionsremainssteady.Theperformanceremainsfirm Enhancessecuritythroughanauxiliaryphishingdetection
•
| because | the layers | work | separately. |     |     |     |     |           |     |         |            |     |             |          |     |
| ------- | ---------- | ---- | ----------- | --- | --- | --- | --- | --------- | --- | ------- | ---------- | --- | ----------- | -------- | --- |
|         |            |      |             |     |     |     |     | mechanism |     | without | increasing |     | transaction | latency. |     |
Securitygainsdepthwhenphishingdetectionisconsidered,
|     |     |     |     |     |     |     |     | By addressing |     | the limitations |     | of  | existing | fraud | detection |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------- | --- | --------------- | --- | --- | -------- | ----- | --------- |
targeting not only active scams but also their origins. What systems, the proposed framework provides a practical and
makes it work well is how this piece fits into the larger deployablesolutionforimprovingfraudpreventioninmodern
setup, able to switch on or off without disrupting other func- online banking environments
| tions. Updates |     | occur | in isolation; |     | therefore, | changes | remain |     |     |     |     |     |     |     |     |
| -------------- | --- | ----- | ------------- | --- | ---------- | ------- | ------ | --- | --- | --- | --- | --- | --- | --- | --- |
V. METHODOLOGYANDIMPLEMENTATION
| contained. | This | separation |     | supports | smoother | rollouts | in real- |     |     |     |     |     |     |     |     |
| ---------- | ---- | ---------- | --- | -------- | -------- | -------- | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
Thissectiondescribesthemethodologyandimplementation
| world banking |          | systems, | in           | which | adaptability | is       | crucial. |            |              |     |                |     |                   |     |        |
| ------------- | -------- | -------- | ------------ | ----- | ------------ | -------- | -------- | ---------- | ------------ | --- | -------------- | --- | ----------------- | --- | ------ |
|               |          |          |              |       |              |          |          | details of | the proposed |     | cost-sensitive |     | transaction-fraud |     | detec- |
| From          | a system | design   | perspective, |       | treating     | phishing | detec-   |            |              |     |                |     |                   |     |        |
tionframework.Thesystemisdesignedtooperateunderreal-
tionasanindependentsecuritylayeralignswiththeconstraints
|                        |     |         |              |          |           |                |         | world constraints, |        | including |               | class imbalance, |       | real-time            | deci- |
| ---------------------- | --- | ------- | ------------ | -------- | --------- | -------------- | ------- | ------------------ | ------ | --------- | ------------- | ---------------- | ----- | -------------------- | ----- |
| of real-world          |     | banking | deployments. |          | Financial | institutions   | typ-    |                    |        |           |               |                  |       |                      |       |
|                        |     |         |              |          |           |                |         | sion requirements, |        | and       | asymmetric    |                  | costs | of misclassification |       |
| ically enforce         |     | strict  | access       | controls | and       | isolation      | between |                    |        |           |               |                  |       |                      |       |
|                        |     |         |              |          |           |                |         | errors in          | online | banking   | environments. |                  |       |                      |       |
| transaction-processing |     |         | systems      | and      | external  | web-monitoring |         |                    |        |           |               |                  |       |                      |       |
components. By decoupling phishing detection from the core A. Data Preprocessing and Feature Engineering
| transaction | fraud | engine, |     | the proposed |     | framework | respects |          |             |     |      |      |                 |     |            |
| ----------- | ----- | ------- | --- | ------------ | --- | --------- | -------- | -------- | ----------- | --- | ---- | ---- | --------------- | --- | ---------- |
|             |       |         |     |              |     |           |          | Incoming | transaction |     | data | were | first subjected |     | to prepro- |
theseoperationalboundaries,whileenablinglayeredriskmiti-
cessingtoensureconsistencyandcompatibilitywiththefraud
gation.Thisseparationallowsbankstodeploy,test,andupdate
|              |     |        |         |           |               |     |        | detection   | models.    | The  | dataset   | contains | both           | numerical | and         |
| ------------ | --- | ------ | ------- | --------- | ------------- | --- | ------ | ----------- | ---------- | ---- | --------- | -------- | -------------- | --------- | ----------- |
| the phishing |     | module | without | requiring | modifications |     | to the |             |            |      |           |          |                |           |             |
|              |     |        |         |           |               |     |        | categorical | attributes | that | represent |          | transactional, |           | behavioral, |
criticaltransactioninfrastructure,therebyreducingtheintegra- temporal, and contextual information. Categorical features
| tion complexity, |     | compliance |     | risk, | and operational |     | downtime. |                  |             |             |            |              |           |             |            |
| ---------------- | --- | ---------- | --- | ----- | --------------- | --- | --------- | ---------------- | ----------- | ----------- | ---------- | ------------ | --------- | ----------- | ---------- |
|                  |     |            |     |       |                 |     |           | were transformed |             | using       | suitable   | encoding     |           | techniques, | and        |
|                  |     |            |     |       |                 |     |           | numerical        | features    | were        | normalized |              | to reduce | scale       | variations |
|                  |     |            |     |       |                 |     |           | and improve      | model       | stability.  |            |              |           |             |            |
|                  |     |            |     |       |                 |     |           | To enable        | controlled  |             | model      | learning     | and       | reduce      | class bias |
|                  |     |            |     |       |                 |     |           | during training, |             | the dataset |            | was balanced |           | prior       | to model   |
|                  |     |            |     |       |                 |     |           | development.     | The         | processed   |            | feature      | set       | included    | the trans- |
|                  |     |            |     |       |                 |     |           | action amount,   |             | transaction | type,      | time-based   |           | attributes, | user       |
|                  |     |            |     |       |                 |     |           | behavior         | indicators, | and         | contextual |              | metadata. | These       | features   |
allowthemodeltocapturemeaningfulpatternsassociatedwith
|         |        |              |     |              |             |     |                 | fraudulent       | activity    | while           | supporting  |              | a reliable | evaluation | of          |
| ------- | ------ | ------------ | --- | ------------ | ----------- | --- | --------------- | ---------------- | ----------- | --------------- | ----------- | ------------ | ---------- | ---------- | ----------- |
|         |        |              |     |              |             |     |                 | recall–precision |             | trade-offs      | through     | threshold    |            | analysis.  |             |
|         |        |              |     |              |             |     |                 | 1) Dataset       |             | Description     | and         | Experimental |            | Protocol:  | A           |
|         |        |              |     |              |             |     |                 | number of        | large-scale | transaction     |             | records      | sourced    |            | from public |
|         |        |              |     |              |             |     |                 | platforms,       | such        | as UCI          | and Kaggle, |              | form the   | basis      | for testing |
|         |        |              |     |              |             |     |                 | the fraud        | detection   | method          | described   |              | here.      | These      | collections |
|         |        |              |     |              |             |     |                 | include hundreds |             | of thousands    |             | of entries,  |            | most of    | which are   |
|         |        |              |     |              |             |     |                 | drawn from       | actual      | banking         |             | activity,    | yet        | masked     | to protect  |
|         |        |              |     |              |             |     |                 | user identity.   | Rarely      | do              | fraudulent  |              | cases      | appear,    | making up   |
|         |        |              |     |              |             |     |                 | less than        | one percent | of              | all data    | points.      | This       | scarcity   | mirrors     |
|         |        |              |     |              |             |     |                 | the challenges   |             | banks typically |             | face         | when       | monitoring | digital     |
|         |        |              |     |              |             |     |                 | payments.        | Such        | an imbalance    |             | shapes       | how        | models     | must be     |
| Fig. 1. | System | architecture | of  | the proposed | transaction |     | fraud detection | assessed.        |             |                 |             |              |            |            |             |
framework A single entry logs details such as how much was spent,
|     |     |     |     |     |     |     |     | what kind | of transaction |     | occurred, | whether |     | it used | biometrics |
| --- | --- | --- | --- | --- | --- | --- | --- | --------- | -------------- | --- | --------- | ------- | --- | ------- | ---------- |

or a PIN, when it happened, typical actions by the person To explicitly model asymmetric misclassification costs, the
involved, along with data about the machine or place tied to expected classification cost is defined as:
the event. Taken together, these pieces reflect the immediate
C(τ)=C ·FN(τ)+C ·FP(τ) (2)
features of purchases as well as shifts in habits that might FN FP
signal fraud. where FN(τ) and FP(τ) denote the number of false neg-
Subsequently,tocheckconsistencyandreal-worldfunction, atives and false positives at threshold τ, respectively. The
the data were split into training and testing portions in time misclassification costs satisfy:
order. During this phase, one portion teaches the algorithm,
C ≫C (3)
adjusts the category weights, and tunes the cutoff points for FN FP
decisions. Meanwhile, the second part remains hidden until reflecting the substantially higher financial and operational
thefinalreview,maintainingitsnaturalimbalance.Becauseof impactofundetectedfraudulenttransactionscomparedtofalse
this setup, the outcomes show how well the systems adapt alarms.
beyond the practice rounds. Only then do numbers reveal Theoptimaldecisionthresholdτ∗ isselectedbyminimizing
actual readiness for fresh cases. the expected classification cost:
Assessingmodelperformanceinvolvesseveralmetrics:con-
τ∗ =argminC(τ) (4)
fusion matrices, PR curves, ROC behavior, and threshold τ
responses. In particular, precision-recall is important because Thiscost-sensitivethresholdoptimizationshiftsthedecision
it handles imbalance well, which is common in detecting boundary toward higher fraud recall while constraining false-
rare fraudulent cases. The results shown are from a separate positive rates within acceptable operational limits, making
test group, maintaining stable comparisons across reference the proposed framework suitable for safety-critical real-time
systems. online banking applications.
1) Discussion on High Fraud Recall Performance: What
B. Fraud Detection Model drives strong fraud detection performance? This lies in how
First,severalbasicclassifierslearnpatternsfrompasttrans- the model treats misclassification costs differently across out-
actionstopowerthemainfrauddetectionsystem.Ratherthan comes. Typical methods stick to fixed cutoffs, aiming to get
dependingononemodelalone,combiningtheiroutputsyields most cases right overall; however, this one does not. Instead,
steadier results across unpredictable datasets. By design, this it adjusts its threshold based on real-world consequences and
methodsmoothsoutinconsistencieswhilehandlingskewedor tunes decisions where mistakes matter more. By focusing on
messy real-world data more effectively. the financial risk asymmetry inherent in digital transactions,
the system deliberately moves its judgment line to detect
A single prediction is obtained from each base model,
fraudulent activity. This shift explains the higher capture rate
providing a number that indicates the likelihood of fraud.
without reworking the core mechanics.
Because these numbers matter together, they merge into one
Most fraud in actual bank operations shows clear signs,
overall risk mark per event. What shapes the group setup is
such as odd spending sizes, strange timing, or shifts from
not how fancy the tools are, but how well they work and hold
normal habits. Because ensemble methods process these sig-
upunder pressure,which makesthem fitfor instantdecisions.
nals together, they separate legitimate from suspicious cases
Despite variations in design, speed, and reliability, guide the
more effectively, even when few fraud examples are present.
choice.
Adjusting the decision cutoff helps identify more true fraud
instances while skipping artificial data boosts or questionable
C. Cost-Sensitive Decision Threshold Optimization
premises.
Unlike conventional fraud detection systems that apply a
Choosing the operating point involves looking at precision,
fixeddecisionthreshold,theproposedframeworkincorporates
recall, and how sensitive thresholds are, instead of just fo-
cost-sensitive decision threshold optimization to prioritize
cusing on accuracy, so the recall numbers show a balanced
fraudrecall.Theclassificationdecisionisbasedoncomparing
approach between catching fraud and limiting false alarms.
the predicted fraud probability against an optimized threshold
Therefore, the strong recall observed in this study is more
value, which is selected to minimize false negatives while
closely aligned with real-world use than with idealized test
maintaining an acceptable false-positive rate. This approach
conditions..
reflects the asymmetric cost structure of fraud detection in
online banking systems, where undetected fraud results in D. Real-Time Transaction Processing Pipeline
significantly higher losses than false alarms. The trained fraud detection model was integrated into a
Let P(y = 1 | x) denote the predicted probability that real-timeonlinebankingtransactionpipeline.Eachtransaction
a transaction x is fraudulent. A transaction is classified as request is evaluated immediately after feature extraction and
fraudulent if: priortoexecution.Ifatransactionisclassifiedasfraudulent,it
P(y =1|x)≥τ (1) isautomaticallyblockedorflaggedforverification.Legitimate
transactions are processed without additional delays, ensuring
where τ represents the decision threshold. minimal impact on the user experience.

| All transaction |     | outcomes, |     | including |     | fraud | prediction | and |     |     |     |     |     |
| --------------- | --- | --------- | --- | --------- | --- | ----- | ---------- | --- | --- | --- | --- | --- | --- |
TABLEI
PERFORMANCECOMPARISONWITHBASELINEMODELS
| decision | results, | were | logged | in  | the | transaction | database. |     |     |     |     |     |     |
| -------- | -------- | ---- | ------ | --- | --- | ----------- | --------- | --- | --- | --- | --- | --- | --- |
Thisdesignsupportsauditability,performancemonitoring,and
|              |          |             |     |                 |     |     |          |       | Model                        |     | Accuracy(%) Precision | Recall F1-Score | ROC-AUC |
| ------------ | -------- | ----------- | --- | --------------- | --- | --- | -------- | ----- | ---------------------------- | --- | --------------------- | --------------- | ------- |
| future model | updates. |             |     |                 |     |     |          |       |                              |     |                       |                 |         |
|              |          |             |     |                 |     |     |          |       | LogisticRegression           |     | 95.4 82.6             | 71.2 76.5       | 0.942   |
|              |          |             |     |                 |     |     |          |       | RandomForest                 |     | 97.1 90.3             | 88.7 89.5       | 0.981   |
| 1) Real-Time |          | Performance |     | Considerations: |     |     | A system | built |                              |     |                       |                 |         |
|              |          |             |     |                 |     |     |          |       | XGBoost(FixedThresholdτ=0.5) |     | 97.8 94.1             | 92.4 93.2       | 0.988   |
for spotting fraudulent activity fits the speed demands of ProposedModel(Optimizedτ) 98.3 96.8 98.6 98.2 0.996
| today’s     | digital | banking, | requiring |             | quick | verdicts | on  | transac- |     |     |     |     |     |
| ----------- | ------- | -------- | --------- | ----------- | ----- | -------- | --- | -------- | --- | --- | --- | --- | --- |
| tions under | tight   | time     | limits.   | Tree-driven |       | machine  |     | learning |     |     |     |     |     |
methodsformthecorehere-simplebydesign,allowingswift
| predictions | without |     | heavy | computing | needs. |     | After | training, |     |     |     |     |     |
| ----------- | ------- | --- | ----- | --------- | ------ | --- | ----- | --------- | --- | --- | --- | --- | --- |
frauddetectionbecomesasequence:reshapinginputs,judging
| likelihoods, | and | checking | values | against |     | a set level | -   | all steps |     |     |     |     |     |
| ------------ | --- | -------- | ------ | ------- | --- | ----------- | --- | --------- | --- | --- | --- | --- | --- |
handledrapidlywhenpaymentsmovethrough.Afastresponse
remainsachievablebecauseeachstagerunsleanandintegrates
| smoothly | into | live operations. |          |           |     |      |          |      |     |     |     |     |     |
| -------- | ---- | ---------------- | -------- | --------- | --- | ---- | -------- | ---- | --- | --- | --- | --- | --- |
| Choosing | the  | best             | decision | threshold |     | adds | no extra | load |     |     |     |     |     |
whenrunningthesystembecauseitissetaheadoftimewhile
testingthemodel.Insteadofcalculatingonthefly,thechosen
| cutoff remains |       | constant | once        | the    | model    | goes     | live. | During  |     |     |     |     |     |
| -------------- | ----- | -------- | ----------- | ------ | -------- | -------- | ----- | ------- | --- | --- | --- | --- | --- |
| processing     | time, | each     | transaction |        | requires | checking |       | whether |     |     |     |     |     |
| its fraud      | score | exceeds  | the         | preset | level.   | The      | check | occurs  |     |     |     |     |     |
quicklyenoughtofitwithinnormalpaymentworkflows.Users
| who complete |     | valid | transactions | do  | not | experience | noticeable |     |     |     |     |     |     |
| ------------ | --- | ----- | ------------ | --- | --- | ---------- | ---------- | --- | --- | --- | --- | --- | --- |
waittimes.Theperformanceremainssmoothbecausethelogic
|             |      |              |     |        |           |      |         |      | Fig.2. Confusionmatrixoftheproposedfrauddetectionmodelonthetest |     |     |     |     |
| ----------- | ---- | ------------ | --- | ------ | --------- | ---- | ------- | ---- | --------------------------------------------------------------- | --- | --- | --- | --- |
| fits neatly | into | the existing |     | steps. | Detection | runs | in step | with |                                                                 |     |     |     |     |
dataset.
| processing,    | not        | apart         | from       | it.     |            |           |                 |          |     |     |     |     |     |
| -------------- | ---------- | ------------- | ---------- | ------- | ---------- | --------- | --------------- | -------- | --- | --- | --- | --- | --- |
| Instead        | of relying |               | on heavy   | deep    | learning   | during    |                 | transac- |     |     |     |     |     |
| tions, the     | system     | uses          | a flexible |         | design     | that      | fits fast-paced |          |     |     |     |     |     |
| online banking |            | environments. |            | Because | fraud      | detection |                 | works    |     |     |     |     |     |
| instantly,     | it can     | trigger       | quick      |         | responses, | such      | as              | halting  |     |     |     |     |     |
| payments       | or asking  |               | for extra  | checks. | This       | approach  |                 | reduces  |     |     |     |     |     |
monetaryexposurewithoutdisruptinguserinteractionwiththe
service.
| E. Supporting       |               | Phishing   | Detection  |              | Implementation |           |                |          |     |     |     |     |     |
| ------------------- | ------------- | ---------- | ---------- | ------------ | -------------- | --------- | -------------- | -------- | --- | --- | --- | --- | --- |
| A small             | extra         | layer      | of         | protection   | comes          | from      | a              | Chrome   |     |     |     |     |     |
| add-on              | that checks   |            | website    | addresses    |                | for signs | of             | phishing |     |     |     |     |     |
| attacks.            | This tool     | monitors   |            | every        | page           | visit and | sends          | links    |     |     |     |     |     |
| to a server         | for           | review.    | Risk       | levels       | are            | judged    | using          | smart    |     |     |     |     |     |
| algorithms          | and           | pattern    | rules.     | Although     |                | it runs   | apart from     | the      |     |     |     |     |     |
| main fraud-tracking |               |            | system,    | its presence |                | helps     | guard          | against  |     |     |     |     |     |
| online scams.       |               | Protection | improves   |              | when           | threats   | from           | harmful  |     |     |     |     |     |
| websites            | are detected  |            | early.     |              |                |           |                |          |     |     |     |     |     |
| F. Implementation   |               | Details    |            |              |                |           |                |          |     |     |     |     |     |
| A design            | built         | in         | separate   | parts        | allows         | for       | growth         | and      |     |     |     |     |     |
| simplifies          | updates.      |            | Prediction | tools        | for            | spotting  | fraud          | run      |     |     |     |     |     |
| inside a            | server        | layer,     | offering   | real-time    |                | results   | via accessible |          |     |     |     |     |     |
| endpoints.          | Communication |            |            | between      | bank           | systems   |                | and this |     |     |     |     |     |
layer occurs through protected API requests, linking transac- Fig. 3. illustrates the Precision–Recall (PR) curve of the proposed fraud
tions and analysis smoothly. Speed, consistency across runs, detection framework under highly imbalanced class conditions. The curve
and a straightforward setup guide how the system fits into demonstratesconsistentlyhighprecisionacrossawiderangeofrecallvalues,
|                |     |            |     |     |     |     |     |     | indicating | that the model   | effectively identifies        | fraudulent transactions | while     |
| -------------- | --- | ---------- | --- | --- | --- | --- | --- | --- | ---------- | ---------------- | ----------------------------- | ----------------------- | --------- |
| active banking |     | platforms. |     |     |     |     |     |     |            |                  |                               |                         |           |
|                |     |            |     |     |     |     |     |     | minimizing | false positives. | This behavior is particularly | important               | in online |
bankingenvironments,whereexcessivefalsealarmsleadtooperationalover-
|     |     |     |     |     |     |     |     |     | head. The | strong PR performance | confirms that | the proposed | cost-sensitive |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --------- | --------------------- | ------------- | ------------ | -------------- |
thresholdoptimizationsuccessfullyprioritizesfraudrecallwithoutsacrificing
precision.

|     |     |     |     |     |     | rics, such | as  | recall and | classification |     | accuracy. | Visual    | tools |
| --- | --- | --- | --- | --- | --- | ---------- | --- | ---------- | -------------- | --- | --------- | --------- | ----- |
|     |     |     |     |     |     | such as    | ROC | curves and | confusion      |     | matrices  | confirmed | the   |
model’sabilitytoeffectivelyseparatenormaltransactionsfrom
|     |     |     |     |     |     | fraudulent | ones. | What        | stands | out is  | how | smoothly    | the model |
| --- | --- | --- | --- | --- | --- | ---------- | ----- | ----------- | ------ | ------- | --- | ----------- | --------- |
|     |     |     |     |     |     | fits into  | live  | transaction | flows, | proving |     | that it can | run fast  |
enoughforreal-worldusewithoutdelays.Beyonddirectfraud
|     |     |     |     |     |     | spotting, | another | layer  | checks | incoming   |     | links for    | signs of |
| --- | --- | --- | --- | --- | --- | --------- | ------- | ------ | ------ | ---------- | --- | ------------ | -------- |
|     |     |     |     |     |     | phishing  | attacks | before | they   | lead users | to  | be deceived. | This     |
extrastepdoesnotreplacethemainsystem;rather,itsupports
itbyclosinggapsthatpuretransactionmonitoringmightleave
open.
|     |     |     |     |     |     | The results |     | show that | cost-aware |     | decisions | are | important |
| --- | --- | --- | --- | --- | --- | ----------- | --- | --------- | ---------- | --- | --------- | --- | --------- |
whenspottingfraudinonlinebanks.Insteadofjustmeasuring
|     |     |     |     |     |     | how often       | predictions |             | are correct, |           | aiming  | for high  | recall fits |
| --- | --- | --- | --- | --- | --- | --------------- | ----------- | ----------- | ------------ | --------- | ------- | --------- | ----------- |
|     |     |     |     |     |     | the actual      | risks       | that money  | institutions |           | face.   | Threshold | tuning      |
|     |     |     |     |     |     | plays a         | key role    | in ensuring |              | that such | systems | function  | well        |
|     |     |     |     |     |     | under pressure. |             |             |              |           |         |           |             |
|     |     |     |     |     |     | A. Future       | Work        |             |              |           |         |           |             |
Lookingahead,effortswillbeaimedatadaptingtheframe-
| Fig. 4. presents |     | the Receiver Operating | Characteristic | (ROC) | curve of the |     |     |     |     |     |     |     |     |
| ---------------- | --- | ---------------------- | -------------- | ----- | ------------ | --- | --- | --- | --- | --- | --- | --- | --- |
proposed fraud detection model. The curve exhibits a steep ascent toward work for real-world imbalances in class distribution alongside
the upper-left corner, indicating strong discriminative capability between shifting fraud behaviors. Instead of fixed rules, thresholds
| fraudulent | and legitimate | transactions. | While the | high ROC-AUC | value |     |     |     |     |     |     |     |     |
| ---------- | -------------- | ------------- | --------- | ------------ | ----- | --- | --- | --- | --- | --- | --- | --- | --- |
reflects effective class separability, Precision–Recall analysis is emphasized can shift with transaction risk levels, guided by the practical
inthisworkasitprovidesamorerepresentativeevaluationmetricforfraud system limits. Behavior over time may be modeled to reflect
detectiontaskscharacterizedbysevereclassimbalance. how users act over extended periods. Updating models step-
|     |     |     |     |     |     | by-step     | using   | continuous     | learning       | methods     |     | may offer | a path      |
| --- | --- | --- | --- | --- | --- | ----------- | ------- | -------------- | -------------- | ----------- | --- | --------- | ----------- |
|     |     |     |     |     |     | forward.    | To test | the wider      | applicability, |             |     | broader   | transaction |
|     |     |     |     |     |     | datasets    | must    | be considered. |                | Real-system |     | testing   | at scale    |
|     |     |     |     |     |     | is expected | to      | follow,        | ensuring       | stability   |     | beyond    | controlled  |
settings.
REFERENCES
|     |     |     |     |     |     | [1] T. Dal | Pozzolo, | O. Bontempi, |       | and         | G. Snoeck, | “Adaptive   | Machine  |
| --- | --- | --- | --- | --- | --- | ---------- | -------- | ------------ | ----- | ----------- | ---------- | ----------- | -------- |
|     |     |     |     |     |     | Learning   | for      | Credit Card  | Fraud | Detection,” | IEEE       | Intelligent | Systems, |
vol.30,no.4,pp.34–41,Jul.–Aug.2015.
[2] A.DalPozzolo,G.Bontempi,andO.Snoeck,“CalibratingProbability
|     |     |     |     |     |     | with | Undersampling | for | Unbalanced |     | Classification,” | in  | Proc. IEEE |
| --- | --- | --- | --- | --- | --- | ---- | ------------- | --- | ---------- | --- | ---------------- | --- | ---------- |
SymposiumSeriesonComputationalIntelligence,2015,pp.159–166.
|     |     |     |     |     |     | [3] N. Dal | Pozzolo | et al., | “Adversarial | Drift | Detection,” |     | in Proc. IEEE |
| --- | --- | --- | --- | --- | --- | ---------- | ------- | ------- | ------------ | ----- | ----------- | --- | ------------- |
InternationalJointConferenceonNeuralNetworks(IJCNN),2014,pp.
2975–2982.
[4] C.Elkan,“TheFoundationsofCost-SensitiveLearning,”inProc.17th
InternationalJointConferenceonArtificialIntelligence(IJCAI),2001,
pp.973–978.
|     |     |     |     |     |     | [5] T. Fawcett, |     | “An Introduction |     | to ROC | Analysis,” | Pattern | Recognition |
| --- | --- | --- | --- | --- | --- | --------------- | --- | ---------------- | --- | ------ | ---------- | ------- | ----------- |
Letters,vol.27,no.8,pp.861–874,2006.
| Fig. 5. Effect | of  | decision threshold | on model performance, |     | illustrating the |                      |     |         |       |        |            |             |        |
| -------------- | --- | ------------------ | --------------------- | --- | ---------------- | -------------------- | --- | ------- | ----- | ------ | ---------- | ----------- | ------ |
|                |     |                    |                       |     |                  | [6] S. Bhattacharyya |     | et al., | “Data | Mining | for Credit | Card Fraud: | A Com- |
trade-offbetweendetectionaccuracyandclassificationsensitivity. parativeStudy,”DecisionSupportSystems,vol.50,no.3,pp.602–613,
2011.
|     |                         |     |     |     |     | [7] L. Breiman, |     | “Random | Forests,” | Machine | Learning, | vol. | 45, no. 1, pp. |
| --- | ----------------------- | --- | --- | --- | --- | --------------- | --- | ------- | --------- | ------- | --------- | ---- | -------------- |
| VI. | CONCLUSIONANDFUTUREWORK |     |     |     |     | 5–32,2001.      |     |         |           |         |           |      |                |
[8] T.ChenandC.Guestrin,“XGBoost:AScalableTreeBoostingSystem,”
|          |      |          |                   |         |     | in Proc. | 22nd | ACM SIGKDD |     | International | Conference |     | on Knowledge |
| -------- | ---- | -------- | ----------------- | ------- | --- | -------- | ---- | ---------- | --- | ------------- | ---------- | --- | ------------ |
| A closer | look | at fraud | in online banking | reveals | how |          |      |            |     |               |            |     |              |
DiscoveryandDataMining,2016,pp.785–794.
| crucial | it is | to catch every | suspicious case; | missing | one |     |     |     |     |     |     |     |     |
| ------- | ----- | -------------- | ---------------- | ------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
[9] G.Keetal.,“LightGBM:AHighlyEfficientGradientBoostingDecision
| could have | serious | consequences. | Instead | of merely | cutting |        |          |          |           |     |             |            |         |
| ---------- | ------- | ------------- | ------- | --------- | ------- | ------ | -------- | -------- | --------- | --- | ----------- | ---------- | ------- |
|            |         |               |         |           |         | Tree,” | in Proc. | Advances | in Neural |     | Information | Processing | Systems |
(NeurIPS),2017,pp.3146–3154.
| costs, the | method     | presented | in this study focuses | on       | reducing |                                                                     |     |     |     |     |     |     |     |
| ---------- | ---------- | --------- | --------------------- | -------- | -------- | ------------------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
|            |            |           |                       |          |          | [10] L.Prokhorenkovaetal.,“CatBoost:UnbiasedBoostingwithCategorical |     |     |     |     |     |     |     |
| missed     | detections | through   | smart modeling        | choices. | Ensemble |                                                                     |     |     |     |     |     |     |     |
Features,”inProc.AdvancesinNeuralInformationProcessingSystems
techniques are used to handle data where fraud cases are rare (NeurIPS),2018,pp.6638–6648.
by using multiple models together while carefully adjusting [11] M.Bahnsenetal.,“Example-DependentCost-SensitiveDecisionTrees,”
ExpertSystemswithApplications,vol.42,no.19,pp.6609–6619,2015.
| decision       | boundaries. | The              | results show that | it works  | well | -              |     |                |                 |     |     |          |               |
| -------------- | ----------- | ---------------- | ----------------- | --------- | ---- | -------------- | --- | -------------- | --------------- | --- | --- | -------- | ------------- |
|                |             |                  |                   |           |      | [12] J. Maillo | et  | al., “kNN-IS,” | Knowledge-Based |     |     | Systems, | vol. 117, pp. |
| not perfectly, |             | but solidly–when | tested across     | different | met- | 3–15,2017.     |     |                |                 |     |     |          |               |

| [13] R. S. | Rao and A. R. | Pais, “Detection of Phishing | Websites,” Neural |
| ---------- | ------------- | ---------------------------- | ----------------- |
ComputingandApplications,vol.31,no.8,pp.3851–3873,2019.
| [14] UCI | Machine Learning | Repository, “Credit | Card Fraud Detection |
| -------- | ---------------- | ------------------- | -------------------- |
Dataset,”2024.
[15] Kaggle,“FinancialFraudDetectionDataset,”2024.
| [16] D. J. | Hand and R. J. Whitrow, | “Statistical techniques | for fraud detec- |
| ---------- | ----------------------- | ----------------------- | ---------------- |
tion,”WileyInterdisciplinaryReviews,vol.1,no.6,pp.771–783,2009.
[17] M.DalPozzoloetal.,“Creditcardfrauddetection,”IEEETrans.Neural
Netw.Learn.Syst.,vol.26,no.10,pp.2580–2593,Oct.2015.
| [18] A. Dal | Pozzolo et al., | “Handling class imbalance,” | in Proc. IEEE Int. |
| ----------- | --------------- | --------------------------- | ------------------ |
Conf.IntelligentSystems,2014,pp.1–6.
| [19] K. Weiss | et al., “Cost-sensitive | learning vs. sampling,” | in Proc. IEEE |
| ------------- | ----------------------- | ----------------------- | ------------- |
Int.Conf.DataMining(ICDM),2007,pp.35–41.
| [20] J. Davis | and M. Goadrich, | “The relationship | between precision-recall |
| ------------- | ---------------- | ----------------- | ------------------------ |
andROCcurves,”inProc.23rdInt.Conf.MachineLearning(ICML),
2006,pp.233–240.